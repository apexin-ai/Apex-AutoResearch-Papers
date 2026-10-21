---
round: 15
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-25T21:44:34.361324+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 15 Consolidated Review Report (Updated with Cross-Responses)

**Paper**: Complete Execution Traces Degrade SFT-Based Verdict Prediction: A Diagnostic Signal Analysis
**Venue**: EMNLP 2026 (ARR)
**Date**: 2026-05-25 (updated; original submission 2026-05-22)
**Mode**: Fresh review (no prior round context)
**Reviewers**: R1 (statistical methodology + experimental rigor), R2 (novelty/framing + theoretical grounding)
**Cross-sharing**: Complete. R2→R1: 7 AGREE, 1 REBUT (升级 binding constraint). R1→R2: 5 AGREE, 2 REBUT (泛化范围过高; prior work 区分已足够), 1 AGREE with nuance.

---

## Summary

本文研究 execution trace 各组分（exception message, loop iteration, variable state 等）对 SFT 模型 verdict prediction 性能的影响。在 Qwen-1.5B/7B 和 DeepSeek-1.3B/6.7B 四个模型上，使用 VOTA 方法压缩 trace 信号训练 LoRA 适配器，展示了组分贡献层级：exception_only (Tier 1) 在所有模型上接近 100% 准确率，显著优于包含更多信息的 full_trace (81-86%)。论文提出 gradient masking decomposition 框架，将性能差距归因于 backward-pass gradient dilution (~24%) 和 inference-time signal sparsity (~76%)。

实验执行 thorough（13 页附录，多种子验证，校准分析，OOD 评估，去重分析），在同类实证研究中属于 top tier。但两个结构性问题限制了贡献：(1) gradient masking 分解仅在 Qwen 家族有效，不具通用性；(2) "information density as the binding constraint" 的核心声称超出证据支撑。

---

## Strengths

**S1. 系统性组分消融设计**：9 个 trace 组分 × 4 模型 × 3 架构族，多种子验证。在 SFT 设定下首次细粒度量化每个 trace 组分的贡献，实验规模和覆盖度在同类工作中突出。

**S2. 反直觉的核心发现**：full_trace 包含 exception 全部信息却性能降低 18-23pp。这一 "less is more" 现象是非平凡的负面结果：论文价值不在于 exception_only 的高准确率本身（接近 tautological），而在于 (a) full_trace 仅 81.76% 这个负面发现，以及 (b) 系统消融揭示的 degradation mechanism。R1 在交叉回应中准确指出：核心贡献应是 "how verbosity degrades SFT" 而非 "how to achieve high accuracy"。

**S3. 充分的控制实验**：padded2048（排除长度不对称）、nomarker（部分排除格式依赖，仍高于 regex B4 达 4pp+）、tail-truncation 分析（空间定位诊断信号）、budget curve 等构成较完整的证据链。Nomarker 实验特别值得注意——移除所有 format markers 后仍达 ~97.8%，说明并非纯粹 surface-level pattern matching（R1 交叉回应中强调此点）。

**S4. 校准分析**：ECE 和 reliability diagram 为 "性能提升是否来自真正的语义理解" 提供量化分析入口，是同类消融工作中少见的分析维度。

**S5. 详尽的附录**：13 页覆盖 per-class breakdown、tokenizer 分析、persistent error analysis、exception type breakdown、calibration diagrams、error overlap、DebugBench OOD、training dynamics——empirical completeness 的典范。

---

## Weaknesses

### Must-Fix (4 issues)

**MF-1. Gradient masking decomposition 泛化性不足** [R1-N1, R2-N2, 双方交叉 AGREE | Issue W21]

24%/76% 分解仅在 Qwen-1.5B/7B 完成（2 scales, 3 seeds）。CodeLlama 和 DeepSeek 出现 label-only collapse，论文自身在 §4.4 末段承认分解是 "approximate (Qwen family, 2 scales, 3 seeds)"。但此 caveat 被埋在段落末尾，与 Introduction Contribution 的强 claim 落差明显。Label-only collapse 说明分解框架对 tokenizer 效率高度敏感，削弱其作为通用分析工具的价值。

R1 交叉回应中指出论文仍有超越 Shi et al. (2023) 的增量（SFT 设定下的量化、gradient masking 分解、tail-truncation 空间定位），但 framework 不具通用性。R1 还观察到剩余 76% 本质上是 Shi et al. 的 "irrelevant context distraction"——论文已引用但 Discussion 未充分承认这一联系，使 density framing 看起来比实际更原创。

