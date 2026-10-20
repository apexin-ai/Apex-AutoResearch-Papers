---
round: 2
overall_score: borderline reject
timestamp: 2026-05-15T13:34:17.562590+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4 (Fresh Review)

**论文**: "Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision"
**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)
**审稿日期**: 2026-05-15
**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+格式合规）
**轮次**: Round 1 独立审稿 → 交叉分享 → 共识收敛（1 轮完成）

---

## Summary

本文研究 LLM coding agent 的进度停滞检测，提出基于弱监督的方法论：3 个标注函数 (cmd_rep, file_diff, outcome_bp) 通过多数投票生成 205K+ 窗口的银标签，在此基础上系统比较 30 个结构特征、GRU 神经探针和 LLM-as-judge baseline。论文报告了部署场景 trade-off——零数据跨 agent 迁移中结构特征优于探针 36.9pp 和 LLM 16.8pp，但目标域微调后探针反超。同时报告了 5 个时序标注模型均不优于多数投票的负面发现。金标注集 (N=505, 3 annotators, κ=0.39) 提供部分非循环验证。

---

## Strengths

**S1. 方法论透明度高** [R1, R2 共识]
论文在 §4 开篇即明确承认 in-domain 0.995 是 LF 重构性而非真实检测能力，并通过三种方式尝试打破循环（cross-agent, instance isolation, gold set）。这种诚实度在 ML 论文中少见。

**S2. 实验覆盖全面、统计严谨** [R1, R2 共识]
多维度 ablation 设计完整：encoder ablation (3 backbone)、window size ablation (k=3/5/7)、data scaling curve、multi-seed stability (5 seeds)、instance isolation (284 shared tasks)、feature overlap ablation (11 vs 19 vs 30)、prevalence-matched cmd_rep ablation。关键对比有 paired bootstrap 和 McNemar 检验。

**S3. 实用导向的 deployment trade-off framing** [R1, R2 共识]
从 "structural dominates" 的 overclaiming 演进为清晰的部署场景分析：零数据用结构特征（<5ms, no GPU），有标注预算用探针微调。这为实践者提供了明确的决策框架。

**S4. Instance isolation 实验设计精到** [R1]
移除 284 个 SWE-bench/OH 共享任务后 cross-agent F1 变化 <0.1pp (Table 7)，有效排除 instance memorization 假说。

**S5. cmd_rep 的 coverage vs precision 分析** [R1]
high-precision low-recall LF 的核心价值是扩大训练数据量（4K→43K windows, ~10×）而非修正标签——对弱监督实践者有指导意义。

**S6. LLM-as-Judge 全面评估** [R1, R2 共识]
Table 8 包含 6 种配置（zero-shot, CoT, few-shot, 5-shot-CoT, GPT-5.5, structural augmentation），报告了 GPT-5.5 22.4% parse failure rate 和 structural input 反而降低 LLM 性能的反直觉发现。

---

## Weaknesses

### Critical Issues（影响接收决定）

**C1. Headline 16.8pp 跨数据集/跨难度比较** [R1-N1 + R2-N2, 全票共识]
Abstract 核心数字 "cross-coding-agent structural 0.967 vs best LLM 0.799 (16.8pp)" 对比的是：
- 0.967: GB 在 OH 上的 cross-agent 零样本迁移（更难的设置）
- 0.799: Claude 5-shot-CoT 在 SWE-Agent 上的 in-domain 评估（更容易的设置）

这是不同数据集、不同评估难度的对比。§4.2 承认了设置差异但 Abstract/Introduction/Conclusion 均未加任何限定。LLM 从未在 OH 上评估。16.8pp 作为核心 selling point 反复出现，读者会默认为同条件对比。

**C2. Headline 36.9pp 评估范围不一致** [R1-N2 + R2 AGREE, 全票共识]
Table 1 中 structural GB 在全部 150,652 OH windows 上评估 (0.967)，而 ProgressProbe 零样本在 15% test split (N=6,122) 上评估 (0.598)。36.9pp = 不同 N、不同 scope 的差值。Probe 只在 6K 子集评估的原因是 OH embeddings 未完整计算——这是评估基础设施缺陷。Table 1 脚注标注了差异但 Abstract 未作限定。

