---
round: 35
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-21T02:53:00.731173+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告：Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains

**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿模式**: Fresh (初审)
**Reviewers**: R1 (方法严谨性 + 实验设计) + R2 (新颖性 + 完整性)
**交叉审稿**: 完成，双向逐条 [AGREE]/[REBUT]

---

## Summary

本文提出 Depth Fingerprinting，将 AI 文本检测从 binary (human/machine) 扩展到 ordinal depth estimation (gen-0/gen-1/gen-2+)。核心发现是 Differential Depth Response (DDR)：在 8 个 base-model generators（5 个架构家族，0.6B-8B）上，NLL location 特征随 generation depth 单调漂移（Cohen's d=0.76-1.17），而 shape 特征保持近稳态（d<0.10）。基于 DDR 的 7-feature XGBoost 在 LOGO 下达 leak-free binary F1=0.694；QLoRA 端到端达 0.905。论文将 DDR 分解本身（而非分类器性能）定位为主要贡献。

---

## Strengths

**S1. 任务定义新颖且有价值。** 从 binary detection 到 ordinal depth classification 的扩展填补了检测文献中的空白，具有清晰的 data provenance 和 model collapse 分析 motivation。[R1+R2 共识]

**S2. DDR 分解提供机械性解释。** Location drifts while shape is preserved 的发现通过 top-p truncation 给出了机制解释，并通过温度消融和 prompt type 消融提供了两个可检验的预测，均得到验证。[R1]

**S3. 实验控制极其详尽。** Seed-sharing control、length confound control、independent-seed experiment、cross-reference model、cross-temperature、cross-domain、cross-prompt-type、TOST equivalence testing——几乎所有合理的混淆变量均有控制实验。附录 20+ 页系统性消融展示了对潜在质疑的充分预判。[R1+R2 共识]

**S4. 诚实处理 null results 和限制。** Downstream utility 的 TOST equivalence (null result)、instruction-tuned models 下的性能退化、baseline 在某些 metric 上超越——均被坦诚报告。这种学术诚实度在投稿论文中较为少见。[R1+R2 共识]

**S5. 统计方法论自觉。** Cohen's d effect sizes、bootstrap CIs、TOST equivalence tests、Bonferroni correction、LOGO cross-validation 贯穿全文。[R2]

**S6. 写作质量。** 叙事结构清晰，从问题定义到方法到结果到 mechanistic interpretation 的逻辑链连贯，语言精练。主文 8 页信息密度高。[R1+R2 共识]

**S7. 格式合规。** 正文 ≤8 页、ACL template、匿名、Limitations/Ethics 齐全。[R2 验证]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [Critical, 共识] **k=2 聚类在 7 个数据点上的 "data-driven" 验证方法学不足。**
DDR 分区是论文核心贡献，但 k-means 聚类对象仅 7 个特征点。对 7 个点做 k=2 聚类在数学上接近 trivial——任何存在基本分离结构的小样本集合都能产生可观的 silhouette。silhouette 从 k=2 (0.632) 到 k=3 (0.499) 到 k=4 (0.571) 的非单调变化在此样本量下不具统计意义。论文 Abstract 和 §4.2 中的 "data-driven clustering" 表述给人以由数据驱动发现的印象，实际上更接近对先验直觉的定量确认。R2 补充指出 Appendix V 的 holdout generator split validation 比 k-means 更有说服力，但当前叙事重心未对准。
→ 建议：(1) 下调 "data-driven" 表述；(2) 将验证重心转向 generator-split consistency；(3) 考虑 per-generator 聚类 (7×8=56 点) 或 permutation test。

**N2** [Critical, 共识] **tail_decay 的 near-stationary 分类证据不足（TOST 仅 4/8 通过）。**
tail_decay 在 ε=0.20 下仅 4/8 generators 通过 TOST，OLMo-2-1B 的 |d|=0.22 超过等价界。论文承认 "genuine boundary case" 但主文仍将其归入 near-stationary 组以维持整齐的二分法叙事（3 drifting + 1 intermediate + 3 near-stationary）。Sensitivity analysis 显示 tail_decay 在 ε=0.25 时才达 7/8 通过率，说明其 near-stationarity 对阈值敏感。R2 建议将 tail_decay 单独降级为 intermediate（3/2/1+1 格局），而非 R1 建议的 3/2/2。
→ 建议：主文更诚实处理 tail_decay 的 boundary status；不应以 neat 二分法遮盖 50% 通过率。

