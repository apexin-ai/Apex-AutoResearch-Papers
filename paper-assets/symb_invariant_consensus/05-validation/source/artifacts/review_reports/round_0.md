---
round: 0
overall_score: 2.5 - Borderline Findings (Resubmit next cycle)
timestamp: 2026-05-17T17:54:16.039955+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 1
**项目**: symb_invariant_consensus
**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)
**日期**: 2026-05-17
**Reviewer 配置**: R1（方法+实验）+ R2（新颖性+相关工作）

---

## Summary

论文研究 self-extracted symbolic constraints（FOL formalization + MAX-SAT aggregation）能否改善 LLM majority voting (Self-Consistency)。核心发现是 "capability trap"：模型自身能力限制了约束质量，导致 self-extracted SICA 在大部分条件下无法超越 SC。论文定义了 C0-precision 诊断框架并给出部署建议。

---

## Strengths

1. **研究问题有实际意义** — Practitioners 确实需要知道何时值得为 SC 增加 symbolic aggregation overhead [R1, R2 共识]
2. **Constraint ablation 设计精巧** — Table 2 的 MAX-SAT ≡ count-only ≡ random-weight（803/804 agreement）干净地验证了 constraints 无区分力 [R1]
3. **Capability trap 概念框架清晰** — Diversity vs quality tradeoff 叙事连贯 [R1, R2]
4. **Overhead analysis 务实** — 报告 wall-time 和 cost multiplier，对 practitioner 有参考价值 [R1]
5. **Negative result paper 结构完整** — Motivation → Method → Evaluation → Failure analysis → Diagnostic 逻辑线条清楚 [R1, R2]

---

## Weaknesses (Critical — 影响接收决定)

### W-C1: Method Section Stage 3 完全未描述 [R1-N1, R2 AGREE]
- `sat(a, c_{i,j}) ∈ {0,1}` 的实现方式未说明：LLM 调用？FOL solver model checking？字符串匹配？
- 这是 pipeline 核心步骤，直接决定 constraint precision 度量方式
- 如果 sat() 由 LLM 完成，overhead 分析 (Table 4) 漏算 O(|C|·|A|) 次调用
- **影响**: 方法不可复现，整个 precision 分析的度量基础不明

### W-C2: 大部分实验严重 underpowered [R1-N2, R2 强烈 AGREE]
- Table 1 的 11 行中 8 行 n≤60
- McNemar's test 在 n=60 时检测 3-5pp 差异的 power 仅约 15-20%
- 论文从未报告 power analysis
- 核心贡献是 negative result，无法排除 Type II error（"no significant effect" ≠ "no effect"）
- **影响**: 论文的 negative conclusion 的统计基础不成立

### W-C3: Oracle/upper-bound 实验完全缺失 [R1-N6, R2 AGREE 并更正自身]
- 论文声称 capability trap 根源是 self-extracted constraints precision ≈ 0.50
- 未通过 gold FOL constraints 验证："好的 constraints 是否真能帮 MAX-SAT 超越 SC？"
- 无法区分 H1（self-extracted constraints 太差）vs H2（MAX-SAT 框架本身无效）
- FOLIO 原始数据集带 gold FOL 标注，此实验完全可行
- **影响**: 论文的整个 "capability trap" 因果叙事缺少关键控制实验

### W-C4: 与 Huang et al. (ICLR 2024) 严重 novelty 重叠且未引用 [R2-N1, R1 AGREE]
- "LLMs Cannot Self-Correct Reasoning Yet" 已证明 LLMs 在无外部反馈时无法可靠自我纠正
- "Capability trap" 本质上是 correlated error problem 在 symbolic constraint extraction 场景的特化
- 论文未引用、未区分、未讨论增量
- R1 补充：SICA 引入了 FOL+MAX-SAT 结构化中间层，这是可论证的差异点，但论文需要明确 position
- **影响**: 核心 novelty claim 可能已被覆盖

