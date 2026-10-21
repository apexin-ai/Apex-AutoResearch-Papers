---
round: 15
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-20T15:41:47.508867+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 16 (Fresh Review)

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**审稿模式**: 重新审稿 (fresh)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+Related Work）

---

## Summary

本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器。轻量级 predictor（75.9M 参数，<1% base model）通过 Gumbel-Sigmoid 松弛和 adaptive penalty controller 实现端到端训练。在 LLaMA-3.1-8B 上 30% 稀疏度下 PPL 相对 TEAL 降低 14.5%（matched sparsity），commonsense reasoning 4/4 任务胜出，但 knowledge-intensive 任务退化（MMLU -5.2pp）。Target-swap ablation 表明 KL 发现的 mask targets（与 magnitude 46-68% 不同）是质量驱动因素。跨架构验证（Mistral-7B 3-seed, Qwen-14B preliminary）显示 PPL 优势泛化但下游结果 task/scale-dependent。论文自述为 "primarily empirical study"。

---

## Strengths

**S1. C1 Target-Swap Ablation 设计精妙 [R1, R2 共识]**
§4.4 的目标-交换消融有效解耦了 mask quality 和 gradient coupling 的贡献——BCE 在 KL-derived targets 上重现 KL 质量（max Δ≤0.79pp at 50%），确认 mask targets 而非 coupling 机制本身驱动 inference-stage 质量。此实验设计在 activation sparsity 文献中未见先例。

**S2. 诚实报告负面结果 [R1, R2 共识]**
MMLU/GSM8K 退化（30%）、Mistral GSM8K 反转、Qwen-14B 推理崩溃（-20pp）、50% 下游全面崩溃均被明确报告。Limitations 部分全面且自我批评。

**S3. 受控实验设计**
MSE baseline（Appendix G）保持架构/数据/优化器完全一致仅变 loss function；BCE extended training（2700 steps）控制 compute budget；敏感性分析覆盖 bottleneck/温度/训练步数（均 <3% PPL 变化）。

**S4. 训练效率高**
1000 步、~45 min、单 GPU (RTX PRO 6000)，75.9M 参数（<1% base）。实用门槛低。

**S5. 丰富的附录支撑**
10 页附录覆盖 inference latency、bottleneck sensitivity、温度调度、训练收敛、penalty dynamics、OOD 评估、per-layer retention、mask 可视化、cross-architecture 详细结果。

**S6. 数据一致性和格式合规通过核查 [R1 验证]**
表格间数字全部匹配；Abstract 数字验证通过；引用 47 条无虚假引用；正文 8 页合规；double-blind 合规。

---

## Weaknesses

### Critical（影响接收决定）

**C1. 多种子覆盖不一致，存在选择性报告风险 [R1-N1, R2 AGREE]**
Table 2 headline result（50% KL global PPL 11.79）为 single-seed (s42)，而次优结果（50% KL uniform 11.92±0.07）为 3-seed。MSE baseline（支撑核心 "coupling alignment" 论点）全部 single-seed。当最优结果为 single-seed 时，读者无法判断其是否在 multi-seed 分布的幸运端。

**C2. 消融实验仅在 50% 稀疏度，实际可用的 30% regime 缺失 [R1-N3, R2 AGREE]**
Table 4 所有消融（Forward KL/JSD/Reverse KL/STE/BCE variants）均在 50%。但论文自身承认 50% downstream 崩溃至随机水平（"capacity-limited regime"），30% 才是可用稀疏度。在 30% 下 loss function 选择效果未知——如果 forward KL 相对 JSD/reverse KL 的优势缩小甚至消失，论文的核心结论可能不成立。

**C3. 新颖性不足 [R2-N1 critical, R1 REBUT — 分歧]**
R2 认为：KL distillation 匹配 teacher/student 输出分布是经典范式；Gumbel-Sigmoid、adaptive Lagrangian、TEAL allocation 均为已有技术组合；与 MaskLLM 核心训练原理高度重合。R1 反驳：C1 ablation 设计新颖、mask divergence 46-68% 是新定量发现、MSE catastrophic failure 区分了 coupling 和 output-alignment。**两位 Reviewer 均同意算法新颖性有限，分歧在于 empirical insights 是否足以弥补。**

### Warning（应修复但不阻挡接收）

**W1. PPL 改善与下游任务 task-type-dependent 脱节 [R1-N2 critical → R2 降级为 warning]**
30% 稀疏度下 KL vs TEAL：commonsense 4/4 胜（ARC +4.4pp, HS +7.8pp, WG +3.9pp, PIQA +2.2pp），knowledge 0/2 败（MMLU -5.2pp, GSM8K -1.3pp）。R1 认为 critical（PPL 改善未转化为一致的下游提升），R2 指出 R1 选择性引用了负面结果。**综合判断降为 warning**：task-type split 真实存在但论文已报告；MMLU 退化成因（forward KL mode-covering hypothesis）缺实验验证。

