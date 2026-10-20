---
round: 8
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-21T18:09:44.840031+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 13 Consolidated Review Report
## "Less Is More: Exception Events Outperform Complete Traces for Verdict Prediction"
**Target Venue**: EMNLP 2026 via ARR (deadline 2026-05-25)
**Review Date**: 2026-05-21
**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性/引用)
**Cross-sharing**: Complete (R1↔R2, all [AGREE]/[REBUT] collected)

---

## Summary

本文对 verdict prediction（测试执行 pass/fail 分类）任务进行了系统性的 trace 组件消融实验，涵盖 4 个模型（1.5B–13B，3 个架构家族）和 7 种 trace 表征。核心发现：(1) exception_only 在所有模型上达到 ≥99.33%，而 full_trace 仅约 72–82%；(2) 提出了 gradient dilution (~24%) 与 information overload (~76%) 的近似分解；(3) 观察到跨模型的 two-tier 组件层级模式。论文在消融设计的系统性上有贡献，但在 novelty、核心 claim 的因果强度、以及实验混淆变量控制上存在显著问题。

---

## Strengths

**S1. 系统性的消融设计 [R1+R2 共识]**
7 种 trace 条件 × 4 个模型 × 3 个架构家族的矩阵设计在 trace 表征研究中是首次。实验覆盖面远超前人工作（TracePile、NExT 等仅使用单一或少量 trace 格式）。

**S2. 跨模型一致性强 [R1+R2 共识]**
exception_only ≥99.33% 的结论在 Qwen-2.5-Coder-7B/1.5B、CodeLlama-13B、DeepSeek-Coder-6.7B 上全部成立，跨 3 个架构家族的一致性增强了结论的可信度。

**S3. 丰富的辅助分析 [R1]**
格式标记消融（nomarker ablation）、训练动态曲线、校准分析（ECE < 0.005）、trace 长度 budget sweep、DebugBench 跨数据集实验等构成了多维度的证据链。17 节 Appendix 提供了充分的补充材料。

**S4. 论文写作整体清晰 [R2]**
Section 2（Method）的任务定义和数据集描述准确完整。Table 1 的跨模型主实验表格信息传达直观有效。Related Work 覆盖面广（53 citations），涵盖 7 个相关方向。

**S5. 校准结果有意义 [R1]**
ECE < 0.005 表明 compact 输入不仅提高准确率，还改善了模型置信度与实际正确率的对齐——这对下游应用（如 fault localization）有实际意义。

---

## Weaknesses

### Must-Fix（共识项，需解决后方可接收）

**MF-1. 核心发现 near-tautological [R1-N1 + R2-N1, 双方 AGREE]** ⚠️ 
Exception events 在任务构造层面编码了 verdict 信号（fail 类有异常 → 有 exception event；pass 类无异常 → 无 exception event）。regex baseline B5（基于 "Traceback" 关键词匹配）达到 99.33%，与 SFT exception_only 的 99.83% 仅差 0.50pp（约 6 个样本）。"Less Is More" 的 framing 夸大了发现的反直觉性——exception events 之所以有效并不令人惊讶，真正需要解释的是 full trace 为何严重损害性能。

**建议**：将论文核心叙事从 "exception events are surprisingly effective"（近乎同义反复）reframe 为 "quantifying why complete traces actively harm SFT learning"（非平凡且有价值的发现）。标题需相应调整。

**MF-2. 24%/76% 分解存在严重混淆变量 [R1-N1 + R2 AGREE]** ⚠️
`full_trace_label_only` 相对于标准 `full_trace` 同时改变了三个变量：(a) 梯度来源分布，(b) 有效学习率，(c) 训练目标。这使得 "24% gradient dilution / 76% information overload" 的归因无法可靠成立。更严重的是，该分解在 CodeLlama 和 DeepSeek 上 collapse 至 ~28.5%（接近随机），仅在 Qwen 家族（2/4 模型，1/3 架构）上成立。Round 12 已将 C3 降级为 "preliminary analysis"，但 wording 修改未解决底层混淆——confounders 仍存在。

