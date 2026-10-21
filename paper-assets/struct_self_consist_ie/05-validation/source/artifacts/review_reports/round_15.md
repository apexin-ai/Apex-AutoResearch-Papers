---
round: 15
overall_score: borderline
timestamp: 2026-05-16T08:58:54.626080+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 15 审稿报告 — Consolidated Review

**论文**: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition"
**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验+统计; R2: 新颖性+Related Work+写作+格式）
**圆桌流程**: Round 1 独立审稿 → 交叉分享 → 收敛判断（1 轮收敛）

---

## Summary

论文研究 LLM-based NER 中 5 个置信度信号（4 个 instance-level 一致性信号 + 1 个 per-sample LP）的质量估计与样本选择能力，在 SciERC（primary, ~65% F1）、CoNLL-2003（ceiling control, ~91% F1）、WNUT-17（collapse boundary, 48% F1）上评估，使用 Qwen3-8B、LLaMA-3.1-8B 及 4B ablation。核心发现是 "correlation-selection gap"：信号有中等 QE 能力（ρ=0.38 on SciERC）但选择失败，greedy decoding (T=0) 超过所有 N=8 选择策略。诊断两个机制：instance degeneracy（21-58% 实例产生相同 F1）和 LP compression（中位数 within-instance range 0.041 nats）。

---

## Strengths

**S1. QE vs selection 解耦框架有方法论价值** [Both]
将 quality estimation（哪些 input 可靠？）与 sample selection（哪个 output 最好？）解耦是重要的方法论贡献。Figure 1 一张图传达核心发现，设计精良。

**S2. 诊断分析系统性强** [Both]
五层 ablation chain（free-form decoding、entity-token LP、verbalized confidence、non-tied subset、signal combination）逐层排除替代解释。Verbalized confidence baseline（更高 ρ 但更差 selection）特别有力地验证了 gap 概念。

**S3. Within-instance analysis 是最强贡献** [Both]
MBR utility 在 non-degenerate instances 上与 F1 正相关（median ρ=0.52），且 MBR 在这些 instances 上 closes 23-41% of oracle gap——证明 MBR 在有 headroom 时 work。Failure 来自 headroom vanishing 而非 utility misalignment，这与 Eikema et al. (2025) 报告的 MBR failure mode 有 qualitative 区别。

**S4. 实验透明度高** [R1]
对 post-hoc 分析（ε=0.05）、thinking token confound、gold-filtering 方法论、configuration-dependent TOST 结果的主动披露达到高标准。Limitations 诚实详尽。

**S5. Appendix 质量极高** [R2]
16+ appendix sections 提供了 FK independence test、SJ normalizer robustness、ε sensitivity sweep、calibration analysis、diversity quantification、free-form ablation 等全面补充分析。

**S6. 三数据集难度梯度设计** [Both]
虽然 selection 有效测试仅在 SciERC 上（见 MF1），ceiling/medium/collapse 梯度本身是良好的实验设计，为信号行为随难度变化提供了有用的 calibration。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [强共识] Framing conflation: "5 signals all fail" 混淆 definitional limitation 与 empirical finding**
- R1-N2 (critical) + R2-N1 (critical)；交叉验证：R1 AGREE R2-N1，R2 AGREE R1-N2
- 4/5 信号（SJ、VC、FK、EM）是 instance-level，by construction 对同一 input 的所有 N 个候选给出相同分数。Table 2 中这些信号的 "selection" 实际测试的是 consensus-proximity (MBR)。将 MBR failure 归因于 "信号失败" 是 attribution error。
- Abstract ("five confidence signals... yet best-of-N selection fails")、Contribution #1 和 Conclusion 将两类本质不同的 failure 混为一谈。§3.1 第一段已有区分 ("This distinction is consequential for selection") 但未向 Abstract/Intro/Conclusion 传递。
- **真正的 empirical findings 是**: (a) MBR 转换产生 per-sample ranking 后仍失败（despite within-instance ρ=0.52），因 instance degeneracy 消除 headroom; (b) LP 因 compression 失败（median range 0.041 nats）。
- **Required action**: Abstract/Intro 拆分三层叙事——(a) instance-level 需 MBR 转换（acknowledged design property），(b) MBR 转换后仍失败 despite positive within-instance correlation（empirical），(c) LP per-sample but compressed（empirical）。
- **历史**: 此问题自 Round 3 (R3-W2) 首次提出，持续 13 轮未完全解决。

