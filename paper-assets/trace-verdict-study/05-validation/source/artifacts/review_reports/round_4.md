---
round: 4
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T13:09:25.606065+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — trace-verdict-study Round 9 (Fresh Review)

**论文**: "Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction"
**Venue**: EMNLP 2026 (ARR May 2026)
**日期**: 2026-05-19
**Reviewer 配置**: R1（方法严谨性 + 实验有效性）+ R2（新颖性 + 完整性 + 写作质量）
**轮次**: Round 1 + 交叉回应，一轮收敛

---

## Summary

本文对 verdict prediction（判断测试是否通过）任务进行了首次系统性 trace component ablation，在 4 个模型（Qwen-7B/1.5B, CodeLlama-13B, DeepSeek-6.7B）、3 个架构家族、1.5B–13B 参数范围上评估了 7 种 trace condition。核心发现：exception events 单独达到 ≥99.83%（3/4 模型），而完整 trace 仅 82–88%。论文将差距近似分解为 information overload (~76%) 和 gradient dilution (~24%)，并通过 tail-truncation budget sweep 发现 ~500 token 的相变点。

---

## Strengths

**S1. 实验覆盖面和严谨性出色。** 4 模型 × 7 conditions × 多维度分析（cross-model, budget sweep, calibration, error overlap, cross-dataset, training dynamics）。exception_only 跨 4 模型的 0.56pp 极窄 band 是强有力的发现。Wilson 95% CIs、paired bootstrap ($B$=10,000)、McNemar 检验、multi-seed 方差均有报告。[R1 AGREE, R2 AGREE]

**S2. Training dynamics 分析提供了 mechanism-level 证据。** exception_only 在 50 步内收敛到 99.33% 并稳定，而 full_trace 全程在 82–89% 振荡（Figure 3）。这不仅报告终态数字，还展示了学习过程差异，为 "information density determines learning efficiency" 提供了直接经验证据。[R1 强调此为关键贡献; R2 认可其价值但指出输入长度差异 10× 使对比不完全公平]

**S3. Format marker ablation 巧妙回应 "trivial shortcut" 质疑。** nomarker 条件证明去除格式标记后仅降 ~2pp（97.65%），~91% 的信号是 semantic 的。这有效解决了 regex B5 (99.33%) 带来的 shortcut 担忧。[R1 R2 AGREE]

**S4. Cross-model budget sweep 定位信号窗口。** 4 模型 × 6 budget levels 的 tail-truncation 曲线一致展示 384→512 token 的 phase transition，cross-seed 验证（12 个 model×seed 组合全在 [93.6%, 98.2%] band 内）。[R1 R2 AGREE]

**S5. Limitations 诚实详尽。** 9 条限制，涵盖 seed variance、generator-evaluator overlap、self-familiarity bias、语言/数据集泛化等。学术自觉程度高于同类论文。[R1 R2 AGREE]

**S6. 统计基础设施完善。** Regex baseline 系列（6 条）、zero-shot/few-shot comparison、calibration analysis、error overlap（Jaccard）、deduplication sensitivity analysis。每个发现都有对照和 sanity check。[R1 R2 AGREE]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [critical] 核心发现的非平凡性（novelty）存疑 [R2-N1, R1 部分同意]**

Exception events 本身就是 runtime 的 fault indicator——有 exception = fail，无 exception = pass（包括 test assertion 产生的 AssertionError，覆盖 55.5% 的 silent logic errors）。"exception events predict verdict" 在概念上接近循环论证。SFT 相对 regex B4 的增量仅 6.22pp（去 marker 后 4.04pp），语义增量集中在 6/8 caught-exception boundary samples。

**R1 部分反驳**："more info → worse SFT" 和 training dynamics mechanism 非同义反复，量化 scale（18pp gap, 0.56pp cross-model band）不可从先验推导。

**Director 判断**：论文的 headline claim（"exception events are all you need"）确实接近预期，但 training dynamics mechanism 和 information density decomposition 有独立贡献。问题在于 framing——论文以一个 near-trivial finding 为核心，将更有 novelty 的 mechanism 分析作为次要贡献。需要重新排列贡献权重。

**MF2. [critical] Tier hierarchy (ae_only/loop_only) 仅 Qwen-7B 验证 [R1-N2, R2-W2→升级 AGREE]**

Contribution 4 声明 "Two-tier diagnostic hierarchy"，但 ae_only 和 loop_only 仅在 Qwen-7B 上测试。Discussion 直接建议了基于该 hierarchy 的 fallback design（"extract exception events first, resort to Tier 2 only when no exception is raised"），超出了单模型验证的证据范围。如果 ae_only 在 DeepSeek 上因 tokenizer truncation 退化（类似 VOTA），Tier 1 的"两个成员"可能缩减为仅 exception_only。

