# diagnose eval pi05 l2norm k07 long seed47 w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_l2norm_k07_long_seed47_w41_20260529T023205_result.json`
- **Structured JSON:** [`c331d371d8885259e2ca.json`](../../sessions/c3/c331d371d8885259e2ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成，注册表已更新。

## 调查结果

**状态：已完成，SR=62.0%**

实验被重复提交到了两台服务器：

| 服务器 | 开始时间 (UTC) | 结束时间 (UTC) | 耗时 | EXIT_CODE | SR |
|--------|---------------|---------------|------|-----------|-----|
| westd-41074 | 01:06 | 03:44 | 156min | 0 | 62.0% |
| cqa1-33015 | 06:23 | 10:24 | 238min | 0 | 62.0% |

cron 监控报进程消失是因为 **w41 上的进程已在 03:44 UTC 正常退出**（不是被 kill）。cqa1 上的重复运行也正常完成。

两次运行 overall SR 一致（62.0%, 310/500），但 per-task 有差异（环境非确定性），w41 的 T9=94% vs cqa1 的 T9=82%。注册表已用 w41 的结果（先完成）更新为 DONE/success。

---