→ **共识行动**：将 gradient masking 从核心贡献降级为 Qwen-specific case study。Discussion 显式承认与 Shi et al. 的关系。

**MF-2. 关键 baseline 缺乏多种子方差估计** [R1-N2, R2 AGREE | Issue W3]

Table 3 density decomposition 依赖 full_trace 绝对值（81.76%）作为分解起点，但 full_trace 仅报告单 seed。如果方差与 no_trace 的 σ=4.48pp 类似，"24% backward-pass contribution" 可能在 ±5-10% 范围内浮动。Appendix E 辩护 "baselines' absolute values matter less than the gap to Tier 1" 与 Table 3 依赖绝对值形成逻辑矛盾。

R2 补充：tier 间大 gap (~18pp) 使 tier 排序不受影响，precision 受影响最大。

DeepSeek seed 42 排除是 post-hoc outcome-dependent exclusion。虽然归因分析 thorough（Appendix F：91.7% 截断），但 1/3 seeds 产生 failure 是 VOTA 脆弱性的关键证据，恰好强化 density argument。

→ **共识行动**：(1) 补充 full_trace 至少 2 个额外 seed，或标注为单 seed 估计；(2) Table 1 报告 DeepSeek 3-seed 均值含 seed 42，将 failure 框定为支持 density hypothesis 的正面证据。

**MF-3. Exception_only 48.99% test duplicates 导致 CI 膨胀** [R1-N3, R2-W5, 双方交叉 AGREE | Issue W12]

Table 2 报告的 exception_only 95% CI [99.58, 100.00] 基于 N=1,190，有效独立样本约 N_eff≈119（problem-level clustered bootstrap）。Appendix F 的 deduplicated CI [98.81, 99.91] 与主表差距显著。脚注提到 clustered bootstrap 但正文 CI 仍用 N=1,190。

影响评估：cross-tier gaps（~13pp）在 clustered CI 下仍显著，但 within-tier 比较（exception_only vs ae_only 差距仅 0.19pp）在 clustered CI 下很可能不显著。"exception_only 是唯一 minimal sufficient signal" 的 claim 需修正为 "Tier 1 signals are minimal sufficient"。

→ **共识行动**：主表同时报告 standard CI 和 clustered CI。

**MF-4. "Binding constraint" claim 过度泛化** [R1-W4 should-fix → R2 REBUT 升级 critical; R1 交叉 AGREE R2-N2 | Issue W22]

"Information density as the binding constraint on SFT learning" 是 Contribution 1 字面表述和标题核心 claim。R1 列为 should-fix，R2 认为该 claim 仅在 2/4 模型 gradient masking 上成立、依赖单 seed baseline、且仅在 binary classification 验证，应升级为 critical。R1 在交叉回应中 AGREE overclaim 存在，建议改为 "the dominant factor in our setting"。

**Director 采纳 R2 升级**：Contribution 1 的字面表述建立在不充分证据上，需降级。

→ **共识行动**：降级为 "candidate mechanism" / "the dominant factor in our setting"。Title/Abstract/Conclusion 同步修改。

### Should-Fix (8 issues)

**SF-1. "Phase transition" 术语过度使用** [R1-W1, R2 AGREE | Issue W19]

Figure 3 budget curve 仅 5 个数据点（256, 384, 512, 1024, 2048），不足以表征 transition 形状。384→512 的 +13-22pp jump 是 Python traceback 长度分布（400-500 tokens）在 budget sweep 上的投影，非模型 critical phenomenon。4 个模型的 cross-model 一致性有信息量，但不应称 "phase transition"。
→ 改为 "sharp threshold" 或 "diagnostic-boundary effect"。

**SF-2. DebugBench ceiling effect** [R1-W3, R2-N3 partial | Issue W8]

no_trace baseline 96.71%，headroom 仅 3.29pp。Synthetic single-point mutations 在源码层面高度可识别。"Cross-dataset transfer preserves ranking" 需 caveat。R1 在交叉回应中 REBUT R2 的更广泛泛化要求（跨任务+跨数据集+跨语言），认为标准过高——论文 scope 明确为 verdict prediction + Python + 4 models，Limitations 已覆盖。**Director 裁决**：R1 rebuttal 有理，泛化范围要求降级为 warning；但 DebugBench 具体 ceiling caveat 仍需添加。

**SF-3. 8 个 boundary samples 统计效力不足** [R1-W5, R2-N1, 双方交叉 AGREE | Issue W20]

