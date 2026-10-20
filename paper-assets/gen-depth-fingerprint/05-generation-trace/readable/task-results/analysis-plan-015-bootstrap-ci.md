# analysis plan 015 bootstrap ci

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-015-bootstrap-ci_20260515T003225_result.json`
- **Structured JSON:** [`95e76ab42e78ce71460b.json`](../../sessions/95/95e76ab42e78ce71460b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

| 模型 | LOGO F1 | 95% CI |
|------|---------|--------|
| **7-feature** | 0.7977 | [0.7925, 0.8031] |
| Avg-LogProb | 0.7586 | [0.7530, 0.7640] |
| FastDetectGPT | 0.7310 | [0.7251, 0.7369] |

**Paired bootstrap 检验**（1000次，seed=42）：
- 7-feat vs Avg-LogProb: **ΔF1 = +3.9pp** [+3.4, +4.4], p=0.000
- 7-feat vs FastDetectGPT: **ΔF1 = +6.7pp** [+6.0, +7.3], p=0.000

**结论**: 7-feature ensemble 相对 Avg-LogProb 的 3.9pp 优势在统计上高度显著（p<0.001），95% CI 完全不重叠。两个模型的 CI 也互不重叠（7-feat 下界 0.7925 > Avg-LogProb 上界 0.7640）。

产出已保存到 `/root/gen-depth-fingerprint/artifacts/plan-015/bootstrap_ci_results.txt`，registry plan-015 metrics 已更新 `bootstrap_ci` 字段。

---
