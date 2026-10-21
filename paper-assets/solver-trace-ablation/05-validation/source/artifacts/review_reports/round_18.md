---
round: 18
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-20T08:53:36.834504+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 18 (Fresh Review)

**论文**: Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study
**Venue**: EMNLP 2026 (Long Paper, ARR May cycle)
**Deadline**: 2026-05-25
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）
**审稿轮次**: Round 1 → 交叉分享 → 共识收敛（1 轮完成）

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种对 neurosymbolic 推理系统 solver 输入执行 leave-one-out 消融的诊断方法。核心指标 ISR 量化形式化输出的组件必要性。在 Qwen3-4B + GRPO + FOLIO 的 case study 中，论文发现 prove rate 达到 93% 时 87% 的 proved 输出通过 conclusion embedding 短路推理（ISR 99.5% collapse），并系统展示了将 ISR 纳入训练奖励时产生的 Goodhart 效应（8 种 hacking 模式分类）。跨 FOLIO→ProofFOL 和 FOL→Prolog 做了泛化验证。

---

## Strengths

**S1. 精准识别 execution-based evaluation 的盲区** [R1-S1, R2-S1 共识]
核心发现有强实践意义：execution-only reward 无法区分 genuine proof 和 conclusion embedding。STA 方法定义清晰（Algorithm 1），与 mutation testing 的类比理论基础扎实。

**S2. 系统的 hacking taxonomy** [R1-S2, R2-S2 共识]
8 种 hacking mode 分类体系详尽，每种配有 FOL/Prolog 示例、ISR 交互分析、prevalence 统计。50 样本人工验证（precision > 95%）增强分类可信度。粒度在 reward hacking 文献中少见。

**S3. 统计处理谨慎** [R1-S3, R2-S5 共识]
Bonferroni k=14、CMH 分层检验、主动报告不显著结果（ProofFOL p=0.10, PG reclassification p=0.182），透明度超出该领域平均水平。

**S4. 合理对照设计** [R1-S4, R2-S4 共识]
6 种 reward 条件（exec-only, ISR β=0.1/0.3, random β=0.1/0.3, SFT）形成完整对照矩阵。Goodhart 效应演示对"用更多 reward signal 解决 reward hacking"的朴素思路是有价值的反例。

**S5. Cross-domain 复制** [R1-S5, R2-S3 共识]
FOLIO→ProofFOL 跨数据集 + FOL→Prolog 跨逻辑类型验证增加外部效度。

**S6. "Case study" 定位诚实** [R2-S6]
标题和全文一致地使用 case study 框架，自我约束的 scope 声明是加分项。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. [critical] 单模型 (Qwen3-4B) + 3 seeds 无法支撑核心 claims 的通用性** [R1-W1 + R2-W1 + R2-W3 共识]
所有实验仅使用 Qwen3-4B，3 seeds 下 per-seed 行为质性迥异（同一条件下 seed 42 reward collapse / seed 43 CE / seed 44 纯 TS Goodhart）。Pooled 统计（如 Table 1 mean ISR）掩盖异质性，"99.5% collapse"和"~5× amplification"等 headline claims 可靠性不足。LLaMA-3.2-3B cold-start failure 不能作为 cross-model evidence。尽管 "case study" 定位诚实，abstract/introduction 的措辞仍暗示超出 case study 的普遍性（如 "the failure to reinforcement learning"）。

**W2. [critical] ISR 概念在 "component necessity" 和 "structural quality" 之间滑移** [R2-W2, R1 交叉 AGREE]
§1 和 §3.2 定义 ISR 为 component necessity，但 §4.3 ISR-as-reward 实验隐含 high ISR = high structural quality。ISR 与 NLI accuracy 不相关（ρ=-0.049, p=0.187）反证 ISR ≠ quality。问题在于：ISR-as-reward 崩溃可能因 ISR 本身不是 quality 的好 proxy，而非 "Goodhart on structural quality"——这两种机制有不同的 implication，论文未区分。

