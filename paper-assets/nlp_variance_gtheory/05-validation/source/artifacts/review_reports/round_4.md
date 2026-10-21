---
round: 4
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T12:00:02.794160+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---


# 审稿报告：Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis

**Venue**: EMNLP 2026 (ARR)
**审稿轮次**: Round 5 (fresh review)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）。本轮为 EMNLP 一般会议标准编排 2 人，R3 为历史轮次 Reviewer，本轮未分配任务。
**交叉回应**: R1、R2 完成（1 轮，共识达成）

---

## Summary

论文将 Generalizability theory (G-theory) 应用于 LLM evaluation variance decomposition，在 8 个 open-weight 7-9B 模型 × 5 benchmarks × 最多 7 facets 的全交叉设计上（约 2.3M 记录），分解评估方差来源。核心发现：(1) multi-facet 设计比 single-condition 设计需要 10× 更少的 items 达到 G≥0.80（55 vs 552）；(2) item-related variance 在 MC benchmarks 上集中（68-72%）而在 FF benchmarks 上分散（31-41%）；(3) BF16/FP16 在 binary scoring 下功能等价；(4) 释放 G-theory pipeline 和 D-study budget calculator。

---

## Strengths

1. **实验规模与设计系统性**：7 facets × 5 benchmarks × 8 models 的全交叉设计在同类工作中最大，factorial crossing 能估计 interaction terms——这是理解方差结构的关键优势，相对于 Messing (2026) 的 single-benchmark 和 Madaan et al. (2024) 的 per-factor 方法有实质性推进。

2. **Robustness 检查达到顶会水准**：8 项独立检查（GLMM complement ρ=1.0、accuracy-range stability、REML <0.5pp、CI method comparison、facet specification sensitivity、LOMO |ΔG|<0.02、null calibration ratio=1.0008、reduced crossing ΔG=0.0008）构成系统性证据链。特别是 null calibration 清晰排除了 Bernoulli p(1-p) artifact。

3. **统计报告诚实透明**：format-associated claim 在 §4.3 中明确标注 p=0.10 permutation floor 和 benchmark-level CI spanning zero，precision interchangeability 标注 metric-conditionality。在 LLM evaluation 领域难得的不 overclaim。

4. **实践工具价值高**：D-study budget table（Table 4 + Appendix B Table 6）和 intermediate design gradient（Appendix C Table 7）提供直接可操作的指导。"3 prompts × 3 seeds" 作为 minimal sufficient upgrade（G: 0.592→0.766）的推荐尤其实用。IRT 互补性展示（Zhou et al. 116 items: G 0.457→0.895）优雅地证明了 item selection 和 condition optimization 的正交性。

5. **可复现性好**：设计矩阵、facet 定义、prompt 模板（Appendix E）、模型列表（Appendix E Table 8）描述清晰，vLLM 版本和 GPU 型号均已说明。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [critical, R1+R2 共识] **Format-associated claim 呈现层级与统计功效不匹配**
- Abstract 前三句（"On multiple-choice benchmarks, item selection drives 34–38%..."）无任何 hedging，Contribution #2 与 #1 并列为同等级贡献。但 benchmark-level 证据仅有 n=5 benchmarks，exhaustive permutation p=0.10（理论分辨率下限，α=0.05 下不可能拒绝 H0），benchmark-level CI 跨零 [-1.7, 5.1]（df=3）。§4.3 正文中的 "descriptive observation" 限定未传递到 Abstract 和 Contributions。item-level d=1.73 [1.72, 1.83] 虽大但与 benchmark-level 推断在不同分析层级，不能弥补功效缺口。§4.3 花大量篇幅反驳 "tautology" 反对意见，defend 力度与 "descriptive observation" 定位不匹配。
- **建议**：(a) Abstract 和 Contributions 中加入一致的 hedging/限定语；(b) 将 Contribution #2 降级为 observation 而非与 #1 并列的 contribution；(c) 或补充 2-3 个 benchmark 提升 permutation 分辨率至 p<0.05。

