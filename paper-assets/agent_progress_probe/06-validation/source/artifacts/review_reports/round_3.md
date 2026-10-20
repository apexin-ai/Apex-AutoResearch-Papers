---
round: 3
overall_score: weak reject
timestamp: 2026-05-16T04:41:14.615814+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 5 Consolidated Review Report

**Paper**: "Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision"
**Venue**: EMNLP 2026 ARR (Main Conference Track)
**Deadline**: 2026-05-25
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 写作/格式 + Framing)

---

## Summary

本文提出弱监督方法论用于检测 LLM 编程 agent 的语义停滞：三个 labeling function 通过多数投票生成 205K+ 窗口的 silver labels，系统比较了 30 个结构特征、GRU probe、n-gram cycle detector 和 LLM-as-judge 在 zero-data 跨 agent 迁移与域内检测两种部署场景下的表现。核心发现是 deployment-regime trade-off：零数据时结构特征显著优于 probe 和 LLM judge，但 fine-tuning 后 probe 反超；五种 label model 均未超越多数投票。

---

## Strengths

**S1. 系统的实验设计和充分的消融**（R1-S2, R2-S1, 共识）
覆盖 6 种检测方法、3 种 encoder、3 种窗口大小、多种数据比例、gold set 验证、instance isolation、6-LF expansion 等。每个设计决策有实验支撑。跨 agent 转移实验设计清晰，instance isolation（Table A.4, Δ<0.1pp）排除任务重叠混淆。

**S2. Circularity 问题的坦诚处理**（R1-S3, R2-S2, 共识）
§4.2 开头标注 "Circular evaluation caveat"，§5.1 详细讨论三种打破循环的途径，Limitations 再次承认局限。这种透明度在实证论文中值得肯定。

**S3. 有价值的负面发现**（R1-S5, R2-S3, 共识）
五种 label model 在 3-LF regime 下全部失败，6-LF 扩展确认瓶颈在 LF 数量而非聚合方法。对弱监督实践者有直接指导价值。

**S4. 部署导向的 trade-off framing**（R1-S4, R2-S4, 共识）
清晰划分 zero-data vs fine-tuned 两种部署 regime 的方法选择，实用性强。

**S5. Cycle detector 对比提供 insight**（R1-S6）
Table 12 的 silver-gold inversion（cycle detector silver 0.721 < gold 0.841, structural silver 0.995 > gold 0.839）提供了理解两种评估框架差异的有价值分析。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [critical] 正文超过 8 页限制 — desk-reject 风险**（R2-W1, R1 AGREE）
§6 Conclusion 溢出约 4-5 行至 page 9（~8.1 页），违反 EMNLP 2026 ARR ≤8 页正文限制。Round 4 已标记此问题但未修复。这是 desk-reject 条件，必须在提交前解决。

压缩建议：(a) Introduction Finding 1-3 与 §4/§5 高度重复，可精简 ~0.3 页；(b) §5.3 Additional Analysis 可移入 Appendix 留交叉引用；(c) Conclusion 前四句与 Abstract 近乎逐字重复。

**W2 [critical] 16.8pp headline 比较基准不对等**（R2-W2, R1-W1, 共识）
16.8pp = cross-agent structural GB on OH (0.967) vs in-domain LLM 5-shot-CoT on SWE-Agent (0.799)。不同 dataset、不同 evaluation regime、不同 difficulty。§4.2 有限定语但 Abstract 无任何限定。R1 补充：跨 regime 减法在统计上无意义——不同 test set 上的 F1 之差不构成 effect size，"outperform...by 16.8pp" 暗示 paired comparison 但实际不可 pair。

关键缺失实验：LLM judge 在 OH 上的 cross-agent 评估（当前仅有 SWE-Agent in-domain）。

**W3 [critical] "evade repetition detectors" 动机与方法依赖矛盾**（R2-W3, R1 AGREE）
Abstract 以"逃避重复检测器"为核心动机，但实验证据表明方法的成功恰恰建立在重复信号之上：
- cmd_rep 特征贡献 cross-agent F1 的 40.6pp（Table A.10）
- LF-overlapping 11 特征 (0.977) **超过**完整 30 特征 (0.967)
- 19 个 residual features（真正"超越重复"的特征）崩溃至 0.566

