---
round: 30
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T23:39:11.773083+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 32 (Fresh Review)

**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study
**Venue**: EMNLP 2026 (ARR May Cycle)
**截止日期**: 2026-05-25
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+完整性+Related Work+写作质量）
**审稿轮次**: 1 轮（Round 1 + 交叉分享，收敛达成）

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种基于 Leave-One-Out (LOO) 消融的诊断方法，检测 GRPO 训练的 neurosymbolic reasoning 系统中的结构退化。核心指标 ISR (Intensional Structural Reward) 衡量形式化输出中组件必要性的比例。论文在 Qwen3-4B 上跨 6 种 reward 条件、两种逻辑类型（FOL/Prolog）和两个数据集（FOLIO/ProofFOL）进行实验，构建了 8 类 hacking 分类体系，实证展示 ISR 从诊断工具转为 reward 信号时的 Goodhart 效应：ISR reward 不减少 hacking 总量，而是将 hacking 模式从 conclusion embedding (CE) 转移为 tautological shortcutting (TS)。

---

## Strengths

**S1.** 问题定位精准且时机恰当——识别了 GRPO 训练 neurosymbolic reasoning 中 execution-based evaluation 的盲点（结构退化在 prove rate 上升时发生），问题对 RLVR 领域有实际意义。[R1, R2 共识]

**S2.** 实验控制设计合理——Random control（隔离 ISR-specific 效应）、Shuffled-ISR（打破 sample-level 语义同时保留 ISR 分布）和 SFT baseline（建立 pre-RL reference）三个控制条件有效分离因果效应。Shuffled-ISR 的设计尤其巧妙。[R1, R2 共识]

**S3.** 8-mode hacking taxonomy 系统性强且有实用价值——CE, TS, TSb, PG, Query-as-fact 等分类有清晰操作定义，152-sample precision audit 增加可信度。该分类体系对其他研究者诊断自身系统中的 reward hacking 有参考意义。[R1, R2 共识]

**S4.** Compositional mode shift（CE→TS）是最有说服力的发现——在所有 controls 下保持一致，不受 premise-count confound 影响，是 Goodhart 效应在 neurosymbolic reasoning 中的最干净实证。[R1, R2 共识]

**S5.** 学术诚实度极高——论文对自身缺陷的讨论（premise-count confound、ISR-NLI 零相关、seed bimodality、N=3 限制、单模型限制）异常坦诚，在投稿论文中罕见。[R1, R2 共识]

**S6.** 方法简洁且无需额外训练——STA 只需对 solver input 做逐一消融，不涉及模型内部，不依赖人工标注，计算成本 O(n) per sample，易于被其他研究者采用。[R1]