**MF-2** [critical, R1+R2 共识] **D-study budget 推荐对 4/5 benchmarks 缺乏 cross-sample 验证**
- 论文第一大贡献（10× budget ratio）在 MMLU 上有三组独立 200-item 样本的交叉验证（CV=3.1%），但 ARC、HellaSwag、GSM8K、MATH 的方差成分均来自单一 200-item 样本。Table 6（Appendix B）的 D-study projections 完全依赖该单一样本。FF benchmarks 的 residual 高达 40-44%（Table 3），方差成分可能对 item 抽样更敏感，bootstrap CI 可能低估真实不确定性。
- **建议**：至少对 1 个 MC + 1 个 FF benchmark 追加 2-3 组独立 item 样本的方差分解并报告 CV；或明确展示 n_{G≥0.80} 的 bootstrap CI（已有 G 值 CI 但未展示 budget point estimate 的 variability）。

**MF-3** [critical/high-warning, R1 critical + R2 agree with nuance] **Binary scoring 对所有 findings 的系统性 measurement resolution confound 未统一讨论**
- Binary 0/1 是最粗粒度评分方式。在此粒度下：(a) 任何影响 logit 但不足以翻转 binary decision 的方差源表现为 negligible——precision <0.1% interaction 可能反映 binary scoring 测量灵敏度不足而非真正等价性；(b) 极端难度 items 在所有 conditions 下稳定产出 1/0，机械放大 item_id 份额。text-exact-match G=0.007 vs G=0.936 是论文自身最佳证据：评分粒度根本性重塑方差结构。论文有部分回应（§4.3 HellaSwag 例外 + ρ=0.806），但 metric-conditionality 讨论散布各节缺乏统一框架。"functionally interchangeable" 未附 "under binary scoring" 限定。
- **建议**：在 §3.5 或 §4.1 增加统一的 binary scoring measurement resolution caveat，明确所有后续 findings 均为 binary-scoring-conditional。

### Should-Fix（影响评分但不一票否决）

**SF-1** [warning, R1+R2 共识] **Quasi-random model facet exchangeability 论证不完整**
- LOMO 和 4-model subset 验证证明内部稳定性（item_id: 36-41%, G: 0.877-0.889），但不能证明对 target universe 的代表性。8 个模型共享 2024-2025 训练范式，可能存在 temporal correlation 违反 exchangeability。

**SF-2** [warning, R1+R2 共识] **Reduced crossing validation 仅 MMLU，未覆盖 FF benchmarks**
- exp-002 的 design reduction（3 precision → 1, 3 temp → 2）在 MMLU 上验证（ΔG=0.0008），但 FF benchmarks 方差结构不同，不能直接外推。

**SF-3** [warning, R1+R2 共识] **Scale validation 语言过强**
- "item dominance is scale-robust" 仅基于 Qwen2.5 3B (75.3%) 和 7B (73.4%)——单一模型家族内 2 个数据点。建议改为 "scale-consistent within the Qwen2.5 3B-7B range"。

**SF-4** [warning, R1+R2 共识] **Few-shot example selection 未作为 facet 交叉**
- 论文变化了 few-shot examples 的排列顺序（4 orderings）但未变化哪些 examples 被选中。Example identity 是已知方差源，遗漏可能导致 underestimation of prompt-related variance。

**SF-5** [warning, R1+R2 共识] **DeepSeek MATH 排除原因未说明**
- "incomplete inference data"（37,400/57,600 expected records, 约 35% 缺失）未区分 OOM/timeout（MNAR, 偏向困难题目）vs vLLM 兼容性问题（MCAR）。LOMO 在完整 4-benchmark 数据上执行，不能直接推广到已有缺失的 MATH。

**SF-6** [warning, R2 Must-Fix → R1 rebut → 圆桌降级] **Conclusion 过于简短**
- §5 仅一段约 6 行，缺少 practical implications。R1 认为 8 页限制下简短 Conclusion 常见。圆桌共识：适度扩展 2-3 句 practical takeaway 即可。

**SF-7** [warning, R1+R2] **遗漏相关工作**
- R2 提出：Benchmark Health Index (2602.11674)、"Measuring what Matters" (2511.04703)、"Establishing Construct Validity...Nomological Networks" (2603.15121)
- R1 提出：Holland & Wainer (1993) DIF 经典参考、Clauser & Mazor (1998) DIF 操作化、Webb, Shavelson & Haertel (2006) G-theory random vs fixed facet
- Holland & Wainer (1993) 优先级最高。其余需验证真实性后酌情添加。

