---
round: 15
review_mode: fresh
overall_score: 3.0 Findings
timestamp: 2026-05-21T21:56:56.727719+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints

**Venue**: EMNLP 2026 (ARR May cycle)
**Round**: 18 (fresh review)
**Reviewers**: R1 (方法严谨性+实验充分性), R2 (新颖性+完整性+写作质量)

---

## Summary

本文提出将递归生成深度估计形式化为序数分类，构建 3 模型×3 解码策略×4 深度的 180K 样本基准，使用 19 维统计特征（perplexity 尾部统计量为主）+ Random Forest 分类器进行深度估计，并提出 Effective Discriminable Depth (EDD) 度量。在 1-1.5B 规模 in-distribution 下表现出色（d1-d3: 59-82%），但方法论无创新（标准特征+标准分类器），full-replacement 假设脱离现实，14B 规模下 EDD=0（self-ref 50.8%），跨策略迁移 d1-d3 仅 45.9%。

---

## Strengths

**S1. 任务定义新颖且有实际意义。** 将 AI 文本检测从二分类推进到有序深度估计，与 model collapse 文献直接对接。这一 framing 在现有文献中是新的。[共识]

**S2. EDD 度量设计优雅且实用。** Definition 1 (§3.4) 提供可操作的单一数字量化"深度信号能穿透多远"，与 contraction factor α^d 的理论关联建立了与 model collapse 理论的桥梁。[共识]

**S3. 实验设计系统。** 3×3×4 网格变量控制合理，180K 样本量充分，跨模型/跨策略/跨规模/跨域四个泛化轴全面覆盖。[共识]

**S4. 特征重要性三重验证。** Gini/SHAP/permutation importance 三种方法一致确认 perplexity tail features 主导深度判别（Kendall's W=0.90, p<0.005），跨条件 Spearman ρ̄=0.868。[共识]

**S5. 附录极其详尽。** 17 页 29 个子实验（B.1-B.29），几乎预先回答了所有可预见的 reviewer 问题。诚实报告负面结果（cross-strategy 45.9%、14B EDD=0、DCOL 训练失败）。[共识]

**S6. 引用体系干净可靠。** 75 条 bib entries 验证通过，63 条在线确认，无假引用，4 条 author order mismatch 均为 API 差异。[共识]

---

## Weaknesses

### Critical (Must-Fix)

**C1. 方法论创新不足——标准特征+标准分类器** [R2-N1, R1 AGREE]
19 个特征均非新提出（见于 GLTR/DetectGPT/Ghostbuster），分类器为标准 RF 且无超参搜索（B.29）。论文自我定位为 "benchmark-driven empirical study"（§1），但 EMNLP Excitement 维度要求 "something interesting"——方法层面贡献接近零。R1 认为任务定义本身提供 excitement（Excitement 3.5/5），R2 认为不够（2.5/5），但双方均认同方法论零创新。四个分类器在跨模型迁移下收敛至 0.8pp 以内（§5.1）虽然支持 "feature-determined ceiling" 论点，但也强化了"方法不重要"的印象。

**C2. Full-replacement 假设严重限制生态效度** [R2-N2 critical, R1 升级同意 critical]
整个实验基于 full-replacement chain——每代完全替换训练数据。现实中递归污染几乎都是 accumulation 模式（Gerstgrasser et al., 2024）。论文仅在 §8 Limitations 用一句话提及 pilot accumulation 结果（14-15pp 衰减），无系统实验。Full-replacement 是信号最强的设定，14-15pp 衰减意味着 accumulation 下方法性能可能大幅退化。这不仅是 limitation，而是对论文实际价值的根本性质疑。

**C3. 14B EDD=0——方法在当代模型规模下已失效** [R2-N3, R1 AGREE 并自纠加重]
Self-reference 准确率仅 50.8%（2× chance），EDD=0：连 d0（人类）vs d1（首代生成）都无法区分（d0/d1 AUC=0.56-0.64，均低于 T=0.70；Appendix B.14 Table 17）。Cross-reference 下 EDD=2 但准确率仅 44.1%。14B 已非前沿规模（GPT-4/Claude 远超此量级），EDD=0 暗示方法在更大模型上可能彻底失效。§6 Discussion 对此语气过于轻描淡写，未讨论方法的有效边界在哪里。R1 Round 1 中错误引用 85.8%（实为 50.8%），自纠后认为问题比原先评估更严重。

