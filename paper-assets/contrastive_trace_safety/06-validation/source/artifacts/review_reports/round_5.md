---
round: 5
overall_score: 3.0 (Findings)
timestamp: 2026-05-18T01:53:13.599238+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 6

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 via ARR May cycle (Findings track)
**Deadline**: 2026-05-25
**审稿人**: Reviewer 1 (方法严谨性+实验设计), Reviewer 2 (新颖性+完整性+写作质量)
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）

---

## Summary

本文研究推理模型中 hidden-state (HS) 探针与 text 探针对 safety commitment 检测的对比，核心方法论发现是层选择指标中的 crossing rate 组件会系统性选出浅层，在 32B scale 上逆转 HS vs text 的对比结论。论文在 corrected layers 上报告 HS 探针在 4 个模型上统计显著优于 text 探针（Holm-Bonferroni 校正），并系统报告了 7 种替代方法的 negative results。新增 PCA-384d 维度控制和 BGE-large encoder robustness check。

---

## Strengths

1. **层选择敏感性发现有重要方法论价值** [R1,R2 共识]：crossing rate 偏好浅层的机制分析清晰，五指标消融设计合理，对整个 probing 文献有警示意义。

2. **实验覆盖面好** [R1,R2 共识]：4 模型跨 2 架构（Llama, Qwen）、2 训练方法（R1 distillation, STILL）、2 规模（7-8B, 32B），避免单模型过度泛化。

3. **透明度在同领域论文中突出** [R1,R2 共识]：M002 bug disclosure（Appendix F）在 ML 论文中罕见；control task、position baseline、7 种 negative results 的完整报告；Limitations section 诚实覆盖 7 个具体限制。

4. **统计方法论总体严谨** [R1,R2 共识]：Holm-Bonferroni 12-test 校正、PCA 维度匹配、BGE-large encoder robustness check 构成多层验证体系，远超该领域多数 empirical study。

5. **Temporal windowing 分析全面** [R1]：7 种窗口大小 × 4 模型 × 2 模态的完整消融，提供实用部署指导。

6. **写作质量良好** [R2]：无 em-dash、无用词黑名单词汇、无过度分段。Discussion/Conclusion 重复问题（跨 5 轮历史 issue）已修复，Conclusion 压缩为 3 句。

---

## Weaknesses

### Critical (Must-Fix)

**W-C1. BGE-large 结果（1/4 显著）被藏在附录，核心 HS advantage claim scope 需调整** [R1-N3 + R2-N2，完全共识]

当 text encoder 从 MiniLM-384d 升级到 BGE-large-1024d 时，仅 OT-7B 的 HS 优势在 HB 校正后仍显著（+18.1pp, p<0.001）。其余 3 模型不再显著：R1-8B +5.8pp p=0.185; R1-32B +11.7pp p=0.027 不过 HB; QwQ +9.4pp p=0.132。3/4 模型的 CI 包含 0。

论文在主文仅用一句话处理（"effect sizes narrow for the remaining models, consistent with the prediction in our Limitations"），将详细数据放附录。R2 精确指出：Limitations 中的"预测"被实验证实后，它不再是 limitation 而是 finding——一个 finding 不应被藏在附录中。

核心 claim "HS probes significantly outperform text probes on all four models" 对 encoder 选择高度敏感。如果此 claim 需要依赖特定的弱 text baseline 才成立，claim scope 必须重新限定。

**修复要求**：(1) Section 4.2 增加完整段落正面讨论 BGE-large 结果；(2) Abstract 中 precision gains 注明 "vs MiniLM baseline"；(3) Contribution 2 调整为 "HS significantly outperforms a 384d sentence encoder; with stronger encoders, the advantage narrows and becomes model-dependent"。

**W-C2. Abstract/Introduction 对 QwQ-32B 不利证据呈现严重不足** [R2-N1 + R1-W4→AGREE，完全共识]

Abstract 用 "model-specific detection timing trade-offs at 32B scale" 掩盖三个关键事实：
- QwQ position-only baseline bal_acc (0.746) > HS probe (0.740)
- QwQ HS lead time 为负（−1.2 to +1.9 steps），text 为 +3.7 to +12.3 steps
- Position baseline margin 仅 −0.6pp

Contribution 2 "Consistent HS advantage at corrected layers" 中的 "consistent" 在 QwQ 语境下 misleading——统计显著性 ≠ 实用性优势。论文在 Section 4.3-4.4 诚实报告了数据，但 Abstract/Introduction 的 framing 与实验证据存在系统性偏差。

