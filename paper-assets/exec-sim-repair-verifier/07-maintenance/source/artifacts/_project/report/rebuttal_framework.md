# Rebuttal Framework — Pre-Submission Attack Surface Analysis

Date: 2026-05-20 | Venue: EMNLP 2026 ARR

---

## Attack #1: CWM ≤8B LoRA ≠ Real 32B CWM

### Reviewer 可能措辞

> "The CWM baseline is a ≤8B LoRA fine-tuned model, not the original 32B Code World Model with execution trace mid-training. The comparison is unfair—CWM was designed to operate at much larger scale with specialized pretraining. The paper's conclusion that 'generation degrades at repo level' may simply reflect insufficient model capacity rather than a fundamental formulation limitation."

### 回应要点

**核心论点：matched comparison at controlled capacity isolates formulation effect from scale confounds, which is complementary to—not competing with—scaling studies.**

1. **Function-level 证明 LoRA 可以成功适配 CWM formulation。** CLS 和 CWM 在 function-level 达到统计等价（TOST p=0.007, 5 seeds, ±2pp margin），证明同一 LoRA 配置下 CWM formulation 能完全发挥作用。退化仅在 repo-level 出现，不是 LoRA 容量不足的全局问题。

2. **退化模式指向 formulation 本身，而非容量瓶颈——四种标准干预全部失败。**
   - Format collapse (53–74% unparseable outputs) 是输出空间复杂度问题：function-level 输出为短字符串（integers, booleans），repo-level 输出为无约束执行轨迹（均值 ~477 tokens），错误呈乘性积累
   - 即使在可解析输出中，accuracy (38–43%) 仍低于 majority baseline (72.96%)，表明存在超越格式合规的语义鸿沟
   - **LoRA rank-32 ablation（双倍参数）：无改善（−0.51pp）**，排除 adapter 容量瓶颈
   - **Majority voting K=3：accuracy 反降 0.68pp**（87.51→86.83%），93.3% 样本三次一致，errors 是系统性偏差非随机噪声
   - **Relaxed matching（放宽格式要求）：accuracy 反降 1.06pp**（58.04→56.98%），因为 unparseable 默认为 majority class 比模型自身预测更准
   - **Model scaling 4B→8B：parseable-only accuracy 反降**（42.88→38.52%），表面 accuracy 提升完全是 default-assignment artifact
   - Matched-context ablation：输入差异仅解释 <3% 的 gap
   
   **每种干预分别靶向不同的替代解释（容量不足 / 随机噪声 / 解析严格 / 模型规模），全部失败。这构成 formulation-level bottleneck 的最强证据链。**

   **Convergent null results summary (rebuttal 可直接引用):**
   > "Four convergent null results strengthen this argument: (1) doubling model size yields +0.16pp (flat); (2) majority voting K=3 decreases accuracy by 0.69pp, confirming errors are systematic; (3) forced parsing rescues 90.6% of unparseable outputs but accuracy remains below majority baseline (49.4% vs 72.96%); (4) at repo level, scaling from 4B to 8B worsens parseable-only accuracy (42.88→38.52%) while increasing format collapse (54→74%). These collectively rule out adapter capacity, model capacity, inference stochasticity, and format compliance as explanations, localizing the bottleneck to the generation formulation's output space complexity."

3. **我们的贡献是 formulation comparison methodology，不是 CWM SOTA。** 本文的价值在于提供首个 matched experimental framework 来隔离 formulation effects。32B CWM 在更大规模上可能表现不同（我们在 Limitations 中明确承认），但 matched comparison 是理解 formulation dynamics 的必要第一步。

4. **CLS 过拟合鲁棒性（formulation-level 差异）。** CLS 和 CWM 在相同训练配置下表现出截然不同的过拟合行为：
   - CLS: eval_loss 涨 123%，但 accuracy 仅下降 0.1pp → classification formulation 对过拟合天然鲁棒
   - CWM: eval_loss 上升后 accuracy 下降 5.36pp (epoch 2→3) → generation formulation 更敏感
   - 即使 oracle early stopping (epoch 1 = 75.45%)，CWM 仍 ~7pp below CLS 且 66% unparseable
   - 结论：这是 formulation-level 的固有差异，不是 training-level 的超参问题

   数据来源：
   - CLS: registry cls8b-s42 系列
   - CWM epoch 2→3: deepseek-cwm-repo-s42 (66.85% → 61.49%, -5.36pp)
   - CWM epoch 1: deepseek-cwm-repo-s123-eval-1epoch (75.45%, unparseable 66.4%)

