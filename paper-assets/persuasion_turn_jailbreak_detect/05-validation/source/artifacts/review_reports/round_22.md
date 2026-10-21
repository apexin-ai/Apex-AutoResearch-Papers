---
round: 22
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-23T15:11:13.613122+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection

**Round 22 | EMNLP 2026 (ARR May 2026) | 2 Reviewers + 交叉回应 + 视觉审查**

---

## Summary

本文提出 DisPeD，一个两阶段 pipeline（Stage-1 encoder adaptation + Stage-2 frozen BiGRU）用于多轮 jailbreak 检测。核心贡献是通过 13 个 encoder 配置的控制消融，分解了 domain exposure、classification supervision、label granularity 等因素对跨攻击 OOD 泛化的贡献。在合成数据上，classification-based DAPT 恢复 OOD 检测（F1=0.97–1.0 vs vanilla 0.26–0.31）；在人类数据（ToxicChat）上，该 hierarchy 完全反转（MLM F1=0.837 vs 9-class 0.596）。论文同时报告了 few-shot benign adaptation 将 FPR 从 58–68% 降至 0–1.5%。

---

## Strengths

**S1. 消融设计方法论贡献显著。** 7 个 Stage-1 变体系统分解了 domain exposure、classification objective、label granularity、label semantics、task relevance 五个因素。Scrambled 和 Topic 变体的设计尤其巧妙，分别隔离了 label correctness 和 domain relevance。这种 controlled decomposition 在 jailbreak detection 领域是首次，具有方法论模板价值。[R1 + R2 共识]

**S2. 统计分析全面规范。** 3-seed 均值±标准差、bootstrap 95% CI（10,000 resamples）、paired permutation tests（10,000 permutations）、TOST equivalence test 的组合使用远超大多数 NLP 安全领域论文。TOST 用于证明 "无差异" 而非仅报告 p>0.05 是方法论上的正确做法。[R1 + R2 共识]

**S3. 诚实报告 negative results。** MLM 在 mixed-LLM 训练下崩溃（Section 4.5）、BiGRU ≈ mean pooling（Appendix T）、ToxicChat 上证据层级反转（Section 4.6）、WildChat FPR 68.1%（Appendix P）——论文未回避不利结果，提升了可信度。[R1 + R2 共识]

**S4. 附录极其详尽（16 页）。** 覆盖 cross-encoder comparison、perturbation robustness、frozen probing vs E2E fine-tuning、representation analysis、inference efficiency、dataset scaling、length stratification、cross-seed ensemble 等。这些分析大大增强了结论的可信度并预先回答了审稿人可能提出的 follow-up 问题。[R1 + R2 共识]

