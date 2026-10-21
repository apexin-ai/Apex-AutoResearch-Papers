---
round: 12
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-24T23:10:31.397203+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — trace-verdict-study (Round 12)

**Venue**: EMNLP 2026 (ARR)
**Reviewer 配置**: 2 人（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 概念完整性）
**轮次**: Round 1 初审 + 交叉回应，1 轮收敛

---

## Summary

本文研究执行 trace 表示形式对 LLM test verdict prediction 性能的影响。通过 7 种 trace 条件的系统消融实验（涵盖 4 个模型、3 种架构），发现完整 trace 不仅未提升性能，反而相较于无 trace baseline 导致退化（最大 ~23pp）；仅包含 exception 信息的精简表示即可达到最优或接近最优效果。论文通过尾部截断实验揭示了 384–512 token 的 phase transition，并用梯度掩码实验尝试解释退化机制。

---

## Strengths

**S1. 系统性消融设计（R1-S1, R2-S1）。** 7 种 trace 条件（no.trace → full.trace）的递进消融覆盖了从无 trace 到完整 trace 的连续体，设计思路清晰，粒度适当。Table 1 的多条件对比和 Table 2 的 component 分解提供了丰富的实证证据。两位 Reviewer 一致认为这是本文最大的方法论优势。

**S2. 多模型多架构验证（R1-S2, R2-S4）。** 跨 4 个模型（Qwen2.5-1.5B/7B, CodeLlama-13B, DeepSeek-Coder-6.7B）和 3 种架构的验证增强了结论的泛化性。可复现性强：完整超参数表（Appendix B）、代码结构描述。

**S3. 尾部截断 phase transition（R1-S5, R2-S2）。** Figure 3 揭示的 384–512 token sharp transition 是本文最可验证、最具实践指导意义的发现，为 practitioner 的 trace 截断策略提供了具体参考。

**S4. 训练动态分析（R1-S3）。** Figure 5 展示的收敛差异（exception.only ~50 steps 收敛 vs. full.trace 持续振荡）从过程层面补充了最终性能差异的证据。

**S5. 透明度（R1-S6, R2-S4）。** DebugBench OOD 验证、tokenizer 失败的坦诚报告（Appendix F）体现了良好的研究规范。

---

## Weaknesses

### Must-Fix

**W1. 核心发现的同义反复性（R2-W1; R1 部分同意）。** 在 assert-based Python 测试中，test failure 必然产生 exception，因此 "exception 信息有效预测 verdict" 接近 tautological。Regex baseline B4 达 93.61%，exception.type.only 达 100%（Table 20），直接佐证了这一点。R1 指出 full-trace 退化发现本身非同义反复，论文的核心贡献在于定量展示退化机制——但论文当前 framing 将 "exception-only 有效" 作为主要卖点而非退化机制，加剧了 tautology 印象。作者需在 Discussion 中坦诚讨论 exception=verdict 的 tautological 关系，并将贡献重心明确转向退化机制的发现和分解。
- R1: Should-Fix | R2: Must-Fix | **Director: Must-Fix**（结构性 framing 问题）

**W2. 梯度掩码实验的 forward-pass confound（R1-W1, R2-W6; 双方均同意）。** §4.4 实验中模型训练和推理均处理 ~150 token 紧凑输入，从未在推理时面对 ~2,000 token full trace。实验仅证明"梯度信号数量不是主要瓶颈"，但对"推理时无关 token 是否降低预测质量"无 evidence。论文在 §4.4 承认此 confound 但未充分讨论其对 "mechanistic explanation" 声明的影响。R1 建议的"错配训练-推理"实验（用 exception-only 数据训练 + full-trace 推理，或反之）可直接检验此问题。
- R1: Must-Fix | R2: Should-Fix → 交叉后升级 | **Director: Must-Fix**（直接影响三大贡献之一）

**W3. 单 seed 结果（R1-W2; R2 同意）。** 主要结论基于单一随机种子。DeepSeek VOTA seed 42 的灾难性失败（84.45%, Appendix F）直接证明 seed variance 可极大。核心对比（exception.only vs. full.trace, ~18-23pp gap）主效应可能稳健，但中间条件排序稳定性存疑。3-seed 实验成本低且可显著增强可信度。
- R1: Must-Fix | R2: Agree | **Director: Must-Fix**

