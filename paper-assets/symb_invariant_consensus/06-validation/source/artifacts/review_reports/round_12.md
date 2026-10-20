---
round: 12
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T00:52:46.372005+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 15 (Fresh)

**论文**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning
**Venue**: EMNLP 2026 via ARR (May cycle)
**截止日期**: 2026-05-25
**审稿模式**: Fresh (2 Reviewers × 1 Round + 交叉分享)

---

## Summary

本文系统评估了 LLM 自提取符号约束（SICA pipeline: trace → FOL constraint extraction → Z3 MAX-SAT → scoring）能否突破 Self-Consistency (SC) 投票天花板。在 6 个开源模型（7B–32B）× 3 个逻辑推理数据集上的 3,000+ condition-evaluations 显示 SICA 未能显著超越 SC（aggregate sign test: 8+/7−, p=1.00; McNemar + BH 校正后无一显著）。作者将此归因于"Symbolic Confirmation Bias" (SCB)：自提取约束是模型分布先验的投射（BR 1.66–4.97×），shuffle 控制证实偏差具有结构性。论文贡献了三个诊断指标（K_eff, BR, C₀）和跨架构 NLI 验证的概念验证。

---

## Strengths

**S1. 评估规模出色**
3,000+ condition-evaluations 覆盖 6 个开源模型 + 5 个 frontier 跨模型提取、3 个核心逻辑推理数据集 + 3 个探索性数据集。27 种 training-free remediation 策略的穷举排查。在负面结果论文中属于罕见的覆盖度。[共识]

**S2. 多重收敛证据策略**
不依赖单一统计检验：符号检验 + McNemar + BH 校正 + Bootstrap 95% CIs + TOST 等价检验 + BR 机制分析 + ProcessSim 过程独立性 + Oracle 控制。这种三角验证方法论值得肯定。[共识]

**S3. Shuffle 控制设计精巧**
§5.2 打乱 constraint-answer 配对后 BR_shuf ≈ BR_orig (p > 0.17)，令人信服地证明偏差来自 trace-count 分布（结构性）而非提取质量本身。这是本文方法论上最亮眼的设计。[共识]

**S4. Oracle 控制精确定位问题**
Oracle SICA 在 Mistral-7B FOLIO 上 +29.90pp，证明约束聚合方法在获得高质量约束时有效，将问题精确定位到自提取环节而非 pipeline 本身。[R1 提出, R2 认可]

**S5. 诊断框架有泛化价值**
K_eff、BR、C₀ 三个指标定义清晰（Eq. 1-5），可直接应用于任何 trace-aggregation 方法的事前评估。C₀ 作为退化条件零成本检测器正确分类全部 60 个条件。[共识]

**S6. 附录极其详尽，可复现性优秀**
27 页中 18 页附录，覆盖 prompt 模板、Z3 伪代码、case study、oracle control、failure mode 分类、温度敏感性、多种子复现等。[共识]

---

## Weaknesses

### Must-Fix (影响接收决定)

**W1 [critical/major, 共识] 统计功效不足 vs "Fail to Improve" claim 强度**
全部 10 个非退化条件 observed power < 21%（Table 6, Appendix E），MDE 远大于观测效应量。Bootstrap 95% CIs 区间宽度达 ±1.5–2pp（Table 7），无法排除 ±1pp 级别的真实正效应。标题 "Fail to Improve" 表述为 evidence of absence，但实际证据仅支持 absence of evidence。R1 视为 critical，R2 视为 major（论文有 oracle/shuffle/SCB 机制等多重收敛证据部分缓解），两位均同意标题和 Abstract 需弱化措辞。

→ **建议**: 标题改为 "No Evidence That..." 或 "Limitations of..."；Abstract 增加 power caveat（"observed power < 21% for individual conditions; our conclusion rests on converging evidence across..."); 主文 §4.2 增加对功效局限性的显式讨论。

**W2 [major, 共识] SCB 概念独立性不足——与 CoT confirmation bias 机制同构**
SCB 的因果链（distributional prior → biased self-generated output → downstream confirmation）与 Wan et al. (ACL Findings 2025) 的 CoT confirmation bias 在机制层面同构。论文 §2 仅用一句话区分，未充分论证 SCB 作为独立概念的必要性。R1 交叉回应中同意此判断，但补充 SCB 的贡献在于量化该偏差在形式化验证管道中的具体表现（BR 1.66–4.97×）以及证明 Z3 solver 的 provable soundness 无法弥补 input 偏差。

