# ops kill duplicate pid

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_duplicate_pid_20260512T183907_result.json`
- **Structured JSON:** [`24cd9e04a92611736e51.json`](../../sessions/24/24cd9e04a92611736e51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

1. **278651 fd/1** → `mvp_output.log (deleted)`（写入已删除文件句柄，确认是遗留重复进程）
2. **Kill 确认** — `kill 278651` 成功，状态 KILLED
3. **279220 存活** — PID 279220 正常运行，RSS 2148420 KB
4. **显存变化** — GPU 5: **18736 MiB → 9311 MiB**（释放 ~9425 MiB）
5. **日志最后 5 行** — ACDC 正常推进，24779/32491（76.2%），速度 4.74 it/s，预计剩余 ~27 分钟

---
