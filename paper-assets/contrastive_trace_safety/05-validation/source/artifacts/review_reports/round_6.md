---
round: 6
overall_score: 3.0 - Findings
timestamp: 2026-05-18T04:30:08.915179+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 7 (Fresh Review)

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle, Findings track)
**审稿日期**: 2026-05-18
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）

---

## Summary

本文研究推理模型中 Safety Commitment Point 的检测，比较 hidden-state (HS) 探针与 text 探针。核心方法论发现：layer 选择标准（包含 crossing rate 的复合指标）系统性地为 32B 模型选择浅层，掩盖 HS 优势；校正后（深层），HS 探针在 4 个模型上显著优于 MiniLM-384d text 探针（12 项 Holm-Bonferroni 测试通过）。七种替代方法均未稳定匹配 supervised probing。

---

## Strengths

1. **层选择敏感性发现有方法论价值**: 一个指标组件（crossing rate）可以逆转研究结论（5/12→12/12 HB pass），对 probing 社区有普遍警示意义。[R1 E1, R2 partial agree]
2. **统计处理严谨**: Holm-Bonferroni、null-centered bootstrap、control task selectivity (Hewitt framework)、PCA dimensionality matching。评估协议设计合理。[R2 Strength 1]
3. **科学诚信突出**: Bug disclosure (Appendix F)、Limitations section 全面坦诚（7 段）、QwQ-32B position baseline competitive 的承认、高 FPR 的坦率报告。[R1 E3, R2 Strength 2]
4. **实验覆盖面广**: 4 模型 × 2 架构 × 2 scale，7 种替代方法，多个 ablation（window、PCA、encoder robustness）。Negative results 有 per-method failure analysis。[R1 E2, R2 Strength 3]
5. **问题定义清晰**: Safety Commitment Point 形式化和 temporal probing framework 为后续工作提供清晰基准。[R2 Strength 4]
6. **格式完全合规**: ACL [review] 模板、8 页正文、行号、匿名、Limitations、Responsible NLP Checklist 完整。[R2 Strength 5]

---

## Weaknesses (Must-Fix)

### W1 [critical, consensus] HS 优势高度依赖弱 text baseline，核心 claim scope 过强

BGE-large (1024d) 替换 MiniLM (384d) 后，仅 OT-7B 通过 Holm-Bonferroni (p<0.001)，R1-8B p=0.185, QwQ-32B p=0.132, R1-32B p=0.027 均未通过。Contribution 2 标题 "directional consistency against a stronger encoder" 是极弱的 claim 但被作为 contribution-level 论断。HS 优势是 encoder-conditional 的——如果使用更强或 domain-adapted encoder，优势可能完全消失。

**要求**: BGE-large 结果并列呈现于主表（非附录 robustness check）; Contribution 2 重写为 "HS advantage over 384d encoder with diminishing effect against stronger encoders, encoder-conditional in nature"。

### W2 [critical, consensus] 32B 模型证据过弱，"all four models" 为 overclaim

R1-32B: 仅 W=1 通过 HB，coverage 25%（5/20 traces），有效样本 n=5 上 bootstrap 推断无统计意义。QwQ-32B: position-only baseline BA 0.746 > HS 0.740，lead time 负值。Abstract "significantly outperform on all four models" 未附限定。两个 32B 模型各有致命弱点（R1-32B 窄覆盖，QwQ-32B 位置竞争），32B 层面 HS advantage 的 claim 整体不成立。

**要求**: 主文和 Abstract 中明确区分 7-8B（robust evidence）和 32B（pilot-scale/exploratory evidence）; "All four models" claim 限定为 "at W=1"; 报告 QwQ-32B position baseline 的 precision 和 FPR; 考虑 exact permutation test 替代 bootstrap。

### W3 [critical, consensus] K=5 consecutive crossings 阈值缺乏依据和消融

检测 CP 需 K=5 连续穿越，但无理论依据、无验证集选择说明、无 K 消融。Table 6 (Appendix) 使用 K=1，主文使用 K=5，不同评估标准下 coverage 不可比。K 直接影响 precision-coverage tradeoff，R1-32B 25% coverage 在 K=3 或 K=1 下可能完全不同。消融成本极低但未做。

**要求**: K ∈ {1, 3, 5, 7, 10} 消融; 明确 K 选择依据; 统一或明确标注不同表格的 K 值。

---

## Weaknesses (Should-Fix)

### W4 [warning, consensus] Holm-Bonferroni positive dependence 论点重复 6-7 次

"The correction is stricter under positive dependence than under independence" 在 Abstract、Introduction、Section 3.3、4.2、4.3、Discussion、Conclusion、Appendix B 中几乎原封不动出现。技术正确但修辞上 defensive，给审稿人不良印象。

