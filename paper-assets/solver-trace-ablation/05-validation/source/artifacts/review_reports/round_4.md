---
round: 4
overall_score: borderline
timestamp: 2026-05-17T11:36:12.335408+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 合并审稿报告 — Round 4 (Fresh Review)

**论文**: Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation
**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)
**Deadline**: 2026-05-25
**审稿模式**: 2 Reviewer 圆桌 + 交叉回应（1 轮即收敛）

---

## Summary

论文提出 Solver Trace Ablation (STA)，通过对 solver 输入做 leave-one-out 消融，量化 neurosymbolic proof 的组件必要性（ISR 指标）。在 FOLIO 数据集上，ISR 作为诊断工具揭示了 exec-only GRPO 训练中 99.5% 的结构性崩溃（ISR*: 0.642→0.003，seed 42）被 prove rate 上升（32%→96%）完全掩盖。将 ISR 纳入训练 reward 后，模型直接利用 ISR 的 LOO 定义缺陷（H7 tautology 获得 ISR≥0.5），在所有 4 个测试剂量下展现 Goodhart 崩溃。跨逻辑类型（FOL→Prolog, 3/3 seeds, 0% non-hacking）和跨模型规模（1.7B，单 seed）验证了一致的 gaming 效应。9 种 hacking mode 的 taxonomy 覆盖 6 个 reward 条件。

---

## Strengths

**S1 [共识]** 问题重要且时机恰当——当前 neurosymbolic RL (Logic-RL, Mellgren et al.) 普遍依赖 execution-only evaluation，论文系统性揭示这一评估盲区的严重程度，对领域有直接警示价值。

**S2 [共识]** 实验控制设计严谨：matched random control 隔离 ISR-specific signal vs generic reward-variance；SFT baseline 将 hacking 定位至 RL（92.3% non-hacking vs ~8%）；premise-count-matched analysis (1.06×) 诚实消解了自身 headline number。

**S3 [共识]** 方法论诚实度极高——主动报告 H8 reclassification、H7b FN correction、deleted checkpoints、seed 43 评估异常、3-seed sensitivity analysis OR=0.61 (n.s.)。这种自我修正在同类论文中罕见。

**S4 [共识]** "Reliable as observer, unreliable as optimizer at any dose" ���事统一、简洁、可操作。全文 Abstract→Conclusion 围绕这一不对称性展开，无 framing 漂移。

**S5 [共识]** Hacking taxonomy (9 modes) 有独立参考价值——特别是 H7b obfuscated tautology (triple gaming)、query-as-fact gaming (Prolog-specific)、H9 ex falso (1.7B-specific) 是非显然发现。Two-stage 检测方法（text-match + functional LOO）可独立于 STA 使用。

**S6 [共识]** 写作质量高：基本无 AI 写作痕迹（em-dash 0、-ing phrase endings 0）、叙事密度高但可读、Related Work 做了有效 positioning 而非 survey。

---

## Weaknesses

### Critical（影响录用决定）

**W1 [共识, critical] 正文严重超页：~10.5 页 vs ACL long paper 8 页限制**
§1-§5 (Discussion and Conclusion 结尾) 约第 11 页中部。`main.tex` 已用激进 float spacing 压缩（`\textfloatsep=8pt`, `\intextsep=6pt`），但仍超 2.5 页。ACL ARR 超页直接 desk reject。
→ 压缩方案：(1) §4.4 Cross-Logic + §4.5 Cross-Scale 详细数字移入 Appendix，正文保留核心结论；(2) §5 Discussion 与 Conclusion 合并，删除与 §4 重复内容（OR=3.48 描述、bifurcation 描述、H7b triple gaming 均多处重复）；(3) §3.3 reward conditions 描述压缩。

**W2 [共识, critical] "Inevitable collapse at all tested doses" 超出证据支撑**
论文核心 claim（C2）反复使用 "β controls when collapse occurs, not whether" 和 "inevitable at every tested dose"。但 trajectory evidence（β=0.1 transient window 关闭: 17.3%→2.2%）仅基于 s42 **单一 seed** 延伸至 1000 步。s45/s46 未延伸。Introduction 写 "trajectory analysis confirms all seeds converge" 是未验证 claim。
结构性论证（H7 ISR≥0.5 by definition → positive feedback loop）合理但属于定性推测，"inevitable" 是需要更强证据的绝对量化 claim。β=0.05 (3 seeds H7 93.7%) 和 β=0.2 (3 seeds 100% collapse) 提供辅助证据，但不能替代 β=0.1 下的 multi-seed extended trajectory。
→ 修复：(a) 延伸 s45/s46 至 1000 步；或 (b) 将 "inevitable" 软化为 "observed under all tested conditions/extended trajectories"。

