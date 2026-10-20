---
round: 21
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-19T01:34:46.722916+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 21 (Fresh Review)
## Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains
**Target Venue**: EMNLP 2026 (ARR) | **Review Date**: 2026-05-19

---

## Summary

本文提出 generation depth classification 任务，将文本按递归 LLM 生成深度分类为 gen-0/gen-1/gen-2+（超越 binary real-vs-synthetic）。基于 8 个 base model generators（5 families, 0.6B–8B），使用 7 个手工分布特征（reference-model NLL 统计量 + surface lexical diversity）+ XGBoost 分类器，在 LOGO 评估下达到 leak-free binary F1 = 0.694。核心发现是 Differential Depth Response (DDR) 三分法：3 个 drifting features 随深度单调偏移，1 个 intermediate feature 呈非单调 level shift，3 个 near-stationary features 效应可忽略。论文包含大量消融实验（温度、prompt type、跨域、instruction-tuning、下游 utility 等），并诚实报告了多个负面结果。

---

## Strengths

1. **有价值的新研究问题**：Generation depth classification 将 binary detection 扩展为 ordinal depth 维度，提供更细粒度的 provenance 信息。任务定义清晰，形式化合理（§3.1）。

2. **评估协议设计严谨**：LOGO（Leave-One-Generator-Out）和 LOFO（Leave-One-Family-Out）双重交叉验证有效控制了泄漏和家族效应。Leak-free binary F1 排除 gen-0 seed sharing 影响的设计体现了方法论意识。长度匹配子采样、seed-level demeaning、independent-seed 实验形成三层 confound 控制。

3. **分析维度全面**：27 页论文包含 16+ 个附录实验，覆盖温度消融、prompt 类型泛化、instruction-tuning 退化、跨域迁移、下游训练效用、分类器敏感性、特征相关性、TOST 等价检验等，工作量值得认可。

4. **诚实报告负面结果**：下游 curation null result、baseline 集成优于所提方法、instruction-tuning 退化——论文没有隐藏不利证据，体现学术诚信。

5. **可复现性好**：特征定义清晰、数据集构建流程详尽、所有超参和软件版本明确列出、承诺代码/数据/模型开源。

---

## Weaknesses

### Must-Fix 问题（6 个，两位 Reviewer 达成共识）

**MF1** [R1-N1, R2 AGREE] **DDR 三分阈值 post-hoc，缺乏原则性选择依据**
- DDR 将 7 特征划分为 drifting（|ρ| > 0.60）、intermediate、near-stationary（|d| < 0.10），但阈值无理论推导或数据驱动选择过程。论文声称 "shifting thresholds by ±0.10 does not alter grouping"（§4.2），但未给出支持性数据。DDR 是论文的核心 conceptual contribution——阈值任意性直接削弱框架可信度。
- **需要**：阈值 sensitivity analysis（ρ ∈ [0.45, 0.65] 范围内分组稳定性），或 clustering（如 k-means on [|ρ|, d] space）提供数据驱动分组。R2 指出特征间存在天然宽间隔，sensitivity analysis 可能足以化解此问题。

**MF2** [R1-N2, R2 AGREE] **TTR/hapax r=0.97 冗余虚增 "3 drifting features" 声明**
- TTR 和 hapax ratio 测量同一 latent variable（词汇多样性），有效 drifting 维度为 2（entropy mean + lexical diversity），非 3。LOFO 去掉 hapax ratio 仅降低 F1 约 0.43pp。论文在 §4.2 承认冗余但 DDR 叙事仍声称 "three drifting features"（Contribution 2），在 conceptual 层面有误导性。
- **需要**：在 DDR 描述中显式标注 effective dimensionality 约 5（而非 7），或将 TTR/hapax 合并讨论为单一 lexical diversity drifting 维度。

**MF3** [R2-N1, R1 AGREE with nuance] **新颖性增量有限**
- 从 binary 到 3-class 的扩展是渐进的，核心方法（手工特征 + XGBoost）无方法论创新。DDR 三分法本质上重新描述了已知现象的组合（vocabulary diversity decline + distributional shape stability）。R1 补充：根因在于 DDR 框架的方法论不够成熟（post-hoc 阈值、特征冗余），而非简单的 "重新描述"——如果 DDR 有坚实的统计基础，贡献会更有说服力。
- **需要**：论证 DDR 相对于 model collapse 文献和并行工作（Broken Telephone, Markovian Chains）的不可还原新知识点。

**MF4** [R2-N2, R1 AGREE] **下游负面结果与 Introduction 动机存在叙事矛盾**
- Introduction 将动机锚定在 data provenance 和 model collapse downstream implications，但 Appendix L 的 TOST 证明 depth-aware curation 与 random sampling 统计不可区分。§5 退缩到 "diagnostic rather than prescriptive" 定位，构成 motivation-result mismatch。
- R1 补充：TOST 仅 n=3 seeds，统计效力极低，negative result 本身也需审慎表述。
- **需要**：Introduction 重定位为 scientific characterization of recursive generation dynamics，下游作为探索性实验而非核心贡献。

