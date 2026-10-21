---
round: 4
overall_score: borderline (Findings upper range / Weak Accept lower range, 3.25)
timestamp: 2026-05-16T05:42:58.255290+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 审稿报告 — Round 4 (Continue Review, Final)

**论文**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains
**Venue**: EMNLP 2026 Main Conference (Long Paper, ARR May cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法严谨性/实验/统计), R2 (新颖性/相关工作/写作/格式)
**交叉回应**: 完成。两位 Reviewer 逐条 [AGREE]/[REBUT]，大部分判定收敛。

---

## Summary

Round 4 是对 Round 3 审稿意见修改后的修订评估。论文进行了大幅修改：

- **Abstract/Introduction 完全重写**：以 base-model recursive generation 科学研究为框架，web contamination 降为背景
- **贡献从 3 条减至 2 条**：下游实验从贡献列表移除，降级为补充分析
- **Table 1 增加 Binary F1 列**：作为主指标，附 gen-0 overlap caveat
- **Discussion 从 ~4 段扩展到 ~11 段**：含形状稳态假说、检测器集成对比、prompt 类型依赖、语料级效用、model collapse 关系等

**核心结论**: Round 3 全部三个 Critical issue 已完全解决（交叉回应共识）。R1 升至 3.5（Weak Accept），R2 维持 3.0（Findings upper range）。分歧集中在：(1) entropy_std 的 "near-stationary" 分类依赖 aggregation 选择（Rd3-INT1 + Rd4-W1），R2 认为动摇 DDR 二分法可靠性；(2) 方法新颖性（R1-W6），R1 引用 ARR H7 反驳，R2 降级为 Should-Fix。R2 给出**条件性升分路径**：如 Figure 1/text 数值不匹配和 entropy_std aggregation 问题得到 substantive clarification，可 3.0→3.5。

---

## Round 3 Critical Issues — 修复评估（交叉回应共识）

**N1 [RESOLVED, full consensus]** Base-model-only 与 web-scale framing 脱节
- Abstract 开篇改为 "Recursive application of language models"，web contamination 降为 Intro 背景（3 句）。Base-model 作为 "deliberate design choice" 前置（Intro para 2），instruct confounds 作为 justification。
- **交叉回应**: R1 AGREE, R2 AGREE。双方一致认为 framing 重写质量高。

**N2 [RESOLVED, full consensus]** 下游实验 underpowered 且被列为 Contribution #3
- 贡献从 3 条减至 2 条。正文 §4.4 压缩至 4 行 + Appendix reference。Appendix 补充了 sign-flip test (p=0.25)、Cohen's d=34.8、cross-seed variance <0.001。
- **交叉回应**: R1 AGREE, R2 AGREE（w/ qualification："unambiguous" 措辞需改，见 Rd4-W3）。

**N3 [RESOLVED, full consensus]** Gen-0 共享种子导致 3-class LOGO 虚高
- Table 1 增加 Binary F1 列，Caption 标注 binary 为主指标 + gen-0 overlap caveat。
- **交叉回应**: R1 AGREE, R2 AGREE。R1 补充：§3.2 应加 1 句解释共享 seed 的 design rationale（input-controlled comparison）。Minor gap。

---

## Strengths

1. **Framing 重写质量高**: "Deliberate design choice" framing 有效化解了 scope limitation 质疑。逻辑链清晰：web contamination 背景 → base-model 设计选择 → instruct confounds 论证 → 贡献声明。[R1, R2 一致]

2. **Discussion 大幅扩展且质量高**: ~11 段覆盖 mechanistic hypothesis、detector ensemble comparison、prompt-type dependence、corpus-level vs document-level utility、model collapse relation、paraphrastic chains、instruct tuning、negative downstream finding。R1 评价 "scholarly responsiveness"。[R1, R2 一致]

3. **Round 3 所有 Critical 完全解决**: 交叉回应在所有三个 Critical 上达成完全共识。修改幅度大但质量稳定。[R1, R2 一致]

4. **任务定义新颖性强化**: Contribution 精简后更聚焦（task formulation + empirical characterization），避免了过度声称。[R1, R2 一致]

5. **统计实践和透明度提升**: Binary F1 作为主指标、下游实验正确降级、所有表格标注评估协议。负面结果诚实报告。[R1, R2 一致]

---

## Weaknesses

### Divergence — Reviewer 分歧

