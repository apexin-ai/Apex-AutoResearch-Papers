---
round: 4
overall_score: 3.0 — Findings
timestamp: 2026-05-18T01:51:41.226461+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 5 Consolidated Review Report

**论文**: "Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study"
**Venue**: EMNLP 2026 via ACL Rolling Review (Findings track)
**Deadline**: 2026-05-25
**Reviewers**: R1（方法严谨性 + 实验有效性）, R2（新颖性 + 完整性 + 写作质量）
**Cross-sharing**: 完成，所有关键问题已达成共识

---

## Summary

本文提出 ContamCal，一个两阶段框架：Stage 1 用 Reciprocal Rank Fusion 融合多个 contamination detection signals 生成连续 exposure scores；Stage 2 将其嵌入 contamination-augmented 2PL IRT 模型（2PL+γ）进行校准。在 Qwen2.5 (0.5B-3B) 的 LoRA SFT injection 实验中得到核心 null finding：aggregate contamination effect 仅 ~0.6-0.7pp，raw accuracy 已是最优估计。论文将框架价值重新定位为 diagnostic（domain-level γ 异质性分析），附带 Min-K%++ 在 0.5B 的 directional reversal 发现和 γ recovery 的 identifiability boundary 分析（J≥50 at AUC≥0.55）。

---

## Strengths

**S1. Null finding 的负责任报告 [R1, R2 共识]**
在 publication bias 严重的领域中，坦诚报告 ContamCal 未能超越 raw accuracy 是值得肯定的。Table 3 系统性展示了所有 7 个 baseline 的比较，DCR 的 systematic overcorrection (MAE 0.108-0.314) 为社区提供了有价值的负面证据。

**S2. 统计方法论超出 NLP 论文典型水平 [R1, R2 共识]**
Bayesian inference via NUTS + proper convergence diagnostics (split-R̂ < 1.01, bulk ESS > 400)、oracle ablation (ground-truth binary labels)、prior sensitivity analysis (区分 prior-dominated vs data-dominated conclusions)、simulation study for identifiability boundaries。

**S3. Min-K%++ directional reversal 有实用价值 [R1, R2 共识]**
Cohen's d = -1.55 to -1.98 at 0.5B 是此前未报告的 failure mode。对 contamination detection 实践有直接指导意义（practitioners 不应在 small-scale SFT models 上使用 Min-K%++）。

**S4. Identifiability boundary analysis 提供 actionable guidelines [R1, R2 共识]**
J≥50 at AUC≥0.55 的定量条件为未来 IRT-based LLM evaluation research 建立了操作标准，当前实践 (J=8-30) 远低于此阈值。

**S5. RRF vs S1-only ablation 揭示了 IRT 应用的实践洞察 [R1]**
S1-only item selection 导致 exposure variance compression ([0.749, 0.867]) 和 MCMC non-convergence (R̂=1.53, ESS=7)，证明了 multi-signal fusion 对 IRT parameter separability 的必要性。

**S6. 写作质量整体良好 [R2]**
无 em-dash，无显著 AI 写作痕迹。Calibration disambiguation paragraph 是好的预防性澄清。Limitations 覆盖 9 条，坦诚充分。

---

## Weaknesses — Must-Fix（影响接收决定）

**W1. [critical] 页面超限 [R2 提出, R1 AGREE]**
Tables 2/3 (Results 核心内容) 浮动到 page 9 顶部，Discussion/Conclusion 尾部延续到 page 9，Limitations 约在 page 9 的 60% 才开始。主要内容约 8.5 页，超出 ACL Long paper ≤8 页正文限制。存在 desk-reject 风险。
- 修改方向：(1) 移 ARC IRT 结果到 Appendix（同时解决 W3）; (2) 压缩 §5.1 RRF ablation 段落 (~15 行→3-4 行 + Appendix pointer); (3) 考虑 Table 2 (domain γ) 移入 Appendix 或 Table 3 inline 化。

