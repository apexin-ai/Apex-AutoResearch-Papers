---
round: 8
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-21T17:41:35.890844+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 10 (Fresh Review)

**论文**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families
**Venue**: EMNLP 2026 via ARR May 2026
**审稿模式**: Fresh（重新审稿，无历史上下文）
**Reviewer 配置**: 2 人（R1 方法严谨性+实验设计+统计分析 / R2 新颖性+完整性+相关工作+写作质量）
**轮次**: 1 轮初审 + 1 轮交叉分享，关键问题达成共识，无需进入 Round 2

---

## Summary

本文对"benchmark contamination 是否统一 inflate 模型分数"这一社区默认假设进行了系统性实证检验。通过受控 SFT 注入（LoRA, 5 个剂量水平）对 5 个模型家族（4 个独立实验室，7B-14.7B）进行实验，发现 contamination 产生质的不同剂量-反应模式——从 Immune（Phi-4, ±0.5pp）到 Collapse（Qwen-14B, -9 to -25pp）。论文进一步提出 ContamCal 两阶段管线（多信号 RRF exposure mapping + contamination-augmented IRT），提供域级污染诊断。DiD 分析在 MMLU 上未发现 item-specific memorization（MDES 1.2-2.0pp），支持全局能力调节而非记忆化机制。

---

## Strengths

1. **受控注入实验设计是核心优势**。在 contamination 文献中大多为观察性研究的背景下，本文通过 controlled SFT injection 实现了对 dosage 的精确控制（5 个水平 × 5 个家族 × 3 seeds），使因果推断成为可能。这是相对于 Han et al. (2026) 观察性 DIF 和其他检测方法的本质优势。[R1, R2 共识]

2. **"contamination ≠ inflation" 的核心发现有实际意义**。4 种定性不同的剂量-反应模式（Immune, Collapse, V-recovery, Benefit）挑战了社区默认假设，对 leaderboard 解读和模型评估实践有直接影响。Table 1 和 Figure 1 清晰呈现了这一发现。[R1, R2 共识]

3. **DiD 分析严谨**。Treated vs untreated items 的差分-差分检验逻辑清晰，post-hoc power analysis（MDES）正确计算和解读，ARC 的低功效被恰当标注。"No detectable item-specific memorization at current power levels" 的表述诚实且 bounded。[R1 评级 Acceptable]

4. **Cross-benchmark transfer 分析丰富了理解**。MMLU-targeted contamination 对 GSM8K 的正迁移（所有非排除家族 +1 to +16pp）和方向反转（Qwen-7B: MMLU -1.8pp 但 GSM8K +10.1pp）是有价值的实证发现。[R1, R2 共识]

5. **信号失效特征化有实践价值**。Min-K%++ 在 0.5B 处的方向反转（Cohen's d = -1.55 to -1.98）对使用 membership inference 做 contamination detection 的实践者有直接警示意义。[R2 特别标注]

6. **统计方法论透明度高**。论文诚实报告了 CI over-coverage (83%)、PPP 值、MDES、先验敏感度、Appendix K "exploratory status" 等局限。11 页 Appendix 覆盖了 robustness checks、sensitivity analyses、parametric DR model comparison 等。[R1, R2 共识]

---

## Weaknesses

### Must-Fix（3 项，影响接收决定）

**MF-1** [R1-N1, R2 AGREE] **J=16 先验主导 + P(γ<0) 数值不一致 + Bonferroni 显著性声明不稳健**

论文在 J=16 配置下的 IRT 定量结论存在三层问题：
- **先验主导**：Appendix K 承认 "J=16 provides insufficient data to override the prior"，后验均值跨先验变化 2.6×（0.34→0.89），50% CI over-coverage 达 83%。
- **数值不一致**：Section 5.7 报告 Social Sciences P(γ<0)=99.7%，但 Appendix K Table 10 在同一 N(0,1) 先验下显示 P(γ<0)=98.48%。ESS>3800 排除 MCMC 随机变异，差异来源未解释。
- **Bonferroni 声明不成立**：8 次检验的 Bonferroni 阈值为 P>99.375%。Table 10 的 98.48% 未达标；即使取最宽松先验 N(0,2) 的 98.95% 仍未达标。Section 5.7 "crossing the Bonferroni-corrected threshold" 声明与论文自己的先验敏感性数据矛盾。

