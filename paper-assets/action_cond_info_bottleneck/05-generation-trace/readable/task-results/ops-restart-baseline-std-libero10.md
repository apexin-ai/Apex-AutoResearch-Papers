# ops restart baseline std libero10

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-baseline-std-libero10_20260516T032009_result.json`
- **Structured JSON:** [`20e49a481daef65779f7.json`](../../sessions/20/20e49a481daef65779f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现关键事实：用户的前提不成立。先汇报情况，等用户确认再决定是否 kill+重启。

## 调查结果

**PID 733616 不是"未知进程"，它是 baseline_std libero_10 eval 本身的子进程，目前还活着。**

- 父进程 PID 733608（bash wrapper）启动时间 16:16 分钟前
- 运行命令：`lerobot-eval --policy.path=lerobot/smolvla_libero --env.task=libero_10 --eval.n_episodes=50 --output_dir=/root/acib/outputs/baseline_std_v3/libero_10`
- output 目录已创建 `videos/` 子目录（11:08 创建，正在写）

这条命令与 `scripts/eval_baseline.py` 内部展开的 lerobot-eval 命令一致（eval_baseline.py 只是个 subprocess 包装器）。所以**旧 eval 并没有死，只是某些 PID（708166, 738549）是已退出的辅助进程**。

**GPU 1 实际占用**：
- PID 733616（lerobot-eval libero_10）6.6GB ← 仍在跑的 baseline_std eval
- PID 744808（`scripts/train_acib.py ... --output_dir /root/acib/outputs/acib_v5_div_reg_seed2`）16.2GB，刚启动 1:50 ← 这是 seed2（不是用户记录的 PID 736291，应该是新启动的）

## 建议

按 C001 约束，启动新 eval 前必须 kill 旧的同 output_dir 进程。但这里旧 eval 还活着且产出在持续写，**贸然 kill 会丢失 16 分钟进度**。

请确认下一步：
- **选项 A**：保留 PID 733616 不动，等它自然完成（推荐——eval 还活着，无需重启）
- **选项 B**：仍然 kill 733616/733608 重启，理由是？

需要你拍板再操作。

---
