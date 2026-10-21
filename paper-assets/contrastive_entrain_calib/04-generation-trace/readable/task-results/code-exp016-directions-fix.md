# code exp016 directions fix

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp016-directions-fix_20260518T205541_result.json`
- **Structured JSON:** [`5cb044e91c189ea1bc9f.json`](../../sessions/5c/5cb044e91c189ea1bc9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已修复。`load_directions` 现在正确地将 `directions.pt` 作为 dict 解析，通过 `data["d_syc"]` 取出 tensor 后再做 layer 索引，同时加了 `weights_only=True`。验证确认文件中无残留的 `raw[` 模式。

---
