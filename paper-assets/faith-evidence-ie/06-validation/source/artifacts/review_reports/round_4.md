---
round: 4
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-25T23:04:05.281208+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 4 审稿报告（修订版——整合双向交叉回应）

## Summary

本文研究 evidence-grounded document-level relation extraction 中不同训练范式（SFT/RSFT/GRPO/DPO）对 RE-evidence coupling 的影响。在 Qwen3 (1.7B–14B) 和 LLaMA-3.1-8B 上进行系统比较。核心发现：(1) evidence tax 是 scale-dependent 的（1.7B 有益，≥4B 近中性）；(2) gradient-based 方法导致 evidence-extraction decoupling，而 RSFT 通过 output filtering 维持 coupling；(3) EDCR 作为 diagnostic metric 量化 decoupling 程度。论文定位为实证研究。

## Round 3 → Round 4 改进确认

以下 Must-Fix/Should-Fix 已确认修复：
- ✅ **页数限制**（R3-FMT）：正文 8 页内，Conclusion 压缩至 2 句。PDF 已验证。
- ✅ **EDCR ρ 一致性**（R3 W-SF5）：统一为 −0.96（cross-method, n=7）/ −0.79（per-relation, n=76）。
- ✅ **RSFT seed protocol 透明化**：§3.3 明确声明 primary experiments 共享 SFT s42 checkpoint。
- ✅ **Variance 降级为 observation**：Contribution 3 添加 shared SFT initialization 和 n=3 caveats。
- ✅ **Evidence tax sign convention**：全文统一 Tax = no-evi − with-evi; positive = cost。
- ✅ **Spectrum 限制**：Limitations 声明 spectrum 仅 4B 验证。
- ✅ **CED 定位**：正确定位为 scoring variant，0.02pp 诚实报告，无 contribution language。
- ✅ **DeepSeek-R1 + ReST 引用**：已添加。
- ✅ **bf16 G=4 控制实验**：已新增（Rel-F1 28.73）。

## Strengths

1. **系统实验覆盖广泛**：5 model scales × 4 训练范式 + cross-architecture (LLaMA) + cross-dataset (Re-DocRED) 验证，evidence-grounded DocRE 领域最全面的实证比较。

2. **Decoupling spectrum 有洞察力**：按 RE-evidence coupling 程度排列训练方法的 conceptual framework 为社区提供有用参考。

3. **Evidence tax 量化有实用价值**：training-time 和 inference-time 双维度分离，matched@2048 fair evaluation 方法严谨。

4. **实验设计周全**：random selection baseline、matched@2048 evaluation、no-evidence SFT、CED vs flat-NLI、DeBERTa base vs large ablation。

5. **EDCR 验证扎实**：per-relation 分析 (n=76, ρ=−0.79)、partial correlation、permutation test、similar-TP pairs——R1 确认 EDCR 是纯 annotation-based 指标（不使用 NLI），验证链完整且独立。

6. **可复现性强**：代码+数据开源承诺，hyperparameters 详尽，seed protocol 透明。

## Weaknesses

### Must-Fix（两位 Reviewer 共识）

**[W-MF1] DPO β=0.1 单点实验——连续 4 轮未解决**
- DPO β=0.1 导致 Rel-F1 从 44.39 暴跌至 33.37（−11pp），高度可能是超参选择导致
- DPO 文献中 β=0.01-0.05 常用，避免过度偏离 reference policy
- 整个 decoupling spectrum 的 DPO 段（"gradual decay"）建立在单一 β 值上
- R1 补充：RSFT k=1 也是最激进的过滤策略——k=3/k=5 可能有不同 extraction-evidence balance。缺少这些消融，无法区分"方法固有属性"和"特定超参下的行为"
- **要求**：β∈{0.01, 0.05} sweep 或将所有 DPO 结论限定为 "under β=0.1"
- *[R1, R2 强烈共识 — 4 轮 recurring, 升级为 Must-Fix]*

### Should-Fix（两位 Reviewer 共识）

**[W-SF1] Evidence tax 1.7B 核心效应是 truncation artifact，framing 过度简化 ⚠️ NEW**
- **R1 称此为"本轮最有力的批评"**，R2 首提，R1 cross-response 强烈同意
- 论文自己的 Appendix E：matched@2048 fair evaluation 控制 truncation 后，1.7B tax **反转为 −5.63pp（beneficial）**；≥4B 近中性 (+0.25±0.47pp)
- Appendix K：truncation FN 是 RSFT 改进的首要机制（1.7B: −22% truncation FN reduction）
- 这意味着 Abstract/Contribution 1 宣称的 "scale-dependent evidence tax" 在 1.7B（效应最显著的规模）**实质是 truncation/format compliance artifact，非 evidence 固有代价**
- 论文将此关键 nuance 埋在 Appendix E，正文 §4.4 仅一笔带过
- **要求**：(1) 在正文 §4.4 区分 "truncation-induced tax" 和 "information-interference tax"；(2) 将 matched@2048 的关键发现从附录提升到正文显著位置；(3) 修订 Contribution 1 framing，承认 1.7B benefit 主要来自格式约束效应
- *[R1 强烈同意 R2 — 双向交叉确认]*

