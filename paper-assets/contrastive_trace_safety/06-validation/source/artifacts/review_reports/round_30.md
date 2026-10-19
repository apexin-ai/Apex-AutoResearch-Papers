---
round: 30
review_mode: fresh
overall_score: 3.5 - Borderline Conference (Findings recommended)
timestamp: 2026-05-21T19:21:25.996469+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 30 (Fresh Review)

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 via ARR | **Deadline**: 2026-06-15
**Reviewer 编排**: R1 (方法严谨性) + R2 (新颖性/完整性) | 1 轮初审 + 交叉分享，共识收敛

---

## Summary

本文系统研究了 layer selection metric 的选择如何影响 hidden-state (HS) vs text probe 在 safety commitment point (CP) 检测中的比较结论。核心发现是 crossing-rate composite 系统性选择浅层（产生 p=0.83），而 threshold-based metrics 选择深层（产生 p<0.005），同一数据上可产生定性逆转。论文在 4 个 reasoning model（3 Qwen, 1 Llama）、两种规模（7-8B, 32B）上进行了系统实验，统计处理严谨（nested CV, Holm-Bonferroni, exact permutation），但新颖性受制于这本质上是已知 probing sensitivity 问题在 safety 领域的验证，且所有 CP-dependent claims 依赖单一数据集 HarmThoughts。

---

## Strengths

1. **统计方法论标杆级别**: nested 5-fold CV（7-8B）、Holm-Bonferroni step-down 12 tests、exact sign-flip permutation（32B primary inference）、三级证据分级（cross-validated / significant / exploratory†）、random-label controls、control task selectivity——统计处理远超同领域平均水平。[R1, R2 consensus]

2. **Transparency 异常突出**: 32B sample limitations 标记为 †、false positive rates 11-50%、encoder-conditional advantage、position mediation confound——几乎没有 overclaim。Section N（Appendix）公开报告 QwQ-32B text probe bug 及修正过程，为研究诚信树立了高标准。[R1, R2 consensus]

3. **Negative results 完整记录**: 7 种 alternative methods（BOCPD, CUSUM, Mahalanobis, RepE, MLP, CCS, cross-model transfer）全部失败，附录提供详细配置和失败原因分析，对社区有参考价值。[R1, R2 consensus]

4. **Layer selection taxonomy 可操作**: 5 种 metric 分类（crossing-rate vs threshold-based）及 multi-metric audit 建议为后续 probing 研究提供了实用检查清单。[R2]

5. **低复现门槛**: <4 GPU-hours、详尽超参数报告（32 页含附录）、承诺代码公开。[R1, R2 consensus]

6. **强大的控制任务设计**: 随机标签 selectivity 实验（Appendix H）提供了真正的证据表明探针捕捉了安全相关结构而非表面相关性。[R1]

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [consensus, major] Contribution 1 新颖性受限——已知问题的领域迁移**
Belinkov (2022) 已系统讨论 probing metric sensitivity；Tenney et al. (2019) 已确立 layer-wise information gradient。论文自承 "Prior work has noted metric sensitivity in probing"。crossing-rate composite 选浅层因浅层 cosine compression 导致频繁 threshold crossing，机制可预测。R1 部分反驳认为 qualitative reversal（p=0.83 vs p<0.005 的二元结论翻转）超越了已知的"数值差异"，有独立实证价值。但两位 Reviewer 均认为需更明确阐述增量贡献——建议在非 safety probing 任务上做对比验证 safety-specificity。
*R2: critical → R1 partial rebut → consensus: major*

**W2 [consensus, major] 单一数据集限制所有 CP-dependent claims**
全部 CP-dependent claims 依赖 HarmThoughts，annotations 缺乏 formal human IAA（仅 AdvBench LLM proxy κ=0.606）。AdvBench 分析仅验证几何属性（1.67× cosine ratio），未验证 probe performance 或 layer selection reversal。HarmThoughts 是唯一有 step-level CP annotation 的公开数据集（论文 Limitations 已说明），但 structural limitation 仍限制泛化性。R1 指出 layer selection sensitivity 发现（Table 2）不依赖 CP、与 CP 正交，可部分缓解此问题。
*R2: critical → R1 agrees, downgrades to major → consensus: major (structural, Findings acceptable)*

