---
round: 4
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-23T12:25:44.173765+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4 (Fresh Review)

**论文**: Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审稿日期**: 2026-05-23
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性；R2: 新颖性+完整性+格式合规）

---

## Summary

本文提出 Gated Many-Facet Rasch Model (G-MFRM)，在标准 MFRM 线性预测器中引入源自 DG-IRT 的乘性 contamination gating 项 c_n · e_i，将模型能力、judge severity 和 contamination susceptibility 纳入统一估计框架。核心 insight 是：分别校正 judge bias 和 benchmark contamination 会引入 omitted variable bias (OVB)，使受污染模型的能力被系统性高估。方法上采用三阶段估计（MFRM warm-start → 外部 exposure 估计 → joint MCMC），并给出 identifiability 充分条件（Theorem 1）和 error propagation 界。在合成数据（N=50 models）上 ability RMSE 降低 51.2%（p<0.001）；在 Arena-Hard 实际数据（8 个目标模型、9 个 judges）上，排名相关性从 τ=0.786 提高到 0.857，但统计不显著（bootstrap Δτ CI 跨零），LOO 交叉验证显示显著的 predictive fit 提升（ΔELPD = −55.7, |Δ/SE| = 5.9）。

---

## Strengths

**S1** [共识] OVB 形式化（§2, Observation 1）优雅且有实质贡献。将 benchmark contamination 遗漏形式化为 MFRM 中的 OVB，严格论证了 sequential estimation（无论先去 bias 还是先去 contamination）都无法解决这一问题。这一 insight 对 LLM evaluation 社区有独立参考价值。

**S2** [共识] 可识别性分析完整正确（Propositions 1-2, Theorem 1）。Appendix A 的证明通过 Fisher information matrix 的 Cauchy-Schwarz 分解和 Schur complement 论证建立了参数可分离的充分条件。这是首次为 gated IRT 模型提供形式化的 identifiability 条件。

**S3** [共识] 结果报告诚实透明——明确承认 Δτ CI 跨零、CI coverage 68-71%、MCMC 未达最严格标准、power 仅 ~50%。这种 intellectual honesty 在学术论文中值得肯定。

**S4** [共识] 合成实验设计周密。覆盖 error propagation (Table 2)、ablation (Table 3)、matched-scale calibration (Appendix P, Δτ_synthetic=+0.072 精确匹配 Δτ_real=+0.071)、power analysis (Appendix M)、CI coverage (Appendix Q)。

**S5** [共识] Appendix 极其全面（16 节补充材料），涵盖完整证明、posterior predictive check、self-evaluation robustness、judge count sensitivity、weight robustness 等。Reviewer 能验证几乎所有 claim。

**S6** [共识] per-model c_n 和 per-judge d_j 提供可操作的诊断信息。Table 8 (Bias Absorption) 中 Δθ 与 c_n 的完美秩相关 (Spearman ρ=1.0) 是 OVB 理论预测的有力实证确认。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1** [共识 — R1 N2 + R2 N2] N=8 下主结果统计不显著，power 严重不足
- Δτ=+0.071 的 bootstrap 95% CI = [−0.071, +0.071]，完全对称跨零。Posterior median τ = 0.786（与 baseline 相同），point estimate 位于分布上尾。
- N=8 下 Kendall τ 最小非零增量恰好为 ~0.071（= 2/C(8,2)），意味着该方法的改善在当前离散分辨率下根本无法被统计检测。
- Power analysis (Appendix M) 确认 N=8 仅有 ~50% power，需 N≥17 for 80% power。
- 论文的核心 claim 之一是 ranking improvement，但唯一的 real-data 评估无法 statistically support 这一 claim。虽然合成实验 (N=50) 显示显著改善，real-data 验证在当前规模下不足。
- **建议**：(a) 扩展到 N≥17 的评测；或 (b) 将 claim 重心从 ranking improvement 转向 contamination diagnostics 和 model fit（ΔELPD）。

