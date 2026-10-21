---
round: 8
overall_score: 3.0 Findings
timestamp: 2026-05-18T08:07:49.063405+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 9 审稿报告

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 (ARR May cycle)
**投稿类别**: Findings
**Reviewers**: R1 (方法严谨性), R2 (新颖性/完整性)
**轮次**: Round 9 (fresh review)
**外部审稿**: 未配置，跳过

---

## Summary

本文对四个推理模型（R1-8B, OT-7B, QwQ-32B, R1-32B）进行了 hidden-state (HS) 与 text-based probe 在 safety commitment 检测上的系统对比。核心方法论发现是 layer selection metric 的选择（尤其是包含 crossing rate 的复合指标）可以在 32B scale 上系统性地选择浅层，从而逆转 HS 优势的结论。在修正后的深层上，所有四个模型在 384d MiniLM baseline 下显示显著 HS 优势（Holm-Bonferroni 校正），但该优势是 encoder-conditional 的：升级到 1024d BGE-large 后仅 1/4 模型保持显著。32B 结果为 pilot-scale（n=19-20），QwQ-32B 的 HS 优势主要由位置编码介导。

---

## Strengths

**S1. Layer selection sensitivity 是稳健且有广泛价值的方法论贡献。** [共识: R1-S3, R2-S1] 五指标消融清楚展示了 crossing rate 如何系统性偏向浅层。LOO-CV 验证了选择稳定性（68%/65% dominant fold ratio）。该发现可推广到任何 threshold-based probing 研究。Discussion 中对 sentiment/factuality/toxicity 的泛化假设合理。

**S2. 统计方法透明度高。** [共识: R1-S1, R2-S2] 完整的 Holm-Bonferroni 12-test step-down 表（Appendix C）、permutation test 交叉验证、5-seed 稳定性报告、PCA dimensionality matching、control task selectivity 构成了多层验证体系。这种透明度在同类 probing 论文中罕见。

**S3. 负面结果的系统报告。** [共识: R1-S4, R2-S3] Table 4 中 7 种替代方法的系统排除有信息量，每种方法的失败原因有明确归因（BOCPD: gradual transition; Mahalanobis: signal in minor PCs; RepE: model-dependent）。

**S4. Bug disclosure 体现罕见透明度。** [共识: R1-S5, R2-S4] Appendix L 主动披露 QwQ-32B text probe 初始化 bug 及完整影响链。

**S5. Related Work 结构清晰。** [R2-S5] 四段式组织（Safety in Reasoning Models / Hidden-State Detection / Probing Methodology / Change-Point Detection）有明确 positioning 功能，非列表式堆砌。46 篇引用数量达标（但有关键遗漏，见 W6）。

---

## Weaknesses

### Must-Fix (Critical)

**W1. HS advantage headline claim 严重依赖弱 baseline，framing 名不副实。** [共识: R1-W6/AGREE R2-W1, R2-W1]
- Abstract/Introduction 的 headline "+15.4 to +32.5pp precision" 全部来自 vs. 2020 年 384d MiniLM（22M params）。BGE-large-1024d 后仅 OT-7B 1/4 模型 precision 通过 HB。
- PCA-384d 控制实验（Section 4.3）确认 HS 优势是 modality effect 而非纯 capacity artifact（+16.8 to +23.1pp, 4/4 precision pass HB）。但实际优势幅度取决于 encoder 强度——against competitive encoder, advantage largely vanishes in significance。
- **要求**: Abstract/Introduction 以 layer selection sensitivity 为核心 framing；BGE 结果在 Abstract 中获得与 384d 同等篇幅；Contribution 2 重述为 "encoder-conditional directional advantage"。

