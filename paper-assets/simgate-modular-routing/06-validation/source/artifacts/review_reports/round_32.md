---
round: 32
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-25T21:49:29.355796+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 32 审稿报告

**Venue**: EMNLP 2026 (ARR)  |  **Reviewers**: 2  |  **Rounds**: 1（交叉回应后收敛）  |  **模式**: Fresh review

---

## Summary

本文提出 Death Avoidance Framework (DAF)，用于诊断 LLM agent 多策略路由中的信号组成。通过在 ScienceWorld 环境中对 deterministic 和 internal 两种策略进行 matched-seed paired comparison，论文发现 78.9% 的路由标签由 death avoidance 驱动（DAF=90.4% at P=100），并在 3 个模型族（7B-72B）和 2 个 agent improvement 方法下验证了该发现的稳健性。论文还在 MATH 和 ALFWorld 进行了跨环境 probe，分别显示 no routing signal 和 information asymmetry-dominated signal。

## Strengths

**S1. "先诊断再路由"的范式价值**：不同于直接学习 router 的主流方法，论文提出先分解 routing signal 的组成——这一 diagnostic 视角具有独立的方法论贡献（R1 Excitement 3.5/5）。

**S2. 实验设计严谨**：matched-seed paired comparison 设计、完整的 anti-cherry-picking 分析（排除的 19 个 task 的 ΔDR=+38.2pp > 保留的 +28.7pp）、多层统计检验（episode-level bootstrap CI、permutation test p=0.002、leave-one-out、sign test）。

**S3. 多维稳健性验证**：3 个模型族（Qwen2.5/Llama-3.1/Gemma-2）、2 个 agent improvement 方法（Retry/Reflexion）、72B 规模 probe——核心发现在多维度下保持稳健。

**S4. 负面结果的诚实报告**：router 训练失败（§3.5）和跨环境 probe 的零/弱信号结果（Table 5）均如实报告，而非隐藏或 spin 为正面发现。

**S5. 材料完整性**：21 个附录提供了全面的补充分析、failure mode 分类、sensitivity analysis 和 ablation study。

## Weaknesses

### Must-Fix (Critical)

**[C1] 核心发现的 Triviality 风险——P-dependence + Oracle Privilege 双重叠加** [R1-W1, R1-W2, R2-N1; AGREE x2]

论文的两个标志性数字（DAF=90.4%, label fraction=78.9%）受到两个独立因素的质疑：

(a) **P-dependence**：DAF = 1 − Δ_nd/(Δ^P + Δ_nd) 在数学上保证 P→∞ 时 DAF→1。Appendix K 显示 P=0 时 DAF=7.4%，P=100 时 DAF=90.4%——"death dominance" 的强度是惩罚参数的单调函数而非环境的固有属性。虽然 label fraction 78.9% 是 P-invariant 的，但正文对两者的区分不够清晰，且 headline positions（Abstract/Intro）仍多处突出 DAF=90.4%。

(b) **Oracle privilege**：deterministic strategy 通过 privileged simulator access（§3.1）直接读取环境状态，其 death rate 16.3% vs internal 的 42.9%（Table 1）在很大程度上源于信息不对称而非策略类型差异。缺少 non-oracle deterministic baseline 作为控制实验来分离 oracle effect 与 strategy effect。

两个因素叠加后，核心发现接近 "强 oracle 在高惩罚环境中避免灾难性失败" 这一不言自明的结论。

**建议**：(1) 将 headline claim 锚定在 P-invariant 指标（ΔDR=28.7pp）上；(2) 补充 non-oracle deterministic baseline；(3) 将贡献从 "discover death dominance" 重新定位为 "provide diagnostic framework that quantifies routing signal composition"。

**[C2] 跨环境验证严重不足** [R1-W5, R2-N2; AGREE x2]

三个环境仅覆盖信号空间的极端：ScienceWorld（death-dominated, DAF≈90%）、MATH（no signal, near-identical accuracy）、ALFWorld（information asymmetry, no death）。缺少中间验证——例如 death 存在但 DAF 在 30-60% 范围的环境。框架在中间地带的诊断能力未经检验。

ALFWorld 的 probe 尤其初步：仅报告 label 分布，未做完整 DAF 分解。考虑到 ALFWorld 的 Δ_int = -10.70（Table 5），其 information asymmetry 机制值得深入分析。

