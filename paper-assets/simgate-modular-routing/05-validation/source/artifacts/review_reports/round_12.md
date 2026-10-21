---
round: 12
overall_score: weak accept
timestamp: 2026-05-17T06:48:10.230495+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 11 审稿报告 — simgate-modular-routing

**论文**: Death Avoidance as a Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**目标**: EMNLP 2026 Findings (via ARR May 2026)
**Reviewers**: R1 (方法严谨性+统计推断), R2 (新颖性+写作+Related Work)

---

## Summary

论文提出 episode-level counterfactual 框架（Algorithm 1 + DAF + SCI）用于诊断 modular LLM agent 的 routing signal 来源。以 ScienceWorld 为 case study（11/30 task types, N=245, Qwen2.5-7B-Instruct），发现 78.9% 的 non-tie routing labels 由 death asymmetry 驱动，DAF=90.4%@P=100。跨环境（MATH confirmed null, ALFWorld information asymmetry）和跨模型（Llama pilot）分析展示框架 diagnostic flexibility。Router training 作为 informative negative 支持 analytical framework 优于 brute-force learned routing 的结论。

---

## Strengths

1. **R10 问题修复优秀**：前轮 12 条 open issues 中，10 条已完全修复（R10-C2/C3/C4/W1/W2/W5/W6/W7/m1/m2），1 条部分修复（R10-W3 引用），1 条未修复（R10-C1 partial correlation, 升级为 R11-C1）。Claim calibration 全文一致。

2. **方法论透明度**：DAF 的 mathematical nature（随 P 单调递增）被显式承认为 "mathematical consequence, not empirical finding"；r=0.97 被定位为 "internal consistency check"；data scaling 区分 augmentation vs real-data；cross-model 标注 "preliminary pilot"。

3. **框架设计合理**：Algorithm 1 逻辑无歧义（四个 mutually exclusive cases），DAF decomposition 数学正确，SCI 有效补充 "systematic vs outlier-driven" 问题。Dual-metric（penalty-independent 78.9% + penalty-dependent DAF）设计使结论不依赖单一假设。

4. **统计实践规范**：Episode-level bootstrap (B=10,000), cluster bootstrap sensitivity, McNemar test, LOO robustness, penalty sensitivity, seed robustness（8 seeds）, capacity scaling controlled replication。

5. **Negative result 有价值**：Router diagnostic 不是 "failure report" 而是 "framework predicts and explains why routing fails"——对 agent routing 社区有实际指导意义。

---

## Weaknesses

### Must-Fix (投稿前)

**[Critical] W1: Partial correlation (r=0.02, p=0.91, df=27) 数学上 undefined**
- 位置：Abstract, Introduction, §4.1, Conclusion（4 处引用）
- 问题：P=100 对所有 task types 为常数 → δ·P = 100δ → r(δ, δ·P) = 1.0 → partial correlation 分母为零 → undefined。扩展到 n=30 不解决 structural collinearity。r=0.02 是 floating-point artifact。
- 影响：论文核心论证（r=0.97 is structural）的支撑证据无效。概念论证正确但数值报告有误，损害全文统计可信度。
- 修复：删除 r=0.02/p=0.91/df=27 所有出现，替换为代数论证："When P is constant across tasks, δ·P is perfectly collinear with δ; this collinearity proves r=0.97 is a mathematical consequence of death dominance." 或改用 corr(Δ_nd, δ) 作为替代 well-defined statistic。

**[Warning] W2: Em-dash (---) 泛滥，20+ 处 AI 写作标志**
- 位置：全文正文（Abstract 到 Conclusion）
- 影响：不影响 soundness 但触发 reviewer 对 AI-generated content 的警觉
- 修复：全局 `grep "---" *.tex`，替换为逗号/括号/拆句。保留 en-dash (--) 数字范围和专有名词。

**[Warning] W3: \nolinenumbers 违反 ACL ARR review 格式**
- 位置：main.tex line 23
- 影响：Desk reject 风险
- 修复：删除 `\nolinenumbers`

### Should-Fix

**[Warning] W4: Capacity scaling dual-reporting**
- Main text (4-seed controlled): 0.6B=50.7%, 1.7B=43.1±1.0%, 4B=59.0%
- Appendix Table 8 (8-seed original): 1.7B=47.1±2.2%
- 两套 1.7B 数字共存造成混淆。0.6B/4B 在 main text 缺 error bars。
- 修复：统一为一套 controlled 数字（带 error bars），8-seed 放 appendix robustness。

**[Warning] W5: Cluster bootstrap K=11 缺 formal caveat**
- CI [73.3%, 100%] 基于 K=11 clusters（远低于 K≥40 推荐值）
- 上界 100% 是 small-K artifact
- 修复：引用 Cameron, Gelbach & Miller (2008)，加 caveat statement。

**[Warning] W6: McNemar test 输入未与 routing labels 区分**
- MATH §4.3 并列报告 McNemar p=0.81 和 routing labels (107/95)，但二者定义不同
- McNemar 应用于 binary correct/incorrect discordant pairs (≈103/99)，routing labels 包含额外 score-comparison discordances
- 修复：加一句澄清 McNemar input definition。

### Nice-to-Fix

**[Minor] W7: §4.1 和 §4.5 段落过密** — 加 \paragraph{} 标记拆分
**[Minor] W8: Abstract 中 78.9% vs DAF=90.4% 区分不直观** — 加半句因果链
**[Minor] W9: Mann-Whitney vs Wilcoxon signed-rank** — 明确 reasoning depth ablation 是否 paired design
**[Minor] W10: 引用 37 篇略低** — R1 认为可接受，R2 建议补 2-3 篇。非 blocking。