**W2. [critical] 叙事不一致：method paper vs empirical investigation [R2 提出, R1 AGREE]**
- Introduction ¶1-3 重度 motivate "post-hoc calibration is essential"，建立 calibration 方法改进的期待
- Results 发现 raw accuracy 最好，framework 的核心 pitch 被自己的实验推翻
- Contributions 1-3 分属 empirical finding / engineering observation / exploratory analysis，缺乏统一主线
- "Why not just use raw accuracy?" 段落在论证自己论文不必要
- Subtitle "An IRT Decomposition Study" 与 method paper framing 矛盾
- 修改方向：从 ¶1 即以 question-driven empirical investigation 切入；ContamCal 定位为 investigative instrument 而非最终产品；Contributions 精简为 2 条。

**W3. [critical] ARC PPP=0.003 下结果与 MMLU 并列呈现 [R1 提出, R2 AGREE]**
PPP=0.003 在所有 J 配置 (8/13/16) 下持续，表明 2PL+γ 对 ARC 的结构性 misfit。Table 3 中 ARC IRT 与 MMLU 并列给读者同等可靠的印象。Caption caveat 容易被忽略。
- 修改方向：ARC IRT 移入 Appendix（保留 raw accuracy）；讨论 misfit 原因（item pool 更小 1172 vs 14042、difficulty distribution homogeneity）。

**W4. [critical] SFT injection 生态效度限制核心 claim 适用范围 [R1 提出, R2 AGREE]**
标题暗示通用结论，但证据仅覆盖 LoRA SFT injection at ≤3B。Pretraining contamination 机制根本不同（distributed exposure across millions of steps, representation-level embedding, no instruction formatting artifact）。Schaeffer et al. (2026) 显示 pretraining contamination 可能产生更大效应。R2 补充：pretraining contamination 可能 embed into θ rather than capturable by γ（§5.5 θ asymmetry 已暗示此点）。
- 修改方向：标题加限定（"Does SFT-Injected Benchmark Contamination Need Calibration?"）或 Abstract 首句即 scope 为 SFT injection。

**W5. [critical] Social Sciences γ=-0.57 未经多重比较校正 [R1 提出, R2 AGREE]**
8 个 MMLU domain 独立检验，仅 Social Sciences 达 P(γ<0)=99.1%。Bonferroni 阈值 P≥99.375%，不通过。Abstract 直接报告此数字未标注 multiplicity。R2 nuance：独立 per-domain fits 无 shrinkage，Gelman 2012 的 Bayesian 免校正论证需要 hierarchical model。
- 修改方向：(a) Abstract 中加 "uncorrected for multiplicity"；(b) 报告 Bonferroni-adjusted 结论；(c) 最优方案：改用 hierarchical IRT (per-domain γ_k from shared hyperprior)，自然实现 shrinkage + multiplicity adjustment。

**W6. [critical] 技术新颖性有限 [R2 提出, R1 AGREE]**
2PL+γ 是 standard explanatory IRT/DIF 的直接应用。论文自己承认 "formally an instance of explanatory DIF"。与 Han et al. EACL 2026 差异仅在 continuous vs binary exposure + domain stratification，是 modeling 变体而非 paradigm shift。论文的 oracle ablation 用 binary labels 也得到 non-significant γ，说明 continuous vs binary 区别在此设置下无实质影响。
- 修改方向：明确定位为 empirical investigation，不 claim 方法创新。

---

## Weaknesses — Should-Fix（影响评分但不一票否决）

**W7. [warning] Oracle ablation 的 model-free vs model-dependent 结论未区分 [R1 提出, R2 partial REBUT → 收敛]**
R2 partial rebut 有实质贡献：aggregate 0.6-0.7pp 是 model-free observation（直接 d000 vs d005/d025/d100 accuracy 差异），不依赖 γ specification。但 γ diagnostic claims（Social Sciences P(γ<0)=99.1%, domain-level heterogeneity）依赖 additive linear specification。论文应在 Abstract/Results 中区分：model-free findings 保持原有表述，model-dependent findings 加 specification caveat。
- 注：R2 补充：aggregate negligibility 可能掩盖 item-level distortions，§5.4 opposing domain signs 正是证据。

**W8. [warning] Abstract 数字密度过高 [R2 提出, R1 AGREE]**
~202 words 含 8-9 个具体数值（~12 quantitative info points），读起来像 Results 压缩版。应保留 2-3 个关键数字（aggregate effect, identifiability threshold），其余改为定性描述。

