---
round: 46
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-25T22:50:16.034694+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 46 审稿报告 — struct_self_consist_ie

**论文**: "When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap"
**目标 Venue**: EMNLP 2026 Main Conference via ARR (May 2026 cycle)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）
**轮次**: 1 轮（交叉分享后关键问题达成共识，无需 Round 2）

---

## Summary

本文研究 self-consistency（SC）在 NER 任务上的效用，在 4 个 NER 数据集上用 fine-tuned 7-14B 模型定义了 5 种质量估计信号，发现这些信号虽能有效估计输出质量（AUROC 最高 0.82），但无法转化为选择增益——称为 **correlation-selection gap**。通过诊断框架识别两个共现条件：**退化**（12-68% 实例输出相同）和**信号对齐塌缩**（per-sample 信号无法区分候选）。Entity-level construction 在 Few-NERD 上获得 +1.40pp 条件性增益，但大多数配置下呈 inverse scaling。跨任务扩展（RE、SQL）确认结构化输出上的失败模式。

---

## Strengths

1. **Correlation-selection gap 概念清晰有力**：将质量估计能力与选择增益之间的脱节命名并系统分析，为理解 structured SC 的失败提供了 reusable 的诊断框架。比简单报告 "SC doesn't work for NER" 有更高的分析价值。[R1, R2 共识]

2. **统计方法论达到同行评审标准上限**：TOST 等效性检验支持 negative claims、paired bootstrap 估计效应量、Holm-Bonferroni 多重比较校正。Table 12 完整枚举 k=57 个统计检验的做法值得推广。Limitations 中主动披露 Holm p_adj=0.055、MDE≈1.5pp 等不利统计细节，透明度极高。[R1, R2 共识]

3. **5 信号分类学设计周密**：覆盖 per-sample vs instance-level、structural vs probabilistic 的二维空间，使不同信号的失败模式可被独立分析。LP 作为唯一产生正面选择增益的信号的发现有实际指导意义。[R1]

4. **实验覆盖度高**：45 页 appendix 提供极为详尽的消融分析（温度敏感性、N-scaling、cross-dataset OOD、free-form decoding、calibration、entity-level verifier transfer、few-shot 对比等）。几乎每一个合理的质疑都能在 appendix 中找到对应分析。[R1, R2 共识]

5. **高可复现性**：匿名代码/数据链接、超参数详尽记录（Table 21）、信号定义明确。[R1, R2 共识; Reproducibility 4.0/5]

6. **三步诊断协议（Appendix ae）具有实践价值**：测量退化 → 评估信号对齐 → 选择聚合策略，为 practitioners 提供 actionable guidance。[R1]

---

## Weaknesses

### Must-Fix（影响接收决定）— 3 项共识

**N1 [critical, consensus]** 模型规模限制削弱广泛性声明
- 标题 "When Self-Consistency Fails for NER" 暗示普遍诊断，但所有核心证据仅来自 Qwen3-8B 和 LLaMA-3.1-8B（7-14B fine-tuned）。论文自身数据构成内在张力：Table 44 显示 72B headroom 为 8.1pp（远高于 8B 的 1.2pp），Limitations 承认 frontier models 退化率 8.5-24%。诊断框架预测低退化→SC 有效，但未在大模型上验证。
- **建议**：(a) 标题/摘要/引言明确限定为 "fine-tuned 7-14B open-weight models"；或 (b) 至少补充一个 30B+ 或 proprietary 模型验证。
- **跨轮追踪**：该问题自 Round 43 (R43-W5) 持续存在，Round 45 升级为 Must-Fix，Round 46 仍未解决。

**N2 [critical, consensus]** 退化分解上界（§6.3）理论贡献定位不当
- 上界 $E[\Delta F1] \leq (1-D) \cdot G_{nd} \cdot \alpha$ 本质是 partition 恒等式加 trivial 约束。Recovery ratio 仅 3-12%（Table 32），bound 比实际值宽松 8-33 倍。以 Theorem/Corollary 形式呈现让读者预期非平凡理论贡献，但实际数学深度不支持。
- R2 补充：分解本身在诊断层面有用（三因子可独立量化），问题在于用 Theorem 格式 overclaim 数学贡献层次。
- **建议**：重新定位为 empirical decomposition framework；移除 Theorem/Corollary 形式化框架，改用文字叙述。
- **跨轮追踪**：Round 43 (R43-N2) 曾通过三阶段重构标记 resolved，Round 46 以更精确角度重新提出。

