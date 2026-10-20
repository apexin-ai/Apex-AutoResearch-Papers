---
round: 16
review_mode: continue
overall_score: 4.0 - Conference
timestamp: 2026-05-22T17:38:20.024664+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 16 (Continue Review)

**Paper**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法严谨性), R2 (新颖性与完整性)
**Review Mode**: Continue from R15 fresh review
**Previous Score**: 3.5 (Borderline Conference) → **Current: 4.0 (Conference)**

---

## Summary

R16 修订全面回应了 R15 审稿的 3 个 Must-Fix 和 7 个 Should-Fix/Warning 问题。两位 Reviewer 独立验证后一致将评分从 3.5 提升至 4.0。核心因果发现（C1: +34 pp, OR=15.1）的方法论强度不变，claims 的精准化消除了之前的主要障碍。

---

## R15 Issues 修复验证汇总

### Must-Fix — 全部 RESOLVED ✅

| Issue ID | 问题 | 修复方式 | R1 | R2 |
|----------|------|----------|----|----|
| R15F-N1 | "intervention-design framework" overclaim | 全文 → "diagnostic taxonomy for failure-mechanism prediction" | ✅ RESOLVED | ✅ RESOLVED |
| R15F-N2 | Cross-judge ρ=0.09 mid-tier judge-dependency | §5.2 新增独立段落限定 C2 为 "robust extremes" | ✅ RESOLVED | ✅ RESOLVED |
| R15F-N3 | Incompleteness confound-free range 主文缺失 | §5.1 添加 confound-controlled range (+18.7 to +36.0pp) | ✅ RESOLVED | ✅ RESOLVED |

### Should-Fix/Warning — 全部 RESOLVED ✅

| Issue ID | 问题 | 修复方式 | 验证 |
|----------|------|----------|------|
| R15F-W1 | 标题 "All" overclaim | 标题删除 "All" | ✅ (Intro 残留一处 "all" — minor) |
| R15F-W2 | "30×" MI ratio 缺绝对值 | Intro 添加 I=0.41 bits vs 0.014 bits | ✅ |
| R15F-W3 | C2-C4 framing bridge 缺失 | §5.1 末尾 bridge sentence | ✅ |
| R15F-W4 | 错误分析循环性 caveat | Limitations 添加人工验证建议 | ✅ |
| R15F-W5 | 遗漏 5 篇参考文献 | 5 篇全部添加至 Related Work | ✅ |
| R16-Q1 | Type III SS 安全措辞 | §5.1 脚注引用 logistic pseudo-R²=0.175 | ✅ |
| R16-Q2 | 方差分解 residual 完整报告 | §5.1: 22.4+15.8+1.0+60.8=100% | ✅ |

---

## Remaining Issues（均为 minor/info，不影响接收）

1. **R16-Q5 [info, STILL_OPEN]**: Appendix B 提供了 4 个 prompt 文本（generic, auth scope, lexical, incompleteness），但 Table 4 报告 5 种类型的结果。**Conditional precedence 和 scopal 的 prompt 文本缺失**。建议补充或说明使用了 generic prompt。

2. **R15F-W1 residual [info]**: Introduction 残留 "all policy ambiguity is nocuous"，与已修改的标题轻微不一致。Camera-ready 可统一为 "policy ambiguity is consistently nocuous" 或 "all six types of policy ambiguity are nocuous"。

3. **R10-M6 [info]**: Method §4 连续 2-3 页纯文本无 display item。R1 降级为非关注项（整体论文的视觉密度可接受）。Visual check 仍标为 warning。

4. **R15F-M1 [info]**: Conclusion 仍主要镜像 Abstract 核心数字。在 2 句 Conclusion 的长度下难以避免。

5. **排版 [info]**: Page 7 三个 display items 堆积（Table 2 + Figure 2 + Figure 3），Figure 2/3 被压缩。可通过前移 Table 2 或后移 Figure 3 改善。

---

## Strengths（延续 R15 评价）

**S1. 严谨的 matched-pair 因果框架** — Perturbation control Δ = −0.67 pp (CI 含零) 有效隔离语义歧义因果效应。

**S2. 全面的统计工具箱** — McNemar / TOST / Fisher / Type III SS / bootstrap / MI，每个工具与用途匹配。7 档 margin sensitivity 和主动的 margin dependence 披露透明度突出。

**S3. 诚实的方差分解** — Type 0.4% vs clause 22.4% 的反直觉发现被积极利用重新定位 taxonomy。

**S4. Claim calibration 精准（R16 新增强项）** — 修订后 claims 与证据严格匹配：C1/C2 primary, C3 inconclusive, C4 exploratory。"Diagnostic taxonomy" 定位诚实且可辩护。Contribution (2) 降级后说服力反而增强。

