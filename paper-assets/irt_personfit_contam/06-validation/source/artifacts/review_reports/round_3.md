---
round: 3
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T05:05:32.247607+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 4 (Fresh Review)

**论文**: What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization
**Venue**: EMNLP 2026 (via ACL Rolling Review, Long Paper)
**审稿日期**: 2026-05-22
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）
**交叉轮数**: 1 轮（关键问题达成共识，无需第二轮）

---

## Summary

本文首次将心理测量学中的 IRT person-fit 统计量（ℓz*）系统性地迁移到 LLM benchmark 污染检测领域，提出 Δℓz* difference-in-differences 设计以应对 LLM 对 IRT 假设的系统性违反。在三个 7-8B 模型家族（Qwen2.5-7B、Llama-3.1-8B、Mistral-7B）和两个 benchmark（MMLU、ARC-Challenge）上，通过 QLoRA SFT 控制实验验证了四个行为边界：inverted-U dose-response、模型特异性 θ-shift dynamics、detection-diagnosis tradeoff、以及初步的 post-RL 残留模式。论文定位为 characterization study 而非 detection tool。

---

## Strengths

**S1.** **跨学科桥梁构建得当**（R1/R2 共识）。将教育测量中成熟的 person-fit 统计量（Snijders 2001, Karabatsos 2003）迁移到 LLM 污染检测，"被污染 LLM ≈ 作弊考生" 的类比自然且有说服力。两个此前独立的研究领域被有效连接。

**S2.** **Δℓz* DiD 设计巧妙**（R1/R2 共识）。57/60 model-benchmark cells 在无污染下即产生 |ℓz*| > 1.96，说明绝对阈值不可用。差分设计将系统性 IRT 违反转化为可控特征，模拟验证支持其在 shared LD 下的鲁棒性（d_ratio ≥ 0.93 for σ_τ ≤ 0.5）。

**S3.** **Detection-diagnosis tradeoff 有实际价值**（R1/R2 共识）。Table 3 系统对比了 ℓz*、HT、accuracy z-score 的检测力和诊断力，two-stage workflow 建议（先 z-score 筛查，再 ℓz* 诊断）具有实际指导意义。论文主动揭示 ℓz* 检测力劣于简单统计量，学术诚实。

**S4.** **诚实的 framing 和自我审视**（R1/R2 共识）。论文将自身定位为 "characterization" 而非 "detection tool"；Appendix H 主动验证 PSN-IRT 依赖的必要性（MML-EM 失败，r_a=0.127）；Limitations 覆盖了主要范围限制。

**S5.** **附录鲁棒性分析全面**（R1/R2 共识）。4PL vs. 3PL ablation、LD 模拟（shared + asymmetric）、参数扰动、BCa 校正、MML-EM refit 等覆盖了多个潜在质疑方向。

**S6.** **θ-shift absorption 机制有理论深度**（R1 特别肯定）。高能力模型在高污染下检测信号反而减弱不是显而易见的，论文从 IRT 理论给出了清晰因果解释，并通过 fixed-θ vs. free-θ 对比验证了机制。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1.** **25% 污染条件未在 §3.3 描述——核心证据来源不透明**（R1-N1, R2 AGREE）
§3.3 明确写 "three conditions: clean, 15% contamination, and 50% contamination"，但 Table 1 包含 Qwen 25% 数据（d=−8.22），inverted-U（Finding 1，论文首要贡献）完全依赖此数据点。25% 是先验计划还是看到非单调趋势后追加的 post-hoc 条件未说明。如果是 post-hoc，构成 researcher degrees of freedom。这是方法论透明性的核心缺陷。

**C2.** **Inverted-U 证据不足以支撑首要发现地位**（R1-N2, R2 AGREE）
仅基于 1 个模型家族（Qwen）的 3 个数据点（15%, 25%, 50%）。Llama 和 Mistral 均显示单调 dose-response（2/3 模型不支持 inverted-U）。CI 极宽（d(25%) CI: [−18.9, −5.7]）。3 点非单调性可由噪声产生。论文虽限定为 "specific to Qwen"，但 Abstract/Introduction 将其列为首要发现，claim 强度与证据不匹配。

