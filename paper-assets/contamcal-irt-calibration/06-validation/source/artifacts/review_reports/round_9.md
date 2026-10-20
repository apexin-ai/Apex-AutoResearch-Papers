---
round: 9
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T23:08:06.565232+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 11 (Fresh Review)

**论文**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families
**Venue**: EMNLP 2026 via ACL Rolling Review
**Reviewers**: R1 (方法严谨性 + 实验设计) / R2 (新颖性 + 完整性 + 写作)
**日期**: 2026-05-22

---

## Summary

论文提出 ContamCal 框架，通过 controlled SFT injection（LoRA, 5 个剂量水平）到 5 个家族的 6 个模型（7B-14.7B），结合 contamination-augmented IRT (2PL+γ) 量化 benchmark contamination 的 dose-response 效应。主要发现：(1) 四种 dose-response pattern（Benefit, Immune, Collapse, V-recovery）；(2) 65-70% MMLU baseline band 内模型最脆弱；(3) DiD 分析未检测到 item-specific memorization；(4) Min-K%++ 在小规模模型上出现 directional reversal；(5) IRT 参数恢复需 J≥50。

---

## Strengths

1. **Controlled injection 填补方法论空白** [R1-S1, R2-S1, AGREE]：首个 controlled contamination dosage + clean control 的准实验因果框架，跨学科借鉴药理学 dose-response 建模。
2. **IRT 建模 principled** [R1-S2, R2-S4, AGREE]：2PL+γ 将 contamination exposure 作为连续变量建模，是 DIF 分析的自然推广。Bayesian inference via Stan + convergence diagnostics 体现良好统计实践。
3. **实验覆盖面广** [R1-S3, R2-S2, AGREE]：7 个 baseline 对比、cross-benchmark transfer、domain decomposition、out-of-sample validation、signal ablation。附录 A-Z 极详尽。
4. **Min-K%++ directional reversal** [R1-S4, AGREE]：对 contamination detection 社区有重要 cautionary value。
5. **Simulation 边界条件** [R1-S5, R2-S5, AGREE]：J≥50 的实用建议和 CI coverage 分析有参考价值。
6. **DiD null finding** [R2-S5, AGREE]：item-specific memorization 的否定结果是有价值的负结论（附 MDES）。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. [Critical] AUGMENT 设计引入 data quantity confound——缺少最关键的控制实验** [R1-N1, R2-W1+W5, CONSENSUS]

Section 4.1 采用 augmentation 设计，高剂量组系统性包含更多训练数据（d000 ~50k → d100 ~65.4k，+30%）。Benefit pattern (+1.2-4.2pp) 可能部分或完全由 data quantity 而非 contamination content 驱动。此 confound 的影响范围极广：
- Benefit 因果解释受损
- DiD null finding 的"global capability modification"可能只是"more training data"（见 W5）
- 整个 dose-response framework 的 interpretability 被削弱

**两位 Reviewer 一致认定 data-quantity control 是本文最关键的缺失实验。**

需要：在每个剂量水平添加等量非 benchmark 高质量 Q&A 数据的对照组，或改用 replacement 设计（总训练量恒定）。

**W2. [Critical] Collapse 和 V-recovery 各仅由单一模型支撑，"across model families" 过度泛化** [R1-N2, R2-N1, CONSENSUS]

四种 pattern 中：Benefit 3 个模型 / Immune 2 个模型，但 Collapse 仅 Qwen-14B、V-recovery 仅 Qwen-7B。更严重的是，两者同属 Qwen2.5 家族但呈现相反 pattern——这 **contradicts** 论文关于 family-level consistency 的暗示。Out-of-sample validation (LLaMA-3.1) 仅覆盖 Immune。

Title "Not All Models Are Inflated" 在 4/6 模型实际展现 Benefit/Immune 的情况下有误导性。

**W3. [Critical] Abstract/Title 的 claims 显著超出实验证据** [R2-N1, R1 cross-response AGREE, CONSENSUS]

