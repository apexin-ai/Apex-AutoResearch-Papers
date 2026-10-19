# Rebuttal Framework — R22 后续挑战应对

> 基于 R22 审稿（2026-05-20, Overall 3.0 Findings）的 5 个 Critical 和 8 个 Should-Fix 问题，
> 以及已完成的修订（abstract 压缩、8-page 合规、参考文献补充、doubly conditional 前置）。

---

## 核心论点 1: N1 — HB Correction Scope / Search Space

### 审稿人攻击角度

- "你们做了 ~980–2,240 configs/model 的搜索（5 metrics × 7 windows × 28–64 layers），但 HB 只覆盖最终 12 个 tests，自相矛盾——你们自己论文的主题就是 researcher degrees of freedom"
- "Nested CV / split-half 只在 7–8B 做了，32B（n=19–20，最脆弱）恰恰没有这个保护"
- "为什么不用 permutation-based FWER 或 BH-FDR？"

### 我们的回应

**核心论证**：HB 12-test 是 **final inference** 的 correction；upstream 搜索的 multiplicity 由 **独立验证机制** 覆盖，而非需要扩大 HB 范围。

1. **Two-stage design 分离搜索与推断**：Layer/W/metric 选择在 validation set 上完成；final HS-vs-text comparison 在 held-out test set 上执行。这是标准的 train-val-test protocol，upstream 搜索不需要被 HB 覆盖——正如 hyperparameter tuning 不需要 Bonferroni 校正 final test accuracy。
   - **引用**: §3.3 protocol description; App H (hyperparameter robustness)

2. **BA-layer 独立验证 (16/16 HB pass)**：所有 4 个模型 × 4 个 threshold-based metrics 独立收敛到相同深层区域（Tab 1），而 BA 独立选择的 layers 也全部通过 HB（App S, tab:ba_layer_results: 16/16 model-metric-split configurations pass）。如果 deep-layer 选择是 overfitting，不同 metrics 不会独立收敛。
   - **引用**: Tab 1 (tab:layer_selection); App S (tab:ba_layer_results)

3. **搜索空间已量化**：我们在 Limitations §9 para 3 中显式量化了搜索空间（"up to 2,240 configurations"）。这恰恰是 methodological contribution——我们是**唯一**在 probing 论文中量化 upstream DoF 的工作。
   - **引用**: §9 para 3 (sec:limitations)

4. **32B 保护措施**：
   - Exact sign-flip permutation tests (2^19 / 2^20 enumerations) — all 6 tests reject at α=0.05 (App D, tab:holm_bonferroni note)
   - Power analysis 显示 MDE=8.6–9.5pp，观测效应 +15.4–19.2pp 超过 MDE (App Y)
   - 但我们主动将 32B 标记为 exploratory (†)，abstract 中已标注

5. **如果审稿人坚持 permutation-based FWER**：可在 rebuttal 期间对 32B 运行 max-T permutation test（对 layer × W 的 joint 搜索空间做 permutation），预期仍 pass（因为 deep-layer signal 是 real-label specific，random-label control 已证明）。

### 证据强度：**Strong**
- 理由：two-stage protocol 是标准做法；BA-layer 独立验证提供 robustness；搜索空间显式量化在同类论文中独一无二。
- 风险：审稿人可能认为 val set 太小（n=4–9 per-class at 32B），validation 选择本身不够稳定。应对：引用 LOO-CV stability (App A) 和 multi-seed stability (App R)。

---

## 核心论点 2: N2/N4 — Position Confound + Encoder Quality ("Doubly Conditional")

### 审稿人攻击角度

**N2 (Position)**:
- "Linear residualization 3/4，quadratic 2/4——你们选择性报告了有利的那个"
- "QwQ-32B 的 HS advantage 被 quadratic position 完全吸收，说明 HS probe 可能只是更好的 position encoder"

**N4 (Encoder)**:
- "384d→1024d 就从 4/4 HB 掉到 1/4 HB，如果用 2048d encoder 可能 0/4"
- "HS 'advantage' 本质上是 text encoder 太弱的 artifact"

### 我们的回应

**核心策略**：不回避，而是**将 doubly conditional 本身框架为诚实科学的优势**。