**C4. 跨策略迁移失败** [R1-N2, R2 AGREE]
d1-d3 跨策略迁移平均 45.9%（Table 6, chance=33%），仅高于随机 13pp。Two-stage pipeline（Appendix B.28）恢复 11.5pp 但最终仍仅 ~57%，远未达到实用水平。实际应用中解码策略通常未知，方法部署场景极为有限。论文动机（Abstract: "yet no method estimates..."）暗示通用性，但证据仅支持 within-strategy 使用。

### Warning (Should-Fix)

**W1. LoRA 链种子不足** [R1-N1 critical → R2 REBUT → 共识降为 warning]
每个 cell 仅一条 LoRA 链（seed=42）。R1 认为无法排除 idiosyncratic artifacts，列为 critical。R2 指出 Appendix B.16 已有 seed=43 的 cross-seed replication（+0.14 to +3.17pp，CI 重叠），初步排除 artifact 可能，建议降级为 warning。共识：2 个种子有限但已初步缓解 artifact 风险，应增加到 3-5 个种子。

**W2. 未进行多重比较校正** [R1-W1, R2 AGREE]
Footnote 3（§3.5）承认 p-values 为 exploratory 未做校正，但主文多处基于未校正 p-value 做确定性声明（如 §4.3 "p<0.001"、§5.1 "p>0.05"）。100+ 统计测试量级，应至少报告 FDR-corrected 结果或做 sensitivity check。

**W3. Neural baseline 对比可能不公平** [R1-W3, R2 部分 REBUT]
仅用 base-size PLMs（DeBERTa-v3-base ~184M, RoBERTa-base ~125M）。R2 指出 B.5 中 DeBERTa-v3-large 因 DCOL 框架数值不稳定而失败（非故意回避），但标准 fine-tuning 的 large 变体未尝试。此外 RF 与 PLM 的信息 access 不同（reference-model perplexity features vs raw text），对比的公平性存疑。

**W4. Binoculars 统计等价削弱独特价值** [R1-W4, R2 AGREE]
Binoculars 11-feature calibrated 达到 78.1% vs 19-feature RF 78.4%（§5.1, p>0.05）。已有方法 calibration 后即可匹敌，19-feature pipeline 的增量价值不清。计算效率差异（单模型 forward pass vs 双模型）未讨论。

**W5. 参考模型依赖性未充分讨论为部署限制** [R1-W5, R2 AGREE]
Pipeline 依赖固定参考模型（Pythia-1.4B）提取特征。跨架构切换导致 4-11pp 下降（B.13），跨规模更大。部署时需选择合适参考模型但论文未提供选择指南。Limitations 未将其列为独立限制。

**W6. 术语不一致** [R2-W3, R1 AGREE]
Title/Abstract 用 "estimation"（暗示连续值预测），§3.1 定义为 "ordinal classification"。全文交替使用两个术语。应统一或在首次出现时声明等价。

**W7. Downstream curation PoC 不足** [R2-W4, R1 AGREE]
Appendix B.22 的 PoC 过于 toy（Pythia-410M, 单种子, PPL 变化 0.03-0.12, 不显著 p>0.4）。§6 "depth-aware curation" 主张与 evidence 力度不匹配。

### Minor

**M1.** d0 样本是否跨 cell 共享未显式声明 [R2-M1, R1 AGREE]
**M2.** Table 2 主表未报告 CI/std，仅在文字中零散提及 [R2-M2, R1 AGREE]
**M3.** §3.5 "Theoretical Grounding" 标题过大，内容为 post-hoc motivation [R2-M3, R1 AGREE]
**M4.** \cite/\citet 格式不一致 [R2-M4, R1 AGREE]
**M5.** VIF>10 的 14-16/19 特征，实际独立维度 ~4-5，应在 §3.3 更早提及 [R1-M1, R2 AGREE]
**M6.** 生成长度固定 512 tokens，B.18 显示 128 tokens 时 accuracy ~66%，短文本推广未讨论 [R1-M3]
**M7.** RF 无超参搜索（B.29 确认），200 trees 为默认值 [R1-M2]

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全一致：
1. **Overall 3.0 (Findings)** — 独立给出相同评分
2. **任务定义是最重要的贡献** — EDD 度量有独立价值
3. **14B EDD=0 构成核心叙事威胁** — self-ref 50.8% 无法区分 d0/d1
4. **Cross-strategy 45.9% 是实用性的主要障碍** — 策略未知时方法接近失效
5. **Accumulation 是最大实验缺口** — full-replacement 结论无法直接推广
6. **方法论无创新** — 标准特征 + 标准分类器
7. **引用体系干净** — 无假引用

