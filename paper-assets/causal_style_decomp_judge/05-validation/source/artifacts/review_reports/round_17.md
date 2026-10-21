---
round: 17
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-25T21:41:27.805128+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 19 审稿报告（Fresh Review）

**Venue**: EMNLP 2026 (ARR)  
**Paper**: "The Likert Blindspot: How Pairwise Comparison Reveals Style Sensitivity That Rating Scales Miss"  
**Reviewers**: R1 + R2 | 交叉回应完成 | 收敛达成（12/16 AGREE，4 partial REBUT）

---

## Summary

本文研究 LLM-as-Judge 评估中 Likert 量表与 pairwise comparison 在检测风格敏感性方面的系统性差异（"Likert Blindspot"）。通过单轴风格干预（formality/verbosity）结合 NLI 语义门控，对比 Bradley-Terry 模型和多种 Likert 分析方法的检测力差异。GEE logistic regression 分解风格效应和原文偏好。实验覆盖 4 个 judge（GPT-4o、Qwen3-32B、Llama-70B、Claude Sonnet 4）× 2 轴 × 2 基准（LLMBar + cross-benchmark），辅以 n=355 scaled replication、100-point Likert 变体和人类标注验证。

**核心发现**：Pairwise comparison（BT P=0.63-0.92, p<.05）系统性地检测到风格敏感性，而所有 Likert 变体均失败（7/7 methods NS）。GEE 揭示 verbosity 为 style-dominated（Style OR=8-13）而 formality 为 dual-confounded。Cross-benchmark replication 部分成功（6/24 cells 中 6/6 BT 显著，4/6 Likert NS）。

---

## Strengths

1. **方法学设计精巧** (S1): 单轴干预 + NLI 门控 + direction-aware gating 是一个严密的实验设计流水线。每一步都有 robustness 检查。

2. **统计分析层次丰富** (S2): BT 非参数检测 → GEE 分解 → TOST 等价检验 → FK mediation → 100-point Likert → 人类标注验证。分析工具链的广度和深度在该领域少见。

3. **透明度高** (S3): Cross-benchmark 选择性、shrinkage、overlap inflation 等不利信息均有报告。22 个 Appendix 覆盖几乎所有 robustness 检查。

4. **因果语言审慎** (S4): Appendix A 明确 disclaimer，§3.5 设计理据不过度声称。Related Work 对 RATE 和 Comparative Trap 的定位被两位 Reviewer 评为"准确且诚实"。

5. **Per-axis structure discovery** (S5): Table 2 揭示 verbosity 与 formality 的 confound structure 结构性差异——verbosity 为 style-dominated 而 formality 为 dual-confounded。这是此前文献未报告的发现（R1 强调此为 genuine contribution）。

6. **人类标注验证** (S6): 100-pair annotation（AC₁=0.96, gate pass precision=98.6%）有效回应了早期轮次的 NLI gate 质量 concern。标注者仅在 49-66% 的 NLI-passed pairs 中检测到可辨风格变化，意味着观察到的效应是真实敏感性的稀释下界（R2 独立指出）。

---

## Weaknesses

### Must-Fix (3)

**MF1: Power analysis "prospective" 标签存在循环论证（Post-hoc power fallacy）** [R1 提出, R2 strongly AGREE]

§4.1 使用同一数据集的 observed effect size 计算 power（"confirms that our sample sizes provide >90% power to detect BT effects of the observed magnitude (P≥0.63)"），这正是 Hoenig & Heisey (2001) 批评的 post-hoc power fallacy。Figure 4 caption 的 disclaimer "(not post-hoc power; cf. Hoenig & Heisey, 2001)" 与该引用的核心论点直接矛盾。

- "Likert 需要 4-206× 样本量" 作为 sensitivity analysis 有信息价值
- 但 "prospective" 标签在无独立先验 effect size 来源的情况下不成立
- Figure 4 y-axis "at observed effect magnitudes" 进一步固化 post-hoc 印象

**Action**: 改为 "sensitivity power analysis"；修改 Figure 4 caption 移除自相矛盾的 disclaimer。

**MF2: Cross-benchmark replication 选择性构成确认偏差** [R1 Must-Fix, R2 strongly AGREE]

24 cells 仅填 6 个（25%），论文明确称 "targeting the strongest effects"（§5.3）。这是 cherry-picking 的一种形式：
- 4 个 exception cells (‡) 用 "severity spectrum" 解释，更接近 post-hoc rationalization
- 未测试的 18 cells 可能包含反例（Likert 检测到而 pairwise 未检测到），将直接挑战 "Blindspot" 的单向性叙事
- Contribution 2 的 "first at this scale" 与 25% 覆盖率不匹配

**Action**: (1) 报告全部 24 cells 结果（至少 Appendix）或论证为何反例不可能；(2) Contribution 2 弱化措辞；(3) cross-benchmark 明确标注为 exploratory hypothesis-generating。

**MF3: Claude "negative control" 论证需根本性重新框定** [R1 + R2 交叉共同发现]