1. **R22 之后已完成的修订**：Abstract 已前置 "doubly conditional" 表述（commit 23e8e5e），明确写入 "4/4 HB at 384d → 1/4 at 1024d" 和 "partially overlaps with temporal position"。这不是 selective reporting，而是**主动量化 boundary conditions**。
   - **引用**: Abstract (revised); §6.2 (sec:32b-analysis)

2. **Position 分析的分层逻辑**：
   - Linear residualization: 3/4 retain significance → HS 包含 beyond-position signal
   - Quadratic: 2/4 retain → QwQ-32B 的 residual 含有 non-linear position component
   - 这不是"有利/不利"的选择，而是**系统性拆解**——Tab position_quadratic 完整呈现两个控制水平
   - **引用**: Tab position_quadratic (App Q); §6.2 lines on quadratic

3. **Encoder 梯度是 informative, not damaging**：
   - PCA capacity matching (384d projection of HS) 保持 significance (+16.8 to +23.1pp) → **信息量**而非维度是关键
   - Random projection baseline (App T, tab:random_projection): 384d random projection of HS 仍大幅优于 384d text (all p<0.001)，证明 HS 优势不来自维度
   - Encoder 梯度恰恰是 **calibrating what "advantage" means**——我们是唯一做这个分析的 probing 论文
   - **引用**: App R (tab:encoder_robustness); App T (tab:random_projection); §6.2

4. **Framing 转换**："The HS advantage is not universal — it is conditional on encoder quality and position control. This conditionality is itself an empirical finding that prior work did not report."
   - 对比：SafeProbing (Zhu et al. 2026) 没有做 encoder sensitivity analysis
   - 对比：Probing Subspaces (arXiv:2503.09066) 没有做 position control

### 证据强度：**Strong**
- 理由：R22 之后 abstract 已修订；doubly conditional 框架是**主动诚实**而非被动让步；PCA/random-projection 控制提供了 text encoder 之外的独立验证。
- 风险：审稿人可能认为 "conditional on so many things = not a real finding"。应对：强调 layer selection bias（Contribution 1）不依赖任何 conditionality，是 unconditional result。

---

## 核心论点 3: N3 — Architecture Diversity / Random-Label Control

### 审稿人攻击角度

- "Random-label control 只在 QwQ-32B 上做，但你 claim 'architecture-independent'——R1-8B (Llama) 没验证"
- "4 个模型有 3 个是 Qwen family，实际上只测了 2 个 architecture"

### 我们的回应

1. **4/4 模型 crossing rate → shallow 选择**：CR→shallow bias 在所有 4 个模型上一致观察到（Tab 1）：
   - R1-8B (Llama): L0 (0%)
   - OT-7B (Qwen-7B): L0 (0%)
   - QwQ-32B (Qwen-32B): L2 (3%)
   - R1-32B (Qwen-32B): L10 (16%)
   
   **包括 Llama 架构的 R1-8B**。Phenomenological consistency across architectures 是 observation-level 的 evidence，不需要 random-label control 来确认。
   - **引用**: Tab 1 (tab:layer_selection)

2. **Random-label control 在 QwQ-32B 上验证了 mechanism**：
   - 100% of random-label repeats still select L0–L7 for crossing rate
   - 这证明 bias 来自 **representation geometry**（cosine compression），不来自 safety labels
   - Cosine volatility analysis 在 **R1-8B 上也做了** (App B, fig:cosine_volatility)，确认 shallow-layer compression 是跨架构的
   - **引用**: App A §Random-Label (tab:random_cp); App B (app:cosine_volatility)

3. **Cosine distance compression + R1-8B full-layer sweep**：
   - R1-8B full-layer sweep (L0–L24) 显示 crossing rate 在所有 4 个 window sizes 选择 L0，threshold-based metrics 选 L9–L16 (Tab r1_8b_full_layer)
   - 这与 QwQ-32B pattern 完全一致，只是层数不同
   - **引用**: App A (tab:r18b_full_layer)

4. **如果审稿人坚持要 R1-8B random-label control**：可在 rebuttal 期间运行（computational cost 极低：25 layers × 10 random seeds × 5 metrics ≈ 几分钟 CPU time）。预期结果：crossing rate 100% select L0–L3，与 QwQ-32B 一致。

