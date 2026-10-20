---
round: 27
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T11:45:08.977265+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 27 (Fresh Review)

**论文**: "The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Structured Generation"
**Venue**: EMNLP 2026 Main Conference (Long Paper, via ARR)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验充分性; R2: 新颖性+完整性+写作质量）
**交叉分享**: 完成（R1→R2, R2→R1，逐条[AGREE]/[REBUT]回应）

---

## Summary

本文调查 self-consistency (SC) 在结构化信息抽取（主要是 NER）中为何失败。核心发现是 "correlation-selection gap"：质量估计信号与 oracle F1 相关（ρ up to 0.45, AUROC up to 0.82），但无法选出比 greedy decoding 更好的样本。论文提出四阶段诊断级联（QE → degeneracy → agreement fidelity → LP compression）来定位失败机制，测试了 7 种 entity-level 方法（ESJ, MRSC, LSC, Het-T, ASB, SCD, supervised verifier），均未能弥合 gap。处方性结果包括 LP-weighted entity construction (+1.02–1.40pp on Few-NERD)、cross-model ensemble (+0.42pp) 和 regime-specific LP selection (+1.39pp on Few-NERD)。实验跨 4 个 NER 数据集、2 个模型族（Qwen/LLaMA）、4B–72B 规模和 GPT-5.5。

---

## Strengths

**S1 [Consensus]** 四阶段诊断级联是论文最有价值的贡献。从质量估计到 degeneracy 到 agreement fidelity 到 LP compression 的递进式诊断结构，每个阶段都有对应的 metric 和实验验证。

**S2 [Consensus]** NER 范围内的实验覆盖度堪称典范。4 个数据集（SciERC, Few-NERD, CoNLL-2003, WNUT-17）覆盖不同难度梯度；2 个模型族；4B–72B 规模范围；5 种信号；60+ 张表格。

**S3 [Consensus]** 统计方法论严谨性远超同类论文。全局 Holm-Bonferroni 校正（k=57）、paired bootstrap tests（B=10,000）、bootstrap 95% CI、multi-seed 设计（3 seeds on key datasets）、post-hoc power analysis。

**S4 [R1]** MBR 等价性证明（Proposition 1）将 entity construction 与 MBR decoding 联系，提供了概率论基础。

**S5 [R1]** 三个独立诊断探针（ESJ, MRSC, LSC）从不同角度收敛到相同结论——entity-level self-verification 失败——构成 converging evidence。

**S6 [R2]** ~35 页附录提供极高可追溯性。Table 62 与先前工作的差异化矩阵清晰。

**S7 [Consensus]** 引用验证通过：51 bib entries, 49 cited, 2 orphan, 0 虚假引用。

---

## Weaknesses

### Must-Fix（3 个 critical，两位 Reviewer 完全共识）

**C1 [CONSENSUS CRITICAL] 标题 "Structured Generation" 与实验范围严重不匹配**
- R1-N1 + R2-N1 独立提出，交叉后完全一致
- NER 有 4 数据集 × 2 模型族 × 60+ 表格。RE 仅 SciERC 1 个数据集（Appendix o），且 55.5% 实例因 entity span error 获 F1=0。SQL 仅 GPT-5.5 on Spider (n=196) 一句话描述，无详细表格。
- RE 中 FEATURE-OF ρ≈0 vs HYPONYM-OF ρ=0.646，信号质量高度关系类型依赖
- 建议: 标题和 Abstract 收窄为 NER-specific（如 "Named Entity Recognition" 或 "Structured Information Extraction"），RE/SQL 降为 "preliminary observations"

**C2 [CONSENSUS CRITICAL] 因果语言与相关性证据不匹配**
- R1-N2 提出，R2 AGREE with nuance
- Figure 1 caption 正确标注 "diagnostic sequence, not causal chain"，但 Section 9 用 "Degeneracy **governs** the selection gap"，Abstract 用 "**explaining** where and why"，Introduction 用 "fills this gap"
- 论文实际做的是相关性诊断（Spearman ρ, subgroup 对比, AUROC），无干预实验验证因果方向
- R2 认为论文有准因果证据缓解（MBR 理论机制、非退化子集条件分析、温度扫描），但全文语言仍需统一
- 建议: 全文替换因果动词为相关性语言；Discussion 加段讨论因果推断局限