→ **建议**: §2 或 §3.3 坦诚承认与 CoT confirmation bias 的机制同构性，将 SCB 定位为该现象在符号约束管道中的特例和实证深化，而非独立概念。

**W3 [major, 共识] 多种子复制极其有限**
仅 Mistral-7B（3 seeds, σ=±2.70pp）和 Qwen2.5-14B（4 seeds）进行了多种子复制。种子间方差已超过大多数观测效应量（|Δ| < 2pp），其余 4 个模型单种子运行。在种子方差未充分量化下报告精确 Δ 值有虚假精度之嫌。

→ **建议**: 至少再对 2 个模型补充 3-seed 复制；或在主文诚实讨论单种子结果的局限性，将 Δ 值呈现附带种子不确定性范围。

**W4 [major, 共识] §6 跨架构 NLI escape 证据偏薄，结论外推过度**
显著增益仅出现在 Mistral-7B（SC < 40%，最弱模型），4/6 main conditions 共享 DeBERTa 系列 verifier。§6 claim "generators up to SC ≈ 70%" 无数据支撑——实际验证仅覆盖 SC < 40%。Table 3 显示强生成器（Qwen2.5-14B, SC > 70%）无显著改善。

→ **建议**: claim 限定为 "works on weak generators (SC < 40%)"；"SC ≈ 70% 阈值" 改为 suggestive observation；§7 的实践建议相应弱化。

### Should-Fix (提升论文质量)

**W5 [major, 共识] K_eff 作为贡献的新颖性 overstated**
K_eff = K/[1+(K−1)·κ] 是 Kish (1965) effective sample size 的直接应用（论文自引 Kish 1965）。将其称为 "general diagnostic framework"（Contribution 2）夸大了方法论创新。R1 补充指出 Fleiss' κ→ICC 近似在高 prevalence 下受 paradox 影响（K_eff 偏高）。

→ **建议**: Contribution 2 重新定位为 "application of established diagnostics to LLM trace-aggregation evaluation"。

**W6 [major, 共识] Independence-accuracy trade-off 未与 ensemble learning bias-variance 文献建立联系**
§6 的权衡（独立但较弱的 verifier 引入更多 variance 但降低 correlated bias）是 ensemble learning 经典 bias-variance tradeoff。论文引用了 Krogh & Vedelsby (1994) 但未讨论对应关系。缺引 Lakshminarayanan et al. (2017) Deep Ensembles。

→ **建议**: §6 或 §7 显式建立与 ensemble diversity 文献的联系。

**W7 [major→部分共识] Symbolic Mirage Hypothesis 的 Predictions post-hoc 性质**
R1 认为 Predictions 1-2 均为事后构造；R2 部分反驳——P1（结构性独立验证打破 SCB）是 out-of-sample prediction（§6 用全新实验设计验证），P2（MAX-SAT ≈ count-only, 94.4%）确实是 SCB 假说的同义反复。

→ **建议**: P2 重定位为 "diagnostic observation"；P1 的 prediction 框架可保留；在 §3.3 明确标注 exploratory/post-hoc 性质。

**W8 [major, 共识] BR 指标存在部分循环论证——措辞混淆结构性局限与提取质量问题**
当多数答案错误时，更多 trace 产生错误答案 → 更多约束来自这些 trace → BR > 1 部分是 trace-count 不平衡的数学必然。Shuffle 控制实际确认了这一点（BR_real ≈ BR_shuf），但论文措辞时而暗示"提取质量"问题，时而作为"结构性局限"证据。两位 Reviewer 共识：核心论点成立（自提取约束不提供超越 trace 分布的独立信号），但需更精确区分 BR 的两个组成部分。

→ **建议**: 明确区分 (a) BR 中由 trace-count 不平衡导致的 trivial 分量 与 (b) 约束未能提供超越 trace 分布的独立信号（non-trivial 发现）。

**W9 [minor-major, 共识] Abstract 中 BR 1.66–4.97× 选择性报告**
仅给出 min-max 范围，未提供中位数或均值。4.97× 可能是单一异常值。定性结论（BR 全 > 1）不受影响，但数值呈现有 cherry-picking 之嫌。

