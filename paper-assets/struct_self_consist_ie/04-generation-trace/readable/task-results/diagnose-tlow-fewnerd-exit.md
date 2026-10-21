# diagnose tlow fewnerd exit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_tlow_fewnerd_exit_20260520T193849_result.json`
- **Structured JSON:** [`99b27bf5a4ba266460de.json`](../../sessions/99/99b27bf5a4ba266460de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：正常完成。** Registry 已更新为 DONE/success。

关键指标：
- 37648 instances × 8 samples, T=0.5, 耗时 ~15 min
- Greedy F1: **0.7938**, Oracle F1: **0.8473** (headroom +0.0535)
- Fleiss' κ: 0.7567, Soft Jaccard: 0.9164
- Structural > Surface: **YES** (Δ=+0.0178)
- Logprob AUROC: 0.7185
- Verdict: **MARGINAL**

输出文件：`samples.jsonl` (716MB) + `report.json`，cuda:2 已释放。

---
