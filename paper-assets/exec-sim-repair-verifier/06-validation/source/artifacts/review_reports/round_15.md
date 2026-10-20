---
round: 15
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-23T17:46:08.993302+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 17 审稿报告（Fresh Review）

## Summary

本文提出了三种 execution-free 代码修复验证 formulation（CLS、CWM、TRAJ）的首个系统性比较，在两个代码 LLM 家族（Qwen3、DeepSeek-Coder）、两个复杂度级别和多个随机种子下进行 ≤8B LoRA 微调评估。核心发现：function-level 下 CLS 和 CWM 统计等价（TOST p=0.007）；repo-level 下 CWM 因 format collapse 落后 CLS 18-26pp。14B 初步结果（3 seeds, 单家族）显示所有 formulation 收敛至 1.07pp 以内。

---

## Strengths

1. **统计方法论极为出色** [共识: R1, R2]：TOST 等价检验（非仅不显著）、Bayesian ROPE、clustered bootstrap + Holm-Bonferroni 校正、mixed-effects regression——在 NLP 论文中极为罕见的统计严谨度。统计层次声明清晰（§3.1: TOST primary → bootstrap CI → ROPE robustness → regression mechanism）。

2. **匹配实验设计** [共识: R1, R2]：相同超参数、训练数据、checkpoint 策略、计算预算——首个真正公平的 formulation 比较。CLS-CWM 比较的控制变量设计是方法论层面的真正贡献。

3. **诚实的局限性披露** [R1]：坦承功效不足（§3.4: ~0.3）、CLS-TRAJ 等价性未确认、confound 分析不能完全排除混淆。

4. **Failure mode taxonomy (Table 4)** [共识: R1, R2]：format collapse / decision collapse / aggregation penalty 三分类为从业者选择 verification formulation 提供了可操作的诊断标准，是本文最有实践价值的贡献。

5. **References 覆盖全面** [R2]：CodePRM, GenPRM, FunPRM, SWE-RM, CodeScaler, RepoExec, VeRPO, Aletheia, CRUXEval, SolidCoder 等近期重要工作均已引用。GenRM domain-specific 对比分析（math vs code）有 insight。

6. **丰富附录** [R1]：15+ 页 appendix 包含 robustness checks、ablation details、qualitative analysis 和 hyperparameter tables，大幅提升可审查性和可复现性。

---

## Weaknesses

### Must-Fix [共识 Critical]

**N1. TRAJ 175× 训练数据量混淆变量未得到充分控制**
[R1-N1 提出, R2 AGREE] | 对应 Issue Tracker: R6-W4

TRAJ 使用 ~400 variant-level 训练样本 vs CLS/CWM ~70K per-test 样本，差异达 175×。论文声称该差异 "inherent to the formulation"（§2.1），但无法分离 formulation effect 和 data regime effect。Appendix O 的下采样实验（CLS 降至 ~1K）仍是 TRAJ 的 2.5×。14B 收敛可能反映更大模型从少量数据学习更好（R2 补充），而非 formulation 本身收敛。关于 TRAJ 的所有结论——§3.5 的归因和 routing 建议——证据基础不足。

**建议**：(a) 将 TRAJ 比较重新定位为 "formulation-in-its-natural-data-regime" 联合比较，明确声明不是 controlled-data 比较；(b) 增加 CLS 在 ~400 samples 的极端下采样实验。

**N2. 统计功效 ~0.3 限制等价性声明的可解释性**
[R1-N2 提出, R2 AGREE] | 对应 Issue Tracker: R8-W1

TOST 功效 ~0.3 → 70% 概率无法确认等价。CLS-CWM 等价通过（p=0.007, Holm-corrected）是强证据，无争议。但 CLS-TRAJ 未通过（adjusted p=0.075）在低功效下是 inconclusive——既非等价也非不等价的证据。"not confirmed" 措辞仍暗示方向性判断，建议改为 "inconclusive"。Repo-level 2-3 seeds 功效更低（Table 14 CLS-TRAJ CI: ±10.42pp），不允许得出方向性结论。

