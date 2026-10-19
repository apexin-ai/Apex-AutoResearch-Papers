---
round: 23
review_mode: fresh
overall_score: 3.5 - Borderline Conference (推荐 Findings)
timestamp: 2026-05-24T04:19:43.574056+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 23 审稿报告

**Venue**: EMNLP 2026 (via ARR)  
**格式**: Long Paper, 8-page main text limit  
**审稿模式**: Fresh (重新审稿)  
**Reviewer 编排**: 2 人（R1: 方法严谨性/理论完整性; R2: 新颖性/完整性/相关工作）  
**轮次**: 1 轮（交叉回应后达成共识，无需额外轮次）

---

## Summary

本文系统分析 LLM 标注误差在因果推断中的传播机制，覆盖 7 种 DAG 拓扑 × K 类别。核心贡献包括：(1) K≥3 下标注误差引发质性新现象（exposure 拓扑 83.6% sign reversal vs 其他拓扑 0-2.1%），建立跨拓扑的 bias taxonomy；(2) Annotation Sensitivity Value (ASV) 诊断工具，量化混淆矩阵到 sign flip 的最小扰动；(3) FWL futility result 证明 4 种 covariate 拓扑下矩阵校正在 OLS 中无效，以及 topology-aware correction guidance。理论框架建立在 non-differential misclassification + linear SEM + proportional effects 三个核心假设之上。

---

## Strengths

**S1. 系统性覆盖的独立价值。** 首次在统一框架下比较 7 种 DAG 拓扑 × K 类别的标注误差传播行为。K≥3 引入的 structural dichotomy 是质性新现象（而非 K=2 的量的推广）：exposure 拓扑在 K≥3 下从安全变为高危（83.6% sign reversal），confounding/mediation 在 K≥3 下也出现非零 violation rate（13.7% under realistic accuracy）。这不是 Brenner (1993) 的直接推广。

**S2. 严格的理论层次。** K=2 exact proof (Theorem 1) → K=3 symmetric exact (Theorem 2) → general K≥3 conjecture with extensive numerical verification (545,945 adversarial curves)。理论推导在适用范围内是正确和完整的。

**S3. FWL futility result 的实践价值。** 虽然证明技巧简短（FWL 定理的直接推论），但 observation 本身对 NLP 实践者有重要警示价值：使用 confusion matrix 校正标注再跑回归在 4 种 covariate 拓扑下 provably useless。这是一个 counterintuitive negative result。（两位 Reviewer 对其 novelty 有分歧——见 Divergence D1。）

**S4. 真实 LLM 混淆矩阵的验证。** Section 4.4 使用 23 个真实 LLM 配置的混淆矩阵验证 bias ranking 和 sign-flip predictions；Appendix B.18 Political Ad case study、B.19-B.20 semi-real case study 提供超越纯模拟的实证成分。

**S5. 数值验证覆盖面广。** MC 模拟 MAPE 1.6%，100,000 Dirichlet-sampled matrices，adversarial monotonicity 验证，bootstrap CI 收敛分析。在计算数学标准下，这是 strong evidence。

**S6. 实践工具完整。** Algorithm 1 将理论发现转化为决策流程（risk assessment → correction routing → FWL check），对 practitioner 有直接指导价值。

---

## Weaknesses

### Must-Fix（两位 Reviewer 共识）

**MF-1 [Critical | R1-N3 + R2-N2 | 共识 AGREE]: Conjecture 1 未证明，削弱 K≥3 ASV 框架的理论可靠性。**

Conjecture 1（general K≥3 approximate envelope monotonicity）是 ASV 框架的理论基石。依赖链：Conjecture 1 → ASV vulnerability ranking 有序性 → Algorithm 1 Step 1 risk level 判断 → correction routing 正确性。若 conjecture 存在反例，Algorithm 1 可能给出错误建议。

数值验证虽然广泛（545,945 adversarial curves, max step deviation < 0.04），但存在两个隐忧：(a) Appendix B.12 Table 11 显示 K=7 worst-case magnitude deviation 0.060，比 K=3 的 0.003 大一个数量级——approximate monotonicity 质量随 K 增大恶化，在 HumAID K=10 下可靠性存疑；(b) adversarial search 的 4 种结构族基于直觉选择，是否覆盖 worst case 不清楚。

论文应讨论：如果 approximate monotonicity 偶尔被违反（ε < 0.017），Algorithm 1 的 robustness 如何？小幅违反是否导致 correction routing 质变？

**MF-2 [Critical | R1-N2 + R2-W1→升级 | 共识 AGREE]: Non-differential misclassification 假设与论文自身 stress test 结果构成内部一致性矛盾。**

