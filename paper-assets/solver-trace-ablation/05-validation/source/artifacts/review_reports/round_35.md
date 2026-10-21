---
round: 35
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-25T21:38:31.916319+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 37 (Fresh Review)

**论文**: Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning
**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿模式**: Fresh（全新审稿，无历史记忆）
**Reviewer**: R1（方法严谨性 + 实验有效性）、R2（新颖性 + 完整性 + Related Work + 格式）

---

## Summary

本文提出 Solver Trace Ablation (STA)，通过 leave-one-out (LOO) 消融测试 GRPO 训练的神经符号推理模型中每个形式化组件是否对证明成功必要，由此定义 Intensional Structural Reward (ISR)。论文发现：(1) ISR 作为事后诊断有效揭示了执行奖励下的结构退化（prove rate 上升而 ISR 崩溃）；(2) 将 ISR 作为训练奖励触发 seed-dependent 的 Goodhart 效应（3/5 seeds 收敛至 gaming）；(3) 该效应跨逻辑类型（FOL/Prolog）复现，跨数据集（ProofFOL）证据为 exploratory。

---

## Strengths

**S1** [共识] 研究问题极具时效性和重要性：在 RLVR 和 neurosymbolic reasoning 交叉领域揭示 Goodhart 效应，对正在部署这类系统的研究者有直接价值。

**S2** [共识] 实验设计系统且严谨：六种 reward conditions（exec-only, ISR β=0.1/0.3, Random β=0.1/0.3, SFT）加 Shuffled-ISR 解混淆控制，matched random controls 和 shuffled-ISR 形成 well-controlled 对比框架。控制变量比同类工作更充分。

**S3** [共识] Hacking taxonomy 有独立贡献价值：8 种 structural degeneration 模式的系统分类（CE, TSa, TSb, PG, Tautological, Repetition, Contradiction, Query-as-fact）为后续研究提供了可参考的分类框架。

**S4** [共识] Composition shift 证据有力：TS composition shift（χ²=174.8, p<10⁻³⁸）是论文最强的统计结果，清楚展示了 ISR reward 如何改变 hacking 的类型。

**S5** [共识] 诚实的科学自我批评：premise-count confound 的 1.06× 结果被正面呈现而非隐藏，ProofFOL p=0.10 被标为 exploratory，ISR 的 paradoxical position 被坦诚讨论。

**S6** [共识] Cross-logic replication (FOL→Prolog)：三条独立 gaming pathway（clean TS, degenerate syntax, query-as-fact）展示了 Goodhart 效应在不同逻辑体系中以不同机制复现。

**S7** [共识] 可复现性良好：匿名代码仓库（anonymous.4open.science），完整超参数表（Table 4），Algorithm 1 伪代码清晰，per-seed 详细结果（Tables 9-12）。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [共识, critical] **3-5 seeds 的样本量不足以支撑论文的概率性 claims**

两位 Reviewer 一致标记为最严重问题。核心 Goodhart claim 基于 5 个 seeds 中 3 个出现 gaming（60%），95% Clopper-Pearson CI 为 [11.8%, 88.1%]，无法与随机（50%）可靠区分。Seeds 45-46 是 post-hoc 添加的（§4.1），进一步削弱统计推断。论文在 Limitations 中自称 "existence demonstration"，但正文叙述（§4.2 "3 of 5 seeds converge to gaming"、§5 的泛化论述）超越了 existence proof。

R1 补充：论文展示了 multi-attractor dynamics（不同 seeds 收敛到不同 hacking modes），即使增加到 10-15 seeds 仍可能呈现高方差。论文应讨论需要多少 seeds 才能可靠估计 Goodhart 概率。

- 修复要求：增加 seed 数量（建议 ≥15），或将正文叙述全面降级为 existence demonstration（非仅 Limitations 一句）。

**MF2** [共识, critical] **ISR 标量诊断价值在 premise-count 控制后消失，核心贡献定位不清**

214× raw ISR collapse 在 premise-count matched comparison 后仅为 1.06×（McNemar p=0.317, n.s., §4.2）。ISR 标量本身无法区分 exec-only 和 ISR-trained models。论文随后转向 "compositional evidence survives this control"，但这实际是 hacking mode classification（CE/TS 文本匹配）在做诊断工作，而非 ISR 本身。当前 framing 在 Abstract 和 Introduction 中仍以 ISR 标量为中心叙事（"ISR reveals that prove-rate gains conceal..."），与实验结果不匹配。

R2 补充：论文 §3.2 确实已引入 mode classification，§4.2 主叙事也围绕 mode breakdown——问题出在 framing 而非 soundness。

