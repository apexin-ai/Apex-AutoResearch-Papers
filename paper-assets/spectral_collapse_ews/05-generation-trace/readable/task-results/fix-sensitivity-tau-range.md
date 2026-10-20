# fix sensitivity tau range

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_sensitivity_tau_range_20260517T064535_result.json`
- **Structured JSON:** [`565a6d7c1dd62953f571.json`](../../sessions/56/565a6d7c1dd62953f571.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成：

- `TAU_VALUES` 已改为 `[0.002, 0.005, 0.01]`
- `signal` 默认为 `"log_det"`，通过 `--signal` 参数可覆盖，已接入 `config.controller_signal`
- `--help` 验证通过

---
