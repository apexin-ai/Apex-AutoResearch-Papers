# code distributional tests

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_distributional-tests_20260517T142156_result.json`
- **Structured JSON:** [`0278980b358f427d0a8c.json`](../../sessions/02/0278980b358f427d0a8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

**所有 7 个特征的 KS 检验全部显著**（Bonferroni 校正后 p ≈ 0），确认 depth 维度上存在 location shift。

**Levene 检验也全部显著**（p < 1e-10），说明方差也随 depth 变化。

**分类汇总：**
- Location shift + shape preserved: **无**（预期的 entropy_mean/ttr/hapax_ratio 没有出现在这里）
- Location shift + shape shift: **全部 7 个特征**
- No shift: **无**

这意味着 depth 不仅移动分布中心，还改变分布形状（方差）。所有特征都呈现全面漂移，而非简单的 location-only shift。结果已写入 `/root/gen-depth-fingerprint/results/distributional_tests.json`。

---
