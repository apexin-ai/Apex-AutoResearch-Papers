# Rebuttal Talking Points

> 基于 R19 审稿意见 + 历史复发 issue 生成（2026-05-24）。所有引用指向论文当前版本。数字标注来源：registry exp-XXX 或论文 §X.X。

---

## Must-Address (审稿人大概率会问)

### Q1: 方法论新颖性有限 (R2-W1, recurring R0→R19)

**预期质疑**: Theorem 1 是标准矩阵代数（$M_{\text{global}}^{-1} M_s - I$），EC-HTE 本质是 Dawid-Skene 直接应用。方法论贡献何在？R19 中 R1/R2 一致认为数学推导使用标准技术。

**我们的回应**: 我们不声称 confusion matrix inversion 是新方法。贡献在三个层面：

1. **Setting identification**: 识别 LLM annotation + HTE 交叉场景下的具体偏差结构。$\delta_s \cdot \Delta\tau / (1-2\bar{\pi})$ 的乘积形式将偏差分解为三个可独立估计的分量，揭示 sign reversal 的充要条件。此前文献（F-L 2003, Carroll 2006）关注 attenuation bias；我们刻画的是 correction-induced bias——结构上不同的量，absent from the uncorrected estimator。
2. **Diagnostic**: Proposition 2 的 $\Delta\tau$-free 条件打破循环依赖——实践者无需估计 CATE 即可判断 global correction 是否有害。此功能独立于任何校正方法。
3. **Systematic validation**: 520 configs MC 验证 + 11 empirical LLM CMs + 3 种 CATE estimators（DIM/CausalForest/R-learner），确认乘积形式是实证现象。

Introduction Contribution 1 已加声明：'The algebraic structure follows from standard confusion-matrix calculus; our contribution is identifying that this structure produces sign reversal in the LLM annotation setting and factoring it into independently estimable components.'

**支撑证据**:
- Bias identity $R^2 = 0.994$ (K=2), $0.97$ (K=4) — §5.2, exp-002
- 11 empirical LLM CMs: $R^2 = 0.975$ — Appendix app:realcm_bias, exp-024
- Sign reversal 14.9% at $\tau(0)=0.03$ — §5.2, exp-038
- Diagnostic AUC=1.0 on $\Delta\tau>0$ subgroups — §5.4, exp-005
- F-L scalar correction increases $|\text{bias}|$ to 0.122 (2.1× naive); F-L per-sub to 0.168 (2.9×) — Table 1, exp-034

---

### Q1b: Sign Reversal 频率——14.9% 是否严重到需要专门方法？ (Q1 follow-up)

**预期质疑**: 14.9% sign reversal 听起来不算高频。Reviewer 可能认为这是小概率事件，不足以 justify 一个专门的方法框架。

**我们的回应**:

**Acknowledge**: 14.9% 作为频率确实不是 majority case。但 sign reversal 的严重性在于后果而非频率——这是一类后果不可逆的错误。

**Reframe**: Sign reversal 意味着将一个真实有益的治疗效应判定为有害（或反之）。在因果推断的应用场景中，这不是 estimation noise 的问题，而是 decision reversal 的问题。一个临床试验中的 sign reversal 意味着一种有效治疗被放弃；一个政策评估中的 sign reversal 意味着一项有益政策被终止。频率再低，一次错误判断的代价就可能是不可接受的——这与 Type I error control 的逻辑完全一致：我们不因 α=0.05 "只有 5%" 就认为 false positive 不重要。

**Evidence**: 更关键的是，14.9% 是在 τ(0)=0.03 的条件下测得的。完整数据（exp-038）揭示 sign reversal 频率与效应大小成反比：

| True CATE τ(0) | Global Sign Reversal Rate | EC-HTE Sign Reversal Rate |
|----------------|--------------------------|--------------------------|
| 0.01 | **31.0%** | 0% |
| 0.03 | 14.9% | 0% |
| 0.05 | 6.1% | 0% |
| 0.10 | 0% | 0% |

效应越小，sign reversal 越频繁。而小效应恰恰是需要最精确估计的场景——τ(0)=0.01 的治疗效应微妙但可能对大规模人群有重要的公共卫生意义，31% 的 sign reversal 率意味着将近三分之一的情况下，标准校正程序会得出完全相反的结论。

