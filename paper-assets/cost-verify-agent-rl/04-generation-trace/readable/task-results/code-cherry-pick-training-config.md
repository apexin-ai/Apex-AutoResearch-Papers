# code cherry pick training config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cherry_pick_training_config_20260515T083553_result.json`
- **Structured JSON:** [`6643092a4622ec784216.json`](../../sessions/66/6643092a4622ec784216.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Hydra 配置验证通过，所有关键参数解析正确。

**已创建的文件**：

| 文件 | 路径 |
|---|---|
| 配置 YAML | `RAGEN/config/_alfworld_exp026_step_independent_grpo.yaml` |
| 训练脚本 | `scripts/run_exp026_step_independent_grpo.sh` |
| Dry-run 脚本 | `scripts/run_exp026_dryrun.sh` |

**相比 exp022-24 的关键变更**：

| 参数 | exp022-24 | exp026 | 来源 |
|---|---|---|---|
| `kl_loss_coef` | 0.5 | **0.01** | verl-agent default |
| `kl_loss_type` | kl | **low_var_kl** | verl default (k3) |
| `lr` | 5e-7 | **1e-6** | verl-agent default |
| `context_window_mode` | full | **step_independent** | Worker 1 新增 |
| `max_context_window` | -1 (全量) | **5** (bounded) | 配合 step-independent |
| `max_turn` | 30 | **50** | 对齐 verl-agent |
| `use_turn_scores` | False | **True** | Worker 2 step-level reward |
| `total_training_steps` | 30 | **150** | 充分训练 |
| `test_freq` | 20 | **5** | 更频繁验证 |
| `save_freq` | 5 | **25** | 减少 IO |
| `logger` | console only | **console+wandb** | 完整监控 |

**依赖 Worker 1/2 的部分**：
- `context_window_mode: "step_independent"` — 需要 Worker 1 在 ctx_manager.py 中实现
- `use_turn_scores: True` — 需要 Worker 2 的 step-level reward 计算
- `invalid_action_penalty` — RAGEN 尚未支持，已在 config 中标注 TODO

---
