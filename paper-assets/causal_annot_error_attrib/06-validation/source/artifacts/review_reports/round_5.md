---
round: 5
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T17:12:29.557702+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告 — Round 5 (Fresh Review)

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (via ARR, Long Paper)
**Deadline**: 2026-05-25
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验验证; R2: 新颖性+完整性+写作质量）
**审稿模式**: Fresh（重新审稿）

---

## Summary

本文系统研究了 K≥3 类 LLM 标注误差在七种因果 DAG 拓扑下的偏差传播特性。核心发现包括：(1) 二元情形下的 "toward-null" 保证在多类情形下结构性失效——exposure 和 IV 拓扑可产生符号反转，而 confounding、collider、mediation、M-bias、front-door 在特定 DGP 条件下保持符号；(2) 基于 FWL 不变性，矩阵类校正方法对 4 种 covariate 拓扑产生恰好 0% 偏差减少；(3) 提出 Annotation Sensitivity Values (ASV) 框架，揭示从 IV（最脆弱）到 M-bias（免疫）的拓扑依赖脆弱性谱系。23 个真实 LLM 配置的经验验证与理论预测一致。

---

## Strengths

**S1. 系统性的跨拓扑分析填补了明确的研究空白。** [R1-S1, R2-S1, 共识] 现有文献各自分析单一拓扑或仅覆盖二元情形；本文首次在统一框架下用同一混淆矩阵比较 7 种拓扑的偏差行为。"首次跨 7 种拓扑系统比较"的声明经 R2 核查成立。

**S2. FWL 不变性负面结果干净且重要。** [R1-S2, R2-S3, 共识] 证明矩阵类校正方法（Naive plug-in, MLA, SIMEX）对 4 种 covariate 拓扑产生 exactly 0% bias reduction。证明路径（column space preservation）简洁完整，是标注校正文献忽略的重要发现。

**S3. 三级证据层次结构透明、学术诚实。** [R1-S3, R2-S2, 共识] 明确区分 (i) 解析证明（Proposition 1(a,b), Theorem 1）、(ii) 数值验证零违反（mediation, M-bias, front-door）、(iii) ε-近似猜想（Conjecture 1），比笼统声称"我们证明了"要可信得多。

**S4. 经验验证覆盖面广且设计合理。** [R1-S4, R2-S4, 共识] 23 个真实 LLM 配置 × 7 拓扑 × 3 数据集（HumAID K=10, VAST K=3, CivilComments K=2），覆盖 frontier 到 7B 模型。Theory-MC 一致性 MAPE 2.0%。

**S5. ASV 框架是 E-value 的有意义扩展。** [R1-S5, R2-S5, 共识] 三个关键技术差异（K×K→1D 参数化需证明近似单调性、三种 ASV 类型对应不同失效模式、与 FWL 结合指导校正选择）使其超越 E-value 的简单迁移。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [CRITICAL/MAJOR — R1 CRITICAL, R2 AGREE with nuance] Theorem 1 对 K≥3 缺乏解析证明**
- Theorem 1 声称 confounding 和 mediation（proportional effects）下 |B(C(δ))| 关于 δ 单调不减。关键步骤 V_B(δ) 单调不增：K=2 有解析证明，K≥3 仅有数值验证（10,000 矩阵零违反）。Proof sketch 中 "algebraically" 一词可能误导。
- **分歧**：R1 主张降级为 Conjecture（"标为 Theorem 意味着有完整证明"）；R2 主张修改措辞而非降级（"zero violations + proportional effects 约束使其与 Conjecture 1 有质的区别"）。
- **Director 判断**：R2 的 nuance 有理——Theorem 1（zero violations, 强结构约束）与 Conjecture 1（60-98% 非单调步骤，weak ε bound）确有质的区别。建议采用 R2 方案：Theorem 声明中明确 "K=2: proved; K≥3: verified numerically with zero violations across 10,000 random C₀"，删除 "algebraically" 措辞。
- **建议修改方向**：Theorem + Remark 组合，或 Theorem 适用 K=2 + Proposition（numerical evidence）适用 K≥3。