**C3. Gold set 验证力度不足** [R1-N3 + R2-W1, 全票共识]
Gold set 是打破循环评估的关键证据，但存在多重局限：
- (a) Fleiss' κ=0.39 仅 "fair agreement"，二分类 chance-corrected agreement 低，反映标注者对 "stagnation" 定义严重不一致
- (b) IAA 基于仅 52 个 three-annotator windows (Set A)，统计功效极低
- (c) Probe 在 gold set 上只在 SWE-only subset (N≈335) 评估，cross-agent 迁移的核心 claim 在 gold set 上缺乏验证
- (d) GB gold F1=0.839 vs silver 0.967——12.8pp gap 未被分析（来源不明：LF 系统偏差还是标注遗漏？）
- (e) Gold set stagnation prevalence 未报告，无法验证 corrected silver 21.4% 是否与人类判断一致

**C4. λ₃ 特权信号——headline numbers 基于不可部署配置** [R1-N4 + R2-W5, 全票共识（R2 有 nuance）]
λ₃ (outcome_bp) 使用推理时不可用的 task outcome，贡献 33.5% conf≥2 标签。所有 headline numbers (0.967 cross-agent, 0.995 in-domain) 基于 3-LF 配置。主表缺少 2-LF (λ₁+λ₂) 的 structural cross-agent transfer 结果。论文卖点是 "<5ms, no GPU" 实时监控，但 headline 性能基于需要 task outcome 的配置。R2 指出 λ₃ never flips MV（仅扩展 coverage），但 33.5% coverage 减少意味着 2-LF 训练数据量少 1/3，downstream 性能必然受影响。

**C5. 正文超出 8 页限制** [R2-N1 + R1 AGREE, 全票共识]
§6 Conclusion 起始于第 8 页底部，延伸至第 9 页上部（含 Reproducibility 段落）。EMNLP 正文限制 ≤8 页。超出约 0.3-0.5 页。**Desk reject 风险**。

**C6. 新颖性不足以支撑 main conference** [R2-N3, R1 部分同意]
四个 contributions 均为已有技术的组合/应用：
- C1 (WS methodology): Data Programming 直接应用（R1 认为 LF 设计有部分新意）
- C2 (Label quality as bottleneck): 本质是工程 debugging（R1 认为有 generalizable insight）
- C3 (Label model negative finding): 3 LF 不足以让复杂聚合超过 MV——理论可预见
- C4 (Deployment trade-off): 结构特征 zero-data 优于学习表示是 domain adaptation 已知规律

两位 Reviewer 均认为论文达到 Findings 水准但不足以进 main conference。R1 援引 ARR H6/H7 guidelines 认为负面发现和方法简单性不应作为 reject 理由，但同意整体新颖性有限。

### Should-Fix Issues（影响评分但不一票否决）

**W1. "语义停滞" motivation 与 cmd_rep 依赖性矛盾** [R2-W2, R1 强烈同意]
Abstract 声称检测 "evade repetition detectors" 的语义停滞，但 Table 9 显示移除 cmd_rep features 导致 cross-agent F1 下降 40.6pp。方法的成功严重依赖命令重复信号——恰恰是论文声称要超越的。"evade repetition detectors" 措辞过强。

**W2. Feature overlap 解读争议** [R1-W1, R2 REBUT]
11 个 LF-overlap features (0.977) > full 30 features (0.967)。R1 提出 alternative interpretation：模型学习重建 LF 输出而非 "universal stagnation signals"。R2 反驳：cmd_rep firing rate 65.5%→5.4% 说明 LF memorization 无法解释。**两者均认为需要 11 vs 30 的显著性检验**。

**W3. Temporal label model negative finding 信息量有限** [R1-W2 + R2 AGREE]
3 binary LFs → 8 种投票模式 → conf≥2 agreement 95.1%。MV 不可超越几乎是必然结果。Contribution 3 过度包装了一个可预测的 finding。