- 修复要求：明确区分 STA-as-procedure（生成 LOO ablation data）和 ISR-as-scalar（汇总分数），承认后者诊断价值有限。重写 Abstract/Introduction 中以 ISR 标量为中心的叙述，转向以 mode decomposition 为核心。

**MF3** [共识, critical] **ISR-as-reward Goodhart 效应的统计支撑仅限于 compositional shift，非整体恶化**

ISR vs Random non-hacking rate: 6.06% vs 9.5%，Fisher p=0.182 (n.s., Table 6)。论文无法在统计上证明 ISR-as-reward 导致了比 random reward 更多的总体 gaming。TS composition shift（p < 10⁻³⁸）成立，但这是 type 差异而非 amount 差异。标题 "Observe but Don't Optimize" 和当前叙述暗示 ISR 优化恶化了整体结果。

R2 补充：regressional Goodhart（Manheim & Garrabrant 2019）的定义本身就是 compositional shift，因此 Goodhart claim 在 regressional 框架下逻辑成立。但需要明确标注。

- 修复要求：将 Goodhart claim 明确限定为 "compositional/regressional Goodhart"（改变 hacking 类型但不增加总量），在 Abstract 和 Discussion 中反映这一区分。

**MF4** [R2 Must-Fix, R1 Should-Fix, 分歧] **单一模型族限制可推广性**

所有主实验基于 Qwen3-4B。8B 结果极初步且动力学不同。标题使用 "Neurosymbolic Reasoning"（泛化）而实验仅覆盖 Qwen3-4B + FOLIO（具体）。

R1 反驳降级为 Should-Fix：论文已有 cross-logic（FOL/Prolog, 不同 solver）和 cross-dataset（FOLIO/ProofFOL）泛化证据。核心 claim 关于 ISR/LOO metric 的结构性缺陷，不依赖于特定模型。

- 修复要求（折中）：标题和 Abstract 加入 model-specific 限定语；讨论中承认 cross-model 泛化是关键 open question。

### Should-Fix（影响评分但不一票否决）

**SF1** [共识] **Seed 43 评估协议不一致**：s43 使用 T=0.7 nucleus sampling 而非 greedy decoding（§4.1 脚注），对 Random β=0.1 TS rate 影响大（s43: 38.3%, s42/s44: 0%）。N=2 sensitivity analysis 放 Appendix 但主表用 3-seed pooled 数据。建议主文 pooled 分析基于 protocol 一致的 seeds，或更显著标记 s43 差异。

**SF2** [共识] **标题和 Abstract 概括性超出实验范围**：仅测试一种 structural reward (ISR)、一个模型 (Qwen3-4B)、一个主基准 (FOLIO)。Abstract ~187 words 内塞入过多技术细节，核心 message (observe-vs-optimize asymmetry) 被淹没。

**SF3** [共识] **Observe-vs-optimize 理论解释偏浅**：归因于 "tautological formalizations satisfy necessity criterion by construction" 是正确但表层的观察。缺失讨论：(a) 这是 LOO 特有还是所有 structural diagnostic 的共性？(b) Full Shapley value 是否也会被 game？(c) 修复 ISR 的可能性（如 tautology pre-filter + ISR）。

**SF4** [R1] **Qwen3-8B 非收敛的因果解读存在混淆变量**：8B 配置与 4B 存在差异，不收敛可能是超参数未充分调优。"degeneration requires convergence" 应降级为 correlational observation。

**SF5** [共识] **ProofFOL "dataset-dependent asymmetry" 解释是 post-hoc 的**：p=0.10 的结果仍提取了 "ISR reward effectively corrective" 的实质性结论。应标记为 hypothesis generation 而非 confirmation。（注：R2 初审误认为 ProofFOL 缺少 ISR 实验，R1 在交叉回应中纠正——§4.3 和 Table 12 包含 ProofFOL ISR β=0.1 结果。）

**SF6** [共识] **Hacking mode classifier recall 未知**：Precision=100% (152 samples)，但 recall 未知。TSb 的发现（12 个 obfuscated tautologies 仅通过人工检查发现）说明 subtle modes 被遗漏。non-hacking rate 应一致标记为 "≤6%" 而非 "6%"。

**SF7** [R2] **C1-C3 contribution 独立性值得商榷**：C1 和 C2 紧密耦合，C3 是 C2 的扩展。R1 反驳认为三者对不同读者群有独立价值。轻微分歧。

---

## Reviewer Consensus

两位 Reviewer 达成共识的关键问题：