5. **预备回应："execution trace mid-training 可能改变结果"**

   如果 reviewer 追问 "execution trace pretraining is an integral part of CWM, without it your comparison is incomplete"：

   > "Function-level equivalence demonstrates LoRA successfully adapts both formulations (TOST p=0.007). The degradation is complexity-conditional, not LoRA-global. Execution trace mid-training may improve CWM's long-output generation capacity, but this represents an orthogonal training paradigm—not a formulation change. Our contribution is isolating the formulation dimension; scaling and pretraining dimensions require separate matched studies."

   此论点将 execution trace pretraining 重新定位为 **training paradigm** 而非 **formulation property**——reviewer 如果坚持这是 formulation 的一部分，则需要论证为什么 CLS 和 TRAJ 不需要类似 pretraining 来"公平比较"。

### 支撑证据

| Evidence | Location |
|----------|----------|
| TOST equivalence at function-level | §4.2, Table 1 |
| Format collapse rates 53–74% | §4.3, Table 4 |
| Parseable-only accuracy 38–43% < majority 72.96% | §4.3, Appendix C |
| Rank-32 ablation −0.51pp | Appendix B |
| Majority voting K=3 −0.68pp | Appendix (g) |
| Relaxed matching −1.06pp | Appendix (c) |
| Model scaling 4B→8B parseable acc ↓ | §4.3 |
| Matched-context ablation <3% | Appendix B |
| Output token ratio 1:477 (CLS:CWM) | §4.4 |
| Four failed interventions summary | §4.4, Appendix (g) |
| Limitation acknowledged | Limitations, §4.5 |

### 如果 CWM multi-seed + 14B pilot 数据到齐（增补版）

> "We additionally provide multi-seed CWM results (N seeds) confirming the single-seed findings: [具体数据]. A 14B pilot [如果跑了] shows [结果], suggesting that [scaling 趋势]."

此段可在 camera-ready 或 rebuttal 中按实际数据填入。

---

## Attack #2: Repo-Level 单 Seed → 统计力不足

### Reviewer 可能措辞

> "The repo-level results rely on a single seed for most comparisons. With n=48 variant-level instances, the 19–26pp gap could be an artifact of seed variance. The authors themselves note 'single-seed design and multiple confounds limit causal attribution.' Without multi-seed replication, these results are suggestive at best."

### 补充统计数据（M027 修正后）

| Metric | 修正前 | 修正后 | 备注 |
|--------|--------|--------|------|
| Cohen's d (CLS vs TRAJ, Qwen) | 5.015 | **4.590** | 仍为 very large (>0.8 threshold) |
| Statistical power (Qwen) | 0.940 | **0.914** | 仍 >0.80 sufficient threshold |
| Qwen CLS mean | 85.11 | **84.83** | — |

修正原因：Qwen CLS s42 和 TRAJ s42 值与 D159 决策对齐。

### 回应要点（当前版本：数据到齐前）

**核心论点：variant-level 是单 seed，但 per-test interaction effect 基于 n=56,480 observations 且统计上不可争议。**

1. **区分两层证据。** Formulation×complexity interaction 在 per-test level 已经 statistically confirmed：
   - Cross-complexity LPM：z=−23.7, p<0.001, n=56,480, 139 problem clusters (DeepSeek-Coder)
   - Cross-model LPM：CWM deficit −22pp, z=−64.4, p<0.001
   - Formulation 解释 >95% of predictable variance
   - 这不是 "suggestive evidence"，而是 overwhelming statistical evidence for the interaction

2. **Cross-model 方向一致性。** Qwen3 和 DeepSeek-Coder 两个架构不同的模型家族展现相同方向（CLS > CWM），model identity 仅调节 gap magnitude (+1.6pp interaction, z=2.8) 而不改变方向。

3. **Gap magnitude 超过所有已评估 confounds。** §4.5 逐一评估 5 个潜在混淆因素，19–26pp gap 超过任何单个 confound（checkpoint <1pp, seq_length ~1.5pp, preprocessing ~8pp cross-config variance）。即使 confounds 相关，gap 的量级提供 substantial margin。

4. **Holm-Bonferroni 控制 FWER。** 两个核心 claim 在校正后仍然 significant（adjusted p=0.012 and p=0.021）。

5. **Variant-level power 分析。** 即使在 variant-level (n=48)，MDE (minimum detectable effect) ≈ 25pp（two-sided, α=0.05, power=0.8, McNemar's test）。观测到的 CLS–CWM gap 为 29–35pp（视配置），超过 MDE。也就是说：即使在 n=48 的严苛条件下，观测 gap 仍足够大以被统计检测到。这不是 underpowered——是 gap 太大了。

### 回应要点（增补版：CWM multi-seed 数据到齐后）

