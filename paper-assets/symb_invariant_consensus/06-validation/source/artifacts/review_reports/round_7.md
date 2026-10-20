---
round: 7
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-21T06:51:29.427085+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告（Round 10 — Fresh Review）

**论文**: *Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning*
**Venue**: EMNLP 2026 (via ACL Rolling Review) — Long Paper
**ARR Deadline**: 2026-05-25

---

## Summary

本文研究自提取符号约束能否突破 Self-Consistency (SC) 的性能天花板。作者提出 SICA（Symbolic Invariant Consensus Aggregation），从 CoT 推理轨迹中提取形式逻辑约束并通过加权 Partial MAX-SAT (Z3) 选择答案。在 6 个模型（7B-32B）、3 个逻辑推理数据集 + 3 个辅助数据集、3,000+ 条件评估上，自提取约束均未显著改善 SC（BH 校正后无条件达到显著）。作者将失败归因为 "Symbolic Confirmation Bias"（错误问题上 83.3% 约束支持错误多数答案，BR=4.97×），识别出 independence-accuracy trade-off（同模型 κ≥0.40 ceiling），并测试了 27 种修复策略（全部失败）。Oracle 控制确认机制本身有效（+29.90pp, +14.22pp FOLIO）。跨架构 DeBERTa NLI 验证在弱 generator 上显著有效（+6.67pp ProofWriter, p<0.001），DRC 以 39% 验证成本恢复 90% 增益。

---

## Strengths

1. **穷举式负面结果令人信服**：27 种补救策略横跨 15 个方法族（prompt-level, method-level, solver-level, diversity-level），系统性地关闭了"也许换策略就行"的反驳空间。这是该领域对 self-extraction 最全面的实验评估。

2. **Oracle 控制实验设计精良**：用 FOLIO gold FOL 和 ProofWriter DSL 替换自提取约束，在相同 MAX-SAT 管道下获得 +29.90/+14.22/+11.50pp 增益（p < 10⁻⁷），干净地隔离了"约束质量"这一瓶颈变量。这是论文方法论上最强的部分。

3. **多层次诊断体系**：answer-level κ、process-level cosine similarity、confirmation bias ratio、C₀ diagnostic、entropy decomposition 从不同角度三角验证同一结论。统计处理（McNemar + BH FDR + TOST + Bootstrap CI + Power Analysis）在 NLP 论文中罕见地严谨。

4. **CJT 理论框架有启发性**：用 Condorcet Jury Theorem 的独立性条件分析 SC 的失败模式，为理解 LLM 采样局限性提供了清晰的理论透镜。

5. **建设性方案缓解纯负面问题**：DeBERTa NLI escape + DRC 展示了"怎样才行得通"，DRC 以 39% cost 恢复 90% gain 有实用价值。

6. **可重复性高**：完整 prompt 模板、算法伪代码、22 个 Appendix section，代码承诺开源。

---

## Weaknesses

### Critical（Must-Fix，影响接收决定）

**C1. Proposition 1（Self-Extraction Ceiling）无证明** [R1-N1, R2-W3 — 共识]
- §3.3 的 Proposition 1 声称 Δ_max^self ≲ Δ_oracle / BR(M)，但全文无证明或推导。"≲" 不精确（上界？渐近？近似？）。Page 5 的 "proof sketch" 实际论证的是 Corollary 1 的单调性，非 Proposition 1。Δ_oracle 的定义依赖于实验设置而非纯数学构造——这是 "empirical claim dressed as theorem"。
- **必须**：提供完整证明（可放 Appendix）或降级为 "Empirical Finding"。

**C2. κ→Effective-K 映射理论基础不足** [R1-N2, R2 交叉同意 — 共识]
- Kish (1965) design effect 公式使用 ICC，非 Fleiss' κ。论文以 r=0.625 验证，仅中等相关（~61% 方差未被解释）。§3.1 有 ordinal diagnostic caveat，但 Abstract ("K_eff ≈ 1.20-3.62") 和 §5.1 中 K_eff 被作为定量指标使用——ordinal caveat 与 quantitative usage 矛盾。
- **必须**：(a) 报告 ICC 值并与 κ 对比；(b) Appendix 中提供 sensitivity analysis；(c) 全文统一为 ordinal 使用。

