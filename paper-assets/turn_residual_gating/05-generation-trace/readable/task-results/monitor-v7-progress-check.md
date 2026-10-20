# monitor v7 progress check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v7_progress_check_20260518T234724_result.json`
- **Structured JSON:** [`a6d9523be0edc16b1fd6.json`](../../sessions/a6/a6d9523be0edc16b1fd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

- **当前位置**: Epoch 2 (最后一个 epoch), data step 4500/8000, gs ~2562 / 3000 (~85%)
- **最新指标**: L_NTP=0.7697, L_GAR=0.0018, L_DIV=0.0000, Loss=0.7715, Gate=0.9523
- **最新 GATE 统计** (gs=2550): mean=0.9371, std=0.0526, min=0.7773, max=0.9922
- **剩余**: ~3500 data steps (~438 global steps), 约 15% 剩余
- **是否已完成**: no

日志无时间戳，无法精确估算剩余时间。Gate profile 稳定，L3/L4 层 gate 值持续最低 (~0.79-0.80)，高层 (L25-L27) 接近 1.0。

---
