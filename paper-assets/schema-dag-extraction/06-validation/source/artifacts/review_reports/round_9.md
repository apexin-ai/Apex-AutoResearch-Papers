---
round: 9
overall_score: weak reject
timestamp: 2026-05-16T17:59:04.937767+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# 审稿报告：Round 9
**论文**: "Does Type Confusability Shape Schema-Induced Degradation in Training-Free LLM Information Extraction?"
**目标 venue**: EMNLP 2026 Main Conference (ACL Rolling Review)
**审稿人**: Reviewer 1 (方法严谨性, 3.0/5) + Reviewer 2 (新颖性与完整性, 3.0/5) + Reviewer 3 (格式合规性, Pass w/ Minor Issues)
**外部审稿**: Stanford Agentic Reviewer — skipped

---

## Summary

本文研究 training-free LLM IE 中 schema complexity 导致的性能下降，通过 stratified experimental design 分离 type count 和 type confusability。提出 Schema Confusability Score (SCS, pairwise embedding cosine similarity) 和 Batch Confusability Score (BCS)，在 4 个数据集 (Few-NERD, FewRel, DocRED, MAVEN) 和 2 个模型 (Qwen3-32B, Llama-3.1-8B) 上实验。主要发现：count-driven recall decline 主导 (最大 -49pp)，confusability-driven type substitution 典型效应约 2.2pp (CI [0.4, 4.0])；TOST 检验在 full-range regression 下支持 RE 中 additive separability (p=0.003)；NER schema decomposition 因 merge amplification 失败 (F1 0.445→0.251)；confusability-aware grouping 在 RE 上无显著优势 (+1.4pp, p≈0.19, rank 13/15 random seeds)。

---

## Strengths

1. **精心设计的 stratified 实验框架** — count curves + BCS-controlled experiments 首次在 zero-shot IE 中通过正交设计分离 count 和 confusability。Within-pool analysis + permutation test (p=0.60) 控制了 pool composition confound。[三位 Reviewer 一致认可]

2. **坦诚报告负面结果** — SDGD 在 NER 上全面失败、confusability-aware grouping null result、pairwise R² 极小——均未回避。Merge amplification 机制的系统诊断有直接领域指导意义。[R1 引 ARR H6: 负面结果具有科学价值]

3. **系统性 sensitivity analyses** — prompt version (v1/v2)、embedding choice (Qwen3/MiniLM)、BCS aggregation (mean/max)、cross-model validation、TOST margin sensitivity (±1/2/3/5pp)、SCS name-only vs name+definition ablation。统计方法远超 NLP 论文平均水平。

4. **MAVEN centrality confound 分析** (§4.5) — per-type BCS-F1 正相关（与预期方向相反）的识别及 partial correlation 控制后效应消失，是 genuinely novel methodological insight。[R1/R2 共识为论文最 non-trivial 的发现之一]

5. **格式与可复现性** — 正文精确 8 页、ACL [review] 模板、double-blind 完整无泄露；模型/推理参数/prompt templates/硬件/bootstrap CI 参数齐备；53 条引用 0 hallucinated。[R3 确认]

---

## Weaknesses — Must-Fix (影响接收决定)

### W1 [Critical | R1+R2+R3 三人共识] TOST "additive separability" 声称过强

TOST margin ±3pp 用 prompt variation (~25pp) 锚定不合逻辑（不同变异来源），且 margin > typical confusability main effect (2.2pp)。Sensitivity analysis: ±2pp borderline (p=0.047)，±1pp 失败 (p=0.278)。三个 separability 检验中仅 full-range regression TOST (n=69) 通过；2×2 factorial (p=0.56) 和 Few-NERD factorial (p=0.50) 均未达 equivalence。"Cleanly separable" 措辞与证据不匹配。

**要求**: (1) SESOI 重新论证——锚定于 typical effect 的 practitioner-relevant fraction（引用 Lakens 2017），不再用 prompt variation; (2) 弱化为 "interaction bounded below ~2pp under full-range regression; lower-powered factorial designs did not confirm equivalence"; (3) 承认 ±1pp inconclusive 的含义——interaction 可能达 main effect 一半大小。

### W2 [Critical | R1+R2+R3 三人共识] Abstract/Intro extreme vs typical framing 失衡

