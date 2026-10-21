---
round: 20
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-25T05:48:48.075674+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 22 审稿报告（Fresh Review）

**Venue**: EMNLP 2026 (ARR)  
**论文标题**: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction: Symbolic Confirmation Bias in LLM Self-Verification  
**审稿模式**: Fresh（重新审稿，无上轮记忆）  
**Reviewer**: R1, R2  
**交叉讨论轮次**: 1 轮（已收敛）

---

## Summary

本文研究 LLM 自提取约束（SICA）是否能超越多数投票（SC）改进推理准确率。通过 6 个模型（7B-32B）、4 个 benchmark、27 种 training-free 策略的系统实验，论文得出否定结论并提出 Symbolic Confirmation Bias（SCB）作为根因解释。核心论证链为：Observation 1（source-attribution scoring）→ Bias Ratio 量化 → 27 策略穷举失败 → 诊断框架（C₀/K_eff/BR）→ Cross-architecture escape 作为初步解决方向。

论文的核心贡献在于将一个常见的 negative empirical observation 系统化为可诊断、可解释的框架，并给出了明确的 escape condition。

---

## Strengths

**S1. 系统性 negative result 论证（双方一致）**  
不同于简单报告"方法不 work"，论文构建了完整的 evidence chain：Observation 1 条件 → BR 量化偏差 → permutation test 验证 → 27 策略穷举排除 → 诊断框架 → escape condition。这是负面结果论文的典范式写作。

**S2. 统计方法论规范（双方一致）**  
TOST 等价检验、BH FDR 校正、Bootstrap CI、permutation test 的组合使用展示了对 null-result claim 的严谨态度。尽管 TOST margin 存在问题（见 N1），方法论工具箱本身值得肯定。

**S3. 实用诊断框架（双方一致）**  
C₀、K_eff、BR 三指标 + §5.3 的零成本诊断规则具有直接的 practitioner 价值。从业者可以从采样 traces 计算这些指标而无需运行完整 pipeline，判断 self-verification 是否值得尝试。

**S4. Cross-architecture escape 的建设性方向（双方一致，权重有分歧）**  
§6 将论文从纯负面结果转为建设性贡献——给出"什么条件下才能 work"的初步答案。R1 认为这是论文建设性贡献的核心；R2 认为其初步性质（n=6, mixed significance）下应缩减正文占比。

**S5. 写作清晰度与诚实限定（双方一致）**  
标题限定 "under Zero-Shot Extraction"；Limitations 坦承 frontier model 完整实验未覆盖；§6 使用 "preliminary evidence" 限定。核心 argument 在 8 页内完整呈现。

---

## Weaknesses

### Must-Fix

**N1. 标题 "Reduce to" 与 TOST 统计证据严重不匹配 [R1-N2 + R2-N1, 完全一致]**

论文标题声称 self-extracted constraints "reduce to majority voting"，但 TOST 等价检验仅 4/11 条件通过（±2pp margin）。Sensitivity analysis（Appendix U, p.23）暴露了关键问题：±1pp → 0 条件通过；±2pp → 4 条件通过；±3pp → 全部通过。这是经典的 post-hoc margin selection——搜索"恰好能通过的 margin" 在概念上等价于 p-hacking。

更严重的是，7/11 underpowered 条件的分布非随机：MDE 较高（4.6-4.8pp）的条件恰恰是较大 dataset 上的较弱模型，系统性覆盖了论文最想证明 equivalence 的场景。Qwen3-14B FOLIO Δ=+0.92±1.14pp 暗示可能存在小正效应，当前 power 无法排除。

**必须修改**：(1) ±2pp margin 需先验论证（从 SC seed-to-seed variance 或领域共识出发）而非 post-hoc sensitivity analysis；(2) 标题软化——R2 建议 "Self-Extracted Constraints Fail to Improve LLM Reasoning"，R1 建议限定为 "未在测试条件下检测到显著改进"；(3) Abstract 明确报告 4/11 TOST 通过率和 confirmatory/underpowered 区分。

**N2. Causal DAG M→T→A→C 形式化不成立，DPI bound 适用性被高估 [R1-N1 + R2 AGREE]**