如果 ScienceWorld 整体就是 death-dominated 环境（所有 30 个 task 的 ΔDR 均 >0），发现的 scope 可能仅为 "ScienceWorld is death-dominated" 而非 "routing signal is generally death-dominated"。

### Should-Fix (Warning)

**[W1] DAF 公式的 P-dependence 需在正文充分讨论** [R1-W1, R2-W1; AGREE x2]

Penalty sensitivity analysis（Appendix K）直接关系到核心 claim 的稳健性。目前正文对 P-dependence 几乎一笔带过（§3.4 仅脚注提到 P*=100），读者需翻到第 16 页才能看到 DAF 随 P 变化的全貌。这不是补充分析，而是核心方法论问题被放在了附录中。建议将 Appendix K 核心结论移至正文 §3.4。

**[W2] "Counterfactual" 术语使用松散** [R1-W4, R2-W3; AGREE x2]

论文的 paired controlled comparison 设计（同一实例、同一种子、两种策略）在 ScienceWorld 的确定性环境中确实可以观测两个 potential outcomes，但 "counterfactual" 与因果推断文献（Rubin 1974, Pearl 2009）的标准用法存在偏差。distributional decomposition ≠ causal decomposition。建议在 §3 开头加简短定位声明。

**[W3] Router 训练负面结果的过度推断** [R1-W6, R2-W4; AGREE x2]

从 LoRA rank=8、245 episodes、Qwen2.5-7B 的单一配置得出 "no exploitable signal" 是过度推断。Appendix P 的 capacity scaling（0.6B → 4B）显示 episode-level accuracy 仅在 4B 时勉强超过 random baseline，这更可能是 data/capacity insufficiency 而非 signal absence。论文应区分 "no signal exists" 与 "signal not learnable with this setup"。替代假设包括：特征表示不够（仅 LLM hidden states）、数据不足（245 episodes 对 binary classification）、评估指标天花板。

**[W4] 附录体量异常（21 节, ~15 页）** [R2-W1; R1 AGREE]

关键的 Penalty sensitivity（App K）、Failure mode analysis（App N）、Grounding ablation（App O）直接关系核心 claim，但被放在附录深处。读者无法仅通过正文评估贡献的稳健性。建议将 App K 的核心结论移至正文 §3.4。

**[W5] Spearman ρ=0.586 与 Pearson r=0.97 的巨大差异** [R1-W8; R2 AGREE]

正文 Figure 3 突出展示 Pearson r=0.97（"near-perfect correlation"），但 Appendix D 的 Spearman ρ=0.586 远低于此。Pearson r 对极端值敏感，K=11 个点中少数高 death rate 任务（如 chemistry-mix Δ_int=+47.50）可能驱动 r 的膨胀。ρ=0.586 虽仍显著（p<0.05）但远不能称为 "near-perfect"。正文应同时报告两个相关系数并讨论差异原因。

**[W6] Discussion 过薄** [R2-W8]

Discussion section（~0.5 页, 2 个话题）缺少关键讨论：(1) death avoidance 何时/何条件下 dominate（P/max_score 条件分析）；(2) 与 concurrent adaptive routing work 的对话；(3) 与 risk-sensitive RL / CVaR 的概念连接。

**[W7] Related Work 缺 Risk-sensitive RL / CVaR 文献** [R2-W5; R1 AGREE]

Death avoidance 与 risk-sensitive RL 的 tail-risk minimization（CVaR, Tamar 2015; Chow 2015; Dabney 2018）在概念上高度相关——论文将 death 视为 catastrophic failure，正是 CVaR 优化的场景。§2 或 §5 应引用并讨论连接。Agent failure taxonomy（Kambhampati 2024, Valmeekam 2023）与 Appendix N 的 failure mode analysis 直接相关，也应引用。

### Minor

**[M1] "708-scale" 疑为排版错误** [R1-W10; R2 AGREE]
Abstract 中 "three model families (7B-708B) at 708-scale" 中最大模型为 Qwen2.5-72B（Table 3）。"708" 可能是 "70B" 或 "70.8B" 的排版错误。需更正。

**[M2] Table 2 D/I/N 列标题不直观** [R1; R2 AGREE]
需查 caption 才能理解。建议改为 Det/Int/NoPref 或在表头加脚注。

