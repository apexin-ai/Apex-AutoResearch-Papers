---
round: 30
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-24T11:05:46.976587+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 30

**Paper**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety"
**Venue**: EMNLP 2026 via ARR May cycle (Long paper, 8-page limit)
**Reviewers**: R1 (方法严谨性 + 实验设计) / R2 (新颖性 + 完整性 + 格式合规)
**交叉回应**: R1→R2, R2→R1 均已完成，1 轮即收敛
**评分**: R1 = 3.5, R2 = 3.5（一致）

---

## Summary

论文提出首个匹配对因果研究，证明自然语言策略规范中的歧义增加 LLM agent 安全违规（+34.0 pp on τ²-bench, 300 clause pairs × 5 models × 2,997 episodes）。六类型分类法下，条款措辞解释 22.4% 方差而类型归属仅 0.4%。提出 convergent nocuity 概念（41.3% 条款触发多模型收敛违规，77% permissive bias）和 type–mechanism dissociation（V=0.45 LLM-coded; human κ=0.41）。SOPBench 跨基准复制（+12.7 pp unweighted mean, 5/5 Δ>0），healthcare pilot 跨领域扩展（+58.8 pp）。

核心因果发现（C1）方法论扎实、效应量大且方向稳健。C2（type ordering）有合理支撑。C3（type–mechanism dissociation）human validation 不足（κ=0.41），是主要瓶颈。格式操纵（\enlargethispage）存在 desk rejection 风险。

---

## Strengths

**S1: 严谨的因果推断设计** — 匹配对设计在同一 model–judge 配对内比较，系统性偏差在差分中取消。Perturbation control（Δ=-0.67 pp, CI [-4.67, 6.67]）确认效应特异于语义歧义。Coreferential 类型（Δtoken ≈ 7.8 words, +18.7 pp）提供信息添加混淆最小化的下界。这种设计在 agent safety 文献中是首创。

**S2: 统计分析全面** — 方差分解（Type III SS）、TOST 7-margin sensitivity analysis、bootstrap clustering（B=10,000）、McNemar OR、logistic regression（Tjur's R²=0.175）、permutation test——工具箱使用充分且互相佐证。特别是 sensitivity analysis 避免了锚定单一 SESOI 的弱点。

**S3: Convergent nocuity 是真正的概念贡献** — 反转 Berry & Kamsties (2004) divergent/innocuous 框架，提出 LLM agent 收敛到相同错误解读的失效模式，使基于一致性的安全监控失效。77% permissive attractor 揭示系统性偏差方向。具有超出本文的理论价值。

**S4: 多层次复制** — τ²-bench 双域（retail/airline）、7 个模型、SOPBench 跨基准、healthcare pilot 跨领域。方向一致性在所有条件下稳健。

**S5: 透明的自我约束** — §6 标题标注 [Exploratory]、C4 标记 exploratory、incompleteness 标注 information-addition confound、κ=0.41 标注 "preliminary evidence"。这种诚实的 hedging 提高可信度。

---

## Weaknesses

### Critical

**W1 [R1-N2 + R2, 强共识]: Human κ=0.41 不足以支撑 C3**

核心问题链：(a) LLM-coded V=0.45 可能受 shared classification conventions 放大（§6 第一段自承）；(b) Human κ=0.41 作为独立验证仅达 Landis & Koch "moderate"，远低于 Krippendorff α≥0.667 的内容分析标准；(c) Abstract 中 "V = 0.45, LLM-coded; human collapsed κ = 0.41" 并列暗示类似水平支撑，但 V 衡量 association strength（6×5 table），κ 衡量 inter-rater reliability，性质不同；(d) Contributions (3) 中 C3 占核心位置但 §6 标题标注 [Exploratory]，定位不完全一致（"preliminary evidence" 已是正确方向但 contributions 列表的篇幅权重暗示与 C1/C2 同等重要）。

**要求**：二选一——(a) 扩大人工标注至 ≥200 episodes 使 κ≥0.60；或 (b) 在 Abstract/contributions 中明确将 C3 标注为 exploratory/hypothesis-generating 并减少相对权重。

**W2 [R2 主导，R1 认同]: \enlargethispage 格式操纵**

论文使用 3 处 `\enlargethispage`（experiments.tex: 8 + 18 baselines; method.tex: 8 baselines）。`\enlargethispage{18\baselineskip}` 极其激进——约 3 英寸额外页面高度。目的是将正文压缩至 8 页内。

- 18\baselineskip 可能导致底部边距低于 ACL 模板要求
- 即使边距合规，审稿人/AC 可能视此为规避页数限制
- **潜在 desk rejection 风险**

