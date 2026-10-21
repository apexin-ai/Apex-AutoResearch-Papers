---
round: 7
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T10:10:18.288094+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — "Mapping the Detectability Landscape of Iterative Model Collapse"

**Venue**: EMNLP 2026 (ARR June 2026) | **截止日期**: 2026-06-15
**Reviewer 编排**: 2 人（R1: 方法严谨性 / R2: 新颖性与完整性）
**审稿轮次**: Round 1（fresh review）| **交叉分享**: 完成，1 轮收敛

---

## Summary

本文系统研究了迭代模型训练中 model collapse 的可检测性。使用 Pythia-410M 作为主要架构，在 13 个污染水平（α=0.00 到 1.00）、5 种统计检测方法、multi-seed 复制条件下构建了 detection landscape。核心发现包括：(1) Permutation Granger causality (PermG) 在 α≈0.48 处呈现 sharp detection onset；(2) detection boundary α_c(T) 随观测长度 T 按幂律下降；(3) 5 种方法在相同数据上产生 0%-92% 的 FPR 差异；(4) entropy Granger-precedes diversity（14/15 实验确认），可作为 canary signal。跨架构验证覆盖 5 个 model families（345M-6.9B），15 个 model-seed 组合中 10 个确认 directional detection。

---

## Strengths

1. **实验规模和系统性**：13 个 contamination levels × 5 个 model families × multi-seed replication × 5 种统计方法的全组合覆盖，在 model collapse 文献中属最全面之列。[两位共识]

2. **统计处理严谨**：一致使用 BH-FDR 校正、permutation-based p-values、cluster-bootstrap CI。论文诚实报告了 5/15 non-confirming conditions 和所有 failure modes。[两位共识]

3. **Multi-method comparison 对领域有警示价值**：Table 1 展示的 5 种方法在相同数据上 FPR 从 0% 到 92% 的差异（κ=0.185），对 NLP 社区将计量经济学方法引入 collapse 检测是有建设性的。[两位共识]

4. **Cascade ordering 有实践指导意义**：entropy → diversity 的 ≥1-generation lag（14/15 验证）为 monitoring pipeline 的指标选择提供了理论基础和实证支持。[两位共识]

5. **附录完整性**：16 个附录提供了 specification curve、power analysis、Shapley values、CUSUM calibration 等大量补充分析。[R1]

---

## Weaknesses

### CRITICAL

**W-C1. PermG FPR=0% 声明在主文中具有误导性** [R1-N1, 两位共识 AGREE]

主文（Abstract, §4.1）反复声称 PermG null-control FPR=0% 且 95% CI=[0,0]。但 Appendix R 揭示 within-seed ICC=0.34，effective N≈7，cluster-adjusted 95% CI 实为 **[0%, 41%]**。MMCT 权重体系给 PermG 赋予 w=100（所有方法最高），正因其 "zero FPR" 特性。41% 的 CI 上界意味着这一独特性声明的统计基础极弱。在主文中报 [0,0] 而将 [0%,41%] 藏在附录中，构成对核心方法论声明的系统性低报。

**W-C2. Detection boundary 模型验证严重不足** [R1-N2, 两位共识 AGREE]

Proposition 3 的 α_c(T) = A·T^{−1/(2β)} 用 **2 个 T 值（T=10, T=20）训练 2 个参数（A, β）**，自由度为零——任何 2 参数模型都能完美拟合 2 个点。验证集仅 6 个 α-T 组合点（MAE=0.106），样本量极小。子线性信号模型 S(α) = c·α^β 的假设未经独立验证。Sigmoid steepness SE(k)≈k 说明函数形式不可靠确定。这是论文标题 "Mapping the Detectability Landscape" 的核心贡献，但验证力度不足以支撑 formal proposition 的定位。

**W-C3. Statistical power≈37% 无法支撑 sharp onset 声明** [R1-N3, 两位共识 AGREE]

T=10 时 PermG power≈37%，63% 假阴性率。观察到的 0/8→6/8 "sharp transition"（α=0.45→0.50）可完全用 power curve 在边界处的陡峭上升解释，不需要底层信号存在 phase transition。R2 补充：Figure 1 "Phase diagram" 实际上是 detection power 分布图而非信号相变图。论文需要明确区分 "detection power boundary"（方法的检测下界）和 "signal onset boundary"（信号真正出现的位置）。

