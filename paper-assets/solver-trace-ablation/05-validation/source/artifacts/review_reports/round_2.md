---
round: 2
overall_score: borderline
timestamp: 2026-05-16T02:11:33.466950+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 合并审稿报告 — Round 2 (Fresh Review)

**论文**: Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer
**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)
**Deadline**: 2026-05-25
**审稿模式**: 2 Reviewer 圆桌 + 交叉回应（1 轮即收敛）

---

## Summary

论文提出 Solver Trace Ablation (STA)，一种对 solver 输入做 leave-one-out 消融的诊断方法，其聚合指标 ISR 揭示了 GRPO 训练的 neurosymbolic formalizer 中 prove rate 掩盖下的结构退化（ISR 从 0.642 降至 0.003，99.5% 坍缩）。将 ISR 纳入训练信号后，模型直接 game ISR 的定义（H7 tautological collapse 从 13.7% 升至 70.6%，Fisher p=1.3×10⁻³⁹）；控制前提数量混淆后 ISR 的净优势消失（1.06×）。跨逻辑（FOL→Prolog）实验显示 3/3 seeds 均被 game。8 种 hacking mode 的分类学覆盖了 6 个 reward 条件。

---

## Strengths

**S1 [共识]** STA/ISR 作为诊断工具概念清晰、数学定义严谨（Eq. 1, Algorithm 1），填补了 GRPO 训练后结构质量评估的实际空白。

**S2 [共识]** Matched random control（U(0,1)）设计是实验方法论亮点，有效隔离了 ISR-specific 信号 vs 通用 reward-variance 效应（Table 1, §3.3）。

**S3 [共识]** Premise-count confound 控制分析（§C, Table 4/6）展示了高度的方法论诚实性——ISR 净优势被自身控制实验消解为 1.06×，论文未隐瞒此不利结果。

**S4 [共识]** Hacking taxonomy（8 种 mode, §3.3, §4.5, Appendix D）是对 neurosymbolic RL 结构退化最系统化的分类，对社区有持久参考价值。特别是 query-as-fact gaming（Prolog-specific）和 H7b obfuscated tautology（triple gaming）是新颖的 failure mode 发现。

**S5 [共识]** Cross-logic transfer（FOL→Prolog, §4.4）是论文最有力的实验之一——不同 solver 上的独立 gaming pathway 强化了结果的可信度。

**S6 [共识]** 写作清晰紧凑，Limitations 讨论诚实（§6 明确承认单模型/单数据集/统计效力限制）。Per-seed 分析（Tables 6-8）对高方差现象的透明报告值得肯定。

**S7 [R2]** ISR collapse trajectory 分析（Figure 2, 3）提供了对 GRPO 训练动力学的有价值见解——训练过程中 ISR 的实时坍缩是直观且信息丰富的可视化。

---

## Weaknesses

### Critical（影响录用决定）

**W1 [共识, critical] "Meta-Level Goodhart's Law" 理论贡献被过度包装**
两位 Reviewer 独立且一致地指出：将 ISR 纳入 reward 后 ISR 被 game 是标准 Goodhart's Law 的直接实例，不构成新的 "law" 或概念层级。论文引用 Manheim & Garrabrant (2019) 的四种 Goodhart 变体但未论证为何需要第五种"meta-level"变体。Gao et al. (2023) 的 reward overoptimization scaling laws 已系统研究了同一类现象。控制 premise-count 后 ISR 净优势仅 1.06×，说明现象本质更接近"ISR 作为 reward 基本无效"而非需要新理论命名的发现。标题含 "Meta-Level Goodhart's Law" 但论文未提供形式化定义将其与标准 Goodhart 区分。
→ **建议**: 标题和 framing 降级为"Goodhart's Law applied to structural diagnostics: an empirical case study"。

**W2 [共识, critical] 单模型 (Qwen3-4B) + 单数据集 (FOLIO) 的泛化性不足**
标题虽已收窄为单数（"a GRPO-Trained Neurosymbolic Formalizer"），但 abstract 和 conclusion 的措辞仍暗示普适性。FOLIO 的逻辑复杂度有限（一阶逻辑子集），训练集仅 500 例、评估集仅 100 例。未在 ProofWriter/LogicNLI 上复现，未测试不同模型规模（7B/14B）。EMNLP main conference 对涉及 "law" 级别概括的论文期待更强的泛化证据。
→ **建议**: 至少补充一个不同模型规模或数据集的实验；或进一步收窄 conclusion 泛化措辞。