论文全部理论结果依赖 non-differential misclassification（标注误差独立于 outcome），但论文自己的实证检验显示该假设在目标场景中被系统性违反：
- Appendix B.6 Table 8-9: 13.3% baseline violation rate
- 14/16 K≥3 exposure configurations 在 α=0.01 下出现 structured departures（正文 p.4）
- Appendix B.26 Y-stratified permutation test 在 VAST 数据上 13.3% violation rate

R2 补充 violation 主要是 content-dependent（topic/sentiment driven）而非纯粹 outcome-dependent，在控制 topic 后可能不违反假设。但这个论点在论文中未被充分发展。当理论框架的核心假设在目标应用中被系统性违反时，理论结果的实际指导价值需要更诚实的讨论。

**MF-3 [Critical/Should-Fix | R1-N1 + R2 partially agree | 共识 PARTIALLY AGREE]: Theorem 1 的 proportional effects 假设在 NLP 中几乎不可验证。**

Theorem 1 要求所有类别的 treatment effect 按同一比例缩放。论文的数值验证使用满足该假设的 DGP，non-proportional sparse DGP 下 24.2% 违反率被正文忽略。R2 认为 R1 对假设不合理性的判断"稍过强"（ordinal 单调效应场景下是合理近似），但双方共识：论文缺少"NLP 中何时/何种任务下 proportional effects 合理"的实质讨论。

---

### Should-Fix（两位 Reviewer 共识或多数同意）

**SF-1 [R1-W1 + R2-W2 | 共识 AGREE]: Linear SEM 假设严重限制 practical recommendations 的适用范围。**

Appendix B.7 nonlinear DGP 测试显示 sign-flip rate 在 structured violation 下仍为 0%（部分 robustness），但 matrix-based correction 在 logistic regression 下 bias reduction ≈ 0%，FWL invariance 在非线性模型下形式上不再成立。论文的 practical recommendations 对非线性模型（matching, doubly-robust, deep learning）几乎完全不适用。这对 EMNLP 读者群体（更多使用非线性模型）构成重大适用性限制。

**SF-2 [R1-W4 + R2-N3 | 共识 AGREE]: 端到端真实因果验证缺失。**

论文的 "empirical validation" 本质是 theory-MC consistency check + retrospective analysis（已知 ground truth 或 simulated outcomes）。缺少在 researcher 不知 ground truth 的真实因果推断场景中展示框架 decision-making value 的验证。理想验证：对一个有 gold-standard causal effect 的 NLP 任务，展示 Algorithm 1 routing 后的 corrected estimate 比 naive estimate 更接近 ground truth。

两位 Reviewer 均认为获取同时有 gold labels 和已知因果效应的真实数据很困难，因此定级 should-fix 而非 must-fix。

**SF-3 [R2-W3 | R1 AGREE]: 相关工作缺口。**
- 缺少与 Cinelli & Hazlett (2020) partial R² sensitivity analysis 的方法论对比
- 缺少 regression calibration (Carroll et al. 2006) 在 categorical misclassification 下的不适用性讨论
- PPI++ 理论 guarantees (Angelopoulos et al. 2023) 值得在 Related Work 中讨论（R1 认为非重大遗漏）

**SF-4 [R1-W3 | R2 AGREE]: C(δ) 线性插值参数化的局限性。**

C(δ) = (1-δ)I + δC₀ 假设误分类模式在质量变化时保持结构不变，但 LLM 在不同 prompt/temperature 下混淆矩阵结构可能定性改变。ASV 的 "minimum perturbation to sign flip" 解释可能不准确。R2 认为这是 sensitivity analysis 通用问题（E-values 类似），非本文特有缺陷。应 acknowledge 但不必改变方法。

**SF-5 [R1-Q1 + R2 AGREE]: B_OV 间接可观测性问题。**

Proposition 1(a) 中 B_OV = Cov(g(A), f(A)) / Var(f(A)) 涉及真实 A 而非 observed A*。Section 3.3 通过 bootstrap (A* → C⁻¹ → A) 间接估计，但 estimation error propagation 未讨论。这是 ASV 从理论到实用的潜在瓶颈。

---

### Minor Issues

**m1**: Figure 2 轴标签字号偏小（~7pt），视觉审查和 R2 均指出。R1 认为密度在 8 页限制下合理。

**m2**: Section 3.1 notation 密度高（plim/FWL 对 NLP 读者不友好），R2 建议 notation table。

**m3**: DAG misspecification under measurement error 应在 limitations 讨论。

**m4**: AI assistance in proof development 未在 Section D 明确披露（ACL policy 要求充分描述）。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全或实质性共识：

