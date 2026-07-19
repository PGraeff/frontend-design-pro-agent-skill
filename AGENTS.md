# Agent Contribution Instructions

## Scope

The deployable source of truth is `skills/frontend-design-pro/`. Do not add maintainer documentation, generated archives, screenshots, or temporary output inside that directory.

## Workflow

1. Start from an up-to-date `main` branch.
2. Create a focused branch named `agent/<description>`, `feat/<description>`, `fix/<description>`, or `docs/<description>`.
3. Read `skills/frontend-design-pro/SKILL.md` completely before changing its behavior.
4. Load only the reference or data files relevant to the change.
5. Preserve the existing progressive-disclosure structure and keep `SKILL.md` below 500 lines.
6. Keep visible UI-copy guidance strict: product text must help users decide, act, understand state, recover, or give informed consent.
7. Do not introduce machine-specific absolute paths, agent-specific environment assumptions, secrets, telemetry, or network calls into the skill runtime.
8. Run `python scripts/validate_repo.py` and `python scripts/package_skill.py` before committing.
9. Commit only source changes. Do not commit `dist/`, caches, virtual environments, or editor state.
10. Open a pull request describing behavior changes, provenance implications, and validation evidence.

## Compatibility

- Keep runtime Python code compatible with Python 3.10 and newer.
- Use the Python standard library unless a dependency is justified and documented.
- Resolve skill resources relative to `SKILL.md` or `__file__`; never assume a Codex-, Claude-, or user-specific installation path.
- Keep the `name` in `SKILL.md` equal to the containing directory name.
- Preserve `agents/openai.yaml` for Codex while keeping the core skill valid for other Agent Skills consumers.

## Licensing

Do not copy external guidance, data, or code without verifying its license. Preserve required notices and update `NOTICE` or `LICENSES/` whenever provenance changes. Files derived from Apache-licensed material must carry a modification notice when changed.
