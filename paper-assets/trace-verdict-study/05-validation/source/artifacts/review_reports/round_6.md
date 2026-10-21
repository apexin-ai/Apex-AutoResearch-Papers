---
round: 6
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-21T07:21:26.955684+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 11 (Fresh Review)

**论文**: *Less Is More: Exception Events Outperform Complete Traces for Verdict Prediction*
**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿日期**: 2026-05-21
**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）
**交叉回应**: 完成（双向）

---

## Summary

本文对 trace-based verdict prediction（预测测试通过/失败）进行首个系统性组件消融研究，涵盖 4 个模型（Qwen-7B/1.5B, CodeLlama-13B, DeepSeek-6.7B）、3 个架构家族、1.5B-13B 参数范围。核心发现：仅包含 exception events 的最小表征在所有模型上达到 ≥99.33% 准确率，而包含完整 trace 信息的表征仅达 ~76%——尽管后者是前者的严格信息超集。论文将此归因于"information density"假说：高密度诊断信号（exception events）促进快速收敛（50步），而低密度 trace 内容导致过拟合和震荡。

---

## Strengths

**S1** [共识] 核心发现稳健且反直觉。exception_only ≥99.33% vs full_trace ~76% 的 >23pp gap 在 4 个模型、3 个架构家族上一致复现，差距巨大到即使考虑 single-seed 方差也不会翻转。

**S2** [共识] 消融设计系统全面。7 个 trace 条件（exception_only → ae_only → loop_only → VOTA → VOTA_no_ae → full_trace → no_trace）+ component ablation (Table 2) + budget sweep + training dynamics (Figure 3) + cross-dataset (DebugBench) + regex baseline，构成完整的证据链。

**S3** [共识] 附录极为详尽（12页，A-P 共16子节），覆盖 per-class/per-seed/per-exception-type 分析、训练失败诊断、去重分析、calibration 分析等。透明度在 ACL 论文中不常见。

**S4** [共识] Caveats 讨论诚实。Section 7 主动讨论了 decomposition 非正交性、序列长度混淆、DebugBench 天花板——比多数论文的 Limitations 更坦诚。

**S5** [R1] Training dynamics 分析有价值。Figure 3 展示 exception_only 50步收敛至99.33%，full_trace（即使 label-only loss）全程震荡82-89%不收敛——这提供了超越准确率对比的机制性洞察。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [共识, R1-N1 + R2 AGREE] **24%/76% gradient dilution vs information overload 分解存在严重变量混淆**

`label_only` 条件同时改变至少三个变量：(a) 梯度来源分布（仅 verdict token vs 全序列 token），(b) 有效学习率（单 token loss vs 多 token 平均 loss），(c) 训练目标本身。因此 24% 的 "gradient dilution" 贡献无法与有效学习率变化分离。更严重的是，该分解在 CodeLlama-13B 和 DeepSeek-6.7B 上完全 collapse（label_only 跌至 28.5%），仅在 Qwen 家族（2/4 模型，1/3 架构）成立。Contribution 3 以独立贡献的强度呈现一个仅在单一架构家族成立的 "quantitative decomposition" → 过度承诺。

**建议**：降级 Contribution 3 为 "preliminary/exploratory analysis limited to the Qwen family"，或移入 Discussion 作为假设性分析。理想情况下补充学习率归一化实验以分离 gradient dilution 与 effective LR。

**MF-2** [共识, R1-N2 + R2 AGREE] **Component ablation (Table 2) 仅 Qwen-7B 单模型，不足以支撑 Contribution 4**

Table 2 的 7 组件消融仅在 Qwen-2.5-7B (seed=42) 上执行。Contribution 4 声称 "two-tier diagnostic hierarchy" 跨模型一致——但 ao_only 和 loop_only 在 CodeLlama/DeepSeek 上无数据。Tier 1 的跨模型证据仅来自 exception_only 条件，不包含其他 Tier 1 sub-component。

**建议**：至少在一个非 Qwen 模型上重复 ao_only + loop_only + VOTA 消融（即使 single-seed）。若无法完成，将 Contribution 4 降格为 Qwen-specific observation。

**MF-3** [共识, R1-N3 + R2 AGREE] **绝大多数条件仅 single seed (seed=42)，系统性低估方差**

仅 exception_only 在所有模型上有 3 seeds；其余关键条件（full_trace, VOTA, no_trace 等）大多为 single seed。Bootstrap CI 仅反映 test-set 采样方差，不包含训练过程方差。VOTA vs exception_only 差 0.3-0.5pp 在 single-seed 下完全不可靠。DeepSeek VOTA seed=42 训练失败（84.45%）直接说明某些条件存在显著 seed 敏感性。