**W2** [R1 独有 — R1 N1] c_n 的 95% CI coverage 仅 68-71%，暗示结构性问题
- N=8 时 coverage 67.9%，N=50 时 71%——从 N=8 到 N=50 几乎无改善，说明非小样本问题而是模型结构性缺陷（乘性耦合 c_n·e_i + HalfNormal 边界约束 c_n≥0 系统性压窄 CI）。
- 论文仍在 Table 7 报告具体 c_n 95% CI（如 GPT-3.5-Turbo: [4.40, 6.80]），可能误导读者认为这些区间是校准的。
- **建议**：(a) 在 Table 7 明确标注 "coverage-uncalibrated"；(b) 探索 SBC (Talts et al., 2018) 校正；(c) 讨论 coverage 不随 N 改善是否暗示 model misspecification。

**W3** [R1 独有 — R1 N3] Murphy-Topel 渐近校正在 N=8 下适用性存疑
- Murphy-Topel (1985) 基于大样本渐近理论（经验法则 N≥30），N=8 远低于适用范围。论文将此列为方法论贡献（"neither of which exists for DG-IRT"），但未验证其在 N=8 下是否实际改善 coverage。c_n CI coverage 68-71% 可能部分归因于校正不充分。
- **建议**：报告 coverage with vs without Murphy-Topel 的对比；讨论小样本替代方案（parametric bootstrap）。

**W4** [R2 独有 — R2 N1] Abstract 超过 200 词限制（~209-213 词）
- EMNLP 2026 规定 abstract ≤ 200 words。当前约超出 10-13 词，存在 desk rejection 风险。
- R1 同意超词但建议降为 Should-Fix（5 分钟可修的编辑问题）。Director 判断：格式违规事实确凿，但可快速修复，不反映科学内容缺陷。
- **建议**：删减 LOO 细节或合并 synthetic/real-data 结果描述，压缩至 ≤195 词。

### Should-Fix（影响评分但不一票否决）

**W5** [R2 独有，R1 agree with nuance] Contamination 验证存在循环性风险
- Stage 2 用 reference model anchoring 估计 e_i，Stage 3 用 e_i 估计 c_n。c_n 本质上反映模型在 high-e_i items 上的超常表现——信息已编码在 e_i 里。论文未展示 c_n 提供了超出 e_i 的额外信息。
- R1 补充：验证方式（model age proxy）是 face validity 而非 ground truth 验证。Table 8 的 Δθ-c_n 完美秩相关验证的是 OVB 理论预测而非 contamination ground truth。
- **建议**：设计 out-of-sample 验证；或明确将 c_n 定位为 "differential performance on high-exposure items" 而非"真实污染程度"。

**W6** [共识] 7 个 baseline 产生完全相同排名，对比缺乏信息量
- 所有 7 个 baseline（Raw Average, MFRM-only, Sequential, CyclicJudge, CyclicJudge+discard, DCR Factor, Pref Leakage）产生 τ=0.786, ρ=0.905。Raw ability scores 差异 <0.03 logits，baseline space 完全退化。
- G-MFRM 的比较对象实质上仅为 "raw average"，而非 7 种不同的校准方法。这从侧面说明 OVB 问题在 N=8 下可能 practically irrelevant。

**W7** [共识] LOO-CV (ΔELPD) 与 ranking accuracy 仍存在逻辑分离不足
- 论文已重构为两条独立评估轴（predictive fit vs ranking accuracy），较前版本有改善。但 §4.2 中两者仍在同段落并列讨论，读者可能产生 "model fit improvement → ranking improvement" 的印象。
- ΔELPD_LOO = -55.7 (|Δ/SE| = 5.9) 是论文最强的 real-data evidence，但它衡量的是 held-out response prediction 而非 aggregate ranking accuracy。

**W8** [R1 独有] MCMC 收敛诊断未达 Vehtari 2021 推荐标准
- R̂ ≤ 1.03, ESS_min = 174。未达 Vehtari 2021 的 R̂ < 1.01 / ESS > 400。论文诚实承认但未报告 ESS_tail（HalfNormal 下 tail behavior 对 CI 重要）。
- **建议**：报告 ESS_tail；考虑增加 sampling iterations。

**W9** [R1 独有] Rank-1 contamination 结构假设过强
- c_n · e_i 假设所有模型通过同一 item-level exposure pattern 受污染。未测试假设违反时的行为（graceful degradation vs systematic bias）。Limitations 第 6 点已讨论但无实证支持。
- **建议**：在合成实验中加入 rank-2 misspecification 测试。

