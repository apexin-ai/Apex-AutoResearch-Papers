# reviewer / loop_6.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`a940434446396fa7ed21.json`](../../sessions/a9/a940434446396fa7ed21.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-16T20:55:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只允许 cuda:0 和 cuda:1（westd-34887 的 RTX PRO 6000 Blackwell ×2）。C001 约束。
- BCE iso 实验用 `CUDA_VISIBLE_DEVICES=1`（物理 GPU 1），d_b sweep 用 `CUDA_VISIBLE_DEVICES=0`（物理 GPU 0）。不要搞反。
- 论文中所有超参数字必须有代码来源验证（C003），禁止从记忆填写。Predictor 正确参数：GELU, d_b=128, 2.37M/layer, 75.9M total。
- 论文 GPU 型号是 "NVIDIA RTX PRO 6000 Blackwell Server Edition"，不是 H800/A6000。

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887(root)，工作目录 `/root/distill_sparse_swiglu/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`/root/autodl-tmp/models/llama-3.1-8b`，Mistral：`/root/autodl-tmp/models/mistral-7b`
- HF cache：`/root/autodl-tmp/.hf_cache`，offline mode（网络不通）
- Checkpoints：`/root/distill_sparse_swiglu/checkpoints/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/`
- 活跃进程：d_b sweep (`run_db_sweep.sh`, tmux=db_sensitivity_sweep, GPU 0)，BCE iso 已完成
- Registry 无 RUNNING 实验（eval_c4_ood_kl50 stuck 为 RUNNING 但进程早已退出，需要手动 close）

### 3. 📊 当前状态
**刚完成的关键审查：**
- ✅ C4 ablation (BCE+Gumbel+Lagrangian)：3 LR 全部训练+PPL eval 完成。**PPL 38.02 (best) — 比 vanilla TEAL (23.31) 还差。Structural claim 铁证。**
- ✅ C3 OOD eval (C4 dataset)：KL advantage 52.5%，与 WikiText-2 的 49% 一致
- 🔄 d_b sensitivity sweep (64/256/512)：d_b=64 训练中/已完成，后续 256/512 排队，全在 GPU 0

**已提交给 Director 的报告：**
1. C3 OOD 核实报告（data count 132 vs 200 warning）
2. BCE+Gumbel 代码审计 critical（现已解决）
3. BCE+Gumbel PPL 最终报告（38.02 铁证）

### 4. 📋 待办
- d_b sweep 完成（cron 或手动检查 `logs/db_sweep.log`）→ 核实 d_b=64/256/512 PPL，判断 sensitivity level，报告给 Director
- eval_c4_ood_kl50 registry 未更新 → 提醒 Director/Agent 手动 close（数据在 `/root/distill_sparse_swiglu/results/c4_ood_ppl.json`）
- Paper Agent 下一轮写作提交审查 → 检查：(1) BCE+Gumbel ablation row 是否加入 table (2) C4 OOD 数据是否正确引用 (3) structural claim 措辞是否 calibrated
- Director 可能要求审查 rebuttal letter → 核对所有数字对应 registry 实验

### 5. 🎯 战略上下文
- 项目目标：EMNLP 2026 ARR May（deadline 2026-05-25，剩 9 天）
- 核心论点："KL distillation eliminates compensation networks via structural coupling"
- Round 1 review 得分 3.0/5 (borderline, Findings recommended)。审稿人主要质疑：structural claim 是否 rigorous (C4)、OOD generalization (C3)、page count (C2)、Limitations (C1)
- **C4 已解决**（BCE+Gumbel PPL 38.02 铁证），**C3 已解决**（52.5% advantage on C4）
- 易错判断：BCE+Gumbel PPL (38.02) 用的是 uniform allocation，不能直接对比原始 BCE 的 TEAL global (27.97)。公平对比是：KL uniform=11.92 vs BCE+Gumbel uniform=38.02 vs vanilla TEAL=23.31
- d_b sweep 预期是 "low sensitivity" story — d_b=64 训练 loss (0.31) 与 d_b=128 (0.30) 差异极小，但 PPL 需要确认
- 论文当前 abstract 说 "27.97 for BCE"，这是 TEAL global 下的数字，来自 eval_bce_v3_s42


---
