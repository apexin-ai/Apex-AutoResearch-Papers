# code grpo v3 emergency scripts

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-v3-emergency-scripts_20260515T071556_result.json`
- **Structured JSON:** [`362ee39d61eb3863ebf2.json`](../../sessions/36/362ee39d61eb3863ebf2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

---

**产出汇总**

**创建的文件（3 个）：**
| 文件 | 说明 |
|------|------|
| `src/train_grpo_v3.py` | v3 训练脚本，基于 train_grpo.py 修改 |
| `scripts/run_grpo_stage2_v3_rasp.sh` | RASP 变体启动脚本（cuda:0） |
| `scripts/run_grpo_stage2_v3_standard.sh` | Standard 变体启动脚本（cuda:1） |

**reward function 修改：**
- 原版：`accuracy_reward` 仅 1.0（正确）/ 0.0（错误）
- v3：`accuracy_reward + format_reward`，其中 `format_reward = 0.1 if \boxed{...} in completion else 0.0`
- format_reward_weight 可通过 `--format_reward_weight` 调整（默认 0.1）

**v3 新增参数（相对原 train_grpo.py）：**
- `--beta 0.01` → 传入 GRPOConfig 启用 KL penalty
- `--loss_type dapo` → 传入 GRPOConfig
- `--format_reward_weight 0.1` → 控制 format reward 权重
- `--max_completion_length` 默认值从 4096 改为 2048

**需 Director 注意：**
1. **sft_standard_20 不存在** — westb-23072 上已删除，standard 脚本无法直接运行。需确认 checkpoint 来源（其他服务器/重训）。
2. **beta=0.01 兼容性** — 依赖 trl GRPOConfig 支持 `beta` 和 `loss_type` 参数，已写入配置但未做 runtime 验证（避免触发模型加载）。
3. 两个脚本均 **未启动**，等待审批。

---
