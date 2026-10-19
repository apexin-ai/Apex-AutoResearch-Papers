# analysis cka mvp full

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cka_mvp_full_20260521T041353_result.json`
- **Structured JSON:** [`479562af89e6a22c0361.json`](../../sessions/47/479562af89e6a22c0361.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个模型的完整 CKA 分析已跑完：

**Qwen2.5-7B**: 8 层 × 5 语言，CKA 峰值在 layer 16 (0.760)，到 layer 27 降至 0.244
**Llama-3.1-8B**: 9 层 × 5 语言，CKA 峰值在 layer 12 (0.810)，到 layer 31 降至 0.317

两个模型语言排序一致：zh > ar/ko > sw > hi。Llama 的 CKA–degradation 相关性更强 (ρ=−0.52, p=0.001)，与其跨层 CKA 异质性更大一致。

产出：
- CSV: `results_cka_mvp001/cka_matrix_qwen25_7b.csv`, `results_cka_mvp003/cka_matrix_llama31_8b.csv`（服务器端）
- 报告: `artifacts/cka_mvp_full_results.md`（含完整矩阵、深度趋势对比、与已有 degradation 数据交叉验证）

---
