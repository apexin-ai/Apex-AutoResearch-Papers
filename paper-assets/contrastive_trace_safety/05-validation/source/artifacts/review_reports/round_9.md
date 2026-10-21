---
round: 9
overall_score: 3.0 - Findings
timestamp: 2026-05-18T11:19:03.276782+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 10 审稿报告 — contrastive_trace_safety

**论文**: *Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models*
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewer 编排**: R1 (方法严谨性+统计有效性) + R2 (新颖性+Framing+写作)
**轮次**: Round 10（继续审稿，追踪 R9 open issues）

---

## Summary

本文对比 hidden-state (HS) probes 和 text-based monitors 在检测推理模型 safety commitment point 上的表现，使用 4 个推理模型（2 架构 × 2 规模）和 HarmThoughts 数据集。核心发现是方法论性的：layer selection metric 中的 crossing rate 成分在 32B 模型上系统性地选择浅层，从而掩盖 HS 优势。使用 threshold-dependent metrics 选择深层后，所有 4 个模型在 384d text baseline 下均显示显著 HS 优势（Holm-Bonferroni corrected）。但该优势是 encoder-conditional 的：对 1024d BGE-large encoder，仅 1/4 模型保持显著性。

---

## Strengths

1. **Layer selection sensitivity 具有方法论普适价值**: 证明单一 layer selection metric 可以逆转 probing study 的核心结论，五指标消融设计严谨，representation compression 机制解释有 cosine distance 数据支撑（Appendix B）。这一发现超越本文的安全检测场景，对整个 probing 文献有 cautionary 意义。[R1 ✓, R2 ✓]

2. **统计报告诚实度远超同类论文**: Holm-Bonferroni step-down correction + exact sign-flip permutation tests 双重验证；multi-seed stability analysis；position-residualized probe；encoder robustness (384d vs 1024d)；threshold sensitivity sweep。主动披露不利结果（R1-8B FPR 边缘通过、QwQ position mediation、encoder-conditional narrowing、R1-32B 25% coverage）。Bug disclosure（Appendix L）体现科学诚信。[R1 ✓, R2 ✓]

3. **全面的 negative results 系统评估**: Section 4.6 评估 7 种 alternative methods，每种有 failure analysis。RepE 的 metric-dependent discrepancy 分析（bal_acc competitive 但 precision 差距大）对领域有建设性价值。[R1 ✓, R2 ✓]

4. **两级 framing 有效区分证据强度**: Abstract 和 Introduction 明确区分 7-8B（robust across 5 seeds）和 32B（sample-limited, pilot-scale, model-specific caveats）。QwQ-32B position mediation 在 Contribution 2 中充分披露。[R1 ✓, R2 ✓]

5. **引用覆盖完整**: 54 篇引用，涵盖直接相关方法、baseline、benchmark、理论基础，2025-2026 最新工作覆盖充分，0 orphan entries。[R2 ✓]

---

## Weaknesses

### Must-Fix（影响 camera-ready 质量，应在修改中解决）

**W1** [R1 critical → Director 判定 warning] **Table 3/4 HB 列 "3/3" 与正文 "effective DoF=4" 矛盾**
- 位置：experiments.tex Table 3 L49-55, Table 4 L82-83
- 正文 Section 3.3 明确论证 "effective number of independent comparisons is four (one per model)"，Appendix C 报告了 4-test model-level HB。但 Table 3/4 的 HB 列逐行显示 "3/3"，给读者 12 项独立验证的视觉印象。
- Director 判定：从 R1 的 critical 降为 **warning**。核心结论不受影响（4-test HB 也全部通过），但表格呈现与正文不一致属于修辞问题，camera-ready 必须修复。
- 修复方式：HB 列改为 "✓" (per-model pass)，caption 注明 "All four model-level tests pass HB correction (α=0.05)"。

**W2** [R1 critical → Director 判定 warning] **Table 3 缺 ±std，R1-32B 高方差不可见**
- 位置：experiments.tex Table 3
- R1-32B precision std=0.128（Appendix K），seed 0 precision 仅 0.441。将 ±std 仅放附录降低了审稿人评估稳健性的能力。
- Director 判定：从 critical 降为 **warning**。数据在 Appendix K 完整存在，Table 3 caption 已指向附录。但主表应至少标注 32B 方差信息。
- 修复方式：Table 3 脚注添加 "R1-32B: precision std=0.128, FPR std=0.145 across 5 seeds (Appendix K)"。

