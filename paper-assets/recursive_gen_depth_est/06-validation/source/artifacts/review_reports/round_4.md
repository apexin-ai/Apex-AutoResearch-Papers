---
round: 4
overall_score: weak accept / findings
timestamp: 2026-05-16T17:34:50.481868+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 5

**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
**Venue**: EMNLP 2026 Main Conference (ARR May cycle)
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + Related Work)
**日期**: 2026-05-16

---

## Summary

本文将 recursive generation depth estimation 形式化为 ordinal classification，构建 180K 样本 benchmark (3 model families × 3 decoding strategies × 4 depths)，发现 perplexity tail statistics（p90_ppl, var_surprisal）在 9/9 配置中稳定主导深度判别。提出 EDD metric 量化可区分深度前沿 (EDD₀.₇₅=4, Pythia, p=0.001)。在 7 个泛化轴测试，包括 cross-model (66.4%)、cross-strategy (59.1%)、preliminary cross-scale (60-70%)。

---

## Strengths

1. **Task novelty 确认无争议**：两位 Reviewer 一致认为 recursive generation depth estimation 是 genuinely 新的、有实际价值的问题。没有找到任何 prior work 做相同任务。从 binary detection 到 ordinal depth 是概念性跳跃。

2. **系统性 empirical coverage**：3×3 atlas 设计严谨，180K 样本规模充分，7 个泛化轴展现难得的探索广度。Feature consistency (Spearman ρ=0.868 cross-model) 和 classifier convergence (≤0.4pp spread) 是有说服力的证据。

3. **诚实透明��� Limitations**：论文对 d0 inflation、cross-strategy failure、reference model dependency、FPR 等问题的 disclosure 异常透明。Domain bias analysis 中主动报告并修正 bug (Appendix §A.6) 尤其值得肯定。

4. **Surface-text ablation**：Zero-shot LLM 在 30-36% 的 failure 清��地建立了 depth signal 不在 surface text 中的 negative evidence，虽 framing 需调整（见 Weaknesses）。

5. **Negative results 有参考价值**：PLM failure (19pp gap)、cross-τ non-transferability (46.7%)���curation PoC non-significance——这些对后续工作有重要指导意义。

---

## Weaknesses（按严重程度排序）

### Must-Fix（影响接收决定）

**[W-Critical-1] "Universal" overclaim 持续未解决** [AGREE R1+R2]
- 论文用 "universal and scale-variant" 描述 depth signal，但证据仅覆盖 5 个 decoder-only transformer (3×1-1.5B + 2×7B)
- Cross-model d1-d3 balanced accuracy 仅 55.4% (1.67× chance)，Pythia holdout d2 recall 低至 26.8%
- 此问题从 Round 3 持续至今，abstract/introduction 虽有 qualifier 但核心词 "universal" 未替换
- **要求**：全文替换 "universal" 为 "consistent across the three model families studied" 或等价限定表述

**[W-Critical-2] Perplexity tail dominance 的 novelty positioning 不足** [AGREE R1+R2, R1 with nuance]
- Dohmatob et al. (2024) "A Tale of Tails" 已建立 recursive training erodes distributional tails 的理论框架
- 本文的 p90_ppl/var_surprisal dominance 在概念层面是该理论的 empirical realization
- 论文未充分区分 "theory predicts tails erode" vs "our contribution: operationalizing erosion into classifiable ordinal depth"
- **要求**：Introduction/Related Work 明确 articulate 本文超越理论预测的贡献（EDD quantification、strategy-dependent trajectories、non-monotonic 7B behavior）

**[W-Critical-3] Curation PoC 统计不显著但列为 contribution** [AGREE R1+R2]
- RF-filtered vs unfiltered: p=0.407/0.492/0.607（全部不显著）
- RF vs random subsampling 显著仅证明 "informed selection > random dropping"——binary detection 即可实现
- Discussion 仍将 "depth-graduated curation" 列为 enabling application
- **要求**：从 contribution list 删除 curation claim，或降级为 "inconclusive pilot with insufficient statistical power"

