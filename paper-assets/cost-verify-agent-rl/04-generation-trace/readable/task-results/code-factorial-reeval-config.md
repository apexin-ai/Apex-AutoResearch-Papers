# code factorial reeval config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_factorial-reeval-config_20260517T205254_result.json`
- **Structured JSON:** [`a36da2c07c9ed6147fb3.json`](../../sessions/a3/a36da2c07c9ed6147fb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过，config 解析正确。

**产出总结：**

Config 文件已创建于两台服务器：
- `bjb1-17606:/root/cost-verify-agent-rl/RAGEN/config/_alfworld_factorial_h2_reeval_sg_ood.yaml`
- `westd-47453:/root/cost-verify-agent-rl/RAGEN/config/_alfworld_factorial_h2_reeval_sg_ood.yaml`

**Dry-run 验证结果：**
| 参数 | 值 |
|------|-----|
| val.tags | `['AlfworldSG_OOD']` (修复：原为 AlfworldOOD) |
| val.env_groups | 134 |
| context_window_mode | step_independent |
| step_independent_history_length | 2 |
| advantage_mode | episode_level |
| val_before_train | True |
| total_training_steps | 1 |
| resume_from_path | `.../global_step_PLACEHOLDER` |

**待实验完成后**：将 `resume_from_path` 中的 `PLACEHOLDER` 替换为实际最佳 step 编号即可执行 re-eval。

---