**C3. Capability gap "perfectly monotonic" 结论依赖 n=6 非独立数据点** [R1-N3, R2 交叉同意 — 共识]
- Spearman ρ=1.0 基于 6 个 verifier-generator pairs（3 NLI 架构 × 2 有效 generator 水平），非完全独立（共享 Mistral-7B traces 和 DeBERTa verifier）。n=9 robustness check (ρ=0.836, p=0.007) 更诚实。R2 指出可能存在选择性纳入显著结果的循环论证风险。
- **必须**：将 "perfectly monotonically" 降级为 "strongly monotonically" 或 "consistent directional trend"；以 n=9 result 为主；显式承认 n=6 局限。

**C4. 相对于 Huang et al. (2024) / Stechly et al. (2025) 的增量新颖性论证不足** [R2-N1, R1 部分 REBUT — 分歧]
- 核心发现——"自提取约束继承模型偏差"——与 Huang (LLMs cannot self-correct) 和 Stechly (self-verification limitations) 的已知结论在概念层面高度一致。R1 REBUT 指出 Z3 formal verification channel 使其非平凡（neurosymbolic 社区假设"形式化 → 可靠"），但 R2 认为这仍是 instantiation 而非 fundamental discovery。
- **Director 判断**：R1 的 Z3 论据有道理——formal verification 下偏差仍存在确实比 NL self-correction 更令人惊讶。但论文当前仅用 §1 中 2 句话区分，远不够显著。如果这个区分无法在修改中变得足够有说服力，则论文的 Excitement 不足以支撑主会议。
- **必须**：在 §1 和 §2 中用 1-2 段显式论证：(a) 为什么 Z3 formal verification 不同于 NL self-correction；(b) neurosymbolic 社区的隐含假设是什么；(c) 本文如何挑战该假设。

**C5. SatLM 正面结果与 SICA 负面结果的对比不充分** [R2-N2, R1 部分 REBUT — 共识需扩展]
- SatLM (Ye et al., NeurIPS 2023) 同样使用 LLM+SAT solver 但报告正面结果。论文在 §2 中有 2 句话对比（specification-generation vs trace-extraction），但对理解"为什么 SatLM works 而 SICA doesn't"远不够充分。这个对比恰恰能强化论文论点：trace-level extraction 的 answer contamination 是结构性的。
- **必须**：在 §2 或 §7 中系统化展开 specification-generation / program-generation / trace-extraction 三种范式的对比。

---

### Warning（Should-Fix，影响评分但不一票否决）

**W1. DRC τ 阈值无 held-out 评估** [R1-W1, R2 同意 — 共识]
- τ ∈ {0.3, 0.5, 0.7, 0.9} 均在同一 ProofWriter (n=600) 上选择和评估。作为第 4 个正式 contribution，"90% recovery at 39% cost" 可能 overfitted。
- 建议：dev/test split 或跨数据集 τ 验证，或显式标注 oracle selection。

**W2. Cross-architecture NLI escape 适用面极窄** [R1-W2, R2-W5 — 强共识]
- BH 校正后仅 2/12 条件存活（均为 Mistral-7B ProofWriter）。NLI 仅适用于弱 generator + premise-conclusion 可分解 + verifier 强于 generator 的场景。LogiQA 无效。
- 建议：显式框定为 narrow PoC，讨论适用条件，避免暗示 general escape。

**W3. 四种子复制方差大 + 统计功效 <21%** [R1-W3, R2 有 nuance 地同意 — 共识]
- Δ ∈ {+3.43, +2.94, 0.00, −0.49}pp。Power analysis 显示所有确认性条件观测功效 <21%。R2 补充：四种子不是唯一证据支柱（还有 15 条件 FDR null + oracle + 27 策略失败），但 power limitation 应在主文更显著。
- 建议：在核心 claim 措辞中更明确承认 power limitation。