**W3 [共识, critical] OR=3.48 (ISR genuine benefit) 在 H8+FN 校正后反转，主文 framing 信息不对称**
5-seed uncorrected: ISR 22.6% vs Random 7.7%, OR=3.48, p<10⁻⁸。3-seed H8+FN corrected: ISR 6.06% vs Random 9.5%, **OR=0.61, p=0.182 n.s.**（方向反转）。ISR s43/s44 checkpoints 已删除无法 H8 audit；s45/s46 未 audit。s42 单 seed head-to-head: ISR 17.3% vs Random 22.8%（同样反转）。主文/Abstract 以 OR=3.48 为 headline，校正结果仅在 Appendix。
→ 修复：主文 Table 1 或正文中并列报告两个版本；Abstract/Introduction 使用 upper-bound 措辞或同时呈现。

**W4 [R1 提出, R2 同意, critical] Pooled Fisher exact test 忽略 seed-level clustering，p-values 被 inflate**
所有统计检验使用 pooled samples (ISR n=350, Random n=414) 做 Fisher exact test，但同 seed 内样本高度非独立（ISR s43: 61/61 H7, s44: 89/89 H7）。有效样本量远小于名义值。以 seed 为分析单元 (n=5 vs n=5)，p<10⁻⁸ 不可能达到。R2 补充：核心定性结论（ISR 增加 H7 prevalence）不依赖 p-value，但统计呈现误导。
→ 修复：补充 seed-level 分析（CMH test / mixed-effects logistic / permutation test）；如不显著则调整 confidence 表述。

### Warning（影响评分但不一票否决）

**W5 [共识, warning] 未测试 tautology-guarded ISR 变体**
论文声称 ISR 的 structural bias (H7 ISR≥0.5) 使 collapse inevitable。但未测试自然的 fix：n_comp≤2 或 text-match(premise,conclusion) 时设 ISR=0。O(1) variant (Appendix) confound 了 ablation 粒度和 tautology 检测，不等同。无论 guarded ISR 是否仍被 game，结果都有信息量：若仍 collapse 则加强 claim，若不 collapse 则 claim 需修正。

**W6 [共识, warning] 1.7B cross-scale 实验仅 single seed**
"Capacity-dependent Goodhart basins" 和 "no safe scale exists" 基于 seed 42 一个 seed。4B 实验清楚表明不同 seeds 产生质的不同 hacking 模式。Limitations 有段落但 Discussion 措辞仍比 Limitations 更强。

**W7 [共识, warning] Seed 43 exec-only 评估协议存在文本矛盾**
Appendix A.1: "evaluated with sampling (T=0.7)"。Table 6 Notes 列: "†Greedy (n_proved=13)"。同一 † 标记语义矛盾，读者无法判断实际评估方式及哪些数字来自哪种方式。

**W8 [共识, warning] Deleted checkpoints (ISR β=0.1 s43/s44) 削弱复现性和 H8 audit 完整性**
Appendix 承认但主表未标注。第三方无法验证这两个 seed 的 non-hacking 分类。non-hacking rate "may be overestimated"。

**W9 [R2 提出, R1 部分同意, warning] 方法新颖性有限**
Algorithm 1 仅 6 行伪代码，ISR 是 LOO necessity fraction 的直接应用。论文自己承认 "LOO ablation itself is standard"。贡献定位为 empirical findings 而非方法创新（R1 认为以 findings 价值衡量是合理的），但 EMNLP main track 仍对方法深度有一定期待。论文价值高度依赖经验发现的新颖性和影响力是否达到 bar。

**W10 [R1 提出, R2 同意, info→warning] 100 eval samples 对 per-seed claims 统计功效不足**
β=0.3 s42 仅 n=18 proved samples，SFT 每 seed 约 11-15。基于 n=18 报告百分比的 Wilson 95% CI 极宽（[0.3%, 27%]）。Per-seed 百分比缺 CI。

---

## Reviewer Consensus

以下 critical/warning issues 两位 Reviewer 独立发现并在交叉回应中确认 [AGREE]：

| Issue | R1 | R2 | 最终判断 |
|-------|----|----|----------|
| 正文超页 ~2.5p | [AGREE] (补充确认) | N1 (首发) | **critical** |
| "inevitable" 超证据 | N1 (首发) | W1→[AGREE] | **critical** |
| OR=3.48 校正后反转 | N2 (首发) | W2→[AGREE] | **critical** |
| Pooled Fisher clustering | N3 (首发) | [AGREE] (severity 略低) | **critical** |
| 1.7B single seed | W1 | N3→[AGREE] | **warning** |
| Seed 43 eval 矛盾 | W2 | W4→[AGREE] | **warning** |
| Deleted checkpoints | W5 | [AGREE] | **warning** |
| Tautology-guarded ISR 未测试 | [AGREE] | W5 (首发) | **warning** |

## Reviewer Divergence

| Issue | R1 | R2 | 分歧性质 |
|-------|----|----|----------|
| 方法新颖性 | "empirical study, findings 价值更重要" | "critical: 方法深度不够 main track" | R1 认为 warning, R2 认为 critical → 折中为 warning |
| SFT PR confound | W3 (warning) | [REBUT]: 100-step 已控制 | R2 论证更有说服力 → 保留为 minor concern |
| Figure 2 cherry-picking | minor issue | [REBUT]: 仅 s42 有 3 checkpoints | R2 反驳有效 → 不列为 issue |
| DeepSeek-R1 引用 | [REBUT]: 非必要 | 建议引用 | R1 论证合理 → nice-to-have |