R1 提供精确 reframe：论文的贡献在于用**更丰富的结构词汇**（fuzzy match ratios, edit distance, file operations）编码重复和停滞模式，而非检测"非重复性停滞"。R2 建议 Abstract 改为 "rich structural signals beyond simple n-gram repetition"。

**W4 [critical] 36.9pp headline scope mismatch**（R1-W1, R2-W4, 共识）
36.9pp = structural GB on all OH windows (N=150,652) vs probe on 15% test split (N=6,122)。两者 evaluation scope 不同。Table 1 footnote $^a$ 承认但 Abstract 不加限定。conf≥2 子集上 gap 缩小至 GB 0.992 vs fine-tuned probe 0.976 = 1.6pp。GB 在 probe 的 6K test split 上的结果未报告。

**W5 [critical] Gold set 统计功效不足**（R1-W2, R2 AGREE）
Gold set 是唯一非循环证据锚点，但存在多个统计问题：
- κ=0.39 基于仅 52 个 triple-annotated windows，95% CI ≈ [0.15, 0.63]——跨越 "slight" 到 "substantial"
- Silver-gold gap 12.8pp (GB silver 0.967 → gold 0.839) 无分解分析（按 confidence strata / trajectory position / agent type）
- Gold stagnation prevalence 未报告——stratified sampling 可能偏离自然分布 (21-28%)，影响 macro-F1 解读
- Probe 仅在 SWE-only subset (N≈335) 评估，无法与 structural 全集 (N=505) 直接比较

**W6 [critical] Circularity defense 逻辑缺口**（R1-W3, R2 AGREE）
Feature overlap ablation (§5.2) 实际上**强化**了 circularity 担忧：cross-agent transfer 完全依赖 LF-overlapping features (0.977)，residual features collapse (0.566)。这表明 cross-agent 验证的是 "LF 判断模式在 agent 间可迁移"，而非"模型学到了 LF 之外的停滞信号"。Finding 1 "features that generalize encode stagnation patterns beyond overt repetition" 容易误导——实际是超越 n-gram exact match，而非超越 LF signals。

### Should-Fix（影响评分）

**W7 [major] λ₃ 特权信号的 2-LF 版本缺 structural cross-agent 结果**（R1-W4, R2 AGREE）
λ₃ 需要 task outcome，仅离线可用。现有数据：移除 λ₃ feature 仅 -0.2pp（Table A.10），移除 λ₃ label 后 probe -7.7pp（Appendix §A.9）。但关键缺失：structural GB 在 2-LF (λ₁+λ₂) labels 训练后的 cross-agent transfer 结果。λ₃ 贡献 33.5% 的 conf≥2 labels，移除将显著缩小训练集。

**W8 [major] Headline comparisons 缺 paired significance tests**（R1-W5, R2 AGREE）
36.9pp 和 16.8pp 因 scope mismatch 不可 pair。43.7pp (structural vs cycle detector cross-agent) 未报告 significance test。部分改善：GB vs fine-tuned probe CI [1.11, 2.23]pp 已添加。解决 SCOPE-1 后才能做完整 paired tests。

**W9 [major] 新颖性有限——更适合 Findings track**（R2-W5, R1 AGREE with nuance）
四个技术组件（WS/GRU probe/structural features/LLM judge）均为已知方法。C1 (weak supervision methodology) 实质是 Snorkel data programming 的领域应用，方法论创新有限。C2/C3/C4 均为实验发现。核心贡献在 systematic empirical findings，更符合 Findings track 标准。

R1 Excitement: 3.5/5, R2 Excitement: 2/5. 分歧在于 deployment trade-off framing 的实用价值——R1 认为有参考价值，R2 认为不足以构成 main conference 标准。

**W10 [minor] Cross-agent transfer 仅单向验证**（R1-W6, R2 AGREE）
仅测试 SWE-Agent → OH。OH → SWE 反向、ACR third-agent (GB 0.608) 基本失败。Headline claim "uniquely enable zero-data cross-agent transfer" 基于单向 2-agent 实验。

**W11 [minor] 7 个 orphan bib entries**（R2-W6, R1 AGREE）
ACL 模板示例条目（APA:83, Aho:72, Ando2005, Chandra:81, Gusfield:97, andrew2007scalable, rasooli-tetrault-2015）未清除。R4 14→7，改善但未完成。