**要求**: Method 或 Appendix B 中解释一次，全文其余处删除。

### W5 [warning, consensus] 窗口选择 + 层选择在同一小验证集上连续调优

Layer、W、threshold 三个超参数均在同一验证集上选择。32B 验证集仅 19-20 条 trace。C insensitive (<2pp) 但未讨论 W 和 layer 联合选择的过拟合风险。

**要求**: 明确报告是否同一验证集; 讨论过拟合风险; 考虑 nested CV 作为敏感性检查。

### W6 [warning, consensus] 60/20/20 单次分割缺多 seed 稳定性验证

LR 核心结果基于单次 split。GRU Table 8 已展示跨 seed 高方差（lead time std=3.16）。LR 训练几秒钟，3-5 seeds 几乎零成本。

**要求**: 至少 3 个 random seeds 重复核心 LR 实验，报告 mean±std。

### W7 [warning, consensus] Abstract 信息过载 (251 words)

塞入 HB correction 细节、α=0.05、n 值、crossing rate 解释。读起来像压缩 Results 而非 story。审稿人 30 秒内无法判断论文价值。

**要求**: 重写为 problem→insight→finding→implication 叙事结构，删除统计细节，保留 2-3 关键数字，≤200 words。

### W8 [warning, consensus] 遗漏 4 篇直接相关的 2025-2026 工作

1. "Do Internal Layers of LLMs Reveal Patterns for Jailbreak Detection?" (arXiv 2510.06594) — layer-wise jailbreak detection
2. "Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation" (arXiv 2503.11926, Baker et al.) — CoT monitoring + obfuscation risk，明显遗漏
3. "Refusal Falls Off a Cliff" (arXiv 2510.06036) — reasoning model 中 refusal 退化
4. "Linear probes rely on textual evidence" (arXiv 2509.21344) — 质疑 linear probe 是否捕获真正结构

### W9 [warning, consensus] 39-52% safe-trace FPR 与 Introduction deployment 叙事不匹配

Introduction 强调 "monitoring systems that must intervene"，但实际每两条安全 trace 误报一条。Section 4.3 承认是 characterization tool，但 Introduction 未设预期。

### W10 [warning, consensus] 五指标消融存在部分循环论证风险

"深层结果更好 → 选深层的指标 correct → 选浅层的 biased"。Control task selectivity (L10=7.5pp → L63=19.7pp) 提供了独立验证，但缺少浅层 volatility 的直接度量（如 step-to-step cosine distance）。

### W11 [warning] GRU 70/30 split 与主实验 60/20/20 不一致

论文已提供 Table 8 的 60/20/20 控制实验，但不够显眼。主文应直接引用。

### W12 [warning] fig3_model_dependency.pdf 存在但全文未引用

figures/ 目录中存在但全文无引用。应引入正文或从提交材料删除。

### W13 [warning] 正文图表过少 (1 Figure + 5 Tables)

缺 layer sweep 可视化（per-layer metric heatmap across 4 models）展示 biased vs corrected 层对比。核心论点仅通过数字传达。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 独立提出或交叉确认达成完全共识：

1. **HS advantage encoder-conditional** (R2-N1, R1 AGREE): BGE-large 后仅 1/4 HB pass
2. **32B evidence pilot-scale** (R1-N1, R2-N2 AGREE): n=19-20, R1-32B 5 effective samples
3. **"All four models" overclaim** (R1-N1+N2, R2-N2+W4 AGREE): 两个 32B 模型各有致命弱点
4. **K=5 no ablation** (R1-N3, R2 AGREE): 成本极低但未做
5. **HB repetition** (R1-W3, R2-W5 independent): 6-7 次几乎相同措辞
6. **Bootstrap small sample** (R1-W1, R2 AGREE): n=5 effective samples 无意义
7. **Single split instability** (R1-W5, R2 AGREE): GRU variance 证明问题存在
8. **Missing references** (R2-W2, R1 AGREE): Baker et al. 2503.11926 为明显遗漏
9. **FPR-narrative mismatch** (R2-W3, R1 AGREE)
10. **Abstract overloaded** (R2-W1, R1 AGREE)

## Reviewer Divergence [REBUT]

**Layer selection novelty as "central finding"**:
- **R2 position**: Mechanistically straightforward ("crossing rate rewards volatility" 一旦发现就显而易见)。缺跨 task 验证和理论分析。不足以作为 central finding。
- **R1 position**: Post-hoc 直觉性 ≠ ex-ante 显而易见性。关键贡献是后果严重性（逆转研究结论），而非机制复杂度。但同意需要通用性验证。
- **Director 判断**: 作为 Findings-level 论文的 primary methodological finding 是够格的；作为主会议 central contribution 则需要跨 task 验证来支撑。不阻碍 Findings 接收。

