# Setup

## Base Environment

AgentHPOBench requires Python 3.10 or newer on Linux. The orchestration layer can be installed with:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[local,analysis]"
```

The 30 tasks originate from heterogeneous repositories and cannot be represented faithfully by one dependency set. Install each upstream repository according to its own instructions, then add task-specific packages required by the corresponding adapter.

The released adapters default to Conda environments under `/opt/miniconda3`,
matching the evaluation machines. Set `CONDA_ROOT` when Conda is installed
elsewhere:

```bash
export CONDA_ROOT="$HOME/miniconda3"
```

## Repository and Asset Layout

Clone upstream repositories with:

```bash
python3 scripts/clone_repositories.py
```

Pinned repositories are fetched at their exact commit whenever the Git server
supports an object-level shallow fetch. Existing destinations are accepted only
when their revision, compatibility patch, and worktree match the manifest.

Expected local-only directories are:

```text
repositories/   Upstream source repositories
data/           Downloaded or licensed datasets
models/         Agent and task model weights
results/        Result JSON files and run artifacts
logs/           Execution logs
```

These directories are ignored by Git except for small published summaries.

## Model Paths

Default agent-model paths are listed in `configs/models.json`. Override them without changing source:

```bash
export QWEN3_8B_MODEL=/path/to/Qwen3-8B
export AUTOREP_MODEL_PATH=/path/to/Qwen3-32B
```

The runners default to Hugging Face offline mode because the reported experiments used predownloaded assets. Set `HF_HUB_OFFLINE=0`, `TRANSFORMERS_OFFLINE=0`, and `HF_DATASETS_OFFLINE=0` when downloads are permitted.

## API Agents

Copy `.env.example` to `.env` and set only the provider variables you use. `.env` is ignored by Git. You can also point to another file:

```bash
export AGENTHPOBENCH_ENV_FILE=/secure/path/agenthpobench.env
```

Never place credentials in task JSON, result JSON, shell scripts, or committed logs.

## Runner Controls

Common overrides:

| Variable | Purpose |
|---|---|
| `CONDA_ROOT` | Conda installation root; defaults to `/opt/miniconda3` |
| `AUTOREP_ROOT` | Repository root |
| `AUTOREP_TASK_OVERLAY` | Main or ablation task directory |
| `AUTOREP_MODEL_PATH` | Local agent model |
| `AUTOREP_RUN_TAG` | Result and log namespace |
| `AUTOREP_NONRAY_TASKS` | Comma-separated non-Ray subset |
| `AUTOREP_RAY_TASKS` | Comma-separated Ray subset |
| `AUTOREP_SKIP_RAY=1` | Run only the non-Ray phase |
| `AUTOREP_DRY_RUN=1` | Validate paths without executing |
| `AUTOREP_REJECT_FALLBACK=1` | Fail on any fallback decision |
| `VERL_INITIAL_CHECKPOINT` | Initial checkpoint for the limited-budget VERL task |

Run at most one Ray workload per host. The supplied launchers serialize Ray phases with a host-local file lock.

The `AUTOREP_*` names are kept for compatibility with the exact experiment
scripts. New code should treat them as AgentHPOBench runner controls.