**建议**：(a) 增加 MDE（Minimum Detectable Effect）表格；(b) 功效不足的比较使用 "inconclusive" 措辞。

**N3. 14B convergence 叙事权重与证据严重不匹配**
[R2-N2 提出, R1 AGREE] | 对应 Issue Tracker: R13-W3

14B 结果在 abstract、introduction、conclusion 中均作为关键叙事元素（"the gap narrows monotonically from 3.11pp to 1.07pp"），但仅基于 3 seeds、单一模型家族、TOST df=2。在 power ~0.3 背景下 df=2 几乎无统计区分力。论文标注 "preliminary observation" 但随后围绕它构建了 capacity-dependent account 和 GenRM 桥接论述，使读者高估 14B 发现的可靠性。Conclusion 承认 "scaling to 32B+ with more seeds" 是 future direction，实际上承认了证据不足，但 abstract 叙事未反映这一不确定性。

**建议**：(a) 14B 结果从 abstract 降级或移除；(b) conclusion 中明确标注为 speculative direction 而非 supported finding。

### Should-Fix [共识 Warning]

**W1. 标题/Abstract scope 超出实际实验范围**
[R2-N1 提出, R1 AGREE with nuance] | 对应 Issue Tracker: R16-N2

"A Systematic Comparison of Execution-Free Verification Formulations for Code Repair" 暗示通用比较，实际限于 ≤8B LoRA + 2 families + Python + 合成 mutation。R1 认为 "systematic" 可指方法论系统性而非穷举性，建议降为 Should-Fix；R2 认为读者期望更广覆盖。共识：标题或 abstract 应加范围限定。Conclusion §5 "We presented the first systematic comparison" 无任何限定词尤为突出。

**W2. 单基准/单语言/合成数据限制泛化性**
[R1-W1 + R2-W3 提出, 双方 AGREE] | 对应 Issue Tracker: R6-W6

全部实验仅 SWE-bench Verified（500 实例）+ Python + 合成 mutation（5 种 operator）。真实 repo-level bug 涉及多文件语义错误、逻辑缺陷，非简单 mutation 能覆盖。R1 补充：不同 formulation 对合成 mutation 可能有不同敏感度——CLS 对 mutation 类型更 robust，CWM 在合成 mutation 简单输出上可能被高估。此方向性 confound 论文未讨论。

**W3. CWM format collapse 的 "inherent limitation" 归因需更审慎**
[R1-W2 提出, R2 AGREE] | 对应 Issue Tracker: R16-W2

论文自身的 14B 数据（gap 收窄到 1.07pp）和 conclusion hedging 暗示 format collapse 可能是容量不足的症状，与正文中将其描述为结构性弱点（§2.2, §3.5）存在叙事张力。4 种 intervention 全在 ≤8B 上测试。建议改为 "limitation under current ≤8B LoRA training regime"。

**W4. Error complementarity 实践价值 framing 与证据不匹配**
[R1-W3 ≈ R2-W2, 双方 AGREE] | 对应 Issue Tracker: R13-W2

Oracle combination +2.80pp/+14.58pp（single-seed），但 simple routing heuristics <0.4pp。Conclusion 仍将 "complexity-aware routing" 列为第一 future direction——对 <0.4pp 的结果过于乐观。互补性在 §1 contributions list 被列为第二大贡献，权重过大。建议降级为 future work motivation 而非 standalone contribution。

**W5. ±2pp SESOI 缺少独立实践论证**
[R1-W4 提出, R2 AGREE with nuance] | 对应 Issue Tracker: R6-W1

SESOI 应基于 downstream 实践意义——2pp verifier accuracy 差异对 repair@K 影响多大？论文未提供此分析。Sensitivity analysis（±1.5-3pp）表明 CLS-CWM 等价对 margin 选择 robust，但 SESOI 本身需实践论证。R2 认为 ±2pp 是合理 convention，严重程度低于 R1 评估。

**W6. 核心发现可预测性未被讨论**
[R2-W1 提出, R1 partial REBUT] | 新建 Issue: R17-W1