**W4. Label version bias 讨论不够深入** [R1-W3 + R2 AGREE]
OH stagnation rate 6.56%→21.4% (3.3× 变化) 是 embedding version mismatch 导致。缺少：bug 发现过程、corrected vs gold 一致性验证、pipeline robustness implications。

**W5. Multi-seed stability 缺正式统计检验** [R1-W4 + R2 AGREE]
只报告 mean±std (5 seeds)，关键对比缺少 paired t-test 或 Wilcoxon。

**W6. Conf≥2 作为 primary evaluation 合理性** [R1-W5, R2 部分同意]
conf=1 窗口（最模糊案例）恰是部署中最需处理的。主文几乎所有数字在 conf≥2 上报告，conf=1 专项分析缺失。

**W7. Table 1 脚注过密** [R2-W4 + R1 AGREE]
†, a, b 三个脚注承载过多关键信息（循环性 caveat、评估范围差异、显著性检验）。

**W8. 14 个 orphan bibliography 条目 + 年份错误** [R2-W3 + R1 AGREE]
7 个 ACL 模板残留 + 7 个 unused 引用。ratner2017snorkel 年份应为 2019。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成完全共识：

1. **Headline 数字不公平**：16.8pp 和 36.9pp 均涉及跨数据集/跨范围的不可直接比较，必须在 Abstract 中明确标注或替换为 same-scope 数字 [C1, C2]
2. **Gold set 验证不足**：κ=0.39, N=505, 12.8pp silver-gold gap 未分析——gold set 不足以 definitively 打破循环 [C3]
3. **λ₃ 特权信号**：headline 基于不可部署配置，需要 2-LF 主表结果 [C4]
4. **页数超限**：desk reject 风险 [C5]
5. **"语义停滞" motivation 与 cmd_rep 依赖性矛盾** [W1]
6. **Label model negative finding 可预测** [W3]
7. **Findings track 适合性**：两位均认为达到 Findings 水准但不足以进 main conference [C6]

---

## Reviewer Divergence [REBUT]

1. **新颖性程度** [Minor divergence]
   - R2: 四个 contribution 均无创新（Excitement 2/5）
   - R1: C1 (LF 设计) 和 C2 (label quality insight) 有部分新意（Excitement 3/5）
   - 结论：两者差异不大，均建议 Findings

2. **Feature overlap 解读** [Technical divergence]
   - R1: 11>30 features 可解读为 LF 重建而非 universal signals
   - R2: cmd_rep firing rate 跨 agent 差异说明不是 LF memorization
   - 结论：两者均要求 11 vs 30 的显著性检验

---

## Questions to Authors

Q1. 能否在同一评估集上做 structural GB vs LLM (5-shot-CoT) 的直接对比？（在 OH cross-agent 上跑 LLM，或在 SWE-Agent in-domain 上用非循环方式评估 structural GB）

Q2. Gold set 的 stagnation prevalence 是多少？它与 corrected silver labels 的 21.4% 一致吗？

Q3. 2-LF (λ₁+λ₂ only, no λ₃) 配置下 structural GB 的 cross-agent transfer F1 是多少？

Q4. Probe 的零样本 OH evaluation 为什么只在 15% test split 上做？OH embeddings 是否不完整？如果是，能否补算？

Q5. 11 个 LF-overlap features (0.977) 比 full 30 features (0.967) cross-agent F1 高 1.0pp——这个差异是否统计显著？

Q6. GB gold F1=0.839 vs silver F1=0.967 的 12.8pp gap 来自何处？是否集中在特定 LF 配置（conf=1 vs conf≥2）或 trajectory 阶段（early/mid/late）？

Q7. 论文检测到的 "stagnation" 中，有多大比例也能被简单的重复阈值检测器发现？这关系到 "语义停滞" motivation 的真实性。

---

## Missing References

1. **WRENCH benchmark** (Zhang et al., 2021, NeurIPS)——已在 bib 但未在正文引用。作为 WS benchmark 应在 Related Work 讨论适用性。
2. **Confident Learning** (Northcutt et al., 2021, JAIR)——noisy label 检测主流方法，与本文 label quality focus 直接相关。
3. **Label model theory** (Shin et al., 2022)——分析了 label model 在 low-LF 场景下的 performance bounds，与 Finding 3 直接相关。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。

