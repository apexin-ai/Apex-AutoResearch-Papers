---
round: 12
overall_score: 3.0 - Findings
timestamp: 2026-05-17T18:33:05.454877+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 13 Consolidated Review Report

**论文**: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains
**Venue**: EMNLP 2026 via ARR May cycle (Findings track)
**Reviewers**: R1 (方法严谨性+实验验证), R2 (新颖性+完整性+写作质量)
**交叉回应**: 完成。所有关键分歧已解决。

---

## Summary

本文提出 generation depth classification 任务，将传统 binary AI text detection 扩展为三类有序分类（gen-0/gen-1/gen-2+）。在 8 个 base model generator（5 个 family，0.6B–8B）构建的 37,058 条递归生成链上，作者发现 differential depth response (DDR)：central-tendency/diversity 特征随 depth 单调漂移，shape 特征近似平稳。7 特征 + XGBoost 在 8-generator LOGO 下达到 leak-free binary F1=0.694，3-class F1=0.762。

---

## Strengths

**S1 [共识]** 任务定义新颖且有研究价值。Generation depth classification 将 binary detection 推向 ordinal depth estimation，是此前未被系统研究的方向。与 broken_telephone（paraphrasing chains）和 markovian_chains（attractor dynamics）的区分清晰充分（§2.2 三点区分+互补分析）。

**S2 [共识]** DDR 分析有洞察力。Drifting vs stationary 特征分组揭示了递归生成对 NLL 分布的结构化影响（6 倍 magnitude gap: |ρ|>0.60 vs <0.10），超越简单的 perplexity 阈值检测。

**S3 [共识]** 评估方案全面。LOGO 8-fold、LOFO 5-family、cross-model chains、cross-domain（Appendix J）、perturbation robustness（Appendix I）、length confound（Appendix B）、temperature sensitivity、classifier ablation 等消融分析系统覆盖。统计检验规范：bootstrap CIs、McNemar tests、Bonferroni correction 均到位。

**S4** 轻量高效。仅需单个 Pythia-410M reference model（905 MB），计算成本 9.7 ms/text，远低于 multi-detector ensemble（22.8 ms/text, 2.4×）。

**S5 [共识]** 科学诚实。Downstream utility null result 如实报告（§4.4），Limitations 全面坦诚，引用完整无幽灵（58 条全被引用，验证无 fabrication）。

**S6 [共识]** 写作质量较高。AI 痕迹极少（仅 Appendix D 一处 "Notably"），专有名词定义完整，段落长度自然，过渡连贯。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1 [critical, 共识]** 正文超 8 页限制（约溢出 1/3 页）

Discussion 结束于 page 9，Conclusion 起始于 page 9 约 1/6 处。ARR Long paper ≤8 页正文是硬约束，违规有 desk reject 风险。建议将 §4.4 Downstream Utility 移入附录（1–2 句结论留正文），压缩 Discussion。

[R2-N1 提出, R1 AGREE]

**MF2 [critical, 共识]** Abstract/Introduction 选择性报告性能数字

- Abstract 突出 cross-model 5-gen 结果（binary F1=0.764, 3-class=0.809），而非更严格的 8-gen LOGO（binary=0.694, 3-class=0.762）。
- Introduction "outperforming all individual detection baselines by 6–11 pp" 仅覆盖两个最强 baseline，实际范围 6–36 pp。
- Table 4 中 4-det+surface ensemble 的 3-class F1（0.795）和 binary F1（0.708）均高于 7-feature（0.774, 0.705），但论文表述为 "comparable"。
- **建议**: 以 8-gen LOGO binary F1 (0.694) 为主指标；坦率承认 ensemble baseline 数值优势；修正 "6–11 pp" 为准确范围。

[R2-N2 提出, R1 AGREE. 历史 R7-W1/R8-N2 持续复发]

**MF3 [critical, 共识]** Base-model-only 限制在 framing 中严重不足

