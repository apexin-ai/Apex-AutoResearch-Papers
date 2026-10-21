# code add logdet

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add_logdet_20260516T124310_result.json`
- **Structured JSON:** [`e99da48d6bb5311b61d4.json`](../../sessions/e9/e99da48d6bb5311b61d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

- `rankme.py`: `compute_effective_rank` 新增 `log_det` 返回值（第三项），docstring 已更新
- `evaluate.py`: `evaluate_generation` 解包三项返回值，results dict 中 `log_det` 位于 `effective_rank` 之后

---
