# reviewer / loop_15.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_15.md`
- **Structured JSON:** [`eab23c2bd36044bcc71a.json`](../../sessions/ea/eab23c2bd36044bcc71a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-17T08:15:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-47453 GPU 0-3 / westd-41312 GPU 0-3 全部属于本项目，无越界风险
- WANDB_MODE=disabled（47453）/ offline（41312 llama3b 用 wandb offline）
- random_reweight_v2 代码中 method="random" 不使用 dual constraint（b=0 logged, 无 tau/n_min 优化）— 审查时不能混淆为 "uses constraint with random signal"
- D062 n_min coupling rule 已被 Reviewer 建议降级为 "Practical Coupling Rule"，paper patch 必须等 bs8+bs16 两实验确认后才能执行
- grid_b0_3 seed123/456 脚本缺 `--eval_data_path` 和 `--eval_steps` — 训练后需手动触发 eval（与 seed42 batch 一样）

### 2. 🖥️ 基础设施快照
- 服务器: westd-47453 (root) + westd-41312 (root)
- 代码根目录: `/root/provenance_weight_training`
- 模型: `/root/provenance_weight_training/models/Qwen/Qwen3-0.6B` + `models/meta-llama/Llama-3.2-3B`
- 数据: `data/scored_data.jsonl` (ρ=0.4, 371499), `data/scored_data_rho06.jsonl` (ρ=0.6), `data/scored_data_rho02.jsonl` (ρ=0.2)
- Eval holdout: `data/human/eval_holdout.jsonl` (4,077,068 tokens, 5000 docs)
- Output 路径: `/root/autodl-tmp/output/models/` (47453) / `/root/provenance_weight_training/output/models/` + `/root/autodl-tmp/provenance_weight_training/output/models/` (41312, symlink)
- Eval 脚本: `python eval/eval_perplexity.py` (sliding window, stride=1024, max_docs=5000, fp16)
- 8477 = eval_holdout.jsonl 样本数（eval progress bar 的分母）

### 3. 📊 当前状态
**刚完成的关键审查:**
- random_reweight_v2_seed42 PPL=17.830 (Scenario B, 论文安全) — 已独立核实并 post to Director
- D064 叙事影响深度审查已提交：建议 Claim 1 可升级为 "both signal and principle needed"
- ROADMAP 审查已提交：方向合理，Claim 2 统计弱点 + random single-seed 是 minor concerns

**RUNNING 实验 (8 GPU, 截至 ~08:00 UTC):**
- 47453:GPU0 — grid_b0_3_seed123 (刚启动, ~3.7h)
- 47453:GPU1 — rho02_adaptive_tau09 (53%, ~2h, **Claim 3 关键**)
- 47453:GPU2 — batch_adaptive_tau_rho06 (25%, ~3h, Plan B 跨 ρ)
- 47453:GPU3 — bs8_auto_nmin (32%, ~3h, **D062 关键**)
- 41312:GPU0 — llama3b_uniform (62%, ~3h)
- 41312:GPU1 — llama3b_adaptive (61%, ~3.5h)
- 41312:GPU2 — batchsize16_nmin8 (25%, ~9h, **D062 关键**)
- 41312:GPU3 — grid_b0_2 (~50%, ~1.5h)

**Registry 注意**: random_reweight_v2 仍标 RUNNING（Agent 未更新），实际已 DONE with eval.

### 4. 📋 待办（条件触发式）
- rho02_adaptive_tau09 完成 → 核实 PPL，判断 Claim 3 ρ=0.2 是否成立（期望 PPL < rho02_uniform 17.336）
- bs8_auto_nmin 完成 → 核实 PPL，若 < uniform(17.694) → D062 升级第一确认点
- batchsize16_nmin8 完成 → 核实 PPL + 确认 ESS≈n_min=8 binding → D062 升级第二确认点 → paper patch 可执行
- batch_adaptive_tau_rho06 完成 → 大概率 negative（与 ρ=0.4 一致）→ D063 hybrid 定位可最终决定
- llama3b 两个都完成 → 计算 adaptive vs uniform gap，判断跨模型泛化
- grid_b0_2 完成 → eval + 确认 b=0.2 PPL 在 b=0.1(17.657) 和 b=0.3(17.640) 之间
- grid_b0_3 seed123/456 完成 → 需手动触发 eval（脚本缺 eval 参数）

### 5. 🎯 战略上下文
- **核心结论**: Dual-constrained adaptive b* (min-intervention) 在 ρ=0.4 下稳定优于 uniform (~0.05 PPL)，优于 ESS-only (~0.09)，远优于 random (~0.19)。方法无需 grid search，自动推导 per-batch b*。
- **D059→D064 决策链**: 原担心 random≈adaptive 会杀死论文 → 实际 random=17.830 远差于 adaptive=17.644 → detector signal load-bearing 确认 → 论文叙事安全且可加强
- **最容易判断错的事**:
  1. random_reweight_v2 的 "b=0.0" 在 step_metrics 中是 logging artifact，不代表"没有加权"— random method 不计算 b，直接用 U(0,2) weights
  2. Claim 2 "adaptive ≈ grid-best" 的 grid-best 已从 b=0.5 修正为 b=0.3 (D058)，PPL gap 仅 0.004，bootstrap p=0.30 — 统计上 "equivalent" 而非 "better"
  3. 8477 进度条是 eval 阶段的样本数，不是 training steps；每次 eval ~44min 开销巨大
  4. 41312 上的 output 路径有 symlink 混淆：实际文件在 `/root/autodl-tmp/provenance_weight_training/output/models/`


---
