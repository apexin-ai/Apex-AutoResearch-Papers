# ops kill westd41074 correct server

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_westd41074_correct_server_20260519T192726_result.json`
- **Structured JSON:** [`ab46046fb5348e2190bf.json`](../../sessions/ab/ab46046fb5348e2190bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Kill 完成，结果确认：

- **PID 30737 已死** — GPU 1 显存已释放（0 MiB）
- **PID 26118 存活** — GPU 0 正常运行（30108 MiB）
- GPU 1/2/3 全部空闲

第一次 `kill` 实际上生效了，只是 nvidia-smi 在 3 秒内还有残留显示，稍后就清掉了。

---
