---
round: 21
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-24T23:23:39.708038+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 21 审稿报告 — Entrainment-Gated Fine-Tuning

**Venue**: EMNLP 2026 via ARR
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1 方法严谨性 + R2 新颖性/完整性）
**轮次**: 1 轮初审 + 1 轮交叉分享，关键问题达成充分共识

---

## Summary

本文研究 hybrid linear recurrent 模型（结合 attention 和 recurrent 组件）在 aggregate benchmark 等价表面下的 per-example 行为差异。使用 Wang et al. (2025) 的 controlled model zoo（5 架构 × 多种 attention ratio × 2 规模 = 30 配置），论文报告三项发现：(1) 不同架构在 per-example 层面高度不重叠（Jaccard ≈ 0.10）；(2) 该不重叠在 4% attention ratio 即出现饱和模式；(3) confidence margin 可部分预测哪些样本受 attention 影响（AUC 0.70-0.74）。

---

## Strengths

**S1.** 新颖研究问题：per-example multiplicity 在 hybrid linear recurrent 模型中是首次系统研究，对模型选择和部署有直接意义 [R1, R2 共识]

**S2.** 控制良好的实验设计：使用 controlled model zoo 隔离架构变量（共享训练数据、tokenizer、超参数），比 D'Amour et al. (2022) 的观察性研究和 Yang & Wang (2026) 的 frontier LLM 比较提供了更强的变量控制 [R1 S2]

**S3.** 统计方法的诚实披露：Section 3.5 坦率承认 n=5 Spearman 和 n=3 bootstrap 的局限性——这种透明度值得肯定，问题在于主文 claim 未始终遵循这些 caveats [R1 S3, R2 同意]

**S4.** 详尽的附录：21 页附录覆盖大量 robustness check（continuous Jaccard、GDN exclusion、scale comparison、seed variation comparison 等），显示作者对潜在问题有充分认识 [R1 S4]

**S5.** 核心观察的直觉有效性：即使统计证据不够强，"aggregate 等价不等于 behavioral 等价" 的基本发现（低 Jaccard ≈ 0.10）在方向上可信，对社区有启发价值 [R1 S5]

**S6.** 5-架构扩展验证（GLA + DeltaNet at 340M）增强泛化性，10 对全部 J ≤ 0.14, p ≤ .002 [R2 S6]

---

## Weaknesses

### Critical

**W1. [Critical, 共识] Spearman ρ 在 n=5 下检验力近乎为零，但驱动了多项关键 claim**

Section 3.5 明确承认 "all Spearman-based inferences are descriptive and exploratory"，但正文多处做了确定性陈述：
- Section 4.2 标题 "Per-Example Overlap **Saturates** at Minimal Attention"
- Conclusion "**saturates** at 4% attention and remains flat"
- Table 2 报告 10 个 benchmark 的 ρ 值，但 8/10 的 |ρ| < 1.0，在 n=5 下不可能达到显著性（最小可能 p = .017）
- Bonferroni 校正阈值 α/10 = .005 在 n=5 下数学上不可能达到，使多重比较校正成为 vacuous exercise
- R2 补充：仅 LAMBADA 的 ρ = -1.0 达到 n=5 下唯一可能的显著水平 p = .017

**影响**：Saturation 是论文的核心 contribution 之一（写入 Abstract 和 Contributions），但统计方法根本无法支撑 claim 的强度。正文 claim 置信度与 Section 3.5 caveat 严重脱节。

**W2. [Critical, 共识] Saturation at 4% 的两个竞争性解释未解决**

(a) 混合架构保留独特逐样本特征（架构指纹）vs (b) 少量 attention 即使行为向 Transformer 收敛（entrainment）。Appendix L Table 15 显示三个架构的 h3-1 correct set 均更接近 Transformer baseline（Δ 为正），支持解释 (b)。Section 4.2 承认需要 random-projection attention ablation 但 "leave to future work"。R1 指出：与 W1 叠加——n=5 检验力不足 + 解释歧义 = saturation claim 双重薄弱。R1 修正 R2 "buried in appendix" 描述为 "discussed but unresolved ambiguity"。

### Major

**W3. [Major, R1 Critical → R2 REBUT → Director 判定 Major] 核心 model zoo 缺少 seed variation**

所有 30 个配置为单次训练 run。Section 7 / Appendix W 用 Pythia 70M seed variation 做参照，但跨架构族、小 14 倍、不同训练数据。

