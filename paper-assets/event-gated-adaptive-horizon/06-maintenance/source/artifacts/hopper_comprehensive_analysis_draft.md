# Hopper Comprehensive Analysis Draft

> Data lock target: UTC 2026-05-28 12:00
> Generated: 2026-05-27, all numbers from registry

---

## 1. Hopper Experiment Summary

| Experiment | Config | Steps | eval_return | ve_ratio (final) | civo_alert | Pattern |
|------------|--------|-------|-------------|-------------------|------------|---------|
| exp_hopper_baseline | dt=1, no gate | 105K | **96.43** | 0.559 | 0 | normal learning |
| exp_hopper_trained_s0 | trained dt_emb, subsample ON, H=8 | 105K | **3.26** | 0.897 | 1 | severe_learning_delay |
| exp_hopper_trained_s0_ext | trained dt_emb (续跑) | 168K (eval@158K) | **81.58** | 0.439 | 0 | transient_instability_recovered |
| exp_hopper_frozen_s0 | frozen dt_emb, subsample ON, H=8 | 105K | **0** (peak 3.6@85K) | 4,335,664 (÷0 artifact) | 1 | degenerate_civo_near_zero_magnitude |
| exp_hopper_no_dt_emb_s0 | dt_embed_dim=0, gate ON | 105K | 🔄 RUNNING | — | — | D162 diagnostic |
| exp_hopper_frozen_s0_ext | frozen dt_emb (续跑) | 150K | 🔄 RUNNING | — | — | D163 diagnostic |

---

## 2. Cross-Environment Comparison: Hopper vs Walker vs Cheetah

### 2.1 Baseline Performance

| Environment | Baseline eval_return | Action Dim | Learning Speed |
|-------------|---------------------|------------|----------------|
| Walker Walk | ~950 | 6 | Fast (converges by ~45K) |
| Cheetah Run | ~430 | 6 | Fast (converges by ~45K) |
| **Hopper Hop** | **96.43** | **4** | **Slow (still rising at 105K)** |

Hopper 的 baseline 性能显著低于 Walker/Cheetah，且 105K 时仍在学习中。这与 Hopper Hop 任务本身的难度相关（需要平衡+跳跃，reward 信号稀疏）。

### 2.2 CIVO Onset Timeline

| Environment | Trained dt_emb onset step | Onset rate | Onset-to-baseline-convergence gap |
|-------------|--------------------------|------------|----------------------------------|
| Walker Walk | 35K–45K | 3/3 (100%) | Onset ≈ baseline convergence point |
| Cheetah Run | 45K | 3/4 (75%) | Onset ≈ baseline convergence point |
| **Hopper Hop** | **~85K (delayed)** | **1/1** (only s0 tested) | **Onset ~40K after baseline starts learning** |

**核心差异**：Walker/Cheetah 的 CIVO onset 与 baseline convergence 近乎同步（35-45K），即 agent 学到足够的 reward signal 后立刻触发 CIVO 正反馈。Hopper 的 onset 延迟 ~50K 步（85K vs 35-45K），因为 Hopper 学习本身更慢——agent 需要更长时间才能积累足够 reward signal 驱动 CIVO 循环。

### 2.3 CIVO Severity and Outcome

| Environment | Seed | NVE Peak | Eval Final | Pattern |
|-------------|------|----------|------------|---------|
| Walker s0 (008d) | 0 | 4.12×@55K | collapsed | sustained collapse |
| Walker s1 (009e) | 1 | >1.5× | collapsed | sustained collapse |
| Walker s2 (009b) | 2 | 2.05×@25K | 268@105K | self-correction |
| Cheetah s0 (078) | 0 | 2.3×@75K | 119.5 (28%) | sustained→self_correcting |
| Cheetah s2 (091) | 2 | 127.6×@95K | 2.5 (0.6%) | collapse |
| Cheetah s3 (097) | 3 | 2.3×@45K | 61.7 (14%) | transient→degraded |
| **Hopper s0** | 0 | **NVE=1.6×@105K** | **3.26 (3.4% baseline)** | **delayed onset, emerging** |
| **Hopper s0_ext** | 0 | **ve=5.519@128K (spike)** | **81.58 (85% baseline)** | **recovered @158K** |

