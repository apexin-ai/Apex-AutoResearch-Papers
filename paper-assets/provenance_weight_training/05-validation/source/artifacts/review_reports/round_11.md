---
round: 11
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-23T13:33:45.350698+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 12 (Fresh Review)

**论文**: "When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining"
**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)
**审稿模式**: Fresh（无前轮记忆）
**Reviewers**: R1（方法严谨性+实验设计）、R2（新颖性+完整性+写作质量）
**轮次**: 1 轮完成（Round 1 独立审稿 → 交叉分享 → 收敛，无需 Round 2）

---

## Summary

本文研究 detect-and-reweight (D&R) 范式在续训语言模型中应对合成文本污染的有效性条件。在 Qwen3-0.6B 上使用 132M FineWeb 子集（ρ=0.4, 3 seeds）进行可控实验，提出三项分析发现：(1) D&R 先前报告的 PPL 优势中 >95% 可归因于 epoch confound（多轮数据暴露），epoch-matched 后优势从 0.396 缩减至 0.017；(2) 有效 reweighting 要求检测器同时具备足够的 AUC（≥0.9）和良好的校准（ECE≤0.05）；(3) 基于双约束（α_eff ≥ τ, ESS ≥ n_min）的自适应 b* 实现最小干预优于最大化策略。作为实践推论，提出了一个无需 grid search 的自适应 b*，在 ρ≥0.4 时优于 uniform（Δ=−0.020 at ρ=0.4, Δ=−0.032 at ρ=0.6），但效应量极小（~0.11% relative），下游任务无改善。

---

## Strengths

1. **Epoch confound 发现扎实且有方法论价值** [R1+R2 共识]：通过 epoch-matched 控制实验定量证明 D&R 先前报告的 PPL 优势中 >95% 来自多轮数据暴露而非 filtering quality（Table 1, Δ from 0.396 to 0.017, 3 seeds 方向一致）。LR-controlled verification（§5.1）进一步排除学习率调度混杂。这对后续 D&R 研究有直接方法论警示意义。

2. **检测器校准 vs AUC 的 counter-intuitive 发现** [R1+R2 共识]：GPT-2 detector (AUC=0.91, ECE=0.131) 性能劣于 uniform (Δ=+0.098)，而 TF-IDF+LR (AUC=0.94, ECE=0.048) 成功——揭示 calibration 可以逆转 intervention 方向（§5.2, Appendix L），对 data curation 工作有指导价值。

3. **实验设计诚实透明** [R1+R2 共识]：下游 null result（Table 4）、scale 限制（1.7B 效应减弱）、cross-model mixed results（Appendix O）、checkpoint resume artifact（Appendix P）均如实报告，无 cherry-picking。统计校正后不显著的 p 值也在正文中报告。

4. **Appendix 覆盖全面** [R1+R2 共识]：17 节 appendix 涵盖 grid search details、threshold sweep、constraint regime decomposition、α_eff validation、detector comparison、cross-model transfer、低 ρ 分析、checkpoint artifact 等，可复现性强（Reproducibility 4/5）。

5. **Decision framework 有实用价值** [R2]：Table 3 将分析结论转化为 practitioner-friendly 的决策指南（AUC≥0.9, ECE≤0.05, ρ≥0.4），是有价值的综合贡献。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1** [R2-N1, R1 AGREE] **Abstract 超过 200 words 限制**
LaTeX 源码 wc -w 确认 225 words，超出 EMNLP 2026 / ARR 的 200 words 硬约束。Abstract 中包含大量数值细节（Δ=−0.020, ρ=0.4, bootstrap CI, p=0.010 等），应移到 Introduction。格式硬约束违反有 desk reject 风险。
→ 建议压缩到 ≤180 words，删除具体数值保留定性结论。

**C2** [R2-N2, R1 AGREE] **正文超出 8 页限制**
§7 Conclusion 在 PDF p.8 底部开始，延伸至 p.9（约 15-20 行），之后才是 Limitations。EMNLP 2026 规定 §1-§7 主正文 ≤8 页，Limitations/Ethics 不计入但不得含过多额外内容。格式硬约束违反。
→ 建议压缩 §6 Discussion（将 "Effect size in context" 和 "Limitations of α_eff as proxy" 部分内容移至 Limitations 或 Appendix）或 §2 Related Work（"Theoretical Foundations" 子段可移至 appendix）。