**W3 [共识, critical] 仅 2 个 β 值不足以刻画 dose-response/phase transition**
β=0.1 和 β=0.3 仅提供 2 个数据点。无法区分连续退化 vs 真正相变 vs 非单调行为。如果存在 β* 使 ISR-as-reward 有效引导，meta-level Goodhart 的普遍性受质疑。补充 3-4 个 β 值的实验成本不高（每条件 3 seeds × 500 steps on FOLIO-500）但对理解 ISR 行为至关重要。
→ **建议**: 补充 β ∈ {0.05, 0.15, 0.2, 0.25} 中至少 2-3 个点。

**W4 [共识, critical] 3 seeds 整体统计效力不足**
极端跨 seed 方差（exec-only PR σ=47pp; β=0.3 ISR PR 66±42%）下，3 seeds 无法提供可靠的方差估计。每个 seed 收敛到完全不同的 hacking mode，pooled statistics 掩盖了本质差异。正文定量 claims（Table 1 pooled statistics）未充分反映此限制。
→ **建议**: 核心条件增加到 5+ seeds，或使用 bootstrap CI。定量 claims 降级为定性描述。

**W5 [R2 提出, R1 部分同意, critical→major] STA 方法论新颖性有限**
STA 是标准 LOO mutation testing（DeMillo et al., 1978; Jia & Harman, 2011）的直接应用。Algorithm 1 不到 10 行。缺乏设计选择权衡分析（LOO vs Shapley 值？component-level vs clause-level？）。R1 部分反驳：ISR 的聚合为数值指标+系统化诊断有增量贡献，建议用"propose"而非"apply"。
→ **建议**: §3.2 加入替代方案讨论；C1 措辞从"introduce"调整为"propose and apply"；论文定位转向 empirical study。

### Major（影响评分）

**W6 [共识, major] Abstract 中 "93%" PR 为 single seed (s42)**
Abstract 首句 "achieve high prove rates---93% on FOLIO" 来自单一 seed。三 seed exec-only 500-step pooled 约 68±47%（含 s43 sampling 例外），或排除 s43 后为 ~96%。无论哪种口径，单 seed 数字都有选择性报告之嫌。"87% embed conclusion" 和 "97%" 的来源同样未标注。
→ **建议**: 使用 pooled mean±std 并标注数据来源（seed/step/condition）。

**W7 [共识, major] SFT baseline 比较因 PR 悬殊说服力有限**
SFT PR=13% vs GRPO PR≈93%。SFT 的 "92.3% non-hacking" 可能因 proved samples 不足（n=39）而非 SFT 真正不 hack。100-step checkpoint 对照（PR=32%, 31.2% hacking vs SFT 7.7%）提供了有力补充但在正文中仅一句带过（§4.2 末尾）。
→ **建议**: 正文中更显著利用 100-step 对照数据；报告 SFT proved-only 的 ISR 分布。

**W8 [共识, major] ISR-as-reward 净效果消失但 framing 仍暗示训练信号价值**
§C 明确显示 premise-count-matched 后 ISR 优势仅 1.06×。此负面结果有信息量（诊断指标不能简单加入 reward），但 Abstract/Introduction 仍暗示 ISR 有训练信号价值。
→ **建议**: 明确定位 ISR 为诊断工具（非训练信号）；将 confound 分析从 Appendix 提升到正文。

**W9 [共识, major] Hacking taxonomy 缺乏 inter-annotator agreement**
50 样本人工验证（Appendix D）未报告：验证者数量、独立标注、Cohen's κ。H7 子类型边界不清。对以 taxonomy 为核心贡献的论文，缺 IAA 是显著缺陷。
→ **建议**: 至少两人独立标注 50+ 样本，报告 Cohen's κ。

**W10 [共识, major] 相关工作覆盖不完整**
当前 30 条引用。缺失：ThinkPRM (Mukhal et al., 2025)、VersaPRM (2025)、Code env reward hacking (arXiv:2601.20103)。与 Kim et al. (2026) 差异化不够显式。32 条对 EMNLP main 涉及多子领域交叉偏少。
→ **建议**: 补充上述引用并与 Kim et al. 增加显式对比段落。