**W2. "All four models significant" 叙事将脆弱 32B 与稳健 7-8B 等量齐观。** [共识: R1-W2/W3, R2-W2]
- QwQ-32B: position baseline bal_acc (0.832) > HS (0.796)；position-residualized probe drops 18.3pp（0.796→0.612 ≈ chance+noise）；HS vs position 的 precision/FPR p-value 未报告，在 n=19 下极可能不显著。论文自己承认 "remaining margins likely reflect finer-grained position encoding"。
- R1-32B: 仅 W=1 显著（5/20 traces, 25% coverage）；multi-seed precision std=0.128, FPR std=0.145（单次 split 可能随机）。
- R1-8B FPR: 4-test HB 下 p=0.044, threshold=0.050, margin 仅 0.006。Multi-seed FPR std=0.026 足以翻转。（R2 nuanced: 即使失败，precision p<0.001 仍成立，影响范围有限。）
- **要求**: Abstract/Introduction 分层表述 "robust at 7-8B; pilot-scale at 32B with model-specific caveats"；报告 QwQ-32B HS vs position bootstrap p-value；报告 R1-8B FPR 5-seed p-value 分布；主 Table 添加 ±std。

**W3. "3/3 correlated metrics" 膨胀证据强度。** [共识: R1-W1, R2-AGREE]
- bal_acc/precision/FPR 共享混淆矩阵，自由度仅 2。全文反复使用 "each on three correlated metrics" 在 Abstract, Introduction, Section 4.2, Section 4.3 出现，给人 12 项独立验证的印象。Appendix C 已正确报告 4-test HB，但正文叙事包装膨胀。
- **要求**: 全文以 "all 4 models significant (HB corrected)" 为主表述；"3/3 correlated metrics" 仅在 Appendix 补充。

**W4. 32B 验证集规模与超参搜索空间严重不匹配。** [共识: R1-W4/W9, R2-AGREE]
- "n=4-9 at 32B" 含义不清（per-class? total? 与 Table 1 的 20%=20 traces 矛盾）。
- 448+ configurations（64 layers × 7 W，不含 K 和 threshold）在 tiny validation set 上选择。
- LOO-CV 仅验证 layer 稳定性，未验证 (layer, W) 联合稳定性。
- C-insensitivity (<2pp) 仅覆盖 1/5 超参数；threshold sensitivity 未报告。
- **要求**: 澄清 "n=4-9" 含义；(layer, W) 联合 LOO-CV；threshold sensitivity 分析；或采用 fixed hyperparameter protocol。

### Should-Fix (Warning)

**W5. Introduction monitoring/intervention framing 与 39-52% safe-trace FPR 不匹配。** [共识: R2-W4, R1-AGREE partial]
- Introduction 首段以 real-time monitoring/intervention 为动机，但 FPR 接近 50%。Introduction L3 有 characterization 对冲但不够突出。
- **要求**: Introduction 更早管理预期，明确本文是 characterization study；contributions 列表后增加 explicit scope statement。

**W6. 缺少 5 个关键引用，其中 3 个是论文直接使用工具的原始出处。** [共识: R2-W5, R1-AGREE]
- Page 1954 (CUSUM) — 论文广泛使用但未引原文
- Reimers & Gurevych 2019 (Sentence-BERT) / Wang et al. 2020 (MiniLM) — primary text baseline 的原始出处
- Xiao et al. 2023 (BGE) — encoder robustness 核心 baseline 原始出处
- Meng et al. 2022 (causal tracing) — Conclusion 和 Appendix 提到但未引用
- 另有 2 个 orphan bib 条目（liu2025probing_quantitative, jiang2025infalign）应删除
- **要求**: 补充全部 5 篇引用；删除 orphan 条目。

**W7. K=5 "Pareto-optimal" 标签暗示不存在的优化质量；K×W 交互未探索。** [共识: R1-W8, R2-AGREE]
- K=5 mean safe FPR ≈ 0.485（接近 50%）。K=5 "design pre-selection" 无 pre-registration 证据。
- **要求**: "Pareto-optimal" 改为中性描述；补充 K×W 联合 ablation 子集或标注 K=5 为 convention choice。

**W8. GRU 评估协议 split 不一致。** [部分分歧: R1-W7, R2-REBUT partial]
- 60/20/20 GRU 结果仅限 R1-8B (Table 10)；OT-7B GRU 未标注 split。
- R2 认为 GRU 非核心方法，严重性低。
- **要求**: OT-7B GRU 段落补充 split 说明。

**W9. 正文仅 2 个 Figure，对 8 页 long paper 偏少。** [共识: R2-W7, R1-AGREE partial]
- 缺少：(a) HS vs text probe score 时间序列对比图；(b) 32B detection profile 可视化；(c) encoder-conditional comparison figure。
- **建议**: 增加 1-2 个正文 figure 增强叙事视觉支撑。