**W3 [consensus, major] 有效自由度估计不充分（196-448→12）**
层选择步骤在验证集上搜索了 28-64 层 × 7 窗口 = 196-448 个候选配置，但最终仅报告 12 个 Holm-Bonferroni 检验。论文 Appendix W 的三个论据（指标冗余、验证/测试分离、K 固定）对 7-8B（有 nested CV）有效，但 32B 模型缺乏 nested 结构（仅 LOO-CV），且 Appendix W 末句对 Type I error 的承认被埋在附录中。主文需加入 conditional inference caveat。
*R1: critical → R2 AGREE → consensus: major (7-8B mitigated by nested CV, 32B remains gap)*

**W4 [consensus, major] 架构多样性不足（3/4 Qwen, 1 Llama）**
Crossing-rate geometric bias 部分 Qwen-specific（Appendix B.1 random-label controls: QwQ retained, R1-8B dissolved）。R1-8B 是 R1-distilled Llama，其 hidden state 分布可能已被蒸馏改变，不完全代表原生 Llama。Title "Reasoning Models" 未限定架构覆盖范围。直接削弱 Contribution 1 的泛化性声明。
*R1, R2 consensus: major*

### Should-Fix（影响评分但不一票否决）

**W5 [consensus, major] "Doubly conditional" framing 误导**
Abstract/Contributions 将 HS advantage 描述为 "doubly conditional" on encoder quality AND position overlap。但 metric **决定** layer（因果链），两者不是独立条件。实际关系是 metric → layer → conclusion 单一因果链。正文（Section 4.2-4.4）正确解释了逻辑关系，但 abstract 简写误导读者以为存在两个正交自由度。建议改为 "conditional on metric-induced layer selection" 或明确因果关联。
*R1-W2, R2-W4 consensus*

**W6 [consensus, should-fix] 32B exploratory 结果在 abstract 过度呈现**
Abstract 引用 QwQ-32B "+19.2pp" 和 R1-32B "+15.4pp" 但未标注 exploratory（n≤20）。读者仅读 abstract 会产生 validated findings 印象。正文 Section 4.4 framing 合理（"Both 32B results are exploratory"），但 abstract 必须同步。R1-32B 残差化后 HS-text gap 仅 +1.9pp，远低于 MDE ~9pp，与零效应不可区分——论文应明确指出。
*R1-W6 + R2-W3 consensus*

**W7 [R1, should-fix] BCa bootstrap 在 32B（n≤20）下可能反保守**
BCa 校正需从 19-20 个 jackknife 副本估计 â 和 ẑ₀，统计文献指出 n<25 时可能 CI 偏窄。R2 反驳认为论文已将 exact permutation test 作为 32B primary inference、BCa 仅辅助，severity 应降级。Consensus: permutation test 缓解了主要风险，但建议补充 percentile bootstrap CI 作为 sensitivity check，并引用 Carpenter & Bithell (2000)。
*R1: critical → R2 rebut → consensus: should-fix*

**W8 [R2, should-fix] Multi-metric ensemble 被埋在附录**
Appendix Z.1 报告 multi-metric layer ensemble 完全消除 metric-induced bias（p≤0.002），但仅在附录最后半页出现。两位 Reviewer 均认为这可将论文从"诊断问题"提升为"诊断+解决问题"，增强实践价值。但需 CV 验证方可提升为正文贡献。
*R2-Q3 + R1 AGREE*

### Minor

**W9 [R1, minor]** C=1.0 默认值缺乏原则性理由（已有 C sweep <2pp 变化）
**W10 [R1, minor]** AUROC 排除削弱与先前工作可比性（R2 反驳: Appendix Y 已提供 AUROC 分析）
**W11 [R1, minor]** Figure 1 heatmap 字号偏小（约正文 60%），metric 名称和 layer 编号 150dpi 下勉强可读
**W12 [R2, minor]** CP 定义是 HarmThoughts 16-label taxonomy 的二值化衍生（R1 反驳: CP 未被列为 contribution，且有非平凡的时序解读）

---

## Reviewer Consensus [AGREE]

1. **架构多样性不足是结构性限制**: 3/4 Qwen + crossing-rate bias 部分 Qwen-specific → 泛化性受限 [R1 AGREE R2-W2, R2 AGREE R1 Limitations comment]
2. **"Doubly conditional" 表述需修正**: metric→layer 是因果链而非独立条件 [R1-W2 + R2-W4 mutual AGREE]
3. **Abstract 必须标注 32B 为 exploratory**: 当前数字密度过高且未标注 sample-limited [R1 partial AGREE R2-W3]
4. **有效自由度主文需 conditional inference caveat**: Appendix W 讨论不够，应在正文体现 [R2 AGREE R1-N2]
5. **单一数据集是 Findings-level 可接受的结构限制**: HarmThoughts 是唯一 step-level CP 公开数据集 [R1 AGREE R2-N2, both 认为 Findings 可接受]
6. **Multi-metric ensemble 有提升潜力**: 应考虑从附录提升到正文 [R1 AGREE R2-Q3]
7. **R1-32B position-corrected 效应与零效应不可区分**: +1.9pp vs MDE 9pp [R2 AGREE R1-W6]