**W2. 无实际推理加速 [R1-W5, R2-W1 AGREE]**
Appendix A 明确承认 unstructured mask 不能被现有 sparse kernel 加速，pipeline 增加 6.4% overhead。论文贡献严格限于 prediction quality，但 framing 暗示效率收益。

**W3. Forward KL 方向选择论证不足 [R1-W2, R2-M1 AGREE]**
§3.4 使用 forward KL 但未论证选择理由。标准 KD 文献（MiniLLM, DistiLLM）讨论 reverse KL 对 capacity-limited student 的优势。实验（Table 4）验证了 forward > reverse，但理论解释缺失。

**W4. 评估域同质性 [R1-W3, R2-W2 AGREE]**
WikiText-103 训练 + WikiText-2 评估（同为 Wikipedia）。C4 OOD 评估（Appendix D）显示 cross-seed CV 从 0.2% 增至 6.3%，方差放大 30×。仅一个 OOD domain。

**W5. §3.6 梯度分析 informal [R1-W4, R2 AGREE]**
分析直觉正确但缺乏：(1) ∂L_KL/∂s_j 的显式展开；(2) coupling degree 量化指标；(3) 低 SNR 产生更好 mask 的正式解释。§3.6 已标注 "suggestive"。

**W6. 缺少与已有训练型预测器的直接数值对比 [R2-N2 critical → R1 降级]**
R2 认为缺 DejaVu/ShadowLLM/FastForward 数值对比。R1 反驳：controlled ablation 已等价覆盖（BCE=DejaVu, MSE=ShadowLLM, compensation=FastForward）。**综合判断降为 warning**：R1 的论点有理，但 §4 应明确标注 baseline 与已有方法的等价关系。

**W7. Taxonomy (Table 1) 分析价值有限 [R2-W3, R1 REBUT]**
矩阵 5/6 cell 有代表方法（R1 指出），但 taxonomy 的 predictive power 未通过系统对比验证。空 cell 未讨论。降为 minor editorial issue。

---

## Reviewer Consensus [AGREE]

1. **多种子覆盖需补全**（C1）：Table 2 所有行应有 3-seed 统计；MSE 至少 2 额外种子
2. **30% regime 需消融覆盖**（C2）：Forward KL/JSD/Reverse KL/STE 在 30% 的对比
3. **无实际加速**（W2）：framing 应调整为 mask quality study
4. **Forward KL 论证不足**（W3）：需理论或更充分的经验论证
5. **评估域同质性**（W4）：Limitations 应更明确
6. **梯度分析 informal**（W5）：已有 suggestive hedge，可接受
7. **Missing references**：三篇应补充（activation sparsity opportunities, 2:4 activation sparsity, rethinking KL in KD）
8. **Griffin 引用**：关联弱，应去掉或降权

## Reviewer Divergence [REBUT]

1. **新颖性（C3）**：R2 (3.0) 认为标准 KL 应用 novelty 不足以支撑 main conference；R1 (3.5) 认为 C1 ablation + mask divergence + MSE failure 的 empirical insights 足够 borderline。核心分歧在于 EMNLP main 对 empirical-only contribution 的接收门槛。
2. **PPL-下游脱节严重性（W1）**：R1 认为 critical（MMLU/GSM8K 退化），R2 认为 warning（4/6 任务正面）。综合为 warning。
3. **已有方法对比（W6）**：R2 认为 critical（需直接数值对比），R1 认为 controlled ablation 已覆盖。综合为 warning。

---

## Questions

1. Table 4 消融是否做了多种子？BCE+STE vs KL 的 Δ=0.62 PPL 是否统计显著？（R2-Q1, R1 AGREE）
2. 为何不在 SwiGLU gate 分支做 sparsity prediction？Gate 的 sigmoid 输出天然接近二值化。（R2-Q2）
3. Adaptive penalty controller 超参数（ε=0.02, doubling rate）的敏感性分析？（R2-Q4, R1 AGREE）
4. MMLU/GSM8K 退化的 per-task mask overlap 分析？（R1-N2 延伸）
5. 30% 稀疏度下 forward vs reverse KL 的下游表现差异？（R1-N3 核心）

---

## Missing References