**W2 [CRITICAL — R1 CRITICAL, R2 AGREE] Table 1 的 sign-flip guarantee ✓ 掩盖 DGP 条件性**
- Table 1 对 5 个拓扑标注 ✓（"structural sign-flip guarantee holds"），但仅 M-bias 是无条件的。其余 4 个均有 DGP 条件：confounding 需 sign(τ)=sign(τ+B_OV)，mediation 需 sign(τ_dir)=sign(τ_total)，front-door 和 collider 各有条件。Practitioners 直接查表做决策会获得错误安全感。
- **建议**：用不同符号区分无条件保证（M-bias: ✓）和有条件保证（其余 4 个: ✓*），caption 中明确列出条件引用。

### Should-Fix（影响评分但不一票否决）

**W3 [MAJOR — 双方共识] 非差异性误分类假设在 LLM 场景下的适用性讨论不足**
- LLM 从同一文本同时提取 treatment 和 outcome 信号（"文本作为共同原因"），这是 Definition 1 的结构性违反。Few-shot demonstrations 编码 treatment-outcome 关联。RAG 系统可能检索包含 Y 的文档。Appendix B.5 stress test 仅测试人为 ε-perturbation，未测试 LLM 诱导的真实差异性模式。
- **建议**：Section 3.1 加入 "text as common cause" 机制讨论；提供 practitioner diagnostic（如在 gold-label 子集上检验条件独立性）。

**W4 [MAJOR — 双方共识] 线性 SEM 假设限制 FWL 不变性的通用性**
- FWL 不变性根本性依赖线性投影，在 logistic/probit 回归中不成立。Section 4.5 声称 "matrix-based corrections are provably ineffective for four topologies" 严格来说仅在 OLS 下成立。Algorithm 1 的非线性 caveat 仅在 caption 中，正文未讨论。Appendix B.6 logistic DGP 检查仅验证 sign-flip pattern，未验证 FWL breakdown 或 correction 效果。
- **建议**：Section 4.5 明确 FWL 适用范围限于线性模型；logistic DGP 下验证至少一个拓扑的 correction 效果。

**W5 [MAJOR — 双方共识] Conjecture 1 的 ε 处理过于轻描淡写**
- ε 可达 0.14（front-door, extreme τ）和 0.15（exposure, extreme-tail matrices），ε/η 误差在 ASV 0-2 范围内可达 1.3-1.4 δ-units。Table 7 显示 60-98% 矩阵存在非单调步骤。"negligible" 一词不准确。
- **缓解因素**：Conjecture 正文已标注了 τ 范围和 ε 上界（非 hidden fine print）；推荐操作范围 τ ∈ [0.5, 2.0] 内 ε < 0.06。
- **建议**：将 "negligible" 改为 "bounded"；用独立段落讨论 ε 对 δ* 精度的定量影响；明确 ASV 推荐适用范围。

**W6 [MINOR — 双方共识] "Primary coefficient never reverses" 缺乏理论保证**
- 基于 23 个配置的经验观察，Abstract 措辞暗示普遍性。从 Eq.(2) 看，same-sign β_k 保证仅 attenuation，值得 formalize 但论文未做。
- **建议**：Abstract 改为 conditional 表述；如可能，formalize same-sign β_k → sign preservation 的充分条件。

**W7 [MINOR — R2] 数字密度较高影响部分段落可读性**
- Introduction 第二段 3 行内 6 个百分比；Section 4.4 Cross-K 段落密集堆积数字。
- **建议**：Introduction 精简至 2-3 个关键数字；Cross-K 比较考虑表格呈现。

**W8 [MINOR — R2, R1 AGREE] 符号 τ 在不同拓扑下含义不同，main text 切换时无明确提示**

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 独立提出并在交叉回应中达成共识：

1. **线性 SEM / FWL 限制**（R1-W3 ↔ R2-N2）：FWL 不变性仅在线性框架下成立，需要明确适用范围并在非线性 DGP 下验证
2. **Non-differential 假设讨论不足**（R1-W2 ↔ R2-N1）：LLM 场景下文本作为共同原因是结构性违反，需要更充分讨论
3. **Conjecture 1 ε 处理**（R1-W1 ↔ R2-N3）："negligible" 不准确，需要更审慎的呈现
4. **Primary coefficient claim**（R1-W4 ↔ R2-W1）：经验发现需要降级表述或 formalize 充分条件
5. **Table 1 条件性**（R1-N2, R2 AGREE）：✓ 符号应区分有条件/无条件保证

