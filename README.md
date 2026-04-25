# PromptStudio 🐖

<div>
  <p>
  AI-powered prompt builder, scorer, validator, and optimizer.
  </p>
  <img src="https://badgen.net/badge/status/Under Development/red?icon=lgtm" alt="">

  ![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen.svg)
  ![License](https://img.shields.io/badge/License-MIT-blue.svg)
  ![Commits](https://img.shields.io/github/commit-activity/m/utk2103/Prompt-Studio)
  ![Repo Size](https://img.shields.io/github/repo-size/utk2103/Prompt-Studio)
  ![Code Size](https://img.shields.io/github/languages/code-size/utk2103/Prompt-Studio)
  ![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)

</div>

<p align="center">
  <img width="320" height="320" src="/public/prompt-studio.png" alt="Material Bread logo" style="margin-right:20px;">
</p>

<hr>

## Quick Start
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
# Docs at http://localhost:8000/docs
```

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/models` | List all supported models |
| POST | `/analyze` | Full analysis: score + issues + tokens + format |
| POST | `/score` | 7-dimension scoring + recommendations |
| POST | `/tokens/count` | Token count + context window + cost |
| POST | `/validate/format` | Format validation + model-native preview |
| POST | `/optimize` | Rule-based prompt improvement |
| POST | `/compare/models` | Cross-model compatibility matrix |
| GET | `/wizard/questions` | Adaptive wizard question set |
| POST | `/wizard/generate` | Build prompt from wizard answers |
| POST | `/prompt/compress` | Token compression pass |
| GET | `/health` | Health check |

## Features sourced from open-source research

- **Scoring engine** — 7-dimension analysis (clarity, specificity, context, format, mode-alignment, token-efficiency, constraints) — inspired by PromptWizard (Microsoft) and promptfoo
- **Rule-based optimizer** — intent-based calibration from AutoPrompt (Eladlev)
- **Token compression** — filler removal without semantic loss, from prompt-optimizer (vaibkumr)
- **Cross-model comparison** — format adaptation matrix from promptfoo
- **Adaptive wizard** — guided Q&A prompt construction, from Promptomatix (Salesforce)
- **Format validation** — model-native wrapping (ChatML, XML Tags, Llama Template)
- **Cost estimation** — per-call USD cost across 7 providers

## Modes
- `TECHNICAL` — Code, systems, analysis
- `CREATIVE` — Narrative, content, ideation
- `SYSTEM` — Persona/instruction prompts for assistants