三个维度的 overclaiming：
- (a) Title 暗示一般性结论，但仅 6 个 ≤14B 模型
- (b) Abstract 列举"pre-training data composition, tokenizer design, and training recipe"作为 vulnerability modulators，但论文无法访问这些因素、无法建立因果归因——这是 observational association 被表述为 causal explanation
- (c) "contamination equals inflation is a gross oversimplification" 过强

### Should-Fix（影响评分但不一票否决）

**W4. [Major] Algorithm 1 的分类是 hand-crafted 规则系统** [R2-N2, R1-W2, PARTIAL CONSENSUS]

Algorithm 1 包含 ≥6 个手工阈值（ε_noise=2pp, ε_sig=0.5 等），四类 pattern 是先验定义而非 data-driven discovery。100% 分类稳定性（Table 14）可能因仅 6 个模型而 trivially stable。τ=2pp 是 Immune/Benefit 的定义性边界——不同阈值可能改变"Not All Models Are Inflated"的结论。

R2 列为 Critical，R1 列为 Major。R1 argues rule-based 在 n=6 场景比 clustering 更透明。**Director 判定 Major**：问题真正的 fix 是增加模型数量，而非换分类方法，但阈值 sensitivity analysis 仍为必做。

**W5. [Major] "Contamination" vs "additional training" 概念张力** [R2-W5, R1-Q5, CONSENSUS]

DiD null + augmentation confound 形成闭环：如果 SFT injection 不导致 item-level memorization，且高剂量 = 更多训练数据，那么 Benefit pattern 的最 parsimonious 解释是"additional supervised training improves general capability"而非 contamination-specific 机制。论文的整个叙事建立在 SFT injection 确实模拟了 contamination 这一前提上，但 DiD null finding 可能 undermine 该前提。

**W6. [Major] n=3 seeds 统计功效不足** [R1-W3, R2-W3, CONSENSUS]

n=3 下 directional consistency 有 12.5% 概率纯由 chance 产生。Cross-seed magnitude 变化约 35%（Qwen2.5 Δ: +2.90 to +3.92）。Collapse 和 V-recovery 无跨种子复制报告。n=3 下 t-distribution 的 95% CI coverage 偏离 nominal level。

**W7. [Major] DiD 的 parallel trends 假设未检验** [R1-W4, R2 AGREE]

Treated items（注入 SFT corpus 的 benchmark items）和 untreated items 可能在 difficulty、topic、format 上系统性不同。SFT 可能对不同 difficulty 的 items 产生差异化影响。论文未提供 pre-treatment trends 对比或 balance check。

**W8. [Major] 2PL+γ 可识别性讨论不足** [R2-W4, R1 AGREE]

θ_j 和 γ_k·r_ij 之间存在可识别性问题。如果 e_ij（exposure score）与 item difficulty b_j 相关，γ 和 b_j 会有 collinearity。§3.3 讨论过于简略。Simulation（Appendix F）未模拟 e_ij-b_j 相关场景。

**W9. [Major] 模型规模上限 14B，缺乏大规模模型覆盖** [R1-W5（R2 修正）, R2-N1]

R2 修正：Within-family（Qwen2.5）覆盖 0.5B-14B，非 R1 所述"7-14B"。但所有 cross-family 比较均在 7-14B 范围内，无 70B+ 模型。Scaling laws 可能根本性改变 contamination dynamics。

### Minor

- **M1**: d025 排版错误（§4.1 出现两次）[R1-M1]
- **M2**: RRF κ=60 和 |S|=.3 阈值未 justify；S2/S4 AUC≈0.48-0.51（近随机）保留在 RRF 中 rationale 不足 [R1-M2, R2-M4]
- **M3**: LoRA 配置不完整：缺 alpha、dropout、target modules、epochs、batch size、warmup steps、loss curves [R1-M3]
- **M4**: Table 1 "Baseline" 列含义应明确标注（d000 SFT 后 accuracy）[R1-M4, R2-M2]
- **M5**: 300/14042 item subset 高 exposure variance 选择可能引入 selection bias [R1-M5]
- **M6**: Figure 1 y轴 50-75% range 可能视觉夸大 1-4pp 效应，应在 caption 提示 [R2-M3, R1 AGREE]
- **M7**: Algorithm 1 notation 不一致（数学符号 vs 英文名混用）[R2-M1]
- **M8**: Limitations 未提及 LoRA rank 对 memorization capacity 的影响 [R2-M5]
- **M9**: Schaeffer et al. 区别度——R2 认为 Major，R1 认为现有 Section 2 对比已足够（Minor）。**DIVERGENT**，Director 判定 Minor：现有对比已覆盖三个区别维度。[R2-W6, R1 REBUT]