- TOST Δ=12pp 时才显著 (p=.035)，Δ=10pp 不显著 (p=.100)，BF₀<3 inconclusive
- 等价边界 Δ=12pp 几乎与最小正效应（GPT-4o formality BT=63.0%=13pp）重合
- **关键新发现**: Claude 在 AEval verbosity 上有 genuine style sensitivity（Style OR=4.76, p<.001）——Claude 并非 universally style-insensitive
- §5.4 TOST 论述仅基于 LLMBar 数据；扩展到 AEval 后 Claude 不满足等价条件
- 整个 discriminative validity 论证需要限定为 benchmark-specific

**Action**: 将 Claude 重定位为 "partial negative control" 或 "benchmark-specific low-sensitivity case"；正文必须讨论 AEval verbosity 的 Style OR=4.76。

### Should-Fix (7)

**SF1: GEE OR shrinkage 49-72% 未在正文突出呈现** [R1 + R2 AGREE]

Table 2 以 n=88 膨胀值为主视觉印象。n=355 scaled replication 显示 49-72% shrinkage（Qwen3-32B formality Style OR: 4.20→2.15）。shrinkage 后仍显著（p<.0001），但 effect magnitude 报告存在误导。GPT-4o formality shrinkage 后 OR≈1.32 可能失去显著性。

**Action**: Table 2 并列报告 n=88 和 n=355 估计值。

**SF2: Evaluator-producer overlap 22% inflation** [R1 + R2 双方独立提出]

GPT-4o 独立 rewriter 使 Style OR 从 13.10 降至 10.17（-22%）。inflation 是 axis-dependent（verbosity 22% > formality 2.1pp）。正文 §5.4 未显著讨论，仅 Table 1 脚注 b 提及。n=355 scaled replication 恰好选用有 overlap 的 Qwen3-32B，不是最 clean 的验证。

**Action**: 正文显著讨论 overlap caveat；建议至少一个 scaled replication 用非 overlap 配置。

**SF3: Verbosity same-style double-rewrite artifact 严重（BT P(orig)=0.082）** [R1 发现, R2 strongly AGREE]

Table 19 (Appendix O): Qwen3 verbosity same-style rewrite 中 judge 在 91.8% 的情况下偏好 LLM-polished 版本。GEE Orig OR=0.49 (n.s.) 方向与 artifact 一致但可能吸收不完全。如果 same-style artifact 幅度远大于 GEE 吸收量，verbosity Style OR=13.10 可能仍包含未控制的 polishing artifact。

**Action**: 定量比较 same-style BT artifact 与 GEE Orig OR 的吸收量。

**SF4: Title "Blindspot" 预设 Likert attenuation 解释** [R2 提出, R1 AGREE]

"Blindspot" 隐含 Likert 有缺陷，与 §5.1 三种非排他解释（attenuation / amplification / construct divergence）不一致。标题引导读者预先接受单一因果方向的印象。

**Action**: 保留标题但 Abstract 更早 qualify（如 "an operational descriptor without committing to a specific causal mechanism"）。

**SF5: §3.1 "per-axis causal attribution" 与 Appendix A disclaimer 语调不一致** [R1 + R2 AGREE]

正文 §3.1 "a single-axis intervention design that enables per-axis causal attribution" 使用了比 Appendix A disclaimer ("not a complete structural causal model") 更强的因果语言。前后不一致让 reviewer 质疑 claim 边界。

**Action**: §3.1 因果语言弱化至与 Appendix A 一致。

**SF6: Novelty positioning——Thurstone (1927) domain transfer vs genuine contribution** [R2 Must-Fix, R1 REBUT severity → 分歧]

R2 认为是 Must-Fix（Excitement 3.0 的主因）：pairwise vs. Likert discriminability 差异是已知心理测量效应的 domain transfer，概念新颖性有限。R1 认为应降级为 Should-Fix：per-axis confound structure 差异（Table 2: verbosity style-dominated vs formality dual-confounded）是此前文献未报告的实质性发现。

**Director 判定**: Should-Fix（偏 R1）。GEE 分解揭示的 per-axis 结构差异确实超出了 Thurstone 一般原理的简单 domain transfer，但论文的 novelty framing 仍需更精确。

**SF7: Measurement-mode divergence 缺少正式检验** [R1 发现, R2 AGREE]

论文分别报告 BT 显著和 Likert 不显著，但未正式检验二者的 effect size 是否 significantly different。Absence of evidence ≠ evidence of absence。n=355 TOST 和 bootstrap attenuation 间接回应，但缺少 measurement-mode interaction test。

**Action**: 添加 bootstrap effect-size difference test 或 measurement-mode interaction test。

### Minor (6)

