---
round: 29
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-21T15:27:01.881396+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 28 (Fresh Review)

**论文**: "The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition"
**Venue**: EMNLP 2026 (via ARR, Main Conference Long Paper)
**Deadline**: 2026-05-25
**审稿模式**: Fresh（重新审稿，无上轮记忆）

---

## Summary

本文系统研究了自一致性（self-consistency, SC）在命名实体识别（NER）中的局限性。论文提出"correlation-selection gap"概念：质量估计信号（如 Soft Jaccard、Fleiss κ）与 oracle F1 存在中等相关（ρ up to 0.47, AUROC up to 0.82），但没有任何信号能在 sample selection 层面超越 greedy decoding。通过四阶段诊断级联（QE → degeneracy → agreement fidelity → LP compression），论文定位了 SC 失败的环节。9 类方法、4 个 NER 数据集、2 个模型族的实验均为负面结果。论文同时提出三条"逃逸路径"：LP-weighted entity construction（+1.02–1.40 pp）、cross-model ensemble（+0.42 pp）和 LP selection（+1.39 pp, 仅 Few-NERD），均绕过 entity-level self-verification。

---

## Strengths

**S1. 实验覆盖深度和广度属该领域顶级。** 4 个 NER 数据集（SciERC, CoNLL-2003, Few-NERD, WNUT-17）× 2 个模型族（Qwen3-8B, LLaMA-3.1-8B）× 9 类方法（16+ 配置变体）× 4B/8B/14B/72B scale 消融 × N=2–32 scaling × 温度消融 × free-form vs constrained decoding × cross-task（RE, SQL）。62 张表、47 页附录构成极其详尽的证据网络。Table 62 的 differentiation matrix 清晰定位了本文相对于先行工作的独特贡献。

**S2. 统计方法论远超 NLP 论文平均水准。** Holm-Bonferroni 多重比较校正（k=57 全局 + per-family）、bootstrap 95% CI、TOST 等价检验（含外部锚点）、permutation tests、GroupKFold CV（hidden-state probe）。为负面结果提供了可信的证据基础。**Reproducibility 5/5**：Appendix Table 21 列出全部超参数，NLP Checklist 完整填写，承诺代码/数据开源。

**S3. 诊断框架（四阶段级联）有持久的工具价值。** Degeneracy → agreement fidelity → LP compression 的层次分解为未来研究提供了 operationalizable 的诊断路径。θ_crit = 0.70 的 degeneracy 阈值给出了从业者判断 SC 是否值得尝试的定量依据。

**S4. MBR 理论联系具有原创性。** 将 entity-level construction 形式化为 MBR decoding under entity-wise independence（Proposition 1-2），在文献中是新颖的。Corollary 1 给出 SC gain 的 closed-form 必要条件。

**S5. Introspection gap 是有价值的发现。** Hidden-state probe（AUROC 0.63–0.88）超越 prompt-based self-judgment（0.51）但低于 multi-sample agreement（0.87, 仅 CoNLL），揭示模型内部表示包含 prompt 接口无法访问的质量信息。

**S6. 写作质量高。** 术语一致，叙事逻辑清晰（问题定义 → 诊断 → 失败分析 → 逃逸路径），Limitations 坦诚且具体。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [Critical] 标题"Capability Ceiling"与 observational 证据不匹配，因果语言贯穿全文。**
[R1-N1, R2 AGREE | 共识]
- 四阶段级联基于观察性关联，Figure 1 caption 标注 "diagnostic sequence, not causal chain"，Limitations 承认 "not interventional"——但标题"Capability Ceiling"暗示已证明的硬上界，§9 使用 "governs"，Abstract 使用 "explaining where and why"。
- LoRA-rank 消融（degeneracy 17.8%→7.2%）和温度扫描提供了有限的 quasi-interventional 证据，但不足以支撑 "ceiling" claim。
- **建议**：(1) 修改标题，降低因果强度（如 "Diagnostic Analysis of..." 或 "Characterizing..."）；(2) §1 或 §3 明确声明 observational 性质；(3) 全文统一将因果动词替换为相关性语言。无需新实验。

**MF2. [Critical] 核心统计 claim 在严格多重比较校正下不稳健，正文与附录存在矛盾。**
[R2-N1, R1-M3 aligned | 共识]
- Appendix f（line 317）声称全局 Holm-Bonferroni（k=57）下 "no core NER claim survives（p_adj=0.055 for Few-NERD LP selection and construction）"。但 experiments_main.tex（line 244）声称 Few-NERD construction "+1.40±0.51 pp, p<0.001; survives Holm-Bonferroni at k=57"——**两处表述直接矛盾**。
- 正文 §7.5 使用 per-family 校正（selection k=21, construction k=10），但 per-family 分割的预注册依据不足。SciERC construction p_adj=0.20 不显著。
- **建议**：(1) 核实 construction 的 exact p_raw 和 Holm rank，修正矛盾表述；(2) 正文 §7.5 添加显式指向 Appendix f 的说明，告知读者全局校正结果；(3) 提供 per-family 分割的先验 justification 或补充 permutation test/Bayesian 分析。

