# compute r5w1 split origin covariate

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_r5w1_split_origin_covariate_20260516T175323_result.json`
- **Structured JSON:** [`c86981f7ad5e5e4eee1f.json`](../../sessions/c8/c86981f7ad5e5e4eee1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，无 warnings。

---

**完成总结：**

**分析结果：**
- N=213 multi-type batches，train_origin_ratio 范围 0.40–1.00（均值 0.80）
- Simple regression: β_BCS = −0.412, p < 10⁻¹⁶, R² = 0.284
- Multiple regression: β_BCS = −0.416, p < 10⁻¹⁶（不变）; β_origin = −0.057, p = 0.245（不显著）; ΔR² = 0.005
- **结论**：split-origin 不是 BCS-accuracy 关系的 confound

**论文修改：**
- 新增 Appendix `\section{Split-Origin Covariate Analysis}` (`\label{app:split-origin}`)，包含 method + results
- Limitations 的 Data contamination 条目末尾添加了 cross-reference 到新 appendix
- 编译成功，19 页，无错误

---
