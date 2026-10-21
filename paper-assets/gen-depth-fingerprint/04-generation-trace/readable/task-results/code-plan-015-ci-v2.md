# code plan 015 ci v2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-015-ci-v2_20260515T003044_result.json`
- **Structured JSON:** [`0823d0123f883eea46df.json`](../../sessions/08/0823d0123f883eea46df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| 指标 | Point | 95% CI |
|------|-------|--------|
| **7-feature LOGO F1** | 0.7977 | [0.7925, 0.8031] |
| **Avg-LogProb LOGO F1** | 0.7586 | [0.7530, 0.7640] |
| **FastDetectGPT LOGO F1** | 0.7310 | [0.7252, 0.7366] |

**Paired bootstrap ΔF1:**
- 7-feature vs Avg-LogProb: **ΔF1=+0.039** [0.033, 0.044], p=0.000 — **显著**
- 7-feature vs FastDetectGPT: **ΔF1=+0.067** [0.061, 0.073], p=0.000 — **显著**

**Spearman ρ (vs label):**
- Avg-LogProb: ρ=0.728 [0.720, 0.735]
- FastDetectGPT: ρ=0.343 [0.330, 0.358]

三组 CI 无重叠，1000 次 bootstrap 中没有一次 ΔF1≤0，7-feature 相对 Avg-LogProb 的优势在统计上高度显著。输出已存 `/root/gen-depth-fingerprint/data/plan015_bootstrap_ci.json`。

---
