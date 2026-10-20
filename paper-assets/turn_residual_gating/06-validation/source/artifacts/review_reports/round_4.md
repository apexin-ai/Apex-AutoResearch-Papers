---
round: 4
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-25T05:56:02.268630+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 4

**Paper**: Turn-Residual Gating for Multi-Turn Dialogue (working title)
**Venue**: EMNLP 2026 (ARR submission)
**Reviewers**: R1 (方法严谨性/实验设计), R2 (新颖性/写作质量)
**Cross-response convergence**: 高度收敛。R2 对 R1 几乎全部 [AGREE]，唯一 [REBUT] 为 W4（多重比较），且仅部分成立。

---

## Summary

本文研究多轮对话中辅助注意力损失（auxiliary attention loss）在自回归推理时的效能退化问题。作者提出 Goal Attention Ratio（GAR）指标量化注意力衰减，设计 ThreadGate（基于对话轮次的残差门控）和 Scheduled Sampling（SS）两种缓解方案，在 Qwen2.5-3B + LoRA 上进行五路对比实验（Base, PCGrad, Uniform Gate, ThreadGate, ThreadGate+SS）。核心发现：所有 teacher-forcing 训练的变体在自回归推理时 GAR 均大幅退化（20-33× gap），Scheduled Sampling 是唯一有效压缩该 gap 的方案，ThreadGate 本身贡献边际。论文将此归因于 exposure bias。Llama-3.1-8B 上做了部分跨模型验证（3/5 条件）。

论文提出了一个有意义的研究问题，实验设计在消融维度上较为完整，SS 的实用发现有价值。但核心指标（GAR）的 construct validity 严重不足（r²=0.04），统计支撑薄弱（多条件单 seed，SS 跨 seed 方差 31%），因果声明超出证据范围，下游任务评估完全缺失。

---

## Strengths

**S1. 重要且未被充分研究的问题。** 多轮对话中辅助注意力损失在推理时失效是一个实际且重要的现象。现有文献对此的系统性量化几乎空白。论文正确识别了这个 gap 并试图填补。

**S2. 系统性五路消融设计。** Base / PCGrad / Uniform Gate / ThreadGate / ThreadGate+SS 的五路对比在方法维度上覆盖了主要假设（梯度冲突、架构设计、训练策略），结构化程度高于该领域多数工作。

**S3. Scheduled Sampling 的实用发现。** SS 显著压缩 TF-AR gap（从 20-33× 降至 ~1.3×）且无推理成本，这一发现对该领域的实践者有直接参考价值。

**S4. 详尽的 Appendix 和可追溯性。** 论文提供了大量补充材料（v1-v7 loss 迭代历史、per-turn 动态、gradient statistics、per-seed 结果），展现了研究过程的透明性。

**S5. β-steering 作为轻量推理时干预。** 无需重训练即可调控注意力分布的方案，有工程实用价值。跨模型（Qwen β=3, Llama β≥5）差异也提供了有价值的 negative signal。

---

## Weaknesses

### Critical（必须修复，否则影响接收）

**C1. GAR 指标的 construct validity 严重不足。** [R1-N1, R2-N1, 交叉一致]
- GAR 与下游指令保持率的相关性 r=0.200, r²=0.04。全文从标题到结论以 GAR 改善为核心叙事，但 GAR 仅解释 4% 的下游方差。
- N=54 paired samples 下 95% CI ≈ [0.05, 0.35]，置信区间过宽。
- β=10 时 PPL 退化至 4.22，表明 GAR 极端提升可能有害，进一步质疑其作为优化目标的合理性。
- 所有 variants PPL ≈ 2.78, AUC ≈ 0.98——GAR 的巨大差异未映射到任何下游性能差异。
- **缺少任何标准多轮对话基准评测**（MT-Bench、AlpacaEval 等）。论文的全部评估建立在 GAR 这个未经外部验证的内部指标上。
- **建议**：补充 MT-Bench 等下游评测（≥100 对话人工评估），或将 GAR 重新定位为 diagnostic probe 而非优化目标/成功指标。

**C2. 单 seed 消融 + SS 跨 seed 方差 31%。** [R1-N2, R1-W5, R2 交叉一致]
- Table 1 中 Base, PCGrad, Uniform Gate 三个重要条件**仅有 seed=42 单次结果**。ThreadGate 有 2 seeds，SS 有 2 seeds 但策略不同不可直接比较。
- SS 两 seed AR GAR: 0.318 vs 0.418（相差 31%），说明 between-run variance 极高。Abstract 以确定性语气呈现这些结果（"compresses the gap to 1.29×"）构成 overclaim。
- Appendix T 的 3-seed 验证仅覆盖 ThreadGate（CoV=9%），不能替代全条件多 seed 验证。
- Table 6 Wilcoxon signed-rank test 以 conversation 为单元（N=50），衡量 within-run variability，无法支撑 between-run 对比结论。
- **建议**：全部 5 条件 × 3 seeds 完整实验，报告 mean±std。当前单 seed 数据仅能作为 pilot study。