"Complexity moderates formulation choice" 方向直觉可预测（CWM ~477 tokens + exact match vs CLS 1 token）。R1 反驳：方向可预测 ≠ 研究无价值，量化 18-26pp gap、function-level 等价性、format collapse 机制是 non-trivial。共识：增加讨论区分 "confirmation of intuition" vs "genuinely novel finding"。

### Dismissed

**R2-W4 (Appendix 与正文比例失衡)**：R1 有效 REBUT——ACL ARR 对 appendix 无页数限制，正文自洽，appendix 提供 reproducibility 材料是标准做法。不计入 weakness。

### Minor [共识]

- **M1**: Table 1 TRAJ 配置差异脚注（"Training configuration differs"）应在正文中更显著呈现 [R1, R2]
- **M2**: Figure 2 y-axis 非零起点应在 caption 标注（与 Figure 3 统一）[R1, R2]
- **M3**: CWM 术语可能与 RL world model 概念混淆，建议 §2.1 首次出现时加注释区分 [R2]
- **M4**: DreamPRM 和 CodePRM 建议在 Related Work 正文中增加具体讨论 [R2]

---

## Reviewer Consensus [AGREE]

1. 统计方法论是论文最大优势 [unanimous]
2. CLS-CWM function-level 等价性证据可信 (p=0.007) [unanimous]
3. TRAJ 比较因 175× data volume confound 需重新定位 [R1 raised, R2 AGREE]
4. 14B 叙事权重应降低 [R2 raised, R1 AGREE]
5. Error complementarity 目前无实用 routing 方案 [mutual AGREE]
6. Failure mode taxonomy 有独立实践价值 [unanimous]
7. 标题/结论 scope 应与实验 scope 匹配 [mutual AGREE]
8. 核心发现方向直觉可预测但量化有价值 [partial consensus]

## Reviewer Divergence

1. **Overall Assessment**: R1 3.5 (Borderline Conference) vs R2 3.0 (Findings)。分歧在于 matched experimental design 的方法论贡献是否达到 main conference novelty 门槛。R1 更看重填补文献空白的独立价值；R2 认为 empirical comparison 无 new method 难达主会议标准。合理的 judgment call。
2. **Soundness**: R1 3/5（因 TRAJ confound 和 power 限制）vs R2 4→3.5/5（交叉回应后下调）。

---

## Questions for Authors

1. 能否提供 CLS 在 ~400 samples（与 TRAJ 完全匹配）下的极端下采样实验？这将直接回答 data volume vs formulation effect 的归因问题。
2. Minimum Detectable Effect (MDE) 在当前样本量和 TOST 设置下是多少？能否提供 MDE 表格以帮助读者判断结论强度？
3. 14B 结果能否获得第二个模型家族（如 DeepSeek-Coder-14B 或其他）的验证？
4. ±2pp SESOI 对应下游 repair@K 的预期影响量级是多少？

---

## Missing References

无重要遗漏。R2 建议 DreamPRM 和 CodePRM 在 Related Work 正文中增加具体讨论（当前仅在引用列表中），因其与本文 PRM 类比直接相关。

---

## External Review (Stanford Agentic Reviewer)

未请求（项目未启用 external_review）。

---

## Visual Layout Check（非评分项）

**状态：done**（2 warnings, 19 info）

- **Warning 1 (page 1-2)**：连续两页纯文本（Abstract + Introduction），首个 display item Figure 1 出现在第 3 页。审稿人前 2 分钟只看到文字墙，可能影响第一印象。建议将 Figure 1 提前或在 page 2 加入概览图/表。
- **Warning 2 (page 5)**：三个 display items（Table 1 + Figure 2 + Table 2）挤压在同一页，视觉密度偏高。建议将 Table 2 移至下一页。
- **Info**：全文排版整洁专业，booktabs 统一，无 margin 溢出或 LaTeX 渲染错误。主文 8 页含 6 个 display items（2 figures + 4 tables），密度适中。References 3 页格式统一，无未解析引用。正文 8 页合规，Limitations 约半栏合规。匿名性无违反。

---

## Overall Assessment