**[W-SF2] GRPO bf16 G=4 暴露 group size + lr confound**
- bf16 G=4（Rel-F1 28.73）vs bf16 G=8（45.49）= 16.76pp drop → group size 有显著影响
- QLoRA G=8 (lr=5e-6) vs bf16 G=8 (lr=5e-5) 学习率差 10×，非 "residual confound"
- §4.3 "attributable to quantization precision" 仍过强
- **要求**：弱化归因语言；显式讨论 lr 10× 差异；承认 group size 非trivial 贡献
- *[R1, R2 共识 — 从 Must-Fix 降级为 Should-Fix，因 bf16 G=4 部分回应]*

**[W-SF3] Variance "observation" 在文中篇幅与其证据力度不匹配**
- §4.4 仍用 ~250 words + 精确 ratio (32.6×, 7.5×, 6.5×) + "36× more predictable"
- sign test p=0.0625 不显著；Cohen's d=0.46 at 4B = small effect
- **要求**：压缩至 2-3 句，精确 ratio 移至 appendix，移除 "predictable" 措辞
- *[R1, R2 共识]*

**[W-SF4] "Implicit regularization" 仍未按 R3 共识重命名**
- §4.4 和 Appendix E 仍使用 "implicit regularization hypothesis"
- R1 cross-response进一步指出：结合 W-SF1 的 truncation-mediation 发现，所谓 "regularization" 实质是格式约束效应，非 learning effect
- **要求**：替换为 "structural output constraint"；增加 matched@2048 counter-evidence 讨论
- *[R1, R2 共识 — R3 carry-over, 被 W-SF1 进一步强化]*

**[W-SF5] RSFT "cannot exploit trade-off" 缺实证**
- §G 仍为纯 structural argument，无实验验证
- R1 补充：RSFT k>1 ablation 也是理解 discrete selection 机制的必要实验
- **要求**：完成 single-objective RSFT 或降级为 hypothesis
- *[R1, R2 共识 — R3 carry-over]*

**[W-SF6] Method-innovation 语言残留**
- Contribution 2: "introduce the EDCR as a diagnostic"
- §3.5: "we define the EDCR"
- R1：应将 RSFT 的角色明确为 "empirical finding: discrete selection avoids decoupling" 而非暗示方法新颖性
- **要求**："introduce" → "use"/"employ"；"define" → "compute"/"measure"；Contribution 3 reframe 为 empirical finding
- *[R1, R2 共识]*

**[W-SF7] §4.4 信息密度过高**
- R1 同意 R2：§4.4 在 ~1.5 页内叠加 tax 定义、scale-dependency、CI 分析、cross-seed variance、cross-architecture、inference-time tax
- CI-crosses-zero 这个关键 caveat 容易被淹没
- **要求**：拆分为 §4.4 Evidence Tax（含 CI）和 §4.5 Cross-Scale Patterns；或压缩 variance 部分
- *[R1, R2 共识]*

**[W-SF8] 14B test-set reversal 仍缺 precision/recall 分解**
- 14B: SFT truncation 50.6% vs RSFT 13.4%；dev +2.78pp → test −0.37pp
- R1 补充：14B 高 cross-seed variance + 仅 1 SFT seed，evidence tax 在更大规模可能不稳定
- **要求**：precision/recall 分解或显式承认 single-SFT-seed 限制
- *[R1, R2 共识 — R3 carry-over]*

### Minor Issues

| ID | 问题 | 共识 |
|---|---|---|
| M1 | SFT no-evidence 1.7B/8B 仅 s42；1.7B s42 是最强 seed | AGREE |
| M2 | "co-optimization" 和 "joint optimization" 术语未统一 | AGREE |
| M3 | matched@2048 定义在 Appendix E，§4.4 引用时读者需翻附录 | AGREE — 至少加一句定义 |
| M4 | Figure 4 dual y-axis 视觉误导（Rel-F1 40-55 vs Evi-F1 0-90 range）| AGREE — 建议并排子图 |
| M5 | CED template sensitivity / NLI model family 测试有限 | AGREE — 影响小 |
| M6 | BM25 k=2 未 justify | AGREE |
| M7 | Re-DocRED test 20pp drop 缺定量统计支撑（dev vs test annotation density）| AGREE |
| M8 | Figure 10 (Appendix) 色盲不友好 | AGREE — minor |