**N3** [Critical, 共识] **与 Markovian Chains (Geng et al., 2026) 的区分度不足。**
Markovian Chains 同样研究 fixed-parameter inference chains 下的 convergence dynamics，核心 setup 重叠度高。当前 §2.2 仅用一句话区分。三种独立方法（Markovian dynamics、information-theoretic loss、DDR feature compression）收敛到 ~3 个可区分深度类——这反而强化了重叠性的质疑。R1 补充："attractor dynamics = location drift" 是过度简化，但需要量化对比。
→ 建议：增加系统性对比表（chain type / feature space / 分析目标 / generator 规模 / 核心 insight）。

### Should-Fix（影响评分但不一票否决）

**W1** [Major, 共识] **Base-model-only scope 与 motivation narrative 存在张力。**
Introduction 引用 "7-17% of scientific publications contain LLM-modified content" 作为 motivation，但这些文本几乎全部来自 instruction-tuned models。Appendix K 显示 instruct models 下 DDR 退化 3.7×（OLMo-Instruct 3-class F1=0.575 vs base 0.754），DDR silhouette 从 0.632 降至 0.338，feature correlations 甚至反转。QLoRA 在 instruct 上恢复到 0.89-0.91，说明 token-level depth signal 存在但 DDR 的 7-feature 分解无法捕获——这本身质疑了 DDR 作为通用 explanatory framework 的地位。R1 评为 Major，R2 评为 Critical。
→ 建议：Abstract 更早限定 scope；Discussion curation 场景限定为 base-model pipeline。

**W2** [Major, 共识] **Five "independent" effect-size metrics 存在 overclaim。**
Cohen's d 和 Glass's Δ 仅在方差处理上不同，KS statistic 也主要捕获 location shift。真正提供独立信息的仅有 Cliff's δ (rank-based) 和 CV shift (relative variability)。"Five independent effect-size metrics" 的表述属于 overclaim。
→ 建议：改为 "five complementary effect-size measures"；区分 parametric overlap 与 genuinely independent perspectives。

**W3** [Major, 共识] **TOST ε=0.20 的 justification 存在循环论证。**
特征先按 d<0.20 分类为 near-stationary → LOFO 验证贡献小 → LOFO 结果 justify ε=0.20。R2 指出 mitigating factor：ε=0.20 对应 Cohen (1988) 的 small effect 传统阈值，非完全 ad hoc。Appendix V 的 partition stability across ε 已部分缓解。
→ 建议：主文承认 ε=0.20 是 conventional 选择；将 Appendix V 的 robustness check 提升到主文引用。

**W4** [Major, 共识] **Downstream null result 未在主文 Discussion 中讨论。**
Appendix M 的 TOST equivalence (depth-aware curation ≈ random subsampling) 直接关系到 §5 中 data curation pipeline 应用叙事，但 Discussion 只字未提。这构成 selective reporting concern。
→ 建议：Discussion 加一段承认 null result；reframe value proposition 从 "improves training" 转向 "data provenance / audit tool"。

**W5** [Divergent: R2 Critical / R1 Rebut] **Shape stability 可能是固定采样机制的 trivial 推论。**
R2 指出 §5 自己承认 top-p truncation preserves functional form，因此 shape stability 不是 emergent property 而是采样机制的直接推论。R1 反驳：(1) 机制可解释 ≠ 经验上 trivial；(2) 温度消融表明 shape stability 在 τ≥0.9 时开始被打破，证明其有边界条件而非无条件成立；(3) 论文提供了两个可检验预测并得到验证。R1 建议区分 mechanistic explanation (post-hoc) 和 empirical contribution (DDR partition)。
→ **分歧保留，记入报告。** 如修改时能明确 shape stability 的成立条件和边界，将大幅缓解此 concern。

### Minor

**M1** [Info, 共识] Abstract 中 "leak-free binary F1=0.694" 未明确 binary 指 gen-1 vs gen-2+（排除 gen-0），而非传统的 human vs machine。建议加 "(gen-1 vs gen-2+, excluding shared gen-0 seeds)"。

**M2** [Info, R1+R2 agree] 14B preliminary evidence 放在 Discussion 正文中，读者可能高估证据等级。建议移至 Appendix。

**M3** [Info, R1] Bootstrap CI 仅反映采样变异性，不反映 generator selection uncertainty（per-generator F1 span 9.1pp）。建议区分 sampling CI 和 generalization variability。

**M4** [Info, R1] Chain depth=4 的选择未在主文中 justify。

**M5** [Info, R2] 5 条 bib entries 存在 first_author mismatch（LaTeX 编码 vs API 索引差异），camera-ready 前应检查。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识 [AGREE]：