**W-C4. Du & Tanaka-Ishii (2026) 引用三重错误** [R2-N1, R1 AGREE 需修正]

论文将 Du & Tanaka-Ishii (2026) 定位为 "closest predecessor"（§2），但存在三重错误：(1) PDF 中 arXiv ID 为 2605.00635（实际对应数学论文 Keimer & Pflug）；(2) 标题写 "generative regulation"（应为 "geometric regulation"）；(3) 更关键的是，Du & Tanaka-Ishii 研究的是 **mode collapse**（生成时文本重复），非 **model collapse**（迭代训练退化）——这是两个不同的研究问题。R1 核查 bib 源码显示 bib 文件可能已部分修正（标题写 "Mode Collapse"），但 PDF 编译使用了旧版。无论 bib 状态如何，将 mode collapse 工作定位为 model collapse 研究的 "closest predecessor" 是根本性误判。

**W-C5. 贡献定位不清——方法创新 vs. 系统应用边界模糊** [R2-N2, R1 部分 AGREE]

三项贡献均存在 framing 问题：贡献 1 "landscape characterization" 本质是 empirical benchmarking；贡献 2 Proposition 1 仅用 Jensen's inequality；贡献 3 "method sensitivity" 在计量经济学中是常识。论文应重定位为 "empirical study applying established econometric tools to a new domain"。R1 对此部分反驳：认为 Proposition 1 的形式化提供了可检验预测的价值，method sensitivity 对 NLP 社区有增量信息——但同意整体应重定位为 empirical study，Proposition 3 应降级为 empirical scaling observation。

### MAJOR

**W-M1. Cross-architecture "coupling preserved" 条件存在循环论证** [R1-W2, R2 强烈 AGREE]

15 个 model-seed 组合中 5 个 non-confirming（33%）。论文以 "when entropy-diversity coupling is preserved" 为条件限定结论，但该条件是事后根据检测结果判定的——检测成功→coupling 存在→方法有效；检测失败→coupling 不存在→不算失败。需要独立的预先判定标准（如 Pearson r > 0.8），在 null condition 下预先定义验证。

**W-M2. Intervention (§5.6) 统计力度严重不足** [R1-W3, 两位共识 AGREE]

仅 n=2 模型、α=1.0（最极端场景）、post-hoc 15% threshold、bootstrap CI 29-64%。无 α=0.50-0.75 区间的证据。即使定位为 proof-of-concept，n=2 的统计力度极弱。

**W-M3. 非单调 dip (α=0.60) fp32/bf16 翻转无机制解释** [R1-W1, 两位共识 AGREE]

0/8 (bf16, T≤20) vs 8/8 (fp32) 的完全翻转。"Precision mechanism" 假说无独立证据。如果数值精度变化导致 0%→100% 翻转，严重质疑方法的可移植性和实际可部署性。

**W-M4. Discussion §6 过于简短** [R2-W1, R1 AGREE]

§6 仅约 100 词，一段密集文字。对于 13 种 contamination levels、5 个 model families、5 种方法的系统研究，缺乏对 5/15 non-confirming 条件原因、ML pipeline 实际指导意义、detection boundary 理论含义的综合讨论。建议扩展至少 0.5 页。

**W-M5. 与 Schaeffer et al. (2025) "8 种 collapse 定义" 的关系讨论不充分** [R2-W2, R1 AGREE]

§2 仅一句引用。本文的 model collapse 操作性定义对应 Schaeffer 分类中的哪一族？Detection boundary 结论在所有定义下是否成立？需要明确映射。

**W-M6. "Methodological pitfalls" framing 有 straw-man 倾向** [R2-W3, R1 部分 REBUT]

R2 认为 first-differencing 消除共同趋势是设计目的而非 "pitfall"，method sensitivity 是常识。R1 反驳：具体到 model collapse 语境的实证发现（canary→perplexity 被消除但 canary→diversity 保留）对 NLP 社区有信息增量。**共识**：同意改 "pitfalls" 为 "design considerations"。

### MINOR

**W-m1. Seed sensitivity 在 boundary 处未充分量化** [R1-W4]

α_c=0.487±0.006 的 SE 暗示极高定位精度，但 T=10, α=0.50 处不同 seed 结果从 6/8 跳到 0/8。真实不确定性远大于报告值。