**S5. 完整的方差分解报告（R16 新增）** — clause 22.4%, condition 15.8%, model 1.0%, type 0.4%, residual 60.8%，附来源说明。

---

## Weaknesses（仅残留 minor）

无 Must-Fix 或 Should-Fix 残留。

**Minor residuals**:
- 2 个 prompt 文本缺失（Appendix B reproducibility gap）
- Intro "all" 残留
- Method 段视觉密度
- Conclusion 与 Abstract 重复

---

## Questions（R16 新增/残留）

**Q1 [minor]**: Appendix B Table 4 的 cond. prec. 和 scopal 结果使用了 type-specific prompt 还是 generic prompt？prompt 文本缺失影响可复现性。

---

## Missing References

R15 识别的 5 篇遗漏引用已全部添加 ✅：
1. Gur-Arieh et al. (2026) — Ambiguity Collapse taxonomy
2. OpenAgentSafety (Vijayvargiya et al., ICLR 2026)
3. Disambiguation CQA Survey (2025)
4. ATBench (2026)
5. RiskyBench (2026)

R1 注：ATBench、RiskyBench、CQA Survey 在 bib 中使用 "Anonymous" 作者名，camera-ready 应更新为实际作者。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未启用）。

---

## Visual Layout Check（非评分项）

状态：✅ 已完成（0 critical, 2 warning, 8 info）

**Warning (2)**:
- Pages 4-6 连续 3 页纯文本（Method → Evaluation → Results 开头），无 display item 穿插
- Page 7 三个 display items 堆积（Table 2 + Figure 2 + Figure 3），Figure 2/3 被纵向压缩

**Info (8)**:
- Figure 2/3 axis label 字号偏小（~6-7pt）
- Section 5 标题出现在右栏底部接近 orphan heading
- Discussion 仅约 8 行显得简短
- Figure 1 内部方框文字较小
- Table 1 和 Table 2 格式规范 ✓
- 附录页 tables 密度可接受
- 参考文献格式统一，无未解析引用 ✓

R15 的 critical（page 17 大量空白）在 R16 visual check 中未再出现。

---

## Overall Assessment

**Overall Score: 4.0 / 5 — Conference（可被主会议接收）**

**ACL ARR 维度评分（R1, R2 综合）：**

| 维度 | R15 | R16 | 变化 |
|------|-----|-----|------|
| Soundness | 3.5-4.0 | 4.0 | 方差分解完整化 + confound-free range 主文呈现 + Type III SS 交叉验证 |
| Excitement | 3.5 | 3.5 | 不变——单 benchmark 范围限制仍在，但 claims 精准化使方法论贡献更清晰 |
| Reproducibility | 4.0 | 4.0 | Prompt 文本部分缺失（2/5 types）是唯一残留 gap |
| Overall | 3.5 | **4.0** | 所有 Must-Fix 实质性解决，claims 与证据匹配 |

**Confidence**: 4 / 5

**升分核心理由**：

论文的方法论强度（matched-pair causal design + comprehensive statistics + honest variance decomposition）在 R15 就已确立。R15 的主要障碍是 (1) "intervention-design framework" overclaim、(2) C2 mid-tier 的 judge-dependency 不够突出、(3) incompleteness confound 的主文处理不足。R16 通过精准的 claim calibration 有效消除了这三个障碍：

- "Diagnostic taxonomy" 定位诚实且与数据匹配——overclaim 是说服力的敌人，降级后 Contribution (2) 反而更有力
- C2 的 "robust extremes rather than complete linear ordering" 限定精准——既保留了价值（extremes 确实 robust），又未掩盖局限
- Confound-free range 在主文显式区分了 upper bound 和可靠范围

Remaining issues 均为 minor formatting/reproducibility gaps，不影响核心 contributions 的评估。

---

## Detailed Comments

### 修订质量评估

修订展示了高水平的 claim calibration 能力：
- 每个修改都精准回应了审稿意见的核心关切
- 措辞调整既解决了问题又避免了过度弱化（如 C2 "robust extremes" 保留了发现的价值）
- 没有引入新的 substantive 问题
- Type III SS 脚注和方差分解完整化属于超出审稿要求的 proactive 改进

### Camera-ready 建议（非 blocking）

1. Intro 统一 "all" → "all six types" 或 "consistently"
2. Appendix B 补充 cond. prec. 和 scopal 的 prompt 文本
3. Bib 中 Anonymous 条目更新为实际作者
4. 考虑将 Table 2 前移至 p.5-6 以改善视觉密度分布