**C3. Exposure bias 因果归因超出证据。** [R2-C3, R1-W3, 交叉一致]
- 论文将 TF-AR gap 归因于 exposure bias，但未实验排除 KV cache drift 假说（§6 承认，§8 留给 future work）。
- PCGrad 失败被用作 modus tollens 否定 gradient conflict 假说，但 PCGrad 的投影操作本身引入副作用（NTP magnitude 增长 7.5×-14.7×），失败可能反映投影副作用而非 gradient conflict 不存在。
- Appendix L 的 gradient statistics 在 PCGrad 条件下获得，不构成独立验证。
- 对一篇以 "mechanistic/diagnostic analysis" 自居的论文，留下核心因果链的最关键环节未验证是不可接受的。
- **建议**：设计 TF→AR 切换实验区分 prefix-level exposure bias 和 cache-level drift；或大幅弱化因果声称。

### Should-Fix（应修复，影响评分但不单独构成拒稿理由）

**W1. SS+LoRA-only 关键消融缺失。** [R1-W1, R2 交叉一致]
- TG AR GAR ≈ 0.047（相比 Base ~2.6× 改善），SS AR GAR ≈ 0.401（相比 TG ~8.5× 改善）。SS 是压缩 TF-AR gap 的主要贡献者。
- 缺少 SS+LoRA-only（不加 ThreadGate）的消融。如果该配置效果相似，ThreadGate 作为架构贡献的价值将大幅降低。
- §6 未直面 ThreadGate vs SS 的贡献归因问题。

**W2. 单一数据集（UltraChat）。** [R1-W5, R2-W2, 交叉一致]
- 所有实验仅在 UltraChat 上进行，无法评估 GAR decay 是否为 UltraChat 特异现象。
- 缺少 ShareGPT、LMSYS-Chat-1M 等替代数据集验证。

**W3. Llama 跨模型验证不完整。** [R1-W1, R2-M2, 交叉一致]
- 仅 3/5 条件（Base, TG, TG+SS），缺 PCGrad 和 Uniform Gate。
- Median vs mean 切换在 Qwen→Llama 间不一致，有 metric selection 之嫌。
- §5.5 标题 "Cross-Model Validation" 过度概括，建议改为 "Cross-Model Replication"。

**W4. 标题与副标题 overclaim。** [R2-N2, R1-W2, 交叉一致]
- 标题暗示 gating 固有失败，但实际发现是 exposure bias 的通用问题（LoRA-only 无 gate 表现相同）。
- "Mechanistic Analysis" 副标题与分析深度不匹配——宏观层面非 circuit-level。建议改为 "Diagnostic Analysis"。

**W5. Li et al. split-softmax / Rhea 缺实验对比。** [R2-W7-new, R2-W2]
- 论文声称 split-softmax "cannot address exposure bias" 但未实验验证。
- 作为最直接竞争方法，至少需要理论论证或承认未验证。

**W6. Appendix C instruction retention 多重比较未校正。** [R1-W4, R2 部分反驳]
- 主实验已有 Holm-Bonferroni 校正（Appendix E p30），此关切对主实验不成立。
- 但 Appendix C 18-category McNemar's test 未做 FDR/Bonferroni 校正。

**W7. 写作冗余。** [R2-W4-new]
- '20-33× gap' 至少出现 7 次，'0.064 to 0.727' 出现 4+ 次。

### Minor

**M1.** r_min 数值正文未报告，影响可复现性。[R1-M1]
**M2.** GAR-D 全条件接近零（ThreadGate TF下仅0.02），说明干预仅在 τ-masked last token 成功，泛化性未讨论。[R1-W5]
**M3.** Table 1 四舍五入与正文数字精度不一致（0.75pp vs 1pp）。[R2-W6]
**M4.** LoRA rank=16 是否影响结论未讨论。[R2-Q4]
**M5.** 无代码/数据发布承诺。[R1-M6, R2-M6]
**M6.** Bib 格式：Raposo et al. 2024 应更新为 ICML 2024 @inproceedings；Gromov et al. 年份一致性。[R2-M3]

---

## Questions

**Q1.** SS+LoRA-only（不加 ThreadGate）的 TF-AR gap 是多少？如果与 SS+ThreadGate 相似，ThreadGate 的独立贡献是什么？[R1, R2 一致]

**Q2.** Table 1 中 Base, PCGrad, Uniform Gate 是否均为 seed=42？请明确标注。[R1]

**Q3.** 如果 GAR 与下游任务的 r²=0.04，作者是否考虑 GAR 可能不是指令遵循的可靠代理指标？将 GAR 重新定位为 diagnostic probe 而非优化目标是否更准确？[R1, R2 一致]

**Q4.** β-steering 最优 β 的 architecture dependence（Qwen β=3 vs Llama β≥5）意味着什么？该方法是否需要 per-model tuning？[R1, R2 一致]

**Q5.** 其他数据集（ShareGPT, LMSYS-Chat-1M）上 GAR decay 是否一致？[R1, R2 一致]

