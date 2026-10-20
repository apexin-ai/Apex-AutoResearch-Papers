---
round: 8
overall_score: borderline
timestamp: 2026-05-16T12:36:18.608938+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 8

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Deadline**: 2026-05-25
**Reviewers**: R1 (方法严谨性 + 实验有效性), R2 (新颖性 + 完整性 + 写作质量)

---

## Summary

本文提出 episode-level counterfactual analysis 方法来分解模块化 LLM agent 中的 routing signal。在 ScienceWorld 的 11/30 任务类型（245 episodes, Qwen2.5-7B-Instruct）上，发现 78.9% 的非平局路由标签源自 death asymmetry（penalty-independent），DAF 在 P=100 时达 90.4%（95% CI [81.6%, 98.8%]）。一个探索性 step-level router 在 held-out episodes 上低于 always-deterministic baseline（47.1% vs 50.0%），data scaling（32×）和 capacity scaling（0.6B-4B）确认结构性限制。MATH 和 ALFWorld 的 cross-environment 分析提供方向性支撑。

## Strengths

1. **双指标设计解决了 R6-C1 的核心关切**：78.9% penalty-independent label fraction 与 DAF 并列贯穿全文，读者可自行评估 penalty 选择的影响。[R1-S3, R2-S1, 共识]
2. **透明度极高**：DAF penalty-dependence (50%-98%)、r=0.97 structural coupling、11/30 scope 均主动在 Abstract 中披露。前轮要求的所有 qualifier 均已落实。[R1-S2]
3. **Router failure 诊断彻底**：data scaling、capacity scaling、per-task-type breakdown、classification head vs SFT、cross-split robustness (8 seeds) 构成系统性的 negative-result 证据链。[R1-S6, R2-S2]
4. **Robustness diagnostics 丰富**：LOO Pearson r [0.963, 0.980]、bootstrap CI、Spearman ρ=0.986、anti-cherry-picking paragraph、penalty sensitivity analysis (Table 5-6) 深化了边界条件。[R1-S4, R2-S3]
5. **Labeling quality audit** (Appendix A) 排除 oracle circularity——zero labels depend on tie-breaking。[R1-S5]
6. **Related Work 覆盖全面**——RouteLLM、Reflexion、tool-learning survey、CRPO、6 篇 2025-2026 concurrent work 均已纳入。[R2-S4]
7. **Limitations 诚实具体**——19 个排除 task types、episode-level label 粗粒度、DAgger distribution shift、ReAct-only、Llama pilot 统计不足均被明确承认。[R2-S5]

## Weaknesses

### Must-Fix（共识）

**W1** [R1-W4 + R2-W1, 共识 AGREE]: **"routing signal vanishes" 措辞过度解读 non-significant result**
- Abstract 和 Conclusion 中 "routing signal vanishes without a death penalty" 暗示 null effect，但 MATH 数据显示 30:17 label distribution 和 +4.3pp directional trend——signal 存在但方向反转。p=0.079 未达 α=0.05，Conclusion 中缺少 significance hedge（Abstract/Introduction 中有）。
- 修复：替换为 "the deterministic advantage disappears" 或 "death-driven routing signal is absent"；Conclusion 统一添加 "not reaching α=0.05"。

### Should-Fix（共识）

**W2** [R1-W1, R2 AGREE]: **Data scaling ablation minority-class confound**
- 32× augmentation（synonym substitution + template variation）仅增加 step-level surface diversity，internal-preferred episodes 始终只有 9 个 unique episode 的 paraphrase 变体。"rules out data scarcity" 混淆了 step-level scarcity 和 episode-level minority-class scarcity。25% unaugmented scale 的 collapse 说明 "9 个 episode 的子集不够"，不等于 "episode diversity 不重要"。
- 修复：软化为 "rules out step-level data scarcity; episode-level minority-class diversity remains a potential confound that cannot be resolved without collecting more internal-preferred episodes—which the 86:9 ground-truth ratio makes structurally impossible in this environment"。

**W3** [R1-W2, R2 AGREE]: **Capacity scaling ablation缺 episode-level 评估**
- Appendix G 仅报告 step-level balanced accuracy (52.8%/54.1%/53.5%)。论文核心发现是 step-level vs episode-level 的 generalization gap (§4.3)。episode-level capacity scaling 结果缺失使 "structural limitation" 结论在 capacity 维度上不完整。范围也偏窄（0.6B-4B，均 <5B）。
- 修复：补充 episode-level capacity scaling 数据；或明确声明 ablation 仅为 step-level 并注明局限。

**W4** [R2-W5, R1 AGREE]: **"Safety critic" 类比过度延伸**
- Discussion 称 "The router functions as a safety critic"，但论文实际发现是 router 失败（47.1% < 50%）且 always-deterministic 即最优。Safe RL 中 safety critic 是 learned 约束机制；本文发现更像 "default to safe modality"——trivial default policy，非 learned critic。
- 修复：修改为 "The routing problem reduces to safety-first modality selection—closer to a conservative default policy than to a learned safety critic"。

### Should-Fix（R2 raised, R1 partial rebut — 建议改为 presentation fix）

**W5** [R2-W2, R1 REBUT with caveat]: **Deterministic modality 跨环境定义不一致未显式讨论**
- ScienceWorld (ground-truth obs) / MATH (code interpreter) / ALFWorld (admissible actions) 的 det modality 定义不同。R1 rebut: cross-env 是 contrast argument（有 death → det wins; 无 death → advantage gone），不要求同一 modality 定义。但 R1 同意加一段显式讨论会改善 presentation。
- 修复：Discussion 中加 1 paragraph 明确三环境 modality 定义及其对跨环境推断的限制。

