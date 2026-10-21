---
round: 0
overall_score: borderline
timestamp: 2026-05-14T12:20:27.321042+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Round 1 圆桌审稿

**论文**: "Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction"
**目标 Venue**: EMNLP 2026 (ARR)
**Reviewer 配置**: R1（方法与实验）+ R2（新颖性与相关工作）
**轮次**: Round 1（已收敛，无需第二轮）

---

## Summary

本文系统比较了 5 种 training-free confidence signals（Log-Probability、Entropy、Set Jaccard、Token Jaccard、Exact-Match）在 LLM-based 结构化信息抽取（NER/RE）的 best-of-N selection 场景中的表现。核心发现：(1) Set Jaccard (SJ) 在 NER 上显著优于 log-probability (Δρ≈0.16, p<10⁻²⁵)；(2) RE 中所有 signal 退化，归因于 compound error propagation。实验覆盖 3 个 NER 数据集 + 1 个 RE 数据集，2 个 8B 模型，多 seed/多温度/OOD 等消融维度。

---

## Strengths

**S1. 系统且全面的实验矩阵** [R1+R2 共识]
5 signal × 3 NER dataset × 1 RE dataset × 2 model × 2 budget × 2 temperature × 4 metric，13/15 实验完整覆盖。该领域首个如此系统的比较（限定为 LLM-based structured IE）。

**S2. LOO-SJ circularity check 方法论亮点** [R1 提出，R2 认可]
Table 1 Leave-one-out SJ（ρ=0.40 vs full SJ ρ=0.42, Δ=0.02）严谨地排除了 SJ 有效性依赖于自我循环的担忧。

**S3. Compound error boundary 诊断有理论价值** [R1 提出，R2 认可]
Section 5.9 对 RE 退化的因果分析（head + tail + relation type 三重叠加），Table 12 per-relation-type 证据具体。

**S4. 多维度鲁棒性验证** [R1+R2 共识]
Multi-seed（Std ≤ 0.01）、cross-dataset（排序一致）、cross-model、OOD（SJ-LP gap 从 +0.15 降至 +0.12 但仍显著）。

**S5. Best-of-N selection 实用性** [R2 提出]
将 ranking 指标转化为 F1 gain，对 practitioners 有直接指导价值。

**S6. Inverted-U pattern** [R1 提出]
Section 5.11, Table 15: SJ ρ 在 F1 bucket [0.3, 0.7] 最高，为 SJ 适用条件划定边界。

---

## Weaknesses（按严重程度排序）

### Must-Fix（影响接收决定）

**C1. 模型规模单一，严重限制普适性** [R1 critical + R2 agree]
仅 Qwen3-8B 和 LLaMA-3.1-8B 两个同规模模型。Confidence calibration 和 output diversity 随规模变化显著——更大模型的 greedy 可能已足够准确使 LP 优势明显化，更小模型高方差可能放大 SJ 优势。Abstract 中 "establish" 措辞过强。**建议**：至少增加一个 >30B 或 <3B 模型，或将 "establish" 降级为 "investigate"/"examine"。

**C2. 相关工作显著遗漏** [R2 critical + R1 逐条核实 agree]
5 篇核心文献缺失：
- Guo et al. 2017 (On Calibration of Modern Neural Networks, ICML) — 论文用 ECE 作核心指标却未引用其定义来源
- Snell et al. 2024 (Scaling LLM Test-Time Compute, ICLR 2025) — 标题围绕 TTS 却缺核心引用
- Aggarwal et al. 2023 (Adaptive-Consistency, EMNLP 2023) — 与 N-scaling 直接相关
- CISC: Huang et al. 2025 (Confidence Improves Self-Consistency, ACL Findings 2025) — 加权投票+confidence 融合，发现 "最 calibrated 的方法反而最无效"，直接挑战本文解读
- 传统 IE confidence（CRF 边际概率、span-level confidence、MC-dropout）— 至少应说明排除理由

**C3. RE task-complexity boundary 证据严重不足** [R1+R2 共识 critical]
全部 RE 实验仅在 SciERC relation subset (n=397, 6 relation types) 上进行。"Universal bottleneck" claim 需跨数据集验证（TACRED/DocRED/NYT），单数据集观察至多是 hypothesis。**建议**：增加至少一个 RE 数据集或降级措辞。

