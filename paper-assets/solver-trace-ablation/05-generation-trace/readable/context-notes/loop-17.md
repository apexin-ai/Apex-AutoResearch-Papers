# agent / loop_17.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_17.md`
- **Structured JSON:** [`d569704977de98a5368f.json`](../../sessions/d5/d569704977de98a5368f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: idle_timeout
updated: '2026-05-16T10:58:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单只有 westd-39279:cuda:0 和 cuda:1，不可用其他卡
- Round 2 实验全部用 `--no_wandb`（服务器无 wandb key），metrics 从 reward_log.csv / eval 输出提取
- submit_training_job command 必须 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && ..."`——裸 source 在 tmux sh 下会 127
- 磁盘空间紧张（刚清理过 54GB），提交前应检查 `df -h /root/autodl-tmp/`，中间 checkpoint 及时清理
- 训练脚本路径：`python3 scripts/train_grpo.py --config configs/...`（不是根目录下的 train_grpo.py）

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279，工作目录 `/root/solver-trace-ablation`
- Python：`/root/miniconda3/bin/python3`（conda base env）
- 模型：`/root/autodl-tmp/models/Qwen3-4B`（Round 2 全部用 4B）
- 数据：`data/train_500_seed42.jsonl`（训练），`data/proofwriter_fol_100.jsonl`（eval）
- 输出目录：`/root/autodl-tmp/outputs/`
- 活跃进程：plan018-random-b01-s45-r2（PID 679720, tmux session, cuda:0）
- 无 wandb，无 HF 下载需求

### 3. 📊 当前状态
**刚做完**：sweep-isr-b02-s44 磁盘满失败 → 清理 54GB → 重提交 → 训练完成 500/500 步。已派 eval Worker（worker_eval_sweep-isr-b02-s44_20260516T065624）跑 eval_sta.py + classify_h7.py。

**Registry 状态**：
- RUNNING：`plan018-random-b01-s45-r2`（Random β=0.1 s45 对照组，cuda:0）
- ANALYZING：`sweep-isr-b02-s44`（等 eval Worker 回调）
- PREPARING × 13：5-seed 扩展实验（exec-only s45/s46, random s45/s46, ISR s46 等）

**等待中**：
- Worker 回调：eval Worker 完成 → 标 conclusion + 汇报 Director
- Cron：plan018-random-b01-s45-r2 完成回调
- cuda:1 空闲，等 eval 结束后可排下一个 PREPARING 实验

### 4. 📋 待办
- eval Worker 回调到达 → 检查 h7a/genuine 指标，预期 h7a≈95-100% genuine=0%（与 s42/s43 一致）→ 标 success + 汇报 Director β=0.2 三 seed 全部完成
- plan018-random-b01-s45-r2 完成回调 → eval + hacking taxonomy → 标 conclusion
- cuda:1 空闲且 eval 完成 → 从 PREPARING 池挑下一个提交（优先 P2: sweep-random-b01-s45 或 P3: 5-seed 扩展）
- β=0.2 三 seed 全部 success 后 → 汇报 Director P1 完成，建议铺 P2/P3

### 5. 🎯 战略上下文
- **核心方向**：ISR 作为 Goodhart's Law 案例研究，DDL 2026-05-25（剩 9 天）
- **D095 Narrative A 已锁定**：H7a 是 GRPO-general seed-dependent，H7b 是 ISR-specific；genuine 无显著差异（p=0.182）
- **D101 Round 2 排期**：P1 β=0.2 三 seed（s42✓ s43✓ s44 分析中）→ P2 random s45 对照 → P3 5-seed 扩展
- **D102**：Goodhart 阈值锁定 β∈(0.05,0.1)，不加更多剂量点，多 seed 复现优先
- **易错点**：
  - 双实验并行时 RAM OOM（s45 曾被 kill，exit 137）——cuda:0+cuda:1 同时跑大实验要小心
  - 不要说 "H7 is ISR-specific"——只有 H7b 是，H7a 是 GRPO 通用的（来回修了 8 次）
  - conclusion=success 的判断标准：高 hacking + ISR collapse = 验证 Goodhart 假设 = success（不是 negative）


---
