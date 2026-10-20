# reviewer / loop_13.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`6038624d79296baf4ae7.json`](../../sessions/60/6038624d79296baf4ae7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-16T14:35:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-47453 GPU 分配：cuda:0 threshold_q07, cuda:1 rho02_uniform, cuda:2 batch_adaptive_tau, cuda:3 threshold_q03。westd-41312：cuda:0 llama3b_uniform, cuda:1 llama3b_adaptive, cuda:2 hybrid_rho04, cuda:3 hybrid_rho06
- random_reweight_v2 脚本当前 CUDA_VISIBLE_DEVICES=-1（安全占位），提交前**必须改为实际 GPU ID**
- westd-47453 根分区 30G 仅剩 7.1G（77%），**禁止在根分区写大文件**，模型/checkpoint 必须走 /root/autodl-tmp/
- Llama-3B 实验 lr=5e-5 已知偏高，完成后需检查是否 diverge，但不要中途干预（uniform/adaptive 用同一 LR，相对比较仍公平）
- random_reweight_v2 **未在 registry PREPARING 队列中**（D055 标记 P0 但 registry 未更新），GPU 释放时需同步注册+提交

### 2. 🖥️ 基础设施快照
- **westd-47453**: 4× RTX PRO 6000 96G, /root/provenance_weight_training, conda base (/root/miniconda3/bin/python)
- **westd-41312**: 4× RTX PRO 6000 96G, /root/provenance_weight_training, conda base (/root/miniconda3/bin/python)
- 数据盘: westd-47453 /root/autodl-tmp (250G, 45G free 83%), westd-41312 /root/autodl-tmp (250G, 217G free 14%)
- HF cache: /root/autodl-tmp/.hf_cache（两台）
- WANDB: 项目用 WANDB_MODE=offline 或 disabled（v2 脚本用 disabled）
- 本地 workspace: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/
- 活跃进程（PID 均为 bash wrapper 或 python 子进程）:
  - 47453: 324550(threshold_q07), 316980(rho02_uniform), 326274(batch_adaptive_tau), 325196(threshold_q03)
  - 41312: 3112(llama3b_uniform), 4005(llama3b_adaptive), 3656(hybrid_rho04), 3727(hybrid_rho06)

### 3. 📊 当前状态
Loop #13 续，8 GPU 满载无空闲。最近一次全面巡检进度：

| 实验 | 服务器 | 步数 | 进度 | 预计剩余 |
|------|--------|------|------|----------|
| threshold_q07 (resume) | 47453:0 | 3999/6103 | 65% | ~5h（**最先完成**）|
| rho02_uniform | 47453:1 | 2809/6103 | 46% | ~7h |
| batch_adaptive_tau_rho04 | 47453:2 | 1889/6103 | 31% | ~9h |
| threshold_q03 (restart) | 47453:3 | 1999/6103 | 33% | ~10h |
| hybrid_rho04 | 41312:2 | 1499/6103 | 25% | ~10h |
| hybrid_rho06 | 41312:3 | 1499/6103 | 25% | ~10h |
| llama3b_uniform | 41312:0 | 999/6103 | 16% | ~22h |
| llama3b_adaptive | 41312:1 | 999/6103 | 16% | ~22h |

PREPARING 队列（5）：bs8_auto_nmin, batch_adaptive_tau_rho06, rho02_adaptive_tau09, batchsize16_nmin8, grid_b0_2

本轮已发 6 次 reviewer_post_to_director：GPU 状态巡检(WARNING)、ROADMAP 审查×2(WARNING/INFO)、rho02_tau09 代码检查(WARNING)、random_reweight 诊断(INFO)、结构性审视(WARNING)、b* 分析审查(WARNING)、random_reweight_v2 代码审查(INFO)

### 4. 📋 待办（条件触发式）
- **threshold_q07 完成** → 审查最终 PPL（⚠️ LR 中断风险：checkpoint-2000 resume 无 optimizer/scheduler，LR 经历了重启-爬升-衰减），检查 PPL 是否有异常偏差 → GPU 0 给 random_reweight_v2（需注册 registry + 改 CUDA_VISIBLE_DEVICES=0 + 提交）
- **rho02_uniform 完成** → 审查 PPL → GPU 1 给 rho02_adaptive_tau09（Claim 3 第三验证点，τ=0.9）
- **hybrid_rho04/rho06 完成** → 审查 PPL，对比 detect_remove(17.29) 和 standard adaptive(17.651/17.730) → 判断 Plan C 是否值得论文 section
- **llama3b 两个完成** → 审查 adaptive vs uniform 相对排序是否与 Qwen 一致（跨模型泛化性）；检查 loss 曲线有无 spike（lr=5e-5 偏高风险）
- **batch_adaptive_tau_rho04 完成** → 对比 fixed-τ adaptive(17.651)，判断 Plan B 价值 → GPU 给 batch_adaptive_tau_rho06
- **random_reweight_v2 完成** → **最关键审查**：PPL 应显著差于 adaptive(17.651)。若 random ≈ adaptive → Claim 1/2 的 detector-signal-is-load-bearing 论证崩溃，**立即 CRITICAL 通知 Director**

### 5. 🎯 战略上下文
- **投稿目标**: EMNLP 2026 ARR May 25（9 天）
- **核心方法**: Dual-constrained adaptive b* (α_eff ≥ τ AND ESS ≥ n_min)
- **三个 Claim**: (1) dual > ESS-only ★★★★☆, (2) adaptive ≈ grid-best ★★★☆☆, (3→推论) proportion-agnostic ★★☆☆☆
- **D055 关键决策**: Claim 3 降级为 Claim 2 推论；random_reweight 是唯一可被一击致命的缺口
- **已发现图表数据不一致**: bstar_distribution_rho_comparison.png 的 ρ=0.4 median=0.069 vs 文本分析 median=0.871（图表可能未排除 eval checkpoint 数据），alpha_eff_binding_rate 图同样有矛盾。**论文用图前必须修复**
- **b* 对 ρ 不敏感的双刃剑**: binding_diagnosis 发现 b* 在 ρ=0.4 和 0.6 之间几乎不变（mean 1.393 vs 1.390）。正面：天然 proportion-agnostic。负面：审稿人可问"为什么不直接用固定 b=0.87"。论文需主动讨论
- **易错点**: (1) threshold_q07 有 LR 中断，PPL 可能偏差——不要直接用作 calibration 标准；(2) detect_remove PPL=17.29 看似大幅优于 adaptive 17.651，但 eval_holdout 是纯人类数据导致的 confound（D051），不能直接比较；(3) 两台服务器都是 AutoDL 实例，可能被回收——进程死亡不一定是代码 bug


---
