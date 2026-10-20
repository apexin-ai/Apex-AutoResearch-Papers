---
round: 9
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T03:51:44.461407+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 14 (Fresh Review)

**论文**: *Complete Execution Traces Impair SFT-Based Verdict Prediction: An Information Density Analysis*
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性/实验设计/统计分析; R2: 新颖性/写作质量/相关工作/格式合规）
**圆桌轮次**: 1 轮（Round 1 独立审稿 → 交叉分享 → 收敛）

---

## Summary

本文研究执行轨迹表示对 SFT 判定预测（pass/fail 分类）的影响。在 4 个代码 LLM（Qwen-2.5-1.5B/7B、CodeLlama-13B、DeepSeek-6.7B）上系统比较 7 种 trace 条件，发现完整执行轨迹（full_trace，>2048 tokens）仅达 72–82% 准确率，而仅包含异常信息的紧凑表示（exception_only，~150 tokens）达 ≥99.33%，18+pp 差距跨模型稳健。论文提出信息密度框架，将性能差距分解为梯度稀释（~26%）和推理时信息过载（~74%），并通过 truncation budget curve、padding 控制实验和 DebugBench 泛化验证支撑结论。

---

## Strengths

**S1. 稳健的核心发现，跨架构一致**
exception_only 在全部 4 模型 3 架构家族上均达 ≥99.33%（Table 1），与 full_trace 的 18+pp 差距在所有配置下均通过非重叠 CI 确认。padding exception_only 到 2,048 tokens 后准确率不变（Section 3.5），有效排除序列长度混淆。

**S2. 精心设计的控制实验矩阵**
7 种 trace 条件构成信息梯度，配合 format marker ablation、loss ablation、truncation direction analysis（Appendix I）、budget curve（Figure 4）、padding control。每个潜在 confound 都有对应控制实验。

**S3. 实用的两层诊断层级**
Tier 1（exception signals ≥98.53%）vs. Tier 2（loop compression 77–86%）的 12+pp gap 提供了清晰的工程指导。

**S4. 充分的再现性细节**
Appendix 提供完整超参数（Table 5）、wall-clock 时间（Table 6）、VOTA 提取算法（Algorithm 1）、per-seed breakdown（Appendix A）。

**S5. padding 控制实验有效排除长度混淆**
exception_only padded 到 2,048 tokens 后准确率不变，确认 18+pp 差距归因于 full_trace 噪声信息而非序列长度本身。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [Consensus: R1-N1 + R2-AGREE] **label_only 分解存在多重未控制的混淆变量**
26%/74% gradient dilution vs. information overload 分解（Section 3.4, Table 3）是论文的关键分析贡献。但 label_only loss 同时改变：(a) 有效学习率（~2048 tokens 平均 vs 1 token，~2000× 差异），(b) 训练目标（移除 trace 生成的隐式正则化），(c) 优化景观（高维 → 单 token 目标）。论文使用 "approximate decomposition" 和 "upper/lower bound" 表述，但未明确报告 LR 设置，未讨论这些具体混淆因素。CodeLlama 和 DeepSeek 的 label_only collapse（28.5%）说明分解方法本身不稳定（仅 2/4 模型、1/3 架构成功）。Abstract 中 "at least ~74% to information overload at inference" 未限定 Qwen-family。

**MF-2** [Consensus: R2-N1 + R1-AGREE with nuance] **核心发现新颖性受限——near-tautological**
Exception events 结构性编码 verdict：失败测试必然产生 exception，通过测试则无 exception。Regex baseline B5 仅通过检测 format marker 即达 99.33%，与 SFT 99.83% 仅差 0.50pp。nomarker 消融下 SFT semantic advantage 仅 ~2pp（97.65%）。"Less Is More" / "more information hurts" framing 高估了反直觉性——这更接近特征选择/信噪比的已知 ML 原理。R1 承认但指出系统性分析（7 条件 × 4 模型的 information gradient + component ablation + truncation analysis）提供了超越 tautological observation 的工程洞察。**Director 判定**：论文应重新定位 contribution——从 "fundamental insight" 转为 "systematic quantification of trace component signal content + practical representation design principles"。