**W3** [R1 major] **Limitations 中 "n=4-9 at 32B" 含义不清**
- 位置：limitations.tex L10
- 60/20/20 split 下 32B 验证集 = 19-20 traces。"n=4-9" 从何而来？R9 已标记，R10 文字完全未改。
- 修复方式：明确标注含义，如 "n=4-9 per-class validation traces at 32B scale"。

### Should-Fix（影响评分但不 blocking）

**W4** [R1 warning, R2 implicit agree] **QwQ-32B 仍被计入 "all four significant" 但 advantage 主要 position-mediated**
- 位置：Section 4.2 L37, Conclusion L3-4
- HS vs text 统计检验确实通过，但 Section 4.5 自行证明 advantage 主要由位置编码驱动（residualized drop 18.3pp, HS vs position p=0.133/0.279）。建议分层措辞："three models show robust HS advantage; QwQ-32B passes HB correction but the advantage is predominantly position-mediated"。

**W5** [R2 warning] **Abstract 中 384d vs 1024d 叙事权重不平衡**
- 位置：abstract.tex paragraph 2
- +15.4 to +32.5pp (384d) 仍是 headline 数字（~35 words），BGE-large 仅 ~20 words。Encoder-conditional 是核心发现之一，两者篇幅应更接近。

**W6** [R2 warning] **正文仅 2 figures（layer heatmap + forest plot）**
- 同类 EMNLP long paper 通常 3-5 个。缺少 temporal context 效果可视化或 commitment trace 示例图。建议将附录 temporal improvement figure 移入正文 Section 4.4。

**W7** [R2 warning] **Related Work "Safety in Reasoning Models" 段引用密度过高**
- related_work.tex paragraph 1, ~250 words / 16 引用，后半段连续 6 个 \citet 开头有堆砌感。建议按子主题分组（attack characterization / detection / mitigation）。

**W8** [R1 warning] **附录 K=5 ablation 仍用 "Pareto-optimal"，与主文 "empirically selected" 不一致**
- 位置：appendix.tex L452

**W9** [R1 warning] **OT-7B GRU split protocol 未标注**
- 位置：appendix.tex L346-347

### Minor Issues（不影响接收）

- **M1**: Related Work 3 处 ", complementing..." -ing 结尾（AI 写作残留）
- **M2**: Abstract "crossing rate" 未定义（可替换为 "frequency of threshold crossings"）
- **M3**: OpenThinker-7B vs OpenThoughts 名称关系未澄清
- **M4**: "only 1/4 models retains" → "retain"（语法）
- **M5**: Table 3 caption "Mean values from canonical split" → "Values from canonical split"

---

## Reviewer Consensus [AGREE]

**完全共识项**:
- Overall Assessment: 3.0 (Findings) [R1 ✓, R2 ✓]
- Soundness: 3.5/5 [R1 ✓, R2 ✓]
- Novelty 定位: Findings（layer selection sensitivity 有价值但无新方法/数据集）[R1 ✓, R2 ✓]
- Layer selection sensitivity 是核心贡献且有普适价值 [R1 ✓, R2 ✓]
- Encoder-conditional finding 削弱 headline claim 但增加了诚实度 [R1 ✓, R2 ✓]
- Table 3 "3/3" 呈现需修复 [R1 ✓, R2 未单独提出但不反对]
- 统计报告诚实度高于同类论文 [R1 ✓, R2 ✓]

## Reviewer Divergence [minor]

| 问题 | R1 | R2 | Director 判定 |
|------|------|------|------|
| Excitement | 3.0/5 | 2.5/5 | 2.75（取均值，差异不影响结论）|
| Table 3 ±std severity | critical | 未提出 | warning（数据在附录完整，主表脚注即可） |
| Reproducibility | 3.5/5 | 4.0/5 | 3.75（OT-7B GRU split 未标注轻微扣分） |

无重大分歧。

---

## Questions（合并两位 Reviewer，去重后 8 条）

1. "n=4-9 at 32B" 具体指什么？[R1 Q1]
2. W 选择在不同 validation fold 下是否一致？尤其 R1-32B W=1。[R1 Q2]
3. R1-32B seed 0 FPR outlier (0.483) 的具体原因？[R1 Q3]
4. Position-residualized probe 的 residualization 是否损失了非位置信号（position 与 safety features 不正交时）？[R1 Q4]
5. R1-32B 25% coverage 的 5 条 traces 是否有可识别共性？[R1 Q5]
6. 更强 encoder（E5-large-v2, GTE-large）是否可能完全消除 HS advantage？[R2 Q1]
7. 39-52% FPR 的 false positive pattern 是什么？是否与 safe traces 中的 commitment-like transitions（如 refusal decision）相关？[R2 Q2]
8. 7-8B 模型上做 position-residualized analysis 的结果如何？如果也存在 position mediation，则 "genuine safety signal" claim 需重新评估。[R2 Q3]

