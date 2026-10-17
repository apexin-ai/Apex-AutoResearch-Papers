---
round: 32
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-25T21:35:42.761368+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 32 审稿报告

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**Venue**: EMNLP 2026 (ARR May 2026)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人 — R1 方法严谨性, R2 新颖性/完整性
**轮次**: 1 轮（交叉分享后达成共识，无需第二轮）

---

## Summary

本文对 zero-shot LLM 信息抽取中 schema 复杂度的两个维度——type count 和 inter-type confusability——进行受控实证分析。使用基于 embedding 的 Schema Confusability Score (SCS/BCS) 和 BCS-controlled batch 设计，在 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）上实验。核心发现：(1) count 导致跨任务的单调性能退化（最高 -49pp）；(2) BCS 在 FewRel RE 上独立解释约 27% batch-level accuracy 方差（semipartial R² = 0.273）；(3) NER batch-level BCS 无效应（boundary condition）；(4) Schema decomposition (SDGD) 因 merge amplification 和 routing failure 全部失败。

---

## Strengths

**S1. 受控实验设计精巧，填补方法论空白 [共识]**
BCS-controlled batch 方法论是本文最核心的贡献。通过在匹配 type count 条件下构造 low-BCS / high-BCS 对照批次，结合 VIF=1.18 验证正交性，首次在 training-free LLM IE 中隔离 confusability 的独立效应。实验设计在 NLP empirical 论文中属上乘。

**S2. 统计工具链远超同类论文水准 [共识]**
VIF 检查排除 multicollinearity；percentile bootstrap CI 避免正态性假设；cluster-robust SE 处理 batch 内非独立性；TOST equivalence testing 量化交互效应上界；power analysis 诚实报告 NER null 的 65% power。两位 Reviewer 均对此高度肯定。

**S3. 诚实报告负面结果 [共识]**
SDGD 全部策略低于 single-pass baseline；NER BCS null 未回避而给出 power analysis 解释；MAVEN centrality confound 在正文讨论。这种透明度在审稿中少见，显著增强论文可信度。

**S4. Count-degradation 跨任务跨模型稳健 [共识]**
从 NER 到 RE 到 ED，降解曲线在 4 个数据集、4 个模型（Qwen3-32B, Llama-8B, Llama-70B, Gemini Flash）上一致复现。这是对社区有实际价值的 characterization。

**S5. Appendix 质量极高 [共识]**
17 页涵盖 format independence、prompt sensitivity、domain distribution、few-shot interaction、cross-model validation、aggregation simulation 等十余项 robustness check。审稿人几乎所有质疑都能在 Appendix 中找到预先回答。

**S6. BCS 作为 pre-hoc proxy 有实用价值 [R1]**
SCS/BCS 仅需 embedding 计算，无需运行抽取即可预测 schema 难度。跨 embedding 一致性（Appendix I）增强可信度。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1. [critical] BCS 独立效应泛化性严重不足——title 声称 "IE" 但 evidence 仅支撑 FewRel RE [R1-N1, R2 隐式认同]**

逐数据集检查 BCS 独立效应：
- **FewRel** (sentence-level RE): 干净成立 ✓ (VIF=1.18, semipartial R²=0.273)
- **DocRED** (document-level RE): ✗ (VIF=50.9, semipartial R²_BCS=0.056, BCS-centrality r≈0.99 无法分离)
- **Few-NERD** (NER): ✗ (batch-level r=0.069, p=0.219, power=65%)
- **MAVEN** (ED): ✗ (BCS-F1 正相关归因于 centrality confound，控制后信号消失)

4 个数据集中仅 1 个支撑核心 claim。Abstract 已改善（"focusing on RE as primary testbed"），但 title 仍为 "Information Extraction"。按 ARR 标准，framing 与 evidence 的 gap 直接影响 soundness 评分。

→ **修改方向**: Title 限定为 RE 或加 qualifier；§6 RQ1 讨论为什么仅 RE 成立（如 RE 的 pairwise type distinction 更适合 embedding-based confusability 度量）。

**C2. [critical] 核心定量 claim (semipartial R²=0.273) 缺乏跨模型复现 [R1-N2]**

