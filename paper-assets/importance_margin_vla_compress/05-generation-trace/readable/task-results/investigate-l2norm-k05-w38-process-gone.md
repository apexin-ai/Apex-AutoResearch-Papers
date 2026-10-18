# investigate l2norm k05 w38 process gone

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_l2norm_k05_w38_process_gone_20260527T122736_result.json`
- **Structured JSON:** [`d2087c65dc27eac01690.json`](../../sessions/d2/d2087c65dc27eac01690.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无法清空 conclusion 字段（只接受预定义值）。registry 中 conclusion="killed" 是误判产生的脏数据，但进程实际正在运行。

## 总结

- **进程正常运行**，PID 250745，在 GPU 3 上跑 π0.5 L2norm k=0.5 Long，已完成 Task 0 (SR=58%)，正在 Task 1，预计 ~3h 完成
- **误报原因**：实验用 nohup 启动，没有 tmux session，日志路径不在 reconcile_crons 监控目录
- **Registry 脏数据**：conclusion="killed" 是误判设置的，无法清空（API 不支持空值）。实验完成后用正确 metrics 更新即可覆盖
- **服务器状态正常**：4 GPU 全部在用，磁盘充裕

---