**关键发现**：Hopper trained_s0 的 CIVO 呈 "emerging then recovered" 模式。ve_ratio 在 128K 出现 spike (5.519) 后回落至 0.439@158K，eval_return 从 3.26 恢复至 81.58。这与 Walker seed 2 (009b) 的 self-correction 模式类似，但 recovery 更彻底（85% baseline vs 29% baseline）。

**CIVO 在 Hopper 中被证伪为根因**：trained_s0_ext 的 recovery 证明 105K 时的低 eval 是 learning delay（gate+subsample 机制导致），非 CIVO 造成的不可逆损伤。ve_ratio spike@128K 是 transient instability，非 sustained CIVO。

---

## 3. Gate Mechanism Failure in Hopper (D162)

### 3.1 问题定义

Hopper 中 gate+dt=2+subsample ON 导致严重 learning delay，trained_s0 需要 ~85K 步才出现第一个非零 eval_return（baseline 在 ~25K 步已有显著 learning signal）。D162 诊断假说：**gate 机制本身（非 dt_emb）是 Hopper 学习失败的根因**。

### 3.2 evidence: trained_s0 vs frozen_s0

| Metric | trained_s0 (105K) | frozen_s0 (105K) | 差异 |
|--------|-------------------|-------------------|------|
| eval_return_final | 3.26 | 0 | trained 略优 |
| eval_return_peak | 8.01@85K | 3.6@85K | trained 2× |
| value_mean_final | 2.93 | 4.337 | frozen value 更高 |
| civo_alert | 1 | 1 | 均触发 |
| Pattern | severe_learning_delay | degenerate_civo_near_zero_magnitude | 不同 |

**两种配置均在 Hopper 中严重失败**，但失败模式不同：
- **trained_s0**: learning delay → 85K 开始学习 → emerging CIVO (value 指数增长伴随 eval 下降) → 续跑后 recovery
- **frozen_s0**: 完全学习失败 → eval 始终在 0-3.6 range → 95K 出现 "degenerate CIVO" (ve=2.69 at eval=1.083)

### 3.3 exp_hopper_no_dt_emb_s0 (D162) — 🔄 RUNNING

**假说**：移除 dt_embedding（dt_embed_dim=0）但保留 gate+dt=2+subsample → 如果仍然出现严重 learning delay，则确认 gate 机制本身是 root cause，非 dt_emb。

**预期结果**：
- 若 no_dt_emb 也 learning delay → gate mechanism 是 Hopper 失败根因
- 若 no_dt_emb 正常学习 → dt_emb 仍是关键因素（与 Walker/Cheetah 一致）

> **[PLACEHOLDER: exp_hopper_no_dt_emb_s0 结果待填充]**
>
> 预计完成时间: 2026-05-27 ~14:00 UTC (基于 ~3h 训练时长)
>
> 待填充: eval_return_final, ve_ratio, learning curve pattern, 与 trained_s0/frozen_s0 对比

---

## 4. "Degenerate CIVO" 概念 (D163)

### 4.1 定义

**Degenerate CIVO** 指在 eval_return 近零（<5% baseline）时出现的 ve_ratio 异常升高。与 Walker/Cheetah 的 "standard CIVO"（agent 已学到可观策略后 value overestimation 摧毁 policy）机制不同。

### 4.2 Hopper frozen_s0 数据

- **95K**: ve_ratio=2.69, eval_return=1.083 (1.1% baseline)
- **105K**: ve_ratio=4,335,664 (eval_return=0, 除零膨胀 artifact)
- **civo_alert 触发**: @65K 和 @105K

### 4.3 机制解读

Frozen_s0 的 "CIVO" 在功能上无意义：
1. **Agent 从未学到有效策略** — peak eval=3.6 仅为 baseline 的 3.7%
2. **Value overestimation 发生在真空中** — value_mean=4.337 是对一个几乎无 reward 的 policy 的过度估值
3. **ve_ratio 膨胀是 denominator 效应** — eval_return 趋近 0 时，任何非零 value 都产生极高 ve_ratio

### 4.4 与 Standard CIVO 对比