1. "Activation Sparsity Opportunities for Compressing General Large Language Models" (arXiv:2412.12178, Dec 2024) — SwiGLU FFN 稀疏化机会的系统研究 [R1, R2 AGREE]
2. "Accelerating Transformer Inference and Training with 2:4 Activation Sparsity" (arXiv:2503.16672, Mar 2025) — 结构化 activation sparsity，与 future work 直接相关 [R1, R2 AGREE]
3. "Rethinking KL Divergence in Knowledge Distillation for Large Language Models" (Wen et al., arXiv:2404.02657, 2024) — forward vs reverse KL 分析，与 §3.4 直接相关 [R1, R2 AGREE]

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: 已完成（耗时 ~3 min）

**Critical**:
- **正文溢出第 9 页**：Conclusion 超出 8 页正文限制，Ethics Statement 从第 9 页中部才开始。有 desk-reject 风险。
- **前 4 页无任何 display item**：Figure 1（Method Overview）直到第 6 页才出现，审稿人前 2 分钟仅看到密集文字，无视觉锚点。

**Warning**:
- 第 7 页三张表格（Table 2/3/4）集中，与前 4 页纯文本形成极端"荒漠-绿洲"反差
- Appendix 最后一页 Figure 8 仅占 40% 页面，空白过多
- 布局节奏失衡：前半段无 display item，后半段集中全部 7 个

**Info**: Figure 1 设计清晰；Table 2 booktabs 格式规范；公式渲染正确；参考文献无 [?] 残留。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

**评分理由**：

论文在受控实验设计（C1 target-swap ablation）、mask divergence 的定量发现（46-68%）、以及 MSE catastrophic failure 的实证上有价值。敏感性分析全面，负面结果报告诚实，训练成本极低。

但存在三个结构性问题阻碍 main conference 接收：
1. **消融覆盖缺口**（C2）：核心 loss function 选择消融仅在 50%（downstream 崩溃的 regime），实际可用的 30% 缺消融——这是 empirical study 的根本性 gap
2. **多种子不一致**（C1）：headline result 为 single-seed，作为 empirical study 统计严谨性不足
3. **新颖性天花板**（C3）：方法是已有技术的组合应用，贡献主要在 empirical insights 层面；两位 Reviewer 对是否足够存在分歧

如果能补充 30% 消融数据和完整 multi-seed Table 2，论文可升至 Borderline Conference (3.5)。新颖性问题是结构性的，需更深的理论贡献或更广的实验覆盖（多模型、多任务、实际加速）来弥补。

| 维度 | 分数 | 说明 |
|------|------|------|
| Soundness | 3.5/5 | 技术正确，消融设计好，但多种子覆盖和消融 regime 有 gap |
| Excitement | 2.5/5 | Empirical insights 有价值但算法无新意，无 runtime speedup |
| Reproducibility | 4.0/5 | 超参完整，单 GPU 可复现，但代码不可用 |
| Overall | 3.0/5 | Findings 水平 — empirical 发现有价值但 novelty 和实验全面性未达 main conference |

**Confidence: 4/5**

---

## Detailed Comments

### §1 Introduction
- "primarily empirical study" 声明诚实但在 EMNLP submission 中是双刃剑——明确管理了期望但也降低了 perceived contribution
- Contribution list 第 4 条（allocation-to-downstream interactions）缺 "preliminary" 标注

### §2 Related Work
- MaskLLM 三点区分（sparsity type / mask generation / allocation）是有效的，但 R2 指出核心训练原理重合度高
- 缺三篇重要引用（见 Missing References）
- Griffin speculation 无实验支撑，建议去掉

### §3 Method
- §3.6 梯度分析直觉正确但 informal（缺显式表达式和量化）
- §3.7 Taxonomy 分析框架有用但 predictive power 未充分验证
- Forward KL 选择（§3.4）需理论论证

### §4 Experiments
- Table 2：需完整 3-seed 覆盖
- Table 4：需 30% regime 消融
- C1 ablation 设计精妙但 oracle mask 来自 KL 训练的 confound 应被明确讨论
- BCE baseline 等价于 DejaVu-style predictor 应在文中显式标注
- MSE baseline single-seed 不够（尽管 1.9×/9.6× gap 使 seed sensitivity 不太可能改变结论）

### §5 Conclusion
- Task-type split（commonsense vs knowledge）应更显著地讨论，而非仅在 §4.2 一句话
- "Future work: N:M sparsity and 70B+" 暗示当前工作不完整

### Limitations
- 全面且自我批评，质量高
- 可补充 "domain homogeneity" 和 "30% 消融缺失" 的明确声明

### 格式
- ⚠️ **正文溢出第 9 页** — 需压缩使 Conclusion 在第 8 页内结束（desk-reject 风险）
- Figure 1 应前移至第 2 页以改善视觉节奏