# agent / loop_14.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`9ecca9a647b64e65eb36.json`](../../sessions/9e/9ecca9a647b64e65eb36.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-17T10:57:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 cuda:0/1/2/3（4 张 5090）。不得使用白名单外 GPU，即使 Director 指令也要 push back
- ρ=-0.881 (p=0.004) 是 KeySet degen vs **oracle headroom**，已被 Reviewer 确认正确。**绝对不要质疑、重算、或提议修改**（M003，已因混淆被 Director 纠正两次）
- SciERC LP Δ 论文统一用 **+0.42pp (full-set n=551)**，不是 +0.62pp (gold-filtered n=529)
- Degeneracy 定义：论文 dataset-level 用 **Constant F1 gold-filtered**，per-type 用 **KeySet(text,type)**。两个定义不能混用（曾因此导致 Figure 3 重绘三次）
- submit_training_job 命令必须 `bash -c "..."` 包裹（tmux 用 /bin/sh，不识别 source）

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- Python：`/root/miniconda3/bin/python`，激活方式 `source /root/miniconda3/bin/activate`
- SciERC checkpoint：`checkpoints/qwen3-8b-scierc-merged-v2`（ft_002_v2, rank=32）
- Few-NERD checkpoint：`checkpoints/qwen3-8b-fewnerd-exp021-merged`（exp-021, 3 epoch）
- LLaMA checkpoint：`checkpoints/llama3.1-8b-scierc-merged`
- 数据：`data/scierc/processed_data`（551 inst），`data/fewnerd_n16_subset`（5000 inst），`data/conll2003/`
- 活跃进程：exp_028 PID 371545, tmux=exp_028_fewnerd_5epoch, cuda:0（5-epoch Few-NERD 训练，step ~1477/41180 截至 09:12，预计 ~2026-05-18 08:00 完成）
- 本地项目目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/`
- 论文目录：`docs/paper/sections/`（experiments.tex, introduction.tex 等）
- Figure 脚本：`output/figures/plot_degeneracy_lp.py`

### 3. 📊 当前状态
**刚完成**：
- exp-026 T ablation 三组（T=0.5/0.8/1.2）推理+分析+收尾全部 DONE/success。Degeneracy 已修正为 Constant F1 定义，within-instance ρ(LP,F1) 已补算
- exp-024 claim audit：97✅/1❌/5⚠️。唯一 ❌（experiments.tex L52 WNUT ρ 混引）已修复
- Figure 3 Option A 最终修正完成（cross_delta SciERC 0.62→0.42）
- 引用修复 5/5（2 CRITICAL + 3 MINOR）
- MLP verifier：feature bottleneck 确认（MLP ≤ LR，支持论文结论）

**RUNNING**：
- exp_028 (cuda:0)：Few-NERD 5-epoch LoRA 训练，PID 371545，预计 ~明早完成。训练完需 merge LoRA → inference 5000 subset → 测 degeneracy 变化

**空闲**：cuda:1/2/3 空闲。Director 明确说"等 exp_028 明天完成后统一规划"，不需要为占用而跑实验。

**无等待中的 Worker/Cron 回调**（除 exp_028 的 cron 监控）。

### 4. 📋 待办（条件触发式）
- exp_028 cron 回调（训练完成）→ spawn Worker: merge LoRA checkpoint → N=8 T=1.0 inference on 5000 subset with logprobs → 计算 degeneracy rate + LP selection F1 → 对比 exp-021 (3-epoch) 数据 → 更新 registry → 汇报 Director
- exp_028 conclusion=success（degeneracy 无显著变化）→ 确认 "low degeneracy is structural property of Few-NERD, not under-convergence"，支持论文 claim
- exp_028 conclusion=negative（degeneracy 显著上升）→ 需要修改论文中 Few-NERD 相关叙述，产出 Framing 提案给 Director
- Director 指派 Paper Agent 写 MLP verifier 段落 → 不需要你做，但可能需要提供数据（`artifacts/` 下已有 `mlp_verifier_comparison.json`）
- Director 要求处理 claim audit ⚠️ 项 → 特别是 LP range 差异（0.041 vs 0.060 at T=1.0）需要确认数据源

### 5. 🎯 战略上下文
- **论文核心**：Structured self-consistency for IE quality estimation。Claim 1 = dual contribution（QE positive + selection diagnostic），Claim 2 = methodology
- **Regime-dependent thesis 是论文骨架**：degeneracy 控制 selection 效果。高 degen（CoNLL 47%）→ selection 失败；低 degen（Few-NERD 14%）→ LP selection 有效（+1.36pp N=8, +1.88pp N=16）
- **T ablation（exp-026）刚提供了最强证据**：T↓ → degen↑ + LP range↓ + selection↓。T=0.8 是 sweet spot（LP Δ +1.1pp）
- **DDL ~8 天**（从 5/17 算）。exp_028 是最后一个 GPU 实验，之后全是论文打磨
- **易错点**：
  - 不要混淆 full-set vs gold-filtered 数值（+0.42 vs +0.62）
  - 不要混淆 global ρ vs within-instance ρ vs conditional ρ（三种完全不同的指标）
  - T=1.0 对照数据有两个来源（exp_012 vs exp_026 同 checkpoint 重跑），greedy F1 不同（0.585 vs 0.618），跨温度比较用 selection delta 不用绝对值
  - exp_028_fewnerd_5epoch 是 exp_028 的重复条目（同 PID 371545），conclusion=killed，忽略它


---