**N3 [critical, consensus]** SQL 跨任务证据严重不足
- Abstract "Cross-task pilots on RE and SQL parsing **confirm** task-specific failure modes" 中 "confirm" 暗示系统性验证，但 SQL 实际证据仅一个退化率统计量（87.2%, n=196）。RE 有完整 Appendix q 分析（LP selection、flip instances、free-form comparison），SQL 深度完全不匹配。R1 补充：Appendix ah SQL 引用的是外部 GPT-3.5 结果，非本文 fine-tuned 模型。
- **建议**：(a) SQL 从 abstract 移除或降级为 "anecdotal observation"；或 (b) 补充完整诊断。

### Should-Fix（影响评分但不一票否决）— 6 项

**W1 [warning, consensus]** Few-NERD 正面结果未被充分利用为框架验证
- Few-NERD 退化率最低（13%）时 LP 获得 +1.39pp，是框架 "低退化→SC 有效" 预测的最佳正面验证。论文 framing 偏向 "SC fails"，将 Few-NERD 当作例外而非验证。
- **建议**：§8 Discussion 中重构为框架预测能力的正面验证；补充 Few-NERD 低退化原因分析。

**W2 [warning, Director 判定]** Entity construction +1.40pp 在全局 Holm 校正下为 marginal significance
- p_adj=0.055（global k=57），未达 α=0.05。Abstract 中作为唯一具体数字被突出。
- R2 列为 Must-Fix，R1 REBUT：核心贡献是诊断性的非建设性的，family-wise k=21 下 p=0.013 显著，核心 negative claim 由 TOST 支撑。
- **Director 判定**：降级为 Should-Fix。R1 论据充分——论文价值主要在诊断框架而非建设性增益。但 abstract/Figure 1 的 framing 需更谨慎。
- **建议**：Abstract 加 qualifier（"marginally significant under global correction"）；Figure 1 标注为单配置/单数据集结果。

**W3 [warning, consensus]** 与 Landesberg (2026) 差异化论述不足
- §2 concurrent work 段仅约 4 行，Table 1 维度选择单方面偏向本文。
- **建议**：扩展至完整段落，承认 Landesberg 优势并说明互补关系。
- **跨轮追踪**：自 Round 39 持续存在。

**W4 [warning, consensus]** 2-3 seeds 统计推断力有限
- Table 11 LP on SciERC 95% CI [-0.41, +2.34] 跨零点。2-3 seeds 的基础设计与上层统计方法精密度不匹配。
- **建议**：至少一个核心配置运行 5 seeds。
- **跨轮追踪**：自 Round 40 持续存在。

**W5 [warning, consensus]** MBR 连接 novelty 声明过高
- Proposition 1 在 entity-wise independence 假设下是标准 MBR 理论的直接应用。概念上有用但非独立理论贡献。
- **建议**：定位为 "connecting existing MBR theory to NER" 而非原创理论结果。

**W6 [warning, consensus]** Entity-level construction 的 inverse scaling 未充分解释
- 40/58 transitions 呈 inverse scaling，归因分析不够深入。如果方法在大多数配置下有害，"建设性贡献"定位需更强 qualification。
- **建议**：补充归因分析或明确定位为 preliminary exploration。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键判断上达成共识：
1. Correlation-selection gap 是有价值的诊断概念 [AGREE]
2. 模型规模 scope 与 evidence 不匹配 [AGREE, N1]
3. 退化分解上界应重新定位为 empirical framework [AGREE, N2]
4. SQL 证据不足以支撑 "confirm" 声明 [AGREE, N3]
5. Few-NERD 正面结果应重构为框架验证 [AGREE, W1]
6. 2-3 seeds 统计推断力不足 [AGREE, W4]
7. MBR Proposition 1 novelty overclaimed [AGREE, W5]
8. Entity construction inverse scaling 需更好解释 [AGREE, W6]