> "We have completed multi-seed CWM replication. The [N]-seed mean CWM accuracy is [X]% ± [Y]%, confirming the single-seed finding. The CLS–CWM gap at repo level is [Z]pp (p=[value], [N] seeds), consistent with the per-test interaction effect (z=−23.7). This addresses the reviewer's concern about seed-specific artifacts."

如果 multi-seed 方差大于预期：
> "The multi-seed variance is [较大], but the gap remains directionally consistent across all seeds. The per-test interaction (z=−23.7, n=56,480) remains the primary evidence for complexity-dependent divergence; variant-level accuracy provides a practical summary statistic."

### 支撑证据

| Evidence | Location |
|----------|----------|
| Per-test LPM z=−23.7, n=56,480 | §4.3 |
| Cross-model z=−64.4 | §4.3 |
| Formulation explains >95% variance | §4.3 |
| 5 confounds assessed | §4.5, Appendix F |
| Holm-Bonferroni adjusted p | §4.5, Table 5 |
| Cross-model consistency | §4.3 |

---

## Attack #3: 合成突变 vs 真实 Bug

### Reviewer 可能措辞

> "The training data is synthetically generated via mutation operators, not real developer bugs. SWE-bench uses real GitHub issues, but the training-side synthetic distribution may not transfer. The paper's findings about formulation divergence could be an artifact of the synthetic data distribution rather than a genuine property of the verification task."

### 回应要点

**核心论点：our core finding concerns relative ordering, not absolute accuracy—relative rankings are expected to be preserved under uniform distributional shifts.**

1. **Mutation testing 文献的 established validity。** Andrews et al. (2005) 和 Just et al. (2014) 建立了 mutants 作为真实 faults 的 reasonable proxies 在 test effectiveness 研究中的有效性。我们的 mutation operators (operator_swap, off_by_one, return_value, boundary_removal) 覆盖 PMT 文献中的标准突变类型。

2. **Coupling effect 支持 relative ranking validity。** Mutation testing 的 coupling effect 表明：能检测简单突变的 verifier 也倾向于检测复杂真实 bug。这意味着：
   - Domain shift 从 synthetic mutations 到 real bugs 可能影响 absolute accuracy levels
   - 但 relative performance ordering（即 "formulation choice matters at repo level but not function level"）预期在均匀 distributional shift 下保持不变
   - 除非某个 formulation 对 synthetic mutations 有 specific bias（没有理论或实证根据）

3. **Evaluation-side 已包含真实数据。** Repo-level evaluation 使用 SWE-bench Verified（来自真实 GitHub issues 和 pull requests），不是 synthetic data。Function-level 使用 HumanEval/MBPP mutants，但 function-level 结果（near-equivalence）恰恰是我们的 positive finding——即使这受 synthetic bias 影响，也只会低估 formulation difference（如果真实 bugs 更难，divergence 可能更大）。

4. **Gold parse rate 反直觉证据。** Gold mutations（未修改代码，所有测试通过）是 CWM 最简单的目标——模型只需生成"全部通过"的输出。但 gold 的 parse rate 在 8B 仅 23.9%（最差），parseable-only accuracy 仅 16.5%。这直接反驳 "failure comes from mutation difficulty" 的解释：最简单的任务反而最差，说明失败源于输出空间复杂度本身，而非 mutation-specific 难度。

5. **回应 "uniform shift" 质疑的 3 条 counter：**
   - **Counter 1 (directionality):** 如果 synthetic bias 导致了 formulation divergence，我们预期 bias 在 function-level 和 repo-level 一致。但 function-level 观察到 equivalence，repo-level 观察到 divergence。一个 uniform bias 无法同时解释 equivalence 和 divergence。
   - **Counter 2 (mechanism):** CWM 退化的直接机制是 format collapse (53–74% unparseable) 和 long-output generation failure (mean ~477 tokens)。这些是模型能力的物理限制，与训练数据分布无关——无论用 synthetic 还是 real bugs 训练，477-token output 的生成难度不变。
   - **Counter 3 (conservative direction):** 如果 real bugs 比 synthetic mutations 更难（合理假设），那么 CWM 的 repo-level 退化只会更严重——我们的 synthetic 实验给出了 divergence 的 **下界**。

6. **Acknowledging the gap。** 我们在 Limitations 中明确承认："the synthetic-to-real transfer gap for absolute accuracy remains untested." 这是诚实的 scope limitation，不削弱 relative ranking finding。

### 支撑证据

| Evidence | Location |
|----------|----------|
| Andrews & Just citations | Limitations |
| Coupling effect → relative ranking argument | Limitations, Appendix G |
| SWE-bench Verified (real GitHub issues) | §4.1 |
| HumanEval/MBPP mutation operators | §4.1, Appendix D |
| 5 mutation types listed | Appendix D |
| Gold parse rate 23.9% (worst among all types) | Appendix C, Table cwm_mutation_parse |
| Gold parseable-only accuracy 16.5% | Appendix C |
| Limitations acknowledgment | Limitations |