### 证据强度：**Moderate → Strong (if R1-8B control added)**
- 理由：Phenomenological evidence (4/4 models) + mechanistic verification (1/1 model) + cosine analysis (2/2 models) 构成 converging evidence；但 random-label 确实只有 1 个模型。
- 风险：审稿人可能说 "你应该做了再投，不是 rebuttal 补"。应对：我们可以在 camera-ready 前完成，且预期结果与 existing evidence 一致（cosine compression pattern 已在 R1-8B 确认）。
- **建议：rebuttal 期间主动补做 R1-8B random-label control**。

---

## 核心论点 4: Significance Defense — Layer Selection Bias 的社区影响

### 审稿人攻击角度

- "Layer selection sensitivity 不新鲜——Belinkov (2022), Hewitt & Liang (2019) 早就说过 probing 方法论有问题"
- "这只是已知问题在 safety domain 的又一个 instantiation"
- "Excitement 2.5/5——为什么社区应该关心？"

### 我们的回应

1. **Methodological artifact 的实际影响**：
   - 我们的论文不是 "probing 有问题" 的泛泛警告——我们**具体量化了** metric 选择如何 **逆转结论**
   - Tab 1: CR-composite layers → 32B HS advantage non-significant; threshold-based layers → all 4 models significant
   - 这不是 "performance varies by layer"（everybody knows），而是 "metric choice determines whether you publish a positive or negative result"
   - **引用**: Tab 1; §6.1 (sec:layer-results)

2. **其他论文可能在报告 methodological artifact**：
   - SafeProbing (Zhu et al. 2026) 用单一 metric 选 layer，没有 multi-metric audit
   - 如果他们碰巧用了 crossing-rate-like metric，他们的 negative results at scale 可能是 artifact
   - 这直接影响社区对 "HS probes don't scale" 的共识
   - **引用**: Related Work discussion of SafeProbing; §7 (discussion)

3. **Geometric mechanism 是 novel**：
   - Crossing-rate bias 的根因是 cosine distance compression at shallow layers（App B）
   - Random-label control 证明这是 label-independent geometric property
   - 这不是 Belinkov (2022) 或 Hewitt & Liang (2019) 讨论的 "capacity vs. selectivity" 问题——是一个新的 failure mode specific to temporal probing
   - **引用**: App A (tab:random_cp); App B (app:cosine_volatility)

4. **Actionable output**：5-metric audit protocol + 3-layer ensemble（Tab ensemble, all p ≤ 0.002）提供了**具体的解决方案**，不仅仅是 "be careful"。
   - **引用**: §7 (audit protocol); Tab ensemble

### 证据强度：**Strong**
- 理由：quantified impact（结论逆转）+ novel mechanism（cosine compression）+ actionable solution（audit protocol + ensemble）
- 风险：R2 认为这是 "known problem, new domain"。应对：承认 meta-level message 与 probing literature 一致，但 crossing-rate geometric mechanism 和 conclusion-reversal quantification 是新贡献。

---

## Limitations 位置索引

| Limitation | 位置 | 引用 |
|-----------|------|------|
| Single dataset (HarmThoughts only) | §9 para 1 | sec:limitations |
| No category stratification | §9 para 1 | sec:limitations |
| No IAA for CP annotations | §9 para 1 | sec:limitations; also App I (AdvBench IAA κ=0.606) |
| R1-32B: significance only at W=1, 25% coverage | §9 para 2 | sec:limitations |
| R1-32B: position mediation (+1.9pp, p=0.914) | §9 para 2 | sec:limitations; App Q (app:position_residual) |
| QwQ-32B: position baseline higher BA (0.832 vs 0.796) | §9 para 2 | sec:limitations |
| QwQ-32B: negative HS lead time | §9 para 2 | sec:limitations; Tab 3 (tab:32b_divergence) |
| R1-8B FPR seed-fragile (3/5 HB) | §9 para 2 | sec:limitations; App R (app:multi_seed) |
| 32B MDE = 8.6–9.5pp (n=19–20) | §9 para 2 | sec:limitations; App Y (app:power_analysis) |
| HB covers 12 final tests, not upstream search | §9 para 3 | sec:limitations; App H (app:hyperparameter_robustness) |
| Up to 2,240 config search space | §9 para 3 | sec:limitations |
| BA-layer split-sensitive (7–98% depth) | §9 para 3 | sec:limitations; App S (app:ba_layer_comparison) |
| K=5 fixed from R1-8B, not model-specific | §9 para 3 | sec:limitations; App F (app:k_ablation) |
| Joint (layer, W) stability: QwQ only, not R1-32B | §9 para 3 | sec:limitations; App A (app:layer_sweep) |
| 3/4 models Qwen family | §9 para 3 | sec:limitations |
| Correlational, no causal intervention | §9 para 3 | sec:limitations; §7 (discussion DAS/ITI/CB) |
| Cross-model transfer: PCA only, no Procrustes/CKA | §9 para 3 | sec:limitations; App P (app:transfer_details) |
| CP permanence assumption (oscillating traces) | §9 para 4 | sec:limitations |
| Encoder quality conditions HS advantage | §6.2 | sec:32b-analysis; App R (app:encoder_robustness) |
| Position overlap: 3/4 linear, 2/4 quadratic | §6.2 | sec:32b-analysis; App Q (tab:position_quadratic) |
| FPR 11–50% (not production-ready) | §9 para 2 | sec:limitations |
| Oracle gap 76.7% (R1-8B) | §9 para 2 | sec:limitations; App E (sec:oracle) |
| AdvBench geometric validation only (no CP) | §9 para 1 | sec:limitations; App B (app:cosine_volatility) |

