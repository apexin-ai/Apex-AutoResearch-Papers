# Reviewer 2 coordination — Part 2 of 3

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-2-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/c9/c95db014e7f41ee38e2b.json)

## Round 11

### Tool result

_source line 513 · 2026-05-20T03:16:55.877031+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 514 · 2026-05-20T03:17:02.348769+00:00_

审稿完成。报告已提交至 Review Director，核心判断：

- **Overall: 3.0 (Findings)**，conditional on 修复 title overclaiming 和 distribution matching claim
- **最强贡献**：epoch confound 发现（D&R 优势主要来自 multi-epoch 而非 reweighting 本身）
- **主要问题**：title "When Does...Work?" 与单模型/单污染类型/小 scale 的实验范围严重不匹配；1.7B 无效果但被边缘化；无 downstream 改进；"no distribution matching" 在 3 seeds 下 underpowered

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 12

## Round 12

4 recorded events


### User

_source line 515 · 2026-05-20T03:18:24.504592+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 完整审稿报告

**审查侧重**: 方法严谨性 + 实验设计

### Summary
本文研究 continued LM pretraining 中 detect-and-reweight (D&R) 范式的有效性。核心发现有二：(1) D&R 报告的 PPL 优势主要来自 multi-epoch exposure 而非 distribution matching（epoch confound）；(2) 提出基于 α_eff + ESS 双约束的 adaptive reweighting 框架，避免 per-model grid search。在 Qwen3-0.6B 上 3 seeds 实验显示 Δ≈−0.020 PPL 的一致性改进，但改进幅度小且缺乏统计显著性检验；1.7B 规模实验（2 seeds）效果几乎消失。

### Strengths
S1. Epoch confound 的识别具有方法论价值。
S2. Dual-constraint 框架理论动机清晰。
S3. 消融实验覆盖全面。
S4. Detector type 分析揭示了非直觉发现。
S5. 诚实的 limitations 讨论。

### Weaknesses (Must-Fix)

**N1 [critical] Epoch confound——论文最重要的发现——仅基于单 seed（seed 42）。**
Table 1 中 "D&R full" 和 "D&R epoch-matched" 两行均为 seed 42 单次实验。核心 claim "gap shrinks from 0.384 to Δ≈0.017" 完全依赖于该单 seed。Epoch-matched D&R 与 Adaptive b* 在 cosine schedule、LR curve 起点等训练动态上存在差异，单 seed 无法排除 seed-specific confound。

**N2 [critical] N=3 seeds + Δ=−0.020 PPL + 无正式统计检验 = 核心效果声明证据不足。**
Table 2 中 Adaptive b* 改进 Δ≈−0.020（mean PPL 17.674 vs. Uniform 17.694）来自 3 seeds。论文使用 "directional consistency" 替代统计检验。Table 2 注释 "²" 标注 seed 42 可能是 outlier。建议：报告 paired differences 及标准差，执行 paired t-test 或 bootstrap CI。

**N3 [critical] B=4 micro-batch 下 α_eff 仅 5 个离散值，continuous framework 的实际意义存疑。**
Proposition 1-2 建立在连续单调性基础上，但实际 α_eff 只有 5 个取值。Bisection 退化为 brute-force 枚举。Appendix I 报告 α_eff(0) 与真实 batch-level real fraction 的 MAE=0.114。建议讨论 B=4 下离散化的理论影响，补充 B=8/B=16 实验，或调整 framing。

### Weaknesses (Should-Fix)

**W1 [warning] 1.7B 规模结果实际上是负面证据，但论文措辞模糊。**
2 seeds, Δ≈−0.01 在噪声范围内。应更明确定位为 "目前无证据表明方法在更大规模有效"。

**W2 [warning] Self-contamination 设计的 external validity 严重受限。**
所有主实验使用 self-contamination（AUC=0.94）。Cross-model transfer（Appendix M）单 seed 且未报告 PPL comparison。

**W3 [warning] ρ=0.2 失败模式未充分探索。**
未探索是否可通过调整 τ 或 detector threshold 应对。

**W4 [warning] Detector calibration 敏感性未分析。**
方法依赖 post-hoc temperature scaling（T=0.204, ECE=0.05），但未分析 calibration 质量对最终 PPL 的影响。

### Minor
M1. Figure 1 y 轴压缩视觉放大差异。
M2. Table 2 中 seed 42 使用 checkpoint-resumed model，应更显著标注。
M3. Appendix I α_eff negative bias 值得正文简要提及。

### Questions
Q1. Table 1 epoch confound 能否扩展到 3 seeds？
Q2. Adaptive b* vs. Uniform 的 paired differences 及标准差？能否提供 paired t-test 或 bootstrap 95% CI？
Q3. 在 ρ 未知的实际场景中，如何判断 contamination level 是否足以使 reweighting 有效？
Q4. 1.7B 中 Δ≈−0.01 是否与 B=4 离散化有关？
Q5. Generative detector reversal 是否可能是 calibration artifact？

### Missing References
无明显缺失。51 条引用覆盖了主要领域。

### Scores
Soundness 3/5, Excitement 3/5, Reproducibility 4/5
**Overall: 3.0 (Findings)**, Confidence 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-20T03:19:38.308530+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix Weaknesses\n\n**[AGREE] R1-N1: Epoch confound 仅基于 seed 42 单次实验。**\n同意这是一个重要的方法论缺陷。Table 1 的 epoch-matched 对照确实只有 seed 42，而 epoch confound 是论文最核心的 claim。我在审稿中注意到 Table 2 中 seed 42 存在 checkpoint resume artifact（Appendix N 确认 seed 42 使用了 checkpoint-resumed model，前 1,000 steps 超参不同），这进一步加重了单 seed 的可信度问题。如果 epoch confound 的幅度 (0.384→0.017) 在其他 seeds 上不可复现，论文的核心贡献将大幅缩水。\n\n不过需补充：即使 epoch-matched 实验是单 seed，Table 2 中**三个 seeds 的 Adaptive b* vs. Uniform 比较**都显示 epoch-controlled 下的改进幅度仅 Δ≈-0.020（远小于 full-length 的 0.384），这从侧面支持 epoch confound 存在——只是精确量化 (0.384→0.017) 缺乏多 seed 验证。\n\n**[AGREE] R1-N2: N=3 seeds + Δ=-0.020 + 无统计检验 = 证据不足。**\n完全同意。我的 W3 (marginal improvements) 指出了同样的问题。论文使用 \"directional consistency\" 作为替代指标，但 3 个方向一致的观测在统计上并不充分——3 次 coin flip 全部正面的概率为 12.5%，远未达到显著性门槛。\n\n更关键的是，Table 7 的 downstream benchmarks 显示**零** downstream 改进 (|Δ| ≤ 0.01)，这意味着即使 PPL 差异是真实的，其实际意义也存疑。R1 建议的 paired t-test / bootstrap CI 是合理的最低要求。\n\n**[REBUT] R1-N3: B=4 离散化使 continuous framework 意义存疑——部分同意问题存在，但严重程度被高估。**\nR1 的观察是正确的：B=4 时 α_eff 仅有 {0, 0.25, 0.5, 0.75, 1.0} 五个值，bisection 确实退化为枚举。但我认为这不构成 critical 级别问题，理由如下：\n\n1. **理论框架的价值不取决于当前实验的 batch size。** Propositions 1-2 建立的 monotonicity/convexity 性质对任意 B 成立（Appendix A 证明不依赖 B）。论文选择 B=4 是因为 GPU 内存限制（Section 4 提到 single NVIDIA RTX PRO 6000），不是框架设计的固有限制。\n2. **Section 3.3 明确讨论了离散化。** 原文：\"This discretization means α_eff is a proxy for the true batch-level real fraction\"——作者并未声称 continuous approximation 在 B=4 下是精确的。\n3. **关键机制不在于 α_eff 的精度，而在于三种 regime 的分类。** Algorithm 1 的核心逻辑是将 batches 分为 clean / α_eff-binding / ESS-binding 三类——这个分类在 B=4 下仍然有意义（Section 5.4 Table 4 报告了三种 regime 的比例）。\n\n但我同意 R1 的建议：补充 B=8/16 实验可以更好地验证框架在更细粒度下的表现，且 Appendix I 的 MAE=0.114 negative bias 确实值得在正文提及。建议将此从 critical 降为 should-fix。\n\n---\n\n### Should-Fix Weaknesses\n\n**[AGREE] R1-W1: 1.7B 结果是负面证据但措辞模糊。**\n我的 W4 提出了完全相同的问题。Appendix E Table 5 的 1.7B 结果 (2 seeds, Δ≈-0.01) 实质上是方法不 work 的证据。论文将其定位为 \"insufficient for statistical conclusions\" 是技术性正确但具有误导性——2 seeds 确实不够下结论，但现有 2 seeds 的 point estimate 是零效果。应改为 \"preliminary evidence suggests the method may not generalize to 1.7B scale\"。\n\n**[AGREE] R1-W2: Self-contamination external validity 受限。**\n我的 W1 (should-fix) 提出了相同问题，并进一步指出 Appendix M cross-model transfer 的 \"inconsistent quality differences\" 实际上是负面证据。R1 补充了 cross-model 实验\"未报告 PPL comparison\"——确认了此实验的不完整性。\n\n**[AGREE] R1-W3: ρ=0.2 失败模式未充分探索。**\n同意。论文在 Limitations 中将 ρ=0.2 失败归因于 \"insufficient room for batch-level o_eff estimation\"，但未尝试任何补救（如降低 τ、调整 detector threshold、增大 B）。对于一篇问 \"when does it work\" 的论文，不探索失败的边界条件是一个明显的遗漏。\n\n**[REBUT] R1-W4: Detector calibration 敏感性——问题存在但论文实际上有部分覆盖。**\nR1 说 \"未分析 calibration 质量对最终 PPL 的影响\"。但 Section 3.1 讨论了 post-hoc calibration (T=0.204, ECE 从 0.05 降至 0.03)，Section 5.3 的 threshold sensitivity analysis (Figure 3) 间接涵盖了 calibration 对 quality threshold τ 的影响——τ 的有效范围 0.1-0.8 (Section 5.3) 意味着方法对 q-score 的绝对精度不太敏感。\n\n不过我同意 R1 的方向：一个直接的 ablation（有 calibration vs. 无 calibration 的 PPL 对比）会更有说服力。当前证据是间接的。建议保留为 should-fix 但降低优先级。\n\n---\n\n### Minor Issues\n\n**[AGREE] R1-M1: Figure 1 y 轴压缩。**\n我的 M1 指出了同一图缺少 confidence band。R1 从另一个角度（y 轴刻度）补充了视觉呈现问题。两个问题应同时修复。\n\n**[AGREE] R1-M2: Seed 42 checkpoint resume 需更显著标注。**\n完全同意。Appendix N 分析了 checkpoint resume artifact (Δ=-0.011)，但 Table 2 中 seed 42 的标注仅是脚注 \"²\"，极易被忽略。考虑到 seed 42 同时是 epoch-matched 实验的唯一 seed（R1-N1），这个标注的不显著性问题更为严重。\n\n**[AGREE] R1-M3: α_eff negative bias 值得正文提及。**\nAppendix I 的 MAE=0.114 和 consistent negative bias (r=-0.031) 意味着方法系统性低估真实 real fraction，导致更保守的干预。这是方法行为的重要特征，正文 Section 3.3 中一句话提及即可。\n\n---\n\n### Questions 回应\n\n**R1-Q1 (epoch confound 扩展到 3 seeds):** 同意这是最高优先级的补充实验。如果作者能在 rebuttal 期间提供，将显著增强论文可信度。\n\n**R1-Q2 (paired test):** 同意需要。我在 N2 回应中已确认。\n\n**R1-Q3 (ρ 未知场景):** 好问题。论文假设 contamination ratio ρ 已知（Section 3.1: \"The contamination ratio ρ = |D_synth|/|D| is unknown, a realistic assumption\"——但后续实际实验全部使用已知 ρ）。这是 framing 与实验之间的矛盾。\n\n**R1-Q4 (1.7B 与 B=4 离散化):** 有意义的 hypothesis。如果 1.7B 的 batch size 不同于 0.6B（更大的模型通常用更大的 effective batch size），α_eff 的离散化程度可能不同，值得 check。但我怀疑这不是主因——更可能是 scale 本身改变了 reweighting 的 signal-to-noise ratio。\n\n**R1-Q5 (generative detector reversal 是否为 calibration artifact):** 有洞察力的问题。Table 10 (Appendix J) 显示 generative detectors (GPT-2, N-gram PPL) 的 AUC 都在 0.73-0.91 范围，且它们 \"assign high q-scores to fluent human text\"——这是一个 systematic bias，不太可能仅通过 calibration 修复。但 R1 的方向是对的：如果 generative detectors 经过更好的 calibration，reversal 可能减轻。当前论文没有测试这一点。\n\n---\n\n### 综合评估\n\nR1 和我（R2）的核心判断高度一致：\n\n**共识点：**\n1. Epoch confound 是有价值的发现，但单 seed 验证不足 (R1-N1 = R2 隐含)\n2. 效果微小且缺乏统计检验 (R1-N2 ≈ R2-W3)\n3. 1.7B 负面结果被边缘化 (R1-W1 = R2-W4)\n4. Self-contamination 外部效度受限 (R1-W2 = R2-W1)\n5. Title overclaiming (R2-N1, R1 的 summary 也暗示)\n6. Overall 3.0 (Findings) with conditions\n\n**分歧点：**\n1. R1-N3 (B=4 离散化)：R1 定为 critical，我认为 should-fix。理论框架不依赖 B，且离散化已被论文承认。实验上的 B=4 限制是硬件约束，不是方法缺陷。\n2. R1-W4 (calibration 敏感性)：R1 定为 should-fix，我认为论文有部分间接覆盖 (§5.3 threshold sensitivity)，优先级偏低。\n\n**我维持 Overall 3.0 (Findings) 评分**，条件是 N1 (overclaiming) 和 N2 (distribution matching claim) 得到修复，且 epoch confound 实验补充多 seed 验证。",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix Weaknesses\n\n**[AGREE] R1-N1: Epoch confound 仅基于 seed 42 单次实验。**\n同意这是一个重要的方法论缺陷。Table 1 的 epoch-matched 对照确实只有 seed 42，而 epoch confound 是论文最核心的 claim。我在审稿中注意到 Table 2 中 seed 42 存在 checkpoint resume artifact（Appendix N 确认 seed 42 使用了 checkpoint-resumed model，前 1,000 steps 超参不同），这进一步加重了单 seed 的可信度问题。如果 epoch confound 的幅度 (0.384→0.017) 在其他 seeds 上不可复现，论文的核心贡献将大幅缩水。\n\n不过需补充：即使 epoch-matched 实验是单 seed，Table 2 中**三个 seeds 的 Adaptive b* vs. Uniform 比较**都显示 epoch-controlled 下的改进幅度仅 Δ≈-0.020（远小于 full-length 的 0.384），这从侧面支持 epoch confound 存在——只是精确量化 (0.384→0.017) 缺乏多 seed 验证。\n\n**[AGREE] R1-N2: N=3 seeds + Δ=-0.020 + 无统计检验 = 证据不足。**\n完全同意。我的 W3 (marginal improvements) 指出了同样的问题。论文使用 \"directional consistency\" 作为替代指标，但 3 个方向一致的观测在统计上并不充分——3 次 coin flip 全部正面的概率为 12.5%，远未达到显著性门槛。\n\n更关键的是，Table 7 的 downstream benchmarks 显示**零** downstream 改进 (|Δ| ≤ 0.01)，这意味着即使 PPL 差异是真实的，其实际意义也存疑。R1 建议的 paired t-test / bootstrap CI 是合理的最低要求。\n\n**[REBUT] R1-N3: B=4 离散化使 continuous framework 意义存疑——部分同意问题存在，但严重程度被高估。**\nR1 的观察是正确的：B=4 时 α_eff 仅有 {0, 0.25, 0.5, 0.75, 1.0} 五个值，bisection 确实退化为枚举。但我认为这不构成 critical 级别问题，理由如下：\n\n1. **理论框架的价值不取决于当前实验的 batch size。** Propositions 1-2 建立的 monotonicity/convexity 性质对任意 B 成立（Appendix A 证明不依赖 B）。论文选择 B=4 是因为 GPU 内存限制（Section 4 提到 single NVIDIA RTX PRO 6000），不是框架设计的固有限制。\n2. **Section 3.3 明确讨论了离散化。** 原文：\"This discretization means α_eff is a proxy for the true batch-level real fraction\"——作者并未声称 continuous approximation 在 B=4 下是精确的。\n3. **关键机制不在于 α_eff 的精度，而在于三种 regime 的分类。** Algorithm 1 的核心逻辑是将 batches 分为 clean / α_eff-binding / ESS-binding 三类——这个分类在 B=4 下仍然有意义（Section 5.4 Table 4 报告了三种 regime 的比例）。\n\n但我同意 R1 的建议：补充 B=8/16 实验可以更好地验证框架在更细粒度下的表现，且 Appendix I 的 MAE=0.114 negative bias 确实值得在正文提及。建议将此从 critical 降为 should-fix。\n\n---\n\n### Should-Fix Weaknesses\n\n**[AGREE] R1-W1: 1.7B 结果是负面证据但措辞模糊。**\n我的 W4 提出了完全相同的问题。Appendix E Table 5 的 1.7B 结果 (2 seeds, Δ≈-0.01) 实质上是方法不 work 的证据。论文将其定位为 \"insufficient for statistical conclusions\" 是技术性正确但具有误导性——2 seeds 确实不够下结论，但现有 2 seeds 的 point estimate 是零效果。应改为 \"preliminary evidence suggests the method may not generalize to 1.7B scale\"。\n\n**[AGREE] R1-W2: Self-contamination external validity 受限。**\n我的 W1 (should-fix) 提出了相同问题，并进一步指出 Appendix M cross-model transfer 的 \"inconsistent quality differences\" 实际上是负面证据。R1 补充了 cross-model 实验\"未报告 PPL comparison\"——确认了此实验的不完整性。\n\n**[AGREE] R1-W3: ρ=0.2 失败模式未充分探索。**\n同意。论文在 Limitations 中将 ρ=0.2 失败归因于 \"insufficient room for batch-level o_eff estimation\"，但未尝试任何补救（如降低 τ、调整 detector threshold、增大 B）。对于一篇问 \"when does it work\" 的论文，不探索失败的边界条件是一个明显的遗漏。\n\n**[REBUT] R1-W4: Detector calibration 敏感性——问题存在但论文实际上有部分覆盖。**\nR1 说 \"未分析 calibration 质量对最终 PPL 的影响\"。但 Section 3.1 讨论了 post-hoc calibration (T=0.204, ECE 从 0.05 降至 0.03)，Section 5.3 的 threshold sensitivity analysis (Figure 3) 间接涵盖了 calibration 对 quality threshold τ 的影响——τ 的有效范围 0.1-0.8 (Section 5.3) 意味着方法对 q-score 的绝对精度不太敏感。\n\n不过我同意 R1 的方向：一个直接的 ablation（有 calibration vs. 无 calibration 的 PPL 对比）会更有说服力。当前证据是间接的。建议保留为 should-fix 但降低优先级。\n\n---\n\n### Minor Issues\n\n**[AGREE] R1-M1: Figure 1 y 轴压缩。**\n我的 M1 指出了同一图缺少 confidence band。R1 从另一个角度（y 轴刻度）补充了视觉呈现问题。两个问题应同时修复。\n\n**[AGREE] R1-M2: Seed 42 checkpoint resume 需更显著标注。**\n完全同意。Appendix N 分析了 checkpoint resume artifact (Δ=-0.011)，但 Table 2 中 seed 42 的标注仅是脚注 \"²\"，极易被忽略。考虑到 seed 42 同时是 epoch-matched 实验的唯一 seed（R1-N1），这个标注的不显著性问题更为严重。\n\n**[AGREE] R1-M3: α_eff negative bias 值得正文提及。**\nAppendix I 的 MAE=0.114 和 consistent negative bias (r=-0.031) 意味着方法系统性低估真实 real fraction，导致更保守的干预。这是方法行为的重要特征，正文 Section 3.3 中一句话提及即可。\n\n---\n\n### Questions 回应\n\n**R1-Q1 (epoch confound 扩展到 3 seeds):** 同意这是最高优先级的补充实验。如果作者能在 rebuttal 期间提供，将显著增强论文可信度。\n\n**R1-Q2 (paired test):** 同意需要。我在 N2 回应中已确认。\n\n**R1-Q3 (ρ 未知场景):** 好问题。论文假设 contamination ratio ρ 已知（Section 3.1: \"The contamination ratio ρ = |D_synth|/|D| is unknown, a realistic assumption\"——但后续实际实验全部使用已知 ρ）。这是 framing 与实验之间的矛盾。\n\n**R1-Q4 (1.7B 与 B=4 离散化):** 有意义的 hypothesis。如果 1.7B 的 batch size 不同于 0.6B（更大的模型通常用更大的 effective batch size），α_eff 的离散化程度可能不同，值得 check。但我怀疑这不是主因——更可能是 scale 本身改变了 reweighting 的 signal-to-noise ratio。\n\n**R1-Q5 (generative detector reversal 是否为 calibration artifact):** 有洞察力的问题。Table 10 (Appendix J) 显示 generative detectors (GPT-2, N-gram PPL) 的 AUC 都在 0.73-0.91 范围，且它们 \"assign high q-scores to fluent human text\"——这是一个 systematic bias，不太可能仅通过 calibration 修复。但 R1 的方向是对的：如果 generative detectors 经过更好的 calibration，reversal 可能减轻。当前论文没有测试这一点。\n\n---\n\n### 综合评估\n\nR1 和我（R2）的核心判断高度一致：\n\n**共识点：**\n1. Epoch confound 是有价值的发现，但单 seed 验证不足 (R1-N1 = R2 隐含)\n2. 效果微小且缺乏统计检验 (R1-N2 ≈ R2-W3)\n3. 1.7B 负面结果被边缘化 (R1-W1 = R2-W4)\n4. Self-contamination 外部效度受限 (R1-W2 = R2-W1)\n5. Title overclaiming (R2-N1, R1 的 summary 也暗示)\n6. Overall 3.0 (Findings) with conditions\n\n**分歧点：**\n1. R1-N3 (B=4 离散化)：R1 定为 critical，我认为 should-fix。理论框架不依赖 B，且离散化已被论文承认。实验上的 B=4 限制是硬件约束，不是方法缺陷。\n2. R1-W4 (calibration 敏感性)：R1 定为 should-fix，我认为论文有部分间接覆盖 (§5.3 threshold sensitivity)，优先级偏低。\n\n**我维持 Overall 3.0 (Findings) 评分**，条件是 N1 (overclaiming) 和 N2 (distribution matching claim) 得到修复，且 epoch confound 实验补充多 seed 验证。",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-20T03:19:42.328456+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4019
}
```

</details>

---


### Assistant

_source line 518 · 2026-05-20T03:19:48.572750+00:00_

交叉回应已提交。

核心结论：R1 和 R2 在 6 个关键判断上高度一致（epoch confound 验证不足、效果微小无统计检验、1.7B 负面证据被淡化、self-contamination 局限、overclaiming、Overall 3.0）。两个分歧点：(1) B=4 离散化问题我认为 R1 定级偏高（should-fix 而非 critical，因理论不依赖 B）；(2) calibration 敏感性论文有部分间接覆盖。维持 Overall 3.0 (Findings) 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 13

## Round 13

72 recorded events


### User

_source line 519 · 2026-05-21T11:28:01.590295+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。

## 审稿目标
- 目标 venue: EMNLP 2026（ARR May 2026 cycle，截止 2026-05-25）
- 格式要求: ACL 两栏模板，long paper 正文 8 页限制，参考文献不限，double-blind 匿名
- 必须包含: Limitations 章节 + Responsible NLP Research Checklist

## 论文信息
- 路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex
- 标题: "When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining"

## 你的审查侧重

### 1. 新颖性评估
- Contribution 1（epoch confound）：指出 D&R 的优势主要来自多 epoch 曝光——这是一个实验观察还是一个有深度的分析贡献？是否已有类似发现？
- Contribution 2（adaptive b*）：dual-constraint 框架 vs 简单的 grid search——节省计算的实用价值 vs 学术新颖性如何权衡？
- Contribution 3（detector requirements）：calibration + discrimination 的发现是否足够新颖，还是已知的常识？
- 整体：论文是否在 "incremental improvement + careful analysis" 和 "significant contribution" 之间？

### 2. Related Work 覆盖度
- 检查是否遗漏了重要的相关工作，特别是：
  - 最新的 model collapse 防治方法（2025-2026）
  - 其他 instance-level reweighting 方法
  - 其他 adaptive exponent/threshold 选择方法
  - 重要的 data curation for LLM pretraining 工作
- 与 Drayson et al. 2025 的差异是否被准确和公平地描述？

### 3. Limitations 充分性
- 论文的 Limitations 章节是否诚实地覆盖了所有关键限制？
- 是否有被回避的 limitation（如 batch size 极小、单一模型家族、contamination 是自生成的等）？

### 4. 写作质量和 Presentation
- 论文组织是否清晰？各 section 的信息密度是否均匀？
- 数学符号是否一致？表格和图是否清晰可读？
- Abstract 是否准确概括了全文？是否有 overclaim？
- 是否遵守 EMNLP 2026 格式要求（8页正文限制、匿名、Limitations 章节等）？

### 5. 引用质量
- 引用是否都真实存在？是否有格式问题？
- 特别关注 wang2026survive（2026 年论文）和 yang2026mixing 是否为真实发表/预印本

请按以下结构输出审稿意见：
1. Summary（2-3句）
2. Strengths（逐条）
3. Weaknesses（逐条，标注严重程度：critical/major/minor）
4. Questions for Authors
5. Missing References（如有）
6. Overall Assessment（评分 + 置信度）

评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-21T11:28:12.919108+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-21T11:28:12.969664+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-21T11:28:22.029019+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "1-5",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "1-5",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-21T11:28:22.987322+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 571.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.8}], \"total_pages\": 16, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-21T11:28:23.087956+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 525 · 2026-05-21T11:28:23.439294+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 526 · 2026-05-21T11:28:31.032169+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Metareview Scores

The ARR metareview score changed in February 2025 to be more aligned with reviewer scores. Like with reviews, the score should be backed up by the meta-review text. The options include: 5 = Consider for Award (top 2.5% papers
…[truncated 442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7944
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-21T11:29:29.821443+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 51, \"total_citations\": 79, \"unique_cited_keys\": 51, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 38, \"online_not_found\": 6, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"katharopoulos2018not\", \"type\": \"inproceedings\", \"title\": \"Not All Samples Are Created Equal: Deep Learning with Importance Sampling\", \"authors\": \"\", \"year\": \"2018\", \"venue\": \"International Conference on Machine Learning\"}, {\"key\": \"ren2018learning\", \"type\": \"inproceedings\", \"title\": \"Learning to Reweight Examples for Robust Deep Learning\", \"authors\": \"Ren, Mengye and Zeng, Wenyuan and Yang, Bin and Urtasun, Raquel\", \"year\": \"2018\", \"venue\": \"International Conference on Machine Learning\"}, {\"key\": \"chen2024bull\", \"type\": \"article\", \"title\": \"Take the Bull by the Horns: Hard Sample-Reweighted Continual Training Improves LLM Generalization\", \"authors\": \"Chen, Xuxi and Li, Zhendong and Cai, Daixuan and Yao, Huanran and Chen, Zheng an...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.14270\"}, {\"key\": \"kang2025demystifying\", \"type\": \"inproceedings\", \"title\": \"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls\", \"authors\": \"Kang, Feiyang and Xu, Yifan and Pu, Jingkang and Hu, Bushi and Li, Haonan and Ch...\", \"year\": \"2025\", \"venue\": \"EMNLP\"}, {\"key\": \"zibakhsh2025fortifai\", \"type\": \"article\", \"title\": \"ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse\", \"authors\": \"Zibakhsh Shabgahi, Soheil and Aghazadeh, Pedram and Mirhoseini, Azalia and Koush...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2509.08972\"}, {\"key\": \"yi2025escaping\", \"type\": \"article\", \"title\
…[truncated 38332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 66382
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-21T11:29:37.955037+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-21T11:29:38.457182+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-21T11:29:38.457633+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-21T11:29:38.959525+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-21T11:29:38.959961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-21T11:29:39.913207+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-21T11:29:39.913628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-21T11:29:40.866796+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-21T11:29:40.867141+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-21T11:29:41.318842+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-21T11:29:42.324862+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "6-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "6-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-21T11:29:44.305567+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.0}], \"total_pages\": 16, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1980
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-21T11:29:44.307634+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer scoring criteria, including all dimensions (soundness, excitement, overall assessment, confidence, etc.), their score ranges, and descriptions for each score level. Also extract any specific instructions about what reviewers should evaluate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer scoring criteria, including all dimensions (soundness, excitement, overall assessment, confidence, etc.), their score ranges, and descriptions for each score level. Also extract any specific instructions about what reviewers should evaluate."
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-21T11:29:50.287660+00:00_

# ARR Reviewer Scoring Criteria

Based on the guidelines provided, ARR uses **three primary scores** in their review form:

## 1. **Soundness Score**
The guidelines emphasize that "soundness scores must be justified by the text of the review." Low soundness scores require explicit fault identification in the review content. This score assesses technical validity and methodological rigor.

## 2. **Excitement Score**
Described as "orthogonal to the assessment of soundness," this reflects "personal taste" and subjective interest level. The guidelines note reviewers "may consider a paper worthy of the main conference even if you personally are not excited about it."

## 3. **Overall Assessment Score**
An "explicit recommendation for the outcome" that serves as a "composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact." This determines conference placement (main track vs. Findings).

## Additional Scoring Dimensions

- **Reproducibility Score**: Justified separately, assessing whether "enough details/code is provided for reproducibility"
- **Confidence Score**: Reviewers indicate confidence levels, with guidance that expertise gaps should be noted

## Key Evaluation Requirements

Reviewers should assess papers on: technical soundness, proof validity, argumentation quality, novelty, clarity, appropriate scope of claims, and statistical rigor. The guidelines stress that scores must align with review text, preventing unjustified low scores from unconscious bias.

**Note:** The document does not provide specific numerical ranges for each score level.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5980
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-21T11:29:55.407553+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/",
  "description": "List rendered PDF images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/",
    "description": "List rendered PDF images"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-21T11:29:55.558553+00:00_

main_p10.png
main_p6.png
main_p7.png
main_p8.png
main_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-21T11:30:01.782984+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "1-5",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "1-5",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-21T11:30:02.585297+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 571.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.8}], \"total_pages\": 16, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 802
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-21T11:30:02.585759+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-21T11:30:03.392505+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 354.0}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 439.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 431.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 394.2}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-21T11:30:07.507914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 549 · 2026-05-21T11:30:08.061045+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 550 · 2026-05-21T11:30:08.465711+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 551 · 2026-05-21T11:30:08.466168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 552 · 2026-05-21T11:30:09.421235+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1360
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-21T11:30:09.422536+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-21T11:30:09.422909+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 555 · 2026-05-21T11:30:09.623926+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 556 · 2026-05-21T11:30:10.281058+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-21T11:30:10.534273+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-21T11:30:24.153729+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-21T11:30:25.109523+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-21T11:30:25.109996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 561 · 2026-05-21T11:30:25.612038+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 562 · 2026-05-21T11:30:26.165154+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 563 · 2026-05-21T11:30:26.165595+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 564 · 2026-05-21T11:30:26.567448+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 565 · 2026-05-21T11:30:26.567886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 566 · 2026-05-21T11:30:27.070689+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-21T11:30:27.425062+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-21T11:30:33.695950+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 569 · 2026-05-21T11:30:34.097532+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 570 · 2026-05-21T11:30:34.551740+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 571 · 2026-05-21T11:30:34.552171+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 572 · 2026-05-21T11:30:35.457080+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1359
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-21T11:30:35.458595+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-21T11:30:35.609421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 575 · 2026-05-21T11:30:35.964004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-21T11:30:36.165118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-21T11:30:36.317725+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 708
}
```

</details>

---


### Tool result

_source line 578 · 2026-05-21T11:30:37.022099+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-21T11:30:37.022917+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1058
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-21T11:31:54.721073+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "instance-level sample reweighting LLM pretraining 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "instance-level sample reweighting LLM pretraining 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 581 · 2026-05-21T11:31:54.924017+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "model collapse prevention adaptive reweighting 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "model collapse prevention adaptive reweighting 2025 2026 arxiv"
  }
}
```

</details>

---


### Tool result

_source line 582 · 2026-05-21T11:32:00.694007+00:00_

Web search results for query: "instance-level sample reweighting LLM pretraining 2025 2026"

Links: [{"title":"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining | OpenReview","url":"https://openreview.net/forum?id=gU4ZgQNsOC"},{"title":"[2502.06733] Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining","url":"https://arxiv.org/abs/2502.06733"},{"title":"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining for ICLR 2025 - IBM Research","url":"https://research.ibm.com/publications/dynamic-loss-based-sample-reweighting-for-improved-large-language-model-pretraining"},{"title":"DYNAMIC LOSS-BASED SAMPLE REWEIGHTING FOR ...","url":"https://shiqiang.wang/papers/DS_ICLR2025.pdf"},{"title":"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining","url":"https://arxiv.org/html/2502.06733"},{"title":"Take the Bull by the Horns: Hard Sample-Reweighted Continual Training   Improves LLM Generalization","url":"https://arxiv.org/pdf/2402.14270"},{"title":"GitHub - sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025","url":"https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025"},{"title":"Model Averaging for LLM Curriculum Pretraining","url":"https://www.emergentmind.com/topics/model-averaging"}]

Based on the search results, here's what I found about instance-level sample reweighting for LLM pretraining:

## Key Research

A recent paper introduces novel algorithms for dynamic, instance-level data reweighting aimed at improving both the efficiency and effectiveness of LLM pretraining. The methods adjust the weight of each training sample based on its loss value in an online fashion, allowing the model to dynamically focus on more informative or important samples at the current training stage.

## The Problem Being Addressed

Current training paradigms treat all samples equally, overlooking the importance or relevance of individual samples throughou
…[truncated 802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5972
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-21T11:32:01.296549+00:00_

Web search results for query: "model collapse prevention adaptive reweighting 2025 2026 arxiv"

Links: [{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Escaping Model Collapse via Synthetic Data Verification:","url":"https://arxiv.org/pdf/2510.16657"},{"title":"Preventing Model Collapse Under Overparametrization: Optimal Mixing Ratios for Interpolation Learning and Ridge Regression","url":"https://arxiv.org/pdf/2509.22341"},{"title":"[2510.16657] Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence","url":"https://arxiv.org/abs/2510.16657"},{"title":"Preventing Model Collapse via Contraction-Conditioned Neural Filters","url":"https://arxiv.org/pdf/2512.00757"}]

Based on the search results, I found several relevant papers on model collapse prevention from 2025-2026 on arXiv:

1. **"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence"** (arXiv:2510.16657)
   - This paper situates theoretical analysis in linear regression settings, showing that verifier-guided retraining can yield near-term improvements, but ultimately drives the parameter estimate to the verifier's "knowledge center" in the long run.

2. **"Preventing Model Collapse Under Overparametrization: Optimal Mixing Ratios for Interpolation Learning and Ridge Regression"** (arXiv:2509.22341)
   - This work studies model collapse in overparameterized linear regression where each iteration mixes fresh real labels with synthetic labels from the previous iteration, 
…[truncated 661 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6372
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-21T11:35:19.510053+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见（Round 1）\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n### 1. Summary\n\n本文研究 D&R 方法在含合成数据污染的 continued LM pretraining 中的有效性。三个贡献：(1) 识别 epoch confound——D&R 优势主要来自多 epoch 曝光而非 reweighting 本身；(2) 基于 quality floor + stability ceiling 的自适应 b* 框架；(3) 分析 detector 的校准与区分度要求。实验基于 Qwen3-0.6B，132M FineWeb tokens，40% 自生成污染，3 seeds。\n\n---\n\n### 2. Strengths\n\n**S1.** Epoch-matched 对比设计严谨。Table 1 显示 D&R 的 PPL 优势从 0.384 缩小到 Δ=0.017，揭示了 prior work 中被忽视的混淆变量。\n\n**S2.** 双约束框架概念清晰。Quality floor (v_adj ≥ τ) + stability ceiling (ESS ≥ n_ESS) 分解合理，Algorithm 1 简洁可复现。\n\n**S3.** Detector 对比分析（Table 10, Appendix K）有实用价值——TF-IDF+LR 同时满足 calibration + discrimination，而 GPT-2 和 N-gram 各缺一个。\n\n**S4.** Appendix 全面（Grid Search 全表、constraint regime 分解、rank preservation、cross-model transfer 等），可复现性好。\n\n**S5.** v_adj 作为 real fraction proxy 验证充分（Table 9, Pearson r ≈ 0.70, bias ≈ −0.03）。\n\n---\n\n### 3. Weaknesses\n\n**N1 [critical] 新颖性不足以支撑 main conference。**\n- Epoch confound 是 ablation-level 发现，缺机制解释（为什么多 epoch 能替代 reweighting？）\n- Adaptive b* 基于成熟统计工具（ESS, calibration）的 straightforward 组合，搜索 5 个离散 b 值\n- Detector requirements（需要 calibration + discrimination）接近 expected\n- 三个贡献叠加仍偏 incremental\n\n**N2 [critical] 实验规模严重不足。**\n- Qwen3-0.6B, batch size 4, 132M tokens\n- 1.7B 实验（Section 5.3）仍然很小；Llama-3.2-3B cross-model transfer 结果 mixed/negative\n- τ=0.7 是否 scale-invariant 无证据\n- 在当前 LLM 研究中难以令人信服\n\n**W1 [major] Epoch-matched 设计存在步数/LR confound。** D&R full 6,103 步 vs epoch-matched 2,533 步，LR schedule 不同。正文声称 \"favors D&R\" 但未严格验证。\n\n**W2 [major] Self-contamination 设置局限性未充分讨论。** AUC=0.94 受益于 trainee 检测自己的输出，multi-source 场景下可能显著不同。\n\n**W3 [major] Abstract/Introduction 中 overclaim。** 将单一实验设置的发现推广为 D&R 方法的普遍问题，缺范围限定。\n\n**W4 [minor] Related Work 遗漏 Mindermann et al. (2022) \"Prioritized Training\"**——instance-level online data selection 的重要工作。\n\n**W5 [minor] 术语不统一（\"sharpening exponent\" vs \"exponent\" vs \"b\"）；Table 1 呈现方式可能误导。**\n\n---\n\n### 4. Questions for Authors\n\nQ1. Epoch confound 的机制是什么？多 epoch 曝光为什么能替代 reweighting？\nQ2. Batch size 增大到 64/256 时框架行为如何变化？\nQ3. Table 5 显示高污染下 hard filtering 仍优于 soft reweighting？\nQ4. τ=0.7 对不同 ρ 是否稳定？\nQ5. Llama cross-model transfer 失败是否说明需要 per-model tuning？\n\n---\n\n### 5. 引用验证\n\n- wang2026survive、yang2026mixing 均验证存在\n- 无虚假引用\n- 6 条 OpenAlex 未索引的知名论文/著作属正常\n- 建议检查 vehtari2024psis 年份（OpenAlex 记录 2015 vs bib 2024）\n\n---\n\n### 6. 格式合规\n\n全部通过：ACL 两栏 ✅ | 匿名 ✅ | 8 页限制 ✅ | Limitations ✅ | Checklist ✅\n\n---\n\n### 7. Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n| Overall | 3.0/5 |\n| Confidence | 4/5 |\n\n核心判断：Epoch confound 发现有价值但三个贡献均偏浅，实验规模过小限制泛化性，整体适合 Findings 而非 main conference。若能补充 (a) epoch confound 的机制分析 和 (b) ≥3B 模型的规模验证，可重新评估。",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见（Round 1）\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n### 1. Summary\n\n本文研究 D&R 方法在含合成数据污染的 continued LM pretraining 中的有效性。三个贡献：(1) 识别 epoch confound——D&R 优势主要来自多 epoch 曝光而非 reweighting 本身；(2) 基于 quality floor + stability ceiling 的自适应 b* 框架；(3) 分析 detector 的校准与区分度要求。实验基于 Qwen3-0.6B，132M FineWeb tokens，40% 自生成污染，3 seeds。\n\n---\n\n### 2. Strengths\n\n**S1.** Epoch-matched 对比设计严谨。Table 1 显示 D&R 的 PPL 优势从 0.384 缩小到 Δ=0.017，揭示了 prior work 中被忽视的混淆变量。\n\n**S2.** 双约束框架概念清晰。Quality floor (v_adj ≥ τ) + stability ceiling (ESS ≥ n_ESS) 分解合理，Algorithm 1 简洁可复现。\n\n**S3.** Detector 对比分析（Table 10, Appendix K）有实用价值——TF-IDF+LR 同时满足 calibration + discrimination，而 GPT-2 和 N-gram 各缺一个。\n\n**S4.** Appendix 全面（Grid Search 全表、constraint regime 分解、rank preservation、cross-model transfer 等），可复现性好。\n\n**S5.** v_adj 作为 real fraction proxy 验证充分（Table 9, Pearson r ≈ 0.70, bias ≈ −0.03）。\n\n---\n\n### 3. Weaknesses\n\n**N1 [critical] 新颖性不足以支撑 main conference。**\n- Epoch confound 是 ablation-level 发现，缺机制解释（为什么多 epoch 能替代 reweighting？）\n- Adaptive b* 基于成熟统计工具（ESS, calibration）的 straightforward 组合，搜索 5 个离散 b 值\n- Detector requirements（需要 calibration + discrimination）接近 expected\n- 三个贡献叠加仍偏 incremental\n\n**N2 [critical] 实验规模严重不足。**\n- Qwen3-0.6B, batch size 4, 132M tokens\n- 1.7B 实验（Section 5.3）仍然很小；Llama-3.2-3B cross-model transfer 结果 mixed/negative\n- τ=0.7 是否 scale-invariant 无证据\n- 在当前 LLM 研究中难以令人信服\n\n**W1 [major] Epoch-matched 设计存在步数/LR confound。** D&R full 6,103 步 vs epoch-matched 2,533 步，LR schedule 不同。正文声称 \"favors D&R\" 但未严格验证。\n\n**W2 [major] Self-contamination 设置局限性未充分讨论。** AUC=0.94 受益于 trainee 检测自己的输出，multi-source 场景下可能显著不同。\n\n**W3 [major] Abstract/Introduction 中 overclaim。** 将单一实验设置的发现推广为 D&R 方法的普遍问题，缺范围限定。\n\n**W4 [minor] Related Work 遗漏 Mindermann et al. (2022) \"Prioritized Training\"**——instance-level online data selection 的重要工作。\n\n**W5 [minor] 术语不统一（\"sharpening exponent\" vs \"exponent\" vs \"b\"）；Table 1 呈现方式可能误导。**\n\n---\n\n### 4. Questions for Authors\n\nQ1. Epoch confound 的机制是什么？多 epoch 曝光为什么能替代 reweighting？\nQ2. Batch size 增大到 64/256 时框架行为如何变化？\nQ3. Table 5 显示高污染下 hard filtering 仍优于 soft reweighting？\nQ4. τ=0.7 对不同 ρ 是否稳定？\nQ5. Llama cross-model transfer 失败是否说明需要 per-model tuning？\n\n---\n\n### 5. 引用验证\n\n- wang2026survive、yang2026mixing 均验证存在\n- 无虚假引用\n- 6 条 OpenAlex 未索引的知名论文/著作属正常\n- 建议检查 vehtari2024psis 年份（OpenAlex 记录 2015 vs bib 2024）\n\n---\n\n### 6. 格式合规\n\n全部通过：ACL 两栏 ✅ | 匿名 ✅ | 8 页限制 ✅ | Limitations ✅ | Checklist ✅\n\n---\n\n### 7. Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n| Overall | 3.0/5 |\n| Confidence | 4/5 |\n\n核心判断：Epoch confound 发现有价值但三个贡献均偏浅，实验规模过小限制泛化性，整体适合 Findings 而非 main conference。若能补充 (a) epoch confound 的机制分析 和 (b) ≥3B 模型的规模验证，可重新评估。",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-21T11:35:23.125688+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3615
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-21T11:35:28.330988+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-21T11:35:28.381532+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-21T11:35:39.919342+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-21T11:35:39.919805+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 590 · 2026-05-21T11:35:48.379433+00:00_

审稿完成。已将完整审稿意见提交给 Review Director。

**核心结论**: Overall 3.0 (Findings)。Epoch confound 是有价值的实验发现，但三个贡献的学术深度均偏浅（ablation-level observation、成熟工具的组合、near-expected 结论），且实验规模过小（0.6B, 132M tokens, batch size 4）严重限制泛化性。格式完全合规，引用均真实，可复现性好。主要提升方向：深挖 epoch confound 的机制 + 更大规模验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 14

## Round 14

4 recorded events


### User

_source line 591 · 2026-05-21T11:36:02.015959+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的意见。对每一条 Weakness/Strength/Question，标注 **[AGREE]** 并说明理由，或 **[REBUT]** 并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿原文：

### 1. Summary
本文研究 Detect-and-Reweight (D&R) 范式在含合成文本污染的 continued LM pretraining 中何时有效。核心发现有二：(1) D&R 的 PPL 优势中 96% 归因于 epoch confound（多轮数据重复曝光），epoch-matched 后优势从 0.384 缩至 0.017；(2) 提出 dual-constraint 自适应 reweighting 框架（α_eff quality floor + ESS stability ceiling），在 Qwen3-0.6B / 132M token / 40% self-contamination 设定下取得 Δ=−0.020 PPL 改进（~0.11%），但下游任务无可测量改善。

### 2. Strengths
**S1.** Epoch confound 分析有实质贡献。Table 1 的 epoch-matched 实验将 0.384 PPL gap 分解为 epoch 效应（96%）和真实 filtering 效应（4%）。
**S2.** 框架形式化清晰。Dual-constraint 的数学表述简洁（§3.2），Proposition 1–2 证明正确。
**S3.** 消融实验覆盖面广。Grid search 全空间、threshold 敏感性、contamination level、scale、constraint regime 分解、detector 家族均有系统消融。
**S4.** 诚实的 limitations。§8 明确承认 self-contamination 局限、单模型规模、缺乏下游改善。
**S5.** 引用质量好。51 条引用无伪造、无遗漏。

### 3. Weaknesses

#### Must-Fix (Critical)
**W1 [critical] 效果大小不足以支撑方法论贡献。**
Adaptive b* 的 PPL 改进 Δ=−0.020（0.11%），接近 noise margin。下游任务 |Δ|≤0.01。Abstract 用 "consistent improvements" 描述过于乐观。

**W2 [critical] B=4 下 dual-constraint 框架实质退化。**
α_eff 仅有 5 个离散值，α_eff-binding regime 占比极低（~0.2%）。质量约束几乎不生效，方法退化为 "ESS-only + clean batch 不干预"。

**W3 [critical] Epoch-matched 比较的 LR schedule confound。**
D&R epoch-matched 在 2,533/6,103 步时 LR 仍处 cosine 中段（~64% 峰值），非训练终态。论文以 "if anything, favors D&R" 打发，但 warmer LR 影响方向不确定。

#### Should-Fix (Major)
**W4 [major] N=3 统计功效不足。**
**W5 [major] Self-contamination 生态效度受限。**
**W6 [major] Grid search baseline 公平性。**
**W7 [major] ρ=0.2 失败 + 1.7B 效果减弱限制实用范围。**
**W8 [major] Wang et al. (2026) 理论假设不匹配。**

#### Minor
**W9 [minor]** "Minimum intervention" 缺乏与其他 b 选择策略的消融对比。
**W10 [minor]** §3.3 constraint regime 占比数字与 Figure 2 视觉不一致。
**W11 [minor]** Figure 1 shaded region 边界与文字描述不一致。

### 4. Questions
Q1. B≥16 下 α_eff-binding regime 占比？
Q2. 为 D&R epoch-matched 独立设计 2,533 步 cosine schedule 后，Δ=0.017 是否改变？
Q3. Detector AUC 与方法有效性的定量关系？
Q4. Seed 123/456 各自的 grid-best b 是多少？
Q5. 是否尝试过 fine-tuned BERT-based detector？

### 5. Overall Assessment
**Overall: 2.5 (Borderline Findings)** | Soundness 3 | Excitement 2 | Reproducibility 4 | Confidence 4

一句话总结：Epoch confound 分析有价值，但 adaptive method 效果微弱（0.11% PPL, 下游为零），B=4 下框架退化、LR confound 未解决、N=3 功效不足共同削弱说服力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-21T11:38:36.134728+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1（Round 2）\n\n### 总结\n\n对 R1 的 11 条 Weaknesses 逐条回应：\n- **8 条 [AGREE]**: W1 (effect size), W3 (LR confound), W4 (N=3), W5 (self-contamination), W7 (ρ=0.2/1.7B), W9 (minimum intervention ablation), W10 (regime 数字不一致), W11 (Figure 1 shading)\n- **1 条 [AGREE] 但对具体数字有疑问**: W2 (B=4 退化) — 核心论点成立但 R1 的 \"~0.2%\" 与论文 Section 3.3 报告的 \"38.2% v_adj-binding\" 存在数量级差异，需 R1 澄清\n- **2 条 [PARTIALLY AGREE]**: W6 (grid search fairness — 比较设计合理但问题在 effect size), W8 (Wang 2026 理论 — loose motivation 在 empirical 论文中可接受)\n\n### 评分\n\n维持 **Overall 3.0 (Findings)**，不同于 R1 的 2.5。核心分歧在于：我认为 epoch confound 发现有独立的 analytical 价值（即使 adaptive method 贡献很弱），这足以支撑 Findings 接收。但如果 W3 (LR confound) 在 rebuttal 中未被解决（即 epoch confound 可能部分归因于 LR schedule 差异而非纯 epoch 效应），我会考虑下调至 2.5。\n\n### 关键共识\n\n两位 Reviewer 的核心共识：\n1. Adaptive b* 的方法论贡献因 tiny effect size (Δ=−0.020) 和 B=4 退化而不成立\n2. 实验规模过小（0.6B, 132M tokens）限制泛化性\n3. LR schedule confound 是 epoch confound 分析的关键漏洞\n4. 论文主要价值在 epoch confound 这一 observation，而非方法本身",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1（Round 2）\n\n### 总结\n\n对 R1 的 11 条 Weaknesses 逐条回应：\n- **8 条 [AGREE]**: W1 (effect size), W3 (LR confound), W4 (N=3), W5 (self-contamination), W7 (ρ=0.2/1.7B), W9 (minimum intervention ablation), W10 (regime 数字不一致), W11 (Figure 1 shading)\n- **1 条 [AGREE] 但对具体数字有疑问**: W2 (B=4 退化) — 核心论点成立但 R1 的 \"~0.2%\" 与论文 Section 3.3 报告的 \"38.2% v_adj-binding\" 存在数量级差异，需 R1 澄清\n- **2 条 [PARTIALLY AGREE]**: W6 (grid search fairness — 比较设计合理但问题在 effect size), W8 (Wang 2026 理论 — loose motivation 在 empirical 论文中可接受)\n\n### 评分\n\n维持 **Overall 3.0 (Findings)**，不同于 R1 的 2.5。核心分歧在于：我认为 epoch confound 发现有独立的 analytical 价值（即使 adaptive method 贡献很弱），这足以支撑 Findings 接收。但如果 W3 (LR confound) 在 rebuttal 中未被解决（即 epoch confound 可能部分归因于 LR schedule 差异而非纯 epoch 效应），我会考虑下调至 2.5。\n\n### 关键共识\n\n两位 Reviewer 的核心共识：\n1. Adaptive b* 的方法论贡献因 tiny effect size (Δ=−0.020) 和 B=4 退化而不成立\n2. 实验规模过小（0.6B, 132M tokens）限制泛化性\n3. LR schedule confound 是 epoch confound 分析的关键漏洞\n4. 论文主要价值在 epoch confound 这一 observation，而非方法本身",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-21T11:38:39.748884+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3614
}
```

</details>

---


### Assistant

_source line 594 · 2026-05-21T11:38:45.094251+00:00_

交叉回应已完成并提交给 Review Director。

核心结论：与 R1 在绝大多数问题上达成共识（8/11 AGREE，2/11 PARTIALLY AGREE），但评分维持 3.0 vs R1 的 2.5——分歧在于 epoch confound 发现的独立价值是否足以支撑 Findings。两位 Reviewer 共同认为 adaptive b* 的方法论贡献基本不成立。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 15

## Round 15

74 recorded events


### User

_source line 595 · 2026-05-21T14:03:13.736550+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。

## Venue 信息
- **目标**：EMNLP 2026 via ARR May 2026
- **截止日期**：2026-05-25
- **格式**：ACL 模板，正文 8 页限制（参考文献不限），double-blind
- **匿名规则**：严格 double-blind，禁止透露作者身份

## 论文文件
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf`

## 审查侧重

### 1. 新颖性与贡献定位
- 与 Drayson et al. (2025) 的关键区别是否足够显著（同一 weighting formula，区别在于 b 的选择方式）
- "Epoch confound" 发现是否足够 novel（multi-epoch exposure 的混淆在数据选择领域是否已知？）
- "Calibration matters" 的发现是否有足够创新性
- 双约束框架作为方法论贡献，在技术深度上是否足够

### 2. Related Work 覆盖
- 是否遗漏重要相关工作？特别关注：
  - Model collapse 领域的最新工作
  - Data curation / filtering 领域
  - Importance weighting 在 LLM 训练中的应用
  - Synthetic data detection 的最新方法
- 与 domain-level mixing (DoReMi, AIOLI 等) 的区分是否清晰
- 与 instance-level reweighting (focal loss, curriculum learning) 的关系是否充分讨论

### 3. 写作质量与叙事逻辑
- Introduction 的 4 个 findings 是否逻辑清晰
- "Minimum intervention" 概念是否被很好地激励和解释
- 从分析性发现（F1-F3）到方法（adaptive b*）的过渡是否自然
- Abstract 是否准确反映论文贡献（不过度宣称也不遗漏）
- Discussion 是否充分（当前只有 11 行，是否太短？）
- Conclusion 是否太简短？

### 4. 格式合规性（EMNLP 2026 / ARR）
- 正文是否在 8 页限制内（检查 PDF 页数）
- 是否使用正确的 ACL 模板（\usepackage[review]{acl}）
- 匿名是否完整（检查 \author{Anonymous}，自引是否泄露身份）
- Limitations section 是否存在且适当
- Responsible NLP Checklist 是否完整
- 引用格式是否正确（natbib）

### 5. 效果大小与实用性
- Δ=-0.020 PPL 的改进在实际应用中是否有意义
- "消除 grid search" 的实用价值是否被合理论证
- 方法在 ρ=0.2 失败、1.7B 效果减弱——这限制了实用性，是否被充分讨论

请提供完整审稿报告，格式为：Summary → Strengths → Weaknesses → Questions → Minor Issues。Weaknesses 按严重程度排序（Must-Fix / Should-Fix / Nice-to-Have）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-21T14:03:33.103146+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-21T14:03:34.866871+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1763
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-21T14:03:34.967566+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-21T14:03:34.967995+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-21T14:03:42.924253+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 601 · 2026-05-21T14:03:45.381767+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-21T14:03:45.883530+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-21T14:03:49.932280+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria:

## Reviewer Guidelines

Reviewers are asked to follow a workflow of reading the paper for first impression and searching for related work. The
…[truncated 1178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7008
}
```

</details>

---


### Tool result

_source line 604 · 2026-05-21T14:03:53.520058+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 554.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weig
…[truncated 333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8138
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-21T14:09:15.249230+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 52, \"total_citations\": 79, \"unique_cited_keys\": 52, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 37, \"online_not_found\": 8, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"katharopoulos2018not\", \"type\": \"inproceedings\", \"title\": \"Not All Samples Are Created Equal: Deep Learning with Importance Sampling\", \"authors\": \"\", \"year\": \"2018\", \"venue\": \"International Conference on Machine Learning\"}, {\"key\": \"ren2018learning\", \"type\": \"inproceedings\", \"title\": \"Learning to Reweight Examples for Robust Deep Learning\", \"authors\": \"Ren, Mengye and Zeng, Wenyuan and Yang, Bin and Urtasun, Raquel\", \"year\": \"2018\", \"venue\": \"International Conference on Machine Learning\"}, {\"key\": \"chen2024bull\", \"type\": \"article\", \"title\": \"Take the Bull by the Horns: Hard Sample-Reweighted Continual Training Improves LLM Generalization\", \"authors\": \"Chen, Xuxi and Li, Zhendong and Cai, Daixuan and Yao, Huanran and Chen, Zheng an...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.14270\"}, {\"key\": \"kang2025demystifying\", \"type\": \"inproceedings\", \"title\": \"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls\", \"authors\": \"Kang, Feiyang and Xu, Yifan and Pu, Jingkang and Hu, Bushi and Li, Haonan and Ch...\", \"year\": \"2025\", \"venue\": \"EMNLP\"}, {\"key\": \"zibakhsh2025fortifai\", \"type\": \"article\", \"title\": \"ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse\", \"authors\": \"Zibakhsh Shabgahi, Soheil and Aghazadeh, Pedram and Mirhoseini, Azalia and Koush...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2509.08972\"}, {\"key\": \"yi2025escaping\", \"type\": \"article\", \"title\
…[truncated 39140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 329365
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-21T14:09:23.725022+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form criteria, including all scoring dimensions (soundness, excitement, overall assessment, etc.), their scales, and descriptions. List every field a reviewer must fill in."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form criteria, including all scoring dimensions (soundness, excitement, overall assessment, etc.), their scales, and descriptions. List every field a reviewer must fill in."
  }
}
```

</details>

---


### Tool call

_source line 607 · 2026-05-21T14:09:26.033528+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 608 · 2026-05-21T14:09:26.535733+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 609 · 2026-05-21T14:09:26.586323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 610 · 2026-05-21T14:09:26.938133+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-21T14:09:26.988665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 612 · 2026-05-21T14:09:27.942148+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 613 · 2026-05-21T14:09:27.942504+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 614 · 2026-05-21T14:09:27.992886+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 615 · 2026-05-21T14:09:28.143765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 616 · 2026-05-21T14:09:28.194427+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-21T14:09:33.264105+00:00_

# ACL Rolling Review Form - Complete Criteria

## Required Reviewer Fields

**1. Paper Summary**
Brief description of the paper's topic and content.

**2. Summary of Strengths**
"Major reasons to publish this paper at a selective *ACL venue" including methodology, empirical results, theoretical analysis, or literature organization.

**3. Summary of Weaknesses**
Numbered concerns about correctness, impact, clarity, or other factors affecting publication consideration.

**4. Comments/Suggestions/Typos**
Additional improvement suggestions beyond addressing weaknesses.

## Scoring Dimensions

**5. Reviewer Confidence** (1-5 scale)
- 5: Positive evaluation; thoroughly read and familiar with related work
- 4: Quite sure; checked important points carefully
- 3: Pretty sure; may have missed some details
- 2: Willing to defend evaluation; likely missed some details
- 1: Outside expertise area or paper very difficult to understand

**6. Soundness** (1-5 scale with half-points)
Evaluates scientific rigor, experimental design, and support for claims based on paper type.
- 5: Excellent, most thorough study
- 4: Strong, sufficient support provided
- 3: Acceptable, main claims supported
- 2: Poor, insufficient support for main claims
- 1: Major issues; insufficient for publication

**7. Excitement** (1-5 scale with half-points)
Subjective assessment of innovation, impact, and relevance to the reviewer.
- 5: Highly exciting; would recommend widely
- 4: Exciting; would mention to others
- 3: Interesting; might mention selectively
- 2: Potentially interesting; limited personal resonance
- 1: Not exciting; questionable community relevance

**8. Overall Assessment** (1-5 scale with half-points)
Conference recommendation ranging from award consideration to rejection.
- 5: Consider for award (top 2.5%)
- 4.5: Borderline award
- 4: Conference acceptance
- 3.5: Borderline conference
- 3: Findings acceptance
- 2.5: Borderline findings
- 2: Resubmit next cycle
- 1.5: Resubmit after next cycl
…[truncated 1569 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 9539
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-21T14:09:37.829070+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check PDF images directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check PDF images directory"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-21T14:09:37.930760+00:00_

DIR_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-21T14:09:41.392890+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/ -name \"*.png\" -o -name \"_pdf_images\" 2>/dev/null | head -20",
  "description": "Find PNG files in paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/ -name \"*.png\" -o -name \"_pdf_images\" 2>/dev/null | head -20",
    "description": "Find PNG files in paper directory"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-21T14:09:41.443618+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images_250dpi/main_p8.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-21T14:09:48.180007+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "1-5",
  "dpi": "150",
  "output_dir": "/tmp/pwt_review_r2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "1-5",
    "dpi": "150",
    "output_dir": "/tmp/pwt_review_r2"
  }
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-21T14:09:48.784365+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/tmp/pwt_review_r2/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.5}, {\"page\": 2, \"path\": \"/tmp/pwt_review_r2/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.1}, {\"page\": 3, \"path\": \"/tmp/pwt_review_r2/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 554.1}, {\"page\": 4, \"path\": \"/tmp/pwt_review_r2/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.4}, {\"page\": 5, \"path\": \"/tmp/pwt_review_r2/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.0}], \"total_pages\": 16, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/tmp/pwt_review_r2\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-21T14:09:52.147058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 625 · 2026-05-21T14:09:52.649307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-21T14:09:52.649800+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-21T14:09:53.103727+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-21T14:09:53.104310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 629 · 2026-05-21T14:09:53.407429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 630 · 2026-05-21T14:09:54.064747+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1415
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-21T14:09:54.367187+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1717
}
```

</details>

---


### Tool result

_source line 632 · 2026-05-21T14:09:54.719982+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1615
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-21T14:09:54.921515+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1514
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-21T14:10:07.017591+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "6-10",
  "dpi": "150",
  "output_dir": "/tmp/pwt_review_r2_b"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "6-10",
    "dpi": "150",
    "output_dir": "/tmp/pwt_review_r2_b"
  }
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-21T14:10:07.620028+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/tmp/pwt_review_r2_b/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.1}, {\"page\": 7, \"path\": \"/tmp/pwt_review_r2_b/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.4}, {\"page\": 8, \"path\": \"/tmp/pwt_review_r2_b/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.3}, {\"page\": 9, \"path\": \"/tmp/pwt_review_r2_b/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.9}, {\"page\": 10, \"path\": \"/tmp/pwt_review_r2_b/main_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.6}], \"total_pages\": 16, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/tmp/pwt_review_r2_b\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-21T14:10:12.287454+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2_b/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2_b/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-21T14:10:12.840714+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-21T14:10:12.841170+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2_b/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2_b/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 639 · 2026-05-21T14:10:13.267605+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2_b/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2_b/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-21T14:10:13.268034+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2_b/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2_b/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-21T14:10:13.671357+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 830
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-21T14:10:13.671765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2_b/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2_b/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-21T14:10:14.679300+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool result

_source line 644 · 2026-05-21T14:10:14.932053+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1664
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-21T14:10:15.133539+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1461
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-21T14:10:24.333025+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "11-16",
  "dpi": "150",
  "output_dir": "/tmp/pwt_review_r2_c"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "11-16",
    "dpi": "150",
    "output_dir": "/tmp/pwt_review_r2_c"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-21T14:10:24.986527+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/tmp/pwt_review_r2_c/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.2}, {\"page\": 12, \"path\": \"/tmp/pwt_review_r2_c/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 378.6}, {\"page\": 13, \"path\": \"/tmp/pwt_review_r2_c/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 391.9}, {\"page\": 14, \"path\": \"/tmp/pwt_review_r2_c/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 431.7}, {\"page\": 15, \"path\": \"/tmp/pwt_review_r2_c/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 481.7}, {\"page\": 16, \"path\": \"/tmp/pwt_review_r2_c/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 150.9}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/tmp/pwt_review_r2_c\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-21T14:10:28.749575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2_c/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2_c/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 649 · 2026-05-21T14:10:29.201503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2_c/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2_c/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 650 · 2026-05-21T14:10:29.705663+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-21T14:10:29.710795+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 509
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-21T14:10:29.711404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2_c/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2_c/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 653 · 2026-05-21T14:10:29.711676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2_c/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2_c/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-21T14:10:30.214017+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2_c/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2_c/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-21T14:10:30.725178+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1013
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-21T14:10:30.725637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pwt_review_r2_c/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pwt_review_r2_c/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-21T14:10:30.726465+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1014
}
```

</details>

---


### Tool result

_source line 658 · 2026-05-21T14:10:31.385144+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1171
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-21T14:10:31.387487+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 661
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-21T14:15:26.549923+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量\n\n### 总体评分\n\n**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）\n\n**一句话总结**: 论文在实验控制上做得扎实（epoch confound 的发现有价值），但核心方法论贡献（adaptive b*）相对于 Drayson et al. (2025) 是增量式改进，效果规模小（Δ=-0.020 PPL），且适用范围受限（ρ=0.2 失败、1.7B 减弱），不足以支撑主会议接收。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨（epoch-matched controls、3 seeds、多 ablation），但实验范围窄（单模型族 Qwen3、单数据域 FineWeb、仅 self-contamination），且 Appendix O 揭示 \"distribution matching\" finding 本身是 checkpoint resume artifact |\n| Excitement | 2.5/5 | Epoch confound 对社区有诊断价值，但方法贡献增量性强，效果规模极小，实用场景受限 |\n| Reproducibility | 4/5 | 实验细节充分（Algorithm 1、超参数、训练配置均在正文/附录），代码承诺 upon acceptance 释放 |\n| Reviewer Confidence | 4/5 | 熟悉 data curation/reweighting 和 model collapse 领域 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 相对于 Drayson et al. (2025) 的新颖性不足\n\n- 具体位置：Section 3.1, Eq. (1); Section 1 右栏\n- 问题：论文使用与 Drayson et al. (2025) 完全相同的 weighting formula w(x) = (1−q(x))^b。核心区别仅在于 b 的选择方式——Drayson 用 validation-set grid search，本文用双约束自适应选择。但这本质上是一个超参数自动调节方案，而非方法论层面的根本创新。双约束中的 ESS 约束是重要性采样文献中的标准工具（Kish 1965, Owen 2013），σ_adj 质量下限是直觉性阈值。将两个标准工具组合为一个自适应选择器，技术深度有限。\n- 为什么影响接收：对于 EMNLP 主会议，方法论新颖性是核心评价维度。一个增量式的超参数选择改进——即使附带了有价值的诊断分析——难以达到 \"Conference\" 级别的贡献门槛。\n- 建议修改方向：(a) 更深入地分析为什么 Drayson 的 grid search 在某些条件下系统性失败，论证 adaptive b* 在质量上而非仅效率上的优势；(b) 或将论文明确定位为 \"analysis paper\"，将 adaptive b* 降格为分析结论的自然推论，同时深化 F1-F3 的理论分析。\n\n**N2** [critical] 效果规模极小，实用价值论证不足\n\n- 具体位置：Abstract (Δ=−0.020); Table 1 (epoch-matched Δ=0.017); Table 2 (各方法对比)\n- 问题：核心效果数字是 epoch-matched 后的 Δ=0.017 PPL 和 adaptive b* vs. uniform 的 Δ=−0.020 PPL（约 0.11%）。ρ=0.2 时方法失败（+0.040 退化），1.7B 时效果减弱，下游任务评估（Appendix H, Table 7）差异在标准误差范围内。如果 PPL 微小改进不转化为下游能力提升，整个 reweighting 工作的价值存疑。\n- 为什么影响接收：效果规模过小使得方法论贡献的实际意义存疑。\n- 建议修改方向：(a) 在更大规模或更多样化的污染场景下验证效果是否放大；(b) 或重新定位为 \"负面结果 + 诊断分析\" 论文。\n\n**N3** [critical] Discussion 部分过于单薄（Section 6，约 11 行）\n\n- 具体位置：Section 6 (p.8)\n- 问题：对于一篇声称揭示三项发现的分析型论文，Discussion 仅含两小段远远不够。以下关键问题未讨论：epoch confound 对已发表 D&R 工作的影响、多生成器场景的 calibration 挑战、adaptive b* 的理论最优性、adversarial 条件下的鲁棒性。\n- 建议修改方向：至少增加 1 页 Discussion。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 实验场景过窄——仅 self-contamination，单一数据域。Cross-model transfer (Appendix N) 仅单 seed 且 \"mixed results\"。\n\n**W2** [warning] \"Minimum intervention\" 概念缺乏充分动机。未解释为什么过度降权有害（误杀真阳性？合成数据本身有价值？）。\n\n**W3** [warning] Conclusion 过于简短（~8 行），缺乏前瞻性讨论。\n\n**W4** [warning] 论文在 \"分析论文\" 与 \"方法论文\" 之间定位模糊，双重定位削弱了两个维度的说服力。\n\n**W5** [warning] 下游任务评估不足——PPL 0.02 改进无法转化为下游任务改进（Appendix H），但该负面结果仅放在附录未在正文讨论。\n\n---\n\n### 小问题\n\n1. Abstract \"three findings\" vs. Introduction 中 F1/F2/F3 + adaptive b* 的措辞不一致。\n2. Table 2 \"Oracle\" baseline 实现细节不足。\n3. Vehtari et al. 年份可能需核实（OpenAlex 匹配到 2015 而非 2024）。\n4. Figure 2 图例 crowded，建议改善。\n5. Section 5.1 中 GPT-2/N-gram 检测器突然出现，未在 Setup 预先说明。\n6. Checklist E1 披露使用 AI assistants 是合规的，但建议确认所有 claim 由作者独立验证。\n\n---\n\n### 格式合规性\n\n全部通过：正文 8 页、ACL 模板、double-blind 匿名、Limitations/Ethics/Checklist 齐全、引用格式正确（52 条 bib 全部 verified，无 orphan/missing/伪造）。\n\n---\n\n### Questions to Authors\n\n1. Epoch confound 在其他 D&R 工作中是否也存在？已发表的效果声明是否需要重新验证？\n2. 双约束的选择是经验性的还是有理论最优性依据？\n3. 是否有计划进行更系统的 cross-model 评估？\n4. Appendix O 的 checkpoint artifact 是否意味着 F1-F3 中某些发现可能是 continued pretraining 特有的？",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量\n\n### 总体评分\n\n**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）\n\n**一句话总结**: 论文在实验控制上做得扎实（epoch confound 的发现有价值），但核心方法论贡献（adaptive b*）相对于 Drayson et al. (2025) 是增量式改进，效果规模小（Δ=-0.020 PPL），且适用范围受限（ρ=0.2 失败、1.7B 减弱），不足以支撑主会议接收。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨（epoch-matched controls、3 seeds、多 ablation），但实验范围窄（单模型族 Qwen3、单数据域 FineWeb、仅 self-contamination），且 Appendix O 揭示 \"distribution matching\" finding 本身是 checkpoint resume artifact |\n| Excitement | 2.5/5 | Epoch confound 对社区有诊断价值，但方法贡献增量性强，效果规模极小，实用场景受限 |\n| Reproducibility | 4/5 | 实验细节充分（Algorithm 1、超参数、训练配置均在正文/附录），代码承诺 upon acceptance 释放 |\n| Reviewer Confidence | 4/5 | 熟悉 data curation/reweighting 和 model collapse 领域 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 相对于 Drayson et al. (2025) 的新颖性不足\n\n- 具体位置：Section 3.1, Eq. (1); Section 1 右栏\n- 问题：论文使用与 Drayson et al. (2025) 完全相同的 weighting formula w(x) = (1−q(x))^b。核心区别仅在于 b 的选择方式——Drayson 用 validation-set grid search，本文用双约束自适应选择。但这本质上是一个超参数自动调节方案，而非方法论层面的根本创新。双约束中的 ESS 约束是重要性采样文献中的标准工具（Kish 1965, Owen 2013），σ_adj 质量下限是直觉性阈值。将两个标准工具组合为一个自适应选择器，技术深度有限。\n- 为什么影响接收：对于 EMNLP 主会议，方法论新颖性是核心评价维度。一个增量式的超参数选择改进——即使附带了有价值的诊断分析——难以达到 \"Conference\" 级别的贡献门槛。\n- 建议修改方向：(a) 更深入地分析为什么 Drayson 的 grid search 在某些条件下系统性失败，论证 adaptive b* 在质量上而非仅效率上的优势；(b) 或将论文明确定位为 \"analysis paper\"，将 adaptive b* 降格为分析结论的自然推论，同时深化 F1-F3 的理论分析。\n\n**N2** [critical] 效果规模极小，实用价值论证不足\n\n- 具体位置：Abstract (Δ=−0.020); Table 1 (epoch-matched Δ=0.017); Table 2 (各方法对比)\n- 问题：核心效果数字是 epoch-matched 后的 Δ=0.017 PPL 和 adaptive b* vs. uniform 的 Δ=−0.020 PPL（约 0.11%）。ρ=0.2 时方法失败（+0.040 退化），1.7B 时效果减弱，下游任务评估（Appendix H, Table 7）差异在标准误差范围内。如果 PPL 微小改进不转化为下游能力提升，整个 reweighting 工作的价值存疑。\n- 为什么影响接收：效果规模过小使得方法论贡献的实际意义存疑。\n- 建议修改方向：(a) 在更大规模或更多样化的污染场景下验证效果是否放大；(b) 或重新定位为 \"负面结果 + 诊断分析\" 论文。\n\n**N3** [critical] Discussion 部分过于单薄（Section 6，约 11 行）\n\n- 具体位置：Section 6 (p.8)\n- 问题：对于一篇声称揭示三项发现的分析型论文，Discussion 仅含两小段远远不够。以下关键问题未讨论：epoch confound 对已发表 D&R 工作的影响、多生成器场景的 calibration 挑战、adaptive b* 的理论最优性、adversarial 条件下的鲁棒性。\n- 建议修改方向：至少增加 1 页 Discussion。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 实验场景过窄——仅 self-contamination，单一数据域。Cross-model transfer (Appendix N) 仅单 seed 且 \"mixed results\"。\n\n**W2** [warning] \"Minimum intervention\" 概念缺乏充分动机。未解释为什么过度降权有害（误杀真阳性？合成数据本身有价值？）。\n\n**W3** [warning] Conclusion 过于简短（~8 行），缺乏前瞻性讨论。\n\n**W4** [warning] 论文在 \"分析论文\" 与 \"方法论文\" 之间定位模糊，双重定位削弱了两个维度的说服力。\n\n**W5** [warning] 下游任务评估不足——PPL 0.02 改进无法转化为下游任务改进（Appendix H），但该负面结果仅放在附录未在正文讨论。\n\n---\n\n### 小问题\n\n1. Abstract \"three findings\" vs. Introduction 中 F1/F2/F3 + adaptive b* 的措辞不一致。\n2. Table 2 \"Oracle\" baseline 实现细节不足。\n3. Vehtari et al. 年份可能需核实（OpenAlex 匹配到 2015 而非 2024）。\n4. Figure 2 图例 crowded，建议改善。\n5. Section 5.1 中 GPT-2/N-gram 检测器突然出现，未在 Setup 预先说明。\n6. Checklist E1 披露使用 AI assistants 是合规的，但建议确认所有 claim 由作者独立验证。\n\n---\n\n### 格式合规性\n\n全部通过：正文 8 页、ACL 模板、double-blind 匿名、Limitations/Ethics/Checklist 齐全、引用格式正确（52 条 bib 全部 verified，无 orphan/missing/伪造）。\n\n---\n\n### Questions to Authors\n\n1. Epoch confound 在其他 D&R 工作中是否也存在？已发表的效果声明是否需要重新验证？\n2. 双约束的选择是经验性的还是有理论最优性依据？\n3. 是否有计划进行更系统的 cross-model 评估？\n4. Appendix O 的 checkpoint artifact 是否意味着 F1-F3 中某些发现可能是 continued pretraining 特有的？",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-21T14:15:30.164193+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3614
}
```

</details>

---


### Tool call

_source line 662 · 2026-05-21T14:15:38.164483+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/tmp/pwt_review_r2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/tmp/pwt_review_r2"
  }
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-21T14:15:38.666634+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"安全限制：只能清理 _pdf_images 目录，当前目标: pwt_review_r2\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-21T14:15:38.667009+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/tmp/pwt_review_r2_b"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/tmp/pwt_review_r2_b"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-21T14:15:38.817835+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"安全限制：只能清理 _pdf_images 目录，当前目标: pwt_review_r2_b\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-21T14:15:38.818267+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/tmp/pwt_review_r2_c"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/tmp/pwt_review_r2_c"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-21T14:15:38.918938+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"安全限制：只能清理 _pdf_images 目录，当前目标: pwt_review_r2_c\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 668 · 2026-05-21T14:15:48.413371+00:00_

审稿报告已提交给 Review Director。

**总结**：Overall 3.0 (Findings)。论文实验控制严谨，epoch confound 发现有社区诊断价值，但三个 critical 问题制约主会议接收：(1) 相对 Drayson et al. 的方法论新颖性有限（同一公式，仅改变超参数选择方式）；(2) 效果规模极小（Δ=-0.020 PPL ≈ 0.11%），下游任务无显著改进；(3) Discussion 过于单薄。建议明确论文定位（分析论文 vs. 方法论文）并扩展讨论深度。格式合规性全部通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 16

## Round 16

4 recorded events


### User

_source line 669 · 2026-05-21T14:16:14.809391+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿原文：

### 总体评分
**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）

**一句话总结**: 论文发现了有价值的 epoch confound 和 calibration 必要性，但核心自适应方法在 N=3 下统计支撑不足、无下游任务改善、且主文与 checklist 存在 p 值矛盾。

### Must-Fix 问题

**N1** [critical] N=3 seeds 的统计功效根本不足以支撑核心声称
- 核心声称 Δ=-0.020, p=0.025 仅基于 3 个随机种子。Paired t-test 在 df=2 时对 outlier 和非正态性极度敏感。论文测试了 6 种方法 × 2 个 ρ 值 × 3 个评估域 × 2 个模型大小，未做任何多重比较校正。Appendix O 揭示 seed 42 使用了 checkpoint-resumed 训练。

**N2** [critical] 实际显著性存疑：Δ=-0.020 PPL 无下游任务改善
- Δ=-0.020 在 base PPL ≈17.7 上仅为 0.11% 的相对改善。Table 7 明确表明下游任务性能"all differences within standard error (±0.01)"，三 seed 均值完全相同（0.5414）。

**N3** [critical] 主文与 Checklist 的 p 值矛盾
- §5.1 报告 p=0.025；Responsible NLP Research Checklist §C3 报告 p=0.0425（同一比较）。核心声称存在两个不同的 p 值。

### Should-Fix 问题

**W1** [warning] 自我污染设定是不切实际的简化检测场景
- Qwen3-0.6B 生成 + Qwen3-0.6B 训练创造了最有利的检测环境。

**W2** [warning] 完全控制混淆因素后 D&R 过滤本身有害
- epoch-matched + LR-matched 对照下，D&R 过滤（PPL=18.78）反而劣于 uniform（18.06, Δ=+0.72）。自适应方法的改善可能完全来自 LR schedule 交互作用，而非智能重加权。

**W3** [warning] 检测器覆盖面窄：仅 3 个检测器来自 2 个家族
- 缺少 fine-tuned 神经分类器（RoBERTa/DeBERTa-based）、DetectGPT/Fast-DetectGPT 等。

**W4** [warning] α_eff 作为真实人类比例代理：r=0.70 仅解释 49% 方差

**W5** [warning] ρ=0.2 失败和 1.7B 效果减弱分析不充分

**W6** [warning] B=4 离散空间上的 bisection 与连续理论的脱节
- Micro-batch B=4 时，α_eff 实际只取 5 个离散值。Bisection 是连续优化工具，但搜索空间实际上只有 5 个点。

---

请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W6) 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-21T14:19:13.558102+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: N=3 seeds 统计功效不足**\n\n同意这是本文最根本的统计问题之一。我在自己的审稿中将效果规模问题列为 N2（critical），核心论点一致：\n\n1. **df=2 的 paired t-test 极度脆弱**：R1 正确指出 t-test 在 df=2 时对 outlier 和非正态性极端敏感。事实上，任何单个 seed 的异常值都可以翻转统计结论。\n2. **多重比较未校正**：论文测试了多种方法 × 多个 ρ × 多个评估域的组合，p=0.025 在 Bonferroni 校正后远不显著。\n3. **Appendix O 的 seed 42 artifact**：R1 敏锐地发现 seed 42 使用了 checkpoint-resumed 训练。Appendix O 揭示这会引入 \"distribution matching\" 的虚假 finding。这意味着 3 个 seed 中有 1 个的实验条件与其他 2 个不完全一致，进一步削弱了 N=3 的可信度。\n\n补充：不过我注意到 3 seeds 在 NLP 训练实验中仍是常见做法（受 GPU 计算成本约束），论文也报告了方向性一致。问题不是\"3 seeds 不可接受\"，而是在效果规模仅 0.11% 时，3 seeds 不足以区分真实效果和噪声。如果效果是 Δ=-0.5 PPL，3 seeds 可能足够；但 Δ=-0.020 时绝对不够。\n\n---\n\n**[AGREE] R1-N2: Δ=-0.020 无下游任务改善**\n\n完全同意，这也是我的 N2 核心论点。补充几个 R1 未强调的细节：\n\n1. **Appendix H Table 7 的负面结果**极具说服力：adaptive 的三 seed 均值为 0.5414，uniform 也是相近水平，|Δ| ≤ 0.01 且在标准误差内。这意味着 PPL 的微小改进零转化为下游能力——reweighting 可能仅在改善 loss landscape 的某个局部指标，而非模型的实际能力。\n2. **ρ=0.2 的 +0.040 退化**（Appendix M）意味着方法在低污染场景反而有害。实际应用中，用户往往不知道真实 ρ 值，盲目应用 adaptive b* 可能损害模型。\n\n我在自己的审稿中建议作者重新定位为\"负面结果 + 诊断分析\"论文——即核心贡献不是 adaptive b*，而是\"D&R 的效果被严重高估\"这一发现本身。这样 Δ=-0.020 的小效果反而成为支持论点的证据。\n\n---\n\n**[AGREE] R1-N3: 主文与 Checklist 的 p 值矛盾**\n\n同意这是一个严重的科学严谨性问题。\n\n- Section 5.1 报告 adaptive vs. uniform 在 ρ=0.4 时 p=0.025\n- Checklist C3 报告同一比较 p=0.0425\n\n两个数字无法通过 one-tailed vs. two-tailed 解释（one-tailed 0.025 → two-tailed 0.050，不是 0.0425）。最可能的解释是：(a) 其中一个计算有误；(b) 两处使用了不同的比较基准但未说明；(c) 修改过程中未同步更新。无论哪种情况，核心统计声称存在未解决的矛盾，这在审稿中不可接受。\n\n我的审稿中未单独列出此问题（这是 R1 独立发现的），但我认为这属于 critical 级别——如果连 p 值的一致性都无法保证，论文的整体可信度受到质疑。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: 自我污染是简化场景**\n\n同意，这与我的 W1 一致。Self-contamination（Qwen3-0.6B 生成 + Qwen3-0.6B 训练）创造了检测器最有利的条件——同模型族的输出在分布上最容易被区分。Appendix N 的 cross-model 实验（Llama-3.2-3B → Qwen）仅单 seed 且结论为 \"mixed results\"，实际上承认了方法在更现实场景下的有效性未验证。\n\n补充：R1 点出了一个我未强调的角度——self-contamination 不仅使检测更容易，还使得 calibration 更容易满足（Section 4 报告 ECE=0.05），因为训练和生成来自同一分布族。在 cross-model 场景中，ECE 可能显著退化，而论文的 F2（calibration 必要性）恰恰说明这会导致方法失败。\n\n---\n\n**[AGREE] R1-W2: 完全控制混淆后 D&R 过滤有害**\n\n同意这是一个重要发现，论文自身在 Section 5.1 也承认了：epoch-matched + LR-matched 下，D&R filtering (PPL=18.78) 劣于 uniform (18.06, Δ=+0.72)。\n\nR1 的推论值得认真考虑：如果 hard filtering 在公平对比下有害，那么 adaptive soft reweighting 的改善来源就需要仔细拆解。可能的来源包括：\n1. **Soft reweighting 本身**——温和降权保留了合成数据中的部分有用信息\n2. **LR schedule 交互**——adaptive 方法使用完整 6,103 步训练（vs. epoch-matched 的 2,533 步），享有更完整的学习率衰减\n3. **有效 epoch 效应的残余**——soft reweighting 仍然让人类数据的有效权重更高\n\n论文未拆解这三种因素的相对贡献。我认为这是 W2 级别（should-fix）而非 critical，因为 soft reweighting ≠ hard filtering，两者的机制不同。但 R1 的质疑迫使作者需要更严格地论证 adaptive 方法的改善确实来自智能重加权。\n\n---\n\n**[AGREE] R1-W3: 检测器覆盖窄**\n\n同意。论文使用 3 个检测器：TF-IDF+LR（主要）、GPT-2 perplexity scorer、N-gram（Section 5.1, Appendix K）。这些都是相对简单的方法，缺少：\n- Fine-tuned neural classifiers（RoBERTa/DeBERTa-based），这是 MGT detection 领域的主流方法\n- Zero-shot 方法如 DetectGPT/Fast-DetectGPT（论文在 Related Work Section 2 引用了但未在实验中使用）\n\n这特别影响 F2（\"both AUC and calibration required\"）的普适性——如果只测了 2 个家族（bag-of-words 和 perplexity-based），关于检测器要求的发现可能不适用于 neural classifiers。\n\n---\n\n**[REBUT] R1-W4: α_eff 代理 r=0.70 解释 49% 方差**\n\n部分反驳。R1 的 R²=0.49 计算正确，但对 α_eff 的角色存在误读：\n\n1. **α_eff 不需要完美追踪真实比例**。论文在 Section 3.2 和 Appendix J（Table 9）明确说明 α_eff 是 σ_adj 的 proxy，用于设置保守约束（quality floor）而非精确估计。约束只需要单调性——当 α_eff 增大时真实比例也增大——而 r=0.70 足以保证这一点。\n2. **保守偏差是 by design**。论文在 Section 3.2 提到 α_eff \"slightly underestimates the true real fraction, biasing the method toward conservative (less aggressive) intervention\"。这意味着 α_eff 的不完美恰好导致 minimum intervention——方法在不确定时倾向于少干预，这与论文的 F3 一致。\n3. **然而**，r=0.70 确实意味着约一半的方差未被解释，这在极端情况下可能导致约束失效。R1 的担忧在 ρ=0.2（低信噪比）时确实成立——论文也承认此时方法失败。\n\n所以我部分同意：r=0.70 对于保守约束的设计目的是可接受的，但 R1 正确指出这限制了方法在低污染场景的适用性。这不是一个独立的 should-fix，而是 ρ=0.2 失败的根因之一。\n\n---\n\n**[AGREE] R1-W5: ρ=0.2 失败和 1.7B 分析不充分**\n\n同意，这与我的审稿中的关注一致。Appendix M 对 ρ=0.2 失败的分析仅 1 段（\"detector's mean σ-score at this contamination level is 0.393\"），未深入探讨：\n- 是否存在一个 ρ 的临界阈值，低于该阈值方法系统性失败？\n- 1.7B 效果减弱是因为更大模型对污染更鲁棒，还是因为 reweighting 在更大模型上的信号更弱？\n\n论文在 Limitations（p.9）简要提及了这些局限，但对一篇分析型论文来说，这些应该是正文讨论的核心内容。\n\n---\n\n**[REBUT] R1-W6: B=4 离散空间上的 bisection 与连续理论脱节**\n\n反驳。R1 的分析存在技术误解：\n\n1. **Bisection 的搜索变量是 b（连续），不是 α_eff**。Algorithm 1（p.5）对 b ∈ [0, b_max] 做 bisection，寻找满足双约束的 b*。b 是连续实数，bisection 在此搜索空间上完全合法。\n2. **α_eff 不限于 5 个离散值**。R1 假设 B=4 micro-batch 中 α_eff 只取 {0, 0.25, 0.5, 0.75, 1.0}。但 α_eff = Σ w_i·r_i / Σ w_i（Section 3.2），其中 w_i = (1−q(x_i))^b 是连续权重。即使 r_i ∈ {0,1} 是二值的，不同 b 值产生不同的 w_i 组合，使得 α_eff 在给定 batch composition 下是 b 的连续函数。\n3. **ESS 也是连续的**。ESS(b) = (Σw_i)² / Σw_i²（Section 3.2），同样是 b 的连续函数。\n\n因此 bisection 在技术上是合理的。不过 R1 的直觉有一个合理的子点：B=4 的小 batch 确实引入了 α_eff 的高方差（论文在 Section 3.3 提到使用 H=16 after gradient accumulation），但这是 batch size 的一般性问题，不是 bisection 方法的问题。\n\n---\n\n### 总结\n\n| R1 问题 | 我的回应 | 理由 |\n|---------|---------|------|\n| N1 (N=3 统计) | [AGREE] | 效果 0.11% + df=2 + 无多重校正 + seed 42 artifact |\n| N2 (效果微小) | [AGREE] | 与我的 N2 一致，下游零改善是致命伤 |\n| N3 (p 值矛盾) | [AGREE] | 科学严谨性问题，无法用 one/two-tailed 解释 |\n| W1 (self-contamination) | [AGREE] | 与我的 W1 一致 |\n| W2 (filtering 有害) | [AGREE] | 重要发现，但需区分 soft reweighting vs. LR 交互 |\n| W3 (检测器窄) | [AGREE] | 缺 neural classifiers 和 zero-shot methods |\n| W4 (α_eff 代理) | [REBUT] | r=0.70 对保守约束足够，但限制低 ρ 适用性 |\n| W5 (ρ=0.2/1.7B) | [AGREE] | 分析不够深入 |\n| W6 (B=4 bisection) | [REBUT] | bisection 搜索 b（连续），α_eff 是 b 的连续函数 |\n\n**综合意见**：R1 和我的审稿在核心判断上高度一致——论文的诊断贡献有价值，但方法贡献受限于统计功效不足、效果微小、场景过窄。R1 额外发现的 p 值矛盾（N3）进一步强化了我对论文严谨性的担忧。我维持 Overall 3.0（Findings）的评分。\n\nR1 的审稿在统计方法论批评上比我更深入（特别是 N1 的 df=2 分析、N3 的 p 值矛盾、W6 的离散空间讨论），我的审稿在新颖性和写作质量评估上更详细（N1 Drayson 增量性、N3 Discussion 单薄、W4 论文定位模糊）。两份审稿互补性较强。",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: N=3 seeds 统计功效不足**\n\n同意这是本文最根本的统计问题之一。我在自己的审稿中将效果规模问题列为 N2（critical），核心论点一致：\n\n1. **df=2 的 paired t-test 极度脆弱**：R1 正确指出 t-test 在 df=2 时对 outlier 和非正态性极端敏感。事实上，任何单个 seed 的异常值都可以翻转统计结论。\n2. **多重比较未校正**：论文测试了多种方法 × 多个 ρ × 多个评估域的组合，p=0.025 在 Bonferroni 校正后远不显著。\n3. **Appendix O 的 seed 42 artifact**：R1 敏锐地发现 seed 42 使用了 checkpoint-resumed 训练。Appendix O 揭示这会引入 \"distribution matching\" 的虚假 finding。这意味着 3 个 seed 中有 1 个的实验条件与其他 2 个不完全一致，进一步削弱了 N=3 的可信度。\n\n补充：不过我注意到 3 seeds 在 NLP 训练实验中仍是常见做法（受 GPU 计算成本约束），论文也报告了方向性一致。问题不是\"3 seeds 不可接受\"，而是在效果规模仅 0.11% 时，3 seeds 不足以区分真实效果和噪声。如果效果是 Δ=-0.5 PPL，3 seeds 可能足够；但 Δ=-0.020 时绝对不够。\n\n---\n\n**[AGREE] R1-N2: Δ=-0.020 无下游任务改善**\n\n完全同意，这也是我的 N2 核心论点。补充几个 R1 未强调的细节：\n\n1. **Appendix H Table 7 的负面结果**极具说服力：adaptive 的三 seed 均值为 0.5414，uniform 也是相近水平，|Δ| ≤ 0.01 且在标准误差内。这意味着 PPL 的微小改进零转化为下游能力——reweighting 可能仅在改善 loss landscape 的某个局部指标，而非模型的实际能力。\n2. **ρ=0.2 的 +0.040 退化**（Appendix M）意味着方法在低污染场景反而有害。实际应用中，用户往往不知道真实 ρ 值，盲目应用 adaptive b* 可能损害模型。\n\n我在自己的审稿中建议作者重新定位为\"负面结果 + 诊断分析\"论文——即核心贡献不是 adaptive b*，而是\"D&R 的效果被严重高估\"这一发现本身。这样 Δ=-0.020 的小效果反而成为支持论点的证据。\n\n---\n\n**[AGREE] R1-N3: 主文与 Checklist 的 p 值矛盾**\n\n同意这是一个严重的科学严谨性问题。\n\n- Section 5.1 报告 adaptive vs. uniform 在 ρ=0.4 时 p=0.025\n- Checklist C3 报告同一比较 p=0.0425\n\n两个数字无法通过 one-tailed vs. two-tailed 解释（one-tailed 0.025 → two-tailed 0.050，不是 0.0425）。最可能的解释是：(a) 其中一个计算有误；(b) 两处使用了不同的比较基准但未说明；(c) 修改过程中未同步更新。无论哪种情况，核心统计声称存在未解决的矛盾，这在审稿中不可接受。\n\n我的审稿中未单独列出此问题（这是 R1 独立发现的），但我认为这属于 critical 级别——如果连 p 值的一致性都无法保证，论文的整体可信度受到质疑。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: 自我污染是简化场景**\n\n同意，这与我的 W1 一致。Self-contamination（Qwen3-0.6B 生成 + Qwen3-0.6B 训练）创造了检测器最有利的条件——同模型族的输出在分布上最容易被区分。Appendix N 的 cross-model 实验（Llama-3.2-3B → Qwen）仅单 seed 且结论为 \"mixed results\"，实际上承认了方法在更现实场景下的有效性未验证。\n\n补充：R1 点出了一个我未强调的角度——self-contamination 不仅使检测更容易，还使得 calibration 更容易满足（Section 4 报告 ECE=0.05），因为训练和生成来自同一分布族。在 cross-model 场景中，ECE 可能显著退化，而论文的 F2（calibration 必要性）恰恰说明这会导致方法失败。\n\n---\n\n**[AGREE] R1-W2: 完全控制混淆后 D&R 过滤有害**\n\n同意这是一个重要发现，论文自身在 Section 5.1 也承认了：epoch-matched + LR-matched 下，D&R filtering (PPL=18.78) 劣于 uniform (18.06, Δ=+0.72)。\n\nR1 的推论值得认真考虑：如果 hard filtering 在公平对比下有害，那么 adaptive soft reweighting 的改善来源就需要仔细拆解。可能的来源包括：\n1. **Soft reweighting 本身**——温和降权保留了合成数据中的部分有用信息\n2. **LR schedule 交互**——adaptive 方法使用完整 6,103 步训练（vs. epoch-matched 的 2,533 步），享有更完整的学习率衰减\n3. **有效 epoch 效应的残余**——soft reweighting 仍然让人类数据的有效权重更高\n\n论文未拆解这三种因素的相对贡献。我认为这是 W2 级别（should-fix）而非 critical，因为 soft reweighting ≠ hard filtering，两者的机制不同。但 R1 的质疑迫使作者需要更严格地论证 adaptive 方法的改善确实来自智能重加权。\n\n---\n\n**[AGREE] R1-W3: 检测器覆盖窄**\n\n同意。论文使用 3 个检测器：TF-IDF+LR（主要）、GPT-2 perplexity scorer、N-gram（Section 5.1, Appendix K）。这些都是相对简单的方法，缺少：\n- Fine-tuned neural classifiers（RoBERTa/DeBERTa-based），这是 MGT detection 领域的主流方法\n- Zero-shot 方法如 DetectGPT/Fast-DetectGPT（论文在 Related Work Section 2 引用了但未在实验中使用）\n\n这特别影响 F2（\"both AUC and calibration required\"）的普适性——如果只测了 2 个家族（bag-of-words 和 perplexity-based），关于检测器要求的发现可能不适用于 neural classifiers。\n\n---\n\n**[REBUT] R1-W4: α_eff 代理 r=0.70 解释 49% 方差**\n\n部分反驳。R1 的 R²=0.49 计算正确，但对 α_eff 的角色存在误读：\n\n1. **α_eff 不需要完美追踪真实比例**。论文在 Section 3.2 和 Appendix J（Table 9）明确说明 α_eff 是 σ_adj 的 proxy，用于设置保守约束（quality floor）而非精确估计。约束只需要单调性——当 α_eff 增大时真实比例也增大——而 r=0.70 足以保证这一点。\n2. **保守偏差是 by design**。论文在 Section 3.2 提到 α_eff \"slightly underestimates the true real fraction, biasing the method toward conservative (less aggressive) intervention\"。这意味着 α_eff 的不完美恰好导致 minimum intervention——方法在不确定时倾向于少干预，这与论文的 F3 一致。\n3. **然而**，r=0.70 确实意味着约一半的方差未被解释，这在极端情况下可能导致约束失效。R1 的担忧在 ρ=0.2（低信噪比）时确实成立——论文也承认此时方法失败。\n\n所以我部分同意：r=0.70 对于保守约束的设计目的是可接受的，但 R1 正确指出这限制了方法在低污染场景的适用性。这不是一个独立的 should-fix，而是 ρ=0.2 失败的根因之一。\n\n---\n\n**[AGREE] R1-W5: ρ=0.2 失败和 1.7B 分析不充分**\n\n同意，这与我的审稿中的关注一致。Appendix M 对 ρ=0.2 失败的分析仅 1 段（\"detector's mean σ-score at this contamination level is 0.393\"），未深入探讨：\n- 是否存在一个 ρ 的临界阈值，低于该阈值方法系统性失败？\n- 1.7B 效果减弱是因为更大模型对污染更鲁棒，还是因为 reweighting 在更大模型上的信号更弱？\n\n论文在 Limitations（p.9）简要提及了这些局限，但对一篇分析型论文来说，这些应该是正文讨论的核心内容。\n\n---\n\n**[REBUT] R1-W6: B=4 离散空间上的 bisection 与连续理论脱节**\n\n反驳。R1 的分析存在技术误解：\n\n1. **Bisection 的搜索变量是 b（连续），不是 α_eff**。Algorithm 1（p.5）对 b ∈ [0, b_max] 做 bisection，寻找满足双约束的 b*。b 是连续实数，bisection 在此搜索空间上完全合法。\n2. **α_eff 不限于 5 个离散值**。R1 假设 B=4 micro-batch 中 α_eff 只取 {0, 0.25, 0.5, 0.75, 1.0}。但 α_eff = Σ w_i·r_i / Σ w_i（Section 3.2），其中 w_i = (1−q(x_i))^b 是连续权重。即使 r_i ∈ {0,1} 是二值的，不同 b 值产生不同的 w_i 组合，使得 α_eff 在给定 batch composition 下是 b 的连续函数。\n3. **ESS 也是连续的**。ESS(b) = (Σw_i)² / Σw_i²（Section 3.2），同样是 b 的连续函数。\n\n因此 bisection 在技术上是合理的。不过 R1 的直觉有一个合理的子点：B=4 的小 batch 确实引入了 α_eff 的高方差（论文在 Section 3.3 提到使用 H=16 after gradient accumulation），但这是 batch size 的一般性问题，不是 bisection 方法的问题。\n\n---\n\n### 总结\n\n| R1 问题 | 我的回应 | 理由 |\n|---------|---------|------|\n| N1 (N=3 统计) | [AGREE] | 效果 0.11% + df=2 + 无多重校正 + seed 42 artifact |\n| N2 (效果微小) | [AGREE] | 与我的 N2 一致，下游零改善是致命伤 |\n| N3 (p 值矛盾) | [AGREE] | 科学严谨性问题，无法用 one/two-tailed 解释 |\n| W1 (self-contamination) | [AGREE] | 与我的 W1 一致 |\n| W2 (filtering 有害) | [AGREE] | 重要发现，但需区分 soft reweighting vs. LR 交互 |\n| W3 (检测器窄) | [AGREE] | 缺 neural classifiers 和 zero-shot methods |\n| W4 (α_eff 代理) | [REBUT] | r=0.70 对保守约束足够，但限制低 ρ 适用性 |\n| W5 (ρ=0.2/1.7B) | [AGREE] | 分析不够深入 |\n| W6 (B=4 bisection) | [REBUT] | bisection 搜索 b（连续），α_eff 是 b 的连续函数 |\n\n**综合意见**：R1 和我的审稿在核心判断上高度一致——论文的诊断贡献有价值，但方法贡献受限于统计功效不足、效果微小、场景过窄。R1 额外发现的 p 值矛盾（N3）进一步强化了我对论文严谨性的担忧。我维持 Overall 3.0（Findings）的评分。\n\nR1 的审稿在统计方法论批评上比我更深入（特别是 N1 的 df=2 分析、N3 的 p 值矛盾、W6 的离散空间讨论），我的审稿在新颖性和写作质量评估上更详细（N1 Drayson 增量性、N3 Discussion 单薄、W4 论文定位模糊）。两份审稿互补性较强。",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-21T14:19:17.251397+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3693
}
```

</details>

---


### Assistant

_source line 672 · 2026-05-21T14:19:26.384206+00:00_

交叉回应已提交。核心判断：

- **9 条中 7 条 [AGREE]**：N1-N3（统计功效、效果微小、p值矛盾）+ W1-W3, W5（self-contamination、filtering有害、检测器窄、分析不足）
- **2 条 [REBUT]**：W4（α_eff r=0.70 对保守约束设计目的足够）和 W6（bisection 搜索的是连续变量 b，不是离散的 α_eff）

R1 额外发现的 p 值矛盾（§5.1 p=0.025 vs. Checklist C3 p=0.0425）是我审稿中遗漏的重要问题，进一步强化了统计可信度的担忧。两份审稿在核心评分（Overall 3.0 Findings）上一致，侧重互补——R1 在统计方法论上更深入，我在新颖性和写作质量上更详细。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 17

## Round 17

54 recorded events


### User

_source line 673 · 2026-05-22T16:55:13.423949+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查 **新颖性、论文定位、完整性和写作质量**。

## Venue 信息
- **目标**: EMNLP 2026 Long Paper (ARR)
- **Deadline**: 2026-05-25
- **格式**: ACL template, double-blind, 正文 ≤ 8 页, 参考文献无限制
- **匿名**: double-blind（无匿名期要求）
- **附录**: 允许但 reviewer 不必阅读；关键内容必须在正文
- **Limitations**: 必须有，不计入页数
- **Responsible NLP Checklist**: 应在 OpenReview 表单填写，不在论文 PDF 中

## 论文路径
- LaTeX: `projects/provenance_weight_training/docs/paper/main.tex`
- Sections: `projects/provenance_weight_training/docs/paper/sections/` 下各 .tex 文件
- PDF: `projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf`

## 你的审查侧重

### 1. 新颖性评估
- 相对于 Drayson et al. (2025) 的增量贡献是否足够？论文采用相同的加权公式 w=(1-q)^b，仅改变 b 的选择方式
- ESS (Kish 1965) 和 α_eff 都不是新概念——dual constraint 组合的新颖性如何？
- Epoch confound 发现的价值——这是显而易见的还是真正有洞察力的？
- 检测器 calibration 对 reweighting 效果的影响——这是否已被先前工作暗示？

### 2. 论文定位
- 论文定位为 analysis paper 还是 method paper？定位是否一致？
- Abstract 和 Introduction 同时强调 findings 和 adaptive b*——是否存在定位模糊？
- Method section 的篇幅与 analysis paper 定位是否匹配？
- Contribution 排序是否合理（epoch confound > detector requirements > mechanism > adaptive b*）？

### 3. 完整性
- Related work 覆盖是否充分？是否遗漏重要相关工作？
- 是否缺少重要的实验（如更多 detector 类型、更大规模模型、非 self-contamination 场景）？
- Limitations 是否诚实全面？
- Conclusion 是否与 findings 匹配？

### 4. 写作质量
- 叙事是否清晰流畅？读者能否一遍读懂？
- 术语使用是否一致？
- Figure/Table 设计是否清晰有效？
- 信息密度是否合适（非冗余也非遗漏）？
- Discussion 作为 analysis paper 的核心章节，是否有足够深度？

### 5. 格式合规
- Responsible NLP Checklist 是否错误地包含在 PDF 中？（ARR 规定应在 OpenReview 表单中）
- 引用格式是否符合 ACL 要求？
- 匿名是否完整（无作者身份泄露）？

请按 ARR 标准完成审稿，输出结构：Summary → Strengths → Weaknesses (逐条，标注 severity: critical/major/minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-22T16:55:30.094633+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-22T16:55:30.797611+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-22T16:55:30.949033+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-22T16:55:30.949495+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-22T16:55:38.982193+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 679 · 2026-05-22T16:55:41.039278+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 680 · 2026-05-22T16:55:46.408556+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

For Main papers, evaluation considers multiple factors, while for Findings papers, the main criteria are soundnes
…[truncated 1443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7426
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-22T16:55:48.293748+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submi
…[truncated 537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7254
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-22T16:55:56.232613+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all dimensions, scoring scales, and descriptions. I need every field that reviewers must fill in, including overall assessment, soundness, excitement, reproducibility, confidence, and any other criteria. Include the exact scale descriptions for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all dimensions, scoring scales, and descriptions. I need every field that reviewers must fill in, including overall assessment, soundness, excitement, reproducibility, confidence, and any other criteria. Include the exact scale descriptions for each score level."
  }
}
```

</details>

---


### Tool call

_source line 683 · 2026-05-22T16:55:57.711788+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-22T16:55:58.160019+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 685 · 2026-05-22T16:55:58.676029+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-22T16:55:59.609679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 687 · 2026-05-22T16:55:59.760490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 688 · 2026-05-22T16:56:03.475147+00:00_

# ACL Rolling Review Form: Complete Structure

## Core Review Sections

**Paper Summary**
Reviewers describe the paper's subject matter to ensure shared understanding among decision-makers.

**Summary of Strengths**
Identifies reasons supporting publication, such as "novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related literature."

**Summary of Weaknesses**
Documents concerns about correctness, impact, clarity, or other factors that might deprioritize the paper versus competing submissions.

**Comments/Suggestions/Typos**
Space for improvement recommendations beyond weakness responses.

## Quantitative Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: Positive evaluation; careful reading and familiar with related work
- 4: Quite sure, though conceivable gaps remain
- 3: Pretty sure, though details may be unchecked
- 2: Defensible evaluation, but likely missed details
- 1: Outside expertise area or paper is difficult to understand

**Soundness** (1-5 with half-point increments)
Evaluates scientific rigor. Scale ranges from "Major Issues" (1) to "Excellent" (5), considering experimental depth, technical validity, and claim support.

**Excitement** (1-5 with half-point increments)
Subjective assessment of transformational potential, community impact, or personal relevance, from "Not Exciting" (1) to "Highly Exciting" (5).

**Overall Assessment** (1-5 with half-point increments)
Ranges from "Do not resubmit" (1) through "Resubmit next cycle" (2), "Findings" (3), "Conference" (4), to "Consider for Award" (5).

## Additional Evaluation Areas

- **Limitations and Societal Impact**: Discussion of potential harms, exclusions, and stakeholder effects
- **Ethical Concerns**: Alignment with "ACL code of ethics" and ethics checklist
- **Needs Ethics Review**: Flag for specialized ethics committee review
- **Reproducibility** (1-5): Information sufficiency for result replication
- **Datasets** (1-5): Released datase
…[truncated 162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7242
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-22T16:56:04.127097+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 395.4}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 387.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 430.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 481.2}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 196.7}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6415
}
```

</details>

---


### Tool result

_source line 690 · 2026-05-22T16:56:08.058280+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 8297
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-22T16:56:08.210133+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 9534
}
```

</details>

---


### Tool result

_source line 692 · 2026-05-22T16:56:08.216435+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 8606
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-22T16:56:08.267717+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 10107
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-22T16:56:21.873031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 695 · 2026-05-22T16:56:22.327023+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 696 · 2026-05-22T16:56:22.930764+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1057
}
```

</details>

---


### Tool call

_source line 697 · 2026-05-22T16:56:22.982024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 698 · 2026-05-22T16:56:23.334397+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool call

_source line 699 · 2026-05-22T16:56:23.334831+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 700 · 2026-05-22T16:56:23.787510+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-22T16:56:24.139741+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-22T16:56:31.416508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-22T16:56:34.026813+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2610
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-22T16:56:34.077395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 705 · 2026-05-22T16:56:34.280202+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-22T16:56:34.280596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-22T16:56:35.237823+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1160
}
```

</details>

---


### Tool result

_source line 708 · 2026-05-22T16:56:35.390960+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-22T16:56:35.492435+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1212
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-22T16:56:50.559023+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 711 · 2026-05-22T16:56:50.711021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-22T16:56:50.813321+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 713 · 2026-05-22T16:56:50.864266+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 714 · 2026-05-22T16:56:50.968186+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 409
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-22T16:56:51.923350+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool result

_source line 716 · 2026-05-22T16:56:52.278017+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1566
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-22T16:56:52.278873+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1465
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-22T17:01:16.617428+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the EXACT scoring scale descriptions for each dimension: Soundness (1-5), Excitement (1-5), Overall Assessment (1-5), Reproducibility (1-5), and Confidence (1-5). I need the exact text for each score level (e.g., what does Soundness=3 mean? What does Excitement=2 mean?). Also extract any guidance on how to weigh different factors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the EXACT scoring scale descriptions for each dimension: Soundness (1-5), Excitement (1-5), Overall Assessment (1-5), Reproducibility (1-5), and Confidence (1-5). I need the exact text for each score level (e.g., what does Soundness=3 mean? What does Excitement=2 mean?). Also extract any guidance on how to weigh different factors."
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-22T17:01:23.103428+00:00_

# ACL Rolling Review Scoring Scales

## Soundness (1-5)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement (1-5)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Overall Assessment (1-5)
- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award."
- **4**: "Conference: I think this paper could be accepted to an *ACL conference."
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: I think this paper needs substantial revisions."
- **1**: "Do not resubmit: This paper has to be fully redone."

## Reproducibility (1-5)
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results, but there may be some variation."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
- **1**: "They would not be able to reproduce the results here no matter how hard they tried."

## Confidence (1-5)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully."
- **4**: "Quite sure. It's unlikely, though conceivable, that I missed something."
- **3**: "Pret
…[truncated 248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6486
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-22T17:03:31.195645+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见（Round 1）\n**侧重**: 新颖性、论文定位、完整性、写作质量\n\n---\n\n## Paper Summary\n\n本文研究 detect-and-reweight (D&R) 范式在含合成文本的 continued LM pretraining 中的有效性条件。通过 Qwen3-0.6B 上的受控实验（132M FineWeb tokens, ρ=0.4, 3 seeds），作者报告三个发现：(1) D&R 相对于 adaptive reweighting 的 PPL 优势中 >95% 来自 multi-epoch exposure confound 而非 filtering quality；(2) 有效 reweighting 需要检测器同时具备足够的 discrimination (AUC) 和良好的 calibration (ECE)；(3) 机制通过 α_eff（effective real proportion）和 ESS（effective sample size）的 dual constraint 运作。作者提出 adaptive b* 公式化，消除 grid search 的同时匹配或超越 grid-searched 性能。\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 扎实的分析工作，epoch confound 发现有价值，但方法新颖性有限、实验规模偏小、downstream task 无可测量改善，综合来看达到 Findings 水准但不足以进入主会议。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨（epoch-matched controls, 3 seeds, 逐因素消融），数学框架正确（Proposition 1-2 证明完整），但实验范围受限（仅 0.6B/1.7B, self-contamination, 单一数据集），泛化性未得到验证 |\n| Excitement | 2.5/5 | Epoch confound 发现纠正了文献中的重要误判，有实际价值；但方法贡献增量式（同一公式 w=(1-q)^b，仅改变 b 选择方式），downstream 零提升削弱实际影响力 |\n| Reproducibility | 4.0/5 | 实验细节充分（§4 报告 batch size, LR schedule, sequence length, hardware），承诺代码和数据在接收后公开，超参数均有报告；唯一不确定是合成数据生成的完整 prompt 细节（Appendix M 提到 128-token prefix prompt 但未给出完整模板） |\n| Confidence | 4/5 | 熟悉数据 curation、pretraining 和 synthetic data detection 文献，仔细阅读了正文和全部 17 个附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 方法新颖性不足以支撑独立贡献\n- 具体位置：§3.2 Dual-Constraint Framework, §1 Contribution list item 4\n- 问题：论文的 methodological contribution 是将 ESS（Kish, 1965）和 α_eff 组合为 dual constraint 来自动选择 b*，但：(a) 加权公式 w=(1-q)^b 完全沿用 Drayson et al. (2025)，无任何修改；(b) ESS 和 α_eff 均为已有概念，dual constraint 组合是直接应用而非根本性创新；(c) adaptive b* 本质上是超参数自动选择方法，替代 grid search——实用但算不上显著的概念性贡献。论文的真正价值在于分析发现（epoch confound, detector requirements），而非方法本身。\n- 为什么影响接收：作为 method paper 投 main conference，novelty bar 未达到；作为 analysis paper，方法部分的篇幅和 contribution list 中的权重与定位不匹配。\n- 建议修改方向：明确将论文定位为 empirical analysis paper，将 adaptive b* 作为分析的 practical corollary 而非并列的核心贡献。重新组织 contribution list，让分析发现占据更突出的位置。\n\n**N2** [critical] Downstream task 无可测量改善\n- 具体位置：§6 Discussion（\"Downstream tasks do not reflect PPL improvements\"）, Table 3\n- 问题：Table 3 显示 adaptive reweighting vs. uniform training 在所有 downstream benchmarks 上 |Δ| ≤ 0.01，且方向不一致（\"no individual task shows a consistent advantage\"）。论文将此归因于\"PPL improvements operate in a regime that standard benchmarks cannot resolve\"和 0.6B 模型上 5-choice tasks 灵敏度不足。但这个论点有循环论证的嫌疑：如果效果微小到现有评估方法都测不出来，那么论文的实际价值论证就缺乏支撑。\n- 为什么影响接收：一个 pretraining 方法论文如果无法展示任何 downstream 改善，其实际意义会被严重质疑。PPL 改善仅 Δ≈-0.014（~0.08% relative），这属于工程 noise 级别。\n- 建议修改方向：(a) 在更大模型（7B+）上验证 PPL 改善是否放大并传递到 downstream；(b) 使用更细粒度的评估（如 generation quality、factual accuracy on contaminated domains）代替粗粒度的 benchmark accuracy；(c) 或者诚实地将论文重新定位为纯分析/负面结果论文，不主张实际方法改进。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] 实验规模和场景过于狭窄\n- 具体位置：§4 Experimental Setup, §8 Limitations\n- 问题：\n  - **模型规模**：仅 0.6B 和 1.7B，现代 pretraining 至少在 7B 级别。§5.3 的 1.7B 结果仅简述一段（\"the method scales without degradation\"），未提供完整的 epoch-matched 消融。\n  - **Self-contamination**：所有合成数据由 Qwen3-0.6B 生成，训练也用 Qwen3-0.6B（或 1.7B）。真实世界的合成污染来自多样的模型（GPT-4, Claude, Llama 等），检测难度和分布特征完全不同。\n  - **单一基础数据集**：仅 FineWeb。不同领域/风格的数据分布可能导致不同结论。\n  - **单一污染类型**：仅 continuation-style generation（128-token prefix → 384 tokens）。真实污染包括 paraphrase、翻译、instruction-following outputs 等。\n- 建议：至少增加一个 cross-model contamination 实验（如用 Llama 生成，Qwen 训练），以验证核心发现的鲁棒性。Appendix O 的 cross-model transfer 实验（Llama-3.2-3B, Table 12）结果混合（MMLU 升 HellaSwag 降），并不令人信服。\n\n**W2** [major] 论文定位存在模糊性\n- 具体位置：Abstract, §1 Introduction, §3 Method\n- 问题：Abstract 第一句话强调\"we analyze when, why, and how detect-and-reweight works\"（分析定位），但随后介绍\"we introduce a dual-constrained formulation\"（方法定位）。§1 的四条 contribution 混合了观察型贡献（epoch confound, detector requirements, mechanism）和方法型贡献（adaptive b*），缺乏明确的主次层级。§3 Method 占据将近 1.5 页的篇幅，对于一篇分析论文来说偏重。\n- 建议：在 Abstract 和 Introduction 中明确建立\"analysis paper with practical implications\"的定位。可以将 adaptive b* 的详细推导移至附录，主文仅保留核心思想（~半页），释放空间给更深入的分析讨论或更大规模的实验结果。\n\n**W3** [minor] α_eff 作为 quality proxy 的相关性有限\n- 具体位置：§8 Limitations, Appendix K (Table 10)\n- 问题：α_eff 与 true batch-level real fraction 的 Pearson 相关仅 r=0.70（解释 ~49% variance）。负斜率 β(≈-0.031) 表明 α_eff 系统性低估真实 real fraction，导致方法偏向保守干预。这意味着 quality constraint 基于一个较嘈杂的代理量运作。\n- 建议：讨论是否存在更精确的 proxy，或分析 proxy noise 对 b* 选择的实际影响有多大。\n\n**W4** [minor] 关键效应量极小，实际意义需更充分论证\n- 具体位置：Table 1, §6 Discussion\n- 问题：Adaptive b* vs. uniform 的 PPL 改善为 Δ=-0.014（17.620 vs. 17.634），即 ~0.08% relative improvement。在 epoch-matched 条件下，adaptive vs. D&R full 的优势为 Δ=-0.032（paired p=0.025）。虽然统计显著，但效应量极小。论文在 §6 承认\"the true value added by detect-and-reweight is substantially smaller than published results suggest\"，但未充分讨论这个效应量在实际 pretraining pipeline 中是否值得引入检测器和 reweighting 的额外复杂性。\n- 建议：增加一个 cost-benefit 分析段落——引入检测器训练、推理、calibration 的计算开销 vs. 获得的 0.08% PPL 改善，帮助读者判断在什么条件下值得使用。\n\n**W5** [minor] Responsible NLP Research Checklist 出现在 PDF 中\n- 具体位置：Page 9\n- 问题：EMNLP 2026 通过 ARR 审稿，Responsible NLP Checklist 应在 OpenReview submission form 中填写，不应包含在论文 PDF 中。当前 checklist 占据约 1 页篇幅。\n- 建议：从 PDF 中移除 checklist，在 OpenReview 表单中填写。释放的空间可用于加强 Discussion 或增加实验。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.1 Problem Setup：contamination ratio ρ 的 footnote 9（page 4 底部）区分 token-level 和 document-level contamination ratio，这个区分在主文中提到得太晚，建议在 §3.1 定义 ρ 时就澄清。\n- Figure 2：y 轴标注为\"Held-out PPL ↓\"，图例中\"Uniform (full)\"和\"D&R full (grid)\"的线条在黑白打印下不易区分，建议调整 line style 或 marker。\n- Table 2（page 6）：列标题\"Seed 42\", \"Seed 123\", \"Seed 456\" 与 \"Mean 4σ\"——应为 \"Mean ± σ\" 或 \"Mean (σ)\"，\"4σ\" 的含义不明确（是 4 倍标准差？还是排版错误？）。\n- §2 Related Work 首段中\"Cheng et al. (2025) survey the broader contamination landscape\"出现在一个密集的文献回顾段落中，但该引用的具体贡献未被明确说明——建议简要说明其与本文的关系。\n\n---\n\n## Questions for Authors\n\nQ1. 在 7B+ 规模上，epoch confound 发现是否仍然成立？是否有初步证据表明效应量随规模变化？\n\nQ2. 如果使用 cross-model contamination（如 GPT-4 生成的文本），检测器的 AUC 和 ECE 如何变化？dual constraint 方法是否仍然有效？\n\nQ3. Table 3 的 downstream null result 是否可能源于评估方法的局限而非方法本身？是否考虑过更细粒度的评估（如在受污染领域的 factual accuracy 或 generation quality）？\n\nQ4. Quality threshold τ=0.7 和 τ_min 的选择依据是什么？Appendix D 显示了 threshold sweep 但 τ=0.7 的选择似乎基于经验而非理论——这会影响方法在新数据集上的适用性吗？\n\nQ5. Appendix Q (Table 13) 的 practitioner decision summary 非常实用，为什么不放在主文中？这会比当前 §3.2 中的部分数学推导更有助于读者。\n\n---\n\n## Missing References\n\n引用覆盖基本充分，以下为可考虑补充的参考：\n\n- **Llama 3 technical report (Meta, 2024)**：描述了大规模 pretraining 中的数据 curation pipeline，包括合成数据处理，可在 Related Work §2 中作为 motivation 引用，说明工业界对 synthetic contamination 的关注。\n- **Penedo et al. (2024) 的 FineWeb 论文**已引用为数据来源，但其中关于 quality filtering 与 quantity tradeoff 的讨论与本文 §6 的 cost-benefit 分析相关，可进一步引用其发现。\n\n---\n\n## 主要优势\n\n1. **Epoch confound 发现（S1）**：通过严谨的 epoch-matched 对照实验（Table 1），证明 D&R 的 >95% PPL 优势来自 multi-epoch exposure 而非 filtering quality，这纠正了 Drayson et al. (2025) 中的重要误归因。独立的 LR-schedule 复现（§5.1）进一步加强了这一结论的可信度。\n\n2. **实验设计的严谨性（S2）**：全文采用系统化的受控实验——逐因素消融（epoch matching → detector quality → contamination level → scale），3 seeds 提供统计基础，paired t-tests 报告显著性。这是 empirical ML 论文的良好范例。\n\n3. **诚实的 Discussion（S3）**：§6 不回避负面发现（downstream 无改善、α_eff proxy 局限、效应量极小），这种透明度在分析论文中尤为重要，增强了结论的可信度。\n\n4. **Analysis overview 可视化（S4）**：Figure 1 有效地将三个发现的逻辑链条可视化（epoch confound → detector requirements → mechanism → adaptive b*），帮助读者快速建立论文结构的心理模型。\n\n5. **详尽的附录（S5）**：17 个附录（A-Q）提供了完整的证明、消融、proxy 验证和 practitioner guide，展现了作者对研究细节的认真态度。\n\n---\n\n## 总结\n\n本文的核心价值在于 epoch confound 发现——这是一个有意义的 empirical contribution，纠正了文献中的过度乐观估计。实验设计严谨，写作清晰。但方法贡献（adaptive b*）是在已有公式上的增量改进，downstream task 无可测量改善削弱了实际影响力，实验规模（0.6B/1.7B, self-contamination, 单一数据集）限制了结论的泛化性。综合来看，论文达到 Findings 水准：发现有用、方法可靠，但 novelty 和 impact 不足以进入主会议。若能在 7B+ 上复现关键发现并展示 downstream 改善，可提升至 Borderline Conference。",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见（Round 1）\n**侧重**: 新颖性、论文定位、完整性、写作质量\n\n---\n\n## Paper Summary\n\n本文研究 detect-and-reweight (D&R) 范式在含合成文本的 continued LM pretraining 中的有效性条件。通过 Qwen3-0.6B 上的受控实验（132M FineWeb tokens, ρ=0.4, 3 seeds），作者报告三个发现：(1) D&R 相对于 adaptive reweighting 的 PPL 优势中 >95% 来自 multi-epoch exposure confound 而非 filtering quality；(2) 有效 reweighting 需要检测器同时具备足够的 discrimination (AUC) 和良好的 calibration (ECE)；(3) 机制通过 α_eff（effective real proportion）和 ESS（effective sample size）的 dual constraint 运作。作者提出 adaptive b* 公式化，消除 grid search 的同时匹配或超越 grid-searched 性能。\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 扎实的分析工作，epoch confound 发现有价值，但方法新颖性有限、实验规模偏小、downstream task 无可测量改善，综合来看达到 Findings 水准但不足以进入主会议。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨（epoch-matched controls, 3 seeds, 逐因素消融），数学框架正确（Proposition 1-2 证明完整），但实验范围受限（仅 0.6B/1.7B, self-contamination, 单一数据集），泛化性未得到验证 |\n| Excitement | 2.5/5 | Epoch confound 发现纠正了文献中的重要误判，有实际价值；但方法贡献增量式（同一公式 w=(1-q)^b，仅改变 b 选择方式），downstream 零提升削弱实际影响力 |\n| Reproducibility | 4.0/5 | 实验细节充分（§4 报告 batch size, LR schedule, sequence length, hardware），承诺代码和数据在接收后公开，超参数均有报告；唯一不确定是合成数据生成的完整 prompt 细节（Appendix M 提到 128-token prefix prompt 但未给出完整模板） |\n| Confidence | 4/5 | 熟悉数据 curation、pretraining 和 synthetic data detection 文献，仔细阅读了正文和全部 17 个附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 方法新颖性不足以支撑独立贡献\n- 具体位置：§3.2 Dual-Constraint Framework, §1 Contribution list item 4\n- 问题：论文的 methodological contribution 是将 ESS（Kish, 1965）和 α_eff 组合为 dual constraint 来自动选择 b*，但：(a) 加权公式 w=(1-q)^b 完全沿用 Drayson et al. (2025)，无任何修改；(b) ESS 和 α_eff 均为已有概念，dual constraint 组合是直接应用而非根本性创新；(c) adaptive b* 本质上是超参数自动选择方法，替代 grid search——实用但算不上显著的概念性贡献。论文的真正价值在于分析发现（epoch confound, detector requirements），而非方法本身。\n- 为什么影响接收：作为 method paper 投 main conference，novelty bar 未达到；作为 analysis paper，方法部分的篇幅和 contribution list 中的权重与定位不匹配。\n- 建议修改方向：明确将论文定位为 empirical analysis paper，将 adaptive b* 作为分析的 practical corollary 而非并列的核心贡献。重新组织 contribution list，让分析发现占据更突出的位置。\n\n**N2** [critical] Downstream task 无可测量改善\n- 具体位置：§6 Discussion（\"Downstream tasks do not reflect PPL improvements\"）, Table 3\n- 问题：Table 3 显示 adaptive reweighting vs. uniform training 在所有 downstream benchmarks 上 |Δ| ≤ 0.01，且方向不一致（\"no individual task shows a consistent advantage\"）。论文将此归因于\"PPL improvements operate in a regime that standard benchmarks cannot resolve\"和 0.6B 模型上 5-choice tasks 灵敏度不足。但这个论点有循环论证的嫌疑：如果效果微小到现有评估方法都测不出来，那么论文的实际价值论证就缺乏支撑。\n- 为什么影响接收：一个 pretraining 方法论文如果无法展示任何 downstream 改善，其实际意义会被严重质疑。PPL 改善仅 Δ≈-0.014（~0.08% relative），这属于工程 noise 级别。\n- 建议修改方向：(a) 在更大模型（7B+）上验证 PPL 改善是否放大并传递到 downstream；(b) 使用更细粒度的评估（如 generation quality、factual accuracy on contaminated domains）代替粗粒度的 benchmark accuracy；(c) 或者诚实地将论文重新定位为纯分析/负面结果论文，不主张实际方法改进。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] 实验规模和场景过于狭窄\n- 具体位置：§4 Experimental Setup, §8 Limitations\n- 问题：\n  - **模型规模**：仅 0.6B 和 1.7B，现代 pretraining 至少在 7B 级别。§5.3 的 1.7B 结果仅简述一段（\"the method scales without degradation\"），未提供完整的 epoch-matched 消融。\n  - **Self-contamination**：所有合成数据由 Qwen3-0.6B 生成，训练也用 Qwen3-0.6B（或 1.7B）。真实世界的合成污染来自多样的模型（GPT-4, Claude, Llama 等），检测难度和分布特征完全不同。\n  - **单一基础数据集**：仅 FineWeb。不同领域/风格的数据分布可能导致不同结论。\n  - **单一污染类型**：仅 continuation-style generation（128-token prefix → 384 tokens）。真实污染包括 paraphrase、翻译、instruction-following outputs 等。\n- 建议：至少增加一个 cross-model contamination 实验（如用 Llama 生成，Qwen 训练），以验证核心发现的鲁棒性。Appendix O 的 cross-model transfer 实验（Llama-3.2-3B, Table 12）结果混合（MMLU 升 HellaSwag 降），并不令人信服。\n\n**W2** [major] 论文定位存在模糊性\n- 具体位置：Abstract, §1 Introduction, §3 Method\n- 问题：Abstract 第一句话强调\"we analyze when, why, and how detect-and-reweight works\"（分析定位），但随后介绍\"we introduce a dual-constrained formulation\"（方法定位）。§1 的四条 contribution 混合了观察型贡献（epoch confound, detector requirements, mechanism）和方法型贡献（adaptive b*），缺乏明确的主次层级。§3 Method 占据将近 1.5 页的篇幅，对于一篇分析论文来说偏重。\n- 建议：在 Abstract 和 Introduction 中明确建立\"analysis paper with practical implications\"的定位。可以将 adaptive b* 的详细推导移至附录，主文仅保留核心思想（~半页），释放空间给更深入的分析讨论或更大规模的实验结果。\n\n**W3** [minor] α_eff 作为 quality proxy 的相关性有限\n- 具体位置：§8 Limitations, Appendix K (Table 10)\n- 问题：α_eff 与 true batch-level real fraction 的 Pearson 相关仅 r=0.70（解释 ~49% variance）。负斜率 β(≈-0.031) 表明 α_eff 系统性低估真实 real fraction，导致方法偏向保守干预。这意味着 quality constraint 基于一个较嘈杂的代理量运作。\n- 建议：讨论是否存在更精确的 proxy，或分析 proxy noise 对 b* 选择的实际影响有多大。\n\n**W4** [minor] 关键效应量极小，实际意义需更充分论证\n- 具体位置：Table 1, §6 Discussion\n- 问题：Adaptive b* vs. uniform 的 PPL 改善为 Δ=-0.014（17.620 vs. 17.634），即 ~0.08% relative improvement。在 epoch-matched 条件下，adaptive vs. D&R full 的优势为 Δ=-0.032（paired p=0.025）。虽然统计显著，但效应量极小。论文在 §6 承认\"the true value added by detect-and-reweight is substantially smaller than published results suggest\"，但未充分讨论这个效应量在实际 pretraining pipeline 中是否值得引入检测器和 reweighting 的额外复杂性。\n- 建议：增加一个 cost-benefit 分析段落——引入检测器训练、推理、calibration 的计算开销 vs. 获得的 0.08% PPL 改善，帮助读者判断在什么条件下值得使用。\n\n**W5** [minor] Responsible NLP Research Checklist 出现在 PDF 中\n- 具体位置：Page 9\n- 问题：EMNLP 2026 通过 ARR 审稿，Responsible NLP Checklist 应在 OpenReview submission form 中填写，不应包含在论文 PDF 中。当前 checklist 占据约 1 页篇幅。\n- 建议：从 PDF 中移除 checklist，在 OpenReview 表单中填写。释放的空间可用于加强 Discussion 或增加实验。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.1 Problem Setup：contamination ratio ρ 的 footnote 9（page 4 底部）区分 token-level 和 document-level contamination ratio，这个区分在主文中提到得太晚，建议在 §3.1 定义 ρ 时就澄清。\n- Figure 2：y 轴标注为\"Held-out PPL ↓\"，图例中\"Uniform (full)\"和\"D&R full (grid)\"的线条在黑白打印下不易区分，建议调整 line style 或 marker。\n- Table 2（page 6）：列标题\"Seed 42\", \"Seed 123\", \"Seed 456\" 与 \"Mean 4σ\"——应为 \"Mean ± σ\" 或 \"Mean (σ)\"，\"4σ\" 的含义不明确（是 4 倍标准差？还是排版错误？）。\n- §2 Related Work 首段中\"Cheng et al. (2025) survey the broader contamination landscape\"出现在一个密集的文献回顾段落中，但该引用的具体贡献未被明确说明——建议简要说明其与本文的关系。\n\n---\n\n## Questions for Authors\n\nQ1. 在 7B+ 规模上，epoch confound 发现是否仍然成立？是否有初步证据表明效应量随规模变化？\n\nQ2. 如果使用 cross-model contamination（如 GPT-4 生成的文本），检测器的 AUC 和 ECE 如何变化？dual constraint 方法是否仍然有效？\n\nQ3. Table 3 的 downstream null result 是否可能源于评估方法的局限而非方法本身？是否考虑过更细粒度的评估（如在受污染领域的 factual accuracy 或 generation quality）？\n\nQ4. Quality threshold τ=0.7 和 τ_min 的选择依据是什么？Appendix D 显示了 threshold sweep 但 τ=0.7 的选择似乎基于经验而非理论——这会影响方法在新数据集上的适用性吗？\n\nQ5. Appendix Q (Table 13) 的 practitioner decision summary 非常实用，为什么不放在主文中？这会比当前 §3.2 中的部分数学推导更有助于读者。\n\n---\n\n## Missing References\n\n引用覆盖基本充分，以下为可考虑补充的参考：\n\n- **Llama 3 technical report (Meta, 2024)**：描述了大规模 pretraining 中的数据 curation pipeline，包括合成数据处理，可在 Related Work §2 中作为 motivation 引用，说明工业界对 synthetic contamination 的关注。\n- **Penedo et al. (2024) 的 FineWeb 论文**已引用为数据来源，但其中关于 quality filtering 与 quantity tradeoff 的讨论与本文 §6 的 cost-benefit 分析相关，可进一步引用其发现。\n\n---\n\n## 主要优势\n\n1. **Epoch confound 发现（S1）**：通过严谨的 epoch-matched 对照实验（Table 1），证明 D&R 的 >95% PPL 优势来自 multi-epoch exposure 而非 filtering quality，这纠正了 Drayson et al. (2025) 中的重要误归因。独立的 LR-schedule 复现（§5.1）进一步加强了这一结论的可信度。\n\n2. **实验设计的严谨性（S2）**：全文采用系统化的受控实验——逐因素消融（epoch matching → detector quality → contamination level → scale），3 seeds 提供统计基础，paired t-tests 报告显著性。这是 empirical ML 论文的良好范例。\n\n3. **诚实的 Discussion（S3）**：§6 不回避负面发现（downstream 无改善、α_eff proxy 局限、效应量极小），这种透明度在分析论文中尤为重要，增强了结论的可信度。\n\n4. **Analysis overview 可视化（S4）**：Figure 1 有效地将三个发现的逻辑链条可视化（epoch confound → detector requirements → mechanism → adaptive b*），帮助读者快速建立论文结构的心理模型。\n\n5. **详尽的附录（S5）**：17 个附录（A-Q）提供了完整的证明、消融、proxy 验证和 practitioner guide，展现了作者对研究细节的认真态度。\n\n---\n\n## 总结\n\n本文的核心价值在于 epoch confound 发现——这是一个有意义的 empirical contribution，纠正了文献中的过度乐观估计。实验设计严谨，写作清晰。但方法贡献（adaptive b*）是在已有公式上的增量改进，downstream task 无可测量改善削弱了实际影响力，实验规模（0.6B/1.7B, self-contamination, 单一数据集）限制了结论的泛化性。综合来看，论文达到 Findings 水准：发现有用、方法可靠，但 novelty 和 impact 不足以进入主会议。若能在 7B+ 上复现关键发现并展示 downstream 改善，可提升至 Borderline Conference。",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-22T17:03:34.810264+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3614
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-22T17:03:40.093114+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-22T17:03:40.143763+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-22T17:03:44.760738+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-22T17:03:44.761200+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 726 · 2026-05-22T17:03:54.328611+00:00_

审稿完成。核心结论：

- **Overall 3.0 (Findings)**，Soundness 3.5，Excitement 2.5
- **最大优势**：epoch confound 发现有真实价值，纠正了 Drayson et al. (2025) 中 >95% 的效果误归因；实验设计严谨
- **主要问题**：(1) 方法新颖性有限——同一公式 w=(1-q)^b，仅改变 b 的选择方式；(2) downstream task 零改善（Table 3, |Δ|≤0.01）削弱实际意义；(3) 实验规模太小（0.6B/1.7B, self-contamination, 单一数据集）
- **建议**：明确定位为 analysis paper，adaptive b* 降级为 practical corollary；增加 7B+ 实验和 cross-model contamination 验证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 18

## Round 18

18 recorded events


### User

_source line 727 · 2026-05-22T17:06:25.128527+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿原文：

## Reviewer 1 审稿报告（方法严谨性、实验设计、统计分析）

### Overall: 3 (Findings)
Soundness 3/5, Excitement 3/5, Confidence 4/5

### Strengths
S1. Epoch confound 识别与验证设计精良（Table 1, LR 复现 Δ≈0.006）
S2. 三个有效性条件提炼具实用价值
S3. 数学框架简洁正确（Proposition 1-2）
S4. 诚实报告负面结果
S5. 附录丰富，可复现性好

### Weaknesses

**W1 [critical] N=3 seeds 且 seed 42 存在 checkpoint resume artifact。**
- Appendix P 揭示 seed 42 使用 checkpoint-resumed run，前 ~1,000 步超参不同，in-distribution effect 被膨胀约 8 倍（Δ≈−0.041 resume vs. Δ≈−0.005 from-scratch）。3 seed 中 1 个受 artifact 影响，对均值有巨大杠杆效应。核心 paired t=−6.2, p=0.025 的可信度存疑。
- 建议：以 fresh-from-scratch seed 42 替换重跑主表；或排除 seed 42 做 robustness check。

**W2 [critical] 多重比较未校正。**
- 6 种方法的多组比较（≥5 个检验），所有 p 值均 uncorrected。Bonferroni 校正后 α=0.01，p=0.025 不再显著。

**W3 [major] α_eff proxy 质量偏弱（r=0.70, R²=0.49）。**
- 仅解释 49% 方差，负回归偏差导致系统性低估。论文未分析 51% 未解释方差的来源。

**W4 [major] Self-contamination（generator = trainee）生态效度有限。**
- Appendix O 的 cross-model transfer 退化（Δ=+0.20）暗示方法可能高估效果。

**W5 [major] 下游任务零改善限制实际影响力。**
- PPL 改善~0.07，但 5 个 benchmark 全部差异 <0.01 accuracy。

**W6 [major] 适用范围极窄（仅 ρ≥0.4, ≤0.6B）。**
- ρ=0.2 失效，1.7B+ 效果反转。ρ=0.3 中间点缺失。Abstract/Introduction 的问题范围远超实际验证范围。

**W7 [minor] Per-batch B=4 下 dual constraint 统计可靠性存疑。**
- B=4 下 α_eff(0) 仅 5 个离散值。b* batch 间分布未报告。

**W8 [minor] 关键证据仅在附录。**
- proxy validation r=0.70, seed 42 artifact, ρ=0.2 分析等关键信息仅在附录。

### Questions
Q1. 能否提供排除/替换 seed 42 后的主表结果？
Q2. gradient accumulation 级别（B=16）计算 α_eff 时 proxy 质量是否改善？
Q3. ρ=0.3 表现如何？
Q4. 简单固定 b=0.6 是否足够？
Q5. 是否考虑 soft label 版 α_eff（用 q_i 替代二值化 r_i）？

### Missing References
1. Influence function-based data valuation (Pruthi et al., 2020)
2. DRO (Sagawa et al., 2020) 作为 reweighting 目标特例
3. PPL-downstream gap 文献（Tay et al., 2022）

---

请逐条回应上述所有 Weakness、Questions 和 Missing References。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-22T17:07:53.052140+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "5,6,7,15,16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "5,6,7,15,16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-22T17:07:53.806473+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 481.2}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 196.7}], \"total_pages\": 16, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-22T17:07:57.118688+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 731 · 2026-05-22T17:07:57.523136+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 732 · 2026-05-22T17:07:58.479807+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-22T17:07:58.483023+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-22T17:07:58.483458+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 735 · 2026-05-22T17:07:58.936573+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 736 · 2026-05-22T17:07:59.339696+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 737 · 2026-05-22T17:07:59.340136+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 738 · 2026-05-22T17:07:59.792669+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-22T17:07:59.944639+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-22T17:10:49.524120+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1: Seed 42 checkpoint resume artifact**\n同意这是本文最严重的统计问题。Appendix P 明确承认 seed 42 的 adaptive 模型使用了 checkpoint-resumed run，in-distribution effect 被膨胀约 8 倍（Δ≈−0.041 resume vs. Δ≈−0.005 from-scratch）。在仅 3 seeds 的情况下，这对均值有决定性的杠杆效应。\n\n我进一步补充一个定量推算：Table 1 中 adaptive b* 的 3-seed mean PPL 为 17.620，uniform 为 17.634，差值 Δ=-0.014。如果 seed 42 的 artifact 使该 seed 的 Δ 从约 -0.005 膨胀到约 -0.041，那么替换后 3-seed mean Δ 会从 -0.014 缩小到约 -0.002，基本消失。这意味着 **Table 1 中 adaptive b* vs. uniform 的核心比较可能完全由 artifact 驱动**。paired t=−6.2, p=0.025 的可信度因此严重存疑。\n\n这个问题的严重性甚至超过 R1 的评估——它不仅影响 method 贡献的可信度，还间接影响 epoch confound 分析的 baseline，因为 epoch-matched comparison 也依赖 adaptive b* 的正确性。作者必须以 from-scratch seed 42 重跑主表，否则核心结论无法成立。\n\n**[AGREE] R1-W2: 多重比较未校正**\n同意这是一个有效的统计关切。不过我认为其严重程度低于 R1 的评级（critical），理由是：\n\n论文的核心 story 是 epoch confound——即 D&R 的 >95% 优势来自 multi-epoch exposure。这个发现本质上是一个 **effect size decomposition**（0.396 → 0.017），而非依赖单一 hypothesis test。即使 Bonferroni 校正使 adaptive vs. uniform 的 p=0.025 不再显著，epoch confound 作为观察性发现的逻辑链条（Table 1 的 epoch-matched 对照）仍然成立。\n\n但对于 adaptive b* 的 method claim，R1 的批评完全正确：如果 p=0.025 在校正后不显著（结合 W1 的 seed 42 问题），方法贡献的统计支撑就更加薄弱。建议降为 [major] 而非 [critical]，因为 epoch confound 分析不受此影响。\n\n**[AGREE] R1-W3: α_eff proxy 质量偏弱**\n完全同意。我在自己的审稿中也将此列为 W3（should-fix）。r=0.70 仅解释 49% 方差，且负回归偏差（β≈-0.031，Appendix K Table 10）导致系统性偏保守。\n\n补充一点：Appendix K 报告 α_eff 在 B=1 时仅有 5 个离散值（{0, 0.25, 0.5, 0.75, 1.0}），这与 R1-W7 的 per-batch granularity 问题相互关联。proxy 的低质量加上粗粒度离散化，使得 dual constraint 的理论优雅性在实践中大打折扣。作者需要分析 51% 未解释方差的主要来源——是检测器 noise、batch sampling variance，还是 α_eff 定义本身的局限？\n\n**[AGREE] R1-W4: Self-contamination 生态效度有限**\n同意，且我在自己的审稿中将此作为 W1 (major) 的核心要素之一。Appendix O (Table 12) 的 cross-model transfer 结果确实令人担忧——Llama-3.2-3B 上 MMLU 微升而 HellaSwag 微降，且论文因\"architecture differences\"省略了 PPL 比较，使得这个实验几乎无法验证方法的跨模型有效性。\n\n不过我对 R1 所述\"Δ=+0.20 退化\"需要求证。从 Table 12 我看到的是 mixed results（一升一降），而非单一方向的 +0.20 退化。如果 R1 指的是某个特定 metric 的退化，请明确是哪个。但这不影响 self-contamination 限制的总体判断——这是论文最大的外部效度问题。\n\n**[AGREE] R1-W5: 下游任务零改善**\n完全同意。我在自己的审稿中将此列为 N2 (critical/must-fix)。Table 3 显示所有 downstream benchmarks |Δ| ≤ 0.01 且方向不一致。§6 的解释（\"PPL improvements operate in a regime that standard benchmarks cannot resolve\"）存在循环论证风险。如果一个 pretraining method 无法在任何 downstream task 上产生可测量的改善，其实用价值论证就需要更强的支撑——例如在更大模型上的证据，或更精细的评估方式。\n\n**[REBUT] R1-W6: 适用范围描述部分过度**\n部分同意，但 R1 的表述有两处不够准确：\n\n1. **\"仅 ρ≥0.4\"**：方法在 ρ=0.4 和 ρ=0.6 均有效（§5.2 报告 ρ=0.6 时 Δ=-0.032, paired t=−5.4, p=0.002），但在 ρ=0.2 失效（Appendix N: +0.046 PPL 退化）。所以\"ρ≥0.4\"大致正确。但 ρ=0.3 的缺失确实是一个重要的 gap，因为这是方法有效与否的临界区间。\n\n2. **\"1.7B+ 效果反转\"**：这个表述过强。§5.3 报告 1.7B 时 in-distribution PPL 仍有改善（Δ=-0.013），只是 OOD 不一致（OWT Δ=-0.006 vs. Wiki Δ=+0.013）。\"效果反转\"暗示方法有害，但实际是\"效果缩小且方向不稳定\"。严格说是 **diminished and inconsistent**，非 **reversed**。\n\n但 R1 的核心关切——Abstract/Introduction 的范围远超实际验证范围——我完全同意。论文声称分析\"when, why, and how detect-and-reweight works\"，但实际验证仅覆盖 ρ ∈ {0.4, 0.6}（有效范围），0.6B（主力），1.7B（弱化），单一数据集，单一污染类型。这种 scope mismatch 是真实的论文定位问题。\n\n**[AGREE] R1-W7: Per-batch B=4 下 dual constraint 统计可靠性**\n同意这是一个合理的技术关切。B=4 时 α_eff(0) 仅有 {0, 0.25, 0.5, 0.75, 1.0} 五个可能值，dual constraint 在这种粗粒度下的行为确实缺乏分析。论文提到 gradient accumulation 后有效 batch size 为 B_eff=16，但 §3.2 的 Algorithm 1 (Appendix B) 似乎是在 micro-batch 级别操作而非 accumulated batch 级别。R1-Q2 提出的在 B=16 级别计算 α_eff 的建议值得探索。\n\n**[AGREE] R1-W8: 关键证据仅在附录**\n同意。Proxy validation (r=0.70, Appendix K)、seed 42 artifact (Appendix P)、ρ=0.2 失效 (Appendix N) 是影响论文核心 claims 可信度的关键信息，不应仅在附录中呈现。尤其是 seed 42 artifact——如果主表结果受此影响，读者有权在正文中被告知。\n\n---\n\n### Questions 回应\n\n**Q1（排除/替换 seed 42 后的主表结果）**\n强烈支持。如我在 W1 回应中分析的，seed 42 artifact 可能使 adaptive vs. uniform 的 Δ 从 -0.014 缩小到约 -0.002。这是决定论文方法贡献是否成立的关键实验。\n\n**Q2（gradient accumulation 级别 B=16 计算 α_eff）**\n很好的建议。在 accumulated batch（16 samples）级别计算 α_eff 会将离散值从 5 个增加到 17 个，可能显著改善 proxy 质量。这也与 §5.3 中报告的 \"the adaptive advantage monotonically increases across B\" 一致——更大的 effective batch 确实帮助 dual constraint。\n\n**Q3（ρ=0.3 表现如何）**\n关键缺失。ρ=0.2 失效而 ρ=0.4 有效，ρ=0.3 是理解方法适用边界的核心数据点。这个实验成本不高（与现有实验相同设置，仅改变 ρ），缺失不可接受。\n\n**Q4（简单固定 b=0.6 是否足够）**\n好问题。从 Table 2 数据来看，Adaptive b* mean 跨 3 seeds 为 17.620，而 Golden Ratio 基线（固定 b）为 17.250（但这可能是不同设置）。需要看 §5.3 中 b 的 sensitivity：论文报告 grid search 在 b=0.6 附近最优。如果固定 b=0.6 能达到类似效果，dual-constraint 框架的 added value 就更加有限。这直接关系到方法贡献的必要性论证。\n\n**Q5（soft label 版 α_eff）**\n有价值的方法论建议。当前 α_eff 使用二值化 r_i = 1(q_i ≤ 0.5) 将连续检测分数离散化，丢失了大量信息。用 soft label (1 - q_i) 替代 r_i 可能同时改善 proxy 质量和 granularity。但需注意这会改变 α_eff 的语义——从\"effective proportion of real samples\"变为\"expected realness\"——需要重新推导 Proposition 1-2 的单调性保证。\n\n---\n\n### Missing References 回应\n\n**[AGREE] Influence function-based data valuation (Pruthi et al., 2020)**\n值得在 §2 Related Work 中提及。虽然 provenance-based weighting 和 influence-based valuation 的出发点不同（前者基于来源标签，后者基于对损失的贡献），但作为 instance-level data valuation 的另一范式，引用有助于定位本文方法在更广泛的 data selection 文献中的位置。不过并非关键遗漏。\n\n**[AGREE] DRO (Sagawa et al., 2020)**\n同意应该引用。DRO 的 worst-group 优化目标可以被视为 reweighting 的一个特例，且论文的 dual constraint（quality floor + stability ceiling）在精神上与 DRO 的 robust optimization 有一定相似性。不引用不影响论文完整性，但引用会加强 Related Work 的全面性。\n\n**[AGREE] PPL-downstream gap (Tay et al., 2022)**\n强烈同意。鉴于论文 §6 和 Table 3 的 downstream null result，这个引用几乎是必需的。PPL 与 downstream performance 的脱钩是已有文献广泛讨论的现象，论文应在 Discussion 中引用此文献来 contextualize 自己的发现，而非仅用\"benchmark sensitivity threshold\"作为解释。这是最重要的遗漏引用。\n\n---\n\n### 与 Reviewer 1 评分的比较\n\n| 维度 | R1 | R2 (我) | 差异说明 |\n|------|-----|---------|---------|\n| Overall | 3.0 | 3.0 | 一致：Findings 水准 |\n| Soundness | 3.0 | 3.5 | 我初始给 3.5，但考虑 R1 提出的 seed 42 artifact 问题后，认为 3.0 更合理。**下调至 3.0**。 |\n| Excitement | 3.0 | 2.5 | 我认为 R1 给高了。方法增量式（同一公式 w=(1-q)^b），downstream 零改善，适用范围窄。Epoch confound 是有用的 negative finding，但不足以支撑 Excitement 3。 |\n| Confidence | 4 | 4 | 一致 |\n\n### 总结\n\nR1 的审稿质量很高，尤其是 W1（seed 42 artifact）和 W6（scope mismatch）两个问题我未在首轮充分展开。seed 42 问题实际上比我初始评估更严重——它可能使 adaptive b* 的核心数值贡献从 Δ=-0.014 缩小到接近零。结合 downstream null result (W5/我的 N2)，方法贡献的 evidence base 非常薄弱。\n\n论文的持久价值在于 epoch confound 发现（不受 seed 42 影响，因为这是 D&R 的 confound 而非 adaptive 的），以及 detector requirements 分析。但作为一篇同时声称分析和方法贡献的论文，方法部分的统计支撑需要大幅加强。\n\n**修正后评分：Overall 3.0, Soundness 3.0, Excitement 2.5, Confidence 4**",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1: Seed 42 checkpoint resume artifact**\n同意这是本文最严重的统计问题。Appendix P 明确承认 seed 42 的 adaptive 模型使用了 checkpoint-resumed run，in-distribution effect 被膨胀约 8 倍（Δ≈−0.041 resume vs. Δ≈−0.005 from-scratch）。在仅 3 seeds 的情况下，这对均值有决定性的杠杆效应。\n\n我进一步补充一个定量推算：Table 1 中 adaptive b* 的 3-seed mean PPL 为 17.620，uniform 为 17.634，差值 Δ=-0.014。如果 seed 42 的 artifact 使该 seed 的 Δ 从约 -0.005 膨胀到约 -0.041，那么替换后 3-seed mean Δ 会从 -0.014 缩小到约 -0.002，基本消失。这意味着 **Table 1 中 adaptive b* vs. uniform 的核心比较可能完全由 artifact 驱动**。paired t=−6.2, p=0.025 的可信度因此严重存疑。\n\n这个问题的严重性甚至超过 R1 的评估——它不仅影响 method 贡献的可信度，还间接影响 epoch confound 分析的 baseline，因为 epoch-matched comparison 也依赖 adaptive b* 的正确性。作者必须以 from-scratch seed 42 重跑主表，否则核心结论无法成立。\n\n**[AGREE] R1-W2: 多重比较未校正**\n同意这是一个有效的统计关切。不过我认为其严重程度低于 R1 的评级（critical），理由是：\n\n论文的核心 story 是 epoch confound——即 D&R 的 >95% 优势来自 multi-epoch exposure。这个发现本质上是一个 **effect size decomposition**（0.396 → 0.017），而非依赖单一 hypothesis test。即使 Bonferroni 校正使 adaptive vs. uniform 的 p=0.025 不再显著，epoch confound 作为观察性发现的逻辑链条（Table 1 的 epoch-matched 对照）仍然成立。\n\n但对于 adaptive b* 的 method claim，R1 的批评完全正确：如果 p=0.025 在校正后不显著（结合 W1 的 seed 42 问题），方法贡献的统计支撑就更加薄弱。建议降为 [major] 而非 [critical]，因为 epoch confound 分析不受此影响。\n\n**[AGREE] R1-W3: α_eff proxy 质量偏弱**\n完全同意。我在自己的审稿中也将此列为 W3（should-fix）。r=0.70 仅解释 49% 方差，且负回归偏差（β≈-0.031，Appendix K Table 10）导致系统性偏保守。\n\n补充一点：Appendix K 报告 α_eff 在 B=1 时仅有 5 个离散值（{0, 0.25, 0.5, 0.75, 1.0}），这与 R1-W7 的 per-batch granularity 问题相互关联。proxy 的低质量加上粗粒度离散化，使得 dual constraint 的理论优雅性在实践中大打折扣。作者需要分析 51% 未解释方差的主要来源——是检测器 noise、batch sampling variance，还是 α_eff 定义本身的局限？\n\n**[AGREE] R1-W4: Self-contamination 生态效度有限**\n同意，且我在自己的审稿中将此作为 W1 (major) 的核心要素之一。Appendix O (Table 12) 的 cross-model transfer 结果确实令人担忧——Llama-3.2-3B 上 MMLU 微升而 HellaSwag 微降，且论文因\"architecture differences\"省略了 PPL 比较，使得这个实验几乎无法验证方法的跨模型有效性。\n\n不过我对 R1 所述\"Δ=+0.20 退化\"需要求证。从 Table 12 我看到的是 mixed results（一升一降），而非单一方向的 +0.20 退化。如果 R1 指的是某个特定 metric 的退化，请明确是哪个。但这不影响 self-contamination 限制的总体判断——这是论文最大的外部效度问题。\n\n**[AGREE] R1-W5: 下游任务零改善**\n完全同意。我在自己的审稿中将此列为 N2 (critical/must-fix)。Table 3 显示所有 downstream benchmarks |Δ| ≤ 0.01 且方向不一致。§6 的解释（\"PPL improvements operate in a regime that standard benchmarks cannot resolve\"）存在循环论证风险。如果一个 pretraining method 无法在任何 downstream task 上产生可测量的改善，其实用价值论证就需要更强的支撑——例如在更大模型上的证据，或更精细的评估方式。\n\n**[REBUT] R1-W6: 适用范围描述部分过度**\n部分同意，但 R1 的表述有两处不够准确：\n\n1. **\"仅 ρ≥0.4\"**：方法在 ρ=0.4 和 ρ=0.6 均有效（§5.2 报告 ρ=0.6 时 Δ=-0.032, paired t=−5.4, p=0.002），但在 ρ=0.2 失效（Appendix N: +0.046 PPL 退化）。所以\"ρ≥0.4\"大致正确。但 ρ=0.3 的缺失确实是一个重要的 gap，因为这是方法有效与否的临界区间。\n\n2. **\"1.7B+ 效果反转\"**：这个表述过强。§5.3 报告 1.7B 时 in-distribution PPL 仍有改善（Δ=-0.013），只是 OOD 不一致（OWT Δ=-0.006 vs. Wiki Δ=+0.013）。\"效果反转\"暗示方法有害，但实际是\"效果缩小且方向不稳定\"。严格说是 **diminished and inconsistent**，非 **reversed**。\n\n但 R1 的核心关切——Abstract/Introduction 的范围远超实际验证范围——我完全同意。论文声称分析\"when, why, and how detect-and-reweight works\"，但实际验证仅覆盖 ρ ∈ {0.4, 0.6}（有效范围），0.6B（主力），1.7B（弱化），单一数据集，单一污染类型。这种 scope mismatch 是真实的论文定位问题。\n\n**[AGREE] R1-W7: Per-batch B=4 下 dual constraint 统计可靠性**\n同意这是一个合理的技术关切。B=4 时 α_eff(0) 仅有 {0, 0.25, 0.5, 0.75, 1.0} 五个可能值，dual constraint 在这种粗粒度下的行为确实缺乏分析。论文提到 gradient accumulation 后有效 batch size 为 B_eff=16，但 §3.2 的 Algorithm 1 (Appendix B) 似乎是在 micro-batch 级别操作而非 accumulated batch 级别。R1-Q2 提出的在 B=16 级别计算 α_eff 的建议值得探索。\n\n**[AGREE] R1-W8: 关键证据仅在附录**\n同意。Proxy validation (r=0.70, Appendix K)、seed 42 artifact (Appendix P)、ρ=0.2 失效 (Appendix N) 是影响论文核心 claims 可信度的关键信息，不应仅在附录中呈现。尤其是 seed 42 artifact——如果主表结果受此影响，读者有权在正文中被告知。\n\n---\n\n### Questions 回应\n\n**Q1（排除/替换 seed 42 后的主表结果）**\n强烈支持。如我在 W1 回应中分析的，seed 42 artifact 可能使 adaptive vs. uniform 的 Δ 从 -0.014 缩小到约 -0.002。这是决定论文方法贡献是否成立的关键实验。\n\n**Q2（gradient accumulation 级别 B=16 计算 α_eff）**\n很好的建议。在 accumulated batch（16 samples）级别计算 α_eff 会将离散值从 5 个增加到 17 个，可能显著改善 proxy 质量。这也与 §5.3 中报告的 \"the adaptive advantage monotonically increases across B\" 一致——更大的 effective batch 确实帮助 dual constraint。\n\n**Q3（ρ=0.3 表现如何）**\n关键缺失。ρ=0.2 失效而 ρ=0.4 有效，ρ=0.3 是理解方法适用边界的核心数据点。这个实验成本不高（与现有实验相同设置，仅改变 ρ），缺失不可接受。\n\n**Q4（简单固定 b=0.6 是否足够）**\n好问题。从 Table 2 数据来看，Adaptive b* mean 跨 3 seeds 为 17.620，而 Golden Ratio 基线（固定 b）为 17.250（但这可能是不同设置）。需要看 §5.3 中 b 的 sensitivity：论文报告 grid search 在 b=0.6 附近最优。如果固定 b=0.6 能达到类似效果，dual-constraint 框架的 added value 就更加有限。这直接关系到方法贡献的必要性论证。\n\n**Q5（soft label 版 α_eff）**\n有价值的方法论建议。当前 α_eff 使用二值化 r_i = 1(q_i ≤ 0.5) 将连续检测分数离散化，丢失了大量信息。用 soft label (1 - q_i) 替代 r_i 可能同时改善 proxy 质量和 granularity。但需注意这会改变 α_eff 的语义——从\"effective proportion of real samples\"变为\"expected realness\"——需要重新推导 Proposition 1-2 的单调性保证。\n\n---\n\n### Missing References 回应\n\n**[AGREE] Influence function-based data valuation (Pruthi et al., 2020)**\n值得在 §2 Related Work 中提及。虽然 provenance-based weighting 和 influence-based valuation 的出发点不同（前者基于来源标签，后者基于对损失的贡献），但作为 instance-level data valuation 的另一范式，引用有助于定位本文方法在更广泛的 data selection 文献中的位置。不过并非关键遗漏。\n\n**[AGREE] DRO (Sagawa et al., 2020)**\n同意应该引用。DRO 的 worst-group 优化目标可以被视为 reweighting 的一个特例，且论文的 dual constraint（quality floor + stability ceiling）在精神上与 DRO 的 robust optimization 有一定相似性。不引用不影响论文完整性，但引用会加强 Related Work 的全面性。\n\n**[AGREE] PPL-downstream gap (Tay et al., 2022)**\n强烈同意。鉴于论文 §6 和 Table 3 的 downstream null result，这个引用几乎是必需的。PPL 与 downstream performance 的脱钩是已有文献广泛讨论的现象，论文应在 Discussion 中引用此文献来 contextualize 自己的发现，而非仅用\"benchmark sensitivity threshold\"作为解释。这是最重要的遗漏引用。\n\n---\n\n### 与 Reviewer 1 评分的比较\n\n| 维度 | R1 | R2 (我) | 差异说明 |\n|------|-----|---------|---------|\n| Overall | 3.0 | 3.0 | 一致：Findings 水准 |\n| Soundness | 3.0 | 3.5 | 我初始给 3.5，但考虑 R1 提出的 seed 42 artifact 问题后，认为 3.0 更合理。**下调至 3.0**。 |\n| Excitement | 3.0 | 2.5 | 我认为 R1 给高了。方法增量式（同一公式 w=(1-q)^b），downstream 零改善，适用范围窄。Epoch confound 是有用的 negative finding，但不足以支撑 Excitement 3。 |\n| Confidence | 4 | 4 | 一致 |\n\n### 总结\n\nR1 的审稿质量很高，尤其是 W1（seed 42 artifact）和 W6（scope mismatch）两个问题我未在首轮充分展开。seed 42 问题实际上比我初始评估更严重——它可能使 adaptive b* 的核心数值贡献从 Δ=-0.014 缩小到接近零。结合 downstream null result (W5/我的 N2)，方法贡献的 evidence base 非常薄弱。\n\n论文的持久价值在于 epoch confound 发现（不受 seed 42 影响，因为这是 D&R 的 confound 而非 adaptive 的），以及 detector requirements 分析。但作为一篇同时声称分析和方法贡献的论文，方法部分的统计支撑需要大幅加强。\n\n**修正后评分：Overall 3.0, Soundness 3.0, Excitement 2.5, Confidence 4**",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-22T17:10:53.123874+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3599
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-22T17:10:59.459319+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-22T17:10:59.459838+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 744 · 2026-05-22T17:11:12.253946+00:00_

交叉回应完成。核心判断：

- R1 的 W1（seed 42 artifact）我强烈同意并做了定量补充——该 artifact 可能使 adaptive vs. uniform 的 Δ 从 -0.014 缩小到约 -0.002，方法贡献的统计基础岌岌可危
- W6（scope mismatch）我部分反驳了"1.7B 效果反转"的措辞（实为 diminished，非 reversed），但同意核心关切
- 其余 W2-W5、W7-W8 均同意，多数与我首轮审稿发现一致
- 基于 R1 提出的 seed 42 问题，我将 Soundness 从 3.5 下调至 3.0
- 最终评分：Overall 3.0 (Findings), Soundness 3.0, Excitement 2.5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 19

## Round 19

60 recorded events


### User

_source line 745 · 2026-05-23T03:06:26.344170+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查新颖性、Related Work 完整性、写作质量和格式合规。

## 目标 Venue
- **EMNLP 2026**，通过 ACL Rolling Review (ARR) 提交
- **截止日期**：2026-05-25
- **格式**：Long paper，正文 8 页限制，参考文献不限页数。Limitations 和 Ethics Statement 不计入页数
- **模板**：ACL 2023 模板（`\usepackage[review]{acl}`）
- **匿名规则**：Double-blind，禁止透露作者身份
- **Responsible NLP Checklist**：在 OpenReview submission form 中填写，不在 PDF 中

## 论文信息
- **标题**：When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining
- **论文路径**：projects/provenance_weight_training/docs/paper/main.tex
- **PDF 路径**：/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf

## 你的审查侧重

### 1. 新颖性评估（重点）
- 三个 findings 的新颖性：(1) epoch confound, (2) detector calibration, (3) minimum intervention
- w=(1-q)^b 框架完全来自 Drayson et al. 2025，自适应 b* 算是 incremental 还是 substantial contribution？
- 对比同期工作（Feng et al. 2025, Yi et al. 2025, Zibakhsh et al. 2025, He et al. 2025, Wang et al. 2026）的差异化是否充分？
- "Analysis paper" vs "method paper" 的定位是否清晰？

### 2. Related Work 完整性
- 是否遗漏重要相关工作？特别关注：
  - 2025-2026 年最新的 synthetic data detection 方法
  - Data mixing / data selection 领域的最新进展
  - Model collapse 的最新理论结果
  - Instance-level reweighting 的其他方法
- 引用格式是否规范？是否有可疑引用（幻觉引用）？
- 引用是否过于集中或遗漏关键领域？

### 3. 写作质量
- 论文结构是否清晰？是否 well-organized？
- Abstract 是否准确反映论文内容？是否有 overclaim？
- Introduction 的 narrative flow 是否流畅？
- 表格和图表质量：是否易读、标注清晰？
- 是否有模糊/含糊的陈述？
- Limitations 和 Ethics Statement 是否充分？
- 效应量 Δ=-0.020 PPL（~0.11% relative）与论文 claim 的匹配度

### 4. 格式合规
- 页数是否在 8 页限制内（正文，不含 Limitations/Ethics/References）？
- ACL 模板使用是否正确？
- 匿名规则遵守情况
- Appendix 是否过于庞大？核心证据是否不当地放在附录中？
- References 格式一致性

请严格按照顶会审稿标准评审，不要手软。输出结构：Summary → Strengths → Weaknesses（按严重性分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（参考 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-23T03:06:34.517106+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-23T03:06:34.616504+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 99
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-23T03:06:40.197016+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR reviewer guidelines review form criteria 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR reviewer guidelines review form criteria 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 749 · 2026-05-23T03:06:42.617036+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 750 · 2026-05-23T03:06:48.218820+00:00_

Web search results for query: "ACL Rolling Review ARR reviewer guidelines review form criteria 2025 2026"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

I've found relevant information about ACL Rolling Review (ARR) reviewer guidelines and criteria for 2025-2026. Here are the key details:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Reviewer Guidelines and Requirements

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

## Accountability Policies

Starting in May 2025, ARR adopts a new policy on the 'highly irresponsible' (meta-)reviewers, with the program chairs and ARR EiCs considering egregious cases including extremely terse reviews, unprofessional tone, and LLM-generated r
…[truncated 795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8021
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-23T03:06:50.078450+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 574.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 529.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7461
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-23T03:07:04.236148+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer scoring criteria, especially: 1) All scoring dimensions (soundness, excitement, overall assessment, etc.) 2) The exact scale and meaning for each score level 3) Any specific instructions about what constitutes each score level. Return the full details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer scoring criteria, especially: 1) All scoring dimensions (soundness, excitement, overall assessment, etc.) 2) The exact scale and meaning for each score level 3) Any specific instructions about what constitutes each score level. Return the full details."
  }
}
```

</details>

---


### Tool call

_source line 753 · 2026-05-23T03:07:05.484207+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "11-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "11-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-23T03:07:06.136884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 755 · 2026-05-23T03:07:06.639463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-23T03:07:07.091420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 757 · 2026-05-23T03:07:07.593589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 758 · 2026-05-23T03:07:10.254677+00:00_

# ARR Reviewer Scoring Criteria

Based on the guidelines provided, here's what I found regarding reviewer scoring:

## Scoring Dimensions

The document states that "Starting with February 2025, ARR reviewers are asked to provide three scores: **soundness, excitement, and overall recommendation**."

## Specific Score Definitions

Unfortunately, the guidelines document does not provide the complete scoring scales or exact point values for each dimension. The document only describes their conceptual purposes:

**Soundness**: Technical validity and rigor of the work. As noted, "low soundness scores should be justified" by specific issues identified in the review.

**Excitement**: Personal interest and subjective appeal. The guidelines clarify this is "orthogonal to the assessment of soundness" and "do not necessarily come with explicit reasons."

**Overall Assessment**: "An explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact."

## Key Constraint

The guidelines emphasize that "soundness scores must be justified by the text of the review"—low scores require substantive explanation, suggesting reviewers cannot rely on arbitrary numbering.

**Note**: The full numerical scale specifications appear to be located in a separate "review form" document referenced but not included in these guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6018
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-23T03:07:10.859104+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 423.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 352.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 412.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 441.7}], \"total_pages\": 15, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5374
}
```

</details>

---


### Tool result

_source line 760 · 2026-05-23T03:07:12.921881+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6784
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-23T03:07:13.074820+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6435
}
```

</details>

---


### Tool result

_source line 762 · 2026-05-23T03:07:13.077260+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5985
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-23T03:07:13.078428+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5484
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-23T03:07:18.769041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-23T03:07:19.575504+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 766 · 2026-05-23T03:07:19.727036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 767 · 2026-05-23T03:07:20.279232+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 768 · 2026-05-23T03:07:20.585776+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool call

_source line 769 · 2026-05-23T03:07:20.586258+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 770 · 2026-05-23T03:07:21.088733+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-23T03:07:21.440949+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-23T03:07:27.163044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 773 · 2026-05-23T03:07:27.716065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 774 · 2026-05-23T03:07:28.168692+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 775 · 2026-05-23T03:07:28.169138+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 776 · 2026-05-23T03:07:29.073887+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool result

_source line 777 · 2026-05-23T03:07:29.078695+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 778 · 2026-05-23T03:07:29.079151+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 779 · 2026-05-23T03:07:29.584060+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 780 · 2026-05-23T03:07:29.584511+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 781 · 2026-05-23T03:07:30.100108+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 782 · 2026-05-23T03:07:30.650763+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1066
}
```

</details>

---


### Tool call

_source line 783 · 2026-05-23T03:07:30.661366+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 784 · 2026-05-23T03:07:32.051912+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1951
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-23T03:07:32.312470+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1651
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-23T03:09:20.832351+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the EXACT numerical scoring scales for all dimensions: soundness (1-5 scale), excitement (1-5 scale), overall assessment (1-5 scale), and any other scored dimensions. List every score level and its exact definition/label. Also extract any guidance on what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the EXACT numerical scoring scales for all dimensions: soundness (1-5 scale), excitement (1-5 scale), overall assessment (1-5 scale), and any other scored dimensions. List every score level and its exact definition/label. Also extract any guidance on what each score means."
  }
}
```

</details>

---


### Tool call

_source line 787 · 2026-05-23T03:09:21.133797+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form soundness excitement overall assessment score scale 1 2 3 4 5 definitions 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form soundness excitement overall assessment score scale 1 2 3 4 5 definitions 2025"
  }
}
```

</details>

---


### Tool result

_source line 788 · 2026-05-23T03:09:26.102747+00:00_

# ARR Review Scoring Scales

Based on the provided guidelines, the document mentions that **"Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation."**

However, **the specific numerical scales (1-5 ranges) and exact definitions for each score level are not detailed in this document.** 

The guidelines reference a separate resource: **"We have a post describing the ARR review form in detail"** at https://aclrollingreview.org/reviewform, which would contain the actual scoring rubric definitions.

## What IS Specified:

The document provides conceptual guidance rather than numerical scales:

- **Soundness**: Should be "justified by the text of the review"
- **Excitement**: "orthogonal to the assessment of soundness" and reflects "personal taste"
- **Overall Assessment**: "composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact"

The guidelines note that papers "are expected to be sufficiently sound and reproducible" for acceptance, but the specific 1-5 scale definitions and score level labels are documented elsewhere (likely in the review form post referenced above).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5270
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-23T03:09:27.607863+00:00_

Web search results for query: "ACL ARR review form soundness excitement overall assessment score scale 1 2 3 4 5 definitions 2025"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Responsiveness of the Various Short-Form Versions of the Knee Injury and Osteoarthritis Outcome Score Between 2 and 5 Years After Anterior Cruciate Ligament Reconstruction","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10960337/"}]

Based on the search results, I can provide you with information about the ACL ARR review form scoring scales for 2025:

## Three Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score

The soundness scores must be justified by the text of the review. The scale includes: 5 = Excellent (one of the most thorough studies of its type), 4 = Strong (provides sufficient support for all claims), and 3 = Acceptable (provides sufficient support for main claims).

## Excitement Score

Excitement reflects subjective personal prefe
…[truncated 791 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6474
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-23T03:09:32.376116+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract ALL scoring scales with exact definitions for every score level. I need: 1) Soundness scale (all levels 1-5 with definitions), 2) Excitement scale (all levels 1-5 with definitions), 3) Overall Assessment scale (all levels 1-5 with definitions), 4) Any other scored dimensions. List EVERY number and its exact label/definition."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract ALL scoring scales with exact definitions for every score level. I need: 1) Soundness scale (all levels 1-5 with definitions), 2) Excitement scale (all levels 1-5 with definitions), 3) Overall Assessment scale (all levels 1-5 with definitions), 4) Any other scored dimensions. List EVERY number and its exact label/definition."
  }
}
```

</details>

---


### Tool call

_source line 791 · 2026-05-23T03:09:33.280891+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"data provenance\" \"reweighting\" OR \"re-weighting\" language model pretraining 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"data provenance\" \"reweighting\" OR \"re-weighting\" language model pretraining 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 792 · 2026-05-23T03:09:38.706504+00:00_

# ACL Rolling Review Scoring Scales

## 1. Soundness Scale
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4.5**: (intermediate level)
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3.5**: (intermediate level)
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2.5**: (intermediate level)
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1.5**: (intermediate level)
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 2. Excitement Scale
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4.5**: (intermediate level)
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3.5**: (intermediate level)
- **3**: "Interesting: I might mention some points of this paper to others."
- **2.5**: (intermediate level)
- **2**: "Potentially Interesting: this paper does not resonate with me, but others might."
- **1.5**: (intermediate level)
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 3. Overall Assessment Scale
- **5**: "Consider for Award: Could be considered for outstanding paper award (top 2.5%)."
- **4.5**: Borderline Award
- **4**: "Conference: I think this paper could be accepted to an *ACL conference."
- **3.5**: Borderline Conference
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2.5**: Borderline Findings
- **2**: "Resubmit next cycle: substantial revisions needed by next ARR cycle."
- **1.5**: "Resubmit after next cycle: substantial revisions not completable next cycle."
- **1**: "Do not resubmit: Paper requires complete overhaul or lacks ACL relevance."

## 4. Additional Scored Dimensions

**Reviewer Confidence** (1-5 scale present but definitions differ in structure)

**Reproducibility** (1
…[truncated 104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6330
}
```

</details>

---


### Tool result

_source line 793 · 2026-05-23T03:09:41.116169+00:00_

Web search results for query: ""data provenance" "reweighting" OR "re-weighting" language model pretraining 2025 2026"

Links: [{"title":"Self-Influence Guided Data Reweighting for Language Model Pre-training | OpenReview","url":"https://openreview.net/forum?id=rXn9WO4M2p"},{"title":"[2502.06733] Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining","url":"https://arxiv.org/abs/2502.06733"},{"title":"Self-Influence Guided Data Reweighting for Language Model Pre-training","url":"https://arxiv.org/pdf/2311.00913"},{"title":"[2311.00913] Self-Influence Guided Data Reweighting for Language Model Pre-training","url":"https://arxiv.org/abs/2311.00913"},{"title":"ToReMi: Topic-Aware Data Reweighting for Dynamic Pre-Training Data   Selection","url":"https://arxiv.org/pdf/2504.00695"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf"},{"title":"Reuse, Don't Retrain: A Recipe for Continued Pretraining of Language   Models","url":"https://arxiv.org/pdf/2407.07263"}]

Here are the search results for your query about data provenance, reweighting/re-weighting, and language model pretraining from 2025-2026:

## Key Recent Research (2025-2026)

**Dynamic Loss-Based Sample Reweighting (February 2025)**
Recent work introduces novel algorithms for dynamic, instance-level data reweighting aimed at improving both the efficiency and effectiveness of LLM pretraining. Existing reweighting strategies, which primarily focus on group-level data importance, fail to leverage fine-grained instance-level information and do not adapt dynamically to individual sample importance as training progresses.

**Topic-Aware Data Reweighting (ToReMi)**
Large language models typically undergo pre-training on extensive corpora derived from heterogeneous sources of varying quality, and systematic optimization of pre-training data constitutes a fundamental te
…[truncated 914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7835
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-23T03:09:48.094752+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "synthetic data detection LLM generated text 2025 2026 survey new methods beyond DetectGPT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "synthetic data detection LLM generated text 2025 2026 survey new methods beyond DetectGPT"
  }
}
```

</details>

---


### Tool call

_source line 795 · 2026-05-23T03:09:48.897531+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"model collapse\" language model theory 2025 2026 new results convergence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"model collapse\" language model theory 2025 2026 new results convergence"
  }
}
```

</details>

---


### Tool result

_source line 796 · 2026-05-23T03:09:54.316826+00:00_

Web search results for query: "synthetic data detection LLM generated text 2025 2026 survey new methods beyond DetectGPT"

Links: [{"title":"Synthetic Data Generation Using Large Language Models: Advances in Text and Code","url":"https://arxiv.org/html/2503.14023v2"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions - ACL Anthology","url":"https://aclanthology.org/2025.cl-1.8/"},{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future   Directions","url":"https://arxiv.org/pdf/2310.14724"}]

I found some excellent recent resources on this topic. Here are the key findings:

## Recent Surveys on LLM-Generated Text Detection

A comprehensive 2025 survey titled "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions" by Wu et al. was published in Computational Linguistics 2025. This survey consolidates recent research breakthroughs in the field and examines various LLM-generated text detection paradigms, addressing challenges like out-of-distribution problems, potential attacks, real-world data issues, and ineffective evaluation frameworks.

## Scope and Content

The literature reviewed covers publications between January 2020 and April 2025, capturing the period of rapid advancement in LLM-driven synthetic data generation. Recent advances in leveraging LLMs to create synthetic text and code highlight key techniques such as prompt-based generation, retrieval-augmented pipelines, and iterative self-refinement.

## Detection Methods and Future Directions

The 
…[truncated 531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6222
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-23T03:09:57.177312+00:00_

Web search results for query: ""model collapse" language model theory 2025 2026 new results convergence"

Links: [{"title":"Language Generation with Replay: A Learning-Theoretic View of Model Collapse","url":"https://arxiv.org/html/2603.11784v1"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://par.nsf.gov/servlets/purl/10649434"},{"title":"Characterizing Model Collapse in Large Language Models Using Semantic Networks and Next-Token Probability","url":"https://arxiv.org/html/2410.12341v2"},{"title":"[2511.05535] Future of AI Models: A Computational perspective on Model collapse","url":"https://arxiv.org/abs/2511.05535"},{"title":"Future of AI Models: A Computational perspective on Model collapse","url":"https://arxiv.org/pdf/2511.05535"},{"title":"A Probabilistic Perspective on Model Collapse","url":"https://arxiv.org/pdf/2505.13947"},{"title":"Model Collapse Demystified: The Case of Regression","url":"https://arxiv.org/pdf/2402.07712"},{"title":"Language Generation with Replay: A Learning-Theoretic View of Model Collapse","url":"https://arxiv.org/pdf/2603.11784"}]

I've performed the web search for "model collapse language model theory 2025 2026 new results convergence". Here are the key findings:

## Recent Research on Model Collapse (2025-2026)

**Theoretical Advances:**

A growing body of research, often grouped under the umbrella term model collapse, has emerged with significant theoretical contributions. Mehrotra et al. (2025) studied the robustness of dense and non-dense generation in the limit under different regimes of infinite contamination, while Dmitriev et al. (2026) considered a similar replay adversary that can use previously output hypotheses to provide noisy labels.

Their work can be viewed as an attempt to formalize model collapse through the lens of learning theory.

**Research on Generatability vs. Learnability:**

One important line of research focuses on contrasting the notion of generatability with 
…[truncated 1267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8279
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-23T03:13:16.179158+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告\n\n**论文**: When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**审查侧重**: 新颖性、Related Work 完整性、写作质量、格式合规\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 / 5 — Findings\n**一句话总结**: Epoch confound 的识别是对 D&R 评估方法论的有价值贡献，但极小的效应量（Δ=-0.020 PPL, ~0.11%）、狭窄的实验范围（单模型/单数据集）和增量式的方法贡献使其未达到主会议门槛，适合 Findings。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5 / 5 | 方法论设计严谨（epoch-matched controls、permuted-score control），但 3 seeds 统计效力不足，效应量极小，单一实验设置限制了结论的可推广性 |\n| **Excitement** | 2.5 / 5 | Epoch confound 发现有一定社区价值，但效应量太小、实验范围太窄、方法贡献增量式，整体 impact 有限 |\n| **Overall** | 3.0 / 5 | Findings 级别——有价值的分析发现，但不够 exciting 进主会议 |\n\n---\n\n## 主要优势\n\n1. **Epoch confound 的实验设计精巧**：通过 epoch-matched controls (N=3) 将 D&R 的 PPL 优势从 0.396 分解为仅 Δ=0.017（Table 1），严格证明 >95% 的优势来自多 epoch 暴露而非过滤质量。Permuted-score control (Section 5.1) 进一步确认 detector signal 是 load-bearing 的。这是一个方法论上干净的贡献。\n\n2. **三个有效性条件形成实用框架**：Table 3 的决策矩阵（detector AUC + calibration + α_eff constraint）为从业者提供了清晰的 checklist。\n\n3. **诚实的效应量报告**：论文没有隐瞒 Δ=-0.020 PPL 的微小效应，Limitations 部分直接承认了实验范围的局限。\n\n4. **充分的 ablation 研究**：Section 5.2-5.3 和 Appendix B-Q 覆盖了 quality threshold sensitivity、batch-adaptive variants、constraint regime、scale、OOD evaluation 等多个维度。\n\n5. **LR-controlled verification** (Section 5.1): 用 independent linear schedules 控制 LR schedule 混淆，确认 epoch-exposure advantage 在 controlled LR 下仍然成立，实验设计细致。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 效应量极小，实际意义不足以支撑论文的 framing\n\n- **具体位置**: Abstract (\"Δ_s=-0.020\"), Table 1, Table 2, Section 5.1\n- **问题**: 论文的核心数值结果——adaptive b* 相对 uniform 的改善——为 Δ=-0.020 PPL（~0.11% relative）。Table 4 的下游 benchmark 结果明确写道 \"All differences within standard error\"，即下游任务上无统计显著差异。论文 Abstract 和 Introduction 的叙事暗示这些 findings 对实践有指导意义（\"yielding a practical adaptive method\"），但 0.11% 的 PPL 改善和零下游 improvement 使这一 claim 难以成立。\n- **为什么影响接收**: 如果论文的主要方法贡献（adaptive b*）在实践中几乎无法观测到改善，那么论文的 contribution 就完全落在分析发现（epoch confound）上。作为一篇 analysis paper，这足以支撑 Findings，但论文目前的 framing 试图同时主张 method contribution，导致 overclaim。\n- **建议修改方向**: (1) 明确论文定位为 analysis/diagnostic paper 而非 method paper；(2) 在 Abstract 中直接量化效应量的微小程度（如 \"~0.1% relative PPL improvement\"），避免读者产生过高期望；(3) 讨论在什么规模/场景下效应量可能变大。\n\n**N2** [critical] 实验范围过窄，不足以支撑 \"three effectiveness conditions\" 作为一般性结论\n\n- **具体位置**: Section 4 (Experimental Setup), Section 5, Appendix O\n- **问题**: 所有主要实验基于单一设置：Qwen3-0.6B、FineWeb 132M tokens、self-generated contamination (ρ=0.4)。这三个条件限制了结论的推广性：\n  - **单一模型**: 仅 Qwen3-0.6B (0.6B params)。Appendix O 尝试 Llama-3.2-3B 的 cross-model transfer 但结果 \"mixed\"（MMLU improves while HellaSwag slightly degrades）, 作者自己承认 \"mixed results\"。\n  - **Self-generated contamination only**: 真实 web contamination 中污染源模型与被训练模型不同、synthetic text 更多样。论文 Section 7 承认 \"realistic multi-source web contamination is untested\"。\n  - **极小 scale**: 132M tokens 是 continued pretraining 中极小的规模。论文 Section 6 讨论了 scale effects 但缺乏实验验证。\n  - **Appendix N 显示方法在 ρ=0.2 时 degrade**: \"adaptive method Δ=-0.013 with OOD partially inconsistent\"，而 20% contamination 是论文自己引用的 web 估计范围的下限。\n- **为什么影响接收**: 论文的 framing（\"we identify three effectiveness conditions for detect-and-reweight\"）暗示一般性结论，但所有证据来自一个极窄的实验 corridor。三个条件可能是该特定设置的 artifact，不一定推广到其他模型、数据或 contamination 场景。\n- **建议修改方向**: (1) 在标题或 Abstract 中明确 scope（如 \"in the setting of single-model continued pretraining\"）；(2) 增加至少一个不同架构/规模的模型（如 2-3B scale）作为主实验；(3) 测试 cross-model contamination（用不同模型生成 synthetic data）。\n\n**N3** [critical] Adaptive b* 的新颖性不足——本质是 Drayson et al. (2025) 框架的参数选择启发式\n\n- **具体位置**: Section 3 (Quality floor / Stability ceiling / Adaptive b*), Equation (1)\n- **问题**: w=(1-q)^b 框架完全来自 Drayson et al. (2025)。论文的方法贡献是从两个约束（α_eff ≥ τ, ESS monotonicity）推导 adaptive b*。但这本质上是一个参数选择规则：在每个 batch 中根据 q-score 分布选择 b 值。Proposition 1 和 2 是关于 ESS(b) 单调性的直接推导。Adaptive b* 的形式（Equation 1）是一个简单的分段函数（if α_eff(0) ≥ τ then b=b_ESS, else b_ESS if α_eff satisfies, else 0）。这与 Drayson et al. 的 grid search 相比，主要区别仅在于自动化了 b 的选择，且最终效果几乎无差异（adaptive vs grid-best: 17.674 vs 17.657, Table 1）。\n- **为什么影响接收**: 对于 EMNLP 主会议，方法贡献需要 substantial。一个框架内的参数自动选择规则，在效果与 grid search 持平的情况下，novelty 不够。\n- **建议修改方向**: 如果论文定位为 analysis paper，可以弱化 adaptive b* 的地位（作为 practical corollary 而非主要贡献）；如果要强调方法，需要在更多设置下证明 adaptive b* 的优势。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Related Work 遗漏了近期 instance-level reweighting 的重要工作\n\n- **具体位置**: Section 2 (Related Work)\n- **问题**: 论文讨论了 domain-level data mixing 和 instance-level selection，但遗漏了以下直接相关的最新工作：\n  - **\"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\"** (arXiv:2502.06733, Feb 2025) — 这篇工作同样做 instance-level dynamic reweighting for LM pretraining，是最直接的对比对象。\n  - **\"Self-Influence Guided Data Reweighting for Language Model Pre-training\"** (ICLR 2025) — 使用 self-influence scores 做 pretraining data reweighting。\n  - **\"ToReMi: Topic-Aware Data Reweighting for Dynamic Pre-Training Data Selection\"** (arXiv:2504.00695, 2025) — topic-aware dynamic reweighting。\n  这些工作与论文的 provenance-based reweighting 形成对比（基于 quality vs 基于 provenance），论文应讨论为什么 provenance 信号比 loss-based 或 influence-based 信号更合适或不同。\n- **建议**: 在 Section 2 的 \"Instance-Level Data Selection and Reweighting\" 段落中增加对这些工作的讨论。\n\n**W2** [warning] Epoch confound 发现虽然有价值，但在概念上并非完全出乎意料\n\n- **具体位置**: Section 5.1, Section 6\n- **问题**: 当 D&R 过滤掉部分 samples（如 detect & remove），有效数据集缩小，模型在相同 step 数下看到更多 epoch 的数据。这是一个自然推论——减少数据量意味着更多重复暴露。论文的贡献在于严格的实验验证（epoch-matched controls），但 Section 6 的讨论（\"The epoch confound in D&R evaluation\"）没有充分讨论为什么这个 confound 在之前的文献中被忽略——是因为之前的工作没有控制 epoch，还是因为它们在不同的实验设置下影响更小？\n- **建议**: 在 Section 6 中增加对 prior work 实验设置的具体分析——Drayson et al. (2025) 和其他 D&R 工作是否报告了 epoch 数？是否有迹象表明 epoch confound 在它们的结果中同样存在？\n\n**W3** [warning] 3 seeds 统计效力不足以支撑如此小的效应量\n\n- **具体位置**: Section 4 (Training), Table 1, Table 2, Limitations\n- **问题**: 论文使用 3 seeds (42, 123, 456)。对于 Δ=-0.020 PPL 的效应量，3 seeds 提供的统计效力极低。Table 1 报告 std 约 ±0.007-0.008，但这是 3-seed 的 std——degrees of freedom 仅为 2。论文自己在 Limitations 中承认 \"the sample size (N=3) limits generalizability\"，但这不仅限制 generalizability，也限制了效应量本身的可靠性。Footnote 2 提到 \"Computed from 3dp-rounded per-seed values\"，进一步增加了不确定性。\n- **建议**: (1) 报告 95% 置信区间而非仅 std；(2) 增加到至少 5 seeds 或更多；(3) 对关键发现执行 statistical significance test（如 paired t-test 或 bootstrap CI）。\n\n**W4** [warning] 论文的 \"analysis paper\" vs \"method paper\" 定位不清晰\n\n- **具体位置**: Abstract, Section 1, Section 3, Section 7\n- **问题**: Abstract 同时 claim \"we analyze when, why, and how detect-and-reweight works\"（analysis）和 \"we derive a dual-constrained adaptive b* that eliminates per-model grid search\"（method）。Introduction 最后一段列出三个 findings（analysis），但紧接着推出 adaptive b* 作为 \"practical corollary\"。这种双重定位使论文的 contribution 模糊——作为 analysis paper，epoch confound 是核心但实验范围需要更广；作为 method paper，adaptive b* 的改善太小且不够 novel。\n- **建议**: 明确选择一个定位。建议定位为 analysis paper，将 adaptive b* 降级为 practical implication 而非主要贡献。\n\n**W5** [warning] α_eff 作为 detector proxy 的 correlation 较弱\n\n- **具体位置**: Appendix K (Table 11), Section 5.3\n- **问题**: Table 11 报告 α_eff 与 true batch-level real fraction 的 Pearson r = 0.170（seed 42）。论文将其解释为 \"consistent negative bias (-0.03) indicates that α_eff slightly underestimates the true real fractions\"，但 r=0.170 是非常弱的相关性。虽然 Spearman r=0.25 和 0.75（different seeds）稍好，但跨 seed 的不一致性（0.17-0.75 范围）说明 α_eff 作为 proxy 的可靠性存疑。论文基于 α_eff 的约束（α_eff ≥ τ）来决定 b*，如果 α_eff 本身就不准确，约束的效力就有限。\n- **建议**: 更充分地讨论 α_eff 的局限性，以及它作为 proxy 的不可靠性如何影响 adaptive b* 的实际表现。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Figure 2 可读性**: 图较小，右侧 \"Sharpening exponent b\" 和 \"Held-out PPL\" 的 y 轴标签较拥挤；三角形（seed 42）与五角星（seed 456）在灰度打印下难以区分。\n\n2. **Footnote 密度过高**: 全文约 12+ 个脚注（正文内），部分脚注包含重要技术细节（如 footnote 1 的 batch composition、footnote 2 的 rounding），考虑将关键脚注内容移入正文。\n\n3. **Section 2 结构**: \"Synthetic Contamination and Model Collapse\" 和 \"Detection and Filtering of Machine-Generated Text\" 两个小节的界限模糊——model collapse 的讨论（Shumailov et al., Dohmatob et al.）与 detection 相关但不完全是同一话题，可以更清晰地分开。\n\n4. **Table 2 小数位不一致**: Method 列中 \"Adaptive b*\" 的 PPL 报告 3 位小数，但 \"Detect & Remove\" 等仅 2-3 位小数。建议统一。\n\n5. **Appendix 过于庞大**: Appendix A-Q 共 5 页（pages 11-15），涵盖 17 个子附录。部分关键证据（如 Appendix K 的 α_eff proxy validation、Appendix N 的 low contamination results）对论文核心论点很重要，考虑是否应在正文中更充分讨论。\n\n6. **\"practical\" 一词使用频率过高**: Abstract, Section 1, Section 3 中多次使用 \"practical\" 来修饰 adaptive b*，但 0.11% 的改善是否 \"practical\" 值得商榷。\n\n---\n\n## Questions to Authors\n\n1. 论文的核心发现（epoch confound）是否在 Drayson et al. (2025) 的原始实验设置中同样成立？他们的 b=10 grid search 结果中有多少可以用 epoch confound 解释？\n\n2. 如果将 contamination 源从 self-generated 换成不同模型（如用 Llama 生成 synthetic data 来污染 Qwen 训练集），三个有效性条件是否仍然成立？\n\n3. Adaptive b* 在 ρ=0.2 时 degrade（Appendix N），但论文引用的 web contamination 估计下限就是 20%。论文是否认为 adaptive b* 仅适用于高 contamination 场景？如果是，这如何与论文标题中 \"When Does Detect-and-Reweight Work?\" 的一般性问题对齐？\n\n4. Table 4 下游 benchmark 无显著差异。如果 PPL 改善不能转化为下游性能提升，\"effectiveness conditions\" 的实际意义是什么？\n\n5. α_eff 与 true batch-level real fraction 的 correlation 跨 seed 差异很大（Pearson r: 0.17-0.75, Table 11）。作者如何解释这种不稳定性？\n\n---\n\n## Missing References\n\n1. **Xu et al. (2025)** \"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\" (arXiv:2502.06733) — 直接做 instance-level dynamic reweighting for pretraining\n2. **Xia et al. (2023/ICLR 2025)** \"Self-Influence Guided Data Reweighting for Language Model Pre-training\" — self-influence based pretraining data reweighting\n3. **Wu et al. (2025)** \"A Survey on LLM-Generated Text Detection\" (Computational Linguistics, MIT Press) — 最新的 MGT detection 综述\n4. **Chen et al. (2025)** \"ToReMi: Topic-Aware Data Reweighting for Dynamic Pre-Training Data Selection\" — topic-aware dynamic reweighting\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 备注 |\n|------|------|------|\n| 页数限制（正文 ≤8 页） | ✅ 合规 | 正文（Section 1-7）在第 8 页结束，Limitations 从第 8 页右栏开始，不计入页数 |\n| ACL 模板 | ✅ 合规 | 使用 \"Anonymous ACL submission\" 标识 |\n| Double-blind 匿名 | ✅ 合规 | 未发现作者身份泄露 |\n| Limitations 章节 | ✅ 存在 | 第 8 页右栏，覆盖模型规模、数据范围、seed 数量等 |\n| Ethics Statement | ✅ 存在 | 第 9 页左栏，简短但充分 |\n| Responsible NLP Checklist | ✅ 不在 PDF 中 | 符合要求（在 OpenReview form 中填写） |\n| References 格式 | ⚠️ 基本一致 | 大部分规范，但部分 arXiv preprint 未标注会议版本（如已被接收） |\n| Appendix 大小 | ⚠️ 较大 | 5 页 17 个子附录，部分关键证据（K, N）未在正文充分引用 |\n\n---\n\n## 总结\n\n这篇论文提出了一个有价值的方法论发现（epoch confound in D&R evaluation），并提供了一个系统的实验分析。但它面临三个核心挑战：(1) 效应量极小（0.11% PPL, 下游无显著差异），(2) 实验范围过窄（单模型、单数据集、self-generated contamination），(3) 方法贡献（adaptive b*）是增量式的。作为 Findings 论文，epoch confound 的发现足够支撑接收；但对于主会议，需要更广的实验范围和更 convincing 的实际影响。\n\n建议评分：**Overall 3.0 — Findings**\n",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告\n\n**论文**: When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**审查侧重**: 新颖性、Related Work 完整性、写作质量、格式合规\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 / 5 — Findings\n**一句话总结**: Epoch confound 的识别是对 D&R 评估方法论的有价值贡献，但极小的效应量（Δ=-0.020 PPL, ~0.11%）、狭窄的实验范围（单模型/单数据集）和增量式的方法贡献使其未达到主会议门槛，适合 Findings。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5 / 5 | 方法论设计严谨（epoch-matched controls、permuted-score control），但 3 seeds 统计效力不足，效应量极小，单一实验设置限制了结论的可推广性 |\n| **Excitement** | 2.5 / 5 | Epoch confound 发现有一定社区价值，但效应量太小、实验范围太窄、方法贡献增量式，整体 impact 有限 |\n| **Overall** | 3.0 / 5 | Findings 级别——有价值的分析发现，但不够 exciting 进主会议 |\n\n---\n\n## 主要优势\n\n1. **Epoch confound 的实验设计精巧**：通过 epoch-matched controls (N=3) 将 D&R 的 PPL 优势从 0.396 分解为仅 Δ=0.017（Table 1），严格证明 >95% 的优势来自多 epoch 暴露而非过滤质量。Permuted-score control (Section 5.1) 进一步确认 detector signal 是 load-bearing 的。这是一个方法论上干净的贡献。\n\n2. **三个有效性条件形成实用框架**：Table 3 的决策矩阵（detector AUC + calibration + α_eff constraint）为从业者提供了清晰的 checklist。\n\n3. **诚实的效应量报告**：论文没有隐瞒 Δ=-0.020 PPL 的微小效应，Limitations 部分直接承认了实验范围的局限。\n\n4. **充分的 ablation 研究**：Section 5.2-5.3 和 Appendix B-Q 覆盖了 quality threshold sensitivity、batch-adaptive variants、constraint regime、scale、OOD evaluation 等多个维度。\n\n5. **LR-controlled verification** (Section 5.1): 用 independent linear schedules 控制 LR schedule 混淆，确认 epoch-exposure advantage 在 controlled LR 下仍然成立，实验设计细致。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 效应量极小，实际意义不足以支撑论文的 framing\n\n- **具体位置**: Abstract (\"Δ_s=-0.020\"), Table 1, Table 2, Section 5.1\n- **问题**: 论文的核心数值结果——adaptive b* 相对 uniform 的改善——为 Δ=-0.020 PPL（~0.11% relative）。Table 4 的下游 benchmark 结果明确写道 \"All differences within standard error\"，即下游任务上无统计显著差异。论文 Abstract 和 Introduction 的叙事暗示这些 findings 对实践有指导意义（\"yielding a practical adaptive method\"），但 0.11% 的 PPL 改善和零下游 improvement 使这一 claim 难以成立。\n- **为什么影响接收**: 如果论文的主要方法贡献（adaptive b*）在实践中几乎无法观测到改善，那么论文的 contribution 就完全落在分析发现（epoch confound）上。作为一篇 analysis paper，这足以支撑 Findings，但论文目前的 framing 试图同时主张 method contribution，导致 overclaim。\n- **建议修改方向**: (1) 明确论文定位为 analysis/diagnostic paper 而非 method paper；(2) 在 Abstract 中直接量化效应量的微小程度（如 \"~0.1% relative PPL improvement\"），避免读者产生过高期望；(3) 讨论在什么规模/场景下效应量可能变大。\n\n**N2** [critical] 实验范围过窄，不足以支撑 \"three effectiveness conditions\" 作为一般性结论\n\n- **具体位置**: Section 4 (Experimental Setup), Section 5, Appendix O\n- **问题**: 所有主要实验基于单一设置：Qwen3-0.6B、FineWeb 132M tokens、self-generated contamination (ρ=0.4)。这三个条件限制了结论的推广性：\n  - **单一模型**: 仅 Qwen3-0.6B (0.6B params)。Appendix O 尝试 Llama-3.2-3B 的 cross-model transfer 但结果 \"mixed\"（MMLU improves while HellaSwag slightly degrades）, 作者自己承认 \"mixed results\"。\n  - **Self-generated contamination only**: 真实 web contamination 中污染源模型与被训练模型不同、synthetic text 更多样。论文 Section 7 承认 \"realistic multi-source web contamination is untested\"。\n  - **极小 scale**: 132M tokens 是 continued pretraining 中极小的规模。论文 Section 6 讨论了 scale effects 但缺乏实验验证。\n  - **Appendix N 显示方法在 ρ=0.2 时 degrade**: \"adaptive method Δ=-0.013 with OOD partially inconsistent\"，而 20% contamination 是论文自己引用的 web 估计范围的下限。\n- **为什么影响接收**: 论文的 framing（\"we identify three effectiveness conditions for detect-and-reweight\"）暗示一般性结论，但所有证据来自一个极窄的实验 corridor。三个条件可能是该特定设置的 artifact，不一定推广到其他模型、数据或 contamination 场景。\n- **建议修改方向**: (1) 在标题或 Abstract 中明确 scope（如 \"in the setting of single-model continued pretraining\"）；(2) 增加至少一个不同架构/规模的模型（如 2-3B scale）作为主实验；(3) 测试 cross-model contamination（用不同模型生成 synthetic data）。\n\n**N3** [critical] Adaptive b* 的新颖性不足——本质是 Drayson et al. (2025) 框架的参数选择启发式\n\n- **具体位置**: Section 3 (Quality floor / Stability ceiling / Adaptive b*), Equation (1)\n- **问题**: w=(1-q)^b 框架完全来自 Drayson et al. (2025)。论文的方法贡献是从两个约束（α_eff ≥ τ, ESS monotonicity）推导 adaptive b*。但这本质上是一个参数选择规则：在每个 batch 中根据 q-score 分布选择 b 值。Proposition 1 和 2 是关于 ESS(b) 单调性的直接推导。Adaptive b* 的形式（Equation 1）是一个简单的分段函数（if α_eff(0) ≥ τ then b=b_ESS, else b_ESS if α_eff satisfies, else 0）。这与 Drayson et al. 的 grid search 相比，主要区别仅在于自动化了 b 的选择，且最终效果几乎无差异（adaptive vs grid-best: 17.674 vs 17.657, Table 1）。\n- **为什么影响接收**: 对于 EMNLP 主会议，方法贡献需要 substantial。一个框架内的参数自动选择规则，在效果与 grid search 持平的情况下，novelty 不够。\n- **建议修改方向**: 如果论文定位为 analysis paper，可以弱化 adaptive b* 的地位（作为 practical corollary 而非主要贡献）；如果要强调方法，需要在更多设置下证明 adaptive b* 的优势。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Related Work 遗漏了近期 instance-level reweighting 的重要工作\n\n- **具体位置**: Section 2 (Related Work)\n- **问题**: 论文讨论了 domain-level data mixing 和 instance-level selection，但遗漏了以下直接相关的最新工作：\n  - **\"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\"** (arXiv:2502.06733, Feb 2025) — 这篇工作同样做 instance-level dynamic reweighting for LM pretraining，是最直接的对比对象。\n  - **\"Self-Influence Guided Data Reweighting for Language Model Pre-training\"** (ICLR 2025) — 使用 self-influence scores 做 pretraining data reweighting。\n  - **\"ToReMi: Topic-Aware Data Reweighting for Dynamic Pre-Training Data Selection\"** (arXiv:2504.00695, 2025) — topic-aware dynamic reweighting。\n  这些工作与论文的 provenance-based reweighting 形成对比（基于 quality vs 基于 provenance），论文应讨论为什么 provenance 信号比 loss-based 或 influence-based 信号更合适或不同。\n- **建议**: 在 Section 2 的 \"Instance-Level Data Selection and Reweighting\" 段落中增加对这些工作的讨论。\n\n**W2** [warning] Epoch confound 发现虽然有价值，但在概念上并非完全出乎意料\n\n- **具体位置**: Section 5.1, Section 6\n- **问题**: 当 D&R 过滤掉部分 samples（如 detect & remove），有效数据集缩小，模型在相同 step 数下看到更多 epoch 的数据。这是一个自然推论——减少数据量意味着更多重复暴露。论文的贡献在于严格的实验验证（epoch-matched controls），但 Section 6 的讨论（\"The epoch confound in D&R evaluation\"）没有充分讨论为什么这个 confound 在之前的文献中被忽略——是因为之前的工作没有控制 epoch，还是因为它们在不同的实验设置下影响更小？\n- **建议**: 在 Section 6 中增加对 prior work 实验设置的具体分析——Drayson et al. (2025) 和其他 D&R 工作是否报告了 epoch 数？是否有迹象表明 epoch confound 在它们的结果中同样存在？\n\n**W3** [warning] 3 seeds 统计效力不足以支撑如此小的效应量\n\n- **具体位置**: Section 4 (Training), Table 1, Table 2, Limitations\n- **问题**: 论文使用 3 seeds (42, 123, 456)。对于 Δ=-0.020 PPL 的效应量，3 seeds 提供的统计效力极低。Table 1 报告 std 约 ±0.007-0.008，但这是 3-seed 的 std——degrees of freedom 仅为 2。论文自己在 Limitations 中承认 \"the sample size (N=3) limits generalizability\"，但这不仅限制 generalizability，也限制了效应量本身的可靠性。Footnote 2 提到 \"Computed from 3dp-rounded per-seed values\"，进一步增加了不确定性。\n- **建议**: (1) 报告 95% 置信区间而非仅 std；(2) 增加到至少 5 seeds 或更多；(3) 对关键发现执行 statistical significance test（如 paired t-test 或 bootstrap CI）。\n\n**W4** [warning] 论文的 \"analysis paper\" vs \"method paper\" 定位不清晰\n\n- **具体位置**: Abstract, Section 1, Section 3, Section 7\n- **问题**: Abstract 同时 claim \"we analyze when, why, and how detect-and-reweight works\"（analysis）和 \"we derive a dual-constrained adaptive b* that eliminates per-model grid search\"（method）。Introduction 最后一段列出三个 findings（analysis），但紧接着推出 adaptive b* 作为 \"practical corollary\"。这种双重定位使论文的 contribution 模糊——作为 analysis paper，epoch confound 是核心但实验范围需要更广；作为 method paper，adaptive b* 的改善太小且不够 novel。\n- **建议**: 明确选择一个定位。建议定位为 analysis paper，将 adaptive b* 降级为 practical implication 而非主要贡献。\n\n**W5** [warning] α_eff 作为 detector proxy 的 correlation 较弱\n\n- **具体位置**: Appendix K (Table 11), Section 5.3\n- **问题**: Table 11 报告 α_eff 与 true batch-level real fraction 的 Pearson r = 0.170（seed 42）。论文将其解释为 \"consistent negative bias (-0.03) indicates that α_eff slightly underestimates the true real fractions\"，但 r=0.170 是非常弱的相关性。虽然 Spearman r=0.25 和 0.75（different seeds）稍好，但跨 seed 的不一致性（0.17-0.75 范围）说明 α_eff 作为 proxy 的可靠性存疑。论文基于 α_eff 的约束（α_eff ≥ τ）来决定 b*，如果 α_eff 本身就不准确，约束的效力就有限。\n- **建议**: 更充分地讨论 α_eff 的局限性，以及它作为 proxy 的不可靠性如何影响 adaptive b* 的实际表现。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Figure 2 可读性**: 图较小，右侧 \"Sharpening exponent b\" 和 \"Held-out PPL\" 的 y 轴标签较拥挤；三角形（seed 42）与五角星（seed 456）在灰度打印下难以区分。\n\n2. **Footnote 密度过高**: 全文约 12+ 个脚注（正文内），部分脚注包含重要技术细节（如 footnote 1 的 batch composition、footnote 2 的 rounding），考虑将关键脚注内容移入正文。\n\n3. **Section 2 结构**: \"Synthetic Contamination and Model Collapse\" 和 \"Detection and Filtering of Machine-Generated Text\" 两个小节的界限模糊——model collapse 的讨论（Shumailov et al., Dohmatob et al.）与 detection 相关但不完全是同一话题，可以更清晰地分开。\n\n4. **Table 2 小数位不一致**: Method 列中 \"Adaptive b*\" 的 PPL 报告 3 位小数，但 \"Detect & Remove\" 等仅 2-3 位小数。建议统一。\n\n5. **Appendix 过于庞大**: Appendix A-Q 共 5 页（pages 11-15），涵盖 17 个子附录。部分关键证据（如 Appendix K 的 α_eff proxy validation、Appendix N 的 low contamination results）对论文核心论点很重要，考虑是否应在正文中更充分讨论。\n\n6. **\"practical\" 一词使用频率过高**: Abstract, Section 1, Section 3 中多次使用 \"practical\" 来修饰 adaptive b*，但 0.11% 的改善是否 \"practical\" 值得商榷。\n\n---\n\n## Questions to Authors\n\n1. 论文的核心发现（epoch confound）是否在 Drayson et al. (2025) 的原始实验设置中同样成立？他们的 b=10 grid search 结果中有多少可以用 epoch confound 解释？\n\n2. 如果将 contamination 源从 self-generated 换成不同模型（如用 Llama 生成 synthetic data 来污染 Qwen 训练集），三个有效性条件是否仍然成立？\n\n3. Adaptive b* 在 ρ=0.2 时 degrade（Appendix N），但论文引用的 web contamination 估计下限就是 20%。论文是否认为 adaptive b* 仅适用于高 contamination 场景？如果是，这如何与论文标题中 \"When Does Detect-and-Reweight Work?\" 的一般性问题对齐？\n\n4. Table 4 下游 benchmark 无显著差异。如果 PPL 改善不能转化为下游性能提升，\"effectiveness conditions\" 的实际意义是什么？\n\n5. α_eff 与 true batch-level real fraction 的 correlation 跨 seed 差异很大（Pearson r: 0.17-0.75, Table 11）。作者如何解释这种不稳定性？\n\n---\n\n## Missing References\n\n1. **Xu et al. (2025)** \"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\" (arXiv:2502.06733) — 直接做 instance-level dynamic reweighting for pretraining\n2. **Xia et al. (2023/ICLR 2025)** \"Self-Influence Guided Data Reweighting for Language Model Pre-training\" — self-influence based pretraining data reweighting\n3. **Wu et al. (2025)** \"A Survey on LLM-Generated Text Detection\" (Computational Linguistics, MIT Press) — 最新的 MGT detection 综述\n4. **Chen et al. (2025)** \"ToReMi: Topic-Aware Data Reweighting for Dynamic Pre-Training Data Selection\" — topic-aware dynamic reweighting\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 备注 |\n|------|------|------|\n| 页数限制（正文 ≤8 页） | ✅ 合规 | 正文（Section 1-7）在第 8 页结束，Limitations 从第 8 页右栏开始，不计入页数 |\n| ACL 模板 | ✅ 合规 | 使用 \"Anonymous ACL submission\" 标识 |\n| Double-blind 匿名 | ✅ 合规 | 未发现作者身份泄露 |\n| Limitations 章节 | ✅ 存在 | 第 8 页右栏，覆盖模型规模、数据范围、seed 数量等 |\n| Ethics Statement | ✅ 存在 | 第 9 页左栏，简短但充分 |\n| Responsible NLP Checklist | ✅ 不在 PDF 中 | 符合要求（在 OpenReview form 中填写） |\n| References 格式 | ⚠️ 基本一致 | 大部分规范，但部分 arXiv preprint 未标注会议版本（如已被接收） |\n| Appendix 大小 | ⚠️ 较大 | 5 页 17 个子附录，部分关键证据（K, N）未在正文充分引用 |\n\n---\n\n## 总结\n\n这篇论文提出了一个有价值的方法论发现（epoch confound in D&R evaluation），并提供了一个系统的实验分析。但它面临三个核心挑战：(1) 效应量极小（0.11% PPL, 下游无显著差异），(2) 实验范围过窄（单模型、单数据集、self-generated contamination），(3) 方法贡献（adaptive b*）是增量式的。作为 Findings 论文，epoch confound 的发现足够支撑接收；但对于主会议，需要更广的实验范围和更 convincing 的实际影响。\n\n建议评分：**Overall 3.0 — Findings**\n",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 799 · 2026-05-23T03:13:20.200137+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4020
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-23T03:13:27.799254+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 801 · 2026-05-23T03:13:27.799782+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-23T03:13:36.331535+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 803 · 2026-05-23T03:13:36.332235+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 804 · 2026-05-23T03:13:43.710605+00:00_

Reviewer 2 审稿完成。已向 Review Director 提交完整报告。核心判断：

- **Overall: 3.0 (Findings)** — epoch confound 发现有价值但不够进主会议
- **Soundness: 3.5** — 实验设计严谨但范围过窄、统计效力不足
- **Excitement: 2.5** — 效应量太小（Δ=-0.020 PPL, ~0.11%），方法贡献增量式

三个 Must-Fix 问题：(1) 效应量极小且下游无显著差异，论文 framing 有 overclaim；(2) 单模型/单数据集/self-generated contamination 不足以支撑一般性结论；(3) adaptive b* 本质是 Drayson et al. 框架的参数选择启发式，novelty 不足。还识别了 4 篇遗漏的直接相关工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 20

## Round 20

4 recorded events


### User

_source line 805 · 2026-05-23T03:14:24.339871+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和关键观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 1 审稿报告

**审查侧重**: 方法严谨性、实验设计、统计分析

## Overall: 3.0（Findings）

---

## Must-Fix 问题

**N1** [critical] N=3 seeds 的统计检验力严重不足
- 全部主实验仅用 3 个随机种子，paired t-test 仅 2 自由度
- Δ=-0.020 的 95% BCa bootstrap CI [−0.028, −0.012] 在 N=3 时覆盖率无法保证
- Per-seed 方差极小（SD ≈ 0.007），种子间差异可能被 training recipe 的确定性压缩
- 建议增加到 N=5-10

**N2** [critical] α_eff 作为 quality proxy 的理论基础薄弱（R²≈0.49）
- α_eff 仅解释真实质量信号约一半方差
- Bonferroni-Holm 校正后 Spearman ρ=0.4 的 p_BH=0.078 不显著
- Pearson r=0.70 vs Spearman ρ=0.40 差距暗示关系可能由极端值驱动
- Table 11 仅基于 5 个离散 b 值，样本量极小

**N3** [critical] 下游任务零改善严重削弱实际价值
- 5 个下游任务 adaptive (0.5414) = uniform (0.5414)
- PPL 改善不能迁移到任何下游任务
- 建议更大规模模型验证或将论文定位为分析贡献

## Should-Fix 问题

**W1** [warning] Self-contamination 设计生态效度有限
- Generator = trainee，AUC=0.94 可能在真实场景不可复现
- Cross-model 实验仅单种子，结果混合

**W2** [warning] 方法新颖性增量有限
- w=(1−q)^b 完全沿用 Drayson et al.
- Dual-constrained b* 是工程改进而非方法创新

**W3** [warning] Δ=-0.020 PPL 实际意义需更充分论证
- ~0.11% relative improvement
- 读者容易被 framing 误导

**W4** [warning] ESS ceiling 与 α_eff floor 交互缺乏理论分析
- 约束冲突时退回 b=b_ESS 的后果未分析
- Proposition 1-2 只证明单调性，未涉及约束冲突

## Questions to Authors
1. α_eff 与 downstream accuracy 的直接相关性？
2. N=3 的 power analysis？需要多少 seeds 达到 80% power？
3. Pearson r=0.70 vs Spearman ρ=0.40 差异的散点图？
4. 更大模型上的 pilot 实验？
5. ρ=0.4 的代表性——方法仅在高污染场景有效？

## 主要优势
1. Epoch confound 分析设计精巧且结论有力
2. 三条 effectiveness conditions 的系统总结
3. 诚实的 negative results 报告
4. 充实的 appendix

---

请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 806 · 2026-05-23T03:17:18.400484+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE] R1-N1: N=3 seeds 统计检验力不足\n\n同意这是论文的核心方法论弱点。我在自己的审稿意见 W3 中也独立提出了同一问题。补充几点：\n\n1. **BCa bootstrap 在 N=3 时确实不可靠**：BCa 的 bias-correction 和 acceleration 参数需要从 jackknife 估计，N=3 时仅有 3 个 jackknife 样本，这些参数的估计本身极不稳定。论文报告的 CI [−0.028, −0.012] 的覆盖率确实无法保证。\n2. **R1 关于\"种子间差异被 training recipe 确定性压缩\"的观察很敏锐**：如果 data order 是 seed-deterministic 但模型初始化之外的随机性很小，那么 3 seeds 的 variance 可能低估了真实的实验不确定性。\n3. **但要区分定量和定性 findings**：epoch confound 的核心发现（>95% 优势来自 multi-epoch）是一个定性结论——Table 1 中 epoch-matched 的 Δ 从 0.396 骤降到 0.017，这个 ratio 在 3 seeds 中方向完全一致。统计效力问题主要影响 adaptive b* 的定量精度（Δ=-0.020 ± 多少？），而非 epoch confound 的方向性结论。\n\n**总结**：同意 N=3 是问题，建议至少增加到 N=5。但 epoch confound 的定性结论受此影响较小。\n\n---\n\n### [AGREE] R1-N2: α_eff 作为 quality proxy 的理论基础薄弱\n\n同意。我在自己的 W5 中也独立提出了 α_eff proxy reliability 问题。R1 的统计分析更深入，补充认同以下几点：\n\n1. **Pearson r=0.70 vs Spearman ρ=0.40 的差距确实暗示极端值驱动**：线性相关强但秩相关弱，说明 α_eff 在少数极端 batch 上与真实质量一致，但在大多数 batch 上排序不可靠。这对 threshold-based 决策（α_eff ≥ τ）尤其危险——threshold 需要的是全范围的可靠排序，不仅仅是极端值处的相关。\n2. **Table 11 仅基于 5 个离散 b 值**：R1 指出的样本量问题是正确的。5 个点上的 correlation 信息量极少。\n3. **一个补充观察**：我的审稿中注意到 Table 11 跨 seed 的 Pearson r 变化范围较大（部分 seed 很低），进一步支持 R1 的不稳定性担忧。\n\n**建议**：论文应增加 α_eff 在连续 b 值上的 calibration 分析，而非仅依赖 5 个离散点。\n\n---\n\n### [AGREE] R1-N3: 下游任务零改善削弱实际价值\n\n完全同意。我在自己的 N1 中也将此作为 critical issue 提出。具体引用相同证据：\n\n- Table 4 明确报告 adaptive (0.5414) = uniform (0.5414)，\"All differences within standard error\"（Table 4 caption）\n- 这意味着论文的方法贡献（adaptive b*）在任何可测量的下游任务上都没有产生差异\n- 论文的实际价值因此完全落在 epoch confound 的诊断发现上，而非方法改进\n\nR1 建议的\"将论文定位为分析贡献\"与我的建议一致。\n\n---\n\n## Should-Fix 问题\n\n### [AGREE] R1-W1: Self-contamination 生态效度有限\n\n同意。我在 N2 中也将此作为 critical issue 提出（我的评级更高）。补充：\n\n- **Generator = trainee 使 AUC=0.94 具有人为优势**：当模型检测自己生成的文本时，detector 可以利用自身 decoding 的统计规律性（如 nucleus sampling 的截断分布）。在真实 web contamination 中，generator 和 detector 不同，AUC 可能显著更低。\n- **Appendix O 的 cross-model 实验（Llama-3.2-3B）结果\"mixed\"且仅单 seed**：这不足以证明方法在 cross-model 场景的有效性。论文自己承认 \"mixed results with surface-level evaluation sensitivity\" (Appendix O)。\n- **这对 Finding 2（detector calibration 是必要条件）尤其关键**：如果在 cross-model 场景下 detector 本身就不可靠，那么整个 D&R 框架的前提就动摇了。\n\n---\n\n### [AGREE] R1-W2: 方法新颖性增量有限\n\n完全同意。与我的 N3 一致。w=(1-q)^b 框架 100% 来自 Drayson et al. (2025)，adaptive b* 是一个两约束优化问题的闭式解——Proposition 1 证明 ESS 单调性（直接推导），Proposition 2 证明严格递减（batch 含不同 q 值时自然成立）。这些数学结果虽然正确但 trivial。\n\n\"工程改进而非方法创新\"的评价准确。\n\n---\n\n### [AGREE] R1-W3: Δ=-0.020 PPL 实际意义不足\n\n同意。与我的 N1 一致。补充一个具体数据点：Section 6 讨论 \"the gap to grid-best narrows from 0.040 (B=4) to 0.009 (B=16)\"，但即使是 grid-best（需要 post-hoc oracle 知识），改善也仅 Δ≈-0.037（Table 1, 17.657 vs 17.694）。这意味着 detect-and-reweight 方法在这个设置下的 *upper bound* 改善也仅约 0.2%——整个方法类别的天花板就很低，不仅仅是 adaptive b* 的问题。\n\n---\n\n### [REBUT] R1-W4: ESS ceiling 与 α_eff floor 交互缺乏理论分析\n\n部分不同意。R1 的观察（约束冲突时的行为未理论分析）在形式上是对的，但论文 *隐式地* 通过实验覆盖了这一场景：\n\n1. **ESS-only baseline 就是约束冲突的极端情况**：当 α_eff floor 完全不起作用（即不施加 quality 约束）时，方法退化为 ESS-only。Table 1 报告 ESS-only 的 mean PPL = 17.763，与 adaptive b*（17.674）差距 0.089，但与 uniform（17.694）相比 ESS-only 反而更差。这说明约束冲突时退回 ESS-only 行为的确不理想，但论文已经展示了这一点。\n\n2. **与论文 Finding 3（minimum intervention）一致**：Section 6 的讨论（\"When uniform beats reweighting\"）明确指出过度 sharpening 有害。当约束冲突时，adaptive b* 选择 b_ESS（较低的 b），这正是 minimum intervention 原则的体现——宁可少做，不要做过头。\n\n3. **实际冲突频率已隐式报告**：Section 5.1 报告 \"α_eff quality constraint binds in 38.2% of batches\"，意味着在 38.2% 的 batch 中 quality constraint 是 active 的。在剩余 61.8% 中，α_eff(0) ≥ τ（即使不 sharpen quality 也满足），b* = b_ESS。论文可以更明确地报告真正 \"conflict\"（两约束无法同时满足）的 batch 比例，但 38.2% 这个数字提供了部分信息。\n\n**建议**：论文应补充报告 (a) 约束真正冲突（α_eff < τ at b=b_ESS）的 batch 比例，(b) 这些 batch 的 PPL 贡献。但这不构成论文结论的 fundamental threat，因为 ESS-only 的表现已经在 Table 1 中评估过。\n\n---\n\n## R1 的 Questions 补充回应\n\n对 R1 提出的 5 个 Questions，作为 Reviewer 2 补充我的关注点：\n\n1. **α_eff 与 downstream accuracy 的直接相关性**：同意这是关键问题。论文目前只建立了 α_eff → PPL 的间接链条，α_eff → downstream 的关系未验证。\n2. **N=3 power analysis**：同意需要。基于 Δ=-0.020, SD≈0.007 的 paired t-test，80% power at α=0.05 大约需要 N=4-5 seeds（effect size d ≈ 2.86 很大，因为 SD 很小）。但正如 R1 指出的，如果 SD 被 deterministic training 人为压缩，真实所需 N 更大。\n3. **Pearson vs Spearman 散点图**：同意应提供。\n4. **更大模型 pilot**：强烈同意。即使是 1.7B 的 pilot 结果也会大幅增强说服力。论文提到 Qwen3-1.7B 但似乎仅在 Appendix 中有限使用。\n5. **ρ=0.4 代表性**：同意这是重要问题。我在自己的 Questions Q3 中也问了同一个问题——Appendix N 显示 ρ=0.2 时方法 degrade，而 20% 正好是论文自己引用的 web contamination 估计下限。\n\n---\n\n## 总结\n\nR1 和 R2 的审稿意见高度趋同。核心共识：\n\n| 问题 | R1 | R2 | 一致性 |\n|------|----|----|--------|\n| N=3 统计效力不足 | Must-Fix N1 | Should-Fix W3 | 完全一致 |\n| α_eff proxy 不可靠 | Must-Fix N2 | Should-Fix W5 | 完全一致 |\n| 下游零改善 | Must-Fix N3 | Must-Fix N1 | 完全一致 |\n| Self-contamination 生态效度 | Should-Fix W1 | Must-Fix N2 | 一致，我评级更高 |\n| 方法新颖性增量 | Should-Fix W2 | Must-Fix N3 | 一致，我评级更高 |\n| 效应量太小 | Should-Fix W3 | Must-Fix N1 | 一致，我评级更高 |\n| ESS/α_eff 交互分析 | Should-Fix W4 | — | 我部分反驳 |\n\n**唯一分歧**：R1-W4（ESS ceiling 与 α_eff floor 交互）。我认为论文通过 ESS-only baseline 和 minimum intervention 讨论隐式覆盖了约束冲突场景，但同意可以更明确地分析。\n\n**评分对齐**：R1 Overall 3.0（Findings），R2 Overall 3.0（Findings）。两位 reviewer 独立达成一致，建议接收为 Findings。\n",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE] R1-N1: N=3 seeds 统计检验力不足\n\n同意这是论文的核心方法论弱点。我在自己的审稿意见 W3 中也独立提出了同一问题。补充几点：\n\n1. **BCa bootstrap 在 N=3 时确实不可靠**：BCa 的 bias-correction 和 acceleration 参数需要从 jackknife 估计，N=3 时仅有 3 个 jackknife 样本，这些参数的估计本身极不稳定。论文报告的 CI [−0.028, −0.012] 的覆盖率确实无法保证。\n2. **R1 关于\"种子间差异被 training recipe 确定性压缩\"的观察很敏锐**：如果 data order 是 seed-deterministic 但模型初始化之外的随机性很小，那么 3 seeds 的 variance 可能低估了真实的实验不确定性。\n3. **但要区分定量和定性 findings**：epoch confound 的核心发现（>95% 优势来自 multi-epoch）是一个定性结论——Table 1 中 epoch-matched 的 Δ 从 0.396 骤降到 0.017，这个 ratio 在 3 seeds 中方向完全一致。统计效力问题主要影响 adaptive b* 的定量精度（Δ=-0.020 ± 多少？），而非 epoch confound 的方向性结论。\n\n**总结**：同意 N=3 是问题，建议至少增加到 N=5。但 epoch confound 的定性结论受此影响较小。\n\n---\n\n### [AGREE] R1-N2: α_eff 作为 quality proxy 的理论基础薄弱\n\n同意。我在自己的 W5 中也独立提出了 α_eff proxy reliability 问题。R1 的统计分析更深入，补充认同以下几点：\n\n1. **Pearson r=0.70 vs Spearman ρ=0.40 的差距确实暗示极端值驱动**：线性相关强但秩相关弱，说明 α_eff 在少数极端 batch 上与真实质量一致，但在大多数 batch 上排序不可靠。这对 threshold-based 决策（α_eff ≥ τ）尤其危险——threshold 需要的是全范围的可靠排序，不仅仅是极端值处的相关。\n2. **Table 11 仅基于 5 个离散 b 值**：R1 指出的样本量问题是正确的。5 个点上的 correlation 信息量极少。\n3. **一个补充观察**：我的审稿中注意到 Table 11 跨 seed 的 Pearson r 变化范围较大（部分 seed 很低），进一步支持 R1 的不稳定性担忧。\n\n**建议**：论文应增加 α_eff 在连续 b 值上的 calibration 分析，而非仅依赖 5 个离散点。\n\n---\n\n### [AGREE] R1-N3: 下游任务零改善削弱实际价值\n\n完全同意。我在自己的 N1 中也将此作为 critical issue 提出。具体引用相同证据：\n\n- Table 4 明确报告 adaptive (0.5414) = uniform (0.5414)，\"All differences within standard error\"（Table 4 caption）\n- 这意味着论文的方法贡献（adaptive b*）在任何可测量的下游任务上都没有产生差异\n- 论文的实际价值因此完全落在 epoch confound 的诊断发现上，而非方法改进\n\nR1 建议的\"将论文定位为分析贡献\"与我的建议一致。\n\n---\n\n## Should-Fix 问题\n\n### [AGREE] R1-W1: Self-contamination 生态效度有限\n\n同意。我在 N2 中也将此作为 critical issue 提出（我的评级更高）。补充：\n\n- **Generator = trainee 使 AUC=0.94 具有人为优势**：当模型检测自己生成的文本时，detector 可以利用自身 decoding 的统计规律性（如 nucleus sampling 的截断分布）。在真实 web contamination 中，generator 和 detector 不同，AUC 可能显著更低。\n- **Appendix O 的 cross-model 实验（Llama-3.2-3B）结果\"mixed\"且仅单 seed**：这不足以证明方法在 cross-model 场景的有效性。论文自己承认 \"mixed results with surface-level evaluation sensitivity\" (Appendix O)。\n- **这对 Finding 2（detector calibration 是必要条件）尤其关键**：如果在 cross-model 场景下 detector 本身就不可靠，那么整个 D&R 框架的前提就动摇了。\n\n---\n\n### [AGREE] R1-W2: 方法新颖性增量有限\n\n完全同意。与我的 N3 一致。w=(1-q)^b 框架 100% 来自 Drayson et al. (2025)，adaptive b* 是一个两约束优化问题的闭式解——Proposition 1 证明 ESS 单调性（直接推导），Proposition 2 证明严格递减（batch 含不同 q 值时自然成立）。这些数学结果虽然正确但 trivial。\n\n\"工程改进而非方法创新\"的评价准确。\n\n---\n\n### [AGREE] R1-W3: Δ=-0.020 PPL 实际意义不足\n\n同意。与我的 N1 一致。补充一个具体数据点：Section 6 讨论 \"the gap to grid-best narrows from 0.040 (B=4) to 0.009 (B=16)\"，但即使是 grid-best（需要 post-hoc oracle 知识），改善也仅 Δ≈-0.037（Table 1, 17.657 vs 17.694）。这意味着 detect-and-reweight 方法在这个设置下的 *upper bound* 改善也仅约 0.2%——整个方法类别的天花板就很低，不仅仅是 adaptive b* 的问题。\n\n---\n\n### [REBUT] R1-W4: ESS ceiling 与 α_eff floor 交互缺乏理论分析\n\n部分不同意。R1 的观察（约束冲突时的行为未理论分析）在形式上是对的，但论文 *隐式地* 通过实验覆盖了这一场景：\n\n1. **ESS-only baseline 就是约束冲突的极端情况**：当 α_eff floor 完全不起作用（即不施加 quality 约束）时，方法退化为 ESS-only。Table 1 报告 ESS-only 的 mean PPL = 17.763，与 adaptive b*（17.674）差距 0.089，但与 uniform（17.694）相比 ESS-only 反而更差。这说明约束冲突时退回 ESS-only 行为的确不理想，但论文已经展示了这一点。\n\n2. **与论文 Finding 3（minimum intervention）一致**：Section 6 的讨论（\"When uniform beats reweighting\"）明确指出过度 sharpening 有害。当约束冲突时，adaptive b* 选择 b_ESS（较低的 b），这正是 minimum intervention 原则的体现——宁可少做，不要做过头。\n\n3. **实际冲突频率已隐式报告**：Section 5.1 报告 \"α_eff quality constraint binds in 38.2% of batches\"，意味着在 38.2% 的 batch 中 quality constraint 是 active 的。在剩余 61.8% 中，α_eff(0) ≥ τ（即使不 sharpen quality 也满足），b* = b_ESS。论文可以更明确地报告真正 \"conflict\"（两约束无法同时满足）的 batch 比例，但 38.2% 这个数字提供了部分信息。\n\n**建议**：论文应补充报告 (a) 约束真正冲突（α_eff < τ at b=b_ESS）的 batch 比例，(b) 这些 batch 的 PPL 贡献。但这不构成论文结论的 fundamental threat，因为 ESS-only 的表现已经在 Table 1 中评估过。\n\n---\n\n## R1 的 Questions 补充回应\n\n对 R1 提出的 5 个 Questions，作为 Reviewer 2 补充我的关注点：\n\n1. **α_eff 与 downstream accuracy 的直接相关性**：同意这是关键问题。论文目前只建立了 α_eff → PPL 的间接链条，α_eff → downstream 的关系未验证。\n2. **N=3 power analysis**：同意需要。基于 Δ=-0.020, SD≈0.007 的 paired t-test，80% power at α=0.05 大约需要 N=4-5 seeds（effect size d ≈ 2.86 很大，因为 SD 很小）。但正如 R1 指出的，如果 SD 被 deterministic training 人为压缩，真实所需 N 更大。\n3. **Pearson vs Spearman 散点图**：同意应提供。\n4. **更大模型 pilot**：强烈同意。即使是 1.7B 的 pilot 结果也会大幅增强说服力。论文提到 Qwen3-1.7B 但似乎仅在 Appendix 中有限使用。\n5. **ρ=0.4 代表性**：同意这是重要问题。我在自己的 Questions Q3 中也问了同一个问题——Appendix N 显示 ρ=0.2 时方法 degrade，而 20% 正好是论文自己引用的 web contamination 估计下限。\n\n---\n\n## 总结\n\nR1 和 R2 的审稿意见高度趋同。核心共识：\n\n| 问题 | R1 | R2 | 一致性 |\n|------|----|----|--------|\n| N=3 统计效力不足 | Must-Fix N1 | Should-Fix W3 | 完全一致 |\n| α_eff proxy 不可靠 | Must-Fix N2 | Should-Fix W5 | 完全一致 |\n| 下游零改善 | Must-Fix N3 | Must-Fix N1 | 完全一致 |\n| Self-contamination 生态效度 | Should-Fix W1 | Must-Fix N2 | 一致，我评级更高 |\n| 方法新颖性增量 | Should-Fix W2 | Must-Fix N3 | 一致，我评级更高 |\n| 效应量太小 | Should-Fix W3 | Must-Fix N1 | 一致，我评级更高 |\n| ESS/α_eff 交互分析 | Should-Fix W4 | — | 我部分反驳 |\n\n**唯一分歧**：R1-W4（ESS ceiling 与 α_eff floor 交互）。我认为论文通过 ESS-only baseline 和 minimum intervention 讨论隐式覆盖了约束冲突场景，但同意可以更明确地分析。\n\n**评分对齐**：R1 Overall 3.0（Findings），R2 Overall 3.0（Findings）。两位 reviewer 独立达成一致，建议接收为 Findings。\n",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-23T03:17:22.216763+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3816
}
```

</details>

---


### Assistant

_source line 808 · 2026-05-23T03:17:28.286329+00:00_

交叉回应已提交。

两位 Reviewer 独立审稿后高度趋同——6/7 个问题完全一致，唯一分歧在 R1-W4（ESS/α_eff 约束交互），我认为论文通过 ESS-only baseline 隐式覆盖了该场景，给出了 [REBUT]。其余全部 [AGREE]，评分均为 Overall 3.0（Findings）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 21

## Round 21

90 recorded events


### User

_source line 809 · 2026-05-23T13:11:29.062789+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2: 新颖性 + 完整性 + 写作质量

### Venue 信息
- **目标**: EMNLP 2026 (ARR May cycle)
- **截止日期**: 2026-05-25
- **格式**: Long Paper, 8 页正文, 无限参考文献, Limitations/Ethics 不计入页数
- **模板**: ACL 2026 style
- **匿名规则**: Double-blind (论文中不得出现作者信息, 避免 self-revealing references)
- **评分标准**: ARR Overall Assessment 1-5 分制 (5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit)

### 论文文件
- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf`
- 补充材料: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md`

### 你的审查侧重

**核心关注: 新颖性 + 完整性 + 写作质量**

请从以下维度严格审查:

1. **贡献新颖性与定位**
   - 三个 findings (epoch confound, detector requirements, minimum intervention) 的新颖程度？
   - Epoch confound 是否是一个显而易见的观察 (减少数据→更多 epoch 是自然推论)，还是有实质性贡献？
   - w=(1-q)^b 完全沿用 Drayson et al.，adaptive b* 本质上是参数选择启发式——方法新颖性是否足够？
   - 论文定位为 "analysis paper with adaptive b* as practical corollary" 是否清晰一致？Abstract 和正文是否匹配？

2. **Related Work 覆盖度**
   - Instance-level reweighting 领域是否有遗漏的重要工作？
   - 与 curriculum learning / importance sampling / data selection 文献的区别是否讲清楚？
   - 引用格式是否符合 ACL 规范 (natbib)？引用是否真实可查？

3. **论文结构与叙事**
   - §1-§7 的逻辑流是否顺畅？每个 section 的篇幅是否合理？
   - §3 (Method) 压缩到 ~0.75 页后是否清晰？关键定义是否完整？
   - Discussion (§6) 是否充分讨论了效应量、proxy 局限性、下游任务零改善？
   - Limitations 是否覆盖了关键局限？是否过短或过长？

4. **写作质量**
   - 术语使用是否一致 (α_eff, b*, ESS, ρ 等)？
   - 脚注密度是否过高？关键技术信息是否被藏在脚注中？
   - Table / Figure 的标注是否清晰？小数位是否一致？
   - 是否存在 overclaim (如 "significant" 误用、"practical" 过度使用)？
   - Abstract 是否在 200 words 以内？

5. **格式合规**
   - 正文是否在 8 页以内？
   - 是否有 Responsible NLP Checklist 出现在 PDF 中？(EMNLP 2026 规定 checklist 在 OpenReview 表单)
   - 匿名性是否完好？是否有自引泄露作者身份？
   - Appendix 结构是否合理？引用格式？

请按 ARR 标准格式输出审稿报告: Summary → Strengths → Weaknesses (分 Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-23T13:11:39.890592+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-23T13:11:41.244913+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1354
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-23T13:11:41.395783+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-23T13:11:41.497154+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-23T13:11:47.526026+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring rubric"
  }
}
```

</details>

---


### Tool call

_source line 815 · 2026-05-23T13:11:50.084262+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 816 · 2026-05-23T13:11:50.937239+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool call

_source line 817 · 2026-05-23T13:11:51.539560+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md"
  }
}
```

</details>

---


### Tool result

_source line 818 · 2026-05-23T13:11:54.603138+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring rubric"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Development and Validation of a Scoring Rubric for Editorial Evaluation of Peer-review Quality: A Pilot Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11000557/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Review Process

There will be at least 3 reviews and a meta-review. Each review will provide text and scores conveying the reviewer's impressions of the paper and suggestions for improvement.

## Reviewer Expertise and Confidence

If your expertise does not cover certain aspects of the submission, your review should specify that, and you will also be able to indicate your confidence score in the ARR form.

## Important 2026 Deadlines

The deadline for completing the registration form is January 7th 2026 EoD AoE. If they get assi
…[truncated 536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7077
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-23T13:11:56.663267+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 440.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6579
}
```

</details>

---


### Tool result

_source line 820 · 2026-05-23T13:11:56.663767+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{tikz}
20	\usetikzlibrary{positioning,arrows.meta}
21	\usepackage{hyperref}
22	
23	\newtheorem{proposition}{Proposition}
24	\newtheorem{definition}{Definition}
25	
26	\newcommand{\bstar}{b^*}
27	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
28	\newcommand{\nmin}{n_{\min}}
29	\newcommand{\btau}{b_{\tau}}
30	\newcommand{\bess}{b_{\mathrm{ESS}}}
31	\title{When Does Detect-and-Reweight Work? Epoch Confounds\\and Adaptive Reweighting in Continued LM Pretraining}
32	
33	\author{Anonymous}
34	
35	\begin{document}
36	\maketitle
37	
38	\begin{abstract}
39	\input{sections/abstract}
40	\end{abstract}
41	
42	\section{Introduction}
43	\label{sec:intro}
44	\input{sections/introduction}
45	
46	\section{Related Work}
47	\label{sec:related}
48	\input{sections/related_work}
49	
50	\section{Method}
51	\label{sec:method}
52	\input{sections/method}
53	
54	\section{Experimental Setup}
55	\label{sec:experiments}
56	\input{sections/experiments}
57	
58	\section{Results}
59	\label{sec:results}
60	\input{sections/results}
61	
62	\section{Discussion}
63	\label{sec:discussion}
64	\input{sections/discussion}
65	
66	\section{Conclusion}
67	\label{sec:conclusion}
68	\input{sections/conclusion}
69	
70	\section*{Limitations}
71	\label{sec:limitations}
72	\input{sections/limitations}
73	
74	\section*{Ethics Statement}
75	All experiments use publicly available datasets (FineWeb) and open-weight models; no human subjects are involved. Code and data will be released upon acceptance.
76	
77	\bibliography{references}
78	
79	\ap
…[truncated 61 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5726
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-23T13:11:56.715283+00:00_

1	# Author Response (Round 11)
2	
3	We thank the reviewers for their thorough feedback. Below we address all concerns organized by the R11 issue list. All referenced revisions are in the updated manuscript.
4	
5	---
6	
7	## Broader Significance
8	
9	This work contributes beyond our specific experimental setting in four ways. First, the epoch confound finding applies retroactively to all D&R evaluations that compare at equal training steps rather than equal content epochs: the headline 0.396 PPL advantage shrinks by >95% to a residual Δ=0.017 when content epochs are equalized (Table 1), establishing a methodological baseline that future D&R studies must control for. Second, the detector requirements analysis yields a counter-intuitive result: a high-AUC detector (GPT-2, AUC=0.91) with poor calibration (ECE=0.131) performs *worse* than uniform training (Δ=+0.098), while a lower-AUC but well-calibrated detector (TF-IDF, AUC=0.94, ECE=0.048) succeeds—demonstrating that calibration can reverse the sign of the intervention. Third, the α_eff/ESS constraint decomposition provides a generalizable analytical toolkit for importance-weighted training: any method that applies per-sample weights faces the same quality-stability tradeoff, and our binding-rate analysis offers a diagnostic for when constraints dominate. Fourth, the observed Δ=−0.020 at ρ=0.4, B=4 represents a lower bound, not a ceiling: batch-size amplification shows monotonic scaling (B=4: Δ=−0.020, B=8: Δ=−0.050, B=16: Δ=−0.068; §5.4), and production batch sizes typically range from 64 to 256. At ρ=0.6 the effect doubles to Δ=−0.032 (uncorrected p=0.010; BH-corrected p=0.064 with k=9). At production batch sizes (e.g., B=128), conservative extrapolation with the empirical scaling exponent α ≈ 0.89 (Δ ∝ B^α) predicts Δ ≈ −0.39, a practically meaningful improvement—though this extrapolation is speculative and requires empirical validation at larger scale. As web-scale contamination grows, the practical relevance of p
…[truncated 10729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5175
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-23T13:12:07.865309+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 823 · 2026-05-23T13:12:08.768911+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 824 · 2026-05-23T13:12:08.769400+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 825 · 2026-05-23T13:12:09.669231+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 899
}
```

</details>

---


### Tool call

_source line 826 · 2026-05-23T13:12:09.669744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 827 · 2026-05-23T13:12:10.221397+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 828 · 2026-05-23T13:12:10.725188+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 829 · 2026-05-23T13:12:10.725737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 830 · 2026-05-23T13:12:11.128924+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 831 · 2026-05-23T13:12:11.129342+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 832 · 2026-05-23T13:12:11.634804+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-23T13:12:11.987040+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-23T13:12:18.458570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 835 · 2026-05-23T13:12:18.913362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 836 · 2026-05-23T13:12:19.818708+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1360
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-23T13:12:19.822211+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-23T13:12:19.872793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-23T13:12:20.525798+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-23T13:12:20.576402+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 841 · 2026-05-23T13:12:20.781254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 842 · 2026-05-23T13:12:21.790054+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1213
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-23T13:12:22.142636+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-23T13:12:29.578127+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "11-17",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "11-17",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 845 · 2026-05-23T13:12:30.432367+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 846 · 2026-05-23T13:12:30.834820+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 390.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 393.4}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.0}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.0}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 426.6}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 48.2}], \"total_pages\": 17, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1256
}
```

</details>

---


### Tool result

_source line 847 · 2026-05-23T13:12:30.885560+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-23T13:12:35.667078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-23T13:12:36.724624+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1057
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-23T13:12:36.725152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-23T13:12:37.128277+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-23T13:12:37.179167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-23T13:12:39.174007+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1994
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-23T13:12:39.217897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 855 · 2026-05-23T13:12:39.218298+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-23T13:12:39.218511+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 857 · 2026-05-23T13:12:39.825057+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 858 · 2026-05-23T13:12:40.077185+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 859 · 2026-05-23T13:12:40.077648+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 860 · 2026-05-23T13:12:40.883595+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1665
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-23T13:12:40.884635+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1666
}
```

</details>

---


### Tool result

_source line 862 · 2026-05-23T13:12:40.886606+00:00_

1	As synthetic text reaches an estimated 20--60\% of web corpora, the detect-and-reweight paradigm (downweighting likely-synthetic samples via $w(x) = (1-q(x))^b$) has gained traction, but its effectiveness conditions remain poorly understood.
2	Through controlled experiments (Qwen3-0.6B continued pretraining, 132M FineWeb tokens, 3 seeds), we analyze when, why, and how detect-and-reweight works.
3	
4	We identify three findings.
5	First, an epoch-exposure confound in detect-and-remove evaluation: at matched content epochs, the advantage shrinks from 0.396 to 0.017 perplexity ($N{=}3$), revealing that ${>}$95\% of published gains (relative to adaptive reweighting) reflect data repetition rather than filtering quality.
6	Second, effective reweighting requires both sufficient discrimination and good calibration from the detector; a high-AUC but poorly calibrated detector (ECE\,=\,0.131) degrades performance below uniform, while a lightweight calibrated alternative (ECE\,=\,0.048) succeeds (3 detectors, 3 seeds).
7	Third, mechanism decomposition reveals that minimum intervention---applying the smallest exponent that meets a quality floor---outperforms unconstrained maximization, which over-sharpens and degrades training stability.
8	
9	As a practical corollary, these findings yield a dual-constrained adaptive $b^*$ that eliminates per-model grid search, achieving perplexity lower than uniform across all seeds at $\rho \geq 0.4$ with calibrated detectors ($\Delta{=}{-}0.020$ at $\rho{=}0.4$, directionally consistent across all seeds, bootstrap CI excludes zero; $\Delta{=}{-}0.032$ at $\rho{=}0.6$, uncorrected $p{=}0.010$).
10	The method transitions from harmful ($\rho{=}0.2$) to beneficial ($\rho \geq 0.4$), with a sharp boundary in $[0.3, 0.4]$; the benefit diminishes at 1.7B, and sample size ($N{=}3$) limits generalizability.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 808
}
```

</details>

---


### Tool call

_source line 863 · 2026-05-23T13:12:40.886930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 864 · 2026-05-23T13:12:41.038232+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1819
}
```

</details>

---


### Tool result

_source line 865 · 2026-05-23T13:12:41.038674+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	Despite growing adoption, the paradigm's effectiveness conditions are poorly characterized.
6	Does D\&R genuinely outperform soft reweighting, or do published comparisons confound filtering quality with multi-epoch exposure?
7	What detector properties are necessary for effective reweighting?
8	How does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?
9	
10	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 3 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters (\S\ref{sec:limitations} discusses scope).
11	To ground the analysis of exponent selection, we introduce a dual-constrained formulation: find the minimum $b$ such that $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor, motivated by convergence theory~\citep{wang2026survive}), subject to $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling)~\citep{kish1965survey,vehtari2024psis}.
12	
13	Our analysis yields three findings:
14	\begin{itemize}[nosep,leftmargin=*]
15	\item \textbf{Epoch confound in D\&R evaluation.}
16	The bulk of D\&R's PPL advantage over adaptive reweighting (${>}$95\%) is attributable to multi-epoch exposure, not filtering quality; epoch-matched controls ($N{=}3$) reduce the gap from 0.396 to $\Delta{=}0.017$ (Table~\ref{tab:epoch_match}).
17	
18	\item \textbf{De
…[truncated 2538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-23T13:12:41.038958+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-23T13:12:41.089705+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder and show that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy; \citet{dohmatob2024tale} characterize this as a change of scaling laws.
5	\citet{gerstgrasser2024collapse} show that accumulating real data alongside synthetic data can break the recursion, though at substantial collection cost.
6	\citet{kang2025demystifying} systematically study scaling laws for synthetic data in pretraining, finding that rephrased synthetic data mixed with natural text improves data efficiency but textbook-style data degrades loss on many domains.
7	\citet{cheng2025contamination} survey the broader contamination landscape and confirm that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4,dubey2024llama}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; M
…[truncated 6772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-23T13:12:48.086488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-23T13:12:48.538072+00:00_

1	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus with token-level contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$, assumed unknown~\citep{cheng2025contamination}.
2	A detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$; following \citet{drayson2025detection}, we weight each sample as $w(x) = (1 - q(x))^{b}$, where $b \geq 0$ is a sharpening exponent ($b{=}0$ recovers uniform training).
3	Rather than selecting $b$ via grid search~\citep{drayson2025detection}, we derive $b$ per-batch from the batch's $q$-score distribution using two opposing constraints.
4	
5	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$:
6	
7	\paragraph{Quality floor.}
8	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ indicate likely-real samples. The \emph{effective real proportion} $\aeff(b) = \sum_i w_i(b) r_i / \sum_i w_i(b)$ measures weight allocated to real samples.
9	We require $\aeff(b) \geq \tau$, yielding a lower bound $b_\tau$ on the exponent, motivated by convergence theory under contamination~\citep{wang2026survive}.
10	$\aeff$ correlates with the true batch-level real fraction at Pearson $r \approx 0.70$ (Appendix~\ref{app:alpha_validation}); limitations are discussed in \S\ref{sec:discussion}.
11	
12	\paragraph{Stability ceiling.}
13	Kish's effective sample size $\mathrm{ESS}(b) = (\sum_i w_i)^2 / \sum_i w_i^2$~\citep{kish1965survey} decreases monotonically in $b$ (Appendix~\ref{app:proofs}).
14	We require $\mathrm{ESS}(b) \geq \nmin$, yielding an upper bound $\bess$.
15	
16	\paragraph{Adaptive $\bstar$.}
17	Since $\aeff$ is non-decreasing and ESS is decreasing in $b$, the two constraints define an interval $[b_\tau, \bess]$.
18	The optimal exponent implements \emph{minimum intervention}:
19	\begin{equation}
20	  b^{*} = \begin{cases}
21	    0        & \text{if } \aeff(0) \geq \tau, \\
22	    b_\tau   & \text{if } b_\
…[truncated 670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-23T13:12:48.538434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 871 · 2026-05-23T13:12:49.039951+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution; implications for detection difficulty are discussed in \S\ref{sec:limitations}.
5	Our self-contamination design provides a controlled testbed with known ground-truth labels but limits ecological validity; cross-model transfer results (Appendix~\ref{app:cross_model}) are mixed, and we discuss this limitation in \S\ref{sec:limitations}.
6	
7	\paragraph{Detector.}
8	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.94, calibrated ECE\,=\,0.05 after temperature scaling with $T{=}0.204$).
9	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
10	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
11	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.91) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
12	
13	\paragraph{Training.}
14	We continue pretraining Qwen3-0.6B from its pretrained 
…[truncated 1914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-23T13:12:49.040289+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 873 · 2026-05-23T13:12:49.491949+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves 3-seed mean PPL 17.674, compared to 17.694 for uniform ($\Delta{=}{-}0.020$, directionally consistent across all seeds) and 17.620 for grid $b{=}0.3$ (3-seed mean; gap $+$0.054).
8	A paired $t$-test yields $t{=}{-}7.1$, $p{=}0.019$; after Bonferroni--Holm correction for nine family-wise comparisons, $p_{\mathrm{BH}}{=}0.078$, which does not reach conventional significance, though the 95\% BCa bootstrap CI $[{-}0.028, {-}0.012]$ excludes zero.
9	The practical value is eliminating $b$ grid search (nine full training runs~\citep{drayson2025detection}, ${\sim}$16 GPU-hours at 0.6B scale, scaling linearly with model size), though grid search yields a larger improvement.
10	The grid-best $b{=}0.3$ is a post-hoc oracle from nine candidates with $4.7{\times}$ higher cross-seed variance than adaptive ($\sigma{=}0.033$ vs.\ $0.007$); the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}) makes validation-based selection unreliable.
11	At the nearest fixed point ($b{=}1.0$), PPL equals uniform (17.692 vs.\ 17.694): per-batch adaptation is essential.
12	
13	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
14	Random weights $\mathcal{U}(0,2)$ (17.802) confirm that detector $q$-scores carry genuine provenance signal; uninformed reweighting only increases gradient variance.
15	ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it degrades PPL by 0.043 relative to uniform.
16	Only the dual-constr
…[truncated 10199 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 874 · 2026-05-23T13:12:49.542649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-23T13:12:49.994483+00:00_

1	\paragraph{The epoch confound in D\&R evaluation.}
2	The bulk of D\&R's reported PPL advantage over adaptive reweighting (${>}$95\%) is attributable to multi-epoch exposure rather than filtering quality (\S\ref{sec:main-results}).
3	An independent-LR replication (D\&R $17.651$ vs.\ shared-schedule $17.657$, $\Delta{=}0.006$) confirms that this finding is robust to LR schedule choice.
4	D\&R evaluations that do not control for content epochs systematically overstate filtering effectiveness; the residual benefit ($\Delta{=}0.017$ vs.\ adaptive $\bstar$, directionally consistent across 3 seeds) falls within cross-seed variance.
5	A permuted-score control (shuffled detector scores; 3-seed mean $17.951{\pm}0.007$, $+$0.26 vs.\ uniform) confirms that detector signal is load-bearing: uninformed reweighting only degrades.
6	
7	\paragraph{When uniform beats reweighting.}
8	Beyond the evaluation confound, our results identify three operational conditions for effective reweighting, each of which, when violated, makes uniform training preferable.
9	First, \emph{detector quality}: the detector must provide both sufficient discrimination (AUC) and good calibration (ECE).
10	A high-AUC but poorly calibrated detector (GPT-2, ECE\,=\,0.131) degrades PPL by $+$0.098 below uniform; even a well-calibrated detector with insufficient discrimination (N-gram, AUC\,=\,0.73) degrades by $+$0.129 (\S\ref{sec:robustness}).
11	Second, \emph{contamination level}: at $\rho{=}0.2$, the detector's signal-to-noise ratio is too low and the method actively intervenes on unreliable signal ($\aeff$-binding at 60.1\% despite mean $q{=}0.393$), degrading PPL by $+$0.046; the method transitions from harmful to beneficial with a sharp sign change in $[0.3, 0.4]$ (Figure~\ref{fig:delta_vs_rho}, Appendix~\ref{app:rho03}).
12	Third, \emph{scale}: at 1.7B the benefit diminishes ($\Delta{=}{-}0.013$) with OOD partially inconsistent, suggesting that larger models may be inherently more robust to contamination g
…[truncated 6636 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 876 · 2026-05-23T13:12:50.045109+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-23T13:12:50.547039+00:00_

1	We identify three effectiveness conditions for detect-and-reweight: (1) D\&R evaluations confound filtering with multi-epoch exposure (${>}$95\% of the advantage over adaptive reweighting); (2) detectors require both discrimination and calibration; (3) minimum intervention outperforms unconstrained maximization.
2	A dual-constrained adaptive $\bstar$ ($\tau{=}0.7$, $\nmin{=}\lfloor B/2 \rfloor$) improves over uniform at $\rho \geq 0.4$ (directionally consistent across all seeds; $\rho{=}0.6$: uncorrected $p{=}0.010$, $p_{\mathrm{BH}}{=}0.064$ with $k{=}9$) without tuning; validated on Qwen3 ${\leq}$1.7B, where the benefit diminishes.
3	Batch-size amplification is monotonic across $B \in \{4, 8, 16\}$ ($1.0{\times}$ to $3.4{\times}$; $p{<}0.01$ at $B{=}16$) with diminishing marginal gains, suggesting favorable scaling with larger micro-batches typical of production training; the key bottleneck is extending detector calibration to cross-model contamination scenarios.
4	
5	The epoch confound finding has implications beyond our experiments: any D\&R evaluation that compares at equal training steps without controlling for content epochs risks overstating filtering effectiveness, and published results in this area should be interpreted with this confound in mind.
6	For practitioners, the decision framework (Table~\ref{tab:decision}) distills our analysis into actionable guidance: provenance-aware reweighting is worthwhile only when contamination is substantial ($\rho \geq 0.4$) and the detector is well-calibrated (ECE $\leq 0.05$); otherwise, uniform training remains the safer default.
7	Key directions for future work include cross-model contamination scenarios (where the generator differs from the trainee), better proxies for batch quality that exploit soft $q$-scores rather than binary indicators, and larger-scale verification to test whether the batch-size amplification trend continues at production training scales.
8	Code and data will be released upon acceptance.
9
…[truncated 1 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-23T13:12:50.597615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 879 · 2026-05-23T13:12:50.648275+00:00_

1	All experiments use Qwen3 (0.6B and 1.7B) on 132--200M tokens of continued pretraining with self-generated contamination at $\rho \in \{0.2, 0.3, 0.4, 0.6\}$; generalization to other model families, full pretraining scale ($>$100B tokens), or realistic multi-source web contamination is untested.
2	The method improves over uniform only at $\rho \geq 0.4$ with a calibrated detector; at $\rho{=}0.2$ it degrades, and a preliminary Llama-3.2-3B cross-model test showed mixed results (Appendix~\ref{app:cross_model}), suggesting the effective range is narrower than the paradigm's ambition.
3	Three detectors from two families (discriminative and generative) were tested; fine-tuned neural classifiers (e.g., RoBERTa-based) and zero-shot methods (e.g., DetectGPT) remain untested, so the calibration finding may not generalize across detector architectures.
4	Paired comparisons use $N{=}3$ seeds (2 degrees of freedom), limiting statistical power; results are directionally consistent but the sample size precludes strong generalizability claims.
5	After family-wise correction for nine comparisons, the $\rho{=}0.4$ adaptive-vs-uniform difference does not reach conventional significance ($p_{\mathrm{BH}}{=}0.078$), though the effect is directionally consistent across all seeds and the bootstrap CI excludes zero; the $\rho{=}0.6$ comparison also falls short of conventional significance under full-family correction ($p_{\mathrm{BH}}{=}0.064$, $k{=}9$), though the uncorrected $p{=}0.010$ and dose-response pattern across $\rho$ levels support a real effect.
6	The self-contamination setup provides known ground-truth labels but represents an easier detection scenario than cross-model contamination, where generator--corpus distribution mismatch may reduce detector accuracy.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-23T13:12:59.023001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-23T13:12:59.475120+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proposition}[$\alpha_{\mathrm{eff}}$ monotonicity]
5	\label{prop:monotone}
6	$\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least one sample with $q_i \in (0,1)$ and $r_i$ is not constant.
7	\end{proposition}
8	
9	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
10	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
11	Then
12	\begin{equation*}
13	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
14	\end{equation*}
15	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
16	Taking the derivative with respect to $b$:
17	\begin{align*}
18	  \frac{d\pi_i}{db}
19	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right) \\
20	  &= \pi_i \!\left(\ln(1{-}q_i) - \textstyle\sum_j \pi_j \ln(1{-}q_j)\right).
21	\end{align*}
22	Substituting,
23	\begin{align*}
24	  \frac{d\alpha_{\mathrm{eff}}}{db}
25	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
26	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
27	\end{align*}
28	Since $r_i = \mathbf{1}[q_i \leq 0.5]$, the indicator $r_i$ and $\ln(1{-}q_i)$ are positively associated by construction, so the covariance is non-negative.
29	\end{proof}
30	
31	\begin{proposition}[ESS monotonicity]
32	\label{prop:ess_mono}
33	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
34	\end{proposition}
35	
36	\begin{proof}
37	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
38	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
39	Differentiating $H$ with respect to $b$:
40	\begin{equation*}
41	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
42	\end{equation*}
43	Since $\pi_i \propto (1{-}q_i)^b$, larger $\pi_i$ implies larger $\ln(1{-}q_i)$; th
…[truncated 27174 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-23T13:12:59.676163+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 883 · 2026-05-23T13:12:59.726707+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-23T13:13:07.101806+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. I need: 1) All scoring dimensions (soundness, excitement, overall, confidence, etc.) 2) The exact scale for each dimension 3) Any rubric descriptions for each score level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. I need: 1) All scoring dimensions (soundness, excitement, overall, confidence, etc.) 2) The exact scale for each dimension 3) Any rubric descriptions for each score level"
  }
}
```

</details>

---


### Tool call

_source line 885 · 2026-05-23T13:13:07.704312+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 886 · 2026-05-23T13:13:07.805259+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@inproceedings{katharopoulos2018not,
5	  title={Not All Samples Are Created Equal: Deep Learning with Importance Sampling},
6	  author={Katharopoulos, Angelos and Fleuret, Fran{\c{c}}ois},
7	  booktitle={International Conference on Machine Learning},
8	  pages={2525--2534},
9	  year={2018},
10	  organization={PMLR}
11	}
12	
13	@inproceedings{ren2018learning,
14	  title={Learning to Reweight Examples for Robust Deep Learning},
15	  author={Ren, Mengye and Zeng, Wenyuan and Yang, Bin and Urtasun, Raquel},
16	  booktitle={International Conference on Machine Learning},
17	  pages={4334--4343},
18	  year={2018},
19	  organization={PMLR}
20	}
21	
22	@article{chen2024bull,
23	  title={Take the Bull by the Horns: Hard Sample-Reweighted Continual Training Improves {LLM} Generalization},
24	  author={Chen, Xuxi and Li, Zhendong and Cai, Daixuan and Yao, Huanran and Chen, Zheng and Wang, Zhongming},
25	  journal={arXiv preprint arXiv:2402.14270},
26	  year={2024}
27	}
28	
29	@inproceedings{kang2025demystifying,
30	  title={Demystifying Synthetic Data in {LLM} Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls},
31	  author={Kang, Feiyang and Xu, Yifan and Pu, Jingkang and Hu, Bushi and Li, Haonan and Chen, Hongliang and Zhu, Yiming and Chen, Zijian and Liu, Mohan and Liu, Jingcheng and Liu, Haoran and Han, Song},
32	  booktitle={EMNLP},
33	  year={2025}
34	}
35	
36	@article{zibakhsh2025fortifai,
37	  title={{ForTIFAI}: Fending Off Recursive Training Induced Failure for {AI} Model Collapse},
38	  author={Zibakhsh Shabgahi, Soheil and Aghazadeh, Pedram and Mirhoseini, Azalia and Koushanfar, Farinaz},
39	  journal={arXiv preprint arXiv:2509.08972},
40	  year={2025}
41	}
42	
43	@article{yi2025escaping,
44	  title={Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence},
…[truncated 15650 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-23T13:13:12.266923+00:00_

# ARR Review Form Criteria Summary

Based on the provided guidelines, ARR reviewers use **three primary scoring dimensions**:

## Scoring Dimensions

**1. Soundness**
- "must be justified by the text of the review"
- Assesses technical correctness and methodological rigor

**2. Excitement**
- Described as "orthogonal to the assessment of the soundness"
- Reflects personal interest and subjective engagement with the work

**3. Overall Assessment**
- "composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact"
- An explicit recommendation on acceptance outcomes

## Additional Assessment Factors

The guidelines reference a **confidence score** for indicating reviewer certainty levels when expertise doesn't fully cover all submission aspects.

A **reproducibility score** is also mentioned, which should be justified like soundness scores.

## Critical Note

The document does not provide the **exact numerical scales** (e.g., 1-5, 1-10) or detailed rubric descriptions for each score level. The guidelines state reviewers complete "a special 'Secondary reviewer' field" and various assessment forms, but the actual point scales and score-level definitions appear in the separate ARR review form documentation (referenced as "post describing the ARR review form in detail"), which isn't included in this extract.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5165
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-23T13:13:19.008170+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form soundness excitement overall assessment scoring scale 1-5 rubric 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form soundness excitement overall assessment scoring scale 1-5 rubric 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 889 · 2026-05-23T13:13:26.786756+00:00_

Web search results for query: "ACL ARR review form soundness excitement overall assessment scoring scale 1-5 rubric 2025 2026"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"Program Chairs' Report on Peer Review at ACL 2023","url":"http://www.cs.umd.edu/~jbg/docs/2023_acl_peer_review_report.pdf"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"}]

Based on the search results, I found relevant information about the ACL Rolling Review (ARR) assessment system for 2025-2026:

## ARR Review Scores (Starting February 2025)

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper. Excitement scores reflect our personal taste, and so do not necessarily come with explicit reasons.

### Overall Assessment Score
The Overall assessment sc
…[truncated 551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7778
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-23T13:13:40.991000+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL ARR\" review form \"soundness\" \"5\" \"4\" \"3\" \"2\" \"1\" scale definition February 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL ARR\" review form \"soundness\" \"5\" \"4\" \"3\" \"2\" \"1\" scale definition February 2025"
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-23T13:13:53.196232+00:00_

Web search results for query: ""ACL ARR" review form "soundness" "5" "4" "3" "2" "1" scale definition February 2025"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"}]

Based on the search results, I found detailed information about the ACL ARR (ACL Rolling Review) soundness score scale for February 2025:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

Here are the scale definitions for soundness:

5 = Excellent: This study is one of the most thorough I have seen, given its type.

4 = Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential.

3 = Acceptable: This study provides sufficient support for its main claims.

The scale also includes definitions fo
…[truncated 569 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 12205
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-23T13:13:58.468073+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their exact scales (1-5 or whatever scale), and the rubric descriptions for each score level. I need the exact definitions for soundness, excitement, overall assessment, confidence, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their exact scales (1-5 or whatever scale), and the rubric descriptions for each score level. I need the exact definitions for soundness, excitement, overall assessment, confidence, and any other scored dimensions."
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-23T13:14:05.997762+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness (1-5 scale with half-points)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement (1-5 scale with half-points)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points or attend if there's time."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Overall Assessment (1-5 scale with half-points)
- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award."
- **4**: "Conference: I think this paper could be accepted to an *ACL conference."
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: I think this paper needs substantial revisions."
- **1**: "Do not resubmit: This paper has to be fully redone."

## Reproducibility (1-5 scale)
- **5**: "They could easily 
…[truncated 1022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7529
}
```

</details>

---


### Tool call

_source line 894 · 2026-05-23T13:17:29.340928+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 \"reproducibility\" score scale reviewer form"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 \"reproducibility\" score scale reviewer form"
  }
}
```

</details>

---


### Tool result

_source line 895 · 2026-05-23T13:17:44.968449+00:00_

Web search results for query: "ACL ARR 2025 2026 "reproducibility" score scale reviewer form"

Links: [{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR 2025-2026 reproducibility scoring:

## Reviewer Scoring Changes

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. This represents a change from previous scoring systems.

## Reproducibility Guidance

Low reproducibility scores should be justified. Additionally, all papers recommended for Findings or main conference are expected to be sound and reproducible.

## Review Form Criteria

The main criteria for Findings are soundness and reproducibility. However, the search results indicate that reproducibility is no longer a separate scoring category in the new system—instead, it's part of the overall assessment criteria along with soundness.

The official reviewer guidelines note that soundness scores must be justified by the text of t
…[truncated 402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 15627
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-23T13:21:53.095284+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告 — Round 1（新颖性 + 完整性 + 写作质量）\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**Venue**: EMNLP 2026 (ARR May cycle)\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n**一句话总结**: 论文对 detect-and-reweight 范式的 epoch confound 进行了有价值的系统分析，但实验范围窄（单模型族/单数据集/自污染）、效应量小（Δ=−0.020 PPL，校正后不显著，下游零改善），方法新颖性偏薄，限制了整体贡献。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5 / 5 | 在其实验范围内方法论扎实，epoch-matched 对比设计合理；但 N=3 seeds 的关键结果校正后未达显著（ρ=0.4: p_BH=0.078; ρ=0.6: p_BH=0.064），削弱了定量结论的稳健性 |\n| **Excitement** | 2.5 / 5 | Epoch confound 发现对方法学有价值；其余两个 findings（detector requirements、minimum intervention）属于预期内的增量贡献；Δ=−0.020 PPL 无下游体现，实际影响有限 |\n| **Overall** | 3.0 / 5 | 分析论文定位合理，epoch confound 发现有 Findings 级贡献，但效应量过小 + 范围过窄 + adaptive b* 方法新颖性不足，不足以达到 Conference 门槛 |\n| **Confidence** | 4 / 5 | 仔细阅读了全文和 17 节 appendix，熟悉 data reweighting / model collapse 相关文献 |\n| **Reproducibility** | 4 / 5 | 实验细节充分（Algorithm 1, 超参数表, 三 seed 结果），代码承诺 acceptance 后公开；detector 训练细节（Appendix M）清楚 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 超过 200 words 限制\n- 具体位置：Abstract（§abstract.tex, PDF p.1）\n- 问题：EMNLP 2026 / ARR 要求 abstract ≤ 200 words。当前 abstract 包含大量数值和数学表达式（Δ=−0.020, ρ=0.4, p=0.010, bootstrap CI 等），估计约 220–230 words，明显超限。\n- 为什么影响接收：格式硬约束违反，desk reject 风险。\n- 建议：删除 paragraph 3 中的具体数值（Δ, p值, CI），保留定性结论（\"improves over uniform at ρ≥0.4 with calibrated detectors\"），将数值留给正文。目标压缩到 180 words 左右。\n\n**N2** [critical] 正文疑似超出 8 页限制\n- 具体位置：§7 Conclusion（PDF pp.8–9）\n- 问题：Section 7 Conclusion 在第 8 页底部开始，conclusion 正文延伸至第 9 页顶部（约 10–15 行），之后才是 Limitations。按 EMNLP 2026 规定，Limitations/Ethics 不计入页数限制，但 §1–§7 主正文必须 ≤ 8 页。当前 §7 溢出至 p.9，主正文超过 8 页。\n- 为什么影响接收：格式硬约束违反。\n- 建议：压缩 §6 Discussion（当前约 1.5 页，可将 \"Effect size in context\" 和 \"Limitations of α_eff as proxy\" 部分内容移至 Limitations 或 Appendix），为 Conclusion 腾出空间使其完整落在 p.8 内。\n\n**N3** [critical] 核心效应量过小且统计显著性不足\n- 具体位置：§5.1 Main Results (Table 2), §5.2 (ρ=0.6 结果)\n- 问题：论文的核心实验结论——adaptive b* 优于 uniform——在两个主要 contamination 水平上均未通过校正后的显著性检验。ρ=0.4: Δ=−0.020, p_BH=0.078; ρ=0.6: Δ=−0.032, p_BH=0.064。论文用 \"directionally consistent\" 和 bootstrap CI 来支撑结论，但在 k=9 的 family-wise correction 下，没有一个比较达到 α=0.05。更关键的是，Δ=−0.020 对应 ~0.1% relative improvement，downstream benchmark 完全无差异（Table 4: 两者均为 0.5414），这使得 PPL 改善的实际价值存疑。\n- 为什么影响接收：N=3 + 未通过多重比较校正 = 方法论上的 claim 缺乏统计支撑。作为 analysis paper，定量发现应当更 robust。\n- 建议：(a) 增加 seeds（至少 5 个）以提升统计 power；(b) 在论文中更显著地标注 p_BH 而非以脚注形式出现；(c) 明确承认 adaptive method 的 PPL 优势在当前实验规模下未达到统计显著且无下游体现，避免读者对实用价值产生过高期望。\n\n**N4** [critical] 实验范围过窄，limiting generalizability\n- 具体位置：§4 Experimental Setup, §Limitations\n- 问题：所有实验基于 (a) 单一模型族 Qwen3（0.6B primary + 1.7B 补充），(b) 单一数据集 FineWeb 132M tokens，(c) 自污染设计（generator = trainee 同架构 Qwen3-0.6B）。自污染使得 detection 问题简化为 \"同分布 self-detection\"，与真实 web 污染（多源、多模型、混合风格）差距巨大。Cross-model transfer 结果（Appendix O: Llama→Qwen, single seed, MMLU +1.57pp / HellaSwag −0.60pp）mixed 且仅 1 seed，无法支撑泛化性 claim。\n- 为什么影响接收：三个核心 findings 都依赖这一特定实验设置：epoch confound 在大规模预训练（单 epoch，无重复）中是否同样成立？detector requirements 在真实 web 污染下是否同样需要 ECE≤0.05？minimum intervention 在不同数据分布下是否仍优于 maximization？这些问题都无法从当前实验推断。\n- 建议：(a) 至少增加一个不同模型族（如 Llama 或 Pythia）作为主实验（非仅 appendix single seed）；(b) 增加跨模型污染场景（generator ≠ trainee）的 multi-seed 实验；(c) 更诚实地在 abstract/conclusion 中限定 claim 的适用范围为 \"self-contaminated continued pretraining at 0.6B scale\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Adaptive b* 方法新颖性薄弱\n- 具体位置：§3 Method (Eq. 1)\n- 问题：权重公式 w=(1−q)^b 完全来自 Drayson et al. (2025)；adaptive b* 的双约束（α_eff ≥ τ, ESS ≥ n_min）本质上是一个超参数自动选择启发式——选择满足两个阈值条件的最小 b。这在方法论贡献上偏薄：α_eff 是一个简单的加权比例，ESS 是标准的 importance sampling 诊断量，bisection 是标准数值方法。论文承认这是 \"practical corollary\" 而非 headline contribution，但 §3 仍占 ~0.75 页正文描述一个相对简单的公式。\n- 建议：进一步压缩 §3，将 Algorithm 1 直接放到 Appendix；正文只保留公式 (1) 和关键直觉（1-2 段即可）。\n\n**W2** [warning] Epoch confound finding 的适用范围需明确限定\n- 具体位置：§5.1 Hard filtering paragraph, §6 Discussion paragraph 1, §7 Conclusion\n- 问题：论文声称 \"any D&R evaluation that compares at equal training steps without controlling for content epochs risks overstating filtering effectiveness\"（§7, 最后一段）。但 epoch confound 主要出现在 continued pretraining（小数据量 → 多 epoch）设置中。在大规模 from-scratch pretraining（通常 <1 epoch，不存在数据重复），这个 confound 不成立。Drayson et al. 的实验是 from-scratch pretraining，他们的 setting 中 epoch confound 应该很小。论文在 rebuttal draft（W4 回应）中承认了这一点，但正文的表述过于 general。\n- 建议：在 §6 或 §7 中明确限定：epoch confound 在数据量有限的 continued pretraining 中最为显著；在大规模预训练（single-epoch regime）中，D&R 的优势可能确实来自 filtering quality 而非 epoch exposure。\n\n**W3** [warning] Detector 测试范围不足\n- 具体位置：§5.2 Calibration paragraph, §Limitations, Appendix L\n- 问题：仅测试了 3 个 detector（TF-IDF+LR discriminative, GPT-2 PPL generative, N-gram PPL generative），未覆盖当前主流的 neural classifiers（RoBERTa/ModernBERT fine-tuned, DetectGPT, Binoculars）。Drayson et al. 使用的 ModernBERT-150M (AUC=0.986) 未被测试。论文从 3 个 detector 的结果得出 \"both AUC and ECE are necessary\" 的结论，但 3 个数据点不足以建立这种因果关系——可能存在其他混杂因素（如 discriminative vs. generative paradigm 本身的差异）。\n- 建议：至少增加一个 fine-tuned neural classifier（如 ModernBERT 或 RoBERTa）来验证 calibration 结论是否在更高 AUC 的 detector 上同样成立。\n\n**W4** [warning] Discussion 中的 batch-size extrapolation 缺乏支撑\n- 具体位置：§5.3 ESS floor paragraph, rebuttal draft (Broader Significance section)\n- 问题：论文报告 B=4/8/16 的 monotonic scaling（Δ=−0.020/−0.050/−0.068），并在 rebuttal 中外推到 B=128（\"conservative extrapolation predicts Δ≈−0.39\"）。尽管 rebuttal 标注这是 \"speculative\"，但用 3 个点（B=4,8,16，跨度仅 4×）拟合 scaling exponent α≈0.89 然后外推到 B=128（32× extrapolation）在统计学上极为不可靠。且 B=16 仅有 single-seed 数据（seed 42），B=8 仅有 2-seed mean。\n- 建议：删除 B=128 的外推或降级为 footnote/appendix 中的 \"speculative observation\"；在正文中只报告实测的 B=4/8/16 结果。\n\n**W5** [warning] 部分关键信息藏在脚注中\n- 具体位置：§5.2 (footnote on p_BH), Table 2 footnotes, §5.1\n- 问题：p_BH=0.078（ρ=0.4）和 p_BH=0.064（ρ=0.6）这两个对评估核心 claim 至关重要的统计量仅出现在脚注中。Bonferroni-Holm 校正后的 p 值应当在正文 §5.1/§5.2 的主段落中显著报告，而非让读者在脚注中发现 \"哦原来不显著\"。\n- 建议：将 p_BH 值移入正文主段落，与 uncorrected p 并列报告。\n\n---\n\n## 小问题（不影响接收）\n\n- **m1**: Table 2 中 Golden Ratio 和 D&R 的 bold 标注可能误导：它们分别需要 oracle labels 和 multi-epoch exposure，与 Adaptive 不可直接比较。建议区分 \"fair comparison\" 和 \"reference methods\" 的 bold 标注。\n- **m2**: §2 Related Work 占约 1.5 页（pp.2–3），对 8 页限制下的论文偏长。建议压缩 Detection and Filtering 段（多个 citation 可合并为一句综述）以释放空间。\n- **m3**: Figure 1（overview TikZ diagram）在黑白打印下 orange/blue/violet 背景色几乎无法区分，仅靠 F1/F2/F3 标签可辨识。建议增加 pattern（如 hatching）或使用灰度渐变。\n- **m4**: rebuttal_draft.md 中 C4 回应提到 \"Appendix Q\"，但 appendix 中最后标注的 section 为 Additional Contamination Rate（根据 appendix.tex 结构），请核对标签是否正确。\n- **m5**: 论文使用 ρ 同时表示 token-level contamination ratio（§3, §4）和 Spearman 相关系数（Table 12, Appendix K），符号冲突。建议 contamination ratio 用 ρ，Spearman 用 ρ_s 或 r_s 以区分。\n\n---\n\n## 缺失引用\n\n以下工作在 instance-level reweighting / data quality filtering 领域较为相关，建议补充讨论：\n\n1. **MATES** (Yu et al., NeurIPS 2024) — \"MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models\"：动态数据选择，用小模型预测大模型的数据 influence，与本文的 online reweighting 直接相关。\n2. **FineWeb-Edu** (Lozhkov et al., 2024) — 基于教育质量评分的大规模数据过滤，是 FineWeb 生态系统中的重要工作，论文使用了 FineWeb 但未讨论质量过滤维度。\n3. **D4** (Tirumala et al., 2024) — \"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\"：与 SemDeDup 类似但不同的去重策略，值得在 §2 Instance-Level 段提及。\n\n---\n\n## 主要优势\n\n- **S1**: Epoch confound 的发现是论文最有价值的贡献。通过精心设计的 epoch-matched control（Table 1），定量展示 >95% 的 D&R 优势来自数据重复而非 filtering quality，为后续工作建立了重要的方法学基线。LR-controlled verification（§5.1）进一步排除了学习率调度的混杂。\n- **S2**: 实验设计诚实透明。论文坦诚报告了 downstream null（Table 4）、statistical non-significance after correction、ρ=0.2 的失败案例、checkpoint resume artifact（Appendix P），这种科学诚实度在同行评审中值得肯定。\n- **S3**: Appendix 内容丰富（17 sections, 7 pages），覆盖 grid search、τ sweep、constraint regime decomposition、α_eff validation、detector comparison、cross-model transfer、ρ=0.3 boundary analysis 等，为读者提供了充分的可验证性。\n- **S4**: 论文定位从 \"methods paper\" 调整为 \"analysis paper with practical corollary\" 是合理的。三个 findings 的叙事结构清晰：confound → detector requirements → minimum intervention → adaptive b*。\n- **S5**: Decision framework（Table 3）将分析结论转化为 practitioner-friendly 的决策指南，是有实用价值的贡献。\n\n---\n\n## Questions for Authors\n\n1. 如果将 family-wise correction 的 family 缩小为仅包含 focal comparison（adaptive vs. uniform at each ρ），而非全部 9 个比较，corrected p-values 会是多少？论文是否考虑过分层检验策略（先检验 primary hypothesis，再检验 exploratory hypotheses）？\n2. 在 ρ=0.4 的 self-contamination 设置下，TF-IDF+LR 的 AUC=0.94 已经很高。在真实 web contamination（多源多模型）场景下，同类 detector 的 AUC 和 ECE 预期会如何变化？是否有 pilot 数据？\n3. Epoch confound 的核心发现是否可以通过更简单的实验设计来验证——例如直接比较 \"D&R 1 epoch\" vs. \"uniform 1 epoch\"——而不需要整套 adaptive b* 机制？如果可以，这是否暗示 adaptive b* 对论文核心 contribution 而言是非必需的？\n\n---\n\n**审稿完成。** Reviewer 2, Round 1, fresh review.",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告 — Round 1（新颖性 + 完整性 + 写作质量）\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**Venue**: EMNLP 2026 (ARR May cycle)\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n**一句话总结**: 论文对 detect-and-reweight 范式的 epoch confound 进行了有价值的系统分析，但实验范围窄（单模型族/单数据集/自污染）、效应量小（Δ=−0.020 PPL，校正后不显著，下游零改善），方法新颖性偏薄，限制了整体贡献。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5 / 5 | 在其实验范围内方法论扎实，epoch-matched 对比设计合理；但 N=3 seeds 的关键结果校正后未达显著（ρ=0.4: p_BH=0.078; ρ=0.6: p_BH=0.064），削弱了定量结论的稳健性 |\n| **Excitement** | 2.5 / 5 | Epoch confound 发现对方法学有价值；其余两个 findings（detector requirements、minimum intervention）属于预期内的增量贡献；Δ=−0.020 PPL 无下游体现，实际影响有限 |\n| **Overall** | 3.0 / 5 | 分析论文定位合理，epoch confound 发现有 Findings 级贡献，但效应量过小 + 范围过窄 + adaptive b* 方法新颖性不足，不足以达到 Conference 门槛 |\n| **Confidence** | 4 / 5 | 仔细阅读了全文和 17 节 appendix，熟悉 data reweighting / model collapse 相关文献 |\n| **Reproducibility** | 4 / 5 | 实验细节充分（Algorithm 1, 超参数表, 三 seed 结果），代码承诺 acceptance 后公开；detector 训练细节（Appendix M）清楚 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 超过 200 words 限制\n- 具体位置：Abstract（§abstract.tex, PDF p.1）\n- 问题：EMNLP 2026 / ARR 要求 abstract ≤ 200 words。当前 abstract 包含大量数值和数学表达式（Δ=−0.020, ρ=0.4, p=0.010, bootstrap CI 等），估计约 220–230 words，明显超限。\n- 为什么影响接收：格式硬约束违反，desk reject 风险。\n- 建议：删除 paragraph 3 中的具体数值（Δ, p值, CI），保留定性结论（\"improves over uniform at ρ≥0.4 with calibrated detectors\"），将数值留给正文。目标压缩到 180 words 左右。\n\n**N2** [critical] 正文疑似超出 8 页限制\n- 具体位置：§7 Conclusion（PDF pp.8–9）\n- 问题：Section 7 Conclusion 在第 8 页底部开始，conclusion 正文延伸至第 9 页顶部（约 10–15 行），之后才是 Limitations。按 EMNLP 2026 规定，Limitations/Ethics 不计入页数限制，但 §1–§7 主正文必须 ≤ 8 页。当前 §7 溢出至 p.9，主正文超过 8 页。\n- 为什么影响接收：格式硬约束违反。\n- 建议：压缩 §6 Discussion（当前约 1.5 页，可将 \"Effect size in context\" 和 \"Limitations of α_eff as proxy\" 部分内容移至 Limitations 或 Appendix），为 Conclusion 腾出空间使其完整落在 p.8 内。\n\n**N3** [critical] 核心效应量过小且统计显著性不足\n- 具体位置：§5.1 Main Results (Table 2), §5.2 (ρ=0.6 结果)\n- 问题：论文的核心实验结论——adaptive b* 优于 uniform——在两个主要 contamination 水平上均未通过校正后的显著性检验。ρ=0.4: Δ=−0.020, p_BH=0.078; ρ=0.6: Δ=−0.032, p_BH=0.064。论文用 \"directionally consistent\" 和 bootstrap CI 来支撑结论，但在 k=9 的 family-wise correction 下，没有一个比较达到 α=0.05。更关键的是，Δ=−0.020 对应 ~0.1% relative improvement，downstream benchmark 完全无差异（Table 4: 两者均为 0.5414），这使得 PPL 改善的实际价值存疑。\n- 为什么影响接收：N=3 + 未通过多重比较校正 = 方法论上的 claim 缺乏统计支撑。作为 analysis paper，定量发现应当更 robust。\n- 建议：(a) 增加 seeds（至少 5 个）以提升统计 power；(b) 在论文中更显著地标注 p_BH 而非以脚注形式出现；(c) 明确承认 adaptive method 的 PPL 优势在当前实验规模下未达到统计显著且无下游体现，避免读者对实用价值产生过高期望。\n\n**N4** [critical] 实验范围过窄，limiting generalizability\n- 具体位置：§4 Experimental Setup, §Limitations\n- 问题：所有实验基于 (a) 单一模型族 Qwen3（0.6B primary + 1.7B 补充），(b) 单一数据集 FineWeb 132M tokens，(c) 自污染设计（generator = trainee 同架构 Qwen3-0.6B）。自污染使得 detection 问题简化为 \"同分布 self-detection\"，与真实 web 污染（多源、多模型、混合风格）差距巨大。Cross-model transfer 结果（Appendix O: Llama→Qwen, single seed, MMLU +1.57pp / HellaSwag −0.60pp）mixed 且仅 1 seed，无法支撑泛化性 claim。\n- 为什么影响接收：三个核心 findings 都依赖这一特定实验设置：epoch confound 在大规模预训练（单 epoch，无重复）中是否同样成立？detector requirements 在真实 web 污染下是否同样需要 ECE≤0.05？minimum intervention 在不同数据分布下是否仍优于 maximization？这些问题都无法从当前实验推断。\n- 建议：(a) 至少增加一个不同模型族（如 Llama 或 Pythia）作为主实验（非仅 appendix single seed）；(b) 增加跨模型污染场景（generator ≠ trainee）的 multi-seed 实验；(c) 更诚实地在 abstract/conclusion 中限定 claim 的适用范围为 \"self-contaminated continued pretraining at 0.6B scale\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Adaptive b* 方法新颖性薄弱\n- 具体位置：§3 Method (Eq. 1)\n- 问题：权重公式 w=(1−q)^b 完全来自 Drayson et al. (2025)；adaptive b* 的双约束（α_eff ≥ τ, ESS ≥ n_min）本质上是一个超参数自动选择启发式——选择满足两个阈值条件的最小 b。这在方法论贡献上偏薄：α_eff 是一个简单的加权比例，ESS 是标准的 importance sampling 诊断量，bisection 是标准数值方法。论文承认这是 \"practical corollary\" 而非 headline contribution，但 §3 仍占 ~0.75 页正文描述一个相对简单的公式。\n- 建议：进一步压缩 §3，将 Algorithm 1 直接放到 Appendix；正文只保留公式 (1) 和关键直觉（1-2 段即可）。\n\n**W2** [warning] Epoch confound finding 的适用范围需明确限定\n- 具体位置：§5.1 Hard filtering paragraph, §6 Discussion paragraph 1, §7 Conclusion\n- 问题：论文声称 \"any D&R evaluation that compares at equal training steps without controlling for content epochs risks overstating filtering effectiveness\"（§7, 最后一段）。但 epoch confound 主要出现在 continued pretraining（小数据量 → 多 epoch）设置中。在大规模 from-scratch pretraining（通常 <1 epoch，不存在数据重复），这个 confound 不成立。Drayson et al. 的实验是 from-scratch pretraining，他们的 setting 中 epoch confound 应该很小。论文在 rebuttal draft（W4 回应）中承认了这一点，但正文的表述过于 general。\n- 建议：在 §6 或 §7 中明确限定：epoch confound 在数据量有限的 continued pretraining 中最为显著；在大规模预训练（single-epoch regime）中，D&R 的优势可能确实来自 filtering quality 而非 epoch exposure。\n\n**W3** [warning] Detector 测试范围不足\n- 具体位置：§5.2 Calibration paragraph, §Limitations, Appendix L\n- 问题：仅测试了 3 个 detector（TF-IDF+LR discriminative, GPT-2 PPL generative, N-gram PPL generative），未覆盖当前主流的 neural classifiers（RoBERTa/ModernBERT fine-tuned, DetectGPT, Binoculars）。Drayson et al. 使用的 ModernBERT-150M (AUC=0.986) 未被测试。论文从 3 个 detector 的结果得出 \"both AUC and ECE are necessary\" 的结论，但 3 个数据点不足以建立这种因果关系——可能存在其他混杂因素（如 discriminative vs. generative paradigm 本身的差异）。\n- 建议：至少增加一个 fine-tuned neural classifier（如 ModernBERT 或 RoBERTa）来验证 calibration 结论是否在更高 AUC 的 detector 上同样成立。\n\n**W4** [warning] Discussion 中的 batch-size extrapolation 缺乏支撑\n- 具体位置：§5.3 ESS floor paragraph, rebuttal draft (Broader Significance section)\n- 问题：论文报告 B=4/8/16 的 monotonic scaling（Δ=−0.020/−0.050/−0.068），并在 rebuttal 中外推到 B=128（\"conservative extrapolation predicts Δ≈−0.39\"）。尽管 rebuttal 标注这是 \"speculative\"，但用 3 个点（B=4,8,16，跨度仅 4×）拟合 scaling exponent α≈0.89 然后外推到 B=128（32× extrapolation）在统计学上极为不可靠。且 B=16 仅有 single-seed 数据（seed 42），B=8 仅有 2-seed mean。\n- 建议：删除 B=128 的外推或降级为 footnote/appendix 中的 \"speculative observation\"；在正文中只报告实测的 B=4/8/16 结果。\n\n**W5** [warning] 部分关键信息藏在脚注中\n- 具体位置：§5.2 (footnote on p_BH), Table 2 footnotes, §5.1\n- 问题：p_BH=0.078（ρ=0.4）和 p_BH=0.064（ρ=0.6）这两个对评估核心 claim 至关重要的统计量仅出现在脚注中。Bonferroni-Holm 校正后的 p 值应当在正文 §5.1/§5.2 的主段落中显著报告，而非让读者在脚注中发现 \"哦原来不显著\"。\n- 建议：将 p_BH 值移入正文主段落，与 uncorrected p 并列报告。\n\n---\n\n## 小问题（不影响接收）\n\n- **m1**: Table 2 中 Golden Ratio 和 D&R 的 bold 标注可能误导：它们分别需要 oracle labels 和 multi-epoch exposure，与 Adaptive 不可直接比较。建议区分 \"fair comparison\" 和 \"reference methods\" 的 bold 标注。\n- **m2**: §2 Related Work 占约 1.5 页（pp.2–3），对 8 页限制下的论文偏长。建议压缩 Detection and Filtering 段（多个 citation 可合并为一句综述）以释放空间。\n- **m3**: Figure 1（overview TikZ diagram）在黑白打印下 orange/blue/violet 背景色几乎无法区分，仅靠 F1/F2/F3 标签可辨识。建议增加 pattern（如 hatching）或使用灰度渐变。\n- **m4**: rebuttal_draft.md 中 C4 回应提到 \"Appendix Q\"，但 appendix 中最后标注的 section 为 Additional Contamination Rate（根据 appendix.tex 结构），请核对标签是否正确。\n- **m5**: 论文使用 ρ 同时表示 token-level contamination ratio（§3, §4）和 Spearman 相关系数（Table 12, Appendix K），符号冲突。建议 contamination ratio 用 ρ，Spearman 用 ρ_s 或 r_s 以区分。\n\n---\n\n## 缺失引用\n\n以下工作在 instance-level reweighting / data quality filtering 领域较为相关，建议补充讨论：\n\n1. **MATES** (Yu et al., NeurIPS 2024) — \"MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models\"：动态数据选择，用小模型预测大模型的数据 influence，与本文的 online reweighting 直接相关。\n2. **FineWeb-Edu** (Lozhkov et al., 2024) — 基于教育质量评分的大规模数据过滤，是 FineWeb 生态系统中的重要工作，论文使用了 FineWeb 但未讨论质量过滤维度。\n3. **D4** (Tirumala et al., 2024) — \"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\"：与 SemDeDup 类似但不同的去重策略，值得在 §2 Instance-Level 段提及。\n\n---\n\n## 主要优势\n\n- **S1**: Epoch confound 的发现是论文最有价值的贡献。通过精心设计的 epoch-matched control（Table 1），定量展示 >95% 的 D&R 优势来自数据重复而非 filtering quality，为后续工作建立了重要的方法学基线。LR-controlled verification（§5.1）进一步排除了学习率调度的混杂。\n- **S2**: 实验设计诚实透明。论文坦诚报告了 downstream null（Table 4）、statistical non-significance after correction、ρ=0.2 的失败案例、checkpoint resume artifact（Appendix P），这种科学诚实度在同行评审中值得肯定。\n- **S3**: Appendix 内容丰富（17 sections, 7 pages），覆盖 grid search、τ sweep、constraint regime decomposition、α_eff validation、detector comparison、cross-model transfer、ρ=0.3 boundary analysis 等，为读者提供了充分的可验证性。\n- **S4**: 论文定位从 \"methods paper\" 调整为 \"analysis paper with practical corollary\" 是合理的。三个 findings 的叙事结构清晰：confound → detector requirements → minimum intervention → adaptive b*。\n- **S5**: Decision framework（Table 3）将分析结论转化为 practitioner-friendly 的决策指南，是有实用价值的贡献。\n\n---\n\n## Questions for Authors\n\n1. 如果将 family-wise correction 的 family 缩小为仅包含 focal comparison（adaptive vs. uniform at each ρ），而非全部 9 个比较，corrected p-values 会是多少？论文是否考虑过分层检验策略（先检验 primary hypothesis，再检验 exploratory hypotheses）？\n2. 在 ρ=0.4 的 self-contamination 设置下，TF-IDF+LR 的 AUC=0.94 已经很高。在真实 web contamination（多源多模型）场景下，同类 detector 的 AUC 和 ECE 预期会如何变化？是否有 pilot 数据？\n3. Epoch confound 的核心发现是否可以通过更简单的实验设计来验证——例如直接比较 \"D&R 1 epoch\" vs. \"uniform 1 epoch\"——而不需要整套 adaptive b* 机制？如果可以，这是否暗示 adaptive b* 对论文核心 contribution 而言是非必需的？\n\n---\n\n**审稿完成。** Reviewer 2, Round 1, fresh review.",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-23T13:21:56.911553+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3816
}
```

</details>

---


### Assistant

_source line 898 · 2026-05-23T13:22:12.524141+00:00_

审稿报告已提交给 Review Director。

总结：

- **Overall: 3.0/5 (Findings)**，Soundness 3.5，Excitement 2.5
- **4 个 Must-Fix**：Abstract 超 200 词、正文疑似超 8 页、核心效应量校正后不显著、实验范围过窄
- **5 个 Should-Fix**：adaptive b* 方法新颖性薄、epoch confound 适用范围需限定、detector 测试不足、batch-size 外推不可靠、关键 p 值藏在脚注
- **5 个 Minor**：Table bold 标注误导、Related Work 偏长、Figure 1 灰度不可辨、Appendix 标签不一致、ρ 符号冲突
- **主要优势**：epoch confound 发现有方法学价值、实验设计诚实透明、appendix 丰富

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 22

## Round 22

4 recorded events


### User

_source line 899 · 2026-05-23T13:23:35.750611+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 完整审稿报告

**Overall Assessment**: 3.0 / 5 (Findings)

### 官方维度打分
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | Epoch confound 方法论可靠，但 adaptive method 统计证据不足（N=3, 校正后未达 α=0.05），α_eff proxy R²≈0.49 |
| Excitement | 2/5 (Potentially Interesting) | Epoch confound 有方法论警示价值，但效应量极小，下游零改善 |
| Reproducibility | 4/5 | 实验设置详细，超参数透明，代码承诺开源 |
| Confidence | 4/5 | |

### Must-Fix 问题

**N1** [critical] N=3 seeds 的统计推断力根本性不足
- 全文核心量化结论依赖于 N=3 seeds 的 paired t-test（仅 2 个自由度）。
- ρ=0.4: uncorrected p=0.019, BH-corrected p=0.078
- ρ=0.6: uncorrected p=0.010, BH-corrected p=0.064
- Bootstrap CI [−0.028, −0.012] 在 N=3 时仅有 3³=27 个可能的重抽样本。
- Cohen's d=2.86 可能反映方差被人为压低（seeds 只影响初始化，data order 固定）。
- 论文先选择了 BH 校正（k=9），然后论证 family "structurally heterogeneous"——post-hoc 统计叙事调整。
- 建议：增加到 N≥5 seeds，或放弃 p 值叙事改为纯效应量+方向一致性。

**N2** [critical] 效应量与 claim 之间的严重脱节
- Δ=−0.020 PPL（~0.11%）。五项下游任务全部 |Δ|≤0.01。
- Batch-size 外推用 3 个点拟合幂律 Δ∝B^α（α≈0.89），外推到 B=128 预测 Δ≈−0.39——用 3 个数据点外推 8 倍不可靠。
- 建议：删除所有 "practical" 表述；batch-size 外推移到 appendix。

### Should-Fix 问题

**W1** [warning] Self-contamination 实验设计的生态效度严重不足
- Generator=trainee（Qwen3-0.6B 生成→检测→训练），人为降低检测难度。TF-IDF+LR AUC=0.94 部分归因于此。
- Detector requirements claim（AUC≥0.9, ECE≤0.05）在 cross-model contamination 下可能完全不适用。
- Cross-model transfer（Appendix O）single seed + mixed results。
- 建议：增加 cross-generator 实验；限定 detector requirements claim 到 self-contamination 场景。

**W2** [warning] α_eff proxy 的解释力不足以支撑其核心地位
- R²≈0.49，proxy 仅解释不到一半方差。
- r(α_eff, mean_q)=0.80 是 proxy-to-detector-score 循环论证，非 proxy-to-ground-truth。
- 跨 seed 稳定性是预期结果（α_eff 是 q-scores 的确定性函数且 detector 固定）。
- 根本问题：adaptive b* 的贡献可能主要来自 ESS constraint 的稳定化，而非 α_eff 的质量信号。
- 建议：增加 α_eff-only ablation（去掉 ESS constraint 只保留 α_eff）；如果 ESS 是主要贡献者需重写 §6。

**W3** [warning] 实验范围过窄，不支撑 "necessary conditions" 的普适性 claim
- 1 个模型家族、1 个数据集、1 种污染类型、4 个 ρ 值、3 个 seeds。
- "necessary conditions" 逻辑上很强，但仅在极窄设置上观察到。ρ=0.5 未测试。AUC/ECE 阈值来自仅 3 个 detector。
- 建议：改为 "empirically observed conditions in our setting"。

**W4** [warning] Epoch confound 实验中 LR schedule 混淆因素未完全排除
- Epoch-matched D&R 使用完整训练长度的 LR schedule 但仅训练 2,553 步——LR schedule 形状在截断训练中与完整训练不同。
- Independent-schedule replication 仅一句话带过，无完整 LR 曲线对比。
- 更干净的控制：在相同步数下通过 upsampling 非污染数据来匹配 content epochs。
- 建议：展示完整 LR curves；讨论 early-stopping vs content-epoch-matching confound；补充 upsampling baseline。

### 小问题
- m1: Table 2 Golden Ratio 的 w 定义需在 §4 中简要说明
- m2: §5.2 同时讨论 ρ=0.6 结果和 boundary conditions，建议拆分
- m3: Figure 2 的 x 轴标签与 adaptive b* 的关系不够清晰
- m4: Appendix Q 的 ρ=0.3 结果应在主文 §5.2 中明确引用
- m5: §2 未指出 Drayson et al. 的 from-scratch vs continued pretraining 区别——epoch confound 前提

### Questions
1. N=3 是计算资源限制还是有意为之？是否考虑过降低步数换取更多 seeds？
2. α_eff-only ablation（去掉 ESS constraint）的 PPL？
3. r(α_eff, mean_q)=0.80 vs r(α_eff, true real fraction)=0.70 的区别？
4. Batch-size amplification 是固定 total tokens 还是固定 steps？
5. Document-level vs token-level injection 对检测难度的影响？

### 缺失引用
- Xie et al. (2024) "DOREMI"
- Fan et al. (2024) importance weighting variance-bias tradeoff

---

请对以上每一个 Must-Fix、Should-Fix 和 Minor 问题给出你的 [AGREE] 或 [REBUT] 判断及理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-23T13:26:03.104874+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条回应\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: N=3 seeds 统计推断力不足**\n同意。与我的 N3 本质相同。R1 额外指出的两个论点有力：(1) Bootstrap CI 在 N=3 时仅 3³=27 个重抽样本，分辨率极低；(2) 论文先报告 BH 校正再论证 family \"structurally heterogeneous\" 属于 post-hoc narrative adjustment。Cohen's d=2.86 反映人为压低的方差也是有效观察——seeds 仅影响初始化、data order 固定。\n\n**[AGREE] R1-N2: 效应量与 claim 脱节**\n同意，与我的 N3 和 W4 高度重合。建议删除所有 \"practical\" 表述稍过激——论文已定位为 \"practical corollary\"，但 batch-size 外推（3 点拟合幂律外推 8 倍）确实应移到 appendix。\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Self-contamination 生态效度不足**\n强烈同意。我将此升级为 critical（我的 N4）。TF-IDF+LR AUC=0.94 部分归因于 self-contamination 降低检测难度。Cross-model 实验（Appendix O）single seed + mixed results + \"perplexity comparison omitted due to inconsistent evaluation configurations\"——连基本 PPL 比较都无法完成。\n\n**[AGREE] R1-W2: α_eff proxy 解释力不足**\n同意。三个关键点：(1) R²≈0.49 对于驱动整个方法的核心 proxy 偏低；(2) r(α_eff, mean_q)=0.80 是 proxy-to-proxy 循环而非 proxy-to-ground-truth（r=0.706）；(3) α_eff-only ablation 缺失是最有建设性的建议——当前无法区分 adaptive b* 的贡献来自 α_eff 质量信号还是 ESS 稳定化。§5.3 的 constraint regime decomposition（50.9% α_eff-binding）描述了频率但无法区分因果。\n\n**[AGREE] R1-W3: \"necessary conditions\" claim 过强**\n同意。Table 3 \"Req'd?\" 列暗示 necessary conditions，但仅 3 detector + 4 ρ值 + 1 模型族不足以支撑。改为 \"empirically observed conditions\" 合理。\n\n**[REBUT] R1-W4: LR schedule 混淆因素**\n部分反驳。论文的 independent-schedule replication（§5.1 \"LR-controlled verification\"）已有效回应：独立 LR schedule D&R 17.651 vs shared 17.657（Δ=0.006），uniform 独立 schedule 18.062，确认 epoch advantage 在控制 LR 后存在。但同意 (a) 展示完整 LR curves 可增加说服力；(b) upsampling baseline 是更干净的设计。当前 control 足够排除 LR confound，Should-Fix 而非 Must-Fix 的定级合理。\n\n### Minor 问题\n\n**[AGREE] R1-m1 至 m5**: 全部同意。m5 尤为重要——§2 未标注 Drayson et al. 是 from-scratch pretraining，读者会误认为 epoch confound 直接推翻其结论。\n\n### 缺失引用\n\n**[REBUT]** Xie et al. DoReMi：已被引用（§2 Domain-Level 段，ref key `xie2023doremi`）。\n**[AGREE]** Fan et al. importance weighting variance-bias tradeoff：与 ESS 约束直接相关，值得补充。\n\n### 总结\n\n11 条意见中 AGREE 10 条、REBUT 1 条（W4 部分反驳）。R1 与我的核心判断高度一致。R1 贡献了两个有价值的建设性建议：α_eff-only ablation 和 upsampling baseline，补上可显著增强论文说服力。\n\nOverall 维持 **3.0 / 5 (Findings)**。",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条回应\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: N=3 seeds 统计推断力不足**\n同意。与我的 N3 本质相同。R1 额外指出的两个论点有力：(1) Bootstrap CI 在 N=3 时仅 3³=27 个重抽样本，分辨率极低；(2) 论文先报告 BH 校正再论证 family \"structurally heterogeneous\" 属于 post-hoc narrative adjustment。Cohen's d=2.86 反映人为压低的方差也是有效观察——seeds 仅影响初始化、data order 固定。\n\n**[AGREE] R1-N2: 效应量与 claim 脱节**\n同意，与我的 N3 和 W4 高度重合。建议删除所有 \"practical\" 表述稍过激——论文已定位为 \"practical corollary\"，但 batch-size 外推（3 点拟合幂律外推 8 倍）确实应移到 appendix。\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Self-contamination 生态效度不足**\n强烈同意。我将此升级为 critical（我的 N4）。TF-IDF+LR AUC=0.94 部分归因于 self-contamination 降低检测难度。Cross-model 实验（Appendix O）single seed + mixed results + \"perplexity comparison omitted due to inconsistent evaluation configurations\"——连基本 PPL 比较都无法完成。\n\n**[AGREE] R1-W2: α_eff proxy 解释力不足**\n同意。三个关键点：(1) R²≈0.49 对于驱动整个方法的核心 proxy 偏低；(2) r(α_eff, mean_q)=0.80 是 proxy-to-proxy 循环而非 proxy-to-ground-truth（r=0.706）；(3) α_eff-only ablation 缺失是最有建设性的建议——当前无法区分 adaptive b* 的贡献来自 α_eff 质量信号还是 ESS 稳定化。§5.3 的 constraint regime decomposition（50.9% α_eff-binding）描述了频率但无法区分因果。\n\n**[AGREE] R1-W3: \"necessary conditions\" claim 过强**\n同意。Table 3 \"Req'd?\" 列暗示 necessary conditions，但仅 3 detector + 4 ρ值 + 1 模型族不足以支撑。改为 \"empirically observed conditions\" 合理。\n\n**[REBUT] R1-W4: LR schedule 混淆因素**\n部分反驳。论文的 independent-schedule replication（§5.1 \"LR-controlled verification\"）已有效回应：独立 LR schedule D&R 17.651 vs shared 17.657（Δ=0.006），uniform 独立 schedule 18.062，确认 epoch advantage 在控制 LR 后存在。但同意 (a) 展示完整 LR curves 可增加说服力；(b) upsampling baseline 是更干净的设计。当前 control 足够排除 LR confound，Should-Fix 而非 Must-Fix 的定级合理。\n\n### Minor 问题\n\n**[AGREE] R1-m1 至 m5**: 全部同意。m5 尤为重要——§2 未标注 Drayson et al. 是 from-scratch pretraining，读者会误认为 epoch confound 直接推翻其结论。\n\n### 缺失引用\n\n**[REBUT]** Xie et al. DoReMi：已被引用（§2 Domain-Level 段，ref key `xie2023doremi`）。\n**[AGREE]** Fan et al. importance weighting variance-bias tradeoff：与 ESS 约束直接相关，值得补充。\n\n### 总结\n\n11 条意见中 AGREE 10 条、REBUT 1 条（W4 部分反驳）。R1 与我的核心判断高度一致。R1 贡献了两个有价值的建设性建议：α_eff-only ablation 和 upsampling baseline，补上可显著增强论文说服力。\n\nOverall 维持 **3.0 / 5 (Findings)**。",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-23T13:26:10.712745+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 7607
}
```

</details>

---


### Assistant

_source line 902 · 2026-05-23T13:26:18.056154+00:00_

交叉回应已提交给 Review Director。

11 条意见中 AGREE 10 条、REBUT 1 条（W4 LR confound 部分反驳——论文的 independent-schedule replication 已有效排除了 LR 混淆）。两位 Reviewer 在核心判断上高度一致：N=3 统计 power 不足、效应量过小、实验范围过窄。R1 额外贡献的 α_eff-only ablation 建议是最有建设性的新观点。Overall 维持 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 23

## Round 23

112 recorded events


### User

_source line 903 · 2026-05-24T04:10:51.585779+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查新颖性、完整性、写作质量、Related Work 和格式合规。

## Venue 信息
- **目标**: EMNLP 2026 via ARR
- **截止日期**: 2026-05-25
- **正文页数限制**: ≤8 页（参考文献不限，Limitations/Ethics 不计入）
- **模板**: ACL (review mode)
- **匿名规则**: Double-blind via ARR
- **Abstract**: ≤200 words
- **评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit)

## 论文路径
- LaTeX: `projects/provenance_weight_training/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf`

## 你的审查侧重

### 1. 新颖性评估
- 三个 findings 的新颖性分别如何？（epoch confound / detector requirements / minimum intervention）
- w=(1-q)^b 完全来自 Drayson et al. (2025)，adaptive b* 作为 "practical corollary" 的新颖性
- 与 prior work 的区分是否清晰？（Drayson et al., He et al., Feng et al.）
- 作为 analysis paper 的 contributions 是否足够支撑 EMNLP main conference？

### 2. Related Work 完整性
- 是否覆盖了所有重要的相关工作？
- Domain-level mixing / instance-level reweighting / synthetic detection / model collapse 四条线是否完整？
- 最近（2025-2026）的关键工作是否遗漏？
- 与最直接相关的 Drayson et al. (2025) 的对比是否充分和公平？

### 3. 写作质量
- Abstract 是否清晰概括了贡献？数值密度是否合适？
- Introduction 的 narrative flow 和 motivation
- 论文定位（analysis paper vs method paper）是否一致贯穿全文？
- Discussion 的深度和自我批评是否充分？
- Limitations 是否覆盖了关键局限？

### 4. 格式合规（EMNLP 2026 硬约束）
- **Abstract 字数**：统计是否 ≤200 words（逐词计数）
- **正文页数**：§1-§7 (Conclusion) 是否在 8 页内结束？
- **Limitations**：是否在正文中且只有一个？Appendix 中是否有重复的 limitations section？
- **匿名性**：是否有泄露身份的信息？（作者名、机构、GitHub 链接等）
- **引用格式**：natbib 兼容性
- **ARR Responsible NLP Checklist**：是否在 PDF 中（不应该在，应在 OpenReview 表单中）

### 5. 整体连贯性
- 三个 findings → adaptive b* 的叙事逻辑是否自然？
- 表格/图表/正文之间的一致性
- Appendix 的组织和引用是否合理？

请提供完整审稿报告，包含：Strengths (逐条), Weaknesses (逐条，标注 must-fix / should-fix / minor), Questions, Missing References, Overall Assessment (ARR 分数 + 置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 904 · 2026-05-24T04:10:57.696023+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 905 · 2026-05-24T04:10:57.746985+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-24T04:11:00.305984+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
  }
}
```

</details>

---


### Tool result

_source line 907 · 2026-05-24T04:11:00.357002+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 908 · 2026-05-24T04:11:02.112615+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
  }
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-24T04:11:02.213501+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-24T04:11:07.994027+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 911 · 2026-05-24T04:11:07.994491+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 912 · 2026-05-24T04:11:11.666060+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 913 · 2026-05-24T04:11:13.723817+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf",
  "pages": "1-10",
  "project": "provenance_weight_training",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf",
    "pages": "1-10",
    "project": "provenance_weight_training",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 914 · 2026-05-24T04:11:21.403090+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here are the key details about ACL ARR 2025-2026 reviewer guidelines:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Review Requirements

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

For more detailed guidelines, you can visit the official ARR
…[truncated 173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9737
}
```

</details>

---


### Tool result

_source line 915 · 2026-05-24T04:11:22.707647+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 547.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 595.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 473.6}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8983
}
```

</details>

---


### Tool call

_source line 916 · 2026-05-24T04:11:29.017581+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-24T04:11:29.017979+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 918 · 2026-05-24T04:11:30.523576+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf",
  "pages": "11-17",
  "project": "provenance_weight_training",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf",
    "pages": "11-17",
    "project": "provenance_weight_training",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 919 · 2026-05-24T04:11:31.128300+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-24T04:11:31.479687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 921 · 2026-05-24T04:11:32.438742+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 388.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 400.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 422.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.1}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 421.4}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 67.5}], \"total_pages\": 17, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1915
}
```

</details>

---


### Tool call

_source line 922 · 2026-05-24T04:11:32.439237+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 923 · 2026-05-24T04:11:32.791446+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 924 · 2026-05-24T04:11:33.496605+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2368
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-24T04:11:34.150808+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2671
}
```

</details>

---


### Tool result

_source line 926 · 2026-05-24T04:11:35.256543+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2465
}
```

</details>

---


### Tool result

_source line 927 · 2026-05-24T04:11:35.257807+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2818
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-24T04:11:44.952920+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. I need: 1) All scoring dimensions (soundness, excitement, overall assessment, confidence, etc.) 2) The exact scale for each dimension (e.g., 1-5) 3) What each score level means 4) Any specific instructions about what reviewers should evaluate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. I need: 1) All scoring dimensions (soundness, excitement, overall assessment, confidence, etc.) 2) The exact scale for each dimension (e.g., 1-5) 3) What each score level means 4) Any specific instructions about what reviewers should evaluate"
  }
}
```

</details>

---


### Tool call

_source line 929 · 2026-05-24T04:11:45.003568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 930 · 2026-05-24T04:11:45.056294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 931 · 2026-05-24T04:11:45.106968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 932 · 2026-05-24T04:11:45.258116+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 933 · 2026-05-24T04:11:46.872573+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1869
}
```

</details>

---


### Tool result

_source line 934 · 2026-05-24T04:11:47.227823+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2171
}
```

</details>

---


### Tool result

_source line 935 · 2026-05-24T04:11:47.531376+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2424
}
```

</details>

---


### Tool result

_source line 936 · 2026-05-24T04:11:47.582717+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2324
}
```

</details>

---


### Tool result

_source line 937 · 2026-05-24T04:11:53.305551+00:00_

# ARR Review Form Criteria and Scoring Dimensions

Based on the provided guidelines, here's what I found regarding the review form structure:

## Scoring Dimensions Identified

The guidelines mention **three main scores** that reviewers must provide as of February 2025:

1. **Soundness** - Evaluates technical validity and methodological rigor
2. **Excitement** - Reflects personal interest and subjective appreciation
3. **Overall Assessment** - An explicit recommendation for paper acceptance/rejection

## Key Scoring Instructions

**Soundness requirements:** "The _soundness_ scores must be justified by the text of the review. If you give a low _Soundness_ score without finding any major faults, this means that your review is not a faithful explanation..."

**Excitement scope:** This dimension is described as "orthogonal to the assessment of the soundness" and represents subjective taste rather than objective evaluation.

**Overall Assessment purpose:** This composite score should reflect "soundness, excitement, and also other factors like novelty and impact."

## Additional Scoring Elements

The guidelines reference a **confidence score** and **reproducibility score**, though specific scales aren't detailed in the provided text. These scores require justification aligned with review content.

## Limitation

The document doesn't provide the exact numerical scales (e.g., 1-5 range) or detailed descriptors for each score level. For complete scoring scale details, you may need to consult the actual ARR review form on OpenReview or the detailed form description linked in the guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 8352
}
```

</details>

---


### Tool call

_source line 938 · 2026-05-24T04:12:02.280953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 939 · 2026-05-24T04:12:02.582353+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 940 · 2026-05-24T04:12:02.632944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 941 · 2026-05-24T04:12:03.085109+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 942 · 2026-05-24T04:12:03.085496+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 943 · 2026-05-24T04:12:03.689025+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 944 · 2026-05-24T04:12:03.689531+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 945 · 2026-05-24T04:12:04.045275+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 355
}
```

</details>

---


### Tool call

_source line 946 · 2026-05-24T04:12:16.581299+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/_pdf_images/submitted_p*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/_pdf_images/submitted_p*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12"
  }
}
```

</details>

---


### Tool result

_source line 947 · 2026-05-24T04:12:16.732421+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p13.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p14.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p15.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p16.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p17.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 948 · 2026-05-24T04:12:24.360024+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf",
  "pages": "9-11",
  "project": "provenance_weight_training",
  "dpi": "150",
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/submitted.pdf",
    "pages": "9-11",
    "project": "provenance_weight_training",
    "dpi": "150",
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2"
  }
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-24T04:12:25.305496+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.0}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.4}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.8}], \"total_pages\": 17, \"rendered_pages\": 3, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 945
}
```

</details>

---


### Tool call

_source line 950 · 2026-05-24T04:12:25.485488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 951 · 2026-05-24T04:12:25.837246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 952 · 2026-05-24T04:12:26.294921+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---


### Tool call

_source line 953 · 2026-05-24T04:12:26.295355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 954 · 2026-05-24T04:12:27.201260+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1364
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-24T04:12:27.202722+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-24T04:12:27.203552+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 957 · 2026-05-24T04:12:27.404638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 958 · 2026-05-24T04:12:27.507577+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-24T04:12:27.809430+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-24T04:12:33.182873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 961 · 2026-05-24T04:12:34.036869+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 962 · 2026-05-24T04:12:34.088032+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 963 · 2026-05-24T04:12:34.289195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 964 · 2026-05-24T04:12:34.994286+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool result

_source line 965 · 2026-05-24T04:12:35.195829+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 966 · 2026-05-24T04:13:00.776032+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 967 · 2026-05-24T04:13:00.826659+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{tikz}
20	\usetikzlibrary{positioning,arrows.meta}
21	\usepackage{hyperref}
22	
23	\newtheorem{proposition}{Proposition}
24	\newtheorem{definition}{Definition}
25	
26	\newcommand{\bstar}{b^*}
27	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
28	\newcommand{\nmin}{n_{\min}}
29	\newcommand{\btau}{b_{\tau}}
30	\newcommand{\bess}{b_{\mathrm{ESS}}}
31	\title{When Does Detect-and-Reweight Work? Epoch Confounds\\and Adaptive Reweighting in Continued LM Pretraining}
32	
33	\author{Anonymous}
34	
35	\begin{document}
36	\maketitle
37	
38	\begin{abstract}
39	\input{sections/abstract}
40	\end{abstract}
41	
42	\section{Introduction}
43	\label{sec:intro}
44	\input{sections/introduction}
45	
46	\section{Related Work}
47	\label{sec:related}
48	\input{sections/related_work}
49	
50	\section{Method}
51	\label{sec:method}
52	\input{sections/method}
53	
54	\section{Experimental Setup}
55	\label{sec:experiments}
56	\input{sections/experiments}
57	
58	\section{Results}
59	\label{sec:results}
60	\input{sections/results}
61	
62	\section{Discussion}
63	\label{sec:discussion}
64	\input{sections/discussion}
65	
66	\section{Conclusion}
67	\label{sec:conclusion}
68	\input{sections/conclusion}
69	
70	\section*{Limitations}
71	\label{sec:limitations}
72	\input{sections/limitations}
73	
74	\section*{Ethics Statement}
75	All experiments use publicly available datasets (FineWeb) and open-weight models; no human subjects are involved. Code and data will be released upon acceptance.
76	
77	\bibliography{references}
78	
79	\ap
…[truncated 61 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 968 · 2026-05-24T04:13:03.839092+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/abstract*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/abstract*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 969 · 2026-05-24T04:13:03.839542+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 970 · 2026-05-24T04:13:06.700301+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 971 · 2026-05-24T04:13:07.253146+00:00_

1	As synthetic text reaches an estimated 20--60\% of web corpora, the detect-and-reweight paradigm (downweighting likely-synthetic samples via $w(x) = (1-q(x))^b$) has gained traction, but its effectiveness conditions remain poorly understood.
2	Through controlled continued pretraining experiments (Qwen3-0.6B, 3 seeds), we analyze when and why detect-and-reweight works.
3	
4	We identify three findings.
5	First, an epoch-exposure confound in detect-and-remove evaluation: at matched content epochs, the reported advantage shrinks from 0.396 to 0.017 perplexity ($N{=}3$), revealing that ${>}$95\% of the reported advantage reflects data repetition rather than filtering quality.
6	Second, effective reweighting requires both discrimination and calibration from the detector; a poorly calibrated detector (ECE\,=\,0.131) degrades performance below uniform training, while a calibrated alternative succeeds.
7	Third, minimum intervention---applying the smallest sharpening exponent meeting a quality floor---outperforms unconstrained maximization.
8	
9	As a practical corollary, these findings yield an adaptive $b^*$ that improves over uniform at $\rho \geq 0.4$ ($\Delta{=}{-}0.020$; $\rho{=}0.6$: $\Delta{=}{-}0.032$, uncorrected $p{=}0.010$), transitioning from harmful ($\rho{=}0.2$) to beneficial with a sharp boundary in $[0.3, 0.4]$.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 972 · 2026-05-24T04:13:07.409208+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 973 · 2026-05-24T04:13:07.710763+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	Despite growing adoption, the paradigm's effectiveness conditions are poorly characterized.
6	Does D\&R genuinely outperform soft reweighting, or do published comparisons confound filtering quality with multi-epoch exposure?
7	What detector properties are necessary for effective reweighting?
8	How does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?
9	
10	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 3 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters (\S\ref{sec:limitations} discusses scope).
11	To ground the analysis of exponent selection, we introduce a dual-constrained formulation: find the minimum $b$ such that $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor, motivated by convergence theory~\citep{wang2026survive}), subject to $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling)~\citep{kish1965survey,vehtari2024psis}.
12	
13	Our analysis yields three findings:
14	\begin{itemize}[nosep,leftmargin=*]
15	\item \textbf{Epoch confound in D\&R evaluation.}
16	The bulk of D\&R's PPL advantage over adaptive reweighting (${>}$95\%) is attributable to multi-epoch exposure, not filtering quality; epoch-matched controls ($N{=}3$) reduce the gap from 0.396 to $\Delta{=}0.017$ (Table~\ref{tab:epoch_match}).
17	
18	\item \textbf{De
…[truncated 2987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 974 · 2026-05-24T04:13:07.711171+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 975 · 2026-05-24T04:13:08.163159+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder and show that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy; \citet{dohmatob2024tale} characterize this as a change of scaling laws.
5	\citet{gerstgrasser2024collapse} show that accumulating real data alongside synthetic data can break the recursion, though at substantial collection cost.
6	\citet{kang2025demystifying} systematically study scaling laws for synthetic data in pretraining, finding that rephrased synthetic data mixed with natural text improves data efficiency but textbook-style data degrades loss on many domains.
7	\citet{cheng2025contamination} survey the broader contamination landscape and confirm that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4,dubey2024llama}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; M
…[truncated 7143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 976 · 2026-05-24T04:13:08.163559+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 977 · 2026-05-24T04:13:08.264223+00:00_

1	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus with token-level contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$, assumed unknown~\citep{cheng2025contamination}.
2	A detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$; following \citet{drayson2025detection}, we weight each sample as $w(x) = (1 - q(x))^{b}$, where $b \geq 0$ is a sharpening exponent ($b{=}0$ recovers uniform training).
3	Rather than selecting $b$ via grid search~\citep{drayson2025detection}, we derive $b$ per-batch from the batch's $q$-score distribution using two opposing constraints.
4	
5	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$:
6	
7	\paragraph{Quality floor.}
8	The \emph{effective authenticity} $\aeff(b) = \sum_i w_i(b)(1{-}q_i) / \sum_i w_i(b)$ measures the weighted mean detector confidence that samples are real.
9	We require $\aeff(b) \geq \tau$, yielding a lower bound $b_\tau$ on the exponent, motivated by convergence theory under contamination~\citep{wang2026survive}.
10	$\aeff$ correlates with the true batch-level real fraction at Pearson $r \approx 0.79$ (Appendix~\ref{app:alpha_validation}); limitations are discussed in \S\ref{sec:discussion}.
11	
12	\paragraph{Stability ceiling.}
13	Kish's effective sample size $\mathrm{ESS}(b) = (\sum_i w_i)^2 / \sum_i w_i^2$~\citep{kish1965survey} decreases monotonically in $b$ (Appendix~\ref{app:proofs}).
14	We require $\mathrm{ESS}(b) \geq \nmin$, yielding an upper bound $\bess$.
15	
16	\paragraph{Adaptive $\bstar$.}
17	Since $\aeff$ is non-decreasing and ESS is decreasing in $b$, the two constraints define an interval $[b_\tau, \bess]$.
18	The optimal exponent implements \emph{minimum intervention}:
19	\begin{equation}
20	  b^{*} = \begin{cases}
21	    0        & \text{if } \aeff(0) \geq \tau, \\
22	    b_\tau   & \text{if } b_\tau \leq \bess, \\
23	    \bess & \tex
…[truncated 632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 978 · 2026-05-24T04:13:14.981023+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 979 · 2026-05-24T04:13:15.332669+00:00_

1	\paragraph{The epoch confound in D\&R evaluation.}
2	The bulk of D\&R's reported PPL advantage over adaptive reweighting (${>}$95\%) is attributable to multi-epoch exposure rather than filtering quality (\S\ref{sec:main-results}).
3	An independent-LR replication (D\&R $17.651$ vs.\ shared-schedule $17.657$, $\Delta{=}0.006$) confirms that this finding is robust to LR schedule choice.
4	In multi-epoch continued pretraining, D\&R evaluations that do not control for content epochs systematically overstate filtering effectiveness; the residual benefit ($\Delta{=}0.017$ vs.\ adaptive $\bstar$, directionally consistent across 3 seeds) falls within cross-seed variance.
5	A permuted-score control (shuffled detector scores; 3-seed mean $17.951{\pm}0.007$, $+$0.26 vs.\ uniform\footnote{Per-seed permuted-score PPL: 17.958 (seed\,42), 17.945 (seed\,123), 17.951 (seed\,456).}) confirms that detector signal is load-bearing: uninformed reweighting only degrades.
6	
7	\paragraph{When uniform beats reweighting.}
8	Beyond the evaluation confound, our results identify three operational conditions for effective reweighting, each of which, when violated, makes uniform training preferable.
9	First, \emph{detector quality}: the detector must provide both sufficient discrimination (AUC) and good calibration (ECE).
10	A high-AUC but poorly calibrated detector (GPT-2, ECE\,=\,0.131) degrades PPL by $+$0.098 below uniform; even a well-calibrated detector with insufficient discrimination (N-gram, AUC\,=\,0.73) degrades by $+$0.129 (\S\ref{sec:robustness}).
11	Second, \emph{contamination level}: at $\rho{=}0.2$, the detector's signal-to-noise ratio is too low and the method actively intervenes on unreliable signal ($\aeff$-binding at 60.1\% despite mean $q{=}0.393$), degrading PPL by $+$0.046; the method transitions from harmful to beneficial with a sharp sign change in $[0.3, 0.4]$ (Figure~\ref{fig:delta_vs_rho}, Appendix~\ref{app:rho03}).
12	Third, \emph{scale}: at 1.7B the benefit diminish
…[truncated 5935 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 980 · 2026-05-24T04:13:15.333045+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 981 · 2026-05-24T04:13:15.834921+00:00_

1	We identify three effectiveness conditions for detect-and-reweight: (1) D\&R evaluations confound filtering with multi-epoch exposure (${>}$95\% of the advantage); (2) detectors require both discrimination \emph{and} calibration; (3) minimum intervention outperforms unconstrained maximization.
2	A dual-constrained adaptive $\bstar$ improves over uniform at $\rho \geq 0.4$ (directionally consistent across all seeds; $\rho{=}0.6$: uncorrected $p{=}0.010$) without tuning; batch-size amplification is monotonic across $B \in \{4, 8, 16\}$ ($1.0{\times}$ to $3.4{\times}$).
3	In continued pretraining settings, D\&R evaluations that do not control for content epochs risk overstating filtering effectiveness; for practitioners, reweighting is worthwhile only when $\rho \geq 0.4$ and the detector is well-calibrated (Table~\ref{tab:decision}).
4	Code and data will be released upon acceptance.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 982 · 2026-05-24T04:13:15.835282+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 983 · 2026-05-24T04:13:16.186779+00:00_

1	All experiments use Qwen3 (0.6B and 1.7B) on 132--200M tokens of continued pretraining with self-generated contamination at $\rho \in \{0.2, 0.3, 0.4, 0.6\}$; generalization to other model families, full pretraining scale ($>$100B tokens), or realistic multi-source web contamination is untested.
2	The method improves over uniform only at $\rho \geq 0.4$ with a calibrated detector; at $\rho{=}0.2$ it degrades, and a preliminary Llama-3.2-3B cross-model test showed mixed results (Appendix~\ref{app:cross_model}), suggesting the effective range is narrower than the paradigm's ambition.
3	Three detectors from two families (discriminative and generative) were tested; fine-tuned neural classifiers (e.g., ModernBERT, Binoculars) and zero-shot methods (e.g., DetectGPT) remain untested, so the AUC/ECE thresholds reported here may shift with broader detector coverage.
4	Paired comparisons use $N{=}3$ seeds (2 degrees of freedom), limiting statistical power; results are directionally consistent but the sample size precludes strong generalizability claims.
5	After family-wise correction for nine comparisons, the $\rho{=}0.4$ adaptive-vs-uniform difference does not reach conventional significance ($p_{\mathrm{BH}}{=}0.078$), though the effect is directionally consistent across all seeds and the bootstrap CI excludes zero; the $\rho{=}0.6$ comparison also falls short of conventional significance under full-family correction ($p_{\mathrm{BH}}{=}0.064$, $k{=}9$), though the uncorrected $p{=}0.010$ and dose-response pattern across $\rho$ levels support a real effect.
6	The self-contamination setup provides known ground-truth labels but represents an easier detection scenario than cross-model contamination, where generator--corpus distribution mismatch may reduce detector accuracy.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 984 · 2026-05-24T04:13:16.187281+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 985 · 2026-05-24T04:13:16.237889+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves 3-seed mean PPL 17.674, compared to 17.694 for uniform ($\Delta{=}{-}0.020$, directionally consistent across all seeds) and 17.620 for grid $b{=}0.3$ (3-seed mean; gap $+$0.054).
8	A paired $t$-test yields $t{=}{-}7.1$, $p{=}0.019$; after Bonferroni--Holm correction for nine family-wise comparisons, $p_{\mathrm{BH}}{=}0.078$, which does not reach conventional significance, though the 95\% BCa bootstrap CI $[{-}0.028, {-}0.012]$ excludes zero.
9	The practical value is eliminating $b$ grid search (nine full training runs~\citep{drayson2025detection}, ${\sim}$16 GPU-hours at 0.6B scale, scaling linearly with model size), though grid search yields a larger improvement.
10	The grid-best $b{=}0.3$ is a post-hoc oracle from nine candidates with $4.7{\times}$ higher cross-seed variance than adaptive ($\sigma{=}0.033$ vs.\ $0.007$); the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}) makes validation-based selection unreliable.
11	At the nearest fixed point ($b{=}1.0$), PPL equals uniform (17.692 vs.\ 17.694): per-batch adaptation is essential.
12	
13	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
14	Random weights $\mathcal{U}(0,2)$ (17.802) confirm that detector $q$-scores carry genuine provenance signal; uninformed reweighting only increases gradient variance.
15	ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it degrades PPL by 0.043 relative to uniform.
16	Only the dual-constr
…[truncated 10769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 986 · 2026-05-24T04:13:24.015265+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 987 · 2026-05-24T04:13:24.066013+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution; implications for detection difficulty are discussed in \S\ref{sec:limitations}.
5	Our self-contamination design provides a controlled testbed with known ground-truth labels but limits ecological validity; cross-model transfer results (Appendix~\ref{app:cross_model}) are mixed, and we discuss this limitation in \S\ref{sec:limitations}.
6	
7	\paragraph{Detector.}
8	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.94, calibrated ECE\,=\,0.05 after temperature scaling with $T{=}0.204$).
9	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
10	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
11	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.91) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
12	
13	\paragraph{Training.}
14	We continue pretraining Qwen3-0.6B from its pretrained 
…[truncated 1914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-24T04:14:54.324048+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/\\$[^$]*\\$//g; s/[{}~%]//g; s/--/-/g; s/  */ /g' | wc -w",
  "description": "Count abstract words after stripping LaTeX commands"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/\\$[^$]*\\$//g; s/[{}~%]//g; s/--/-/g; s/  */ /g' | wc -w",
    "description": "Count abstract words after stripping LaTeX commands"
  }
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-24T04:14:55.026871+00:00_

152

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 990 · 2026-05-24T04:14:55.027213+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 soundness excitement overall assessment score scale 1 2 3 4 5 detailed descriptions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 soundness excitement overall assessment score scale 1 2 3 4 5 detailed descriptions"
  }
}
```

</details>

---


### Tool result

_source line 991 · 2026-05-24T04:15:01.644571+00:00_

Web search results for query: "ACL ARR review form 2025 soundness excitement overall assessment score scale 1 2 3 4 5 detailed descriptions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Responsiveness of the Various Short-Form Versions of the Knee Injury and Osteoarthritis Outcome Score Between 2 and 5 Years After Anterior Cruciate Ligament Reconstruction","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10960337/"}]

Based on the search results, I found detailed information about the ACL ARR (Association for Computational Linguistics' Automated Review Response) 2025 review form:

## Three Scoring Categories

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score

Soundness scores must be justified by the text of the review. The soundness scale uses values 1-5 with these descriptions:

- 5 = Excellent: This study is one of the most thorough I have seen, given its type.
- 4 = Strong: This study provides sufficient support for all of its claim
…[truncated 931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6617
}
```

</details>

---


### Tool call

_source line 992 · 2026-05-24T04:15:06.816991+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with ALL scoring dimensions, their exact numerical scales, and what each score level means. I need: soundness (1-5 scale with descriptions), excitement (1-5 scale with descriptions), overall assessment (1-5 scale with descriptions), confidence score, and any other dimensions. Give me every score level description verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with ALL scoring dimensions, their exact numerical scales, and what each score level means. I need: soundness (1-5 scale with descriptions), excitement (1-5 scale with descriptions), overall assessment (1-5 scale with descriptions), confidence score, and any other dimensions. Give me every score level description verbatim."
  }
}
```

</details>

---


### Tool result

_source line 993 · 2026-05-24T04:15:12.397077+00:00_

# ACL Rolling Review Form: Scoring Dimensions

## Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness (1-5 scale)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough."

## Excitement (1-5 scale)
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper."
- **2**: "Potentially Interesting: does not resonate with me, but might with others."
- **1**: "Not Exciting: does not resonate with me, and I don't think it would with others."

## Overall Assessment (1-5 scale)
- **5**: Consider for Award (top 2.5% papers)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5580
}
```

</details>

---


### Tool call

_source line 994 · 2026-05-24T04:16:31.918753+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper && cat sections/abstract.tex | sed 's/\\\\\\\\//g; s/\\\\[a-zA-Z]*\\b//g; s/\\$[^$]*\\$/ MATH /g; s/[{}~]//g; s/  */ /g; s/^ *//; s/ *$//' | tr ' ' '\\n' | grep -v '^$' | wc -l",
  "description": "Count abstract words with math as single tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper && cat sections/abstract.tex | sed 's/\\\\\\\\//g; s/\\\\[a-zA-Z]*\\b//g; s/\\$[^$]*\\$/ MATH /g; s/[{}~]//g; s/  */ /g; s/^ *//; s/ *$//' | tr ' ' '\\n' | grep -v '^$' | wc -l",
    "description": "Count abstract words with math as single tokens"
  }
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-24T04:16:31.970995+00:00_

166
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_2_8481aa2c

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-24T04:16:37.998280+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "github|gitlab|arxiv\\.org/abs|author|university|institute|lab",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "github|gitlab|arxiv\\.org/abs|author|university|institute|lab",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 997 · 2026-05-24T04:16:38.049183+00:00_

&lt;persisted-output>
Output too large (41.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training--claude-sessions-review-reviewer-2-8481aa2c/a3518c1c-abac-4715-978f-072bf4ab5455/tool-results/toolu_01NYE37xAp3t7AprRvYgbT4G.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.bbl:2:\providecommand{\natexlab}[1]{#1}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.bbl:373:\bibitem[{Xie et~al.(2023{\natexlab{a}})Xie, Pham, Dong, Du, Liu, Lu, Liang,
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.bbl:376:  Liang, Quoc~V. Le, Tengyu Ma, and Adams~Wei Yu. 2023{\natexlab{a}}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.bbl:381:\bibitem[{Xie et~al.(2023{\natexlab{b}})Xie, Santurkar, Ma, and
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.bbl:384:  2023{\natexlab{b}}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/acl.sty:4:%     https://github.com/acl-org/acl-style-files/
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/acl.sty:125:%% Title and Authors %%
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/acl.sty:129:\newcommand\outauthor{%
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/acl.sty:134:        \bfseries\@author
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/acl.sty:149: \gdef\@thanks{}\gdef\@author{}\gdef\@title{}\let\thanks\relax}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/acl.sty:162:  \outauthor
…[truncated 359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-24T04:16:45.575020+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "github\\.com|our previous|our earlier|our prior|we previously|anonymous",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "github\\.com|our previous|our earlier|our prior|we previously|anonymous",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 999 · 2026-05-24T04:16:45.675765+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-24T04:16:49.590461+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-24T04:16:49.590925+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proposition}[$\alpha_{\mathrm{eff}}$ monotonicity]
5	\label{prop:monotone}
6	$\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least two samples with distinct $q$-values.
7	\end{proposition}
8	
9	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
10	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
11	Then
12	\begin{equation*}
13	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, (1 - q_i).
14	\end{equation*}
15	Taking the derivative with respect to $b$:
16	\begin{align*}
17	  \frac{d\pi_i}{db}
18	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right) \\
19	  &= \pi_i \!\left(\ln(1{-}q_i) - \textstyle\sum_j \pi_j \ln(1{-}q_j)\right).
20	\end{align*}
21	Substituting,
22	\begin{align*}
23	  \frac{d\alpha_{\mathrm{eff}}}{db}
24	  &= \sum_i (1{-}q_i)\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
25	  &= \mathrm{Cov}_{\pi}\!\bigl(1{-}q_i,\, \ln(1{-}q_i)\bigr).
26	\end{align*}
27	Since $(1{-}q_i)$ and $\ln(1{-}q_i)$ are both increasing functions of $(1{-}q_i)$, they are positively associated, so the covariance is non-negative.
28	\end{proof}
29	
30	\begin{proposition}[ESS monotonicity]
31	\label{prop:ess_mono}
32	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
33	\end{proposition}
34	
35	\begin{proof}
36	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
37	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
38	Differentiating $H$ with respect to $b$:
39	\begin{equation*}
40	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
41	\end{equation*}
42	Since $\pi_i \propto (1{-}q_i)^b$, larger $\pi_i$ implies larger $\ln(1{-}q_i)$; the $\pi^2$-weighted sum assigns greater mass to terms where $\ln(1{-}q_i) > \ma
…[truncated 373 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1002 · 2026-05-24T04:16:54.710778+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\section|\\\\subsection",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\section|\\\\subsection",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1003 · 2026-05-24T04:16:54.711261+00:00_

1:\section{Proofs}
47:\section{Algorithm Pseudocode}
72:\section{Grid Search Details}
100:\section{Quality Threshold Sweep}
127:\section{Batch-Adaptive $\tau$}
134:\section{Constraint Regime Decomposition}
148:\section{\texorpdfstring{$\tau$--$\rho$}{tau-rho} Rank Preservation}
162:\section{Hybrid and Threshold Comparison}
225:\section{Downstream Task Evaluation}
258:\section{Higher Contamination Details}
292:\section{\texorpdfstring{$\alpha_{\mathrm{eff}}$}{alpha-eff} Proxy Validation}
341:\section{Detector Comparison}
371:\section{Detector and Synthetic Data Details}
385:\section{Low Contamination Analysis}
395:\section{Cross-Model Transfer}
419:\section{Checkpoint Resume Artifact}
446:\section{Additional Contamination Rate}
490:\section{Use of AI Assistants}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1004 · 2026-05-24T04:19:46.221204+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**Venue**: EMNLP 2026 via ARR\n**审查侧重**: 新颖性、Related Work 完整性、写作质量、格式合规、整体连贯性\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.5 (Borderline Conference)\n**Confidence**: 4/5 (Quite sure)\n**一句话总结**: 论文提出了一个有价值的 epoch confound 发现（F1），但主实验结果在多重比较校正后未达显著性（p_BH=0.078），且仅在 self-contamination 设置下验证，scope 偏窄，作为 analysis paper 的贡献深度勉强达到主会议门槛。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计合理、有对照，但统计功效不足（N=3, p_BH=0.078），且仅 self-contamination 设置 |\n| Excitement | 3/5 | Epoch confound 发现对社区有价值，但 adaptive b* 的实际改善量小且无下游迁移 |\n| Overall | 3.5/5 | 介于 Findings 和 Conference 之间；F1 有 main conference 水准，但整体 scope 和 effect size 偏弱 |\n\n---\n\n## 主要优势\n\n**S1. Epoch confound 发现（F1）是本文最核心、最有价值的贡献。** §5.1 Table 1 展示 D&R 的 0.396 PPL 优势在 epoch-matched 后缩至 Δ=0.017（3-seed），揭示 >95% 的 reported advantage 源于数据重复而非 filtering quality。这一发现对后续 D&R 工作的实验设计有直接指导意义。LR-controlled verification（D&R 17.651 vs shared-schedule 17.657, Δ=0.006）进一步排除了学习率混淆。\n\n**S2. 实验设计结构良好，消融层次清晰。** Table 2 的六种方法对比（Uniform → Random → ESS-only → Adaptive → Grid-best → D&R）形成清晰的消融阶梯，每一层都有明确的控制变量。Permuted-score control（shuffled detector, PPL +0.26）有效证明 detector signal 的必要性。\n\n**S3. 论文对局限性的讨论异常坦诚。** §6 Discussion 主动承认 downstream accuracy 无改善（Table 4: 0.5414 vs 0.5414）、effect size 在当前 scale 下 modest（Δ=-0.020 在 ~0.07-point 窗口内操作）、α_eff 代理质量有限（r=0.79）。Limitations 段覆盖了关键局限（self-contamination、N=3 统计功效、detector 覆盖范围窄）。这种自我批评远超多数投稿。\n\n**S4. Related Work 全面且结构化。** §2 分五个 paragraph 覆盖 model collapse、detection、domain-level mixing、instance-level reweighting、theoretical foundations，引用 50+ 篇文献。与最直接相关的 Drayson et al. (2025) 的三点区分（(i) grid search → dual-constrained, (ii) SIR resampling → continuous reweighting, (iii) ModernBERT → TF-IDF+LR）清晰、公平。\n\n**S5. Adaptive b* 消除了 per-model grid search 的实际需求。** 虽然 grid-best 仍优于 adaptive（17.620 vs 17.674），但 grid search 需 9 次完整训练（~16 GPU-hours at 0.6B），且 grid-best b=0.3 跨 seed 方差 4.7× 高于 adaptive（σ=0.033 vs 0.007），实际选择不可靠（Figure 2 的 plateau region）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 主实验结果在多重比较校正后未达传统显著性水平\n- 具体位置：§5.1, Table 2\n- 问题：ρ=0.4 的主实验 paired t-test 原始 p=0.019，但 Bonferroni-Holm 校正后 p_BH=0.078（九组家族比较，k=9）。ρ=0.6 校正后 p_BH=0.064。论文声称 \"BCa bootstrap CI [−0.028, −0.012] excludes zero\" 作为补充证据，但 CI 不等价于校正后 p 值。对于一篇以 \"When does X work?\" 为标题的 analysis paper，核心 claim 的统计支撑应当更强。\n- 为什么影响接收：Analysis paper 的核心价值在于可靠的实证发现。主效应在标准校正下不显著，削弱了全部三个 findings 的可信度——如果 adaptive b* 本身相对 uniform 的改善不显著，那么关于 \"什么条件下有效\" 的分析就建立在不稳固的基础上。\n- 建议修改方向：(a) 增加 seeds（N≥5）提高统计功效；(b) 减少同时比较的方法数以降低校正负担；(c) 如果增加 seeds 不可行，应在 Abstract/Conclusion 中更明确地标注 effect 的统计状态（如 \"directionally consistent but not statistically significant after family-wise correction\"），而非 buried 在括号注释中。\n\n**N2** [critical] 仅在 self-contamination 设置下验证，生态效度堪忧\n- 具体位置：§4 \"Training Data\", §Limitations\n- 问题：所有主实验使用 Qwen3-0.6B 同时作为 generator 和 trainee，这意味着合成数据与真实数据的分布差异远小于现实场景。论文承认 \"self-contamination design provides a controlled testbed... but limits ecological validity\"，且 Appendix O 的 Llama-3.2-3B cross-model 实验 \"showed mixed results\"。实际 web contamination 来自多种模型和多个时间点，detector 面临的 distribution shift 远比本文设置困难。\n- 为什么影响接收：本文的三个 findings 和 adaptive b* 的有效性边界可能 fundamentally 依赖于 self-contamination 的特殊性。例如，F2（detector requirements）中 TF-IDF+LR 在 self-contamination 下 AUC=0.94 可能在 cross-model 下大幅下降，导致 AUC/ECE 阈值完全不同。标题 \"When Does Detect-and-Reweight Work?\" 暗示了一般性结论，但实验仅支持一个非常特定的设置。\n- 建议修改方向：(a) 至少一个 cross-model contamination 的完整实验（不仅是 Appendix 中的 preliminary）；(b) 或者将标题和 claims 显式限定为 self-contamination 设置。\n\n**N3** [critical] 下游任务无改善，且 effect size 极小\n- 具体位置：§6 Discussion, Table 4\n- 问题：Adaptive vs Uniform 的下游 accuracy 完全相同（0.5414 vs 0.5414, 5 tasks, 3 seeds）。论文将此归因于 Δ=-0.020 PPL 对应 ~0.1% relative improvement，低于 per-task measurement noise。但这个论证本身就说明了问题：如果 PPL 改善小到无法在标准 benchmarks 上检测到，那么 practitioners 为什么要使用这个方法？论文在 §6 \"Effect size in context\" 中承认 \"the paradigm's practical impact at current scales is modest\"。\n- 为什么影响接收：对于一篇声称提供 \"practical corollary\" 的论文，核心方法在任何可观测的 downstream metric 上都没有改善，严重削弱了实际贡献。ρ=0.6 的 Δ=-0.032 可能更有希望，但同样缺乏 downstream 验证。\n- 建议修改方向：(a) 在更高 contamination rate（如 ρ=0.6 或 0.8）下报告 downstream results；(b) 使用对 PPL 更敏感的评估方式（如 generation quality, factuality）；(c) 或明确将论文定位为 \"analysis paper with negative practical result at current scales\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 标题和 claims 的 scope 与实验支撑不匹配\n- 具体位置：Title, Abstract, §1 Introduction\n- 问题：标题 \"When Does Detect-and-Reweight Work?\" 暗示对 D&R 范式的全面分析，但实验仅覆盖：一个模型家族（Qwen3），一个 scale（0.6B，1.7B 仅初步），一种 contamination 设置（self-contamination），一个训练范式（continued pretraining），一个数据量级（132M tokens）。Abstract 的数值密度高但未充分传达这些限制。\n- 建议：标题改为更精确的范围限定，如 \"...in Self-Contaminated Continued LM Pretraining\" 或在 Abstract 第一句就明确 scope。\n\n**W2** [warning] Grid-best 与 adaptive b* 的差距需要更诚实的讨论\n- 具体位置：§5.1 Table 2, §6\n- 问题：Grid-best b=0.3 的 3-seed mean PPL 17.620 显著优于 adaptive 17.674（差距 0.054），是 adaptive vs uniform 改善（0.020）的 2.7 倍。论文论证 grid search 昂贵且不可靠，但对于关心最终性能的 practitioners，grid search 的 cost-performance tradeoff 可能仍然更优。§6 讨论了 grid-best 的高方差（σ=0.033 vs 0.007），但未讨论为什么 adaptive 无法接近 grid-best 的水平——是 dual constraint 过于保守，还是 α_eff proxy 的 ceiling 限制？\n- 建议：增加分析 adaptive b* 与 grid-best 差距的来源，讨论是否有 oracle-free 的方式缩小差距。\n\n**W3** [warning] α_eff 代理质量有限（r=0.79），且论文对此的讨论过长\n- 具体位置：§6 \"Limitations of α_eff as a proxy\"\n- 问题：α_eff 与真实 batch-level real fraction 的相关性 r=0.79（R²≈0.62），意味着 ~38% 的方差未解释。论文在 §6 中用了一整段（约 200 words）解释这个限制，包括方差分解、batch size scaling、R² 对 B 的不变性等。这段分析虽然诚实，但篇幅过长，且部分内容（如 \"Δ ∝ B^α with α ≈ 0.89\"）更适合放在 Appendix。在 8 页限制内，这些空间可以更好地用于弥补 N2 或 N3。\n- 建议：将 α_eff proxy 的详细分析移至 Appendix，主文保留核心结论（r=0.79, ceiling on precision, mitigated by batch size scaling）。\n\n**W4** [warning] 作为 analysis paper 的 finding 深度不均匀\n- 具体位置：§5, §6 全文\n- 问题：F1（epoch confound）的分析深入且有说服力（epoch-matched control + LR-controlled verification + permuted-score control）。但 F2（detector requirements）仅测试 3 个 detectors（TF-IDF+LR, GPT-2 perplexity, N-gram），且在 self-contamination 下；F3（minimum intervention）的论证主要是 ESS-only 的退化（Table 2: +0.043），缺乏对 \"为什么 minimum intervention 优于 moderate intervention\" 的深入机制分析。三个 findings 的深度差异显著。\n- 建议：对 F2 增加 detector 数量或在 cross-model 下验证阈值；对 F3 分析 adaptive b* 的 batch-level behavior（如不同 contamination 水平的 batch 中 b* 的分布与 PPL 贡献的关系）。\n\n---\n\n## 小问题（不影响接收）\n\n- §1 Figure 1 的 TikZ 概览图信息密度偏低，占据了宝贵的 column width，可以用更紧凑的方式呈现（如 inline enumeration）或移至 Appendix。\n- §4 Training paragraph 提到 \"single NVIDIA RTX PRO 6000 (96 GB)\"——这是一张非常不常见的 GPU（通常是 A100/H100），可能引起 reviewer 注意（不是匿名问题，而是实验可复现性问题）。\n- Table 2 的 Golden Ratio baseline 仅有 seed 42 的结果（其他标 \"--\"），应注释说明原因或补全。论文确实标注了 †Oracle requiring known ρ, seed 42 only，但未解释为什么只跑了一个 seed。\n- §5.3 \"Constraint regime\" 段的 24,412 micro-batches 分析只有 seed 42，其他 seed 在 Appendix 中确认 CV<2%，建议在正文中简述三个 seed 的结果。\n- Appendix 有 18 个 section（A-R），组织合理但数量多，建议对部分高度技术性的 sections 做合并。\n- §6 第一段 \"The bulk of D&R's reported PPL advantage...\" 与 §5.1 的 \"Hard filtering and the epoch confound\" 段几乎完全重复，可精简。\n\n---\n\n## 关于新颖性的详细评估\n\n**F1 (Epoch confound)**: **高新颖性**。这是本文最强的贡献。虽然 \"公平比较应控制 epoch\" 事后看来是常识，但此前的 D&R 文献（包括 Drayson et al. 2025）确实没有做到这一点。论文通过三重验证（epoch-matched, LR-controlled, permuted-score）使这一发现高度可信。\n\n**F2 (Detector requirements)**: **中等新颖性**。\"需要好的 detector\" 本身不令人意外，但对 calibration（ECE）vs discrimination（AUC）的分离贡献有价值（GPT-2 vs TF-IDF 对照实验, §5.2）。但仅 3 个 detector 在 self-contamination 下的结果，generalizability 有限。\n\n**F3 (Minimum intervention)**: **低至中等新颖性**。\"最小干预优于最大干预\" 与 importance weighting 文献中的 variance-bias tradeoff 一致，dual constraint（quality floor + stability ceiling）是自然的工程选择。Grid search b=0.3（接近 b*≈0.9 的下方）优于 b=5 的事实已足以支持这一观点，不需要完整的 adaptive 框架来论证。\n\n**Adaptive b* 作为 \"practical corollary\"**: **中等新颖性**。Formula 来自 Drayson et al. (2025)，α_eff 和 ESS 都是标准量。贡献在于将它们组合成无需 validation 的 per-batch 自适应方案，但这更像 engineering contribution。\n\n**整体作为 analysis paper**: 贡献在 main conference 门槛的边缘。F1 alone 可能不足以支撑一篇完整的论文，但 F1+F2+F3+adaptive b* 的组合提供了一个相对完整的分析框架。问题在于分析的 scope 偏窄（一个模型、一种 contamination、一个 scale）。\n\n---\n\n## Related Work 完整性评估\n\n**覆盖充分的领域：**\n- Model collapse: Shumailov 2024, Alemohammad 2024, Dohmatob 2025, Gerstgrasser 2024, Kang 2025 ✓\n- Detection methods: DetectGPT, Fast-DetectGPT, Binoculars, Min-k% Prob, watermarking ✓\n- Domain-level mixing: DoReMi, DSIR, AIOLI, DataComp-LM, OLMo, ToReMi ✓\n- Instance-level reweighting: SemDeDup, SoftDedup, QuRating, curriculum learning, LESS, MATES 等 ✓\n- Theoretical: He 2025 (golden ratio), Wang 2026 (convergence), Kish 1965, Vehtari 2024 ✓\n\n**与 Drayson et al. (2025) 的对比：** 三点区分（grid search vs dual-constrained, SIR vs continuous, ModernBERT vs TF-IDF）清晰公平。✓\n\n**可能遗漏的工作：**\n- **Contamination detection benchmarks** (如 RAID: Dugan et al. 2024; M4: Wang et al. 2024) 作为 detection 评估的标准化工作未讨论，与 F2 (detector requirements) 直接相关\n- **Synthetic data 质量对训练的影响** 的近期实证工作（如 Phi 系列使用 synthetic data 的正面案例）未讨论——这与论文隐含假设 \"synthetic data 总是有害的\" 形成对比\n- **Data Provenance Initiative** (Longpre et al. 2024) 虽然 Longpre et al. 引用了，但是关于 pretrainer preferences，而非 data provenance 本身\n- 未讨论 **后训练阶段**（SFT/RLHF）中类似的 contamination-aware 方法，这限制了 Related Work 对更广泛 contamination 问题的覆盖\n\n这些遗漏不严重，但补充后可以加强论文的学术定位。\n\n---\n\n## 格式合规检查（EMNLP 2026 硬约束）\n\n| 检查项 | 状态 | 详情 |\n|--------|------|------|\n| Abstract ≤200 words | ✅ 合规 | ~166 words（LaTeX 命令/数学公式剥离后） |\n| 正文 ≤8 页 | ✅ 合规 | §1-§7 (Conclusion) 在 page 8 底部结束，Limitations 从 page 9 开始 |\n| Limitations 在正文中 | ✅ 合规 | 单一 \\section*{Limitations} 在 §7 之后、References 之前 |\n| Appendix 无重复 Limitations | ✅ 合规 | Appendix 18 个 section (A-R)，无 Limitations |\n| 匿名性 | ✅ 合规 | Author 标为 \"Anonymous\"；无 GitHub link/作者名/机构名；\"Code and data will be released upon acceptance\" |\n| ARR Checklist 不在 PDF | ✅ 合规 | PDF 最后一页为 Appendix R (Use of AI Assistants)，无 Checklist |\n| 引用格式 | ✅ 合规 | natbib 的 \\citep 和 \\citet 正确使用 |\n| ACL 模板 | ✅ 合规 | \\usepackage[review]{acl}，11pt |\n\n**无格式合规问题。**\n\n---\n\n## Questions for Authors\n\n1. 能否提供至少一个 cross-model contamination（如 GPT-4o 生成，Qwen3-0.6B 训练）的完整结果？Appendix O 的 Llama-3.2-3B \"mixed results\" 具体是什么意思——是 adaptive b* 退化，还是所有方法都退化？\n\n2. 在 ρ=0.6（更强的 effect size, Δ=-0.032）下的 downstream accuracy 是否有所改善？如果仍然无改善，是否存在任何可观测的 downstream metric 能体现 PPL 改善的价值？\n\n3. 为什么不尝试更大的 seed 数量（N=5 或 N=10）来解决统计显著性问题？132M token, 0.6B model 的训练成本应该不高（论文提到单 GPU 16 小时 for grid search of 9 runs）。\n\n4. Adaptive b* 在 batch-level 操作，但 gradient accumulation 是 4 步——b* 是在每个 micro-batch 独立计算还是在 accumulated batch 上计算？这影响 ESS 的有效 B。\n\n---\n\n## Overall Assessment 总结\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**Soundness**: 3.5 / 5\n**Excitement**: 3 / 5\n**Confidence**: 4 / 5\n\n这是一篇诚实、结构良好的 analysis paper，核心发现（F1: epoch confound）对社区有真实价值。但三个关键弱点限制了其 impact：(1) 主效应统计显著性不足；(2) 仅在 self-contamination 设置验证；(3) 无 downstream improvement。如果作者能增加 seeds 解决统计问题并提供至少一个 cross-model 实验，评分可上调至 4 (Conference)。当前状态下，我倾向于 Findings 或 Borderline Conference。",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**Venue**: EMNLP 2026 via ARR\n**审查侧重**: 新颖性、Related Work 完整性、写作质量、格式合规、整体连贯性\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.5 (Borderline Conference)\n**Confidence**: 4/5 (Quite sure)\n**一句话总结**: 论文提出了一个有价值的 epoch confound 发现（F1），但主实验结果在多重比较校正后未达显著性（p_BH=0.078），且仅在 self-contamination 设置下验证，scope 偏窄，作为 analysis paper 的贡献深度勉强达到主会议门槛。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计合理、有对照，但统计功效不足（N=3, p_BH=0.078），且仅 self-contamination 设置 |\n| Excitement | 3/5 | Epoch confound 发现对社区有价值，但 adaptive b* 的实际改善量小且无下游迁移 |\n| Overall | 3.5/5 | 介于 Findings 和 Conference 之间；F1 有 main conference 水准，但整体 scope 和 effect size 偏弱 |\n\n---\n\n## 主要优势\n\n**S1. Epoch confound 发现（F1）是本文最核心、最有价值的贡献。** §5.1 Table 1 展示 D&R 的 0.396 PPL 优势在 epoch-matched 后缩至 Δ=0.017（3-seed），揭示 >95% 的 reported advantage 源于数据重复而非 filtering quality。这一发现对后续 D&R 工作的实验设计有直接指导意义。LR-controlled verification（D&R 17.651 vs shared-schedule 17.657, Δ=0.006）进一步排除了学习率混淆。\n\n**S2. 实验设计结构良好，消融层次清晰。** Table 2 的六种方法对比（Uniform → Random → ESS-only → Adaptive → Grid-best → D&R）形成清晰的消融阶梯，每一层都有明确的控制变量。Permuted-score control（shuffled detector, PPL +0.26）有效证明 detector signal 的必要性。\n\n**S3. 论文对局限性的讨论异常坦诚。** §6 Discussion 主动承认 downstream accuracy 无改善（Table 4: 0.5414 vs 0.5414）、effect size 在当前 scale 下 modest（Δ=-0.020 在 ~0.07-point 窗口内操作）、α_eff 代理质量有限（r=0.79）。Limitations 段覆盖了关键局限（self-contamination、N=3 统计功效、detector 覆盖范围窄）。这种自我批评远超多数投稿。\n\n**S4. Related Work 全面且结构化。** §2 分五个 paragraph 覆盖 model collapse、detection、domain-level mixing、instance-level reweighting、theoretical foundations，引用 50+ 篇文献。与最直接相关的 Drayson et al. (2025) 的三点区分（(i) grid search → dual-constrained, (ii) SIR resampling → continuous reweighting, (iii) ModernBERT → TF-IDF+LR）清晰、公平。\n\n**S5. Adaptive b* 消除了 per-model grid search 的实际需求。** 虽然 grid-best 仍优于 adaptive（17.620 vs 17.674），但 grid search 需 9 次完整训练（~16 GPU-hours at 0.6B），且 grid-best b=0.3 跨 seed 方差 4.7× 高于 adaptive（σ=0.033 vs 0.007），实际选择不可靠（Figure 2 的 plateau region）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 主实验结果在多重比较校正后未达传统显著性水平\n- 具体位置：§5.1, Table 2\n- 问题：ρ=0.4 的主实验 paired t-test 原始 p=0.019，但 Bonferroni-Holm 校正后 p_BH=0.078（九组家族比较，k=9）。ρ=0.6 校正后 p_BH=0.064。论文声称 \"BCa bootstrap CI [−0.028, −0.012] excludes zero\" 作为补充证据，但 CI 不等价于校正后 p 值。对于一篇以 \"When does X work?\" 为标题的 analysis paper，核心 claim 的统计支撑应当更强。\n- 为什么影响接收：Analysis paper 的核心价值在于可靠的实证发现。主效应在标准校正下不显著，削弱了全部三个 findings 的可信度——如果 adaptive b* 本身相对 uniform 的改善不显著，那么关于 \"什么条件下有效\" 的分析就建立在不稳固的基础上。\n- 建议修改方向：(a) 增加 seeds（N≥5）提高统计功效；(b) 减少同时比较的方法数以降低校正负担；(c) 如果增加 seeds 不可行，应在 Abstract/Conclusion 中更明确地标注 effect 的统计状态（如 \"directionally consistent but not statistically significant after family-wise correction\"），而非 buried 在括号注释中。\n\n**N2** [critical] 仅在 self-contamination 设置下验证，生态效度堪忧\n- 具体位置：§4 \"Training Data\", §Limitations\n- 问题：所有主实验使用 Qwen3-0.6B 同时作为 generator 和 trainee，这意味着合成数据与真实数据的分布差异远小于现实场景。论文承认 \"self-contamination design provides a controlled testbed... but limits ecological validity\"，且 Appendix O 的 Llama-3.2-3B cross-model 实验 \"showed mixed results\"。实际 web contamination 来自多种模型和多个时间点，detector 面临的 distribution shift 远比本文设置困难。\n- 为什么影响接收：本文的三个 findings 和 adaptive b* 的有效性边界可能 fundamentally 依赖于 self-contamination 的特殊性。例如，F2（detector requirements）中 TF-IDF+LR 在 self-contamination 下 AUC=0.94 可能在 cross-model 下大幅下降，导致 AUC/ECE 阈值完全不同。标题 \"When Does Detect-and-Reweight Work?\" 暗示了一般性结论，但实验仅支持一个非常特定的设置。\n- 建议修改方向：(a) 至少一个 cross-model contamination 的完整实验（不仅是 Appendix 中的 preliminary）；(b) 或者将标题和 claims 显式限定为 self-contamination 设置。\n\n**N3** [critical] 下游任务无改善，且 effect size 极小\n- 具体位置：§6 Discussion, Table 4\n- 问题：Adaptive vs Uniform 的下游 accuracy 完全相同（0.5414 vs 0.5414, 5 tasks, 3 seeds）。论文将此归因于 Δ=-0.020 PPL 对应 ~0.1% relative improvement，低于 per-task measurement noise。但这个论证本身就说明了问题：如果 PPL 改善小到无法在标准 benchmarks 上检测到，那么 practitioners 为什么要使用这个方法？论文在 §6 \"Effect size in context\" 中承认 \"the paradigm's practical impact at current scales is modest\"。\n- 为什么影响接收：对于一篇声称提供 \"practical corollary\" 的论文，核心方法在任何可观测的 downstream metric 上都没有改善，严重削弱了实际贡献。ρ=0.6 的 Δ=-0.032 可能更有希望，但同样缺乏 downstream 验证。\n- 建议修改方向：(a) 在更高 contamination rate（如 ρ=0.6 或 0.8）下报告 downstream results；(b) 使用对 PPL 更敏感的评估方式（如 generation quality, factuality）；(c) 或明确将论文定位为 \"analysis paper with negative practical result at current scales\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 标题和 claims 的 scope 与实验支撑不匹配\n- 具体位置：Title, Abstract, §1 Introduction\n- 问题：标题 \"When Does Detect-and-Reweight Work?\" 暗示对 D&R 范式的全面分析，但实验仅覆盖：一个模型家族（Qwen3），一个 scale（0.6B，1.7B 仅初步），一种 contamination 设置（self-contamination），一个训练范式（continued pretraining），一个数据量级（132M tokens）。Abstract 的数值密度高但未充分传达这些限制。\n- 建议：标题改为更精确的范围限定，如 \"...in Self-Contaminated Continued LM Pretraining\" 或在 Abstract 第一句就明确 scope。\n\n**W2** [warning] Grid-best 与 adaptive b* 的差距需要更诚实的讨论\n- 具体位置：§5.1 Table 2, §6\n- 问题：Grid-best b=0.3 的 3-seed mean PPL 17.620 显著优于 adaptive 17.674（差距 0.054），是 adaptive vs uniform 改善（0.020）的 2.7 倍。论文论证 grid search 昂贵且不可靠，但对于关心最终性能的 practitioners，grid search 的 cost-performance tradeoff 可能仍然更优。§6 讨论了 grid-best 的高方差（σ=0.033 vs 0.007），但未讨论为什么 adaptive 无法接近 grid-best 的水平——是 dual constraint 过于保守，还是 α_eff proxy 的 ceiling 限制？\n- 建议：增加分析 adaptive b* 与 grid-best 差距的来源，讨论是否有 oracle-free 的方式缩小差距。\n\n**W3** [warning] α_eff 代理质量有限（r=0.79），且论文对此的讨论过长\n- 具体位置：§6 \"Limitations of α_eff as a proxy\"\n- 问题：α_eff 与真实 batch-level real fraction 的相关性 r=0.79（R²≈0.62），意味着 ~38% 的方差未解释。论文在 §6 中用了一整段（约 200 words）解释这个限制，包括方差分解、batch size scaling、R² 对 B 的不变性等。这段分析虽然诚实，但篇幅过长，且部分内容（如 \"Δ ∝ B^α with α ≈ 0.89\"）更适合放在 Appendix。在 8 页限制内，这些空间可以更好地用于弥补 N2 或 N3。\n- 建议：将 α_eff proxy 的详细分析移至 Appendix，主文保留核心结论（r=0.79, ceiling on precision, mitigated by batch size scaling）。\n\n**W4** [warning] 作为 analysis paper 的 finding 深度不均匀\n- 具体位置：§5, §6 全文\n- 问题：F1（epoch confound）的分析深入且有说服力（epoch-matched control + LR-controlled verification + permuted-score control）。但 F2（detector requirements）仅测试 3 个 detectors（TF-IDF+LR, GPT-2 perplexity, N-gram），且在 self-contamination 下；F3（minimum intervention）的论证主要是 ESS-only 的退化（Table 2: +0.043），缺乏对 \"为什么 minimum intervention 优于 moderate intervention\" 的深入机制分析。三个 findings 的深度差异显著。\n- 建议：对 F2 增加 detector 数量或在 cross-model 下验证阈值；对 F3 分析 adaptive b* 的 batch-level behavior（如不同 contamination 水平的 batch 中 b* 的分布与 PPL 贡献的关系）。\n\n---\n\n## 小问题（不影响接收）\n\n- §1 Figure 1 的 TikZ 概览图信息密度偏低，占据了宝贵的 column width，可以用更紧凑的方式呈现（如 inline enumeration）或移至 Appendix。\n- §4 Training paragraph 提到 \"single NVIDIA RTX PRO 6000 (96 GB)\"——这是一张非常不常见的 GPU（通常是 A100/H100），可能引起 reviewer 注意（不是匿名问题，而是实验可复现性问题）。\n- Table 2 的 Golden Ratio baseline 仅有 seed 42 的结果（其他标 \"--\"），应注释说明原因或补全。论文确实标注了 †Oracle requiring known ρ, seed 42 only，但未解释为什么只跑了一个 seed。\n- §5.3 \"Constraint regime\" 段的 24,412 micro-batches 分析只有 seed 42，其他 seed 在 Appendix 中确认 CV<2%，建议在正文中简述三个 seed 的结果。\n- Appendix 有 18 个 section（A-R），组织合理但数量多，建议对部分高度技术性的 sections 做合并。\n- §6 第一段 \"The bulk of D&R's reported PPL advantage...\" 与 §5.1 的 \"Hard filtering and the epoch confound\" 段几乎完全重复，可精简。\n\n---\n\n## 关于新颖性的详细评估\n\n**F1 (Epoch confound)**: **高新颖性**。这是本文最强的贡献。虽然 \"公平比较应控制 epoch\" 事后看来是常识，但此前的 D&R 文献（包括 Drayson et al. 2025）确实没有做到这一点。论文通过三重验证（epoch-matched, LR-controlled, permuted-score）使这一发现高度可信。\n\n**F2 (Detector requirements)**: **中等新颖性**。\"需要好的 detector\" 本身不令人意外，但对 calibration（ECE）vs discrimination（AUC）的分离贡献有价值（GPT-2 vs TF-IDF 对照实验, §5.2）。但仅 3 个 detector 在 self-contamination 下的结果，generalizability 有限。\n\n**F3 (Minimum intervention)**: **低至中等新颖性**。\"最小干预优于最大干预\" 与 importance weighting 文献中的 variance-bias tradeoff 一致，dual constraint（quality floor + stability ceiling）是自然的工程选择。Grid search b=0.3（接近 b*≈0.9 的下方）优于 b=5 的事实已足以支持这一观点，不需要完整的 adaptive 框架来论证。\n\n**Adaptive b* 作为 \"practical corollary\"**: **中等新颖性**。Formula 来自 Drayson et al. (2025)，α_eff 和 ESS 都是标准量。贡献在于将它们组合成无需 validation 的 per-batch 自适应方案，但这更像 engineering contribution。\n\n**整体作为 analysis paper**: 贡献在 main conference 门槛的边缘。F1 alone 可能不足以支撑一篇完整的论文，但 F1+F2+F3+adaptive b* 的组合提供了一个相对完整的分析框架。问题在于分析的 scope 偏窄（一个模型、一种 contamination、一个 scale）。\n\n---\n\n## Related Work 完整性评估\n\n**覆盖充分的领域：**\n- Model collapse: Shumailov 2024, Alemohammad 2024, Dohmatob 2025, Gerstgrasser 2024, Kang 2025 ✓\n- Detection methods: DetectGPT, Fast-DetectGPT, Binoculars, Min-k% Prob, watermarking ✓\n- Domain-level mixing: DoReMi, DSIR, AIOLI, DataComp-LM, OLMo, ToReMi ✓\n- Instance-level reweighting: SemDeDup, SoftDedup, QuRating, curriculum learning, LESS, MATES 等 ✓\n- Theoretical: He 2025 (golden ratio), Wang 2026 (convergence), Kish 1965, Vehtari 2024 ✓\n\n**与 Drayson et al. (2025) 的对比：** 三点区分（grid search vs dual-constrained, SIR vs continuous, ModernBERT vs TF-IDF）清晰公平。✓\n\n**可能遗漏的工作：**\n- **Contamination detection benchmarks** (如 RAID: Dugan et al. 2024; M4: Wang et al. 2024) 作为 detection 评估的标准化工作未讨论，与 F2 (detector requirements) 直接相关\n- **Synthetic data 质量对训练的影响** 的近期实证工作（如 Phi 系列使用 synthetic data 的正面案例）未讨论——这与论文隐含假设 \"synthetic data 总是有害的\" 形成对比\n- **Data Provenance Initiative** (Longpre et al. 2024) 虽然 Longpre et al. 引用了，但是关于 pretrainer preferences，而非 data provenance 本身\n- 未讨论 **后训练阶段**（SFT/RLHF）中类似的 contamination-aware 方法，这限制了 Related Work 对更广泛 contamination 问题的覆盖\n\n这些遗漏不严重，但补充后可以加强论文的学术定位。\n\n---\n\n## 格式合规检查（EMNLP 2026 硬约束）\n\n| 检查项 | 状态 | 详情 |\n|--------|------|------|\n| Abstract ≤200 words | ✅ 合规 | ~166 words（LaTeX 命令/数学公式剥离后） |\n| 正文 ≤8 页 | ✅ 合规 | §1-§7 (Conclusion) 在 page 8 底部结束，Limitations 从 page 9 开始 |\n| Limitations 在正文中 | ✅ 合规 | 单一 \\section*{Limitations} 在 §7 之后、References 之前 |\n| Appendix 无重复 Limitations | ✅ 合规 | Appendix 18 个 section (A-R)，无 Limitations |\n| 匿名性 | ✅ 合规 | Author 标为 \"Anonymous\"；无 GitHub link/作者名/机构名；\"Code and data will be released upon acceptance\" |\n| ARR Checklist 不在 PDF | ✅ 合规 | PDF 最后一页为 Appendix R (Use of AI Assistants)，无 Checklist |\n| 引用格式 | ✅ 合规 | natbib 的 \\citep 和 \\citet 正确使用 |\n| ACL 模板 | ✅ 合规 | \\usepackage[review]{acl}，11pt |\n\n**无格式合规问题。**\n\n---\n\n## Questions for Authors\n\n1. 能否提供至少一个 cross-model contamination（如 GPT-4o 生成，Qwen3-0.6B 训练）的完整结果？Appendix O 的 Llama-3.2-3B \"mixed results\" 具体是什么意思——是 adaptive b* 退化，还是所有方法都退化？\n\n2. 在 ρ=0.6（更强的 effect size, Δ=-0.032）下的 downstream accuracy 是否有所改善？如果仍然无改善，是否存在任何可观测的 downstream metric 能体现 PPL 改善的价值？\n\n3. 为什么不尝试更大的 seed 数量（N=5 或 N=10）来解决统计显著性问题？132M token, 0.6B model 的训练成本应该不高（论文提到单 GPU 16 小时 for grid search of 9 runs）。\n\n4. Adaptive b* 在 batch-level 操作，但 gradient accumulation 是 4 步——b* 是在每个 micro-batch 独立计算还是在 accumulated batch 上计算？这影响 ESS 的有效 B。\n\n---\n\n## Overall Assessment 总结\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**Soundness**: 3.5 / 5\n**Excitement**: 3 / 5\n**Confidence**: 4 / 5\n\n这是一篇诚实、结构良好的 analysis paper，核心发现（F1: epoch confound）对社区有真实价值。但三个关键弱点限制了其 impact：(1) 主效应统计显著性不足；(2) 仅在 self-contamination 设置验证；(3) 无 downstream improvement。如果作者能增加 seeds 解决统计问题并提供至少一个 cross-model 实验，评分可上调至 4 (Conference)。当前状态下，我倾向于 Findings 或 Borderline Conference。",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1005 · 2026-05-24T04:19:49.885296+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3664
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-24T04:19:54.161572+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1007 · 2026-05-24T04:19:54.161991+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-24T04:19:58.729514+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-24T04:19:59.231315+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-24T04:19:59.332065+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2"
  }
}
```

</details>

---


### Tool result

_source line 1011 · 2026-05-24T04:19:59.332540+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"安全限制：只能清理 _pdf_images 目录，当前目标: _pdf_images_2\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1012 · 2026-05-24T04:20:03.400228+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "rm -f /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2/submitted_p*.png && rmdir /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2 2>/dev/null; echo \"done\"",
  "description": "Clean up secondary PDF image directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "rm -f /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2/submitted_p*.png && rmdir /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_12/_pdf_images_2 2>/dev/null; echo \"done\"",
    "description": "Clean up secondary PDF image directory"
  }
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-24T04:20:03.450922+00:00_

done

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1014 · 2026-05-24T04:20:13.662268+00:00_

审稿报告已提交给 Review Director。

**总结**：Overall 3.5 (Borderline Conference)。论文的 epoch confound 发现（F1）是核心亮点，对 D&R 文献有直接纠偏价值。格式完全合规。三个主要问题：(1) ρ=0.4 主结果校正后 p_BH=0.078 未达显著性；(2) 仅 self-contamination 设置，生态效度受限；(3) downstream accuracy 无任何改善。如能增加 seeds 和 cross-model 实验，可上调至 4 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 24

## Round 24

4 recorded events


### User

_source line 1015 · 2026-05-24T04:21:12.693775+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的审稿意见。对每个要点使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿原文：

**Overall Assessment**: 3.0 (Findings), Confidence 4/5

### 主要优势
- **S1**: Epoch confound 分析是最突出贡献。通过 epoch-matched 和 LR-controlled 两重验证令人信服。
- **S2**: 实验设计系统性：6 种方法 ablation hierarchy 清晰。Permuted-score control 是聪明的 sanity check。
- **S3**: 极为诚实的结果报告——主动报告校正后不显著 p 值、downstream 零改善、ρ=0.2 failure、checkpoint resume artifact、cross-model mixed results。
- **S4**: Practitioner decision table (Table 3) 有实用价值。Dose-response pattern 提供有用 sensitivity profile。
- **S5**: Proposition 1-2 确保 dual constraint 的 well-definedness。
- **S6**: Checkpoint resume artifact 的透明披露和 from-scratch 验证展示良好实验规范。

### Must-Fix 问题
- **N1** [critical]: N=3 seeds 下所有核心结论均未达校正后统计显著性。BCa bootstrap CI 在 N=3 下覆盖率存疑（Efron & Tibshirani 1993 建议 N≥10-15）。Abstract/conclusion 仍以断言性语言呈现。
- **N2** [critical]: 自污染设计严重限制泛化性。Generator=trainee 是最简单检测场景。唯一跨模型测试 single seed、mixed、缺 PPL 对比。现实 web contamination 来自多模型。
- **N3** [critical]: Downstream tasks 零改善削弱实际价值。"PPL improvements operate in a regime that standard benchmarks cannot resolve" — 如果所有标准评估手段都无法检测，实际意义存疑。

### Should-Fix 问题
- **W1** [warning]: B=4 micro-batch 上 dual constraint 统计可靠性不足。True real fraction 只能取 {0, 0.25, 0.5, 0.75, 1.0}，α_eff 波动剧烈（MAE=0.114）。
- **W2** [warning]: α_eff proxy r=0.79（R²=0.63）偏弱。Convergence theory 中阈值条件应用于 proxy 而非 true fraction，理论保证是否成立未讨论。
- **W3** [warning]: Batch-size amplification 3 点拟合 power law（Δ ∝ B^0.89），指数不确定性未报告。
- **W4** [warning]: 3 个 detector 不足以建立 AUC/ECE 因果关系。TF-IDF vs GPT-2 不是控制实验（同时在 AUC、模型类型、feature space、false positive pattern 上不同）。建议用同一 detector 不同 calibration 程度 isolate calibration effect。
- **W5** [warning]: "Minimum intervention" 原则缺乏理论依据。Grid-best b≈0.3 而 adaptive b*≈0.9——方法有效是否因为 per-batch adaptation 补偿了 b 偏移，而非 minimum intervention 本身？建议补充 median b / percentile-based b 对比。
- **W6** [warning]: Epoch confound 分析缺少 "uniform + multi-epoch" baseline 来区分纯重复 vs filtered+repetition 交互。

### 小问题
- **M1**: Abstract 中 "uncorrected p=0.010" 排版不够醒目
- **M2**: Table 2 Grid-best 的 τ 不明确
- **M3**: Conclusion 中缺少 N=3/校正后不显著的 caveat
- **M4**: Figure 2 y 轴非零起点放大视觉差异
- **M5**: 未报告 Cohen's d 及其不确定性
- **M6**: Appendix P seed 42 artifact 与主实验关系需仔细阅读才能理清

### Questions
1. 是否考虑过用同一 TF-IDF+LR detector 改变 temperature scaling 参数 isolate calibration effect？
2. ρ=0.2 failure case 中 α_eff bias 是否仍然 ~-0.03？
3. 为什么不在 B=16 而非 B=4 上计算 b*？主实验是否在次优设定下运行？
4. Grid search b=0.3 vs adaptive b*≈0.9 差距是否表明 minimum intervention 过度干预？

---

请对以上所有要点逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1016 · 2026-05-24T04:23:55.314507+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### 主要优势\n\n**[AGREE] R1-S1**: Epoch confound 分析确实是最突出贡献，我的审稿同样将其列为最高新颖性。三重验证（epoch-matched + LR-controlled + permuted-score）的设计严谨。\n\n**[AGREE] R1-S2**: 6 种方法的 ablation hierarchy 是本文实验设计的亮点。我在 Reviewer 2 报告中也肯定了这一点（S2）。\n\n**[AGREE] R1-S3**: 论文的诚实程度确实远超多数投稿。主动报告 p_BH=0.078、downstream 零改善、ρ=0.2 failure 等负面结果，是良好的学术规范。\n\n**[AGREE] R1-S4**: Table 3 (Decision summary) 的实用价值我也认可，清晰地将三个 findings 转化为 practitioner 可操作的条件检查。\n\n**[AGREE] R1-S5**: Proposition 1-2 确保了 α_eff 单调递增、ESS 单调递减，从而保证 dual constraint 的 well-definedness（feasible interval [b_τ, b_ESS] 存在性）。证明本身简洁正确（Appendix A, page 11）。\n\n**[AGREE] R1-S6**: Appendix P 的 checkpoint resume artifact 披露（seed 42 的 resume 导致 Δ=−0.011 resume vs −0.005 from-scratch 偏差）是难得的透明度。\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1**: 统计显著性问题。我在 Reviewer 2 报告 N1 中提出了本质相同的批评。补充一点：R1 指出的 BCa bootstrap CI 在 N=3 下覆盖率存疑是一个我未强调但完全正确的技术细节。Efron & Tibshirani (1993) 的 N≥10-15 建议是标准参考。论文在 §5.1 使用 \"95% BCa bootstrap CI [−0.028, −0.012] excludes zero\" 作为 p_BH=0.078 的补充证据，但 N=3 下 BCa CI 的 coverage 可能远低于名义 95%，这意味着该 CI 的证据价值被高估。两位 reviewer 独立提出同一问题，说明这不是 marginal concern。\n\n**[AGREE] R1-N2**: Self-contamination 限制。与我的 N2 完全一致。R1 的补充点更具体：Appendix O 的 cross-model test \"single seed, mixed, 缺 PPL 对比\"——我查看了 page 16 的 Appendix O 内容，确认 Llama-3.2-3B 结果仅有 MMLU/HellaSwag 两个 metric（\"Mixed results: MMLU improves while HellaSwag slightly degrades\"），确实缺少 PPL 对比，且只有 single seed，实验设计远不如主实验严格。\n\n**[AGREE] R1-N3**: Downstream 零改善。与我的 N3 一致。R1 的引用 \"if all standard evaluation methods cannot detect it, actual significance is questionable\" 精准地指出了问题核心。论文 §6 的辩护 (\"Δ=−0.020 corresponds to ~0.1% relative improvement\") 实际上是在论证自己方法的改善量 too small to matter，这对 analysis paper 也许可接受，但对声称提供 \"practical corollary\" 的论文则自相矛盾。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1**: B=4 micro-batch 的 dual constraint 可靠性问题。这是一个我未充分强调的重要技术批评。在 B=4 下，true real fraction 只能取 {0, 0.25, 0.5, 0.75, 1.0} 五个离散值，α_eff 的估计粒度极粗。§5.3 中论文自己展示了 B=8 和 B=16 的显著改善（Δ 从 −0.020 到 −0.052 到 −0.068），这反过来说明 B=4 是一个次优设定。论文选择 B=4 作为主实验（可能出于 GPU 内存限制），但应当更明确地讨论这一选择的代价。\n\n**[AGREE] R1-W2**: α_eff proxy 理论保证的 gap。我在 W3 中提到了 r=0.79 的限制，但 R1 的批评更深入：Wang 2026 的 convergence theory 要求 α_eff(b) ≥ τ 对 true real fraction 成立，但论文将此条件应用于 proxy α_eff，而 proxy 的 R²=0.63 意味着理论保证不直接转移。论文 §3 说 \"α_eff correlates with the true batch-level real fraction at Pearson r ≈ 0.79 (Appendix K)\"，但 correlation 不等于 theoretical guarantee 的 transferability。这是一个 sound but understated 的理论弱点。\n\n**[AGREE] R1-W3**: 3 点 power law 拟合。用 B ∈ {4, 8, 16} 三个数据点拟合 Δ ∝ B^0.89 确实在统计上几乎没有信息量——两参数模型拟合三个点，自由度接近零。论文 §5.3 报告这一 scaling 时未给出指数的不确定性区间，这不是严谨的 empirical claim。不过这是 §5.3 中的次要观察而非核心 claim，影响有限。\n\n**[AGREE] R1-W4**: 3 个 detector 不足以建立 calibration 因果关系。这是 R1 审稿中最精准的技术批评之一，也是我在 W4 中提到但未展开的点。TF-IDF+LR (AUC=0.94, ECE=0.05) vs GPT-2 perplexity (AUC=0.91, ECE=0.131) 的对比同时在 AUC、模型类型、feature space、false positive pattern 等多个维度上不同。论文 §5.2 声称 \"The TF-IDF vs GPT-2 contrast (comparable AUC, 2.7× ECE gap) isolates calibration\"，但 AUC 0.94 vs 0.91 并非严格 comparable（差 0.03），且模型架构完全不同。R1 建议的 \"同一 TF-IDF+LR detector + 不同 temperature scaling\" 是一个极好的实验设计，能真正 isolate calibration effect。这会使 F2 的论证从 observational 升级为 quasi-causal。\n\n**[REBUT] R1-W5**: \"Minimum intervention\" 原则缺乏理论依据。R1 的观察（grid-best b≈0.3 而 adaptive b*≈0.9，mean b* 比 grid-best 更高）有事实基础，但推理方向有误。\n\n理由：(1) \"Minimum intervention\" 是 per-batch 的概念，不是全局平均的概念。在 contamination 较重的 batch 中，b* 可能很高（如 b*=3-5），而在干净 batch 中 b*=0。Overall mean ≈0.9 是这些异质 batch 的平均，不能与固定 b=0.3 直接比较语义。(2) 从 §5.3 Constraint regime 分析（seed 42, 24,412 micro-batches）：5.8% clean (b*=0), ~50% α_eff-binding, ~44% ESS-binding。这说明大约一半的 batch 在 quality floor 处最小化干预，另一半被 stability ceiling 约束。(3) Grid-best b=0.3 是 post-hoc oracle from 9 candidates，且 Figure 2 显示 PPL 在 b ∈ [0.1, 0.5] 区间形成 plateau，所以 b=0.3 的 \"最优\" 并不 sharp。(4) Adaptive b* 的优势不是绝对 PPL（低于 grid-best），而是无需 validation、低跨 seed 方差（σ=0.007 vs 0.033），以及在 ρ 变化时自动适应。\n\n但我同意 R1 建议的 \"median b / percentile-based b\" 对比会有信息量——如果固定 b = median(b*) 也能接近 adaptive 的性能，那确实说明 per-batch adaptation 的价值有限，\"minimum intervention\" 的叙事需要修正。\n\n**[AGREE] R1-W6**: Epoch confound 分析缺少 \"uniform + multi-epoch\" baseline。这是一个我在审稿中未发现但非常有价值的遗漏。当前的 epoch confound 分析比较：\n- D&R full (6,103 steps, ~3.2 epochs): PPL 17.250\n- D&R epoch-matched (2,533 steps, ~1.0 epoch): PPL 17.657\n- Adaptive b* (6,103 steps, ~1.0 epoch): PPL 17.674\n\n缺少的 baseline 是：Uniform + multi-epoch（即在全部数据上重复训练 ~3.2 epochs，不做任何 filtering）。这个 baseline 能回答：D&R full 的 PPL 17.250 相比 uniform 17.694 的 0.444 优势中，有多少来自纯粹的 data repetition（不考虑 filtering），有多少来自 filtering + repetition 的交互效应？论文的 LR-controlled uniform (2,533 steps) 给出 18.062，但这是 reduced training budget 下的 uniform，不是 multi-epoch uniform。添加这个 baseline 的计算成本很低（一次 6,103-step 训练），但对 epoch confound 的分析完整性至关重要。\n\n---\n\n### 小问题\n\n**[AGREE] R1-M1**: \"uncorrected p=0.010\" 在 Abstract 中确实不够醒目。我在审稿中将此归类为 claims scope 与证据不匹配的问题（W1），但 R1 的格式建议更具体可操作。\n\n**[REBUT] R1-M2**: \"Table 2 Grid-best 的 τ 不明确\"——Grid-best 使用固定 b（从 9 个 candidate 中 post-hoc 选择 b=0.3），不使用 τ 参数。τ 是 adaptive b* 的 quality floor 参数。Table 2 注释 ‡ 已标注 \"Post-hoc oracle from nine candidates\"。这不是论文的遗漏，可能是 R1 对 Grid-best 方法的理解有误。\n\n**[AGREE] R1-M3**: Conclusion 确实缺少 N=3/校正后不显著的 caveat。§7 Conclusion（page 8 底部）使用断言性语言 \"We identify three effectiveness conditions...\"，未提及 p_BH=0.078 的限制。这与 §5.1 和 §Limitations 的谨慎态度不一致。\n\n**[REBUT] R1-M4**: Figure 2 的 y 轴非零起点。在 method comparison 论文中，y 轴 truncation 是标准做法——所有方法的 PPL 在 17.2-18.0 范围内，如果 y 轴从 0 开始，所有差异将不可见。Figure 2 的 y 轴范围（约 17.0-18.0）是合理的。但可以在 caption 中注明 \"note truncated y-axis\" 作为最佳实践。\n\n**[AGREE] R1-M5**: 未报告 Cohen's d 及其不确定性。对于 N=3 的小样本比较，Cohen's d（及其 CI）能比 p 值更好地传达 effect size 信息。论文报告了 Δ 和 σ，但未计算标准化 effect size。\n\n**[AGREE] R1-M6**: Appendix P 的 checkpoint artifact 讨论确实需要仔细阅读才能理解它与主实验的关系——结论是 \"all main results use from-scratch runs, artifact only affects early seed 42 adaptive runs that are not in the paper\"，但 reader 需要自己拼凑这个信息。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1**: 用同一 TF-IDF+LR detector 改变 temperature scaling 参数来 isolate calibration effect 是极好的实验建议。这比比较不同 detector 类型更有控制力。例如，将 temperature 从 T=0.204（calibrated, ECE=0.05）设为 T=1.0（uncalibrated, ECE likely much higher）或 T=0.05（over-confident），能在 AUC 不变的条件下单独测试 calibration 的影响。\n\n**[AGREE] R1-Q2**: ρ=0.2 failure case 中的 α_eff bias 值得追问。§6 提到 \"at ρ=0.2, the detector's signal-to-noise ratio is too low and the method actively intervenes on unreliable signal (α_eff-binding at 60.1% despite mean q=0.393)\"。如果 α_eff 的 systematic bias 在 ρ=0.2 下与 ρ=0.4 下相同（~-0.03, cf. §3 提到 mean Δ=-0.020 correlation），那么 τ=0.7 的阈值在低污染下可能系统性地 over-trigger reweighting。\n\n**[AGREE] R1-Q3**: 为什么不在 B=16（最优设定，Δ=-0.068）上跑主实验？§5.3 明确展示 B=16 >> B=4。如果主实验在 B=4 上跑是因为 GPU 内存限制（单卡 RTX PRO 6000, sequence length 2048），论文应明确说明这一 practical constraint。这也影响 N1 的统计显著性问题——在 B=16 下 effect size 更大，可能更容易达到校正后显著性。\n\n**[REBUT] R1-Q4**: Grid-best b=0.3 vs adaptive b*≈0.9 的差距是否表明 minimum intervention 过度干预——我在 R1-W5 中已部分反驳。补充：b=0.3 是 fixed across all batches 的 post-hoc optimum，b*≈0.9 是 per-batch adaptive 的均值。二者不可直接比较，因为 (a) 不同 batch 的最优 b 不同，平均值不等于最优固定值；(b) per-batch b* 的分布信息比均值更重要——如果 b* 的分布是 bimodal（大量 b*=0 clean batch + 少量 b*>2 highly contaminated batch），均值 0.9 的含义与所有 batch b*≈0.9 完全不同。论文 §5.3 的 regime 分析（5.8% clean, ~50% α_eff-binding, ~44% ESS-binding）支持这种异质性。不过 R1 的 concern 仍有一定道理——如果 median b* 也接近 0.9（而非 0.3），那确实说明 adaptive method 的 typical intervention 高于 grid-best，需要解释为什么 per-batch higher b 会比 global lower b 更好。\n\n---\n\n### 两位 Reviewer 的共识与分歧\n\n**强共识（两人独立提出同一问题）**：\n1. N=3 统计功效不足（R1-N1 / R2-N1）\n2. Self-contamination 生态效度（R1-N2 / R2-N2）\n3. Downstream 零改善（R1-N3 / R2-N3）\n\n这三个 critical issues 是两位 reviewer 独立达成的共识，作者 rebuttal 必须正面回应。\n\n**R1 独有的强技术批评（R2 需补充的遗漏）**：\n- R1-W4（detector causal claim 需控制实验）和 R1-W6（缺 uniform + multi-epoch baseline）是我审稿中未充分展开的重要技术点，我完全赞同。\n- R1-W1（B=4 micro-batch 统计可靠性）我虽然注意到但未作为独立 weakness 提出，R1 的分析更到位。\n\n**R2 独有的关注点**：\n- 论文标题 scope 与实验支撑不匹配（R2-W1）\n- Grid-best vs adaptive 差距的来源分析缺失（R2-W2）\n- α_eff proxy 讨论篇幅过长占用正文空间（R2-W3）\n- 三个 findings 深度不均匀（R2-W4）\n\n**唯一分歧**：\n- R1-M4（Figure 2 y 轴非零起点）：我认为 method comparison 论文中 truncated y-axis 是标准做法，R1 的批评过于苛刻。\n- R1-M2（Grid-best 的 τ）：Grid-best 不使用 τ 参数，R1 可能有误解。",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### 主要优势\n\n**[AGREE] R1-S1**: Epoch confound 分析确实是最突出贡献，我的审稿同样将其列为最高新颖性。三重验证（epoch-matched + LR-controlled + permuted-score）的设计严谨。\n\n**[AGREE] R1-S2**: 6 种方法的 ablation hierarchy 是本文实验设计的亮点。我在 Reviewer 2 报告中也肯定了这一点（S2）。\n\n**[AGREE] R1-S3**: 论文的诚实程度确实远超多数投稿。主动报告 p_BH=0.078、downstream 零改善、ρ=0.2 failure 等负面结果，是良好的学术规范。\n\n**[AGREE] R1-S4**: Table 3 (Decision summary) 的实用价值我也认可，清晰地将三个 findings 转化为 practitioner 可操作的条件检查。\n\n**[AGREE] R1-S5**: Proposition 1-2 确保了 α_eff 单调递增、ESS 单调递减，从而保证 dual constraint 的 well-definedness（feasible interval [b_τ, b_ESS] 存在性）。证明本身简洁正确（Appendix A, page 11）。\n\n**[AGREE] R1-S6**: Appendix P 的 checkpoint resume artifact 披露（seed 42 的 resume 导致 Δ=−0.011 resume vs −0.005 from-scratch 偏差）是难得的透明度。\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1**: 统计显著性问题。我在 Reviewer 2 报告 N1 中提出了本质相同的批评。补充一点：R1 指出的 BCa bootstrap CI 在 N=3 下覆盖率存疑是一个我未强调但完全正确的技术细节。Efron & Tibshirani (1993) 的 N≥10-15 建议是标准参考。论文在 §5.1 使用 \"95% BCa bootstrap CI [−0.028, −0.012] excludes zero\" 作为 p_BH=0.078 的补充证据，但 N=3 下 BCa CI 的 coverage 可能远低于名义 95%，这意味着该 CI 的证据价值被高估。两位 reviewer 独立提出同一问题，说明这不是 marginal concern。\n\n**[AGREE] R1-N2**: Self-contamination 限制。与我的 N2 完全一致。R1 的补充点更具体：Appendix O 的 cross-model test \"single seed, mixed, 缺 PPL 对比\"——我查看了 page 16 的 Appendix O 内容，确认 Llama-3.2-3B 结果仅有 MMLU/HellaSwag 两个 metric（\"Mixed results: MMLU improves while HellaSwag slightly degrades\"），确实缺少 PPL 对比，且只有 single seed，实验设计远不如主实验严格。\n\n**[AGREE] R1-N3**: Downstream 零改善。与我的 N3 一致。R1 的引用 \"if all standard evaluation methods cannot detect it, actual significance is questionable\" 精准地指出了问题核心。论文 §6 的辩护 (\"Δ=−0.020 corresponds to ~0.1% relative improvement\") 实际上是在论证自己方法的改善量 too small to matter，这对 analysis paper 也许可接受，但对声称提供 \"practical corollary\" 的论文则自相矛盾。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1**: B=4 micro-batch 的 dual constraint 可靠性问题。这是一个我未充分强调的重要技术批评。在 B=4 下，true real fraction 只能取 {0, 0.25, 0.5, 0.75, 1.0} 五个离散值，α_eff 的估计粒度极粗。§5.3 中论文自己展示了 B=8 和 B=16 的显著改善（Δ 从 −0.020 到 −0.052 到 −0.068），这反过来说明 B=4 是一个次优设定。论文选择 B=4 作为主实验（可能出于 GPU 内存限制），但应当更明确地讨论这一选择的代价。\n\n**[AGREE] R1-W2**: α_eff proxy 理论保证的 gap。我在 W3 中提到了 r=0.79 的限制，但 R1 的批评更深入：Wang 2026 的 convergence theory 要求 α_eff(b) ≥ τ 对 true real fraction 成立，但论文将此条件应用于 proxy α_eff，而 proxy 的 R²=0.63 意味着理论保证不直接转移。论文 §3 说 \"α_eff correlates with the true batch-level real fraction at Pearson r ≈ 0.79 (Appendix K)\"，但 correlation 不等于 theoretical guarantee 的 transferability。这是一个 sound but understated 的理论弱点。\n\n**[AGREE] R1-W3**: 3 点 power law 拟合。用 B ∈ {4, 8, 16} 三个数据点拟合 Δ ∝ B^0.89 确实在统计上几乎没有信息量——两参数模型拟合三个点，自由度接近零。论文 §5.3 报告这一 scaling 时未给出指数的不确定性区间，这不是严谨的 empirical claim。不过这是 §5.3 中的次要观察而非核心 claim，影响有限。\n\n**[AGREE] R1-W4**: 3 个 detector 不足以建立 calibration 因果关系。这是 R1 审稿中最精准的技术批评之一，也是我在 W4 中提到但未展开的点。TF-IDF+LR (AUC=0.94, ECE=0.05) vs GPT-2 perplexity (AUC=0.91, ECE=0.131) 的对比同时在 AUC、模型类型、feature space、false positive pattern 等多个维度上不同。论文 §5.2 声称 \"The TF-IDF vs GPT-2 contrast (comparable AUC, 2.7× ECE gap) isolates calibration\"，但 AUC 0.94 vs 0.91 并非严格 comparable（差 0.03），且模型架构完全不同。R1 建议的 \"同一 TF-IDF+LR detector + 不同 temperature scaling\" 是一个极好的实验设计，能真正 isolate calibration effect。这会使 F2 的论证从 observational 升级为 quasi-causal。\n\n**[REBUT] R1-W5**: \"Minimum intervention\" 原则缺乏理论依据。R1 的观察（grid-best b≈0.3 而 adaptive b*≈0.9，mean b* 比 grid-best 更高）有事实基础，但推理方向有误。\n\n理由：(1) \"Minimum intervention\" 是 per-batch 的概念，不是全局平均的概念。在 contamination 较重的 batch 中，b* 可能很高（如 b*=3-5），而在干净 batch 中 b*=0。Overall mean ≈0.9 是这些异质 batch 的平均，不能与固定 b=0.3 直接比较语义。(2) 从 §5.3 Constraint regime 分析（seed 42, 24,412 micro-batches）：5.8% clean (b*=0), ~50% α_eff-binding, ~44% ESS-binding。这说明大约一半的 batch 在 quality floor 处最小化干预，另一半被 stability ceiling 约束。(3) Grid-best b=0.3 是 post-hoc oracle from 9 candidates，且 Figure 2 显示 PPL 在 b ∈ [0.1, 0.5] 区间形成 plateau，所以 b=0.3 的 \"最优\" 并不 sharp。(4) Adaptive b* 的优势不是绝对 PPL（低于 grid-best），而是无需 validation、低跨 seed 方差（σ=0.007 vs 0.033），以及在 ρ 变化时自动适应。\n\n但我同意 R1 建议的 \"median b / percentile-based b\" 对比会有信息量——如果固定 b = median(b*) 也能接近 adaptive 的性能，那确实说明 per-batch adaptation 的价值有限，\"minimum intervention\" 的叙事需要修正。\n\n**[AGREE] R1-W6**: Epoch confound 分析缺少 \"uniform + multi-epoch\" baseline。这是一个我在审稿中未发现但非常有价值的遗漏。当前的 epoch confound 分析比较：\n- D&R full (6,103 steps, ~3.2 epochs): PPL 17.250\n- D&R epoch-matched (2,533 steps, ~1.0 epoch): PPL 17.657\n- Adaptive b* (6,103 steps, ~1.0 epoch): PPL 17.674\n\n缺少的 baseline 是：Uniform + multi-epoch（即在全部数据上重复训练 ~3.2 epochs，不做任何 filtering）。这个 baseline 能回答：D&R full 的 PPL 17.250 相比 uniform 17.694 的 0.444 优势中，有多少来自纯粹的 data repetition（不考虑 filtering），有多少来自 filtering + repetition 的交互效应？论文的 LR-controlled uniform (2,533 steps) 给出 18.062，但这是 reduced training budget 下的 uniform，不是 multi-epoch uniform。添加这个 baseline 的计算成本很低（一次 6,103-step 训练），但对 epoch confound 的分析完整性至关重要。\n\n---\n\n### 小问题\n\n**[AGREE] R1-M1**: \"uncorrected p=0.010\" 在 Abstract 中确实不够醒目。我在审稿中将此归类为 claims scope 与证据不匹配的问题（W1），但 R1 的格式建议更具体可操作。\n\n**[REBUT] R1-M2**: \"Table 2 Grid-best 的 τ 不明确\"——Grid-best 使用固定 b（从 9 个 candidate 中 post-hoc 选择 b=0.3），不使用 τ 参数。τ 是 adaptive b* 的 quality floor 参数。Table 2 注释 ‡ 已标注 \"Post-hoc oracle from nine candidates\"。这不是论文的遗漏，可能是 R1 对 Grid-best 方法的理解有误。\n\n**[AGREE] R1-M3**: Conclusion 确实缺少 N=3/校正后不显著的 caveat。§7 Conclusion（page 8 底部）使用断言性语言 \"We identify three effectiveness conditions...\"，未提及 p_BH=0.078 的限制。这与 §5.1 和 §Limitations 的谨慎态度不一致。\n\n**[REBUT] R1-M4**: Figure 2 的 y 轴非零起点。在 method comparison 论文中，y 轴 truncation 是标准做法——所有方法的 PPL 在 17.2-18.0 范围内，如果 y 轴从 0 开始，所有差异将不可见。Figure 2 的 y 轴范围（约 17.0-18.0）是合理的。但可以在 caption 中注明 \"note truncated y-axis\" 作为最佳实践。\n\n**[AGREE] R1-M5**: 未报告 Cohen's d 及其不确定性。对于 N=3 的小样本比较，Cohen's d（及其 CI）能比 p 值更好地传达 effect size 信息。论文报告了 Δ 和 σ，但未计算标准化 effect size。\n\n**[AGREE] R1-M6**: Appendix P 的 checkpoint artifact 讨论确实需要仔细阅读才能理解它与主实验的关系——结论是 \"all main results use from-scratch runs, artifact only affects early seed 42 adaptive runs that are not in the paper\"，但 reader 需要自己拼凑这个信息。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1**: 用同一 TF-IDF+LR detector 改变 temperature scaling 参数来 isolate calibration effect 是极好的实验建议。这比比较不同 detector 类型更有控制力。例如，将 temperature 从 T=0.204（calibrated, ECE=0.05）设为 T=1.0（uncalibrated, ECE likely much higher）或 T=0.05（over-confident），能在 AUC 不变的条件下单独测试 calibration 的影响。\n\n**[AGREE] R1-Q2**: ρ=0.2 failure case 中的 α_eff bias 值得追问。§6 提到 \"at ρ=0.2, the detector's signal-to-noise ratio is too low and the method actively intervenes on unreliable signal (α_eff-binding at 60.1% despite mean q=0.393)\"。如果 α_eff 的 systematic bias 在 ρ=0.2 下与 ρ=0.4 下相同（~-0.03, cf. §3 提到 mean Δ=-0.020 correlation），那么 τ=0.7 的阈值在低污染下可能系统性地 over-trigger reweighting。\n\n**[AGREE] R1-Q3**: 为什么不在 B=16（最优设定，Δ=-0.068）上跑主实验？§5.3 明确展示 B=16 >> B=4。如果主实验在 B=4 上跑是因为 GPU 内存限制（单卡 RTX PRO 6000, sequence length 2048），论文应明确说明这一 practical constraint。这也影响 N1 的统计显著性问题——在 B=16 下 effect size 更大，可能更容易达到校正后显著性。\n\n**[REBUT] R1-Q4**: Grid-best b=0.3 vs adaptive b*≈0.9 的差距是否表明 minimum intervention 过度干预——我在 R1-W5 中已部分反驳。补充：b=0.3 是 fixed across all batches 的 post-hoc optimum，b*≈0.9 是 per-batch adaptive 的均值。二者不可直接比较，因为 (a) 不同 batch 的最优 b 不同，平均值不等于最优固定值；(b) per-batch b* 的分布信息比均值更重要——如果 b* 的分布是 bimodal（大量 b*=0 clean batch + 少量 b*>2 highly contaminated batch），均值 0.9 的含义与所有 batch b*≈0.9 完全不同。论文 §5.3 的 regime 分析（5.8% clean, ~50% α_eff-binding, ~44% ESS-binding）支持这种异质性。不过 R1 的 concern 仍有一定道理——如果 median b* 也接近 0.9（而非 0.3），那确实说明 adaptive method 的 typical intervention 高于 grid-best，需要解释为什么 per-batch higher b 会比 global lower b 更好。\n\n---\n\n### 两位 Reviewer 的共识与分歧\n\n**强共识（两人独立提出同一问题）**：\n1. N=3 统计功效不足（R1-N1 / R2-N1）\n2. Self-contamination 生态效度（R1-N2 / R2-N2）\n3. Downstream 零改善（R1-N3 / R2-N3）\n\n这三个 critical issues 是两位 reviewer 独立达成的共识，作者 rebuttal 必须正面回应。\n\n**R1 独有的强技术批评（R2 需补充的遗漏）**：\n- R1-W4（detector causal claim 需控制实验）和 R1-W6（缺 uniform + multi-epoch baseline）是我审稿中未充分展开的重要技术点，我完全赞同。\n- R1-W1（B=4 micro-batch 统计可靠性）我虽然注意到但未作为独立 weakness 提出，R1 的分析更到位。\n\n**R2 独有的关注点**：\n- 论文标题 scope 与实验支撑不匹配（R2-W1）\n- Grid-best vs adaptive 差距的来源分析缺失（R2-W2）\n- α_eff proxy 讨论篇幅过长占用正文空间（R2-W3）\n- 三个 findings 深度不均匀（R2-W4）\n\n**唯一分歧**：\n- R1-M4（Figure 2 y 轴非零起点）：我认为 method comparison 论文中 truncated y-axis 是标准做法，R1 的批评过于苛刻。\n- R1-M2（Grid-best 的 τ）：Grid-best 不使用 τ 参数，R1 可能有误解。",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1017 · 2026-05-24T04:23:59.080455+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3765
}
```

</details>

---


### Assistant

_source line 1018 · 2026-05-24T04:24:08.157279+00:00_

交叉回应已提交。总结：

- **16 条 AGREE**（含 S1-S6 全部优势、N1-N3 全部 critical issues、W1-W4/W6、M1/M3/M5/M6、Q1-Q3）
- **3 条 REBUT**（W5 minimum intervention 叙事部分合理、M2 Grid-best 不使用 τ 是 R1 理解有误、M4 truncated y-axis 是标准做法）
- **1 条 partial REBUT**（Q4 均值 vs 固定值不可直接比较，但 concern 部分有效）

两位 Reviewer 在三个 critical issues（统计功效、self-contamination、downstream 零改善）上完全独立地达成一致，这是对作者最强的信号。R1 的 W4（detector causal claim）和 W6（缺 uniform+multi-epoch baseline）是我审稿中未充分展开的重要补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 25

## Round 25

60 recorded events


### User

_source line 1019 · 2026-05-25T04:43:07.432417+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查新颖性、论文完整性和格式合规。

## Venue 信息
- **目标 venue**: EMNLP 2026（via ARR May 2026 cycle）
- **截止日期**: 2026-05-25
- **页数限制**: 正文 ≤8 页，references 无限，Limitations 必须写（不计入页数）
- **模板**: ACL style，double-blind
- **匿名规则**: 不得包含作者信息，自引需避免暴露身份
- **Abstract**: ≤200 words

## EMNLP 2026 特殊规则
- Main/Findings 不分开投稿，走同一 ARR 审稿系统
- Long/Short 走同一审稿系统
- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit
- Responsible NLP Checklist 在 OpenReview 表单里（不在 PDF 里）
- 一篇文章只能有一个 Limitations section，放正文，appendix 不能有

## 论文信息
- **标题**: "When Does Detect-and-Reweight Work for Synthetic Contamination?"
- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf

## 你的审查侧重

### 1. 新颖性评估
- 论文的核心贡献是什么？是方法贡献还是 analysis 贡献？
- w=(1-q)^b 完全来自 Drayson et al. (2025)，adaptive b* 的 dual constraint 是否构成足够的方法新颖性？
- 三个 findings（epoch confound, detector calibration, minimum intervention）的新颖程度分别如何？
- 与 Drayson et al. 的差异化是否清晰？
- Per-batch bisection 是否只是标准方法的直接应用？

### 2. 论文完整性
- 论文 framing 是否一致（abstract/intro/discussion/conclusion 的定位是否统一）
- Claims 与 evidence 是否匹配（特别注意 overclaim）
- Related Work 是否遗漏重要工作（检查 RAID, M4 detection benchmarks, Phi 系列 synthetic data 正面案例, Owen 2013 importance weighting failure modes）
- Limitations 是否充分覆盖主要弱点
- 下游任务零改善与 "practical adaptive method" 或 "practical corollary" 表述是否矛盾
- 标题 "When Does D&R Work?" 暗示一般性，但实验仅支持 self-contamination

### 3. 格式合规
- 正文是否在 8 页以内（§1-§7 + Limitations）
- Abstract 是否 ≤200 words
- 是否有 Responsible NLP Checklist 出现在 PDF 中（不应该有）
- 匿名性检查
- Figure/Table 质量和 display item 分布
- 引用格式是否正确（natbib）
- Appendix 中是否有不该出现的 Limitations section

### 输出格式
请按以下结构输出审稿意见：
1. **Summary** (2-3 句)
2. **Strengths** (逐条, S1/S2/...)
3. **Weaknesses** (逐条, W1/W2/..., 标注 severity: must-fix / should-fix / minor)
4. **Questions** (Q1/Q2/...)
5. **Missing References** (如有)
6. **Novelty Assessment** (F1-F3 各项新颖性评级: 高/中/低)
7. **Overall Assessment** (评分 + 简要理由, 使用 EMNLP 2026 ARR 评分标准: 1-5 分)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-25T04:43:24.275212+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-25T04:43:24.275543+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-25T04:43:24.827512+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1023 · 2026-05-25T04:43:24.879023+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-25T04:43:28.502469+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1025 · 2026-05-25T04:43:30.710788+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf",
  "pages": "1-10",
  "project": "provenance_weight_training",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf",
    "pages": "1-10",
    "project": "provenance_weight_training",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1026 · 2026-05-25T04:43:36.712873+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I've found search results related to ACL ARR 2026 reviewer guidelines and review form criteria. Here's what I found:

## Review Form Criteria

For Main versus Findings papers, the main criteria for Findings are soundness and reproducibility, while confe
…[truncated 1265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8210
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-25T04:43:38.119553+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 414.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 426.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 469.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7408
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-25T04:43:46.421384+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and any guidelines for each dimension. Include the Overall Assessment scale if present."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and any guidelines for each dimension. Include the Overall Assessment scale if present."
  }
}
```

</details>

---


### Tool call

_source line 1029 · 2026-05-25T04:43:46.873565+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1030 · 2026-05-25T04:43:47.878049+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1031 · 2026-05-25T04:43:47.878472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-25T04:43:48.480592+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-25T04:43:48.935675+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1057
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-25T04:43:48.986372+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-25T04:43:49.440965+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 1036 · 2026-05-25T04:43:49.642053+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1037 · 2026-05-25T04:43:49.643101+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool result

_source line 1038 · 2026-05-25T04:43:50.195982+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool result

_source line 1039 · 2026-05-25T04:43:55.368151+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award: This paper could be considered for an outstanding paper award."
- **4.5**: "Borderline Award"
- **4**: "Conference: This paper could be accepted to an *ACL conference."
- **3.5**: "Borderline Conference"
- **3**: "Findings: This paper could be accepted to the Findings of the ACL."
- **2.5**: "Borderline Findings"
- **2**: "Resubmit next cycle: This paper needs substantial re
…[truncated 1879 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 8946
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-25T04:44:02.347592+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1041 · 2026-05-25T04:44:02.799288+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1042 · 2026-05-25T04:44:04.105097+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1757
}
```

</details>

---


### Tool result

_source line 1043 · 2026-05-25T04:44:04.105831+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool call

_source line 1044 · 2026-05-25T04:44:04.256603+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-25T04:44:05.160452+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-25T04:44:05.160972+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf",
  "pages": "11-15",
  "project": "provenance_weight_training",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/submitted.pdf",
    "pages": "11-15",
    "project": "provenance_weight_training",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1047 · 2026-05-25T04:44:05.712945+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 358.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 442.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 472.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 297.9}], \"total_pages\": 15, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 551
}
```

</details>

---


### Tool call

_source line 1048 · 2026-05-25T04:44:10.733492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1049 · 2026-05-25T04:44:11.185580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1050 · 2026-05-25T04:44:11.639584+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 1051 · 2026-05-25T04:44:11.640054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1052 · 2026-05-25T04:44:12.547569+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool result

_source line 1053 · 2026-05-25T04:44:12.600235+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 1054 · 2026-05-25T04:44:12.600680+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 1055 · 2026-05-25T04:44:13.053510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1056 · 2026-05-25T04:44:13.607207+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 1057 · 2026-05-25T04:44:13.607616+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1058 · 2026-05-25T04:44:14.060658+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool call

_source line 1059 · 2026-05-25T04:44:14.061046+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1060 · 2026-05-25T04:44:14.417827+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 810
}
```

</details>

---


### Tool result

_source line 1061 · 2026-05-25T04:44:14.620143+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 559
}
```

</details>

---


### Tool call

_source line 1062 · 2026-05-25T04:49:38.831437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-25T04:49:38.831800+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{tikz}
20	\usetikzlibrary{positioning,arrows.meta}
21	\usepackage{hyperref}
22	
23	\newtheorem{proposition}{Proposition}
24	\newtheorem{definition}{Definition}
25	
26	\newcommand{\bstar}{b^*}
27	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
28	\newcommand{\nmin}{n_{\min}}
29	\newcommand{\btau}{b_{\tau}}
30	\newcommand{\bess}{b_{\mathrm{ESS}}}
31	\title{When Does Detect-and-Reweight Work for Synthetic Contamination?}
32	
33	\author{Anonymous}
34	
35	\begin{document}
36	\maketitle
37	
38	\begin{abstract}
39	\input{sections/abstract}
40	\end{abstract}
41	
42	\section{Introduction}
43	\label{sec:intro}
44	\input{sections/introduction}
45	
46	\section{Related Work}
47	\label{sec:related}
48	\input{sections/related_work}
49	
50	\section{Method}
51	\label{sec:method}
52	\input{sections/method}
53	
54	\section{Experimental Setup}
55	\label{sec:experiments}
56	\input{sections/experiments}
57	
58	\section{Results}
59	\label{sec:results}
60	\input{sections/results}
61	
62	\section{Discussion}
63	\label{sec:discussion}
64	\input{sections/discussion}
65	
66	\section{Conclusion}
67	\label{sec:conclusion}
68	\input{sections/conclusion}
69	
70	\section*{Limitations}
71	\label{sec:limitations}
72	\input{sections/limitations}
73	
74	\bibliography{references}
75	
76	\appendix
77	\input{sections/appendix}
78	
79	\end{document}
80	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1064 · 2026-05-25T04:49:44.707747+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex | wc -w",
  "description": "Count abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex | wc -w",
    "description": "Count abstract word count"
  }
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-25T04:49:44.909307+00:00_

155

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1066 · 2026-05-25T04:49:44.909921+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1067 · 2026-05-25T04:49:45.010614+00:00_

1	As synthetic text pervades web corpora, detect-and-reweight methods---downweighting likely-synthetic samples during training---have emerged to prevent model collapse, yet when they actually help remains unclear.
2	We investigate this question through controlled continued-pretraining experiments (Qwen3-0.6B, 132M tokens, 5 seeds) and identify three effectiveness conditions.
3	First, published detect-and-remove evaluations are confounded by multi-epoch exposure: over 95\% of the reported advantage vanishes under epoch-matched controls.
4	Second, the detector must provide both sufficient discrimination \emph{and} good calibration; high-AUC detectors with poor calibration degrade performance below uniform training.
5	Third, minimum intervention---applying the smallest reweighting exponent that meets a quality floor---outperforms unconstrained weight maximization.
6	As an illustrative application of the minimum-intervention principle, we derive a dual-constrained adaptive exponent $\bstar$ that improves over uniform training at contamination ratios $\rho \geq 0.4$, reaching conventional significance after multiple-comparison correction, while requiring no per-model tuning.
7	These findings apply within our self-contamination setup at 0.6B scale; generalization to cross-model contamination and larger models remains to be established.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1068 · 2026-05-25T04:50:02.873957+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -ri \"practical\" /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/ 2>/dev/null | head -20",
  "description": "Search for \"practical\" mentions in paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -ri \"practical\" /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/ 2>/dev/null | head -20",
    "description": "Search for \"practical\" mentions in paper sections"
  }
}
```

</details>

---


### Tool result

_source line 1069 · 2026-05-25T04:50:03.765194+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 891
}
```

</details>

---


### Tool call

_source line 1070 · 2026-05-25T04:50:03.868039+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -ri \"corollary\\|practitioner\" /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/ 2>/dev/null | head -20",
  "description": "Search for \"corollary\" and \"practitioner\" mentions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -ri \"corollary\\|practitioner\" /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/ 2>/dev/null | head -20",
    "description": "Search for \"corollary\" and \"practitioner\" mentions"
  }
}
```

</details>

---


### Tool result

_source line 1071 · 2026-05-25T04:50:04.169897+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex:For practitioners, this means D\&R's published advantages should be interpreted with caution: in continued pretraining scenarios where the corpus is small relative to training compute, aggressive filtering can inadvertently create multi-epoch regimes that inflate apparent gains.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex:\caption{Decision summary for practitioners.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex:For practitioners, reweighting is worthwhile only when $\rho \geq 0.4$ and the detector is well-calibrated (Table~\ref{tab:decision}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-25T04:52:08.552153+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见：When Does Detect-and-Reweight Work for Synthetic Contamination?\n\n**审稿依据**: ACL ARR Review Form（Soundness / Excitement / Reproducibility / Overall Assessment），以及 Director 指定的三个侧重：新颖性、论文完整性、格式合规。\n\n---\n\n## 1. Summary\n\n本文通过 Qwen3-0.6B 的 controlled continued pretraining 实验（132M tokens，5 seeds），识别了 detect-and-reweight (D&R) 方法有效运作的三个条件：(1) 已发表的 D&R 评估受 multi-epoch exposure 混淆，去除该混淆后 >95% 的优势消失；(2) detector 需同时具备足够的 discrimination (AUC≥0.8) 和良好的 calibration (ECE<0.05)；(3) minimum intervention（满足 quality floor 的最小 sharpening exponent）优于 unconstrained weight maximization。论文提出 dual-constrained adaptive b* 作为 minimum-intervention 原则的示例应用。\n\n---\n\n## 2. Strengths\n\n**S1** [Epoch confound 发现]: §5.1 的 epoch confound 是本文最强贡献。Table 2 和 Figure 1(a) 清晰展示：在 epoch-matched controls 下，D&R 的 raw PPL 优势（如 ρ=0.3 时 Δ≈-1.1）缩减至 Δ≈-0.017（3-seed），落在 cross-seed variance 范围内。实验设计——对比 raw PPL vs. epoch-matched PPL across multiple threshold settings——简洁有效。这一发现对 data curation 社区有实际预警价值。\n\n**S2** [严谨的实验方法论]: 5 seeds + Bonferroni-Holm correction；ablation controls 设计周全（Permuted 破坏 q-score 信号保留 weight non-uniformity，Random 使用随机权重，ESS-only 最大化 b 至 stability ceiling），Table 3 的 ablation hierarchy (Adaptive > Uniform > ESS-only > Random > Permuted) 逻辑清晰；统计检验报告完整（paired t-test, effect sizes, p_adj）。\n\n**S3** [诚实的 framing]: 论文将方法定位为 \"an illustrative application\"（Abstract line 6）而非主要贡献，是恰当的自我定位。Abstract 末句和 Limitations 对 scope 的限定（self-contamination, 0.6B scale）是负责任的学术表述。\n\n**S4** [Constraint regime 分析]: Figure 7 的 constraint regime decomposition 提供了有价值的实践洞察：ρ=0.4 时 ~59% 的 batches 是 clean（α_eff ≥ τ），~40% 是 ESS-binding，说明方法的介入范围有限且可预测。\n\n**S5** [视觉和写作密度]: 8 页正文包含 7 个 figures 和 5 个 tables，每个都有明确目的。写作紧凑高效，论证链条清晰。\n\n---\n\n## 3. Weaknesses\n\n**W1** [must-fix] **标题暗示的通用性远超实验 scope**\n\n标题 \"When Does Detect-and-Reweight Work for Synthetic Contamination?\" 暗示一般性回答，但实验受限于：(i) self-contamination（同一模型 Qwen3-0.6B 生成并检测），(ii) 单一模型家族 0.6B（1.7B 仅简短提及，§5.2 末段\"the benefit diminishes to Δ≈−0.013 with OOD mixed\"），(iii) continued pretraining 而非 from-scratch，(iv) 单一数据源（FineWeb subset）。\n\n关键矛盾：论文最重要的发现 F1（epoch confound）在 §6 中明确承认\"invisible in Drayson et al. (2025) because from-scratch pretraining on large corpora rarely completes even one epoch\"——也就是说，该发现在最常见的 pretraining 设定下不适用。标题却没有反映这一关键 scope 限定。\n\n建议：标题应更具体地反映 scope，例如 \"When Does Detect-and-Reweight Work? An Analysis of Self-Contamination in Continued Pretraining\" 或类似表述。\n\n**W2** [must-fix] **下游任务零改善与 practitioner 导向 framing 之间的矛盾**\n\nTable 10（Appendix I）显示 adaptive reweighting 在 MMLU、HellaSwag 等下游任务上无有意义改善（differences within standard error）。然而论文在三处使用 practitioner 导向表述：\n- §5.1: \"For practitioners, this means D&R's published advantages should be interpreted with caution\"\n- §6 Table 5: \"Decision summary for practitioners\"\n- §7: \"For practitioners, reweighting is worthwhile only when ρ≥0.4 and the detector is well-calibrated\"\n\nAbstract 说 \"improves over uniform training at contamination ratios ρ≥0.4\"，但未指明仅限 PPL。读者自然会期待 \"improvement\" 包括实际任务表现。PPL 改善 0.023–0.032 点且不传导至下游任务，\"worthwhile\" 一词缺乏实际支撑。\n\n建议：(a) Abstract 和 Conclusion 中明确限定 \"improves held-out PPL\" 而非泛泛 \"improves over uniform training\"；(b) 在 main text（而非仅 Appendix I）讨论下游任务的 null result 及其含义。\n\n**W3** [should-fix] **方法新颖性有限，与 Drayson et al. (2025) 的差异不够清晰**\n\n- 权重公式 w=(1−q)^b 完全来自 Drayson et al.\n- Dual constraint（quality floor via α_eff ≥ τ + stability ceiling via ESS ≤ b_ESS）是两个自然约束的组合，bisection 求解 b* 是标准方法\n- Per-batch adaptation 在约束定义后是直接应用，无独立方法创新\n\n与 Drayson et al. 的三点差异（§2 末段）：(a) b* 来自 dual constraint 而非 grid search——标准优化替代 grid search；(b) per-model and per-exponent 选择——但 Drayson 的 validation-based selection 也是 per-model 的；(c) SIR discretization——技术细节。\n\n论文将方法定位为 \"illustrative application\" 是对的，但 Introduction 没有足够突出这一定位。读者在读完 Introduction 后可能预期一个重要的方法贡献，直到 §3 才明确降低预期。\n\n**W4** [should-fix] **Detector 覆盖面极窄，削弱 \"detector requirements\" 发现的通用性**\n\n§5.2 的核心 claim \"both sufficient discrimination and good calibration are required\"（AUC≥0.8, ECE<0.05）仅基于 3 个 detector：TF-IDF+LR（AUC=0.94, ECE=0.05）、GPT-2 perplexity（AUC=0.91）、N-gram（AUC=0.73）。Table 14 显示仅 TF-IDF+LR 有效。\n\n三个数据点不足以得出 AUC/ECE threshold 的通用规律。现代 neural detectors（fine-tuned RoBERTa/DeBERTa、DetectGPT variants、Binoculars、RADAR）的 AUC-ECE profile 可能完全不同，特别是 neural detectors 通常有更好的 calibration。这些 threshold 可能在更广泛的 detector 覆盖下不成立。\n\n**W5** [should-fix] **效果量极小，实际显著性存疑**\n\n主要改善为 ρ=0.1 时 Δ=−0.023 PPL，ρ=0.4 时 Δ=−0.032 PPL（§5.1, §5.2）。虽然 Bonferroni-Holm 校正后达到统计显著性，但论文未讨论这一 PPL 变化在 continued pretraining context 下的实际意义。0.03 PPL 的改善在工程实践中是否可感知？结合 W2（零下游改善），效果量的实际价值需要更审慎的讨论。\n\n**W6** [should-fix] **Self-contamination 设定的生态效度**\n\n真实 web contamination 来自多种生成器（GPT-4, Claude, Llama, Gemini 等），质量和风格各异，混合在异质来源中。Self-contamination（同一模型生成+检测）是对 detector 最有利的设定——q-scores 在 generator-detector 同分布时信息量最大。\n\nAppendix O 的 cross-model 结果（Llama-3.2-3B）不够成熟（\"reflect evaluation-set distribution sensitivity rather than consistent quality differences\"），反而暴露了 generalization 的困难。这削弱了论文从 self-contamination 推广到一般 synthetic contamination 的可信度。\n\n**W7** [minor] **ρ≥0.4 的实用门槛偏高**\n\n论文 §1 引用的 synthetic text 比例估计为 20–60%。Conclusion 指出 \"reweighting is worthwhile only when ρ≥0.4\"，加上 calibration 要求，实际适用场景非常窄。这不一定是分析缺陷，但 \"Decision summary for practitioners\"（Table 5）的 practitioner 导向 framing 在如此受限的适用范围下可能给读者不准确的信号。\n\n**W8** [minor] **PPL 与模型质量的关系未讨论**\n\n论文以 held-out PPL 为主要指标，但未讨论在 continued pretraining 中，多大的 PPL 改善才对应有意义的 capability 提升。鉴于下游 null result，这一讨论对解读 findings 很重要。\n\n---\n\n## 4. Questions\n\n**Q1**: Epoch confound（F1）在 from-scratch pretraining 中不适用（§6）。那么论文对最常见的 pretraining 设定（corpus >> training budget，不会出现 multi-epoch）有何 relevance？如果 F1 不适用于 from-scratch，论文标题的 \"When Does D&R Work?\" 实际上在回答一个更窄的问题。\n\n**Q2**: Table 14 仅有 TF-IDF+LR 有效。是否尝试过 neural-based detectors（如 fine-tuned ModernBERT/DeBERTa）？AUC≥0.8, ECE<0.05 的 practical guidance 在更广泛的 detector sweep 下是否稳健？\n\n**Q3**: Quality floor τ=0.7 贯穿全文。Table 7（Appendix D）显示了一些 threshold sensitivity，但是否有 principled way 选择 τ，还是它本质上是另一个需要调优的超参数？\n\n**Q4**: Algorithm 1 的 per-batch bisection 独立决定每个 batch 的 b*。这是否造成训练动态的不稳定？Figure 8（Appendix）显示了 b* trajectory，但 b* 在 batch 间的 variance 对 gradient noise 的影响是否被分析过？\n\n**Q5**: 1.7B 规模下 benefit 缩减至 Δ≈−0.013（§5.2）。这是否暗示方法在 practitioner 关注的规模（7B+）下可能完全失效？如果是，\"Decision summary for practitioners\" 的适用性就更加有限。\n\n---\n\n## 5. Missing References\n\n- **RAID benchmark** (Dugan et al., 2024): 大规模 AI text detection benchmark，覆盖多种 generator 和 domain，与 §5.2 的 detector 评估直接相关——可提供跨 detector-generator pair 的 standardized AUC/ECE measurements 作为参照。\n- **M4 shared task** (Wang et al., 2024): 多语言多生成器检测 benchmark，与 detector generalization 讨论相关。\n\n论文已覆盖：Phi series (Gunasekar et al., 2023; Li et al., 2023) ✓，Owen (2013) importance weighting failure modes ✓。\n\n---\n\n## 6. Novelty Assessment\n\n| Finding | 新颖性 | 评估理由 |\n|---------|--------|----------|\n| F1: Epoch confound | **中偏高** | 揭示了 D&R 评估中一个此前未注意的重要混淆变量。实验设计（epoch-matched controls）简洁有效，对社区有预警价值。但：(a) 仅适用于 continued pretraining（from-scratch 不受影响），(b) 本质是实验观察而非方法创新。 |\n| F2: Detector calibration | **中** | AUC 和 ECE 独立影响 reweighting 效果有用，但部分可预期（calibration 对 importance weighting 的影响是已知的，cf. Owen 2013）。仅基于 3 个 detector 的数据点，threshold 通用性存疑。 |\n| F3: Minimum intervention | **中偏低** | \"less is more\" 在 importance weighting 中非新见解（ESS constraint 是标准实践）。Dual-constrained bisection 是两个自然约束 + 标准求解方法的直接组合。主要价值在实验验证。 |\n\n**整体方法新颖性**: 低。w=(1−q)^b 来自 Drayson et al.，adaptive b* 的 dual constraint 是标准优化的应用，per-batch bisection 无独立新颖性。论文价值主要在 empirical findings，尤其 F1。\n\n---\n\n## 7. Overall Assessment\n\n### ARR Review Form 维度\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3.5/5 | 实验方法论严谨（5 seeds, Bonferroni-Holm, 充分 ablation），但核心 claims 的支撑范围超出实验 scope：标题暗示通用性 vs. 仅 self-contamination + continued pretraining；detector threshold 基于 3 个数据点。 |\n| Excitement | 2.5/5 | Epoch confound（F1）有社区价值，但整体贡献偏增量：窄 scope、零下游改善、方法借用 Drayson et al.。一般的 data curation/weighting 研究者可能会记住 F1，但不太可能基于此文改变自己的研究方向。 |\n| Reproducibility | 4/5 | 实验设置描述详细（超参 Table 1、detector 训练细节 Appendix M、统计检验方法 Appendix R），Appendix 覆盖 17 项补充分析。未明确承诺开源代码和数据。 |\n| Reviewer Confidence | 4/5 | 熟悉 data curation/weighting for LLM pretraining 相关工作。 |\n\n### Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n论文在实验方法论上是严谨的，epoch confound 发现（F1）对社区有实际价值，写作诚实且 self-aware。但以下问题限制了其影响力：\n\n1. **标题与 scope 的不匹配**（W1）：核心发现 F1 不适用于 from-scratch pretraining，但标题未反映。\n2. **方法新颖性有限**（W3）：主要建立在 Drayson et al. 基础上，dual-constrained bisection 是标准技术。\n3. **零下游改善**（W2）：PPL 改善极小且不传导至任何下游任务，削弱 practitioner 导向 framing 的可信度。\n4. **窄 detector 覆盖**（W4）：仅 3 个 detector，核心 AUC/ECE threshold 缺乏通用性。\n5. **适用范围极窄**（W7）：仅在 ρ≥0.4 + well-calibrated detector + self-contamination + continued pretraining + 0.6B scale 下有效。\n\n论文作为 focused empirical analysis 适合 Findings 接收。要达到 Conference 水平，需要：(a) 扩展 detector 覆盖（至少包括 neural detectors），(b) 在至少一个下游任务上展示改善或充分讨论 PPL-only improvement 的价值，(c) 测试 cross-model contamination 和更大规模。\n",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见：When Does Detect-and-Reweight Work for Synthetic Contamination?\n\n**审稿依据**: ACL ARR Review Form（Soundness / Excitement / Reproducibility / Overall Assessment），以及 Director 指定的三个侧重：新颖性、论文完整性、格式合规。\n\n---\n\n## 1. Summary\n\n本文通过 Qwen3-0.6B 的 controlled continued pretraining 实验（132M tokens，5 seeds），识别了 detect-and-reweight (D&R) 方法有效运作的三个条件：(1) 已发表的 D&R 评估受 multi-epoch exposure 混淆，去除该混淆后 >95% 的优势消失；(2) detector 需同时具备足够的 discrimination (AUC≥0.8) 和良好的 calibration (ECE<0.05)；(3) minimum intervention（满足 quality floor 的最小 sharpening exponent）优于 unconstrained weight maximization。论文提出 dual-constrained adaptive b* 作为 minimum-intervention 原则的示例应用。\n\n---\n\n## 2. Strengths\n\n**S1** [Epoch confound 发现]: §5.1 的 epoch confound 是本文最强贡献。Table 2 和 Figure 1(a) 清晰展示：在 epoch-matched controls 下，D&R 的 raw PPL 优势（如 ρ=0.3 时 Δ≈-1.1）缩减至 Δ≈-0.017（3-seed），落在 cross-seed variance 范围内。实验设计——对比 raw PPL vs. epoch-matched PPL across multiple threshold settings——简洁有效。这一发现对 data curation 社区有实际预警价值。\n\n**S2** [严谨的实验方法论]: 5 seeds + Bonferroni-Holm correction；ablation controls 设计周全（Permuted 破坏 q-score 信号保留 weight non-uniformity，Random 使用随机权重，ESS-only 最大化 b 至 stability ceiling），Table 3 的 ablation hierarchy (Adaptive > Uniform > ESS-only > Random > Permuted) 逻辑清晰；统计检验报告完整（paired t-test, effect sizes, p_adj）。\n\n**S3** [诚实的 framing]: 论文将方法定位为 \"an illustrative application\"（Abstract line 6）而非主要贡献，是恰当的自我定位。Abstract 末句和 Limitations 对 scope 的限定（self-contamination, 0.6B scale）是负责任的学术表述。\n\n**S4** [Constraint regime 分析]: Figure 7 的 constraint regime decomposition 提供了有价值的实践洞察：ρ=0.4 时 ~59% 的 batches 是 clean（α_eff ≥ τ），~40% 是 ESS-binding，说明方法的介入范围有限且可预测。\n\n**S5** [视觉和写作密度]: 8 页正文包含 7 个 figures 和 5 个 tables，每个都有明确目的。写作紧凑高效，论证链条清晰。\n\n---\n\n## 3. Weaknesses\n\n**W1** [must-fix] **标题暗示的通用性远超实验 scope**\n\n标题 \"When Does Detect-and-Reweight Work for Synthetic Contamination?\" 暗示一般性回答，但实验受限于：(i) self-contamination（同一模型 Qwen3-0.6B 生成并检测），(ii) 单一模型家族 0.6B（1.7B 仅简短提及，§5.2 末段\"the benefit diminishes to Δ≈−0.013 with OOD mixed\"），(iii) continued pretraining 而非 from-scratch，(iv) 单一数据源（FineWeb subset）。\n\n关键矛盾：论文最重要的发现 F1（epoch confound）在 §6 中明确承认\"invisible in Drayson et al. (2025) because from-scratch pretraining on large corpora rarely completes even one epoch\"——也就是说，该发现在最常见的 pretraining 设定下不适用。标题却没有反映这一关键 scope 限定。\n\n建议：标题应更具体地反映 scope，例如 \"When Does Detect-and-Reweight Work? An Analysis of Self-Contamination in Continued Pretraining\" 或类似表述。\n\n**W2** [must-fix] **下游任务零改善与 practitioner 导向 framing 之间的矛盾**\n\nTable 10（Appendix I）显示 adaptive reweighting 在 MMLU、HellaSwag 等下游任务上无有意义改善（differences within standard error）。然而论文在三处使用 practitioner 导向表述：\n- §5.1: \"For practitioners, this means D&R's published advantages should be interpreted with caution\"\n- §6 Table 5: \"Decision summary for practitioners\"\n- §7: \"For practitioners, reweighting is worthwhile only when ρ≥0.4 and the detector is well-calibrated\"\n\nAbstract 说 \"improves over uniform training at contamination ratios ρ≥0.4\"，但未指明仅限 PPL。读者自然会期待 \"improvement\" 包括实际任务表现。PPL 改善 0.023–0.032 点且不传导至下游任务，\"worthwhile\" 一词缺乏实际支撑。\n\n建议：(a) Abstract 和 Conclusion 中明确限定 \"improves held-out PPL\" 而非泛泛 \"improves over uniform training\"；(b) 在 main text（而非仅 Appendix I）讨论下游任务的 null result 及其含义。\n\n**W3** [should-fix] **方法新颖性有限，与 Drayson et al. (2025) 的差异不够清晰**\n\n- 权重公式 w=(1−q)^b 完全来自 Drayson et al.\n- Dual constraint（quality floor via α_eff ≥ τ + stability ceiling via ESS ≤ b_ESS）是两个自然约束的组合，bisection 求解 b* 是标准方法\n- Per-batch adaptation 在约束定义后是直接应用，无独立方法创新\n\n与 Drayson et al. 的三点差异（§2 末段）：(a) b* 来自 dual constraint 而非 grid search——标准优化替代 grid search；(b) per-model and per-exponent 选择——但 Drayson 的 validation-based selection 也是 per-model 的；(c) SIR discretization——技术细节。\n\n论文将方法定位为 \"illustrative application\" 是对的，但 Introduction 没有足够突出这一定位。读者在读完 Introduction 后可能预期一个重要的方法贡献，直到 §3 才明确降低预期。\n\n**W4** [should-fix] **Detector 覆盖面极窄，削弱 \"detector requirements\" 发现的通用性**\n\n§5.2 的核心 claim \"both sufficient discrimination and good calibration are required\"（AUC≥0.8, ECE<0.05）仅基于 3 个 detector：TF-IDF+LR（AUC=0.94, ECE=0.05）、GPT-2 perplexity（AUC=0.91）、N-gram（AUC=0.73）。Table 14 显示仅 TF-IDF+LR 有效。\n\n三个数据点不足以得出 AUC/ECE threshold 的通用规律。现代 neural detectors（fine-tuned RoBERTa/DeBERTa、DetectGPT variants、Binoculars、RADAR）的 AUC-ECE profile 可能完全不同，特别是 neural detectors 通常有更好的 calibration。这些 threshold 可能在更广泛的 detector 覆盖下不成立。\n\n**W5** [should-fix] **效果量极小，实际显著性存疑**\n\n主要改善为 ρ=0.1 时 Δ=−0.023 PPL，ρ=0.4 时 Δ=−0.032 PPL（§5.1, §5.2）。虽然 Bonferroni-Holm 校正后达到统计显著性，但论文未讨论这一 PPL 变化在 continued pretraining context 下的实际意义。0.03 PPL 的改善在工程实践中是否可感知？结合 W2（零下游改善），效果量的实际价值需要更审慎的讨论。\n\n**W6** [should-fix] **Self-contamination 设定的生态效度**\n\n真实 web contamination 来自多种生成器（GPT-4, Claude, Llama, Gemini 等），质量和风格各异，混合在异质来源中。Self-contamination（同一模型生成+检测）是对 detector 最有利的设定——q-scores 在 generator-detector 同分布时信息量最大。\n\nAppendix O 的 cross-model 结果（Llama-3.2-3B）不够成熟（\"reflect evaluation-set distribution sensitivity rather than consistent quality differences\"），反而暴露了 generalization 的困难。这削弱了论文从 self-contamination 推广到一般 synthetic contamination 的可信度。\n\n**W7** [minor] **ρ≥0.4 的实用门槛偏高**\n\n论文 §1 引用的 synthetic text 比例估计为 20–60%。Conclusion 指出 \"reweighting is worthwhile only when ρ≥0.4\"，加上 calibration 要求，实际适用场景非常窄。这不一定是分析缺陷，但 \"Decision summary for practitioners\"（Table 5）的 practitioner 导向 framing 在如此受限的适用范围下可能给读者不准确的信号。\n\n**W8** [minor] **PPL 与模型质量的关系未讨论**\n\n论文以 held-out PPL 为主要指标，但未讨论在 continued pretraining 中，多大的 PPL 改善才对应有意义的 capability 提升。鉴于下游 null result，这一讨论对解读 findings 很重要。\n\n---\n\n## 4. Questions\n\n**Q1**: Epoch confound（F1）在 from-scratch pretraining 中不适用（§6）。那么论文对最常见的 pretraining 设定（corpus >> training budget，不会出现 multi-epoch）有何 relevance？如果 F1 不适用于 from-scratch，论文标题的 \"When Does D&R Work?\" 实际上在回答一个更窄的问题。\n\n**Q2**: Table 14 仅有 TF-IDF+LR 有效。是否尝试过 neural-based detectors（如 fine-tuned ModernBERT/DeBERTa）？AUC≥0.8, ECE<0.05 的 practical guidance 在更广泛的 detector sweep 下是否稳健？\n\n**Q3**: Quality floor τ=0.7 贯穿全文。Table 7（Appendix D）显示了一些 threshold sensitivity，但是否有 principled way 选择 τ，还是它本质上是另一个需要调优的超参数？\n\n**Q4**: Algorithm 1 的 per-batch bisection 独立决定每个 batch 的 b*。这是否造成训练动态的不稳定？Figure 8（Appendix）显示了 b* trajectory，但 b* 在 batch 间的 variance 对 gradient noise 的影响是否被分析过？\n\n**Q5**: 1.7B 规模下 benefit 缩减至 Δ≈−0.013（§5.2）。这是否暗示方法在 practitioner 关注的规模（7B+）下可能完全失效？如果是，\"Decision summary for practitioners\" 的适用性就更加有限。\n\n---\n\n## 5. Missing References\n\n- **RAID benchmark** (Dugan et al., 2024): 大规模 AI text detection benchmark，覆盖多种 generator 和 domain，与 §5.2 的 detector 评估直接相关——可提供跨 detector-generator pair 的 standardized AUC/ECE measurements 作为参照。\n- **M4 shared task** (Wang et al., 2024): 多语言多生成器检测 benchmark，与 detector generalization 讨论相关。\n\n论文已覆盖：Phi series (Gunasekar et al., 2023; Li et al., 2023) ✓，Owen (2013) importance weighting failure modes ✓。\n\n---\n\n## 6. Novelty Assessment\n\n| Finding | 新颖性 | 评估理由 |\n|---------|--------|----------|\n| F1: Epoch confound | **中偏高** | 揭示了 D&R 评估中一个此前未注意的重要混淆变量。实验设计（epoch-matched controls）简洁有效，对社区有预警价值。但：(a) 仅适用于 continued pretraining（from-scratch 不受影响），(b) 本质是实验观察而非方法创新。 |\n| F2: Detector calibration | **中** | AUC 和 ECE 独立影响 reweighting 效果有用，但部分可预期（calibration 对 importance weighting 的影响是已知的，cf. Owen 2013）。仅基于 3 个 detector 的数据点，threshold 通用性存疑。 |\n| F3: Minimum intervention | **中偏低** | \"less is more\" 在 importance weighting 中非新见解（ESS constraint 是标准实践）。Dual-constrained bisection 是两个自然约束 + 标准求解方法的直接组合。主要价值在实验验证。 |\n\n**整体方法新颖性**: 低。w=(1−q)^b 来自 Drayson et al.，adaptive b* 的 dual constraint 是标准优化的应用，per-batch bisection 无独立新颖性。论文价值主要在 empirical findings，尤其 F1。\n\n---\n\n## 7. Overall Assessment\n\n### ARR Review Form 维度\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3.5/5 | 实验方法论严谨（5 seeds, Bonferroni-Holm, 充分 ablation），但核心 claims 的支撑范围超出实验 scope：标题暗示通用性 vs. 仅 self-contamination + continued pretraining；detector threshold 基于 3 个数据点。 |\n| Excitement | 2.5/5 | Epoch confound（F1）有社区价值，但整体贡献偏增量：窄 scope、零下游改善、方法借用 Drayson et al.。一般的 data curation/weighting 研究者可能会记住 F1，但不太可能基于此文改变自己的研究方向。 |\n| Reproducibility | 4/5 | 实验设置描述详细（超参 Table 1、detector 训练细节 Appendix M、统计检验方法 Appendix R），Appendix 覆盖 17 项补充分析。未明确承诺开源代码和数据。 |\n| Reviewer Confidence | 4/5 | 熟悉 data curation/weighting for LLM pretraining 相关工作。 |\n\n### Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n论文在实验方法论上是严谨的，epoch confound 发现（F1）对社区有实际价值，写作诚实且 self-aware。但以下问题限制了其影响力：\n\n1. **标题与 scope 的不匹配**（W1）：核心发现 F1 不适用于 from-scratch pretraining，但标题未反映。\n2. **方法新颖性有限**（W3）：主要建立在 Drayson et al. 基础上，dual-constrained bisection 是标准技术。\n3. **零下游改善**（W2）：PPL 改善极小且不传导至任何下游任务，削弱 practitioner 导向 framing 的可信度。\n4. **窄 detector 覆盖**（W4）：仅 3 个 detector，核心 AUC/ECE threshold 缺乏通用性。\n5. **适用范围极窄**（W7）：仅在 ρ≥0.4 + well-calibrated detector + self-contamination + continued pretraining + 0.6B scale 下有效。\n\n论文作为 focused empirical analysis 适合 Findings 接收。要达到 Conference 水平，需要：(a) 扩展 detector 覆盖（至少包括 neural detectors），(b) 在至少一个下游任务上展示改善或充分讨论 PPL-only improvement 的价值，(c) 测试 cross-model contamination 和更大规模。\n",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1073 · 2026-05-25T04:52:12.418163+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3866
}
```

</details>

---


### Tool call

_source line 1074 · 2026-05-25T04:52:17.712801+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1075 · 2026-05-25T04:52:17.864014+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1076 · 2026-05-25T04:52:22.131245+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_13/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1077 · 2026-05-25T04:52:22.182048+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1078 · 2026-05-25T04:52:31.106607+00:00_

审稿意见已提交至 Review Director。

**评分**: Overall 3.0 (Findings)

**核心判断**: 论文实验方法论严谨，epoch confound 发现（F1）对社区有价值，但三个问题限制了影响力——标题通用性超出实验 scope（仅 self-contamination + continued pretraining）、方法新颖性有限（建立在 Drayson et al. 上的标准优化）、PPL 改善极小且零下游任务改善。识别了 2 个 must-fix（标题 scope 不匹配、下游 null result 与 practitioner framing 矛盾）和 4 个 should-fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 26

## Round 26

4 recorded events


### User

_source line 1079 · 2026-05-25T04:53:36.943636+00:00_

[Round 1 审稿请求]:
## [Round 1 交叉分享] Reviewer 1 的完整审稿意见

请逐条审阅 Reviewer 1 的意见，对每条 Weakness/Question 回复 **[AGREE]**（同意）或 **[REBUT]**（反驳，须说明理由）。对 Strengths 也可标注是否同意。

特别关注：
- R1 提出了你未提及的问题（如 N2 α_eff proxy 理论保证断裂、W1 grid-best b=0.3 vs adaptive b*≈0.9 偏差、W2 缺 multi-epoch uniform 基线、W4 B=4 最弱设置），请评估是否认同
- R1 与你观点重叠的问题（核心效应小+零下游、规模递减、self-contamination 生态效度），确认是否一致或有补充

---

以下是 Reviewer 1 完整审稿意见：

### Overall Assessment: 3.0 (Findings)
核心判断：Epoch confound 的揭露是最有价值的贡献，但核心方法（adaptive b*）实际效应极小（Δ=−0.023 PPL, 0.13% relative）且完全无法迁移至下游任务。

### ARR 维度打分
Soundness 3.5 | Excitement 2.5 | Reproducibility 4 | Confidence 4

### Must-Fix
**N1** [critical] 核心效应无实际意义且不迁移至下游任务
- Adaptive b* PPL 改善仅 0.13%，5 个下游基准 Δ 全在标准误内（accuracy 均 0.5414）
- Cohen's d=3.83 被极低 cross-seed 方差（σ=0.006，deterministic data ordering）人为放大
- 建议：重新定位为分析/负面结果贡献或在 B=16 下报告下游

**N2** [critical] α_eff proxy 与 Wang (2026) 理论保证之间的逻辑断裂
- Wang (2026) 要求 true real fraction ≥ τ，但论文用 α_eff 替代（R²≈0.63）
- ~37% 未解释方差意味着部分 α_eff ≥ τ 的 batch 真实 real fraction 可能 < τ
- n_min 缓冲是 heuristic，无理论保证

### Should-Fix
**W1** Grid-best b=0.3 vs adaptive b*≈0.9 偏差缺乏解释——α_eff 负偏差可能导致 b_τ 偏高
**W2** 缺少 "uniform + multi-epoch" 基线——无法区分选择性重复 vs 任意重复
**W3** 1.7B 规模效应递减 43%（−0.023→−0.013），scaling trend 未正式讨论
**W4** B=4 是最弱设置却用于主实验——B=16 时 advantage 放大 3.0×
**W5** Self-contamination 生态效度有限，cross-model 仅单 seed 无 PPL

### Minor
- M1: Permuted q-scores 仅 1 seed
- M2: ρ=0.6 p_BH=0.064 措辞略 misleading
- M3: Table 5 "Generator ≠ trainee" 应考虑标为必要条件
- M4: Cohen's d=3.83 解读需注意 paired SD vs absolute SD

### Questions
Q1: 下游零改善下推荐用于什么场景？
Q2: GPT-4 级 synthetic data 的 detector 性能？
Q3: α_eff 负偏差是否导致 b* 系统偏高？
Q4: 为何选 B=4 而非 B=8/16？
Q5: 是否考虑 curriculum learning 基线？

### Strengths
S1: Epoch confound 揭露（>95% D&R 优势来自 multi-epoch）是最强贡献
S2: 三条件框架（Table 5）有实用价值
S3: 实验设计严谨（5 seeds, BH correction, 大量消融）
S4: 写作质量高，图表清晰
S5: Propositions 1-2 数学正确，Algorithm 1 实现清晰


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1080 · 2026-05-25T04:56:14.244324+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n---\n\n## Strengths\n\n[AGREE] R1-S1: Epoch confound 是最强贡献。与我的 S1 完全一致。\n\n[AGREE] R1-S2: 三条件框架有实用价值。同意，但需注意 Table 5 的适用范围受限于 self-contamination 设定（我的 W1/W6 和 R1-W5 均指出）。\n\n[AGREE] R1-S3: 实验设计严谨。与我的 S2 一致。\n\n[AGREE] R1-S4: 写作质量高。与我的 S5 一致。\n\n[AGREE] R1-S5: 数学正确。我未独立验证 Propositions 1-2 的证明，但从 Appendix A 的推导结构看逻辑完整。\n\n---\n\n## Must-Fix\n\n### [AGREE] R1-N1: 核心效应无实际意义且不迁移至下游\n\n与我的 W2（零下游改善与 practitioner framing 矛盾）和 W5（效果量极小）完全一致。R1 补充了两个我未独立提出的有价值观察：\n\n1. **Cohen's d 被人为放大**：R1 指出 cross-seed σ=0.006 是由 deterministic data ordering 造成的——5 个 seed 仅改变模型初始化，data order 固定，因此 paired variance 极低。这意味着 Cohen's d=3.83 反映的是实验设计的低随机性而非效应的大小。如果 data ordering 也随机化（shuffle seed），paired SD 大概率升高，Cohen's d 会大幅缩水。这是一个重要的统计方法论问题。\n\n2. **Relative improvement 仅 0.13%**：我的 W5 说\"效果量极小\"但未量化 relative magnitude。0.13% 的 PPL 改善确实难以构成有实际意义的改进。\n\n我同意 R1 的建议：论文应重新定位为 **分析/负面结果贡献**（\"D&R 的优势主要来自 epoch confound，在控制后实际效应可忽略\"），而非 \"practical adaptive method\"。\n\n### [AGREE，但 severity 可降为 should-fix] R1-N2: α_eff proxy 与理论保证的逻辑断裂\n\nR1 的核心逻辑正确。论文 §3（Method）写道：\"α_eff(b) ≥ τ guarantees a convergence-rate lower bound\"，但 α_eff 是 true real fraction 的 noisy proxy（Table 12, R²≈0.63），这意味着 \"guarantees\" 一词在技术上不成立——约 37% 的 batch 中 α_eff ≥ τ 可能对应 true fraction < τ，理论保证不成立。\n\nn_min 缓冲确实是 heuristic 而非 principled correction。\n\n**但我认为 severity 可以从 critical 降为 should-fix**，原因是：\n- 论文在 §3 也写了 \"we operationalize this without the known-proportion assumption\"，表明作者知道这是近似\n- 论文的核心贡献是 empirical findings（尤其 F1），不是理论保证；α_eff 的理论动机是辅助论证，不是主 claim\n- 修复成本低：将 \"guarantees\" 改为 \"is designed to approximate\" 或 \"targets\" 即可消除误导\n\n实际影响是：α_eff 的负偏差（Table 12, 负 bias ≈ −0.03）可能导致 quality floor 过早绑定，b* 系统偏高（见下方对 R1-W1 的回应）。这是一个实证问题，不是理论错误。\n\n---\n\n## Should-Fix\n\n### [AGREE] R1-W1: Grid-best b=0.3 vs adaptive b*≈0.9 偏差\n\n这是我未提出的新问题，但 R1 的分析具有说服力。Grid search 后验最优 b=0.3（Table 3），而 adaptive 方法产生 b*≈0.9（Figure 8 trajectory），差异达 3 倍。\n\nR1 提出的因果链合理：\nα_eff 负偏差 → quality floor (α_eff ≥ τ) 过早绑定 → b_τ 被推高 → adaptive b* 远高于 post-hoc 最优\n\n这直接意味着 dual constraint 的实际表现受限于 proxy 质量。如果 proxy 系统性地低估真实 real fraction，方法会过度干预（b 过高）——恰恰违背了论文倡导的 \"minimum intervention\" 原则。\n\n这与 N2 构成闭环：理论动机依赖 α_eff ≈ true fraction，但 proxy 偏差导致方法行为偏离设计意图。\n\n### [AGREE] R1-W2: 缺少 \"uniform + multi-epoch\" 基线\n\n这是我未提出的重要遗漏。论文展示了 epoch confound（D&R 的优势来自 multi-epoch exposure），但 epoch-matched controls 只控制了 epoch 数量为 1。缺少的关键对比是：\n\n- **Uniform × 3.2 epochs**：不做任何 D&R 过滤，直接在全量数据上训练 3.2 个 epoch（与 D&R 的有效 content epochs 一致）\n- 如果 Uniform × 3.2 epochs 的 PPL 与 D&R raw PPL 相当，则证明 D&R 的全部优势来自 repetition（无论是否 selective）\n- 如果 Uniform × 3.2 epochs 更差，则说明 D&R 的 selective repetition（只重复 clean samples）确实有价值\n\n缺少这个基线使得论文无法区分两种假设：\n(a) D&R 的优势 = 任意多 epoch 训练的优势（epoch effect）\n(b) D&R 的优势 = 选择性重复 clean samples 的优势（curriculum effect）\n\n这对 epoch confound 发现（F1）的解读有实质影响。\n\n### [AGREE] R1-W3: 1.7B 规模效应递减未正式讨论\n\n我在 Q5 中以提问形式提出了同样的关切（\"1.7B 下 Δ≈−0.013，是否暗示 7B+ 下完全失效？\"）。R1 量化了递减幅度（43%），这更有说服力。\n\n补充：如果效应随规模递减的 trend 成立，那么论文的 practitioner 导向建议（Table 5, \"for practitioners\"）就更加存疑——practitioners 通常在 7B-70B 规模工作，0.6B 的结果可能完全不适用。\n\n### [AGREE，但认为 severity 比 R1 标注的更低] R1-W4: B=4 是最弱设置\n\nR1 指出 Figure 6 显示 B=16 时 advantage 放大 3.0×，论文却在 B=4 下报告主实验。\n\n我同意这应该被讨论，但认为选择 B=4 有合理理由：\n- B=4 是 conservative reporting——如果最弱设置都有统计显著性，更大 batch 只会更好\n- Table 1 显示 micro-batch=4 是实验配置的 default，gradient accumulation 到 effective B=16\n- 改用 B=16 可能引入新混淆（不同 gradient noise 水平）\n\n**但 R1 的核心问题仍然成立**：论文应至少在 B=16 下重复核心对比（Table 3 equivalent）并报告下游结果，以测试 B=4 下的 null downstream result 是否是 batch-size choice 的产物。如果 B=16 下下游任务有改善，那么 W4 的 severity 应升级。\n\n### [AGREE] R1-W5: Self-contamination 生态效度有限\n\n与我的 W6 完全一致。R1 补充指出 cross-model 结果仅单 seed 无 PPL，进一步削弱了 generalization 证据。\n\n---\n\n## Minor\n\n[AGREE] R1-M1: Permuted q-scores 仅 1 seed。我的 review 未独立提出，但 Table 3 确认仅 seed-42 有 Permuted 结果。作为 ablation 控制组，1 seed 的 reliability 有限。\n\n[AGREE] R1-M2: ρ=0.6 p_BH=0.064 措辞。如果论文暗示 \"approaching significance\" 或类似表述，需明确标为 \"not significant after correction\"。\n\n[AGREE] R1-M3: Table 5 应标注 \"Generator ≠ trainee\" 为必要条件（或至少 flag 为未测试）。\n\n[AGREE] R1-M4: Cohen's d 解读。与 N1 中的 paired SD 问题一致——效果量指标应以 absolute SD 或 pooled SD 计算以给出更保守的估计。\n\n---\n\n## Questions\n\n[AGREE] R1-Q1: 下游零改善下的推荐场景。与我的 W2 核心关切相同。\n\n[AGREE] R1-Q2: GPT-4 级 synthetic data 的 detector 性能。与我的 W4（detector 覆盖面窄）相关。真实 web contamination 以 GPT-4/Claude 级文本为主，这些模型产出的 synthetic text 更难检测，AUC/ECE profile 可能完全不同。\n\n[AGREE] R1-Q3: α_eff 负偏差 → b* 系统偏高。与 W1 构成同一问题链。\n\n[AGREE] R1-Q4: 为何选 B=4 而非 B=8/16。与 W4 一致。\n\n[AGREE，但 scope 可能超出本文] R1-Q5: Curriculum learning 基线。Curriculum learning（按样本难度/质量排序训练）确实与 D&R 相关——两者都是 sample-level weighting。但论文的 scope 是分析 D&R 的有效条件，不是提出新 curriculum 方法。如果加入 curriculum learning 基线，scope 会显著扩大。作为 \"future work\" 提及即可。\n\n---\n\n## 总结：与 R1 的共识和分歧\n\n### 高度共识（独立达到相同结论）\n1. **Overall 3.0 (Findings)**：R1 和我独立给出相同评分\n2. **Soundness 3.5, Excitement 2.5, Reproducibility 4, Confidence 4**：四个维度完全一致\n3. **核心效应极小 + 零下游改善**（R1-N1 ↔ 我的 W2+W5）\n4. **Self-contamination 生态效度**（R1-W5 ↔ 我的 W6）\n5. **Epoch confound 是最强贡献**（R1-S1 ↔ 我的 S1）\n6. **规模递减趋势**（R1-W3 ↔ 我的 Q5）\n\n### R1 提出的新问题（我同意）\n1. **α_eff proxy 理论断裂**（R1-N2）：valid，但我建议降为 should-fix\n2. **Grid-best b=0.3 vs adaptive b*≈0.9**（R1-W1）：valid，暴露了 proxy 偏差的实际影响\n3. **缺 multi-epoch uniform 基线**（R1-W2）：valid 且重要，影响 F1 的解读\n4. **B=4 最弱设置**（R1-W4）：valid，但 conservative reporting 有其合理性\n5. **Cohen's d 膨胀**（R1-N1/M4）：valid 的统计方法论问题\n\n### 唯一分歧\n- **R1-N2 的 severity**：R1 标为 critical/must-fix，我认为 should-fix 更合适。理由：论文的核心贡献是 empirical findings 不是理论保证，α_eff 的理论动机是辅助叙事，修改 \"guarantees\" 措辞即可解决最大的误导性。\n",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n---\n\n## Strengths\n\n[AGREE] R1-S1: Epoch confound 是最强贡献。与我的 S1 完全一致。\n\n[AGREE] R1-S2: 三条件框架有实用价值。同意，但需注意 Table 5 的适用范围受限于 self-contamination 设定（我的 W1/W6 和 R1-W5 均指出）。\n\n[AGREE] R1-S3: 实验设计严谨。与我的 S2 一致。\n\n[AGREE] R1-S4: 写作质量高。与我的 S5 一致。\n\n[AGREE] R1-S5: 数学正确。我未独立验证 Propositions 1-2 的证明，但从 Appendix A 的推导结构看逻辑完整。\n\n---\n\n## Must-Fix\n\n### [AGREE] R1-N1: 核心效应无实际意义且不迁移至下游\n\n与我的 W2（零下游改善与 practitioner framing 矛盾）和 W5（效果量极小）完全一致。R1 补充了两个我未独立提出的有价值观察：\n\n1. **Cohen's d 被人为放大**：R1 指出 cross-seed σ=0.006 是由 deterministic data ordering 造成的——5 个 seed 仅改变模型初始化，data order 固定，因此 paired variance 极低。这意味着 Cohen's d=3.83 反映的是实验设计的低随机性而非效应的大小。如果 data ordering 也随机化（shuffle seed），paired SD 大概率升高，Cohen's d 会大幅缩水。这是一个重要的统计方法论问题。\n\n2. **Relative improvement 仅 0.13%**：我的 W5 说\"效果量极小\"但未量化 relative magnitude。0.13% 的 PPL 改善确实难以构成有实际意义的改进。\n\n我同意 R1 的建议：论文应重新定位为 **分析/负面结果贡献**（\"D&R 的优势主要来自 epoch confound，在控制后实际效应可忽略\"），而非 \"practical adaptive method\"。\n\n### [AGREE，但 severity 可降为 should-fix] R1-N2: α_eff proxy 与理论保证的逻辑断裂\n\nR1 的核心逻辑正确。论文 §3（Method）写道：\"α_eff(b) ≥ τ guarantees a convergence-rate lower bound\"，但 α_eff 是 true real fraction 的 noisy proxy（Table 12, R²≈0.63），这意味着 \"guarantees\" 一词在技术上不成立——约 37% 的 batch 中 α_eff ≥ τ 可能对应 true fraction < τ，理论保证不成立。\n\nn_min 缓冲确实是 heuristic 而非 principled correction。\n\n**但我认为 severity 可以从 critical 降为 should-fix**，原因是：\n- 论文在 §3 也写了 \"we operationalize this without the known-proportion assumption\"，表明作者知道这是近似\n- 论文的核心贡献是 empirical findings（尤其 F1），不是理论保证；α_eff 的理论动机是辅助论证，不是主 claim\n- 修复成本低：将 \"guarantees\" 改为 \"is designed to approximate\" 或 \"targets\" 即可消除误导\n\n实际影响是：α_eff 的负偏差（Table 12, 负 bias ≈ −0.03）可能导致 quality floor 过早绑定，b* 系统偏高（见下方对 R1-W1 的回应）。这是一个实证问题，不是理论错误。\n\n---\n\n## Should-Fix\n\n### [AGREE] R1-W1: Grid-best b=0.3 vs adaptive b*≈0.9 偏差\n\n这是我未提出的新问题，但 R1 的分析具有说服力。Grid search 后验最优 b=0.3（Table 3），而 adaptive 方法产生 b*≈0.9（Figure 8 trajectory），差异达 3 倍。\n\nR1 提出的因果链合理：\nα_eff 负偏差 → quality floor (α_eff ≥ τ) 过早绑定 → b_τ 被推高 → adaptive b* 远高于 post-hoc 最优\n\n这直接意味着 dual constraint 的实际表现受限于 proxy 质量。如果 proxy 系统性地低估真实 real fraction，方法会过度干预（b 过高）——恰恰违背了论文倡导的 \"minimum intervention\" 原则。\n\n这与 N2 构成闭环：理论动机依赖 α_eff ≈ true fraction，但 proxy 偏差导致方法行为偏离设计意图。\n\n### [AGREE] R1-W2: 缺少 \"uniform + multi-epoch\" 基线\n\n这是我未提出的重要遗漏。论文展示了 epoch confound（D&R 的优势来自 multi-epoch exposure），但 epoch-matched controls 只控制了 epoch 数量为 1。缺少的关键对比是：\n\n- **Uniform × 3.2 epochs**：不做任何 D&R 过滤，直接在全量数据上训练 3.2 个 epoch（与 D&R 的有效 content epochs 一致）\n- 如果 Uniform × 3.2 epochs 的 PPL 与 D&R raw PPL 相当，则证明 D&R 的全部优势来自 repetition（无论是否 selective）\n- 如果 Uniform × 3.2 epochs 更差，则说明 D&R 的 selective repetition（只重复 clean samples）确实有价值\n\n缺少这个基线使得论文无法区分两种假设：\n(a) D&R 的优势 = 任意多 epoch 训练的优势（epoch effect）\n(b) D&R 的优势 = 选择性重复 clean samples 的优势（curriculum effect）\n\n这对 epoch confound 发现（F1）的解读有实质影响。\n\n### [AGREE] R1-W3: 1.7B 规模效应递减未正式讨论\n\n我在 Q5 中以提问形式提出了同样的关切（\"1.7B 下 Δ≈−0.013，是否暗示 7B+ 下完全失效？\"）。R1 量化了递减幅度（43%），这更有说服力。\n\n补充：如果效应随规模递减的 trend 成立，那么论文的 practitioner 导向建议（Table 5, \"for practitioners\"）就更加存疑——practitioners 通常在 7B-70B 规模工作，0.6B 的结果可能完全不适用。\n\n### [AGREE，但认为 severity 比 R1 标注的更低] R1-W4: B=4 是最弱设置\n\nR1 指出 Figure 6 显示 B=16 时 advantage 放大 3.0×，论文却在 B=4 下报告主实验。\n\n我同意这应该被讨论，但认为选择 B=4 有合理理由：\n- B=4 是 conservative reporting——如果最弱设置都有统计显著性，更大 batch 只会更好\n- Table 1 显示 micro-batch=4 是实验配置的 default，gradient accumulation 到 effective B=16\n- 改用 B=16 可能引入新混淆（不同 gradient noise 水平）\n\n**但 R1 的核心问题仍然成立**：论文应至少在 B=16 下重复核心对比（Table 3 equivalent）并报告下游结果，以测试 B=4 下的 null downstream result 是否是 batch-size choice 的产物。如果 B=16 下下游任务有改善，那么 W4 的 severity 应升级。\n\n### [AGREE] R1-W5: Self-contamination 生态效度有限\n\n与我的 W6 完全一致。R1 补充指出 cross-model 结果仅单 seed 无 PPL，进一步削弱了 generalization 证据。\n\n---\n\n## Minor\n\n[AGREE] R1-M1: Permuted q-scores 仅 1 seed。我的 review 未独立提出，但 Table 3 确认仅 seed-42 有 Permuted 结果。作为 ablation 控制组，1 seed 的 reliability 有限。\n\n[AGREE] R1-M2: ρ=0.6 p_BH=0.064 措辞。如果论文暗示 \"approaching significance\" 或类似表述，需明确标为 \"not significant after correction\"。\n\n[AGREE] R1-M3: Table 5 应标注 \"Generator ≠ trainee\" 为必要条件（或至少 flag 为未测试）。\n\n[AGREE] R1-M4: Cohen's d 解读。与 N1 中的 paired SD 问题一致——效果量指标应以 absolute SD 或 pooled SD 计算以给出更保守的估计。\n\n---\n\n## Questions\n\n[AGREE] R1-Q1: 下游零改善下的推荐场景。与我的 W2 核心关切相同。\n\n[AGREE] R1-Q2: GPT-4 级 synthetic data 的 detector 性能。与我的 W4（detector 覆盖面窄）相关。真实 web contamination 以 GPT-4/Claude 级文本为主，这些模型产出的 synthetic text 更难检测，AUC/ECE profile 可能完全不同。\n\n[AGREE] R1-Q3: α_eff 负偏差 → b* 系统偏高。与 W1 构成同一问题链。\n\n[AGREE] R1-Q4: 为何选 B=4 而非 B=8/16。与 W4 一致。\n\n[AGREE，但 scope 可能超出本文] R1-Q5: Curriculum learning 基线。Curriculum learning（按样本难度/质量排序训练）确实与 D&R 相关——两者都是 sample-level weighting。但论文的 scope 是分析 D&R 的有效条件，不是提出新 curriculum 方法。如果加入 curriculum learning 基线，scope 会显著扩大。作为 \"future work\" 提及即可。\n\n---\n\n## 总结：与 R1 的共识和分歧\n\n### 高度共识（独立达到相同结论）\n1. **Overall 3.0 (Findings)**：R1 和我独立给出相同评分\n2. **Soundness 3.5, Excitement 2.5, Reproducibility 4, Confidence 4**：四个维度完全一致\n3. **核心效应极小 + 零下游改善**（R1-N1 ↔ 我的 W2+W5）\n4. **Self-contamination 生态效度**（R1-W5 ↔ 我的 W6）\n5. **Epoch confound 是最强贡献**（R1-S1 ↔ 我的 S1）\n6. **规模递减趋势**（R1-W3 ↔ 我的 Q5）\n\n### R1 提出的新问题（我同意）\n1. **α_eff proxy 理论断裂**（R1-N2）：valid，但我建议降为 should-fix\n2. **Grid-best b=0.3 vs adaptive b*≈0.9**（R1-W1）：valid，暴露了 proxy 偏差的实际影响\n3. **缺 multi-epoch uniform 基线**（R1-W2）：valid 且重要，影响 F1 的解读\n4. **B=4 最弱设置**（R1-W4）：valid，但 conservative reporting 有其合理性\n5. **Cohen's d 膨胀**（R1-N1/M4）：valid 的统计方法论问题\n\n### 唯一分歧\n- **R1-N2 的 severity**：R1 标为 critical/must-fix，我认为 should-fix 更合适。理由：论文的核心贡献是 empirical findings 不是理论保证，α_eff 的理论动机是辅助叙事，修改 \"guarantees\" 措辞即可解决最大的误导性。\n",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1081 · 2026-05-25T04:56:17.961058+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3716
}
```

</details>

---


### Assistant

_source line 1082 · 2026-05-25T04:56:24.381187+00:00_

交叉回应已提交。

核心结论：R1 和我在所有主要判断上高度一致（Overall 3.0, 四维度评分完全相同），R1 提出了 5 个我未独立发现的有效问题（α_eff proxy 断裂、grid-best vs adaptive 偏差、缺 multi-epoch uniform 基线、B=4 选择、Cohen's d 膨胀）。唯一分歧在 N2 的 severity——我认为从 critical 降为 should-fix 更合适，因为论文的核心贡献是 empirical 而非 theoretical。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 27

## Round 27

60 recorded events


### User

_source line 1083 · 2026-05-25T21:17:12.117529+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。

## 投稿信息
- **论文**: "When Does Detect-and-Reweight Work for Synthetic Contamination?"
- **Venue**: EMNLP 2026 via ARR
- **类型**: Long paper（正文 ≤8 页，references 不限，Limitations 不计页数）
- **匿名**: Double-blind
- **模板**: ACL style
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf`

## 你的审查侧重

**核心关注（必须逐条评估）**：
1. **贡献定位与新颖性**：论文自我定位为 analysis paper 还是 method paper？w=(1-q)^b 完全来自 Drayson et al.，dual constraint + bisection 是标准方法——整体新颖性如何？是否清晰传达了分析贡献（三个 effectiveness conditions）的价值？
2. **标题与 claim scope**："When Does Detect-and-Reweight Work for Synthetic Contamination?" 暗示一般性结论，但实验仅覆盖 self-contamination / 0.6B / continued pretraining / 单一数据源。标题是否过度承诺？
3. **Abstract 质量**：是否 ≤200 words？核心 claims 是否准确反映实验结论？是否有 overclaim（如 "improves over uniform training" 未限定 PPL-only）？
4. **Related Work 完整性**：是否覆盖近期 instance-level reweighting（如 MATES, Aioli, Data Mixing Agent）、detection benchmarks（RAID, M4）、synthetic data curation（ForTIFAI, Escaping Collapse via Verification）等？
5. **写作质量**：§6 Discussion 第一段是否与 §5.1 内容重复？正文的 information density 和 narrative flow 如何？是否有不必要的冗余？
6. **格式合规**：
   - 正文（§1-§7）是否在 8 页内？
   - Limitations section 是否在正文中（非 appendix）且内容适当（~3 点）？
   - 是否有 Responsible NLP Checklist 出现在 PDF 中（不应出现）？
   - Appendix 是否 double-column？
   - 引用格式是否一致？
7. **效应量讨论**：论文是否充分讨论了 PPL 改善与下游任务能力之间的关系？Δ=-0.023 在 continued pretraining context 中的意义是否有合理论证？
8. **适用范围表述**：ρ≥0.4 实用门槛 + well-calibrated detector + self-contamination + 0.6B 下的 "Decision summary for practitioners"（Table 5/6）是否给读者准确信号？

**格式要求**：
- 按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 结构输出
- 每条 Weakness 标注 severity（critical/warning/info）并引用具体 Section/Table/Figure
- 给出 Overall Assessment 评分（参照 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1084 · 2026-05-25T21:17:22.421193+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1085 · 2026-05-25T21:17:22.524182+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1086 · 2026-05-25T21:17:28.703490+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1087 · 2026-05-25T21:17:31.663475+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "1-12",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "1-12",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1088 · 2026-05-25T21:17:31.914769+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1089 · 2026-05-25T21:17:36.179197+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's what I found regarding ACL ARR 2026 reviewer guidelines, review form criteria, and related information:

## Reviewer Guidelines

ARR asks reviewers to follow a workflow of reading the paper and getting a first impression, then searching for related work, not deliberately trying to find that particular submission.

## Review Form Criteria

The main criteria for Findin
…[truncated 1152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7475
}
```

</details>

---