**事实澄清**：R1 引用 "ARC-Easy cross-architecture J=0.332" 有误。R2 核实 Appendix W 实际数据：ARC-Easy within-seed J=0.322 vs cross-architecture J≈0.092（3.5× 差异），LAMBADA within-seed J=0.323 vs cross-architecture J≈0.10（3.2× 差异）。论文主文 Limitations 确认 "within-seed J is 2.7–4.3× higher"。两个 benchmark 一致支持架构效应独立于种子变异。

但 Pythia 70M 校准的外部效度仍有限：(a) 不同架构族（Transformer vs hybrid），(b) 14× 规模差异，(c) Pythia 410M 校准失败。理想情况下需要同一 model zoo 内的 seed variation。

**W4. [Major, 共识] GDN h3-1 的 16 vs 32 head confound**

GDN 在 h3-1 (1.3B) 下使用 16 个 attention heads（vs RetNet/HGRN2 的 32 个），占 3 个架构的 33%。移除 GDN 后 LAMBADA ρ 从 -1.0 变为 -0.7 (p=.233，不再显著)，MMLU ρ 方向完全反转。Per-example saturation 不受 GDN 影响，但 aggregate convergence trend 高度敏感。

**W5. [Major, 共识] Permutation test 保守性论证方向可能有误**

Section 3.5 称 permutation test "conservative"。R1 的分析（R2 称其为"R1 最有价值的技术贡献"）表明：不条件化 item difficulty 使 null baseline 偏低（而非偏高），检验可能是 anti-conservative 而非 conservative。
- 具体逻辑：difficulty-driven 相关性推高 observed Jaccard，但 permutation 打破此相关性使 null 偏低 → observed 更容易超过 null → anti-conservative
- 缓解因素：observed Jaccard (~0.10) 与 null (~0.039) 有 2.5× 差异（z > 5.0），即使 difficulty-conditioned null 上升，定性结论（overlap 显著超过 chance）可能仍成立
- 但 "conservative" 的论述应被修正

**W6. [Major, 共识] Routing 实用价值有限**

4 个 benchmark：LAMBADA +1.2pp, ARC-Easy +1.2pp, HellaSwag -0.06pp (p=.374), PIQA 显著为负。Abstract 和 Conclusion 对 routing 的提及暗示了比实际支持更广泛的实用性。论文称其为 "illustrative case study"，但 2/4 非正向结果削弱了 illustrative 价值。

**W7. [Major, R2 Critical → R1 REBUT → Director 判定 Major] 增量新颖性受限**

核心信息（aggregate ≠ per-example）已被 Marx et al. (2020)、D'Amour et al. (2022)、Yang & Wang (2026) 建立。R1 rebut 指出实验设计贡献（controlled model zoo、5 比例系统扫描、confidence margin predictor）超越概念复制。Director 判定：概念层面增量有限，但经验贡献在 Findings 标准下有价值。

### Minor/Warning

**W8.** Bootstrap CI 在 n=3 architectures 下仅 27 个可能样本，BCa 校正缺乏理论支撑。Section 3.5 标注为 "heuristic"，但 Table 2 呈现暗示更强可靠性 [R1-W1, R2 AGREE]

**W9.** Related work positioning 不够 sharp——selective prediction (Geifman & El-Yaniv 2017/2019) 和 ensemble selection 的关联未充分讨论 [R2-Major-4, R1 AGREE]

**W10.** Confidence margin AUC 0.69-0.74 被称为 "reliable"，实际属 "moderate"（Hosmer-Lemeshow 标准）；参数化推导（Gaussian intersection）而非实证 ROC，Appendix P skewness 1.33-1.41 违反 Gaussian 假设 [R1-W5, R2 部分同意但降为 minor——非核心 claim]

**W11.** Task taxonomy（retrieval/comprehension/reasoning/mixed）未 pre-register（Appendix A），不同分类可能改变结论 [R1-M1, R2 AGREE 但影响有限]

**W12.** 偶尔使用因果语言（"architecture-driven divergence"），在缺少 seed variation 的观察性研究中不够谨慎 [R1-M2, R2 AGREE]

---

## Reviewer Consensus

| 问题 | R1 | R2 | 最终判定 |
|------|----|----|----------|
| Overall 3.0 (Findings) | ✓ | ✓ | **共识** |
| Spearman n=5 power (W1) | Critical | Critical (交叉升级) | **共识 Critical** |
| Saturation 双解释 (W2) | Agree | Critical | **共识 Critical** |
| GDN confound (W4) | Major | Major | **共识 Major** |
| Permutation anti-conservative (W5) | Major | Agree (最有价值贡献) | **共识 Major** |
| Routing limited (W6) | Minor→Major | Major | **共识 Major** |
| Seed variation limitation (W3) | — | — | **共识为 limitation**（严重程度见分歧） |