### W-C5: 关键相关工作大面积缺失 [R2-N2, R1 AGREE 并修正]
- 缺失：Huang et al. 2024、"Two Failures of Self-Consistency" (EMNLP 2024)、"Self-Consistency Falls Short" (TACL 2025)、"Beyond Majority Voting" (2025)、"Reasoning Aware Self-Consistency" (NAACL 2025)
- R1 修正：FOLIO 原始论文 Han et al. 2022 实际已被引用；实际引用量 ~30 篇（非 R2 初评的 ~18 篇）
- 但 SC 失败模式、self-correction 局限性、aggregation 替代方法三个子话题完全空白
- **影响**: 审稿人会认为对领域 landscape 理解不充分

### W-C6: "18 experimental conditions" 无法验证 [R1-N3, R2 AGREE]
- Table 1 仅 11 行，最大合理拆分后为 13 个
- 达到 18 需将 n=60 pilot 的子域各算独立条件（n≈20/domain）
- 进一步恶化 W-C2 的 power 问题
- **影响**: 核心数字不透明，meta-level 分析自由度存疑

### W-C7: Introduction 列出 Mistral-7B 但全文无结果 [R1-N4, R2 AGREE]
- Section 1 L59 列出 5 个 model families 含 Mistral-7B
- 实际实验中无 Mistral 数据
- 明显的 draft 残留错误
- **影响**: 损害论文可信度，暗示结果可能被选择性删除

### W-C8: Abstract Δ 范围与 Table 1 矛盾 [R1-N5, R2 AGREE]
- Abstract: "−3.3pp to +2.0pp"，Table 1: StrategyQA Δ=+3.33pp
- 事实性错误
- **影响**: 对论文其他数字准确性产生系统性怀疑

### W-C9: Capability Trap 概念独立贡献不清晰 [R2-N3, R1 部分 AGREE]
- 四个子组件单独来看均非新洞察
- 组合增量主要是量化（阈值数字），但 n=30-60 样本量不足以支撑精确阈值
- R1 归因为 soundness 问题（量化基础不扎实），R2 归因为 novelty 问题（概念非新）
- **影响**: 核心 framing 需要在已有知识之上提供更清晰的增量

---

## Weaknesses (Warning — 影响评分但不一票否决)

1. **Constraint extraction prompt 完全缺失** — 核心方法环节无法复现 [R1-W1, R2 AGREE]
2. **Temperature τ 未指定** — 影响 C0 和 SC baseline 强度 [R1-W2, R2 AGREE]
3. **LLaMA-8B 行缺少绝对 accuracy** — 无法判断 Δ 的实际意义 [R1-W3, R2 AGREE]
4. **Confidence intervals 未展示** — negative result paper 中 CI 比 p-value 更重要 [R1-W4, R2 AGREE]
5. **Constraint precision 分析仅 Qwen-14B** — precision>0.6 阈值的泛化性未验证 [R1-W5, R2 AGREE]
6. **C0 diagnostic 贡献被高估** — Pearson r=0.05 (p=0.84) [R1-W6; R2 部分 REBUT: C0 作为 screening step (specificity 1.0 at C0<5%) 可能仍有诊断价值]
7. **全文零 figure** — 11 页实证论文无任何可视化 [R1-W7, R2 AGREE]
8. **"5 model families" 计数歧义** — Qwen within-family scaling 不应算独立 family [R1-W8, R2 AGREE]
9. **Self-limitation framing 尴尬** — 自限后发现不 work，practical recommendation 本质是 "别用此方法" [R2-W2, R1 部分 AGREE]

---

## Reviewer Consensus [AGREE]

以下 critical 问题两位 Reviewer 完全一致：
- Oracle 实验缺失（论文中确认不存在，R2 撤回原评）
- 实验 underpowered + power analysis 缺失
- Huang et al. (ICLR 2024) 未引用
- Method Stage 3 描述缺失
- 内部矛盾（Mistral-7B、Δ 范围）
- 条件数 claim 不可验证

**归因共识**: 论文同时存在 novelty 定位问题（R2 侧重）和 soundness/rigor 问题（R1 侧重），两者独立、需同时修复。

---

## Reviewer Divergence [REBUT]