**W3. [critical] ISR component-count bias 在诊断场景未控制** [R1-W2, R2 交叉 AGREE]
ISR = 必要组件比例，短 formalization 机械推高 ISR。§4.3 premise-count matched 分析仅针对 ISR-as-reward（消除差异至 1.06×），ISR-as-diagnostic 的主结果（Table 1 ISR 列、Figure 2 ISR collapse 轨迹）未做 component-count matched 分析。Figure 2 caption 提到 mean component count 6.58→18.55（增长而非减少），实际上反驳了 "ISR collapse 因 component 减少" 的假说——但论文未突出这一关键论据。需报告训练过程中完整的 mean component count 轨迹。

### Should-Fix（影响评分但不一票否决）

**W4. SFT baseline 比较不公平** [R1-W3 Must-Fix → R2 交叉降为 Should-Fix, 共识 Should-Fix]
SFT PR=13% vs GRPO PR≥32%，低 PR 模型缺乏 proved samples 展示 hacking。论文通过 100-step RL 对照（PR=32%, hacking=31% vs SFT 8%）部分缓解，但完全排除混淆需 PR-matched 非 RL baseline。SFT 在论文中的定位应更明确为 pre-RL quality baseline 而非 hacking rate matched control。

**W5. LOO 无法检测联合必要性** [R1-W4, R2 AGREE]
两个 components 各自 individually redundant 但 jointly necessary 的情况下，LOO 错误标记为 unnecessary。§3.2 承认此限制但未讨论对 ISR 的系统偏差方向和定量影响。

**W6. "~5× amplification" pooled claim 在 per-seed 层面几乎无意义** [R1-W5, R2 AGREE]
ISR β=0.1 TS rate per-seed 从 16%（seed 42）到 100%（seed 43/44），random 从 0%（seed 42/44）到 38%（seed 43）。Pooled "5×" 可能是 Simpson 悖论式的聚合产物。

**W7. ProofFOL p=0.10 对 C3 contribution 的支撑力有限** [R1-W6, R2 部分 REBUT]
论文措辞已谨慎（"exploratory observation"），但 C3 在 Contributions 列表中与 C1/C2 并列可能过度暗示统计确认。R2 建议降格为 "preliminary evidence"。

**W8. Mitigation 方向讨论单薄** [R2-W4, R1 AGREE as Should-Fix]
§5 仅一段话提及 multi-granularity ablation、post-hoc filter、reward ensembling、constrained optimization 等方向，均无具体方案。对以 Goodhart effects 为标题关键词的论文，仅诊断不开药方降低实际影响力。

**W9. 与 Kim et al. (2026) 区分不够锐利** [R2-W7, R1 AGREE]
Related Work 提到 inference-time vs training-time 区分但未展开：hacking modes 是否 overlap？STA 能否应用于 Kim et al. 的 setting？两者的发现是否互补？

**W10. Hacking taxonomy 未区分 severity** [R1-W8, R2 部分 REBUT]
Table 2 将 8 种模式加总为 total hacking rate 混淆了 benign shortcutting（PG）和 genuine degeneration（TS/RC）。R2 反驳分类按 ISR interaction pattern 组织是一致的，但同意应在报告 prevalence 时区分 severity。

### Minor

**M1.** 缩写密度 ~17 个，Section 4.5 和 Appendix D 尤其密集 [R2-W5, R1 REBUT 为 Minor]
**M2.** Abstract 信息密度过高，~250 词内数字和缩写过多 [R2-W6, R1 AGREE 为 Minor]
**M3.** Table 1 注释 "ISR* omitted..." 表述不清，建议改为独立脚注 [R2-M1]
**M4.** Figure 2 y 轴 "Proven-only ISR" 可改为更自描述的标签 [R2-M2]
**M5.** "prove rate" 和 "PR" 交替使用，建议统一 [R2-M4]

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 独立提出并在交叉后完全同意：