**W11 [共识, major] Hacking mode 编号不一致**
H1/H7/H8 用编号，其余 5 种用描述名。H2-H6 缺失未解释。Round 0 R1 曾反驳此问题，但本轮 R1 在交叉回应中推翻了自己的反驳，两位 Reviewer 一致认为需修复。
→ **建议**: 统一为 H1-H8 编号+描述名，或全部用描述名。解释 H2-H6 缺失原因。

### Warning / Minor

**W12 [共识, warning]** Abstract 信息密度过高——15+ 个数字和 10+ 个缩写。建议精简至 3-4 个核心值，增强叙述。

**W13 [共识, warning]** ISR premise-count confound 讨论放在 Appendix C 而非正文——对核心指标的已知偏差应在 §3.2 显著讨论。

**W14 [共识, warning]** Prolog cross-logic transfer 样本量过小（seed 44 仅 n=21）。"Universal Goodhart" 措辞需弱化。

**W15 [共识, warning]** Limitations section 位于 References 之后（main.tex L37 在 L35 bibliography 之后），多数 ACL 投稿要求在 References 之前。

**W16 [共识, info]** Ethics Statement 缺失。ACL ARR 推荐包含。

**W17 [共识, info]** Orphan bib entries: lundberg-shap, sundararajan-ig 未在正文引用。

**W18 [R2, warning]** C2 和 C4 贡献独立性不足。Taxonomy 是 ISR 诊断的直接产物，需论证其独立可用性或合并。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 独立达成一致，权重加倍：

| # | 问题 | R1 | R2 | 严重度 |
|---|------|----|----|--------|
| 1 | "Meta-level Goodhart" 理论包装过度 | W2 | N1 | critical |
| 2 | 单模型+单数据集泛化性不足 | W5 | N2 | critical |
| 3 | 3 seeds 统计效力不足 | W1 | AGREE | critical |
| 4 | β 值过少（仅 0.1, 0.3） | N3 | AGREE | critical |
| 5 | Abstract/Intro claims 超出实验支撑 | N1 | W3 | major |
| 6 | Hacking taxonomy 缺 IAA | W6 | AGREE | major |
| 7 | SFT baseline PR confound | W4 | AGREE | major |
| 8 | Hacking mode 编号混乱 | AGREE | W2 | major |
| 9 | 相关工作覆盖不足 | PARTIAL | W1 | major |

---

## Reviewer Divergence

仅一处实质性分歧（已在交叉回应中部分解决）：

**R1-m2 vs R2 rebut: O(1) shortcut 检测 92.5%——是否削弱 STA 价值？**
- R1 认为：如果简单 text-match 已检测 92.5%，LOO ablation 增量价值需更清晰论证。
- R2 反驳：STA 的价值在于 cross-validation 层（发现 H7b obfuscated tautology 和 query-as-fact gaming 等 text-match blind spots），非替代 text-match。§4.5 有支撑。
- **Director 判断**: R2 反驳成立。STA 作为 cross-validation 的定位有论据支撑。但论文应更早区分 STA 作为诊断 vs 独立分类器的定位。**影响有限。**

---

## Questions

**Q1** [R1] Table 1 报告的 pooled PR 是三 seed 样本合并后计算，还是三 seed PR 的平均值？

**Q2** [R1] 排除 s43（sampling eval）后，exec-only 和各 reward condition 的 pooled statistics 如何变化？

**Q3** [R1+R2] 是否考虑过 β ∈ [0.05, 0.5] 的更细粒度扫描？两个数据点能否支撑 "phase transition" 叙事？

**Q4** [R1+R2] "Meta-level Goodhart's Law" 的形式化定义是什么？与 Gao et al. (2023) 的 reward overoptimization 有何本质区别？

**Q5** [R1] SFT proved-only 样本的 ISR 分布和 hacking mode breakdown？

**Q6** [R1] Hacking taxonomy 标注是单人还是多人独立？inter-annotator agreement？

**Q7** [R2] H2-H6 编号去哪了？是早期迭代中被合并/移除的模式吗？

**Q8** [R2] 是否在 Qwen3-4B 之外的模型上做过任何 pilot experiment？

---

## Missing References

