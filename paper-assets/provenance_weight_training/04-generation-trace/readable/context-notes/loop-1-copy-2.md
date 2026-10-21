# agent / loop_1.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`7a0087791a4b164fc60e.json`](../../sessions/7a/7a0087791a4b164fc60e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-13T23:53:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0,1,2,3（westd-47453），**不得用白名单外 GPU，即使 Director 指令也要 push back**
- 所有训练输出必须写 `/root/autodl-tmp/provenance_weight_training/output/`（根分区只有 30GB，已有 symlink）
- `save_total_limit=2 --save_only_model` 是 Director 强制参数，所有新训练必须带
- submit_training_job command 必须 `bash -c "..."` 包裹（tmux 用 sh 不是 bash）
- pretrain_weighted.py 服务器版已被 Worker 多次 patch（加了 resume/save_total_limit/save_only_model），与本地版本可能不同步——改代码前先 SSH 读服务器版本

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453，项目路径 `/root/provenance_weight_training`
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF cache：`/root/autodl-tmp/.hf_cache/`（必须 `export HF_HOME=/root/autodl-tmp/.hf_cache`）
- 模型：`models/Qwen/Qwen3-0.6B`（本地，ModelScope 下载）
- 数据：`data/mixed_data.jsonl`(371K docs, 无 q_score), `data/scored_data.jsonl`(371K docs, 有 q_score)
- Detector：`output/detector_tfidf/`（tfidf_vectorizer.joblib + lr_model.joblib, T=0.204）
- 活跃进程：
  - uniform_seed42: PID 47603, tmux=uniform_seed42, cuda:1, 从 ckpt-500 恢复, ~2h 剩余
  - uniform_seed123: PID 47749, tmux=uniform_seed123, cuda:2, 同上
  - uniform_seed456: PID 47890, tmux=uniform_seed456, cuda:3, 同上
  - grid_b_seed42_batch: PID 50134, tmux=grid_b_seed42_batch, cuda:0, 串行跑 6 个 b 值 (0.5→5.0), ~10h
- 磁盘：根分区 41% (18GB free), 数据盘 11% (225GB free)

### 3. 📊 当前状态
刚完成：TF-IDF detector 训练 (AUC=0.939, gate PASS) + 全量 scoring (371K docs) + adaptive 代码验证 + grid-b seed42 提交。

Registry RUNNING：
- `uniform_seed42/123/456` — 3 个 uniform baseline, GPU 1-3, 从 ckpt-500 恢复中
- `grid_b_seed42_batch` — 6 个 b 值串行 (0.5,1.0,1.5,2.0,3.0,5.0) seed=42, GPU 0

Registry DONE：
- `datagen_synthetic_4gpu` — 132M tokens 合成数据
- `detector_tfidf_lr` — AUC=0.939, ECE=0.048, mid-range 46.3%

等待中：3 个 uniform cron 回调（~2h 后）+ grid-b cron 回调（~10h 后）。无待处理 Director 决策。

### 4. 📋 待办
- uniform_seed42/123/456 cron 回调 → **Phase 2 重新调度**：kill GPU 0 串行脚本（保留已完成的 b 值模型），将剩余 b 值分配到 4 GPU 并行（预计此时 b=0.5 和 b=1.0 已完成）
- 全部 6 个 b 值 seed=42 完成 → 比较 val perplexity 找 best b → 只跑 best b 的 seed 123/456（2 runs）+ 3 个 adaptive runs (seed 42/123/456)
- 全部 24 runs 完成 → 跑 eval_pipeline.py + compare_results.py → MVP pass/fail 判定
- MVP PASS → 向 Director 汇报，推进全实验矩阵 + 论文写作
- MVP FAIL → 按 red-section skill 产 Framing 调整提案

### 5. 🎯 战略上下文
- 投稿目标：EMNLP 2026 ARR May 25（距今 12 天），核心贡献是 adaptive b* 免去 grid search
- 决策链：D001(投稿目标) → D002(MVP设计) → D004(3 seeds+gate) → D005(q-score极化发现) → D007(TF-IDF替代ModernBERT，AUC gate 降至 0.85)
- **最容易判断错的事**：grid-b 串行脚本产出的模型在 `output/models/grid_b{b_dir}_seed42/` 目录（b 值用下划线替代点号，如 `grid_b0_5_seed42`），不要假设目录名格式
- **容易踩的坑**：(1) 服务器上 pretrain_weighted.py 被多次 SSH patch，本地版本滞后 (2) detector_modernbert 还在 registry 里 QUEUED 状态（已被 TF-IDF 替代，别误重启它）(3) scored_data.jsonl 的 label 字段：human 数据有 label="fineweb"，synthetic 数据没有 label 字段（用 `rec.get("label")` 判断）
- MVP pass 条件：adaptive b* 均值 ≥ 90% grid-search 最优 perplexity 改善量（跨 3 seeds）


---