---

## Overall Assessment

**评分**: Borderline Reject（main conference）/ Weak Accept（Findings track）
**置信度**: 4/5

**综合评分**: R1 2.5/5, R2 3/5 → 平均 2.75/5

**评判理由**:

本文解决了一个有实践价值的问题（LLM agent 停滞检测），实验覆盖面广，循环性讨论的诚实度值得肯定。经过多轮修改，gold set 验证已完成、LLM-as-judge 评估已全面化、deployment trade-off framing 清晰。

但核心方法学问题仍未解决：

1. **两个 headline numbers (36.9pp, 16.8pp) 均涉及不可直接比较的评估设置**——前者是不同评估规模（150K vs 6K），后者是不同数据集（cross-agent vs in-domain）。这不是 framing 问题而是 validity 问题。
2. **Gold set 作为唯一外部验证，其 κ=0.39 和 12.8pp silver-gold gap 削弱了非循环 claim 的力度**。
3. **所有 headline numbers 基于包含特权信号 (λ₃) 的不可部署配置**，可部署版本的性能未知。
4. **"语义停滞" 的 motivation 与方法实际依赖的 cmd_rep 信号存在内在张力**。
5. **正文超 8 页限制**，有 desk reject 风险。
6. **方法论新颖性不足**——四个 contribution 均为已有技术的组合应用。

**建议**: 
- **短期（ARR 提交前）**: 修复页数超限 (C5)；在 Abstract 限定 headline 比较条件；添加 2-LF 结果。
- **中期（commitment 前）**: 补充 matched-scope 评估（structural GB on 6K subset 或 probe on 150K）；补 LLM on OH 实验；分析 silver-gold gap。
- **Track 选择**: 两位 Reviewer 均强烈建议 **Findings track**。

---

## Detailed Comments（逐节）

### Abstract
- "outperform the neural probe by 36.9pp and the best LLM judge by 16.8pp" 需加限定语标明评估条件差异
- "cross-coding-agent structural 0.967 vs best LLM 0.799" 需标注前者是 cross-agent OH、后者是 in-domain SWE-Agent
- "semantic stagnation...evade repetition detectors" 措辞过强，与实际依赖 cmd_rep 的事实矛盾

### §1 Introduction
- Finding 1-3 的详细描述（L28-50）与 §4/§5 高度重复，可压缩为 2-3 句以省空间
- 16.8pp 的 cross-dataset comparison 在此处同样未加限定

### §2 Related Work
- WRENCH (Zhang et al., 2021) 已在 bib 但未 cite
- 缺 Confident Learning 和 label model theory 讨论

### §3 Method
- λ₁ 的具体 threshold（what repetition ratio triggers stagnation vote）未给出
- "silver labels" 术语首次出现时未定义
- Label convention (0=stagnation) 与通常 positive-class convention 相反，可能造成困惑

### §4 Experiments
- Table 1 脚注 †/a/b 过密，建议将 a/b 内容整合到正文
- Table 1 footnote b 的 paired bootstrap: N=6,122 来自 probe test split——如果 GB 是在全集评估，paired test 需要在相同 N 上进行
- §4.2 "the structural advantage holds even comparing the harder cross-agent setting against the LLM's easier in-domain regime"——这句话承认了不可比性，但 Abstract 没有

### §5 Analysis
- §5.1 + §5.2 建议合并为 "Circularity Analysis"
- §5.3 可整体移入 Appendix 以省空间
- 11 features vs 30 features 的 1.0pp 差异需显著性检验

### §6 Conclusion
- 超出 8 页限制——Reproducibility 段落可移至 Appendix

### Limitations
- 内容充实且诚实
- 建议增加对 "semantic stagnation" 与实际检测信号之间 tension 的讨论

### Appendix
- Table 8 (LLM evaluation) 信息量丰富
- Appendix D (label quality) 和 Appendix I (error analysis) 质量高
- 14 个 orphan bib entries 需清理
- ratner2017snorkel 年份应为 2019