McNemar p=.041 在多重比较校正后不再显著。这 8 个 samples 是区分 "semantic understanding" 和 "surface patterns" 的唯一直接证据。R1 交叉回应中独立验证此判断。Nomarker 实验间接支持语义理解 claim（比 regex 高 4pp+），但 boundary analysis 本身统计功效不足。
→ 保留为 exploratory evidence，移除 p-value，改为 descriptive statistics。

**SF-4. "Scale invariance" claim 需限定** [R2-W4, R1 AGREE | Issue W25]

1.5B-13B（8.7×）不足以支撑 "scale invariance"。30B+ 模型可能有更强 long-context 处理能力。
→ 改为 "scale independence within the 1.5B-13B range"。

**SF-5. Figure 1 (fig:cross_scale) 未在正文中引用** [R2-W3, R1 grep 验证 AGREE | Issue W23]

introduction.tex line 29-34 定义 `\label{fig:cross_scale}`，但全文无 `\ref{fig:cross_scale}`。ACL 模板要求所有 figures 在正文中被引用。明确的格式错误。

**SF-6. Discussion (Section 5) 过长** [R2-W2, R1 AGREE | Issue W24]

约占正文 2/8 页，比例偏高。"Exception events capture test verdicts" 段落是实验发现的补充说明，更适合 §4。"Alternative explanations" 可精简或移至 Appendix。节省空间可用于加强实验。

**SF-7. 缺失引用** [R1, R2 共识 | Issue W18]

两位一致要求补充：
- Shi et al. (2023) "Large Language Models Can Be Easily Distracted by Irrelevant Context"
- LDB (Zhong et al. 2024)
- SelfDebug (Chen et al. 2024)
- Reflexion (Shinn et al. 2023)
- LongLLMLingua (Jiang et al. 2024)（R1 交叉回应中新增建议）

R2 提到的 FisherSFT 和 Bruni et al. 真实性未确认，R1 要求提供完整引用信息后再决定。

**SF-8. 核心贡献 reframing** [R1 交叉回应 R2-N1 | Issue W5]

R1 交叉回应中 AGREE R2 的 task trivial concern（B5 99.33% vs SFT 99.83% 仅 0.50pp），但补充 nuance：nomarker 仍高于 regex 4pp+。R1 赞同 reframing 建议——弱化 "exception events as minimal sufficient signal"，重心转向 "verbose trace input actively impairs SFT learning"。两位共识：论文的真正价值在于负面发现（full_trace degradation），而非正面发现（exception_only ceiling）。

### Minor (3 issues)

**M-1. Abstract 数字过多** [Issue W11]
建议部分精确数字替换为定性描述，精确数字保留在 §1。

**M-2. Training dynamics Figure 仅单 seed** [Issue W17]
Caption 应限定为 "Seed 42; 3-seed final accuracies in Table 1 are consistent"。

**M-3. Discussion 中 76% inference-time 部分与 Shi et al. 关系未承认** [Issue W2b]
R1 指出该部分本质是 irrelevant context distraction（Shi et al. 2023），但论文在 Discussion 中未充分承认，使 density framing 看起来比实际更原创。论文在 SFT 设定下有增量（量化、分解、空间定位），但应明确标注 novelty 边界。

---

## Questions for Authors

Q1. Gradient masking 分解依赖 Qwen tokenizer 特性。是否考虑过在支持 label-only loss 收敛的非 Qwen 模型上验证该框架？

Q2. Exception_only 近完美表现是否部分归因于 exception message 在预训练语料中的高频出现（distribution match）？padded2048 和 nomarker 实验未控制此 confound。

Q3. 位置集中度（诊断信息在 trace 末尾）是否比 "密度" 更精确？如果将 exception 移至 trace 中部，结果如何？

Q4. Clustered bootstrap（n_eff=119）和 standard bootstrap（N=1190）的 CI 差异有多大？是否存在 within-tier 比较失去显著性的情况？

Q5. 30B+ 模型是否因更强的 long-context 处理能力而降低 full_trace degradation？（R1, R2 共同关注）

---

## Missing References

- Shi et al. (2023) — "Large Language Models Can Be Easily Distracted by Irrelevant Context"
- Zhong et al. (2024) — LDB
- Chen et al. (2024) — SelfDebug
- Shinn et al. (2023) — Reflexion
- Jiang et al. (2024) — LongLLMLingua

---

## External Review