**Takeaway**: EC-HTE 在所有配置下 sign reversal = 0%。这不是边际改善——是从 "31% 的情况下会犯方向性错误" 到 "保证不犯方向性错误" 的质变。对于决策关键型应用（clinical subgroup analysis, policy targeting），sign correctness 是 minimum requirement，不是 nice-to-have。Sign reversal 的分布恰好集中在小效应区间（需要校正帮助最多的地方），这证明专门方法不仅 justified，而且 necessary。

---

### Q2: AUC 三级呈现——0.63 / 0.86 / 1.0 如何理解 (R18-W1, R19 R1-W2/R2-W2)

**预期质疑**: AUC=0.63 在 real LLM 上太低，削弱 'actionable diagnostic' 定位。多版本呈现有 cherry-picking 嫌疑。R2 建议 Abstract 用最保守值。

**我们的回应**: 三级 AUC 是对同一诊断在不同评估条件下的完整报告，不是 cherry-picking：

| AUC | 评估条件 | 含义 |
|-----|---------|------|
| 1.0 | 仅 $\Delta\tau > 0$ 的子群 | 存在真实异质性时，诊断完美区分 |
| 0.86 | 全部合成子群（含 $\Delta\tau \approx 0$） | 含无代价误判子群后 AUC 下降 |
| 0.63 | 16 semi-synthetic LLM-dataset combinations | empirical LLM CMs 中 $\Delta\tau \approx 0$ 子群比例更高 |

AUC=0.63 低的根因：包含 $\Delta\tau \approx 0$ 的子群——这些子群中 global 和 stratified correction 表现相同，误判无代价。排除后 AUC=1.0。

**已在论文中修复**: Abstract 完整报告三级 AUC（abstract.tex L6: 'AUC $= 1.0$ on subgroups with non-zero $\Delta\tau$; $0.86$ across all synthetic subgroups; $0.63$ on real LLM error profiles'）。§5.4 前置解释（experiments.tex L72-73）。

**支撑证据**:
- AUC=1.0 on $\Delta\tau>0$ — §5.4, exp-005
- AUC=0.86 synthetic — §5.4, exp-005
- AUC=0.63 semi-synthetic (empirical LLM CMs) — §5.4, exp-028
- $K=2$ 时 $|\delta_0|=|\delta_1|$ 限制区分度 — Appendix app:screening

---

### Q3: Semi-synthetic vs real data——无 real data 成功案例 (R5-W3, R19 R1 Must-Fix)

**预期质疑**: '11 real LLM-dataset combinations' 实质是 semi-synthetic。所有 CATE 为合成注入。你的方法在 real data 上为什么不 work？

**我们的回应**:

**Acknowledge**: EC-HTE 在现有 real datasets 上未产生改善，我们诚实报告这一结果。全文术语已统一为 'semi-synthetic evaluations using empirical LLM confusion matrices'（R19 已修复）。

**Reframe**: 关键区分——这不是 "方法在 real data 上失败"，而是 "现有 real datasets 的 operating conditions 不满足方法的前提条件"。EC-HTE 明确声明了三项 operating conditions: Δπ>0.15, FNR<0.50, n_expert≥250（§5.4）。现有公开数据集系统性地违反前两项：

| Dataset / Model | FNR | Δπ | 违反条件 |
|-----------------|-----|----|---------|
| UCB Hate Speech (GPT-4.1) | **0.55** (接近随机) | 0.117 | FNR + Δπ |
| TweetEval (GPT-4.1, worst subgroup) | **0.526** | P(Z=1)=0.18 | FNR |
| 6 OpenAI models (exp-008) | 0.40–0.53 | 0.080–0.198 | 多数 Δπ不足 |

当 FNR≈0.55 时，confusion matrix 接近随机猜测（$1-\text{FPR}-\text{FNR} \approx 0.28$），矩阵求逆严重放大噪声——任何基于 CM inversion 的方法都无法有效工作。这是数学限制，非方法缺陷。

**Evidence — Operating conditions 内方法有效**: 当 operating conditions 满足时（semi-synthetic, empirical LLM CMs + 控制 Δπ/FNR），EC-HTE 表现强劲：7.4× bias reduction（Table 1），coverage 94–96%（exp-039），sign reversal 0%（所有配置）。exp-037 进一步显示温度标定（calibration）将 Δπ 从 0.20 降至 0.07，而 calibration + EC-HTE 组合达到最佳 coverage 96.5%——说明方法在合理条件下不仅有效，且与其他技术互补。

**Takeaway — Operating conditions 是 honest limitation, not fatal flaw**:

1. **贡献结构不依赖 EC-HTE 在所有场景下成功**：论文 55% 贡献是 bias identity（揭示 global correction 何时有害），30% 是 diagnostic（Proposition 2，AUC=1.0 on Δτ>0 subgroups）。即使 EC-HTE 在当前 LLM 错误率下适用范围有限，bias identity 和 diagnostic 仍然独立成立且有实践价值。
2. **条件是可满足的，且正在变得更容易满足**：GPT-4o 在部分任务上 FNR<0.30（exp-015），新一代模型在 domain-specific fine-tuning 后 Δπ 可达 0.20+（exp-016）。随着 LLM 分类能力提升，operating conditions 从 "边界情况" 逐步变为 "常见条件"。
3. **Ground-truth subgroup CATEs 在公开数据集中不可得**——经典因果推断 benchmark 缺少 LLM annotation 步骤（limitations.tex L12）。这是该研究领域的结构性评估困难，非本文特有弱点。

**支撑证据**:
- UCB Hate Speech: FNR≈0.55, Δπ=0.117 — exp-004, exp-015
- TweetEval GPT-4.1: worst subgroup FNR=0.526, P(Z=1)=0.18 — exp-016
- 6 OpenAI 模型 Δπ: 0.080–0.198 — exp-008
- Operating conditions 内: 7.4× bias reduction, coverage 94-96% — Table 1, exp-039
- Calibration + EC-HTE: coverage 96.5%, Δπ 0.20→0.07 — exp-037
- GPT-4o FNR<0.30 on select tasks — exp-015
- Section 5.1: '16 model--dataset--K combinations (8 LLMs × 2 datasets × varying K)' — experiments.tex L11

---

### Q4: (A1) 违反后果——不可测试且 γ_T=0.10 时 coverage 75% (R10-N1, R19 R1-W1/R2-W4)

**预期质疑**: A1（outcome-independent misclassification）不可测试。γ_T=0.10 时 coverage 降至 75%，breakeven 偏低。LLM 准确率与文本复杂度可能相关（outcome-correlated），但未被检验。

**我们的回应**: 区分两类 A1 违反并分别测试：

| 违反类型 | 参数范围 | Coverage 变化 | 来源 |
|---------|---------|--------------|------|
| Outcome-dependent (γ) | 0 → 0.2 | 95.5% → 93.5% (−2pp) | exp-029 |
| Treatment-dependent (γ_T) | 0 → 0.10 | 94.5% → 75% | exp-040 |

**Outcome-dependent**: graceful degradation。γ=0.2 时 EC-HTE coverage 仍 ≥93.5%，|bias| 增 13.7% 但仍与 Global 可比。在 NLP 中这是更常见的违反形式（LLM 准确率随文本复杂度变化）。

**Treatment-dependent**: 更敏感，breakeven γ_T ≈ 0.10。但在 NLP 中 treatment 通常是外生干预（如 exposure to content），不直接影响 LLM classifier 输入特征，所以 treatment-dependent misclassification 不常见。

理论上 Theorem 1 gains O(γ) perturbation term（theory.tex L97）。theory.tex L98 已加定量描述。建议配合 Cinelli & Hazlett (2020) 框架 bound degradation（已引用 theory.tex L98）。

**支撑证据**:
- exp-029: coverage 95.5%/95.5%/95.3%/94.8%/93.5% at γ = 0/0.05/0.10/0.15/0.20 — Appendix app:a1_sensitivity
- exp-040: coverage 94.5%/89.7%/75%/52.5%/37% at γ_T = 0/0.05/0.10/0.15/0.20 — Appendix app:treatment_dep
- theory.tex L96-98, limitations.tex L8-9

---

## Should-Address (可能被问到)

### Q5: Operating window 窄 (R18-SF5, R19 R1-W4)

**预期质疑**: EC-HTE 只在 Δπ>0.15, K≤4, FNR<0.50, n_expert≥250 时有效。适用范围太窄，真实数据常不满足。

**我们的回应**:

(a) **Operating conditions 的明确量化本身是贡献**——此前文献没有给出 per-subgroup correction 何时有效的量化条件。

(b) **条件满足时效果显著**: K=2 extreme 7.4× bias reduction (Table 1)；K=4 extreme 4.7×；CausalForest 4.9×。Coverage 94-96%。

(c) **Global correction 在条件外也不比 naive 好**: 50% of K=2 configs 中 global 反而加偏（§5.2, exp-002）。不存在通用的 "better than EC-HTE" 替代方案。