**S5. Few-shot benign adaptation 的实用价值。** 10–25 条 WildChat/OASST2 对话将 FPR 从 58–68% 降至 0–1.5%，是有实际部署价值的发现。[R1 + R2 共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. [critical] 单一 LLM 合成数据生态系统对外部效度的根本性威胁。** [R1-N1 + R2-N3 | 共识]
训练数据（350 conversations）和全部 OOD 测试集均由 Qwen3-8B 生成。论文声称的 "cross-attack generalization" 可能部分是 "same-LLM generation pattern consistency"——encoder 学到的可能包含 Qwen3-8B 的回复模式而非纯粹的 persuasion features。三条佐证：(1) Cross-LLM 实验（Section 4.5）中 ActorAttack 降至 0.504（≈chance level）；(2) ToxicChat 人类数据上 hierarchy 完全反转；(3) WildChat 真实 benign 上 9-class FPR 高达 68.1%。论文已在 Limitations 和 scope qualifier 中做了限定，但 abstract/conclusion 的措辞强度与数据支撑之间仍有 gap。**建议**：在至少一个真实多轮 jailbreak 数据集上验证因子排序，或将 framing 明确限定为 "synthetic-data regime 下的因子分析"。

**W2. [critical] ToxicChat 上 evidence hierarchy 完全反转，削弱核心 claim 的普适性。** [R1-N1 + R2-N2 | 共识]
ToxicChat 上 JB-MLM F1=0.837±0.013 领先，9-class 下降至 0.596±0.087（Table 5）。这不是边际差异而是质的反转。论文归因为 "distributional differences between synthetic and human text"，但未提供控制实验来分离 distribution shift 和 single-turn vs multi-turn 两个因素。Abstract 中 "classification-based adaptation recovers OOD detection" 的 claim 实际仅在合成数据上成立，论文的 take-away 降级为 "adaptation strategy depends on data distribution"——一个更弱的贡献。论文已在 Abstract/Conclusion 中呈现为 "condition-specific rather than universal"，但 R2 认为这实质上削弱了核心贡献的 excitement。

**W3. [critical → major, 存在分歧] 核心贡献的新颖性不足。** [R2-N1 | R1 AGREE 但建议降为 major]
核心发现（classification DAPT > MLM > vanilla）可从 Gururangan et al. (2020) "Don't Stop Pretraining" 预期。Classification DAPT 实质上等同于 task-adaptive pretraining 在 jailbreak detection 领域的应用。"Controlled factorial study" 是实验设计选择，不构成方法创新。R1 认为因子分解本身有贡献，scrambled ≈ 9-class 是反直觉发现，建议降为 major。**分歧**：R2 认为 critical（excitement 不足以支撑 main conference），R1 认为 major（因子分解的模板价值部分弥补）。

### Should-Fix（影响评分但不一票否决）

**W4. [major, R2 部分反驳] Benign-Jailbreak 对话长度系统性差异构成潜在混淆变量。** [R1-N2 | R2 REBUT(部分)]
Jailbreak 3–10 turns vs benign 12–20 turns 长度不重叠。R2 反驳指出 truncation 实验（Table 32 Part A，截断 benign 到 K 最后几轮 FPR=0）和 prefix-length analysis（9-class 在 K=1 时 F1=1.000 而 vanilla 接近 0）部分化解了长度混淆论点。**共识**：长度本身不是唯一检测信号，但 WildChat 68.1% FPR 暗示更广泛的 synthetic-vs-real distributional shift，根因不仅是长度差异。

**W5. [major] Scrambled ≈ 9-class 等价性能与论文叙事的张力。** [R1-W2 | R2 AGREE]
Scrambled 在 DD（F1=0.997±0.005）和 FTTD（0.972±0.026）上与 9-class TOST 等价（δ=5pp）。这说明标签语义不重要，核心机制是 classification objective structure + domain exposure 的组合，而非 persuasion taxonomy 本身。论文对 9-class taxonomy 的大量讨论（Section 3.1, Appendix N, Appendix Y）在检测性能角度显得 misaligned。这个发现比论文当前叙述更有洞察力，但也进一步降低了相对于 Gururangan et al. (2020) 的增量贡献。**建议**：reframe 为 "any domain-relevant classification objective provides sufficient discriminative adaptation"。

**W6. [major] TOST δ=5pp 在高性能区间过于宽松。** [R1-W1 | R2 AGREE]
在 F1>0.95 区间，5pp 差异意味着 miss rate 数倍变化（F1=0.95 vs 1.0 → miss rate 5倍）。ActorAttack 上 scrambled vs 9-class TOST 未通过（p=0.183）。76 样本下 TOST 的统计功效可能不足。**建议**：报告 δ=3pp 和 δ=2pp 下的 sensitivity analysis；补充 power analysis。不改变定性结论但影响定量 claims 的精度。

**W7. [major] BiGRU temporal aggregation 缺乏必要性 justification。** [R1-W3 | R2 AGREE with reservation]
Table 30 显示 mean pooling 在绝大多数条件下 F1=1.000，与 BiGRU 持平。选择理由为分析便利性（CKA, t-SNE）而非检测需要。Figure 1 架构图和 Section 3.2 给读者的印象是 BiGRU 是 pipeline 关键组件，与 Table 30 矛盾。R2 保留意见：为表征分析保留 BiGRU 可接受，但需在正文明确声明。

**W8. [major] 9-class 策略标注质量验证不足。** [R1-W4 | R2 AGREE]
50 样本验证 9 类分类（κ=0.78），部分类别可能仅 2–5 个样本。Scrambled 实验缓解了对主要检测结论的影响，但 Appendix Y 策略预测（90.1% accuracy）的评估上限受标注质量限制。**建议**：增加至 ≥100 个验证样本；报告 per-class κ。

**W9. [major] 相关工作遗漏。** [R2-W1 | R1 REBUT(部分)]
Galinkin & Sablotny (2024) "Improved LLM Jailbreak Detection via Pretrained Embeddings" (arXiv 2412.01547) 使用 pretrained encoder embeddings 做 jailbreak detection，与本文方法高度相关，应当引用。R1 反驳认为 R2 列出的另外两篇（Hua et al. 2025 针对 VLM、"Do Internal Layers..." 针对 decoder probing）交集有限。**共识**：补充 Galinkin & Sablotny (2024)。

### Minor Issues（不影响接收）

**W10. [warning] Conclusion "reusable template" claim 超出证据。** [R2-W3 | R1 AGREE]
仅在 jailbreak detection 一个任务上实验，不能推广到所有 domain adaptation 场景。建议限定为 "template for future controlled studies in safety-critical NLP tasks"。

**W11. [warning] 自创术语过多。** [R2-W2 | R1 部分AGREE]
"Evidence hierarchy" 暗示超出经验排序的理论地位，建议改为 "performance ranking"。"Cross-attack OOD" 和 "discriminative compression" 可接受但需首次出现时定义。

**W12. [minor] Abstract 句法模糊。** "this hierarchy reverses" 后的修饰对象不清。Few-shot benign adaptation 的 FPR 数字应明确标注来源（WildChat）。

**W13. [minor] 规模局限性讨论不足。** R2 提出仅 base-scale 实验，R1 反驳论文已覆盖 125M–355M。共识：Limitations 可增加 2–3 句讨论 scale 对因子排序的潜在影响。

**W14. [minor] 视觉排版问题。** Figure 1 Stage-1 七个 variant 拥挤；Table 2 "3-seed mean±std where noted" caveat 易被忽略；Figure 2/3 axis labels 偏小。

---

## Reviewer Consensus

| 问题 | R1 | R2 | 状态 |
|------|----|----|------|
| 合成数据外部效度 (W1) | critical | major→共识critical | ✅ [AGREE] |
| ToxicChat 反转 (W2) | critical | critical | ✅ [AGREE] |
| 新颖性 (W3) | major | critical | ⚠️ 分歧（严重程度） |
| 长度混淆 (W4) | critical | REBUT(部分) | ⚠️ 分歧（R2 认为 truncation 部分化解） |
| Scrambled ≈ 9-class (W5) | major | AGREE | ✅ [AGREE] |
| TOST δ=5pp (W6) | major | AGREE | ✅ [AGREE] |
| BiGRU 必要性 (W7) | major | AGREE(有保留) | ✅ 基本共识 |
| 标注质量 (W8) | major | AGREE | ✅ [AGREE] |
| 相关工作 (W9) | REBUT(部分) | major | ⚠️ 分歧（范围：1篇 vs 3篇） |
| Conclusion overclaiming (W10) | AGREE | warning | ✅ [AGREE] |
| 术语 (W11) | 部分AGREE | major | ✅ 基本共识 |

---

## Reviewer Divergence

1. **新颖性严重程度**：R2 认为 critical（阻碍 main conference），R1 认为 major（因子分解有独立贡献价值，scrambled ≈ 9-class 是反直觉发现）。Director 判断：偏向 R2——控制消融的方法论价值部分弥补，但核心发现的可预期性确实限制了 excitement。

2. **长度混淆的程度**：R1 认为 critical（系统性差异未控制），R2 部分反驳（truncation 实验和 prefix analysis 部分化解）。Director 判断：R2 的反驳有效——Table 32 和 K=1 analysis 提供了合理的反证据。降级为 major，根因归入更广泛的 synthetic distribution shift 问题（W1）。

---

## Questions

Q1. ToxicChat 上 JB-MLM 领先是否意味着在真实多轮数据上分类 DAPT 的优势同样不成立？是否有计划在真实多轮 jailbreak 数据上验证？

Q2. WildChat FPR 68.1% 是否暗示 9-class DAPT 学到的 discriminative features 部分是 synthetic benign vs real benign 的分布差异而非 jailbreak-specific signals？

Q3. 如果 scrambled labels 在 template attacks 上与正确 labels 等价，保留 9-class taxonomy 的核心价值是什么？仅是 interpretability 还是在 strategy-diverse attacks 上有统计显著差异？

Q4. Mixed-LLM 训练中 MLM 崩溃的原因是什么？是 Qwen/Llama tokenization/style 差异导致 MLM 目标无法同时拟合两种分布？

---

## Missing References

- **Galinkin & Sablotny (2024)** "Improved Large Language Model Jailbreak Detection via Pretrained Embeddings" (arXiv 2412.01547) — 使用 pretrained encoder embeddings 做 jailbreak detection，方法高度相关 [R1 + R2 共识需补充]

---

## External Review

外部审稿：未启用（项目配置未开启 paperreview.ai）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（1 warning + 13 info）。主要发现：

- **[warning] Page 6 拥挤**：单页堆叠 Figure 2 + Figure 3 + Table 3，bar chart 被压缩，axis labels 和 legend 字号接近可读下限。建议将 Figure 3 或 Table 3 移至下一页。
- **[info] Page 1 无视觉锚点**：首页全为文字（Title/Abstract/Intro），Figure 1 出现在 p2。
- **[info] Page 8 仓促收尾感**：末页包含 5 个 section 起始（4.7、4.8、5、6、7），Section 5 和 6 篇幅极短。
- **[info] Figure 4 偏小**：单栏内两个散点 sub-panel，改为 figure*（双栏全宽）可提升可读性。
- **[info] 表格排版专业**：统一 booktabs 风格，最优值加粗，小数位数一致。
- **[info] 格式合规**：正文 8 页 + Limitations 在 p9 不计页数 + References 2.5 页 + Appendix 13 页。无 [?] 未解析引用。

---

## Overall Assessment

**Overall Score: 3.0 / 5 — Findings**

**评分理由：**

本文是一篇执行质量极高的经验性消融研究。消融设计方法论严谨（7 个 controlled variants），统计分析全面（bootstrap CI + permutation test + TOST），negative results 诚实报告，附录极为详尽（16 页）。这些优点使论文远超平均水平的实验论文。

但三个核心限制使其更适合 Findings 而非 main conference：

1. **新颖性有限**：核心发现（classification DAPT > MLM > vanilla）可从 Gururangan et al. (2020) 预期。Scrambled ≈ 9-class 这个最有洞察力的发现（W5）未被充分开发为主要贡献。

2. **外部效度不足**：全合成数据训练和评估使所有 findings 局限于 synthetic regime。ToxicChat 上的 hierarchy 反转（W2）表明核心结论是 condition-specific 而非 universal，实质上降低了论文的 impact。

3. **贡献深度**：论文的 take-away 最终是 "adaptation strategy depends on data distribution and evaluation condition"——虽然有实证价值，但作为 main conference 贡献显得不够 "exciting"（ARR excitement 标准）。

**推荐**：Findings 接收。论文的实验方法论模板价值、诚实的 negative results 报告、以及 few-shot benign adaptation 的实用发现足以支撑 Findings 级别的贡献。

**置信度: 4/5** — 两位 Reviewer 仔细阅读了全文 + 附录，熟悉 domain adaptation 和 LLM safety 文献。

---

## Detailed Comments

### Abstract
- 约 173 词，符合 200 词限制 ✅
- "this hierarchy reverses" 后的句法结构可更清晰（W12）
- Few-shot FPR 数字应标注 "on WildChat" 来源

### Introduction (Section 1)
- 三个 "unexpected findings" (i)(ii)(iii) 的组织清晰
- "to our knowledge, [first] controlled factorial study" 限定到位
- 但 contribution bullet 1 的信息密度过高

### Related Work (Section 2)
- 主要覆盖充分（Crescendo, FTTD, ActorAttack, RED QUEEN, WildGuard, ShieldGemma, Llama Guard 等）
- 缺少 Galinkin & Sablotny (2024) — encoder-based detection 的近期工作（W9）

### Method (Section 3)
- 7 个 variant 的设计逻辑清晰
- BiGRU 的选择理由应更明确说明是为分析便利性而非检测需要（W7）
- κ=0.78 n=50 的标注验证应增强（W8）

### Experiments (Section 4)
- 4.1 Data：scope qualifier 到位（"on synthetic data"）
- 4.3 Decomposing：scrambled ≈ 9-class 是最有价值的发现，但当前叙事未充分展开（W5）
- 4.5 Mixed-LLM：AA=0.504 ≈ chance level 的诚实报告值得肯定
- 4.6 Human Data：ToxicChat 反转是论文最重要的 negative result，归因（"distributional differences"）需更深入分析

### Discussion (Section 5)
- Discriminative compression 分析有价值但因果语言已适当弱化
- Cross-condition transfer 段落诚实讨论了 ToxicChat 反转和 WildChat FPR
- Length confound 段落提供了合理的反证据

### Conclusion (Section 6)
- "reusable template" claim 应限定范围（W10）
- 其他 claims 基本在证据范围内

### Limitations (Section 7)
- 3 个 bullets 覆盖合理：synthetic data, IID benign upper bound, scope
- 可增加 scale 对因子排序的影响讨论（W13）