**要求**：移除所有 `\enlargethispage`，通过内容调整（§6 部分内容或 Table 2 移入 appendix）自然适配 8 页。

### Warning

**W3 [R1-N1 + R2, 共识]: 生态效度差距分析不充分**

τ²-bench +34.0 pp → SOPBench +12.7 pp = 2.7× 衰减。Discussion §7 "Practical implications" 段仅一句话列出三个效应量。未分析差距来源：合成最大化（synthetic maximalism）、评估方法差异（SOP compliance constraints vs four-tier violation classification）、自然歧义严重程度分布。Limitations 标注 "upper bound / cross-benchmark lower bound" 但未分析 bound 之间的结构性原因。R2 补充：SOPBench 使用 unweighted mean、且 healthcare pilot 反向显示 +58.8 pp > +34.0 pp，说明效应在高风险域可能被放大。

**要求**：Discussion 增加一段（~150 words）分析衰减机制。

**W4 [R1-W1 + R2 部分同意]: SESOI ±15 pp 缺乏领域成本锚定**

论文承认 "pragmatic default, not a principled domain-anchored threshold"。7-margin sensitivity analysis 和 bootstrap clustering 比固定单一 SESOI 更信息丰富。但缺少将 15 pp 与实际部署成本关联的一步——例如 $200/违规 × 15 pp = $3,000/100 episodes。一段简短分析即可。

**W5 [R1-W2 + R2, 共识]: Temperature pilot underpowered**

3/5 模型、50 clause pairs、无 CI。Appendix Table 28 仅报告 agreement rate（85–97%），未报告 per-clause Jaccard 或效应量 CI。论文的先验论证（unambiguous floor 6.9%，温度主要影响 ambiguous condition）方向性成立，但不能替代效应量的温度敏感性分析。

**W6 [R1-W3 + R2-W7, 共识]: Cross-judge 设计不平衡**

5 个法官中 3 个来自 OpenAI 家族（3:2 分配）。§4.4 的缓解论证（matched-pair 内 bias 取消）对 C1/C2 成立，但对 convergent nocuity（§6.3）不成立——convergent nocuity 依赖跨模型 absolute violation patterns 的比较，受法官选择影响。Limitations 承认 "may inflate cross-model convergence estimates" 但未量化偏差方向或幅度。

**W7 [R1-M1 + R2, 共识]: Convergent nocuity 缺少独立性基线**

5 个模型各有 ~41% 独立违规率时，二项分布预期 ≥3/5 收敛约 33.5%。观测 41.3% 超出约 8 pp。论文的 Jaccard 分析（bootstrap p<0.0001）提供更强非独立性证据，但缺少独立性基线使 41.3% 的解读不够精确。添加一行计算即可。

**W8 [R1-W5 + R2, 共识]: Authorization scope 驱动 C4 但可靠性最低**

Table 2 脚注 ‡ 标注 auth scope κ=0.385（n≈17）。C4 排除 auth scope 后完全消失（p=0.97）。论文已适当 hedge（C4 标记 exploratory），但 auth scope 的低可靠性限制了 model×type interaction 的可解读性。

---

## Questions

**Q1**: Perturbation control 的 300 episodes 是否使用与主实验相同的 clause pairs 的 unambiguous 版本？§4.5 描述不够明确。

**Q2**: SOPBench 衰减中 measurement methodology difference vs genuine attenuation 各占多少？是否可用 episode-level detail 分解？

**Q3**: Healthcare pilot +58.8 pp 的放大机制？§7 仅说 "domain-specific amplification"。可能原因：(a) 高风险场景 stakes 放大；(b) healthcare policy 语言 less in-distribution；(c) 不同平台 safety guardrails 差异。建议 Discussion 简要讨论。

**Q4**: Residual 方差中 ~46% 系统方差的来源？§5.1 仅提及 "Appendix R" 但未在正文讨论。可能来源包括 episode-specific 对话轨迹差异、非操作条款上下文、user 行为模式差异。如果主要是非歧义因素则强化论点；如含未控制混淆则削弱因果推断。

**Q5**: Coreferential 排除于 SOPBench 的具体原因？Appendix B 解释了 mitigation 排除理由，但 SOPBench 排除原因不明。

---

## Points of Divergence

**R2 反驳 R1-W4 (Perturbation control CI 过宽)**: R2 论证 CI 宽度本身不是论证缺陷——perturbation control 目的是证明 surface-level text changes 不产生效应（CI 含零已确认），coreferential +18.7 pp 远超 CI 上界。论文将 CI 作为 worst-case bound 使用恰当。**Director 判断：R2 反驳成立**，此项不计入 weakness。