**建议**：(1) 解决 §5.7 与 Table 10 的数值差异来源；(2) 报告 P(γ<0) 范围而非单一值；(3) 将 Bonferroni 声明降级为 "approaching Bonferroni significance"；(4) 主文中所有 γ 定量结论标记为 exploratory。

**MF-2** [R2-N1, R1 AGREE] **N=5 家族归纳 4 类 taxonomy 的统计基础不足**

四类分类中 Collapse 仅 Qwen-14B（n=1），V-recovery 仅 Qwen-7B（n=1），两者均来自同一 Qwen2.5 家族。无法排除这两种模式是 Qwen 架构特异性行为。论文 §5.1 写 "This empirical taxonomy is preliminary at N=5 families" 是诚实的，但 Abstract 和 Introduction 使用 "four qualitatively different dose-response patterns" 和 "taxonomy" 时 scoping 不足。Section 6 "Two of four patterns attested in ≥2 independent families" 有误导性——Benefit 的两个实例（OLMo-2, Gemma-2）均为 construction 家族，非 OOS。

**建议**：(1) Abstract/Introduction 将 "taxonomy" 替换为 "profiles" 或 "observed patterns"；(2) 明确承认 Collapse/V-recovery 各 n=1；(3) 讨论 Qwen 家族特异性的可能。

**MF-3** [R2-N3, R1 AGREE] **Out-of-sample 验证仅覆盖 Immune（四类中最不 interesting 的一类）**

LLaMA-3.1-8B 被分类为 Immune——最容易验证的模式（不受影响即可）。Collapse、V-recovery、Benefit 三类均无独立家族的 OOS 验证。Limitations 未列此为局限。

**建议**：(1) 在 Limitations 中明确承认 OOS 验证的局限性；(2) 讨论验证其他模式的条件和计划。

### Should-Fix（7 项，影响评分但不一票否决）

**SF-1** [R1-W1, R2 AGREE] **AUGMENT 模式的数据量混淆未讨论**。d000=50k→d100≈66.5k (+33.1%)，高 dosage 准确率提升可能部分来自更多训练数据。DiD 控制了 item-level 混淆，但 aggregate-level 混淆（尤其影响 Benefit 和 V-recovery 解释）未被讨论。Limitations 应补充。

**SF-2** [R1-W2, R2 AGREE] **γ 参数化选择（outside a_i）未论证**。论文采用 σ(a_i(θ-b)+γ·e)，标准 DIF 为 σ(a_i(θ-b+γ·e))。两种形式含义不同（logit-constant vs ability-constant）。如果全局能力调节是主要机制（DiD 证据支持），标准参数化可能更合适。需讨论选择理由。

**SF-3** [R1-W3, R2 AGREE] **MMLU PPP=0.16-0.25 仅在 Appendix K，主文未报告**。论文核心模型在 MMLU（主要分析基准）上 PPP 显著低于理想值 0.5，但主文仅报告了 ARC 的 PPP=0.003。两个 benchmark 的 IRT 模型均存在拟合问题应在正文提及。

**SF-4** [R2-W2, R1 AGREE] **方法新颖性定位不够明确**。2PL+γ 是标准 explanatory IRT/DIF 在 LLM 评估中的应用，IRT 建模层面无技术创新。论文应在 §3.3 或 §6 明确定位：新颖性在于受控注入实验设计和实证发现，而非 IRT 模型本身。

**SF-5** [R2-W3, R1 AGREE] **与 Han et al. (2026) 和 Schaeffer et al. (2026) 的比较不充分**。Han et al.（DIF-based contamination quantification）和 Schaeffer et al.（pretraining-stage controlled injection）是最直接的竞争/互补工作，当前仅一句话提及。需要方法论层面的显式对比。

**SF-6** [R1-W4, R2 AGREE] **LoRA r=16 参数比例未量化报告**。Limitations 定性讨论了 Phi-4 vs Qwen-14B 反驳，但未报告各模型实际可训练参数百分比。

**SF-7** [R1-W5, R2 AGREE] **300/14,042 MMLU item 子集的代表性**。IRT 在 2.1% 的 MMLU items 上拟合（选择标准为 exposure 方差最大化），引入选择偏差。低 exposure 变异 items 的污染效应可能不同。

### Minor（8 项）

