# ops investigate cuda0 pid58051

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate-cuda0-pid58051_20260515T010611_result.json`
- **Structured JSON:** [`b1004f8f34891bd58dd2.json`](../../sessions/b1/b1004f8f34891bd58dd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查报告：cuda:0 PID 58051

**进程身份（已知合法实验，非未知）**
- 命令: `python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s43_r3`
- CUDA_VISIBLE_DEVICES=0 ✅（合规，未越界）
- CWD: `/root/solver-trace-ablation`
- 用户: root
- 运行时长: 04:32（启动 ~01:02 UTC，当前 step 24，活跃训练中）
- 输出目录: `/root/autodl-tmp/outputs/exp1_isr_b03_s43_r3`，reward_log.jsonl 持续更新（最新 timestamp 01:06:46 UTC）

**进程链**
- 58051 (python3 train_grpo) ← 58050 (`timeout 86400 env bash -c ...`) ← 58046 (`bash -c rm -f /tmp/agent-ml...` submit_training_job 包装器) ← 51291 (tmux session)

**身份判定**
这是 **exp1-isr-b03-s43-r3**（additive_bonus reward, seed 43, beta 0.3, run 3）实验，与 cuda:1 的 exp1-random-b03-s44-r2（PID 51297）配对运行。明显是另一个 Worker 通过 submit_training_job 提交的合法 exp1 系列实验，遵守了 C001/C002（用 train_500_seed42.jsonl，显式 export CUDA_VISIBLE_DEVICES=0）。

**建议: 不要 kill**
- 进程合法、活跃训练（24/500 步，~21s/step → 估计还需 ~2.8 小时）
- 配对设计：cuda:0 跑 isr 条件 vs cuda:1 跑 random 条件，两张 GPU 各占一张，符合 C002
- 之前 Worker 报告"unknown"是因为没有查 cmdline；查 registry 时大概率能找到对应实验记录（建议核对 registry 里 exp1-isr-b03-s43-r3 是否存在以确认）

---