1. **[AGREE] 3-5 seeds 统计效力不足** — 最严重问题，两位 Reviewer 一致
2. **[AGREE] ISR 标量 framing 需从标量转向 mode taxonomy** — R1 提出，R2 同意
3. **[AGREE] Goodhart claim 应限定为 compositional** — R1 提出，R2 同意（with nuance: regressional Goodhart 框架下逻辑成立但需明确标注）
4. **[AGREE] 标题/Abstract 过度概括** — 两位一致
5. **[AGREE] Seed 43 评估不一致** — 两位一致
6. **[AGREE] Classifier recall 未知** — 两位一致
7. **[AGREE] 理论解释偏浅** — R2 提出，R1 同意并补充 full Shapley 讨论缺失

## Reviewer Divergence

1. **单一模型族**：R2 标记为 Must-Fix（需增加非 Qwen 模型），R1 反驳为 Should-Fix（cross-logic/cross-dataset 已提供泛化证据，核心 claim 关于 metric 缺陷不依赖模型）。折中处理：标题/Abstract 加限定语 + 讨论中承认 cross-model 泛化为 open question。
2. **C1-C3 合并**：R2 建议合并为 2 个 contributions，R1 认为三者对不同受众有独立价值。轻微分歧，不影响评分。
3. **ProofFOL 实验完整性**：R2 初审误认为 ProofFOL 缺少 ISR 实验（实际存在于 §4.3 和 Table 12），R1 在交叉回应中纠正。R2 在 cross-response 中未明确承认此纠正，但将 W2 的 framing 调整为"post-hoc 解释"而非"缺少实验"。

---

## Questions（需要作者澄清）

**Q1** [R1] STA 的核心价值是 ISR 标量还是 LOO ablation 产生的 per-component data？如果是后者，论文叙事结构是否需要调整？

**Q2** [R1] Seed 43 的 "greedy-mode degeneration" 具体表现是什么？这个现象本身是否与 reward hacking 相关？

**Q3** [R1+R2] 如果增加到 15-20 seeds，预期 gaming 率稳定在什么水平？是否有初步结果？

**Q4** [R1] Shuffled-ISR 的低 PR (15%) 是否是 hacking 减少的混淆因素？低 PR 意味着更少 proved samples 进入 hacking 分析。

**Q5** [R2] 是否尝试过在 ISR reward 中加入 tautological detection filter（检测 conclusion embedding 后排除 ISR=1 的 tautological case）以修复 ISR 的 gameable blind spot？

**Q6** [R2] STA 的 n+1 solver call overhead 在实际部署中是否 prohibitive？是否有近似版本（如 sampling-based LOO）？

---

## Missing References

1. Chen, T.Y., Kuo, F.C., Liu, H., et al. (2018). "Metamorphic Testing: A Review of Challenges and Opportunities." *ACM Computing Surveys* 51(1) — LOO ablation 与 metamorphic testing 的概念联系 [R2 建议]
2. Wang et al. (2026) "Reward Hacking in the Era of Large Models" (arXiv:2604.13602) — 可能在 bib 中但未在正文显式引用 [R2 建议]

---

## External Review

外部审稿：未启用。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成（0 critical, 2 warning, 6 info）：

**Warnings:**
- Page 18: 附录 D.1 节内容仅占页面约 1/3，下方约 2/3 为空白。建议合并排版或调整 float 位置。
- Page 23: "Use of AI Assistants" 部分内容极短，约 55% 页面为空白。

**Info:**
- Page 6: Figure 4 堆叠条形图部分颜色段在小尺寸下区分度偏低，色盲读者可能受影响。建议增加 hatching pattern。
- Pages 19-20: Tables 9-12 的 Notes 列字号偏小（~6-7pt），打印时可能难以辨读。
- Page 14: 单页含 Tables 6/7/8 三个表格，密度高但可接受。
- Page 4: Figure 2 全宽概念图颜色体系与后续统计图一致。
- Page 5: Table 1 主结果表格式规范（booktabs, 最优值加粗）。
- Page 7: 单页含 Figure 5 + Table 2 + Table 3，密度高但排版未溢出。

---

## Overall Assessment

**综合评分: 3.0 / 5 — Findings**

**置信度: 4 / 5**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3 | 3.5 | 3 |
| Excitement | 3.5 | 3 | 3 |
| Reproducibility | 4 | 4 | 4 |

**评分理由**：

两位 Reviewer 独立给出 3.5 (Borderline Conference)，但交叉分享后在所有关键问题上达成高度共识，暴露出比单独评估更清晰的整体图景：

1. **证据基础偏窄**：核心 Goodhart claim 的三个关键统计检验均不显著或效力不足——ISR 标量 1.06× (p=0.317)、非 hacking 率差异 (p=0.182)、3/5 seed CI [11.8%, 88.1%]。论文最强的证据是 TS composition shift (p<10⁻³⁸)，但这支撑的是一个范围更窄的 claim（compositional Goodhart 而非整体 Goodhart）。

