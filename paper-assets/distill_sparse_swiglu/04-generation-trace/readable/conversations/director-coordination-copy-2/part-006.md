# Director coordination — Part 6 of 8

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 7 →](part-007.md) · [Structured JSON](../../../sessions/e0/e0d2e26e51128e828a96.json)

## Round 146

### Tool call

_source line 1718 · 2026-05-22T13:10:42.034222+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每一条 Weakness/Question，用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿报告\n\n**Overall**: 3 (Findings), Confidence 4/5\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n\n### 主要优势\nS1. 新颖且 well-motivated 的问题框架（per-neuron BCE → output-distribution KL），forward KL mode-covering 在 false-negative 不对称场景有理论基础。2D taxonomy (Table 1) 有用。\nS2. 全面且诚实的消融实验——Table 4 覆盖 8 种配置，不利结果如实报告。\nS3. C1 target-swap ablation 设计有创意——3 种子 ≤1.70pp 一致性。\nS4. 跨架构验证——Mistral-7B (3-seed) 和 Qwen-2.5-14B PPL advantage ratio 一致。\nS5. 训练效率高——单 GPU ~45min，predictor <1% 参数。\n\n### Must-Fix 问题\n**N1** [Critical] 无 wall-clock 加速——6.4% overhead，unstructured masks 无 speedup。\n**N2** [Critical] Per-layer KL \"97.5% signal type\" 基于 confounded K=1 设置（训练 mask 1/32 层 vs 推理 32 层）。K=4 pilot 仅 single-seed，MMLU K=4 超过 E2E KL（43.5 vs 40.7±1.3），GSM8K 负向 gap closure（-6.8%）——反常结果未排除。\n**N3** [Major] MMLU/GSM8K 系统性退化跨 8B/14B 两 scale、LLaMA/Qwen 两架构，但 framing 偏重 PPL。Abstract/Intro 以 PPL 为主叙事，下游 trade-off 在 Conclusion 以 \"task- and scale-dependent\" 一笔带过。\n\n### Should-Fix 问题\n**W1** [Major] C1 的 trajectory confound——oracle masks 从特定 KL trajectory 提取，s42 oracle 来自 earlier training run。C1 证明 masks 可 transfer 但未证明 KL 是发现好 masks 的唯一/最佳途径。\n**W2** [Major] 训练/评估域重叠——WikiText-103→WikiText-2 同 Wikipedia。C4 OOD 31× 更高 cross-seed variance。\n**W3** [Minor] MSE baseline 可能未公平调参——seed 123 灾难性失败（PPL=15,789, 5.1% sparsity）。\n**W4** [Minor] Global allocation 30% MMLU σ=9.5pp 不可解读。\n**W5** [Minor] 符号冲突——g^(ℓ) 在 Eq.(1) 为 gate activation，Eq.(4) 中 g1/g2 为 Gumbel noise。\n\n### Questions\nQ1. K=4 是否有多种子数据？MMLU 超 E2E 是否系统性？\nQ2. 有没有尝试 per-layer sparsity 约束缓解 L22-L28 过度修剪？\nQ3. 补偿对 BCE predictor 效果如何？\"compensation provides no benefit\" 可能仅因 KL 自带补偿。\nQ4. 更大/更多样训练集是否缓解 OOD variance？\n\n### Missing References\nGriffin et al. 2024, Mirzadeh et al. 2024 (ReLU-fication), Wanda 互补性讨论。\n\n---\n\n请对以上每条 N/W/Q 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每一条 Weakness/Question，用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿报告\n\n**Overall**: 3 (Findings), Confidence 4/5\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n\n### 主要优势\nS1. 新颖且 well-motivated 的问题框架（per-neuron BCE → output-distribution KL），forward KL mode-covering 在 false-negative 不对称场景有理论基础。2D taxonomy (Table 1) 有用。\nS2. 全面且诚实的消融实验——Table 4 覆盖 8 种配置，不利结果如实报告。\nS3. C1 target-swap ablation 设计有创意——3 种子 ≤1.70pp 一致性。\nS4. 跨架构验证——Mistral-7B (3-seed) 和 Qwen-2.5-14B PPL advantage ratio 一致。\nS5. 训练效率高——单 GPU ~45min，predictor <1% 参数。\n\n### Must-Fix 问题\n**N1** [Critical] 无 wall-clock 加速——6.4% overhead，unstructured masks 无 speedup。\n**N2** [Critical] Per-layer KL \"97.5% signal type\" 基于 confounded K=1 设置（训练 mask 1/32 层 vs 推理 32 层）。K=4 pilot 仅 single-seed，MMLU K=4 超过 E2E KL（43.5 vs 40.7±1.3），GSM8K 负向 gap closure（-6.8%）——反常结果未排除。\n**N3** [Major] MMLU/GSM8K 系统性退化跨 8B/14B 两 scale、LLaMA/Qwen 两架构，但 framing 偏重 PPL。Abstract/Intro 以 PPL 为主叙事，下游 trade-off 在 Conclusion 以 \"task- and scale-dependent\" 一笔带过。\n\n### Should-Fix 问题\n**W1** [Major] C1 的 trajectory confound——oracle masks 从特定 KL trajectory 提取，s42 oracle 来自 earlier training run。C1 证明 masks 可 transfer 但未证明 KL 是发现好 masks 的唯一/最佳途径。\n**W2** [Major] 训练/评估域重叠——WikiText-103→WikiText-2 同 Wikipedia。C4 OOD 31× 更高 cross-seed variance。\n**W3** [Minor] MSE baseline 可能未公平调参——seed 123 灾难性失败（PPL=15,789, 5.1% sparsity）。\n**W4** [Minor] Global allocation 30% MMLU σ=9.5pp 不可解读。\n**W5** [Minor] 符号冲突——g^(ℓ) 在 Eq.(1) 为 gate activation，Eq.(4) 中 g1/g2 为 Gumbel noise。\n\n### Questions\nQ1. K=4 是否有多种子数据？MMLU 超 E2E 是否系统性？\nQ2. 有没有尝试 per-layer sparsity 约束缓解 L22-L28 过度修剪？\nQ3. 补偿对 BCE predictor 效果如何？\"compensation provides no benefit\" 可能仅因 KL 自带补偿。\nQ4. 更大/更多样训练集是否缓解 OOD variance？\n\n### Missing References\nGriffin et al. 2024, Mirzadeh et al. 2024 (ReLU-fication), Wanda 互补性讨论。\n\n---\n\n请对以上每条 N/W/Q 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1719 · 2026-05-22T13:10:43.492846+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1458
}
```

</details>

---


### Assistant

_source line 1720 · 2026-05-22T13:10:46.223385+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 147

## Round 147

2 recorded events


### User

_source line 1721 · 2026-05-22T13:10:48.916388+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**总结**：给出 Overall 3.0 (Findings)，Soundness 3.5，Excitement 2.5。主要问题：(1) 与 MaskLLM 的 recipe 新颖性区分不足（2 个 critical）；(2) 无实际 wall-clock 加速；(3) "97.5% signal type" 基于非正交分解存在 overclaim；(4) K=4 pilot 单 seed 但结论被推广。优势在于 target-swap ablation 设计精巧、多 seed 评估严谨、写作诚实。格式合规无问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1722 · 2026-05-22T13:10:53.975166+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 148

## Round 148

2 recorded events


### User

_source line 1723 · 2026-05-22T13:12:31.025802+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 无 wall-clock 加速**
同意这是 critical 问题。与我的 N2 一致。论文在 Appendix A 承认 unstructured masks 无法转化为 speedup（Table 5: +6.4% overhead），但这个 disclaimer 在正文中过于隐蔽（Introduction 倒数第二段括号内）。对于以 "sparsity prediction" 为核心的论文，无法展示 end-to-end 效率收益是硬伤。不过需要注意：论文自我定位为 "primarily an empirical study"（Section 1 倒数第二段），如果这一定位更加前置和显著，该问题的 severity 可以部分降低。

**[AGREE] R1-N2: 97.5% signal type 基于 confounded 设置**
同意。与我的 W1 一致。补充两点：
1. Per-layer KL (K=1) 训练时只 mask 1/32 层但推理时 apply 全部 32 层，这个 train-inference mismatch 本身就是一个 confound——不能将 per-layer KL vs. E2E KL 的 gap 纯粹归因于 coupling scope。论文在 Section 4.5 脚注中承认 "signal type and coupling scope are not fully orthogonal"，但 Abstract 和 Conclusion 中引用 97.5% 时没有任何 caveat。
2. K=4 的 MMLU 异常（43.5 vs. E2E 40.7±1.3）和 GSM8K 负向 gap closure (-6.8%) 确实是 red flags。Table 17 (Appendix R) 注释说 "interpret cautiously"，但这种 hedging 在 Abstract/Conclusion 中消失了——"reveals task-dependent downstream structure" 作为 headline finding 过于自信。

**[AGREE] R1-N3: 下游回退 framing 偏重 PPL**
同意这是 major concern，但 severity 可从 Critical 降为 Major。理由：
- Abstract 确实提到 "commonsense gains but knowledge-intensive decline"（第 3 行）
- Section 4.2 "Task-Type Split" 段落完整报告了 MMLU/GSM8K 的回退
- Limitations 第二点 "Knowledge-intensive regression" 明确承认跨 scale 的系统性问题

但 R1 的核心批评成立：Conclusion 的 "task- and scale-dependent" 措辞过于模糊，回避了 "KL 在 knowledge tasks 上输给 training-free baseline" 这一尖锐事实。Introduction 的叙事以 PPL 改善为主线（"reduces perplexity by 14.5%"），下游 trade-off 被压缩在列表第一项的子句中。建议将 Conclusion 改为更 balanced 的双面叙事。

---

### Should-Fix 问题

**[AGREE] R1-W1: C1 trajectory confound**
同意，但认为论文已 partially address。Appendix O (Oracle Mask Provenance) 明确讨论了 trajectory 依赖问题："C1's oracle masks are extracted from a converged KL predictor and binarized via hard threshold...The s42/s123/s456 consistency (≤1.70pp) provides partial evidence of robustness, but does not rule out trajectory-dependent confounds." 3-seed 一致性（Table 3: max Δ≤1.70pp at 30%）是一定程度的 evidence，但 R1 的核心论点成立：C1 证明好 masks 可 transfer，但没有证明 KL 是发现好 masks 的 *唯一* 途径。可能存在其他方法（如 evolutionary search、reinforcement learning）也能发现类似质量的 masks。这不影响论文的核心 finding（mask quality drives performance），但限制了 "KL 作为 discovery mechanism" 这一 claim 的 strength。

**[AGREE] R1-W2: 训练/评估域重叠**
同意。与我的 Q4 一致。WikiText-103 和 WikiText-2 都源自 Wikipedia，PPL 改善可能部分来自 in-domain 优势。C4 OOD 评估（Appendix C, Table 10）虽然保持了 KL 优势（52.5% advantage at 50%），但 cross-seed variance 急剧增大（CV 6.3% vs. 0.2%），且 seed 42 的 C4 PPL 异常偏高（18.22 vs. 其他 seed 16.37），暗示 predictor 对训练域有一定 overfitting。

**[REBUT] R1-W3: MSE baseline 未公平调参**
部分反驳。论文在 Appendix F 中详细说明了 MSE 的配置：与 KL/BCE 使用完全相同的架构、数据、优化器、Gumbel-Sigmoid relaxation，仅 loss function 不同。λ_max 设为 1000（vs. KL 的 5000）是因为 MSE 的 per-layer gradient magnitude 约 5× 大于 KL 的 end-to-end gradient，这是合理的工程调整而非不公平。Seed 123 的灾难性失败（PPL=15,789, 5.1% sparsity）恰恰说明 MSE loss 的 *内在不稳定性*——KL loss 在相同条件下 3-seed σ=0.02，而 MSE σ=1.68。这种 initialization sensitivity 本身就是一个有意义的 finding，而非调参不足的证据。但 R1 有一定道理：论文没有报告对 MSE 做 λ_max grid search 的尝试，无法排除更好的 λ_max 能部分缓解问题。

**[REBUT] R1-W4: Global allocation MMLU σ=9.5pp 不可解读**
反驳。论文的处理方式恰当：
1. Table 2 同时报告了 global (σ=9.5pp) 和 uniform (σ=1.3pp) 两种 allocation 的 MMLU
2. Section 4.2 明确解释了 global 高 variance 的来源——late-layer starvation (L31 retention 28.4%)
3. Appendix J (Table 14) 展示了完整的 allocation 对比，30% 时推荐 uniform
4. 高 variance 本身是一个 informative finding：它揭示了 global allocation 在 moderate sparsity 下的不稳定性

论文没有用 global 30% MMLU 作为 headline number——Table 2 的 bold 标记在 MMLU 列给了 TEAL (45.86)，KL uniform 40.7±1.3 作为稳定替代。R1 的 concern 更多是 presentation 问题，非 soundness 问题。

**[AGREE] R1-W5: 符号冲突 g^(ℓ) vs. g1/g2**
同意。Eq.(1) 的 g^(ℓ) 表示 gate activation，Eq.(4) 的 g1, g2 表示 Gumbel noise samples。虽然上下标不同（上标 ℓ vs. 下标 1/2），但 g 作为 base symbol 在同一篇论文中有两种含义确实影响可读性。建议将 Gumbel noise 改为 ε1, ε2 或 ξ1, ξ2 以消除歧义。这是 minor fix。

---

### Questions

**[AGREE] R1-Q1: K=4 多种子数据**
与我的 W2 和 Q3 一致。K=4 单 seed 的 MMLU 异常（43.5 > E2E 40.7±1.3）很可能是噪声。需要至少 3-seed K=4 数据才能判断这是系统性的还是随机的。

**[AGREE] R1-Q2: Per-layer sparsity 约束**
与我的 W4 建议一致。如果 late-layer over-pruning (L22-L28 at 48-57%, Appendix T, Table 20) 是 MMLU/GSM8K 回退的原因，per-layer sparsity cap（如 max 35%）是最直接的验证手段。论文未尝试这一自然实验是一个遗憾。

**[AGREE] R1-Q3: 补偿对 BCE 效果**
这是一个很好的问题，我在初审中遗漏了。论文报告 "compensation provides no benefit"（Section 4.5），但从 exp_id 看（kl_comp_30_s42, kl_comp_50_s42, bce_comp_staged_s42），似乎有做过 BCE+compensation 的实验。然而结果未在正文或附录中单独报告。如果 BCE+compensation 能显著缩小与 KL 的 gap，论文的核心论点（KL 的 mask quality 使 compensation 冗余）就需要重新审视：可能不是 KL masks 本身好到不需要 compensation，而是 BCE masks 差到 compensation 也救不了。两种解读有本质区别。

**[AGREE] R1-Q4: 更多样训练集**
与我的 Q4 一致。C4 subsample 或 mixed-domain 训练是降低 OOD variance 的自然尝试。

---

### Missing References

**[REBUT] Griffin et al. 2024**: Griffin (De et al., 2024) 提出 gated linear recurrence 架构，与本文研究的 SwiGLU FFN activation sparsity 关联较弱。Griffin 的 sparsity 来自架构设计而非 post-hoc prediction，与本文方法论正交。不认为缺失此引用构成 weakness。

**[REBUT] Mirzadeh et al. 2024 (ReLU Strikes Back)**: 论文已在 Related Work Section 2 "Activation Function Engineering" 段落中引用并讨论了此工作（"ReLU Strikes Back (Mirzadeh et al., 2024) replaces SiLU with ReLU for >90% natural sparsity"）。R1 可能遗漏了这一引用。

**[AGREE] Wanda 互补性讨论**: 论文在 Related Work 提及 Wanda（Section 2 "Weight Pruning, Distillation, and Routing"），但仅作为 weight pruning 方法列举。Wanda 的 activation-aware weight selection 与本文的 activation sparsity prediction 有方法论上的关联（都利用 activation magnitude 作为 importance signal），补充讨论两者的互补性是合理的。

---

### 总结

R1 的审稿整体公正且 well-calibrated。我们在 N1（无加速）、N2（97.5% confound）、N3（framing 偏重 PPL）上完全一致。我对 W3（MSE 调参公平性）和 W4（global MMLU variance）有部分反驳，认为论文的处理并非不合理。R1 的 Q3（BCE+compensation）是我初审遗漏的有价值问题。

综合 R1 意见后，我维持 **Overall 3.0 (Findings)** 的评分不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1724 · 2026-05-22T13:12:35.966618+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 149

## Round 149

10 recorded events


### User

_source line 1725 · 2026-05-22T13:12:39.830178+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

### Must-Fix

[AGREE] R2-N1: MaskLLM recipe 重合。核心技术组件（KL+Gumbel+frozen model）确实与 MaskLLM 高度重合。论文更接近 empirical study（Introduction 自承），方法创新有限。

[AGREE] R2-N2: 无 wall-clock 加速。与我的 N1 一致，+6.4% overhead 是最根本的实践性缺陷。

### Should-Fix

[AGREE] R2-W1: "97.5% signal type" 非正交分解。与我的 N2 一致，Abstract/Conclusion 缺乏 caveat。

[AGREE] R2-W2: K=4 单 seed。与我的 N2 一致，MMLU 43.5 > E2E KL 40.7±1.3 的反常结果在单 seed 下无法排除随机波动。

[REBUT] R2-W3: Sparsity mismatch。论文处理审慎——Table 2 脚注标注差异，Abstract 用 matched 14.5% 而非 main table 19%，Appendix C 补充了 TEAL@28.5% 的 PPL。0.8pp 差异不改变定性结论。但同意应在正文中更显著讨论。

[AGREE] R2-W4: Late-layer over-pruning 归因缺因果验证。仅 correlational 证据，缺 per-layer sparsity constraint 的 interventional 实验。与我的 Q2 一致。

[REBUT] R2-W5: 缺 R-Sparse/CATS/FastForward 完整 pipeline 对比。论文控制变量比较训练目标（KL vs BCE vs MSE），R-Sparse/CATS 架构不同会混淆变量。FastForward 补偿已在 §4.5 测试。但同意补充参考数字会增强 positioning。

### 小问题

[AGREE] M1, M2, M4。[REBUT] M3: taxonomy table 价值在概念框架而非信息密度。

### Questions

[AGREE] Q1-Q4 均为合理问题。

### 两位 Reviewer 共识

核心弱点：(1) 无 wall-clock 加速；(2) K=4 pilot underpowered 导致 97.5% claim 不可靠；(3) 知识任务退化归因缺因果验证。Overall 维持 3 (Findings)。

---

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 的逐条回应。

核心共识：N1（无加速）、N2（97.5% confound）、N3（framing 偏 PPL）三个 critical/major 问题我与 R1 完全一致。两个部分反驳：W3（MSE baseline 的配置差异有工程合理性，seed 不稳定本身是 finding）和 W4（global MMLU 高 variance 的报告方式实际上是 informative 的）。采纳了 R1 的 Q3（BCE+compensation 未单独报告）作为我初审遗漏的有效问题。维持 Overall 3.0 不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1726 · 2026-05-22T13:12:56.684056+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1727 · 2026-05-22T13:12:58.091767+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T13:03:05.532701+00:00\", \"completed_at\": \"2026-05-22T13:03:09.130256+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 6pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool call

_source line 1728 · 2026-05-22T13:12:58.293226+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml",
  "description": "Read current review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml",
    "description": "Read current review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1729 · 2026-05-22T13:12:58.495362+00:00_

issues:
  # ============================================================
  # Round 20 — Active issues
  # ============================================================

  - id: "R19-N3"
    summary: "无实际 wall-clock 加速: +6.4% overhead, Intro 仍有 efficiency motivation 残留"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 16
    last_seen_round: 20
    mentions:
      - {round: 16, reviewers: [1, 2], note: "首次提出。"}
      - {round: 18, reviewers: [1, 2], note: "Introduction 仍以 efficiency 动机展开。"}
      - {round: 19, reviewers: [1, 2], note: "Table 5 +6.4% overhead, Intro 暗示 efficiency gain。"}
      - {round: 20, reviewers: [1, 2], note: "[AGREE] R20-N1 Critical。§1 L3 仍有 'potential inference acceleration'。R19 Paper Agent 漏掉此处。"}
    action_items:
      - {round: 19, action: "Paper Agent: Intro 去掉 efficiency motivation", assigned_to: "paper_agent", status: done}
      - {round: 20, action: "Paper Agent: 彻底清除 intro L3 'potential inference acceleration' + 全文搜索残留", assigned_to: "paper_agent", status: done}
    resolution: "Intro L3 efficiency 残留已清除，全文无 efficiency motivation 残留。"
    resolution_round: 21

  - id: "R20-N2"
    summary: "MMLU/GSM8K 跨三个架构系统性退步未解释 (8B -5.2pp, 14B -8.1pp/-20pp, Mistral -7.3pp)"
    category: experiment
    severity: critical
    status: in_progress
    first_raised_round: 18
    last_seen_round: 20
    mentions:
      - {round: 18, reviewers: [1, 2], note: "R18-W8。14B 仅 30% sparsity。"}
      - {round: 19, reviewers: [1, 2], note: "R19-W2/W3。GSM8K -20pp σ=5.2pp。"}
      - {round: 20, reviewers: [1, 2], note: "[AGREE] 升级为 Critical。跨三架构一致。如果 KL 在 MMLU/GSM8K 劣于零训练成本的 TEAL, 实用价值存疑。"}
    action_items:
      - {round: 19, action: "Paper Agent: 14B 失败模式分析, reframe as finding", assigned_to: "paper_agent", status: done}
      - {round: 20, action: "Agent: 提取 per-layer predicted sparsity rate 分析机制", assigned_to: "main_agent", status: done}
      - {round: 20, action: "Paper Agent: §4.2 从假设升级为数据支撑的分析 (protection valley
…[truncated 11072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 1730 · 2026-05-22T13:17:50.326536+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 21 — Active issues\n  # ============================================================\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无 speedup\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 21\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"首次提出。\"}\n      - {round: 18, reviewers: [1, 2], note: \"Introduction 仍以 efficiency 动机展开。\"}\n      - {round: 19, reviewers: [1, 2], note: \"Table 5 +6.4% overhead, Intro 暗示 efficiency gain。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] R20-N1 Critical。§1 L3 仍有 'potential inference acceleration'。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R21 fresh review 再次标 Critical。Intro framing 已修改为 empirical study, 但 disclaimer 位于括号内过于隐蔽。根本问题(无实际加速)仍是最大实践性缺陷。R2 补充: 效率价值完全依赖未来 sparse kernel 支持。\"}\n    action_items:\n      - {round: 19, action: \"Paper Agent: Intro 去掉 efficiency motivation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 20, action: \"Paper Agent: 彻底清除 intro L3 'potential inference acceleration'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 21, action: \"Paper Agent: 将 'empirical study' 定位前移到 Abstract/§1 首段; wall-clock disclaimer 从括号提升到正文\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"Framing 已部分修复(efficiency motivation 清除), 但 disclaimer 位置仍隐蔽, 根本问题(无 speedup)无法通过写作修复。\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨三个架构系统性退步 (8B -5.2pp, 14B -20pp GSM8K, Mistral tied)\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 21\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W8。14B 仅 30% sparsity。\"}\n      - {round: 19, reviewers: [1, 2], note: \"R19-W2/W3。GSM8K -20pp σ=5.2pp。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 升级为 Critical。跨三架构一致。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-N3 Major + R2-W4 minor-to-major。Protection valley 分析(L14-L18)仅为 correlational, 未通过 per-layer constraint 做 interventional 验证。Conclusion 'task- and scale-dependent' 措辞过于模糊。\"}\n    action_items:\n      - {round: 19, action: \"Paper Agent: 14B 失败模式分析, reframe as finding\", assigned_to: \"paper_agent\", status: done}\n      - {round: 20, action: \"Agent: 提取 per-layer predicted sparsity rate 分析机制\", assigned_to: \"main_agent\", status: done}\n      - {round: 20, action: \"Paper Agent: §4.2 从假设升级为数据支撑的分析 (protection valley)\", assigned_to: \"paper_agent\", status: done}\n      - {round: 21, action: \"Agent: per-layer sparsity constraint 实验(如 late-layer ≤35%)验证因果链\", assigned_to: \"main_agent\", status: open}\n      - {round: 21, action: \"Paper Agent: Conclusion 将 'task- and scale-dependent' 改为明确陈述 'KL underperforms TEAL on MMLU/GSM8K across all tested scales'\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL train-inference mismatch confounds 2D 分解; 97.5% signal type 为 confounded upper bound\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] downstream 24-35% coupling 可能主要来自 mismatch。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-N2 Critical + R2-W1/W2 Major。97.5% 在 Abstract/Conclusion 无 caveat 是 overclaim。K=4 pilot 仅 single-seed, MMLU 43.5>E2E 40.7±1.3 和 GSM8K -6.8% gap closure 为 red flags。Abstract 'reveals task-dependent downstream structure' 对单种子结果过于自信。\"}\n    action_items:\n      - {round: 20, action: \"Agent: K=4 per-layer KL pilot 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 20, action: \"Paper Agent: §4.5 coupling 改为 upper bound + mismatch caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 21, action: \"Abstract/Conclusion 中 '97.5%' 加 '(upper bound; dimensions not orthogonal)' caveat\", assigned_to: \"paper_agent\", status: open}\n      - {round: 21, action: \"Abstract/Conclusion 中 K=4 findings 加 '(single seed, preliminary)' 标注\", assigned_to: \"paper_agent\", status: open}\n      - {round: 21, action: \"Agent: K=4 补充至少 2 个额外 seed (s123, s456)\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分不足: KL+Gumbel+frozen model 配方高度重合\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 21\n    mentions:\n      - {round: 16, reviewers: [2], note: \"R2 首次提出。\"}\n      - {round: 18, reviewers: [1, 2], note: \"R18-W1。\"}\n      - {round: 19, reviewers: [1, 2], note: \"R19-W1。R2 Critical, R1 REBUT。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[分歧] R2-N1 Critical, R1 REBUT。Director 判定 Warning。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R2-N1 Critical + R1 交叉 AGREE。fresh review 两位 reviewer 均认为 recipe overlap 是 critical concern。论文已承认 'shares the recipe-level principle' 但未在实验中量化 activation sparsity 设定下的差异。\"}\n    action_items:\n      - {round: 19, action: \"Paper Agent: 贡献重新定位为分析框架\", assigned_to: \"paper_agent\", status: done}\n      - {round: 20, action: \"Paper Agent: §2 承认配方相似 + 强调 first decomposition\", assigned_to: \"paper_agent\", status: done}\n      - {round: 21, action: \"Paper Agent: §1/§3 更明确论证 dynamic activation sparsity vs static N:M 的本质差异(generalization, per-token variability, global allocation 交互)\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD cross-seed variance 31×\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"WikiText-103→WikiText-2 同分布。C4 30% OOD 仅 2-seed global。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-W2 Major + R2 Q4。C4 CV 6.3% vs in-domain 0.2%, seed 42 异常偏高(18.22 vs 16.37)。暗示 predictor 对训练域有 overfitting。\"}\n    action_items:\n      - {round: 20, action: \"Paper Agent: Limitations 加 WikiText 同分布 + C4 限制\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W4\"\n    summary: \"MSE baseline 50% sparsity seed 123 灾难性失败(PPL=15,789, 5.1% sparsity)\"\n    category: experiment\n    severity: info\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 21\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W5。\"}\n      - {round: 19, reviewers: [1, 2], note: \"R19-W4 Major。\"}\n      - {round: 20, reviewers: [1, 2], note: \"R20-W5 Warning。severity 下降。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[分歧] R1-W3 Minor(调参不公平), R2 REBUT(instability 是 finding, λ_max=1000 工程合理)。Director 判定 Info—— Appendix F 配置充分, 但缺 λ_max grid search。\"}\n    action_items:\n      - {round: 19, action: \"Paper Agent: Table 4 footnote about s123 failure\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap ablation trajectory confound\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"R19-N2 Critical。循环论证 + soft-vs-hard confound。\"}\n      - {round: 20, reviewers: [1, 2], note: \"R20-W3 Major→Warning。reframe 部分有效。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-W1 Major。3-seed 一致性(≤1.70pp)提供部分 robustness, 但未证明 KL 是发现好 masks 的唯一途径。论文已用 'suggests' 替代 'confirms'——hedging 改善被认可。\"}\n    action_items:\n      - {round: 19, action: \"Paper Agent: reframe 为 transferability + circularity caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 20, action: \"Paper Agent: 'confirms'→'suggests' 全文替换\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Hedging 改善(suggests)被 R21 认可。根本 confound 无法通过写作消除, 但 severity 持续下降。\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Actual sparsity mismatch (KL 28.5% vs TEAL 29.3%) 在主表不够显著\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 21\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W6。\"}\n      - {round: 19, reviewers: [1, 2], note: \"R19-W6 Minor。\"}\n      - {round: 20, reviewers: [1, 2], note: \"R20-W6 Info。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[分歧] R2-W3 Major(Abstract/主表数字不一致), R1 REBUT(处理审慎)。Director 判定 Minor→Info。footnote + matched-sparsity appendix 信息完整。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot 限制实际影响\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"R19-W7 Info。\"}\n      - {round: 20, reviewers: [1, 2], note: \"R20-W7 Info。Limitations 已讨论。\"}\n      - {round: 21, reviewers: [], note: \"本轮未显式提出, 但隐含于 MMLU/GSM8K 退化讨论中。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 21 — New issues\n  # ============================================================\n\n  - id: \"R21-W1\"\n    summary: \"缺少 R-Sparse/CATS 等同类 baseline 的实验对比\"\n    category: experiment\n    severity: minor\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - {round: 21, reviewers: [2], note: \"R2-W5 Minor。论文仅 TEAL/BCE/MSE baseline, 缺 R-Sparse/CATS/FastForward 完整 pipeline。R1 partial REBUT: 控制变量比较训练目标, 架构差异会混淆。Director: Minor。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W2\"\n    summary: \"符号冲突: g^(ℓ) (gate activation, Eq.1) vs g1/g2 (Gumbel noise, Eq.4)\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-W5 Minor。建议将 Gumbel noise 改为 ε1, ε2 或 ξ1, ξ2。\"}\n    action_items:\n      - {round: 21, action: \"Paper Agent: Eq.(4) Gumbel noise g1/g2 → ε1/ε2\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W3\"\n    summary: \"Figure 2 仅展示 global allocation 但 30% 结论推荐 uniform\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - {round: 21, reviewers: [2], note: \"R2-M4 Minor。图表与结论 allocation 策略不一致。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Earlier rounds — Resolved (unchanged)\n  # ============================================================\n\n  - id: \"R20-N3\"\n    summary: \"'Coupling alignment' 术语已替换为 'output-distribution alignment'; 97.5% 标注为 upper bound\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"'coupling alignment' conflates signal type 和 coupling mechanism。\"}\n      - {round: 21, reviewers: [], note: \"术语问题未被 R21 reviewer 提出(已修复)。但 97.5% caveat 在 §4.5 脚注中存在, Abstract/Conclusion 中仍缺——衍生为 R20-W1 的一部分。\"}\n    action_items:\n      - {round: 20, action: \"Paper Agent: 全文替换 + 标注 upper bound\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"术语替换完成。97.5% 在 §4.5 有 caveat 但 Abstract/Conclusion 缺——见 R20-W1。\"\n    resolution_round: 21\n\n  - id: \"R20-W9\"\n    summary: \"Batched inference 对 contextual sparsity 的影响完全未讨论\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] mask 在 batch 内需取交集。\"}\n      - {round: 21, reviewers: [], note: \"R21 未提出。Limitations 已包含。\"}\n    action_items:\n      - {round: 20, action: \"Paper Agent: Limitations 加 batched inference\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Limitations 已加 batched inference 讨论。\"\n    resolution_round: 21\n\n  - id: \"R20-W10\"\n    summary: \"Abstract 'universally use BCE' → 'predominantly'\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"不准确。\"}\n      - {round: 21, reviewers: [], note: \"R21 未提出。已修复。\"}\n    action_items:\n      - {round: 20, action: \"'universally' → 'predominantly'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"已修复。\"\n    resolution_round: 21\n\n  - id: \"R19-F1\"\n    summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"已删除。R20/R21 未再提出。\"\n    resolution_round: 20\n\n  - id: \"R19-N1\"\n    summary: \"97.5% signal-type 归因缺乏 downstream 定量分解\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    resolution: \"Downstream 2D 分解已落地。衍生问题见 R20-W1。\"\n    resolution_round: 20\n\n  - id: \"R19-W5\"\n    summary: \"'hierarchy' → 'ranking' 术语降级\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    resolution: \"已修复。R21 未提出。\"\n    resolution_round: 20\n\n  - id: \"R19-W3\"\n    summary: \"Knowledge-intensive 任务退步缺乏机制解释\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 21\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W3。\"}\n      - {round: 19, reviewers: [1, 2], note: \"R19-W3 Major。\"}\n      - {round: 20, reviewers: [1, 2], note: \"合并进 R20-N2。\"}\n      - {round: 21, reviewers: [1, 2], note: \"仍存在。protection valley 分析为 correlational, 缺 interventional 验证。见 R20-N2。\"}\n    action_items:\n      - {round: 20, action: \"见 R20-N2 action items\", assigned_to: \"main_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W4\"\n    summary: \"Per-layer KL 对照实验缺失\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    resolution: \"Per-layer KL 3-seed 完成。\"\n    resolution_round: 19\n\n  - id: \"R18-W7\"\n    summary: \"Cross-seed Jaccard 未报告\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    resolution: \"Appendix 已补充。\"\n    resolution_round: 19\n\n  - id: \"R16-N1\"\n    summary: \"多种子覆盖不一致\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 19\n    resolution: \"所有关键行均为 3-seed。\"\n    resolution_round: 19\n\n  - id: \"R16-VIS1\"\n    summary: \"正文溢出到第9页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"正文 8 页合规。\"\n    resolution_round: 17\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界不够清晰\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 21\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"R20-W2。\"}\n      - {round: 21, reviewers: [1, 2], note: \"R21 两位 reviewer 均 AGREE Critical。见 R19-W1。\"}\n    action_items:\n      - {round: 20, action: \"见 R19-W1 action items\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 21 — Active issues\n  # ============================================================\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无 speedup\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 21\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"首次提出。\"}\n      - {round: 18, reviewers: [1, 2], note: \"Introduction 仍以 efficiency 动机展开。\"}\n      - {round: 19, reviewers: [1, 2], note: \"Table 5 +6.4% overhead, Intro 暗示 efficiency gain。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] R20-N1 Critical。§1 L3 仍有 'potential inference acceleration'。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R21 fresh review 再次标 Critical。Intro framing 已修改为 empirical study, 但 disclaimer 位于括号内过于隐蔽。根本问题(无实际加速)仍是最大实践性缺陷。R2 补充: 效率价值完全依赖未来 sparse kernel 支持。\"}\n    action_items:\n      - {round: 19, action: \"Paper Agent: Intro 去掉 efficiency motivation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 20, action: \"Paper Agent: 彻底清除 intro L3 'potential inference acceleration'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 21, action: \"Paper Agent: 将 'empirical study' 定位前移到 Abstract/§1 首段; wall-clock disclaimer 从括号提升到正文\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"Framing 已部分修复(efficiency motivation 清除), 但 disclaimer 位置仍隐蔽, 根本问题(无 speedup)无法通过写作修复。\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨三个架构系统性退步 (8B -5.2pp, 14B -20pp GSM8K, Mistral tied)\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 21\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W8。14B 仅 30% sparsity。\"}\n      - {round: 19, reviewers: [1, 2], note: \"R19-W2/W3。GSM8K -20pp σ=5.2pp。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 升级为 Critical。跨三架构一致。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-N3 Major + R2-W4 minor-to-major。Protection valley 分析(L14-L18)仅为 correlational, 未通过 per-layer constraint 做 interventional 验证。Conclusion 'task- and scale-dependent' 措辞过于模糊。\"}\n    action_items:\n      - {round: 19, action: \"Paper Agent: 14B 失败模式分析, reframe as finding\", assigned_to: \"paper_agent\", status: done}\n      - {round: 20, action: \"Agent: 提取 per-layer predicted sparsity rate 分析机制\", assigned_to: \"main_agent\", status: done}\n      - {round: 20, action: \"Paper Agent: §4.2 从假设升级为数据支撑的分析 (protection valley)\", assigned_to: \"paper_agent\", status: done}\n      - {round: 21, action: \"Agent: per-layer sparsity constraint 实验(如 late-layer ≤35%)验证因果链\", assigned_to: \"main_agent\", status: open}\n      - {round: 21, action: \"Paper Agent: Conclusion 将 'task- and scale-dependent' 改为明确陈述 'KL underperforms TEAL on MMLU/GSM8K across all tested scales'\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL train-inference mismatch confounds 2D 分解; 97.5% signal type 为 confounded upper bound\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] downstream 24-35% coupling 可能主要来自 mismatch。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-N2 Critical + R2-W1/W2 Major。97.5% 在 Abstract/Conclusion 无 caveat 是 overclaim。K=4 pilot 仅 single-seed, MMLU 43.5>E2E 40.7±1.3 和 GSM8K -6.8% gap closure 为 red flags。Abstract 'reveals task-dependent downstream structure' 对单种子结果过于自信。\"}\n    action_items:\n      - {round: 20, action: \"Agent: K=4 per-layer KL pilot 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 20, action: \"Paper Agent: §4.5 coupling 改为 upper bound + mismatch caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 21, action: \"Abstract/Conclusion 中 '97.5%' 加 '(upper bound; dimensions not orthogonal)' caveat\", assigned_to: \"paper_agent\", status: open}\n      - {round: 21, action: \"Abstract/Conclusion 中 K=4 findings 加 '(single seed, preliminary)' 标注\", assigned_to: \"paper_agent\", status: open}\n      - {round: 21, action: \"Agent: K=4 补充至少 2 个额外 seed (s123, s456)\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分不足: KL+Gumbel+frozen model 配方高度重合\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 21\n    mentions:\n      - {round: 16, reviewers: [2], note: \"R2 首次提出。\"}\n      - {round: 18, reviewers: [1, 2], note: \"R18-W1。\"}\n      - {round: 19, reviewers: [1, 2], note: \"R19-W1。R2 Critical, R1 REBUT。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[分歧] R2-N1 Critical, R1 REBUT。Director 判定 Warning。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R2-N1 Critical + R1 交叉 AGREE。fresh review 两位 reviewer 均认为 recipe overlap 是 critical concern。论文已承认 'shares the recipe-level principle' 但未在实验中量化 activation sparsity 设定下的差异。\"}\n    action_items:\n      - {round: 19, action: \"Paper Agent: 贡献重新定位为分析框架\", assigned_to: \"paper_agent\", status: done}\n      - {round: 20, action: \"Paper Agent: §2 承认配方相似 + 强调 first decomposition\", assigned_to: \"paper_agent\", status: done}\n      - {round: 21, action: \"Paper Agent: §1/§3 更明确论证 dynamic activation sparsity vs static N:M 的本质差异(generalization, per-token variability, global allocation 交互)\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD cross-seed variance 31×\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"WikiText-103→WikiText-2 同分布。C4 30% OOD 仅 2-seed global。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-W2 Major + R2 Q4。C4 CV 6.3% vs in-domain 0.2%, seed 42 异常偏高(18.22 vs 16.37)。暗示 predictor 对训练域有 overfitting。\"}\n    action_items:\n      - {round: 20, action: \"Paper Agent: Limitations 加 WikiText 同分布 + C4 限制\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W4\"\n    summary: \"MSE baseline 50% sparsity seed 123 灾难性失败(PPL=15,789, 5.1% sparsity)\"\n    category: experiment\n    severity: info\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 21\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W5。\"}\n      - {round: 19, reviewers: [1, 2], note: \"R19-W4 Major。\"}\n      - {round: 20, reviewers: [1, 2], note: \"R20-W5 Warning。severity 下降。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[分歧] R1-W3 Minor(调参不公平), R2 REBUT(instability 是 finding, λ_max=1000 工程合理)。Director 判定 Info—— Appendix F 配置充分, 但缺 λ_max grid search。\"}\n    action_items:\n      - {round: 19, action: \"Paper Agent: Table 4 footnote about s123 failure\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap ablation trajectory confound\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"R19-N2 Critical。循环论证 + soft-vs-hard confound。\"}\n      - {round: 20, reviewers: [1, 2], note: \"R20-W3 Major→Warning。reframe 部分有效。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-W1 Major。3-seed 一致性(≤1.70pp)提供部分 robustness, 但未证明 KL 是发现好 masks 的唯一途径。论文已用 'suggests' 替代 'confirms'——hedging 改善被认可。\"}\n    action_items:\n      - {round: 19, action: \"Paper Agent: reframe 为 transferability + circularity caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 20, action: \"Paper Agent: 'confirms'→'suggests' 全文替换\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Hedging 改善(suggests)被 R21 认可。根本 confound 无法通过写作消除, 但 severity 持续下降。\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Actual sparsity mismatch (KL 28.5% vs TEAL 29.3%) 在主表不够显著\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 21\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W6。\"}\n      - {round: 19, reviewers: [1, 2], note: \"R19-W6 Minor。\"}\n      - {round: 20, reviewers: [1, 2], note: \"R20-W6 Info。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[分歧] R2-W3 Major(Abstract/主表数字不一致), R1 REBUT(处理审慎)。Director 判定 Minor→Info。footnote + matched-sparsity appendix 信息完整。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot 限制实际影响\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"R19-W7 Info。\"}\n      - {round: 20, reviewers: [1, 2], note: \"R20-W7 Info。Limitations 已讨论。\"}\n      - {round: 21, reviewers: [], note: \"本轮未显式提出, 但隐含于 MMLU/GSM8K 退化讨论中。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 21 — New issues\n  # ============================================================\n\n  - id: \"R21-W1\"\n    summary: \"缺少 R-Sparse/CATS 等同类 baseline 的实验对比\"\n    category: experiment\n    severity: minor\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - {round: 21, reviewers: [2], note: \"R2-W5 Minor。论文仅 TEAL/BCE/MSE baseline, 缺 R-Sparse/CATS/FastForward 完整 pipeline。R1 partial REBUT: 控制变量比较训练目标, 架构差异会混淆。Director: Minor。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W2\"\n    summary: \"符号冲突: g^(ℓ) (gate activation, Eq.1) vs g1/g2 (Gumbel noise, Eq.4)\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-W5 Minor。建议将 Gumbel noise 改为 ε1, ε2 或 ξ1, ξ2。\"}\n    action_items:\n      - {round: 21, action: \"Paper Agent: Eq.(4) Gumbel noise g1/g2 → ε1/ε2\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W3\"\n    summary: \"Figure 2 仅展示 global allocation 但 30% 结论推荐 uniform\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - {round: 21, reviewers: [2], note: \"R2-M4 Minor。图表与结论 allocation 策略不一致。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Earlier rounds — Resolved (unchanged)\n  # ============================================================\n\n  - id: \"R20-N3\"\n    summary: \"'Coupling alignment' 术语已替换为 'output-distribution alignment'; 97.5% 标注为 upper bound\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"'coupling alignment' conflates signal type 和 coupling mechanism。\"}\n      - {round: 21, reviewers: [], note: \"术语问题未被 R21 reviewer 提出(已修复)。但 97.5% caveat 在 §4.5 脚注中存在, Abstract/Conclusion 中仍缺——衍生为 R20-W1 的一部分。\"}\n    action_items:\n      - {round: 20, action: \"Paper Agent: 全文替换 + 标注 upper bound\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"术语替换完成。97.5% 在 §4.5 有 caveat 但 Abstract/Conclusion 缺——见 R20-W1。\"\n    resolution_round: 21\n\n  - id: \"R20-W9\"\n    summary: \"Batched inference 对 contextual sparsity 的影响完全未讨论\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] mask 在 batch 内需取交集。\"}\n      - {round: 21, reviewers: [], note: \"R21 未提出。Limitations 已包含。\"}\n    action_items:\n      - {round: 20, action: \"Paper Agent: Limitations 加 batched inference\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Limitations 已加 batched inference 讨论。\"\n    resolution_round: 21\n\n  - id: \"R20-W10\"\n    summary: \"Abstract 'universally use BCE' → 'predominantly'\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"不准确。\"}\n      - {round: 21, reviewers: [], note: \"R21 未提出。已修复。\"}\n    action_items:\n      - {round: 20, action: \"'universally' → 'predominantly'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"已修复。\"\n    resolution_round: 21\n\n  - id: \"R19-F1\"\n    summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"已删除。R20/R21 未再提出。\"\n    resolution_round: 20\n\n  - id: \"R19-N1\"\n    summary: \"97.5% signal-type 归因缺乏 downstream 定量分解\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    resolution: \"Downstream 2D 分解已落地。衍生问题见 R20-W1。\"\n    resolution_round: 20\n\n  - id: \"R19-W5\"\n    summary: \"'hierarchy' → 'ranking' 术语降级\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    resolution: \"已修复。R21 未提出。\"\n    resolution_round: 20\n\n  - id: \"R19-W3\"\n    summary: \"Knowledge-intensive 任务退步缺乏机制解释\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 21\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W3。\"}\n      - {round: 19, reviewers: [1, 2], note: \"R19-W3 Major。\"}\n      - {round: 20, reviewers: [1, 2], note: \"合并进 R20-N2。\"}\n      - {round: 21, reviewers: [1, 2], note: \"仍存在。protection valley 分析为 correlational, 缺 interventional 验证。见 R20-N2。\"}\n    action_items:\n      - {round: 20, action: \"见 R20-N2 action items\", assigned_to: \"main_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W4\"\n    summary: \"Per-layer KL 对照实验缺失\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    resolution: \"Per-layer KL 3-seed 完成。\"\n    resolution_round: 19\n\n  - id: \"R18-W7\"\n    summary: \"Cross-seed Jaccard 未报告\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    resolution: \"Appendix 已补充。\"\n    resolution_round: 19\n\n  - id: \"R16-N1\"\n    summary: \"多种子覆盖不一致\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 19\n    resolution: \"所有关键行均为 3-seed。\"\n    resolution_round: 19\n\n  - id: \"R16-VIS1\"\n    summary: \"正文溢出到第9页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"正文 8 页合规。\"\n    resolution_round: 17\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界不够清晰\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 21\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"R20-W2。\"}\n      - {round: 21, reviewers: [1, 2], note: \"R21 两位 reviewer 均 AGREE Critical。见 R19-W1。\"}\n    action_items:\n      - {round: 20, action: \"见 R19-W1 action items\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1731 · 2026-05-22T13:17:50.479441+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 15280}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1732 · 2026-05-22T13:20:08.558466+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "report": "# Round 21 审稿报告（Fresh Review）\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法严谨性 + 实验设计) + R2 (新颖性 + 完整性 + 写作)\n**模式**: Fresh review (无上轮记忆)\n\n---\n\n## Summary\n\n本文研究用 KL 散度蒸馏替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器。在 LLaMA-3.1-8B 上 30% 稀疏度下，KL predictor（75.9M params, <1% base）将 TEAL 的 PPL 降低 14.5%（matched sparsity），并在 Mistral-7B（3-seed, -17.3%）和 Qwen-2.5-14B 上验证了 PPL 优势的跨架构泛化性。论文提出 signal type × coupling scope 的 2D 分类框架，通过 target-swap ablation（C1）和 per-layer KL 对照实验分析 mask quality 与 gradient coupling 的贡献。然而，论文在知识密集型任务上系统性输给 training-free baseline (TEAL)，且无实际 wall-clock 加速。\n\n---\n\n## Strengths\n\n**S1. Target-swap ablation (C1) 设计精巧且证据充分。** BCE 在 KL-derived masks 上训练后 PPL 与 KL predictor 一致（max Δ≤1.70pp at 30%, 3-seed; ≤0.79pp at 50%），有力支持 mask patterns 而非 gradient coupling 作为 PPL-level 质量驱动因素。论文已适当使用 \"suggests\" 而非 \"confirms\"。(Table 3, §4.3) **[R1-S3, R2-S1: 共识]**\n\n**S2. 全面的多种子消融实验 + 诚实的不利结果报告。** Table 4 覆盖 8 种配置（5 loss × 2 relaxation × 2 coupling scope），3-seed 评估贯穿全文（PPL σ=0.02）。MMLU/GSM8K 退化在 Abstract、§4.2 Task-Type Split、Limitations 中如实报告，未选择性隐藏。(Table 2, Table 4) **[R1-S2, R2-S2: 共识]**\n\n**S3. 2D taxonomy 提供有用的组织框架。** Signal type × coupling scope 将 DejaVu/ShadowLLM/FastForward/SPON/本文放入统一坐标系，per-layer KL decomposition 提供定量填充。(§3.7, Table 1, Appendix L) **[R1-S1, R2-S3: 共识]**\n\n**S4. 跨架构验证。** Mistral-7B-v0.3 (GQA+sliding window) 3-seed PPL -17.3%；Qwen-2.5-14B PPL 泛化但诚实报告 GSM8K -20pp regression。PPL advantage ratio 跨架构一致 (within 8% at ≤50%)。(§4.6, Tables 12-13) **[R1-S4, R2-S4: 共识]**\n\n**S5. 训练效率门槛低 + 可复现性高。** 单 GPU ~45min，1000 steps，predictor <1% base params。超参/架构/评估细节充分（bottleneck/temperature/steps sensitivity in Appendix B）。 **[R1-S5, R2 Reproducibility 4/5]**\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [Critical] 无实际推理加速，实用价值存疑。**\nPipeline 增加 6.4% latency overhead (126.78 vs 119.11 ms/fwd, Table 5)。Unstructured element-wise masks 无法转化为 wall-clock speedup。论文定位为 \"primarily an empirical study\"（§1），但此 disclaimer 位于括号内过于隐蔽。Introduction 叙事（\"learned sparsity predictors\"、\"inference allocates budgets globally\"）仍暗示效率目标。\n**[R1-N1 Critical + R2-N2 Critical: 完全共识]**\n\n**W2 [Critical] 与 MaskLLM 的 recipe 层面新颖性区分不足。**\nFrozen weights + KL divergence + Gumbel relaxation + learnable masks 的核心组合在 MaskLLM (Fang et al., 2024, NeurIPS) 中已建立。论文在 §2 承认 \"shares the recipe-level principle\" 并指出 static N:M vs dynamic per-token 差异，但 (a) 未实验量化此差异（如在 activation sparsity 设定下复现 MaskLLM learnable-mask variant）；(b) 分析框架（2D taxonomy）的概念创新幅度有限。论文更接近 \"MaskLLM applied to activation sparsity + post-hoc analysis\"。\n**[R2-N1 Critical + R1 交叉 AGREE]**\n\n**W3 [Critical] \"97.5% signal type\" claim 基于非正交分解 + confounded K=1 设置。**\nPer-layer KL (K=1) 训练 mask 1/32 层但推理 apply 全部 32 层，train-inference mismatch 与 coupling scope 混淆。§4.5 脚注承认 \"not fully orthogonal\"，但 Abstract 和 Conclusion 引用 \"up to 97.5%\" 时无 caveat。K=4 pilot 仅 single-seed，MMLU 反常结果（43.5 超过 E2E 40.7±1.3）和 GSM8K 负向 gap closure (-6.8%) 无法排除随机波动。Abstract \"reveals task-dependent downstream structure\" 对单种子结果过于自信。\n**[R1-N2 Critical + R2-W1/W2 Major: 共识升级 Critical]**\n\n### Should-Fix（影响评分）\n\n**W4 [Major] MMLU/GSM8K 系统性退化跨架构一致，framing 偏重 PPL。**\n8B MMLU -5.2pp, 14B GSM8K -20pp (σ=5.2pp), Mistral MMLU tied (43.3 vs 43.5)。KL 在知识密集型任务上系统性输给 training-free baseline (TEAL)，限制实用价值。Abstract/Introduction 以 PPL 改善为主叙事，Conclusion 以 \"task- and scale-dependent\" 回避。Per-layer sparsity 分析（L22-L28 at 48-57%, L14-L18 protection valley）仅为 correlational 证据——未通过 per-layer sparsity constraint 实验验证因果链。\n**[R1-N3 Major + R2-W4: R2 同意核心批评但建议从 Critical 降为 Major。Director 判定 Major——论文已在 §4.2/Limitations 中报告，但 Conclusion 措辞不够直接。]**\n\n**W5 [Major] C1 target-swap ablation 的 trajectory confound。**\nOracle masks 从特定 KL 训练轨迹提取（s42 来自 earlier run, Table 3 footnote）。3-seed 一致性（≤1.70pp）提供部分 robustness 证据，Appendix O 讨论了 trajectory 依赖。但 C1 仅证明好 masks 可 transfer，未证明 KL 是发现好 masks 的唯一/最佳途径。论文已适当使用 \"suggests\"——hedging 改善被两位 reviewer 认可。\n**[R1-W1 Major + R2 AGREE]**\n\n**W6 [Major] WikiText 同分布评估 + C4 OOD 覆盖不足。**\nWikiText-103 训练 → WikiText-2 评估均来自 Wikipedia。C4 OOD 30% 仅 2-seed global，cross-seed variance 急剧增大（CV 6.3% vs 0.2%），seed 42 异常偏高（18.22 vs 16.37）。Limitations 已提及但未量化域敏感性的 practical implications。\n**[R1-W2 Major + R2 AGREE]**\n\n### Minor\n\n**W7 [Minor] Sparsity mismatch 在主表中不够显著。** Table 2 中 KL 实际 28.5% vs TEAL 29.3%。Abstract 引用 matched 14.5% 而非主表 19%。Footnote + Appendix C 信息完整但正文显著性可提升。**[R2-W3, R1 REBUT 但同意可改进]**\n\n**W8 [Minor] 缺少同类方法参考对比。** 论文控制变量比较训练目标（KL/BCE/MSE），R-Sparse/CATS 架构差异会混淆变量。但补充参考数字会增强 positioning。**[R2-W5, R1 partial REBUT]**\n\n**W9 [Minor] MSE baseline seed 稳定性。** Seed 123 灾难性失败（PPL=15,789, 5.1% sparsity）。R2 认为 instability 本身是 finding，配置差异（λ_max=1000）有工程合理性。但缺 λ_max grid search。**[R1-W3, R2 REBUT]**\n\n**W10 [Minor] 符号冲突：g^(ℓ) (gate activation, Eq.1) vs g1/g2 (Gumbel noise, Eq.4)。** 建议 Gumbel noise 改为 ε1, ε2。**[R1-W5, R2 AGREE]**\n\n**W11 [Info] Figure 2 仅展示 global allocation 但 30% 时推荐 uniform。** 图表与结论 allocation 策略不一致。**[R2-M4]**\n\n**W12 [Info] Introduction wall-clock disclaimer 位于括号内，过于隐蔽。** **[R2-M1]**\n\n**W13 [Info] Table 2 注释过长（6行），信息密度过高。** **[R2-M2]**\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n1. **无 wall-clock 加速**是最根本的实践性缺陷 (Critical)\n2. **97.5% signal type claim** 基于 confounded 非正交分解，Abstract/Conclusion 缺 caveat (Critical)\n3. **K=4 pilot 单 seed** 不足以支撑推广，反常结果未排除 (Critical)\n4. **MaskLLM recipe 重合**限制方法创新幅度 (Critical)\n5. **MMLU/GSM8K 退化**需要更 balanced 的 framing + causal verification (Major)\n6. **WikiText 同分布评估**引入偏差 (Major)\n7. **C1 trajectory confound** 部分缓解但未根本解决；hedging 改善被认可 (Major)\n8. **Per-layer starvation 假说**缺因果验证——per-layer sparsity constraint 实验是自然 follow-up (Major)\n\n## Reviewer Divergence\n\n以下问题存在分歧但已通过交叉讨论解决：\n\n1. **Sparsity mismatch (R2-W3 Major vs R1 REBUT)**: Director 判定 **Minor**——footnote + matched-sparsity appendix 信息完整，但正文显著性可提升。\n2. **MSE baseline 公平性 (R1-W3 Minor vs R2 REBUT)**: Director 判定 **Minor (Info-leaning)**——instability 本身是 finding，配置差异有工程合理性。\n3. **Global MMLU variance (R1-W4 Minor vs R2 REBUT)**: Director 判定 **Info**——论文同时报告 global(σ=9.5pp) 和 uniform(σ=1.3pp)，处理得当。\n4. **Missing baselines (R2-W5 Minor vs R1 partial REBUT)**: Director 判定 **Minor**——controlled comparison 逻辑成立，但参考数字有价值。\n5. **R1-N3 severity (R1 Major vs R2 建议 Major)**: Director 维持 **Major**——论文已在多处报告退化，但 Conclusion 措辞过于模糊。\n\n---\n\n## Questions\n\n1. 在 activation sparsity 设定下实现 MaskLLM 的 learnable-mask approach（去掉 predictor network），PPL 和下游表现如何？这能直接隔离 \"predictor generalization\" 的贡献。\n2. K=4 是否有多种子数据？50% sparsity 下 K=4 数据是否可用？MMLU 超过 E2E KL 是否为系统性？\n3. Per-layer sparsity constraint（如限制 late-layer sparsity ≤35%）是否能缓解 MMLU/GSM8K 回退？\n4. BCE+compensation 的单独结果是什么？\"compensation provides no benefit\" 是否仅因 KL 自带补偿而 BCE 需要？\n5. 更多样训练集（如 C4 subsample）是否能降低 OOD variance？\n\n---\n\n## Missing References\n\n- **CATS** (Lee et al., 2024): 已提及但无实验对比——作为 training-free sophisticated baseline 值得补充\n- **R-Sparse** (Zhang et al., 2025): 已提及但无对比——同为 learned predictor\n- **Wanda** (Sun et al., 2024): 已提及但未讨论 activation-aware weight selection 与本文方法论关联\n- **Griffin/Hawk** (De et al., 2024): R1 建议，R2 REBUT（gated linear recurrence vs SwiGLU FFN sparsity 关联弱）。Director 判定**不需要**。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置/未请求。\n\n---\n\n## Visual Layout Check\n\n视觉审查 Agent 因 API 限额耗尽而失败（`agent_error: You've hit your limit · resets 6pm (UTC)`）。无排版审查结果。用户可在限额重置后重新触发。\n\n**格式合规（Reviewer 人工确认）：**\n| 项目 | 状态 |\n|------|------|\n| 正文 ≤ 8 页 | ✅ Sections 1-5 在 pages 1-8 |\n| ACL template [review] | ✅ |\n| Double-blind (Anonymous) | ✅ |\n| Mandatory Limitations | ✅ 1 段，覆盖 3 点 |\n| Ethics Statement | ✅ |\n| References 格式 | ✅ natbib, acl_natbib.bst |\n| Table/Figure 编号 | ✅ 连续正确 |\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 (Findings)**\n**Confidence: 4/5**\n**R1: 3.0 (Findings), Confidence 4/5 | R2: 3.0 (Findings), Confidence 4/5**\n\n这是一篇执行严谨的实证研究，target-swap ablation 和 2D taxonomy 对理解稀疏预测训练目标的设计空间有贡献。多种子评估、全面消融、诚实的不利结果报告体现了良好的研究规范。\n\n**阻止 Conference-level 接收的四个核心因素：**\n\n1. **实践价值缺失**：+6.4% overhead 且无路径到 wall-clock speedup。对于稀疏预测领域的论文，无法展示实际效率收益是硬伤。\n2. **Recipe 新颖性有限**：KL+Gumbel+frozen model 的核心组合已在 MaskLLM 中建立。迁移到 activation sparsity 设定有技术合理性但不足以构成独立方法贡献。分析框架（2D taxonomy）概念上直观。\n3. **核心分析 claim 可靠性不足**：97.5% signal-type 归因基于 confounded 非正交分解；K=4 pilot 单 seed 且有反常结果；late-layer starvation → knowledge regression 的因果链缺 interventional 证据。\n4. **下游 trade-off 显著**：MMLU/GSM8K 跨架构系统性输给 training-free TEAL（8B -5.2pp, 14B -20pp），限制 KL predictor 在知识密集场景下的实用性。\n\n**适合 Findings track 发表**——分析框架和消融实验对后续 predictor-based sparsity 研究有参考价值。\n\n**升级路径**（Borderline Conference 潜力）：\n- (a) Triton block-sparse proof-of-concept 加速数据\n- (b) 多种子 K=4 数据消除 mismatch confound\n- (c) Per-layer sparsity constraint 实验验证 late-layer starvation 假说\n- (d) Abstract/Conclusion 中 97.5% 和 K=4 claims 加充分 caveat\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"primarily an empirical study\" 声明应前移到 Abstract 或 §1 首段，不应藏在 contribution 列表前。\n- \"(Appendix A)\" 括号内的 wall-clock disclaimer 过于隐蔽，建议提升到正文句子。\n- Contribution 列表第一项过长（4行），建议拆分 per-layer decomposition 和 cross-scale evidence。\n\n### §2 Related Work\n- MaskLLM 段落应更直接量化 activation sparsity 设定下的技术难点（per-token variability, OOD generalization, global allocation interaction），而非仅列举 \"technically differ\"。\n- CATS/R-Sparse 仅列举未讨论优劣，错失 positioning 机会。\n\n### §3 Method\n- Eq.(1) g^(ℓ) vs Eq.(4) g1/g2 符号冲突——建议 Gumbel noise 改为 ε1, ε2。\n- §3.5 adaptive penalty controller: \"geometric doubling\" 的 double/halve 条件和频率仅在 appendix，正文应补充关键实现细节。\n- §3.7 Taxonomy table (Table 1): 多数 cell 为空/---，作为 visual representation 信息含量有限。\n\n### §4 Experiments\n- Table 2: 注释 6 行过长；实际 sparsity 差异（28.5% vs 29.3%）应在正文讨论而非仅 footnote。\n- §4.2 Task-Type Split: per-layer sparsity 分析（L14-L18 protection valley）是 correlational，建议明确标注\"correlational, not causal\"。\n- §4.5 Per-layer KL: \"up to 97.5%\" 在 Abstract/Conclusion 中需加 \"(upper bound; dimensions not orthogonal)\" caveat。K=4 pilot 推广时需标注 \"(single seed, preliminary)\"。\n- §4.6: Figure 2 仅展示 global allocation 但结论推荐 uniform，不一致。\n- §4.5 Compensation: BCE+compensation 的单独结果未报告——应明确 compensation 对 BCE 的效果以区分 \"KL masks 好到不需要\" vs \"BCE masks 差到 compensation 也救不了\"。\n\n### §5 Conclusion\n- \"task- and scale-dependent\" 过于模糊。建议改为直接陈述：KL 在 commonsense 任务上优于 TEAL，在 knowledge-intensive 任务上系统性劣于 TEAL。\n\n### Limitations\n- 覆盖 3 点，符合 EMNLP 要求。建议量化 OOD variance 的 practical implications（如 CV 从 0.2% → 6.3% 意味着什么）。\n\n### Appendix\n- Table 5 (latency) 的 +6.4% overhead 数据应在正文中更显著引用。\n- K=4 pilot (Table 17) 应在标题中明确标注 \"n=1 seed, preliminary\"。",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "report": "# Round 21 审稿报告（Fresh Review）\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法严谨性 + 实验设计) + R2 (新颖性 + 完整性 + 写作)\n**模式**: Fresh review (无上轮记忆)\n\n---\n\n## Summary\n\n本文研究用 KL 散度蒸馏替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器。在 LLaMA-3.1-8B 上 30% 稀疏度下，KL predictor（75.9M params, <1% base）将 TEAL 的 PPL 降低 14.5%（matched sparsity），并在 Mistral-7B（3-seed, -17.3%）和 Qwen-2.5-14B 上验证了 PPL 优势的跨架构泛化性。论文提出 signal type × coupling scope 的 2D 分类框架，通过 target-swap ablation（C1）和 per-layer KL 对照实验分析 mask quality 与 gradient coupling 的贡献。然而，论文在知识密集型任务上系统性输给 training-free baseline (TEAL)，且无实际 wall-clock 加速。\n\n---\n\n## Strengths\n\n**S1. Target-swap ablation (C1) 设计精巧且证据充分。** BCE 在 KL-derived masks 上训练后 PPL 与 KL predictor 一致（max Δ≤1.70pp at 30%, 3-seed; ≤0.79pp at 50%），有力支持 mask patterns 而非 gradient coupling 作为 PPL-level 质量驱动因素。论文已适当使用 \"suggests\" 而非 \"confirms\"。(Table 3, §4.3) **[R1-S3, R2-S1: 共识]**\n\n**S2. 全面的多种子消融实验 + 诚实的不利结果报告。** Table 4 覆盖 8 种配置（5 loss × 2 relaxation × 2 coupling scope），3-seed 评估贯穿全文（PPL σ=0.02）。MMLU/GSM8K 退化在 Abstract、§4.2 Task-Type Split、Limitations 中如实报告，未选择性隐藏。(Table 2, Table 4) **[R1-S2, R2-S2: 共识]**\n\n**S3. 2D taxonomy 提供有用的组织框架。** Signal type × coupling scope 将 DejaVu/ShadowLLM/FastForward/SPON/本文放入统一坐标系，per-layer KL decomposition 提供定量填充。(§3.7, Table 1, Appendix L) **[R1-S1, R2-S3: 共识]**\n\n**S4. 跨架构验证。** Mistral-7B-v0.3 (GQA+sliding window) 3-seed PPL -17.3%；Qwen-2.5-14B PPL 泛化但诚实报告 GSM8K -20pp regression。PPL advantage ratio 跨架构一致 (within 8% at ≤50%)。(§4.6, Tables 12-13) **[R1-S4, R2-S4: 共识]**\n\n**S5. 训练效率门槛低 + 可复现性高。** 单 GPU ~45min，1000 steps，predictor <1% base params。超参/架构/评估细节充分（bottleneck/temperature/steps sensitivity in Appendix B）。 **[R1-S5, R2 Reproducibility 4/5]**\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [Critical] 无实际推理加速，实用价值存疑。**\nPipeline 增加 6.4% latency overhead (126.78 vs 119.11 ms/fwd, Table 5)。Unstructured element-wise masks 无法转化为 wall-clock speedup。论文定位为 \"primarily an empirical study\"（§1），但此 disclaimer 位于括号内过于隐蔽。Introduction 叙事（\"learned sparsity predictors\"、\"inference allocates budgets globally\"）仍暗示效率目标。\n**[R1-N1 Critical + R2-N2 Critical: 完全共识]**\n\n**W2 [Critical] 与 MaskLLM 的 recipe 层面新颖性区分不足。**\nFrozen weights + KL divergence + Gumbel relaxation + learnable masks 的核心组合在 MaskLLM (Fang et al., 2024, NeurIPS) 中已建立。论文在 §2 承认 \"shares the recipe-level principle\" 并指出 static N:M vs dynamic per-token 差异，但 (a) 未实验量化此差异（如在 activation sparsity 设定下复现 MaskLLM learnable-mask variant）；(b) 分析框架（2D taxonomy）的概念创新幅度有限。论文更接近 \"MaskLLM applied to activation sparsity + post-hoc analysis\"。\n**[R2-N1 Critical + R1 交叉 AGREE]**\n\n**W3 [Critical] \"97.5% signal type\" claim 基于非正交分解 + confounded K=1 设置。**\nPer-layer KL (K=1) 训练 mask 1/32 层但推理 apply 全部 32 层，train-inference mismatch 与 coupling scope 混淆。§4.5 脚注承认 \"not fully orthogonal\"，但 Abstract 和 Conclusion 引用 \"up to 97.5%\" 时无 caveat。K=4 pilot 仅 single-seed，MMLU 反常结果（43.5 超过 E2E 40.7±1.3）和 GSM8K 负向 gap closure (-6.8%) 无法排除随机波动。Abstract \"reveals task-dependent downstream structure\" 对单种子结果过于自信。\n**[R1-N2 Critical + R2-W1/W2 Major: 共识升级 Critical]**\n\n### Should-Fix（影响评分）\n\n**W4 [Major] MMLU/GSM8K 系统性退化跨架构一致，framing 偏重 PPL。**\n8B MMLU -5.2pp, 14B GSM8K -20pp (σ=5.2pp), Mistral MMLU tied (43.3 vs 43.5)。KL 在知识密集型任务上系统性输给 training-free baseline (TEAL)，限制实用价值。Abstract/Introduction 以 PPL 改善为主叙事，Conclusion 以 \"task- and scale-dependent\" 回避。Per-layer sparsity 分析（L22-L28 at 48-57%, L14-L18 protection valley）仅为 correlational 证据——未通过 per-layer sparsity constraint 实验验证因果链。\n**[R1-N3 Major + R2-W4: R2 同意核心批评但建议从 Critical 降为 Major。Director 判定 Major——论文已在 §4.2/Limitations 中报告，但 Conclusion 措辞不够直接。]**\n\n**W5 [Major] C1 target-swap ablation 的 trajectory confound。**\nOracle masks 从特定 KL 训练轨迹提取（s42 来自 earlier run, Table 3 footnote）。3-seed 一致性（≤1.70pp）提供部分 robustness 证据，Appendix O 讨论了 trajectory 依赖。但 C1 仅证明好 masks 可 transfer，未证明 KL 是发现好 masks 的唯一/最佳途径。论文已适当使用 \"suggests\"——hedging 改善被两位 reviewer 认可。\n**[R1-W1 Major + R2 AGREE]**\n\n**W6 [Major] WikiText 同分布评估 + C4 OOD 覆盖不足。**\nWikiText-103 训练 → WikiText-2 评估均来自 Wikipedia。C4 OOD 30% 仅 2-seed global，cross-seed variance 急剧增大（CV 6.3% vs 0.2%），seed 42 异常偏高（18.22 vs 16.37）。Limitations 已提及但未量化域敏感性的 practical implications。\n**[R1-W2 Major + R2 AGREE]**\n\n### Minor\n\n**W7 [Minor] Sparsity mismatch 在主表中不够显著。** Table 2 中 KL 实际 28.5% vs TEAL 29.3%。Abstract 引用 matched 14.5% 而非主表 19%。Footnote + Appendix C 信息完整但正文显著性可提升。**[R2-W3, R1 REBUT 但同意可改进]**\n\n**W8 [Minor] 缺少同类方法参考对比。** 论文控制变量比较训练目标（KL/BCE/MSE），R-Sparse/CATS 架构差异会混淆变量。但补充参考数字会增强 positioning。**[R2-W5, R1 partial REBUT]**\n\n**W9 [Minor] MSE baseline seed 稳定性。** Seed 123 灾难性失败（PPL=15,789, 5.1% sparsity）。R2 认为 instability 本身是 finding，配置差异（λ_max=1000）有工程合理性。但缺 λ_max grid search。**[R1-W3, R2 REBUT]**\n\n**W10 [Minor] 符号冲突：g^(ℓ) (gate activation, Eq.1) vs g1/g2 (Gumbel noise, Eq.4)。** 建议 Gumbel noise 改为 ε1, ε2。**[R1-W5, R2 AGREE]**\n\n**W11 [Info] Figure 2 仅展示 global allocation 但 30% 时推荐 uniform。** 图表与结论 allocation 策略不一致。**[R2-M4]**\n\n**W12 [Info] Introduction wall-clock disclaimer 位于括号内，过于隐蔽。** **[R2-M1]**\n\n**W13 [Info] Table 2 注释过长（6行），信息密度过高。** **[R2-M2]**\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n1. **无 wall-clock 加速**是最根本的实践性缺陷 (Critical)\n2. **97.5% signal type claim** 基于 confounded 非正交分解，Abstract/Conclusion 缺 caveat (Critical)\n3. **K=4 pilot 单 seed** 不足以支撑推广，反常结果未排除 (Critical)\n4. **MaskLLM recipe 重合**限制方法创新幅度 (Critical)\n5. **MMLU/GSM8K 退化**需要更 balanced 的 framing + causal verification (Major)\n6. **WikiText 同分布评估**引入偏差 (Major)\n7. **C1 trajectory confound** 部分缓解但未根本解决；hedging 改善被认可 (Major)\n8. **Per-layer starvation 假说**缺因果验证——per-layer sparsity constraint 实验是自然 follow-up (Major)\n\n## Reviewer Divergence\n\n以下问题存在分歧但已通过交叉讨论解决：\n\n1. **Sparsity mismatch (R2-W3 Major vs R1 REBUT)**: Director 判定 **Minor**——footnote + matched-sparsity appendix 信息完整，但正文显著性可提升。\n2. **MSE baseline 公平性 (R1-W3 Minor vs R2 REBUT)**: Director 判定 **Minor (Info-leaning)**——instability 本身是 finding，配置差异有工程合理性。\n3. **Global MMLU variance (R1-W4 Minor vs R2 REBUT)**: Director 判定 **Info**——论文同时报告 global(σ=9.5pp) 和 uniform(σ=1.3pp)，处理得当。\n4. **Missing baselines (R2-W5 Minor vs R1 partial REBUT)**: Director 判定 **Minor**——controlled comparison 逻辑成立，但参考数字有价值。\n5. **R1-N3 severity (R1 Major vs R2 建议 Major)**: Director 维持 **Major**——论文已在多处报告退化，但 Conclusion 措辞过于模糊。\n\n---\n\n## Questions\n\n1. 在 activation sparsity 设定下实现 MaskLLM 的 learnable-mask approach（去掉 predictor network），PPL 和下游表现如何？这能直接隔离 \"predictor generalization\" 的贡献。\n2. K=4 是否有多种子数据？50% sparsity 下 K=4 数据是否可用？MMLU 超过 E2E KL 是否为系统性？\n3. Per-layer sparsity constraint（如限制 late-layer sparsity ≤35%）是否能缓解 MMLU/GSM8K 回退？\n4. BCE+compensation 的单独结果是什么？\"compensation provides no benefit\" 是否仅因 KL 自带补偿而 BCE 需要？\n5. 更多样训练集（如 C4 subsample）是否能降低 OOD variance？\n\n---\n\n## Missing References\n\n- **CATS** (Lee et al., 2024): 已提及但无实验对比——作为 training-free sophisticated baseline 值得补充\n- **R-Sparse** (Zhang et al., 2025): 已提及但无对比——同为 learned predictor\n- **Wanda** (Sun et al., 2024): 已提及但未讨论 activation-aware weight selection 与本文方法论关联\n- **Griffin/Hawk** (De et al., 2024): R1 建议，R2 REBUT（gated linear recurrence vs SwiGLU FFN sparsity 关联弱）。Director 判定**不需要**。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置/未请求。\n\n---\n\n## Visual Layout Check\n\n视觉审查 Agent 因 API 限额耗尽而失败（`agent_error: You've hit your limit · resets 6pm (UTC)`）。无排版审查结果。用户可在限额重置后重新触发。\n\n**格式合规（Reviewer 人工确认）：**\n| 项目 | 状态 |\n|------|------|\n| 正文 ≤ 8 页 | ✅ Sections 1-5 在 pages 1-8 |\n| ACL template [review] | ✅ |\n| Double-blind (Anonymous) | ✅ |\n| Mandatory Limitations | ✅ 1 段，覆盖 3 点 |\n| Ethics Statement | ✅ |\n| References 格式 | ✅ natbib, acl_natbib.bst |\n| Table/Figure 编号 | ✅ 连续正确 |\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 (Findings)**\n**Confidence: 4/5**\n**R1: 3.0 (Findings), Confidence 4/5 | R2: 3.0 (Findings), Confidence 4/5**\n\n这是一篇执行严谨的实证研究，target-swap ablation 和 2D taxonomy 对理解稀疏预测训练目标的设计空间有贡献。多种子评估、全面消融、诚实的不利结果报告体现了良好的研究规范。\n\n**阻止 Conference-level 接收的四个核心因素：**\n\n1. **实践价值缺失**：+6.4% overhead 且无路径到 wall-clock speedup。对于稀疏预测领域的论文，无法展示实际效率收益是硬伤。\n2. **Recipe 新颖性有限**：KL+Gumbel+frozen model 的核心组合已在 MaskLLM 中建立。迁移到 activation sparsity 设定有技术合理性但不足以构成独立方法贡献。分析框架（2D taxonomy）概念上直观。\n3. **核心分析 claim 可靠性不足**：97.5% signal-type 归因基于 confounded 非正交分解；K=4 pilot 单 seed 且有反常结果；late-layer starvation → knowledge regression 的因果链缺 interventional 证据。\n4. **下游 trade-off 显著**：MMLU/GSM8K 跨架构系统性输给 training-free TEAL（8B -5.2pp, 14B -20pp），限制 KL predictor 在知识密集场景下的实用性。\n\n**适合 Findings track 发表**——分析框架和消融实验对后续 predictor-based sparsity 研究有参考价值。\n\n**升级路径**（Borderline Conference 潜力）：\n- (a) Triton block-sparse proof-of-concept 加速数据\n- (b) 多种子 K=4 数据消除 mismatch confound\n- (c) Per-layer sparsity constraint 实验验证 late-layer starvation 假说\n- (d) Abstract/Conclusion 中 97.5% 和 K=4 claims 加充分 caveat\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"primarily an empirical study\" 声明应前移到 Abstract 或 §1 首段，不应藏在 contribution 列表前。\n- \"(Appendix A)\" 括号内的 wall-clock disclaimer 过于隐蔽，建议提升到正文句子。\n- Contribution 列表第一项过长（4行），建议拆分 per-layer decomposition 和 cross-scale evidence。\n\n### §2 Related Work\n- MaskLLM 段落应更直接量化 activation sparsity 设定下的技术难点（per-token variability, OOD generalization, global allocation interaction），而非仅列举 \"technically differ\"。\n- CATS/R-Sparse 仅列举未讨论优劣，错失 positioning 机会。\n\n### §3 Method\n- Eq.(1) g^(ℓ) vs Eq.(4) g1/g2 符号冲突——建议 Gumbel noise 改为 ε1, ε2。\n- §3.5 adaptive penalty controller: \"geometric doubling\" 的 double/halve 条件和频率仅在 appendix，正文应补充关键实现细节。\n- §3.7 Taxonomy table (Table 1): 多数 cell 为空/---，作为 visual representation 信息含量有限。\n\n### §4 Experiments\n- Table 2: 注释 6 行过长；实际 sparsity 差异（28.5% vs 29.3%）应在正文讨论而非仅 footnote。\n- §4.2 Task-Type Split: per-layer sparsity 分析（L14-L18 protection valley）是 correlational，建议明确标注\"correlational, not causal\"。\n- §4.5 Per-layer KL: \"up to 97.5%\" 在 Abstract/Conclusion 中需加 \"(upper bound; dimensions not orthogonal)\" caveat。K=4 pilot 推广时需标注 \"(single seed, preliminary)\"。\n- §4.6: Figure 2 仅展示 global allocation 但结论推荐 uniform，不一致。\n- §4.5 Compensation: BCE+compensation 的单独结果未报告——应明确 compensation 对 BCE 的效果以区分 \"KL masks 好到不需要\" vs \"BCE masks 差到 compensation 也救不了\"。\n\n### §5 Conclusion\n- \"task- and scale-dependent\" 过于模糊。建议改为直接陈述：KL 在 commonsense 任务上优于 TEAL，在 knowledge-intensive 任务上系统性劣于 TEAL。\n\n### Limitations\n- 覆盖 3 点，符合 EMNLP 要求。建议量化 OOD variance 的 practical implications（如 CV 从 0.2% → 6.3% 意味着什么）。\n\n### Appendix\n- Table 5 (latency) 的 +6.4% overhead 数据应在正文中更显著引用。\n- K=4 pilot (Table 17) 应在标题中明确标注 \"n=1 seed, preliminary\"。",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 1733 · 2026-05-22T13:20:12.524130+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3965
}
```

</details>

---


### Assistant

_source line 1734 · 2026-05-22T13:20:21.261379+00:00_

审稿报告已投递。

---

**Round 21 审稿完成。**

**评分**: **3.0 (Findings)**，两位 Reviewer 完全一致，Confidence 4/5。

**四个阻止 Conference-level 的核心问题**：
1. **无 wall-clock 加速** (+6.4% overhead)，实践价值缺失
2. **MaskLLM recipe 重合**，方法新颖性有限
3. **97.5% signal-type claim confounded** (非正交分解 + K=4 单 seed)
4. **MMLU/GSM8K 跨架构系统性输给 TEAL**，framing 偏重 PPL

**升级路径** (→ Borderline Conference)：补充 block-sparse 加速 proof-of-concept、多种子 K=4 数据、per-layer sparsity constraint 实验、Abstract/Conclusion caveat。

Issue Tracker 已同步更新（4 条 Critical open/in_progress, 3 条 Major, 4 条 Minor/Info, 3 条新建）。视觉审查因 API 限额失败，格式合规由 Reviewer 人工确认通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 150

## Round 150

2 recorded events


### User

_source line 1735 · 2026-05-22T13:20:24.075139+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

与 R2 在多数关键问题上达成共识，在 2 条上提出部分反驳（W3 sparsity mismatch 处理合理、W5 baseline scope 有实验设计逻辑）。两位 reviewer 共同确认的核心弱点：无 wall-clock 加速、K=4 pilot 证据不足、知识任务退化归因缺因果验证。Overall 维持 3 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1736 · 2026-05-22T13:20:34.424518+00:00_

审稿报告已投递至 Research Director。

**Round 21 审稿总结：**

- **Overall: 3.0 (Findings)**，R1 和 R2 完全一致
- **4 个 Critical**: (1) 无 wall-clock 加速 (+6.4% overhead); (2) MaskLLM recipe 新颖性不足; (3) 97.5% signal-type claim 基于 confounded 非正交分解 + K=4 单 seed; (4) MMLU/GSM8K 跨架构系统性退化
- **3 个 Major**: C1 trajectory confound (hedging 改善被认可); WikiText 同分布评估; late-layer starvation 缺因果验证
- **升级路径**: Triton proof-of-concept 加速 + 多种子 K=4 + per-layer constraint 实验 + Abstract/Conclusion caveat 补充
- **视觉审查**: Agent API 限额耗尽，未完成
- **Issue Tracker**: 已同步更新至 Round 21（4 critical in_progress, 3 warning in_progress, 3 new minor/info）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 151

## Round 151

74 recorded events


### User

_source line 1737 · 2026-05-22T17:08:27.561684+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1738 · 2026-05-22T17:08:33.269548+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1739 · 2026-05-22T17:08:33.320586+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1740 · 2026-05-22T17:08:41.346365+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch,TodoWrite",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch,TodoWrite",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 1741 · 2026-05-22T17:08:41.346911+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1742 · 2026-05-22T17:08:46.589425+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1743 · 2026-05-22T17:08:46.640005+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1744 · 2026-05-22T17:08:51.558199+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1745 · 2026-05-22T17:08:51.608797+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1746 · 2026-05-22T17:09:01.993184+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1747 · 2026-05-22T17:09:01.993583+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1748 · 2026-05-22T17:09:11.820211+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool call

_source line 1749 · 2026-05-22T17:09:12.272002+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 submission guidelines author instructions page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 submission guidelines author instructions page limit"
  }
}
```

</details>

---


### Tool result

_source line 1750 · 2026-05-22T17:09:13.678223+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (374 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T16:17:03Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 373 个实验 — ANALYZING 1, DEPLOYED 1, DONE 321, PENDING 1, PREPARING 49\n**DONE 分布**: failed 33, killed 17, negative 28, success 243\n\n### 💾 磁盘余量\n- **westd-34887**:\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/usr/bin/nvidia-smi`: 817G/879G 可用（已用 3%）\n- **westd-41718**:\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/init`: 150M/150M 可用（已用 0%）\n  - `/usr/bin/nvidia-smi`: 765G/879G 可用（已用 9%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `perlayer_kl_k4_s456` [failed] — 2026-05-22T16:16:58 — EXIT_CODE=129 (non-zero)\n- `perlayer_kl_k4_s123` [failed] — 2026-05-22T16:12:32 — EXIT_CODE=129 (non-zero)\n- `mse30_s123_downstream` [success] — 2026-05-22T15:13:32\n- `constraint_remove_valley_kl30_s42` [negative] — 2026-05-22T14:47:00\n- `constraint_protect_late_kl30_s42` [negative] — 2026-05-22T14:28:00\n\n### 🔴 最近失败原因 (top 3)\n- `perlayer_kl_k4_s456`: EXIT_CODE=129 (non-zero)\n- `perlayer_kl_k4_s123`: EXIT_CODE=129 (non-zero)\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B
…[truncated 1790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1858
}
```

</details>

---


### Tool call

_source line 1751 · 2026-05-22T17:09:14.130294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1752 · 2026-05-22T17:09:14.632617+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	\input{limitations}
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1753 · 2026-05-22T17:09:14.783562+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1754 · 2026-05-22T17:09:14.834196+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1755 · 2026-05-22T17:09:19.201344+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 submission guidelines author instructions page limit"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, I found relevant information about ACL Rolling Review (ARR) submission guidelines for May 2026:

## Submission Guidelines

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

## Author Instructions

Key anonymity requirements include:
- Papers must not include authors' names and affiliations, and s
…[truncated 762 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6929
}
```

</details>

---


### Tool call

_source line 1756 · 2026-05-22T17:09:29.790075+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1757 · 2026-05-22T17:09:29.840766+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1758 · 2026-05-22T17:09:29.891354+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 CFP submission format template anonymity appendix rules site:aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 CFP submission format template anonymity appendix rules site:aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 1759 · 2026-05-22T17:09:30.092526+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1760 · 2026-05-22T17:09:30.092994+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns---not the training mechanism itself---as the proximate quality driver.
5	An output-distribution alignment ranking emerges across five loss configurations; a per-layer KL control decomposes this into two dimensions: signal type dominates PPL (up to 97.5\% of the gap at 30\%; upper bound, as dimensions are not fully orthogonal), while coupling scope contributes 10--47\% on downstream tasks (3-seed $K{=}4$-corrected; commonsense 22--47\%, reasoning 10\%); a train--inference mismatch confound in the $K{=}1$ control inflates the $K{=}1$ upper bound (21--48\%).
6	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
7	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1761 · 2026-05-22T17:09:30.695444+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1762 · 2026-05-22T17:09:30.846412+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	While MaskLLM~\cite{fang2024maskllm} applies KL-based mask optimization, it targets static N:M weight sparsity; activation sparsity requires masks that generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation suggests that these discovered mask targets are the proximate quality driver at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.20.
…[truncated 2956 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool result

_source line 1763 · 2026-05-22T17:09:48.737322+00:00_

Web search results for query: "ACL Rolling Review 2026 CFP submission format template anonymity appendix rules site:aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"}]

I've successfully found the ACL Rolling Review (ARR) Call for Papers (CFP) with information 
…[truncated 1591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 18845
}
```

</details>

---


### Tool call

_source line 1764 · 2026-05-22T17:09:55.363117+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1765 · 2026-05-22T17:09:56.318449+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importan
…[truncated 9598 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1766 · 2026-05-22T17:09:56.619974+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1767 · 2026-05-22T17:09:56.620847+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1768 · 2026-05-22T17:09:56.821889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1769 · 2026-05-22T17:09:56.973064+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address dynamic sparsity--quantization interaction; AWQ~\cite{lin2024awq} applies activation-aware weight quantization for on-device deployment; Outlier Suppression+~\cite{wei2023outlier} mitigates outlier-induced quantization errors via shifting and scaling.
7	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
8	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
9	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
10	
11	\paragraph{Predictor-Based Contextual Sparsity.}
12	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
13	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
14	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
15	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity pred
…[truncated 5023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1770 · 2026-05-22T17:09:57.274727+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1771 · 2026-05-22T17:09:57.777086+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the dominant design dimension for PPL (signal type: up to 97.5\% of the gap at 30\%; upper bound, not fully orthogonal); cross-layer coupling contributes 10--47\% on downstream tasks (3-seed $K{=}4$-corrected; commonsense 22--47\%, GSM8K 10\%); MMLU anomalously favors $K{=}4$, reflecting allocation alignment confirmed by constraint analysis (Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A predictor ($<$1\% of base) reduces TEAL's PPL by 14.5\% via masks 46--68\% divergent from magnitude; KL outperforms TEAL on commonsense (ARC-c, WG, BoolQ) but underperforms on knowledge tasks (MMLU, GSM8K) across tested scales---a learned allocation trade-off, not an inherent objective limitation (Appendix~\ref{app:constraint}).
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1772 · 2026-05-22T17:09:57.777410+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1773 · 2026-05-22T17:09:58.279430+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated. Evaluation is limited to 7--14B; scaling to 70B+ and wall-clock speedup via sparse kernels remain future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1774 · 2026-05-22T17:09:58.430360+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1775 · 2026-05-22T17:09:59.183564+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 1776 · 2026-05-22T17:09:59.183902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1777 · 2026-05-22T17:10:00.138012+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 36672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1778 · 2026-05-22T17:10:00.138420+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR ACL Rolling Review dates deadlines May 2026 cycle site:aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR ACL Rolling Review dates deadlines May 2026 cycle site:aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 1779 · 2026-05-22T17:10:00.841156+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 commitment deadline ARR submission site:2026.emnlp.org OR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 commitment deadline ARR submission site:2026.emnlp.org OR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1780 · 2026-05-22T17:10:06.287148+00:00_

Web search results for query: "ARR ACL Rolling Review dates deadlines May 2026 cycle site:aclrollingreview.org"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Dates – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/some-important-dates/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"ARR Dashboard","url":"http://stats.aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

I found information about ARR ACL Rolling Review dates and deadlines. Here's what I found regarding the May 2026 cycle:

The deadline for completing the author registration form is January 7th 2026 EoD AoE.

For reviewers and area chairs in the May 2026 cycle:
- AC checklists must be completed by
…[truncated 732 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6148
}
```

</details>

---


### Tool result

_source line 1781 · 2026-05-22T17:10:07.290604+00:00_

Web search results for query: "EMNLP 2026 commitment deadline ARR submission site:2026.emnlp.org OR site:aclweb.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Resolutions - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Resolutions"},{"title":"The Second Workshop on Evaluation for Multimodal Generation | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-workshop-multi-modal-generation"}]

Based on the search results, I found information about EMNLP 2026 ARR submission and commitment deadlines:

## EMNLP 2026 ARR Submission and Commitment Information

Papers must be submitted, at latest, by the ARR 2026 May cycle. According to the search results, papers that have received reviews and a meta
…[truncated 897 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6449
}
```

</details>

---


### Tool call

_source line 1782 · 2026-05-22T17:10:14.717007+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1783 · 2026-05-22T17:10:16.172368+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (374 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T16:17:03Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 373 个实验 — ANALYZING 1, DEPLOYED 1, DONE 321, PENDING 1, PREPARING 49\n**DONE 分布**: failed 33, killed 17, negative 28, success 243\n\n### 💾 磁盘余量\n- **westd-34887**:\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/usr/bin/nvidia-smi`: 817G/879G 可用（已用 3%）\n- **westd-41718**:\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/init`: 150M/150M 可用（已用 0%）\n  - `/usr/bin/nvidia-smi`: 765G/879G 可用（已用 9%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `perlayer_kl_k4_s456` [failed] — 2026-05-22T16:16:58 — EXIT_CODE=129 (non-zero)\n- `perlayer_kl_k4_s123` [failed] — 2026-05-22T16:12:32 — EXIT_CODE=129 (non-zero)\n- `mse30_s123_downstream` [success] — 2026-05-22T15:13:32\n- `constraint_remove_valley_kl30_s42` [negative] — 2026-05-22T14:47:00\n- `constraint_protect_late_kl30_s42` [negative] — 2026-05-22T14:28:00\n\n### 🔴 最近失败原因 (top 3)\n- `perlayer_kl_k4_s456`: EXIT_CODE=129 (non-zero)\n- `perlayer_kl_k4_s123`: EXIT_CODE=129 (non-zero)\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B
…[truncated 1790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 1784 · 2026-05-22T17:10:16.224078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1785 · 2026-05-22T17:10:16.626204+00:00_

1	% =============================================================================
2	% Additional references (R20 review response)
3	% =============================================================================
4	
5	@inproceedings{geva2023dissecting,
6	  title = {Dissecting Recall of Factual Associations in Auto-Regressive Language Models},
7	  author = {Geva, Mor and Bastings, Jasmijn and Filippova, Katja and Globerson, Amir},
8	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
9	  pages = {12216--12235},
10	  year = {2023},
11	}
12	
13	@article{fu2024lazyllm,
14	  title = {{LazyLLM}: Dynamic Token Pruning for Efficient Long Context {LLM} Inference},
15	  author = {Qichen Fu and Minsik Cho and Thomas Merth and Sachin Mehta and Mohammad Rastegari and Mahyar Najibi},
16	  year = {2024},
17	  journal = {arXiv preprint arXiv:2407.14057},
18	}
19	
20	@article{zhang2025cots,
21	  title = {{COTS}: Connected Sparse Activation for Efficient {LLM} Inference},
22	  author = {Yilong Zhang and Junyuan Shang and Huanqi Cao and Shiyao Li and Shuguang Jiang and Lingxiao Ma and Shun Zheng and Cheng Li and Jiang Bian},
23	  year = {2025},
24	  journal = {arXiv preprint arXiv:2502.14475},
25	}
26	
27	@inproceedings{alizadeh2024llmflash,
28	  title = {{LLM} in a Flash: Efficient Large Language Model Inference with Limited Memory},
29	  author = {Keivan Alizadeh and Iman Mirzadeh and Dmitry Belenko and Karen Khatamifard and Minsik Cho and Carlo C Del Mundo and Mohammad Rastegari and Mehrdad Farajtabar},
30	  year = {2024},
31	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
32	}
33	
34	@article{wei2023outlier,
35	  title = {Outlier Suppression+: Accurate Quantization of Large Language Models by Equivalent and Effective Shifting and Scaling},
36	  author = {Xiuying Wei and Yunchen Zhang and Yuhang Li and Xiangguo Zhang and Ruihao Gong and Jinyang Guo and Xianglong 
…[truncated 23340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1786 · 2026-05-22T17:10:16.626666+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": "598"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "offset": "598"
  }
}
```

</details>

---


### Tool result

_source line 1787 · 2026-05-22T17:10:16.727334+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (598). The file has 598 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1788 · 2026-05-22T17:11:05.806831+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1789 · 2026-05-22T17:11:06.309073+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1790 · 2026-05-22T17:11:06.761253+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1791 · 2026-05-22T17:11:07.263463+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1792 · 2026-05-22T17:11:07.464396+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf",
    "limit": "1"
  }
}
```

</details>

---


### Tool result

_source line 1793 · 2026-05-22T17:11:07.514989+00:00_

This PDF has 19 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1794 · 2026-05-22T17:11:10.525294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1795 · 2026-05-22T17:11:10.977107+00:00_

1	issues:
2	  # ============================================================
3	  # Round 21 — Active issues
4	  # ============================================================
5	
6	  - id: "R19-N3"
7	    summary: "无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无 speedup"
8	    category: experiment
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 16
12	    last_seen_round: 21
13	    mentions:
14	      - {round: 16, reviewers: [1, 2], note: "首次提出。"}
15	      - {round: 18, reviewers: [1, 2], note: "Introduction 仍以 efficiency 动机展开。"}
16	      - {round: 19, reviewers: [1, 2], note: "Table 5 +6.4% overhead, Intro 暗示 efficiency gain。"}
17	      - {round: 20, reviewers: [1, 2], note: "[AGREE] R20-N1 Critical。§1 L3 仍有 'potential inference acceleration'。"}
18	      - {round: 21, reviewers: [1, 2], note: "[AGREE] R21 fresh review 再次标 Critical。Intro framing 已修改为 empirical study, 但 disclaimer 位于括号内过于隐蔽。"}
19	    action_items:
20	      - {round: 19, action: "Paper Agent: Intro 去掉 efficiency motivation", assigned_to: "paper_agent", status: done}
21	      - {round: 20, action: "Paper Agent: 彻底清除 intro L3 'potential inference acceleration'", assigned_to: "paper_agent", status: done}
22	      - {round: 21, action: "Paper Agent: Abstract 加 'empirical study' 定位; §1 wall-clock disclaimer 从括号提升到正文句子", assigned_to: "paper_agent", status: done}
23	    resolution: "结构性限制无法通过实验消除。写作修复完成: Abstract 定位 'empirical study' + §1 wall-clock disclaimer 为独立正文句子。"
24	    resolution_round: 22
25	
26	  - id: "R20-N2"
27	    summary: "MMLU/GSM8K 跨三个架构系统性退步 (8B -5.2pp, 14B -20pp GSM8K, Mistral tied)"
28	    category: experiment
29	    severity: critical
30	    status: resolved
31	    first_raised_round: 18
32	    last_seen_round: 21
33	    mentions:
34	      - {round: 18, reviewers: [1, 2], note: "R18-W8。14B 仅 30% sparsity。"}
35	      - {round: 19, reviewers: [1, 2], note: "R19-W2/W3。GSM8K -20pp σ=5.2pp。"}
36	      - {round: 20, reviewers: [1, 2], note: "[AGREE] 升级为 Critica
…[truncated 16591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1796 · 2026-05-22T17:11:11.027657+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool result

_source line 1797 · 2026-05-22T17:11:11.682361+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf (528.3KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 1798 · 2026-05-22T17:11:59.286166+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'in_progress', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'in_progress', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1799 · 2026-05-22T17:11:59.286663+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1800 · 2026-05-22T17:12:06.576488+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool call

_source line 1801 · 2026-05-22T17:12:08.585051+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf",
  "venue": "EMNLP 2026",
  "note": "ARR May 2026 cycle, deadline 2026-05-25. Long paper (8 pages)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf",
    "venue": "EMNLP 2026",
    "note": "ARR May 2026 cycle, deadline 2026-05-25. Long paper (8 pages)."
  }
}
```

</details>

---


### Tool result

_source line 1802 · 2026-05-22T17:12:30.075469+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23498
}
```

</details>

---


### Tool result

_source line 1803 · 2026-05-22T17:12:30.075806+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 21490
}
```

</details>

---


### Tool call

_source line 1804 · 2026-05-22T17:12:32.183704+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责审查论文的**方法严谨性和实验设计**。\n\n## 论文信息\n- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- **Venue**: EMNLP 2026 (通过 ARR May 2026 投稿)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 8 页, references 不限, Limitations 和 Ethics 不计入页数\n- **模板**: ACL LaTeX (review mode)\n- **匿名规则**: Double-blind\n- **论文路径**: `projects/distill_sparse_swiglu/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- KL distillation framework 的数学严谨性：forward KL 选择是否 well-motivated？gradient analysis (§3.6) 的论证是否严密？\n- Gumbel-Sigmoid relaxation 的数学正确性和与 STE 的对比是否公平\n- Adaptive penalty controller (§3.5) 是否有收敛保证或仅依赖经验\n- 2D taxonomy (§3.7) 是否真正是有意义的框架，还是 post-hoc 组织\n\n### 2. 实验设计与统计分析\n- Baseline 选择是否公平（BCE 1000 steps vs KL 1000 steps, 但 BCE 2700 steps 也测了）\n- 3-seed coverage 是否充分？哪些关键行缺少多种子？\n- C1 target-swap ablation (§4.4) 的因果推断是否成立？circularity 和 soft-vs-hard confound 怎么评估？\n- Per-layer KL decomposition (§4.5) 的 97.5% signal type 归因：K=1 的 train-inference mismatch confound 有多严重？K=4 的 3-seed 结果是否足够消解？MMLU anomaly 的解释可信度？\n- Actual sparsity mismatch (KL 28.5% vs TEAL 29.3%) 对主要结论的影响\n- MSE baseline 50% seed 123 catastrophic failure (PPL=15,789) 说明什么\n\n### 3. 可复现性\n- 所有超参数是否充分报告\n- 训练和评估 protocol 是否清晰可复现\n\n### 评分标准 (ARR Overall Assessment)\n5 = Consider for Award (~top 2.5%), 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n请严格、客观地评审。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → 评分建议。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责审查论文的**方法严谨性和实验设计**。\n\n## 论文信息\n- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- **Venue**: EMNLP 2026 (通过 ARR May 2026 投稿)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 8 页, references 不限, Limitations 和 Ethics 不计入页数\n- **模板**: ACL LaTeX (review mode)\n- **匿名规则**: Double-blind\n- **论文路径**: `projects/distill_sparse_swiglu/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- KL distillation framework 的数学严谨性：forward KL 选择是否 well-motivated？gradient analysis (§3.6) 的论证是否严密？\n- Gumbel-Sigmoid relaxation 的数学正确性和与 STE 的对比是否公平\n- Adaptive penalty controller (§3.5) 是否有收敛保证或仅依赖经验\n- 2D taxonomy (§3.7) 是否真正是有意义的框架，还是 post-hoc 组织\n\n### 2. 实验设计与统计分析\n- Baseline 选择是否公平（BCE 1000 steps vs KL 1000 steps, 但 BCE 2700 steps 也测了）\n- 3-seed coverage 是否充分？哪些关键行缺少多种子？\n- C1 target-swap ablation (§4.4) 的因果推断是否成立？circularity 和 soft-vs-hard confound 怎么评估？\n- Per-layer KL decomposition (§4.5) 的 97.5% signal type 归因：K=1 的 train-inference mismatch confound 有多严重？K=4 的 3-seed 结果是否足够消解？MMLU anomaly 的解释可信度？\n- Actual sparsity mismatch (KL 28.5% vs TEAL 29.3%) 对主要结论的影响\n- MSE baseline 50% seed 123 catastrophic failure (PPL=15,789) 说明什么\n\n### 3. 可复现性\n- 所有超参数是否充分报告\n- 训练和评估 protocol 是否清晰可复现\n\n### 评分标准 (ARR Overall Assessment)\n5 = Consider for Award (~top 2.5%), 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n请严格、客观地评审。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → 评分建议。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1805 · 2026-05-22T17:12:51.453259+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19269
}
```

</details>

---


### Tool call

_source line 1806 · 2026-05-22T17:12:52.357759+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责审查论文的**新颖性、写作质量和完整性**。\n\n## 论文信息\n- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- **Venue**: EMNLP 2026 (通过 ARR May 2026 投稿)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 8 页, references 不限, Limitations 和 Ethics 不计入页数\n- **模板**: ACL LaTeX (review mode)\n- **匿名规则**: Double-blind\n- **论文路径**: `projects/distill_sparse_swiglu/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 与 MaskLLM (Fang et al., 2024) 的区分度：两者都用 frozen model + learnable masks + KL + Gumbel。§2 列出的 3 个差异 (per-token generalization, global allocation, OOD robustness) 是否足以构成独立贡献？\n- 2D taxonomy (signal type × coupling scope) 是否是真正的 intellectual contribution，还是对已有方法的简单重组？\n- 论文自我定位为 \"primarily empirical study\" — 对于 EMNLP 2026，这种定位的 empirical contribution 是否足够？\n- Target-swap ablation 和 per-layer KL decomposition 的分析深度是否达到发表标准？\n\n### 2. 写作质量\n- Abstract 信息密度：7 句话覆盖了多少内容？读者能否快速理解核心发现？\n- Introduction 的叙事结构：问题→动机→方法→结果的逻辑链是否清晰？\n- 符号一致性和数学表述清晰度\n- Table/Figure 的设计：Table 2 注释是否过长？Figure 1 是否有效传达方法？Figure 2 仅展示 global 但推荐 uniform 是否 misleading？\n- Conclusion 是否过于简短/过于密集？\n- 正文与 Appendix 的信息分配是否合理\n\n### 3. 完整性与 Related Work\n- Related Work (§2) 的覆盖面：是否遗漏重要工作？特别关注 2025-2026 年的新工作\n- 是否缺少与 R-Sparse, CATS, DIP 等同类 training-free 方法的实验对比？\n- 论文没有 wall-clock speedup — 这对实际影响力的影响\n- Limitations 是否充分？是否遗漏重要限制？\n- Ethics Statement 是否适当？\n\n### 4. 格式合规\n- 正文是否严格 8 页以内\n- Appendix 是否使用双栏格式（ARR 从 2025.07 起要求）\n- 匿名化是否彻底\n- 引用格式是否正确\n\n### 评分标准 (ARR Overall Assessment)\n5 = Consider for Award (~top 2.5%), 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n请严格、客观地评审。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → 评分建议。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责审查论文的**新颖性、写作质量和完整性**。\n\n## 论文信息\n- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- **Venue**: EMNLP 2026 (通过 ARR May 2026 投稿)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 8 页, references 不限, Limitations 和 Ethics 不计入页数\n- **模板**: ACL LaTeX (review mode)\n- **匿名规则**: Double-blind\n- **论文路径**: `projects/distill_sparse_swiglu/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 与 MaskLLM (Fang et al., 2024) 的区分度：两者都用 frozen model + learnable masks + KL + Gumbel。§2 列出的 3 个差异 (per-token generalization, global allocation, OOD robustness) 是否足以构成独立贡献？\n- 2D taxonomy (signal type × coupling scope) 是否是真正的 intellectual contribution，还是对已有方法的简单重组？\n- 论文自我定位为 \"primarily empirical study\" — 对于 EMNLP 2026，这种定位的 empirical contribution 是否足够？\n- Target-swap ablation 和 per-layer KL decomposition 的分析深度是否达到发表标准？\n\n### 2. 写作质量\n- Abstract 信息密度：7 句话覆盖了多少内容？读者能否快速理解核心发现？\n- Introduction 的叙事结构：问题→动机→方法→结果的逻辑链是否清晰？\n- 符号一致性和数学表述清晰度\n- Table/Figure 的设计：Table 2 注释是否过长？Figure 1 是否有效传达方法？Figure 2 仅展示 global 但推荐 uniform 是否 misleading？\n- Conclusion 是否过于简短/过于密集？\n- 正文与 Appendix 的信息分配是否合理\n\n### 3. 完整性与 Related Work\n- Related Work (§2) 的覆盖面：是否遗漏重要工作？特别关注 2025-2026 年的新工作\n- 是否缺少与 R-Sparse, CATS, DIP 等同类 training-free 方法的实验对比？\n- 论文没有 wall-clock speedup — 这对实际影响力的影响\n- Limitations 是否充分？是否遗漏重要限制？\n- Ethics Statement 是否适当？\n\n### 4. 格式合规\n- 正文是否严格 8 页以内\n- Appendix 是否使用双栏格式（ARR 从 2025.07 起要求）\n- 匿名化是否彻底\n- 引用格式是否正确\n\n### 评分标准 (ARR Overall Assessment)\n5 = Consider for Award (~top 2.5%), 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n请严格、客观地评审。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → 评分建议。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1807 · 2026-05-22T17:12:53.666357+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool call

_source line 1808 · 2026-05-22T17:13:16.699974+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 和 Reviewer 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 和 Reviewer 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1809 · 2026-05-22T17:13:16.700528+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1810 · 2026-05-22T17:13:34.698139+00:00_

全部派发完成：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | 已启动，并行执行 |
| 外部审稿 (Stanford Agentic Reviewer) | 已发送请求，8h 自动提醒 |
| Reviewer 1（方法+实验） | 已派发 |
| Reviewer 2（新颖性+写作） | 已派发 |

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 152

## Round 152

2 recorded events


### User

_source line 1811 · 2026-05-22T17:17:31.833446+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

## 总体评分

**Overall Assessment**: 3.0 (Findings)
**一句话总结**: 扎实的实证研究，系统地比较了 KL vs BCE 训练目标对 SwiGLU 稀疏预测器的影响，但新颖性有限（核心 recipe 与 MaskLLM 共享），缺乏 wall-clock speedup 和强 baseline 实验对比，且知识密集型任务上的系统性退化削弱了实际价值。

## 官方维度打分（ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claim 有实验支撑，但 C1 ablation 存在 soft-vs-hard confound 未完全解耦；"97.5% signal type" 为 upper bound 且维度不正交；per-layer KL K=1 有 train-inference mismatch confound |
| Excitement | 2.5/5 | 核心 recipe (frozen weights + learnable masks + KL + Gumbel) 与 MaskLLM 共享；2D taxonomy 是简单分类而非深刻理论贡献；自我定位为 empirical study 但缺少 wall-clock speedup 削弱实际影响力 |
| Overall | 3.0/5 | Findings 级别：分析深度达到发表标准但不足以进入主会议；需补充实际加速数据和更强 baseline 对比 |
| Confidence | 4/5 | 仔细阅读了全文和 appendix，对 activation sparsity 领域较为熟悉 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 缺乏 wall-clock speedup 实验——实际增加 6.4% 延迟
- 具体位置：Appendix A (Table 5), §4.6 最后一段, Limitations
- 问题：论文提出的方法在当前实现下不仅没有加速，反而增加了 6.4% 推理延迟（126.78 vs 119.11 ms/forward）。论文在 Limitations 中承认 "wall-clock speedup requires sparse kernels not addressed here"，但对于一篇声称改进 sparsity prediction 的论文，完全没有端到端加速证据是严重缺陷。TEAL 原论文已展示 1.53× 和 1.8× 的 wall-clock speedup（40% 和 50% sparsity）。如果 KL predictor 的 mask 质量更好但无法转化为实际加速，其实际价值存疑。
- 为什么影响接收：作为 efficiency-motivated 工作，没有加速数据使得论文的实际贡献仅限于分析层面，严重限制了 impact。
- 建议修改方向：至少用 Triton block-sparse kernel 或 DejaVu 的 sparse GEMM 展示一个 sparsity level 的 wall-clock speedup；或者彻底将论文重新定位为纯分析工作并在 title 中体现。

**N2** [critical] 知识密集型任务（MMLU, GSM8K）的系统性退化未得到充分解释
- 具体位置：Table 2 (30%: MMLU 40.7 vs 45.86, GSM8K 7.5 vs 8.79), §4.2 Task-Type Split, Table 13 (Qwen-14B: GSM8K −20pp)
- 问题：KL predictor 在所有测试规模上（8B, 7B, 14B）系统性地在 MMLU 和 GSM8K 上逊于 TEAL。论文将此归因为 "distribution-matching objectives systematically sacrifice reasoning-critical pathways"，但这只是描述现象而非解释机制。如果 KL 的 mode-covering 特性（§3.4 中作为选择 forward KL 的论据）无法保护推理关键路径，这实际上挑战了论文选择 forward KL 的理论动机。更关键的是，Appendix T（Remove Valley 实验）显示通过简单调整 per-layer allocation 可以恢复 MMLU +3.3pp 和 GSM8K +1.5pp——这表明退化可能是可避免的分配问题，而非 KL 目标的固有缺陷，但论文未进一步追踪此线索。
- 为什么影响接收：MMLU 和 GSM8K 是评估 LLM 能力的核心 benchmark。在这些任务上系统性地逊于 training-free baseline（TEAL），使得方法的实用性大打折扣。
- 建议修改方向：(1) 深入分析 KL mask 在具体哪些层/neuron 上与 MMLU-critical activations 冲突；(2) 基于 Remove Valley 发现，提出一个任务感知的 allocation 策略并验证。

**N3** [critical] 与 MaskLLM 的区分度不足以支撑独立贡献
- 具体位置：§2 Related Work（第19-21行）
- 问题：论文列出的 3 个与 MaskLLM 的差异——(a) per-token generalization vs static N:M, (b) global top-k allocation, (c) OOD robustness——主要是应用场景差异（activation sparsity vs weight sparsity），而非方法论创新。核心训练 recipe 完全相同：frozen model + learnable masks + KL divergence + Gumbel relaxation。论文的真正贡献是将此 recipe 应用到 activation sparsity 并进行系统分析，但 §2 的措辞暗示了更大的方法论距离。2D taxonomy（Table 1）作为组织框架有用，但本身并不构成 intellectual contribution——它只是对已有方法的简单分类，其中 4/6 个格子被已有工作占据。
- 为什么影响接收：如果 reviewer 认为这是 MaskLLM 的直接应用而非独立方法贡献，论文的 novelty 将受到严重质疑。
- 建议修改方向：(1) 更诚实地定位——将论文明确框定为 "systematic empirical analysis of KL distillation for contextual activation sparsity"，而非暗示方法论创新；(2) 强化独特贡献：target-swap ablation 和 per-layer decomposition 是真正的分析创新，应给予更多篇幅。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 缺少与 training-free 方法的直接实验对比
- 具体位置：§2 第5行提到 R-Sparse, CATS, DIP, SparseInfer，§4 Baselines
- 问题：Related Work 中引用了多个 2024-2025 的同类方法（R-Sparse [ICLR 2025], CATS, DIP [MLSys 2024], SparseInfer），但实验部分仅与 TEAL 和 DejaVu-style BCE 对比。R-Sparse 使用 rank-aware SVD 预测，与本文的 learned predictor 在同一赛道竞争，缺乏直接对比削弱了论文 claims 的说服力。LaRoSA (2025) 也在 SwiGLU 模型上展示了 wall-clock speedup，是高度相关的 baseline。
- 建议：至少加入 R-Sparse 的实验对比（同为 predictor-based 方法），或解释为什么这些方法不适合作为 baseline。

**W2** [warning] Figure 2 展示 global allocation 但推荐 uniform——存在误导
- 具体位置：Figure 2（第8页），§4.2（"Uniform allocation preserves downstream performance best"），§4.5（Allocation Behavior）
- 问题：Figure 2 展示的是 global allocation 下的 PPL scaling 曲线，但正文 §4.2 明确建议 uniform allocation 以获得更好的 downstream 性能。读者看 Figure 2 得到的印象（"KL 在所有 sparsity 下都大幅优于 TEAL"）可能在 uniform allocation 下不成立（实际上 uniform TEAL 在 MMLU 上系统性优于 KL uniform）。Caption 虽标注了 "(global allocation)"，但作为正文仅有的两张 figure 之一，其 framing 效果很强。
- 建议：在 Figure 2 中加入 uniform allocation 的对比曲线，或在 caption 中明确说明 downstream 结果在 uniform 下不同。

**W3** [warning] Conclusion（§5）过于密集且遗漏 limitation 信号
- 具体位置：§5 Conclusion（仅2句话，约130词）
- 问题：Conclusion 将大量信息压缩到2句话中，包含多个带括号的数字和 appendix 引用，可读性差。更重要的是，Conclusion 完全没有提及 MMLU/GSM8K 退化、缺乏 wall-clock speedup、以及方法的适用边界。一个好的 conclusion 应该 balance strengths and limitations，而非只强调正面发现。Conclusion 中提到 "BoolQ" 但 BoolQ 并未出现在 Table 2 主实验中（仅在 Appendix Table 18），这是不一致的。
- 建议：扩展至 3-4 句，加入主要 limitation 的 honest acknowledgment，删除 BoolQ（或将其加入 Table 2）。

**W4** [warning] C1 Target-Swap Ablation 的 soft-vs-hard confound 未完全解耦
- 具体位置：§4.3 "Soft-vs-Hard Confound" 段落, Appendix P
- 问题：C1 ablation 同时改变了两个变量：(1) mask targets (KL-derived vs magnitude) 和 (2) mask representation (soft Gumbel vs hard binary)。论文试图通过 BCE+Gumbel (32.22) vs standard BCE (27.97) 来论证 softness 不是主要因素，但这个比较并不干净——BCE+Gumbel 的 PPL 更差（32.22 > 27.97），说明 Gumbel 在 BCE 设置下是有害的，而非中性的。正确的控制实验应该是：KL predictor with hard masks (STE) vs KL predictor with soft masks，但 STE 在 30% 时 sparsity 无法收敛（§4.5 STE Failure），使得完全解耦不可行。论文承认了这一局限（"trajectory-dependent confounds"），但对 C1 的结论措辞（"masks as the proximate quality driver"）过于强硬。
- 建议：将 C1 的结论从 "suggests" 弱化为更加 hedged 的表述，明确列出无法完全解耦的原因。

**W5** [warning] Abstract 信息密度过高
- 具体位置：Abstract（7句话，约180词）
- 问题：Abstract 第5句长达约60词，包含多个嵌套的数字和条件（"97.5% of the gap at 30%; upper bound, as dimensions are not fully orthogonal; while coupling scope contributes 10-47% on downstream tasks; 3-seed K=4-corrected; commonsense 22-47%, reasoning 10%"）。这对首次阅读的 reviewer 来说几乎不可能在一遍内理解。Abstract 应帮助读者快速 grasp 核心发现，而非压缩完整结果。
- 建议：简化第5句，将数值细节移入 Introduction；Abstract 聚焦 high-level takeaway。

---

## 小问题（不影响接收）

- **M1**: Table 2 注释过多（†, ‡, *, ±, §），建议精简。BCE 30% 使用 TEAL global（†）而非 uniform，与其他行不一致，读者容易忽略。
- **M2**: §3.5 Adaptive Penalty Controller 的 deadzone margin ε=0.02 的选择缺乏 justification。
- **M3**: §4.3 "Cross-seed KL Jaccard distance (36.3%; Appendix F.1)" 提供了 noise baseline，但未与 random mask baseline（0.462）做更显式的对比来量化 systematic component。
- **M4**: 论文在 §4.2 中报告 MMLU 40.7±1.3%（3-seed），但 global allocation 的 MMLU 方差极大（35.7±9.5%），跨度从 25.3% 到 43.5%——这种不稳定性值得在正文中更突出地讨论。
- **M5**: References 中 Gautam et al. (2026) 的 FastForward 标注为 arXiv:2602.00397——这是 2026 年 2 月的 preprint，如果已被会议接收应更新引用信息。
- **M6**: §3.1 中 d_ff=14,336 的逗号分隔在数学环境中使用了 `{,}` hack，建议使用 `\,` 提高一致性。
- **M7**: Appendix 部分的 Table 编号（Table 5-21）跨度很大，建议检查是否有遗漏或重复编号。

---

## Questions for Authors

1. 既然 Remove Valley 实验（Appendix T）显示调整 per-layer allocation 可以恢复 MMLU +3.3pp，为什么不将此作为默认配置或提出一个任务感知的 allocation 机制？这似乎是一个低悬果实。

2. Figure 2 仅展示 global allocation 的 PPL 曲线。能否提供 uniform allocation 下的 PPL scaling 数据？在 uniform 下 KL 的优势是否同样随 sparsity 增加而扩大？

3. 论文在 30% sparsity 时实际达到 28.5%（5% deviation），在 TEAL 28.5% 时 PPL 10.30。那么 "14.5% PPL reduction" 的 claim 是基于 matched sparsity（28.5%: 8.81 vs 10.30 = 14.5%）还是 target sparsity（30%: 8.81 vs 10.82 = 18.6%）？Abstract 和 Introduction 的措辞应保持一致。

4. 训练仅用 1000 steps 在 WikiText-103 上——这是否足以让 predictor 学习到 generalizable 的 activation patterns？C4 上的高 cross-seed variance（CV=6.3% vs in-domain 0.2%）暗示可能存在过拟合。是否尝试过在更大/更多样化的数据上训练？

5. 论文在 §3.6 gradient analysis 中声称 "KL's coupled gradients discover neuron importance patterns that diverge 68% from magnitude-based masks"，但 §4.3 C1 ablation 又说 "masks as the proximate quality driver, not the coupling mechanism itself"。这两个 claim 之间的关系需要更清晰的阐述——如果 coupling 主要是用来 discover 好的 mask patterns，而非提供 inference-time 优势，那么是否可以用 KL 训练后提取 masks 再用更简单的方法（如 BCE）部署？

---

## Missing References

1. **LaRoSA** (2025, arXiv:2507.01299): Layerwise Rotated Sparse Activation——在 SwiGLU 模型上实现 wall-clock speedup 的 activation sparsity 方法，高度相关但未被引用。
2. **Geva et al. (2023)** "Dissecting Recall of Factual Associations": 虽已在 bib 中但正文未引用——与 MMLU regression 的讨论相关（factual recall 与 MLP 层的关系）。

---

## 主要优势

- **S1**: 系统性的实验设计——5 种 loss function 的对比（KL, reverse KL, JSD, BCE, MSE）、3-seed 评估、cross-architecture 验证（LLaMA, Mistral, Qwen），实验严谨度高于该领域多数工作。
- **S2**: Target-swap ablation (C1) 是一个巧妙的分析方法，能够部分解耦 mask quality 和 training mechanism 的贡献，具有方法论参考价值。
- **S3**: Per-layer KL decomposition（K=1 和 K=4 控制实验）对 signal type vs coupling scope 的定量分解是该领域的新颖分析维度。
- **S4**: 诚实的自我定位——论文明确声明 "primarily an empirical study" 并详细讨论了 confounds 和 upper bounds，这种学术诚实值得肯定。
- **S5**: Comprehensive appendix（19页总计）提供了充分的补充材料，包括 sensitivity analysis、OOD evaluation、mask visualization 等。

---

## 格式合规检查

| 项目 | 状态 | 说明 |
|------|------|------|
| 正文页数 | ✅ | §1-§5 在第8页结束（Conclusion 在 p8 底部） |
| Limitations | ✅ | 在 p9，不计入页数限制，覆盖3个关键点 |
| Ethics | ✅ | 在 p9，简短适当 |
| 匿名化 | ✅ | "Anonymous ACL submission"，未发现泄露 |
| Appendix 双栏 | ✅ | p12-19 使用双栏 ACL 格式 |
| 引用格式 | ✅ | 使用 acl_natbib，格式一致 |

---

## 评分总结

本文是一篇执行质量较高的实证研究，系统分析了 KL distillation 对 SwiGLU activation sparsity 预测器的影响。主要贡献是分析性的（target-swap ablation、2D decomposition），而非方法论创新（核心 recipe 来自 MaskLLM）。三个 critical 问题——缺乏 wall-clock speedup、MMLU/GSM8K 系统性退化、与 MaskLLM 区分度不足——使其更适合 Findings 而非主会议。如果作者能补充实际加速数据并深化 MMLU regression 的分析，有潜力升至 3.5 (Borderline Conference)。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1812 · 2026-05-22T17:17:48.589328+00:00_

Reviewer 2 审稿意见已收到，评分 3.0 (Findings)。三个 Critical 问题：wall-clock speedup 缺失、MMLU/GSM8K 退化、MaskLLM 区分度。等待 Reviewer 1 完成审稿后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 153

## Round 153

2 recorded events


### User

_source line 1813 · 2026-05-22T17:17:51.105712+00:00_

[Reviewer 2 审稿结果]:
审稿完成。已将完整审稿意见提交给 Review Director。

**审稿结论**：Overall 3.0 (Findings)，Soundness 3.5，Excitement 2.5。

核心问题：
1. **缺乏 wall-clock speedup**——方法实际增加 6.4% 延迟，无加速证据
2. **MMLU/GSM8K 系统性退化**——在所有规模上逊于 training-free baseline TEAL
3. **与 MaskLLM 区分度不足**——核心 recipe（frozen weights + KL + Gumbel masks）完全共享

主要优势在于实验设计的系统性（5 种 loss 对比、3-seed、cross-architecture）和 target-swap ablation / per-layer decomposition 的分析创新。格式完全合规。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1814 · 2026-05-22T17:18:00.079241+00:00_

Reviewer 2 审稿完成（Overall 3.0 Findings）。等待 Reviewer 1 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 154

## Round 154

8 recorded events


### User

_source line 1815 · 2026-05-22T17:20:55.136423+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

---

## 总体评分

**Overall**: 3.5/5 (Borderline Conference)

**一句话总结**: 扎实的实证研究，KL 蒸馏优于 BCE 训练稀疏性预测器的核心发现可信且有价值，但两个关键因果分析声明（C1 ablation 和 97.5% signal-type decomposition）超出实验证据支撑范围，加之无实际推理加速、规模仅 7–14B，整体处于 Conference/Findings 边界。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心 KL distillation 方法数学正确、实验设计合理。但 C1 因果推断存在循环性，K=1 signal-type decomposition 受严重 train-inference mismatch 混淆，97.5% 精确数字给人虚假精确感。 |
| Excitement | 3/5 | "训练目标如何塑造 mask quality" 的研究问题有意义，但技术组件（KL 蒸馏、Gumbel-Sigmoid、adaptive penalty）均为成熟工具的应用组合。无 wall-clock speedup 削弱实际影响力。 |
| Confidence | 4/5 | 仔细阅读全文及全部 19 页附录，逐表核验了关键数字。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] C1 Target-Swap Ablation 的因果推断存在循环性，causal claim 过强

- 具体位置：§4.4, Table 3, Abstract ("the discovered patterns—not the training mechanism itself—as the proximate quality driver")
- 问题：C1 实验将 KL 训练发现的 mask 作为 BCE 的 oracle target，证明 BCE 在这些 target 上能达到接近 KL 的 PPL。但这些 mask 本身就是 KL 的 end-to-end gradient coupling 发现的产物。因此 C1 **不能**分离 "mask pattern quality" 和 "the training dynamics that shaped those masks"——它仅证明了 "KL-derived masks are transferable to simpler training"，而非 "mask patterns alone, independent of discovery mechanism, drive quality"。
- 补充证据：
  - s42 C1 使用了 "earlier checkpoint" 的 oracle (Table 3 footnote †)，PPL gap = 0.65pp；而 s123/s456 使用 matched retrained oracle 后 gap ≤0.03pp。两组结果的不一致性本身就说明 oracle 来源（即 KL 训练动态）影响 C1 质量。
  - 下游任务方向不一致：s42 C1 在 MMLU (+1.7pp) 和 GSM8K (+0.23pp) 上优于 KL，但 s456 C1 在 MMLU (−0.96pp) 和 GSM8K (−0.98pp) 上劣于 KL。如果 mask pattern 是唯一质量驱动因素，下游方向应一致。
- 为什么影响接收：这是论文三大 contribution 之一（Abstract bullet 3），因果声明的过强直接影响论文核心贡献的可信度。
- 建议修改方向：将 claim 降级为 "KL-discovered masks are transferable: BCE trained on KL-derived targets approaches KL-level PPL, suggesting mask patterns carry substantial quality information"。删除 "not the training mechanism itself" 的排除性声明。

**N2** [critical] Per-Layer KL Decomposition 的 "97.5% signal type dominance" 受严重混淆变量影响

- 具体位置：§4.5 (Per-Layer KL: Decomposing Signal Type and Coupling Scope)
- 问题：
  1. **K=1 的 train-inference mismatch 极大**：训练时仅 mask 1/32 层，推理时 mask 全部 32 层。论文承认 "The K=1 downstream gap conflates true coupling with train-inference mismatch"，但仍在主文中使用 "97.5%" 作为 headline 数字。
  2. **K=4 control 引入新的混淆变量**：K=4 的 MMLU 超过 E2E (42.7±1.4 vs 40.7±1.3，Table S in Appendix)，论文解释为 "near-uniform allocation matching uniform inference"（即 K=4 的 allocation pattern 恰好比 E2E 更适合 MMLU 的 uniform eval）。这说明 allocation strategy 本身就是一个混淆变量——K=4 改变了 coupling 的同时也改变了 learned allocation pattern。
  3. **Gap closure 方向不一致**：ARC-c 仅 2.6% closure（"coupling-dominated"），WG 33.3%，PPL 66.7%，MMLU >100%（anomalous）。四个 metric 指向截然不同的结论，无法支持一个单一的 "signal type dominates" 叙事。
  4. **论文自己在 footnote 5 中承认 "signal type and coupling scope are not fully orthogonal"**，但主文仍给出精确到小数点的 "97.5%" 上界，给读者虚假的分离精度。
- 为什么影响接收：§4.5 是论文的核心分析贡献之一。如果 decomposition 不 clean，论文的分析深度优势大幅减弱。
- 建议修改方向：
  - 将 "97.5%" 替换为定性描述："signal type accounts for the majority of the PPL gap (upper bound; confounded by train-inference mismatch at K=1)"
  - 在主文而非 footnote 中明确讨论 orthogonality limitation
  - 增加 K=4 在 50% sparsity 的实验（目前 50% 仅有 K=1，恰恰是 coupling 贡献最大的区间）

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 无实际推理加速，论文的效率动机与交付成果之间存在 gap

- 具体位置：Appendix A (Table 5), §1 (Introduction)
- 问题：Table 5 显示方法增加 6.4% 推理延迟 (126.78 vs 119.11 ms/fwd)。论文在 Introduction 中声明 "we do not address latency optimization (Appendix A)"，但论文的开篇叙事仍以 inference efficiency 为核心动机 ("inference allocates budgets globally via top-k ranking")。虽然论文定位为 empirical study，但缺乏实际 speedup 限制了实际影响力。
- 建议：在 Introduction 或 Conclusion 主文中（而非仅 Appendix）更显著地讨论这个 gap，并给出 wall-clock speedup 所需的具体条件（什么稀疏核、什么硬件约束），让读者能评估实际可行性。

**W2** [warning] 主表 (Table 2) 中 KL vs TEAL 在不匹配的实际稀疏度下比较

- 具体位置：Table 2, footnote ‡
- 问题：30% target 下 KL 实际稀疏度 28.5% vs TEAL 29.3%，相差 0.8pp。在 PPL 对稀疏度高度敏感的区间（见 Figure 2），这个差异非 negligible。论文在 Appendix C 中提供了 matched 28.5% 比较 (14.5%)，这比 Table 2 的 raw 数字 (18.6% = (10.82−8.81)/10.82) 低。Abstract 使用了更保守的 14.5%，这是好的，但 Table 2 给读者的第一印象是 18.6% improvement。
- 建议：在 Table 2 中增加一行 "TEAL at 28.5% actual sparsity" 或在 caption 中更显著标注 matched comparison。

**W3** [warning] 规模泛化不足

- 具体位置：§4.6 (Cross-Architecture and Scale)
- 问题：仅在 7–14B 模型上验证 (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B)。所有三个模型的 MMLU/GSM8K 均出现系统性下降（8B MMLU −5.2pp, 14B GSM8K −20pp），论文解释为 "a systematic property of distribution-matching objectives"。如果 KL 的 mode-covering 特性在更大规模下同样牺牲 reasoning 能力，该方法的适用性堪忧。
- 建议：如无法补充 70B 实验，至少在 Limitations 中明确讨论 "KL-based training may face a fundamental accuracy-fidelity trade-off on reasoning tasks that could worsen at scale"。

**W4** [warning] Table 2 中 KL global 50% 的下游评测不完整

- 具体位置：Table 2, KL global (Ours) 50% 行
- 问题：PPL 报告了 3-seed (11.84±0.15)，但 ARC-c (32.85)、WG (63.46)、MMLU (28.1)、GSM8K (1.29) 均无 ±，表明仅为 s42 单种子结果。同表中 KL uniform 50% 的 ARC-c 和 WG 都有 3-seed ±。这种不一致使读者无法评估 KL global 50% 下游的稳定性。
- 建议：补充 KL global 50% 的 3-seed 下游评测，或明确标注哪些是单种子结果。

**W5** [warning] K=4 decomposition 仅在 30% 做，50% 缺失

- 具体位置：§4.5
- 问题：50% 的 per-layer KL 仅有 K=1 结果 (PPL 34.85 vs E2E 11.92，gap 192%)。论文说 "coupling's share rising from 2.5% to 10.6% (4×)"，但这个 10.6% 完全来自 K=1，其中 train-inference mismatch 在 50% 处更严重（mask 50% 的神经元 vs 30%）。没有 K=4 的 50% 结果，无法判断 coupling 在高稀疏度下的真实贡献。
- 建议：补充 K=4 在 50% 的 3-seed 实验，或将 50% 的 coupling 贡献数字标注为 "confounded upper bound"。

---

## 小问题（不影响接收）

- **M1**: §4.3 extended training 部分，BCE 2700 steps (46 min) 的 wall-clock match 声明值得质疑——KL 需要两次 forward pass (dense + sparse) 而 BCE 仅一次，但 KL 1000 步与 BCE 2700 步花费相同时间。这意味着 BCE 每步更快？如果是，应解释原因（batch size 差异？BCE 不需要 dense forward pass？）。
- **M2**: Table 1 (Taxonomy) 中 SPON 被归入 "Static × Coupled"，但 SPON 是 per-layer bias，其 "coupling" 来自 KL loss 但 mask 不依赖 input。这个分类是否准确应在正文中讨论而非仅在 Appendix O。
- **M3**: Eq. 6 中 penalty 函数使用 $\text{clamp}(|\bar{s} - (1-\rho)| - \epsilon, \min=0)^2$——这是 squared hinge loss 形式，但论文称之为 "adaptive penalty controller"。实际的 "adaptive" 部分是 λ 的 geometric doubling，而非 penalty 函数本身。命名可能误导读者以为有更复杂的自适应机制。
- **M4**: Limitations 中提到 "Batched inference... may reduce effective sparsity"，但未讨论 sequence length 的影响——较长序列可能改变 activation pattern，影响 predictor mask 质量。

---

## Questions to Authors

1. **C1 circularity**: 如果在 magnitude-based masks 上训练 KL (而非 BCE)——即 "reverse C1"——结果会怎样？如果 KL coupling 在 magnitude targets 上也能达到好效果，这会进一步弱化 "mask patterns are the driver" 的声明。你们是否有这个实验？

2. **K=4 at 50%**: 为什么没有做 50% 的 K=4 实验？这是最能体现 coupling 贡献的区间。是否存在训练不稳定问题？

3. **MMLU 系统性下降**: 你们在三个架构上都观察到 MMLU 下降。这是否暗示 forward KL 的 mode-covering 特性系统性地损害了 reasoning-critical 的 neuron preservation？如果是，这对方法的适用范围有什么根本性限制？

4. **Sparsity controller 在 30% 的 5% deviation**: Appendix C 显示 30% target 下 λ 达到 cap (5000) 但实际稀疏度仅 28.5%。这是否意味着 penalty controller 在低稀疏度下力度不足？如果 λ_max 设更高，实际稀疏度能否逼近 30%？

---

## 主要优势

1. **研究问题有价值且定义清晰**：训练目标如何影响 learned sparsity predictor 的 mask quality 是一个 under-explored 但重要的问题，论文给出了系统性的实证分析。

2. **实验覆盖面广、消融设计用心**：3 个架构、2 个稀疏度水平、6+ 个下游任务、5 个 baseline（TEAL/BCE/MSE/Uniform/STE）、C1 target-swap、K=1/K=4 decomposition、SNR 分析。总实验量远超一般 EMNLP 投稿。

3. **梯度分析 (§3.6) 提供有用 insight**：BCE 梯度仅依赖 neuron j，KL 梯度通过下游 Jacobian 耦合所有层——这个 analysis 虽然是 standard chain rule，但在稀疏性预测场景下的应用是新颖的。配合 SNR 分析（KL 信号更噪但 mask 更好）构成了 "search mechanism > gradient clarity" 的有趣叙事。

4. **诚实的局限性讨论**：论文对 MMLU/GSM8K 下降、sparsity mismatch、K=1 confound 等问题有坦诚的讨论（虽然部分问题被放在 footnote/appendix 中显著性不够）。

5. **可复现性好**：所有超参数完整报告（lr、weight decay、τ schedule、batch size、steps、GPU 型号），exp_id 标注在 LaTeX 注释中，training 仅需 ~45 min 单卡。

---

**总结判断**: 论文的核心发现（KL > BCE for sparsity prediction）可信且有实验支撑。但两个关键因果分析（C1 和 signal-type decomposition）的 claim 强度超出实验证据，加之缺乏 wall-clock speedup 和规模泛化，建议评为 Borderline Conference (3.5)。如果 N1 和 N2 的 claim 调整为更审慎的措辞，本文有望进入 Conference (4.0) 档位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1816 · 2026-05-22T17:21:12.150848+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 和 Reviewer 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 和 Reviewer 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1817 · 2026-05-22T17:21:12.151464+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1818 · 2026-05-22T17:21:50.138322+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — Round 1\n\n以下是 **Reviewer 2** 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和 Questions，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n**Reviewer 2 Overall**: 3.0 (Findings), Soundness 3.5, Excitement 2.5\n\n### Must-Fix:\n\n**N1** [critical] 缺乏 wall-clock speedup——方法实际增加 6.4% 延迟\n- Appendix A (Table 5) 显示 126.78 vs 119.11 ms/forward (+6.4%)\n- TEAL 原论文已展示 1.53×/1.8× wall-clock speedup\n- 作为 efficiency-motivated 工作，无加速数据使贡献仅限分析层面\n\n**N2** [critical] MMLU/GSM8K 系统性退化未充分解释\n- Table 2: 30% MMLU 40.7 vs 45.86, GSM8K 7.5 vs 8.79\n- Qwen-14B: GSM8K −20pp\n- Remove Valley 实验（Appendix T）可恢复 MMLU +3.3pp 但未追踪此线索\n- \"distribution-matching objectives sacrifice reasoning pathways\" 是描述非解释\n\n**N3** [critical] 与 MaskLLM 区分度不足\n- 核心 recipe 完全共享：frozen model + learnable masks + KL + Gumbel\n- §2 列出的 3 个差异主要是应用场景差异，非方法论创新\n- 2D taxonomy 是简单分类而非 intellectual contribution\n\n### Should-Fix:\n\n**W1** [warning] 缺少与 R-Sparse, CATS, DIP 等 training-free 方法的实验对比\n**W2** [warning] Figure 2 仅展示 global allocation 但推荐 uniform——存在误导\n**W3** [warning] Conclusion 过于密集且遗漏 limitation 信号；BoolQ 出现在 Conclusion 但不在 Table 2\n**W4** [warning] C1 soft-vs-hard confound 未完全解耦\n**W5** [warning] Abstract 信息密度过高，第5句约60词难以一遍理解\n\n### Questions:\n1. Remove Valley 可恢复 MMLU +3.3pp，为何不作为默认配置？\n2. 能否提供 uniform allocation 下的 PPL scaling 数据？\n3. \"14.5% PPL reduction\" 是 matched (28.5%) 还是 target (30%) sparsity？\n4. WikiText-103 仅 1000 steps 训练是否足够？C4 CV=6.3% 暗示过拟合？\n5. §3.6 gradient coupling 发现 68% divergent masks，但 C1 说 mask patterns 是 driver 而非 coupling——关系需要更清晰阐述。\n\n### Missing References:\n1. LaRoSA (2025, arXiv:2507.01299)\n2. Geva et al. (2023) 已在 bib 中但正文未引用\n\n### Minor: M1-M7（Table 2 注释过多、ε=0.02 无 justification、Jaccard vs random baseline、MMLU 方差讨论不足、FastForward 引用更新、d_ff 排版、Table 编号检查）\n\n---\n\n请逐条回应。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — Round 1\n\n以下是 **Reviewer 2** 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和 Questions，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n**Reviewer 2 Overall**: 3.0 (Findings), Soundness 3.5, Excitement 2.5\n\n### Must-Fix:\n\n**N1** [critical] 缺乏 wall-clock speedup——方法实际增加 6.4% 延迟\n- Appendix A (Table 5) 显示 126.78 vs 119.11 ms/forward (+6.4%)\n- TEAL 原论文已展示 1.53×/1.8× wall-clock speedup\n- 作为 efficiency-motivated 工作，无加速数据使贡献仅限分析层面\n\n**N2** [critical] MMLU/GSM8K 系统性退化未充分解释\n- Table 2: 30% MMLU 40.7 vs 45.86, GSM8K 7.5 vs 8.79\n- Qwen-14B: GSM8K −20pp\n- Remove Valley 实验（Appendix T）可恢复 MMLU +3.3pp 但未追踪此线索\n- \"distribution-matching objectives sacrifice reasoning pathways\" 是描述非解释\n\n**N3** [critical] 与 MaskLLM 区分度不足\n- 核心 recipe 完全共享：frozen model + learnable masks + KL + Gumbel\n- §2 列出的 3 个差异主要是应用场景差异，非方法论创新\n- 2D taxonomy 是简单分类而非 intellectual contribution\n\n### Should-Fix:\n\n**W1** [warning] 缺少与 R-Sparse, CATS, DIP 等 training-free 方法的实验对比\n**W2** [warning] Figure 2 仅展示 global allocation 但推荐 uniform——存在误导\n**W3** [warning] Conclusion 过于密集且遗漏 limitation 信号；BoolQ 出现在 Conclusion 但不在 Table 2\n**W4** [warning] C1 soft-vs-hard confound 未完全解耦\n**W5** [warning] Abstract 信息密度过高，第5句约60词难以一遍理解\n\n### Questions:\n1. Remove Valley 可恢复 MMLU +3.3pp，为何不作为默认配置？\n2. 能否提供 uniform allocation 下的 PPL scaling 数据？\n3. \"14.5% PPL reduction\" 是 matched (28.5%) 还是 target (30%) sparsity？\n4. WikiText-103 仅 1000 steps 训练是否足够？C4 CV=6.3% 暗示过拟合？\n5. §3.6 gradient coupling 发现 68% divergent masks，但 C1 说 mask patterns 是 driver 而非 coupling——关系需要更清晰阐述。\n\n### Missing References:\n1. LaRoSA (2025, arXiv:2507.01299)\n2. Geva et al. (2023) 已在 bib 中但正文未引用\n\n### Minor: M1-M7（Table 2 注释过多、ε=0.02 无 justification、Jaccard vs random baseline、MMLU 方差讨论不足、FastForward 引用更新、d_ff 排版、Table 编号检查）\n\n---\n\n请逐条回应。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1819 · 2026-05-22T17:22:13.940120+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23801
}
```

</details>

---


### Tool call

_source line 1820 · 2026-05-22T17:22:14.845215+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — Round 1\n\n以下是 **Reviewer 1** 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N2)、Should-Fix (W1-W5) 和 Questions，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n**Reviewer 1 Overall**: 3.5 (Borderline Conference), Soundness 3.5, Excitement 3.0\n\n### Must-Fix:\n\n**N1** [critical] C1 Target-Swap Ablation 因果推断存在循环性，causal claim 过强\n- KL-derived masks 本身是 KL coupling 的产物，C1 不能分离 mask quality 和 discovery mechanism\n- s42 使用 \"earlier checkpoint\" oracle (PPL gap 0.65pp) vs s123/s456 matched oracle (gap ≤0.03pp) 不一致\n- 下游方向不一致：s42 C1 在 MMLU +1.7pp 但 s456 C1 在 MMLU −0.96pp\n- 建议 claim 降级为 \"transferability\" 而非 \"proximate quality driver\"\n\n**N2** [critical] 97.5% signal type decomposition 受严重混淆变量影响\n- K=1 train-inference mismatch：训练 mask 1/32 层 vs 推理 mask 全部 32 层\n- K=4 引入 allocation pattern 变化作为新混淆变量（MMLU >100% gap closure = anomalous）\n- 四个 metric 指向截然不同结论（ARC-c 2.6% vs PPL 66.7% vs MMLU >100%）\n- Footnote 5 承认 \"not fully orthogonal\" 但主文仍给精确 97.5%\n- 建议替换为定性描述 + 50% K=4 实验\n\n### Should-Fix:\n\n**W1** [warning] 无实际推理加速，Intro 效率动机与交付成果有 gap\n**W2** [warning] Table 2 中 KL 28.5% vs TEAL 29.3% 的 actual sparsity mismatch\n**W3** [warning] 规模泛化不足（7-14B），reasoning 下降可能随规模恶化\n**W4** [warning] Table 2 KL global 50% 的下游仅 s42 单种子\n**W5** [warning] K=4 decomposition 仅在 30% 做，50% 缺失\n\n### Questions:\n1. \"Reverse C1\"——在 magnitude masks 上训练 KL 结果如何？\n2. 为何 50% 没做 K=4？是否训练不稳定？\n3. MMLU 系统性下降是否暗示 forward KL mode-covering 的根本限制？\n4. 30% target λ 达 cap (5000) 但实际仅 28.5%——λ_max 设更高能否逼近 30%？\n\n### Minor: M1-M4（BCE wall-clock match 疑问、SPON taxonomy 分类、adaptive penalty 命名、sequence length 影响）\n\n### Strengths:\n1. 研究问题有价值且定义清晰\n2. 实验覆盖面广、消融设计用心\n3. 梯度分析 (§3.6) 有用\n4. 诚实的局限性讨论\n5. 可复现性好\n\n---\n\n请逐条回应。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — Round 1\n\n以下是 **Reviewer 1** 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N2)、Should-Fix (W1-W5) 和 Questions，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n**Reviewer 1 Overall**: 3.5 (Borderline Conference), Soundness 3.5, Excitement 3.0\n\n### Must-Fix:\n\n**N1** [critical] C1 Target-Swap Ablation 因果推断存在循环性，causal claim 过强\n- KL-derived masks 本身是 KL coupling 的产物，C1 不能分离 mask quality 和 discovery mechanism\n- s42 使用 \"earlier checkpoint\" oracle (PPL gap 0.65pp) vs s123/s456 matched oracle (gap ≤0.03pp) 不一致\n- 下游方向不一致：s42 C1 在 MMLU +1.7pp 但 s456 C1 在 MMLU −0.96pp\n- 建议 claim 降级为 \"transferability\" 而非 \"proximate quality driver\"\n\n**N2** [critical] 97.5% signal type decomposition 受严重混淆变量影响\n- K=1 train-inference mismatch：训练 mask 1/32 层 vs 推理 mask 全部 32 层\n- K=4 引入 allocation pattern 变化作为新混淆变量（MMLU >100% gap closure = anomalous）\n- 四个 metric 指向截然不同结论（ARC-c 2.6% vs PPL 66.7% vs MMLU >100%）\n- Footnote 5 承认 \"not fully orthogonal\" 但主文仍给精确 97.5%\n- 建议替换为定性描述 + 50% K=4 实验\n\n### Should-Fix:\n\n**W1** [warning] 无实际推理加速，Intro 效率动机与交付成果有 gap\n**W2** [warning] Table 2 中 KL 28.5% vs TEAL 29.3% 的 actual sparsity mismatch\n**W3** [warning] 规模泛化不足（7-14B），reasoning 下降可能随规模恶化\n**W4** [warning] Table 2 KL global 50% 的下游仅 s42 单种子\n**W5** [warning] K=4 decomposition 仅在 30% 做，50% 缺失\n\n### Questions:\n1. \"Reverse C1\"——在 magnitude masks 上训练 KL 结果如何？\n2. 为何 50% 没做 K=4？是否训练不稳定？\n3. MMLU 系统性下降是否暗示 forward KL mode-covering 的根本限制？\n4. 30% target λ 达 cap (5000) 但实际仅 28.5%——λ_max 设更高能否逼近 30%？\n\n### Minor: M1-M4（BCE wall-clock match 疑问、SPON taxonomy 分类、adaptive penalty 命名、sequence length 影响）\n\n### Strengths:\n1. 研究问题有价值且定义清晰\n2. 实验覆盖面广、消融设计用心\n3. 梯度分析 (§3.6) 有用\n4. 诚实的局限性讨论\n5. 可复现性好\n\n---\n\n请逐条回应。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1821 · 2026-05-22T17:22:16.157354+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1312
}
```

</details>

---


### Assistant

_source line 1822 · 2026-05-22T17:22:26.480974+00:00_

交叉分享已发出。两位 Reviewer 正在逐条回应对方意见，等待交叉回应结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 155

## Round 155

2 recorded events


### User

_source line 1823 · 2026-05-22T17:22:29.013400+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**评审要点总结**：

- **Overall 3.5/5 (Borderline Conference)**，Soundness 3.5，Excitement 3.0
- **两个 Must-Fix**：(1) C1 target-swap ablation 的因果声明存在循环性——实验证明 mask 可转移但不能证明 "mask 是唯一质量驱动因素"；(2) 97.5% signal-type decomposition 受 K=1 train-inference mismatch 严重混淆，K=4 引入新的 allocation confound（MMLU anomaly），精确数字不可靠
- **五个 Should-Fix**：无实际推理加速、Table 2 sparsity mismatch 不显著标注、规模仅 7–14B、KL global 50% 下游缺 3-seed、K=4 在 50% 缺失
- **核心判断**：KL > BCE 的发现可信，但两个分析性 contribution 的 claim 需降级为更审慎的措辞后方可进入 Conference 档位

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1824 · 2026-05-22T17:22:36.132402+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 156

## Round 156

14 recorded events


### User

_source line 1825 · 2026-05-22T17:24:06.586418+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[REBUT] R2-N1: 缺乏 wall-clock speedup**

R2 将此列为 critical，我在自己的审稿中将其列为 Should-Fix (W1)。理由如下：

1. 论文在 Introduction (§1, p.2) 明确声明："this paper is primarily an empirical study; we do not propose a new architecture or algorithm, but rather characterize how the training objective shapes sparsity prediction quality"，并紧接着说 "Wall-clock speedup requires sparse kernel support; we do not address latency optimization (Appendix A)"。论文的自我定位是分析性工作，不是系统工作。

2. R2 援引 TEAL 原论文展示了 1.53×/1.8× speedup，但 TEAL 使用了 Triton semi-structured kernel——这是一个 systems-level 贡献，与 mask quality（本文关注点）正交。本文的 predictor 产生的 mask 可以直接 plug into TEAL 的 kernel pipeline（§4.1 "predictor-TEAL" protocol），因此 TEAL 展示的加速原则上也适用于 KL-derived masks。

3. 但我同意 R2 的一个隐含观点：**论文应在主文中更清晰说明 speedup 路径**，而非仅靠 Appendix A 一段话。这是我在 W1 中提出的相同建议。

判断：应为 **Should-Fix** 而非 Must-Fix。论文的贡献在于 mask quality analysis，而非 system speedup。如果将此升级为 Must-Fix，大量分析性论文（如 pruning 方法比较、distillation 目标分析）都会因 "无端到端系统集成" 而被拒——这不是合理的 review standard。

---

**[AGREE] R2-N2: MMLU/GSM8K 系统性退化未充分解释**

同意这是一个需要更深入处理的问题，但我认为严重程度介于 Should-Fix 和 Must-Fix 之间。

1. 论文确实在 Table 2 中展示了 30% sparsity 下 MMLU 从 45.86 (TEAL) 降至 40.7 (KL uniform)，降幅 −5.2pp。且这不是随机波动——跨三个架构一致出现（§4.6: "the consistent regression across scales (8B MMLU −5.2pp, 14B GSM8K −20pp) suggests a systematic property of distribution-matching objectives"）。

2. R2 指出 Remove Valley（Appendix T, Table 20）可恢复 MMLU +3.3pp（40.7→44.0），说明中间层保护是 MMLU 下降的直接原因。但论文承认这以 ARC-c −4.4pp 为代价——这是 task-dependent trade-off，不是 free lunch。**然而 R2 正确指出论文未追踪这个线索**：如果 remove valley 可以恢复 reasoning 而仅损失 commonsense，为什么不探索 task-aware allocation？

3. R2 对 "distribution-matching objectives sacrifice reasoning pathways" 的批评有道理——这是描述而非解释。论文没有给出 mechanistic explanation 为什么 forward KL 的 mode-covering 会系统性损害 reasoning neurons。

我的判断：**Should-Fix to borderline Must-Fix**。不同于 N1，这个问题直接影响方法的 soundness 判断——如果 KL training 在最重要的 benchmark 上系统性退化，方法的适用性存疑。

---

**[REBUT] R2-N3: 与 MaskLLM 区分度不足**

不同意这是 critical issue。

1. **核心区别是 contextual vs static masks，这不是 "应用场景差异" 而是 fundamental architectural choice**。MaskLLM（§2, p.3）学习 "fixed per-input masks" (static N:M patterns)——每层每 token 的 mask 固定，不依赖输入。本文的 predictor 根据 x^(ℓ)（attention 后的 hidden state）动态生成 per-token masks。这意味着：
   - MaskLLM 的 mask 无法适应 unseen inputs（论文 §2: "MaskLLM's masks are fixed per input... must be robust to distribution shift at inference"）
   - 本文的 predictor 为每个 token 生成不同 mask，可以 coordinate across layers through global top-k（§3.1 Eq. 2）

2. **Cross-layer allocation 是本文独有的**。MaskLLM 没有 cross-layer budget distribution（论文 §2: "no cross-layer allocation interaction"）。本文通过 TEAL 的 global top-k 实现 cross-layer 预算分配，这直接影响了 §4.5 中 coupling scope 的分析。

3. **2D taxonomy 的价值**：同意 R2 的判断——taxonomy 本身不是 intellectual contribution，我在自己的审稿中也未将其列为优势。但 taxonomy 确实组织了 Related Work 并引出了可测试的预测（coupled > intermediate > decomposed），论文在 §4.5 中验证了这个预测。

4. **Recipe 层面的共享不等于方法论重叠**。"frozen model + learnable masks + KL" 也是 knowledge distillation 的标准 recipe——如果这构成区分度不足，那大量 distillation 工作都不可接受。关键是 what you train (contextual predictor vs static masks)、what you optimize through (per-layer vs cross-layer)、和 what you analyze (mask pattern quality, signal-type decomposition)。

判断：应降级为 **Minor** 或至多 **Should-Fix**（需要在 §2 中更清晰对比 MaskLLM 的 contribution boundary）。将其列为 Must-Fix 不合理。

---

### Should-Fix

**[REBUT] R2-W1: 缺少与 R-Sparse, CATS, DIP 的实验对比**

部分不同意。

1. 这些方法与本文不在同一设计空间内：
   - **R-Sparse**（Zhang et al., 2025b）从 rank-aware SVD projections 预测稀疏性——不同的 predictor architecture 和 scoring mechanism
   - **CATS**（Lee et al., 2024）adapts per-layer thresholds for SiLU/SwiGLU activation——training-free 方法，与 learned predictor 不可直接比较训练目标
   - **DIP**（Federici et al., 2024）combines dynamic input pruning with cache-aware masking——不同的 sparsity granularity

2. 论文选择 TEAL 作为 primary baseline 是合理的：TEAL 是最接近的 training-free 方法（activation-magnitude scoring + global top-k），本文的 predictor 直接替换 TEAL 的 scoring（§4.1: "predictor-TEAL"）。BCE baseline 覆盖了 learned predictor 的比较。

3. **但 R2 有一个 valid 点**：如果 CATS 或 R-Sparse 在 MMLU/GSM8K 上不像 TEAL 那样退化，这可能说明 KL training 的 reasoning degradation 不是稀疏性的固有代价。补充一个 training-free baseline（如 CATS）的数字会增强论文的 contextualization。

判断：保持 Should-Fix 级别，建议补充 1-2 个 training-free 方法的数字作为 context。

---

**[AGREE] R2-W2: Figure 2 仅展示 global allocation 但推荐 uniform**

同意。Figure 2 caption 标注 "(global allocation)"，但论文在 §4.6 和 Table 2 中推荐 uniform allocation（特别是 ≤30% 时）。读者自然会用 Figure 2 理解 PPL scaling 趋势，但实际推荐的 operating point 使用不同的 allocation。建议补充 uniform allocation 的 scaling curve 或在 caption 中明确说明。

---

**[AGREE] R2-W3: Conclusion 密度 + BoolQ 问题**

同意。Conclusion (§5) 引用了 BoolQ 数据但 BoolQ 不在 Table 2 主表中（仅在 Appendix S Table K=4 中出现且 variance 极高: std=11.5）。在 conclusion 中引用一个仅在 appendix 出现且不可靠的 metric 是不审慎的。

---

**[AGREE] R2-W4: C1 soft-vs-hard confound 未完全解耦**

同意，且这与我自己的 N1 一致。论文在 §4.4 讨论了 BCE+Gumbel (32.22) vs standard BCE (27.97) 来 argue softness 不是主要因素，但这个比较本身也有问题：BCE+Gumbel 加了 Gumbel noise 但没有正确的 sparsity target，所以 PPL 恶化可能来自 sparsity 偏移而非 softness 本身。论文将详细讨论推到 Appendix P，但主文的 claim 强度（"softness alone does not explain"）需要在 Appendix 有更严格的支撑。

---

**[AGREE] R2-W5: Abstract 信息密度过高**

同意。Abstract 第 5 句 ("Output-distribution optimization yields masks that diverge 46–68% from magnitude-based targets; a target-swap ablation suggests these discovered patterns—not the training mechanism itself—as the proximate quality driver.") 约 30 词包含了两个独立 claim + 一个因果声明。建议拆分为两句。

---

### Questions

**R2-Q1: Remove Valley 为何不作为默认配置？**

好问题。Appendix T (Table 20) 显示 remove valley: MMLU +3.3pp, GSM8K +1.5pp, ARC-c −4.4pp。论文将此解读为 "task-dependent trade-off" 但未讨论为什么不提供 task-aware 配置选项。如果用户关心 MMLU 多于 ARC-c，remove valley 就是更好的默认。这值得在论文中讨论。

**R2-Q2: Uniform allocation 下的 PPL scaling 数据？**

同意这是有价值的补充。Figure 2 仅展示 global，uniform 的 scaling 行为可能不同。

**R2-Q3: "14.5% PPL reduction" 是 matched 还是 target sparsity？**

这个问题在论文中有明确回答。§4.2: "reducing TEAL's perplexity by 19% (10.82 → 8.81; 14.5% at matched 28.5% sparsity, Appendix D)"。Abstract 也使用 "at matched sparsity"。14.5% 是在 matched 28.5% actual sparsity 下计算的。R2 如果读到了 §4.2 这句应该不会有此疑问——但这也侧面说明 Table 2 的呈现方式不够清晰（呼应我的 W2 和 R2 的 Q3）。

**R2-Q4: WikiText-103 1000 steps 是否足够？C4 CV=6.3%？**

1. Appendix B.2 (Table 8) 显示 PPL 在 step 600 时已达 95% quality (12.046 vs final 11.906)，step 800 后 Δ < 0.001。1000 steps 提供 conservative margin。
2. C4 CV=6.3% 主要来自 seed 42 的异常值 (18.22 vs s123/s456 的 16.37)。WikiText-2 的 CV=0.2% 说明 predictor 本身稳定。C4 上较高的 variance 更可能反映 **domain shift sensitivity**（不同种子学到的 mask pattern 在 OOD 下表现差异）而非 training insufficiency。但这确实暗示 generalization 有改进空间。

**R2-Q5: §3.6 gradient coupling vs C1 的关系**

同意这个关系需要更清晰阐述——这也是我自己 N1 的核心关切。当前叙事的矛盾是：§3.6 argue gradient coupling 是 KL 优势的来源（通过 downstream Jacobian 耦合），但 §4.4 C1 argue mask patterns（而非 coupling）是质量驱动因素。如果 coupling 的作用仅在于 **发现** 好的 mask（training-time effect），而非 **维持** 好的 mask（inference-time effect），论文应更清晰区分这两个层面。当前的措辞（"not the training mechanism itself"）过于绝对。

---

### Missing References

**R2-Ref1: LaRoSA (2025, arXiv:2507.01299)**

无法评估——我不确认这篇论文是否已在 ARR 提交截止日前（2026-05-25）公开。如果是，应引用。

**R2-Ref2: Geva et al. (2023)**

同意应在正文中引用，如果 bib 中已有但正文未 cite，这是一个遗漏。

---

### Minor Issues (M1-M7)

简要回应：
- **M1 (Table 2 注释过多)**: [AGREE] Table 2 有 5 个不同的 footnote symbols (*, †, ±, ‡, §)，确实增加认知负担。
- **M2 (ε=0.02 无 justification)**: [AGREE] §3.5 仅说 "ε = 0.02 is a deadzone margin" 但未解释为何选 0.02 而非其他值。
- **M3 (Jaccard vs random baseline)**: [REBUT] 论文在 Appendix F.1 中给出了 random baseline Jaccard distance = 0.462，且在 §4.4 中比较了 cross-seed divergence (36.3%) vs KL-vs-magnitude divergence (46-68%)。这个 context 已经提供。
- **M4-M7**: [AGREE] 均为 valid editorial improvements。

---

### 总结

R2 的 Overall 3.0 (Findings) 比我的 3.5 (Borderline Conference) 低 0.5 分。主要分歧在于：

1. **Wall-clock speedup (R2-N1)**: R2 视为 critical，我视为 Should-Fix。论文明确定位为 analysis 而非 system work，降级为 Should-Fix 更合理。

2. **MaskLLM 区分度 (R2-N3)**: R2 视为 critical，我认为应为 Minor/Should-Fix。Contextual vs static masks 是 fundamental difference，不是 "应用场景差异"。

3. **MMLU 退化 (R2-N2)**: 我们基本一致——这是一个 real 问题，介于 Should-Fix 和 Must-Fix 之间。

如果 N1 和 N3 降级为 Should-Fix（我认为有充分理由），R2 的评分应上调至 3.5 左右，与我的评估一致。

---

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1

## Must-Fix

**[AGREE] R1-N1: C1 Target-Swap Ablation 因果推断存在循环性**

同意 R1 的核心论点。我在自己的审稿 W4 中也指出了 C1 的 soft-vs-hard confound，R1 进一步揭示了更根本的循环性问题：KL masks 本身就是 KL coupling 的产物，用它们训练 BCE 只能证明 mask patterns 的可迁移性（transferability），而非它们是 "proximate quality driver"。

补充 R1 未提及的一点：§4.3 "Soft-vs-Hard Confound" 段的控制实验逻辑有瑕疵——BCE+Gumbel (32.22) 比 standard BCE (27.97) 更差，这说明 Gumbel relaxation 在 BCE 设置下是有害的，无法作为 "softness 不是主因" 的中性控制。

s42 使用 earlier checkpoint oracle（PPL gap 0.65pp）vs s123/s456 matched oracle（gap ≤0.03pp）的不一致确实削弱说服力。Table 3 s42 行的 ‡ 标注容易被忽略。不过，s123/s456 的 matched oracle 结果（PPL gap ≤0.03pp）本身仍提供了有意义的证据——只是论文不应以 s42 的 0.65pp gap 作为主要叙事。

建议将 claim 从 "proximate quality driver" 降级为 "transferable quality patterns"，这仍是一个有价值的发现。

**[AGREE] R1-N2: 97.5% signal type decomposition 受严重混淆变量影响**

完全同意。这是我认为论文最大的表述问题之一。

关键证据：
1. K=1 的 train-inference mismatch 是根本性的。训练时只 mask 1/32 层，推理时 mask 全部 32 层——这不是 "isolating coupling" 而是引入了一个巨大的 distribution shift confound。论文在 Footnote 5 承认维度 "not fully orthogonal"，但 97.5% 这个数字在 Abstract（第5句）、Introduction（contribution list 第1条）、Conclusion（第1句）中反复出现，给读者的印象远比 caveat 强烈。
2. K=4 控制实验（Appendix S, Table 19）确实减轻了 mismatch，但引入了新 confound：K=4 的 near-uniform per-layer sparsity（std=0.003）恰好匹配 uniform eval allocation，导致 MMLU >100% gap closure——这是 allocation alignment 的 artifact 而非 coupling 的真实效应。论文在 Appendix S footnote 中承认了这一点，但这实际上意味着 K=4 也不是一个干净的控制。
3. 四个 metric 的分歧（R1 正确指出：ARC-c 2.6% vs PPL 66.7% vs MMLU >100%）说明这个 decomposition 框架本身不稳定，无法支撑精确的定量结论。

同意 R1 的建议：替换为定性描述（"signal type is the dominant factor for PPL; coupling contributes meaningfully to some downstream tasks"）比精确的 97.5% 更诚实也更有说服力。

## Should-Fix

**[AGREE] R1-W1: 无实际推理加速**

强烈同意，这也是我的 N1（critical 级别）。Appendix A Table 5 显示方法实际增加 6.4% 延迟。作为 efficiency-motivated 工作，这是核心缺陷。

**[AGREE] R1-W2: Table 2 actual sparsity mismatch (KL 28.5% vs TEAL 29.3%)**

同意这是一个公平性问题。论文在 Appendix C 提供了 matched comparison（28.5%: 8.81 vs 10.30 = 14.5% reduction），但 Table 2 的主比较（8.81 vs 10.82 at nominal 30%）夸大了优势。Table 2 的 ‡ 脚注（"Actual sparsity: KL 28.5% vs TEAL 29.3%"）容易被忽略。建议在 Table 2 中使用 matched sparsity 的结果作为主要比较。

**[AGREE] R1-W3: 规模泛化不足（7-14B）**

同意。Table 13（Appendix K）的 Qwen-14B 结果（GSM8K −20pp vs dense，MMLU −16pp vs dense at 30%）暗示 reasoning 退化可能随规模恶化。但我要补充一个 nuance：Qwen-14B 的 dense 基线本身远强于 LLaMA-8B（MMLU 79.77 vs 65.27），绝对下降幅度不直接可比。相对退化率需要更仔细的分析。

**[AGREE] R1-W4: KL global 50% 下游仅 s42 单种子**

同意。Table 2 中 KL global 50% 的 ARC-c (32.85)、WG (63.46)、GSM8K (1.29) 均为 s42 单种子结果，仅 PPL (11.84±0.15) 和 MMLU (28.1±0.2, from Appendix F) 有多种子报告。对于声称 global allocation 在 50% 优于 uniform 的 claim（§4.5 Allocation Behavior），单种子证据不够充分。KL uniform 50% 的全部指标都有 3-seed 报告，两者标准不一致。

**[REBUT] R1-W5: K=4 decomposition 仅在 30% 做，50% 缺失**

部分同意但认为不应列为 Should-Fix。论文在 §4.5 最后一段已报告 50% K=1 结果（per-layer KL 34.85 vs E2E KL 11.92, +192% gap），并指出 "coupling's share rising from 2.5% to 10.6% (4×)"。50% 时不做 K=4 可能有合理原因：(1) 50% 是 capacity-limited regime，所有方法的 downstream 都接近 random（MMLU ~28%），K=4 的 downstream decomposition 在 noise floor 附近意义不大；(2) K=4 训练可能在 50% 不稳定（R1 Q2 也在问这个问题）。论文应解释原因，但缺失本身不构成重大缺陷。

## Questions

**[AGREE] R1-Q1: "Reverse C1"（在 magnitude masks 上训练 KL）**

非常好的实验建议。如果 KL trained on magnitude masks 的表现接近 standard KL（即 KL 的 training mechanism 本身比 mask targets 更重要），则直接反驳论文的 C1 结论。这是我在自己审稿 Q5 中类似的问题——如果 coupling 主要用来 discover masks，是否可以用 KL 训练后提取 masks 再用 BCE 部署？Reverse C1 可以直接回答这个问题。

**[AGREE] R1-Q2: 为何 50% 没做 K=4？**

如上所述（我对 W5 的回应），这是一个合理的问题。论文应解释是资源限制还是训练不稳定。

**[AGREE] R1-Q3: MMLU 系统性下降是否暗示 forward KL mode-covering 的根本限制？**

完全同意这是一个核心问题。我在 N2 中详细分析了这一点。论文在 §3.4 中以 mode-covering 作为选择 forward KL 的理论动机（"false negatives cascade through downstream layers"），但 MMLU/GSM8K 的系统性退化恰好说明 mode-covering 可能在覆盖 "breadth" 时牺牲了 reasoning-critical pathways 的 "precision"——这与 reverse KL 的 mode-seeking 形成了未被讨论的 trade-off。更值得关注的是 Appendix T 的 Remove Valley 实验（MMLU +3.3pp），暗示退化部分源于可纠正的 allocation 问题而非 KL 目标的固有限制。

**[AGREE] R1-Q4: λ_max cap 问题**

技术细节问题但有价值。Table 9（Appendix C）显示 30% target 时 λ 达到 cap (5000) 但实际仅 28.5%（5% deviation）。这说明 adaptive penalty controller 在 30% 时已饱和，提高 λ_max 可能帮助逼近 30%，进而消除 W2 的 actual sparsity mismatch 问题。论文应在 Appendix 中报告 λ_max sensitivity。

## Minor

**[AGREE] R1-M1 (BCE wall-clock match)**: 论文声称 BCE 2700 steps 的 wall-clock 与 KL 1000 steps 相当（~46 vs ~45 min, §4.3），但 BCE 不需要 dense forward pass（仅需 magnitude targets），每步应更快。如果实际 wall-clock 接近，需要解释为什么。

**[REBUT] R1-M2 (SPON taxonomy 分类)**: SPON 使用 closed-form KL minimization per layer，确实是 "coupled" signal（KL on output distribution）但 "static" granularity（fixed bias per layer）。将其放在 Static × Coupled 格子中是合理的——R1 可能认为 SPON 的 per-layer KL 不算 "coupled"，但 Table 1 的 "coupled" 定义是 "whether the objective captures inter-neuron dependencies"，SPON 的 KL 目标确实耦合了同一层内的所有 neuron。

**[AGREE] R1-M3 (adaptive penalty 命名)**: "Adaptive Penalty Controller" 确实不是标准的 Lagrangian——它使用 geometric doubling + deadzone 而非经典的 dual ascent。命名应更准确。

**[AGREE] R1-M4 (sequence length 影响)**: 训练和评估都固定 seq_len=2048，未分析更长序列下的行为。这对 batched inference 和 long-context 场景的 generalization 是合理的 concern。

## Strengths 回应

完全同意 R1 列出的 5 个优势。特别是 S4（诚实的局限性讨论）——论文在多处主动 caveat confounds 和 upper bounds，这在该领域并不常见。我在自己的审稿 S4 中也独立指出了这一点。

## 总结

R1 和 R2 的审稿意见高度一致：
- **共识 Critical**: C1 causal claim 过强（R1-N1 ≈ R2-W4）、wall-clock speedup 缺失（R1-W1 = R2-N1）、MMLU/GSM8K 退化（R2-N2）
- **共识 Warning**: actual sparsity mismatch（R1-W2）、规模泛化不足（R1-W3 ≈ R2-N2 部分）
- **唯一分歧**: R1 将 97.5% decomposition confound 列为 N2 (critical)，我在 W 级别提及但同意 R1 升级为 critical 是合理的——因为 97.5% 出现在 Abstract/Intro/Conclusion 的核心位置，misleading 的影响范围大。

综合来看，我维持 **Overall 3.0 (Findings)** 的评分。R1 给 3.5 (Borderline Conference) 略高于我，差异主要在 Excitement 评分（R1: 3.0 vs 我: 2.5）——R1 更肯定研究问题的价值，而我对与 MaskLLM 的区分度更严格。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1826 · 2026-05-22T17:24:45.452557+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 和 Reviewer 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 和 Reviewer 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1827 · 2026-05-22T17:24:45.452957+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1828 · 2026-05-22T17:24:50.770740+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1829 · 2026-05-22T17:24:50.921714+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T17:12:10.100630+00:00\", \"completed_at\": \"2026-05-22T17:12:13.760192+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 6pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1830 · 2026-05-22T17:24:50.922236+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1831 · 2026-05-22T17:24:50.922532+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-22T17:12:10.921256+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_dbbf8d2c695f1e79e11713aebc107790\", \"skipped_at\": \"2026-05-22T17:17:56.113647+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1832 · 2026-05-22T17:28:04.392610+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 22 (fresh review) — Active issues\n  # ============================================================\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap ablation 因果声明过强: 'proximate quality driver' 超出实验证据\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"R19-N2 Critical。循环论证 + soft-vs-hard confound。\"}\n      - {round: 20, reviewers: [1, 2], note: \"R20-W3 Major→Warning。reframe 部分有效。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-W1 Major。3-seed 一致性提供 robustness, 'suggests' hedging 被认可。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R1-N1 Critical + R2-W4 Warning。s42 earlier checkpoint oracle (0.65pp gap) vs s123/s456 matched (≤0.03pp) 不一致; downstream 方向跨 seed 不一致 (s42 MMLU +1.7 vs s456 -0.96); soft-vs-hard confound BCE+Gumbel 控制实验逻辑有瑕疵。建议降级为 transferability claim。\"}\n    action_items:\n      - {round: 19, action: \"Paper Agent: reframe 为 transferability + circularity caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 20, action: \"Paper Agent: 'confirms'→'suggests' 全文替换\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"将 'proximate quality driver' 降级为 'transferable quality patterns'; 删除 'not the training mechanism itself' 排除性声明; 主文明确列出无法完全解耦的原因\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"97.5% signal type decomposition 受 K=1 train-inference mismatch 严重混淆; 精确数字给人虚假精确感\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] downstream 24-35% coupling 可能主要来自 mismatch。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-N2 Critical + R2-W1/W2 Major。97.5% 在 Abstract/Conclusion 无 caveat。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R1-N2 Critical + R2 交叉同意升级 Critical。K=1 mismatch 根本性; K=4 引入 allocation confound (MMLU >100% gap closure); 四个 metric 指向截然不同结论 (ARC-c 2.6% vs PPL 67% vs MMLU >100%); 建议替换为定性描述。\"}\n    action_items:\n      - {round: 20, action: \"Agent: K=4 per-layer KL pilot 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 21, action: \"Abstract/Conclusion 97.5% 加 caveat + K=4 multi-seed\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"将 '97.5%' 替换为定性描述: 'signal type accounts for the majority of the PPL gap'; 在主文而非 footnote 讨论 orthogonality limitation; 补充 K=4 at 50% 实验(如可行)\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨三个架构系统性退步, 机制解释不充分\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 22\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W8。14B 仅 30% sparsity。\"}\n      - {round: 19, reviewers: [1, 2], note: \"R19-W2/W3。GSM8K -20pp σ=5.2pp。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 升级为 Critical。跨三架构一致。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-N3 Major + R2-W4。Protection valley 分析仅 correlational, 缺 interventional 验证。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R2-N2 Critical + R1 borderline Must-Fix。Remove Valley 实验 (Appendix T) 证明 MMLU +3.3pp 可恢复, 但论文未追踪此线索(如 task-aware allocation); 'distribution-matching objectives sacrifice reasoning pathways' 是描述非机制解释; forward KL mode-covering 动机 (§3.4) 与 reasoning 退化之间的矛盾未讨论。\"}\n    action_items:\n      - {round: 21, action: \"per-layer constraint 实验提供因果证据\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"深入分析 KL mask 在具体哪些层/neuron 上与 MMLU-critical activations 冲突; 基于 Remove Valley 发现讨论 task-aware allocation 可能性; 讨论 forward KL mode-covering 与 reasoning 退化的 trade-off\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无 speedup\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 22\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"首次提出。\"}\n      - {round: 18, reviewers: [1, 2], note: \"Introduction 仍以 efficiency 动机展开。\"}\n      - {round: 19, reviewers: [1, 2], note: \"Table 5 +6.4% overhead, Intro 暗示 efficiency gain。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] R20-N1 Critical。§1 L3 仍有 'potential inference acceleration'。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R21 fresh review 再次标 Critical。Intro framing 已修改为 empirical study, 但 disclaimer 位于括号内过于隐蔽。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[分歧] R2-N1 Critical vs R1-W1 Should-Fix。R1 认为论文已定位为 analysis work 非 system work, predictor masks 可 plug into TEAL kernel pipeline; R2 认为 efficiency-motivated 工作无加速证据是核心缺陷。Director 判定 Warning: 论文自我定位清晰, 但应在主文更显著说明 speedup 路径。\"}\n    action_items:\n      - {round: 21, action: \"Abstract 加 'empirical study' 定位; §1 wall-clock disclaimer 从括号提升到正文句子\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"在 Introduction 或 Conclusion 主文中更显著讨论 speedup gap 及所需条件 (sparse kernel type, hardware constraints)\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分不足: KL+Gumbel+frozen model 配方高度重合\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 22\n    mentions:\n      - {round: 16, reviewers: [2], note: \"R2 首次提出。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R2-N1 Critical + R1 交叉 AGREE。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[分歧] R2-N3 Critical vs R1 REBUT (Minor/Should-Fix)。R1 认为 contextual vs static masks 是 fundamental difference; R2 认为 3 个差异主要是应用场景差异。Director 判定 Warning: §2 已做 3-point differentiation, 但应更诚实定位为 systematic empirical analysis。\"}\n    action_items:\n      - {round: 21, action: \"§2 MaskLLM 段落强化 3 个 activation sparsity vs static N:M 本质差异\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"更明确定位为 'systematic empirical analysis of KL distillation for contextual activation sparsity'; 强化 target-swap ablation 和 per-layer decomposition 的独特分析贡献\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD cross-seed variance 31×\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"WikiText-103→WikiText-2 同分布。C4 30% OOD 仅 2-seed global。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-W2 Major + R2 Q4。C4 CV 6.3% vs 0.2%, seed 42 异常偏高。\"}\n      - {round: 22, reviewers: [], note: \"本轮未显式提出为独立 issue, 但 R2-Q4 涉及 C4 variance 和训练数据充分性。\"}\n    action_items:\n      - {round: 20, action: \"Paper Agent: Limitations 加 WikiText 同分布 + C4 限制\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Limitations 已包含定性讨论。\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Actual sparsity mismatch (KL 28.5% vs TEAL 29.3%) 在主表不够显著\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 22\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"[分歧] R2-W3 Major, R1 REBUT。Director 判定 Info。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R1-W2 + R2 同意。Table 2 ‡ 脚注容易忽略; Table 2 的 raw comparison (8.81 vs 10.82 = 18.6%) 夸大优势, matched 28.5% comparison (14.5%) 仅在 Appendix。建议 Table 2 使用 matched sparsity 结果或更显著标注。\"}\n    action_items:\n      - {round: 21, action: \"Paper Agent: Table 2 加 ‡ 脚注标注 actual sparsity\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"在 Table 2 中增加 TEAL at 28.5% actual sparsity 行, 或在 caption 中更显著标注 matched comparison\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 22 — New issues\n  # ============================================================\n\n  - id: \"R22-W1\"\n    summary: \"KL global 50% 下游仅 s42 单种子, Table 2 标准不一致\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R1-W4 + R2 交叉同意。Table 2 KL global 50% ARC-c (32.85), WG (63.46), GSM8K (1.29) 均无±, 仅 PPL 和 MMLU 有多种子; 同表 KL uniform 50% 全部有 3-seed ±, 标准不一致。\"}\n    action_items:\n      - {round: 22, action: \"补充 KL global 50% 3-seed 下游评测, 或明确标注哪些是单种子结果\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 第5句信息密度过高 (~60词含多层嵌套数字), 一遍难以理解\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R2-W5 + R1 交叉同意。Abstract 第5句包含 '97.5% ... upper bound ... not fully orthogonal ... 10-47% ... K=4-corrected ... commonsense 22-47%, reasoning 10%'。建议简化为 high-level takeaway, 细节移入 Introduction。\"}\n    action_items:\n      - {round: 22, action: \"简化 Abstract 第5句; 将数值细节移入 Introduction\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W3\"\n    summary: \"Conclusion 引用 BoolQ 但 BoolQ 不在 Table 2 主实验中\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R2-W3 + R1 交叉同意。BoolQ 仅在 Appendix K=4 表中出现且 variance 极高 (std=11.5), 不应在 Conclusion 中引用。\"}\n    action_items:\n      - {round: 22, action: \"从 Conclusion 删除 BoolQ, 或将 BoolQ 加入 Table 2\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W3\"\n    summary: \"Figure 2 仅展示 global allocation 但 30% 结论推荐 uniform\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - {round: 21, reviewers: [2], note: \"R2-M4 Minor。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R2-W2 + R1 交叉同意。Figure 2 作为正文仅有的两张 figure 之一, framing 效果很强; TEAL uniform 在 MMLU 上系统性优于 KL uniform, 但 Figure 2 给读者相反印象。\"}\n    action_items:\n      - {round: 21, action: \"Paper Agent: Figure 2 caption 加 uniform 推荐注释\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 22, action: \"在 Figure 2 中加入 uniform allocation 对比曲线, 或在 caption 中明确说明 downstream 结果在 uniform 下不同\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W1\"\n    summary: \"缺少 R-Sparse/CATS 等同类 baseline 的实验对比\"\n    category: experiment\n    severity: minor\n    status: open\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - {round: 21, reviewers: [2], note: \"R2-W5 Minor。R1 partial REBUT: 控制变量混淆。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R2-W1 Warning + R1 partial REBUT。R1 认为 TEAL+BCE 已覆盖核心比较, 其他方法不在同一设计空间; 但同意补充 1-2 个 training-free 方法数字有价值。LaRoSA (2025) 作为 missing reference 也被指出。\"}\n    action_items:\n      - {round: 22, action: \"补充 1-2 个 training-free 方法 (如 CATS 或 R-Sparse) 的数字作为 context, 或解释为什么不适合作为 baseline\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W4\"\n    summary: \"规模泛化仅 7-14B, reasoning 退化可能随规模恶化\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R1-W3 + R2 交叉同意。Qwen-14B GSM8K -20pp 暗示 reasoning 退化可能恶化; 但 R2 补充 dense baseline 差异 (Qwen MMLU 79.77 vs LLaMA 65.27) 使绝对下降不直接可比。\"}\n    action_items:\n      - {round: 22, action: \"Limitations 中明确讨论 'KL-based training may face accuracy-fidelity trade-off on reasoning tasks that could worsen at scale'\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W4\"\n    summary: \"Table 2 注释过长(6行), 信息密度过高\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - {round: 21, reviewers: [2], note: \"R2-M2 Info。信息密度过高。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R2-M1 + R1 交叉同意。5 个 footnote symbols (*, †, ±, ‡, §) 增加认知负担; BCE 30% 使用 TEAL global (†) 而非 uniform 与其他行不一致。\"}\n    action_items:\n      - {round: 22, action: \"Table 2 notes 精简; 确保 allocation 一致性或更显著标注差异\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 22 — Prior issues not raised (possibly resolved)\n  # ============================================================\n\n  - id: \"R19-W4\"\n    summary: \"MSE baseline 50% sparsity seed 123 灾难性失败(PPL=15,789, 5.1% sparsity)\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 21\n    mentions:\n      - {round: 22, reviewers: [], note: \"本轮未提及, 可能已修复(Appendix G 配置充分)。\"}\n    action_items: []\n    resolution: \"Instability 本身是 finding。Appendix G 配置充分。Severity 持续下降。\"\n    resolution_round: 22\n\n  - id: \"R21-W2\"\n    summary: \"符号冲突: g^(ℓ) (gate activation, Eq.1) vs g1/g2 (Gumbel noise, Eq.4)\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - {round: 22, reviewers: [], note: \"本轮未提及, 已修复 (ε1/ε2)。\"}\n    action_items: []\n    resolution: \"method.tex 已修改。\"\n    resolution_round: 22\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot 限制实际影响\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - {round: 22, reviewers: [], note: \"本轮未显式提出, Limitations 已讨论。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W5\"\n    summary: \"§1 Contribution list #1 过长(4行)需拆分\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - {round: 22, reviewers: [], note: \"本轮未显式提出。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W6\"\n    summary: \"BCE+compensation 单独结果未在正文报告\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - {round: 22, reviewers: [], note: \"本轮未显式提出。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Earlier rounds — Resolved (unchanged from R21)\n  # ============================================================\n\n  - id: \"R20-N3\"\n    summary: \"'Coupling alignment' 术语已替换为 'output-distribution alignment'; 97.5% 标注为 upper bound\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    resolution: \"术语替换完成。\"\n    resolution_round: 21\n\n  - id: \"R20-W9\"\n    summary: \"Batched inference 对 contextual sparsity 的影响完全未讨论\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"Limitations 已加 batched inference 讨论。\"\n    resolution_round: 21\n\n  - id: \"R20-W10\"\n    summary: \"Abstract 'universally use BCE' → 'predominantly'\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"已修复。\"\n    resolution_round: 21\n\n  - id: \"R19-F1\"\n    summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"已删除。\"\n    resolution_round: 20\n\n  - id: \"R19-N1\"\n    summary: \"97.5% signal-type 归因缺乏 downstream 定量分解\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    resolution: \"Downstream 2D 分解已落地。\"\n    resolution_round: 20\n\n  - id: \"R19-W5\"\n    summary: \"'hierarchy' → 'ranking' 术语降级\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    resolution: \"已修复。\"\n    resolution_round: 20\n\n  - id: \"R18-W4\"\n    summary: \"Per-layer KL 对照实验缺失\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    resolution: \"Per-layer KL 3-seed 完成。\"\n    resolution_round: 19\n\n  - id: \"R18-W7\"\n    summary: \"Cross-seed Jaccard 未报告\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    resolution: \"Appendix 已补充。\"\n    resolution_round: 19\n\n  - id: \"R16-N1\"\n    summary: \"多种子覆盖不一致\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 19\n    resolution: \"所有关键行均为 3-seed。\"\n    resolution_round: 19\n\n  - id: \"R16-VIS1\"\n    summary: \"正文溢出到第9页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"正文 8 页合规。\"\n    resolution_round: 17\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界不够清晰\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 21\n    resolution: \"§2 MaskLLM 段落已含 3 个本质差异。与 R19-W1 同步。\"\n    resolution_round: 22\n\n  - id: \"R19-W3\"\n    summary: \"Knowledge-intensive 任务退步缺乏机制解释\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 21\n    resolution: \"Constraint 实验提供因果证据。但 R22 重新指出机制解释仍不充分, 已合并进 R20-N2。\"\n    resolution_round: 22"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 22 (fresh review) — Active issues\n  # ============================================================\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap ablation 因果声明过强: 'proximate quality driver' 超出实验证据\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"R19-N2 Critical。循环论证 + soft-vs-hard confound。\"}\n      - {round: 20, reviewers: [1, 2], note: \"R20-W3 Major→Warning。reframe 部分有效。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-W1 Major。3-seed 一致性提供 robustness, 'suggests' hedging 被认可。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R1-N1 Critical + R2-W4 Warning。s42 earlier checkpoint oracle (0.65pp gap) vs s123/s456 matched (≤0.03pp) 不一致; downstream 方向跨 seed 不一致 (s42 MMLU +1.7 vs s456 -0.96); soft-vs-hard confound BCE+Gumbel 控制实验逻辑有瑕疵。建议降级为 transferability claim。\"}\n    action_items:\n      - {round: 19, action: \"Paper Agent: reframe 为 transferability + circularity caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 20, action: \"Paper Agent: 'confirms'→'suggests' 全文替换\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"将 'proximate quality driver' 降级为 'transferable quality patterns'; 删除 'not the training mechanism itself' 排除性声明; 主文明确列出无法完全解耦的原因\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"97.5% signal type decomposition 受 K=1 train-inference mismatch 严重混淆; 精确数字给人虚假精确感\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] downstream 24-35% coupling 可能主要来自 mismatch。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-N2 Critical + R2-W1/W2 Major。97.5% 在 Abstract/Conclusion 无 caveat。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R1-N2 Critical + R2 交叉同意升级 Critical。K=1 mismatch 根本性; K=4 引入 allocation confound (MMLU >100% gap closure); 四个 metric 指向截然不同结论 (ARC-c 2.6% vs PPL 67% vs MMLU >100%); 建议替换为定性描述。\"}\n    action_items:\n      - {round: 20, action: \"Agent: K=4 per-layer KL pilot 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 21, action: \"Abstract/Conclusion 97.5% 加 caveat + K=4 multi-seed\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"将 '97.5%' 替换为定性描述: 'signal type accounts for the majority of the PPL gap'; 在主文而非 footnote 讨论 orthogonality limitation; 补充 K=4 at 50% 实验(如可行)\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨三个架构系统性退步, 机制解释不充分\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 22\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W8。14B 仅 30% sparsity。\"}\n      - {round: 19, reviewers: [1, 2], note: \"R19-W2/W3。GSM8K -20pp σ=5.2pp。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 升级为 Critical。跨三架构一致。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-N3 Major + R2-W4。Protection valley 分析仅 correlational, 缺 interventional 验证。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R2-N2 Critical + R1 borderline Must-Fix。Remove Valley 实验 (Appendix T) 证明 MMLU +3.3pp 可恢复, 但论文未追踪此线索(如 task-aware allocation); 'distribution-matching objectives sacrifice reasoning pathways' 是描述非机制解释; forward KL mode-covering 动机 (§3.4) 与 reasoning 退化之间的矛盾未讨论。\"}\n    action_items:\n      - {round: 21, action: \"per-layer constraint 实验提供因果证据\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"深入分析 KL mask 在具体哪些层/neuron 上与 MMLU-critical activations 冲突; 基于 Remove Valley 发现讨论 task-aware allocation 可能性; 讨论 forward KL mode-covering 与 reasoning 退化的 trade-off\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无 speedup\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 22\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"首次提出。\"}\n      - {round: 18, reviewers: [1, 2], note: \"Introduction 仍以 efficiency 动机展开。\"}\n      - {round: 19, reviewers: [1, 2], note: \"Table 5 +6.4% overhead, Intro 暗示 efficiency gain。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] R20-N1 Critical。§1 L3 仍有 'potential inference acceleration'。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R21 fresh review 再次标 Critical。Intro framing 已修改为 empirical study, 但 disclaimer 位于括号内过于隐蔽。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[分歧] R2-N1 Critical vs R1-W1 Should-Fix。R1 认为论文已定位为 analysis work 非 system work, predictor masks 可 plug into TEAL kernel pipeline; R2 认为 efficiency-motivated 工作无加速证据是核心缺陷。Director 判定 Warning: 论文自我定位清晰, 但应在主文更显著说明 speedup 路径。\"}\n    action_items:\n      - {round: 21, action: \"Abstract 加 'empirical study' 定位; §1 wall-clock disclaimer 从括号提升到正文句子\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"在 Introduction 或 Conclusion 主文中更显著讨论 speedup gap 及所需条件 (sparse kernel type, hardware constraints)\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分不足: KL+Gumbel+frozen model 配方高度重合\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 22\n    mentions:\n      - {round: 16, reviewers: [2], note: \"R2 首次提出。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R2-N1 Critical + R1 交叉 AGREE。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[分歧] R2-N3 Critical vs R1 REBUT (Minor/Should-Fix)。R1 认为 contextual vs static masks 是 fundamental difference; R2 认为 3 个差异主要是应用场景差异。Director 判定 Warning: §2 已做 3-point differentiation, 但应更诚实定位为 systematic empirical analysis。\"}\n    action_items:\n      - {round: 21, action: \"§2 MaskLLM 段落强化 3 个 activation sparsity vs static N:M 本质差异\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"更明确定位为 'systematic empirical analysis of KL distillation for contextual activation sparsity'; 强化 target-swap ablation 和 per-layer decomposition 的独特分析贡献\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD cross-seed variance 31×\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"WikiText-103→WikiText-2 同分布。C4 30% OOD 仅 2-seed global。\"}\n      - {round: 21, reviewers: [1, 2], note: \"[AGREE] R1-W2 Major + R2 Q4。C4 CV 6.3% vs 0.2%, seed 42 异常偏高。\"}\n      - {round: 22, reviewers: [], note: \"本轮未显式提出为独立 issue, 但 R2-Q4 涉及 C4 variance 和训练数据充分性。\"}\n    action_items:\n      - {round: 20, action: \"Paper Agent: Limitations 加 WikiText 同分布 + C4 限制\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Limitations 已包含定性讨论。\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Actual sparsity mismatch (KL 28.5% vs TEAL 29.3%) 在主表不够显著\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 22\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"[分歧] R2-W3 Major, R1 REBUT。Director 判定 Info。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R1-W2 + R2 同意。Table 2 ‡ 脚注容易忽略; Table 2 的 raw comparison (8.81 vs 10.82 = 18.6%) 夸大优势, matched 28.5% comparison (14.5%) 仅在 Appendix。建议 Table 2 使用 matched sparsity 结果或更显著标注。\"}\n    action_items:\n      - {round: 21, action: \"Paper Agent: Table 2 加 ‡ 脚注标注 actual sparsity\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"在 Table 2 中增加 TEAL at 28.5% actual sparsity 行, 或在 caption 中更显著标注 matched comparison\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 22 — New issues\n  # ============================================================\n\n  - id: \"R22-W1\"\n    summary: \"KL global 50% 下游仅 s42 单种子, Table 2 标准不一致\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R1-W4 + R2 交叉同意。Table 2 KL global 50% ARC-c (32.85), WG (63.46), GSM8K (1.29) 均无±, 仅 PPL 和 MMLU 有多种子; 同表 KL uniform 50% 全部有 3-seed ±, 标准不一致。\"}\n    action_items:\n      - {round: 22, action: \"补充 KL global 50% 3-seed 下游评测, 或明确标注哪些是单种子结果\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 第5句信息密度过高 (~60词含多层嵌套数字), 一遍难以理解\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R2-W5 + R1 交叉同意。Abstract 第5句包含 '97.5% ... upper bound ... not fully orthogonal ... 10-47% ... K=4-corrected ... commonsense 22-47%, reasoning 10%'。建议简化为 high-level takeaway, 细节移入 Introduction。\"}\n    action_items:\n      - {round: 22, action: \"简化 Abstract 第5句; 将数值细节移入 Introduction\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W3\"\n    summary: \"Conclusion 引用 BoolQ 但 BoolQ 不在 Table 2 主实验中\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R2-W3 + R1 交叉同意。BoolQ 仅在 Appendix K=4 表中出现且 variance 极高 (std=11.5), 不应在 Conclusion 中引用。\"}\n    action_items:\n      - {round: 22, action: \"从 Conclusion 删除 BoolQ, 或将 BoolQ 加入 Table 2\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W3\"\n    summary: \"Figure 2 仅展示 global allocation 但 30% 结论推荐 uniform\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - {round: 21, reviewers: [2], note: \"R2-M4 Minor。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R2-W2 + R1 交叉同意。Figure 2 作为正文仅有的两张 figure 之一, framing 效果很强; TEAL uniform 在 MMLU 上系统性优于 KL uniform, 但 Figure 2 给读者相反印象。\"}\n    action_items:\n      - {round: 21, action: \"Paper Agent: Figure 2 caption 加 uniform 推荐注释\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 22, action: \"在 Figure 2 中加入 uniform allocation 对比曲线, 或在 caption 中明确说明 downstream 结果在 uniform 下不同\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W1\"\n    summary: \"缺少 R-Sparse/CATS 等同类 baseline 的实验对比\"\n    category: experiment\n    severity: minor\n    status: open\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - {round: 21, reviewers: [2], note: \"R2-W5 Minor。R1 partial REBUT: 控制变量混淆。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R2-W1 Warning + R1 partial REBUT。R1 认为 TEAL+BCE 已覆盖核心比较, 其他方法不在同一设计空间; 但同意补充 1-2 个 training-free 方法数字有价值。LaRoSA (2025) 作为 missing reference 也被指出。\"}\n    action_items:\n      - {round: 22, action: \"补充 1-2 个 training-free 方法 (如 CATS 或 R-Sparse) 的数字作为 context, 或解释为什么不适合作为 baseline\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W4\"\n    summary: \"规模泛化仅 7-14B, reasoning 退化可能随规模恶化\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R1-W3 + R2 交叉同意。Qwen-14B GSM8K -20pp 暗示 reasoning 退化可能恶化; 但 R2 补充 dense baseline 差异 (Qwen MMLU 79.77 vs LLaMA 65.27) 使绝对下降不直接可比。\"}\n    action_items:\n      - {round: 22, action: \"Limitations 中明确讨论 'KL-based training may face accuracy-fidelity trade-off on reasoning tasks that could worsen at scale'\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W4\"\n    summary: \"Table 2 注释过长(6行), 信息密度过高\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - {round: 21, reviewers: [2], note: \"R2-M2 Info。信息密度过高。\"}\n      - {round: 22, reviewers: [1, 2], note: \"[AGREE] R2-M1 + R1 交叉同意。5 个 footnote symbols (*, †, ±, ‡, §) 增加认知负担; BCE 30% 使用 TEAL global (†) 而非 uniform 与其他行不一致。\"}\n    action_items:\n      - {round: 22, action: \"Table 2 notes 精简; 确保 allocation 一致性或更显著标注差异\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 22 — Prior issues not raised (possibly resolved)\n  # ============================================================\n\n  - id: \"R19-W4\"\n    summary: \"MSE baseline 50% sparsity seed 123 灾难性失败(PPL=15,789, 5.1% sparsity)\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 21\n    mentions:\n      - {round: 22, reviewers: [], note: \"本轮未提及, 可能已修复(Appendix G 配置充分)。\"}\n    action_items: []\n    resolution: \"Instability 本身是 finding。Appendix G 配置充分。Severity 持续下降。\"\n    resolution_round: 22\n\n  - id: \"R21-W2\"\n    summary: \"符号冲突: g^(ℓ) (gate activation, Eq.1) vs g1/g2 (Gumbel noise, Eq.4)\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - {round: 22, reviewers: [], note: \"本轮未提及, 已修复 (ε1/ε2)。\"}\n    action_items: []\n    resolution: \"method.tex 已修改。\"\n    resolution_round: 22\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot 限制实际影响\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - {round: 22, reviewers: [], note: \"本轮未显式提出, Limitations 已讨论。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W5\"\n    summary: \"§1 Contribution list #1 过长(4行)需拆分\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - {round: 22, reviewers: [], note: \"本轮未显式提出。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W6\"\n    summary: \"BCE+compensation 单独结果未在正文报告\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - {round: 22, reviewers: [], note: \"本轮未显式提出。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Earlier rounds — Resolved (unchanged from R21)\n  # ============================================================\n\n  - id: \"R20-N3\"\n    summary: \"'Coupling alignment' 术语已替换为 'output-distribution alignment'; 97.5% 标注为 upper bound\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    resolution: \"术语替换完成。\"\n    resolution_round: 21\n\n  - id: \"R20-W9\"\n    summary: \"Batched inference 对 contextual sparsity 的影响完全未讨论\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"Limitations 已加 batched inference 讨论。\"\n    resolution_round: 21\n\n  - id: \"R20-W10\"\n    summary: \"Abstract 'universally use BCE' → 'predominantly'\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"已修复。\"\n    resolution_round: 21\n\n  - id: \"R19-F1\"\n    summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"已删除。\"\n    resolution_round: 20\n\n  - id: \"R19-N1\"\n    summary: \"97.5% signal-type 归因缺乏 downstream 定量分解\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    resolution: \"Downstream 2D 分解已落地。\"\n    resolution_round: 20\n\n  - id: \"R19-W5\"\n    summary: \"'hierarchy' → 'ranking' 术语降级\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    resolution: \"已修复。\"\n    resolution_round: 20\n\n  - id: \"R18-W4\"\n    summary: \"Per-layer KL 对照实验缺失\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    resolution: \"Per-layer KL 3-seed 完成。\"\n    resolution_round: 19\n\n  - id: \"R18-W7\"\n    summary: \"Cross-seed Jaccard 未报告\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    resolution: \"Appendix 已补充。\"\n    resolution_round: 19\n\n  - id: \"R16-N1\"\n    summary: \"多种子覆盖不一致\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 19\n    resolution: \"所有关键行均为 3-seed。\"\n    resolution_round: 19\n\n  - id: \"R16-VIS1\"\n    summary: \"正文溢出到第9页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"正文 8 页合规。\"\n    resolution_round: 17\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界不够清晰\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 21\n    resolution: \"§2 MaskLLM 段落已含 3 个本质差异。与 R19-W1 同步。\"\n    resolution_round: 22\n\n  - id: \"R19-W3\"\n    summary: \"Knowledge-intensive 任务退步缺乏机制解释\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 21\n    resolution: \"Constraint 实验提供因果证据。但 R22 重新指出机制解释仍不充分, 已合并进 R20-N2。\"\n    resolution_round: 22"
  }
}
```

</details>

---


### Tool result

_source line 1833 · 2026-05-22T17:28:04.496396+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 17705}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 1834 · 2026-05-22T17:30:58.445011+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 22 (Fresh Review)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+写作完整性）\n**圆桌轮次**: 1 轮初审 + 1 轮交叉分享（达成收敛）\n\n---\n\n## Summary\n\n本文提出用 forward KL 蒸馏训练 SwiGLU LLM 的上下文稀疏性预测器，替代传统 BCE 训练。在 LLaMA-3.1-8B 上，KL 预测器在 30% 稀疏度下将 TEAL 的困惑度降低 14.5%（matched sparsity），在 50% 下降低 50%。论文进行了系统性分析：target-swap ablation (C1) 探索 mask pattern 的可迁移性，per-layer KL 分解（K=1/K=4 控制实验）尝试解耦 signal type 和 coupling scope 的贡献，跨三个架构（LLaMA-8B, Mistral-7B, Qwen-14B）验证泛化性。论文自我定位为实证研究（\"primarily an empirical study\"），不涉及 wall-clock 加速。\n\n---\n\n## Strengths\n\n**S1 [共识]** 实验设计严谨且覆盖面广：5 种 loss function 对比（KL, reverse KL, JSD, BCE, MSE）、3-seed 评估、3 个架构、6+ 下游任务、C1 target-swap、K=1/K=4 分解、SNR 分析、bottleneck/temperature/training steps sensitivity。总实验量远超一般 EMNLP 投稿（registry 显示 374 个实验）。\n\n**S2 [共识]** Target-swap ablation (C1) 是一个巧妙的分析方法，能够部分解耦 mask quality 和 training mechanism 的贡献。尽管因果声明存在过强问题（见 Weakness N1），实验设计本身具有方法论参考价值。\n\n**S3 [共识]** Per-layer KL 分解（K=1 和 K=4 控制实验）对 signal type vs coupling scope 的定量分解是该领域的新颖分析维度，即使精确数字不可靠（见 N2），分析框架本身有贡献。\n\n**S4 [共识]** 诚实的自我定位：论文明确声明 \"primarily an empirical study\"，详细讨论了 confounds、upper bounds、和 limitations。这种学术诚实在该领域并不常见。\n\n**S5 [共识]** 可复现性好：所有超参数完整报告，exp_id 标注在 LaTeX 注释中，训练仅需 ~45 min 单卡，19 页 Appendix 提供充分补充材料。\n\n**S6 [R1]** 梯度分析 (§3.6) 虽基于标准 chain rule，但在稀疏性预测场景下的应用新颖：BCE 梯度仅依赖 neuron j，KL 梯度通过下游 Jacobian 耦合所有层。配合 SNR 分析（KL 信号更噪但 mask 更好）构成 \"search mechanism > gradient clarity\" 的有趣叙事。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [共识 Critical]** C1 Target-Swap Ablation 的因果声明过强\n\n论文在 Abstract 和 §4.4 中声称 \"the discovered patterns—not the training mechanism itself—as the proximate quality driver\"。两位 Reviewer 一致认为此 claim 超出实验证据：\n\n- **循环性**：KL-derived masks 本身是 KL coupling 的产物。C1 仅证明 mask patterns 的可迁移性（BCE trained on KL targets approaches KL-level PPL），而非 mask patterns 是 \"唯一\" 质量驱动因素。\n- **s42 不一致**：s42 使用 earlier checkpoint oracle (PPL gap 0.65pp)，而 s123/s456 使用 matched retrained oracle (gap ≤0.03pp)。Table 3 footnote † 容易忽略。\n- **下游方向不一致**：s42 C1 在 MMLU +1.7pp 优于 KL，但 s456 C1 在 MMLU −0.96pp 劣于 KL。如果 mask pattern 是唯一驱动因素，方向应一致。\n- **Soft-vs-hard confound**：BCE+Gumbel (32.22) vs standard BCE (27.97) 的控制实验不干净——Gumbel 在 BCE 设置下有害，无法作为 \"softness 不是主因\" 的中性控制。\n\n**建议**: 将 claim 降级为 \"KL-discovered masks are transferable: BCE trained on KL-derived targets approaches KL-level PPL, suggesting mask patterns carry substantial quality information\"。删除 \"not the training mechanism itself\" 的排除性声明。\n\n**N2 [共识 Critical]** 97.5% Signal Type Decomposition 受严重混淆变量影响\n\n97.5% 出现在 Abstract（第5句）、Introduction（contribution #1）、Conclusion（第1句）的核心位置，但实验证据不支持这一精确数字：\n\n- **K=1 train-inference mismatch**：训练时仅 mask 1/32 层，推理时 mask 全部 32 层。论文在 Footnote 5 承认 \"not fully orthogonal\"，但 caveat 的显著性远不及 97.5% 的反复出现。\n- **K=4 引入新 confound**：K=4 的 near-uniform per-layer sparsity (std=0.003) 恰好匹配 uniform eval allocation，导致 MMLU >100% gap closure——这是 allocation alignment artifact，非 coupling 效应。\n- **Metric 分歧**：ARC-c gap closure 2.6%（coupling-dominated）vs PPL 66.7%（mismatch-dominated）vs MMLU >100%（anomalous）。四个 metric 指向截然不同结论，无法支撑单一叙事。\n- **50% 缺 K=4**：50% 仅有 K=1 结果（per-layer KL 34.85 vs E2E 11.92, +192%），恰恰是 coupling 贡献最大的区间却缺少 mismatch 控制。\n\n**建议**: 将 \"97.5%\" 替换为定性描述 \"signal type accounts for the majority of the PPL gap (upper bound; confounded by train-inference mismatch)\"。在主文而非 footnote 中讨论 orthogonality limitation。如可行，补充 K=4 at 50% 的 3-seed 实验。\n\n**N3 [R2 Critical, R1 borderline Must-Fix]** MMLU/GSM8K 跨架构系统性退化\n\nKL predictor 在所有测试规模上系统性逊于 TEAL：\n- LLaMA-8B 30%: MMLU −5.2pp (40.7 vs 45.86), GSM8K −1.3pp\n- Qwen-14B 30%: GSM8K −20pp, MMLU −8pp (uniform)\n- Mistral-7B 30%: GSM8K 8.6 vs 15.9 (TEAL wins)\n\n论文的 \"distribution-matching objectives sacrifice reasoning pathways\" 是描述非解释。更关键的是，Appendix T (Remove Valley) 实验显示 MMLU +3.3pp 可恢复——这表明退化部分源于可纠正的 allocation 问题，但论文未追踪此线索（如 task-aware allocation）。Forward KL 的 mode-covering 动机（§3.4: \"false negatives cascade\"）与 reasoning 退化之间的矛盾未讨论。\n\n**建议**: 深入分析 KL mask 在哪些层与 reasoning-critical activations 冲突；基于 Remove Valley 发现讨论 task-aware allocation 可能性；讨论 mode-covering 与 reasoning 退化的 trade-off。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [分歧 → Director 判定 Warning]** 无实际推理加速\n\nR2 将此列为 Critical，R1 列为 Should-Fix。论文在 Introduction 已明确定位为 empirical study 且声明不涉及 latency optimization。R1 正确指出 predictor 产生的 mask 可 plug into TEAL 的 kernel pipeline。**但**论文的 opening motivation 仍以 inference allocation 为核心，且 Table 5 显示 +6.4% 延迟。Director 判定：Should-Fix。论文应在主文中更显著说明 speedup 所需条件。\n\n**W2 [分歧 → Director 判定 Warning]** 与 MaskLLM 区分度\n\nR2 列为 Critical，R1 REBUT（contextual vs static masks 是 fundamental difference）。R1 的论证有力——per-token generalization、cross-layer allocation、OOD robustness 确实是本质差异而非应用场景差异。但核心 recipe（frozen model + KL + Gumbel masks）的重合不可否认。Director 判定：Warning。§2 已做 3-point differentiation，但论文应更明确定位为 systematic empirical analysis 而非暗示方法论创新。\n\n**W3 [共识]** Table 2 actual sparsity mismatch (KL 28.5% vs TEAL 29.3%)\n\nTable 2 的 ‡ 脚注容易忽略。Raw comparison (8.81 vs 10.82 = 18.6% improvement) 夸大优势，matched 28.5% comparison (14.5%) 仅在 Appendix。建议 Table 2 增加 TEAL at 28.5% 行或更显著标注。\n\n**W4 [共识]** KL global 50% 下游仅 s42 单种子\n\nTable 2 中 KL global 50% 的 ARC-c (32.85)、WG (63.46)、GSM8K (1.29) 无 ± 标注，与同表 KL uniform 50%（全部 3-seed）标准不一致。\n\n**W5 [共识]** 规模泛化仅 7–14B\n\nQwen-14B 的 GSM8K −20pp 暗示 reasoning 退化可能随规模恶化。如无法补充更大规模实验，应在 Limitations 中明确讨论 scale trade-off。\n\n**W6 [共识]** Figure 2 仅展示 global allocation 但 §4.2 推荐 uniform\n\n作为正文仅有的两张 figure 之一，Figure 2 的 framing 效果很强，但 uniform allocation 下 TEAL 在 MMLU 上系统性优于 KL。建议加入 uniform 曲线或在 caption 中明确说明。\n\n**W7 [共识]** Abstract 第5句信息密度过高\n\n约 60 词包含多层嵌套数字和条件，首次阅读几乎不可能理解。建议简化为 high-level takeaway。\n\n**W8 [共识]** Conclusion 引用 BoolQ 但不在 Table 2\n\nBoolQ 仅在 Appendix K=4 表中出现且 variance 极高 (std=11.5)，不应在 Conclusion 中引用。\n\n---\n\n### Minor（不影响接收）\n\n- **M1**: Table 2 注释过多（†, ‡, *, ±, §），BCE 30% 使用 TEAL global 与其他行不一致\n- **M2**: §3.5 deadzone margin ε=0.02 缺乏 justification\n- **M3**: §4.3 BCE 2700 steps 与 KL 1000 steps wall-clock 接近 (~46 vs ~45 min) 需解释（BCE 无 dense forward pass）\n- **M4**: \"Adaptive Penalty Controller\" 命名不准确——实际是 geometric doubling + deadzone，非经典 dual ascent\n- **M5**: References 中 FastForward (arXiv:2602.00397) 如已被会议接收应更新\n- **M6**: Limitations 未讨论 sequence length 对 predictor mask 质量的影响\n- **M7**: Table 1 (Taxonomy) 中 SPON 归入 \"Static × Coupled\" 的合理性应在正文讨论\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成 **[AGREE]**：\n\n1. **C1 因果声明过强** — 应降级为 transferability claim（R1-N1 + R2-W4）\n2. **97.5% decomposition 不可靠** — 应替换为定性描述（R1-N2 + R2 交叉同意升级 Critical）\n3. **MMLU/GSM8K 退化需更深分析** — Remove Valley 线索未追踪（R2-N2 + R1 borderline Must-Fix）\n4. **Table 2 sparsity mismatch 不够显著** — 需更显著标注（R1-W2 + R2 AGREE）\n5. **KL global 50% 下游缺 3-seed** — 标准不一致（R1-W4 + R2 AGREE）\n6. **Figure 2 global/uniform 误导** — 需补充 uniform 曲线（R2-W2 + R1 AGREE）\n7. **Abstract/Conclusion 写作问题** — 密度过高 + BoolQ 不当引用（R2-W3/W5 + R1 AGREE）\n8. **研究问题有价值** — 训练目标如何影响 mask quality 是 under-explored 但重要的问题\n9. **实验覆盖面远超同类工作** — 消融设计用心，可复现性好\n\n---\n\n## Reviewer Divergence\n\n**分歧 1: Wall-clock speedup 的严重程度**\n- **R2**: Critical (N1) — 作为 efficiency-motivated 工作，+6.4% 延迟且无加速证据是核心缺陷\n- **R1**: Should-Fix (W1, REBUT) — 论文已定位为 analysis work；predictor masks 可 plug into TEAL kernel pipeline；如果将此升级为 Must-Fix，大量分析性论文都会因 \"无端到端系统集成\" 被拒\n- **Director 判定**: **Warning** — R1 论证有力，论文的自我定位清晰且合理，但应在主文更显著说明 speedup 路径\n\n**分歧 2: MaskLLM 区分度**\n- **R2**: Critical (N3) — 核心 recipe 完全共享，3 个差异是应用场景差异非方法论创新\n- **R1**: REBUT (Minor/Should-Fix) — contextual vs static masks 是 fundamental architectural difference；cross-layer allocation 是本文独有的；recipe 层面的共享不等于方法论重叠（类似 knowledge distillation 的标准 recipe）\n- **Director 判定**: **Warning** — R1 的 REBUT 有效，contextual vs static 确实是本质差异；但论文应更诚实定位为 systematic empirical analysis\n\n**分歧 3: K=4 at 50% 缺失的严重程度**\n- **R1**: Should-Fix (W5) — 50% 是 coupling 贡献最大的区间，缺少 K=4 无法判断真实贡献\n- **R2**: REBUT (不应为 Should-Fix) — 50% 是 capacity-limited regime，所有方法 downstream 接近 random，K=4 decomposition 在 noise floor 附近意义不大\n- **Director 判定**: 保留为 **Warning**。R2 的 rebut 有道理但论文应解释原因\n\n---\n\n## Questions\n\n1. **[R1-Q1]** \"Reverse C1\"——在 magnitude-based masks 上训练 KL（而非 BCE）结果如何？如果 KL coupling 在 magnitude targets 上也效果好，则弱化 \"mask patterns are the driver\" 声明。\n2. **[R1-Q2]** 为何 50% 没做 K=4？是资源限制还是训练不稳定？\n3. **[R1-Q3 / R2-Q1]** Remove Valley 可恢复 MMLU +3.3pp，为何不探索 task-aware allocation？这是低悬果实。\n4. **[R2-Q3]** \"14.5% PPL reduction\" 基于 matched 28.5% sparsity——Table 2 呈现方式是否会让读者误读为 18.6%？\n5. **[R2-Q5]** §3.6 声称 gradient coupling 发现 68% divergent masks，但 C1 说 mask patterns（而非 coupling）是 driver——两者关系需更清晰阐述。如果 coupling 主要用于 discover masks，是否可以 KL 训练后提取 masks 再用 BCE 部署？\n6. **[R1-Q4]** 30% target λ 达 cap (5000) 但实际仅 28.5%（5% deviation）。提高 λ_max 能否逼近 30%？\n\n---\n\n## Missing References\n\n1. **LaRoSA** (2025, arXiv:2507.01299) — Layerwise Rotated Sparse Activation，在 SwiGLU 模型上实现 wall-clock speedup，高度相关但未引用\n2. **Geva et al. (2023)** \"Dissecting Recall of Factual Associations\" — 已在 bib 中但正文未引用，与 MMLU regression 讨论相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 已跳过（用户在审稿群中跳过了外部审稿请求）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 完成但 Agent 报错（rate limit: \"You've hit your limit · resets 6pm (UTC)\"），无有效视觉审查发现。用户可在 rate limit 重置后重新触发。\n\n格式合规检查由 R2 手动完成：\n| 项目 | 状态 |\n|------|------|\n| 正文页数 | ✅ §1-§5 在第8页结束 |\n| Limitations | ✅ p9，不计入页数，3个关键点 |\n| Ethics | ✅ p9，简短适当 |\n| 匿名化 | ✅ \"Anonymous ACL submission\" |\n| Appendix 双栏 | ✅ ACL 格式 |\n| 引用格式 | ✅ acl_natbib |\n\n---\n\n## Overall Assessment\n\n**评分**: 3.0 (Findings)\n**置信度**: 4/5\n\n**R1**: 3.5 (Borderline Conference) — Soundness 3.5, Excitement 3.0\n**R2**: 3.0 (Findings) — Soundness 3.5, Excitement 2.5\n**Director 综合**: 3.0 (Findings)\n\n**理由**: 论文的核心发现（KL distillation 优于 BCE 训练稀疏性预测器）可信且有实验支撑，实验设计的系统性和覆盖面是明显优势。但两个核心分析贡献（C1 target-swap ablation 和 97.5% signal-type decomposition）的 claim 强度超出实验证据——这两个声明出现在 Abstract、Introduction contributions list、和 Conclusion 的核心位置，是论文三大贡献中的两个。加之 MMLU/GSM8K 在所有测试规模上系统性逊于 training-free baseline TEAL，且缺乏 wall-clock speedup，整体贡献更适合 Findings 而非主会议。\n\n**升级路径**: 如果 (1) N1/N2 的 claim 调整为更审慎的措辞，(2) 基于 Remove Valley 发现追踪 task-aware allocation，(3) 补充 K=4 at 50% 实验，论文有望升至 3.5 (Borderline Conference)。如进一步补充 wall-clock speedup 数据（即使仅一个 sparsity level），可达 4.0 (Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution list 第1条过长（4行），建议拆分为 per-layer decomposition 和 cross-scale evidence\n- \"14.5% over TEAL at matched sparsity\" 的 \"matched sparsity\" 在此处首次出现但未解释，建议明确 (KL 28.5% vs TEAL 28.5%)\n\n### §3 Method\n- §3.5 Adaptive Penalty Controller: ε=0.02 的选择缺乏 justification；\"adaptive\" 命名可能误导——实际是 geometric doubling + deadzone\n- §3.6 Gradient Analysis: 与 §4.4 C1 的关系需要更清晰阐述——§3.6 argue coupling 是优势来源，§4.4 argue mask patterns（而非 coupling）是 driver。当前叙事的矛盾是：coupling 的作用仅在于 training-time discovery 还是 inference-time maintenance？\n- §3.7 Taxonomy: Table 1 有用但本身不构成 intellectual contribution；SPON 的 \"Static × Coupled\" 分类应在正文简要讨论\n\n### §4 Experiments\n- Table 2: 注释过多（5 种 footnote symbols）；BCE 30% 使用 TEAL global (†) 与其他行不一致且容易被忽略\n- §4.3 Extended Training: BCE 2700 steps wall-clock 与 KL 1000 steps 接近 (~46 vs ~45 min) 需解释——BCE 不需要 dense forward pass，每步应更快\n- §4.4 C1 Ablation: \"suggests\" hedging 是好的，但 Abstract 中的 \"as the proximate quality driver\" 措辞过于绝对\n- §4.5 Per-Layer KL: \"97.5%\" 的精确数字与 Footnote 5 的 \"not fully orthogonal\" caveat 之间的显著性严重不对称；K=4 MMLU anomaly (>100% gap closure) 应在正文而非 Appendix 讨论\n\n### §5 Conclusion\n- 仅 2 句话 (~130 词)，信息密度过高\n- 引用了 BoolQ (仅 Appendix, high variance) 但未引用 HellaSwag/PIQA (Table 11, stable)\n- 完全没有提及 limitations (MMLU regression, no speedup, scale bounds)\n\n### Appendix\n- 19 页 Appendix 提供了充分补充，信息分配总体合理\n- Appendix T (Constraint Analysis) 的发现（Remove Valley: MMLU +3.3pp）应在正文获得更多讨论，而非仅作为 supporting evidence",
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 22 (Fresh Review)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+写作完整性）\n**圆桌轮次**: 1 轮初审 + 1 轮交叉分享（达成收敛）\n\n---\n\n## Summary\n\n本文提出用 forward KL 蒸馏训练 SwiGLU LLM 的上下文稀疏性预测器，替代传统 BCE 训练。在 LLaMA-3.1-8B 上，KL 预测器在 30% 稀疏度下将 TEAL 的困惑度降低 14.5%（matched sparsity），在 50% 下降低 50%。论文进行了系统性分析：target-swap ablation (C1) 探索 mask pattern 的可迁移性，per-layer KL 分解（K=1/K=4 控制实验）尝试解耦 signal type 和 coupling scope 的贡献，跨三个架构（LLaMA-8B, Mistral-7B, Qwen-14B）验证泛化性。论文自我定位为实证研究（\"primarily an empirical study\"），不涉及 wall-clock 加速。\n\n---\n\n## Strengths\n\n**S1 [共识]** 实验设计严谨且覆盖面广：5 种 loss function 对比（KL, reverse KL, JSD, BCE, MSE）、3-seed 评估、3 个架构、6+ 下游任务、C1 target-swap、K=1/K=4 分解、SNR 分析、bottleneck/temperature/training steps sensitivity。总实验量远超一般 EMNLP 投稿（registry 显示 374 个实验）。\n\n**S2 [共识]** Target-swap ablation (C1) 是一个巧妙的分析方法，能够部分解耦 mask quality 和 training mechanism 的贡献。尽管因果声明存在过强问题（见 Weakness N1），实验设计本身具有方法论参考价值。\n\n**S3 [共识]** Per-layer KL 分解（K=1 和 K=4 控制实验）对 signal type vs coupling scope 的定量分解是该领域的新颖分析维度，即使精确数字不可靠（见 N2），分析框架本身有贡献。\n\n**S4 [共识]** 诚实的自我定位：论文明确声明 \"primarily an empirical study\"，详细讨论了 confounds、upper bounds、和 limitations。这种学术诚实在该领域并不常见。\n\n**S5 [共识]** 可复现性好：所有超参数完整报告，exp_id 标注在 LaTeX 注释中，训练仅需 ~45 min 单卡，19 页 Appendix 提供充分补充材料。\n\n**S6 [R1]** 梯度分析 (§3.6) 虽基于标准 chain rule，但在稀疏性预测场景下的应用新颖：BCE 梯度仅依赖 neuron j，KL 梯度通过下游 Jacobian 耦合所有层。配合 SNR 分析（KL 信号更噪但 mask 更好）构成 \"search mechanism > gradient clarity\" 的有趣叙事。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [共识 Critical]** C1 Target-Swap Ablation 的因果声明过强\n\n论文在 Abstract 和 §4.4 中声称 \"the discovered patterns—not the training mechanism itself—as the proximate quality driver\"。两位 Reviewer 一致认为此 claim 超出实验证据：\n\n- **循环性**：KL-derived masks 本身是 KL coupling 的产物。C1 仅证明 mask patterns 的可迁移性（BCE trained on KL targets approaches KL-level PPL），而非 mask patterns 是 \"唯一\" 质量驱动因素。\n- **s42 不一致**：s42 使用 earlier checkpoint oracle (PPL gap 0.65pp)，而 s123/s456 使用 matched retrained oracle (gap ≤0.03pp)。Table 3 footnote † 容易忽略。\n- **下游方向不一致**：s42 C1 在 MMLU +1.7pp 优于 KL，但 s456 C1 在 MMLU −0.96pp 劣于 KL。如果 mask pattern 是唯一驱动因素，方向应一致。\n- **Soft-vs-hard confound**：BCE+Gumbel (32.22) vs standard BCE (27.97) 的控制实验不干净——Gumbel 在 BCE 设置下有害，无法作为 \"softness 不是主因\" 的中性控制。\n\n**建议**: 将 claim 降级为 \"KL-discovered masks are transferable: BCE trained on KL-derived targets approaches KL-level PPL, suggesting mask patterns carry substantial quality information\"。删除 \"not the training mechanism itself\" 的排除性声明。\n\n**N2 [共识 Critical]** 97.5% Signal Type Decomposition 受严重混淆变量影响\n\n97.5% 出现在 Abstract（第5句）、Introduction（contribution #1）、Conclusion（第1句）的核心位置，但实验证据不支持这一精确数字：\n\n- **K=1 train-inference mismatch**：训练时仅 mask 1/32 层，推理时 mask 全部 32 层。论文在 Footnote 5 承认 \"not fully orthogonal\"，但 caveat 的显著性远不及 97.5% 的反复出现。\n- **K=4 引入新 confound**：K=4 的 near-uniform per-layer sparsity (std=0.003) 恰好匹配 uniform eval allocation，导致 MMLU >100% gap closure——这是 allocation alignment artifact，非 coupling 效应。\n- **Metric 分歧**：ARC-c gap closure 2.6%（coupling-dominated）vs PPL 66.7%（mismatch-dominated）vs MMLU >100%（anomalous）。四个 metric 指向截然不同结论，无法支撑单一叙事。\n- **50% 缺 K=4**：50% 仅有 K=1 结果（per-layer KL 34.85 vs E2E 11.92, +192%），恰恰是 coupling 贡献最大的区间却缺少 mismatch 控制。\n\n**建议**: 将 \"97.5%\" 替换为定性描述 \"signal type accounts for the majority of the PPL gap (upper bound; confounded by train-inference mismatch)\"。在主文而非 footnote 中讨论 orthogonality limitation。如可行，补充 K=4 at 50% 的 3-seed 实验。\n\n**N3 [R2 Critical, R1 borderline Must-Fix]** MMLU/GSM8K 跨架构系统性退化\n\nKL predictor 在所有测试规模上系统性逊于 TEAL：\n- LLaMA-8B 30%: MMLU −5.2pp (40.7 vs 45.86), GSM8K −1.3pp\n- Qwen-14B 30%: GSM8K −20pp, MMLU −8pp (uniform)\n- Mistral-7B 30%: GSM8K 8.6 vs 15.9 (TEAL wins)\n\n论文的 \"distribution-matching objectives sacrifice reasoning pathways\" 是描述非解释。更关键的是，Appendix T (Remove Valley) 实验显示 MMLU +3.3pp 可恢复——这表明退化部分源于可纠正的 allocation 问题，但论文未追踪此线索（如 task-aware allocation）。Forward KL 的 mode-covering 动机（§3.4: \"false negatives cascade\"）与 reasoning 退化之间的矛盾未讨论。\n\n**建议**: 深入分析 KL mask 在哪些层与 reasoning-critical activations 冲突；基于 Remove Valley 发现讨论 task-aware allocation 可能性；讨论 mode-covering 与 reasoning 退化的 trade-off。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [分歧 → Director 判定 Warning]** 无实际推理加速\n\nR2 将此列为 Critical，R1 列为 Should-Fix。论文在 Introduction 已明确定位为 empirical study 且声明不涉及 latency optimization。R1 正确指出 predictor 产生的 mask 可 plug into TEAL 的 kernel pipeline。**但**论文的 opening motivation 仍以 inference allocation 为核心，且 Table 5 显示 +6.4% 延迟。Director 判定：Should-Fix。论文应在主文中更显著说明 speedup 所需条件。\n\n**W2 [分歧 → Director 判定 Warning]** 与 MaskLLM 区分度\n\nR2 列为 Critical，R1 REBUT（contextual vs static masks 是 fundamental difference）。R1 的论证有力——per-token generalization、cross-layer allocation、OOD robustness 确实是本质差异而非应用场景差异。但核心 recipe（frozen model + KL + Gumbel masks）的重合不可否认。Director 判定：Warning。§2 已做 3-point differentiation，但论文应更明确定位为 systematic empirical analysis 而非暗示方法论创新。\n\n**W3 [共识]** Table 2 actual sparsity mismatch (KL 28.5% vs TEAL 29.3%)\n\nTable 2 的 ‡ 脚注容易忽略。Raw comparison (8.81 vs 10.82 = 18.6% improvement) 夸大优势，matched 28.5% comparison (14.5%) 仅在 Appendix。建议 Table 2 增加 TEAL at 28.5% 行或更显著标注。\n\n**W4 [共识]** KL global 50% 下游仅 s42 单种子\n\nTable 2 中 KL global 50% 的 ARC-c (32.85)、WG (63.46)、GSM8K (1.29) 无 ± 标注，与同表 KL uniform 50%（全部 3-seed）标准不一致。\n\n**W5 [共识]** 规模泛化仅 7–14B\n\nQwen-14B 的 GSM8K −20pp 暗示 reasoning 退化可能随规模恶化。如无法补充更大规模实验，应在 Limitations 中明确讨论 scale trade-off。\n\n**W6 [共识]** Figure 2 仅展示 global allocation 但 §4.2 推荐 uniform\n\n作为正文仅有的两张 figure 之一，Figure 2 的 framing 效果很强，但 uniform allocation 下 TEAL 在 MMLU 上系统性优于 KL。建议加入 uniform 曲线或在 caption 中明确说明。\n\n**W7 [共识]** Abstract 第5句信息密度过高\n\n约 60 词包含多层嵌套数字和条件，首次阅读几乎不可能理解。建议简化为 high-level takeaway。\n\n**W8 [共识]** Conclusion 引用 BoolQ 但不在 Table 2\n\nBoolQ 仅在 Appendix K=4 表中出现且 variance 极高 (std=11.5)，不应在 Conclusion 中引用。\n\n---\n\n### Minor（不影响接收）\n\n- **M1**: Table 2 注释过多（†, ‡, *, ±, §），BCE 30% 使用 TEAL global 与其他行不一致\n- **M2**: §3.5 deadzone margin ε=0.02 缺乏 justification\n- **M3**: §4.3 BCE 2700 steps 与 KL 1000 steps wall-clock 接近 (~46 vs ~45 min) 需解释（BCE 无 dense forward pass）\n- **M4**: \"Adaptive Penalty Controller\" 命名不准确——实际是 geometric doubling + deadzone，非经典 dual ascent\n- **M5**: References 中 FastForward (arXiv:2602.00397) 如已被会议接收应更新\n- **M6**: Limitations 未讨论 sequence length 对 predictor mask 质量的影响\n- **M7**: Table 1 (Taxonomy) 中 SPON 归入 \"Static × Coupled\" 的合理性应在正文讨论\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成 **[AGREE]**：\n\n1. **C1 因果声明过强** — 应降级为 transferability claim（R1-N1 + R2-W4）\n2. **97.5% decomposition 不可靠** — 应替换为定性描述（R1-N2 + R2 交叉同意升级 Critical）\n3. **MMLU/GSM8K 退化需更深分析** — Remove Valley 线索未追踪（R2-N2 + R1 borderline Must-Fix）\n4. **Table 2 sparsity mismatch 不够显著** — 需更显著标注（R1-W2 + R2 AGREE）\n5. **KL global 50% 下游缺 3-seed** — 标准不一致（R1-W4 + R2 AGREE）\n6. **Figure 2 global/uniform 误导** — 需补充 uniform 曲线（R2-W2 + R1 AGREE）\n7. **Abstract/Conclusion 写作问题** — 密度过高 + BoolQ 不当引用（R2-W3/W5 + R1 AGREE）\n8. **研究问题有价值** — 训练目标如何影响 mask quality 是 under-explored 但重要的问题\n9. **实验覆盖面远超同类工作** — 消融设计用心，可复现性好\n\n---\n\n## Reviewer Divergence\n\n**分歧 1: Wall-clock speedup 的严重程度**\n- **R2**: Critical (N1) — 作为 efficiency-motivated 工作，+6.4% 延迟且无加速证据是核心缺陷\n- **R1**: Should-Fix (W1, REBUT) — 论文已定位为 analysis work；predictor masks 可 plug into TEAL kernel pipeline；如果将此升级为 Must-Fix，大量分析性论文都会因 \"无端到端系统集成\" 被拒\n- **Director 判定**: **Warning** — R1 论证有力，论文的自我定位清晰且合理，但应在主文更显著说明 speedup 路径\n\n**分歧 2: MaskLLM 区分度**\n- **R2**: Critical (N3) — 核心 recipe 完全共享，3 个差异是应用场景差异非方法论创新\n- **R1**: REBUT (Minor/Should-Fix) — contextual vs static masks 是 fundamental architectural difference；cross-layer allocation 是本文独有的；recipe 层面的共享不等于方法论重叠（类似 knowledge distillation 的标准 recipe）\n- **Director 判定**: **Warning** — R1 的 REBUT 有效，contextual vs static 确实是本质差异；但论文应更诚实定位为 systematic empirical analysis\n\n**分歧 3: K=4 at 50% 缺失的严重程度**\n- **R1**: Should-Fix (W5) — 50% 是 coupling 贡献最大的区间，缺少 K=4 无法判断真实贡献\n- **R2**: REBUT (不应为 Should-Fix) — 50% 是 capacity-limited regime，所有方法 downstream 接近 random，K=4 decomposition 在 noise floor 附近意义不大\n- **Director 判定**: 保留为 **Warning**。R2 的 rebut 有道理但论文应解释原因\n\n---\n\n## Questions\n\n1. **[R1-Q1]** \"Reverse C1\"——在 magnitude-based masks 上训练 KL（而非 BCE）结果如何？如果 KL coupling 在 magnitude targets 上也效果好，则弱化 \"mask patterns are the driver\" 声明。\n2. **[R1-Q2]** 为何 50% 没做 K=4？是资源限制还是训练不稳定？\n3. **[R1-Q3 / R2-Q1]** Remove Valley 可恢复 MMLU +3.3pp，为何不探索 task-aware allocation？这是低悬果实。\n4. **[R2-Q3]** \"14.5% PPL reduction\" 基于 matched 28.5% sparsity——Table 2 呈现方式是否会让读者误读为 18.6%？\n5. **[R2-Q5]** §3.6 声称 gradient coupling 发现 68% divergent masks，但 C1 说 mask patterns（而非 coupling）是 driver——两者关系需更清晰阐述。如果 coupling 主要用于 discover masks，是否可以 KL 训练后提取 masks 再用 BCE 部署？\n6. **[R1-Q4]** 30% target λ 达 cap (5000) 但实际仅 28.5%（5% deviation）。提高 λ_max 能否逼近 30%？\n\n---\n\n## Missing References\n\n1. **LaRoSA** (2025, arXiv:2507.01299) — Layerwise Rotated Sparse Activation，在 SwiGLU 模型上实现 wall-clock speedup，高度相关但未引用\n2. **Geva et al. (2023)** \"Dissecting Recall of Factual Associations\" — 已在 bib 中但正文未引用，与 MMLU regression 讨论相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 已跳过（用户在审稿群中跳过了外部审稿请求）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 完成但 Agent 报错（rate limit: \"You've hit your limit · resets 6pm (UTC)\"），无有效视觉审查发现。用户可在 rate limit 重置后重新触发。\n\n格式合规检查由 R2 手动完成：\n| 项目 | 状态 |\n|------|------|\n| 正文页数 | ✅ §1-§5 在第8页结束 |\n| Limitations | ✅ p9，不计入页数，3个关键点 |\n| Ethics | ✅ p9，简短适当 |\n| 匿名化 | ✅ \"Anonymous ACL submission\" |\n| Appendix 双栏 | ✅ ACL 格式 |\n| 引用格式 | ✅ acl_natbib |\n\n---\n\n## Overall Assessment\n\n**评分**: 3.0 (Findings)\n**置信度**: 4/5\n\n**R1**: 3.5 (Borderline Conference) — Soundness 3.5, Excitement 3.0\n**R2**: 3.0 (Findings) — Soundness 3.5, Excitement 2.5\n**Director 综合**: 3.0 (Findings)\n\n**理由**: 论文的核心发现（KL distillation 优于 BCE 训练稀疏性预测器）可信且有实验支撑，实验设计的系统性和覆盖面是明显优势。但两个核心分析贡献（C1 target-swap ablation 和 97.5% signal-type decomposition）的 claim 强度超出实验证据——这两个声明出现在 Abstract、Introduction contributions list、和 Conclusion 的核心位置，是论文三大贡献中的两个。加之 MMLU/GSM8K 在所有测试规模上系统性逊于 training-free baseline TEAL，且缺乏 wall-clock speedup，整体贡献更适合 Findings 而非主会议。\n\n**升级路径**: 如果 (1) N1/N2 的 claim 调整为更审慎的措辞，(2) 基于 Remove Valley 发现追踪 task-aware allocation，(3) 补充 K=4 at 50% 实验，论文有望升至 3.5 (Borderline Conference)。如进一步补充 wall-clock speedup 数据（即使仅一个 sparsity level），可达 4.0 (Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution list 第1条过长（4行），建议拆分为 per-layer decomposition 和 cross-scale evidence\n- \"14.5% over TEAL at matched sparsity\" 的 \"matched sparsity\" 在此处首次出现但未解释，建议明确 (KL 28.5% vs TEAL 28.5%)\n\n### §3 Method\n- §3.5 Adaptive Penalty Controller: ε=0.02 的选择缺乏 justification；\"adaptive\" 命名可能误导——实际是 geometric doubling + deadzone\n- §3.6 Gradient Analysis: 与 §4.4 C1 的关系需要更清晰阐述——§3.6 argue coupling 是优势来源，§4.4 argue mask patterns（而非 coupling）是 driver。当前叙事的矛盾是：coupling 的作用仅在于 training-time discovery 还是 inference-time maintenance？\n- §3.7 Taxonomy: Table 1 有用但本身不构成 intellectual contribution；SPON 的 \"Static × Coupled\" 分类应在正文简要讨论\n\n### §4 Experiments\n- Table 2: 注释过多（5 种 footnote symbols）；BCE 30% 使用 TEAL global (†) 与其他行不一致且容易被忽略\n- §4.3 Extended Training: BCE 2700 steps wall-clock 与 KL 1000 steps 接近 (~46 vs ~45 min) 需解释——BCE 不需要 dense forward pass，每步应更快\n- §4.4 C1 Ablation: \"suggests\" hedging 是好的，但 Abstract 中的 \"as the proximate quality driver\" 措辞过于绝对\n- §4.5 Per-Layer KL: \"97.5%\" 的精确数字与 Footnote 5 的 \"not fully orthogonal\" caveat 之间的显著性严重不对称；K=4 MMLU anomaly (>100% gap closure) 应在正文而非 Appendix 讨论\n\n### §5 Conclusion\n- 仅 2 句话 (~130 词)，信息密度过高\n- 引用了 BoolQ (仅 Appendix, high variance) 但未引用 HellaSwag/PIQA (Table 11, stable)\n- 完全没有提及 limitations (MMLU regression, no speedup, scale bounds)\n\n### Appendix\n- 19 页 Appendix 提供了充分补充，信息分配总体合理\n- Appendix T (Constraint Analysis) 的发现（Remove Valley: MMLU +3.3pp）应在正文获得更多讨论，而非仅作为 supporting evidence",
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 1835 · 2026-05-22T17:31:02.462215+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4017
}
```

</details>

---


### Tool call

_source line 1836 · 2026-05-22T17:31:20.108591+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 和 Reviewer 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 和 Reviewer 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1837 · 2026-05-22T17:31:20.109158+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1838 · 2026-05-22T17:31:32.844421+00:00_

审稿报告已投递至 Research Director。

**Round 22 审稿完成。**

- **Overall**: 3.0 (Findings)，R1 给 3.5 / R2 给 3.0
- **3 个 Must-Fix**：C1 因果声明过强、97.5% decomposition 混淆、MMLU/GSM8K 系统性退化
- **8 个 Should-Fix**：wall-clock speedup gap、MaskLLM 定位、sparsity mismatch、50% 单种子、规模泛化、Figure 2 误导、Abstract 密度、BoolQ 引用
- **2 个分歧**：wall-clock 严重程度（R2 Critical vs R1 Warning → Director 判 Warning）、MaskLLM 区分度（R2 Critical vs R1 Minor → Director 判 Warning）
- **升级路径**：claim 调整 + task-aware allocation 追踪 → 3.5；再加 wall-clock speedup → 4.0
- **Issue Tracker 已同步更新**（22 条 issue，7 条 open/pending action items）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 157

## Round 157

2 recorded events


### User

_source line 1839 · 2026-05-22T17:31:33.867775+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心分歧点：

1. **R2-N1 (wall-clock speedup)**: 我反驳其 critical 级别——论文明确定位为 empirical analysis 而非 system work，应为 Should-Fix
2. **R2-N3 (MaskLLM 区分度)**: 我反驳——contextual vs static masks 是 fundamental architectural difference，非 "应用场景差异"
3. **R2-N2 (MMLU 退化)**: 基本同意，认为介于 Should-Fix 和 Must-Fix 之间
4. 其余 Should-Fix 和 Questions 大部分同意 R2 的判断，特别是 W2 (Figure 2 误导)、W3 (Conclusion BoolQ)、W4 (C1 confound) 与我自己的审稿一致

---

[Reviewer 2 审稿结果]:
交叉回应已提交。主要判断：

- R1 的 N1 (C1 causal claim) 和 N2 (97.5% decomposition confound) **均同意**，两者都涉及论文核心 claim 的过度表述
- R1 的 W1-W4 **同意**，W5 (K=4 at 50% 缺失) **部分反驳**——50% 是 capacity-limited regime，K=4 downstream decomposition 在 noise floor 附近意义有限
- Minor 中对 M2 (SPON taxonomy 分类) **反驳**——SPON 的 per-layer KL 确实符合 "coupled" 定义
- 两位 reviewer 的核心共识：C1 claim 过强、wall-clock speedup 缺失、MMLU 退化未充分解释
- 我维持 Overall 3.0 (Findings)，与 R1 的 3.5 差异主要在 novelty 评估上

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1840 · 2026-05-22T17:31:47.746371+00:00_

审稿报告已投递至 Research Director。

**Round 22 审稿总结**：

- **Overall: 3.0 (Findings)**（R1: 3.5 Borderline Conference, R2: 3.0 Findings）
- **3 个 Must-Fix**: (1) C1 因果声明过强→应降级为 transferability; (2) 97.5% decomposition 受混淆变量影响→应替换为定性描述; (3) MMLU/GSM8K 跨架构退化缺机制解释→应追踪 Remove Valley 线索
- **8 个 Should-Fix**: wall-clock gap [分歧→Warning]、MaskLLM 区分度 [分歧→Warning]、actual sparsity mismatch、KL global 50% 单种子、规模泛化不足、Figure 2 misleading、Abstract 密度、Conclusion BoolQ
- **升级路径**: N1/N2 claim 调整 + task-aware allocation 探索 → 3.5; 补充 wall-clock speedup → 4.0
- Issue Tracker 已同步更新（14 个 open/in_progress issues）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 158

## Round 158

84 recorded events


### User

_source line 1841 · 2026-05-22T23:36:44.464668+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1842 · 2026-05-22T23:36:53.110396+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1843 · 2026-05-22T23:36:53.161369+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1844 · 2026-05-22T23:37:00.084688+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1845 · 2026-05-22T23:37:00.135296+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1846 · 2026-05-22T23:37:02.344608+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1847 · 2026-05-22T23:37:02.495576+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1848 · 2026-05-22T23:37:05.055267+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1849 · 2026-05-22T23:37:05.156046+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1850 · 2026-05-22T23:37:07.113540+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_post_to_reviewer",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_post_to_reviewer",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1851 · 2026-05-22T23:37:07.164155+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1852 · 2026-05-22T23:37:10.526656+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "dispatch_visual_check",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "dispatch_visual_check",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1853 · 2026-05-22T23:37:10.577346+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1854 · 2026-05-22T23:37:11.029300+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "submit_review_report_to_research_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "submit_review_report_to_research_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1855 · 2026-05-22T23:37:11.029649+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1856 · 2026-05-22T23:37:11.531660+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "update_review_issues",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "update_review_issues",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1857 · 2026-05-22T23:37:11.531990+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1858 · 2026-05-22T23:37:11.983829+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "get_visual_check_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "get_visual_check_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1859 · 2026-05-22T23:37:11.984196+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1860 · 2026-05-22T23:37:12.436071+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "get_external_review_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "get_external_review_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1861 · 2026-05-22T23:37:12.436466+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1862 · 2026-05-22T23:37:12.941161+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "request_external_review",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "request_external_review",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1863 · 2026-05-22T23:37:12.941482+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1864 · 2026-05-22T23:37:13.042057+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_project_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1865 · 2026-05-22T23:37:13.092628+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1866 · 2026-05-22T23:37:18.442223+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1867 · 2026-05-22T23:37:19.446258+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (378 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- perlayer_kl_50_s42_boolq（准备中）\n- perlayer_kl_50_s42_ppl（准备中）\n- revkl_30_s42_boolq_uniform（准备中）\n- diag_eval_env_34887（准备中）\n- perlayer_kl_s456_ppl_repro: Reproducibility check: per-layer KL s456 PPL should match original 9.0282. Running with same checkpoint on different eval session to verify stability.（准备中）\n- diag_status_34887（准备中）\n- diag_status_41718（准备中）\n- read_boolq_results（准备中）\n- diag_ckpt_34887（准备中）\n- diag_ckpt_41718（准备中）\n- …另有 39 项\n\n## 近期结论\n- **perlayer_kl_50_s42** (negative): Per-layer KL 50% uniform training (seed 42). Tests whether 2D decomposition (signal type × coupling scope) holds at higher sparsity. PPL should fall between E2E KL 50% (11.84) and MSE (18.52). If gap to E2E KL is small (&lt;5%), signal type dominates PPL even at 50%, strengthening the 2D claim.\n  [perlayer_kl_50_s42 analysis](/api/workspace-files/projects/distill_sparse_swiglu/artifacts/perlayer_kl_50_s42/report/analysis.md)\n- **perlayer_kl_s123_downstream_v2** (success): Per-layer KL s123 downstream 6-task eval (ARC-c, WG, MMLU, GSM8K, HS, PIQA) — excluding BoolQ due to missing super_glue cache on westd-34887. Retry of perlayer_kl_s123_downstream. ← 基于 perlayer_kl_30_s123_v
…[truncated 1796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1868 · 2026-05-22T23:37:19.446781+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1869 · 2026-05-22T23:37:19.447094+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1870 · 2026-05-22T23:37:19.648159+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1871 · 2026-05-22T23:37:19.749000+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1872 · 2026-05-22T23:37:28.682099+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions",
  "allowed_domains": "['aclweb.org', 'openreview.net', '2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions",
    "allowed_domains": "['aclweb.org', 'openreview.net', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 1873 · 2026-05-22T23:37:34.001772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1874 · 2026-05-22T23:37:34.052498+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	\input{limitations}
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1875 · 2026-05-22T23:37:34.153208+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/submitted.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/submitted.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1876 · 2026-05-22T23:37:34.203893+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1877 · 2026-05-22T23:37:34.254659+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1878 · 2026-05-22T23:37:34.405536+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool result

_source line 1879 · 2026-05-22T23:37:36.011417+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EMNLP 2026 Workshop NLLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FNLLP_ARR_Commitment"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

Based on the search results, here's what I found about EMNLP 2026 ARR call for papers submission guidelines and author instructions:

## Submission Process

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system with final decisions 
…[truncated 1618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7329
}
```

</details>

---


### Tool call

_source line 1880 · 2026-05-22T23:37:44.573771+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May cycle submission deadline page limits formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May cycle submission deadline page limits formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 1881 · 2026-05-22T23:37:44.875343+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1882 · 2026-05-22T23:37:45.377595+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (max $\Delta$$\leq$0.79pp, 3-seed).
5	Signal type (output-distribution vs.\ intermediate loss) accounts for the majority of the PPL gap at 30\% (upper bound; not fully orthogonal with coupling scope).
6	Cross-layer coupling contributes 29--97\% on downstream tasks (3-seed $K{=}4$-corrected): coupling-dominated for commonsense (ARC-c 97\%, WG 67\%) and mismatch-dominated for reasoning (GSM8K 29\%).
7	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
8	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1883 · 2026-05-22T23:37:45.378055+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1884 · 2026-05-22T23:37:45.779899+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	While MaskLLM~\cite{fang2024maskllm} applies KL-based mask optimization, it targets static N:M weight sparsity; activation sparsity requires masks that generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation suggests that KL-discovered mask targets carry most of the quality information at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.2
…[truncated 2952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1885 · 2026-05-22T23:37:45.780464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1886 · 2026-05-22T23:37:45.831187+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importan
…[truncated 9686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1887 · 2026-05-22T23:37:58.100640+00:00_

Web search results for query: "ACL Rolling Review 2026 May cycle submission deadline page limits formatting requirements"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Let me search for more specific information about the May cycle details and formatting requirements.

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational 
…[truncated 4125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 13526
}
```

</details>

---


### Tool call

_source line 1888 · 2026-05-22T23:38:02.717980+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1889 · 2026-05-22T23:38:03.671797+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17513 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1890 · 2026-05-22T23:38:03.672213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1891 · 2026-05-22T23:38:04.124121+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
7	Wang et al.~\cite{wang2025dynamicsparse} address dynamic sparsity--quantization interaction; AWQ~\cite{lin2024awq} applies activation-aware weight quantization for on-device deployment; Outlier Suppression+~\cite{wei2023outlier} mitigates outlier-induced quantization errors via shifting and scaling.
8	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
9	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
10	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
11	
12	\paragraph{Predictor-Based Contextual Sparsity.}
13	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
14	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
15	FastForward~\cite{gautam2026fastforward} adds a 67.2M-
…[truncated 5170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1892 · 2026-05-22T23:38:04.124543+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1893 · 2026-05-22T23:38:04.626502+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the dominant design dimension for PPL (signal type accounts for the majority of the gap; upper bound); cross-layer coupling contributes 29--97\% on downstream tasks (3-seed $K{=}4$-corrected; Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A predictor ($<$1\% of base) reduces TEAL's PPL by 14.5\% via masks 46--68\% divergent from magnitude, with commonsense gains but knowledge-task regression across scales.
6	Limitations: MMLU/GSM8K decline, no wall-clock speedup, evaluation bounded at 7--14B.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1894 · 2026-05-22T23:38:04.626840+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1895 · 2026-05-22T23:38:04.827812+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated. All experiments use sequence length 2048; behavior at longer contexts (e.g., 8K--128K) is untested. Evaluation is limited to 7--14B; scaling to 70B+ and wall-clock speedup via sparse kernels remain future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 1896 · 2026-05-22T23:38:04.828220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1897 · 2026-05-22T23:38:04.878732+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1898 · 2026-05-22T23:38:13.059041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1899 · 2026-05-22T23:38:13.511410+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 36747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1900 · 2026-05-22T23:38:14.013579+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1901 · 2026-05-22T23:38:14.465593+00:00_

1	% =============================================================================
2	% Additional references (R20 review response)
3	% =============================================================================
4	
5	@article{huang2025larosa,
6	  title={La{R}o{SA}: Accelerating Large Language Model Inference with Layerwise Rotated Sparse Activation},
7	  author={Huang, Fangcheng and others},
8	  journal={arXiv preprint arXiv:2507.01299},
9	  year={2025}
10	}
11	
12	@inproceedings{geva2023dissecting,
13	  title = {Dissecting Recall of Factual Associations in Auto-Regressive Language Models},
14	  author = {Geva, Mor and Bastings, Jasmijn and Filippova, Katja and Globerson, Amir},
15	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
16	  pages = {12216--12235},
17	  year = {2023},
18	}
19	
20	@article{fu2024lazyllm,
21	  title = {{LazyLLM}: Dynamic Token Pruning for Efficient Long Context {LLM} Inference},
22	  author = {Qichen Fu and Minsik Cho and Thomas Merth and Sachin Mehta and Mohammad Rastegari and Mahyar Najibi},
23	  year = {2024},
24	  journal = {arXiv preprint arXiv:2407.14057},
25	}
26	
27	@article{zhang2025cots,
28	  title = {{COTS}: Connected Sparse Activation for Efficient {LLM} Inference},
29	  author = {Yilong Zhang and Junyuan Shang and Huanqi Cao and Shiyao Li and Shuguang Jiang and Lingxiao Ma and Shun Zheng and Cheng Li and Jiang Bian},
30	  year = {2025},
31	  journal = {arXiv preprint arXiv:2502.14475},
32	}
33	
34	@inproceedings{alizadeh2024llmflash,
35	  title = {{LLM} in a Flash: Efficient Large Language Model Inference with Limited Memory},
36	  author = {Keivan Alizadeh and Iman Mirzadeh and Dmitry Belenko and Karen Khatamifard and Minsik Cho and Carlo C Del Mundo and Mohammad Rastegari and Mehrdad Farajtabar},
37	  year = {2024},
38	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
39	}
40	
41	@article{wei2023outlier,
4
…[truncated 3106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1902 · 2026-05-22T23:38:14.767001+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "writing_plan.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "writing_plan.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1903 · 2026-05-22T23:38:14.817730+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026 (ARR May cycle)\\n  track: Efficient Methods for NLP\\n  template: acl2023  # ARR confirmed acl2023 style\\n  template_note: \\\"\\\"\\n  page_limit: 8\\n  deadline: 2026-05-25\\n  core_claim: >\\n    Output-distribution distillation (KL) simultaneously achieves better quality\\n    and simpler architecture (no error compensation) for activation sparsity prediction\\n    in SwiGLU LLMs. The KL advantage is structural — BCE's per-neuron objective is\\n    mismatched with global top-k inference — and persists across 30–70% sparsity with\\n    growing gap (18%→48%→82%). SPON's static correction is orthogonal to KL and too\\n    weak to complement it. We unify existing methods through a 2D taxonomy and validate\\n    across architectures (LLaMA-3.1-8B / Mistral-7B-v0.3).\\n  created_at: 2026-05-16T00:00:00Z\\n  verify_refs: true\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 200\\n    core_bullets:\\n      - \\\"问题: SwiGLU LLMs 的 activation sparsity 推理加速需要 predictor，但现有 BCE-trained predictor 需额外 compensation network（67.2M params）\\\"\\n      - \\\"Insight: KL divergence 训练将所有 neuron 决策通过 output distribution 耦合，自然捕获 joint interaction\\\"\\n      - \\\"结果: KL-only predictor PPL 11.79 @ 50% sparsity（无 compensation），BCE iso-compute 2700步 PPL 27.97（structural mismatch）\\\"\\n      - \\\"分析: SPON static correction 与 KL 近正交（cos_sim=0.196），magnitude 仅 15.8%——KL subsumes SPON 效果\\\"\\n      - \\\"贡献: 2D taxonomy 统一现有方法，30-70% sparsity scaling（KL优势 18%→48%→82%），跨架构验证（Mistral-7B）\\\"\\n    dependencies: [experiments, method]\\n\\n  - section: introduction\\n    word_budget: 1100\\n    core_bullets:\\n      - \\\"Hook: SwiGLU LLMs 可通过 50% neuron pruning 获得 ~2x 推理加速，但 training-free 方法 PPL 退化 94-480%\\\"\\n      - \\\"Context: learned predictor 是当前最佳方案（DejaVu, FastForward），
…[truncated 1533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1904 · 2026-05-22T23:38:19.368345+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1905 · 2026-05-22T23:38:19.418920+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1906 · 2026-05-22T23:38:25.893206+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1907 · 2026-05-22T23:38:26.245199+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1908 · 2026-05-22T23:38:26.245617+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1909 · 2026-05-22T23:38:26.296151+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1910 · 2026-05-22T23:38:29.207149+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1911 · 2026-05-22T23:38:29.559090+00:00_

1	issues:
2	  # ============================================================
3	  # Round 22 — Active issues
4	  # ============================================================
5	
6	  - id: "R19-N3"
7	    summary: "无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无 speedup"
8	    category: experiment
9	    severity: warning
10	    status: resolved
11	    first_raised_round: 16
12	    last_seen_round: 22
13	    mentions:
14	      - {round: 21, reviewers: [1, 2], note: "R21 Critical。Intro framing 已修改为 empirical study。"}
15	      - {round: 22, reviewers: [1, 2], note: "降为 Warning (W1)。R1 REBUT 有效。论文已定位为 analysis work。"}
16	    action_items:
17	      - {round: 21, action: "Abstract 加 empirical study + §1 disclaimer 正文句子", assigned_to: "paper_agent", status: done}
18	      - {round: 22, action: "§1 加 speedup 条件 (sparse GEMM kernels) + 6.4% overhead 数字", assigned_to: "paper_agent", status: done}
19	    resolution: "结构性限制。Abstract 'empirical study' + §1 wall-clock disclaimer + speedup 条件全部落地。降为 Warning 并 resolved。"
20	    resolution_round: 23
21	
22	  - id: "R20-N2"
23	    summary: "MMLU/GSM8K 跨架构系统性退步"
24	    category: experiment
25	    severity: critical
26	    status: resolved
27	    first_raised_round: 18
28	    last_seen_round: 22
29	    mentions:
30	      - {round: 21, reviewers: [1, 2], note: "R21 Critical。Protection valley 分析仅 correlational。"}
31	      - {round: 22, reviewers: [1, 2], note: "R22 N3。要求追踪 Remove Valley + task-aware allocation + mode-covering 讨论。"}
32	    action_items:
33	      - {round: 21, action: "Constraint 实验 (protect_late + remove_valley)", assigned_to: "main_agent", status: done}
34	      - {round: 22, action: "§4.2 深化: Geva 引用 + task-aware allocation future direction + mode-covering trade-off", assigned_to: "paper_agent", status: done}
35	    resolution: "Constraint 因果证据 + §4.2 task-dependent trade-off 叙事 + Geva 引用 + task-aware allocation future direction。"
36	    resolution_round: 23
37	
38	  - id: "R20-W1"
39	    summary: "Per-layer KL tr
…[truncated 10427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1912 · 2026-05-22T23:38:29.609765+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent"
  }
}
```

</details>

---


### Tool result

_source line 1913 · 2026-05-22T23:38:29.660373+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1914 · 2026-05-22T23:38:34.728436+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "paper_framing.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "paper_framing.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1915 · 2026-05-22T23:38:34.929632+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md\", \"content\": \"# Paper Framing — distill_sparse_swiglu\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\\n- Deadline: 2026-05-25 (ARR submission)\\n- Track: Efficient Methods for NLP\\n\\n## Core Claims\\n\\n1. **KL distillation discovers fundamentally different (and superior) neuron importance patterns that magnitude-based oracles miss**: The C1 target-swap ablation (D059, 3-seed) suggests that KL-discovered mask targets carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (max Δ≤0.79pp, 3-seed). Standard BCE (magnitude masks) PPL ≈ 22.51. The 46-68% mask divergence (per-layer Jaccard 32%) between KL-derived and magnitude-based masks is the core empirical finding: KL discovers a qualitatively different neuron importance landscape. **2D decomposition (K=4 per-layer KL)**: Signal type (output-distribution vs intermediate loss) accounts for the majority of the PPL gap at 30% (upper bound; not fully orthogonal with coupling scope). Cross-layer coupling contributes 29-97% on downstream tasks (3-seed K=4-corrected): coupling-dominated for commonsense (ARC-c 97%, WG 67%) and mismatch-dominated for reasoning (GSM8K 29%). **Sparsity-dependent pattern**: At 50%, K=4 per-layer KL (PPL 44.23) is worse than K=1 (34.85), revealing that coupling scope dominates at high sparsity—reversing the 30% pattern where signal type dominates. **Implication**: The gradient coupling analysis (§3.6) provides mathematical intuition for *why* KL can discover better targets (coupled gradients explore joint neuron interaction patterns). C1 shows the discovered masks carry most quality info; K=4 shows coupling helps discover better masks with task-dependent contribution. This shifts the contribution from \\\"engineering a better loss\\\" to \\\"discovering that output-distribution d
…[truncated 1346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1916 · 2026-05-22T23:38:34.929984+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1917 · 2026-05-22T23:38:35.030681+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1918 · 2026-05-22T23:39:21.531355+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查**方法严谨性和实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL template ([review] option), double-blind\n- **页数限制**: 8 页正文 + unlimited references; Limitations/Ethics 不计页数\n- **匿名规则**: double-blind（作者匿名为 \"Anonymous\"）\n\n## 论文路径\n- LaTeX: `projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf`\n\n## 你的审查侧重\n\n### 方法严谨性\n1. **KL Distillation 框架**：Gumbel-Sigmoid 放松、forward KL 选择的理论/实验依据、geometric penalty schedule 的收敛性\n2. **C1 Target-Swap Ablation**：实验设计是否足以支撑 \"mask patterns carry most quality information\" 的声明？oracle mask provenance（s42 早期 checkpoint vs s123/s456 matched retrained）是否引入 confound？\n3. **Per-layer KL 2D 分解**：K=1 和 K=4 控制实验的 train-inference mismatch confound 处理是否充分？\"signal type dominates PPL (upper bound)\" 声明的强度是否合理？\n4. **统计严谨性**：3-seed mean±std 的充分性、seed 选择偏差风险、高方差指标（ARC-c σ=3.6, BoolQ σ=11.5）的处理\n\n### 实验设计\n5. **Baselines 公平性**：BCE iso-compute 比较（1000 vs 2700 步）、MSE baseline 配置、TEAL comparison 的 actual sparsity mismatch\n6. **评估覆盖度**：WikiText-2/C4 PPL + 6 下游任务是否足够？sequence length 2048 的限制性？缺少 batched inference 评估？\n7. **跨架构泛化**：Mistral-7B 和 Qwen-14B 结果是否充分支持泛化声明？14B GSM8K -20pp 的系统性退步是否被充分讨论？\n8. **Reproducibility**：实验细节是否完整（超参、硬件、数据处理）？\n\n请按 ARR 标准给出：Summary (2-3 句) → Strengths (逐条) → Weaknesses (逐条，按严重性排列：Critical > Warning > Minor) → Questions → Missing References → Overall Assessment (1-5 分，参照 EMNLP 2026 ARR 评分标准)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查**方法严谨性和实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL template ([review] option), double-blind\n- **页数限制**: 8 页正文 + unlimited references; Limitations/Ethics 不计页数\n- **匿名规则**: double-blind（作者匿名为 \"Anonymous\"）\n\n## 论文路径\n- LaTeX: `projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf`\n\n## 你的审查侧重\n\n### 方法严谨性\n1. **KL Distillation 框架**：Gumbel-Sigmoid 放松、forward KL 选择的理论/实验依据、geometric penalty schedule 的收敛性\n2. **C1 Target-Swap Ablation**：实验设计是否足以支撑 \"mask patterns carry most quality information\" 的声明？oracle mask provenance（s42 早期 checkpoint vs s123/s456 matched retrained）是否引入 confound？\n3. **Per-layer KL 2D 分解**：K=1 和 K=4 控制实验的 train-inference mismatch confound 处理是否充分？\"signal type dominates PPL (upper bound)\" 声明的强度是否合理？\n4. **统计严谨性**：3-seed mean±std 的充分性、seed 选择偏差风险、高方差指标（ARC-c σ=3.6, BoolQ σ=11.5）的处理\n\n### 实验设计\n5. **Baselines 公平性**：BCE iso-compute 比较（1000 vs 2700 步）、MSE baseline 配置、TEAL comparison 的 actual sparsity mismatch\n6. **评估覆盖度**：WikiText-2/C4 PPL + 6 下游任务是否足够？sequence length 2048 的限制性？缺少 batched inference 评估？\n7. **跨架构泛化**：Mistral-7B 和 Qwen-14B 结果是否充分支持泛化声明？14B GSM8K -20pp 的系统性退步是否被充分讨论？\n8. **Reproducibility**：实验细节是否完整（超参、硬件、数据处理）？\n\n请按 ARR 标准给出：Summary (2-3 句) → Strengths (逐条) → Weaknesses (逐条，按严重性排列：Critical > Warning > Minor) → Questions → Missing References → Overall Assessment (1-5 分，参照 EMNLP 2026 ARR 评分标准)。"
  }
}
```

</details>

---


### Tool result

_source line 1919 · 2026-05-22T23:39:37.298455+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15767
}
```

</details>

---


### Tool call

_source line 1920 · 2026-05-22T23:39:37.599926+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查**新颖性和完整性**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL template ([review] option), double-blind\n- **页数限制**: 8 页正文 + unlimited references; Limitations/Ethics 不计页数\n- **匿名规则**: double-blind（作者匿名为 \"Anonymous\"）\n\n## 论文路径\n- LaTeX: `projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf`\n\n## 你的审查侧重\n\n### 新颖性评估\n1. **核心贡献新颖性**：将 KL distillation 应用于 activation sparsity prediction 的新颖性如何？与 MaskLLM (frozen weights + learnable masks + KL) 的本质区别是否成立？\"output-distribution alignment as the dominant design dimension\" 是否足够新颖构成 EMNLP 主会议贡献？\n2. **2D Taxonomy**：signal type × coupling scope 分类框架是否有新颖洞见？还是仅仅是对现有方法的组织？\n3. **分析性贡献 vs 工程贡献**：论文自称 \"primarily an empirical study\"——在 EMNLP 2026 的标准下，纯分析/实证工作是否有足够的贡献门槛？\n\n### 完整性\n4. **Related Work 覆盖度**：是否遗漏了重要的相关工作？特别关注：(a) 其他 KL-based pruning/sparsity 方法, (b) 最新 2025-2026 activation sparsity 论文, (c) Gumbel-Sigmoid 在 mask learning 中的应用\n5. **叙事结构**：Abstract → Intro → Method → Experiments → Conclusion 的逻辑链是否清晰连贯？核心 claim 是否在各章节间一致？\n6. **Framing 诚实度**：论文声明的限制是否完整？是否有 overclaim？\"empirical study\" 定位是否前后一致？\n7. **写作质量**：信息密度、可读性、图表质量、notation 一致性\n\n### 格式合规\n8. **ARR 格式检查**：页数是否合规（8 页正文）？Limitations 章节是否存在且恰当？Ethics Statement 是否存在？匿名性是否维持？\n\n请按 ARR 标准给出：Summary (2-3 句) → Strengths (逐条) → Weaknesses (逐条，按严重性排列：Critical > Warning > Minor) → Questions → Missing References → Overall Assessment (1-5 分，参照 EMNLP 2026 ARR 评分标准)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查**新颖性和完整性**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL template ([review] option), double-blind\n- **页数限制**: 8 页正文 + unlimited references; Limitations/Ethics 不计页数\n- **匿名规则**: double-blind（作者匿名为 \"Anonymous\"）\n\n## 论文路径\n- LaTeX: `projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf`\n\n## 你的审查侧重\n\n### 新颖性评估\n1. **核心贡献新颖性**：将 KL distillation 应用于 activation sparsity prediction 的新颖性如何？与 MaskLLM (frozen weights + learnable masks + KL) 的本质区别是否成立？\"output-distribution alignment as the dominant design dimension\" 是否足够新颖构成 EMNLP 主会议贡献？\n2. **2D Taxonomy**：signal type × coupling scope 分类框架是否有新颖洞见？还是仅仅是对现有方法的组织？\n3. **分析性贡献 vs 工程贡献**：论文自称 \"primarily an empirical study\"——在 EMNLP 2026 的标准下，纯分析/实证工作是否有足够的贡献门槛？\n\n### 完整性\n4. **Related Work 覆盖度**：是否遗漏了重要的相关工作？特别关注：(a) 其他 KL-based pruning/sparsity 方法, (b) 最新 2025-2026 activation sparsity 论文, (c) Gumbel-Sigmoid 在 mask learning 中的应用\n5. **叙事结构**：Abstract → Intro → Method → Experiments → Conclusion 的逻辑链是否清晰连贯？核心 claim 是否在各章节间一致？\n6. **Framing 诚实度**：论文声明的限制是否完整？是否有 overclaim？\"empirical study\" 定位是否前后一致？\n7. **写作质量**：信息密度、可读性、图表质量、notation 一致性\n\n### 格式合规\n8. **ARR 格式检查**：页数是否合规（8 页正文）？Limitations 章节是否存在且恰当？Ethics Statement 是否存在？匿名性是否维持？\n\n请按 ARR 标准给出：Summary (2-3 句) → Strengths (逐条) → Weaknesses (逐条，按严重性排列：Critical > Warning > Minor) → Questions → Missing References → Overall Assessment (1-5 分，参照 EMNLP 2026 ARR 评分标准)。"
  }
}
```

</details>

---


### Tool call

_source line 1921 · 2026-05-22T23:39:38.704145+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 1922 · 2026-05-22T23:39:39.012473+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool result

_source line 1923 · 2026-05-22T23:39:40.522362+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 1818
}
```

</details>

---


### Assistant

_source line 1924 · 2026-05-22T23:39:53.061004+00:00_

Reviewer 1、Reviewer 2 和视觉审查 Agent 已全部派发，等待审稿结果返回。

- **Reviewer 1**: 方法严谨性 + 实验设计
- **Reviewer 2**: 新颖性 + 完整性
- **Visual Check**: 排版审查（非评分项，不阻塞报告）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 159

## Round 159

2 recorded events


### User

_source line 1925 · 2026-05-22T23:45:27.876077+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告（新颖性与完整性）

---

## 总体评分
**Overall**: 3.0 / 5 — Findings
**一句话总结**: 实验设计扎实、分析有洞见的实证研究，但核心贡献（KL 训练 sparsity masks）相对于 MaskLLM 的新颖性增量有限，"dominant design dimension" 的 claim 仅基于两种信号类型的对比，overclaim 风险较高。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 方法论整体合理，实验设计规范（C1 ablation、per-layer decomposition 等设计精巧），但核心 claim "output-distribution alignment is the dominant design dimension" 仅基于 BCE vs KL 二元对比，未测试其他分布级别损失函数（reverse KL、JSD、logit MSE），支撑不足以称"dominant" |
| Excitement | 2.5 / 5 | §3.6 梯度分析（BCE per-neuron independent vs KL coupled through output distribution）是有价值的分析性洞见；但整体方法是将已有技术（KL distillation + Gumbel relaxation）应用到新场景（contextual activation sparsity），incremental flavor 较重；无 wall-clock speedup 削弱实际影响力 |
| Reproducibility | 4.0 / 5 | 超参数、训练细节、predictor 架构均有详细描述；Appendix A-B 提供了完整的 inference efficiency 和 bottleneck sensitivity 分析；代码未公开但描述足够复现 |
| Overall Assessment | 3.0 / 5 | Findings 水平——实证工作扎实，但新颖性不足以达到主会议 bar |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心贡献与 MaskLLM 的新颖性区分不充分
- 具体位置：Section 2 (Related Work, paragraph "Weight Pruning, Distillation, and Routing") 及 Section 3.4
- 问题：MaskLLM (Fang et al., 2024, NeurIPS 2024 Spotlight) 已提出 KL divergence + Gumbel relaxation 训练可学习 sparsity masks 的范式。本文声称的区别是：(a) contextual vs. static masks, (b) activation sparsity vs. N:M weight sparsity, (c) cross-layer coupling analysis。但 (a) 和 (b) 属于 sparsity setting 的差异而非训练方法论的创新——核心 recipe（KL on output distributions + differentiable mask sampling）完全一致。论文 Section 2 仅用一句话提到 MaskLLM ("MaskLLM shares the recipe-level principle of frozen weights + learnable masks + KL training")，未深入分析为何在 contextual activation sparsity setting 下这一 recipe 会产生质性不同的 behavior。
- 为什么影响接收：如果 reviewer/AC 认为这是 MaskLLM 在不同 sparsity setting 的直接应用，整篇论文的贡献定位会受到根本性质疑。
- 建议修改方向：(1) 专门设立 paragraph 深入对比 MaskLLM——不仅说"区别在哪"，更要说"为什么这些区别导致了不同的技术挑战和 findings"（如 MaskLLM 的 Gumbel-Softmax 在有限候选集上采样 vs. 本文 Gumbel-Sigmoid 在连续空间上的 per-neuron relaxation；MaskLLM 无 cross-layer coupling 因为 N:M masks 是 layer-local 的）；(2) §3.6 梯度分析是本文的独特贡献，应更突出其与 MaskLLM 的区别——MaskLLM 未分析 gradient coupling。

**N2** [critical] "Dominant design dimension" claim overclaimed
- 具体位置：Abstract ("output-distribution alignment is the critical design dimension for learned sparsity"), Section 5 Conclusion ("Output-distribution alignment is the dominant design dimension for PPL")
- 问题：该 claim 仅基于两种 signal type 的对比：BCE（per-neuron classification）vs. forward KL（output distribution）。论文未测试：
  - **Reverse KL**（仅在 Section 3.5 提及"forward rather than reverse KL" 并引用一个 validation choice，但未提供 reverse KL 实验结果）
  - **JSD**（Jensen-Shannon divergence，knowledge distillation 领域常用）
  - **MSE on logits/hidden states**（intermediate distillation，不同于 per-neuron BCE 也不同于 output KL）
  - **Cosine similarity on output distributions**
  在仅比较两种方法的情况下声称"dominant"，逻辑上不成立。此外，Table 3 中 BCE+Gumbel (32.22) vs KL (28.13) 的差距虽然显著，但 BCE+Gumbel 仍然远优于 BCE-only，说明 Gumbel relaxation 本身也是重要因素，不能简单归功于 KL vs BCE。
- 为什么影响接收：Overclaim 是 ARR reviewer 的核心 red flag。如果 claim 被降级为 "KL outperforms BCE for contextual sparsity prediction"，论文的 framing 需要全面调整。
- 建议修改方向：(1) 补充至少一种其他分布级别损失（reverse KL 或 JSD）的实验；(2) 将 claim 软化为 "output-distribution alignment substantially outperforms per-neuron classification"，而非 "dominant design dimension"。

**N3** [critical] 实验规模单一，削弱 generalizability claim
- 具体位置：Section 4 全部主实验（Table 2-4, Figure 2）均基于 LLaMA-3.1-8B；跨架构实验（Mistral-7B, Qwen-2.5-14B）仅在 Appendix N-O
- 问题：论文声称发现了 learned sparsity 的通用设计原则（"the dominant design dimension"），但核心实验（Table 2-4, §4.3-4.5）全部基于单一模型（LLaMA-3.1-8B）。跨架构验证（Appendix N: Mistral-7B 仅 Table 16 一个表；Appendix O: Qwen-2.5-14B 仅 Table 13-14）过于简略。特别是：
  - Qwen-2.5-14B 的 Table 13 仅展示 30% sparsity 下的 PPL 和 downstream accuracy，无 C1 ablation 或 gradient SNR 分析
  - 无任何 70B+ 模型的实验，而 sparsity 在大模型上的实际价值更高
  - 无非 LLaMA-family 架构的深入分析（如 Falcon、Gemma 等）
- 为什么影响接收：从单一 8B 模型推广到 "the dominant design dimension for learned sparsity" 的 generalization gap 过大。
- 建议修改方向：(1) 将至少一个跨架构实验（含 C1 ablation）提升到主文；(2) 在 Limitations 中明确承认实验规模的局限性。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 无 wall-clock speedup 结果
- 具体位置：Abstract ("wall-clock speedup without sparse kernel support is not addressed here"), Appendix A
- 问题：作为一篇 activation sparsity 论文，完全不报告实际推理加速效果是一个明显缺失。Appendix A 仅展示 predictor overhead (6.4%) 和 dense inference 对比下的 latency，但未展示 sparse execution 的实际加速。论文承认 "unstructured element-wise masks... do not translate to wall-clock speedup without sparse kernel support"——这实质上承认了方法当前没有实际加速价值。
- 建议：(1) 至少展示使用已有 sparse kernel (如 Triton block-sparse) 的 wall-clock 对比；或 (2) 在 Limitations 中更显著地讨论此限制而非仅一句话带过。

**W2** [warning] 训练数据过于有限
- 具体位置：Section 4.1 ("trained for 1000 steps on WikiText-103")
- 问题：Predictor 仅在 WikiText-103 上训练 1000 步（约 200M tokens）。Appendix D (Out-of-Distribution Evaluation) 在 C4 上测试了 OOD 泛化，结果 "comparable" 但仅在 PPL 和 3 个下游任务上验证。未测试：
  - 代码生成任务（HumanEval/MBPP）
  - 多语言文本
  - 长文档理解
  训练数据的 domain 和 volume 对 predictor 泛化能力的影响未充分讨论。

**W3** [warning] 2D Taxonomy 贡献度有限
- 具体位置：Section 3.7, Table 1
- 问题：Signal type × coupling scope 的 2D 分类（Table 1）作为组织框架有用，但新颖洞见有限——它本质上是对已有方法的 post-hoc 归类。Table 1 标注 "Empty cells represent unexplored combinations; their relative merit is an open question"，但论文未尝试填充这些空白（如 coupled BCE+MSE 或 per-token BCE），也未讨论为什么某些组合不可行或不有趣。如果 taxonomy 是贡献之一，需要更深入的分析。

**W4** [warning] Gumbel-Sigmoid relaxation 的贡献被低估/混淆
- 具体位置：Section 3.3, Table 3
- 问题：Table 3 的 C1 ablation 中，BCE achieves PPL 11.79 vs KL 11.79 (几乎相同)，但 BCE+Gumbel = 32.22 vs standard BCE = 需要从正文对比。关键问题是：论文将 KL 的优势归因于"output-distribution alignment"，但 KL 方法同时使用了 Gumbel-Sigmoid relaxation（§3.3），而 BCE baseline 使用 hard threshold。这引入了混淆变量——KL 的优势可能部分来自 Gumbel relaxation 本身（连续梯度流）而非 KL vs BCE 的信号差异。Table 4 的 "Relaxation, Divergence, and SPON" 行显示 Gumbel-Sigmoid 对 STE 有 PPL 15.77 → 11.79 的巨大改进，说明 relaxation method 本身是关键因素。论文应更清晰地 disentangle 这两个因素。

---

## 小问题（不影响接收）

- Section 3.5 公式 (7)：geometric penalty schedule 的 deadzone ε = 0.02 未充分 justify 为什么选择这个值
- Figure 2 右图：y 轴 "WikiText-2 PPL↓" 与左图 "Achieved Model-Level Sparsity (%)" 的对比信息密度可以提高——建议加入 Pareto frontier 标注
- Section 4.2 脚注 2："TEAL is deterministic; single-run evaluation suffices" ——但 KL predictor 使用了 Gumbel noise，single-run evaluation 是否足够？论文提到 3-seed evaluation（Table 2 报告 mean±std），但应在正文而非脚注中明确
- Appendix 编号从 A 到 U（21 个 appendix sections），信息量虽大但部分内容可精简（如 Appendix P "SPON Orthogonality" 仅 4 行）
- 部分符号不一致：正文用 $m_\ell$ 但部分地方用 $m^{(\ell)}$

---

## 遗漏的相关工作

**应引用但未引用：**
1. **SparseInfer** (Li et al., 2024, arXiv:2411.12692): Training-free prediction of activation sparsity for fast LLM inference。直接相关——另一种 training-free 的 sparsity predictor 方法，应在 Related Work 讨论作为对比。
2. **GRASP** (Group-Based Prediction of Activation Sparsity, DAC 2025): Group-based sparsity prediction method，在 prediction accuracy 上有创新。
3. **TurboSparse** (Song et al., 2024, arXiv:2406.05955): dReLU activation for SwiGLU models achieving ~90% sparsity。虽然是 activation engineering 而非 prediction，但与论文 "Activation Function Engineering" 小节（Section 2, p.3）直接相关，且同样关注 SwiGLU 模型的 sparsity。需确认是否已引用（从 PDF 难以完全确认 references 列表）。

**建议检查：**
4. Universal Properties of Activation Sparsity (2025, arXiv:2509.00454): 研究 activation sparsity 的跨模型通用属性，与本文 §4.4 mask pattern analysis 相关。

---

## 主要优势

1. **§3.6 梯度分析是真正的分析性贡献**：清晰展示 BCE gradient $\partial \mathcal{L}_{BCE}/\partial o_j = \sigma(s_j) - m_j^*$ 仅依赖 neuron $j$，而 KL gradient 通过 downstream Jacobian $\partial \mathcal{L}_{KL}/\partial o_j$ 耦合所有 neuron——这解释了为什么 KL 能发现 composition-aware mask patterns。这是本文最有价值的洞见。

2. **C1 target-swap ablation 设计精巧（§4.3, Table 3）**：用 KL-derived masks 训练 BCE predictor（C1），证明 mask pattern 质量本身可迁移（PPL within 0.79pp of KL），有力支撑了"KL 的优势在于 pattern discovery 而非仅 loss function"的论点。

3. **实验覆盖面宽（虽深度不足）**：主文和 Appendix 共覆盖了 allocation analysis（§4.5）、per-layer retention（Appendix E）、training stability（Appendix F）、mask pattern visualization（Appendix M）、cross-architecture（Appendix N-O）等多个维度，信息密度高。

4. **定位诚实**：论文自称 "primarily an empirical study"（Section 2, p.2）且始终保持这一定位，未虚增方法论贡献。Limitations 章节（虽简短）覆盖了三个核心局限。

5. **Predictor 设计高效**：75.9M 参数（< 1% base model），2.37M per layer，训练 1000 步（~45 min on single GPU）——实际部署门槛低。

---

## 总结判断

本文是一篇执行良好的实证研究，§3.6 梯度分析和 C1 ablation 是有价值的贡献。但三个核心问题阻碍了主会议接收：(1) 与 MaskLLM 的新颖性区分不充分——核心 recipe 相同，区别主要在 sparsity setting；(2) "dominant design dimension" claim 仅基于 BCE vs KL 二元对比，overclaimed；(3) 实验几乎完全依赖 LLaMA-3.1-8B，generalizability 证据不足。建议降级为 "KL outperforms BCE for contextual sparsity prediction in SwiGLU models"，补充 reverse KL/JSD 实验，并在主文中加入跨架构 C1 ablation。以当前形式适合 Findings 而非主会议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1926 · 2026-05-22T23:45:52.675686+00:00_

Reviewer 2 审稿已收到。记录关键发现，等待 Reviewer 1 返回后进入交叉分享。

初步注意到 Reviewer 2 的 N2 存在事实性错误：论文 Table 4 已包含 Reverse KL (9.26±0.07 / 12.80) 和 JSD (8.90±0.02 / 12.54) 的实验结果，Reviewer 2 声称"未测试"不成立。将在交叉分享阶段让 Reviewer 1 核实。

等待 Reviewer 1 审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 160

## Round 160

2 recorded events


### User

_source line 1927 · 2026-05-22T23:45:55.167067+00:00_

[Reviewer 2 审稿结果]:
审稿完成。核心结论：

- **Overall: 3.0/5 (Findings)**
- 3 个 Critical 问题：(1) 与 MaskLLM 的新颖性区分不充分（核心 KL+Gumbel recipe 相同）；(2) "dominant design dimension" claim overclaimed（仅 BCE vs KL 二元对比，未测试 reverse KL/JSD 等）；(3) 实验几乎全依赖 LLaMA-3.1-8B，generalizability 证据不足
- 主要优势：§3.6 梯度分析是真正的分析性贡献，C1 target-swap ablation 设计精巧，定位诚实
- 4 个 Should-Fix：无 wall-clock speedup、训练数据有限、2D taxonomy 贡献度有限、Gumbel relaxation 与 KL 的贡献未充分 disentangle

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1928 · 2026-05-22T23:46:03.338335+00:00_

Reviewer 2 报告已收到（3.0/5 Findings）。等待 Reviewer 1 报告，收齐后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 161

## Round 161

6 recorded events


### User

_source line 1929 · 2026-05-22T23:46:51.811697+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿报告：方法严谨性与实验设计

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May 2026)
**审查侧重**: 方法严谨性 + 实验设计

---

## Summary

本文用 forward KL divergence + Gumbel-Sigmoid 松弛训练 SwiGLU FFN 稀疏预测器，替代传统 BCE per-neuron 独立目标。在 LLaMA-3.1-8B 上 30%/50% 稀疏度下相比 TEAL 和 BCE baseline 取得显著 PPL 优势，并通过 C1 target-swap ablation 和 per-layer KL 控制实验分解了信号类型（output-distribution vs. intermediate）和耦合范围对性能的贡献。论文定位为经验研究而非提出新架构，分析深度值得肯定，但几项关键分析存在未解决的 confound，知识密集型任务系统性退步限制了实用性。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 核心 KL vs BCE 对比可靠（效应量大、多 seed），但 per-layer 分解存在 train-inference mismatch confound，C1 ablation 有残余 confound |
| Excitement | 2.5/5 | 无新方法/算法/架构（作者自述），KL+Gumbel-Sigmoid 均为已有技术；无 wall-clock 加速；核心发现（KL 优于 BCE）有价值但属预期范围 |
| Reproducibility | 4.0/5 | 超参、架构、硬件细节完整，训练/评估协议清晰，但无代码/数据释放声明 |
| Reviewer Confidence | 4/5 | 熟悉稀疏性预测、KD、SwiGLU 相关文献 |
| **Overall Assessment** | **3.0** | **Findings 级别**：经验发现有价值，分析深度突出，但 per-layer 分解的 confound 削弱关键贡献，缺乏实际加速，知识任务系统性退步限制影响力 |

---

## Strengths

**S1. 核心对比可靠且效应量大。**
KL vs BCE 的 PPL 差距在 30%（8.81 vs 11.25）和 50%（11.84 vs 28.13）均超过 25%，3-seed 方差极低（KL σ=0.02 at 30%），跨架构（Mistral-7B -17.3%）一致。这不是边界效应，而是实质性差异。

**S2. C1 target-swap ablation 是创造性的实验设计。**
将 KL 发现的 mask 作为 BCE 训练目标（Table 3），分离 mask 质量 vs. 训练动态的贡献。s123/s456 的匹配实验（gap ≤0.03pp at 30%）令人信服。这一分析设计在稀疏性预测文献中是新颖的。

**S3. 消融覆盖广泛且控制严格。**
Table 4 系统比较 5 种 loss（forward KL, reverse KL, JSD, BCE, MSE）× 2 种松弛（Gumbel, STE），MSE baseline 除 loss 外完全一致（Appendix G 详述）。附录提供 d_b 敏感性（Appendix B）、温度 schedule（B.1）、训练收敛（B.2）、补偿网络冗余（J），形成完整的 hyperparameter robustness 图景。

**S4. 论文对自身局限性的透明度高于平均水平。**
明确标注 per-layer 分解为 "upper bound"（§4.5），承认 C1 的 s42 oracle 来自早期 checkpoint（Table 3 脚注），Limitations 逐条列出 seq length、batched inference、知识任务退步等。这种诚实度值得肯定。

**S5. 2D taxonomy（Table 1）提供有用的组织框架。**
correction granularity × training signal coupling 的分类法清晰定位了本文贡献，尽管框架本身较简单。

---

## Must-Fix 问题（影响接收决定）

**N1 [Critical] Per-layer KL 分解存在根本性 confound，定量结论不可靠**

- **具体位置**: §4.5, Table 4（ablation rows: per-layer KL K=1, K=4）, Abstract line 5-6, Conclusion line 1
- **问题**: 
  (a) K=1 控制实验在训练时仅 mask 1/32 层，推理时 mask 全部 32 层，存在 32× 的 train-inference mismatch。论文承认这是 "upper bound"，但 Abstract 和 Conclusion 仍将 "signal type accounts for the majority of the PPL gap" 作为核心贡献之一呈现，未充分传达 upper bound 的资格限定。
  (b) K=4 控制实验出现反常结果：50% 稀疏度下 K=4 (PPL 44.23) **显著差于** K=1 (PPL 34.85)，差距达 27%。更多训练上下文（4 层 vs 1 层 masked）反而导致更差性能，这与 "K 越大越接近 E2E" 的直觉相矛盾。论文仅描述现象（"coupling scope dominates at high sparsity, reversing the 30% pattern"），但未提供机制解释——为什么在 50% 时同时 mask 4 层会比 mask 1 层更差？
  (c) K=4 在 30% 时 MMLU 超过 E2E（42.7 vs 40.7），论文归因于 allocation matching（Appendix S 注释），但这意味着 K=4 与 E2E 的差异中混入了 allocation 效应，进一步污染了 coupling scope 的估计。
  (d) 缺少 K=8, K=16 等中间值。仅两个数据点（K=1, K=4）无法拟合 coupling scope 的单调趋势，更无法支撑 "29-97% on downstream tasks" 的精确分解数字。
- **为什么影响接收**: 信号类型 vs 耦合范围的分解是论文三大贡献之一（Introduction bullet 1）。如果这一分解不可靠，论文的分析深度主张大幅削弱。
- **建议修改方向**: (1) 在 Abstract/Conclusion 中明确标注 "upper bound" 限定，不应呈现为确定性结论；(2) 增加 K=8/K=16 实验或承认仅有两个数据点不足以做定量分解；(3) 对 50% K=4 < K=1 的反常提供假设性解释（如 gradient interference、sparsity compounding）。

**N2 [Critical] 知识密集型任务系统性退步缺乏机制分析**

- **具体位置**: Table 2（MMLU: KL 40.7 vs TEAL 45.86 at 30%），Table 14/Appendix K（Qwen-14B GSM8K -20pp），Limitations paragraph 2
- **问题**: KL 在所有测试规模和架构上均系统性地低于 TEAL 的 MMLU/GSM8K 性能：
  - 8B 30%: MMLU -5.2pp（40.7 vs 45.86）
  - 8B 30% global: MMLU -10.2pp（35.7 vs 45.86），σ=9.5
  - 14B 30% uniform: MMLU -2.8pp（63.55 vs 66.34），GSM8K -20.1pp（32.0 vs 52.1）
  
  论文推测 "distribution-matching objectives systematically sacrifice reasoning-critical pathways"，但这仅是事后叙事，无实验支撑。§4.4 的 per-layer sparsity 分析（L14-L18 protection valley）提供了一个数据点（Remove valley: MMLU +3.4pp, Table 20），但没有回答根本问题：为什么 KL 的 output-distribution 目标会学到一个牺牲知识路径的 allocation pattern？是 WikiText-103 训练数据的偏差？是 forward KL 的固有特性？还是 Gumbel-Sigmoid 的采样偏差？
- **为什么影响接收**: MMLU 和 GSM8K 是 LLM 评估的核心指标。如果方法在这些指标上系统性退步，实际应用场景将严重受限。仅报告退步而不提供分析，对于定位为 "characterize how the training objective shapes sparsity prediction quality" 的论文来说是一个显著空白。
- **建议修改方向**: (1) 分析 KL 和 TEAL 在知识密集型层（Meng et al., 2022 的知识神经元）上的 mask 差异；(2) 用不同训练数据（如包含更多 reasoning 内容的数据）测试退步是否缓解；(3) 至少在 Discussion 中提供更具体的假设和未来验证路径。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1 [Warning] C1 ablation 残余 confound 未完全控制**

- **具体位置**: §4.4 "Soft-vs-Hard Confound" 段落, Table 3, Appendix P
- **问题**: C1 同时改变了两个变量：(a) 训练目标（KL mask → BCE mask），(b) mask 表示（soft Gumbel → hard binary）。论文用 BCE+Gumbel（PPL 32.22）vs standard BCE（27.97）论证 softness 不解释 KL 优势，但这一对比使用的是 magnitude-based targets，不能直接推广到 KL-derived targets。此外，oracle mask 提取过程（从连续 Gumbel 分数到二值化 logits > 0）可能丢失排序信息，而这些信息在 TEAL global top-k 排序中可能有用。
- **建议**: 明确讨论 oracle 提取时信息损失的可能性，或增加一个使用连续 KL 分数（非二值化）训练 BCE 的对比实验。

**W2 [Warning] 无 wall-clock 加速，实际影响受限**

- **具体位置**: Appendix A（Table 5: +6.4% overhead），Limitations
- **问题**: Predictor 增加 6.4% 推理延迟，无稀疏内核支持。所有 PPL 改进在实际部署中不带来速度收益。论文定位为 empirical study 避开了这一点，但这意味着论文的直接实际价值有限——仅当未来有稀疏内核适配时才有价值。
- **建议**: 至少在 Discussion 中讨论稀疏内核的可行性估算（如 Triton block-sparse 能否支持 unstructured element-wise masks？如果不能，需要 structured sparsity 适配，这又是一个未验证的步骤）。

**W3 [Warning] 评估覆盖度存在关键空白**

- **具体位置**: §4.1 Evaluation 段落, Limitations
- **问题**: 
  (a) 所有下游任务均为 classification/multiple-choice 格式，无生成任务评估（MT-Bench, AlpacaEval 等）。稀疏预测对自回归生成质量的影响可能与 classification 不同。
  (b) 序列长度固定 2048。现代 LLM 应用场景常用 8K-128K 上下文。稀疏 pattern 可能随序列长度变化（长序列中 attention pattern 变化可能影响 FFN 稀疏性）。
  (c) Batched inference 未评估。实际部署中多序列需取 mask 交集，可能显著降低有效稀疏度。
- **建议**: 补充至少一项生成任务评估，或明确讨论 classification-only 评估的局限性。

**W4 [Warning] 高方差指标的统计可靠性不足**

- **具体位置**: Table 2（ARC-c σ=3.6 at 30% global），Appendix R（BoolQ σ=11.5）
- **问题**: ARC-c σ=3.6pp 意味着 95% CI 宽度约为 ±8.9pp（t 分布, df=2），BoolQ σ=11.5pp 更甚。在 3 seed 下，这些指标的均值差异基本不可解释。Table 4 (ablation) 多行仅有 s42 单 seed 数据（Per-layer KL K=1 50%: 34.85, BCE variants 50%: 27.97/32.22/38.02/60.54），无法评估可靠性。
- **建议**: (1) 在正文中对高方差指标加注 "differences not statistically significant"；(2) ablation table 关键行补充 3-seed 数据，至少 forward KL + Gumbel 和 BCE 两行。

**W5 [Warning] Geometric penalty schedule 在 30% 目标下偏差较大**

- **具体位置**: Appendix C（Table 9: 30% target → 28.5% actual, 5% deviation），§3.5 Eq. 7
- **问题**: ε=0.02 的 deadzone 设计意味着实际稀疏度 28.5%（retention 71.5%）距目标 30%（retention 70.0%）的偏差 |71.5%-70%|=1.5pp < ε=2pp，落入 deadzone 内，λ 不再增长。因此 30% 目标永远无法精确达到——这是 schedule 设计的固有限制而非收敛不足。论文在 Appendix C 处理了 matched sparsity comparison（TEAL at 28.5% → PPL 10.30 vs KL 8.96），但 main text Table 2 标注 "30%" 可能误导读者。
- **建议**: Table 2 注释应更醒目地标注实际稀疏度（目前 ‡ 脚注存在但不够显眼）。

---

## 小问题（不影响接收）

- Table 2 中 BCE 30% 使用 global allocation（脚注 †），但未提供 BCE 30% uniform 的对比，使读者无法在同一 allocation 策略下比较 BCE 与 KL。建议补充或说明省略原因。
- §3.5 称 "geometric penalty schedule"，实际实现是 augmented penalty method with geometric λ update rule。术语不影响理解但不够精确。
- Abstract 第 3 句 "reduces perplexity by 14.5% over TEAL at matched sparsity" 的 "matched sparsity" 指 28.5% 而非名义 30%，这一资格限定在 abstract 中容易被忽略。
- Appendix G（MSE baseline）提到 seed 123 出现 catastrophic failure（PPL=15,789），但 MSE 的 3-seed 报告仍包含了可能在该 seed 上偏好的结果（仅排除了灾难 seed 后用剩余两个有效 seed）。MSE 3-seed mean 的计算方式应澄清。
- 无代码/数据/模型释放声明。对于定位为 empirical study 的论文，reproducibility 需要代码可用。

---

## Questions for Authors

**Q1.** Per-layer KL K=4 在 50% 时为何比 K=1 差？是否有 gradient interference 或 optimization landscape 方面的解释？增加 K 是否单调恶化，还是存在 sweet spot？

**Q2.** 知识密集型退步是否与 WikiText-103 训练数据有关？如果用包含 Wikipedia + 数学/代码数据的混合语料训练，MMLU/GSM8K 退步是否缓解？

**Q3.** C1 oracle 提取时使用 logits > 0 二值化。是否尝试过保留连续分数（如直接用 KL predictor 输出作为 BCE 回归目标）？信息损失是否可量化？

**Q4.** STE 在 30% 仅达到 20.8% effective sparsity（§4.5 STE Failure 段落）。是否调整过 STE 的 learning rate 或 gradient scaling？如果 STE 达到了目标稀疏度，其 PPL 如何？

**Q5.** Table 2 中 MSE 50% 报告 PPL=229.26（仅 s42），Appendix G 显示 s123 catastrophic（PPL=15,789）。MSE 30% 的 3-seed mean 18.52±1.68 是否包含了所有 3 个 seed，还是也排除了部分失败 seed？

---

## Missing References

- Meng et al., 2022 "Locating and Editing Factual Associations in GPT" — 与知识密集型退步的讨论直接相关，可用于分析 KL masks 在知识存储层的行为。
- Li et al., 2023 "Inference with Reference: Lossless Acceleration of Large Language Models" — 与 contextual sparsity prediction 路线相关但未讨论的加速方法。
- 论文已引用的 MaskLLM (Fang et al., 2024) 仅在 Related Work 中讨论，未做实验对比。虽然 static N:M vs contextual sparsity 确有差异，但 KL+Gumbel 的共享方法论使得读者自然期待某种程度的对比或讨论。

---

## Overall Assessment

**Overall: 3.0 (Findings)**

核心发现（KL 显著优于 BCE 用于稀疏预测训练）可靠且有价值，target-swap ablation 设计巧妙。但论文存在以下主要问题：(1) per-layer 分解是三大贡献之一，却因 train-inference mismatch confound 和 K=4 反常结果而不可靠；(2) 知识密集型任务系统性退步缺乏分析深度；(3) 无实际加速。论文分析详尽、写作透明，适合 Findings track；Conference 接收需解决 per-layer 分解的 confound 并提供知识退步的机制分析。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1930 · 2026-05-22T23:47:33.364718+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告（新颖性与完整性）\n\n**Overall**: 3.0 / 5 — Findings\n\n### Must-Fix 问题\n\n**N1** [critical] 核心贡献与 MaskLLM 的新颖性区分不充分\n- MaskLLM (Fang et al., 2024, NeurIPS 2024 Spotlight) 已提出 KL divergence + Gumbel relaxation 训练可学习 sparsity masks 的范式。本文声称的区别是：(a) contextual vs. static masks, (b) activation sparsity vs. N:M weight sparsity, (c) cross-layer coupling analysis。但 (a) 和 (b) 属于 sparsity setting 的差异而非训练方法论的创新——核心 recipe（KL on output distributions + differentiable mask sampling）完全一致。论文 Section 2 仅用一句话提到 MaskLLM。\n\n**N2** [critical] \"Dominant design dimension\" claim overclaimed\n- 该 claim 仅基于两种 signal type 的对比：BCE vs forward KL。论文未测试 Reverse KL、JSD、MSE on logits/hidden states、cosine similarity 等。在仅比较两种方法的情况下声称 \"dominant\"，逻辑上不成立。此外 Table 3 中 BCE+Gumbel (32.22) vs standard BCE (27.97) 说明 Gumbel relaxation 本身也是重要因素。\n\n**N3** [critical] 实验规模单一，削弱 generalizability claim\n- 核心实验全部基于 LLaMA-3.1-8B；跨架构实验仅在 Appendix。Qwen-2.5-14B 无 C1 ablation 或 gradient SNR 分析。无 70B+ 模型实验。\n\n### Should-Fix 问题\n\n**W1** [warning] 无 wall-clock speedup 结果\n**W2** [warning] 训练数据过于有限（WikiText-103, 1000 步）\n**W3** [warning] 2D Taxonomy 贡献度有限——post-hoc 归类，未填充空白组合\n**W4** [warning] Gumbel-Sigmoid relaxation 的贡献被低估/混淆——KL 方法同时使用 Gumbel，而 BCE baseline 使用 hard threshold，引入混淆变量\n\n### 遗漏的相关工作\n1. SparseInfer (Li et al., 2024)\n2. GRASP (DAC 2025)\n3. TurboSparse (Song et al., 2024)\n4. Universal Properties of Activation Sparsity (2025)\n\n### 主要优势\n1. §3.6 梯度分析是真正的分析性贡献\n2. C1 target-swap ablation 设计精巧\n3. 实验覆盖面宽\n4. 定位诚实\n5. Predictor 设计高效\n\n---\n\n请对上述每个 N1-N3、W1-W4 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告（新颖性与完整性）\n\n**Overall**: 3.0 / 5 — Findings\n\n### Must-Fix 问题\n\n**N1** [critical] 核心贡献与 MaskLLM 的新颖性区分不充分\n- MaskLLM (Fang et al., 2024, NeurIPS 2024 Spotlight) 已提出 KL divergence + Gumbel relaxation 训练可学习 sparsity masks 的范式。本文声称的区别是：(a) contextual vs. static masks, (b) activation sparsity vs. N:M weight sparsity, (c) cross-layer coupling analysis。但 (a) 和 (b) 属于 sparsity setting 的差异而非训练方法论的创新——核心 recipe（KL on output distributions + differentiable mask sampling）完全一致。论文 Section 2 仅用一句话提到 MaskLLM。\n\n**N2** [critical] \"Dominant design dimension\" claim overclaimed\n- 该 claim 仅基于两种 signal type 的对比：BCE vs forward KL。论文未测试 Reverse KL、JSD、MSE on logits/hidden states、cosine similarity 等。在仅比较两种方法的情况下声称 \"dominant\"，逻辑上不成立。此外 Table 3 中 BCE+Gumbel (32.22) vs standard BCE (27.97) 说明 Gumbel relaxation 本身也是重要因素。\n\n**N3** [critical] 实验规模单一，削弱 generalizability claim\n- 核心实验全部基于 LLaMA-3.1-8B；跨架构实验仅在 Appendix。Qwen-2.5-14B 无 C1 ablation 或 gradient SNR 分析。无 70B+ 模型实验。\n\n### Should-Fix 问题\n\n**W1** [warning] 无 wall-clock speedup 结果\n**W2** [warning] 训练数据过于有限（WikiText-103, 1000 步）\n**W3** [warning] 2D Taxonomy 贡献度有限——post-hoc 归类，未填充空白组合\n**W4** [warning] Gumbel-Sigmoid relaxation 的贡献被低估/混淆——KL 方法同时使用 Gumbel，而 BCE baseline 使用 hard threshold，引入混淆变量\n\n### 遗漏的相关工作\n1. SparseInfer (Li et al., 2024)\n2. GRASP (DAC 2025)\n3. TurboSparse (Song et al., 2024)\n4. Universal Properties of Activation Sparsity (2025)\n\n### 主要优势\n1. §3.6 梯度分析是真正的分析性贡献\n2. C1 target-swap ablation 设计精巧\n3. 实验覆盖面宽\n4. 定位诚实\n5. Predictor 设计高效\n\n---\n\n请对上述每个 N1-N3、W1-W4 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1931 · 2026-05-22T23:47:59.140926+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25776
}
```

</details>

---


### Tool call

_source line 1932 · 2026-05-22T23:47:59.342068+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告（方法严谨性与实验设计）\n\n**Overall**: 3.0 / 5 — Findings\n\n### Must-Fix 问题\n\n**N1 [Critical] Per-layer KL 分解存在根本性 confound，定量结论不可靠**\n- K=1 训练时仅 mask 1/32 层，推理时 mask 全部 32 层，32× train-inference mismatch。Abstract/Conclusion 仍将 \"signal type accounts for the majority of the PPL gap\" 作为核心贡献呈现，未充分传达 upper bound 资格限定。\n- K=4 在 50% 下比 K=1 差（44.23 vs 34.85），与 \"K 越大越接近 E2E\" 的直觉矛盾，论文未提供机制解释。\n- K=4 在 30% MMLU 超过 E2E（42.7 vs 40.7），混入 allocation 效应。\n- 仅两个数据点（K=1, K=4）无法支撑 \"29-97% on downstream tasks\" 的精确分解。\n\n**N2 [Critical] 知识密集型任务系统性退步缺乏机制分析**\n- KL 在所有测试规模和架构上均系统性地低于 TEAL 的 MMLU/GSM8K：8B -5.2pp MMLU, 14B -20pp GSM8K。\n- 论文推测 \"distribution-matching objectives systematically sacrifice reasoning-critical pathways\" 仅是事后叙事，无实验支撑。\n- §4.4 Remove valley (MMLU +3.4pp) 是一个数据点但未回答根本问题：为什么 KL 会学到牺牲知识路径的 allocation pattern？\n\n### Should-Fix 问题\n\n**W1 [Warning] C1 ablation 残余 confound 未完全控制**\n- C1 同时改变训练目标和 mask 表示（soft → hard）。BCE+Gumbel (32.22) vs standard BCE (27.97) 使用 magnitude-based targets，不能直接推广到 KL-derived targets。Oracle mask 提取（logits > 0 二值化）可能丢失排序信息。\n\n**W2 [Warning] 无 wall-clock 加速**\n- Predictor 增加 6.4% 推理延迟，无稀疏内核支持。\n\n**W3 [Warning] 评估覆盖度存在关键空白**\n- 无生成任务评估（MT-Bench, AlpacaEval）；序列长度固定 2048；batched inference 未评估。\n\n**W4 [Warning] 高方差指标的统计可靠性不足**\n- ARC-c σ=3.6pp 在 3 seed 下 95% CI 约 ±8.9pp；BoolQ σ=11.5pp；Table 4 多行仅 s42 单 seed。\n\n**W5 [Warning] Geometric penalty schedule 在 30% 目标下偏差较大**\n- ε=0.02 deadzone 导致 30% 目标永远无法精确达到（28.5% actual）；main text Table 2 标注 \"30%\" 可能误导。\n\n### Questions\nQ1. K=4 50% 为何比 K=1 差？是否有 gradient interference 解释？\nQ2. 知识退步是否与 WikiText-103 训练数据有关？\nQ3. C1 oracle 提取二值化是否尝试过保留连续分数？\nQ4. STE 在 30% 仅 20.8% sparsity，是否调整过 lr/gradient scaling？\nQ5. MSE 30% 3-seed mean 是否包含所有 3 个 seed？\n\n### Missing References\n- Meng et al., 2022 \"Locating and Editing Factual Associations in GPT\"\n- Li et al., 2023 \"Inference with Reference\"\n- MaskLLM 无实验对比\n\n---\n\n请对上述每个 N1-N2、W1-W5 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告（方法严谨性与实验设计）\n\n**Overall**: 3.0 / 5 — Findings\n\n### Must-Fix 问题\n\n**N1 [Critical] Per-layer KL 分解存在根本性 confound，定量结论不可靠**\n- K=1 训练时仅 mask 1/32 层，推理时 mask 全部 32 层，32× train-inference mismatch。Abstract/Conclusion 仍将 \"signal type accounts for the majority of the PPL gap\" 作为核心贡献呈现，未充分传达 upper bound 资格限定。\n- K=4 在 50% 下比 K=1 差（44.23 vs 34.85），与 \"K 越大越接近 E2E\" 的直觉矛盾，论文未提供机制解释。\n- K=4 在 30% MMLU 超过 E2E（42.7 vs 40.7），混入 allocation 效应。\n- 仅两个数据点（K=1, K=4）无法支撑 \"29-97% on downstream tasks\" 的精确分解。\n\n**N2 [Critical] 知识密集型任务系统性退步缺乏机制分析**\n- KL 在所有测试规模和架构上均系统性地低于 TEAL 的 MMLU/GSM8K：8B -5.2pp MMLU, 14B -20pp GSM8K。\n- 论文推测 \"distribution-matching objectives systematically sacrifice reasoning-critical pathways\" 仅是事后叙事，无实验支撑。\n- §4.4 Remove valley (MMLU +3.4pp) 是一个数据点但未回答根本问题：为什么 KL 会学到牺牲知识路径的 allocation pattern？\n\n### Should-Fix 问题\n\n**W1 [Warning] C1 ablation 残余 confound 未完全控制**\n- C1 同时改变训练目标和 mask 表示（soft → hard）。BCE+Gumbel (32.22) vs standard BCE (27.97) 使用 magnitude-based targets，不能直接推广到 KL-derived targets。Oracle mask 提取（logits > 0 二值化）可能丢失排序信息。\n\n**W2 [Warning] 无 wall-clock 加速**\n- Predictor 增加 6.4% 推理延迟，无稀疏内核支持。\n\n**W3 [Warning] 评估覆盖度存在关键空白**\n- 无生成任务评估（MT-Bench, AlpacaEval）；序列长度固定 2048；batched inference 未评估。\n\n**W4 [Warning] 高方差指标的统计可靠性不足**\n- ARC-c σ=3.6pp 在 3 seed 下 95% CI 约 ±8.9pp；BoolQ σ=11.5pp；Table 4 多行仅 s42 单 seed。\n\n**W5 [Warning] Geometric penalty schedule 在 30% 目标下偏差较大**\n- ε=0.02 deadzone 导致 30% 目标永远无法精确达到（28.5% actual）；main text Table 2 标注 \"30%\" 可能误导。\n\n### Questions\nQ1. K=4 50% 为何比 K=1 差？是否有 gradient interference 解释？\nQ2. 知识退步是否与 WikiText-103 训练数据有关？\nQ3. C1 oracle 提取二值化是否尝试过保留连续分数？\nQ4. STE 在 30% 仅 20.8% sparsity，是否调整过 lr/gradient scaling？\nQ5. MSE 30% 3-seed mean 是否包含所有 3 个 seed？\n\n### Missing References\n- Meng et al., 2022 \"Locating and Editing Factual Associations in GPT\"\n- Li et al., 2023 \"Inference with Reference\"\n- MaskLLM 无实验对比\n\n---\n\n请对上述每个 N1-N2、W1-W5 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1933 · 2026-05-22T23:48:00.702473+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1360
}
```

</details>

---


### Assistant

_source line 1934 · 2026-05-22T23:48:03.956188+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 162

## Round 162

2 recorded events


### User

_source line 1935 · 2026-05-22T23:48:06.465712+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.0（Findings 级别）**。

主要问题：
1. **Per-layer KL 分解的 confound**（N1 Critical）：K=1 有 32× train-inference mismatch，K=4 在 50% 时反常地差于 K=1（44.23 vs 34.85），仅两个 K 值不足以支撑定量分解。
2. **知识任务系统性退步无机制解释**（N2 Critical）：MMLU/GSM8K 在所有规模/架构上均退步（8B -5.2pp MMLU, 14B -20pp GSM8K），仅有事后推测。

核心优势：KL vs BCE 的效应量大且稳健（PPL 差 2-2.4×），C1 target-swap ablation 设计巧妙，消融覆盖广泛，论文对局限性高度透明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1936 · 2026-05-22T23:48:10.978353+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 163

## Round 163

2 recorded events


### User

_source line 1937 · 2026-05-22T23:49:44.369288+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 的逐条回应

---

### N1: 核心贡献与 MaskLLM 的新颖性区分不充分

**[REBUT]** R2 称 "论文 Section 2 仅用一句话提到 MaskLLM"——这与原文不符。Section 2 (Related Work) 用 **4 句话**（related_work.tex lines 19-23）详细讨论 MaskLLM，明确列出三个维度的差异：(a) static N:M vs per-token contextual masks, (b) 无 cross-layer allocation interaction vs TEAL global top-k coordination, (c) weight masks input-independent vs activation masks 需 distribution shift robustness。

更重要的是，R2 低估了 contextual vs static 的差异。MaskLLM 学习 **固定的** N:M weight masks（每个 mask 是 Gumbel-Softmax 采样的 static pattern），不需要泛化到未见输入。本文的 predictor 必须从 $\mathbf{x}^{(\ell)}$ **实时预测** per-token masks 并在 OOD 数据上保持性能（Appendix D, Table 10: C4 下游 Δ≤1.1pp）。这不仅是 "sparsity setting 的差异"，而是根本不同的学习问题——one is parameter optimization, the other is function approximation。

但我同意 R2 的一个隐含观点：论文应在 Introduction 中更早、更清晰地定位与 MaskLLM 的关系，而不是仅在 Related Work 中讨论。这是 framing 问题，不是 novelty 缺失。

---

### N2: "Dominant design dimension" claim overclaimed

**[REBUT]** R2 声称 "论文未测试 Reverse KL、JSD、MSE"——这与原文 **直接矛盾**。Table 4 (§4.5 Ablation Studies) 明确对比了 **5 种 loss function**：

| Loss | 30% PPL | 50% PPL |
|------|---------|---------|
| Forward KL + Gumbel | **8.81±0.02** | **11.79** |
| JSD + Gumbel | 8.90±0.02 | 12.54 |
| Reverse KL + Gumbel | 9.26±0.07 | 12.80 |
| Per-layer MSE | 18.52±1.68 | 229.26 |
| BCE | 15.71 | 27.97 |

Forward KL、Reverse KL、JSD（对称）、MSE（intermediate activations）、BCE（decomposed）——涵盖了 R2 要求的所有 divergence measure 类型。R2 的 "仅比较两种方法" 断言是事实性错误。

关于 Gumbel confound：论文 §4.5 "STE Failure and Loss-Relaxation Interaction" 已精确量化——loss effect (ΔPPL=20.4) 是 relaxation effect (ΔPPL=3.98) 的 **5.1×**（experiments.tex line 168）。此外，MSE baseline 使用 **完全相同的** Gumbel-Sigmoid 松弛（Appendix G, appendix.tex line 239），因此 KL vs MSE 的对比完全控制了 relaxation 变量。

不过，我在自己的审稿中指出（R1-N1），"dominant" 这一 claim 的定量基础（per-layer 分解的 signal type vs coupling scope 百分比）确实因 train-inference mismatch confound 而不够可靠。但 R2 给出的理由是错误的——不是因为缺少对比，而是因为分解方法学的 confound。

---

### N3: 实验规模单一，削弱 generalizability claim

**[AGREE]** R2 的核心观点成立：跨架构证据是 preliminary 的。Mistral-7B 和 Qwen-14B 仅有 main results，无 C1 ablation、per-layer 分解或 SNR 分析。我在 R1 审稿中也指出了类似问题（R1-W3 评估覆盖度）。

不过，两点补充：
1. 论文明确自称 "primarily an empirical study"（Introduction, introduction.tex line 18），Conclusion 也标注 "evaluation bounded at 7-14B"。作者对这一局限是诚实的。
2. 要求 70B+ 实验需考虑计算成本——论文使用单卡 RTX PRO 6000（96GB）训练，70B+ 模型的 predictor 训练可能超出合理的审稿修改范围。但至少应在 Discussion 中讨论 scaling 预期。

这一不足是 **影响评分但非一票否决** 的问题——将 generalization claims 限定在已验证的 7-14B 范围内即可。升级到 critical 级别过于严格。

---

### W1: 无 wall-clock speedup 结果

**[AGREE]** 与我的审稿意见 R1-W2 一致。Predictor 增加 6.4% latency overhead（Appendix A, Table 5），无稀疏内核支持。论文透明但影响力受限。

---

### W2: 训练数据过于有限（WikiText-103, 1000 步）

**[REBUT]** R2 未充分考虑论文已提供的 OOD 证据：
- Appendix D (Table 8): C4 validation PPL 保持 KL 优势（50%: 18.40 vs TEAL 38.75，与 WikiText-2 的 50% advantage 一致）
- Appendix D (Table 10): 用 C4 text 生成 mask（OOD calibration），6 个下游任务 Δ≤1.1pp
- Appendix B.2 (Table 7): 训练在 600 步即收敛 95%，1000 步提供保守余量

WikiText-103 作为训练数据确实是限制（Limitations 段落 3 已承认，特别提到 cross-seed variance 在 C4 上升至 CV=6.3%），但 R2 的措辞 "过于有限" 忽略了已有的泛化验证。这是一个已被适当讨论的 limitation，不是 experimental oversight。

---

### W3: 2D Taxonomy 贡献度有限

**[AGREE]** Taxonomy（Table 1）是 post-hoc 组织框架而非实验发现。论文也未声称它是 key contribution——Introduction 的 4 个 bullet points 未包含 taxonomy。这是一个 minor organizational contribution，R2 的评价合理。

---

### W4: Gumbel-Sigmoid relaxation 的贡献被低估/混淆

**[REBUT]** 如 N2 回应所述，论文已显式控制了这一 confound：

1. **BCE vs BCE+Gumbel**（Table 4）：BCE 27.97 → BCE+Gumbel 32.22，Gumbel 在 BCE 上反而 **恶化** 性能。这排除了 "Gumbel 本身解释 KL 优势" 的假说。
2. **Forward KL+Gumbel vs Forward KL+STE**（Table 4）：11.79 vs 15.77，relaxation effect = ΔPPL 3.98。
3. **Loss effect vs relaxation effect**：ΔPPL 20.4 vs 3.98，loss 是 relaxation 的 **5.1×**（§4.5）。
4. **MSE 使用相同 Gumbel**（Appendix G, appendix.tex line 239）：KL vs MSE 完全控制了 relaxation 变量。

R2 的 "引入混淆变量" 判断未考虑论文已提供的消融证据。这一 confound 被充分控制。

---

### R2 遗漏的相关工作评论

R2 列出 4 篇遗漏引用，其中两篇论文 **已被引用**：
- **SparseInfer** (Shin et al., 2025)：Section 2 line 4 已引用（related_work.tex: "SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs"）
- **TurboSparse** (Song et al., 2024)：Section 2 line 31 已引用（related_work.tex: "TurboSparse~\cite{song2024turbosparse} and ProSparse~\cite{song2025prosparse}"）

R2 可能未仔细阅读 Related Work section。GRASP (DAC 2025) 和 "Universal Properties" (2025) 可补充但非 critical omission。

---

### 总结

R2 的 N2 和 W4 基于 **事实性错误**（遗漏 Table 4 的 5-loss 对比和 §4.5 的 confound 量化），应降级或撤回。N1 的 MaskLLM 讨论量也被低估（实际 4 句而非 1 句），但 Introduction framing 可改善。N3 和 W1 有效但严重性适中。W2 忽略了已有的 OOD 验证。W3 合理。

R2 遗漏相关工作列表中两篇已被论文引用，反映了阅读不够仔细，可能影响其他判断的可靠性。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1938 · 2026-05-22T23:49:48.880519+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 164

## Round 164

2 recorded events


### User

_source line 1939 · 2026-05-22T23:50:02.921369+00:00_

[Reviewer 1 审稿结果]:
已向 Director 提交对 Reviewer 2 的逐条回应。主要结论：

- **N2、W4**：基于事实性错误（R2 遗漏了 Table 4 的 5-loss 对比和 §4.5 的 confound 量化），应降级或撤回
- **N1**：MaskLLM 讨论量被 R2 低估（4 句非 1 句），但 Introduction framing 确可改善
- **N3、W1**：有效但严重性适中
- **W2**：忽略了论文已有的 OOD 验证
- **W3**：合理

另外指出 R2 遗漏相关工作列表中 SparseInfer 和 TurboSparse 已被论文引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1940 · 2026-05-22T23:50:07.328533+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 165

## Round 165

8 recorded events


### User

_source line 1941 · 2026-05-22T23:51:02.670927+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix 问题

**[AGREE] R1-N1: Per-layer KL 分解的 confound 问题**

R1 的核心批评成立。具体同意以下几点：

1. **32× train-inference mismatch 是真实 confound**：K=1 训练时仅 mask 1/32 层，模型几乎在 dense 状态下运行，optimizer 面对的 loss landscape 远比 E2E（32 层全 mask）平滑。K=1 的好表现可能反映的是"训练容易"而非"signal type 本身足够"——论文未控制这一混淆变量。

2. **K=4 在 50% 下比 K=1 差（PPL 44.23 vs 34.85）确实缺乏机制解释**：论文 §4.5 (p.8) 仅说 "coupling scope dominates at high sparsity, reversing the 30% pattern"，但未解释为什么增加 coupling（K=4）反而恶化。一个合理假设是 4 层同时 masking 在 50% sparsity 下引入过大扰动导致 gradient interference，但这需要实验验证（如 gradient norm/SNR 随 K 的变化曲线）。

3. **"29-97% on downstream tasks" 的精确分解仅基于两个数据点（K=1, K=4）**：要声称精确的百分比分解，至少需要 K=2, 4, 8, 16 等更多数据点以观察趋势。

**但补充一点**：R1 的批评主要针对 per-layer KL decomposition 实验（§4.5），而论文对 signal type 重要性的论证并非仅依赖此实验。§3.6 的梯度分析（BCE gradient $\partial \mathcal{L}/\partial o_j = \sigma(s_j) - m_j^*$ 仅依赖 neuron $j$，而 KL gradient 通过 downstream Jacobian 耦合所有 neuron）提供了与实验独立的理论论证。Table 3 的 C1 ablation 也从另一角度支撑了 signal type 的重要性。所以 N1 削弱的是 "quantitative decomposition" 的精度，但不完全否定 "signal type matters" 的定性结论。

建议作者：(1) 删除或大幅软化 "29-97%" 的精确分解 claim；(2) 补充更多 K 值的实验或移除 decomposition framing，改为定性讨论；(3) 明确承认 K=1 的 near-dense training confound。

---

**[AGREE] R1-N2: 知识密集型任务退步缺乏机制分析**

完全同意。这也与我 Review 中的 W1 (wall-clock) 关切呼应——如果方法在 MMLU/GSM8K 上系统性退步，其实际部署场景会进一步受限。

具体补充：

1. **退步的一致性和幅度令人担忧**：从论文数据看，KL predictor 在 30% sparsity 下 MMLU 40.7±1.3（Table 2）vs TEAL baseline 应该更高；在 Qwen-2.5-14B 上 GSM8K 退步更严重（Table 13, Appendix O）。这不是个别 seed 的噪声，而是跨架构的系统性 pattern。

2. **§4.4 的 "Remove valley" 实验（Table 4: MMLU +3.4pp）方向正确但不够**：它证明了 allocation pattern 影响 MMLU，但未回答核心问题——为什么 KL 的 output-distribution objective 会系统性地学到一个牺牲知识路径的 allocation？是因为 WikiText-103 训练分布中知识密集型 context 不足？还是 KL 本身的 mode-covering 特性导致它对高 entropy 层（恰好是知识存储层）施加更强的 sparsity 压力？论文应至少提出并讨论这些假设。

3. **R1 建议的 Meng et al. (2022) "Locating and Editing Factual Associations" 参考是合理的**：理解哪些层/neuron 存储 factual knowledge 可以帮助解释为什么 KL 的 allocation 会伤害 MMLU。但我认为这更适合作为 future work 方向而非 must-fix——要求作者做完整的 knowledge attribution analysis 超出了 revision 的合理范围。

---

### Should-Fix 问题

**[AGREE] R1-W1: C1 ablation 残余 confound**

同意 soft→hard mask representation 变化引入了额外混淆变量。具体而言：

1. KL 训练使用 Gumbel-Sigmoid 连续 soft masks（§3.3），C1 ablation 用 $\mathbb{1}(s_j \geq 0)$ 二值化提取 oracle masks。这一过程丢弃了 neuron importance 的 **排序信息**——两个 $s_j = 0.01$ 和 $s_j = 5.0$ 的 neuron 被等同对待。如 R1 所问（Q3），保留连续分数可能改善 C1 结果。

2. 但 C1 的核心结论（KL-derived patterns transfer quality advantage to simpler training, PPL within 0.79pp）在方向上仍然成立——即使存在 confound，0.79pp 的差距说明 mask pattern 质量是主要贡献因素。confound 的存在使精确量化不可靠，但定性结论稳健。

---

**[AGREE] R1-W2: 无 wall-clock 加速**

完全同意，我在自己的审稿中也将此列为 W1。Appendix A 显示 predictor 增加 6.4% overhead，且 "unstructured element-wise masks do not translate to wall-clock speedup without sparse kernel support"（Abstract）。对于一篇 sparsity 论文，这是显著缺失。

---

**[AGREE] R1-W3: 评估覆盖度空白**

同意所有三点：

1. **无生成任务（MT-Bench, AlpacaEval）**：sparsity 对 autoregressive generation quality 的影响可能与 perplexity 和 MC-style downstream tasks 不同——generation 中误差可能累积，而 PPL 只衡量 next-token prediction。这与 N2 (knowledge-intensive degradation) 结合尤为重要：如果 MMLU 已经退步，generation quality 退步可能更严重。

2. **序列长度固定 2048**：论文未讨论长序列下 activation pattern 是否变化。contextual sparsity 的核心假设是 mask depends on input——如果 input 长度从 2048 增到 8192 或 32K，pattern 可能发生质性变化。

3. **Batched inference 未评估**：实际部署中 batch size > 1 是常态，但 predictor 的 overhead 和 sparsity pattern 的 batch consistency 均未测试。

---

**[AGREE] R1-W4: 高方差指标的统计可靠性**

同意，但补充 nuance：

1. **PPL（论文的 primary metric）方差很低**：Table 2 报告 11.84±0.15（3-seed），置信区间窄，结论可靠。

2. **但 downstream tasks 方差确实过大**：ARC-c σ=3.6pp 在 3 seed 下 95% CI ≈ ±8.9pp，这意味着 KL vs TEAL 的差异（如 Table 2 中 ARC-c 的绝对值）可能在统计上不显著。BoolQ σ=11.5pp 更是使得该指标的任何结论都不可靠。论文应至少做 paired permutation test 或报告 effect size。

3. **Table 4 多行单 seed（s42）确实削弱可信度**：特别是 ablation study（Table 4）的 "Relaxation, Divergence, and SPON" 部分，这些是论文的核心 design choice 验证，理应 multi-seed。

---

**[REBUT] R1-W5: Geometric penalty 在 30% 目标下偏差**

部分不同意。

1. R1 说 "30% 目标永远无法精确达到（28.5% actual）"——但论文 Appendix C (Table 9, p.13) 明确报告了 actual sparsity 随 target 的收敛曲线，且指出 "the controller reliably drives actual sparsity to within ±2% of the target across all tested regimes"。28.5% vs 30% 是 1.5pp 偏差，在 sparsity 研究中属于正常范围。

2. **但 labeling 的 concern 有道理**：主文 Table 2 表头标注 "uniforms at 30%" 而非 "uniforms at ~28.5% actual"，这可能误导读者做精确的跨方法对比（如与 TEAL exactly 30% 对比）。建议在 Table 2 脚注标注 actual sparsity range。

3. ε=0.02 deadzone 的工程合理性在 Appendix C 有解释（"suppresses oscillation near the target"），这不是任意选择。但 R1 的 concern 是 deadzone 导致 systematic undershoot，这确实需要在正文中 acknowledge。

总结：偏差本身不严重（1.5pp），但 labeling 应更精确。这是 minor 而非 warning 级别问题。

---

### 对 R1 Questions 的补充看法

**Q1 (K=4 50% 为何比 K=1 差)**：R1 的问题切中要害。我推测是因为 50% sparsity 下同时 mask 4 层（K=4 = 4/32 = 12.5% 层被 mask）引入的前向扰动远大于 K=1，导致 gradient signal 质量下降。但这需要实验验证（如比较 K=1/2/4/8 的 training loss curve 和 gradient SNR）。

**Q2 (知识退步是否与 WikiText-103 有关)**：合理假设。WikiText-103 是百科风格但主要是英文维基，可能缺少数学推理和多步逻辑链的训练信号。如果在 code+math 混合数据上训练 predictor，MMLU/GSM8K 表现可能改善。但这也是推测，需要实验。

**Q3 (C1 保留连续分数)**：好问题。当前 $\mathbb{1}(s_j \geq 0)$ 二值化确实丢弃了 ranking 信息。一个改进方案是用 KL-derived soft scores 作为 BCE target 的 soft label（而非 hard 0/1），这可能更干净地隔离 pattern quality 的贡献。

**Q4 (STE 30% 仅 20.8% sparsity)**：Table 4 显示 STE 在 30% 下 PPL 15.77，且实际 sparsity 仅 20.8%。这说明 STE 的 gradient 通路问题不仅影响 quality 还影响 sparsity control——进一步支持 Gumbel-Sigmoid 作为 relaxation method 的重要性。但 R1 问是否调过 lr/gradient scaling——论文确实应回答这一问题，否则 STE 可能是 undertrained 而非方法本身不行。

**Q5 (MSE 30% 3-seed)**：合理的数据完整性问题，应在 camera-ready 中明确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1942 · 2026-05-22T23:51:52.952816+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1943 · 2026-05-22T23:51:53.003688+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T23:39:40.137898+00:00\", \"completed_at\": \"2026-05-22T23:42:52.408058+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item（纯 Abstract + Introduction 文字）。第一个视觉锚点 Figure 1（Method overview）出现在 page 2 右栏，在前 3 页范围内，符合预期。Title/Author/Abstract 排版整洁专业。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 为单栏图，展示方法架构概览。Caption 自包含（描述了 predictor 结构、KL 目标、TEAL 分配），与 title/abstract 讲同一个故事。分辨率清晰可读。作为首个 display item 有效传达核心 idea。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"整页纯文本（Related Work），无 figure/table/equation。但前后页（p2 有 Figure 1，p4 有多个公式）打断了文字单调感，不构成连续纯文本问题。Related Work 纯文本属常见模式。\"}, {\"severity\": \"info\", \"dimension\": \"page 4-5\", \"message\": \"Method 节公式(1)-(7)渲染正确，无乱码/缺失符号。Table 1（Taxonomy）出现在 p5 右栏，booktabs 风格，空白单元格有注释说明。文字-公式-表格节奏良好。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 中脚注字号偏小但仍可读。表格清晰展示了二维分类法，Empty cells 有 caption 说明。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2（Main results）在 Experiments 开头出现，位置合理。Booktabs 风格，最优结果加粗，精度统一（小数点后 1-2 位）。表头清晰，caption 自包含。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Tables 3-4 紧凑排列在右栏。两个表均使用 booktabs 风格，最优加粗。Table 4 的 ablation 设计清晰，各列精度一致。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2（PPL scaling plot）出现在右栏，线条清晰，颜色可区分。图例（legend）字号略小但仍可辨认。Section 5 Conclusion 从本页底部开始，heading 后有足够正文行数（无孤悬问题）。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 2 的 y 轴标签和图例文字字号偏小（估计 ~6-7pt），接近正文字号 70% 下限。打印时可能不够清晰。建议适当增大图内文字。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落简短精炼（~3 个要点），Ethics Statement 紧随其后。References 从本页下半部开始。主正文（pages 1-8）符合 EMNLP 8 页限制。\"}, {\"severity\": \"info\", \"dimension\": \"pages 10-11\", \"message\": \"References 页排版正常，双栏格式统一
…[truncated 1361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1944 · 2026-05-22T23:57:38.783401+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 24 (Fresh Review) — Active issues\n  # ============================================================\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL decomposition 的 train-inference mismatch confound 未解决\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 20\n    last_seen_round: 24\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。K=4 single-seed。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N2。97.5% 精确数字不可靠。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C1。K=1 有 32× train-inference mismatch；K=4 在 50% 反常差于 K=1 (44.23 vs 34.85) 缺乏机制解释；仅两个 K 值不足以支撑 29-97% 精确分解。定性结论（signal type matters）由 Table 4 五种 loss 对比和梯度分析独立支撑。\"}\n    action_items:\n      - {round: 21, action: \"K=4 3-seed (s42/s123/s456)\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"97.5% → 定性 'majority of PPL gap'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"K=4 50% s42 PPL-only 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 24, action: \"Abstract/Conclusion 的 decomposition claim 需进一步软化或删除精确百分比\", assigned_to: \"paper_agent\", status: pending}\n      - {round: 24, action: \"补充 K=8/K=16 实验或移除定量分解框架\", assigned_to: \"main_agent\", status: pending}\n      - {round: 24, action: \"K=4 50% 反常结果需提供假设性解释\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨架构系统性退步缺乏机制分析\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 24\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。Protection valley 分析仅 correlational。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N3。要求追踪 Remove Valley + task-aware allocation。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C2。Remove valley 方向正确但不够——未回答 WHY KL 系统性学到牺牲知识路径的 allocation。8B MMLU -5.2pp, 14B GSM8K -20pp。\"}\n    action_items:\n      - {round: 21, action: \"Constraint 实验 (protect_late + remove_valley)\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"§4.2 深化: Geva 引用 + task-aware allocation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 24, action: \"至少提出并讨论具体假设（训练数据偏差？forward KL mode-covering？）\", assigned_to: \"paper_agent\", status: pending}\n      - {round: 24, action: \"引用 Meng et al. 2022 分析知识存储层 mask 差异\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W1\"\n    summary: \"评估覆盖度关键空白：无生成任务、固定 seq_len=2048、无 batched inference\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"无 MT-Bench/AlpacaEval 等生成任务；seq length 固定 2048；batched inference 未评估。Sparsity 对 autoregressive generation 和长序列的行为可能与 PPL/MC tasks 不同。\"}\n    action_items:\n      - {round: 24, action: \"Limitations 加入 '生成任务未评估' 作为第四点\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W2\"\n    summary: \"高方差下游指标（ARC-c σ=3.6, BoolQ σ=11.5）统计可靠性不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"ARC-c 3-seed 95% CI ≈ ±8.9pp，差异统计不显著。Table 4 多行仅 s42。PPL primary metric 方差极低（σ=0.02），结论可靠。\"}\n    action_items:\n      - {round: 24, action: \"正文对高方差指标加注 'not statistically significant'\", assigned_to: \"paper_agent\", status: pending}\n      - {round: 24, action: \"Table 4 关键行补充 3-seed\", assigned_to: \"main_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W3\"\n    summary: \"C1 ablation soft→hard mask representation 残余 confound\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"Oracle 二值化 logits>0 丢失排序信息。定性结论（mask patterns transfer, PPL within 0.79pp）稳健，精确量化不可靠。\"}\n    action_items:\n      - {round: 24, action: \"讨论 oracle 提取信息损失的可能性\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W4\"\n    summary: \"'Dominant design dimension' 声明需资格限定\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"定量基础因 per-layer 分解 confound 不可靠。定性方向由 Table 4 五种 loss 和梯度分析支撑。建议软化为 'substantially outperforms per-neuron classification and intermediate losses'。\"}\n    action_items:\n      - {round: 24, action: \"Abstract/Conclusion 中 'dominant' → 软化措辞\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 24 — Carried forward (status unchanged or minor update)\n  # ============================================================\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无 speedup\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 24\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。Intro framing 已修改为 empirical study。\"}\n      - {round: 22, reviewers: [1, 2], note: \"降为 Warning。论文已定位为 analysis work。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 W1。仍为 Warning。论文 framing 诚实但实际影响力受限。\"}\n    action_items:\n      - {round: 21, action: \"Abstract 加 empirical study + §1 disclaimer\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"§1 加 speedup 条件 + 6.4% overhead\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"结构性限制。已充分 framed。\"\n    resolution_round: 23\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 24\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。\"}\n      - {round: 22, reviewers: [1, 2], note: \"降为 Warning。R1 REBUT 有效。\"}\n      - {round: 24, reviewers: [2], note: \"R2 再次提出 Critical，但 R1 factual correction 有效（Related Work 实际 4 句话、contextual vs static 是不同学习问题）。降级为 Warning（framing 可改善但非 novelty 缺失）。\"}\n    action_items:\n      - {round: 21, action: \"§2 MaskLLM 3-point differentiation\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"§2 三点本质差异已讨论。Introduction 可更早定位与 MaskLLM 的关系。\"\n    resolution_round: 23\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap ablation 因果声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 24\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Warning。'suggests' hedging 被认可。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N1。排除性声明超出证据。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 新增 W3 (soft→hard confound)。定性结论稳健。\"}\n    action_items:\n      - {round: 22, action: \"降级为 transferability + 删除排除性声明\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"C1 claim 已降级为 transferability。soft→hard confound 作为独立 warning (R24-W3) 追踪。\"\n    resolution_round: 23\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD variance\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 24\n    mentions:\n      - {round: 22, reviewers: [], note: \"R22 未单独提出（已在 Limitations 讨论）。\"}\n      - {round: 24, reviewers: [1], note: \"R1 指出论文已有充分 OOD 证据（Appendix D: C4 PPL + 下游 Δ≤1.1pp）。R2 concern 被 R1 REBUT。仍为 in_progress。\"}\n    action_items:\n      - {round: 20, action: \"Limitations 加 WikiText 同分布 + C4 限制\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W5\"\n    summary: \"规模泛化仅 7-14B\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W5。Qwen-14B GSM8K -20pp。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 W5。跨架构证据仍 preliminary，无跨模型 C1 ablation。但论文已 acknowledge。R2 Critical, R1 降为 Warning。\"}\n    action_items:\n      - {round: 22, action: \"Limitations 加 scale trade-off 讨论\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Limitations 已包含 'evaluation bounded at 7-14B'。\"\n    resolution_round: 23\n\n  - id: \"R22-W6\"\n    summary: \"Figure 2 仅展示 global allocation 但推荐 uniform\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 24\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W6。正文 Figure 之一，framing 效果强。\"}\n      - {round: 24, reviewers: [], note: \"R24 Visual check 发现 Figure 2 字号偏小 (~6-7pt)。issue 未被 reviewer 单独提出。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot 限制实际影响\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [], note: \"本轮未被 Reviewer 单独提出。论文 Limitations 已覆盖。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Carried forward — resolved, unchanged\n  # ============================================================\n\n  - id: \"R22-W3\"\n    summary: \"Table 2 actual sparsity mismatch ‡ 脚注不够显著\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W3。\"}\n      - {round: 24, reviewers: [1], note: \"R1 W5 提及 labeling 仍不够醒目但降为 Minor。R2 partial REBUT (1.5pp 偏差正常)。\"}\n    action_items:\n      - {round: 22, action: \"§4.1 matched sparsity 独立句\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"§4.1 matched 14.5% 作为独立句。‡ 脚注存在。\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"KL global 50% 下游 3-seed 已补全\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W4。Table 2 更新为 3-seed。\"}\n    action_items:\n      - {round: 22, action: \"Table 2 更新为 3-seed mean±std\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Table 2 KL global 50% 全部 3-seed。\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"Abstract 第5句信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"Abstract 第5句拆为两个清晰句子。\"\n    resolution_round: 23\n\n  - id: \"R22-W8\"\n    summary: \"Conclusion 引用 BoolQ (高 variance, 仅 Appendix)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"Conclusion BoolQ → HellaSwag/PIQA。\"\n    resolution_round: 23\n\n  - id: \"R22-M2\"\n    summary: \"§3.5 deadzone margin ε=0.02 缺乏 justification\"\n    category: method\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"'suppresses oscillation near the target'\"\n    resolution_round: 23\n\n  - id: \"R22-M3\"\n    summary: \"BCE 2700 steps wall-clock 与 KL 1000 steps 接近需解释\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"已解释。\"\n    resolution_round: 23\n\n  - id: \"R22-M4\"\n    summary: \"'Adaptive Penalty Controller' 命名不准确\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"重命名为 'Geometric Penalty Schedule'。\"\n    resolution_round: 23\n\n  - id: \"R22-M6\"\n    summary: \"Limitations 未讨论 sequence length\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"已修复。Limitations 包含 seq length。\"}\n    resolution: \"已修复。\"\n    resolution_round: 23\n\n  - id: \"R19-W4\"\n    summary: \"MSE baseline 50% s123 灾难性失败\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [1], note: \"R1 Q5 问 MSE 30% 3-seed 是否含所有 seed。\"}\n    resolution: \"Instability 本身是 finding。\"\n    resolution_round: 22\n\n  - id: \"R19-W3\"\n    summary: \"Knowledge-intensive 退步缺乏机制解释\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 22\n    resolution: \"合并进 R20-N2。\"\n    resolution_round: 23\n\n  - id: \"R21-W2\"\n    summary: \"符号冲突 g→ε\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"method.tex g1/g2 → ε1/ε2。\"\n    resolution_round: 22\n\n  - id: \"R20-N3\"\n    summary: \"'Coupling alignment' 术语替换\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    resolution: \"术语替换完成。\"\n    resolution_round: 21\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [2], note: \"R2 再次提出但 R1 factual rebuttal 有效。合并进 R19-W1。\"}\n    resolution: \"§2 三点本质差异。\"\n    resolution_round: 23\n\n  - id: \"R19-W6\"\n    summary: \"Actual sparsity mismatch 在主表不够显著\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 22\n    resolution: \"合并进 R22-W3。\"\n    resolution_round: 23"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 24 (Fresh Review) — Active issues\n  # ============================================================\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL decomposition 的 train-inference mismatch confound 未解决\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 20\n    last_seen_round: 24\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。K=4 single-seed。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N2。97.5% 精确数字不可靠。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C1。K=1 有 32× train-inference mismatch；K=4 在 50% 反常差于 K=1 (44.23 vs 34.85) 缺乏机制解释；仅两个 K 值不足以支撑 29-97% 精确分解。定性结论（signal type matters）由 Table 4 五种 loss 对比和梯度分析独立支撑。\"}\n    action_items:\n      - {round: 21, action: \"K=4 3-seed (s42/s123/s456)\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"97.5% → 定性 'majority of PPL gap'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"K=4 50% s42 PPL-only 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 24, action: \"Abstract/Conclusion 的 decomposition claim 需进一步软化或删除精确百分比\", assigned_to: \"paper_agent\", status: pending}\n      - {round: 24, action: \"补充 K=8/K=16 实验或移除定量分解框架\", assigned_to: \"main_agent\", status: pending}\n      - {round: 24, action: \"K=4 50% 反常结果需提供假设性解释\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨架构系统性退步缺乏机制分析\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 24\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。Protection valley 分析仅 correlational。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N3。要求追踪 Remove Valley + task-aware allocation。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C2。Remove valley 方向正确但不够——未回答 WHY KL 系统性学到牺牲知识路径的 allocation。8B MMLU -5.2pp, 14B GSM8K -20pp。\"}\n    action_items:\n      - {round: 21, action: \"Constraint 实验 (protect_late + remove_valley)\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"§4.2 深化: Geva 引用 + task-aware allocation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 24, action: \"至少提出并讨论具体假设（训练数据偏差？forward KL mode-covering？）\", assigned_to: \"paper_agent\", status: pending}\n      - {round: 24, action: \"引用 Meng et al. 2022 分析知识存储层 mask 差异\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W1\"\n    summary: \"评估覆盖度关键空白：无生成任务、固定 seq_len=2048、无 batched inference\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"无 MT-Bench/AlpacaEval 等生成任务；seq length 固定 2048；batched inference 未评估。Sparsity 对 autoregressive generation 和长序列的行为可能与 PPL/MC tasks 不同。\"}\n    action_items:\n      - {round: 24, action: \"Limitations 加入 '生成任务未评估' 作为第四点\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W2\"\n    summary: \"高方差下游指标（ARC-c σ=3.6, BoolQ σ=11.5）统计可靠性不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"ARC-c 3-seed 95% CI ≈ ±8.9pp，差异统计不显著。Table 4 多行仅 s42。PPL primary metric 方差极低（σ=0.02），结论可靠。\"}\n    action_items:\n      - {round: 24, action: \"正文对高方差指标加注 'not statistically significant'\", assigned_to: \"paper_agent\", status: pending}\n      - {round: 24, action: \"Table 4 关键行补充 3-seed\", assigned_to: \"main_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W3\"\n    summary: \"C1 ablation soft→hard mask representation 残余 confound\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"Oracle 二值化 logits>0 丢失排序信息。定性结论（mask patterns transfer, PPL within 0.79pp）稳健，精确量化不可靠。\"}\n    action_items:\n      - {round: 24, action: \"讨论 oracle 提取信息损失的可能性\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W4\"\n    summary: \"'Dominant design dimension' 声明需资格限定\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"定量基础因 per-layer 分解 confound 不可靠。定性方向由 Table 4 五种 loss 和梯度分析支撑。建议软化为 'substantially outperforms per-neuron classification and intermediate losses'。\"}\n    action_items:\n      - {round: 24, action: \"Abstract/Conclusion 中 'dominant' → 软化措辞\", assigned_to: \"paper_agent\", status: pending}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 24 — Carried forward (status unchanged or minor update)\n  # ============================================================\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无 speedup\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 24\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。Intro framing 已修改为 empirical study。\"}\n      - {round: 22, reviewers: [1, 2], note: \"降为 Warning。论文已定位为 analysis work。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 W1。仍为 Warning。论文 framing 诚实但实际影响力受限。\"}\n    action_items:\n      - {round: 21, action: \"Abstract 加 empirical study + §1 disclaimer\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"§1 加 speedup 条件 + 6.4% overhead\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"结构性限制。已充分 framed。\"\n    resolution_round: 23\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 24\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。\"}\n      - {round: 22, reviewers: [1, 2], note: \"降为 Warning。R1 REBUT 有效。\"}\n      - {round: 24, reviewers: [2], note: \"R2 再次提出 Critical，但 R1 factual correction 有效（Related Work 实际 4 句话、contextual vs static 是不同学习问题）。降级为 Warning（framing 可改善但非 novelty 缺失）。\"}\n    action_items:\n      - {round: 21, action: \"§2 MaskLLM 3-point differentiation\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"§2 三点本质差异已讨论。Introduction 可更早定位与 MaskLLM 的关系。\"\n    resolution_round: 23\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap ablation 因果声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 24\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Warning。'suggests' hedging 被认可。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N1。排除性声明超出证据。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 新增 W3 (soft→hard confound)。定性结论稳健。\"}\n    action_items:\n      - {round: 22, action: \"降级为 transferability + 删除排除性声明\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"C1 claim 已降级为 transferability。soft→hard confound 作为独立 warning (R24-W3) 追踪。\"\n    resolution_round: 23\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD variance\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 24\n    mentions:\n      - {round: 22, reviewers: [], note: \"R22 未单独提出（已在 Limitations 讨论）。\"}\n      - {round: 24, reviewers: [1], note: \"R1 指出论文已有充分 OOD 证据（Appendix D: C4 PPL + 下游 Δ≤1.1pp）。R2 concern 被 R1 REBUT。仍为 in_progress。\"}\n    action_items:\n      - {round: 20, action: \"Limitations 加 WikiText 同分布 + C4 限制\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W5\"\n    summary: \"规模泛化仅 7-14B\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W5。Qwen-14B GSM8K -20pp。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 W5。跨架构证据仍 preliminary，无跨模型 C1 ablation。但论文已 acknowledge。R2 Critical, R1 降为 Warning。\"}\n    action_items:\n      - {round: 22, action: \"Limitations 加 scale trade-off 讨论\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Limitations 已包含 'evaluation bounded at 7-14B'。\"\n    resolution_round: 23\n\n  - id: \"R22-W6\"\n    summary: \"Figure 2 仅展示 global allocation 但推荐 uniform\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 24\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W6。正文 Figure 之一，framing 效果强。\"}\n      - {round: 24, reviewers: [], note: \"R24 Visual check 发现 Figure 2 字号偏小 (~6-7pt)。issue 未被 reviewer 单独提出。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot 限制实际影响\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [], note: \"本轮未被 Reviewer 单独提出。论文 Limitations 已覆盖。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Carried forward — resolved, unchanged\n  # ============================================================\n\n  - id: \"R22-W3\"\n    summary: \"Table 2 actual sparsity mismatch ‡ 脚注不够显著\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W3。\"}\n      - {round: 24, reviewers: [1], note: \"R1 W5 提及 labeling 仍不够醒目但降为 Minor。R2 partial REBUT (1.5pp 偏差正常)。\"}\n    action_items:\n      - {round: 22, action: \"§4.1 matched sparsity 独立句\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"§4.1 matched 14.5% 作为独立句。‡ 脚注存在。\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"KL global 50% 下游 3-seed 已补全\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W4。Table 2 更新为 3-seed。\"}\n    action_items:\n      - {round: 22, action: \"Table 2 更新为 3-seed mean±std\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Table 2 KL global 50% 全部 3-seed。\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"Abstract 第5句信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"Abstract 第5句拆为两个清晰句子。\"\n    resolution_round: 23\n\n  - id: \"R22-W8\"\n    summary: \"Conclusion 引用 BoolQ (高 variance, 仅 Appendix)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"Conclusion BoolQ → HellaSwag/PIQA。\"\n    resolution_round: 23\n\n  - id: \"R22-M2\"\n    summary: \"§3.5 deadzone margin ε=0.02 缺乏 justification\"\n    category: method\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"'suppresses oscillation near the target'\"\n    resolution_round: 23\n\n  - id: \"R22-M3\"\n    summary: \"BCE 2700 steps wall-clock 与 KL 1000 steps 接近需解释\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"已解释。\"\n    resolution_round: 23\n\n  - id: \"R22-M4\"\n    summary: \"'Adaptive Penalty Controller' 命名不准确\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"重命名为 'Geometric Penalty Schedule'。\"\n    resolution_round: 23\n\n  - id: \"R22-M6\"\n    summary: \"Limitations 未讨论 sequence length\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"已修复。Limitations 包含 seq length。\"}\n    resolution: \"已修复。\"\n    resolution_round: 23\n\n  - id: \"R19-W4\"\n    summary: \"MSE baseline 50% s123 灾难性失败\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [1], note: \"R1 Q5 问 MSE 30% 3-seed 是否含所有 seed。\"}\n    resolution: \"Instability 本身是 finding。\"\n    resolution_round: 22\n\n  - id: \"R19-W3\"\n    summary: \"Knowledge-intensive 退步缺乏机制解释\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 22\n    resolution: \"合并进 R20-N2。\"\n    resolution_round: 23\n\n  - id: \"R21-W2\"\n    summary: \"符号冲突 g→ε\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"method.tex g1/g2 → ε1/ε2。\"\n    resolution_round: 22\n\n  - id: \"R20-N3\"\n    summary: \"'Coupling alignment' 术语替换\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    resolution: \"术语替换完成。\"\n    resolution_round: 21\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [2], note: \"R2 再次提出但 R1 factual rebuttal 有效。合并进 R19-W1。\"}\n    resolution: \"§2 三点本质差异。\"\n    resolution_round: 23\n\n  - id: \"R19-W6\"\n    summary: \"Actual sparsity mismatch 在主表不够显著\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 22\n    resolution: \"合并进 R22-W3。\"\n    resolution_round: 23"
  }
}
```

</details>

---


### Tool result

_source line 1945 · 2026-05-22T23:57:38.884548+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 13540}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1946 · 2026-05-22T23:59:56.717260+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 24 (Fresh Review)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性)\n**圆桌轮次**: 1 轮初审 + 1 轮交叉分享，关键问题达成共识\n\n---\n\n## Summary\n\n本文用 forward KL divergence + Gumbel-Sigmoid 松弛训练 SwiGLU LLM 的上下文稀疏预测器（75.9M 参数，<1% base），替代传统 BCE per-neuron 独立目标。在 LLaMA-3.1-8B 上，KL predictor 在 30%/50% 稀疏度下分别降低 TEAL 的 PPL 14.5%/50%，且无需额外补偿网络（-67.2M params）。论文通过 C1 target-swap ablation 和 per-layer KL 控制实验分解了 signal type 与 coupling scope 的贡献，并提供梯度分析和 2D taxonomy 组织现有方法。定位为经验研究。\n\n---\n\n## Strengths\n\n**S1. 核心效应量大且跨架构稳健** [AGREE: R1, R2]\nKL vs BCE/TEAL 的 PPL 差距在 30%（8.81 vs 11.25/10.82）和 50%（11.84 vs 28.13/23.90）均超过 25%，3-seed 方差极低（σ=0.02 at 30%）。跨架构验证（Mistral-7B -17.3%, Qwen-14B consistent PPL advantage）确认不是架构特异现象。\n\n**S2. C1 target-swap ablation 是精巧的实验设计** [AGREE: R1, R2]\n用 KL 发现的 mask 训练 BCE predictor，分离 mask 质量 vs 训练动态的贡献（PPL within 0.79pp at 50%, s42；3-seed at 30% gap ≤1.70pp）。这一分析在稀疏性预测文献中是新颖的。\n\n**S3. 消融覆盖广泛且控制严格** [R1]\nTable 4 系统比较 5 种 loss（Forward KL, Reverse KL, JSD, MSE, BCE）× 2 种 relaxation（Gumbel, STE），MSE baseline 除 loss 外完全一致（Appendix G）。附录提供 d_b sensitivity、temperature schedule、training convergence、compensation redundancy 完整 robustness picture。\n\n**S4. 梯度分析提供有价值的理论直觉** [AGREE: R1, R2]\n§3.6 清晰展示 BCE gradient 仅依赖 neuron j，而 KL gradient 通过 downstream Jacobian 耦合所有 neuron——解释了 KL 为何能发现 composition-aware mask patterns。\n\n**S5. 自我定位诚实** [AGREE: R1, R2]\n论文自称 \"primarily an empirical study\"，始终保持定位。Limitations 覆盖 seq length、batched inference、知识任务退步等。\n\n**S6. Predictor 高效且训练成本低** [R2]\n75.9M params (<1% base)，45 min 单 GPU 训练，消除 67.2M 补偿网络。\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**C1. Per-layer KL 分解存在根本性 confound，定量声明不可靠** [AGREE: R1-N1, R2 cross-AGREE]\n\nK=1 控制实验存在 32× train-inference mismatch（训练 mask 1/32 层，推理 mask 全部 32 层）。论文标注 \"upper bound\" 但 Abstract/Conclusion 仍将 \"signal type accounts for the majority of the PPL gap\" 作为核心贡献呈现，资格限定传达不足。\n\nK=4 在 50% 下反常差于 K=1（PPL 44.23 vs 34.85），与 \"K 越大越接近 E2E\" 的直觉矛盾，缺乏机制解释。K=4 在 30% MMLU 超过 E2E（42.7 vs 40.7），混入 allocation 效应。仅两个数据点（K=1, K=4）不足以支撑 \"29-97% on downstream tasks\" 的精确分解。\n\n**重要补充**：定性结论（signal type matters）仍由梯度分析（§3.6）和 Table 4 的 5-loss 对比独立支撑，不完全依赖 per-layer 分解。被削弱的是精确的定量百分比，而非方向性结论。\n\n**C2. 知识密集型任务系统性退步缺乏机制分析** [AGREE: R1-N2, R2 cross-AGREE]\n\nKL 在所有测试规模和架构上均系统性低于 TEAL 的 MMLU/GSM8K：\n- 8B 30%: MMLU -5.2pp (40.7 vs 45.86)\n- 8B 30% global: MMLU -10.2pp (35.7 vs 45.86), σ=9.5\n- 14B 30% uniform: MMLU -2.8pp, GSM8K -20.1pp\n\n§4.4 的 Remove valley (MMLU +3.4pp) 方向正确，但未回答核心问题：为什么 KL 的 output-distribution 目标系统性学到牺牲知识路径的 allocation pattern？是 WikiText-103 训练分布的偏差？是 forward KL mode-covering 的固有特性？还是 Gumbel-Sigmoid 的采样偏差？对于自称 \"characterize how training objective shapes sparsity prediction quality\" 的论文，这是核心分析空白。\n\n### Should-Fix (Warning)\n\n**W1. 无 wall-clock speedup** [AGREE: R1, R2]\nPredictor 增加 6.4% latency overhead，unstructured masks 无法实现实际加速。论文定位为 empirical study 已适当 frame，但实际影响力受限。\n\n**W2. C1 ablation 存在残余 confound** [AGREE: R1-W1, R2 cross-AGREE]\nC1 同时改变训练目标（KL→BCE）和 mask 表示（soft Gumbel → hard binary）。Oracle 二值化（logits > 0）丢失排序信息。定性结论（mask patterns transfer quality, PPL within 0.79pp）因 gap 小而稳健，精确量化不可靠。\n\n**W3. 评估覆盖度存在关键空白** [AGREE: R1-W3, R2 cross-AGREE]\n无生成任务评估（MT-Bench, AlpacaEval）；序列长度固定 2048；batched inference 未评估。Sparsity 对 autoregressive generation 和长序列的行为可能与 PPL/MC-style tasks 显著不同。\n\n**W4. 高方差下游指标的统计可靠性不足** [AGREE: R1-W4, R2 cross-AGREE]\nARC-c σ=3.6pp（3-seed 95% CI ≈ ±8.9pp），BoolQ σ=11.5pp，使得这些指标的均值差异统计不显著。Table 4 多行仅 s42 单 seed。PPL（primary metric）方差极低（σ=0.02-0.15），结论可靠。\n\n**W5. 跨架构/跨规模泛化证据不足** [R2-N3 降级, R1 AGREE at warning level]\n核心实验全部基于 LLaMA-3.1-8B。Mistral-7B 和 Qwen-14B 仅有 main results，无 C1 ablation 或 per-layer 分解。论文已 acknowledge (\"evaluation bounded at 7-14B\")，但 \"dominant design dimension\" 声明隐含通用性。\n\n**W6. \"Dominant design dimension\" 声明需资格限定** [Derived from C1 confound]\n该声明的定量基础因 per-layer 分解 confound 不可靠。定性方向由 Table 4 五种 loss 对比和梯度分析支撑，但 \"dominant\" 措辞过强。建议软化为 \"output-distribution alignment substantially outperforms per-neuron classification and intermediate losses\"。\n\n### Minor\n\n- Figure 2 y 轴和图例文字偏小（~6-7pt），接近可读性下限（视觉审查 Warning）\n- Geometric penalty schedule 实际稀疏度 28.5% vs 名义 30%，Table 2 ‡ 标注存在但不够醒目\n- Table 2 中 BCE 30% 使用 global allocation（脚注 †），无 BCE 30% uniform 对比\n- 无代码/数据/模型释放声明\n- Introduction 中与 MaskLLM 的关系应更早建立（当前仅在 Related Work）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **KL vs BCE/TEAL 的 PPL 优势大、稳健、跨架构一致**——核心发现可靠，不是边界效应\n2. **C1 target-swap ablation 是新颖且有价值的实验设计**——在稀疏性预测文献中前所未见\n3. **Per-layer KL 分解的 confound 削弱定量声明**——\"29-97%\" 精确分解不可靠，但定性方向（signal type matters）独立成立\n4. **知识密集型任务退步是实际影响力的主要限制**——缺乏机制分析\n5. **无 wall-clock speedup 限制了实用价值**——论文 framing 诚实\n6. **论文定位诚实、消融全面、写作透明**——高于平均水平\n\n## Reviewer Divergence\n\n**R2-N1 (MaskLLM 新颖性)**：R2 判定 Critical（\"仅1句话讨论 MaskLLM\"），R1 REBUT（实际4句话，contextual vs static 是 fundamentally different learning problems）。\n→ **Director 判定**：R1 factual correction 成立。MaskLLM 区分已有基本讨论，contextual activation sparsity vs static N:M weight sparsity 确是不同学习问题。**降级为 Warning**（Introduction framing 可改善，非 novelty 缺失）。\n\n**R2-N2 (\"Dominant\" overclaimed)**：R2 判定 Critical（\"仅比较两种方法\"），R1 REBUT（Table 4 已对比 5 种 loss：Forward KL, Reverse KL, JSD, MSE, BCE）。\n→ **Director 判定**：R2 断言为**事实性错误**——Table 4 明确包含 5 种 loss function 的系统对比。但 \"dominant\" 声明仍因 per-layer 分解 confound 需资格限定。**降级为 Warning**（合并入 W6）。\n\n**R2-W4 (Gumbel confound)**：R2 判定 Warning（\"KL 和 Gumbel 贡献未 disentangle\"），R1 REBUT（BCE+Gumbel 反而恶化性能；loss effect 5.1× relaxation effect；MSE 使用相同 Gumbel）。\n→ **Director 判定**：R1 证据充分，confound 已被论文充分控制。**降级为 Info**。\n\n**R2 遗漏相关工作**：R2 列出 SparseInfer 和 TurboSparse 为遗漏引用——R1 指出两篇均已在 Section 2 引用。**R2 在此处阅读不够仔细。**\n\n---\n\n## Questions\n\n1. K=4 在 50% 下为何比 K=1 差？是否有 gradient interference 或 optimization landscape 解释？增加 K 是否单调恶化？\n2. 知识密集型退步是否与 WikiText-103 训练数据分布有关？用含 math/code 的混合语料训练是否缓解？\n3. C1 oracle 提取使用 logits > 0 二值化——是否尝试保留连续分数作为 soft label？\n4. STE 在 30% 仅达 20.8% effective sparsity——是否调整过 learning rate 或 gradient scaling？\n5. MSE 30% 3-seed mean 18.52±1.68 是否包含所有 3 个 seed（含可能的失败 seed）？\n\n---\n\n## Missing References\n\n- **Meng et al., 2022** \"Locating and Editing Factual Associations in GPT\" — 与知识密集型退步的分析直接相关 [AGREE: R1, R2]\n- **GRASP** (Group-Based Prediction of Activation Sparsity, DAC 2025) [R2]\n- Li et al., 2023 \"Inference with Reference: Lossless Acceleration of Large Language Models\" [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 完成（2026-05-22，耗时 ~3 min）\n\n- **Critical**: 0\n- **Warning**: 1 — Figure 2 的 y 轴标签和图例文字字号偏小（~6-7pt），打印时可能不够清晰\n- **Info**: 18 — 整体排版专业整洁。Figure 1 出现在 p2（首个 display item，位置合理）。所有表格 booktabs 风格，格式一致。主正文 8 页符合 EMNLP 限制。Appendix 内容密度高但排版整齐。无未解析引用。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 — Findings (可被 Findings 接收)**\n\n**置信度: 4/5**\n\n### 评分理由\n\n核心发现（KL 显著优于 BCE/TEAL 用于稀疏预测训练）可靠、效应量大、跨架构一致。C1 target-swap ablation 和梯度分析是有价值的分析性贡献。\n\n**Conference (4.0) 的主要障碍**：\n1. Per-layer 分解是三大贡献之一，但因 train-inference mismatch confound 和 K=4 反常结果，定量声明（\"29-97%\"）不可靠——需补充更多 K 值数据或降级为定性讨论\n2. 知识密集型任务系统性退步（8B MMLU -5.2pp, 14B GSM8K -20pp）缺乏机制分析——对于自称 \"characterize how training objective shapes quality\" 的论文，这是核心分析空白\n3. 无实际 wall-clock speedup，方法当前无部署价值\n\n**Findings (3.0) 的支撑理由**：\n- KL vs BCE 的核心比较稳健（多 seed、多架构、多稀疏度），实证发现有实际参考价值\n- C1 ablation 提供了 sparsity prediction 文献中前所未见的分析角度\n- 5 种 loss 的系统消融（Table 4）为后续工作提供设计指导\n- 消融全面、写作透明、自我定位诚实\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 第 5-6 句的 signal type / coupling scope 分解数字应进一步软化或删除精确百分比（\"upper bound\" 资格限定传达不足）\n- \"wall-clock speedup requires sparse kernel support not addressed here\" 和 \"primarily an empirical study\" 是重要的 honest disclaimers，应保留\n\n### Introduction (§1)\n- 与 MaskLLM 的关系应在 Introduction 更早建立——当前仅在 Related Work 讨论，读者在 Introduction 即会产生 \"this is MaskLLM for activation sparsity\" 的疑问\n- 贡献 bullet 1 的 \"29-97%\" 分解数字应降级为定性范围\n- \"This paper is primarily an empirical study\" 的定位声明是正确的策略选择\n\n### Method (§3)\n- §3.3 Gumbel-Sigmoid 设计选择论证充分，BCE+Gumbel 恶化性能的发现（Table 4）有效排除了 Gumbel 单独解释 KL 优势的假说\n- §3.5 geometric penalty 的 deadzone ε=0.02 justification 可简短补充 sensitivity 引用\n- §3.6 梯度分析是论文最有价值的部分——但应增加 caveat：coupled gradient 是发现好 mask 的充分条件还是必要条件？C1 结果暗示 coupling 不是推理阶段的必要条件\n\n### Experiments (§4)\n- Table 2：BCE 30% 使用 global allocation（脚注 †），建议补充 BCE 30% uniform 对比或说明省略原因\n- Table 2：实际稀疏度 ‡ 标注可更醒目\n- §4.5 Per-layer KL：需补充 K=8/K=16 或删除精确百分比；K=4 50% 反常结果需假设性解释\n- §4.4 Remove valley MMLU +3.4pp：应追问 \"why KL learns this pattern\" 而不仅是 \"what happens if we override it\"\n- Table 4 核心行（Forward KL + Gumbel, BCE）的 30% 数据应补充 3-seed\n\n### Limitations\n- 覆盖三个核心点，篇幅适当（符合 EMNLP 要求）\n- 建议加入 \"生成任务（open-ended generation）未评估\" 作为第四点\n\n### Ethics Statement\n- 覆盖数据来源、计算成本、安全性，内容适当",
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 24 (Fresh Review)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性)\n**圆桌轮次**: 1 轮初审 + 1 轮交叉分享，关键问题达成共识\n\n---\n\n## Summary\n\n本文用 forward KL divergence + Gumbel-Sigmoid 松弛训练 SwiGLU LLM 的上下文稀疏预测器（75.9M 参数，<1% base），替代传统 BCE per-neuron 独立目标。在 LLaMA-3.1-8B 上，KL predictor 在 30%/50% 稀疏度下分别降低 TEAL 的 PPL 14.5%/50%，且无需额外补偿网络（-67.2M params）。论文通过 C1 target-swap ablation 和 per-layer KL 控制实验分解了 signal type 与 coupling scope 的贡献，并提供梯度分析和 2D taxonomy 组织现有方法。定位为经验研究。\n\n---\n\n## Strengths\n\n**S1. 核心效应量大且跨架构稳健** [AGREE: R1, R2]\nKL vs BCE/TEAL 的 PPL 差距在 30%（8.81 vs 11.25/10.82）和 50%（11.84 vs 28.13/23.90）均超过 25%，3-seed 方差极低（σ=0.02 at 30%）。跨架构验证（Mistral-7B -17.3%, Qwen-14B consistent PPL advantage）确认不是架构特异现象。\n\n**S2. C1 target-swap ablation 是精巧的实验设计** [AGREE: R1, R2]\n用 KL 发现的 mask 训练 BCE predictor，分离 mask 质量 vs 训练动态的贡献（PPL within 0.79pp at 50%, s42；3-seed at 30% gap ≤1.70pp）。这一分析在稀疏性预测文献中是新颖的。\n\n**S3. 消融覆盖广泛且控制严格** [R1]\nTable 4 系统比较 5 种 loss（Forward KL, Reverse KL, JSD, MSE, BCE）× 2 种 relaxation（Gumbel, STE），MSE baseline 除 loss 外完全一致（Appendix G）。附录提供 d_b sensitivity、temperature schedule、training convergence、compensation redundancy 完整 robustness picture。\n\n**S4. 梯度分析提供有价值的理论直觉** [AGREE: R1, R2]\n§3.6 清晰展示 BCE gradient 仅依赖 neuron j，而 KL gradient 通过 downstream Jacobian 耦合所有 neuron——解释了 KL 为何能发现 composition-aware mask patterns。\n\n**S5. 自我定位诚实** [AGREE: R1, R2]\n论文自称 \"primarily an empirical study\"，始终保持定位。Limitations 覆盖 seq length、batched inference、知识任务退步等。\n\n**S6. Predictor 高效且训练成本低** [R2]\n75.9M params (<1% base)，45 min 单 GPU 训练，消除 67.2M 补偿网络。\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**C1. Per-layer KL 分解存在根本性 confound，定量声明不可靠** [AGREE: R1-N1, R2 cross-AGREE]\n\nK=1 控制实验存在 32× train-inference mismatch（训练 mask 1/32 层，推理 mask 全部 32 层）。论文标注 \"upper bound\" 但 Abstract/Conclusion 仍将 \"signal type accounts for the majority of the PPL gap\" 作为核心贡献呈现，资格限定传达不足。\n\nK=4 在 50% 下反常差于 K=1（PPL 44.23 vs 34.85），与 \"K 越大越接近 E2E\" 的直觉矛盾，缺乏机制解释。K=4 在 30% MMLU 超过 E2E（42.7 vs 40.7），混入 allocation 效应。仅两个数据点（K=1, K=4）不足以支撑 \"29-97% on downstream tasks\" 的精确分解。\n\n**重要补充**：定性结论（signal type matters）仍由梯度分析（§3.6）和 Table 4 的 5-loss 对比独立支撑，不完全依赖 per-layer 分解。被削弱的是精确的定量百分比，而非方向性结论。\n\n**C2. 知识密集型任务系统性退步缺乏机制分析** [AGREE: R1-N2, R2 cross-AGREE]\n\nKL 在所有测试规模和架构上均系统性低于 TEAL 的 MMLU/GSM8K：\n- 8B 30%: MMLU -5.2pp (40.7 vs 45.86)\n- 8B 30% global: MMLU -10.2pp (35.7 vs 45.86), σ=9.5\n- 14B 30% uniform: MMLU -2.8pp, GSM8K -20.1pp\n\n§4.4 的 Remove valley (MMLU +3.4pp) 方向正确，但未回答核心问题：为什么 KL 的 output-distribution 目标系统性学到牺牲知识路径的 allocation pattern？是 WikiText-103 训练分布的偏差？是 forward KL mode-covering 的固有特性？还是 Gumbel-Sigmoid 的采样偏差？对于自称 \"characterize how training objective shapes sparsity prediction quality\" 的论文，这是核心分析空白。\n\n### Should-Fix (Warning)\n\n**W1. 无 wall-clock speedup** [AGREE: R1, R2]\nPredictor 增加 6.4% latency overhead，unstructured masks 无法实现实际加速。论文定位为 empirical study 已适当 frame，但实际影响力受限。\n\n**W2. C1 ablation 存在残余 confound** [AGREE: R1-W1, R2 cross-AGREE]\nC1 同时改变训练目标（KL→BCE）和 mask 表示（soft Gumbel → hard binary）。Oracle 二值化（logits > 0）丢失排序信息。定性结论（mask patterns transfer quality, PPL within 0.79pp）因 gap 小而稳健，精确量化不可靠。\n\n**W3. 评估覆盖度存在关键空白** [AGREE: R1-W3, R2 cross-AGREE]\n无生成任务评估（MT-Bench, AlpacaEval）；序列长度固定 2048；batched inference 未评估。Sparsity 对 autoregressive generation 和长序列的行为可能与 PPL/MC-style tasks 显著不同。\n\n**W4. 高方差下游指标的统计可靠性不足** [AGREE: R1-W4, R2 cross-AGREE]\nARC-c σ=3.6pp（3-seed 95% CI ≈ ±8.9pp），BoolQ σ=11.5pp，使得这些指标的均值差异统计不显著。Table 4 多行仅 s42 单 seed。PPL（primary metric）方差极低（σ=0.02-0.15），结论可靠。\n\n**W5. 跨架构/跨规模泛化证据不足** [R2-N3 降级, R1 AGREE at warning level]\n核心实验全部基于 LLaMA-3.1-8B。Mistral-7B 和 Qwen-14B 仅有 main results，无 C1 ablation 或 per-layer 分解。论文已 acknowledge (\"evaluation bounded at 7-14B\")，但 \"dominant design dimension\" 声明隐含通用性。\n\n**W6. \"Dominant design dimension\" 声明需资格限定** [Derived from C1 confound]\n该声明的定量基础因 per-layer 分解 confound 不可靠。定性方向由 Table 4 五种 loss 对比和梯度分析支撑，但 \"dominant\" 措辞过强。建议软化为 \"output-distribution alignment substantially outperforms per-neuron classification and intermediate losses\"。\n\n### Minor\n\n- Figure 2 y 轴和图例文字偏小（~6-7pt），接近可读性下限（视觉审查 Warning）\n- Geometric penalty schedule 实际稀疏度 28.5% vs 名义 30%，Table 2 ‡ 标注存在但不够醒目\n- Table 2 中 BCE 30% 使用 global allocation（脚注 †），无 BCE 30% uniform 对比\n- 无代码/数据/模型释放声明\n- Introduction 中与 MaskLLM 的关系应更早建立（当前仅在 Related Work）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **KL vs BCE/TEAL 的 PPL 优势大、稳健、跨架构一致**——核心发现可靠，不是边界效应\n2. **C1 target-swap ablation 是新颖且有价值的实验设计**——在稀疏性预测文献中前所未见\n3. **Per-layer KL 分解的 confound 削弱定量声明**——\"29-97%\" 精确分解不可靠，但定性方向（signal type matters）独立成立\n4. **知识密集型任务退步是实际影响力的主要限制**——缺乏机制分析\n5. **无 wall-clock speedup 限制了实用价值**——论文 framing 诚实\n6. **论文定位诚实、消融全面、写作透明**——高于平均水平\n\n## Reviewer Divergence\n\n**R2-N1 (MaskLLM 新颖性)**：R2 判定 Critical（\"仅1句话讨论 MaskLLM\"），R1 REBUT（实际4句话，contextual vs static 是 fundamentally different learning problems）。\n→ **Director 判定**：R1 factual correction 成立。MaskLLM 区分已有基本讨论，contextual activation sparsity vs static N:M weight sparsity 确是不同学习问题。**降级为 Warning**（Introduction framing 可改善，非 novelty 缺失）。\n\n**R2-N2 (\"Dominant\" overclaimed)**：R2 判定 Critical（\"仅比较两种方法\"），R1 REBUT（Table 4 已对比 5 种 loss：Forward KL, Reverse KL, JSD, MSE, BCE）。\n→ **Director 判定**：R2 断言为**事实性错误**——Table 4 明确包含 5 种 loss function 的系统对比。但 \"dominant\" 声明仍因 per-layer 分解 confound 需资格限定。**降级为 Warning**（合并入 W6）。\n\n**R2-W4 (Gumbel confound)**：R2 判定 Warning（\"KL 和 Gumbel 贡献未 disentangle\"），R1 REBUT（BCE+Gumbel 反而恶化性能；loss effect 5.1× relaxation effect；MSE 使用相同 Gumbel）。\n→ **Director 判定**：R1 证据充分，confound 已被论文充分控制。**降级为 Info**。\n\n**R2 遗漏相关工作**：R2 列出 SparseInfer 和 TurboSparse 为遗漏引用——R1 指出两篇均已在 Section 2 引用。**R2 在此处阅读不够仔细。**\n\n---\n\n## Questions\n\n1. K=4 在 50% 下为何比 K=1 差？是否有 gradient interference 或 optimization landscape 解释？增加 K 是否单调恶化？\n2. 知识密集型退步是否与 WikiText-103 训练数据分布有关？用含 math/code 的混合语料训练是否缓解？\n3. C1 oracle 提取使用 logits > 0 二值化——是否尝试保留连续分数作为 soft label？\n4. STE 在 30% 仅达 20.8% effective sparsity——是否调整过 learning rate 或 gradient scaling？\n5. MSE 30% 3-seed mean 18.52±1.68 是否包含所有 3 个 seed（含可能的失败 seed）？\n\n---\n\n## Missing References\n\n- **Meng et al., 2022** \"Locating and Editing Factual Associations in GPT\" — 与知识密集型退步的分析直接相关 [AGREE: R1, R2]\n- **GRASP** (Group-Based Prediction of Activation Sparsity, DAC 2025) [R2]\n- Li et al., 2023 \"Inference with Reference: Lossless Acceleration of Large Language Models\" [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 完成（2026-05-22，耗时 ~3 min）\n\n- **Critical**: 0\n- **Warning**: 1 — Figure 2 的 y 轴标签和图例文字字号偏小（~6-7pt），打印时可能不够清晰\n- **Info**: 18 — 整体排版专业整洁。Figure 1 出现在 p2（首个 display item，位置合理）。所有表格 booktabs 风格，格式一致。主正文 8 页符合 EMNLP 限制。Appendix 内容密度高但排版整齐。无未解析引用。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 — Findings (可被 Findings 接收)**\n\n**置信度: 4/5**\n\n### 评分理由\n\n核心发现（KL 显著优于 BCE/TEAL 用于稀疏预测训练）可靠、效应量大、跨架构一致。C1 target-swap ablation 和梯度分析是有价值的分析性贡献。\n\n**Conference (4.0) 的主要障碍**：\n1. Per-layer 分解是三大贡献之一，但因 train-inference mismatch confound 和 K=4 反常结果，定量声明（\"29-97%\"）不可靠——需补充更多 K 值数据或降级为定性讨论\n2. 知识密集型任务系统性退步（8B MMLU -5.2pp, 14B GSM8K -20pp）缺乏机制分析——对于自称 \"characterize how training objective shapes quality\" 的论文，这是核心分析空白\n3. 无实际 wall-clock speedup，方法当前无部署价值\n\n**Findings (3.0) 的支撑理由**：\n- KL vs BCE 的核心比较稳健（多 seed、多架构、多稀疏度），实证发现有实际参考价值\n- C1 ablation 提供了 sparsity prediction 文献中前所未见的分析角度\n- 5 种 loss 的系统消融（Table 4）为后续工作提供设计指导\n- 消融全面、写作透明、自我定位诚实\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 第 5-6 句的 signal type / coupling scope 分解数字应进一步软化或删除精确百分比（\"upper bound\" 资格限定传达不足）\n- \"wall-clock speedup requires sparse kernel support not addressed here\" 和 \"primarily an empirical study\" 是重要的 honest disclaimers，应保留\n\n### Introduction (§1)\n- 与 MaskLLM 的关系应在 Introduction 更早建立——当前仅在 Related Work 讨论，读者在 Introduction 即会产生 \"this is MaskLLM for activation sparsity\" 的疑问\n- 贡献 bullet 1 的 \"29-97%\" 分解数字应降级为定性范围\n- \"This paper is primarily an empirical study\" 的定位声明是正确的策略选择\n\n### Method (§3)\n- §3.3 Gumbel-Sigmoid 设计选择论证充分，BCE+Gumbel 恶化性能的发现（Table 4）有效排除了 Gumbel 单独解释 KL 优势的假说\n- §3.5 geometric penalty 的 deadzone ε=0.02 justification 可简短补充 sensitivity 引用\n- §3.6 梯度分析是论文最有价值的部分——但应增加 caveat：coupled gradient 是发现好 mask 的充分条件还是必要条件？C1 结果暗示 coupling 不是推理阶段的必要条件\n\n### Experiments (§4)\n- Table 2：BCE 30% 使用 global allocation（脚注 †），建议补充 BCE 30% uniform 对比或说明省略原因\n- Table 2：实际稀疏度 ‡ 标注可更醒目\n- §4.5 Per-layer KL：需补充 K=8/K=16 或删除精确百分比；K=4 50% 反常结果需假设性解释\n- §4.4 Remove valley MMLU +3.4pp：应追问 \"why KL learns this pattern\" 而不仅是 \"what happens if we override it\"\n- Table 4 核心行（Forward KL + Gumbel, BCE）的 30% 数据应补充 3-seed\n\n### Limitations\n- 覆盖三个核心点，篇幅适当（符合 EMNLP 要求）\n- 建议加入 \"生成任务（open-ended generation）未评估\" 作为第四点\n\n### Ethics Statement\n- 覆盖数据来源、计算成本、安全性，内容适当",
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings"
  }
}
```

</details>

---


### Tool result

_source line 1947 · 2026-05-23T00:00:00.889325+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4172
}
```

</details>

---


### Assistant

_source line 1948 · 2026-05-23T00:00:12.990165+00:00_

审稿报告已投递至 Research Director。

**审稿圆桌会议总结**：

- **Overall: 3.0/5 — Findings**
- **2 个 Critical**：(1) Per-layer KL 分解存在 train-inference mismatch confound，"29-97%" 定量声明不可靠；(2) 知识密集型任务系统性退步缺乏机制分析
- **6 个 Warning**：无 wall-clock speedup、C1 残余 confound、评估覆盖度空白、高方差指标统计可靠性、跨规模泛化不足、"dominant" 措辞需软化
- **交叉分享纠正**：R2 的两个 Critical（"仅两种方法对比"、"Gumbel confound"）被 R1 以事实性证据 REBUT 并降级；R2 遗漏引用列表中两篇已被论文引用
- **核心共识**：KL vs BCE 的 PPL 优势大且稳健，C1 ablation 设计精巧，论文定位诚实——适合 Findings 而非 Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 166

## Round 166

2 recorded events


### User

_source line 1949 · 2026-05-23T00:00:15.571900+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **R1-N1 (per-layer KL decomposition confound)**: [AGREE] — 32× train-inference mismatch 是真实 confound，K=4 anomaly 未解释，"29-97%" 精确分解证据不足。但补充指出 §3.6 梯度分析和 C1 ablation 提供了独立于该 decomposition 的 signal type 重要性证据。
- **R1-N2 (知识密集型退步)**: [AGREE] — 跨架构系统性退步缺乏机制解释，"sacrifice reasoning-critical pathways" 是事后叙事。
- **R1-W1 (C1 confound)**: [AGREE] — soft→hard 变化引入混淆，但定性结论（0.79pp gap）仍稳健。
- **R1-W2 (无 wall-clock)**: [AGREE]
- **R1-W3 (评估空白)**: [AGREE] — 无生成任务、固定序列长度、无 batched inference 均为真实缺失。
- **R1-W4 (高方差)**: [AGREE] — PPL 可靠但 downstream tasks（ARC-c, BoolQ）方差过大。
- **R1-W5 (geometric penalty 偏差)**: [REBUT] — 1.5pp 偏差属正常范围且 Appendix C 有详细报告，但同意 Table 2 labeling 应更精确。建议降级为 minor。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1950 · 2026-05-23T00:00:33.177393+00:00_

审稿报告已投递至 Research Director。

**审稿圆桌会议总结**：

- **Overall: 3.0 / 5 — Findings**
- **流程**: 2 名 Reviewer × 1 轮初审 + 1 轮交叉分享，关键问题达成共识
- **2 个 Critical**: (1) Per-layer KL 分解 confound 削弱定量声明；(2) 知识任务退步缺机制分析
- **6 个 Warning**: 无 wall-clock speedup、C1 残余 confound、评估空白、高方差指标、泛化证据不足、"dominant" 声明需软化
- **交叉分享纠正**: R2 的两项 Critical（"仅两种 loss 对比"、"Gumbel confound"）被 R1 以事实证据 REBUT 并降级
- **视觉审查**: 完成，1 Warning（Figure 2 字号偏小），整体排版专业
- **Issue Tracker**: 已同步更新 review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 167

## Round 167

56 recorded events


### User

_source line 1951 · 2026-05-23T00:31:40.671050+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1952 · 2026-05-23T00:31:45.896179+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1953 · 2026-05-23T00:31:45.947379+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1954 · 2026-05-23T00:31:54.529496+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1955 · 2026-05-23T00:31:54.580147+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1956 · 2026-05-23T00:31:57.995234+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1957 · 2026-05-23T00:31:57.995574+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1958 · 2026-05-23T00:32:01.810048+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1959 · 2026-05-23T00:32:01.810384+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1960 · 2026-05-23T00:32:04.157856+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1961 · 2026-05-23T00:32:04.209193+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1962 · 2026-05-23T00:32:10.231907+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1963 · 2026-05-23T00:32:11.637511+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (378 个)\n\n- **eval_spon_supp_retry**: DONE (failed) — \n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n- Worker `paper_r24_writing_fixes` (CPU): 执行 R24 全部写作修复（2C+6W+Minor），等回调\n\n## 待处理\n- Worker 回调到 → 检查论文编译 + 8 页 → 提交 review（continue mode）\n- DDL 2026-05-25 EMNLP 2026 ARR May cycle（剩 2 天）\n\n## 近期完成\n- **qwen14b_kl30_s42_gsm8k_uniform** (success): Qwen-14B KL 30% GSM8K uniform → **GSM8K=35.48%**\n- **perlayer_kl_50_s42_downstream** (negative): Per-layer KL 50% 6-task → 近随机水平，强化 2D decomposition\n- **perlayer_kl_k4_s123/s456** (done): K=4 3-seed downstream 完成，ARC-c 97% coupling\n- **constraint_protect_late/remove_valley** (done): 双向 constraint 实验完成\n\n## R24 修复状态（全部写作，无需实验）\n- [ ] C1: 删除 \"29-97%\" 精确分解 → 定性描述 + K=4 50% 反常假设\n- [ ] C2: §4.2 补 MMLU/GSM8K 退步机制假设\n- [ ] W1-W5: Limitations 生成任务、高方差 caveat、soft→hard confound、dominant 软化、MaskLLM 区分\n- [ ] Minor: 代码释放声明、missing refs\n- [ ] 编译检查 8 页\n\n## 资源状态\n- westd-34887: cuda:0,1 空闲（2× RTX PRO 6000 96GB）— D104 无新实验\n- westd-41718: 已由用户释放\n- Worker 池: 1 (paper fixes)\n\n## 下一步\n1. Paper Worker 回调 → 验证修复 → 编译检查\n2. 提交 review（continue mode）→ R25\n3. R25 通过 → 最终版本提交"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 1964 · 2026-05-23T00:32:11.788498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1965 · 2026-05-23T00:32:12.591542+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	\input{limitations}
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1966 · 2026-05-23T00:32:12.742663+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1967 · 2026-05-23T00:32:13.545619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1968 · 2026-05-23T00:32:14.499687+00:00_

1	issues:
2	  # ============================================================
3	  # Round 24 (Fresh Review) — Active issues
4	  # ============================================================
5	
6	  - id: "R20-W1"
7	    summary: "Per-layer KL decomposition 的 train-inference mismatch confound 未解决"
8	    category: method
9	    severity: critical
10	    status: in_progress
11	    first_raised_round: 20
12	    last_seen_round: 24
13	    mentions:
14	      - {round: 21, reviewers: [1, 2], note: "R21 Critical。K=4 single-seed。"}
15	      - {round: 22, reviewers: [1, 2], note: "R22 N2。97.5% 精确数字不可靠。"}
16	      - {round: 24, reviewers: [1, 2], note: "R24 C1。K=1 有 32× train-inference mismatch；K=4 在 50% 反常差于 K=1 (44.23 vs 34.85) 缺乏机制解释；仅两个 K 值不足以支撑 29-97% 精确分解。定性结论（signal type matters）由 Table 4 五种 loss 对比和梯度分析独立支撑。"}
17	    action_items:
18	      - {round: 21, action: "K=4 3-seed (s42/s123/s456)", assigned_to: "main_agent", status: done}
19	      - {round: 22, action: "97.5% → 定性 'majority of PPL gap'", assigned_to: "paper_agent", status: done}
20	      - {round: 22, action: "K=4 50% s42 PPL-only 实验", assigned_to: "main_agent", status: done}
21	      - {round: 24, action: "Abstract/Conclusion 的 decomposition claim 删除精确百分比改为定性描述", assigned_to: "paper_agent", status: in_progress}
22	      - {round: 24, action: "K=8/K=16 实验不做（D104: DDL不允许），改为移除定量分解框架", assigned_to: "paper_agent", status: in_progress}
23	      - {round: 24, action: "K=4 50% 反常结果补假设性解释（gradient interference at high sparsity）", assigned_to: "paper_agent", status: in_progress}
24	    resolution: ""
25	    resolution_round: null
26	
27	  - id: "R20-N2"
28	    summary: "MMLU/GSM8K 跨架构系统性退步缺乏机制分析"
29	    category: experiment
30	    severity: critical
31	    status: in_progress
32	    first_raised_round: 18
33	    last_seen_round: 24
34	    mentions:
35	      - {round: 21, reviewers: [1, 2], note: "R21 Critical。Protection valley 分析仅 correlational。"}
36	      - {round: 22, reviewers: [1, 2], note: "R22 N3。要求追踪 Remove Valley
…[truncated 13184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1969 · 2026-05-23T00:32:14.702184+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1970 · 2026-05-23T00:32:14.904851+00:00_

-rw-r--r-- 1 ubuntu ubuntu 541390 May 23 00:30 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool result

_source line 1971 · 2026-05-23T00:32:28.060767+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"The 14th Joint Conference on Lexical and Computational Semantics | ACL Member Portal","url":"https://www.aclweb.org/portal/content/14th-joint-conference-lexical-and-computational-semantics"},{"title":"ACL Policy on Publication Ethics - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policy_on_Publication_Ethics"},{"title":"EACL 2026 - Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-call-system-demonstrations"}]

I found relevant information about ACL Rolling Review (ARR) and 2026 submission guidelines. Here's what the search results show:

## ARR Submission Guidelines

ACL Rolling Review (ARR) invites the submission of long and short papers on substantial, original, and unpublished research in all aspects of Computational Linguistics and Natural Language Processing.

## Paper Format and Templates

Paper submissions must use the official ACL style templates, which are available as an Overleaf template and can also be downloaded directly via https://aclrollingreview.org/cfp under 'Paper Submission Process, Criteria and Templates'. All sub
…[truncated 852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 15318
}
```

</details>

---


### Tool call

_source line 1972 · 2026-05-23T00:32:34.530884+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 1973 · 2026-05-23T00:32:34.531339+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 submission deadline dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 submission deadline dates"
  }
}
```

</details>

---


### Tool result

_source line 1974 · 2026-05-23T00:32:39.298359+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 submission deadline dates"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR 2026 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMay"}]

Based on the search results, I found information about ACL Rolling Review (ARR) submission deadlines. However, the search results don't contain the complete specific details for the May 2026 submission cycle. Here's what I can tell you:

ARR switched to 10-week review cycles starting in May 2025, which means the schedule has changed from the previous 8-week cycles.

The search results reference that there is an ACL ARR 2026 May cycle on OpenReview, but the specific deadline dates for May 2026 submissions are not clear
…[truncated 644 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 4767
}
```

</details>

---


### Tool result

_source line 1975 · 2026-05-23T00:32:40.001254+00:00_

Web search results for query: "EMNLP 2026 submission guidelines page limit format requirements"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"}]

Based on the search results, I found submission guidelines information for EMNLP 2026. Here are the key page limit and format requirements:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

For the Industry Track specifically, authors are invited to submit original, full-length (maximum of 6 pages) industry track papers.

## Format Requirements

Manuscripts should be submitted electronically, in PDF format and formatted using the templates available on the conference website. Please do not modify these style files, nor should you use templates desi
…[truncated 637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 5470
}
```

</details>

---


### Tool call

_source line 1976 · 2026-05-23T00:32:50.037954+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1977 · 2026-05-23T00:32:50.339469+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (max $\Delta$$\leq$0.79pp, 3-seed).
5	Signal type (output-distribution vs.\ intermediate loss) accounts for the majority of the PPL gap at 30\% (upper bound; not fully orthogonal with coupling scope).
6	On downstream tasks, cross-layer coupling contributes substantially for commonsense reasoning but minimally for mathematical reasoning (3-seed $K{=}4$-corrected decomposition).
7	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
8	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1978 · 2026-05-23T00:32:50.339824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1979 · 2026-05-23T00:32:50.390341+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	Unlike MaskLLM~\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation suggests that KL-discovered mask targets carry most of the quality information at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.20. Cross-
…[truncated 2908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1980 · 2026-05-23T00:32:50.842391+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1981 · 2026-05-23T00:32:51.294339+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importan
…[truncated 9554 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1982 · 2026-05-23T00:32:51.294840+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1983 · 2026-05-23T00:32:52.298721+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 1984 · 2026-05-23T00:32:52.349357+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1985 · 2026-05-23T00:32:52.751427+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} and GRASP~\cite{shin2025grasp} predict activation sparsity patterns without additional training.
6	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
7	Wang et al.~\cite{wang2025dynamicsparse} address dynamic sparsity--quantization interaction; AWQ~\cite{lin2024awq} applies activation-aware weight quantization for on-device deployment; Outlier Suppression+~\cite{wei2023outlier} mitigates outlier-induced quantization errors via shifting and scaling.
8	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
9	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
10	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
11	
12	\paragraph{Predictor-Based Contextual Sparsity.}
13	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
14	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
15	FastForward~\cite{gautam2026fastforward} adds a
…[truncated 5177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1986 · 2026-05-23T00:32:52.751945+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1987 · 2026-05-23T00:32:52.802496+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the primary design dimension for PPL (signal type accounts for the majority of the gap; upper bound); cross-layer coupling contributes task-dependently---substantially for commonsense, marginally for reasoning (3-seed $K{=}4$-corrected; Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A predictor ($<$1\% of base) reduces TEAL's PPL by 14.5\% via masks 46--68\% divergent from magnitude, with commonsense gains but knowledge-task regression across scales.
6	Limitations: MMLU/GSM8K decline, no wall-clock speedup, evaluation bounded at 7--14B.
7	Code and trained predictors will be released upon acceptance.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1988 · 2026-05-23T00:32:53.254576+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1989 · 2026-05-23T00:32:53.706682+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated. All experiments use sequence length 2048; behavior at longer contexts (e.g., 8K--128K) is untested. Our evaluation focuses on perplexity and multiple-choice benchmarks; open-ended generation quality (e.g., MT-Bench) remains untested and may exhibit different sparsity sensitivity. Evaluation is limited to 7--14B; scaling to 70B+ and wall-clock speedup via sparse kernels remain future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1990 · 2026-05-23T00:32:53.707150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1991 · 2026-05-23T00:32:54.009017+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1992 · 2026-05-23T00:32:54.009387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1993 · 2026-05-23T00:32:54.311217+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 36747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1994 · 2026-05-23T00:33:01.135463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": "598"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "offset": "598"
  }
}
```

</details>

---


### Tool result

_source line 1995 · 2026-05-23T00:33:01.487165+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (598). The file has 598 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1996 · 2026-05-23T00:33:01.487573+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1997 · 2026-05-23T00:33:02.340669+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (378 个)\n\n- **eval_spon_supp_retry**: DONE (failed) — \n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n- Worker `paper_r24_writing_fixes` (CPU): 执行 R24 全部写作修复（2C+6W+Minor），等回调\n\n## 待处理\n- Worker 回调到 → 检查论文编译 + 8 页 → 提交 review（continue mode）\n- DDL 2026-05-25 EMNLP 2026 ARR May cycle（剩 2 天）\n\n## 近期完成\n- **qwen14b_kl30_s42_gsm8k_uniform** (success): Qwen-14B KL 30% GSM8K uniform → **GSM8K=35.48%**\n- **perlayer_kl_50_s42_downstream** (negative): Per-layer KL 50% 6-task → 近随机水平，强化 2D decomposition\n- **perlayer_kl_k4_s123/s456** (done): K=4 3-seed downstream 完成，ARC-c 97% coupling\n- **constraint_protect_late/remove_valley** (done): 双向 constraint 实验完成\n\n## R24 修复状态（全部写作，无需实验）\n- [ ] C1: 删除 \"29-97%\" 精确分解 → 定性描述 + K=4 50% 反常假设\n- [ ] C2: §4.2 补 MMLU/GSM8K 退步机制假设\n- [ ] W1-W5: Limitations 生成任务、高方差 caveat、soft→hard confound、dominant 软化、MaskLLM 区分\n- [ ] Minor: 代码释放声明、missing refs\n- [ ] 编译检查 8 页\n\n## 资源状态\n- westd-34887: cuda:0,1 空闲（2× RTX PRO 6000 96GB）— D104 无新实验\n- westd-41718: 已由用户释放\n- Worker 池: 1 (paper fixes)\n\n## 下一步\n1. Paper Worker 回调 → 验证修复 → 编译检查\n2. 提交 review（continue mode）→ R25\n3. R25 通过 → 最终版本提交"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1998 · 2026-05-23T00:33:39.711711+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool call

_source line 1999 · 2026-05-23T00:33:40.213805+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2000 · 2026-05-23T00:34:02.548057+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22836
}
```

</details>

---


### Tool result

_source line 2001 · 2026-05-23T00:34:02.548544+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 22334
}
```

</details>

---


### Tool call

_source line 2002 · 2026-05-23T00:34:02.699538+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long paper，8 页正文限制（不含 references/limitations/ethics），ACL 模板 (acl.sty)\n- **匿名规则**: Double-blind\n- **评分标准**: ARR Overall Assessment 1-5 分（4=Conference，3.5=Borderline Conference，3=Findings）\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- 各章节: 同目录下 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex\n\n## 你的审查侧重\n\n### 1. 方法论严谨性\n- KL divergence 公式（forward KL 选择的理论依据是否充分）\n- Gumbel-Sigmoid relaxation 的数学推导是否正确\n- Geometric Penalty Schedule 是否是合理的 sparsity 控制方案\n- §3.6 梯度分析——BCE vs KL 对比是否公正、严谨\n\n### 2. 实验设计\n- 控制变量是否充分（KL vs BCE vs MSE 的 fair comparison：同架构、同数据、同步数）\n- 统计显著性：哪些结果是 3-seed，哪些仅 s42？confidence interval 是否足够窄？\n- Per-layer KL 分解（§4.5 \"Per-Layer KL: Decomposing Signal Type and Coupling Scope\"）——K=1 的 32x train-inference mismatch confound 是否被充分讨论？K=4 是否真正 deconfound？\n- C1 target-swap ablation（§4.3）——soft→hard 二值化是否引入了额外 confound？oracle mask 来自单一训练轨迹是否是问题？\n- Cross-architecture（Mistral-7B, Qwen-14B）——14B 仅单 seed 是否足够？GSM8K -20pp 是否被充分分析？\n\n### 3. 关键数字审计\n- Table 1 main results：检查 PPL 和 downstream 数字是否自洽\n- Table 3 C1 ablation：max Δ≤0.79pp 的声明是否被数据支持（注意 30% s42 gap=0.65pp 但使用了不同 checkpoint）\n- Table 4 ablation：检查 Δ 列计算\n- TEAL baseline 的公平性：TEAL 是 deterministic 的，但 actual sparsity 不同（28.5% vs 29.3%），matched comparison 是否充分\n\n### 4. 可复现性\n- 训练细节是否足够（lr, optimizer, batch size, seq_len 都有）\n- 代码是否承诺释放？\n- 硬件描述是否充分\n\n请按 ARR 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment（含评分和置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long paper，8 页正文限制（不含 references/limitations/ethics），ACL 模板 (acl.sty)\n- **匿名规则**: Double-blind\n- **评分标准**: ARR Overall Assessment 1-5 分（4=Conference，3.5=Borderline Conference，3=Findings）\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- 各章节: 同目录下 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex\n\n## 你的审查侧重\n\n### 1. 方法论严谨性\n- KL divergence 公式（forward KL 选择的理论依据是否充分）\n- Gumbel-Sigmoid relaxation 的数学推导是否正确\n- Geometric Penalty Schedule 是否是合理的 sparsity 控制方案\n- §3.6 梯度分析——BCE vs KL 对比是否公正、严谨\n\n### 2. 实验设计\n- 控制变量是否充分（KL vs BCE vs MSE 的 fair comparison：同架构、同数据、同步数）\n- 统计显著性：哪些结果是 3-seed，哪些仅 s42？confidence interval 是否足够窄？\n- Per-layer KL 分解（§4.5 \"Per-Layer KL: Decomposing Signal Type and Coupling Scope\"）——K=1 的 32x train-inference mismatch confound 是否被充分讨论？K=4 是否真正 deconfound？\n- C1 target-swap ablation（§4.3）——soft→hard 二值化是否引入了额外 confound？oracle mask 来自单一训练轨迹是否是问题？\n- Cross-architecture（Mistral-7B, Qwen-14B）——14B 仅单 seed 是否足够？GSM8K -20pp 是否被充分分析？\n\n### 3. 关键数字审计\n- Table 1 main results：检查 PPL 和 downstream 数字是否自洽\n- Table 3 C1 ablation：max Δ≤0.79pp 的声明是否被数据支持（注意 30% s42 gap=0.65pp 但使用了不同 checkpoint）\n- Table 4 ablation：检查 Δ 列计算\n- TEAL baseline 的公平性：TEAL 是 deterministic 的，但 actual sparsity 不同（28.5% vs 29.3%），matched comparison 是否充分\n\n### 4. 可复现性\n- 训练细节是否足够（lr, optimizer, batch size, seq_len 都有）\n- 代码是否承诺释放？\n- 硬件描述是否充分\n\n请按 ARR 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 2003 · 2026-05-23T00:34:25.192180+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22492
}
```

</details>

---


### Tool call

_source line 2004 · 2026-05-23T00:34:25.393246+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long paper，8 页正文限制（不含 references/limitations/ethics），ACL 模板 (acl.sty)\n- **匿名规则**: Double-blind\n- **评分标准**: ARR Overall Assessment 1-5 分（4=Conference，3.5=Borderline Conference，3=Findings）\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- 各章节: 同目录下 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 核心贡献是什么？是将 KL distillation 应用到 activation sparsity prediction——这与 MaskLLM（KL + static N:M weight masks）有多大区别？\n- MaskLLM 三点区分（§2 Related Work）是否有说服力：(a) contextual vs static, (b) cross-layer allocation, (c) distribution shift robustness\n- \"2D taxonomy\"（Table 2）是否真的组织了 prior work，还是为了制造 novelty？\n- Target-swap ablation（C1）和 per-layer KL decomposition 作为分析贡献是否足够新颖？\n- 与 DejaVu、FastForward、ShadowLLM、D2DMoE 的 positioning 是否准确\n\n### 2. 完整性\n- 评估覆盖度：PPL + 6 个下游任务够吗？是否缺少生成任务（MT-Bench, AlpacaEval）？\n- Seq length 固定 2048——是否覆盖了实际场景？\n- Batched inference 未评估——这对实际部署意味着什么？\n- 仅 7-14B 规模——是否足以支撑 general claims？\n- 训练数据仅 WikiText-103——OOD 泛化是否被充分验证（C4 evaluation 在 Appendix D）？\n\n### 3. 写作质量\n- Abstract 信息密度是否合理？8 句 abstract 是否 too dense？\n- Introduction 逻辑流是否清晰：problem → gap → approach → results → contributions\n- Claims 与 evidence 的匹配：特别注意 \"signal type accounts for the majority of the PPL gap\" 这个 claim 是否被 upper bound caveat 充分修饰\n- \"dominant design dimension\" / \"primary design dimension\" 等措辞是否过强\n- Conclusion 是否准确反映了论文发现（包括 limitations）\n- 术语一致性：检查全文术语使用是否统一\n- 数字引用准确性：正文中引用的数字是否与表格一致\n\n### 4. 格式合规\n- 页数检查：正文是否在 8 页内？\n- 匿名性：是否有 de-anonymizing 信息（代码链接、GPU 型号泄露身份、致谢等）\n- 参考文献格式：natbib, ACL .bst\n- Figure/Table 质量：字号是否可读（≥8pt），caption 是否 self-contained\n- Limitations 章节覆盖度\n\n### 5. Missing References\n- 检查是否遗漏了 2024-2026 年的重要相关工作\n- 特别注意：contextual sparsity prediction、KL distillation for pruning、SwiGLU sparsity 方向的新工作\n\n请按 ARR 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues → Missing References → Overall Assessment（含评分和置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long paper，8 页正文限制（不含 references/limitations/ethics），ACL 模板 (acl.sty)\n- **匿名规则**: Double-blind\n- **评分标准**: ARR Overall Assessment 1-5 分（4=Conference，3.5=Borderline Conference，3=Findings）\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- 各章节: 同目录下 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 核心贡献是什么？是将 KL distillation 应用到 activation sparsity prediction——这与 MaskLLM（KL + static N:M weight masks）有多大区别？\n- MaskLLM 三点区分（§2 Related Work）是否有说服力：(a) contextual vs static, (b) cross-layer allocation, (c) distribution shift robustness\n- \"2D taxonomy\"（Table 2）是否真的组织了 prior work，还是为了制造 novelty？\n- Target-swap ablation（C1）和 per-layer KL decomposition 作为分析贡献是否足够新颖？\n- 与 DejaVu、FastForward、ShadowLLM、D2DMoE 的 positioning 是否准确\n\n### 2. 完整性\n- 评估覆盖度：PPL + 6 个下游任务够吗？是否缺少生成任务（MT-Bench, AlpacaEval）？\n- Seq length 固定 2048——是否覆盖了实际场景？\n- Batched inference 未评估——这对实际部署意味着什么？\n- 仅 7-14B 规模——是否足以支撑 general claims？\n- 训练数据仅 WikiText-103——OOD 泛化是否被充分验证（C4 evaluation 在 Appendix D）？\n\n### 3. 写作质量\n- Abstract 信息密度是否合理？8 句 abstract 是否 too dense？\n- Introduction 逻辑流是否清晰：problem → gap → approach → results → contributions\n- Claims 与 evidence 的匹配：特别注意 \"signal type accounts for the majority of the PPL gap\" 这个 claim 是否被 upper bound caveat 充分修饰\n- \"dominant design dimension\" / \"primary design dimension\" 等措辞是否过强\n- Conclusion 是否准确反映了论文发现（包括 limitations）\n- 术语一致性：检查全文术语使用是否统一\n- 数字引用准确性：正文中引用的数字是否与表格一致\n\n### 4. 格式合规\n- 页数检查：正文是否在 8 页内？\n- 匿名性：是否有 de-anonymizing 信息（代码链接、GPU 型号泄露身份、致谢等）\n- 参考文献格式：natbib, ACL .bst\n- Figure/Table 质量：字号是否可读（≥8pt），caption 是否 self-contained\n- Limitations 章节覆盖度\n\n### 5. Missing References\n- 检查是否遗漏了 2024-2026 年的重要相关工作\n- 特别注意：contextual sparsity prediction、KL distillation for pruning、SwiGLU sparsity 方向的新工作\n\n请按 ARR 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues → Missing References → Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 2005 · 2026-05-23T00:34:26.802508+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1409
}
```

</details>

---


### Assistant

_source line 2006 · 2026-05-23T00:34:33.734330+00:00_

**Round 1 已启动**：
- Reviewer 1（方法严谨性 + 实验设计）：已派发
- Reviewer 2（新颖性 + 完整性 + 写作质量）：已派发
- 视觉审查 Agent：已启动
- 外部审稿：未配置，跳过

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 168

## Round 168

2 recorded events


### User

_source line 2007 · 2026-05-23T00:40:04.746268+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 (Borderline Conference)
**Soundness**: 3.5/5
**Excitement**: 3/5
**Confidence**: 4/5（仔细验证了所有关键数字和公式）

**一句话总结**: 扎实的实证研究，证明了 output-distribution alignment（forward KL）显著优于 per-neuron BCE 来训练 sparsity predictor，C1 target-swap ablation 设计巧妙；但系统性的 knowledge-task regression、coupling decomposition 的 confounds、以及缺乏 wall-clock speedup 限制了贡献。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | KL 公式正确，Gumbel-Sigmoid 标准，ablation 设计巧妙。但 coupling decomposition 有未解决的 confounds（K=4 anomaly），sparsity controller 在 30% target 饱和未达目标 |
| Excitement | 3/5 | 填补了 training objective for sparsity predictor 的文献空白，C1 ablation 有洞察力；但缺乏 wall-clock speedup 和系统性 knowledge regression 限制实际影响 |
| Reproducibility | 4/5 | 训练细节充分（lr, optimizer, batch size, seq_len, hardware），承诺 release code；但 seed 覆盖不完整（14B 单 seed） |
| Overall | 3.5/5 | 介于 Conference 和 Findings 之间；若能修复关键问题可达 Conference |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Per-layer KL K=4 在 50% sparsity 的反常行为削弱 coupling decomposition 的可信度

- 具体位置：§4.5 (Table 4, Per-layer KL K=4 行)
- 问题：K=4 per-layer KL 在 50% sparsity 的 PPL 为 44.23，**劣于** K=1 的 34.85，而 E2E KL 为 11.84。如果 coupling 是有益的，增加 masked layers 数量（K=1→K=4）应缩小与 E2E 的差距，但实际上差距扩大了（+23.06→+32.44）。论文给出的解释是 "gradient interference"（§4.5 倒数第二段），但这是纯粹的 speculation，没有任何实验验证。
- 为什么影响接收：该反常行为直接动摇了 §4.5 signal type vs. coupling scope decomposition 的核心叙事。如果 K=4 的行为无法被解释，那么基于 K=1 和 K=4 的 decomposition percentages（如 "PPL 67% closure"）的可靠性也存疑。论文的一个主要 contribution 是这个 decomposition，但它在更高 sparsity 下失效。
- 建议修改方向：(1) 增加 K=2, K=8, K=16 的实验以追踪 PPL 随 K 的变化趋势；(2) 或者限制 decomposition 分析仅在 30% sparsity 下声称有效，明确指出 50% 下 decomposition 失效；(3) 分析 K=4 at 50% 的 per-layer sparsity 分布，看是否存在 pathological allocation。

**N2** [critical] MMLU K=4 超过 E2E 的 anomaly 暴露 decomposition confound

- 具体位置：§4.5, Appendix S (Table in App S: MMLU K=4 = 42.7±1.4 vs E2E = 40.7±1.3)
- 问题：K=4 在 MMLU 上系统性超过 E2E（所有 3 个 seed），论文解释为 K=4 的 near-uniform per-layer sparsity（std=0.003）匹配了 uniform inference protocol。但这说明 K=4 control 无法独立地隔离 coupling 效应——它同时改变了 allocation pattern。因此 signal type vs. coupling 的百分比分解（Table in Appendix R）混淆了 coupling effect 和 allocation effect。
- 为什么影响接收：如果 decomposition 的两个维度不正交（论文自己承认 "dimensions not fully orthogonal"），那么 "signal type accounts for the majority of the PPL gap" 这一核心结论的 upper bound 性质需要更强的 caveat。目前论文在 abstract 和 conclusion 中反复强调此结论，但 caveat 仅在脚注中出现。
- 建议修改方向：(1) 在 main text（非仅 appendix 脚注）中明确讨论 allocation confound 对 decomposition 的影响；(2) 考虑在 K=4 实验中强制使用与 E2E 相同的 per-layer allocation pattern（而非 K=4 自然学出的 near-uniform），以真正隔离 coupling effect。

**N3** [critical] Qwen-2.5-14B 的 GSM8K -20pp regression 仅有单 seed 支撑

- 具体位置：§4.6 (Table in Appendix K: Qwen-14B uniform KL GSM8K = 32.0±5.2 vs TEAL = 52.1)
- 问题：GSM8K 从 52.1pp（TEAL）下降到 32.0pp（KL），降幅达 20pp，且标准差为 5.2pp（相对于均值 32.0 的 CV=16.3%）。论文在 §4.6 称这是 "systematic property of distribution-matching"，但 global allocation 行（Table in Appendix K）仅有 seed 42。3-seed 仅用于 uniform 的 GSM8K，而 global 的所有 6 个 metrics 均为单 seed。
- 为什么影响接收：-20pp GSM8K 是论文最大的负面结果之一。如果这个结果是 seed-dependent 的（14B global 没有 multi-seed 验证），那么 "knowledge-task regression scales with model size" 的结论可能不成立。单 seed 不足以支撑如此强的跨规模趋势声明。
- 建议修改方向：补充 Qwen-14B 至少 3-seed 评估，或者弱化跨规模趋势的措辞为 "preliminary observation"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 系统性 knowledge-task regression 缺乏机制分析

- 具体位置：§4.2 "Knowledge-Task Regression: Hypothesis" 段落
- 问题：KL 在所有规模和架构上一致性地 underperform TEAL 在 MMLU 和 GSM8K 上：8B MMLU -5.2pp, 14B GSM8K -20pp, Mistral GSM8K -7.3pp。论文提出两个假说（WikiText-103 数据偏差和 forward KL 的 mode-covering 稀释 rare activations），但两者均 "await validation via knowledge-neuron probing"。
- 建议：至少做一个简单验证：(1) 比较 KL 和 magnitude 在 knowledge-critical layers（如 L14-L18）的 neuron retention 差异；(2) 或者在 GSM8K 样本上计算 KL vs magnitude mask 的 per-layer Jaccard，看 divergence 是否在特定层更严重。Appendix T 的 constraint analysis（remove valley → MMLU +3.4pp）已经暗示了方向，可以更深入。

**W2** [warning] C1 ablation s42 oracle 来自不同 checkpoint

- 具体位置：Table 3 caption footnote "†s42 oracle is from an earlier training run"
- 问题：s42 的 C1 在 30% 时 PPL = 9.45（vs KL 8.80, gap 0.65pp），而 s123 和 s456 使用 matched retrained oracles 后 gap 降至 ≤0.03pp。这表明 s42 的 0.65pp gap 主要来自 oracle provenance mismatch，而非 target-swap 本身的效应。但 s42 是 Table 3 中最显眼的第一行数据。
- 建议：(1) 为 s42 补训 matched oracle 以消除 provenance confound；(2) 或在 Table 3 中将 s42 标记为 "oracle mismatch" 并优先展示 s123/s456 的结果。

**W3** [warning] BCE 30% 仅报告 global allocation，缺少 uniform 对比

- 具体位置：Table 1, BCE 30% 行标注 "BCE global†"
- 问题：KL 30% 有 global（8.96）和 uniform（8.81）两个配置，但 BCE 30% 仅有 global（11.25）。由于 KL 的 best 在 uniform（8.81），但 BCE 没有 uniform 数据，无法直接对比相同 allocation strategy 下 KL vs BCE 的差异。
- 建议：补充 BCE 30% uniform 数据，或解释为什么 BCE uniform 数据缺失。

**W4** [warning] Sparsity controller 在 30% target 饱和（λ=5000 cap）

- 具体位置：Appendix C, Table 9 第一行（30% target, λ_max=5000, Final λ=5000 cap, Actual sparsity=0.285）
- 问题：λ 饱和在 cap 意味着 controller 已尽最大努力仍无法达到 30% target（实际 28.5%，偏差 5%）。这是 geometric penalty schedule 的失败模式。虽然论文在 Appendix C 末尾说明 TEAL at 28.5% PPL=10.30 仍远不如 KL 8.81，但 systematic under-sparsification 意味着 KL 的 PPL 优势部分来自更低的实际 sparsity。
- 建议：(1) 在 main text 而非仅 appendix 中讨论这一偏差；(2) 为 main results 补充一个在 exactly matched actual sparsity 下的对比行。

**W5** [warning] 无 wall-clock speedup 限制实际影响

- 具体位置：Appendix A（6.4% latency overhead），§5 Conclusion
- 问题：Sparse prediction 的最终目的是加速推理。论文在 Appendix A 说 "Our contribution is prediction quality and inference simplification, not end-to-end latency reduction"，并诚实地报告了 6.4% overhead。但对于 sparsity 领域的论文，缺乏 speedup 结果显著限制了贡献的实际意义。
- 建议：(1) 至少在一层使用 Triton block-sparse 做 proof-of-concept speedup 实验；(2) 或更清晰地在 introduction 中 frame 论文为 "training objective study"，弱化 efficiency claim。

---

## 小问题（不影响接收）

- §4.2: "reducing TEAL's perplexity by 19% (10.82 → 8.81)" — 准确值为 18.6%，19% 是向上取整，建议用 "~19%" 或精确值。
- Eq. 3: s_j 缺少层标 ℓ 的上标，与 Eq. 1-2 的 notation 不一致。
- §3.4: "No temperature scaling (T=1) is applied (Hinton et al., 2015)" — 这里的 T 是 KL distillation 的 temperature，而 §3.3 的 τ 是 Gumbel-Sigmoid 的 temperature。两者使用不同符号很好，但可能让读者困惑是否两者相关。建议在首次出现 T 时加一句澄清。
- Table 4: STE 在 30% 缺少 PPL 数据（标记为 "---‡"），footnote 解释 STE 仅达 20.8% effective sparsity。但这实际上意味着 STE 和 Gumbel 在不同 actual sparsity 下对比，公平性有限。
- Limitations 段落：提到 "scaling to 70B+ remains future work"，但论文已经在 14B 上观察到 regression 加剧，这使得 70B+ 的前景更加不确定，建议提及。

---

## 主要优势

1. **C1 target-swap ablation 设计巧妙**：将 "what"（mask target quality）和 "how"（gradient coupling mechanism）解耦，证明 KL 发现的 mask patterns 是质量优势的主要来源。这是论文最有洞察力的实验。

2. **实验控制严格**：KL / BCE / MSE 使用完全相同的 architecture、data、optimizer、steps，仅改变 loss function。这种 controlled comparison 在 empirical ML 论文中并不常见。

3. **诚实的 limitations**：论文明确承认无 wall-clock speedup、knowledge-task regression、training data homogeneity。Abstract 使用更保守的 14.5%（matched sparsity）而非 18.6%（nominal）。

4. **丰富的 appendix**：从 bottleneck sensitivity 到 temperature schedule 到 training convergence 到 cross-seed mask consistency，appendix 覆盖了大部分可预见的 reviewer 问题。

5. **2D taxonomy**（Table 1, §3.7）提供了一个有用的组织框架：correction granularity × training signal coupling，帮助定位论文贡献。

6. **3-seed 评估**用于主要结果（8B），PPL 标准差极小（±0.02），增强了结果的可靠性。

---

## Questions for Authors

Q1: K=4 at 50% 为什么比 K=1 差？你们是否有 K=2, K=8 的数据来追踪 PPL vs K 的趋势？

Q2: 如果在 K=4 实验中强制使用 E2E KL 的 per-layer allocation pattern（而非 K=4 自然学出的），MMLU anomaly 是否消失？

Q3: 你们是否尝试过在 GSM8K 或 math 数据上训练 predictor（而非 WikiText-103），以检验 knowledge-task regression 是否来自 training data bias？

Q4: BCE 30% 为什么缺少 uniform allocation 数据？

Q5: 在 Appendix T 的 remove-valley 实验中，MMLU +3.4pp 的代价是 ARC-c -1.5pp。是否存在一个 per-layer allocation 配置能同时改善两者？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2008 · 2026-05-23T00:40:11.753250+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 169

## Round 169

2 recorded events


### User

_source line 2009 · 2026-05-23T00:40:26.322128+00:00_

[Reviewer 1 审稿结果]:
审稿完成。总结：

- **Overall 3.5（Borderline Conference）**，Soundness 3.5，Excitement 3
- 3 个 Must-Fix：(1) K=4 at 50% 反常行为削弱 coupling decomposition 可信度；(2) MMLU K=4 > E2E anomaly 暴露 allocation confound；(3) Qwen-14B GSM8K -20pp 仅单 seed
- 5 个 Should-Fix：系统性 knowledge regression 缺机制分析、C1 s42 oracle provenance、BCE 30% 缺 uniform 对比、sparsity controller 30% 饱和、无 wall-clock speedup
- 主要优势：C1 target-swap ablation 巧妙、实验控制严格、limitations 诚实、appendix 丰富

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2010 · 2026-05-23T00:40:33.543382+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 170

## Round 170

6 recorded events


### User

_source line 2011 · 2026-05-23T00:42:23.809669+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

---

## Paper Summary

本文提出用前向 KL 散度（output-distribution distillation）替代 BCE 来训练 SwiGLU LLM 的轻量级稀疏性预测器（<1% base 参数）。核心 insight 是 KL 将所有 mask 决策通过输出分布耦合，而 BCE 独立处理每个神经元。在 LLaMA-3.1-8B 上 30% sparsity 下，KL predictor 将 PPL 相对 TEAL 降低 14.5%（matched sparsity），在 Mistral-7B 和 Qwen-2.5-14B 上 PPL 优势泛化。论文通过 C1 target-swap ablation 和 per-layer KL 分解，将 KL 的优势解耦为 signal type（output-distribution vs intermediate loss）和 coupling scope（cross-layer vs per-layer），发现 signal type 主导 PPL 差距（upper bound），coupling scope 对下游 commonsense 任务有实质贡献但对 reasoning 贡献有限。

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 实验设计严谨、分析框架有巧思的实证论文，但方法本身新颖性有限（将已有技术 KL+Gumbel 应用于稀疏预测器训练），且知识密集型任务的系统性退化和缺乏实际 wall-clock 加速削弱了实用价值。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法论扎实（multi-seed、cross-architecture、controlled ablation），但 K=1 per-layer 控制有 train-inference mismatch confound，MSE baseline 在 50% 仅 1/3 seed 成功 |
| Excitement | 3/5 | C1 ablation 和 signal type/coupling scope 分解是有信息量的分析贡献，但核心方法（KL+Gumbel→sparsity predictor）是已有技术的直接应用 |
| Overall Assessment | 3.5/5 | Borderline Conference：分析贡献扎实但技术新颖性受限，知识任务退化和无 speedup 限制实用性 |
| Confidence | 4/5 | 对 LLM 稀疏性和知识蒸馏方向较为熟悉 |
| Reproducibility | 4/5 | 超参数、架构细节充分，承诺开源 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 知识密集型任务的系统性退化缺乏充分调查

- 具体位置：§4.1 (Knowledge-Task Regression: Hypothesis)、§4.6 (Cross-Architecture and Scale)、Limitations
- 问题：KL predictor 在所有测试规模上系统性地在 MMLU/GSM8K 上退化（8B: MMLU -5.2pp; Mistral: GSM8K 15.9→8.6; Qwen-14B: GSM8K -20pp, MMLU -8.1pp）。论文仅提出两个假设（WikiText-103 训练数据偏差、forward KL mode-covering 稀释稀有激活），但 **没有做任何控制实验来验证这些假设**。例如：(a) 在更多样化的训练数据上训练 predictor 能否缓解？(b) 调整 temperature 或使用 reverse KL 是否能保护 reasoning pathways？这些都是可行的消融实验但未执行。
- 为什么影响接收：一个声称优于 TEAL 的方法如果在知识任务上系统退化，其实用价值大打折扣。读者需要知道这是方法固有的限制还是可以通过简单改进缓解的。仅提出假设而不验证，使核心发现的实用意义存疑。
- 建议修改方向：至少执行一个控制实验——例如在 C4 或 RedPajama 子集上训练 predictor，测试知识任务是否改善。或者测试 task-specific allocation（论文自己在 Appendix T 的 constraint analysis 中展示了 remove-valley 能提升 MMLU +3.4pp 和 GSM8K +1.6pp，这一发现应在正文中更突出）。

**N2** [critical] 方法新颖性的边界需要更清晰地论证

- 具体位置：§1 Introduction、§3 Method、§2 Related Work
- 问题：核心技术贡献——KL 散度 + Gumbel-Sigmoid 松弛训练 sparsity predictor——每个组件都是成熟技术：KL distillation (Hinton 2015)、Gumbel-Sigmoid (Maddison 2017, Louizos 2018)、sparsity predictor 架构 (DejaVu 2023)。MaskLLM (Fang et al., 2024) 已将 KL + Gumbel-Softmax 用于可学习稀疏 mask 训练。论文在 §2 提出的三点区分（contextual vs static, cross-layer allocation, distribution shift robustness）是合理的，但这些区别更多来自 **应用场景的不同**（activation sparsity vs weight sparsity），而非方法论的创新。
- 为什么影响接收：ACL 审稿需要评估 contribution 的 significance。若核心方法仅是将已有技术组合应用到新场景，则论文需要在分析贡献上具有更强的 novelty 来弥补。C1 ablation 和 per-layer decomposition 是有价值的分析贡献，但它们作为主要 contribution 是否足够需要 reviewer 判断。
- 建议修改方向：论文可以更明确地将自己定位为 **分析驱动的实证贡献**（the paper already does this somewhat with "primarily an empirical study"），并加强 C1 ablation 和 signal type/coupling scope 分解的 framing，将其作为主要贡献而非辅助发现。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Per-layer KL 分解在 50% sparsity 下失效

- 具体位置：§4.5 (Per-Layer KL)，Table 4
- 问题：在 50% sparsity 下，K=4 per-layer KL (PPL 44.23) 比 K=1 (34.85) 更差，而 E2E KL 为 11.84。论文假设这是 partial coupling 下的 gradient interference，但未提供证据。这意味着论文的核心分析框架（signal type vs coupling scope decomposition）在高稀疏度下不适用，但 abstract 和 conclusion 仍使用来自 30% 实验的分解结果做出 general claims。
- 建议：在 abstract/conclusion 中明确限定 decomposition 结论的适用范围（"at moderate sparsity"），或提供 50% 下的替代分析。

**W2** [warning] 无 wall-clock 加速，6.4% latency overhead

- 具体位置：Appendix A、§1 Introduction (sentence 8)
- 问题：论文诚实地披露了这一点（appreciated），但这意味着目前的方法在实际部署中不仅没有加速，反而增加了 6.4% 延迟。Without sparse kernel support, the predictor is purely an analytical tool, not a practical system contribution. 这对一篇投稿到 NLP 会议（而非系统会议）的论文是可以接受的，但对实用影响的声明需要相应弱化。
- 建议：这已在论文中处理得相当好。可在 Conclusion 中更明确地说明 "实际加速取决于未来稀疏核的支持" 而非仅在 appendix 中提及。

**W3** [warning] 缺少生成质量评估

- 具体位置：Limitations (acknowledged)
- 问题：评估仅涵盖 PPL 和 multiple-choice benchmarks。Open-ended generation (MT-Bench, AlpacaEval) 在 sparsity 下的表现可能与 PPL/选择题结果不一致。特别是论文发现 KL 的 mode-covering 特性在 commonsense 上优势但知识任务退化——这对生成质量可能有不同的影响模式。
- 建议：这已在 Limitations 中提及。若能增加 MT-Bench 或 AlpacaEval 的结果将显著增强论文的完整性。

**W4** [warning] Introduction 中 "19%" PPL 减少数字有误

- 具体位置：§4.1, Introduction ¶13
- 问题：Introduction 声称 "reducing TEAL's perplexity by 19% (10.82 → 8.81)"。实际计算：(10.82 - 8.81) / 10.82 = 18.58%，约 18.6%，而非 19%。Abstract 正确使用了 matched-sparsity 的 14.5%。这种不精确虽小，但在审稿人 verify 数字时会引发信任问题。
- 建议：修正为 18.6% 或 ~19%，并注明此为 nominal sparsity 下的比较（actual sparsity 分别为 28.5% vs 29.3%）。

**W5** [warning] MSE baseline 在 50% sparsity 下的可靠性

- 具体位置：Appendix G (MSE Baseline Configuration)、Table 4
- 问题：MSE baseline 在 50% sparsity 下，seed 123 catastrophic failure (PPL=15,789, 仅 5.1% 实际稀疏度)。因此 Table 4 中 MSE 50% 的 229.26 实际仅来自 seed 42（标注 §），而非 3-seed 平均。这使得 MSE 在高稀疏度下的比较不可靠，但论文在 §3.7 中仍使用 MSE 50% 结果（"1.7×/9.6× worse PPL"）来论证 taxonomy 的预测力。
- 建议：正文中使用 MSE 50% 结果时应明确注明 single-seed caveat，并讨论这种 instability 是否反映了 MSE loss 本身的问题还是实现细节。

**W6** [warning] C1 ablation 中 seed 42 oracle provenance 问题

- 具体位置：Table 3 footnote、Appendix P
- 问题：C1 ablation 的 s42 oracle 来自 "earlier training run"，而 s123/s456 使用 matched retrained oracles。s42 的 PPL gap (0.65pp at 30%) 显著大于 s123/s456 (≤0.03pp)。虽然论文在 footnote 中披露了这一点，但 s42 是唯一有 50% 数据的 seed，使得 50% 的 C1 结论基于可能有 confound 的单 seed。
- 建议：提供 s123 或 s456 在 50% sparsity 下的 C1 结果以增强稳健性，或明确说明 50% 的 C1 结论仅基于 s42。

---

## 小问题（不影响接收）

- **Table 2 比较不对齐**：BCE 30% 使用 TEAL global 分配（标注 †），而 KL 30% 使用 uniform 分配，使直接比较不公平。建议在同一 allocation 下展示 BCE 结果，或在 caption 中更醒目地标注。
- **Abstract 信息密度偏高**：9 句 abstract 涵盖了 problem、method、主结果、C1 ablation、signal type claim、coupling scope claim、cross-arch、disclaimer——信息量极大，但对首次阅读的读者来说可能太密集。考虑将 abstract 压缩至 6-7 句，将 C1 和 decomposition 细节移至正文。
- **Conclusion 过于简洁**：仅 4 句话，缺少对 future work 方向的讨论（如 task-aware allocation, diverse training data, sparse kernel integration）。
- **术语一致性**："output-distribution alignment"、"output-distribution distillation"、"output-distribution objective" 在全文中交替使用，建议统一。
- **Figure 2 caption 的 14.5%**：此处使用 matched-sparsity 的 14.5%，而 §4.1 正文使用 nominal 的 "19%"（实为 18.6%），两处使用不同基准但未解释，可能造成困惑。
- **GPU 型号**："NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96GB)" 是非常具体的新硬件（2025 年发布），虽然不直接暴露身份，但在 double-blind 审稿中需注意——拥有该 GPU 的实验室相对较少。

---

## Missing References

本文的 related work 覆盖面相当完善（50+ 引用），涵盖了 training-free、predictor-based、activation function engineering、weight pruning、KL distillation、MoE routing 等主要方向。以下为可能的补充：

- **TurboSparse-Mistral**（Song et al., 2025）：虽已引用 TurboSparse，但该系列后续工作包括特定模型适配，可能值得更新引用。
- 论文未引用 **Mixtral-of-Experts** 相关的稀疏激活工作，虽然 MoE 与 activation sparsity 有本质区别，但部分读者可能期望看到更明确的区分说明。
- 建议补充检索 2026 年 1-5 月是否有新的 **KL distillation for activation sparsity** 的工作（如 SVD-CSP 已引用，但该方向可能有更多新进展）。

总体上，missing references 不构成重大问题。

---

## 主要优势

1. **实验设计严谨**：3-seed 评估、cross-architecture 验证（3 个模型）、matched-sparsity 比较、多达 18 个 appendix sections 的补充实验。这在同类工作中是高标准。
2. **C1 target-swap ablation 设计巧妙**：通过将 KL 发现的 mask 模式转移给 BCE 训练，干净地分离了 "mask pattern quality" 和 "gradient coupling mechanism" 的贡献。这是一个有 insight 的实验设计。
3. **诚实的 limitations 披露**：论文自始至终坦诚地报告了知识任务退化、无 wall-clock 加速、评估限制等。这增强了结果的可信度。
4. **Per-layer KL decomposition**：K=1 和 K=4 控制实验合理地（虽然不完美地）分解了 signal type 和 coupling scope 的贡献，并发现了有趣的 task-dependent dissociation。
5. **写作质量**：Claims 有适当的 hedging（"upper bound"、"suggests"、"primarily empirical"），数字引用有 exp_id 追踪。
6. **Compensation redundancy finding**：发现 KL predictor 使得额外的 67.2M 参数补偿网络冗余，简化了推理管线。

---

## 评分总结

| 维度 | 分数 |
|------|------|
| Soundness | 3.5 |
| Excitement | 3 |
| Overall Assessment | 3.5 |
| Reviewer Confidence | 4 |
| Reproducibility | 4 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2012 · 2026-05-23T00:43:06.926172+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference), Soundness 3.5, Excitement 3, Confidence 4\n\n### Must-Fix 问题\n\n**N1** [critical] Per-layer KL K=4 在 50% sparsity 的反常行为削弱 coupling decomposition 的可信度\n- K=4 per-layer KL 在 50% sparsity 的 PPL 为 44.23，劣于 K=1 的 34.85，而 E2E KL 为 11.84。如果 coupling 是有益的，增加 masked layers 数量（K=1→K=4）应缩小与 E2E 的差距，但实际上差距扩大了。论文给出的解释是 \"gradient interference\"，但纯粹是 speculation。\n- 建议：(1) 增加 K=2, K=8, K=16 实验；(2) 或限制 decomposition 分析仅在 30% 下声称有效；(3) 分析 K=4 at 50% 的 per-layer sparsity 分布。\n\n**N2** [critical] MMLU K=4 超过 E2E 的 anomaly 暴露 decomposition confound\n- K=4 在 MMLU 上系统性超过 E2E（所有 3 个 seed），论文解释为 K=4 的 near-uniform per-layer sparsity（std=0.003）匹配了 uniform inference protocol。但这说明 K=4 control 无法独立地隔离 coupling 效应——它同时改变了 allocation pattern。\n- 建议：(1) 在 main text 中明确讨论 allocation confound；(2) 考虑在 K=4 实验中强制使用与 E2E 相同的 per-layer allocation pattern。\n\n**N3** [critical] Qwen-2.5-14B 的 GSM8K -20pp regression 仅有单 seed 支撑\n- GSM8K 从 52.1pp（TEAL）下降到 32.0pp（KL），降幅达 20pp，且标准差为 5.2pp。Global allocation 行仅有 seed 42。\n- 建议：补充 Qwen-14B 至少 3-seed 评估，或弱化跨规模趋势的措辞。\n\n### Should-Fix 问题\n\n**W1** 系统性 knowledge-task regression 缺乏机制分析（仅假设无验证）\n**W2** C1 ablation s42 oracle 来自不同 checkpoint（s42 gap 0.65pp vs s123/s456 ≤0.03pp）\n**W3** BCE 30% 仅报告 global allocation，缺少 uniform 对比\n**W4** Sparsity controller 在 30% target 饱和（λ=5000 cap, actual 28.5%）\n**W5** 无 wall-clock speedup 限制实际影响\n\n### 小问题\n- §4.2 \"19%\" 实际为 18.6%\n- Eq. 3 s_j 缺少层标 ℓ\n- §3.4 T 和 τ 可能让读者困惑\n- Table 4 STE 30% 在不同 actual sparsity 下对比\n- Limitations 未提及 14B regression 加剧对 70B+ 前景的影响\n\n### 主要优势\n1. C1 target-swap ablation 设计巧妙\n2. 实验控制严格（KL/BCE/MSE 同架构同数据同 optimizer）\n3. 诚实的 limitations\n4. 丰富的 appendix\n5. 2D taxonomy 有用\n6. 3-seed 评估 PPL σ=0.02\n\n### Questions\nQ1: K=4 at 50% 为什么比 K=1 差？有 K=2, K=8 数据吗？\nQ2: K=4 中强制使用 E2E 的 per-layer allocation，MMLU anomaly 是否消失？\nQ3: 是否尝试过在 GSM8K/math 数据上训练 predictor？\nQ4: BCE 30% 为什么缺少 uniform allocation 数据？\nQ5: remove-valley 中，是否存在同时改善 MMLU 和 ARC-c 的 allocation？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference), Soundness 3.5, Excitement 3, Confidence 4\n\n### Must-Fix 问题\n\n**N1** [critical] Per-layer KL K=4 在 50% sparsity 的反常行为削弱 coupling decomposition 的可信度\n- K=4 per-layer KL 在 50% sparsity 的 PPL 为 44.23，劣于 K=1 的 34.85，而 E2E KL 为 11.84。如果 coupling 是有益的，增加 masked layers 数量（K=1→K=4）应缩小与 E2E 的差距，但实际上差距扩大了。论文给出的解释是 \"gradient interference\"，但纯粹是 speculation。\n- 建议：(1) 增加 K=2, K=8, K=16 实验；(2) 或限制 decomposition 分析仅在 30% 下声称有效；(3) 分析 K=4 at 50% 的 per-layer sparsity 分布。\n\n**N2** [critical] MMLU K=4 超过 E2E 的 anomaly 暴露 decomposition confound\n- K=4 在 MMLU 上系统性超过 E2E（所有 3 个 seed），论文解释为 K=4 的 near-uniform per-layer sparsity（std=0.003）匹配了 uniform inference protocol。但这说明 K=4 control 无法独立地隔离 coupling 效应——它同时改变了 allocation pattern。\n- 建议：(1) 在 main text 中明确讨论 allocation confound；(2) 考虑在 K=4 实验中强制使用与 E2E 相同的 per-layer allocation pattern。\n\n**N3** [critical] Qwen-2.5-14B 的 GSM8K -20pp regression 仅有单 seed 支撑\n- GSM8K 从 52.1pp（TEAL）下降到 32.0pp（KL），降幅达 20pp，且标准差为 5.2pp。Global allocation 行仅有 seed 42。\n- 建议：补充 Qwen-14B 至少 3-seed 评估，或弱化跨规模趋势的措辞。\n\n### Should-Fix 问题\n\n**W1** 系统性 knowledge-task regression 缺乏机制分析（仅假设无验证）\n**W2** C1 ablation s42 oracle 来自不同 checkpoint（s42 gap 0.65pp vs s123/s456 ≤0.03pp）\n**W3** BCE 30% 仅报告 global allocation，缺少 uniform 对比\n**W4** Sparsity controller 在 30% target 饱和（λ=5000 cap, actual 28.5%）\n**W5** 无 wall-clock speedup 限制实际影响\n\n### 小问题\n- §4.2 \"19%\" 实际为 18.6%\n- Eq. 3 s_j 缺少层标 ℓ\n- §3.4 T 和 τ 可能让读者困惑\n- Table 4 STE 30% 在不同 actual sparsity 下对比\n- Limitations 未提及 14B regression 加剧对 70B+ 前景的影响\n\n### 主要优势\n1. C1 target-swap ablation 设计巧妙\n2. 实验控制严格（KL/BCE/MSE 同架构同数据同 optimizer）\n3. 诚实的 limitations\n4. 丰富的 appendix\n5. 2D taxonomy 有用\n6. 3-seed 评估 PPL σ=0.02\n\n### Questions\nQ1: K=4 at 50% 为什么比 K=1 差？有 K=2, K=8 数据吗？\nQ2: K=4 中强制使用 E2E 的 per-layer allocation，MMLU anomaly 是否消失？\nQ3: 是否尝试过在 GSM8K/math 数据上训练 predictor？\nQ4: BCE 30% 为什么缺少 uniform allocation 数据？\nQ5: remove-valley 中，是否存在同时改善 MMLU 和 ARC-c 的 allocation？"
  }
}
```

</details>

---


### Tool result

_source line 2013 · 2026-05-23T00:43:30.059080+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23132
}
```

</details>

---


### Tool call

_source line 2014 · 2026-05-23T00:43:30.461256+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference), Soundness 3.5, Excitement 3, Confidence 4\n\n### Must-Fix 问题\n\n**N1** [critical] 知识密集型任务的系统性退化缺乏充分调查\n- KL predictor 在所有测试规模上系统性地在 MMLU/GSM8K 上退化（8B: MMLU -5.2pp; Mistral: GSM8K 15.9→8.6; Qwen-14B: GSM8K -20pp, MMLU -8.1pp）。论文仅提出两个假设但没有做任何控制实验验证。\n- 建议：至少执行一个控制实验——例如在 C4 或 RedPajama 子集上训练 predictor，或更突出 Appendix T 的 constraint analysis（remove-valley → MMLU +3.4pp）。\n\n**N2** [critical] 方法新颖性的边界需要更清晰地论证\n- 核心技术（KL distillation + Gumbel-Sigmoid + sparsity predictor 架构）每个组件都是成熟技术。MaskLLM 已将 KL + Gumbel-Softmax 用于可学习稀疏 mask。论文的三点区分更多来自应用场景不同（activation vs weight sparsity），而非方法论创新。\n- 建议：更明确地定位为分析驱动的实证贡献，加强 C1 ablation 和 signal type/coupling scope 分解的 framing。\n\n### Should-Fix 问题\n\n**W1** Per-layer KL 分解在 50% sparsity 下失效（K=4 PPL 44.23 > K=1 34.85），abstract/conclusion 仍使用 30% 结论做 general claims\n**W2** 无 wall-clock 加速，6.4% latency overhead\n**W3** 缺少生成质量评估（MT-Bench, AlpacaEval）\n**W4** Introduction 中 \"19%\" PPL 减少实际为 18.6%\n**W5** MSE baseline 在 50% 仅 seed 42（seed 123 catastrophic failure PPL=15,789），single-seed 结论不可靠\n**W6** C1 ablation s42 oracle provenance 问题（s42 gap 0.65pp vs s123/s456 ≤0.03pp）\n\n### 小问题\n- Table 2 BCE 30% global vs KL uniform 比较不公平\n- Abstract 信息密度偏高（9 句）\n- Conclusion 过于简洁，缺 future work\n- 术语不一致：\"output-distribution alignment/distillation/objective\" 交替使用\n- Figure 2 caption 14.5% vs §4.1 \"19%\" 使用不同基准\n- GPU 型号 \"RTX PRO 6000 Blackwell Server Edition\" double-blind 风险\n\n### Missing References\n- TurboSparse-Mistral 后续工作\n- Mixtral-of-Experts 区分说明\n- 2026 年 1-5 月新工作检索\n- 总体 missing refs 不构成重大问题\n\n### 主要优势\n1. 实验设计严谨（3-seed, cross-arch, 18 个 appendix sections）\n2. C1 target-swap ablation 巧妙\n3. 诚实的 limitations 披露\n4. Per-layer KL decomposition 有 insight\n5. 写作有适当 hedging\n6. Compensation redundancy finding 简化推理管线\n\n### 评分\nSoundness 3.5, Excitement 3, Overall 3.5, Confidence 4, Reproducibility 4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference), Soundness 3.5, Excitement 3, Confidence 4\n\n### Must-Fix 问题\n\n**N1** [critical] 知识密集型任务的系统性退化缺乏充分调查\n- KL predictor 在所有测试规模上系统性地在 MMLU/GSM8K 上退化（8B: MMLU -5.2pp; Mistral: GSM8K 15.9→8.6; Qwen-14B: GSM8K -20pp, MMLU -8.1pp）。论文仅提出两个假设但没有做任何控制实验验证。\n- 建议：至少执行一个控制实验——例如在 C4 或 RedPajama 子集上训练 predictor，或更突出 Appendix T 的 constraint analysis（remove-valley → MMLU +3.4pp）。\n\n**N2** [critical] 方法新颖性的边界需要更清晰地论证\n- 核心技术（KL distillation + Gumbel-Sigmoid + sparsity predictor 架构）每个组件都是成熟技术。MaskLLM 已将 KL + Gumbel-Softmax 用于可学习稀疏 mask。论文的三点区分更多来自应用场景不同（activation vs weight sparsity），而非方法论创新。\n- 建议：更明确地定位为分析驱动的实证贡献，加强 C1 ablation 和 signal type/coupling scope 分解的 framing。\n\n### Should-Fix 问题\n\n**W1** Per-layer KL 分解在 50% sparsity 下失效（K=4 PPL 44.23 > K=1 34.85），abstract/conclusion 仍使用 30% 结论做 general claims\n**W2** 无 wall-clock 加速，6.4% latency overhead\n**W3** 缺少生成质量评估（MT-Bench, AlpacaEval）\n**W4** Introduction 中 \"19%\" PPL 减少实际为 18.6%\n**W5** MSE baseline 在 50% 仅 seed 42（seed 123 catastrophic failure PPL=15,789），single-seed 结论不可靠\n**W6** C1 ablation s42 oracle provenance 问题（s42 gap 0.65pp vs s123/s456 ≤0.03pp）\n\n### 小问题\n- Table 2 BCE 30% global vs KL uniform 比较不公平\n- Abstract 信息密度偏高（9 句）\n- Conclusion 过于简洁，缺 future work\n- 术语不一致：\"output-distribution alignment/distillation/objective\" 交替使用\n- Figure 2 caption 14.5% vs §4.1 \"19%\" 使用不同基准\n- GPU 型号 \"RTX PRO 6000 Blackwell Server Edition\" double-blind 风险\n\n### Missing References\n- TurboSparse-Mistral 后续工作\n- Mixtral-of-Experts 区分说明\n- 2026 年 1-5 月新工作检索\n- 总体 missing refs 不构成重大问题\n\n### 主要优势\n1. 实验设计严谨（3-seed, cross-arch, 18 个 appendix sections）\n2. C1 target-swap ablation 巧妙\n3. 诚实的 limitations 披露\n4. Per-layer KL decomposition 有 insight\n5. 写作有适当 hedging\n6. Compensation redundancy finding 简化推理管线\n\n### 评分\nSoundness 3.5, Excitement 3, Overall 3.5, Confidence 4, Reproducibility 4"
  }
}
```

</details>

---


### Tool result

_source line 2015 · 2026-05-23T00:43:31.871003+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1409
}
```

</details>

---


### Assistant

_source line 2016 · 2026-05-23T00:43:34.323206+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 171

## Round 171

2 recorded events


### User

_source line 2017 · 2026-05-23T00:43:36.870199+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：Overall 3.5（Borderline Conference）。两个 Must-Fix：(1) 知识任务系统性退化仅有假设无控制实验验证；(2) 方法新颖性边界需更清晰论证（KL+Gumbel 均为成熟技术，核心是应用到新场景）。六个 Should-Fix 包括 per-layer decomposition 在 50% 下失效、无 wall-clock 加速、缺少生成评估、Introduction "19%" 数字不准确、MSE baseline 50% 仅单 seed、C1 ablation 的 s42 oracle provenance 问题。主要优势是实验设计严谨（3-seed, 3 architectures, 18 appendix sections）、C1 target-swap ablation 设计巧妙、limitations 披露诚实。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2018 · 2026-05-23T00:43:40.780643+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 172

## Round 172

2 recorded events


### User

_source line 2019 · 2026-05-23T00:45:03.236694+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R1-N1: K=4 在 50% sparsity 的反常行为削弱 decomposition 可信度**

同意这是一个实质性问题。我在自己的 W1 中也指出了这一点。论文的 "gradient interference" 解释确实是 speculation（§4.5: "We hypothesize that partial coupling (K=4 of 32 layers) under tight capacity amplifies gradient interference"），没有任何实验证据支撑。

补充观察：这个反常不仅影响可信度，还从根本上限制了 decomposition 框架的 generality——论文的分析核心贡献之一（signal type vs coupling scope decomposition）在高稀疏度下不可用。论文 abstract 和 conclusion 中的 general claims（"signal type accounts for the majority of the PPL gap"）实际上只在 30% sparsity 下有证据支持。

R1 建议的 K=2, K=8, K=16 梯度实验很好，能帮助区分 "K 增加后性能单调改善"（支持 coupling 有益）vs "存在最优 K"（支持 gradient interference）。

**[AGREE] R1-N2: MMLU K=4 anomaly 暴露 allocation confound**

同意。K=4 训练产生 near-uniform per-layer sparsity (std=0.003)，而 E2E KL 产生非均匀分配（L14-L18 valley, L22-L28 aggressive pruning，见 Appendix U Table 21）。因此 K=4 vs E2E 的差异同时反映了 coupling scope 和 allocation pattern 两个变量的变化，无法独立归因。

论文在 Appendix T footnote 和 Appendix S 的 constraint analysis 中已隐式承认了这一点——remove-valley 条件下 MMLU=44.0%，与 K=4 的 42.7% 接近——但这一 confound 仅在 appendix 中讨论，在正文 §4.5 的 decomposition 叙事中未充分体现。

R1 建议的 "强制 K=4 使用 E2E 的 per-layer allocation" 在技术上是可行的（推理时 override per-layer budget），这将是一个更干净的控制实验。

**[PARTIALLY REBUT] R1-N3: Qwen-14B GSM8K -20pp 仅单 seed 支撑**

部分反驳。R1 声称 "-20pp regression 仅有单 seed 支撑"，但根据 Appendix K Table 14，uniform allocation 行的 KL 结果标注为 32.0±5.2，表明这是 3-seed 结果（尽管高方差 std=5.2pp）。TEAL 是 deterministic 无需多 seed。因此 -20pp 的 gap（52.1 vs 32.0）是 3-seed KL 与 deterministic TEAL 的比较，并非单 seed。

不过，R1 的担忧仍有部分道理：
1. Global allocation 行确实仅为 seed 42（KL 48.82 vs TEAL 49.51，几乎无差异）
2. Uniform allocation 的 std=5.2pp 极高（CV=16.3%），95% CI 约为 ±10pp
3. 3 个 seed 的统计力较弱

因此，虽然 -20pp 非单 seed，但其可靠性确实受限于高方差和少量 seed。建议论文在引用此数字时使用完整的 "32.0±5.2 vs 52.1" 而非仅 "-20pp"。

---

### Should-Fix 问题

**[AGREE] R1-W1: Knowledge-task regression 缺乏机制分析**

完全同意，我将此列为自己的 N1（Must-Fix）。这是两位 reviewer 共同指出的问题，权重应加大。论文在 Appendix S 中已有 remove-valley constraint analysis 证明 allocation redistribution 能恢复 MMLU +3.4pp / GSM8K +1.6pp，这一发现应在正文中更突出地呈现，并启发进一步的控制实验（如在 math-heavy 数据上训练 predictor）。

**[AGREE] R1-W2: C1 s42 oracle provenance 问题**

同意。我在 W6 中也指出了这一点。s42 的 0.65pp gap 与 s123/s456 的 ≤0.03pp gap 差异显著。50% sparsity 的 C1 结论仅基于 s42，增加了 confound 风险。

**[AGREE] R1-W3: BCE 30% 缺少 uniform allocation 对比**

同意。Table 2 中 BCE 30% 使用 TEAL global（标注 †），而 KL 30% 使用 uniform，使读者难以直接比较。我在自己的 minor issues 中也提到了这一点。

**[PARTIALLY REBUT] R1-W4: Sparsity controller 在 30% 饱和**

部分反驳。论文在 Appendix C 已充分 address 了这一问题：

1. 实际稀疏度 28.5%（偏差 5%），但论文提供了 matched-sparsity 比较——KL at 28.5% vs TEAL at 28.5% (PPL 10.30)，gap 为 14.5%（§4.1 和 Figure 2 caption）
2. Appendix C 明确指出 "This does not affect conclusions: TEAL at 28.5% actual sparsity yields PPL 10.30 (vs. 10.97 at exact 30%), a 0.67 PPL difference negligible relative to the KL vs. TEAL gap"
3. 对于方法论而言，Lagrangian 控制器的饱和是一个工程问题（可通过调高 λ_max 或使用更激进的 schedule 来解决），不影响核心发现

不过 R1 的 concern 有一定道理：如果 KL predictor 在 30% target 下只能达到 28.5%，这意味着方法在精确稀疏度控制上有局限性。建议论文在正文（而非仅 appendix）中讨论这一 deviation。

**[AGREE] R1-W5: 无 wall-clock speedup**

同意。我在 W2 中也指出了这一点。论文的诚实披露值得肯定，但这确实限制了实用影响。

---

### 小问题

**[AGREE] 19% → 18.6%**：我也在 W4 中指出了这一数值不精确。(10.82-8.81)/10.82 = 18.58%，四舍五入到 19% 偏激进。

**[AGREE] Eq. 4 s_j 缺少层标 ℓ**：确认 §3.3 Eq. 4 中 s_j 和 m̃_j 均缺少 ℓ 上标，而 §3.1 中 s^(ℓ) 有层标。应保持一致。

**[AGREE] T 和 τ 可能混淆**：§3.4 最后一句 "No temperature scaling (T=1) is applied (Hinton, 2015)" 中的 T 指 distillation temperature，与 Gumbel-Sigmoid 的 τ 不同。建议明确区分或使用不同符号。

**[AGREE] Table 4 STE 30% 比较不公平**：STE 在 30% target 下仅达到 20.8% actual sparsity（标注 ‡），与其他方法在不同实际稀疏度下比较，应标注更醒目或提供 matched-sparsity 结果。

**[AGREE] Limitations 未提 14B regression 对更大规模的影响**：8B→14B regression 加剧（GSM8K: -1.3pp at 8B → -20pp at 14B），但 Limitations 未讨论这对 70B+ 的前景意味着什么。这是一个合理的补充建议。

---

### Questions 回应

**Q1 (K=2, K=8 data)**：同意这些实验有价值。若 K 与 PPL 的关系呈 U 形（K=1 best among per-layer, K=4 worse, E2E best），支持 gradient interference 假设；若单调改善，支持 coupling 有益。

**Q2 (K=4 forced allocation)**：好的实验建议。在推理时用 E2E KL 的 per-layer budget 覆盖 K=4 predictor 的 near-uniform pattern，可隔离 allocation confound vs coupling 效应。

**Q3 (Math training data)**：与我的 N1 一致。在 GSM8K 或数学文本上训练 predictor 是测试知识退化是否源于训练数据偏差的直接方法。

**Q4 (BCE 30% uniform)**：合理的问题。缺少 BCE 30% uniform 使 Table 2 的比较不对称。可能是 BCE 在 uniform allocation 下表现更差，作者选择了 BCE 最优的配置（global），但这应该被解释。

**Q5 (Remove-valley compromise)**：好问题。Appendix S 的 remove-valley 提升了 MMLU +3.4pp 和 GSM8K +1.6pp 但 ARC-c -1.5pp。是否存在 Pareto-optimal 的中间方案（如部分缩窄 valley 而非完全移除）值得探索，但可能超出本文范围。

---

### 总结

我与 R1 在核心评估上高度一致：论文实验设计严谨，C1 ablation 和 decomposition 分析有价值，但 (1) 技术新颖性有限，(2) decomposition 框架在 50% 下失效且有 allocation confound，(3) 知识任务退化缺乏机制调查。

两位 reviewer 共同认可的优势：实验控制质量、诚实的 limitations、C1 ablation 设计。
两位 reviewer 共同的 concerns：decomposition 的可信度（K=4 anomaly）、knowledge regression（unverified hypotheses）、无 speedup。

我维持 **Overall 3.5 (Borderline Conference)** 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2020 · 2026-05-23T00:45:07.997534+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 173

## Round 173

2 recorded events


### User

_source line 2021 · 2026-05-23T00:45:11.500643+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

总结：与 R1 在大部分核心评估上一致。对 R1-N3（Qwen-14B GSM8K 单 seed）做了 partial rebut——该数据实为 3-seed 但高方差。对 R1-W4（sparsity controller 饱和）做了 partial rebut——论文已在 Appendix C 提供了 matched-sparsity 对比。其余 Must-Fix 和 Should-Fix 均同意。维持 Overall 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2022 · 2026-05-23T00:45:15.302369+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 174

## Round 174

10 recorded events


### User

_source line 2023 · 2026-05-23T00:45:24.169071+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 知识密集型任务的系统性退化缺乏充分调查**

同意这是论文最大的弱点之一。我在自己的审稿中也将此列为 W1 (Should-Fix)。数据模式非常清晰且跨规模一致：

- 8B: MMLU 40.7 vs TEAL 45.86 (-5.2pp)，GSM8K 7.5 vs 8.79 (-1.3pp)（Table 2）
- Mistral-7B: GSM8K 8.6 vs TEAL 15.9 (-7.3pp)（Appendix N, Table 17）
- Qwen-14B uniform: GSM8K 32.0 vs TEAL 52.1 (-20pp)（Appendix K, Table 13）

论文在 §4.2 "Knowledge-Task Regression: Hypothesis" 段提出两个假设但明确说 "await validation via knowledge-neuron probing"。R2 建议的控制实验（C4/RedPajama 训练）合理。我补充一点：Appendix T 的 constraint analysis 已经显示 remove-valley → MMLU +3.4pp, GSM8K +1.6pp（Table in Appendix T），这暗示 regression 部分源于 learned allocation（而非 loss function 本身），但论文未将此线索发展为系统性分析。至少应将 Appendix T 的发现提升到 main text，并讨论 allocation-aware training 的可能。

**[AGREE with nuance] R2-N2: 方法新颖性的边界**

部分同意。R2 正确指出核心组件（KL + Gumbel-Sigmoid + predictor architecture）均为成熟技术。但我认为 R2 对 MaskLLM 的对比略有偏差：

1. MaskLLM（Fang et al., 2024）处理的是 **static N:M weight masks**，mask 在部署后固定不变；本文处理的是 **contextual activation sparsity**，mask 随每个 token 变化，且需要 global top-k 跨层协调。这不仅是 "应用场景不同"，而是优化问题根本不同——MaskLLM 直接优化离散 mask 组合，本文需要 predictor 来泛化到未见输入。论文在 Introduction 第一段已做此区分。

2. 论文自身定位为 "primarily an empirical study"（Abstract 末句, Introduction §1 末段）。其贡献不在方法组件的新颖性，而在 (a) C1 target-swap ablation 解耦了 "what" vs "how"，(b) signal type vs coupling scope decomposition，(c) 跨 5 种 loss 的系统对比。这些 **实验设计** 是新颖的。

建议：论文应更早且更显著地承认组件层面的非新颖性（目前仅在 Related Work §2 的 MaskLLM 段提及），并在 Introduction 的 contribution list 中将 C1 ablation 和 decomposition 置于首位（目前第一条是 "ranking across five losses"，信息量不如 "C1 + decomposition"）。

---

### Should-Fix 问题

**[AGREE] R2-W1: Per-layer KL 分解在 50% sparsity 下失效**

强烈同意。我在自己的审稿中将此列为 **N1 (Critical)**——K=4 at 50% PPL 44.23 > K=1 34.85 的反常行为是 coupling decomposition 可信度的核心威胁。论文在 §4.5 末段给出 "gradient interference" 假说但无实验支撑。Abstract ("Signal type accounts for the majority of the PPL gap") 和 Conclusion ("signal type accounts for the majority of the PPL gap; upper bound") 均基于 30% 结果做 general claim，但未注明此结论在 50% 下不成立。

**[AGREE] R2-W2: 无 wall-clock 加速**

同意。我也列为 W5。Appendix A 报告 6.4% overhead（126.78 vs 119.11 ms/fwd），无任何 sparse kernel 实验。论文诚实披露了这一点，但对 sparsity 论文而言这显著限制了实际影响。

**[REBUT] R2-W3: 缺少生成质量评估（MT-Bench, AlpacaEval）**

不完全同意这属于 Should-Fix。理由：

1. 论文评估的是 **base model**（LLaMA-3.1-8B，非 Instruct），MT-Bench 和 AlpacaEval 需要 instruction-tuned model。在 base model 上跑这些 benchmark 没有意义。
2. 论文的 Limitations 段已承认 "open-ended generation quality (e.g., MT-Bench) remains untested"，并将其列为 future work。
3. 当前的 evaluation suite（PPL + 6 个 downstream tasks + OOD + cross-architecture）对于一篇 training objective 的 empirical study 已经相当充分。

如果 R2 的意图是评估 fluency/coherence 而非 instruction-following，更合适的 benchmark 是 perplexity（已有）或 text completion quality。但我不认为缺少 MT-Bench 是一个需要修复的问题。

**[AGREE] R2-W4: "19%" vs 18.6%**

同意是不精确的取整。我在自己的小问题中也指出了这一点。(10.82-8.81)/10.82 = 18.58% ≈ 18.6%。应改为 "~19%" 或 "18.6%"。

**[AGREE] R2-W5: MSE baseline at 50% single seed**

同意。MSE 50% 仅 seed 42 有效（PPL=229.26），seed 123 灾难性失败（PPL=15,789，Appendix G）。Table 4 中 MSE 50% 标注了 "§" footnote 但仅在 caption 中提及。单 seed 的 229.26 可能不代表 MSE 的典型表现。不过，MSE 30% 有 3-seed（18.52±1.68），已经 1.7× 劣于 TEAL，所以 MSE 劣势的结论在 30% 是稳健的。建议在 50% 对比中弱化对 MSE 的 claim 或补充更多 seed。

**[AGREE] R2-W6: C1 s42 oracle provenance**

同意。我列为 W2。s42 的 oracle 来自 earlier checkpoint（PPL gap 0.65pp），而 s123/s456 使用 matched oracle 后 gap 降至 ≤0.03pp。这使 s42 成为 Table 3 中的 outlier。建议为 s42 补训 matched oracle 或调整展示顺序。

---

### 小问题

**[AGREE] BCE 30% comparison fairness**: 我在 W3 中提出了同样的问题。Table 2 中 BCE 30% 仅有 global，KL 有 global+uniform，比较不完整。

**[AGREE] Abstract 信息密度**: 9 句话包含 PPL 数字、C1 ablation 结论、decomposition 结论、cross-architecture 结论，确实偏密。但内容均有必要，可考虑拆分为两段。

**[REBUT] Conclusion 过于简洁**: Conclusion 虽仅 4 句但覆盖了：(1) 核心发现（signal type 主导 PPL gap），(2) key result（14.5% PPL reduction, 46-68% divergence），(3) limitations summary，(4) code release。ARR 对 conclusion 格式无硬性要求。简洁但完整。Future work 在 Limitations 段中隐含（knowledge-task regression, wall-clock speedup, scaling to 70B+）。我不认为这需要修复。

**[AGREE] 术语不一致**: 确实存在。"output-distribution alignment"（Introduction, Conclusion）、"KL distillation"（§3, §4）、"output-distribution objective"（Abstract）交替使用。建议统一为 "output-distribution alignment" 并在首次出现时定义。

**[AGREE] Figure 2 caption vs §4.1 基准不一致**: Figure 2 caption 用 "14.5% at 30%" 而 §4.2 用 "19%"。前者是 matched sparsity（both at 28.5%），后者是 nominal TEAL 30%。两者都正确但对读者造成困惑。建议在 Figure 2 caption 中注明 "(matched actual sparsity 28.5%)"。

**[REBUT] GPU 型号 double-blind 风险**: "RTX PRO 6000 Blackwell Server Edition" 是 2025 年发布的商用 GPU，全球数万个实验室可能拥有。这不比 "A100 80GB" 更具识别性。ARR 的 anonymity policy 允许报告具体硬件配置。不构成 de-anonymization 风险。

---

### Missing References

**[AGREE with caveat]**: R2 提到的 TurboSparse-Mistral 和 2026 年新工作值得检查，但 R2 自己也说 "总体 missing refs 不构成重大问题"。论文的 Related Work（§2）已经相当全面，覆盖了 TEAL, CATS, R-Sparse, DejaVu, FastForward, ShadowLLM, D2DMoE, MaskLLM, SPON, PowerInfer, Deja Vu, LazyLLM 等。我同意可以补充但这不影响接收决定。

---

### 对 R2 优势评价的认同

完全同意 R2 列出的 6 个优势。特别是：
- **C1 target-swap ablation 的巧妙性** 是我和 R2 的共识
- **诚实的 limitations 披露** 在 ML 论文中难能可贵
- **Compensation redundancy finding** 确实简化了推理管线（去掉 67.2M 参数的 compensation network）

---

### 总结：与 R2 的分歧

| R2 观点 | R1 立场 | 理由 |
|---------|---------|------|
| N2 新颖性不足 | 部分同意 | 组件非新颖，但实验设计（C1, decomposition）有新颖性；论文已自定位为 empirical study |
| W3 缺 MT-Bench | 反驳 | Base model 不适用 instruction-following benchmarks |
| Conclusion 太短 | 反驳 | 简洁但完整，ARR 无格式要求 |
| GPU double-blind | 反驳 | 商用 GPU，不构成 de-anonymization |

其余所有 Must-Fix 和 Should-Fix 均同意或基本同意。我和 R2 的核心共识是：**knowledge-task regression 的机制分析不足**和 **coupling decomposition 在高 sparsity 下失效**是论文两个最关键的弱点。

**维持我的评分：Overall 3.5, Soundness 3.5, Excitement 3, Confidence 4。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2024 · 2026-05-23T00:45:49.052435+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2025 · 2026-05-23T00:45:49.053089+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T00:33:43.172793+00:00\", \"completed_at\": \"2026-05-23T00:38:03.239158+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（全文本：Title + Abstract）。Figure 1 在第 2 页右上角出现，属于可接受范围，但如果能将 Figure 1 提升到首页底部（ACL 模板通常可做到），会显著提升审稿人第一印象锚定效果\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（Method overview）caption 自包含性良好，能独立传达核心 idea（predictor → KL divergence → Gumbel-Sigmoid → TEAL top-k）。图中文字在 150dpi 下可读，但部分标注字号偏小（约正文 60%），建议适当放大\"}, {\"severity\": \"warning\", \"dimension\": \"page 3-4\", \"message\": \"连续 2 页无 figure/table。Page 3 是 Related Work → Method 过渡，Page 4 全为公式推导。虽然 Page 4 有 4 个 displayed equations 提供视觉节奏，但审稿人快速翻阅时可能感觉文本墙偏重。如有空间可考虑将 Table 1（当前在 p5）前移至 p4\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1（Taxonomy of Sparsity Prediction Methods）为全新贡献（二维分类框架），位置合理，放在 Method 末尾帮助审稿人理解方法定位。表格使用 booktabs 风格，格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"纯文本页（Experimental Setup：模型、训练、评估、baseline 描述）。位于 Table 1 (p5) 和 Tables 2-3 (p7) 之间，仅 1 页间隔，节奏可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"表格密集页：Table 2（主结果）+ Table 3（target-swap ablation）+ Table 4（设计消融）。所有表格使用 booktabs 风格，最优值加粗，精度一致（小数位统一）。列宽合理，无溢出。审稿人关注的核心数据集中在此页，信息效率高\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"内容密度高：Figure 2 + Section 4.5/4.6 + Section 5 Conclusion + Limitations 起始。Conclusion 约占左栏 1/2，篇幅适中。Limitations 从右栏底部开始（不计入 8 页限制），主体正文恰好 8 页，符合 ACL 要求\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2（PPL scaling with sparsity）：单栏图，两条曲线（KL predictor vs vanilla TEAL），颜色区分度可（蓝/橙系），axis label 可读。建议在 caption 中补充\\\"lower is better\\\"方向提示\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Ethics Statement 简洁（约 1/3 栏），References 从同页开始。格式符合 ACL 模板要求\"}, {\"severity\": \"info\", \"dimension\": \"
…[truncated 1868 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2026 · 2026-05-23T00:45:52.314873+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2027 · 2026-05-23T00:45:53.770611+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 2028 · 2026-05-23T00:49:05.872665+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 25 (Fresh Review) — Active issues\n  # ============================================================\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL decomposition 的 train-inference mismatch confound 未解决\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 25\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。K=4 single-seed。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N2。97.5% 精确数字不可靠。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C1。K=1 有 32× train-inference mismatch；K=4 在 50% 反常差于 K=1 (44.23 vs 34.85) 缺乏机制解释；仅两个 K 值不足以支撑 29-97% 精确分解。定性结论（signal type matters）由 Table 4 五种 loss 对比和梯度分析独立支撑。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 N1/N2。K=4 at 50% 反常（PPL 44.23 > K=1 34.85）仍仅有 gradient interference speculation 无实验证据。MMLU K=4 > E2E anomaly 暴露 allocation confound（K=4 near-uniform std=0.003 vs E2E non-uniform），decomposition 的两个维度不正交。Abstract/Conclusion 仍基于 30% 结果做 general claim 但 50% 下框架失效。两位 reviewer 一致认为这是核心可信度问题。\"}\n    action_items:\n      - {round: 21, action: \"K=4 3-seed (s42/s123/s456)\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"97.5% → 定性 'majority of PPL gap'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"K=4 50% s42 PPL-only 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 24, action: \"Abstract/Conclusion 的 decomposition claim 删除精确百分比改为定性描述\", assigned_to: \"paper_agent\", status: done}\n      - {round: 24, action: \"K=4 50% 反常结果补假设性解释（gradient interference at high sparsity）\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"Abstract/Conclusion 中限定 decomposition 结论适用范围为 moderate sparsity (30%)\", assigned_to: \"paper_agent\", status: open}\n      - {round: 25, action: \"正文 §4.5 明确讨论 allocation confound（K=4 改变 allocation pattern 导致无法独立归因 coupling）\", assigned_to: \"paper_agent\", status: open}\n      - {round: 25, action: \"考虑 K=2/K=8/K=16 实验追踪 PPL vs K 趋势，或限制 decomposition 仅 30% 有效\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨架构系统性退步缺乏机制分析\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 25\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。Protection valley 分析仅 correlational。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N3。要求追踪 Remove Valley + task-aware allocation。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C2。Remove valley 方向正确但不够——未回答 WHY KL 系统性学到牺牲知识路径的 allocation。8B MMLU -5.2pp, 14B GSM8K -20pp。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 两位 reviewer 的共同最高优先级问题。§4.2 两个假设（WikiText 偏差 + forward KL mode-covering）仍仅 speculation，无任何控制实验验证。Appendix T remove-valley 结果（MMLU +3.4pp, GSM8K +1.6pp）暗示 regression 部分源于 allocation 而非 loss function，但此发现在正文中不够突出。跨规模趋势加剧：8B MMLU -5.2pp → 14B GSM8K -20pp。\"}\n    action_items:\n      - {round: 21, action: \"Constraint 实验 (protect_late + remove_valley)\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"§4.2 深化: Geva 引用 + task-aware allocation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 24, action: \"§4.2 补机制假设段（WikiText-103 分布偏差 + forward KL mode-covering）\", assigned_to: \"paper_agent\", status: done}\n      - {round: 24, action: \"引用 Meng et al. 2022 分析知识存储层 mask 差异\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"至少一个控制实验验证假设：(a) C4/RedPajama 训练 predictor 测试数据偏差假设，或 (b) knowledge-layer neuron retention 对比 KL vs magnitude\", assigned_to: \"main_agent\", status: open}\n      - {round: 25, action: \"Appendix T constraint analysis 结论提升到正文 §4.2，讨论 allocation-aware training 可能性\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-N1\"\n    summary: \"方法新颖性边界需更清晰论证\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - {round: 25, reviewers: [2], note: \"R2 Critical。核心组件（KL+Gumbel-Sigmoid+predictor arch）均为成熟技术，MaskLLM 已用 KL+Gumbel-Softmax 训练 mask。三点区分更多来自应用场景不同而非方法论创新。R1 部分同意但指出：(1) contextual vs static 确实是不同优化问题；(2) 论文已自定位为 empirical study；(3) C1 ablation 和 decomposition 的实验设计本身有新颖性。两位共识：应更早更显著承认组件非新颖性，将 C1 和 decomposition 置于 contribution list 首位。\"}\n    action_items:\n      - {round: 25, action: \"Introduction contribution list 重排：C1 ablation + decomposition 置于首位，ranking across five losses 降级\", assigned_to: \"paper_agent\", status: open}\n      - {round: 25, action: \"Introduction 更早承认组件层面非新颖性（不仅在 Related Work 中提及）\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W1\"\n    summary: \"评估覆盖度关键空白：无生成任务、固定 seq_len=2048、无 batched inference\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 25\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"无 MT-Bench/AlpacaEval 等生成任务；seq length 固定 2048；batched inference 未评估。\"}\n      - {round: 25, reviewers: [2], note: \"R2 W3 仍提出缺少生成评估。R1 factual rebuttal 有效：base model 不适用 MT-Bench/AlpacaEval（需 instruction-tuned）。Limitations 已覆盖此点。降为 info。\"}\n    action_items:\n      - {round: 24, action: \"Limitations 加入 '生成任务未评估' 作为限制点\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W2\"\n    summary: \"高方差下游指标（ARC-c σ=3.6, BoolQ σ=11.5）统计可靠性不足\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 25\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"ARC-c 3-seed 95% CI ≈ ±8.9pp，差异统计不显著。Table 4 多行仅 s42。PPL primary metric 方差极低（σ=0.02），结论可靠。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 Qwen-14B GSM8K uniform 3-seed std=5.2pp (CV=16.3%)。R2 partial rebut 指出 -20pp 非单 seed 但高方差使统计力有限。建议引用时使用完整 32.0±5.2 vs 52.1 而非仅 '-20pp'。\"}\n    action_items:\n      - {round: 24, action: \"正文对高方差指标加注 'not statistically significant'\", assigned_to: \"paper_agent\", status: pending}\n      - {round: 24, action: \"Table 4 关键行补充 3-seed — DDL 不允许，改为加 caveat\", assigned_to: \"paper_agent\", status: pending}\n      - {round: 25, action: \"§4.6 引用 Qwen-14B GSM8K 时使用完整 32.0±5.2 vs 52.1 格式\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W3\"\n    summary: \"C1 ablation soft→hard mask representation 残余 confound + s42 oracle provenance\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 25\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"Oracle 二值化 logits>0 丢失排序信息。定性结论（mask patterns transfer, PPL within 0.79pp）稳健，精确量化不可靠。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 两位 reviewer 均指出 s42 oracle 来自 earlier checkpoint（gap 0.65pp），而 s123/s456 matched oracle gap ≤0.03pp。s42 是 Table 3 中最显眼第一行且唯一有 50% 数据的 seed。建议为 s42 补训 matched oracle 或调整展示顺序优先展示 s123/s456。\"}\n    action_items:\n      - {round: 24, action: \"讨论 oracle 提取信息损失的可能性\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"为 s42 补训 matched oracle 消除 provenance confound，或在 Table 3 中优先展示 s123/s456\", assigned_to: \"paper_agent\", status: open}\n      - {round: 25, action: \"为 s123 或 s456 补充 50% sparsity C1 结果增强稳健性\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W4\"\n    summary: \"'Dominant design dimension' 声明需资格限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 25\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"定量基础因 per-layer 分解 confound 不可靠。定性方向由 Table 4 五种 loss 和梯度分析支撑。建议软化为 'substantially outperforms'。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 论文已改为 'primary design dimension'，但 R2 仍指出 abstract/conclusion 中 general claim 超出 30% evidence 范围。与 R20-W1 的 decomposition scope 限定问题重叠。\"}\n    action_items:\n      - {round: 24, action: \"'dominant' → 软化措辞\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"abstract/conclusion 中限定 'primary design dimension' 的适用范围（30% moderate sparsity）\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-W1\"\n    summary: \"BCE 30% 缺少 uniform allocation 对比，Table 2 比较不对称\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"Table 2 中 BCE 30% 仅有 global（标注 †），KL 有 global+uniform。无法在相同 allocation strategy 下直接比较 KL vs BCE。两位 reviewer 均指出此不对称性。\"}\n    action_items:\n      - {round: 25, action: \"补充 BCE 30% uniform 数据，或在 caption 中解释为何缺失\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-W2\"\n    summary: \"MSE 50% baseline 仅 seed 42 有效（seed 123 catastrophic PPL=15789）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"MSE 50% 在 Table 4 标注 § 但仅 caption 提及 single-seed。seed 123 catastrophic failure 表明 MSE 在高 sparsity 下高度不稳定。论文在 §3.7 使用 MSE 50% 结果论证 taxonomy 预测力但未注明 single-seed caveat。MSE 30% 3-seed (18.52±1.68) 结论稳健。\"}\n    action_items:\n      - {round: 25, action: \"正文使用 MSE 50% 结果时注明 single-seed caveat，讨论 instability 是 MSE loss 本身问题\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-W3\"\n    summary: \"Introduction '19%' PPL 减少实际为 18.6%\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"§4.1 'reducing TEAL's perplexity by 19% (10.82 → 8.81)'，实际 (10.82-8.81)/10.82=18.58%。两位 reviewer 均指出。同时 Figure 2 caption 使用 14.5%（matched sparsity）而 §4.1 使用 19%（nominal），基准不一致未解释。\"}\n    action_items:\n      - {round: 25, action: \"修正为 18.6% 或 ~19%，在 Figure 2 caption 中注明 matched actual sparsity 28.5%\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-M1\"\n    summary: \"术语不一致：output-distribution alignment/distillation/objective 交替使用\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - {round: 25, reviewers: [2], note: \"R2 指出全文交替使用 'output-distribution alignment'（Intro, Conclusion）、'KL distillation'（§3, §4）、'output-distribution objective'（Abstract）。R1 同意。建议统一为 'output-distribution alignment' 并在首次出现时定义。\"}\n    action_items:\n      - {round: 25, action: \"全文统一术语为 'output-distribution alignment'\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-M2\"\n    summary: \"Eq. 4 s_j 缺少层标 ℓ 上标\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"§3.3 Eq. 4 中 s_j 和 m̃_j 均缺少 ℓ 上标，与 §3.1 中 s^(ℓ) 不一致。\"}\n    action_items:\n      - {round: 25, action: \"Eq. 4 补充 ℓ 上标保持 notation 一致\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 25 — Carried forward (status unchanged or minor update)\n  # ============================================================\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无 speedup\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 25\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。Intro framing 已修改为 empirical study。\"}\n      - {round: 22, reviewers: [1, 2], note: \"降为 Warning。论文已定位为 analysis work。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 W1。仍为 Warning。论文 framing 诚实但实际影响力受限。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 两位 reviewer 仍列为 Should-Fix。论文诚实披露（appreciated），但 6.4% overhead 限制实用影响。R1 建议至少做 Triton block-sparse proof-of-concept。论文 framing 已充分，结构性限制。\"}\n    action_items:\n      - {round: 21, action: \"Abstract 加 empirical study + §1 disclaimer\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"§1 加 speedup 条件 + 6.4% overhead\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"结构性限制。已充分 framed。\"\n    resolution_round: 23\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 25\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。\"}\n      - {round: 22, reviewers: [1, 2], note: \"降为 Warning。R1 REBUT 有效。\"}\n      - {round: 24, reviewers: [2], note: \"R2 再次提出 Critical，但 R1 factual correction 有效。降级为 Warning。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 合并进 R25-N1 (novelty framing)。R1 指出 contextual vs static 确为不同优化问题，区分合理但不够突出。\"}\n    action_items:\n      - {round: 21, action: \"§2 MaskLLM 3-point differentiation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 24, action: \"Introduction 早期建立 MaskLLM 区分\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD variance\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 25\n    mentions:\n      - {round: 22, reviewers: [], note: \"R22 未单独提出（已在 Limitations 讨论）。\"}\n      - {round: 24, reviewers: [1], note: \"R1 指出论文已有充分 OOD 证据（Appendix D: C4 PPL + 下游 Δ≤1.1pp）。\"}\n      - {round: 25, reviewers: [], note: \"R25 未被 reviewer 单独提出。Appendix D OOD 证据被认为充分。\"}\n    action_items:\n      - {round: 20, action: \"Limitations 加 WikiText 同分布 + C4 限制\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot 限制实际影响\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 25\n    mentions:\n      - {round: 24, reviewers: [], note: \"本轮未被 Reviewer 单独提出。论文 Limitations 已覆盖。\"}\n      - {round: 25, reviewers: [], note: \"R25 未单独提出。Limitations 已覆盖。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Carried forward — resolved, unchanged\n  # ============================================================\n\n  - id: \"R22-W5\"\n    summary: \"规模泛化仅 7-14B\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 25\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W5。Qwen-14B GSM8K -20pp。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 W5。跨架构证据仍 preliminary。\"}\n      - {round: 25, reviewers: [1], note: \"R1 指出 Limitations 未讨论 8B→14B regression 加剧对 70B+ 前景的影响。\"}\n    action_items:\n      - {round: 22, action: \"Limitations 加 scale trade-off 讨论\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"Limitations 补充 14B regression 加剧对更大规模前景的讨论\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"Limitations 已包含 'evaluation bounded at 7-14B'。\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"Table 2 actual sparsity mismatch ‡ 脚注不够显著\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 25\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W3。\"}\n      - {round: 24, reviewers: [1], note: \"R1 W5 提及 labeling 仍不够醒目但降为 Minor。\"}\n      - {round: 25, reviewers: [1], note: \"R1 W4 指出 sparsity controller 30% 饱和（λ=5000 cap, actual 28.5%）。R2 partial rebut：Appendix C 已提供 matched-sparsity 对比。\"}\n    action_items:\n      - {round: 22, action: \"§4.1 matched sparsity 独立句\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"§4.1 matched 14.5% 作为独立句。‡ 脚注存在。\"\n    resolution_round: 23\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap ablation 因果声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 24\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Warning。'suggests' hedging 被认可。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N1。排除性声明超出证据。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 新增 W3 (soft→hard confound)。定性结论稳健。\"}\n    action_items:\n      - {round: 22, action: \"降级为 transferability + 删除排除性声明\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"C1 claim 已降级为 transferability。soft→hard confound 作为独立 warning (R24-W3) 追踪。\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"KL global 50% 下游 3-seed 已补全\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W4。Table 2 更新为 3-seed。\"}\n    action_items:\n      - {round: 22, action: \"Table 2 更新为 3-seed mean±std\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Table 2 KL global 50% 全部 3-seed。\"\n    resolution_round: 23\n\n  - id: \"R22-W6\"\n    summary: \"Figure 2 仅展示 global allocation 但推荐 uniform\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 25\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W6。正文 Figure 之一，framing 效果强。\"}\n      - {round: 24, reviewers: [], note: \"R24 Visual check 发现 Figure 2 字号偏小。\"}\n      - {round: 25, reviewers: [], note: \"R25 未单独提出。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W7\"\n    summary: \"Abstract 第5句信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"Abstract 第5句拆为两个清晰句子。\"\n    resolution_round: 23\n\n  - id: \"R22-W8\"\n    summary: \"Conclusion 引用 BoolQ (高 variance, 仅 Appendix)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"Conclusion BoolQ → HellaSwag/PIQA。\"\n    resolution_round: 23\n\n  - id: \"R22-M2\"\n    summary: \"§3.5 deadzone margin ε=0.02 缺乏 justification\"\n    category: method\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"'suppresses oscillation near the target'\"\n    resolution_round: 23\n\n  - id: \"R22-M3\"\n    summary: \"BCE 2700 steps wall-clock 与 KL 1000 steps 接近需解释\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"已解释。\"\n    resolution_round: 23\n\n  - id: \"R22-M4\"\n    summary: \"'Adaptive Penalty Controller' 命名不准确\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"重命名为 'Geometric Penalty Schedule'。\"\n    resolution_round: 23\n\n  - id: \"R22-M6\"\n    summary: \"Limitations 未讨论 sequence length\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"已修复。Limitations 包含 seq length。\"}\n    resolution: \"已修复。\"\n    resolution_round: 23\n\n  - id: \"R19-W4\"\n    summary: \"MSE baseline 50% s123 灾难性失败\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 25\n    mentions:\n      - {round: 24, reviewers: [1], note: \"R1 Q5 问 MSE 30% 3-seed 是否含所有 seed。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 MSE 50% single-seed caveat 升级为 R25-W2。\"}\n    resolution: \"Instability 本身是 finding。\"\n    resolution_round: 22\n\n  - id: \"R19-W3\"\n    summary: \"Knowledge-intensive 退步缺乏机制解释\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 22\n    resolution: \"合并进 R20-N2。\"\n    resolution_round: 23\n\n  - id: \"R21-W2\"\n    summary: \"符号冲突 g→ε\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"method.tex g1/g2 → ε1/ε2。\"\n    resolution_round: 22\n\n  - id: \"R20-N3\"\n    summary: \"'Coupling alignment' 术语替换\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    resolution: \"术语替换完成。\"\n    resolution_round: 21\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 25\n    mentions:\n      - {round: 24, reviewers: [2], note: \"R2 再次提出但 R1 factual rebuttal 有效。合并进 R19-W1。\"}\n      - {round: 25, reviewers: [2], note: \"R25 合并进 R25-N1 (novelty framing)。\"}\n    resolution: \"§2 三点本质差异。\"\n    resolution_round: 23\n\n  - id: \"R19-W6\"\n    summary: \"Actual sparsity mismatch 在主表不够显著\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 22\n    resolution: \"合并进 R22-W3。\"\n    resolution_round: 23"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 25 (Fresh Review) — Active issues\n  # ============================================================\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL decomposition 的 train-inference mismatch confound 未解决\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 25\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。K=4 single-seed。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N2。97.5% 精确数字不可靠。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C1。K=1 有 32× train-inference mismatch；K=4 在 50% 反常差于 K=1 (44.23 vs 34.85) 缺乏机制解释；仅两个 K 值不足以支撑 29-97% 精确分解。定性结论（signal type matters）由 Table 4 五种 loss 对比和梯度分析独立支撑。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 N1/N2。K=4 at 50% 反常（PPL 44.23 > K=1 34.85）仍仅有 gradient interference speculation 无实验证据。MMLU K=4 > E2E anomaly 暴露 allocation confound（K=4 near-uniform std=0.003 vs E2E non-uniform），decomposition 的两个维度不正交。Abstract/Conclusion 仍基于 30% 结果做 general claim 但 50% 下框架失效。两位 reviewer 一致认为这是核心可信度问题。\"}\n    action_items:\n      - {round: 21, action: \"K=4 3-seed (s42/s123/s456)\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"97.5% → 定性 'majority of PPL gap'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"K=4 50% s42 PPL-only 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 24, action: \"Abstract/Conclusion 的 decomposition claim 删除精确百分比改为定性描述\", assigned_to: \"paper_agent\", status: done}\n      - {round: 24, action: \"K=4 50% 反常结果补假设性解释（gradient interference at high sparsity）\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"Abstract/Conclusion 中限定 decomposition 结论适用范围为 moderate sparsity (30%)\", assigned_to: \"paper_agent\", status: open}\n      - {round: 25, action: \"正文 §4.5 明确讨论 allocation confound（K=4 改变 allocation pattern 导致无法独立归因 coupling）\", assigned_to: \"paper_agent\", status: open}\n      - {round: 25, action: \"考虑 K=2/K=8/K=16 实验追踪 PPL vs K 趋势，或限制 decomposition 仅 30% 有效\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨架构系统性退步缺乏机制分析\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 25\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。Protection valley 分析仅 correlational。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N3。要求追踪 Remove Valley + task-aware allocation。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C2。Remove valley 方向正确但不够——未回答 WHY KL 系统性学到牺牲知识路径的 allocation。8B MMLU -5.2pp, 14B GSM8K -20pp。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 两位 reviewer 的共同最高优先级问题。§4.2 两个假设（WikiText 偏差 + forward KL mode-covering）仍仅 speculation，无任何控制实验验证。Appendix T remove-valley 结果（MMLU +3.4pp, GSM8K +1.6pp）暗示 regression 部分源于 allocation 而非 loss function，但此发现在正文中不够突出。跨规模趋势加剧：8B MMLU -5.2pp → 14B GSM8K -20pp。\"}\n    action_items:\n      - {round: 21, action: \"Constraint 实验 (protect_late + remove_valley)\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"§4.2 深化: Geva 引用 + task-aware allocation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 24, action: \"§4.2 补机制假设段（WikiText-103 分布偏差 + forward KL mode-covering）\", assigned_to: \"paper_agent\", status: done}\n      - {round: 24, action: \"引用 Meng et al. 2022 分析知识存储层 mask 差异\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"至少一个控制实验验证假设：(a) C4/RedPajama 训练 predictor 测试数据偏差假设，或 (b) knowledge-layer neuron retention 对比 KL vs magnitude\", assigned_to: \"main_agent\", status: open}\n      - {round: 25, action: \"Appendix T constraint analysis 结论提升到正文 §4.2，讨论 allocation-aware training 可能性\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-N1\"\n    summary: \"方法新颖性边界需更清晰论证\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - {round: 25, reviewers: [2], note: \"R2 Critical。核心组件（KL+Gumbel-Sigmoid+predictor arch）均为成熟技术，MaskLLM 已用 KL+Gumbel-Softmax 训练 mask。三点区分更多来自应用场景不同而非方法论创新。R1 部分同意但指出：(1) contextual vs static 确实是不同优化问题；(2) 论文已自定位为 empirical study；(3) C1 ablation 和 decomposition 的实验设计本身有新颖性。两位共识：应更早更显著承认组件非新颖性，将 C1 和 decomposition 置于 contribution list 首位。\"}\n    action_items:\n      - {round: 25, action: \"Introduction contribution list 重排：C1 ablation + decomposition 置于首位，ranking across five losses 降级\", assigned_to: \"paper_agent\", status: open}\n      - {round: 25, action: \"Introduction 更早承认组件层面非新颖性（不仅在 Related Work 中提及）\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W1\"\n    summary: \"评估覆盖度关键空白：无生成任务、固定 seq_len=2048、无 batched inference\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 25\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"无 MT-Bench/AlpacaEval 等生成任务；seq length 固定 2048；batched inference 未评估。\"}\n      - {round: 25, reviewers: [2], note: \"R2 W3 仍提出缺少生成评估。R1 factual rebuttal 有效：base model 不适用 MT-Bench/AlpacaEval（需 instruction-tuned）。Limitations 已覆盖此点。降为 info。\"}\n    action_items:\n      - {round: 24, action: \"Limitations 加入 '生成任务未评估' 作为限制点\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W2\"\n    summary: \"高方差下游指标（ARC-c σ=3.6, BoolQ σ=11.5）统计可靠性不足\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 25\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"ARC-c 3-seed 95% CI ≈ ±8.9pp，差异统计不显著。Table 4 多行仅 s42。PPL primary metric 方差极低（σ=0.02），结论可靠。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 Qwen-14B GSM8K uniform 3-seed std=5.2pp (CV=16.3%)。R2 partial rebut 指出 -20pp 非单 seed 但高方差使统计力有限。建议引用时使用完整 32.0±5.2 vs 52.1 而非仅 '-20pp'。\"}\n    action_items:\n      - {round: 24, action: \"正文对高方差指标加注 'not statistically significant'\", assigned_to: \"paper_agent\", status: pending}\n      - {round: 24, action: \"Table 4 关键行补充 3-seed — DDL 不允许，改为加 caveat\", assigned_to: \"paper_agent\", status: pending}\n      - {round: 25, action: \"§4.6 引用 Qwen-14B GSM8K 时使用完整 32.0±5.2 vs 52.1 格式\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W3\"\n    summary: \"C1 ablation soft→hard mask representation 残余 confound + s42 oracle provenance\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 25\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"Oracle 二值化 logits>0 丢失排序信息。定性结论（mask patterns transfer, PPL within 0.79pp）稳健，精确量化不可靠。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 两位 reviewer 均指出 s42 oracle 来自 earlier checkpoint（gap 0.65pp），而 s123/s456 matched oracle gap ≤0.03pp。s42 是 Table 3 中最显眼第一行且唯一有 50% 数据的 seed。建议为 s42 补训 matched oracle 或调整展示顺序优先展示 s123/s456。\"}\n    action_items:\n      - {round: 24, action: \"讨论 oracle 提取信息损失的可能性\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"为 s42 补训 matched oracle 消除 provenance confound，或在 Table 3 中优先展示 s123/s456\", assigned_to: \"paper_agent\", status: open}\n      - {round: 25, action: \"为 s123 或 s456 补充 50% sparsity C1 结果增强稳健性\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W4\"\n    summary: \"'Dominant design dimension' 声明需资格限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 25\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"定量基础因 per-layer 分解 confound 不可靠。定性方向由 Table 4 五种 loss 和梯度分析支撑。建议软化为 'substantially outperforms'。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 论文已改为 'primary design dimension'，但 R2 仍指出 abstract/conclusion 中 general claim 超出 30% evidence 范围。与 R20-W1 的 decomposition scope 限定问题重叠。\"}\n    action_items:\n      - {round: 24, action: \"'dominant' → 软化措辞\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"abstract/conclusion 中限定 'primary design dimension' 的适用范围（30% moderate sparsity）\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-W1\"\n    summary: \"BCE 30% 缺少 uniform allocation 对比，Table 2 比较不对称\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"Table 2 中 BCE 30% 仅有 global（标注 †），KL 有 global+uniform。无法在相同 allocation strategy 下直接比较 KL vs BCE。两位 reviewer 均指出此不对称性。\"}\n    action_items:\n      - {round: 25, action: \"补充 BCE 30% uniform 数据，或在 caption 中解释为何缺失\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-W2\"\n    summary: \"MSE 50% baseline 仅 seed 42 有效（seed 123 catastrophic PPL=15789）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"MSE 50% 在 Table 4 标注 § 但仅 caption 提及 single-seed。seed 123 catastrophic failure 表明 MSE 在高 sparsity 下高度不稳定。论文在 §3.7 使用 MSE 50% 结果论证 taxonomy 预测力但未注明 single-seed caveat。MSE 30% 3-seed (18.52±1.68) 结论稳健。\"}\n    action_items:\n      - {round: 25, action: \"正文使用 MSE 50% 结果时注明 single-seed caveat，讨论 instability 是 MSE loss 本身问题\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-W3\"\n    summary: \"Introduction '19%' PPL 减少实际为 18.6%\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"§4.1 'reducing TEAL's perplexity by 19% (10.82 → 8.81)'，实际 (10.82-8.81)/10.82=18.58%。两位 reviewer 均指出。同时 Figure 2 caption 使用 14.5%（matched sparsity）而 §4.1 使用 19%（nominal），基准不一致未解释。\"}\n    action_items:\n      - {round: 25, action: \"修正为 18.6% 或 ~19%，在 Figure 2 caption 中注明 matched actual sparsity 28.5%\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-M1\"\n    summary: \"术语不一致：output-distribution alignment/distillation/objective 交替使用\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - {round: 25, reviewers: [2], note: \"R2 指出全文交替使用 'output-distribution alignment'（Intro, Conclusion）、'KL distillation'（§3, §4）、'output-distribution objective'（Abstract）。R1 同意。建议统一为 'output-distribution alignment' 并在首次出现时定义。\"}\n    action_items:\n      - {round: 25, action: \"全文统一术语为 'output-distribution alignment'\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-M2\"\n    summary: \"Eq. 4 s_j 缺少层标 ℓ 上标\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"§3.3 Eq. 4 中 s_j 和 m̃_j 均缺少 ℓ 上标，与 §3.1 中 s^(ℓ) 不一致。\"}\n    action_items:\n      - {round: 25, action: \"Eq. 4 补充 ℓ 上标保持 notation 一致\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 25 — Carried forward (status unchanged or minor update)\n  # ============================================================\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无 speedup\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 25\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。Intro framing 已修改为 empirical study。\"}\n      - {round: 22, reviewers: [1, 2], note: \"降为 Warning。论文已定位为 analysis work。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 W1。仍为 Warning。论文 framing 诚实但实际影响力受限。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 两位 reviewer 仍列为 Should-Fix。论文诚实披露（appreciated），但 6.4% overhead 限制实用影响。R1 建议至少做 Triton block-sparse proof-of-concept。论文 framing 已充分，结构性限制。\"}\n    action_items:\n      - {round: 21, action: \"Abstract 加 empirical study + §1 disclaimer\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"§1 加 speedup 条件 + 6.4% overhead\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"结构性限制。已充分 framed。\"\n    resolution_round: 23\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 25\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。\"}\n      - {round: 22, reviewers: [1, 2], note: \"降为 Warning。R1 REBUT 有效。\"}\n      - {round: 24, reviewers: [2], note: \"R2 再次提出 Critical，但 R1 factual correction 有效。降级为 Warning。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 合并进 R25-N1 (novelty framing)。R1 指出 contextual vs static 确为不同优化问题，区分合理但不够突出。\"}\n    action_items:\n      - {round: 21, action: \"§2 MaskLLM 3-point differentiation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 24, action: \"Introduction 早期建立 MaskLLM 区分\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD variance\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 25\n    mentions:\n      - {round: 22, reviewers: [], note: \"R22 未单独提出（已在 Limitations 讨论）。\"}\n      - {round: 24, reviewers: [1], note: \"R1 指出论文已有充分 OOD 证据（Appendix D: C4 PPL + 下游 Δ≤1.1pp）。\"}\n      - {round: 25, reviewers: [], note: \"R25 未被 reviewer 单独提出。Appendix D OOD 证据被认为充分。\"}\n    action_items:\n      - {round: 20, action: \"Limitations 加 WikiText 同分布 + C4 限制\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot 限制实际影响\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 25\n    mentions:\n      - {round: 24, reviewers: [], note: \"本轮未被 Reviewer 单独提出。论文 Limitations 已覆盖。\"}\n      - {round: 25, reviewers: [], note: \"R25 未单独提出。Limitations 已覆盖。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Carried forward — resolved, unchanged\n  # ============================================================\n\n  - id: \"R22-W5\"\n    summary: \"规模泛化仅 7-14B\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 25\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W5。Qwen-14B GSM8K -20pp。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 W5。跨架构证据仍 preliminary。\"}\n      - {round: 25, reviewers: [1], note: \"R1 指出 Limitations 未讨论 8B→14B regression 加剧对 70B+ 前景的影响。\"}\n    action_items:\n      - {round: 22, action: \"Limitations 加 scale trade-off 讨论\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"Limitations 补充 14B regression 加剧对更大规模前景的讨论\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"Limitations 已包含 'evaluation bounded at 7-14B'。\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"Table 2 actual sparsity mismatch ‡ 脚注不够显著\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 25\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W3。\"}\n      - {round: 24, reviewers: [1], note: \"R1 W5 提及 labeling 仍不够醒目但降为 Minor。\"}\n      - {round: 25, reviewers: [1], note: \"R1 W4 指出 sparsity controller 30% 饱和（λ=5000 cap, actual 28.5%）。R2 partial rebut：Appendix C 已提供 matched-sparsity 对比。\"}\n    action_items:\n      - {round: 22, action: \"§4.1 matched sparsity 独立句\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"§4.1 matched 14.5% 作为独立句。‡ 脚注存在。\"\n    resolution_round: 23\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap ablation 因果声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 24\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Warning。'suggests' hedging 被认可。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N1。排除性声明超出证据。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 新增 W3 (soft→hard confound)。定性结论稳健。\"}\n    action_items:\n      - {round: 22, action: \"降级为 transferability + 删除排除性声明\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"C1 claim 已降级为 transferability。soft→hard confound 作为独立 warning (R24-W3) 追踪。\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"KL global 50% 下游 3-seed 已补全\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W4。Table 2 更新为 3-seed。\"}\n    action_items:\n      - {round: 22, action: \"Table 2 更新为 3-seed mean±std\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Table 2 KL global 50% 全部 3-seed。\"\n    resolution_round: 23\n\n  - id: \"R22-W6\"\n    summary: \"Figure 2 仅展示 global allocation 但推荐 uniform\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 25\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"R22 W6。正文 Figure 之一，framing 效果强。\"}\n      - {round: 24, reviewers: [], note: \"R24 Visual check 发现 Figure 2 字号偏小。\"}\n      - {round: 25, reviewers: [], note: \"R25 未单独提出。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W7\"\n    summary: \"Abstract 第5句信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"Abstract 第5句拆为两个清晰句子。\"\n    resolution_round: 23\n\n  - id: \"R22-W8\"\n    summary: \"Conclusion 引用 BoolQ (高 variance, 仅 Appendix)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"Conclusion BoolQ → HellaSwag/PIQA。\"\n    resolution_round: 23\n\n  - id: \"R22-M2\"\n    summary: \"§3.5 deadzone margin ε=0.02 缺乏 justification\"\n    category: method\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"'suppresses oscillation near the target'\"\n    resolution_round: 23\n\n  - id: \"R22-M3\"\n    summary: \"BCE 2700 steps wall-clock 与 KL 1000 steps 接近需解释\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"已解释。\"\n    resolution_round: 23\n\n  - id: \"R22-M4\"\n    summary: \"'Adaptive Penalty Controller' 命名不准确\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"重命名为 'Geometric Penalty Schedule'。\"\n    resolution_round: 23\n\n  - id: \"R22-M6\"\n    summary: \"Limitations 未讨论 sequence length\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"已修复。Limitations 包含 seq length。\"}\n    resolution: \"已修复。\"\n    resolution_round: 23\n\n  - id: \"R19-W4\"\n    summary: \"MSE baseline 50% s123 灾难性失败\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 25\n    mentions:\n      - {round: 24, reviewers: [1], note: \"R1 Q5 问 MSE 30% 3-seed 是否含所有 seed。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 MSE 50% single-seed caveat 升级为 R25-W2。\"}\n    resolution: \"Instability 本身是 finding。\"\n    resolution_round: 22\n\n  - id: \"R19-W3\"\n    summary: \"Knowledge-intensive 退步缺乏机制解释\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 22\n    resolution: \"合并进 R20-N2。\"\n    resolution_round: 23\n\n  - id: \"R21-W2\"\n    summary: \"符号冲突 g→ε\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"method.tex g1/g2 → ε1/ε2。\"\n    resolution_round: 22\n\n  - id: \"R20-N3\"\n    summary: \"'Coupling alignment' 术语替换\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    resolution: \"术语替换完成。\"\n    resolution_round: 21\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 25\n    mentions:\n      - {round: 24, reviewers: [2], note: \"R2 再次提出但 R1 factual rebuttal 有效。合并进 R19-W1。\"}\n      - {round: 25, reviewers: [2], note: \"R25 合并进 R25-N1 (novelty framing)。\"}\n    resolution: \"§2 三点本质差异。\"\n    resolution_round: 23\n\n  - id: \"R19-W6\"\n    summary: \"Actual sparsity mismatch 在主表不够显著\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 22\n    resolution: \"合并进 R22-W3。\"\n    resolution_round: 23"
  }
}
```

</details>

---


### Tool result

_source line 2029 · 2026-05-23T00:49:06.826797+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 20850}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2030 · 2026-05-23T00:51:46.784762+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "report": "# Round 25 审稿报告（Fresh Review）\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**目标 Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）\n**轮次**: 1 轮（交叉分享后关键问题达成共识，无需第 2 轮）\n\n---\n\n## Summary\n\n本文提出用前向 KL 散度替代 BCE 训练 SwiGLU LLM 的轻量级稀疏性预测器（<1% base 参数）。核心 insight 是 KL 将所有 mask 决策通过输出分布耦合，发现的 mask patterns 与 magnitude-based 方法分歧 46-68%，但产生显著更优的 PPL（LLaMA-3.1-8B 30% sparsity 下减少 14.5%）。C1 target-swap ablation 将 KL 优势解耦为 signal type（output-distribution vs intermediate loss）和 coupling scope，发现 signal type 在 30% 下主导 PPL 差距（upper bound）。跨架构评估（Mistral-7B, Qwen-14B）确认 PPL 泛化但知识密集型任务系统性退化。论文自定位为 empirical study；无 wall-clock speedup（+6.4% overhead）。\n\n---\n\n## Strengths\n\n**S1** [两位 reviewer 共识] **C1 target-swap ablation 设计巧妙**：将 KL 发现的 mask targets 转移给 BCE 训练，干净地分离了 \"what\"（mask pattern quality）和 \"how\"（gradient coupling mechanism）的贡献。max Δ≤0.79pp（50% s42）证明 KL 发现的 mask 模式是质量优势的主要来源。这是论文最有洞察力的实验。\n\n**S2** [两位 reviewer 共识] **实验控制质量高**：KL / BCE / MSE 使用完全相同的 architecture（2-layer MLP, d_b=128）、data（WikiText-103）、optimizer（AdamW）、steps（1000），仅改变 loss function。3-seed 评估用于主要结果，PPL 标准差极低（±0.02）。这种 controlled comparison 在 empirical ML 论文中并不常见。\n\n**S3** [两位 reviewer 共识] **诚实且全面的 limitations 披露**：明确承认无 wall-clock speedup、knowledge-task regression、training data homogeneity、evaluation bounds。Abstract 使用更保守的 14.5%（matched sparsity）而非 18.6%（nominal）。Claims 有适当 hedging（\"upper bound\"、\"suggests\"、\"primarily empirical\"）。\n\n**S4** **丰富的 appendix**（~18 个 display items）：从 bottleneck sensitivity 到 temperature schedule 到 training convergence 到 cross-seed mask consistency 到 OOD evaluation，覆盖了大部分可预见的 reviewer 问题。\n\n**S5** **Compensation redundancy finding**：发现 KL predictor 使得额外的 67.2M 参数补偿网络冗余，简化推理管线——实用且有信息量。\n\n**S6** **2D taxonomy**（Table 1）提供了有用的组织框架：correction granularity × training signal coupling，帮助定位论文贡献和 prior work。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1** [critical, 两位 reviewer 共识] **Coupling decomposition 在 50% sparsity 下失效且存在 allocation confound**\n\n- **K=4 at 50% 反常**：K=4 per-layer KL PPL=44.23 **劣于** K=1 的 34.85，而 E2E KL 为 11.84。如果增加 masked layers（K=1→K=4）应缩小与 E2E 差距，但实际差距从 +23.06 扩大到 +32.44。论文的 \"gradient interference\" 解释（§4.5）是 speculation，无实验证据。\n- **MMLU allocation confound**：K=4 在 MMLU 上系统性超过 E2E（42.7±1.4 vs 40.7±1.3，3 个 seed 均是），因为 K=4 产生 near-uniform allocation（std=0.003）匹配了 uniform inference protocol，而 E2E 产生非均匀分配（L14-L18 valley）。因此 decomposition 的两个维度不正交，无法独立归因 coupling vs allocation 效应。\n- **General claims 超出 evidence 范围**：Abstract（\"Signal type accounts for the majority of the PPL gap\"）和 Conclusion 基于 30% 结果做 general claim，但 decomposition 在 50% 下不成立。\n- **建议**：(1) Abstract/Conclusion 限定为 \"at moderate sparsity (30%)\"；(2) 正文 §4.5 显著讨论 allocation confound；(3) 补充 K=2/K=8 实验追踪趋势，或明确放弃 50% 下的 decomposition 分析。\n\n**C2** [critical, 两位 reviewer 共识] **知识密集型任务系统性退化仅有假设无控制实验**\n\n- 跨所有规模一致退化：8B MMLU -5.2pp，Mistral GSM8K -7.3pp，Qwen-14B GSM8K -20pp, MMLU -8.1pp。\n- §4.2 提出两个假设（WikiText-103 数据偏差 + forward KL mode-covering 稀释 rare activations），但明确说 \"await validation via knowledge-neuron probing\"——没有做任何验证实验。\n- Appendix T 的 constraint analysis 已显示 remove-valley → MMLU +3.4pp, GSM8K +1.6pp，暗示 regression 部分源于 learned allocation 而非 loss function 本身，但此关键发现仅在 appendix 中。\n- **建议**：(1) 至少一个控制实验：C4/RedPajama 训练 predictor 测试数据偏差假设，或比较 KL vs magnitude 在 knowledge-critical layers 的 neuron retention 差异；(2) Appendix T 发现提升到正文。\n\n**C3** [warning→critical by consensus] **方法新颖性边界需更清晰论证**\n\n- 核心组件（KL distillation + Gumbel-Sigmoid + predictor arch）均为成熟技术。MaskLLM 已用 KL + Gumbel-Softmax 训练可学习 mask。论文的三点区分合理但更多来自应用场景不同。\n- **R1 nuance**：contextual vs static 确为不同优化问题（predictor 需泛化到未见输入），且论文已自定位为 \"primarily an empirical study\"。C1 ablation 和 per-layer decomposition 的**实验设计**本身有新颖性。\n- **共识建议**：(1) Introduction 更早承认组件层面非新颖性；(2) Contribution list 重排：C1 ablation + decomposition 置于首位（当前第一条是 \"ranking across five losses\"，信息量不如 C1 + decomposition）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [两位 reviewer 共识] **C1 ablation s42 oracle provenance 问题**：s42 oracle 来自 earlier checkpoint（PPL gap 0.65pp at 30%），而 s123/s456 matched oracle gap ≤0.03pp。s42 是 Table 3 第一行且唯一有 50% 数据的 seed。建议为 s42 补训 matched oracle，或优先展示 s123/s456，并补充 s123/s456 在 50% 的 C1 结果。\n\n**W2** [两位 reviewer 共识] **BCE 30% 缺少 uniform allocation 对比**：Table 2 中 BCE 30% 仅有 global（†），KL 有 global+uniform。无法在相同 allocation strategy 下直接比较。建议补充 BCE 30% uniform 或解释缺失原因。\n\n**W3** [两位 reviewer 共识] **MSE 50% single-seed caveat 不充分**：seed 123 catastrophic failure（PPL=15,789），Table 4 的 229.26 仅 seed 42。正文 §3.7 使用 MSE 50% 数据论证 taxonomy 但未注明 single-seed。MSE 30% 3-seed（18.52±1.68）结论稳健。建议正文标注 caveat。\n\n**W4** [两位 reviewer 共识] **无 wall-clock speedup，+6.4% latency overhead**：论文诚实披露（appreciated），但对 sparsity 领域论文实用影响受限。论文 framing 已充分（\"primarily an empirical study\"），结构性限制。\n\n**W5** **Qwen-14B GSM8K 高方差**：uniform 3-seed 32.0±5.2（CV=16.3%），95% CI 约 ±10pp。建议正文引用完整 32.0±5.2 vs 52.1 而非仅 \"-20pp\"。\n\n**W6** **Limitations 未讨论 14B regression 对更大规模的影响**：8B→14B regression 加剧（GSM8K -1.3pp→-20pp），但 Limitations 未讨论 70B+ 前景。\n\n### Minor Issues\n\n**M1** §4.1/Introduction \"19%\" 实际为 18.6%（(10.82-8.81)/10.82=18.58%）。Figure 2 caption 使用 14.5%（matched sparsity）而 §4.1 使用 19%（nominal），基准不一致。\n\n**M2** 术语不一致：\"output-distribution alignment\"/\"distillation\"/\"objective\" 交替使用，建议统一。\n\n**M3** Eq. 4 s_j 和 m̃_j 缺少层标 ℓ 上标，与 §3.1 notation 不一致。\n\n**M4** §3.4 T（distillation temperature）与 §3.3 τ（Gumbel temperature）使用不同符号但未明确区分，可能造成困惑。\n\n**M5** Table 4 STE 30% 仅达 20.8% actual sparsity（‡），与其他方法在不同实际 sparsity 下对比，公平性有限。\n\n---\n\n## Reviewer Consensus\n\n两位 reviewer 评分一致（Overall 3.5, Soundness 3.5, Excitement 3, Confidence 4），在以下核心评估上达成共识：\n\n| 问题 | 共识状态 |\n|------|----------|\n| C1: Coupling decomposition 在 50% 失效 + allocation confound | [AGREE] 两位均列为 Critical |\n| C2: Knowledge regression 缺机制分析 | [AGREE] R1 W1 + R2 N1，两位均认为最高优先级 |\n| C3: 方法新颖性边界 | [AGREE with nuance] R2 Critical, R1 部分同意但指出实验设计新颖性 |\n| W1: C1 s42 oracle provenance | [AGREE] 两位均指出 |\n| W2: BCE 30% 缺 uniform | [AGREE] 两位均指出 |\n| W4: 无 wall-clock speedup | [AGREE] 结构性限制，framing 已充分 |\n| S1-S3: C1 ablation 巧妙 + 实验控制 + 诚实 limitations | [AGREE] 两位共同认可的主要优势 |\n\n---\n\n## Reviewer Divergence\n\n| 分歧点 | R1 立场 | R2 立场 | 解决 |\n|--------|---------|---------|------|\n| 缺少 MT-Bench/AlpacaEval | [REBUT] Base model 不适用 instruction-following benchmarks | [Should-Fix] 缺少生成评估 | **R1 rebuttal 有效**：论文评估 base model，MT-Bench 需 instruction-tuned。Limitations 已覆盖。不计入最终 weakness |\n| Conclusion 过于简洁 | [REBUT] 简洁但完整，ARR 无格式要求 | Minor issue | **R1 rebuttal 有效**：Conclusion 覆盖了核心发现、key result、limitations、code release |\n| GPU 型号 double-blind 风险 | [REBUT] 商用 GPU，不构成 de-anonymization | Minor concern | **R1 rebuttal 有效**：RTX PRO 6000 是 2025 年商用 GPU，不比 A100 更具识别性 |\n| Qwen-14B 单 seed vs 多 seed | [Critical] 单 seed 不足 | [Partial REBUT] 实为 3-seed 但高方差 | **R2 factual correction 有效**：GSM8K uniform 是 3-seed (32.0±5.2)，非单 seed。降级为 Warning（高方差限制统计力）|\n| Sparsity controller 30% 饱和 | [Should-Fix] λ=5000 cap, 28.5% | [Partial REBUT] Appendix C matched-sparsity 对比充分 | **R2 rebut 部分有效**：matched comparison 已提供，但建议在正文中讨论 deviation |\n\n---\n\n## Questions\n\n1. K=4 at 50% 为什么比 K=1 差？是否有 K=2/K=8 数据追踪 PPL vs K 趋势？\n2. 如果在 K=4 实验中强制使用 E2E KL 的 per-layer allocation（而非 K=4 自然学出的 near-uniform），MMLU anomaly 是否消失？\n3. 是否尝试过在 math-heavy 数据（如 GSM8K 训练集或 math subset of C4）上训练 predictor 来检验 knowledge regression 是否源于数据偏差？\n4. BCE 30% 为什么缺少 uniform allocation 数据？是否存在 BCE uniform 表现更差的情况？\n5. Appendix T 的 remove-valley 实验中，是否存在同时改善 MMLU 和 ARC-c 的 per-layer allocation 配置？\n\n---\n\n## Missing References\n\n论文 Related Work 覆盖面相当完善（50+ 引用），两位 reviewer 未发现重大遗漏。建议检查：\n- 2026 年 1-5 月是否有新的 KL distillation for activation sparsity 工作\n- TurboSparse 系列后续工作的更新引用\n\nMissing references 不构成接收障碍。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（耗时 4 分 20 秒）\n\n**统计**：0 critical, 3 warning, 17 info\n\n**Warnings**:\n1. **Page 3-4 连续 2 页无 figure/table**：Related Work → Method 过渡，可考虑将 Table 1 前移至 p4\n2. **Page 13（附录）极高密度**：Table 7 + 8 + 9 + Figure 3 + Table 10 + 3 subsections 挤入单页，阅读体验欠佳\n3. **Page 17（附录）底部拥挤**：Table 15 + Figure 7 + Table 16-17 密集堆叠\n\n**Info highlights**:\n- 主体正文恰好 8 页，符合 ACL 要求\n- 全文 6 个 display items（2 Figure + 4 Table），密度 0.75/页，适中\n- 未见 margin overflow、公式渲染错误、[?] 未解析引用\n- References 格式统一（ACL natbib），无异常\n- Figure 1 在 p2（可提升到 p1 底部以增强首页视觉锚定）\n\n---\n\n## Overall Assessment\n\n**评分：3.5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3 | 3 | 3 |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4 | 4 | 4 |\n| Reproducibility | 4 | 4 | 4 |\n\n**核心判断**：这是一篇实验设计严谨、分析有深度的 empirical study。C1 target-swap ablation 和 signal type/coupling scope decomposition 是有价值的分析贡献，5 种 loss 的 controlled comparison 在同类工作中罕见。\n\n**阻碍 Conference 的三个核心问题**：\n1. **Coupling decomposition 在 50% 失效且有 allocation confound**——论文的主要分析贡献之一的 generality 受限\n2. **Knowledge regression 仅假设无验证**——论文最大负面结果（跨规模 MMLU/GSM8K 退化）缺乏任何机制分析实验\n3. **方法组件层面新颖性有限**——KL+Gumbel 应用于新场景，但论文已通过 empirical study 定位和 C1/decomposition 分析贡献部分弥补\n\n**如何提升至 Conference (4.0)**：\n- 修复 C1（限定 decomposition scope + 讨论 allocation confound）和 C2（至少一个控制实验验证 regression 假设）可能足以跨过 borderline\n- C3（novelty framing）通过 contribution list 重排和更早承认组件非新颖性可以改善\n\n**Findings (3.0) 下限条件**：若 C1 和 C2 不修复，论文仍有足够的实验质量和 C1 ablation insight 支撑 Findings 级别接收。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 9 句 abstract 信息密度偏高。可考虑将 C1 和 decomposition 细节移至正文，压缩至 6-7 句。\n- \"Signal type accounts for the majority\" 需加 \"at 30% sparsity\" 限定。\n\n### Introduction (§1)\n- 逻辑流清晰（problem → gap → approach → results），但 contribution list 排序可优化：C1 ablation 和 decomposition 应置于首位。\n- \"reducing TEAL's perplexity by 19%\" → 18.6% 或 ~19%。\n- MaskLLM 区分（¶7）位置合理，但组件非新颖性应更早承认。\n\n### Related Work (§2)\n- 覆盖全面（50+ 引用），结构合理。MaskLLM 三点区分有说服力。\n- 无重大遗漏。\n\n### Method (§3)\n- KL 公式正确，Gumbel-Sigmoid 推导标准。\n- Geometric Penalty Schedule 是合理的替代 Lagrangian multiplier 的方案。\n- §3.6 梯度分析：BCE vs KL 对比公正，\"suggestive; empirical evidence in §4.3\" 的 hedging 恰当。\n- Eq. 4 缺少层标 ℓ。\n- T vs τ 可加一句区分说明。\n\n### Experiments (§4)\n- §4.1 Main results：PPL 结论可靠（σ=0.02），downstream 差异为 directional evidence（论文已注明）。\n- §4.3 C1 ablation：设计巧妙，s123/s456 matched oracle 结果 convincing。s42 provenance 问题需修复。\n- §4.5 Per-layer KL decomposition：30% 分析有价值，50% 失效需明确标注。Allocation confound 需在正文讨论。\n- §4.6 Cross-arch：PPL 泛化 convincing，downstream regression 需更完整统计报告。\n\n### Conclusion (§5)\n- 简洁完整。\"primary design dimension\" 需限定适用范围。\n\n### Limitations\n- 覆盖 5 个要点（sparsity sweet spot, knowledge regression, training data, batched inference/seq length, generation tasks），充分。\n- 建议补充 14B regression 加剧对 70B+ 的影响讨论。\n\n### Formatting\n- 正文 8 页，符合 ACL 8 页限制 ✓\n- Double-blind：未见 de-anonymizing 信息 ✓\n- ACL 模板 (acl.sty, [review] option) ✓\n- References 格式统一 ✓\n- 代码释放声明：Conclusion 末尾 \"Code and trained predictors will be released upon acceptance\" ✓"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "report": "# Round 25 审稿报告（Fresh Review）\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**目标 Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）\n**轮次**: 1 轮（交叉分享后关键问题达成共识，无需第 2 轮）\n\n---\n\n## Summary\n\n本文提出用前向 KL 散度替代 BCE 训练 SwiGLU LLM 的轻量级稀疏性预测器（<1% base 参数）。核心 insight 是 KL 将所有 mask 决策通过输出分布耦合，发现的 mask patterns 与 magnitude-based 方法分歧 46-68%，但产生显著更优的 PPL（LLaMA-3.1-8B 30% sparsity 下减少 14.5%）。C1 target-swap ablation 将 KL 优势解耦为 signal type（output-distribution vs intermediate loss）和 coupling scope，发现 signal type 在 30% 下主导 PPL 差距（upper bound）。跨架构评估（Mistral-7B, Qwen-14B）确认 PPL 泛化但知识密集型任务系统性退化。论文自定位为 empirical study；无 wall-clock speedup（+6.4% overhead）。\n\n---\n\n## Strengths\n\n**S1** [两位 reviewer 共识] **C1 target-swap ablation 设计巧妙**：将 KL 发现的 mask targets 转移给 BCE 训练，干净地分离了 \"what\"（mask pattern quality）和 \"how\"（gradient coupling mechanism）的贡献。max Δ≤0.79pp（50% s42）证明 KL 发现的 mask 模式是质量优势的主要来源。这是论文最有洞察力的实验。\n\n**S2** [两位 reviewer 共识] **实验控制质量高**：KL / BCE / MSE 使用完全相同的 architecture（2-layer MLP, d_b=128）、data（WikiText-103）、optimizer（AdamW）、steps（1000），仅改变 loss function。3-seed 评估用于主要结果，PPL 标准差极低（±0.02）。这种 controlled comparison 在 empirical ML 论文中并不常见。\n\n**S3** [两位 reviewer 共识] **诚实且全面的 limitations 披露**：明确承认无 wall-clock speedup、knowledge-task regression、training data homogeneity、evaluation bounds。Abstract 使用更保守的 14.5%（matched sparsity）而非 18.6%（nominal）。Claims 有适当 hedging（\"upper bound\"、\"suggests\"、\"primarily empirical\"）。\n\n**S4** **丰富的 appendix**（~18 个 display items）：从 bottleneck sensitivity 到 temperature schedule 到 training convergence 到 cross-seed mask consistency 到 OOD evaluation，覆盖了大部分可预见的 reviewer 问题。\n\n**S5** **Compensation redundancy finding**：发现 KL predictor 使得额外的 67.2M 参数补偿网络冗余，简化推理管线——实用且有信息量。\n\n**S6** **2D taxonomy**（Table 1）提供了有用的组织框架：correction granularity × training signal coupling，帮助定位论文贡献和 prior work。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1** [critical, 两位 reviewer 共识] **Coupling decomposition 在 50% sparsity 下失效且存在 allocation confound**\n\n- **K=4 at 50% 反常**：K=4 per-layer KL PPL=44.23 **劣于** K=1 的 34.85，而 E2E KL 为 11.84。如果增加 masked layers（K=1→K=4）应缩小与 E2E 差距，但实际差距从 +23.06 扩大到 +32.44。论文的 \"gradient interference\" 解释（§4.5）是 speculation，无实验证据。\n- **MMLU allocation confound**：K=4 在 MMLU 上系统性超过 E2E（42.7±1.4 vs 40.7±1.3，3 个 seed 均是），因为 K=4 产生 near-uniform allocation（std=0.003）匹配了 uniform inference protocol，而 E2E 产生非均匀分配（L14-L18 valley）。因此 decomposition 的两个维度不正交，无法独立归因 coupling vs allocation 效应。\n- **General claims 超出 evidence 范围**：Abstract（\"Signal type accounts for the majority of the PPL gap\"）和 Conclusion 基于 30% 结果做 general claim，但 decomposition 在 50% 下不成立。\n- **建议**：(1) Abstract/Conclusion 限定为 \"at moderate sparsity (30%)\"；(2) 正文 §4.5 显著讨论 allocation confound；(3) 补充 K=2/K=8 实验追踪趋势，或明确放弃 50% 下的 decomposition 分析。\n\n**C2** [critical, 两位 reviewer 共识] **知识密集型任务系统性退化仅有假设无控制实验**\n\n- 跨所有规模一致退化：8B MMLU -5.2pp，Mistral GSM8K -7.3pp，Qwen-14B GSM8K -20pp, MMLU -8.1pp。\n- §4.2 提出两个假设（WikiText-103 数据偏差 + forward KL mode-covering 稀释 rare activations），但明确说 \"await validation via knowledge-neuron probing\"——没有做任何验证实验。\n- Appendix T 的 constraint analysis 已显示 remove-valley → MMLU +3.4pp, GSM8K +1.6pp，暗示 regression 部分源于 learned allocation 而非 loss function 本身，但此关键发现仅在 appendix 中。\n- **建议**：(1) 至少一个控制实验：C4/RedPajama 训练 predictor 测试数据偏差假设，或比较 KL vs magnitude 在 knowledge-critical layers 的 neuron retention 差异；(2) Appendix T 发现提升到正文。\n\n**C3** [warning→critical by consensus] **方法新颖性边界需更清晰论证**\n\n- 核心组件（KL distillation + Gumbel-Sigmoid + predictor arch）均为成熟技术。MaskLLM 已用 KL + Gumbel-Softmax 训练可学习 mask。论文的三点区分合理但更多来自应用场景不同。\n- **R1 nuance**：contextual vs static 确为不同优化问题（predictor 需泛化到未见输入），且论文已自定位为 \"primarily an empirical study\"。C1 ablation 和 per-layer decomposition 的**实验设计**本身有新颖性。\n- **共识建议**：(1) Introduction 更早承认组件层面非新颖性；(2) Contribution list 重排：C1 ablation + decomposition 置于首位（当前第一条是 \"ranking across five losses\"，信息量不如 C1 + decomposition）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [两位 reviewer 共识] **C1 ablation s42 oracle provenance 问题**：s42 oracle 来自 earlier checkpoint（PPL gap 0.65pp at 30%），而 s123/s456 matched oracle gap ≤0.03pp。s42 是 Table 3 第一行且唯一有 50% 数据的 seed。建议为 s42 补训 matched oracle，或优先展示 s123/s456，并补充 s123/s456 在 50% 的 C1 结果。\n\n**W2** [两位 reviewer 共识] **BCE 30% 缺少 uniform allocation 对比**：Table 2 中 BCE 30% 仅有 global（†），KL 有 global+uniform。无法在相同 allocation strategy 下直接比较。建议补充 BCE 30% uniform 或解释缺失原因。\n\n**W3** [两位 reviewer 共识] **MSE 50% single-seed caveat 不充分**：seed 123 catastrophic failure（PPL=15,789），Table 4 的 229.26 仅 seed 42。正文 §3.7 使用 MSE 50% 数据论证 taxonomy 但未注明 single-seed。MSE 30% 3-seed（18.52±1.68）结论稳健。建议正文标注 caveat。\n\n**W4** [两位 reviewer 共识] **无 wall-clock speedup，+6.4% latency overhead**：论文诚实披露（appreciated），但对 sparsity 领域论文实用影响受限。论文 framing 已充分（\"primarily an empirical study\"），结构性限制。\n\n**W5** **Qwen-14B GSM8K 高方差**：uniform 3-seed 32.0±5.2（CV=16.3%），95% CI 约 ±10pp。建议正文引用完整 32.0±5.2 vs 52.1 而非仅 \"-20pp\"。\n\n**W6** **Limitations 未讨论 14B regression 对更大规模的影响**：8B→14B regression 加剧（GSM8K -1.3pp→-20pp），但 Limitations 未讨论 70B+ 前景。\n\n### Minor Issues\n\n**M1** §4.1/Introduction \"19%\" 实际为 18.6%（(10.82-8.81)/10.82=18.58%）。Figure 2 caption 使用 14.5%（matched sparsity）而 §4.1 使用 19%（nominal），基准不一致。\n\n**M2** 术语不一致：\"output-distribution alignment\"/\"distillation\"/\"objective\" 交替使用，建议统一。\n\n**M3** Eq. 4 s_j 和 m̃_j 缺少层标 ℓ 上标，与 §3.1 notation 不一致。\n\n**M4** §3.4 T（distillation temperature）与 §3.3 τ（Gumbel temperature）使用不同符号但未明确区分，可能造成困惑。\n\n**M5** Table 4 STE 30% 仅达 20.8% actual sparsity（‡），与其他方法在不同实际 sparsity 下对比，公平性有限。\n\n---\n\n## Reviewer Consensus\n\n两位 reviewer 评分一致（Overall 3.5, Soundness 3.5, Excitement 3, Confidence 4），在以下核心评估上达成共识：\n\n| 问题 | 共识状态 |\n|------|----------|\n| C1: Coupling decomposition 在 50% 失效 + allocation confound | [AGREE] 两位均列为 Critical |\n| C2: Knowledge regression 缺机制分析 | [AGREE] R1 W1 + R2 N1，两位均认为最高优先级 |\n| C3: 方法新颖性边界 | [AGREE with nuance] R2 Critical, R1 部分同意但指出实验设计新颖性 |\n| W1: C1 s42 oracle provenance | [AGREE] 两位均指出 |\n| W2: BCE 30% 缺 uniform | [AGREE] 两位均指出 |\n| W4: 无 wall-clock speedup | [AGREE] 结构性限制，framing 已充分 |\n| S1-S3: C1 ablation 巧妙 + 实验控制 + 诚实 limitations | [AGREE] 两位共同认可的主要优势 |\n\n---\n\n## Reviewer Divergence\n\n| 分歧点 | R1 立场 | R2 立场 | 解决 |\n|--------|---------|---------|------|\n| 缺少 MT-Bench/AlpacaEval | [REBUT] Base model 不适用 instruction-following benchmarks | [Should-Fix] 缺少生成评估 | **R1 rebuttal 有效**：论文评估 base model，MT-Bench 需 instruction-tuned。Limitations 已覆盖。不计入最终 weakness |\n| Conclusion 过于简洁 | [REBUT] 简洁但完整，ARR 无格式要求 | Minor issue | **R1 rebuttal 有效**：Conclusion 覆盖了核心发现、key result、limitations、code release |\n| GPU 型号 double-blind 风险 | [REBUT] 商用 GPU，不构成 de-anonymization | Minor concern | **R1 rebuttal 有效**：RTX PRO 6000 是 2025 年商用 GPU，不比 A100 更具识别性 |\n| Qwen-14B 单 seed vs 多 seed | [Critical] 单 seed 不足 | [Partial REBUT] 实为 3-seed 但高方差 | **R2 factual correction 有效**：GSM8K uniform 是 3-seed (32.0±5.2)，非单 seed。降级为 Warning（高方差限制统计力）|\n| Sparsity controller 30% 饱和 | [Should-Fix] λ=5000 cap, 28.5% | [Partial REBUT] Appendix C matched-sparsity 对比充分 | **R2 rebut 部分有效**：matched comparison 已提供，但建议在正文中讨论 deviation |\n\n---\n\n## Questions\n\n1. K=4 at 50% 为什么比 K=1 差？是否有 K=2/K=8 数据追踪 PPL vs K 趋势？\n2. 如果在 K=4 实验中强制使用 E2E KL 的 per-layer allocation（而非 K=4 自然学出的 near-uniform），MMLU anomaly 是否消失？\n3. 是否尝试过在 math-heavy 数据（如 GSM8K 训练集或 math subset of C4）上训练 predictor 来检验 knowledge regression 是否源于数据偏差？\n4. BCE 30% 为什么缺少 uniform allocation 数据？是否存在 BCE uniform 表现更差的情况？\n5. Appendix T 的 remove-valley 实验中，是否存在同时改善 MMLU 和 ARC-c 的 per-layer allocation 配置？\n\n---\n\n## Missing References\n\n论文 Related Work 覆盖面相当完善（50+ 引用），两位 reviewer 未发现重大遗漏。建议检查：\n- 2026 年 1-5 月是否有新的 KL distillation for activation sparsity 工作\n- TurboSparse 系列后续工作的更新引用\n\nMissing references 不构成接收障碍。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（耗时 4 分 20 秒）\n\n**统计**：0 critical, 3 warning, 17 info\n\n**Warnings**:\n1. **Page 3-4 连续 2 页无 figure/table**：Related Work → Method 过渡，可考虑将 Table 1 前移至 p4\n2. **Page 13（附录）极高密度**：Table 7 + 8 + 9 + Figure 3 + Table 10 + 3 subsections 挤入单页，阅读体验欠佳\n3. **Page 17（附录）底部拥挤**：Table 15 + Figure 7 + Table 16-17 密集堆叠\n\n**Info highlights**:\n- 主体正文恰好 8 页，符合 ACL 要求\n- 全文 6 个 display items（2 Figure + 4 Table），密度 0.75/页，适中\n- 未见 margin overflow、公式渲染错误、[?] 未解析引用\n- References 格式统一（ACL natbib），无异常\n- Figure 1 在 p2（可提升到 p1 底部以增强首页视觉锚定）\n\n---\n\n## Overall Assessment\n\n**评分：3.5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3 | 3 | 3 |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4 | 4 | 4 |\n| Reproducibility | 4 | 4 | 4 |\n\n**核心判断**：这是一篇实验设计严谨、分析有深度的 empirical study。C1 target-swap ablation 和 signal type/coupling scope decomposition 是有价值的分析贡献，5 种 loss 的 controlled comparison 在同类工作中罕见。\n\n**阻碍 Conference 的三个核心问题**：\n1. **Coupling decomposition 在 50% 失效且有 allocation confound**——论文的主要分析贡献之一的 generality 受限\n2. **Knowledge regression 仅假设无验证**——论文最大负面结果（跨规模 MMLU/GSM8K 退化）缺乏任何机制分析实验\n3. **方法组件层面新颖性有限**——KL+Gumbel 应用于新场景，但论文已通过 empirical study 定位和 C1/decomposition 分析贡献部分弥补\n\n**如何提升至 Conference (4.0)**：\n- 修复 C1（限定 decomposition scope + 讨论 allocation confound）和 C2（至少一个控制实验验证 regression 假设）可能足以跨过 borderline\n- C3（novelty framing）通过 contribution list 重排和更早承认组件非新颖性可以改善\n\n**Findings (3.0) 下限条件**：若 C1 和 C2 不修复，论文仍有足够的实验质量和 C1 ablation insight 支撑 Findings 级别接收。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 9 句 abstract 信息密度偏高。可考虑将 C1 和 decomposition 细节移至正文，压缩至 6-7 句。\n- \"Signal type accounts for the majority\" 需加 \"at 30% sparsity\" 限定。\n\n### Introduction (§1)\n- 逻辑流清晰（problem → gap → approach → results），但 contribution list 排序可优化：C1 ablation 和 decomposition 应置于首位。\n- \"reducing TEAL's perplexity by 19%\" → 18.6% 或 ~19%。\n- MaskLLM 区分（¶7）位置合理，但组件非新颖性应更早承认。\n\n### Related Work (§2)\n- 覆盖全面（50+ 引用），结构合理。MaskLLM 三点区分有说服力。\n- 无重大遗漏。\n\n### Method (§3)\n- KL 公式正确，Gumbel-Sigmoid 推导标准。\n- Geometric Penalty Schedule 是合理的替代 Lagrangian multiplier 的方案。\n- §3.6 梯度分析：BCE vs KL 对比公正，\"suggestive; empirical evidence in §4.3\" 的 hedging 恰当。\n- Eq. 4 缺少层标 ℓ。\n- T vs τ 可加一句区分说明。\n\n### Experiments (§4)\n- §4.1 Main results：PPL 结论可靠（σ=0.02），downstream 差异为 directional evidence（论文已注明）。\n- §4.3 C1 ablation：设计巧妙，s123/s456 matched oracle 结果 convincing。s42 provenance 问题需修复。\n- §4.5 Per-layer KL decomposition：30% 分析有价值，50% 失效需明确标注。Allocation confound 需在正文讨论。\n- §4.6 Cross-arch：PPL 泛化 convincing，downstream regression 需更完整统计报告。\n\n### Conclusion (§5)\n- 简洁完整。\"primary design dimension\" 需限定适用范围。\n\n### Limitations\n- 覆盖 5 个要点（sparsity sweet spot, knowledge regression, training data, batched inference/seq length, generation tasks），充分。\n- 建议补充 14B regression 加剧对 70B+ 的影响讨论。\n\n### Formatting\n- 正文 8 页，符合 ACL 8 页限制 ✓\n- Double-blind：未见 de-anonymizing 信息 ✓\n- ACL 模板 (acl.sty, [review] option) ✓\n- References 格式统一 ✓\n- 代码释放声明：Conclusion 末尾 \"Code and trained predictors will be released upon acceptance\" ✓"
  }
}
```

</details>

---


### Tool result

_source line 2031 · 2026-05-23T00:51:50.602199+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3817
}
```

</details>

---


### Assistant

_source line 2032 · 2026-05-23T00:52:03.043431+00:00_

Round 25 审稿完成。

**结果汇总**：
- **Overall 3.5（Borderline Conference）**，两位 Reviewer 评分完全一致
- **3 个 Must-Fix**：(1) Coupling decomposition 在 50% 失效 + allocation confound；(2) Knowledge regression 仅假设无控制实验；(3) 方法组件层面新颖性需更清晰 framing
- **6 个 Should-Fix**：C1 s42 oracle provenance、BCE 30% 缺 uniform 对比、MSE 50% single-seed caveat、无 wall-clock speedup、Qwen-14B 高方差报告、Limitations 补 14B→70B 讨论
- **5 个 Minor**：19%→18.6%、术语不一致、Eq.4 层标缺失、T/τ 区分、STE 30% 公平性
- **视觉审查**：已完成，0 critical / 3 warning / 17 info，排版整体合规

报告已投递至 Research Director。Issue tracker 已同步更新（新增 7 个 issue，更新 8 个现有 issue）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 175

## Round 175

2 recorded events


### User

_source line 2033 · 2026-05-23T00:52:05.607731+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。

核心共识：knowledge-task regression 缺乏机制分析、coupling decomposition 在 50% sparsity 下失效是两个最关键的共同关注点。在 MT-Bench（base model 不适用）、Conclusion 长度、GPU double-blind 三点上持反对意见。维持 Overall 3.5 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2034 · 2026-05-23T00:52:18.105514+00:00_

Round 25 审稿已完成。

**最终结果：3.5（Borderline Conference）**，两位 Reviewer 评分一致。

**核心共识**：
- **3 个 Must-Fix**：(1) Coupling decomposition 在 50% 失效 + allocation confound；(2) Knowledge regression 无控制实验验证假设；(3) 方法组件新颖性需更清晰定位
- **6 个 Should-Fix**：C1 s42 oracle provenance、BCE 30% 缺 uniform 对比、MSE 50% single-seed、无 wall-clock speedup、Qwen-14B 高方差、Limitations 缺 70B+ 讨论
- **3 个分歧已解决**：MT-Bench（R1 rebuttal 有效——base model）、Conclusion 长度（简洁但完整）、GPU double-blind（商用 GPU）

审稿报告和 Issue Tracker 均已提交。视觉审查已完成（0 critical, 3 warning），外部审稿未启用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 176

## Round 176

52 recorded events


### User

_source line 2035 · 2026-05-23T01:26:11.177930+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2036 · 2026-05-23T01:26:17.365679+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2037 · 2026-05-23T01:26:17.416819+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2038 · 2026-05-23T01:26:25.034162+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2039 · 2026-05-23T01:26:25.034564+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2040 · 2026-05-23T01:26:27.502992+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2041 · 2026-05-23T01:26:27.553572+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2042 · 2026-05-23T01:26:33.829773+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2043 · 2026-05-23T01:26:35.234608+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (379 个)\n\n- **eval_spon_supp_retry**: DONE (failed) — \n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-23T01:05:43Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 378 个实验 — DEPLOYED 1, DONE 377\n**DONE 分布**: failed 35, killed 82, negative 24, success 236\n\n### 💾 磁盘余量\n- **westd-34887**:\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/usr/bin/nvidia-smi`: 817G/879G 可用（已用 3%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `c4_kl30_s42` [failed] — 2026-05-23T01:05:38 — CUDA OOM: CUDA out of memory. Tried to allocate 224.00 MiB. GPU 0 has a total ca\n- `spon_2048_s42` [killed] — 2026-05-23T00:11:36 — 启动后崩溃，日志仅9行，停在 Setting up data loader... 待诊断\n- `bce_isocompute_v2_s42` [killed] — 2026-05-23T00:11:35\n- `kl_sparsity70_s42_v2` [killed] — 2026-05-23T00:11:33\n- `jsd_50pct_s42` [killed] — 2026-05-23T00:11:32\n\n### 🔴 最近失败原因 (top 3)\n- `c4_kl30_s42`: CUDA OOM: CUDA out of memory. Tried to allocate 224.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 188.56 MiB is free. Process 94893 has 65.98 GiB memory in use. Including non-PyTorch memory\n- `spon_2048_s42`: 启动后崩溃，日志仅9行，停在 Setting up data loader... 待诊断\n- `bce_isocompute_v2_s42`: _(no failure_reason — pre-2026-04-24 entry)_\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Hando
…[truncated 1810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1404
}
```

</details>

---


### Tool call

_source line 2044 · 2026-05-23T01:26:35.385696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2045 · 2026-05-23T01:26:35.887967+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	\input{limitations}
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2046 · 2026-05-23T01:26:35.938721+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 2047 · 2026-05-23T01:26:44.521978+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"The 14th Joint Conference on Lexical and Computational Semantics | ACL Member Portal","url":"https://www.aclweb.org/portal/content/14th-joint-conference-lexical-and-computational-semantics"},{"title":"ACL Policy on Publication Ethics - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policy_on_Publication_Ethics"},{"title":"EACL 2026 - Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-call-system-demonstrations"}]

I found several results related to ACL Rolling Review (ARR) and 2026 conferences. Here are the key findings:

## ACL Rolling Review (ARR) 2026 Overview

ACL Rolling Review (ARR) invites the submission of long and short papers on substantial, original, and unpublished research in all aspects of Computational Linguistics and Natural Language Processing.

## Submission Guidelines and Author Instructions

**Style and Format:**
Paper submissions must use the official ACL style templates, which are available as an Overleaf template and can be downloaded directly via https://aclrollingreview.org/cfp under 'Paper Submission Process, Cri
…[truncated 890 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 8583
}
```

</details>

---
