# reviewer / loop_10.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`a36ef782f5ce9defb8b4.json`](../../sessions/a3/a36ef782f5ce9defb8b4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-15T23:29:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0/1/2/3 全部四张，均属本项目。无越界风险但须注意多实验抢占同一 GPU（grid_b_low_r3 就是因为没设 CUDA_VISIBLE_DEVICES 与 contamination_60_seed42_r2 撞 cuda:0 崩溃）
- 代码用 `AutoModelForCausalLM.from_pretrained()`，是 continued pretraining 不是 from scratch。Experiments 节写了 "from random initialization" 是错的，已标 critical 但截至 handoff 未修复
- eval holdout 是纯人类数据（data/human/eval_holdout.jsonl, 67823 条 FineWeb），不是 "balanced real/synthetic"。Experiments 节描述也错了，同上已标 critical

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453 (root)，代码根目录 /root/provenance_weight_training
- Python：/root/miniconda3/bin/python，conda activate base
- 模型：/root/provenance_weight_training/models/Qwen/Qwen3-0.6B（1.5GB pretrained, ModelScope 下载）
- 数据：data/scored_data.jsonl (ρ=0.4, 371K 条), data/scored_data_60.jsonl (ρ=0.6), data/human/eval_holdout.jsonl (67823 条)
- WANDB_MODE=disabled（大部分实验），无需查 W&B
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/

### 3. 📊 当前状态
**刚完成**：审查了 Introduction + Conclusion 写作、bs8_nmin2_seed42_r2 假失败（EXIT_CODE=129, 训练实际完成, eval PPL=17.73）、grid_b_low 三连失败、ess_only 三 seed 汇总、full_experiment_data.md 数据提取

**RUNNING 实验（截至 handoff）**：
- contamination_60_seed42_r2 — cuda:0, ρ=0.6 adaptive, ~10% 进度
- contamination_60_uniform_seed42 — cuda:1, ρ=0.6 uniform baseline, ~10% 进度  
- contamination_60_grid_b0_5_seed42 — cuda:3, ρ=0.6 grid b=0.5
- grid_b_low_seed42_r3 — cuda:0（已 failed，与 r2 撞 GPU）；grid_b_low_serial_seed42 QUEUED 等 GPU

**待 Director 决策**：grid_b_low 三连失败，建议拆成三条独立实验

### 4. 📋 待办（条件触发式）
- contamination_60_* 三个实验完成 → 审查 ρ=0.6 下 adaptive vs uniform vs grid 对比，验证 "graceful degradation" claim
- grid_b_low_serial_seed42 启动/完成 → 验证 b=0.1/0.2/0.3 的 PPL 是否接近 uniform，确认 b=0.5 是 lower useful bound
- Results / Discussion / Abstract 写作 worker 完成 → 章节对抗审查（重点：PPL 数字与 table1_data.md 一致性、88.6% claim 是否修正、"from random init" 是否修正）
- bs8_nmin2_seed42_r2 eval 已出 PPL=17.73 → 如果 Agent 用这个数字写 batch size robustness 结论，注意 bs8 的 PPL(17.73) 比 bs4(17.65) 差很多，可能因为 n_min=2 在 bs=8 下约束力不同

### 5. 🎯 战略上下文
**核心结论**：adaptive b* (τ=0.8, n_min=2) 3-seed mean PPL=17.651，vs grid-best(b=0.5)=17.646，vs uniform=17.693。Adaptive 恢复 grid-best 89.4% 的改善（ratio-of-means），无需 grid search。ESS-only(17.72) 劣于 uniform，证明 min-intervention > max-intervention。

**已提交未修复的 critical/warning 汇总**：
1. [critical] Experiments "from random initialization" → 应为 "continued pretraining"
2. [critical] Experiments "balanced real/synthetic test set" → eval 是纯人类数据
3. [critical] Introduction vs Experiments 对同一事实矛盾（continued vs random init）
4. [warning] Conclusion PPL "17.651 vs 17.646" 需报告 mean±std
5. [warning] "calibration > discrimination" claim 无直接实验支撑
6. [warning] Method 节 line 136 "46.7% hitting ceiling at b_max=20" 数据错误（46.7% 是 b*≥2 不是 b*=b_max）
7. [warning] Related Work cheng_2025 "20-60%" 来源需核实

**易错点**：
- table1_data.md 里 uniform seed42 PPL=17.690，但 unified_nmin_eval 里的 baseline 是 17.6939。前者是 3 位小数截断，注意对比时用哪个源
- adaptive_seed42 (n_min=3, legacy) vs adaptive_fix_seed42 (n_min=2, correct) — 论文用的是 fix 版本，但 registry 里两个都在，别搞混
- bs8 实验 PPL=17.73 比 bs4 差很多，如果 Agent 试图 claim "batch size robust"，这个数据不支持


---