| 编号 | 问题 | 共识类型 | 严重性 |
|------|------|----------|--------|
| MF-1 | Conjecture 1 未证明 | [AGREE] 双方完全一致 | Critical |
| MF-2 | Non-differential 假设内部矛盾 | [AGREE] 双方完全一致 | Critical |
| MF-3 | Proportional effects 实践讨论缺失 | [PARTIALLY AGREE] | Critical/Should-Fix |
| SF-1 | Linear SEM 限制 | [AGREE] 双方完全一致 | Should-Fix |
| SF-2 | 端到端真实验证缺失 | [AGREE] 双方完全一致 | Should-Fix |
| SF-3 | 相关工作缺口 | [AGREE] | Should-Fix |
| SF-4 | C(δ) 参数化局限 | [AGREE] | Should-Fix |
| SF-5 | B_OV 可观测性 | [AGREE] | Should-Fix |

---

## Reviewer Divergence

**D1 [FWL futility result novelty]: R1 认为 novelty 不足（FWL 定理直接推论，3-4 步证明），R2 认为 observation 的实践价值大于证明技巧的深度。**

共识落点：R2 同意 R1 的 framing 建议——论文应将此定位为 "a practically important observation that follows from FWL"，而非暗示 deep theoretical contribution。贡献列表中与 bias taxonomy 和 ASV 并列可能给人过高 novelty 印象。

**D2 [Theorem 2 symmetric assumption]: R1 认为 should-fix（VAST d_rel=0.30-0.38 远非对称，Remark 4 与正文脱节），R2 rebut（Theorem 2 定位为 theoretical stepping stone，论文处理得当）。**

共识落点：Theorem 2 symmetric 假设本身不是 must-fix，但正文不应暗示 Theorem 2 直接适用于实际 K=3 场景。真正问题仍是 Conjecture 1。

**D3 [Abstract "annotation quality is the wrong thing to worry about"]: R2 认为 overclaiming，R1 rebut（这是合理的 framing statement，正文内容支撑）。**

共识落点：R1 论证更有说服力——Table 1 确实说明 aggregate accuracy 不是正确 metric，counterintuitive hook 是合理写作策略。保留。

**D4 [核心贡献的增量性]: R2 强调技术手段标准、ASV 为 one-parameter sweep，R1 强调 K≥3 引入质性新现象赋予独立价值。**

共识落点：双方在结论上相近——贡献 1 的核心价值在 K≥3 质性新现象而非量的推广；贡献 2-3 方法论深度有限。定性为 "solid systematic contribution with novel qualitative insights"。

---

## Questions for Authors

**Q1**: Proposition 1(a) 中 B_OV 的估计依赖通过 C⁻¹ 从 A* 反推 A 的分布。这个间接估计步骤的 error propagation 如何？在 gold label budget 极少（50-100 samples）时 ASV 是否仍可靠？

**Q2**: 如果 Conjecture 1 的 approximate monotonicity 在实践中偶尔被违反（ε < 0.017），Algorithm 1 的 correction routing 是否会发生质变——即推荐错误的 correction method？

**Q3**: 论文能否提供一个 NLP 任务的具体例子，说明在什么条件下 proportional effects 假设是合理的近似？（如 ordinal sentiment classification）

**Q4**: Non-differential misclassification violation 中，content-dependent 和 outcome-dependent 的区别是否可以被利用——即在控制 topic 后，论文的理论结果在条件 non-differential 意义下是否仍然成立？

**Q5**: Section D 的 AI assistance 披露是否覆盖了定理证明过程？ACL 2025/2026 policy 要求 "describe the use in sufficient detail"。

---

## Missing References

**必须引用**:
- Cinelli & Hazlett (2020) — partial R² sensitivity analysis，与 ASV 方法论对比（Section 2 已引用但未对比）
- Regression calibration (Carroll et al. 2006) — 即使不适用于 categorical case 也应说明原因

**建议引用（R22 遗留）**:
- Mahajan (2006) — polytomous misclassification 非参数识别
- Hu (2008) — 非线性模型下的误分类处理
- Cornfield et al. (1959) — sensitivity analysis 方法论源头
- Törnberg (2024) — LLM 注释质量实证

---

## External Review (Stanford Agentic Reviewer)

未请求外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 已完成  
**结果**: 0 critical, 1 warning, 6 info

| 严重性 | 位置 | 发现 |
|--------|------|------|
| ⚠️ warning | p.23 | 附录单页堆叠 4 个 display items（Figure 5 + Figure 6 + Table 5 + Figure 7），版面极度拥挤 |
| ℹ️ info | p.1-2 | 连续 2 页纯文本，无 display item。ACL 格式下属常规 |
| ℹ️ info | p.5 | Figure 2 轴标签和拓扑名称字号偏小（~7pt） |
| ℹ️ info | p.6 | 纯文本页（定理密集），属理论推导例外 |
| ℹ️ info | p.8 | Figure 4 尺寸较小，适当放大可增强视觉冲击力 |
| ℹ️ info | p.28-29 | Tables 12-13 列数多、字号小、数字密度高 |
| ℹ️ info | p.35 | Algorithm 1 占 60% 页面，底部 40% 空白 |