---

## Missing References

无遗漏。54 篇引用覆盖完整。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Overall Assessment

**评分: 3.0 (Findings)**

两位 Reviewer 独立给出相同评分，交叉分享后无分歧。

**EMNLP 2026 评分对照**:
- 3 = Findings（可被 Findings 接收）

**置信度**: 4/5（两位 Reviewer 均认真审读全文含附录，probing/safety 方向熟悉）

**推荐**: 以 Findings 接收，条件是 camera-ready 阶段修复 W1-W3（Table 3/4 HB 呈现、主表 ±std 脚注、"n=4-9" 澄清）。W4-W9 的修复会进一步提升论文质量但非 blocking。

**理由**:
- 核心贡献（layer selection sensitivity）扎实且有普适价值
- 统计方法论严谨，诚实度高，negative results 详尽
- 但缺乏方法创新（无新方法/模型/数据集），excitement 不足以支撑 Main Conference
- Encoder-conditional finding（1/4 HB vs 1024d）削弱了 HS advantage claim 的绝对性
- 32B 结果为 pilot-scale（n=19-20），QwQ position mediation 进一步限制了 "all four models" 叙事的说服力
- 39-52% FPR 明确定位为 characterization 而非 production detector，scope 合理

---

## Detailed Comments（逐节）

### Abstract
- 结构改善（~168 words, story format）✓
- "retains" → "retain" 语法修正
- 384d/1024d 叙事权重可更平衡
- "crossing rate" 首次出现应定义

### Introduction
- Characterization scope 明确（末尾 FPR + oracle gap）✓
- 两级 framing（7-8B robust vs 32B sample-limited）✓
- Contribution 2 "Encoder-conditional directional advantage" 措辞准确 ✓
- QwQ position mediation 充分披露 ✓
- 建议：核心 claim 中 QwQ 降级为 boundary case

### Related Work
- 54 引用，覆盖完整 ✓
- 第一段密度过高（16 引用/250 words），后半段连续 \citet 堆砌
- 3 处 ", complementing..." -ing 结尾

### Method
- Layer selection sensitivity 论证清晰 ✓
- "effective number of independent comparisons is four" 解释正确 ✓
- K=5 "empirically selected as a middle-ground tradeoff" ✓
- "n=4-9 at 32B" 需澄清

### Experiments
- Table 3 "3/3" 需改为 "✓"
- Table 3 缺 ±std（至少脚注标注 32B 方差）
- QwQ-32B Section 4.5 position analysis 详尽 ✓
- Negative results Section 4.6 措辞合理 ✓

### Discussion
- 不再逐句复述数字，增加新信息（AUROC 层选择、control task selectivity）✓
- "Design implications" 段 FPR 三重复述轻微

### Conclusion
- 精简为 3 句 + future work ✓

### Limitations
- 量化累积 DoF (64×7×5=2240) ✓
- Bootstrap CI coverage caveat ✓
- "n=4-9" 需澄清

### Appendix
- K=5 "Pareto-optimal" 需统一为 "empirically selected"
- OT-7B GRU split 需标注
- Exact sign-flip permutation test 术语正确 ✓
- Bug disclosure 透明 ✓

---

## R9→R10 改善总结

**已解决（本轮确认 resolved）**: C6(引用完整性), R2-W9(Abstract堆砌), R2-W11(Discussion重复), R5-N1(维度对等), R5-W2(negative results framing), R7-W3(monitoring framing), R8-W1(QwQ p-value), R9-N1(R1-8B FPR per-seed), R9-W1(permutation test术语), R9-W2(orphan bib), R9-W3(C-insensitivity), R6-W4(bootstrap有效性)

**已改善但残留问题**: R3-W3/R5-N2(指标膨胀→Table 3/4未改), R5-N3(QwQ position→仍在核心claim中), R5-W1/R7-W2(32B功效→Table缺±std), R7-W1(过拟合→n=4-9未澄清), R2-W14(encoder-conditional→叙事权重), R7-N1(K=5→附录措辞)

**未改善**: R8-M1(OpenThoughts名称), R7-W5(figure数量)

**新发现**: R10-W1(Related Work堆砌), R10-M1(语法微瑕), R10-M2(Table caption措辞)