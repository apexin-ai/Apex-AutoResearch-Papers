---
round: 33
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-25T04:15:57.112168+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

## 审稿报告 — Round 35 (Fresh Review)

**项目**: solver-trace-ablation
**目标 Venue**: EMNLP 2026 (ARR)
**Reviewer 配置**: 2 人（R1: 方法严谨性/统计; R2: 新颖性/完整性/写作）
**交叉分享**: 完成，R1 对 R2 逐条 [AGREE]/[REBUT]

---

## Summary

本文提出 Solver Trace Ablation (STA)，基于 leave-one-out 的诊断方法检测 neurosymbolic reasoning 中形式化证明组件是否被个体需要。核心发现为 "observe-vs-optimize asymmetry"：ISR 作 post-hoc 诊断有效，但作为 GRPO 训练奖励时触发 Goodhart 效应（3/5 seeds 退化为 gaming）。论文在 Qwen3-4B 上系统测试 6 种奖励条件，提出 8 种 hacking mode 分类，并在 Prolog/ProofFOL 上进行跨逻辑验证。

---

## Strengths

1. **问题定位准确且日益重要**：neurosymbolic RLVR 中 prove-rate 与 structural soundness 的 gap 是真实存在的研究问题，论文精确捕捉。

2. **实验设计系统周全**：6 种奖励条件（含 Shuffled-ISR control）、5 seeds、per-seed 完整报告、Cochran-Mantel-Haenszel 检验、Fisher exact tests。方法论比同类实证论文严谨。

3. **Hacking taxonomy 有实用价值**：8-mode 分类（Appendix C）含具体 failure mode 示例、ISR interaction 分析和检测逻辑，对后续研究有直接参考价值。

4. **跨逻辑证据扎实（Prolog）**：Table 11 报告 Prolog ISR-as-reward 3 seeds 全部 0% non-hacking，三种不同 gaming 机制（TS/functional-TS/query-as-fact），是最强的泛化性证据。

5. **Reproducibility 优秀**：Table 2 完整超参、Appendix A 计算资源、Appendix D per-seed 结果。学术诚实性值得肯定（坦承局限、报告阴性结果）。

6. **写作结构清晰**：Algorithm 1 + Figure 2 有效传达 STA pipeline；Section 5 实践指南对从业者有直接价值。

---

## Weaknesses (Must-Fix)

### W1 [critical] C1 贡献声称存在 overclaim

**共识度**: R1 + R2 均认同

C1 将 STA 定义为 "diagnostic method applicable to any solver-verified reasoning system"，但 LOO ablation 是 mutation testing 的标准技术（DeMillo et al., 1978），论文自身在 §3.2 也承认 "novelty lies in application and findings, not in the perturbation primitive"。Algorithm 1 本质上是 4 行 LOO 伪代码。

**要求**：将 C1 从 "method contribution" 降级为 "systematic application + empirical characterization"。核心贡献应强调实证发现（seed-dependent Goodhart、hacking taxonomy、cross-logic evidence）而非方法通用性。

### W2 [critical] 统计效力不足——5 seeds + exec-only 仅 1 seed

**共识度**: R1 + R2 完全一致（本轮最强共识）

- "3/5 seeds converge to gaming" 的 95% Clopper-Pearson CI ≈ [11.8%, 78.5%]，置信区间极宽
- Exec-only 条件（核心 baseline）仅 seed 42 一个完整训练结果
- Seeds 45-46 为 post-hoc 添加（§4.3），削弱 pre-registered 设计的可信度
- 论文自身注明统计检验为 "exploratory"（§4.2），但 abstract/contributions 以确定性语气陈述

**要求**：(1) Abstract 和 C2 措辞需反映统计不确定性（如 "demonstrates that the Goodhart effect can occur" 而非 "occurs frequently"）；(2) 正文中给出 binomial CI 提示读者效力限制；(3) 如资源允许，增加 exec-only seeds。

### W3 [warning→aggregated] 单一模型限制泛化性

**共识度**: R1 + R2 均提出（跨轮次复现第 4 次）

全部实验基于 Qwen3-4B。Qwen3-8B 无法收敛（Appendix D.7），LLaMA-3.2-3B 无法冷启动（Appendix D.4）。结构退化是否为 Qwen3 家族的特殊性质尚不可知。

**说明**：论文已在 §6 Limitations 中充分说明，claims 已 scope 到 Qwen3-4B。作为结构性限制标注为 wont_fix（前提是 claims 不外推）。当前 §6 表述 "cross-scale generalization remains untested" 与 D.7 的实际阴性结果一致（8B 未收敛≠退化被测试），无需修改。

---

## Weaknesses (Should-Fix)

### W4 [warning] ISR/ISR* 术语使用不一致

**共识度**: R1 + R2 均认同

§3.2 定义 ISR*（proved-only ISR）并声明 "We report ISR* throughout"，但后续行文中频繁使用 ISR 而非 ISR*（如 §4.2 标题、§4.3 标题）。读者需要反复确认所指。

**要求**：首次使用后加 "henceforth ISR refers to ISR* unless otherwise noted" 或全文统一标注。

### W5 [warning] 缺少与 PRM 的 Goodhart susceptibility 对比讨论

**共识度**: R1 + R2 均认同

§2 引用 PRM 文献（Lightman, Math-Shepherd, Setlur, Cui）但仅作背景。核心 claim 是 structural rewards 被优化时失效——PRM 的 step-level signal 是否面临同样风险？这一对比会强化论文定位。

**要求**：在 Discussion 或 Related Work 中增加 1-2 句对比。

### W6 [warning] Premise-count confound 对 compositional evidence 的影响

**共识度**: R1 提出