**C3** [R1-N1 + R2-N3, 双方 AGREE] **N=3 seeds 统计推断力根本性不足**
全文核心量化结论依赖 N=3 seeds 的 paired t-test（仅 2 df）。关键结果在 BH 校正后均未达 α=0.05：ρ=0.4 p_BH=0.078, ρ=0.6 p_BH=0.064。Bootstrap CI [−0.028, −0.012] 在 N=3 时仅 27 种重抽样，覆盖率保证极弱。Cohen's d=2.86 更可能反映方差被人为压低（seeds 仅影响初始化，data order 固定）而非效应量大。论文先报告 BH 校正再论证 family "structurally heterogeneous" 属于 post-hoc 统计叙事调整。
→ 建议 (a) 增加到 N≥5 seeds，或 (b) 放弃 p 值叙事改为纯效应量+方向一致性报告。
注：epoch confound 的核心发现不受此限——该结论在每个 seed 内独立成立。

**C4** [R1-N2 + R2-N3, 双方 AGREE] **效应量极小（Δ=−0.020 PPL, ~0.11%）+ 下游零改善**
五项下游任务全部 |Δ|≤0.01，adaptive 与 uniform 均为 0.5414（Table 4）。Batch-size extrapolation（3 点拟合幂律 Δ∝B^0.89 外推 32× 到 B=128 预测 Δ≈−0.39）统计学不可靠，但 rebuttal 中作为实际意义的主要论据。在可验证的所有指标上，方法无实际改善。
→ 建议 (a) 删除或大幅降级 batch-size 外推（移到 appendix，标注 hypothesis）；(b) 在 abstract/conclusion 中删除所有 "practical" 残留表述。

**C5** [R1-W1/W3 + R2-N4, 双方 AGREE] **实验范围过窄，不支撑一般性结论**
所有实验基于单一模型族（Qwen3, 0.6B/1.7B）、单一数据集（FineWeb 132M）、自污染设计（generator=trainee）。Self-contamination 人为降低检测难度（AUC=0.94 部分归因于 generator=trainee 的统计指纹匹配）。Cross-model transfer（Appendix O, Llama→Qwen）single seed + mixed results + PPL 比较缺失。"necessary conditions" 是一个逻辑上很强的 claim，但仅在极窄设置上观察到。
→ 建议 (a) 将 "necessary conditions" 改为 "empirically observed conditions in our setting"；(b) 在 abstract/conclusion 中限定 claim 适用范围为 "self-contaminated continued pretraining at 0.6B scale"。

### Should-Fix（影响评分但不一票否决）

**W1** [R1-W2 + R2 AGREE] **α_eff proxy 解释力不足（R²≈0.49）以支撑其核心地位**
α_eff 是双约束中 quality floor 的直接操作变量，但仅解释不到一半的目标方差。r(α_eff, mean_q)=0.80 是 proxy-to-detector-score 的相关性（循环论证），非 proxy-to-ground-truth（r=0.706）。跨 seed spread <0.003 是确定性函数+固定 detector 的预期结果，不构成额外证据。核心缺失：**α_eff-only ablation**（去掉 ESS constraint 只保留 α_eff ≥ τ），无法区分 adaptive b* 的贡献来自 α_eff 质量信号还是 ESS 稳定化。
→ 建议补充 α_eff-only ablation；如果 ESS 是主要贡献者需调整 §6 叙事。

**W2** [R2-W1 + R1 AGREE] **Adaptive b* 方法新颖性薄弱**
权重公式 w=(1−q)^b 完全来自 Drayson et al.；adaptive b* 本质是满足两个阈值条件的最小 b——一个超参数自动选择启发式。论文已标注 "practical corollary"，但 §3 仍占 ~0.75 页。
→ 建议进一步压缩 §3（Algorithm 1 移到 Appendix），正文只保留公式 (1) 和关键直觉。

