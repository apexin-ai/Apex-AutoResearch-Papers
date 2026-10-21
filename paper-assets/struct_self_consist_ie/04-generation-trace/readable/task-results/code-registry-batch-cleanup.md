# code registry batch cleanup

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_registry_batch_cleanup_20260518T195913_result.json`
- **Structured JSON:** [`498e769fb1ff19548ab3.json`](../../sessions/49/498e769fb1ff19548ab3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5个实验全部注册成功，状态均为 DONE。

| 实验 | conclusion | 状态 |
|---|---|---|
| `exp_ccs_selection` | negative | DONE |
| `exp_entity_consensus` | negative | DONE |
| `exp_adaptive_temperature` | negative | DONE |
| `exp_diagnostic_calibration` | negative | DONE |
| `exp_epoch_dgs_analysis` | success | DONE |

无失败。每个实验经过完整状态机 PREPARING → PENDING → QUEUED → ALLOCATED → RUNNING → DONE，hypothesis、conclusion、checkpoint_path、log_path、spec 均已设置。

---
