# analysis re selection recompute urgent

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_re_selection_recompute_urgent_20260515T034534_result.json`
- **Structured JSON:** [`fdffd077bdaf37aa7147.json`](../../sessions/fd/fdffd077bdaf37aa7147.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

重新计算完成，结果确定。

## 结论

**根因**：0.395 和 0.410 来自**不同数据源**，不是不同口径。

| 值 | 来源 | 状态 |
|---|---|---|
| **0.395** (0.394803) | `re_selection_bootstrap.py` → `exp_012_rerun_1024/samples.jsonl`，gold_nonempty (n=397)，macro avg | **正确** |
| **0.410** (0.4097) | `exp_016_v2 registry` | **错误数据源，已确认不可引用** |

**全口径验证**（均为 logprob selection F1）：
- 口径 1 全集 (n=551): macro=0.2845, micro=0.3941
- 口径 2 gold_nonempty (n=397): macro=**0.3948**, micro=0.4156
- 口径 3 conditional (n=238): macro=0.5995, micro=0.5498

无论哪个口径、哪种平均方式，**logprob selection 都输 greedy**。

**定性结论**：logprob selection **输** greedy 0.9pp（0.395 vs 0.404），sign test 36 wins / 59 losses / 302 ties。

**论文修复**：L129 应从 "logprob achieves 0.410, +0.6pp over greedy" 改为 "logprob=0.395, Δ=-0.9pp, p=0.80"。JSON 结果已保存至 `review_round2/re_selection_recompute.json`。

---