**C3 [CONSENSUS CRITICAL] Holm-Bonferroni k=19 (Abstract) vs Table 13 实际 21 行——影响核心统计声明可复现性**
- R1-N3 提出，R2 AGREE
- Abstract 声称 "selection family k=19"，但 Table 13 的 selection family 共 21 项测试，差异 2 项未解释
- 直接影响 p_adj 计算和读者独立验证
- 建议: 核实 k 值来源，修正 Abstract，在 Appendix f 提供完整 Holm correction trace

### Should-Fix（7 个 warning）

**W1 [Consensus]** Degeneracy bound 极松且被过度呈现。Table 30 显示 bound 仅捕获实际增益 4.7–12.1%，且无法预测负增益方向。Introduction 将其作为主要贡献之一呈现，但 bound 的实际预测能力有限。建议: 在主文讨论 tightness。

**W2 [Consensus]** RE 分析被 entity span error 严重混淆。RE 本质上测量 NER→RE 错误传播而非 RE 本身的 SC 失败。Table 3 RE 列与 NER 并列但未充分标注混淆因素。建议: Section 7.6 首段明确声明。

**W3 [R1, R2 AGREE]** k=57 全局 Holm + RE/小配置样本量导致统计功效不足。核心结论 "no signal improves selection" 在 RE 和小配置上可能反映 insufficient power 而非 true null。建议: Conclusion 加 hedge。

**W4 [R1, R2 partially AGREE]** 7 种方法分类边界模糊。Abstract "7 methods" 含 diagnostic probes (ESJ/MRSC/LSC) 和 selection methods (DALS/SCD) 但未区分。Het-T 在 Table 2 无对应行。Table 2 列 9 categories 与 Abstract 7 methods 不对齐。

**W5 [R2→R1 降级]** Prescriptive gains 边际化 (+1.0–1.4pp at 8× cost)。R2 列为 critical，R1 降为 should-fix——论文主贡献是诊断框架而非 prescriptive methods，negative results 有独立价值。交叉后共识: 保持 should-fix，建议在 Section 10 或 Discussion 直接 address cost-effectiveness。

**W6 [R1, partially]** Entity-wise independence 假设（Proposition 1）未经验验证。相邻 entity 预测常相关，可能解释 bound 松散度。

**W7 [Consensus]** 与 Yun et al. (2025) "diversity collapse" 差异化需强化。§8/§9 需 3–4 句明确区分。

### Minor（8 个 info）

- M1: 2 个 orphan bib entries（holm1979simple 应补 \cite，xia2025survey 应删除）
- M2: Figure 2 caption "oracle gap" 未自含定义
- M3: "VotConsLogProb" 在 Figure 6 突然出现未正式定义
- M4: Table 61 (cost-benefit) 在 Appendix p45 但主文未引用
- M5: Abstract "ρ up to 0.45"——最高值为 EM 0.472 (LLaMA CoNLL)，建议核实
- M6: Table 30 Ratio 列 "—" 含义未说明
- M7: Limitations 未讨论 closed-source API 模型的 degeneracy profile 差异
- M8: 附录 a–ag（33 个子附录）导航困难，建议增加 TOC

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成**完全共识**：

1. **[AGREE] 标题-范围不匹配**（C1）：最高优先级修订。标题 "Structured Generation" 与 NER-centric 证据严重不匹配。
2. **[AGREE] 因果语言不当**（C2）：全文因果动词需统一替换为相关性语言。
3. **[AGREE] k 值不一致**（C3）：Abstract k=19 需核实修正。
4. **[AGREE] 诊断框架是核心贡献**：四阶段级联设计精巧，NER 实验覆盖度典范。
5. **[AGREE] 统计严谨性优秀**：Holm-Bonferroni + bootstrap + multi-seed 远超同类论文。
6. **[AGREE] RE 混淆**（W2）：span error 使 RE 分析测量的是 NER 错误传播。
7. **[AGREE] Prescriptive gains 有限但可接受**（W5）：对 diagnostic 论文，~1pp escape route 不需大效果量。

---

## Reviewer Divergence

