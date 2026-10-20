---
round: 45
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T08:34:32.529818+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 45 (Fresh Review)

**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text
**Venue**: EMNLP 2026 (ARR)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人 — R1 (方法严谨性/实验设计/统计检验) + R2 (新颖性/完整性/写作质量)

---

## Summary

本文提出 depth profiling——对 base-model LLM 文本的递归生成深度进行 ordinal classification（gen-0/gen-1/gen-2+）。核心发现是 DDR（Differential Depth Response）分解：7 个统计特征按深度响应分为单调漂移的 location 组（entropy mean, TTR, hapax ratio; Cohen's d=0.76–1.17）和近似稳定的 shape 组（entropy max/min, tail decay; d<0.10），中间有一个 intermediate 成员（entropy std; d=0.55）。在 37K 文本、8 generators、5 families 的数据集上，LOGO 交叉验证下 XGBoost 7-feature ensemble 达到 leak-free binary F1=0.694（gen-1 vs gen-2+）、3-class macro F1=0.762；QLoRA 端到端分类器在 6-generator 子集上达到 3-class F1=0.905。

---

## Strengths

**S1. 问题定义的原创性** [共识]
Depth profiling 将 AI 文本检测从 binary human-vs-machine 扩展到 ordinal depth classification，填补了明确的研究空白。任务动机（data provenance, corpus curation）清晰，与现有检测工作的区别有说服力。

**S2. DDR 分解是高质量的实证发现** [共识]
Location drift vs shape stability 的不对称性通过 5 种效应量指标（Cohen's d, Glass's Δ, Cliff's δ, KS, CV shift）、k-means 聚类验证（silhouette=0.660, p=0.030）、per-generator replication（8/8 独立恢复相同 partition）、TOST 等价性检验多维度验证。方法论严谨性在同类 empirical study 中属上乘。

**S3. 评估协议设计严谨** [共识]
LOGO（Leave-One-Generator-Out）是最严格的跨 generator 泛化测试；leak-free binary metric 正确规避 gen-0 seed 共享问题；配套控制实验系统性地排除主要 confounds（length confound: F1=0.724 vs 0.770; independent seed: F1=0.680; cross-reference: spread=0.013）。

**S4. 诚实的 scope characterization** [共识]
论文坦诚报告了 instruction tuning 的失败（Appendix k）、Gemma-2-2B anomaly（Appendix z.5）、downstream utility 的 null result（Appendix m）、high-temperature 下的性能下降。这种 honesty 在投稿论文中不常见。

**S5. 极为充分的实验覆盖** [共识]
37 页、25+ 附录 section，覆盖 temperature sensitivity、prompt type、domain transfer、perturbation robustness、instruction tuning、QLoRA、finer depth、feature ablation、confusion matrix、error analysis、downstream utility、cross-temperature、DDR causality、decoding strategy 等。附录覆盖度在同类论文中极为罕见。

**S6. 基线对比框架公平** [共识]
4 个检测基线（Avg-LogProb, FastDetectGPT, Binoculars, LD-Score）接入同一 XGBoost/LOGO 框架，避免分类器差异 confound。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [Critical] **Instruction tuning 大幅削弱 DDR，限制论文核心实用价值** [R1-N2 + R2-N1, 共识]
- Appendix k: 3-class F1 下降 3.7–19.9pp (Table 18); retrained binary F1 仅 0.487 (Table 19); DDR silhouette 从 0.660 崩至 0.372 (Figure 7)
- 论文动机（data provenance, corpus curation）依赖于方法可应用于实际 LLM 输出，但实际输出几乎全部来自 instruction-tuned model
- Discussion §5 的两个 testable predictions 和 Conclusion 的 "open challenge" 暗示方法可推广，与实证结论不一致
- QLoRA 在 instruct data 上恢复到 0.89-0.91 说明 depth signal 存在但 DDR 特征表征不足——limitation 在于 DDR 分解而非 depth 信息本身
- **建议**: Introduction 更早限定 scope（目前 base-model 限定出现在 para 5 偏后）；Discussion 量化说明 instruct 影响并 temper extensibility claim；将 motivation 从 "corpus curation" 调整为 "base-model generation dynamics analysis / provenance auditing"
- **跨轮追踪**: 此问题从 Round 34 持续至今（R34-W1, R42-N2），12 轮未充分修复

