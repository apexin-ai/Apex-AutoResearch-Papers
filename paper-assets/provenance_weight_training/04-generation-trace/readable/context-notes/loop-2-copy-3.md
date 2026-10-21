# reviewer / loop_2.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`8fc290ba21853180e7f5.json`](../../sessions/8f/8fc290ba21853180e7f5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T02:19:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- `output/` 是 symlink → `/root/autodl-tmp/provenance_weight_training/output`，checkpoint 实际在数据盘。**不要再报磁盘溢出**（已误报 3 次被 Director 纠正）
- uniform 训练用 `mixed_data.jsonl`（无 q_score），grid-b/adaptive 用 `scored_data.jsonl`（有 q_score）。不要混淆
- 项目无显式 gpu_ids 白名单限制，但需核实进程实际占用的 GPU 与 registry spec 一致
- ModernBERT detector（AUC≈1.0）已弃用，当前方案是 TF-IDF+LR detector（AUC=0.939, D007/D008）。不要质疑"为什么不用更强的检测器"——q-score 极化问题是故意用弱检测器解决的

### 2. 🖥️ 基础设施快照
- 服务器：`westd-47453(root)`，4× NVIDIA RTX PRO 6000 Blackwell 98GB
- 工作目录：`/root/provenance_weight_training`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 模型：`/root/provenance_weight_training/models/Qwen/Qwen3-0.6B`
- 数据盘：`/root/autodl-tmp/`（250GB，~226GB 可用）
- HF_HOME：`/root/autodl-tmp/.hf_cache`
- 训练数据：`data/mixed_data.jsonl`（371,499 行）、`data/scored_data.jsonl`（371,499 行，含 q_score）
- 评估数据：`data/human/eval_holdout.jsonl`（67,823 行）
- 检测器：`output/detector_tfidf/`（TF-IDF+LR，T=0.204）
- 评估脚本：`evaluation/eval_pipeline.py`（perplexity + lm-eval-harness + Self-BLEU/Distinct-n）
- W&B：未配置，不检查
- 活跃进程（截至 handoff 前）：
  - uniform_seed42 (PID 47603, cuda:1, tmux)
  - uniform_seed123 (PID 47749, cuda:2, tmux)
  - uniform_seed456 (PID 47890, cuda:3, tmux)
  - grid_b_seed42_batch (PID 50134, cuda:0, tmux, 串行 6 个 b 值)

### 3. 📊 当前状态
- 3 个 uniform baseline 约 58% 完成（step ~3520/6103），ETA ~1.5h
- grid_b_seed42_batch b=0.5 约 37% 完成（step ~2275/6103），ETA ~2.3h（仅当前 b 值）
- 已完成审查：mixed-data-fix、detector-check、detector-tfidf-lr、score-mixed-data、eval-pipeline-check、grid-b-runner-submit、prepare-next-batch-scripts、training-progress-monitor、grid-b-output-path
- seed123/456 的 grid-b batch 脚本已就绪（`run_grid_b_seed{123,456}.sh`），等 uniform 释放 GPU 后提交
- eval_pipeline.py 有一个 warning 未解决：`device_map="auto"` 缺 GPU 隔离，运行时需 `CUDA_VISIBLE_DEVICES`

### 4. 📋 待办（条件触发式）
- uniform 3 runs 完成 → 核实 registry 更新为 DONE + 检查最终 loss/metrics → 发审查报告
- uniform 完成释放 GPU 1-3 → 确认 seed123/456 batch 脚本已提交 + registry 已创建条目
- grid_b_seed42 每个 b 值完成 → 抽查 weighting metrics（ESS/alpha_eff 是否合理，b=5.0 时 ESS 应接近 batch_size 因为高 b 几乎二值化权重）
- 全部 grid-b 完成 → 审查 eval pipeline 执行结果（perplexity/HellaSwag/MMLU 跨 b 值是否有 monotonic trend）
- adaptive b* 实验提交 → 重点审查 `find_optimal_b` 实现和 contamination_ratio=0.4 是否与数据一致

### 5. 🎯 战略上下文
- 投稿目标：EMNLP 2026 ARR May 25（D003），AAAI 2027 后备
- 核心假设：adaptive b* 能替代 grid search 选择最优 provenance weight（D002）
- 决策链：D001(AAAI) → D003(改回 EMNLP) → D002(MVP 设计) → D004(3 seeds + detector gate + grid-b 定义) → D005(q-score 极化风险) → D006(减数据重训，失败) → D007/D008(改 TF-IDF+LR)
- TF-IDF detector 的 mid_range_ratio=46.3% 是关键指标——这使得不同 b 值的权重有区分度。grid-b=0.5 的 ESS（2.0-3.3/4.0）已验证此路径可行
- **易错点**：
  1. 不要报 `output/` 目录的磁盘风险（symlink，已踩坑 3 次）
  2. uniform 用 `mixed_data.jsonl` 是正确的（不需要 q_score），不要标记为不一致
  3. `contamination_ratio=0.4` 参数在 grid-b 方法中不生效（只影响 adaptive），出现在命令行中是无害的
  4. detector_modernbert 的 registry status 是 QUEUED（应为 DONE），这是历史遗留未修正的状态字段


---
