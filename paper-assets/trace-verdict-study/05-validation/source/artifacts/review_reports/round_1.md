---
round: 1
overall_score: weak reject
timestamp: 2026-05-16T05:31:45.952749+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告 — Round 5

**论文**: Exception Events Are All You Need: Cross-Model Fault Detection for Verdict Prediction
**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**审稿编排**: 2 Reviewers（R1: 方法严谨性 + 实验有效性；R2: 新颖性 + 完整性 + Related Work）
**轮次**: Round 1，1 轮收敛（交叉回应全部 [AGREE]，无 [REBUT]）

---

## Summary

本文对 verdict prediction（判定测试是否通过）中 execution trace 的各组件进行系统消融，在 Qwen-2.5-7B 和 DeepSeek-6.7B 上评估 7 种 trace 表示。核心发现：exception events 单独达到近完美准确率（Qwen 99.83%），多组件表示 VOTA 在较弱模型上反而退化 14.96pp。论文提出 gradient dilution (26%) vs information overload (74%) 的分解框架，建立了两层诊断信号层级（Tier 1: exceptions/assertions ≥99.8%; Tier 2: loop compression 85.6%）。

---

## Strengths

1. **系统性消融设计**：7 个 trace 条件构成了完整的信号维度探索空间（no_trace → full_trace），Figure 1 pipeline 清晰，每个条件定义明确。这是该领域首次针对 verdict prediction 的组件级消融。

2. **统计方法选择合理**：paired bootstrap resampling (B=10,000)、McNemar test、Wilson CI 的使用超越了多数同类工作。Irreducible sample analysis（Appendix §B.5，追溯到 GeneratorExit 的 Python 迭代器协议）展示了深入的实验理解。

3. **极高的实验透明度**：13 个附录覆盖 per-class breakdown、training dynamics、deduplication stats、regex baselines、calibration、trace length ablation 等。特别是 Appendix §B.10 的 regex baseline 分析——虽然结果反而削弱了核心发现，但体现了科学诚实。

4. **Information density decomposition 概念清晰**：通过 label-only loss masking 将 train-time 信号质量与 inference-time 输入质量分离，设计简洁有方法论参考价值。

5. **Limitations 诚实全面**：主动列举了单数据集、2 模型、seed 依赖、循环依赖等主要局限，在同类工作中不常见。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1 [critical, 强共识] 格式伪影使 SFT 核心贡献近乎无效**

Regex baseline B5（检测 `[No exception data in trace]` 格式标记）达 99.33%，仅比 SFT 的 99.83% 低 0.50pp（McNemar p=0.041）。最强 legitimate regex B4（exception 类名匹配）达 93.61%，SFT 增量贡献 6.22pp。论文在 Appendix 中承认 B5 利用了"format-level shortcut"，但未验证 SFT 模型是否也在利用同一 shortcut。SFT 的增量语义贡献（caught vs uncaught exception 区分）仅体现在 8 个边界样本中的 6 个。

**影响**：论文标题级声称"Exception Events Are All You Need"隐含 SFT 学到了异常语义，但格式标记的存在使得核心发现可能是表示工程 artifact 而非学习发现。

**建议**：移除确定性格式标记后重新训练评估；或将贡献重定位为"异常事件的存在/缺失是 verdict prediction 的充分信号"。

---

**C2 [critical, 共识] exception_only 测试集 49% 重复，统计推断无效**

exception_only 测试集 1,190 样本中仅 607 unique（48.99% 重复），但所有 Wilson CI 和 paired bootstrap 均假设 N=1,190 独立 Bernoulli 试验。CI 系统性偏窄。"99.83% ± 0.00"（3-seed zero variance）可能是样本重叠 artifact：3 个 seed 均错在同样的 2 个 irreducible 样本上（Appendix §B.5 确认），zero variance 不代表真正的 seed robustness。Deduplicated CI [98.81, 99.91]（Appendix §B.6）比主文 [99.58, 100.00] 宽得多，但主文和 Abstract 未使用。

**建议**：以 problem ID 为聚类单元使用 cluster-robust CI；同时报告去重后和去重前结果；所有跨条件对比基于校正后 CI。

