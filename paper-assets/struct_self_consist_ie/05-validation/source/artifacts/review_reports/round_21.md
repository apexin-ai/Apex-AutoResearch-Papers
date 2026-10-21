---
round: 21
review_mode: 
overall_score: weak reject
timestamp: 2026-05-19T03:51:49.913166+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 22（Fresh Review）

**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Improve LLM-Based Named Entity Recognition
**Venue**: EMNLP 2026 Main Conference (ARR May 2026)
**Deadline**: 2026-05-25
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+叙事完整性+写作质量）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）

---

## Summary

本文系统评估 5 种 confidence signal（4 种 consistency-based + log-probability）在 LLM NER 上的质量估计（QE）和样本选择能力。核心发现为"correlation-selection gap"：所有信号可靠预测输出质量（ρ 高达 0.45, AUROC 高达 0.82），但在 best-of-N selection 上无法持续超越 greedy decoding。论文将此归因于 instance degeneracy 和 LP-quality alignment weakness，并提出 entity-level construction 作为替代方案（SciERC +1.67 pp, Few-NERD +0.88 pp）。实验覆盖 4 个 NER benchmark、2 个模型家族、4B ablation、22 页附录，统计分析极度充分。

---

## Strengths

**S1. 实验设计和统计严谨性远超平均水准。** 4 数据集难度梯度、2 模型家族 + 4B ablation、3-seed stability、bootstrap CI、TOST equivalence testing、power analysis（MDE）、Bonferroni correction。22 页附录涵盖温度消融、N-scaling、epoch confound、free-form 格式、hidden state probe、supervised combination 等。这种严谨程度在 NLP 实证论文中罕见。[R1, R2 共识]

**S2. QE-selection 分离的概念框架有实际指导价值。** 明确区分 quality estimation 和 sample selection 两个任务（§3.1），并实证证明 QE 强不等于 selection 强。Instance-level signal 无法 rank per-sample candidates 的 "by construction" 论证清晰。对部署决策有直接参考意义。[R1, R2 共识]

**S3. 诊断分析链条完整。** Instance degeneracy → LP compression → capability-diversity tension 的诊断逻辑自洽。温度消融（Table 35）提供了更干净的因果测试。Hidden state probe（§4.6）确认信息瓶颈不在 feature engineering 层面，而在 selection 的 diminishing marginal returns。[R2-S3, R1 同意]

**S4. Entity-level construction 提供可操作的正面结果。** LP-weighted entity aggregation 在 SciERC (+1.67 pp, p=0.004) 和 Few-NERD (+0.88 pp, p<0.001) 上显著优于 greedy，提供了 selective prediction 之外的实用方案。Alignment-based gating protocol 虽为初步验证，但方向正确。[R2-S4, R1 同意]

**S5. 写作质量通过 AI 风格硬检查。** 全文无 em-dash (—) 或解释性 en-dash (–)；无 AI 黑名单词汇；无 -ing 短语结尾模式；无过度分段。\textendash 仅用于数值范围，用法正确。[R2-S5]

**S6. Thinking token confound 的诚实处理。** 主动记录 Qwen3 SciERC checkpoint 的 thinking token 问题，并提供三部分反驳论证（LP shift magnitude, constant prefix cancellation, CoNLL control）。[R1-S5]

---

## Weaknesses

### Must-Fix（影响接收决定）

**R22-N1 [critical] 正文再次超页约 2 页（约 10 页 vs 8 页限制）**
- Section 6 Conclusion 结束于 PDF 第 10 页右栏，Limitations 从同页底部开始。ACL ARR 规定正文 ≤ 8 页，当前超出约 1.5–2 页。
- **主因**：Discussion §5 单独占约 2 页；§4.5 Robustness 和 §4.6 Hidden state probe 包含过多细节。
- **注意**：R21-C1 曾 resolved（"Sections 1-6 + Limitations 在 page 8 结束"），但当前版本再次超页，说明后续修改引入了新内容。
- **风险**：Desk reject。ARR 政策明确拒绝超页论文。
- **建议**：Discussion §5 压缩至 ~0.5 页（仅保留核心诊断结论）；§4.5/§4.6 细节移入 appendix；Figure 1+2 考虑合并或缩小。
- [R1, R2 独立发现，交叉一致]

