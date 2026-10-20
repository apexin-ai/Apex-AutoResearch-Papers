---
round: 0
overall_score: weak reject
timestamp: 2026-05-15T02:39:51.693165+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 1

**Paper**: "Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision"
**Venue**: EMNLP 2026 via ACL Rolling Review
**Reviewers**: R1 (Methods + Experiments), R2 (Novelty + Related Work)
**Date**: 2026-05-15

---

## Summary

本文系统比较了三种范式在 LLM 编程智能体停滞检测任务上的表现：30 个手工结构特征 + GB/RF 分类器、GRU 探针（frozen Qwen3-Embedding）、LLM-as-Judge（Claude Sonnet 4.6 zero-shot）。基于弱监督（3 labeling functions + majority vote）标注约 194K 轨迹窗口，650 窗口 gold set（3 annotators, κ=0.82）验证结果。核心发现：结构 GB 在 gold set 上达到 0.948 F1，领先 GRU 探针 8.7pp、LLM 判官 25.9pp（zero-shot cross-agent transfer）。

论文提供了有价值的实证工作，包括系统性的多维度比较、诚实的循环性自我批判、以及标签质量瓶颈的洞察。但核心主张的幅度被银标签循环评估放大约 4 倍，LLM 基线设计不够公平，方法论上的 LF-feature 循环性在三条 defense 线全部被削弱后实质上未被有效解决。

---

## Strengths

1. **系统性多维度实验设计** [R1, R2 consensus]：覆盖数据量曲线（Figure 2）、embedding backbone 消融（Table 7/8）、label aggregation 比较（Table 6）、窗口大小消融（Table 8），提供了远超单一比较的完整图景。

2. **Gold-set validation 是最佳实践** [R1, R2 consensus]：650 窗口、3 annotators、κ=0.82 的人工验证在弱监督研究中属于高标准。conf≥2 分层有理有据。

3. **诚实的循环性自我批判** [R1, R2 consensus]：论文在 §4.6 和 §5.1 显式承认结构特征与 LF 的重叠，区分了"LF 可重构性"与"真实检测精度"。这种透明度在弱监督文献中不常见。

4. **标签质量发现有洞察力** [R1, R2 consensus]：OH 嵌入版本偏差修正（stag rate 6.56%→21.4%）是对弱监督实践有价值的经验教训。

5. **实用部署特性** [R2]：zero-data、no-GPU、sub-5ms per window 的结构特征部署特性有真实价值。

6. **规范的统计方法** [R1]：McNemar 检验、Kruskal-Wallis + Bonferroni 校正、多种子稳定性报告。

7. **有价值的负面结果** [R1]：4 种时序标签模型均未超越 MV（§4.7, Table 6），为弱监督社区界定了适用边界。

---

## Weaknesses

### Critical (Must-Fix)

**C1. LF-Feature 循环性实质上未被有效解决** [R1-W1, R2-W2 → AGREE, upgraded to critical]
论文承认结构特征与 labeling functions 高度重叠（λ₁→repetition, λ₂→file ops, λ₃→action patterns），并提出三条 defense：
- (a) Gold set validation → 但 gold set 采样程序未公开，仅覆盖 SWE-Agent，可能偏向 high-confidence windows
- (b) Boundary disagreement analysis → 仅 52 个 disagreement windows，Fisher exact test p≈0.10-0.15，统计不显著
- (c) cmd_rep ablation → −29.4pp 证明了强依赖而非独立性

**三条 defense 线同时被削弱后，"结构特征检测真实停滞而非重构 LF 信号"的核心主张缺乏充分方法论支撑。**

所需行动：(1) LF oracle baseline（3 LF votes 作为 features 的 LR，报告 gold F1）；(2) 公开 gold set 采样程序；(3) OpenHands gold annotations 或限定 claim 范围；(4) 计算所有 non-overlap 特征与 LF 输出的互信息。