R²=0.273 完全来自 Qwen3-32B 单一模型。跨模型验证仅覆盖 count-curve 和 BCS-controlled accuracy gap，未在任何其他模型上报告完整回归分析（R², β, CI）。Abstract 声称 "replicating across two model families at three scales" 但核心定量指标仅有单模型数据。如果 R²=0.273 是 Qwen3-32B 特有的，核心 claim 不可泛化。

→ **修改方向**: 至少在 Llama-8B 或 70B 上复现 FewRel BCS→accuracy 完整回归，报告 semipartial R² 和 bootstrap CI。

**C3. [critical] SDGD/RQ3 分析深度不足 [R2-N1, R1 交叉认同]**

作为三个 RQ 之一，Section 5 仅约半栏。缺乏：(a) merge amplification 的具体错误模式（type 混淆还是 span 错误？），(b) failure case 分布分析，(c) confidence-gated selection 失败原因的 error analysis，(d) "negative results actionable" 的具体路径。Reviewer 可能认为 SDGD 只是为凑第三个 contribution 草草加入。

→ **修改方向**: Section 5 增加至少半栏 error analysis（merge 后哪些 type pair 产生最多 false positive、SCS 分布、actionability 具体路径）。

### Should-Fix（影响评分但不一票否决）

**W1. SCS/BCS metric 新颖性声明需更清晰界定 [R2-N2]**
SCS 定义（cos embedding similarity）与 LLM-PEE 数学形式完全相同。Contributions #1 将 "SCS/BCS, building on Liu et al." 与 "independently predicts" 并列，读者可能误以为新 metric。论文的真正贡献是实验方法论（BCS-controlled batch + VIF + cluster bootstrap），而非 metric 本身。建议 §3.2 开头明确 "We adopt the pairwise embedding similarity from LLM-PEE"，contributions 中 "building on" 改为 "adopting the metric from"。

**W2. TOST scale 选择存在事后合理化嫌疑 [R1-W1]**
Probability scale TOST 通过 (p=0.003) 但 logit scale 不通过 (p=0.209)。对有界准确率数据，logit scale 是更自然的分析尺度。选择给出有利结论的尺度作为 primary，存在 scale shopping 嫌疑。建议在正文明确报告两个尺度结论并承认矛盾，弱化 "bounded interaction" claim。

**W3. DocRED VIF=50.9 下解读仍偏乐观 [R1-W2]**
VIF=50.9 下标准误膨胀约 7×。论文 Appendix 承认 "impossible to fully separate the two predictors"，但正文 §4.3 仍纳入 "BCS retains predictive value" 的 narrative。建议将 DocRED BCS 结论显式标记为 "inconclusive due to severe multicollinearity"。R31 曾为 Critical，本轮降为 Warning 因论文已有改善（VIF caveat 前置），但仍不充分。

**W4. Ecological inference gap 正文讨论不足 [R1-W4, R2-W1 共识]**
Pairwise r²≈1.5% 到 batch-level R²=27% 的跳跃是论文最关键的统计推理。Appendix N 有 Monte Carlo 模拟，但正文缺少对 ecological fallacy 风险的直接讨论。建议 §4.2 或 §4.3 增加 2-3 句：(1) pair→batch 聚合机制，(2) batch 作为分析单元的合理性（prompt 以 batch 为单位），(3) 指向 Appendix N。

**W5. NER null 解释缺乏实证支撑 [R1-W5, R2-W2 共识]**
"Dispersed error modes" 是事后推测。Observed r=0.069 远低于 minimum detectable |r|=0.132，更接近 "evidence of a very small or null effect" 而非纯粹的 "insufficient power"。建议更平衡地讨论——即使修正 restricted range，NER BCS 效应如存在也远弱于 RE。

**W6. "Two model families at three scales" 表述误导 [R1-W3]**
Abstract 已改为 "two model families"，但 Figure 5 caption 仍说 "three model families"（含 Gemini），全文不一致。Qwen 仅 32B、Llama 仅 8B+70B，非交叉设计，"three scales" 暗示每个 family 均有三个 scale，实际并非如此。建议统一为 "three models from two open-weight families, plus one proprietary model"。

**W7. "Two dimensions" 框架充分性未论证 [R2-W3]**
Schema complexity 可能还包括 type hierarchy depth、argument structure complexity、type definition ambiguity、inter-type dependency 等。§4.5 centrality confound 实际上暗示了第三维度存在。建议在 Introduction 或 Discussion 增加 1-2 句选择理由，承认其他维度为 future work。