**修复要求**：(1) Abstract 将 "model-specific timing trade-offs" 替换为具体描述；(2) Contribution 2 从 "Consistent" 改为 "Statistically significant...with model-specific practical trade-offs"；(3) Introduction 用 1-2 句明确 QwQ 的 position baseline 竞争力和负 lead time。

**W-C3. "12/12 Holm-Bonferroni" 呈现方式给出独立性错觉** [R1-N1，R2 AGREE（presentation issue 非 soundness issue）]

全文多处强调 "12/12 tests pass"（Abstract, Introduction, Section 4.2, Conclusion, Appendix B），给读者 12 条独立证据的印象。但论文自己承认 3 个 metrics "positively correlated by construction"。HB 在正相关下统计上 valid（更保守），但 "12/12" 的修辞效果系统性高估了证据强度。有效独立确认约为 4 个模型 × ~2 个独立 metric families。

**修复要求**：(1) 主文改为 "all 4 models × 3 correlated metrics"；(2) 保留 HB 在正相关下更保守的说明；(3) Appendix B 标注同模型内的相关指标组。

**W-C4. 32B 效应量缺失 95% CI** [R1-N2，R2 AGREE]

Table 2 报告 4 模型的 Δ 值（precision +15.4 to +23.6pp）但无 CI。n=19-20 的 32B 模型 CI 宽度对评估效应量可靠性至关重要。仅 Appendix E（OT-7B）给出 CI。Bootstrap 已经跑了，补充成本极低。

**修复要求**：Table 2 增加 precision Δ 的 95% CI 列；R1-32B 5-trace precision 单独报告 CI。

### Warning (Should-Fix)

**W-S1. "四个互补指标收敛"实质独立性 ≈ 2** [R1-W1，R2 AGREE]
Precision 和 inverse FPR 在 binary classification 下数学耦合；additive composite 由前三者派生。真正独立收敛信号约 2 个 metric families（accuracy-based + FP-based）。
→ 改为 "metrics from two complementary measurement families converge"；量化 rank correlation。

**W-S2. PCA-384d 控制实验未报告哪 2/12 测试失败** [R1-W2，R2 AGREE]
10/12 通过但未说明失败的 model×metric 组合。若两个失败在 32B 模型则进一步限定结论。论文在 Mahalanobis 分析中已证实 safety signal 在 minor PCA components 中，PCA 降维可能恰恰丢弃关键信号。
→ 报告具体失败组合；讨论方差损失影响。

**W-S3. R1-32B W=1 precision 基于 5 个 detected traces** [R1-W3，R2 AGREE]
Coverage 25%（5/20），基于 5 样本的 precision 有极大抽样方差。C=1.0 regularization 在 p>>n（51200 features, n=20）下适当性未讨论。
→ 报告 5-trace precision CI；讨论 regularization 适当性或 C 值 sweep。

**W-S4. Negative results framing 仍偏笼统** [R1-W7 + R2-W2，完全共识]
"Inconsistent or limited results" 比 "all fail" 更好，但仍将 7 种方法笼统归类。RepE-QwQ 0.756 bal_acc（接近 supervised 0.778）不应归为 failure。BOCPD 93% detection rate（on R1-8B）有部署价值。
→ 改为 "no method consistently matches supervised probing across models"；RepE-QwQ 单独讨论为 partial success。

**W-S5. Related Work 仍缺 3 篇高相关论文** [R2-W3，R1 AGREE 3/4]
38 篇引用已大幅改善，但仍缺：
1. Stechly et al. 2025 "Reasoning Models Know When They're Right" (arXiv:2504.05419) — HS probing on reasoning models for correctness，方法论几乎相同
2. "Where Does Reasoning Break?" (arXiv:2605.13772, 2026) — step-level HS geometry for hallucination detection
3. "When Models Outthink Their Safety" (arXiv:2510.21285) — Chain-of-Guardrails for self-jailbreak
前两篇是直接相关工作，审稿人很可能注意到缺失。

**W-S6. AUROC 选中层但缺中层处 HS vs text 对比** [R1-W6，R2 partial REBUT]
R2 反驳 "轻描淡写" 的判断（论文已 acknowledge AUROC 分歧作为层选择敏感性佐证），但同意缺少 AUROC 最优层处的 HS vs text 比较。无论结果如何都是核心论点的天然验证。
→ 报告 AUROC 最优层处的 HS vs text 对比。

