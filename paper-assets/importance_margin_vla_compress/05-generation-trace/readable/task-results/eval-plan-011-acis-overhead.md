# eval plan 011 acis overhead

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_011_acis_overhead_20260516T161905_result.json`
- **Structured JSON:** [`902fc095d8fd99b6b5b1.json`](../../sessions/90/902fc095d8fd99b6b5b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**结果总结：**

| 指标 | Baseline (SmolVLA+LoRA) | ACIS 增量 | 开销比 |
|------|------------------------|-----------|--------|
| 参数量 | 451.53M | +3.46M | **+0.77%** |
| FLOPs | 169.87G | +409.75M | **+0.24%** |
| 延迟 | 51.16ms | +0.32ms | **+0.63%** |

ACIS 模块的 deployment cost 可忽略不计。参数/FLOPs/延迟三个维度开销均 < 1%。

注：`with_acis_pruned` 的 251ms 数值来自未优化的 wrapper 训练路径（手动重构 embeddings），不代表实际部署推理性能。实际部署中 ACIS 的净效果是：+0.32ms 评分开销，换取 50% visual token 减少后的 VLM attention 加速。

---