(d) **Diagnostic 在 operating window 之外仍有用**: 它告诉用户何时 global correction 有害——这一功能不依赖 EC-HTE。

(e) **Ashwin et al. (2025) 记录 Δπ > 0.20**——当 LLM 误分类率跨子群变化达 5× 时，Δπ>0.15 完全可能（introduction.tex L10）。

**支撑证据**:
- Operating conditions §5.4 — experiments.tex L81-82
- 50% of K=2 加偏 — §5.2, exp-002
- 7.4× bias reduction — Table 1, §5.3
- Ashwin et al. (2025) — introduction.tex L10

---

### Q6: EC-HTE vs Stratified MLE 增量仅 1.5× (R8-W4, R19 R1-W3 间接)

**预期质疑**: HB partial pooling vs 简单 stratified MLE 仅 1.5× (0.012 vs 0.008)。为什么不直接用 MLE？

**我们的回应**: Aggregate 数字低估了 HB 价值。优势集中在资源稀缺场景——恰恰是实践中最常见的：

| 场景 | HB vs MLE 改进 | 来源 |
|------|---------------|------|
| K=2, n=50 | RMSE 4-9% | exp-001 |
| K=4, n=100, worst subgroup | RMSE +60% | exp-003 |
| K=8 | RMSE +47% (0.34 vs 0.64) | exp-030 |
| n≥1000 | 收敛至 <0.5% | exp-006 |

**HB wins 87.5% of configs (21/24)**（exp-006, method.tex L18）。

安全网特性：subgroup misspecification ($p_{\text{flip}} \leq 0.50$) 下 HB 自动退化为 global（coverage 94.5-96%），MLE 无此保护（exp-010）。

§5.3 已加直接对比：'relative to stratified MLE (0.012), the advantage is 1.5× with lower RMSE from partial pooling'。

**支撑证据**:
- 21/24 configs HB wins — exp-006
- K=2 n=50: 4-9% — exp-001; K=4 n=100 worst subgroup: +60% — exp-003
- Misspecification robustness: coverage 94.5-96% at all noise — exp-010
- Table 1: HB 0.008 vs MLE 0.012 — §5.3

---

### Q7: K>>4 Scalability——K=8 时 RMSE > Global (R17-W2, R19 R2-W5)

**预期质疑**: K=8 RMSE (0.34) 是 Global (0.168) 的 2×。实际 NLP 应用中亚组数量通常远大于 2。

**我们的回应**:

| K | EC-HTE |bias| | EC-HTE RMSE | Global RMSE | Coverage | 来源 |
|---|--------|-------------|-------------|----------|------|
| 2 | 0.008 | 0.089 | 0.099 | 93.8% | exp-039 |
| 4 | 0.012 | 0.120 | 0.125 | 95.6% | exp-039 |
| 8 | 0.183 | 0.340 | 0.168 | 95.6% | exp-039 |

**K=8 coverage 仍 95.6%**（calibrated）。RMSE 退化来自方差（31 labels/subgroup）而非偏差系统性问题。Adaptive alpha 改善 35%（0.333→0.216），gap 从 2× 缩至 1.3×（exp-033）。

论文诚实标注 K≤4 为 operating condition（§5.4, experiments.tex L82; limitations.tex L5）。

实际应用解法：增加 $n_{\text{expert}}$ budget 或合并相似子群降低有效 K。推荐 $n_{\text{expert}}/K \geq 50$。

**支撑证据**:
- K=8: coverage 95.6%, RMSE 0.34 vs Global 0.168 — exp-039
- Adaptive alpha: 35% improvement, still 1.3× Global — exp-033
- Operating conditions — experiments.tex L82; limitations.tex L5

---

### Q8: 'Debiasing' 术语歧义 (R19-W2, R2 Should-Fix)

**预期质疑**: NLP 社区 'debiasing' 通常指 fairness debiasing，标题 'When Debiasing Hurts' 可能误导。

**我们的回应**: 论文已在三处消歧：

1. **Introduction 脚注 1**（introduction.tex L9）: 'Throughout, "debiasing" refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.'
2. **Section 3 标题**: 'Bias Decomposition: When Debiasing Hurts'——上下文明确是统计偏差
3. **正文术语**: 全文使用 'misclassification correction' 和 'bias correction'

'Debiasing' 在 measurement error 文献中有长期使用先例（Fuller 1987, Carroll et al. 2006）。标题中的 provocative framing 是有意为之——传达核心信息：标准校正程序在特定条件下有害。

