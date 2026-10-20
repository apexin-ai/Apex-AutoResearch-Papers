# check d129 1 7b isr b03 s43 urgent

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d129-1_7b-isr-b03-s43-urgent_20260518T062145_result.json`
- **Structured JSON:** [`fbc2c083e28ca3d9d648.json`](../../sessions/fb/fbc2c083e28ca3d9d648.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**d129-1.7b-isr-b03-s43 状态：崩溃于 step 100，已重启**

| 项目 | 详情 |
|------|------|
| 崩溃原因 | 磁盘满（250G/250G，0 可用） |
| 崩溃位置 | step 100/500（03:18 UTC） |
| 磁盘清理 | 删除崩溃输出 (8.7G) + 5个旧实验 checkpoint 副本 (~80G) → 84G 可用 |
| 重启时间 | 14:24:55 UTC |
| 新 PID | **148580** |
| tmux | `d129-isr-b03-s43` |
| GPU | cuda:0, 39.3GB 占用, 69% util |
| 预计完成 | ~16:05 UTC (~1h40m) |
| 当前进度 | step 2/500, ~12s/step |
| Cron | 每小时 :53 检查（14:53, 15:53, 16:53） |

**nvidia-smi**:
- GPU 0: 39303MiB / 97887MiB, PID 148580 (python)
- 无其他 GPU 进程

**附注**: d129-random-b01-s43-r2 训练已完成（500步, 08:50 UTC），eval+classify 已执行，tmux session 仍存活但空闲。

---