**MF2. [强共识] 核心 claim 实质上仅由 SciERC (n=529) 单数据集支撑**
- R1-N1 (critical)；R2 交叉 AGREE
- CoNLL 是论文自己的 "ceiling-effect control"（oracle headroom 仅 4pp，论文在 Appendix §D 承认 "selection analysis on these configurations is uninformative"）。WNUT-17 是 "signal-collapse boundary"（52% zero F1）。因此核心 finding——greedy > all N=8 selection——仅在 SciERC 上验证。
- SciERC 的 medium-difficulty regime (~65% F1) 可能是 sweet-spot artifact 而非普遍现象。LLaMA/SciERC 提供 cross-model 复现但仍限于同一 domain（科学文本，6 entity types）。
- **Required action**: (1) 增加至少一个 medium-difficulty NER 数据集（OntoNotes subset、ACE 2005、Few-NERD）在 50-70% F1 range 验证; 或 (2) 将所有 claim 显式限定为 "medium-difficulty scientific NER" 并相应调整 title/abstract 泛化程度。
- **历史**: 自 Round 0 (R0-C3) 首次提出，持续 15 轮。

**MF3. [强共识] Table 2 Random (0.610) vs Single (0.645): 3.5pp 差距未解释**
- R2-N3 (critical)；R1 交叉 AGREE
- 在 T=1.0 下，Random（从 N=8 均匀选取）和 Single（一次 T=1.0 采样）的期望 F1 应相同：E[Random] = E[Single] = (1/N)ΣE[F1(yi)]。3.5pp 系统性差距（across n=529 instances, 2 seeds, ±0.003 variance, ~2.7σ）不太可能是随机波动。
- 此差距影响所有 selection method 的 baseline 解读。若 Random 系统性偏低，则 selection methods 相对 Random 的 +3-4pp 可能仅是恢复期望，而非真正的 selection gain。
- **Required action**: 明确 Random 和 Single 的精确计算方式。若定义不同（如 Random=instance-level random draw, Single=per-seed mean），需显式说明并讨论对 baseline 解读的影响。
- **历史**: Round 14 (R14-M1) 作为 info 提出，本轮升级为 critical。

**MF4. [方向共识, Severity 分歧] 2-seed Fisher combined p 统计效力不足**
- R1-N3 (critical) + R2-W6 (should-fix)；R2 交叉 REBUT on severity（同意方向）
- 核心 negative conclusion "no signal significantly outperforms single-sample (all p>0.05)" 基于 2-seed Fisher combined p。Bootstrap 95% CI [-3.0, +4.2]pp（宽 7.2pp），远超 oracle headroom 40%。
- **R2 反驳 severity**: Cohen's d=0.038 接近零是更可靠的证据；TOST equivalence、4 cross-configurations 复现、greedy comparison 构成多重证据链，超越单一 p-value。
- **共识 action**: (1) 报告 selection F1 的 3-seed variance（当前仅报告 QE 的 seed stability）；(2) 主文从 "all p>0.05" 叙事转向 "d=0.038 with multiple convergent lines"；(3) 考虑 power analysis。

### Should-Fix（影响评分）

**SF1. [共识] Instance degeneracy: fine-tuning recipe artifact 未排除**
- R2-N2(b) + R1 交叉 PARTIALLY AGREE
- LoRA rank=32, dropout=0, 5 epochs（Table 9），SciERC 未用 load_best_model_at_end。8B vs 4B degeneracy 差异（21% vs 10.4%）可能反映 larger model with same epochs overfits faster，而非 capability-intrinsic property。
- **Action**: 在 Discussion/Limitations 显式承认 fine-tuning recipe confound；理想情况提供 LoRA rank 或 epoch ablation。

**SF2. [共识] 与 Yao et al. (2026) positioning: 缺少 hard-prompted degeneracy 讨论**
- R2-W3 + R1 交叉 AGREE
- 关键未回答问题：hard-prompted models 是否存在 instance degeneracy？如果否→degeneracy 是 fine-tuning artifact 非 task-intrinsic。这是论文最强差异化论点但未被显式讨论。
- **Action**: Related Work 或 Discussion 增加显式对比。

**SF3. [共识] "Surpassing all N=8 selection strategies" 修辞过强**
- R2-W5 + R1 交叉 AGREE
- Greedy (T=0, 0.663) vs Single (T=1.0, 0.645) +1.8pp 未经 significance test。如不显著，结论应为 "Greedy ≈ Single > all selection strategies"——failure 是 selection 不如 random single draw，非 greedy 特别好。
- **Action**: 测试 Greedy vs Single 显著性；修辞改为 "selection adds no benefit"。