---

## Reviewer Consensus

以下为两位 Reviewer 完全达成共识的关键问题：

1. **[AGREE] Data quantity confound 是最关键缺陷**——augmentation 设计使 dose-response 因果解释不可靠
2. **[AGREE] Extreme patterns 泛化性不足**——Collapse/V-recovery 各 1 个模型，且同家族内相反
3. **[AGREE] Title/Abstract overclaiming**——family-level factors 的因果归因、"gross oversimplification" 措辞
4. **[AGREE] n=3 seeds 功效有限**——方向一致性可能偶然，magnitude 变化 ~35%
5. **[AGREE] "Contamination" vs "additional training" 概念张力**——DiD null + data quantity confound 形成闭环
6. **[AGREE] DiD parallel trends 未检验**
7. **[AGREE] 2PL+γ 可识别性讨论不足**
8. **[AGREE] Min-K%++ directional reversal 有价值**（正面共识）
9. **[AGREE] 实验覆盖面广、附录详尽**（正面共识）

---

## Reviewer Divergence

1. **Algorithm 1 严重性**：R2 Critical vs R1 Major。R1 argues rule-based 在 n=6 下比 clustering 更透明。Director 判定 Major。
2. **Excitement**：R1 3.5（框架可复用）vs R2 2.5（"不同模型反应不同"不出人意料）。
3. **Schaeffer et al. 区别度**：R2 Minor→Major vs R1 Minor。R1 认为 Section 2 已有足够三维对比。Director 判定 Minor。
4. **Overall 评分**：R1 3.5 (Borderline Conference) vs R2 3.0 (Findings)。

---

## Questions for Authors

1. 在 augmentation 设计下（d100 比 d000 多 ~30% 训练数据），是否有 evidence 排除 data quantity 对 Benefit pattern 的贡献？是否考虑过 replacement 设计？
2. Qwen-14B Collapse 和 Qwen-7B V-recovery 同属 Qwen2.5 家族但呈现相反 pattern——如何解释 family-level consistency？
3. 如果 DiD 显示无 item-specific memorization，那 Benefit 的 +1.2-4.2pp gain 的机制是什么？是 contamination 还是 additional training？
4. Algorithm 1 的 τ=2pp 如何确定？如果改为 1pp 或 3pp，分类结果如何变化？
5. DiD 分析中 treated vs untreated items 在 d000 下的 baseline accuracy 和 difficulty 分布是否均衡？

---

## Missing References

- **Rodriguez et al. (2021)** "Evaluation Examples Are Not Equally Informative" — IRT 用于 NLP 评测，与本文 item-level analysis 直接互补。[R2 提出, R1 AGREE]
- **Carlini et al. (2023)** "Quantifying Memorization Across Neural Language Models" — model size 与 memorization 关系，与 scale 限制相关。[R1 提出]
- **Gu et al. (2024)** "OLMES" — 标准化 LLM 评测方法论。[R2 提出, R1 AGREE 建议简要提及]
- **Emax model 文献** — 药理学标准 dose-response 模型，Appendix W 对比了 Hill 但遗漏 Emax。[R1 提出, R2 AGREE]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用。

---

## Visual Layout Check（非评分项）

状态：**已完成**（耗时 ~4 分钟）

