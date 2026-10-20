---
round: 10
overall_score: weak accept / borderline (Findings acceptance)
timestamp: 2026-05-16T02:29:04.735110+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 9 审稿报告

**论文**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction
**Venue**: EMNLP 2026 Main Conference (via ARR May 2026)
**Reviewers**: R1 (方法严谨性+实验设计+统计分析), R2 (新颖性+完整性+相关工作+格式)
**审稿模式**: Fresh review (Round 9)

---

## Summary

本文研究 LLM-based 结构化信息抽取（NER/RE）中五种一致性信号（SJ, VC, FK, EM, LP）的质量估计与样本选择能力。核心发现是 "correlation-selection gap"：所有信号均能有效预测输出质量（ρ 达 0.45, AUROC 达 0.82），但无法从 N 个采样中选出最优输出，尽管 oracle headroom 达 13-18pp。论文通过 free-form decoding ablation 证明 LP score compression 是 task-intrinsic 的（NER 上成立），并在 4B-8B 两个规模上验证了结论的稳健性。

---

## Strengths

**S1. 概念框架有价值。** Quality estimation vs. sample selection 的显式区分在 IE 文献中此前未被正式化。Instance-level vs. per-sample 信号的分类法直接解释了 4/5 信号为何不能做 selection，为后续工作提供设计准则。[R1-S1, R2-S1 共识]

**S2. LP 压缩分析深入且有实际价值。** Median within-instance LP range = 0.041 nats, 60.3% tied instances, non-tied subset 显著优于 greedy (+2.9pp, p=0.004), ε sensitivity sweep 验证阈值稳健性。这是论文最有价值的实证发现。[R2-S2, R1 隐含认同]

**S3. 统计分析显著优于同类 empirical NLP 工作。** Bootstrap CI with pairwise Δρ、TOST 等价检验（含三类外部锚点 δ_SEM/δ_practical/δ_literature）、instance-level permutation test、Fisher combined p、Cohen's d 报告。诚实标注所有 borderline/preliminary 结果。[R1-S3, R2-S3 高度共识]