---

## Reviewer Divergence [REBUT]

**1. LoRA 种子严重程度**：R1 列为 critical，R2 提供 B.16 证据 REBUT 并建议降为 warning。R1 未在交叉回应中直接反驳。**结论：降为 warning。B.16 初步排除 artifact 但 2 个种子统计功效不足。**

**2. Excitement 评分**：R1 给 3.5/5（任务定义新颖性驱动），R2 给 2.5/5（方法零创新压制 excitement）。R1 REBUT R2-W2 指出 strategy > model effect 和 cross-ref 提升 EDD 是 non-trivial findings。**结论：分歧合理，反映 task novelty vs method novelty 的权重偏好。合并取 3.0/5。**

**3. Soundness 评分**：R1 给 ~2.5-3.0/5（实验 gap），R2 给 3.5/5（受限条件下执行质量高）。**结论：两者视角互补。合并取 3.0/5。**

**4. Benchmark study 定位**（R2-W2, R1 REBUT）：R2 认为三个 findings 不 surprising；R1 指出 strategy > model effect 和 cross-ref 提升 EDD 是 non-trivial findings，引用 EMNLP 接受 benchmark 论文先例。**结论：benchmark study 在 EMNLP 可接受但需更强的 surprising insight。不列入合并 weakness。**

**5. Figure 1 信息密度**（R2-W5, R1 REBUT）：R2 认为偏低浪费空间，R1 认为任务定义图的信息密度适当。**结论：分歧不影响评分，不列入合并 weakness。**

---

## Questions for Authors

**Q1.** [共识] Accumulation 模式下的系统性实验结果？至少一个模型在 25/50/75% 混合比例下的 EDD？
**Q2.** [共识] 14B 能否用同族不同规模模型（如 Pythia-6.9B）分离 self-reference vs scale effect？
**Q3.** [共识] Binoculars in-distribution 等价——19-feature pipeline 的具体优势场景？计算效率差异？
**Q4.** [共识] 是否探索过策略不变特征子集以改善 cross-strategy transfer？
**Q5.** [R2] 19 特征中有多少是本文首创的？
**Q6.** [R1] 为什么不做多重比较校正？关键结论在 FDR 校正后是否仍显著？
**Q7.** [R2] 两阶段 pipeline 的策略分类阶段准确率是多少？
**Q8.** [R1] B.16 的 2 个 LoRA 种子是否足够？是否有更多种子的实验？

---

## Missing References

**共识推荐：**
- Carlini et al. (2021) "Extracting Training Data from Large Language Models" — data provenance motivation [R1 标注为最重要缺失]
- Rothe et al. (2018) "Deep ordinal regression" — ordinal classification 方法论 [R2 推荐, R1 同意]

**建议补充：**
- Guo et al. (2025) "Generative AI May Prefer to Present Scientific Uncertainties as Certainties"
- Li et al. (2024) "Synthetic Data (Almost) from Scratch"

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿。

---

## Visual Layout Check（非评分项）

视觉审查已完成（3 warning, 7 info, 0 critical）：

**Warnings：**
- pp.1-2 连续两页纯文本无 display item，审稿人第一印象 text-heavy。建议提前 Figure 1 或加 teaser
- p.8 极度拥挤——4 个 display items（Table 4, Figure 4, Table 5, Table 6）+ 4 个章节（§5.2/5.3/5.4/6）。建议移部分表格至 Appendix
- p.7 Figure 2 feature importance heatmap 内部字体偏小，打印可读性受影响

**Info：**
- Figure 3 仅用颜色区分线条，缺 line style/marker 辅助（灰度/色盲不友好）
- Figure 4 混淆矩阵尺寸偏小
- Tables 2/3 booktabs 格式规范 ✓
- Table 1 排版清晰 ✓
- References 格式统一无 [?] ✓
- Appendix 表格格式与正文一致 ✓