**两位 Reviewer 共识**：至少在 1 个非 Qwen 模型上补做 ae_only + loop_only，或将 Contribution 4 降格为 Qwen-7B observation。

**MF3. [critical] Verdict prediction 实际应用动机不清 [R2-N2, R1 大体同意]**

要获取 execution trace（sys.settrace）必须先运行测试，此时 test framework 已直接报告 verdict。Discussion 提到的三个应用场景（patch correctness prediction, flaky test detection, offline trace analysis）无任何实验验证或具体 use case 分析。

**R1 缓解论点**：作为分析性工作，verdict prediction 是干净的 testbed（binary classification, 无 generation 噪声），方法论发现有迁移价值。

**Director 判断**：这主要影响 Excitement 而非 Soundness。论文需选择一条路径：(A) 论证至少一个具体下游应用 或 (B) 明确重新定位为 "understanding what code LLMs learn from traces" 的分析性工作。当前两头不靠。

### Should-Fix（影响评分但不一票否决）

**SF1. [warning] "Richer traces actively hurt" 的 claim 被 truncation artifact 部分混淆 [R2-N3, R1 部分反驳]**

full_trace 和 VOTA 的低性能部分由 2048-token context window 截断导致（DeepSeek VOTA 91.7% 样本被截断；未截断 100% vs 截断 83.04%）。R1 提供反驳：Qwen full_trace no_limit 仍仅 81.76%（截断压力较小）、tail-2048 残余 gap 2.52pp、label_only 实验排除纯截断解释。

**Director 判断**：Information overload 是真实效应，但论文未充分区分 truncation-driven degradation（DeepSeek VOTA）和 genuine information overload（Qwen 残余 gap）。Contribution 3 的 claim scope 需缩窄，或补充 8k+ context 实验以 definitively 分离。

**SF2. [warning] 24%/76% 因果分解 claim 过强 [R1-W2, R2-W1, 双方 AGREE]**

label_only 改变的不仅是 gradient signal，还改变了 effective gradient norm、隐式正则化等。正文 §3.4 有 caveats 但 Abstract/Conclusion 未充分传达。且仅 Qwen-7B 单模型 3-seed 验证，跨模型未测。

**SF3. [warning] Wilson CI 在 49% 重复数据上的报告 [R1-N1, R2 REBUT 降级]**

exception_only 测试集 48.99% 重复（607 unique / 1190 total）。论文已在脚注 1、Appendix F/O 讨论，去重后 accuracy 0.00pp 变化。R2 论证核心结论（18+pp gap）不受影响，建议降级为报告规范问题。

**Director 判断**：同意 R2 的降级判断——这不影响核心结论，但正文 Table 1 应补充去重后 CI，bootstrap 建议考虑 problem-level resampling。

**SF4. [warning] DebugBench cross-dataset validation 证据不足 [R1-W4, R2 AGREE]**

no_trace baseline 已达 96.71%（仅 3.29pp headroom），exception_only vs VOTA 差距 0.23pp 在 $N$=426 下不显著。Introduction 和 Abstract 中 "100% on DebugBench" 的呈现过强。

**SF5. [warning] Figure 3 (Training Dynamics) 图例与 caption 不一致 [R2-W3, R1 AGREE]**

图例标注 "Full Trace" 但 caption 写 "Full-trace with label-only loss (red, dashed)"。这两个是不同条件（full_trace 81.76% vs label_only 85.94%），会误导读者。

**SF6. [warning] Figure 2 (Cross-Model Gap) x 轴混淆模型家族 [R2-W4, R1 AGREE]**

x 轴 "Model Scale" 将不同家族模型映射到连续 scale 维度，6.7B 处有两个不同家族。建议改用分组柱状图或标注模型名称。

**SF7. [warning] Abstract 信息密度过高 [R2-W5, R1 AGREE]**

Abstract 含 8+ 个具体数字。建议精简至 3-4 个关键数字，传达 narrative arc 而非数据密度。

**SF8. [warning] CodeLlama tail-2048 collapse (41.8%) 未诊断 [R1-W3, R2 AGREE]**

论文仅归因 "LoRA long-sequence instability" 并排除，无 training loss curve 或 gradient norm 诊断。这同时影响 24%/76% 分解的可信度（label-only loss 在某些配置下不可用）。

