# Contributing

Contributions should preserve the benchmark's task definitions, intervention budgets, and result provenance.

1. Create a focused branch and keep generated data, model weights, checkpoints, logs, and credentials out of Git.
2. Run `python scripts/validate_release.py`.
3. Run `python analysis/validate_tasks.py`.
4. For runner changes, execute the relevant `AUTOREP_DRY_RUN=1` command.
5. Add or update tests when changing parsing, scoring, intervention validation, or result schemas.

New tasks must include a `baseline.json`, an executable baseline adapter, an intervention adapter, a bounded search space derived from upstream resources, and an entry in `configs/tasks.json` and `configs/repositories.json`.
