# writing sf limitations appendix

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_sf-limitations-appendix_20260525T223705_result.json`
- **Structured JSON:** [`a38fed5362de4277f652.json`](../../sessions/a3/a38fed5362de4277f652.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改总结：

1. **limitations.tex**（paper/ + docs/ 两份）：
   - 扩展单数据集讨论：UltraChat 覆盖 18 种对话类型，但跨数据集验证是 future work
   - 新增 LoRA-only 限制：rank 16 LoRA 可能 confound capacity exclusion
   - 删除了原来冗余的 "one auxiliary loss family" 点（已被 appendix caveat 覆盖）
   - "causal exclusion" → "diagnostic exclusion"

2. **appendix.tex**（paper/ + docs/ 两份）：在 Loss Formulation Search 的 table 后新增 `\paragraph{Overfitting caveat.}` 段落，说明 v1-v7 在单一数据集上开发的过拟合风险、TF-AR gap 在所有 variants 中出现的结构性证据、v7 使用标准 MSE 无 dataset-specific tricks。

---