**Status**: 未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（4 info，0 critical/warning）：
- Page 5: Figure 2 右侧 y 轴刻度标签与图边界距离较近
- Page 6: Figure 4 ECE 数值字号偏小（~6-7pt）
- Page 7: Figure 5 heatmap 数值字号偏小，面板紧凑
- Page 13: 附录单页含 6 个表格，排版紧凑

---

## Overall Assessment

| Reviewer | 评分 | 推荐 |
|----------|------|------|
| R1 | 3.5 | Borderline Conference |
| R2 | 3.0 | Findings |

**综合评分：3.0 (Findings)**

**Director 评分理由：**

R1 正确指出 full_trace degradation (-11.9pp vs no_trace) 是独立的非平凡发现，不可简化为 exception_only 的格式设计。这部分挽救了 novelty concern。但：

1. **核心分析框架泛化性不足**：Gradient masking decomposition 仅在 Qwen 有效（MF-1），24%/76% 分解不能作为通用方法论贡献。

2. **"Binding constraint" 声称超出证据**：Contribution 1 的理论声称建立在 2/4 模型、单 seed、binary classification 基础上（MF-4）。两位 Reviewer 均同意需降级。

3. **统计方法需修正**：CI 膨胀（MF-3）不威胁主效应但影响细粒度 claims；多种子覆盖不一致（MF-2）影响 decomposition 精度。

4. **正面因素**：实验 thoroughness 超过大多数 Findings 论文；控制实验设计严谨（特别是 nomarker 仍高于 regex 4pp+，是非 trivial 的正面证据）；R2 表示如果 MF-1/MF-2/MF-3 解决，愿意上调至 3.0-3.5 区间。

**分歧处理**：

- **Task triviality 权重**（主要分歧）：R2 认为 verdict prediction 近 trivial（regex 99.33%）根本性限制贡献意义；R1 认为 case study 定位下可接受。Director 倾向 R1——论文标题和 scope 已限定，task 选择是 deliberate diagnostic setting。但 exception_only ceiling 的叙事权重应降低。

- **泛化范围**：R2-N3 要求跨任务+跨数据集+跨语言；R1 REBUT 标准过高。**Director 裁决**：R1 rebuttal 成立，论文 scope 明确且 Limitations 已覆盖，降级为 warning。但 Discussion 中的推测性表述（"should transfer"）需加 hedging。

- **Prior work 区分**：R2-W1 认为与 DCSH/ferrando 区分不够；R1 REBUT Section 2.1 已有 4 点明确区分。**Director 裁决**：R1 rebuttal 成立，撤销。

**Confidence**: High. 两位 Reviewer 在 4 个 must-fix 上达成共识，2 个 rebuttal 经 Director 裁决后不影响整体判断。

---

## Detailed Comments

### 跨 Reviewer 共识（按优先级排序）

1. **Gradient masking → Qwen-specific case study** [MF-1, W21]
2. **CI 修正 + clustered CI 双报** [MF-3, W12]
3. **"Binding constraint" → "candidate mechanism"** [MF-4, W22]
4. **Full_trace 补充多 seed / seed 42 reframe** [MF-2, W3]
5. **"Phase transition" → "sharp threshold"** [SF-1, W19]
6. **Figure 1 引用修复** [SF-5, W23]
7. **Boundary analysis 移除 p-value** [SF-3, W20]
8. **Scale invariance 加限定** [SF-4, W25]
9. **Discussion 精简** [SF-6, W24]
10. **补充引用（5 篇）** [SF-7, W18]
11. **Reframe: "traces hurt" > "exceptions help"** [SF-8, W5]

### Director 裁决的 Rebuttal

| Rebuttal | 提出者 | 裁决 | 理由 |
|----------|--------|------|------|
| R2-N3 泛化范围 | R1 | **R1 成立** | 跨任务+跨数据集+跨语言对单篇 ablation study 标准过高；Limitations 已覆盖 |
| R2-W1 prior work | R1 | **R1 成立** | Section 2.1 已有 4 点明确区分（component ablation, gradient masking, tail-truncation, cross-architecture） |
| R1-W4 severity | R2 | **R2 成立** | "Binding constraint" 是 Contribution 1 核心声称，证据链缺口影响理论贡献可信度 |

### Issue Tracker 更新摘要

本轮共 25 条 issue（新增 W19-W25），状态分布：
- **Resolved**: 10 条（W1, W2, W4, W7, W9, W10, W13, W14, W16, W10）
- **In progress**: 5 条（W2b, W3, W5, W6, W8）
- **Open**: 10 条（W11, W12, W15, W17, W18, W19, W20, W21, W22, W23, W24, W25）