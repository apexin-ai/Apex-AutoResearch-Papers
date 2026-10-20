# analysis p1 appendix b null

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p1_appendix_b_null_20260515T143038_result.json`
- **Structured JSON:** [`52c584d38091dacee652.json`](../../sessions/52/52c584d38091dacee652.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**确认：Appendix B 中 G_× = 58–241× 来自 n=50 旧数据，需要更新。**

### 关键证据
- n=500 additive G 最大值 = 208，而 multiplicative correction 只会让 G 变小
- G_× = 241 > 208，因此不可能来自 n=500 数据
- n=50 additive G = 69–274，经 multiplicative 调整（×0.84–0.88）后恰好是 58–241

### 更新数据

| Sparsity | 旧值 (n=50) G_× | 新值 (n=500) G_× est |
|----------|-----------------|---------------------|
| 0.15     | 58              | **51**              |
| 0.20     | —               | **91**              |
| 0.25     | —               | **133**             |
| 0.30     | 241             | **183**             |

**建议更新 appendix.tex 第 38 行：** `G_× = 58–241×` → `G_× ≈ 51–183×`

### 定性结论不变
- G_× 随 sparsity 单调递增
- Importance-based: G_× >> 1；Random: G_× ≈ 1
- s=0.25 crossover 保留

### 交付文件
- 报告：`artifacts/p1_appendix_b_null/report.md`
- 服务器 JSON：`analysis_output/p1_appendix_b_multiplicative_null.json`

### 方法注意
精确 n=500 G_× 需要 per-problem PPL ratio（未持久化在 profiling output 中）。当前估计使用 n=50 已知 G_×/G_add 比值（0.84–0.88）校准。如需精确值，需重新运行 profiling 并存储 per-problem PPL 分项。

---
