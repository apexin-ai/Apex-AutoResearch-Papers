# ssh kill orphan cuda0

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_orphan_cuda0_20260515T144805_result.json`
- **Structured JSON:** [`f24964dc869b472b5751.json`](../../sessions/f2/f24964dc869b472b5751.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- **PID 111481**: 已杀死（日志最后可见 `Terminated` + `EXIT_CODE=129`）
- **PID 112299**: 存活，运行 1h00m55s
- **GPU 显存**: GPU 0 占用 71.6GB / 97.9GB（孤儿进程的 ~22GB 尚未完全释放或被当前进程回收），GPU 1 占用 22.4GB / 97.9GB
- **训练进度**: 当前进程正常推进，已到 129/444 步（~29%），~36s/it

---
