---
round: 17
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-20T06:54:27.184798+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 17 (Fresh Review)

**论文**: Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning
**Venue**: EMNLP 2026 (Long Paper, ARR)
**截止**: 2026-05-25
**Reviewer 编排**: R1（方法严谨性+实验设计+统计分析）、R2（新颖性+相关工作+写作+格式）
**审稿模式**: Fresh（无历史轮次记忆）

---

## Summary

本文提出 Solver Trace Ablation (STA)，将 LOO 消融应用于 GRPO 训练的神经符号推理器，通过 Intensional Structural Reward (ISR) 指标量化形式化输出的结构质量。核心发现：(1) exec-only GRPO 在 prove rate 93-96% 时 ISR 坍塌至近零（99.5% 退化），SFT baseline 以 92.3% non-hacking 定位故障源于 RL；(2) ISR 作为训练奖励产生 Goodhart 效应（TS 放大 ~5×，premise-count deconfounding 后优势仅 1.06×）；(3) 跨域泛化（FOL→Prolog、FOLIO→ProofFOL）显示 dataset-dependent 结果。实验基于 Qwen3-4B，6 种奖励条件 × 3 seeds × 2 逻辑后端 × 2 数据集族，定义 8 种 hacking 模式分类法。

---

## Strengths

**S1. 诊断框架新颖且有实际价值** [R1, R2 一致]。STA/ISR 揭示了 execution-based evaluation 完全隐藏的结构退化——PR 持续上升时 ISR 同步坍塌。LOO 本身不新，但系统化为 neurosymbolic RL 的训练期组件级诊断是有创造性的应用迁移。

**S2. 系统的实验设计** [R1, R2 一致]。6 条件 × 3 seeds × 2 logic × 2 datasets 的矩阵设计，加上 100-step 早期 checkpoint、matched random control、SFT baseline，体现方法论审慎。

**S3. Hacking 分类法详尽实用** [R1, R2 一致]。8 种 hacking 模式（CE/TS/PG/tautological collapse/repetition/contradiction/complexity-without-utility/query-as-fact），每种有 FOL/Prolog 示例、ISR 交互分析、prevalence 统计和检测标准，构成可操作的诊断 checklist。

**S4. 负面结果的诚实报告** [R1, R2 一致]。ISR-as-reward Goodhart 效应、LLaMA-3.2-3B 冷启动失败、ProofFOL p=0.10 标为 exploratory、checkpoint 被删除无法 audit——透明披露增强可信度。

**S5. 统计分析框架合理** [R1]。Fisher exact tests + Bonferroni 校正（k=14）+ CMH 分层检验 + premise-count deconfounding。

**S6. 引用覆盖基本完整** [R2]。39 篇引用无 orphan/missing，近期关键工作已覆盖。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. 单模型 (Qwen3-4B) + 3 seeds 无法支撑标题的通用性声明** [R1-W1, R2-W1; 交叉后完全一致]
- 全部实验基于 Qwen3-4B 一个模型。3 seeds 收敛到质性完全不同的模式（seed 42 CE 87%, seed 43 repetition collapse, seed 44 TS 100%），PR σ=47pp。
- LLaMA-3.2-3B 冷启动失败是能力不足，不构成泛化验证。
- 标题 "GRPO-Trained Neurosymbolic Reasoning" 暗示通用性，但 N=1 模型 + N=3 seeds 的证据不支撑此范围。
- **行动项**: 增加至少 1 个不同架构/规模模型（如 7B/8B），或将 claims 明确限定为 "on Qwen3-4B"。增加 seeds 至 5-8。

**W2. 摘要 headline 数字追溯困难，存在选择偏差** [R1-W2; R2 交叉 AGREE]
- "99.5% structural collapse" 来自 seed 42 单 seed（ISR 0.642→0.003），该 seed 恰好是 PR 最低的（0.18）。
- "≤1.4% genuine in converged seeds" 无法从 Table 7 直接追溯。不同 seeds 使用不同训练步数（500 vs 1000）使 pooled 统计复杂化。
- **行动项**: 明确每个数字来源（seed, step, condition）；改用 3-seed mean±std 或标注为单 seed 结果。

**W3. ISR 对 TS hacking 完全失效，诊断能力比论文暗示的更窄** [R1-W3; R2 交叉 AGREE 提升为 Must-Fix]
- Seed 44 exec-only: ISR=0.742 但 N-H=0%（100% TS）。P→P tautology 天然产生 ISR≈1。
- ISR 的 false negative rate 对 TS 类退化为 100%。
- Method §3.2 定义 ISR=1 为 "full necessity" 但未讨论此系统性盲区。
- **行动项**: 在 §3.2 明确声明 ISR 对 TS 的盲区；将 ISR + text-match classifier 联合使用作为推荐的完整诊断方案。