**C2. 核心 claim 幅度被循环评估放大约 4 倍** [R1-W1, R2-W1 → AGREE]
标题声称 "Structural Features Dominate"，摘要引用 36.9pp 和 30.5pp 优势。但 gold 验证将差距从 36.9pp 缩小到 8.7pp。银标签评估系统性低估探针能力（探针零样本银 0.598→gold 0.861，+26.3pp）。更关键的是，probe 全量微调后达 0.976 超过结构 0.967。

"Dominate" 在 gold 证据下不成立。标题和摘要传达的印象（~30+pp）与 gold 证据（8.7pp，可被微调反超）之间的落差构成 claim 过度陈述。

所需行动：(1) 修改标题避免"dominate"；(2) 以 gold 数字为主，银标签降级为 circular upper bound；(3) 完整呈现零数据结构优势 vs 有数据探针反超的图景。

**C3. LLM-as-Judge 基线设计不公平** [R1-W2, R2 cross-response R1-Issue-4 → AGREE]
LLM 基线仅用 Claude Sonnet 4.6 单模型、零样本提示、原始文本输入。相比之下结构特征接收 30 维精心工程化的特征向量。具体不足：(1) 未测试 GPT-4o/Claude Opus/开源 LLM；(2) 未用 CoT 或 self-consistency；(3) 未给 LLM 结构化特征输入；(4) few-shot 仅一种配置。25.9pp gold 差距中，prompt 工程不足 vs LLM 根本局限无法区分。

所需行动：(1) 添加至少一个额外 LLM + CoT 实验；(2) 测试 LLM + 结构化输入；(3) 或明确将 LLM 定位为 cost-performance baseline 而非能力上界。

**C4. 3-LF 弱监督退化限制 Finding 3 推广性** [R1-W3]
3 个二值 LF 最多 8 种投票模式，conf≥2 上 LF 一致率 95.1%。FlyingSquid 与 MV 100% 一致。TWV 仅翻转 14.1% conf=1 标签。Finding 3（"no label model improves over MV"）本质上是 3-LF 低冲突条件的必然结果，而非可推广的领域发现。

所需行动：(1) 限定 Finding 3 为 low-conflict 3-LF regime；(2) 报告银标签噪声率（vs gold，按 conf 分层）；(3) 讨论增加至 5-10 个 LF 后结论是否可能反转。

### Warning (Should-Fix)

**W1. 核心发现缺乏顶会新颖性** [R2-W1]
手工领域特征在窄分类任务上胜过通用方法是 well-established pattern（medical imaging, fraud detection, anomaly detection）。论文将其包装为 novel finding 不成立。更有价值的贡献——标签质量瓶颈（§4.6）和时序模型失败（§4.7）——反而被边缘化。

建议：reframe 为"面向 agent 监控的弱监督方法论研究"，以 label quality bottleneck 和 temporal model failure 为核心。

**W2. Gold set 采样策略和规模论证不足** [R1-W4, R2-W2 → AGREE]
650 窗口仅占 0.33%。未报告采样策略、agent 比例、标注员是否有权访问 outcome、标注指南中"停滞"的操作性定义。

**W3. Overlap ablation 边界模糊** [R1-W5, R2 cross-response R1-Issue-5 → AGREE]
14 vs 16 特征划分标准未说明。"重叠"是直接计算重叠还是统计相关？edit distance 等"non-overlap"特征可能与 file_diff LF 间接相关。5.8pp 差距（0.890 vs 0.948）说明 LF 相关特征确实贡献显著信号。

**W4. 探针架构搜索不充分** [R1-W6, R2-Q3]
仅 GRU。BGE-M3 (0.941) 优于 Qwen3 (0.906) 达 3.6pp，但主实验仍用 Qwen3 未解释。未测 Transformer encoder。

**W5. Agent 多样性不足** [R2-W3]
仅 2 个 coding agent + SWE-bench。"Cross-agent transfer" 泛化声明过强。不覆盖非 coding agent、不同 benchmark。

**W6. 重要 Related work 缺失** [R2-W4]
缺 process mining（van der Aalst，最严重——paper 本质是 process mining on agent trajectories）、SpecRA、AgentBoard/Progress Rate、sequential anomaly detection。

