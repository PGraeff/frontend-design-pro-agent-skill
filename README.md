# Frontend Design Pro

[![Validate](https://github.com/PGraeff/frontend-design-pro-agent-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/PGraeff/frontend-design-pro-agent-skill/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0%20%2B%20MIT-blue.svg)](LICENSE)

Frontend Design Pro is a portable Agent Skill for designing, implementing, reviewing, and polishing production web and mobile interfaces.

It combines four concerns in one workflow:

- Product-specific creative direction instead of generic interface patterns.
- Searchable design intelligence across UX, accessibility, color, typography, motion, charts, and framework guidance.
- A strict UI-copy filter that removes filler, redundant explanations, and implementation commentary from visible interfaces.
- Implementation and verification rules for responsive layouts, interaction states, accessibility, motion, and real-device constraints.

## Install

The repository follows the open Agent Skills folder convention. The installable unit is `skills/frontend-design-pro`.

### Codex

```bash
npx skills add PGraeff/frontend-design-pro-agent-skill --skill frontend-design-pro --global --agent codex --yes --copy
```

Restart Codex after installation. Invoke it explicitly with `$frontend-design-pro`, or let its description trigger automatically for frontend and mobile UI work.

Codex also includes a direct GitHub installer. On macOS or Linux:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo PGraeff/frontend-design-pro-agent-skill \
  --path skills/frontend-design-pro
```

On Windows PowerShell:

```powershell
py -3 "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --repo PGraeff/frontend-design-pro-agent-skill `
  --path skills/frontend-design-pro
```

### Other supported agents

Replace `codex` with a target supported by the [`skills` CLI](https://github.com/vercel-labs/skills), for example:

```bash
npx skills add PGraeff/frontend-design-pro-agent-skill --skill frontend-design-pro --global --agent claude-code --yes --copy
npx skills add PGraeff/frontend-design-pro-agent-skill --skill frontend-design-pro --global --agent cursor --yes --copy
```

### From a clone

PowerShell:

```powershell
git clone https://github.com/PGraeff/frontend-design-pro-agent-skill.git
cd frontend-design-pro-agent-skill
.\scripts\install.ps1 -Agent codex
```

macOS or Linux:

```bash
git clone https://github.com/PGraeff/frontend-design-pro-agent-skill.git
cd frontend-design-pro-agent-skill
./scripts/install.sh --agent codex
```

Pass `-Project` in PowerShell or `--project` in the shell script to install into the current project instead of the global agent directory.

## Use

Example requests:

```text
Use $frontend-design-pro to redesign this Flutter onboarding flow.
Review this dashboard for usability, accessibility, and unnecessary UI copy.
Create a responsive product interface with a distinctive visual direction.
```

The bundled search engine can also be called directly:

```bash
python skills/frontend-design-pro/scripts/search.py "running app mobile training" --design-system -p "Kilometro"
python skills/frontend-design-pro/scripts/search.py "safe areas and navigation" --stack flutter
python skills/frontend-design-pro/scripts/search.py "accessible chart interaction" --domain ux
```

The search scripts use only the Python standard library.

## Repository layout

```text
skills/frontend-design-pro/   Installable Agent Skill and its runtime resources
scripts/                      Repository validation, packaging, and installation
.github/workflows/            Pull-request validation and tagged releases
AGENTS.md                     Contribution instructions for coding agents
CONTRIBUTING.md               Human and agent contribution workflow
LICENSES/                     Third-party license texts
```

The skill folder stays self-contained so agents can download only that path. Human-facing maintenance documents remain at the repository root and do not consume skill context.

## Validate

```bash
python scripts/validate_repo.py
python scripts/package_skill.py
npx skills add . --list
```

Validation checks the skill manifest, portable paths, UTF-8 readability, bundled data, Python tests, search execution, license files, and package contents. GitHub Actions runs the same checks on Windows and Linux for every pull request.

## Contribute

Fork the repository, create a focused branch, run the validation command, and open a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for branch names and review expectations. Agents should also read [AGENTS.md](AGENTS.md) before editing.

## Provenance and license

The repository combines and substantially modifies ideas from Anthropic's [`frontend-design`](https://github.com/anthropics/skills/tree/main/skills/frontend-design), licensed under Apache License 2.0, with data and search tooling derived from Next Level Builder's [`ui-ux-pro-max-skill`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), licensed under MIT.

Original repository contributions are distributed under Apache License 2.0. Bundled MIT components retain their original license. See [LICENSE](LICENSE), [NOTICE](NOTICE), and [LICENSES](LICENSES).
