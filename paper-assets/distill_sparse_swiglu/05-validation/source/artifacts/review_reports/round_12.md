---
round: 12
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-20T01:53:13.954842+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# Round 13 审稿报告（Fresh Review）

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 via ARR May 2026
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作格式）
**轮次**: 1 轮（交叉分享后收敛，无需 Round 2）

---

## Summary

本文提出将 SwiGLU LLM 稀疏预测器的训练目标从 per-neuron BCE 替换为 output-distribution KL divergence，配合 Gumbel-Sigmoid relaxation 实现端到端可微训练。在 LLaMA-3.1-8B 上，KL predictor（75.9M 参数，<1% base）在 30% sparsity 下将 TEAL perplexity 降低 18.6%（8.81 vs 10.82），在 50% 降低 51%。C1 target-swap ablation 表明 KL 发现的 mask pattern（与 magnitude mask 46–68% divergence）是质量提升的 proximate driver。跨架构验证覆盖 Mistral-7B 和 Qwen-2.5-14B，揭示 scale-dependent effects。

---

## Strengths

**S1. C1 Target-Swap Ablation 设计精巧且有力 [Full consensus]**
通过将 KL-discovered masks 转移到 BCE 训练，干净分离了 mask quality 和 gradient coupling 的贡献。50% sparsity 下 max Δ≤0.79pp（s42），retrained seeds (s123/s456) 30% PPL Δ≤0.03。这是全文最强的贡献，提供了有价值的 empirical insight。

**S2. 系统性消融覆盖全面 [Full consensus]**
Table 4 隔离了 Gumbel vs STE（+3.98 PPL）、divergence direction（forward > JSD > reverse）、loss function 贡献（KL effect 5.1× relaxation effect）、compensation redundancy。Appendix B–C 确认对 bottleneck/temperature/training steps 不敏感。

**S3. 诚实报告负面结果 [Full consensus]**
14B GSM8K −25pp、50% downstream collapse、无实际加速、OOD gap（C4 1.74× vs in-domain 1.46×）均在 Limitations 和正文中明确讨论。

**S4. 高可复现性 [Full consensus]**
1000 步 / 45 min / 单 GPU。超参完整披露。3-seed 评估（PPL CV<1%）。GPU 型号/训练时间均报告。Soundness 4/5。

**S5. Related Work 覆盖全面**
47 篇引用系统覆盖 training-free sparsity、predictor-based methods、KL distillation、MoE routing 等。与 MaskLLM 的三点区分论述清晰。

---

## Weaknesses

### Must-Fix（3 项，影响接收决定）

**N1. MSE intermediate baseline 缺失，taxonomy 核心 claim 无实验支撑 [Full consensus, R1-N1 + R2-W1]**
Table 1 定义 Decomposed/Intermediate/Coupled 三级 taxonomy，实验仅评估两端。§3.7 显式承认 "per-layer MSE is not evaluated in our experiments"。没有 MSE baseline，无法区分改进来自：(a) 任何形式的 non-trivial coupling，还是 (b) 特定的 end-to-end output-level coupling。ShadowLLM 在 taxonomy 中标为 Intermediate 但无数据对比。实验成本极低（替换 loss function），缺失令人遗憾。
→ **Action**: 训练 per-layer MSE predictor（相同架构），加入 Table 2 和 Table 4。或弱化 taxonomy 为概念组织工具。

**N2. 跨架构/跨规模 claim 过强，数据支撑不足 [Full consensus, R1-N2 + R2-N2]**
- Mistral-7B 全部 single seed，5/6 tasks win 的统计意义有限
- Qwen-14B GSM8K 32.1±5.2% vs TEAL 57.1%（−25pp, σ=5.2pp），MMLU −2.79pp uniform / −8.1pp global
- 14B actual sparsity mismatch: KL 29.6% vs TEAL 26.8%（2.8pp 差异可能解释部分 degradation）
- §4.6 的 "forward KL's mass-covering property disrupts narrow reasoning pathways" 是未验证推测
→ **Action**: Mistral 补 3-seed; 14B 对齐 actual sparsity 或明确报告; mass-covering 标为 hypothesis; 降低 abstract/conclusion cross-arch claim 强度。

**N3. SNR 证据选择性呈现 [Consensus with nuance, R1-N3 + R2 升级同意]**
§3.6 报告 "at step 300, KL achieves 5.14× higher SNR"，但 Appendix G 揭示 trajectory 是 non-monotonic 的——BCE 在 steps 100–250 surpasses KL。主文完全省略这一关键信息。Step 300 恰好是 BCE 刚被反超的时间点。且缺少 step 300–1000 的完整 trajectory。这构成 selective presentation，削弱 §3.6 "coupled gradient structural advantage" 叙事的可信度。
（R2 补充 nuance：如 KL 在 300–1000 持续保持优势则非 cherry-pick，但论文未展示后续数据。）
→ **Action**: 主文加一句 acknowledge non-monotonic trajectory; Appendix G 补完整 SNR 曲线至 step 1000。

