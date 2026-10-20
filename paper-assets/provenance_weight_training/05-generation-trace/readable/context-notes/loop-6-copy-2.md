# agent / loop_6.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`1344373eaf800a3e441f.json`](../../sessions/13/1344373eaf800a3e441f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-14T23:28:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1, cuda:2, cuda:3（westd-47453）。无其他服务器/GPU 可用
- grid_b2_0_seed456 状态 ALLOCATED 在 cuda:0，但尚未实际提交训练（需等 cuda:0 空闲或确认可用）
- grid_b3_0_seed456 和 grid_b5_0_seed456 仍 QUEUED，需等 seed456 的 b=0.5/1.0/1.5 跑完释放 GPU 才能提交
- adaptive_v2_seed* 三个已 killed（D012 决策：改用 adaptive_fix 无 EMA 版本），不要重启
- submit 命令**必须包含** `--eval_data_path data/human/eval_holdout.jsonl --eval_steps 500`，之前有漏掉导致补跑 eval 的教训
- 数据/模型路径必须在 `/root/provenance_weight_training/`（根分区 30GB 限制）
- Python 路径：`/root/miniconda3/bin/python`，激活方式 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453（4× RTX 6000 Pro 96GB）
- 工作目录：`/root/provenance_weight_training`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`/root/provenance_weight_training/models/Qwen/Qwen3-0.6B`
- 数据：`/root/provenance_weight_training/data/scored_data.jsonl`（371,499 条，40% 合成污染）
- Eval holdout：`/root/provenance_weight_training/data/human/eval_holdout.jsonl`（~4.08M tokens）
- WANDB_MODE=disabled（所有实验）
- 活跃进程（reconcile 确认 RUNNING）：
  - grid_b0_5_seed456: PID 145057, cuda:1, tmux session
  - grid_b1_0_seed456: PID 142902, cuda:2, tmux session
  - grid_b1_5_seed456: PID 142985, cuda:3, tmux session
- Cron 监控以上 3 个实验（自动回调）
- grid_b2_0_seed456: ALLOCATED on cuda:0 但未提交（需确认 cuda:0 是否空闲）

### 3. 📊 当前状态
**刚完成的关键工作**：
- grid_b_seed42_batch（6 值串行）已全部完成：b=0.5 best PPL=17.651，与 seed123 趋势一致
- adaptive_fix 三 seed 全部 DONE：seed42=17.65, seed123=17.643, seed456=17.66（一致优于 uniform，≈grid-best）
- **MVP 判定条件接近满足**：adaptive_fix 三 seed + grid_b seed42 已完成。差 grid_b seed456 六值完整数据

**当前 RUNNING**：
- grid_b0_5_seed456 (cuda:1) — 已重提交成功，ETA ~3h from 21:20 UTC
- grid_b1_0_seed456 (cuda:2) — 运行中
- grid_b1_5_seed456 (cuda:3) — 运行中

**等待中**：
- grid_b2_0_seed456: ALLOCATED cuda:0，未提交（cuda:0 可能空闲——grid_b_seed42_batch 已完成释放了 cuda:0）
- grid_b3_0_seed456, grid_b5_0_seed456: QUEUED，等 GPU 释放
- 无活跃 Worker

### 4. 📋 待办（条件触发式）
- **立即**：grid_b2_0_seed456 已 ALLOCATED 且 cuda:0 已空闲（seed42 batch 完成）→ 派 Worker 用 `submit_on_allocated` 提交训练（命令须含 eval 参数）
- grid_b0_5/1_0/1_5_seed456 cron 回调完成 → 提交 grid_b3_0_seed456 和 grid_b5_0_seed456（按 GPU 释放顺序）
- seed456 全 6 值完成 → 汇总三 seed × 6b 结果表 + adaptive_fix 对比 → **MVP PASS/FAIL 判定**
- MVP PASS → 向 Director 汇报，请求进入 post-MVP 阶段（paper_framing 细化 → experiment_plan 全矩阵 → 多污染比例实验）
- MVP FAIL（unlikely）→ 诊断 seed456 是否异常，考虑扩展 b<0.5（b=0.1/0.2/0.3）
- seed123 best-b 和 seed42 best-b 均在边界 (0.5) → 若 MVP PASS 后在 full 阶段补 b=0.1/0.2/0.3 grid

### 5. 🎯 战略上下文
**核心结论链**：
- D007-D008: ModernBERT 废弃 → TF-IDF 检测器（AUC=0.939, 连续 q-score）
- D011: adaptive 原版 seed42 零改善 → 诊断为 n_min=3 钳制 ESS
- D012/D017/D018: adaptive_fix = n_min=2 无 EMA。唯一变量是 n_min，无混淆
- 核心 claim：adaptive b* ≈ grid-best（seed123 差 0.005 PPL），且 cross-seed 稳定（range 0.017 vs 原版 0.06）
- 论文 story 应 frame 为 **robustness + 免 grid search**，而非 absolute PPL improvement（改善量 0.2-0.3% 太小做主 claim）

**易错点**：
- cuda:0 上 grid_b2_0_seed456 已 ALLOCATED 但没人提交——这是上一轮遗留的 gap，新 session 要立即处理
- train_loss 跨方法不可比（weighted vs unweighted CE）——只能用 eval_ppl_holdout 做公平对比
- b* 分布中位数≈0 意味着 ~60% batch 不加权——论文讨论需解释为什么这仍有效（40% 高污染 batch 的下权重才是关键）
- D013 新颖性风险：Drayson et al. (EMNLP 2025) 用同一公式 w=(1-q)^b，我们的差异化在于 **adaptive b*** 而非 weighting scheme 本身


---