---

## Overall Assessment

**评分: 3.5 — Borderline Conference（推荐 Findings）**

**置信度: High（两位 Reviewer 独立给出相同评分，关键问题强共识）**

本文在系统性和覆盖面上做出了扎实贡献——首次在统一框架下揭示 K≥3 标注误差传播的质性新现象（structural dichotomy），FWL futility result 对 NLP 实践者有直接警示价值。理论框架在 K=2 和 K=3 symmetric 范围内是完整的。

阻碍进入主会议的核心障碍：

1. **理论完整性缺口**：最重要的 general K≥3 case 停留在 conjecture 而非 theorem，ASV 框架的核心性质缺乏证明保障。K=7 worst-case deviation 的增长趋势加剧了这一担忧。

2. **假设-实证矛盾**：论文理论依赖的 non-differential misclassification 假设在论文自己的 stress test 中被系统性违反（13.3% violation rate），形成内部一致性问题。若不能在条件 non-differential 或 robustness 层面化解这个矛盾，理论结果的实际指导价值存疑。

3. **实践适用范围窄**：Linear SEM + proportional effects + non-differential 三个假设叠加，使得框架的直接适用场景在 NLP 中相当有限。Correction recommendations 对非线性模型几乎不适用。

4. **方法论深度有限**：ASV 本质是 one-parameter sweep，Algorithm 1 更接近 practical guideline 而非 algorithmic contribution。贡献定位应为 "solid systematic contribution with novel qualitative insights" 而非 methodological breakthrough。

**Findings 推荐理由**：覆盖度贡献真实（7 拓扑 × K≥3 的系统比较此前不存在）、K≥3 sign reversal 是质性新发现、FWL futility result 有传播价值。这些足以支撑 Findings 级别发表，但不足以进入主会议。

---

## Detailed Comments

### Section 1 (Introduction)
- "annotation quality is the wrong thing to worry about" framing 是合理的 counterintuitive hook（R1 rebut R2 的 overclaim 指控成立），但后续论证应更早连接到假设条件。
- Contribution list 中 FWL futility 与 bias taxonomy 和 ASV 并列，可能给人过高 novelty 印象。建议调整措辞为 "topology-aware correction guidance including a FWL futility result"。

### Section 3 (Theory)
- Theorem 1 (K=2) 和 Theorem 2 (K=3 symmetric) 证明完整，无误。
- Conjecture 1 是核心软肋——数值验证覆盖面广但不能替代证明。K=7 worst-case deviation 0.060 vs K=3 的 0.003 暗示 large-K 质量恶化。
- Section 3.1 notation 密度高（plim/FWL），对 NLP 读者有一定障碍。现有 footnote 覆盖基本定义，但可考虑 notation table。
- "provably" 一词在 abstract/正文中使用隐含 non-differential + proportional effects + C_A > 0 三个假设，应附加限定。

### Section 3.3 (ASV)
- ASV 的 C(δ) = (1-δ)I + δC₀ 参数化是标准 sensitivity analysis 做法，但应 acknowledge LLM 质量变化可能不沿此路径。
- B_OV 通过 bootstrap (A* → C⁻¹ → A) 间接估计，estimation error propagation 未讨论。
- Gold label budget 极少（< 500）时 ASV reliability 是开放问题。

### Section 4.2 (Empirical Results)
- Table 1 有效传达 structural dichotomy。
- Figure 2 信息密度可接受（R1 rebut R2），但轴标签 ~7pt 偏小。

### Section 4.4 (Validation)
- 23 real LLM confusion matrices 的验证比纯模拟更有说服力，但仍是 retrospective analysis。
- B.19-B.20 semi-real case study 补充了实践色彩，但仍使用构造的因果关系。

### Section 4.5 (Correction Guidance)
- FWL futility result 在 OLS 下正确且有实践价值。
- 5 种 correction methods 的对比有用，但 regression calibration 缺席。
- 对非线性模型的 recommendations 几乎完全缺失——这是最大的实践适用性缺口。

### Appendix
- B.6 stress test 结果自毁假设——论文需要更诚实地面对这个矛盾。
- B.12 adversarial verification 覆盖面广，但 4 种结构族的选择基础不清楚。
- p.23 版面拥挤（4 个 display items），建议分页。

### Limitations
- 当前 limitations 缺少：proportional effects 在 NLP 中的适用性讨论、DAG misspecification 影响、非线性模型的明确不适用声明。