# ScienceWorld RAGEN Adapter Report

Date: 2026-05-19
Server: westd-47453

## 1. Environment Setup

- `scienceworld==1.2.3` + `py4j==0.10.9.9` installed via pip
- JVM: installed via `apt-get install default-jre` (not in base conda image)
- 30 tasks available, each with train/dev/test variation splits
- Verified: JVM starts, tasks load, gold sequences execute, scores reach 100

## 2. Adapter Implementation

### Files created on westd-47453

**`/root/autodl-tmp/cost-verify-agent-rl/RAGEN/ragen/env/scienceworld/`**

| File | Purpose |
|------|---------|
| `__init__.py` | Exports `ScienceWorldEnvConfig`, `ScienceWorldTXTEnv` |
| `config.py` | `ScienceWorldEnvConfig(BaseEnvConfig)` dataclass |
| `env.py` | `ScienceWorldTXTEnv(BaseLanguageBasedEnv)` adapter |

### Config parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `task_names` | `"boil"` | Comma-separated task list, random selection per episode |
| `score` | `10.0` | Reward scale on full completion |
| `max_steps` | `100` | Step limit per episode |
| `simplification_str` | `""` | ScienceWorld simplification flags |
| `max_valid_actions` | `50` | Cap on admissible actions in observation |
| `eval_split` | `"dev"` | Which split for val mode (`"dev"` or `"test"`) |

### Reward design

- **Sparse reward only at episode end**: `reward = (final_score / 100) * config.score`
- Intermediate steps return `reward = 0.0`
- `final_score` = ScienceWorld cumulative score (0-100)
- Compatible with GRPO episode total return constraint (sum of step rewards = single terminal reward)

### Observation format

```
Task: {task_description}
{environment_observation}

Admissible actions: [{action1}, {action2}, ...]
```

- Task description included on reset
- Admissible actions capped at `max_valid_actions` (ScienceWorld can have 400+ valid actions)

## 3. Registration

### `ragen/env/__init__.py`
```python
try:
    from .scienceworld.env import ScienceWorldTXTEnv
    from .scienceworld.config import ScienceWorldEnvConfig
    REGISTERED_ENVS['scienceworld'] = ScienceWorldTXTEnv
    REGISTERED_ENV_CONFIGS['scienceworld'] = ScienceWorldEnvConfig
except ImportError:
    pass
```

### `config/envs.yaml` entries

| Config Name | Tasks | Notes |
|------------|-------|-------|
| `ScienceWorldBoil` | boil | Single task |
| `ScienceWorldMelt` | melt | Single task |
| `ScienceWorldFreeze` | freeze | Single task |
| `ScienceWorldMixed` | boil,melt,freeze,change-the-state-of-matter-of,use-thermometer,test-conductivity | Multi-task |

All configs: `max_actions_per_traj=50`, `parallel_friendly=false`, `max_workers=1`

## 4. Functional Verification

Verified on westd-47453:

- `reset(seed=42)`: returns observation with task description, env state, admissible actions
- `step(action)`: returns `(obs, 0.0, False, info)` for intermediate steps
- Mode switching: `reset(mode='val')` uses dev variations (different substances)
- Registration: `scienceworld` present in both `REGISTERED_ENVS` and `REGISTERED_ENV_CONFIGS`
- Full gold episode (boil, var 0): 36 steps, final score 100/100, total reward 10.0

## 5. Expert SFT Data Generation

**Status**: Running in background (PID 755742 on westd-47453)

**Script**: `/root/autodl-tmp/cost-verify-agent-rl/generate_scienceworld_sft.py`

**Output files**:
- `/root/autodl-tmp/expert_sft/scienceworld_sft_train.jsonl`
- `/root/autodl-tmp/expert_sft/scienceworld_sft_val.jsonl`

**Format**: RAGEN multi-turn conversation JSONL (matches ALFWorld SFT format)
```json
{"messages": [
  {"role": "system", "content": "..."},
  {"role": "user", "content": "Turn 1:\nTask: ...\nState: ...\nAdmissible actions: [...]"},
  {"role": "assistant", "content": "<think>...</think><answer>action</answer>"},
  ...
], "metadata": {"task": "boil", "variation": 0, "final_score": 100, "num_steps": 39, "success": true}}
```

**Progress at report time**: 16/30 tasks started, ~1650 trajectories generated. Estimated total: 3000-4000 trajectories across all 30 tasks.

**Key observations**:
- Tasks like `find-animal`, `find-living-thing`, `find-plant` have 200+ variations each
- `inclined-plane-friction-*` tasks have 200+ variations with gold sequences up to 700+ steps
- Most tasks achieve 100/100 with gold sequences, some complex tasks reach only 20-50

**Monitor**: `tail -f /root/autodl-tmp/scienceworld_sft_gen.log`

## 6. ScienceWorld Task Statistics (from gold sequences)

| Task | Gold Steps (typical) | Gold Score | Notes |
|------|---------------------|------------|-------|
| boil | 26-143 | 78-100 | State-of-matter experiments |
| change-the-state-of-matter-of | 21-88 | 100 | Similar to boil/melt/freeze |
| chemistry-mix | 16-29 | 100 | Short sequences |
| chemistry-mix-paint-* | 11-24 | 100 | Short sequences |
| find-animal/living/non-living/plant | 5-16 | 100 | Very short but 200+ variations |
| freeze | 30-87 | 82-100 | Some variations don't reach 100 |
| grow-fruit/grow-plant | 61-105 | 50-100 | Long sequences, some incomplete |
| inclined-plane-* | 48-774 | 20-100 | Extremely variable |

## 7. Architecture Notes

- **Thread safety**: `ScienceWorldEnv` JVM is cached per-thread via `_ENV_CACHE` + `_ENV_LOCK`
- **Not parallel-friendly**: Single JVM process, `max_workers=1` in envs.yaml
- **Graceful import**: `try/except ImportError` in `__init__.py` (won't break RAGEN if scienceworld not installed)
- **ALFWorld parity**: Same base class, same observation format pattern, same sparse reward design