**R22-N2 [critical] 标题与 positive construction result 的叙事矛盾**
- 标题 "Why Confidence Signals **Fail** to Improve LLM-Based NER" 暗示纯 negative result。
- §4.7 entity-level construction 给出显著 positive result：SciERC +1.67 pp (p=0.004), Few-NERD +0.88 pp (p<0.001)。
- Conclusion 也以 construction 和 gating protocol 作为积极贡献结尾。
- 标题与正文之间的矛盾会让审稿人质疑核心贡献定位。
- **建议**：标题应反映完整故事弧。如 "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based NER" 或 "From Selection to Construction: ..."。
- [R1, R2 独立发现，交叉一致]

### Should-Fix（影响评分但不一票否决）

**R22-W1 [warning] correlation-selection gap 概念缺乏理论支撑**
- 本质上是实证观察而非理论贡献。未提供形式化分析解释为什么 QE ρ 高不等于 selection 有效。
- R2 列为 critical，R1 建议降为 warning 并增加简化分析框架。交叉后共识为 warning。
- **建议**：增加简化的 expected gain bound（如在 degeneracy 率 d 下，expected selection gain ≤ (1-d) × oracle_gap），无需完整理论证明。

**R22-W2 [warning] Abstract 中 LP 和 AUROC 缩写未展开**
- LP 在 Abstract line 5 首次出现未定义；AUROC 在 line 4 未展开。
- ACL 规范要求 Abstract 内缩写自包含定义。
- **修复**："log-probability (LP)", "area under the ROC curve (AUROC)"。
- [R2 提出，R1 交叉同意]

**R22-W3 [warning] LP-alignment gating protocol 使用 test set 做 probe**
- §4.7 line 266 承认 "probe instances are drawn from the test set for simplicity"。
- 仅 3 个数据集验证 gating 效果。
- Entity construction 阈值 θ 在 SciERC 上也为 post-hoc (θ=2/N) vs 其他 CV。
- 构成同一类方法论关切：评估与选择之间的 information leakage。
- **建议**：用 validation split 重做，或弱化 claim 为 preliminary proof-of-concept；统一阈值选择为 CV。
- [R2-W3, R1 交叉同意; 与 R22-W5 相关]

**R22-W4 [warning] SciERC 主实验 seed sensitivity 高，统计推断力受限**
- SciERC LP selection 3-seed mean: +0.04±0.48 pp（Limitations line 14），但 main text 主要引用 1-seed 结果。
- n=529, MDE ≈ 1.5 pp at 80% power。TOST 未报告 post-hoc power。
- 核心结论不依赖 SciERC 等价性检验（Few-NERD n=32,565 提供 definitive test），但 SciERC 作为 primary test bed 的 positioning 与其统计功效不匹配。
- **建议**：主文更显著地报告 multi-seed 结果和 seed sensitivity。
- [R1-W3, R2-W4 交叉一致]

**R22-W5 [warning] Entity construction 阈值 θ 跨数据集不一致**
- SciERC 用 post-hoc θ=2/N，Few-NERD/CoNLL 用 5-fold CV。
- Post-hoc 阈值有 data snooping 风险，可能高估 SciERC 的 construction gain。
- **建议**：统一为 CV 或明确标注为 exploratory。
- [R2-Q4, R1 交叉同意]

**R22-W6 [warning] "the correct self-consistency analogy" 措辞过于绝对**
- Contribution 3 和 Abstract 使用 "the correct"。仅在 NER 上验证，CoNLL 上不 work (-0.39 pp)。
- **建议**：改为 "a more effective" 或 "a natural"。
- [R2-W6, R1 交叉同意]

**R22-W7 [warning] 仅测试 LoRA 微调但 claim 范围不限定**
- 所有实验均为 LoRA fine-tuned models。LP compression 可能是 LoRA 特有现象。
- Discussion §5 讨论了 ICL 可能不同，Limitations 承认未测试，但标题/Abstract 未限定。
- **建议**：标题或 Abstract 中限定为 fine-tuned LLMs。
- [R1-W2, R2 交叉部分同意]

