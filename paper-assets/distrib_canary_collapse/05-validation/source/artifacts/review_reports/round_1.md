---
round: 1
overall_score: weak reject
timestamp: 2026-05-16T06:05:19.452398+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

## 审稿报告 — Round 1（distrib_canary_collapse → EMNLP 2026 Main Conference）

**Reviewer Panel**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性 + 相关工作 + 格式）
**交叉分享**: 完成，所有关键问题达成实质共识

---

## Summary

本文研究 iterative model collapse 中 lead-lag 分析的方法论可靠性问题。作者暴露三个 pitfalls（method sensitivity, spurious regression, regime dependence），提出 multi-method consensus framework（K-of-M methods × S-of-N seeds），并以 Pythia-410M 在 WikiText-103 上的实验验证 token entropy 为 diversity collapse 的 one-generation-ahead canary（α=1.0, 4 seeds）。

---

## Strengths

1. **选题填补真实空白**：model collapse 文献中的 lead-lag claims 普遍缺乏方法论审视，本文首次系统量化了这一问题
2. **重要的负面发现**：canary→perplexity 通道在 differencing 后完全消失（F≈0, p=0.99），对文献中已有的错误 claim 具有纠正价值
3. **Null control 设计合理**：α=0.0 作为 FPR 验证的实验设计在该领域罕见
4. **方向性不对称证据有力**：24/24 forward vs 0/24 reverse 是最强实证结果
5. **诚实的 scope 限定**：明确将 canary claim 限制在 distinct-n，不过度推广
6. **自我批判透明度高**：Discussion 中对 T-Y power、FPR 不对称、α=0.75 局限的坦诚讨论
7. **写作清晰、论证链完整**
8. **Practical guidance tiers**（Table 1 四级建议）对实践者友好

---

## Weaknesses（按严重程度排序）

### Critical（Must-Fix，影响接收决定）

**C1. Ground-truth 定义循环论证** [共识: R1 提出, R2 完全同意]
- 6 个 ground-truth pairs 由 "first-differencing diagnostic 后仍 FDR-significant" 定义（§3.3），但 differenced cross-correlation 本身是 consensus panel 的 method 2
- Ground truth 定义和 consensus 投票使用同一统计性质（detrending 后相关性是否存留），"independently validated" 的措辞不准确
- FNR=0% claim 受 inflation：ground-truth pairs 天然已通过 5 个方法中的 1 个
- Pipeline filtering 叙事（§3.2 "14 survive Stage 2"）同时既是 filtering step 又是 ground-truth 依据

**C2. FPR=0% 标定仅单 seed，abstract/conclusion 未加限定** [共识: 双方一致]
- FPR=0% 来自 α=0.0, seed=42 单次实验，论文自认"may be optimistic"（§6）
- 但 abstract 和 conclusion 以同等力度宣称 "0% false-positive rate"，无限定语
- 对以方法论严谨为核心贡献的论文，自身标定存在 rigor gap

**C3. α=0.50/0.75 仅 1 seed，regime boundary 结论不稳健** [共识: 核心观点一致，R2 纠正 α=0.25 有 3 seeds]
- α=0.50 和 α=0.75 各仅 seed=42，而 regime boundary 恰在此区间
- Table 1 非单调 distinct-1 pattern、Table 2 的 "最极端 method×regime divergence"（α=0.50）可能是 seed-specific
- α=0.75 的 11/16 single-seed count（§5.3）可能因缺乏 multi-seed filtering 而虚高

**C4. α=0.75 multi-seed 未完成 + Appendix A（distinct-3）缺失** [共识: 双方一致]
- α=0.75 仅 seed=42，p 值 borderline（p_fdr=0.046-0.054）
- Appendix A 被引用 ≥3 次但提交材料中不存在
- 6 个 ground-truth pairs 中 2 个（entropy→distinct-3, ECE→distinct-3）依赖 Appendix A——30% ground truth 不可验证

**C5. 新颖性有限：核心方法论为计量经济学已有知识的直接迁移** [R2 提出, R1 部分接受]
- 三个 pitfalls 是时间序列计量经济学经典问题（Granger & Newbold 1974 即系统研究 spurious regression）
- Consensus framework（K-of-M, S-of-N）是标准 multi-method triangulation
- 论文 framing 在 "method innovation" 和 "empirical contribution" 之间摇摆
- R1 认为：如果 reframe 为 "empirical exposure for NLP community" 可部分缓解，但当前 framing 不合适
- 缺少针对 NLP 短时序特性的方法论适配（如 small-sample corrections）