---

## Reviewer Consensus

所有关键发现均已达成共识：

- **[AGREE]** Partial correlation 必须删除（structural collinearity, undefined）
- **[AGREE]** Em-dash 和 \nolinenumbers 必须修复
- **[AGREE]** Cluster bootstrap 需 citation + caveat
- **[AGREE]** Capacity dual-reporting 需统一
- **[AGREE]** R10 issues 绝大部分已有效修复
- **[AGREE]** 框架设计 sound，DAF decomposition 数学正确
- **[AGREE]** Negative result (router failure) 有社区价值

---

## Reviewer Divergence

**McNemar p=0.81 (轻微分歧, 已解决)**：
- R1: p=0.81 与 routing labels 107/95 不一致 (应得 p≈0.40)
- R2: [REBUT] 重构表明 McNemar 基于 binary discordant pairs (≈103/99 with continuity correction → p≈0.83)，与报告吻合
- 共识：p=0.81 大概率正确，但需澄清 definition difference

**引用数量 (轻微分歧)**：
- R2: 37 篇偏低 (EMNLP 典型 40-60)，建议补 ToolBench, Safe RLHF
- R1: [REBUT] 37 可接受，覆盖度比数量重要，ToolBench/Safe RLHF 研究问题与本文不同
- 共识：2-3 篇额外引用是 nice-to-have，非 blocking

**Excitement (评分差异)**：
- R1: 3.5/5 (框架 reuse potential 高，Findings bar 合适)
- R2: 2.5/5 (scope 窄，core insight 不 surprising)
- 差异主要在 Findings track 标准理解——R1 认为 "novel diagnostic framework + informative case study" 达标，R2 认为仍偏 niche

---

## Questions（需作者回应）

1. Partial correlation 的具体计算代码？是否因 floating-point tolerance 返回 r=0.02 而非 NaN？
2. MATH McNemar exact discordant cell counts (b, c) 是多少？
3. 0.6B/4B controlled replication 是否也有 std？为何 main text 不报告？
4. `find-non-living-thing` 两批数据（n=40）是否存在 batch effect？
5. 排除的 19 task types 延长 step budget 后是否可能产生 routing signal？
6. "Dominant" 的判据是什么——DAF>50%? label fraction>50%? 两者 AND?

---

## Missing References

- ToolBench (Qin et al., 2024) — tool-use benchmark [R2 建议, R1 认为非必须]
- Safe RLHF (Dai et al., 2024) — LLM-era safe alignment [R2 建议, R1 认为研究问题不同]
- Cameron, Gelbach & Miller (2008) — cluster bootstrap minimum K [R1 和 R2 共识]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 external_review.paperreview_ai.enabled）

---

## Overall Assessment

**Borderline Accept (Findings)**

框架设计 sound，case study 分析详尽且诚实，claim calibration 优秀，R10 issues 修复到位。核心 critical issue 仅 1 条（partial correlation 无效统计量），且修复方案明确（删除数值，保留代数论证，不影响主要结论）。Em-dash 和 \nolinenumbers 是 mechanical fixes。

主要限制：单环境 evidence (ScienceWorld 11/30 tasks)、excitement 中等 (analytical/negative result)、scope 窄。但对 EMNLP Findings track（"solid work with niche interest"），这些限制可接受。

修复 W1-W3 后，论文达到 Findings accept 水平。

**评分**: weak accept (Findings)
**置信度**: 4/5

---

## Detailed Comments

### Abstract
- 删除 "partial r=0.02, p=0.91" 引用，替换为 collinearity 论证
- 78.9% 和 DAF=90.4% 之间加半句区分 (penalty-independent → penalty-dependent)
- "Algorithm~1" 改为 "our labeling procedure" 或删除

### Introduction
- §1 para 5 (contributions): 无需修改，claim 已 well-calibrated
- 删除 partial correlation 数值（line 25 area）

### Method
- §3.4 DAF: 无实质问题，mathematical caveat 已充分
- §3.5 SCI: sound

### Experiments
- §4.1: 删除 partial correlation r=0.02 数值；拆分长段落
- §4.3 MATH: 加 McNemar input clarification sentence
- §4.5 Router: 统一 capacity scaling reporting；拆分长段落

### Related Work
- 可选补 2-3 refs (ToolBench, Safe RLHF, Cameron et al. for cluster bootstrap)
- 当前覆盖五个主题，结构清晰

### Discussion
- 无实质问题

### Conclusion
- 删除 partial correlation 数值引用

### Format
- 删除 \nolinenumbers
- 全局清零 em-dash (---)

---

## 优先级排序（投稿前 action list）

| 优先级 | Item | 预计工作量 |
|--------|------|-----------|
| P0 (blocking) | 删除 partial correlation r=0.02 (4 处) + 替换为代数论证 | 15 min |
| P0 (blocking) | 删除 \nolinenumbers | 1 min |
| P0 (blocking) | 全局清除 em-dash (20+ 处) | 30 min |
| P1 (should-fix) | 统一 capacity scaling reporting + error bars | 20 min |
| P1 (should-fix) | Cluster bootstrap citation + caveat | 5 min |
| P1 (should-fix) | McNemar clarification sentence | 5 min |
| P2 (nice-to-fix) | 段落拆分 (§4.1, §4.5) | 10 min |
| P2 (nice-to-fix) | Abstract 78.9%/DAF 区分半句 | 5 min |
| P2 (nice-to-fix) | Mann-Whitney/Wilcoxon 澄清 | 5 min |
| P2 (nice-to-fix) | 补 2-3 references | 10 min |