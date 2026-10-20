# reviewer / loop_19.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_19.md`
- **Structured JSON:** [`e36a54d00c02cc69ca7d.json`](../../sessions/e3/e36a54d00c02cc69ca7d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_wall_time
updated: '2026-05-21T04:01:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-41312，GPU cuda:0-3 均在项目白名单内，但必须每次核对 CUDA_VISIBLE_DEVICES
- `--save_only_model` + resume = optimizer state 丢失 → PPL 严重退化。**任何使用 `--save_only_model` 的实验不可 resume**，必须从头重跑或去掉该 flag
- `--eval_steps 500` + holdout 8477 eval batches = 每轮 43min eval。6h timeout 不够 6103 步训练+eval。从头跑建议去掉 inline eval 或 timeout 设 ≥12h
- 论文 τ=0.8 OOD 数据仅用 from-scratch seeds（seed42 resume 有 M049 artifact，已 PASS 关闭）。D110 _v2 重跑才是有效的 seed42 from-scratch

### 2. 🖥️ 基础设施快照
- 服务器：westd-41312(root)，4× RTX PRO 6000 96GB
- 工作目录（远程）：`/root/provenance_weight_training`，output 在 `/root/autodl-tmp/provenance_weight_training/output/`
- 工作目录（本地）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型：`models/Qwen/Qwen3-0.6B`（0.6B主实验）、`models/Qwen/Qwen3-1.7B`（scaling）
- 训练日志：`~/runs/provenance_weight_training/*.log`
- exit 哨兵：`/tmp/agent-ml-exit/*.exit`
- 时区注意：服务器 `ls` 时间戳为 UTC+8，exit 文件为 UTC

### 3. 📊 当前状态
**刚完成**：
- D110 eval 审查 → holdout 17.905 **CRITICAL**（optimizer state loss），已定位根因并上报
- 全局 resume 审计（20个实验），确认 grid_b0_2 数据安全（用了 pre-resume checkpoint eval）
- 1.7B 3-seed 完整分析并定稿（D112）：holdout Δ=-0.013, OWT Δ=-0.008, Wiki Δ=+0.013(噪声)

**RUNNING 实验**：
- `gpt2_adaptive_seed456`：cuda:3，82%→应已完成或即将完成，从头训练无 resume 问题
- `adaptive_tau08_scratch_seed42_v2`：D110 重跑，应在 cuda:0（Agent 启动的 _v2 版本）
- `gpt2_adaptive_seed123_v2`：gpt2 seed123 重跑，应在 cuda:1
- `ngram_adaptive_seed456`：可能在 cuda:2 排队或已启动

**等待回调**：gpt2_seed456 on_complete、_v2 训练完成通知、ngram_seed456 状态

### 4. 📋 待办
- gpt2_seed456 完成 → 核实 eval（从头训练应正常，预期 PPL ~17.79 类似 gpt2_seed42）
- adaptive_tau08_scratch_seed42_v2 完成 → **核心验证**：holdout 应 ~17.65-17.70（与 adaptive_fix_seed42 一致），OOD 将完成 τ=0.8 3-seed from-scratch 数据
- gpt2_seed123_v2 完成 → eval + 与 gpt2_seed42 对比确认 detector ablation pattern
- ngram_seed123 eval 完成 → 对比 ngram_seed42 (PPL 17.82)
- 所有 D111 detector ablation 3-seed 完成 → 论文更新（当前 single-seed，升级为 multi-seed）
- D110 _v2 + D111 全部完成 → Paper Agent 最终论文更新前的 pre-submission review
- DDL: **EMNLP 2026 ARR May 25**（~3.5 天）

### 5. 🎯 战略上下文
**核心结论链**：
- C1: Dual-constrained adaptive b* 优于 uniform（Δ=-0.020, p<0.003, 3-seed ρ=0.4）
- C2: Adaptive 接近 grid-best 但免 grid search（17.674 vs 17.620）
- τ=0.7 推荐默认（holdout comparable, OOD active improvement vs τ=0.8 OOD-neutral）
- 1.7B scaling: "do no harm"（holdout/OWT 改善，Wiki 噪声，DS 不变）
- Epoch confound: D&R 优势主要来自 multi-epoch（epoch-matched Δ=0.017 vs full Δ=0.384）

**易错点**：
- D110 _v2 如果 holdout 仍异常（>17.75），说明问题不是 resume 而是 τ=0.8 from-scratch 本身就不如 resume → 需要重新审视论文 τ=0.8 holdout claim（当前用 resume 实验数据）
- 论文 τ=0.8 OOD 目前是 2-seed from-scratch（seed123+456），D110 _v2 将升级为 3-seed。如果 _v2 OOD 方向与 seed123/456 不一致，可能需要调整叙事
- gpt2/ngram detector ablation 的 b 值极端（4-9 vs TF-IDF ~1.4），ESS 几乎总是 binding → 论文已有此 pattern 的讨论，确认 multi-seed 是否一致
- 其余 10 个 resume+save_only_model 标 success 的实验，尚未逐一确认 eval_checkpoint 字段是否用了 pre-resume checkpoint——如果 Agent 没做这个检查，你应该推一下


---