## Reviewer Divergence [REBUT]

**分歧 1**: R2-N2（Holm p_adj=0.055 严重程度）
- R2: Must-Fix——核心建设性 claim 未达显著性阈值
- R1: Should-Fix——核心贡献是诊断性的，+1.40pp 不是核心 claim，family-wise 显著
- **Director 判定**：Should-Fix。R1 论据更有说服力，论文价值在诊断框架而非建设性增益。

**分歧 2**: R2-W2（§4/§7 结构分散）
- R2: Should-Fix——读者难以区分诊断发现和方法验证
- R1: Minor——"建立核心发现→外部验证"结构在 empirical NLP 中常见，加定位声明即可
- **Director 判定**：Minor。R1 的结构分析合理，加定位声明足够。

**分歧 3**: R2-W4（缺少 NER ensemble 文献）
- R2: Should-Fix——Florian et al. (2003) 和 Diverse Beam Search 是重要遗漏
- R1: Minor——Florian 是 supervised ensemble 而非 SC，领域不同；DBS 可加但非 gap
- **Director 判定**：Minor。两者与 SC 的核心假设不同，用一句话提及即可。

---

## Questions（需要作者澄清）

1. Few-NERD 退化率（13%）显著低于其他数据集，是否与 fine-grained entity type（66 types）特性有关？低退化的原因分析是否可以增强诊断框架的 prescriptive value？
2. 72B 模型的退化率具体是多少？如果确实更低，这将直接验证论文核心机制。
3. 如果增加 seed 数量（从 3 到 5 或 10），Holm 校正后 p_adj 是否有望降至 0.05 以下？
4. SQL 87.2% degeneracy 是否有计划补充完整诊断框架验证？
5. Table 32 中有多少配置的 D 低于 critical degeneracy threshold $D_{crit}$？如果大多数配置远高于阈值，bound 的 prescriptive value 有多大？
6. 使用 full evaluation set（包含 zero-entity 实例）时，退化率和 gap 如何变化？
7. Landesberg (2026) 是否覆盖了 NER？本文 "NER-specific" 角度的独特性有多强？

---

## Missing References

1. **Florian et al. (2003)** — NER ensemble learning，虽与 SC（单模型多采样）机制不同，但作为多输出聚合的自然历史对照值得提及。[R2 提出, R1 认为 minor]
2. **Vijayakumar et al. (2018)** — Diverse Beam Search，与降低 degeneracy 的概念联系值得一句话提及。[R2 提出, R1 部分同意]

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目配置未启用外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: Agent 超时（300s 后无结果返回）。视觉审查未能完成。用户可选择重新触发 `dispatch_visual_check()`。

---

## Overall Assessment

**评分: 3.0 (Findings)**
**置信度: 4/5**

**评分理由**：

论文的核心诊断贡献——correlation-selection gap 的识别和 degeneracy + signal alignment collapse 的分解——是扎实且有用的。统计方法论严谨（TOST、bootstrap、Holm-Bonferroni），实验覆盖全面（4 数据集 × 2 模型 × 5 信号 + 45 页 appendix），透明度极高。

但以下问题累积使论文未达 Main Conference 水平：

1. **Scope-evidence 不匹配**（N1）：标题暗示普遍诊断，但证据仅限 7-14B fine-tuned 模型，且论文自身数据显示退化率是 model-family-dependent 的。这是自 Round 43 以来持续未解决的核心问题。

2. **理论贡献定位偏差**（N2）：退化分解上界的数学 trivialness 与 Theorem 形式的 expectation 不匹配。MBR 连接也是已有理论的直接应用。论文的理论贡献声明整体偏高。

3. **SQL 跨任务证据空洞**（N3）：Abstract 声称 "confirm"，但仅有一个数字。

