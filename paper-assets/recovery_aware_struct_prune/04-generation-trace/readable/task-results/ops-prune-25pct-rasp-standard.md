# ops prune 25pct rasp standard

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prune-25pct-rasp-standard_20260516T044629_result.json`
- **Structured JSON:** [`73e4066d915685a59fbd.json`](../../sessions/73/73e4066d915685a59fbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

磁盘满了，无法完成 Standard 25% 保存。当前状况：

| 目录 | 大小 | 说明 |
|------|------|------|
| `grpo_stage2_rasp_20_v9/` | 143G | GRPO 训练 checkpoints |
| `pruned_rasp_alpha_0.0/` | 12G | α ablation 模型 |
| `pruned_rasp_alpha_1.0/` | 12G | α ablation 模型 |
| `sft_rasp_20/` | 12G | SFT 模型 |
| `sft_standard_20/` | 12G | SFT 模型 |
| `grpo_stage2_standard_20_v8/` | 12G | GRPO checkpoints |
| `pruned_rasp_25/` | 11G | **刚完成** |
| `pruned_standard_25/` | 9.6G | **残缺，需删除** |
| `models/Qwen2.5-Math-7B/` | 15G | 基线模型 |

**必须做**：删除残缺的 `pruned_standard_25/`（9.6G）
**但仍差 ~2G**：删除后只有 ~10G 可用，standard_25 需要 ~11G。

建议清理候选（任选其一即可）：
1. `grpo_stage2_rasp_20_v9/` 中的旧 checkpoints（143G，删部分即可）
2. 空的 GRPO 目录（v5/v6/v7 等，但只释放几KB没用）
3. `pruned_rasp_alpha_0.0/`（12G，如果 ablation 已完成）

哪些可以删？

---