**建议**：至少为 full_trace 和 VOTA 在所有模型上补充 2-3 个 seed。明确标注哪些比较是 single-seed、统计意义受限。

### Should-Fix

**SF-1** [Director 裁定, R2-N1 ← R1 REBUT] **核心发现的 novelty 需要 reframing**

R2 认为核心发现 near-tautological（exception 直接编码 verdict，regex B5 达 99.33%）。R1 反驳：(1) R2 数值有误（0.02pp 不存在，实际 0.50pp/6 样本，McNemar p=0.01），(2) nomarker 消融 97.65% 证明 SFT 学习语义而非格式，(3) 核心贡献是 "more info hurts" 而非 "exceptions work"。

**Director 判定**：R1 的事实纠错和 nomarker 反驳有效——论文确实展示了超越 format matching 的学习。但 R2 的底层 concern 成立：regex 99.33% 使 exception_only 结果的 surprise 大幅降低。论文应将 regex 对比从 Appendix 提升到主文，明确区分两层贡献：(a) exception 作为 verdict 高密度 proxy（不令人惊讶）vs (b) 完整 trace 反而严重损害 SFT（核心发现）。

**SF-2** [Director 裁定, R2-N2 ← R1 REBUT] **任务动机需加强，应用场景需降级**

R2 批评 verdict prediction 存在循环动机（获取 trace 即已知 verdict）。R1 反驳：CRUXEval、NExT、Liu et al. (2023) 等 proxy task 在 *CL 有充分先例。

**Director 判定**：R1 的先例论证有效——proxy task 范式在 *CL 被广泛接受。但 Discussion 中三个应用场景缺乏实验验证，应从 "application scenarios" 降级为 "potential future directions"，强化分析性工作的定位。

**SF-3** [共识降级, R2-N3 + R1 部分 AGREE] **Information density 需要工作定义**

全文使用 "information density" 30+ 次无数学定义。R1 指出论文提供了操作性度量（token 数、accuracy、convergence speed）且 loop_only 构成可证伪反例，实证论文不强制要求完整形式化。

**Director 判定**：同意 R1 的降级判断。需在 Section 2 或 3 增加工作定义段落（如 "ratio of diagnostic tokens to total tokens"），但不要求信息论形式化。

**SF-4** [共识] **DebugBench 交叉验证因天花板效应缺乏区分力** — no_trace 已达 96.71%，exception_only 100%，差距仅 0.29pp（约 1 个样本）。应从 "cross-dataset validation" 降级为 "supplementary OOD analysis with ceiling limitations"。

**SF-5** [共识] **序列长度作为混淆变量未被充分隔离** — exception_only ~150 tokens vs full_trace >2048 tokens。性能差异可能部分来自序列长度超出模型处理能力，而非纯粹 "information density"。tail-truncation 分析同时改变了长度和内容。需要 controlled-length 实验（exception_only padding 到 full_trace 长度）。

**SF-6** [共识] **DeepSeek VOTA seed=42 排除有选择性报告之嫌** — 1/3 seed 训练失败 = VOTA 表征在该 tokenizer 下 fragile。应报告含/不含该 seed 的两版结果，Discussion 加 tokenizer compatibility caveat。

**SF-7** [共识] **Abstract "complete traces reach only ~80%" 不准确** — Table 1 跨模型均值约 76.5%，仅 CodeLlama 超过 80%。应改为 "~76%" 或 "72-83%"。

**SF-8** [共识] **数据集范围过窄** — 591 问题，仅 Python，仅竞赛编程。真实代码异常模式更复杂（自定义异常、silent failures）。

**SF-9** [R2] **遗漏相关工作** — R2 指出以下可能遗漏：Paul et al. (2021) "Deep Learning on a Data Diet"、Sorscher et al. (2022) "Beyond neural scaling laws"、Press et al. (2022) "Train Short, Test Long"。此外 Gwak et al. (NeurIPS 2025) 待验证真实性。

### Minor

- Table 1 未一致标注 single/multi-seed 条目（建议用 † 标注）
- 生成模型 (Qwen-7B) = 评估模型之一，可能引入分布偏差（Limitations 应讨论）
- Ethics Statement 提及 "RTX PRO 6000 Blackwell GPUs"，可考虑模糊化
- "Less Is More" 标题虽无因果承诺但较陈词滥调
- chen2025tracepile 引用待核实发表状态
- bib key 与 year 不匹配（qwen2025coder → year=2024）
- Abstract 数据密度偏高（5+ 精确数字）

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识 [AGREE]：

