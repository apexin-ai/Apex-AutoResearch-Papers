---
round: 21
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-25T21:34:29.945075+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 23 审稿报告（Fresh Review）— 交叉分享后修订版

**项目**: symb_invariant_consensus
**Venue**: EMNLP 2026 (ARR)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+Related Work）
**圆桌轮次**: 1 轮（独立初审 + 交叉分享，达成共识）
**交叉分享完成度**: R1 和 R2 均完成逐条 [AGREE]/[REBUT] 回应

---

## Summary

本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM chain-of-thought traces 中提取 FOL 约束并用 Z3 求解 weighted partial MAX-SAT 以选答案。核心发现为负面结果：自提取约束系统性地确认多数投票结果（symbolic confirmation bias, SCB），SICA 在退化条件下归约为多数投票。论文在 9 个模型（7B 到 frontier）、4 个 benchmark 上验证了这一现象，测试了 27 种 training-free 补救策略均失败，提出三项诊断指标（C₀, K_eff, BR），并展示跨架构 NLI verifier 可部分突破瓶颈。

---

## Strengths

**S1.** 实验方法论的高标准远超同类工作——McNemar + BH correction + TOST 等价检验 + bootstrap CI + 功效分析 + 多种子复制在 NLP 论文中罕见。[R1, R2 共识]

**S2.** 27 种 training-free 补救策略的系统测试是有价值的负面证据，independence-accuracy trade-off 防止社区重复探索已证明无效的方向。[R1, R2 共识]

**S3.** Observation 1（Argmax Preservation）将经验发现提升为可验证的形式化命题，推导在给定前提下正确。[R2 初审 Soundness 4/5]

**S4.** 诊断框架（C₀, K_eff, BR）从 K=12 pilot run 即可计算，具有实际应用价值。[R1, R2 共识]

**S5.** 22 页附录的消融和敏感性分析（prompt templates、case studies、per-subtype 分析、CV 直方图等）大幅增强可复现性。[R1, R2 共识]

**S6.** Limitations 坦诚，Discussion 不过度声称——exploratory vs. confirmatory 的区分、统计功效不足的报告体现良好学术诚信。[R1, R2 共识]

