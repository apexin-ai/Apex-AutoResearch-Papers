---
round: 5
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T15:47:41.526638+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 5 (Fresh Review)

**论文**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models
**Venue**: EMNLP 2026 via ARR May 2026
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作）
**轮次**: Round 1 独立审稿 → 交叉回应 → 收敛（1 轮即达成共识）

---

## Summary

本文在 DeepSeek-R1-Distill-Qwen-7B (20% structured sparsity) 上对比四种结构化剪枝准则（CKA-only、Random、Standard、RASP）经 SFT warmup → GRPO 两阶段恢复后的训练动态差异。核心发现：CKA-only（仅移除功能冗余结构）在 GRPO reward 空间实现 active learning（peak 0.354, 4.4× Standard），而基于梯度重要性的方法（Standard, RASP）训练坍塌。作者将此归因于剪枝时保留的表征多样性（CKA heatmap）。同时报告了 reward-accuracy decoupling 现象。

---

## Strengths

**S1. 研究问题新颖且时机恰当**（R1、R2 共识）。"剪枝准则是否影响下游 RL 恢复能力"此前未被系统研究。现有工作关注恢复策略本身（Self-Healing, PASER, PAT），本文首次将剪枝决策与 RLVR 训练动态直接关联。

**S2. 控制变量设计严谨**（R1、R2 共识）。四种准则共享同一结构分析、同一稀疏度、同一 per-layer capacity floor、同一 SFT/GRPO 配置，仅在评分公式上不同。Internal validity 高。

**S3. 多维训练动态诊断**（R1、R2 共识）。Reward trajectory + $f_0$（零方差 batch 比例）+ gradient norm + KL divergence 四维诊断，比同类工作更完整。CKA-only 的 recovery event（step 90）和 Standard 的梯度坍塌模式有说服力。

**S4. Reward-accuracy decoupling 是有价值的独立发现**（R1 S4, R2 共识）。Table 2 + 四个 benchmark 一致显示 GRPO reward 增长不直接转化为精度提升，对 pruned-model-recovery 领域有警示意义。

**S5. 相关工作覆盖全面**（R2 S5）。结构化剪枝、推理特定剪枝、功能相似性剪枝、剪枝后恢复、RLVR 训练动态五个方向均有覆盖。

**S6. CKA 可靠性论证到位**（R2 S4）。intra-layer CKA 避免了已知的跨维度敏感性问题，Spearman ρ ≥ 0.964 验证了排名稳定性。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [critical, 共识] Reward-accuracy decoupling 严重削弱核心贡献的实际意义。**
- Table 2: CKA-only GRPO Δ=+0.48pp, Standard Δ=+0.55pp——**Standard 的 GRPO 精度增益反而略高于 CKA-only**。
- CKA-only vs Standard 最终精度差距 4.55pp 中，4.62pp 来自 SFT 阶段（63.91% vs 59.29%），GRPO 净贡献为 −0.07pp。
- 论文核心叙事围绕 GRPO recovery capacity，但精度层面的主要贡献实际发生在 SFT，非 GRPO。
- 15% sparsity 下 GRPO 确实使差距从 5.69pp 扩大至 7.20pp（Appendix L Table 12），这是 GRPO 产生差异化影响的最强证据，但被放在 Appendix 而非正文。
- **核心挑战**：如果 reward 不预测精度，为什么 reward trajectory 是"合适的诊断指标"？论文需要更强的论证来回答这一问题。

**N2 [critical, 共识] Cross-architecture (Qwen2.5-Math-7B) 缺乏 GRPO 验证。**
- Table 13 仅有 SFT 恢复结果（CKA-only 1.0%→51.50% vs Standard 18.5%→21.00%），GRPO 被推迟到 future work。
- 论文核心 claim 关于 GRPO recovery capacity，跨架构验证仅覆盖 SFT 不构成有效支撑。
- 核心发现的 generalizability 受限于 DeepSeek-R1-Distill-Qwen family（7B + 1.5B）。

### Should-Fix（影响评分但不一票否决）

**W1 [warning, 共识] RASP/Random 种子不对称。**
- CKA-only 和 Standard 有 3 seeds，RASP 和 Random 仅 1 seed。排序中 2/4 位置无统计支撑。
- R2 论证 CKA-only vs Standard（最关键比较）已有充分验证（p=0.0009），Random/RASP 排序不确定不影响核心 insight。Director 同意此评估，但 Random 作为 uninformed baseline，其方差直接影响排序可信度，应优先补充。

**W2 [warning, 共识] CKA-recovery 因果机制仅为相关性证据。**
- Figure 4 的 CKA heatmap（CKA-only μ=0.62 vs Standard μ=0.90）展示了相关性，但无干预实验证明因果关系。
- 低 dense fidelity 也可解读为"模型被扰动最大"而非"保留了更多多样性"。

**W3 [warning, R1 提出, R2 AGREE] Per-layer capacity floor (40%) 未消融。**
- 40% floor 与不同评分准则的交互可能产生混淆效应。RASP 的 collapse 可能部分源于 floor 与其复合评分的特定交互。