**MF5** [R2-N3, R1 AGREE] **Base-model-only scope 严重限制适用性，Title/Abstract 声明不充分**
- OLMo-2-1B-Instruct LOGO F1 从 0.763 降到 0.338。实际部署的 LLM 几乎全部是 instruction-tuned/RLHF-aligned，方法对此类模型不适用。Title 含 "Base" 但不醒目（末尾从属位置），Abstract 括号限定 "base (pretrained)" 易被忽略。
- **需要**：Abstract 结论句显式加 "for base (pretrained) models" 限定；Introduction 贡献列表加 scope limitation。

**MF6** [R1-N4, R2 AGREE] **温度敏感性严重限制实用性 + 跨域实验温度 confound**
- t=0.9 导致 binary F1 下降 9.3–26.0pp。§5 承认 DDR 是 "parameter-dependent phenomenon"，实质上是 decoding configuration 的函数而非文本 intrinsic property。跨域实验训练 t=0.7 / 测试 t=1.0 引入混淆变量，R2 引用 Appendix O 数据表明跨域性能下降可能大部分归因于温度不匹配（cross-temp F1 从 0.80 降到 0.42）。
- **需要**：跨域实验增加 t=0.7 条件以分离温度和域效应；Limitations 集中讨论温度敏感性。

### Should-Fix 问题（9 个）

**SF1** [R1-N3/R2 partial REBUT] **Baseline 集成优于所提方法的 positioning**：4-det ensemble 3-class F1 领先 7.4pp（0.798 vs 0.724）。R2 认为 §4.3 的 "contextualize" framing 已足够诚实，但同意底层关切：检测分数已隐含编码深度信息，DDR 框架独特价值降低。（降级为 warning，因 Reviewer 间存在分歧）

**SF2** [R2-W1, R1 AGREE] **与并行工作区分不够清晰**：未讨论 DDR 与 Markovian Chains 的 convergence behavior 是否描述同一底层现象。需系统对比表格。

**SF3** [R2-W2, R1 AGREE] **参考模型依赖——DDR partition 可能是 Pythia-410M artifact**：7 特征中 5 个依赖参考模型。Cross-reference F1 spread 0.013 不等于 DDR partition 结构一致。缺少用不同参考模型重新计算 ρ 和 d 验证分组一致性的实验。

**SF4** [R2-W3, R1 AGREE] **生成器覆盖范围窄**：8 models, 0.6B-8B, 无大规模（>10B）或闭源模型。DDR 普遍性 claim 与证据范围不匹配。

**SF5** [R2-W4, R1 AGREE] **正文可能超 8 页限制**：§6 Conclusion 出现在 page 9，正文约 8.5 页，超 ARR Long Paper 8 页限制，可能导致 desk reject。

**SF6** [R2-W5, R1 AGREE with nuance] **特征选择缺乏系统方法论**：7 特征 ad hoc 手工选取，无 feature discovery 过程。DDR 框架可能遗漏重要的 drifting 或 stationary 维度。

**SF7** [R1-W2, R2 AGREE] **XGBoost 默认超参，无超参搜索**：Appendix H 多分类器对比缓和此问题，但未排除调优缩小与 baseline 差距的可能。

**SF8** [R1-W3, R2 AGREE] **TOST n=3 统计效力极低**：下游等价性结论不可靠。低 power 下 "未拒绝差异" 不等于 "证明等价"。

**SF9** [R1-W5, R2 AGREE] **缺少 learned classifier baseline**：QLoRA F1=0.905 vs XGBoost 0.694（+21.1pp），暗示 handcrafted features 是主要瓶颈。Depth classification 可能远比 0.694 暗示的容易，改变对贡献的评估。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成 [AGREE]：
- DDR 阈值 post-hoc（MF1）
- TTR/hapax 冗余虚增特征计数（MF2）
- 下游负面结果与动机的叙事矛盾（MF4）
- Base-model scope 声明不足（MF5）
- 温度敏感性 + 跨域 confound（MF6）
- 所有 9 个 Should-Fix 问题

## Reviewer Divergence

**R1-N3（baseline positioning）**：R1 认为 positioning "不够诚实"，R2 部分反驳——§4.3 开头明确声明 "contextualize rather than claim competitive advantage"，且 Contribution 1 强调任务 formulation 而非性能。但 R2 同意底层关切：检测分数隐含编码深度信息使 DDR 框架独特价值降低。**最终处理**：降级为 Should-Fix（SF1），因 Reviewer 间存在实质分歧。

**R1-W1（entropy_min 归类）**：R2 纠正 R1 的事实错误——"sole intermediate" 特征是 entropy_std 而非 entropy_min。Entropy_min 被归为 near-stationary，其 pooled |ρ|=0.40 完全来自 gen-0/gen-1 跳变，gen-1 vs gen-2+ d≈0。**最终处理**：不列入 weakness。

---

## Questions to Authors