**W-m2. 数字一致性："13 contamination levels" vs "12 contamination levels"** [R2-W5, R1 REBUT]

R1 认为是含/不含 null 的计数约定差异。建议统一表述。

**W-m3. Figure 1 子图内文字偏小** [视觉审查]

Axis label、legend、tick label 在打印时可能接近可读下限。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上完全一致：

1. **FPR=0% CI 在主文中被低报**（W-C1）——需在主文报告 cluster-adjusted CI
2. **Detection boundary 验证不足**（W-C2）——2 个 T 值拟合 2 参数，自由度为零
3. **Power artifact 可能性**（W-C3）——sharp onset 可能是 power curve 效应
4. **Du & Tanaka-Ishii 引用错误**（W-C4）——mode ≠ model collapse
5. **整体应重定位为 empirical study**（W-C5 部分）
6. **Cross-architecture 循环论证**（W-M1）
7. **Intervention 证据不足**（W-M2）
8. **Discussion 过短**（W-M4）

## Reviewer Divergence [REBUT]

分歧仅存在于程度和措辞层面，不涉及核心结论：

1. **Proposition 1 的价值**：R2 认为 "trivial"（Jensen's inequality），R1 认为形式化提供了可检验预测的价值。共识：不应称为 "定理级" 贡献，但 "形式化观察" 有一定价值。
2. **Method sensitivity 对 NLP 的新颖性**：R2 认为是计量经济学常识，R1 认为对 NLP 社区有增量信息。共识：framing 应更谦逊——"引入已知最佳实践" 而非 "发现新现象"。
3. **"Pitfalls" 措辞**：R2 认为 straw-man，R1 认为在 NLP 语境下有信息增量。共识：改为 "design considerations"。
4. **13 vs 12 contamination levels**：R2 认为不一致，R1 认为计数约定差异。共识：统一表述即可。

---

## Questions

1. 如果在主文中报告 cluster-adjusted FPR CI [0%,41%] 而非 [0,0]，MMCT 的权重分配在 FPR=10% 假设下会如何变化？核心结论是否仍然成立？
2. Proposition 3 的 β=0.24 是否在不同 seed 或架构下稳定？能否报告 bootstrap CI？
3. 如何排除 "sharp onset"（0/8→6/8）是 power curve artifact 而非真实 phase transition？需要多大的 T 才能在 power=80% 下区分二者？
4. Cross-architecture validation 中 "entropy-diversity coupling" 能否用不依赖检测结果的独立度量预先判定？
5. Du & Tanaka-Ishii (2026) 研究的是 mode collapse 还是 model collapse？为何将其定位为 "closest predecessor"？
6. 本文的 model collapse 操作性定义对应 Schaeffer et al. (2025) 八种定义中的哪一种？

---

## Missing References

- **Du & Tanaka-Ishii (2026)**: 需更正 arXiv ID 和标题；重新评估其与本文的关系
- **Tank et al. (2021, IEEE TPAMI) / KAN-based Granger causality (arXiv:2501.08958)**: 非线性 Granger causality 方法应被讨论，说明为何在短序列设定下选择 PermG
- **arXiv:2509.16499**: "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective" [R2 建议]
- **Schick et al. (2024) Self-Play Fine-Tuning**: 合成数据训练中 quality 保持的条件 [R1 建议]

---

## External Review (Stanford Agentic Reviewer)

**状态：未返回**（已请求，pending）

外部审稿请求于 2026-05-22T09:49:21Z 发送，截至报告提交时尚未返回。如后续收到，将作为补充材料另行发送。

---

## Visual Layout Check（非评分项）

**状态：已完成** | 0 Critical, 2 Warning, 7 Info

关键发现：
- **[WARNING]** Pages 4-5 连续两页纯文本（§4 Method + §5.1 Setup），无 figure/table/equation display，审稿人可能失去注意力。建议将附录中某个关键结果表提前到正文。
- **[WARNING]** 主正文 8 页仅 4 个 display items（2 figures + 2 tables），对于覆盖 5 种方法、13 种 contamination 的实证论文偏少。大量实验结果被压入附录（~20 张表）。
- **[INFO]** Figure 1 子图内文字偏小（axis label、legend）。
- **[INFO]** Page 8 内容密度高但无溢出；页数合规（主体 8 页）。
- **[INFO]** Ethics Statement 和 AI Writing Disclosure 格式规范。无 [?] 未解析引用。

