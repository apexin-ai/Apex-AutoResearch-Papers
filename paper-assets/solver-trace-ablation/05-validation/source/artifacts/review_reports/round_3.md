---
round: 3
overall_score: borderline accept
timestamp: 2026-05-16T22:55:39.685144+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 3 审稿报告 — Consolidated

**论文**: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"
**目标 venue**: EMNLP 2026 (ARR May cycle, long paper)
**审稿轮次**: Round 3（继续审稿，基于 Round 2 的 15 个 open issues）

---

## Summary

论文做了大幅修订，回应了 Round 2 的审稿意见。核心改进包括：(1) 标题和 framing 从 "Meta-Level Goodhart's Law" 降级为 "empirical instance of Goodhart's Law (regressional variant)"；(2) β 值从 2 个扩展至 4 个，提供完整 dose-response；(3) 新增 Qwen3-1.7B cross-scale 实验，发现 H9 (ex falso) 新模式；(4) ISR 的 premise-count confound 从附录提升至正文 §3.2；(5) LOO vs Shapley 设计选择讨论；(6) 格式问题全部修复（Ethics Statement、Limitations 位置、orphan bib）。

两位 Reviewer 在交叉分享后达成高度共识。R1 修正了两个基于 stale PDF 的误判（cross-scale 实际存在、Abstract "95±5%" 为 1000-step 收敛值）。

---

## Issue Resolution Summary

**Round 2 遗留的 18 个 open issues（含 format）:**
- **RESOLVED**: 15 个
  - R1-W5, R2-W8, v2-R1-N1, v2-R1-N3, v2-R2-N3, v2-R2-N2, v2-R1-W1, v2-R1-W3, v2-R1-W4, v2-R1-W6, v2-R2-W3, v2-R2-W4, v2-R2-W5, v2-FMT-1/2/3, v2-R1-M4, R2-MISSING-REF (降级 info)
- **仍有残留（minor/info）**: 部分 resolved issues 有小的残留问题，已作为 Round 3 新 issues 记录

**Round 3 新发现**: 5 个（均为 minor/info 级别）
- v3-R12-NI-1: Cross-scale 1-seed 限制未在 Limitations 标注 (warning)
- v3-R1-NI-2: β=0.2 未在 Table 1 报告 (info)
- v3-R1-NI-3: §4.2 "collapses to" 叙述缺步数标注 (info)
- v3-R12-NI-4: ~30-40 处 prose em-dash 需清理 (info)
- v3-R2-NI-5: Abstract "zero" vs Table 1 N-H=8% 轻微歧义 (info)

---

## Strengths

1. **实质性实验扩展**：4 个 β 值的 dose-response + Qwen3-1.7B cross-scale 是真正的新数据，而非仅写作修复。发现 H9 (ex falso) 模式证明了 cross-scale 实验的价值。
2. **Framing 大幅改善**：从过度声称 conceptual novelty 转向 honest empirical characterization。"Valid but Vacuous" 标题比原标题更吸引审稿人且更准确。
3. **方法论透明度**：premise-count confound 在正文中坦诚讨论，1.06× 被 frame 为 informative negative result——这种自我批评增加了可信度。
4. **统计报告规范化**：Wilson CI、Fisher exact + OR + 95% CI 的系统使用。
5. **Taxonomy 独立性**：明确论证 taxonomy 不依赖 ISR/STA 即可使用，增强了 C4 的独立贡献价值。

---

## Weaknesses（按严重度排序）

### Major（需修复但非 blocking）

**W1. Cross-scale 实验单 seed 限制未声明**
Qwen3-1.7B 仅 seed 42，但论文核心发现之一正是极端跨 seed 方差。应在 Limitations 明确标注。

### Minor（建议修复）

**W2. β=0.2 报告深度与其在 Introduction 中的定位不匹配**
Introduction 称 β=0.2 为 "maximum exploitation point (0% non-hacking, all seeds)"，但 §4.3 仅 2 行描述，Table 1 不包含该行。要么降低 intro 突出度，要么在 Table 1 加入数据。

**W3. §4.2 cross-seed 描述时间标注缺失**
"s43 collapses to PR=13%" 未标注为 500-step 中间状态。读者（包括 R1）将其理解为最终状态，与 Abstract "95±5%, 3 seeds" 产生表面矛盾。

**W4. Em-dash 过度使用**
~30-40 处 prose em-dash 是 AI 写作痕迹。EMNLP 审稿人可能注意到。建议终稿前做一轮替换。

**W5. Abstract "zero structurally sound outputs"**
严格来说仅对 1000 步成立（500 步 exec-only N-H=8%）。建议改为 "near-zero" 或加 "at convergence"。

---

## Questions for Authors

1. s43 在 500 → 1000 步的 PR 恢复轨迹是什么？从重复坍缩(13% PR)恢复到哪种 hacking mode？建议在正文中明确说明。
2. 1.7B 是否有计划补充更多 seeds？即使作为 future work 标注也好于完全不提。

---

## Missing References

ThinkPRM (Mukhal et al., 2025) 和 VersaPRM (2025) 与 PRM 讨论相关但非必需。当前 31 条引用覆盖核心领域，borderline 可接受。建议补充 2-3 篇提升至 ~34 条。

---

## Overall Assessment

**评分: 3.5/5 (Borderline Accept)**

**R1 最终评分**: 3.5 (Borderline Conference) — 从 3.0 上调，因 cross-scale 实验确实存在且 Abstract PR 矛盾为叙述歧义非数据错误。
**R2 最终评分**: 3.0 (Findings) — 维持原判，但认可修改质量良好。

**Director 综合判断**: 3.5。论文从 Round 2 的 borderline reject 实质性改善至 borderline accept 区间。主要进步在于：实验从 2β → 4β 的完整 dose-response，cross-scale 实验发现新 gaming mode，framing 从过度声称转为诚实的 empirical study。残留问题均为 minor/info 级别的写作优化，不构成 rejection 理由。

**投稿建议**: 修复 5 个 minor issues（特别是 W1 cross-scale limitation 声明 + W3 时间标注 + W4 em-dash 清理）后可提交。这些修复预计 1-2 小时工作量，不需要新实验。

---

## Detailed Action Items（优先级排序）

| 优先级 | Issue | 预计工作量 | 类型 |
|--------|-------|-----------|------|
| P1 | W1: Limitations 加 cross-scale 1-seed 声明 | 5 min | 写作 |
| P1 | W3: §4.2 s43 描述加步数标注 | 5 min | 写作 |
| P2 | W4: 全文 em-dash 清理 | 30 min | 写作 |
| P2 | W5: Abstract "zero" → "near-zero" | 2 min | 写作 |
| P3 | W2: β=0.2 加入 Table 1 或弱化 intro 措辞 | 15 min | 写作 |
| P3 | 补充 2-3 条 PRM 引用 | 15 min | 引用 |
| P3 | bib key 重命名 lundberg-shap-game → shapley-1953 | 2 min | 格式 |
| MUST | 重新编译 PDF 确保反映最新 .tex | 5 min | 格式 |