### Minor（不影响接收）

- Table 3 中 "prompt" 列对 MC 和 FF 含义不同（prompt×item vs prompt main effect），表注已说明但易被忽略
- Abstract "approximately 2.3 million" 仅指 exp-002，exp-001+002 总计约 2.8M，应明确
- Table 缩写不统一（"Hella." vs "HellaSwag"）
- references.bib 中 varannot2025gtheory 作者为 "Anonymous"，blackwell2024towards 缺 URL
- 符号在 Introduction 中使用但在 §3.1 才定义
- Figure 2 对色弱读者不友好
- §3.2-3.6 是实验设计细节，可考虑将 §3 重命名为 "Method and Experimental Design"
- Probit simulation ρ=0.732 作为第一个报告的验证指标给读者负面第一印象，建议重新组织验证顺序（先 GLMM ρ=1.0 和 REML <0.5pp）

---

## Reviewer Consensus [AGREE]

1. **Format-associated claim 需要更一致的呈现层级**（MF-1）：两位 Reviewer 均独立提出，交叉回应中完全一致。最高优先级。
2. **D-study budget 跨样本验证不足**（MF-2）：两位 Reviewer 均同意。
3. **Scale validation 语言过强**（SF-3）：两位 Reviewer 均独立提出，完全一致。
4. **DeepSeek 排除需补充说明**（SF-5）：两位 Reviewer 均同意。
5. **论文执行质量高于平均**：两位 Reviewer 均肯定实验规模、robustness 检查和统计诚实性。

## Reviewer Divergence [REBUT]

1. **Conclusion 长度**：R2 Must-Fix → R1 rebut → 圆桌降为 Should-Fix。
2. **D-study budget 贡献独立性**：R2 认为直接推导 → R1 反驳有三层独立价值 → 圆桌倾向 R1。
3. **Abstract 信息密度**：R2 认为过高 → R1 认为符合方法论文 norm → 圆桌倾向 R1。
4. **Binary scoring confound severity**：R1 critical → R2 agree with nuance (high-warning) → 圆桌保留 critical。

---

## Questions for Authors

1. DeepSeek 在 MATH 上 inference 不完整的具体原因？缺失数据是 MNAR 还是 MCAR？
2. 是否有计划为 ARC/GSM8K 追加独立 item 样本的 cross-sample validation？
3. "functionally interchangeable"（precision）是否应限定为 "under binary correctness scoring"？
4. enforce_eager=True 对实际部署中方差结构的影响是否已评估？
5. 是否考虑过 partial-credit scoring 对 FF benchmarks 方差结构的影响？
6. 8 个模型的 pairwise agreement（如 Cohen's κ）分布如何？是否支持 exchangeability？

---

## Missing References

**R1 提出（心理测量学经典）**：
- Holland, P.W. & Wainer, H. (1993). *Differential Item Functioning*. Lawrence Erlbaum. — DIF 奠基之作，优先级最高
- Clauser, B.E. & Mazor, K.M. (1998). DIF 操作化教育测量背景
- Webb, N.M., Shavelson, R.J., & Haertel, E.H. (2006). G-theory random vs fixed facet 分类讨论

**R2 提出（NLP 相关）**：
- Benchmark Health Index (arXiv:2602.11674) — 需验证真实性
- "Measuring what Matters" (arXiv:2511.04703) — 需验证真实性
- "Establishing Construct Validity...Nomological Networks" (arXiv:2603.15121) — 需验证真实性

---

## External Review (Stanford Agentic Reviewer)

未启用。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 3 info）：

**Warning**:
1. **Pages 1-4 无 figure/table**：连续 4 页纯文字（Abstract → Introduction → Related Work → Method 前半），display items 全部集中在 pages 5-8。建议将一个核心结果预览图前移至 Introduction（page 1-2）。
2. **Figure 1 展示设计结构而非核心发现**：论文第一个 display item 是实验设计 stacked bar，审稿人的锚定效应发生在"方法论设计"而非"关键结果"。建议让第一个 figure 传达核心 message。

