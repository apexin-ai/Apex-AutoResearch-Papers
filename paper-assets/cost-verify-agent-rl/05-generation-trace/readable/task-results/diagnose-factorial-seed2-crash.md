# diagnose factorial seed2 crash

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_factorial-seed2-crash_20260518T104524_result.json`
- **Structured JSON:** [`6dccf68673313eee0c52.json`](../../sessions/6d/6dccf68673313eee0c52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

| 项目 | 状态 |
|------|------|
| **PID 505305** | 已死，无任何 factorial 相关进程存活 |
| **tmux session** | 不存在（仅有 `gsweep_watchdog`） |
| **GPU 0,1** | 空闲（0MiB, 0% util） |
| **GPU 2,3** | 被其他进程占用（PID 423548/423549, ~29GB each, 95-96% util） |

### 崩溃原因：`/tmp` 磁盘满

```
OSError: [Errno 28] No space left on device
```

进程完成了 step:0 的 validation，但在启动第一轮 training rollout 时，`fast_downward` 库尝试将 `libdownward.so` 复制到 `/tmp` 失败。Ray 也报告 `/tmp/ray/session_*` 已超过 95%（仅剩 6MB / 30GB）。

当前 `/` 分区（含 `/tmp`）已用 24G/30G (80%)，崩溃时应该更满。seed1 的日志（20MB vs seed2 的 1MB）加上 Ray session 数据可能是主要占用。

**恢复前需要**：清理 `/tmp` 下的 Ray session 残留和其他临时文件。

---