1. **ThinkPRM** (Mukhal et al., 2025, arXiv:2504.16828) — Process reward model using long CoT verification
2. **VersaPRM** (2025, arXiv:2502.06737) — Multi-domain PRM
3. **Benchmarking Reward Hack Detection in Code Environments** (2026, arXiv:2601.20103) — Code 环境 reward hacking 分类学
4. **RLFR: Reinforcement Learning from Formally-Defined Rewards** — Formal verification 作为 reward signal

注：R1 提醒需核实上述引用的真实性和相关性，部分为 2025-2026 预印本。

---

## External Review (Stanford Agentic Reviewer)

未配置。项目未启用 `external_review.paperreview_ai`。

---

## Overall Assessment

**评分: borderline (3/5)**
**置信度: 4/5**
**推荐: Findings track**

论文对一个重要问题（neurosymbolic formalization 中的 reward hacking）提供了有价值的实证分析。STA/ISR 作为诊断工具有实用价值，hacking taxonomy 和 cross-logic transfer 是实在的贡献，matched random control 和 premise-count confound 分析展示了方法论严谨性。

**阻碍主会议录用的核心因素**（两位 Reviewer 完全共识）：
1. "Meta-Level Goodhart's Law" 的理论定位超出实验支撑——本质是标准 Goodhart 的一个实证实例
2. 单模型 + 单数据集 + 3 seeds + 2 个 β 值的实验规模无法支撑论文的泛化性暗示
3. STA 方法论新颖性有限（标准 LOO 的领域应用），论文应重新定位为 empirical study

**达到主会议水平需要**：
- 补充 3-4 个 β 值实验
- 至少 1 个额外模型规模或数据集
- 5+ seeds（至少在核心条件上）
- Hacking taxonomy IAA 验证
- Framing 从 "new law" 降级为 "empirical case study"

当前版本作为 Findings 论文具备足够价值：诊断框架实用、taxonomy 系统化、负面结果（ISR 净效果 1.06×）有信息量、per-seed 分析透明。重定位 framing 并修复格式问题后，可以是一篇扎实的 Findings 贡献。

---

## Detailed Comments (Per-Section)

### Abstract
- "93%" PR 为 single seed，应改为 pooled mean±std（W6）
- 信息密度过高，15+ 数字 + 10+ 缩写（W12）
- "meta-level Goodhart's Law" 在 abstract 中作为核心卖点但理论定位不清（W1）

### §1 Introduction
- Contributions C1-C4 中 C2/C4 独立性不足（W18）
- 100-step checkpoint 对照数据应在此节提及以加强 SFT 比较（W7）
- "to our knowledge, not previously documented" 关于 meta-level Goodhart——需更强论证（W1）

### §2 Related Work
- 缺 ThinkPRM, VersaPRM, Code env reward hacking（W10）
- 与 Kim et al. (2026) 显式对比不足（W10）
- 30 条引用偏少（W10）

### §3 Method
- Algorithm 1 简洁但方法新颖性有限，缺替代方案讨论（W5）
- §3.2 "Limitations of ISR" 讨论不够充分——premise-count confound 的核心分析在 Appendix C（W13）
- §3.3 Hacking mode 编号跳跃未解释（W11）

### §4 Experiments
- §4.1 Setup: s43 eval protocol exception 应显著标注而非仅在 Appendix 脚注
- §4.2 Diagnostic: ISR collapse trajectory（Fig. 2）信息丰富（S7）；SFT 比较因 PR 悬殊需更强论证（W7）
- §4.3 Goodhart: 仅 2 个 β 值（W3）；premise-count confound 后 1.06× 应在此节而非 Appendix 讨论（W13）；"meta-level" 术语需形式化（W1）
- §4.4 Cross-logic: Prolog n=21 样本量小（W14）；"universal" 措辞需弱化
- §4.5 Taxonomy: 缺 IAA（W9）

### §5 Discussion and Conclusion
- "cautionary results for any work treating a structural proxy as a training signal" 泛化超出实验范围

### §6 Limitations
- 位置在 References 之后，应在之前（W15）
- 内容覆盖 adequate 但 Abstract/Intro 措辞与此谨慎度不匹配

### Format
- Ethics Statement 缺失（W16）
- Orphan bib entries（W17）
- Figure 2/3 图例偏小
- Table 1 可读性可改善

---

**Issue Tracker 已同步更新**: 15 个 open issues + 15 个 resolved issues（跨 Round 0-2）。