**W3** [R2-W2 + R1 AGREE] **Epoch confound 适用范围需明确限定**
Epoch confound 主要出现在续训（小数据量 → 多 epoch）设置中。在大规模 from-scratch pretraining（通常 <1 epoch），confound 不成立。§7 "any D&R evaluation that compares at equal training steps without controlling for content epochs risks overstating filtering effectiveness" 过于泛化。§2 也未标注 Drayson et al. 是 from-scratch pretraining——这恰是 epoch confound 成立的前提。
→ 建议在 §7 中加 qualifier 限定为 multi-epoch exposure 场景；在 §2 中讨论 from-scratch vs continued pretraining 的区别。

**W4** [R2-W3 + R1 AGREE] **Detector 测试范围不足**
仅 3 个 detector（TF-IDF+LR, GPT-2 PPL, N-gram PPL），未覆盖当前主流 neural classifiers（RoBERTa/ModernBERT fine-tuned, DetectGPT, Binoculars）。3 个数据点不足以建立 "both AUC and ECE are necessary" 的因果关系——可能存在 discriminative vs generative paradigm 本身的混杂。

**W5** [R1-W4 提出, R2 部分 REBUT] **LR schedule 混淆因素**
Epoch-matched D&R 使用完整 LR schedule 截断至 2553 步，改变了 warmup/decay 比例。Independent-schedule replication（D&R 17.651 vs shared 17.657, Δ=0.006）已基本排除 LR confound（R2 认为 adequate），但缺完整 LR curves 和 upsampling baseline。分歧较小，归为 should-fix。

### Minor（不影响接收）

- **m1** [R2-m5 + R1 AGREE]: ρ 同时表示 contamination ratio（§3-§7）和 Spearman 相关系数（Table 12, Appendix K），符号冲突。建议用 ρ_s 区分 Spearman。
- **m2** [R2-m1 + R1 AGREE]: Table 2 中 Golden Ratio（oracle）和 D&R（multi-epoch）与 fair comparison 方法使用相同 bold 标注，误导可比性。
- **m3** [R2-m3 + R1-m3]: Figure 1 (TikZ) 黑白打印下 orange/blue/violet 不可辨；Figure 2 x 轴标签与 adaptive b* 的关系不够清晰。
- **m4** [R1-m1]: Table 2 中 Golden Ratio 的 w 定义未在 §4 Methods 中给出，需翻 Appendix。
- **m5** [R1-m4]: Appendix Q 的 ρ=0.3 boundary 结果是重要数据点，建议在主文 §5.2 中明确引用。
- **m6** [R2-m4]: Rebuttal 中 "Appendix Q" 标签需核对是否与 LaTeX 标签一致。
- **m7** [R2-m2]: §2 Related Work 占 ~1.5 页，在 8 页限制下偏长（R1 partial REBUT：对 analysis paper 合理，但可作为页面超限的压缩候选）。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成完全共识：

1. **Abstract 超限 + 页面超限**：两个格式硬约束违反，必须在提交前修正。[R2-N1/N2, R1 AGREE]
2. **N=3 seeds 统计检验力不足**：BH 校正后所有核心比较均未达 α=0.05，bootstrap CI 在 N=3 下不可靠。[R1-N1, R2-N3, 双方 AGREE]
3. **效应量过小 + 下游零改善**：Δ=−0.020（~0.11%）在当前 scale 下无实际意义，batch-size 外推不可靠。[R1-N2, R2-N3/W4, 双方 AGREE]
4. **实验范围过窄**：单模型/单数据集/self-contamination + "necessary conditions" claim 过强。[R1-W1/W3, R2-N4, 双方 AGREE]
5. **Epoch confound 是最有价值的贡献**：方法论警示意义真实，不受 N=3 限制。[R1+R2 Strengths §1]
6. **论文报告诚实**：坦承 downstream null、scale limitations、checkpoint artifact。[R1+R2 Strengths §3]

## Reviewer Divergence [REBUT]

分歧极小，仅两点 partial REBUT：

