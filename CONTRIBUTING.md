# Contributing

Contributions from people and coding agents are welcome through pull requests.

## Setup

```bash
git clone https://github.com/PGraeff/frontend-design-pro-agent-skill.git
cd frontend-design-pro-agent-skill
python scripts/validate_repo.py
```

No Python packages are required for the skill or its validation suite.

## Branches

Use one focused branch per change:

- `feat/<description>` for new behavior or design intelligence.
- `fix/<description>` for defects.
- `docs/<description>` for maintainer documentation.
- `agent/<description>` for changes prepared by a coding agent.

External contributors normally create the branch in a fork and open a pull request against `main`.

## What to change

- Edit the installable skill under `skills/frontend-design-pro/`.
- Keep repository-only documentation and automation outside the skill folder.
- Add focused tests for search, persistence, parsing, or packaging behavior.
- Keep guidance concise and remove duplication before adding more context.
- Update attribution files before introducing third-party material.

## Required checks

Run these from the repository root:

```bash
python scripts/validate_repo.py
python scripts/package_skill.py
npx skills add . --list
```

The pull request must also pass the `Validate` GitHub Actions workflow on Linux and Windows.

## Pull requests

Describe:

- The problem and intended behavior.
- The files and behavior changed.
- Validation commands and results.
- Any compatibility or licensing impact.

Keep pull requests narrow enough to review without unrelated cleanup. By submitting a contribution, you agree that your original contribution is licensed under Apache License 2.0. Existing third-party components remain under their stated licenses.