论文 Figure 3 和 §5.1 将 Model→Trace→Answer→Constraint 建模为 Markov chain，据此声称 DPI bound I(C;Y) ≤ I(A;Y)。R1 精确指出：C 从完整 trace T 提取（而非仅从 A），正确因果图应为 T→(A,C) 共同子代。DPI bound 需要 C⊥T|A（给定 answer，constraint 不携带额外 trace 信息），此条件未被形式化证明也未被经验验证。

R2 补充缓解因素：论文 p.7 已写 "is not a formal consequence of the DPI bound"，核心论证实际依赖 Observation 1 的经验条件而非 DPI。但 Figure 3 的视觉呈现（带框公式直接标注在 DAG 上）与正文 hedge 不一致，制造了虚假的理论严谨性印象。

**必须修改**：(1) 修正 DAG 为 T→(A,C) 并标注经验性条件；(2) 将 DPI 从 "bound" 降级为 "motivating analogy"；(3) 降低 Figure 3 中 DPI 公式的视觉权重；(4) 补充 I(C;T|A) 的部分经验验证（控制 answer 后 constraint 的条件互信息）。

**N3. SCB 与 CoT Confirmation Bias 的 novelty 分离不足 [R2-N2 + R1 AGREE，实验设计分歧]**

论文定义的 Symbolic Confirmation Bias 与已知的 CoT confirmation bias（Turpin et al., 2023; Wan et al., 2025）在经验上难以分离。约束从 trace 中提取——如果 trace 本身已因 CoT confirmation bias 而 biased，约束自然继承该 bias，不需要 SCB 作为独立现象来解释。§5.1 的 per-trace 分析 "Self-extracted constraints systematically align with the model's majority answer" 恰恰与 CoT confirmation bias 的下游预测一致。

R1 提出更精确的分离实验设计：固定 trace 内容，替换约束提取模型（用模型 A 的 traces 喂给模型 B）。如果模型 B 提取的约束仍 align with 模型 A 的 majority answer → CoT bias 主导；如果 align with 模型 B 的 prior → SCB 独立存在。Table 17（p.20）的 cross-model extraction 部分触及此方向但未从分离角度分析。

**必须修改**：(1) 在 §5.1 增加 cross-model extraction 的 SCB vs CoT bias 分离分析（现有数据即可完成）；(2) 明确 SCB 是否可约化为 CoT confirmation bias 的 constraint-extraction 投影，并讨论两种可能的理论含义；(3) 如果无法分离，应在 framing 中承认 SCB 可能是 CoT bias 的重新包装而非独立现象。

---

### Should-Fix

**W1. §5 信息密度过高 vs §6 空间分配 [R2-W1, R1 REBUT]**

R2 认为 §5（~2.5 页覆盖 SCB + DPI + 27 策略 + 诊断框架）相对于 §6（~1 页 preliminary cross-architecture escape）被过度压缩，建议将 §6 大幅移至 appendix。R1 反驳：§6 是论文从纯负面结果转为建设性贡献的关键，移除将损害叙事完整性。

**Director 判断**：R1 论点更有说服力——保留 §6 在正文。解决方案应是将 §5.1 的部分 permutation test 细节移至 appendix 为 §5 核心论证腾出空间，而非缩减 §6。

**W2. Few-shot extraction 未测试 [R2-W2 + R1 AGREE]**

27 种策略全部是 zero-shot template extraction。Few-shot 示例（人工设计的约束模板）属于 training-free 但可能打破 source-attribution 自循环——示例中的约束格式/内容可能与模型 default 提取模式不同。标题限定 "zero-shot" 部分缓解，但 §5.2 声称 "training-free 策略全部失败" 需排除或讨论 few-shot。

**建议**：Limitations 中明确讨论 few-shot extraction 作为未测试的 training-free 策略。

**W3. Related Work 对 PRM/learned verification 讨论不足 [R2-W3 + R1 AGREE]**

PRM（Lightman et al.）和 ORM（Cobbe et al.）是 self-verification 的 learned counterpart。§7 提及 "trained external verifiers" 但未在 §2 系统讨论。读者难以定位本文在 verification 方法 spectrum 中的位置。特别是未将 learned verification 与 cross-architecture escape 建立联系——后者本质上是用 NLI 模型作为轻量级 learned verifier。