**Findings（5 warnings, 16 info）**：
- ⚠️ 正文 8 页仅 1 个 figure（Figure 1, page 2），display items 总计 5 个（1 figure + 1 algorithm + 3 tables），偏少。缺少方法架构图（ContamCal 3-stage pipeline 适合流程图可视化）。
- ⚠️ Page 1 纯文本无视觉锚点；Page 3-4 连续 2 页纯文本（Related Work + Method 推导）。
- ⚠️ Page 6（Experimental Setup）为纯文本页，视觉节奏平淡。
- ⚠️ 末页（Appendix Z）仅 1/3 有内容，2/3 空白。
- ✓ Figure 1 信息传达清晰，dose-response 曲线直接呈现核心发现。
- ✓ Tables 1-3 booktabs 风格，格式专业。
- ✓ Algorithm 1 伪代码排版规整。
- ✓ 附录图表风格一致。
- ℹ️ Figure 6/Figure 8 标签字号偏小。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.0 | 3.0 |
| Excitement | 3.5 | 2.5 | 3.0 |
| Reproducibility | 3.5 | 3.5 | 3.5 |
| Overall | 3.5 | 3.0 | **3.0** |

**评分理由**：

论文选题重要、实验覆盖面广、附录详尽，controlled injection + IRT 框架有方法论价值。但三个 Critical 问题共同构成了一条致命的方法论弱点链：

**Data quantity confound → DiD null → "是 contamination 还是 additional training？"**

这条链条从根本上动摇了论文的核心叙事——"contamination dose-response profiling"。如果 Benefit pattern 主要由额外训练数据驱动而非 contamination content，则论文大部分 findings 的因果解读需要 recalibrate。Overclaiming（Title/Abstract 超出 6 个 ≤14B 模型的 SFT 实验范围）进一步削弱论文的说服力。

Director 综合评分偏向 R2 的 3.0 而非 R1 的 3.5，理由：(1) data quantity confound 未被充分控制是实验设计缺陷而非可轻易弥补的叙事问题；(2) Algorithm 1 作为核心方法论贡献之一，其 hand-crafted 性质在 n=6 模型下无法充分验证；(3) 4/6 模型展现 Benefit/Immune 实际上更支持而非驳斥"contamination ≈ inflation"假说。

**改进路径**：
1. 添加 data-quantity control（最关键）
2. 缩窄 Title/Abstract claims + 替换因果归因语言
3. Algorithm 1 阈值 sensitivity analysis
4. 增加模型数量或将 Collapse/V-recovery 定位为 preliminary observation

通过 (1)+(2) 后有潜力从 3.0 提升至 3.5 (Borderline Conference)。

---

## Detailed Comments

### Section 1 (Introduction)
- ¶1 motivation 清晰，从 benchmark contamination prevalence 到 "actual effect unknown" 的逻辑链条有力。
- Contributions 列表中 C2 ("no detectable item-specific memorization") 与 data quantity confound 之间的张力未被 Introduction 预告。
- "four qualitatively different dose-response patterns" 应限定为 "observed profiles"。

### Section 3 (Method)
- §3.2 RRF fusion: S2 (Min-K%++) AUC ≈ 0.48-0.51, S4 (Self-Critique) 近随机，保留在 RRF 中的 rationale 应在主文说明。
- §3.3 Eq.2: 公式本身一致（γ outside a_k），但 notation clarity 需改进。γ parameterization 选择（outside vs inside a_k）的 substantive justification 缺失。
- §3.4 Algorithm 1: τ=2pp 是 definitional boundary，非 data-driven threshold。需 sensitivity analysis。

### Section 4 (Experimental Setup)
- §4.1: AUGMENT mode 的 data volume 增加（+30% at d100）应在此处量化报告，而非仅在 Limitations 提及。
- LoRA 配置需补充 alpha、dropout、target modules 等关键超参。
- d025 排版错误需修复。

### Section 5 (Results)
- §5.1 Table 1: Collapse/V-recovery 各 1 个模型的事实应在此处突出标注，而非等到 Limitations。
- §5.3: n=3 seeds 的 directional consistency test 应报告 p-value。
- §5.4 DiD: parallel trends 假设需检验；null finding 的"global capability modification"解读需与 data quantity confound 交叉讨论。
- §5.5: 300-item subset selection bias 应讨论。

### Section 6 (Discussion/Conclusion)
- "gross oversimplification" → "requires nuance"
- Family-level factors 归因 → 改为观察性描述
- 缺少"contamination vs additional training"的概念讨论