**C4. SJ 方法新颖性有限** [R2 critical + R1 agree]
SJ 是 set-level F1/Jaccard 的 confidence 化自然迁移（type-grouped Hungarian matching + token-overlap kernel）。缺少理论分析解释 Δρ≈0.16 的来源，也未与其他 set-similarity kernel（edit distance、embedding similarity）做消融。论文定位为 empirical study 但措辞暗示更高原创性。

**C5. 全文零图表** [R1 critical + R2 agree]
17 个表格，0 个 Figure。对 confidence/calibration 研究而言，缺少 selection curves、reliability diagrams、cost-effectiveness scatter 是严重呈现缺陷。Table 8 有 selection curve 数据但以表格呈现。**建议**：至少添加 3 个核心 Figure（selection curve、reliability diagram、cost-effectiveness）。

**C6. 成本分析需补充** [R1 critical, R2 rebut 为 warning — 存在分歧]
Section 6 称 SJ 额外成本 "negligible (O(N²) set comparisons vs. O(N) LLM forward passes)"，但 LP 可在 greedy decode（1 pass）上工作，SJ 需 N≥8 pass。**R1 立场**：将 8-16× 推理开销描述为 "negligible" 是系统性误导。**R2 立场**：在 TTS 语境（同 N 下比较）内论文陈述准确，LP@N=1 vs SJ@N=8 混淆了 selective prediction 与 TTS。**共识**：需补充 cost-effectiveness 分析（F1 gain per unit compute）。

### Should-Fix

**W1. 未探索 signal combination** [R1+R2 共识]
Section 5.8 证明 SJ 和 LP 互补（Δρ=0.14），却未尝试 α·SJ+(1-α)·LP 线性组合。

**W2. 标题与核心发现不匹配** [R2 critical → R1 rebut 降为 warning]
"Log-Probability Is All You Need?" 暗示 log-prob 可能足够，但核心发现是 SJ 显著优于 log-prob。R1 认为问号修辞反问可接受，最终定为 warning。**建议**：改为 "Beyond Log-Probability: ..." 或类似。

**W3. 单一 prompt 模板** [R1 提出，R2 agree]
未提及 prompt 变体。LLM-based IE 输出格式直接影响 set-based 指标。**建议**：appendix 给出完整 prompt，讨论 format 影响。

**W4. 统计检验不系统** [R1 提出，R2 部分 agree]
核心比较（Table 4/5 cross-dataset/cross-model）无 bootstrap CI，3 seed std 不替代正式统计检验。p-value 极小部分弥补但不充分。

**W5. SJ 失败案例分析不足** [R1 提出，R2 部分 rebut]
SJ ρ 最佳也仅 0.42-0.51。Section 5.11 inverted-U 提供统计层面分析，但缺实例级 case study（高 SJ 低 F1 / 低 SJ 高 F1 的具体模式）。

**W6. "Diagnostic framework" 过度包装** [R2 提出，R1 agree]
标准消融技术（F1 分桶、component 分解、stratification）不构成可复用 framework。**建议**：降格为 "diagnostic analysis"。

**W7. 未讨论 trained approaches 作为 upper bound** [R2 提出，R1 部分 agree]
Scope 限定为 training-free signals 合理，但 Related Work 应更充分讨论 verifier/reward model 等 trained approaches。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致：
1. **Overall 评分**: 3/5 (Findings)，Main 偏弱
2. **模型规模不足**: 仅 8B 模型不支撑普适性主张
3. **RE 单数据集**: "Universal bottleneck" 需降级
4. **零图表**: 严重影响可读性和说服力
5. **相关工作遗漏**: 5 篇核心文献必须补充
6. **Signal combination**: 已证明互补性但未尝试组合
7. **"首个系统比较"**: 需限定为 "for LLM-based structured IE"
8. **Diagnostic framework**: 降格为 "diagnostic analysis"

## Reviewer Divergence

| 问题 | R1 立场 | R2 立场 | 最终定级 |
|------|---------|---------|----------|
| 成本分析 | Critical（系统性误导） | Warning（TTS 语境下准确，需补充分析） | Critical（保守取高，但记录分歧） |
| SJ 失败分析 | 完全缺失 | Section 5.11 部分覆盖 | Warning（缺实例级分析） |
| 优先级排序 | 模型规模 > 成本分析 > 零图表 | 相关工作 > RE 数据集 > 新颖性 | 均为 critical |
| EM baseline | 合理（SC 原始实现） | Straw man | Info（R1 论证更充分） |