### Should-Fix（9 项，影响评分但不一票否决）

**W1. 方法新颖性有限 [Full consensus, R2-N1 + R1 agrees]**
核心是 standard forward KL + standard Gumbel-Sigmoid 的组合。MaskLLM (NeurIPS 2024) 已证明 frozen weights + learnable masks + KL training 的有效性。论文自称 "primarily empirical"——Findings 定位合理，但不足以支撑 Main track long paper。
→ **Action**: 强化 empirical study 定位，弱化方法论创新暗示。

**W2. 下游 PPL disconnect [Divergence: R2 Must-Fix → R1 rebuts → Director 裁定 Should-Fix with caveat]**
30% 8B: KL 赢 ARC-c +4.4pp, WG +3.9pp, HS +7.8pp, PIQA +2.2pp，但输 MMLU −5.2pp, GSM8K −1.3pp（赢 4/6）。14B: GSM8K −25pp 和 MMLU reversal 更显著。PPL 改善不一致地 translate 为下游改善。R1 正确指出 8B 层面 KL 在多数任务上赢，但 14B 的 mixed results 削弱了方法的实用价值叙事。
→ **Action**: narrative 更平衡地呈现下游结果; 14B 结论标为 preliminary observation。

**W3. 30% sparsity mismatch [Full consensus, R1-W1]**
Penalty controller 在 30% 目标下 actual sparsity 28.5%（偏差 5%），λ 达 cap 5000。KL 比声称保留了更多 neurons。
→ **Action**: 主文报告 actual achieved sparsity; 验证更高 λ_max 效果。

**W4. Abstract "68% divergence" 未限定 sparsity [Full consensus, R1-W2]**
68% 是 50% sparsity 下数字; 30% 操作点仅 46%。Abstract/Introduction 未标注。
→ **Action**: 改为 "46–68% depending on sparsity" 或标注 "at 50%"。

**W5. 数值系统性向上取整 [Full consensus, R1-W3]**
19%（实 18.6%）、7.5×（实 7.31×）、MMLU +0.6pp（实 +0.5pp）——所有方向一致偏高。
→ **Action**: 统一精度或标注 "≈"。

**W6. 无 wall-clock speedup [Full consensus, R1-W4 + R2-W2]**
Predictor 增加 6.4% total overhead（§4.6 主文仅报告 2.7% predictor-only，有 downplaying 之嫌）。整个 pipeline 比 dense 更慢。方法的实用价值是 hypothetical 的。
→ **Action**: Abstract "renders compensation redundant" → "redundant in prediction quality"; Introduction 更早界定贡献范围。

**W7. OOD 统计覆盖不足 [Full consensus, R1-W5]**
C4 30% 仅 2-seed，50% single seed。"generalize across distributions" claim 与主实验 3-seed 标准不一致。
→ **Action**: 补 3-seed C4 或降低 claim。

**W8. Cross-arch allocation confound [Full consensus, R1-W6]**
Table 15 LLaMA 用 global，Mistral 用 uniform，Adv ratio 跨架构比较不 clean。
→ **Action**: 增加 matched allocation 行或更显著标注。

**W9. Conclusion 过短 [Full consensus, R2-W3]**
3 句话 + vspace{-14pt}，无 future work。Formatting red flag。
→ **Action**: 精简 §4.6，为 Conclusion 腾空间。

---

## Reviewer Consensus

**[AGREE] 所有 Must-Fix 和绝大多数 Should-Fix/Minor**:
- MSE baseline 缺失（N1）
- Cross-arch claim 过强（N2）
- SNR selective presentation（N3，R2 程度判断略保守但同意核心问题）
- 方法新颖性有限（W1）
- Sparsity mismatch（W3）
- 68% unlabeled（W4）
- 数值 rounding（W5）
- 无 speedup（W6）
- OOD 不足（W7）
- Allocation confound（W8）
- Conclusion 短（W9）

## Reviewer Divergence

**[REBUT on severity] 下游 PPL disconnect（W2）**:
- R2 定 Must-Fix: PPL 改善不 translate 为下游改善，削弱实用价值
- R1 rebut: 30% 8B 上 KL 赢 4/6 任务（ARC-c +4.4, WG +3.9, HS +7.8, PIQA +2.2），仅输 MMLU −5.2 和 GSM8K −1.3。PPL-downstream non-monotonic 关系是论文发现之一，非缺陷。
- **Director 裁定**: Should-Fix with strong caveat。8B 层面不构成 Must-Fix，但 14B GSM8K −25pp 是 serious concern，需在 narrative 中更平衡呈现。