**W4. TOST ±2pp margin 缺少显式理由** [R1-W4, R2 同意 — 共识]
- 未论证 2pp 为何是合适的实际意义阈值。NLP 领域缺乏共识，但至少应讨论 SC 文献中的典型改进幅度并展示不同 margin 下的 sensitivity。

**W5. Bias Ratio 无置信区间** [R1-W5, R2 同意 — 共识]
- BR (4.97×, 3.93×, 2.88×) 缺 CI。Bootstrap CI 计算成本极低。无 CI 则无法判断跨模型 BR 差异是否显著。

**W6. "Symbolic Confirmation Bias" 需与近期 CoT confirmation bias 工作区分** [R2-N3, R1 同意 — 共识]
- 近期 arXiv:2506.12301 和 arXiv:2604.02485 已研究 CoT confirmation bias。本文的特殊性——偏差在 Z3 satisfiability 验证后仍存在——需要更清晰地表述。

**W7. Related Work 过度压缩** [R2-W2, R1 同意 — 共识]
- 三段 Related Work 将约 25 篇论文压缩为引用列表。Neurosymbolic 段混合 specification-generation / program-generation / trace-extraction 未分类。

**W8. 27 种修复策略正文展示不足** [R2-W4, R1 同意 — 共识]
- §5.4 仅 5 行文字 + Figure 2 概览。作为核心论证环节应在正文增加代表性策略的分类讨论。

---

### Info（小问题，不影响接收）

- Independence-Accuracy Trade-off 作为独立贡献有 bias-variance tradeoff 重述嫌疑（R2-W1, R1 REBUT）
- Table 1 信息密度极高，脚注系统复杂（b, †, 4s, *, ***），可读性可优化
- "Symbolic Mirage" 引入后极少复用，与 "Symbolic Confirmation Bias" 的层次关系不清
- Abstract 约 250 词偏长（可接受但可精简）
- §5.1 标题 "Condorcet Effective-K" 中 K 与 κ (kappa) 容易混淆
- 缺失引用：CoT confirmation bias 文献 (arXiv:2506.12301, arXiv:2604.02485)、Eidoku (arXiv:2512.20664)、Tree of Thoughts (Yao et al., 2023)

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识（[AGREE] 或 REBUT 后达成一致方向）：
- [AGREE] Proposition 1 无证明，需降级或补证（C1）
- [AGREE] κ→K_eff 映射理论基础弱，需 ICC + sensitivity（C2）
- [AGREE] n=6 capability gap 需降级措辞（C3）
- [AGREE] SatLM 对比需扩展（C5）
- [AGREE] SCB 术语需与 CoT confirmation bias 区分（W6）
- [AGREE] DRC 无 held-out（W1）
- [AGREE] Cross-arch escape 太窄（W2）
- [AGREE] TOST margin 无理由（W4）
- [AGREE] BR 无 CI（W5）
- [AGREE] Related Work 压缩（W7）
- [AGREE] 27 策略正文不足（W8）

## Reviewer Divergence

**核心分歧：新颖性权重 → Overall 评分**
- **R1 (3.5, Borderline Conference)**：更看重实验的严谨性和 27 策略穷举。认为 Z3 formal verification 使其非平凡推广，κ≥0.40 定量边界超越已知原理。
- **R2 (3.0, Findings)**：更看重概念新颖性。认为核心发现对熟悉 self-correction 文献的读者可预测，诊断指标是已有度量的直接应用。
- **Director 判断**：论文的实验贡献优秀，但概念增量相对于 Huang/Stechly 有限。Z3 formal verification channel 确实是更强的测试条件，但论文未充分发挥这一区分。当前版本更适合 Findings。

---

## Questions for Authors