→ **建议**: Abstract 报告中位数或 IQR 而非 min-max。

### Nice-to-Fix (次要改进)

**W10 [minor, 共识] §5.4 Remediation Analysis 缺共性失败机制解释**
R2 认为 ~15 行过薄；R1 部分反驳（Figure 2 + Table 14 在附录已够，8 页限制下取舍合理）。共识：需补充 1-2 句共性失败机制解释（如"所有 training-free 策略无法改变约束的分布来源"）。

**W11 [minor, 共识] "Symbolic Mirage" 与 "SCB" 术语关系模糊**
Abstract 用 SCB，§3.3 用 Symbolic Mirage Hypothesis，正文混用。建议明确：Symbolic Mirage Hypothesis 是理论假说，SCB 是该假说预测的可观测现象。

**W12 [minor, 共识] Related Work §2 讨论深度不足**
Wan et al. (2025) 与 SCB 的区分仅一句话；trained verifiers (PRM) 与 self-extracted constraints 的根本区别未讨论——前者引入 external training signal 打破自引用循环。

**W13 [minor, 共识] Spearman ρ=-1.0 (n=6) 用于 capability gap analysis 脆弱**
n=6 下完美负相关统计意义有限，任一排名互换 ρ 大幅下降。建议定位为 suggestive observation。

**W14 [minor, 分歧] §7 Discussion 过短 vs Appendix Z 补充**
R2 认为 §7 仅 ~1/3 页不足；R1 反驳称 Appendix Z（~2.5 页）覆盖了 neuro-symbolic 启示、test-time scaling、future directions。共识：在 §7 末尾加明确指引句。

**W15 [minor, 共识] α=0.5 敏感性分析结论过强**
Table 11 的 ≥99% agreement 是主效应接近零时的 ceiling effect，非真正鲁棒性。应加限定语。

---

## Reviewer Consensus [AGREE]

1. **标题和 Abstract 需弱化** — "Fail to Improve" overclaims given power < 21%; 应改为 "No Evidence" 或限定 MDE 范围 [R1-W1, R2 交叉 AGREE]
2. **SCB 应定位为 CoT confirmation bias 在 formal verification 的实例化** — 而非独立概念 [R2-W1, R1 交叉 AGREE]
3. **多种子复制不足** — 种子方差 ±2.70pp 超过多数效应量 [R1-W3, R2 交叉 AGREE]
4. **§6 escape 证据偏薄** — claim 应限定到 SC < 40% [R1-W5, R2 交叉 AGREE]
5. **K_eff 新颖性 overstated** — Kish (1965) 的直接应用 [R2-W2, R1 交叉 AGREE]
6. **Independence-accuracy trade-off = bias-variance** — 缺 ensemble 文献联系 [R2-W3, R1 交叉 AGREE]
7. **BR 措辞需精确化** — 区分 trivial (trace-count) 与 non-trivial (independence failure) 分量 [R1-W4, R2 交叉 AGREE with nuance]

## Reviewer Divergence [REBUT]

1. **W1 严重度**: R1 视为 critical，R2 视为 major（多重证据部分缓解频率主义功效不足）。Director 判定：**major-to-critical**——功效问题真实存在但论文的多重收敛策略部分缓解了对单一统计检验的依赖。
2. **§5.4 主文篇幅**: R2 认为过薄(major)，R1 认为大致合理但需补共性机制(minor)。Director 判定：**should-fix minor**——补 1-2 句解释即可。
3. **§7 Discussion 长度**: R2 认为过短(minor)，R1 反驳有 Appendix Z。Director 判定：**nice-to-fix**——加指引句。
4. **指标过载**: R2 认为 ProcessSim/CCR 可移附录(minor)，R1 反驳 ProcessSim 不可替代。Director 判定：**不作为缺陷**——当前安排合理。
5. **Predictions post-hoc**: R1 认为 P1-P2 均 post-hoc (major)，R2 认为 P1 是真 out-of-sample prediction。Director 判定：P2 需重定位为 observation；P1 可保留 prediction 框架。

---

## Questions for Authors