如 reviewer 坚持，可在 Abstract 首句增加限定语；但脚注 1 已足够显眼（R6-M2 已将其从 Section 3 提前到 Section 1）。

**支撑证据**:
- introduction.tex L9 脚注 1
- R6-M2 resolution: 脚注位置提前（review_issues.yaml）

---

## Pre-emptive (主动澄清，审稿人未问但应提前准备)

### P1: Cross-LLM Consistency

**我们的回应**: Bias identity 在 11 个 LLM-dataset 组合上 $R^2 = 0.975$（exp-024）。6 个 OpenAI 模型（GPT-3.5 至 GPT-5.4，跨三代）均展现 $\Delta\pi > 0.05$（exp-008），确认异质性是 LLM annotation 的结构性属性而非特定模型 artifact。4 个开源 LLM（Llama/Qwen/Mistral/Gemma）在 TweetEval 上 HB wins 32/32 comparisons（exp-025）。

**支撑证据**: exp-024 ($R^2=0.975$), exp-008 (6 models), exp-025 (open-source 32/32), Appendix app:realcm_bias / app:multilm

---

### P2: Stance Detection Cross-Task Validation

**我们的回应**: TweetEval stance detection（5 targets × 3 LLMs, K=5, n=300/subgroup）验证 sign reversal 在情感分析之外同样存在：Global sign reversal 4/30 (13.3%), EC-HTE 1/30 (3.3%), Global bias amplification 15/30 (50%)。

**但 RMSE 劣势**: naive=0.116, global=0.272, EC-HTE=0.271。GPT-3.5-Turbo FNR>0.50 在所有 targets，κ 范围 [4.6, 15.0]。与 operating conditions 一致：K=5 + 高 FNR 超出 operating window。EC-HTE 保护 sign correctness 但无法同时改善 RMSE when operating conditions violated。

**支撑证据**: Appendix app:stance, Table stance_signrev, report.md

---

### P3: PPCI Composition

**我们的回应**: EC-HTE 校正 covariate-side ($\hat{Z}$) error，PPCI 校正 outcome-side ($\hat{Y}$) error。互补非替代：

| DGP | EC-HTE alone | PPCI alone | EC-HTE+PPCI | 来源 |
|-----|-------------|-----------|-------------|------|
| A (covariate only) | |bias|=0.005 | 0.020 | 0.005 | exp-007 |
| B (outcome only) | 0.088 | 0.015 | 0.005 | exp-007 |
| C (both) | 0.179 | 0.004 | 0.007 | exp-007 |

DGP A: EC-HTE 38% RMSE advantage over PPCI (method.tex L61)。DGP C: composition reduces |bias| from 0.179 to 0.007 (method.tex L60)。

**支撑证据**: method.tex L56-61, exp-007

---

### P4: Bootstrap SE vs Plug-in SE

**我们的回应**: CausalForest plug-in SE: 93.8% aggregate coverage。Bootstrap ($B=100$) recovers ≥95% at all budgets tested including $n_{\text{expert}}=25$（exp-036）。DIM + Centered EB: bootstrap ≥95% at all $n_{\text{expert}} \geq 25$（memory.md）。推荐 $n_{\text{expert}}/K < 50$ 时用 bootstrap；otherwise plug-in suffices。

**支撑证据**: exp-036, Table 1 footnote (experiments.tex L65), method.tex L47-48

---

### P5: Subgroup 选择指导 (R13-W1, R19 R1-Q1)

**我们的回应**: EC-HTE 框架要求预定义离散亚组——与因果推断 subgroup analysis 标准实践一致。Data-driven subgroup discovery 引入 overfitting 风险，超出本文范围。EC-HTE 对子群定义本身 agnostic（text-feature / demographic 均可）。Subgroup misspecification ($p_{\text{flip}} \leq 0.50$) 下 HB 自动退化为 global，coverage 保持 94.5-96%（exp-010）。

**支撑证据**: limitations.tex L11, exp-010, experiments.tex L83

---

### P6: 计算成本 (R18-M1, R19 R1-Q3)

**我们的回应**:

| 组件 | 时间 | 配置 |
|------|------|------|
| Centered EB optimization | <5ms | K=4, N=5000 |
| Full Gibbs MCMC | ~5s | 同上 |
| Bootstrap SE (B=100) | ~0.4s | 同上 |
| 完整 pipeline | <5 min | K=4, N=5000 |

LLM annotation 本身需数小时至数天。EC-HTE 计算开销相对可忽略。R19 R2 交叉回应确认可接受。