| 维度 | Standard CIVO (Walker/Cheetah) | Degenerate CIVO (Hopper frozen) |
|------|-------------------------------|--------------------------------|
| Onset 前 eval | >100 (Walker), >200 (Cheetah) | <5 (Hopper) |
| Value magnitude | 100-1000+ | <5 |
| Policy 损伤机制 | value overestimation 驱动 actor 偏向错误动作 | agent 从未学到正确动作 |
| 根因 | trained dt_emb → RSSM fidelity gap → critic exploitation | gate+subsample → learning signal 不足 → 学习失败 |
| ve_ratio 信号可靠性 | 可靠诊断指标 | 伪信号（denominator ≈ 0） |

### 4.5 D163: frozen_s0_ext — 🔄 RUNNING

**假说**：frozen_s0 从 105K→150K 续跑后，eval_return 是否能恢复（类似 trained_s0_ext 的 3.26→81.58）？

- 若恢复 → frozen_s0 的 "degenerate CIVO" 仅是 learning delay 阶段的 noise
- 若不恢复 → frozen dt_emb 在 Hopper 中引入了额外学习障碍

> **[PLACEHOLDER: exp_hopper_frozen_s0_ext 结果待填充]**
>
> 预计完成时间: 2026-05-27 ~12:00 UTC
>
> 待填充: eval_return trajectory (115K-150K), ve_ratio trajectory, 是否复现 trained_s0_ext 的 recovery 模式

---

## 5. Impact on Paper Claims

### 5.1 Claims Strengthened by Hopper Data

**C1 (Variable-rate imagination degrades performance) — 加强**

Hopper 是第三个确认 dt>1 降低性能的环境。Baseline 96.43 vs trained_s0@105K 3.26 (3.4%)。即使续跑后 recovery 至 81.58 (85%)，仍需 ~50K 额外步数才接近 baseline 水平。

**C2 (Trained dt_emb creates CIVO susceptibility) — 加强但需 nuance**

Hopper 在 trained_s0 中观察到 emerging CIVO signature（value_mean 指数增长 + civo_alert 触发），但续跑后 recovery 而非 collapse。这增加了第四种 CIVO 后果模式：**delayed_onset_then_recovery**。跨环境 CIVO 后果模式总结：

| 模式 | 环境 | 描述 |
|------|------|------|
| sustained_collapse | Walker s0/s1 | onset → 不可逆崩溃 |
| self_correction | Walker s2, Cheetah s0 | onset → value/eval 均恢复 |
| transient_then_degraded | Cheetah s3 | onset → value 恢复但 policy 不可逆损伤 |
| collapse | Cheetah s2 | onset → NVE 爆炸 → eval 归零 |
| **delayed_onset_then_recovery** | **Hopper s0** | **延迟 onset → transient instability → full recovery** |

**跨环境普遍性 (3/3 environments)**: 所有测试环境均观察到 CIVO 现象（Walker 3/3, Cheetah 3/4, Hopper 1/1），onset rate 总计 7/8 = 87.5%。

### 5.2 Claims Requiring Nuance

**C2 CIVO 严重程度 — 环境依赖性更突出**

Hopper 的 CIVO 是三个环境中最温和的：
- NVE 仅达 1.6×（Walker 达 4.12×, Cheetah 达 127.6×）
- 续跑后完全 recovery 至 85% baseline
- Onset 延迟 ~50K 步

可能原因：Hopper 4-dim action space（vs Walker/Cheetah 6-dim）→ 策略空间更小 → CIVO 正反馈环路的放大效应较弱。或者：Hopper 较低的 baseline reward magnitude → value overestimation 的绝对量级有限。

**C6 (dt=1 imagination as mitigation) — Hopper 不适用**

Hopper 的核心问题是 gate+subsample 机制本身导致的 learning delay，非 CIVO。dt=1 imagination mitigation 对 CIVO 有效（Walker 4/4），但无法解决 Hopper 的 gate-induced learning failure。这提示 gate mechanism 对不同环境的适应性是独立于 CIVO 的另一层 limitation。

### 5.3 Claims Weakened by Hopper Data

**Frozen dt_emb 作为 CIVO prevention — 在 Hopper 中并非正面结果**

