# ssh kill 392856 deploy perdof norm02 seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-392856-deploy-perdof-norm02-seed43_20260517T113632_result.json`
- **Structured JSON:** [`bfadb2dbbdaed969d816.json`](../../sessions/bf/bfadb2dbbdaed969d816.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在只剩一个实例了。结果汇总：

---

**Kill 结果**：PID 392856 已终止 ✓

**新实验**：
- **PID**: 401104
- **GPU cuda:2**: RTX 4090, 5645MiB / 24564MiB, 17% util
- **启动日志**:
```
[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt (337,438 params)
[eval] Override max_correction_norm = 0.2
[eval] Loading LIBERO object environments...
[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[eval] 10 tasks loaded.
```

注意：首次用 `bash -lc` 启动时 SSH 工具报超时但进程实际启动了，导致出现重复实例。已杀掉重复的 PID 399712，当前只有 401104 在运行。

---