**W12 [minor] TLM Table A.8 caption 不清晰**（R2-W7, R1 AGREE）
MV 行 Conf≥2 F1 = 0.8946 实际是 downstream probe performance（footnote $^\ast$），与其他行含义不同。

**W13 [minor] 0.7512 vs 0.7514 值碰撞**（R2-W8, R1 AGREE）
已改 4 位小数但仍易混淆。

---

## Reviewer Consensus

两位 Reviewer 在所有 critical/major issues 上达成完全共识（全部 [AGREE]）：

1. **[AGREE] Headline numbers scope mismatch**：36.9pp 和 16.8pp 均不在 matched evaluation sets 上（R1-W1 = R2-W2 + R2-W4）
2. **[AGREE] Framing 矛盾**：方法依赖重复信号但 framing 声称超越重复检测（R1-W3 ≈ R2-W3）
3. **[AGREE] Gold set 统计功效**：κ=0.39 on N=52，CI 跨越 "slight" 到 "substantial"（R1-W2, R2 AGREE）
4. **[AGREE] Circularity defense 缺口**：feature overlap ablation 强化而非缓解 circularity 担忧（R1-W3, R2 AGREE）
5. **[AGREE] λ₃ 2-LF 实验缺失**：deployable 版本的关键数据缺失（R1-W4, R2 AGREE）
6. **[AGREE] Findings track 推荐**：方法论新颖性不足以支撑 main conference（R1 Overall 3.0, R2 Overall 2.5）
7. **[AGREE] 页数超限**：desk-reject 条件（R2-W1, R1 AGREE）

## Reviewer Divergence

**[REBUT] Circularity 讨论结构**（R1-W7 vs R2）
R1 认为 circularity 讨论散布 §3.3/§4.2/§5.1/§5.2/Limitations 五处不利于阅读。R2 轻微反驳：分布式结构符合 "先标注→后分析" 惯例，集中可能打断逻辑流。双方同意加 §5.1 交叉引用即可——minor issue，不影响评分。

**评分差异来源**（R1: 3.0 vs R2: 2.5）
R2 对 MOTIV-1（framing 矛盾）权重更高，认为是核心叙事的根基性缺陷。R1 更关注统计功效和缺失实验（可修复项）。R2 将 gold set 列为 Strength (S5)，R1 认为 gold set 存在统计功效不足问题，应进一步压低评分。

---

## Questions for Authors

**Q1.** Table 1 中 probe 的 "All" 和 "Conf≥2" 列均为 0.598——是否 probe 仅在其 test split 上评估而未按 conf 分层？如果是，应将 Conf≥2 列标注 "—" 或补充分层结果。

**Q2.** LF-overlapping 11 features (0.977) 超过 full 30 features (0.967)——19 个 residual features 引入 negative transfer。是否考虑 11-feature 配置作为推荐部署方案？

**Q3.** Gold set 中 stagnation 窗口占比是多少？stratified sampling 是否导致 prevalence 显著偏离自然分布 (21-28%)？

**Q4.** 2-LF (λ₁+λ₂) trained structural GB 在 OH cross-agent transfer 上的 macro-F1 是多少？

**Q5.** Silver-gold gap 12.8pp 中，哪些 confidence strata / trajectory position 的 gap 更大？

**Q6.** 16.8pp 是否有 apple-to-apple 替代数字？例如：在 OH 上运行 LLM cross-agent baseline，或使用 gold set 比较（GB 0.839 vs LLM 0.663 = 17.6pp, non-circular）。

**Q7.** 论文核心故事是否应从 "stagnation detection" 转向 "cross-agent transfer"？cycle detector 在 in-domain gold 上已匹配 structural GB (0.841 vs 0.839)。

**Q8.** C1 (weak supervision methodology for agent monitoring) 与 Snorkel data programming 在方法论上有何本质区别？

---

## Missing References

