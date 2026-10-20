# fix calibrate tau k

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_calibrate_tau_k_20260516T125722_result.json`
- **Structured JSON:** [`7c77e51955235a91b04d.json`](../../sessions/7c/7c77e51955235a91b04d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

- **修改**: `uniform_share` 从 `1.0 / T` (= 0.10) 改为 `0.50` (= `r_base`)，同时用 `headroom = target_max - uniform_share` 和 `max()` 防除零替代原来的 `if/else` 分支
- **验证**: k = 3.2785，在 1–5 范围内

---