1. **k=2 聚类 "data-driven" overclaim** — 7 点 k-means 不构成 principled validation（N1）
2. **tail_decay near-stationary 证据不足** — 4/8 TOST 通过率不支撑分类（N2）
3. **Markovian Chains 区分不足** — 需系统性对比表（N3）
4. **Base-model scope 与 motivation 张力** — instruct 退化严重，Abstract 应更早限定（W1）
5. **Five "independent" metrics overclaim** — 改为 "complementary"（W2）
6. **TOST ε 循环论证** — 有 external justification 但需承认（W3）
7. **Downstream null result 未在主文讨论** — selective reporting concern（W4）
8. **Binary F1 定义模糊** — Abstract 应明确（M1）

---

## Reviewer Divergence

| 问题 | R1 | R2 | 评估 |
|------|----|----|------|
| Shape stability trivial (W5) | REBUT: 有边界条件的经验发现，非 trivial | Critical: top-p 直接推论 | R1 反驳有力（温度消融证据），但 R2 核心论点仍成立——需更明确区分机制解释与经验贡献 |
| Instruct failure severity (W1) | Major: scope 已限定 | Critical: motivation 张力 | 介于两者之间，定为 Major-to-Critical |
| Baseline fairness (R1-W3) | Major: 被超越应更诚实 | Partial rebut: classifier 是 proof-of-concept | R2 反驳有效——DDR 贡献是分解非分类，不降低此 issue severity 但需注意 |
| Entropy terminology (R2-W2) | Rebut: 领域惯例 | Major: 不够精确 | R1 反驳有效——已有显式声明且符合惯例，降为 Minor presentation issue |

---

## Questions（需作者在 rebuttal 中回答）

1. **[高优先级]** 如果将 tail_decay 重新分类为 intermediate，对分类性能和 DDR 核心叙事有何具体影响？能否提供替代分区下的 ablation 结果？
2. **[高优先级]** DDR 的 location drift 与 Markovian Chains 的 attractor convergence 在定量层面是否等价？DDR 是否可被视为 attractor dynamics 的 NLL 特征空间投影？
3. **[高优先级]** QLoRA 在 instruct data 上恢复到 F1=0.89-0.91，但 DDR 7-feature 方法严重退化。QLoRA 在 instruct 上学到的是 DDR features 还是 confound features？这对 DDR 框架的 generality 有何影响？
4. **[中优先级]** 是否测试过不同 top-p 值（如 p=0.5, 0.7, 0.95）下的 shape stability？如果 shape 在 top-p 变化时被打破，支持 "trivial 推论" 解释；反之则支持其作为 non-trivial 发现。
5. **[中优先级]** Downstream null result (Appendix M) 下，depth fingerprinting 的主要应用场景是什么？是否存在现实 pipeline 使用 base model 生成大量文本？
6. **[低优先级]** Gemma-2-2B 的 gen-1 F1=0.036 暗示 DDR 在某些架构上不成立——具体失败模式是什么？

---

## Missing References

两位 Reviewer 均未发现重大遗漏。引用覆盖良好：66 条引用，0 orphan，0 missing。concurrent work (Broken Telephone, Markovian Chains, attractor_cycles) 均已引用。

R2 建议考虑但不要求引用：
- "Variation is the Key: A Variation-Based Framework for LLM-Generated Text Detection" (arXiv:2602.13226, 2026) — 概念联系但研究目标不同

R1 建议加强讨论（非缺失引用）：
- Sadasivan et al. (2024) adversarial robustness findings 对 DDR 的潜在影响
- Kirchenbauer et al. (2023) watermarking 与 depth detection 的关系

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Visual Layout Check（非评分项）

**状态**: done (4 warning, 7 info)

**Warnings:**
1. **Pages 1-4 连续 4 页纯文本无 display item** — 审稿人前 2 分钟只看到密集文字，无法建立视觉锚点。建议在 p.2 前插入概念图/pipeline 图或将核心图前移。
2. **缺少方法概览图 (overview/pipeline figure)** — 作为实证论文，期望在 Method 开始前看到 generation chain → feature extraction → classification 流程的概念图。
3. **Page 7 display items 过度密集** — 2 figures + 1 table 挤在同一页，而相邻 p.4 和 p.8 全是纯文本。建议分散 float 位置。
4. **Pages 8-9 连续纯文本** — Discussion + Conclusion + Limitations + Ethics 连续 2 页无 display item。

**Info:**
- Figure 1 的 8+ 条彩色线在小尺寸下区分度不足
- Figure 2/3 点标记和轴标签字号偏小
- Table 1 CI 列与 F1 列视觉拥挤
- Appendix 中 Figure 4 hapax_ratio y 轴可裁剪
- Figure 8/9 颜色体系不一致
- 正文 8 页仅 5 个 display items（3 fig + 2 table），对实证论文偏少

---

## Overall Assessment