**MF-3** [Consensus: R2-N3 + R1-W4, both AGREE] **"Information density" 定义循环且未正式度量**
Section 2.1 给出两个不等价定义：(1) verdict-diagnostic tokens 占总 token 数的比例（数据属性），(2) 每 token 带来的 accuracy improvement（模型性能属性）。用准确率（因变量）操作化自变量（density）构成循环论证。全文未将 information density 作为连续变量正式计算——没有任何 condition 的具体 density 数值。对于一篇标题为 "An Information Density Analysis" 的论文，核心概念定义不严谨动摇了分析框架。两位 Reviewer 均建议采用独立于 accuracy 的度量（token-level attribution、gradient saliency、互信息）。

---

### Should-Fix（影响评分但不一票否决）

**SF-1** [Consensus: R1-N2 + R2-AGREE] **49% 重复样本系统性收窄 CI**
exception_only 有效独立 N ≈ 607 而非 1,190，Wilson CI 偏窄约 1.4×。Point estimate 不受影响（Appendix O, 0.00pp delta），但 Table 2 中 1–4pp 的 component ablation 差异在校正后可能失去显著性。Bootstrap resampling unit（sample vs. problem level）未明确报告。核心 18+pp 结论稳健，但细粒度比较需 problem-level clustered bootstrap。

**SF-2** [R2-N2 Must-Fix → R1 partial AGREE → Director: Should-Fix] **Verdict prediction 任务动机不足**
Test framework 直接报告 pass/fail，proxy task 定位未验证下游迁移性。R1 指出 ARR guidelines 不要求当前 claims 之外的额外实验，且 proxy task 有 *CL 先例（CRUXEval, NExT）。**Director 判定**：Should-Fix——影响 Excitement 而非 Soundness。Introduction 应更明确连接 proxy task 先例和潜在下游价值。

**SF-3** [Consensus: R1-W1 + R2-partial-REBUT] **Component ablation 跨模型泛化不足**
Table 2 详细消融（含 VOTA_no_ae）仅在 Qwen-7B 上进行。R2 指出 Table 1 已含 ae_only（2 模型）、loop_only（3 模型）跨模型数据，two-tier hierarchy 核心 gap 在 Table 1 跨 4 模型验证。但 VOTA_no_ae 等组件级结论仍限于单模型。至少一个非 Qwen 模型的关键条件复现可显著增强说服力。

**SF-4** [Consensus: R1-W2 + R2-AGREE] **Figure 3 训练动态分析缺乏定量刻画**
仅展示约 150 步（总 444 步的 1/3）；未标明 train/val accuracy；"振荡"仅视觉描述无定量指标（方差、收敛速率）；缺 training loss curve。低成本修复（重绘 + 统计）。

**SF-5** [Consensus: R1-W5 + R2-AGREE] **真实世界泛化性受限**
仅含 HumanEval/MBPP 简单 assert-based 测试，真实世界失败模式（segfault、timeout、复杂 assertion libraries）未覆盖。DebugBench 仍为 synthetic injected bugs。Discussion 应更明确讨论 exception_only 优势对测试结构均匀性的依赖。

**SF-6** [Consensus: R1-W6 + R2-AGREE] **DeepSeek VOTA seed 42 排除合理性不充分**
1/4 模型出现 tokenizer-induced truncation failure 本身是 VOTA 的 limitation（tokenizer sensitivity），不应简单排除为 outlier。应作为 VOTA 的鲁棒性限制讨论，对比 exception_only 紧凑表示天然免疫此问题。

**SF-7** [R1-W3 + R2-partial-AGREE] **标题 "Impair" 因果声明偏强**
控制实验设计提供部分因果证据（same model/hyperparams/data, padding control），但 decomposition 混淆（MF-1）削弱因果链。"Degrade" 或 "Are Associated with Lower Accuracy" 更精确。

**SF-8** [Consensus: R2-W1 + R1-AGREE] **缺失 data pruning 关键文献**
Paul et al. (2021) "Deep Learning on a Data Diet" (NeurIPS) 和 Sorscher et al. (2022) "Beyond Neural Scaling Laws" (NeurIPS Outstanding Paper) 与 "fewer but more informative tokens" 叙事直接相关，应纳入 Section 5。