---

## Reviewer Questions 快速回应

| Q# | 问题 | 回应方向 | 引用 |
|----|------|---------|------|
| Q1 | 32B false discovery risk beyond HB? | Exact permutation tests already done (2^19/2^20); can add max-T permutation in rebuttal | App D |
| Q2 | QwQ quadratic: HS = nonlinear position? | Partially yes — honest admission; residualized signal still above chance (p<0.001) | App Q; §6.2 |
| Q3 | CR weight in composite → layer flip? | Yes, by design — this is exactly the layer selection sensitivity we document | Tab 1; §6.1 |
| Q4 | K=5 appropriate for all models? | Acknowledged limitation; K ablation shows K=3–7 stable for R1-8B; model-specific tuning is future work | App F |
| Q5 | HarmThoughts CP annotation source/IAA? | Manual inspection by benchmark authors; no IAA; AdvBench LLM IAA κ=0.606 | §9; App I |
| Q6 | Stronger encoders than BGE-1024d? | E5-Mistral (App U) tested; PCA capacity matching preserves significance | App U; App R |
| Q7 | Layer sensitivity by category? | Not stratified; acknowledged limitation; sample size per category too small | §9 para 1 |

---

## Additional Attack Angles

### A1: Crossing-rate strawman

**攻击**："你们用 CR-composite 作为对比基线，但没有人真正用这个 metric 选层，这是在打稻草人。"

**回应**：

1. **CR 逻辑渗透在 change-point 类方法中**：Crossing rate 度量的是 probe prediction 跨越 decision boundary 的频率——这与 BOCPD~\citep{adams2007bayesian} 和 CUSUM~\citep{page1954cusum} 的核心逻辑（检测 state transition frequency）同构。虽然没有论文明确使用 BA×CR 作为 layer selection metric，但只要 layer sweep 隐式偏好 "transition-rich" layers（e.g., selecting by change-point density），就等价于引入了 crossing-rate bias。
   - **引用**: §6.1 (sec:layer-results); Tab negative (BOCPD/CUSUM failures)

2. **Composite metric 形式在 AutoML 中常见**：BA×CR 的乘积形式遵循 multi-objective optimization 的标准做法（accuracy × diversity in ensemble selection; precision × recall = F-score 的乘积结构）。如果一个 reviewer 在 layer sweep 中同时考虑 probe quality 和 temporal dynamics，这种 composite 是自然选择。

3. **Strawman 批评恰恰反转为 contribution**：即使 CR-composite 从未被显式使用过，我们的发现是：**任何** 含有 cosine-compression-sensitive 成分的 composite metric 都可能产生浅层偏差。这是一类 failure mode 的 characterization，不是对特定 metric 的批评。Cosine volatility ratio 1.4–2.7× (App B) 表明浅层 compression 是 transformer 的固有几何属性。
   - **引用**: App B (app:cosine_volatility); App A §Random-Label (tab:random_cp)

**证据强度**: **Strong** — 即使接受 "没人用" 的前提，mechanism characterization 本身仍有价值。最坏情况下是 "contribution about a potential pitfall" 而非 "debunking existing practice"。

---

### A2: Retrospective vs prospective gap

**攻击**："你们做的是 retrospective classification，但 title/framing 暗示对 online detection 有实用价值。Retrospective probe 的结论能迁移到 online setting 吗？"

**回应**：