Typical-batch gap 仅 2.2pp (CI [0.4, 4.0])，但 Introduction 未出现此数字；extreme-batch 31.2pp 和 "up to 53% variance explained"（单一 DocRED 条件）占据显著篇幅。Full 80-relation condition 下自然 BCS 变异不足以检测效应 (IQR=0.033, p=0.76)，直接削弱 "pre-hoc screening tool" 建议。

**要求**: (1) Abstract/Intro 以 typical 2.2pp + quartile 5.3pp 为主锚; (2) extreme 31.2pp 标注为 "under maximum BCS contrast (methodological upper bound)"; (3) Discussion 增加: natural BCS IQR=0.033 下 screening 实际决策价值有限; (4) "up to 53%" → 报告 range "22-53%"。

### W3 [Critical | R1+R2+R3 三人共识] Pair-to-batch R² 聚合 conditioning issue

Unconditional r²=1.3-1.7% 输入 simulation → batch R²≈0.01-0.04，远低于 observed 0.218。Conditional R²=7.4%（non-zero confusion pairs）才 match，但 conditioning on dependent variable 有上偏。如需先知哪些 pairs "active" 才获有意义 R²，SCS pre-hoc predictive value 受限。R2 qualification: batch R²=0.218 是直接观测（不依赖 simulation），simulation 是 explanatory model 非 evidence base。

**要求**: (1) Appendix I 标注为 illustrative explanatory model; (2) main text 以 observed batch R²=0.218 作为 primary empirical fact，不以 simulation match 论证 aggregation mechanism; (3) Discussion 讨论 pre-hoc value 的前提条件（BCS 在什么 IQR 范围内有用）。

### W4 [Critical | R1+R2 共识, R3 不评判] Two-channel conceptual contribution 有限

"Count 多了 recall 下降" + "相似 types 容易混淆" 高度直觉化（Deng 2010, Guo 2021, Zhou 2025 已在其他领域展示）。Core finding "count >> confusability" (2.2pp vs -49pp) 主要 confirmatory。Non-trivial elements（量级差异 ~20×, merge amplification, centrality confound, NER coupling）未被充分凸显。

**要求**: 重新组织 contributions，将 surprising/non-obvious findings 提升为核心卖点；考虑提交 Findings track 或重新定位核心故事。

### W5 [Critical | R1 partial agree, R2 critical, R3 agree] Contribution #4 decomposition framing

NER F1 0.445→0.251 (灾难性失败)、RE +1.4pp p≈0.19 (null result)、oracle +29.8pp (不可部署)。R1 认为 merge amplification mechanistic explanation 构成有效贡献 (ARR H6)；R2/R3 认为 "contribution" framing 仍偏正面。

**要求**: 措辞具体化为 "Merge amplification as structural barrier to NER decomposition; null confusability-aware advantage (+1.4pp, n.s.) despite oracle ceiling (+29.8pp)"。确保不暗示 positive practical outcome。

---

## Weaknesses — Should-Fix (影响评分)

1. **Single-seed / 5 batches per count level** [R1 critical → R2 rebut → Director: warning] — 跨 4 数据集 directional consistency 提供 robustness (R2 论点有力)，但 Figure 1a 缺 error bars 是 presentation gap，5 batches 统计功效有限。**要求**: Figure 1a 添加 ±1SD error bars；明确 count curve 为 trend visualization，magnitude claims 基于 BCS-controlled (n=25-100)。

2. **FewRel contamination 风险** [R1+R2+R3 agree] — train+val 合并；train-origin -8.8pp (p=0.06) borderline；non-uniform contamination 未排除。**建议**: val-only 16-relation sensitivity check 或 split-origin covariate。

3. **NER text matching 混淆 boundary/type errors** [R1+R2 agree] — exact match 下 boundary errors 计入 recall decline 但可能与 confusability 无关。**建议**: relaxed match sensitivity analysis 或 error taxonomy 增加 boundary 类别。

4. **SCS 与 LLM-PEE 形式等价** [R2 critical, R1 rebut → Director: warning] — Contribution #2 易误读为 metric novelty。R1 认为 empirical validation + centrality confound 识别是新贡献，wording 可解决。**要求**: 改为 "Empirical validation that pairwise SCS predicts type confusion (r=0.112-0.129), with centrality confound identified"。

5. **Few-NERD shared-representation bias** [R1 warning, R2 rebut] — extraction model 自身 embedding 计算 SCS；MiniLM cross-check 方向一致 (r=0.172 > 0.138, conservative)。**建议**: Limitations 增加 bias 讨论。