1. **24%/76% 分解方法论不足**：变量混淆 + 仅 Qwen 家族成立 → Contribution 3 需降级
2. **Component ablation 跨模型证据不足**：仅 Qwen-7B → Contribution 4 需补充实验或降格
3. **Single-seed 系统性低估方差**：除 exception_only 外大多数条件缺乏方差估计
4. **DebugBench 天花板效应**：no_trace 96.71% → 无法独立验证 trace 价值
5. **序列长度混淆**：150 vs 2048 tokens → 需要 controlled-length 实验
6. **DeepSeek VOTA 排除**：1/3 seed 失败 = 需报告两版结果
7. **Abstract 数值偏差**：~80% → ~76%
8. **数据集范围**：591 问题/Python/竞赛编程 → 泛化性受限

---

## Reviewer Divergence

以下问题存在分歧，Director 已作裁定：

**D1: 核心发现是否 near-tautological？**
- R2 (2/5 Excitement)：exception 直接编码 verdict，regex B5 已达 99.33%，SFT 边际贡献极小 → Must-Fix
- R1 (3.5/5 Excitement)：R2 数值有误（0.50pp 非 0.02pp）；nomarker 消融 97.65% 证明语义学习；核心贡献是 "more info hurts" 非 "exceptions work" → 降为 Should-Fix
- **Director 裁定**：R1 事实纠错成立，nomarker 反驳有效。但 regex 99.33% 确实削弱 surprise。**降为 Should-Fix**，要求 reframe 而非根本性重构。

**D2: 任务动机是否致命循环？**
- R2：获取 trace 即已知 verdict → circular → Must-Fix
- R1：CRUXEval/NExT 等 proxy task 先例充分 → 降为 Should-Fix
- **Director 裁定**：proxy task 在 *CL 有充分先例。**降为 Should-Fix**，要求应用场景降级但不要求验证。

**D3: Information density 是否必须形式化？**
- R2：Must-Fix（不可证伪）
- R1：Should-Fix（实证论文有操作性度量即可）
- **Director 裁定**：**Should-Fix**。需增加工作定义，不要求完整形式化。

---

## Questions（需作者澄清）

1. `label_only` 条件下调整学习率（使 gradient norm 匹配 exception_only）是否改变 24%/76% 分解结果？
2. `exception_only` 输入 padding 到 full_trace 长度（~2048 tokens，用无信息 token）后性能是否下降？
3. `ao_only` 和 `loop_only` 在 CodeLlama 或 DeepSeek 上是否有消融结果（即使 single-seed）？
4. SFT 比 regex 多正确的 6 个样本具体涉及哪些 case？能否在 Appendix 展示？
5. 除 DeepSeek seed=42 外，其他 seed 上是否观察过 VOTA 训练失败？
6. 更高 LoRA rank (r=32/64) 或更长训练能否缩小 full_trace 与 exception_only 的 gap？

---

## Missing References

已确认遗漏（双方共识或 R2 提出、R1 未反驳）：
- Paul et al. (2021) "Deep Learning on a Data Diet" — 直接研究训练数据质量 vs 数量
- Sorscher et al. (2022) "Beyond neural scaling laws" — data quality/quantity tradeoff
- Press et al. (2022) "Train Short, Test Long" — 序列长度对 transformer 性能的影响

待验证（R2 提出、R1 质疑真实性）：
- Gwak et al. (NeurIPS 2025) "Revisiting the UID Hypothesis in LLM Reasoning Traces" — 若属实则高度相关
- LongCodeZip (2026) — code-specific context compression
- LogSage (2025) — CI/CD failure detection

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Visual Layout Check（非评分项）

状态：**done**（耗时 ~4 分钟）

视觉审查发现 4 个 warning + 4 个 info：

| 严重度 | 位置 | 发现 |
|--------|------|------|
| warning | Pages 1-2 | 前 2 页纯文本无 display item。建议将 Figure 1 提前到 page 2 |
| warning | Page 4 | 单页承载 Figure 1 + Figure 2 + Table 2，视觉过载 |
| warning | Pages 6-8 | 连续 3 页纯文本（§3.5-§6），审稿人容易疲劳 |
| warning | Page 4 | Figure 2 图内文字偏小，低分辨率下难辨认 |
| info | Page 8 | 正文填满 8 页上限，Conclusion 和 Limitations 起始段略拥挤 |
| info | Page 15 | Figure 4 红蓝配色灰度打印时可能混淆 |
| info | Pages 12-21 | Appendix 充实（~10 页），为正文提供充分支撑 |
| info | Page 21 | 附录末页约 60% 填充 |