**D1 [R1: not an issue / R2: should-fix]** 方法新颖性
- **R1 交叉回应 REBUT**: (1) ARR H7 明确适用（"Do not penalize a method for being simple"）；(2) Discussion "Comparison with detector ensembles" 诚实承认 performance parity，贡献重新定位为 task formulation + interpretability + simplicity；(3) "DDR 是已知现象的重新描述" 在修订后更难成立——Discussion "Shape stationarity" 给出的 mechanistic account（softmax + sampling → shape, context shift → central tendency）在 model collapse 文献中无 prior documentation；(4) 用 method novelty 标准评价 task-formulation paper 是类别错误。
- **R2 交叉回应**: 降级为 Should-Fix（从 Round 3 Critical），承认 task formulation 有独立价值，但维持 EMNLP main 通常期望更深的方法贡献。
- **Director 判定**: 分歧缩窄为 "acknowledged characteristic vs minor concern"。R1 的 ARR H7 论证有力。作为 Findings paper 不构成任何障碍；作为 Main Conference 可通过 rebuttal 论证。

### Warning — Should-Fix（交叉回应后共识）

**Rd4-W1 + Rd3-INT1 [warning, consensus — 本轮最重要联合发现]** Figure 1/text 数值不匹配 + entropy_std aggregation 问题
- **问题**: Figure 1（strip plot）显示 per-generator median Spearman ρ，§4.2 正文报告 pooled correlation。5 个特征均有差异（hapax: -0.647 vs -0.558）。entropy_std 上差异最显著：per-gen median ρ=-0.200 vs pooled |ρ|=0.076。
- **影响**: R2 在交叉回应中称此为"本轮最重要发现"——per-gen median ρ=-0.200 是 "质的差异"，不仅是 presentation 问题，而是动摇 DDR 二分法（drifting vs near-stationary）的可靠性。"Near-stationary" 分类依赖 aggregation 选择。
- **R2 建议措辞**: "near-stationary in aggregate (pooled |ρ| = 0.076), though individual generators show weak-to-moderate negative correlations (per-generator median ρ = -0.200)"。
- **R1 交叉回应 AGREE**: 需加 caveat，但认为 camera-ready 可修。
- **R2 条件性升分**: 如此问题得到 substantive clarification（报告两种 ρ + 讨论 aggregation），R2 可从 3.0 升至 3.5。
- **建议**: (a) Figure 1 caption 明确标注 "per-generator median"；(b) §4.2 报告两种 ρ 并讨论 aggregation 影响；(c) 修改 "near-stationary" 为 qualified statement（per-gen median suggests weak drift that is attenuated by cross-generator pooling）。

**Rd4-W2 [warning, consensus]** Table 4 caption "6-gen LOGO" 但数据来自 5-gen 实验
- Table 4 Pythia-410M F1=0.803 ≈ Table 1 5-gen 值 0.802，非 6-gen 0.789。交叉回应双方 AGREE。
- **建议**: 用 6-gen 数据重跑 Table 4，或修正 caption 为 "5-gen LOGO (excl. Qwen3-8B)"。

**Rd4-W3 [warning, consensus]** Appendix downstream "unambiguous" 与 p=0.25 矛盾
- **R1 交叉回应 AGREE**: 确认是真实矛盾。"unambiguous" 暗示强统计证据，但 p=0.25 + "severely underpowered" 暗示证据不足。论文实际想说的是 direction 一致（3/3 seeds），而非统计显著。
- **R1 建议措辞**: "The directional pattern is consistent across all seeds: data quantity outperforms depth-aware curation, though the comparison is underpowered (p=0.25, n=3)"。
- **建议**: 替换 "The results are unambiguous" 为 "The directional evidence is consistent" 或 "All three seeds show the same ordering"。

### Minor — 不影响接收

- **Rd4-M1**: "leading indicators" 推测性声明。交叉回应共识 AGREE，加 "speculatively" 即可。
- **Rd4-M2**: §3.2 缺少共享 seed 的 design rationale。R1 建议加 1 句："We use shared seeds to ensure that cross-generator comparisons control for input content."
- **Rd3-SYNC**: artifacts/ 与 docs/ 文件不同步。提交前需修复。
- **Rd3-M4 zone 标签**: Figure 1 zone 标签准确性待修复（H_min 归类问题）。

---

## Questions for Authors

1. Figure 1 显示的度量（per-generator median ρ）与 §4.2 正文（pooled ρ）不同。能否统一报告，或在 caption/text 中明确区分并讨论 aggregation 影响？
2. entropy_std per-gen median ρ=-0.200 vs pooled |ρ|=0.076——这一 aggregation 差异是否影响 "near-stationary" 分类的可靠性？
3. Table 4 是在几个 generator 的 LOGO 下运行的？0.803 ≈ 5-gen 0.802 而非 6-gen 0.789。
4. Appendix downstream "The results are unambiguous" 是否应改为与 p=0.25 一致的措辞？

---

## Missing References

无新增遗漏。Round 3 识别的所有遗漏已补入。