- Abstract 完全未提及 "base model" 限制。
- Introduction 仅一句话（"We restrict to base (pretrained) models as a deliberate design choice"）。
- Instruct model 性能骤降（OLMo-Instruct: F1=0.338 vs base 0.763）意味着方法在最具实际意义的场景下近乎不可用，但这一关键信息被埋在 Limitations。
- 论文 framing 暗示实际应用价值（data curation, provenance），与实际适用范围不匹配。
- **建议**: Abstract 必须标注 "base (pretrained) models"；Contributions 列表包含 scope constraint；正文而非仅 Limitations 讨论 instruct model 结果及衰减机制。

[R1-N3 + R2-N3 独立提出, 完全一致. 历史 R7-W5 持续复发]

**MF4 [critical, 共识]** Gen-0 seed sharing 偏差未量化

所有 8 个 generator 共享相同 gen-0 seed，LOGO 中 held-out generator 的 gen-0 与训练集 gen-0 完全相同。论文仅定性承认（Table 1 footnote: "may carry upward bias"），未量化影响幅度。

**建议**: (a) LOGO 训练集中去除 held-out generator 的 gen-0 样本后重跑，直接量化 3-class inflation；(b) 或 per-fold unique seed split。

[R1-N2 提出, R2 AGREE. 历史 R7-W1 持续复发]

### Should-Fix（影响评分但不一票否决）

**SF1 [warning, 共识]** DDR 阈值 |ρ|>0.60/<0.10 缺乏正式依据

阈值是 post-hoc 选择，但论文表述为 "operative criteria"（§4.2）。7 个特征 |ρ| 自然形成两个 cluster（6 倍 magnitude gap），具体阈值选择对结论影响不大，但论文应补充 sensitivity analysis 说明分组稳定性。

[R1-W1 提出, R2 AGREE. 历史 R11-M5]

**SF2 [warning, 共识]** Levene test 全 reject 与 "approximately preserves shape" 张力

§4.2 中 Levene test 对所有 7 个特征 reject 等方差（p<10^{-10}），与 "approximately preserves distributional shape" claim 产生 framing 矛盾。N=37,058 大样本下微小差异也达显著——这是 significance vs. effect size 的经典问题。论文用 CV shift（<3% vs >15%）部分回应，但仍需 effect size measure（η² 或 variance ratio）替代纯 p-value。

[R1-W2 提出, R2 AGREE. 历史 R7-W2]

**SF3 [warning, 共识]** Downstream n=3 功效不足 + 正文空间效率

§4.4 仅 3 seeds，Cohen's d 膨胀至 86–120（论文自承 "artificially inflating"）。该 null result 占正文约 1/4 页，在超页情况下尤其昂贵。建议移入附录，正文 1–2 句总结。

[R1-W3 功效角度 + R2-W3 空间角度, 共识. 历史 R10-N3]

**SF4 [warning, 共识（severity 分歧）]** 方法技术新颖性极低

7 个标准统计特征 + off-the-shelf XGBoost，无 non-trivial 算法贡献。论文自认 "Our contribution is not a new detection method but the task formulation"（§2.1）。R1 认为 task novelty 部分补偿（Excitement 3.0），R2 认为整体 excitement 偏低（2.5）。作为 Findings track phenomenon paper 可接受，但需在 Introduction 中更显式声明。

[R2-W2 提出, R1 AGREE. 历史 R7-W4]

**SF5 [warning, 共识]** Cross-model 评估仅用 5/8 generators

Llama/Mistral 后加入仅做 single-generator 评估。Cross-model F1=0.809 基于更小 generator pool，原因在 footnote 中但不够突出。建议正文中明确说明原因。

[R1-W5 提出, R2 AGREE. 历史 R11-W3]

**SF6 [warning, 共识]** 附录 5/6/8-gen subset 不一致

正文 8-gen、cross-model 5-gen、部分附录 6-gen，subset 变化散在 footnote 中。建议 §3 中统一说明各评估方案的 generator subset 及理由。

[R2-W5 提出, R1 AGREE. 历史 R11-W3]

**SF7 [warning, 共识]** 模型规模有限（0.6B–8B），无 >10B model

Scale effect（larger → lower F1：Mistral-7B 0.633，Qwen3-8B 0.692）暗示 70B+ 模型可能进一步压缩 feature margins。对 Findings phenomenon paper 是 acknowledged limitation，非 fatal flaw。