| 问题 | R1 | R2 | 分析 |
|------|----|----|------|
| Prescriptive gains 严重度 | Should-Fix (W5) | Critical (N2) | R1 论点更有说服力——论文主贡献是诊断框架，negative results 有独立价值。R2 同意若其他问题修复可降级。**采纳 R1: Should-Fix。** |
| 论文结构 (§3–7 交织) | REBUT（diagnostic narrative 合理） | Critical (N3) | R1 引用 ACL/EMNLP 先例（Chen 2024a, Yun 2025）论证 interleaved 结构有据可循。论文的 hypothesis-driven diagnostic 叙事需要在方法中嵌入初步结果。**采纳 R1: 非缺陷，建议加 roadmap 句。** |
| "Capability ceiling" 措辞 | REBUT（72B+GPT-5.5 已测） | W1（3B–8B 仅） | R2 事实前提有误——论文已测 4B→72B + GPT-5.5。R1 纠正有据。**R2 W1 撤销。** |
| Abstract 信息密度 | REBUT（empirical NLP 惯例） | W4 | R1 引用同类论文先例。当前数字密度尚可接受。**采纳 R1: 非缺陷。** |
| Related Work 后置 | REBUT（标准做法） | W5 | ACL/EMNLP 无硬性要求。概念依赖决定后置更合理。**采纳 R1: 非缺陷。** |
| "Inverse Scaling" 标题 | REBUT（R2 误读） | M6 | 论文描述的确是 performance degradation with increased N，符合 inverse scaling 定义。**R2 M6 撤销。** |
| 干预实验 (R1-Q3) | 要求 | REBUT（不可行） | R2 正确指出 degeneracy 是 emergent property，完全干预不可行。准因果证据链（MBR 理论/条件分析/温度扫描）部分缓解。**采纳 R2: 不要求正式干预，但需在 Discussion 讨论局限。** |

---

## Questions（需作者澄清）

1. **k=19 vs k=21**: 请确认 Abstract "selection family k=19" 的来源。Table 13 有 21 行。
2. **RE oracle entity spans**: 是否考虑过先用 oracle entity spans 隔离 RE-specific 的 SC 失败？
3. **Degeneracy 因果方向**: 是否有任何证据（超出温度扫描）支持 degeneracy→selection failure 的因果方向？
4. **Entity-wise independence**: Proposition 1 的 independence 假设在 NER 中是否合理？相邻 entity 预测常相关。
5. **GPT-5.5 SQL MDE**: n=196 instances 能检测到的最小效应量是多少？

---

## Missing References

两位 Reviewer 共同建议补充：
1. **DeNero et al. (2009)** — consensus decoding in MT，与 entity construction 的 MBR 等价性直接相关
2. **Huang et al. (2024)** — "Large Language Models Cannot Self-Correct Reasoning Yet"，self-verification 失败的相关讨论
3. **Desai & Durrett (2020)** — calibration of pre-trained transformers for sequence labeling
4. **Aronica et al. (2024)** — structured IE output improvement（如与 entity construction 方向相关）

可选补充：
5. KDD 2025 UQ & Calibration survey
6. Test-time Scaling of LLMs survey (arXiv:2511.14772)

---

## External Review (Stanford Agentic Reviewer)

未启用（项目配置中 external_review.paperreview_ai.enabled 不存在）。

---

## Visual Layout Check（非评分项）

**状态**: done（耗时 ~4 分钟）
**结果**: 0 critical, 6 warning, 16 info

主要 findings：
- **[warning] Pages 1–2**: 前两页纯文本无 display item，第一个视觉锚点 Figure 1 在 page 3。建议提前或加 teaser figure。
- **[warning] Page 8**: Section 8 (Related Work) + Section 9 (Discussion) 整页纯文本，与 pages 6–7 高密度形成反差。
- **[warning] Page 17**: Figure 6 heatmap 单色渐变（黄→深绿），色盲读者可能难以区分。建议双色发散色板。
- **[warning] Pages 40, 45, 46**: 附录表格后大面积空白（>2/3 页），可重新排列。
- **[info]** 主文 8 页含 3 Figure + ~8 Table = 11 display items，密度充足。所有表格 booktabs 风格统一。无 margin 溢出、未解析引用或 LaTeX 错误。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | 综合评分 | 说明 |
|------|---------|------|
| Soundness | 3.5/5 | NER 诊断方法论扎实，但 claim scope 超出证据（RE/SQL），因果语言与证据不匹配，k 值不一致 |
| Excitement | 2.5/5 | 负面结果有警示价值，诊断框架新颖，但 prescriptive gains 边际化，set-valued SC 失败非完全出人意料 |
| Reproducibility | 4/5 | 附录极详尽，公开数据集，承诺代码释放 |