---

### Minor Issues（不影响接收）

- Bib key `qwen2025coder` 应改为 `qwen2024coder`（year=2024, arXiv 2409.12186）
- TracePile 命名：应明确为数据集名称而非论文名
- Appendix B GPU 型号（RTX PRO 6000 Blackwell）可能缩小匿名范围，建议模糊为 "high-end GPU with 96 GB VRAM"
- Table 1 † single-seed 标注较隐蔽，建议正文首次引用时提及
- Appendix G persistent error analysis（2 个 GeneratorExit 样本）值得正文简要提及
- Orphan bib entry `pornprasit2021jitline` 应清理
- Conclusion 长度：R2 认为过短（~5 行），R1 认为已足够（~10 行）——minor stylistic issue
- Abstract 数据密度：R2 建议减少 50% 数字，R1 认为 data-rich abstract 在 empirical paper 中标准——stylistic preference

---

## Reviewer Consensus [AGREE]

1. Information density 定义循环/不一致——核心概念定义不严谨（R1-W4 = R2-N3）
2. label_only 分解有多重未控制混淆变量且仅 2/4 模型成功（R1-N1 + R2-AGREE）
3. 核心发现新颖性受限——exception events 结构性编码 verdict（R2-N1 + R1-AGREE with nuance）
4. CI 收窄需方法论校正（R1-N2 + R2-AGREE）
5. Figure 3 需定量改进（R1-W2 + R2-AGREE）
6. 真实世界泛化受限于 benchmark 简单性（R1-W5 + R2-AGREE）
7. VOTA seed 42 排除是 VOTA limitation 而非 outlier（R1-W6 + R2-AGREE）
8. 缺失 data pruning 关键文献（R2-W1 + R1-AGREE）

## Reviewer Divergence [REBUT]

1. **Excitement 评分**：R1 = 3.5, R2 = 2.0（1.5 分差距）。R1 认为系统性跨模型分析有 incremental value；R2 认为 near-tautological core finding 和 weak task motivation 显著削弱 excitement。Director: 系统性实验有价值，但分析框架（information density）的循环定义使其无法从 "empirical comparison" 提升为 "analytical contribution"，Excitement ≈ 2.5–3.0。
2. **任务动机严重性**：R2 = Must-Fix, R1 = Should-Fix。Director: Should-Fix——proxy task 有先例，影响 Excitement 非 Soundness。
3. **Conclusion 长度**：R2 = Should-Fix, R1 = REBUT（足够）。Director: minor issue。
4. **Component ablation 范围**：R1 = Should-Fix, R2 = partial REBUT（Table 1 跨模型数据存在）。Director: Table 1 部分覆盖但 VOTA_no_ae 仅单模型，Should-Fix。

---

## Questions to Authors

1. label_only 条件下学习率是否调整过？标准 SFT 对 ~2048 tokens 平均 loss，label_only 仅对 1 token，如果 LR 不变则有效梯度幅度差异约 2000×。
2. Bootstrap resampling（B=10,000）是在 individual sample 级别还是 problem 级别进行的？对含大量重复的 exception_only 条件，sample-level bootstrap CI 受非独立性影响。
3. 能否提供全部 3 epoch、所有 seed 的完整训练曲线（含 training loss 和 validation accuracy）？
4. 能否将 information density 作为独立于 accuracy 的变量计算（如 token-level mutual information with verdict label）？
5. Nomarker 条件下 regex baseline 分数是多少？这是判断 SFT 真实语义增量的关键缺失对比。

---

## Missing References