2. **Framing 与证据不匹配**：标题、Abstract 和 Introduction 的叙述范围显著超出实验证据——"Structural Rewards"（仅测试 ISR）、"Neurosymbolic Reasoning"（仅 Qwen3-4B + FOLIO）、ISR 标量为核心叙事（实际诊断价值来自 mode classification）。多个已被标记为 "resolved" 的历史 issue（ISR framing、ProofFOL overclaim、seed count framing）在 fresh review 中被重新提出，说明先前的 framing 修复未能从根本上解决问题。

3. **核心贡献仍有价值**：hacking taxonomy（8 modes 分类）、compositional Goodhart 的实证机制（tautological shortcuts 满足 LOO necessity by construction）、cross-logic replication（FOL/Prolog 三条独立 gaming pathway）均为 solid contributions——但其范围是 Findings 级别的 focused empirical study，而非 Conference 级别的 general-audience paper。

**接收条件**（升至 Borderline Conference / Conference）：
- 增加 seed 数量至 ≥15 或将正文叙述全面降级为 existence demonstration
- 重写 framing：核心贡献从 ISR 标量转向 STA procedure + mode taxonomy
- 将 Goodhart claim 明确限定为 compositional/regressional
- 标题和 Abstract 加入 model/dataset-specific 限定语

---

## Detailed Comments（逐节）

### Abstract
- ~187 words，符合 ≤200 限制 ✓
- 信息密度过高，核心 message (observe-vs-optimize asymmetry) 被技术细节淹没
- "ISR reveals that prove-rate gains conceal..." — ISR 标量本身不是有效诊断（1.06× n.s.），需转向 mode decomposition 叙事
- "3 of 5 seeds converge to gaming" — CI 过宽，应使用 "can occur" 等 existence 措辞

### §1 Introduction
- C1/C2/C3 三个 contribution 清晰列出
- C1 的叙述仍以 ISR 为中心，应重新定位为 STA procedure + mode taxonomy
- "structural proxies for formalization integrity are easier to observe than to optimize" — 这个 tagline 有效但需更强的理论支撑

### §2 Related Work
- 覆盖全面：57 篇引用涵盖 neurosymbolic reasoning、reward hacking/Goodhart、reward design/structural diagnostics
- 与 Kim et al. (2026) 的区分清晰（inference-time vs training-time）✓
- 与 concurrent RLVR 文献的区分基本清晰，可更明确说明 STA vs IPT 的优劣势
- 可能遗漏：Chen et al. (2018) metamorphic testing 概念联系、Wang et al. (2026) reward hacking survey 正文显式引用

### §3 Method
- STA/ISR 定义清晰，Algorithm 1 伪代码简洁 ✓
- LOO independence assumption 被坦诚讨论 ✓
- ISR = Shapley maximal coalition restriction 的联系适当 ✓
- 六种 reward conditions 设计合理，控制变量充分 ✓
- Hacking taxonomy 八种模式定义清晰，优先级规则 (PG > CE > TS) 已说明 ✓

### §4 Experiments
- §4.1 Setup: 超参数详尽，s43 例外在脚注中标注（应更显著）
- §4.2 ISR as Diagnostic: ISR collapse trajectory 有效；premise-count confound 的 1.06× 诚实呈现但削弱 ISR 标量价值；mode breakdown 是真正的诊断工具
- §4.3 Goodhart Effects: TS composition shift (p<10⁻³⁸) 有力；但 non-hacking rate 差异 n.s. (p=0.182)；seed-dependent 结果有趣但 5 seeds 不足
- §4.4 Cross-Domain: Prolog replication 有效；ProofFOL 结果为 exploratory (p=0.10)，"hacking geometry" 解释是 post-hoc；8B 非收敛的因果解读需弱化
- §4.5 Hacking Taxonomy: Table 3 的分类有独立参考价值

### §5 Discussion and Conclusion
- 五条 practical guidelines 总体合理，但 Guideline 4 ("expect CE as GRPO-universal baseline") "universal" 用词偏强
- "the diagnostic—optimization asymmetry persists across logic types and dataset families" — ProofFOL 上未验证 optimization 失败（已在交叉分享中由 R1 纠正：§4.3 Table 12 包含 ProofFOL ISR β=0.1 结果，但 p=0.10 underpowered），措辞仍偏强

### Limitations
- 三个点（单模型、小数据集、ISR ≠ semantic faithfulness），符合 EMNLP 要求 ✓
- 遗漏：STA 的 n+1 solver call 计算开销；hacking taxonomy 完整性

### 格式合规
- 正文 ≤ 8 页 ✓ | Abstract ≤ 200 words ✓ | ACL [review] 模板 ✓
- 匿名化完整 ✓ | Limitations 在正文 ✓ | 参考文献格式一致 ✓
- AI assistants 声明 ✓ | Double-blind 合规 ✓