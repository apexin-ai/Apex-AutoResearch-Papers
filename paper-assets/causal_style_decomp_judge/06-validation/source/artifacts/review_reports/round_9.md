---
round: 9
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-22T16:52:46.317974+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 11 (Fresh Review)

**论文**: *The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition*
**Venue**: EMNLP 2026 via ARR (May cycle)
**审稿模式**: Fresh（两位 Reviewer 独立初审 + 交叉回应）
**Reviewer 编排**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 写作完整性 + 格式合规）

---

## Summary

论文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated style rewriting + pairwise comparison 检测 LLM judge 中被 Likert 量表遗漏的风格偏差（"Likert Blindspot"）。在 4 个 judge（Qwen3-32B, GPT-4o, Llama-70B, Gemini-2.5-Flash）× 3 个风格轴（formality, verbosity, register）上验证，GEE decomposition 区分了 style-dominated（verbosity）与 conditionally style-driven（formality）轴。统计框架完整（BT + GEE + Holm-Bonferroni + TOST + Bootstrap），控制设计多层（NLI gate, position swap, negative control, rewriter independence test）。然而，核心发现本质上是心理测量学经典结论的 domain transfer，且 detection 与 amplification 无法干净分离，削弱了"Likert 是盲区"这一叙事的说服力。

---

## Strengths

1. **统计框架罕见完整**：BT + GEE conditional decomposition + Holm-Bonferroni + TOST equivalence + Bootstrap attenuation + 7-method sensitivity analysis 的组合在 NLP 评估论文中极少见，体现了认真的统计思考。（R1, R2 共识）
2. **GEE per-axis decomposition 有真正方法论贡献**：将 verbosity 识别为 style-dominated、formality 为 conditionally style-driven，超越简单的 "有偏差/无偏差" 二分法。这是论文最扎实的独立贡献。（R1, R2 共识）
3. **多层控制设计**：NLI quality gate + position swap + direction-aware gating + Claude Sonnet 4 negative control + rewriter independence test + 同风格 double-rewrite control，整体设计优于大部分同类工作。（R1, R2 共识）
4. **跨 judge 覆盖面**：4 个独立架构的 judge（含开源和闭源）独立复现 Blindspot，增强了结论的 generalizability。（R1）
5. **Appendix 深度令人印象深刻**：17 个附录（A-R）覆盖了几乎所有可预见的 robustness concern。（R1）
6. **诚实讨论 Comparative Trap 和 alternative interpretation**：§5.4 讨论了 detection vs. amplification 的歧义，Limitations 全面且自我批判。（R2）
7. **CSD 作为 black-box framework 有即时实用性**：evaluation practitioners 可直接应用于检测自己 judge 的风格偏差。（R2）

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, R2-N1 + R1 AGREE] **新颖性定位过度——核心发现有深厚心理测量学先例**

Pairwise 优于 Likert 在灵敏度上的优势是 Thurstone (1927) Law of Comparative Judgment 的经典结论，Mohammad (2017) 和 Novikova et al. (2018) 已在 NLG 评估中实证验证。论文虽引用了这些工作，但叙事将已知现象包装为新发现：
- 标题 "Detecting **Hidden** Style Bias" 暗示首次揭示
- §2 "first controlled quantification" 的 scope 不够限定
- Abstract 和 Conclusion 中 "reveals"/"systematically misses" 措辞过强

**两位 Reviewer 共识**：论文真正的新颖贡献是 CSD 框架 + GEE per-axis decomposition，而非 "Likert Blindspot" 现象本身。建议 reframe 为 "在 LLM judge 场景下首次系统量化已知的 measurement-format sensitivity gap"，并将 per-axis confound taxonomy 提升为 co-equal contribution。

**MF2** [critical, R2-N2 + R1-N3 + 交叉共识] **Detection vs. Amplification 无法分离——论文最根本的解读困境**