---

## Questions for Authors

1. **为什么不评估 MSE intermediate baseline？** 训练成本与 BCE 相当，能直接回答 coupling 程度的关键问题。
2. **Step 1000 的 SNR ratio？** 论文仅展示到 step 300。完整 trajectory 对 "coupled gradient advantage" narrative 至关重要。
3. **14B sparsity mismatch 影响？** KL 29.6% vs TEAL 26.8%。控制 actual sparsity 后 MMLU/GSM8K 差距是否缩小？
4. **C1 oracle 对 checkpoint 的敏感性？** 如在 step 500 提取 masks，BCE 是否仍能 match KL quality？
5. **单 predictor 多 sparsity 目标？** 每个 target 训练 45 min 在部署中不可忽视。

---

## Missing References

无重大遗漏。可考虑补充（非必须）：
- Bambhaniya et al., 2024, "Progressive Gradient Flow for Robust N:M Sparsity Training" — 如讨论 N:M 扩展
- Li et al., 2023, "Lazy Neuron Phenomenon in Transformers" — 与 mask pattern divergence 分析相关

---

## External Review

**状态**: 未请求（项目未启用 paperreview.ai 外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: 超时（elapsed 794s）。视觉审查 Agent 未能在时限内完成。用户可决定是否重新触发 `dispatch_visual_check`。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

**评分理由**:

这是一篇执行扎实的实证研究。C1 target-swap ablation 是精巧的 disentanglement 实验，证明了 mask quality 而非 gradient coupling mechanism 是 inference-stage quality 的 proximate driver。系统性消融全面（Table 4 隔离了 5+ 设计选择），负面结果的诚实报告值得肯定（14B GSM8K −25pp、50% downstream collapse、无加速）。训练成本极低（1000 步/45 min/单 GPU），可复现性高。

但方法新颖性有限（standard KL + standard Gumbel，MaskLLM 已证明该 principle），taxonomy 的核心 claim（end-to-end coupling 优于 intermediate coupling）因 MSE baseline 缺失而无法验证。SNR 证据的选择性呈现（隐藏 mid-training BCE 反超）是 presentation integrity concern。跨架构 claim 数据不足（Mistral single seed, 14B sparsity mismatch）。14B 的 GSM8K −25pp 和 MMLU reversal 使得方法的 scale generalization 存疑。无 wall-clock speedup，实用价值 hypothetical。

论文定位为 empirical study 是合理的，C1 ablation 和 regime analysis 对 activation sparsity 社区有参考价值，符合 EMNLP Findings 水平。但方法论和 presentation 问题阻止其达到 Borderline Conference。

**Reviewer 评分**:
- R1: 3.5 (Borderline Conference), Confidence 4/5
- R2: 3.0 (Findings), Confidence 4/5

**Confidence**: 4/5

---

## Detailed Comments（逐节）

### Abstract
- "diverge 68%" 应标注 "at 50% sparsity"（30% 仅 46%）[W4]
- "renders compensation redundant" 应加 "in prediction quality"[W6]
- "19%" 实为 18.6%, "7.5×" 实为 7.31× [W5]
- 14B 描述未区分 uniform vs global allocation [R2-M4]

### §1 Introduction
- "proximate driver" 全文 7+ 处，此处首次出现，后续应减少重复 [R1-Minor]
- Cross-arch contribution (line 23) 强度应降低 [N2]

### §2 Related Work
- 覆盖全面，无重大遗漏

### §3 Method
- §3.6 SNR 分析：必须 acknowledge non-monotonic trajectory [N3]
- §3.7 Taxonomy: MSE intermediate cell 无实验支撑 [N1]

### §4 Experiments
- §4.1: 应报告 all methods 的 actual achieved sparsity [W3]
- §4.2 Main Results: 数值精度需修正 [W5]
- §4.4 C1 Ablation: s42 oracle 版本差异应在正文讨论（非仅脚注）[R2-W5]
- §4.6 Cross-arch: Mistral 补 3-seed; 14B 对齐 sparsity; mass-covering 标为 hypothesis [N2]
- §4.6 Overhead: 报告 total 6.4% 而非仅 predictor 2.7% [W6]

### §5 Conclusion
- 扩展至 4-6 句，加 future work，删 vspace{-14pt} [W9]

### Limitations
- 讨论充分且诚实，是论文的优点 [S3]

### Appendix
- G: 补完整 SNR 曲线至 step 1000 [N3]
- D: C4 补 3-seed [W7]
- L: Table 15 标注或增加 matched allocation [W8]

### References
- Griffin (de2024): 更新 venue/year
- AdamW (loshchilov2019): 统一使用 venue 年份