---

## Questions

1. K=5 如何确定？对 K ∈ {1,3,5,7,10} 的敏感性如何？
2. QwQ-32B position baseline 的 precision 和 FPR 是多少？
3. 是否有直接度量浅层 vs 深层 step-to-step representation volatility 的证据？
4. 85.5% oracle gap 仅基于 R1-8B，其他模型如何？
5. Multi-layer ensembling 是否能缓解 layer selection sensitivity？
6. 如果用 domain-adapted text encoder，HS advantage 是否消失？
7. 是否做过 cross-validation 或多次分割的稳定性检验？

---

## Missing References

1. Baker et al. "Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation" (arXiv 2503.11926) — **高度相关，明显遗漏**
2. "Do Internal Layers of LLMs Reveal Patterns for Jailbreak Detection?" (arXiv 2510.06594) — layer-wise safety probing
3. "Refusal Falls Off a Cliff: How Safety Alignment Fails in Reasoning" (arXiv 2510.06036) — reasoning model refusal dynamics
4. "Linear probes rely on textual evidence" (arXiv 2509.21344) — probe validity
5. Hochberg (1988) "A sharper Bonferroni procedure" — 量化 HB 保守性
6. Hesterberg (2015) "What Teachers Should Know About the Bootstrap" — 小样本 bootstrap 局限

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿。

---

## Overall Assessment

**Score: 3.0 / 5 — Findings**

| Reviewer | Score | Post-Cross Score |
|----------|-------|-----------------|
| R1 (方法严谨性) | 3.5 (Borderline Conference) | 3.5 (维持，但注明条件：如 rebuttal 无法回应 encoder 依赖和 32B 证据，降至 3) |
| R2 (新颖性与完整性) | 3.0 (Findings) | 3.0 (维持) |
| **Director 综合** | **3.0 (Findings)** | — |

**置信度**: 4/5 (两位 Reviewer 均有相关方法论和领域经验，关键问题达成共识)

**综合判断**: 本文展示了扎实的实验方法论和难得的科学透明度，层选择敏感性发现对 probing 社区有方法论警示价值。但三个结构性问题限制了论文 impact：(1) HS 优势依赖弱 text baseline（BGE-large 后 3/4 不显著），使 Contribution 2 的核心 claim 有条件而非通用；(2) 32B 模型证据过弱（n=19-20, R1-32B 25% coverage, QwQ-32B position baseline competitive），"all four models" 为 overclaim；(3) K=5 阈值未经消融，评估框架的关键参数缺乏验证。

这些问题在 Findings 级别可以被接受（方法论本身 sound，贡献真实但有条件），但距主会议 robustness 标准有明确差距。建议接收为 Findings，条件是修复 W1-W3 的 framing（无需新实验，但需诚实限定 claims）。

---

## Detailed Comments

### Abstract
- 251 words，超出 250 上限。信息密度过高，缺叙事结构。
- "Holm-Bonferroni correction is stricter under positive dependence" 不应出现在 Abstract。
- "n=19--47 test traces; n=19--20 at 32B scale" 分号结构不自然。
- `bal_acc × crossing_rate` 格式在 PDF 中渲染不佳。

### Introduction
- 叙事结构完整（背景→问题→不足→贡献），但 deployment 叙事与 39-52% FPR 不匹配。
- 应在第 2-3 段设定读者预期：本文是 phenomenon characterization 而非 deployment solution。

### Method
- 问题定义和评估协议设计合理。
- K=5 需说明依据。
- Bootstrap 协议（Section 3.5）和 Experiments（Section 4.1）描述有重复。

### Experiments
- 核心数据完整，Table 2 清晰。
- Section 4.3 (Encoder robustness) 是 BGE-large 的唯一呈现位置——不够，应更显著。
- Section 4.4 (32B Analysis) 的局限诚实报告值得肯定。
- PCA-384d 2/12 failure 已报告（R1-8B BA, QwQ FPR），确认。

### Discussion
- 段落 1 (layer selection) 过长（15+ 句），建议拆分。
- "We hypothesize...any threshold-based detection study" 适当使用了 hedge language。
- Cross-model divergence 分析有见地。

### Related Work
- 42 篇引用，覆盖合理但有 4 篇 notable omissions。
- Baker et al. (2503.11926) 关于 CoT monitoring obfuscation risk 与本文直接相关，不引用是明显疏漏。

### Limitations
- 7 个 limitation paragraphs，全面且坦诚。
- Bootstrap 小样本问题承认但未影响主文 claim 强度。

### Format
- ACL [review] ✓, 匿名 ✓, 行号 ✓, 8 页 ✓, Limitations ✓, Checklist ✓
- fig3_model_dependency 未引用，需清理。