**建议**：§2 增加 "Learned Verification" 子节（2-3 句），对比 training-free self-extraction vs learned PRM/ORM 的 trade-off。补引 Math-Shepherd (Wang et al., 2024)、GRACE (Khalifa et al., 2023)。

**W4. ProcessSim 阈值对表示方法高度敏感 [R2-W4 + R1 AGREE]**

§5.3 使用 ProcessSim > 0.6 作为 SCB 预测阈值（TF-IDF 表示）。Appendix R 显示替换为 SBERT 后 ProcessSim 从 0.74 升至 0.91——绝对值变化巨大。0.6 只在 TF-IDF 下有意义。

**建议**：明确标注 0.6 为 TF-IDF-specific；讨论 representation-invariant 替代方案（如 percentile-based 阈值）。

**W5. 27 种策略的独立性未论证 [R1-W4 + R2 AGREE]**

Contrastive prompting vs Contrastive Scoring（同一思路的 prompt/scoring 变体）、Multi-temperature vs Probabilistic perturbation（都是注入随机性）等本质上共享核心机制。真正独立方向约 5-6 种。"27" 的修辞效果被夸大。

**建议**：Figure 5 或 Appendix K 增加策略间 taxonomy/overlap matrix，报告按独立方向计数的数字。

**W6. n=6 Spearman ρ=1.0 统计可靠性 [R1-W2, R2 partial REBUT]**

§6 的 capability-gap pattern 基于 n=6 数据点。R1 要求 leave-one-out stability；R2 认为 §6 已定位为 "preliminary evidence"，批评权重应降低。

**Director 判断**：论文措辞已较谨慎（"preliminary evidence"）。但 Abstract 和 Intro 中对 Contribution 3 的表述仍应更明确标注 exploratory 性质。不要求额外实验，但要求 framing 限定。

**W7. 3-4 seeds 对 null-result 偏弱 [R1-W3 + R2 conditional AGREE]**

Mistral-7B FOLIO 的 cross-seed 变异 Δ 从 -1.47pp 到 +3.43pp（std=2.70pp）。3-4 seeds 不足以精确估计效应大小。R2 补充缓解因素：SCB 结构性证据（BR > 1 across all seeds）部分补偿。

**建议**：维持 Limitations 中已有的 seed 数量讨论，但建议在 Table 1 注脚标注 per-condition seed 数量。

**W8. Observation 1 条件 (iii) CV=0.267 gap [R1-W1 + R2 AGREE]**

"Approximately uniform constraint yield" 依赖 CV=0.267（全局中位数），但缺少 per-problem CV 分布和 high-CV 条件下 argmax preservation 失效的 boundary analysis。

**建议**：Appendix 补充 per-problem CV 直方图和分层分析（CV > 0.3 时 SICA 行为是否显著偏离）。

---

## Questions

1. ±2pp margin 是在何种先验知识基础上确定的？是否存在与 SC seed-to-seed variance 相关的推导？
2. Permutation test 的 null model 是 within-problem（打乱同一问题内 trace-constraint 对应关系）还是 across-problem（打乱问题归属）？
3. Table 40 诊断阈值（ProcessSim > 0.6）是否有 held-out 验证？抑或在同一数据上拟合并评估？
4. Cross-model extraction（Table 17）中，frontier 模型提取的约束是否仍 align with 原始模型的 majority answer？若是，则 SCB 可能完全约化为 CoT bias。
5. Few-shot extraction（使用人工设计约束模板作为 in-context 示例）是否在 roadmap 上？这可能是打破 source-attribution 自循环的最低成本方案。

---

## Missing References

- **Poesia et al. (2023/2024)** — LLM + formal verification 的 self-correction 能力，与 SICA 的 MAX-SAT verification 直接相关
- **Stechly et al. (2024)** — LLM planning verification 的局限性，与 self-verification failure 主题契合
- **Math-Shepherd (Wang et al., 2024)** — Process reward model，作为 learned verification 的代表与 training-free extraction 形成对比
- **GRACE (Khalifa et al., 2023)** — Learned verification 方法