---

## 交叉防御：多个攻击面的组合回应

如果 reviewer 同时提出多个攻击面，统一回应模板：

> "We appreciate the reviewer's thorough engagement with our experimental design. We address each concern below, and note a unifying theme: our contribution is primarily **methodological**—providing the first matched experimental framework for comparing verification formulations. The per-test interaction effect (z=−23.7, n=56,480) is statistically robust regardless of (1) model scale, since it isolates formulation effects at controlled capacity; (2) seed count, since it is based on >56K observations with 139 problem-level clusters, not variant-level aggregates; and (3) training data source, since the interaction concerns relative ordering across formulations that share the same training distribution."

---

## Q2 预备：Re-repair Negative + Oracle Ensemble

### Reviewer 可能追问

> "The re-repair pilot found no benefit (p=0.42). Doesn't this undermine the practical value of per-test diagnostics, which is one of CLS's main advantages over TRAJ?"

### 回应要点

1. **Statistical power 不足以检测 medium effect。** n=44 instances, power ≈ 0.3 for medium effect size (Cohen's h=0.3)。p=0.42 是 inconclusive, not evidence of absence。需要 n≈200 才能 power=0.8。

2. **Oracle ensemble ceiling 证明 formulation diversity 有实际价值。** 即使 re-repair 未证明直接 downstream benefit：
   - Function-level oracle ensemble: 90.63% (+2.80pp over best single)
   - Repo-level oracle routing: 95.83% variant accuracy (+14.58pp over best single, n=48)
   - 95.83% 意味着：如果有一个 perfect router，只需从已有 formulations 中选择，就可以 resolve 95.83% 的 variants
   - 这是 "formulation design space worth exploring" 的最直接证据

3. **Per-test diagnostics 的价值不仅限于 re-repair。** CLS 的 per-test granularity 还支持：
   - Failure localization（哪些测试失败）
   - Confidence estimation（多少测试通过 / 总测试数）
   - Selective re-execution（只重跑可疑测试）
   - 这些 downstream applications 未被 re-repair pilot 覆盖

4. **诚实承认 limitation。** 论文已在 Limitations 中明确标注 re-repair negative + insufficient power。这是透明的科学报告，不是 weakness——reviewer 如果因此降分，可以在 rebuttal 中指出这恰恰是 rigorous self-assessment。

---

## 状态标注

| 攻击面 | 当前防御强度 | 数据到齐后 |
|--------|------------|----------|
| #1 CWM scale | ★★★★ (4 convergent nulls + exec trace reframing + methodology argument) | ★★★★+ if 14B pilot confirms |
| #2 Single seed | ★★★★ (per-test LPM overwhelming + MDE analysis + variant gap > MDE) | ★★★★+ with multi-seed CWM |
| #3 Synthetic data | ★★★☆ (coupling effect + gold parse rate counter + 3 uniform-shift counters) | 不变（需要 real-bug training data 才能完全 close，超出 scope） |
| Q2 Re-repair | ★★★☆ (power analysis + oracle ceiling + broader diagnostic utility) | 需要 n≈200 re-repair 才能 close |

---

## 储备/待用

以下素材已有数据支撑或数据部分就绪，reviewer 问到时可快速出图或展开论述。

### Checkpoint Selection Sensitivity（储备，reviewer 问时出图）

28 个 val/test checkpoint sweep 数据点已存在 registry，覆盖：
- CLS 8B: ckpt-1000 到 ckpt-6400，多个 seq_length
- CLS 4B: ckpt-800 到 ckpt-4600
- 跨 checkpoint 的 accuracy 波动 <1pp（例：s42 三个 ckpt = 85.34/84.48/85.29）

Reviewer 如果质疑 checkpoint selection bias，可在 rebuttal 期间 <1h 画出 sensitivity 图。

### CWM Epoch-wise Accuracy Curve（储备，等数据到齐后画）

已有数据点：
- s42: epoch 2 = 66.85% (partial coverage 31.2%), epoch 3 = 61.49%
- s123-v2: epoch 1 = 75.45% (checkpoint-4209)
- s456-v2: 训练中，epoch 2 eval_loss = 4.727

完整 multi-seed epoch 曲线需要：
- s123-v3 和 s456-v2 完成 3-epoch 训练后的 final accuracy
- 各 seed 的 epoch 1/2 checkpoint eval（如果 checkpoint 保留了的话）

用途：证明 CWM 在 repo-level 随训练推进而退化，支撑 "CWM generation + long traces = fundamental mismatch" 的论点。