**W4. Claims 过度泛化（R1-W4/W7, R2-W3/W8; 双方均同意）。** 多处声明超出证据支撑：(a) 标题无限定，暗示结论适用于所有 LLM + trace 场景；(b) "input curation > model scaling" 基于 1.5B–13B（4 模型，8.5× 参数范围），不足以支撑 scaling 声明；(c) "mechanistic explanation" 实为 correlational input ablation，非因果机制解释；(d) Tokenizer failure 削弱 "architecture-independent" 论断。
- R1: Must-Fix | R2: Must-Fix | **Director: Must-Fix**

### Should-Fix

**W5. Verdict prediction 作为 proxy task 动机不足（R2-W2; R1 部分同意）。** Verdict prediction 是一个接近可被规则解决的二分类任务（model-free r=0.918），在此任务上的发现不一定迁移到需要 intermediate trace state 的复杂任务（fault localization、program repair）。将其定位为 controlled diagnostic setting 是合理的研究设计选择，但论文未充分讨论任务难度对 trace utility 结论的边界条件。TraceCoder (ICSE 2026) 在 fault localization 上得到相反结论（更多 trace 有益），这一对比至关重要。
- R1: Should-Fix | R2: Must-Fix | **Director: Should-Fix**（设计合理，framing 需限定适用范围）

**W6. Related Work 覆盖不足（R2-W4; R1 同意）。** 三个关键缺失：(a) SBFL 与本文 exception-only 结论的精简信息理念有相似之处；(b) Information Bottleneck 理论（Tishby et al., 2000）——移除冗余信息提升性能是 IB 的核心预测，本文是其在 code SFT 中的实例化；(c) TraceCoder 反向发现——trace utility 随任务复杂度变化的 boundary condition 讨论不能缺失。

**W7. VOTA 超参数敏感性分析缺失（R1-W6; R2 同意）。** Algorithm 1 中 loop compression 阈值（≤2 iterations）直接影响 token 数量和信息密度，但无敏感性实验。

**W8. 数据集和任务多样性不足（R2-W5; R1-W4 相关）。** 主实验和 OOD 验证（DebugBench）均为 Python function-level，不构成真正的 task/language diversity。DebugBench margin 仅 3.29pp，证据强度有限。

**W9. 多重比较校正缺失（R1-W3; R2 同意但认为次要）。** 多条件对比未做 Bonferroni 或 FDR 校正。核心对比效应量极大（18-23pp），校正后仍显著，但次要对比可能受影响。

**W10. 数据生成分布偏差（R1-W5; R2 部分反驳）。** GPT-4o 生成的 candidate solutions 可能有分布偏差。R2 提出三点缓解证据（DebugBench OOD 验证、8+ exception types 覆盖、机制不依赖特定 error pattern），但用其他模型交叉验证仍有价值。

### Minor

**W11. Abstract 数字过多（R2-W7）。** 建议精简至最核心的 2-3 个数字。

---

## Questions

**Q1.** 如果用 exception-only 数据训练的模型在推理时接收 full trace 输入，性能如何变化？反之呢？（直接检验 W2 的 forward-pass confound）

**Q2.** 384–512 token phase transition 的位置是否随模型规模或 context window 大小变化？

**Q3.** 在 fault localization 等需要 trace 中间状态的任务上，是否观察到相同的 full-trace 退化现象？

**Q4.** Table 2 的 component ablation 在 Qwen-7B 之外的模型上是否保持相同的 component ranking？

**Q5.** exception.type.only 在 DebugBench 上同样达到 100%？如果是，这是否进一步佐证 tautology 论点？

---

## Missing References

1. **Tishby, N., Pereira, F. C., & Bialek, W. (2000).** The Information Bottleneck method. — 移除冗余信息提升性能的理论框架，本文核心发现的理论根基
2. **TraceCoder (ICSE 2026)** — fault localization 上 trace 信息有益的反向发现，boundary condition 讨论必需
3. **SBFL 经典工作**（Ochiai, Tarantula; Jones & Harrold, 2005）— 精简覆盖信息用于故障定位的相关范式
4. R1/R2 均指出上述引用缺失影响论文对自身 contribution 边界的定位

---

## External Review

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（2 warnings, 5 info）：