**MF3. [Critical] "Correlation-selection gap"与 MBR 文献已知发现的增量新颖性需更精确定位。**
[R2-N2, R1 部分分歧 | 单方 Must-Fix，但 Director 判定有效]
- Eikema & Aziz（2020, 2022）已证明 MAP decoding 不足，Eikema et al.（2025）指出 MBR utilities 在 structured outputs 退化。§8 讨论 MBR 但聚焦 utility function 选择，未明确论证诊断 cascade 的增量价值——即 MBR 文献指出问题存在，本文定位问题在哪个环节发生（degeneracy vs LP compression vs signal alignment），这是真正的新贡献。
- R1 在优势 #3 中赞赏 MBR 理论联系的原创性，但这不影响 Related Work 中需要更精确的差异化表述。
- **建议**：§8 增加 explicit comparison 段落，用 3-4 句说明 MBR utility degradation vs correlation-selection gap 的区别与联系。

### Should-Fix（影响评分但不一票否决）

**SF1. 理论 bound 过松（actual/bound ratio 3–12×），定位需调整。**
[R1-W1, R2 AGREE | 共识]
- Table 30 显示 bound 仅捕获实际 gain 的 5–12%，signal alignment α 是瓶颈（best signal 恢复非退化 oracle gap 的 6.8%）。
- θ_crit = 0.70 提供了有效的定性预测力（necessary condition），但 quantitative bound 对实际决策指导有限。
- **建议**：§6.3 明确将 bound 定位为 necessary condition 而非 tight bound，正文讨论 tightness 和失败条件。

**SF2. Hidden-state probe 跨数据集 AUROC 方差（SciERC 0.63 vs CoNLL 0.88）未充分解释。**
[R1-W2, R2 AGREE | 共识]
- Cross-dataset transfer 下降显著（Few-NERD→CoNLL=0.759, CoNLL→Few-NERD=0.671）。CoNLL 高 AUROC 不能转化为 selection gain——因为 probe 是 instance-level signal，无法区分 per-sample candidates。
- **建议**：(1) §3 补充 CoNLL 简单任务使错误 entity 在 hidden space 中为更明显 outlier 的解释；(2) 明确说明高 AUROC 不转化为 selection gain 的结构性原因。

**SF3. Escape routes 效果量偏小，cost-effectiveness 未定量分析。**
[R1-W3, R2-W4 | 共识]
- +1.02–1.40 pp (N× cost), +0.42 pp (2N× cost), +1.39 pp (仅 Few-NERD)。Discussion 承认 "N× cost for ≈1 pp may only justify safety-critical use"。Table 61 在 Appendix 但主文未引用，缺 Pareto 曲线。
- **建议**：明确区分 proof of concept vs practical recommendation；主文引用 Table 61 或添加简化的 cost-benefit 讨论。

**SF4. N-scaling 止步于 N=32，未讨论更大 N 的外推。**
[R1-W4, R2 部分 AGREE | 共识]
- N=32 时 degeneracy 降至 4% 但 selection Δ 仅 +0.95 pp（p=0.091, CI 跨零），说明瓶颈是 signal alignment 而非 candidate pool size。但论文引用 Brown et al.（2024）却未讨论 N=100+ 外推。
- **建议**：Appendix s 增加基于 scaling law F₁(N) = a − b·N^{−c} 的外推讨论。

**SF5. 模型覆盖有限，泛化性措辞过度。**
[R1-W5 + R2-W1 | 共识]
- 完整实验仅 Qwen3-8B 和 LLaMA-3.1-8B（LoRA 微调），共享训练流程可能限制 diversity 上限。72B 仅 Few-NERD，GPT-5.5 仅 200 实例。Limitations 承认 frontier models degeneracy 不同（4%–5.5%）。
- **建议**：弱化 Introduction/Conclusion 泛化性措辞，明确区分 "fine-tuned open-weight models" 和一般性结论。

**SF6. Cross-task validation 薄弱。**
[R2-W2 | 单方]
- RE 仅 SciERC 一个数据集，55.5% zero-F1 来自 entity span 错误——测量的是 NER→RE 错误传播而非 RE 本身。SQL 仅提到 87.2% degeneracy 缺系统分析。
- **建议**：(1) RE 分析加 span error 混淆的 caveat；(2) 降低 cross-task generalization claim 强度。