**W-S7. 小样本 bootstrap 有效性未讨论** [R2-W4，R1 AGREE]
n=19-20 的 bootstrap CI 覆盖率在 n<30 时可能偏低（Efron 建议 n≥25）。p<0.001 在 1000 resamples 下可能是分辨率限制 artifact。
→ Limitations 或 Method 中简短讨论；考虑补充 permutation test。

**W-S8. 跨方法比较未标注数据划分差异** [R1-W5，R2 AGREE]
60/20/20（LR）vs 70/30（GRU）vs merged（two-stage），主文跨方法对比时未每次标注。
→ 每次跨方法比较标注划分。

### Minor

- Discussion 段落 1 过长（15+ 句），建议拆分 [R2-M3，R1 agree]
- Responsible NLP Checklist 未讨论 dual-use 风险 [R2-M5，R1 agree]
- Method/Experiments bootstrap 描述重复；Appendix G control task 段落内重复 [R1,R2 共同发现]
- Abstract 中 n 值信息密度过高 [R1,R2]
- 个别 bib 年份需核实 [R2-M6]

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 独立发现或交叉确认后完全同意：

1. **BGE-large 结果是核心 claim 的最重要反驳证据，不应仅放附录** — R1 和 R2 独立将此列为 Must-Fix，交叉分享中双方完全同意。R2 提供了精确的 framing 观察："Limitations 中的预测被实验证实后，它不再是 limitation 而是 finding"。

2. **QwQ-32B 的 position baseline 竞争力和负 lead time 必须在 Abstract/Introduction 中透明呈现** — R2 首先标记为 N1，R1 在交叉回应中 AGREE 并补充了 Appendix G 和 Limitations 的佐证数据。

3. **"12/12 HB" 的呈现虽然统计上 valid 但修辞上 misleading** — R1 首先标记，R2 AGREE 并区分了 soundness issue vs presentation issue。

4. **Negative results framing 需更精确** — 两人独立标记（R1-W7, R2-W2），交叉互相 AGREE。

5. **32B CI 缺失和小样本 bootstrap 问题** — 两人从不同角度覆盖同一地带（R1: CI 缺失；R2: bootstrap 有效性）。

---

## Reviewer Divergence [REBUT]

仅两处，均为程度分歧而非根本矛盾：

1. **Novelty 评估** (R2-W1 vs R1 REBUT)：R2 认为层选择敏感性仅在安全 probing 验证，novelty 偏窄。R1 反驳：机制是通用的（crossing rate 偏好浅层因 volatility，不特定于安全任务），且论文已用 "We hypothesize" 诚实标注 scope。共识：对 Findings track 的 novelty 门槛充分，但推广价值的上限存在分歧。

2. **AUROC 讨论的充分性** (R1-W6 vs R2 partial REBUT)：R1 认为被"轻描淡写"。R2 反驳：论文已 acknowledge AUROC 分歧作为层选择敏感性的额外证据，非轻描淡写。但 R2 同意缺少 AUROC 最优层处的 HS vs text 对比。共识：需补充该对比，但 severity 分歧（R1: warning; R2: nice-to-have）。

---

## Questions (需作者在 author response 中回答)

1. PCA-384d 实验中失败的 2/12 测试具体是哪个模型的哪个指标？
2. 如果 AUROC 用于层选择（选出 ~50% depth 中层），HS vs text 在该层的 precision 和 balanced accuracy 对比如何？
3. R1-32B 在 C=1.0 条件下的 5-trace precision 的 95% bootstrap CI 是多少？是否做过 C 值敏感性分析？
4. 论文是否考虑过 BCa bootstrap 或 permutation test 作为小样本下的 robustness check？

---

## Missing References

1. **Stechly et al. (2025)** "Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification" — arXiv:2504.05419 [R2 raise, R1 verify: 应当引用，方法论高度相关]
2. **"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry"** (2026) — arXiv:2605.13772 [R2 raise, R1 verify: 应当引用]
3. **"When Models Outthink Their Safety"** (Mao et al. 2025) — arXiv:2510.21285 [R2 raise, R1 verify: 应当引用]
4. **SCoT** (arXiv:2501.19180) — [R2 raise, R1: nice-to-have，非必须]

---

## Overall Assessment

**评分: 3.0 (Findings)**
**置信度: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3/5 | 2.5/5 | 2.5/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |

两位 Reviewer 独立给出相同评分（3.0 Findings），交叉分享后维持。

