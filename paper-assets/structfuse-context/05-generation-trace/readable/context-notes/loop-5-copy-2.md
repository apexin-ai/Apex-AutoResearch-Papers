# agent / loop_5.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`4364c89d7428eb21b599.json`](../../sessions/43/4364c89d7428eb21b599.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-14T14:57:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-42106 上只能用 cuda:0 和 cuda:1，历史上有两次 GPU 越界违规
- m2_full_starcoder 正在 cuda:1 上跑，不要 kill 或干扰
- m1_reextract_v2 是 CPU 任务（4 workers 并行 CodeQL），不占 GPU，但磁盘 IO 重，不要在同一时间跑大量磁盘密集任务
- submit_training_job 命令必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ...`
- 服务器用 conda 环境（不是 venv），pip/python 在 `/root/miniconda3/bin/`
- ARR deadline May 25，关键路径极紧

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106，账号 root
- 工作目录：`/root/structfuse/`
- Python：`/root/miniconda3/bin/python`，conda base 环境
- 数据目录：`/root/autodl-tmp/structfuse/`（M1 数据、checkpoints、artifacts）
- M2 Qwen checkpoints：`/root/autodl-tmp/structfuse/full_m2_qwen_checkpoints/` （待 Worker 确认具体路径）
- M2 StarCoder checkpoints：`/root/autodl-tmp/structfuse/full_m2_starcoder_data/`
- M1 数据：`/root/autodl-tmp/structfuse/full_m2_data/`（~11K train/seed）
- wandb：离线模式（`WANDB_MODE=offline`）
- 活跃进程：
  - m2_full_starcoder: PID 74122, tmux session, cuda:1, cron 监控中
  - m1_reextract_v2: PID=m1_reextract_v2, 4 CPU workers 并行 CodeQL，cron 监控中
  - cuda:0 已空闲（m2_full_qwen 刚完成）

### 3. 📊 当前状态
收到 m2_full_qwen 完成回调（ANALYZING），已 spawn Worker `worker_analysis_m2_full_qwen_20260514T112525` 去服务器读日志、提取全部 9 runs metrics。**Worker 尚未回调，结果未知。**

Registry 中只有 random_s42 的 metrics（best R@1=0.553 @step1000），其余 8 runs 的 metrics 需要 Worker 从日志中提取。

- m2_full_qwen: ANALYZING → 等 Worker 回调后更新 registry → 推 DONE → 汇报 Director
- m2_full_starcoder: RUNNING，cuda:1，random_s42 跑到 step 2500（best R@1=0.454 @step1000）
- m1_reextract_v2: RUNNING，CPU，~15% 进度，预计还需 ~12h

**等待中**：
- Worker `worker_analysis_m2_full_qwen_20260514T112525` 回调
- m2_full_starcoder cron 完成回调
- m1_reextract_v2 cron 完成回调

### 4. 📋 待办
- Worker 分析回调到达 → 读 artifacts/m2_full_qwen_analysis.md → 更新 registry（conclusion + 全部 metrics + checkpoint_path + log_path）→ 推 DONE → 按 on-experiment-done skill 处理（success/negative 分叉）→ 汇报 Director（带 [资源] 行）
- m2_full_qwen conclusion=success 且 embedding > random 显著 → cuda:0 立即启动 plan_003 SWE-bench eval（脚本已 dry-run pass）或 plan_014 temperature ablation
- m2_full_qwen conclusion=negative → 按 red-section 产 Framing 提案，禁止默默跑下一个
- cuda:0 空闲 = 失职 → Worker 回调后必须立即铺下一个任务上去
- m2_full_starcoder 完成 → 合并 Qwen+StarCoder 全部 metrics → 统计检验（bootstrap CI, paired t-test）→ 最终 go/no-go for paper claims
- m1_reextract_v2 完成 → 更新 Claim 3 scalability 数字（coverage rate 预计从 36% 大幅提升）

### 5. 🎯 战略上下文
- **核心方向**："Hard negative mining for code retrieval: what works, what doesn't, and why"——系统性分析+机制解释论文
- **D024 重大 framing 重写**：旧 Claim 2（"embedding harms"）已证伪并移除。新叙事线：embedding universally helps → dataflow conditionally helps → mechanistic explanation via representation saturation
- **Claim 1（embedding > random）**：pilot 已一致确认（+1.6~2.0pp），full M2 提供 3-seed CI。这是最核心的 claim
- **Claim 2（dataflow conditional benefit）**：Qwen 正向、StarCoder 中性（pilot 已知）。D028 决定 "conditional benefit" 还是独立 claim
- **plan_013_starcoder pilot = negative**：strategy ranking 跨 encoder 不一致（dataflow encoder-dependent），但 embedding > random 两个 encoder 都成立
- **neg_difficulty_analysis**：已完成。Qwen pretrained margin 极小（0.017~0.074），StarCoder margin 大 2.6-4.1x。这解释了为什么 embedding negatives 对 Qwen 更 "hard"
- **n=3 统计功效限制**：df=2，Type II error 高。Discussion 必须讨论
- **关键路径**：M2(~May 18) → plan_014(~May 19.5) → plan_003(~May 21) → 统计+初稿(~May 24) → ARR May 25
- **易错点**：
  - D026 已决定 s42 保持 3 epochs、s43/s44 减至 2 epochs——不要假设所有 seed 都是相同 epoch 数
  - Checkpoint 有两种：best_by_val_loss 和 best_by_recall_at_1，下游 eval 用哪个需要 Director 决定
  - plan_015（dynamic mining）和 plan_017（inference-time graph）是 0 GPU-h 的写作任务，可以在等 GPU 时并行做


---