---

## Reviewer Divergence [分歧]

**Theorem 1 处理方式**：
- R1 [CRITICAL]：应降级为 Conjecture/Proposition，因为"标为 Theorem 意味着有完整证明"
- R2 [AGREE with nuance]：应修改措辞而非降级——zero violations + proportional effects 约束使其与 Conjecture 1 有质的区别。建议 Theorem + Remark 组合。
- **Director 判断**：R2 的区分有理。建议修改措辞明确 K=2 proved / K≥3 numerically verified，而非完全降级。

**Excitement / Venue 适配性**：
- R1 (3.5/5)：问题重要且具实践价值，但"与 NLP community 核心关注点有一定距离"
- R2 (3/5)："NLP 社区可能对此理论较重的工作兴趣有限"，但 R2-S1 同时确认"填补明确研究空白"
- **Director 判断**：LLM-as-annotator 是 NLP 热点话题，本文的 practical guidance 对 CSS+NLP 交叉社区有直接价值。Excitement 不应成为 reject 理由。

---

## Questions（需要作者回答）

**Q1.** [R1-Q1, R2 AGREE] Theorem 1 对 K≥3 能否通过 symbolic differentiation 完成 V_B(δ) 的导数符号验证？

**Q2.** [R1-Q2, R2 AGREE] Sign preservation 的 DGP 条件（如 sign(τ)=sign(τ+B_OV)）在实践中如何验证？ASV 框架是否充分解决了这一循环依赖问题？

**Q3.** [R1-Q3, R2 AGREE] Same-sign β_k 是否给出 exposure sign preservation 的充分条件？如果是，这是一个重要结论应 formalize。

**Q4.** [R1-Q5, R2-Q4, 双方共识] FWL 不变性在 logistic regression 下是否 breakdown？能否用 logistic DGP 验证 Naive plug-in 不再是 0% reduction？

**Q5.** [R2-Q2] DGP 参数（τ=2.0）是否代表 CSS 典型效应量？社会科学中效应通常较小（τ<0.5），在小效应下 sign preservation 条件是否更容易被违反？

**Q6.** [R2-Q3] 当候选拓扑包含 exposure（可能反转）和 confounding（不会反转）时，如何操作性地定义 "most conservative" ASV？

**Q7.** [R1-Q4] PPI++ 的 gold label fraction 和 sensitivity 分析？

**Q8.** [R1-Q6, R2-Q5 部分分歧] 83.4% 在 informative prior（拟合真实 LLM confusion matrices 的 Dirichlet(α)）下会如何变化？R1 认为当前 framing 已平衡，R2 认为 2.1%（diagonal≥0.7）更具参考价值。

---

## Missing References

**高优先级（双方共识）：**
1. Mahajan (2006) 或 Frölich (2007) — IV with mismeasured instruments，与 IV 拓扑分析直接相关
2. Lash, Fox, Fink (2009/2021) — *Applying Quantitative Bias Analysis to Epidemiologic Data*，QBA 标准教科书，与 ASV 框架定位相关
3. Kuroki & Pearl (2014) — measurement bias and effect restoration，与 correction guidance 形成对照

**可选（部分共识）：**
4. Mohan, Pearl, Tian (2013) — missing data as causal problem（R1 mildly agree，相关性有限）
5. Kang & Schafer (2007) — doubly robust estimators（R2 partially rebut，FWL invariance 的线性框架限制）

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 项目配置未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态：失败。** 视觉审查 Agent 因资源限制（rate limit）未能完成逐页检查。Error: "You've hit your limit · resets 4pm (UTC)"。建议用户可在资源恢复后重新触发。

**格式合规（R2 手动检查）：** 全部通过——正文 ≤ 8 页、ACL 模板（`\usepackage[review]{acl}`）、匿名（"Anonymous ACL submission"）、Limitations 覆盖 4 个局限点、References 格式一致、图表清晰可读。

---

## Overall Assessment

