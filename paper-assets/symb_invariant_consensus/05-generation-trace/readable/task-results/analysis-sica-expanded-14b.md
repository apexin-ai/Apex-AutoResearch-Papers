# analysis sica expanded 14b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sica_expanded_14b_20260516T192141_result.json`
- **Structured JSON:** [`2ffb3c5ccc3be46bf6fc.json`](../../sessions/2f/2ffb3c5ccc3be46bf6fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Exp-001 (N=804) 结果：SICA 几乎无优势**

| | SICA | SC | Gap |
|--|--|--|--|
| Overall (804) | 76.49% | 76.24% | +0.25 pp |
| ProofWriter D5 (600) | 75.50% | 75.17% | +0.33 pp |
| FOLIO (204) | 79.41% | 79.41% | 0.00 pp |

- **Bootstrap p = 0.7433** — 完全不显著，95% CI = [-1.12, +1.62] pp
- **Disagreements**: 31 题中 SICA wins 16, SC wins 14, both wrong 1 → 净收益仅 +2 题
- **Tie-break 模式确认**: 20/31 (65%) 的 disagreements 是 SC tie-break (如 6:6 投票)
- **Capability trap**: SICA 仅在 multi-candidate 问题上有微弱优势 (+0.65 pp)，unanimous 问题为 0
- **Constraint quality**: 平均 21.5 unique constraints/题，exclusion rate 约在活跃使用中，但过滤力度不足以改变最终答案

与 D012 pilot (+3.3 pp) 相比，full-scale 实验的 gap 从 3.3 pp 坍缩到 0.25 pp，说明 pilot 的正向信号是小样本偏差。

报告已输出到 `/root/symb_invariant_consensus/results/exp001_analysis.md`。

---