**建议**：将 24%/76% 从点估计改为上界/下界表述（"gradient dilution accounts for at most ~24%"）；明确标注 Qwen-only 限制；或设计中间条件隔离变量。

**MF-3. VOTA 在所有模型上均不优于 exception_only，方法贡献不成立 [R1-N2 + R2 AGREE]** ⚠️
Table 1 数据：Qwen-7B VOTA 99.05% vs exc 99.83%（-0.78pp），Qwen-1.5B 99.54% vs 99.83%（-0.29pp），CodeLlama 98.74% vs 99.89%（-1.15pp），DeepSeek 99.25% vs 99.39%（-0.14pp）——四个模型全部 VOTA ≤ exception_only。论文用完整 §2.3 节介绍 VOTA + Appendix C Algorithm 1，但实验未显示任何增量贡献。这构成方法-结果失配。

**建议**：将论文重新定位为 ablation study 而非新方法提出；大幅缩减 VOTA 介绍篇幅（移入 Appendix 或合并到实验条件描述）；或论证 VOTA 在更困难 benchmark 上的潜在优势。

### Should-Fix（建议修改，不修改可能降低评分）

**SF-1. 序列长度混淆未控制 [R1-W6 + R2-W2, 双方 AGREE]**
exception_only ~150 tokens vs full_trace >2,048 tokens（>13× 差距）。性能差异可能部分来自序列长度（模型 capacity 限制）而非信息密度差异。tail-truncation 同时改变长度和内容，无法分离两种效应。controlled-length 实验（如 exception_only padding 到 2,048 tokens，或 max_seq=4096 重跑 full_trace）仍未补充。

**SF-2. Information density 定义循环且出现过晚 [R1-W4 + R2 AGREE]**
全文 30+ 次使用 "information density" 但 §4 的 operationalization 出现太晚（应在 §2/3），且定义存在循环性（verdict-relevant tokens 由 accuracy 定义，而 density 声称解释 accuracy）。需在 Method 节提供先验的、非循环的工作定义。

**SF-3. 任务动机薄弱 [R2-N2 → R1 REBUT → Director 降级]**
获取 trace 即已知 verdict（test framework 直接报告 pass/fail），"为何需要预测？" 的问题未充分回应。R1 以 CRUXEval/NExT 等 proxy task 先例 REBUT，Director 认为先例论证有效（proxy task 在 *CL 有充分先例），但 Discussion 中的三个应用场景缺乏实验验证，仍应降级为 future directions。

**SF-4. DebugBench 天花板效应削弱 cross-dataset validation [R2-W1 + R1 AGREE]**
DebugBench no_trace baseline 已达 96.71%（headroom 仅 3.29pp），使得 cross-dataset validation 缺乏区分力。应从 "cross-dataset validation" 降级为 "supplementary OOD analysis with ceiling limitations"。

**SF-5. Table 2 组件消融仅 Qwen-7B [R1-W2, residual concern]**
Round 12 已将 C4 降级为 "observation/pattern"，但完整的跨模型组件消融数据仍缺失。ao_only/loop_only 在其他模型无数据，two-tier pattern 的泛化证据不足。

**SF-6. SFT vs regex 增量过小 [R1+R2 共识]**
SFT exception_only (99.83%) vs regex B5 (99.33%) 仅差 0.50pp。nomarker 条件下 regex baseline 的表现未报告——这是判断 SFT 真实增量的关键缺失对比。format marker `[No exception data in trace]` 在 pass 类中确定性出现，直接编码 verdict；nomarker ablation 显示 ~2pp marker 贡献（错误率翻倍 0.61%→2.52%）。

