# ssh persist 5epoch recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_persist_5epoch_recompute_20260521T220030_result.json`
- **Structured JSON:** [`d5a93d6f072e0d05d063.json`](../../sessions/d5/d5a93d6f072e0d05d063.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 持久化完成
- `fewnerd_5epoch_s42/recompute_mv_results.txt`: 902 bytes
- `fewnerd_5epoch_s123/recompute_mv_results.txt`: 905 bytes
- `fewnerd_5epoch_s456/recompute_mv_results.txt`: 已存在（904 bytes，在 autodl-5090-c 上）

关键数值摘要：

| seed | greedy_f1 | mv_strict_f1 | mv_incl_f1 | oracle_f1 | Δ_SC strict | Δ_SC incl | α_crit |
|------|-----------|--------------|------------|-----------|-------------|-----------|--------|
| 42   | 0.7980    | 0.7935       | 0.7968     | 0.8781    | -0.45pp     | -0.12pp   | 0.399  |
| 123  | 0.7976    | 0.7941       | 0.7984     | 0.8814    | -0.35pp     | +0.08pp   | 0.399  |

---