- Paul et al. (2021) "Deep Learning on a Data Diet: Finding Important Examples Early in Training" (NeurIPS 2021)
- Sorscher et al. (2022) "Beyond Neural Scaling Laws: Beating Power Law Scaling via Data Pruning" (NeurIPS 2022, Outstanding Paper Award)

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 4 info）：
- **[Warning]** Pages 1–2：连续两页纯文本无 display item，第一个视觉锚点（Table 1）在 page 3。建议将 Figure 1（pipeline overview，当前 page 4）提前到 page 2。
- **[Warning]** Pages 6–7：连续两页纯文本（Section 3.5 + Discussion），建议将 Figure 3（Training Dynamics，当前 page 8）提前或增加总结性表格。
- [Info] Figure 1 移至 page 2 可改善审稿人第一印象。
- [Info] 主文 8 页共 6 个 display items，略低于典型密度但内容充实。
- [Info] Table 2 和 Table 3 同页，信息密度高但可读性尚可。
- [Info] Appendix 末页仅 1/3 内容，影响有限。

---

## Overall Assessment

**Overall Score: 3.0 / 5 (Findings)**
**Confidence: 4 / 5**

| 维度 | R1 | R2 | Director 综合 |
|------|----|----|---------------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 2.0 | 2.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.0 | 3.0 |

本文实验方法论在同类工作中属于上乘——4 模型 3 架构家族、multi-seed、comprehensive controls（padding、truncation direction、format marker ablation）。核心发现（exception_only >> full_trace，18+pp gap）跨模型稳健且有工程指导价值。

**评分定为 3.0（Findings）而非 3.5+（Conference）的原因：**

1. **分析框架不可靠**：论文的关键差异化贡献是 "Information Density Analysis"，但该核心概念定义循环（用 accuracy 定义 density），且未作为连续变量正式计算。这使标题中的分析框架更像 post-hoc narrative 而非严格方法论贡献。
2. **Decomposition 方法不稳定**：26%/74% 分解仅在 Qwen 家族成功，2/4 模型 collapse，且存在未控制的混淆变量（有效学习率 ~2000× 差异）。作为论文的核心分析工具，可靠性不足。
3. **新颖性受限**：exception events 结构性编码 verdict 使核心发现接近 tautological；regex baseline 99.33% vs SFT 99.83% 的 0.50pp 差距进一步削弱了 SFT incremental value narrative。
4. **任务动机薄弱**：proxy task 定位有 *CL 先例，但下游迁移性完全未验证。

**如果 revision 能**：(a) 选择独立于 accuracy 的 information density 度量并量化，(b) 澄清 label_only 的 LR 设置并将分解降级为 preliminary analysis with explicit confounders，(c) 提供 problem-level clustered bootstrap CI，(d) 重新定位 contribution 为 systematic quantification 而非 fundamental insight——评分可提升至 **3.5 (Borderline Conference)**。

---

## Detailed Comments

### Section 1 (Introduction)
- "Less Is More" framing 应降调：核心发现更接近 "signal-to-noise ratio determines SFT performance" 而非 "counter-intuitive finding"
- Proxy task motivation 需强化：连接 CRUXEval/NExT 先例，明确 downstream applications 为 future directions 而非 current claims

### Section 2 (Method)
- Information density 工作定义应在 Section 2 引入，采用独立于 accuracy 的度量
- Section 2.1 "binary classification task" 表述应注意与标准分类区分——SFT loss 在序列上计算而非仅分类 head

### Section 3 (Experiments)
- Table 2 component ablation 标注为 Qwen-7B-only
- Table 1/2 中 CI 应补充 problem-level clustered bootstrap 结果
- Bootstrap resampling unit 应明确报告
- Section 3.4 decomposition 应明确报告 LR 设置、讨论三重混淆变量、Abstract 限定为 "on the Qwen family"

### Section 4 (Discussion)
- Figure 3 展示完整 444 步 + loss curve + 定量指标
- VOTA seed 42 排除应作为 VOTA tokenizer sensitivity limitation 讨论
- 真实世界泛化限制（测试结构多样性依赖）应更明确讨论

### Section 5 (Related Work)
- 补充 Paul et al. (2021) 和 Sorscher et al. (2022) data pruning 文献

### Section 6 (Conclusion)
- 当前长度可接受，但可考虑补充 broader implications 和 future directions（minor）

### Format/Bib
- `qwen2025coder` → `qwen2024coder`
- 清理 orphan bib `pornprasit2021jitline`
- Appendix B GPU 型号模糊化
- TracePile 命名明确为数据集名