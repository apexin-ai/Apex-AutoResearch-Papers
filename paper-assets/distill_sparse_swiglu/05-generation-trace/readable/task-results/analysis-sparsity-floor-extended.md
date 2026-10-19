# analysis sparsity floor extended

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sparsity_floor_extended_20260517T044139_result.json`
- **Structured JSON:** [`5e26c7ec92327fc3f743.json`](../../sessions/5e/5e26c7ec92327fc3f743.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

```
Sparsity Target | Always-Pruned % | Late-Layer Max % | Pruned Neurons
30%             | 0.0499          | 0.4604           | 229 / 458,752
50%             | 0.0726          | 1.2347           | 333 / 458,752
70%             | 0.1936          | 4.3666           | 888 / 458,752
```

**关键发现**：
- 所有 sparsity 级别的 always-pruned floor 都极低（< 0.2%），证实预测器几乎完全是上下文驱动的
- Early/middle layers（0-23）几乎零静态剪枝，所有 always-pruned neurons 集中在 late layers（28-31）
- Floor 从 30%→70% 增长约 4×，但即使在 70% 目标下仍仅 0.19%
- Layer 31 在 70% 目标下有最高单层 floor（4.37%），可能因为最后一层 hidden states 对输出影响较小

**产出**：
- 脚本：`/root/distill_sparse_swiglu/scripts/sparsity_floor_extended.py`
- 数据：`/root/distill_sparse_swiglu/artifacts/sparsity_floor_extended.json`（完整 per-layer 数据）
- 注册：`art_20260517_29b602`

---