**W10** [共识] OVB 线性近似 r=0.86，26% 方差未解释
- Observation 1 依赖线性近似，synthetic validation r=0.86。两位 Reviewer 共识：影响叙事说服力而非方法有效性（G-MFRM 使用完整非线性模型 Eq. 4，不依赖此近似）。但正文应更明确地讨论近似的适用范围和失效条件。

**W11** [R2 独有，R1 agree with nuance] "First joint contamination-severity diagnostic" claim 需更精确
- Li et al. (2024, Preference Leakage) 已识别 judge-specific contamination patterns。"first" 需限定为 measurement-theoretic framework 层面。

**W12** [共识] Stage 2 对 reference model (gpt-4-0314) 的依赖
- 所有 weight sensitivity 测试 (Appendix L) 使用相同 anchor。换用不同 anchor model 的 robustness check 缺失。Limitations 提及但未量化风险。

### Minor

1. [共识] Abstract 中 synthetic (N=50) 和 real-data (N=8) 结果并列，N 不同但未充分区分，可能造成混淆。
2. [R1] 316→176 items 的过滤标准（"filtering for full coverage"）应更详细说明。
3. [R1] Table 7 中 c_n CI 宽度大（如 Qwen3-8B: [0.14, 2.50]），在 coverage 71% 下诊断价值有限。
4. [R1] Qwen2.5-72B 自评 win rate = 1.000 (42/42) 是 judge bias 极端案例，值得正文提及。
5. [R1+R2] Table 2 的 σ 值未与 real-data Stage 2 实际噪声水平对接。论文未报告 real-data 的 Var(e_i) 和 Stage 2 estimated σ。
6. [R2] Related Work (§5) 约半页，部分文献仅一句话覆盖（如 CyclicJudge 方法论差异未展开）。

---

## Reviewer Consensus

[AGREE] **N=8 是核心实证弱点** — 两位 Reviewer 均列为 critical。主排名结果不显著，power 仅 50%，需 N≥17。论文诚实报告了这一局限，但当前规模无法支持 ranking improvement claim。

[AGREE] **OVB 形式化是有价值的 insight** — 即使对不使用 G-MFRM 的研究者也有参考意义。

[AGREE] **结果报告诚实** — 在 LLM evaluation 文献中值得肯定。

[AGREE] **7 个 baseline 同排名** — 比较信息量有限，baseline space 退化。

[AGREE] **LOO vs ranking 需更清晰分离** — ΔELPD 衡量 model fit 而非 ranking accuracy。

---

## Reviewer Divergence

[REBUT] **新颖性判断（R2-N3）** — 这是两位 Reviewer 的核心分歧。

- **R2 立场 (3.0)**：G-MFRM 的模型 specification（Eq. 4）是 MFRM + DG-IRT gating 的直接组合。Binary→continuous 和 single→multi-rater 是自然泛化。Identifiability 条件（connected design、J≥2、exposure variation）直觉上显然。Error propagation 是标准工具应用。增量不足以支撑 main conference。

- **R1 立场 (3.5)**：核心贡献是围绕模型的理论分析体系而非模型本身。(1) OVB 形式化是首次在 LLM-as-a-judge 文献中的严格论证；(2) DG-IRT 无任何 identifiability 分析，Theorem 1 的 Cauchy-Schwarz + Schur complement 证明非平凡；(3) Continuous gating 改善 c_n-RMSE 40% (p<0.001)；(4) Murphy-Topel 在 staged IRT 中的首次应用。"事后看来直觉"和"事前形式化证明"之间有本质差别。

- **Director 判断**：R1 的 REBUT 有说服力——identifiability 分析和 error propagation 框架确实超越了"标准工具的简单应用"，在 gated IRT 文献中没有先例。但 R2 的关注也合理——模型 specification 本身确实是已知组件的组合。综合来看，理论贡献介于 Findings 和 Conference 之间，但实证弱点（N=8 不显著 + CI coverage 结构性问题）是决定性因素，阻止了 Conference 评分。

---

## Questions