**SF4. [共识] Non-tied LP subset Bonferroni correction scope 不完整**
- R1-W1 + R2 交叉 AGREE
- Footnote 4 称 "+2.9pp, p=0.004 survives Bonferroni over 5 comparisons"，但未计入 7 个 ε 值的 post-hoc 选择。Full correction: 7ε × 5 signals = 35 comparisons, α_adj=0.0014, p=0.004 不再 survive。
- **Action**: 修正 Bonferroni scope 或改为 "exploratory finding"。

**SF5. [共识] Kendall's W=1.0 (3 seeds) 呈现缺乏 precision caveat**
- R1-W2 + R2 交叉 AGREE
- m=3, n=5 下单个 ranking swap 即导致 W 大幅下降。Main text 需加 precision caveat。

**SF6. [共识] Scale range (3B-8B) 不足以支撑 "intrinsic" claim**
- R1-W3 + R2 交叉 AGREE
- 两个数据点不支持 "intrinsic to capable fine-tuned models" 的外推。
- **Action**: 限定为 "within the 3B-8B fine-tuned regime"。

**SF7. [共识] TOST 等价性 configuration-dependent, main text 未充分呈现**
- R1-W5 + R2 交叉 AGREE
- Qwen-CoNLL: 所有 external δ 下 FAIL（selection degrades 0.9-1.5pp）——信号 actively harmful。此结论比 "no benefit" 更强，但被埋在 Appendix。
- **Action**: Section 4.3 更平衡呈现 TOST 结果。

**SF8. [部分共识] Abstract ρ=0.45 headline 来自 ceiling-effect dataset**
- R2-W1 + R1 交叉 PARTIALLY AGREE
- CoNLL ρ=0.45 受 zero/non-zero boundary inflate (+0.03-0.05)。Primary SciERC ρ=0.38 按 Cohen (1988) 属 medium effect。
- **Action**: Abstract 仅报告 primary ρ=0.38，或明确标注 0.45 来源。

### Minor Issues

M1. Free-form ablation "ruling out" 改为 "provides evidence against"（共识）
M2. VC QE (continuous, Eq.5) vs VC selection (freq>N/2, discrete) 在 Table 2 中共享标签 "VC"，需在 caption 澄清
M3. Greedy vs Single 1.8pp 需 significance test
M4. SciERC checkpoint 未用 load_best_model_at_end，可能增加 degeneracy，需 acknowledge
M5. "Soft Jaccard" 命名（R2 提出，R1 rebut——非共识问题，但可考虑首次使用时加注）
M6. Yun et al. (2025) diversity collapse 与 degeneracy 的联系需显式讨论（1-2 句）

---

## Reviewer Consensus [AGREE]

1. **Framing 必须重构**：区分 definitional (instance-level) 和 empirical (MBR + LP) failure modes
2. **核心 claim scope** 必须限定或跨数据集验证
3. **Random vs Single 差距**必须解释
4. **"Intrinsic" claim** 需限定到已测试 regime
5. **Greedy 修辞**应重新定位
6. **Yao et al. 对比**需补充 hard-prompted degeneracy 讨论
7. **Non-tied LP Bonferroni** correction scope 需修正
8. 两位 Reviewer 独立评分均为 **3.0/5 (Findings-level)**

## Reviewer Divergence [REBUT]

1. **2-seed Fisher p severity**: R1 评 critical，R2 评 should-fix。R2 认为 d=0.038 + 多重证据链比单一 p-value 更可靠。两位同意方向（power 不足），分歧仅在是否 blocks acceptance。
2. **Free-form ablation cross-task inference**: R1 认为 RE reversal (+1.8pp) 削弱 NER "ruling out" claim；R2 认为 NER/RE output structure 不同，NER-specific evidence (std ratio 0.97) 在 NER 范围内充分。**共识: 弱化措辞为 "provides evidence against"。**
3. **"Soft Jaccard" 命名**: R2 认为误导；R1 rebut（footnote + Appendix Δρ<0.01 + 先例）。非共识问题。

---

## Questions for Authors