**Overall**: **3.5 (Borderline Conference)**

**Soundness**: 3.5/5 — DDR 核心发现有多重证据支撑且实验控制详尽，但 k=2 聚类验证方法学存在缺陷（N1），tail_decay 部分通过率不足（N2），五个 effect-size metrics 冗余度高于声称的 convergent validation（W2）。

**Excitement**: 3.0/5 — 从 binary detection 到 ordinal depth estimation 的延伸有新颖性，DDR 分解提供了有用的实证框架，但与 Markovian Chains 重叠显著（N3），shape stability 的理论新颖性存疑（W5 divergent），实际应用受限于 base-model-only 约束（W1）。

**Reproducibility**: 4.0/5 — 实验设置详尽，超参明确，Bootstrap CI 贯穿全文。

**Confidence**: 4/5 — 两位 Reviewer 均仔细阅读了全部 33 页（含 20 页附录），交叉验证了引用。

**判断依据**：
- **支持接收的因素**：任务定义新颖（ordinal depth classification 是合理且有价值的研究方向）；实验控制在 empirical study 中属于顶级水平；DDR 分解对后续研究有组织价值；写作诚实且统计方法论自觉。
- **阻碍接收的因素**：核心分区验证（7 点 k-means）方法学薄弱；tail_decay 的 near-stationary 分类仅半数 generators 支撑；与 Markovian Chains 的增量性需更强论证；base-model-only scope 严重限制实际影响力；downstream utility 为 null result。
- **总结**：分析框架新颖且 insight 有价值，但验证方法存在可质疑之处，practical impact 受限于 base-model-only 约束。作为 analytical contribution 足以进入 Findings；若能补强 N1（分区验证）、N2（tail_decay 分类）和 N3（concurrent work 区分），有望达到 Conference 水平。

---

## Detailed Comments

### §1 Introduction
- 第 1 句 "LLM outputs re-enter generation pipelines" 暗示了比 base-model-only 更广的适用性——应更早限定 scope。
- Contribution list 清晰，proof-of-concept 定位到位。但 "data-driven clustering (k=2, silhouette=0.632)" 的表述在 Contribution 1 中需降调。

### §2 Related Work
- Detection 文献覆盖全面。Model collapse 区分到位。
- 与 Markovian Chains 的区分仅一句话（"We study inference chains..."），需要系统性对比表（N3）。
- §2.2 最后一段关于三种方法收敛到 ~3 classes 的讨论是好的学术 contextualization，但应更明确说明 DDR 的独特增量。

### §3 Method
- Task formulation (§3.1) 和 generation chain construction (§3.2) 清晰完整。
- Feature extraction (§3.3) 的 a priori design rationale 合理（dual-view: reference-model + surface）。
- "entropy" 用作 NLL shorthand 已有显式声明且符合领域惯例（R1 反驳有效），但建议将声明移至首次使用处。
- Evaluation protocol (§3.4) 详尽：LOGO + LOFO + binary leak-free metric + length confound control。

### §4 Results
- §4.1 诚实呈现了 gen-0 seed sharing 导致的 3-class F1 inflation，采用 leak-free binary F1 作为 primary metric——good practice。
- §4.2 DDR 分解是论文核心。k=2 聚类验证需补强（N1）；tail_decay 处理需更诚实（N2）；"five independent" 应降调（W2）。
- TOST validation 段落中大样本 power masking 的坦诚承认值得肯定，但 ε=0.20 需 external justification（W3）。
- §4.3 Baseline 比较：4-det+surface 超越 7-feature 时的处理尚可接受（DDR 贡献是分解非分类），但可更诚实。

### §5 Discussion
- Mechanistic interpretation（top-p preserves shape）+ 两个可检验预测是亮点。
- 但需更明确区分 post-hoc rationalization 和 empirical contribution（W5）。
- Data curation pipeline 讨论需提及 downstream null result（W4）。
- 14B preliminary evidence 建议移至 Appendix（M2）。
- Instruct failure 的 mechanistic explanation 不足——是 RLHF reward shaping？SFT format constraints？还是 length regulation？

### §6 Conclusion
简洁到位，与 Abstract 一致。

### Limitations
覆盖全面：base-model scope、scale、prompt-type、temperature、English-only、reference model dependency。是本文最强的章节之一。

### 附录
详尽且组织合理。特别值得注意的优质内容：
- Appendix V (DDR Partition Validation) 的 generator-split consistency 比 k-means 更有说服力——应在主文中更显著引用
- Appendix Z.5 (Token-Level NLL Distribution) 的 kernel density plot 信息密度最高——可考虑将代表性示例提升到主文
- Appendix M (Downstream Utility) 的 null result 必须在主文中讨论
