# audit hypothesis deep review

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_hypothesis_deep_review_20260517T034811_result.json`
- **Structured JSON:** [`edf24af01559e71d2aa0.json`](../../sessions/ed/edf24af01559e71d2aa0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All registry updates and idea submission complete. Here's the full analysis output:

---

## Part A: Negative Experiment Deep Analysis

### 1. exp006-pooled-05B-15B-gsm8k-v2

**Hypothesis** (补): Pooled 0.5B+1.5B IRT (N=8) with RRF-derived exposure on GSM8K will yield significant gamma.

**a) 证伪说明什么：** GSM8K 作为生成式 benchmark，contamination signal 天然弱（d000 exposure=0.613 vs d005=0.629，几乎无区分力）。结合 MCMC 收敛失败（rhat=1.015, ess=330）和 N=8 不足，gamma 不显著反映的是 **信号+benchmark 交互问题**，而非方法失败。

**b) 当时处理：** D024 将 GSM8K 降级为负对照（非主结果），D034 切回 S1-only exposure（废弃 RRF），后续 exp006 聚焦 ARC/MMLU MCQ benchmarks。

**c) 处理评估：** 正确。GSM8K 作为负对照实际强化了论文叙事（"benchmark-dependent effect"）。无遗漏。

**d) Parent 链：** exp006-pooled-05B-15B-arc-v2 → exp006-pooled-05B-15B-gsm8k-v2（从 ARC 成功推广到 GSM8K 失败）

---

### 2. exp006_cross_family_pooled_irt

**a) 证伪说明什么：** Gamma 是 **family-specific** 参数，不同模型家族对 SFT 污染反应机制不同。Qwen-only ARC gamma=0.727 → pooled gamma=0.002（delta=-0.725），说明 Llama 的 clean-only 纳入稀释了 Qwen 的 contamination signal。

**b) 当时处理：** D122 将 cross-family gamma 定位为 "within-family diagnostic"；D124 降级为 "calibration robustness" 待 s1 fix 后重评。

**c) 处理评估：** 基本正确，但**遗漏了 hierarchical gamma 方法改进方向**。当前处理是放弃跨家族 gamma，但更好的做法是引入 hierarchical gamma 模型（每 family 独立 gamma_f + shared hyperprior），已写入 ideas.md。

**d) Parent 链：** exp_006_pooled_2pl_gamma_qwen_n24 → exp006_cross_family_pooled_irt

---

### 3. exp_005_noise_prop_v4

**Hypothesis** (改写): Measurement error (sigma_e) propagates through IRT to widen calibrated-score CIs monotonically; CI width is dominated by sigma_e magnitude.

**a) 证伪说明什么：** CI width 对 sigma_e 完全不敏感（0.0997-0.1000 跨 5 个 sigma_e 水平），monotonicity rho=0.4, p=0.505。证明 **CI 瓶颈是 N_models 而非 exposure noise**——N=5 下 posterior 被 prior 主导，sigma_e 的影响被 overwhelm。

**b) 当时处理：** D013 废弃 analytic ME model，统一使用 simple model；exp-005 降级为附录 robustness check。

**c) 处理评估：** 正确。结论与 exp-004 sweep 一致（N 是主要约束）。无遗漏——后续通过 multi-seed pooling 提升 N 是正确路径。

**d) Parent 链：** exp_004_sim_sweep → exp_005_noise_prop_v4（sim_sweep 发现 CI 随 N 改善，noise_prop 验证 CI 不随 sigma_e 改善）

---

### 4. exp_006_pooled_irt_05b_15b_arc_2pl

**Hypothesis** (补): 2PL+gamma on 0.5B+1.5B ARC detects significant negative gamma replicating forgetting pattern.

**a) 证伪说明什么：** PPP=0.000 说明即使 2PL（比 4PL 更简单）也存在 model misspecification。ARC gamma=2.73 CI排除0，但 PPP 失败意味着估计不可信。**问题不是模型复杂度，而是 ARC 数据违反 IRT 单维性假设**。

**b) 当时处理：** D053 废弃联合 IRT，D120 对 ARC 启动 gating criterion（PPP<0.1 → 报 raw scores）。

**c) 处理评估：** 正确。gating 是 pragmatic 解决方案。潜在遗漏：未深入调查 ARC 多维性来源（可能是 STEM vs humanities 子域）。

**d) Parent 链：** exp006-pooled-05B-15B-arc-v2 → exp_006_pooled_irt_05b_15b_arc_2pl

---

### 5. exp_006_scale_stratified_irt

**Hypothesis** (补): Per-scale 2PL+gamma (N=6-8 per stratum) produces reliable scale-specific gamma estimates.

**a) 证伪说明什么：** N=6-8 per stratum 严重不足——gamma 方向不一致（1.5B MMLU gamma=-0.30 vs 3B gamma=+5.70），PPP 全面失败。证明 **stratification 在当前 N 下不可行**，必须 cross-scale pooling。

**b) 当时处理：** D110 将其定位为 ablation motivating cross-scale pooling，在论文中作为 "per-scale insufficient" 的诚实负结果。

**c) 处理评估：** 正确且有价值——负结果直接 motivate 了 pooled IRT 设计。无遗漏。

**d) Parent 链：** exp_006_pooled_2pl_gamma_qwen_n24 → exp_006_scale_stratified_irt

---

## Part B: Director 判断验证

1. **exp-005 → parent exp-004**: ✅ 已确认并设置。exp_004_sim_sweep 发现 gamma recovery 依赖 N≥50，exp_005 进一步探索是否 sigma_e（而非 N���是 CI 主要驱动力。逻辑推导链成立。

2. **Cross-family γ collapse → hierarchical γ**: ✅ 已分析并写入 ideas.md ACTIVE section。Gamma 从 0.73 崩塌到 0.002 是强烈的 family-specificity 信号，hierarchical model 是 natural next step。

3. **Signal failures → C2 concern**: ✅ 确认正确。exp_002_signals_3B 经历 v1-v9 共 8 次失败（disk quota, TMPDIR race, GPU conflict），最终在 v9 成功。这些失败暴露了跨家族数据严重不足（仅 Llama 4 models），正确升级为论文 C2 concern（N 不足限制跨家族 generalizability claim）。

---

## Part D: 摘要

| 指标 | 数量 |
|------|------|
| Negative 实验分析 | 5/5 |
| 补写 hypothesis | 20 条 |
| 设置 parent 链 | 7 条 (5 negative + 部分已有) |
| 新 idea 写入 | 1 (hierarchical gamma) |

**遗漏的方法改进方向：** Hierarchical/family-stratified gamma model（已写入 ideas.md）。

**Parent 链总结：**
- exp_004_sim_sweep → exp_005_noise_prop_v4
- exp006-pooled-05B-15B-arc-v2 → exp006-pooled-05B-15B-gsm8k-v2
- exp006-pooled-05B-15B-arc-v2 → exp_006_pooled_irt_05b_15b_arc_2pl
- exp_006_pooled_2pl_gamma_qwen_n24 → exp006_cross_family_pooled_irt
- exp_006_pooled_2pl_gamma_qwen_n24 → exp_006_scale_stratified_irt

---