**SF9. [warning] 标题 "X Is All You Need" 审美疲劳 [R2-W6, R1 AGREE]**

双方均建议更精确的标题。备选："Exception Events Suffice for Trace-Based Verdict Prediction"、"Less Is More: Why Exception Events Outperform Complete Traces"。

### Minor Issues（不影响接收）

- Table 1 caption 过长（>10 行），建议精简
- Algorithm 1 assertion-point extraction 的 expected value 获取方式不清晰
- bib key 与 year 不匹配（qwen2025coder → year=2024）
- DeepSeek seed 123 报告方式：R1 认为应用 3-seed mean，R2 认为当前披露充分（轻度分歧）
- Generator-evaluator overlap：已在 Limitations 讨论，DebugBench 部分缓解，低严重性

---

## Questions to Authors

Q1. ae_only 和 loop_only 未在 DeepSeek/CodeLlama 上测试的原因？如果 ae_only 在 DeepSeek 因 tokenizer truncation 表现很差，是否会改变 tier hierarchy？

Q2. 是否考虑过在更长 context window (8k+) 下重跑 full_trace，以分离 truncation artifact 和 genuine information overload？

Q3. CodeLlama tail-2048 + label-only loss 崩塌到 41.8% 的 training loss curve 是什么样的？

Q4. 对于不使用 assert 而使用 print/return 比较的测试，exception_only 表现如何？

Q5. 论文应定位为 task-driven（verdict prediction 有实际应用）还是 analysis-driven（理解 code LLMs 如何从 traces 学习）？当前定位模糊。

---

## Missing References

1. **Code agents with execution feedback**: SWE-agent (Yang et al., 2024), OpenHands (Wang et al., 2024) — 使用 execution feedback 进行 iterative debugging，与 "exception as diagnostic signal" 直接相关
2. **Test result parsing / build log analysis**: LogParse 系列 — 工业界使用 log parsing 判定 test verdict
3. **Selective context / input pruning**: LLMLingua (Li et al., 2023), Compresso — 与 "information density" 主题密切相关
4. **Test oracle survey**: Barr et al. (2015) "The Oracle Problem in Software Testing: A Survey" — 论文核心发现本质上是 "test oracle 信号比 execution trace 更有信息量"
5. **Mutation testing**: Equivalent mutant problem 与 DebugBench 的 single-point mutations 直接相关

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未配置（项目未启用外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: 未完成（dispatch 失败，论文 PDF 路径配置问题——期望 `paper/main.tex` 但实际路径为 `docs/paper/main.tex`）。R2 格式合规检查确认：正文 ≤ 8 页 ✓、Limitations ✓、Ethics Statement ✓、匿名 ✓、[review] option ✓、ARR Checklist ✓。

---

## Reviewer Consensus [AGREE]

1. **Tier hierarchy 需跨模型验证** — Contribution 4 仅 Qwen-7B 证据不足 [R1-N2, R2-W2→升级]
2. **24%/76% 分解 claim 需加限定** — Abstract/Conclusion 应标注 "on Qwen-7B" + "approximate" [R1-W2, R2-W1]
3. **DebugBench 验证力不足** — ceiling effect 使之无法独立验证 exception dominance [R1-W4, R2-AGREE]
4. **Claim scope 需限定** — 单语言(Python)、LLM 生成代码、≤13B 模型 [R1, R2]
5. **Abstract 需精简** — 数字过密，应保留 3-4 个关键数字 [R2-W5, R1-AGREE]
6. **Figure 3 图例/caption 不一致需修正** [R2-W3, R1-AGREE]
7. **标题建议更换** — "X Is All You Need" 引起审美疲劳 [R2-W6, R1-AGREE]

## Reviewer Divergence [REBUT]

1. **核心发现 novelty** — R2: near-tautological (Excitement 2/5); R1: training dynamics mechanism 有独立贡献 (Excitement 3/5)。Director 倾向 R2：headline finding 接近预期，但同意 R1 所述 mechanism 分析有价值
2. **应用动机** — R2: Must-Fix 级别缺陷; R1: 分析性贡献有独立价值，verdict prediction 作为 testbed。Director 倾向 R2：需明确定位
3. **Truncation confound** — R2: "richer traces hurt" 主要是 truncation artifact; R1: label_only 实验和 tail-2048 残余 gap 证明 information overload 是真实效应。Director：两者都对——需区分 truncation-driven 和 genuine overload
4. **Wilson CI 严重性** — R1: Must-Fix; R2: Should-Fix（论文已充分披露，核心结论不受影响）。Director 倾向 R2：降级为 Should-Fix

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**Confidence: 4/5**