**[M3] §4.3 未报告 intervention 对 DAF 的影响** [R1; R2 AGREE]
Retry 和 Reflexion 改变了 death rate（Table 1: Retry 43.5%, Reflexion 31.4%），但未报告 DAF 是否同步变化。这会加强或暴露 death avoidance 作为 routing signal 的稳健性/脆弱性，无论结果如何都有信息量。

**[M4] Eq.(4) 近似缺 worst-case bound** [R1-W9; R2 AGREE]
残差 0.23（占 Δ_tot 的 0.8%）虽小，但正式给出 bound（如基于 death-conditional score 分布 range）会强化论证严谨性。

**[M5] Figure 2/4 字号偏小** [Visual Check; R1 noted]
Figure 2 axis label 和 legend ≤6pt，Figure 4 action sequence 文字标签偏小，150 dpi 下已难辨认。

**[M6] Pages 5/7 图表密度过高** [Visual Check]
Page 5 包含 4 个 display items（Figure 3 + Figure 4 + Table 1 + Table 2），Page 7 包含 3 个（Figure 5 + Figure 6 + Table 5），连续形成"图表密集带"。建议将 Table 2 移至 page 6。

## Reviewer Consensus

两位 Reviewer 在以下关键问题上完全一致（AGREE x2）：

1. **P-dependence + Oracle privilege 双重叠加**使核心发现接近 tautology（Critical）
2. **跨环境验证仅覆盖极端**，缺少中间 case（Critical）
3. **"Counterfactual" 术语**需明确定位（Warning）
4. **Router 负面结果**可能反映训练不足而非信号缺失（Warning）
5. **附录过重**，核心 claim 支撑材料被埋在附录中（Warning）
6. **Spearman vs Pearson 差异**需在正文讨论（Warning）
7. **Missing references**: Risk-sensitive RL/CVaR, Agent failure taxonomy, Uesato 2022, Lightman 2023, Snell 2024

## Reviewer Divergence

**[D1] K=11 Cluster Bootstrap（R1-W3 vs R2 REBUT）**
R1 认为 K=11 低于推荐阈值（K≥20-50），cluster bootstrap CI 可能不可靠。R2 反驳——论文核心推断使用 episode-level bootstrap（N=245），cluster bootstrap 仅为 sensitivity analysis，且论文已在 Appendix E 主动承认其局限性。补充统计检验（LOO, sign test, permutation p=0.002）支撑充分。
**Director 判断**：R2 的反驳有效。核心推断链不依赖 cluster bootstrap。维持 Warning 而非 Critical。

**[D2] Anti-cherry-picking / Scope（R1-W7 vs R2 partial REBUT）**
R1 质疑全部 30 tasks 可能都是 death-dominated，发现仅关于 ScienceWorld 而非 routing。R2 反驳——排除的 19 tasks 的 ΔDR (+38.2pp) > 保留的 (+28.7pp)，这与 cherry-picking 假设相反。但 R2 同意 deeper scope 问题成立：即使无 cherry-picking，如果 ScienceWorld 整体就是 death-dominated，发现的 scope 就是 "ScienceWorld is death-dominated"。
**Director 判断**：cherry-picking 指控不成立，但 scope 限制真实——回归 C2（跨环境验证不足）。

**[D3] Concurrent Work 差异化（R2-W2 vs R1 REBUT）**
R2 认为与 concurrent work 差异化不够锐利。R1 反驳——§2 Related Work 的差异化讨论不只是一句话，已有较大篇幅区分 "先诊断再路由" vs "直接学 router" 的核心差异。
**Director 判断**：R1 的反驳部分有效。差异化已有基础，但增加显式 comparison table 仍有价值。降级为建议而非 Weakness。

**[D4] Excitement / Overall Score**
R1 给 3.5（Borderline Conference），Excitement 3.5/5；R2 给 3.0（Findings），Excitement 2/5。
分歧核心：R1 认为 "先诊断再路由" 范式本身有方法论贡献，即使具体发现 information content 有限；R2 认为 oracle + P-dependence 双重叠加后 novelty 受损严重，框架贡献量级更适合 Findings。
**Director 判断**：采纳 3.0。两个 Critical 问题均获双方共识，Excitement 均值 2.75/5 低于 Conference 门槛，贡献类型在当前实证基础上更适合 Findings。