**综合评分：3.0 (Findings)**

**置信度：4/5**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3/5 | 2.5/5 | 2.5/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.5 | 3.0 | **3.0** |

**评分理由**：

论文在统计方法论和实验设计上达到很高水准，填补了 CLS/CWM/TRAJ 无匹配比较的文献空白。CLS-CWM function-level 等价性是有统计支撑的可信结论。Failure mode taxonomy 有独立实践价值。

三个核心限制将其定位在 Findings 水平：
1. **TRAJ 数据量混淆变量** (N1) 使论文三分之一的 formulation 比较缺乏充分因果推断基础。
2. **统计功效 ~0.3** (N2) 使多数比较停留在 inconclusive 状态，削弱了 "systematic comparison" 的信息量。
3. **14B 叙事过重** (N3) 在证据不足的情况下构建了过多推论框架。

贡献类型（empirical comparison, no new method）和 excitement 水平（2.5-3/5）限制了 main conference 竞争力。论文适合 Findings track——soundness 和 reproducibility 达标，方法论有参考价值。

**修复后潜力**：若作者 (a) 将 TRAJ 比较重新定位为 "formulation + data regime" 联合比较，(b) 对功效不足的比较使用 "inconclusive" 措辞，(c) 将 14B 从 abstract/conclusion 核心叙事降级为 exploratory observation，论文可达 **3.5 (Borderline Conference)**。

---

## Detailed Comments

### §1 Introduction
- Contribution 2 (error complementarity): <0.4pp heuristic gain 作为主要贡献权重过大。建议降级为 negative result + future work motivation。
- "first systematic comparison" 需加 scope 限定（≤8B LoRA, Python, SWE-bench）。
- Mechanistic pathway 解释（"operating through output format"）是 R16 的有效修复，本轮无新问题。

### §2 Method
- §2.1: TRAJ 定义后应立即说明其 data regime 与 CLS/CWM 的根本差异（175×），而非留到 §3.5。读者需要在理解 formulation 时就知道这个关键约束。
- §2.2 Expected Failure Modes: "format compliance collapse" 的归因应从 "formulation-inherent" 调整为 "observed under current training regime"，与 14B 收敛数据和 Limitations 的 hedging 保持一致。

### §3 Experiments
- §3.1 Statistics: 统计方法层次声明（TOST primary → bootstrap CI → ROPE robustness → regression mechanism）是 R16 的有效修复，结构清晰。
- §3.3 Scaling: "the gap narrows monotonically" 在仅 3 个 data points (4B, 8B, 14B) 上拟合 monotonic 趋势——df=0 的线性拟合不可靠，措辞应更审慎。
- §3.4 Equivalence: (a) "not confirmed" 改为 "inconclusive at current power"；(b) 增加 MDE 表格；(c) 功效分析从 Appendix 移至主文考虑。
- §3.5 Repo-Level: "format collapse is a structural bottleneck" 需加 "under ≤8B LoRA" 限定。Table 4 failure mode taxonomy 是有独立价值的贡献。
- Table 1: TRAJ 配置差异脚注应在正文中更显著呈现。
- Figure 2: caption 应标注 "y-axis does not start at zero"（与 Figure 3 统一）。

### §4 Related Work
- 覆盖全面，无重要遗漏。
- DreamPRM 和 CodePRM 建议在正文中增加具体讨论（当前仅引用）。
- GenRM domain-specific 对比（code ≠ math for generative verification）是有价值的 insight。

### §5 Conclusion
- "We presented the first systematic comparison" 需加范围限定。
- 14B 相关推论（capacity-dependent account, GenRM 桥接）应明确标注为 speculative。
- "three directions follow" 中 routing 方向需降低乐观程度（<0.4pp heuristic gain）。

### Limitations
- 长度和覆盖面合适（~半栏，3 个要点），符合 EMNLP 2026 规范。
- 建议增加对 mutation data 可能系统性偏向特定 formulation 的讨论。
- "Format-specific interventions (constrained decoding, output-format pretraining) may mitigate CWM format collapse but were not evaluated" 是好的披露。