**W9. [warning] J 值跨分析不一致 [R1 提出, R2 AGREE]**
Domain-level analysis（最有趣的 finding）使用 J=13（统计功效最低的配置），而 pooled baselines 用 J=16。原因是实验时间线，但后续完整数据未用于重新验证 domain findings。Appendix C 中 J=16 prior sensitivity 确认 Social Sciences 方向，但主文 Table 2 仍报告 J=13。

**W10. [warning] Cross-family "Validation" 标题误导 [R1 提出, R2 AGREE]**
§5.5 标题 "Cross-Family Validation" vs 实际内容 J=4 single-seed + Llama d100 MMLU excluded。与论文自己的 "exploratory" 标注矛盾。Llama catastrophic format collapse 暗示 cross-architecture SFT injection 机制根本不同。

**W11. [warning] RRF 的贡献是 exposure variance 而非 signal quality [R1 提出, R2 AGREE（"R1 最独到的观察"）]**
Ablation 证据仅支持 RRF 对 exposure variance diversification 的贡献。S1 AUC > 0.95 远超 RRF composite。§5.1 总结句 "not only signal quality aggregation but exposure variance" 暗示两者都有证据支持，但实际只有后者有实验验证。

**W12. [warning] "Diagnostic value" 叙事说服力不足 [R2 提出, R1 AGREE]**
8 domains 中 1 个 significant（uncorrected）、J=13 被论文自己标为 exploratory（需 J≥50）、family-specific 不跨架构推广。作为 Contribution 3 的支撑证据链不够强。

**W13. [warning] Han et al. EACL 2026 差异化不足 [R2 提出, R1 partial REBUT → 收敛]**
R1 nuance：实际差异比 R2 描述的更大（目标不同：detection vs calibration；continuous vs group-based DIF；counterfactual inference），但论文仅用一句话区分。应扩展为 3-4 句话，在 Method §2.1 讨论为什么 continuous exposure 在 LLM 场景下更合适。

**W14. [warning] CI coverage 不对称且解释不足 [R1 提出, R2 AGREE]**
MMLU 50% CI covers 83%（over-coverage = uninformative intervals），ARC 50% CI covers 45%（under-coverage = overconfident）。MMLU 95% CI covers 100% = 完全无信息。Over-coverage 和 under-coverage 根源不同，应分开讨论。

**W15. [warning] Min-K%++ directional reversal 可能是 SFT artifact [R1 提出, R2 partial REBUT → 收敛]**
R2 认为论文已 qualify（post-hoc hypothesis + alternative explanations），但两者都同意 Conclusion claim "Min-K%++ should not be trusted at the 0.5B scale" 应限定为 "under SFT injection"。

**W16. [warning] Missing references: IRT classics + LLM evaluation [R2 提出, R1 AGREE 全部 4 条]**
缺少 Lord (1980), Hambleton et al. (1991) 作为 IRT 基础文献；缺少 HELM (Liang et al. 2023) 作为 LLM evaluation 代表性工作；缺少 Magar & Schwartz (2022) 作为 contamination 早期文献。

**W17. [info] -ing 分词短语散见 [R2 提出, R1 AGREE（影响极低）]**
method.tex 中 "adapting...", "avoiding...", "making it applicable..." 等处，密度不高但存在。

---

## Reviewer Consensus

两位 Reviewer 在以下所有关键问题上达成一致（[AGREE]）：

1. **Overall 3.0 (Findings)**：方法框架有参考价值，null finding 对社区有信息量，但证据强度和影响力不足以支撑主会议。
2. **SFT 生态效度**：核心限制。标题/Abstract 需更明确 scope。
3. **ARC PPP<0.05**：IRT 结果不应与 MMLU 并列呈现。
4. **多重比较**：Social Sciences 在 Bonferroni 校正下不通过，Abstract 未标注。
5. **页面超限**：~8.5 页，desk-reject 风险。
6. **叙事不一致**：method paper vs empirical investigation framing 混淆。
7. **技术新颖性**：2PL+γ 是 standard explanatory IRT/DIF 应用。
8. **Cross-family 标题**："Validation" 对 J=4 数据过强。
9. **RRF variance vs quality**：ablation 仅支持 variance 贡献。
10. **Abstract 数字密度**：需进一步精简。

---

## Reviewer Divergence

所有分歧已在交叉回应中收敛为具体修改建议，无遗留矛盾：

