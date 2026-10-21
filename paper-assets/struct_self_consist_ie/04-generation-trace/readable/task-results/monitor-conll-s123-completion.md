# monitor conll s123 completion

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_conll_s123_completion_20260518T103545_result.json`
- **Structured JSON:** [`e137eaebb0c3424dd0b6.json`](../../sessions/e1/e137eaebb0c3424dd0b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇报结果：

---

**CoNLL seed=123 — 完成**
- samples.jsonl 行数: 3,453 ✓
- gold-filtered n: 2,756
- greedy_f1: **0.9077**, oracle_f1: 0.9476, headroom: 3.99pp
- LP_sel_f1: 0.8999, **LP_delta: -0.77pp**
- degen (CF1 gold-filtered): **63.0%**
- 其他 signal: SJ=-0.56pp, FK=-0.53pp, VC=-0.37pp, EM=-0.66pp

**三 seed 汇总对比:**

| | seed=42 | seed=456 | seed=123 | **3-seed mean** |
|---|---|---|---|---|
| greedy_f1 | 0.9079 | 0.9068 | 0.9077 | **0.9075** |
| LP_delta | -1.05pp | -0.73pp | -0.77pp | **-0.85 ± 0.17pp** |
| degen% | 59.1% | 62.9% | 63.0% | **61.7 ± 2.2%** |

三个 seed 的 greedy F1 非常一致（0.9068–0.9079），LP selection 全部低于 greedy（均为负 delta），退化率约 62%。所有 signal 的 selection F1 均未能超过 greedy baseline。

---