**W10. Abstract ~251 words，数据堆砌仍严重。** [隐含共识: 基于 R2-W1/W2 framing 问题]
- 包含 crossing rate 机制、position baseline 数字 (0.832 vs 0.796)、"Seven alternative approaches fail"。更像 Results 压缩版而非 story。
- **要求**: 重写为 story 结构（problem→insight→finding→implication），压缩到 ~200 words。

### Minor / Info

**W11.** "Exact permutation test (5,000 permutations)" 术语矛盾 — 应为 "Monte Carlo permutation test" 或执行穷举。[共识: R1-W5, R2-AGREE]

**W12.** OpenThoughts (数据集) vs OpenThinker-7B (模型) 名称混淆 — 首次使用时应澄清关系。[共识: R2-W8, R1-AGREE]

**W13.** -ing 短语结尾模式（AI 写作标志）约 15+ 处仍存在。[R8 遗留，R9 未单独检查]

---

## Reviewer Consensus

两位 Reviewer 在以下 critical issues 上完全共识（所有 AGREE）：
1. **[AGREE] Headline HS advantage claim 依赖 2020 年弱 384d baseline**；BGE-large 后 1/4 significant — framing 需重大调整
2. **[AGREE] "All four models significant" 夸大 32B 证据强度** — 需分层表述 robust 7-8B vs pilot 32B
3. **[AGREE] "3/3 correlated metrics" 修辞膨胀** — 应以 4-test model-level HB 为主
4. **[AGREE] 32B 验证集过拟合风险** — 搜索空间与样本量严重不匹配
5. **[AGREE] 缺少 5 个关键引用**（CUSUM, Sentence-BERT, MiniLM, BGE, causal tracing）

## Reviewer Divergence

| Issue | R1 | R2 | Director 判断 |
|-------|-----|-----|-------------|
| RepE "fail" 措辞 (R2-W3) | REBUT: precision-priority 在 safety 语境合理；"consistently" 已修饰 | WARNING: bal_acc 差仅 2.2pp | R1 有理：论文原文 "No method consistently matches" 已准确。建议增加一句承认 RepE 单模型竞争力。 |
| Abstract crossing rate 定义 (R2-W6) | REBUT: 括号定义已足够 | WARNING: 不够透明 | R1 有理：Abstract 篇幅受限，括号定义可接受。可选优化。 |
| GRU split 严重性 (R1-W7) | WARNING | REBUT partial: GRU 非核心方法 | R2 有理：严重性低，仅需补标注。 |

---

## Questions (需作者澄清)

**Q1.** "n=4-9 at 32B"（Limitations）指 per-class count 还是 total？与 Table 1 的 20% validation 不一致。

**Q2.** QwQ-32B HS vs. position baseline 在 precision 和 FPR 上的 bootstrap p-value？如不显著，是否应从 "all four models" 核心声明降级？

**Q3.** R1-8B FPR 5-seed 下各 seed 的 HS-vs-text p-value 分布？是否有 seed 不通过 4-test HB？

**Q4.** LOO-CV 是否验证了 (layer, W) pair 的联合稳定性？

**Q5.** QwQ-32B position-residualized probe 0.612 balanced accuracy 在 n=19 下是否显著高于 chance (0.5)？如不显著，QwQ-32B 的 HS representation 中是否存在 position-independent safety structure？

**Q6.** R1-32B multi-seed FPR std=0.145 的 outlier seed 其他指标（precision, bal_acc）表现如何？

---

## Missing References

1. **Page, E. S. (1954).** "Continuous Inspection Schemes." Biometrika. — CUSUM 原始论文
2. **Reimers, N. & Gurevych, I. (2019).** "Sentence-BERT." EMNLP. — all-MiniLM-L6-v2 framework
3. **Wang, W. et al. (2020).** "MiniLM." NeurIPS. — MiniLM 原始论文
4. **Xiao, S. et al. (2023).** BGE 论文 — BGE-large-en-v1.5 原始出处
5. **Meng, K. et al. (2022).** "Locating and Editing Factual Associations in GPT." NeurIPS. — causal tracing
6. *(可选) Li, K. et al. (2024).* ITI. NeurIPS 2023. — inference-time intervention