**MF2** [Critical] **QLoRA 6-gen F1=0.905 与 8-gen 主实验不可比，Abstract 并列呈现存在误导** [R1-N1 + R2-W4, 共识]
- Abstract 并列 binary F1=0.694（8-gen LOGO）和 3-class F1=0.905（6-gen LOGO），虽标注 "(6-gen LOGO)" 但容易被忽略
- 6-gen 子集排除了 Mistral-7B（binary F1=0.633, 最弱）和 Qwen3-8B（F1=0.692），是对方法更友好的子集
- Appendix e 脚注自承 "Not directly comparable to 8-generator LOGO due to differing subsets"
- **建议**: (a) 在 8-gen 完整集上运行 QLoRA LOGO 并报告结果；或 (b) Abstract 优先报告 8-gen LOGO 3-class F1=0.762，将 QLoRA 0.905 作为附录补充；或 (c) 至少明确标注两个数字的评估条件差异
- **跨轮追踪**: R43-W2, R44-W1，持续 3 轮

### Should-Fix（影响评分但不一票否决）

**SF1** [Major] **Binary F1=0.694 的实际可用性论证不足 + downstream null result 呈现不当** [R1-W2 + R2 交叉同意]
- ~30% 错误率在什么应用场景下足够有用？论文未充分论证
- Downstream utility (Appendix m) 的 TOST 确认等效性实际上是 null result（depth-stratified curation 未优于 random），但 Discussion §5 仍用 "may serve as a prophylactic against model collapse" 的正面措辞
- **建议**: Discussion 应弱化 "operational dimension" claim，将 downstream null result 更显著纳入，将 motivation 聚焦 "provenance tracking / contamination estimation"

**SF2** [Major] **3-class resolution ceiling claim 措辞过强** [R2-N2, R1 部分同意]
- 5-class F1≈0.50 远高于 random 0.20，说明残余深度信号存在
- R1 反驳：QLoRA 端到端也≈0.50，支持信号层面 ceiling（非仅特征集 ceiling）
- **共识**: 结论方向正确（3-class 是当前 practical limit），但措辞 "resolution ceiling" 带有 information-theoretic 含义过强，应改为 "practical resolution limit under current approaches"
- **跨轮追踪**: R39-N3, R42-W6，持续 7 轮

**SF3** [Warning] **Nucleus sampling 假说 "both confirmed" 措辞过强** [R2-W1, R1 同意]
- §5 的两个 predictions（τ=1.0 correlation collapse; elaboration prompt F1 drop）仅 consistent with 假说，不构成因果验证
- τ=1.0 下的 correlation 崩溃可用 "高随机性掩盖所有系统性信号" 解释，不需要 nucleus sampling 特异性
- **建议**: 改 "both confirmed" 为 "both consistent with the hypothesis"；明确承认替代解释

**SF4** [Warning] **Concurrent work 三方收敛讨论不足** [R2-W2, R1 同意]
- 本文 DDR、Geng et al. (2026) Markovian dynamics、Mohamed et al. (2025) information loss 三项独立工作收敛到 ≈3 distinguishable classes，是重要 meta-finding
- 目前仅在 Appendix z.6 (Table 46) 列元数据对比，Discussion 正文缺 finding-level 讨论
- **建议**: §5 用 1-2 句突出三方收敛的意义——强化 3-class limit 作为递归生成过程本身属性的论点

**SF5** [Warning] **Entropy 术语可能造成混淆** [R2-W5, R1 同意]
- §3.3 声明 "entropy" 指 reference-model NLL（cross-entropy），但此后全文持续使用 "entropy_mean" 等术语
- 仅一段 disclaimer 不够，快速阅读的 reviewer 可能误以为是 information-theoretic entropy
- **建议**: Table 1 caption 再次标注 "(ref-model NLL-based)"；或考虑 feature 改名为 nll_mean 等
- **跨轮追踪**: R32-W3，持续 14 轮未修复

**SF6** [Warning] **Gemma-2-2B 异常应在主文提及** [R1-W5, R2 同意]
- 1/8 generator 大幅低于平均（binary F1=0.633, 3-class 最弱），当前仅在 Appendix z.5 讨论
- 对 "cross-generator generalization" claim 构成实质性限制
- **建议**: §4.1 或 Discussion 用 1-2 句提及此异常

**SF7** [Warning] **Seed-sharing 间接泄漏应在正文报告 conservative estimate** [R2-N3, R1 部分同意降级]
- Independent-seed F1=0.680 vs shared-seed 0.694，1.4pp 差距在 bootstrap CI 内但非零
- R1 降级为 Minor（主指标已排除 gen-0，差距在 CI 内）
- **建议**: §4.1 加一句 "conservative independent-seed estimate: F1 = 0.680"

### 小问题（不影响接收）