排版改进建议：将 display items 更均匀地分布在正文 8 页中，避免 pages 1-2 和 6-8 的 "文字荒漠" 与 page 4 的 "视觉过载" 对比。

---

## Overall Assessment

### 评分：**3.0 / 5 (Findings)**

| 维度 | 综合评分 | R1 | R2 |
|------|---------|----|----|
| Soundness | 3/5 | 3.5 | 3 |
| Excitement | 3/5 | 3.5 | 2 |
| Reproducibility | 4/5 | 4 | 4 |
| Overall | 3.0 | 3.5 | 2.5 |
| Confidence | 4/5 | 4 | 4 |

### 评分理由

**核心贡献有价值但存在三个方法论短板。**

论文的主要实证发现——exception_only (≥99.33%) 远超 full_trace (~76%)，且跨 4 模型 3 架构一致——是稳健且有实际指导意义的结果。Training dynamics 分析（Figure 3）提供了超越准确率对比的机制性洞察。写作质量高，附录详尽，caveats 讨论诚实。

但三个 Must-Fix 问题共同削弱了论文的贡献强度：
1. **24%/76% 分解**在 2/4 模型上 collapse，变量未隔离 → Contribution 3 证据不足
2. **Component ablation** 仅 Qwen-7B → Contribution 4 跨模型声称无支撑
3. **Single-seed** 设计使大多数条件间的精确比较不可靠

此外，regex baseline 99.33% 削弱了 exception_only 结果的 surprise（虽然 R1 成功反驳了完全 tautological 的指控），task motivation 需要更清晰的 proxy task 定位。

**综合判断**：当前版本适合 **Findings 接收**。核心实证贡献扎实，但次要贡献（Contribution 3/4）方法论不足，novelty 不够支撑 Main Conference。

**升级路径**（达到 4.0 Conference 水平）：
- (a) 补充 full_trace/VOTA multi-seed 结果
- (b) 至少一个非 Qwen 模型的 component ablation
- (c) 降级 Contribution 3 声称强度
- (d) 增加 information density 工作定义
- (e) Reframe：将 "why richer traces hurt" 而非 "exceptions are best" 作为核心叙事

---

## Detailed Comments（逐节）

### Abstract
- "~80%" → "~76%" 或 "72-83%"（SF-7）
- "all seeds tested under this condition" 措辞需精确限定（仅对 exception_only 成立，其他条件大多 single-seed）
- 数据密度偏高，考虑精简至 3 个关键数字

### Introduction (Section 1)
- 任务动机段应更明确地定位为 proxy task 研究（cite CRUXEval/NExT 先例）
- 应尽早承认 exception events 本身包含强 verdict 信号，突出 "为什么更多信息反而有害" 作为核心问题

### Method (Section 2)
- 需增加 "information density" 工作定义段落
- 数据集描述应提及 Qwen-7B 同时作为生成模型和评估模型之一

### Experiments (Section 3)
- Table 1：增加 † 标注 single-seed 条目
- Table 2：明确标注 "Qwen-2.5-7B only"，避免暗示跨模型泛化
- Table 3 (24%/76%)：需加显著 caveat（"Qwen family only; collapses on CodeLlama/DeepSeek"）
- Section 3.3 (Format Marker Ablation)：nomarker 结果应提升到更显著位置（是反驳 tautological 指控的关键证据）
- Section 3.5 (Trace Length)：需讨论序列长度作为混淆变量

### Discussion (Section 4)
- Regex baseline 对比应从 Appendix 提升到 Discussion 显著位置
- 三个应用场景降级为 "future directions"
- 增加 "limitation of causal claims" 段落
- Fallback design 建议超出证据范围（仅 Qwen-7B 验证）

### Related Work (Section 5)
- 补充 data quality/efficiency 文献（Paul et al. 2021, Sorscher et al. 2022）
- 验证 Gwak et al. (NeurIPS 2025) 并根据相关性决定是否引用

### Limitations
- 增加：(1) 生成模型=评估模型的分布偏差；(2) 序列长度混淆未完全隔离；(3) LoRA rank/训练长度可能影响 full_trace 性能
- Ethics Statement 中 GPU 型号考虑模糊化

### Appendix
- Appendix P (regex baseline) 中的 discordant sample 分析应在正文引用并简要讨论