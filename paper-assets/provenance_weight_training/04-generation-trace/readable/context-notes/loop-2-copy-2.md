# agent / loop_2.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`0d26c423e425311fa0a1.json`](../../sessions/0d/0d26c423e425311fa0a1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T06:53:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3（westd-47453），不可用其他设备
- output 必须走 symlink `/root/provenance_weight_training/output` → `/root/autodl-tmp/provenance_weight_training/output/`，绝对禁止直接写根分区（30GB，之前磁盘满崩溃过）
- submit_training_job 的 command 必须 `bash -c "..."` 包裹（tmux 用 sh，不包裹 source/conda 会 EXIT_CODE=127）
- Grid-b 单 b 值用 `--grid_b_value X`，不要用串行脚本（Director 已批准拆分并行）
- save_total_limit=2 + save_only_model=True 是 Director 强制要求，不可省略
- HF 下载必须 `HF_HUB_DISABLE_XET=1`，否则 401

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453，账号 root，工作目录 `/root/provenance_weight_training`
- Python：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- torch=2.10.0+cu128, transformers=4.57.6, lm_eval=0.4.11
- 模型：`/root/provenance_weight_training/models/Qwen/Qwen3-0.6B`
- 数据：`data/mixed_data.jsonl`（371,499 docs, 60/40 human/synth），`data/scored_data.jsonl`（同上 + q_score 字段）
- HF cache：`/root/autodl-tmp/.hf_cache/`
- 检测器：`output/detector_tfidf/`（TF-IDF+LR, AUC=0.939, ECE=0.048）
- 活跃进程（待确认，handoff 时有 Worker 正在检查）：
  - grid_b_seed42_batch: PID 50134, tmux=grid_b_seed42_batch, cuda:0（串行 6 b 值）
  - adaptive_seed42: PID 58888, tmux=adaptive_seed42, cuda:1
  - adaptive_seed123: PID 58978, tmux=adaptive_seed123, cuda:2
  - adaptive_seed456: PID 59058, tmux=adaptive_seed456, cuda:3
- **⚠️ 关键不确定性**：handoff 时 Director 报告 3 张 GPU 空闲，我已派 Worker `worker_ops_urgent-status-and-action_20260514T065244` 去检查并处理（如果 adaptive 已完成则自动提交 grid_b_seed123 round 1）。这个 Worker 的结果你需要第一时间处理。

### 3. 📊 当前状态
**刚做完**：uniform ×3 标记 DONE（train_loss 均值 7.304±0.012，各 3.43 GPU-hours），adaptive ×3 提交成功（02:46 UTC），grid_b 拆分方案已确认（原生支持 `--grid_b_value`），grid_b_seed123 × 6 b值 registry 条目已创建（QUEUED）。

**Registry 状态**：
- DONE: uniform_seed42/123/456, detector_tfidf_lr, datagen_synthetic_4gpu
- RUNNING: grid_b_seed42_batch（cuda:0，串行 6 b 值，约 21h 总计），adaptive_seed42/123/456（cuda:1/2/3，各 ~3.6h）
- QUEUED: grid_b0_5/1_0/1_5/2_0/3_0/5_0_seed123（等 adaptive 完成后按轮次提交）

**等待中**：
- Worker `worker_ops_urgent-status-and-action_20260514T065244` 回调——这是最关键的待处理项，它在检查 adaptive 是否完成并自动提交 grid_b round 1
- 如果该 Worker 已提交 grid_b round 1，你需要更新 adaptive registry → DONE + 确认 grid_b RUNNING

### 4. 📋 待办（条件触发式）
- Worker `urgent-status-and-action` 回调 → 读结果：若 adaptive 已完成则更新 registry DONE + 记录 metrics + 确认 grid_b round 1 已启动；若 adaptive 异常则查日志决定重跑
- adaptive 仍在跑（Worker 报告 PIDs alive）→ 等 cron 回调，完成后立即提交 grid_b_seed123 round 1（cuda:1→b=0.5, cuda:2→b=1.0, cuda:3→b=1.5）
- grid_b_seed123 round 1 完成 → 立即提交 round 2（cuda:1→b=2.0, cuda:2→b=3.0, cuda:3→b=5.0），无需 Director 确认
- grid_b_seed123 全部完成 → 同方式跑 seed456（需先注册 6 个 registry 条目）
- 全部 MVP 实验完成 → 跑 eval_pipeline.py 对比 uniform vs grid-b vs adaptive，汇报 Director

### 5. 🎯 战略上下文
- **核心假设**：adaptive b*（从 α_eff 理论推导）无需网格搜索即可匹配/超越 grid-searched best-b
- **Pass/Fail**：adaptive 均值 ≥ 90% grid-search 最优 perplexity 改善量（跨 3 seeds）
- **投稿目标**：EMNLP 2026 ARR May 25（主攻，剩余 ~11 天），AAAI 2027 后备
- **检测器教训**：Qwen3-0.6B 合成文本太容易被神经网络区分（AUC→1.0），必须用弱分类器 TF-IDF+LR 才能获得有梯度的 q-score。这个决策链是 D005→D006→D007→D008
- **易踩的坑**：
  - 不要试图用 ModernBERT 做检测器（已验证 AUC 极化无用）
  - GPU 空闲就是失职——每轮切换间 < 2 分钟
  - grid_b 串行脚本（run_grid_b_seed42.sh）是历史遗留，seed123/456 已改为单 b 值并行提交
  - Worker 的 CPU dry-run 会卡死（模型加载太慢），不要在 CPU 上做任何 transformer 推理


---
