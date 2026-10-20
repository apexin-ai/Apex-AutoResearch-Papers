---
round: 14
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-25T08:17:39.958035+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# Round 14 审稿报告 — trace-verdict-study

**投稿目标**: EMNLP 2026 (via ARR)  
**审稿模式**: Fresh (重新审稿)  
**Reviewer 编排**: 2 人（R1: 方法严谨性/统计方法论 | R2: 新颖性/贡献显著性）  
**交叉回应**: 已完成，16 个问题中 14 个 [AGREE]，2 个 [REBUT]  

---

## Summary

本文研究执行 trace 格式对 verdict prediction（判断代码是否通过测试）微调效果的影响。通过 4 个 code-specialized 模型（1.5B-13B）、7 种 trace 条件的系统消融实验，发现仅包含 exception 信息的最简 trace 格式即达到近完美准确率（99.83%），而完整 trace 反而导致 18-23pp 的性能退化。论文尝试通过 gradient masking 分解将退化归因于训练时梯度稀释（≤4%）和推理时信号稀疏（~76%）。

---

## Strengths

1. **实验设计系统性强**：7 种 trace 条件构成完整的信息量梯度，消融层次清晰（format markers → component → gradient masking → truncation → cross-dataset），实验设计本身具有方法论示范价值。

2. **透明度高**：outlier 排除（DeepSeek VOTA seed 42）有完整根因分析和独立验证（Appendix F），未隐藏不利结果；CodeLlama head-2048 proxy 在 Limitations 中主动披露；clustered bootstrap 在脚注中报告。

3. **"More information hurts" 的方向性发现有价值**：full_trace 严格包含 exception_only 的全部信息，却导致显著性能退化——这个反直觉发现本身值得报告，且对 trace-augmented pretraining/fine-tuning 的实践有参考意义。

4. **Calibration 分析**：ECE 从 0.171（full_trace）到 0.0027（exception_only）的差异，配合 reliability diagram（Figure 4），提供了超越准确率的评估视角。

5. **消融深度**：Appendix I 的 exception subcomponent ablation（exc.type.only 达 100%）和 Appendix J 的 truncation position 实验提供了细粒度的诊断信息，虽然这些数据同时也暴露了 shortcut 风险。

---

## Weaknesses

### Must-Fix（不修复则不建议接收）

**[MF-1] Exception 信号优势的结构性 shortcut 未被排除** [共识: R1 AGREE, R2 AGREE]
- Exception_only 的 99.83% ceiling 在很大程度上是 structurally expected：exception events 直接编码 verdict direction（有 exception → fail，无 exception → pass）。论文 Abstract 自己承认 "this ceiling is expected"。
- 三个具体的替代解释未被排除：
  - **(a) 格式熟悉度**：exception message 格式（`TypeError: ...`）在预训练语料中高频出现，模型可能因 distribution match 而非语义理解获得优势。§4.3 的 format marker removal 仅移除了 `[ERROR]` 标记，未控制 exception message 本身的预训练分布匹配度。
  - **(b) 位置集中度**：Appendix J 证实诊断信息集中在 trace 末尾。"位置"而非"密度"可能是更精确的解释变量。
  - **(c) 长度不对称**：Fail cases 含 traceback ~150 tokens，Pass cases 仅短文本 `[No exception data in trace]`，模型可能学到长度 heuristic。Appendix I 的 exc.type.only（仅 exception 类名一个词）达 100%，加剧了 shortcut concern——模型可能退化为规则匹配。
- B5 regex baseline 已达 93.61%，与 SFT exception_only（99.83%）仅差 6.22pp，进一步支持 shortcut 假说。
- **核心问题**：论文将 exception_only 的优势归因于"信息密度"效应，但上述证据表明结构性/表面特征可能是更主要的解释。这一区分直接影响论文的理论贡献。