**C3.** **实验设计矩阵不完整**（R1-N3, R2 AGREE）
完整 3 模型 × 2 benchmark × 3 污染水平 = 18 条件，实际仅完成约 8 条。ARC-C 仅 Qwen，25% 仅 Qwen，Mistral n=6。Figure 2 灰色格子直观暴露。此外全部模型为 7-8B（R2-N3），无法区分 Finding 2 的 ability-driven vs. scale-driven 效应。Abstract "across three 7–8B model families (n=10 seeds each)" 暗示完整覆盖。

**C4.** **Abstract 事实错误**（R1-N4, R2 AGREE）
Abstract 写 "n=10 seeds each"，但 §3.3 明确写 Mistral 仅 n=6。必须修正。

**C5.** **Post-RL Finding 4 (N=1) 不应列为核心贡献**（R2-N1, R1 AGREE）
N=1（Qwen+GRPO, 15%），§4.5 自己声明 "no statistical inference is drawn"，但 Abstract/Introduction 将其与其他三个经 factorial design 验证的发现并列。应降级为 Discussion 中的 preliminary observation。

### Should-Fix（影响评分但不一票否决）

**W1.** **"Black-box access" framing overclaim**（R1-W2, R2-W1, 交叉完全一致）
方法依赖 PSN-IRT 外部 4PL item parameters（13,000+ 模型校准）和 clean baseline seeds。"only binary response patterns" 和 "black-box" 的标签过度简化了实际访问需求。应区分 target model access (binary only) vs. external item bank (substantial)。

**W2.** **QLoRA SFT 生态效度 vs. 标题范围**（R1-W1, R2 AGREE）
标题 "Benchmark Contamination" 暗示广泛适用性，但实验仅覆盖 QLoRA SFT。Introduction 有 SFT scope 限定但 title/abstract 未充分反映。

**W3.** **缺乏与 ConStat 等方法的实证对比**（R2-N2, R1 partial REBUT → 见 Divergence）
Discussion 称与 ConStat "complementary" 但无实证验证。论文自身 Table 3 已揭示 ℓz* 检测劣势。至少应系统解释为何不做直接对比。

**W4.** **PSN-IRT 校准循环性**（R1-W5, R2 AGREE）
校准样本可能包含被污染模型，Appendix F.2 随机扰动分析未覆盖系统性偏差（高估 θ → 偏移 difficulty）。

**W5.** **Bootstrap CI 小样本可靠性**（R1-W3, R2 partial REBUT）
Mistral n=6 下 percentile bootstrap coverage 较差。BCa 已在 Appendix G 但主文未使用。建议主文改用 BCa 或加注 caveat。

**W6.** **遗漏直接相关近期工作**（R2-W5, R1 AGREE）
Han et al. (EACL 2026 Findings, arXiv 2510.07175) 处于 psychometrics × contamination 交叉点未引用；RADAR (Zawalski et al., 2025) 也值得讨论。

**W7.** **Cohen's d 将被污染模型视为固定点**（R1-W6, R2 partial REBUT）
未报告每个污染条件的运行次数。如仅 1 次，低估真实不确定性。效应量极大故不影响定性结论。

**W8.** **LD 模拟代表性有限**（R1-W7, R2 AGREE）
Testlet+Gaussian 模型不一定捕捉真实 LLM 依赖结构（attention 机制、序列效应等）。应在 Limitations 讨论。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致（[AGREE]）：

| # | 问题 | R1 | R2 | 共识 |
|---|------|----|----|------|
| 1 | Post-RL N=1 不应为核心贡献 | W4 → AGREE | N1 | 降级为 preliminary observation |
| 2 | Inverted-U 证据薄弱 | N2 | W3 → AGREE | 降级或补数据 |
| 3 | 25% 条件透明性 | N1 | — → AGREE | §3.3 必须补充描述 |
| 4 | 实验矩阵不完整 | N3 | — → AGREE | 补数据或限定 claims |
| 5 | Abstract n=10 事实错误 | N4 | — → AGREE | 简单修正 |
| 6 | Black-box framing overclaim | W2 | W1 | 调整术语或明确定义 |
| 7 | QLoRA SFT 范围 vs. 标题 | W1 | — → AGREE | title/abstract 加限定 |
| 8 | PSN-IRT 循环性 | W5 | — → AGREE | 讨论系统性偏差 |
| 9 | LD 模拟代表性 | W7 | — → AGREE | Limitations 讨论 |
| 10 | 遗漏 Han et al. / RADAR | — → AGREE | W5 | Related Work 补充 |