**判断依据**:

R1 给 3.5 (Borderline Conference), R2 给 3.0 (Findings)。三个 consensus critical 问题（标题 overclaiming、因果语言、k 值）中，C1 和 C2 是系统性问题——标题和全文的 scope 声明与证据不匹配，因果语言贯穿全文多处。这些不是局部修补可解决的，需要重新定位论文 scope 并统一语言。C3 是技术性问题但影响可复现性。

论文在 NER 范围内的诊断深度和统计严谨性是其核心竞争力，足以达到 Findings 水平。但 "Structured Generation" 的宏大标题与 NER-centric 证据之间的 gap，以及 prescriptive results 的边际增益，限制了 Main Conference 的竞争力。

**如果作者能修复**：(1) 标题收窄为 NER-specific，(2) 全文统一相关性语言，(3) 核实 k 值——评分可上调至 **3.5 (Borderline Conference)**。

**Confidence: 4/5** — 两位 Reviewer 均仔细审读全文 46 页（含附录），对 NER/IE、SC 文献和统计方法熟悉。

---

## Detailed Comments（逐节）

### Abstract
- 信息密度当前可接受（交叉后共识），但 "ρ up to 0.45" 需核实（最高 EM 0.472）
- "selection family k=19" 需修正为实际值
- "structured generation" scope 需收窄

### Introduction (§1)
- Contribution #1–#3 定位准确；Contribution #4 (prescriptive) 应降低 framing 强度
- "our diagnostic framework fills this gap" → 应改为 "characterizes" 或 "identifies"
- "four failure modes explaining where and why" → "characterizing where and how"

### Diagnostic Framework (§2)
- 方法论完善：5 信号定义清晰、evaluation protocol 明确
- per-sample vs instance-level 区分是重要概念贡献

### How Self-Verification Fails (§3)
- ESJ/MRSC/LSC 三个探针的 converging evidence 是强项
- Hidden-state probe (AUROC 0.63–0.88) 提供了 introspection boundary 的定量证据

### Where Single-Signal Selection Fails (§4)
- Definitional vs empirical 二分法处理得当
- LP compression (median 0.041 nats) 是重要发现
- Table 1 清晰展示 selection gap

### Adaptive Methods (§5)
- Table 2 方法总结有效
- Cross-model SC (+0.42pp) 有趣但仅 1 数据集 1 模型对
- Supervised verifier AUC=0.923 → +0.30pp 的 disconnect 是重要 negative result

### Threshold Regime Analysis (§6)
- MBR 等价性（Proposition 1）是 clean 的理论贡献
- Degeneracy bound 松散需在主文讨论（W1）
- Inverse scaling (40/58 transitions negative) 是值得注意的发现

### Experiments (§7)
- Setup 详尽；QE results (Table 3) 清晰
- Few-NERD contrast (Table 4) 是最有说服力的实验
- Entity construction (Table 5) 结果 dataset-dependent，CoNLL 负增益

### Related Work (§8)
- 后置位置合理（交叉后共识）
- §8.1 与 Yun et al. 差异化需强化
- 缺 DeNero 2009, Huang 2024 等引用

### Discussion (§9)
- "Degeneracy governs" 需改为相关性语言
- 实用建议（construction when D<22%）有价值但应标注为 empirical pattern

### Conclusion (§10)
- 简洁有效
- 缺 cost-effectiveness 讨论（Table 61 应在此引用）

### Limitations
- 覆盖面合理，长度符合 EMNLP 规范
- 缺 closed-source API degeneracy profile 讨论

### Appendix
- 60+ 表格极详尽，可追溯性高
- 导航困难（a–ag），建议加 TOC