§5.4 六项控制 bound 了 amplification 但未 eliminate：
- 缺乏独立于两种测量格式的 **ground-truth bias measure**——没有 ground truth，就无法区分 (A) Likert attenuation vs. (B) pairwise amplification
- 100-point continuous Likert（Appendix M）排除了 scale granularity 解释，但 R1 指出这实际上 **支持** construct divergence 解读——如果问题不在粒度，更可能是 absolute vs. relative measurement 的根本差异
- Likert ATE 达到 80% power 需 n=336-1200+（Appendix L），当前 n≈88 的 Likert null 结果可能仅反映 power 不足而非方法论缺陷
- Bootstrap attenuation δ̄ ≈ -0.017（Appendix J）的 CI 包含 0（R2 确认），不能排除无 attenuation

**两位 Reviewer 共识**：§6 开头 "Likert scoring systematically misses style biases" 直接预设了解读 A，hedging 不充分。如果 amplification 解读成立，论文标题和核心 claim 需根本重构。建议：(1) 设计 ground-truth bias 已知的合成实验，或 (2) 诚实 reframe 为 "divergent signals" 而非单方面归因为 Likert failure。

**MF3** [critical→warning, R1-N2, R2 降级] **NLI Quality Gate 选择偏差未充分量化**

- 50 对人工标注偏少（Wilson CI 下界 86.3%），未报告 recall/FNR
- Gate 过滤 12-35% 配对，被过滤配对的风格分布和特征未分析
- Appendix N ablation（NLI-fail 样本）样本量太小（n≈12-21）

**分歧记录**：R1 定为 critical Must-Fix；R2 交叉降为 Should-Fix，理由是 Appendix E threshold sweep（11 阈值 × 44 组合全显著，BT 变化 ≤4pp）提供了部分缓解。
**Director 判断**：threshold sweep 缓解了结果对特定阈值的依赖，但未解决 selection bias 的方向性问题。定为 **高优 Should-Fix**。

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, R1-W1 + R2 AGREE] **TOST 等价边界 Δ=15pp 缺乏严格论证**

用自己观测到的效应量定义等价边界是循环论证。15pp ≈ d=0.43 属 medium effect，偏宽松。若 Δ=5pp 或 10pp，等价结论可能不成立。需基于领域先验（如 leaderboard 排名影响）论证，或报告 Δ=5/10/15/20pp 的 sensitivity。

**SF2** [warning, R1-N3 + R2-W2 共识] **样本量限制 Likert null 的解读**

主实验 LLMBar n=100（gate 后 ≈88），GEE 等深度分析仅在此 benchmark。n=355 scaled replication 部分弥补但 Likert 仍 n.s.。Conclusion "systematically misses" 需加 hedge——不能排除 power 不足解释。

**SF3** [warning, R1-W3 + R2-Minor-3 共识] **因果术语与方法论强度不匹配**

"Controlled Style Decomposition"/"interventional"/Figure 2 DAG notation 整体给人因果推断研究的印象。实际上 rewriting 非真正随机干预，NLI gate 非 do-operator，GEE 是关联分析。需更早声明 "controlled = experimentally controlled rewriting, not formal causal identification"。

**SF4** [warning, R1-W2 + R2-W4 共识] **Evaluator-producer confound 控制实验覆盖不完整**

Appendix D 覆盖 formality + verbosity 两轴（R2 更正 R1 原始描述），但 **register 轴完全未做 rewriter independence test**。Register 在 Table 1/3 中与其他轴同等呈现，需显式 caveat。22% Style OR 下降不可忽略。

**SF5** [warning, R2-W3 + R1 AGREE] **标题和叙事预设 pairwise 为 ground truth**

"The Likert Blindspot" 暗示 Likert 有缺陷，但 "pairwise measures relative preference, Likert measures absolute quality" 的 construct 差异同样合理。标题应更中性。

**SF6** [warning, R2-W1 + R1 AGREE] **Abstract 信息密度过高**

数字堆砌（d→0, n=355, p<0.01, 60%, OR 68×11 等）影响可读性。建议保留 1-2 个最有力数字，其余移至正文。

**SF7** [warning, R1-W4 + R2 AGREE] **负控制仅 Claude Sonnet 4 一个模型**

不足以论证 Blindspot 是特定架构/训练方式的产物。未讨论 Claude 为何不受影响的机制假设。

### Minor（不影响接收）