**评分：3.5 (Borderline Conference)**
**置信度：4/5**（两位 Reviewer 均为 4/5）

### 评分理由

**支持接收的因素：**
- 填补了跨拓扑系统比较的明确研究空白（首创性经核查成立）
- FWL 不变性负面结果对标注校正文献有重要修正意义
- 三级证据层次处理体现学术诚实
- 经验验证覆盖广（23 LLM configs × 7 topologies × 3 datasets, MAPE 2.0%）
- ASV 框架为从业者提供可操作的敏感性分析工具
- 格式合规，写作整体清晰

**阻止更高评分的因素：**
- Theorem 1 对 K≥3 的证明不完整（核心理论结果依赖数值验证）
- Table 1 的 ✓ 符号掩盖 DGP 条件性，可能误导 practitioners
- Non-differential misclassification 假设在 LLM 场景下的适用性受限，论文对此讨论不足
- 线性 SEM 限制了 FWL 不变性等核心结论的通用性，非线性验证缺失
- Conjecture 1 的 ε 在极端条件下较大，对 ASV 精度的影响被低估

### 接收建议

本文处于 Conference/Findings 边界。如果作者能在 camera-ready 中：
1. 修改 Theorem 1 措辞明确 K≥3 的数值验证性质（成本低，效果大）
2. 修改 Table 1 区分有条件/无条件保证（成本低，效果大）
3. 在 Section 3.1 和 Section 4.5 中分别加强 non-differential 假设和线性 SEM 限制的讨论（成本中等）

则论文可达到 Conference 水平。当前版本更适合 Findings。

### 维度评分汇总

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5/5 | 4/5 | 3.5/5 |
| Excitement | 3.5/5 | 3/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.5/5 | 3.5/5 | **3.5/5** |
| Confidence | 4/5 | 4/5 | 4/5 |

---

## Detailed Comments（逐节）

### Abstract
- 整体准确概括了三个贡献
- "the primary treatment effect never reverses in any of 23 empirical LLM configurations" 应改为 conditional 表述
- 数字密度可控（~5 个核心数字），较前版本已大幅改善

### Section 1 (Introduction)
- 动机叙事有说服力：LLM annotators 快速普及 + K≥3 结构性突变
- 83.4% 与 2.1% 的并列呈现已较平衡，但 Introduction 第二段数字密度仍高（3 行 6 个百分比）
- 三个贡献陈述清晰

### Section 2 (Related Work)
- 三段结构（measurement error / LLM annotation / sensitivity analysis）覆盖完整
- 定位准确："all analyze a single DAG topology; ours is the first to characterize across seven"
- 缺少 Mahajan(2006)/Frölich(2007)（IV mismeasurement）、Lash/Fox/Fink(2009/2021)（QBA）、Kuroki&Pearl(2014)

### Section 3 (Method)
- Definition 1 需加 "text as common cause" 讨论
- Bias expressions (3.2) 推导清晰，7 个拓扑的处理系统
- Proposition 1 的条件在正文中呈现较好，但 Table 1 未反映
- Theorem 1 的 proof sketch 需修改 "algebraically" 措辞
- Conjecture 1 正文已标注 ε 范围（非 hidden fine print），但 "negligible" 一词需替换
- ASV 三种类型的动机和定义清晰

### Section 4 (Experiments)
- Theory-MC agreement MAPE 2.0% 可靠（R1 建议补充 tail statistics，合理）
- Exposure sign reversal 分析充分（Dirichlet full + realistic subspace）
- Empirical validation 23 configs × 7 topologies 覆盖广
- Correction guidance 的 FWL invariance 需明确线性适用范围
- Cross-K comparison 数字密度高，建议表格化

### Section 5 (Conclusion + Limitations)
- Conclusion 简洁到位
- Limitations 覆盖 4 个点：non-differential assumption, DAG specification, K/nonlinearity extensions, single annotator
- 建议补充：商业 LLM 缺失、线性 SEM 对 FWL 的限制

### Appendix
- 证明细节充分（Appendix A）
- 实验补充完整（Appendix B）
- ClinicalBERT 案例研究（Appendix B.3）过于简略，建议加定量 ASV 计算