**W6 (C0 贡献价值)**:
- R1：C0 与 SICA 增益的相关为零 (r=0.05)，作为 "contribution" 不成立
- R2：C0 作为 screening step (C0<5% → degeneration, specificity 1.0) 可能仍有诊断价值，问题在于论文将其包装为 "predicts benefit" 而非 "screens failure"
- **判定**: 分歧在程度而非方向。建议 Research Director 将 C0 从 "contribution" 降格为 "observation"，或提供更多 screening 价值的实证。

---

## Questions (需作者澄清)

1. sat(a, c_{i,j}) 的具体实现是什么？如果是 LLM 调用，overhead 需重新计算
2. 所有实验使用的 temperature τ 具体是多少？不同实验是否一致？
3. 如何从论文数据得到 "18 conditions"？请列出完整条件表
4. Mistral-7B 实验是否已做但被删除？如是，原因是什么？
5. K=12 的选择依据是什么？
6. ~31% multi-candidate rate 的计算基础（哪些条件、哪些问题子集）？

---

## Missing References

1. **Huang et al. (ICLR 2024)** "Large Language Models Cannot Self-Correct Reasoning Yet" — 直接上位概念
2. **"Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs" (EMNLP 2024)** — SC 失败模式
3. **"Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems" (TACL 2025)** — SC 局限性
4. **"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information" (2025)** — aggregation 替代方法
5. **"Reasoning Aware Self-Consistency" (NAACL 2025)** — quality-aware SC 变体

注：R2 初评中列出的 FOLIO 原始论文（Han et al. 2022）经 R1 核实已被引用（bibkey: han2022folio）。

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求。本轮未启用外部审稿。

---

## Overall Assessment

**评分: 2.5 (Borderline Findings)**

**置信度**: 高 (4/5) — 两位 Reviewer 独立审稿后经交叉验证达成高度一致

**理由**:
- 研究问题有价值，但执行存在结构性缺陷
- 9 个 critical-level 问题中，至少 4 个是 "可修复但需要大量工作"（oracle 实验、powered experiments、related work、method 描述），至少 3 个是 "低成本修复"（Mistral 残留、Δ 矛盾、条件数说明），2 个需要 re-framing（novelty positioning、capability trap 贡献）
- 当前形态距离 Findings 接收标准（3.0）仍有差距
- 修复路径存在但工作量大：补 oracle 实验 + 扩大 powered 实验 + 完善 method + Related Work + 修复内部矛盾

**与 EMNLP 2026 ARR 评分对照**:
- 2.5 = Borderline Findings（需大幅修改，可在下一周期完成）
- 两位 Reviewer 最终评分均为 2.5，完全一致

**建议**: Resubmit next cycle。核心实验基础（尤其 oracle + powered tests）补齐后有 Findings 潜力，但需要一个完整修改周期。

---

## Detailed Comments (按优先级排序的修改建议)

### Priority 1: 补实验（决定论文能否升级为 Findings）
1. **Oracle experiment on FOLIO** — 用 gold FOL annotations 跑 SICA pipeline，验证 H1 vs H2
2. **Power up 至少 3 个 model×domain 到 n≥200** — 确保 negative results 有统计效力
3. **报告 power analysis** — 为所有条件报告 MDE (minimum detectable effect)

### Priority 2: 补方法描述（影响复现性评分）
4. **Section 3 Stage 3**: 完整描述 sat() 实现 + 示例
5. **Appendix**: Constraint extraction prompt 模板 + 示例
6. **明确报告所有 τ 值和 K 选择理由**

### Priority 3: Related Work + Framing（影响 novelty 评分）
7. **引用并区分 Huang et al. 2024** — 论证 FOL+MAX-SAT 结构化中间层的增量
8. **补充 SC 失败模式 + aggregation 替代方法文献**
9. **降低 capability trap 的 "新概念" 调门** — 定位为已知现象的系统性量化验证
10. **C0 从 "contribution" 降格为 "observation"** 或提供 screening 实证

### Priority 4: 修复内部矛盾（低成本但影响可信度）
11. **统一 Introduction/Setup 模型列表** — 删除 Mistral-7B 或补数据
12. **更新 Abstract Δ 范围** — 核对所有条件
13. **明确列出所有实验条件定义**（Table 或 Appendix）
14. **增加 2-3 个 figure**（pipeline 图、precision 分布、C0 vs Δ scatter）