1. **Dawid & Skene (1979)** — 经典 label aggregation model（EM-based），Snorkel/data programming 的理论基础。§3.4/§4.7 讨论 label model 时应引用。（R1 提出，R2 AGREE）
2. **ProbGuard (2025)**: "Probabilistic Runtime Monitoring for LLM Agent Safety" — 如存在，与 agent monitoring 直接相关。（R2 提出，需作者验证）
3. **Agent Drift (2026)**: "Quantifying Behavioral Degradation in Multi-Agent LLM Systems" — 如存在，与 stagnation detection 高度相关。（R2 提出，需作者验证）
4. **Zhan et al. (2019)**: "Generating Multi-Agent Trajectories using Programmatic Weak Supervision" (ICLR) — 如存在，是 C1 claim 的直接先驱，需讨论与 C1 的关系。（R2 提出，R1 标注需验证）

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Overall Assessment

### 综合评分

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0/5 | 3.5/5 | 3.25/5 |
| Excitement | 3.5/5 | 2.0/5 | 2.75/5 |
| Reproducibility | 3.5/5 | 4.0/5 | 3.75/5 |
| Overall | 3.0/5 | 2.5/5 | **2.75/5** |

### 总评

**Overall: Weak Reject (for main conference)**
**Confidence: 4/5**

论文是一项扎实的系统性实证研究，实验覆盖面广、circularity 处理坦诚、负面发现有信息价值。但存在以下阻碍 main conference 接收的问题：

1. **正文超页**（desk-reject 条件，必须修复）
2. **两个 headline numbers 的比较基准不对等**（36.9pp scope mismatch + 16.8pp cross-regime comparison），Abstract 呈现方式构成 overclaim
3. **核心动机叙事与实验证据矛盾**（"evade repetition detectors" vs 方法对 repetition signal 的 40.6pp 依赖）
4. **Gold set 作为唯一非循环锚点统计功效不足**（κ CI 极宽，silver-gold gap 未分析）
5. **方法论新颖性不足**——已知技术的组合应用

**推荐**：修复 framing 问题（W2/W3/W4）和页数超限（W1）后，投 **EMNLP 2026 Findings track**。如坚持 main conference，需补充关键实验（2-LF structural cross-agent, LLM cross-agent on OH, OH→SWE reverse transfer）并提供方法论层面的创新贡献。

### Round 5 vs Round 4 变化总结

**Round 4 遗留问题状态**：
- Critical issues: 7 个 open/in_progress → **0 resolved, 0 improved on substance, 7 unchanged**
- Warning issues: 5 个 → **0 resolved, 2 improved (FMT-3 14→7, COLLISION-1 4位小数), 3 unchanged**
- 新增 issues: TRANSFER-1 (单向 transfer), REF-1 (missing references)

论文在 Round 4→5 期间无实质性修改，所有 critical issues 持续存在。

---

## Detailed Comments

### §1 Introduction
- Finding 1-3 的描述与 §4/§5 的结果叙述高度重复，建议精简（同时缓解页数问题）
- Finding 1 末句 "features that generalize encode stagnation patterns beyond overt repetition" 应修正为更精确的表述，区分 "beyond n-gram exact match" 和 "beyond LF signals"

### §3 Method
- §3.3 Structural Features 末尾的 circularity 提示可加 forward reference 至 §5.1

### §4 Experiments
- §4.2: "comparing the harder cross-agent setting against the LLM's easier in-domain regime" 的限定语应传播至 Abstract
- Table 1: 需补充 (a) GB 在 probe 的 6K test split 上的结果；(b) 2-LF trained structural GB 的 cross-agent 结果；(c) Probe Conf≥2 列应标注 "—" 或补充分层结果
- §4.8: Gold set stagnation prevalence 应明确报告

### §5 Analysis
- §5.1 开头加交叉引用句
- §5.2: 应明确讨论 LF-overlap features (0.977) > full features (0.967) 的含义——residual features 引入 negative transfer，cross-agent transfer 的成功完全依赖 LF-aligned features
- §5.3: 考虑移入 Appendix 以缓解页数

### §6 Conclusion
- 前四句与 Abstract 重复，需压缩
- Cross-agent transfer claim 应降级以反映单向验证 + third-agent 失败

### Abstract
- 第 2 行 "evade repetition detectors" → 改为 "beyond simple n-gram repetition" 或类似精确表述
- 36.9pp 和 16.8pp 应加明确限定条件，或替换为 matched-scope numbers

### References
- 移除 7 个 ACL 模板 orphan 条目
- 补充 Dawid & Skene (1979)
- 验证并考虑补充 ProbGuard, Agent Drift, Zhan et al.