---

## External Review (Stanford Agentic Reviewer)

未配置，跳过。

---

## Overall Assessment

**Overall Score: 3.0 / 5 — Findings**

| 维度 | R1 | R2 | 合议 |
|------|-----|-----|------|
| Soundness | 3/5 | 3.5/5 | **3/5** — HB 实施规范但核心 claim 有多个统计薄弱环节 |
| Excitement | 3.5/5 | 2.5/5 | **3/5** — Layer selection sensitivity 有方法论价值；HS advantage 在 competitive encoder 下不 robust |
| Reproducibility | 4/5 | 3/5 | **3.5/5** — 超参完整报告，公开 benchmark，承诺代码；2240 configs 精确复现依赖代码 |
| Overall | 3/5 | 3/5 | **3.0/5 (Findings)** |
| Confidence | 4/5 | 4/5 | **4/5** |

**评分理由**:

Layer selection sensitivity（Contribution 1）是论文中最稳健、最有价值的贡献，不依赖 encoder 选择、不受 32B sample size 影响，对 probing 社区有广泛方法论参考价值。该发现值得在 Findings 发表。

但 Contribution 2（HS advantage）的 headline claim 建立在 2020 年弱 baseline 上，在合理 encoder 下基本消失（1/4 HB-significant）。32B 结果为 pilot-scale，QwQ-32B 的 HS 优势主要由位置编码介导。"All four models significant" 的齐一叙事对审稿人有误导性。论文在 Limitations 和 Appendix 中对这些问题有坦率承认，但 Abstract/Introduction 的 framing 未反映这些 caveats。

修复 W1-W4（framing 调整 + 缺失 p-values + 分层表述）后可升至 3.5 (Borderline Conference)。当前状态下 3.0 (Findings) 是准确评价。

---

## Detailed Comments (逐节)

### Abstract
- ~251 words，包含过多技术细节（crossing rate 机制、HB correction、position baseline 数字）。应重写为 story 结构，压缩到 ~200 words。
- "+15.4 to +32.5pp" headline 应加 "over 384d sentence embeddings" 限定，并同等篇幅提及 1024d 结果。
- "crossing rate" 有括号定义但可考虑更通俗表述。

### Introduction
- 首段 monitoring/intervention framing 过强，与 39-52% FPR 现实不匹配。L3 的 characterization 对冲不够突出。
- Contribution 2 应以 encoder-conditional 为前提条件而非括号修饰。
- Contribution 3 的 "Seven alternative approaches" 措辞准确（"No method consistently matches"），但 Introduction 中的隐含 framing 可能暗示更强的否定。

### Related Work
- 结构清晰，49 篇引用数量达标。
- 缺少 5 个关键引用（见 Missing References）。
- 2 个 orphan bib 条目应删除。

### Method
- Section 3.3 Layer Selection Sensitivity 写作清晰。
- "n=4-9 at 32B" (Limitations) 含义需澄清。

### Experiments
- Table 2 (layer selection) 和 Table 3 (HS vs text) 信息密度合理。
- Table 3 主表缺 ±std（Appendix K 有但不够可见）。
- Section 4.5 (32B analysis): position-residualized probing 是重要补充，但 HS vs position p-value 缺失。
- Section 4.6 (negative results): precision-priority framing 有先验声明，RepE 评价总体准确。
- "Pareto-optimal" (K=5) 标签应改为中性描述。
- "Exact permutation test" 术语需修正。

### Discussion
- Layer selection as researcher degree of freedom 段落有独立方法论价值。
- 与 Introduction/Experiments 有数字级重复，可精简。
- 泛化假设（其他 probing 任务）合理且有 hedge。

### Conclusion
- 已精简为 3 句 + future work，长度合适。

### Limitations
- 坦率且全面（32B caveats, FPR, cumulative DoF, scope）。
- "two-tier framing" 在此段出现但 Abstract/Introduction 未反映。

### Appendix
- 信息丰富（HB 表、permutation test、multi-seed、encoder robustness、bug disclosure）。
- Bug disclosure (Appendix L) 体现学术诚实。

---

*Report generated by Review Director (Round 9, 2 Reviewers, 1 round + cross-sharing)*