| 维度 | 综合评分 | R1 | R2 |
|------|----------|----|----|
| Soundness | 3/5 | 3/5 | 3/5 |
| Excitement | 2.5/5 | 3/5 | 2/5 |
| Reproducibility | 4/5 | 4/5 | — |
| Overall | 3.0 | 3.5 | 3.0 |

**评分理由**：

这是一篇执行质量高的实证研究——实验覆盖面宽、统计报告严谨、Limitations 诚实。但有三个结构性问题限制了其会议级别的竞争力：

1. **Novelty 瓶颈**：headline finding（exception events predict verdict）在概念上接近预期。更有 novelty 的发现（information density mechanism, training dynamics, "more info hurts SFT"）被呈现为次要贡献，framing 倒置。
2. **Motivation gap**：verdict prediction 的实际应用场景不清晰（有 trace 即有 verdict），论文在 task-driven 和 analysis-driven 定位之间摇摆。
3. **Evidence scope 与 claim scope 不匹配**：Tier hierarchy 仅单模型、24%/76% 分解仅单模型、cross-dataset 验证被 ceiling effect 削弱、"richer traces hurt" 部分混淆于 truncation。

如果修订中能完成以下改动，论文有潜力达到 3.5 (Borderline Conference)：
- 重新框定核心贡献：以 information density mechanism 为中心
- 明确论文定位（analysis-driven）
- 至少 1 个非 Qwen 模型的 ae_only/loop_only 验证
- 区分 truncation-driven 和 genuine information overload
- 缩窄 claim scope 至 evidence 支撑范围

当前版本适合 **Findings**：solid empirical work，但 novelty 和 motivation 不足以支撑 main conference 接收。

---

## Detailed Comments（逐节）

### Title
"Exception Events Are All You Need" 审美疲劳 + claim 过于绝对。建议更换。

### Abstract
数字密度过高（8+ 个具体数字）。24%/76% 需标注 "on Qwen-7B"。DebugBench 100% 的呈现需加 "narrow margins" caveat。建议精简至核心 narrative：exception events suffice → more info hurts → mechanism (training dynamics + density decomposition)。

### Introduction
Contribution 4（Tier hierarchy）应降格或补充跨模型证据。DebugBench 证据权重应降低。"≥99.83% on three of four models" 和 DeepSeek 3-seed mean 96.58% 的并列呈现是合理的。

### Method (§2)
数据集构造清晰。VOTA 提取有 Algorithm 1 伪代码（此前 round 缺失，现已补充）。但 assertion-point extraction 的 expected value 获取方式仍需补充。Generator-evaluator overlap 可在此处更早提及。

### Experiments (§3)
Table 1/2 的统计报告严谨。§3.2 component ablation 的单模型限制是核心弱点。§3.4 information density decomposition 有 caveats 但传播到 Abstract/Conclusion 时被弱化。§3.5 budget sweep 是论文最强部分之一。

### Discussion (§4)
"Tier hierarchy: practical implications" 段的 fallback design 建议超出单模型证据。"Exception events capture test verdict signals, not just crashes" 段落有效但也暴露了 near-tautological 问题——test assertions generate exception events，所以 exception_only 本质上编码了 test oracle 的判决。

### Related Work (§5)
54 条引用，6 个方向，覆盖面可接受但缺 5 个方向（code agents, log parsing, selective context, test oracle survey, mutation testing）。无虚假引用。

### Conclusion
与 Abstract 类似的 data density 问题。"information density, not information quantity" 是好的 takeaway message。

### Limitations
异常详尽（9 条），远超同类论文。这是一个 strength。

### Appendix
内容丰富（training details, VOTA algorithm, full results, tokenizer analysis, irreducible samples, exception type breakdown, trace length ablation, calibration, error overlap, DebugBench, robustness, training dynamics, dedup stats, regex baselines, zero-shot comparison）。部分 Table caption 引用了 main text section 编号而非 Appendix label。

### Figures
- Figure 1: 概览图，清晰
- Figure 2 (Cross-Model Gap): x 轴混淆模型家族，需修正
- Figure 3 (Training Dynamics): 图例/caption 不一致，需修正
- Figure 4 (Budget Curve): 清晰，cross-model 一致性展示得好
- Figure 5 (Calibration): 清晰
- Figure 6 (Error Overlap): 清晰

### Format Compliance
正文 ≤ 8 页 ✓ | Limitations ✓ | Ethics Statement ✓ | 匿名 ✓ | ACL [review] ✓ | ARR Checklist ✓ | 无代码/数据链接暴露 ✓