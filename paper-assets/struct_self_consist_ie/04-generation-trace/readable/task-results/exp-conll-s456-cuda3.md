# exp conll s456 cuda3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_conll_s456_cuda3_20260518T094912_result.json`
- **Structured JSON:** [`67c223519ad03635b221.json`](../../sessions/67/67c223519ad03635b221.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理和分析均已完成。结果汇报：

```
CoNLL seed=456:
- samples.jsonl 行数: 3,453
- gold-filtered n: 2,756
- greedy_f1: 0.9070, LP_sel_f1: 0.8997, LP_delta: -0.73pp
- degen: 62.9%
- best signal: SJ (f1=0.9025, delta=-0.45pp)

vs seed=42: greedy=0.9079, LP_delta=-1.05pp, degen=59.1%
```

seed=456 相比 seed=42：greedy F1 基本持平（0.9070 vs 0.9079），LP delta 略好（-0.73pp vs -1.05pp），degeneracy 稍高（62.9% vs 59.1%）。SJ 是最佳 selection signal（-0.45pp）。

---