1. Figure 1 灰度打印下可读性有限，建议为 stationary 系列增加虚线或不同 marker [R2-W6, R1 同意]
2. Ordinal classification 文献连接薄弱——CORAL/Frank-Hall 表现与 XGBoost 相当的 negative result 值得在 Related Work 或 Discussion 讨论 [R2-W3, R1 同意]
3. Perturbation robustness "survives moderate perturbation" 措辞需精确化——5% replacement 已造成 ~4pp drop [R1-W4, R2 同意]
4. Table 2 和 Table 3 使用不同 F1 计算方式（per-generator macro vs pooled），增加认知负担 [R1+R2]
5. PyTorch 2.10.0 (CUDA 12.8) 版本号请确认准确性 [R2]
6. Reference model tokenizer 兼容性（32K vs 128K vocab）未在 Limitations 讨论 [R1-W3, R2 认为现有数据已回应主论点]

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全达成共识：

1. **Instruction tuning 限制是核心 concern**（MF1）——DDR 在 instruct model 上结构性失效，论文 framing 需调整
2. **QLoRA 6-gen vs 8-gen 可比性**（MF2）——Abstract 并列呈现存在误导，需更透明标注
3. **Nucleus sampling "both confirmed" 措辞过强**（SF3）——应改为 "consistent with"
4. **Concurrent work 三方收敛值得在 Discussion 突出**（SF4）
5. **Entropy 术语混淆**（SF5）——14 轮未修复
6. **Gemma anomaly 应在主文提及**（SF6）
7. **DDR 分解是高质量 empirical finding**——任务定义新颖，统计方法论严谨
8. **Downstream null result 应更诚实地呈现**——"prophylactic against model collapse" 措辞与实证不一致

---

## Reviewer Divergence [REBUT]

两位 Reviewer 存在程度分歧的问题：

1. **3-class ceiling claim**（SF2）：R2 认为可能是特征集 ceiling（Major），R1 认为 QLoRA 也≈0.50 支持信号层面 ceiling（partial rebut）。**共识**: 保留 ceiling 结论但弱化措辞为 "practical resolution limit"。

2. **Seed-sharing 严重程度**（SF7）：R2 列为 Major，R1 降级为 Minor（1.4pp 在 CI 内，主指标已排除 gen-0）。**共识**: 报告 conservative estimate 但不改变核心结论。

3. **DDR 阈值 sensitivity**：R1 要求 d ∈ {0.40–0.60} sweep，R2 反驳认为 Appendix v (Table 33) 已提供 ε∈[0.10,0.75] 完整扫描且 partition 在所有阈值下 stable。**结论**: 现有数据已回答 R1 concern，仅 presentation 可改进。

4. **Reference model 依赖性**：R1 列为 Major（tokenizer 兼容性），R2 反驳（cross-reference F1 spread=0.013 + surface-only F1=0.688 已回应主论点）。**结论**: 补充 tokenizer 讨论合理但不升级为 Major。

---

## Questions to Authors

1. QLoRA 端到端分类器是否可在完整 8-gen 集上运行？如果计算资源有限，可否至少报告 Mistral-7B 和 Gemma-2-2B 作为 hold-out 时的 F1？
2. DDR 在 instruction-tuned models 上的崩溃是否主要由 RLHF/DPO 引起？是否测试过仅做 SFT（无 reward modeling）的模型？
3. Downstream utility 的 null result 如何解读——depth profiling 的实际应用是否应聚焦 provenance tracking 而非 training data curation？
4. 3-class ceiling 是否在更丰富的特征集（如 full NLL distribution 的非参数统计、n-gram level features）下仍然成立？
5. DDR partition 在不同 prompt template 下是否保持一致？Appendix c 报告了分类 F1 但未报告 per-feature Cohen's d。
6. Cross-model chains 的 F1 提升（+2pp over single-generator LOGO）是否因 generator diversity accumulation 而非纯粹的 depth signal？

---

## Missing References

两位 Reviewer 均认为参考文献覆盖较为完整（74 篇）。建议补充方向：
- Ordinal classification 在 NLP 中的应用（如 sentiment ordinal classification），与论文的 ordinal task framing 相关
- DetectGPT (Mitchell et al., 2023) 与 DDR shape feature 的方法论对比价值可在 Related Work 强化

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目配置中未启用外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: ✅ 已完成

| 严重程度 | 数量 |
|---------|------|
| Critical | 1 |
| Warning | 4 |
| Info | 7 |