- **m1**: "taxonomy"/"profiles"/"patterns" 术语交替使用，建议统一。[R2-M1, R1 AGREE]
- **m2**: Algorithm 1 阈值（τ=2pp, σ=5pp）无理论推导。Appendix P grid sweep 已验证稳定性，但正文应简要说明参数设定理据。[R1-M4, R2 AGREE]
- **m3**: Figure 1 各 panel y 轴范围不同，可能误导 effect size 感知。[R2-M4, R1 AGREE]
- **m4**: GSM8K 评估 max_new_tokens=256 可能截断 CoT，附录已 caveat 但主文应提及。[R1-M5, R2 AGREE]
- **m5**: n=3 seeds CI 宽度 1.5-14.5pp 限制精度，但方向一致性标准合理。[R1-M3, R2 AGREE]
- **m6**: 5%→25% 剂量间距跳跃可能遗漏 V-recovery 拐点。[R1-M2, R2 AGREE]
- **m7**: RRF vs 学习型融合方法对比缺失，但信号正交性（|ρ|<0.06）和消融已充分支持。[R1-M1, R2 AGREE]
- **m8**: Contribution 2（null result）的 Abstract 表述可被误读为 positive 发现。[R2-M2, R1 partial rebut]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识（均标注 [AGREE]）：

1. **J=16 先验主导问题是全文最重要的技术发现** [MF-1]——P(γ<0) 数值不一致直接影响论文四大发现之一的可信度
2. **Taxonomy 过度泛化** [MF-2]——N=5, Collapse n=1, V-recovery n=1, "taxonomy" 措辞过强
3. **OOS 验证不足** [MF-3]——仅覆盖 Immune，最不 interesting 的一类
4. **定性贡献稳健** [Strengths 1-6]——受控注入设计、核心发现、DiD 分析、cross-benchmark transfer 均获两人认可
5. **AUGMENT 混淆** [SF-1]、**γ 参数化** [SF-2]、**PPP 报告** [SF-3]、**新颖性定位** [SF-4]、**相关工作** [SF-5]——7 个 Should-Fix 全部达成共识

---

## Reviewer Divergence

**R2-N2: ContamCal 校准 MAE 不优于 Raw Accuracy** [DIVERGENT]

- **R2 立场 [Must-Fix]**：Table 4 B0 Raw MAE=0.006 vs ContamCal MAE=0.009。核心方法在校准指标上未超越 baseline，削弱方法贡献的实用价值声称。
- **R1 立场 [Not an issue]**：论文 §3.3 明确预测并解释了这一结果——"Eq.3 depends on θ_j, not γ directly, predicting that vanilla 2PL (γ=0) achieves comparable calibration to 2PL+γ, with γ_k serving diagnosis rather than calibration." Table 4 的结果是理论一致性的验证而非缺陷。ContamCal 的价值在于域级诊断（Social Sciences γ_ss=-0.63），非数值校准。
- **Director 判定**：R1 的 rebut 有力——论文确实在 method section 预测了这一结果并定位 γ 为诊断工具。但 R2 的关注也合理：如果 ContamCal 的校准不优于 raw，且其诊断价值（γ）受先验主导影响（MF-1），则方法的整体 practical value 需要更清晰的定位。**降级为 Should-Fix**：建议在 §5.5 显式阐明 ContamCal 的价值主张是诊断而非校准，并可选地按受影响/未受影响模型分层报告 MAE。

---

## Questions

1. Section 5.7 的 P(γ<0)=99.7% 与 Appendix K Table 10 的 P(γ<0)=98.48% 差异的具体来源是什么？是否使用了不同的 J、item subset 或 MCMC 配置？
2. 是否考虑过 REPLACE 模式（等量替换基础 SFT 数据）以消除数据量混淆？如果未做，原因是什么？
3. 为什么选择 γ 在 a_i 括号外的参数化？是否有预实验显示此形式拟合更优？
4. LLaMA-3.1-8B (53.5%) 的 Immune 与 OLMo-2 (53.8%) 的 Benefit 在 baseline 几乎相同——作者对这种差异的 mechanistic 解释是什么？论文提到 "family-level factors" 但未具体化。

---

## Missing References

R2 验证了 58 条引用，无虚假引用。当前引用覆盖已显著改善。以下参考建议确认：
- Golchin & Surdeanu (ICLR 2024) — 时间戳引用
- Sainz et al. (EMNLP 2023 Findings) — contamination survey
- Yang et al. (2023) — rethinking benchmark contamination
- 以上在 Round 8 action items 中标注 open，需确认是否已全部添加

---

## External Review (Stanford Agentic Reviewer)

**状态：未返回**（pending since 2026-05-21T17:14:04Z）