**[MF-2] 因果声称超出证据强度，gradient masking 分解的可加性假设未验证** [共识: R1 AGREE, R2 AGREE, R1 升级为 critical]
- Abstract 使用 "quantify why more information hurts"，Section 5 使用 "determines" 级别的因果表述，但实验证据是受控消融下的相关性。
- §4.4 的 gradient masking 分解假设训练时效应和推理时效应可加（total = gradient dilution + complementary confounded）。但 CodeLlama label-only tail-2048 collapse 至 41.8%（Table 3）证明两种效应存在非加性交互——性能不是简单叠加下降，而是 catastrophic degradation。
- "24%/76%" 的精确百分比呈现与 "upper bound" 的 framing 矛盾：读者看到 "24%" 时理解为精确分解而非上界估计。
- label-only loss 仅在 Qwen 家族有效（CodeLlama/DeepSeek collapse 到 majority baseline），作为 gradient dilution 的补充证据力度不足。
- **建议**：全文搜索 "determines"/"quantify why" 等因果表述并降级；移除百分比表述改为 range（"gradient dilution contributes at most ~4pp of the ~18pp gap"）；Discussion 显式列出未排除的 confounds。

**[MF-3] Wilson CI 在 49% 重复样本下的有效性** [共识: R1 AGREE, R2 AGREE]
- Exception_only 条件下同一 problem 的多个 candidate solutions 产生相同 exception pattern（Appendix G 显示 exception_only 仅 2 个 error set），problem-level clustering 真实存在。
- 主表 Wilson CI 基于 N=1,190 计算，但有效独立样本约 607（problem-level）或低至 119（clustered bootstrap n_eff）。约 10 倍的 N 差异意味着某些看似显著的差异（尤其 Tier 2 条件间）可能不显著。
- 3/80 comparisons 在 Bonferroni 校正后失去显著性，但未在正文披露。
- **建议**：主表同时报告 Wilson CI 和 clustered CI，或至少正文明确说明 clustered CI 是否改变核心结论。

### Should-Fix（影响论文质量但不阻碍接收）

**[SF-1] GPT-4o 对比的误导性** [共识: R1 AGREE, R2 AGREE]
- Zero-shot GPT-4o vs SFT Qwen-7B 混淆学习范式和输入格式两个变量。Abstract 中高亮构成 prominence elevation，即使有 "(zero-shot, not directly comparable to SFT)" caveat。
- GPT-4o 数字仅出现在 Abstract 和 §1，正文缺乏可复现的实验配置表格。
- **建议**：从 Abstract 移除 GPT-4o 比较，或在正文增加完整实验表格。

**[SF-2] DCSH 增量贡献界限模糊** [共识: R1 AGREE with qualification, R2 提出]
- §2 对 DCSH 的定位过弱——"在不同任务上做了更细的消融" novelty 有限。
- R1 指出真正增量包括 two-tier signal hierarchy 量化、trace length phase transition、calibration analysis，但正文未显式列出。
- **建议**：§2 中用具体列表明确列出相对 DCSH 的增量。

**[SF-3] 模型覆盖同质性高，"across architectures" 声称过强** [共识: R1 提出, R2 AGREE]
- 4 个模型全部是 decoder-only、code-specialized、1.5B-13B、LoRA fine-tuning。
- Limitations 承认了覆盖限制，但正文 §4.1 "across four models and three architecture families" 给人更强的 generalization 印象。
- **建议**：正文加入覆盖范围限制的 qualification。

**[SF-4] DebugBench margin 过窄** [共识: R1 AGREE, R2 提出]
- no_trace 在 DebugBench 已达 96.71%，headroom 仅 3.29pp。Ranking preservation 的 discriminative power 有限。
- DebugBench 的 synthetically injected single-point mutations 使任务过于简单。
- **建议**：DebugBench 结果降级为补充证据，不作为 generalization 的主要证据。

**[SF-5] Training dynamics 单 seed 证据不充分** [共识: R1 提出, R2 AGREE]
- Figure 5 仅展示 1 个 seed 的训练曲线。"full_trace with label-only loss oscillates (82-89%) without convergence" 需至少 3 seeds 验证。
- **建议**：增加 seeds 或将声称限定为 "observed in this seed"。

**[SF-6] CodeLlama full_trace head-2048 proxy** [共识: R1 AGREE, R2 AGREE]
- Head truncation 切掉 trace 末尾诊断信息，Table 1 中 84.63% 可能是下界估计。
- 此 proxy 也影响 §4.4 decomposition 的可靠性——18.07pp gap 可能被高估。
- Limitations 已披露，影响有限但应注意。