---

## Reviewer Consensus [AGREE]

1. **整体评分**: 两位 Reviewer 独立给出 3.5 (Borderline Conference)
2. **统计方法论优秀**: 两人均将统计工具链列为主要优势，在 NLP empirical 论文中属标杆级别
3. **BCS 泛化性有限**: R1 直接论证（逐数据集检查），R2 隐式认同（NER null 限制泛化性讨论）
4. **Ecological inference 需显式讨论**: R1-W4 + R2-W1 共识
5. **NER null 解释不充分**: R1-W5 + R2-W2 共识
6. **负面结果坦诚**: 两人均高度肯定
7. **Appendix 质量**: 两人均列为主要优势
8. **引用真实性**: R2 抽查 7/7 verified，未发现虚构 citation

## Reviewer Divergence

两位 Reviewer 在评分和核心判断上无实质性分歧。差异体现在**关注侧重**而非矛盾立场：

1. **R1 关注 cross-model R² replication (C2)，R2 未独立提出但在交叉中认同**: R2 对 multi-model validation 评价更积极（Soundness 4/5 vs R1 的 3.5/5），但认同 R² 的单模型局限。
2. **R2 将 SDGD 深度列为 Must-Fix (C3)，R1 在初审中列为 Should-Fix**: 交叉后 R1 认同 RQ3 深度不足，接受升级。
3. **R2 将 SCS 新颖性列为 Must-Fix (W1)，R1 在初审中未独立提出**: R1 认为本文贡献是实验方法论，metric 是否新颖是次要问题。两人视角互补。
4. **R2 提出 simpler metrics 对比缺失 (W4)**: 实际上论文 Appendix P (Table 21) 已包含 SCS vs Levenshtein / WordNet / Same-parent 对比，R2 可能遗漏了该 appendix。此项不纳入最终 action items。

---

## Questions for Authors

**Q1** [R1]: 能否在 Llama-8B 或 70B 上复现 FewRel 完整 BCS→accuracy 回归（semipartial R², bootstrap CI）？这是验证核心 claim 泛化性的最直接方式。

**Q2** [R1]: TOST 等价边界 ±3pp 是否 pre-registered？如果使用 ±5pp，logit scale 结论是否改变？

**Q3** [R1]: 是否考虑过在 FewRel 上也控制 relation 在 Wikidata knowledge graph 中的 degree centrality？FewRel 的 BCS 效应是否也部分归因于 structural 属性？

**Q4** [R2]: V2 prompt 下 BCS 效应显著减弱——confusability 是 prompt-induced 还是 schema-intrinsic？如果 prompt 设计如此敏感地影响效应，是否削弱了 "structural property" 的结论？

**Q5** [R2]: Oracle routing (72.4%) 虽高于 single-pass (50.4%)，但仍远低于 solo-type baseline (~85.7%)。Sub-schema 之间的 type overlap 是否导致了系统性问题？

**Q6** [R1]: Task-specific embedding（如 FewRel 训练集微调的 sentence encoder）是否改变 BCS 预测力？这与 SCS 作为 "pre-hoc proxy" 的定位相关——如果最优 BCS 需 task-specific embedding，则 pre-hoc 属性打折扣。

---

## Missing References

**引用真实性**: R2 抽查 7 篇引用均 verified，未发现虚构 citation。

**建议补充**:
1. Hou et al. (2020); Ma et al. (2022) — Label semantics for few-shot NER，使用 label embedding/description 增强 NER，与 SCS embedding similarity 思路直接相关
2. Fei et al. (2022) "LasUIE" (NeurIPS 2022) — Schema structure 对 IE 的影响
3. Lu et al. (2022) "UIE" (ACL 2022) — 统一 IE 建模中 schema 设计问题

**注意**: R2 提出缺少 simpler confusability metrics 对比，但论文 Appendix P (Table 21) 已包含 SCS vs Levenshtein / WordNet Wu-Palmer / Same-parent baselines，SCS 在 FewRel 上显著优于所有 baselines（ρ=0.218 vs 0.097/0.073/0.016）。R2 可能遗漏了该 appendix。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目未启用 `external_review.paperreview_ai`）。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 完成（耗时 ~3.5 分钟）
**统计**: 0 critical, 4 warning, 22 info