**W4. 正文溢出至第 9 页（~8.2 页），超出 EMNLP 2026 的 8 页限制** [视觉审查 Critical]
- Section 5 Discussion and Conclusion 溢出至 page 9 左栏约 1/3。EMNLP 2026 strict 8-page limit，存在 desk-reject 风险。
- **行动项**: 压缩正文至 8 页以内。

### Should-Fix

**W5. LOO 独立性假设讨论不充分** [R1-W4; R2 AGREE]
- ISR 声称为 "conservative lower-bound"，但未量化 gap。Premise 间链式依赖（A→B→C）场景下 LOO 可能严重低估真实结构依赖。
- **行动项**: 在 §3.2 或 Limitations 讨论 LOO 假设失败场景及偏差方向；提及 Shapley value/pairwise ablation 作为更 tight 的替代。

**W6. Fisher exact test pooling 3 seeds 可能违反独立性假设** [R1-W6; R2 AGREE]
- 3 seeds 共享训练数据和架构，pooling 可能膨胀样本量。Main text 主要引用 pooled Fisher 结果，CMH 分层检验仅在 Appendix。
- **行动项**: Main text 优先报告分层或 per-seed 检验结果。

**W7. 乘法耦合未充分 deconfound** [R1-W7; R2 AGREE]
- r = r_exec · (1 + β·ISR) 使 ISR 完全依赖 execution 成功。未测试加法耦合对照。
- **行动项**: 讨论乘法耦合局限性；如无加法实验，明确说明无法分离 coupling structure 影响。

**W8. ProofFOL GPT-4o 翻译偏差可能混淆跨数据集结论** [R1-W8; R2 AGREE]
- Silver-standard 翻译可能引入系统性偏差。p=0.10 borderline 结果进一步削弱跨数据集声明。
- **行动项**: 讨论 GPT-4o 翻译可能引入的 systematic bias。

**W9. 与 Kim et al. (2026) 差异化需加强** [R2-W2; R1 REBUT 降为 Should-Fix]
- 两者都在 FOLIO 上研究 formalization gaming。当前 Related Work 仅一句话区分。
- R1 指出实质差异存在（training vs inference, LOO vs detection, trajectory vs static），但论述不够展开。
- **行动项**: Related Work 增加 2-3 句系统对比。

**W10. 500 训练 + 100 评估样本偏小** [R1-W5; R2 部分 AGREE]
- 100 eval 样本上 N-H=4.7% 仅约 5 个样本，hacking mode 比例估计不可靠。
- **行动项**: 讨论 data scale 对结论的 sensitivity。

**W11. Abstract 信息过载** [R2-W5; R1 AGREE]
- ~250 词内压入 4 个独立发现和大量数字（7+ 数字、3+ p 值），可读性受损。
- **行动项**: 精简至核心 message + 1-2 个最关键数字。

### Minor

**W12.** 术语/缩写密度过高（ISR/ISR*/STA/CE/TS/PG/N-H 等 ~17 个缩写）[R2-W7; R1 AGREE]
**W13.** Figure 4, 5 内部文字（axis label, legend）偏小 [R2-W8; R1 AGREE; 视觉审查同]
**W14.** Seed 43 使用 sampling eval (T=0.7) 而非 greedy，影响 cross-seed 比较 [R1-W9; R2 AGREE]
**W15.** Hacking mode 分类器人工验证仅 50 样本，Wilson CI [85%, 99%] 过宽 [R1-W10; R2 AGREE]
**W16.** 前 3 页纯文本无 display item，page 8 堆叠 3 个 items，视觉节奏不均 [视觉审查 Warning]

---

## Reviewer Consensus [AGREE]

1. **单模型泛化** (W1): 最核心问题。两位 Reviewer 完全一致列为 Must-Fix。
2. **Headline 数字** (W2): 两位一致同意追溯困难且存在选择偏差。
3. **ISR TS 盲区** (W3): R1 初审提出，R2 交叉后提升为 Must-Fix。
4. **诊断框架价值** (S1): 一致认为 STA/ISR 的诊断贡献是论文最大优势。
5. **Hacking taxonomy** (S3): 一致认为实用且详尽。
6. **LOO 假设/Fisher pooling/乘法耦合/ProofFOL 质量/数据规模**: 均达成 Should-Fix 共识。

