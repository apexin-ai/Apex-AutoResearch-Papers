# diagnose gpu0 v5 exit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu0-v5-exit_20260514T041809_result.json`
- **Structured JSON:** [`05bad3de6c7906a023c8.json`](../../sessions/05/05bad3de6c7906a023c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**退出原因：killed（被主动终止）**

日志最后关键行：
```
Terminated
(EngineCore pid=935125) INFO 05-14 12:16:49 Shutdown initiated (timeout=0)
(EngineCore pid=935125) INFO 05-14 12:16:49 Aborting 1 requests
[Thu May 14 12:16:49 CST 2026] All tasks complete.
(EngineCore pid=935125) INFO 05-14 12:16:49 Shutdown complete
```

- `Terminated` = 进程收到 SIGTERM，是 shell 的标准提示，与 ops worker kill PID 一致
- vLLM EngineCore 在收到信号后做了 graceful shutdown，中断了 1 个正在处理的请求
- 时间戳 05-14 12:16:49

**GPU0 当前状态：已有新进程在跑**
- PID 789051，占用 28004 MiB 显存，大概率是 ops worker 启动的 v6

---
