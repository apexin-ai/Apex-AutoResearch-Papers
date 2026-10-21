# analysis clustered bootstrap

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_clustered_bootstrap_20260522T043519_result.json`
- **Structured JSON:** [`0d3b18005bfa71b60ade.json`](../../sessions/0d/0d3b18005bfa71b60ade.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出文件在 `/root/trace-verdict-study/artifacts/clustered_bootstrap/`。

## 结果摘要

### Per-condition CI（7 个主条件）

| Condition | Acc% | Sample 95% CI | Clustered 95% CI | Width Ratio |
|---|---|---|---|---|
| No Trace | 75.13% | [72.69, 77.56] | [68.40, 81.76] | 2.74x |
| Full Trace | 81.76% | [79.50, 83.95] | [75.88, 87.39] | 2.58x |
| Loop Only | 85.63% | [83.61, 87.56] | [80.08, 90.59] | 2.66x |
| VoTA (no AE) | 99.41% | [98.99, 99.83] | [98.32, 100.00] | 2.00x |
| VoTA | 99.41% | [98.91, 99.83] | [98.32, 100.00] | 1.82x |
| AE Only | 99.92% | [99.75, 100.00] | [99.75, 100.00] | 1.00x |
| Exception Only | 99.83% | [99.58, 100.00] | [99.50, 100.00] | 1.20x |

**平均 CI width ratio: 2.00x** — clustering 使 CI 宽度加倍，主要影响中等准确率条件（no_trace/full_trace/loop_only），近饱和条件几乎不变。

### 关键 pairwise 显著性检验

| Comparison | Δ (pp) | Clustered 95% CI | Sig? |
|---|---|---|---|
| Exception Only vs AE Only | -0.08 | [-0.50, +0.25] | **NO** |
| Loop Only vs Full Trace | +3.87 | [-1.09, +8.91] | **NO** (p=0.06) |
| Exception Only vs Loop Only | +14.20 | [+9.24, +19.58] | **YES** |
| VoTA vs No Trace | +24.29 | [+17.90, +31.01] | **YES** |
| VoTA vs Full Trace | +17.65 | [+12.18, +23.53] | **YES** |
| Exception Only vs No Trace | +24.71 | [+18.24, +31.60] | **YES** |
| AE Only vs Loop Only | +14.29 | [+9.33, +19.75] | **YES** |
| VoTA (no AE) vs VoTA | +0.00 | [-0.25, +0.25] | **NO** |

### Reviewer 回应要点

1. 即使采用 problem-level clustered bootstrap（119 clusters, 10 tests/cluster），Table 2 中所有 ≥14pp 的差异仍然高度显著
2. Exception Only vs AE Only (Δ=0.08pp) 和 Loop Only vs Full Trace (Δ=3.87pp) 在 clustered CI 下不显著 — 但论文中也未声称这些是显著差异
3. Clustered CI 平均比 sample CI 宽 2.0x，说明 within-problem correlation 确实存在，但不足以改变核心结论

---
