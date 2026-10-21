# Reviewer 2 coordination — Part 7 of 7

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

[← Part 6](part-006.md) · [Transcript overview](../reviewer-2-coordination.md) · [Structured JSON](../../../sessions/61/612e3ccdc1fa1ccf1a84.json)

## Round 71

### Tool call

_source line 3395 · 2026-05-25T21:27:23.505357+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 架构覆盖失衡，\"cross-architecture\" 过度声称**\n\n同意，且 R1 的观察比我自己的 N2 更精确。我原本将论文描述为 \"2 个架构家族\"（Llama + Qwen），但 R1 正确指出 Table 1 中实际是 **1 Llama + 3 Qwen**：R1-8B 基于 Llama-3-8B，而 OT-7B、QwQ-32B、R1-32B 均基于 Qwen2.5 不同规模的版本。这使架构多样性比我初始评估更弱。\n\n补充证据：Gemma-2 (Section B.3, p15) 仅用于验证 geometric precondition（cosine compression 的存在），而非完整的 metric → layer → conclusion cascade。论文 Section B.3 自身承认 \"Gemma-2-9B-it (mixed sliding/fullattention) ... produce insufficient positive samples for reliable probe-based layer selection analysis; we therefore report only the geometric precondition.\" 这意味着 cascade 的 cross-architecture 验证实质上仅有 1 个非 Qwen 模型（R1-8B）提供完整支持。\n\n我维持 \"增加非 reasoning 模型作为 control\" 的建议（我的 N2），R1 的发现进一步强化了这一需求。\n\n---\n\n**[AGREE] R1-N2: 位置混淆在 32B 上吸收 HS 优势**\n\n同意这是一个我未充分关注的重要问题。R1 准确识别了一个统计混淆：\n\n1. Section 4.3 (p6) 承认 \"quadratic residualization absorbs the advantage in 2/4 models\"——即 32B 模型。\n2. R1 进一步指出，保留显著性的 2 个模型恰好是样本量较大的 7-8B 模型（R1-8B n=43, OT-7B n=17 vs. QwQ-32B n=17, R1-32B n=20），引入了 **统计功效 vs. 真实效应的混淆**。虽然 OT-7B 和 QwQ-32B 的 n 相同（都是 17），但 R1-8B 的 n=43 远大于其余模型，确实可能驱动显著性。\n3. Section 8 (p8) 的 boundary conditions 承认 \"residualized advantage is suggestive at 32B\"，但 Abstract 和 Section 5 的 framing 并未充分传达这一限制。\n\n这与我的 W3（32B 结果弱）互补，但 R1 的角度更尖锐：问题不仅是 \"32B 弱\"，而是 **HS vs. position 的因果分离在 32B 上可能失败**，直接动摇 C2 的 generality。\n\n不过我补充一点：Table S2（Appendix U）报告 linear residualization 下 3/4 模型保留显著性。HS advantage 并非完全被 position 解释——linear vs. quadratic 的差异暗示位置效应可能是非线性的，而非 HS 信号不存在。论文如果能更明确地讨论 \"linear sufficient\" vs. \"quadratic needed\" 的含义（是过拟合 quadratic 还是真实非线性 confound），会更有说服力。\n\n---\n\n**[AGREE] R1-N3: Cosine compression 因果链缺直接证据**\n\n完全同意，这与我的 W1 一致。R1 将其升级为 Must-Fix 是合理的，因为论文 Abstract 使用了 \"The mechanism is cosine compression\" 这样的因果措辞。\n\nR1 提出的两个反事实实验都很精准：\n- (a) 归一化 cosine distance 后重新计算 crossing-rate，观察 layer selection discrepancy 是否消失；\n- (b) 人为压缩深层表征，观察 CR-composite 是否转移到深层。\n\n我补充一个额外观察：论文 Section A.1 (p12) 的 random-label decomposition 显示 \"100% of random-label repeats still select layers L0-L1\"，论文将此解释为 \"crossing-rate shallow-layer preference is label-independent\"。R1 正确指出这只证明了偏置与标签无关，**不证明 cosine compression 是该偏置的原因**。替代解释包括：浅层的 lower-rank structure、浅层更接近 input embedding 的 token-level patterns 等。\n\n综合两位 reviewer 的意见，我认为这是本文最关键的方法论缺陷。建议要么：(1) 补充归一化实验提供因果证据；(2) 将 \"mechanism\" 措辞改为 \"geometric correlate\" 或 \"candidate mechanism\"。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: AdvBench 仅验证 C1 未验证 C2**\n\n同意。Section B.1-B.2 (p14) 在 AdvBench 上复现了 metric-induced layer selection bias (C1)：CR-composite 选浅层 (median L2), precision 选深层 (median L14)。但 HS vs. text 的优势对比（C2 的核心）**仅在 HarmThoughts 数据集上完整报告**（Table 4, Section 4.3）。\n\nSection B.2 (p14) 报告了 AdvBench layer selection 的 bootstrap validation，但验证的是 \"layer selection 在 AdvBench 上是否 consistent\"（是的——仍然是 metric-induced bias），而非 \"HS 在 correct layer 上是否优于 text\"。这是一个重要区分：C1（bias 存在）和 C2（在 correct layer 上 HS 有优势）是两个独立 claim，后者的外部验证更弱。\n\n---\n\n**[AGREE] R1-W2: 两阶段设计探索自由度**\n\n部分同意。论文确实有一定的 mitigation：Section V（Hyperparameter Robustness）和 Section X.2（Effective Independent Tests）尝试量化探索空间的有效维度。Section X.2 (p29) 报告 \"the effective number of independent tests is far smaller than the raw exploration space\" 并讨论了 metric redundancy 和 layer autocorrelation 导致 effective tests 远小于 980-2,240 configurations。\n\n但 R1 的核心担忧仍然成立：**layer 和 window 的选择基于 validation set，而最终评估也在同一分布的 test set 上进行**。Table 34 的 13-25% shrinkage 是这种 optimism 的直接量化。虽然论文做了 5-fold LOO-CV (Section A, p12) 和 leave-one-out stability analysis (Section A)，但未采用真正的 nested cross-validation（即 inner loop 选参数、outer loop 评估）。\n\n建议在 Limitations 中更明确地承认这一 design choice 的后果。\n\n---\n\n**[AGREE] R1-W3: 32B n=19-20 统计推断限制**\n\n同意。这与我的 W3 一致。论文自身在 Section 4 (p4) 承认 \"BCa confidence intervals are reported for comparability but may have reduced coverage at these sample sizes\"。\n\n补充：Section A (p12) 报告 LOO-CV 在 32B 模型上的 fold stability——\"layer selection instability is particularly acute at small sample sizes\"，R1-32B 和 QwQ-32B 的 dominant layer 仅在 65-68% 的 folds 中被选中（vs. R1-8B 的 100%）。这直接印证 R1 的担忧。\n\n---\n\n**[AGREE] R1-W4: Ensemble holdout 估计的选择偏置**\n\n同意。Table 3 (p5) 的 ensemble 由 precision-best, balanced-accuracy-best, inverse-FPR-best 三个 metric 的预测平均构成——这三个 metric 和对应的层都在 validation set 上选定。然后 ensemble 在同一分布的 test folds 上评估。这构成了 selection bias：ensemble 的组成本身是 data-driven 的，却在同源数据上评估 \"是否优于 single metric\"。\n\nR1 引用 Table 34 的 13-25% shrinkage 是对这种 optimism 的定量证据。论文的 Level 3 recommendation（use ensemble）因此缺乏严格的 out-of-distribution 验证。\n\n---\n\n### 总结\n\n我与 R1 在所有 7 个问题上 **全部 AGREE**。R1 的 N1（1 Llama + 3 Qwen）和 N2（position confound + power confound）比我的初始审查更精确。R1 的 N3 与我的 W1 重合，但 R1 将其升级为 Must-Fix 是合理的，因为 Abstract 使用了因果措辞。\n\n两位 reviewer 的共识是：\n1. **架构多样性不足**（R1-N1 ≈ R2-N2）\n2. **Cosine compression 因果证据缺失**（R1-N3 ≈ R2-W1）\n3. **32B 结果弱 + position confound**（R1-N2 ≈ R2-W3）\n4. **\"Cross-architecture\" 过度声称**（R1-N1 ≈ R2-N2）\n\n这些共识问题指向 Findings 而非 Main Conference 的定位。\n\n我维持 **Overall 3.0 (Findings)** 的评分不变。",
  "reviewer_id": "2",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉回应 Reviewer 1\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 架构覆盖失衡，\"cross-architecture\" 过度声称**\n\n同意，且 R1 的观察比我自己的 N2 更精确。我原本将论文描述为 \"2 个架构家族\"（Llama + Qwen），但 R1 正确指出 Table 1 中实际是 **1 Llama + 3 Qwen**：R1-8B 基于 Llama-3-8B，而 OT-7B、QwQ-32B、R1-32B 均基于 Qwen2.5 不同规模的版本。这使架构多样性比我初始评估更弱。\n\n补充证据：Gemma-2 (Section B.3, p15) 仅用于验证 geometric precondition（cosine compression 的存在），而非完整的 metric → layer → conclusion cascade。论文 Section B.3 自身承认 \"Gemma-2-9B-it (mixed sliding/fullattention) ... produce insufficient positive samples for reliable probe-based layer selection analysis; we therefore report only the geometric precondition.\" 这意味着 cascade 的 cross-architecture 验证实质上仅有 1 个非 Qwen 模型（R1-8B）提供完整支持。\n\n我维持 \"增加非 reasoning 模型作为 control\" 的建议（我的 N2），R1 的发现进一步强化了这一需求。\n\n---\n\n**[AGREE] R1-N2: 位置混淆在 32B 上吸收 HS 优势**\n\n同意这是一个我未充分关注的重要问题。R1 准确识别了一个统计混淆：\n\n1. Section 4.3 (p6) 承认 \"quadratic residualization absorbs the advantage in 2/4 models\"——即 32B 模型。\n2. R1 进一步指出，保留显著性的 2 个模型恰好是样本量较大的 7-8B 模型（R1-8B n=43, OT-7B n=17 vs. QwQ-32B n=17, R1-32B n=20），引入了 **统计功效 vs. 真实效应的混淆**。虽然 OT-7B 和 QwQ-32B 的 n 相同（都是 17），但 R1-8B 的 n=43 远大于其余模型，确实可能驱动显著性。\n3. Section 8 (p8) 的 boundary conditions 承认 \"residualized advantage is suggestive at 32B\"，但 Abstract 和 Section 5 的 framing 并未充分传达这一限制。\n\n这与我的 W3（32B 结果弱）互补，但 R1 的角度更尖锐：问题不仅是 \"32B 弱\"，而是 **HS vs. position 的因果分离在 32B 上可能失败**，直接动摇 C2 的 generality。\n\n不过我补充一点：Table S2（Appendix U）报告 linear residualization 下 3/4 模型保留显著性。HS advantage 并非完全被 position 解释——linear vs. quadratic 的差异暗示位置效应可能是非线性的，而非 HS 信号不存在。论文如果能更明确地讨论 \"linear sufficient\" vs. \"quadratic needed\" 的含义（是过拟合 quadratic 还是真实非线性 confound），会更有说服力。\n\n---\n\n**[AGREE] R1-N3: Cosine compression 因果链缺直接证据**\n\n完全同意，这与我的 W1 一致。R1 将其升级为 Must-Fix 是合理的，因为论文 Abstract 使用了 \"The mechanism is cosine compression\" 这样的因果措辞。\n\nR1 提出的两个反事实实验都很精准：\n- (a) 归一化 cosine distance 后重新计算 crossing-rate，观察 layer selection discrepancy 是否消失；\n- (b) 人为压缩深层表征，观察 CR-composite 是否转移到深层。\n\n我补充一个额外观察：论文 Section A.1 (p12) 的 random-label decomposition 显示 \"100% of random-label repeats still select layers L0-L1\"，论文将此解释为 \"crossing-rate shallow-layer preference is label-independent\"。R1 正确指出这只证明了偏置与标签无关，**不证明 cosine compression 是该偏置的原因**。替代解释包括：浅层的 lower-rank structure、浅层更接近 input embedding 的 token-level patterns 等。\n\n综合两位 reviewer 的意见，我认为这是本文最关键的方法论缺陷。建议要么：(1) 补充归一化实验提供因果证据；(2) 将 \"mechanism\" 措辞改为 \"geometric correlate\" 或 \"candidate mechanism\"。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: AdvBench 仅验证 C1 未验证 C2**\n\n同意。Section B.1-B.2 (p14) 在 AdvBench 上复现了 metric-induced layer selection bias (C1)：CR-composite 选浅层 (median L2), precision 选深层 (median L14)。但 HS vs. text 的优势对比（C2 的核心）**仅在 HarmThoughts 数据集上完整报告**（Table 4, Section 4.3）。\n\nSection B.2 (p14) 报告了 AdvBench layer selection 的 bootstrap validation，但验证的是 \"layer selection 在 AdvBench 上是否 consistent\"（是的——仍然是 metric-induced bias），而非 \"HS 在 correct layer 上是否优于 text\"。这是一个重要区分：C1（bias 存在）和 C2（在 correct layer 上 HS 有优势）是两个独立 claim，后者的外部验证更弱。\n\n---\n\n**[AGREE] R1-W2: 两阶段设计探索自由度**\n\n部分同意。论文确实有一定的 mitigation：Section V（Hyperparameter Robustness）和 Section X.2（Effective Independent Tests）尝试量化探索空间的有效维度。Section X.2 (p29) 报告 \"the effective number of independent tests is far smaller than the raw exploration space\" 并讨论了 metric redundancy 和 layer autocorrelation 导致 effective tests 远小于 980-2,240 configurations。\n\n但 R1 的核心担忧仍然成立：**layer 和 window 的选择基于 validation set，而最终评估也在同一分布的 test set 上进行**。Table 34 的 13-25% shrinkage 是这种 optimism 的直接量化。虽然论文做了 5-fold LOO-CV (Section A, p12) 和 leave-one-out stability analysis (Section A)，但未采用真正的 nested cross-validation（即 inner loop 选参数、outer loop 评估）。\n\n建议在 Limitations 中更明确地承认这一 design choice 的后果。\n\n---\n\n**[AGREE] R1-W3: 32B n=19-20 统计推断限制**\n\n同意。这与我的 W3 一致。论文自身在 Section 4 (p4) 承认 \"BCa confidence intervals are reported for comparability but may have reduced coverage at these sample sizes\"。\n\n补充：Section A (p12) 报告 LOO-CV 在 32B 模型上的 fold stability——\"layer selection instability is particularly acute at small sample sizes\"，R1-32B 和 QwQ-32B 的 dominant layer 仅在 65-68% 的 folds 中被选中（vs. R1-8B 的 100%）。这直接印证 R1 的担忧。\n\n---\n\n**[AGREE] R1-W4: Ensemble holdout 估计的选择偏置**\n\n同意。Table 3 (p5) 的 ensemble 由 precision-best, balanced-accuracy-best, inverse-FPR-best 三个 metric 的预测平均构成——这三个 metric 和对应的层都在 validation set 上选定。然后 ensemble 在同一分布的 test folds 上评估。这构成了 selection bias：ensemble 的组成本身是 data-driven 的，却在同源数据上评估 \"是否优于 single metric\"。\n\nR1 引用 Table 34 的 13-25% shrinkage 是对这种 optimism 的定量证据。论文的 Level 3 recommendation（use ensemble）因此缺乏严格的 out-of-distribution 验证。\n\n---\n\n### 总结\n\n我与 R1 在所有 7 个问题上 **全部 AGREE**。R1 的 N1（1 Llama + 3 Qwen）和 N2（position confound + power confound）比我的初始审查更精确。R1 的 N3 与我的 W1 重合，但 R1 将其升级为 Must-Fix 是合理的，因为 Abstract 使用了因果措辞。\n\n两位 reviewer 的共识是：\n1. **架构多样性不足**（R1-N1 ≈ R2-N2）\n2. **Cosine compression 因果证据缺失**（R1-N3 ≈ R2-W1）\n3. **32B 结果弱 + position confound**（R1-N2 ≈ R2-W3）\n4. **\"Cross-architecture\" 过度声称**（R1-N1 ≈ R2-N2）\n\n这些共识问题指向 Findings 而非 Main Conference 的定位。\n\n我维持 **Overall 3.0 (Findings)** 的评分不变。",
    "reviewer_id": "2",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 3396 · 2026-05-25T21:27:28.274414+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4769
}
```

</details>

---


### Assistant

_source line 3397 · 2026-05-25T21:27:34.934962+00:00_

交叉回应已提交。与 Reviewer 1 的 7 个问题全部 AGREE，核心共识集中在：架构多样性不足（1 Llama + 3 Qwen）、cosine compression 缺因果验证、32B 结果受 position confound 和小样本限制。维持 Overall 3.0 (Findings) 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2"
}
```

</details>

---
