# analysis atlas v2 9cells

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_atlas_v2_9cells_20260515T024722_result.json`
- **Structured JSON:** [`b6fd106273a8fa5567f8.json`](../../sessions/b6/b6fd106273a8fa5567f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是 9-cell Atlas v2 分析摘要：

---

**3×3 矩阵 (RF accuracy)**

| | nucleus | temp09 | topk50 |
|---|:---:|:---:|:---:|
| Pythia-1.4B | 78.2% | 76.3% | 69.6% |
| OLMo-1B | 78.8% | 82.0% | 74.2% |
| GPT-2 XL | 83.3% | 85.4% | 74.5% |

**Director 关注的 3 个问题：**

1. **GPT-2 XL top-k 敏感性**: temp09→topk50 下降 -10.97pp（OLMo 仅 -7.83pp）。原因：GPT-2 XL 的优势来自 tail token variance（var_surprisal），top-k 硬截断直接消除这一信号源。OLMo 更依赖 p90_ppl（percentile-based），受截断影响较小。

2. **Feature importance 一致性**: p90_ppl 在 **9/9** cells 中均为 top-2（100%），var_surprisal 在 **7/9** cells 中为 top-2（78%）。仅 GPT-2 XL 的 2 个 cell 例外（p90_ppl 占比过高 >0.24，挤压了 var_surprisal 排名）。

3. **EDD < 3 的 cells**（threshold=0.80）：4 个 — pythia_topk50 (EDD=1), pythia_temp09 (EDD=2), olmo_topk50 (EDD=2), **gpt2xl_topk50 (EDD=2, 新增)**。3/4 是 top-k，确认 top-k 导致深层递归信号早期饱和。

**vs 8-cell 版本关键变化**: topk_k50 跨模型一致性从 ρ=0.736（2 models）升至 **ρ=0.811**（3 models），成为三种策略中最强的——top-k 的确定性截断使不同模型的 feature landscape 趋同。

---
