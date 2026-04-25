# Contributing to Prompt Studio

## Quick Links

- **GitHub:** https://github.com/utk2103/Prompt-Studio
- **X/Twitter:** [@utk2103](https://x.com/utk2103)

## Maintainers

- **Utkarsh Upadhyay** — Core, API, Frontend, Prompt Engine
  - GitHub: [@utk2103](https://github.com/utk2103) · X: [@utk2103](https://x.com/utk2103)

## How to Contribute

1. **Bugs & small fixes** → Open a PR!
2. **New features / architecture** → Open a [GitHub Issue](https://github.com/utk2103/Prompt-Studio/issues/new/choose) first. Large features should be discussed before implementation.
3. **Refactor-only PRs** → Don't open a PR. Not accepted unless a maintainer explicitly requests it as part of a concrete fix.
4. **Test/CI-only PRs for known `main` failures** → Don't open a PR. Known failures are already tracked; PRs that only tweak tests to chase them will be closed.
5. **Questions** → Open a GitHub Issue with the `question` label.

## PR Limits

We cap at **10 open PRs per author**. If you exceed this, the `r: too-many-prs` label is added and your PR is auto-closed.

## Before You PR

- Test locally: start the API with `uvicorn main:app --reload --port 8000` and verify the frontend
- Run `pip install -r requirements.txt` and confirm no import errors
- Keep PRs focused — one concern per PR; do not mix unrelated changes
- Describe what changed and **why**
- Use American English spelling in code, comments, docs, and UI strings
- **Include screenshots** for any UI or visual changes (before/after)
- Ensure CI checks pass

## Review Conversations Are Author-Owned

If a review bot leaves conversations on your PR:

- Resolve them yourself once addressed
- Reply and leave open only when you need maintainer judgment
- Do not leave bot review cleanup for maintainers

## Tech Stack

- **Backend:** FastAPI (Python 3.10+), Pydantic v2
- **Frontend:** Next.js 14+ (App Router), Tailwind CSS, TypeScript
- **Dev:** `uvicorn main:app --reload --port 8000`

## AI/Vibe-Coded PRs Welcome!

Built with Codex, Claude, or other AI tools? **Awesome - just mark it!**

Please include in your PR:

- [ ] Mark as AI-assisted in the PR title or description
- [ ] Note the degree of testing (untested / lightly tested / fully tested)
- [ ] Include prompts or session logs if possible
- [ ] Confirm you understand what the code does
- [ ] Resolve or reply to bot review conversations after you address them

AI PRs are first-class citizens. We just want transparency so reviewers know what to look for.

## Current Focus

- **Prompt scoring accuracy** — improving the 7-dimension analysis engine
- **Model coverage** — adding newer models and updated pricing
- **Wizard UX** — smarter question flows and generated prompt quality
- **Frontend** — migrating to Next.js, improving the terminal UI

Check [GitHub Issues](https://github.com/utk2103/Prompt-Studio/issues) for
[`good first issue`](https://github.com/utk2103/Prompt-Studio/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) labels.

## Report a Vulnerability

Report security issues directly via GitHub:
[utk2103/Prompt-Studio Security](https://github.com/utk2103/Prompt-Studio/security)

### Required in Reports

1. **Title**
2. **Severity Assessment**
3. **Impact**
4. **Affected Component**
5. **Technical Reproduction**
6. **Demonstrated Impact**
7. **Environment**
8. **Remediation Advice**

Reports without reproduction steps, demonstrated impact, and remediation advice will be deprioritized.