**SF7. 遗漏直接相关参考文献。**
[R2-W3 | 单方]
- Ma et al.（2024）"Self-Improving for Zero-Shot NER with LLMs"（NAACL）——直接使用 SC 进行 NER 获正面结果，与本文负面结果形成有意义对比（zero-shot vs fine-tuned）。
- Madaan et al.（2023）"Self-Refine"（NeurIPS）——MRSC 方法的直接先行工作。
- **建议**：§8 加入讨论。

---

## Reviewer Consensus

| 问题 | R1 | R2 | 交叉结果 |
|------|----|----|---------|
| MF1: 因果语言/标题 | Must-Fix | [AGREE] | **强共识** |
| MF2: 统计稳健性/Holm 校正 | M3 aligned | Must-Fix | **共识** |
| MF3: MBR 新颖性定位 | 优势#3 原创 | Must-Fix | **部分分歧**（见下） |
| SF1: 理论 bound 松弛 | Should-Fix | [AGREE] | 共识 |
| SF2: Probe 方差 | Should-Fix | [AGREE] | 共识 |
| SF3: Escape routes 效果量 | Should-Fix | [AGREE] | 共识 |
| SF4: N-scaling 范围 | Should-Fix | [AGREE]（部分） | 共识 |
| SF5: 模型覆盖 | Should-Fix | [AGREE] | 共识 |
| R1-N2: SciERC free-form 缺失 | Must-Fix | **[REBUT]** | **R2 正确，R1 事实性误读** |

---

## Reviewer Divergence

**R1-N2（SciERC free-form decoding 缺失）**：R1 声称 free-form 消融未覆盖 SciERC，R2 引用 Appendix q Table `tab:freeform_ablation` 反驳。**Director 核实：R2 正确**——appendix.tex:1154-1165 明确标注 Free-Form Decoding Ablation 以 SciERC 为首要数据集，4-panel 分析完整，NER selection 在 free-form 下仍然无效（gap 从 +0.0059 降至 +0.0018）。R1-N2 不构成有效 Must-Fix，已从最终评估中移除。

**MF3（MBR 新颖性）**：R1 在优势评价中赞赏 MBR 理论联系的原创性（Proposition 1-2 将 entity construction 形式化为 MBR decoding "在文献中是新颖的"），R2 则认为核心概念在 Eikema et al.（2025）中已有类似表述。Director 判断：两者不矛盾——MBR formalization 本身有原创性，但 §8 对 MBR 文献的差异化定位确实不够精确。列为 Must-Fix 但修改量可控（增加几句 Related Work 即可）。

---

## Questions（需要作者澄清）

1. **Holm 校正数值不一致**：experiments_main.tex 声称 Few-NERD construction "survives Holm-Bonferroni at k=57"，但 Appendix f 声称 "no core NER claim survives（p_adj=0.055）"。请核实 exact p_raw 和 Holm rank。
2. **Abstract k=21 vs 正文**：Abstract 报告 "selection family k=21"——请确认 Appendix f Table 13 的 selection family 实际行数是否为 21。
3. **Proposition 1 entity-wise independence**：NER 中相邻实体预测常相关（如 "New York" 和 "City"）——该假设何时 violated？violation 对 bound 的影响如何？

---

## Missing References

1. **Ma, Wang, Sun & Li (2024). "Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models." NAACL 2024.** — 直接使用 SC 进行 NER 获正面结果，最相关先行工作。
2. **Madaan, Tandon, Gupta et al. (2023). "Self-Refine: Iterative Refinement with Self-Feedback." NeurIPS 2023.** — MRSC 方法的直接基准。
3. **Wei, Wang, Schuurmans et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." NeurIPS 2022.** — SC 的前置基础工作。
4. **"Test-time Scaling of LLMs: A Survey" (2025, arXiv:2511.14772)** — TTS 分类框架，有助于定位本文的 inverse scaling 发现。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 `external_review.paperreview_ai.enabled`）。

---

## Visual Layout Check（非评分项）

状态：**done**（耗时 4m9s）

**Findings（4 warnings, 18 info, 0 critical）**：

