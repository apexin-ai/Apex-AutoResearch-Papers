---
round: 3
overall_score: weak accept - findings
timestamp: 2026-05-14T18:29:18.749145+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 3 Consolidated Review Report

**Paper**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**Venue**: EMNLP 2026 (ARR Short Paper, 4 pages + references + appendix)
**Round**: 3 (Final)
**Reviewers**: R1, R2

---

## Summary

本文提出 episode-level counterfactual analysis 方法，用于诊断模块化 LLM agent 中 deterministic computation 与 internal reasoning 之间的 routing 行为。在 ScienceWorld 环境（245 episodes, 11 task types）上的实验表明，Death Avoidance Factor (DAF) = 90.41%——即 deterministic 策略相对于 internal reasoning 的优势中约 90% 来自避免 agent 死亡，而非存活场景下的性能差异。论文还提供了 MATH（50 题）和 ALFWorld（135 games）的初步跨环境证据。

经过 3 轮审稿，论文从 8 页主会议投稿压缩为 4 页短文，解决了绝大部分审稿问题。

---

## Strengths

1. **清晰的核心发现**：DAF ≈ 90% 的分解结果直观且具启发性，揭示了 routing signal 高度集中于灾难性失败预防这一非显然事实。
2. **方法论贡献**：Episode-level counterfactual analysis 作为诊断工具，解决了 sparse reward 下 per-step oracle labeling 退化的问题（97.4% tie rate），具有方法论价值。
3. **统计严谨性**：Bootstrap CI、Pearson 相关（r=0.9698, p=8.12×10⁻⁷）、oracle degeneracy 分析（96.3% agreement）、penalty sensitivity 分析（P=10→46.4%, P=200→94.5%）形成多角度验证。
4. **诚实的 scope 限定**：标题加入 "on ScienceWorld"，Limitations 节坦承单模型/单环境局限，conclusion 使用 "consistent with the hypothesis" 而非断言性表述。
5. **跨环境初步证据**：MATH pilot 和 ALFWorld 探索性研究虽规模有限，但支持 death avoidance 现象的普遍性假说。

---

## Weaknesses

### Camera-Ready 必修项

1. **Δ_nd 数值不一致**（R1/R2 共识）：正文 §3.1 报告 Δ_nd = 2.84，Appendix D 报告 Δ_nd = 3.07。两者各自内部一致（DAF 分别为 90.41% 和 89.6%），但不可能同时正确。需统一为同一计算结果。**严重程度：中等——不影响核心结论（DAF 均 ≈ 90%），但损害数值可信度。**

2. **页数需编译验证**：短文正文限 4 页（不含 references 和 appendix）。Reviewer 无法编译验证，camera-ready 需确认合规。

### 残留局限（已在论文中适当 acknowledge）

3. **单模型局限**：仅使用 Qwen2.5-7B-Instruct，DAF 对模型能力的敏感性未知。Limitations 节已承认。
4. **跨环境证据规模有限**：MATH 50 题、ALFWorld 135 games 均为 pilot/exploratory 级别，不足以作为独立结论。论文已以 "preliminary" 和 "exploratory" 定性。
5. **Death penalty 依赖**：DAF 的绝对值与惩罚幅度强相关（P=10 时仅 46.4%）。Penalty sensitivity 分析已加入，但读者需注意 90% 这个数字的条件性。

---

## Questions（供作者 camera-ready 参考）

1. Δ_nd = 2.84 vs 3.07：哪个是正确值？是否因 episode 筛选标准不同导致？
2. 如果将 ScienceWorld death penalty 从 -100 改为环境实际执行的惩罚机制（如 episode 提前终止但不扣分），routing signal 是否消失？

---

## Missing References

无重大遗漏。Related work 已覆盖 22 篇文献，包括 4 篇 2026 concurrent work 和 safe RL 经典综述。

---

## Overall Assessment

**评分：3.25 / 5（Weak Accept — Findings Track）**

| Reviewer | Round 1 | Round 2 | Round 3 | 推荐 |
|----------|---------|---------|---------|------|
| R1 | 2.5 | 3.0 | 3.5 | Findings 接收 |
| R2 | 2.0 | 2.5 | 3.0 | Findings 接收 |

**共识**：两位 Reviewer 一致推荐 EMNLP 2026 Findings track 接收。

**理由**：
- 核心贡献（DAF 分解 + episode-level counterfactual methodology）对 LLM agent routing 社区有实际诊断价值
- 3 轮修订有效解决了所有 critical blockers：scope overclaim → 标题限定；DAF triviality → penalty sensitivity；train/test ambiguity → 显式数据划分段落
- 短文格式合理——单一核心发现 + 诊断方法论，不需要主会议级别的广度
- 残留问题（Δ_nd 不一致）为数值校对问题，不影响结论方向，camera-ready 可修

**风险**：如果 Δ_nd 不一致源于更深层的计算错误（而非简单的版本不同步），可能需要重新验证核心数字。建议作者在 camera-ready 中明确报告计算 pipeline 版本。

---

## Detailed Comments (Per-Round Evolution)

### Round 1 → Round 2 主要改进
- 8 页主会议 → 4 页短文（scope 匹配度大幅提升）
- 标题加入 "on ScienceWorld" 限定
- Abstract 去除数字堆砌，加入 backbone 限定
- Related work 从 13 → 20 篇，新增 Concurrent Work 小节
- 独立 Limitations 节

### Round 2 → Round 3 主要改进
- DAF 定义增加 well-defined 条件 + 内联 penalty sensitivity
- Router training 细节移至 Appendix C，正文压缩
- 新增 Data split 段落（85/15 episode-stratified, fresh env evaluation）
- Conclusion 措辞从 "structural driver" → "consistent with the hypothesis"
- 新增 safe RL 引用（García & Fernández 2015）
- DAgger 引用恢复

### 未解决
- Δ_nd 数值不一致（camera-ready fix）
- 页数编译验证（camera-ready check）

---

## Issue Tracker Summary (19 issues)

| 状态 | 数量 |
|------|------|
| resolved | 15 |
| open (camera-ready) | 2 |
| wontfix (acknowledged in limitations) | 2 |

Open issues: #11 Δ_nd inconsistency, #19 page count verification.

---

*Round 3 Final — Review Director*