- **M1**: GEE ρ=−0.25 被称为 "near-zero"——|ρ|>0.1，应改为 "small in magnitude"（robust to correlation structure choice per Table 3）
- **M2**: 缺少 Likert (1932) 原始引用；1-10 整数量表称 "Likert" 严格来说为 interval rating scale
- **M3**: Table 1 "Cat." 列标注（†, †_e, †_c, ---）难以解析，建议更直观标签
- **M4**: Figure 4 y-axis "at observed effect magnitudes" 强化 post-hoc 印象（与 MF1 相关）
- **M5**: Adjusted p-values 在 Table 1 中不可见——仅显示 significance markers，具体数值需查 Appendix
- **M6**: BT 正则化已确认两处均为 α=10⁻⁶（R2 核查 LaTeX 源码），R1 初报的 10⁻⁴ vs 10⁻⁷ 不一致为 PDF 渲染误读 — **已澄清，非问题**

---

## Questions

1. **[Critical]** Power analysis effect size 是否有独立 pilot 或先验来源？如果没有，"prospective" 标签不成立。
2. **[Critical]** 未测试的 18 个 cross-benchmark cells 有结果吗？如果包含反例（Likert 检测到但 BT 未检测到），Blindspot 的单向性叙事如何维持？
3. **[Critical]** Same-style rewrite artifact (BT P=0.082) 中有多少被 GEE Originality term 吸收？Orig OR=0.49 (n.s.) 是 under-powered 还是零效应？
4. **[Important]** Claude AEval verbosity Style OR=4.76 (p<.001) 如何与 "negative control" 定位兼容？§5.4 TOST 是否需要重写？
5. **[Important]** Table 2 能否并列报告 n=88 和 n=355 GEE 估计，以避免小样本膨胀误导？

---

## Missing References

- **Likert, R. (1932)**. A technique for the measurement of attitudes. *Archives of Psychology*. — 论文大量使用 "Likert" 一词但未引用原始文献。
- **Hoenig & Heisey (2001)** — 已引用但用法与该文核心论点矛盾（需修正上下文）。

---

## External Review

未请求外部审稿。

---

## Visual Layout Check

视觉审查 Agent 因 rate limit 崩溃，未产出有效结果。建议下轮重试。

---

## Overall Assessment

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness | 3.5 | 3.5 | **3.5** |
| Excitement | 3.5 | 3.0 | **3.25** |
| Overall | 3.5 | 3.5 | **3.5** |
| Confidence | 4 | 4 | **4** |

**Overall Score: 3.5 (Borderline Conference)**

**判定理由**: 实验设计和统计分析链在该领域属上乘水平（Strengths 1-6），但三个 Must-Fix 问题（power analysis 循环论证、cross-benchmark 选择性、Claude negative control 论证崩塌）构成对论文 claim reliability 的系统性威胁。核心 Blindspot 现象（BT 检测到 Likert 未检测到）在 primary cells 上证据充分，但论文的 framing 和 generalizability claims 超出了当前证据支撑。

**与 EMNLP 标准对标**: 3.5 = Borderline Conference。论文方法学质量满足主会议水平，但 claim 可靠性问题（特别是 MF1-MF3）如不修正，将使 AC 倾向 Findings。如果三个 Must-Fix 全部修正且 SF1-SF3 至少部分回应，论文有望升至 4.0 (Conference)。

---

## Detailed Comments

### 交叉分歧记录

| 问题 | R1 | R2 | Director 判定 |
|------|----|----|---------------|
| Novelty severity | Should-Fix | Must-Fix | Should-Fix（SF6）|
| Cross-benchmark severity | Must-Fix | AGREE Must-Fix | Must-Fix（MF2）|
| Two axes insufficient | Partial REBUT | Should-Fix | Should-Fix——两轴已揭示结构性差异 |
| BT regularization 10⁻⁴ vs 10⁻⁷ | 初报不一致 | REBUT（源码均为 10⁻⁶）| R2 正确，问题不存在 |
| Adjusted p-values method | 未说明 | REBUT（§4.1 已说明）| R2 正确，方法已说明 |

### 跨轮次持续问题（累计 19 轮仍 open/in_progress）

以下问题已在多轮反复出现但始终未完全解决：
- **R2-N1** (Novelty positioning): 第 1 轮至今，19 轮持续。核心张力：domain transfer vs genuine contribution。
- **R15-N1** (Title framing): 第 15 轮至今。"Blindspot" 与三种解释并列的张力。
- **R15-N2** (Claude negative control): 第 15 轮至今。本轮新发现（AEval Style OR=4.76）使问题进一步恶化。
- **R17-W1** (Cross-benchmark selectivity): 第 17 轮至今。本轮升级为 Must-Fix。

### 对作者的建议优先级

1. **立即修正**（阻塞投稿）: MF1 (power label), MF3 (Claude AEval disclosure)
2. **强烈建议修正**（影响评分）: MF2 (cross-benchmark), SF1 (shrinkage), SF2 (overlap), SF7 (interaction test)
3. **改善论文质量**: SF3-SF6, M1-M5
4. **Camera-ready**: AUDIT-H1 (Sobel z/p 错误), AUDIT-D1/D2 (Likert d/p 不一致)