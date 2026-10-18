# diagnose acis k03 cron

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_acis_k03_cron_20260517T072404_result.json`
- **Structured JSON:** [`f9f54d58a450bb8bf289.json`](../../sessions/f9/f9f54d58a450bb8bf289.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论：

- **进程未退出**，Cron 报告为误报
- 训练在 GPU 3 上正常运行（PID 11343），当前 step 2000/10000，margin_loss ~0.18，速度 4.3 sps
- 实例启动于 15:16 UTC（原 07:12 UTC 的实例可能被重启过，旧日志已覆盖）
- 预计约 31 分钟后（~15:56 UTC）完成
- Registry 已更新为 RUNNING，保留 cron 监控直到训练完成

---