## Reviewer Consensus

两位 Reviewer 在以下问题上达成完全共识 [AGREE]：

1. **DPO β 单点**：4 轮 recurring，升级为 Must-Fix。无法区分 method property 和 hyperparameter artifact
2. **Evidence tax truncation-mediation**（NEW）：1.7B 的 evidence tax 主要是 truncation artifact。R1 称为 "本轮最有力的批评"
3. **n=3 seeds 统计效力**：variance evidence 不足，observation 定位正确但文本过冗长
4. **GRPO attribution**：bf16 G=4 部分回应，但暴露 group size effect + lr confound
5. **Implicit regularization**：R3 共识未执行，被 truncation-mediation 发现进一步削弱
6. **Method-innovation 语言**："introduce"/"define" 暗示 novel contribution
7. **EDCR 验证扎实**：R1 确认 EDCR 是纯 annotation-based 指标，per-relation 验证链完整

## Reviewer Divergence

**[W-DIV1] RSFT variance 比较的方法论公平性**
- **R2 部分反驳 R1**：end-to-end variance 比较有实践价值（practitioner 关心 pipeline 稳定性）
- **R1 坚持**：方法论不对称（SFT = full pipeline, RSFT = fine-tuning stage only）
- **Director 判定**：R2 practical argument 有道理，但精确 ratio 和 "predictable" 措辞削弱 caveat。**WARNING — 压缩 variance 讨论。**

**[W-DIV2] Conclusion 长度**
- **R2**：列为 critical（过短，无 broader implications）
- **R1 反驳**：Conclusion 长度是写作偏好；broader implications 在 §4.7 Discussion 中讨论；ARR 评分标准不含 conclusion 长度
- **Director 判定：Minor** — R1 论点更有说服力。简短 conclusion 不影响 soundness。可选扩充 2-3 句 future directions。

**[W-DIV3] EDCR-CED circular dependency**
- **R2 原始意见**：EDCR 和 CED 共享 NLI backbone，存在 circular dependency
- **R1 反驳（factual correction）**：EDCR（Eq. 2）是纯 annotation-based 指标（gold vs predicted evidence 集合差运算），**完全不使用 NLI**。CED（§3.4）使用 DeBERTa-v3 NLI。两者无共享组件。R2 混淆了 EDCR 和 CED。
- **Director 判定：R1 正确。** R2 此条为事实性错误，不纳入报告 weakness。EDCR 验证链完整且独立。

**[W-DIV4] "Evidence tax" 术语**
- **R2**：术语不直观，建议改为 "evidence delta"/"evidence impact"
- **R1 反驳**：Tax 是标准隐喻（"abstraction tax"、"safety tax"），negative tax = benefit 符合直觉。"Delta" 方向中性，丢失核心叙事
- **Director 判定：R1 正确。** 术语选择合理，不需更改。

## Questions for Authors

1. bf16 G=4 实验的学习率是多少？如与 bf16 G=8 相同 (5e-5)，则 16.76pp drop 纯粹由 G 导致。
2. DPO β=0.01 或 β=0.05 实验是否在进行中？已持续 4 轮。
3. Single-objective RSFT / RSFT k>1 ablation 结果？
4. 14B precision/recall 分解数据？
5. Appendix E matched@2048 结果何时提升到正文？这是 evidence tax framing 的关键 nuance。

## Missing References

| 引用 | 理由 | 共识 |
|---|---|---|
| Yu et al. 2020 (PCGrad) | 梯度手术解决 multi-task gradient conflict，直接关联 §4.3 gradient pressure 讨论 | R1 AGREE |
| Rashkin et al. 2023 (Attribution) | NLG 中的 attribution 与 evidence citation 有概念对应 | R1 AGREE |
| ~~Maynez et al. 2020~~ | R1 反驳：abstractive summarization faithfulness 与 DocRE evidence 关联较远 | R1 REBUT |

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 本轮未启用外部审稿。

## Visual Layout Check（非评分项）

**状态：已完成** (耗时 ~3.5 分钟)

| 严重性 | 位置 | 发现 |
|---|---|---|
| ℹ️ | p5 | Figure 3 (CED scoring) 内部文字偏小（正文 60-65%），建议 ≥70% |
| ℹ️ | p7 | Figure 4 图例文字偏小，在绘图区域内部 |
| ℹ️ | p12 | Appendix 单页含 4 张表，信息密度极高（格式正确） |
| ℹ️ | p17 | Figure 7 三子图 y 轴标签偏小 |
| ℹ️ | p18 | 末页约 25% 空白（Appendix 末页） |
| ✅ | p2 | Figure 1 清晰专业 |
| ✅ | p6 | Table 2 booktabs 规范 |
| ✅ | p8 | Figure 5 红/蓝对比清晰 |