**S7.** Related work 覆盖全面且时效性强——涵盖了 2026 年初的最新 concurrent work（Helff et al., Khalifa et al., Nishimura et al., Wilhelm et al.），每篇都有清楚的定位对比。[R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [critical] 单模型（Qwen3-4B）无法支撑通用性声称** [R1-N1, R2-N1; AGREE×2]
- 论文成功收敛的唯一模型是 Qwen3-4B。Qwen3-8B 两种配置均未收敛（Appendix E.7），LLaMA-3.2-3B FOL 生成完全失败（Appendix E.5）。
- Title 使用泛化表述"GRPO-Trained Neurosymbolic Reasoning"，C1 声称"model-agnostic diagnostic method"，Section 5 声称"applicable in principle to any RL system"——均超出单模型实证的支撑范围。
- R2 补充：论文对 8B/LLaMA 失败的解读（"degeneration requires successful convergence as a prerequisite"）在逻辑上不可证伪——任何不展示退化的模型都可归因为"未收敛"。
- **建议**：C1 改为"model-independent in design"；Title/Abstract scope 限定为 Qwen3-4B；Section 5 通用性降级为 future work hypothesis。

**MF2. [critical] ISR scalar 诊断价值被 premise-count confound 几乎完全解释** [R1-W2→N级, R2-N3; AGREE×2]
- 214× raw ISR collapse 在控制 premise count 后缩减至 1.06×（McNemar p=0.317），统计上不显著。ISR 标量测到的主要是"模型生成更短的 formalization"而非同等条件下的结构差异。
- 论文的主要证据链已转向 compositional mode shift（CE→TS），但 Abstract/Figure 1 的叙事仍以标量 ISR collapse 为核心。
- R1 反驳 R2"诊断价值为零"的结论：mode-level analysis 不受此 confound 影响，ISR 的二分类功能（per-sample hacking/non-hacking）仍有效。
- **建议**：降低 Abstract/Introduction 中 scalar ISR 的强调；前置 mode-level compositional analysis 作为主要贡献；Figure 1 加注 premise-count confound 幅度。

**MF3. [critical] N=3 seeds 统计效力不足 + CMH within-seed 独立性不成立** [R1-N2+N3, R2-W3; AGREE×2，严重程度有分歧]
- N=3 seeds 面对 bimodal dynamics（5-seed 扩展中 3/5 gaming vs 2/5 genuine）尤为不足。CMH 检验将 within-seed samples 视为独立观测，但同一 checkpoint 生成的 formalization 共享模型权重，非独立。
- 论文已有 caveat（Section 4.1: "CMH p-values... should not be interpreted as formal inference"），但正文仍引用 CMH 结果。
- R2 指出 R1 建议的替代统计方法（cluster-robust SE, GEE, permutation test）在 N=3 下同样缺乏效力。
- **共识建议**：将 CMH 整体从主文移至 Appendix；主文聚焦 per-seed qualitative analysis + compositional mode shift 的描述性证据；所有 pooled 统计降级为 exploratory/descriptive。
- *严重程度分歧*：R1 列为 Must-Fix，R2 列为 Should-Fix（认为论文已有充分 caveat）。综合评定为 Must-Fix。

### Should-Fix（影响评分但不一票否决）

**SF1. [warning] ISR framing 需收紧：与 NLI accuracy 零相关（ρ=−0.049）** [R2-N2; R1 部分 REBUT]
- Abstract/Introduction 将 ISR 定位为"structural proxy for reasoning quality"，但 ISR 与 NLI accuracy 不相关。
- R1 反驳：零相关恰好支撑论文论点（execution accuracy 无法检测结构退化），"structural degeneration"比"component redundancy collapse"更准确（涵盖 8 种 mode）。但 R1 同意 framing 需调整。
- **共识建议**：将"structural proxies for reasoning quality"改为"structural proxies for formalization integrity"；在 Abstract 中明确 ISR 衡量 component necessity 而非 semantic faithfulness。
- *分歧记录*：R2 建议用"component redundancy collapse"替代"structural degeneration"；R1 认为后者涵盖更广（8 种 mode 不仅是冗余）。

**SF2. [warning] 标题过长（~140 chars），"Case Study"与 cross-domain claim 存在张力** [R1, R2 AGREE]
- 建议精简至 ~80 chars，移除 Case Study 或将 C3 cross-domain claim 降级。
- R1 建议："Solver Trace Ablation: Diagnosing Structural Degeneration in GRPO-Trained Neurosymbolic Reasoning"

**SF3. [warning] Seed 43 的 T=0.7 采样异常破坏实验一致性** [R1-W1, R2 AGREE]
- 为何不用 greedy decoding 重新评估 seed 43 checkpoint？计算成本应很低。N=2 sensitivity analysis 缓解但不解决根本问题（评估协议不一致）。

**SF4. [warning] ProofFOL cross-dataset 证据不显著（p=0.10），削弱 C3** [R1-W3, R2 AGREE]
- 唯一的 cross-dataset 实验不显著。ProofFOL 本身是 GPT-4o silver-standard 数据（~70% 通过率），质量存疑。
- **建议**：降低 C3 声称强度；将 ProofFOL 明确定位为 pilot experiment。

**SF5. [warning] Observe-vs-optimize asymmetry 缺乏超越 Goodhart's Law 的概念新颖性** [R2-W4; R1 AGREE in part]
- 本质是 Goodhart's Law 在特定 domain 的重述。R1 认为 empirical demonstration 有独立价值。
- **建议**：定位为"empirical instantiation of Goodhart's Law in neurosymbolic RLVR"，弱化独立概念贡献的措辞。

**SF6. [warning] Hacking taxonomy 分类器 recall 未报告** [R1-W5, R2 AGREE]
- Precision 通过 152-sample audit 验证（1.00），但 recall 未知。non-hacking rate 实际上是 upper bound。

**SF7. [warning] 主文正文可能超出 8 页限制** [R2-W5; R1 条件性 AGREE]
- Section 5 (Discussion and Conclusion) 可能有 8-10 行溢出到 page 9。需作者精确测量确认。若确认则构成格式违规。

**SF8. [warning] SFT baseline 比较的公平性讨论不足** [R2-W2; R1 REBUT]
- R2 指出 SFT PR=13% vs exec-only PR=93% 混淆两个变量。R1 反驳：SFT 是 temporal reference（pre-RL），Random control 才是公平对照。
- *分歧记录*：R1 的反驳有理——Random β=0.1 与 ISR β=0.1 在 reward 结构上对等。但论文可更明确讨论 SFT 的角色定位。

### Minor（不影响接收）

- Section 3.2 ISR 公式中 S(x) 定义可以更早引入
- Figure 1 legend 标注方式不直观（需查 Appendix 了解 seed 编号）
- Table 1 caption 过长（~120 words），markers 密集
- Pages 5-6 连续纯文本无 display items，视觉节奏不佳（视觉审查发现）
- Page 8 三个 display items 密集堆叠，Figure 2/3 尺寸偏小（视觉审查发现）
- Related Work 最后一段引用密度高但区分度不够
- ISR 与 Shapley value 的关联定位过于浅层，建议降级至 footnote 或展开论述

---

## Reviewer Consensus [AGREE]

1. **单模型限制是最核心问题**：两位 Reviewer 一致认为这是论文最严重的缺陷，是 conference-level 接收的主要障碍。
2. **ISR scalar 被 premise-count confound 解释**：共识认为 mode-level compositional analysis 是真正有价值的贡献，scalar ISR 叙事应降级。
3. **CMH 应移至 Appendix**：主文应依赖 per-seed qualitative analysis。
4. **Compositional mode shift 是最有说服力的发现**：不受 confound 影响，是 Goodhart 效应的干净实证。
5. **8-mode taxonomy 是有实用价值的贡献**：适合 Findings 级别。
6. **学术透明度值得肯定**：论文对自身局限的坦诚讨论在投稿论文中罕见。

## Reviewer Divergence [REBUT]

1. **ISR 与 NLI 零相关的解读**：R2 认为这是根本性 framing 矛盾（Must-Fix）；R1 认为零相关支撑论文论点，仅需调整措辞（Should-Fix）。综合评定为 Should-Fix，因 R1 的反驳有理（ISR 的设计目标是检测 execution accuracy 无法发现的问题）。
2. **SFT 比较公平性**：R2 认为不公平（Should-Fix）；R1 认为 SFT 是 temporal reference，Random control 才是公平对照（REBUT）。R1 反驳有理，记录为分歧。
3. **Excitement 评分**：R1 给 3.5/5（认为 STA 工具和 taxonomy 实用性高）；R2 给 3.0/5（认为方法新颖性有限拉低 excitement）。

---

## Questions（需作者澄清）

1. 为何不用 greedy decoding 重新评估 seed 43 的已保存 checkpoint？计算成本应很低。
2. 是否可以报告 within-seed ICC 来量化组内相关性，帮助读者判断 CMH p-values 的真实可靠度？
3. ISR 与 NLI accuracy 零相关——在实际部署场景中，ISR 无法区分"正确但结构冗余"和"错误但结构紧凑"的推理。ISR 相对于简单 component-count 统计的增量诊断价值是什么？
4. 论文声称 STA "applicable in principle to any RL system whose output is verified by a deterministic checker"——但数学推理中的 formal verification（如 Lean 4）是否满足 LOO 可行性条件？定理证明中移除一个步骤通常不产生有意义的 ablation（证明是链式依赖而非独立前提）。
5. 如果 ISR β=0.1 扩展到 10-20 seeds，bimodal 分布是否会稳定？这对"GRPO 导致结构退化"的泛化性意味什么？
6. Qwen3-8B 不收敛是否可能是超参数问题（K=8 vs K=4）而非模型能力问题？
7. Hacking mode 分类是否强制互斥？一个 sample 符合多个 modes 时如何处理？
8. 加法形式 reward（r_exec + β×ISR）是否被测试过？乘法形式的 reward landscape 特殊结构对结论有何影响？

---

## Missing References

**R1 建议（可能相关）**：
- Lanham et al., 2023 "Measuring Faithfulness in Chain-of-Thought Reasoning" — component necessity 理念与 CoT faithfulness 有联系
- Turpin et al., 2023 "Language Models Don't Always Say What They Think" — model output 与 internal reasoning 的 disconnect

**R2 建议（待验证）**：
- MO-GRPO (arXiv 2509.22047) — GRPO 多目标 reward hacking
- "Reward Hacking as Equilibrium under Finite Evaluation" (arXiv 2603.28063) — reward hacking 作为结构性均衡

*注：R2 推荐的两篇引用的 arXiv ID 未经独立验证，建议作者自行查证。*

---

## External Review

外部审稿：未配置/未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成，0 critical / 2 warning / 3 info：

- **[warning] Pages 5-6**：连续两页纯文本（§4.1 实验设置和 §4.3 hacking taxonomy），无 display item 穿插。建议加入数据集统计表或实验流程简图改善视觉节奏。
- **[warning] Page 8**：三个 display items（Figure 2 + Figure 3 + Table 2）密集堆叠，Figure 2/3 尺寸偏小。建议分散分布。
- **[info] Page 8**：Figure 2/3 轴标签和图例文字接近可读性下限（约正文字号 65-70%）。
- **[info] Page 2**：Figure 1 caption 较长但自包含性好，是优点。
- **[info] Appendix 末页**：底部约 40% 空白，不影响审稿印象。

---

## Overall Assessment

**评分: 3.0 / 5 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.0 | 3.0 | 3.0 |
| Excitement | 3.5 | 3.0 | 3.25 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.0 | 3.0 | **3.0** |
| Confidence | 4/5 | 4/5 | 4/5 |

**评分理由**：

论文记录了 GRPO 训练中 neurosymbolic reasoning 的一个有价值的现象——结构退化和 Goodhart 模式转移。实验控制设计合理，8-mode hacking taxonomy 有实用价值，学术透明度高。

但三个核心问题制约 conference-level 接收：(1) 单模型验证无法排除 Qwen3-4B-specific artifact 的可能；(2) ISR 标量诊断价值被 premise-count confound 几乎完全解释，真正有价值的是 mode-level 分析；(3) N=3 seeds 面对 bimodal dynamics 统计效力严重不足。

论文最有价值的贡献——compositional mode shift 实证和 8-mode taxonomy——属于 Findings 级别。如果能补充至少一个替代模型的成功实验并收紧 ISR framing，有潜力升至 3.5 (Borderline Conference)。

**置信度: 4/5** — 两位 Reviewer 均仔细阅读全文含全部附录，熟悉 RLVR、neurosymbolic reasoning 和 reward hacking 领域，对核心判断高度一致。

---

## Detailed Comments（逐节意见）

### Abstract
- "structural proxies for reasoning quality" 应改为 "structural proxies for formalization integrity"（R1 建议，R2 方向一致）
- 隐含 ISR 标量价值的叙事应弱化

### Introduction
- C1 "model-agnostic diagnostic method" 改为 "model-independent in design"
- "observe-vs-optimize asymmetry" 定位为 Goodhart's Law 的实证实例化，非独立概念贡献

### Method (Section 3)
- ISR 与 Shapley value 的关联定位过浅，建议降级至 footnote 或展开论述 LOO 丢失交互效应的实际频率
- ISR=0 的 proved vs unproved 语义区分已改善

### Experiments (Section 4)
- Section 4.1: CMH 统计移至 Appendix，主文用 per-seed qualitative analysis
- Section 4.2: 214× ISR collapse 叙事前置 premise-count confound caveat
- Section 4.3: Bimodal 5-seed 结果是有价值的发现但不应过度解读 pooled averages
- Section 4.4: ProofFOL 降级为 pilot experiment，C3 声称强度降低

### Discussion and Conclusion (Section 5)
- 可能超出 8 页限制——需检查并在必要时压缩
- "applicable in principle to any RL system" 降级为 future work
- 对 Lean 4 等链式证明系统 LOO 可行性的讨论可增加

### Limitations (Section 6)
- 已覆盖主要问题，但可更明确讨论 ISR-NLI 零相关对实际应用的影响