**[W-Critical-4] Cross-scale 实验 confound-stacked，无法支撑 generalization claim** [AGREE R1+R2]
- 4 �� confounds 同时存在：4-bit QLoRA、instruction-tuning、n=500、single strategy
- 两个 7B 模型行为矛盾（Llama monotonic vs Qwen U-shaped）
- 论文 §5.4 caveats 已承认但 abstract 未充分反映
- **要求**：Abstract 对 7B 结果加 "preliminary" 和 explicit confound caveat

**[W-Critical-5] Reference model 循环依赖** [AGREE R1+R2, R2 lower severity]
- Pythia-1.4B 同时为 generator 和 reference，self-reference vs cross-reference 存在 4.1pp gap
- 仅测试 2 个同族 (~1B autoregressive) reference models
- **要求**：补充至少一个 architecturally distinct reference 实验，或在 Limitations 明确讨论 deployment 影响

### Should-Fix（影响评分但不一票否决）

**[W-Warn-1] LoRA 超参数 sensitivity 未探索** [AGREE R1+R2]
- 整个 benchmark 使用单一配置 (r=16, α=32, 3 epochs)
- 不同 rank/epochs 可能导致不同退化动态
- 至少应在一个 cell 测试 rank ∈ {4, 16, 64}

**[W-Warn-2] Cross-strategy transfer 需先验知识** [AGREE R1+R2]
- 从 ~70% 降到 59.1%；cross-τ 更差 (46.7%)
- 论文承认需 "strategy-conditioned classifiers" 但无 strategy detection 方案
- 对声称 practical relevance 的论文是 significant gap

**[W-Warn-3] Wild data FPR 过高** [AGREE R1+R2]
- GPT-2 XL C4: 22.4%，集中在 template/SEO content
- Model-dependent (OLMo 4.7% vs GPT-2 XL 22.4%) 意味 worst-case 不可接受
- 削弱 deployment framing

**[W-Warn-4] EDD 的 classifier-dependence 未明确** [AGREE R1+R2]
- 当前呈现为数据内在属性，实为 classifier+features 联合性质
- 应报告 EDD 在不同分类器下的一致性

**[W-Warn-5] Abstract 对 transfer 结果 representation 不平衡** [AGREE R1+R2]
- 70-85% 是 in-distribution；cross-model 仅 66.4% (d1-d3: 55.4%)
- Abstract 缺 transfer degradation 的 explicit acknowledgment

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识 [AGREE]：
- "Universal" overclaim 必须修正（R2-N1, R1 cross-response AGREE）
- Curation PoC 应降级（R2-N2, R1 AGREE 并修正自己 Round 1 判断）
- Cross-scale confounds 过多（R1-N4, R2-W3 一致）
- EDD 应标注为 operational measure（R1-N1, R2 AGREE with lower severity）
- LoRA sensitivity 需探索（R1-W1, R2 AGREE）
- Cross-strategy 限制 deployment（R1-W5, R2 AGREE）
- Wild data FPR 问题（R1-W4, R2 AGREE）
- Related Work 需补充 Schaeffer et al. (2025) 和 ordinal classification 经典工作

---

## Reviewer Divergence

**[分歧-1] CV 样本非独立性的严重程度**
- R1 (critical): 每个 depth 的 5000 样本来自同一 LoRA instance，违反 i.i.d. 假设
- R2 (REBUT): LOGO evaluation (72.1%=CV 72.0%)、cross-model transfer (66.4%)、feature consistency (ρ=0.868) 已充分 mitigate
- **Director 判断**：R2 的 empirical evidence 有说服力，降级为 should-fix。但建议在 Limitations 添加一段讨论。

**[分歧-2] 方法论贡献是否足够**
- R2 (concern): 19 perplexity features + RF，EDD 是 AUC threshold 的简单包装，方法论深度不足
- R1 (REBUT): Problem formulation + benchmark papers 在 *ACL 有先例 (GLUE, BIG-Bench)；方法简洁性本身有价值
- **Director 判断**：方法论轻量是客观事实，但不构成 reject 理由——论文贡献类型为 "novel task + systematic empirical study"。对 Findings 足够，Main Conference borderline���

---

## Questions for Authors