**Findings**:
- ✅ 主文 8 页，每页至少 1 个 display item，视觉节奏优秀
- ✅ Figure 1 作为视觉锚点在首页，审稿人第一印象良好
- ✅ 11 个 display items / 8 页主文，密度符合实证论文预期
- ✅ 所有 Figure/Table 均在首次引用后合理位置，无 float 漂移
- ✅ 双栏间距均匀，无 margin 溢出，公式渲染正确
- ✅ booktabs 风格表格，专业
- ⚠️ Figure 7 (SDGD Pipeline) 内部注释文字偏小，打印时可能不易辨认
- ⚠️ Appendix pages 19, 25 多个表格字号压缩至正文 70% 下限
- ⚠️ Appendix G (Prompt Templates) 整页 monospace 纯文本，视觉疲劳较高

---

## Overall Assessment

**评分**: 3.5 / 5 — Borderline Conference
**置信度**: 4/5

**总评**: 这是一篇方法论扎实、统计工具链远超同类论文水准的实证分析论文。BCS-controlled batch 实验设计是真正的贡献，诚实报告负面结果（SDGD 失败、NER null、MAVEN centrality confound）增强可信度。

**核心障碍**在于 claims 与 evidence 的 gap：(1) BCS 独立效应仅在 FewRel 一个数据集上干净成立，但 title/abstract 声称 "Information Extraction"；(2) 核心定量指标 R²=0.273 缺乏跨模型复现；(3) RQ3 (SDGD) 分析深度不足以支撑一个核心 contribution。

**如果 C1-C3 被充分修改**（title 限定、跨模型 R² 复现、SDGD error analysis 扩展），论文可达 Conference (4.0) 水平——受控实验设计的方法论贡献和对 schema complexity 的首个 controlled characterization 值得主会议发表。

**如果作者无法补充跨模型 R² 数据**，建议将核心 claim 限定为 FewRel-specific 发现，论文仍可作为 Findings (3.0-3.5) 接收——方法论框架和负面结果对社区有价值，但贡献范围缩窄。

---

## Detailed Comments

### R31 → R32 跨轮进展

以下 R31 问题在本轮已解决，不再列为 open issues：
- **R31-W3** (domain confound): §4.3 增加 domain entropy covariate (p_entropy=0.97, VIF<2) ✅
- **R31-W5** (FP8 noise power analysis): Appendix 增加 min detectable slope 分析 ✅
- **R31-W6** (unexplained variance): Discussion 增加残差因素讨论 ✅
- **R31-M6** (Monte Carlo ρ sensitivity): Appendix N 增加 ρ=0.20/0.35/0.50 sensitivity ✅

以下 R31 问题在本轮仍然存在或升级：
- **R31-C1** → **R32-C1**: BCS scope framing 仍未充分解决
- **R31-C2** → **R32-W3**: DocRED VIF 从 Critical 降为 Warning（论文已改善但仍不充分）
- **R31-D1** → **R32-W1**: SCS/BCS 新颖性仍需界定
- **R31-W1** → **R32-C2**: 模型多样性从 Should-Fix 升级为 Must-Fix
- **R31-W2** → **R32-W2**: TOST scale 问题持续
- **R31-W4** → **R32-C3**: RQ3 深度从 Should-Fix 升级为 Must-Fix
- **R31-F1** → **R32-W6**: 文内一致性仍有残留

### 格式合规检查

- ✅ ACL review 模板 (`\usepackage[review]{acl}`)
- ✅ Double-blind (Author: Anonymous)
- ✅ Limitations 在正文中（p9, 正文后 references 前）
- ✅ Checklist 不在 PDF 中（注释掉，注明在 OpenReview form）
- ✅ 主文 8 页内（视觉审查确认）
- ✅ Abstract ~160 words (< 200 word limit)
- ✅ AI 使用透明披露 (Appendix Z)
- ✅ Anonymous repo link 提供

### 引用验证

引用抽查 7/7 verified real。未启用系统引用验证。

### 对 R2-W4 的 Director 注记

R2 指出缺少 simpler confusability metrics 对比（Levenshtein, WordNet），但论文 Appendix P (§app:scs-baselines, Table 21) 已包含该对比：SCS vs Levenshtein / WordNet Wu-Palmer / Same-parent，FewRel 上 SCS 显著优于所有 baselines (ρ=0.218 vs 0.097/0.073/0.016)。此项已有论文内回答，不纳入修改要求。