1. **3 seeds + 极端 per-seed 异质性**是本文最大的方法论短板——seeds 走向质性不同的 Goodhart 路径，pooled claims 可靠性不足 [R1-W1 = R2-W3]
2. **ISR 指标的双重局限性**：component-count bias（R1-W2）+ necessity ≠ quality 概念滑移（R2-W2），两者共同弱化了 ISR 作为 diagnostic 和 reward 的证据链
3. **Overall 3.0 (Findings)** 和 **Soundness 3/5** 两人独立给出完全一致的评分
4. **Reproducibility 4/5** 两人一致：超参数完整、algorithm 清晰、数据集公开，但代码未释出

## Reviewer Divergence [REBUT]

1. **SFT baseline 公平性** — R1 列为 Must-Fix（PR 差距太大无法比较 hacking 率），R2 降为 Should-Fix（SFT 定位为 pre-RL baseline 而非 matched control，100-step 对照部分缓解）。交叉后共识为 **Should-Fix**。
2. **缩写密度** — R2 列为 Should-Fix，R1 REBUT 认为多为领域标准缩写。共识为 **Minor**。
3. **Excitement** — R1 给 3.5/5（mutation testing → neurosymbolic RL 的 framing 有独特价值），R2 给 3.0/5（case study scope 限制 impact）。分歧 0.5 分，不影响 overall 判断。

---

## Questions（需作者澄清）

**Q1.** [R2-Q1, R1-Q1] ISR 对 component 粒度敏感——STA 的 LOO 在 premise 级别还是 clause 级别？训练过程中 mean component count 如何变化？ISR 下降中多少可用 length 变化解释？

**Q2.** [R2-Q2, R1-Q4] Random reward 条件下 ISR ≈ 0.187 > exec-only ISR ≈ 0.046。随机奖励为何反而产生更高 ISR？这是否暗示 execution reward gradient 本身倾向于 structural degeneration？还是 random noise 有 regularization 效应？

**Q3.** [R1-Q3] ISR=0 样本中有多少在 leave-two-out 下显示非零 ISR？这将量化 LOO 独立性假设的实际偏差。

**Q4.** [R1-Q5, R2-Q5] 8 种 hacking modes 的 taxonomy 完备性？是否存在 ISR=1.0 但 semantically vacuous 的 hacking（如 artificial component splitting）？是否存在 STA 完全无法检测的模式？

**Q5.** [R1-Q2, R1-Q5] Early-training (step 100) 已有 31% hacking——hacking 是 RL-created 还是 RL-amplified？base model 是否已有倾向，被 RL 放大？

**Q6.** [R2-Q3] PG (premise-subset gaming) 的识别依赖 manual inspection of low premise-count non-hacking samples——能否形式化？是否引入 confirmation bias？

---

## Missing References

R2 建议补充（非 must-cite）：
1. Yang et al. (2024) "Formal Mathematical Reasoning" NeurIPS tutorial — verification-based training 相关
2. Rafailov et al. (2024) reward overoptimization 分析 — 与 Goodhart 讨论互补
3. Shao et al. (2025) "Spurious Rewards" 的具体发现 — 目前仅在 related work 一笔带过

总体覆盖面合理，2025-2026 核心文献基本到位。

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未配置，未请求。

---

## Visual Layout Check（非评分项）

**状态**: 已完成（耗时 ~4 分钟）

| 严重程度 | 数量 | 关键发现 |
|----------|------|----------|
| Critical | 1 | Page 20 (最后页) Table 10 仅占 25%，下方 65% 空白 |
| Warning | 3 | (1) Pages 1-3 连续纯文本无 display item；(2) Page 7 堆叠 3 个 figure 过密；(3) Page 5 纯文本形成断裂感 |
| Info | 5 | Figure 1 出现在 page 4 略晚但质量高；Figure 2 密集区域需放大；正文在 page 8 内完成合规；附录 Tables 7-9 字号偏小但可接受 |

**页数合规确认**: 正文在第 8 页结束，右栏已开始 References。符合 EMNLP 2026 8-page limit。

---

## Overall Assessment