**核心判断**：层选择敏感性是一个真实且有方法论价值的发现，实验设计总体认真，透明度在同领域突出。但论文存在系统性的 "overstatement without misstatement" 模式：12/12 的独立性错觉、BGE-large 结果被边缘化、QwQ 不利证据在 Abstract/Intro 中模糊处理、四指标独立性夸大。这些不是统计错误——统计方法本身是 valid 的——而是呈现方式系统性高估了证据强度。

BGE-large 结果（1/4 显著）是最具影响的 concern：如果 HS advantage 的普适性依赖特定的弱 text baseline，论文的核心叙事需要重新 scoping。层选择方法论贡献本身足以支撑 Findings 级别，但 "consistent HS advantage" claim 需要更诚实的边界。

**修复路径**：4 个 critical issues 中，3 个是 framing/presentation 修改（W-C1 BGE-large 入正文、W-C2 QwQ caveat 上提、W-C3 12/12 表述），1 个是低成本数据补充（W-C4 CI 列）。无需重做实验。修复后论文可达 Findings 稳固接收水平。

**风险评估**：若 W-C1 和 W-C2 未修复，ARR reviewer 很可能将 framing bias 视为 critical issue，评分可能降至 2.5 (Borderline Findings)。

---

## Detailed Comments (逐节)

### Abstract
- ~190 words，在 150-250 范围内。数字密度偏高但可接受。
- **需修改**：(1) "precision gains of +15 to +24pp" 注明 "vs MiniLM-384d baseline"；(2) "model-specific detection timing trade-offs" 替换为更具体的 QwQ caveat；(3) "12 tests" 改为 "all four models, each on three correlated metrics"。

### Introduction
- 5 段叙事结构完整，从问题到贡献的逻辑链连贯。
- **需修改**：Contribution 2 从 "Consistent HS advantage" 改为 "Statistically significant HS advantage with model-specific practical trade-offs"，并用 1-2 句明确 QwQ 的 position baseline 竞争力。

### Related Work
- 4 个主题段落组织清晰，38 篇引用覆盖主要领域。positioning 清晰。
- **需修改**：补充 3 篇高相关论文并 positioning。

### Method
- Problem setup, probe architecture, layer sensitivity, baselines, evaluation protocol 均清晰。
- **需修改**：与 Experiments 的 bootstrap/HB 描述去重。

### Experiments
- 层选择消融 + HS vs text + 32B 分析 + temporal context + negative results 结构合理。
- **需修改**：(1) Table 2 增加 CI 列；(2) Section 4.2 "Dimensionality control" 扩展为完整的 encoder robustness 讨论（整合 BGE-large）；(3) 12/12 表述调整；(4) Negative results framing 精化。

### Discussion
- 四个主题段落覆盖层选择方法论、temporal context、cross-model divergence、design implications。
- **需修改**：段落 1 拆分为 2 段；AUROC 分歧处增加中层 HS vs text 对比数据。

### Conclusion
- 3 句，简洁。与 Discussion 无逐句重复。无需修改。

### Limitations
- 7 个具体限制诚实列出。
- **需修改**：增加小样本 bootstrap 有效性讨论。

### Appendix
- Checklist、layer sweep、HB table、window ablation、OT-7B details、GRU details、control task、oracle、BOCPD、bug disclosure、two-stage、temporal details、negative details、transfer details、encoder robustness。结构完整。
- **需修改**：(1) Appendix G control task 去重；(2) Checklist 增加 dual-use 讨论。

### 格式合规
- ACL template `[review]`：✓
- Double-blind 匿名：✓（"Anonymous ARR Submission"）
- Limitations section 位置：✓（Conclusion 后 References 前）
- Responsible NLP Checklist：✓（内容需补充 dual-use）
- 引用格式（natbib）：✓

---

## 历史 Issue 追踪摘要

| 状态 | 数量 | 说明 |
|------|------|------|
| 本轮确认修复 | 3 | R5-W4(Discussion/Conclusion重复), R5-W5(泛化claim降级), R2-W11(Conclusion压缩) |
| 部分修复/进展中 | 5 | R5-N1(维度控制实验done但framing问题), R5-W2(framing改善但不够精确), R5-W3(38→仍缺3篇), R2-W14(实验done framing open), R2-W7(划分标注done但跨方法比较未标) |
| 未修复 | 3 | R5-N2(12/12表述), R5-N3(QwQ Abstract/Intro), R5-W1(32B CI) |
| 本轮新增 | 7 | R6-N1(BGE-large入正文), R6-W1(PCA 2/12), R6-W2(R1-32B 5-trace CI), R6-W3(AUROC层对比), R6-W4(小样本bootstrap), R6-M1(段落拆分), R6-M2(dual-use) |
