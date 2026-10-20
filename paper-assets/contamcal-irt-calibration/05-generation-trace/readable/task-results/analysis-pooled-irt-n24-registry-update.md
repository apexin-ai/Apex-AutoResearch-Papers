# analysis pooled irt n24 registry update

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pooled-irt-n24-registry-update_20260516T191706_result.json`
- **Structured JSON:** [`7e2663ac37476c7615d4.json`](../../sessions/7e/7e2663ac37476c7615d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated: `exp_006_pooled_2pl_gamma_qwen_n24` → DONE/success with full metrics.

---

## 结果解读

**GSM8K** — 最强结果。γ≈0（无污染信号）但 ΔMAE=0.163（96% MAE 降幅），PPP=0.54（完美拟合）。IRT 的 ability + difficulty 参数单独就能把 raw 0.11–0.74 的 accuracy 校准到 MAE=0.006。这是 Claim 2（calibration effectiveness independent of contamination）的 headline evidence。

**MMLU** — γ=0.66 但 95% CI 跨 0。PPP=0.19 模型拟合可接受。γ 不显著符合 D108 domain heterogeneity 假设：14042 items 里 subsample 300, 污染信号被稀释。校准仍有效（ΔMAE=0.009）。

**ARC** — γ=0.73, CI 排除 0（污染信号显著），但 **PPP=0.003 表示严重 model misfit**。观察发现 obs_mean=0.799 vs pred_mean=0.780，模型系统性低估。根因：1.5B (~0.76) 和 3B (~0.83) 形成双峰 ability 分布，N=16 下 2PL 拟合困难。

---

## ARC Misfit 诊断

PPP=0.003 **不是** 3PL 的问题。在 75-83% accuracy 下（4选1 MCQ），guessing floor (25%) 远低于实际表现，加 guessing parameter 不会改善拟合。

真正原因：两个 scale 之间 ability gap 太大且每个 scale 内部 variance 很小，导致 item discrimination 估计不稳定。解决路径：

1. **增加 N（优先）**：加入 0.5B respondents（如果 ARC signals 就绪），N=24 的三层 ability 分布比 N=16 的双峰好拟合得多
2. **多组 IRT**：用 scale 作为 group covariate 的 hierarchical 2PL+γ
3. **接受并报告为 limitation**：ARC cal_MAE=0.020 仍优于 raw_MAE=0.034（40% 降幅），只是统计检验力不足

**不建议跑 3PL+γ**——根据 C008 规则，N=16 已经低于 4PL 的 identifiability 门槛，3PL 多一个参数同样有风险，且 guessing 不是此处的问题。

---

## 对论文的影响

| Claim | 支撑强度 | 来源 |
|-------|---------|------|
| Claim 2: IRT calibration effective | **强** | GSM8K ΔMAE=0.163, PPP=0.54 |
| Claim 1: γ detects contamination | **中** | ARC γ显著但 model misfit; MMLU γ不显著 |

---

## 建议下一步

**最高优先级**：等 0.5B s123 signals 完成后，重跑 ARC pooled IRT（N=24，三个 scale），预期 PPP 显著改善。这同时满足 C007 优先级（0.5B s123 是最高 ROI）和解决 ARC misfit。不需要单独跑 3PL+γ 实验。

---