**W4 [warning, 共识] α 消融缺 GRPO reward 数据。**
- Table 6 测试了 6 个 α 值但仅报告 post-prune accuracy (N=100)。α=4.0 时精度最高（40%）暗示 RASP collapse 可能由 α=1.0 超参数驱动而非机制缺陷。应补充关键 α 值的 GRPO reward。

**W5 [warning, R2 提出, R1 AGREE] "Recovery capacity gradient" 术语与 gradient descent 语境混淆。**
- 论文同时高频使用 "gradient" 指代 ML 梯度和方法排序，增加阅读负担。建议改为 "spectrum" 或 "ordering"。

### Minor

**M1.** Section 5 末尾约 2 行溢出至第 9 页——可能触及 8 页 hard limit（R2-m4）。
**M2.** Abstract p<0.001 未说明统计检验方法；N=3 t-test 报告 p<0.001 需要极大效应量（R2-m5）。
**M3.** Page 7 display items 过度拥挤（Figure 3 + Figure 4 + Table 2 挤在同一页），Figure 3/4 内部文字可能低于 8pt 可读阈值（R2-m3 + 视觉审查）。
**M4.** bib key 年份误导（lachance2024cka 实为 2022, klabunde 实为 2023）；selfhealing2025 venue 字段为空；6 篇 OpenAlex not_found（R1-M4, R2-m1/m2）。
**M5.** Figure 3 两子图 y 轴刻度差异大，视觉上容易误导（R1-M2）。
**M6.** RASP checkpoint 未保存，部分数据不可回溯验证（R1-M1）。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致（[AGREE]）：

1. **Reward-accuracy decoupling 是论文面临的最核心挑战**——CKA-only 在 reward 空间领先 4.4×，但精度层面的优势完全来自 SFT 而非 GRPO。
2. **Cross-architecture 缺 GRPO 验证**——Qwen2.5-Math-7B 仅有 SFT 结果，无法支撑 GRPO recovery capacity 的泛化 claim。
3. **CKA-recovery 机制为相关性证据**——需要干预实验或更强的因果论证。
4. **CKA-only vs Standard 的核心排序有充分统计支撑**（3-seed, p=0.0009）——这一核心比较是稳健的。
5. **研究问题新颖、控制变量设计严谨**——论文的实验框架本身是高质量的。

## Reviewer Divergence

| 问题 | R1 | R2 | Director 判定 |
|------|----|----|--------------|
| **GRPO 训练步数（100/300步）** | N2 critical: 300步不足以证明 structural gap | REBUT: Figure 5 $f_0>0.5$ 全程，Standard 已收敛到坍塌状态 | **R2 胜**——$f_0$ 收敛证据有力，Standard 不是"还没学够"而是"结构性缺乏梯度信号"。降为 info。 |
| **单一稀疏度** | N3 critical: 仅 20% 运行完整 pipeline | REBUT: Appendix L Table 12 有 15%/20%/25% 完整 SFT→GRPO 结果 | **R2 胜**——R1 遗漏了 Appendix L。事实修正成立。降为 info（但正文展示应更显著）。 |
| **种子不对称严重性** | N1 critical | W1 should-fix（核心比较已有 3-seed） | **折中**——列为 warning。核心 insight 不受影响，但排序完整性受损。 |
| **Figure 1 质量** | S5 正面 | W4 信息密度低 | **小分歧**——排版问题而非设计问题，列为 info。 |

---

## Questions（需要作者澄清）

1. **[高优先级]** Table 2 显示 Standard GRPO Δ (+0.55pp) 高于 CKA-only (+0.48pp)。如何调和这一观察与 "CKA-only achieves active learning while Standard collapses" 的核心叙事？是否应区分 reward-level recovery 和 accuracy-level recovery？

2. **[高优先级]** 15% sparsity 结果（Appendix L: GRPO 使差距从 5.69pp 扩大至 7.20pp）比 20% 更能支撑论文叙事。为什么选 20% 而非 15% 作为主要报告点？

3. **[中优先级]** Table 6 α=4.0 post-prune accuracy 最高（40%），但 Table 1 RASP (α=1.0) 全面坍塌。α=4.0 时 GRPO 行为如何？如果 GRPO 也改善，则 RASP collapse 可能仅是超参数问题。

4. **[中优先级]** CKA-only 与 Standard 保留的结构重叠度是多少？如果重叠度 >80%，说明少量不同结构决定了训练动态——这对因果机制的理解至关重要。

5. **[中优先级]** Unpruned 模型 GRPO reward 从 0 升至 0.669 但精度不变 (81.27%)。这是否意味着 reward-accuracy decoupling 是 GRPO + GSM8K binary reward 的系统性现象，而非与剪枝相关？如果是，用 GRPO reward 作为 recovery capacity 诊断指标是否恰当？

6. **[低优先级]** 40% per-layer capacity floor 如何选定？不同 floor 值下排序是否稳健？

---

## Missing References

