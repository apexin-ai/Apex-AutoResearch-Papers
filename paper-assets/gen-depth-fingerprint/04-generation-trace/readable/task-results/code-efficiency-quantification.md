# code efficiency quantification

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_efficiency-quantification_20260517T115235_result.json`
- **Structured JSON:** [`87fa4ee0c9eb8c3a3f97.json`](../../sessions/87/87fa4ee0c9eb8c3a3f97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `/root/gen-depth-fingerprint/results/efficiency_comparison.json`。

核心数据：

| Metric | 7-feature | 4-det+surface |
|---|---|---|
| Models | 1× Pythia-410M | Pythia-410M + Pythia-1B |
| Total params | 410M | 1.41B (3.4×) |
| Forward passes/text | 1 | 3 (naive) / 2 (optimized) |
| GPU memory | 905 MB | 2,868 MB (3.2×) |
| Wall-clock | 9.7 ms/text | 22.8 ms/text |
| FLOPs/text | 1.94×10¹¹ | 6.68×10¹¹ (optimized, 3.4×) |
| **Speedup** | — | **2.35× slower** |

时间 breakdown (4-det+surface 的 2.28s/100 texts):
- FDG+LogProb (Pythia-410M pass): 0.858s (37.6%)
- Binoculars (410M+1B double pass): 1.359s (59.6%)
- LD-Score (CPU trigram JSD): 0.061s (2.7%)
- Surface features (CPU): 0.002s (<0.1%)

Binoculars 的双模型 forward pass 占了近 60% 的开销。7-feature ensemble 以单次 410M forward pass 实现了与 4-det+surface 统计不可区分的 binary F1 (0.701 vs 0.707)，但速度快 2.35×、显存省 3.2×。

---