---

## Questions（需作者澄清）

1. 是否计划增加 >30B 或 <3B 模型实验？如不可行，如何限定当前结论的适用范围？
2. Table 16 entity count 6+ 时 SJ ρ 降至 0.34 的原因是什么？
3. SJ 的 similarity kernel 是否考虑过其他选择（edit distance、embedding cosine）？选择 token-level overlap 的理由？
4. Section 5.8 发现 SJ 和 LP 互补后，是否尝试过任何形式的组合？
5. 如何回应 CISC (Huang et al. 2025) 发现 "最 calibrated 的方法反而最无效" 与本文结论的张力？

---

## Missing References

1. **Guo et al. 2017** — On Calibration of Modern Neural Networks (ICML) — ECE 定义来源
2. **Snell et al. 2024** — Scaling LLM Test-Time Compute Optimally (ICLR 2025) — TTS 核心工作
3. **Aggarwal et al. 2023** — Adaptive-Consistency (EMNLP 2023) — N-scaling 相关
4. **Huang et al. 2025** — CISC: Confidence Improves Self-Consistency (ACL Findings 2025) — 挑战本文解读
5. **传统 IE confidence 文献** — CRF 边际概率、span-level confidence、MC-dropout uncertainty

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Overall Assessment

**评分**: 3/5 (Findings) — 两位 Reviewer 完全一致
**Director Scale**: 3.5/6 (Borderline Reject / Weak Accept for Findings)
**置信度**: 4/5

**定位判断**: Findings 可接受，Main 不足。论文的实用价值（practitioners 的 confidence signal 选择指南）适合 Findings 定位，但 6 个 critical 问题（模型规模、相关工作、RE 数据集、方法新颖性、零图表、成本分析）共同削弱了当前版本的竞争力。

**核心障碍**（按优先级）:
1. 模型规模单一 — 普适性主张无法成立
2. 相关工作遗漏 — 5 篇核心文献缺失严重损害可信度
3. RE 证据不足 — "Universal bottleneck" 仅单数据集支撑
4. 零图表 — calibration 研究无图不可接受
5. 方法新颖性有限 — SJ 是自然迁移，缺 kernel 消融
6. 成本分析 — 需补充 cost-effectiveness

**修改建议优先级**:
- P0（决定性）: 补充相关工作 + 添加核心图表 + 降级 "establish"/"universal" 措辞
- P1（强烈建议）: 增加 ≥1 个非 8B 模型 + 增加 ≥1 个 RE 数据集 + 补充 cost-effectiveness 分析
- P2（改善质量）: signal combination 实验 + prompt sensitivity + 失败案例分析 + bootstrap CI

---

## Detailed Comments

### Section 1 (Introduction)
- "establish best practices" 措辞过强，改为 "investigate" 或 "examine"
- 缺少 Snell et al. 2024 (TTS) 和 Guo et al. 2017 (ECE) 引用

### Section 3 (Method)
- Eq.(1) SJ similarity kernel 的具体实现分散在多处，建议集中说明
- 缺少 kernel 选择的动机说明和消融

### Section 4 (Experimental Setup)
- 未给出完整 prompt 模板
- 仅 T=0.7 和 T=1.0 两个温度点（R1 认为足够，R2 认为偏少）

### Section 5 (Results)
- Table 8 selection curve 数据应可视化为 Figure
- Table 16 entity count 6+ ρ 下降未解释
- Section 5.9 "universal bottleneck" 需降级措辞或增加数据集
- Section 5.11 inverted-U 缺实例级 case study

### Section 6 (Discussion)
- 成本分析需区分 TTS 内比较 vs 跨范式比较
- 补充 F1 gain per unit compute 分析
- "Diagnostic framework" 降格为 "diagnostic analysis"

### Section 7 (Limitations)
- 需明确讨论模型规模限制的影响
- 需讨论 trained approaches 作为 upper bound

### Related Work
- 补充 5 篇遗漏文献
- 讨论传统 IE confidence 或说明排除理由
- 讨论 CISC 与本文结论的张力

### Format
- Abstract 有未解析引用标记（"?"）
- 全文需添加至少 3 个核心 Figure
