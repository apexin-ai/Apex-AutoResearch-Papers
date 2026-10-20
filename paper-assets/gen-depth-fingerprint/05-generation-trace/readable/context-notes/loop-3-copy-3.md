# reviewer / loop_3.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`85035f11f5f1f046a4fe.json`](../../sessions/85/85035f11f5f1f046a4fe.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-15T12:42:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU: autodl-5090 cuda:0-3 (4× RTX 5090)，当前全部空闲（实验阶段结束）
- `ordinal_baseline.py` 使用 n_estimators=100, max_depth=3(baselines)/5(7-feat)，与 `bootstrap_ci_v2.py` 的 200/6 不同——method.tex:68 声称 "throughout all experiments, including baseline comparisons" 是**虚假声明**，这是唯一未修复的 CRITICAL，必须在提交前解决
- Spearman ρ 值必须在 class-balanced downsample 后计算（plan-014 权威值），不能用全量未平衡数据（review_overall_ci_v1 的值偏大，entropy_std 从 0.076 变成 0.200）
- 6-gen LOGO 权威来源：`bootstrap_ci_v2_results.json`（有 downsample），per-gen F1 以此为准

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090(root)，工作目录 `/root/gen-depth-fingerprint`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/`
- 论文源文件：`docs/paper/`（main.tex + 14 个 \input 文件），编译通过 13 页
- 关键数据：`data/features_all_models.csv` (27,529 rows, 6-gen)，`data/detector_scores.csv` (23,032 rows, 5-gen only，缺 Binoculars/LD-Score per-sample scores，无 Qwen3-8B)
- 结果 JSON 均在 `/root/gen-depth-fingerprint/results/`，权威文件：`bootstrap_ci_v2_results.json`, `review_overall_ci_v2_results.json`, `review_topic_drift_results.json`, `family_holdout_3class.json`, `lofo_ablation_results.json`, `alt_classifier_results.json`
- 活跃进程：无。全部 GPU 空闲，无 tmux session / cron

### 3. 📊 当前状态
刚完成 batch2 写作修改审查。项目处于 pre-submission 状态，EMNLP ARR DDL 2026-05-25（~10天）。
- Registry：40 experiments 全部 DONE/FAILED，无 RUNNING/PREPARING
- Paper Agent Step 5 收敛 8/10，Review Director Round 1 审稿(Overall 3/5)后的 Action Matrix 修改进行了 2 batch
- 已审查的 worker：topic-drift(PASS), overall-ci-v2(PASS), paper-edits-batch1(WARNING), paper-edits-batch2(WARNING)
- 等待中：W1 baseline ensemble 实验（最重要的 GPU 实验，需重跑 baseline 统一超参后做 4-baseline ensemble）

### 4. 📋 待办
- method.tex:68 "including baseline comparisons" 出现在最终提交版 → **立即 flag CRITICAL**，要求删除或重跑 baseline 用 200/6
- W1 baseline ensemble worker 完成 → 核实 4-baseline ensemble F1 + CI width，如果 ≈ 7-feature 则 narrative 需大改（fallback: CI width argument）
- W4 Beyond Binary / SemEval 参考文献补入 → 核实 Related Work + Introduction L15 qualifier
- W14 开源声明 → 核实 Ethics/Conclusion
- 所有修改完成后 → 做全文最终扫描（数字一致性 + LOFO 缩写冲突是否修复）

### 5. 🎯 战略上下文
- 核心结论：6-gen LOGO F1=0.789，CI width 0.9pp，differential depth response（drift vs stationary features），downstream negative (diagnostic not curative)
- 决策链：D009(负面结果 reframe) → D011(8B scale验证) → D012(恢复EMNLP) → D013(prompt type纳入)
- **最容易判断错的事**：(1) 有两套 LOGO 实现——有 downsample（bootstrap_ci_v2）和无 downsample（review_overall_ci_v1, ordinal_baseline）。per-gen F1 差异可达 2.5pp，average 几乎相同。永远以 bootstrap_ci_v2 为准。(2) Table 3 是 5-gen LOGO，Table 1 是 6-gen LOGO，CI 口径不同——L138 已做桥接但要注意。(3) 论文的 LOFO 缩写同时代表 Leave-One-Family-Out 和 Leave-One-Feature-Out，已 flag 但尚未修复。(4) detector_scores.csv 只有 5-gen 3 列，做 baseline ensemble 需要扩充。


---