**R22-MR1 [warning] 缺失引用**
- Related Work 缺少 ensemble-based NER methods 讨论（与 entity-level construction 直接相关）。
- Xie et al. (2023) self-evaluation beam search、Wan et al. (2024) IE survey 未引用。
- 9 条 bib entry 年份/venue 需复核（hobelsberger2025, lightman2024 等）。
- [R1, R2 分别提出]

---

## Reviewer Consensus [AGREE]

以下问题双方独立发现并在交叉后确认一致：

1. **超页限** — 正文约 10 页 vs 8 页限制，desk reject 风险。[R1-N1 = R2-N1]
2. **标题叙事矛盾** — "Fail" vs entity-level construction positive result。[R1-N3 ≈ R2-N3]
3. **SciERC 统计功效/seed sensitivity** — n=529, 1 primary seed, σ=0.48 pp。[R1-W3 ≈ R2-W4]
4. **Gating/threshold data snooping** — test set probe + post-hoc θ。[R1 Q5-Q6 ≈ R2-W3 ≈ R2-Q4]
5. **实验设计和统计严谨性是核心优势** — 22 页附录、TOST、bootstrap、power analysis。[S1]
6. **QE-selection 分离框架有社区价值** — 可操作的概念贡献。[S2]
7. **定位为 Findings 更合适** — Main Conference 需要更强的正面结果或理论深度。[双方 3.0/5]

---

## Reviewer Divergence [REBUT]

1. **R1-N2 实体匹配标准是否缺失**：R1 列为 critical（定义缺失），R2 反驳称定义完整但分散在 §3.2 各段落中（VC: exact (text, type) tuple; SJ: type-grouped Hungarian matching with token-level IoU; FK: exact string matching; EM: complete output exact match）。R1 未对此反驳进一步回应。**Director 判断**：R2 的证据令人信服，定义确实存在但可读性不佳。降级为 info (R22-I1)，建议增加统一展示表格。

2. **R2-N2 理论深度 critical vs warning**：R2 列为 critical，R1 建议降为 warning（论文定位为 empirical analysis, Findings 接受高质量实证分析）。**Director 判断**：采纳 R1 建议，降为 warning (R22-W1)。增加简化分析框架即可。

3. **R2-W5 Entity-level construction 新颖性**：R2 认为本质是 majority voting，新颖性有限。R1 部分反驳：论文将其定位为分析发现而非方法贡献，新颖性要求应更低。**Director 判断**：R1 的论点合理，但 Abstract 和 Contribution 3 的措辞确实有 overclaim 风险（"the correct analogy"），需调整语气。已包含在 R22-W6。

---

## Questions（需要作者澄清）

**Q1.** Few-NERD LP selection 成功是否本质上是 under-training 的结果？如果 Few-NERD 模型 under-trained（3 epochs vs 5），LP compression 尚未充分发生，LP selection 的 "成功" 可能仅反映模型 calibration 尚未被破坏。Epoch ablation 显示 5-epoch 控制组 LP gains 减半——这是否暗示 LP selection 是 training 不充分的 artifact 而非 dataset 特性？[R2-Q2, R1 交叉同意为有洞察力的假设]

**Q2.** within-instance ρ(LP, F1) 跨数据集能否量化地预测 LP gain？论文宣称 LP-quality alignment 是 primary predictor，但未给出 alignment-gain 的跨数据集相关性数据。如果有 3+ 个数据点的 ρ_within vs Δ_LP 关系，将大幅增强诊断框架的说服力。[R2-Q3]

**Q3.** Greedy (T=0) 与单个 T=1.0 样本的平均 F1 比较如何？如果 T=1.0 单样本 F1 显著低于 greedy，则 selection 面对的是"从 N 个较弱样本中选最好的 vs 一个强样本"的比较，这与"信号无信息量"是不同的 claim。[R1-Q4]

**Q4.** Oracle selection 在哪些类型的 instance 上成功？按实体类型、句子长度、实体密度分层的 oracle-selected vs signal-selected 对比分析，可提供可操作的改进方向。[R1-W4]

---

## Missing References