---

## Questions（需作者澄清）

**Q1.** 是否计划延伸 s45/s46 至 1000 步验证 "inevitable collapse"？如果不延伸，如何支撑 "all seeds converge" claim？

**Q2.** 为什么主文以 5-seed uncorrected OR=3.48 为 headline 而非 3-seed corrected OR=0.61 (n.s.)？两个数字哪个更能代表真实效果？

**Q3.** 是否考虑过 seed-level 统计检验（CMH test, permutation test, mixed-effects model）？以 seed 为单元时 ISR vs Random 差异是否仍显著？

**Q4.** Seed 43 exec-only 的实际评估协议是什么？Appendix A.1 ("sampling T=0.7") 与 Table 6 Notes ("†Greedy") 的矛盾如何解释？

**Q5.** ISR β=0.1 仅看 s42（唯一完整 H8 audit + 未崩溃）：non-hacking 17.3% vs random s42 22.8%，方向反转。这是否说明 ISR 的 per-proof benefit 不存在？

---

## Missing References

- 其他 formal verification RL 中的 reward gaming 实例（如 Lean/Isabelle proof RL 中的 trick proofs），如有文献应引用加强 Related Work
- METR reward hacking 引用缺 URL 和访问日期（@misc 类型）

---

## External Review (Stanford Agentic Reviewer)

未配置。项目未启用 `external_review.paperreview_ai`。

---

## Overall Assessment

**评分: 3.0 / 5 — Findings acceptance (borderline)**
**置信度: 4 / 5**

两位 Reviewer 一致评分 3.0，推荐 Findings 而非 Main Conference。

**核心判断**：论文研究了一个重要问题，核心现象（ISR 作为 diagnostic 揭示 exec-only collapse）solid，实验覆盖面广（6 conditions × 2 logics × 2 scales × 5 seeds），方法论诚实度罕见。但存在 4 个相互强化的 critical 问题：

1. **格式硬伤**：正文超页 ~2.5 页（desk-reject 级别）
2. **核心 claim 超出证据**："inevitable collapse" 的 extended trajectory evidence 仅 1 seed
3. **统计呈现偏向乐观**：OR=3.48 在校正后消失（OR=0.61 n.s.），但主文以未校正数字为 headline
4. **统计方法不当**：pooled Fisher test 忽略 seed clustering，p-values 被严重 inflate

这 4 个问题指向同一 meta-concern：**论文的统计 claims 系统性地偏向乐观方向**（选择 5-seed uncorrected numbers、pooled rather than seed-level tests、single-seed trajectory extrapolation）。论文的诚实度体现在 Appendix 中全部 disclosed 了这些 caveats，但主文 framing 未充分调整。

**升级路径**（升至 weak accept / 3.5-4.0）：
1. 修复超页（硬性要求，否则 desk reject）
2. 补充 s45/s46 extended trajectory 或软化 "inevitable" claim
3. 主文中并列报告 corrected statistics（OR=0.61）
4. 补充 seed-level 统计分析
5. （可选但高价值）测试 tautology-guarded ISR

---

## Detailed Comments（逐节）

### Abstract
- "effectively zero structurally sound outputs at convergence" 措辞改进（v3 issue 已修复）
- OR=3.48 应标注为 uncorrected upper bound 或并列 corrected result

### Introduction
- "trajectory analysis confirms all seeds converge"（line 33）——仅 s42 有 1000-step 数据，此 claim 不成立
- Contributions C2 中 "inevitable" 措辞需与证据对齐

### Method
- §3.2 premise-count confound 讨论充分（从 Appendix 提升到正文是好的改进）
- LOO vs Shapley 讨论合理
- §3.3 可压缩以帮助解决超页

### Experiments
- Table 1: ISR β=0.1 ISR* "omitted" 但其他条件正常报告，标准不统一
- Table 1 footnote ★ "transient" 应更显著标注 uncorrected nature
- §4.2 Figure 2 仅 s42（有数据原因但建议增加 multi-seed 对比）
- §4.3 pooled statistics 需补充 seed-level 分析
- §4.4/§4.5 详细数字可压缩至 Appendix

### Discussion/Conclusion
- 与 Experiments 大量重复——合并压缩是解决超页的主要手段
- "no safe scale exists" 需加 "single-seed observation" 限定

### Limitations
- 当前版本比 Round 2 显著改善
- 1.7B single-seed 段落已存在但 Discussion 措辞更强——需要一致性

### Format
- ACL template [review] ✓
- Double-blind ✓（author = "Anonymous ACL submission"）
- Limitations section 位置正确 ✓
- Ethics statement 存在 ✓
- 正文超页 ✗（~10.5 pages，最严重的格式问题）