**Q6.** 是否尝试过更高 LoRA rank（32, 64）？rank=16 下的结论是否因 capacity saturation 被低估？[R2]

---

## Missing References

1. **Zhang et al. 2024** — "Tell Your Model Where to Attend"：与 β-steering 思路相似的推理时注意力操控方法，应在 §2 讨论。[R2]
2. **Rhea (arXiv:2512.06869)** — Role-aware Heuristic Episodic Attention：§2 已讨论但缺实验对比。[R1, R2 跨轮追踪]
3. **Li et al. 2024** — Split-softmax：最直接竞争方法，需加强理论对比。[R2]

---

## External Review

**状态**：已跳过（skipped at 2026-05-25T05:44:29）。未获得外部审稿数据。

---

## Visual Layout Check（非评分项）

**状态**：已完成 (0 critical, 3 warning, 6 info)

**Warning:**
- Page 6: Figure 4（Scheduled sampling compression）尺寸偏小，柱状图条形窄、标签字号小
- Page 8: Figure 6a（per-layer gate values）28 层数据压缩在单栏宽度内，个别柱体 <2px，建议改用折线图或全宽
- Pages 5/7/8: 多个 bar chart 使用高饱和度配色（亮橙+亮蓝+亮绿），与用户规则"配色饱和度对比别太高"不符

**Info:**
- Page 1: 首页无 display item，Figure 1 在 Page 2
- Page 2: Figure 1 caption ~7 行，偏密集
- Page 7: Figure 5 仅两根柱子，信息密度低
- Page 30: Appendix 整页纯文本（可接受）
- Pages 25-26: Tables 19-22 列数多但字号可辨
- Pages 16/18/19: Appendix 图表 axis label 约正文 60-65%

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Overall | 3.0 (Findings) | 3.5→3.0 (Findings) | **3.0 (Findings)** |
| Soundness | 3/5 | 3/5 | 3/5 |
| Novelty | 2/5 | 2.5/5 | 2/5 |
| Reproducibility | 3/5 | 4/5 | 3/5 |

### 综合评价

**Overall Score: 3.0 — Findings**

论文识别了一个重要且未被充分研究的问题（多轮对话辅助注意力损失在 AR 推理时的效能退化），五路消融设计系统性较好，SS 的实用发现有直接价值。

然而，三个 Critical 问题共同构成了接收的主要障碍：

1. **GAR construct validity**（r²=0.04）——全文核心叙事建立在一个仅解释 4% 下游方差的指标上，且无任何标准多轮对话基准评测。这不是精度问题，而是整个评估框架的根基问题。

2. **统计不可靠**——多条件单 seed，SS 跨 seed 方差 31%，AR 评估 N=5。当前数据本质上是 pilot study 级别，不足以支撑论文的定量结论。

3. **因果 overclaiming**——exposure bias 归因未排除 KV cache drift，PCGrad modus tollens 论证依赖过强假设。"Mechanistic analysis" 的定位与实际分析深度不匹配。

R2 指出论文的**诊断框架和问题发现**本身有独立价值，即使方法贡献是增量的。如果 GAR 被重新定位为 diagnostic probe（而非优化目标），因果声称被大幅弱化，统计问题被修复（全条件 3-seed + N≥50 AR 评估），论文可达到 Findings 水准。当前状态距此仍有实质性 gap。

### 修改优先级

1. **[实验]** 全条件 3-seed × N≥50 AR 评估 + mean±std → 解决 C2
2. **[实验]** SS+LoRA-only 消融 → 解决 W1
3. **[评估]** MT-Bench 或等价下游评测 → 部分解决 C1
4. **[写作]** GAR 重新定位为 diagnostic probe + 因果声称弱化 → 部分解决 C1, C3
5. **[写作]** 标题/副标题调整 → 解决 W4
6. **[实验]** 第二数据集验证 → 解决 W2

---

## Detailed Comments

### 交叉回应分歧记录

仅一项分歧，已在报告中体现：

- **R1-W4（多重比较）**：R2 部分反驳——主实验已有 Holm-Bonferroni 校正（Appendix E p30），R1 关切对主实验不成立。但对 Appendix C 18-category McNemar's test 成立。报告中记录为 W6（Should-Fix，限定于 Appendix C）。

### 评分调整说明

R2 初始评分 3.5（Borderline Conference），交叉回应后表示"如果 GAR 的 construct validity 问题（r²=0.04）得不到解决，愿意将评分下调至 3.0"。鉴于 C1 目前未解决，R2 有效评分调整为 3.0。两位 Reviewer 共识为 3.0（Findings）。

### 跨轮次追踪

本轮为 Round 4（fresh re-review）。Issue tracker 中有 5 个 Critical 级别未解决问题（R1-N2, R1-W5, R2-C3, R4-N1, R2-N3），12 个 Warning 级别未解决问题，6 个 Info 级别未解决问题。详见 `artifacts/review_issues.yaml`。