### Minor（共识或单方）

**W6** [R1-W3, R2 AGREE]: Reasoning depth ablation 未报告 episode 数量（n per condition）。修复：加括号注明 n。

**W7** [R1-W5, R2 AGREE with nuance]: r=0.97 数学近必然性在 §4.1 首次出现时 foreground 不够——读者可能误读为独立于 DAF decomposition 的额外证据。Abstract 和 Appendix D 已有 qualification，但 §4.1 应加一句显式说明。

**W8** [R2-W6, R1 AGREE]: 3 个 orphan bib entries (toolkengpt, tot, voyager)；tool-learning-survey year 可能应为 2025。Camera-ready 级别 cleanup。

## Reviewer Consensus

| 问题 | R1 | R2 | 判定 |
|------|----|----|------|
| "vanishes" overstatement | AGREE | AGREE | **Must-Fix** |
| Data scaling minority-class confound | Raised | AGREE | Should-Fix |
| Capacity scaling 缺 episode-level | Raised | AGREE | Should-Fix |
| Safety critic 类比 | AGREE | Raised | Should-Fix |
| Modality 定义异质性 | REBUT (presentation) | Raised | Presentation fix |
| 11/30 generalizability | REBUT (adequately scoped) | Raised | No action (scope acknowledged) |
| Abstract 过长 | REBUT (prior review required density) | Raised | No action |

## Reviewer Divergence

- **R2-W3 (11/30 scope)**: R2 认为 63% 排除率仍是 generalizability concern；R1 rebut: excluded tasks 无 routing signal (Δ_full=0)，无法分析不存在的东西，scope 已充分限定。Director 判定：R1 论据成立——这是 acknowledged scope limitation，论文已正确处理。
- **R2-W4 (Abstract 长度)**: R2 认为 ~250 词过载；R1 rebut: 密度是前轮 review 要求 qualifier 的直接结果。Director 判定：R1 论据成立——可选择性删除 Llama pilot mention 以节约 ~20 词，但不构成问题。

## Questions for Authors

1. Data scaling 800% scale 的 internal-preferred episodes 是否仍只是 9 个原始 episode 的 paraphrase？如果是，这对 "rules out data scarcity" 结论有什么影响？
2. Capacity scaling (0.6B-4B) 在 episode-level 的表现如何？是否也 flat at ~47-50%？
3. 70 of 75 death-asymmetry labels 是 internal-dies-det-survives。是否一个简单的 "internal death predictor" 就足够了——routing 可完全简化为单策略 death prediction？
4. find-non-living-thing 的 non-death routing signal (Δ=+9.58) 来源是什么？是否分析过 post-death-avoidance routing 的可能性？
5. Reasoning depth ablation 的 n (per condition) 是多少？

## Missing References

核心 references 已覆盖。可选建议（非必须）：
- FrugalGPT (Chen et al., 2023) / HybridLLM (Ding et al., 2024)——cost-quality routing 先驱
- CPO (Stooke et al., 2020)——若要加强 safety critic 类比精度

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。

## Overall Assessment

**Score: Borderline (3.25/5)**
- R1: 3.5/5 (Borderline to Weak Accept, Findings track)
- R2: 3.0/5 (Findings acceptance)
- Confidence: 4/5 (both reviewers)

**判定**：论文在选定范围内做了扎实的 empirical analysis。核心发现（78.9% death-asymmetry labels, DAF=90.4%）可信且有 insight 价值。Router failure 的诊断彻底、透明度高、前轮 critical issues 已全部修复。

阻碍 main conference acceptance 的主要因素：
1. 核心发现绑定于 ScienceWorld 的特定 failure structure（-100 death penalty），generalizability 受限
2. Episode-level counterfactual analysis 方法论本身较为直接（paired comparison），方法创新性不足以单独支撑 main track
3. Cross-environment validation 的 MATH 结果未达统计显著性 (p=0.079)，且 modality 定义跨环境不一致

**推荐**：**Findings track acceptance**。论文的 insight 清晰度、分析彻底性和自我批判诚实度达到 publishable 水平，适合作为 empirical findings paper。如能修复 Must-Fix（"vanishes" 措辞）和 2-3 个 Should-Fix，可进一步加强。

## Detailed Comments

### §Abstract
- "routing signal vanishes" → Must-Fix (W1)
- 可选删除 Llama pilot mention 以缩短 ~20 词

### §3.3 (DAF Definition)
- 双指标设计优秀，无修改需求

### §4.1 (Death Avoidance Decomposition)
- r=0.97 处加一句 mathematical near-inevitability 说明 (W7)

### §4.3 (Router Training as Diagnostic)
- "rules out data scarcity" 需软化 (W2)
- Capacity scaling 补充 episode-level 或注明局限 (W3)

### §5 (Discussion)
- "safety critic" 类比修改 (W4)
- 加 modality heterogeneity paragraph (W5)

### §6 (Conclusion)
- "routing signal vanishes" → Must-Fix (W1)
- 确保 p=0.079 后有 "not reaching α=0.05" hedge

### Appendix E (Data Scaling)
- 区分 step-level vs episode-level data scarcity (W2)

### Appendix G (Capacity Scaling)
- 补 episode-level 或声明 step-level only (W3)

### §3.1 (Method)
- 报告 reasoning depth ablation 的 n (W6)

### Bib
- 删除 orphan entries；核实 tool-learning-survey year (W8)