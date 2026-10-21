---
round: 5
overall_score: 3.5 — Weak Accept
timestamp: 2026-05-16T16:24:04.494855+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 5 (Continue Review)

**论文**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains
**Venue**: EMNLP 2026 Main Conference (Long Paper, ARR May cycle, deadline 2026-05-25)
**Reviewers**: R1 (数值一致性/实验完整性审计), R2 (DDR 修订评估/写作一致性)
**交叉回应**: 完成。两位 Reviewer 逐条 [AGREE]/[REBUT]，高度收敛。

---

## Summary

Round 5 评估 8-generator/5-family 扩展后的论文修订。核心修改包括：

- **DDR 三层分类**：从二分法 (drifting/near-stationary) 改为三层 (strong drift/moderate drift/near-stationary)，entropy_std 正确重分类为 "moderate drift"
- **"Partial shape preservation"**：替代 "shape stationarity"，反映 entropy_std 的 moderate drift
- **8-gen 数据迁移**：主实验、Table 1、§4.2、Figure 1 已更新至 8-gen (N=37,058)
- **Table 4 caption 修正**：明确标注 "6-generator subset for controlled comparison"
- **多处写作修订**：downstream "unambiguous"→"directional evidence"、"leading indicators"→"speculatively"、§3.2 共享 seed rationale

**核心结论**: Round 4 的 9 个 open/in_progress 问题中，7 个完全解决，R1-W6 (method novelty) 维持持续分歧，Rd3-SYNC 未处理。R2 的 Round 4 条件性升分触发条件已满足（entropy_std reclassification + Figure 1/text 一致性），双方收敛于 3.5 (Weak Accept)。

然而，8-gen 扩展暴露了系统性的 **editorial sync failure**：至少 6 处 appendix/discussion 仍使用 6-gen 数据但未标注，Discussion 一个段落内出现 rank-order reversal（L15: 0.694>0.690 vs L18: 0.705>0.694），多处 TODO 注释残留。这些问题虽属 editorial 而非 methodological，但数量和分散程度表明投稿前需要完整的 consistency pass。

---

## Round 4 Issues — 修复评估（交叉回应共识）

**Rd3-INT1 [RESOLVED, full consensus]** entropy_std Simpson's paradox / DDR dichotomy
- entropy_std 重分类为 "moderate drift"（pooled |ρ|=0.200, per-gen median |ρ|=0.209）。三层 DDR 分类（strong/moderate/near-stationary）替代二分法。
- R1: 确认阈值对应自然聚类（gap 在 0.200 vs 0.050 和 0.610 vs 0.406）
- R2: 条件性升分触发条件已满足，升至 3.5

**Rd4-W1 [RESOLVED, full consensus]** Figure 1 vs §4.2 数值不一致
- Figure 1 caption 和 §4.2 现在统一使用 pooled Spearman ρ，三层标签一致。Per-gen median 在 §4.2 L74 作为补充报告。

**Rd4-W2 [RESOLVED, full consensus]** Table 4 caption
- Caption 修正为 "Evaluated on the original 6-generator subset for controlled comparison; main results use all 8 generators."

**Rd4-W3 [RESOLVED, full consensus]** "unambiguous" 措辞
- 改为 "The directional evidence is consistent"

**Rd4-M1 [RESOLVED, full consensus]** "leading indicators"
- Discussion L44: "Speculatively, these trends suggest..."

**Rd4-M2 [RESOLVED, full consensus]** §3.2 共享 seed rationale
- §3.2 L21: "We use shared seeds across generators to ensure that cross-generator comparisons control for input content"

**Rd3-M4 [RESOLVED, full consensus]** Figure 1 zone 标签
- Figure 1 改为三层分类标签，pooled correlations 标注在 caption

**Rd3-SYNC [STILL OPEN]** artifacts/ vs docs/ 不同步
- 本轮未处理。

**R1-W6 [PERSISTENT, narrowed]** 方法新颖性
- R1: not an issue (ARR H7)。R2: acknowledged task formulation value，维持 minor concern。分歧缩窄至不影响评分。

---

## Strengths

1. **DDR 三层分类科学合理**: 阈值对应自然聚类（strong: |ρ|>0.6, moderate: 0.20-0.41, near-stationary: <0.05），gap 在层间明显。解决了 Round 3-4 的核心分歧。[R1, R2 一致]

2. **"Partial shape preservation" 全文一致**: 替代 "shape stationarity" 后，abstract、intro、discussion、conclusion 措辞统一，更准确反映 entropy_std moderate drift 的经验事实。[R1, R2 一致]

3. **8-gen 扩展增强 empirical breadth**: 新增 Llama-3.2-3B 和 Mistral-7B 覆盖 5 个 family，性能下降 2.9pp (0.723→0.694) 被诚实报告。7-feature 现在在 binary 上超过 4-det+surface (0.694>0.690)——这是 8-gen 扩展的正面效应，更多 diverse generators 时 interpretable summary statistics 比 multi-detector ensemble 更 robust。[R1, R2 一致]