| 问题 | 分歧 | 收敛结论 |
|------|------|---------|
| Oracle/misspecification (R1-N1) | R2 partial REBUT: aggregate 0.6-0.7pp 是 model-free | 共识：区分 model-free findings 和 model-dependent findings，分层限定 |
| Min-K++ causal (R1-W4) | R2 partial REBUT: 论文已 qualify | 共识：post-hoc 标注足够，但 Conclusion claim 需加 "under SFT injection" |
| Han et al. (R2-W5) | R1 partial REBUT: 实际差异更大 | 共识：差异确实存在但论文应展开为 3-4 句话 |

---

## Questions for Authors

1. **Domain γ at J=16**: 是否可以在 J=16 配置下重跑 domain-level γ 分析以确认 Social Sciences finding？
2. **Non-linear γ specification**: 是否尝试过 threshold model (γ·𝟙[e>τ]) 或 interaction terms (γ×a_i) 来区分 genuine null 和 misspecification？
3. **RRF composite AUC**: RRF 融合后的 overall AUC 与 S1-only AUC 的直接对比是什么？S1 + uniform noise 是否也能达到类似的 exposure variance？
4. **Hierarchical IRT**: 是否考虑过 hierarchical model (per-domain γ_k from shared hyperprior) 来同时解决 multiplicity 和 independent fitting 问题？
5. **Han et al. 实验对比**: Han et al. EACL 2026 在类似设置下的结论是什么？continuous vs binary exposure 的差异是否在可比条件下产生不同结果？
6. **Code/data release**: Stan 代码、SFT 训练脚本和实验数据是否计划开源？

---

## Missing References

| 参考文献 | 理由 | R1/R2 一致性 |
|----------|------|-------------|
| Lord (1980) "Applications of IRT to Practical Testing Problems" | IRT 奠基性教科书，使用 2PL 的论文应引 | 两者 AGREE |
| Hambleton, Swaminathan & Rogers (1991) "Fundamentals of IRT" | IRT 标准参考 | 两者 AGREE |
| Liang et al. (2023) HELM | LLM evaluation 代表性框架 | 两者 AGREE |
| Magar & Schwartz (2022) "Data Contamination: From Memorization to Exploitation" | Contamination 早期系统研究 | 两者 AGREE |

另需核实：holland_1993_dif (OpenAlex 返回 year=2009, author=Osterlind)、deboeck_2004_explanatory_irt (OpenAlex 返回 year=2005) 的元数据准确性。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置中未找到 external_review.paperreview_ai.enabled 设置）。

---

## Overall Assessment

**3.0 — Findings（可被 Findings 接收）**

**置信度**: 4/5（两位 Reviewer 均有 IRT + LLM evaluation 领域背景，核心判断高度一致）

**评分理由**:

论文提出了一个合理的框架（将 detection signals 嵌入 IRT 进行 contamination calibration），实验设计在受控条件下严谨，null finding 的报告诚实透明。附带贡献（Min-K%++ reversal, identifiability boundaries）对社区有实用价值。

但以下根本限制将论文定位于 Findings 而非主会议：

1. **SFT ecological validity**: 核心 null finding 仅在 SFT injection ≤3B 下成立。Pretraining contamination 机制完全不同，可能产生更大效应。论文回答的是 "SFT injection 需要校准吗？" 而非标题所问的 "LLM benchmark contamination 需要校准吗？"

2. **Technical novelty**: 2PL+γ 是 standard explanatory IRT/DIF，不是方法创新。与 Han et al. EACL 2026 的差异化不足。贡献在 empirical 层面，但 empirical 范围又被 SFT/≤3B 严格限定。

3. **Evidence strength**: 三个贡献中，C1 (null finding) 受 SFT proxy 限制，C3 (domain diagnosis) 受 multiple comparison + J=13 underpowered 限制。C2 (signal failure modes) 是最 solid 的但属于 empirical observation。

4. **Narrative**: 仍在 method paper 和 empirical investigation 之间摇摆。Introduction 建立 calibration 期待，Results 推翻之，造成读者期待落差。

5. **Format**: 页面超限 (~8.5 页) 需立即修复。