1. **Ensemble-based IE methods**（如 multi-model voting for NER）——与 entity-level construction 直接相关，Related Work 应讨论。[R1, R2 共识]
2. **Xie et al. (2023)** "Self-Evaluation Guided Beam Search for Reasoning" (NeurIPS 2023)——另一种 per-sample scoring method。[R2]
3. **Wan et al. (2024)** Knowledge Extraction in Low-Resource Scenarios survey (ACL 2024 Findings)——NER/IE LLM 综述。[R2]
4. **9 条 bib entry 需复核年份/venue**：hobelsberger2025, lightman2024, venktesh2025, aggarwal2023 在 OpenAlex 中未找到；feng2025, snell2025, muller2021, park2024, chen2025twofailures 存在轻微不匹配。均可能为索引延迟，但建议核查。[R1]

注：R1 提出的 Kadavath et al. (2022) 已在论文中引用（Related Work §2 line 19, Limitations line 13）。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。

---

## Overall Assessment

**评分：weak reject（Main Conference）/ borderline accept（Findings）**
**置信度：4/5**

| 维度 | 分数 | 说明 |
|------|------|------|
| Soundness | 3.5/5 | 实验方法论扎实，统计严谨，但 gating protocol test-set leak 和 SciERC seed sensitivity 削弱部分结论 |
| Excitement | 2.5/5 | QE-selection gap 的诊断有启发性但缺理论深度；entity construction 增量偏小；诊断性论文定位 Findings 更合适 |
| Reproducibility | 4/5 | 超参数、训练配置、seed 协议详尽，承诺 code release。缺总 GPU hours |
| Overall | 3.0/5 | 实证工作扎实但核心贡献停留在实证描述层面，EMNLP Main 需要更锐利的贡献或更强的正面结果 |

**核心判断**：这是一篇实验极度充分、统计严谨的诊断性论文。QE-selection 分离的概念框架和 entity-level construction 方案对社区有实际价值。但三个因素限制了 Main Conference 竞争力：

1. **格式违规**（超页 ~2 页）是首要障碍，必须在提交前解决。
2. **叙事不统一**（标题暗示纯 negative，但有显著 positive result）会让审稿人困惑核心定位。
3. **Excitement gap**：correlation-selection gap 停留在实证描述层面，缺乏理论支撑；entity construction 是已知技术的应用而非方法创新。

**建议路径**：(A) 修复超页和标题后投 Findings（最稳妥）；(B) 增加简化理论框架 + 限定 claim scope 后投 Main Conference（有竞争力但需要更精确的 positioning）。

---

## Detailed Comments（逐节）

### Abstract
- LP 和 AUROC 缩写需展开 [R22-W2]
- "the correct self-consistency analogy" → "a more effective" [R22-W6]
- 最后一句过长（~50 words），建议拆分 [R2-Minor-2]

### Introduction
- 标题暗示纯 negative result，但 Contribution 3 是 positive [R22-N2]
- Contribution 3 "correct" 措辞需弱化 [R22-W6]
- 与 Yao et al. (2026) 的 3-4 个关键差异应更明确 [R2-W2]

### Method (§3)
- 实体匹配标准分散在各段落中，建议增加统一对比表格 [R22-I1]
- "Soft Jaccard" 命名与标准 Jaccard 有区别，应更明确说明 [R1-W5, R2 反驳认为命名合理，minor]

### Experiments (§4)
- §4.5 Robustness 和 §4.6 Hidden state probe 细节建议移入 appendix 以节省页数 [R22-N1]
- §4.7 gating protocol 应用 validation split 而非 test set [R22-W3]
- Entity construction θ 应统一为 CV [R22-W5]
- SciERC multi-seed 结果应在 main text 显著报告 [R22-W4]

### Discussion (§5)
- 当前约 2 页，是超页主因。建议压缩至 ~0.5 页 [R22-N1]
- 增加简化的 expected selection gain bound [R22-W1]

### Conclusion (§6)
- "a alignment-based" → "an alignment-based" [R22-I2]

### Limitations
- LoRA 限定应更显著 [R22-W7]

### References
- 9 条 bib entry 年份/venue 需复核 [R22-MR1]
- 补充 ensemble-based IE methods 等引用 [R22-MR1]

### Formatting
- \citep 和 \cite 混用需统一 [R22-I2]
- Figure 3 标签在打印尺寸下可能难辨 [R22-I3]