---

## Reviewer Divergence

| 问题 | R1 | R2 | Director 判定 |
|------|----|----|---------------|
| **Soundness** | 2.5 | 3.5 | **3.0** — R1 统计分析深入但 ARC-Easy 反证数据有误（被 R2 纠正）；R2 方法学宽容度偏高但纠正了关键数据错误 |
| **Excitement** | 3.0 | 2.5 | **2.5** — 概念层面增量确实有限，R2 判断更准确 |
| **Seed variation 严重程度 (W3)** | Critical（核心反证） | Major（R1 数据有误） | **Major** — R2 纠正了 ARC-Easy 数据（3.5× 差异支持架构效应），但 Pythia 70M 校准外部效度仍有限 |
| **Novelty (W7)** | Major (rebut R2) | Critical | **Major** — Findings 标准下经验贡献有价值 |
| **Binarization** | Major | Minor (Appendix O 回应) | **Minor** — Appendix O continuous-threshold 分析有效回应 |
| **AUC 描述** | Major | Minor (非核心 claim) | **Minor** — 非核心 claim，但 'reliable' 用词应修正 |

---

## Questions

1. 能否对至少 1-2 个 model zoo 配置提供 seed variation 实验？Pythia 70M 不在同一架构族和规模。[R1-Q1, R2 同意价值但注意到可能超出合理范围——model zoo 来自第三方]
2. Table 2 Ratio >1（如 LAMBADA 4.87）的含义应在正文更显眼地解释。[R1-Q2, R2 已解释但同意正文不够清晰]
3. 能否提供 difficulty-conditioned permutation test 作为对照？这能直接验证 W5 的 anti-conservative 关切。[R1-Q3, R2 同意改进方向]
4. 为何不计算实证 ROC AUC 而用参数化推导？Appendix P skewness 1.33-1.41 违反 Gaussian 假设。[R1-Q4, R2 同意]
5. Saturation 的两个竞争性解释能否通过 random-projection attention ablation 区分？[R2, R1 同意]

---

## Missing References

1. **Behzad et al. (2025) FAccT** — multiplicity 在 fairness 语境下的系统研究 [R2 提出, R1 条件性同意：nice-to-have，非 critical]
2. **Selective prediction 文献充分讨论** — Geifman & El-Yaniv (2017/2019) 已被引用但与 routing 的关系未充分讨论 [R2-Major-4, R1 AGREE]
3. ~~Jamba (Lieber et al., 2024)~~ — R1 交叉核实：**已被引用**（Abstract, Section 2, references.bib）。R2 此处有误。
4. ~~Model Soups (Wortsman et al., 2022)~~ — R1 交叉核实：**已被引用**（Section 2, references.bib）。R2 此处有误。

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。**

---

## Visual Layout Check（非评分项）

**状态：已完成**（2026-05-24 22:51–22:54 UTC，耗时 ~3 分钟）

| 严重程度 | 位置 | 发现 |
|----------|------|------|
| ⚠️ Warning | Page 7 | Figure 5 scatter plots 子面板密集，轴标签和数据点文字偏小（~6-7pt），灰度打印时点标记可能难以区分 |
| ⚠️ Warning | Page 6 | Figure 4 两个面板的轴标签和 legend 文字偏小，特别是面板 (a) 的 tick labels |
| ⚠️ Warning | Page 8 | Figure 6 + Figure 7 堆叠占页面 ~55%，下方紧接 Conclusion + Limitations，视觉节奏头重脚轻 |
| ℹ️ Info | Page 1 | 首页无 display item，Figure 1 在 page 2 顶部——可考虑提升至 page 1 底部加速锚定 |
| ℹ️ Info | Page 5 | Figure 3 bar chart 无 pattern fill，灰度打印时 helped/hurt 柱可能不易区分 |
| ℹ️ Info | Pages 13-15 | Appendix Tables 字号 ~7pt，可读性在边界线 |
| ℹ️ Info | Page 21 | 最后一页底部 ~1/3 空白（appendix 末页可接受） |
| ℹ️ Info | Pages 9-10 | References 格式统一，无 [?] 未解析引用，无明显 overfull box |