---

## Overall Assessment

**Overall: 3.0 (Findings)**

**置信度: 4.5/5** — 两位 Reviewer 独立审稿后达成完全一致的评分，交叉讨论解决了主要分歧。

**评分依据（EMNLP 2026 ARR 标准）：**

| 维度 | 合并评分 | 理由 |
|------|----------|------|
| Soundness | 3.0/5 | 在受限条件下（1-1.5B, in-distribution）实验质量高，但 14B EDD=0、cross-strategy 45.9%、limited seed chain、无 accumulation 系统实验构成显著缺口 |
| Excitement | 3.0/5 | 任务定义有价值（R1: 3.5），但方法论零创新压制（R2: 2.5），取中值 |
| Reproducibility | 3.5/5 | 超参报告完整（B.29），特征定义清晰，承诺释放代码。LoRA 种子有限降低完全复现信心 |

**总评：** 论文提出了有价值的新任务（递归深度估计）和实用度量（EDD），在 1-1.5B 规模 in-distribution 条件下提供了详尽的实证刻画。但四个 critical 问题——方法论无创新（标准特征+RF）、核心假设脱离现实（full-replacement）、方法在 14B 规模已失效（EDD=0）、跨策略迁移接近失效（45.9%）——叠加使论文达不到 Conference（4.0）门槛。作为 Findings（3.0）论文，任务定义的原创性、EDD 度量的价值、引用和实验的高质量执行支撑其发表。

**达到 Conference (4.0) 所需：**
1. 至少一组系统的 accumulation 实验（25/50/75% 混合比例下的 EDD）
2. 14B 使用同族参考模型（如 Pythia-6.9B）分离 self-reference confound
3. 引入一个 non-trivial 方法改进或 surprising finding 提升 Excitement

---

## Detailed Comments

### Abstract
- 数字密度适中（~6 个关键数字），"three findings" 结构清晰
- 14B 结果呈现准确（EDD=2, cross-reference 条件），但应更显著标注规模限制

### §1 Introduction
- 动机推进自然（model collapse → binary detection → depth estimation）
- "benchmark-driven empirical study" 定位诚实但限制论文上限
- 贡献 3 正确标注 cross-strategy 为 boundary condition

### §2 Related Work
- 覆盖全面，组织清晰
- 缺 Carlini et al. (2021) 作为 data provenance 补充
- 与 GLTR 的关系（同用统计特征，不同任务定义）应更明确讨论

### §3 Method
- Problem definition 和 EDD 定义（Definition 1）清晰
- T=0.70 有 Hosmer &amp; Lemeshow (2000) justification
- "Theoretical Grounding" 标题过大——改为 "Theoretical Motivation"
- 19 特征的 VIF>10 多重共线性应在 §3.3（而非 §4.2）首次提及
- LoRA 链单种子应在主文显式声明并讨论影响

### §4 Depth Degradation Atlas
- Table 2 主要结果清晰但缺 CI
- §4.2 特征重要性分析扎实（三重验证）
- §4.3 EDD 分析是论文最精彩部分——AUC decay curves 直观有力
- Figure 2 heatmap 字体偏小，影响打印可读性

### §5 Generalization and Robustness
- §5.1 Binoculars 等价结果需在主文更充分讨论（计算效率差异、具体优势场景）
- §5.3 Cross-strategy 45.9% 应更 prominently 讨论对实用性的影响
- §5.4 "Preliminary" 定位适当，但 14B EDD=0 的含义（方法有效边界、是否存在参数量阈值使统计指纹方法不可行）讨论严重不足

### §6 Discussion
- 深度不足——缺乏 "why does signal attenuate with scale?" 的机制分析
- Curation 主张过于 speculative（p>0.4 evidence, B.22 PoC 不显著）

### Limitations
- 覆盖了 full-replacement vs accumulation 和 scale boundaries
- 遗漏：仅英文文本、仅 Wikipedia seed corpus、仅 LoRA fine-tuning、参考模型依赖作为独立限制

### 格式合规
- 主文 8 页 ✓
- 匿名合规（"Anonymous ACL submission"）✓
- 引用格式基本规范（natbib）✓
- Ethics Statement 合规 ✓
- Limitations 长度合适 ✓