6. **Cross-model: Channel 2 在 8B NER 失败** [R1+R2 agree] — 当前仅 cross-ref Limitations。**要求**: §4.3 main text 明确提及。

7. **"First controlled study" 声称** [R2 should-fix, R1 rebut → Director: should-fix] — 加 "To our knowledge" 是低成本改进。

8. **AI assistant 披露** [R3 W1, R1 agree] — Checklist A4 需具体说明系统名称 (ARR 要求)。

9. **缺少匿名代码链接** [R3 W2, R1 agree] — 提交前补充 Anonymous GitHub。

---

## Questions for Authors

1. TOST margin 若设为 typical effect 的 50% (±1.1pp)，equivalence 是否成立？如不成立，additive separability claim 如何解读？
2. FewRel 仅用 val-split 16 relations 时，BCS-controlled effects 是否仍显著？
3. Natural BCS IQR=0.033 下，pre-hoc screening 的具体 decision boundary 是什么？如何 actionably 指导 schema design？
4. Oracle routing 在 realistic setting 中（如 LLM-based routing）是否有 pilot 结果？
5. Greedy decoding bitwise reproducibility 是否在 vLLM FP8 下经过验证？

---

## Missing References

§2 已补充 hierarchical classification 文献 (Deng 2010, Zhou 2025, Guo 2021, Novack 2023, ZERONER 2025)。引用覆盖当前可接受。需核实 camera-ready: `sclar-sensitivity-2024` bib title 截断；`gliner2-2025`, `json-schema-bench-2025`, `li2023evaluating` OpenAlex 未精确匹配（非 hallucinated，为索引延迟）。

---

## External Review (Stanford Agentic Reviewer)

状态：**skipped**（用户未在规定时间内提交至 paperreview.ai）。

---

## Overall Assessment

**Score: Weak Reject (borderline → Findings accept)**
**推荐**: EMNLP 2026 **Findings** track

### 理由

**支持接收的因素**:
- Stratified experimental design 方法论本身是对领域的贡献
- Merge amplification 的系统诊断直接影响后续 decompose-then-merge 工作
- Centrality confound 识别是 genuinely novel methodological insight
- 统计方法规范、sensitivity analyses 全面、负面结果诚实报告
- 格式合规、可复现性优秀

**反对 Main Conference 的因素**:
- Core conceptual contribution (two-channel decomposition) 主要 confirmatory，直觉可预期
- Channel 2 typical effect 仅 2.2pp (CI 下界 0.4pp)，practical value 在 natural BCS variation 下不可检测 (p=0.76)
- No actionable intervention: NER decomposition 失败，RE confusability-aware grouping n.s.
- Statistical inference gaps: TOST margin > main effect, conditioning bias, incomplete factorial confirmation
- SCS metric 与 LLM-PEE 形式等价，novelty 来自 evidence 而非 method

**Findings 接收的充分条件**:
- 修正 Must-Fix W1-W5 中的 framing/措辞问题（无需新实验）
- 格式 minor issues (AI disclosure, anon code link)
- 论文在 intellectual rigor、experimental coverage、honest reporting 上已达 publication quality

---

## Reviewer Consensus Matrix

| Issue | R1 | R2 | R3 | Consensus |
|-------|----|----|-----|-----------|
| TOST separability overclaim | Must-Fix | Must-Fix | Agree | ✓ 三人共识 |
| Extreme vs typical framing | Should-Fix | Should-Fix | Agree | ✓ 三人共识 |
| Pair-to-batch conditioning | Must-Fix | Should-Fix (w/ qualification) | Agree (w/ caveat) | ✓ 共识 |
| Findings-level novelty | Agree (3.0) | Must-Fix (2.5 excitement) | Not judging | ✓ R1+R2 共识 |
| Contribution #4 framing | Rebut (ARR H6) | Must-Fix | Agree | Partial → Must-Fix wording |
| Single-seed | Must-Fix | Rebut (should-fix) | Agree w/ nuance | 分歧 → Should-Fix |
| SCS novelty | Rebut (wording) | Must-Fix | N/A | 分歧 → Should-Fix |
| AI disclosure | Agree | N/A | Must-Fix | ✓ R1+R3 共识 |
| Format/anonymity | N/A | N/A | Pass | ✓ |

**置信度**: 4/5 — 三位 Reviewer 在核心判断 (Findings-level, typical effect 过小, separability overclaim) 上高度一致；分歧仅在严重性分级而非方向性。