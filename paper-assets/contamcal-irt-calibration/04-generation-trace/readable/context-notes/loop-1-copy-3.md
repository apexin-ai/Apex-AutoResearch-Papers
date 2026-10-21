# reviewer / loop_1.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`56e951f69ebf47274011.json`](../../sessions/56/56e951f69ebf47274011.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-13T20:36:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 cqa1-21977 是 AutoDL 实例，6× RTX 4090 (24GB each)，GPU 0-5 全部属于本项目，无跨项目共享限制
- MMLU paraphrase 使用 vLLM on GPU 0（PID 204758），**不要 kill**——这是唯一成功用 vLLM 的 benchmark，GSM8K/ARC 都因 "duplicate template name" 回退到 transformers
- SFT 数据当前仅含 ARC+GSM8K contamination（MMLU paraphrase 未完成），dosage 文件需在 MMLU 完成后重新生成
- D010 决策：跳过 QC 过滤，使用全部 paraphrase（GSM8K QC 仅 17.3%，ARC 59.5%）——我已标 WARNING 但 Director 未回应，需持续关注对 γ 估计的影响

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-21977`，工作目录 `/root/contamcal-irt-calibration`
- Python：`/root/miniconda3/bin/python3`（conda base 环境，非 venv）
- 模型：`/root/autodl-tmp/models/Qwen/` 下有 Qwen2.5-{0.5B,1.5B,3B,7B-Instruct}
- 数据：paraphrases → `/root/autodl-tmp/exp001/paraphrases/`，SFT data → `/root/autodl-tmp/exp001/sft_data/`，checkpoints → `/root/autodl-tmp/exp001/checkpoints/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/`
- CPU 实验（exp_004 sweep, exp_005 noise prop）在本地 workspace 的 `.venv` 环境里跑
- 训练日志：`/root/runs/contamcal-irt-calibration/` (tmux sessions via submit_training_job)

### 3. 📊 当前状态
**刚完成**：审查 exp_001_sft_0pct_05B (0.5B, 0% dosage, seed=42) — PASS，LoRA adapter 已保存。

**Registry RUNNING/ANALYZING（9 experiments total）**：
- `exp_001_sft_injection` RUNNING — Phase 1 MMLU paraphrase 仍在 GPU 0 (vLLM, 上次 ~21%)
- `exp_001_sft_0pct` RUNNING — 伞状实验
- `exp_001_sft_0pct_05B` ANALYZING — 0.5B 完成，GPU 3 已释放
- `exp_001_sft_0pct_15B` RUNNING — 1.5B on GPU 4 (~6%, ETA ~90 min from last check)
- `exp_001_sft_0pct_3B` RUNNING — 3B on GPU 5 (~1%, ETA ~3h from last check)
- `exp_004_sim_sweep` RUNNING — CPU, seed 4 of auc0.55_n50 (12 conditions × 10 seeds, ~28h remaining)
- `exp_005_noise_prop` RUNNING — CPU, σ_e=0.1 seed=42 first chain (~40h total)

**GPU 空闲**：1, 2, 3 空闲。已提醒 Director 分配 contaminated dosage SFT 或 additional seeds。

### 4. 📋 待办（条件触发式）
- MMLU paraphrase 完成 → 验证输出文件 + QC 统计 → 提醒 Agent 重新生成含 MMLU 的 SFT dosage 文件
- exp_001_sft_0pct_15B / 3B 完成 cron 回调 → 审查 loss 曲线 + checkpoint 完整性
- contaminated dosage SFT 启动 → 核查 GPU 分配 + contamination labels 正确性（哪些 items 被注入）
- exp_004_sim_sweep 完成 → 审查 12 conditions 的 γ recovery、AUC threshold、N_models scaling
- exp_005_noise_prop 完成 → 审查 ME attenuation 是否匹配 Fisher Info Corollary 2 理论值
- 任何 Worker 提交论文章节修改 → 按 §5 写作审查维度审查，特别关注 claim 强度 vs evidence

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 ARR May 25（D006），12 天冲刺，今天是 Day 1
- **核心方法**：2-stage ContamCal = RRF fusion (4 signals) → 4PL+γ IRT (Bayesian Stan NUTS)
- **MVP 已通过**（D004）：mvp_sim_4pl_gamma + mvp_sim_confounding 均 PASS，γ 可分离
- **Fisher Info 理论推导已验证**：Theorem 1 (I(γ) = Σw·τ²)，Corollary 1 (AUC-Info)，Corollary 2 (ME attenuation) 均与 MC 数值吻合
- **最大风险点**：
  1. GSM8K paraphrase QC 仅 17.3%——如果 γ 估计不出来，无法确定是方法问题还是注入失败
  2. exp-008 (RL signal survival) 尚未启动但 Related Work Table 2 已标 ContamCal "RL-robust partial✓"——如果 exp-008 结果不支持，需删除该 claim
  3. "2+ model families" claim 多次标记（exp-014 deferred to rebuttal）——目前只有 Qwen 一个 family
- **易踩的坑**：
  - 监控系统会对无 sentinel/W&B 的长 nohup 进程误判 failed（本轮已踩过，exp_001 被误标 5 次）
  - contam_irt_4pl_me_analytic.stan 的 dead code bug 已修复，但注意区分 `contam_irt_4pl_me.stan`（full latent τ，exp_005 在用）和 `contam_irt_4pl_me_analytic.stan`（analytical，exp_006 将用）
  - 论文 experiments.tex 的 B1 baseline 描述 "75th percentile" 未与代码核实——我标了 warning 但没人跟进


---