**关键发现**:
- **[Critical]** 最后一页（p.37）大面积空白（~60%），Figure 15 孤立放置，上方完全空白——审稿人翻到末页印象极差
- **[Warning]** Pages 1-2 连续纯文本无 display item，审稿人前 2 分钟无视觉锚点（跨轮持续标注，已标为 wont_fix: 8 页预算极紧）
- **[Warning]** Abstract/Intro 引用 Figure 2（DDR）但直到 page 7 才出现，float 漂移严重
- **[Warning]** Figure 1 是论文第一个 figure 但出现在第 6 页
- **[Warning]** Page 24 底部约 1/3 空白
- **[Info]** 主文 6 个 display items 在 8 页中属可接受范围下限；Tables 2,3 booktabs 风格专业；Figure 5 confusion matrix 清晰可读

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference**
**Reviewer Confidence: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 4/5 | 3.5/5 | 3.75/5 |
| Excitement | 3/5 | 3/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.5 | 3.5 | **3.5** |

**核心判断**:

DDR 分解（location drift vs shape stability）是一个扎实且新颖的实证发现，任务定义有明确的学术价值，实验设计和统计方法论在同类 empirical study 中属上乘。37 页附录的实验覆盖度极为罕见，诚实地报告了 negative results。

**限制论文评分的核心因素**:
1. **Base-model-only 适用范围**（MF1）: DDR 在 instruction-tuned model 上结构性失效（silhouette 0.660→0.372, retrained binary F1=0.487），而实际 LLM 输出几乎全部来自 instruct model。论文的 data provenance/corpus curation 动机与 base-model-only 实证之间存在 scope-motivation mismatch。
2. **QLoRA headline 数字可比性**（MF2）: F1=0.905 在对方法更友好的 6-gen 子集上评估，与 8-gen 主实验不可直接比较。
3. **分类性能绝对水平**（SF1）: Binary F1=0.694（~30% 错误率）不构成 strong practical tool；downstream utility 为 null result。

**如果作者能充分 address MF1+MF2**（调整 Introduction scope framing + 提供 8-gen QLoRA 结果或透明标注），论文适合 **EMNLP Findings**（3.0–3.5）。如果能进一步提供 instruct model 的 DDR 结构化分析（即使是 negative result 的系统分析），有潜力升至 **Borderline Conference**（3.5）。

当前版本: **3.5 Borderline Conference** — 主要基于 DDR 发现的质量、实验 rigor 和诚实的 scope characterization，但 practical scope 限制和 QLoRA 可比性问题阻止更高评分。

---

## Detailed Comments

### Section 1 Introduction
- Para 1 的 data provenance/corpus curation 动机与 base-model-only 实验存在 tension（MF1）。建议更早（para 1-2）限定 scope 而非 para 5 才提及 base model。
- Contribution 3 "Scope characterization" 是一个 strength——honest about operational boundaries。

### Section 3 Method
- §3.1 Task Formulation: gen-2+ 合并方案的实证支撑充分（5-class F1≈0.50, Appendix d）。
- §3.2 Generation Chain Construction: shared seeds 的 rationale 应在首次出现时明确说明。
- §3.3 Feature Extraction: "entropy" 术语歧义问题持续 14 轮（SF5），建议 Table 1 caption 加 "(ref-model NLL-based)" 标注。

### Section 4 Results
- §4.1: 建议加 independent-seed conservative estimate (F1=0.680) 作为一句 robustness bound。
- §4.1: QLoRA F1=0.905 的 6-gen 评估条件需更显著标注或在 8-gen 上重新评估（MF2）。
- §4.2 DDR: partition 验证充分（k-means, holdout, TOST, per-generator replication）。Appendix v 的 threshold sweep 已回答 sensitivity concern，建议在主文加 1 句引用。
- §4.3: DDR 7-feature F1=0.705 与 4-det+surface F1=0.708 持平——论文正确定位 DDR 贡献在分解洞察而非性能优势，但可更明确。

### Section 5 Discussion
- "both confirmed" → "both consistent with"（SF3）
- 加 1-2 句 concurrent work 三方收敛讨论（SF4）
- "may serve as a prophylactic against model collapse" 与 Appendix m null result 不一致（SF1）
- 加 instruct model DDR 失效的量化说明（MF1）

### Section 6 Conclusion
- "extending DDR to instruction-tuned and frontier-scale models remains the key open challenge" 准确但应配合 Discussion 中的 instruct 量化数据，避免暗示近期可行性。

### Limitations
- Gemma-2-2B anomaly 应更突出（SF6）
- 建议补充 tokenizer 兼容性讨论（Minor）
- English-only 限制应作为独立 limitation point

### Appendix
- 覆盖度极高，是论文的重要 strength
- Appendix m downstream utility 应更明确标注为 null result
- 25+ sections 中部分内容有重复（DDR validation 出现在多处），可考虑合并
