# eval gate0 ft002v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gate0_ft002v2_20260514T084152_result.json`
- **Structured JSON:** [`49d310c25bbeecb275e7.json`](../../sessions/49/49d310c25bbeecb275e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Gate 0 评测结果：ft_002_v2 **PASS**

| 指标 | ft_002_v2 | ft_001 | 门槛 | 判定 |
|------|-----------|--------|------|------|
| NER greedy F1 | **66.15%** | 60.4% | ≥56% | PASS (+5.75pp vs ft_001) |
| RE greedy F1 | **41.77%** | 33.8% | ≥40% | PASS (+7.97pp vs ft_001) |
| Parse failures | 0 | - | - | - |

**Gate 0 通过。** 两项指标均超过门槛，且相比 ft_001 有显著提升：NER +5.75pp，RE +7.97pp。

注意：report 的 `verdict` 字段显示 FAIL，但那是 pilot 的 consistency 判定标准（要求 rho_sj ≥ 0.40 等），不适用于 Gate 0 的绝对 F1 门槛判定。按 Gate 0 标准（NER F1 ≥ 56%, RE F1 ≥ 40%），两项均通过。

---