4. **核心方法论质量保持**: 尽管大规模修订，统计实践（LOGO/LOFO、bootstrap CI、McNemar test、Bonferroni correction）保持一致且正确。[R1, R2 一致]

5. **Round 4 所有 actionable issues 充分解决**: 9 个 open/in_progress 中 7 个 fully resolved，修改精准到位。[R1, R2 一致]

---

## Weaknesses

### 系统性 Editorial Sync Failure（8-gen 迁移不完整）

**Rd5-W1 [warning, consensus — R1:HIGH / R2:minor]** Discussion L15/L18 同段落 rank reversal
- L15: "7-feature ensemble ... edges out the 4-detector+surface ensemble (0.690)" → 7-feature (0.694) > 4-det+surface (0.690)
- L18: "the 4-detector+surface ensemble achieves marginally higher pooled F1 (0.705 vs. 0.694)" → 4-det+surface (0.705) > 7-feature (0.694)
- 同一段落内排名方向反转。Table 3 确认 0.690 正确；0.705 为 stale 数字。
- **R1 诊断**: 论文未定义 "pooled F1" vs "LOGO F1" 区分，Table 3 只报告一种 binary F1，因此 0.705 是 plain error，不是不同 aggregation。Director 采纳此判定。
- **R2 诊断**: 可能是不同 aggregation method，标 minor。
- **修复**: 删除 L18 或将 0.705 改为 0.690，消除 "pooled" 歧义。

**Rd5-W2 [warning, consensus]** LOFO appendix 完全 stale
- LOFO appendix 使用 6-gen 数据（baseline F1=0.789），但论文 8-gen baseline 为 0.762。含 TODO 注释。
- **修复**: 用 8-gen 数据重跑 LOFO，或在 caption 标注 "6-generator subset"。

**Rd5-W3 [warning, R1]** Figure 1 legend 缺 Llama/Mistral
- Caption 声称 "pooled across all eight generators"，但 legend 中 per-gen dots 只有 6 个 generator。
- **修复**: 补全 8 个 generator 的 data points 或标注 "6-generator subset"。

**Rd5-W4 [warning, consensus]** Dataset statistics appendix stale
- 仍显示 6-gen 总计 27,529，应为 37,058。
- **修复**: 用 8-gen 数据更新。

**Rd5-W5 [warning, R2 discovered / R1 confirmed]** QLoRA 实验使用 6-gen baseline 未标注
- Discussion L49: "QLoRA fine-tuning raises 3-class F1 to 0.905 (+11.6pp over XGBoost)"
- 算术验证: 0.789 + 0.116 = 0.905 ✓ (6-gen baseline)；0.762 + 0.116 = 0.878 ≠ 0.905 (8-gen)
- 确认 QLoRA 实验未在 8-gen 上重跑，但正文未标注。
- **修复**: 标注 "(evaluated on the 6-generator subset; XGBoost 3-class F1=0.789)" 或用 8-gen 重跑。

**Rd5-W6 [warning, consensus]** TODO 注释残留
- 至少 5 处: results.tex L53, method.tex L79, appendix_lofo L1, appendix_qlora L4, appendix_human_edit L1
- **修复**: 删除所有 TODO 注释。

### Minor — 不影响接收

- **Rd5-M1 [info]**: Instruct base 值 stale（Discussion L61: 0.764→应为 0.781, 0.816→0.780；Limitations L7 同样）
- **Rd5-M2 [info]**: Cross-model chain 数字 (0.809/0.764) 未标注 6-gen 还是 8-gen（Results L23 / Conclusion）
- **Rd5-M3 [info, optional]**: Mistral-7B 最低 binary F1 (0.633) 可能与 sliding-window attention + GQA 有关，Discussion 可加 1 句

---

## Questions for Authors

1. Discussion L18 的 0.705 来源是什么？如果是不同 aggregation method，需要定义 "pooled F1" 并在 Table 3 报告。如果是同一 metric 的 stale 数字，需要更正。
2. 哪些 appendix 实验已用 8-gen 数据重跑？请提供 8-gen vs 6-gen 实验的完整 mapping。
3. Cross-model chain 实验 (F1=0.809/0.764) 是在 8-gen 还是 6-gen 上运行的？

---

## Missing References

无新增遗漏。R1 建议 Mistral 架构引用（sliding-window attention），optional。

---

## Overall Assessment

**Overall Score: 3.5 — Weak Accept**

**R1**: 3.5 (Weak Accept, 维持) — conditional 3.75 if 5 specific editorial issues fixed
- Soundness 4.0/5, Excitement 3.5/5, Confidence 4/5

**R2**: 3.5 (Weak Accept, 升自 Round 4 的 3.0) — conditional: appendix fixes must be completed, otherwise drops to 3.0
- DDR 三层分类 + Figure 1/text 一致性满足 Round 4 升分条件

