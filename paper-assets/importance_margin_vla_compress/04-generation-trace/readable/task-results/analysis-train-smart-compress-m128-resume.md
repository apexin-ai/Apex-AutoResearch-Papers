# analysis train smart compress m128 resume

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_train_smart_compress_m128_resume_20260518T100802_result.json`
- **Structured JSON:** [`80487364defb9b0c39fe.json`](../../sessions/80/80487364defb9b0c39fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。汇总：

## M=128 Passthrough 训练结果

**训练状态**: 成功完成，step 32001 → 99999，无 error/OOM，速度 ~4.1 sps

**最终指标**:
- train/action_loss: **0.054**
- eval/action_loss: **0.057**

**三配置对比**:

| 配置 | Train Loss | Eval Loss |
|------|-----------|-----------|
| M=32 | 0.110 | **0.052** |
| M=64 | 0.045 | 0.062 |
| M=128 (passthrough) | 0.054 | 0.057 |

**核心结论**: 三个配置 eval loss 都在 0.052-0.062 区间，差距 <0.01。M=128 不压缩不比压缩版本更好或更差，说明：
1. Cross-attention 架构本身不损害性能
2. 压缩到 M=32 (1/4 token) 也不损害性能
3. 在当前数据规模下，压缩比对最终 eval 性能影响有限
4. M=32 train loss 偏高 (0.11 vs 0.054) 暗示压缩增加训练难度，但 eval loss 反而最低，可能有 regularization 效应

Registry 已更新 metrics 和 spec（未设 status/conclusion，留给主 Agent）。分析报告已注册为 artifact。

---