1. 如果使用多个独立 LoRA seeds 生成同��� depth 的数据（如 5 seeds × 1000 samples），然后进行 seed-grouped CV，预期准确率下降多少？
2. ��� 1.4B 模型同时运行 standard LoRA 和 QLoRA 以隔离量化效应的结果？
3. EDD 在 RF/XGB/LR 不同分类器下的值差异多大？
4. C4 FPR 是否有简单 post-hoc rule（如 repetition ratio threshold）可降低？
5. Pooled training（3 families 合并训练）vs leave-one-out 的 transfer performance 对比？

---

## Missing References

1. **Schaeffer et al. (2025)** "Position: Model Collapse Does Not Mean What You Think" — 对 model collapse 叙事的挑战，与本文基础假设直接相关
2. **Frank & Hall (2001)**; **Rennie & Srebro (2005)** — Ordinal classification 经典工作
3. **C2PA / Content Credentials framework** — Discussion provenance toolkit 部分应提及
4. **"A Closer Look at Model Collapse" (2025)** — memorization perspective，与 Appendix §A.5 "memorization as prerequisite" 直接相关

---

## External Review (Stanford Agentic Reviewer)

外部审稿未启用（项目配置 `external_review.paperreview_ai.enabled` 未设置）。

---

## Overall Assessment

**Score: Weak Accept → Findings (3.25/5)**
**Confidence: 4/5**

| Reviewer | Score | Key Concern |
|----------|-------|-------------|
| R1 | 3.0 (Findings) | 方法论缺陷（CV independence, reference circularity, cross-scale confounds） |
| R2 | 3.5 (Borderline) | Overclaiming + novelty positioning + curation non-significance |
| Director | 3.25 | 综合：novel task + solid-but-overclaimed empirics |

**判决理由**：
- **Novel task + genuine contribution**：Recursive generation depth estimation 是重要且未被 addressed 的问题。180K benchmark、EDD metric、Depth Degradation Atlas 有独立价值。
- **Overclaiming 是核心问题**："Universal"、curation application、cross-scale generalization 的 claims 与 evidence 之间存在 systematic gap。这不是技术错误而是 framing 问题——大部分可通过 toning down claims 解决。
- **方法论轻量但非 fatal**：作为 empirical study / task definition paper，方法不需要复杂。但 EMNLP main conference 对 novelty 的要求使其在 Main 和 Findings 之间。
- **建议**：Findings of EMNLP——修正 overclaiming 后可接收。如要冲击 Main Conference，需 (a) 补充 reference model 完整矩阵实验，(b) LoRA rank sensitivity，(c) 理论分析连接 Dohmatob framework。

---

## Detailed Comments

### §1 Introduction
- L14 "universal and scale-variant": 替换为 "consistent across the three decoder-only model families and three decoding strategies studied"
- Contribution bullet 3: 删除或降级 curation 相关 claim
- 明确区分本文贡献 vs Dohmatob (2024) 的理论预测

### §3 Method
- §3.2: BOS-seeded caveat 已加，adequate
- §3.3: 加段讨论 single-LoRA-instance 的 limitation
- §3.4 EDD: 加一句 "EDD is an operational measure conditional on the classifier and feature set, not an intrinsic data property"

### §4 Atlas
- §4.2: 弱化 individual feature "universal marker" → feature GROUP level dominant
- Table 1/2: 确认 accuracy 不一致（78.2% vs 78.8%）已解释

### §5 Generalization
- §5.1: LLM baseline 重新定位为 "surface-text ablation"，不再�� "superiority comparison"
- §5.4: Abstract 加 "preliminary" + confound caveat

### §6 Discussion
- Curation: 降级为 inconclusive pilot
- 加 strategy detection as deployment prerequisite
- 加理论段连接 Dohmatob tail-cutting framework（可选但 recommended）

### Limitations
- 加 single-LoRA-instance per depth ���论
- 加 reference model deployment dependency 讨论

### Related Work
- 补 Schaeffer et al. (2025)
- 补 Frank & Hall (2001), Rennie & Srebro (2005)
- 扩展 Mohamed et al. (2025) 区分至 2-3 句