**C6. 实验规模过窄** [共识: 双方一致]
- 单模型（Pythia-410M）+ 单数据集（WikiText-103, 5k subset）+ 单训练范式（replace-only）
- GPT-2-medium 交叉验证为 single-seed/single-α=1.0，batch size 差异（32 vs 4）引入混淆变量
- §6 确实报告了 GPT-2-medium 的具体数字（6/6 pairs, p_FDR=0.003, 0/6 reverse），但不足以建立泛化性
- "framework transfers directly to any domain"（§7）在当前证据下过度 claim

---

### Warning（Should-Fix）

**W1.** Abstract "Granger-causes" vs Discussion "Granger-precedes" 措辞不一致——应全文统一为 "Granger-precedes" [共识]

**W2.** Permutation Granger（linchpin method, Shapley=+0.375）缺少 formal power analysis——T-Y 有 bootstrap power 分析但 linchpin method 反而没有 [共识]

**W3.** "spurious-signal rate = 75%" headline 依赖 underpowered T-Y 的 25% 端——排除 T-Y 后为 62.5%，应作为 headline [共识]

**W4.** α=0.75 borderline 单 seed 结果（p_fdr=0.046-0.054）出现在 abstract/conclusion——对批评他人 rigor 的论文，标准不一致 [共识]

**W5.** Toda-Yamamoto 纳入（Shapley=-2.625, power=0.05-0.20）的表述不充分——覆盖 unknown integration order 的理由成立，但应明确 frame 为"保险策略" [部分共识]

**W6.** 可重复性严重不足：缺 lr/optimizer/warmup/weight decay、generation temperature/top-k/max-len、metric 计算细节（distinct-n sample 数量和长度、ECE bin 数量、entropy 计算方式）、未提及代码开源 [共识]

**W7.** Token entropy canary 仅在 α=1.0 完整验证——"the canary works where it's least needed"——低 α regime 下完全失效（0/8），实际效用悖论未在 Discussion 中正面讨论 [共识]

**W8.** 缺少独立 `\section*{Limitations}` section——ARR 格式要求放在 Conclusion 之后、不计入页数 [共识]

**W9.** 缺少 AI Writing Disclosure 和 Responsible NLP Checklist——ARR 2025+ 合规要求 [共识]

**W10.** canary→perplexity 为何 spurious 缺少深入解释——特别是 perplexity = exp(entropy) 的数学关系未讨论（若成立则结果 trivial）[部分共识]

---

## Reviewer Consensus

以下关键问题两位 Reviewer 达成完全共识：
- [AGREE] Ground-truth 循环论证 (C1)
- [AGREE] FPR 单 seed 标定 (C2)
- [AGREE] Appendix A 缺失 + α=0.75 未完成 (C4)
- [AGREE] 实验规模过窄 (C6)
- [AGREE] Granger-causes/precedes 不一致 (W1)
- [AGREE] 75% headline 问题 (W3)
- [AGREE] 可重复性不足 (W6)
- [AGREE] 格式合规 (W8, W9)

## Reviewer Divergence

**Novelty (C5)**: R2 认为 critical，R1 认为 reframing 后可接受（"empirical exposure" 对 NLP 有价值）。双方同意当前 framing 不合适。

**GPT-2-medium (C6 sub-point)**: R1 初始认为"无数字无检验"，R2 纠正事实错误——§6 确实有 6/6, p_FDR=0.003, 0/6 reverse 的具体数字。双方同意验证仍不充分。

**T-Y 纳入 (W5)**: R1 认为理由不充分，R2 认为方法论理由成立（覆盖 unknown integration order）但表述需改进。

---

## Questions（需作者澄清）

1. Ground-truth pairs 能否用完全外部标准定义（如 held-out architecture 复现或更长时序 convergence）？
2. 为什么未对 permutation Granger（framework 的 linchpin method）做 bootstrap power analysis？
3. Token entropy 和 perplexity 之间是否存在直接数学关系（perplexity = exp(cross-entropy)）？如果是，canary→perplexity 为 "spurious" 是否只是这一数学恒等式的后果？
4. 实际应用中，用户如何在 α 未知时使用此框架？Canary 在 α≤0.50 下完全不可检测的事实如何影响 practical deployment？
5. α=0.75 的 multi-seed 实验预计何时完成？Appendix A 为何未包含在提交中？
6. 代码是否计划开源？