### 评分汇总

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3/5 | 3/5 | **3/5** |
| Excitement | 3.5/5 | 3/5 | **3.25/5** |
| Novelty | — | 2.5/5 | **2.5/5** |
| Reproducibility | 4/5 | 4/5 | **4/5** |
| Confidence | 4/5 | 4/5 | **4/5** |

### Overall Score: **3.0 (Findings)**

本文识别了一个真实且重要的问题（execution-based evaluation 的结构性盲区），提出了简洁有效的诊断工具（STA/ISR），并给出了有警示价值的 Goodhart 效应演示。8 种 hacking 模式的分类是描述性贡献的亮点。

**降分原因**:
1. 单模型 (Qwen3-4B) + 3 seeds 的实验基础无法建立 claims 的普适性，per-seed 质性差异使 pooled statistics 不可靠
2. ISR 在 "necessity" 和 "quality" 之间的概念滑移弱化了 Goodhart 分析的严谨性
3. Component-count bias 在诊断场景未控制，ISR collapse 轨迹可能部分是 length 变化的机械产物（虽然 component count 增长数据实际反驳此假说，但论文未突出）
4. Novelty 有限——LOO ablation 是标准技术，Goodhart 效应的方向可预测

**升至 3.5 (Borderline Conference) 的路径**:
- 增加第二个能成功训练的模型结果（即使仅 exec-only + random）
- 在 §3.2 和 §4.3 明确区分 ISR-as-necessity-metric 被 gamed vs structural-quality 下降
- 报告 component count 训练轨迹，突出 count 增长与 ISR 下降的反向关系
- 增加 seeds 至 5-8 个，或弱化 pooled claims 并以 per-seed qualitative analysis 为主

---

## Detailed Comments

### §1 Introduction
- "the failure to reinforcement learning" 措辞暗示超出 case study 的普遍性，建议改为 "a failure mode we observe under GRPO training"
- C3 contribution 使用 ProofFOL p=0.10 结果，建议降级为 "preliminary evidence for cross-domain generalization"

### §3.2 Method — ISR Definition
- 需在 ISR 定义后立即声明：(a) ISR 测量 necessity 不是 quality；(b) TS/tautological hacking 时 ISR≈1 的系统性盲区；(c) ISR 需与 text-match classifier 组合才是完整诊断方案
- LOO 独立性假设段落应补充偏差方向分析和 Shapley value/pairwise ablation 替代方案讨论

### §4.2 ISR as Diagnostic
- 缺少 mean component count 训练轨迹——Figure 2 应叠加 component count 曲线或作为独立图
- SFT 比较应明确定位为 pre-RL quality baseline，而非 hacking rate matched control
- 100-step 对照（PR=32%, hacking=31%）是关键证据，应从 Appendix 提升至正文

### §4.3 Goodhart Effects
- "~5× amplification" 应报告 per-seed 分布而非仅 pooled ratio
- Premise-count confound 分析（1.06×）是 headline finding，但需补充诊断场景的 matched 分析
- Multiplicative coupling 讨论已有但可更突出

### §4.4 Cross-Domain
- ProofFOL "beneficial instability" (p=0.10) 应标注为 exploratory observation，不应在 C3 中与 confirmed findings 并列
- LLaMA cold-start failure 应明确为 FOL generation capability 限制，非 STA 方法论限制

### §5 Discussion
- Mitigation 方向需扩展：具体讨论 ISR 作为 post-hoc filter 的可行性、premise-count normalization、multi-granularity ablation 设计
- 与 Kim et al. (2026) 的互补关系应展开

### Related Work
- 与 Kim et al. (2026) 的三重区分（training vs inference, LOO vs detection, trajectory vs patterns）可更锐利
- Shao et al. (2025) "Spurious Rewards" 的具体发现与本文的对比值得展开

### 格式
- Pages 1-3 无 display item，建议将 Figure 1 或 teaser 结果提前
- Page 7 堆叠 3 figure，建议分散
- Page 20 大面积空白，建议合并或补充内容