## Reviewer Divergence [REBUT]

1. **Kim et al. 区分 — Must-Fix vs Should-Fix**: R2 认为与 Kim et al. 核心观察高度重叠（Must-Fix）；R1 REBUT 指出 training-time trajectory analysis vs. inference-time detection 是实质性差异（Should-Fix）。**Director 采纳 R1 判断**: 两者方法论和发现层面有本质差异，补充 2-3 句对比即可，降为 Should-Fix。

2. **Goodhart 可预测性**: R2 认为 Goodhart 发现理论上高度可预测，削弱 Excitement（Should-Fix）；R1 REBUT 指出方向可预测 ≠ 机制可预测（TS 5× amplification、multiplicative coupling 分析为新信息）。**Director 判断**: 双方均有道理。Goodhart 方向确实可预测，但具体量化结果和 8 种 hacking 模式的刻画超出先验预测。此为论文的结构性 novelty 限制，非修改可完全解决。

3. **Mitigation 需求**: R2 认为缺乏 actionable mitigation 削弱影响力（Should-Fix）；R1 REBUT 指出诊断论文不必提供解法（引 McCoy et al. 2019 先例），§5 已有方向讨论。**Director 采纳 R1 判断**: 论文定位为诊断工具，§5 的 mitigation 方向讨论已足够。

4. **Overall Score**: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)。核心分歧在 Excitement（R1: 3.5/5, R2: 2.5/5）。R1 认为应用迁移型创新有足够价值；R2 认为 LOO 非新、Goodhart 可预测、无解法使 Excitement 不足。

---

## Questions（需作者在 rebuttal 中澄清）

**Q1.** "≤1.4% genuine (in converged seeds)" 的精确计算：来自哪些 seeds、哪些 steps、哪些 condition 的哪些样本子集？请提供可追溯的 derivation。

**Q2.** Table 7 不同 seeds 训练步数不同（500 vs 1000）。为什么不统一步数再做 pooled comparison？

**Q3.** ISR 对 TS hacking 失效（seed 44: ISR=0.742 但 N-H=0%）。是否考虑 ISR + classifier 的 unified metric？

**Q4.** β=0.3 reward collapse（seed 42 PR=0.18）——是 β 过大还是 multiplicative coupling 缺陷？

**Q5.** LLaMA-3.2-3B 冷启动失败可能是 tokenizer/pretraining 差异而非 "capability" 差异？

**Q6.** "sufficient FOL generation capability" 的定量标准是什么？

**Q7.** ISR=0 无法区分"冗余"和"退化"——如何量化 redundancy vs. degradation 比例？

---

## Missing References

**应补充**（两位 Reviewer 一致或 Director 确认相关）:
1. **Geirhos et al. (2020), "Shortcut Learning in Deep Neural Networks," Nature Machine Intelligence** — ISR 揭示的退化本质上是 shortcut learning 在 neurosymbolic RL 中的体现，此综述提供理论框架。[R1 推荐, R2 AGREE]
2. **Lean 4 RL 工作**（Kimina-Prover, Leanabell-Prover）— 形式验证 RL 的 parallel track，Limitations 中应提及。[R2 推荐]

**待验证后补充**（R2 推荐，arXiv ID 需确认真实性）:
3. Xie et al. (2025) "Pushing the Boundaries of Natural Reasoning" (arXiv:2601.22642)
4. "Spurious Rewards Paradox" (arXiv:2601.11061)
5. "Reward Hacking Mitigation using Verifiable Composite Rewards" (arXiv:2509.15557)

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿（项目配置中无 `external_review.paperreview_ai.enabled`）。

---

## Visual Layout Check

**状态**: ✅ done（耗时 ~4 分钟）

**发现**:
| 严重度 | 位置 | 问题 |
|--------|------|------|
| **Critical** | Page 9 | 正文溢出至第 9 页（Section 5 Discussion, ~8.2 页），超出 EMNLP 2026 的 8 页限制，**desk-reject 风险** |
| Warning | Page 1-3 | 连续 3 页纯文本无 display item，建议将 Figure 1 提前至 page 2-3 |
| Warning | Page 8 | 单页堆叠 3 个 display items（Figure 4 + Figure 5 + Table 2），视觉拥挤 |
| Warning | Page 5 | 整页无 display item |
| Info | Page 8 | Figure 4, 5 内部文字偏小（axis label, legend），建议 ≥ 8pt |
| Info | Page 4 | Figure 1 panel (a) 标注偏小 |
| Info | Page 7 | Figure 3 与 Figure 2 使用不同色彩语义，建议确认跨图一致性 |
| Info | Page 11 | Limitations 位置正确（References 后、Appendix 前），符合 ARR 格式 |

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**Soundness: 3/5** — 实验设计系统但单模型 + 3 seeds + 高方差限制定量声明可靠性；headline 数字追溯困难；ISR 对 TS 盲区未在方法论中声明。