---

## Overall Assessment

**Overall Score: 3.25 — Borderline (Findings acceptance upper range / Weak Accept lower range)**

**R1**: 3.5 (Weak Accept, 升自 3.0) — Soundness 4.0/5, Excitement 3.5/5, Confidence 4/5
**R2**: 3.0 (Findings upper range, 维持) — Soundness 3.5/5, Excitement 3.0/5 (升自 2.5), Confidence 4/5

**条件性收敛路径**: R2 明确表示，如 Rd4-W1 + Rd3-INT1（Figure 1/text 数值不匹配 + entropy_std aggregation）得到 substantive clarification，可升至 3.5。此时双方收敛于 3.5 (Weak Accept)。

### 评分依据

**为什么升至 3.25（从 Round 3 的 3.0）**:
- Round 3 全部三个 Critical issue 完全解决，交叉回应确认无遗留争议
- Framing 重写从根本上修正了 claims-evidence mismatch
- Discussion 大幅扩展，理论深度和诚实度显著提升
- 方法新颖性分歧从 Critical/Should-Fix 缩窄为 acknowledged/Should-Fix
- R2 Excitement 升至 3.0（从 2.5）

**为什么不是 ≥3.5 (Accept)**:
- entropy_std aggregation 问题（Rd3-INT1 + Rd4-W1）是论文 Contribution #2（DDR empirical characterization）的核心可靠性问题。per-gen median ρ=-0.200 vs pooled |ρ|=0.076 不是 rounding 差异，而是分类标签是否成立的问题。在此问题 clarified 前，3.5 需要条件达成。
- 修订过程引入了新的 inconsistency（Table 4 caption、"unambiguous" 措辞），虽都可修但反映校对不够仔细
- 方法新颖性分歧虽缩窄但未消除

**为什么不是 ≤2.5 (Reject)**:
- 所有根本性缺陷已修复，论文基本功扎实
- Task formulation 新颖性得到两位 Reviewer 一致认可
- 实验方法论质量超出平均水平
- 负面结果诚实报告，Limitations 覆盖全面

### 对作者的 Action Items（按优先级排序）

**Priority 1 — 阻塞性修复（可触发 R2 升分至 3.5）**:
1. **§4.2 + Figure 1 caption**: 报告两种 Spearman ρ（pooled + per-generator median），讨论 aggregation 影响。修改 entropy_std 的 "near-stationary" 为 qualified statement。采用 R2 建议措辞："near-stationary in aggregate (pooled |ρ| = 0.076), though individual generators show weak-to-moderate negative correlations (per-generator median ρ = -0.200)"。

**Priority 2 — Camera-ready 修复**:
2. Table 4：用 6-gen 数据重跑或修正 caption
3. "unambiguous" 替换为 "directionally consistent"
4. "leading indicators" 加 "speculatively"
5. §3.2 加共享 seed rationale（1 句话）
6. artifacts/ 与 docs/ 同步

**Priority 3 — Rebuttal 准备**:
7. 方法新颖性：ARR H7 simplicity + first systematic empirical characterization + drift/stationary decomposition 文献空白 + Discussion mechanistic hypothesis 作为理论贡献

### 修订进度总结

| Round | Score | Critical | 主要变化 |
|-------|-------|----------|---------|
| 1     | 3.5   | 5        | 初审 |
| 2     | 3.0   | 4        | 新发现 gen-0 leakage、instruct gap |
| 3     | 3.0   | 3        | framing 脱节、downstream、binary 呈现 |
| 4     | 3.25  | 0        | 所有 Critical 解决。新发现 4 Warning。条件性收敛路径至 3.5。 |

### 交叉回应收敛总结

| Issue | R1 | R2 | Consensus |
|-------|----|----|-----------|
| N1 framing | RESOLVED | RESOLVED | Full |
| N2 downstream | RESOLVED | RESOLVED (w/ Rd4-W3 caveat) | Full |
| N3 gen-0 | RESOLVED | RESOLVED (w/ Rd4-M2 minor) | Full |
| D1 method novelty | Not an issue (ARR H7) | Should-Fix | Narrowed |
| Rd4-W1 Fig1/text mismatch | Warning, fixable | **本轮最重要发现** | Full |
| Rd3-INT1 entropy_std | Needs caveat | Challenges DDR dichotomy | Full |
| Rd4-W2 Table 4 caption | Warning | Warning | Full |
| Rd4-W3 "unambiguous" | AGREE real contradiction | Original finder | Full |
| Rd4-M1 "leading indicators" | Minor | AGREE minor | Full |

**置信度: 4/5** — 两位 Reviewer 均完成独立评审和交叉回应，对 15+ 具体判定逐条 AGREE/REBUT。