## Questions

**Q1. ΔDR 重新锚定**：如果将核心 claim 从 DAF=90.4% 重新锚定在 P-invariant 的 ΔDR=28.7pp 上，结论本质不变但对 P-dependence 批评的抵抗力大幅增强。作者是否愿意采纳？

**Q2. Non-oracle deterministic baseline**：是否可以设计 non-oracle deterministic strategy（仅使用 LLM 可观察信息，deterministic action selection logic），以分离 oracle effect 与 strategy effect？如果 non-oracle deterministic 的 death rate 接近 internal（~42.9%），则 death asymmetry 主要来自 oracle access；如果仍远低于 internal，则策略结构本身有独立的安全效果。

**Q3. Table 12 vs §4.5 评估协议差异**：Table 12 的 6-seed cross-split evaluation 与 §4.5 的固定 seed single-trial evaluation 的 accuracy 数字不直接可比——47.1±5.4%（cross-validated mean）vs always-deterministic 96.3%（oracle-agreement rate）。正文应更明确区分两个评估框架。

**Q4. P=100 的环境特异性**：P=100 是 ScienceWorld 的内置惩罚（all-or-nothing, P/max_score ≈ 1），而非作者选择。论文应讨论 P/max_score 比值对 DAF 的影响——在 P/max_score ≈ 1 时 death dominance 是预期的，在 P/max_score << 1 时可能不成立。

**Q5. Grounding ablation 后 DAF 重新计算**：当前 grounding ablation（Appendix O）仅报告 death rate 变化（+26.6pp → ~+8pp），未重新收集 counterfactual 计算 DAF。这是验证 "death dominance vs grounding confusion" 的关键缺失实验。

## Missing References

以下文献与论文主题直接相关但未被引用：

1. **Risk-sensitive RL / CVaR**：Tamar et al. (2015) "Optimizing the CVaR via Sampling"; Chow et al. (2015) "Risk-sensitive and robust decision-making"; Dabney et al. (2018) "Implicit quantile networks"——death avoidance 本质是 tail-risk minimization
2. **Agent failure taxonomy**：Kambhampati et al. (2024), Valmeekam et al. (2023)——LLM agent planning 局限性分析，与论文的 failure mode analysis（App N）直接相关
3. **Process vs outcome feedback**：Uesato et al. (2022) "Solving math word problems with process- and outcome-based feedback"——Algorithm 1 实质是 outcome-based labeling
4. **Process reward models**：Lightman et al. (2023) "Let's Verify Step by Step"——step-level supervision 可能改善 router 性能
5. **Scaling test-time compute**：Snell et al. (2024)——adaptive computation routing 的 compute-optimal 决策

注：Adaptive computation / early exit 文献（Universal Transformers, CALM）在抽象层次上与本文有本质差异（layer-level vs episode-level），引用非必要（R1 rebut 有效）。

## External Review (Stanford Agentic Reviewer)

**状态：未请求。**

## Visual Layout Check（非评分项）

**状态：已完成**（耗时 ~3 分钟）

| 严重度 | 位置 | 描述 |
|--------|------|------|
| ⚠️ Warning | Page 5 | 单页 4 个 display items（Figure 3 + Figure 4 + Table 1 + Table 2），视觉极度拥挤 |
| ⚠️ Warning | Page 7 | 3 个 display items（Figure 5 + Figure 6 + Table 5），与 page 5 连续形成图表密集带 |
| ⚠️ Warning | Page 3 | Figure 2 axis label 和 legend ≤6pt，低分辨率下难辨认 |
| ⚠️ Warning | Page 5 | Figure 4 action sequence 文字标签字号过小 |
| ℹ️ Info | Page 2 | Figure 1 framework 图整体清晰，部分箭头和小字标注缩小后不够醒目 |
| ℹ️ Info | Page 5 | Figure 3 散点图单栏宽度，数据点拥挤，改为 figure* 全宽可提升可读性 |
| ℹ️ Info | Page 6 | Table 3/4 booktabs 风格规范，最优值加粗 |
| ℹ️ Info | Page 8 | Limitations 段落简短（~1/3 栏），符合 EMNLP 要求 |
| ℹ️ Info | Pages 9-10 | References 排版正常，无未解析引用 |
| ℹ️ Info | Page 11 | Appendix 目录 A-T 共 20 个附录，条目清晰 |
| ℹ️ Info | Page 4 | Algorithm 1 伪代码和公式 (1)-(5) 渲染正确 |

