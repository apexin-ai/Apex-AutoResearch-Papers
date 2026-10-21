---
round: 5
overall_score: weak accept
timestamp: 2026-05-14T21:28:21.185118+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 5 (修订验证)

**Paper**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Venue**: EMNLP 2026 · ARR Findings · Deadline 2026-05-25
**Reviewers**: R1 (方法严谨性) + R2 (新颖性与完整性)
**交叉回应**: 完成。完全收敛。

---

## Summary

本轮为修订验证——论文已根据 Round 4 审稿报告进行全面修改。Round 4 提出 2 个 critical、3 个 major、5 个 minor issues。本轮验证结果：**所有 critical 和 major issues 均已 RESOLVED**，修订质量整体优秀，仅剩 4 个 camera-ready 级别的小修复。两位 Reviewer 一致将评分从 3.0 上调至 3.5，推荐 Findings track 接收。

---

## Round 4 Issues 验证结果

### Critical Issues — 全部 RESOLVED

**R4-W1 [critical] DAF headline claim penalty 条件 + 78.9% metric → [RESOLVED]**
- Abstract: ✅ "approximately 90% ... under the default −100 death penalty"
- §2.3: ✅ Penalty sensitivity 正文讨论 + "75 of 95 non-tie routing labels (78.9%) are driven by death asymmetry"
- Conclusion: ✅ "90.41% ... under the default −100 penalty (78.9% of non-tie labels from death asymmetry)"
- ⚠️ Related Work §4 有两处残留的 "~90%" 未加条件 → camera-ready fix (R5-CR1)

**R4-W2 [critical] Pearson r robustness → [FULLY RESOLVED]**
- §3.1: ✅ Spearman ρ=0.986 (p=2.4×10⁻⁸) + bootstrap 95% CI [0.952, 0.995] + LOO r∈[0.963, 0.980]
- 新 Appendix C: ✅ 完整 LOO table，最低 r=0.963，无高杠杆点
- **R1 评价："本轮修订中做得最好的一处，统计 robustness 堪称 short paper 典范"**

### Major Issues — 全部 RESOLVED

**R4-W3 [major] Router diagnostic caveat → [RESOLVED]**
- §3.3: ✅ "we cannot conclusively distinguish structurally thin routing signal from data insufficiency"
- §3.3: ✅ "not statistically outperforming always-deterministic (overlapping 95% CIs)"
- §3.3: ✅ Majority-class baseline 89.2% 报告
- §3.3: ✅ Balanced accuracy 统一为 58.1±0.8% (4-seed mean±std)
- ⚠️ Introduction contribution (2) 仍用 "failing to outperform" → camera-ready fix (R5-CR3)

**R4-W4 [major] 单模型外部效度 → [RESOLVED]**
- Limitations: ✅ "Stronger models likely exhibit lower internal-strategy death rates, which would reduce DAF. Our finding may reflect a capability-dependent failure mode."

**R4-W5 [major] 方法论贡献 framing → [RESOLVED]**
- Introduction: ✅ "identifying step-level oracle degeneracy in sparse-reward environments and applying episode-level counterfactual analysis to diagnose routing signal composition"
- R2 确认与 Findings track 定位一致

### Minor Issues — 全部 RESOLVED

**R4-W6 [minor] Δ_nd 符号不一致 (2.84 vs 3.07) → [RESOLVED]**
- Appendix E caption 明确解释两种计算口径差异
- ⚠️ 但修订引入新的 Δ_nd 2.84 vs 2.81 不一致 → camera-ready fix (R5-CR2)

**R4-W7 [minor] 58.1% vs 59.3% → [FULLY RESOLVED]**
- §3.3 和 Conclusion 统一为 58.1±0.8% (4-seed mean±std)

**R4-W8 [minor] ALFWorld Conclusion 措辞 → [FULLY RESOLVED]**
- "catastrophic failure prevention being a cross-environment phenomenon, though the specific mechanism varies (death avoidance in ScienceWorld vs. action space pruning in ALFWorld)"

**R4-W9 [minor] Prescreening scope → [FULLY RESOLVED]**
- Limitations: "11 of 30 ScienceWorld task types; the remaining 19 (63%) were excluded"
- Introduction/§2.1: "97.4% of steps (across 11 prescreened task types)"