4. **Concurrent work 削弱新颖性**（W3）：Landesberg (2026) 独立发现了 correlation-selection gap，差异化论述不足。

5. **统计 power 基础薄弱**（W4）：2-3 seeds 不足以支撑论文的统计精密度声明。

**Findings 推荐理由**：诊断框架对 structured prediction + SC 的研究社区有实际参考价值，实验设计全面严谨，方法论上可以作为该方向研究的参考标准。在修复 framing 问题（限定 scope、降级 SQL、重定位 bound）后，Findings 水平的贡献是明确的。

**升级至 Main Conference 所需**：(1) 至少一个大模型验证框架预测；(2) 增加 seed 数量提升统计 power；(3) Landesberg 差异化论述大幅加强。

---

## Detailed Comments（逐节）

### Abstract
- "+1.40pp on Few-NERD" 作为唯一具体数字被突出，但在全局 Holm 校正下仅 p_adj=0.055，需加 qualifier。
- "+1.40pp" 与正文 "+1.39pp" 不一致（四舍五入），应统一。
- "Cross-task pilots on RE and SQL parsing confirm task-specific failure modes" 中 "confirm" 对 SQL 而言 overclaiming，建议改为 "suggest" 或移除 SQL。
- 字数需确认是否在 200 words 以内（EMNLP 2026 要求）。

### §1 Introduction
- 三阶段结构（Discover/Diagnose/Construct）清晰有效。
- 脚注 1 匿名代码链接格式正确。
- 但标题/引言的 framing 需限定模型 scope。

### §2 Related Work
- Table 1 novelty comparison 维度选择偏向本文，需增加本文较弱维度或在 caption 中承认局限。
- Concurrent work（Landesberg 2026）讨论仅约 4 行，需扩展至完整段落。
- 缺少 NER ensemble（Florian et al., 2003）和 diverse decoding（Vijayakumar et al., 2018）的简要提及。

### §3 Diagnostic Framework
- 问题形式化严谨，per-sample vs instance-level 信号的区分是重要洞察。
- §3.1 "capability ceiling" 中 N≤16 缺乏选择依据。
- 符号首次出现时定义不够直观。

### §4 Single-Signal Selection Results
- 核心发现（信号能估计质量但无法提升选择）证据充分。
- 第 2 段信息密度过高（10+ 统计量），建议精简关键数字到正文，其余移至 table/appendix。

### §5 Adaptive Methods
- 9 种方法覆盖全面，Table 3 设计有效。
- Cross-model self-consistency（§5.1）仅单数据集，需注明 preliminary。

### §6 Threshold Regime Analysis
- §6.1 MBR 连接概念有用，但 Proposition 1 novelty 声明应降级。
- §6.3 退化分解上界应从 Theorem 重定位为 empirical decomposition。
- Inverse scaling（40/58 transitions 为负）是重要发现但归因分析不足。

### §7 Cross-Dataset Experiments
- 跨数据集验证设计合理。
- Few-NERD 正面结果（+1.39pp）应被重构为框架预测能力的正面验证。
- Entity construction 在大多数配置下有害，§7.5 需更强 qualification。

### §8 Discussion
- 过短，应增加 Few-NERD 作为框架正面验证的讨论。
- "Primarily diagnostic" 定位与 abstract 突出 +1.40pp 之间存在张力。

### Limitations
- 内容充分，主动披露不利统计细节（p_adj=0.055、MDE≈1.5pp）。
- 符合 EMNLP 2026 要求（正文末尾、references 之前）。
- MDE≈1.5pp 应在 §4 或 §7 首次出现。

### Appendix
- 36 页，覆盖极为详尽，但正文对关键 appendix 的引导不足。特别是 Appendix i（self-verification）、s（free-form decoding）、x（cross-dataset OOD）包含重要分析。

### 格式合规
- ✅ ACL template（`\usepackage[review]{acl}`）
- ✅ Double-blind（`\author{Anonymous}`）
- ✅ Limitations section 在正文中
- ⚠️ 正文页数需确认是否在 8 页以内（从 TeX 结构看包含 8 个 \input sections + limitations）