## Reviewer Divergence [REBUT]

1. **C1 新颖性 severity**: R2 评为 critical（已知问题的领域迁移），R1 partial rebut 降为 major（qualitative reversal 有独立价值）。→ **Consensus: major**，但 R2 的增量性关切成立。
2. **BCa severity**: R1 评为 critical，R2 rebut（permutation 已是 primary inference）。→ **Consensus: should-fix**。
3. **CP 原创性**: R2 评为 major，R1 rebut（CP 未被列为 contribution，是工具性定义）。→ **R1 论据充分，W12 降为 minor**。
4. **GRU data split**: R1 评为 major，R2 rebut（60/20/20 GRU 已在 Appendix F Table 16）。→ **R2 纠正有效，降为 minor（叙述组织问题）**。
5. **Crossing-rate artifact vs contribution**: R1 认为 crossing-rate 浅层偏好是构造伪影需更明确区分；R2 认为 documenting 此 artifact 本身就是 C1 贡献。→ **Both valid**：C1 需在正文（而非仅附录）明确展示 artifact vs signal 区分。

---

## Questions（需要作者回答）

1. 对 32B BCa CI，是否对比过 percentile bootstrap CI？如果 BCa 校正不稳定，Table 3 CI 可能系统性偏窄。[R1-Q1]
2. Crossing-rate composite 是否有先前 safety probing 工作实际采用？如无，C1 的 "correcting a mistake no one has made yet" 定位如何调整？R1 rebut 认为 crossing rate 作为一类指标在时间序列分析中是自然选择。[R2-Q2]
3. Multi-metric ensemble（Appendix Z.1, p≤0.002）为什么不提升为正文方法贡献？[R2-Q3, R1 AGREE]
4. 是否尝试过在 AdvBench 上用 binary jailbreak/safe label 做 probe training + layer selection 实验（不需要 CP，验证 metric divergence 是否复现）？[R2-Q1, R1 AGREE]
5. R1-32B 残差化 HS-text gap +1.9pp (p=0.914)，能否准确说 R1-32B 在位置校正后未检测到 HS 优势？[R1-Q4, R2 AGREE]
6. CP perturbation ±2 步 BA<2.5pp（Appendix I），但 ±3/±5 步分析缺失。IAA MAD=8.5 步下，主要结论对更大扰动的敏感度如何？[R1-Q6]

---

## Missing References

1. **[must-cite]** "First is Not Really Better Than Last: Layer Choice and Aggregation" (arXiv 2511.04715) — layer choice 对 probing 结论的影响，与 C1 直接对话 [R2 建议, R1 AGREE "高度相关"]
2. **[should-cite]** "Stop Before You Fail: Operational Capability Boundaries" (arXiv 2509.24711) — hidden states failure prediction，与 CP 概念交集 [R2 建议, R1 AGREE]
3. **[should-cite]** "Exposing the Ghost in the Transformer: Hidden State Forensics" (arXiv 2504.00446) — 层级 activation pattern safety 检测 [R2 建议, R1 AGREE]
4. **[should-cite]** Carpenter & Bithell (2000) "Bootstrap confidence intervals" — BCa 小样本性质讨论 [R1 建议]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 paperreview.ai）。

---

## Visual Layout Check（非评分项）

**状态**: done (耗时 3m23s)
**结果**: 3 warnings, 4 info

| Severity | Finding |
|----------|---------|
| ⚠️ warning | 前 5 页无实质性视觉锚点：Figure 1 直到 p7，审稿人需翻过 5 页密集文本。建议 p1-2 加概念图 |
| ⚠️ warning | pp3-5 连续纯文本（Related Work + Problem Setup），无 figure/table 穿插 |
| ⚠️ warning | 6 个 display items 全集中在最后 3 页主文（p6-8），前 5 页仅 1 个 Table 1，节奏头轻脚重 |
| ℹ️ info | Figure 1 heatmap metric 名称和 layer 编号字号偏小（约正文 60%） |
| ℹ️ info | Table 1 仅 4 模型基本信息，作为论文第一个 display item 信息价值有限 |
| ℹ️ info | 3 页（p10, p21, p22）渲染为空，建议手动确认 PDF 完整性 |
| ℹ️ info | Appendix 20 页含 30+ 表格 + 3 figure，格式统一 |

