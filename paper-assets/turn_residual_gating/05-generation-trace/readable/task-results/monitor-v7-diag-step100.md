# monitor v7 diag step100

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v7_diag_step100_20260518T184649_result.json`
- **Structured JSON:** [`9194d8e27524ac962965.json`](../../sessions/91/9194d8e27524ac962965.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练在跑，GPU 97% 利用率。当前进度：micro-step ~200（global_step ~25）。GATE 日志目前只有 step=0 的记录。

已观察到的早期数据：
- micro-step 200 时 L_DIV=0.0000，gate mean=0.8054 — L_DIV 已经掉到 0，值得关注
- L_NTP 从 2.03 → 1.31（step 100 micro）→ 1.46（step 200 micro），正常下降中
- L_GAR 基本持平在 0.23 附近，尚未出现明显下降

4.5 分钟后再检查，等待 global_step 50/100 的 GATE 数据出现。

---