- **M1**: n=355 replication 讨论分散在 §5.1, Appendix J, K 多处，不易追踪（R1）
- **M2**: Appendix Q Holm-Bonferroni 8-test family 未包含 cross-benchmark tests（R1）
- **M3**: Register axis 的 n 值和 power 未明确报告，读者可能误解为 "register 无偏差" 而非 "power 不足"（R1）
- **M4**: Limitations 中 tone 轴实验的 pass rate 数字可移至 Appendix（R2 提出，R1 反驳认为一个数字不构成 excessive content——**分歧记录**）

---

## Reviewer Consensus

以下问题两位 Reviewer 达成明确共识（交叉标注 [AGREE]）：

1. **Detection vs. amplification 不可分离**是论文最根本的解读困境（MF2）
2. **新颖性定位过度**——CSD 框架和 GEE decomposition 是真正贡献，但被 "Blindspot" 命名遮蔽（MF1）
3. **因果术语偏强**需校准（SF3）
4. **Register 轴 evaluator-producer 控制缺失**（SF4）
5. **TOST Δ=15pp 需先验论证**（SF1）
6. **Abstract 密度过高**（SF6）
7. **负控制单一**（SF7）

## Reviewer Divergence

| 问题 | R1 定级 | R2 定级 | 核心分歧 |
|------|---------|---------|----------|
| BT IIA 假设未检验 | Must-Fix (critical) | Should-Fix (warning) | R2 认为 binary-choice BT 中 IIA 自动满足（无 irrelevant alternative 可删除），且 Table 2 五种非参数方法独立确认 Blindspot；R1 认为同源文本重复出现 + Appendix B direction asymmetry 仍构成风险 |
| NLI gate 选择偏差 | Must-Fix (critical) | Should-Fix (warning) | R2 认为 threshold sweep（11阈值×44组合，BT变化≤4pp）提供充分缓解；R1 认为 sweep 未解决 selection bias 的方向性问题 |

**Director 判断**：
- BT IIA：R2 的技术论证更有说服力——在 binary forced choice 中 IIA 确实自动成立，且多种非参数方法一致。但 R1 关于 direction asymmetry 的观察值得在 Discussion 中补充解释。**定为 Should-Fix**。
- NLI gate：两方各有理据。Threshold sweep 缓解了阈值依赖，但 selection bias 方向性分析仍缺。**定为高优 Should-Fix**（介于 MF 和 SF 之间）。

---

## Questions（需要作者澄清）

1. 能否设计 ground-truth bias 幅度已知的合成实验，独立验证 Likert 和 pairwise 的 sensitivity curve？（R2-Q1, R1 AGREE）
2. 100-point continuous Likert 仍未检测到 bias——作者是否认为这支持 absolute vs. relative evaluation 是根本区分？（R2-Q2, R1 AGREE）
3. Rewriter independence test 中 Style OR 下降 22% 如何解读——是 rewriter artifact 还是 transformation 强度差异？（R2-Q3, R1 AGREE）
4. 是否考虑 human annotators 在 CSD pairs 上同时做 Likert + pairwise 评估？（R2-Q4, R1 AGREE）
5. 50 对人工标注中 gate-rejected 配对的 false negative 数据是否已收集？（R1-Q2）
6. AlpacaEval/MT-Bench 的 per-judge per-axis 完整结果在哪个 Appendix？（R1-Q4）
7. Bootstrap attenuation δ̄ ≈ -0.017 的 CI 包含 0（R2 确认）——如何解读这一结果？（R1-Q5）

---

## Missing References

1. **Bojar et al. (2016)** 或 WMT human evaluation 工作——大规模 pairwise vs. rating 方法比较的重要先例（R1 提出, R2 AGREE）
2. **Karpinska et al. (2021)** 或类似 scale design 影响的研究（R1 提出）

---

## External Review

**外部审稿（Stanford Agentic Reviewer）**：未配置，跳过。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 1 warning, 14 info）。

**Warning**:
- Figure 1（CSD pipeline overview, p.2）中各阶段缩略图标非常小，在正常阅读距离下细节难以辨认。作为全文第一个 display item，建议放大或简化图标。

