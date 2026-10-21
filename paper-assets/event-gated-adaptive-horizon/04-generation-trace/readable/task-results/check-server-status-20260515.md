# check server status 20260515

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server-status-20260515_20260515T120747_result.json`
- **Structured JSON:** [`3f0d09d76676f5cf9893.json`](../../sessions/3f/3f0d09d76676f5cf9893.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### exp_015b_frozen_dt_emb
- **PID 142033**: **已死亡**，进程不存在
- **日志**: 以 `RuntimeError: cannot schedule new futures after shutdown` 结束，退出码 1 — **崩溃退出**（dm_control 渲染线程池关闭后仍被调用）
- **logdir**: `metrics.jsonl` 不存在 — 未产出指标文件

### exp_009d_baseline_walker_s0
- **日志**: `can't open file '/root/runs/event-gated-adaptive-horizon/dreamer.py': No such file or directory`，退出码 2 — **启动即失败**，脚本路径错误
- **logdir**: 目录不存在 — 无任何输出
- **进程**: 无相关进程在运行

### GPU 状态
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 0% | 0 / 97887 MiB |
| 1 | RTX PRO 6000 Blackwell | 0% | 0 / 97887 MiB |

两块 GPU 完全空闲，无任何训练任务占用。

### 其他进程
唯一相关的后台进程是 `checkpoint_monitor.py`（PID 123058），自 5月14日 起运行中。

**结论**: 两个实验均已停止，GPU 空闲。exp_015b 因 dm_control 渲染线程错误崩溃；exp_009d 因脚本路径错误从未成功启动。

---