---

## Reviewer Divergence

**D1. ConStat 对比的严重程度**
- R2（Must-Fix）：论文定位在 contamination detection 领域却不与主要方法（ConStat/PaCoST/CoDeC）对比是重大缺陷。
- R1（Should-Fix）：信息访问层级不同使直接对比不公平——ConStat 需跨 benchmark 性能分数，ℓz* 仅需 binary responses。论文已通过 Table 3 自我揭示检测劣势。缺乏对比的原因应在论文中系统解释，但不应要求在不同访问层级的方法间做 apple-to-apple 对比。
- **部分共识**：两人同意至少应在 Discussion/Related Work 中系统解释为何不做直接对比。

**D2. Finding 2/3 的 novelty 评估**
- R2：θ-shift dynamics 本质是 IRT 天花板效应，detection-diagnosis tradeoff 是 ℓz* by design 的结果。Novelty 有限。
- R1：定性方向可预测，但定量结果（7.6× amplification、ARC-C 反转、57/60 vs 4/60 flagged cells）和边界条件是新的。LLM 严重违反 IRT 假设下理论预测是否成立需实证回答，empirical quantification 有独立价值。
- **未达共识**：两人对 "empirical validation in a new domain" 的 contribution 价值评估存在根本性差异。

---

## Questions

1. 25% 污染条件是预先计划的实验条件还是看到 15%/50% 趋势后追加的 post-hoc 探索？请在 §3.3 中透明说明。
2. 每个污染条件（15%, 25%, 50%）有多少个独立训练 run？如果仅 1 次，Cohen's d 将污染 ℓz* 视为固定点是否合理？
3. 为什么 ARC-C 仅在 Qwen 上测试而排除了 Llama 和 Mistral？Figure 2 灰色格子应简要说明缺失原因。
4. Llama/Mistral 是否存在在 25% 污染下也出现 inverted-U 的可能？是否有计划补充这些条件？
5. PSN-IRT 校准样本中被污染模型的比例是多少？是否可能导致 item difficulty 的系统性偏移？
6. Reproducibility Statement 说 "random seeds are reported for all experiments"，但正文中未列出具体 seed 值。

---

## Missing References

1. **Han et al. (2026)** "Quantifying Data Contamination in Psychometric Evaluations of LLMs" (EACL 2026 Findings, arXiv 2510.07175) — 直接处于 psychometrics × contamination 交叉点，虽侧重 personality inventories 但方法论高度相关
2. **RADAR** (Zawalski et al., 2025, arXiv 2510.08931) — 近期有影响力的 mechanistic contamination detection 工作，与本文 "behavioral characterization" 形成对比

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warnings, 16 info）。

**Warnings**:
- Figure 2 heatmap 单元格内数值标注字号偏小，标准打印尺寸下可能需要放大阅读
- Figure 4 的 4 个子图 axis label 和 legend 字号偏小（约正文 60-65%），建议增大至 ≥70%

**Positive findings**:
- 主正文恰好 8 页，符合 EMNLP 2026 页数限制
- 7 个 display items（4 figures + 3 tables），密度 0.875/页，实证论文合理范围
- 所有 float 位于首次引用附近，无漂移
- 颜色方案色盲安全，灰度友好
- 无 margin 溢出、LaTeX 渲染错误或 section heading 孤悬
- References 格式一致，无未解析引用

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Confidence: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0/5 | 3.0/5 | 3.0/5 |
| Excitement | 3.0/5 | 2.5/5 | 2.75/5 |
| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |
| Overall | 3.5 | 3.0 | **3.0** |

**评分理由**：

本文做了一个有价值的跨学科迁移工作，将心理测量学 person-fit 统计量引入 LLM 污染检测。DiD 设计巧妙，detection-diagnosis tradeoff 分析有实际价值，诚实的 framing 值得肯定。