**W7. 可复现性不完整** [R1-W7]
30 特征未逐一定义（仅 4 类概述），无代码可用性声明，数据划分策略不完整。

### Info (Nice-to-Fix)

**I1.** PDF 中可见 `{GOLD_SET: ...}` 占位符文本 [R1-W8]
**I2.** LLM 和 Cosine Similarity 缺少跨智能体迁移结果 [R1-W9]
**I3.** 7 个 orphan 参考文献条目（ACL 模板残留） [R1-W10, R2-W5]
**I4.** 结果部分 §4.2-4.7 信息密度过大 [R2-W6]

---

## Reviewer Consensus

以下问题两位 Reviewer **达成一致**：

| Issue | R1 | R2 | 一致性 |
|-------|----|----|--------|
| 循环性是核心方法论缺陷 | W1 (major) | W2 (critical) | [AGREE] — R2 升级严重性 |
| Claim 幅度过度 (dominate + 36.9pp) | W1 (major) | W1 (major) | [AGREE] |
| LLM 基线不够公平 | W2 (major) | Cross-R1-Issue-4 [AGREE] | [AGREE] |
| Gold set 采样未公开 | W4 (moderate) | Cross-R1-Issue-1 [AGREE] | [AGREE] |
| 间接 feature overlap 存在 | W5 (moderate) | Cross-R1-Issue-5 [AGREE] | [AGREE] |
| Boundary analysis 统计 underpowered | Implicit in W1 | Cross-R1-Issue-3 [AGREE] | [AGREE] |
| 模板 bib 条目需清理 | W10 (minor) | W5 (minor) | [AGREE] |
| 诚实 self-critique 值得肯定 | Strength | Strength | [AGREE] |
| 实验覆盖面扎实 | Strength | Strength | [AGREE] |

## Reviewer Divergence

| Issue | R1 | R2 | 说明 |
|-------|----|----|------|
| TWV 是否有定义 | 认为未定义 (Issue-2) | [REBUT] TWV 在 §3.4.1 有定义 | R2 正确——TWV 有定义，R1 混淆了 Table 3 和 Table 6 |
| 3-LF 退化问题 | W3 (major) | 未直接涉及 | R1 独立发现，R2 未评论 |
| Finding 3 推广性 | 质疑推广性 | 接受负面结果价值 | 轻度分歧，R1 更严格 |

---

## Questions for Authors (Consolidated, Deduplicated)

1. **LF oracle baseline**: 用 3 个 LF votes 作为 features 训练 LR，gold F1 多少？这是量化循环性的关键实验。
2. **Gold set 采样**: 如何从 194K 选出 650？按 agent/confidence 分层？标注员是否知道 task outcome？
3. **Gold-silver 差距解释**: 探针零样本 silver 0.598→gold 0.861（+26.3pp），为什么银标签如此系统性偏向结构方法？
4. **LLM + 结构化输入**: 给 LLM 提供 30 维结构特征作为格式化输入，性能如何变化？
5. **为什么 Qwen3 而非 BGE-M3?** Appendix 显示 BGE-M3 优于 Qwen3 达 3.6pp，这会将结构-探针差距缩小到多少？
6. **Non-overlap 特征间接相关性**: 16 个 non-overlap 特征中，与 LF 输出的 Pearson r > 0.3 的有多少？
7. **银标签噪声率**: 以 gold 为基准，整体噪声率多少？conf=1 vs conf≥2 分别多少？
8. **银标签 precision/recall 分解**: 银标签的 FP 和 FN 各占多少？哪种类型的错误更多？

---

## Missing References

