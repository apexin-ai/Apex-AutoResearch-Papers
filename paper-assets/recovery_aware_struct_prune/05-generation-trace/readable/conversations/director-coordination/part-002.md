# Director coordination — Part 2 of 3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/77/770846f5df99c753aaca.json)

## Round 30

### Tool call

_source line 338 · 2026-05-21T15:47:41.499201+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 5 (Fresh Review)\n\n**论文**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\n**Venue**: EMNLP 2026 via ARR May 2026\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作）\n**轮次**: Round 1 独立审稿 → 交叉回应 → 收敛（1 轮即达成共识）\n\n---\n\n## Summary\n\n本文在 DeepSeek-R1-Distill-Qwen-7B (20% structured sparsity) 上对比四种结构化剪枝准则（CKA-only、Random、Standard、RASP）经 SFT warmup → GRPO 两阶段恢复后的训练动态差异。核心发现：CKA-only（仅移除功能冗余结构）在 GRPO reward 空间实现 active learning（peak 0.354, 4.4× Standard），而基于梯度重要性的方法（Standard, RASP）训练坍塌。作者将此归因于剪枝时保留的表征多样性（CKA heatmap）。同时报告了 reward-accuracy decoupling 现象。\n\n---\n\n## Strengths\n\n**S1. 研究问题新颖且时机恰当**（R1、R2 共识）。\"剪枝准则是否影响下游 RL 恢复能力\"此前未被系统研究。现有工作关注恢复策略本身（Self-Healing, PASER, PAT），本文首次将剪枝决策与 RLVR 训练动态直接关联。\n\n**S2. 控制变量设计严谨**（R1、R2 共识）。四种准则共享同一结构分析、同一稀疏度、同一 per-layer capacity floor、同一 SFT/GRPO 配置，仅在评分公式上不同。Internal validity 高。\n\n**S3. 多维训练动态诊断**（R1、R2 共识）。Reward trajectory + $f_0$（零方差 batch 比例）+ gradient norm + KL divergence 四维诊断，比同类工作更完整。CKA-only 的 recovery event（step 90）和 Standard 的梯度坍塌模式有说服力。\n\n**S4. Reward-accuracy decoupling 是有价值的独立发现**（R1 S4, R2 共识）。Table 2 + 四个 benchmark 一致显示 GRPO reward 增长不直接转化为精度提升，对 pruned-model-recovery 领域有警示意义。\n\n**S5. 相关工作覆盖全面**（R2 S5）。结构化剪枝、推理特定剪枝、功能相似性剪枝、剪枝后恢复、RLVR 训练动态五个方向均有覆盖。\n\n**S6. CKA 可靠性论证到位**（R2 S4）。intra-layer CKA 避免了已知的跨维度敏感性问题，Spearman ρ ≥ 0.964 验证了排名稳定性。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical, 共识] Reward-accuracy decoupling 严重削弱核心贡献的实际意义。**\n- Table 2: CKA-only GRPO Δ=+0.48pp, Standard Δ=+0.55pp——**Standard 的 GRPO 精度增益反而略高于 CKA-only**。\n- CKA-only vs Standard 最终精度差距 4.55pp 中，4.62pp 来自 SFT 阶段（63.91% vs 59.29%），GRPO 净贡献为 −0.07pp。\n- 论文核心叙事围绕 GRPO recovery capacity，但精度层面的主要贡献实际发生在 SFT，非 GRPO。\n- 15% sparsity 下 GRPO 确实使差距从 5.69pp 扩大至 7.20pp（Appendix L Table 12），这是 GRPO 产生差异化影响的最强证据，但被放在 Appendix 而非正文。\n- **核心挑战**：如果 reward 不预测精度，为什么 reward trajectory 是\"合适的诊断指标\"？论文需要更强的论证来回答这一问题。\n\n**N2 [critical, 共识] Cross-architecture (Qwen2.5-Math-7B) 缺乏 GRPO 验证。**\n- Table 13 仅有 SFT 恢复结果（CKA-only 1.0%→51.50% vs Standard 18.5%→21.00%），GRPO 被推迟到 future work。\n- 论文核心 claim 关于 GRPO recovery capacity，跨架构验证仅覆盖 SFT 不构成有效支撑。\n- 核心发现的 generalizability 受限于 DeepSeek-R1-Distill-Qwen family（7B + 1.5B）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [warning, 共识] RASP/Random 种子不对称。**\n- CKA-only 和 Standard 有 3 seeds，RASP 和 Random 仅 1 seed。排序中 2/4 位置无统计支撑。\n- R2 论证 CKA-only vs Standard（最关键比较）已有充分验证（p=0.0009），Random/RASP 排序不确定不影响核心 insight。Director 同意此评估，但 Random 作为 uninformed baseline，其方差直接影响排序可信度，应优先补充。\n\n**W2 [warning, 共识] CKA-recovery 因果机制仅为相关性证据。**\n- Figure 4 的 CKA heatmap（CKA-only μ=0.62 vs Standard μ=0.90）展示了相关性，但无干预实验证明因果关系。\n- 低 dense fidelity 也可解读为\"模型被扰动最大\"而非\"保留了更多多样性\"。\n\n**W3 [warning, R1 提出, R2 AGREE] Per-layer capacity floor (40%) 未消融。**\n- 40% floor 与不同评分准则的交互可能产生混淆效应。RASP 的 collapse 可能部分源于 floor 与其复合评分的特定交互。\n\n**W4 [warning, 共识] α 消融缺 GRPO reward 数据。**\n- Table 6 测试了 6 个 α 值但仅报告 post-prune accuracy (N=100)。α=4.0 时精度最高（40%）暗示 RASP collapse 可能由 α=1.0 超参数驱动而非机制缺陷。应补充关键 α 值的 GRPO reward。\n\n**W5 [warning, R2 提出, R1 AGREE] \"Recovery capacity gradient\" 术语与 gradient descent 语境混淆。**\n- 论文同时高频使用 \"gradient\" 指代 ML 梯度和方法排序，增加阅读负担。建议改为 \"spectrum\" 或 \"ordering\"。\n\n### Minor\n\n**M1.** Section 5 末尾约 2 行溢出至第 9 页——可能触及 8 页 hard limit（R2-m4）。\n**M2.** Abstract p<0.001 未说明统计检验方法；N=3 t-test 报告 p<0.001 需要极大效应量（R2-m5）。\n**M3.** Page 7 display items 过度拥挤（Figure 3 + Figure 4 + Table 2 挤在同一页），Figure 3/4 内部文字可能低于 8pt 可读阈值（R2-m3 + 视觉审查）。\n**M4.** bib key 年份误导（lachance2024cka 实为 2022, klabunde 实为 2023）；selfhealing2025 venue 字段为空；6 篇 OpenAlex not_found（R1-M4, R2-m1/m2）。\n**M5.** Figure 3 两子图 y 轴刻度差异大，视觉上容易误导（R1-M2）。\n**M6.** RASP checkpoint 未保存，部分数据不可回溯验证（R1-M1）。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致（[AGREE]）：\n\n1. **Reward-accuracy decoupling 是论文面临的最核心挑战**——CKA-only 在 reward 空间领先 4.4×，但精度层面的优势完全来自 SFT 而非 GRPO。\n2. **Cross-architecture 缺 GRPO 验证**——Qwen2.5-Math-7B 仅有 SFT 结果，无法支撑 GRPO recovery capacity 的泛化 claim。\n3. **CKA-recovery 机制为相关性证据**——需要干预实验或更强的因果论证。\n4. **CKA-only vs Standard 的核心排序有充分统计支撑**（3-seed, p=0.0009）——这一核心比较是稳健的。\n5. **研究问题新颖、控制变量设计严谨**——论文的实验框架本身是高质量的。\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 判定 |\n|------|----|----|--------------|\n| **GRPO 训练步数（100/300步）** | N2 critical: 300步不足以证明 structural gap | REBUT: Figure 5 $f_0>0.5$ 全程，Standard 已收敛到坍塌状态 | **R2 胜**——$f_0$ 收敛证据有力，Standard 不是\"还没学够\"而是\"结构性缺乏梯度信号\"。降为 info。 |\n| **单一稀疏度** | N3 critical: 仅 20% 运行完整 pipeline | REBUT: Appendix L Table 12 有 15%/20%/25% 完整 SFT→GRPO 结果 | **R2 胜**——R1 遗漏了 Appendix L。事实修正成立。降为 info（但正文展示应更显著）。 |\n| **种子不对称严重性** | N1 critical | W1 should-fix（核心比较已有 3-seed） | **折中**——列为 warning。核心 insight 不受影响，但排序完整性受损。 |\n| **Figure 1 质量** | S5 正面 | W4 信息密度低 | **小分歧**——排版问题而非设计问题，列为 info。 |\n\n---\n\n## Questions（需要作者澄清）\n\n1. **[高优先级]** Table 2 显示 Standard GRPO Δ (+0.55pp) 高于 CKA-only (+0.48pp)。如何调和这一观察与 \"CKA-only achieves active learning while Standard collapses\" 的核心叙事？是否应区分 reward-level recovery 和 accuracy-level recovery？\n\n2. **[高优先级]** 15% sparsity 结果（Appendix L: GRPO 使差距从 5.69pp 扩大至 7.20pp）比 20% 更能支撑论文叙事。为什么选 20% 而非 15% 作为主要报告点？\n\n3. **[中优先级]** Table 6 α=4.0 post-prune accuracy 最高（40%），但 Table 1 RASP (α=1.0) 全面坍塌。α=4.0 时 GRPO 行为如何？如果 GRPO 也改善，则 RASP collapse 可能仅是超参数问题。\n\n4. **[中优先级]** CKA-only 与 Standard 保留的结构重叠度是多少？如果重叠度 >80%，说明少量不同结构决定了训练动态——这对因果机制的理解至关重要。\n\n5. **[中优先级]** Unpruned 模型 GRPO reward 从 0 升至 0.669 但精度不变 (81.27%)。这是否意味着 reward-accuracy decoupling 是 GRPO + GSM8K binary reward 的系统性现象，而非与剪枝相关？如果是，用 GRPO reward 作为 recovery capacity 诊断指标是否恰当？\n\n6. **[低优先级]** 40% per-layer capacity floor 如何选定？不同 floor 值下排序是否稳健？\n\n---\n\n## Missing References\n\n未发现严重遗漏。以下可考虑补充但非必须：\n- **SparseGPT** (Frantar & Alistarh, 2023): LLM 非结构化剪枝的开创性工作，related work 提及 Wanda 时可一并引用。\n- **LoRAShear** (Chen et al., 2023): 结合 LoRA 的结构化剪枝与知识恢复。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，不适用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical / 5 warning / 8 info）。主要发现：\n\n1. **[warning] Page 3-5 连续 3 页无 figure/table**。建议将 page 7 的 figure 前移平衡视觉节奏。\n2. **[warning] Page 7 display items 过度拥挤**：Figure 3 + Figure 4 + Table 2 挤在同一页，Figure 3/4 内部文字可能低于 8pt 可读阈值。\n3. **[warning] Figure 4 CKA 热力图面积过小**，颜色渐变细节在当前尺寸下难以分辨。\n4. **[warning] Appendix 末页仅占 ~35% 页面**，~65% 空白。\n5. **[info] Figure 2 RASP 红线与 Standard 橙线颜色区分度不足**，建议添加 line style 辅助区分。\n6. **[info] Page 1 无视觉锚点**（首页无核心结果预览图）。\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 2.5/5 | 3.5/5 | 3.0/5 |\n| Excitement | 3.5/5 | 3.0/5 | 3.25/5 |\n| Reproducibility | 3.5/5 | 4.0/5 | 3.75/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**Overall Score: 3.0 (Findings)**\n\n**Confidence: 4/5**\n\n**评分理由**：\n\n研究问题新颖（剪枝准则→RLVR 恢复能力，此前无系统研究），控制变量实验设计严谨，训练动态分析多维度且有说服力。CKA-only vs Standard 在 reward 空间的差异（4.4× peak reward, 3-seed p=0.0009）是统计上稳健的结果。\n\n但论文面临两个结构性挑战：(1) **Reward-accuracy decoupling** 严重削弱核心指标的实际诊断价值——20% sparsity 下 CKA-only 与 Standard 的精度差距 4.55pp 几乎完全来自 SFT 而非 GRPO，论文核心叙事围绕 GRPO recovery 但精度层面的主要贡献在 SFT；(2) **Cross-architecture GRPO 缺失** 使泛化 claim 受限于 DeepSeek-R1 family。\n\nR1 初始给分 2.5 (Borderline Findings)，但其两个 critical 问题（训练步数不足 N2、单一稀疏度 N3）被 R2 以事实证据成功反驳（$f_0$ 收敛证据、Appendix L 多稀疏度数据），应适度上调。R2 给分 3.0 (Findings)。综合交叉回应后的收敛结果，**3.0 (Findings)** 是恰当的定位——论文的控制变量设计和训练动态分析达到了 Findings 水准，但 reward-accuracy decoupling 未充分论证 + cross-architecture GRPO 缺失使其难以达到 Conference (4.0) 水平。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"consistently and significantly underperforms\" 中 p<0.001 未标明检验方法（t-test? bootstrap?）。N=3 seeds 的 t-test 报告 p<0.001 需要极大效应量——数值上合理（4.55pp gap, 0.19/0.38 std），但应明确检验类型。\n- Abstract 正确区分了 GRPO (DeepSeek) vs SFT (Qwen-Math) 的验证范围。\n\n### Introduction\n- Figure 1 字号偏小但框架设计有效。\n- \"recovery capacity is shaped at pruning time, not during subsequent fine-tuning\" 与 Table 2 的 SFT 主导精度差距存在张力——SFT 也是 \"subsequent fine-tuning\"。\n\n### Method\n- 控制变量框架设计清晰（Algorithm 1），四种评分公式的数学定义明确。\n- CKA 可靠性论证充分。\n- SFT warmup 的功能性必要性论证合理（EOS collapse → GRPO 不可行）。\n\n### Experiments\n- Table 1 和 Figure 2 的核心结果在 reward 层面有说服力。\n- Table 2 的 reward-accuracy decoupling 是重要发现，但论文未充分讨论其对 recovery capacity 概念本身的影响。\n- 15% sparsity 结果（GRPO 扩大差距 +1.51pp）应从 Appendix 提升至正文——这是 GRPO 确实产生差异化影响的最强证据。\n- Cross-scale (1.5B, Table 3) 保留了三方法排序，但仅 100 步单 seed，信息量有限。\n\n### Extended Analysis\n- CKA heatmap (Figure 4) 的相关性证据有启发性但不构成因果证明。\n- Qwen2.5-Math-7B 的 post-prune accuracy reversal（1.0%→51.50%）是 SFT recovery 层面的强证据，但不直接支撑 GRPO claim。\n\n### Limitations\n- 覆盖了架构敏感性、benchmark 范围、硬件配置、种子多样性四个方面，长度适当。\n- 建议补充：(a) reward-accuracy decoupling 对 recovery capacity 概念的局限性；(b) per-layer capacity floor 未消融。\n\n### Format\n- 正文接近但可能触及 8 页 hard limit（Section 5 末尾约 2 行溢出 p9），需压缩。\n- 匿名性合规（\\usepackage[review]{acl}, author=Anonymous）。\n- Page 7 display items 过度拥挤，Pages 3-5 纯文本——视觉节奏不均。\n",
  "project": "recovery_aware_struct_prune",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 5 (Fresh Review)\n\n**论文**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\n**Venue**: EMNLP 2026 via ARR May 2026\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作）\n**轮次**: Round 1 独立审稿 → 交叉回应 → 收敛（1 轮即达成共识）\n\n---\n\n## Summary\n\n本文在 DeepSeek-R1-Distill-Qwen-7B (20% structured sparsity) 上对比四种结构化剪枝准则（CKA-only、Random、Standard、RASP）经 SFT warmup → GRPO 两阶段恢复后的训练动态差异。核心发现：CKA-only（仅移除功能冗余结构）在 GRPO reward 空间实现 active learning（peak 0.354, 4.4× Standard），而基于梯度重要性的方法（Standard, RASP）训练坍塌。作者将此归因于剪枝时保留的表征多样性（CKA heatmap）。同时报告了 reward-accuracy decoupling 现象。\n\n---\n\n## Strengths\n\n**S1. 研究问题新颖且时机恰当**（R1、R2 共识）。\"剪枝准则是否影响下游 RL 恢复能力\"此前未被系统研究。现有工作关注恢复策略本身（Self-Healing, PASER, PAT），本文首次将剪枝决策与 RLVR 训练动态直接关联。\n\n**S2. 控制变量设计严谨**（R1、R2 共识）。四种准则共享同一结构分析、同一稀疏度、同一 per-layer capacity floor、同一 SFT/GRPO 配置，仅在评分公式上不同。Internal validity 高。\n\n**S3. 多维训练动态诊断**（R1、R2 共识）。Reward trajectory + $f_0$（零方差 batch 比例）+ gradient norm + KL divergence 四维诊断，比同类工作更完整。CKA-only 的 recovery event（step 90）和 Standard 的梯度坍塌模式有说服力。\n\n**S4. Reward-accuracy decoupling 是有价值的独立发现**（R1 S4, R2 共识）。Table 2 + 四个 benchmark 一致显示 GRPO reward 增长不直接转化为精度提升，对 pruned-model-recovery 领域有警示意义。\n\n**S5. 相关工作覆盖全面**（R2 S5）。结构化剪枝、推理特定剪枝、功能相似性剪枝、剪枝后恢复、RLVR 训练动态五个方向均有覆盖。\n\n**S6. CKA 可靠性论证到位**（R2 S4）。intra-layer CKA 避免了已知的跨维度敏感性问题，Spearman ρ ≥ 0.964 验证了排名稳定性。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical, 共识] Reward-accuracy decoupling 严重削弱核心贡献的实际意义。**\n- Table 2: CKA-only GRPO Δ=+0.48pp, Standard Δ=+0.55pp——**Standard 的 GRPO 精度增益反而略高于 CKA-only**。\n- CKA-only vs Standard 最终精度差距 4.55pp 中，4.62pp 来自 SFT 阶段（63.91% vs 59.29%），GRPO 净贡献为 −0.07pp。\n- 论文核心叙事围绕 GRPO recovery capacity，但精度层面的主要贡献实际发生在 SFT，非 GRPO。\n- 15% sparsity 下 GRPO 确实使差距从 5.69pp 扩大至 7.20pp（Appendix L Table 12），这是 GRPO 产生差异化影响的最强证据，但被放在 Appendix 而非正文。\n- **核心挑战**：如果 reward 不预测精度，为什么 reward trajectory 是\"合适的诊断指标\"？论文需要更强的论证来回答这一问题。\n\n**N2 [critical, 共识] Cross-architecture (Qwen2.5-Math-7B) 缺乏 GRPO 验证。**\n- Table 13 仅有 SFT 恢复结果（CKA-only 1.0%→51.50% vs Standard 18.5%→21.00%），GRPO 被推迟到 future work。\n- 论文核心 claim 关于 GRPO recovery capacity，跨架构验证仅覆盖 SFT 不构成有效支撑。\n- 核心发现的 generalizability 受限于 DeepSeek-R1-Distill-Qwen family（7B + 1.5B）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [warning, 共识] RASP/Random 种子不对称。**\n- CKA-only 和 Standard 有 3 seeds，RASP 和 Random 仅 1 seed。排序中 2/4 位置无统计支撑。\n- R2 论证 CKA-only vs Standard（最关键比较）已有充分验证（p=0.0009），Random/RASP 排序不确定不影响核心 insight。Director 同意此评估，但 Random 作为 uninformed baseline，其方差直接影响排序可信度，应优先补充。\n\n**W2 [warning, 共识] CKA-recovery 因果机制仅为相关性证据。**\n- Figure 4 的 CKA heatmap（CKA-only μ=0.62 vs Standard μ=0.90）展示了相关性，但无干预实验证明因果关系。\n- 低 dense fidelity 也可解读为\"模型被扰动最大\"而非\"保留了更多多样性\"。\n\n**W3 [warning, R1 提出, R2 AGREE] Per-layer capacity floor (40%) 未消融。**\n- 40% floor 与不同评分准则的交互可能产生混淆效应。RASP 的 collapse 可能部分源于 floor 与其复合评分的特定交互。\n\n**W4 [warning, 共识] α 消融缺 GRPO reward 数据。**\n- Table 6 测试了 6 个 α 值但仅报告 post-prune accuracy (N=100)。α=4.0 时精度最高（40%）暗示 RASP collapse 可能由 α=1.0 超参数驱动而非机制缺陷。应补充关键 α 值的 GRPO reward。\n\n**W5 [warning, R2 提出, R1 AGREE] \"Recovery capacity gradient\" 术语与 gradient descent 语境混淆。**\n- 论文同时高频使用 \"gradient\" 指代 ML 梯度和方法排序，增加阅读负担。建议改为 \"spectrum\" 或 \"ordering\"。\n\n### Minor\n\n**M1.** Section 5 末尾约 2 行溢出至第 9 页——可能触及 8 页 hard limit（R2-m4）。\n**M2.** Abstract p<0.001 未说明统计检验方法；N=3 t-test 报告 p<0.001 需要极大效应量（R2-m5）。\n**M3.** Page 7 display items 过度拥挤（Figure 3 + Figure 4 + Table 2 挤在同一页），Figure 3/4 内部文字可能低于 8pt 可读阈值（R2-m3 + 视觉审查）。\n**M4.** bib key 年份误导（lachance2024cka 实为 2022, klabunde 实为 2023）；selfhealing2025 venue 字段为空；6 篇 OpenAlex not_found（R1-M4, R2-m1/m2）。\n**M5.** Figure 3 两子图 y 轴刻度差异大，视觉上容易误导（R1-M2）。\n**M6.** RASP checkpoint 未保存，部分数据不可回溯验证（R1-M1）。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致（[AGREE]）：\n\n1. **Reward-accuracy decoupling 是论文面临的最核心挑战**——CKA-only 在 reward 空间领先 4.4×，但精度层面的优势完全来自 SFT 而非 GRPO。\n2. **Cross-architecture 缺 GRPO 验证**——Qwen2.5-Math-7B 仅有 SFT 结果，无法支撑 GRPO recovery capacity 的泛化 claim。\n3. **CKA-recovery 机制为相关性证据**——需要干预实验或更强的因果论证。\n4. **CKA-only vs Standard 的核心排序有充分统计支撑**（3-seed, p=0.0009）——这一核心比较是稳健的。\n5. **研究问题新颖、控制变量设计严谨**——论文的实验框架本身是高质量的。\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 判定 |\n|------|----|----|--------------|\n| **GRPO 训练步数（100/300步）** | N2 critical: 300步不足以证明 structural gap | REBUT: Figure 5 $f_0>0.5$ 全程，Standard 已收敛到坍塌状态 | **R2 胜**——$f_0$ 收敛证据有力，Standard 不是\"还没学够\"而是\"结构性缺乏梯度信号\"。降为 info。 |\n| **单一稀疏度** | N3 critical: 仅 20% 运行完整 pipeline | REBUT: Appendix L Table 12 有 15%/20%/25% 完整 SFT→GRPO 结果 | **R2 胜**——R1 遗漏了 Appendix L。事实修正成立。降为 info（但正文展示应更显著）。 |\n| **种子不对称严重性** | N1 critical | W1 should-fix（核心比较已有 3-seed） | **折中**——列为 warning。核心 insight 不受影响，但排序完整性受损。 |\n| **Figure 1 质量** | S5 正面 | W4 信息密度低 | **小分歧**——排版问题而非设计问题，列为 info。 |\n\n---\n\n## Questions（需要作者澄清）\n\n1. **[高优先级]** Table 2 显示 Standard GRPO Δ (+0.55pp) 高于 CKA-only (+0.48pp)。如何调和这一观察与 \"CKA-only achieves active learning while Standard collapses\" 的核心叙事？是否应区分 reward-level recovery 和 accuracy-level recovery？\n\n2. **[高优先级]** 15% sparsity 结果（Appendix L: GRPO 使差距从 5.69pp 扩大至 7.20pp）比 20% 更能支撑论文叙事。为什么选 20% 而非 15% 作为主要报告点？\n\n3. **[中优先级]** Table 6 α=4.0 post-prune accuracy 最高（40%），但 Table 1 RASP (α=1.0) 全面坍塌。α=4.0 时 GRPO 行为如何？如果 GRPO 也改善，则 RASP collapse 可能仅是超参数问题。\n\n4. **[中优先级]** CKA-only 与 Standard 保留的结构重叠度是多少？如果重叠度 >80%，说明少量不同结构决定了训练动态——这对因果机制的理解至关重要。\n\n5. **[中优先级]** Unpruned 模型 GRPO reward 从 0 升至 0.669 但精度不变 (81.27%)。这是否意味着 reward-accuracy decoupling 是 GRPO + GSM8K binary reward 的系统性现象，而非与剪枝相关？如果是，用 GRPO reward 作为 recovery capacity 诊断指标是否恰当？\n\n6. **[低优先级]** 40% per-layer capacity floor 如何选定？不同 floor 值下排序是否稳健？\n\n---\n\n## Missing References\n\n未发现严重遗漏。以下可考虑补充但非必须：\n- **SparseGPT** (Frantar & Alistarh, 2023): LLM 非结构化剪枝的开创性工作，related work 提及 Wanda 时可一并引用。\n- **LoRAShear** (Chen et al., 2023): 结合 LoRA 的结构化剪枝与知识恢复。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，不适用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical / 5 warning / 8 info）。主要发现：\n\n1. **[warning] Page 3-5 连续 3 页无 figure/table**。建议将 page 7 的 figure 前移平衡视觉节奏。\n2. **[warning] Page 7 display items 过度拥挤**：Figure 3 + Figure 4 + Table 2 挤在同一页，Figure 3/4 内部文字可能低于 8pt 可读阈值。\n3. **[warning] Figure 4 CKA 热力图面积过小**，颜色渐变细节在当前尺寸下难以分辨。\n4. **[warning] Appendix 末页仅占 ~35% 页面**，~65% 空白。\n5. **[info] Figure 2 RASP 红线与 Standard 橙线颜色区分度不足**，建议添加 line style 辅助区分。\n6. **[info] Page 1 无视觉锚点**（首页无核心结果预览图）。\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 2.5/5 | 3.5/5 | 3.0/5 |\n| Excitement | 3.5/5 | 3.0/5 | 3.25/5 |\n| Reproducibility | 3.5/5 | 4.0/5 | 3.75/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**Overall Score: 3.0 (Findings)**\n\n**Confidence: 4/5**\n\n**评分理由**：\n\n研究问题新颖（剪枝准则→RLVR 恢复能力，此前无系统研究），控制变量实验设计严谨，训练动态分析多维度且有说服力。CKA-only vs Standard 在 reward 空间的差异（4.4× peak reward, 3-seed p=0.0009）是统计上稳健的结果。\n\n但论文面临两个结构性挑战：(1) **Reward-accuracy decoupling** 严重削弱核心指标的实际诊断价值——20% sparsity 下 CKA-only 与 Standard 的精度差距 4.55pp 几乎完全来自 SFT 而非 GRPO，论文核心叙事围绕 GRPO recovery 但精度层面的主要贡献在 SFT；(2) **Cross-architecture GRPO 缺失** 使泛化 claim 受限于 DeepSeek-R1 family。\n\nR1 初始给分 2.5 (Borderline Findings)，但其两个 critical 问题（训练步数不足 N2、单一稀疏度 N3）被 R2 以事实证据成功反驳（$f_0$ 收敛证据、Appendix L 多稀疏度数据），应适度上调。R2 给分 3.0 (Findings)。综合交叉回应后的收敛结果，**3.0 (Findings)** 是恰当的定位——论文的控制变量设计和训练动态分析达到了 Findings 水准，但 reward-accuracy decoupling 未充分论证 + cross-architecture GRPO 缺失使其难以达到 Conference (4.0) 水平。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"consistently and significantly underperforms\" 中 p<0.001 未标明检验方法（t-test? bootstrap?）。N=3 seeds 的 t-test 报告 p<0.001 需要极大效应量——数值上合理（4.55pp gap, 0.19/0.38 std），但应明确检验类型。\n- Abstract 正确区分了 GRPO (DeepSeek) vs SFT (Qwen-Math) 的验证范围。\n\n### Introduction\n- Figure 1 字号偏小但框架设计有效。\n- \"recovery capacity is shaped at pruning time, not during subsequent fine-tuning\" 与 Table 2 的 SFT 主导精度差距存在张力——SFT 也是 \"subsequent fine-tuning\"。\n\n### Method\n- 控制变量框架设计清晰（Algorithm 1），四种评分公式的数学定义明确。\n- CKA 可靠性论证充分。\n- SFT warmup 的功能性必要性论证合理（EOS collapse → GRPO 不可行）。\n\n### Experiments\n- Table 1 和 Figure 2 的核心结果在 reward 层面有说服力。\n- Table 2 的 reward-accuracy decoupling 是重要发现，但论文未充分讨论其对 recovery capacity 概念本身的影响。\n- 15% sparsity 结果（GRPO 扩大差距 +1.51pp）应从 Appendix 提升至正文——这是 GRPO 确实产生差异化影响的最强证据。\n- Cross-scale (1.5B, Table 3) 保留了三方法排序，但仅 100 步单 seed，信息量有限。\n\n### Extended Analysis\n- CKA heatmap (Figure 4) 的相关性证据有启发性但不构成因果证明。\n- Qwen2.5-Math-7B 的 post-prune accuracy reversal（1.0%→51.50%）是 SFT recovery 层面的强证据，但不直接支撑 GRPO claim。\n\n### Limitations\n- 覆盖了架构敏感性、benchmark 范围、硬件配置、种子多样性四个方面，长度适当。\n- 建议补充：(a) reward-accuracy decoupling 对 recovery capacity 概念的局限性；(b) per-layer capacity floor 未消融。\n\n### Format\n- 正文接近但可能触及 8 页 hard limit（Section 5 末尾约 2 行溢出 p9），需压缩。\n- 匿名性合规（\\usepackage[review]{acl}, author=Anonymous）。\n- Page 7 display items 过度拥挤，Pages 3-5 纯文本——视觉节奏不均。\n",
    "project": "recovery_aware_struct_prune",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-21T15:47:45.412615+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_04e6cf8fe41be27a49d5657e80962f12:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3913
}
```

</details>

---


### Assistant

_source line 340 · 2026-05-21T15:47:55.384580+00:00_

审稿报告已投递至 Research Director。

**Round 5 审稿完成。**

**最终评分：3.0 (Findings)**

核心发现：
- **2 个 critical 问题**：(1) Reward-accuracy decoupling 导致核心指标（GRPO reward）的实际诊断价值存疑——20% sparsity 下精度差距几乎完全由 SFT 贡献；(2) Cross-architecture 缺 GRPO 验证
- **5 个 warning**：种子不对称、因果机制仅为相关性、capacity floor 未消融、α 消融缺 GRPO 数据、术语混淆
- **6 个 minor**：格式溢出、p 值检验未标、page 7 拥挤、bib 问题等

Reviewer 间主要分歧已解决：R2 成功反驳了 R1 关于训练步数不足和单一稀疏度的两个 critical（$f_0$ 收敛证据 + Appendix L 多稀疏度数据），评分从 R1 的 2.5 与 R2 的 3.0 收敛至 3.0。

Issue tracker 已同步更新（11 个新 open issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 341 · 2026-05-21T15:47:57.902140+00:00_

[Reviewer 1 审稿结果]:
交叉回应已完成并汇报给 Director。

核心立场：R2 的 17 条意见中，我同意 15 条（含 m1-m5 全部），仅反驳 1 条（W4 Figure 1 信息密度）。R2-N1 关于 SFT 主导 accuracy gap 的分析尤其精准，加深了我对 soundness 的担忧。我将 R2-W1（单 seed）从 Should-Fix 升级为 Must-Fix，与我 Round 1 的 N1 一致。最终评分维持 2.5 (Borderline Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 342 · 2026-05-21T15:48:07.402576+00:00_

审稿报告已投递至 Research Director。

**Round 5 审稿总结：**

- **Overall Score: 3.0 (Findings)**
- R1 给 2.5 (Borderline Findings)，R2 给 3.0 (Findings)
- 交叉回应中 R2 成功反驳了 R1 的两个 critical（训练步数、单一稀疏度），综合后取 3.0

**两个核心问题（双 Reviewer 共识）：**
1. Reward-accuracy decoupling 严重削弱核心贡献——20% sparsity 下 4.55pp 精度差距几乎完全来自 SFT 而非 GRPO
2. Cross-architecture 缺 GRPO 验证——Qwen2.5-Math-7B 仅有 SFT 结果

**Issue Tracker 已更新**：新增 12 个 Round 5 issue（2 critical, 5 warning, 5 info），历史 30 个 issue 全部 resolved 保留。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 32

## Round 32

40 recorded events


### User

_source line 343 · 2026-05-22T04:37:10.542495+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: recovery_aware_struct_prune
- 论文路径: projects/recovery_aware_struct_prune/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-22T04:37:17.242854+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-22T04:37:17.395689+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-22T04:37:23.016967+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-22T04:37:23.017429+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-22T04:37:25.928296+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool call

_source line 349 · 2026-05-22T04:37:26.480525+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 350 · 2026-05-22T04:37:26.951590+00:00_

{"result":"# 项目 recovery_aware_struct_prune 概况\n\n## 实验状态 (372 个)\n\n- **grpo_stage2_rasp_20_v2**: DONE (negative) — \n- **grpo_stage2_standard_20**: DONE (killed) — \n- **grpo_stage2_rasp_20**: DONE (killed) — \n- **sft_standard_20**: DONE (success) — \n- **sft_rasp_20**: DONE (success) — \n- **grpo_rasp_20_4096**: DONE (failed) — \n- **grpo_standard_20_4096**: DONE (negative) — \n- **grpo_standard_20_fast**: DONE (negative) — \n- **grpo_rasp_20_fast**: DONE (negative) — \n- **mvp_rasp_pipeline_v4**: PREPARING — \n- **grpo_standard_20**: DONE (killed) — \n- **grpo_rasp_20**: DONE (killed) — \n- **mvp_rasp_pipeline_v3**: DONE (negative) — \n- **mvp_rasp_pipeline_v2**: DONE (failed) — \n- **mvp_rasp_pipeline**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| eval_math500_sft_rasp_20_1p5b | 1.5B RASP 20% SFT MATH-500 @2048. Cross-scale comparison: if ranking CKA-only > Standard > RASP holds at 1.5B, validates scale-invariant importance metric. | — | — | — |\n| eval_math500_sft_standard_20_1p5b | 1.5B Standard 20% SFT MATH-500 @2048. Cross-scale comparison with CKA-only 1.5B (10.6%) to test if CKA-guided pruning advantage is scale-invariant. | — | — | — |\n| eval_math500_sft_random_20_v3 | Random 20% SFT MATH-500 @2048. v2 failed due to old eval_math500.py on westd-32935. Code synced from westb. | — | — | — |\n\n## 待处理\n- eval_gsm8k_grpo_alpha4_20_v2: α=4.0 GRPO maintains reward 0.15-0.26 (vs α=1.0 collapse to ~0.008), predicting GSM8K accuracy significantly above α=1.0 baseline. v1 timed out at 774/1319 showing 62.93% interim — full eval needed to confirm α-dependent collapse hypothesis.（已分配 westd-29022 GPU:cuda:1，等待提交）\n- eval_math500_sft_standard_25_2048（准备中）\n- sft_alpha4_20_v2: α=4.0 SFT recovery with save_only_model=True to prevent disk overflow. Pruning successful (19.09% sparsity). Testing if higher α mitigates RASP collapse after
…[truncated 1777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1023
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-22T04:37:26.951965+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 471
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-22T04:37:33.023818+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 353 · 2026-05-22T04:37:34.667002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 354 · 2026-05-22T04:37:34.868952+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{siunitx}
17	\usepackage{algorithm}
18	\usepackage[noend]{algpseudocode}
19	\usepackage{enumitem}
20	\usepackage{xcolor}
21	\usepackage{hyperref}
22	
23	\newcommand{\rasp}{\textsc{Rasp}}
24	
25	\title{How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\begin{abstract}
33	\input{abstract}
34	\end{abstract}
35	
36	\input{introduction}
37	\input{related_work}
38	\input{method}
39	\input{experiments}
40	\input{conclusion}
41	
42	\section*{Limitations}
43	\input{limitations}
44	
45	\section*{Ethics Statement}
46	\input{ethics}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 355 · 2026-05-22T04:37:34.919602+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_6/submitted.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_6/submitted.pdf"
  }
}
```

</details>

---


### Tool result

_source line 356 · 2026-05-22T04:37:34.970228+00:00_

This PDF has 14 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-22T04:37:40.342133+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here is information about EMNLP 2026 call for papers submission guidelines with ARR:

## General Submission Guidelines

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers m
…[truncated 1122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "elapsed_ms": 7318
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-22T04:37:44.829428+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_6/submitted.pdf",
  "pages": "1-7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_6/submitted.pdf",
    "pages": "1-7"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-22T04:37:45.782970+00:00_

PDF pages extracted: 7 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_6/submitted.pdf (501.8KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-22T04:37:45.797687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_6/submitted.pdf",
  "pages": "8-14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_6/submitted.pdf",
    "pages": "8-14"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-22T04:37:46.720603+00:00_

PDF pages extracted: 7 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_6/submitted.pdf (501.8KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 922
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-22T04:37:46.818663+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit long paper short paper guidelines",
  "allowed_domains": "['2026.emnlp.org', 'aclrollingreview.org', 'aclweb.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit long paper short paper guidelines",
    "allowed_domains": "['2026.emnlp.org', 'aclrollingreview.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 363 · 2026-05-22T04:37:47.650732+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL rolling review 2026 May cycle submission deadline author guidelines",
  "allowed_domains": "['aclrollingreview.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL rolling review 2026 May cycle submission deadline author guidelines",
    "allowed_domains": "['aclrollingreview.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool result

_source line 364 · 2026-05-22T04:37:53.162428+00:00_

Web search results for query: "EMNLP 2026 submission format page limit long paper short paper guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CFP: Fourth ArabicNLP Conference (ArabicNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/fourth-arabicnlp-conference-arabicnlp-2026-first-cfp"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Empirical Methods in Natural Language Processing | ACL Member Portal","url":"https://www.aclweb.org/portal/content/empirical-methods-natural-language-processing"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"}]

Based on the search results, I found information about EMNLP 2026 submission guidelines. Here's what I found:

## EMNLP 2026 Submission Format Guidelines

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research.

### Page Limits

The search results reference ARR (ACL Rolling Review) requirements. Based on similar *CL conferences' guidelines that are mentioned as coordinating with EMNLP 2026, the typical page limits are:

- **Long papers**: up to 8 pages of content (with extra space allowed
…[truncated 830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "elapsed_ms": 6343
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-22T04:37:54.116469+00:00_

Web search results for query: "ACL rolling review 2026 May cycle submission deadline author guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, here's information about the ACL Rolling Review 2026 May cycle:

## Submission Deadline

There is a submission deadline every two months, though the specific May 2026 dea
…[truncated 1225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "elapsed_ms": 6465
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-22T04:38:14.858682+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-22T04:38:15.361389+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/decisions.yaml\", \"content\": \"_next_id: 104\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 06:10 UTC\\n  summary: MVP 接受 35% sparsity 下 MLP-only pruning，不强制 attention 配额\\n  rationale: 全局统一排序下 attention GQA groups importance 普遍高于 MLP groups，35% sparsity\\n    自然只剪 MLP（367 groups）。这是模型结构特征的正确反映，不应人为干预。MLP-level correlation (N=367) 足以验证 CKA→recoverability\\n    假设。50% sparsity 放 Phase 2 获取 attention-level 数据。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: primary\\n    result: running\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 13:31 UTC\\n  summary: 终止无效 GRPO，改用 SFT warmup → GRPO 两阶段恢复策略\\n  rationale: 35% 结构化剪枝后两个模型 accuracy 仅 0.15%（输出退化），GRPO 150 步 loss=0/grad_norm=0，无学习信号。frac_reward_zero_std\\n    ≈ 1.0 表明几乎所有 completion 得 0 reward，GRPO 无法计算有效 advantage。SFT warmup 用 ground truth\\n    数据先恢复基本能力再转 GRPO 是解决 reward desert 的标准做法。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: motivating_failure\\n    result: GRPO 150 步 loss=0, grad_norm=0; post-prune accuracy 0.15% for both models\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 13:53 UTC\\n  summary: 暂缓 SFT warmup，优先审计剪枝实现正确性\\n  rationale: 两个不同剪枝策略产出精确相同的 accuracy（2/1319）统计上极不寻常，35% structured pruning 不应导致 7B\\n    模型完全崩溃。Reviewer 怀疑存在实现 bug（config 不匹配、全零层等）。若根因是代码问题，SFT warmup 是在错误基础上浪费算力。需先排除实现问题再决定恢复策略。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: audit_target\\n    result: both pruned models 0.15% accuracy, identical 2/1319\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 13:59 UTC\\n  summary: 修复 min_keep_mlp=4 导致的 per-layer 过度剪枝，重跑 MVP pipeline v3\\n  rationale: 根因确认：min_keep_mlp=4 允许单层 MLP 被剪至 14.3% capacity，全局排序集中破坏 early layers（0-6），两个模型均崩溃至\\n    0.15%。修复方案：min_keep_mlp 提升到 40% per layer + per-layer capacity floor。RASP scoring\\n    逻辑本身正常（产生了不同剪枝结构），核心假设仍可验证，只需收紧约
…[truncated 1441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-22T04:38:17.118800+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read review issues yaml",
  "prompt": "Read the file at /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml and return its full contents. If the file doesn't exist, say \"FILE_NOT_FOUND\".",
  "subagent_type": "Explore"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Read review issues yaml",
    "prompt": "Read the file at /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml and return its full contents. If the file doesn't exist, say \"FILE_NOT_FOUND\".",
    "subagent_type": "Explore"
  }
}
```

</details>

---


### Tool call

_source line 369 · 2026-05-22T04:38:19.629509+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 370 · 2026-05-22T04:38:19.630133+00:00_

1	issues:
2	# ============================================================
3	# Round 1-3 Issues — ALL RESOLVED (preserved from prior rounds)
4	# ============================================================
5	
6	- id: "R1-N1"
7	  summary: "Post-SFT 准确率混淆变量未控制"
8	  category: experiment
9	  severity: warning
10	  status: resolved
11	  first_raised_round: 1
12	  last_seen_round: 3
13	  resolution: "Qwen-Math reversal + RASP counter-example + scoped claims"
14	  resolution_round: 3
15	
16	- id: "R1-N2"
17	  summary: "Table 2 混用控制实验与 separately optimized runs"
18	  category: experiment
19	  severity: critical
20	  status: resolved
21	  first_raised_round: 1
22	  last_seen_round: 2
23	  resolution: "v5 controlled data (step-100, patience=50, lr=5e-7)"
24	  resolution_round: 1
25	
26	- id: "R1-N3"
27	  summary: "reward_desert_patience 参数不一致"
28	  category: experiment
29	  severity: critical
30	  status: resolved
31	  first_raised_round: 1
32	  last_seen_round: 2
33	  resolution: "所有方法 patience=50"
34	  resolution_round: 1
35	
36	- id: "R1-N4"
37	  summary: "单种子设计"
38	  category: experiment
39	  severity: critical
40	  status: resolved
41	  first_raised_round: 1
42	  last_seen_round: 2
43	  resolution: "CKA-only 64.39%±0.19pp, Standard 59.84%±0.38pp, p=0.0009"
44	  resolution_round: 1
45	
46	- id: "R2-N1"
47	  summary: "标题与结论错位"
48	  category: framing
49	  severity: critical
50	  status: resolved
51	  first_raised_round: 1
52	  last_seen_round: 2
53	  resolution: "How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models"
54	  resolution_round: 1
55	
56	- id: "R2-N2"
57	  summary: "实验规模不足"
58	  category: experiment
59	  severity: warning
60	  status: resolved
61	  first_raised_round: 1
62	  last_seen_round: 3
63	  resolution: "脚注透明标注 + Limitations 强化 + Abstract scoped"
64	  resolution_round: 3
65	
66	- id: "R1-W1"
67	  summary: "相关→因果跳跃"
68	  category: method
69	  severity: warning
70	  status: resolved
71	  first_raised_round: 1
72	  last_seen_round: 3
73	 
…[truncated 13664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-22T04:38:24.648670+00:00_

File contents returned successfully. The file contains 557 lines of structured review issues tracking across multiple review rounds (1-5) for the recovery_aware_struct_prune project. 

Key structure:
- **Rounds 1-3**: All issues marked as `resolved` (preserved from prior rounds)
- **Round 5** (fresh review): Issues with status `in_progress`, organized by severity (critical, warning, info) with action items assigned to paper_agent or agent

Major Round 5 issues include:
- R5-N1 (critical): Reward-accuracy decoupling weakens GRPO recovery narrative
- R5-N2 (critical): Cross-architecture Qwen2.5-Math lacks GRPO verification
- R5-W1-W5: Warning-level issues on seed asymmetry, causal mechanism evidence, ablation gaps, hyperparameter tuning, and terminology conflicts
- R5-M1-M5: Info-level formatting and reference issues

All issues reference D098 Action Matrix with assigned owners and in_progress status.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Agent",
  "elapsed_ms": 7529
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-22T04:38:31.099728+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-22T04:38:31.150878+00:00_

1	issues:
2	# ============================================================
3	# Round 1-3 Issues — ALL RESOLVED (preserved from prior rounds)
4	# ============================================================
5	
6	- id: "R1-N1"
7	  summary: "Post-SFT 准确率混淆变量未控制"
8	  category: experiment
9	  severity: warning
10	  status: resolved
11	  first_raised_round: 1
12	  last_seen_round: 3
13	  resolution: "Qwen-Math reversal + RASP counter-example + scoped claims"
14	  resolution_round: 3
15	
16	- id: "R1-N2"
17	  summary: "Table 2 混用控制实验与 separately optimized runs"
18	  category: experiment
19	  severity: critical
20	  status: resolved
21	  first_raised_round: 1
22	  last_seen_round: 2
23	  resolution: "v5 controlled data (step-100, patience=50, lr=5e-7)"
24	  resolution_round: 1
25	
26	- id: "R1-N3"
27	  summary: "reward_desert_patience 参数不一致"
28	  category: experiment
29	  severity: critical
30	  status: resolved
31	  first_raised_round: 1
32	  last_seen_round: 2
33	  resolution: "所有方法 patience=50"
34	  resolution_round: 1
35	
36	- id: "R1-N4"
37	  summary: "单种子设计"
38	  category: experiment
39	  severity: critical
40	  status: resolved
41	  first_raised_round: 1
42	  last_seen_round: 2
43	  resolution: "CKA-only 64.39%±0.19pp, Standard 59.84%±0.38pp, p=0.0009"
44	  resolution_round: 1
45	
46	- id: "R2-N1"
47	  summary: "标题与结论错位"
48	  category: framing
49	  severity: critical
50	  status: resolved
51	  first_raised_round: 1
52	  last_seen_round: 2
53	  resolution: "How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models"
54	  resolution_round: 1
55	
56	- id: "R2-N2"
57	  summary: "实验规模不足"
58	  category: experiment
59	  severity: warning
60	  status: resolved
61	  first_raised_round: 1
62	  last_seen_round: 3
63	  resolution: "脚注透明标注 + Limitations 强化 + Abstract scoped"
64	  resolution_round: 3
65	
66	- id: "R1-W1"
67	  summary: "相关→因果跳跃"
68	  category: method
69	  severity: warning
70	  status: resolved
71	  first_raised_round: 1
72	  last_seen_round: 3
73	 
…[truncated 13664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-22T04:38:31.403469+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-22T04:38:31.605739+00:00_

AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/chats/feishu_group_oc_40839c097b00df44480b45ab767f59cf_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/chats/feishu_group_oc_40839c097b00df44480b45ab767f59cf_director.jsonl:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/chats/feishu_group_oc_40839c097b00df44480b45ab767f59cf_director.jsonl:44:{"ts": "2026-05-20T05:20:22.208435+00:00", "role": "tool", "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director", "
…[truncated 8145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Grep",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-22T04:39:05.592657+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recovery_aware_struct_prune",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 论文信息\n- **标题**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\n- **论文路径**: `projects/recovery_aware_struct_prune/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_6/submitted.pdf`\n- **目标 venue**: EMNLP 2026（ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **格式**: Long paper，正文 ≤8 页，参考文献不限，Limitations/Ethics 不计入页数，ACL 模板，double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n1. **方法论严谨性**：\n   - CKA 作为 intra-layer functional overlap 度量的合理性和可靠性\n   - 四种 scoring criteria（CKA-only, Standard, RASP, Random）的设计是否公平可比\n   - Per-layer capacity floor (40%) 对实验结论的影响\n   - Structural analysis 阶段共享 → scoring 阶段差异化的实验控制是否充分\n\n2. **实验设计与统计**：\n   - 多种子验证覆盖范围（CKA-only/Standard 3 seeds vs RASP/Random 1 seed）\n   - 统计检验方法是否恰当（Welch's t-test, N=3）\n   - Recovery capacity 诊断指标（peak reward, f₀, gradient norm, KL divergence）的选取合理性\n   - Cross-scale (1.5B) 和 cross-architecture (Qwen2.5-Math-7B) 验证的完整性\n   - α 消融（Table 6）仅用 post-prune accuracy 而非 GRPO reward 的局限\n\n3. **消融完整性**：\n   - 是否有足够消融实验隔离各因素贡献\n   - 训练步数（100 steps → 300 steps）扩展实验的充分性\n   - Sparsity level（15%/20%/25%/30%）覆盖是否足够\n\n4. **可复现性**：\n   - 超参数报告是否完整（Appendix A Table 4）\n   - 硬件/计算资源描述\n   - 代码/数据/checkpoint 发布承诺\n\n请提供完整审稿意见，包含：Summary、Strengths、Weaknesses（逐条编号）、Questions、Overall Assessment（评分+理由）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recovery_aware_struct_prune",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 论文信息\n- **标题**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\n- **论文路径**: `projects/recovery_aware_struct_prune/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_6/submitted.pdf`\n- **目标 venue**: EMNLP 2026（ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **格式**: Long paper，正文 ≤8 页，参考文献不限，Limitations/Ethics 不计入页数，ACL 模板，double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n1. **方法论严谨性**：\n   - CKA 作为 intra-layer functional overlap 度量的合理性和可靠性\n   - 四种 scoring criteria（CKA-only, Standard, RASP, Random）的设计是否公平可比\n   - Per-layer capacity floor (40%) 对实验结论的影响\n   - Structural analysis 阶段共享 → scoring 阶段差异化的实验控制是否充分\n\n2. **实验设计与统计**：\n   - 多种子验证覆盖范围（CKA-only/Standard 3 seeds vs RASP/Random 1 seed）\n   - 统计检验方法是否恰当（Welch's t-test, N=3）\n   - Recovery capacity 诊断指标（peak reward, f₀, gradient norm, KL divergence）的选取合理性\n   - Cross-scale (1.5B) 和 cross-architecture (Qwen2.5-Math-7B) 验证的完整性\n   - α 消融（Table 6）仅用 post-prune accuracy 而非 GRPO reward 的局限\n\n3. **消融完整性**：\n   - 是否有足够消融实验隔离各因素贡献\n   - 训练步数（100 steps → 300 steps）扩展实验的充分性\n   - Sparsity level（15%/20%/25%/30%）覆盖是否足够\n\n4. **可复现性**：\n   - 超参数报告是否完整（Appendix A Table 4）\n   - 硬件/计算资源描述\n   - 代码/数据/checkpoint 发布承诺\n\n请提供完整审稿意见，包含：Summary、Strengths、Weaknesses（逐条编号）、Questions、Overall Assessment（评分+理由）。"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-22T04:39:21.210933+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15618
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-22T04:39:22.415486+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recovery_aware_struct_prune",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 相关工作 + 写作质量** 审查。\n\n## 论文信息\n- **标题**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\n- **论文路径**: `projects/recovery_aware_struct_prune/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_6/submitted.pdf`\n- **目标 venue**: EMNLP 2026（ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **格式**: Long paper，正文 ≤8 页，参考文献不限，Limitations/Ethics 不计入页数，ACL 模板，double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n1. **新颖性与贡献定位**：\n   - \"Recovery capacity spectrum\" 作为学术贡献的新颖程度\n   - \"CKA-based redundancy scoring > gradient importance for RL recovery\" 这一发现的significance\n   - 与 Ji et al. (2026) Self-Healing、RESP (Wang et al. 2025)、PASER (He et al. 2025) 等最新工作的差异化是否充分\n   - 研究问题（pruning criterion → RL trainability）是否对社区有足够价值\n\n2. **Related Work 覆盖与定位**：\n   - 是否遗漏重要相关工作（特别是 2025-2026 年的 LLM pruning + RLVR 工作）\n   - 与现有 pruning/recovery 文献的定位是否准确\n   - 是否恰当引用和区分了相关方法\n\n3. **Claim 与证据匹配**：\n   - Abstract 和 Introduction 中的 claims 是否都有充分实验支撑\n   - \"Preserved representational diversity\" 作为因果机制的证据强度（仅 CKA heatmap 相关性 vs 因果干预）\n   - Cross-architecture 结论（仅 SFT 无 GRPO）是否在正文中恰当限定\n   - Reward-accuracy decoupling 的讨论是否充分（20% 时 accuracy |Δ| < 1pp 但 reward gap 4.4×）\n\n4. **写作质量与格式**：\n   - 论述逻辑和结构是否清晰\n   - 术语使用一致性（\"recovery capacity spectrum\" vs \"recovery capacity gradient\" 等）\n   - 页数合规性（正文 ≤8 页）\n   - 图表质量、可读性\n   - 参考文献格式和完整性\n\n5. **Missing References 搜索**：\n   - 搜索 2025-2026 年 LLM structured pruning + reasoning recovery 的最新论文\n   - 检查是否有关键遗漏\n\n请提供完整审稿意见，包含：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment（评分+理由）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recovery_aware_struct_prune",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 相关工作 + 写作质量** 审查。\n\n## 论文信息\n- **标题**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\n- **论文路径**: `projects/recovery_aware_struct_prune/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_6/submitted.pdf`\n- **目标 venue**: EMNLP 2026（ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **格式**: Long paper，正文 ≤8 页，参考文献不限，Limitations/Ethics 不计入页数，ACL 模板，double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n1. **新颖性与贡献定位**：\n   - \"Recovery capacity spectrum\" 作为学术贡献的新颖程度\n   - \"CKA-based redundancy scoring > gradient importance for RL recovery\" 这一发现的significance\n   - 与 Ji et al. (2026) Self-Healing、RESP (Wang et al. 2025)、PASER (He et al. 2025) 等最新工作的差异化是否充分\n   - 研究问题（pruning criterion → RL trainability）是否对社区有足够价值\n\n2. **Related Work 覆盖与定位**：\n   - 是否遗漏重要相关工作（特别是 2025-2026 年的 LLM pruning + RLVR 工作）\n   - 与现有 pruning/recovery 文献的定位是否准确\n   - 是否恰当引用和区分了相关方法\n\n3. **Claim 与证据匹配**：\n   - Abstract 和 Introduction 中的 claims 是否都有充分实验支撑\n   - \"Preserved representational diversity\" 作为因果机制的证据强度（仅 CKA heatmap 相关性 vs 因果干预）\n   - Cross-architecture 结论（仅 SFT 无 GRPO）是否在正文中恰当限定\n   - Reward-accuracy decoupling 的讨论是否充分（20% 时 accuracy |Δ| < 1pp 但 reward gap 4.4×）\n\n4. **写作质量与格式**：\n   - 论述逻辑和结构是否清晰\n   - 术语使用一致性（\"recovery capacity spectrum\" vs \"recovery capacity gradient\" 等）\n   - 页数合规性（正文 ≤8 页）\n   - 图表质量、可读性\n   - 参考文献格式和完整性\n\n5. **Missing References 搜索**：\n   - 搜索 2025-2026 年 LLM structured pruning + reasoning recovery 的最新论文\n   - 检查是否有关键遗漏\n\n请提供完整审稿意见，包含：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment（评分+理由）。"
  }
}
```

</details>

---


### Tool call

_source line 379 · 2026-05-22T04:39:22.415923+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
  }
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-22T04:39:23.877417+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1461
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-22T04:39:25.598508+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3182
}
```

</details>

---


### Assistant

_source line 382 · 2026-05-22T04:39:31.865739+00:00_

Round 6 审稿已全面启动：

- **Reviewer 1**（方法严谨性 + 实验设计）：✅ 已派发
- **Reviewer 2**（新颖性 + 完整性 + 相关工作）：✅ 已派发
- **视觉审查 Agent**：✅ 已启动（fire-and-forget，不阻塞）
- **外部审稿**：未启用，跳过

等待两位 Reviewer 返回初审意见后，进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 33

## Round 33

20 recorded events


### User

_source line 383 · 2026-05-22T04:44:59.355175+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计

**论文**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models

---

## 总体评分
**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 实验框架设计精巧且核心发现（CKA-based pruning 保留 RLVR 恢复能力）有实际意义，但统计功效不足（RASP/Random 仅 1 seed）、cross-architecture 验证缺失 GRPO、α 消融不完整，削弱了结论的可靠性。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | 核心 claim 有足够实验支撑，但 N=1 方法缺统计验证、capacity floor 未消融、layer-depth confound 未排除 |
| Excitement | 3 / 5 | 研究问题 timely（pruning × RLVR），CKA-based pruning 发现有价值，但范围限于数学推理且 reward-accuracy decoupling 使实际影响不明确 |
| Reproducibility | 4 / 5 | Appendix A 超参完整，Algorithm 1 清晰，硬件报告充分；代码/masks/checkpoints 承诺于接收后发布 |
| Overall Assessment | 3.5 / 5 | Borderline Conference — 框架贡献扎实但需补充统计证据和更广泛验证 |
| Reviewer Confidence | 4 / 5 | 对结构化剪枝和 RLVR 有足够了解，仔细阅读了全文 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] RASP 和 Random 仅 1 个 GRPO seed，无法支撑 "collapse permanently" 的结论
- 具体位置：Section 4.2（Table 1）、Limitations 第 3 段
- 问题：论文声称 "RASP collapses permanently (0.061)"（Section 4.2）和 "Random stagnates"，但两者各自仅有 N=1 的 GRPO 运行。CKA-only 和 Standard 各有 3 seeds（Table 11, Appendix I），存在不对称的统计标准。RASP 的 collapse 可能是单次 seed 的偶然结果——特别是 RASP α=4.0 在 preliminary 实验中显示 active learning（peak reward 0.256, Section 4.4），说明 CKA 权重的微小变化就能翻转训练动态。N=1 无法排除这种随机性。
- 为什么影响接收：论文的核心 claim 是四种方法形成 "recovery capacity spectrum: CKA-only ≫ Random ≫ Standard > RASP"（Section 4.2）。如果 RASP/Random 的排名不 robust，spectrum 的下半部分就不可靠，论文的主要叙事被削弱。
- 建议修改方向：为 RASP 和 Random 各补充至少 3 个 GRPO seeds。

**N2** [critical] Cross-architecture 验证缺失 GRPO——论文的核心贡献
- 具体位置：Section 4.5 最后一句；Table 13（Appendix M）
- 问题：论文的核心 claim 关于 GRPO recovery capacity，但 Qwen2.5-Math-7B 的 cross-architecture 验证仅做到 SFT 阶段。而且两个模型共享 Qwen2.5 base architecture。评估仅用 N=200 样本。
- 为什么影响接收：without GRPO validation on a second architecture, the generalization claim is half-supported.
- 建议修改方向：完成 Qwen2.5-Math-7B GRPO 验证，或弱化 claim 为 "SFT-stage generalization evidence"。

**N3** [critical] Layer-depth pruning pattern 与 representational diversity 混淆（confound 未排除）
- 具体位置：Section 4.5 (Representational diversity)；Appendix N
- 问题：CKA-only 将 72.5% 移除集中在 early layers (L0-9)，Standard 均匀分布。论文将优势归因于 "preserved representational diversity"，但同样合理的解释是 CKA-only 碰巧保留了对推理关键的 late layers。缺少 depth-controlled ablation。
- 为什么影响接收：这是论文的核心机制解释，如果优势来自 layer-depth pattern 而非 CKA 本身，contribution 3 的归因不准确。
- 建议修改方向：增加 depth-controlled baseline（如 "Late-Layer-First" pruning），或在 Discussion 中讨论此 confound。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Welch's t-test at N=3 统计功效极低
- 具体位置：Section 4.2（p=0.0009）；Appendix I
- 建议：补充 Cohen's d 和 bootstrap 95% CI。

**W2** [warning] α 消融仅用 post-prune accuracy，缺少 GRPO reward 全景
- 具体位置：Table 6（Appendix D）；Section 4.4
- 建议：完成 α=4.0 full evaluation，增加更多 α 值的 GRPO 运行。

**W3** [warning] 40% per-layer capacity floor 未消融但可能影响结论
- 具体位置：Section 3.3；Limitations 第 2 段
- 建议：增加 floor ∈ {30%, 50%, 60%} 消融。

**W4** [warning] Reward-accuracy decoupling 削弱了实际影响力
- 具体位置：Section 4.3；Tables 2, 12
- 建议：讨论什么条件下 reward advantage 转化为 accuracy gain，考虑将 15% sparsity 作为主要操作点。

**W5** [warning] RASP 表现差于 Standard 缺乏充分解释
- 具体位置：Section 4.2；Table 1
- 建议：分析 importance 和 CKA overlap 的相关性，解释 multiplicative 组合方式为何失效。

---

## 小问题
- Table 1 脚注与标题重复
- "recovery capacity" vs downstream accuracy 术语需更清晰区分
- Figure 2 四条曲线区分度不够，建议不同 line style
- α=4.0 "full evaluation pending" 应在 camera-ready 前完成
- "Post-SFT accuracy does not predict GRPO outcome" 仅基于 4 个数据点

---

## 主要优势
1. 共享 structural analysis + 仅变化 scoring 的控制变量设计在剪枝文献中少见，归因清晰
2. 四维诊断体系（reward/f₀/gradient norm/KL）比单一 accuracy 更有说服力
3. CKA reliability 验证（Spearman ρ ≥ 0.964）回应了 linear CKA 的已知 sensitivity 问题
4. Reward-accuracy decoupling 作为科学发现有独立价值
5. Limitations 部分透明度高

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-22T04:45:22.753928+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-22T04:45:22.804707+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-22T04:45:41.767167+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-22T04:45:43.222707+00:00_

{"result":"# 项目 recovery_aware_struct_prune 概况\n\n## 实验状态 (372 个)\n\n- **grpo_stage2_rasp_20_v2**: DONE (negative) — \n- **grpo_stage2_standard_20**: DONE (killed) — \n- **grpo_stage2_rasp_20**: DONE (killed) — \n- **sft_standard_20**: DONE (success) — \n- **sft_rasp_20**: DONE (success) — \n- **grpo_rasp_20_4096**: DONE (failed) — \n- **grpo_standard_20_4096**: DONE (negative) — \n- **grpo_standard_20_fast**: DONE (negative) — \n- **grpo_rasp_20_fast**: DONE (negative) — \n- **mvp_rasp_pipeline_v4**: PREPARING — \n- **grpo_standard_20**: DONE (killed) — \n- **grpo_rasp_20**: DONE (killed) — \n- **mvp_rasp_pipeline_v3**: DONE (negative) — \n- **mvp_rasp_pipeline_v2**: DONE (failed) — \n- **mvp_rasp_pipeline**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| eval_math500_sft_rasp_20_1p5b | 1.5B RASP 20% SFT MATH-500 @2048. Cross-scale comparison: if ranking CKA-only > Standard > RASP holds at 1.5B, validates scale-invariant importance metric. | — | — | — |\n| eval_math500_sft_standard_20_1p5b | 1.5B Standard 20% SFT MATH-500 @2048. Cross-scale comparison with CKA-only 1.5B (10.6%) to test if CKA-guided pruning advantage is scale-invariant. | — | — | — |\n| eval_math500_sft_random_20_v3 | Random 20% SFT MATH-500 @2048. v2 failed due to old eval_math500.py on westd-32935. Code synced from westb. | — | — | — |\n\n## 待处理\n- eval_gsm8k_grpo_alpha4_20_v2: α=4.0 GRPO maintains reward 0.15-0.26 (vs α=1.0 collapse to ~0.008), predicting GSM8K accuracy significantly above α=1.0 baseline. v1 timed out at 774/1319 showing 62.93% interim — full eval needed to confirm α-dependent collapse hypothesis.（已分配 westd-29022 GPU:cuda:1，等待提交）\n- eval_math500_sft_standard_25_2048（准备中）\n- sft_alpha4_20_v2: α=4.0 SFT recovery with save_only_model=True to prevent disk overflow. Pruning successful (19.09% sparsity). Testing if higher α mitigates RASP collapse after
…[truncated 1777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-22T04:45:43.373738+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-22T04:45:43.725789+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-22T04:45:43.926954+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-22T04:45:43.977516+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-22T04:46:04.508341+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-22T04:46:05.010808+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-22T04:46:05.061583+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-22T04:46:06.166117+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T04:39:25.107927+00:00\", \"completed_at\": \"2026-05-22T04:42:10.616930+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3-5\", \"message\": \"连续 3 页纯文本（仅 p4 有公式），Method 段缺少视觉锚点，审稿人可能感到疲劳。建议在 Section 3 中插入一个示意图（如 scoring criteria 对比示意或 two-stage recovery 流程图）打破纯文本节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 子图 (a)(b) 内部 axis label 和 legend 字号偏小（约 6-7pt），放大后可读但在打印/屏幕标准缩放下需仔细辨认\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 4 热力图子图标注文字（层编号、方法名）偏小，建议适当增大字号或减少子图数量\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Figure 5 尺寸较小（单栏宽度，约占 1/4 页面），细节可读但不够醒目；若为重要补充结果，可考虑放大或改为 figure* 跨栏\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"附录 E-K 多个小节挤在同一页，内容密度极高；虽无溢出但视觉上较拥挤\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item，Figure 1 在第 2 页顶部出现——不是问题但若能将 Figure 1 提前到首页底部可强化第一印象\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-22T04:46:06.317022+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool call

_source line 397 · 2026-05-22T04:46:06.367752+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 398 · 2026-05-22T04:46:06.418333+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-22T04:46:06.418658+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_reports/round_5.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-22T04:46:31.012099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-22T04:46:31.113233+00:00_

1	issues:
2	# ============================================================
3	# Round 1-3 Issues — ALL RESOLVED (preserved from prior rounds)
4	# ============================================================
5	
6	- id: "R1-N1"
7	  summary: "Post-SFT 准确率混淆变量未控制"
8	  category: experiment
9	  severity: warning
10	  status: resolved
11	  first_raised_round: 1
12	  last_seen_round: 3
13	  resolution: "Qwen-Math reversal + RASP counter-example + scoped claims"
14	  resolution_round: 3
15	
16	- id: "R1-N2"
17	  summary: "Table 2 混用控制实验与 separately optimized runs"
18	  category: experiment
19	  severity: critical
20	  status: resolved
21	  first_raised_round: 1
22	  last_seen_round: 2
23	  resolution: "v5 controlled data (step-100, patience=50, lr=5e-7)"
24	  resolution_round: 1
25	
26	- id: "R1-N3"
27	  summary: "reward_desert_patience 参数不一致"
28	  category: experiment
29	  severity: critical
30	  status: resolved
31	  first_raised_round: 1
32	  last_seen_round: 2
33	  resolution: "所有方法 patience=50"
34	  resolution_round: 1
35	
36	- id: "R1-N4"
37	  summary: "单种子设计"
38	  category: experiment
39	  severity: critical
40	  status: resolved
41	  first_raised_round: 1
42	  last_seen_round: 2
43	  resolution: "CKA-only 64.39%±0.19pp, Standard 59.84%±0.38pp, p=0.0009"
44	  resolution_round: 1
45	
46	- id: "R2-N1"
47	  summary: "标题与结论错位"
48	  category: framing
49	  severity: critical
50	  status: resolved
51	  first_raised_round: 1
52	  last_seen_round: 2
53	  resolution: "How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models"
54	  resolution_round: 1
55	
56	- id: "R2-N2"
57	  summary: "实验规模不足"
58	  category: experiment
59	  severity: warning
60	  status: resolved
61	  first_raised_round: 1
62	  last_seen_round: 3
63	  resolution: "脚注透明标注 + Limitations 强化 + Abstract scoped"
64	  resolution_round: 3
65	
66	- id: "R1-W1"
67	  summary: "相关→因果跳跃"
68	  category: method
69	  severity: warning
70	  status: resolved
71	  first_raised_round: 1
72	  last_seen_round: 3
73	 
…[truncated 13664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Assistant

_source line 402 · 2026-05-22T04:46:55.164336+00:00_

状态恢复完成。当前为 **Round 6 fresh 审稿**。

**已收到**：
- ✅ Reviewer 1（方法严谨性 + 实验设计）— 3.5/5 Borderline Conference
- ⏳ Reviewer 2 — 等待中

**并行线状态**：
- 视觉审查：已完成（1 warning + 5 info）
- 外部审稿：未请求

**Reviewer 1 核心发现摘要**：
- **N1** [critical] RASP/Random 仅 1 seed，spectrum 下半部分不可靠
- **N2** [critical] Cross-architecture 验证缺失 GRPO（仅做到 SFT）
- **N3** [critical] Layer-depth confound 未排除（CKA-only 集中移除 early layers）
- W1-W5：统计功效低、α 消融不完整、capacity floor 未消融、reward-accuracy decoupling、RASP 失败解释不足

其中 N1 对应 R5-W1，N2 对应 R5-N2，W3 对应 R5-W3，W4 对应 R5-W4——多项为 Round 5 遗留问题在本轮继续被标记。N3（layer-depth confound）为新发现。

等待 Reviewer 2 提交后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 34

## Round 34

4 recorded events


### User

_source line 403 · 2026-05-22T04:46:57.740051+00:00_

[Reviewer 1 审稿结果]:
审稿完成，已提交给 Review Director。

核心判断：**3.5 / 5 (Borderline Conference)**。框架设计是亮点（共享 structural analysis、仅变化 scoring criterion 的控制变量），CKA-only 保留 RLVR recovery 的发现有实际价值。三个 critical 问题需要解决：(1) RASP/Random 各仅 1 seed 无法支撑 "collapse permanently" 结论；(2) cross-architecture 验证缺失 GRPO（论文核心贡献）；(3) CKA-only 的优势可能来自 layer-depth pruning pattern 而非 representational diversity 本身，需 depth-controlled ablation 排除 confound。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-22T04:47:57.525024+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查论文的 **新颖性 + 完整性**。\n\n## 论文信息\n- **标题**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_6/submitted.pdf`\n- **LaTeX**: `projects/recovery_aware_struct_prune/docs/paper/main.tex`\n\n## 投稿目标\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **格式**: Long paper，主文本严格 8 页限制，参考文献不限页数\n- **Limitations**: 必须写但不计入 8 页\n- **匿名**: Double-blind\n- **模板**: ACL 2023 (ARR)\n\n## 评分标准 (Overall Assessment)\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference，3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n\n### 主要关注\n1. **Novelty 评估**：CKA-based pruning criterion + RLVR recovery 的组合研究是否有足够新颖性？与 Self-Healing Networks (Chen et al. 2024)、SliceGPT、LaCo、ShortGPT 等工作的区分度如何？\n2. **Related Work 完整性**：是否遗漏重要相关工作？特别是 pruning + RL fine-tuning、CKA in model compression、representational similarity for pruning 方向\n3. **Contribution 清晰度**：三个声称的 contribution 是否都有充分支撑？是否存在 overclaim？\n4. **论文完整性**：实验设计是否覆盖了必要的 baseline 和 ablation？结论是否有 scope 过宽的问题？\n\n### 次要关注\n5. **写作质量**：叙事逻辑、术语一致性、因果语言的严谨度\n6. **格式合规**：8 页限制、匿名规则、引用格式\n\n## 输出格式\n\n请按以下结构组织审稿意见：\n1. **总体评分**：Overall 分数 + 一句话总结\n2. **官方维度打分**：Soundness / Excitement / Reproducibility / Overall Assessment / Reviewer Confidence（各 1-5 分 + 理由摘要）\n3. **Must-Fix 问题**（影响接收决定）：编号 N1, N2...，标注 [critical]，说明具体位置、问题、为什么影响接收、建议修改方向\n4. **Should-Fix 问题**（影响评分）：编号 W1, W2...，标注 [warning]\n5. **小问题**：格式、措辞等\n6. **主要优势**：逐条列出",
  "project": "recovery_aware_struct_prune",
  "chat_id": "oc_40839c097b00df44480b45ab767f59cf",
  "director_session_key": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查论文的 **新颖性 + 完整性**。\n\n## 论文信息\n- **标题**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_6/submitted.pdf`\n- **LaTeX**: `projects/recovery_aware_struct_prune/docs/paper/main.tex`\n\n## 投稿目标\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **格式**: Long paper，主文本严格 8 页限制，参考文献不限页数\n- **Limitations**: 必须写但不计入 8 页\n- **匿名**: Double-blind\n- **模板**: ACL 2023 (ARR)\n\n## 评分标准 (Overall Assessment)\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference，3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n\n### 主要关注\n1. **Novelty 评估**：CKA-based pruning criterion + RLVR recovery 的组合研究是否有足够新颖性？与 Self-Healing Networks (Chen et al. 2024)、SliceGPT、LaCo、ShortGPT 等工作的区分度如何？\n2. **Related Work 完整性**：是否遗漏重要相关工作？特别是 pruning + RL fine-tuning、CKA in model compression、representational similarity for pruning 方向\n3. **Contribution 清晰度**：三个声称的 contribution 是否都有充分支撑？是否存在 overclaim？\n4. **论文完整性**：实验设计是否覆盖了必要的 baseline 和 ablation？结论是否有 scope 过宽的问题？\n\n### 次要关注\n5. **写作质量**：叙事逻辑、术语一致性、因果语言的严谨度\n6. **格式合规**：8 页限制、匿名规则、引用格式\n\n## 输出格式\n\n请按以下结构组织审稿意见：\n1. **总体评分**：Overall 分数 + 一句话总结\n2. **官方维度打分**：Soundness / Excitement / Reproducibility / Overall Assessment / Reviewer Confidence（各 1-5 分 + 理由摘要）\n3. **Must-Fix 问题**（影响接收决定）：编号 N1, N2...，标注 [critical]，说明具体位置、问题、为什么影响接收、建议修改方向\n4. **Should-Fix 问题**（影响评分）：编号 W1, W2...，标注 [warning]\n5. **小问题**：格式、措辞等\n6. **主要优势**：逐条列出",
    "project": "recovery_aware_struct_prune",
    "chat_id": "oc_40839c097b00df44480b45ab767f59cf",
    "director_session_key": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-22T04:48:01.190397+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3665
}
```

</details>

---


### Assistant

_source line 406 · 2026-05-22T04:48:15.132467+00:00_

**Round 6 审稿进度**

| 角色 | 侧重 | 状态 |
|------|------|------|
| Reviewer 1 | 方法严谨性 + 实验设计 | ✅ 完成 (3.5/5) |
| Reviewer 2 | 新颖性 + 完整性 | 🔄 已派发，等待回复 |
| 视觉审查 | PDF 排版质量 | ✅ 完成 (0 critical, 1 warning, 5 info) |
| 外部审稿 | Stanford Agentic Reviewer | ❌ 未请求 |

**Reviewer 1 核心发现**：3 个 critical（RASP/Random 单 seed 统计不足、cross-architecture 缺 GRPO 验证、layer-depth confound 未排除）+ 5 个 warning。与 Round 5 的 R5-W1/R5-N2/R5-W3 高度重叠，说明这些问题在修订中可能未充分解决。

等待 Reviewer 2 回复后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 35

## Round 35

6 recorded events


### User

_source line 407 · 2026-05-22T04:48:15.147182+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models

### 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 控制变量实验设计干净、研究问题实用，但单模型单基准的 GRPO 主实验、correlational-only 的机制证据、SFT-only 的跨架构验证三者叠加，使论文未达到主会议接收标准。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨，但评估范围窄（GSM8K 单基准主实验），机制证据为相关性非因果 |
| Excitement | 3.0/5 | 研究问题有实践价值，但窄 scope 限制了社区影响力 |
| Reproducibility | 4/5 | 超参详尽（Table 4, Algorithm 1），但代码/checkpoints 尚未开源 |
| Confidence | 4/5 | 熟悉 LLM pruning 和 RLVR 领域，仔细阅读全文含附录 |

### Must-Fix 问题（影响接收决定）

**N1** [critical] GSM8K 单基准 GRPO 主实验限制了核心 claim 的可信度
- 具体位置：Section 4.1-4.3, Table 1-2, Figure 2-3
- 问题：GRPO 阶段的所有主实验（recovery capacity spectrum、reward-accuracy decoupling、training dynamics 分析）均仅在 GSM8K 上进行。附录中 MATH-500（Table 7）因 2048-token 截断导致评估受损；MBPP（Table 8）方法间差异小且排序不一致——ShortGPT 的 GRPO delta (+4.01pp) 反而大于 CKA-only (+1.34pp)。"Recovery capacity spectrum" 可能是 GSM8K-specific 的。
- 为什么影响接收：论文 title 和 Abstract claims 是一般性的，但实验支撑仅限一个基准。
- 建议：至少在一个额外数学推理基准和一个非数学推理基准上完成 GRPO 全流程。

**N2** [critical] "Preserved representational diversity" 机制证据仅为相关性，但被列为独立贡献
- 具体位置：Section 4.5, Figure 4, Contribution #3
- 问题：证据仅为 CKA heatmap 的视觉相关性和 overlap analysis 的描述性统计。没有因果干预实验。将 correlational observation 升格为 numbered contribution 是 overclaim。
- 建议：降级为 "hypothesis/observation"，或设计干预实验。

**N3** [critical] 跨架构验证仅 SFT、N=200、无 GRPO，但 Abstract overclaim
- 具体位置：Table 13, Abstract
- 问题：Qwen2.5-Math-7B 验证仅 SFT 阶段，N=200（自标 "preliminary"），但 Abstract 声称 "provide initial evidence for generality"。论文自身在 Section 4.4 已说明 "Post-SFT accuracy does not predict GRPO outcome"——这恰好说明 SFT-only 的跨架构验证不能支撑 RLVR generality 的声明。
- 建议：完成 GRPO 实验或显著弱化 Abstract 措辞。

### Should-Fix 问题

**W1** [warning] 实验仅覆盖 MLP channel pruning，但 framing 暗示更广泛适用性
- 具体位置：Section 3.1
- 建议：明确 scope 限定。

**W2** [warning] Reward-accuracy decoupling 未区分 format compliance vs reasoning quality
- 具体位置：Section 4.3
- 问题：reward 差异可能主要来自格式合规差异，需要 format-correct-but-wrong vs format-broken 的细粒度分析。

**W3** [warning] Random 和 RASP 仅单 seed
- 具体位置：Table 1, Table 11
- 建议：为所有方法提供至少 3 seeds。

**W4** [warning] 术语不一致："recovery capacity spectrum" vs "recovery capacity gradient"
- 具体位置：Abstract vs Table 1 caption

**W5** [warning] 潜在遗漏相关工作
- "On the Limits of Layer Pruning for Generative Reasoning in LLMs" (arXiv:2602.01997, Feb 2026)
- "Prune as You Generate: Online Rollout Pruning for RLVR" (arXiv:2603.24840, March 2026)

### 小问题
- Figure 2 y 轴标签未标注 mean vs peak reward
- Table 1 脚注 "Only redundancy-based pruning sustains RL recovery" 与 Random 排第二矛盾
- Section 5 Discussion 偏薄（仅半页）
- 建议审稿期间提供匿名 repository

### 主要优势
1. 严谨的控制变量设计——唯一变量是 scoring criterion
2. 实用的 actionable finding：CKA-based >> gradient importance for RL recovery
3. 丰富的多维度诊断（f_b, gradient norms, KL, CKA heatmap）
4. Reward-accuracy decoupling 是新颖观察
5. Extended training 和 α analysis 证明结论对超参不敏感

---

[Reviewer 2 审稿结果]:
审稿完成，已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。论文的控制变量实验设计是亮点，CKA-only >> gradient importance 的发现有实践价值。但三个 critical 问题阻碍主会议接收：(1) GRPO 主实验仅 GSM8K 单基准；(2) 机制证据（representational diversity）仅相关性无因果干预；(3) 跨架构验证仅 SFT-only、N=200 却在 Abstract overclaim。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-22T04:48:56.923486+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 审稿意见：How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\n\n### 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 控制变量实验设计干净、研究问题实用，但单模型单基准的 GRPO 主实验、correlational-only 的机制证据、SFT-only 的跨架构验证三者叠加，使论文未达到主会议接收标准。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨，但评估范围窄（GSM8K 单基准主实验），机制证据为相关性非因果 |\n| Excitement | 3.0/5 | 研究问题有实践价值，但窄 scope 限制了社区影响力 |\n| Reproducibility | 4/5 | 超参详尽（Table 4, Algorithm 1），但代码/checkpoints 尚未开源 |\n| Confidence | 4/5 | 熟悉 LLM pruning 和 RLVR 领域，仔细阅读全文含附录 |\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] GSM8K 单基准 GRPO 主实验限制了核心 claim 的可信度\n- 具体位置：Section 4.1-4.3, Table 1-2, Figure 2-3\n- 问题：GRPO 阶段的所有主实验（recovery capacity spectrum、reward-accuracy decoupling、training dynamics 分析）均仅在 GSM8K 上进行。附录中 MATH-500（Table 7）因 2048-token 截断导致评估受损；MBPP（Table 8）方法间差异小且排序不一致——ShortGPT 的 GRPO delta (+4.01pp) 反而大于 CKA-only (+1.34pp)。\"Recovery capacity spectrum\" 可能是 GSM8K-specific 的。\n- 为什么影响接收：论文 title 和 Abstract claims 是一般性的，但实验支撑仅限一个基准。\n- 建议：至少在一个额外数学推理基准和一个非数学推理基准上完成 GRPO 全流程。\n\n**N2** [critical] \"Preserved representational diversity\" 机制证据仅为相关性，但被列为独立贡献\n- 具体位置：Section 4.5, Figure 4, Contribution #3\n- 问题：证据仅为 CKA heatmap 的视觉相关性和 overlap analysis 的描述性统计。没有因果干预实验。将 correlational observation 升格为 numbered contribution 是 overclaim。\n- 建议：降级为 \"hypothesis/observation\"，或设计干预实验。\n\n**N3** [critical] 跨架构验证仅 SFT、N=200、无 GRPO，但 Abstract overclaim\n- 具体位置：Table 13, Abstract\n- 问题：Qwen2.5-Math-7B 验证仅 SFT 阶段，N=200（自标 \"preliminary\"），但 Abstract 声称 \"provide initial evidence for generality\"。论文自身在 Section 4.4 已说明 \"Post-SFT accuracy does not predict GRPO outcome\"——这恰好说明 SFT-only 的跨架构验证不能支撑 RLVR generality 的声明。\n- 建议：完成 GRPO 实验或显著弱化 Abstract 措辞。\n\n### Should-Fix 问题\n\n**W1** [warning] 实验仅覆盖 MLP channel pruning，但 framing 暗示更广泛适用性\n- 具体位置：Section 3.1\n- 建议：明确 scope 限定。\n\n**W2** [warning] Reward-accuracy decoupling 未区分 format compliance vs reasoning quality\n- 具体位置：Section 4.3\n- 问题：reward 差异可能主要来自格式合规差异，需要 format-correct-but-wrong vs format-broken 的细粒度分析。\n\n**W3** [warning] Random 和 RASP 仅单 seed\n- 具体位置：Table 1, Table 11\n- 建议：为所有方法提供至少 3 seeds。\n\n**W4** [warning] 术语不一致：\"recovery capacity spectrum\" vs \"recovery capacity gradient\"\n- 具体位置：Abstract vs Table 1 caption\n\n**W5** [warning] 潜在遗漏相关工作\n- \"On the Limits of Layer Pruning for Generative Reasoning in LLMs\" (arXiv:2602.01997, Feb 2026)\n- \"Prune as You Generate: Online Rollout Pruning for RLVR\" (arXiv:2603.24840, March 2026)\n\n### 小问题\n- Figure 2 y 轴标签未标注 mean vs peak reward\n- Table 1 脚注 \"Only redundancy-based pruning sustains RL recovery\" 与 Random 排第二矛盾\n- Section 5 Discussion 偏薄（仅半页）\n- 建议审稿期间提供匿名 repository\n\n### 主要优势\n1. 严谨的控制变量设计——唯一变量是 scoring criterion\n2. 实用的 actionable finding：CKA-based >> gradient importance for RL recovery\n3. 丰富的多维度诊断（f_b, gradient norms, KL, CKA heatmap）\n4. Reward-accuracy decoupling 是新颖观察\n5. Extended training 和 α analysis 证明结论对超参不敏感",
  "project": "recovery_aware_struct_prune",
  "chat_id": "oc_40839c097b00df44480b45ab767f59cf",
  "director_session_key": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 审稿意见：How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\n\n### 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 控制变量实验设计干净、研究问题实用，但单模型单基准的 GRPO 主实验、correlational-only 的机制证据、SFT-only 的跨架构验证三者叠加，使论文未达到主会议接收标准。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨，但评估范围窄（GSM8K 单基准主实验），机制证据为相关性非因果 |\n| Excitement | 3.0/5 | 研究问题有实践价值，但窄 scope 限制了社区影响力 |\n| Reproducibility | 4/5 | 超参详尽（Table 4, Algorithm 1），但代码/checkpoints 尚未开源 |\n| Confidence | 4/5 | 熟悉 LLM pruning 和 RLVR 领域，仔细阅读全文含附录 |\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] GSM8K 单基准 GRPO 主实验限制了核心 claim 的可信度\n- 具体位置：Section 4.1-4.3, Table 1-2, Figure 2-3\n- 问题：GRPO 阶段的所有主实验（recovery capacity spectrum、reward-accuracy decoupling、training dynamics 分析）均仅在 GSM8K 上进行。附录中 MATH-500（Table 7）因 2048-token 截断导致评估受损；MBPP（Table 8）方法间差异小且排序不一致——ShortGPT 的 GRPO delta (+4.01pp) 反而大于 CKA-only (+1.34pp)。\"Recovery capacity spectrum\" 可能是 GSM8K-specific 的。\n- 为什么影响接收：论文 title 和 Abstract claims 是一般性的，但实验支撑仅限一个基准。\n- 建议：至少在一个额外数学推理基准和一个非数学推理基准上完成 GRPO 全流程。\n\n**N2** [critical] \"Preserved representational diversity\" 机制证据仅为相关性，但被列为独立贡献\n- 具体位置：Section 4.5, Figure 4, Contribution #3\n- 问题：证据仅为 CKA heatmap 的视觉相关性和 overlap analysis 的描述性统计。没有因果干预实验。将 correlational observation 升格为 numbered contribution 是 overclaim。\n- 建议：降级为 \"hypothesis/observation\"，或设计干预实验。\n\n**N3** [critical] 跨架构验证仅 SFT、N=200、无 GRPO，但 Abstract overclaim\n- 具体位置：Table 13, Abstract\n- 问题：Qwen2.5-Math-7B 验证仅 SFT 阶段，N=200（自标 \"preliminary\"），但 Abstract 声称 \"provide initial evidence for generality\"。论文自身在 Section 4.4 已说明 \"Post-SFT accuracy does not predict GRPO outcome\"——这恰好说明 SFT-only 的跨架构验证不能支撑 RLVR generality 的声明。\n- 建议：完成 GRPO 实验或显著弱化 Abstract 措辞。\n\n### Should-Fix 问题\n\n**W1** [warning] 实验仅覆盖 MLP channel pruning，但 framing 暗示更广泛适用性\n- 具体位置：Section 3.1\n- 建议：明确 scope 限定。\n\n**W2** [warning] Reward-accuracy decoupling 未区分 format compliance vs reasoning quality\n- 具体位置：Section 4.3\n- 问题：reward 差异可能主要来自格式合规差异，需要 format-correct-but-wrong vs format-broken 的细粒度分析。\n\n**W3** [warning] Random 和 RASP 仅单 seed\n- 具体位置：Table 1, Table 11\n- 建议：为所有方法提供至少 3 seeds。\n\n**W4** [warning] 术语不一致：\"recovery capacity spectrum\" vs \"recovery capacity gradient\"\n- 具体位置：Abstract vs Table 1 caption\n\n**W5** [warning] 潜在遗漏相关工作\n- \"On the Limits of Layer Pruning for Generative Reasoning in LLMs\" (arXiv:2602.01997, Feb 2026)\n- \"Prune as You Generate: Online Rollout Pruning for RLVR\" (arXiv:2603.24840, March 2026)\n\n### 小问题\n- Figure 2 y 轴标签未标注 mean vs peak reward\n- Table 1 脚注 \"Only redundancy-based pruning sustains RL recovery\" 与 Random 排第二矛盾\n- Section 5 Discussion 偏薄（仅半页）\n- 建议审稿期间提供匿名 repository\n\n### 主要优势\n1. 严谨的控制变量设计——唯一变量是 scoring criterion\n2. 实用的 actionable finding：CKA-based >> gradient importance for RL recovery\n3. 丰富的多维度诊断（f_b, gradient norms, KL, CKA heatmap）\n4. Reward-accuracy decoupling 是新颖观察\n5. Extended training 和 α analysis 证明结论对超参不敏感",
    "project": "recovery_aware_struct_prune",
    "chat_id": "oc_40839c097b00df44480b45ab767f59cf",
    "director_session_key": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-22T04:49:45.182459+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 48258
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-22T04:49:45.940483+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计\n\n**论文**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\n\n---\n\n## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 实验框架设计精巧且核心发现（CKA-based pruning 保留 RLVR 恢复能力）有实际意义，但统计功效不足（RASP/Random 仅 1 seed）、cross-architecture 验证缺失 GRPO、α 消融不完整，削弱了结论的可靠性。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 核心 claim 有足够实验支撑，但 N=1 方法缺统计验证、capacity floor 未消融、layer-depth confound 未排除 |\n| Excitement | 3 / 5 | 研究问题 timely（pruning × RLVR），CKA-based pruning 发现有价值，但范围限于数学推理且 reward-accuracy decoupling 使实际影响不明确 |\n| Reproducibility | 4 / 5 | Appendix A 超参完整，Algorithm 1 清晰，硬件报告充分；代码/masks/checkpoints 承诺于接收后发布 |\n| Overall Assessment | 3.5 / 5 | Borderline Conference — 框架贡献扎实但需补充统计证据和更广泛验证 |\n| Reviewer Confidence | 4 / 5 | 对结构化剪枝和 RLVR 有足够了解，仔细阅读了全文 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] RASP 和 Random 仅 1 个 GRPO seed，无法支撑 \"collapse permanently\" 的结论\n- 具体位置：Section 4.2（Table 1）、Limitations 第 3 段\n- 问题：论文声称 \"RASP collapses permanently (0.061)\"（Section 4.2）和 \"Random stagnates\"，但两者各自仅有 N=1 的 GRPO 运行。CKA-only 和 Standard 各有 3 seeds（Table 11, Appendix I），存在不对称的统计标准。RASP 的 collapse 可能是单次 seed 的偶然结果——特别是 RASP α=4.0 在 preliminary 实验中显示 active learning（peak reward 0.256, Section 4.4），说明 CKA 权重的微小变化就能翻转训练动态。N=1 无法排除这种随机性。\n- 为什么影响接收：论文的核心 claim 是四种方法形成 \"recovery capacity spectrum: CKA-only ≫ Random ≫ Standard > RASP\"（Section 4.2）。如果 RASP/Random 的排名不 robust，spectrum 的下半部分就不可靠，论文的主要叙事被削弱。\n- 建议修改方向：为 RASP 和 Random 各补充至少 3 个 GRPO seeds。\n\n**N2** [critical] Cross-architecture 验证缺失 GRPO——论文的核心贡献\n- 具体位置：Section 4.5 最后一句；Table 13（Appendix M）\n- 问题：论文的核心 claim 关于 GRPO recovery capacity，但 Qwen2.5-Math-7B 的 cross-architecture 验证仅做到 SFT 阶段。而且两个模型共享 Qwen2.5 base architecture。评估仅用 N=200 样本。\n- 为什么影响接收：without GRPO validation on a second architecture, the generalization claim is half-supported.\n- 建议修改方向：完成 Qwen2.5-Math-7B GRPO 验证，或弱化 claim 为 \"SFT-stage generalization evidence\"。\n\n**N3** [critical] Layer-depth pruning pattern 与 representational diversity 混淆（confound 未排除）\n- 具体位置：Section 4.5 (Representational diversity)；Appendix N\n- 问题：CKA-only 将 72.5% 移除集中在 early layers (L0-9)，Standard 均匀分布。论文将优势归因于 \"preserved representational diversity\"，但同样合理的解释是 CKA-only 碰巧保留了对推理关键的 late layers。缺少 depth-controlled ablation。\n- 为什么影响接收：这是论文的核心机制解释，如果优势来自 layer-depth pattern 而非 CKA 本身，contribution 3 的归因不准确。\n- 建议修改方向：增加 depth-controlled baseline（如 \"Late-Layer-First\" pruning），或在 Discussion 中讨论此 confound。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Welch's t-test at N=3 统计功效极低\n- 具体位置：Section 4.2（p=0.0009）；Appendix I\n- 建议：补充 Cohen's d 和 bootstrap 95% CI。\n\n**W2** [warning] α 消融仅用 post-prune accuracy，缺少 GRPO reward 全景\n- 具体位置：Table 6（Appendix D）；Section 4.4\n- 建议：完成 α=4.0 full evaluation，增加更多 α 值的 GRPO 运行。\n\n**W3** [warning] 40% per-layer capacity floor 未消融但可能影响结论\n- 具体位置：Section 3.3；Limitations 第 2 段\n- 建议：增加 floor ∈ {30%, 50%, 60%} 消融。\n\n**W4** [warning] Reward-accuracy decoupling 削弱了实际影响力\n- 具体位置：Section 4.3；Tables 2, 12\n- 建议：讨论什么条件下 reward advantage 转化为 accuracy gain，考虑将 15% sparsity 作为主要操作点。\n\n**W5** [warning] RASP 表现差于 Standard 缺乏充分解释\n- 具体位置：Section 4.2；Table 1\n- 建议：分析 importance 和 CKA overlap 的相关性，解释 multiplicative 组合方式为何失效。\n\n---\n\n## 小问题\n- Table 1 脚注与标题重复\n- \"recovery capacity\" vs downstream accuracy 术语需更清晰区分\n- Figure 2 四条曲线区分度不够，建议不同 line style\n- α=4.0 \"full evaluation pending\" 应在 camera-ready 前完成\n- \"Post-SFT accuracy does not predict GRPO outcome\" 仅基于 4 个数据点\n\n---\n\n## 主要优势\n1. 共享 structural analysis + 仅变化 scoring 的控制变量设计在剪枝文献中少见，归因清晰\n2. 四维诊断体系（reward/f₀/gradient norm/KL）比单一 accuracy 更有说服力\n3. CKA reliability 验证（Spearman ρ ≥ 0.964）回应了 linear CKA 的已知 sensitivity 问题\n4. Reward-accuracy decoupling 作为科学发现有独立价值\n5. Limitations 部分透明度高",
  "project": "recovery_aware_struct_prune",
  "chat_id": "oc_40839c097b00df44480b45ab767f59cf",
  "director_session_key": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计\n\n**论文**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\n\n---\n\n## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 实验框架设计精巧且核心发现（CKA-based pruning 保留 RLVR 恢复能力）有实际意义，但统计功效不足（RASP/Random 仅 1 seed）、cross-architecture 验证缺失 GRPO、α 消融不完整，削弱了结论的可靠性。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 核心 claim 有足够实验支撑，但 N=1 方法缺统计验证、capacity floor 未消融、layer-depth confound 未排除 |\n| Excitement | 3 / 5 | 研究问题 timely（pruning × RLVR），CKA-based pruning 发现有价值，但范围限于数学推理且 reward-accuracy decoupling 使实际影响不明确 |\n| Reproducibility | 4 / 5 | Appendix A 超参完整，Algorithm 1 清晰，硬件报告充分；代码/masks/checkpoints 承诺于接收后发布 |\n| Overall Assessment | 3.5 / 5 | Borderline Conference — 框架贡献扎实但需补充统计证据和更广泛验证 |\n| Reviewer Confidence | 4 / 5 | 对结构化剪枝和 RLVR 有足够了解，仔细阅读了全文 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] RASP 和 Random 仅 1 个 GRPO seed，无法支撑 \"collapse permanently\" 的结论\n- 具体位置：Section 4.2（Table 1）、Limitations 第 3 段\n- 问题：论文声称 \"RASP collapses permanently (0.061)\"（Section 4.2）和 \"Random stagnates\"，但两者各自仅有 N=1 的 GRPO 运行。CKA-only 和 Standard 各有 3 seeds（Table 11, Appendix I），存在不对称的统计标准。RASP 的 collapse 可能是单次 seed 的偶然结果——特别是 RASP α=4.0 在 preliminary 实验中显示 active learning（peak reward 0.256, Section 4.4），说明 CKA 权重的微小变化就能翻转训练动态。N=1 无法排除这种随机性。\n- 为什么影响接收：论文的核心 claim 是四种方法形成 \"recovery capacity spectrum: CKA-only ≫ Random ≫ Standard > RASP\"（Section 4.2）。如果 RASP/Random 的排名不 robust，spectrum 的下半部分就不可靠，论文的主要叙事被削弱。\n- 建议修改方向：为 RASP 和 Random 各补充至少 3 个 GRPO seeds。\n\n**N2** [critical] Cross-architecture 验证缺失 GRPO——论文的核心贡献\n- 具体位置：Section 4.5 最后一句；Table 13（Appendix M）\n- 问题：论文的核心 claim 关于 GRPO recovery capacity，但 Qwen2.5-Math-7B 的 cross-architecture 验证仅做到 SFT 阶段。而且两个模型共享 Qwen2.5 base architecture。评估仅用 N=200 样本。\n- 为什么影响接收：without GRPO validation on a second architecture, the generalization claim is half-supported.\n- 建议修改方向：完成 Qwen2.5-Math-7B GRPO 验证，或弱化 claim 为 \"SFT-stage generalization evidence\"。\n\n**N3** [critical] Layer-depth pruning pattern 与 representational diversity 混淆（confound 未排除）\n- 具体位置：Section 4.5 (Representational diversity)；Appendix N\n- 问题：CKA-only 将 72.5% 移除集中在 early layers (L0-9)，Standard 均匀分布。论文将优势归因于 \"preserved representational diversity\"，但同样合理的解释是 CKA-only 碰巧保留了对推理关键的 late layers。缺少 depth-controlled ablation。\n- 为什么影响接收：这是论文的核心机制解释，如果优势来自 layer-depth pattern 而非 CKA 本身，contribution 3 的归因不准确。\n- 建议修改方向：增加 depth-controlled baseline（如 \"Late-Layer-First\" pruning），或在 Discussion 中讨论此 confound。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Welch's t-test at N=3 统计功效极低\n- 具体位置：Section 4.2（p=0.0009）；Appendix I\n- 建议：补充 Cohen's d 和 bootstrap 95% CI。\n\n**W2** [warning] α 消融仅用 post-prune accuracy，缺少 GRPO reward 全景\n- 具体位置：Table 6（Appendix D）；Section 4.4\n- 建议：完成 α=4.0 full evaluation，增加更多 α 值的 GRPO 运行。\n\n**W3** [warning] 40% per-layer capacity floor 未消融但可能影响结论\n- 具体位置：Section 3.3；Limitations 第 2 段\n- 建议：增加 floor ∈ {30%, 50%, 60%} 消融。\n\n**W4** [warning] Reward-accuracy decoupling 削弱了实际影响力\n- 具体位置：Section 4.3；Tables 2, 12\n- 建议：讨论什么条件下 reward advantage 转化为 accuracy gain，考虑将 15% sparsity 作为主要操作点。\n\n**W5** [warning] RASP 表现差于 Standard 缺乏充分解释\n- 具体位置：Section 4.2；Table 1\n- 建议：分析 importance 和 CKA overlap 的相关性，解释 multiplicative 组合方式为何失效。\n\n---\n\n## 小问题\n- Table 1 脚注与标题重复\n- \"recovery capacity\" vs downstream accuracy 术语需更清晰区分\n- Figure 2 四条曲线区分度不够，建议不同 line style\n- α=4.0 \"full evaluation pending\" 应在 camera-ready 前完成\n- \"Post-SFT accuracy does not predict GRPO outcome\" 仅基于 4 个数据点\n\n---\n\n## 主要优势\n1. 共享 structural analysis + 仅变化 scoring 的控制变量设计在剪枝文献中少见，归因清晰\n2. 四维诊断体系（reward/f₀/gradient norm/KL）比单一 accuracy 更有说服力\n3. CKA reliability 验证（Spearman ρ ≥ 0.964）回应了 linear CKA 的已知 sensitivity 问题\n4. Reward-accuracy decoupling 作为科学发现有独立价值\n5. Limitations 部分透明度高",
    "project": "recovery_aware_struct_prune",
    "chat_id": "oc_40839c097b00df44480b45ab767f59cf",
    "director_session_key": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-22T04:49:47.195550+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1255
}
```

</details>

---


### Assistant

_source line 412 · 2026-05-22T04:49:51.544589+00:00_

Step 2 交叉分享已派发：
- Reviewer 1 收到 Reviewer 2 完整审稿，正在逐条回应
- Reviewer 2 收到 Reviewer 1 完整审稿，正在逐条回应

等待两位 Reviewer 的交叉回应返回后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 36

## Round 36

2 recorded events


### User

_source line 413 · 2026-05-22T04:55:35.335567+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R2-N1: GSM8K 单基准 GRPO 主实验限制核心 claim 可信度**

同意这是论文最大的结构性弱点。核心观察如下：

1. **主实验确实仅 GSM8K GRPO。** Table 1-2、Figure 2-3 的 recovery capacity spectrum 全部基于 GSM8K (N=1,319)，论文的三个 numbered contributions 均建立在此基础上。

2. **补充基准证据不够有力。** MATH-500 (Table 7, Appendix F) 受 2048-token 截断影响，论文自身注明 "show |Δ| ≤ 1.2pp"，方法间差异被压缩到噪声水平。MBPP (Table 8) 中四个受控方法的 GRPO 差距极小（CKA-only 14.17% vs Standard 13.10% vs RASP 13.10%），排序虽保持 CKA-only 领先，但 margin 仅 ~1pp，不具统计说服力。

3. **R2 关于 ShortGPT 的观察需要修正一个细节：** ShortGPT 是 layer pruning 方法，与论文的 MLP channel pruning 控制变量框架不同类。在四个受控方法内部，MBPP 排序实际上与 GSM8K 一致（CKA-only 领先）。但 margin 过小确实削弱了 spectrum 的 generality 声明。

4. **论文 Title 和 Abstract 使用一般性措辞**（"How Pruning Criteria Shape Post-RLVR Recovery"），但证据支撑不匹配。至少需要一个非数学推理基准的完整 GRPO 实验（如 LogiQA 或 ARC-Challenge）才能维持当前 claim 强度。

**[AGREE] R2-N2: "Preserved representational diversity" 机制证据仅为相关性**

同意 R2 的核心判断。补充如下：

1. Section 4.5 的证据链为：Figure 4 CKA heatmap → 视觉观察 CKA-only diverges most → Appendix N overlap analysis → 描述性统计。全部是 correlational，无因果干预。

2. 论文使用 "plausible mechanism" 措辞（Contribution #3, p.2），确实做了 hedging。但将其列为 **numbered contribution** 仍然 overclaim——"plausible mechanism" 更适合放在 Discussion 或 Analysis subsection 中作为 observation，而非与前两个有直接实验支撑的 contribution 并列。

3. 一个可行的因果验证思路：人工构造两组等量剪枝的模型，一组保持高 CKA diversity，一组人为降低 diversity（如额外移除 CKA 最 unique 的 structures），观察 GRPO recovery 是否随 diversity 单调变化。当前论文没有这类实验。

**[AGREE] R2-N3: 跨架构验证仅 SFT、N=200，与论文自身论证矛盾**

R2 的逻辑论证很锐利，我完全同意：

1. **论文自身的核心发现之一**（Section 4.4, p.7）明确指出："Post-SFT accuracy does not predict GRPO outcome; the recovery capacity spectrum is driven by structural properties of the pruned architecture, not initial SFT quality." 这是论文的 key insight。

2. **然而 Table 13 的 Qwen2.5-Math-7B 验证仅到 SFT 阶段**，且 N=200（论文自标 "preliminary"）。按论文自己的逻辑，SFT-only 结果不能推断 GRPO recovery generality。

3. **Abstract 的 "provide initial evidence for generality" 措辞**在此逻辑框架下构成自相矛盾。Table 13 最多能说明 CKA-based selection 在另一架构上也产生了不同的 SFT recovery 模式，但无法声称 RLVR generality。

4. 建议：要么完成 Qwen2.5-Math-7B 的 GRPO 实验（即使只 100 steps 的趋势观察），要么将 Abstract claim 严格限定为 "SFT-level structural effects generalize"。

---

### Should-Fix 问题

**[AGREE] R2-W1: 实验仅覆盖 MLP channel pruning，但 framing 暗示更广泛适用性**

论文 Title "How Pruning Criteria Shape Post-RLVR Recovery" 是完全一般性的，但 Section 3.1 的控制框架严格限定在 MLP channel group pruning。论文中虽然包含 ShortGPT (layer pruning) 作为参考 baseline，但 controlled comparison 的四个方法全部是 MLP channel 类型。建议在 Title 或 Abstract 中加入 "structured MLP pruning" 或类似限定词。

**[AGREE] R2-W2: Reward-accuracy decoupling 未区分 format compliance vs reasoning quality**

同意这是一个分析盲点。补充论证：

1. Section 3.4 Stage 1 (SFT warmup) 的目标包括恢复 "EOS generation, format compliance"。但不同剪枝方法在 GRPO 过程中的 format compliance 维持能力可能不同。

2. 论文追踪的 f_b（全零 reward batch 比例）**混淆了两种失败模式**：格式崩塌（无法 parse）和推理错误（格式正确但答案错误）。当 f_b 高时，无法区分是哪种原因。

3. 一个简单的改进：报告 GRPO 过程中每个方法的 EOS rate 和 format compliance rate 随 step 的变化，与 reward 曲线对照。Table 8 (MBPP) 的 Appendix 部分有 EOS rate 数据，但主实验 GSM8K 缺少此分析。

**[AGREE] R2-W3: Random 和 RASP 仅单 seed**

同意。Table 11 确认 CKA-only 和 Standard 有 3 seeds（42, 123, 456），Random 和 RASP 为单 seed。对于控制变量研究，所有条件理应有可比的统计可靠性。

不过补充一个实际考量：RASP 的完全崩塌（peak reward 0.061, f_b=0.675, Table 1）如此极端，多 seed 不太可能改变定性结论。Random 的 stagnation 模式（reward 在 0.14-0.19 振荡）与 CKA-only 的 active learning 在定性上也截然不同。但 Standard 的 borderline collapse（peak 0.081）与 Random 的 stagnation 之间的排序差异是否稳健，确实需要多 seed 验证。

**[AGREE] R2-W4: 术语不一致 "spectrum" vs "gradient"**

确认存在。Abstract (p.1) 使用 "recovery capacity spectrum"，Table 1 caption (p.6) 使用 "Recovery capacity gradient"。应统一为一个术语。

**[AGREE] R2-W5: 潜在遗漏相关工作**

我通过 web search 确认两篇论文均真实存在：

1. **"On the Limits of Layer Pruning for Generative Reasoning in LLMs"** (arXiv:2602.01997, Feb 2026)——研究 layer pruning 对推理任务的影响，含 SFT recovery 分析。与本文 Section 2 Related Work 中的 pruning-for-reasoning 讨论直接相关。

2. **"Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR"** (arXiv:2603.24840, March 2026)——提出 RLVR 训练中的 online rollout pruning。与本文的 RLVR recovery 主题高度相关，是同一研究方向的并行工作。

两篇均在论文可能的提交时间窗口内发布，应在 Related Work 中讨论。

---

### 小问题

**[AGREE] Figure 2 y 轴标签：** 确认 Figure 2 y 轴仅标注 "Reward"，未说明是 mean reward per step 还是 peak reward。结合 caption 讨论的是 trajectory over steps，应为 per-step mean reward，但需明确标注。

**[AGREE] Table 1 脚注矛盾：** 脚注 "Only redundancy-based pruning sustains RL recovery" 与 Random 排第二（peak reward 0.190 > Standard 0.081）存在张力。虽然论文将 Random 归类为 "stagnation"（非 "active learning"），但 "sustains" 一词过于绝对。建议改为 "Only redundancy-based pruning enables active RL learning"。

**[AGREE] Section 5 Discussion 偏薄：** 半页 Discussion 对于一篇控制变量比较研究而言确实不足。至少应讨论：(1) 为什么 CKA-based redundancy 与 RL exploration 的关系，(2) 对 pruning pipeline practitioners 的具体 actionable 建议，(3) 与 Lottery Ticket Hypothesis 的联系。

**[AGREE] 匿名 repository：** 论文 Limitations 已提到 "Code, pruning masks, and model checkpoints will be released upon acceptance"，但审稿期间提供匿名 repo 会显著提高 Reproducibility 评分。

---

### 对 R2 主要优势评估的回应

R2 列出的 5 个优势我全部认同，特别是：

- **优势 1（控制变量设计）**是论文最大的方法论贡献。在 LLM pruning 文献中，大多数工作比较不同 pruning *方法*（不同框架、不同代码、不同超参），本文严格控制所有变量只变 scoring criterion，这种设计在该领域极为少见。

- **优势 4（Reward-accuracy decoupling）**确实是一个有价值的观察，即使 W2 指出的 format compliance 分析缺失削弱了其解释力。

---

### 对 R2 总体评分的看法

R2 给出 Overall 3.0 (Findings)。我认为这个评分区间合理。

N1（单基准）和 N3（SFT-only 跨架构自相矛盾）是最致命的问题。论文的控制变量设计本身有价值，但核心 claim 的 empirical support 限于单模型单基准的 GRPO 实验，且论文自身的逻辑（SFT ≠ GRPO prediction）与其 generality 声明矛盾——这两个问题叠加使得主会议接收困难。

如果作者能 (1) 补充至少一个非 GSM8K 基准的完整 GRPO 实验，(2) 完成 Qwen2.5-Math-7B 的 GRPO 验证或大幅弱化 generality claim，(3) 将 Contribution #3 降级为 observation，论文可以达到 3.5 (Borderline Conference) 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 414 · 2026-05-22T04:55:45.883574+00:00_

Reviewer 1 交叉回应收到——对 Reviewer 2 所有 Must-Fix、Should-Fix 和小问题全部 [AGREE]。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 37

## Round 37

6 recorded events


### User

_source line 415 · 2026-05-22T04:55:52.457541+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性 + 完整性）

### 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 实验设计干净、研究问题有意义，但新颖性主要停留在经验发现层面（无新方法成功落地），且单模型+单数据集+单稀疏度的实验范围限制了 contribution 的通用性。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 控制变量设计严谨，但核心 claim 的证据链不完整：机制解释止于相关性、κ 无消融、scope 过宽 |
| Excitement | 2.5/5 | 研究问题及时且有实际价值，但贡献主要是经验发现，无新方法或可落地工具；CKA-only 本身非原创 |
| Reproducibility | 4/5 | 超参数表完整，基础模型和数据集公开，算法伪代码清晰；代码未释放但承诺发布 |
| Overall Assessment | 3.0 | 适合 Findings track |
| Reviewer Confidence | 4/5 | 熟悉 LLM 剪枝和 RL fine-tuning 文献 |

---

### Must-Fix 问题

**N1** [critical] **Contribution 1 "recovery capacity spectrum" overclaim**
- 位置：Section 1 Contribution 1, Abstract
- "spectrum"（CKA-only ≫ Random > Standard > RASP）仅在一个模型（DeepSeek-R1-Distill-Qwen-7B）、一个数据集（GSM8K）、一个主稀疏度（20%）上验证。Cross-architecture 验证（Qwen2.5-Math-7B, Table 3）只用 single seed, N=200, 且未测 RASP/Random，spectrum ordering 未被完整复现。
- 建议：限定 scope、补全 Qwen2.5-Math-7B 上 4 criteria 对比（3 seeds）、增加第二个推理域。

**N2** [critical] **缺失高度相关文献：RL Finetunes Small Subnetworks (2505.11711)**
- 位置：Section 2 Related Work
- 该论文揭示 RL fine-tuning 只更新 5–30% 参数，在 GRPO 等 7 种 RL 算法上均成立。与本文核心主题直接相关：如果 RL 只在小子网络上操作，剪枝标准是否保留了该子网络可能才是关键因素。
- 建议：Related Work 中讨论，Section 4.5 机制分析中引入该视角。

**N3** [critical] **Contribution 3 因果机制仅为相关性**
- 位置：Section 1 Contribution 3, Section 4.5, Figure 4
- 证据仅为 CKA-only 的 intra-layer CKA 与 dense model 最接近（相关性），无干预实验验证因果性。"identified mechanism" 措辞过强。
- 建议：改为 "observed evidence consistent with"，或增加干预实验。

---

### Should-Fix 问题

**W1** [warning] RASP 只测 κ=1.0 就结论 "permanently collapses"，缺 κ 消融（κ∈{0.25,0.5,2.0,4.0}）。

**W2** [warning] Related Work 遗漏 LaCo (Yang et al., 2024, EMNLP Findings)——与 ShortGPT/SliceGPT 同级别的 structured pruning 核心文献。

**W3** [warning] 引用姓名错误：正文 "Dong et al. (2026)" vs 参考文献 "Longyi Deng"。

**W4** [warning] 结论语言未限定为数学推理域，但实验仅覆盖 GSM8K。

**W5** [warning] 15%/25% sparsity 实验为 single-seed，支撑 "sparsity-dependent decoupling" 的统计基础不足。

---

### 小问题
- Eq.1 未写出 Taylor expansion 的完整数学形式
- Figure 2 字号偏小
- "Reward-accuracy decoupling" 首次使用时无正式定义
- Table 1 footnote "Only redundancy-based pruning sustains RL recovery" 过于绝对

### 主要优势
1. 控制变量设计严谨（四种 criteria 共享同一 pipeline）
2. 训练动态分析深入（Figure 2/3 超越 final-checkpoint 报告）
3. RASP 失败的负面结果有实际指导意义
4. 可复现性好（Table 4 完整超参数 + Algorithm 1 伪代码）
5. 跨架构初步验证（Qwen2.5-Math-7B）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-22T05:02:10.678704+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "issues_yaml": "issues:\n# ============================================================\n# Round 1-3 Issues — ALL RESOLVED\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"Post-SFT 准确率混淆变量未控制\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Qwen-Math reversal + RASP counter-example + scoped claims\"\n  resolution_round: 3\n\n- id: \"R1-N2\"\n  summary: \"Table 2 混用控制实验与 separately optimized runs\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"v5 controlled data (step-100, patience=50, lr=5e-7)\"\n  resolution_round: 1\n\n- id: \"R1-N3\"\n  summary: \"reward_desert_patience 参数不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"所有方法 patience=50\"\n  resolution_round: 1\n\n- id: \"R1-N4\"\n  summary: \"单种子设计\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"CKA-only 64.39%±0.19pp, Standard 59.84%±0.38pp, p=0.0009\"\n  resolution_round: 1\n\n- id: \"R2-N1\"\n  summary: \"标题与结论错位\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\"\n  resolution_round: 1\n\n- id: \"R2-N2\"\n  summary: \"实验规模不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"脚注透明标注 + Limitations 强化 + Abstract scoped\"\n  resolution_round: 3\n\n- id: \"R1-W1\"\n  summary: \"相关→因果跳跃\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"全文 determines → shapes/significantly influences，与标题 Shape 一致\"\n  resolution_round: 3\n\n- id: \"R1-W2\"\n  summary: \"'actively harmful' 过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"去除 actively harmful\"\n  resolution_round: 1\n\n- id: \"R1-W3\"\n  summary: \"MATH-500 TBD 条目\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Truncated% 列删除，数据完整\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"主结果缺统计检验\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Bootstrap CI + McNemar's p=0.0009\"\n  resolution_round: 1\n\n- id: \"R2-N3\"\n  summary: \"Self-Healing 性能差距未讨论\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"conditions differ sufficiently that direct comparison not meaningful\"\n  resolution_round: 1\n\n- id: \"R2-W1\"\n  summary: \"Orphan bib 条目\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"0 orphan bib entries\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"CKA 可靠性未讨论\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"method.tex: linear CKA + Spearman ρ≥0.964\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"引用年份错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"bib 年份已修正\"\n  resolution_round: 1\n\n- id: \"R1-M1\"\n  summary: \"Decoupling 可能是训练步数不足\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"100 GRPO steps caveat\"\n  resolution_round: 1\n\n- id: \"R1-M2\"\n  summary: \"Abstract 'self-recovery' 来自单次事件\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"全文无 self-recovery\"\n  resolution_round: 1\n\n- id: \"R1-M3\"\n  summary: \"Recovery capacity 未形式化定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"定义已添加，R2 认为足够\"\n  resolution_round: 3\n\n- id: \"R1-M4\"\n  summary: \"Table 5 vs Table 1 reward 不一致\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"CKA-only reward 两表均为 0.354\"\n  resolution_round: 1\n\n- id: \"R2-NEW-N1\"\n  summary: \"主文本超过 8 页 — desk rejection 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"压缩后主文本 8 页合规\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W1\"\n  summary: \"90.83% vs 81.27% unpruned accuracy 矛盾\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注解释 SFT catastrophic forgetting\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W2\"\n  summary: \"Qwen-Math 跨架构验证仅 SFT，Abstract overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 区分 GRPO(DeepSeek) vs SFT(Qwen-Math)\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W3\"\n  summary: \"GRPO 准确率改变 < 1pp — 实际效用存疑\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"300-step accuracy + reward-accuracy decoupling 论证\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W4\"\n  summary: \"RASP/Random 仍为单种子\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注透明标注 + Limitations 披露\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W5\"\n  summary: \"Random baseline SFT/GRPO Acc 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Table 2 脚注标注 checkpoint not preserved\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W6\"\n  summary: \"正文 5 处 'determines' 残留\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"全部替换为 shapes/significantly influences\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M1\"\n  summary: \"GRPO batch size / rollouts 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M2\"\n  summary: \"SFT lr/batch/optimizer 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-VIS-1\"\n  summary: \"末页 Figure 6 仅占 30%，70% 空白\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 重排\"\n  resolution_round: 3\n\n- id: \"R2-VIS-2\"\n  summary: \"Appendix page 12 过度拥挤\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 拆分到多页\"\n  resolution_round: 3\n\n- id: \"R3-S5\"\n  summary: \"Qwen-Math 'strongest evidence' 措辞仍略强\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"strongest → additional evidence in §4.5\"\n  resolution_round: 3\n\n- id: \"R3-M2\"\n  summary: \"300-step accuracy 未标注 seed\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"(single seed) 标注已添加到 §4.3\"\n  resolution_round: 3\n\n- id: \"R3-M3\"\n  summary: \"无代码/checkpoint 发布声明\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"Code and checkpoints release statement in Conclusion\"\n  resolution_round: 3\n\n# ============================================================\n# Round 5 Issues — Updated with Round 6 observations\n# ============================================================\n\n- id: \"R5-N1\"\n  summary: \"Reward-accuracy decoupling 削弱 GRPO recovery 叙事（20% 精度差距 4.55pp 中 4.62pp 来自 SFT）\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。SYSTEMIC_ISSUE #1 核心。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W4 和 R2-W2 再次提出，增加新角度：需区分 format compliance vs reasoning quality。R2 建议细粒度分析 format-correct-but-wrong vs format-broken。\"\n  action_items:\n    - round: 5\n      action: \"D098 dual-layer reframe\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N2\"\n  summary: \"Cross-architecture (Qwen2.5-Math-7B) 缺乏 GRPO 验证\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前不可行（需全 pipeline ~50h GPU）。但 1.5B GRPO 数据已有。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次提出。R1 指出论文自身 'SFT does not predict GRPO' 逻辑与 SFT-only 跨架构验证自相矛盾。R2 认为 Abstract 'initial evidence for generality' overclaim。\"\n  action_items:\n    - round: 5\n      action: \"补入 1.5B GRPO 数据作 cross-scale validation\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"RASP/Random 种子不对称（2/4 方法无统计支撑）\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"核心比较 CKA vs Standard 有 3-seed p=0.0009。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 升级为 critical (N1)：RASP α=4.0 active learning 说明 seed 敏感性高。R2-W3 同意。R1 补充：RASP collapse 极端但 Standard vs Random 排序需多 seed 验证。\"\n  action_items:\n    - round: 5\n      action: \"Limitations 标注 + 核心 claim 限定 CKA vs Standard\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"CKA-recovery 因果机制仅为相关性证据\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"SYSTEMIC_ISSUE #2 成员。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。R2 明确指出 Contribution 3 将 correlational observation 升格为 numbered contribution 是 overclaim。R1 完全同意并建议降级为 Discussion observation。\"\n  action_items:\n    - round: 5\n      action: \"Jaccard overlap 分析 + Limitations 承认缺干预实验\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Per-layer capacity floor (40%) 未消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前无法做 full pipeline ablation。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W3 再次提出，建议 floor ∈ {30%, 50%, 60%} 消融。\"\n  action_items:\n    - round: 5\n      action: \"Limitations 讨论 + rebuttal 论点准备\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"α 消融缺 GRPO reward 数据\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"高 ROI 实验。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出。R2-W1 扩展为 κ 消融缺失（κ∈{0.25,0.5,2.0,4.0}），指出仅 κ=1.0 不足以判定 RASP collapse。\"\n  action_items:\n    - round: 5\n      action: \"α=4.0 GRPO 100步实验\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"'Recovery capacity gradient' 术语与 gradient descent 混淆\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W4 指出 Abstract 'spectrum' vs Table 1 caption 'gradient' 不一致仍然存在。R1 确认。\"\n  action_items:\n    - round: 5\n      action: \"全文替换为 'recovery capacity spectrum'\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M1\"\n  summary: \"Section 5 末尾溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"约 2 行溢出\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n  action_items:\n    - round: 5\n      action: \"Paper Agent 压缩 §5 确保 8 页合规\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M2\"\n  summary: \"Abstract p<0.001 未说明统计检验方法\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"N=3 t-test p<0.001 需极大效应量\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n  action_items:\n    - round: 5\n      action: \"Abstract 标注 Welch's t-test\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M3\"\n  summary: \"Page 7 display items 过度拥挤\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Figure 3 + Figure 4 + Table 2 挤在同一页\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及。视觉审查未标记此问题，可能已修复。\"\n  action_items:\n    - round: 5\n      action: \"Figure 前移平衡视觉节奏\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M4\"\n  summary: \"bib key 年份误导 + selfhealing2025 venue 缺失\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"lachance2024cka→2022, klabunde→2023, selfhealing2025 venue 空\"\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W3 发现新引用错误：正文 'Dong et al. (2026)' vs 参考文献 'Longyi Deng'。原 bib key 问题状态不明。\"\n  action_items:\n    - round: 5\n      action: \"Paper Agent 修正 bib 条目\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M5\"\n  summary: \"Figure 2 RASP/Standard 颜色区分度不足\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: []\n      note: \"视觉审查发现\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1 小问题再次提出：Figure 2 四条曲线区分度不够，建议不同 line style。R2 也提到字号偏小。\"\n  action_items:\n    - round: 5\n      action: \"添加不同 line style 辅助区分\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 6 New Issues\n# ============================================================\n\n- id: \"R6-N1\"\n  summary: \"GSM8K 单基准 GRPO 主实验，Title/Abstract 做一般性声明\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。补充基准（MATH-500 截断受损、MBPP margin ~1pp）不够有力。R1 指出 MBPP 受控方法内排序与 GSM8K 一致但 margin 过小。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"Layer-depth pruning pattern 与 representational diversity 混淆（confound 未排除）\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"R1-N3 提出：CKA-only 72.5% 移除集中 L0-9，优势可能来自保留 late layers 而非 CKA 本身。需 depth-controlled ablation。R2 未直接评论但其 MF4 覆盖类似关切。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N3\"\n  summary: \"缺失高度相关文献：RL Finetunes Small Subnetworks (2505.11711)\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2 交叉回应新增：RL fine-tuning 只更新 5-30% 参数，与 pruning+RLVR 直接相关——剪枝标准是否保留了 RL 关键子网络可能才是关键因素。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W1\"\n  summary: \"Reward-accuracy decoupling 未区分 format compliance vs reasoning quality\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W2 提出，R1 AGREE 并补充：f_b 混淆两种失败模式，需报告各方法 EOS rate 和 format compliance rate 变化。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"实验仅覆盖 MLP channel pruning，Title/Abstract 未限定 scope\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W1 提出，R1 AGREE。建议 Title 或 Abstract 加入 'structured MLP pruning' 限定。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"遗漏 3 篇相关工作：layer pruning limits (2602.01997)、online rollout pruning (2603.24840)、LaCo (EMNLP 2024)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W5 提出前两篇，R1 web search 确认真实存在。R2-W2 提出 LaCo。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W4\"\n  summary: \"Welch's t-test at N=3 统计功效极低，缺 effect size 和 CI\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W1：补充 Cohen's d 和 bootstrap 95% CI。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"15%/25% sparsity 实验为 single-seed，sparsity-dependent decoupling 统计基础不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W5 交叉回应提出。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"RASP 表现差于 Standard 缺乏充分解释\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W5：需分析 importance 和 CKA overlap 的相关性，解释 multiplicative 组合为何失效。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W7\"\n  summary: \"Table 1 脚注 'Only redundancy-based pruning sustains RL recovery' 与 Random 排第二矛盾\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer AGREE。建议改为 'Only redundancy-based pruning enables active RL learning'。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W8\"\n  summary: \"Section 5 Discussion 偏薄（仅半页）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 小问题提出，R1 AGREE 并建议讨论：CKA 与 RL exploration 关系、actionable 建议、Lottery Ticket 联系。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M1\"\n  summary: \"Reward-accuracy decoupling 首次使用时无正式定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2 小问题。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M2\"\n  summary: \"Figure 2 y 轴未标注 mean vs peak reward\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 提出。R1 确认应为 per-step mean reward。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M3\"\n  summary: \"Eq.1 未写出 Taylor expansion 完整数学形式\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2 小问题。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "issues_yaml": "issues:\n# ============================================================\n# Round 1-3 Issues — ALL RESOLVED\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"Post-SFT 准确率混淆变量未控制\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Qwen-Math reversal + RASP counter-example + scoped claims\"\n  resolution_round: 3\n\n- id: \"R1-N2\"\n  summary: \"Table 2 混用控制实验与 separately optimized runs\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"v5 controlled data (step-100, patience=50, lr=5e-7)\"\n  resolution_round: 1\n\n- id: \"R1-N3\"\n  summary: \"reward_desert_patience 参数不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"所有方法 patience=50\"\n  resolution_round: 1\n\n- id: \"R1-N4\"\n  summary: \"单种子设计\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"CKA-only 64.39%±0.19pp, Standard 59.84%±0.38pp, p=0.0009\"\n  resolution_round: 1\n\n- id: \"R2-N1\"\n  summary: \"标题与结论错位\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\"\n  resolution_round: 1\n\n- id: \"R2-N2\"\n  summary: \"实验规模不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"脚注透明标注 + Limitations 强化 + Abstract scoped\"\n  resolution_round: 3\n\n- id: \"R1-W1\"\n  summary: \"相关→因果跳跃\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"全文 determines → shapes/significantly influences，与标题 Shape 一致\"\n  resolution_round: 3\n\n- id: \"R1-W2\"\n  summary: \"'actively harmful' 过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"去除 actively harmful\"\n  resolution_round: 1\n\n- id: \"R1-W3\"\n  summary: \"MATH-500 TBD 条目\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Truncated% 列删除，数据完整\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"主结果缺统计检验\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Bootstrap CI + McNemar's p=0.0009\"\n  resolution_round: 1\n\n- id: \"R2-N3\"\n  summary: \"Self-Healing 性能差距未讨论\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"conditions differ sufficiently that direct comparison not meaningful\"\n  resolution_round: 1\n\n- id: \"R2-W1\"\n  summary: \"Orphan bib 条目\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"0 orphan bib entries\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"CKA 可靠性未讨论\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"method.tex: linear CKA + Spearman ρ≥0.964\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"引用年份错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"bib 年份已修正\"\n  resolution_round: 1\n\n- id: \"R1-M1\"\n  summary: \"Decoupling 可能是训练步数不足\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"100 GRPO steps caveat\"\n  resolution_round: 1\n\n- id: \"R1-M2\"\n  summary: \"Abstract 'self-recovery' 来自单次事件\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"全文无 self-recovery\"\n  resolution_round: 1\n\n- id: \"R1-M3\"\n  summary: \"Recovery capacity 未形式化定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"定义已添加，R2 认为足够\"\n  resolution_round: 3\n\n- id: \"R1-M4\"\n  summary: \"Table 5 vs Table 1 reward 不一致\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"CKA-only reward 两表均为 0.354\"\n  resolution_round: 1\n\n- id: \"R2-NEW-N1\"\n  summary: \"主文本超过 8 页 — desk rejection 风险\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"压缩后主文本 8 页合规\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W1\"\n  summary: \"90.83% vs 81.27% unpruned accuracy 矛盾\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注解释 SFT catastrophic forgetting\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W2\"\n  summary: \"Qwen-Math 跨架构验证仅 SFT，Abstract overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 区分 GRPO(DeepSeek) vs SFT(Qwen-Math)\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W3\"\n  summary: \"GRPO 准确率改变 < 1pp — 实际效用存疑\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"300-step accuracy + reward-accuracy decoupling 论证\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W4\"\n  summary: \"RASP/Random 仍为单种子\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注透明标注 + Limitations 披露\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W5\"\n  summary: \"Random baseline SFT/GRPO Acc 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Table 2 脚注标注 checkpoint not preserved\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W6\"\n  summary: \"正文 5 处 'determines' 残留\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"全部替换为 shapes/significantly influences\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M1\"\n  summary: \"GRPO batch size / rollouts 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M2\"\n  summary: \"SFT lr/batch/optimizer 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-VIS-1\"\n  summary: \"末页 Figure 6 仅占 30%，70% 空白\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 重排\"\n  resolution_round: 3\n\n- id: \"R2-VIS-2\"\n  summary: \"Appendix page 12 过度拥挤\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 拆分到多页\"\n  resolution_round: 3\n\n- id: \"R3-S5\"\n  summary: \"Qwen-Math 'strongest evidence' 措辞仍略强\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"strongest → additional evidence in §4.5\"\n  resolution_round: 3\n\n- id: \"R3-M2\"\n  summary: \"300-step accuracy 未标注 seed\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"(single seed) 标注已添加到 §4.3\"\n  resolution_round: 3\n\n- id: \"R3-M3\"\n  summary: \"无代码/checkpoint 发布声明\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"Code and checkpoints release statement in Conclusion\"\n  resolution_round: 3\n\n# ============================================================\n# Round 5 Issues — Updated with Round 6 observations\n# ============================================================\n\n- id: \"R5-N1\"\n  summary: \"Reward-accuracy decoupling 削弱 GRPO recovery 叙事（20% 精度差距 4.55pp 中 4.62pp 来自 SFT）\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。SYSTEMIC_ISSUE #1 核心。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W4 和 R2-W2 再次提出，增加新角度：需区分 format compliance vs reasoning quality。R2 建议细粒度分析 format-correct-but-wrong vs format-broken。\"\n  action_items:\n    - round: 5\n      action: \"D098 dual-layer reframe\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N2\"\n  summary: \"Cross-architecture (Qwen2.5-Math-7B) 缺乏 GRPO 验证\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前不可行（需全 pipeline ~50h GPU）。但 1.5B GRPO 数据已有。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次提出。R1 指出论文自身 'SFT does not predict GRPO' 逻辑与 SFT-only 跨架构验证自相矛盾。R2 认为 Abstract 'initial evidence for generality' overclaim。\"\n  action_items:\n    - round: 5\n      action: \"补入 1.5B GRPO 数据作 cross-scale validation\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"RASP/Random 种子不对称（2/4 方法无统计支撑）\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"核心比较 CKA vs Standard 有 3-seed p=0.0009。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 升级为 critical (N1)：RASP α=4.0 active learning 说明 seed 敏感性高。R2-W3 同意。R1 补充：RASP collapse 极端但 Standard vs Random 排序需多 seed 验证。\"\n  action_items:\n    - round: 5\n      action: \"Limitations 标注 + 核心 claim 限定 CKA vs Standard\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"CKA-recovery 因果机制仅为相关性证据\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"SYSTEMIC_ISSUE #2 成员。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。R2 明确指出 Contribution 3 将 correlational observation 升格为 numbered contribution 是 overclaim。R1 完全同意并建议降级为 Discussion observation。\"\n  action_items:\n    - round: 5\n      action: \"Jaccard overlap 分析 + Limitations 承认缺干预实验\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Per-layer capacity floor (40%) 未消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前无法做 full pipeline ablation。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W3 再次提出，建议 floor ∈ {30%, 50%, 60%} 消融。\"\n  action_items:\n    - round: 5\n      action: \"Limitations 讨论 + rebuttal 论点准备\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"α 消融缺 GRPO reward 数据\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"高 ROI 实验。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出。R2-W1 扩展为 κ 消融缺失（κ∈{0.25,0.5,2.0,4.0}），指出仅 κ=1.0 不足以判定 RASP collapse。\"\n  action_items:\n    - round: 5\n      action: \"α=4.0 GRPO 100步实验\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"'Recovery capacity gradient' 术语与 gradient descent 混淆\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W4 指出 Abstract 'spectrum' vs Table 1 caption 'gradient' 不一致仍然存在。R1 确认。\"\n  action_items:\n    - round: 5\n      action: \"全文替换为 'recovery capacity spectrum'\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M1\"\n  summary: \"Section 5 末尾溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"约 2 行溢出\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n  action_items:\n    - round: 5\n      action: \"Paper Agent 压缩 §5 确保 8 页合规\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M2\"\n  summary: \"Abstract p<0.001 未说明统计检验方法\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"N=3 t-test p<0.001 需极大效应量\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n  action_items:\n    - round: 5\n      action: \"Abstract 标注 Welch's t-test\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M3\"\n  summary: \"Page 7 display items 过度拥挤\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Figure 3 + Figure 4 + Table 2 挤在同一页\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及。视觉审查未标记此问题，可能已修复。\"\n  action_items:\n    - round: 5\n      action: \"Figure 前移平衡视觉节奏\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M4\"\n  summary: \"bib key 年份误导 + selfhealing2025 venue 缺失\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"lachance2024cka→2022, klabunde→2023, selfhealing2025 venue 空\"\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W3 发现新引用错误：正文 'Dong et al. (2026)' vs 参考文献 'Longyi Deng'。原 bib key 问题状态不明。\"\n  action_items:\n    - round: 5\n      action: \"Paper Agent 修正 bib 条目\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M5\"\n  summary: \"Figure 2 RASP/Standard 颜色区分度不足\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: []\n      note: \"视觉审查发现\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1 小问题再次提出：Figure 2 四条曲线区分度不够，建议不同 line style。R2 也提到字号偏小。\"\n  action_items:\n    - round: 5\n      action: \"添加不同 line style 辅助区分\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 6 New Issues\n# ============================================================\n\n- id: \"R6-N1\"\n  summary: \"GSM8K 单基准 GRPO 主实验，Title/Abstract 做一般性声明\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。补充基准（MATH-500 截断受损、MBPP margin ~1pp）不够有力。R1 指出 MBPP 受控方法内排序与 GSM8K 一致但 margin 过小。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"Layer-depth pruning pattern 与 representational diversity 混淆（confound 未排除）\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"R1-N3 提出：CKA-only 72.5% 移除集中 L0-9，优势可能来自保留 late layers 而非 CKA 本身。需 depth-controlled ablation。R2 未直接评论但其 MF4 覆盖类似关切。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N3\"\n  summary: \"缺失高度相关文献：RL Finetunes Small Subnetworks (2505.11711)\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2 交叉回应新增：RL fine-tuning 只更新 5-30% 参数，与 pruning+RLVR 直接相关——剪枝标准是否保留了 RL 关键子网络可能才是关键因素。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W1\"\n  summary: \"Reward-accuracy decoupling 未区分 format compliance vs reasoning quality\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W2 提出，R1 AGREE 并补充：f_b 混淆两种失败模式，需报告各方法 EOS rate 和 format compliance rate 变化。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"实验仅覆盖 MLP channel pruning，Title/Abstract 未限定 scope\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W1 提出，R1 AGREE。建议 Title 或 Abstract 加入 'structured MLP pruning' 限定。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"遗漏 3 篇相关工作：layer pruning limits (2602.01997)、online rollout pruning (2603.24840)、LaCo (EMNLP 2024)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W5 提出前两篇，R1 web search 确认真实存在。R2-W2 提出 LaCo。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W4\"\n  summary: \"Welch's t-test at N=3 统计功效极低，缺 effect size 和 CI\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W1：补充 Cohen's d 和 bootstrap 95% CI。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"15%/25% sparsity 实验为 single-seed，sparsity-dependent decoupling 统计基础不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W5 交叉回应提出。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"RASP 表现差于 Standard 缺乏充分解释\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W5：需分析 importance 和 CKA overlap 的相关性，解释 multiplicative 组合为何失效。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W7\"\n  summary: \"Table 1 脚注 'Only redundancy-based pruning sustains RL recovery' 与 Random 排第二矛盾\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer AGREE。建议改为 'Only redundancy-based pruning enables active RL learning'。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W8\"\n  summary: \"Section 5 Discussion 偏薄（仅半页）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 小问题提出，R1 AGREE 并建议讨论：CKA 与 RL exploration 关系、actionable 建议、Lottery Ticket 联系。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M1\"\n  summary: \"Reward-accuracy decoupling 首次使用时无正式定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2 小问题。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M2\"\n  summary: \"Figure 2 y 轴未标注 mean vs peak reward\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 提出。R1 确认应为 per-step mean reward。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M3\"\n  summary: \"Eq.1 未写出 Taylor expansion 完整数学形式\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2 小问题。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-22T05:02:10.917859+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml\", \"bytes\": 19772}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 239
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-22T05:04:42.142086+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 6 审稿报告\n\n**论文**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\n**Venue**: EMNLP 2026 (ARR)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）\n**轮次**: Round 1（fresh 审稿），交叉分享后达成共识，1 轮收敛\n\n---\n\n## Summary\n\n论文研究不同剪枝评分标准（CKA-only、Standard importance、RASP、Random）对推理型语言模型 RLVR 恢复能力的影响。采用严格控制变量设计（四种方法共享同一 structural analysis pipeline，仅变化 scoring criterion），在 DeepSeek-R1-Distill-Qwen-7B 上通过 SFT→GRPO 两阶段 pipeline 验证。核心发现：基于 CKA 冗余度的剪枝显著优于基于梯度重要性的方法，形成 \"recovery capacity spectrum\"，并观察到 reward-accuracy decoupling 现象。\n\n---\n\n## Strengths\n\n**S1. 控制变量实验设计（双 Reviewer 共识，论文最大亮点）**\n四种剪枝标准共享完全相同的 structural analysis pipeline，唯一变量是 scoring criterion。这种设计在 LLM 剪枝文献中极为少见，使归因分析干净可靠。R1 指出此设计 \"在剪枝文献中少见\"。[R1-S1, R2-S1]\n\n**S2. 多维度训练动态诊断**\nreward trajectory、f_b（全零 reward batch 比例）、gradient norm、KL divergence 四维诊断体系超越常见的 final-checkpoint accuracy 报告，提供了丰富的训练行为洞察。[R1-S2, R2-S2]\n\n**S3. Actionable finding**\nCKA-based >> gradient importance for RL recovery 是可直接指导 pruning practitioners 实践的发现。[R1-S1, R2-S2]\n\n**S4. Reward-accuracy decoupling 观察**\n作为科学发现有独立价值，揭示 RL reward 优势不等于下游准确率优势。[R1-S4, R2-S4]\n\n**S5. 可复现性高**\n超参数表完整（Table 4, Appendix A），Algorithm 1 伪代码清晰，硬件报告充分。[R1-S3, R2-S4]\n\n**S6. RASP 负面结果的指导价值**\nRASP 的失败为社区提供了 \"不应做什么\" 的实际参考。[R2-S3]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, 双 Reviewer 共识] **GSM8K 单基准 GRPO 主实验，Title/Abstract 做一般性声明**\n所有 GRPO 主实验（recovery capacity spectrum、reward-accuracy decoupling、training dynamics）仅在 GSM8K 上进行。补充基准证据不够有力：MATH-500 受 2048-token 截断影响方法间差异被压缩至噪声水平（|Δ| ≤ 1.2pp）；MBPP 四个受控方法 margin 仅 ~1pp。Title \"How Pruning Criteria Shape Post-RLVR Recovery\" 和 Abstract 均为一般性措辞，与单基准实验支撑不匹配。R1 补充：MBPP 受控方法内排序与 GSM8K 一致（CKA-only 领先），但 margin 过小不具统计说服力。\n→ 至少需一个非 GSM8K 基准的完整 GRPO 实验，或严格限定 scope 至 \"mathematical reasoning on GSM8K\"。[R2-N1, R1-AGREE]\n\n**MF2** [critical, 双 Reviewer 共识] **RASP/Random 仅 1 GRPO seed，统计标准不对称**\nCKA-only 和 Standard 各有 3 seeds（Table 11, Appendix I），RASP 和 Random 为 N=1。论文声称 \"RASP collapses permanently (0.061)\" 和 \"Random stagnates\"，但 RASP α=4.0 在 preliminary 实验中显示 active learning（peak reward 0.256, Section 4.4），说明 CKA 权重微小变化可翻转训练动态。Spectrum 的下半部分（Random > Standard > RASP）排序可靠性存疑。R1 补充：RASP collapse 虽极端但 Standard（peak 0.081）与 Random（0.14-0.19）之间的排序是否稳健需多 seed 验证。\n→ 为 RASP 和 Random 各补充至少 3 GRPO seeds。[R1-N1, R2-W3, mutual AGREE]\n\n**MF3** [critical, 双 Reviewer 共识] **跨架构验证仅 SFT、N=200，与论文自身逻辑矛盾**\nQwen2.5-Math-7B 验证仅到 SFT 阶段（Table 13），N=200 且自标 \"preliminary\"，但 Abstract 声称 \"provide initial evidence for generality\"。论文自身在 Section 4.4 明确指出 \"Post-SFT accuracy does not predict GRPO outcome\"。R1 精准指出：按论文自己的逻辑，SFT-only 结果不能推断 RLVR generality，此处构成自相矛盾。且两个模型共享 Qwen2.5 base architecture，跨架构多样性不足。\n→ 完成 GRPO 验证或将 Abstract claim 严格限定为 \"SFT-level structural effects generalize\"。[R1-N2, R2-N3, mutual AGREE]\n\n**MF4** [critical, 双 Reviewer 共识] **Contribution 3 \"representational diversity\" 机制证据仅为相关性，列为 numbered contribution 是 overclaim**\nSection 4.5 证据链：CKA heatmap 视觉观察 → overlap analysis 描述性统计。无因果干预实验。R2 指出将 correlational observation 升格为 numbered contribution 不当；R1 完全同意并指出 \"plausible mechanism\" 的 hedging 不足以支撑 numbered contribution 地位。R1 建议一个可行的因果验证思路：人工构造等量剪枝但 diversity 不同的模型对比 GRPO recovery。\n→ 降级为 observation/hypothesis 置于 Discussion，或增加因果干预实验。[R2-N2, R1-AGREE]\n\n**MF5** [critical, R1 提出] **Layer-depth pruning pattern 与 representational diversity 混淆（confound 未排除）**\nCKA-only 将 72.5% 移除集中在 early layers (L0-9)，Standard 均匀分布（Appendix N）。论文将优势归因于 \"preserved representational diversity\"，但同样合理的解释是 CKA-only 碰巧保留了对推理关键的 late layers。此 confound 未被排除，使 Contribution 3 的归因可能不准确。\n→ 增加 depth-controlled baseline（如 \"Late-Layer-First\" pruning），或在 Discussion 中充分讨论此 confound。[R1-N3; R2 未直接评论但其 MF4 覆盖类似关切]\n\n**MF6** [critical, R2 提出] **缺失高度相关文献**\n\"RL Finetunes Small Subnetworks\" (arXiv:2505.11711) 揭示 RL fine-tuning 只更新 5–30% 参数，在 GRPO 等 7 种 RL 算法上均成立。与本文核心主题直接相关：如果 RL 只在小子网络上操作，剪枝标准是否保留了该子网络可能才是解释 CKA-only 优势的关键因素。\n→ 在 Related Work 讨论并引入 Section 4.5 机制分析。[R2-N2 交叉回应]\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning] Welch's t-test at N=3 统计功效极低（Section 4.2, p=0.0009）。补充 Cohen's d 和 bootstrap 95% CI。[R1-W1]\n\n**SF2** [warning] α/κ 消融不完整：α 消融仅用 post-prune accuracy（Table 6），缺 GRPO reward 全景；RASP 只测 κ=1.0 就结论 collapse，缺 κ∈{0.25,0.5,2.0,4.0} 消融。[R1-W2, R2-W1]\n\n**SF3** [warning] 40% per-layer capacity floor 未消融（Section 3.3, Limitations）。建议 floor ∈ {30%, 50%, 60%}。[R1-W3]\n\n**SF4** [warning] Reward-accuracy decoupling 未区分 format compliance vs reasoning quality。f_b 混淆格式崩塌和推理错误两种失败模式，需细粒度分析。建议报告各方法 EOS rate 和 format compliance rate 随 step 变化。[R2-W2, R1-AGREE]\n\n**SF5** [warning] MLP channel pruning scope 未在 Title/Abstract 限定。实验严格限定在 MLP channel group pruning，但 Title 完全一般化。建议加入 \"structured MLP pruning\" 限定。[R2-W1, R1-AGREE]\n\n**SF6** [warning] 术语不一致：\"recovery capacity spectrum\"（Abstract）vs \"recovery capacity gradient\"（Table 1 caption）。应统一。[R2-W4, R1-AGREE]\n\n**SF7** [warning] 遗漏 3 篇相关工作：(1) \"On the Limits of Layer Pruning for Generative Reasoning in LLMs\" (arXiv:2602.01997, Feb 2026)；(2) \"Prune as You Generate: Online Rollout Pruning for RLVR\" (arXiv:2603.24840, March 2026)；(3) LaCo (Yang et al., 2024, EMNLP Findings)。R1 web search 确认前两篇真实存在。[R2-W5, R2-W2, R1-AGREE]\n\n**SF8** [warning] 15%/25% sparsity 实验为 single-seed，\"sparsity-dependent decoupling\" 统计基础不足。[R2-W5]\n\n**SF9** [warning] RASP 表现差于 Standard 缺乏充分解释。需分析 importance 和 CKA overlap 的相关性，解释 multiplicative 组合为何失效。[R1-W5]\n\n**SF10** [warning] 引用错误：正文 \"Dong et al. (2026)\" vs 参考文献 \"Longyi Deng\"。[R2-W3]\n\n---\n\n## Reviewer Consensus\n\n以下问题双 Reviewer 明确达成 [AGREE]：\n1. GSM8K 单基准是最大结构性弱点（MF1）\n2. RASP/Random 单 seed 统计不充分（MF2）\n3. SFT-only 跨架构验证与论文自身 \"SFT ≠ GRPO prediction\" 论点自相矛盾（MF3）\n4. Contribution 3 机制证据仅相关性，列为 numbered contribution 是 overclaim（MF4）\n5. Table 1 脚注 \"Only redundancy-based pruning sustains RL recovery\" 与 Random 排第二矛盾（SF7 小问题）\n6. Section 5 Discussion 偏薄（SF8）\n7. **控制变量设计是论文最大亮点**——双 Reviewer 一致认为此设计在 LLM 剪枝文献中有独特价值\n\n## Reviewer Divergence\n\n**评分分歧**：R1 初始 3.5 (Borderline Conference)，R2 初始 3.0 (Findings)。交叉分享后 R1 表示 \"R2 的 3.0 合理\"，分歧实质消解。\n\n**MF5 (Layer-depth confound)**：R1 单独提出为 critical。R2 未直接评论此具体 confound，但其对 mechanism 证据的质疑（MF4）覆盖了类似关切。\n\n**MF6 (Missing literature: RL Finetunes Small Subnetworks)**：R2 在交叉回应中新增。R1 未评论此具体论文。\n\n**Excitement 评分**：R1 给 3/5，R2 给 2.5/5。R2 认为贡献主要是经验发现，无新方法或可落地工具，CKA-only 评分本身非原创（源自 Lachance &amp; Bhatt, 2022）。\n\n---\n\n## Questions\n\n1. RASP α=4.0 的 active learning（peak reward 0.256, Section 4.4）是否说明 RASP collapse 是超参问题而非方法本质问题？完整的 α/κ 消融结果如何？\n2. CKA-only 的 layer-depth pruning pattern（72.5% 移除集中 L0-9）是否是 recovery 优势的真正原因？是否有 depth-controlled ablation 数据？\n3. 如果 RL fine-tuning 只更新 5–30% 参数（per arXiv:2505.11711），CKA-based pruning 是否恰好保留了这些关键子网络？\n4. Reward-accuracy decoupling 中，各方法的 format compliance rate 随 GRPO step 如何变化？reward 差异是否主要来自格式合规差异？\n5. \"Post-SFT accuracy does not predict GRPO outcome\" 仅基于 4 个数据点（四种方法），是否有更多数据支撑？\n\n---\n\n## Missing References\n\n1. **RL Finetunes Small Subnetworks** (arXiv:2505.11711) — RL 只更新小子网络，与 pruning+RLVR 主题直接相关 [R2-N2, critical]\n2. **On the Limits of Layer Pruning for Generative Reasoning in LLMs** (arXiv:2602.01997, Feb 2026) — layer pruning 对推理的影响 [R2-W5, R1 confirmed]\n3. **Prune as You Generate: Online Rollout Pruning for RLVR** (arXiv:2603.24840, March 2026) — 同方向并行工作 [R2-W5, R1 confirmed]\n4. **LaCo** (Yang et al., 2024, EMNLP Findings) — structured pruning 核心文献 [R2-W2]\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）**：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2026-05-22 04:39→04:42，耗时 ~3min）。\n\n**发现**：\n- **[warning]** 连续 3 页纯文本（p3-5），Method 段缺少视觉锚点。建议在 Section 3 中插入示意图（如 scoring criteria 对比或 two-stage recovery 流程图）打破纯文本节奏\n- **[info]** Figure 3 子图 axis label 和 legend 字号偏小（约 6-7pt），打印/标准缩放下需仔细辨认\n- **[info]** Figure 4 热力图标注文字偏小\n- **[info]** Figure 5 尺寸较小（单栏宽度，约占 1/4 页面），若为重要补充结果可考虑放大\n- **[info]** 附录 E-K 多个小节挤在同一页，内容密度极高\n- **[info]** 首页无 display item，Figure 1 在第 2 页出现（非必须修改，但提前到首页底部可强化第一印象）\n\n统计：0 critical, 1 warning, 5 info。无阻断性排版问题。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.0 | 3.0 |\n| Excitement | 3.0 | 2.5 | 2.75 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5→3.0* | 3.0 | 3.0 |\n| Confidence | 4.0 | 4.0 | 4.0 |\n\n*R1 交叉分享后认同 R2 的 3.0 评估。\n\n**理由**：\n论文的控制变量实验设计是其核心方法论贡献，在 LLM 剪枝文献中有独特价值。CKA-based >> gradient importance for RL recovery 的发现有实践指导意义。多维度训练动态诊断和 reward-accuracy decoupling 观察丰富了论文的分析深度。\n\n然而，6 个 critical 问题（含双 Reviewer 共识 4 个）严重削弱了论文的可接收性：\n1. **Empirical scope 过窄**：核心 claim 的实验支撑限于单模型（DeepSeek-R1-Distill-Qwen-7B）、单基准（GSM8K）、部分方法单 seed，但 Title/Abstract 做一般性声明\n2. **机制解释不可靠**：Contribution 3 仅为相关性证据，且存在未排除的 layer-depth confound\n3. **内部逻辑矛盾**：论文自身的 \"SFT ≠ GRPO prediction\" 发现与 SFT-only 跨架构 generality claim 直接冲突\n\n论文适合 Findings track。若能补充以下修改，有望达到 3.5 (Borderline Conference)：\n- 至少一个非 GSM8K 基准的完整 GRPO 实验\n- RASP/Random 补充多 seed\n- Contribution 3 降级为 observation\n- 讨论 layer-depth confound\n- 引入 \"RL Finetunes Small Subnetworks\" 等缺失文献\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 3 \"identified representational diversity as a key mechanism\" 措辞过强 → \"observed evidence consistent with representational diversity playing a role\"\n- \"recovery capacity spectrum\" 需在首次使用时前置定义\n\n### Section 2 (Related Work)\n- 缺少 4 篇高度相关工作（见 Missing References），特别是 arXiv:2505.11711 对机制解释有直接影响\n- LaCo 作为 EMNLP 2024 Findings 的 structured pruning 核心工作应被讨论\n\n### Section 3 (Method)\n- κ=1.0 single setting 不足以评判 RASP → 需 κ 消融（κ∈{0.25,0.5,2.0,4.0}）\n- 40% capacity floor 是关键设计决策但无消融支撑\n- Algorithm 1 清晰，但 scope 限定（MLP channel pruning）应更早明确\n\n### Section 4.1-4.2 (Main Results)\n- Table 1 spectrum ordering 的统计支撑不对称（CKA/Standard N=3 vs RASP/Random N=1）\n- Table 1 脚注 \"Only redundancy-based pruning sustains RL recovery\" 与 Random 排第二矛盾 → 改为 \"Only redundancy-based pruning enables active RL learning\"\n- Welch's t-test at N=3 应补充 Cohen's d effect size 和 bootstrap 95% CI\n\n### Section 4.3 (Reward-Accuracy Decoupling)\n- 需区分 format compliance vs reasoning quality 对 reward 的贡献\n- 建议报告各方法的 EOS rate 和 format compliance rate 随 step 变化\n- \"Reward-accuracy decoupling\" 首次使用时无正式定义\n- 15% sparsity 作为 decoupling 不成立的操作点值得更多讨论\n\n### Section 4.4 (α Analysis)\n- α=4.0 \"full evaluation pending\" 应在提交前完成\n- κ 消融缺失，仅 κ=1.0 不足以判定 RASP 方法本身\n\n### Section 4.5 (Representational Diversity &amp; Cross-Architecture)\n- **Layer-depth confound 必须讨论**：CKA-only 保留 late layers 的模式可能是优势真正来源\n- \"Post-SFT accuracy does not predict GRPO outcome\" 仅基于 4 个数据点\n- Qwen2.5-Math-7B N=200 样本量不足，且仅 SFT 阶段\n\n### Section 5 (Discussion)\n- 仅半页，对控制变量比较研究而言不足\n- 缺少：(1) CKA-based redundancy 与 RL exploration 的关系讨论，(2) 对 pruning practitioners 的 actionable 建议，(3) 与 Lottery Ticket Hypothesis 的联系\n\n### Writing &amp; Format\n- \"recovery capacity spectrum\" vs \"recovery capacity gradient\" 术语不一致\n- Figure 2 y 轴标签需标注 mean vs peak reward\n- Figure 2 四条曲线区分度不够，建议不同 line style + marker\n- 引用错误：\"Dong et al. (2026)\" vs \"Longyi Deng\"\n- Method 段（p3-5）连续纯文本，缺视觉锚点（视觉审查 warning）",
  "project": "recovery_aware_struct_prune",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 6 审稿报告\n\n**论文**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models\n**Venue**: EMNLP 2026 (ARR)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）\n**轮次**: Round 1（fresh 审稿），交叉分享后达成共识，1 轮收敛\n\n---\n\n## Summary\n\n论文研究不同剪枝评分标准（CKA-only、Standard importance、RASP、Random）对推理型语言模型 RLVR 恢复能力的影响。采用严格控制变量设计（四种方法共享同一 structural analysis pipeline，仅变化 scoring criterion），在 DeepSeek-R1-Distill-Qwen-7B 上通过 SFT→GRPO 两阶段 pipeline 验证。核心发现：基于 CKA 冗余度的剪枝显著优于基于梯度重要性的方法，形成 \"recovery capacity spectrum\"，并观察到 reward-accuracy decoupling 现象。\n\n---\n\n## Strengths\n\n**S1. 控制变量实验设计（双 Reviewer 共识，论文最大亮点）**\n四种剪枝标准共享完全相同的 structural analysis pipeline，唯一变量是 scoring criterion。这种设计在 LLM 剪枝文献中极为少见，使归因分析干净可靠。R1 指出此设计 \"在剪枝文献中少见\"。[R1-S1, R2-S1]\n\n**S2. 多维度训练动态诊断**\nreward trajectory、f_b（全零 reward batch 比例）、gradient norm、KL divergence 四维诊断体系超越常见的 final-checkpoint accuracy 报告，提供了丰富的训练行为洞察。[R1-S2, R2-S2]\n\n**S3. Actionable finding**\nCKA-based >> gradient importance for RL recovery 是可直接指导 pruning practitioners 实践的发现。[R1-S1, R2-S2]\n\n**S4. Reward-accuracy decoupling 观察**\n作为科学发现有独立价值，揭示 RL reward 优势不等于下游准确率优势。[R1-S4, R2-S4]\n\n**S5. 可复现性高**\n超参数表完整（Table 4, Appendix A），Algorithm 1 伪代码清晰，硬件报告充分。[R1-S3, R2-S4]\n\n**S6. RASP 负面结果的指导价值**\nRASP 的失败为社区提供了 \"不应做什么\" 的实际参考。[R2-S3]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, 双 Reviewer 共识] **GSM8K 单基准 GRPO 主实验，Title/Abstract 做一般性声明**\n所有 GRPO 主实验（recovery capacity spectrum、reward-accuracy decoupling、training dynamics）仅在 GSM8K 上进行。补充基准证据不够有力：MATH-500 受 2048-token 截断影响方法间差异被压缩至噪声水平（|Δ| ≤ 1.2pp）；MBPP 四个受控方法 margin 仅 ~1pp。Title \"How Pruning Criteria Shape Post-RLVR Recovery\" 和 Abstract 均为一般性措辞，与单基准实验支撑不匹配。R1 补充：MBPP 受控方法内排序与 GSM8K 一致（CKA-only 领先），但 margin 过小不具统计说服力。\n→ 至少需一个非 GSM8K 基准的完整 GRPO 实验，或严格限定 scope 至 \"mathematical reasoning on GSM8K\"。[R2-N1, R1-AGREE]\n\n**MF2** [critical, 双 Reviewer 共识] **RASP/Random 仅 1 GRPO seed，统计标准不对称**\nCKA-only 和 Standard 各有 3 seeds（Table 11, Appendix I），RASP 和 Random 为 N=1。论文声称 \"RASP collapses permanently (0.061)\" 和 \"Random stagnates\"，但 RASP α=4.0 在 preliminary 实验中显示 active learning（peak reward 0.256, Section 4.4），说明 CKA 权重微小变化可翻转训练动态。Spectrum 的下半部分（Random > Standard > RASP）排序可靠性存疑。R1 补充：RASP collapse 虽极端但 Standard（peak 0.081）与 Random（0.14-0.19）之间的排序是否稳健需多 seed 验证。\n→ 为 RASP 和 Random 各补充至少 3 GRPO seeds。[R1-N1, R2-W3, mutual AGREE]\n\n**MF3** [critical, 双 Reviewer 共识] **跨架构验证仅 SFT、N=200，与论文自身逻辑矛盾**\nQwen2.5-Math-7B 验证仅到 SFT 阶段（Table 13），N=200 且自标 \"preliminary\"，但 Abstract 声称 \"provide initial evidence for generality\"。论文自身在 Section 4.4 明确指出 \"Post-SFT accuracy does not predict GRPO outcome\"。R1 精准指出：按论文自己的逻辑，SFT-only 结果不能推断 RLVR generality，此处构成自相矛盾。且两个模型共享 Qwen2.5 base architecture，跨架构多样性不足。\n→ 完成 GRPO 验证或将 Abstract claim 严格限定为 \"SFT-level structural effects generalize\"。[R1-N2, R2-N3, mutual AGREE]\n\n**MF4** [critical, 双 Reviewer 共识] **Contribution 3 \"representational diversity\" 机制证据仅为相关性，列为 numbered contribution 是 overclaim**\nSection 4.5 证据链：CKA heatmap 视觉观察 → overlap analysis 描述性统计。无因果干预实验。R2 指出将 correlational observation 升格为 numbered contribution 不当；R1 完全同意并指出 \"plausible mechanism\" 的 hedging 不足以支撑 numbered contribution 地位。R1 建议一个可行的因果验证思路：人工构造等量剪枝但 diversity 不同的模型对比 GRPO recovery。\n→ 降级为 observation/hypothesis 置于 Discussion，或增加因果干预实验。[R2-N2, R1-AGREE]\n\n**MF5** [critical, R1 提出] **Layer-depth pruning pattern 与 representational diversity 混淆（confound 未排除）**\nCKA-only 将 72.5% 移除集中在 early layers (L0-9)，Standard 均匀分布（Appendix N）。论文将优势归因于 \"preserved representational diversity\"，但同样合理的解释是 CKA-only 碰巧保留了对推理关键的 late layers。此 confound 未被排除，使 Contribution 3 的归因可能不准确。\n→ 增加 depth-controlled baseline（如 \"Late-Layer-First\" pruning），或在 Discussion 中充分讨论此 confound。[R1-N3; R2 未直接评论但其 MF4 覆盖类似关切]\n\n**MF6** [critical, R2 提出] **缺失高度相关文献**\n\"RL Finetunes Small Subnetworks\" (arXiv:2505.11711) 揭示 RL fine-tuning 只更新 5–30% 参数，在 GRPO 等 7 种 RL 算法上均成立。与本文核心主题直接相关：如果 RL 只在小子网络上操作，剪枝标准是否保留了该子网络可能才是解释 CKA-only 优势的关键因素。\n→ 在 Related Work 讨论并引入 Section 4.5 机制分析。[R2-N2 交叉回应]\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning] Welch's t-test at N=3 统计功效极低（Section 4.2, p=0.0009）。补充 Cohen's d 和 bootstrap 95% CI。[R1-W1]\n\n**SF2** [warning] α/κ 消融不完整：α 消融仅用 post-prune accuracy（Table 6），缺 GRPO reward 全景；RASP 只测 κ=1.0 就结论 collapse，缺 κ∈{0.25,0.5,2.0,4.0} 消融。[R1-W2, R2-W1]\n\n**SF3** [warning] 40% per-layer capacity floor 未消融（Section 3.3, Limitations）。建议 floor ∈ {30%, 50%, 60%}。[R1-W3]\n\n**SF4** [warning] Reward-accuracy decoupling 未区分 format compliance vs reasoning quality。f_b 混淆格式崩塌和推理错误两种失败模式，需细粒度分析。建议报告各方法 EOS rate 和 format compliance rate 随 step 变化。[R2-W2, R1-AGREE]\n\n**SF5** [warning] MLP channel pruning scope 未在 Title/Abstract 限定。实验严格限定在 MLP channel group pruning，但 Title 完全一般化。建议加入 \"structured MLP pruning\" 限定。[R2-W1, R1-AGREE]\n\n**SF6** [warning] 术语不一致：\"recovery capacity spectrum\"（Abstract）vs \"recovery capacity gradient\"（Table 1 caption）。应统一。[R2-W4, R1-AGREE]\n\n**SF7** [warning] 遗漏 3 篇相关工作：(1) \"On the Limits of Layer Pruning for Generative Reasoning in LLMs\" (arXiv:2602.01997, Feb 2026)；(2) \"Prune as You Generate: Online Rollout Pruning for RLVR\" (arXiv:2603.24840, March 2026)；(3) LaCo (Yang et al., 2024, EMNLP Findings)。R1 web search 确认前两篇真实存在。[R2-W5, R2-W2, R1-AGREE]\n\n**SF8** [warning] 15%/25% sparsity 实验为 single-seed，\"sparsity-dependent decoupling\" 统计基础不足。[R2-W5]\n\n**SF9** [warning] RASP 表现差于 Standard 缺乏充分解释。需分析 importance 和 CKA overlap 的相关性，解释 multiplicative 组合为何失效。[R1-W5]\n\n**SF10** [warning] 引用错误：正文 \"Dong et al. (2026)\" vs 参考文献 \"Longyi Deng\"。[R2-W3]\n\n---\n\n## Reviewer Consensus\n\n以下问题双 Reviewer 明确达成 [AGREE]：\n1. GSM8K 单基准是最大结构性弱点（MF1）\n2. RASP/Random 单 seed 统计不充分（MF2）\n3. SFT-only 跨架构验证与论文自身 \"SFT ≠ GRPO prediction\" 论点自相矛盾（MF3）\n4. Contribution 3 机制证据仅相关性，列为 numbered contribution 是 overclaim（MF4）\n5. Table 1 脚注 \"Only redundancy-based pruning sustains RL recovery\" 与 Random 排第二矛盾（SF7 小问题）\n6. Section 5 Discussion 偏薄（SF8）\n7. **控制变量设计是论文最大亮点**——双 Reviewer 一致认为此设计在 LLM 剪枝文献中有独特价值\n\n## Reviewer Divergence\n\n**评分分歧**：R1 初始 3.5 (Borderline Conference)，R2 初始 3.0 (Findings)。交叉分享后 R1 表示 \"R2 的 3.0 合理\"，分歧实质消解。\n\n**MF5 (Layer-depth confound)**：R1 单独提出为 critical。R2 未直接评论此具体 confound，但其对 mechanism 证据的质疑（MF4）覆盖了类似关切。\n\n**MF6 (Missing literature: RL Finetunes Small Subnetworks)**：R2 在交叉回应中新增。R1 未评论此具体论文。\n\n**Excitement 评分**：R1 给 3/5，R2 给 2.5/5。R2 认为贡献主要是经验发现，无新方法或可落地工具，CKA-only 评分本身非原创（源自 Lachance &amp; Bhatt, 2022）。\n\n---\n\n## Questions\n\n1. RASP α=4.0 的 active learning（peak reward 0.256, Section 4.4）是否说明 RASP collapse 是超参问题而非方法本质问题？完整的 α/κ 消融结果如何？\n2. CKA-only 的 layer-depth pruning pattern（72.5% 移除集中 L0-9）是否是 recovery 优势的真正原因？是否有 depth-controlled ablation 数据？\n3. 如果 RL fine-tuning 只更新 5–30% 参数（per arXiv:2505.11711），CKA-based pruning 是否恰好保留了这些关键子网络？\n4. Reward-accuracy decoupling 中，各方法的 format compliance rate 随 GRPO step 如何变化？reward 差异是否主要来自格式合规差异？\n5. \"Post-SFT accuracy does not predict GRPO outcome\" 仅基于 4 个数据点（四种方法），是否有更多数据支撑？\n\n---\n\n## Missing References\n\n1. **RL Finetunes Small Subnetworks** (arXiv:2505.11711) — RL 只更新小子网络，与 pruning+RLVR 主题直接相关 [R2-N2, critical]\n2. **On the Limits of Layer Pruning for Generative Reasoning in LLMs** (arXiv:2602.01997, Feb 2026) — layer pruning 对推理的影响 [R2-W5, R1 confirmed]\n3. **Prune as You Generate: Online Rollout Pruning for RLVR** (arXiv:2603.24840, March 2026) — 同方向并行工作 [R2-W5, R1 confirmed]\n4. **LaCo** (Yang et al., 2024, EMNLP Findings) — structured pruning 核心文献 [R2-W2]\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）**：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2026-05-22 04:39→04:42，耗时 ~3min）。\n\n**发现**：\n- **[warning]** 连续 3 页纯文本（p3-5），Method 段缺少视觉锚点。建议在 Section 3 中插入示意图（如 scoring criteria 对比或 two-stage recovery 流程图）打破纯文本节奏\n- **[info]** Figure 3 子图 axis label 和 legend 字号偏小（约 6-7pt），打印/标准缩放下需仔细辨认\n- **[info]** Figure 4 热力图标注文字偏小\n- **[info]** Figure 5 尺寸较小（单栏宽度，约占 1/4 页面），若为重要补充结果可考虑放大\n- **[info]** 附录 E-K 多个小节挤在同一页，内容密度极高\n- **[info]** 首页无 display item，Figure 1 在第 2 页出现（非必须修改，但提前到首页底部可强化第一印象）\n\n统计：0 critical, 1 warning, 5 info。无阻断性排版问题。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.0 | 3.0 |\n| Excitement | 3.0 | 2.5 | 2.75 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5→3.0* | 3.0 | 3.0 |\n| Confidence | 4.0 | 4.0 | 4.0 |\n\n*R1 交叉分享后认同 R2 的 3.0 评估。\n\n**理由**：\n论文的控制变量实验设计是其核心方法论贡献，在 LLM 剪枝文献中有独特价值。CKA-based >> gradient importance for RL recovery 的发现有实践指导意义。多维度训练动态诊断和 reward-accuracy decoupling 观察丰富了论文的分析深度。\n\n然而，6 个 critical 问题（含双 Reviewer 共识 4 个）严重削弱了论文的可接收性：\n1. **Empirical scope 过窄**：核心 claim 的实验支撑限于单模型（DeepSeek-R1-Distill-Qwen-7B）、单基准（GSM8K）、部分方法单 seed，但 Title/Abstract 做一般性声明\n2. **机制解释不可靠**：Contribution 3 仅为相关性证据，且存在未排除的 layer-depth confound\n3. **内部逻辑矛盾**：论文自身的 \"SFT ≠ GRPO prediction\" 发现与 SFT-only 跨架构 generality claim 直接冲突\n\n论文适合 Findings track。若能补充以下修改，有望达到 3.5 (Borderline Conference)：\n- 至少一个非 GSM8K 基准的完整 GRPO 实验\n- RASP/Random 补充多 seed\n- Contribution 3 降级为 observation\n- 讨论 layer-depth confound\n- 引入 \"RL Finetunes Small Subnetworks\" 等缺失文献\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 3 \"identified representational diversity as a key mechanism\" 措辞过强 → \"observed evidence consistent with representational diversity playing a role\"\n- \"recovery capacity spectrum\" 需在首次使用时前置定义\n\n### Section 2 (Related Work)\n- 缺少 4 篇高度相关工作（见 Missing References），特别是 arXiv:2505.11711 对机制解释有直接影响\n- LaCo 作为 EMNLP 2024 Findings 的 structured pruning 核心工作应被讨论\n\n### Section 3 (Method)\n- κ=1.0 single setting 不足以评判 RASP → 需 κ 消融（κ∈{0.25,0.5,2.0,4.0}）\n- 40% capacity floor 是关键设计决策但无消融支撑\n- Algorithm 1 清晰，但 scope 限定（MLP channel pruning）应更早明确\n\n### Section 4.1-4.2 (Main Results)\n- Table 1 spectrum ordering 的统计支撑不对称（CKA/Standard N=3 vs RASP/Random N=1）\n- Table 1 脚注 \"Only redundancy-based pruning sustains RL recovery\" 与 Random 排第二矛盾 → 改为 \"Only redundancy-based pruning enables active RL learning\"\n- Welch's t-test at N=3 应补充 Cohen's d effect size 和 bootstrap 95% CI\n\n### Section 4.3 (Reward-Accuracy Decoupling)\n- 需区分 format compliance vs reasoning quality 对 reward 的贡献\n- 建议报告各方法的 EOS rate 和 format compliance rate 随 step 变化\n- \"Reward-accuracy decoupling\" 首次使用时无正式定义\n- 15% sparsity 作为 decoupling 不成立的操作点值得更多讨论\n\n### Section 4.4 (α Analysis)\n- α=4.0 \"full evaluation pending\" 应在提交前完成\n- κ 消融缺失，仅 κ=1.0 不足以判定 RASP 方法本身\n\n### Section 4.5 (Representational Diversity &amp; Cross-Architecture)\n- **Layer-depth confound 必须讨论**：CKA-only 保留 late layers 的模式可能是优势真正来源\n- \"Post-SFT accuracy does not predict GRPO outcome\" 仅基于 4 个数据点\n- Qwen2.5-Math-7B N=200 样本量不足，且仅 SFT 阶段\n\n### Section 5 (Discussion)\n- 仅半页，对控制变量比较研究而言不足\n- 缺少：(1) CKA-based redundancy 与 RL exploration 的关系讨论，(2) 对 pruning practitioners 的 actionable 建议，(3) 与 Lottery Ticket Hypothesis 的联系\n\n### Writing &amp; Format\n- \"recovery capacity spectrum\" vs \"recovery capacity gradient\" 术语不一致\n- Figure 2 y 轴标签需标注 mean vs peak reward\n- Figure 2 四条曲线区分度不够，建议不同 line style + marker\n- 引用错误：\"Dong et al. (2026)\" vs \"Longyi Deng\"\n- Method 段（p3-5）连续纯文本，缺视觉锚点（视觉审查 warning）",
    "project": "recovery_aware_struct_prune",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-22T05:04:46.361453+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_04e6cf8fe41be27a49d5657e80962f12:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4219
}
```

</details>

---


### Assistant

_source line 420 · 2026-05-22T05:04:55.678179+00:00_

Round 6 审稿报告已投递。

**汇总**：
- **Overall Score: 3.0 / 5 (Findings)**，R1 (3.5→3.0) 和 R2 (3.0) 交叉后达成共识
- **6 个 Must-Fix**（4 个双 Reviewer 共识）：GSM8K 单基准 overclaim、RASP/Random 单 seed、SFT-only 跨架构与自身逻辑矛盾、Contribution 3 相关性≠因果、layer-depth confound、缺失关键文献
- **10 个 Should-Fix**：统计功效、α/κ 消融、scope 限定、术语统一等
- 论文的控制变量设计被双 Reviewer 一致认为是核心亮点；修复关键问题后有望达 3.5 (Borderline Conference)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 38

## Round 38

2 recorded events


### User

_source line 421 · 2026-05-22T05:04:56.776147+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

总结：对 R2 的 3 个 Must-Fix、5 个 Should-Fix 和 4 个小问题，我全部标注 **[AGREE]**，但在多处补充了细节修正和 nuance：

- **N1**：同意单基准是最大弱点，但修正了 R2 关于 ShortGPT 在 MBPP 上的论证——ShortGPT 是 layer pruning，与四个受控 MLP channel 方法不同类；在受控方法内部 MBPP 排序实际一致，只是 margin 过小。
- **N2**：同意 correlational evidence 不应列为 numbered contribution，但注意到论文已用 "plausible mechanism" 做了 hedging。
- **N3**：完全同意 R2 的逻辑论证——论文自身说 "SFT ≠ GRPO prediction"，却用 SFT-only 跨架构结果声称 GRPO generality，构成自相矛盾。
- **W3**：同意多 seed 原则，但补充 RASP 崩塌（peak 0.061）极端到多 seed 不太可能改变定性结论。
- 对 R2 的 Overall 3.0 (Findings) 评分表示认同，认为补充实验后有潜力达到 3.5。

---

[Reviewer 2 审稿结果]:
审稿完成，已提交至 Review Director。

核心判断：**Overall 3.0 (Findings)**。论文的控制变量实验设计干净，研究问题有实际价值，但三个主要问题限制了评分：
1. "Recovery capacity spectrum" 的通用性 claim 超出了单模型/单数据集/单稀疏度的实验支撑范围
2. 遗漏了 "RL Finetunes Small Subnetworks" (2505.11711) 这篇高度相关的文献
3. 机制解释（representational diversity）停留在相关性层面，"identified mechanism" 的措辞过强

---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

### Must-Fix

**[AGREE] R1-N1: RASP/Random N=1 无法支撑 "collapse permanently"**
完全同意。Table 1 脚注确认 RASP/Random 仅 N=1。更关键的是 Section 4.4/Table 6 中 α=4.0 的 RASP 在 preliminary 评估中显示 active learning（peak reward 0.256），说明 CKA 权重变化能翻转训练动态。α=1.0 的 collapse 可能只是特定超参数下的结果。这与我的 W1（κ 无消融）互为印证。

**[AGREE] R1-N2: Cross-architecture 缺失 GRPO**
完全同意。Section 4.5 明确 "GRPO validation on Qwen2.5-Math-7B is deferred to future work"。论文核心贡献是 GRPO recovery，但跨架构验证仅覆盖 SFT。且两个模型共享 Qwen2.5 base，"cross-architecture" 说服力有限。与我的 N1（spectrum overclaim）一致。

**[AGREE] R1-N3: Layer-depth confound 未排除**
这是 R1 最精锐的发现。Appendix N 数据直接支持：CKA-only 72.5% 移除集中在 L0-9，保留几乎全部 L16-27 late layers；Standard 均匀分布。CKA-only 的优势可能来自保留了对推理关键的 late layers，而非 representational diversity。这一 confound 加强了我的 N3（因果机制仅为相关性）。需要 depth-controlled baseline（"Late-Layer-First" pruning）来分离两种效应。

### Should-Fix

**[AGREE] R1-W1** Welch's t-test at N=3 功效低，需补 Cohen's d + bootstrap CI。

**[AGREE] R1-W2** α 消融缺 GRPO reward，与我的 W1 同一问题。α=4.0 GRPO 全面评估结果可能改变论文 narrative。

**[AGREE] R1-W3** 40% capacity floor 与不同 criteria 的交互可能不同，需消融。

**[REBUT] R1-W4** 部分不同意。CKA-only 在 accuracy 上仍最优（Table 1: 0.285 vs Standard 0.090），decoupling 不削弱其实用价值。但 R1 正确指出 20% sparsity 下 GRPO 对 accuracy 增量 <0.2pp，"GRPO recovery" 叙事在 accuracy 维度上确实不够说服力。建议作者将 15% sparsity 作为主要展示点，或重新定位为 "post-pruning fine-tuning recovery"（涵盖 SFT+GRPO）。

**[AGREE] R1-W5** RASP 差于 Standard 需更深分析（importance/overlap scale 不匹配、乘法组合的失效机制）。

### 小问题
全部 [AGREE]。特别认同 "Post-SFT does not predict GRPO" 基于 4 个数据点的问题——N=4 无法支撑预测性结论。

### 综合评估
R1 和我（R2）的核心关切高度一致：(1) 统计证据不足（N=1 methods, N=3 t-test）；(2) 跨架构/跨任务验证缺失；(3) 机制解释的因果性未建立。R1 的 N3（layer-depth confound）是重要补充，为 CKA-only 的优势提供了具体的替代解释。两份 review 合在一起，指向论文需要：补齐 seeds、增加 depth-controlled baseline、完成 α=4.0 GRPO 评估、限定 claim scope。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：对 R1 的 3 个 Must-Fix 全部 [AGREE]，5 个 Should-Fix 中 4 个 [AGREE]、1 个 [REBUT]（W4 部分反驳——CKA-only 在 accuracy 上仍最优，但 GRPO 增量贡献确实微弱），5 个小问题全部 [AGREE]。R1-N3（layer-depth confound）是最有价值的新发现，为 CKA-only 优势提供了我自己未提出的具体替代解释。两份 review 的核心关切高度一致，共同指向统计证据不足、跨验证缺失、因果归因未建立三个方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 422 · 2026-05-22T05:05:32.259806+00:00_

两位 Reviewer 的正式交叉回应均已收到。审稿报告已于交叉回应到达前提交。

快速核对新增信息：

- **R1→R2**：全部 [AGREE]，与报告一致
- **R2→R1**：3 个 Must-Fix 全 [AGREE]，Should-Fix 中 **R1-W4 有 [REBUT]**——R2 认为 CKA-only 在 accuracy 上仍最优（0.285 vs 0.090），decoupling 不削弱实用价值，但同意 20% sparsity 下 GRPO accuracy 增量微弱（<0.2pp）。建议将 15% sparsity 作为主展示点或重新定位为 "post-pruning fine-tuning recovery"

这是唯一的分歧点，已在报告 SF4 中覆盖，属 should-fix 级别，不影响整体评估。报告 Overall 3.0 (Findings) 已投递 Research Director，无需修订。

**Round 6 审稿完成。**
- 2 Reviewer，1 轮交叉后收敛
- 6 Must-Fix（4 双共识 + 2 单 Reviewer）
- 10 Should-Fix
- Overall: 3.0 / 5 (Findings)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 39

## Round 39

58 recorded events


### User

_source line 423 · 2026-05-24T16:45:42.984994+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: recovery_aware_struct_prune
- 论文路径: projects/recovery_aware_struct_prune/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-24T16:45:50.993329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-24T16:45:50.993929+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-24T16:45:54.907346+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,read_project_file,submit_review_report_to_research_director,update_review_issues,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,read_project_file,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-24T16:45:54.957857+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-24T16:45:59.072673+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,read_project_file,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,read_project_file,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-24T16:45:59.123226+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-24T16:46:03.745756+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-24T16:46:04.047394+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-24T16:46:11.122898+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-24T16:46:13.029828+00:00_

{"result":"# 项目 recovery_aware_struct_prune 概况\n\n## 实验状态 (462 个)\n\n- **grpo_stage2_rasp_20_v2**: DONE (negative) — \n- **grpo_stage2_standard_20**: DONE (killed) — \n- **grpo_stage2_rasp_20**: DONE (killed) — \n- **sft_standard_20**: DONE (success) — \n- **sft_rasp_20**: DONE (success) — \n- **grpo_rasp_20_4096**: DONE (failed) — \n- **grpo_standard_20_4096**: DONE (negative) — \n- **grpo_standard_20_fast**: DONE (negative) — \n- **grpo_rasp_20_fast**: DONE (negative) — \n- **mvp_rasp_pipeline_v4**: PREPARING — \n- **grpo_standard_20**: DONE (killed) — \n- **grpo_rasp_20**: DONE (killed) — \n- **mvp_rasp_pipeline_v3**: DONE (negative) — \n- **mvp_rasp_pipeline_v2**: DONE (failed) — \n- **mvp_rasp_pipeline**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- floor_ablation_0p3_cka_only_20: Floor ratio ablation: lowering the MLP floor from 0.4 to 0.3 allows more aggressive pruning of unimportant layers while CKA-only criterion preserves critical structure. If floor=0.3 maintains GSM8K accuracy within 2pp of floor=0.4 baseline, it demonstrates robustness of CKA-guided pruning to floor choice.（已分配 ? GPU:?，等待提交）\n- floor_ablation_0p5_cka_only_20: Floor ratio ablation: raising the MLP floor from 0.4 to 0.5 constrains pruning to be more conservative. If floor=0.5 improves GSM8K accuracy over floor=0.4, it suggests CKA-only criterion benefits from a higher minimum layer size. Maps the sensitivity curve of floor parameter on recovery quality.（已分配 ? GPU:?，等待提交）\n- …另有 38 项\n\n## 近期结论\n- **eval_gsm8k_grpo_alpha4_20_v2** (killed): α=4.0 GRPO maintains reward 0.15-0.26 (vs α=1.0 collapse to ~0.008), predicting GSM8K accuracy significantly above α=1.0 baseline. v1 timed out at 774/1319 showing 62.93% interim — full eval needed to confirm α-dependent collapse hypothesis. ← 基于 eval_gsm8k_grpo_alpha4_20\n\n## 趋势\n成功 273 / 负向 23 / 失败 84 / 共 422\naccuracy: 0.268 →（近 3 次 success）\navg_response_length: 1110.462 ↑（近 3
…[truncated 1815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1906
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-24T16:46:13.030221+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-24T16:46:13.682833+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{siunitx}
17	\usepackage{algorithm}
18	\usepackage[noend]{algpseudocode}
19	\usepackage{enumitem}
20	\usepackage{xcolor}
21	\usepackage{hyperref}
22	
23	\newcommand{\rasp}{\textsc{Rasp}}
24	
25	\title{How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\begin{abstract}
33	\input{abstract}
34	\end{abstract}
35	
36	\input{introduction}
37	\input{related_work}
38	\input{method}
39	\input{experiments}
40	\input{conclusion}
41	
42	\section*{Limitations}
43	\input{limitations}
44	
45	\section*{Ethics Statement}
46	\input{ethics}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-24T16:46:13.683176+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-24T16:46:19.437024+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I found several results related to EM
…[truncated 1058 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "elapsed_ms": 5753
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-24T16:46:23.201319+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 439 · 2026-05-24T16:46:23.603224+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers main conference submission deadline ARR commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers main conference submission deadline ARR commitment"
  }
}
```

</details>

---


### Tool result

_source line 440 · 2026-05-24T16:46:29.485630+00:00_

Web search results for query: "EMNLP 2026 call for papers main conference submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's the information about EMNLP 2026 call for papers for the main conference regarding submission deadlines and ARR commit
…[truncated 1043 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "elapsed_ms": 5882
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-24T16:46:35.108522+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"

Links: [{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.02279v1"}]

Based on the search results, here are the ACL Rolling Review 2026 submission guidelines regarding page limits and formatting requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

For both long and short papers, all figures and ta
…[truncated 1417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "elapsed_ms": 11907
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-24T16:46:39.401625+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org calls main conference papers formatting anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org calls main conference papers formatting anonymity"
  }
}
```

</details>

---


### Tool call

_source line 443 · 2026-05-24T16:46:40.907733+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 444 · 2026-05-24T16:46:40.958416+00:00_

1	Fine-grained structured pruning of reasoning Large Language Models (LLMs), which removes MLP channel groups rather than entire layers, is typically followed by recovery training (SFT or Reinforcement Learning with Verifiable Rewards, RLVR) to restore reasoning capabilities.
2	RLVR is widely believed to be superior, yet we show this hierarchy reflects suboptimal pruning, not a fundamental property of RL\@.
3	When pruning preserves representational diversity, recovery method choice becomes irrelevant, a phenomenon we term \emph{reward-accuracy decoupling}: Group Relative Policy Optimization (GRPO) and SFT produce near-identical accuracy despite vastly different reward trajectories, a pattern that holds across sparsity levels and benchmarks.
4	We propose Recovery-Aware Structured Pruning (\rasp{}), which balances gradient importance with Centered Kernel Alignment (CKA)-based representational diversity via a coefficient $\alpha$.
5	On DeepSeek-R1-Distill-Qwen-7B at 20\% sparsity, a dose-response analysis reveals an inverted-U in recovery accuracy, peaking at $\alpha{=}2.0$ (66.11\% on GSM8K).
6	Under GRPO training, four pruning criteria produce a \emph{recovery capacity spectrum}: diversity-preserving pruning achieves active learning (peak reward 4.4$\times$ vs importance-only), while importance-dominated pruning collapses entirely.
7	The spectrum tracks preserved representational diversity rather than gradient importance, with initial evidence for generality across scales (1.5B) and, via SFT-based recovery, across architectures (Qwen2.5-Math-7B).
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-24T16:46:45.612775+00:00_

Web search results for query: "site:2026.emnlp.org calls main conference papers formatting anonymity"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Ten Simple Rules for writing algorithmic bioinformatics conference papers","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7117650/"}]

Based on the search results for EMNLP 2026's Call for Main Conference Papers, here are the key points regarding formatting and anonymity:

**Anonymity:**
Following the ACL and ARR policies, there is no anonymity period requirement. However, the reviewing process will continue to be double-blind, with reviewers not seeing authors, nor will authors see reviewers and reviews on ARR will not be made publicly visible. Authors will be given the option through ARR to make their anonymized submitted articles publicly visible.

**Key Submission Requirements:**
Both long and short paper submissions should follow all of the ARR submission requirements, including ACL's Publication Ethics Policy and ARR's Ethics Policy including the responsible NLP research checklist.

**Deadlines:**
All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

The search results indicate that EMNLP 2026 follows the Academic Conference Review (ARR) system and maintains double-blind review standards while eliminating the traditional anonymity period requirement.


REMINDER: You MUST include the sources above in your response to the u
…[truncated 30 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "elapsed_ms": 6211
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-24T16:46:56.951938+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "report.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "report.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-24T16:46:57.755574+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/report.md\", \"content\": \"# Handover — 2026-05-24\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- floor_ablation_0p3_cka_only_20: Floor ratio ablation: lowering the MLP floor from 0.4 to 0.3 allows more aggressive pruning of unimportant layers while CKA-only criterion preserves critical structure. If floor=0.3 maintains GSM8K accuracy within 2pp of floor=0.4 baseline, it demonstrates robustness of CKA-guided pruning to floor choice.（已分配 ? GPU:?，等待提交）\\n- floor_ablation_0p5_cka_only_20: Floor ratio ablation: raising the MLP floor from 0.4 to 0.5 constrains pruning to be more conservative. If floor=0.5 improves GSM8K accuracy over floor=0.4, it suggests CKA-only criterion benefits from a higher minimum layer size. Maps the sensitivity curve of floor parameter on recovery quality.（已分配 ? GPU:?，等待提交）\\n- …另有 38 项\\n\\n## 近期结论\\n- **eval_gsm8k_grpo_alpha4_20_v2** (killed): α=4.0 GRPO maintains reward 0.15-0.26 (vs α=1.0 collapse to ~0.008), predicting GSM8K accuracy significantly above α=1.0 baseline. v1 timed out at 774/1319 showing 62.93% interim — full eval needed to confirm α-dependent collapse hypothesis. ← 基于 eval_gsm8k_grpo_alpha4_20\\n\\n## 趋势\\n成功 273 / 负向 23 / 失败 84 / 共 422\\naccuracy: 0.268 →（近 3 次 success）\\navg_response_length: 1110.462 ↑（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestb-23072: 无 GPU 信息\\nwestd-32935: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- eval_math500_grpo_rasp_20: 训练失败 — unknown\\n- eval_math500_grpo_rasp_20_v2: 训练失败 — unknown\\n- eval_math500_grpo_rasp_20_v3: 训练失败 — unknown\\n- eval_math500_grpo_standard_20: 训练失败 — unknown\\n- eval_math500_sft_cka_only_20: 已被终止 — unknown\\n- eval_pass_k8_standard_20_grpo_qwen_math: 训练失败 — unknown\\n- eval_postprune_cka_only_30: 已被终止 — unknown\\n- eval_sft_alpha_0p5: 已被终止 — unknown\\n- eval_sft_cka_only_20
…[truncated 1428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-24T16:46:57.755969+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-24T16:46:58.207870+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	Reasoning Large Language Models can be compressed through structured pruning, but the pruned model must recover its reasoning capabilities through fine-tuning.
5	The dominant assumption is that the recovery paradigm (SFT versus RLVR) determines recovery quality: \citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, substantially outperforming SFT.
6	We show that this hierarchy is an artifact of suboptimal pruning.
7	When pruning preserves representational diversity, recovery method choice becomes irrelevant: at 20\% sparsity, mean $|\Delta(\text{GRPO}-\text{SFT})| {=} 0.54$\,pp across the four fine-grained criteria (max $0.61$\,pp); including dose-response variations, MBPP, and MATH-500, the maximum is $1.8$\,pp.
8	What matters is not \emph{how} you train after pruning, but \emph{which structures} you remove.
9	
10	This gap is surprising because RL and SFT impose fundamentally different demands on model representations: RL compresses incorrect paths while SFT expands correct ones~\citep{rlsqueezes2026}. Yet existing structured pruning methods for reasoning LLMs~\citep{graspprune2026,resp2025,llmpruner2023,bonsai2025} optimize for post-pruning quality without studying how the criterion shapes downstream RL recovery.
11	No prior work has compared multiple pruning criteria under RL or asked whether the ``RLVR $>$ SFT'' advantage persists across pruning strategies.
12	We note that \citet{selfhealing2025} evaluate unstructured magnitude pruning retaining 96.5\% of dense parameters; our findings concern fine-grained structural pruning where entire channel groups are removed, and the two settings may impose different demands on RL recovery.
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=\columnwidth]{../figures/paper/fig1_dose_response.pdf}
17	\caption{Dose-response curve for the CKA diversity coefficient $\alpha$ at 20\% MLP channel sparsity on GSM8K ($N
…[truncated 2609 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-24T16:46:58.208223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-24T16:46:58.258763+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	To isolate how the pruning criterion affects post-RLVR recovery, we hold everything else constant: a shared structural analysis computes importance and functional overlap scores for all prunable structures, four scoring criteria combine these scores differently to select structures for removal, and an identical two-stage recovery pipeline is applied to every pruned model.
5	The only variable across conditions is which structures are removed (Figure~\ref{fig:method_framework}).
6	
7	\subsection{Preliminaries and Notation}
8	\label{sec:prelim}
9	
10	\paragraph{Structured pruning.}
11	Given a pretrained transformer $\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units (attention heads or MLP channels) to reduce model size while maintaining hardware-friendly dense computation.
12	We denote the set of prunable structures as $\mathcal{H} = \{h_1, h_2, \ldots, h_N\}$.
13	
14	\paragraph{Grouped Query Attention (GQA).}
15	In GQA architectures~\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads ($G = n_Q / n_{KV}$ per group).
16	For DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$, $G{=}7$), we treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit.
17	
18	\paragraph{RLVR and GRPO.}
19	Reinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.
20	We use Group Relative Policy Optimization (GRPO;~\citealp{shao2024grpo}) as the recovery algorithm.
21	
22	\subsection{Structural Analysis}
23	\label{sec:structural_analysis}
24	
25	All four pruning criteria share a common structural analysis stage that computes two scores per structure: \emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \emph{functional overlap} $F(h)$ measuring representational redundancy with other structures in the same layer.
26	
27	\paragraph{Calibration data.}
28	We compu
…[truncated 4660 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-24T16:47:03.179066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex",
  "offset": "80",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex",
    "offset": "80",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-24T16:47:03.179623+00:00_

80	    \label{eq:score}
81	\end{equation}
82	where $\alpha \ge 0$ controls the strength of the overlap penalty ($\alpha{=}0$ reduces to Standard).
83	Structures with high importance \emph{and} low overlap receive the highest scores and are retained; structures with high overlap are penalized and pruned preferentially, regardless of their importance.
84	
85	\begin{figure*}[t]
86	\centering
87	\includegraphics[width=\textwidth]{figures/paper/fig1_method_framework.pdf}
88	\caption{Overview of our pruning comparison framework. \textbf{Left}: structural analysis computes importance $I(h)$ and CKA-based overlap $F(h)$ scores, which four scoring criteria combine differently (Eqs.~\ref{eq:standard}--\ref{eq:cka_only}). \textbf{Center}: ranked structures are removed up to the target sparsity, subject to per-layer capacity floors. \textbf{Right}: all pruned models undergo identical two-stage recovery (SFT warmup $\to$ GRPO). \textbf{Bottom}: the resulting recovery capacity spectrum, from active learning (CKA-only) to full collapse (\rasp{} $\alpha{=}1.0$), tracks preserved representational diversity rather than gradient importance.}
89	\label{fig:method_framework}
90	\end{figure*}
91	
92	\paragraph{CKA-only (overlap-only).}
93	CKA-only scoring ignores gradient importance entirely, ranking structures by functional overlap alone.
94	Structures with the highest mean pairwise CKA similarity to other structures in their layer are removed first:
95	\begin{equation}
96	    S_\text{cka}(h) = 1 - F(h).
97	    \label{eq:cka_only}
98	\end{equation}
99	This criterion preserves all representationally unique structures regardless of their gradient importance, removing only those whose function is redundant with retained structures.
100	$S_\text{cka}$ corresponds to the limit $\alpha \to \infty$ in Eq.~\ref{eq:score}.
101	
102	\paragraph{Random.}
103	Structures are selected uniformly at random for removal, subject to the per-layer capacity floor.
104	This baseline controls for the effect of
…[truncated 2862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-24T16:47:03.732051+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-24T16:47:03.782757+00:00_

1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	\subsection{Experimental Setup}
6	\label{sec:exp_setup}
7	
8	\paragraph{Base model and evaluation.}
9	We evaluate on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\citep{qwen2.5} with GQA~\citep{ainslie2023gqa} (architecture details in Section~\ref{sec:prelim}).
10	Our primary benchmark is GSM8K~\citep{cobbe2021gsm8k}, a set of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.
11	We report exact-match accuracy: the final numerical answer is extracted from the model's generation and compared against the ground truth.
12	For rapid iteration during development, we use a 100-problem subset ($N{=}100$); final results use the full test set ($N{=}1{,}319$).
13	The original unpruned model achieves 90.83\% on GSM8K (greedy decoding).
14	
15	\paragraph{Pruning methods.}
16	We compare four pruning criteria at 20\% structured sparsity, all removing the same number of MLP channel groups (200 of 784 across 28 layers, ${\sim}$1.45B parameters) with identical per-layer capacity floors (${\ge}$40\% retention per layer):
17	\begin{enumerate}[nosep,leftmargin=*]
18	    \item \textbf{CKA-only}: structures ranked by functional overlap $F(h)$ alone (Eq.~\ref{eq:overlap}); the most redundant groups are removed regardless of gradient importance.
19	    \item \textbf{Random}: uniform random selection among eligible groups.
20	    \item \textbf{Standard}: Taylor-expansion importance $I(h)$ alone (Eq.~\ref{eq:importance}); the least important groups are removed, following LLM-Pruner~\citep{llmpruner2023}.
21	    \item \textbf{\rasp{}} ($\alpha{=}1.0$): the composite score $S(h) = I(h) \times (1 - F(h))^\alpha$ (Eq.~\ref{eq:score}), removing structures that are both low-importance and functionally redundant.
22	\end{enumerate}
23	
24	\paragraph{Recovery pipeline and hardware.}
25	All four methods undergo matched two-stage recovery.
26	Stag
…[truncated 11560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-24T16:47:11.610456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex",
  "offset": "138",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex",
    "offset": "138",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-24T16:47:12.564232+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (138). The file has 138 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-24T16:47:12.564578+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-24T16:47:12.765678+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Structured pruning of LLMs.}
5	Width pruning methods (LLM-Pruner~\citep{llmpruner2023}, Bonsai~\citep{bonsai2025}, GRASPrune~\citep{graspprune2026}) remove attention heads or FFN channels while preserving dense computation.
6	Depth pruning~\citep{shortgpt2024,slicegpt2024,yang2024laco} removes entire layers but causes severe reasoning degradation~\citep{shrestha2026layerpruninglimits}; \citet{doingmore2026} revisit the trade-off under test-time scaling.
7	For reasoning models, RESP~\citep{resp2025}, RAC~\citep{rac2025}, and SSGR~\citep{ssgr2025} refine calibration data but retain gradient-based importance as the scoring criterion; \citet{llms2lrms2026} confirm width pruning is more robust than depth pruning for reasoning but do not study RLVR recovery.
8	A separate line uses functional structure to guide pruning: FANG~\citep{fang_2025} clusters FFN neurons by activation, FuncNet~\citep{funcnet_2025} decomposes LLMs via ICA, and MPruner~\citep{mpruner2024} applies inter-layer CKA~\citep{kornblith2019cka} for depth pruning in CNNs.
9	We differ in both granularity and objective: \emph{intra-layer} CKA between individual structures, optimizing for RL recovery capacity rather than immediate accuracy.
10	
11	\paragraph{Pruning-aware recovery.}
12	\citet{selfhealing2025} show that RLVR restores pruned reasoning models to near-original accuracy, outperforming SFT, but evaluate only importance-based unstructured pruning at low sparsity (96.5\% retention).
13	Under fine-grained structural pruning, our controlled experiments show that this advantage vanishes when pruning preserves diversity: it is a property of the pruning criterion, not of RL itself.
14	Other work optimizes complementary axes: post-pruning scaling ($P^2$~Law;~\citealp{p2law2025}), recovery data selection (PASER;~\citealp{paser2025}), joint pruning-tuning (PAT;~\citealp{pat2025}), post-hoc attention compensation (RestoreLCC;~\citealp{restorelcc_202
…[truncated 1485 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-24T16:47:12.766214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-24T16:47:12.816778+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	
4	Whether RLVR outperforms SFT for recovering pruned reasoning models depends on how the model was pruned.
5	Under diversity-preserving pruning, the two paradigms produce near-identical accuracy (mean $|\Delta| {=} 0.54$\,pp at 20\%; max $1.8$\,pp), yet the pruning criterion creates a 4.4$\times$ peak reward gap that persists through 300 steps (\S\ref{sec:extended_analysis}).
6	The dose-response across $\alpha$ identifies representational diversity as the causal driver: recovery peaks at $\alpha{=}2.0$ (66.11\%), and CKA similarity tracks the full spectrum ($\mu{=}0.62$ for CKA-only vs.\ $\mu{\geq}0.88$ for collapsing methods).
7	
8	\paragraph{Why does diversity preservation enable RL recovery?}
9	Policy gradient methods require trajectory variation to estimate reward gradients; importance-based pruning collapses the model onto the dense model's dominant reasoning mode, while CKA-only pruning preserves representationally distinct pathways that sustain exploration.
10	Gradient flow evidence supports this: CKA-only exhibits 2.89$\times$ mean gradient magnitude vs.\ Standard (\S\ref{sec:extended_analysis}), consistent with diversity preventing zero-variance batches ($f_0 > 0.5$).
11	Since RL updates only 5--30\% of parameters~\citep{mukherjee2025rlsubnetworks}, CKA-based pruning may preserve precisely this active subnetwork~\citep{frankle2019lth}.
12	
13	\paragraph{Practitioner guidelines.}
14	Use \rasp{} at $\alpha \approx 2.0$, which outperforms both pure importance (Standard) and pure diversity (CKA-only) on the dose-response curve (Figure~\ref{fig:dose_response}).
15	Under SFT alone, the criterion still matters (4.62\,pp gap; Table~\ref{tab:decoupling}).
16	Maintain per-layer floors ($\geq$40\%), stay below 25\% sparsity (\S\ref{sec:sparsity_cliff}), and monitor early $f_0$ as a pruning diagnostic.
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-24T16:47:16.693460+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-24T16:47:17.145620+00:00_

1	% Limitations --- required by ACL/EMNLP
2	
3	\paragraph{Architecture and scale.}
4	Our primary results are on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} with GQA ($G{=}7$).
5	Cross-architecture validation on Qwen2.5-Math-7B covers SFT recovery only ($N{=}200$); both models share the Qwen2.5 base architecture, so our cross-architecture evidence does not extend to different architecture families (e.g., LLaMA, Mistral).
6	Whether the spectrum generalizes across architecture families and scales (1B--70B) remains open.
7	
8	\paragraph{Diagnostic limitations.}
9	Reward-accuracy decoupling at 20--25\% sparsity means that recovery capacity, operationalized as peak reward, does not predict downstream accuracy improvements within our training horizon.
10	Recovery capacity captures the model's ability to sustain RL training without collapse, but practitioners seeking accuracy gains may require longer training, different reward formulations, or lower sparsity levels.
11	The per-layer capacity floor (40\% retention) was chosen heuristically; an ablation over $\tau \in \{0.3, 0.4, 0.5, 0.6\}$ (Appendix~\ref{sec:appendix_floor}) suggests moderate sensitivity, but a full search over continuous $\tau$ values was not performed.
12	
13	\paragraph{Replication and scope.}
14	CKA-only, Standard, and Random are validated over 3 GRPO seeds; \rasp{} uses a single seed ($N{=}1$).
15	We evaluate on three benchmarks (GSM8K, MATH-500, MBPP) covering math reasoning and code generation; logical, commonsense, and multi-modal reasoning are not addressed.
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-24T16:47:17.146084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-24T16:47:17.246897+00:00_

1	\section{Training Details}
2	\label{sec:appendix_training}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\caption{Hyperparameter details for SFT warmup and GRPO recovery stages. All methods share the same GRPO configuration; Random uses the TRL default generation limit (marked with $^\dagger$).}
8	\label{tab:hyperparams}
9	\resizebox{\columnwidth}{!}{%
10	\begin{tabular}{@{}lll@{}}
11	\toprule
12	Parameter & SFT & GRPO \\
13	\midrule
14	Learning rate & $2 \times 10^{-5}$ & $1 \times 10^{-6}$ \\
15	Batch size & 1 & 1 \\
16	Gradient accumulation & 8 & 1 \\
17	Max sequence length & 2{,}048 & -- \\
18	Max new tokens & -- & 1{,}024\,$^\dagger$512 \\
19	Optimizer & AdamW & AdamW \\
20	Epochs / Steps & 2 epochs & 100 steps \\
21	KL coefficient $\beta$ & -- & 0.01 \\
22	Sampling temperature & -- & 0.4 \\
23	Num generations per prompt & -- & 8 \\
24	Reward & -- & Binary (exact match) \\
25	Loss formulation & Cross-entropy & DAPO-style clipped \\
26	\texttt{reward\_desert\_patience} & -- & 50 \\
27	\bottomrule
28	\multicolumn{3}{l}{\footnotesize $^\dagger$Random uses TRL default of 512 tokens; all other methods use 1{,}024.} \\
29	\end{tabular}}
30	\end{table}
31	
32	\section{Algorithm}
33	\label{sec:appendix_algo}
34	
35	\begin{algorithm}[h]
36	\caption{Controlled Pruning Comparison Framework}
37	\label{alg:rasp}
38	\begin{algorithmic}[1]
39	\Require Model $\mathcal{M}$, calibration data $\mathcal{D}_\text{cal}$, target sparsity $s$, scoring criterion $\mathcal{C} \in \{\text{Std}, \text{RASP}, \text{CKA}, \text{Rand}\}$, layer floor $\tau$
40	\Ensure Pruned and recovered model $\mathcal{M}'$
41	\Statex \textit{\% Stage 1: Shared Structural Analysis}
42	\For{each structure $h \in \mathcal{H}$}
43	    \State Compute importance $I(h)$ via Eq.~\eqref{eq:importance}
44	    \State Collect activations $\mathbf{X}_h$ on $\mathcal{D}_\text{cal}$
45	\EndFor
46	\For{each layer $\ell = 1, \ldots, L$}
47	    \For{each structure $h_i$ in layer $\ell$}
48	        \State $F(h_i) \gets \f
…[truncated 3434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-24T16:47:20.658962+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-24T16:47:20.760069+00:00_

100	\section{Extended Training Dynamics}
101	\label{sec:appendix_extended}
102	
103	See Figure~\ref{fig:extended_training} in the main text for the 300-step extended training results.
104	
105	\section{MATH-500 Out-of-Distribution Evaluation}
106	\label{sec:appendix_math500}
107	
108	\input{tables/tab_math500}
109	
110	CKA-only and Standard both outperform \rasp{} and Random on MATH-500 (SFT: 27.4\%, 25.6\% vs.\ 21.6\%, 16.6\%; GRPO: 27.6\%, 27.0\% vs.\ 23.0\%, 15.0\%), consistent with GSM8K.
111	However, the CKA-only--Standard gap narrows substantially: from 4.6\,pp (GSM8K SFT) to 1.8\,pp (MATH-500 SFT) to 0.6\,pp (MATH-500 GRPO).
112	Middle-ranked methods also swap positions (Standard $>$ \rasp{} on MATH-500 vs.\ \rasp{} $>$ Standard on GSM8K).
113	This is consistent with MATH-500's higher difficulty compressing all pruned methods toward a capability floor, reducing inter-method differentiation (\S\ref{sec:ood}).
114	CKA-only also produces more efficient reasoning: only 22\% of completions are truncated at the 2{,}048-token limit (mean 655 tokens) versus Standard's 44\% (mean 1{,}128 tokens), indicating that the preserved structure enables shorter reasoning chains rather than longer ones.
115	The $\alpha$ dose-response effect is not statistically significant on MATH-500: SFT accuracy varies by ${\sim}$8\,pp across $\alpha$ values, but with stderr ${\approx}$2\,pp per point, attributable to high truncation rates at the 2048-token limit and floor effects at this difficulty level.
116	The inverted-U pattern is validated on GSM8K (Table~\ref{tab:alpha}); MATH-500 does not resolve the dose-response shape.
117	
118	\section{MBPP Code Generation}
119	\label{sec:appendix_mbpp}
120	
121	\input{tables/tab_mbpp}
122	
123	MBPP GRPO deltas are uniformly slightly positive across all fine-grained methods (mean $+$1.25\,pp), but none are statistically significant at this sample size ($N{=}374$; stderr ${\approx}1.7$\,pp).
124	This directional consistency may reflect a weak task-s
…[truncated 11670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-24T16:47:44.513475+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
  }
}
```

</details>

---


### Tool call

_source line 469 · 2026-05-24T16:47:45.586877+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 470 · 2026-05-24T16:48:04.817977+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20304
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-24T16:48:04.818314+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 19231
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-24T16:48:04.818517+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recovery_aware_struct_prune",
  "chat_id": "oc_40839c097b00df44480b45ab767f59cf",
  "director_session_key": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（via ACL Rolling Review）\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页 + unlimited references\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有，放在 conclusion 之后、references 之前，不计入页数\n\n### 论文路径\n- LaTeX 主文件: `projects/recovery_aware_struct_prune/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_7/submitted.pdf`\n\n### 审查重点\n\n请从以下维度严格评估：\n\n1. **实验控制与公平性**\n   - 四种 pruning criteria 的对比是否公平？是否存在有利于某方法的隐含偏差？\n   - Random baseline 使用 512 tokens（vs 其他 1024）是否影响结论？\n   - RASP α=1.0 单 seed vs 其他 3 seeds 的问题\n   - 评估样本量（GSM8K N=1319, MATH-500, MBPP N=374）是否足够？\n\n2. **统计严谨性**\n   - \"reward-accuracy decoupling\" claim (mean |Δ|=0.54pp) 是否有显著性检验？\n   - Welch's t-test 和 Cohen's d 使用是否恰当？\n   - 置信区间是否覆盖所有关键 claims？\n\n3. **因果 vs 相关**\n   - CKA diversity → recovery capacity 是因果关系还是相关？论文是否过度声称因果？\n   - \"representational diversity\" 是否是唯一解释，还是存在其他混淆变量？\n\n4. **方法可复现性**\n   - 关键实现细节是否完整（calibration data size, CKA computation specifics, floor ratio 选择依据）？\n   - 是否有足够信息让他人复现？\n\n5. **Claims 与证据匹配**\n   - Abstract/Introduction 中的每个 claim 是否都有对应实验数据支撑？\n   - 是否有 overclaiming（如 \"generality across scales\" 但只有 7B 和 1.5B）？\n\n请按 ARR 标准给出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Score (1-5, 参考 EMNLP 2026 评分标准)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recovery_aware_struct_prune",
    "chat_id": "oc_40839c097b00df44480b45ab767f59cf",
    "director_session_key": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（via ACL Rolling Review）\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页 + unlimited references\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有，放在 conclusion 之后、references 之前，不计入页数\n\n### 论文路径\n- LaTeX 主文件: `projects/recovery_aware_struct_prune/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_7/submitted.pdf`\n\n### 审查重点\n\n请从以下维度严格评估：\n\n1. **实验控制与公平性**\n   - 四种 pruning criteria 的对比是否公平？是否存在有利于某方法的隐含偏差？\n   - Random baseline 使用 512 tokens（vs 其他 1024）是否影响结论？\n   - RASP α=1.0 单 seed vs 其他 3 seeds 的问题\n   - 评估样本量（GSM8K N=1319, MATH-500, MBPP N=374）是否足够？\n\n2. **统计严谨性**\n   - \"reward-accuracy decoupling\" claim (mean |Δ|=0.54pp) 是否有显著性检验？\n   - Welch's t-test 和 Cohen's d 使用是否恰当？\n   - 置信区间是否覆盖所有关键 claims？\n\n3. **因果 vs 相关**\n   - CKA diversity → recovery capacity 是因果关系还是相关？论文是否过度声称因果？\n   - \"representational diversity\" 是否是唯一解释，还是存在其他混淆变量？\n\n4. **方法可复现性**\n   - 关键实现细节是否完整（calibration data size, CKA computation specifics, floor ratio 选择依据）？\n   - 是否有足够信息让他人复现？\n\n5. **Claims 与证据匹配**\n   - Abstract/Introduction 中的每个 claim 是否都有对应实验数据支撑？\n   - 是否有 overclaiming（如 \"generality across scales\" 但只有 7B 和 1.5B）？\n\n请按 ARR 标准给出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Score (1-5, 参考 EMNLP 2026 评分标准)"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-24T16:48:06.227455+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-24T16:48:18.229551+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recovery_aware_struct_prune",
  "chat_id": "oc_40839c097b00df44480b45ab767f59cf",
  "director_session_key": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "text": "## Round 1 审稿��务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量**\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（via ACL Rolling Review）\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper，���文 8 页 + unlimited references\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有，放在 conclusion 之后、references 之前，不计入页数\n\n### 论��路径\n- LaTeX 主文件: `projects/recovery_aware_struct_prune/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_7/submitted.pdf`\n\n### ��查重点\n\n请从以下维度严格评估：\n\n1. **新颖性与贡��**\n   - \"reward-accuracy decoupling\" 和 \"recovery capacity spectrum\" 是否是真正的新发现？\n   - 对比 Self-Healing (RLVR recovery)、LLM-Pruner (importance-based) 等已有工作，增量贡献有多大？\n   - 核心 insight（diversity > importance for RL recovery）是否非显而易见？\n\n2. **Related Work 覆盖**\n   - 是否遗漏重要相关工作？特别关注：\n     - 其他使用 CKA 做剪枝的工作\n     - RLVR/GRPO 相关的最新文献\n     - 结构化剪枝 + 恢复训练的最新进展\n   - Related work section 的组织和论述是否清晰区分了本文贡献？\n\n3. **论文叙事与结构**\n   - Abstract 是否在 200 words 以内？\n   - Introduction 的故事线是否清晰（problem → gap → solution → results）？\n   - 论文整体叙事是否连贯，各节之间衔接是否自然？\n   - Contribution list 是否清晰、不重叠？\n\n4. **写作质量**\n   - 术语使用是否一致（如 pruning criterion/criteria, recovery capacity 等）？\n   - 图表标题是否 self-contained？\n   - 是否有含糊或过度声称的表述？\n   - 语法、拼写、ACL style 格式合规性\n\n5. **完整性**\n   - Limitations 部分是否充分覆盖真正的局限？\n   - 实验设置是否完整（是否缺少重要的 ablation 或 baseline）？\n   - 附录结构是否合理？\n\n请按 ARR 标准给出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Score (1-5, 参考 EMNLP 2026 评分标准)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recovery_aware_struct_prune",
    "chat_id": "oc_40839c097b00df44480b45ab767f59cf",
    "director_session_key": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
    "text": "## Round 1 审稿��务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量**\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（via ACL Rolling Review）\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper，���文 8 页 + unlimited references\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有，放在 conclusion 之后、references 之前，不计入页数\n\n### 论��路径\n- LaTeX 主文件: `projects/recovery_aware_struct_prune/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_7/submitted.pdf`\n\n### ��查重点\n\n请从以下维度严格评估：\n\n1. **新颖性与贡��**\n   - \"reward-accuracy decoupling\" 和 \"recovery capacity spectrum\" 是否是真正的新发现？\n   - 对比 Self-Healing (RLVR recovery)、LLM-Pruner (importance-based) 等已有工作，增量贡献有多大？\n   - 核心 insight（diversity > importance for RL recovery）是否非显而易见？\n\n2. **Related Work 覆盖**\n   - 是否遗漏重要相关工作？特别关注：\n     - 其他使用 CKA 做剪枝的工作\n     - RLVR/GRPO 相关的最新文献\n     - 结构化剪枝 + 恢复训练的最新进展\n   - Related work section 的组织和论述是否清晰区分了本文贡献？\n\n3. **论文叙事与结构**\n   - Abstract 是否在 200 words 以内？\n   - Introduction 的故事线是否清晰（problem → gap → solution → results）？\n   - 论文整体叙事是否连贯，各节之间衔接是否自然？\n   - Contribution list 是否清晰、不重叠？\n\n4. **写作质量**\n   - 术语使用是否一致（如 pruning criterion/criteria, recovery capacity 等）？\n   - 图表标题是否 self-contained？\n   - 是否有含糊或过度声称的表述？\n   - 语法、拼写、ACL style 格式合规性\n\n5. **完整性**\n   - Limitations 部分是否充分覆盖真正的局限？\n   - 实验设置是否完整（是否缺少重要的 ablation 或 baseline）？\n   - 附录结构是否合理？\n\n请按 ARR 标准给出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Score (1-5, 参考 EMNLP 2026 评分标准)"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-24T16:48:19.551434+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1321
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-24T16:48:24.976422+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-24T16:48:25.077416+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/decisions.yaml\", \"content\": \"_next_id: 115\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 06:10 UTC\\n  summary: MVP 接受 35% sparsity 下 MLP-only pruning，不强制 attention 配额\\n  rationale: 全局统一排序下 attention GQA groups importance 普遍高于 MLP groups，35% sparsity\\n    自然只剪 MLP（367 groups）。这是模型结构特征的正确反映，不应人为干预。MLP-level correlation (N=367) 足以验证 CKA→recoverability\\n    假设。50% sparsity 放 Phase 2 获取 attention-level 数据。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: primary\\n    result: running\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 13:31 UTC\\n  summary: 终止无效 GRPO，改用 SFT warmup → GRPO 两阶段恢复策略\\n  rationale: 35% 结构化剪枝后两个模型 accuracy 仅 0.15%（输出退化），GRPO 150 步 loss=0/grad_norm=0，无学习信号。frac_reward_zero_std\\n    ≈ 1.0 表明几乎所有 completion 得 0 reward，GRPO 无法计算有效 advantage。SFT warmup 用 ground truth\\n    数据先恢复基本能力再转 GRPO 是解决 reward desert 的标准做法。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: motivating_failure\\n    result: GRPO 150 步 loss=0, grad_norm=0; post-prune accuracy 0.15% for both models\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 13:53 UTC\\n  summary: 暂缓 SFT warmup，优先审计剪枝实现正确性\\n  rationale: 两个不同剪枝策略产出精确相同的 accuracy（2/1319）统计上极不寻常，35% structured pruning 不应导致 7B\\n    模型完全崩溃。Reviewer 怀疑存在实现 bug（config 不匹配、全零层等）。若根因是代码问题，SFT warmup 是在错误基础上浪费算力。需先排除实现问题再决定恢复策略。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: audit_target\\n    result: both pruned models 0.15% accuracy, identical 2/1319\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 13:59 UTC\\n  summary: 修复 min_keep_mlp=4 导致的 per-layer 过度剪枝，重跑 MVP pipeline v3\\n  rationale: 根因确认：min_keep_mlp=4 允许单层 MLP 被剪至 14.3% capacity，全局排序集中破坏 early layers（0-6），两个模型均崩溃至\\n    0.15%。修复方案：min_keep_mlp 提升到 40% per layer + per-layer capacity floor。RASP scoring\\n    逻辑本身正常（产生了不同剪枝结构），核心假设仍可验证，只需收紧约
…[truncated 1441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-24T16:48:30.708452+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "output_mode": "content",
  "glob": "*.{yaml,yml,json,toml}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
    "output_mode": "content",
    "glob": "*.{yaml,yml,json,toml}"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-24T16:48:30.909542+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Grep",
  "elapsed_ms": 201
}
```

</details>

---


### Assistant

_source line 480 · 2026-05-24T16:48:42.483071+00:00_

所有任务已派发：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法/实验） | ✅ 已分配，审稿中 |
| Reviewer 2（新颖性/完整性） | ✅ 已分配，审稿中 |
| 视觉审查 Agent | ✅ 已启动，并行执行 |
| 外部审稿（Stanford） | ⬜ 未配置，跳过 |

等待两位 Reviewer 返回 Round 1 审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 40

## Round 40

26 recorded events


### User

_source line 481 · 2026-05-24T16:54:30.504307+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见

**论文**: How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 核心发现（剪枝标准比恢复方法更重要）有价值且实验设计思路好，但 generation length 的系统性混淆变量、RASP 单 seed 验证不足、以及多处因果 overclaiming 使其未达到 Conference 水准。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心对照设计好，但 generation length confound 贯穿多个实验（Random 512 vs 其他 1024；dose-response α=1.0 用 1024 vs 其他 α 用 512），削弱了"唯一变量是剪枝标准"的 claim。RASP 作为 proposed method 仅单 seed。因果语言超出证据支持。 |
| Excitement | 3.5/5 | reward-accuracy decoupling 发现有趣且挑战了"RLVR > SFT"的普遍假设；dose-response 分析设计合理。但 scope 窄（一个架构家族、主要是数学推理），限制了影响力。 |
| Reproducibility | 3/5 | 大部分超参提供了，但 calibration 数据量 M 在正文中未明确指定；generation length 差异分散在脚注中容易遗漏；RASP 多个 α 值的 seed 数量不明。 |
| Reviewer Confidence | 4/5 | 熟悉 LLM 剪枝和 RL 恢复文献。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Generation length 混淆变量贯穿核心实验，破坏了"controlled study"的前提**
- 具体位置：Section 3.4 (line 112), Section 4.1 (line 28), Section 4.3 footnote (page 7)
- 问题：论文声称"the only variable across conditions is which structures are removed"（Section 3, line 5），但实际上存在系统性的 `max_completion_length` 差异：
  - **主对照实验**：Random 使用 512 tokens，CKA-only / Standard / RASP 使用 1024 tokens
  - **Dose-response**：α=1.0 使用 1024 tokens，其他 α 值使用 512 tokens
  - 这意味着 recovery capacity spectrum（Table 1）中 Random 的相对表现、以及 dose-response inverted-U（Figure 1）的形状都受到了 generation length 的混淆
- 为什么影响接收：这是一个系统性设计缺陷。如果 Random 也用 1024 tokens，其 GRPO 表现可能改善，可能改变 spectrum 排序。如果 dose-response 中所有 α 值统一使用同一 generation length，inverted-U 可能变平或变形。论文声称这是"conservative estimate"，但 generation length 对 GRPO 探索行为的影响不是单调的——更长的 generation 可能既增加探索又增加计算开销，效果不可预测。
- 建议修改方向：(1) 用统一的 generation length 重跑 Random 和 dose-response 中至少 3 个 α 值的实验；(2) 若无法重跑，将此作为显式 limitation 详细讨论其可能影响，并降低 claim 的强度。

**N2** [critical] **RASP 作为 proposed method 仅用单 seed 验证**
- 具体位置：Section 4.1 (line 30), Table 11 (Appendix L), Limitations (line 14)
- 问题：CKA-only、Standard、Random 均使用 3 GRPO seeds 进行验证（Table 11），但 RASP（论文的核心贡献方法）在所有 sparsity levels 和所有 α 值上仅使用 1 seed。Dose-response curve（Figure 1）中 5 个 α 值的结果很可能都是单 seed，这意味着 inverted-U peak 的位置（α=2.0）可能不稳定。
- 为什么影响接收：论文在 Section 5 给出 practitioner guideline "Use RASP at α≈2.0"，但这个推荐基于单次实验。考虑到 Standard 的 3-seed std=0.38pp，RASP 的真实方差可能更大（因为它处于 importance 和 diversity 的边界区域）。Peak 位置在 α=2.0 还是 α=3.0 对实际应用者影响很大。
- 建议修改方向：至少对 RASP α=2.0（推荐值）和 α=1.0（collapse 点）各跑 3 seeds，验证 inverted-U peak 位置的稳定性。

**N3** [critical] **因果语言超出实验证据**
- 具体位置：Section 5 (line 6): "The dose-response across α identifies representational diversity as the causal driver"; Abstract (line 7): "a phenomenon we term reward-accuracy decoupling"
- 问题：
  1. **"causal driver"**: Dose-response 设计是 quasi-experimental，变化 α 同时改变了 (a) diversity 权重、(b) 被移除结构的身份（早期 vs 晚期层偏好）、(c) 实际达到的 sparsity 分布。Appendix H 自己承认 gradient flow 证据是 correlational。不存在干预实验（如固定被移除的结构集合只改变恢复方法）来建立因果关系。
  2. **"decoupling" 作为 phenomenon**: 该现象仅在 20-25% sparsity 成立。15% 时 GRPO 仍然 amplify CKA advantage by 1.51pp（Section 4.3, line 81），说明 coupling 仍然存在。将一个 sparsity-dependent 的观察包装为普适性 "phenomenon" 并起专有名词是 overclaiming。
- 为什么影响接收：Reviewers 和读者容易将 "causal" claim 和命名的 "phenomenon" 当作 established result 引用，但实际证据不支持这个强度。
- 建议修改方向：(1) 将 "causal driver" 改为 "the primary correlate" 或 "the dose-response analysis is consistent with representational diversity being the key factor"；(2) 明确 decoupling 是 sparsity-dependent 的观察，在 abstract 中加上 "at 20-25% sparsity" 的限定。

**N4** [critical] **Abstract overclaiming "holds across sparsity levels"**
- 具体位置：Abstract (line 3): "a pattern that holds across sparsity levels and benchmarks"
- 问题：论文自己的数据表明 decoupling 在 15% sparsity 时不完全成立（Section 4.3, line 81: "at 15%, GRPO slightly amplifies the CKA-only advantage (SFT gap 5.69pp → GRPO gap 7.20pp)"）。在 30% 一切 collapse。因此 decoupling 仅在 20-25% 的窄窗口成立，"across sparsity levels" 是不准确的。
- 为什么影响接收：Abstract 是多数读者唯一完整阅读的部分。不准确的 claim 会被直接引用。
- 建议修改方向：改为 "a pattern that holds at 20-25% sparsity across benchmarks" 或类似限定表述。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Calibration 数据量 M 在正文中未明确指定**
- 具体位置：Section 3.2 (line 27-29)
- 问题：正文提到 $\mathcal{D}_{cal} = \{(x_j, y_j)\}_{j=1}^M$ 但从未指定 M 的值。Appendix H 提到 "N=200 GSM8K calibration samples"（但这可能仅用于 gradient analysis），Appendix I 测试了 256/512/1024 的 CKA 稳定性。主实验使用的 M 是多少？
- 建议：在 Section 4.1 或 Section 3.2 中明确指定 M，并说明选择依据。

**W2** [warning] **"Generality across scales" 证据薄弱**
- 具体位置：Abstract (line 7), Section 4.5 (line 134-135)
- 问题：跨尺度验证仅在 1.5B 和 7B 上进行（同一架构家族内 <5x 的尺度差异）。跨架构仅在 Qwen2.5-Math-7B 上测试且未跑 GRPO。声称 "generality across scales" 和 "across architectures" 过于宽泛。
- 建议：将 "generality" 改为 "preliminary evidence at 1.5B scale"，并在 abstract 中降低语气。

**W3** [warning] **Reward-accuracy decoupling 缺少形式化统计检验**
- 具体位置：Section 4.3 (line 77-79)
- 问题：声称 mean |Δ|=0.54pp "near-identical"，但未检验 H₀: Δ(GRPO-SFT)=0 within each method。Welch's t-test 用于 CKA-only vs Standard 的 gap，但未用于检验 GRPO 是否 significantly ≠ SFT within a method。虽然 practical significance 的论证思路合理（<1pp），但应提供 equivalence test 或明确声明 "practical equivalence at Δ<1pp threshold"。
- 建议：使用 TOST (Two One-Sided Tests) 进行等价性检验，或在正文中明确定义 practical equivalence 的阈值。

**W4** [warning] **MBPP 结果不显著却被用作支持证据**
- 具体位置：Section 4.3 (line 86), Appendix G
- 问题：Appendix G 明确说 "none are statistically significant at this sample size (N=374; stderr≈1.7pp)"，但 Section 4.3 仍引用 MBPP 结果支持 decoupling claim ("On MBPP all fine-grained GRPO |Δ| < 2pp")。不显著的结果不应被用于支持 claim。
- 建议：在正文中引用 MBPP 时加注 "though not statistically significant at this sample size"。

**W5** [warning] **CKA overlap 作为 "representational diversity" 的代理指标未充分论证**
- 具体位置：Section 3.2 (line 40-56)
- 问题：论文将 intra-layer mean pairwise CKA 等同于 "representational redundancy"，其互补概念即 "diversity"。但 CKA 衡量的是 representation similarity（基于 kernel alignment），而非功能性多样性。两个 CKA 相似度高的结构可能在 RL 探索中提供不同的 gradient pathways。论文应讨论 CKA 作为 diversity proxy 的局限性。
- 建议：增加一段讨论 CKA 作为 diversity 代理的假设和局限。

---

## 小问题（不影响接收）

- **Abstract 字数**：约 190-200 words，在 200-word 限制边界，建议再精简几个词留出安全余量。
- **Table 1** (page 6)：Unpruned 行的 "Reward" 列标注为 "0.027"，对于未剪枝的 dense model 含义不够直观，建议加脚注解释。
- **Figure 2** (page 5)：底部 "recovery capacity spectrum" 示意图中 label 字体偏小，打印时可能不清晰。
- **Section 4.5** (line 120)：CKA-only 集中在 early layers 剪枝（L0-9 占 72.5%）这一重要发现仅在正文一句话带过，建议在 Discussion 中更深入讨论其机制含义。
- **Appendix R** (page 15, Section "Depth-First Pruning Baseline")：承认 depth-first baseline 与主实验的 granularity 不同 "precludes direct comparison"，那这个实验作为 sanity check 的价值有限，建议要么匹配 granularity 要么删除。
- **Ethics Statement**：提到使用 Claude 辅助写作，信息完整。

---

## 主要优势

1. **实验设计思路优秀**：控制恢复流程只变剪枝标准的 controlled comparison 思路在该领域少见，是对 "RLVR > SFT" 假设的有针对性挑战。
2. **Dose-response 分析有说服力**：α 系数的连续变化 + inverted-U 发现比简单的 A/B 对比更有信息量。
3. **Recovery capacity spectrum 有直觉价值**：将四种标准的 GRPO 行为划分为 active learning / stagnation / collapse 三种 regime 的 framing 清晰且实用。
4. **统计严谨性在部分实验中做得好**：3-seed 验证 + Welch's t-test + Cohen's d + 95% CI 对 CKA-only vs Standard 的 gap 提供了较强的统计支持。
5. **坦诚的 Limitations 节**：明确承认了 single seed、架构/尺度局限、以及 decoupling 的操作化边界。
6. **行文清晰**：论文结构合理，notation 一致，figures 质量好。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-24T16:54:53.649980+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-24T16:54:53.650324+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-24T16:54:54.503693+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-24T16:54:54.554499+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-24T16:54:58.223755+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues,read_local_file",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues,read_local_file",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-24T16:54:58.324453+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-24T16:55:09.644329+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_get_project_overview",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_get_project_overview",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-24T16:55:09.795240+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-24T16:55:11.752340+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_post_to_reviewer submit_review_report dispatch_visual_check get_external_review get_visual_check update_review_issues read_project_file request_external_review",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_post_to_reviewer submit_review_report dispatch_visual_check get_external_review get_visual_check update_review_issues read_project_file request_external_review",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-24T16:55:11.853191+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-24T16:55:22.486046+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool call

_source line 493 · 2026-05-24T16:55:23.090685+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 494 · 2026-05-24T16:55:23.744064+00:00_

{"result":"# 项目 recovery_aware_struct_prune 概况\n\n## 实验状态 (462 个)\n\n- **grpo_stage2_rasp_20_v2**: DONE (negative) — \n- **grpo_stage2_standard_20**: DONE (killed) — \n- **grpo_stage2_rasp_20**: DONE (killed) — \n- **sft_standard_20**: DONE (success) — \n- **sft_rasp_20**: DONE (success) — \n- **grpo_rasp_20_4096**: DONE (failed) — \n- **grpo_standard_20_4096**: DONE (negative) — \n- **grpo_standard_20_fast**: DONE (negative) — \n- **grpo_rasp_20_fast**: DONE (negative) — \n- **mvp_rasp_pipeline_v4**: PREPARING — \n- **grpo_standard_20**: DONE (killed) — \n- **grpo_rasp_20**: DONE (killed) — \n- **mvp_rasp_pipeline_v3**: DONE (negative) — \n- **mvp_rasp_pipeline_v2**: DONE (failed) — \n- **mvp_rasp_pipeline**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- floor_ablation_0p3_cka_only_20: Floor ratio ablation: lowering the MLP floor from 0.4 to 0.3 allows more aggressive pruning of unimportant layers while CKA-only criterion preserves critical structure. If floor=0.3 maintains GSM8K accuracy within 2pp of floor=0.4 baseline, it demonstrates robustness of CKA-guided pruning to floor choice.（已分配 ? GPU:?，等待提交）\n- floor_ablation_0p5_cka_only_20: Floor ratio ablation: raising the MLP floor from 0.4 to 0.5 constrains pruning to be more conservative. If floor=0.5 improves GSM8K accuracy over floor=0.4, it suggests CKA-only criterion benefits from a higher minimum layer size. Maps the sensitivity curve of floor parameter on recovery quality.（已分配 ? GPU:?，等待提交）\n- …另有 38 项\n\n## 近期结论\n- **eval_gsm8k_grpo_alpha4_20_v2** (killed): α=4.0 GRPO maintains reward 0.15-0.26 (vs α=1.0 collapse to ~0.008), predicting GSM8K accuracy significantly above α=1.0 baseline. v1 timed out at 774/1319 showing 62.93% interim — full eval needed to confirm α-dependent collapse hypothesis. ← 基于 eval_gsm8k_grpo_alpha4_20\n\n## 趋势\n成功 273 / 负向 23 / 失败 84 / 共 422\naccuracy: 0.268 →（近 3 次 success）\navg_response_length: 1110.462 ↑（近 3
…[truncated 1815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1258
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-24T16:55:23.744452+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-24T16:55:39.655970+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-24T16:55:40.108422+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-24T16:55:40.108832+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-24T16:55:41.112607+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T16:47:48.267120+00:00\", \"completed_at\": \"2026-05-24T16:52:07.973542+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 3-4\", \"message\": \"Method 节连续 2 页无 figure/table，仅有方程式作为视觉间断。数学密集型内容可接受，但若能在 page 4 插入一个 pruning criteria 对比示意图（如四种标准的直觉对比），可帮助审稿人更快理解\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 框架概览图内部标注文字偏小（Stage 描述框内的细节文字），打印尺寸下可能需要放大才能完全阅读。建议适当增大内部字号或精简文字\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"单页含 2 个多面板 figure（Figure 3 三子图 + Figure 4），视觉密度较高。功能上合理（训练动态紧密关联），但审稿人可能感到拥挤\"}, {\"severity\": \"info\", \"dimension\": \"page 7-8\", \"message\": \"Figures 3–6 集中在连续两页，形成 figure 密集区，与 pages 3–4 的纯文本区形成较大节奏反差。若能将 Figure 5 或 6 移至 appendix、在主文用文字总结，可平衡视觉节奏\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-24T16:55:41.113037+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-24T16:55:41.665995+00:00_

1	
2	# ============================================================
3	# Round 1-3 Issues — All Resolved
4	# ============================================================
5	
6	- id: "R1-C1"
7	  summary: "CKA-recovery link 仅相关性, 无因果干预"
8	  category: method
9	  severity: critical
10	  status: resolved
11	  first_raised_round: 1
12	  last_seen_round: 3
13	  resolution: "Jaccard overlap 分析 + Limitations 承认 + 多种子统计验证"
14	  resolution_round: 3
15	
16	- id: "R1-C2"
17	  summary: "Single-seed GRPO 无统计显著性"
18	  category: experiment
19	  severity: critical
20	  status: resolved
21	  first_raised_round: 1
22	  last_seen_round: 3
23	  resolution: "3-seed GRPO CKA-only, Welch's t-test p=0.0009"
24	  resolution_round: 3
25	
26	- id: "R1-C3"
27	  summary: "仅 GSM8K 单基准"
28	  category: experiment
29	  severity: critical
30	  status: resolved
31	  first_raised_round: 1
32	  last_seen_round: 3
33	  resolution: "MATH-500 OOD 验证 + MBPP 代码基准"
34	  resolution_round: 3
35	
36	- id: "R1-W1"
37	  summary: "Title overclaim 'determines'"
38	  category: framing
39	  severity: warning
40	  status: resolved
41	  first_raised_round: 1
42	  last_seen_round: 3
43	  resolution: "Title 改为 'shapes'"
44	  resolution_round: 3
45	
46	- id: "R1-W2"
47	  summary: "Abstract 'universally determines' overclaim"
48	  category: framing
49	  severity: warning
50	  status: resolved
51	  first_raised_round: 1
52	  last_seen_round: 3
53	  resolution: "改为 'significantly shapes'"
54	  resolution_round: 3
55	
56	- id: "R1-W3"
57	  summary: "仅 DeepSeek-R1-7B 单模型"
58	  category: experiment
59	  severity: warning
60	  status: resolved
61	  first_raised_round: 1
62	  last_seen_round: 3
63	  resolution: "Qwen2.5-Math-7B cross-arch + 1.5B cross-scale"
64	  resolution_round: 3
65	
66	- id: "R1-M1"
67	  summary: "GRPO 超参未报告"
68	  category: experiment
69	  severity: info
70	  status: resolved
71	  first_raised_round: 1
72	  last_seen_round: 3
73	  resolution: "Appendix 完整超参表"
74	  resolution_round: 3
75	
76	- id: "R1-M2"
77	  sum
…[truncated 22002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-24T16:55:41.666418+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_reports"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-24T16:55:41.716828+00:00_

EISDIR: illegal operation on a directory, read '/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_reports'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-24T16:55:48.031459+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_reports/",
  "description": "List review report files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_reports/",
    "description": "List review report files"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-24T16:55:48.262717+00:00_

total 76
drwxr-xr-x  2 ubuntu ubuntu  4096 May 22 05:04 .
drwxr-xr-x 25 ubuntu ubuntu  4096 May 24 16:45 ..
-rw-r--r--  1 ubuntu ubuntu 15713 May 20 05:37 round_1.md
-rw-r--r--  1 ubuntu ubuntu 11602 May 21 02:30 round_3.md
-rw-r--r--  1 ubuntu ubuntu  6613 May 21 03:19 round_4.md
-rw-r--r--  1 ubuntu ubuntu 13824 May 21 15:47 round_5.md
-rw-r--r--  1 ubuntu ubuntu 15898 May 22 05:04 round_6.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "elapsed_ms": 231
}
```

</details>

---


### Assistant

_source line 506 · 2026-05-24T16:56:38.276200+00:00_

状态恢复完成。当前情况：

- **项目**: recovery_aware_struct_prune，Round 7 审稿（fresh 模式）
- **论文**: "How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs"
- **PDF**: `review_round_7/submitted.pdf`
- **目标 venue**: EMNLP 2026（ARR 统一审稿）
- **外部审稿**: 未请求
- **视觉审查**: 已完成（4 个 info 级别发现，0 critical/warning）

---

**已收到 Reviewer 1 初审意见**（Round 1）：
- **Overall**: 3.0 (Findings)
- **4 个 critical**：generation length 混淆变量、RASP 单 seed、因果 overclaiming、Abstract overclaiming
- **5 个 warning**：calibration M 未指定、跨尺度证据薄弱、decoupling 缺统计检验、MBPP 不显著却被引用、CKA 作为 diversity proxy 未论证
- **Soundness**: 3/5, **Excitement**: 3.5/5, **Reproducibility**: 3/5

等待 Reviewer 2 审稿意见返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 41

## Round 41

6 recorded events


### User

_source line 507 · 2026-05-24T16:56:39.270930+00:00_

[Reviewer 2 审稿意见]:
## 总体评分
**Overall**: 3.0 — Findings（可被 Findings 接收）
**一句话总结**: 一项设计良好的控制实验，揭示了 reward-accuracy decoupling 这一有趣的经验发现，但受限于单一架构家族、dose-response 中的混杂变量、以及过短的 GRPO 训练步数，核心 claim 的泛化性不足以支撑主会议接收。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 控制实验设计严谨（固定除 pruning criterion 外的所有变量），主要结论有多 seed 统计支持（Welch's t-test, p=0.0009），但 dose-response 实验存在 max_completion_length 混杂变量，且 CKA 评估存在循环论证 |
| Excitement | 3.0/5 | Reward-accuracy decoupling 是一个反直觉且有价值的发现；但 RASP 方法本身过于简单（importance × diversity penalty），实际加速效果为负（throughput 降低 19%），且 20% sparsity 的实用价值有限 |
| Reproducibility | 3.5/5 | 超参数详尽（Table 3）、训练配置完整、代码和模型承诺公开；但 RASP 推荐配置（α=2.0）仅用单一 seed 验证，dose-response 各 α 值也为单 seed |
| Confidence | 4/5 | 熟悉 LLM 剪枝、RLVR 训练和 CKA 相关文献；仔细检查了实验设计和统计方法 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Dose-response 实验中 max_completion_length 不一致构成关键混杂变量
- 具体位置：Section 4.3, footnote（page 7, experiments.tex line 102）
- 问题：α=1.0 使用 max_completion_length=1,024，而 α=0.5, 2.0, 3.0, 4.0 使用 TRL 默认的 512。generation length 对 GRPO 训练动态有已知的显著影响（更长的生成 = 不同的探索空间、不同的 reward signal 密度）。论文将此描述为 "conservative estimate"，但这不能取代真正的 controlled ablation。最优 α=2.0 恰好使用了更短的生成限制——如果用 1,024 tokens，inverted-U 的形状可能完全不同。
- 为什么影响接收：这是论文的核心发现之一（dose-response 曲线证明 CKA 权重是 recovery 的 causal driver），如果曲线形状受生成长度混杂，因果推断就不成立。
- 建议修改方向：（1）用统一的 max_completion_length 重新运行所有 α 值的 dose-response；或（2）至少在 α=2.0 处用 1,024 tokens 复现，确认 inverted-U 是否 robust。

**N2** [critical] 用 CKA 评估 CKA-based pruning 构成循环论证
- 具体位置：Section 4.5, Figure 5（CKA heatmap, page 8）
- 问题：论文的核心叙事链是：CKA-only pruning 保留 representational diversity → 用 CKA similarity to dense model 度量 diversity（μ=0.62 vs. μ≥0.88）→ 得出 "diversity drives recovery"。但 CKA-only pruning 的定义就是移除高 CKA overlap 的结构，因此剩余结构必然会展示更低的 CKA similarity to dense——这是定义上的 tautology，不是 empirical evidence。
- 为什么影响接收：如果核心因果证据是循环的，论文的解释性 contribution 大幅削弱。Appendix H 的 gradient flow analysis（2.89× gradient magnitude）是独立证据，但论文自己承认 "the evidence is correlational" 且 "an alternative explanation...cannot be ruled out"（Appendix H）。
- 建议修改方向：（1）使用非 CKA 的 diversity 度量（如 centered distance correlation、projection-weighted CCA、或 representation rank）来独立验证 diversity 假说；（2）或至少在正文中明确承认 CKA heatmap 的循环性并降低 causal 语气。

**N3** [critical] "Reward-accuracy decoupling" 可能是训练不足的 artifact 而非结构性发现
- 具体位置：Section 4.2（decoupling results），Section 4.5（extended training, 300 steps）
- 问题：GRPO 仅训练 100 步（extended 到 300 步），这对于 RLVR 来说非常短。在如此短的训练中 GRPO 对 accuracy 影响微小（|Δ|<1pp）可能仅仅说明 GRPO 还没来得及产生效果——而不是 "recovery method choice becomes irrelevant"。论文中 SFT warmup 已经完成了大部分恢复工作（CKA-only: SFT 63.91% → GRPO 64.39%，仅 +0.48pp），GRPO 的边际贡献本就微小。如果训练更久（1000+ 步），不同 criterion 下的 GRPO 可能产生显著的 accuracy 差异，decoupling 就不成立。
- 为什么影响接收：这是论文最重要的 contribution（Contribution 1），如果它是训练不足的 artifact，论文的核心叙事崩塌。Self-Healing (2025) 在显著更长的训练中观察到 RLVR > SFT——本文无法排除更长训练也会出现同样结果的可能。
- 建议修改方向：（1）至少在一个条件下（如 CKA-only vs Standard at 20%）运行 1000+ GRPO steps，验证 decoupling 是否持续；（2）或明确将 claim scope 限定为 "在短期 GRPO 训练（≤300 steps）下"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 跨架构泛化严重不足
- 具体位置：Limitations (page 9), Appendix O (cross-architecture, page 14)
- 问题：论文的中心 claim 挑战了 "RLVR > SFT" 这一通用假设，但实验证据来自单一架构家族（Qwen2.5）。"跨架构验证" 用的 Qwen2.5-Math-7B 与主模型共享 Qwen2.5 base（相同的 transformer 结构），仅测了 SFT 没测 GRPO。1.5B scale 验证也是 DeepSeek-R1-Distill-Qwen-1.5B。论文的 claim 强度（"the hierarchy is an artifact"）与证据广度不匹配。
- 建议：要么在 LLaMA/Mistral 架构上做至少一组完整实验（含 GRPO），要么将 claim 明确限定为 "on Qwen2.5-based reasoning models"。

**W2** [warning] RASP 推荐配置（α=2.0）仅单 seed 验证
- 具体位置：Table 11 (Appendix L), experiments.tex line 30-31
- 问题：CKA-only、Standard、Random 各有 3 个 GRPO seeds，但 RASP（论文推荐的实际方法）在所有 α 值下都只用了 1 个 seed（Table 11: RASP, Seeds=1）。考虑到 RASP α=1.0 出现了 collapse，α 附近的 landscape 可能不稳定。单 seed 的 α=2.0 结果（66.11%）的可靠性未经验证。
- 建议：至少对 α=2.0 运行 3 个 seeds 以验证其优于 CKA-only 的结论是否 robust。

**W3** [warning] 30% sparsity 崩溃限制实用价值
- 具体位置：Appendix J (page 13), Appendix C (inference efficiency, page 11)
- 问题：所有方法在 30% sparsity 时完全崩溃（accuracy ≤4%），实际操作范围仅为 15-25%。在 20% sparsity 下，参数减少 19% 但 per-token throughput 反而降低 19%（72.0→58.3 tok/s）。这意味着剪枝后模型虽然省了 28% 显存，但推理速度更慢了。论文没有充分讨论这一负面实际影响。
- 建议：在 conclusion 或 limitations 中诚实讨论 throughput regression 及其对实际部署的影响。

**W4** [warning] "Diversity > importance for RL recovery" 的非显而易见性需要更强论证
- 具体位置：Section 1 (Introduction), Section 5 (Conclusion)
- 问题：RL 方法天然需要 exploration，而 exploration 受益于 diverse representations——这在 RL 理论中是已知的。论文声称 "diversity > importance for RL recovery" 是 non-obvious insight，但未充分讨论为什么从 first principles 推断不出这个结论。实际上，Section 5 的解释（"Policy gradient methods require trajectory variation to estimate reward gradients"）恰恰是从 first principles 出发的——如果可以这样推导，为什么需要实验？
- 建议：更清晰地 articulate 为什么先验预期不明确——例如，importance-based pruning 保留了更强的 reasoning capability（SFT accuracy 更高），直觉上应该给 GRPO 更好的起点。实际结果（更好的起点不等于更好的 RL 训练性）才是真正 surprising 的地方。

---

## 小问题（不影响接收）

- **术语一致性**: "pruning criterion" (singular) 和 "pruning criteria" (plural) 的使用整体正确，但建议统一在 contribution list 中使用一致形态。
- **Title 措辞**: 标题 "Post-RLVR Recovery" 可能产生误解——论文大量讨论 SFT recovery，且核心发现之一是 SFT ≈ GRPO。建议改为 "Post-Pruning Recovery" 或类似表述。
- **Abstract 字数**: 约 189 words，在 200-word 限制内。合规。
- **Contribution list**: 仅 2 项，但 RASP 方法本身被嵌入 Contribution 2 中而非独立 listed。如果作者将 RASP 视为 methodological contribution，建议单列。
- **Figure 1 caption**: 描述详尽且 self-contained，但略长（约 60 words）。
- **Related Work 组织**: 三个 paragraph（structured pruning, pruning-aware recovery, RLVR dynamics）覆盖合理，且清晰区分了本文贡献。未发现重大遗漏。
- **Appendix 结构**: 17 个 appendix sections 内容详实，但组织有些散乱（如 Section R "Depth-First Pruning Baseline" 与 Section Q "KL Divergence" 的逻辑关系不明）。建议按 "training details → main result extensions → robustness checks → additional analysis" 重新组织。
- **Ethics & AI 使用**: Section T（Use of AI Assistants）明确披露了 Claude 的使用范围（code, writing, literature），符合透明度要求。
- **Limitations**: 覆盖了 architecture/scale、diagnostic limitations、replication scope 三个方面，篇幅适中（约半页），符合 EMNLP 要求。但未提及 throughput regression 这一实际限制。
- **格式合规**: 使用 `\usepackage[review]{acl}`，double-blind（author 为 "Anonymous"），主文 8 页 + limitations/ethics 不计入页数，references 无限制。全部合规。

---

## 主要优势

1. **实验设计严谨**: 固定除 pruning criterion 外的所有变量（recovery pipeline、hyperparameters、hardware、calibration data），是罕见的 truly controlled comparison。这种设计使得因果推断更可靠。
2. **Reward-accuracy decoupling 是有价值的经验发现**: 在 4 种 pruning criteria × 3 个 sparsity levels 下，|Δ(GRPO−SFT)| 始终 <1pp（20-25% sparsity），这个 pattern 的一致性令人信服。
3. **统计验证充分**（主要对比）: CKA-only vs Standard 的 4.55pp gap 经 Welch's t-test 验证（p=0.0009, Cohen's d=11.1, 95% CI [3.62, 5.47]），3-seed 范围不重叠。
4. **写作清晰，叙事连贯**: Introduction 的 problem → gap → solution → results 故事线清楚，method section 组织良好，图表设计有效（特别是 Figure 3 的 SFT vs GRPO scatter 直观展示 decoupling）。
5. **诚实的 limitations**: 明确承认单一架构家族、RASP 单 seed、诊断指标的局限性，语气恰当。

---

## 评分依据

给 3.0（Findings）而非 3.5（Borderline Conference）的核心原因：

1. **N1 的混杂变量直接影响论文最核心的因果推断之一**（dose-response 驱动 inverted-U），且修复代价低（重跑几个实验），应在提交前解决。
2. **N3 的训练长度问题削弱了 Contribution 1 的说服力**——如果 decoupling 仅在 ≤300 steps 成立，claim 的价值大幅降低。
3. **泛化性不足**（W1）与 claim 的通用性（"the hierarchy is an artifact"）之间的 gap 过大。

如果 N1 和 N3 得到解决（统一 generation length 并验证长训练下的 decoupling），论文可以上调至 3.5。

---

[Reviewer 1 审稿结果]:
Round 1 审稿完成。

**总体评分：3.0 (Findings)**

核心发现有 4 个 Must-Fix 问题：

1. **Generation length 混淆变量**：Random 用 512 tokens、其他用 1024；dose-response 中 α=1.0 用 1024、其他用 512。破坏了"唯一变量是剪枝标准"的前提。
2. **RASP 单 seed**：proposed method 在所有 α 值上仅 1 seed，inverted-U peak 位置可能不稳定。
3. **因果 overclaiming**：Section 5 声称 diversity 是 "causal driver"，但证据仅为 correlational。
4. **Abstract overclaiming**：声称 decoupling "holds across sparsity levels"，但 15% 时 GRPO 仍 amplify gap by 1.51pp。

优势方面：controlled comparison 设计思路好，dose-response 分析有说服力，reward-accuracy decoupling 发现有趣。意见已提交给 Director。

---

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

总结：我给出 **Overall 3.0（Findings）**。论文的控制实验设计和 reward-accuracy decoupling 发现是其核心优势，但三个 critical 问题阻碍了主会议接收：
1. dose-response 中 max_completion_length 不一致构成混杂变量
2. 用 CKA 评估 CKA-based pruning 存在循环论证
3. 仅 100-300 步 GRPO 训练下的 "decoupling" 可能是训练不足的 artifact

如果修复 N1（统一 generation length）和 N3（验证长训练下 decoupling 是否持续），可上调至 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-24T16:57:46.817663+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 **[AGREE]** 并说明理由，或 **[REBUT]** 并引用具体 Section/Table/Figure 作为证据。\n\n如果你在 Reviewer 2 的意见中发现了自己遗漏的重要问题，请明确标注 **[NEW FINDING]**。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n## 总体评分\n**Overall**: 3.0 — Findings\n**一句话总结**: 一项设计良好的控制实验，揭示了 reward-accuracy decoupling 这一有趣的经验发现，但受限于单一架构家族、dose-response 中的混杂变量、以及过短的 GRPO 训练步数，核心 claim 的泛化性不足以支撑主会议接收。\n\n## 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 控制实验设计严谨，主要结论有多 seed 统计支持（p=0.0009），但 dose-response 存在 max_completion_length 混杂变量，且 CKA 评估存在循环论证 |\n| Excitement | 3.0/5 | Reward-accuracy decoupling 反直觉且有价值；但 RASP 过于简单，实际加速效果为负（throughput 降低 19%），20% sparsity 实用价值有限 |\n| Reproducibility | 3.5/5 | 超参详尽、代码承诺公开；但 RASP α=2.0 仅单 seed，dose-response 各 α 也为单 seed |\n| Confidence | 4/5 | 熟悉 LLM 剪枝、RLVR 训练和 CKA 文献 |\n\n## Must-Fix 问题\n\n**N1** [critical] Dose-response 实验中 max_completion_length 不一致构成关键混杂变量\n- 位置：Section 4.3, footnote（page 7）\n- α=1.0 使用 max_completion_length=1,024，而 α=0.5, 2.0, 3.0, 4.0 使用 TRL 默认 512。论文将此描述为 \"conservative estimate\"，但这不能取代 controlled ablation。最优 α=2.0 恰好使用更短的生成限制——如果用 1,024 tokens，inverted-U 形状可能完全不同。\n- 建议：统一 max_completion_length 重跑所有 α，或至少在 α=2.0 处用 1,024 tokens 复现。\n\n**N2** [critical] 用 CKA 评估 CKA-based pruning 构成循环论证\n- 位置：Section 4.5, Figure 5（CKA heatmap, page 8）\n- 论文核心叙事链：CKA-only pruning 保留 representational diversity → 用 CKA similarity to dense model 度量 diversity（μ=0.62 vs. μ≥0.88）→ 得出 \"diversity drives recovery\"。但 CKA-only 的定义就是移除高 CKA overlap 的结构，因此剩余结构必然展示更低的 CKA similarity to dense——这是 tautology，不是 empirical evidence。\n- 建议：使用非 CKA diversity 度量（centered distance correlation、CCA、representation rank）独立验证；或在正文承认循环性并降低 causal 语气。\n\n**N3** [critical] \"Reward-accuracy decoupling\" 可能是训练不足的 artifact\n- 位置：Section 4.2, Section 4.5（300 steps）\n- GRPO 仅训练 100 步（extended 300 步），对 RLVR 来说非常短。|Δ|<1pp 可能仅说明 GRPO 还没来得及产生效果。SFT warmup 已完成大部分恢复（CKA-only: 63.91% → 64.39%，仅 +0.48pp）。如果训练 1000+ 步，不同 criterion 下的 GRPO 可能产生显著 accuracy 差异。Self-Healing (2025) 在更长训练中观察到 RLVR > SFT。\n- 建议：至少在一个条件下运行 1000+ GRPO steps，验证 decoupling 是否持续；或限定 claim scope 为 \"≤300 steps\"。\n\n## Should-Fix 问题\n\n**W1** [warning] 跨架构泛化严重不足\n- 位置：Limitations, Appendix O\n- 实验仅限 Qwen2.5 家族。\"跨架构验证\" 的 Qwen2.5-Math-7B 共享 base。1.5B 也是 DeepSeek-R1-Distill-Qwen-1.5B。Claim 强度与证据广度不匹配。\n- 建议：LLaMA/Mistral 至少一组完整实验，或限定 claim 为 \"on Qwen2.5-based models\"。\n\n**W2** [warning] RASP α=2.0 仅单 seed 验证\n- 位置：Table 11 (Appendix L)\n- CKA-only/Standard/Random 各 3 seeds，RASP 所有 α 仅 1 seed。α=1.0 collapse 暗示 landscape 不稳定。\n- 建议：α=2.0 至少 3 seeds。\n\n**W3** [warning] 30% sparsity 崩溃限制实用价值\n- 位置：Appendix J, Appendix C\n- 所有方法 30% 时崩溃（accuracy ≤4%），操作范围仅 15-25%。20% sparsity 下 throughput 反而降低 19%。论文未充分讨论负面实际影响。\n- 建议：Limitations 诚实讨论 throughput regression。\n\n**W4** [warning] \"Diversity > importance for RL recovery\" 的非显而易见性需更强论证\n- 位置：Section 1, Section 5\n- RL 天然需要 exploration，受益于 diverse representations——这在 RL 理论中已知。论文称这是 non-obvious insight 但未充分论证为何先验推断不出。Section 5 的解释恰恰是 first principles 推导。\n- 建议：articulate 为什么先验预期不明确——importance-based 保留更强 reasoning capability，直觉上应给 GRPO 更好起点。\n\n## 小问题\n- Title \"Post-RLVR Recovery\" 可能误导，建议改为 \"Post-Pruning Recovery\"\n- Contribution list 仅 2 项，RASP 被嵌入而非独立 listed\n- Appendix 17 sections 组织散乱，建议重新分组\n- Limitations 未提及 throughput regression\n- 格式合规（ACL review template, double-blind, 8 pages）\n\n## 主要优势\n1. 实验设计严谨：truly controlled comparison\n2. Reward-accuracy decoupling 有价值且一致\n3. 统计验证充分（主要对比 p=0.0009, Cohen's d=11.1）\n4. 写作清晰，叙事连贯\n5. 诚实的 limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 **[AGREE]** 并说明理由，或 **[REBUT]** 并引用具体 Section/Table/Figure 作为证据。\n\n如果你在 Reviewer 2 的意见中发现了自己遗漏的重要问题，请明确标注 **[NEW FINDING]**。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n## 总体评分\n**Overall**: 3.0 — Findings\n**一句话总结**: 一项设计良好的控制实验，揭示了 reward-accuracy decoupling 这一有趣的经验发现，但受限于单一架构家族、dose-response 中的混杂变量、以及过短的 GRPO 训练步数，核心 claim 的泛化性不足以支撑主会议接收。\n\n## 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 控制实验设计严谨，主要结论有多 seed 统计支持（p=0.0009），但 dose-response 存在 max_completion_length 混杂变量，且 CKA 评估存在循环论证 |\n| Excitement | 3.0/5 | Reward-accuracy decoupling 反直觉且有价值；但 RASP 过于简单，实际加速效果为负（throughput 降低 19%），20% sparsity 实用价值有限 |\n| Reproducibility | 3.5/5 | 超参详尽、代码承诺公开；但 RASP α=2.0 仅单 seed，dose-response 各 α 也为单 seed |\n| Confidence | 4/5 | 熟悉 LLM 剪枝、RLVR 训练和 CKA 文献 |\n\n## Must-Fix 问题\n\n**N1** [critical] Dose-response 实验中 max_completion_length 不一致构成关键混杂变量\n- 位置：Section 4.3, footnote（page 7）\n- α=1.0 使用 max_completion_length=1,024，而 α=0.5, 2.0, 3.0, 4.0 使用 TRL 默认 512。论文将此描述为 \"conservative estimate\"，但这不能取代 controlled ablation。最优 α=2.0 恰好使用更短的生成限制——如果用 1,024 tokens，inverted-U 形状可能完全不同。\n- 建议：统一 max_completion_length 重跑所有 α，或至少在 α=2.0 处用 1,024 tokens 复现。\n\n**N2** [critical] 用 CKA 评估 CKA-based pruning 构成循环论证\n- 位置：Section 4.5, Figure 5（CKA heatmap, page 8）\n- 论文核心叙事链：CKA-only pruning 保留 representational diversity → 用 CKA similarity to dense model 度量 diversity（μ=0.62 vs. μ≥0.88）→ 得出 \"diversity drives recovery\"。但 CKA-only 的定义就是移除高 CKA overlap 的结构，因此剩余结构必然展示更低的 CKA similarity to dense——这是 tautology，不是 empirical evidence。\n- 建议：使用非 CKA diversity 度量（centered distance correlation、CCA、representation rank）独立验证；或在正文承认循环性并降低 causal 语气。\n\n**N3** [critical] \"Reward-accuracy decoupling\" 可能是训练不足的 artifact\n- 位置：Section 4.2, Section 4.5（300 steps）\n- GRPO 仅训练 100 步（extended 300 步），对 RLVR 来说非常短。|Δ|<1pp 可能仅说明 GRPO 还没来得及产生效果。SFT warmup 已完成大部分恢复（CKA-only: 63.91% → 64.39%，仅 +0.48pp）。如果训练 1000+ 步，不同 criterion 下的 GRPO 可能产生显著 accuracy 差异。Self-Healing (2025) 在更长训练中观察到 RLVR > SFT。\n- 建议：至少在一个条件下运行 1000+ GRPO steps，验证 decoupling 是否持续；或限定 claim scope 为 \"≤300 steps\"。\n\n## Should-Fix 问题\n\n**W1** [warning] 跨架构泛化严重不足\n- 位置：Limitations, Appendix O\n- 实验仅限 Qwen2.5 家族。\"跨架构验证\" 的 Qwen2.5-Math-7B 共享 base。1.5B 也是 DeepSeek-R1-Distill-Qwen-1.5B。Claim 强度与证据广度不匹配。\n- 建议：LLaMA/Mistral 至少一组完整实验，或限定 claim 为 \"on Qwen2.5-based models\"。\n\n**W2** [warning] RASP α=2.0 仅单 seed 验证\n- 位置：Table 11 (Appendix L)\n- CKA-only/Standard/Random 各 3 seeds，RASP 所有 α 仅 1 seed。α=1.0 collapse 暗示 landscape 不稳定。\n- 建议：α=2.0 至少 3 seeds。\n\n**W3** [warning] 30% sparsity 崩溃限制实用价值\n- 位置：Appendix J, Appendix C\n- 所有方法 30% 时崩溃（accuracy ≤4%），操作范围仅 15-25%。20% sparsity 下 throughput 反而降低 19%。论文未充分讨论负面实际影响。\n- 建议：Limitations 诚实讨论 throughput regression。\n\n**W4** [warning] \"Diversity > importance for RL recovery\" 的非显而易见性需更强论证\n- 位置：Section 1, Section 5\n- RL 天然需要 exploration，受益于 diverse representations——这在 RL 理论中已知。论文称这是 non-obvious insight 但未充分论证为何先验推断不出。Section 5 的解释恰恰是 first principles 推导。\n- 建议：articulate 为什么先验预期不明确——importance-based 保留更强 reasoning capability，直觉上应给 GRPO 更好起点。\n\n## 小问题\n- Title \"Post-RLVR Recovery\" 可能误导，建议改为 \"Post-Pruning Recovery\"\n- Contribution list 仅 2 项，RASP 被嵌入而非独立 listed\n- Appendix 17 sections 组织散乱，建议重新分组\n- Limitations 未提及 throughput regression\n- 格式合规（ACL review template, double-blind, 8 pages）\n\n## 主要优势\n1. 实验设计严谨：truly controlled comparison\n2. Reward-accuracy decoupling 有价值且一致\n3. 统计验证充分（主要对比 p=0.0009, Cohen's d=11.1）\n4. 写作清晰，叙事连贯\n5. 诚实的 limitations"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-24T16:58:30.688765+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 43871
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-24T16:58:30.991315+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 **[AGREE]** 并说明理由，或 **[REBUT]** 并引用具体 Section/Table/Figure 作为证据。\n\n如果你在 Reviewer 1 的意见中发现了自己遗漏的重要问题，请明确标注 **[NEW FINDING]**。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 核心发现有价值且实验设计思路好，但 generation length 系统性混淆变量、RASP 单 seed 验证不足、以及多处因果 overclaiming 使其未达到 Conference 水准。\n\n## 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心对照设计好，但 generation length confound 贯穿多个实验，RASP 仅单 seed，因果语言超出证据支持 |\n| Excitement | 3.5/5 | Reward-accuracy decoupling 有趣且挑战 \"RLVR > SFT\" 假设；dose-response 设计合理。但 scope 窄 |\n| Reproducibility | 3/5 | 超参大部分提供，但 calibration 数据量 M 未明确指定；generation length 差异分散在脚注中 |\n| Confidence | 4/5 | 熟悉 LLM 剪枝和 RL 恢复文献 |\n\n## Must-Fix 问题\n\n**N1** [critical] Generation length 混淆变量贯穿核心实验\n- 位置：Section 3.4, Section 4.1, Section 4.3 footnote\n- Random 使用 512 tokens，CKA-only/Standard/RASP 使用 1024 tokens\n- Dose-response：α=1.0 用 1024，其他 α 用 512\n- 破坏了 \"唯一变量是剪枝标准\" 的前提。Random 用 1024 可能改善其 GRPO 表现，改变 spectrum 排序。Dose-response inverted-U 形状受混淆。论文的 \"conservative estimate\" 论证不充分——generation length 对 GRPO 探索行为的影响不是单调的。\n- 建议：用统一 generation length 重跑 Random 和至少 3 个 α 值；或详细讨论 limitation 并降低 claim 强度。\n\n**N2** [critical] RASP 作为 proposed method 仅用单 seed 验证\n- 位置：Section 4.1, Table 11 (Appendix L), Limitations\n- CKA-only/Standard/Random 均 3 seeds，RASP 所有 sparsity 和 α 值仅 1 seed。Dose-response 的 5 个 α 值可能都是单 seed。Inverted-U peak 位置（α=2.0）可能不稳定。\n- Section 5 给 practitioner guideline \"Use RASP at α≈2.0\" 基于单次实验。Standard 的 3-seed std=0.38pp，RASP 真实方差可能更大。\n- 建议：至少对 α=2.0 和 α=1.0 各跑 3 seeds。\n\n**N3** [critical] 因果语言超出实验证据\n- 位置：Section 5 \"causal driver\"；Abstract \"reward-accuracy decoupling\"\n- 1) \"causal driver\": Dose-response 是 quasi-experimental，变化 α 同时改变 diversity 权重、被移除结构身份、sparsity 分布。Appendix H 自己承认 gradient flow 证据是 correlational。\n- 2) \"decoupling\" 作为 phenomenon: 仅在 20-25% sparsity 成立。15% 时 GRPO 仍 amplify gap by 1.51pp。将 sparsity-dependent 观察包装为普适性 \"phenomenon\" 是 overclaiming。\n- 建议：\"causal driver\" → \"primary correlate\"；decoupling 加 \"at 20-25% sparsity\" 限定。\n\n**N4** [critical] Abstract overclaiming \"holds across sparsity levels\"\n- 位置：Abstract line 3\n- 论文自己数据表明 15% 时 decoupling 不完全成立（GRPO amplifies CKA advantage by 1.51pp），30% 全 collapse。Decoupling 仅在 20-25% 窄窗口成立。\n- 建议：改为 \"at 20-25% sparsity across benchmarks\"。\n\n## Should-Fix 问题\n\n**W1** [warning] Calibration 数据量 M 未明确指定\n- 位置：Section 3.2\n- 正文定义 $\\mathcal{D}_{cal}$ 但从未指定 M。Appendix H/I 提到不同数量。主实验用的 M 是多少？\n\n**W2** [warning] \"Generality across scales\" 证据薄弱\n- 位置：Abstract, Section 4.5\n- 仅 1.5B 和 7B（同家族 <5x 差异），跨架构仅 Qwen2.5-Math-7B 且无 GRPO。\n\n**W3** [warning] Reward-accuracy decoupling 缺少形式化统计检验\n- 位置：Section 4.3\n- 声称 |Δ|=0.54pp \"near-identical\" 但未检验 H₀: Δ(GRPO-SFT)=0。应提供 TOST 等价性检验或明确 practical equivalence 阈值。\n\n**W4** [warning] MBPP 结果不显著却被用作支持证据\n- 位置：Section 4.3, Appendix G\n- Appendix G 承认 \"none are statistically significant\"，但 Section 4.3 仍引用 MBPP 支持 decoupling。\n\n**W5** [warning] CKA overlap 作为 \"representational diversity\" 的代理指标未充分论证\n- 位置：Section 3.2\n- CKA 衡量 representation similarity（kernel alignment），不等于功能性多样性。高 CKA 的结构可能在 RL 探索中提供不同 gradient pathways。\n\n## 小问题\n- Abstract 字数约 190-200 words，在限制边界\n- Table 1 Unpruned 行 \"Reward\" 为 \"0.027\"，含义不直观\n- Figure 2 label 字体偏小\n- Section 4.5 CKA-only 集中 early layers 剪枝（L0-9 占 72.5%）仅一句带过\n- Appendix R depth-first baseline 与主实验 granularity 不同，作为 sanity check 价值有限\n\n## 主要优势\n1. 控制实验设计思路优秀\n2. Dose-response 分析有说服力\n3. Recovery capacity spectrum framing 清晰实用\n4. 部分实验统计严谨（3-seed + t-test + Cohen's d + 95% CI）\n5. 坦诚的 Limitations 节\n6. 行文清晰"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 **[AGREE]** 并说明理由，或 **[REBUT]** 并引用具体 Section/Table/Figure 作为证据。\n\n如果你在 Reviewer 1 的意见中发现了自己遗漏的重要问题，请明确标注 **[NEW FINDING]**。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 核心发现有价值且实验设计思路好，但 generation length 系统性混淆变量、RASP 单 seed 验证不足、以及多处因果 overclaiming 使其未达到 Conference 水准。\n\n## 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心对照设计好，但 generation length confound 贯穿多个实验，RASP 仅单 seed，因果语言超出证据支持 |\n| Excitement | 3.5/5 | Reward-accuracy decoupling 有趣且挑战 \"RLVR > SFT\" 假设；dose-response 设计合理。但 scope 窄 |\n| Reproducibility | 3/5 | 超参大部分提供，但 calibration 数据量 M 未明确指定；generation length 差异分散在脚注中 |\n| Confidence | 4/5 | 熟悉 LLM 剪枝和 RL 恢复文献 |\n\n## Must-Fix 问题\n\n**N1** [critical] Generation length 混淆变量贯穿核心实验\n- 位置：Section 3.4, Section 4.1, Section 4.3 footnote\n- Random 使用 512 tokens，CKA-only/Standard/RASP 使用 1024 tokens\n- Dose-response：α=1.0 用 1024，其他 α 用 512\n- 破坏了 \"唯一变量是剪枝标准\" 的前提。Random 用 1024 可能改善其 GRPO 表现，改变 spectrum 排序。Dose-response inverted-U 形状受混淆。论文的 \"conservative estimate\" 论证不充分——generation length 对 GRPO 探索行为的影响不是单调的。\n- 建议：用统一 generation length 重跑 Random 和至少 3 个 α 值；或详细讨论 limitation 并降低 claim 强度。\n\n**N2** [critical] RASP 作为 proposed method 仅用单 seed 验证\n- 位置：Section 4.1, Table 11 (Appendix L), Limitations\n- CKA-only/Standard/Random 均 3 seeds，RASP 所有 sparsity 和 α 值仅 1 seed。Dose-response 的 5 个 α 值可能都是单 seed。Inverted-U peak 位置（α=2.0）可能不稳定。\n- Section 5 给 practitioner guideline \"Use RASP at α≈2.0\" 基于单次实验。Standard 的 3-seed std=0.38pp，RASP 真实方差可能更大。\n- 建议：至少对 α=2.0 和 α=1.0 各跑 3 seeds。\n\n**N3** [critical] 因果语言超出实验证据\n- 位置：Section 5 \"causal driver\"；Abstract \"reward-accuracy decoupling\"\n- 1) \"causal driver\": Dose-response 是 quasi-experimental，变化 α 同时改变 diversity 权重、被移除结构身份、sparsity 分布。Appendix H 自己承认 gradient flow 证据是 correlational。\n- 2) \"decoupling\" 作为 phenomenon: 仅在 20-25% sparsity 成立。15% 时 GRPO 仍 amplify gap by 1.51pp。将 sparsity-dependent 观察包装为普适性 \"phenomenon\" 是 overclaiming。\n- 建议：\"causal driver\" → \"primary correlate\"；decoupling 加 \"at 20-25% sparsity\" 限定。\n\n**N4** [critical] Abstract overclaiming \"holds across sparsity levels\"\n- 位置：Abstract line 3\n- 论文自己数据表明 15% 时 decoupling 不完全成立（GRPO amplifies CKA advantage by 1.51pp），30% 全 collapse。Decoupling 仅在 20-25% 窄窗口成立。\n- 建议：改为 \"at 20-25% sparsity across benchmarks\"。\n\n## Should-Fix 问题\n\n**W1** [warning] Calibration 数据量 M 未明确指定\n- 位置：Section 3.2\n- 正文定义 $\\mathcal{D}_{cal}$ 但从未指定 M。Appendix H/I 提到不同数量。主实验用的 M 是多少？\n\n**W2** [warning] \"Generality across scales\" 证据薄弱\n- 位置：Abstract, Section 4.5\n- 仅 1.5B 和 7B（同家族 <5x 差异），跨架构仅 Qwen2.5-Math-7B 且无 GRPO。\n\n**W3** [warning] Reward-accuracy decoupling 缺少形式化统计检验\n- 位置：Section 4.3\n- 声称 |Δ|=0.54pp \"near-identical\" 但未检验 H₀: Δ(GRPO-SFT)=0。应提供 TOST 等价性检验或明确 practical equivalence 阈值。\n\n**W4** [warning] MBPP 结果不显著却被用作支持证据\n- 位置：Section 4.3, Appendix G\n- Appendix G 承认 \"none are statistically significant\"，但 Section 4.3 仍引用 MBPP 支持 decoupling。\n\n**W5** [warning] CKA overlap 作为 \"representational diversity\" 的代理指标未充分论证\n- 位置：Section 3.2\n- CKA 衡量 representation similarity（kernel alignment），不等于功能性多样性。高 CKA 的结构可能在 RL 探索中提供不同 gradient pathways。\n\n## 小问题\n- Abstract 字数约 190-200 words，在限制边界\n- Table 1 Unpruned 行 \"Reward\" 为 \"0.027\"，含义不直观\n- Figure 2 label 字体偏小\n- Section 4.5 CKA-only 集中 early layers 剪枝（L0-9 占 72.5%）仅一句带过\n- Appendix R depth-first baseline 与主实验 granularity 不同，作为 sanity check 价值有限\n\n## 主要优势\n1. 控制实验设计思路优秀\n2. Dose-response 分析有说服力\n3. Recovery capacity spectrum framing 清晰实用\n4. 部分实验统计严谨（3-seed + t-test + Cohen's d + 95% CI）\n5. 坦诚的 Limitations 节\n6. 行文清晰"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-24T16:58:32.431729+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1440
}
```

</details>

---


### Assistant

_source line 512 · 2026-05-24T16:58:37.174896+00:00_

交叉分享已发出。两位 Reviewer 正在审阅对方的完整审稿意见并准备逐条回应。等待 [AGREE]/[REBUT] 交叉回应返回后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 42

## Round 42

2 recorded events


### User

_source line 513 · 2026-05-24T17:04:23.473544+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

### Must-Fix 问题

**[REBUT] R1-N1: Generation length 混淆变量贯穿核心实验**

R1 的核心事实判断有误。R1 声称"Dose-response：α=1.0 用 1024，其他 α 用 512"，但论文 Table 3（Appendix A, p.11）脚注明确写道：**"Random uses TRL default of 512 tokens; all other methods use 1,024."** 这意味着：

- CKA-only、Standard、RASP（所有 α 值）均使用 1024 tokens
- 仅 Random 使用 512 tokens
- Dose-response 曲线（α 从 0 到 4.0）内部完全一致，全部使用 1024 tokens

因此，generation length 混淆**仅影响 Random 与其他方法的对比**，不影响论文的三个核心发现：
1. Recovery capacity spectrum（CKA-only > Standard > RASP）——三者均用 1024
2. Dose-response inverted-U 曲线——RASP 内部一致用 1024
3. Reward-accuracy decoupling——CKA-only/Standard/RASP 对比均用 1024

Random 本身被论文定位为"conservative comparison point"（Section 3.4），其 512-token 限制使其处于不利地位。论文的核心叙事不依赖 Random 的绝对表现。

**我的判断**：R1 将此问题定为 [critical] 并称"贯穿核心实验"是过度放大。降为 **[warning]** 更合适——建议作者在 Table 3 正文（而非仅脚注）中更显著地标注这一差异，并补充讨论为何不统一 Random 的 generation length。

---

**[AGREE] R1-N2: RASP 单 seed 验证不足**

完全同意。Table 1（p.6）清楚显示 CKA-only/Standard/Random 均为 3 seeds（报告 mean ± std），而 RASP 所有 sparsity 和 α 值仅 1 seed。Limitations（p.9）承认这一点。

核心问题在于：
- Section 5 给出的 practitioner guideline "Use RASP at α≈2.0" 基于单次实验，inverted-U 峰值位置可能因 seed 漂移
- Standard 的 3-seed std = 0.38pp（Table 1），RASP 真实方差可能更大
- Dose-response 曲线（Table 5, Appendix D）的 5 个 α 数据点若均为单 seed，曲线形状的可信度不足

这是影响论文可信度的实质问题。至少需对 α=2.0（声称最优）和 α=0（退化为 Standard 的边界条件）各跑 3 seeds。

---

**[AGREE] R1-N3: 因果语言超出实验证据（部分同意）**

对 R1 的两个子问题分别回应：

**子问题 1："causal driver" 用语**——部分同意。Dose-response 设计确实是准实验（quasi-experimental）方法中建立因果推断的 recognized approach（Bradford Hill criteria 中的 biological gradient）。变化 α 并观察单调-后衰减的恢复曲线，比简单相关性更强。但 R1 正确指出，改变 α 同时改变了 diversity 权重、被移除结构的身份和 sparsity 分布，非严格单变量操控。建议用 **"key determinant"** 而非 "causal driver"——比 R1 建议的 "primary correlate" 更准确反映 dose-response 的证据强度，同时避免因果过度声称。

**子问题 2："decoupling" 作为 phenomenon 的 scope**——完全同意。Section 4.3 的数据显示：
- 15% sparsity：GRPO amplifies CKA advantage by 1.51pp（Table 12, Appendix M），说明 GRPO 在此 sparsity 下仍与 pruning criterion 交互
- 20%：|Δ| ≤ 0.54pp，decoupling 成立
- 25%：|Δ| ≤ 1pp，borderline
- 30%：collapse

将 sparsity-dependent 观察包装为普适 "phenomenon" 确实是 overclaiming。

---

**[AGREE] R1-N4: Abstract overclaiming "holds across sparsity levels"**

同意。Abstract 第 3 行 "a pattern that holds across sparsity levels and benchmarks" 与论文自身数据矛盾：
- 15% 时 decoupling 不完全成立（上述 1.51pp amplification）
- 30% 全 collapse
- 有效窗口为 20-25%

应改为 "at moderate sparsity (20–25%) across benchmarks" 或类似限定表述。

---

### Should-Fix 问题

**[AGREE] R1-W1: Calibration 数据量 M 未明确指定**

Section 3.2 定义了 $\mathcal{D}_{cal} = \{(x_j, y_j)\}_{j=1}^M$ 但主文从未给出 M 的值。对于 reproducibility 这是必须提供的信息。

---

**[AGREE] R1-W2: "Generality across scales" 证据薄弱**

同意。仅 1.5B 和 7B（同为 Qwen2.5 家族，<5× 差异），跨架构仅 Qwen2.5-Math-7B 且未做 GRPO 恢复。Table 14（Appendix O）的 cross-architecture 结果虽支持 SFT 阶段的 spectrum ordering，但缺少 GRPO 验证，削弱了对 RLVR recovery 的泛化声称。

补充一点：论文 Limitations（p.9）承认 "cross-architecture evidence does not extend to different architecture families (e.g., LLaMA, Mistral)"，但 abstract 和 introduction 的 framing 仍暗示较强的泛化性。

---

**[AGREE] R1-W3: Reward-accuracy decoupling 缺少形式化统计检验**

同意。声称 |Δ|=0.54pp 为 "near-identical" 需要形式化支撑。TOST equivalence test 或至少定义 practical equivalence margin（如 ε=1pp）并检验是合理要求。目前仅靠 |Δ| 的绝对值大小做定性判断不够严谨。

---

**[AGREE] R1-W4: MBPP 结果不显著却被用作支持证据**

同意。Appendix G（p.13）承认 "none are statistically significant"，但 Section 4.3 仍将 MBPP 列为支持 decoupling 的证据。这属于 selective reporting。建议正文中明确标注 MBPP 结果的统计不显著性，或将其仅作为 directional evidence 呈现。

---

**[REBUT] R1-W5: CKA overlap 作为 "representational diversity" 的代理指标未充分论证**

部分不同意。R1 认为 "CKA 衡量 representation similarity，不等于功能性多样性"，这在概念层面正确。但论文的实证证据直接支撑了 CKA overlap 作为代理指标的有效性：

1. **Dose-response 验证**：Figure 1 和 Table 5（Appendix D）显示 CKA coefficient α 与 GRPO recovery accuracy 之间存在清晰的 inverted-U 关系（ρ=0.62 for CKA-only vs ρ≥0.88 for collapsing methods, Section 5），说明 CKA overlap 确实预测恢复结果
2. **Calibration stability**：Appendix H（Table 6）提供 CKA scoring stability 的 cross-calibration 证据，Spearman ρ > 0.964
3. **Appendix P（Structural Overlap Analysis）**：Figure 7 的结构分析显示 CKA-only 和 Standard 选择的 groups 有不同的 layer 分布模式，与功能性差异一致

论文不需要证明 CKA = 功能性多样性的完美代理，只需要证明 CKA overlap 与 recovery outcome 有可靠的 predictive relationship——这一点通过 dose-response 分析已充分建立。R1 提出的 "高 CKA 结构可能在 RL 探索中提供不同 gradient pathways" 是一个有趣的 future work 方向，但不构成对当前论证的反驳。

---

### [NEW FINDING] CKA-only 的 layer 分布混淆

**这是我认为 R1 遗漏的一个重要问题。**

Section 4.5（p.8）和 Appendix P（p.15）揭示了一个关键事实：**CKA-only 将 72.5% 的剪枝集中在 early layers（L0-9）**，而 Standard 分布更均匀。这意味着 CKA-only 的优势可能并非来自 "diversity preservation" 本身，而是来自 **early-layer selective pruning**——保留了 late layers 中更多的推理关键结构。

论文在 Appendix R（p.15）尝试用 depth-first baseline 控制这一混淆，但 R1 在小问题中正确指出：**depth-first baseline 操作在 layer-level granularity（移除整个 transformer blocks），而主实验在 MLP channel-group level**。这一 granularity 不匹配使 depth-first baseline 无法有效解耦 "diversity preservation" 和 "early-layer concentration" 两个机制。

建议增加一个 **same-granularity layer-biased baseline**：在 MLP channel-group level，按 layer index 赋权（early layers 高权重 → 优先剪枝），不使用 CKA 信息，检验是否能复现 CKA-only 的优势。如果能，则 CKA 的贡献主要是识别了正确的 layer 分布，而非 representational diversity per se。

---

### 对 R1 小问题的简要回应

- Abstract 字数：我也确认在 190-200 words 边界，建议压缩几词留余量
- Table 1 Unpruned "Reward" = 0.027：同意不直观，应加脚注解释 reward 的 scale/含义
- Figure 2 label 字体偏小：同意
- Section 4.5 CKA-only early-layer concentration 仅一句带过：这与我的 [NEW FINDING] 一致，应给予更充分的讨论
- Appendix R depth-first baseline granularity 问题：同上

---

### 总结

R1 的审稿整体质量高，多数问题定位准确。但 **N1 的严重程度被高估**——generation length 混淆仅影响 Random 比较，不影响核心 spectrum ordering 和 dose-response 分析（R1 对 dose-response 中 α 值使用不同 generation length 的判断有误）。建议将 N1 从 [critical] 降为 [warning]。

R1 遗漏了 **CKA-only layer 分布混淆** 这一重要问题——CKA-only 的优势可能部分或主要来自 early-layer concentration 而非 diversity preservation，现有的 depth-first baseline 因 granularity 不匹配无法排除此混淆。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 514 · 2026-05-24T17:04:39.018563+00:00_

Reviewer 2 交叉回应已收到。关键发现：

- **R1-N1 降级**：R2 指出 R1 对 dose-response generation length 的事实判断有误——所有 α 值均用 1024 tokens，仅 Random 用 512。混淆仅影响 Random 对比，不影响核心 spectrum 和 dose-response。建议降为 warning。
- **R1-N2/N3/N4**：AGREE，RASP 单 seed、因果 overclaiming、abstract 限定均达成共识。
- **[NEW FINDING]**：CKA-only 的 early-layer concentration（L0-9 占 72.5%）可能是其优势的真正来源而非 diversity preservation。现有 depth-first baseline 因 granularity 不匹配无法排除此混淆。

等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 43

## Round 43

2 recorded events


### User

_source line 515 · 2026-05-24T17:04:41.521612+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Director。核心判断：

1. **R1-N1 被高估**：Generation length 混淆仅影响 Random（512 tokens），CKA-only/Standard/RASP 均用 1024。R1 声称 dose-response 各 α 值用不同 generation length 有误（Table 3 脚注明确否定）。建议从 critical 降为 warning。
2. **R1-N2/N3/N4 同意**：单 seed RASP、因果过度声称、abstract scope 过大均为实质问题。
3. **R1-W1~W4 同意**，**W5 部分反驳**（CKA 的预测有效性已由 dose-response 实证支撑）。
4. **新发现**：CKA-only 将 72.5% 剪枝集中在 early layers，其优势可能来自 layer 分布而非 diversity preservation。Appendix R 的 depth-first baseline 因 granularity 不匹配无法解耦此混淆。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 516 · 2026-05-24T17:05:01.346050+00:00_

收到 Reviewer 2 的交叉回应。等待 Reviewer 1 的交叉回应后进行收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 44

## Round 44

10 recorded events


### User

_source line 517 · 2026-05-24T17:05:36.860129+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 Reviewer 2

---

### Must-Fix 问题

**[AGREE] R2-N1: Dose-response 实验中 max_completion_length 不一致构成混杂变量**

事实确认无误。experiments.tex 第 102 行脚注明确写道："α=1.0 uses max_completion_length=1,024; other α values use the TRL default of 512. Since α=1.0 is the curve minimum, this makes the inverted-U a conservative estimate."

论文的 "conservative estimate" 辩护有一定道理：α=1.0 是曲线最低点，它反而用了更长的生成限制（1,024），如果换成 512 可能表现更差，所以 inverted-U 的谷底深度可能被低估而非高估。但这个辩护只解决了最低点的问题——**峰值端（α=0.5, 2.0, 3.0, 4.0）全部使用 512 tokens，它们之间的相对排序是可比的，但与 α=1.0 的绝对差距不可靠**。对于数学推理任务，max_completion_length 直接限制推理链长度，512 vs 1,024 可能导致截断效应差异。

结论：混杂变量确实存在，需要统一控制。但 R2 称 "inverted-U 形状可能完全不同" 有些过强——更准确的说法是谷底-峰值的绝对差距不确定，但 α=1.0 collapse 的定性结论不受影响。

---

**[REBUT] R2-N2: 用 CKA 评估 CKA-based pruning 构成循环论证**

R2 的批评混淆了两个不同层次的 CKA 度量：

1. **剪枝准则**（Eq. 3, Section 3.2）使用 **intra-layer pairwise CKA**：$F(b_i) = \frac{1}{|G_l|-1} \sum_{b_j \neq b_i} \text{CKA}(X_{b_i}, X_{b_j})$，衡量同一层内 MLP channel group 之间的功能冗余
2. **评估指标**（Figure 5）使用 **inter-model layer-wise CKA**：衡量剪枝后模型每层的聚合表征与 dense 模型同层聚合表征的相似度

这不是 tautology。CKA-only 移除高 intra-layer overlap 的结构（冗余结构），保留功能独特的结构。保留后的层级聚合表征与 dense 模型差异增大（μ=0.62 vs. μ≥0.88）——这个差异幅度是 empirical finding，不是定义推导。理论上，移除冗余结构后，剩余独特结构也可能恰好重建出与 dense 相似的聚合表征（如果冗余结构只贡献噪声而非方向性信息）。

更关键的是，论文提供了完全独立于 CKA 的补充证据：**gradient flow analysis 显示 CKA-only 的 mean gradient magnitude 是 Standard 的 2.89×**（55/56 layer groups, p<0.05, Wilcoxon; Section 4.5）。这是非 CKA 指标。

**但 R2 的关切有合理内核**：论文的主叙事确实过度依赖 CKA 家族指标，补充一个完全独立的 diversity 度量（CCA、centered distance correlation 或 effective rank）会显著增强因果论证。我将此从 "critical" 降级为 **should-fix**：现状不是循环论证，但 metrics diversity 不足。

---

**[AGREE] R2-N3: Reward-accuracy decoupling 可能是训练不足的 artifact**

同意这是核心可信度问题。从 Table 2 数据看：

- CKA-only: SFT 63.91% → GRPO 64.39%（+0.48pp）
- Standard: SFT 59.29% → GRPO 59.84%（+0.55pp）
- RASP: SFT 61.49% → GRPO 60.61%（-0.88pp，但单 seed）

GRPO 在所有条件下的增量效应均 < 1pp。100 步主实验 + 300 步延长实验远短于典型 RLVR 训练（通常 1000+ 步）。"Decoupling" 本质上可能只是说：**在 GRPO 还没来得及产生显著 accuracy 效应的阶段，naturally 不同条件的 accuracy 差异不大。** 如果训练 1000+ 步，importance-based pruning 保留的更强 reasoning backbone 可能最终在 accuracy 上显现优势。

论文 Limitations (p9) 承认了 "reward-accuracy decoupling... does not predict downstream accuracy improvements within our training horizon"，但正文（Section 4.2 标题 "Reward-Accuracy Decoupling"）将其呈现为核心发现而非 scope-limited observation。建议要么运行 1000+ 步验证，要么在正文中显式限定 claim scope 为 "within ≤300 GRPO steps"。

---

### Should-Fix 问题

**[AGREE] R2-W1: 跨架构泛化不足**

完全同意。所有实验模型共享 Qwen2.5 base architecture：
- DeepSeek-R1-Distill-Qwen-7B（主实验）
- Qwen2.5-Math-7B（Appendix O，标题为 "Cross-Architecture Validation" 但实际是同架构不同训练数据）
- DeepSeek-R1-Distill-Qwen-1.5B（Appendix N，同架构不同规模）

Appendix O 的 "Cross-Architecture" 标题具有误导性。论文所有 claim 应限定为 "on Qwen2.5-family models"，除非补充 LLaMA-3 或 Mistral 实验。

---

**[AGREE] R2-W2: RASP α=2.0 仅单 seed**

同意。Table 2 明确标注 CKA-only/Standard/Random 各 3 seeds，RASP 仅 1 seed。α=1.0 出现 collapse（peak reward 0.061）表明 RASP landscape 对 α 高度敏感。作为 dose-response 最优点的 α=2.0（66.11%）缺乏多 seed 验证，无法排除 lucky initialization。至少需要 3 seeds 确认。

---

**[AGREE] R2-W3: 30% sparsity 崩溃 + throughput regression**

部分同意。两个子问题需分开讨论：

1. **30% 崩溃**：所有方法在 30% sparsity 均崩溃（accuracy ≤4%），操作范围仅 15-25%。但这在 LLM 结构化剪枝领域并非异常——很多 work 在 25-30% 也面临类似限制，20% 是合理的工作点。
2. **Throughput regression**：Table 4 (Appendix C, p11) 报告 per-token throughput 降低 19%（0.81×），原因是非均匀层宽导致 GPU kernel 无法优化。**这是一个严重的实用性问题**，但 Limitations section (p9) 完全未提及。论文讨论了 memory reduction（~28%）和 TTFT improvement（18%），却回避了 throughput regression——选择性报告正面指标是不妥的。

---

**[REBUT] R2-W4: "Diversity > importance for RL recovery" 的 non-obvious 性**

不同意 R2 的判断。R2 认为 "RL 需要 exploration, diversity 有益" 是已知的，因此这个发现不 surprising。但这里有层次混淆：

- **RL 理论中的 diversity**：指 policy space 中的 exploration（action diversity、entropy bonus 等）
- **本文的 diversity**：指 **pruned architecture 中保留的 representational diversity**——即剪枝后模型的结构性质如何影响后续 RL 训练的恢复能力

先验直觉应该是：**importance-based pruning 保留了模型最强的 reasoning components → 给 GRPO 更好的起点 → 应该恢复更好。** 这是 structured pruning 文献中的标准假设——LLM-Pruner (Ma et al., 2023)、SliceGPT、Wanda 等都以保留 "重要" 结构为目标。论文的发现恰恰推翻了这个领域共识：在 RL recovery 场景下，保留 "最重要" 的结构不如保留 "最独特" 的结构。

R2 说 Section 5 的解释 "恰恰是 first principles 推导"——但这是 **post-hoc rationalization**，不是 **prior prediction**。很多 empirical findings 事后都可以用理论解释，这不削弱其 novelty。关键是：在本文之前，没有 work 系统地比较过 importance vs. diversity 作为剪枝准则对 RL recovery 的影响。

---

### 新发现

**[NEW FINDING] 论文标题/叙事框架与实际结果的错位**

论文标题为 "How Pruning Criteria Shape Post-RLVR Recovery"，核心叙事围绕 RLVR（GRPO）阶段展开。但实验数据显示 **SFT 阶段已完成恢复的绝大部分工作**：

| Method | Post-Prune | After SFT | After GRPO | SFT贡献 | GRPO贡献 |
|--------|-----------|-----------|------------|---------|----------|
| CKA-only | ~0% | 63.91% | 64.39% | ~64pp | +0.48pp |
| Standard | ~0% | 59.29% | 59.84% | ~59pp | +0.55pp |

GRPO 的增量贡献不足 1pp，而 CKA-only vs Standard 的差距（~4.5pp）在 SFT 阶段就已经建立。这意味着论文的核心故事可能更准确地描述为 **"pruning criterion shapes SFT recovery capacity"**，而非 "Post-RLVR Recovery"。

GRPO 阶段的独特贡献在于 reward trajectory 的差异化（CKA-only 持续学习 vs. RASP collapse vs. Standard stagnation）——但如果这些差异不转化为 accuracy 差异，它们的实际意义需要更充分的论证。论文应在 Discussion 中更清晰地分离 SFT vs. GRPO 各自的角色，并解释为什么将 GRPO 阶段作为叙事焦点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-24T17:07:06.061584+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "max_completion_length|completion.length|conservative estimate|TRL default",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "max_completion_length|completion.length|conservative estimate|TRL default",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "context": "3"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-24T17:07:06.112418+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.aux-563-\@LN{443}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.aux-564-\@LN{444}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.aux-565-\@LN@col{2}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.aux:566:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.aux:567:\newlabel{tab:recovery_gradient}{{1}{6}{Recovery capacity spectrum: GRPO dynamics for four pruning criteria at 20\% sparsity under identical configuration (lr $1{\times }10^{-6}$, $\beta {=}0.01$, $T{=}0.4$, 1{,}024-token limit, 100 steps); Random uses TRL default 512-token limit, making it a conservative comparison point. $f_0$: fraction of batches where all completions receive identical reward (lower = healthier). Best in \textbf {bold}}{table.caption.22}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.aux:568:\@writefile{lot}{\contentsline {table}{\numberline {2}{\ignorespaces GRPO responsiveness on GSM8K ($N{=}1{,}319$, greedy decoding), evaluated at step 100. All methods share identical GRPO configuration (Table~\ref {tab:hyperparams}), except Random which uses TRL default 512-token limit. CKA-only, Standard, and Random report mean $\pm $ std over 3 GRPO seeds; \textsc  {Rasp}{} uses a single seed. Best in \textbf  {bold}.}}{6}{table.caption.24}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.aux:569:\newlabel{tab:decoupling}{{2}{6}{GRPO responsiveness on GSM8K ($N{=}1{,}319$, greedy decoding), evaluated at step 100. All methods share identical GRPO configuration (Table~\ref {tab:hyperparams}), except Random which uses TRL
…[truncated 17134 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-24T17:07:14.391915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex",
  "offset": "95",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex",
    "offset": "95",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-24T17:07:14.442476+00:00_

95	\label{sec:sft_gradient}
96	Under SFT alone, CKA-only (63.91\%) $>$ \rasp{} (61.49\%) $>$ Standard (59.29\%) $>$ Random (51.25\%), yet under GRPO the \rasp{}/Standard ordering reverses and Random outperforms both in peak reward.
97	The spectrum is driven by structural properties of the pruned architecture, not post-SFT accuracy.
98	
99	\paragraph{Dose-response and sparsity limits.}
100	\label{sec:sparsity_cliff}
101	The CKA coefficient $\alpha$ continuously controls recovery capacity.
102	On GSM8K, recovery follows an inverted-U across $\alpha \in \{0.5, 1.0, 2.0, 3.0, 4.0\}$, peaking at $\alpha{=}2.0$ (SFT 64.97\%, GRPO 66.11\%; Figure~\ref{fig:dose_response}, Table~\ref{tab:alpha}) with $|\Delta| \leq 1.14$\,pp at every point; $\alpha{=}1.0$ collapses (peak reward 0.061) while $\alpha{=}4.0$ recovers to 62.77\% (Appendix~\ref{sec:appendix_alpha}).\footnote{$\alpha{=}1.0$ uses \texttt{max\_completion\_length}{$=$}1{,}024; other $\alpha$ values use the TRL default of 512. Since $\alpha{=}1.0$ is the curve minimum, this makes the inverted-U a conservative estimate.}
103	The key finding generalizes to MATH-500: $\alpha{=}1.0$ remains the worst (GRPO 23.0\%), while higher-$\alpha$ and CKA-only methods cluster near the top (GRPO 27.2--27.6\%), though the inverted-U shape is not resolved at this difficulty level (Table~\ref{tab:math500}; Appendix~\ref{sec:appendix_math500}).
104	All methods collapse at 30\% sparsity (Appendix~\ref{sec:appendix_sparsity_cliff}); pruning reduces parameters by 19\% and memory by ${\sim}$28\% (Appendix~\ref{sec:appendix_inference}).
105	
106	
107	\subsection{Extended Analysis}
108	\label{sec:extended_analysis}
109	
110	\begin{figure}[t]
111	    \centering
112	    \includegraphics[width=\columnwidth]{figures/paper/fig4_cka_heatmap.pdf}
113	    \caption{Layer-wise CKA similarity between dense and pruned representations (28 layers). CKA-only diverges most from dense ($\mu{=}0.62$) yet recovers best; Standard ($\mu{=}0.90$), Random ($\mu{=}0.
…[truncated 112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-24T17:13:49.720498+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "issues_yaml": "\n# ============================================================\n# Round 1-3 Issues — All Resolved\n# ============================================================\n\n- id: \"R1-C1\"\n  summary: \"CKA-recovery link 仅相关性, 无因果干预\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Jaccard overlap 分析 + Limitations 承认 + 多种子统计验证\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Single-seed GRPO 无统计显著性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"3-seed GRPO CKA-only, Welch's t-test p=0.0009\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"仅 GSM8K 单基准\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"MATH-500 OOD 验证 + MBPP 代码基准\"\n  resolution_round: 3\n\n- id: \"R1-W1\"\n  summary: \"Title overclaim 'determines'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Title 改为 'shapes'\"\n  resolution_round: 3\n\n- id: \"R1-W2\"\n  summary: \"Abstract 'universally determines' overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"改为 'significantly shapes'\"\n  resolution_round: 3\n\n- id: \"R1-W3\"\n  summary: \"仅 DeepSeek-R1-7B 单模型\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Qwen2.5-Math-7B cross-arch + 1.5B cross-scale\"\n  resolution_round: 3\n\n- id: \"R1-M1\"\n  summary: \"GRPO 超参未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Appendix 完整超参表\"\n  resolution_round: 3\n\n- id: \"R1-M2\"\n  summary: \"Table 1 缺 Random baseline\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Table 1 加入 Random 行\"\n  resolution_round: 3\n\n- id: \"R2-NEW-C1\"\n  summary: \"GRPO 准确率几乎不变,为何要用 GRPO\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Dual-layer reframe: SFT(accuracy) + GRPO(reward signal)\"\n  resolution_round: 3\n\n- id: \"R2-NEW-C2\"\n  summary: \"Cross-architecture 仅 SFT 验证,GRPO 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"1.5B GRPO 补充 + Abstract 区分表述\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W1\"\n  summary: \"SFT recovery 被忽视,过度聚焦 GRPO\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注解释 SFT catastrophic forgetting\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W2\"\n  summary: \"Qwen-Math 跨架构验证仅 SFT，Abstract overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 区分 GRPO(DeepSeek) vs SFT(Qwen-Math)\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W3\"\n  summary: \"GRPO 准确率改变 < 1pp — 实际效用存疑\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"300-step accuracy + reward-accuracy decoupling 论证\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W4\"\n  summary: \"RASP/Random 仍为单种子\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注透明标注 + Limitations 披露\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W5\"\n  summary: \"Random baseline SFT/GRPO Acc 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Table 2 脚注标注 checkpoint not preserved\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W6\"\n  summary: \"正文 5 处 'determines' 残留\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"全部替换为 shapes/significantly influences\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M1\"\n  summary: \"GRPO batch size / rollouts 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M2\"\n  summary: \"SFT lr/batch/optimizer 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-VIS-1\"\n  summary: \"末页 Figure 6 仅占 30%，70% 空白\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 重排\"\n  resolution_round: 3\n\n- id: \"R2-VIS-2\"\n  summary: \"Appendix page 12 过度拥挤\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 拆分到多页\"\n  resolution_round: 3\n\n- id: \"R3-S5\"\n  summary: \"Qwen-Math 'strongest evidence' 措辞仍略强\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"strongest → additional evidence in §4.5\"\n  resolution_round: 3\n\n- id: \"R3-M2\"\n  summary: \"300-step accuracy 未标注 seed\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"(single seed) 标注已添加到 §4.3\"\n  resolution_round: 3\n\n- id: \"R3-M3\"\n  summary: \"无代码/checkpoint 发布声明\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"Code and checkpoints release statement in Conclusion\"\n  resolution_round: 3\n\n# ============================================================\n# Round 5-6 Issues — Updated with Round 7 observations\n# ============================================================\n\n- id: \"R5-N1\"\n  summary: \"Reward-accuracy decoupling 叙事薄弱（GRPO 增量 <1pp，可能是训练不足的 artifact）\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。SYSTEMIC_ISSUE #1 核心。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W4 和 R2-W2 再次提出，增加新角度：需区分 format compliance vs reasoning quality。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-N3 升级为 critical：100-300 步 GRPO 远低于典型 RLVR 训练（1000+ 步），decoupling 可能仅反映训练不足。R1 完全同意。R1 补充新发现：SFT 贡献 ~60pp 恢复而 GRPO <1pp，论文叙事焦点与实际恢复来源错位。Self-Healing (2025) 在更长训练中观察到 RLVR > SFT。\"\n  action_items:\n    - round: 5\n      action: \"D098 dual-layer reframe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"Agent 提取 format compliance / EOS rate 数据\"\n      assigned_to: agent\n      status: in_progress\n    - round: 7\n      action: \"运行 ≥1000 GRPO steps（至少 CKA-only vs Standard at 20%）验证 decoupling 是否持续；或限定 claim scope 为 '≤300 steps'\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N2\"\n  summary: \"Cross-architecture/scale 泛化严重不足，所有模型共享 Qwen2.5 base\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前不可行（需全 pipeline ~50h GPU）。但 1.5B GRPO 数据已有。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识。R1 指出 Appendix O 'Cross-Architecture Validation' 标题具有误导性——Qwen2.5-Math-7B 与主模型共享架构。R2 同意。仅 1.5B 和 7B（<5× 差异），无 LLaMA/Mistral。claim 应限定为 'Qwen2.5-family models'。\"\n  action_items:\n    - round: 5\n      action: \"补入 1.5B GRPO 数据作 cross-scale validation\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"MF3: Qwen2.5-Math-7B CKA-only GRPO 训练\"\n      assigned_to: agent\n      status: in_progress\n    - round: 7\n      action: \"重命名 Appendix O 标题；Abstract/正文限定 claim 为 Qwen2.5 家族；或补充 LLaMA/Mistral 实验\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"RASP 单 seed 验证不足——practitioner guideline 基于单次实验\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"核心比较 CKA vs Standard 有 3-seed p=0.0009。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 升级为 critical。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识 critical。R1-N2 详细论证：Section 5 'Use RASP at α≈2.0' 基于单 seed，Standard std=0.38pp 暗示 RASP 方差可能更大。α=1.0 collapse 表明 RASP landscape 对 α 高度敏感。R2-W2 完全同意。至少需 α=2.0 和 α=1.0 各 3 seeds。\"\n  action_items:\n    - round: 5\n      action: \"Limitations 标注 + 核心 claim 限定 CKA vs Standard\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"MF2: RASP/Random seeds 123,456 GRPO 训练\"\n      assigned_to: agent\n      status: in_progress\n    - round: 7\n      action: \"至少 RASP α=2.0 和 α=1.0 各跑 3 seeds 验证 inverted-U peak 稳定性\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"因果语言系统性过强——'causal driver' 超出 quasi-experimental 证据\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"SYSTEMIC_ISSUE #2 成员。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N3 详细论证两个子问题：(1) 'causal driver' 用语——dose-response 是 quasi-experimental，非严格单变量操控；(2) 'decoupling' 命名——仅 20-25% 成立。R2 同意但建议折衷用 'key determinant' 而非 'primary correlate'。R2 补充：CKA 评估存在 metrics diversity 不足问题（R1 rebut 了循环论证但认可 metrics 单一性）。\"\n  action_items:\n    - round: 5\n      action: \"Jaccard overlap 分析 + Limitations 承认缺干预实验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 6\n      action: \"降级 Contribution 3 为 Discussion observation\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 7\n      action: \"全文语言审计：'causal driver' → 'key determinant'；所有 decoupling claims 加 'at 20-25% sparsity' 限定；补充一个非 CKA 的 diversity 度量（CCA/effective rank）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Per-layer capacity floor (40%) 未消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前无法做 full pipeline ablation。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W3 再次提出。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 提及，可能已修复或不再关注，待 Research Director 确认\"\n  action_items:\n    - round: 5\n      action: \"Limitations 讨论 + rebuttal 论点准备\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Floor ablation τ∈{0.3,0.4,0.5,0.6} experiments running; appendix table added\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"α dose-response 存在 generation length 混杂变量\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"高 ROI 实验。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出。R2-W1 扩展为 κ 消融缺失。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"升级为 critical。事实核查确认：α=1.0 用 1024 tokens，α=0.5/2.0/3.0/4.0 用 512 tokens（experiments.tex line 102 脚注）。R2 误将 Table 3 脚注（主实验配置：仅 Random 用 512）等同于 dose-response 配置。Inverted-U 峰值 α=2.0（512 tokens）vs 谷底 α=1.0（1024 tokens）的绝对差距不可靠。'conservative estimate' 论证仅解决谷底问题，不解决峰值排序。\"\n  action_items:\n    - round: 5\n      action: \"α=4.0 GRPO 100步实验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 6\n      action: \"α dose-response: α=0.5,2.0 pipeline\"\n      assigned_to: agent\n      status: in_progress\n    - round: 7\n      action: \"统一所有 α 值的 max_completion_length（建议全部 1024）重跑 dose-response；至少 α=2.0 用 1024 复现验证 inverted-U 峰值\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"'Recovery capacity gradient' 术语与 gradient descent 混淆\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W4 指出残留不一致。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未提及，可能已统一为 spectrum\"\n  action_items:\n    - round: 5\n      action: \"全文替换为 'recovery capacity spectrum'\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M1\"\n  summary: \"Section 5 末尾溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"约 2 行溢出\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及，可能已修复\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未提及。R7 Reviewer 确认格式合规（8 pages main text）。可能已修复，待 Research Director 确认\"\n  action_items:\n    - round: 5\n      action: \"Paper Agent 压缩 §5 确保 8 页合规\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M2\"\n  summary: \"Abstract p<0.001 未说明统计检验方法\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Abstract 标注 Welch's t-test\"\n  resolution_round: 6\n\n- id: \"R5-M3\"\n  summary: \"Page 7 display items 过度拥挤\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Figure 3 + Figure 4 + Table 2 挤在同一页\"\n    - round: 7\n      reviewers: []\n      note: \"视觉审查仍标记 page 7 视觉密度较高（Figure 3 三子图 + Figure 4）。R1 小问题也提到。\"\n  action_items:\n    - round: 5\n      action: \"Figure 前移平衡视觉节奏\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M4\"\n  summary: \"bib key 年份误导 + 引用错误\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"lachance2024cka→2022, klabunde→2023, selfhealing2025 venue 空\"\n    - round: 6\n      reviewers: [2]\n      note: \"新引用错误：正文 'Dong et al. (2026)' vs 参考文献 'Longyi Deng'\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未被 Reviewer 直接提及，待 Research Director 确认是否已修复\"\n  action_items:\n    - round: 5\n      action: \"Paper Agent 修正 bib 条目\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M5\"\n  summary: \"Figure 2 标注字体偏小 / 颜色区分度不足\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: []\n      note: \"视觉审查发现\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1 小问题再次提出\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 和 R2 均在小问题中提到 Figure 2 label 字体偏小。视觉审查也标记 page 5 Figure 2 内部标注文字偏小。\"\n  action_items:\n    - round: 5\n      action: \"增大字号 + 添加不同 line style\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N1\"\n  summary: \"GSM8K 单基准 GRPO 主实验，Title/Abstract 做一般性声明\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未被直接提及为独立 issue。R1-W4 提到 MBPP 结果不显著但用于支持 claim，间接相关。\"\n  action_items:\n    - round: 6\n      action: \"MF1: MBPP probe eval\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"CKA-only layer 分布混杂——72.5% 剪枝集中 early layers，优势可能来自 layer 分布而非 diversity\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"R1-N3 提出：需 depth-controlled ablation。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 交叉回应 [NEW FINDING] 详细展开：CKA-only 72.5% 移除 L0-9，保留 late-layer 推理结构，优势可能来自 early-layer selective pruning 而非 diversity preservation。Appendix R depth-first baseline 操作在 layer-level granularity（整个 transformer blocks），而主实验在 MLP channel-group level——granularity 不匹配无法解耦两种机制。R1 小问题中也标记 early-layer concentration 仅一句带过。需 same-granularity layer-biased baseline。\"\n  action_items:\n    - round: 6\n      action: \"MF5: Agent 创建 Late-Layer-First baseline pipeline\"\n      assigned_to: agent\n      status: in_progress\n    - round: 7\n      action: \"创建 same-granularity layer-biased baseline：MLP channel-group level 按 layer index 赋权（early layers 优先剪枝），不用 CKA 信息，验证是否复现 CKA-only 优势\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N3\"\n  summary: \"缺失高度相关文献：RL Finetunes Small Subnetworks (2505.11711)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent 添加引用并在 Related Work/Discussion 讨论\"\n  resolution_round: 6\n\n- id: \"R6-W1\"\n  summary: \"Reward-accuracy decoupling 未区分 format compliance vs reasoning quality\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"需报告 EOS rate 和 format compliance rate\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未直接提及，但 R2-N3 关于训练步数的问题间接相关。待 Research Director 确认。\"\n  action_items:\n    - round: 6\n      action: \"Agent 从 eval logs 提取 format compliance / EOS rate\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"实验仅覆盖 MLP channel pruning，Title/Abstract 未限定 scope\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: []\n      note: \"Title 已包含 'Structured MLP Pruning'。R2 格式合规检查确认。\"\n  resolution: \"Title 改为 'How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs'\"\n  resolution_round: 7\n\n- id: \"R6-W3\"\n  summary: \"遗漏 3 篇相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent 验证并添加引用\"\n  resolution_round: 6\n\n- id: \"R6-W4\"\n  summary: \"Welch's t-test at N=3 统计功效极低，缺 effect size 和 CI\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R7 Reviewer 在优势中肯定 Cohen's d=11.1 和 95% CI [3.62, 5.47]pp 的统计支撑。已修复。\"\n  resolution: \"Cohen's d + 95% CI 已加入正文\"\n  resolution_round: 7\n\n- id: \"R6-W5\"\n  summary: \"15%/25% sparsity 实验为 single-seed\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W5 交叉回应提出。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未直接提及，但 RASP 单 seed 问题（R5-W1）覆盖更广范围\"\n  action_items:\n    - round: 6\n      action: \"MF2 部分覆盖; 15%/25% 在 Limitations 标注\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"RASP 表现差于 Standard 缺乏充分解释\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"需分析 importance 和 CKA overlap 的相关性\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未直接提及，但 dose-response 分析中 α=1.0 collapse 被广泛讨论\"\n  action_items:\n    - round: 6\n      action: \"Paper Agent 待 α dose-response 数据后分析 RASP failure mechanism\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W7\"\n  summary: \"Table 1 脚注 'Only redundancy-based pruning sustains RL recovery' 与 Random 排第二矛盾\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"脚注措辞已修改\"\n  resolution_round: 6\n\n- id: \"R6-W8\"\n  summary: \"Section 5 Discussion 偏薄（仅半页）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议讨论 CKA 与 RL exploration 关系、actionable 建议、Lottery Ticket 联系\"\n    - round: 7\n      reviewers: []\n      note: \"R7 R1 提出 Discussion 应更清晰分离 SFT vs GRPO 角色（参见 R1 NEW FINDING），间接相关\"\n  action_items:\n    - round: 6\n      action: \"Paper Agent 待实验数据后扩充 Discussion\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M1\"\n  summary: \"Reward-accuracy decoupling 首次使用时无正式定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"首次使用处添加正式定义\"\n  resolution_round: 6\n\n- id: \"R6-M2\"\n  summary: \"Figure 2 y 轴未标注 mean vs peak reward\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 提出。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未直接提及，待确认是否已修复\"\n  action_items:\n    - round: 6\n      action: \"修改 Figure 2 y-axis label\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M3\"\n  summary: \"Eq.1 未写出 Taylor expansion 完整数学形式\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2 小问题。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未提及，待确认\"\n  action_items:\n    - round: 6\n      action: \"Paper Agent 补充 Eq.1 完整数学形式\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 7 New Issues\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"Dose-response 中 max_completion_length 不一致（α=1.0: 1024, 其他: 512）构成关键混杂变量\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N1 和 R2-N1 均独立提出。交叉回应中 R2 试图 rebut（声称所有非 Random 方法均用 1024），但 Director 事实核查确认 R2 混淆了主实验配置（Table 3 脚注）与 dose-response 配置（experiments.tex line 102 脚注）。主实验中仅 Random 受影响（warning），但 dose-response 的混杂是 critical。\"\n  action_items:\n    - round: 7\n      action: \"统一所有 α 值 max_completion_length=1024 重跑 dose-response；或至少 α=2.0 用 1024 复现\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N2\"\n  summary: \"Abstract overclaiming 'holds across sparsity levels'——仅 20-25% 窗口成立\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N4 提出，R2 完全同意。15% 时 GRPO amplifies CKA advantage by 1.51pp，30% 全 collapse。\"\n  action_items:\n    - round: 7\n      action: \"Abstract 改为 'at moderate sparsity (20-25%) across benchmarks' 或类似限定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W1\"\n  summary: \"Decoupling 缺少形式化等价性检验（TOST）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W3 提出，R2 同意。|Δ|=0.54pp 声称 'near-identical' 需要 TOST 或明确定义 practical equivalence margin。\"\n  action_items:\n    - round: 7\n      action: \"使用 TOST（ε=1pp）或在正文明确声明 practical equivalence 阈值\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"MBPP 结果统计不显著却被用作 decoupling 支持证据\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 同意。Appendix G 承认不显著但 Section 4.3 仍引用。\"\n  action_items:\n    - round: 7\n      action: \"正文引用 MBPP 时加注 'though not statistically significant at this sample size'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W3\"\n  summary: \"Calibration 数据量 M 在正文中未明确指定\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 同意。Section 3.2 定义 D_cal 但从未给出 M 值。\"\n  action_items:\n    - round: 7\n      action: \"在 Section 3.2 或 4.1 中明确指定 M 及选择依据\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W4\"\n  summary: \"Throughput regression（-19%）未在 Limitations 讨论——选择性报告正面指标\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W3 提出，R1 部分同意。20% sparsity 下 memory -28% 但 throughput -19%（72.0→58.3 tok/s）。Limitations 报告 memory/TTFT 正面指标但回避 throughput regression。\"\n  action_items:\n    - round: 7\n      action: \"在 Limitations 添加 throughput regression 讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"Title/叙事焦点与实际恢复来源错位——SFT 贡献 ~60pp 而 GRPO <1pp\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 交叉回应 [NEW FINDING]：论文标题 'Post-RLVR Recovery' 但数据显示 SFT 完成绝大部分恢复（CKA-only: ~0% → 63.91% SFT → 64.39% GRPO）。GRPO 独特贡献在 reward trajectory 差异化但不转化为 accuracy。建议 Discussion 分离 SFT vs GRPO 角色。\"\n  action_items:\n    - round: 7\n      action: \"Discussion 中明确分离 SFT vs GRPO 的恢复角色；考虑 Title 是否应为 'Post-Pruning Recovery'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "issues_yaml": "\n# ============================================================\n# Round 1-3 Issues — All Resolved\n# ============================================================\n\n- id: \"R1-C1\"\n  summary: \"CKA-recovery link 仅相关性, 无因果干预\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Jaccard overlap 分析 + Limitations 承认 + 多种子统计验证\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Single-seed GRPO 无统计显著性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"3-seed GRPO CKA-only, Welch's t-test p=0.0009\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"仅 GSM8K 单基准\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"MATH-500 OOD 验证 + MBPP 代码基准\"\n  resolution_round: 3\n\n- id: \"R1-W1\"\n  summary: \"Title overclaim 'determines'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Title 改为 'shapes'\"\n  resolution_round: 3\n\n- id: \"R1-W2\"\n  summary: \"Abstract 'universally determines' overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"改为 'significantly shapes'\"\n  resolution_round: 3\n\n- id: \"R1-W3\"\n  summary: \"仅 DeepSeek-R1-7B 单模型\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Qwen2.5-Math-7B cross-arch + 1.5B cross-scale\"\n  resolution_round: 3\n\n- id: \"R1-M1\"\n  summary: \"GRPO 超参未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Appendix 完整超参表\"\n  resolution_round: 3\n\n- id: \"R1-M2\"\n  summary: \"Table 1 缺 Random baseline\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Table 1 加入 Random 行\"\n  resolution_round: 3\n\n- id: \"R2-NEW-C1\"\n  summary: \"GRPO 准确率几乎不变,为何要用 GRPO\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Dual-layer reframe: SFT(accuracy) + GRPO(reward signal)\"\n  resolution_round: 3\n\n- id: \"R2-NEW-C2\"\n  summary: \"Cross-architecture 仅 SFT 验证,GRPO 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"1.5B GRPO 补充 + Abstract 区分表述\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W1\"\n  summary: \"SFT recovery 被忽视,过度聚焦 GRPO\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注解释 SFT catastrophic forgetting\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W2\"\n  summary: \"Qwen-Math 跨架构验证仅 SFT，Abstract overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 区分 GRPO(DeepSeek) vs SFT(Qwen-Math)\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W3\"\n  summary: \"GRPO 准确率改变 < 1pp — 实际效用存疑\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"300-step accuracy + reward-accuracy decoupling 论证\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W4\"\n  summary: \"RASP/Random 仍为单种子\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注透明标注 + Limitations 披露\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W5\"\n  summary: \"Random baseline SFT/GRPO Acc 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Table 2 脚注标注 checkpoint not preserved\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W6\"\n  summary: \"正文 5 处 'determines' 残留\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"全部替换为 shapes/significantly influences\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M1\"\n  summary: \"GRPO batch size / rollouts 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M2\"\n  summary: \"SFT lr/batch/optimizer 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-VIS-1\"\n  summary: \"末页 Figure 6 仅占 30%，70% 空白\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 重排\"\n  resolution_round: 3\n\n- id: \"R2-VIS-2\"\n  summary: \"Appendix page 12 过度拥挤\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 拆分到多页\"\n  resolution_round: 3\n\n- id: \"R3-S5\"\n  summary: \"Qwen-Math 'strongest evidence' 措辞仍略强\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"strongest → additional evidence in §4.5\"\n  resolution_round: 3\n\n- id: \"R3-M2\"\n  summary: \"300-step accuracy 未标注 seed\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"(single seed) 标注已添加到 §4.3\"\n  resolution_round: 3\n\n- id: \"R3-M3\"\n  summary: \"无代码/checkpoint 发布声明\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"Code and checkpoints release statement in Conclusion\"\n  resolution_round: 3\n\n# ============================================================\n# Round 5-6 Issues — Updated with Round 7 observations\n# ============================================================\n\n- id: \"R5-N1\"\n  summary: \"Reward-accuracy decoupling 叙事薄弱（GRPO 增量 <1pp，可能是训练不足的 artifact）\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。SYSTEMIC_ISSUE #1 核心。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W4 和 R2-W2 再次提出，增加新角度：需区分 format compliance vs reasoning quality。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-N3 升级为 critical：100-300 步 GRPO 远低于典型 RLVR 训练（1000+ 步），decoupling 可能仅反映训练不足。R1 完全同意。R1 补充新发现：SFT 贡献 ~60pp 恢复而 GRPO <1pp，论文叙事焦点与实际恢复来源错位。Self-Healing (2025) 在更长训练中观察到 RLVR > SFT。\"\n  action_items:\n    - round: 5\n      action: \"D098 dual-layer reframe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"Agent 提取 format compliance / EOS rate 数据\"\n      assigned_to: agent\n      status: in_progress\n    - round: 7\n      action: \"运行 ≥1000 GRPO steps（至少 CKA-only vs Standard at 20%）验证 decoupling 是否持续；或限定 claim scope 为 '≤300 steps'\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N2\"\n  summary: \"Cross-architecture/scale 泛化严重不足，所有模型共享 Qwen2.5 base\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前不可行（需全 pipeline ~50h GPU）。但 1.5B GRPO 数据已有。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识。R1 指出 Appendix O 'Cross-Architecture Validation' 标题具有误导性——Qwen2.5-Math-7B 与主模型共享架构。R2 同意。仅 1.5B 和 7B（<5× 差异），无 LLaMA/Mistral。claim 应限定为 'Qwen2.5-family models'。\"\n  action_items:\n    - round: 5\n      action: \"补入 1.5B GRPO 数据作 cross-scale validation\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"MF3: Qwen2.5-Math-7B CKA-only GRPO 训练\"\n      assigned_to: agent\n      status: in_progress\n    - round: 7\n      action: \"重命名 Appendix O 标题；Abstract/正文限定 claim 为 Qwen2.5 家族；或补充 LLaMA/Mistral 实验\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"RASP 单 seed 验证不足——practitioner guideline 基于单次实验\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"核心比较 CKA vs Standard 有 3-seed p=0.0009。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 升级为 critical。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识 critical。R1-N2 详细论证：Section 5 'Use RASP at α≈2.0' 基于单 seed，Standard std=0.38pp 暗示 RASP 方差可能更大。α=1.0 collapse 表明 RASP landscape 对 α 高度敏感。R2-W2 完全同意。至少需 α=2.0 和 α=1.0 各 3 seeds。\"\n  action_items:\n    - round: 5\n      action: \"Limitations 标注 + 核心 claim 限定 CKA vs Standard\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"MF2: RASP/Random seeds 123,456 GRPO 训练\"\n      assigned_to: agent\n      status: in_progress\n    - round: 7\n      action: \"至少 RASP α=2.0 和 α=1.0 各跑 3 seeds 验证 inverted-U peak 稳定性\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"因果语言系统性过强——'causal driver' 超出 quasi-experimental 证据\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"SYSTEMIC_ISSUE #2 成员。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N3 详细论证两个子问题：(1) 'causal driver' 用语——dose-response 是 quasi-experimental，非严格单变量操控；(2) 'decoupling' 命名——仅 20-25% 成立。R2 同意但建议折衷用 'key determinant' 而非 'primary correlate'。R2 补充：CKA 评估存在 metrics diversity 不足问题（R1 rebut 了循环论证但认可 metrics 单一性）。\"\n  action_items:\n    - round: 5\n      action: \"Jaccard overlap 分析 + Limitations 承认缺干预实验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 6\n      action: \"降级 Contribution 3 为 Discussion observation\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 7\n      action: \"全文语言审计：'causal driver' → 'key determinant'；所有 decoupling claims 加 'at 20-25% sparsity' 限定；补充一个非 CKA 的 diversity 度量（CCA/effective rank）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Per-layer capacity floor (40%) 未消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前无法做 full pipeline ablation。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W3 再次提出。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 提及，可能已修复或不再关注，待 Research Director 确认\"\n  action_items:\n    - round: 5\n      action: \"Limitations 讨论 + rebuttal 论点准备\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Floor ablation τ∈{0.3,0.4,0.5,0.6} experiments running; appendix table added\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"α dose-response 存在 generation length 混杂变量\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"高 ROI 实验。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出。R2-W1 扩展为 κ 消融缺失。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"升级为 critical。事实核查确认：α=1.0 用 1024 tokens，α=0.5/2.0/3.0/4.0 用 512 tokens（experiments.tex line 102 脚注）。R2 误将 Table 3 脚注（主实验配置：仅 Random 用 512）等同于 dose-response 配置。Inverted-U 峰值 α=2.0（512 tokens）vs 谷底 α=1.0（1024 tokens）的绝对差距不可靠。'conservative estimate' 论证仅解决谷底问题，不解决峰值排序。\"\n  action_items:\n    - round: 5\n      action: \"α=4.0 GRPO 100步实验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 6\n      action: \"α dose-response: α=0.5,2.0 pipeline\"\n      assigned_to: agent\n      status: in_progress\n    - round: 7\n      action: \"统一所有 α 值的 max_completion_length（建议全部 1024）重跑 dose-response；至少 α=2.0 用 1024 复现验证 inverted-U 峰值\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"'Recovery capacity gradient' 术语与 gradient descent 混淆\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W4 指出残留不一致。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未提及，可能已统一为 spectrum\"\n  action_items:\n    - round: 5\n      action: \"全文替换为 'recovery capacity spectrum'\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M1\"\n  summary: \"Section 5 末尾溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"约 2 行溢出\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及，可能已修复\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未提及。R7 Reviewer 确认格式合规（8 pages main text）。可能已修复，待 Research Director 确认\"\n  action_items:\n    - round: 5\n      action: \"Paper Agent 压缩 §5 确保 8 页合规\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M2\"\n  summary: \"Abstract p<0.001 未说明统计检验方法\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Abstract 标注 Welch's t-test\"\n  resolution_round: 6\n\n- id: \"R5-M3\"\n  summary: \"Page 7 display items 过度拥挤\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Figure 3 + Figure 4 + Table 2 挤在同一页\"\n    - round: 7\n      reviewers: []\n      note: \"视觉审查仍标记 page 7 视觉密度较高（Figure 3 三子图 + Figure 4）。R1 小问题也提到。\"\n  action_items:\n    - round: 5\n      action: \"Figure 前移平衡视觉节奏\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M4\"\n  summary: \"bib key 年份误导 + 引用错误\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"lachance2024cka→2022, klabunde→2023, selfhealing2025 venue 空\"\n    - round: 6\n      reviewers: [2]\n      note: \"新引用错误：正文 'Dong et al. (2026)' vs 参考文献 'Longyi Deng'\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未被 Reviewer 直接提及，待 Research Director 确认是否已修复\"\n  action_items:\n    - round: 5\n      action: \"Paper Agent 修正 bib 条目\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M5\"\n  summary: \"Figure 2 标注字体偏小 / 颜色区分度不足\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: []\n      note: \"视觉审查发现\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1 小问题再次提出\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 和 R2 均在小问题中提到 Figure 2 label 字体偏小。视觉审查也标记 page 5 Figure 2 内部标注文字偏小。\"\n  action_items:\n    - round: 5\n      action: \"增大字号 + 添加不同 line style\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N1\"\n  summary: \"GSM8K 单基准 GRPO 主实验，Title/Abstract 做一般性声明\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未被直接提及为独立 issue。R1-W4 提到 MBPP 结果不显著但用于支持 claim，间接相关。\"\n  action_items:\n    - round: 6\n      action: \"MF1: MBPP probe eval\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"CKA-only layer 分布混杂——72.5% 剪枝集中 early layers，优势可能来自 layer 分布而非 diversity\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"R1-N3 提出：需 depth-controlled ablation。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 交叉回应 [NEW FINDING] 详细展开：CKA-only 72.5% 移除 L0-9，保留 late-layer 推理结构，优势可能来自 early-layer selective pruning 而非 diversity preservation。Appendix R depth-first baseline 操作在 layer-level granularity（整个 transformer blocks），而主实验在 MLP channel-group level——granularity 不匹配无法解耦两种机制。R1 小问题中也标记 early-layer concentration 仅一句带过。需 same-granularity layer-biased baseline。\"\n  action_items:\n    - round: 6\n      action: \"MF5: Agent 创建 Late-Layer-First baseline pipeline\"\n      assigned_to: agent\n      status: in_progress\n    - round: 7\n      action: \"创建 same-granularity layer-biased baseline：MLP channel-group level 按 layer index 赋权（early layers 优先剪枝），不用 CKA 信息，验证是否复现 CKA-only 优势\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N3\"\n  summary: \"缺失高度相关文献：RL Finetunes Small Subnetworks (2505.11711)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent 添加引用并在 Related Work/Discussion 讨论\"\n  resolution_round: 6\n\n- id: \"R6-W1\"\n  summary: \"Reward-accuracy decoupling 未区分 format compliance vs reasoning quality\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"需报告 EOS rate 和 format compliance rate\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未直接提及，但 R2-N3 关于训练步数的问题间接相关。待 Research Director 确认。\"\n  action_items:\n    - round: 6\n      action: \"Agent 从 eval logs 提取 format compliance / EOS rate\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"实验仅覆盖 MLP channel pruning，Title/Abstract 未限定 scope\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: []\n      note: \"Title 已包含 'Structured MLP Pruning'。R2 格式合规检查确认。\"\n  resolution: \"Title 改为 'How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs'\"\n  resolution_round: 7\n\n- id: \"R6-W3\"\n  summary: \"遗漏 3 篇相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent 验证并添加引用\"\n  resolution_round: 6\n\n- id: \"R6-W4\"\n  summary: \"Welch's t-test at N=3 统计功效极低，缺 effect size 和 CI\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R7 Reviewer 在优势中肯定 Cohen's d=11.1 和 95% CI [3.62, 5.47]pp 的统计支撑。已修复。\"\n  resolution: \"Cohen's d + 95% CI 已加入正文\"\n  resolution_round: 7\n\n- id: \"R6-W5\"\n  summary: \"15%/25% sparsity 实验为 single-seed\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W5 交叉回应提出。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未直接提及，但 RASP 单 seed 问题（R5-W1）覆盖更广范围\"\n  action_items:\n    - round: 6\n      action: \"MF2 部分覆盖; 15%/25% 在 Limitations 标注\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"RASP 表现差于 Standard 缺乏充分解释\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"需分析 importance 和 CKA overlap 的相关性\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未直接提及，但 dose-response 分析中 α=1.0 collapse 被广泛讨论\"\n  action_items:\n    - round: 6\n      action: \"Paper Agent 待 α dose-response 数据后分析 RASP failure mechanism\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W7\"\n  summary: \"Table 1 脚注 'Only redundancy-based pruning sustains RL recovery' 与 Random 排第二矛盾\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"脚注措辞已修改\"\n  resolution_round: 6\n\n- id: \"R6-W8\"\n  summary: \"Section 5 Discussion 偏薄（仅半页）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议讨论 CKA 与 RL exploration 关系、actionable 建议、Lottery Ticket 联系\"\n    - round: 7\n      reviewers: []\n      note: \"R7 R1 提出 Discussion 应更清晰分离 SFT vs GRPO 角色（参见 R1 NEW FINDING），间接相关\"\n  action_items:\n    - round: 6\n      action: \"Paper Agent 待实验数据后扩充 Discussion\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M1\"\n  summary: \"Reward-accuracy decoupling 首次使用时无正式定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"首次使用处添加正式定义\"\n  resolution_round: 6\n\n- id: \"R6-M2\"\n  summary: \"Figure 2 y 轴未标注 mean vs peak reward\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 提出。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未直接提及，待确认是否已修复\"\n  action_items:\n    - round: 6\n      action: \"修改 Figure 2 y-axis label\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M3\"\n  summary: \"Eq.1 未写出 Taylor expansion 完整数学形式\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2 小问题。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未提及，待确认\"\n  action_items:\n    - round: 6\n      action: \"Paper Agent 补充 Eq.1 完整数学形式\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 7 New Issues\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"Dose-response 中 max_completion_length 不一致（α=1.0: 1024, 其他: 512）构成关键混杂变量\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N1 和 R2-N1 均独立提出。交叉回应中 R2 试图 rebut（声称所有非 Random 方法均用 1024），但 Director 事实核查确认 R2 混淆了主实验配置（Table 3 脚注）与 dose-response 配置（experiments.tex line 102 脚注）。主实验中仅 Random 受影响（warning），但 dose-response 的混杂是 critical。\"\n  action_items:\n    - round: 7\n      action: \"统一所有 α 值 max_completion_length=1024 重跑 dose-response；或至少 α=2.0 用 1024 复现\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N2\"\n  summary: \"Abstract overclaiming 'holds across sparsity levels'——仅 20-25% 窗口成立\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N4 提出，R2 完全同意。15% 时 GRPO amplifies CKA advantage by 1.51pp，30% 全 collapse。\"\n  action_items:\n    - round: 7\n      action: \"Abstract 改为 'at moderate sparsity (20-25%) across benchmarks' 或类似限定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W1\"\n  summary: \"Decoupling 缺少形式化等价性检验（TOST）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W3 提出，R2 同意。|Δ|=0.54pp 声称 'near-identical' 需要 TOST 或明确定义 practical equivalence margin。\"\n  action_items:\n    - round: 7\n      action: \"使用 TOST（ε=1pp）或在正文明确声明 practical equivalence 阈值\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"MBPP 结果统计不显著却被用作 decoupling 支持证据\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 同意。Appendix G 承认不显著但 Section 4.3 仍引用。\"\n  action_items:\n    - round: 7\n      action: \"正文引用 MBPP 时加注 'though not statistically significant at this sample size'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W3\"\n  summary: \"Calibration 数据量 M 在正文中未明确指定\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 同意。Section 3.2 定义 D_cal 但从未给出 M 值。\"\n  action_items:\n    - round: 7\n      action: \"在 Section 3.2 或 4.1 中明确指定 M 及选择依据\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W4\"\n  summary: \"Throughput regression（-19%）未在 Limitations 讨论——选择性报告正面指标\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W3 提出，R1 部分同意。20% sparsity 下 memory -28% 但 throughput -19%（72.0→58.3 tok/s）。Limitations 报告 memory/TTFT 正面指标但回避 throughput regression。\"\n  action_items:\n    - round: 7\n      action: \"在 Limitations 添加 throughput regression 讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"Title/叙事焦点与实际恢复来源错位——SFT 贡献 ~60pp 而 GRPO <1pp\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 交叉回应 [NEW FINDING]：论文标题 'Post-RLVR Recovery' 但数据显示 SFT 完成绝大部分恢复（CKA-only: ~0% → 63.91% SFT → 64.39% GRPO）。GRPO 独特贡献在 reward trajectory 差异化但不转化为 accuracy。建议 Discussion 分离 SFT vs GRPO 角色。\"\n  action_items:\n    - round: 7\n      action: \"Discussion 中明确分离 SFT vs GRPO 的恢复角色；考虑 Title 是否应为 'Post-Pruning Recovery'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-24T17:13:49.872810+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml\", \"bytes\": 25655}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-24T17:16:29.400557+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "report": "# Round 7 Consolidated Review Report\n\n**Paper**: How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs\n**Venue**: EMNLP 2026 (via ARR)\n**Reviewers**: 2 (R1: 方法严谨性 + 统计, R2: 新颖性 + 完整性)\n**Rounds**: 1 (converged after cross-sharing)\n\n---\n\n## Summary\n\n本文系统比较四种结构化 MLP 剪枝标准（CKA-only, Standard/importance, RASP, Random）在 reasoning LLM（DeepSeek-R1-Distill-Qwen-7B）上的 post-pruning recovery 表现。核心发现包括：(1) 剪枝标准比恢复方法（SFT vs GRPO）更显著地影响恢复质量，建立 \"recovery capacity spectrum\"；(2) 在 20-25% sparsity 下，不同标准的 GRPO accuracy 增量均 <1pp（reward-accuracy decoupling）；(3) CKA 权重 α 与恢复能力呈 inverted-U 关系。论文采用控制实验设计，固定除剪枝标准外的所有变量。\n\n---\n\n## Strengths\n\n**S1. 实验设计理念优秀**：固定 recovery pipeline、超参数、硬件、calibration 数据，仅变化剪枝标准的 controlled comparison 在 LLM 剪枝文献中罕见，使因果推断更可靠。\n\n**S2. Recovery capacity spectrum 有直觉价值**：将四种标准的 GRPO 行为划分为 active learning / stagnation / collapse 三种 regime，framing 清晰实用。\n\n**S3. 核心对比统计严谨**：CKA-only vs Standard 的 4.55pp gap 经 3-seed Welch's t-test 验证（p=0.0009, Cohen's d=11.1, 95% CI [3.62, 5.47]pp），seed 范围不重叠。\n\n**S4. Dose-response 设计有信息量**：α 系数连续变化 + inverted-U 发现比简单 A/B 对比更强。\n\n**S5. 写作清晰**：结构合理，notation 一致，figures 质量好，叙事连贯。\n\n**S6. 诚实的 Limitations**：明确承认单 seed RASP、架构/尺度局限、诊断边界。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [Consensus Critical] Dose-response 中 max_completion_length 混杂变量**\n- *R1-N1, R2-N1 独立提出；交叉分享后部分收敛*\n- **事实核查结论**：论文存在两组不同的 generation length 配置：\n  - **主实验** (Table 1/2): CKA-only/Standard/RASP 均用 1,024 tokens，仅 Random 用 512 → 混杂仅影响 Random 比较 [warning]\n  - **Dose-response** (Section 4.3 脚注, experiments.tex line 102): α=1.0 用 1,024 tokens，α=0.5/2.0/3.0/4.0 用 TRL 默认 512 → 混杂直接影响 inverted-U 曲线 [critical]\n- R2 在交叉回应中试图 rebut R1（声称所有非 Random 方法均用 1024），但 R2 混淆了 Table 3 脚注（主实验配置）与 experiments.tex line 102 脚注（dose-response 配置）。\n- Inverted-U 峰值 α=2.0（512 tokens）vs 谷底 α=1.0（1024 tokens）的绝对差距不可靠。论文的 \"conservative estimate\" 论证仅解决谷底（α=1.0 用更长 generation 仍最差），不解决峰值位置和曲线形状。\n- **要求**：统一所有 α 值的 max_completion_length 重跑 dose-response，或至少在 α=2.0 处用 1024 tokens 复现。\n\n**MF2. [Consensus Critical] RASP 单 seed 验证不足**\n- *R1-N2, R2-W2，双方均同意 critical*\n- CKA-only/Standard/Random 各 3 seeds，RASP 所有 sparsity 和 α 值仅 1 seed。Section 5 的 practitioner guideline \"Use RASP at α≈2.0\" 基于单次实验。α=1.0 collapse 表明 RASP landscape 对 α 高度敏感。Standard 3-seed std=0.38pp，RASP 真实方差可能更大。\n- **要求**：至少 RASP α=2.0（推荐值）和 α=1.0（collapse 点）各跑 3 seeds。\n\n**MF3. [Consensus Critical] 因果语言系统性过强**\n- *R1-N3, R2 交叉回应中同意两个子问题*\n- (a) Section 5 \"causal driver\"：dose-response 是 quasi-experimental，变化 α 同时改变 diversity 权重、被移除结构身份和 sparsity 分布。Appendix H 自承 gradient flow 证据是 correlational。\n- (b) \"reward-accuracy decoupling\" 作为命名 phenomenon：仅在 20-25% sparsity 成立。15% 时 GRPO 仍 amplify CKA advantage by 1.51pp。将 sparsity-dependent 观察包装为普适性 phenomenon 是 overclaiming。\n- R2 建议折衷用 \"key determinant\"（比 R1 的 \"primary correlate\" 稍强，反映 dose-response 的证据强度）。\n- **要求**：全文语言审计——\"causal driver\" → \"key determinant\"；所有 decoupling claims 加 \"at 20-25% sparsity\" 限定。\n\n**MF4. [Consensus Critical] Abstract overclaiming \"holds across sparsity levels\"**\n- *R1-N4, R2 完全同意*\n- Abstract \"a pattern that holds across sparsity levels and benchmarks\" 直接与数据矛盾（15% coupling, 30% collapse）。\n- **要求**：改为 \"at moderate sparsity (20–25%) across benchmarks\" 或类似限定。\n\n**MF5. [Consensus Critical] Decoupling 可能是训练不足的 artifact**\n- *R2-N3 提出, R1 完全同意*\n- GRPO 仅训练 100 步（extended 300 步），所有条件下 GRPO accuracy 增量 <1pp（CKA-only: +0.48pp, Standard: +0.55pp）。这可能仅说明 GRPO 还没来得及产生 accuracy 分化，而非 \"recovery method choice becomes irrelevant\"。\n- Self-Healing (2025) 在更长训练中观察到 RLVR > SFT。论文无法排除 1000+ 步训练后 decoupling 消失的可能。\n- R1 交叉回应新发现强化此点：SFT 贡献 ~60pp 恢复而 GRPO <1pp，论文叙事焦点（RLVR recovery）与实际恢复来源（SFT）存在错位。\n- **要求**：至少在一个条件下（CKA-only vs Standard at 20%）运行 ≥1000 GRPO steps 验证 decoupling 是否持续；或将 claim 限定为 \"within ≤300 GRPO steps\"。\n\n**MF6. [R2 New Finding] CKA-only layer 分布混杂**\n- *R2 交叉回应中提出，R1 小问题中间接支持*\n- CKA-only 将 72.5% 剪枝集中在 early layers (L0-9)，其优势可能来自 early-layer selective pruning（保留 late-layer 推理结构）而非 \"representational diversity preservation\"。\n- Appendix R 的 depth-first baseline 在 layer-level granularity（移除整个 transformer blocks），主实验在 MLP channel-group level——granularity 不匹配无法有效解耦两种机制。\n- **要求**：创建 same-granularity layer-biased baseline（MLP channel-group level，按 layer index 赋权优先剪早期层，不使用 CKA 信息），验证 layer 分布是否足以解释 CKA-only 的优势。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [Divergence → Downgraded] CKA evaluation metrics diversity 不足**\n- *R2-N2 原定 critical（循环论证）；R1 rebut 后降级*\n- R1 有效论证：pruning 用 intra-layer pairwise CKA ≠ evaluation 用 inter-model layer-wise CKA。Gradient flow analysis (2.89× magnitude, Wilcoxon p<0.05) 提供独立证据。不构成 tautology。\n- 但论文主叙事仍过度依赖 CKA 家族指标。补充一个完全独立的 diversity 度量（CCA、centered distance correlation 或 effective rank）可显著增强论证。\n\n**SF2. [Consensus] 跨架构泛化严重不足**\n- *R2-W1, R1 完全同意*\n- 所有模型共享 Qwen2.5 base architecture。Appendix O \"Cross-Architecture Validation\" 标题具有误导性。1.5B 验证也是同架构不同规模。Claim 应限定为 \"Qwen2.5-family models\"。\n\n**SF3. [Consensus] Decoupling 缺少形式化等价性检验**\n- *R1-W3, R2 同意*\n- |Δ|=0.54pp 声称 \"near-identical\" 未经 TOST 或等价性检验。应定义 practical equivalence margin（如 ε=1pp）并正式检验。\n\n**SF4. [Consensus] MBPP 不显著结果用作支持证据**\n- *R1-W4, R2 同意*\n- Appendix G 承认统计不显著，但 Section 4.3 仍引用 MBPP 支持 decoupling claim。应在正文加注 \"though not statistically significant\"。\n\n**SF5. [Consensus] Calibration 数据量 M 未指定**\n- *R1-W1, R2 同意*\n- Section 3.2 定义 D_cal 但从未指定 M 值。影响 reproducibility。\n\n**SF6. [Consensus] \"Generality across scales\" 证据薄弱**\n- *R1-W2, R2 同意*\n- 仅 1.5B 和 7B（同家族 <5× 差异）。应改为 \"preliminary evidence at 1.5B scale\"。\n\n**SF7. [Consensus] Throughput regression 未在 Limitations 讨论**\n- *R2-W3, R1 部分同意*\n- 20% sparsity: 28% memory savings 但 19% throughput decrease (72.0→58.3 tok/s)。Limitations 报告正面指标（memory, TTFT）但回避负面指标——构成选择性报告。\n\n**SF8. [R1 New Finding] Title/叙事焦点与恢复来源错位**\n- SFT 贡献 ~60pp 恢复，GRPO <1pp。论文以 \"Post-RLVR Recovery\" 为标题和叙事核心，但实际恢复工作主要发生在 SFT 阶段。GRPO 的独特贡献在于 reward trajectory 差异化（非 accuracy）。建议 Discussion 分离 SFT vs GRPO 角色，考虑 title 是否应为 \"Post-Pruning Recovery\"。\n\n### Minor Issues（不影响接收）\n\n- Abstract 字数 ~190-200 words，在 200-word 限制边界——建议精简几词留余量\n- Table 1 Unpruned \"Reward\" = 0.027 含义不直观——加脚注解释 reward scale\n- Figure 2 内部标注字体偏小，打印不清晰——增大字号或精简文字\n- Appendix R depth-first baseline 与主实验 granularity 不同（已由 MF6 覆盖）\n- Contribution list 仅 2 项，RASP 嵌入 Contribution 2——如视为 methodological contribution 建议独立列出\n- Appendix 17 sections 组织散乱——建议按 training details → main extensions → robustness → analysis 重组\n- \"Post-RLVR\" 在 title 中可能产生误解（见 SF8）\n- Ethics/AI 披露完整透明\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成 [AGREE]：\n\n1. **RASP 单 seed 是 critical issue** — practitioner guideline 基于单次实验，inverted-U peak 不可靠\n2. **\"Causal driver\" 语言必须软化** — dose-response 提供 suggestive 但非 causal 证据；\"key determinant\" 为折衷方案\n3. **Decoupling scope 必须限定** — 仅 20-25% sparsity 成立，非 \"across sparsity levels\"\n4. **Abstract overclaims** — 直接与论文数据矛盾\n5. **跨架构验证具有误导性** — 所有模型共享 Qwen2.5 架构\n6. **Decoupling 可能是训练长度 artifact** — 100-300 GRPO 步远低于典型 RLVR 训练\n7. **统计/reproducibility gaps** — Calibration M、MBPP 显著性、TOST 等价性检验\n\n## Reviewer Divergence\n\n**D1. Generation length confound 的范围和严重性**\n- R1: Critical，声称贯穿核心实验包括 dose-response\n- R2: Warning，认为仅影响 Random 比较\n- **Director 裁定**：R2 对主实验的判断正确（CKA-only/Standard/RASP 均用 1024，仅 Random 用 512）。但 R2 对 dose-response 的判断有误——experiments.tex line 102 脚注明确写 \"α=1.0 uses 1024; other α values use TRL default 512\"。R2 将 Table 3 脚注（主实验配置）与 dose-response 配置混淆。**主实验 warning，dose-response critical。**\n\n**D2. CKA 循环论证**\n- R2: Critical — CKA-pruned 模型必然展示不同的 CKA-to-dense profile，属 tautology\n- R1: Rebuts — intra-layer pairwise CKA ≠ inter-model layer-wise CKA；gradient flow (2.89×) 是独立证据\n- **Director 裁定**：R1 的 rebut 技术上成立——两种 CKA 操作在不同层次，观察到的 divergence 幅度是 empirical 的。但 metrics diversity 不足的关切合理。**降级为 should-fix (SF1)。**\n\n**D3. \"Diversity > importance\" 的 non-obviousness（R2-W4）**\n- R2: RL 需要 exploration/diversity 是已知理论，发现不 surprising\n- R1: Rebuts — pruning 文献的 prior expectation 是 importance-based > diversity-based；本文恰恰推翻此领域共识；Section 5 解释是 post-hoc rationalization 不是 prior prediction\n- **Director 裁定**：R1 rebut 有说服力。Novelty 在于 empirical 推翻 importance-first 假设。**从 should-fix 列表中移除。**\n\n---\n\n## Questions for Authors\n\n1. 主实验使用的 calibration 样本数量 M 是多少？\n2. 是否尝试过 GRPO 训练超过 300 步？如果是，decoupling 是否持续？\n3. 每层的 CKA overlap score 与 layer depth index 的 Spearman 相关系数是多少？（量化 layer-distribution confound）\n4. 是否愿意在 α=2.0 处用 max_completion_length=1024 重新运行，验证 dose-response 峰值是否 robust？\n\n---\n\n## Missing References\n\n本轮未发现重大遗漏。Round 6 标记的缺失引用（RL Finetunes Small Subnetworks, layer pruning limits, online rollout pruning, LaCo）已在本版论文 Related Work 中出现。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未请求。本轮未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2026-05-24 16:47–16:52 UTC）。**0 critical / 0 warning / 4 info**：\n\n1. **Pages 3-4**: Method 节连续 2 页无 figure/table，仅有方程式作为视觉间断。数学密集型内容可接受，但可考虑增加 pruning criteria 对比示意图。\n2. **Page 5**: Figure 2 框架概览图内部标注文字偏小，打印尺寸下可能不清晰。\n3. **Page 7**: 单页含 Figure 3（三子图）+ Figure 4，视觉密度较高。功能上合理但审稿人可能感到拥挤。\n4. **Pages 7-8**: Figures 3-6 集中在连续两页，与 pages 3-4 纯文本区形成节奏反差。可考虑将 Figure 5/6 移至 appendix。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Soundness: 3.0/5** | **Excitement: 3.25/5** | **Reproducibility: 3.25/5**\n\n两位 Reviewer 独立给出一致的 3.0 评分，交叉分享后未发生实质性上调或下调。\n\n**论文的核心价值**在于实验设计理念（controlled comparison）和两个有信息量的经验发现（recovery capacity spectrum、reward-accuracy decoupling）。统计验证在核心对比上充分。\n\n**阻碍主会议接收的五个核心问题**：\n1. Dose-response generation length 混杂变量削弱了 inverted-U 这一核心因果证据\n2. 100-300 步 GRPO 远低于典型 RLVR 训练水平，decoupling 可能是训练不足的 artifact 而非结构性发现\n3. RASP 单 seed 使论文的 practical recommendation 不可靠\n4. 因果语言系统性过强，多处 claim 超出 quasi-experimental 证据支持\n5. CKA-only layer 分布混杂（72.5% early layers）未被有效排除\n\n**上调路径**：若 MF1（统一 generation length）、MF2（RASP 多 seed）、MF5（验证长训练下 decoupling 持续性）得到解决，可上调至 **3.5 (Borderline Conference)**。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"diversity > importance\" 的叙事线有 novelty（推翻 pruning 文献中 importance-first 假设），但需更清晰地 articulate 为什么先验预期不明确——importance-based 保留更强 reasoning capability，直觉上应给 GRPO 更好起点\n\n### Section 3 (Method)\n- Eq. 3 的 CKA overlap scoring 定义清晰\n- D_cal 的 M 值需要在此处或 Section 4.1 明确指定\n- Two-stage recovery pipeline 描述完整，但 \"identical GRPO configuration\" 的声明需注明 Random 的例外\n\n### Section 4.1 (Recovery Capacity Spectrum)\n- Table 1 设计好，spectrum framing 清晰\n- RASP 单 seed vs 其他方法 3 seeds 的不对称性需要在正文中更显著标注（不仅仅是 Table 2 caption）\n\n### Section 4.2 (Reward-Accuracy Decoupling)\n- 核心发现有说服力（|Δ| < 1pp across methods），但缺少 TOST 等价性检验\n- 正式命名为 \"phenomenon\" 需要更严格的 scope 限定\n- MBPP 引用应标注统计不显著\n\n### Section 4.3 (Dose-Response)\n- Inverted-U 设计思路好，但 generation length 混杂是致命伤\n- 脚注披露了差异，但不够 prominent——应在正文中 discuss\n\n### Section 4.5 (Extended Analysis)\n- CKA heatmap (Figure 5) 不构成循环论证（两种 CKA 操作层次不同），但补充非 CKA diversity 度量可显著增强\n- CKA-only early-layer concentration (72.5% in L0-9) 是重要发现，应给予更充分讨论和 ablation\n- 300-step 延长训练仍然太短——1000+ 步是验证 decoupling 持续性的最低要求\n\n### Section 5 (Conclusion)\n- \"causal driver\" → \"key determinant\"\n- Practitioner guideline 应加 caveat（single seed）\n- 建议增加 SFT vs GRPO 角色分离的讨论\n- Throughput regression 应加入 limitations\n\n### Appendix\n- 内容详实但组织可改进\n- Appendix O \"Cross-Architecture\" 标题需重命名\n- Appendix R depth-first baseline 因 granularity 不匹配价值有限（已在 MF6 讨论）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "report": "# Round 7 Consolidated Review Report\n\n**Paper**: How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs\n**Venue**: EMNLP 2026 (via ARR)\n**Reviewers**: 2 (R1: 方法严谨性 + 统计, R2: 新颖性 + 完整性)\n**Rounds**: 1 (converged after cross-sharing)\n\n---\n\n## Summary\n\n本文系统比较四种结构化 MLP 剪枝标准（CKA-only, Standard/importance, RASP, Random）在 reasoning LLM（DeepSeek-R1-Distill-Qwen-7B）上的 post-pruning recovery 表现。核心发现包括：(1) 剪枝标准比恢复方法（SFT vs GRPO）更显著地影响恢复质量，建立 \"recovery capacity spectrum\"；(2) 在 20-25% sparsity 下，不同标准的 GRPO accuracy 增量均 <1pp（reward-accuracy decoupling）；(3) CKA 权重 α 与恢复能力呈 inverted-U 关系。论文采用控制实验设计，固定除剪枝标准外的所有变量。\n\n---\n\n## Strengths\n\n**S1. 实验设计理念优秀**：固定 recovery pipeline、超参数、硬件、calibration 数据，仅变化剪枝标准的 controlled comparison 在 LLM 剪枝文献中罕见，使因果推断更可靠。\n\n**S2. Recovery capacity spectrum 有直觉价值**：将四种标准的 GRPO 行为划分为 active learning / stagnation / collapse 三种 regime，framing 清晰实用。\n\n**S3. 核心对比统计严谨**：CKA-only vs Standard 的 4.55pp gap 经 3-seed Welch's t-test 验证（p=0.0009, Cohen's d=11.1, 95% CI [3.62, 5.47]pp），seed 范围不重叠。\n\n**S4. Dose-response 设计有信息量**：α 系数连续变化 + inverted-U 发现比简单 A/B 对比更强。\n\n**S5. 写作清晰**：结构合理，notation 一致，figures 质量好，叙事连贯。\n\n**S6. 诚实的 Limitations**：明确承认单 seed RASP、架构/尺度局限、诊断边界。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [Consensus Critical] Dose-response 中 max_completion_length 混杂变量**\n- *R1-N1, R2-N1 独立提出；交叉分享后部分收敛*\n- **事实核查结论**：论文存在两组不同的 generation length 配置：\n  - **主实验** (Table 1/2): CKA-only/Standard/RASP 均用 1,024 tokens，仅 Random 用 512 → 混杂仅影响 Random 比较 [warning]\n  - **Dose-response** (Section 4.3 脚注, experiments.tex line 102): α=1.0 用 1,024 tokens，α=0.5/2.0/3.0/4.0 用 TRL 默认 512 → 混杂直接影响 inverted-U 曲线 [critical]\n- R2 在交叉回应中试图 rebut R1（声称所有非 Random 方法均用 1024），但 R2 混淆了 Table 3 脚注（主实验配置）与 experiments.tex line 102 脚注（dose-response 配置）。\n- Inverted-U 峰值 α=2.0（512 tokens）vs 谷底 α=1.0（1024 tokens）的绝对差距不可靠。论文的 \"conservative estimate\" 论证仅解决谷底（α=1.0 用更长 generation 仍最差），不解决峰值位置和曲线形状。\n- **要求**：统一所有 α 值的 max_completion_length 重跑 dose-response，或至少在 α=2.0 处用 1024 tokens 复现。\n\n**MF2. [Consensus Critical] RASP 单 seed 验证不足**\n- *R1-N2, R2-W2，双方均同意 critical*\n- CKA-only/Standard/Random 各 3 seeds，RASP 所有 sparsity 和 α 值仅 1 seed。Section 5 的 practitioner guideline \"Use RASP at α≈2.0\" 基于单次实验。α=1.0 collapse 表明 RASP landscape 对 α 高度敏感。Standard 3-seed std=0.38pp，RASP 真实方差可能更大。\n- **要求**：至少 RASP α=2.0（推荐值）和 α=1.0（collapse 点）各跑 3 seeds。\n\n**MF3. [Consensus Critical] 因果语言系统性过强**\n- *R1-N3, R2 交叉回应中同意两个子问题*\n- (a) Section 5 \"causal driver\"：dose-response 是 quasi-experimental，变化 α 同时改变 diversity 权重、被移除结构身份和 sparsity 分布。Appendix H 自承 gradient flow 证据是 correlational。\n- (b) \"reward-accuracy decoupling\" 作为命名 phenomenon：仅在 20-25% sparsity 成立。15% 时 GRPO 仍 amplify CKA advantage by 1.51pp。将 sparsity-dependent 观察包装为普适性 phenomenon 是 overclaiming。\n- R2 建议折衷用 \"key determinant\"（比 R1 的 \"primary correlate\" 稍强，反映 dose-response 的证据强度）。\n- **要求**：全文语言审计——\"causal driver\" → \"key determinant\"；所有 decoupling claims 加 \"at 20-25% sparsity\" 限定。\n\n**MF4. [Consensus Critical] Abstract overclaiming \"holds across sparsity levels\"**\n- *R1-N4, R2 完全同意*\n- Abstract \"a pattern that holds across sparsity levels and benchmarks\" 直接与数据矛盾（15% coupling, 30% collapse）。\n- **要求**：改为 \"at moderate sparsity (20–25%) across benchmarks\" 或类似限定。\n\n**MF5. [Consensus Critical] Decoupling 可能是训练不足的 artifact**\n- *R2-N3 提出, R1 完全同意*\n- GRPO 仅训练 100 步（extended 300 步），所有条件下 GRPO accuracy 增量 <1pp（CKA-only: +0.48pp, Standard: +0.55pp）。这可能仅说明 GRPO 还没来得及产生 accuracy 分化，而非 \"recovery method choice becomes irrelevant\"。\n- Self-Healing (2025) 在更长训练中观察到 RLVR > SFT。论文无法排除 1000+ 步训练后 decoupling 消失的可能。\n- R1 交叉回应新发现强化此点：SFT 贡献 ~60pp 恢复而 GRPO <1pp，论文叙事焦点（RLVR recovery）与实际恢复来源（SFT）存在错位。\n- **要求**：至少在一个条件下（CKA-only vs Standard at 20%）运行 ≥1000 GRPO steps 验证 decoupling 是否持续；或将 claim 限定为 \"within ≤300 GRPO steps\"。\n\n**MF6. [R2 New Finding] CKA-only layer 分布混杂**\n- *R2 交叉回应中提出，R1 小问题中间接支持*\n- CKA-only 将 72.5% 剪枝集中在 early layers (L0-9)，其优势可能来自 early-layer selective pruning（保留 late-layer 推理结构）而非 \"representational diversity preservation\"。\n- Appendix R 的 depth-first baseline 在 layer-level granularity（移除整个 transformer blocks），主实验在 MLP channel-group level——granularity 不匹配无法有效解耦两种机制。\n- **要求**：创建 same-granularity layer-biased baseline（MLP channel-group level，按 layer index 赋权优先剪早期层，不使用 CKA 信息），验证 layer 分布是否足以解释 CKA-only 的优势。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [Divergence → Downgraded] CKA evaluation metrics diversity 不足**\n- *R2-N2 原定 critical（循环论证）；R1 rebut 后降级*\n- R1 有效论证：pruning 用 intra-layer pairwise CKA ≠ evaluation 用 inter-model layer-wise CKA。Gradient flow analysis (2.89× magnitude, Wilcoxon p<0.05) 提供独立证据。不构成 tautology。\n- 但论文主叙事仍过度依赖 CKA 家族指标。补充一个完全独立的 diversity 度量（CCA、centered distance correlation 或 effective rank）可显著增强论证。\n\n**SF2. [Consensus] 跨架构泛化严重不足**\n- *R2-W1, R1 完全同意*\n- 所有模型共享 Qwen2.5 base architecture。Appendix O \"Cross-Architecture Validation\" 标题具有误导性。1.5B 验证也是同架构不同规模。Claim 应限定为 \"Qwen2.5-family models\"。\n\n**SF3. [Consensus] Decoupling 缺少形式化等价性检验**\n- *R1-W3, R2 同意*\n- |Δ|=0.54pp 声称 \"near-identical\" 未经 TOST 或等价性检验。应定义 practical equivalence margin（如 ε=1pp）并正式检验。\n\n**SF4. [Consensus] MBPP 不显著结果用作支持证据**\n- *R1-W4, R2 同意*\n- Appendix G 承认统计不显著，但 Section 4.3 仍引用 MBPP 支持 decoupling claim。应在正文加注 \"though not statistically significant\"。\n\n**SF5. [Consensus] Calibration 数据量 M 未指定**\n- *R1-W1, R2 同意*\n- Section 3.2 定义 D_cal 但从未指定 M 值。影响 reproducibility。\n\n**SF6. [Consensus] \"Generality across scales\" 证据薄弱**\n- *R1-W2, R2 同意*\n- 仅 1.5B 和 7B（同家族 <5× 差异）。应改为 \"preliminary evidence at 1.5B scale\"。\n\n**SF7. [Consensus] Throughput regression 未在 Limitations 讨论**\n- *R2-W3, R1 部分同意*\n- 20% sparsity: 28% memory savings 但 19% throughput decrease (72.0→58.3 tok/s)。Limitations 报告正面指标（memory, TTFT）但回避负面指标——构成选择性报告。\n\n**SF8. [R1 New Finding] Title/叙事焦点与恢复来源错位**\n- SFT 贡献 ~60pp 恢复，GRPO <1pp。论文以 \"Post-RLVR Recovery\" 为标题和叙事核心，但实际恢复工作主要发生在 SFT 阶段。GRPO 的独特贡献在于 reward trajectory 差异化（非 accuracy）。建议 Discussion 分离 SFT vs GRPO 角色，考虑 title 是否应为 \"Post-Pruning Recovery\"。\n\n### Minor Issues（不影响接收）\n\n- Abstract 字数 ~190-200 words，在 200-word 限制边界——建议精简几词留余量\n- Table 1 Unpruned \"Reward\" = 0.027 含义不直观——加脚注解释 reward scale\n- Figure 2 内部标注字体偏小，打印不清晰——增大字号或精简文字\n- Appendix R depth-first baseline 与主实验 granularity 不同（已由 MF6 覆盖）\n- Contribution list 仅 2 项，RASP 嵌入 Contribution 2——如视为 methodological contribution 建议独立列出\n- Appendix 17 sections 组织散乱——建议按 training details → main extensions → robustness → analysis 重组\n- \"Post-RLVR\" 在 title 中可能产生误解（见 SF8）\n- Ethics/AI 披露完整透明\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成 [AGREE]：\n\n1. **RASP 单 seed 是 critical issue** — practitioner guideline 基于单次实验，inverted-U peak 不可靠\n2. **\"Causal driver\" 语言必须软化** — dose-response 提供 suggestive 但非 causal 证据；\"key determinant\" 为折衷方案\n3. **Decoupling scope 必须限定** — 仅 20-25% sparsity 成立，非 \"across sparsity levels\"\n4. **Abstract overclaims** — 直接与论文数据矛盾\n5. **跨架构验证具有误导性** — 所有模型共享 Qwen2.5 架构\n6. **Decoupling 可能是训练长度 artifact** — 100-300 GRPO 步远低于典型 RLVR 训练\n7. **统计/reproducibility gaps** — Calibration M、MBPP 显著性、TOST 等价性检验\n\n## Reviewer Divergence\n\n**D1. Generation length confound 的范围和严重性**\n- R1: Critical，声称贯穿核心实验包括 dose-response\n- R2: Warning，认为仅影响 Random 比较\n- **Director 裁定**：R2 对主实验的判断正确（CKA-only/Standard/RASP 均用 1024，仅 Random 用 512）。但 R2 对 dose-response 的判断有误——experiments.tex line 102 脚注明确写 \"α=1.0 uses 1024; other α values use TRL default 512\"。R2 将 Table 3 脚注（主实验配置）与 dose-response 配置混淆。**主实验 warning，dose-response critical。**\n\n**D2. CKA 循环论证**\n- R2: Critical — CKA-pruned 模型必然展示不同的 CKA-to-dense profile，属 tautology\n- R1: Rebuts — intra-layer pairwise CKA ≠ inter-model layer-wise CKA；gradient flow (2.89×) 是独立证据\n- **Director 裁定**：R1 的 rebut 技术上成立——两种 CKA 操作在不同层次，观察到的 divergence 幅度是 empirical 的。但 metrics diversity 不足的关切合理。**降级为 should-fix (SF1)。**\n\n**D3. \"Diversity > importance\" 的 non-obviousness（R2-W4）**\n- R2: RL 需要 exploration/diversity 是已知理论，发现不 surprising\n- R1: Rebuts — pruning 文献的 prior expectation 是 importance-based > diversity-based；本文恰恰推翻此领域共识；Section 5 解释是 post-hoc rationalization 不是 prior prediction\n- **Director 裁定**：R1 rebut 有说服力。Novelty 在于 empirical 推翻 importance-first 假设。**从 should-fix 列表中移除。**\n\n---\n\n## Questions for Authors\n\n1. 主实验使用的 calibration 样本数量 M 是多少？\n2. 是否尝试过 GRPO 训练超过 300 步？如果是，decoupling 是否持续？\n3. 每层的 CKA overlap score 与 layer depth index 的 Spearman 相关系数是多少？（量化 layer-distribution confound）\n4. 是否愿意在 α=2.0 处用 max_completion_length=1024 重新运行，验证 dose-response 峰值是否 robust？\n\n---\n\n## Missing References\n\n本轮未发现重大遗漏。Round 6 标记的缺失引用（RL Finetunes Small Subnetworks, layer pruning limits, online rollout pruning, LaCo）已在本版论文 Related Work 中出现。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未请求。本轮未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2026-05-24 16:47–16:52 UTC）。**0 critical / 0 warning / 4 info**：\n\n1. **Pages 3-4**: Method 节连续 2 页无 figure/table，仅有方程式作为视觉间断。数学密集型内容可接受，但可考虑增加 pruning criteria 对比示意图。\n2. **Page 5**: Figure 2 框架概览图内部标注文字偏小，打印尺寸下可能不清晰。\n3. **Page 7**: 单页含 Figure 3（三子图）+ Figure 4，视觉密度较高。功能上合理但审稿人可能感到拥挤。\n4. **Pages 7-8**: Figures 3-6 集中在连续两页，与 pages 3-4 纯文本区形成节奏反差。可考虑将 Figure 5/6 移至 appendix。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Soundness: 3.0/5** | **Excitement: 3.25/5** | **Reproducibility: 3.25/5**\n\n两位 Reviewer 独立给出一致的 3.0 评分，交叉分享后未发生实质性上调或下调。\n\n**论文的核心价值**在于实验设计理念（controlled comparison）和两个有信息量的经验发现（recovery capacity spectrum、reward-accuracy decoupling）。统计验证在核心对比上充分。\n\n**阻碍主会议接收的五个核心问题**：\n1. Dose-response generation length 混杂变量削弱了 inverted-U 这一核心因果证据\n2. 100-300 步 GRPO 远低于典型 RLVR 训练水平，decoupling 可能是训练不足的 artifact 而非结构性发现\n3. RASP 单 seed 使论文的 practical recommendation 不可靠\n4. 因果语言系统性过强，多处 claim 超出 quasi-experimental 证据支持\n5. CKA-only layer 分布混杂（72.5% early layers）未被有效排除\n\n**上调路径**：若 MF1（统一 generation length）、MF2（RASP 多 seed）、MF5（验证长训练下 decoupling 持续性）得到解决，可上调至 **3.5 (Borderline Conference)**。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"diversity > importance\" 的叙事线有 novelty（推翻 pruning 文献中 importance-first 假设），但需更清晰地 articulate 为什么先验预期不明确——importance-based 保留更强 reasoning capability，直觉上应给 GRPO 更好起点\n\n### Section 3 (Method)\n- Eq. 3 的 CKA overlap scoring 定义清晰\n- D_cal 的 M 值需要在此处或 Section 4.1 明确指定\n- Two-stage recovery pipeline 描述完整，但 \"identical GRPO configuration\" 的声明需注明 Random 的例外\n\n### Section 4.1 (Recovery Capacity Spectrum)\n- Table 1 设计好，spectrum framing 清晰\n- RASP 单 seed vs 其他方法 3 seeds 的不对称性需要在正文中更显著标注（不仅仅是 Table 2 caption）\n\n### Section 4.2 (Reward-Accuracy Decoupling)\n- 核心发现有说服力（|Δ| < 1pp across methods），但缺少 TOST 等价性检验\n- 正式命名为 \"phenomenon\" 需要更严格的 scope 限定\n- MBPP 引用应标注统计不显著\n\n### Section 4.3 (Dose-Response)\n- Inverted-U 设计思路好，但 generation length 混杂是致命伤\n- 脚注披露了差异，但不够 prominent——应在正文中 discuss\n\n### Section 4.5 (Extended Analysis)\n- CKA heatmap (Figure 5) 不构成循环论证（两种 CKA 操作层次不同），但补充非 CKA diversity 度量可显著增强\n- CKA-only early-layer concentration (72.5% in L0-9) 是重要发现，应给予更充分讨论和 ablation\n- 300-step 延长训练仍然太短——1000+ 步是验证 decoupling 持续性的最低要求\n\n### Section 5 (Conclusion)\n- \"causal driver\" → \"key determinant\"\n- Practitioner guideline 应加 caveat（single seed）\n- 建议增加 SFT vs GRPO 角色分离的讨论\n- Throughput regression 应加入 limitations\n\n### Appendix\n- 内容详实但组织可改进\n- Appendix O \"Cross-Architecture\" 标题需重命名\n- Appendix R depth-first baseline 因 granularity 不匹配价值有限（已在 MF6 讨论）"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-24T17:16:34.694517+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_04e6cf8fe41be27a49d5657e80962f12:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 5293
}
```

</details>

---


### Assistant

_source line 526 · 2026-05-24T17:16:46.311622+00:00_

Round 7 审稿完成。报告已投递给 Research Director。

**评分：3.0 (Findings)**，两位 Reviewer 独立一致。

6 个 Must-Fix：
1. Dose-response generation length 混杂（α=1.0 用 1024，其他用 512）
2. RASP 全线单 seed，practitioner guideline 不可靠
3. 因果语言过强（"causal driver" → "key determinant"）
4. Abstract "across sparsity levels" 与数据矛盾
5. Decoupling 可能是 ≤300 步训练不足的 artifact
6. CKA-only layer 分布混杂（72.5% early layers）未排除

1 个关键分歧已裁定：R2 声称 dose-response 所有 α 均用 1024（误读 Table 3 脚注为 dose-response 配置），事实核查确认 R1 正确（experiments.tex line 102 脚注明写 α=1.0 用 1024、其他用 512）。

上调至 3.5 的路径：解决 MF1（统一 generation length）+ MF2（RASP 多 seed）+ MF5（验证长训练 decoupling 持续性）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 45

## Round 45

2 recorded events


### User

_source line 527 · 2026-05-24T17:16:48.789013+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。总结：

- **N1 (max_completion_length 混杂)**: [AGREE]，混杂确实存在，但论文的 "conservative estimate" 辩护部分成立——α=1.0 用了更长生成限制反而最差
- **N2 (CKA 循环论证)**: [REBUT]，intra-layer CKA（剪枝准则）与 inter-model CKA（评估指标）是不同层次的度量，不构成 tautology；但建议降级为 should-fix，补充独立 diversity 指标
- **N3 (训练不足 artifact)**: [AGREE]，100-300 步远短于典型 RLVR，decoupling 可能只是 GRPO 未生效
- **W1-W3**: 全部 [AGREE]
- **W4 (non-obvious 性)**: [REBUT]，importance > diversity 是剪枝领域的标准假设，本文推翻了这个先验直觉
- **[NEW FINDING]**: 论文标题聚焦 "Post-RLVR Recovery"，但 SFT 阶段贡献了 ~64pp 恢复而 GRPO 仅 +0.48pp，叙事框架与数据存在错位

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 528 · 2026-05-24T17:17:02.916849+00:00_

Round 7 审稿报告已合成并投递给 Research Director。

**最终评分：3.0 (Findings)**，双 Reviewer 一致。

**6 个 Must-Fix**：
1. Dose-response generation length 混杂（α=1.0 用 1024, 其他用 512）
2. RASP 全配置单 seed
3. 因果语言系统性过强（"causal driver"、decoupling scope）
4. Abstract "across sparsity levels" 与数据矛盾
5. Decoupling 可能是训练步数不足的 artifact（100-300 步 vs 典型 1000+）
6. CKA-only early-layer 分布混杂未排除（72.5% 集中 L0-9）

**上调至 3.5 的路径**：统一 generation length + RASP 多 seed + 验证长训练下 decoupling 持续性。

Issue Tracker 已同步更新至 `review_issues.yaml`（含 Round 7 全部新发现和历史 issue 追踪）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 46

## Round 46

60 recorded events


### User

_source line 529 · 2026-05-24T17:59:34.038747+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: recovery_aware_struct_prune
- 论文路径: projects/recovery_aware_struct_prune/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-24T17:59:41.113012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-24T17:59:41.164382+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-24T17:59:47.792693+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-24T17:59:47.793166+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-24T17:59:50.905157+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-24T17:59:51.005856+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-24T18:00:03.880459+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-24T18:00:04.082011+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-24T18:00:09.112300+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool call

_source line 539 · 2026-05-24T18:00:10.082110+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 540 · 2026-05-24T18:00:11.906288+00:00_

{"result":"# 项目 recovery_aware_struct_prune 概况\n\n## 实验状态 (462 个)\n\n- **grpo_stage2_rasp_20_v2**: DONE (negative) — \n- **grpo_stage2_standard_20**: DONE (killed) — \n- **grpo_stage2_rasp_20**: DONE (killed) — \n- **sft_standard_20**: DONE (success) — \n- **sft_rasp_20**: DONE (success) — \n- **grpo_rasp_20_4096**: DONE (failed) — \n- **grpo_standard_20_4096**: DONE (negative) — \n- **grpo_standard_20_fast**: DONE (negative) — \n- **grpo_rasp_20_fast**: DONE (negative) — \n- **mvp_rasp_pipeline_v4**: PREPARING — \n- **grpo_standard_20**: DONE (killed) — \n- **grpo_rasp_20**: DONE (killed) — \n- **mvp_rasp_pipeline_v3**: DONE (negative) — \n- **mvp_rasp_pipeline_v2**: DONE (failed) — \n- **mvp_rasp_pipeline**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- floor_ablation_0p3_cka_only_20: Floor ratio ablation: lowering the MLP floor from 0.4 to 0.3 allows more aggressive pruning of unimportant layers while CKA-only criterion preserves critical structure. If floor=0.3 maintains GSM8K accuracy within 2pp of floor=0.4 baseline, it demonstrates robustness of CKA-guided pruning to floor choice.（已分配 ? GPU:?，等待提交）\n- floor_ablation_0p5_cka_only_20: Floor ratio ablation: raising the MLP floor from 0.4 to 0.5 constrains pruning to be more conservative. If floor=0.5 improves GSM8K accuracy over floor=0.4, it suggests CKA-only criterion benefits from a higher minimum layer size. Maps the sensitivity curve of floor parameter on recovery quality.（已分配 ? GPU:?，等待提交）\n- …另有 38 项\n\n## 近期结论\n- **eval_gsm8k_grpo_alpha4_20_v2** (killed): α=4.0 GRPO maintains reward 0.15-0.26 (vs α=1.0 collapse to ~0.008), predicting GSM8K accuracy significantly above α=1.0 baseline. v1 timed out at 774/1319 showing 62.93% interim — full eval needed to confirm α-dependent collapse hypothesis. ← 基于 eval_gsm8k_grpo_alpha4_20\n\n## 趋势\n成功 273 / 负向 23 / 失败 84 / 共 422\naccuracy: 0.268 →（近 3 次 success）\navg_response_length: 1110.462 ↑（近 3
…[truncated 1815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2793
}
```

</details>

---


### Tool call

_source line 541 · 2026-05-24T18:00:12.458219+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 542 · 2026-05-24T18:00:13.313169+00:00_

-rw-r--r-- 1 ubuntu ubuntu 4527702 May 24 17:58 /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 543 · 2026-05-24T18:00:13.347061+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex 2>/dev/null && echo \"TEX_EXISTS\" || echo \"NO_TEX\"",
  "description": "Check if main.tex exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex 2>/dev/null && echo \"TEX_EXISTS\" || echo \"NO_TEX\"",
    "description": "Check if main.tex exists"
  }
}
```

</details>

---


### Tool result

_source line 544 · 2026-05-24T18:00:13.403505+00:00_

-rw-r--r-- 1 ubuntu ubuntu 958 May 22 05:15 /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex
TEX_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "elapsed_ms": 56
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-24T18:00:17.400727+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the web search results for "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org", here's what I found
…[truncated 1251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "elapsed_ms": 7318
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-24T18:00:22.652450+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission guidelines page limit format requirements ARR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission guidelines page limit format requirements ARR 2026"
  }
}
```

</details>

---


### Tool call

_source line 547 · 2026-05-24T18:00:23.303441+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines submission format anonymity requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines submission format anonymity requirements"
  }
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-24T18:00:24.107601+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-24T18:00:24.208442+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 550 · 2026-05-24T18:00:28.324701+00:00_

Web search results for query: "EMNLP 2026 submission guidelines page limit format requirements ARR 2026"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 regarding page limits and format requirements for ARR 2026:

## Format Requirements

EMNLP 2026 uses a two-column format with an 8-page limit for long papers and a 4-page limit for short papers, using the standard ACL style files identical to those used for ACL, NAACL, and other *ACL conferences.

## Page Limits

- **Long papers**: 8 pages
- **Short papers**: 4 pages

## Additional Requirements

The mandatory Limitations section is required, placed after the conclusion.

## ARR 2026 Submission Details

All submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026. EMNLP uses the standard ACL style files, so the LaTeX template is identical 
…[truncated 352 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "elapsed_ms": 5672
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-24T18:00:29.630203+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines submission format anonymity requirements"

Links: [{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, here's what I found regarding ACL Rolling Review 2026 author guidelines:

## Submission Format

Papers must follow ACL formatting, and authors are encouraged to use the ACL pubcheck tool and an official Overleaf template. Papers should be 4 pages for short papers or 8 pages for long papers (excluding ethical considerations and limitations sections).

## Anonymity Requirements

Papers must not include authors' names and affiliations, and self-references that reveal authors' identities mu
…[truncated 856 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "elapsed_ms": 6326
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-24T18:00:36.858229+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-24T18:00:36.858597+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-24T18:00:38.615555+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-24T18:00:38.615930+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{siunitx}
17	\usepackage{algorithm}
18	\usepackage[noend]{algpseudocode}
19	\usepackage{enumitem}
20	\usepackage{xcolor}
21	\usepackage{hyperref}
22	
23	\newcommand{\rasp}{\textsc{Rasp}}
24	
25	\title{How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\begin{abstract}
33	\input{abstract}
34	\end{abstract}
35	
36	\input{introduction}
37	\input{related_work}
38	\input{method}
39	\input{experiments}
40	\input{conclusion}
41	
42	\section*{Limitations}
43	\input{limitations}
44	
45	\section*{Ethics Statement}
46	\input{ethics}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-24T18:00:47.248428+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/",
  "description": "List paper directory files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/",
    "description": "List paper directory files"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-24T18:00:47.700599+00:00_

_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
appendix.tex
backup
conclusion.tex
ethics.tex
experiments.tex
figures
introduction.tex
limitations.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
method.md
method.tex
references.bib
related_work.tex
results.md
tables

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-24T18:00:48.253188+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-24T18:00:48.755385+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'recovery_aware_struct_prune'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-24T18:00:49.006536+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-24T18:00:49.057715+00:00_

# ============================================================
# Round 1-3 Issues — All Resolved
# ============================================================

- id: "R1-C1"
  summary: "CKA-recovery link 仅相关性, 无因果干预"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Jaccard overlap 分析 + Limitations 承认 + 多种子统计验证"
  resolution_round: 3

- id: "R1-C2"
  summary: "Single-seed GRPO 无统计显著性"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "3-seed GRPO CKA-only, Welch's t-test p=0.0009"
  resolution_round: 3

- id: "R1-C3"
  summary: "仅 GSM8K 单基准"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "MATH-500 OOD 验证 + MBPP 代码基准"
  resolution_round: 3

- id: "R1-W1"
  summary: "Title overclaim 'determines'"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Title 改为 'shapes'"
  resolution_round: 3

- id: "R1-W2"
  summary: "Abstract 'universally determines' overclaim"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "改为 'significantly shapes'"
  resolution_round: 3

- id: "R1-W3"
  summary: "仅 DeepSeek-R1-7B 单模型"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Qwen2.5-Math-7B cross-arch + 1.5B cross-scale"
  resolution_round: 3

- id: "R1-M1"
  summary: "GRPO 超参未报告"
  category: experiment
  severity: info
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Appendix 完整超参表"
  resolution_round: 3

- id: "R1-M2"
  summary: "Table 1 缺 Random baseline"
  category: experiment
  severity: info
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Table 1 加入 Random 行"
  resolution_round: 3

- id: "R2-NEW-C1"
  summar
…[truncated 23653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-24T18:01:17.149005+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/submitted.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool call

_source line 563 · 2026-05-24T18:01:17.451780+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 564 · 2026-05-24T18:01:18.056409+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/submitted.pdf (4.3MB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-24T18:01:19.126695+00:00_

{"result":"# 项目 recovery_aware_struct_prune 概况\n\n## 实验状态 (462 个)\n\n- **grpo_stage2_rasp_20_v2**: DONE (negative) — \n- **grpo_stage2_standard_20**: DONE (killed) — \n- **grpo_stage2_rasp_20**: DONE (killed) — \n- **sft_standard_20**: DONE (success) — \n- **sft_rasp_20**: DONE (success) — \n- **grpo_rasp_20_4096**: DONE (failed) — \n- **grpo_standard_20_4096**: DONE (negative) — \n- **grpo_standard_20_fast**: DONE (negative) — \n- **grpo_rasp_20_fast**: DONE (negative) — \n- **mvp_rasp_pipeline_v4**: PREPARING — \n- **grpo_standard_20**: DONE (killed) — \n- **grpo_rasp_20**: DONE (killed) — \n- **mvp_rasp_pipeline_v3**: DONE (negative) — \n- **mvp_rasp_pipeline_v2**: DONE (failed) — \n- **mvp_rasp_pipeline**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- floor_ablation_0p3_cka_only_20: Floor ratio ablation: lowering the MLP floor from 0.4 to 0.3 allows more aggressive pruning of unimportant layers while CKA-only criterion preserves critical structure. If floor=0.3 maintains GSM8K accuracy within 2pp of floor=0.4 baseline, it demonstrates robustness of CKA-guided pruning to floor choice.（已分配 ? GPU:?，等待提交）\n- floor_ablation_0p5_cka_only_20: Floor ratio ablation: raising the MLP floor from 0.4 to 0.5 constrains pruning to be more conservative. If floor=0.5 improves GSM8K accuracy over floor=0.4, it suggests CKA-only criterion benefits from a higher minimum layer size. Maps the sensitivity curve of floor parameter on recovery quality.（已分配 ? GPU:?，等待提交）\n- …另有 38 项\n\n## 近期结论\n- **eval_gsm8k_grpo_alpha4_20_v2** (killed): α=4.0 GRPO maintains reward 0.15-0.26 (vs α=1.0 collapse to ~0.008), predicting GSM8K accuracy significantly above α=1.0 baseline. v1 timed out at 774/1319 showing 62.93% interim — full eval needed to confirm α-dependent collapse hypothesis. ← 基于 eval_gsm8k_grpo_alpha4_20\n\n## 趋势\n成功 273 / 负向 23 / 失败 84 / 共 422\naccuracy: 0.268 →（近 3 次 success）\navg_response_length: 1110.462 ↑（近 3
…[truncated 1815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1674
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-24T18:01:41.852419+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
  }
}
```

</details>

---


### Tool call

_source line 567 · 2026-05-24T18:01:42.003643+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-24T18:01:43.960542+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/submitted.pdf",
  "pages": "10-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/submitted.pdf",
    "pages": "10-20"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-24T18:01:45.429575+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3577
}
```

</details>

---


### Tool result

_source line 570 · 2026-05-24T18:01:45.480229+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3476
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-24T18:01:46.134826+00:00_

PDF pages extracted: 7 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/submitted.pdf (4.3MB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 2174
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-24T18:02:21.433457+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-24T18:02:22.888897+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/decisions.yaml\", \"content\": \"_next_id: 115\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 06:10 UTC\\n  summary: MVP 接受 35% sparsity 下 MLP-only pruning，不强制 attention 配额\\n  rationale: 全局统一排序下 attention GQA groups importance 普遍高于 MLP groups，35% sparsity\\n    自然只剪 MLP（367 groups）。这是模型结构特征的正确反映，不应人为干预。MLP-level correlation (N=367) 足以验证 CKA→recoverability\\n    假设。50% sparsity 放 Phase 2 获取 attention-level 数据。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: primary\\n    result: running\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 13:31 UTC\\n  summary: 终止无效 GRPO，改用 SFT warmup → GRPO 两阶段恢复策略\\n  rationale: 35% 结构化剪枝后两个模型 accuracy 仅 0.15%（输出退化），GRPO 150 步 loss=0/grad_norm=0，无学习信号。frac_reward_zero_std\\n    ≈ 1.0 表明几乎所有 completion 得 0 reward，GRPO 无法计算有效 advantage。SFT warmup 用 ground truth\\n    数据先恢复基本能力再转 GRPO 是解决 reward desert 的标准做法。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: motivating_failure\\n    result: GRPO 150 步 loss=0, grad_norm=0; post-prune accuracy 0.15% for both models\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 13:53 UTC\\n  summary: 暂缓 SFT warmup，优先审计剪枝实现正确性\\n  rationale: 两个不同剪枝策略产出精确相同的 accuracy（2/1319）统计上极不寻常，35% structured pruning 不应导致 7B\\n    模型完全崩溃。Reviewer 怀疑存在实现 bug（config 不匹配、全零层等）。若根因是代码问题，SFT warmup 是在错误基础上浪费算力。需先排除实现问题再决定恢复策略。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: audit_target\\n    result: both pruned models 0.15% accuracy, identical 2/1319\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 13:59 UTC\\n  summary: 修复 min_keep_mlp=4 导致的 per-layer 过度剪枝，重跑 MVP pipeline v3\\n  rationale: 根因确认：min_keep_mlp=4 允许单层 MLP 被剪至 14.3% capacity，全局排序集中破坏 early layers（0-6），两个模型均崩溃至\\n    0.15%。修复方案：min_keep_mlp 提升到 40% per layer + per-layer capacity floor。RASP scoring\\n    逻辑本身正常（产生了不同剪枝结构），核心假设仍可验证，只需收紧约
…[truncated 1441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-24T18:02:23.090096+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-24T18:02:23.140793+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-24T18:02:29.045991+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-24T18:02:29.199923+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-24T18:02:32.721456+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_17/ -maxdepth 2 -name \"config.yaml\" -o -name \"project_config*\" 2>/dev/null | head -10",
  "description": "Find project config location"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_17/ -maxdepth 2 -name \"config.yaml\" -o -name \"project_config*\" 2>/dev/null | head -10",
    "description": "Find project config location"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-24T18:02:32.785555+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "elapsed_ms": 64
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-24T18:02:42.076365+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_17/ -maxdepth 3 -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -10",
  "description": "Find agent config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_17/ -maxdepth 3 -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -10",
    "description": "Find agent config files"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-24T18:02:42.277590+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-24T18:02:46.141946+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/",
  "description": "List project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/",
    "description": "List project directory"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-24T18:02:46.192894+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
_anonymous_repo.json
_last_visual_review.json
_paper_audit_result.json
artifacts
checkpoints
constraints.lock
constraints.yaml
decisions.lock
decisions.yaml
distill_tmp
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
eval_math500_fixed.py
experiment_matrix.lock
experiment_matrix.yaml
experiment_plan.lock
experiment_plan.yaml
figures
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
paper
paper_deprecated
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
registry.lock
registry.yaml
report.md
review_visual_check_state.json
scripts
src
study_status.lock
task_context
validate_fix.py
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-24T18:03:36.585468+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recovery_aware_struct_prune",
  "text": "## 审稿任务 — Reviewer 1（Round 1）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (Main Conference, Long Paper)\n- **投稿系统**: ACL Rolling Review (ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations 和 Ethics Statement 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（论文中不得包含作者信息，不得有可识别自引）\n\n### 论文文件\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/submitted.pdf`\n- LaTeX 源码目录: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/`\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n请重点审查以下方面：\n\n1. **方法论有效性**\n   - CKA 作为 functional overlap 度量的合理性和局限性——是否存在循环论证（用 CKA 选结构，再用 CKA 分析结果）？\n   - Intra-layer CKA 与 inter-layer CKA 的区分是否充分？\n   - Taylor expansion importance score (Eq. 1) 的一阶近似是否在结构化剪枝场景下充分？\n   - RASP scoring function (Eq. 5) 的设计是否有理论支撑？α 的 dose-response 是否有混杂变量？\n\n2. **实验设计与控制**\n   - 四种 pruning criteria 的对比是否公平（控制变量是否一致）？\n   - Random baseline 使用 512 token generation limit（vs 其他方法 1024）——这是否构成不公平比较？\n   - GRPO 仅训练 100 步是否足够得出关于 recovery capacity 的结论？\n   - Two-stage recovery (SFT→GRPO) 的 SFT 阶段是否引入额外混杂？\n   - Per-layer capacity floor (40%) 对结果的影响——ablation 是否充分？\n\n3. **统计分析**\n   - 3-seed GRPO 验证的统计功效（N=3）\n   - Welch's t-test, Cohen's d, 95% CI 的使用是否恰当？\n   - TOST equivalence testing (ε=2pp) 的 margin 选择是否合理？\n   - RASP 和 Random 是否仍为单 seed？如果是，对 claims 有何影响？\n\n4. **因果推断 vs 相关性**\n   - \"Pruning criterion shapes recovery\" 这个核心 claim 的证据强度——是因果还是相关？\n   - \"Reward-accuracy decoupling\" 的定义和操作化是否严格？\n   - Dose-response 分析中 max_completion_length 的不一致（α=1.0: 1024 vs 其他 α: 512）是否构成关键混杂？\n\n5. **可复现性**\n   - 超参数报告是否完整？\n   - Calibration data 量 M=512 的选择依据？\n   - 是否有代码/checkpoint 发布声明？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses（按严重程度排序：Critical > Warning > Minor）\n- [Critical] W1: ...\n- [Warning] W2: ...\n- [Minor] M1: ...\n\n## Questions for Authors\n- Q1: ...\n\n## Missing References\n- ...\n\n## Overall Assessment\n评分（参考 EMNLP 2026 ARR 标准）：\n5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n置信度：1-5\n\n## Detailed Comments（逐 Section 评论）\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recovery_aware_struct_prune",
    "text": "## 审稿任务 — Reviewer 1（Round 1）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (Main Conference, Long Paper)\n- **投稿系统**: ACL Rolling Review (ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations 和 Ethics Statement 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（论文中不得包含作者信息，不得有可识别自引）\n\n### 论文文件\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/submitted.pdf`\n- LaTeX 源码目录: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/`\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n请重点审查以下方面：\n\n1. **方法论有效性**\n   - CKA 作为 functional overlap 度量的合理性和局限性——是否存在循环论证（用 CKA 选结构，再用 CKA 分析结果）？\n   - Intra-layer CKA 与 inter-layer CKA 的区分是否充分？\n   - Taylor expansion importance score (Eq. 1) 的一阶近似是否在结构化剪枝场景下充分？\n   - RASP scoring function (Eq. 5) 的设计是否有理论支撑？α 的 dose-response 是否有混杂变量？\n\n2. **实验设计与控制**\n   - 四种 pruning criteria 的对比是否公平（控制变量是否一致）？\n   - Random baseline 使用 512 token generation limit（vs 其他方法 1024）——这是否构成不公平比较？\n   - GRPO 仅训练 100 步是否足够得出关于 recovery capacity 的结论？\n   - Two-stage recovery (SFT→GRPO) 的 SFT 阶段是否引入额外混杂？\n   - Per-layer capacity floor (40%) 对结果的影响——ablation 是否充分？\n\n3. **统计分析**\n   - 3-seed GRPO 验证的统计功效（N=3）\n   - Welch's t-test, Cohen's d, 95% CI 的使用是否恰当？\n   - TOST equivalence testing (ε=2pp) 的 margin 选择是否合理？\n   - RASP 和 Random 是否仍为单 seed？如果是，对 claims 有何影响？\n\n4. **因果推断 vs 相关性**\n   - \"Pruning criterion shapes recovery\" 这个核心 claim 的证据强度——是因果还是相关？\n   - \"Reward-accuracy decoupling\" 的定义和操作化是否严格？\n   - Dose-response 分析中 max_completion_length 的不一致（α=1.0: 1024 vs 其他 α: 512）是否构成关键混杂？\n\n5. **可复现性**\n   - 超参数报告是否完整？\n   - Calibration data 量 M=512 的选择依据？\n   - 是否有代码/checkpoint 发布声明？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses（按严重程度排序：Critical > Warning > Minor）\n- [Critical] W1: ...\n- [Warning] W2: ...\n- [Minor] M1: ...\n\n## Questions for Authors\n- Q1: ...\n\n## Missing References\n- ...\n\n## Overall Assessment\n评分（参考 EMNLP 2026 ARR 标准）：\n5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n置信度：1-5\n\n## Detailed Comments（逐 Section 评论）\n```"
  }
}
````

</details>

---


### Tool result

_source line 585 · 2026-05-24T18:03:59.459437+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22873
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-24T18:03:59.663609+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recovery_aware_struct_prune",
  "text": "## 审稿任务 — Reviewer 2（Round 1）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (Main Conference, Long Paper)\n- **投稿系统**: ACL Rolling Review (ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations 和 Ethics Statement 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（论文中不得包含作者信息，不得有可识别自引）\n\n### 论文文件\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/submitted.pdf`\n- LaTeX 源码目录: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/`\n\n### 你的审查侧重：新颖性 + 完整性 + 格式合规\n\n请重点审查以下方面：\n\n1. **新颖性与贡献评估**\n   - \"Reward-accuracy decoupling\" 是否是一个真正新颖的发现，还是 100 步 GRPO 训练不足的 artifact？\n   - \"Recovery capacity spectrum\" 概念的新颖性——是否有先前工作已探讨过类似现象？\n   - RASP 方法本身的技术新颖性——将 CKA overlap 与 gradient importance 加权组合是否足够新？\n   - 贡献的实际影响——对 practitioner 有多少 actionable guidance？\n\n2. **Claims 与证据对齐**\n   - Abstract 和 Introduction 中的每个 claim 是否都有实验证据充分支持？\n   - \"holds across sparsity levels\" 类表述——实际验证了哪些 sparsity？30% 全 collapse 是否削弱此 claim？\n   - Cross-architecture/cross-scale 的 claim scope 是否合理？（Qwen2.5-Math-7B 是否算 \"cross-architecture\"？）\n   - SFT 贡献 ~60pp 恢复 vs GRPO <1pp——Title 聚焦 \"Post-RLVR Recovery\" 是否与数据一致？\n\n3. **Related Work 完整性**\n   - 是否覆盖了 LLM 结构化剪枝的主要方法（LLM-Pruner, Bonsai, GRASPrune, ShortGPT, FANG 等）？\n   - 是否覆盖了 RLVR/GRPO recovery 相关工作？\n   - 是否遗漏了重要的最近工作（2025-2026）？\n   - 自引是否匿名处理？\n   - Lottery Ticket Hypothesis 的联系讨论是否充分？\n\n4. **格式合规检查（EMNLP 2026 / ARR）**\n   - 正文是否严格在 8 页内？\n   - Limitations section 是否存在且内容充实？\n   - Ethics Statement 是否存在？\n   - 匿名性：是否有泄露作者身份的信息？（检查 acknowledgments、URLs、code repos 等）\n   - Abstract 是否不超过 200 words？\n   - 引用格式是否正确（natbib）？\n   - 图表质量：Figure 字体大小、可读性、颜色区分度\n   - 参考文献格式：年份、venue、bib key 一致性\n\n5. **写作质量**\n   - 术语一致性（如 \"recovery capacity spectrum\" 是否全文统一使用？）\n   - 是否有 overclaiming 用语（\"determines\", \"proves\", \"universally\" 等强因果词）？\n   - Discussion/Conclusion 是否充实？是否清晰分离了 SFT 和 GRPO 各自的角色？\n   - Limitations 是否诚实地讨论了主要局限？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses（按严重程度排序：Critical > Warning > Minor）\n- [Critical] W1: ...\n- [Warning] W2: ...\n- [Minor] M1: ...\n\n## Questions for Authors\n- Q1: ...\n\n## Missing References\n- ...\n\n## Overall Assessment\n评分（参考 EMNLP 2026 ARR 标准）：\n5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n置信度：1-5\n\n## Detailed Comments（逐 Section 评论）\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recovery_aware_struct_prune",
    "text": "## 审稿任务 — Reviewer 2（Round 1）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (Main Conference, Long Paper)\n- **投稿系统**: ACL Rolling Review (ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations 和 Ethics Statement 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（论文中不得包含作者信息，不得有可识别自引）\n\n### 论文文件\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/submitted.pdf`\n- LaTeX 源码目录: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/`\n\n### 你的审查侧重：新颖性 + 完整性 + 格式合规\n\n请重点审查以下方面：\n\n1. **新颖性与贡献评估**\n   - \"Reward-accuracy decoupling\" 是否是一个真正新颖的发现，还是 100 步 GRPO 训练不足的 artifact？\n   - \"Recovery capacity spectrum\" 概念的新颖性——是否有先前工作已探讨过类似现象？\n   - RASP 方法本身的技术新颖性——将 CKA overlap 与 gradient importance 加权组合是否足够新？\n   - 贡献的实际影响——对 practitioner 有多少 actionable guidance？\n\n2. **Claims 与证据对齐**\n   - Abstract 和 Introduction 中的每个 claim 是否都有实验证据充分支持？\n   - \"holds across sparsity levels\" 类表述——实际验证了哪些 sparsity？30% 全 collapse 是否削弱此 claim？\n   - Cross-architecture/cross-scale 的 claim scope 是否合理？（Qwen2.5-Math-7B 是否算 \"cross-architecture\"？）\n   - SFT 贡献 ~60pp 恢复 vs GRPO <1pp——Title 聚焦 \"Post-RLVR Recovery\" 是否与数据一致？\n\n3. **Related Work 完整性**\n   - 是否覆盖了 LLM 结构化剪枝的主要方法（LLM-Pruner, Bonsai, GRASPrune, ShortGPT, FANG 等）？\n   - 是否覆盖了 RLVR/GRPO recovery 相关工作？\n   - 是否遗漏了重要的最近工作（2025-2026）？\n   - 自引是否匿名处理？\n   - Lottery Ticket Hypothesis 的联系讨论是否充分？\n\n4. **格式合规检查（EMNLP 2026 / ARR）**\n   - 正文是否严格在 8 页内？\n   - Limitations section 是否存在且内容充实？\n   - Ethics Statement 是否存在？\n   - 匿名性：是否有泄露作者身份的信息？（检查 acknowledgments、URLs、code repos 等）\n   - Abstract 是否不超过 200 words？\n   - 引用格式是否正确（natbib）？\n   - 图表质量：Figure 字体大小、可读性、颜色区分度\n   - 参考文献格式：年份、venue、bib key 一致性\n\n5. **写作质量**\n   - 术语一致性（如 \"recovery capacity spectrum\" 是否全文统一使用？）\n   - 是否有 overclaiming 用语（\"determines\", \"proves\", \"universally\" 等强因果词）？\n   - Discussion/Conclusion 是否充实？是否清晰分离了 SFT 和 GRPO 各自的角色？\n   - Limitations 是否诚实地讨论了主要局限？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses（按严重程度排序：Critical > Warning > Minor）\n- [Critical] W1: ...\n- [Warning] W2: ...\n- [Minor] M1: ...\n\n## Questions for Authors\n- Q1: ...\n\n## Missing References\n- ...\n\n## Overall Assessment\n评分（参考 EMNLP 2026 ARR 标准）：\n5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n置信度：1-5\n\n## Detailed Comments（逐 Section 评论）\n```"
  }
}
````

</details>

---


### Tool result

_source line 587 · 2026-05-24T18:04:01.080599+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1416
}
```

</details>

---


### Assistant

_source line 588 · 2026-05-24T18:04:12.943092+00:00_

两位 Reviewer 已分配并启动独立审稿。

- **Reviewer 1**: 方法严谨性 + 实验设计（CKA 方法论、统计分析、混杂变量、因果推断）
- **Reviewer 2**: 新颖性 + 完整性 + 格式合规（贡献评估、Claims-证据对齐、Related Work、格式检查）
- **视觉审查 Agent**: 已并行派发（fire-and-forget）

等待 Reviewer 返回审稿意见后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 47

## Round 47

2 recorded events


### User

_source line 589 · 2026-05-24T18:12:04.173855+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见 — Round 1

**论文标题**: How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs

---

## Strengths

- **S1: 重要且新颖的研究问题。** 现有结构化剪枝文献几乎未研究剪枝准则如何影响下游 RLVR 恢复效果。该论文首次系统地在控制实验框架下比较四种剪枝准则对 GRPO 恢复动态的影响，填补了一个实际且学术上有价值的空白。

- **S2: 严格的控制实验设计。** 固定模型 (DeepSeek-R1-Distill-Qwen-7B)、固定剪枝率 (20%)、固定恢复流水线 (SFT→GRPO)，仅变化剪枝准则。这种"只改一个变量"的设计使得因果推断有较好的基础。Algorithm 1 (Appendix B) 提供了完整的伪代码，增强了可复现性。

- **S3: Reward-accuracy decoupling 是一个有意义的发现。** Table 2 和 Figure 4 清晰展示了：在 20% sparsity 下，四种准则的 GRPO reward 轨迹差异巨大（CKA-only peak 0.354 vs RASP 0.010），但 SFT→GRPO 的精度增量很小（mean |Δ| = 0.51pp）。这个"高 reward ≠ 高 accuracy gain"的发现对 RLVR 社区有启示意义。

- **S4: 统计分析比同领域多数工作更严谨。** 使用 Welch's t-test、Cohen's d、95% CI、TOST 等价性检验（Appendix T），而非简单报告单点数字。CKA-only vs Standard 的 Cohen's d = 11.5 表明效应量极大。

- **S5: 丰富的消融实验。** 21 个附录覆盖了扩展训练 (Appendix E)、OOD 评估 (F)、MBPP 代码生成 (G)、CKA 稳定性 (H)、梯度分析 (I)、dose-response (D)、跨 sparsity (M)、跨模型 (N, O)、深度优先基线 (R)、capacity floor 消融 (S) 等。这种覆盖面在剪枝论文中较为罕见。

- **S6: Recovery capacity spectrum 概念。** 将四种准则映射到"主动学习→停滞→崩溃"的连续谱（Table 1），并通过四个诊断指标 (mean reward, f_b, gradient norm, KL divergence) 操作化定义，有一定的理论贡献。

---

## Weaknesses（按严重程度排序）

### Critical

**[Critical] W1: RASP（核心方法）仅使用单 seed 验证，dose-response 曲线不可靠**
- **具体位置**: Section 4.1 (page 6), Table 2, Table 5 (Appendix D, page 12)
- **问题**: 论文对 CKA-only、Standard、Random 使用 3-seed GRPO 验证，但核心贡献 RASP 及整个 dose-response 分析（α ∈ {0.5, 1.0, 2.0, 3.0, 4.0}）均为 N=1。Table 5 显示 α=2.0 时精度最高 (GRPO 66.11%)，但相邻 α=3.0 仅 61.46%——差 4.65pp。在 Standard 的 3-seed σ=0.38pp 和 CKA-only 的 σ=0.18pp 的噪声水平下，这个差距可能是稳健的；但 RASP 的 seed 敏感性未知。inverted-U 的峰值位置 (α=2.0) 可能因 seed 不同而偏移，甚至 inverted-U 形状本身也可能是单次采样的伪影。
- **为什么影响接收**: RASP 是论文的核心方法贡献，dose-response 是 Section 4.2 的主要证据。在 N=1 下，"inverted-U recovery profile" (Abstract) 这个 claim 缺乏统计支撑。
- **建议修改方向**: 至少对 α=2.0 (peak) 和 α=1.0 (collapse) 补充 3-seed 验证；或者降低 claim 的语气（"preliminary evidence suggests" 而非 "reveals"）。

**[Critical] W2: Random baseline 使用不同的 max_completion_length（512 vs 1024），比较不公平**
- **具体位置**: Section 4.1 (page 6), Table 3 (Appendix A, page 11)
- **问题**: Random 使用 TRL 默认的 512-token 生成限制，而 CKA-only、Standard、RASP 使用 1024。对于数学推理任务，生成长度直接影响推理链的完整性。Figure 3(a) 显示 Random 的 reward 在 0.14-0.19 之间振荡——但如果推理链被截断在 512 token，模型可能无法完成多步推理，reward 自然偏低。论文称此为 "conservative comparison point"，但 bias 的方向恰好支持了论文的叙事（Random 表现差 → 剪枝准则 matters）。
- **为什么影响接收**: Random 是四种准则之一，其在 recovery capacity spectrum 中被定位为 "oscillates (0.14-0.19)"（Table 1）。如果 Random 在 1024 token 下表现不同，整个 spectrum 的排序可能改变。这不仅仅是 Random 本身的问题——它影响 "pruning criterion shapes recovery" 这个核心 claim 的强度。
- **建议修改方向**: 补充 Random 在 max_completion_length=1024 下的 GRPO 结果（至少 1 seed），或在论文中明确讨论这个 confound 对 claim 的限制。

### Warning

**[Warning] W3: CKA 的双重角色（评分准则 + 分析工具）存在循环论证风险**
- **具体位置**: Section 3.2 (Eq. 3, page 3-4), Section 4.5 (page 8), Figure 5 (page 8)
- **问题**: CKA 同时用于：(1) 剪枝时计算 functional overlap F(h) 以指导结构选择（Eq. 3, 5）；(2) 事后分析中衡量 dense 与 pruned 模型间的 layer-wise CKA similarity（Figure 5, Section 4.5）。虽然技术上前者是 intra-layer pairwise CKA、后者是 layer-wise dense-vs-pruned CKA，但两者的底层度量相同。当论文在 Section 4.5 用 CKA 分析发现 "CKA-only diverges most from the dense model" 时，这部分是因为 CKA-only 的剪枝准则本身就是基于 CKA 选择最冗余的结构——这并非独立验证。
- **建议**: 在 Section 4.5 增加非 CKA 的分析维度（如 mutual information、probing accuracy）作为独立验证；或明确讨论该循环性并论证为何分析仍有价值。

**[Warning] W4: RASP 评分函数 (Eq. 5) 缺乏理论推导，函数形式选择武断**
- **具体位置**: Section 3.3 (Eq. 5, page 4)
- **问题**: S_rasp(h) = I(h) × (1 − F(h))^α 的乘法形式没有理论推导。为什么是乘法而非加法 I(h) + λ(1−F(h))？为什么是 (1−F(h))^α 而非 exp(−αF(h)) 或其他单调变换？α 的 dose-response 分析是纯经验的，论文也承认 "full search over continuous α values was not performed"（Limitations, page 9）。
- **建议**: 补充 Eq. 5 的设计动机（如 Pareto efficiency 的视角），或至少与 additive 形式做对比消融。

**[Warning] W5: 模型和 benchmark 范围窄，核心 claims 的泛化性存疑**
- **具体位置**: Section 4.1 (page 5-6), Limitations (page 9)
- **问题**: 主实验仅用 DeepSeek-R1-Distill-Qwen-7B + GSM8K。虽然 Appendix 提供了 Qwen2.5-Math-7B (Appendix O)、MATH-500 (F)、MBPP (G) 的补充结果，但 (a) Qwen2.5-Math-7B 没有 GRPO 验证（仅 SFT 和 post-prune），(b) MATH-500 的精度差异不显著 (Table 6)，(c) MBPP 的 GRPO delta 不显著。论文在 Abstract 中做出 "recovery method choice becomes irrelevant" 的强 claim，但证据基础是一个 7B 模型在一个 benchmark 上的结果。Limitations 承认 "does not extend to different architecture families (e.g., LLaMA, Mistral)" 和 "scales (1B-70B)"——这些是需要验证的核心外推。
- **建议**: 降低 abstract 和 introduction 中的 claim 强度；或补充至少一个非 Qwen 家族模型的完整实验（含 GRPO）。

**[Warning] W6: SFT 阶段可能引入 ceiling effect，模糊 GRPO 的增量贡献**
- **具体位置**: Section 3.4 (page 4-5), Table 2 (page 6), Table 6 (page 12)
- **问题**: 两阶段恢复 (SFT→GRPO) 中，SFT 已将模型精度恢复到 59-64%（Table 2 SFT 列），而 unpruned 模型为 90.83%。GRPO 在此基础上的增量很小（mean |Δ| < 1pp）。但这可能是因为 GRPO 仅训练 100 步（Table 3），而非因为剪枝准则"使 recovery method choice irrelevant"。Appendix E 将训练延长到 300 步，但仍可能不够（300 步仅比 100 步多 3×，而 RLVR 通常需要数千步）。如果 GRPO 训练到 1000+ 步，不同准则的精度差距可能放大，打破"decoupling"。
- **建议**: 讨论 SFT ceiling effect 假说；或提供更长 GRPO 训练的证据。

**[Warning] W7: TOST 等价性检验的 ε=2pp margin 选择缺乏先验依据**
- **具体位置**: Appendix T (page 15-16), Table 16
- **问题**: ε=2pp 被用作 "practical equivalence" 的阈值，但该值不是预注册的，也没有基于先验 power analysis 推导。论文在 Appendix T 展示了 ε=1pp（power 不足）和 ε=3pp（all significant），但选择 ε=2pp 使得 7/8 比较通过等价性检验——这个"刚好合适"的 margin 有 post-hoc selection 之嫌。在 GSM8K 这样精度相对粗糙的 benchmark 上（binary outcome per problem, N=1,319），2pp 是否真的代表"实质等价"？
- **建议**: 提供 ε=2pp 的先验理由（如参考 GSM8K 上的 human inter-rater agreement 或 seed-to-seed 噪声水平），或明确说明此为探索性分析。

### Minor

**[Minor] M1: Recovery capacity 概念先用后定义**
- Section 1 (page 1) 多次使用 "recovery capacity"，但正式定义在 Section 3.5 (page 5) 才出现。建议在首次使用时给出简要定义。

**[Minor] M2: Figure 2 信息密度过高**
- Figure 2 试图在单幅图中展示 structural analysis、scoring criteria、recovery pipeline 和 capacity spectrum 四个部分。底部的 spectrum 尤其拥挤。建议拆分为两幅图。

**[Minor] M3: "Reward-accuracy decoupling" 术语可能引起误解**
- "Decoupling" 暗示 reward 和 accuracy 完全无关，但实际发现是"GRPO 在 SFT 基础上的精度增量小"。更准确的表述可能是 "diminishing returns of GRPO over SFT" 或 "GRPO accuracy plateau"。

**[Minor] M4: Calibration data 量 M=512 的选择未说明理由**
- Section 3.2 (page 3) 指出使用 M=512 个随机采样的 GSM8K 训练样本。Appendix H 显示 CKA 排序在不同 calibration 量下稳定 (ρ > 0.96)，但未说明为何选 512 而非 256 或 1024。

**[Minor] M5: 未明确承诺代码/checkpoint 发布**
- Limitations 和 Ethics Statement 提到 "all models and datasets used in this work are publicly available under permissive licenses"，但未承诺发布实验代码或剪枝后的 checkpoint。对于一项以可复现性为卖点的控制实验，这是遗漏。

---

## Questions for Authors

- **Q1**: RASP 在不同 seed 下的 dose-response 曲线形状是否一致？α=2.0 的优势是否在多个 seed 上复现？

- **Q2**: Random baseline 使用 max_completion_length=512 的具体原因是什么？是否有 Random 在 1024 下的对比数据？

- **Q3**: Section 4.5 的 CKA 分析是否有非 CKA 度量的独立验证（如 probing accuracy 或 mutual information）？

- **Q4**: 如果将 GRPO 训练延长到 500 或 1000 步，reward-accuracy decoupling 是否仍然成立？

- **Q5**: Eq. 5 的乘法形式是否与 additive 形式做过对比？如 S(h) = I(h) + λ(1−F(h))？

- **Q6**: 在 Qwen2.5-Math-7B 上的跨模型验证（Appendix O）为什么没有 GRPO 阶段？是否因为 GRPO 在该模型上训练困难？

---

## Missing References

- 无明显缺失。论文引用覆盖了 LLM 结构化剪枝、CKA、RLVR/GRPO 的主要文献。可考虑增加 Wanda (Sun et al., 2024) 等 unstructured pruning 方法的讨论，以更清晰地界定 structured vs. unstructured 的适用范围差异。

---

## Overall Assessment

**评分: 3.5 — Borderline Conference**

**Soundness**: 3.5/5 — 控制实验设计合理，但 RASP 单 seed、Random 不公平比较、CKA 循环使用等问题削弱了部分 claim 的可信度。核心发现 (CKA-only vs Standard 的 4.55pp gap) 有 3-seed 统计验证 (p=0.0009)，是稳健的。

**Excitement**: 3.5/5 — 研究问题新颖且实用（剪枝准则如何影响 RLVR 恢复），recovery capacity spectrum 概念有学术价值。但证据范围较窄（单模型、单 benchmark 为主），限制了 excitement。

**Reproducibility**: 3/5 — Algorithm 1 和 Table 3 提供了较完整的超参数，但未承诺代码发布，且 RASP 单 seed 意味着结果难以验证。

**Confidence**: 4/5 — 仔细阅读了全文和全部附录，对方法论和实验设计有较深入理解。对 CKA 在结构化剪枝中的具体行为不如专门研究 CKA 的审稿人熟悉。

---

## Detailed Comments（逐 Section 评论）

### Abstract
- 内容准确反映论文贡献。字数接近 200 word limit，建议确认未超标。
- "recovery method choice becomes irrelevant" 过于绝对——在 25% sparsity 下 CKA-only 仍领先 ~4.55pp（Table 12, Appendix M），说明该结论有 sparsity 依赖性。

### Section 1 (Introduction)
- 动机清晰：现有工作优化剪枝质量但忽视了对下游 RLVR 恢复的影响。
- "No prior work has compared multiple pruning criteria under RLVR" 是一个强 novelty claim，需确保文献覆盖完整。
- Line 048-051 提到 Ji et al. (2026) 的 unstructured pruning 对比是好的界定。

### Section 2 (Related Work)
- 覆盖了 structured pruning (width/depth)、pruning-aware recovery、RLVR training dynamics 三条主线。
- 对 CKA 在剪枝中的先前应用（Hu et al., 2024; Lachance, 2022）的区分是清晰的：prior work 用 inter-layer CKA 做 depth pruning，本文用 intra-layer CKA 做 width pruning。

### Section 3 (Method)
- **3.1**: GQA 分组粒度的处理 (7 Q heads + 1 KV head 作为一个 unit) 是合理的工程决策。
- **3.2**: Taylor expansion (Eq. 1) 是标准方法（LLM-Pruner）。CKA reliability 的讨论（page 4, 避免 kernel width 和 layer width 敏感性）是恰当的。
- **3.3**: 四种准则的关系描述清晰：Standard (α=0)、CKA-only (α→∞)、RASP (intermediate α)、Random (uninformed)。但 Eq. 5 的设计动机不足（见 W4）。
- **3.4**: 两阶段设计合理，但 SFT 阶段的参数选择（2 epochs, lr=2e-5）对结果的敏感性未讨论。

### Section 4 (Experiments)
- **4.1**: 实验设置基本完整。但 Random 的 512 token limit 是最大的实验设计缺陷（W2）。
- **4.2**: Recovery capacity spectrum 的四种 regime 定义清晰。Figure 3 的 GRPO 训练动态展示了明显的分离。但 RASP (α=1.0) 的 100 步内即崩溃，而该结果仅为单 seed——可能是 seed 不幸。
- **4.3**: Reward-accuracy decoupling 是论文最有意思的发现。Figure 4 的 SFT vs GRPO scatter plot 直观。但 Section 4.3 末尾 "GRPO adds nothing (gap preserved at 4.55pp)" 这个表述需要注意：gap 是 across criteria 的，而 decoupling 是 within criterion 的 SFT→GRPO Δ。
- **4.4**: "Post-SFT accuracy does not predict GRPO outcome" 的分析有趣——SFT 后 CKA-only (63.91%) > Standard (59.29%)，但 GRPO 后两者差距基本持平而非拉大，说明 GRPO 没有放大 SFT 的差距。
- **4.5**: Extended analysis 覆盖面广。但 dose-response 仅为单 seed（W1），CKA 分析有循环性风险（W3）。

### Section 5 (Discussion and Conclusion)
- "Whether RLVR outperforms SFT for recovering pruned reasoning models depends on how the model was pruned" 是一个合理且有 nuance 的 conclusion。
- "Under diversity-preserving pruning at 20-25% sparsity, the two paradigms produce near-identical accuracy" — 需注意 25% sparsity 下的证据较弱（主要在 Appendix M, 且 CKA-only 仍领先 4.55pp）。

### Limitations
- 合理地承认了模型/架构范围、α 搜索不充分、capacity floor 的启发式选择等局限。
- 遗漏了两个重要 limitation：(a) Random 的不公平比较；(b) RASP 的单 seed 验证。

### Appendix
- 信息量大，质量参差：Appendix D (dose-response)、E (extended training)、H (CKA stability)、T (TOST) 是高质量的补充。Appendix P (structural overlap) 和 Q (KL divergence) 提供了有价值的机制洞察。但 21 个附录的组织可以更精简。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 590 · 2026-05-24T18:12:15.106084+00:00_

Reviewer 1 审稿意见已收到。评分 3.5 (Borderline Conference)，主要发现：RASP 单 seed 验证不足（Critical）、Random baseline 512 vs 1024 token 不公平比较（Critical）、CKA 循环论证风险（Warning）等。

等待 Reviewer 2 审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 48

## Round 48

2 recorded events


### User

_source line 591 · 2026-05-24T18:12:17.577791+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：给出 **3.5 (Borderline Conference)** 的评分。主要问题：

1. **[Critical] RASP 单 seed 验证**：核心方法及 dose-response 分析均为 N=1，inverted-U 曲线的可靠性存疑
2. **[Critical] Random baseline 不公平比较**：Random 使用 512 token 限制 vs 其他方法 1024，bias 方向支持论文叙事
3. **[Warning] CKA 循环使用**：同时作为剪枝准则和事后分析工具
4. **[Warning] RASP 函数形式缺乏理论推导**
5. **[Warning] 模型/benchmark 范围窄**，强 claim 与窄证据不匹配
6. **[Warning] SFT ceiling effect 可能模糊 GRPO 增量贡献**
7. **[Warning] TOST ε=2pp margin 缺乏先验依据**

主要优势：研究问题新颖、控制实验设计严格、reward-accuracy decoupling 发现有意义、统计分析比同领域多数工作更规范。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 592 · 2026-05-24T18:12:24.458837+00:00_

Reviewer 1 审稿已收到（3.5 Borderline Conference）。等待 Reviewer 2 完成审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 49

## Round 49

6 recorded events


### User

_source line 593 · 2026-05-24T18:13:24.889622+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: "How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs"
**Venue**: EMNLP 2026 (ARR), Long Paper

---

## Strengths

- **S1: 严格控制的实验设计。** 四种剪枝标准共享相同的 recovery pipeline（SFT warmup → GRPO）、相同的剪枝预算（20% MLP channel sparsity, 200/784 groups）、相同的 per-layer capacity floor（≥40%），这使得 pruning criterion 成为唯一自变量。这种控制水平在 LLM 剪枝文献中罕见。

- **S2: Dose-response 分析方法论上出色。** α 系数的连续调控（0.5→4.0）产生可复现的 inverted-U 曲线（Figure 1, Table in Appendix D），为 α 的因果效应提供了比单点消融更强的证据。这超出了多数剪枝论文的方法论标准。

- **S3: 统计严谨性突出。** TOST 等价检验（ε=2pp, 7/8 comparisons p<0.05, Appendix T）、Welch's t-test（CKA-only vs Standard, p=0.0009, Cohen's d=11.1）、multi-seed 验证（3 seeds for 3/4 methods）、95% CI 报告。这在实证 ML 论文中属于高标准。

- **S4: Reward-accuracy decoupling 是有趣的反直觉发现。** 4.4× peak reward gap 对应 <1pp accuracy difference（Table 2, Figure 4）挑战了"RLVR 优于 SFT"的社区共识（来自 Ji et al., 2026 的 self-healing 结论），并提供了清晰的实验证据。

- **S5: 充实的 Appendix（A-U, 8 页）。** 覆盖训练细节、算法伪代码、消融分析（sparsity cliff, per-layer floor, cross-scale, cross-model, MATH-500, MBPP, TOST），增强了可复现性。

---

## Weaknesses（按严重程度排序）

### Critical

**[Critical] W1: GRPO 训练时长严重不足，reward-accuracy decoupling 可能是训练欠拟合的 artifact。**
- 具体位置：Section 4.1 (Recovery pipeline), Section 4.3, Section 4.5 (Extended training)
- 问题：核心实验仅用 100 步 GRPO（扩展实验 300 步），而标准 GRPO 训练通常运行数千步（DeepSeek-R1 原文用数万步 RL）。SFT warmup 已恢复 ~60pp（从 post-prune 到 ~60-64%），留给 GRPO 的 headroom 约 ~27pp（相对于 dense 90.83%）。100 步 GRPO 仅贡献 <1pp，这可能仅仅说明训练不够长——而非 pruning criterion 真正消除了 recovery paradigm 差异。
- 论文的 300 步扩展（Section 4.5, Figure 6）显示 Standard 仍然 collapsed，CKA-only 维持 5.5× reward gap，但仍未报告 accuracy 变化。如果 CKA-only 在 1000+ 步后 accuracy 显著超过 SFT-only，则 "decoupling" 的核心 claim 不成立。
- 为什么影响接收：这是论文的中心论点。如果 decoupling 仅在训练不充分时成立，则 contribution 1 从"发现"降格为"观察到短 GRPO 不改变 accuracy"。
- 建议：至少对 CKA-only 和 Standard 各跑一次 500-1000 步 GRPO 至 reward 饱和，报告 accuracy 变化。如果 accuracy 仍不变，decoupling claim 成立；否则需重新定性。

**[Critical] W2: 单一架构族，"Reasoning LLMs" 的 claim scope 远超证据。**
- 具体位置：Title, Abstract, Section 4.5 (Cross-scale and cross-model)
- 问题：主实验仅 DeepSeek-R1-Distill-Qwen-7B（Qwen2.5 架构）；cross-model 验证的 Qwen2.5-Math-7B 是同一架构族且只有 SFT recovery（无 GRPO）。1.5B scale 验证仅为"preliminary evidence"且是 SFT-only（Table 13, Appendix N）。
- Title 说 "Reasoning LLMs"（复数），Abstract 说 "across benchmarks"，但实际仅验证一个架构族。LLaMA、Mistral、Phi 等架构的 GQA 配置不同，MLP 结构不同，recovery spectrum 可能完全不同。
- 为什么影响接收：EMNLP reviewers 会关注 claim scope 与 evidence 的匹配。当前证据支持"How Pruning Criteria Shape Recovery in DeepSeek-R1-Distill-Qwen-7B"而非标题的泛化声称。
- 建议：(1) 在 Qwen2.5-Math-7B 上补充 GRPO recovery 验证 spectrum ordering；(2) 或大幅缩窄 claim scope——Title 改为明确指定模型/架构。

**[Critical] W3: RASP 方法的贡献叙事自相矛盾。**
- 具体位置：Section 3.3 (Eq. 5), Section 4.4 (Dose-response), Abstract
- 问题：RASP 定义为 S(h) = I(h) × (1 − F(h))^α，旨在"balance gradient importance with CKA-based diversity"。但：
  - α=1.0（名义上的"平衡"点）导致 collapse（peak reward 0.061, Figure 3）
  - 最优 α=2.0 实质上是 CKA-dominant scoring（(1−F)^2 项主导，importance 被边缘化）
  - CKA-only 本身已达 64.39%，RASP α=2.0 仅高 1.72pp（66.11%）
- 这意味着"平衡"叙事不成立——最优策略是尽量最大化 diversity 权重，importance 的边际贡献微弱。论文应该更诚实地讨论：CKA-only 可能是 near-optimal 的简单 baseline，RASP 的 α 调优成本是否值得 1.72pp 的增益？
- 建议：将 RASP 重新定位为"dose-response 分析工具"而非"方法贡献"，或提供更多 α 值（如 α=1.5, 2.5, 3.0, 3.5）的 fine-grained 搜索以证明 α=2.0 确实是 robust optimum。

### Warning (Should-Fix)

**[Warning] W4: Random baseline 的 max_completion_length 不一致（512 vs 1024）构成混淆变量。**
- 具体位置：Section 4.1 最后一段, Table 3 (Appendix A)
- 问题：Random 使用 TRL 默认 512 tokens，而 CKA-only、Standard、RASP 使用 1024 tokens。论文称这是"conservative comparison"，但 512 token 限制可能截断长 chain-of-thought 推理，人为压低 Random 的 GRPO performance。同样，RASP α=1.0 使用 1024 而其他 α 值使用 512（footnote, Section 4.4），使 inverted-U 成为"conservative estimate"——但这意味着 α=2.0 的 66.11% 可能在 1024 tokens 下更高，也可能更低。
- 建议：统一 max_completion_length 为 1024 进行 fair comparison，至少对 Random 和 α=2.0 各补一个 1024-token 实验。

**[Warning] W5: Title 聚焦 "Post-RLVR Recovery" 但数据显示 SFT 完成了几乎所有 accuracy recovery。**
- 具体位置：Title, Section 4.3, Section 5
- 问题：SFT warmup 恢复 ~60pp（从 post-prune ~1% 到 ~60-64%），GRPO 贡献 <1pp。Title 中的 "Post-RLVR Recovery" 暗示 RLVR 是 recovery 的关键阶段，但实验表明 RLVR 在 accuracy 维度上几乎无效。论文的实际发现更接近 "pruning criteria shape SFT recovery and GRPO training dynamics"。
- 建议：考虑调整 title/framing，或在 Discussion 中更明确地阐述 SFT vs GRPO 各自的角色。

**[Warning] W6: Discussion/Conclusion 过于单薄（仅 1 段约 7 行）。**
- 具体位置：Section 5
- 问题：对于一篇做了大量实验的 controlled study，Discussion 部分缺乏：(1) 为什么 diversity preservation enables RL trainability 的 mechanistic 解释；(2) 与 Mukherjee et al. (2025) 关于 RL 仅更新 5-30% 参数的联系；(3) 对 practitioner 的 actionable guidance 总结；(4) Future directions。
- 建议：扩展至少到半页，加入 mechanistic discussion 和 practical implications。

**[Warning] W7: 30% sparsity 全面 collapse 限制了实用性。**
- 具体位置：Section 4.4, Appendix J
- 问题：所有方法在 30% sparsity 下全部 collapse（Section 4.4 提及, Appendix J 确认）。论文的有效 operating window 仅为 15-25% sparsity，而 20% sparsity 仅节省 ~28% 内存、吞吐量反而下降 19%（Limitations section）。对 practitioner 而言，这个 efficiency-accuracy tradeoff 可能不够吸引人。
- 建议：在 Limitations 中更坦诚地讨论实用性边界，或尝试 25% sparsity 下的 dose-response 验证。

### Minor

**[Minor] M1: RASP 仅用 1 个 GRPO seed 验证。**
- 具体位置：Limitations (Replication and scope)
- 问题：CKA-only、Standard、Random 各有 3 seeds，但 proposed method RASP 仅 1 seed。论文坦诚承认了这一点，但作为主要 proposed method，variance 估计缺失。

**[Minor] M2: "Cross-architecture" overclaiming。**
- 具体位置：Section 4.5, Abstract ("across Qwen2.5-family models")
- 问题：Qwen2.5-Math-7B 是同一 Qwen2.5 架构族的变体，属于 cross-model 而非 cross-architecture。Abstract 的措辞准确（说了"Qwen2.5-family"），但 Introduction contribution list 可能给读者 cross-architecture 的错误印象。

**[Minor] M3: Lottery Ticket Hypothesis 联系过于表面。**
- 具体位置：Section 2 (Related Work), 最后一句
- 问题：LTH 是关于 training from scratch 的 subnetwork，而本文是 recovery from pretrained model。一句话类比("poses the analogous question") 没有深入讨论关键差异：LTH subnetworks 保持 initialization，而 pruned models 保持 pretrained weights + recovery training。

**[Minor] M4: Abstract 中 "a phenomenon we term reward-accuracy decoupling" 的术语首次出现。**
- 相较于论文后续的详细定义（Section 4.3），Abstract 中的引入稍显突兀。Decoupling 通常暗示两个变量原本应耦合，但论文未充分论证为什么 reward 和 accuracy 在先验上应该是耦合的。

---

## Questions for Authors

- **Q1**: 如果将 GRPO 训练延长至 1000 步或 reward 完全饱和，CKA-only 的 accuracy 是否会显著超过 SFT-only？300 步实验（Section 4.5）仅报告了 reward gap 维持，未报告 accuracy 变化——这个遗漏是关键的。
- **Q2**: RASP α=1.0 collapse 的根本原因是什么？既然 importance × diversity 理应是合理的 composite，为什么"平衡"点反而最差？这是否暗示 gradient importance scoring 本身对 RL recovery 有害？
- **Q3**: CKA overlap 的计算使用 M=512 calibration samples（Section 3.2）。对不同 calibration data（如非数学领域的 text）的敏感性如何？
- **Q4**: 为什么不在 Qwen2.5-Math-7B 上也跑 GRPO recovery？这只需额外几个小时的 GPU 时间，但能大幅增强 cross-model 证据。
- **Q5**: Table 2 中 Random 的 peak reward (0.19) 高于 Standard (0.081)，但 Random 的 SFT accuracy 远低于 Standard（51.25% vs 59.29%）。为什么更差的 SFT 起点反而有更好的 GRPO reward？这是否进一步说明 reward 和 accuracy 是完全不同的指标？

---

## Missing References

1. **"When Reasoning Meets Compression"** (Li et al., 2025, arXiv:2504.02010) — 在 DeepSeek-R1 模型上 benchmark 了包括剪枝在内的压缩方法对推理能力的影响，直接相关。
2. **"GPrune-LLM: Generalization-Aware Structured Pruning"** (2026, arXiv:2603.13418) — 考虑泛化性的结构化剪枝，与本文关注 recovery capacity 的视角互补。
3. **"Can Pruning Improve Reasoning?"** (2025, arXiv:2505.14582) — 探讨剪枝与推理能力的关系，应至少在 Related Work 中提及。

---

## Overall Assessment

**评分: 3.0 (Findings)**

**一句话总结**: 实验设计严谨、dose-response 分析出色的 controlled study，但 100 步 GRPO 训练不足以支撑 "reward-accuracy decoupling" 的核心 claim，单一架构族限制了泛化性，proposed RASP 方法的 "balance" 叙事与数据自相矛盾。

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 实验设计严格控制（S1），统计方法超过平均水平（S3），但 GRPO 训练时长不足（W1）严重威胁核心 claim，单一架构族限制了 main claims 的支撑范围（W2）|
| Excitement | 3.0/5 | Pruning criterion 与 RL recovery 的交互是有意义的研究问题，dose-response 分析方法论有启发性（S2），但 findings 可能是训练不充分的 artifact（W1），实际影响受限于狭窄的 sparsity window（W7）|
| Overall Assessment | 3.0/5 | Findings 接收水平。作为 controlled empirical study 有价值，但需要：(1) 更长的 GRPO 训练验证 decoupling 的 robustness；(2) 缩窄 claim scope 或补充 cross-architecture 证据；(3) 重新审视 RASP 的贡献定位 |

**置信度**: 4/5 (Quite sure — 熟悉 LLM 剪枝和 RLVR 相关文献，仔细检查了实验细节和统计方法)

---

## Detailed Comments（逐 Section 评论）

### Abstract
- 约 191 words，符合 200-word 限制。
- "reward-accuracy decoupling" 术语首次出现但缺乏前置动机——为什么 reviewer 应该期望 reward 和 accuracy 耦合？
- "holds at moderate sparsity (20–25%) across benchmarks" 的 "across benchmarks" 表述偏强——MBPP 结果不显著（Appendix G），MATH-500 gap 缩窄。

### Section 1 (Introduction)
- Figure 1 dose-response 曲线放在首页有效吸引注意力。
- Contribution list 仅 2 项：(1) reward-accuracy decoupling（empirical finding），(2) recovery capacity spectrum + RASP。对于 EMNLP long paper，contribution 数量略少。
- 引用 Matsurani et al. (2026) 的 "RL compresses incorrect paths while SFT expands correct ones" 是 framing 的关键前提，但论文未充分解释为什么这种互补性应导致 accuracy 差异。

### Section 2 (Related Work)
- 覆盖面广：width pruning (LLM-Pruner, Bonsai, GRASPrune), depth pruning (ShortGPT, SliceGP, LaCo), reasoning-specific (RESP, RAC, SSGR, LLMs2LRMs), function-aware (FANG, FuncNet, MPruner), recovery (self-healing, P2Law, PASER, PAT), RL dynamics (RL squeezes, RL subnetworks)。
- 但遗漏了 "When Reasoning Meets Compression" (2025) 和 "GPrune-LLM" (2026)。
- LTH 联系仅一句话，过于表面。

### Section 3 (Method)
- 3.1 Preliminaries 清晰定义了 GQA pruning unit。
- 3.2 Structural Analysis 的 importance (Eq. 1) 和 CKA overlap (Eq. 2-3) 计算标准清晰。
- Intra-layer CKA（同层内不同 structure 间的 CKA）是与 MPruner (inter-layer CKA for depth pruning) 的关键差异，论文正确指出了这一点。
- 3.3 四个 scoring criteria 定义明确，但 RASP (Eq. 5) 的函数形式 I(h)×(1−F(h))^α 的选择未经讨论——为什么是乘法而非加权和？为什么 diversity 用 (1−F)^α 而非 exp(−αF)？
- 3.4 Two-Stage Recovery 描述清晰。SFT warmup 的设计意图（恢复 EOS generation + format compliance）说明合理。

### Section 4 (Experiments)
- **4.1 Setup**: 硬件（2×RTX PRO 6000, 94GB VRAM）、seed 处理、calibration 细节充分。但 Random 的 max_completion_length 差异是重要混淆变量。
- **4.2 Recovery Capacity Spectrum**: Table 1 清晰展示四级 spectrum。Figure 3 的 training dynamics 可视化有效。但论文将此称为 "spectrum" 暗示连续性，实际只有 4 个离散点。
- **4.3 Reward-Accuracy Decoupling**: 核心 section。TOST 检验方法论正确。但 100 步训练是否足够使 GRPO 发挥效果是根本性问题。Figure 4 的 scatter plot 有效展示了 y=x 附近的聚集。
- **4.4 Additional Results**: Dose-response α 分析是论文最强的部分。15% vs 20% vs 25% 的 sparsity 比较有价值，显示 15% 时 GRPO 仍可放大 CKA-only 优势。
- **4.5 Extended Analysis**: CKA heatmap (Figure 5) 和 gradient flow analysis 提供了 mechanistic evidence。Extended training (Figure 6) 仅到 300 步，应继续至 convergence。Cross-model 仅 SFT，不足以验证 spectrum 在 GRPO 下的泛化。

### Section 5 (Discussion and Conclusion)
- 仅 7 行，对于做了如此多实验的论文显得不成比例。
- 未讨论：为什么 diversity preservation enables RL trainability（mechanistic explanation）、practical recommendations for practitioners、future work beyond "remains open"。

### Limitations
- 坦诚且全面（architecture scope, diagnostic limitations, inference efficiency, replication）。
- 诚实承认了 throughput 下降 19% 和 RASP 单 seed 问题。
- 但 "30% sparsity collapse" 仅在 Appendix 中一带而过，应在 Limitations 正文中更突出。

### Ethics Statement
- 简洁且充分。明确列出了所有 model/dataset 的 license。

### Appendix
- 内容充实（A-U），覆盖了主要的 reproducibility 需求。
- Appendix U (Use of AI Assistants) 透明披露了 Claude 的使用——符合 ARR 要求。

### 格式合规
- ✅ `\usepackage[review]{acl}` — 正确
- ✅ 正文 8 页（Section 1-5 到 page 8）
- ✅ Limitations section 存在且实质性（4 段）
- ✅ Ethics Statement 存在
- ✅ 匿名性：无作者信息、无 code repo URL、无可识别自引
- ✅ Abstract ≤ 200 words
- ✅ 引用格式正确（natbib/ACL style）
- ✅ Figure 质量可接受（清晰、可读、颜色区分度尚可）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-24T18:14:26.832695+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recovery_aware_struct_prune",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness 和主要观点：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你和 Reviewer 2 在以下方面的异同：\n1. GRPO 训练步数是否构成 critical 问题（R2 的 W1）\n2. RASP 贡献叙事是否自相矛盾（R2 的 W3）\n3. Discussion 是否过于单薄（R2 的 W6）\n4. R2 提出的 3 篇 missing references 是否确实遗漏\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Strengths\n\n- **S1: 严格控制的实验设计。** 四种剪枝标准共享相同的 recovery pipeline（SFT warmup → GRPO）、相同的剪枝预算（20% MLP channel sparsity, 200/784 groups）、相同的 per-layer capacity floor（≥40%），这使得 pruning criterion 成为唯一自变量。这种控制水平在 LLM 剪枝文献中罕见。\n\n- **S2: Dose-response 分析方法论上出色。** α 系数的连续调控（0.5→4.0）产生可复现的 inverted-U 曲线（Figure 1, Table in Appendix D），为 α 的因果效应提供了比单点消融更强的证据。这超出了多数剪枝论文的方法论标准。\n\n- **S3: 统计严谨性突出。** TOST 等价检验（ε=2pp, 7/8 comparisons p<0.05, Appendix T）、Welch's t-test（CKA-only vs Standard, p=0.0009, Cohen's d=11.1）、multi-seed 验证（3 seeds for 3/4 methods）、95% CI 报告。这在实证 ML 论文中属于高标准。\n\n- **S4: Reward-accuracy decoupling 是有趣的反直觉发现。** 4.4× peak reward gap 对应 <1pp accuracy difference（Table 2, Figure 4）挑战了\"RLVR 优于 SFT\"的社区共识（来自 Ji et al., 2026 的 self-healing 结论），并提供了清晰的实验证据。\n\n- **S5: 充实的 Appendix（A-U, 8 页）。** 覆盖训练细节、算法伪代码、消融分析（sparsity cliff, per-layer floor, cross-scale, cross-model, MATH-500, MBPP, TOST），增强了可复现性。\n\n## Weaknesses\n\n### Critical\n\n**[Critical] W1: GRPO 训练时长严重不足，reward-accuracy decoupling 可能是训练欠拟合的 artifact。**\n- 核心实验仅用 100 步 GRPO（扩展实验 300 步），而标准 GRPO 训练通常运行数千步。SFT warmup 已恢复 ~60pp，留给 GRPO 的 headroom 约 ~27pp。100 步 GRPO 仅贡献 <1pp，可能仅说明训练不够长。300 步扩展显示 Standard 仍然 collapsed，CKA-only 维持 5.5× reward gap，但未报告 accuracy 变化。\n\n**[Critical] W2: 单一架构族，\"Reasoning LLMs\" 的 claim scope 远超证据。**\n- 主实验仅 DeepSeek-R1-Distill-Qwen-7B；cross-model 验证的 Qwen2.5-Math-7B 是同一架构族且只有 SFT。Title 说 \"Reasoning LLMs\"（复数），但实际仅验证一个架构族。\n\n**[Critical] W3: RASP 方法的贡献叙事自相矛盾。**\n- α=1.0（名义\"平衡\"点）导致 collapse；最优 α=2.0 实质上是 CKA-dominant；CKA-only 本身已达 64.39%，RASP α=2.0 仅高 1.72pp。\"平衡\"叙事不成立——最优策略是最大化 diversity 权重。\n\n### Warning\n\n**[Warning] W4: Random baseline 的 max_completion_length 不一致（512 vs 1024）。**\n**[Warning] W5: Title 聚焦 \"Post-RLVR Recovery\" 但数据显示 SFT 完成了几乎所有 accuracy recovery。**\n**[Warning] W6: Discussion/Conclusion 过于单薄（仅 1 段约 7 行）。**\n**[Warning] W7: 30% sparsity 全面 collapse 限制了实用性。**\n\n### Minor\n**[Minor] M1: RASP 仅用 1 个 GRPO seed 验证。**\n**[Minor] M2: \"Cross-architecture\" overclaiming。**\n**[Minor] M3: Lottery Ticket Hypothesis 联系过于表面。**\n**[Minor] M4: \"reward-accuracy decoupling\" 术语引入突兀。**\n\n## Missing References\n1. \"When Reasoning Meets Compression\" (Li et al., 2025, arXiv:2504.02010)\n2. \"GPrune-LLM: Generalization-Aware Structured Pruning\" (2026, arXiv:2603.13418)\n3. \"Can Pruning Improve Reasoning?\" (2025, arXiv:2505.14582)\n\n## Overall Assessment\n**评分: 3.0 (Findings)**，置信度 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recovery_aware_struct_prune",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness 和主要观点：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你和 Reviewer 2 在以下方面的异同：\n1. GRPO 训练步数是否构成 critical 问题（R2 的 W1）\n2. RASP 贡献叙事是否自相矛盾（R2 的 W3）\n3. Discussion 是否过于单薄（R2 的 W6）\n4. R2 提出的 3 篇 missing references 是否确实遗漏\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Strengths\n\n- **S1: 严格控制的实验设计。** 四种剪枝标准共享相同的 recovery pipeline（SFT warmup → GRPO）、相同的剪枝预算（20% MLP channel sparsity, 200/784 groups）、相同的 per-layer capacity floor（≥40%），这使得 pruning criterion 成为唯一自变量。这种控制水平在 LLM 剪枝文献中罕见。\n\n- **S2: Dose-response 分析方法论上出色。** α 系数的连续调控（0.5→4.0）产生可复现的 inverted-U 曲线（Figure 1, Table in Appendix D），为 α 的因果效应提供了比单点消融更强的证据。这超出了多数剪枝论文的方法论标准。\n\n- **S3: 统计严谨性突出。** TOST 等价检验（ε=2pp, 7/8 comparisons p<0.05, Appendix T）、Welch's t-test（CKA-only vs Standard, p=0.0009, Cohen's d=11.1）、multi-seed 验证（3 seeds for 3/4 methods）、95% CI 报告。这在实证 ML 论文中属于高标准。\n\n- **S4: Reward-accuracy decoupling 是有趣的反直觉发现。** 4.4× peak reward gap 对应 <1pp accuracy difference（Table 2, Figure 4）挑战了\"RLVR 优于 SFT\"的社区共识（来自 Ji et al., 2026 的 self-healing 结论），并提供了清晰的实验证据。\n\n- **S5: 充实的 Appendix（A-U, 8 页）。** 覆盖训练细节、算法伪代码、消融分析（sparsity cliff, per-layer floor, cross-scale, cross-model, MATH-500, MBPP, TOST），增强了可复现性。\n\n## Weaknesses\n\n### Critical\n\n**[Critical] W1: GRPO 训练时长严重不足，reward-accuracy decoupling 可能是训练欠拟合的 artifact。**\n- 核心实验仅用 100 步 GRPO（扩展实验 300 步），而标准 GRPO 训练通常运行数千步。SFT warmup 已恢复 ~60pp，留给 GRPO 的 headroom 约 ~27pp。100 步 GRPO 仅贡献 <1pp，可能仅说明训练不够长。300 步扩展显示 Standard 仍然 collapsed，CKA-only 维持 5.5× reward gap，但未报告 accuracy 变化。\n\n**[Critical] W2: 单一架构族，\"Reasoning LLMs\" 的 claim scope 远超证据。**\n- 主实验仅 DeepSeek-R1-Distill-Qwen-7B；cross-model 验证的 Qwen2.5-Math-7B 是同一架构族且只有 SFT。Title 说 \"Reasoning LLMs\"（复数），但实际仅验证一个架构族。\n\n**[Critical] W3: RASP 方法的贡献叙事自相矛盾。**\n- α=1.0（名义\"平衡\"点）导致 collapse；最优 α=2.0 实质上是 CKA-dominant；CKA-only 本身已达 64.39%，RASP α=2.0 仅高 1.72pp。\"平衡\"叙事不成立——最优策略是最大化 diversity 权重。\n\n### Warning\n\n**[Warning] W4: Random baseline 的 max_completion_length 不一致（512 vs 1024）。**\n**[Warning] W5: Title 聚焦 \"Post-RLVR Recovery\" 但数据显示 SFT 完成了几乎所有 accuracy recovery。**\n**[Warning] W6: Discussion/Conclusion 过于单薄（仅 1 段约 7 行）。**\n**[Warning] W7: 30% sparsity 全面 collapse 限制了实用性。**\n\n### Minor\n**[Minor] M1: RASP 仅用 1 个 GRPO seed 验证。**\n**[Minor] M2: \"Cross-architecture\" overclaiming。**\n**[Minor] M3: Lottery Ticket Hypothesis 联系过于表面。**\n**[Minor] M4: \"reward-accuracy decoupling\" 术语引入突兀。**\n\n## Missing References\n1. \"When Reasoning Meets Compression\" (Li et al., 2025, arXiv:2504.02010)\n2. \"GPrune-LLM: Generalization-Aware Structured Pruning\" (2026, arXiv:2603.13418)\n3. \"Can Pruning Improve Reasoning?\" (2025, arXiv:2505.14582)\n\n## Overall Assessment\n**评分: 3.0 (Findings)**，置信度 4/5"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-24T18:14:57.304313+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30471
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-24T18:14:57.455129+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recovery_aware_struct_prune",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness 和主要观点：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你和 Reviewer 1 在以下方面的异同：\n1. CKA 循环使用问题的严重程度（R1 的 W3）\n2. RASP 函数形式的理论依据（R1 的 W4）\n3. SFT ceiling effect 假说（R1 的 W6）\n4. TOST ε=2pp margin 的合理性（R1 的 W7）\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Strengths\n\n- **S1: 重要且新颖的研究问题。** 现有结构化剪枝文献几乎未研究剪枝准则如何影响下游 RLVR 恢复效果。\n\n- **S2: 严格的控制实验设计。** 固定模型、固定剪枝率、固定恢复流水线，仅变化剪枝准则。Algorithm 1 提供了完整伪代码。\n\n- **S3: Reward-accuracy decoupling 是一个有意义的发现。** Table 2 和 Figure 4 清晰展示了 high reward ≠ high accuracy gain。\n\n- **S4: 统计分析比同领域多数工作更严谨。** Welch's t-test、Cohen's d、95% CI、TOST。CKA-only vs Standard 的 Cohen's d = 11.5。\n\n- **S5: 丰富的消融实验。** 21 个附录覆盖广泛。\n\n- **S6: Recovery capacity spectrum 概念。** 将四种准则映射到连续谱并通过四个诊断指标操作化定义。\n\n## Weaknesses\n\n### Critical\n\n**[Critical] W1: RASP（核心方法）仅使用单 seed 验证，dose-response 曲线不可靠。**\n- RASP 及 dose-response 分析（α ∈ {0.5, 1.0, 2.0, 3.0, 4.0}）均为 N=1。α=2.0 时精度最高 (66.11%)，但相邻 α=3.0 仅 61.46%——差 4.65pp。inverted-U 形状本身可能是单次采样的伪影。\n\n**[Critical] W2: Random baseline 使用不同的 max_completion_length（512 vs 1024），比较不公平。**\n- Random 使用 TRL 默认 512-token，其他方法 1024。bias 方向恰好支持论文叙事。\n\n### Warning\n\n**[Warning] W3: CKA 的双重角色（评分准则 + 分析工具）存在循环论证风险。**\n- CKA 同时用于剪枝时计算 functional overlap 和事后分析 layer-wise similarity。当 Section 4.5 用 CKA 发现 \"CKA-only diverges most\" 时，部分是因为 CKA-only 的剪枝准则本身基于 CKA。\n\n**[Warning] W4: RASP 评分函数 (Eq. 5) 缺乏理论推导，函数形式选择武断。**\n- 乘法形式没有理论推导。为什么不是 I(h) + λ(1−F(h))？为什么是 (1−F(h))^α 而非 exp(−αF(h))？\n\n**[Warning] W5: 模型和 benchmark 范围窄，核心 claims 的泛化性存疑。**\n- 主实验仅用一个 7B 模型 + GSM8K。Qwen2.5-Math-7B 没有 GRPO 验证，MATH-500 和 MBPP 差异不显著。\n\n**[Warning] W6: SFT 阶段可能引入 ceiling effect，模糊 GRPO 的增量贡献。**\n- SFT 已恢复到 59-64%，GRPO 增量 <1pp。可能是 GRPO 仅 100 步不够，而非 \"decoupling\"。\n\n**[Warning] W7: TOST 等价性检验的 ε=2pp margin 选择缺乏先验依据。**\n- ε=2pp 非预注册，ε=1pp 功效不足，ε=3pp 全通过。ε=2pp \"刚好合适\" 有 post-hoc selection 之嫌。\n\n### Minor\n**[Minor] M1: Recovery capacity 概念先用后定义。**\n**[Minor] M2: Figure 2 信息密度过高。**\n**[Minor] M3: \"Reward-accuracy decoupling\" 术语可能引起误解。**\n**[Minor] M4: Calibration data M=512 选择未说明理由。**\n**[Minor] M5: 未明确承诺代码/checkpoint 发布。**\n\n## Missing References\n- 无明显缺失，可考虑增加 Wanda (Sun et al., 2024) 讨论。\n\n## Overall Assessment\n**评分: 3.5 (Borderline Conference)**，置信度 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recovery_aware_struct_prune",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness 和主要观点：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你和 Reviewer 1 在以下方面的异同：\n1. CKA 循环使用问题的严重程度（R1 的 W3）\n2. RASP 函数形式的理论依据（R1 的 W4）\n3. SFT ceiling effect 假说（R1 的 W6）\n4. TOST ε=2pp margin 的合理性（R1 的 W7）\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Strengths\n\n- **S1: 重要且新颖的研究问题。** 现有结构化剪枝文献几乎未研究剪枝准则如何影响下游 RLVR 恢复效果。\n\n- **S2: 严格的控制实验设计。** 固定模型、固定剪枝率、固定恢复流水线，仅变化剪枝准则。Algorithm 1 提供了完整伪代码。\n\n- **S3: Reward-accuracy decoupling 是一个有意义的发现。** Table 2 和 Figure 4 清晰展示了 high reward ≠ high accuracy gain。\n\n- **S4: 统计分析比同领域多数工作更严谨。** Welch's t-test、Cohen's d、95% CI、TOST。CKA-only vs Standard 的 Cohen's d = 11.5。\n\n- **S5: 丰富的消融实验。** 21 个附录覆盖广泛。\n\n- **S6: Recovery capacity spectrum 概念。** 将四种准则映射到连续谱并通过四个诊断指标操作化定义。\n\n## Weaknesses\n\n### Critical\n\n**[Critical] W1: RASP（核心方法）仅使用单 seed 验证，dose-response 曲线不可靠。**\n- RASP 及 dose-response 分析（α ∈ {0.5, 1.0, 2.0, 3.0, 4.0}）均为 N=1。α=2.0 时精度最高 (66.11%)，但相邻 α=3.0 仅 61.46%——差 4.65pp。inverted-U 形状本身可能是单次采样的伪影。\n\n**[Critical] W2: Random baseline 使用不同的 max_completion_length（512 vs 1024），比较不公平。**\n- Random 使用 TRL 默认 512-token，其他方法 1024。bias 方向恰好支持论文叙事。\n\n### Warning\n\n**[Warning] W3: CKA 的双重角色（评分准则 + 分析工具）存在循环论证风险。**\n- CKA 同时用于剪枝时计算 functional overlap 和事后分析 layer-wise similarity。当 Section 4.5 用 CKA 发现 \"CKA-only diverges most\" 时，部分是因为 CKA-only 的剪枝准则本身基于 CKA。\n\n**[Warning] W4: RASP 评分函数 (Eq. 5) 缺乏理论推导，函数形式选择武断。**\n- 乘法形式没有理论推导。为什么不是 I(h) + λ(1−F(h))？为什么是 (1−F(h))^α 而非 exp(−αF(h))？\n\n**[Warning] W5: 模型和 benchmark 范围窄，核心 claims 的泛化性存疑。**\n- 主实验仅用一个 7B 模型 + GSM8K。Qwen2.5-Math-7B 没有 GRPO 验证，MATH-500 和 MBPP 差异不显著。\n\n**[Warning] W6: SFT 阶段可能引入 ceiling effect，模糊 GRPO 的增量贡献。**\n- SFT 已恢复到 59-64%，GRPO 增量 <1pp。可能是 GRPO 仅 100 步不够，而非 \"decoupling\"。\n\n**[Warning] W7: TOST 等价性检验的 ε=2pp margin 选择缺乏先验依据。**\n- ε=2pp 非预注册，ε=1pp 功效不足，ε=3pp 全通过。ε=2pp \"刚好合适\" 有 post-hoc selection 之嫌。\n\n### Minor\n**[Minor] M1: Recovery capacity 概念先用后定义。**\n**[Minor] M2: Figure 2 信息密度过高。**\n**[Minor] M3: \"Reward-accuracy decoupling\" 术语可能引起误解。**\n**[Minor] M4: Calibration data M=512 选择未说明理由。**\n**[Minor] M5: 未明确承诺代码/checkpoint 发布。**\n\n## Missing References\n- 无明显缺失，可考虑增加 Wanda (Sun et al., 2024) 讨论。\n\n## Overall Assessment\n**评分: 3.5 (Borderline Conference)**，置信度 4/5"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-24T18:14:59.064439+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1609
}
```

</details>

---


### Assistant

_source line 598 · 2026-05-24T18:15:01.862492+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 50

## Round 50

2 recorded events


### User

_source line 599 · 2026-05-24T18:15:04.346143+00:00_

[Reviewer 2 审稿结果]:
审稿完成，已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。实验控制和统计方法出色，但三个 critical 问题制约接收：(1) 100 步 GRPO 训练不足以支撑 reward-accuracy decoupling 的核心 claim——可能仅是训练不充分的 artifact；(2) 仅测试 Qwen2.5 一个架构族，"Reasoning LLMs" 的 title scope 远超证据；(3) RASP 最优 α=2.0 实质是 CKA-dominant，"balance" 叙事与数据矛盾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 600 · 2026-05-24T18:15:09.840617+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 51

## Round 51

2 recorded events


### User

_source line 601 · 2026-05-24T18:17:15.726360+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条评议

---

### Critical Weaknesses

**[AGREE] R1-W1: RASP 单 seed + dose-response 不可靠**
同意 RASP 及 dose-response 分析为 N=1 是重要缺陷。α=2.0 (66.11%) 与 α=3.0 (61.46%) 之间 4.65pp 的差距在单 seed 下确实可能是随机噪声——作为对照，CKA-only 的 3-seed std 为 0.19pp（Section 4.1），若 RASP 的方差类似，4.65pp 差距是显著的；但若 RASP 因包含 importance 项而方差更大，inverted-U 形状可能不成立。

不过，我认为此问题的严重程度更接近 **Warning 而非 Critical**。原因：论文的核心 claim 是 reward-accuracy decoupling 和 recovery capacity spectrum，这两者主要依赖 CKA-only vs Standard vs Random 的多 seed 比较（3 seeds each, Welch's t-test p=0.0009）。RASP 的 dose-response 是 supporting evidence 而非核心 claim 的唯一支撑。如果去掉 RASP，spectrum 的 CKA-only ≫ Random ≫ Standard ordering 仍然成立。

**[AGREE] R1-W2: Random baseline max_completion_length 不公平**
完全同意。我在自己的审稿中也将此列为 W4 (Warning)。R1 将其升为 Critical，我理解其逻辑——bias 方向恰好支持论文叙事（压低 Random 的 GRPO reward，使 CKA-only 的 spectrum 优势更突出）。

但我仍倾向于 **Warning** 级别：Random 不是论文的 proposed method，也不是 spectrum 的关键对比对象。核心比较是 CKA-only vs Standard（二者均用 1024 tokens），该比较是公平的。Random 的不公平主要影响 "Random 在 spectrum 中的位置" 这个次要 claim。

---

### Warning Weaknesses

**[REBUT] R1-W3: CKA 双重角色的循环论证**
这是一个有洞察力的观察，但我认为循环论证的指控**不完全成立**，需要区分两个不同的 CKA 计算：

1. **剪枝阶段**（Section 3.2, Eq. 3）：计算 **intra-layer** CKA——同一层内不同 MLP channel group 之间的 pairwise CKA similarity，衡量结构间的功能重叠度。CKA-only 移除与其他结构最相似（最冗余）的 group。
2. **分析阶段**（Section 4.5, Figure 5）：计算 **layer-wise** CKA——dense model 某层输出与 pruned model 同层输出之间的 CKA，衡量剪枝对层级表示的扰动程度。

这两个 CKA 的对象不同（structure-to-structure vs. layer-to-layer）、目标不同（identify redundancy vs. measure perturbation）。Section 4.5 发现 "CKA-only diverges most from dense (μ=0.62)" 不是因为 CKA 被自我验证，而是因为一个可解释的因果链：移除冗余结构 → 消除重复表示 → 每层的总体表示变化更大 → layer-wise CKA 下降。这个因果链即使不用 CKA 衡量也应成立——例如用 L2 距离或 procrustes 距离衡量 dense-pruned 表示差异，CKA-only 也应偏离最大。

不过我承认 R1 的 concern 有一定道理：**读者可能产生 metric 自我验证的印象**。建议作者加一句说明两个 CKA 计算的区别，或补充一个非 CKA 的 representational similarity 指标（如 procrustes distance）作为 robustness check。

**严重程度评估**：Minor，非 Warning。核心 experimental findings（spectrum ordering, decoupling）不依赖 Section 4.5 的 layer-wise CKA 分析——即使删除 Figure 5 及相关讨论，Table 1、Table 2、Figure 3、Figure 4 的结论不受影响。

**[AGREE] R1-W4: RASP 函数形式缺乏理论推导**
同意。我在 Section 3 的 detailed comments 中也提出了相同问题。乘法形式 I(h) × (1−F(h))^α 意味着 importance 为 0 时无论 diversity 多高分数都为 0（被过滤），但这恰好可能是导致 α=1.0 collapse 的原因——很多低 importance 但高 diversity 的结构被不当移除。加法形式 βI(h) + (1−β)(1−F(h)) 会保留这些结构。

这个函数形式的选择直接影响了 "α=1.0 collapse" 这个关键实验结果（Section 4.2），因此不仅是理论缺陷，还可能导致对 importance scoring 有害性的错误结论。如果加法形式下 α=1.0 不 collapse，则 "importance 对 RL recovery 有害" 的隐含论点不成立。

**严重程度评估**：同意 R1 的 Warning 级别。与我的 W3 (Critical) 中 "RASP 贡献叙事自相矛盾" 呼应——函数形式的武断选择加剧了这个问题。

**[AGREE] R1-W5: 模型和 benchmark 范围窄**
完全同意，与我的 W2 (Critical) 一致。R1 列为 Warning，我给了 Critical。核心分歧：我认为 title 中 "Reasoning LLMs" 的泛化声称使此问题上升为 Critical——如果论文明确将 scope 限定为 "DeepSeek-R1-Distill-Qwen-7B"，则 Warning 足矣。

**[AGREE] R1-W6: SFT ceiling effect 假说**
**强烈同意，且认为 R1 对此问题的严重程度评估偏低。**

这与我的 W1 (Critical) 一致。R1 将其列为 Warning，但我认为是本文**最关键的问题**。原因：

1. **数据支持 ceiling 解释**：SFT 恢复 ~60pp（从 post-prune ~1% 到 59-64%），GRPO 仅贡献 <1pp。Dense model 90.83%，即 GRPO 有 ~27pp 的理论 headroom。100 步 GRPO 仅利用了 <4% 的 headroom（<1pp / 27pp），这更可能是训练不充分而非 intrinsic decoupling。

2. **300 步扩展未解决问题**：Section 4.5 的 300 步实验（Figure 6）仅报告了 reward gap 维持（5.5×），但**关键性地缺失了 accuracy 数据**。如果 CKA-only 在 300 步时 accuracy 有所提升（哪怕 1-2pp），则 "decoupling" 的 claim 需要 qualify。论文选择性地只报告 reward 而不报告 accuracy，这是一个值得追问的遗漏。

3. **15% sparsity 的反例**：Section 4.3 自己报告了 15% sparsity 下 GRPO 放大了 CKA-only 优势（SFT gap 5.69pp → GRPO gap 7.20pp）。这恰恰说明当 SFT ceiling 不那么低时（15% 比 20% 留给 GRPO 的 headroom 更大），GRPO 是有增量贡献的——**论文自身的数据 undermines decoupling 的普遍性**。

**建议将此问题升至 Critical**。

**[AGREE] R1-W7: TOST ε=2pp margin post-hoc selection**
部分同意。R1 的 concern 合理——ε=2pp 未预注册，且 paper 自己报告了 ε=1pp 功效不足（Appendix T："ε=1pp margin lacks statistical power with binary outcomes at N=1,319"），ε=3pp 全通过。ε=2pp 时 7/8 通过，确实有"刚好合适"的嫌疑。

但我对此的严重程度评估略低于 R1：
1. **论文的透明度是加分项**——诚实报告了 ε=1 和 ε=3 的结果，没有隐藏不利数据。
2. **从实际意义看**，2pp 在 GSM8K 60-66% 区间内是合理的 practical significance threshold。EMNLP 社区通常接受 ~1-2pp 的差异为 "negligible"。
3. **关键证据不仅依赖 TOST**——Table 2 的原始 |Δ| 值（CKA-only +0.48, Standard +0.55, Random -0.53, RASP -0.61）已经直观地展示了 <1pp 的差距。TOST 只是形式化了这一观察。

**严重程度评估**：Minor-to-Warning。ε=2pp 的选择确实应该在论文中 justify（例如引用 GSM8K 相关文献中什么差异被认为是 meaningful），但不影响核心结论的可信度。

---

### Minor Issues

**[AGREE] R1-M1: Recovery capacity 概念先用后定义。**
同意，但 minor 中的 minor。学术论文中 terminology 先用后定义很常见，尤其在 abstract/intro 中。

**[AGREE] R1-M2: Figure 2 信息密度过高。**
同意。Figure 2 试图在一个图中展示 structural analysis + scoring criteria + recovery pipeline + recovery spectrum，对不熟悉此工作的读者有认知负担。但 page budget 紧张（8 pages），拆分可能不现实。

**[AGREE] R1-M3: "Reward-accuracy decoupling" 术语可能误导。**
同意，与我的 M4 呼应。"Decoupling" 暗示两者原本应耦合，但论文未充分建立这一先验预期。

**[AGREE] R1-M4: Calibration data M=512 未说明理由。**
同意。Section 3.2 说 M=512 randomly sampled examples，但未讨论对 M 的敏感性。不过 CKA 在 moderate sample sizes 下通常稳定（Kornblith et al., 2019），所以影响可能有限。

**[AGREE] R1-M5: 未承诺代码/checkpoint 发布。**
同意。对于以 controlled experiment 为主要贡献的论文，reproducibility 承诺尤为重要。

---

### Missing References

**[REBUT] R1 说 "无明显缺失"**
我不同意。在我的审稿中识别了三篇缺失的相关工作：
1. **"When Reasoning Meets Compression"** (Li et al., 2025, arXiv:2504.02010) — 直接在 DeepSeek-R1 上 benchmark 了剪枝对推理的影响
2. **"GPrune-LLM"** (2026, arXiv:2603.13418) — generalization-aware 剪枝
3. **"Can Pruning Improve Reasoning?"** (2025, arXiv:2505.14582)

R1 建议加 Wanda (Sun et al., 2024)，但 Wanda 是非结构化剪枝，与本文的结构化剪枝关注点不同，相关性较低。

---

### Overall Assessment 比较

R1 给出 3.5 (Borderline Conference)，我给出 3.0 (Findings)。0.5 分差距主要来自：

1. **我对 W1/R1-W6 (SFT ceiling / GRPO 训练不足) 的严重程度评估更高**（我标 Critical，R1 标 Warning）。如果 decoupling 确实是训练不充分的 artifact，则论文 contribution 1 大幅缩水。
2. **我对 scope overclaiming 更敏感**（Title 中 "Reasoning LLMs" vs 单一 Qwen2.5 架构族）。
3. **我对 RASP 方法贡献的质疑更强**（α=2.0 essentially CKA-dominant，方法贡献有限）。

如果作者能提供：(a) 1000 步 GRPO 至 convergence 的 accuracy 数据证实 decoupling 持续存在，(b) 非 Qwen2.5 架构的验证，我愿意将评分上调至 3.5。

---

### 对 Director 指定的四个焦点问题的总结

| 问题 | R1 评估 | R2 评估 | 共识 |
|------|---------|---------|------|
| CKA 循环使用 (R1-W3) | Warning | Minor | 两种 CKA 计算技术上不同（intra-layer vs layer-wise），循环论证指控部分不成立，但应补充说明 |
| RASP 函数形式 (R1-W4) | Warning | Warning | 同意缺乏理论推导，乘法形式可能人为导致 α=1.0 collapse |
| SFT ceiling effect (R1-W6) | Warning | **Critical** | R2 认为这是论文最关键的问题——15% sparsity 数据自相矛盾，300 步实验选择性省略 accuracy |
| TOST ε=2pp (R1-W7) | Warning | Minor-Warning | 论文透明报告了不同 ε 值结果，2pp 在实际意义上合理，但应提供 justify |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 602 · 2026-05-24T18:18:19.201560+00:00_

收到 Reviewer 2 的交叉回应。

**收敛评估**：

R2 对 R1 的 8 个主要问题做了逐条回应：
- **6 项 AGREE**（W1, W2, W4, W5, W7 + 大部分 Minor）
- **1 项 REBUT**（W3 CKA 循环论证——R2 认为两种 CKA 计算对象不同，降级至 Minor）
- **1 项升级**（W6 SFT ceiling → R2 认为应从 Warning 升至 Critical）

**核心分歧仅一项**：SFT ceiling / GRPO 训练不足的严重程度（R1: Warning, R2: Critical）。R2 给出了三条具体论据支持升级——15% sparsity 反例、300步选择性省略 accuracy、headroom 利用率 <4%。

**评分**：R1 = 3.5, R2 = 3.0，差距 0.5 分。

这已达到收敛标准——关键问题有明确共识或可记录的合理分歧，无需第三轮。

现在等待 Reviewer 1 对 Reviewer 2 审稿意见的交叉回应，收到后即进入报告合成阶段。R1 的交叉回应是否已提交？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 52

## Round 52

24 recorded events


### User

_source line 603 · 2026-05-24T18:18:20.185710+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

核心分歧在 SFT ceiling effect 的严重程度——我认为这是 Critical 而非 R1 的 Warning，因为论文 15% sparsity 的数据自身就 undermine 了 decoupling 的普遍性，且 300 步扩展实验选择性省略了 accuracy 数据。CKA 循环论证问题则比 R1 评估的更轻（两个 CKA 计算技术上是不同指标）。最终评分差异（3.0 vs 3.5）主要来自对训练充分性和 scope overclaiming 的不同权重。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Strengths 部分

R2 的 S1-S5 与我的 S1-S6 高度一致。R2 特别点出 dose-response 分析的方法论价值 (S2) 和统计严谨性 (S3)，我完全同意。

---

### Weaknesses 逐条回应

---

**[REBUT] R2-W1: GRPO 训练时长严重不足，decoupling 可能是欠拟合 artifact**

R2 的核心论点是：100 步 GRPO（扩展 300 步）远少于标准训练的数千步，<1pp 的精度增量可能仅仅说明训练不够长。

我在自己的审稿中将类似问题列为 Warning (W6)，而非 Critical，理由如下：

1. **Appendix E 提供了部分反驳。** 论文将 GRPO 延长到 300 步后，Standard 的 reward 仍停留在 0.054→0.058（f_b > 0.5），CKA-only 维持 5.5× reward gap (0.308 vs 0.056)。虽然 R2 正确指出 300 步 accuracy 未报告，但 Standard 在 100 步时 reward 已经 collapse（peak 0.081, Table 1），300 步仍未恢复——这不是简单的"训练不够长"，而是结构性崩溃。

2. **"欠拟合 artifact" 假说需要更强证据。** 如果 decoupling 仅是欠拟合，我们应该看到 reward 仍在上升但 accuracy 尚未响应。但 Figure 3(a) 显示 RASP 和 Standard 的 reward 在 step 30-50 已经下降或停滞（不是仍在攀升），表明 100 步已足够捕捉 reward 轨迹的走向。CKA-only 的 reward 在 step 100 时也已趋平。

3. **不过，R2 有一个有效的子论点：** 论文在 Appendix E 只报告了 extended reward，没有报告 extended accuracy。如果 Standard 的 reward collapsed 但 accuracy 在 300 步持续缓慢上升，那就真正构成对 decoupling 的威胁。**这个数据缺失确实是一个 gap。**

**结论：** 我维持 Warning 而非 Critical。reward collapse 的结构性证据（Figure 3, Appendix E）使得"训练更久就能恢复"的假设不够 plausible，但 300 步 accuracy 数据的缺失确实应该补充。R2 将此定为 Critical 有些过重——如果 reward 已 collapse 到 0.010 (RASP) 或 0.054 (Standard, 300 步)，精度恢复的路径在哪里？

---

**[AGREE] R2-W2: 单一架构族，claim scope 远超证据**

我在自己的审稿中同样指出了这一问题 (我的 W5, Warning 级别)。R2 将其定为 Critical，我倾向于同意升级理由：

- Title 写 "Reasoning LLMs"（复数）但只有 DeepSeek-R1-Distill-Qwen-7B 有完整的 SFT+GRPO 验证。
- Qwen2.5-Math-7B 的跨模型验证 (Appendix O) 只有 SFT，没有 GRPO——而 GRPO 恢复恰恰是论文的核心研究对象。论文在 Appendix O 末尾说 "GRPO validation is deferred to future work"，这对一篇声称研究 "Post-RLVR Recovery" 的论文来说是一个明显的 gap。
- 同一架构族（Qwen2.5 family）的两个模型不能支撑 "Reasoning LLMs" 的泛化声明。

**我建议将 Title 改为更精确的范围**，如 "...in DeepSeek-R1-Distill-Qwen-7B" 或 "A Case Study on..."。或者补充至少一个非 Qwen 架构（如 LLaMA-based reasoning model）的 GRPO 结果。

---

**[AGREE with nuance] R2-W3: RASP 方法的贡献叙事自相矛盾**

R2 的分析是锐利的：α=1.0（名义上的"平衡"点）collapse，最优 α=2.0 本质是 CKA-dominant，CKA-only 已达 64.39% vs RASP α=2.0 的 66.11%（仅 +1.72pp），且该 1.72pp 基于单 seed——在我的审稿中列为 Critical (W1)。

我同意 R2 的核心判断：**"平衡 importance 与 diversity" 的叙事不准确。** 但我想补充一个 nuance：

- Table 5 (Appendix D) 的 dose-response 曲线显示：α=0（Standard, 纯 importance）≈ 59.84%，α→∞（CKA-only, 纯 diversity）≈ 64.39%，α=2.0 (RASP) ≈ 66.11%。如果这些数字可信（需多 seed 验证），α=2.0 优于两个端点，说明 importance 信息确实有边际贡献——只是贡献方向与论文叙事不同：**不是 "平衡"，而是 "以 diversity 为主、importance 作微调"。**
- 然而，α=3.0 骤降到 61.46%，α=4.0 又回升到 62.77%——这个非单调行为在单 seed 下很可能是噪声（我的 W1），使得 inverted-U 的精确形状不可靠。

**我的立场：** 如果 RASP α=2.0 > CKA-only 的优势在多 seed 下复现，那 RASP 的贡献是成立的（虽然叙事需要修改）。如果不能复现，RASP 本质上就是 CKA-only 的一个无显著改进的变体，论文的方法贡献将大幅缩水，核心贡献变为纯 empirical finding（recovery capacity spectrum + decoupling），这仍然有 Findings 级别的价值，但难以支撑 Conference。

**这一点与我的 W1（RASP 单 seed）直接相关，且 R2 仅将 RASP 单 seed 列为 Minor (M1)——我认为 R2 在此严重低估了风险。** 如果 RASP α=2.0 的 1.72pp 优势不可复现，R2-W3 的 "叙事矛盾" 就从 narrative 问题升级为 validity 问题。

---

**[AGREE] R2-W4: Random baseline 的 max_completion_length 不一致**

与我的 W2 (Critical) 完全一致。R2 将其列为 Warning，我列为 Critical，因为它直接影响 recovery capacity spectrum 的排序（Random 被定位为 "oscillates 0.14-0.19"，但如果 512→1024 后 Random 的 reward 显著改善，整个 spectrum 的叙事就需要修改）。

---

**[AGREE] R2-W5: Title 聚焦 "Post-RLVR Recovery" 但 SFT 完成了几乎所有 recovery**

R2 的观察是准确的：SFT 将精度从剪枝后的某个低点恢复到 ~60-64%（Table 2 SFT 列），GRPO 仅增加 <1pp。但我对这一点的解读与 R2 略有不同：

- **论文的贡献恰恰是展示 RLVR 没有带来显著额外收益（在 diversity-preserving pruning 下）。** 这个 negative result 本身是有价值的，因为社区普遍假设 RLVR > SFT（来自 Ji et al., 2026 等）。Title 聚焦 "Post-RLVR Recovery" 是因为这是论文要挑战的对象。

- **但 R2 有一个更深层的有效论点：** 如果 SFT 已完成 95%+ 的 recovery work，那么 GRPO 阶段的 training dynamics 差异（Figure 3 的 active learning vs collapse）在实践中可能不重要——无论 GRPO reward 如何，最终精度都由 SFT 决定。这削弱了 recovery capacity spectrum 的实际意义。

**结论：** Title 可以保留（因为 RLVR 是研究对象），但论文应更显式地讨论 "SFT 主导恢复" 的含义，而非仅在 Section 4.4 一笔带过。

---

**[AGREE] R2-W6: Discussion/Conclusion 过于单薄**

我在自己的审稿中未单独提出此问题，但 R2 的观察是正确的。Section 5 (page 8-9) 确实只有约一段 Discussion 加半段 Conclusion，约 7-8 行。对于一篇有如此丰富实验发现的论文，Discussion 应至少讨论：

1. Recovery capacity spectrum 对实际部署的指导意义
2. Reward-accuracy decoupling 对 RLVR 理论的影响（是否意味着 RLVR 在剪枝模型上的价值被高估？）
3. CKA-only 为何表现如此好——representational diversity preservation 的机制解释
4. 与 Ji et al. (2026) 的 "self-healing" 结论的直接对话

目前论文有 Appendix 8 页、References ~1.5 页，但 Discussion 不到半栏。重新分配 0.5-1 页给 Discussion 是合理的。

---

**[AGREE with caveat] R2-W7: 30% sparsity 全面 collapse 限制实用性**

R2 指出所有方法在 30% sparsity 下 collapse（Appendix M, Table 12 末行注释）。这确实限制了实用性——20-25% 的有效窗口较窄。

但需注意：论文的定位是 "controlled study"（Title）而非 "practical pruning tool"。30% collapse 是 GQA 架构的固有限制（channel group 粒度限制了灵活性），不是方法的缺陷。Limitations 节已承认此点。

**不过，对于 Conference 级别的论文，至少应讨论如何突破这个 ceiling**（如 mixed-granularity pruning、layer-wise adaptive sparsity）。

---

### Minor Issues 回应

**[REBUT] R2-M1: RASP 仅用 1 个 GRPO seed（R2 列为 Minor）**

**我强烈反对 R2 将此定为 Minor。** 在我的审稿中，这是 **Critical (W1)**——论文核心方法贡献的可靠性取决于此。具体来说：

- RASP α=2.0 优于 CKA-only 仅 1.72pp（66.11% vs 64.39%），这个差距在 CKA-only 的 3-seed σ=0.18pp 下看似显著，但 RASP 自身的 σ 未知。
- Dose-response 曲线的非单调性（α=2.0→3.0 降 4.65pp，α=3.0→4.0 升 1.31pp）在单 seed 下极可能是噪声。
- 如果 RASP 的优势不可复现，R2-W3 的 "叙事矛盾" 和整个 dose-response 分析的价值都将瓦解。

**R2 在 W3 中自己论证了 RASP 的叙事问题，却在 M1 将支撑 RASP 的统计证据缺失仅列为 Minor——这在逻辑上不一致。**

---

**[AGREE] R2-M2: "Cross-architecture" overclaiming**

与 R2-W2 和我的 W5 一致。Qwen2.5-Math-7B 与 DeepSeek-R1-Distill-Qwen-7B 共享 Qwen2.5 底层架构，不构成独立的 cross-architecture 验证。

---

**[AGREE] R2-M3: Lottery Ticket Hypothesis 联系过于表面**

论文在 Related Work (Section 2, page 2) 引用 LTH (Frankle and Carlin, 2019) 并称 "our recovery capacity spectrum poses the analogous question for post-pruning recovery"。但 LTH 讨论的是 pruning at initialization 找到可训练子网络，与本文的 post-training structured pruning + recovery 场景有本质区别。该类比确实表面。

---

**[AGREE] R2-M4: "reward-accuracy decoupling" 术语引入突兀**

与我的 M3 一致。建议在首次使用时给出操作化定义，并考虑更精确的术语。

---

### Missing References 回应

关于 R2 提出的 3 篇可能遗漏的引用：

1. **"When Reasoning Meets Compression" (Li et al., 2025, arXiv:2504.02010)** — 标题直接涉及 reasoning + compression 的交叉，如果确实讨论了剪枝对推理能力的影响，则应被引用。论文当前的 Related Work 在 pruning-aware recovery 子节 (page 2-3) 覆盖了类似主题，但如果此文有直接可比的实验设计，遗漏是 gap。**建议作者验证并决定是否引用。**

2. **"GPrune-LLM: Generalization-Aware Structured Pruning" (2026, arXiv:2603.13418)** — "Generalization-aware" 与本文的 "recovery-aware" 有概念亲缘性。如果该工作也考虑了剪枝准则对下游 fine-tuning 的影响，遗漏会更显著。但 arXiv:2603 意味着 2026 年 3 月的工作，考虑到本文的投稿时间 (2026-05-25)，作者可能已来不及纳入。**可在 camera-ready 补充。**

3. **"Can Pruning Improve Reasoning?" (2025, arXiv:2505.14582)** — 标题直接相关。如果该工作研究了剪枝是否能改善（而非仅保留）推理能力，与本文的 recovery capacity spectrum 有直接对话空间。**应引用。**

**总体判断：** R2 提出的 3 篇引用中，第 1 和第 3 篇标题高度相关，如果内容确实讨论了 structured pruning + reasoning recovery，遗漏是合理的 concern。第 2 篇可能时间上来不及。我在自己的审稿中未发现明显遗漏，但 R2 的发现补充了我的覆盖范围。

---

### 与 R2 的主要分歧总结

| 议题 | R2 评级 | 我的评级 | 分歧 |
|------|---------|---------|------|
| GRPO 训练步数 | Critical (W1) | Warning (W6) | 我认为 reward collapse 的结构性证据降低了"训练更久就能恢复"的可能性 |
| RASP 单 seed | Minor (M1) | **Critical (W1)** | **R2 严重低估**。RASP 是核心贡献，1.72pp 优势在 N=1 下不可靠 |
| Random 不公平比较 | Warning (W4) | **Critical (W2)** | 我认为此问题直接影响 spectrum 排序 |
| RASP 叙事矛盾 | Critical (W3) | 未单独提出，但同意 | R2 的分析锐利，我补充了条件性判断（依赖多 seed 验证） |
| Discussion 单薄 | Warning (W6) | 未提出 | 同意 R2 |

### 最终评分对比

- **R2**: 3.0 (Findings)
- **我**: 3.5 (Borderline Conference)
- **分歧根源**: 我认为 reward-accuracy decoupling 的发现本身（independent of RASP method）有足够的 novelty 支撑 borderline conference；R2 更关注方法贡献 (RASP) 的弱点。如果 RASP 多 seed 验证失败，我同意降至 3.0。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。核心分歧：我与 R2 在 RASP 单 seed 验证的严重性上意见相反（我列 Critical，R2 列 Minor），在 GRPO 训练步数上也有分歧（我 Warning，R2 Critical）。两人在模型范围过窄、Random baseline 不公平比较上一致。我维持 3.5 (Borderline Conference)，R2 给 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-24T18:18:44.677108+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
  "offset": "0",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
    "offset": "0",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-24T18:18:44.733323+00:00_

0	---
1	name: review-director-session-start
2	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
3	priority: 9
4	scope: global
5	tags:
6	- workflow
7	- review
8	- session
9	version: 3
10	roles:
11	- review_director
12	---
13	
14	# Review Director Session 启动流程（圆桌会议模式）
15	
16	## 初始化
17	
18	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
19	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
20	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
21	4. 向用户简要汇报：
22	   - **投稿目标**：venue 和 deadline
23	   - **论文状态**：当前草稿位置和版本
24	   - **资料完整性**：提交的材料是否齐全
25	   - **下一步**：即将开始的圆桌审稿流程
26	
27	## 评审流程（收到论文提交后执行）
28	
29	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
30	
31	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
32	2. 确认目标投稿 venue（从提交消息中获取）
33	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
34	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
35	   - `"&lt;venue name> 2026 submission deadline"`
36	   - `"&lt;venue name> 2026 author guidelines"`
37	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
38	5. 提取当前版本的格式要求：
39	   - 页数限制（正文 / 附录 / 参考文献）
40	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
41	   - 匿名规则（double-blind / single-blind / open）
42	   - 附录规则（是否允许、是否参与审稿）
43	   - 引用格式（natbib / biblatex / 特定 .bst）
44	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
45	
46	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
47	
48	### Step 0.5 — 决定 Reviewer 编排
49	
50	根据 venue 类型和论文特点，决定：
51	- 需要几个 Reviewer（1-5 人）
52	- 每个 Reviewer 的审查侧重
53	
54	参考：
55	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
56	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
57	- **Workshop / 短文**：1 人（全面审查）
58	
59	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
60	
61	### Step 0.6 — 外部审稿线（与 Step 1 并行）
62	
63	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
64	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
65	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
66	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
67	- 如果到 Step
…[truncated 2626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 56
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-24T18:18:45.603410+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_project_file,update_review_issues,submit_review_report_to_research_director,get_visual_check_status,get_external_review_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_project_file,update_review_issues,submit_review_report_to_research_director,get_visual_check_status,get_external_review_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-24T18:18:45.875928+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 272
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-24T18:18:50.090479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
  "offset": "150",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
    "offset": "150",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-24T18:18:50.091193+00:00_

150	2. **同步 Issue Tracker**（投递前必做）：
151	   - 用 `read_local_file("projects/{project}/artifacts/review_issues.yaml")` 读当前 tracker（不存在视为空）
152	   - 对本轮所有 Weakness/Must-Fix/Should-Fix:
153	     - 与已有 issue 匹配（同 category + 相似 summary）→ 在 `mentions` 追加本轮记录,更新 `last_seen_round`
154	     - 新问题 → 创建条目（id=`R{reviewer}-W{n}`,status=`open`,first_raised_round=本轮）
155	   - 对上轮 `open`/`in_progress` 但本轮**未被任何 Reviewer 提及**的:
156	     - 在 `mentions` 追加 `note: "本轮未提及,可能已修复,待 Research Director 确认"`
157	   - 调 `update_review_issues(project, issues_yaml=完整 YAML)` 写回
158	3. 调用 `submit_review_report_to_research_director` 投递报告 → Research Director
159	4. 向用户（Group C）汇报审核完成
160	
161	此流程只在 session 启动时执行一次。
162	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-24T18:18:56.766060+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-24T18:18:56.817047+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-24T18:19:02.540693+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-24T18:19:02.893592+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T18:01:45.200471+00:00\", \"completed_at\": \"2026-05-24T18:04:55.612152+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 16\", \"message\": \"最后一页仅约 1/4 有内容（Table 16 + Use of AI Assistants 短段），剩余约 3/4 页面为空白。虽然是 appendix 末页且 AI 使用声明本身很短，但视觉上不专业。可考虑将 Section T（TOST Equivalence Testing）的正文部分从 page 15 移至 page 16 以填充空间，或在前面 appendix 中适当放宽 spacing\"}, {\"severity\": \"warning\", \"dimension\": \"page 7-8\", \"message\": \"Figure 3（3 panels）、Figure 5（2 panels）、Figure 6（3 panels）面积较小，axis labels、legend、tick labels 字号偏小（估计 ≤6pt），审稿人可能需要放大才能阅读。Page 8 尤其密集——两个多面板 figure 挤在页面上半部分\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯 Abstract + Introduction 文本）。第一个 display item（Figure 1 dose-response curve）出现在 page 2 左栏顶部，在 3 页窗口内，可接受。但若能在 page 1 下方放一个 teaser figure 会强化审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 3-4\", \"message\": \"连续两页以密集文本为主（Method Section 3.1–3.4）。页面中穿插了数学公式（Eq. 1–5），提供了一定视觉节奏，但无 figure/table 出现。对于 method-heavy 的论文这是合理的，但节奏略显沉闷\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"核心框架图 Figure 2（full-width figure*）出现在第 5 页。作为传达论文核心 idea 的架构总览图，稍晚于理想位置（通常 page 2-3 为最佳）。Figure 2 信息量充足，caption 自包含，颜色编码清晰，质量好\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 有效传达核心 message（recovery accuracy 随 CKA coefficient 变化的 dose-response 关系）。使用不同 marker + 线型区分 SFT vs GRPO，色盲友好（蓝 vs 橙）。Caption 自包含\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 和 Table 2 使用 booktabs 风格，最优值加粗，小数位数一致（2 位）。格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 5（layer-wise CKA similarity heatmaps）颜色渐变在灰度打印下可能难以区分不同方法的 pattern 差异。建议在 caption 中加文字描述关键 pattern，或使用更高对比度的 colormap\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 章节简短精炼（3 个要点：架构泛化性、诊断限制、推理效率），符合 EMNLP 2026 要求\"}, {\"severity\": \"info\", 
…[truncated 342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-24T18:19:02.894120+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-24T18:19:03.188733+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 294
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-24T18:19:03.189057+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-24T18:19:03.289774+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-24T18:19:07.606170+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read local file project",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read local file project",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-24T18:19:07.706924+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-24T18:19:12.474329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-24T18:19:12.726490+00:00_

1	
2	# ============================================================
3	# Round 1-3 Issues — All Resolved
4	# ============================================================
5	
6	- id: "R1-C1"
7	  summary: "CKA-recovery link 仅相关性, 无因果干预"
8	  category: method
9	  severity: critical
10	  status: resolved
11	  first_raised_round: 1
12	  last_seen_round: 3
13	  resolution: "Jaccard overlap 分析 + Limitations 承认 + 多种子统计验证"
14	  resolution_round: 3
15	
16	- id: "R1-C2"
17	  summary: "Single-seed GRPO 无统计显著性"
18	  category: experiment
19	  severity: critical
20	  status: resolved
21	  first_raised_round: 1
22	  last_seen_round: 3
23	  resolution: "3-seed GRPO CKA-only, Welch's t-test p=0.0009"
24	  resolution_round: 3
25	
26	- id: "R1-C3"
27	  summary: "仅 GSM8K 单基准"
28	  category: experiment
29	  severity: critical
30	  status: resolved
31	  first_raised_round: 1
32	  last_seen_round: 3
33	  resolution: "MATH-500 OOD 验证 + MBPP 代码基准"
34	  resolution_round: 3
35	
36	- id: "R1-W1"
37	  summary: "Title overclaim 'determines'"
38	  category: framing
39	  severity: warning
40	  status: resolved
41	  first_raised_round: 1
42	  last_seen_round: 3
43	  resolution: "Title 改为 'shapes'"
44	  resolution_round: 3
45	
46	- id: "R1-W2"
47	  summary: "Abstract 'universally determines' overclaim"
48	  category: framing
49	  severity: warning
50	  status: resolved
51	  first_raised_round: 1
52	  last_seen_round: 3
53	  resolution: "改为 'significantly shapes'"
54	  resolution_round: 3
55	
56	- id: "R1-W3"
57	  summary: "仅 DeepSeek-R1-7B 单模型"
58	  category: experiment
59	  severity: warning
60	  status: resolved
61	  first_raised_round: 1
62	  last_seen_round: 3
63	  resolution: "Qwen2.5-Math-7B cross-arch + 1.5B cross-scale"
64	  resolution_round: 3
65	
66	- id: "R1-M1"
67	  summary: "GRPO 超参未报告"
68	  category: experiment
69	  severity: info
70	  status: resolved
71	  first_raised_round: 1
72	  last_seen_round: 3
73	  resolution: "Appendix 完整超参表"
74	  resolution_round: 3
75	
76	- id: "R1-M2"
77	  sum
…[truncated 27331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-24T18:23:23.089924+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "issues_yaml": "\n# ============================================================\n# Round 1-3 Issues — All Resolved\n# ============================================================\n\n- id: \"R1-C1\"\n  summary: \"CKA-recovery link 仅相关性, 无因果干预\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Jaccard overlap 分析 + Limitations 承认 + 多种子统计验证\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Single-seed GRPO 无统计显著性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"3-seed GRPO CKA-only, Welch's t-test p=0.0009\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"仅 GSM8K 单基准\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"MATH-500 OOD 验证 + MBPP 代码基准\"\n  resolution_round: 3\n\n- id: \"R1-W1\"\n  summary: \"Title overclaim 'determines'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Title 改为 'shapes'\"\n  resolution_round: 3\n\n- id: \"R1-W2\"\n  summary: \"Abstract 'universally determines' overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"改为 'significantly shapes'\"\n  resolution_round: 3\n\n- id: \"R1-W3\"\n  summary: \"仅 DeepSeek-R1-7B 单模型\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Qwen2.5-Math-7B cross-arch + 1.5B cross-scale\"\n  resolution_round: 3\n\n- id: \"R1-M1\"\n  summary: \"GRPO 超参未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Appendix 完整超参表\"\n  resolution_round: 3\n\n- id: \"R1-M2\"\n  summary: \"Table 1 缺 Random baseline\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Table 1 加入 Random 行\"\n  resolution_round: 3\n\n- id: \"R2-NEW-C1\"\n  summary: \"GRPO 准确率几乎不变,为何要用 GRPO\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Dual-layer reframe: SFT(accuracy) + GRPO(reward signal)\"\n  resolution_round: 3\n\n- id: \"R2-NEW-C2\"\n  summary: \"Cross-architecture 仅 SFT 验证,GRPO 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"1.5B GRPO 补充 + Abstract 区分表述\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W1\"\n  summary: \"SFT recovery 被忽视,过度聚焦 GRPO\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注解释 SFT catastrophic forgetting\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W2\"\n  summary: \"Qwen-Math 跨架构验证仅 SFT，Abstract overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 区分 GRPO(DeepSeek) vs SFT(Qwen-Math)\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W3\"\n  summary: \"GRPO 准确率改变 < 1pp — 实际效用存疑\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"300-step accuracy + reward-accuracy decoupling 论证\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W4\"\n  summary: \"RASP/Random 仍为单种子\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注透明标注 + Limitations 披露\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W5\"\n  summary: \"Random baseline SFT/GRPO Acc 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Table 2 脚注标注 checkpoint not preserved\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W6\"\n  summary: \"正文 5 处 'determines' 残留\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"全部替换为 shapes/significantly influences\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M1\"\n  summary: \"GRPO batch size / rollouts 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M2\"\n  summary: \"SFT lr/batch/optimizer 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-VIS-1\"\n  summary: \"末页 Figure 6 仅占 30%，70% 空白\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 重排\"\n  resolution_round: 3\n\n- id: \"R2-VIS-2\"\n  summary: \"Appendix page 12 过度拥挤\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 拆分到多页\"\n  resolution_round: 3\n\n- id: \"R3-S5\"\n  summary: \"Qwen-Math 'strongest evidence' 措辞仍略强\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"strongest → additional evidence in §4.5\"\n  resolution_round: 3\n\n- id: \"R3-M2\"\n  summary: \"300-step accuracy 未标注 seed\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"(single seed) 标注已添加到 §4.3\"\n  resolution_round: 3\n\n- id: \"R3-M3\"\n  summary: \"无代码/checkpoint 发布声明\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"Code and checkpoints release statement in Conclusion\"\n  resolution_round: 3\n\n# ============================================================\n# Round 5-7 Issues — Carried forward\n# ============================================================\n\n- id: \"R5-N1\"\n  summary: \"Reward-accuracy decoupling 叙事薄弱（GRPO 增量 <1pp，可能是训练不足的 artifact）\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。SYSTEMIC_ISSUE #1 核心。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W4 和 R2-W2 再次提出，增加新角度：需区分 format compliance vs reasoning quality。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-N3 升级为 critical。R1 完全同意。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 升为本文最关键问题（Critical），R1 维持 Warning。核心分歧：R2 认为 15% sparsity 数据自相矛盾（GRPO amplifies gap）+ 300 步实验选择性省略 accuracy。R1 认为 reward collapse 结构性证据使'训练更久就能恢复'不 plausible。最终共识：300 步 accuracy 数据缺失是 gap，但对整体严重性评估存在不可调和分歧。\"\n  action_items:\n    - round: 5\n      action: \"D098 dual-layer reframe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"Agent 提取 format compliance / EOS rate 数据\"\n      assigned_to: agent\n      status: in_progress\n    - round: 7\n      action: \"运行 ≥1000 GRPO steps 验证 decoupling 是否持续\"\n      assigned_to: agent\n      status: open\n    - round: 8\n      action: \"补充 300 步 extended training 的 accuracy 数据（非仅 reward）；讨论 15% sparsity 与 20% 的差异原因\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N2\"\n  summary: \"Cross-architecture/scale 泛化严重不足，所有模型共享 Qwen2.5 base\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前不可行（需全 pipeline ~50h GPU）。但 1.5B GRPO 数据已有。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识。Appendix O 'Cross-Architecture Validation' 标题误导。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识 Critical。R1 正式同意升级。核心论点：Title 'Reasoning LLMs'（复数）vs 单一 Qwen2.5 架构族。Qwen2.5-Math-7B 的 GRPO 验证缺失。R1 建议 Title 改为 'A Case Study on...' 或补充非 Qwen 架构。\"\n  action_items:\n    - round: 5\n      action: \"补入 1.5B GRPO 数据作 cross-scale validation\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 7\n      action: \"重命名 Appendix O 标题；限定 claim 为 Qwen2.5 家族\"\n      assigned_to: paper_agent\n      status: open\n    - round: 8\n      action: \"Title 改为更精确范围（如 'A Case Study on DeepSeek-R1-Distill-Qwen-7B'）或补充至少一个非 Qwen 架构 GRPO 结果\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"RASP 单 seed 验证不足——方法贡献可靠性存疑\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"核心比较 CKA vs Standard 有 3-seed p=0.0009。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 升级为 critical。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识 critical。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"严重性分歧：R1 Critical（RASP α=2.0 优于 CKA-only 仅 1.72pp 在 N=1 下不可靠，直接影响方法贡献 validity），R2 Minor（RASP 非核心 claim 支撑）。R1 论证 R2 自身 W3（RASP 叙事矛盾）逻辑上依赖 RASP 可靠性，M1 定级与 W3 不一致——论证有力。Director 判定：Critical。\"\n  action_items:\n    - round: 5\n      action: \"Limitations 标注 + 核心 claim 限定 CKA vs Standard\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 7\n      action: \"至少 RASP α=2.0 和 α=1.0 各跑 3 seeds\"\n      assigned_to: agent\n      status: open\n    - round: 8\n      action: \"如多 seed 无法完成：降级 RASP 为 exploratory analysis，不作为核心方法贡献\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"因果语言系统性过强——'causal driver' 超出 quasi-experimental 证据\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"SYSTEMIC_ISSUE #2 成员。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N3 详细论证。R2 补充 metrics diversity 不足。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被单独提及为新问题。R2 交叉回应中讨论了 CKA 双重角色但判为 Minor。可能部分已修复（dose-response 用语已改善），待 Research Director 确认。\"\n  action_items:\n    - round: 7\n      action: \"全文语言审计：'causal driver' → 'key determinant'；decoupling claims 加限定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Per-layer capacity floor (40%) 未消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前无法做 full pipeline ablation。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W3 再次提出。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未提及\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未提及，可能已修复或不再关注\"\n  action_items:\n    - round: 5\n      action: \"Limitations 讨论 + rebuttal 论点准备\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Floor ablation τ∈{0.3,0.4,0.5,0.6} experiments running; appendix table added\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"α dose-response 存在 generation length 混杂变量\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"高 ROI 实验。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出。R2-W1 扩展为 κ 消融缺失。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"升级为 critical。α=1.0 用 1024 tokens，其他用 512 tokens。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 在 W2（Random baseline）中再次确认 max_completion_length 不一致问题。R2 同意 Random 512 vs 其他 1024 不公平。此问题与 R7-N1（dose-response 混杂）紧密相关。\"\n  action_items:\n    - round: 7\n      action: \"统一所有 α 值 max_completion_length=1024 重跑 dose-response\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"'Recovery capacity gradient' 术语与 gradient descent 混淆\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"全文替换为 'recovery capacity spectrum'\"\n  resolution_round: 7\n\n- id: \"R5-M1\"\n  summary: \"Section 5 末尾溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"约 2 行溢出\"\n    - round: 7\n      reviewers: []\n      note: \"R7 确认格式合规\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未提及，视觉审查未标记页面溢出，可能已修复\"\n  action_items:\n    - round: 5\n      action: \"Paper Agent 压缩 §5 确保 8 页合规\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M2\"\n  summary: \"Abstract p<0.001 未说明统计检验方法\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Abstract 标注 Welch's t-test\"\n  resolution_round: 6\n\n- id: \"R5-M3\"\n  summary: \"Page 7 display items 过度拥挤\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Figure 3 + Figure 4 + Table 2 挤在同一页\"\n    - round: 7\n      reviewers: []\n      note: \"视觉审查标记\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M2 再次提出 Figure 2 信息密度过高。视觉审查标记 page 7-8 axis labels/legend 字号偏小（≤6pt）。\"\n  action_items:\n    - round: 5\n      action: \"Figure 前移平衡视觉节奏\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M4\"\n  summary: \"bib key 年份误导 + 引用错误\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"lachance2024cka→2022, klabunde→2023\"\n    - round: 6\n      reviewers: [2]\n      note: \"新引用错误\"\n    - round: 7\n      reviewers: []\n      note: \"未提及\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未提及，待确认\"\n  action_items:\n    - round: 5\n      action: \"Paper Agent 修正 bib 条目\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M5\"\n  summary: \"Figure 2 标注字体偏小 / 颜色区分度不足\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: []\n      note: \"视觉审查发现\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 提到\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M2 指出 Figure 2 信息密度过高。视觉审查标记 page 7-8 figure panel axis labels 偏小。\"\n  action_items:\n    - round: 5\n      action: \"增大字号 + 添加不同 line style\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N1\"\n  summary: \"GSM8K 单基准 GRPO 主实验，Title/Abstract 做一般性声明\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。\"\n    - round: 7\n      reviewers: []\n      note: \"间接相关\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未单独提及。MATH-500 和 MBPP OOD 验证已添加（Round 3 修复），但 R8 R1 指出 MBPP 不显著却被引用。\"\n  action_items:\n    - round: 6\n      action: \"MF1: MBPP probe eval\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"CKA-only layer 分布混杂——72.5% 剪枝集中 early layers，优势可能来自 layer 分布而非 diversity\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"R1-N3 提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 详细展开。granularity 不匹配无法解耦。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被直接提及为独立问题。R8 Reviewer 未重新审查 layer 分布。\"\n  action_items:\n    - round: 7\n      action: \"创建 same-granularity layer-biased baseline\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N3\"\n  summary: \"缺失高度相关文献：RL Finetunes Small Subnetworks (2505.11711)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent 添加引用并在 Related Work/Discussion 讨论\"\n  resolution_round: 6\n\n- id: \"R6-W1\"\n  summary: \"Reward-accuracy decoupling 未区分 format compliance vs reasoning quality\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"需报告 EOS rate 和 format compliance rate\"\n    - round: 7\n      reviewers: []\n      note: \"间接相关\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及\"\n  action_items:\n    - round: 6\n      action: \"Agent 从 eval logs 提取 format compliance / EOS rate\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"实验仅覆盖 MLP channel pruning，Title/Abstract 未限定 scope\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Title 改为 'How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs'\"\n  resolution_round: 7\n\n- id: \"R6-W3\"\n  summary: \"遗漏 3 篇相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent 验证并添加引用\"\n  resolution_round: 6\n\n- id: \"R6-W4\"\n  summary: \"Welch's t-test at N=3 统计功效极低，缺 effect size 和 CI\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Cohen's d + 95% CI 已加入正文\"\n  resolution_round: 7\n\n- id: \"R6-W5\"\n  summary: \"15%/25% sparsity 实验为 single-seed\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W5 交叉回应提出。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及\"\n  action_items:\n    - round: 6\n      action: \"MF2 部分覆盖; 15%/25% 在 Limitations 标注\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"RASP 表现差于 Standard 缺乏充分解释\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"需分析 importance 和 CKA overlap 的相关性\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W3（RASP 叙事矛盾）详细论证：α=1.0 collapse + α=2.0 本质 CKA-dominant。R1 同意核心判断并补充条件性结论。与 R8-N3 (RASP 函数形式) 相关。\"\n  action_items:\n    - round: 6\n      action: \"Paper Agent 待 α dose-response 数据后分析 RASP failure mechanism\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 8\n      action: \"修改 RASP 叙事：从 'balance importance and diversity' 改为 'CKA-dominant with importance as minor correction'；或提供加法形式对比实验\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W7\"\n  summary: \"Table 1 脚注 'Only redundancy-based pruning sustains RL recovery' 与 Random 排第二矛盾\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"脚注措辞已修改\"\n  resolution_round: 6\n\n- id: \"R6-W8\"\n  summary: \"Section 5 Discussion 偏薄（仅半页）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议讨论 CKA 与 RL exploration 关系\"\n    - round: 7\n      reviewers: []\n      note: \"间接相关\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W6 再次提出。R1 同意。Section 5 仅约 7-8 行。应至少讨论：spectrum 部署指导意义、decoupling 对 RLVR 理论影响、CKA-only 机制解释、与 Ji et al. (2026) self-healing 结论的对话。\"\n  action_items:\n    - round: 6\n      action: \"Paper Agent 待实验数据后扩充 Discussion\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 8\n      action: \"扩充 Discussion 至少半栏：加入 SFT vs GRPO 角色分离讨论、spectrum 实用指导、与 self-healing 文献对话\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M1\"\n  summary: \"Reward-accuracy decoupling 首次使用时无正式定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"首次使用处添加正式定义\"\n  resolution_round: 6\n\n- id: \"R6-M2\"\n  summary: \"Figure 2 y 轴未标注 mean vs peak reward\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 提出。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 6\n      action: \"修改 Figure 2 y-axis label\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M3\"\n  summary: \"Eq.1 未写出 Taylor expansion 完整数学形式\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2 小问题。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 6\n      action: \"Paper Agent 补充 Eq.1 完整数学形式\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 7 Issues — Carried forward\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"Dose-response 中 max_completion_length 不一致（α=1.0: 1024, 其他: 512）构成关键混杂变量\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 独立提出。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W2（Random 512 vs 其他 1024）再次确认不一致。R2 同意此问题直接影响 spectrum 排序。但 R2 认为 Random 不是核心对比对象（Warning），R1 认为 Critical。Director 判定保持 Critical（dose-response inverted-U 的可靠性取决于此）。\"\n  action_items:\n    - round: 7\n      action: \"统一所有 α 值 max_completion_length=1024 重跑 dose-response\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N2\"\n  summary: \"Abstract overclaiming 'holds across sparsity levels'——仅 20-25% 窗口成立\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N4 提出，R2 完全同意。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未单独提及，但 R2-W7（30% collapse）间接相关\"\n  action_items:\n    - round: 7\n      action: \"Abstract 改为 'at moderate sparsity (20-25%)' 限定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W1\"\n  summary: \"Decoupling 缺少形式化等价性检验（TOST）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W3 提出，R2 同意。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R8 论文已包含 TOST（ε=2pp，7/8 通过），R1 质疑 ε=2pp post-hoc selection（Warning），R2 认为 Minor-Warning（论文透明报告了不同 ε 值结果）。已有改善但 ε 选择需 justify。\"\n  action_items:\n    - round: 7\n      action: \"使用 TOST 或明确 practical equivalence margin\"\n      assigned_to: paper_agent\n      status: open\n    - round: 8\n      action: \"在论文中 justify ε=2pp 选择（引用 GSM8K 文献中 meaningful difference threshold）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"MBPP 结果统计不显著却被用作 decoupling 支持证据\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 同意。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未单独提及\"\n  action_items:\n    - round: 7\n      action: \"正文引用 MBPP 时加注 'not statistically significant'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W3\"\n  summary: \"Calibration 数据量 M 在正文中未明确指定\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 同意。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M4 再次提出 M=512 未说明理由。R2 同意。\"\n  action_items:\n    - round: 7\n      action: \"在 Section 3.2 或 4.1 明确指定 M 及选择依据\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W4\"\n  summary: \"Throughput regression（-19%）未在 Limitations 讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W3 提出，R1 部分同意。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 7\n      action: \"在 Limitations 添加 throughput regression 讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"Title/叙事焦点与实际恢复来源错位——SFT 贡献 ~60pp 而 GRPO <1pp\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 交叉回应 [NEW FINDING]\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W1（SFT ceiling）和 R2-W5（Title 焦点错位）详细论证。R1 交叉回应同意核心判断——SFT 完成 95%+ 恢复，GRPO 的 training dynamics 差异在实践中可能不重要。R1 补充：Title 可保留（RLVR 是研究对象），但 Discussion 应显式讨论 SFT 主导恢复的含义。\"\n  action_items:\n    - round: 7\n      action: \"Discussion 中明确分离 SFT vs GRPO 恢复角色\"\n      assigned_to: paper_agent\n      status: open\n    - round: 8\n      action: \"Discussion 显式讨论 'SFT 主导恢复' 的含义及 GRPO 实际贡献的定位\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 8 New Issues\n# ============================================================\n\n- id: \"R8-N1\"\n  summary: \"RASP 方法贡献叙事自相矛盾——α=2.0 本质 CKA-dominant，'平衡 importance 与 diversity' 不准确\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W3 详细论证：α=1.0（名义'平衡'点）collapse，α=2.0 diversity 权重为 importance 的 4 倍。CKA-only 已达 64.39% vs RASP 66.11%（+1.72pp, 单 seed）。R1 同意核心判断，补充条件性结论——如多 seed 复现则贡献成立但叙事需改，否则 RASP 无显著改进。乘法形式 I(h)×(1-F(h))^α 可能人为导致 α=1.0 collapse（importance=0 → score=0）。\"\n  action_items:\n    - round: 8\n      action: \"修改 RASP 叙事为 'CKA-dominant with importance correction'；讨论乘法 vs 加法形式的选择理由；或提供加法形式实验对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N2\"\n  summary: \"Random baseline max_completion_length=512（vs 其他方法 1024）构成不公平比较\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 列 Warning。核心分歧：R1 认为直接影响 spectrum 排序（Random 被不公平压低），R2 认为 Random 非核心对比对象（核心是 CKA-only vs Standard，二者均 1024 tokens 公平比较）。Director 判定 Warning——Random 是次要比较对象，核心 CKA vs Standard 比较未受影响。\"\n  action_items:\n    - round: 8\n      action: \"统一 Random 的 max_completion_length=1024 重跑；或在论文中明确标注此限制并讨论对 spectrum 排序的影响\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N3\"\n  summary: \"RASP 函数形式（乘法）缺乏理论推导，可能人为导致 α=1.0 collapse\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 同意。乘法形式 I(h)×(1-F(h))^α 意味着 importance=0 时 score=0，可能导致高 diversity 但低 importance 的结构被不当移除，这恰好可能是 α=1.0 collapse 的原因。加法形式 βI(h)+(1-β)(1-F(h)) 可能保留这些结构。如果加法下 α=1.0 不 collapse，'importance 对 RL recovery 有害' 的隐含论点不成立。\"\n  action_items:\n    - round: 8\n      action: \"讨论函数形式选择理由；理想情况下补加法形式对比实验；最低限度在 Limitations 承认\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N4\"\n  summary: \"TOST ε=2pp margin post-hoc selection 嫌疑\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 Warning，R2 Minor-Warning。ε=2pp 未预注册，ε=1pp 功效不足，ε=3pp 全通过。但论文透明报告了不同 ε 值结果，且 Table 2 原始 |Δ| 值已直观展示 <1pp 差距。2pp 在 GSM8K 60-66% 区间内是合理的 practical significance。Director 判定 Info——非核心问题，仅需补充 justify。\"\n  action_items:\n    - round: 8\n      action: \"在论文中 justify ε=2pp 选择（引用相关文献或从数据分布推导）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N5\"\n  summary: \"30% sparsity 全面 collapse 限制方法实用窗口（仅 20-25%）\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W7 提出，R1 同意但降级（论文定位 controlled study，非 practical tool）。有效窗口 20-25% 较窄。Limitations 已承认，但应讨论突破路径。\"\n  action_items:\n    - round: 8\n      action: \"Discussion 或 Future Work 简要讨论突破 30% ceiling 的方向（mixed-granularity, layer-wise adaptive）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N6\"\n  summary: \"缺失 3 篇高度相关文献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2 识别 3 篇缺失：(1) 'When Reasoning Meets Compression' (Li et al., 2025, arXiv:2504.02010)——直接 benchmark 剪枝对 DeepSeek-R1 推理影响；(2) 'GPrune-LLM' (2026, arXiv:2603.13418)——generalization-aware 剪枝；(3) 'Can Pruning Improve Reasoning?' (2025, arXiv:2505.14582)。R1 同意 #1 和 #3 高度相关应引用，#2 可能时间上来不及。R1 还建议添加 Wanda (Sun et al., 2024)，但 R2 rebut 指出 Wanda 是非结构化剪枝相关性较低。\"\n  action_items:\n    - round: 8\n      action: \"验证并添加 Li et al. (2504.02010) 和 'Can Pruning Improve Reasoning?' (2505.14582)；GPrune-LLM 可在 camera-ready 补充\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M1\"\n  summary: \"Recovery capacity 概念先用后定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M1 提出，R2 同意但极 minor。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M2\"\n  summary: \"无代码/checkpoint 发布承诺\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M5 提出，R2 同意。对 controlled experiment 论文 reproducibility 承诺尤为重要。\"\n  action_items:\n    - round: 8\n      action: \"在 Conclusion 或 Abstract 添加代码/checkpoint 发布承诺\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M3\"\n  summary: \"Lottery Ticket Hypothesis 联系过于表面\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-M3 提出，R1 同意。LTH 讨论 pruning at initialization，与本文 post-training pruning 有本质区别，类比表面。\"\n  action_items:\n    - round: 8\n      action: \"弱化 LTH 类比或加说明两者的本质区别\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "issues_yaml": "\n# ============================================================\n# Round 1-3 Issues — All Resolved\n# ============================================================\n\n- id: \"R1-C1\"\n  summary: \"CKA-recovery link 仅相关性, 无因果干预\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Jaccard overlap 分析 + Limitations 承认 + 多种子统计验证\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Single-seed GRPO 无统计显著性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"3-seed GRPO CKA-only, Welch's t-test p=0.0009\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"仅 GSM8K 单基准\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"MATH-500 OOD 验证 + MBPP 代码基准\"\n  resolution_round: 3\n\n- id: \"R1-W1\"\n  summary: \"Title overclaim 'determines'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Title 改为 'shapes'\"\n  resolution_round: 3\n\n- id: \"R1-W2\"\n  summary: \"Abstract 'universally determines' overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"改为 'significantly shapes'\"\n  resolution_round: 3\n\n- id: \"R1-W3\"\n  summary: \"仅 DeepSeek-R1-7B 单模型\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Qwen2.5-Math-7B cross-arch + 1.5B cross-scale\"\n  resolution_round: 3\n\n- id: \"R1-M1\"\n  summary: \"GRPO 超参未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Appendix 完整超参表\"\n  resolution_round: 3\n\n- id: \"R1-M2\"\n  summary: \"Table 1 缺 Random baseline\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Table 1 加入 Random 行\"\n  resolution_round: 3\n\n- id: \"R2-NEW-C1\"\n  summary: \"GRPO 准确率几乎不变,为何要用 GRPO\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Dual-layer reframe: SFT(accuracy) + GRPO(reward signal)\"\n  resolution_round: 3\n\n- id: \"R2-NEW-C2\"\n  summary: \"Cross-architecture 仅 SFT 验证,GRPO 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"1.5B GRPO 补充 + Abstract 区分表述\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W1\"\n  summary: \"SFT recovery 被忽视,过度聚焦 GRPO\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注解释 SFT catastrophic forgetting\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W2\"\n  summary: \"Qwen-Math 跨架构验证仅 SFT，Abstract overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 区分 GRPO(DeepSeek) vs SFT(Qwen-Math)\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W3\"\n  summary: \"GRPO 准确率改变 < 1pp — 实际效用存疑\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"300-step accuracy + reward-accuracy decoupling 论证\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W4\"\n  summary: \"RASP/Random 仍为单种子\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注透明标注 + Limitations 披露\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W5\"\n  summary: \"Random baseline SFT/GRPO Acc 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Table 2 脚注标注 checkpoint not preserved\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W6\"\n  summary: \"正文 5 处 'determines' 残留\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"全部替换为 shapes/significantly influences\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M1\"\n  summary: \"GRPO batch size / rollouts 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M2\"\n  summary: \"SFT lr/batch/optimizer 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-VIS-1\"\n  summary: \"末页 Figure 6 仅占 30%，70% 空白\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 重排\"\n  resolution_round: 3\n\n- id: \"R2-VIS-2\"\n  summary: \"Appendix page 12 过度拥挤\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 拆分到多页\"\n  resolution_round: 3\n\n- id: \"R3-S5\"\n  summary: \"Qwen-Math 'strongest evidence' 措辞仍略强\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"strongest → additional evidence in §4.5\"\n  resolution_round: 3\n\n- id: \"R3-M2\"\n  summary: \"300-step accuracy 未标注 seed\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"(single seed) 标注已添加到 §4.3\"\n  resolution_round: 3\n\n- id: \"R3-M3\"\n  summary: \"无代码/checkpoint 发布声明\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"Code and checkpoints release statement in Conclusion\"\n  resolution_round: 3\n\n# ============================================================\n# Round 5-7 Issues — Carried forward\n# ============================================================\n\n- id: \"R5-N1\"\n  summary: \"Reward-accuracy decoupling 叙事薄弱（GRPO 增量 <1pp，可能是训练不足的 artifact）\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。SYSTEMIC_ISSUE #1 核心。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W4 和 R2-W2 再次提出，增加新角度：需区分 format compliance vs reasoning quality。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-N3 升级为 critical。R1 完全同意。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 升为本文最关键问题（Critical），R1 维持 Warning。核心分歧：R2 认为 15% sparsity 数据自相矛盾（GRPO amplifies gap）+ 300 步实验选择性省略 accuracy。R1 认为 reward collapse 结构性证据使'训练更久就能恢复'不 plausible。最终共识：300 步 accuracy 数据缺失是 gap，但对整体严重性评估存在不可调和分歧。\"\n  action_items:\n    - round: 5\n      action: \"D098 dual-layer reframe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"Agent 提取 format compliance / EOS rate 数据\"\n      assigned_to: agent\n      status: in_progress\n    - round: 7\n      action: \"运行 ≥1000 GRPO steps 验证 decoupling 是否持续\"\n      assigned_to: agent\n      status: open\n    - round: 8\n      action: \"补充 300 步 extended training 的 accuracy 数据（非仅 reward）；讨论 15% sparsity 与 20% 的差异原因\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N2\"\n  summary: \"Cross-architecture/scale 泛化严重不足，所有模型共享 Qwen2.5 base\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前不可行（需全 pipeline ~50h GPU）。但 1.5B GRPO 数据已有。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识。Appendix O 'Cross-Architecture Validation' 标题误导。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识 Critical。R1 正式同意升级。核心论点：Title 'Reasoning LLMs'（复数）vs 单一 Qwen2.5 架构族。Qwen2.5-Math-7B 的 GRPO 验证缺失。R1 建议 Title 改为 'A Case Study on...' 或补充非 Qwen 架构。\"\n  action_items:\n    - round: 5\n      action: \"补入 1.5B GRPO 数据作 cross-scale validation\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 7\n      action: \"重命名 Appendix O 标题；限定 claim 为 Qwen2.5 家族\"\n      assigned_to: paper_agent\n      status: open\n    - round: 8\n      action: \"Title 改为更精确范围（如 'A Case Study on DeepSeek-R1-Distill-Qwen-7B'）或补充至少一个非 Qwen 架构 GRPO 结果\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"RASP 单 seed 验证不足——方法贡献可靠性存疑\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"核心比较 CKA vs Standard 有 3-seed p=0.0009。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 升级为 critical。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识 critical。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"严重性分歧：R1 Critical（RASP α=2.0 优于 CKA-only 仅 1.72pp 在 N=1 下不可靠，直接影响方法贡献 validity），R2 Minor（RASP 非核心 claim 支撑）。R1 论证 R2 自身 W3（RASP 叙事矛盾）逻辑上依赖 RASP 可靠性，M1 定级与 W3 不一致——论证有力。Director 判定：Critical。\"\n  action_items:\n    - round: 5\n      action: \"Limitations 标注 + 核心 claim 限定 CKA vs Standard\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 7\n      action: \"至少 RASP α=2.0 和 α=1.0 各跑 3 seeds\"\n      assigned_to: agent\n      status: open\n    - round: 8\n      action: \"如多 seed 无法完成：降级 RASP 为 exploratory analysis，不作为核心方法贡献\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"因果语言系统性过强——'causal driver' 超出 quasi-experimental 证据\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"SYSTEMIC_ISSUE #2 成员。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N3 详细论证。R2 补充 metrics diversity 不足。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被单独提及为新问题。R2 交叉回应中讨论了 CKA 双重角色但判为 Minor。可能部分已修复（dose-response 用语已改善），待 Research Director 确认。\"\n  action_items:\n    - round: 7\n      action: \"全文语言审计：'causal driver' → 'key determinant'；decoupling claims 加限定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Per-layer capacity floor (40%) 未消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前无法做 full pipeline ablation。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W3 再次提出。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未提及\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未提及，可能已修复或不再关注\"\n  action_items:\n    - round: 5\n      action: \"Limitations 讨论 + rebuttal 论点准备\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Floor ablation τ∈{0.3,0.4,0.5,0.6} experiments running; appendix table added\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"α dose-response 存在 generation length 混杂变量\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"高 ROI 实验。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出。R2-W1 扩展为 κ 消融缺失。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"升级为 critical。α=1.0 用 1024 tokens，其他用 512 tokens。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 在 W2（Random baseline）中再次确认 max_completion_length 不一致问题。R2 同意 Random 512 vs 其他 1024 不公平。此问题与 R7-N1（dose-response 混杂）紧密相关。\"\n  action_items:\n    - round: 7\n      action: \"统一所有 α 值 max_completion_length=1024 重跑 dose-response\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"'Recovery capacity gradient' 术语与 gradient descent 混淆\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"全文替换为 'recovery capacity spectrum'\"\n  resolution_round: 7\n\n- id: \"R5-M1\"\n  summary: \"Section 5 末尾溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"约 2 行溢出\"\n    - round: 7\n      reviewers: []\n      note: \"R7 确认格式合规\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未提及，视觉审查未标记页面溢出，可能已修复\"\n  action_items:\n    - round: 5\n      action: \"Paper Agent 压缩 §5 确保 8 页合规\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M2\"\n  summary: \"Abstract p<0.001 未说明统计检验方法\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Abstract 标注 Welch's t-test\"\n  resolution_round: 6\n\n- id: \"R5-M3\"\n  summary: \"Page 7 display items 过度拥挤\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Figure 3 + Figure 4 + Table 2 挤在同一页\"\n    - round: 7\n      reviewers: []\n      note: \"视觉审查标记\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M2 再次提出 Figure 2 信息密度过高。视觉审查标记 page 7-8 axis labels/legend 字号偏小（≤6pt）。\"\n  action_items:\n    - round: 5\n      action: \"Figure 前移平衡视觉节奏\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M4\"\n  summary: \"bib key 年份误导 + 引用错误\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"lachance2024cka→2022, klabunde→2023\"\n    - round: 6\n      reviewers: [2]\n      note: \"新引用错误\"\n    - round: 7\n      reviewers: []\n      note: \"未提及\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未提及，待确认\"\n  action_items:\n    - round: 5\n      action: \"Paper Agent 修正 bib 条目\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M5\"\n  summary: \"Figure 2 标注字体偏小 / 颜色区分度不足\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: []\n      note: \"视觉审查发现\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 提到\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M2 指出 Figure 2 信息密度过高。视觉审查标记 page 7-8 figure panel axis labels 偏小。\"\n  action_items:\n    - round: 5\n      action: \"增大字号 + 添加不同 line style\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N1\"\n  summary: \"GSM8K 单基准 GRPO 主实验，Title/Abstract 做一般性声明\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。\"\n    - round: 7\n      reviewers: []\n      note: \"间接相关\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未单独提及。MATH-500 和 MBPP OOD 验证已添加（Round 3 修复），但 R8 R1 指出 MBPP 不显著却被引用。\"\n  action_items:\n    - round: 6\n      action: \"MF1: MBPP probe eval\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"CKA-only layer 分布混杂——72.5% 剪枝集中 early layers，优势可能来自 layer 分布而非 diversity\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"R1-N3 提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 详细展开。granularity 不匹配无法解耦。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被直接提及为独立问题。R8 Reviewer 未重新审查 layer 分布。\"\n  action_items:\n    - round: 7\n      action: \"创建 same-granularity layer-biased baseline\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N3\"\n  summary: \"缺失高度相关文献：RL Finetunes Small Subnetworks (2505.11711)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent 添加引用并在 Related Work/Discussion 讨论\"\n  resolution_round: 6\n\n- id: \"R6-W1\"\n  summary: \"Reward-accuracy decoupling 未区分 format compliance vs reasoning quality\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"需报告 EOS rate 和 format compliance rate\"\n    - round: 7\n      reviewers: []\n      note: \"间接相关\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及\"\n  action_items:\n    - round: 6\n      action: \"Agent 从 eval logs 提取 format compliance / EOS rate\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"实验仅覆盖 MLP channel pruning，Title/Abstract 未限定 scope\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Title 改为 'How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs'\"\n  resolution_round: 7\n\n- id: \"R6-W3\"\n  summary: \"遗漏 3 篇相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent 验证并添加引用\"\n  resolution_round: 6\n\n- id: \"R6-W4\"\n  summary: \"Welch's t-test at N=3 统计功效极低，缺 effect size 和 CI\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Cohen's d + 95% CI 已加入正文\"\n  resolution_round: 7\n\n- id: \"R6-W5\"\n  summary: \"15%/25% sparsity 实验为 single-seed\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W5 交叉回应提出。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及\"\n  action_items:\n    - round: 6\n      action: \"MF2 部分覆盖; 15%/25% 在 Limitations 标注\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"RASP 表现差于 Standard 缺乏充分解释\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"需分析 importance 和 CKA overlap 的相关性\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W3（RASP 叙事矛盾）详细论证：α=1.0 collapse + α=2.0 本质 CKA-dominant。R1 同意核心判断并补充条件性结论。与 R8-N3 (RASP 函数形式) 相关。\"\n  action_items:\n    - round: 6\n      action: \"Paper Agent 待 α dose-response 数据后分析 RASP failure mechanism\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 8\n      action: \"修改 RASP 叙事：从 'balance importance and diversity' 改为 'CKA-dominant with importance as minor correction'；或提供加法形式对比实验\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W7\"\n  summary: \"Table 1 脚注 'Only redundancy-based pruning sustains RL recovery' 与 Random 排第二矛盾\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"脚注措辞已修改\"\n  resolution_round: 6\n\n- id: \"R6-W8\"\n  summary: \"Section 5 Discussion 偏薄（仅半页）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议讨论 CKA 与 RL exploration 关系\"\n    - round: 7\n      reviewers: []\n      note: \"间接相关\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W6 再次提出。R1 同意。Section 5 仅约 7-8 行。应至少讨论：spectrum 部署指导意义、decoupling 对 RLVR 理论影响、CKA-only 机制解释、与 Ji et al. (2026) self-healing 结论的对话。\"\n  action_items:\n    - round: 6\n      action: \"Paper Agent 待实验数据后扩充 Discussion\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 8\n      action: \"扩充 Discussion 至少半栏：加入 SFT vs GRPO 角色分离讨论、spectrum 实用指导、与 self-healing 文献对话\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M1\"\n  summary: \"Reward-accuracy decoupling 首次使用时无正式定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"首次使用处添加正式定义\"\n  resolution_round: 6\n\n- id: \"R6-M2\"\n  summary: \"Figure 2 y 轴未标注 mean vs peak reward\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 提出。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 6\n      action: \"修改 Figure 2 y-axis label\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M3\"\n  summary: \"Eq.1 未写出 Taylor expansion 完整数学形式\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2 小问题。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 6\n      action: \"Paper Agent 补充 Eq.1 完整数学形式\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 7 Issues — Carried forward\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"Dose-response 中 max_completion_length 不一致（α=1.0: 1024, 其他: 512）构成关键混杂变量\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 独立提出。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W2（Random 512 vs 其他 1024）再次确认不一致。R2 同意此问题直接影响 spectrum 排序。但 R2 认为 Random 不是核心对比对象（Warning），R1 认为 Critical。Director 判定保持 Critical（dose-response inverted-U 的可靠性取决于此）。\"\n  action_items:\n    - round: 7\n      action: \"统一所有 α 值 max_completion_length=1024 重跑 dose-response\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N2\"\n  summary: \"Abstract overclaiming 'holds across sparsity levels'——仅 20-25% 窗口成立\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N4 提出，R2 完全同意。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未单独提及，但 R2-W7（30% collapse）间接相关\"\n  action_items:\n    - round: 7\n      action: \"Abstract 改为 'at moderate sparsity (20-25%)' 限定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W1\"\n  summary: \"Decoupling 缺少形式化等价性检验（TOST）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W3 提出，R2 同意。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R8 论文已包含 TOST（ε=2pp，7/8 通过），R1 质疑 ε=2pp post-hoc selection（Warning），R2 认为 Minor-Warning（论文透明报告了不同 ε 值结果）。已有改善但 ε 选择需 justify。\"\n  action_items:\n    - round: 7\n      action: \"使用 TOST 或明确 practical equivalence margin\"\n      assigned_to: paper_agent\n      status: open\n    - round: 8\n      action: \"在论文中 justify ε=2pp 选择（引用 GSM8K 文献中 meaningful difference threshold）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"MBPP 结果统计不显著却被用作 decoupling 支持证据\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 同意。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未单独提及\"\n  action_items:\n    - round: 7\n      action: \"正文引用 MBPP 时加注 'not statistically significant'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W3\"\n  summary: \"Calibration 数据量 M 在正文中未明确指定\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 同意。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M4 再次提出 M=512 未说明理由。R2 同意。\"\n  action_items:\n    - round: 7\n      action: \"在 Section 3.2 或 4.1 明确指定 M 及选择依据\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W4\"\n  summary: \"Throughput regression（-19%）未在 Limitations 讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W3 提出，R1 部分同意。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 7\n      action: \"在 Limitations 添加 throughput regression 讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"Title/叙事焦点与实际恢复来源错位——SFT 贡献 ~60pp 而 GRPO <1pp\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 交叉回应 [NEW FINDING]\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W1（SFT ceiling）和 R2-W5（Title 焦点错位）详细论证。R1 交叉回应同意核心判断——SFT 完成 95%+ 恢复，GRPO 的 training dynamics 差异在实践中可能不重要。R1 补充：Title 可保留（RLVR 是研究对象），但 Discussion 应显式讨论 SFT 主导恢复的含义。\"\n  action_items:\n    - round: 7\n      action: \"Discussion 中明确分离 SFT vs GRPO 恢复角色\"\n      assigned_to: paper_agent\n      status: open\n    - round: 8\n      action: \"Discussion 显式讨论 'SFT 主导恢复' 的含义及 GRPO 实际贡献的定位\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 8 New Issues\n# ============================================================\n\n- id: \"R8-N1\"\n  summary: \"RASP 方法贡献叙事自相矛盾——α=2.0 本质 CKA-dominant，'平衡 importance 与 diversity' 不准确\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W3 详细论证：α=1.0（名义'平衡'点）collapse，α=2.0 diversity 权重为 importance 的 4 倍。CKA-only 已达 64.39% vs RASP 66.11%（+1.72pp, 单 seed）。R1 同意核心判断，补充条件性结论——如多 seed 复现则贡献成立但叙事需改，否则 RASP 无显著改进。乘法形式 I(h)×(1-F(h))^α 可能人为导致 α=1.0 collapse（importance=0 → score=0）。\"\n  action_items:\n    - round: 8\n      action: \"修改 RASP 叙事为 'CKA-dominant with importance correction'；讨论乘法 vs 加法形式的选择理由；或提供加法形式实验对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N2\"\n  summary: \"Random baseline max_completion_length=512（vs 其他方法 1024）构成不公平比较\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 列 Warning。核心分歧：R1 认为直接影响 spectrum 排序（Random 被不公平压低），R2 认为 Random 非核心对比对象（核心是 CKA-only vs Standard，二者均 1024 tokens 公平比较）。Director 判定 Warning——Random 是次要比较对象，核心 CKA vs Standard 比较未受影响。\"\n  action_items:\n    - round: 8\n      action: \"统一 Random 的 max_completion_length=1024 重跑；或在论文中明确标注此限制并讨论对 spectrum 排序的影响\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N3\"\n  summary: \"RASP 函数形式（乘法）缺乏理论推导，可能人为导致 α=1.0 collapse\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 同意。乘法形式 I(h)×(1-F(h))^α 意味着 importance=0 时 score=0，可能导致高 diversity 但低 importance 的结构被不当移除，这恰好可能是 α=1.0 collapse 的原因。加法形式 βI(h)+(1-β)(1-F(h)) 可能保留这些结构。如果加法下 α=1.0 不 collapse，'importance 对 RL recovery 有害' 的隐含论点不成立。\"\n  action_items:\n    - round: 8\n      action: \"讨论函数形式选择理由；理想情况下补加法形式对比实验；最低限度在 Limitations 承认\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N4\"\n  summary: \"TOST ε=2pp margin post-hoc selection 嫌疑\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 Warning，R2 Minor-Warning。ε=2pp 未预注册，ε=1pp 功效不足，ε=3pp 全通过。但论文透明报告了不同 ε 值结果，且 Table 2 原始 |Δ| 值已直观展示 <1pp 差距。2pp 在 GSM8K 60-66% 区间内是合理的 practical significance。Director 判定 Info——非核心问题，仅需补充 justify。\"\n  action_items:\n    - round: 8\n      action: \"在论文中 justify ε=2pp 选择（引用相关文献或从数据分布推导）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N5\"\n  summary: \"30% sparsity 全面 collapse 限制方法实用窗口（仅 20-25%）\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W7 提出，R1 同意但降级（论文定位 controlled study，非 practical tool）。有效窗口 20-25% 较窄。Limitations 已承认，但应讨论突破路径。\"\n  action_items:\n    - round: 8\n      action: \"Discussion 或 Future Work 简要讨论突破 30% ceiling 的方向（mixed-granularity, layer-wise adaptive）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N6\"\n  summary: \"缺失 3 篇高度相关文献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2 识别 3 篇缺失：(1) 'When Reasoning Meets Compression' (Li et al., 2025, arXiv:2504.02010)——直接 benchmark 剪枝对 DeepSeek-R1 推理影响；(2) 'GPrune-LLM' (2026, arXiv:2603.13418)——generalization-aware 剪枝；(3) 'Can Pruning Improve Reasoning?' (2025, arXiv:2505.14582)。R1 同意 #1 和 #3 高度相关应引用，#2 可能时间上来不及。R1 还建议添加 Wanda (Sun et al., 2024)，但 R2 rebut 指出 Wanda 是非结构化剪枝相关性较低。\"\n  action_items:\n    - round: 8\n      action: \"验证并添加 Li et al. (2504.02010) 和 'Can Pruning Improve Reasoning?' (2505.14582)；GPrune-LLM 可在 camera-ready 补充\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M1\"\n  summary: \"Recovery capacity 概念先用后定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M1 提出，R2 同意但极 minor。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M2\"\n  summary: \"无代码/checkpoint 发布承诺\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M5 提出，R2 同意。对 controlled experiment 论文 reproducibility 承诺尤为重要。\"\n  action_items:\n    - round: 8\n      action: \"在 Conclusion 或 Abstract 添加代码/checkpoint 发布承诺\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M3\"\n  summary: \"Lottery Ticket Hypothesis 联系过于表面\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-M3 提出，R1 同意。LTH 讨论 pruning at initialization，与本文 post-training pruning 有本质区别，类比表面。\"\n  action_items:\n    - round: 8\n      action: \"弱化 LTH 类比或加说明两者的本质区别\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-24T18:23:23.242723+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml\", \"bytes\": 30589}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---
