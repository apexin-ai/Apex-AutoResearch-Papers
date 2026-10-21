# diagnose westd 11672 connectivity

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd_11672_connectivity_20260517T054209_result.json`
- **Structured JSON:** [`e2a5d74240e9c855c191.json`](../../sessions/e2/e2a5d74240e9c855c191.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**westd-11672 不可达。** 两次连接均失败，错误一致：

```
[Errno None] Unable to connect to port 11672 on 36.103.198.204
```

连接在 0.1-0.3 秒内被拒绝（不是超时），说明端口未开放——服务器很可能已关机或被平台回收。

### 实验状态判断

| 实验 | 状态 |
|------|------|
| eval_sft_rasp_20_seed456 | **failed**（cron 已标记） |
| eval_sft_rasp_20_seed123 | **failed**（cron 已标记） |
| eval_sft_standard_20_seed123 | **failed**（cron 已标记） |
| eval_sft_standard_20_seed456 (pid=75384) | **实际已死**，服务器不可达，进程不可能存活 |

### 结论

westd-11672 当前完全不可用。4 个实验均应视为 failed。需要在平台侧确认服务器状态（是否过期/欠费/维护），恢复后重新提交实验。

---
