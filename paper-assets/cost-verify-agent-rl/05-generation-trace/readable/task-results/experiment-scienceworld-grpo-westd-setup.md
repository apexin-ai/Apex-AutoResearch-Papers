# experiment scienceworld grpo westd setup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_scienceworld-grpo-westd-setup_20260520T111947_result.json`
- **Structured JSON:** [`1dcabeb3393c62cea334.json`](../../sessions/1d/1dcabeb3393c62cea334.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both processes stable and running (Cell A: 2m14s, Cell C: 1m43s). Still in initialization phase (FSDP sharding + vLLM engine startup). ScienceWorld environments take longer to init than ALFWorld.

**Launch summary:**

| Experiment | GPU | PID | W&B Run | Status |
|---|---|---|---|---|
| `scienceworld_grpo_cell_a` (step-independent h=2) | cuda:0,1 | 759987 | `f1c4g6dk` | RUNNING — initializing |
| `scienceworld_grpo_cell_c` (episode-level full) | cuda:2,3 | 766820 | `sx7h864t` | RUNNING — initializing |

**Issues fixed during launch:**
- `enable_response_mask` assertion failed because model path didn't contain "qwen" — created symlink `qwen3_scienceworld_sft → scienceworld_sft` and updated both configs
- `submit_training_job` tool doesn't exist in available toolset — used `ssh_execute` with nohup instead

**Pending cleanup:** bjb1 authorized_keys still has westd's SSH key from the SCP transfer. Low priority but should be removed eventually.

---