**持续问题**: 前 5 页 text wall 和 display items 后置集中已连续 8 轮被标记（R23-R30），建议优先级提升。

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

**Soundness: 3.5/5** — 统计框架整体严谨（nested CV, HB, exact permutation），但 32B 小样本推断存在 BCa coverage 和有效自由度隐患，单数据集限制泛化性。

**Excitement: 2.5-3/5** — Layer selection sensitivity 是 probing 方法论的重要发现，对安全监控有实践意义，但本质上是已知问题（Belinkov 2022）在新领域的量化验证。"Layer selection matters" 对 NLP 社区属于 "known but worth documenting" 而非 "surprising"。

**Confidence: 4/5** — 两位 Reviewer 均熟悉 probing methodology 和 LLM safety 领域。

**推荐**: 更适合 **Findings** 而非 Main Conference。方法论贡献扎实但增量性质明显；统计处理和 transparency 远超同领域平均水平，负面结果有社区参考价值；但新颖性受限（C1 增量、单一数据集、3/4 Qwen 架构）使其难以达到 Main Conference 的 excitement 门槛。若解决 abstract 修正（标注 32B exploratory、简化 "doubly conditional"）、conditional inference caveat、以及在非 safety task 上验证 reversal severity，可稳固 Findings 接收。

**EMNLP 评分映射**: 3.5 = Borderline Conference。两位 Reviewer 独立评分一致，交叉分享后维持。核心分歧（C1 novelty severity、BCa severity）已通过交叉讨论收窄至 severity 层面，无实质性方向性矛盾。

---

## Detailed Comments

### Abstract
- 过度密集，一段内塞入 precision gains、p-values、layer divergence、32B exploratory results，可读性差 [R2]
- 32B 具体数字（+15 to +19pp）未标注 exploratory [R1, R2 consensus]
- "Doubly conditional" 简写误导 [R1, R2 consensus]
- 建议：前 2 句 motivation，中间 2-3 句 core finding（metric reversal + 机制），末尾 1 句 implication；具体数字移入正文

### Introduction (Section 1)
- 叙事逻辑清晰（problem → gap → contribution）[R2]
- Contribution 1 framing 过于强调 "qualitative reversal" 而弱化对 Belinkov (2022) 的 acknowledgment [R2]
- 动机有说服力：先前工作将层选择视为次要细节 [R1]

### Related Work (Section 2)
- 覆盖面广（82 refs），Chan et al. (2025) 区分充分 [R2]
- 密度过高：SafeDream/HiddenDetect/SafeInt/RCS 等仅 one-sentence mention 可精简 [R2]
- 缺少 "First is Not Really Better Than Last" (layer choice, must-cite) [R1 AGREE]

### Problem Setup (Section 3)
- CP 定义清晰，temporal windowing 和 probe architecture 描述紧凑 [R1]
- C=1.0 默认值需理由或内层 CV [R1-W4]
- Crossing-rate composite 应预先讨论浅层偏好的几何机制 [R1-W3]
- K=5 消融仅在附录（Table 22），主文简要提及会加强叙事 [R1]

### Experiments (Section 4)
- Evidence gradient 分级是好的设计 [R1, R2]
- Table 2 是论文最强发现（系统性浅/深层分歧）[R1]
- Table 3 应承认 32B BCa CI 局限性 [R1-N1]
- Section 4.4（32B analysis）篇幅与证据力度不匹配 [R2]
- Table 2 caption 使用 4 个脚注标记，认知负担高 [R2]

### Discussion (Section 5)
- 仅半 column，过度压缩 [R29-W2]
- Multi-metric audit 建议有实用价值但 ensemble solution 被埋附录 [R2]
- 应补入 cosine compression 关键发现摘要 [R29-W2]

### Conclusion (Section 6)
- 简洁准确，适当限定 claims [R2]
- QwQ-32B positional confound 未 caveat [R26-W2]

### Limitations
- 覆盖主要弱点（单数据集、32B power、架构覆盖、causal status）[R1, R2]
- 未说明只用一个数据集的具体原因（资源 vs 数据不可得）[R2]
- 建议补充 oscillating traces 频率 [R23-W3]

### Appendix
- 22 页内容丰富，格式统一 [R1, R2]
- Section N（bug 披露）是 transparency 范例 [R1]
- Section Z.1（ensemble）是 substantial finding，不应只在附录 [R2, R1 AGREE]
- Section W（有效自由度）论点需加强 [R1-N2]