| 严重程度 | 位置 | 发现 |
|---------|------|------|
| ⚠️ Warning | p.3-4 | 连续两页纯文本（Related Work → Method §3.1–3.3），无 display item 穿插，建议插入 trace condition 对比表打破单调 |
| ⚠️ Warning | p.5 | 单页堆叠 3 个 display items（Table 1 + Figure 2 + Table 2），与 p.6 纯文本形成节奏不均 |
| ℹ️ Info | p.1 | 首页无视觉锚点，第一个 display item 在 p.2 顶部 |
| ℹ️ Info | p.5 | Figure 2 axis label/legend ~7pt，建议 ≥8pt |
| ℹ️ Info | p.5 | Table 1 脚注 ~6pt，打印时可能难以辨认 |
| ℹ️ Info | p.18 | Figure 6 热力图使用红-绿色阶，对色盲不友好，建议 viridis/Blue-Orange |
| ℹ️ Info | p.21 | 末页内容填充 ~60% |

---

## Overall Assessment

**综合评分：3.0 / 5（Findings）**

| Reviewer | 评分 | 侧重 |
|----------|------|------|
| R1 | 3.5 (Borderline Conference) | 方法论严谨性、消融设计质量 |
| R2 | 3.0 (Findings) | 概念新颖性、结构性贡献 |
| **Director** | **3.0 (Findings)** | 加权综合 |

**评分逻辑：**

R1 与 R2 的 0.5 分分歧源于评估框架差异：R1 侧重方法论可修复性（梯度掩码、单 seed 可通过补充实验解决，修复后可达 Conference），R2 侧重结构性 novelty（tautology + trivially solvable task 无法通过修订解决）。

Director 倾向 R2 的判断：

1. **Tautology 问题是结构性的**：exception 存在 ≈ failure 的定义性标志，regex baseline 93.61%，exception.type.only 100%。即使 reframe 为 "degradation study"，在 trivially solvable task 上的退化发现 generalizability 存疑。

2. **Full-trace 退化的 novelty 有限**：向固定信号中添加大量噪声降低分类性能是 well-established 的 ML 直觉。本文的贡献在于将这一直觉在 code SFT 场景中实证化和量化——有价值，但更适合 Findings。

3. **消融设计质量支撑 Findings 收录**：7 条件系统消融 + 多模型验证 + phase transition + 训练动态分析，实验工作量和设计质量 above average，empirical contribution 扎实。

4. **4 个 Must-Fix 问题未解决**：梯度掩码 confound（W2）、单 seed（W3）、claims 过度泛化（W4）、tautology framing（W1）均需实质性修订。

**提升路径**：如果作者 (a) 坦诚讨论 exception=verdict 的 tautological 关系、(b) 将 "mechanistic explanation" 弱化为 "diagnostic decomposition"、(c) 限定标题和 claims 范围、(d) 补充关键条件的多 seed 结果、(e) 执行错配训练-推理实验解决梯度掩码 confound，论文可望提升至 3.5（Borderline Conference）。但 novelty ceiling（由任务构造决定）限制了进一步提升空间。

---

## Detailed Comments

### Reviewer 分歧总结

| 议题 | R1 | R2 | Director 裁定 |
|------|----|----|--------------|
| Tautology 严重程度 | Should-Fix | Must-Fix | Must-Fix |
| Task value | Should-Fix | Must-Fix | Should-Fix |
| Gradient masking confound | Must-Fix | Should-Fix→Must-Fix | Must-Fix |
| Data generation bias | Should-Fix | 部分反驳 | Should-Fix |
| 消融设计贡献权重 | 高 | 中 | 中偏高 |
| Overall | 3.5 | 3.0 | 3.0 |

### 对作者的核心修订建议（按优先级）

1. **重写 Framing**（对应 W1/W4）：承认 exception=verdict 的 tautological 关系，将核心贡献重新定位为 "information overload degradation mechanism in code SFT" 而非 "exception-only is the optimal trace representation"。标题加限定词。
2. **补充关键实验**（对应 W2/W3）：(a) 错配训练-推理实验解决梯度掩码 confound；(b) 关键条件 3-seed 重复。
3. **限定 Claims**（对应 W4）：删除或弱化 "mechanistic explanation" 和 "input curation > model scaling"。
4. **补充 Related Work**（对应 W6）：Information Bottleneck 理论、SBFL 精简信息理念、TraceCoder boundary condition 对比。
5. **讨论 Generalizability 边界**（对应 W5/W8）：verdict prediction vs. fault localization/program repair 的 trace utility 差异。