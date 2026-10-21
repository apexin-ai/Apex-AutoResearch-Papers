# ops persist holm bonferroni

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_persist_holm_bonferroni_20260522T074344_result.json`
- **Structured JSON:** [`bf08acc61400cb76bc69.json`](../../sessions/bf/bf08acc61400cb76bc69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已生成。报告：

1. **重用已有数据** — `multiple_comparison_results.json`（80 comparisons）已存在，转换格式生成 `holm_bonferroni_results.json` + `holm_bonferroni_summary.csv`
2. **总比较数**: 80
3. **Holm 校正后仍显著**: 67/80 (83.8%)；BH 校正后: 70/80 (87.5%)
4. **Holm 校正后失去显著性的 3 个比较**（原始 p < 0.05 但 Holm p > 0.05）:
   - **Qwen-1.5B**: ae_only vs exception_only (diff=−0.0075, raw p=0.012 → Holm p=0.060)
   - **Qwen-1.5B**: ae_only vs nomarker (diff=0.0128, raw p=0.015 → Holm p=0.060)
   - **DeepSeek-6.7B**: loop_only vs vota (diff=−0.0319, raw p=0.037 → Holm p=0.110)

另有 10 个比较在校正前就不显著（均为高准确率 condition 之间的微小差异，如 ae_only vs exception_only）。

---
