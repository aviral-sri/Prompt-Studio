"""Initial schema: prompts + history with pgvector

Revision ID: 001
Revises:
Create Date: 2026-04-25
"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector

revision = "001"
down_revision = None
branch_labels = None
depends_on = None

EMBEDDING_DIM = 1536


def upgrade() -> None:
    # Enable pgvector extension (idempotent)
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")

    op.create_table(
        "prompts",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
        sa.Column("text", sa.Text, nullable=False),
        sa.Column("mode", sa.String(20), nullable=False, server_default="TECHNICAL"),
        sa.Column("model_id", sa.String(50), nullable=False, server_default="claude-3-5"),
        # Score dimensions
        sa.Column("score_overall", sa.Integer, nullable=True),
        sa.Column("score_clarity", sa.Integer, nullable=True),
        sa.Column("score_specificity", sa.Integer, nullable=True),
        sa.Column("score_context", sa.Integer, nullable=True),
        sa.Column("score_format", sa.Integer, nullable=True),
        sa.Column("score_mode_alignment", sa.Integer, nullable=True),
        sa.Column("score_token_efficiency", sa.Integer, nullable=True),
        sa.Column("score_constraints", sa.Integer, nullable=True),
        sa.Column("grade", sa.String(2), nullable=True),
        # JSON blobs
        sa.Column("issues", sa.JSON, nullable=True),
        sa.Column("recommendations", sa.JSON, nullable=True),
        # Vector embedding (NULL until populated)
        sa.Column("embedding", Vector(EMBEDDING_DIM), nullable=True),
        sa.Column("created_at", sa.BigInteger, nullable=False),
    )

    # IVFFlat index for approximate nearest-neighbour search on cosine distance.
    # lists=100 is a reasonable default; tune based on row count (sqrt(n_rows)).
    op.execute(
        "CREATE INDEX IF NOT EXISTS prompts_embedding_idx "
        "ON prompts USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100)"
    )

    op.create_table(
        "history",
        sa.Column("id", sa.String(8), primary_key=True),
        sa.Column("ts", sa.BigInteger, nullable=False),
        sa.Column("prompt_preview", sa.String(200), nullable=False),
        sa.Column("mode", sa.String(20), nullable=False, server_default="TECHNICAL"),
        sa.Column("model_id", sa.String(50), nullable=False, server_default="claude-3-5"),
        sa.Column("score", sa.Integer, nullable=True),
        sa.Column(
            "prompt_id",
            sa.UUID(as_uuid=True),
            sa.ForeignKey("prompts.id", ondelete="SET NULL"),
            nullable=True,
        ),
    )

    op.create_index("history_ts_idx", "history", ["ts"], postgresql_using="btree")


def downgrade() -> None:
    op.drop_index("history_ts_idx", table_name="history")
    op.drop_table("history")
    op.execute("DROP INDEX IF EXISTS prompts_embedding_idx")
    op.drop_table("prompts")
