# code exp007 config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp007_config_20260514T001255_result.json`
- **Structured JSON:** [`b6eac1a6e92660b89374.json`](../../sessions/b6/b6eac1a6e92660b89374.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Hydra 加载成功，关键参数全部生效。

---

**产出**

| 文件 | 路径 |
|------|------|
| exp007 主配置 | `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp007_fixed.yaml` |
| exp007 dry-run | `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp007_dryrun.yaml` |

**与 exp003 的 diff：**

| 参数 | exp003 | exp007 |
|------|--------|--------|
| `trainer.total_training_steps` | 100 | 30 |
| `trainer.experiment_name` | exp003-alfworld-selfguide-prompt-trunc | exp007-alfworld-speed-optimized |
| `trainer.local_log_dir` | exp_003/ | exp_007/ |
| `agent_proxy.max_turn` | 50 | 30 |
| `es_manager.train.env_groups` | 16 | 8 |
| `collapse_detection.multi_turn_enabled` | true (base default) | **false** |

dry-run 版本额外差异：`total_training_steps: 1`，`local_log_dir` 指向 `exp_007_dryrun/`。

---
