# kill p0 polling process

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_kill_p0_polling_process_20260523T202256_result.json`
- **Structured JSON:** [`10ca6011266e261a9ae7.json`](../../sessions/10/10ca6011266e261a9ae7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 项目 | 状态 |
|------|------|
| **PID 117506**（p0 轮询父进程） | 已杀 |
| **PID 117507**（p0 轮询子进程） | 已杀 |
| **PID 118504**（sleep 60 轮询等待） | 已杀 |
| **其他 p0 相关进程** | 无 |
| **crontab** | 无法通过 read_only 检查（无 shell 元字符），但进程列表中无 cron 守护进程运行 |
| **SS s456 训练（PID 112418）** | 正常运行，CPU 100%，已跑 144 分钟，占用 ~2.5GB 显存 |

`gpu_chain_next.sh`（PID 108997）保留——它是 SS s456 的父调度脚本，不触发 P0。P0 轮询已彻底清除。

---