1. **明确声明已前置**：Abstract 第二句 "provide initial characterization"；Intro 最后一段 "retrospective classification—not online detection"；Conclusion "false alarm rates remain 11–50%, so current methods characterize the phenomenon rather than constitute production detectors"。Framing 从未 claim online 可用性。
   - **引用**: Abstract; §1 (sec:introduction); §8 (sec:conclusion)

2. **Limitations 专门讨论了 online gap**：§9 para 2 明确写 "FPR 11–50%"；§7 讨论了 deployment operating points (App deployment_operating_points) 并建议 "causal validation via DAS/ITI/circuit breakers" 作为 prospective 方向。
   - **引用**: §9 (sec:limitations); §7 (sec:discussion); App (app:deployment_operating_points)

3. **Retrospective 工具在 safety 领域有独立价值**：
   - **Post-hoc audit**: 部署后审查 model outputs，识别 self-jailbreak 模式
   - **Model selection**: 比较不同 reasoning models 的 safety commitment 深度
   - **Red-teaming**: 理解 model 内部何时 commit to harmful generation，指导 adversarial evaluation
   - 这与医学影像的 retrospective study → prospective trial 的标准研究路径一致

4. **Prior work 同样是 retrospective**：TrajGuard~\citep{trajguard} 和 SafeSwitch~\citep{safeswitch} 的评估也是在已知 adversarial inputs 上做 retrospective classification，然后声称 detection 能力。我们的设定不比 prior work 更 prospective。
   - **引用**: §2 (Related Work); Tab negative

**证据强度**: **Strong** — 多处显式声明 retrospective；retrospective 工具有独立应用场景；prior work 也是 retrospective 评估。

---

### A3: CP annotation IAA weakness

**攻击**："Commitment Point 标注没有 inter-annotator agreement 报告，你们怎么知道标注一致？"

**回应**：

1. **使用 published benchmark 的原始标注**：CP annotations 来自 HarmThoughts~\citep{harmthoughts}，已通过同行评审。我们未引入额外的人工标注，减少了 annotation pipeline 的不确定性。
   - **引用**: §4.1 (sec:setup); Tab models (tab:models)

2. **CP 定义降低了主观性**：我们定义 CP 为 "the first reasoning step after which safety deliberation permanently ceases"（§1）。这是基于 observable text pattern 的 deterministic rule——判断标准是安全相关 deliberation 是否在后续 step 中**永久消失**，而非主观评估内容的 harmfulness 程度。相比 toxicity rating（连续 scale），binary transition point 的 annotator 分歧空间更小。
   - **引用**: §1 (CP definition); §9 para 4 (CP permanence assumption)

3. **AdvBench 辅助验证提供了 IAA 参考**：App I 报告了 LLM-based annotation 的 Cohen's κ = 0.606 (moderate agreement)。虽然这是 AdvBench 而非 HarmThoughts，且是 LLM-human 而非 human-human IAA，但它为 CP-type annotation 的 reliability 提供了 proxy evidence。
   - **引用**: App I (AdvBench IAA)

4. **已承认并指出改进方向**：§9 para 1 承认 "no IAA for CP annotations"；§9 para 4 讨论了 CP permanence assumption 的局限（oscillating traces）。未来工作应引入多标注者 + Cohen's kappa + 标注指南一致性检验。
   - **引用**: §9 (sec:limitations)

**证据强度**: **Moderate** — 使用 published benchmark 降低了风险；deterministic definition 减少了主观性空间；但确实没有 human-human IAA。这是一个 acknowledged 而非 defended 的 limitation。

---

## 整体 Rebuttal 策略

**定位**：不争取 4.0 (Conference)，目标 3.5 (Borderline Conference) → Findings acceptance。

**核心 narrative**：
1. Layer selection bias 是 **unconditional result**（不依赖 encoder/position/sample size）
2. HS advantage 是 **conditional but honestly characterized**（doubly conditional 已前置到 abstract）
3. 我们不是在 hide weaknesses——我们是**唯一量化这些 boundary conditions 的 probing 论文**
4. 7 个 negative results + M002 bug disclosure = 异常高的 scientific integrity

**Rebuttal 期间可补做的实验**（低成本，几分钟 CPU）：
- [ ] R1-8B random-label control（直接回应 N3）
- [ ] Max-T permutation test for 32B（加强回应 N1，如果审稿人坚持）