**SF-7. 测试集 49% 重复，CI 宽度被低估 [R1-W3]**
1,190 样本仅 607 unique（49% 重复率）。点估计不受影响（dedup delta = 0.00pp），但 CI 宽度基于 n=1,190 计算时被低估 ~1.4×（effective n ≈ 607）。R2 REBUT 称 0.00pp delta 表明影响有限——对点估计成立，但 CI 仍需调整。

**SF-8. Qwen 生成+评估循环依赖 [R1-N3 → R2 REBUT → Director 降级]**
数据集由 Qwen 生成、Qwen 也是评估模型之一。R2 REBUT 指出 CodeLlama 在完全 OOD 数据上达到 100% exception_only（跨模型 gap 仅 0.50pp），排除了 Qwen-specific bias。Director 同意 REBUT 有效，维持 resolved 但标注 residual concern。

### Minor

**M-1.** Abstract "~80%" 不准确：Table 1 full_trace 跨模型均值 ~76.5%（72.4%–82.0%），仅 CodeLlama 超过 80%。应改为 "72–82%" 或 "~76%"。[R1]

**M-2.** Table 1 single-seed vs multi-seed 标注不完整：已有 † 标注 no_trace，但其他 single-seed 条目未统一标注。[R1]

**M-3.** "Phase transition" 术语对 N=4 模型过于精确。建议改为 "sharp performance jump"。[R1]

**M-4.** Ethics Statement 中 GPU 型号 "RTX PRO 6000 Blackwell" 可能缩小匿名审稿的匿名范围。建议模糊为 "enterprise-grade GPUs"。[R1]

**M-5.** 1 orphan bib entry (pornprasit2021jitline)；6 篇作者名 LaTeX 编码不匹配。[R2]

**M-6.** Conclusion 过于简短（~4 行），仅重复核心发现，缺方法论启示、局限性摘要、未来方向。[R2-W4 + R1 AGREE]

---

## Questions

**Q1.** nomarker 条件下 regex baseline（B5）的准确率是多少？这决定了 SFT 在移除 format shortcut 后的真实增量。

**Q2.** 如果将 exception_only padding 到 full_trace 同等长度（~2,048 tokens），准确率是否变化？这可以分离序列长度效应和信息密度效应。

**Q3.** 24%/76% 分解在 Qwen-1.5B 上是否成立？（当前仅报告 Qwen-7B，同家族的第二个数据点可以初步验证 family-level consistency）

**Q4.** 作者是否考虑过在非竞赛编程数据集（如真实开源项目的测试执行）上验证？竞赛编程的异常模式可能过于简单和同质。

---

## Missing References

R2 识别以下可能相关但未引用的工作（需核实真实性后决定是否补充）：
- Paul et al. (2021) "Deep Learning on a Data Diet" — data selection 基础文献
- Sorscher et al. (2022) "Beyond neural scaling laws: beating power law scaling via data pruning" — data quality vs quantity
- Related Work §Training Efficiency 已引用 Bengio (2009), Swayamdipta (2020), Sachdeva (2024)，但上述两篇是 data selection 方向的高引经典，补充可加强叙事连贯性。

---

## External Review

**状态**: 未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: 已完成 | 0 Critical, 3 Warnings, 13 Info

| 严重度 | 位置 | 发现 |
|--------|------|------|
| ⚠️ Warning | Page 1–2 | 前 2 页纯文本无 display item。Figure 1 直到 page 4 才出现，错失认知锚点。建议提前至 page 1–2。 |
| ⚠️ Warning | Page 4 | 单页堆积 3 个 display items（Figure 1 + Figure 2 + Table 2），密度不均。Figure 2 被压缩，坐标轴标签勉强可读。 |
| ⚠️ Warning | Page 6–7 | 连续 2 页纯文本（Section 3.5 + Discussion），视觉单调。建议从 Appendix 提升一个图表。 |
| ℹ️ Info | Page 3 | Table 1 作为首个 display item，信息传达清晰，booktabs 格式规范。 |
| ℹ️ Info | Page 8 | Figure 3 浮动漂移约 2 页（讨论在 page 6），在 8 页限制下可接受。 |
| ℹ️ Info | Page 9 | Limitations 简洁覆盖 3 要点，符合 EMNLP 2026 要求。 |
| ℹ️ Info | Page 10–11 | References 格式统一，无 [?] 未解析引用。 |