**0 critical, 0 warning, 8 info** — 排版质量良好。Figure 1 在 p2，解决了 Round 2-3 的 "文字墙" 问题。

## Overall Assessment

**评分：3.5 — Borderline Conference**

| 维度 | 评分 | 说明 |
|---|---|---|
| Soundness | 3 | DPO spectrum 建于单一 β（4 轮未解决）；evidence tax 1.7B 核心效应是 truncation artifact 而非 evidence cost（framing gap）；GRPO attribution 有 confound；variance 统计力度不足 |
| Excitement | 3 | Decoupling spectrum 有启发性；evidence tax truncation-mediation 机制的发现有价值（若正确 frame 的话）；novelty 在 empirical coverage 而非 method |
| Reproducibility | 4 | 代码+数据开源承诺，hyperparameters 详尽，seed protocol 完全透明 |
| Clarity | 3.5 | 格式问题大部分已修复；但 §4.4 密度过高、variance 段过长、implicit regularization 未重命名、evidence tax 关键 nuance 埋在附录 |
| Overall | 3.5 | Borderline Conference |

**置信度：4/5** — 两位 Reviewer 双向交叉回应完成，核心问题高度一致。4 条分歧中 2 条为 R2 factual error（已纠正），1 条为 writing preference（不影响评分），1 条 Director 裁定 WARNING。

**推荐决定**：
- **当前状态 → Borderline Conference (3.5)**：格式显著改善，多个 R3 Must-Fix 已修复。但 DPO β 4 轮 recurring + evidence tax framing gap（truncation-mediation 发现未反映在正文）+ GRPO attribution confound + RSFT "cannot exploit" 缺实证——这些问题阻碍 Conference (4.0) 评分。
- **修复后 → Conference (4.0)**：如果 (1) DPO β sweep 或 scope limitation、(2) evidence tax framing 整合 truncation-mediation、(3) implicit regularization 重命名、(4) variance 压缩 + method-innovation 语言清理、(5) §4.4 密度降低——论文可达 Conference。empirical coverage 和 EDCR 验证基础扎实。
- **关键阻碍**：DPO β（4 轮未解决，需实验数据）和 evidence tax framing（需 writing 重组，将 Appendix E 关键发现提升到正文）。

## Detailed Comments

### §1 Introduction
- Contribution 1："scale-dependent evidence tax" 在 1.7B 的核心效应是 truncation-mediated → 需修订 framing
- Contribution 2："introduce EDCR" → 改为 "use"/"employ"
- Contribution 3：已降级为 observation ✓，但 "RSFT improves extraction without decoupling" 仍读如 method contribution → reframe 为 empirical finding

### §3 Method
- RSFT seed protocol 透明 ✓
- §3.4 CED：effort-vs-payoff 最失衡部分（大量篇幅描述 contrastive design，0.02pp 差异）— R1+R2 均指出
- §3.5 EDCR：R1 确认验证链完整，R2 的 circular dependency 担忧为事实性错误
- EDCR = 纯 annotation-based 指标，不使用 NLI backbone

### §4 Experiments
- §4.2："different sources of variation" caveat ✓，但精确 ratio 和 "predictable" 削弱
- §4.3：bf16 G=4 新增 ✓；"attributable to quantization precision" 过强；lr 10× 非 "residual"
- §4.4：信息密度过高（R1+R2 共识）；evidence tax matched@2048 关键 nuance 埋在附录；"implicit regularization" 被 truncation-mediation 发现进一步削弱
- §4.5：BM25 k=2 缺 justification

### §5 Conclusion
- 2 句，符合 8 页 ✓
- R2 认为过短 (critical)，R1 反驳（writing preference），Director 判定 Minor

### Limitations
- 覆盖 data/architecture scope、CED sensitivity、RSFT mechanistic ✓
- Spectrum 仅 4B ✓
- 未提及 DPO β single-point limitation（应补充）

### Appendix
- §E/F：matched@2048 和 truncation analysis 是论文最有价值的分析之一，但被埋在附录——需提升到正文
- §G："cannot exploit" 仍为 structural argument
- Appendix K：evidence quality unchanged (Δ<0.4pp) 与 "implicit regularization" framing 矛盾

---

*本报告由 2 位 Reviewer 独立审稿 + 双向交叉回应后合成。R1 cross-response 纠正了 R2 的 1 条事实性错误（EDCR 不使用 NLI），并强化了 evidence tax truncation-mediation 为本轮核心新发现。4 条分歧已裁定。Overall 评分一致：3.5 Borderline Conference。*