1. SatLM 使用 LLM+SAT solver 但报告正面结果，关键区别是否在于 specification-generation vs trace-extraction？如果是，请在论文中系统化讨论。
2. Proposition 1 的 "≲" 是严格上界还是近似？能否提供形式化证明？
3. 如果用 ICC 替代 κ 计算 K_eff，排序和结论是否改变？
4. DRC 的 τ=0.7 在 FOLIO 上是否同样是最优？
5. Reasoning model（Qwen3 thinking mode, κ=0.91）是否改变了 confirmation bias 的性质？

---

## Missing References

1. **"Unveiling Confirmation Bias in Chain-of-Thought Reasoning"** (arXiv:2506.12301, Jun 2025) — CoT confirmation bias，与 SCB 概念直接相关
2. **"Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models"** (arXiv:2604.02485, Apr 2026) — LLM confirmation bias 系统评估
3. **"Eidoku: Neuro-Symbolic Verification Gate via Structural Constraint Satisfaction"** (arXiv:2512.20664, Dec 2025) — 约束满足验证，与 Z3 MAX-SAT 相关
4. **Yao et al. (2023) "Tree of Thoughts"** — structured test-time search，self-evaluation 也面临偏差
5. **SatLM (Ye et al., NeurIPS 2023)** — 已引用但讨论不足，需系统化展开对比

---

## External Review

外部审稿未启用。

---

## Visual Layout Check（非评分项）

视觉审查已完成（3 warning, 5 info, 0 critical）：

| 严重度 | 位置 | 发现 |
|--------|------|------|
| ⚠️ Warning | Pages 3-5 | 连续 3 页无 figure/table，建议在 page 5 实验 setup 处加 summary table |
| ⚠️ Warning | Page 7 | Display items 过度拥挤（Table 2 + Figure 2 + Figure 3 + Table 3 共 4 个），建议分散 |
| ⚠️ Warning | Page 7 | Figure 2（27 策略条形图）y 轴标签 ≤6pt，打印后难以辨认，建议改 figure* 全宽 |
| ℹ️ Info | Page 1 | 首页无视觉锚点，建议加 teaser figure |
| ℹ️ Info | Page 2 | Figure 1 pipeline 图内文字偏小 |
| ℹ️ Info | Page 5 | 实验 setup 纯文本呈现，建议 setup table |
| ℹ️ Info | Page 7 | Figure 3 legend/axis label 字号偏小 |
| ℹ️ Info | Page 22 | 末页底部约 1/3 空白 |

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**评分理由**：
- **Soundness (3.5/5)**：核心负面结论有充分实验支撑（6 模型 × 3+ 数据集 × 27 策略全部失败 + oracle 对照）；但 Proposition 1 无证明、κ→K_eff 映射理论基础弱、Spearman ρ=1.0 基于 n=6。
- **Excitement (2.5/5)**：核心发现对熟悉 self-correction 文献的读者部分可预测；Z3 formal verification channel 是更强的测试条件但未充分论证其非平凡性；DRC 有实用价值但适用范围窄。
- **Reproducibility (4/5)**：方法描述清晰，Appendix 材料极充实，代码承诺开源。

**Confidence: 4/5**

**修改建议优先级**：
1. [最高] 加强 Huang/Stechly 区分 + SatLM 对比（C4, C5）— 这决定了论文能否从 Findings 升级到 Borderline Conference
2. [高] Proposition 1 降级或补证（C1）
3. [高] κ→K_eff ICC sensitivity（C2）+ capability gap 措辞降级（C3）
4. [中] DRC held-out + cross-arch framing + BR CI（W1, W2, W5）
5. [中] Related Work 扩展 + 27 策略正文展示（W7, W8）
6. [低] TOST margin + SCB 术语区分 + 视觉布局（W4, W6, VL）

**Venue Fit**：当前版本 **适合 Findings**，主会议需要在新颖性论证（C4）上有实质性突破。如果修改后能充分论证 Z3 formal verification channel 为何构成对 neurosymbolic 社区核心假设的非平凡挑战，评分可能提升至 3.5 (Borderline Conference)。