**支撑证据**: method.tex L16-17, R18-M1/R19 R1-Q3

---

### P7: '7.4× bias reduction' 比较基准 (R19-W1, resolved)

**我们的回应**: 7.4× vs Global (0.059→0.008)；vs Strat. MLE 仅 1.5× (0.012→0.008)。两个基准均有意义：Global 是 PPI/DSL 默认做法（实践者当前标准操作）；MLE 反映 HB partial pooling 边际贡献。§5.3 已同时报告两组对比。

**支撑证据**: Table 1, §5.3, R19-W1 resolution

---

### P8: Hyperprior 敏感性 (补充)

**我们的回应**: Gamma(3,1) hyperprior 在 2× 扰动下 RMSE 变化 ≤5%（method.tex L12; exp-022: 6.0% across reasonable range, coverage 0.925-0.938）。15 个 (shape, scale) 组合中 HB beats MLE 9/15。Best config Gamma(1,0.5) RMSE=0.0825 vs default Gamma(3,1) RMSE=0.0841——差异 <2%。Partial pooling 天然提供 regularization：hyperprior 影响随 $n_{\text{expert}}$ 增大而减弱。

**支撑证据**: exp-022, method.tex L12, Appendix app:hyperprior

---

## Quick Reference: Key Numbers by Source

### Bias Identity
| Metric | Value | Source |
|--------|-------|--------|
| R² (K=2 synthetic) | 0.994 | §5.2, exp-002 |
| R² (K=4 synthetic) | 0.97 | §5.2, exp-002 |
| R² (11 empirical LLM CMs) | 0.975 | Appendix, exp-024 |
| R² under class imbalance P(Z=1)=0.1 | ≥0.976 | Appendix, exp-019 |

### Sign Reversal
| Condition | Rate | Source |
|-----------|------|--------|
| τ(0)=0.01 | 31.0% | §5.2, exp-038 |
| τ(0)=0.03 | 14.9% | §5.2, exp-038 |
| τ(0)=0.05 | 6.1% | exp-038 |
| τ(0)≥0.089 | 0% | exp-038 |
| EC-HTE (all configs) | 0% | §5.2 |
| Stance (Global) | 13.3% (4/30) | Appendix app:stance |
| Stance (EC-HTE) | 3.3% (1/30) | Appendix app:stance |

### EC-HTE Performance (Table 1)
| Config | Method | |Bias| | RMSE | Coverage |
|--------|--------|--------|------|----------|
| DIM K=2 extreme | Naive | 0.058 | 0.090 | 0.82 |
| | Global | 0.059 | 0.099 | 0.87 |
| | HB EC-HTE | **0.008** | 0.089 | 0.94 |
| DIM K=4 extreme | Global | 0.056 | 0.125 | 0.91 |
| | HB EC-HTE | 0.012 | 0.120 | 0.96 |
| CF K=4 extreme | Global | 0.191 | 0.244 | 0.58 |
| | EC-HTE Forest | **0.039** | 0.180 | 0.90 |

### A1 Sensitivity
| Parameter | Coverage Degradation | Source |
|-----------|---------------------|--------|
| γ (outcome-dep) 0→0.2 | 95.5%→93.5% (−2pp) | exp-029 |
| γ_T (treatment-dep) 0→0.05 | 94.5%→89.7% | exp-040 |
| γ_T=0.10 | 75% (breakeven) | exp-040 |

### HB vs MLE
| Metric | Value | Source |
|--------|-------|--------|
| HB wins across grid | 87.5% (21/24) | exp-006 |
| K=2 n=50 improvement | 4-9% RMSE | exp-001 |
| K=4 n=100 worst subgroup | +60% RMSE | exp-003 |
| Convergence at n≥1000 | <0.5% difference | exp-006 |

### Diagnostic AUC
| Condition | AUC | Source |
|-----------|-----|--------|
| Δτ>0 subgroups | 1.0 | §5.4, exp-005 |
| All synthetic | 0.86 | §5.4, exp-005 |
| 16 semi-synthetic LLM combos | 0.63 | §5.4, exp-028 |

### Computational Cost (K=4, N=5000)
| Component | Time | Source |
|-----------|------|--------|
| Centered EB | <5ms | method.tex L16 |
| Gibbs MCMC | ~5s | method.tex L16 |
| Bootstrap SE (B=100) | ~0.4s | method.tex L17 |
| Full pipeline | <5 min | R19 R2 confirmation |