**与 Findings 接收标准的匹配度**:
- ✅ 有用的实证知识（null finding 有信息量）
- ✅ 方法论有参考价值（identifiability analysis, signal failure modes）
- ✅ 统计规范高于领域平均
- ❌ 影响力受限于 SFT/≤3B 条件
- ❌ 不提供新方法或新 insight beyond "calibration is unnecessary at small scale"

**修复后评分可能提升至 3.5 (Borderline Conference) 的条件**:
(a) 页面超限修复 + 叙事统一为 empirical investigation；
(b) 添加 hierarchical IRT 结果解决 multiplicity；
(c) 增加 1-2 个 naturally contaminated model（如利用 GSM1K parallel test set）提升生态效度。
其中 (a) 在 deadline 前可完成，(b)(c) 可能需要更多时间。

---

## Detailed Comments by Section

### Abstract
- 数字密度过高（~12 quantitative info points in 202 words）。保留 aggregate effect + identifiability threshold，其余改为定性。
- P(γ<0)=99.1% 需标注 "uncorrected for multiplicity" 或删除。
- "raw accuracy is already well-calibrated" 是 model-free finding，可保持；γ-related claims 加 specification caveat。

### Introduction
- ¶1-3 过度 motivate calibration 方法的需求，与 Results 中 null finding 形成期待落差。
- ¶3 "No existing method bridges..." 需考虑 Han et al. EACL 2026 是否已部分 bridge。
- Contribution list 建议精简为 2 条，统一为 question-driven framing。

### Related Work
- 48 citations 量级合理，但缺少 IRT classics (Lord 1980, Hambleton 1991) 和 LLM evaluation framework (HELM)。
- Han et al. 差异化仅 1 句话，需扩展为 3-4 句话讨论 goal-level 和 mechanism-level 差异。
- Calibration disambiguation paragraph 是优秀的写法。

### Method
- 符号 k 在 §3.1 (benchmark index) 和 Eq.2 (domain/stratum index) 之间复用，需注明。
- RRF 的 meta-circularity avoidance justification 写得好。
- 2PL+γ additive structure 的 linear assumption 应在此处（而非仅 Limitations）讨论 potential misspecification。

### Experimental Setup
- SFT injection 设计严谨（controlled dosage, multiple seeds, quality-control filter）。
- 0.5B 排除逻辑合理（position bias）。
- Cross-family analysis 标题需从 "Validation" 改为 "Exploratory Analysis"。
- B1b/B5b 的 "b" 后缀未解释。

### Results
- RRF ablation 段落可大幅压缩（核心 message 是 S1-only 导致 variance compression → MCMC failure）。
- Table 3 ARC 列应移至 Appendix 或标注不可靠。
- "Diagnostic value of γ" 段需明确区分 model-free vs model-dependent conclusions。

### Discussion and Conclusion
- "Why not just use raw accuracy?" 是好问题但 framing 不理想——应从 ¶1 开始就设置为 "the answer may be no"。
- "Min-K%++ should not be trusted at the 0.5B scale" 需加 "under SFT injection"。
- 可增加：在什么条件下 ContamCal 会优于 raw accuracy（larger models, pretraining contamination, better signals）。

### Limitations
- 9 条，覆盖面广，诚实。
- "Additive γ linearity" 讨论应在 Method 中也出现，不仅在 Limitations。
- CI coverage 的 over/under-coverage 根源应分开讨论（MMLU: posterior θ uncertainty; ARC: structural misfit）。

### Ethics Statement
- 过于简短（4 句）。应补充 dual-use risk 讨论。

### Appendix
- Prior sensitivity analysis 严谨。
- Model set composition table 有价值。
- 建议将 ARC IRT 详细结果、RRF ablation 技术细节移入此处以释放正文空间。

---

**Issue Tracker 状态**: Round 5 新增 4 个 issue (R5-N1 page limit, R5-W1 symbol overload, R5-W2 ethics brevity, R5-W3 B1b label)，更新 15 个已有 issue 的 last_seen_round 和 mentions。6 个 critical issue 仍为 in_progress (R2-N1 framing, R2-W6 SFT validity, R3-W10 γ misspecification, R4-N1 multiplicity, R3-N3 ARC PPP, R5-N1 page limit)。1 个新 critical issue (R5-N1 page limit) + R3-N7 novelty (warning but fundamental)。