ISR 的 LOO sensitivity 与 premise 数量正相关：premise 多的问题天然 LOO 移除后更可能保留证明能力。这个 confound 可能部分解释 "compositional reasoning requires more premises → higher ISR" 的观察。

**要求**：讨论 premise-count 作为 confound 的可能性，或在分析中控制 premise 数量。

### W7 [warning] Shapley value 表述不精确

**共识度**: R1 提出

§3 提及 LOO = marginal Shapley，但 LOO ≠ Shapley value（后者需所有子集组合）。Appendix 有 4 行推导但正文措辞仍可能误导。

**要求**：正文中明确 "LOO is equivalent to Shapley under component independence assumption"。

---

## Minor Issues (不影响接收)

- Abstract 末句结构较长但语法正确（R1 rebut R2 的语法问题）
- Hacking mode 正文说 "eight" 与 Appendix C 9 节的关系：TS 拆分为 TSa/TSb 两个子节，Table 7 列 8 个模式。建议 Appendix C 开头加说明。
- Table 1 信息密度高，可考虑列组标题提升可读性。
- Figure 5 子面板字号较小，接近可读性下限。

---

## Missing References

1. **Krakovna et al. (2020)** "Specification gaming examples in AI" — specification gaming 领域标准参考，与 hacking taxonomy 直接相关。（R1 + R2 均认同）

**注**：R2 标记的 "LLMs Gaming Verifiers" (arXiv:2604.15149) 和 "Math-Shepherd" (Wang et al., 2024) 均已被论文引用。R2 存在核对失误。

---

## External Review

未请求外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: 完成 (0 critical / 2 warning / 6 info)

| 严重度 | 位置 | 发现 |
|--------|------|------|
| warning | p.19 | 页面底部约 40% 空白（Section D.1 文本提前结束） |
| warning | p.24 | 页面底部约 45% 空白（Section E 内容较短，末页可接受） |
| info | p.2-8 | Figure 1/3/4 红绿配色对色盲不友好，建议加 hatching/marker |
| info | p.8 | Figure 5 子面板字号接近下限 |
| info | p.4 | Figure 2 设计精良，✓/✗ 符号色盲友好（正面） |
| info | p.5 | Table 1 booktabs 格式规范（正面） |

---

## Overall Assessment

**评分: 3.5 / 5 — Borderline Conference**

**评分逻辑**：
- R1: 3.5 (Borderline Conference) — 基于方法实用性 + 实证系统性
- R2: 3.0 (Findings) — 基于概念新颖性不足
- R2 审稿包含 4 处事实性错误（模型大小 1B→实为 4B；声称 Prolog 缺 ISR-reward 数据→Table 11 存在完整数据；标记 2 篇已引用文献为 missing），这些错误削弱了 R2 评分的可信度
- 但 R2 关于 novelty 和统计效力的核心论点仍然有效

**给分理由**：
- 论文方法（LOO/STA）本身不新颖，核心发现（observe-vs-optimize asymmetry）是 Goodhart's Law 的领域特定实证化——这确实更接近 Findings 性质
- 但实证贡献的深度（6 条件 × 5 seeds × 2 逻辑 × 8 hacking modes）、taxonomy 的实用价值、Prolog 3/3 universal gaming 的跨逻辑复制，以及学术诚实性（坦诚报告限制和阴性结果），将其推向 borderline conference
- 统计效力不足是最大弱点，但论文已在正文中透明处理（existence claim framing, exploratory 标注）
- 如果 C1 overclaim 和 abstract 语气两个问题得到修正，论文质量足以支撑 borderline conference

**拒稿风险**：如果审稿人（像 R2）主要从概念新颖性角度评估，可能判 Findings (3.0)。如果从实证系统性和实用价值角度评估（R1 视角），可能判 Conference (3.5-4.0)。建议作者明确定位为 empirical study，强调实证发现而非方法创新。

---

## Detailed Comments

### 致作者的核心建议（优先级排序）

1. **[最优先] 修正 C1 framing**：将 "we propose STA as a diagnostic method" 改为 "we systematically apply LOO ablation to..."，让读者期望对准实证贡献而非方法创新。

2. **[高优先] Abstract/C2 统计语气**：将 "3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect occurs frequently" 调整为 "3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect can occur under standard training conditions"。

3. **[中优先] ISR/ISR* 统一**：加一句 "henceforth ISR denotes ISR*" 即可解决。

4. **[中优先] PRM 对比**：在 §5 Discussion 末尾加 1-2 句 "Whether process reward models face analogous Goodhart risks at the step level remains an open question" 即可。

5. **[低优先] Krakovna citation**：添加即可。

### 格式合规性

- ✅ ACL 模板正确
- ✅ 正文 8 页（含 Limitations）
- ✅ Abstract 189 词（≤200）
- ✅ Limitations 在正文 §6（非 Appendix）
- ✅ 匿名合规（无身份泄露）
- ✅ AI assistants 声明（Section E）

---

## 交叉分享分歧记录

| 争议点 | R1 | R2 | Director 裁定 |
|--------|-----|-----|--------------|
| 模型大小 | 4B（正确）| 1B（错误）| R1 正确。论文明确使用 Qwen3-4B。|
| Prolog ISR-reward | Table 11 存在 | 仅 exec-only | R1 正确。Table 11 完整报告 3 seeds ISR-reward Prolog 结果。|
| Missing refs (2/3) | 已引用 | 标记 missing | R1 正确。Math-Shepherd 和 LLMs Gaming Verifiers 均已在参考文献中。|
| 新颖性评分 | 3.5 | 3.0 | 采 3.5。R2 的 novelty 关切有效但其事实错误削弱评分可信度。|
| 统计效力 | 同意 | 同意 | 共识。本文最大弱点。|
| C1 overclaim | 部分同意 | 强烈主张 | 共识。需修正。|