**[SF-7] Abstract 数字密度** [共识: R1 AGREE, R2 AGREE]
- 169 words 含 12+ 数字，过于密集。
- **建议**：次要数字替换为定性描述，精确数字保留在 §1。

**[SF-8] VOTA tokenizer efficiency 作为系统性限制** [R2 REBUT R1-W3, 但共识 tokenizer 是系统性问题]
- Seed 42 排除本身合理（tokenizer truncation 有确定根因），但 tokenizer efficiency 应在 Discussion 中提升为 VOTA 方法论的已知限制。

---

## Reviewer Consensus

两位 Reviewer 在以下关键判断上达成共识：

1. **Exception 信号优势可能更多来自结构性/表面特征（同义反复性、长度不对称、格式熟悉度、位置集中度）而非论文声称的"信息密度"效应。** 这是决定接收水平的核心 concern。
2. **因果声称需全面降级**："determines" → "strongly predicts"，"24%/76%" → range 表述。
3. **统计 CI 需修正**：主表应反映 clustered CI 或明确说明影响。
4. **GPT-4o 对比应从 Abstract 移除或补充完整实验表格。**
5. **叙事重心应从 exception ceiling 转向 degradation mechanism**：§4.1 篇幅应压缩，§4.4/§5 应扩展。
6. **论文在实验透明度和消融设计方面表现优秀**，但理论贡献被上述方法论问题削弱。

## Reviewer Divergence

**[分歧] Task significance（R2: critical → 3.0 | R1: warning → 3.5）**
- **R2 立场**：Binary verdict prediction 过于简单（执行代码即可获得 ground truth），contribution 的 generalizability 受限。建议增加 non-trivial downstream task 验证。
- **R1 立场**：Verdict prediction 有实际应用场景（sandboxed environments、resource-constrained CI、execution-aware pretraining），且论文定位为 case study，verdict prediction 是研究信息密度效应的 vehicle 而非最终目标。Case study 的 contribution 模式在 *ACL 是被接受的，前提是 case study 本身足够深入（本文的 ablation 深度达标）。应降级为 warning。
- **Director 判定**：R1 的 case study 论证合理，但 R2 对 generalizability 的担忧也有道理。此分歧不影响核心 weakness 判断——即使 task significance 被接受，MF-1/MF-2/MF-3 的方法论问题仍需解决。本分歧对最终评分影响为 ±0.5。

---

## Questions

1. 如果对 pass cases 填充随机文本使输入长度与 fail cases 对齐，exception_only 的准确率是否仍为 99.83%？
2. Clustered CI（n_eff=119）下，Table 1 中哪些 condition pairs 的差异变得不显著？这是否改变任何核心结论？
3. 论文是否测试过 forward-pass attention pattern——full_trace 条件下模型对诊断 tokens 的 attention weight 分布如何？这可以直接测量信号稀释。
4. Appendix I 中 exc.type.only（仅 exception 类名）达 100%，这是否意味着模型在 exception_only 条件下本质上是在做规则匹配而非语义理解？

---

## Missing References

两位 Reviewer 共识缺失以下引用：
1. **Shi et al. (2023)** "Large Language Models Can Be Easily Distracted by Irrelevant Context" — 与 inference-time signal sparsity 直接相关
2. **LDB (Zhong et al., 2024)** — trace-based debugging with segment-level verification
3. **SelfDebug (Chen et al., 2024)** — iterative self-debugging with execution feedback
4. **Reflexion (Shinn et al., 2023)** — verbal reinforcement + execution feedback 框架，与本文 "trace format affects learning" 发现形成有意义的对话

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Visual Layout Check（非评分项）

**状态**: 已完成（耗时约 4 分钟）

