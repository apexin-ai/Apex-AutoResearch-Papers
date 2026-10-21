# analysis uniform vs nonuniform dif

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_uniform-vs-nonuniform-dif_20260523T085354_result.json`
- **Structured JSON:** [`210f966eceebec92c1cb.json`](../../sessions/21/210f966eceebec92c1cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。结果摘要：

**Uniform vs Non-uniform DIF 对比（MMLU, J=16, I=300）**

| 指标 | Non-uniform | Uniform |
|------|-------------|---------|
| γ mean | 0.245 ± 0.197 | −0.458 ± 0.453 |
| γ 90% CI | [−0.081, 0.571] | [−1.224, 0.307] |
| Divergences | 0 | 0 |
| PPP | 0.763 | 0.743 |
| LOO ELPD | −2124.3 | −2123.4 |
| LOO k>0.7 | 7 | 4 |
| Sampling time | 59s | 102s |

**结论**：两个模型的 LOO 本质上相同（ΔELPD=0.9, dSE=1.4，差异远小于 1 SE）。Non-uniform DIF 优势在于：(1) γ 的 posterior 更紧（SD 0.197 vs 0.453），(2) ESS 更高（1468 vs 981），(3) 采样更快（59s vs 102s），(4) γ 直接可解释为固定 logit shift，不被 item discrimination 混淆。

产出已注册：`artifacts/dif_model_comparison.md`，JSON 结果在服务器 `analysis/dif_comparison/results.json`。

---