1. DDR 阈值（|ρ|=0.60, |d|=0.10）在什么范围内三分结构是稳定的？是否尝试过数据驱动分组（如 clustering on effect sizes）？
2. 如果将 TTR 和 hapax ratio 合并为单个 lexical diversity 指标，DDR 框架和分类性能如何变化？
3. 跨域实验为什么选择 t=1.0 而非主实验的 t=0.7？是否有 t=0.7 下的跨域结果以分离温度和域效应？
4. QLoRA F1=0.905 远超 XGBoost 0.694——这是否意味着 handcrafted features 是主要瓶颈？DDR 框架的实用意义如何？
5. 5 seeds std<0.001：LOGO splits 是 deterministic 的吗？Seeds 具体控制什么随机性？
6. DDR 的 drifting/near-stationary partition 是否在不同参考模型（如 OLMo, Qwen）下结构一致（不仅是 F1 一致）？
7. DDR 与 model collapse 文献中的理论预测（tail narrowing, mode collapse）有什么具体对应关系？

---

## Missing References

- **SemEval 2024 Task 8 Subtask B**（multi-class detection by generator）：与本文 multi-class 方向直接相关，应在 §2.1 讨论（R2 提出，R1 同意）
- **Model collapse 理论预测与 DDR 的具体对应关系**：§2.2 引用了 Shumailov et al. 和 Dohmatob et al.，但未讨论 DDR 各类别与其理论预测的映射（R2 提出，R1 同意）

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Confidence: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0 | 3.5 | 3.0 |
| Excitement | 3.0 | 2.5 | 2.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |

论文提出了有价值的新研究问题（generation depth classification），实验工作量大且评估协议设计严谨，诚实报告了多个负面结果。但核心 conceptual contribution（DDR tri-partition）存在方法论缺陷（post-hoc 阈值、特征冗余、参考模型依赖未验证），新颖性增量有限（binary→3-class 渐进扩展、手工特征+XGBoost 无方法论创新），且叙事结构存在矛盾（应用动机 vs 下游 null result）。温度敏感性和 base-model-only scope 严重限制实用性。

**Findings track 是合适的归宿。** 如能解决 MF1（DDR 阈值原则性依据）、MF2（特征冗余处理）、MF4（叙事重定位）和 SF5（页数合规），有潜力达到 3.5 Borderline Conference。

---

## Detailed Comments（逐节）

### Abstract
- "base (pretrained)" 限定出现一次但后续叙述未反复强调，快速扫描的审稿人可能误以为通用性。建议在结论句再次限定。
- 数据量值得肯定（37,058 texts, 8 generators, 5 families），但 binary F1=0.694 作为 headline metric 偏低，需要正确 contextualize。

### Introduction
- 动机从 recursive generation dynamics 和 data provenance 切入，逻辑基本通顺。但 §5 的下游 null result 和 instruction-tuning 退化使得 provenance 动机失去后续支撑。建议重构为 scientific understanding of recursive generation。
- Contribution 3 "comprehensive evaluation spanning temperature sensitivity..." 更像工作量描述而非独立贡献。

### Related Work
- §2.1 对 binary detection 覆盖充分（DetectGPT, FastDetectGPT, Binoculars, LD-Score 等），但对 multi-class detection（Beyond Binary, SemEval 2024 Task 8）讨论不足。
- §2.2 与 Broken Telephone 和 Markovian Chains 的对比存在但深度不够——未讨论 DDR 与 convergence behavior 的理论关系。

### Method
- 任务定义（§3.1）清晰、形式化合理。
- 特征选择（§3.3）from "two complementary perspectives" 的 framing 合理但缺乏系统性验证。
- §3.4 XGBoost 默认超参需至少报告 grid search 结果或 learning curve 饱和证据。

### Results
- §4.1 LOGO/LOFO 评估全面，leak-free binary metric 处理 gen-0 overlap 的设计值得认可。
- §4.2 DDR 分析是论文核心，统计量充足（KS, Cohen's d, TOST, Levene, bootstrap CI），但阈值选择和特征冗余问题削弱可信度。
- §4.3 Baseline 对比的 positioning（contextualize 而非 compete）基本诚实，但 7.4pp 3-class F1 差距的 implication（检测分数隐含编码 depth）未充分讨论。
- Table 1 vs Table 2 的 binary F1 不一致（0.694 per-gen macro vs 0.705 pooled）在 caption 中解释但正文段落未提及，可能造成混淆。

### Discussion
- Location/shape 解释标注为 post-hoc 和 empirical，诚实。
- Instruction-tuning 退化讨论充分（3 families, cross-generator 评估），但建议提升为 prominent subsection 而非分散在 §5 和 Appendix。

### Limitations
- 内容全面（base-model scope, temperature sensitivity, scale effect, prompt-type dependency, cross-domain, reference model, 3-class ceiling）。
- 建议将温度敏感性相关内容集中化，避免散落在正文多处。

### Format
- **正文约 8.5 页，超 ARR 8 页限制**——必须在提交前修复。
- 匿名化完整，无 deanonymizing 信息。
- Limitations 和 Ethics Statement 合规。
- 1 条孤立 bib entry (radar) 未被引用。