**Excitement: 3/5** — 诊断框架有创造性（LOO→neurosymbolic RL），hacking taxonomy 实用，揭示了真实且被忽视的问题。但 LOO 本身非新，Goodhart 方向可预测，单模型限制了影响力。R1（3.5）与 R2（2.5）的中位。

**Reproducibility: 3.5/5** — 超参数表格完整，代码承诺开源。但 seed 43/44 ISR checkpoints 被删除无法 audit，seed 43 使用不同 eval 协议，不同 seeds 训练步数不一致。

**Confidence: 4/5** — 两位 Reviewer 均仔细阅读全文含附录，熟悉 neurosymbolic reasoning 和 RL reward hacking 文献。

**理由**: 论文提出了一个有价值的诊断框架（STA/ISR），揭示了 GRPO 训练中被 prove rate 隐藏的结构退化——这是一个真实的发现。Hacking 分类法详尽，统计分析框架合理，写作质量总体良好。

降分的核心原因：
1. **泛化瓶颈**（W1）: 单模型 + 3 seeds 是最大结构性弱点，两位 Reviewer 完全一致。
2. **ISR 诊断范围**（W3）: ISR 对 TS 盲区意味着它不是独立可靠的诊断指标，需搭配 classifier，但论文 framing 暗示更强的独立诊断能力。
3. **格式问题**（W4）: 正文溢出 8 页，存在 desk-reject 风险。
4. **Headline 数字**（W2）: 追溯困难且有选择偏差，损害可信度。

**升分路径**: 若 rebuttal/revision 解决 W1（增加模型或缩窄 claims）+ W2（修正 headline 数字）+ W3（Method 中声明 ISR 盲区）+ W4（压缩至 8 页），可升至 3.5 (Borderline Conference)。进一步增加模型验证可达 4.0 (Conference)。当前版本适合 Findings。

---

## Detailed Comments

### §1 Introduction
- "93% prove rate" 应标注为单 seed 结果或改用 mean±std
- Contribution (C1)-(C3) 陈述准确，与实验对应清晰
- "ISR=1 indicates full necessity" 需 caveat: 对 tautology 也成立

### §2 Related Work
- 与 Kim et al. (2026) 区分需展开 2-3 句（当前仅一句）
- 缺 Geirhos et al. (2020) shortcut learning 综述
- 现有引用覆盖完整，无 orphan/hallucinated 引用

### §3 Method
- Algorithm 1 清晰。ISR 定义（Eq. 1）无歧义
- **关键缺失**: §3.2 未讨论 ISR 对 TS 类退化的系统性盲区
- LOO 独立性假设（§3.2 末尾）讨论存在但不充分——"conservative lower-bound" 需量化
- ISR limitations paragraph 良好但应提升可见性

### §4 Experiments
- §4.1 Setup: seed 43 sampling eval 需更显著标注
- §4.2 Diagnostic: Figure 2 trajectory 直观有效。"99.5% collapse" 需标注为 seed 42 单 seed
- §4.3 Goodhart: Premise-count deconfounding 分析（1.06×）是重要的 self-critical 结果。乘法耦合讨论需扩展
- §4.4 Cross-domain: ProofFOL p=0.10 标为 exploratory 是正确的。GPT-4o 翻译偏差需讨论
- Table 1: 聚合方式清晰标注。ISR β=0.1 ISR* 列省略有理由但需解释
- Table 2: Hacking taxonomy 表格信息密度高但可读

### §5 Discussion and Conclusion
- Mitigation directions 3.5 行虽简短但涵盖了方向（multi-granularity, filter, ensembling, constrained opt）
- 溢出至 page 9，需压缩

### §6 Limitations
- 内容充实，覆盖模型、数据、统计、ISR 局限性
- Data scale 段落是良好补充

### Appendix
- Table 7 per-seed 详细结果完整
- Hacking mode 定义（Appendix D）详尽实用
- O(1) vs O(n) 消融（Appendix E.3）提供了有价值的对比
- ProofFOL 构建流程（Appendix A）需补充翻译偏差分析
