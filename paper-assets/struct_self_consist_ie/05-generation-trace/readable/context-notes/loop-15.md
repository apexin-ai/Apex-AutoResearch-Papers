# agent / loop_15.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`e581c924e1bf5642fcd3.json`](../../sessions/e5/e581c924e1bf5642fcd3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: idle_timeout
updated: '2026-05-17T18:39:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 cuda:0/1/2/3（4 张 5090）。不得使用白名单外 GPU，即使 Director 指令也要 push back
- ρ=-0.881 (p=0.004) 是 KeySet degen vs **oracle headroom**，已被 Reviewer 确认正确。**绝对不要质疑、重算、或提议修���**（M003）
- SciERC LP Δ 论文统一用 **+0.42pp (full-set n=551)**，不是 +0.62pp (gold-filtered n=529)
- Degeneracy 定义：论文 dataset-level 用 **Constant F1 gold-filtered**，per-type 用 **KeySet(text,type)**。两个定义不能混用
- submit_training_job 命令必须 `bash -c "..."` 包裹（tmux 用 /bin/sh）
- AdaLP (D128) 已 DROP——per-instance degen 需要 gold labels，test time 不可用。脚本保留不用

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- Python：`source /root/miniconda3/bin/activate`（base env）
- SciERC checkpoint：`checkpoints/qwen3-8b-scierc-merged-v2`（ft_002_v2, rank=32）
- Few-NERD checkpoint：`checkpoints/qwen3-8b-fewnerd-exp021-merged`（exp-021, 3 epoch）
- LLaMA SciERC：`checkpoints/llama3.1-8b-scierc-merged`
- LLaMA CoNLL：`checkpoints/llama3.1-8b-conll2003-merged`（exp-017, 已完成）
- 数据：`data/scierc/processed_data`(551), `data/fewnerd_n16_subset`(5000), `data/conll2003/`
- 活跃进程：exp_028 4-GPU 训练，PIDs 391962-391965, tmux=exp_028, cuda:0-3, step ~16452/41180
- Cron：exp_028 registered (PID 391751, interval 300s)
- 后处理脚本：`scripts/exp_028_postprocess/run_all.sh`（merge→inference→analyze，已预写就绪）
- Calibration baseline：`scripts/calibration_baseline.py` + `output/calibration_baseline_results.json`（已完成）
- 本地项目目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/`
- 论文目录：`docs/paper/sections/`

### 3. 📊 当前状态
**刚完成**：
- exp_017_llama_conll DONE/success：LLaMA on CoNLL degen 89.2%, structural signals ρ≈0.43, cross-model validation 通过
- T ablation 表数值修正（5 处 appendix.tex：LP range 改 median, degen T=1.0 改 17.8%）
- Calibration baseline：Platt/TempScale 无法改善 selection（单调变换不改 argmax），ECE 改善但 selection 不变——强 negative baseline
- exp_028 后处理脚本预写 + 修复（ref 值从 JSON 加载，CUDA_VISIBLE_DEVICES=0）
- Claim audit LP range 0.041 vs 0.060 排查完毕（mean vs median 混淆，已修正）

**RUNNING**：
- exp_028 (4×GPU, all cards)：Few-NERD 5-epoch LoRA，step ~16452/41180 (40%), loss 0.035, ~1.77 it/s, ETA ~18:30 UTC 今天

**无等待中的 Worker/Cron 回调**（除 exp_028 cron 监控）。

### 4. 📋 待办（条件触发式）
- exp_028 cron 回调（训练完成）→ 执行 `bash scripts/exp_028_postprocess/run_all.sh`：merge LoRA → N=8 T=1.0 inference on 5000 subset → CF1 gold-filtered degeneracy + LP selection + 5 signals + 与 3-epoch 对比
- exp_028 conclusion=success（degen ≤15%）→ 确认 "low degen is structural property of Few-NERD"，Paper Agent 写 appendix epoch_confound 段
- exp_028 conclusion=negative（degen >20%）→ 产出 Framing 调整提案给 Director
- Director 分配 Paper Agent 写 Practitioner Decision Tree（Discussion/Conclusion 中 guidance 段）→ 提供数据支持（degen thresholds 30%/15%, within-instance ρ>0.3）
- Calibration baseline 结果 → Paper Agent 写入 experiments.tex 或 appendix（Reviewer "为什么不校准" 的预防性回答）

### 5. 🎯 战略上下文
- **论文核心**：Structured self-consistency for IE quality estimation。Dual contribution = QE positive + selection diagnostic。Regime-dependent thesis 是骨架
- **Cross-model 矩阵已完整**：Qwen3×{SciERC, CoNLL, Few-NERD} + LLaMA×{SciERC, CoNLL}。exp_028 是最后一个 GPU 实验
- **DDL ~8 天**（EMNLP 2026, 2026-05-25）。exp_028 后全是论文打磨
- **D127 质量冲刺进展**：AdaLP dropped (D128), calibration done (negative baseline，论文价值高), Practitioner Decision Tree 待 Paper Agent
- **T ablation 已修正**：全表改 median，与主文 0.041 一致，degen T=1.0=17.8% 与主文匹配
- **易错点**：
  - 不要混淆 full-set vs gold-filtered（+0.42 vs +0.62）
  - 不要混淆 global ρ vs within-instance ρ vs conditional ρ
  - Calibration baseline 的结论是"无法改善 selection"——这是正面结果（证明问题不在校准），不是负面的
  - exp_028 cron PID 是 391751（主进程），实际训练 PIDs 是 391962-391965
  - exp_028_fewnerd_5epoch 是 registry 中的重复条目（conclusion=killed），真实状态看 exp_028


---