1. [R1] Murphy-Topel 校正相对于 naive posterior 提供了多少 coverage 改善？能否报告 coverage with vs without 的对比？
2. [R1] Real data 中 Var(e_i) 的实际值是多少？这决定了 σ_crit 阈值。
3. [R1] 如果将 rank-1 放松为 rank-2（coding/reasoning 两维度），identifiability 条件如何变化？
4. [R1] 7 个 baseline 在更大 N 下（如 ~50 个模型）是否仍然产生相同排名？
5. [R2] 如果完全移除 Qwen2.5-72B 和 LLaMA-3.3-70B 从 judge panel（而非仅排除 self-judging observations），c_n 是否显著变化？
6. [R2] LOO ΔELPD 能否按 per-item 或 per-model 分解，帮助理解 G-MFRM 在哪类 observations 上 fit 更好？
7. [R2] Stage 2 中 gpt-4-0314 作为 anchor 的选择理由？Arena-Hard benchmark 在 2023 年 3 月是否已存在？

---

## Missing References

**R1 提出**：
- Ye et al. (2024), "Benchmarking Benchmark Leakage in Large Language Models"
- Oren et al. (2024), "Proving Test Set Contamination in Black Box Language Models"

**R2 提出**（需验证发表时间）：
- "Evaluating Scoring Bias in LLM-as-a-Judge" (arXiv:2506.22316, June 2025)
- "How to Correctly Report LLM-as-a-Judge Evaluations" (arXiv:2511.21140, November 2025)
- "A Benchmark and Pair-Level 4PL-IRT Framework for Reliable Evaluation of LLM Reasoning" (OpenReview, October 2025)

已确认覆盖的文献清单：CyclicJudge ✓, UDA ✓, Fiedler 2026 ✓, Ye 2024 ✓, Panickssery 2024 ✓, ConStat ✓, DCR ✓, LogProber ✓, Min-K% ✓, Preference Leakage ✓, Jiao 2025 ✓, Uto 2020 ✓, Choi 2026 ✓, PSN-IRT ✓, tinyBenchmarks ✓。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 `external_review.paperreview_ai.enabled`）。

---

## Visual Layout Check（非评分项）

状态：**done**（耗时约 2m40s）

发现（0 critical, 3 warning, 3 info）：

| 严重性 | 位置 | 问题 |
|--------|------|------|
| warning | Page 1-3 | 连续 3 页纯文本无 display item，审稿人前 3 页无视觉锚点。建议将 Figure 2（框架概览）提前至第 2 页 |
| warning | Page 4 | Figure 2（核心框架图）被压缩在单栏宽度内，面积偏小。建议改为 figure*（跨栏全宽） |
| warning | Page 5-6 | 连续 2 页纯文本（Identifiability + Error Propagation + Setup），节奏单调 |
| info | Page 1-8 | 正文 8 页仅 4 个 display items（2 figure + 2 table），密度偏低（0.5/页）。建议将 Appendix 中关键图表提升至正文 |
| info | Page 4 | Figure 1 图例文字和散点标注字号偏小（约正文 60-65%），接近可读下限 |
| info | Page 16 | Appendix 末页约 40% 空白（不影响审稿印象） |

---

## Overall Assessment

**Overall Score: 3.0 / 5 — Findings（可被 Findings 接收）**

**评分理由**：

本文的理论框架（OVB 形式化 + identifiability 证明 + error propagation 分析 + Murphy-Topel 校正）是扎实且有原创性的方法论贡献，将教育测量学的经典工具系统性地适配到 LLM 评测场景。两位 Reviewer 一致认可 OVB insight 的价值、论文的诚实报告态度和全面的补充材料。

然而，三个核心短板限制了 Conference-level impact：

1. **实证不足**（共识 critical）：唯一的 real-data 评估仅 8 个模型，主排名改进不显著（bootstrap CI 跨零），论文自身 power analysis 确认 power 仅 ~50%。7 个 baseline 产生完全相同排名，使对比缺乏信息量。虽然 LOO-CV (ΔELPD = −55.7) 提供了强 predictive fit evidence，但 model fit ≠ ranking accuracy。

2. **CI coverage 结构性问题**（R1 critical）：c_n 95% CI 实际 coverage 仅 68-71%，且从 N=8 到 N=50 几乎无改善，暗示非小样本问题而是模型结构性缺陷。Murphy-Topel 校正在 N=8 下的适用性未得验证。

3. **新颖性争议**（分歧）：R2 认为增量不足（3.0），R1 认为理论分析是独立贡献（3.5）。Director 判断理论贡献真实但非变革性——identifiability 和 error propagation 在 gated IRT 中是新的，但不足以独立承载一篇 Conference paper 在缺乏 significant real-data results 的情况下。