统计：0 critical, 3 warning, 5 info。无 blocking issue。

---

## Overall Assessment

**Overall: 3.0 / 5 — Findings（可被 Findings 接收）**

| 维度 | 分数 | 说明 |
|------|------|------|
| Soundness | 3.0 | R1: 2.5, R2: 3.5。统计框架诚实但 claim 强度系统性超出证据支撑 |
| Excitement | 2.5 | R1: 3.0, R2: 2.5。核心信息已被先前工作建立，实验贡献是增量的 |
| Confidence | 4.0 | 两位 Reviewer 均有统计方法论和 hybrid recurrent model 专业知识 |

论文提出了有价值的研究问题，核心观察（不同架构在 per-example 层面行为高度不重叠）在方向上可信且对社区有启发价值。实验设计（controlled model zoo、系统化的 attention ratio 扫描）是其主要贡献。

但存在系统性的 **claim-evidence 脱节**：Section 3.5 的统计 caveats 在 Section 4.2 标题、Conclusion 和 Abstract 中被反复违反。Saturation claim 在统计上（n=5 Spearman 无检验力，W1）和解释上（两个竞争性解释未区分，W2）双重薄弱。Permutation test 的 "conservative" 论述方向可能有误（W5）。Routing 的实际表现（2/4 benchmark 非正向）与叙事权重不匹配（W6）。

如果作者能 (a) 将所有基于 n=5 Spearman 的 claim 一致降级为描述性观察，(b) 修正 permutation test 保守性论述，(c) 在 Section 4.2 同等呈现两个竞争性解释，(d) 缩减 routing 在 Abstract/Conclusion 中的叙事权重，本文有潜力在 Findings 标准下稳固。当前 claim 强度系统性超出证据支撑。

---

## Detailed Comments

### Abstract (~154 words)
- 符合 ≤200 word 要求 ✓
- "saturates at just 4% attention" 应改为 "appears to saturate"——与 Section 3.5 caveat 对齐
- Routing 描述占比偏高，考虑到 2/4 benchmark 非正向结果，应缩减或加 qualifier

### Section 1 (Introduction)
- 贡献列表清晰但 saturation contribution 需要 hedging
- "architecture-driven divergence" 在缺少 seed variation 的情况下是因果语言，应改为 associative

### Section 2 (Related Work)
- Yang & Wang (2026) 引用处理得当 [R2 R20 确认]
- 缺少 selective prediction (Geifman & El-Yaniv 2017/2019) 和 ensemble selection 方法与本文 routing 的充分关联讨论
- 与 Marx et al. (2020) 和 D'Amour et al. (2022) 的差异化定位可更 sharp——当前停留在 "我们的设置不同" 而非 "我们能回答什么新问题"
- 考虑添加 Behzad et al. (2025) FAccT

### Section 3 (Methodology)
- Section 3.5 的统计 caveats 是论文的亮点之一
- **Section 3.5 "conservative" 论述需要修正**——permutation test 不条件化 item difficulty 使 null 偏低，检验可能是 anti-conservative
- Bootstrap CI n=3 的 "heuristic" 标注应在 Table 2 中也体现

### Section 4 (Results)
- **Section 4.2 标题 "Saturates" 与 Section 3.5 "descriptive and exploratory" 矛盾**——这是本轮两位 Reviewer 最强的共识
- GDN 排除分析存在但 MMLU ρ 反转应在主文强调（不仅在 Appendix D.2）
- Confidence margin "reliable" → "moderate"
- Routing case study 的消极发现（PIQA 显著为负）应更显著标注
- Saturation 的两个竞争性解释应在 Section 4.2 同等呈现，而非仅在 "leave to future work" 中提及

### Section 5 (Conclusion)
- "saturates at 4% attention and remains flat" 需要 hedging（"appears to"）
- Routing 作为两大观察之一的定位权重偏高——实际只在 LAMBADA 上有效

### Section 7 (Limitations)
- 涵盖了 single training run 和 format confound——这是正面的
- 建议补充：greedy decoding 对生成任务的潜在影响（一句话即可）

### Appendix
- 内容详尽（21 页），体现了作者对潜在问题的充分认识
- **Appendix L（Transformer entrainment）的关键证据应考虑提升至主文**——这是最具新颖性的发现之一，但被埋在附录中
- Appendix O（continuous Jaccard）有效回应了二值化关切
- Appendix W（seed variation）校准局限性应在主文更充分讨论（Pythia 70M 非同族、410M 失败）