---

## Overall Assessment

**Overall Score: 3.0 / 5 (Findings)**
**Confidence: 4 / 5**

**Reviewer Scores**: R1 = 3.5/5, R2 = 3.0/5

**评分理由**：

论文在消融设计的系统性和跨模型覆盖面上有明确贡献，但三个 Must-Fix 问题构成接收障碍：

1. **Near-tautological framing**（MF-1）：核心 "exception_only outperforms" 的发现在任务构造层面近乎同义反复（regex 99.33% vs SFT 99.83%），论文的标题和叙事夸大了反直觉性。真正非平凡的发现（"complete traces actively harm SFT"）被埋在 framing 之下。

2. **Decomposition confounders**（MF-2）：24%/76% 的归因在底层有三个未隔离的混淆变量，且仅在 2/4 模型上成立。Round 12 的 wording 降级未解决实质问题。

3. **VOTA 无增量贡献**（MF-3）：论文用大量篇幅介绍的唯一新方法在所有实验条件下均不优于更简单的 exception_only baseline，构成方法-结果失配。

如果 MF-1 的 reframing + MF-3 的重新定位完成得当，论文可以作为一篇有价值的 empirical analysis 被 Findings 接收。SF-1（序列长度混淆）和 SF-2（density 定义）是潜在的 borderline 因素——如果审稿人追问 controlled-length 实验，当前论文无法回应。

**ARR 评分对照**：3.0 = Findings（可被 Findings 接收）。当前版本不满足 Conference（4.0）的 novelty 和方法论严谨性要求。

---

## Detailed Comments by Section

### Abstract
- "~80%" full_trace 数值偏高（实际跨模型均值 ~76.5%），应修正为范围或更保守估计
- "Less Is More" framing 在 regex 99.33% 的背景下显得 overclaimed

### §1 Introduction
- 4 个 contributions 的强度与证据不匹配：C1（information density）缺先验定义；C2（exception_only）近乎 tautological；C3（decomposition）仅 Qwen 成立；C4（hierarchy）已降级为 pattern
- 建议将 C1/C2 合并为一个关于 "full trace degradation mechanism" 的贡献

### §2 Method
- §2.3 VOTA 介绍与实验结果不匹配（见 MF-3），建议大幅缩减或移入 Appendix
- Information density 的工作定义应在此节引入

### §3 Experiments
- Table 1：核心结果表设计良好，但 single-seed 标注需完善
- Table 2：仅 Qwen-7B 的组件消融，泛化性不足
- Table 3：24%/76% decomposition 的 confounders 未在 caption 或正文中充分 disclosed
- §3.5 trace length ablation："phase transition" 措辞对 N=4 过精确

### §4 Discussion
- Information density operationalization 出现太晚且存在循环定义
- 应用场景段落需降级为 future directions
- 对 "why full traces hurt" 的机制分析是论文最有价值的部分，应被提升为核心叙事

### §5 Related Work
- 覆盖面广（53 citations），7 个方向合理
- 可补充 data selection 经典文献（Paul 2021, Sorscher 2022）

### §6 Conclusion
- 仅 ~4 行，过于简短。需增加方法论启示、关键局限性摘要、未来方向

### Limitations
- 覆盖 7 个要点，符合 EMNLP 2026 要求
- 序列长度混淆（SF-1）作为核心实验设计限制应被更突出地提及

### Appendix
- 17 节内容丰富详实（训练细节、VOTA 算法、完整结果、去重分析、regex baseline 等）
- Appendix P regex baseline 数据应提升到主文以回应 MF-1