---

**C3 [critical, 共识] 6/7 实验条件仅单 seed，消融层级不可信**

仅 Qwen exception_only 有 3 seeds。ae_only (99.92%)、VOTA (99.41%)、loop_only (85.63%)、full_trace (81.76%)、label_only (86.22%)、no_trace (75.13%) 均为单 seed。论文自身的 DeepSeek exception_only 已证明 seed variance 可达 8.24pp（91.09% vs 99.33%）。在此背景下，Tier 1 vs Tier 2 的层级划分——ae_only 99.92% vs loop_only 85.63%——可能在其他 seed 下完全不成立。

**建议**：至少 ae_only、loop_only、VOTA 补充 3-seed 实验，验证层级划分的稳定性。

---

**C4 [critical, 共识] 26%/74% 因果分解有多个未控制混淆变量**

gradient dilution (26%) vs information overload (74%) 的分解依赖可加性假设（无交互项）和 label_only 仅隔离训练信号的假设。但 label_only 同时改变了 effective gradient norm、隐式正则化、过拟合动态。此外，分解仅在 Qwen 上完成；DeepSeek 的 VOTA 受 truncation 严重影响（91.7% 训练样本截断），分解比例很可能完全不同。

**建议**：(1) 降级为近似/描述性分解，而非因果估计；(2) 在 DeepSeek 上补充 label_only 实验验证跨模型稳定性；(3) 或增加控制实验隔离序列长度效应。

---

**C5 [critical, 共识] 实验 scope 过窄，泛化性声明与证据不匹配**

仅 2 个 ~7B 代码专用模型 + 1 个有效主数据集（HumanEval+MBPP, 591 problems）。DebugBench 的 no_trace 已达 96.71%（ceiling effect），论文自身承认"narrow margins are insufficient to independently validate trace importance"。标题 "Cross-Model" 和 Abstract "transfers well across model families" 与 2 个同规模模型不匹配。

**建议**：增加不同规模模型（13B+ 或 1-3B）；寻找无 ceiling 的第二数据集；或显著弱化泛化性声明至"7B-scale Python verdict prediction"。

---

### Should-Fix（影响评分但不一票否决）

**W1 [major]** 标题 "Exception Events Are All You Need" 与 ae_only (99.92%) > exception_only (99.83%) 不符。两者统计不可区分 (p=0.80)，但标题选择性突出 exception events。ae_only 未在 DeepSeek 上测试，使比较不完整。

**W2 [major]** DeepSeek VOTA 14.96pp gap 主要是 truncation artifact（91.7% 训练样本截断；intact 100% vs truncated 83.04%），但 Abstract 和 Conclusion 反复引用此 gap 作为主要发现，未标注 confounded。

**W3 [major]** Related Work 完全缺失 Spectrum-Based Fault Localization (SBFL) 文献（Ochiai, Tarantula, DStar）及近期 LLM-based fault localization 工作（AutoFL, AgentFL, LLM4FL）。论文以 "fault detection" 做 framing 但不 cite 该领域核心文献。

**W4 [major]** DeepSeek seed 123 异常值 (91.09%) 归因为 "LoRA initialization sensitivity" 缺乏直接证据，仅有间接指标（loss 收敛但准确率不同）。应标记为推测性归因。

**W5 [major]** 数据生成循环依赖：所有候选解由 Qwen-2.5-Coder-7B-Instruct 生成，然后同一模型被微调。存在 self-familiarity bias 和 error distribution bias。Limitations section 轻描淡写。

---

## Reviewer Consensus

两位 Reviewer 在所有 critical/major 问题上达成完全共识（交叉回应全部 [AGREE]，零 [REBUT]）。个别问题严重度标注有差异但方向一致：

| 问题 | R1 | R2 | 共识 |
|------|-----|-----|------|
| 格式伪影/regex baseline | N1 critical | N1 critical | **强共识** |
| 统计推断+重复数据 | N2 critical | W4→升级 major | 共识（R1 更严厉） |
| 因果分解过强 | N3 critical | W2 major | 共识（R1 更严厉） |
| 单 seed 消融 | W1 major | N3 critical | 共识（R2 更严厉） |
| 模型多样性/scope | W5 major | N2 critical | 共识（R2 更严厉） |
| Truncation confound | W4 major | W5 warning | 共识 |
| 数据循环依赖 | W3 major | 同意 R1 | 共识 |

