# analysis v4 vanilla seed1 logs

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-vanilla-seed1-logs_20260515T144214_result.json`
- **Structured JSON:** [`bf96d7b14fe6caddc9fd.json`](../../sessions/bf/bf96d7b14fe6caddc9fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

**v4-vanilla-seed1 训练正常完成，非异常退出。** EXIT_CODE=0。

| 项目 | 值 |
|------|-----|
| 完成度 | **1635/1635 steps, epoch 3.0/3.0 (100%)** |
| 最终 loss | 0.292 (平均 0.416) |
| 最终 token_acc | 0.903 |
| 总耗时 | 58m 50s |
| GPU 内存 | 17.63 GiB |

**之前监控显示 10% (167/1635) 的判断有误**——可能是在训练早期做的快照，或者查了错误的数据源。实际训练 loss 从 4.04 正常下降到 0.29，三个 epoch 全部跑完。

**W&B**：本次训练未启用 W&B，仅有 TensorBoard 日志。

**Checkpoint**（3个，均可用）：
- `checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-545/` (epoch 1)
- `checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1090/` (epoch 2)
- `checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1635/` (epoch 3, 最终)

无需修复，checkpoint-1635 可直接用于后续评估。报告已注册为 artifact `art_20260515_86f5ca`。

---