- **[Warning] 前 2 页纯文本**：Title/Abstract/Introduction/Contributions 连续两页无 display item，Figure 1 直到第 3 页才出现。建议将 Figure 1 提前或在第 2 页插入简化版视觉锚点。
- **[Warning] 前 2 页无 figure/table/equation**：可改进的节奏问题，但 Introduction 纯文本在 NLP 论文中常见。
- **[Info] 中段视觉节奏良好**：p3-7 text-table-figure 三重奏交替频繁，9-10 个 display items 密度适合实证诊断论文。
- **[Info] 色盲友好性**：Figure 1 绿/红对比有 ✓/✗ 符号冗余编码，影响有限。建议红→橙。
- **[Info] Figure 4**：4 子图面板字号接近可读性下限（约正文 65-70%）。
- **[Warning] Appendix p.41, p.47 大面积空白**（>50% 页面），建议合并 float。
- **[Info] 无 LaTeX 渲染错误、overfull hbox、orphan heading、未解析引用。**
- **[Info] 正文 8 页，Limitations 在 page 8 结束，符合 EMNLP 2026 格式要求。**

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 4/5 | 3.5/5 | **3.75/5** |
| Excitement | 3/5 | 3/5 | **3/5** |
| Reproducibility | 5/5 | 4/5 | **4.5/5** |
| Overall | 3.5 | 3.5 | **3.5** |
| Confidence | 4/5 | — | **4/5** |

**判断依据**：
- **Soundness 高于平均**：实验设计和统计方法论在 NLP 论文中属于顶级水平，但因果语言与 observational 证据的张力、以及正文/附录 Holm 校正结果的矛盾需要修复。
- **Excitement 中等**：诊断框架有工具价值，对社区有指导意义（何时 SC 有效/无效），但核心发现（SC 对结构化输出效果差）对熟悉 MBR 文献的读者并不意外；escape routes 增益微弱（+1.0–1.4 pp at N× cost）。
- **Reproducibility 极优**：47 页附录、62 张表、完整超参数记录、代码开源承诺。

**升级到 4（Conference）的路径**：修复 MF1（标题/因果语言）、MF2（统计矛盾）、MF3（MBR 差异化）可使论文升至 Borderline Conference 上端。SF3（cost-effectiveness 量化）和 SF7（missing references）是加分项。如果同时加强 MBR 新颖性定位（MF3），有望达到 3.5–4 区间。

**降级到 3（Findings）的风险**：如果 MF2 的矛盾表明 Few-NERD construction 实际不过 Holm 校正，则唯一正面结果被削弱；如果 MF3 的 MBR 差异化无法令人信服，则核心概念新颖性不足。

---

## Detailed Comments

### §1 Introduction
- "Capability Ceiling" 标题需降级（MF1）。Introduction 叙事弧流畅，从 SC 在 reasoning 的成功到 NER 的结构性限制过渡自然。四个 contribution 清晰但第 4 个（prescriptive escape routes）在统计稳健性上最脆弱。建议在 contribution 列表中明确标注诊断框架的 observational 性质。

### §2 Quality Estimation
- §2.2 定义 4 种信号但 LP 在 §2.3 才引入——结构上可改善（R1-M2）。Table 1 "†One score per input" 与 per-sample/instance-level 区分重叠（R1-M1/R2 小问题 1）。

### §3 Mechanistic Analysis (Hidden-state Probe)
- AUROC 0.63–0.88 跨数据集方差的原因需补充解释（SF2）。Cross-dataset transfer 下降是重要的 negative finding，但未被充分阐释。建议添加 explicit takeaway：即使 AUROC=0.88，instance-level 设计限制仍然阻止 selection 改善——这恰恰印证了 correlation-selection gap。

### §4 Selection Gap
- 核心诊断逻辑自洽但语言需统一为 observational（MF1）。

### §5 Escape Routes / §7.5 Prescriptive
- +1.40 pp (Few-NERD construction) 和 +1.39 pp (LP selection) 是论文的核心正面结果。正文声称前者 survives global Holm 但附录否认——必须修正（MF2）。Cost-effectiveness 讨论需从 Appendix 提到正文（SF3）。

### §6 Theory
- Proposition 1-2 的 MBR 形式化有原创性。Degeneracy bound 过松但 θ_crit = 0.70 的定性预测力有价值（SF1）。Entity-wise independence 假设需补充讨论（Q3）。

### §8 Related Work
- MBR 文献差异化是关键改进点（MF3）。Ma et al.（2024）和 Madaan et al.（2023）是明显遗漏（SF7）。

### §9 Discussion
- 因果语言（"governs"、"explaining where and why"）需替换为相关性语言（MF1）。

### Limitations
- 坦诚且具体。建议增加 closed-source API 模型 degeneracy profile 差异的讨论（Claude 74% vs DeepSeek 5.5%）。

### Appendix
- 34 页附录体量大但内容充实。核心 findings 高度依赖附录表格（如 Table 13 Holm 校正、Table 30 bound tightness），建议在正文中提供更自包含的数字摘要。