**R4-W10 [minor] Hyperparameters → [FULLY RESOLVED]**
- Appendix D Table 4: 两个 architecture 完整参数（lr, optimizer, epochs, LoRA config, batch size, grad accum, warmup, weight decay, seeds）

### 历史遗留 Issues

**R3-CR1 (Δ_nd 2.84 vs 3.07) → [RESOLVED]** — Appendix E caption 解释充分
**R3-CR2 (页数) → [RESOLVED]** — R1 验证：正文 4 页，总计 7 页，合规

---

## Camera-Ready 修复清单（4 项，均为 minor/cosmetic）

| ID | 问题 | 修复 | 发现者 |
|---|---|---|---|
| R5-CR1 | Related Work §4 两处 "~90%" 未加 penalty 条件 | 加 "under the default penalty" | R1+R2 |
| R5-CR2 | Δ_nd=2.84 (§3.1) vs 2.81 (Limitations, Appendix E) | 统一为 2.84 | R1, R2 AGREE |
| R5-CR3 | Intro contribution (2) "failing to outperform" vs §3.3 "not statistically outperforming" | 统一为 "does not significantly outperform" | R1, R2 AGREE |
| R5-CR4 | §3.3 accuracy/recall 单 seed vs balanced accuracy 4-seed 口径未标注 | 标注 "(best seed)" 或全部报 4-seed | R2, R1 AGREE |

以上 4 项均为 5 分钟内可完成的文字修订，不涉及实验或分析变更。

---

## 修订后新增优势

**S7. 统计 robustness 论证堪称 short paper 典范** [R1]：Spearman ρ + bootstrap CI + LOO analysis + Appendix C 详表，完整消除了 "n=11 是否可靠" 的质疑。

**S8. Penalty-independent metric 补强核心 claim** [R1]：78.9% death-asymmetry episode ratio 提供了不依赖 P 的证据线，与 DAF=90.41% 相互印证。

**S9. Data-insufficiency caveat 态度诚恳** [R1]：§3.3 明确承认无法区分 "signal thin" vs "data insufficient"，同时报告 majority-class baseline，使读者可自行判断。

---

## Reviewer Consensus（Round 5）

两位 Reviewer **完全收敛**：
1. ✅ 所有 critical/major issues RESOLVED
2. ✅ 剩余 4 项均为 camera-ready 级别
3. ✅ 评分一致上调：3.0 → 3.5
4. ✅ 推荐 Findings track 接收
5. ✅ Bib 验证：dynathink-2025 author mismatch 为 API 解析问题，无需修改
6. ✅ Missing references (safe RL agents, credit assignment)：nice-to-have，不影响接收

## Reviewer Divergence（Round 5）

无。两位在所有验证项上完全一致。

---

## External Review (Stanford Agentic Reviewer)

项目未配置外部审稿，本轮无外部审稿结果。

---

## Overall Assessment

**Overall Score: 3.5/5 — Weak Accept (Findings)**
**Confidence: High (4/5)**
**建议: Accept for EMNLP 2026 Findings track, pending 4 camera-ready fixes**

**评分变化**: Round 4 (3.0 Borderline) → Round 5 (3.5 Weak Accept)

**升分理由**：
1. R4-W2（统计 robustness）修复质量出色——三重验证完全消除了 n=11 的质疑
2. R4-W1（DAF qualification）修复方向正确——P 条件限定 + 78.9% penalty-independent metric
3. R4-W3（router caveat）诚恳承认局限性
4. R4-W5（贡献 framing）与 Findings track 一致
5. Appendix C (LOO) + Appendix D (hyperparameters) 显著提升可复现性

**未升至 4.0 的原因**：
1. 单环境 + 单模型的 scope 限制未变（固有约束，非修订问题）
2. Router diagnostic（§3.3）底层数据不足问题无法通过措辞解决
3. 修订引入了 3 个小错误（2.81 笔误、Related Work 残留、Intro 措辞），反映校对不够细致

**最终判断**：论文核心贡献（death avoidance dominates routing signal in ScienceWorld）有充分统计支撑（Pearson r=0.97, Spearman ρ=0.99, LOO stable, DAF=90.4% + 78.9% penalty-independent），方法论透明，局限性诚实表述。修复 4 个 camera-ready items 后，符合 EMNLP 2026 Findings 接收标准。