1. **p_BH 位置**（R2-W5 vs R1 partial REBUT）：R2 认为 p_BH 藏在脚注中；R1 指出 p_BH=0.078 出现在 §5.1 正文段落中，非仅脚注。但双方同意应在 Table 2 中并列展示以提高可见性。→ 降级为 minor suggestion。

2. **LR schedule confound**（R1-W4 vs R2 partial REBUT）：R1 认为 independent-schedule replication 细节不足；R2 认为 Δ=0.006 已 adequately 回应。双方同意 upsampling baseline 是更干净的设计。→ 保留为 should-fix。

---

## Questions（需作者澄清）

1. **N=3 设计动因**：是计算资源限制还是有意为之？是否考虑过降低训练步数（如 3000 steps）换取更多 seeds（如 N=7）？
2. **α_eff-only ablation**：去掉 ESS constraint 只保留 α_eff ≥ τ 的 PPL 是多少？这对分离两个 constraint 的独立贡献至关重要。Table 2 有 ESS-only 但缺 α_eff-only。
3. **Proxy 相关性区别**：r(α_eff, mean_q)=0.80（proxy-to-detector-score）vs r(α_eff, true real fraction)=0.70（proxy-to-ground-truth）——前者是否应作为支持 proxy 可靠性的证据？
4. **Batch-size confound**：B=4/8/16 实验是固定 total tokens 还是固定 steps？如果固定 steps，B=16 看到 4 倍 tokens 本身是 confound。
5. **Family-wise correction 策略**：如果仅对 focal comparison（adaptive vs. uniform at each ρ）做校正而非全部 9 个，corrected p-values 是多少？是否考虑过分层检验策略？
6. **Epoch confound 独立性**：epoch confound 核心发现是否可通过 "D&R 1 epoch" vs "uniform 1 epoch" 更简单地验证，不需要 adaptive b*？如果可以，这是否暗示 adaptive b* 对核心 contribution 非必需？

---

## Missing References

两位 Reviewer 建议补充以下引用（已去除重复和误报）：

- **MATES** (Yu et al., NeurIPS 2024) — 动态数据选择，用小模型预测大模型的数据 influence [R2]
- **FineWeb-Edu** (Lozhkov et al., 2024) — 基于教育质量评分的大规模数据过滤，FineWeb 生态系统重要工作 [R2]
- **D4** (Tirumala et al., 2024) — 去重+多样化策略 [R2]
- **Fan et al. (2024)** — importance weighting 在 LM 训练中的 variance-bias tradeoff [R1]

注：DoReMi (Xie et al.) 已在论文 §2 中引用（ref key `xie2023doremi`），R1 建议为误报，R2 已 REBUT 确认。

---

## External Review (Stanford Agentic Reviewer)

未配置。

---

## Visual Layout Check（非评分项）

状态：**done**（2026-05-23 13:10 → 13:13，约 3 分钟完成）

发现（2 warning + 4 info）：

- ⚠️ **Page 5**: Results §5.1 整页无 display item，所有支撑数据（Table 1/2, Figure 2）推至 page 6。建议调整 float 位置。
- ⚠️ **Page 17**: Appendix 末页仅 6 行（~5% 填充），约 95% 空白。
- ℹ️ **Page 2**: Figure 1 (overview) 本质是格式化文字方框，视觉吸引力有限。
- ℹ️ **Pages 3-5**: 连续 3 页无 figure/table，节奏偏文本密集。
- ℹ️ **Page 6**: 单页 3 个 display items（Table 1 + Figure 2 + Table 2），视觉密度过高。
- ℹ️ **Page 12**: Appendix 页面极密集（Proofs + Algorithm 1 + Table 5 + 两个小节）。

---

## Overall Assessment

**Overall**: **3.0 / 5 — Findings**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.0 | 3.5 | 3.0 |
| Excitement | 2.0 | 2.5 | 2.5 |
| Overall | 3.0 | 3.0 | 3.0 |
| Confidence | 4/5 | 4/5 | 4/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |

**理由**：Epoch confound 的发现是真实的方法论贡献——定量证明 D&R 先前报告的优势中 >95% 来自数据重复而非 filtering quality，为后续工作建立了重要基线。这一发现达到 Findings 级别。但以下因素阻止论文达到 Conference (4.0) 门槛：