**R2 反驳 R1-Q5 (Kendall's W=0.398 vs convergent nocuity)**: R2 论证两指标衡量不同层次——W 衡量 type-level ranking concordance，Jaccard 衡量 clause-level co-occurrence。低 W + 高 Jaccard 恰恰一致：clause wording（22.4%）比 type membership（0.4%）重要，所以 clause-level convergence 强但 type-level concordance 弱。**Director 判断：R2 反驳成立**，两指标的 dissociation 支撑而非矛盾论文核心论点。

---

## Missing References

1. **RLHF / Constitutional AI 作为 moderating variable**：不同对齐训练方法可能导致模型对歧义敏感度不同。Table 2 中 Claude (12%) vs GPT-5.4/DeepSeek (60-64%) 在 auth scope 上的巨大差异可能反映训练哲学差异。建议 Discussion 简要讨论。
2. **Prompt robustness / adversarial robustness 文献**：§2 未引用。但鉴于论文侧重 policy specification 而非 adversarial attack，遗漏严重性有限。

---

## External Review

**Stanford Agentic Reviewer**: 未请求。

---

## Visual Layout Check (非评分项)

视觉审查已完成。**0 critical, 0 warning, 7 info**。

主要发现：
- Figure 2 浅色系灰度打印可能难以区分；建议添加纹理或调整色阶
- Figure 5 热图红绿色盲可能区分困难；建议改用 viridis 色阶
- Table 2 脚注字号偏小
- 其余 4 项均为正常范围内的排版观察

无需因视觉问题调整评分。

---

## Overall Assessment

### 3.5 — Borderline Conference

**两位 Reviewer 一致评分 3.5 (Borderline Conference)**。

**录用论据**：
- C1（policy ambiguity → safety violations 因果效应 +34.0 pp）方法论扎实，匹配对设计在 agent safety 文献中是首创
- Convergent nocuity 是对 agreement-based safety monitoring 的重要理论挑战，具有超出本文的价值
- 多层次复制（7 模型、3 基准/场景）方向一致性强化因果推断
- 统计分析全面且互相佐证

**拒稿论据**：
- C3 type–mechanism dissociation 的 human validation（κ=0.41）不足以支撑其作为核心贡献的定位
- `\enlargethispage{18\baselineskip}` 格式操纵存在 desk rejection 风险
- 生态效度差距（2.7×）的 Discussion 分析不充分
- Cross-judge 设计偏差对 convergent nocuity 的影响未量化

**升至 4.0 的路径**（按优先级）：
1. **[必需]** 解决 Human κ 问题：扩大标注或明确降级 C3 在 Abstract/contributions 中的定位
2. **[必需]** 移除 `\enlargethispage`，正文自然适配 8 页
3. **[强建议]** Discussion 增加衰减机制分析段（~150 words）
4. **[建议]** §6.3 添加独立性基线计算

---

## Detailed Comments

### R1 独有发现评估
- **R1-M2 (Berry 概念反转)**: R2 同意。§6.3 "but inverted" 后应增加 1–2 句解释诊断含义变化：从 "divergent → 可检测到分歧" 到 "convergent → 无法检测到一致的错误"。小修即可。
- **R1-Q3 (Healthcare 放大机制)**: R2 同意有效。建议 Discussion 增加 2–3 句简要讨论。

### R2 独有发现评估
- **R2-W1 (\enlargethispage)**: R1 未独立提出但关联 R29-MF1（页数问题）。这是格式合规问题，严重性独立于学术内容质量。**确认为 Critical**——这是可以独立导致 desk rejection 的格式问题。
- **R2 对 [Exploratory] 标签不一致的观察**: Abstract/contributions (3) 中 C3 的定位与 §6 [Exploratory] 标题不完全一致。"preliminary evidence" 措辞已是正确方向，但 contributions 列表中 C3 的位置和篇幅暗示与 C1/C2 同等重要。这与 W1 相关联。

### 跨轮次趋势（R28→R29→R30）
- **κ 值**：0.15 (R28) → 0.41 (R29/R30)。方向正确但仍不足。
- **格式问题**：R28 标注 margin compliant → R29 提出页数疑虑 → R30 确认 \enlargethispage 操纵。问题加剧。
- **C3 framing**：从 "establishes" (R28) → "preliminary evidence" (R30)。改善但需进一步对齐。
- **生态效度**：从 R28 首次提出 → R29 action item → R30 仍 open。3 轮未充分解决。