---

## Overall Assessment

**评分：3.0 (Findings)**
**置信度：4/5**

两位 Reviewer 独立评分均为 3.0，经交叉讨论后维持此评分不变。

**理由**：

论文选题重要——model collapse 的可检测性是一个实际相关且尚未被系统研究的问题。实验规模可观（185 个实验，15 model-seed combinations），统计处理在 accepted framework 内是严谨的。Multi-method comparison (Table 1, κ=0.185) 和 cascade ordering (14/15 验证) 对该领域有建设性贡献。

但存在五个结构性问题限制了主会接收：

1. **核心统计声明的可信度**：FPR=0% 在主文中报 CI [0,0] 而 cluster-adjusted CI [0%,41%] 仅在附录，这是系统性低报而非遗漏。
2. **Detection boundary 的验证力度**：2 个 T 值拟合 2 参数模型是数学上的 trivial fit，不是 validation。
3. **Power artifact 无法排除**：在 power≈37% 下，论文无法区分 "sharp signal onset" 和 "power curve effect"。
4. **引用可靠性**：最重要竞品引用存在 arXiv ID、标题、研究对象三重错误。
5. **贡献 framing 偏高**：实际是成熟统计工具的系统应用，但 framing 暗示理论贡献。

建议修正引用错误、在主文中诚实报告 FPR CI、重定位贡献为 empirical study、扩展 Discussion 后作为 **Findings** 提交。如能补充更多 T 值验证 detection boundary 并解决 power artifact 质疑，有提升至 3.5 (Borderline Conference) 的潜力。

---

## Detailed Comments

### Abstract
- 信息密度过高：β=0.24, γ=2.08, MAE=0.106, 0%-92% FPR 等大量数字影响首读可理解性
- "five model families" — 需核实与正文一致性
- FPR "0% to 92%" — 需注明 0% 为 cluster-adjusted CI [0%,41%]

### §1 Introduction
- 三项贡献的 framing 需调整：贡献 1 重定位为 empirical characterization；贡献 2 保留但降低 "formal" 语气；贡献 3 承认 method sensitivity 对 NLP 是新但对统计学不是
- "predict-then-verify at T=20 matches 3/5 predictions in saturated regimes" — 需明确 2/5 不匹配的含义

### §2 Related Work
- Du & Tanaka-Ishii (2026)：修正引用 + 重新评估 "closest predecessor" 定位
- Schaeffer et al. (2025)：需明确映射本文的 collapse 操作性定义到其 8 种分类

### §3 Cascade Ordering
- Proposition 1：数学工具（Jensen's inequality）简洁，但形式化的可检验预测有价值
- "optimal canary metric" 的措辞可能过强——仅在 entropy-diversity coupling 存在时成立

### §4 Method
- §4.1 "Methodological pitfalls" → 改为 "design considerations"
- PermG FPR：主文必须报告 cluster-adjusted CI [0%,41%]
- Proposition 3：降级为 empirical scaling observation；报告 β 的 bootstrap CI；增加 AIC/BIC 与替代模型的比较
- "Specification curve" 用语需替换为 "systematic robustness check" 或补充联合推断步骤

### §5 Experiments
- §5.2 "Sharp Detection Onset"：明确此为 detection power boundary，是否反映信号 phase transition 需更多证据
- §5.4 "Detection Boundary Left-Shift"：cross-T validation 的 6 个验证点不足以确认幂律形式
- §5.5 "Cross-Architecture"：需提供 entropy-diversity coupling 的独立预先判定标准
- §5.6 Intervention：至少 3 个 α 值 × 2 seeds，或标注 "anecdotal evidence"

### §6 Discussion
- 当前约 100 词，严重不足。需扩展讨论：5/15 non-confirming 原因、实际 ML pipeline 指导意义、detection boundary ≠ signal onset 的含义

### Limitations
- 长度和覆盖面适当（3 个核心限制）
- 可增加对 power artifact 可能性的讨论

### Ethics / AI Writing Disclosure
- 存在且内容适当

### 格式
- 8 页主体合规
- Double-blind 匿名性无明显泄露
- ACL review 模板正确