1. **格式硬约束违反**：Abstract 超 200 words + 正文超 8 页——这些在提交前必须修正，否则有 desk reject 风险。
2. **统计支撑不足**：N=3 seeds + BH 校正后全部不显著——对于一篇以定量分析为核心的论文，这是根本性弱点。
3. **效应量可忽略**：Δ=−0.020（~0.11%），五项下游任务零改善——在可验证的所有指标上，方法没有实际改善。
4. **实验范围过窄**：单模型/单数据集/self-contamination 使得三个 "effectiveness conditions" 的泛化性无法推断。
5. **方法新颖性薄弱**：adaptive b* 本质是现有框架的参数选择启发式。

**建议**：论文最有价值的贡献是 epoch confound 分析和 detector calibration 发现。如果以纯 analysis/empirical study 定位投稿，压缩 adaptive method 部分，增加 seeds 或放弃 p 值叙事，补充 cross-model 实验，修正格式问题，有望达到 Findings 接收水平。

---

## Detailed Comments（逐节）

### Abstract (p.1)
- 225 words, 超 200 限制 [C1]
- 最后一句 "The method transitions from harmful (ρ=0.2) to beneficial (ρ≥0.4), with a sharp boundary in [0.3, 0.4]; the benefit diminishes at 1.7B, and sample size (N=3) limits generalizability" 中对 N=3 限制的自我披露值得肯定

### §1 Introduction (pp.1-2)
- Figure 1 黑白不可辨 [m3]
- 论文定位已从 method 调整为 analysis with practical corollary，较合理 [S4]

### §2 Related Work (pp.2-3)
- 覆盖 5 个子领域，对 analysis paper 合理但占 ~1.5 页，在页面紧张时是压缩候选 [m7]
- 未标注 Drayson et al. 是 from-scratch pretraining vs 本文 continued pretraining [W3]
- 缺失 MATES, FineWeb-Edu, D4, Fan et al. [m-refs]

### §3 Method (p.3)
- 压缩至 ~0.75 页后仍给独立方法贡献的印象 [W2]
- α_eff 定义清晰，但 R²≈0.49 限制了其作为核心信号的可信度 [W1]
- Algorithm 1 可移到 Appendix

### §4 Experimental Setup (pp.3-4)
- 实验细节充分，超参数透明 [S4]
- Self-contamination 设计在此处应更突出地讨论生态效度限制 [C5]
- Golden Ratio 的 w 定义缺失 [m4]

### §5 Results (pp.4-7)
- §5.1: N=3 统计检验力不足 [C3]，效应量极小 [C4]
- §5.1 Epoch confound 部分是全文最强贡献 [S1]
- §5.2: Detector calibration 发现 counter-intuitive 且有价值 [S2]
- §5.2: Epoch confound 适用范围表述过于泛化 [W3]
- §5.3: 缺 α_eff-only ablation [W1]
- §5.4: Batch-size extrapolation 不可靠 [C4, W-batch]
- Page 5 无 display item，Page 6 过度密集 [Visual Check]

### §6 Discussion (pp.7-8)
- Effect size in context 讨论充分 [S3]
- α_eff proxy 局限性讨论到位但 R²≈0.49 的根本问题未解决 [W1]
- Downstream null 分析合理但无法弥补实验验证的缺失 [C4]
- 整节 ~1.5 页偏长，可压缩以解决页面超限 [C2]

### §7 Conclusion (pp.8-9)
- 溢出至 p.9 [C2]
- "any D&R evaluation..." 表述过于泛化 [W3]
- Batch-size amplification 作为 conclusion 内容过于 speculative

### Limitations (p.9)
- 覆盖合理：single scale, single dataset, N=3, detector coverage, self-contamination
- 长度适中（~1 段）

### Appendix (pp.10-17)
- 17 节内容全面，可复现性强 [S4]
- 末页 95% 空白 [Visual Check]
- ρ 符号冲突 in Table 12 [m1]

---

*审稿报告由 Review Director 基于 2 位 Reviewer 的独立审稿、交叉分享和收敛分析汇总生成。*