| 缺失文献 | 相关性 | 提出者 |
|----------|--------|--------|
| Process mining (van der Aalst et al., 2012, 2016) | 核心技术类比——结构特征检测序列过程异常 | R2 |
| SpecRA (OpenReview, 2025) | 直接竞品——LLM agent 频谱重复检测 | R2 |
| AgentBoard / Progress Rate (Ma et al., 2024) | 高度相关的 agent 进度度量 | R2 |
| Sequential anomaly detection (Isolation Forest, LSTM-AD) | 理论支撑——为什么手工特征在窄 AD 任务上常胜 | R2 |
| CodeRL (Le et al., 2022) | 代码生成的 value-function 方法 | R2 |

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求。本轮内部审稿未配置外部审稿线。

---

## Overall Assessment

### Score: 3/6 — Weak Reject (Borderline, leaning reject)

**R1**: 3/6 (Borderline Reject), Confidence 4/5
**R2**: 3/6 (Borderline Reject), Confidence 4.5/5
**Consolidated**: 3/6 (Weak Reject)

### Confidence: 4/5

### 总评

论文方向正确、实验执行扎实、自我批判诚实——这些都是值得肯定的品质。但目前存在 4 个 critical issues 和 7 个 should-fix issues，其核心问题在于：

1. **方法论完整性受损**：LF-feature 循环性的三条 defense 线全部被削弱，核心主张"结构特征检测真实停滞"缺乏充分支撑。LF oracle baseline 是验证循环性程度的关键缺失实验。

2. **Claim 与证据不对齐**：标题"dominate"和摘要 36.9pp 来自循环银标签评估，gold 仅 8.7pp 且可被微调反超。核心 claim 的陈述强度显著超过证据支撑。

3. **基线不公平**：LLM baseline（单模型、零样本、无结构化输入）和 probe baseline（GRU only、非最优 embedding）均未被充分调优，使得比较结论的可信度受限。

4. **贡献定位不准确**：真正有价值的贡献——标签质量瓶颈（§4.6）和弱监督方法论洞察——被"结构特征胜出"的叙事掩盖。核心发现（domain features > generic on narrow task）在顶会标准下缺乏新颖性。

### 修订路径

若作者能：(1) 添加 LF oracle baseline 量化循环性；(2) 修正 claim 强度至 gold 证据水平；(3) 补充至少一个 LLM+CoT 实验；(4) 公开 gold set 采样程序——论文有望达到 **Findings** 接收标准。达到主会议标准还需 reframe 贡献定位和扩展 agent 覆盖面。

---

## Detailed Comments (Per Section)

### Title & Abstract
- "Dominate" → 改为 "Enable" 或 "Outperform in Zero-Shot Settings"
- 36.9pp/30.5pp 银标签数字应降级或移除，以 gold 8.7pp 为主
- 清理 `{GOLD_SET: ...}` 占位符

### §1 Introduction
- 贡献列表应以 gold 验证数字为准
- 添加"有数据 regime 下探针反超"的限定

### §2 Related Work
- 添加 process mining 文献（核心缺失）
- 添加 SpecRA、AgentBoard 引用
- 清理 orphan bib 条目

### §3 Method
- §3.3.1: 逐一定义 30 个特征（可放 appendix）
- §3.3.2: 解释为什么 GRU 而非 Transformer，为什么 Qwen3 而非 BGE-M3
- §3.3.3: 增加 LLM 变体（CoT、结构化输入）

### §4 Results
- §4.3: 以 gold 数字为叙事主线，银标签降级
- §4.6: 提升标签质量发现的叙事地位（这是真正有价值的贡献）
- §4.7: 限定 Finding 3 仅适用于 3-LF low-conflict regime
- 添加 LF oracle baseline 实验
- 报告银标签噪声率

### §5 Analysis
- §5.1: 循环性 defense 需要新的证据线（LF oracle、扩大 gold set、OH gold annotations）
- §5.2: 56% vs 38% boundary analysis 应附统计检验 p 值和 confidence interval

### §6 Conclusion
- 将"dominate"改为更准确的描述
- 添加 3-LF limitation qualifier for Finding 3
- "Cross-agent" 限定为 "cross-coding-agent on SWE-bench"

---

*Report compiled by Review Director, 2026-05-15. Round 1, single pass — no unresolved reviewer divergences requiring additional rounds.*