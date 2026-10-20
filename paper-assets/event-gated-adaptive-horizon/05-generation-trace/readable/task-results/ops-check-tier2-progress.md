# ops check tier2 progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-tier2-progress_20260527T231456_result.json`
- **Structured JSON:** [`7d43bd5876d1c6ec59b3.json`](../../sessions/7d/7d43bd5876d1c6ec59b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Tier 2 实验状态

| 实验 | 子PID | 当前 step | 目标 | 运行时长 | GPU 显存 | 状态 |
|---|---|---|---|---|---|---|
| exp_walker_008d_s6 | 660537 | **8000** | 105K | ~7h | 3255 MiB | **HUNG** |
| exp_walker_008d_s7 | 660817 | **8000** | 105K | ~6h50m | 3255 MiB | **HUNG** |

**两个实验都卡死了。** 具体证据：

- stdout 日志最后输出在 step 8000（4 个 train_return episode 行），之后再无任何输出
- 日志文件 mtime 分别停在 07:15:48 和 07:16:02，距今约 **7 小时无新写入**
- metrics.jsonl 仅记录到 step 5000（eval_return ≈ 31）
- 子进程状态 `Rl`，CPU 占用 1300%+，GPU 利用率仅 20% — 在空转
- fps = 0

**结论**: 进程在 step 8000 后进入训练循环时挂起（可能是 gradient update 内部死循环或数据处理阻塞）。进度 8K/105K = 7.6%，ETA 无法估算（速度为 0）。需要 kill 后排查代码问题再重启。

---