| 严重度 | 位置 | 发现 |
|--------|------|------|
| ⚠️ Warning | pp.3-4 | 连续两页纯文本（Method §3.1-3.5），无 figure/table/equation，缺乏视觉锚点。建议在 §3.3 附近加示例对比表或 trace 示例图 |
| ⚠️ Warning | p.5 | 三个 display items（Table 1 + Table 2 + Figure 2）堆叠同一页，与 pp.3-4 纯文字形成强烈反差。考虑前移 Table 2 或 Figure 2 平衡节奏 |
| ⚠️ Warning | pp.8-9 | Conclusion 从 p.8 右栏底部开始，正文延续至 p.9。**可能超出 EMNLP 8 页正文限制**。建议压缩 Discussion/Conclusion 或移 Figure 4/5 之一至 Appendix |
| ℹ️ Info | p.1 | 首页无 display item，Figure 1 在 p.2 顶部。非最优但可接受 |
| ℹ️ Info | p.5 | Figure 2 axis labels 和 legend 偏小（<7pt），打印后可能难辨认 |
| ℹ️ Info | p.8 | Figure 4/5 中部分标注文字偏小，打印阅读困难 |
| ✅ Good | p.7 | Figure 3 颜色+线型双重编码，色盲友好 |
| ✅ Good | 全文 | Tables 使用 booktabs 风格，格式规范 |
| ✅ Good | p.9 | Limitations 简短（~3 点），符合 EMNLP 要求 |
| ✅ Good | pp.9-21 | References 和 Appendix 表格格式一致，无未解析引用 |

**⚠️ 格式风险**：pp.8-9 的页数可能超限，需确认正文是否严格在 8 页内。

---

## Overall Assessment

**评分: 3.0 — Findings**

**置信度: 4/5（High）**

本文在实验设计的系统性和透明度方面表现出色，7 种 trace 条件的消融矩阵和完整的 outlier 分析体现了扎实的实证研究素养。"More information hurts" 的方向性发现有实践参考价值。

但核心理论贡献被以下方法论问题削弱：(1) exception 信号优势的多个结构性 shortcut 替代解释未被排除，"信息密度"归因缺乏说服力；(2) gradient masking 分解的因果声称超出证据强度，可加性假设有反例；(3) 统计推断存在 CI 膨胀问题。这些问题使得论文的核心 narrative——从 "what"（exception 最好）到 "why"（信息密度机制）——的可信度受限。

**R1 评分 3.5（Borderline Conference）**——认为 case study contribution 模式合理，ablation 深度达标，若修复 MF-1/MF-2 的叙事和因果声称问题可达 Conference。
**R2 评分 3.0（Findings）**——认为 task significance 不足以支撑 Conference，exception tautology 是结构性缺陷。

**Director 综合判定**：3.0（Findings）。论文作为 detailed empirical case study 达到 Findings 门槛——实验工作扎实、报告透明、发现对实践有参考价值。但结构性 shortcut 未排除和因果声称过强这两个核心问题在当前版本无法通过写作修改解决（需要额外控制实验），阻止了向 Conference 的晋升。如果在 revision 中增加 balanced-length ablation 和 attention analysis 排除关键 shortcut，评分有上调空间。

---

## Detailed Comments

### §1 Introduction
- Contribution list 已压缩为 3 条，改善明显。
- 但 "quantify why more information hurts" 的因果表述仍偏强，建议改为 "characterize how..."。

### §2 Related Work
- DCSH 定位需加强——用具体列表明确增量。
- 补充 LDB、SelfDebug、Reflexion、Shi et al. 2023。

### §3 Method
- 实验设计清晰，7 种 trace 条件的描述完整。
- pp.3-4 连续纯文字，建议加入 trace 格式示例对比表。

### §4 Results
- §4.1 花大量篇幅确认 expected result（exception ceiling），应压缩为 1-2 段。
- §4.3 Format marker removal 实验有价值但不够——移除 `[ERROR]` 标记不等于排除格式熟悉度 confound。
- §4.4 Gradient masking decomposition 的 "24%/76%" 应改为 range 表述。Table 3 重新 frame 为 upper bound estimation。
- §4.5 Calibration 分析是亮点，保持。

### §5 Discussion
- 需增加 confound 讨论段落（格式熟悉度、位置集中度、长度不对称作为替代解释）。
- 因果表述全面降级。

### §6 Conclusion
- 检查是否超出 8 页限制。

### Appendix
- Appendix I 的 exc.type.only = 100% 是重要数据点，但目前被埋在附录——其对 shortcut 假说的 implication 应在正文讨论。
- Appendix J 的 truncation 实验完整有价值。

### Figures
- Figure 2/4/5 字号偏小，建议放大至 ≥8pt。
- Figure 5 训练曲线需增加 seeds。