**S7.** 跨架构 NLI escape 虽初步，但指向正确的研究方向。[R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [R1-N1 + R2 AGREE] Observation 1 在 SICA 的 source-attribution scoring 设计下近乎同义反复**
- σ(c,a) 完全基于约束的来源 trace（provenance）而非逻辑内容。在 variable isolation 导致跨 trace 约束无法交叉引用的情况下（§5.2: 56.4% 跨答案约束共享零个 Z3 变量），退化是 scoring 设计的直接后果而非关于 self-extraction 的 surprising discovery。
- R2 补充：syntactic deduplication（46%）未按语义等价去重。两条来自不同 trace 的约束可能语义相同但变量名不同，Z3 将它们视为独立命题。
- R2 修正：论文经验发现退化条件在实践中普遍成立（9 模型、BR 1.66-4.97x）仍有增量贡献，但 Observation 1 的 claim 范围需收窄。
- **修改要求**: (1) 将 Observation 1 明确限定为 SICA 特定设计（provenance-based scoring + variable isolation）的分析结论；(2) 讨论 content-based scoring 替代方案（如语义嵌入跨 trace 匹配、变量规范化）并解释为何不可行；(3) 重新定位经验发现（退化在实践中普遍发生）为核心贡献。

**MF2. [R2-N1 + R1 AGREE] 核心发现新颖性有限——但经验贡献和诊断框架仍有价值**
- SCB 核心机制可从 Huang et al. (2024) / Kamoi et al. (2024) 合理预期。
- R1 同意 framing 需调整，但指出三方面增量：(a) M→T→(A,C) 因果结构和 variable isolation 的具体机制比一般性"self-correction fails"更有操作意义；(b) 9 模型 × 4 基准 × 27 策略的经验广度在该子领域无先例；(c) 诊断工具 C₀/K_eff/BR 是直接可用的实践指导。
- R1 引用 ARR H1 规则："results appearing obvious retrospectively doesn't mean the community already knows them empirically"。LogicLM/LINC/SatLM 均假设形式化约束提供独立信号，本文的系统性反证有发表价值。
- **修改要求**: (1) 将重心从理论贡献（Observation 1）转向经验发现和诊断框架；(2) 论证为什么 SatLM/LogicLM 的成功给了社区错误的乐观预期，从而凸显本文的反直觉价值。

**MF3. [R2-N2 + R1 部分 AGREE] Benchmark 范围有限，claim 需收窄**
- 主要评估仅 FOLIO (n=204) + ProofWriter (n=600)。R1 提出缓解因素：(a) best-case argument（最适合约束提取的任务上都失败）；(b) StrategyQA/LogiQA 非模板化逻辑推理；(c) variable isolation 不依赖特定 benchmark。
- 但 R1 也同意代码生成（约束=可执行单元测试）和数学推理（完整 GSM8K 评估）确实未覆盖。
- R1 建议降级为 should-fix，考虑到 best-case argument 的有效性。
- **修改要求**: (1) Abstract/Intro 限定 claim 为"logical reasoning benchmarks under zero-shot extraction"；(2) 在 Limitations 中更显著地讨论代码生成和数学推理场景。

**MF4. [R1-N2 + R2 AGREE] Cross-architecture escape 的 capability-gap pattern (n=6) 作为三大贡献之一证据不足**
- ρ=1.0, p=0.003 仅基于 n=6 对，对单点扰动不稳健。R2 补充：Table 3 显示 combo gain 随 generator capability 单调递减（Mistral-7B +6.67 → Qwen3-14B +0.50 pp），对 frontier 模型几乎无意义。
- **修改要求**: (1) 降级为 observation 而非 contribution；(2) 主文引用附录 W 的 15-condition 扩展；(3) 对基于 n=6 的 implications 加更多 hedging。

### Should-Fix（影响评分）

**SF1. [R1-W1 + R2 AGREE] 结构独立性与外部监督信号的归因混淆**
- NLI verifiers 在 MultiNLI 上 fine-tuned。跨模型 LLM 投票（也有结构独立性但无 NLI 信号）不奏效（Appendix O）。关键因素是 structural independence + task-relevant supervised signal 的组合。
- Discussion 中"without task-specific training"表述不准确（MultiNLI 与逻辑推理高度相关）。
- **建议**: 明确 escape 需要两个条件，设计控制实验分离两个因素（如用未 fine-tuned 的 DeBERTa base 做 verifier）。

**SF2. [R1-W2 + R2 AGREE] 统计功效不足以支撑等价性声明**
- MDE 4.6-4.8 pp，典型 |Δ| ≤ 2 pp。仅 4/11 通过 TOST。R2 补充 bootstrap CI 提供部分缓解（最有利条件上界 < +1.62 pp）。
- **建议**: 将"no condition shows significant positive effect"改为更审慎表述，如"we find no evidence of positive effect, though power to detect effects below ~4.6pp is limited"。

**SF3. [R1-W3 + R2 AGREE] "Symbolic Confirmation Bias" 命名可能有误导性**
- 排列检验确认 BR 反映 trace-count geometry。约束非 actively biased 而是 not independently informative。R2 理解修辞动机但建议在正文中明确区分现象（constraints confirm majority）和机制（non-independence/redundancy）。
- **建议**: 首次引入术语时明确区分。

**SF4. [R1-W4 + R2 AGREE] Variable normalization 未被测试——27 种策略中最显眼的缺失**
- R2 认同这是直接针对已确认根本原因的修复方案。最简单版本：在提取 prompt 中强制固定变量名方案。
- **建议**: 至少测试 prompt-level 变量规范化，或解释为何不可行。

**SF5. [R2-W2，R1 REBUT 后修正] Test-time compute scaling 范式讨论深度不足（非缺失）**
- R1 核实后指出 DeepSeek-R1 (Guo et al. 2025)、QwQ (Qwen 2024)、o3（Table 2 实测 SCB）、PRM 文献（Lightman/Wang/Cobbe）均已被引用或测试。R2 的"缺失"定性不准确。
- 实际问题是**讨论深度**不足：为什么 o1/R1 的 learned verification 成功而 self-extraction 失败，可以更充分地在 Discussion 中展开。
- **建议**: 在 Discussion 中增加 paradigm-level 对比。

**SF6. [R2-W3 + R1 部分 AGREE] 约束提取质量过浅**
- R1 认为更丰富约束语言不太可能改变核心结论（variable isolation 不依赖约束复杂度），且逻辑 prompt 实际允许 Implies/And/Or 复合结构。但与 SF4 一致，如果约束被设计为跨 trace 可比较的格式（统一本体），SCB 可能改变。
- **建议**: 讨论约束浅层性是设计选择还是模型能力限制。

**SF7. [R2-W4，R1 REBUT 后修正] 近期相关工作覆盖——大部分已到位**
- R1 核实：DeepSeek-R1/QwQ/o3/PRM 均已引用或测试；DyLoS (Xu et al. 2026) 可能就是 R2 所指的 EACL 2026 论文。
- 仅"Neurosymbolic Language Reasoning as SMT (2026)"待确认是否真实存在。
- **建议**: 如 SMT 论文确实存在，补充引用。

**SF8. [R1-W5 + R2 AGREE] Confirmatory vs exploratory 划分标准不透明**
- m=6 confirmatory 条件的选择标准（n ≥ 200 阈值来源、是否预注册）未在正文明确说明。
- **建议**: 在 §4.1 或 §4.2 明确列出 confirmatory 条件及划分标准。

**SF9. [R2-W5 + R1 AGREE] Observation 1 在"近退化"条件下的适用性 gap**
- R1 提供了经验证据（三区域分类、entropy decomposition、α 消融）支持连续过渡而非相变。但缺少对过渡区间行为的形式化刻画——intermediate regime (SC 50-60%) 是否存在某个 |C\|/|C| 阈值使 SICA 开始提供纠错信号？
- **建议**: 在 Discussion 或 Appendix 中讨论过渡区间行为。

---

## Reviewer Consensus [交叉分享后]

两位 Reviewer 在以下关键问题上达成完全共识 [AGREE]：

1. **Observation 1 的设计依赖性**: 退化是 source-attribution scoring + variable isolation 的直接后果，Observation 1 的 claim 范围过宽。[R1-N1 + R2 AGREE]
2. **核心 insight 可预测性较高**: 但经验贡献（9 模型 × 27 策略）和诊断框架仍有发表价值。[R2-N1 + R1 AGREE with nuance]
3. **n=6 capability-gap pattern 作为贡献不足**: 应降级为 observation。[R1-N2 + R2 AGREE]
4. **结构独立性 vs 监督信号混淆**: Escape 需要两个条件。[R1-W1 + R2 AGREE]
5. **统计功效不足**: bootstrap CI 部分缓解，但表述需更审慎。[R1-W2 + R2 AGREE]
6. **SCB 命名有误导性**: 实际机制是 non-independence，非 cognitive bias。[R1-W3 + R2 AGREE]
7. **Variable normalization 缺失**: 最直接的修复方案未测试。[R1-W4 + R2 AGREE]
8. **Confirmatory 划分不透明**: 需明确标准。[R1-W5 + R2 AGREE]
9. **近退化适用性 gap**: 缺少过渡区间形式化。[R2-W5 + R1 AGREE]

## Reviewer Divergence [已解决]

R1 对 R2 的两个 REBUT 均基于事实核实，双方已无未解决矛盾：
1. **R2-W2（缺 test-time scaling 讨论）→ R1 REBUT**: 相关工作已引用，问题是讨论深度而非缺失。
2. **R2-W4（缺近期引用）→ R1 REBUT**: 4 类中至少 3 类已覆盖。

---

## Questions

**Q1** [R2]: 跨模型同架构的约束提取（非自提取）是否改变 SCB？

**Q2** [R2]: SCB 对提取温度有多敏感？Appendix 仅在 Mistral-7B 上测试。

**Q3** [R2]: 诊断框架阈值是否数据集依赖？

**Q4** [R2]: 27 种策略是独立策略还是部分组合？

**Q5** [R1]: Eq. 2 的 argmax formulation 与 Algorithm 1 实现是否存在全局最优性 gap？

**Q6** [R1]: K_eff 公式引用 Ladha (1992) 的准确性？

---

## Missing References

1. **"Neurosymbolic Language Reasoning as SMT" (2026)** — 待确认是否真实存在。如存在，与 Z3 MAX-SAT 方案高度相关。[R2 提出，R1 未能确认]

注：R2 初审列出的其他 3 类"缺失"引用（DeepSeek-R1/o1/o3、PRM、EACL 2026 DyLoS）经 R1 核实后确认**已被论文引用或测试**。

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: 已完成（0 critical, 2 warnings, 23 info）

主要发现：
- 主文 8 页，9 个 display items / 8 页 ≈ 1.1/页，密度优秀
- Figure 1 在 page 2 顶部，Title-Abstract-Figure 1 一致性好
- 所有表格 booktabs 风格，float 无漂移，颜色方案一致

Warnings：
1. Page 30（Appendix 末页 AI Assistants 声明）仅占 ~25%，建议合并到前一页
2. Figure 7 (p.17, appendix) 策略名称字号较小，建议 ≥ 7pt

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference**

**R1**: 3.5（Soundness 3.5, Excitement 3）
**R2**: 3.5（Soundness 3.5↓from 4, Excitement 3）
**Director**: 3.5

**置信度: 4/5**

**评分依据**:

这是一篇实验方法论严谨、统计分析全面的负面结果论文。核心贡献对 neuro-symbolic reasoning 社区有直接指导意义。

四个 Must-Fix 问题制约当前版本：

1. **MF1: Observation 1 的论证循环性** — 核心理论贡献在 source-attribution scoring + variable isolation 设计下近乎同义反复。需收窄 claim 范围并讨论替代方案。

2. **MF2: 核心发现的新颖性定位** — 需将重心从理论贡献转向经验发现和诊断框架，并论证为何 SatLM/LogicLM 的成功给了社区错误预期。

3. **MF3: Benchmark 范围** — claim 暗示 generality 但仅覆盖英文逻辑推理。best-case argument 有效但需在 claim 中反映。

4. **MF4: n=6 capability-gap pattern** — 作为 Contribution 3 证据不足，应降级。

**可行修改路径**:
- MF1: 增加 content-based scoring / variable normalization 的讨论和实验（~1-2 周）
- MF2: 重新定位 framing（~2-3 天）
- MF3: 收窄 claim + 增强 Limitations 讨论（~1 天）
- MF4: 降级 + 引用附录扩展结果（~1 天）

如果 MF1-MF4 充分解决（特别是 MF1 的替代方案讨论），论文有潜力达到 Conference (4.0)。当前版本更适合 Findings (3.0-3.5)。

---

## Detailed Comments

### §1 Introduction
- "symbolic mirage" 作为隐喻可保留但建议在正文中正式定义
- Contribution 3 应反映 n=6 的初步性质（"preliminary observation" 而非 "contribution"）

### §3 Method
- Eq. 2 与 Algorithm 1 的 gap 应在正文注明
- K_eff 公式对 Ladha (1992) 的引用准确性需确认
- 应讨论 content-based scoring 替代方案和 variable normalization

### §4 Experiments
- Table 1 caption 中灰色带可能被误读为显著性
- Figure 2 的 circled points 应标注是否经 BH 校正
- "nine models" 的 BR 和完整评估的 distinction 应更清晰

### §5 Analysis
- §5.1: SCB 术语首次引入时区分实际机制（trace-count geometry）与认知确认偏见
- §5.2: 增加 variable normalization 讨论
- §5.4: 明确 escape 需要 structural independence + supervised signal 两个条件
- §5.4: "without task-specific training" 需修正

### §6 Discussion
- 基于 n=6 pattern 推导的 implications 需更多 hedging
- 增加 learned verification (o1/R1) vs self-extraction 的 paradigm-level 对比

### Limitations
- 增加 benchmark 范围限制对 claim generality 的影响
- 增加 variable normalization 未被测试的讨论