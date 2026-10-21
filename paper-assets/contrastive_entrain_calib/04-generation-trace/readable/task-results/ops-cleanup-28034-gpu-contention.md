# ops cleanup 28034 gpu contention

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-28034-gpu-contention_20260521T071808_result.json`
- **Structured JSON:** [`ee90fd58c36ae2f88d6a.json`](../../sessions/ee/ee90fd58c36ae2f88d6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

### GPU 状态
**无需清理。** 所有 eval 进程已经自行结束，4 块 RTX 5090 全部空闲（每块仅 2MiB 占用，0% 利用率）。没有 tmux session 在运行。

### Checkpoints（`/root/autodl-tmp/checkpoints/exp003/`）
10 个 checkpoint 存在：
- checkpoint-1000 ~ checkpoint-3000（5/20 20:49）
- checkpoint-4000（5/20 22:13）
- checkpoint-4500（5/20 12:33）
- checkpoint-5000（5/20 18:10）
- checkpoint-5500（5/21 00:21）
- checkpoint-6000, 6500, 7000（5/21 12:38）

项目目录下有 5 个 symlink 指向数据盘（1000-4000, 5000），缺 4500/5500/6000/6500/7000 的 symlink。

### Eval 结果（`results/exp003_d027_eval/`）
已产出 6 个 checkpoint 的评估结果：
| Checkpoint | 状态 |
|---|---|
| ckpt1000 | ✅ 完成 |
| ckpt2000 | ✅ 完成 |
| ckpt3000 | ✅ 完成 |
| ckpt4000 | ✅ 完成 |
| ckpt4500 | ✅ 完成 |
| ckpt5500 | ✅ 完成 |

**缺失**：ckpt5000、ckpt6000、ckpt6500、ckpt7000 的 eval 结果尚未产出（可能是进程在竞争中崩溃，未完成这几个 checkpoint 的评估）。

---
