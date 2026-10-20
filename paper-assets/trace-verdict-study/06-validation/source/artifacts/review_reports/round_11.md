---
round: 11
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T18:11:11.757116+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 16 (Fresh Review)

**论文**: Complete Execution Traces Degrade SFT-Based Verdict Prediction: A Diagnostic Signal Analysis
**Venue**: EMNLP 2026 (Long Paper, ARR May cycle)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性/实验/统计 | R2: 新颖性/Framing/Related Work）

---

## Summary

本文研究 execution trace 表示对 SFT-based verdict prediction（判断测试 pass/fail）的影响。核心发现：完整 execution traces（77–82%）反而不如紧凑的 exception events（≥99.33%），跨 4 个模型（1.5B–13B, 3 架构家族）一致复现，gap 达 18pp+。通过 gradient masking 实验将 degradation 归因于 content quality（≥96%）而非 gradient dilution（≤4%）。提出 two-tier signal hierarchy 和 ~512 token tail-truncation 阈值。

---

## Strengths

1. **实验设计系统全面**：7 种 trace 格式 × 4 模型 × 3 架构家族 × 多 seed，辅以 gradient masking、label-only loss、marker removal、cross-dataset transfer、truncation sweep、regex baselines、zero-shot/few-shot、frontier model comparison、calibration analysis，构成了罕见的诊断深度 [R1+R2 AGREE]
2. **核心 degradation 发现实验支撑极为充分**：18pp gap 跨 4 模型一致复现，non-overlapping CIs，即使在 clustered bootstrap 下核心 cross-tier claims 仍显著 [R1]
3. **Cross-dataset transfer 排除 overfitting**：HumanEval→MBPP 99.41%, MBPP→HumanEval 100.0%，near-zero transfer loss [R1+R2]
4. **Marker removal ablation 有效**：regex B5 collapse to 28.49% vs SFT retain 97.65%，69pp gap 证明 SFT 超越 format matching [R1]
5. **Confound 披露诚实**：Section 3.4 正确声明 forward-pass confound 和 label-only loss 的混淆变量 [R1]
6. **Reproducibility 高**：训练超参、GPU hours、data split 细节齐全；Appendix 21 页 [R1+R2]
7. **Calibration 分析**：ECE < 0.005 across 4 models，超越简单 accuracy 比较 [R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [CONSENSUS] 正文页数超限
- Conclusion 约 6–7 行溢出到 page 9，违反 EMNLP 2026 正文 8 页限制。ARR 格式检查可能 desk reject。
- **建议**：Figure 3 (training dynamics) 移入附录；或压缩 Related Work；或微调 spacing。

**MF-2** [CONSENSUS] CI 基准不一致 / 统计报告透明度
- 正文 Tables 1–3 用 Wilson CI (N=1,190)，clustered bootstrap (n_eff=119, CIs 宽 ~2.2×) 仅在脚注报告，3/80 borderline within-tier pairs 在 Holm-Bonferroni 校正后失去显著性。将更严格分析降级到脚注有 selective reporting 风险。
- 脚注说 dedup yields "0.00pp delta"，但 Appendix P 报告 "0.09pp delta"——数字矛盾。
- **建议**：正文明确标注 CI 类型；within-tier 比较提供 clustered p-values；修正数字矛盾。

**MF-3** [CONSENSUS] Abstract/Conclusion 中 gradient masking confound 的 hedging 缺失
- Section 3.4 正确声明 forward-pass confound，但 Abstract 和 Conclusion 用 "confirm" 而非 "suggest"，省略了 confound。"≥96% content quality" 隐含 gradient dilution 与 content quality 互斥——forward-pass attention 是未被量化的第三因素。
- **建议**：Abstract/Conclusion 将 "confirm" 改为 "suggest/indicate"；加入 forward-pass confound 限定语。

**MF-4** [DIVERGENCE] 核心发现的新颖性 / near-tautological concern
- **R2 (Must-Fix)**：exception events 结构性编码 verdict（有 exception=fail, 无=pass），SFT vs regex 增量仅 0.50pp，核心发现近似套义。
- **R1 (REBUT)**：核心贡献是 full trace degradation（-18pp），非 exception ceiling。Full trace 包含 exception 全部信息，理应 ≥ exception_only，但大幅低于——这不是 tautological。Marker removal (69pp gap) 和 cross-dataset transfer 证明 SFT 超越 format matching。
- **Director 判断**：R1 的 rebuttal 部分有效——exception ceiling 的结构性预期确实不构成核心贡献，但 full trace degradation 是 non-trivial 的。然而 R2 的 concern 也有道理：论文当前 framing 将 exception ceiling 作为 headline result，应转向 "complete traces hurt" 叙事。**降级为 Should-Fix**，条件：明确承认 exception/verdict 结构性对应，将核心贡献重心转向 full trace degradation 的 non-trivial 性。

**MF-5** [DIVERGENCE] 贡献过度宣称
- **R2 (Must-Fix)**：C1/C4 重叠，C2 证据弱（0.50pp），C3 在 CodeLlama 不成立。
- **R1 (REBUT)**：C1 是 what (empirical finding)，C4 是 why (mechanism)；C2 核心证据是 marker removal (69pp)；同意 C3 需限定。
- **Director 判断**：C1/C4 区分可保留但应 sharpen；C2 从 "genuine diagnostic patterns" reframe 为 "systematic quantification"；C3 加 "3/4 models" 限定。**维持 Should-Fix**。

### Should-Fix（影响评分但不一票否决）

**SF-1** [CONSENSUS] Two-pathway "descriptive" 限定在 Abstract/Conclusion 缺失。Discussion 说 "(not a causal model)" 但高可见位置未提及。

**SF-2** [CONSENSUS] Abstract 数据过载——10+ 具体数字，关键信息传达效率低。

**SF-3** [CONSENSUS] CodeLlama tail 条件 label-only loss 在 Figure 4 无视觉区分，cross-model 比较 confounded。

**SF-4** [CONSENSUS] DeepSeek VOTA seed 42 truncation failure (1/12 catastrophic) 暴露 VOTA 鲁棒性问题，应在 Limitations 讨论。

**SF-5** [CONSENSUS] Diagnostic ratio d 基于 5 点 (df=3) 的 r=0.949 不稳定，d=0 tail-truncated 达 93–97%，d 无法解释全部 variance。

**SF-6** [CONSENSUS] Cross-model 泛化声明偏强（4 models, max 13B, code-specialized），Conclusion 缺 hedge。

**SF-7** [CONSENSUS] CodeLlama loop_only 仅 +0.93pp (n.s.)，Two-tier C3 需加 "3/4 models" 限定。

**SF-8** [DIVERGENCE → Director 判定 Should-Fix] Verdict prediction 实用动机。R2 认为 Must-Fix；R1 认为 proxy task framing 可接受。Director: proxy task 有 *CL 先例（CRUXEval, NExT），不构成 rejection，但 Introduction 论证需加强。

**SF-9** [CONSENSUS] Single-seed baseline (no_trace, full_trace) 可靠性未系统讨论。

**SF-10** [DIVERGENCE → Director 判定 Should-Fix] 标题 "Degrade" 因果性。R2 认为缺因果证据；R1 认为 controlled comparison 足以支撑。Director: controlled experiment 中 accuracy 从 99.83% 降至 81.44%，"degrade" 用词合理，但 mechanism decomposition 的因果链需更谨慎。

---

## Questions（需要作者澄清）

1. Method section 报告 d 的 r=0.919 vs Discussion 报告 r=0.949——哪个是正确数值？差异来源是什么？
2. 脚注 1 说 dedup yields "0.00pp delta"，Appendix P 说 "0.09pp delta"——哪个正确？
3. Appendix P 说 duplicates "not due to representation compactness"，Section 2.2 说正是因为 "format collapses passing solutions into identical rows"——表述矛盾，请澄清。
4. Gap statistic 和 silhouette ≥0.74 的结果在哪里报告？Section 3.2 提及但未找到完整分析。
5. Label-only loss 在 CodeLlama 和 DeepSeek 上 collapse to 28.5%（2/4 models）——这是否表明该方法本身不稳定？请讨论。

---

## Missing References

R2 指出缺失 data pruning / Information Bottleneck / LIMA / curriculum learning 引用，但 R1 在交叉回应中纠正：**这些文献全部已在 Related Work Section 5 最后一段和 Discussion 中引用**（Tishby 2000, Guyon 2003, Zhou 2023, Paul 2021, Sorscher 2022, Bengio 2009）。R2 的 W4 为事实性错误，不纳入最终建议。

无新增遗漏引用。

---

## External Review (Stanford Agentic Reviewer)

未启用。

---

## Visual Layout Check（非评分项）

状态：**已完成** (0 critical, 2 warning, 4 info)

主要发现：
- **[warning]** Page 1–2 连续 2 页纯文本无 display item，Figure 1 直到 page 4 才出现（引用在 page 2）——建议前移
- **[warning]** Figure 1 float 延迟约 2 页（page 2 引用，page 4 出现）
- **[info]** Figure 2 尺寸偏小，轴标签接近可读性下限
- **[info]** Page 7 整页纯文本无视觉间隔
- **[info]** Page 21 附录末页约 40% 空白
- **[info]** Table 1 作为首个 display item 出现在 page 3

---

## Overall Assessment

**综合评分：3.0 / 5 — Findings**
**置信度：4/5**

| 维度 | R1 | R2 | Director |
|------|-----|-----|----------|
| Overall | 3.5 | 2.5 | 3.0 |
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 2.0 | 2.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |

**评分理由**：

实验执行质量在同类工作中属于高标准——4 模型 × 3 架构 × 多 seed × 多维度消融 × 统计检验 × calibration 分析，且 confound 披露诚实。核心 degradation finding（full trace -18pp vs exception_only）是 non-trivial 的，对 trace-based SFT pipeline 设计有实践指导意义。

但存在以下根本限制：(1) exception events 对 verdict 的结构性编码降低了核心发现的新颖性——这更接近已知 ML 原理（more features can hurt）在特定 domain 的 systematic quantification，而非 fundamental insight；(2) 正文页数超限是硬性违规；(3) Abstract/Conclusion 的 hedging 与正文不一致（confirm vs suggest）构成 overclaiming；(4) 统计报告将更严格分析降级到脚注；(5) 任务范围窄（verdict prediction on simple Python functions, max 13B）。

综合判断：实验深度足以支撑 Findings 接收；novelty 和 scope 限制 main conference 竞争力。修复 MF-1（页数）、MF-2（统计透明度）、MF-3（hedging 一致性）是提交前的硬性要求。

---

## Detailed Comments（按章节）

### Title
- "Degrade" 用词有 controlled comparison 支撑，可保留，但应确保正文因果链的 hedging 与之匹配。

### Abstract
- 数据过载（10+ 数字），建议精简至 2–3 个关键对比
- "confirming" → "suggesting"（gradient masking confound）
- 加入 "across code-specialized models (1.5B–13B)" 范围限定

### Section 1 (Introduction)
- 明确承认 exception events 与 verdict 的结构性对应关系
- 将核心贡献重心从 exception ceiling 转向 full trace degradation
- C2 从 "genuine diagnostic patterns" reframe 为 "systematic quantification"
- C3 加 "significant for 3 of 4 models tested" 限定

### Section 2 (Method)
- d 的 r 值需与 Discussion 统一（0.919 vs 0.949）
- 加强 proxy task 的 motivation（连接 CRUXEval/NExT 先例）

### Section 3 (Experiments)
- CI 类型明确标注（Wilson/unclustered 为主，clustered bootstrap 为 robustness）
- Within-tier 比较提供 clustered p-values
- Figure 4 CodeLlama 数据点用不同 marker 标注
- Label-only loss 2/4 models collapse 值得更明确讨论

### Section 3.4 (Density Decomposition)
- 正文 hedge 良好，需确保 Abstract/Conclusion 一致

### Section 4 (Discussion)
- "Descriptive two-pathway framework" 限定需在 Abstract/Conclusion 保持

### Section 5 (Related Work)
- 引用覆盖充分（经核实，R2 的 W4 为事实性错误）

### Section 6 (Conclusion)
- 页数溢出必须修复
- 加入模型规模和类型限制的 hedge
- "confirm" → "suggest"

### Limitations
- 增加 VOTA tokenizer-driven truncation 脆弱性讨论
- 明确哪些 core claims 依赖 single-seed 结果

### Appendix
- 96GB VRAM 模糊化以降低 de-anonymization 风险
- Appendix P 与 Section 2.2 表述矛盾需修正
- 0.00pp vs 0.09pp dedup delta 矛盾需修正