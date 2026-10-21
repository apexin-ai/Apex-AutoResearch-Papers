# reviewer / loop_13.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`c399206db78fa591845d.json`](../../sessions/c3/c399206db78fa591845d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-17T22:45:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- gpu-6000pro-2 本项目只用 cuda:0（14B 实验占用中）和 cuda:1（instruct/feature 实验）
- C003：EDD 上界必须是 Proposition 不是 Theorem；写入论文前必须过 Reviewer 审查
- C004：wild data FPR 结果禁止用 "contamination" 暗示 AI 内容占比，只能 frame 为 FPR/limitation
- Pareek 引用：作者是 Pareek, Du, Oh（不是 Sanghavi）——已修复，但后续引用时注意
- 论文源文件权威位置：**本地** `docs/paper/*.tex`，远程 `/root/autodl-tmp/.../paper/` 是旧版残留

### 2. 🖥️ 基础设施快照
- **gpu-6000pro-2**：`/root/autodl-tmp/recursive_gen_depth_est/`，cuda:0 跑 qwen25_14b_scale_002（PID 806751）
- **westd-48862**：`/root/autodl-tmp/recursive_gen_depth_est/`，cuda:0 跑 qwen25_14b_scale_003（PID 20700）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/`
- 论文文件：`docs/paper/*.tex`（最近修改 2026-05-17 ~19:57 UTC，D038 patched）
- artifacts：`artifacts/_project/paper/theory_draft.tex`（理论草稿，未编入 main paper）

### 3. 📊 当前状态
**刚完成**：D038 Paper Patch 质量审查（已 post to Director），发现 1 critical（geometric decay 公式不自洽）+ 1 warning（C004 轻度违规）。Framing 风险评估（depth≈perplexity 攻击角度）已回复 Director：中等风险，建议补 single-feature p90_ppl ablation。

**RUNNING 实验**：
- qwen25_14b_scale_002 @ gpu-6000pro-2：d0 已 94%，即将进入 d1-d3（ETA ~数小时）
- qwen25_14b_scale_003 @ westd-48862：d0 约 51%（ETA ~10-12h 全部完成）

**已审无异常的 worker**：rf_seed_robustness（std 0.06%）、feature_importance_ablation（perplexity 组 66.0%/full 66.55%）、pareek_bib_entry（修正完成）

### 4. 📋 待办
- 14B scale_002 完成 → 审查 Phase 4/5 结果，核实 AUC 是否 > 1.5B baseline，检查 GPU 使用合规
- 14B scale_003 完成 → 同上，交叉验证两个 run 一致性
- Director 回复 geometric decay 修复方案 → 审查修复后的 atlas.tex §4.4 是否数学自洽
- single-feature p90_ppl ablation worker 完成 → 审查结果，若 gap < 2pp 需提醒加强叙事防御
- registry 中 downstream_benchmark_001 和 learned_estimator_001 仍标 RUNNING 但实际已 dead（westd 上无进程）→ 待 Director 清理

### 5. 🎯 战略上下文
- **项目目标**：EMNLP 2026 Main via ARR May 25 cycle（~7 天 DDL）
- **核心 story**：recursive generation depth estimation formalization + systematic 3×3 atlas + EDD metric + cross-model generalization
- **最大未解决硬伤**：atlas.tex geometric decay 段落公式 AUC=A₀·γ^d 与 γ=0.74 + 所列预测值三者不自洽。"Predicted" 值实为 3-model means，"observed" 是 Pythia-only，formula 用的是 raw AUC 但 γ=0.74 只在 AUC-excess 空间近似成立。审稿人一行计算即可发现。必须在提交前修复。
- **易错点**：论文本地文件 vs 远程文件——远程是旧版，本地是权威。审查论文时必须读本地 `docs/paper/`，不要只看远程。
- **14B validation**：两台机器并行跑，结果用于 cross-scale claim 加强。如果 14B 结果弱于 7B，需评估是否 report 为 negative（当前叙事已为 "preliminary observations"，有回旋空间）。


---