未发现严重遗漏。以下可考虑补充但非必须：
- **SparseGPT** (Frantar & Alistarh, 2023): LLM 非结构化剪枝的开创性工作，related work 提及 Wanda 时可一并引用。
- **LoRAShear** (Chen et al., 2023): 结合 LoRA 的结构化剪枝与知识恢复。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置，不适用。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical / 5 warning / 8 info）。主要发现：

1. **[warning] Page 3-5 连续 3 页无 figure/table**。建议将 page 7 的 figure 前移平衡视觉节奏。
2. **[warning] Page 7 display items 过度拥挤**：Figure 3 + Figure 4 + Table 2 挤在同一页，Figure 3/4 内部文字可能低于 8pt 可读阈值。
3. **[warning] Figure 4 CKA 热力图面积过小**，颜色渐变细节在当前尺寸下难以分辨。
4. **[warning] Appendix 末页仅占 ~35% 页面**，~65% 空白。
5. **[info] Figure 2 RASP 红线与 Standard 橙线颜色区分度不足**，建议添加 line style 辅助区分。
6. **[info] Page 1 无视觉锚点**（首页无核心结果预览图）。

---

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 2.5/5 | 3.5/5 | 3.0/5 |
| Excitement | 3.5/5 | 3.0/5 | 3.25/5 |
| Reproducibility | 3.5/5 | 4.0/5 | 3.75/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**Overall Score: 3.0 (Findings)**

**Confidence: 4/5**

**评分理由**：

研究问题新颖（剪枝准则→RLVR 恢复能力，此前无系统研究），控制变量实验设计严谨，训练动态分析多维度且有说服力。CKA-only vs Standard 在 reward 空间的差异（4.4× peak reward, 3-seed p=0.0009）是统计上稳健的结果。

但论文面临两个结构性挑战：(1) **Reward-accuracy decoupling** 严重削弱核心指标的实际诊断价值——20% sparsity 下 CKA-only 与 Standard 的精度差距 4.55pp 几乎完全来自 SFT 而非 GRPO，论文核心叙事围绕 GRPO recovery 但精度层面的主要贡献在 SFT；(2) **Cross-architecture GRPO 缺失** 使泛化 claim 受限于 DeepSeek-R1 family。

R1 初始给分 2.5 (Borderline Findings)，但其两个 critical 问题（训练步数不足 N2、单一稀疏度 N3）被 R2 以事实证据成功反驳（$f_0$ 收敛证据、Appendix L 多稀疏度数据），应适度上调。R2 给分 3.0 (Findings)。综合交叉回应后的收敛结果，**3.0 (Findings)** 是恰当的定位——论文的控制变量设计和训练动态分析达到了 Findings 水准，但 reward-accuracy decoupling 未充分论证 + cross-architecture GRPO 缺失使其难以达到 Conference (4.0) 水平。

---

## Detailed Comments（逐节）

### Abstract
- "consistently and significantly underperforms" 中 p<0.001 未标明检验方法（t-test? bootstrap?）。N=3 seeds 的 t-test 报告 p<0.001 需要极大效应量——数值上合理（4.55pp gap, 0.19/0.38 std），但应明确检验类型。
- Abstract 正确区分了 GRPO (DeepSeek) vs SFT (Qwen-Math) 的验证范围。

### Introduction
- Figure 1 字号偏小但框架设计有效。
- "recovery capacity is shaped at pruning time, not during subsequent fine-tuning" 与 Table 2 的 SFT 主导精度差距存在张力——SFT 也是 "subsequent fine-tuning"。

### Method
- 控制变量框架设计清晰（Algorithm 1），四种评分公式的数学定义明确。
- CKA 可靠性论证充分。
- SFT warmup 的功能性必要性论证合理（EOS collapse → GRPO 不可行）。

### Experiments
- Table 1 和 Figure 2 的核心结果在 reward 层面有说服力。
- Table 2 的 reward-accuracy decoupling 是重要发现，但论文未充分讨论其对 recovery capacity 概念本身的影响。
- 15% sparsity 结果（GRPO 扩大差距 +1.51pp）应从 Appendix 提升至正文——这是 GRPO 确实产生差异化影响的最强证据。
- Cross-scale (1.5B, Table 3) 保留了三方法排序，但仅 100 步单 seed，信息量有限。

### Extended Analysis
- CKA heatmap (Figure 4) 的相关性证据有启发性但不构成因果证明。
- Qwen2.5-Math-7B 的 post-prune accuracy reversal（1.0%→51.50%）是 SFT recovery 层面的强证据，但不直接支撑 GRPO claim。

### Limitations
- 覆盖了架构敏感性、benchmark 范围、硬件配置、种子多样性四个方面，长度适当。
- 建议补充：(a) reward-accuracy decoupling 对 recovery capacity 概念的局限性；(b) per-layer capacity floor 未消融。

### Format
- 正文接近但可能触及 8 页 hard limit（Section 5 末尾约 2 行溢出 p9），需压缩。
- 匿名性合规（\usepackage[review]{acl}, author=Anonymous）。
- Page 7 display items 过度拥挤，Pages 3-5 纯文本——视觉节奏不均。