外部审稿请求已发送至用户群，当前仍在等待。本报告不等待外部审稿。如用户后续提交 paperreview.ai 审稿结果，可作为补充参考。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成（2026-05-21T17:17:35Z）。0 critical / 4 warning / 14 info。

**Warnings**:
1. **Page 2**: Figure 1 图例文字偏小，5 条线标签打印时可能难以辨认。建议放大图例字号或移至图内空白区域。
2. **Page 8**: 页面过度密集——2 个 table + 1 个 figure + 4 个 section。Figure 2 被压缩，标签可能低于可读阈值。
3. **Page 13**: Figure 4（Signal Reliability heatmap）单元格内数字 ≤6pt，打印需放大镜。建议改为 figure* 全宽。
4. **Page 17**: Figure 7 和 Figure 8 共挤一页，axis label 极小，严重影响可读性。建议分页。

**其他确认**：格式合规（ACL template, double-blind, 8 页正文, Limitations/Ethics 完整），无 margin 溢出、公式渲染错误或未解析引用。

---

## Overall Assessment

**评分: 3.0 (Findings)**
**置信度: 4/5（高）——两位 Reviewer 独立收敛于相同评估，交叉回应后共识充分**

**理由**：

论文的**定性贡献**是真实且有价值的：受控注入实验设计在 contamination 文献中是首创性的系统性工作，"contamination ≠ inflation" 的核心发现挑战了社区默认假设，DiD 分析严谨，cross-benchmark transfer 分析丰富了理解。实验规模（50+ checkpoints, 3 benchmarks, 3 seeds）和 Appendix 的详尽程度体现了扎实的研究工程。

但论文存在**三个 Must-Fix 问题**使其目前不适合 Conference track：
1. **IRT 定量结论脆弱**——J=16 先验主导，P(γ<0) 数值不一致，Bonferroni 声明与自身数据矛盾。Domain-level heterogeneity 是核心贡献之一，但其统计基础在当前版本中不可靠。
2. **Taxonomy 声称过度**——N=5, Collapse/V-recovery 各 n=1 且来自同一家族，"taxonomy" 措辞暗示的泛化性缺乏支撑。
3. **OOS 验证不足**——仅验证了最 trivial 的 Immune 模式。

这些问题是**可修复的**（主要涉及 reframing/caveating 和数值核查，不需要新实验），修复后论文的 soundness 会显著改善。当前版本适合 Findings track，修订后有潜力达到 Borderline Conference (3.5)。

**评分参考**（EMNLP 2026 ARR）：
- 3.0 = Findings（可被 Findings 接收）
- 3.5 = Borderline Conference
- 4.0 = Conference（可被主会议接收）

---

## Detailed Comments

### Section 1 (Introduction)
- "four qualitatively different dose-response patterns" 应加 "in our five-family sample" 或替换 "taxonomy" 为 "profiles" [MF-2]
- Contribution 1 中 "Out-of-sample validation... provides preliminary evidence for generalizability" 应明确仅覆盖 Immune [MF-3]

### Section 3.3 (Method: IRT)
- Eq.2 的 γ 参数化选择需要论证段落 [SF-2]
- 添加定位语句："Our modeling contribution is not in the IRT specification itself—which follows standard explanatory IRT—but in the controlled injection design." [SF-4]

### Section 4.1 (Experimental Setup)
- 报告每个 dosage 的总训练集大小（d000=50k, d005≈50.8k, ..., d100≈66.5k）[SF-1]
- 报告每个模型的 LoRA 可训练参数百分比 [SF-6]

### Section 5.5 (Calibration Quality)
- 报告 MMLU PPP=0.16-0.25 并简要讨论 [SF-3]
- 阐明 ContamCal 价值主张为诊断而非校准 [divergence resolution]

### Section 5.7 (Domain-Level Analysis)
- 解决 P(γ<0) 99.7% vs 98.48% 不一致 [MF-1]
- 将 "crossing the Bonferroni-corrected threshold" 降级 [MF-1]
- 标记所有 γ 结论为 exploratory [MF-1]

### Section 6 (Discussion)
- 扩展 Han et al. 和 Schaeffer et al. 比较 [SF-5]

### Limitations
- 补充 AUGMENT 模式数据量混淆 [SF-1]
- 补充 OOS 验证仅覆盖 Immune [MF-3]
- 补充 300-item 子集代表性 [SF-7]

### Abstract
- 替换 "taxonomy" 相关措辞 [MF-2]
- 确认 P(γ<0) 数值与正文一致 [MF-1]