**S4. 实验设计严谨。** Difficulty gradient（SciERC → CoNLL → WNUT-17）、cross-model (Qwen/LLaMA)、cross-scale (4B/8B)、multi-seed (3 seeds, Kendall's W=1.000)、free-form ablation。形成完整 robustness picture。[R1-S2, R2-S3]

**S5. Appendix 极其充实（~15 pages）。** 17 个 appendix section 覆盖了几乎所有可预见质疑：SJ normalizer robustness (Δρ<0.005)、LOO-SJ equivalence、ε sensitivity、FK independence permutation test、OOD transfer、thinking token 三部分定量分析、LP failure stability cross-seed analysis。体现高度学术自觉。[R1-S5, R2-S4]

**S6. Limitations 透明度高。** RE preliminary 标注贯穿全文（Abstract, Introduction #3, Table captions, Conclusion），thinking token confound 有三部分定量分析，free-form ablation 的 RE reversal 未回避。[R1-S4, R2-S6]

**S7. Related work 覆盖面广。** Self-consistency 方向（Wang 2023 等 10+ 篇）、MBR decoding（Eikema 2022/2025, Freitag 2022 等）、uncertainty surveys（Geng 2024, Xia 2025, Hobelsberger 2025）、structured IE (Zhou 2024 等)。与 Eikema 2025 structured MBR 的对接尤其到位。[R2-S5]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [critical, 共识] **Correlation-selection gap 对 4/5 信号是 definitional 而非 empirical finding — 框架过度膨胀贡献**

两位 Reviewer 独立提出相同核心问题（R1-N2, R2-N1）：VC, SJ, FK, EM 作为 instance-level 信号，数学上产生 single score per input，无法对 N 个 candidate 排序——这是信号定义的直接推论。标题 "The Correlation-Selection Gap" 和 Abstract "none improves best-of-N selection" 将部分 tautological 的观察框架化为统一发现，过度膨胀了贡献。

真正的实验发现仅是：(a) LP score compression 导致唯一的 per-sample signal 也失败；(b) consensus-proximity/MBR-style selection 也失败——后者是 non-trivial 的。论文 Discussion §5 和 Table 2 已有两层结构和透明声明（line 8: "assign a single score per input; they cannot rank candidates by construction"），但 Abstract/Introduction/Conclusion 的修辞权重仍将 gap 呈现为统一发现。

**建议修改方向**：(1) Abstract/Introduction 中用一句话 dismiss instance-level 信号的 selection 失败为 definitional consequence，将贡献重心移向 LP compression + MBR failure 的实证发现；(2) 或将分类法本身（instance-level vs per-sample）定位为核心贡献（Contribution #1），降低 selection failure 的修辞权重。

⚠️ 此问题自 Round 3 (R3-W2) 起反复出现，Round 8 的 resolution（视觉分组+两层结构）被两位 Reviewer 认为不够——需要在 Abstract/Introduction/Conclusion 层面根本性 reframe。

---

**N2** [critical, 共识] **Abstract/Conclusion 对 free-form ablation 过度概括——省略 RE LP selection 方向反转**

两位 Reviewer 共识（R1-N1, R2-N2）：Abstract 称 "A free-form ablation confirms compression is intrinsic; the gap persists across scales and task types"，但 Discussion 明确记录 RE 在 free-form decoding 下 LP selection 从 −0.68pp 翻转为 +1.69pp（Table 15 Panel B）。"across task types" 与 RE 结果直接矛盾。

论文 Discussion 和 Limitations 诚实承认了 RE reversal，但 Abstract 和 Conclusion 的措辞未限定范围。

**建议修改方向**：Abstract 改为 "confirms NER compression is intrinsic; RE shows a directional reversal warranting further investigation"。Conclusion 同步修改，不能说 "across task types" without qualification。

⚠️ 此问题自 Round 7 (R7-C3) 起存在，Round 8 resolution（Discussion scope 限定为 NER only）被认为不够——Abstract/Conclusion 仍未修正。

---

**N3** [critical, R1 主导, R2 间接支持] **标题/Abstract "Information Extraction" scope 过宽——RE 仅 preliminary**

R1-N3 列 critical：RE 仅在 SciERC 上测试（40% zero F1），全部标注 "preliminary"。标题说 "Information Extraction" 但核心可靠结论仅覆盖 NER。Introduction contribution #3 已正确标注 "RE conclusions rest on SciERC alone (preliminary)"，但 Conclusion 未同步 hedge。

R2 在 W3（Conclusion 未 hedge RE）和 W4（模型规模限制）中间接呼应。

**建议修改方向**：Conclusion 增加 "RE conclusions are preliminary, based on a single benchmark"。标题可保留 "Information Extraction" 但正文需一致 hedge。

---

### Should-Fix（影响评分但不一票否决）

**W1** [warning, R2] **缺少其他 per-sample signal baseline（verbalized confidence, self-certainty）**
Per-sample signal 仅有 LP 一种。Tian et al. (2023, verbalized confidence)、Kang et al. (2025, self-certainty, 已引用) 等 per-sample signal 未对比。"no signal improves selection" 的结论不完整。建议至少在 Limitations 中承认仅测试了一种 per-sample signal。

**W2** [warning, 共识] **24 个 orphan bib entries 未引用**
包括 Culotta & McCallum 2004（IE confidence estimation 开创性工作）、Kadavath 2022（LLMs know what they know）、Malinin & Gales 2021（autoregressive uncertainty for structured prediction）等高度相关工作。应引用相关的或删除不相关的。

**W3** [warning, R1] **TOST 外部锚点结果 configuration-dependent 未整合进主文**
外部锚点下 LLaMA CoNLL 通过所有等价检验，但 SciERC 和 Qwen CoNLL 均 fail。"no signal improves selection" 应改为 "no signal consistently improves selection"。当前主文 Section 4.2 缺少这一 nuance。

**W4** [warning, R1] **VC majority-voting selection 的 per-sample 性质和失败机制未分析**
VC 在 selection 语境下通过 majority-voted output + overlap 实质成为 per-sample-like signal（不同 sample 与 voted output 的 overlap 不同），但表现最差（0.623）。这个失败值得 1-2 句机制分析。

**W5** [warning, R1] **多重比较校正不完整**
5 signals × 3 datasets × 2-3 models 大量比较无系统性校正。对于负结果，未校正 p>0.05 已足够但应明确说明这一逻辑。

**W6** [warning, R1] **Table 1 主表单种子未标注**
Table 1 seed=42 单次结果，与 Table 7 3-seed mean 有差异（LP NER: 0.205 vs 0.217）。虽然 ranking 一致（W=1.000）但应标注。

**W7** [warning, 共识] **Scale ablation "not model capacity" 结论过强**
仅 Qwen3-4B（无 LLaMA 4B），4B→8B 差异不到 2×。应弱化为 "within the 4B-8B range, task difficulty appears to be the primary driver"。

---

### Minor（不影响接收）

- **M1** [info, R2] Table 2 "Greedy" 指 T=1.0 single sample，但 greedy 通常指 argmax (T→0)——建议改措辞或加注释。
- **M2** [info, 共识] Section 3.2 FK 负依赖 "−0.4% to −4.0%" 无推导过程或 appendix reference。
- **M3** [info, R1] "correlation-selection gap" 术语反复使用但无操作性定义。建议 Section 4.2 给出形式化定义。
- **M4** [info, R2] Discussion ρ=0.38 是 VC ρ=0.379 的四舍五入，精度不一致。
- **M5** [info, R1] Table 2 NER 2-seed vs RE single seed 统计标准不一致。
- **M6** [info, R2] Bib entry 名/姓顺序问题（feng2025optimal, snell2025scaling 等），建议统一检查。

---

## Reviewer Consensus

**[AGREE]** 以下问题两位 Reviewer 完全达成共识：
- N1: Instance-level 信号 selection 失败是 definitional — 框架需 reframe
- N2: Abstract 对 free-form ablation 过度概括 — RE reversal 必须标注
- S3/S4: 统计分析和实验设计是论文的核心优势
- S2: LP compression 是最有价值的实证发现
- W2: Orphan bib entries 需清理
- W7: Scale ablation 结论需弱化

## Reviewer Divergence

**分歧 1** [R1: 3.5/5 vs R2: 3.0/5] — R1 认为概念贡献（metric dissociation + correlation-selection gap taxonomy）即使部分 tautological 也有信息量，MBR failure 是 non-trivial 的发现；R2 认为框架性贡献被高估，真正的 novelty 仅限于 LP compression。这是程度分歧而非方向分歧。

**分歧 2** [R2-W1 vs R1 未提] — R2 认为缺少其他 per-sample signal baseline（verbalized confidence）是 should-fix；R1 未独立提出此问题但 Q2 问了组合信号。

**分歧 3** [R2-W5 vs R1 未提] — R2 认为 consensus-proximity operationalization 有些 ad-hoc；R1 认为与 MBR 的连接已在 Appendix L 充分讨论。

---

## Questions to Authors

**Q1**: VC 在 selection 语境下（majority-voted output + overlap）实质成为 per-sample signal——为什么仍然失败？是否因为 voted output 与高频 sample 高度 overlap，导致 selection 退化为选最平庸的 sample？

**Q2**: 是否尝试过其他 per-sample signals（verbalized confidence, self-certainty, entropy of next-token distribution）？或组合信号（LP + SJ weighted combination）？

**Q3**: Free-form RE LP reversal（−0.68pp → +1.69pp）是最 actionable 的发现之一。这在 seed 42 之外能否复现？如果能，这可能成为重要 positive contribution。

**Q4**: ε=0.05 是否构成 p-hacking？Table 13 的 ε sweep 显示此阈值最大化了 statistical separation (p=0.004)。

**Q5**: Thinking token confound（Appendix G）分析了 LP 影响，但是否也改变了模型 output distribution 进而影响 consistency signals？

---

## Missing References

**论文中已有 bib entry 但未引用**（应引用或删除）：
- Kadavath et al. 2022 "Language Models (Mostly) Know What They Know" — LLM self-knowledge/calibration 开创性工作
- Culotta & McCallum 2004 "Confidence Estimation for Information Extraction" — IE confidence estimation 早期工作
- Malinin & Gales 2021 "Uncertainty Estimation in Autoregressive Structured Prediction" — 直接相关

**论文中未有 bib entry**（建议补充）：
- Tian et al. 2023 "Just Ask for Calibration" — verbalized confidence，与 W1 中 per-sample signal baseline 相关
- Ren et al. 2023 "Investigating Uncertainty Calibration of Aligned LMs" (EMNLP 2023 Findings) — LP calibration 相关

---

## External Review (Stanford Agentic Reviewer)

项目未配置 paperreview.ai 外部审稿（external_review.paperreview_ai.enabled 未启用）。外部审稿：未请求。

---

## Overall Assessment

**评分**: weak accept / borderline (3.25/5)
**置信度**: 4/5 (两位 Reviewer 均仔细阅读全文含 Appendix)

**建议**: Findings acceptance（两位 Reviewer 共识）

**理由**：
- **正面**：LP compression 发现有实际价值（median range 0.041 nats → non-tied subset +2.9pp, p=0.004）；统计分析远超同类工作；appendix 详尽；QE vs selection 的 metric dissociation 对社区有启发性
- **负面**：核心 "correlation-selection gap" 对 4/5 信号是 definitional（by construction），真正的 empirical finding scope 较窄（LP compression + MBR failure）；Abstract/Conclusion 对 free-form ablation 过度概括（RE reversal 未标注）；RE 证据不足但标题 scope 过宽

**升格条件**（若满足可考虑 Main Conference）：
1. Abstract/Introduction/Conclusion 层面 reframe：明确 dismiss instance-level failure 为 definitional，将贡献重心移向 LP compression + MBR failure
2. Abstract 修正 RE free-form reversal
3. 补充 free-form multi-seed RE 实验（若时间允许）
4. Conclusion hedge RE

---

## Detailed Comments

### Abstract
- 第 4-5 行："All signals achieve strong quality estimation yet none improves best-of-N selection" — 对 4/5 instance-level 信号是 definitional（N1）
- 第 6 行："the gap persists across scales and task types" — RE reversal 未标注（N2）
- 信息密度恰当（Round 8 后精简为 9 行 问题-发现-意义结构），RE preliminary 有标注

### Introduction
- Contribution list 结构清晰：#1 metric dissociation, #2 correlation-selection gap, #3 difficulty-dependent signal rankings
- Contribution #1 定位为 finding-led（"We find that..."）恰当
- Contribution #3 正确标注 "RE conclusions rest on SciERC alone (preliminary)"
- Figure 1 有效传达 gap 概念

### Related Work
- 覆盖面广，3 段结构清晰
- 与 Yao et al. (2026) 的增量贡献明确（structural matching, selection analysis, difficulty gradient）
- Eikema 2025 structured MBR 对接到位
- 建议引用已有 orphan entries（Kadavath 2022, Culotta 2004, Malinin 2021）

### Method
- 5 信号形式化定义精确
- SJ Hungarian matching 定义完整（threshold, normalizer, IoU）
- Evaluation framework（QE: ρ + AUROC; Selection: best-of-N）恰当
- 建议 Section 3.3 更早 qualify consensus-proximity 为 MBR instantiation

### Experiments
- Difficulty gradient 设计有效（SciERC → CoNLL → WNUT-17）
- Table 1 应标注 single seed (42)（W6）
- Table 2 NER 2-seed vs RE single seed 不一致（M5）
- "Greedy" 术语需澄清（M1）
- Scale ablation "not model capacity" 需弱化（W7）

### Discussion
- 两层结构（definitional + LP compression）存在但需在 Abstract/Introduction 更突出
- VC selection 失败机制缺分析（W4）
- MBR decoding 连接已到位（cite Eikema 2022/2025）

### Conclusion
- 缺 RE preliminary hedge（N3）
- "across task types" 需 qualification（N2）

### Limitations
- 透明度高
- 建议增加"仅测试了一种 per-sample signal"（W1）

### Ethics Statement
- 内容充实，含 CoNLL Reuters 出处和代码发布承诺

### Appendix
- 极其详尽（~15 pages，17 sections）
- SJ normalizer robustness、FK independence、ε sensitivity、OOD、free-form ablation 等细粒度分析增强可重复性