---

## Missing References

1. **Granger, C. W. J. & Newbold, P. (1974).** "Spurious regressions in econometrics." *Journal of Econometrics*. — Pitfall 2 的奠基文献，论文讨论 spurious regression 却未引用 [共识]
2. **Hataya, R. et al. (2023).** "Will Large-scale Generative Models Corrupt Future Datasets?" — 早期系统研究 model collapse [共识]
3. **Seddik, M. E. A. et al. (2024).** "How Bad is Training on Synthetic Data? A Statistical Analysis." — Gaussian mixture 下 collapse 理论分析 [共识]
4. **Toda, H. Y. & Yamamoto, T. (1995).** — §2 中 Toda-Yamamoto 方法错误引用为 Granger (1969) [R1 identified]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置，跳过。

---

## Overall Assessment

**Score: Weak Reject (2.5/5)**
**置信度: High (4/5)**

**理由**：

论文选择了一个及时且重要的 research question，实验设计在其规模内严谨，写作质量高。但存在多个相互强化的问题：

1. **证据-声明不匹配**：核心 claims（framework 泛化性、regime boundary、FPR/FNR=0%）的证据强度不足以支撑其在 abstract/conclusion 中的表述力度
2. **方法论自洽性问题**：以 "methodological rigor" 为卖点的论文，自身存在循环论证（C1）和单 seed 标定（C2）
3. **完整性不足**：Appendix A 缺失、α=0.75 未完成——论文在关键证据缺失的情况下提交
4. **新颖性有限**：核心方法论工具均为成熟领域的直接迁移，缺少针对 NLP/短时序场景的创新适配

**Reviewer 共识建议**：建议 Findings track 接收，前提是完成以下修改：
- 补全 Appendix A 和 α=0.75 multi-seed
- 用外部标准重新定义 ground truth 或明确标注循环性
- FPR 补充 multi-seed 或 abstract/conclusion 加限定
- Reframe contribution 为 empirical exposure 而非 method innovation
- 补全可重复性信息和格式合规项

如果作者能额外补充 1B+ 模型验证并解决 practical utility paradox，可重新考虑 main conference。

---

## Detailed Comments（逐节）

### Abstract
- "Granger-causes" → "Granger-precedes"
- "0% false-positive and 0% false-negative" 需加 "single-seed" 限定
- α=0.75 "preliminary single-seed evidence" 建议移除
- 75% → 62.5%（或并列报告）
- 信息密度过高（7+ 数字），建议精简

### Introduction
- Contribution 2 的 "propose" 暗示方法创新——建议改为 "apply/instantiate"
- "16 pairs" vs "8 primary pairs" 的切换解释滞后

### Background
- §2 Toda-Yamamoto 引用错误：\cite{granger1969investigating} 应为 Toda & Yamamoto (1995)
- 五方法描述简洁清晰（优点）

### Method
- §3.2 `\textsc{robust}` 可能为 LaTeX 排版问题
- §3.3 "independently validated" 措辞需修正——与 consensus method 2 测试同一统计性质
- Tier 3 的 K≥4/5 是否过拟合于当前设置？缺少 sensitivity analysis

### Experiments
- §5.1 "follows the full-replacement paradigm" 但 α<1.0 是 mixed replacement——措辞不准确
- Table 2 α=0.75 列 "---" 缺解释——§5.3 有 single-seed 数据可填入并标注 "(1 seed)"
- §5.3 α=0.75 结果应弱化表述或移至 supplementary

### Related Work
- 补充 Granger & Newbold (1974)、Hataya et al. (2023)、Seddik et al. (2024)
- Citation key `chen2025scales` 疑似与实际作者 Du et al. 不匹配——需作者确认

### Discussion
- 补充 "practical utility paradox" 讨论
- 补充 perplexity = exp(entropy) 数学关系的讨论
- Limitations 内容提取为独立 \section*{Limitations}
- GPT-2-medium 数字（6/6, p=0.003, 0/6 reverse）建议提升到 §5

### Conclusion
- "transfers directly to any domain" 过度 claim——当前证据仅覆盖一个设置
- FPR/FNR claims 加限定