# check 340m eval status

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_340m-eval-status_20260521T230006_result.json`
- **Structured JSON:** [`a6a127636afb559e121d.json`](../../sessions/a6/a6a127636afb559e121d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 检查项 | 状态 |
|--------|------|
| **进程 PID 777365** | 存活，运行 33 分 11 秒，状态 `Ss+` |
| **tmux session** | ssh_read_only 不允许 tmux 命令，无法检查 |
| **GPU** | 利用率 0%，显存占用 1253 MiB / 97887 MiB — 当前处于模型加载/数据准备阶段，非计算密集阶段 |
| **输出目录** | 已有 6 个模型的结果：`GDN-h12-1`, `GDN-h24-1`, `GDN-h3-1`, `GDN-h6-1`, `GDN-pure`, `RetNet-pure` |
| **日志** | 正在跑第 7/15 个模型 `RetNet-h24-1`，刚完成模型加载，正在评估 hellaswag（用的缓存数据集，网络不通但不影响） |

进程正常运行中，进度 6/15 已完成，当前在第 7 个模型的 benchmark 评估阶段。

---