## Reviewer Divergence

无实质分歧。

---

## Questions（需要作者澄清）

1. 如果移除 `[No exception data in trace]` 格式标记后重新训练 SFT，exception_only 的准确率变化如何？
2. ae_only、loop_only、VOTA 在 seeds 123 和 456 下的准确率是多少？Tier 1 vs Tier 2 层级是否稳定？
3. 在 DeepSeek 上做 full_trace_label_only 实验，26%/74% 分解比例是否跨模型一致？
4. 如果将 DeepSeek VOTA 的 context window 扩展到 4096 tokens（消除 truncation），VOTA 性能变化如何？
5. 论文是否计划开源代码和数据？

---

## Missing References

1. **SBFL 经典文献**：Ochiai (Abreu et al., 2007)、Tarantula (Jones & Harrold, 2005)、DStar (Wong et al., 2014)
2. **AutoFL** (Kang et al., 2024) — LLM-based fault localization using coverage data
3. **AgentFL** (Qin et al., 2024) — Multi-agent LLM fault localization
4. **LLM4FL** (Widyasari et al., 2025) — Multi-agent repository-level fault localization
5. **"Simple Fault Localization using Execution Traces"** (Mukherjee et al., ICSE 2025 APR)

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目未启用 `external_review.paperreview_ai`）。

---

## Overall Assessment

**评分：weak reject（2.5/5）**
**置信度：4/5**

本文的研究问题有价值（trace 组件对 verdict prediction 的贡献），消融设计系统，实验执行质量和透明度高。但论文存在五个 critical 问题的共识：(1) 格式伪影使 SFT 核心贡献被 regex 几乎完全解释；(2) 49% 测试重复使统计推断不可信；(3) 6/7 条件仅单 seed 而论文自身证明 seed variance 可达 8pp；(4) 因果分解声明过强；(5) 2 个 7B 模型 + 1 个有效数据集对 "systematic cross-model study" 定位覆盖不足。

核心问题在于 claim 强度与证据 scope 的不匹配：实验执行质量高于 novelty 和 claim 的支撑力。如果解决格式伪影问题（验证 SFT 非 shortcut 依赖）、补充 multi-seed 消融、弱化因果和泛化性声明，论文有望达到 EMNLP Findings 水平。当前状态建议修订后重新提交下一轮 ARR。

---

## Detailed Comments

### §1 Introduction
- L13："our key finding is that exception events alone achieve near-perfect accuracy"——需在此处即交代 regex baseline 的强度，避免过度 claim。
- Contribution 2 的 "26%/74%" 应标注为近似分解。

### §2 Method
- §2.2：候选解来源（Qwen 自身生成）的循环依赖需更充分讨论。
- §2.4：应说明为什么仅 exception_only 跑了 3 seeds，其他条件单 seed 的理由。

### §3 Experiments
- Table 1："14.96pp gap" 应在表注中标注 "confounded by tokenizer-driven truncation"。
- Table 2：应报告 regex B4/B5 baseline 作为对照行。
- §3.3："gradient dilution (26%) vs information overload (74%)"需降级措辞。

### §4 Discussion
- 仅 10 行，作为独立 section 过于单薄。建议扩展讨论：(1) SFT vs regex 的真正增量在哪里；(2) 格式标记对结论的影响；(3) 跨 scale/dataset 的预期行为。

### §5 Related Work
- 增加 SBFL/fault localization 段落。
- TraceCoder/InspectCoder 的 positioning 可更具体。

### Appendix
- §B.7 (Dedup)：建议提供 cluster-robust CI 作为主要结果。
- §B.10 (Regex)：B5 的分析应从附录提到主文，因其直接影响核心 claim。
- Fig 编号跳过 fig3，需修正。
- 4 个 orphan bib 条目需清理。