---

## External Review

**状态**: 未请求

---

## Visual Layout Check（非评分项）

**状态**: Agent 执行错误（rate limit）。基于上轮视觉审查的遗留 findings：

- **[CRITICAL]** Page 30 几乎全空（95% 空白）——末页仅顶部 2 行文字。建议上移内容至 page 29
- **[WARNING]** Page 8 视觉密度过高——Figure 3 + Table 2 + Figure 4 + Discussion/Conclusion/Limitations 挤在单页，与 pages 6-7 纯文本形成强烈反差
- **[WARNING]** Pages 6-7 连续纯文本无 display item——建议将 Figure 3 前移以改善阅读节奏
- **[WARNING]** Pages 1-2 前两页无任何 display item（Figure 1 在 page 3）

---

## Overall Assessment

**Score: 3.5 (Borderline Conference)**

**R1 评分**: 3.5  
**R2 评分**: 3.5  
**Director 综合**: 3.5

**评分理由**:

论文的核心价值在于将一个重要的 negative empirical observation 系统化为可诊断框架——这对 LLM self-verification 领域有实质贡献。方法论工具箱规范，实验覆盖面广，诊断框架具有实践价值。

但三个 must-fix 问题共同削弱了论文的核心主张：(1) 标题 "Reduce to" 的 claim 强度超出统计证据；(2) 理论框架（DPI/Markov chain）存在技术缺陷；(3) 核心概念 SCB 的独立新颖性未与 CoT confirmation bias 充分分离。

如果 N1 得到修正（标题软化 + margin 论证）且 N3 得到部分解决（cross-model extraction 分离分析），论文有潜力达到 4.0（Conference）。N2 的修正相对容易（降级 DPI 的 claim 强度即可）。当前状态下，核心主张的过度声明使论文处于 Borderline Conference / strong Findings 区间。

---

## Detailed Comments

### Reviewer 间共识总结

| 议题 | R1 | R2 | 共识 |
|------|----|----|------|
| 标题/TOST overclaim | N2 (must-fix) | N1 (must-fix) | **完全一致** |
| DPI Markov chain 形式化 | N1 (must-fix) | AGREE | **技术共识** |
| SCB vs CoT bias 分离 | AGREE | N2 (must-fix) | **方向一致，设计分歧** |
| §6 空间分配 | REBUT（保留） | W1（缩减） | **未解决分歧** |
| Few-shot 遗漏 | AGREE | W2 | 共识 |
| PRM/learned verification | AGREE | W3 | 共识 |
| 27 策略独立性 | W4 | AGREE | 共识 |
| Frontier model 覆盖 | W5 | partial REBUT | R2 以事实纠正 R1 |

### 未解决分歧记录

1. **§6 空间分配**：R1 认为 §6 是论文建设性贡献核心不可缩减；R2 认为 §5 被过度压缩应从 §6 腾空间。Director 采纳 R1 立场（保留 §6，从 §5.1 细节处腾空间）。

2. **Frontier model 覆盖**：R1 称"未覆盖 frontier models"；R2 以 Table 16、§3.2 数据纠正——frontier models 参与了 cross-extraction 的 bias ratio 分析，但确实未运行完整 SICA vs SC accuracy 对比。R2 的事实纠正成立。

3. **n=6 批评权重**：R1 作为 should-fix 要求更多实验；R2 认为已用 "preliminary evidence" 限定，权重应降低。Director 采纳中间立场——不要求更多实验但要求 framing 更明确。

### 与上轮对比（Director 备注）

本轮 fresh review 独立识别了与历史 issue tracker 一致的核心问题：
- R10-W4/R11-N3（TOST margin）→ 本轮升级为 Must-Fix
- R10-W7/R21-N2（SCB vs CoT 分离）→ 仍为 Must-Fix，action done 但效果不足
- R20-W1（DPI bound）→ 本轮以更精确的 DAG 技术批评重新出现

已有效解决的上轮问题（本轮未重新提出）：
- R21-N1（'structural property' → 'empirical regularity'）✓
- R21-N3（'Self-Extraction Bound' 命名移除）✓
- R21-VL1（Discussion 溢出 page 9）✓