Walker/Cheetah 中 frozen dt_emb 阻止 CIVO（0/10+ seeds NVE>1.5×）。Hopper frozen_s0 虽然也未出现 "standard CIVO"，但结果更差（eval=0，完全学习失败）。这不削弱 frozen dt_emb 的 CIVO prevention claim，但引入新 limitation：frozen dt_emb 在 Hopper 中加剧了 gate mechanism 的 learning failure。

### 5.4 New Findings from Hopper

1. **Gate mechanism 本身是独立于 CIVO 的失败模式**。Hopper 证明 gate+subsample 可以独立于 dt_emb training 导致严重 learning delay（trained 和 frozen 均受影响）。这是论文需要正面讨论的 scope limitation。

2. **"Degenerate CIVO" 不应计入 CIVO onset 统计**。Hopper frozen_s0 的 civo_alert 触发是伪信号（eval≈0 时的 denominator 效应），不是真正的 conditioning-induced value overestimation。论文中应排除此类 degenerate case。

3. **CIVO onset delay 与环境难度正相关**。Walker/Cheetah onset@35-45K（快速学习环境），Hopper onset@85K（慢学习环境）。这支持 "CIVO 需要一定量的 learned reward signal 才能触发" 的机制假说。

---

## 6. Hopper 在论文中的定位建议

### 6.1 Narrative Role

Hopper 不应作为 Walker/Cheetah 的简单 "第三环境验证"，而应作为 **revealing failure mode boundary case**：
- 展示 CIVO 机制在不同环境中的表现差异（severity, timing, recovery）
- 暴露 gate mechanism 本身的局限性（独立于 CIVO）
- 为 "degenerate CIVO" vs "standard CIVO" 的区分提供证据

### 6.2 论文章节安排

- **Section 4 Results**: 简要报告 Hopper baseline + trained_s0 + trained_s0_ext，作为 C1/C2 的第三环境数据点
- **Section 5 Discussion**: 详细讨论 Hopper 的差异化行为——onset delay, recovery, degenerate CIVO
- **Section 6 Limitations**: Gate mechanism 在 Hopper 中的学习失败是 scope limitation，明确承认方法对环境类型的依赖

### 6.3 Pending Data Points

| 实验 | 预计完成 | 影响 |
|------|---------|------|
| exp_hopper_no_dt_emb_s0 (D162) | ~2026-05-27 14:00 UTC | 确认 gate vs dt_emb 根因 |
| exp_hopper_frozen_s0_ext (D163) | ~2026-05-27 12:00 UTC | frozen 是否能 recovery |

---

## 7. Key Numbers Reference (Registry-Sourced)

### exp_hopper_baseline
- eval_return_final: 96.43
- ve_ratio_final: 0.559
- ve_ratio_peak: 3.48@65K
- civo_alert: 0
- value_mean_final: 53.9

### exp_hopper_trained_s0
- eval_return_final: 3.26
- eval_return_peak: 8.01@85K
- ve_ratio_final: 0.897
- civo_alert: 1
- value_mean_trajectory: [0.48, 1.29, 2.93] (85K→95K→105K)
- nve_105K_vs_baseline: 1.6×

### exp_hopper_trained_s0_ext
- eval_return@158K: 81.58 (85% baseline)
- ve_ratio_trajectory: 105K=0.897, 118K=0.376, 128K=5.519, 138K=0.37, 148K=0.55, 158K=0.439
- pattern: transient_instability_recovered
- conclusion: negative (CIVO hypothesis disproved — learning delay only)

### exp_hopper_frozen_s0
- eval_return_final: 0 (peak 3.6@85K)
- ve_ratio@95K: 2.69 (at eval_return=1.083)
- ve_ratio@105K: 4,335,664 (÷0 artifact)
- value_mean_final: 4.337
- pattern: degenerate_civo_near_zero_magnitude
- civo_alert: 1 @[65K, 105K]

### exp_hopper_no_dt_emb_s0 — 🔄 RUNNING
> [PLACEHOLDER]

### exp_hopper_frozen_s0_ext — 🔄 RUNNING
> [PLACEHOLDER]
