# reviewer / loop_4.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`644ead319256d84c4471.json`](../../sessions/64/644ead319256d84c4471.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-14T13:31:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cuda:0/1/2/3（westd-47453 全部 4 卡），越界 → critical
- adaptive 实验用 `scored_data.jsonl`（含 q_score），uniform 用 `mixed_data.jsonl`（无 q_score）——搞混会静默失败
- `pretrain_weighted.py:233` help 文本写 "Defaults to batch_size // 2" 但 line 277 实际是 `int(batch_size * 0.75)`——**我已上报此 bug 给 Director，等待确认设计意图**，在确认前不要假设 n_min=2 或 n_min=3 哪个是"正确"的
- eval_perplexity.py 有 sliding window overlap masking bug（begin=stride 时 mask_len=0），当前数据集影响可忽略但修复前不可用于长文档 eval

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453，工作目录 `/root/provenance_weight_training`
- Python：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`/root/provenance_weight_training/models/Qwen/Qwen3-0.6B`
- 数据：`data/scored_data.jsonl`（371499 条，含 q_score）、`data/mixed_data.jsonl`（371499 条，uniform 用）
- Eval holdout：`data/eval_holdout.jsonl`（67823 docs, 4.08M tokens）
- 无 wandb 配置（不检查 wandb）
- auto_eval_watcher.py 已修复为动态 GPU 选择（`get_least_loaded_gpu()`），但只 watch `grid_b*` glob pattern，不覆盖 adaptive/uniform

### 3. 📊 当前状态
**刚完成**：审查 seed42 adaptive 诊断报告，已发 WARNING 给 Director，核心发现是 n_min help 文本 vs 代码不一致（可能是 bug 而非设计选择），以及当前 MVP 对比不公平（adaptive 被 n_min=3 系统性削弱 vs 无约束的 grid_b0.5）。

**Registry 状态**（12 DONE, 4 RUNNING, 7 QUEUED）：
- RUNNING：grid_b2_0_seed42 (GPU0), grid_b2_0_seed123 (GPU1), grid_b3_0_seed123 (GPU2), grid_b5_0_seed123 (GPU3)
- QUEUED：grid_b{0.5,1.0,1.5,2.0,3.0,5.0}_seed456（6 个）+ 1 个未确认
- DONE 关键数据点：uniform 3 seeds (17.69/17.69/17.70), adaptive 3 seeds (17.69/17.63/17.64), grid_b0.5 seed123 (17.638)

**等待中**：Director 对 n_min bug 的决策（修到 2 还是保留 3）；seed42 grid batch 和 seed123 grid batch 完成后需要审查。

### 4. 📋 待办
- Director 回复 n_min 设计意图 → 确认后 adaptive 需以正确 n_min 重跑 3 seeds（~12 GPU-hours）
- seed42 grid batch (b=2.0 当前 RUNNING) 完成 → 审查结果，补全 grid search 覆盖
- seed123 grid batch (b=2.0/3.0/5.0 当前 RUNNING) 完成 → 审查，与 seed42 grid 结果交叉验证
- seed456 grid batch (6 runs QUEUED) 启动+完成 → 审查第三 seed 的 grid search
- 全部 grid 完成 → 计算 grid-best（across all b values and seeds），重新评估 MVP pass criterion
- adaptive 重跑完成 → 做最终 MVP pass/fail 判定（adaptive mean improvement / grid-best mean improvement ≥ 90%?）

### 5. 🎯 战略上下文
- **MVP 阶段**，目标 venue ICML/NeurIPS，核心 claim：adaptive b* 用 1 次训练替代 6× grid search
- **当前效果极弱**：改善 ~0.04 ppl（0.23% relative），paper_framing.md 已标为 Key Risk #4
- **两条叙事路径**：Path A（adaptive > grid-best）或 Path B（adaptive ≈ grid-best，省 6× compute）——当前数据更接近 Path B 但尚未确认
- **最容易判断错的事**：不要在 n_min bug 修复前做 MVP pass/fail 判定——当前 adaptive 被系统性削弱，任何对比都不公平
- **另一个坑**：auto_eval_watcher 只 watch `grid_b*`，adaptive/uniform 的 eval 是手动触发的，审查时要确认 eval 是否真的跑了（看 checkpoint 目录下有没有 eval_results）
- 决策链：D004（MVP protocol）定义了 pass criterion，但尚无 D005 以上的决策记录


---