Q1. [Both] Table 2 Random (0.610) vs Single (0.645): 精确计算公式？3.5pp 系统性差距来源？
Q2. [Both] Instance degeneracy 是否对 fine-tuning recipe 敏感（LoRA rank、epochs、dropout、load_best_model_at_end）？
Q3. [R1] 是否有其他 medium-difficulty NER 数据集上的初步结果？
Q4. [R2, R1 AGREE] Free-form decoding 下 constant-F1 fraction 是否改变？
Q5. [R1] Hybrid 策略（degenerate→greedy, non-degenerate→MBR）的 expected gain？
Q6. [R1] Entity-token LP 的 within-instance ρ（F1）是多少？增加的 variance 是 noise 还是 signal？
Q7. [R2, R1 AGREE] Greedy (T=0) vs Single (T=1.0) 是否经过 significance test？

---

## Missing References

1. Gao et al. (2023) "Scaling laws for reward model overoptimization" — best-of-N proxy signal limitation 的概念联系（R2 提出，R1 PARTIALLY AGREE: 相关性有限，可在 Discussion 提及）
2. Deutsch et al. (2022) "Training and meta-evaluating machine translation evaluation metrics at the paragraph level" — MBR with structural metrics（R1 提出）

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Overall Assessment

**Score: borderline**
**Confidence: 4/5**
**推荐 Track: Findings**

两位 Reviewer 独立评分均为 3.0/5。论文提出了有价值的概念贡献（QE vs selection 解耦）并提供了深入的诊断分析。Within-instance analysis（MBR utility aligned but headroom vanishing）是最强贡献，与 Eikema et al. (2025) 的 MBR utility mismatch 有 qualitative 区别。

但四个 Must-Fix 问题限制了当前版本的可接受性：
1. **Framing inflation**: "5 signals all fail" 将 definitional limitation 包装为 empirical discovery（持续 13 轮未完全解决）
2. **Single-dataset support**: 核心 claim 仅在 SciERC (n=529) 上有效验证（持续 15 轮）
3. **Unexplained baseline**: Random vs Single 3.5pp 差距影响 baseline 解读
4. **Statistical power**: 2-seed Fisher p 不足以支撑核心 negative result

**Findings track 路径**: 解决 MF1（framing 重构）、MF3（Random vs Single 解释）、SF1-SF8 中的写作修正即可满足 Findings track 要求。

**Main conference 路径**: 在 Findings 路径基础上，还需 MF2（增加数据集或进一步限定 scope）和 MF4（statistical power 加强）。

---

## Detailed Comments (Section-by-Section)

### Abstract
- 信息密度仍高——5 信号、3 数据集、degeneracy%、LP nats、5-layer ablation 均出现
- ρ=0.45 来自 ceiling-effect control，可能给 "moderate-to-strong" 错觉
- "Five confidence signals" 统一叙事需拆分
- "Within a narrow model-scale range (4B-8B)" 良好限定

### Introduction (§1)
- Contribution #1 混合 definitional 和 empirical failure——需重构
- Figure 1 + operationalization 有效
- 已正确识别 instance-level vs per-sample 区分但未贯彻到 contribution list

### Related Work (§2)
- 覆盖全面（self-consistency, MBR, uncertainty, calibration）
- Schall et al., Yun et al., Park et al., Eikema et al. 均已引用
- 缺少: Yao et al. hard-prompted vs fine-tuned degeneracy 对比
- 缺少: Yun et al. diversity collapse 与 instance degeneracy 的显式联系

### Method (§3)
- 信号定义数学严谨，evaluation framework 清晰
- §3.1 有关键区分但需向前传递

### Experiments (§4)
- Table 1 QE 结果呈现清晰
- Table 2 Selection 结果是核心但 Random vs Single 差距需解释
- §4.3 "all p>0.05" 叙事应转向 effect size
- Table 4 Degeneracy: 含 4B data，within-instance analysis 是最强部分

### Discussion (§5)
- Instance degeneracy mechanism 论证充分（MBR + within-instance ρ）
- LP compression 诊断系统（四个 hypotheses, constraint-imposed vs model-learned）
- "Intrinsic" 用语需 scope 限定
- Signal combinations: LP×VC 三策略 + oracle tiebreaker +7.9pp 是重要 calibration

### Conclusion (§6)
- 准确总结但继承 framing 问题
- 70B+ open question 恰当

### Limitations
- 全面诚实
- 应增加 fine-tuning recipe confound acknowledgment

### Ethics Statement
- 对论文 scope 而言充分

### 格式合规
- ACL review template ✓, Anonymous ✓, Limitations ✓, Ethics ✓
- 引用: 53 entries, 0 orphan, 44 verified（R2 审核）
- 正文页数需编译确认