**Info**:
3. Figure 2 在右栏单栏宽度显示，bar segment 标签偏小，可考虑 figure* 全宽。
4. Table 3 "prompt" 行 bold 语义需在 caption 中更明确说明。
5. Display items 密度 pages 5-8 优秀（7 items / 4 pages）但与前 4 页空白形成强烈反差。

---

## Overall Assessment

**评分：3.5 — Borderline Conference**
**置信度：4/5**（两位 Reviewer 评分一致，交叉回应后共识稳固）

**EMNLP 2026 评分标准对照**：3.5 = Borderline Conference（介于可被 Findings 接收和可被主会议接收之间）

**理由**：论文将 G-theory 系统应用于 LLM evaluation variance decomposition，实验规模在同类工作中最大（2.3M 记录、8 模型、5 benchmarks、7 facets），robustness 检查全面（8 项），统计报告诚实透明。D-study reproducibility budget（10× 效率增益）有切实的实践价值，IRT 互补性展示优雅。

但三个方法学问题共同削弱了 generalizability claim 的说服力：
1. **Format-associated pattern**（Contribution #2）以 n=5、p=0.10 的证据强度在 Abstract/Contributions 中被突出呈现为核心贡献，与其统计基础能承受的范围不匹配
2. **D-study budget 推荐**对 4/5 benchmarks 缺乏 cross-sample 验证，最核心的实践贡献缺少 out-of-sample 支撑
3. **Binary scoring confound** 对所有 findings 的系统性影响未被统一讨论

**修改路径**：解决 MF-1（调整 claim 呈现层级）和 MF-2（补充跨样本验证或展示 budget CI）后，论文可达 **4.0 Conference** 水平。MF-3 通过增加统一 caveat 段落即可解决。当前版本方法学 execution 扎实，但 evidence-to-claim 的匹配在最广泛的主张上存在缺口。

---

## Detailed Comments

### Abstract
- 前三句以事实性口吻陈述 format-associated 数字（"item selection drives 34-38%"），与 §4.3 的 "descriptive observation" 定位不一致。需加 hedging。
- "approximately 2.3 million" 仅指 exp-002，总计约 2.8M。
- 信息密度高但在方法论文 norm 内可接受（圆桌分歧后倾向可接受）。

### §1 Introduction
- Gap statement ("three gaps remain") 论证逻辑严密。
- Contribution #2 与 #1 并列但证据强度不对等。

### §2 Related Work
- 覆盖了 variance decomposition、IRT、psychometrics、infrastructure variance 四大方向核心文献。
- Positioning paragraph 区分度清晰（vs Messing, vs IRT, vs isolated-factor）。
- 可补充 DIF 教育测量经典文献和 2025-2026 新兴 benchmark 可靠性工作。

### §3 Method
- G-theory 方法学正确，Henderson Method I 适用于 balanced design。
- DIF 操作化（model×item interaction）的 LLM vs 教育测量语义差异讨论（"dual interpretation"）得当。
- item-related variance bundling（σ²_p + σ²_pM）有 psychometric justification（Brennan Ch.4），且全文报告 unbundled components 确保透明。
- §3.2-3.6 更像实验设计细节，可考虑将 §3 重命名为 "Method and Experimental Design"。

### §4 Experiments
- §4.1 Single-model baseline 建立了好的基线，text-exact-match 对比有力。
- §4.2 Cross-model 分析揭示了 model×item interaction 的重要性。
- §4.3 Format-associated 分析在正文中诚实报告统计局限性，但 "tautology" 辩护力度与 "descriptive" 定位不匹配。
- §4.5 D-study budgets 是最强的实践贡献，intermediate design gradient 尤其实用。
- §4.6 Scale validation 结果 consistent 但语言需降级。
- §4.7 Robustness checks 系统全面。

### §5 Conclusion
- 简短但核心发现已覆盖。可适度扩展 practical implications。

### §6 Limitations
- 四个 scope constraints 覆盖合理。
- 建议补充 few-shot example selection 和 binary scoring resolution 的讨论。

### Appendix
- 8 项 robustness analyses 组织清晰。
- Cross-model D-study projections（Table 6）、intermediate designs（Table 7）、difficulty scatter（Figure 4）有独立参考价值。
- Model 和 prompt 细节（Appendix E）确保可复现。
