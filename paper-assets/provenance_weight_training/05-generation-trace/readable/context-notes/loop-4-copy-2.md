# agent / loop_4.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`3f5a791ba6ea1e080a26.json`](../../sessions/3f/3f5a791ba6ea1e080a26.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-14T17:14:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 **cuda:0/1/2/3 on westd-47453**，不可用其他服务器或 GPU
- `submit_training_job` 命令**必须包含 `--eval_data_path data/human/eval_holdout.jsonl --eval_steps 500`**，否则训练完无 eval（grid_b2_0/b3_0_seed123 踩过此坑，需补跑 eval）
- 不要在有训练进程的 GPU 上并行跑诊断/eval 任务（D010 教训：显存 93/98GB 导致训练速度减半）
- adaptive_fix 实验的 WANDB_MODE=disabled（服务器无 wandb key），不要加 `--use_wandb`
- D012 实际修改是 n_min=3→2 + 可能引入了 early return (`alpha_0 >= tau → return 0`)，**D016 警告未结案**，论文中不要写"仅改了 n_min"
- Drayson et al. (EMNLP 2025) 用了同一公式 w=(1-q)^b（D013），framing 必须定位为"给 Drayson 框架加 principled adaptive b*"而非"提出 detect-and-reweight"

### 2. 🖥️ 基础设施快照
- **服务器**: westd-47453，4× RTX 6000 Pro 96GB
- **工作目录**: `/root/provenance_weight_training`
- **Python**: `/root/miniconda3/bin/python`（conda base，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **模型**: `/root/provenance_weight_training/models/Qwen/Qwen3-0.6B`
- **训练数据**: `/root/provenance_weight_training/data/scored_data.jsonl`（371499 docs，含 q-score）
- **Eval holdout**: `/root/provenance_weight_training/data/human/eval_holdout.jsonl`（~4.08M tokens，纯 FineWeb 人类文本）
- **Eval 脚本**: `/root/provenance_weight_training/eval_perplexity.py`（每次 ~44min，注意时间预算）
- **输出**: `/root/provenance_weight_training/output/models/&lt;exp_id>/`
- **检测器**: `/root/provenance_weight_training/output/detector_tfidf/`（TF-IDF+LR, AUC=0.939, ECE=0.048）
- **活跃进程**:
  - `grid_b_seed42_batch` — cuda:0, PID 50134, tmux=grid_b_seed42_batch（6 b 值串行，已完 b=0.5/1.0/1.5，当前 b=2.0 step 5149/6103）
  - `adaptive_fix_seed42` — cuda:1, PID 108213, tmux=adaptive_fix_seed42
  - `adaptive_fix_seed123` — cuda:2, PID 109357, tmux=adaptive_fix_seed123
  - `adaptive_fix_seed456` — cuda:3, PID 115066, tmux=adaptive_fix_seed456
- **活跃 Cron**: 4 个（上述 4 个实验各一）
- **活跃 Worker**: `worker_investigate_d012_alpha_eff_changes` (running) — 正在调查 D016（v1→v2 是否引入了 early return 混淆变量）

### 3. 📊 当前状态
**所有 4 张 GPU 满载运行。** 3 个 adaptive_fix (D012 修复版) + 1 个 grid_b_seed42_batch。

已完成的关键结果（seed123 为完整数据点）：
| 方法 | seed42 PPL | seed123 PPL | seed456 PPL |
|------|-----------|-------------|-------------|
| uniform | 17.69 | 17.69 | 17.70 |
| adaptive (旧, n_min=3) | 17.69 (=uniform) | 17.63 | 17.64 |
| grid-best (b=0.5) | 等 batch 完 | 17.638 | QUEUED |
| adaptive_fix (n_min=2) | **RUNNING** | **RUNNING** | **RUNNING** |

grid_b seed123 六个 b 值全 DONE：b=0.5(17.638) < b=1.0(17.674) < b=1.5(17.701) < b=2.0(17.725) < b=3.0(17.76) < b=5.0(17.80)。PPL 随 b 单调递增，b=0.5 最优。

**等待中**:
- 4 个 cron 回调（上述 4 个 RUNNING 实验）
- Worker D016 调查结果（git diff 确认 v1→v2 到底改了什么）
- 6 个 grid_b_seed456 实验 QUEUED（等 GPU 释放）

### 4. 📋 待办（条件触发式）
- **adaptive_fix 3 seeds 全部完成 → MVP 判定**: 3-seed 均值 ≥ 90% grid-best 改善量 → PASS；任一 seed adaptive PPL > uniform → FAIL (D014 per-seed 一致性要求)
- **grid_b_seed42_batch 完成 → 汇总 seed42 六个 b 值 PPL**，确认 seed42 也是 b=0.5 最优（预期与 seed123 一致）
- **D016 Worker 返回 → 更新 memory.md**: 如确认有 early return，论文叙述改为"最终算法"而非"仅修 n_min"
- **GPU 释放（adaptive_fix 完成后） → 优先跑 grid_b_seed456 六组**（批量脚本，参照 grid_b_seed42_batch 的 `run_grid_b_seed42.sh`）
- **MVP PASS → 触发 post-mvp-kickoff**: paper_framing 定稿 → experiment_plan → 扩展到多污染比例(20%/60%) + detector ablation + batch_size=16
- **MVP FAIL → Framing 提案**: 按 red-section skill 产出 3 种 narrative 备选提交 Director

### 5. 🎯 战略上下文
**核心结论**: adaptive b* 在 2/3 seeds 优于 grid-best（即使 buggy n_min=3 版本），但 seed42 因 ESS 钳制退化为 uniform。D012 修复版（n_min=2）正在跑，是 MVP 成败关键。

**决策链**: D001(AAAI)→D003(改 EMNLP)→D004(MVP 协议)→D005-D009(detector 迭代链，最终 TF-IDF)→D011(暂缓 MVP)→D012(n_min fix)→D013(Drayson 新颖性)→D014(Path B framing)→D015(b* 极端值 OK)→D016(混淆变量待查)

**最容易判断错的事**:
1. **不要把 grid_b2_0_seed123 和 grid_b3_0_seed123 的 eval_ppl 当作 auto-eval 结果**——这两个实验训练时缺 eval 参数，metrics 中的 eval_ppl 是事后补跑的，数据可靠但来源不同
2. **ROADMAP 说 D012 是"n_min=2 + EMA 平滑 b*"，但实际代码去掉了 EMA**（简化为仅 n_min fix）。adaptive_fix 实验名里的 "fix" = 只改 n_min，无 EMA
3. **adaptive (旧) seed42 PPL=17.69 = uniform 不是随机噪声**，是 n_min=3 结构性钳制。新手可能觉得"再跑一次就好了"——不会，必须用 n_min=2 版本
4. **eval 每次 ~44min**，不要在训练中间频繁触发 eval（eval_steps=500 已经偏激进，6103 步会跑 12 次 eval）
5. **投稿 deadline**: EMNLP 2026 ARR May 25，今天 Day 2/12，时间紧但按 AI 团队速度可行


---