**Info highlights**:
- 首页无 display item，Figure 1 在 p.2 顶部。方法论论文可接受，但若能提至 p.1 底部锚定更快。
- Figure 1 caption 缺少各阶段功能概述，self-containment 可改进。
- Figure 2（DAG）紧凑清晰，质量好。
- 主体 8 页含 4 figures + 3 tables = 7 个 display items，密度健康。
- 色彩方案保守，打印友好且色盲安全。
- 未发现 LaTeX 渲染错误、margin 溢出或未解析引用。
- Appendix 区域表格密度高，建议部分关键 ablation 结果可视化。

---

## Overall Assessment

**评分**: 3.5 — Borderline Conference（EMNLP 2026 ARR 评分标准）

**置信度**: 4/5（两位 Reviewer 均仔细审查正文和全部 Appendix，熟悉 LLM-as-judge 和 measurement theory 文献）

**详细评价**:

论文在方法论执行上属于高质量工作：CSD 框架设计精巧，统计框架完整且罕见严谨，GEE per-axis decomposition 提供了超越简单 bias detection 的结构性洞察，17 个附录覆盖了几乎所有可预见的 robustness concern。控制设计（NLI gate + negative control + rewriter independence + position swap）构成了可信的多层验证链。

然而，两个根本性问题限制了论文的 Conference-level 接收可能性：

1. **新颖性**：核心 observation（pairwise 比 Likert 更灵敏）有深厚心理测量学先例（Thurstone 1927），论文叙事将 domain transfer 包装为新发现。真正的方法论贡献（CSD + GEE decomposition）被 "Blindspot" 命名所遮蔽。
2. **解读歧义**：在缺乏 ground-truth bias measure 的情况下，detection vs. amplification 无法干净分离。论文的六项控制 bound 了 amplification 但未 eliminate 它，而 Conclusion 的 hedging 不充分。

**路径建议**（不代表修改指导，仅作评审判断的背景说明）：
- 以当前形态更适合 **Findings** track
- 若能 (a) 诚实 reframe novelty、(b) 补充 amplification-bounding evidence（如合成实验或更大样本量验证）、(c) 在标题和 Conclusion 中保留足够 hedging，可达 **Conference** 水平

---

## Detailed Comments（按 Section）

### Abstract
- 信息密度过高，数字堆砌影响首次阅读体验。保留最核心的 1-2 个数字即可。（SF6）

### §1 Introduction
- "Detecting Hidden Style Bias" 的叙事框架预设 pairwise 为 ground truth。（SF5）
- Contribution list 与实际证据强度匹配度待提升——将 per-axis confound taxonomy 提升为 co-equal contribution。（MF1）

### §2 Related Work
- Thurstone (1927)、Mohammad (2017)、Novikova et al. (2018) 已引用但讨论不充分——需更明确 acknowledge 本文在哪个维度上 extend 已有结论。（MF1）
- 缺 Bojar et al. (2016) WMT human evaluation 先例。

### §3 Method
- "Controlled"/"interventional" 术语需更早声明不等于 formal causal identification。（SF3）
- Figure 2 DAG notation 与 §5 disclaimer 之间有张力。（SF3）
- NLI gate 的 recall/FNR 未报告。（MF3）

### §4 Results
- Table 1 register 轴结果需加显式 caveat（无 rewriter independence test）。（SF4）
- BT IIA 可在 Discussion 中补充 direction asymmetry 的解释。（Divergence issue）

### §5 Analysis
- §5.1 measurement attenuation vs. construct divergence 讨论是论文最重要的自我审视，但 framing 偏向 attenuation。（MF2）
- §5.4 六项 amplification controls 是 solid 的贡献，但 "bound ≠ eliminate" 需更显式。（MF2）
- TOST Δ=15pp 需先验论证或 sensitivity analysis。（SF1）

### §6 Conclusion
- "Likert scoring systematically misses style biases" 直接预设解读 A，hedging 不充分。（MF2）

### Limitations
- 全面且自我批判，是论文的优势之一。
- Tone 轴 pass rate 数字不构成 "excessive content"——R1 反驳 R2 的移除建议，Director 同意 R1。

### 格式合规
- 正文 ≤8 页 ✓
- 匿名性 ✓（`\author{Anonymous}`）
- Limitations 无新实验/图表 ✓
- 引用格式 ACL 规范 ✓
- Double-blind ✓