然而，作为 EMNLP 2026 Long Paper 投稿，存在以下实质性问题：

1. **证据基础与 claim 强度不匹配**：首要发现 inverted-U 仅基于 1 个模型 3 个数据点，且 25% 条件未在实验设置中描述（方法论透明性问题）；Post-RL 发现 N=1 却列为核心贡献。
2. **实验覆盖面有缺口**：18 条件仅完成约 8 条，全部 7-8B 模型无规模多样性，Abstract 存在事实错误。
3. **Framing 问题**："black-box access" 过度简化了对 PSN-IRT 外部 item bank 的实质性依赖；标题范围超出 SFT-only 的实验证据。
4. **Contribution density 偏薄**：四大发现中 Finding 4 缺乏支撑，Finding 2/3 的 novelty 存在争议（R2 认为 IRT 理论可预测，R1 认为经验量化有独立价值），仅 Finding 1 被两人认可为真正新颖但证据不足。

综合评估，论文的跨学科贡献和方法论框架有价值，但证据基础和 contribution density 更适合 Findings 而非主会议。如果能：(a) 在 §3.3 透明描述所有实验条件，(b) 补充 Llama/Mistral 25% 数据验证 inverted-U 模型特异性，(c) 将 Post-RL 降级并调整 claims，(d) 修正 Abstract 事实错误和 framing，论文有潜力提升至 3.5 (Borderline Conference)。

---

## Detailed Comments

### §1 Introduction
- 第 3-6 行以 pretraining contamination 为动机，但实验仅覆盖 SFT。第 14-18 行的 SFT scope 限定是好的改进，但应更突出。
- 第 39 行 "n=10 seeds each" → 事实错误，Mistral n=6
- Finding (4) 的 enumerated 位置暗示与其他发现同等份量，建议移除或明确标注 preliminary

### §3.3 Experimental Setup
- **关键缺陷**：仅描述 clean/15%/50% 三个条件，但 Table 1 和 §4.2 使用了 25% 数据。必须补充 25% 条件的描述和动机。
- 未报告每个污染条件的独立运行次数
- 未说明为什么 ARC-C 排除了 Llama/Mistral

### §4.2 Non-Monotonic Dose-Response
- 证据仅限 Qwen，但 §4.2 标题和叙事暗示更广泛的适用性
- "4.3× reduction from peak to high contamination" 的描述准确但可能被噪声解释
- 建议标题改为 "Ability-Dependent Non-Monotonic Dose-Response" 以反映 Qwen 特异性

### §4.3 θ-Shift Dynamics
- 第 66 行关于 MMLU 50% 处 accuracy vs. |d| 的 "negative correlation" 仅基于 3 个数据点，不应使用 "correlation" 一词
- ARC-C ceiling effect 反转（第 70-73 行）是有价值的观察，但仅基于 Qwen

### §4.4 Detection-Diagnosis Tradeoff
- Table 3 accuracy z-score |d|=68.7 的解释（near-zero cross-seed variance）在正文中已给出，但可能仍误导读者
- "57/60 vs. 4/60 flagged cells" 是有力对比，但诊断价值的具体应用场景（什么 workflow 需要 item-level diagnosis 而非 detection）未展示

### §4.5 Post-RL
- 应缩减为 Discussion 中一段。ℓz* 从 2.91→7.69 可能是 GRPO-induced θ-shift 而非 contamination residual——需 clean+GRPO control 来 disentangle。

### §5 Discussion
- "complementary to ConStat" 仅一句带过——应系统解释为何不做直接对比（信息访问层级差异）
- PSN-IRT 校准循环性讨论不够深入——随机扰动 ≠ 系统性偏差

### Abstract
- ~250 词偏长，post-RL 部分可压缩
- "n=10 seeds each" 事实错误
- "only binary response patterns" 和 "externally calibrated 4PL item parameters" 的关系需更突出

### Limitations
- 覆盖了主要限制，但缺少对 LD 模拟代表性的讨论
- 可增加对 PSN-IRT 系统性偏差的讨论

### References
- 遗漏 Han et al. (EACL 2026 Findings) 和 RADAR (Zawalski et al., 2025)
- 当前 33 条引用数量对 EMNLP long paper 偏少