**统计**：0 Critical, 4 Warning, 11 Info

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3/5 | 2.5/5 | 2.5-3/5 |
| Excitement | 3.5/5 | 2/5 | 2.5/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.5 | 3.0 | **3.0** |
| Confidence | 4/5 | 4/5 | 4/5 |

**综合评分：3.0 (Findings)**

**理由**：论文的 diagnostic framework 思路有方法论价值（S1），实验设计在给定设定下严谨（S2-S3），负面结果报告诚实（S4）。但两个结构性问题——(1) oracle privilege 使 death avoidance 发现接近预期结论（C1），(2) 单一主环境 + 极端跨环境 probe 无法支撑泛化性声明（C2）——从根本上限制了贡献的 novelty 和 scope。DAF 对 P 的数学单调依赖进一步削弱了标志性数字的说服力（W1）。

论文适合作为 Findings 论文被接收，但需要在以下方面做出调整：(1) 贡献 reframing（diagnostic framework vs discovery）；(2) P-invariant 指标（ΔDR）作为 headline；(3) Spearman/Pearson 双报告；(4) 正文中正面处理 P-dependence。如果作者能进一步补充 non-oracle baseline 和 intermediate cross-env probe，论文可达到 Conference 水平（3.5-4.0）。

两位 Reviewer 评分范围 3.0-3.5。Director 采纳 3.0 的主要权衡：(1) 两个 Critical 问题均获双方共识（AGREE x2）；(2) Excitement 均值 2.75/5 低于 Conference 门槛；(3) 贡献类型（diagnostic framework）在当前实证基础上更适合 Findings 定位。

## Detailed Comments

### §1 Introduction
- "708-scale" 疑为排版错误，应为 "70B-scale"（M1）
- DAF=90.4% 在 Introduction 中的突出程度应降低，考虑用 ΔDR=28.7pp 替代或并列展示（C1/W1）

### §2 Method / Framework
- "Counterfactual" 术语需在 §3 开头加定位声明——matched-seed paired comparison vs Rubin/Pearl counterfactual（W2）
- SCI 在正文仅出现一次，与 Method 中的显著度不匹配——考虑进一步降级或在 Method 中缩减描述

### §3 Results
- Figure 3 应同时报告 Pearson r=0.97 和 Spearman ρ=0.586，并讨论差异原因（极端值敏感性）（W5）
- Table 2 D/I/N 列标题改为 Det/Int/NoPref 或加表头脚注（M2）
- §3.4 应将 Appendix K 的 P-sensitivity 核心结论（DAF 随 P 单调递增是数学必然）移入正文（W1/W4）
- Eq.(4) 近似应给出 worst-case bound（M4）

### §4 Analysis
- §4.3 需补充 Retry/Reflexion 对 DAF 的影响——当前仅报告 death rate 变化（M3）
- §4.5 需与 Table 12 的评估协议差异做明确区分——cross-validated mean vs oracle-agreement rate 不可比（Q3）
- §4.6 Router 结论应从 "no exploitable signal" 改为 "signal not learnable with this setup"，并列出替代假设（W3）

### §5 Discussion
- 过薄（~0.5 页），需扩展（W6）：
  - P/max_score 条件分析：何时 death avoidance dominate 是预期的 vs 有信息量的
  - 与 CVaR / risk-sensitive RL 的概念连接
  - 与 concurrent adaptive routing work 的对话
  - Non-oracle deterministic baseline 的设计空间

### Related Work (§4)
- 补充 CVaR / risk-sensitive RL 文献（Tamar 2015, Chow 2015, Dabney 2018）（W7）
- 补充 agent failure taxonomy（Kambhampati 2024, Valmeekam 2023）
- 补充 process reward / test-time compute（Uesato 2022, Lightman 2023, Snell 2024）

### Limitations
- 长度适中（EMNLP 标准），但 5 段可适当精简至 3 段

### Visual / Format
- Page 5 图表密度过高——建议 Table 2 移至 page 6 或合并 Figure 3/4 为 subfigure（M6）
- Figure 2 和 Figure 4 字号需增大至 ≥8pt（M5）
- "708" 排版错误需更正（M1）