**置信度**: 4/5（两位 Reviewer 均仔细审查了全文 + 16 节 Appendix）

**改进路径**：如果增加 real-data 评估规模至 N≥17 并获得显著 Δτ（论文自身 power analysis 预测可行），同时 address CI coverage 问题（SBC 诊断或替代校正），论文可提升至 3.5-4.0（Borderline Conference 至 Conference）。当前版本适合 Findings。

---

## Detailed Comments

### §1 Introduction (Page 1-2)
- Contribution 1 ("G-MFRM framework with formal identifiability guarantees") 的定位较前版本显著改善——OVB 已重新定位为 motivating observation。
- 但 Introduction 仍给读者留下 ranking improvement 是主要实证贡献的印象。建议在 C3 中更早注入 "at N=8, not statistically significant" 的限定。

### §2 Confounding in LLM Evaluation (Page 2-3)
- Observation 1 的线性近似（r=0.86）应在正文中更明确讨论适用范围。当前脚注过于简短。
- Figure 1 (OVB scatter) 是有说服力的可视化，但缺少残差分析——r=0.86 的 26% unexplained variance 可能含系统性偏差。

### §3 The G-MFRM Framework (Page 3-5)
- §3.1 末段对 DG-IRT 的方法论区分（identifiability + error propagation）较前版本改善。
- §3.2 Stage 2 exposure estimation 的描述缺乏实现细节：reference model anchoring 的具体计算过程（win-rate residuals 的精确公式、difficulty-adjusted expectations 的来源）未给出。
- §3.4 Error propagation 的 σ_crit 推导假设 i.i.d. Gaussian 噪声。脚注承认了假设的局限但未提供 heteroskedastic 情形下的 robustness check。Table 2 定位为 "empirical validation" 但缺少 real-data σ 的对应估计。

### §4 Experiments (Page 5-8)
- §4.1 Setup 清晰，9 个 judges 完整列出。316→176 items 的过滤标准需补充。
- §4.2 重构为两条独立证据线（predictive fit vs ranking accuracy）是重要改善。但建议在段落级别更明确分隔这两个论点（如使用两个 paragraph headers）。
- Table 1 中 7 个 baseline 的 τ/ρ 完全相同。论文解释为 raw scores 差异 <0.03 logits，这是合理的——但也意味着所有现有校正方法在 N=8 下 practically equivalent，侧面削弱了 G-MFRM 改善的实际意义。
- MCMC 收敛报告：R̂ ≤ 1.03, ESS_min = 174。论文诚实承认未达 Vehtari 2021 strict criteria，这是好的。建议补报 ESS_tail。

### §5 Related Work (Page 8)
- 覆盖了主要竞品。Contamination Avoidance 段落已补充。
- CyclicJudge 的方法论差异（round-robin assignment vs statistical modeling）值得展开一句。
- 可能遗漏 2-5 篇 2025-2026 近期相关工作（见 Missing References）。

### §6 Conclusion (Page 8)
- 4 句话，简洁但完整。明确承认 N=8 局限和 N≥20 验证方向。

### Limitations (Page 8-9)
- 6 个 limitation points 覆盖了主要问题：fill rate、anchor validity、N=8 power、CI coverage、self-evaluation、rank-1 假设。
- CI coverage (68-71%) 的讨论过于轻描淡写——仅表述为 "best interpreted as directional diagnostics"，但未讨论 coverage 不随 N 改善的根本原因。
- 代码/数据可用性声明存在。

### Appendix (Page 10-16)
- 16 个 section，覆盖极其全面。Theorem 1 证明（Appendix A）技术正确。Murphy-Topel 推导（Appendix C）完整。
- Power analysis (Appendix M) 作为独立 section 改善了前版本的不足。
- Synthetic calibration at matched scale (Appendix P) 是强有力的补充验证——Δτ_synthetic (+0.072) 精确匹配 Δτ_real (+0.071)。

### 格式合规
- 正文 ≤ 8 页 ✅
- Abstract ≤ 200 words ❌ (~209-213 词)
- ACL style `[review]` ✅
- Double-blind ✅
- Limitations section ✅（位置正确）
- Appendix 双栏 ✅
- 断裂引用 / TBD ✅ 无
- References 格式 ✅