[R1-W4 提出, R2 AGREE]

### Minor

- **M1**: Appendix D "Notably" — AI 写作标记，删除。[R2-M1, R1 AGREE]
- **M2**: RTX 5090 硬件信息——确认准确性。[R2-M2, R1 AGREE]
- **M3**: `\documentclass` 格式——建议对齐 ARR 模板标准写法。[R2-M3, R1 AGREE]
- **M4**: Table 4 中 ensemble baseline 3-class F1 优势（0.795 vs 0.774）应更坦率讨论。[R2-M5, R1 AGREE]
- **M5**: Figure 2 strip plot entropy_std 区域标签重叠，影响可读性。[R1-M2]

---

## Reviewer Consensus

以下问题双方达成完全共识 [AGREE]：
- **MF1–MF4** 所有 Must-Fix 问题
- **SF1–SF7** 所有 Should-Fix 问题（SF4 severity 有分歧但方向一致）
- **M1–M5** 所有 Minor 问题

## Reviewer Divergence

**已解决的分歧（3 项）：**

1. R1 认为 §3.2 存在 temperature=0 vs 0.7 矛盾（R1-N1 critical）。R2 指出源文 method.tex line 32 明确写 `τ=0.7`，R1 可能误读 LaTeX 渲染。**Director 核实源文确认 R2 正确。R1-N1 撤销。**

2. R1 认为 2.4× 计算成本缺乏依据（R1-W6）。R2 指出 Table 4 有 ms/text 数据（9.7 vs 22.8 = 2.35×）。**R1-W6 撤销。**

3. R1 认为 §2.2 Geng et al. 区分不够（R1-M3）。R2 指出三点区分+互补分析段落充分。**R1-M3 撤销。**

**保留的 severity 分歧（1 项）：**

- **方法新颖性**（SF4）：R1 Excitement 3.0（task novelty 补偿），R2 Excitement 2.5（技术新颖性更重要）。不影响 Findings-appropriate 共识。

---

## Questions for Authors

Q1. Gen-0 per-generator unique seed 实验是否可行？3-class F1 预期下降幅度？

Q2. Instruct model depth signal 衰减的根本机制：是 NLL 分布 variance 压缩，还是 formatting patterns 遮盖 DDR？两种机制的区分对 future work 有指导意义。

Q3. DDR 的 drifting/stationary 分组在 per-generator 级别是否一致？Figure 1 有 per-generator 数据但未按 family 拆分报告 ρ。

Q4. Depth fingerprinting 是否本质上是 "model quality detection" 的 proxy？（larger/better model → weaker signal → DDR 的独立贡献如何界定？）

Q5. §4.4 Downstream utility 若增加到 n≥5 seeds，结论是否改变？

---

## Missing References

无重大遗漏。可选补充：
- "Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems" (2026, arxiv 2601.04170)
- "Visual Fingerprints for LLM Generation Comparison" (2026, arxiv 2605.06054)

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Soundness | 3.0 | 3.5 | 3.0 |
| Excitement | 3.0 | 2.5 | 2.5–3.0 |
| Overall | 3.0 | 2.5 | **3.0** |

**置信度**: 4/5（两位 Reviewer 均仔细阅读全文含 20 页附录，完成交叉回应，3 项事实分歧已核实解决）

**总评**: 本文提出了一个新颖且有意义的任务（generation depth classification），DDR 发现提供了有价值的实证洞察，实验设计总体严谨，消融分析全面，写作质量较高。四个 Must-Fix 问题——正文超页（MF1）、选择性报告（MF2）、base-model-only 限制未充分声明（MF3）、gen-0 偏差未量化（MF4）——在当前状态下阻碍接收。方法层面无技术新颖性（SF4），仅限 base model 的适用范围缩窄了影响力。

**接收建议**:
- 修正 MF1–MF4 后适合 **Findings track**（3.0 → 3.0–3.5）
- 主会议（4.0）需要额外展示 instruct model 下的有效信号或根本性方法改进
- MF1（页数）和 MF2（指标报告）是纯写作修正，可快速完成
- MF3（base-model framing）需 Abstract/Introduction 调整
- MF4（gen-0 量化）需补充实验，工作量最大