### 评分依据

**为什么 3.5 (Weak Accept)**:
- Round 4 条件性升分路径实现：entropy_std reclassification + Figure 1/text 一致性两个条件均已达成
- DDR 三层分类是科学上的改进，不仅是 editorial fix
- 8-gen/5-family 扩展增强了 empirical breadth，覆盖多样架构和规模
- 核心方法论质量在 5 轮审稿中保持稳定
- Task formulation + DDR empirical characterization 的贡献定位清晰
- 7-feature 现在在 binary 上超过 4-det+surface (0.694>0.690)

**为什么不是 ≥4.0 (Accept)**:
- 系统性 editorial sync failure：8-gen 迁移只完成了核心实验，至少 6 处 appendix/discussion 仍使用 6-gen 数据
- Discussion L18 同段落 rank reversal 暴露 QA 流程不足
- 方法新颖性持续分歧（虽缩窄但未消除）
- 性能水平 moderate (binary F1=0.694)，practical utility 有限（document-level 36% 误分率）

**为什么不是 ≤3.0 (Reject/Findings)**:
- 所有 methodological issues 从 Rounds 1-4 已解决
- Task formulation 新颖且有价值（第一个 non-paraphrastic ordinal depth estimation）
- 实验设计（LOGO/LOFO/binary primary metric）严谨
- 统计实践超出平均水平（Bonferroni, bootstrap CI, McNemar, length confound control）
- 负面结果诚实报告，Limitations 全面

### Conditional paths

**R1 条件性升分 (3.5→3.75)**: 修复以下 5 项：(1) Discussion L18 数字, (2) LOFO appendix, (3) Figure 1 legend, (4) dataset stats appendix, (5) TODO 注释

**R2 条件性保持 (3.5, otherwise →3.0)**: 修复 TODO 注释/appendix (Rd5-W2/W4/W5/W6) + Discussion L18 (Rd5-W1)

### 修订进度总结

| Round | Score | Critical | Warning | 主要变化 |
|-------|-------|----------|---------|---------|
| 1     | 3.5   | 5        | 4       | 初审 |
| 2     | 3.0   | 4        | 6       | gen-0 leakage、instruct gap |
| 3     | 3.0   | 3        | 4       | framing 脱节、downstream、binary |
| 4     | 3.25  | 0        | 4       | Critical 全解决，条件性路径 |
| 5     | 3.5   | 0        | 6       | 条件达成，editorial sync failure |

### 交叉回应收敛总结

| Issue | R1 | R2 | Consensus |
|-------|----|----|-----------|
| Rd3-INT1 entropy_std | RESOLVED (三层) | RESOLVED (升分触发) | Full |
| Rd4-W1 Fig1/text | RESOLVED | RESOLVED | Full |
| Rd4-W2 Table 4 | RESOLVED | RESOLVED | Full |
| Rd4-W3 "unambiguous" | RESOLVED | RESOLVED | Full |
| Resolution count (7/9 vs 8/8) | 差异系 tracking 范围不同 | — | Full (无实质分歧) |
| Rd5-W1 Discussion L18 | HIGH severity (rank reversal) | Minor (possible diff aggregation) | Partial — both agree fix needed |
| Rd5-W2 LOFO stale | Flag | Flag | Full |
| Rd5-W3 Figure 1 legend | Flag | — | Full |
| Rd5-W5 QLoRA stale | Confirmed (算术验证) | Original finder | Full |
| D1 method novelty | Not an issue (ARR H7) | Minor concern | Persistent narrowed |

### 对作者的 Action Items（按优先级排序）

**Priority 1 — 投稿前必须修复（阻塞性）**:
1. **Discussion L18**: 删除 0.705 或改为 0.690，消除同段落 rank reversal
2. **LOFO appendix**: 用 8-gen 重跑或标注 "6-generator subset"
3. **Figure 1 legend**: 补全 8 个 generator 的 per-gen dots
4. **Dataset stats appendix**: 用 8-gen 数据更新
5. **TODO 注释全部删除**: results.tex L53, method.tex L79, + appendix files
6. **QLoRA numbers**: 标注 6-gen subset 来源或重跑

**Priority 2 — Camera-ready 修复（推荐）**:
7. Instruct base 值更新 (0.764→0.781, 0.816→0.780)
8. Cross-model chain 标注 6/8-gen 来源
9. Mistral-7B 架构说明 (1 句, optional)

**Priority 3 — Rebuttal 准备**:
10. 方法新颖性：ARR H7 + first systematic DDR three-tier characterization + partial shape preservation hypothesis 在 model collapse 文献中无 prior documentation

**置信度: 4/5** — 两位 Reviewer 独立评审 + 交叉回应完成，高度收敛。Editorial issues 明确且可修复，不涉及 methodological 重新设计。