1. SCB 与 Wan et al. (2025) CoT confirmation bias 在机制层面的本质区别是什么？如果一个方法能减轻 CoT bias，是否预期也能减轻 SCB？
2. 鉴于 power < 21%，是否愿意将标题中的 "Fail" 修改为更审慎的表述（如 "No Evidence"）？
3. 种子间方差 ±2.70pp 超过多数效应量——其余 4 个模型的单种子结果有多少信心？
4. §6 claim "generators up to SC ≈ 70%" 的依据是什么？实际验证仅覆盖 SC < 40%。
5. BR > 1 在 SC 正确时是否也成立？如果是，这会改变 BR 的解释——说明约束普遍偏向多数答案而非特异性偏向错误答案。
6. 27 种 training-free remediation 策略中，是否有任何策略在 BH 校正前显示显著正效果？共同特征？

---

## Missing References

以下遗漏引用两位 Reviewer 均同意 [AGREE]：

1. **DuPO: Enabling Reliable LLM Self-Verification via Dual Preference Optimization** (ICLR 2026) — training-based self-verification，直接相关 §6 escape 和 §2 trained verifiers
2. **S²R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning** (2025) — RL-based self-verification，training-based escape 路径
3. **"A Reality Check of Language Models as Formalizers on Constraint Satisfaction Problems"** (arXiv 2505.13252, 2025) — LLM 形式化能力系统评估，直接互补约束提取质量讨论
4. **Lakshminarayanan et al. (2017) "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles"** — §6 independence-accuracy trade-off 的理论基础文献

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置中 external_review 未启用）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~4 分钟）。3 warnings, 13 info, 0 critical。

**Warnings:**
1. **Pages 1-2**: 前 2 页纯文本（Abstract + Introduction），无视觉锚点。第一个 display item（Figure 1）在 p3 顶部。建议考虑将 Figure 1 提前或加入 motivating example 小图。
2. **Page 8**: Figure 2（27 策略柱状图）x 轴标签非常小且密集，打印/缩放时可能难以辨认。建议增大字号或分组展示。
3. **Page 23**: Figure 7（capability gap 散点图）使用蓝-红连续色梯度，对红绿色盲不友好。建议改用 viridis/cividis 色图。

**Positive:**
- 无 margin 溢出、无 LaTeX 渲染错误、无未解析引用
- 所有表格使用 booktabs 风格，最优值加粗标注
- 主文 5 个 display items (2 figures + 3 tables)，分布合理
- 正文严格 8 页，Limitations 在 p9 顶部，格式完全合规

---

## Overall Assessment

### 维度打分（ACL ARR Review Form）

| 维度 | R1 | R2 | Director |
|------|----|----|----------|
| Soundness | 3/5 | 3.5/5 | **3/5** — pipeline 定义清晰、多重收敛策略得当，但 power < 21% 严重削弱核心 claim，BR 循环论证风险未充分讨论 |
| Excitement | 3/5 | 3/5 | **3/5** — 负面结果有社区价值，诊断框架可迁移，但概念创新有限（SCB ≈ CoT bias 实例化, K_eff = Kish 应用） |
| Reproducibility | — | 4/5 | **4/5** — 附录提供完整复现细节 |
| Confidence | 4/5 | 4/5 | **4/5** |

### Overall Assessment: **3.5 — Borderline Conference**

两位 Reviewer 独立给出 3.5，交叉分享后均维持。

**核心判断**: 这是一篇实验规模可观、统计控制严谨的实证研究，诊断框架（K_eff, BR, C₀）有实用泛化价值。但三项声称的概念贡献均有先验对应（SCB ↔ CoT confirmation bias, K_eff ↔ Kish 1965, independence-accuracy ↔ bias-variance），加之核心 claim "fail" 的强度超出了 power < 21% 的统计支撑，论文当前定位在 Conference 与 Findings 之间。

**接收路径**:
- 当前状态建议 **Findings** 接收
- 升至 Conference 需：(1) 弱化标题和 claim 措辞；(2) 坦诚 SCB 与 CoT bias 的同构性并重新定位贡献为 empirical；(3) 补充 2+ 模型多种子；(4) 限定 §6 escape claim 到 SC < 40%；(5) 建立与 ensemble diversity 文献的联系

---

*Report generated by Review Director (Round 15, Fresh mode). Reviewers: R1 (方法/实验/统计), R2 (新颖性/写作/格式). 1 round + cross-sharing. Convergence achieved on all key issues.*