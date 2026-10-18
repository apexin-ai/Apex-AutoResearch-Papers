# ops kill duplicate gemma2

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_duplicate_gemma2_20260515T191937_result.json`
- **Structured JSON:** [`ab7efdfdfb919b8110b0.json`](../../sessions/ab/ab7efdfdfb919b8110b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **PID 364035** — 已成功 kill，进程不存在
- **PID 364542** — 在 kill 前就已经不存在了（可能已自行结束或崩溃）
- **GPU 显存** — 当前只有 PID 362950 占用 16966 MiB，364035 的 ~18GB 显存已释放

注意：注册的 `gemma2_downstream_k2_4task` 进程（PID 364542）已经消亡，可能需要检查其输出日志确认是正常完成还是异常退出。

---
