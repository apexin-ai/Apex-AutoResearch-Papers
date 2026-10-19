# Director coordination — Part 3 of 8

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/e0/e0d2e26e51128e828a96.json)

## Round 50

### Assistant

_source line 714 · 2026-05-18T14:12:01.131609+00:00_

Round 1 任务已分配给两位 Reviewer。等待审稿意见返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 51

## Round 51

4 recorded events


### User

_source line 715 · 2026-05-18T14:17:46.621356+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 — Round 1 审稿意见

**论文**: "Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"
**Venue**: EMNLP 2026 (ACL Rolling Review May 2026 cycle)

---

## 总体评分
**Overall**: 3.0 / 5 — Findings
**一句话总结**: 观察到 KL 蒸馏优于 BCE 用于稀疏性预测是有价值的实证贡献，但核心因果 claim 存在未解的混淆变量（oracle target quality vs. gradient coupling），14B 结果与主叙事矛盾，且无实际推理加速演示。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | 梯度分析结构正确，但 BCE vs KL 对比存在已知混淆变量（论文自身承认），regime 分析每个 regime 仅 1 个数据点 |
| Excitement | 3 / 5 | KL > BCE 的观察有用且可能启发后续工作，但无实际加速且 14B 结果限制了 claim 的普适性 |
| Reproducibility | 4 / 5 | 超参数报告完整，硬件明确，关键结果有 multi-seed；但 SNR 计算细节缺失 |
| Confidence | 4 / 5 | 熟悉稀疏性预测和蒸馏文献，仔细阅读了全文 |

---

## Summary

本文研究用 forward KL 蒸馏替代 per-neuron BCE 训练 SwiGLU LLM 的稀疏性预测器。核心观察是：BCE 的梯度对每个 neuron 独立，而 KL 的梯度通过下游层的 Jacobian 耦合所有 neuron，更适合 TEAL 的 global top-k 推理分配。在 LLaMA-3.1-8B 上，KL 预测器（75.9M 参数）在 30% 和 50% 稀疏度下均优于 TEAL，并使补偿网络（+67.2M 参数）成为冗余。跨架构验证覆盖 Mistral-7B 和 Qwen-2.5-14B。论文还分析了三个"operating regions"并报告了 allocation-dependent 行为。

---

## 主要优势

1. **梯度分析清晰且有启发性**（§3.6）：BCE gradient $\partial \mathcal{L}/\partial s_j = \sigma(s_j) - m_j^*$ 仅依赖 neuron $j$，而 KL gradient 通过 Jacobian factor (b) 耦合所有 neuron。这是一个简洁有力的 structural observation，即使论文未能完全证明它是性能差异的唯一来源。

2. **诚实报告负面结果**：14B MMLU gap（63.7% vs 71.8%，Table 7）、无 wall-clock speedup、30% 下 global allocation 的 seed 不稳定性（MMLU σ=9.5pp）——这些对论文叙事不利的结果都被如实报告并讨论，这是值得称赞的。

3. **消融设计较完整**（Table 3）：覆盖 divergence direction（forward/reverse/JSD）、relaxation method（Gumbel vs STE）、loss function isolation（BCE+Gumbel+Penalty）、compensation redundancy。每个消融隔离了一个设计选择。

4. **跨架构验证**（Table 6）：LLaMA-8B、Mistral-7B、Qwen-14B 三个架构的 PPL 优势一致（30%: 1.22-1.24×, 50%: 1.98-2.12×），增强了方法的普适性 claim。

5. **Taxonomy（Table 1）**将 prior work 按 correction granularity × training signal coupling 组织，定位清晰。

6. **写作质量高**：结构紧凑，数学符号一致，表格信息密度高。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心因果 claim 存在未隔离的混淆变量
- 具体位置：§4.3（第 7 页）、Limitations（第 9 页）
- 问题：论文的核心叙事是"梯度耦合（gradient coupling）使 KL 优于 BCE"。但 BCE 使用 magnitude-based oracle masks 作为 target，而 KL 直接优化输出分布——这是两个同时变化的变量（training objective 和 implicit target quality）。论文自身在 §4.3 明确承认："an ablation using KL-derived masks as BCE targets would isolate the effect"，但未执行该消融。
- 现有证据的局限：Oracle F1 分析（BCE 0.613 vs KL 0.540，但 KL PPL 好 139%）说明 per-neuron accuracy 不等于 output preservation，但无法区分这是因为（a）KL 的梯度耦合更好，还是（b）magnitude-based oracle masks 本身就是次优 target。如果 BCE 使用 KL-derived masks（即"正确的" target），表现是否仍差？这是一个可执行的消融。
- 为什么影响接收：这是 contribution 1 和 2 的根基。如果改善主要来自 target quality 而非 gradient coupling，论文的主要叙事（structural mismatch → coupled gradient → better allocation）就需要重新 frame。
- 建议修改方向：执行 KL-derived masks as BCE targets 消融（论文自己提出了这个实验）。即使 KL 仍胜出，结果也会更 conclusive；即使 BCE 缩小差距，也是有价值的发现，可以修改 framing 为"both target quality and coupling matter"。

**N2** [critical] "Three Operating Regions" 分析证据不足
- 具体位置：§4.5（Table 5），第 8 页
- 问题：论文声称存在三个 qualitatively distinct 的 operating regions（budget-surplus ≤30%、budget-constrained ~40%、capacity-limited ≥50%），但每个 regime 只有 **一个数据点**（30%、40%、50%），且 40% 仅单 seed。论文承认"Denser sampling (e.g., 35% sparsity) would be needed to precisely locate region boundaries"，但仍然在正文中强调"三个 regions"作为核心发现之一。
- 具体缺陷：
  - 40% regime：global MMLU 38.06% vs uniform 30.68%（+7.4pp），但这是**单 seed**结果。考虑到 30% global MMLU 的 σ=9.5pp，40% 的 7.4pp 差异可能在 seed variance 之内。
  - 边界不确定：30% 和 40% 之间的行为（35%? 37%?）完全未知，40% 和 50% 之间同理。
  - 30% 的 regime 标签"budget-surplus"暗示 30% 是"容易的"，但 30% 的 PPL 已比 dense 恶化 47%（8.96/6.12），downstream 显著退化。
- 为什么影响接收：这是 contribution 3 的主体。以 3 个点声称"三个 qualitative phases"在统计上不严格。
- 建议修改方向：（1）在 25%、35%、45% 补充至少 2-seed 实验以确认 regime boundaries；或（2）将 framing 弱化为"preliminary observations suggesting allocation-dependent behavior"而非 distinct operating regions。

**N3** [critical] 14B 结果与核心 claim 显著矛盾，解释不充分
- 具体位置：§4.6（Table 7），第 8 页
- 问题：在 Qwen-2.5-14B 30% 稀疏度下，KL PPL 最优（7.62 vs TEAL 8.73），但 MMLU 低 8.1pp（63.72% vs 71.83%），GSM8K 低 4.3pp（48.82% vs 53.07%），ARC-c 也略低。在 uniform allocation 下，MMLU 差距仍存在（64.49 vs 66.34）。论文的核心 claim 是"output-distribution preservation is better than per-neuron classification"，但 14B 的 downstream 结果表明，PPL 优化不等于 task 保持，且在更大模型上 BCE/TEAL 的 downstream 表现反而更好。
- 论文的解释（"Higher knowledge density at 14B may cause KL's output-preservation objective to sacrifice task-specific pathways"）是推测性的，没有实证支撑。
- 为什么影响接收：如果方法在 scale up 到 14B 时核心优势反转（PPL 好但 downstream 差），那么"output-distribution distillation is better"的 claim 的 generalization scope 需要严格限定。
- 建议修改方向：（1）在 14B 上测试更多稀疏度（40%, 50%）以确认是否 consistent；（2）分析 14B per-layer retention patterns 与 8B 的差异；（3）修改 claim scope 为明确限定在 7-8B。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] `\enlargethispage{10\baselineskip}` 格式操纵
- 具体位置：experiments.tex 第 253 行
- 问题：使用 `\enlargethispage{10\baselineskip}` 人为扩展第 8 页以容纳更多内容。从 PDF 第 8 页可看到，该页内容密度明显高于其他页（包含 Table 5、Table 6、Table 7、三个 operating regions 分析、SPON 分析、cross-architecture validation、14B 结果、inference efficiency、完整 conclusion）。
- 为什么重要：ACL 模板明确规定不得修改 margin 和 page layout。虽然技术上不算 desk reject，但审稿人和 AC 经常注意到这类操纵。
- 建议：将部分实验内容（如 SPON 详细分析）移至 appendix。

**W2** [warning] BCE baseline 比较不完全公平
- 具体位置：§4.2-4.3（Table 2, Table 3）
- 问题：
  - BCE 在 30% 稀疏度下的结果**未在 Table 2 中报告**。既然 30% 是 recommended operating point，这是一个关键缺失。仅在 50% 展示 BCE（PPL 28.13）放大了 KL 的优势。
  - BCE 和 KL 的 target 不同（magnitude oracle vs output distribution），这不仅是 loss function 的差异，还是 supervision signal 的差异（与 N1 相关但这里聚焦 fairness）。
  - Isolation ablation（BCE+Gumbel+Penalty = 38.02）比 vanilla BCE（27.97）更差，说明 Gumbel+Penalty 框架与 BCE 不兼容，而非 BCE 在该框架下效果不好。
- 建议：（1）补充 BCE 30% 结果；（2）测试 BCE with output-based targets 或 BCE without TEAL allocation（用 BCE 自身的 per-layer top-k）。

**W3** [warning] 训练/评估数据同族问题
- 具体位置：§4.1、Appendix D
- 问题：训练用 WikiText-103，主要评估用 WikiText-2（同一 WikiText 语料族）。C4 OOD 结果（Appendix D）在 30% 时 PPL 退化为 1.74× dense（vs WikiText-2 的 1.47×），退化更严重。C4 30% 仅 2-seed（vs 主结果 3-seed），且无 C4 downstream 评估。
- 建议：（1）C4 补充到 3-seed 以匹配主结果的 rigor；（2）报告 C4 上的 downstream benchmarks 或解释为什么 WikiText-2 的 downstream 结果可以 generalize。

**W4** [warning] SNR 分析覆盖不足
- 具体位置：§3.6（第 5 页），Appendix F
- 问题：
  - SNR 仅测量到 step 300，但训练跑 1000 步。Step 300-1000 的 SNR 演化未知。
  - "5.14× higher SNR at convergence (step 300)" ——但 step 300 不是真正的 convergence（Appendix B.2 显示 training converges by step 800）。
  - SNR 计算的 mini-batch 数量未报告，bootstrap CI 的样本量未报告。
  - 因果 claim（"KL's gradient coupling becoming effective only after the predictor learns a coarse mask structure"）是 post-hoc 解释，未经验证。
- 建议：（1）将 SNR 测量延伸到 1000 步；（2）报告 mini-batch 数量和 bootstrap 参数；（3）弱化因果 claim 为 correlation observation。

**W5** [warning] Adaptive penalty controller 在 30% 处不收敛
- 具体位置：Appendix C（Table 12），第 12 页
- 问题：在 recommended 30% operating point，$\lambda$ 达到 cap（5000），actual sparsity 28.5%（deviation 5.0%）。论文辩称 TEAL 在 28.5% 的 PPL ≈ 10.7 vs 30% 的 10.97，差异可忽略。但这意味着 KL predictor 实际运行在比标称更低的稀疏度上，给 KL 带来了不公平的 ~1.5% sparsity 优势。Table 2 报告"30% sparsity"但实际是 28.5%。
- 建议：（1）在 Table 2 的 caption 或正文中明确注明 actual sparsity；（2）与 TEAL at 28.5% 做 fair comparison。

**W6** [warning] 无实际推理加速
- 具体位置：Appendix A（Table 8），第 11-12 页
- 问题：Pipeline 增加 6.4% overhead（126.78 vs 119.11 ms/fwd）。在 30% recommended sparsity 下，预测器增加 6.3% latency 但未从稀疏性获得任何 speedup（unstructured masks 无法被硬件加速）。论文的 motivation 是推理效率，但实际贡献是 prediction quality 而非 efficiency。
- 建议：论文诚实地在 Limitations 中讨论了这一点，但建议在 Introduction 中更早 set expectations，避免读者产生效率提升的预期。

---

## 小问题（不影响接收）

1. Figure 1（method overview）出现在第 6 页（实验部分之后才开始的位置），位置偏晚。建议移到 Method section 正文中更早的位置。
2. "renders post-hoc compensation redundant" claim 仅测试了一种 compensation 架构（FastForward-style）。措辞可改为"renders FastForward-style compensation redundant"。
3. Abstract 中 "7-14B" 范围暗示 PPL 优势跨 scale 一致，但 14B downstream 结果与此暗示矛盾。
4. Table 2 caption 注脚说明"50% uniform PPL is 3-seed (11.92 ± 0.07; Appendix E)"，但正文 Table 2 中 50% KL uniform 显示为 11.96，不一致。
5. Downstream benchmark 选择标准未解释——为什么 ARC-c, WG, MMLU, GSM8K 在主表而 HellaSwag, PIQA, BoolQ 在 appendix？
6. Appendix 引用完整性：正文提到 Appendix H (app:downstream) 但编号可能需要检查（appendix 使用字母编号 A-F）。

---

## Missing References

引用验证结果：39 条 bib entries 全部被引用，无 orphan/missing。OpenAlex 验证 35 条通过，4 条 minor mismatch（author name formatting）。

建议补充考虑的参考文献：
- **Griffin (De Vries et al., 2024)** 或其他 gated linear unit variant 的稀疏性工作
- **Mixture-of-Experts 稀疏性与 activation sparsity 的交叉文献**（如 Expert Choice routing）——Table 1 taxonomy 可能遗漏了 MoE-based 方法作为"coupled + per-token"的另一个 cell

---

## Detailed Comments

### 技术正确性

1. **梯度分析（§3.6）数学正确**：BCE gradient 分解（Eq. 9-10）和 KL gradient chain rule（Eq. 11）的结构分析是正确的。Factor (b) $\partial \mathbf{z}/\partial \mathbf{h}^{(\ell)}$ 确实通过下游层耦合所有 neuron。

2. **Gumbel-Sigmoid relaxation（§3.3）使用合理**：温度退火 1.0→0.1 是标准做法（Jang et al. 2017; Maddison et al. 2017）。STE 对比（PPL 15.77 vs 11.79）有效展示了 smooth relaxation 的价值。但温度 schedule sensitivity（Appendix B.1）显示 fixed τ=0.5 实际上略好于 default schedule（PPL 11.861 vs 11.963），这与正文描述的 annealing 动机（"从 exploration 到 exploitation"）矛盾。

3. **Adaptive penalty controller（§3.5）收敛保证**：论文明确在 footnote 中说明这不是 formal dual method，不保证 KKT satisfaction。这是诚实的。但 30% 处 5% deviation（28.5% actual）不可忽略——在 PPL scale 上 1.5% sparsity 差异约 0.3 PPL，而 KL vs TEAL 差异为 2.0 PPL，所以影响有限但应注明。

### 实验设计

4. **Iso-compute 对比（§4.3）基本公平**：BCE 2700 步 ≈ 46min vs KL 1000 步 ≈ 45min。Wall-clock 时间匹配合理（KL 需要 dense forward pass + sparse forward pass per step，计算量更大）。但 BCE 2700 步是否收敛？论文说 PPL 28.13±0.20，没有报告 training loss curve 是否已 plateau。如果 BCE training loss 仍在下降，更多步数可能进一步缩小差距。

5. **Oracle F1 分析（§4.3）论证基本 sound**：F1 高但 PPL 差确实说明 per-neuron accuracy 是 misaligned proxy。但 confound 是：BCE 的 oracle masks 来自 magnitude ranking（TEAL's protocol），而不是"最优 output-preserving masks"——所以 BCE 的低 PPL 可能部分来自 target 质量差而非 gradient 不耦合。

6. **OOD 评估覆盖**：C4 evaluation 仅覆盖 30%/50%（Appendix D），无 70%。30% 为 2-seed，50% 为 single seed。考虑到 C4 退化更严重（1.74× vs 1.47×），更多的 OOD 评估会增强说服力。

---

## 格式合规

- [✓] `\usepackage[review]{acl}` — 双盲 review 模式
- [✓] Anonymous 作者
- [⚠️] `\enlargethispage{10\baselineskip}` — 格式操纵（W1）
- [✓] Limitations section 存在且实质性
- [✓] Ethics Statement 存在
- [✓] Responsible NLP Research Checklist 逐项填写
- [✓] 页数：正文 8 页（但第 8 页被人为扩展）
- [✓] 行号开启


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

_source line 716 · 2026-05-18T14:18:06.562245+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "等待 Reviewer 2 完成 Round 1 独立审稿",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: distill_sparse_swiglu\n- 论文路径: projects/distill_sparse_swiglu/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 截止日期: 2026-05-25\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "等待 Reviewer 2 完成 Round 1 独立审稿",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: distill_sparse_swiglu\n- 论文路径: projects/distill_sparse_swiglu/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 截止日期: 2026-05-25\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-18T14:18:06.562767+00:00_

Next wakeup scheduled for 14:22:00 (in 233s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 718 · 2026-05-18T14:18:09.064048+00:00_

Reviewer 1 审稿意见已收到。核心发现：

- **Overall: 3.0 (Findings)**
- **3 个 Critical**: N1 coupling vs oracle confound 未隔离、N2 三 regime 仅 3 个数据点、N3 14B MMLU 反转与核心 claim 矛盾
- **6 个 Warning**: 格式操纵（`\enlargethispage`）、BCE baseline 不完全公平、训练/评估同族数据、SNR 覆盖不足、penalty controller 30% 不收敛、无实际推理加速

等待 Reviewer 2 审稿意见返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 52

## Round 52

2 recorded events


### User

_source line 719 · 2026-05-18T14:18:11.607387+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿完成摘要**：

- **Overall: 3.0 (Findings)**
- **3 个 Critical 问题**：(N1) KL vs BCE 的核心因果 claim 存在未隔离的混淆变量——论文自身承认需要"KL-derived masks as BCE targets"消融但未执行；(N2) "三个 operating regions" 每个 regime 仅 1 个数据点，40% 为单 seed；(N3) 14B 的 MMLU 比 TEAL 低 8pp，与核心叙事矛盾
- **6 个 Warning 问题**：格式操纵 (`\enlargethispage`)、BCE 30% 未报告、训练/评估数据同族、SNR 分析覆盖不足、penalty controller 在 30% 不收敛（实际 28.5%）、无实际加速
- **主要优势**：梯度分析清晰、消融完整、负面结果诚实报告、跨架构验证、写作质量高

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

_source line 720 · 2026-05-18T14:18:20.380303+00:00_

Reviewer 1 结果已确认，与之前收到的完整审稿意见一致。继续等待 Reviewer 2。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 53

## Round 53

10 recorded events


### User

_source line 721 · 2026-05-18T14:19:47.288866+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见（侧重：新颖性 + 完整性）

### 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 方法是已有技术（Forward KL + Gumbel-Sigmoid + Lagrangian penalty）的工程组合，贡献主要是实验性的；8B 上结果扎实但 14B 的 MMLU 退化与"输出分布保持"叙事矛盾，且无实际推理加速。

### 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心 claim 在 8B 上有实验支撑，gradient 分析数学正确但非新洞察；14B 结果削弱核心叙事 |
| Excitement | 2.5/5 | 已有组件的组合，作者自述"primarily empirical"；regime 分析有一定洞察价值 |
| Reproducibility | 4/5 | 超参完整，标准模型/数据集，多 seed 评估，但未释放代码 |
| Reviewer Confidence | 4/5 | 对 activation sparsity 和 KL distillation 方向熟悉 |

### Summary

Paper proposes replacing per-neuron BCE with forward KL divergence for training contextual sparsity predictors in SwiGLU LLMs. The key argument: BCE's per-neuron gradient is structurally misaligned with TEAL's global top-k allocation (Eq. 5 vs. Eq. 8), and end-to-end KL coupling resolves this. A lightweight predictor (<1% params) with Gumbel-Sigmoid relaxation achieves 18-49% PPL improvement over TEAL on LLaMA-3.1-8B, renders compensation networks redundant. Cross-architecture validation on Mistral-7B and Qwen-2.5-14B shows PPL advantage generalizes, though 14B exhibits MMLU gap.

### 主要优势

- 实验设计严谨: 3-seed 评估、bootstrap CI、iso-compute 对比（BCE 2700 steps vs KL 1000 steps）、多维度 ablation
- F1-PPL 反向解耦是有说服力的实证发现: BCE 在 oracle F1 上领先 +7pp 却 PPL 差 139%（Table 3），说明 per-neuron accuracy 是错误的代理指标
- 诚实的自我定位: 作者明确承认"Our contribution is primarily empirical"（§2），Limitations 主动指出 coupling vs oracle quality 未完全 disentangle
- Regime 分析有价值: Table 5 的三区域划分和 uniform allocation 降低 cross-seed MMLU σ（9.5pp → 1.3pp）的发现有实用参考

### Must-Fix 问题

**N1** [critical] 方法论新颖性不足以支撑 Main Conference
- 位置：§3 全节 + Table 1
- Forward KL distillation（Hinton 2015）、Gumbel-Sigmoid（Maddison 2017; Louizos 2018）、adaptive penalty 均为成熟技术。MaskLLM（Fang 2024）已将 frozen weights + learnable masks + KL + Gumbel relaxation 用于 LLM sparsity，技术栈高度重叠。§3.5 的 gradient 分析是 end-to-end > decomposed 这一公知原则的直接实例化。Table 1 taxonomy 在自定义坐标系中填充空白 cell 是循环论证式新颖性声明。

**N2** [critical] 14B 结果与核心叙事矛盾
- 位置：Table 7（§4.5）、Abstract L7、Conclusion L3
- Qwen-2.5-14B at 30%: KL PPL 优势显著（7.62 vs 8.73），但 MMLU 落后 8pp（63.7 vs 71.8）。核心叙事是"output-distribution preservation beats per-neuron classification"，但如果 KL 更好地保留了输出分布，为什么 downstream 性能反而下降？论文给出的"knowledge density"解释是未经检验的推测。Uniform 仅恢复 +0.8pp。这是核心 claim 的最大反例。

**N3** [critical] `\enlargethispage{10\baselineskip}` 页面操控
- 位置：experiments.tex L253
- 在第 8 页增加约 10 行额外内容，底部 margin 被显著压缩。ACL 模板禁止修改 margins。可能导致 desk reject。

### Should-Fix 问题

**W1** 50% downstream collapse 与叙事 framing 不一致（Abstract 突出 49% PPL advantage 但 MMLU ≈ random）
**W2** 训练-评估域重叠（WikiText-103 训练 / WikiText-2 评估，OOD 仅 PPL 无 downstream）
**W3** 39 篇引用偏少；遗漏 Activation Sparsity Opportunities (2412.12178)、Post-Training Calibration (2412.07174)、Activation Pattern Clustering (2025) 等
**W4** 无实际推理加速（pipeline +6.4% overhead，unstructured masks 无 wall-clock speedup）
**W5** Gradient coupling vs oracle quality 未 disentangle（论文自己提出的 ablation "KL-derived masks as BCE targets" 未执行）

### 小问题

- Appendix C Figure 3 上半部分显示 placeholder 文字而非实际图片
- bib key `xu2026spon` year 标记为 2026 但实际为 ICML 2025
- Abstract 数字密度偏高（7 句含 11 个数字）
- §4.5 的 `\label{sec:14b}` 放在 paragraph 后可能导致引用指向问题

### Questions for Authors

1. 能否提供用 KL-derived masks 作为 BCE targets 的 ablation？
2. 14B 上 KL predictor 的 per-layer retention 分布是什么？
3. 如果 PPL 是"poor proxy for reasoning"，为什么核心对比以 PPL 为主？
4. 在非 Wikipedia 域训练的 predictor 是否仍有同等优势？

### Overall Assessment

**3.0 — Findings**。8B 实证贡献扎实（F1-PPL 解耦、compensation 冗余、regime 分析），但方法论新颖性有限（MaskLLM 后技术距离不够），14B 结果与核心叙事矛盾，`\enlargethispage{10\baselineskip}` 是格式违规。适合 Findings track。

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

_source line 722 · 2026-05-18T14:20:04.530562+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6: 外部审稿线', 'status': 'completed', 'activeForm': '外部审稿未启用，跳过'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '两位 Reviewer 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': 'Reviewer 交叉分享并逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛或需要下一轮'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6: 外部审稿线', 'status': 'completed', 'activeForm': '外部审稿未启用，跳过'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '两位 Reviewer 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': 'Reviewer 交叉分享并逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛或需要下一轮'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-18T14:20:04.581324+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-18T14:20:17.849216+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n### Reviewer 2 评分：3.0 (Findings)\n\n**Must-Fix:**\n\n**N1** [critical] 方法论新颖性不足以支撑 Main Conference\n- Forward KL distillation、Gumbel-Sigmoid、adaptive penalty 均为成熟技术。MaskLLM 已将 frozen weights + learnable masks + KL + Gumbel relaxation 用于 LLM sparsity，技术栈高度重叠。§3.5 gradient 分析是 end-to-end > decomposed 这一公知原则的直接实例化。Table 1 taxonomy 是循环论证式新颖性声明。\n\n**N2** [critical] 14B 结果与核心叙事矛盾\n- Qwen-2.5-14B at 30%: KL PPL 7.62 vs TEAL 8.73（优势），但 MMLU 63.7 vs 71.8（落后 8pp）。核心叙事\"output-distribution preservation beats per-neuron classification\"与此矛盾。\"Knowledge density\"解释为未验证推测。\n\n**N3** [critical] `\\enlargethispage{10\\baselineskip}` 页面操控\n- 第 8 页增加约 10 行额外内容，底部 margin 被显著压缩。ACL 模板禁止修改 margins，可能 desk reject。\n\n**Should-Fix:**\n\n**W1** 50% downstream collapse 与叙事 framing 不一致（Abstract 突出 49% PPL advantage 但 MMLU ≈ random）\n**W2** 训练-评估域重叠（WikiText-103 训练 / WikiText-2 评估，OOD 仅 PPL 无 downstream）\n**W3** 39 篇引用偏少；遗漏若干相关工作\n**W4** 无实际推理加速（+6.4% overhead）\n**W5** Gradient coupling vs oracle quality 未 disentangle（论文自己提出的 ablation 未执行）\n\n**小问题:**\n- Appendix C Figure 3 可能有 placeholder\n- bib key `xu2026spon` year 标 2026 实为 ICML 2025\n- Abstract 数字密度偏高\n- §4.5 的 `\\label{sec:14b}` 位置可能导致引用问题\n\n---\n\n请对每个 N 和 W 逐条回应 [AGREE] 或 [REBUT]。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu",
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
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n### Reviewer 2 评分：3.0 (Findings)\n\n**Must-Fix:**\n\n**N1** [critical] 方法论新颖性不足以支撑 Main Conference\n- Forward KL distillation、Gumbel-Sigmoid、adaptive penalty 均为成熟技术。MaskLLM 已将 frozen weights + learnable masks + KL + Gumbel relaxation 用于 LLM sparsity，技术栈高度重叠。§3.5 gradient 分析是 end-to-end > decomposed 这一公知原则的直接实例化。Table 1 taxonomy 是循环论证式新颖性声明。\n\n**N2** [critical] 14B 结果与核心叙事矛盾\n- Qwen-2.5-14B at 30%: KL PPL 7.62 vs TEAL 8.73（优势），但 MMLU 63.7 vs 71.8（落后 8pp）。核心叙事\"output-distribution preservation beats per-neuron classification\"与此矛盾。\"Knowledge density\"解释为未验证推测。\n\n**N3** [critical] `\\enlargethispage{10\\baselineskip}` 页面操控\n- 第 8 页增加约 10 行额外内容，底部 margin 被显著压缩。ACL 模板禁止修改 margins，可能 desk reject。\n\n**Should-Fix:**\n\n**W1** 50% downstream collapse 与叙事 framing 不一致（Abstract 突出 49% PPL advantage 但 MMLU ≈ random）\n**W2** 训练-评估域重叠（WikiText-103 训练 / WikiText-2 评估，OOD 仅 PPL 无 downstream）\n**W3** 39 篇引用偏少；遗漏若干相关工作\n**W4** 无实际推理加速（+6.4% overhead）\n**W5** Gradient coupling vs oracle quality 未 disentangle（论文自己提出的 ablation 未执行）\n\n**小问题:**\n- Appendix C Figure 3 可能有 placeholder\n- bib key `xu2026spon` year 标 2026 实为 ICML 2025\n- Abstract 数字密度偏高\n- §4.5 的 `\\label{sec:14b}` 位置可能导致引用问题\n\n---\n\n请对每个 N 和 W 逐条回应 [AGREE] 或 [REBUT]。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-18T14:20:36.293235+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18444
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-18T14:20:36.444151+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n### Reviewer 1 评分：3.0 (Findings)\n\n**Must-Fix:**\n\n**N1** [critical] 核心因果 claim 存在未隔离的混淆变量\n- BCE 使用 magnitude-based oracle masks，KL 直接优化输出分布——两个变量同时变化。论文承认\"an ablation using KL-derived masks as BCE targets would isolate the effect\"但未执行。Oracle F1 分析（BCE 0.613 vs KL 0.540，但 KL PPL 好 139%）无法区分是 gradient coupling 还是 target quality 的贡献。\n\n**N2** [critical] \"Three Operating Regions\" 分析证据不足\n- 每个 regime 仅一个数据点（30%、40%、50%），40% 仅单 seed。考虑到 30% global MMLU σ=9.5pp，40% 的 7.4pp 差异可能在 seed variance 内。边界（35%?）完全未知。\n\n**N3** [critical] 14B 结果与核心 claim 显著矛盾\n- KL PPL 7.62（最优）但 MMLU 63.72 vs TEAL 71.83（-8.1pp）。\"Knowledge density\"解释为推测。如果 scale up 时核心优势反转，claim 的 generalization scope 需严格限定。\n\n**Should-Fix:**\n\n**W1** `\\enlargethispage{10\\baselineskip}` 格式操纵——ACL 不允许修改 margin/layout\n**W2** BCE baseline 比较不完全公平——30% BCE 未报告，且 BCE 和 KL 的 target 不同\n**W3** 训练/评估数据同族（WikiText-103→WikiText-2），C4 OOD 仅 2-seed 且无 downstream\n**W4** SNR 分析仅到 step 300（训练跑 1000 步），step 300 不是真正 convergence，bootstrap 参数未报告\n**W5** Adaptive penalty controller 在 30%（recommended point）不收敛：actual 28.5%（5% deviation），给 KL 不公平的 sparsity 优势\n**W6** 无实际推理加速（+6.4% overhead，unstructured masks 无法被硬件加速）\n\n**小问题:**\n1. Figure 1 位置偏晚（第 6 页）\n2. \"renders compensation redundant\" 仅测试一种 compensation 架构\n3. Abstract \"7-14B\" 暗示跨 scale 一致但 14B downstream 矛盾\n4. Table 2 caption 50% uniform PPL 与正文不一致（11.92 vs 11.96）\n5. Downstream benchmark 选择标准未解释\n6. Appendix 编号可能需检查\n\n---\n\n请对每个 N 和 W 逐条回应 [AGREE] 或 [REBUT]。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu",
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
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n### Reviewer 1 评分：3.0 (Findings)\n\n**Must-Fix:**\n\n**N1** [critical] 核心因果 claim 存在未隔离的混淆变量\n- BCE 使用 magnitude-based oracle masks，KL 直接优化输出分布——两个变量同时变化。论文承认\"an ablation using KL-derived masks as BCE targets would isolate the effect\"但未执行。Oracle F1 分析（BCE 0.613 vs KL 0.540，但 KL PPL 好 139%）无法区分是 gradient coupling 还是 target quality 的贡献。\n\n**N2** [critical] \"Three Operating Regions\" 分析证据不足\n- 每个 regime 仅一个数据点（30%、40%、50%），40% 仅单 seed。考虑到 30% global MMLU σ=9.5pp，40% 的 7.4pp 差异可能在 seed variance 内。边界（35%?）完全未知。\n\n**N3** [critical] 14B 结果与核心 claim 显著矛盾\n- KL PPL 7.62（最优）但 MMLU 63.72 vs TEAL 71.83（-8.1pp）。\"Knowledge density\"解释为推测。如果 scale up 时核心优势反转，claim 的 generalization scope 需严格限定。\n\n**Should-Fix:**\n\n**W1** `\\enlargethispage{10\\baselineskip}` 格式操纵——ACL 不允许修改 margin/layout\n**W2** BCE baseline 比较不完全公平——30% BCE 未报告，且 BCE 和 KL 的 target 不同\n**W3** 训练/评估数据同族（WikiText-103→WikiText-2），C4 OOD 仅 2-seed 且无 downstream\n**W4** SNR 分析仅到 step 300（训练跑 1000 步），step 300 不是真正 convergence，bootstrap 参数未报告\n**W5** Adaptive penalty controller 在 30%（recommended point）不收敛：actual 28.5%（5% deviation），给 KL 不公平的 sparsity 优势\n**W6** 无实际推理加速（+6.4% overhead，unstructured masks 无法被硬件加速）\n\n**小问题:**\n1. Figure 1 位置偏晚（第 6 页）\n2. \"renders compensation redundant\" 仅测试一种 compensation 架构\n3. Abstract \"7-14B\" 暗示跨 scale 一致但 14B downstream 矛盾\n4. Table 2 caption 50% uniform PPL 与正文不一致（11.92 vs 11.96）\n5. Downstream benchmark 选择标准未解释\n6. Appendix 编号可能需检查\n\n---\n\n请对每个 N 和 W 逐条回应 [AGREE] 或 [REBUT]。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-18T14:20:37.805084+00:00_

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


### Tool call

_source line 728 · 2026-05-18T14:20:47.600694+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "等待两位 Reviewer 完成交叉分享回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: distill_sparse_swiglu\n- 论文路径: projects/distill_sparse_swiglu/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 截止日期: 2026-05-25\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "等待两位 Reviewer 完成交叉分享回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: distill_sparse_swiglu\n- 论文路径: projects/distill_sparse_swiglu/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 截止日期: 2026-05-25\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-18T14:20:47.703213+00:00_

Next wakeup scheduled for 14:25:00 (in 252s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 102
}
```

</details>

---


### Assistant

_source line 730 · 2026-05-18T14:20:49.951832+00:00_

交叉分享任务已分配。两位 Reviewer 将互相审阅对方意见并逐条回应 [AGREE]/[REBUT]。等待回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 54

## Round 54

2 recorded events


### User

_source line 731 · 2026-05-18T14:20:52.464646+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：评分 **3.0 (Findings)**。三个 critical 问题：（1）方法论新颖性不足——Forward KL / Gumbel-Sigmoid / Lagrangian 均为成熟技术，与 MaskLLM 技术栈高度重叠；（2）14B MMLU 退化 8pp 与"输出分布保持"叙事矛盾；（3）`\enlargethispage{10\baselineskip}` 格式违规。五个 should-fix：50% downstream collapse framing、训练评估域重叠、引用偏少、无实际加速、coupling vs oracle quality 未 disentangle。

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

_source line 732 · 2026-05-18T14:20:58.507492+00:00_

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


## Round 55

## Round 55

4 recorded events


### User

_source line 733 · 2026-05-18T14:23:11.237379+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 交叉回应 Reviewer 2 意见

---

### Must-Fix 逐条回应

**[AGREE with nuance] R2-N1: 方法论新颖性不足**

同意 novelty concern 对 Main Conference 是合理的，但 MaskLLM 重叠程度被高估。

同意的部分：
- Forward KL、Gumbel-Sigmoid、adaptive penalty 确实都是成熟技术，论文本身也承认 "Our contribution is primarily empirical"（Related Work, line 18）。
- Table 1 taxonomy 的"循环论证"批评有道理：定义两个轴使自己恰好填充空白 cell，这是 positioning 技巧而非独立贡献。
- §3.6 的梯度分析结构上是 "end-to-end gradient couples neurons" 这一公知原则的直接实例化，analytical novelty 有限。

反驳的部分：
- MaskLLM 解决的是 **static N:M weight sparsity**（per-group Gumbel-Softmax，固定 mask 不随 input 变化），本文是 **dynamic per-token activation sparsity under global budget constraint**。论文在 Related Work 第 14-16 行明确区分："MaskLLM finds optimal static N:M patterns within fixed groups, while we predict dynamic per-token masks under a global budget constraint. The structural mismatch we characterize (per-neuron gradient decomposition vs. global top-k) does not arise in MaskLLM's per-group categorical setting." 这不是同一个优化问题，技术栈的重叠是表面层面的（都用 KL + Gumbel + frozen weights），而 problem formulation 是不同的。
- 真正的 novelty 不在于单个组件，而在于将 KL distillation 应用于 contextual sparsity prediction 这个 **specific combination**，并用实证量化了什么时候 coupling matters。这是 empirical contribution 而非 methodological contribution，论文定位基本准确。

**综合判断**：R2 的 novelty concern 对 Main 合理，但 MaskLLM 的类比不足以构成 "已有工作"——两者解决不同问题。论文作为 empirical contribution 适合 Findings。

---

**[AGREE] R2-N2: 14B 结果与核心叙事矛盾**

完全同意，与我的 R1-N3 一致。

补充证据：
- Table 7：KL PPL 7.62（最优）但 MMLU 63.72（vs TEAL 71.83，落后 8.1pp），GSM8K 48.82（vs BCE 53.07，落后 4.3pp）。
- Uniform allocation 仅恢复 +0.8pp MMLU（64.49 vs 63.72），说明差距不是 allocation-induced。
- §4.6 的解释 "Higher knowledge density at 14B may cause KL's output-preservation objective to sacrifice task-specific pathways" 是推测性的、无实证支撑的 post-hoc rationalization。
- 这直接削弱了 Abstract 第 7 行的 claim "confirms the PPL advantage across 7-14B"——PPL advantage 确实 confirmed，但 downstream 方向相反，而 downstream 才是最终衡量标准。

建议作者在 Abstract 和 Introduction 中将 scope 明确限定为 7-8B，14B 作为 scale-dependent limitation 而非 confirmation。

---

**[AGREE with downgrade] R2-N3: `\enlargethispage{10\baselineskip}` 页面操控**

同意这是问题（与我的 R1-W1 一致），但对严重性判断略有不同。

同意：
- `\enlargethispage{10\baselineskip}`（experiments.tex line 253）确实人为扩展了第 8 页。从 PDF 第 8 页可观察到该页内容密度远超其他页面（包含 Tables 5-7、三个 regime 分析、SPON、cross-architecture、14B、inference efficiency、完整 Conclusion）。
- ACL 模板确实要求不修改 margins/layout。

轻微反驳 "desk reject" 判断：
- `\enlargethispage` 是 LaTeX 的标准命令，不同于直接修改 `\geometry` 或 sty 文件中的 margin 值。许多已发表论文使用过此命令。ARR desk reject 通常针对 **margin/font-size 修改** 而非 per-page stretching。
- 风险确实存在，但更可能的结果是 AC 要求修改而非直接 desk reject。

**建议分级**：Should-Fix (high priority) 而非 Critical。作者应立即移除该命令，将 SPON 详细分析或部分 Table 移至 appendix。

---

### Should-Fix 逐条回应

**[AGREE] R2-W1: 50% downstream collapse 与叙事 framing 不一致**

同意。Abstract 第 6 行突出 "the PPL advantage widens to 49%"，但 Table 2 显示 50% MMLU ≈ 28%（≈random for 4-choice）、GSM8K < 2.2%。Abstract 后半句 "but downstream tasks degrade regardless of allocation" 做了 hedge，但读者首先记住的是 "49% advantage"。

论文在 §4.5 正确将此分析为 "capacity-limited regime"（MMLU 28.1±0.2% vs 28.0±0.6%，差异不显著），但 Abstract 的 emphasis 与此不匹配。建议 Abstract 更明确传达：50% sparsity 下 PPL 改善虽大但 downstream 已 collapse，实际推荐 30%。

---

**[AGREE] R2-W2: 训练-评估域重叠**

同意，与我的 R1-W3 一致。补充：C4 OOD 评估（Appendix D）在 30% 处 PPL 退化为 1.74× dense（vs WikiText-2 的 1.47×），退化显著更大。C4 30% 仅 2-seed（vs 主结果 3-seed），且完全没有 C4 downstream benchmarks。如果 predictor 对 WikiText 族有分布偏好，PPL 优势可能部分来自 distribution overlap 而非 method superiority。

---

**[REBUT] R2-W3: 39 篇引用偏少**

不同意引用数量不足。

- 39 篇引用对于一篇聚焦于 **specific technique (KL for sparsity prediction)** 的 empirical paper 是合理的。论文不是 survey 性质的综述。
- 引用覆盖了所有关键类别：activation sparsity methods（TEAL, CATS, R-Sparse, DIP, SparseInfer, DejaVu, ShadowLLM, FastForward, SVD-CSP, PowerInfer, MaskLLM）、activation function engineering（ReLU Strikes Back, TurboSparse, ProSparse, Sparsing Law, MiniTron）、weight pruning（Wanda, SparseGPT）、KL distillation（Kim & Rush 2016, DistilBERT, MiniLLM, GKD）、conditional computation（Switch Transformers, MoD, D2DMoE）、relaxation methods（Gumbel-Softmax, Concrete, L0）、SPON。
- 我在 R1 审稿中建议补充 Expert Choice routing 等 MoE 稀疏性文献，但这是 "nice to have" 而非 coverage gap。
- EMNLP 录用论文引用量中位数约 40-50，39 在正常范围内。

---

**[AGREE] R2-W4: 无实际推理加速**

同意，与我的 R1-W6 一致。Appendix A Table 8 显示 +6.4% overhead without any demonstrated speedup from sparsity（unstructured masks 无硬件加速支持）。论文在 Limitations 中诚实讨论了这一点，但 Introduction 的 motivation framing 可以更清楚地 set expectations。

---

**[AGREE] R2-W5: Gradient coupling vs oracle quality 未 disentangle**

完全同意，这与我的 R1-N1 是同一问题（我将其列为 Critical）。

补充分析：
- 论文 §4.3 明确写道 "an ablation using KL-derived masks as BCE targets would isolate the effect"——这证明作者意识到了这个 confound。
- BCE isolation ablation（Table 3, BCE+Gumbel+Penalty = PPL 38.02）并不能隔离 loss function 的贡献，因为 penalty controller 是为 KL 设计的，与 BCE 不兼容（结果比 vanilla BCE 更差：38.02 vs 27.97）。
- 缺失的消融是：**用 KL-trained predictor 产生的 masks 作为 BCE 的 oracle targets**，保持其他一切不变。如果 BCE 在"正确 targets"下仍差，则 coupling 是关键因素；如果 BCE 显著缩小差距，则 target quality 是主因。这是一个可在数小时内完成的实验。

我认为这应该是 Must-Fix 而非 Should-Fix——它是核心 claim 的关键 confound。R2 将其放在 W5 可能低估了它的影响。

---

### 小问题回应

**[AGREE] Appendix C Figure 3 placeholder**
确认。PDF 第 13 页 Figure 3 显示 "[Placeholder: lagrangian_dynamics.pdf]" 而非实际图表。appendix.tex line 139 引用 `lagrangian_dynamics.pdf`，但该文件似乎缺失或为占位符。这是提交前必须修复的问题。

**[REBUT with nuance] bib key `xu2026spon` year**
Bib key 名称 `xu2026spon` 中的 "2026" 仅是 key identifier，不影响渲染。references.bib 中该条目的 `year = {2025}` 和 `booktitle = {ICML}` 是正确的。渲染输出显示 "(Xu et al., 2025)"。这是 bib key 命名不规范但不影响论文输出的 cosmetic issue。

**[AGREE] Abstract 数字密度偏高**
Abstract 包含：139%、<1%、67.2M、30%、50%、18%、7.5×、49%、7-14B、MMLU gap 等大量数字。每个句子都有 1-2 个数字，读起来像 results summary 而非 story。建议减少到关键的 3-4 个数字。

**[AGREE] `\label{sec:14b}` 位置问题**
确认。`\label{sec:14b}` 位于 `\paragraph{Scale Generalization: Qwen-2.5-14B.}` 之后（experiments.tex line 224），但 `\paragraph` 在 ACL style 中没有独立 counter。`\ref{sec:14b}` 会解析为父级 section 编号（§4.6 = SPON Orthogonality Analysis），导致 Limitations 中 `\S\ref{sec:14b}` 指向错误 section。应改用 `\S4.6` 硬编码或将 14B 提升为独立 `\subsection`。

---

### 总体评估与 R2 的一致性

R2 和我的 Overall 评分一致：**3.0 (Findings)**。

两位 reviewer 共识的核心问题：
1. KL vs BCE 的因果 claim 存在未隔离的 confound（R1-N1 = R2-W5）
2. 14B 结果与核心叙事矛盾（R1-N3 = R2-N2）
3. 无实际推理加速（R1-W6 = R2-W4）
4. 训练/评估域重叠（R1-W3 = R2-W2）

R1 额外强调的问题：
- Three Operating Regions 分析证据不足（R1-N2）——R2 未提及，但我认为这是独立的 critical issue
- Adaptive penalty 在 30% 处不收敛导致 unfair comparison（R1-W5）

R2 额外强调的问题：
- Novelty 不足（R2-N1）——我部分同意，但认为 MaskLLM 类比被高估
- 格式操纵严重性（R2-N3 = R1-W1）——R2 评为 critical，我评为 high-priority warning

论文作为 empirical contribution 有价值（KL > BCE for sparsity prediction 的观察可能启发后续工作），但核心 claim 的因果归因需要更严格的 ablation 支撑，且 generalization scope 需要从 "7-14B" 收紧到 "7-8B"。Findings 级别合适。


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

_source line 734 · 2026-05-18T14:23:24.943204+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "等待 Reviewer 2 完成交叉回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: distill_sparse_swiglu\n- 论文路径: projects/distill_sparse_swiglu/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 截止日期: 2026-05-25\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "等待 Reviewer 2 完成交叉回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: distill_sparse_swiglu\n- 论文路径: projects/distill_sparse_swiglu/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 截止日期: 2026-05-25\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 735 · 2026-05-18T14:23:24.943628+00:00_

Next wakeup scheduled for 14:28:00 (in 275s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 736 · 2026-05-18T14:23:27.659987+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 56

## Round 56

12 recorded events


### User

_source line 737 · 2026-05-18T14:23:28.660491+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心结论：R2 和我在 Overall 3.0 (Findings) 上一致。5 个问题达成共识（因果 confound、14B 矛盾、无加速、域重叠、格式操纵），分歧点在于 MaskLLM novelty 类比的严重性和格式操纵的分级。我在 R2-W5（gradient coupling vs oracle quality）上认为应升级为 Must-Fix，在 R2-N3（formatting）上认为应降级为 high-priority Should-Fix。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 审稿意见

### Must-Fix

**[AGREE] R1-N1: 核心因果 claim 存在未隔离的混淆变量**
完全同意，与我的 W5 一致。BCE 和 KL 在 gradient coupling 和 optimization target 两个维度同时不同。F1-PPL 反向解耦（Table 3）是好的实证发现但不能归因于 coupling 单一因素。论文承认的"KL-derived masks as BCE targets" ablation 并不复杂但缺失，应为 must-fix。

**[AGREE] R1-N2: "Three Operating Regions" 证据不足**
同意，但补充 nuance。定性观察（非单调 allocation 偏好）有价值，但"three regions"的确定性表述过度。40% 仅单 seed，在 30% MMLU σ=9.5pp 背景下 40% 的 7.4pp 差异可能在 noise 内。论文承认边界未知（experiments.tex L151）但标题仍使用确定性表述。建议弱化为"non-monotonic allocation preference observed at sampled sparsity levels"。

**[AGREE] R1-N3: 14B 结果与核心 claim 矛盾**
完全同意，与我的 N2 一致。补充：Abstract "confirms PPL advantage across 7-14B" 和 Conclusion "PPL advantage persists" 都在 selective reporting——PPL persist 但 downstream 反转，cherry-picking PPL 降低可信度。

### Should-Fix

**[AGREE] R1-W1: `\enlargethispage` 格式操纵**
同意，且我在自己的审稿中将其列为 critical（N3）而非 should-fix。10\baselineskip ≈ 10 行额外内容，等同于修改单页 bottom margin，可能导致 desk reject。严重程度应为 critical。

**[AGREE] R1-W2: BCE baseline 比较不完全公平**
同意。30%（recommended operating point）完全无 BCE baseline；且 BCE 使用"magnitude oracle + FastForward compensation + no TEAL allocation"而 KL 使用"Gumbel-Sigmoid + TEAL allocation"，allocation 策略也不同。

**[AGREE] R1-W3: 训练/评估数据同族**
同意，与我的 W2 一致。WikiText-103→WikiText-2 同源。OOD 仅 PPL 无 downstream。

**[AGREE] R1-W4: SNR 分析仅到 step 300**
同意，是我遗漏的重要问题。训练 1000 步但 SNR 仅测到 step 300（30% of training）。论文称 step 300 为"convergence"但 Table 12 显示 step 800+ 才 PPL 收敛。SNR non-monotonic，300 步后可能再次反转。Misleading。

**[REBUT] R1-W5: Penalty controller 不收敛给 KL 不公平 sparsity 优势**
部分不同意。Appendix C 的 interpolation 论证合理：TEAL at 28.5% yields PPL ≈ 10.7 vs 10.97 at 30%，差距仅 0.27 PPL，远小于 KL-TEAL gap（2.01 PPL）。1.5% sparsity 偏差影响 sub-linear，不足以解释 18% PPL 优势。但同意 λ 命中 cap 本身是 controller failure mode，应更明确讨论。

**[AGREE] R1-W6: 无实际推理加速**
同意，与我的 W4 一致。

### 小问题
1. Figure 1 位置偏晚: 同意
2. Compensation 仅一种架构: 同意但 minor（FastForward 是领域内唯一 compensation 工作）
3. Abstract "7-14B": 同意，selective reporting
4. Table 2 caption 50% uniform PPL 不一致: 确认——caption 说"3-seed (11.92±0.07)"但 table body 显示 11.96，应统一
5. Downstream benchmark 选择标准未解释: 同意
6. Appendix 编号: 未发现明显问题

### 总结
与 R1 在绝大多数问题上一致。唯一部分不同意的是 W5（penalty controller sparsity deviation）——论文的 interpolation 论证合理地解释了 1.5% 偏差的影响可忽略。两位 reviewer 的共识 critical issues：(1) causal confound 未隔离；(2) 14B 叙事矛盾；(3) 格式违规。这三个问题共同支撑 Findings 而非 Conference 的评分。

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

_source line 738 · 2026-05-18T14:24:26.361343+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6: 外部审稿线', 'status': 'completed', 'activeForm': '外部审稿未启用，跳过'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '两位 Reviewer 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '两位 Reviewer 完成交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '分析共识与分歧，判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6: 外部审稿线', 'status': 'completed', 'activeForm': '外部审稿未启用，跳过'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '两位 Reviewer 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '两位 Reviewer 完成交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '分析共识与分歧，判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-18T14:24:26.411967+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-18T14:24:39.389194+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6: 外部审稿线', 'status': 'completed', 'activeForm': '外部审稿未启用，跳过'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '两位 Reviewer 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '两位 Reviewer 完成交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '已收敛，无需第二轮'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6: 外部审稿线', 'status': 'completed', 'activeForm': '外部审稿未启用，跳过'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '两位 Reviewer 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '两位 Reviewer 完成交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '已收敛，无需第二轮'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-18T14:24:39.389605+00:00_

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

_source line 742 · 2026-05-18T14:26:01.008492+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # === Round 8 (fresh review) findings ===\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound: KL-derived masks as BCE targets ablation missing\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-N1 raise critical, R2-W5 raise should-fix then upgraded to critical in cross-response. Full consensus. BCE uses magnitude oracles while KL optimizes output directly — two variables change simultaneously. Paper acknowledges missing ablation (§4.3) but did not execute it.\"}\n    action_items:\n      - {round: 8, action: \"Execute KL-derived masks as BCE targets ablation to isolate coupling vs target quality\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-N2\"\n    summary: \"14B MMLU reversal: KL PPL best (7.62) but MMLU -8.1pp vs TEAL (63.7 vs 71.8), contradicts output-preservation narrative\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-N3 + R2-N2, full AGREE in cross-response. 'Knowledge density' explanation is untested speculation. Uniform only recovers +0.8pp. Abstract 'confirms PPL advantage across 7-14B' is selective reporting — PPL persists but downstream reverses.\"}\n    action_items:\n      - {round: 8, action: \"Restrict claim scope to 7-8B in Abstract/Intro; present 14B as scale-dependent limitation, not confirmation\", assigned_to: \"\", status: open}\n      - {round: 8, action: \"Test additional 14B sparsity levels (40%, 50%) and per-layer retention analysis\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-N3\"\n    summary: \"Three Operating Regions: only 3 data points (30/40/50%), 40% single seed, regime boundaries unknown\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-N2 raise critical, R2 AGREE with nuance. 40% global-uniform gap (7.4pp) within noise given 30% MMLU σ=9.5pp. Paper acknowledges boundary uncertainty (L151) but framing still deterministic.\"}\n    action_items:\n      - {round: 8, action: \"Either add 25%/35%/45% experiments (2-seed min) or weaken framing to 'non-monotonic allocation preference observed at sampled levels'\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-N4\"\n    summary: \"\\\\enlargethispage{10\\\\baselineskip} format manipulation — ACL prohibits margin modification\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R2-N3 critical, R1-W1 high-priority warning. R2 says desk reject risk; R1 says AC more likely to request fix. Consensus: must remove. Page 8 contains Tables 5-7, regime analysis, SPON, cross-arch, 14B, latency, full Conclusion — far too dense.\"}\n    action_items:\n      - {round: 8, action: \"Remove \\\\enlargethispage, move SPON analysis or partial tables to appendix\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W1\"\n    summary: \"Method novelty limited: Forward KL + Gumbel + Lagrangian are mature techniques, MaskLLM overlap\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R2-N1 critical, R1 AGREE with nuance — MaskLLM overlap overstated (static N:M vs dynamic per-token), but agrees novelty insufficient for Main. Consensus: empirical contribution fits Findings.\"}\n    action_items:\n      - {round: 8, action: \"No action needed if targeting Findings; for Main, would need novel algorithmic component\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W2\"\n    summary: \"50% downstream collapse contradicts Abstract emphasis on 49% PPL advantage\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R2-W1, R1 AGREE. MMLU≈28%(random), GSM8K<2.2% at 50%. Abstract hedges but emphasis on PPL misleading.\"}\n    action_items:\n      - {round: 8, action: \"Abstract to more clearly convey 50% downstream collapse; emphasize 30% as recommended\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W3\"\n    summary: \"BCE baseline missing at 30% (recommended operating point); allocation protocol differs\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W2, R2 AGREE. Table 2 has no BCE row at 30%. BCE uses FastForward compensation + no TEAL allocation while KL uses TEAL. Not fully apples-to-apples.\"}\n    action_items:\n      - {round: 8, action: \"Add BCE 30% results to Table 2; consider BCE with TEAL allocation for fair comparison\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W4\"\n    summary: \"Training/eval domain overlap: WikiText-103→WikiText-2, C4 OOD only PPL no downstream\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W3 + R2-W2, full AGREE. C4 30% degradation 1.74× vs WikiText-2 1.47×. C4 30% only 2-seed. No C4 downstream benchmarks.\"}\n    action_items:\n      - {round: 8, action: \"Add C4 downstream eval or explain why WikiText-2 downstream generalizes; upgrade C4 30% to 3-seed\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W5\"\n    summary: \"SNR analysis only to step 300 (30% of training), misleading 'convergence' claim\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W4, R2 AGREE. PPL converges at step 800+ but SNR measured only to 300. Non-monotonic trajectory may reverse after 300. Bootstrap parameters unreported.\"}\n    action_items:\n      - {round: 8, action: \"Extend SNR to 1000 steps; report bootstrap sample size; correct 'convergence' language\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W6\"\n    summary: \"No actual inference speedup: +6.4% overhead, unstructured masks\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W6 + R2-W4, full AGREE. Limitations honest but Introduction should set expectations earlier.\"}\n    action_items:\n      - {round: 8, action: \"Introduction to clarify contribution is prediction quality, not speedup\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-I1\"\n    summary: \"Penalty controller λ hits cap at 30% (actual 28.5%, 5% deviation)\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W5 raise warning, R2 partial REBUT — interpolation shows <0.3 PPL impact, sub-linear. Consensus: impact negligible but should note actual sparsity in Table 2.\"}\n    action_items:\n      - {round: 8, action: \"Note actual sparsity in Table 2 caption or footnote\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-I2\"\n    summary: \"Minor issues: Figure 1 late placement, Table 2 PPL inconsistency, Abstract number density, label cross-ref error, Appendix Figure placeholder\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Collection of minor issues: (1) Fig 1 on p6 too late; (2) Table 2 caption says 11.92±0.07 but body shows 11.96; (3) Abstract ~11 numbers in 7 sentences; (4) \\\\label{sec:14b} resolves to wrong section; (5) Figure 3 in Appendix C may be placeholder.\"}\n    action_items:\n      - {round: 8, action: \"Batch fix all minor issues before submission\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # === Prior rounds (1-7) — compact archive, status retained from last update ===\n  # These issues are from prior review rounds. Status carried forward as-is.\n  # Round 8 fresh reviewers independently re-raised several of these (noted in R8-* entries).\n\n  - id: \"R3-S2\"\n    summary: \"BCE vs KL comparison is pipeline difference not just loss difference — coupling vs oracle confound\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 8\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE\"}\n      - {round: 7, reviewers: [1, 2], note: \"Language corrected to 'correlates vs causes'. Still no ablation.\"}\n      - {round: 8, reviewers: [1, 2], note: \"Re-raised as R8-N1 critical. Fresh reviewers independently identified same confound.\"}\n    action_items:\n      - {round: 6, action: \"Weaken coupling causal claim to correlation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 8, action: \"See R8-N1\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C2\"\n    summary: \"PPL-downstream disconnect: KL global MMLU≈random at 50%, framing contradiction\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 8\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"Two independent raises, strong AGREE.\"}\n      - {round: 7, reviewers: [1, 2], note: \"14B data worsens issue. Narrative improved but fundamental tension remains.\"}\n      - {round: 8, reviewers: [1, 2], note: \"Re-raised as R8-N2 + R8-W2. Fresh reviewers see same fundamental problem.\"}\n    action_items:\n      - {round: 7, action: \"14B discussion added\", assigned_to: \"paper_agent\", status: done}\n      - {round: 8, action: \"See R8-N2, R8-W2\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S1\"\n    summary: \"Core novelty vs MaskLLM distinction insufficient\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 8\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Contribution 1 reworded to 'Empirical observation'. MaskLLM comparison adequate. But method remains direct combination.\"}\n      - {round: 8, reviewers: [1, 2], note: \"Re-raised as R8-W1. Fresh R2 says critical for Main; R1 says MaskLLM overlap overstated but agrees Findings-level.\"}\n    action_items:\n      - {round: 8, action: \"See R8-W1\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R7-W2\"\n    summary: \"\\\\enlargethispage format manipulation\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    mentions:\n      - {round: 7, reviewers: [1], note: \"8\\\\baselineskip expansion noted.\"}\n      - {round: 8, reviewers: [1, 2], note: \"Re-raised as R8-N4. Now 10\\\\baselineskip. Upgraded to critical by both reviewers.\"}\n    action_items:\n      - {round: 8, action: \"See R8-N4\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R7-N1\"\n    summary: \"14B MMLU reversal exposes fundamental limitation of output-preservation objective\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Knowledge density discussion added but speculative.\"}\n      - {round: 8, reviewers: [1, 2], note: \"Re-raised as R8-N2 critical. Fresh reviewers see same contradiction.\"}\n    action_items:\n      - {round: 8, action: \"See R8-N2\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Statistical power: key comparisons still partially single-seed\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 8\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Table 2 improved: 30% KL global 3-seed, 50% KL MMLU 3-seed, BCE 3-seed. But 30% KL uniform PPL still single seed, 40% all single seed.\"}\n      - {round: 8, reviewers: [1, 2], note: \"R1-N2 notes 40% single seed. R1-W2 notes 30% BCE missing entirely.\"}\n    action_items:\n      - {round: 8, action: \"See R8-N3, R8-W3\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # Resolved issues from prior rounds (compact, not re-raised in R8)\n  - id: \"R2-N1\"\n    summary: \"Limitations section 格式不合规\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Fixed in Round 1\"\n    resolution_round: 1\n\n  - id: \"R6-N1\"\n    summary: \"'Eliminates compensation' claim — KL+compensation control experiment\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"KL+comp experiment done: 30% 2-seed + 50% identical metrics. Claim supported.\"\n    resolution_round: 7\n\n  - id: \"R3-C3\"\n    summary: \"No wall-clock speedup, efficiency framing\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    resolution: \"Reframed as understanding paper. Appendix + Limitations explicit.\"\n    resolution_round: 7"
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
    "issues_yaml": "issues:\n  # === Round 8 (fresh review) findings ===\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound: KL-derived masks as BCE targets ablation missing\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-N1 raise critical, R2-W5 raise should-fix then upgraded to critical in cross-response. Full consensus. BCE uses magnitude oracles while KL optimizes output directly — two variables change simultaneously. Paper acknowledges missing ablation (§4.3) but did not execute it.\"}\n    action_items:\n      - {round: 8, action: \"Execute KL-derived masks as BCE targets ablation to isolate coupling vs target quality\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-N2\"\n    summary: \"14B MMLU reversal: KL PPL best (7.62) but MMLU -8.1pp vs TEAL (63.7 vs 71.8), contradicts output-preservation narrative\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-N3 + R2-N2, full AGREE in cross-response. 'Knowledge density' explanation is untested speculation. Uniform only recovers +0.8pp. Abstract 'confirms PPL advantage across 7-14B' is selective reporting — PPL persists but downstream reverses.\"}\n    action_items:\n      - {round: 8, action: \"Restrict claim scope to 7-8B in Abstract/Intro; present 14B as scale-dependent limitation, not confirmation\", assigned_to: \"\", status: open}\n      - {round: 8, action: \"Test additional 14B sparsity levels (40%, 50%) and per-layer retention analysis\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-N3\"\n    summary: \"Three Operating Regions: only 3 data points (30/40/50%), 40% single seed, regime boundaries unknown\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-N2 raise critical, R2 AGREE with nuance. 40% global-uniform gap (7.4pp) within noise given 30% MMLU σ=9.5pp. Paper acknowledges boundary uncertainty (L151) but framing still deterministic.\"}\n    action_items:\n      - {round: 8, action: \"Either add 25%/35%/45% experiments (2-seed min) or weaken framing to 'non-monotonic allocation preference observed at sampled levels'\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-N4\"\n    summary: \"\\\\enlargethispage{10\\\\baselineskip} format manipulation — ACL prohibits margin modification\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R2-N3 critical, R1-W1 high-priority warning. R2 says desk reject risk; R1 says AC more likely to request fix. Consensus: must remove. Page 8 contains Tables 5-7, regime analysis, SPON, cross-arch, 14B, latency, full Conclusion — far too dense.\"}\n    action_items:\n      - {round: 8, action: \"Remove \\\\enlargethispage, move SPON analysis or partial tables to appendix\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W1\"\n    summary: \"Method novelty limited: Forward KL + Gumbel + Lagrangian are mature techniques, MaskLLM overlap\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R2-N1 critical, R1 AGREE with nuance — MaskLLM overlap overstated (static N:M vs dynamic per-token), but agrees novelty insufficient for Main. Consensus: empirical contribution fits Findings.\"}\n    action_items:\n      - {round: 8, action: \"No action needed if targeting Findings; for Main, would need novel algorithmic component\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W2\"\n    summary: \"50% downstream collapse contradicts Abstract emphasis on 49% PPL advantage\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R2-W1, R1 AGREE. MMLU≈28%(random), GSM8K<2.2% at 50%. Abstract hedges but emphasis on PPL misleading.\"}\n    action_items:\n      - {round: 8, action: \"Abstract to more clearly convey 50% downstream collapse; emphasize 30% as recommended\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W3\"\n    summary: \"BCE baseline missing at 30% (recommended operating point); allocation protocol differs\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W2, R2 AGREE. Table 2 has no BCE row at 30%. BCE uses FastForward compensation + no TEAL allocation while KL uses TEAL. Not fully apples-to-apples.\"}\n    action_items:\n      - {round: 8, action: \"Add BCE 30% results to Table 2; consider BCE with TEAL allocation for fair comparison\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W4\"\n    summary: \"Training/eval domain overlap: WikiText-103→WikiText-2, C4 OOD only PPL no downstream\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W3 + R2-W2, full AGREE. C4 30% degradation 1.74× vs WikiText-2 1.47×. C4 30% only 2-seed. No C4 downstream benchmarks.\"}\n    action_items:\n      - {round: 8, action: \"Add C4 downstream eval or explain why WikiText-2 downstream generalizes; upgrade C4 30% to 3-seed\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W5\"\n    summary: \"SNR analysis only to step 300 (30% of training), misleading 'convergence' claim\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W4, R2 AGREE. PPL converges at step 800+ but SNR measured only to 300. Non-monotonic trajectory may reverse after 300. Bootstrap parameters unreported.\"}\n    action_items:\n      - {round: 8, action: \"Extend SNR to 1000 steps; report bootstrap sample size; correct 'convergence' language\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W6\"\n    summary: \"No actual inference speedup: +6.4% overhead, unstructured masks\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W6 + R2-W4, full AGREE. Limitations honest but Introduction should set expectations earlier.\"}\n    action_items:\n      - {round: 8, action: \"Introduction to clarify contribution is prediction quality, not speedup\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-I1\"\n    summary: \"Penalty controller λ hits cap at 30% (actual 28.5%, 5% deviation)\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W5 raise warning, R2 partial REBUT — interpolation shows <0.3 PPL impact, sub-linear. Consensus: impact negligible but should note actual sparsity in Table 2.\"}\n    action_items:\n      - {round: 8, action: \"Note actual sparsity in Table 2 caption or footnote\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-I2\"\n    summary: \"Minor issues: Figure 1 late placement, Table 2 PPL inconsistency, Abstract number density, label cross-ref error, Appendix Figure placeholder\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Collection of minor issues: (1) Fig 1 on p6 too late; (2) Table 2 caption says 11.92±0.07 but body shows 11.96; (3) Abstract ~11 numbers in 7 sentences; (4) \\\\label{sec:14b} resolves to wrong section; (5) Figure 3 in Appendix C may be placeholder.\"}\n    action_items:\n      - {round: 8, action: \"Batch fix all minor issues before submission\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # === Prior rounds (1-7) — compact archive, status retained from last update ===\n  # These issues are from prior review rounds. Status carried forward as-is.\n  # Round 8 fresh reviewers independently re-raised several of these (noted in R8-* entries).\n\n  - id: \"R3-S2\"\n    summary: \"BCE vs KL comparison is pipeline difference not just loss difference — coupling vs oracle confound\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 8\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE\"}\n      - {round: 7, reviewers: [1, 2], note: \"Language corrected to 'correlates vs causes'. Still no ablation.\"}\n      - {round: 8, reviewers: [1, 2], note: \"Re-raised as R8-N1 critical. Fresh reviewers independently identified same confound.\"}\n    action_items:\n      - {round: 6, action: \"Weaken coupling causal claim to correlation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 8, action: \"See R8-N1\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C2\"\n    summary: \"PPL-downstream disconnect: KL global MMLU≈random at 50%, framing contradiction\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 8\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"Two independent raises, strong AGREE.\"}\n      - {round: 7, reviewers: [1, 2], note: \"14B data worsens issue. Narrative improved but fundamental tension remains.\"}\n      - {round: 8, reviewers: [1, 2], note: \"Re-raised as R8-N2 + R8-W2. Fresh reviewers see same fundamental problem.\"}\n    action_items:\n      - {round: 7, action: \"14B discussion added\", assigned_to: \"paper_agent\", status: done}\n      - {round: 8, action: \"See R8-N2, R8-W2\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S1\"\n    summary: \"Core novelty vs MaskLLM distinction insufficient\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 8\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Contribution 1 reworded to 'Empirical observation'. MaskLLM comparison adequate. But method remains direct combination.\"}\n      - {round: 8, reviewers: [1, 2], note: \"Re-raised as R8-W1. Fresh R2 says critical for Main; R1 says MaskLLM overlap overstated but agrees Findings-level.\"}\n    action_items:\n      - {round: 8, action: \"See R8-W1\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R7-W2\"\n    summary: \"\\\\enlargethispage format manipulation\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    mentions:\n      - {round: 7, reviewers: [1], note: \"8\\\\baselineskip expansion noted.\"}\n      - {round: 8, reviewers: [1, 2], note: \"Re-raised as R8-N4. Now 10\\\\baselineskip. Upgraded to critical by both reviewers.\"}\n    action_items:\n      - {round: 8, action: \"See R8-N4\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R7-N1\"\n    summary: \"14B MMLU reversal exposes fundamental limitation of output-preservation objective\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Knowledge density discussion added but speculative.\"}\n      - {round: 8, reviewers: [1, 2], note: \"Re-raised as R8-N2 critical. Fresh reviewers see same contradiction.\"}\n    action_items:\n      - {round: 8, action: \"See R8-N2\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Statistical power: key comparisons still partially single-seed\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 8\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Table 2 improved: 30% KL global 3-seed, 50% KL MMLU 3-seed, BCE 3-seed. But 30% KL uniform PPL still single seed, 40% all single seed.\"}\n      - {round: 8, reviewers: [1, 2], note: \"R1-N2 notes 40% single seed. R1-W2 notes 30% BCE missing entirely.\"}\n    action_items:\n      - {round: 8, action: \"See R8-N3, R8-W3\", assigned_to: \"\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # Resolved issues from prior rounds (compact, not re-raised in R8)\n  - id: \"R2-N1\"\n    summary: \"Limitations section 格式不合规\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Fixed in Round 1\"\n    resolution_round: 1\n\n  - id: \"R6-N1\"\n    summary: \"'Eliminates compensation' claim — KL+compensation control experiment\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"KL+comp experiment done: 30% 2-seed + 50% identical metrics. Claim supported.\"\n    resolution_round: 7\n\n  - id: \"R3-C3\"\n    summary: \"No wall-clock speedup, efficiency framing\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    resolution: \"Reframed as understanding paper. Appendix + Limitations explicit.\"\n    resolution_round: 7"
  }
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-18T14:26:01.110371+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 13729}, \"error\": \"\"}"}

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

_source line 744 · 2026-05-18T14:27:58.574506+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 8 (Fresh Review)\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh review（两位 Reviewer 独立初审 + 交叉分享，1 轮收敛）\n\n---\n\n## Summary\n\n本文研究用 forward KL 蒸馏替代 per-neuron BCE 训练 SwiGLU LLM 的激活稀疏性预测器。核心论点：BCE 梯度对每个 neuron 独立（Eq. 9-10），而 KL 梯度通过下游层 Jacobian 耦合所有 neuron（Eq. 11），更适合 TEAL 的 global top-k 推理分配。在 LLaMA-3.1-8B 上，轻量预测器（75.9M 参数，<1% base）在 30-70% 稀疏度下 PPL 优于 TEAL 18-82%，使补偿网络（+67.2M 参数）冗余。跨架构验证覆盖 Mistral-7B 和 Qwen-2.5-14B。论文还分析了三个 allocation-dependent 的 operating regions。\n\n---\n\n## Strengths\n\n**S1.** 梯度结构分析清晰有力（§3.6）：BCE gradient 仅依赖 neuron j，KL gradient 通过 factor (b) 耦合所有 neuron。简洁且有启发性。\n\n**S2.** F1-PPL 反向解耦是有说服力的实证发现：BCE 在 oracle F1 上领先 +7pp 却 PPL 差 139%（Table 3），说明 per-neuron accuracy 是错误的代理指标。\n\n**S3.** 诚实报告负面结果：14B MMLU gap（-8.1pp）、无 wall-clock speedup、30% global allocation seed 不稳定性（σ=9.5pp）均如实报告。\n\n**S4.** 消融设计较完整（Table 3）：覆盖 divergence direction、relaxation method、loss isolation、compensation redundancy。\n\n**S5.** 跨架构 PPL 优势一致（Table 6）：LLaMA-8B、Mistral-7B、Qwen-14B 三架构 30-70% 稀疏度优势比 1.22-5.59×。\n\n**S6.** 写作质量高：结构紧凑，数学符号一致，表格信息密度高，自我定位准确（\"primarily empirical\"）。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. Coupling vs oracle quality confound 未隔离** [R1-N1 + R2-W5, 交叉全 AGREE]\n- BCE 使用 magnitude-based oracle masks，KL 直接优化输出分布——gradient coupling 和 optimization target 两个变量同时变化。\n- 论文在 §4.3 自行承认 \"an ablation using KL-derived masks as BCE targets would isolate the effect\" 但未执行。\n- Oracle F1 分析不能区分是 coupling 还是 target quality 的贡献。BCE isolation ablation（BCE+Gumbel+Penalty = 38.02 vs vanilla BCE 27.97）反而说明 Gumbel+Penalty 框架与 BCE 不兼容，非有效隔离。\n- 这是 contribution 1 和 2 的根基。如果改善主要来自 target quality，核心叙事需重构。\n- **所需修改**: 执行 KL-derived masks as BCE targets 消融。\n\n**C2. 14B MMLU 反转与核心叙事矛盾** [R1-N3 + R2-N2, 交叉全 AGREE]\n- Qwen-2.5-14B 30%: KL PPL 7.62（最优）但 MMLU 63.72 vs TEAL 71.83（-8.1pp），GSM8K 48.82 vs BCE 53.07（-4.3pp）。Uniform 仅恢复 +0.8pp。\n- 核心叙事 \"output-distribution preservation beats per-neuron classification\" 在 14B downstream 上被反驳。\n- §4.6 \"knowledge density\" 解释是未验证推测。\n- Abstract \"confirms the PPL advantage across 7-14B\" 是 selective reporting——PPL 确认但 downstream 反转。\n- **所需修改**: (1) Abstract/Intro 将 scope 限定为 7-8B，14B 作为 limitation 而非 confirmation；(2) 14B 补充 per-layer retention 分析和更多稀疏度点。\n\n**C3. Three Operating Regions 证据不足** [R1-N2, R2 AGREE with nuance]\n- 每个 regime 仅一个数据点（30%/40%/50%），40% 为单 seed。\n- 30% global MMLU σ=9.5pp，40% 的 global-uniform 差异 7.4pp 可能在 seed variance 内。\n- 边界（35%? 45%?）完全未知。论文承认需 denser sampling（L151）但 framing 仍为确定性 \"three operating regions\"。\n- **所需修改**: 补充 25%/35%/45% 至少 2-seed 实验，或将 framing 弱化为 \"non-monotonic allocation preference observed at sampled sparsity levels\"。\n\n**C4. `\\enlargethispage{10\\baselineskip}` 格式违规** [R2-N3 critical + R1-W1 high warning]\n- experiments.tex L253 人为扩展第 8 页约 10 行。第 8 页内容密度远超其他页（Tables 5-7、regime 分析、SPON、cross-arch、14B、latency、Conclusion）。\n- ACL 模板禁止修改 margins/layout。R2 认为有 desk reject 风险，R1 认为更可能要求修改。两人一致要求移除。\n- **所需修改**: 移除 `\\enlargethispage`，将 SPON 详细分析或部分 Table 移至 appendix。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. 方法论新颖性有限** [R2-N1 critical, R1 AGREE with nuance]\n- Forward KL、Gumbel-Sigmoid、adaptive penalty 均为成熟技术。MaskLLM 已将 frozen weights + learnable masks + KL + Gumbel 用于 LLM sparsity。\n- R1 指出 MaskLLM 是 static N:M weight sparsity，与本文 dynamic per-token activation sparsity 是不同问题，技术栈重叠是表面层面的。\n- 共识：方法论创新不足以支撑 Main Conference；作为 empirical contribution 适合 Findings。\n\n**W2. 50% downstream collapse 与 Abstract framing 不一致** [R2-W1, R1 AGREE]\n- Abstract 突出 \"PPL advantage widens to 49%\" 但 50% MMLU ≈ 28%（≈random）、GSM8K <2.2%。\n- 后半句 hedge 不足。读者首先记住 \"49% advantage\"。\n\n**W3. BCE 30% baseline 缺失** [R1-W2, R2 AGREE]\n- 30% 是 recommended operating point，但 Table 2 无 BCE 30% 行。且 BCE 和 KL 的 allocation protocol 不同（FastForward compensation + no TEAL vs TEAL allocation）。\n\n**W4. 训练/评估域重叠** [R1-W3 + R2-W2, 全 AGREE]\n- WikiText-103 训练 → WikiText-2 评估（同族）。C4 OOD 在 30% 退化 1.74× vs WikiText-2 1.47×。C4 30% 仅 2-seed，无 downstream。\n\n**W5. SNR 分析覆盖不足** [R1-W4, R2 AGREE]\n- SNR 仅测到 step 300（训练 1000 步），但 PPL 在 step 800+ 才收敛。Step 300 称 \"convergence\" 不准确。Non-monotonic trajectory 可能在 300 步后再次反转。Bootstrap 参数未报告。\n\n**W6. 无实际推理加速** [R1-W6 + R2-W4, 全 AGREE]\n- Pipeline +6.4% overhead，unstructured masks 无硬件加速。Limitations 讨论了但 Introduction 应更早 set expectations。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 在交叉分享后达成一致 [AGREE]：\n1. Coupling vs oracle quality confound 是核心 claim 的关键缺陷（C1）\n2. 14B MMLU 反转与 output-preservation 叙事矛盾（C2）\n3. 格式操纵需移除（C4）\n4. 无实际推理加速（W6）\n5. 训练/评估域重叠（W4）\n6. 论文作为 empirical contribution 适合 Findings 而非 Main（W1）\n\n## Reviewer Divergence\n\n1. **格式操纵严重性**: R2 评为 Critical（desk reject 风险），R1 评为 high-priority Warning（AC 更可能要求修改）。→ 本报告采纳 Critical，因 ARR desk reject checklist 明确列出 margin 修改。\n2. **引用数量**: R2 认为 39 篇偏少，R1 REBUT 认为对聚焦论文足够。→ 不列为 issue。\n3. **Penalty controller 28.5% 偏差**: R1 列为 Warning（unfair 1.5% sparsity 优势），R2 partial REBUT（interpolation 论证合理，<0.3 PPL 影响）。→ 降为 Info。\n\n---\n\n## Questions for Authors\n\n1. 能否提供 KL-derived masks 作为 BCE targets 的消融？这是隔离 gradient coupling vs target quality 的关键实验。\n2. 14B per-layer retention 分布是否与 8B 有质的不同？Late-layer starvation pattern 是否在 14B 上更严重？\n3. 论文承认 \"PPL is a poor proxy for reasoning\"，那为什么核心对比仍以 PPL 为主？是否考虑过以 downstream 为主要指标重新组织叙事？\n4. 40% regime 的 global-uniform MMLU 差异（7.4pp）在 multi-seed 下是否可复现？\n5. BCE 在 30% 稀疏度下使用 TEAL allocation 的 PPL 和 downstream 是多少？\n\n---\n\n## Missing References\n\n两位 Reviewer 在引用覆盖上有分歧（R2 认为偏少，R1 认为足够）。39 篇引用基本覆盖了关键方向。可考虑补充：\n- Expert Choice routing（MoE 方向与 activation sparsity 的交叉）\n- Griffin / gated linear unit variants 的稀疏性工作\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。项目 `external_review.paperreview_ai.enabled` 未启用。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 — Findings**（两位 Reviewer 一致）\n\n**置信度: 4/5**（两位 Reviewer 均熟悉 activation sparsity 和 KL distillation 方向）\n\n**理由**:\n8B 上的实证贡献扎实且有启发性——F1-PPL 反向解耦、compensation 冗余性验证、regime 分析定性观察——足以进入 Findings。但三个问题阻止进入 Main Conference：(1) 核心因果 claim（gradient coupling 解释性能差异）存在已知且可解的混淆变量；(2) 14B downstream 结果反转核心叙事（PPL 好但 MMLU -8pp），限制了 generalization claim；(3) 方法是成熟技术的工程组合，无方法论创新。格式违规（`\\enlargethispage`）需在提交前修复以避免 desk reject 风险。\n\n**EMNLP 2026 评分标准映射**:\n- 3.0 = Findings（可被 Findings 接收）\n- 论文的 empirical insights（KL > BCE for sparsity prediction、compensation redundancy、allocation-dependent behavior）对社区有参考价值，但 claim 的因果强度和 scale generalization 不足以支撑 Main。\n\n---\n\n## Detailed Comments\n\n### Abstract (abstract.tex)\n- 7 句包含 ~11 个数字，密度偏高。建议减至 3-4 个关键数字。\n- \"confirms the PPL advantage across 7-14B\" 是 selective reporting；downstream 在 14B 反转。\n- 50% \"PPL advantage widens to 49%\" 的强调与 downstream collapse 不匹配。\n\n### Introduction (introduction.tex)\n- 叙事线清晰：mismatch → gradient analysis → KL → results → contributions。\n- Contribution 1 \"Empirical observation and quantification\" 定位准确。\n- 缺少对推理加速的早期 expectation setting。\n\n### Method (method.tex)\n- §3.3 Gumbel-Sigmoid relaxation 使用合理。但 Appendix B.1 显示 fixed τ=0.5 略优于 default annealing（PPL 11.861 vs 11.963），与 annealing 动机（exploration→exploitation）矛盾。\n- §3.5 Adaptive penalty controller：footnote 诚实承认非 formal dual method。但 30% 处 λ 命中 cap、actual sparsity 28.5% 的影响应在正文注明。\n- §3.6 Gradient analysis 数学正确，但本质是 \"end-to-end gradient couples variables\" 这一公知原则在 sparsity prediction 场景的实例化，analytical novelty 有限。\n- Table 1 Taxonomy：在自定义坐标系中填充空白 cell，positioning 价值 > 独立贡献价值。\n\n### Experiments (experiments.tex)\n- Table 2 main results 在 multi-seed 覆盖上有进步（30% KL global 3-seed, 50% MMLU 3-seed, BCE 3-seed），但 30% KL uniform PPL（recommended config）仍为单 seed，40% 全部单 seed。\n- §4.3 Extended Training Analysis（原 iso-compute）：wall-clock 匹配合理（~46 vs ~45 min），但未报告 BCE 2700 步是否已 converge（training loss plateau？）。\n- §4.5 Table 5 三区域分析：定性观察有价值但统计证据不足以支撑 \"three operating regions\" 的确定性表述。\n- §4.6 14B：最弱的一节。\"knowledge density\" 解释是 post-hoc 推测，无实证。建议大幅弱化 claim scope。\n- L253 `\\enlargethispage{10\\baselineskip}`：必须移除。\n\n### Conclusion (conclusion.tex)\n- 3 句，长度合适但内容聚焦 positive findings。\"scale-dependent tradeoff warranting further investigation\" 对 14B MMLU -8pp 的 hedge 不够。\n\n### Limitations (limitations.tex)\n- 覆盖了关键局限（PPL proxy、单目标 predictor、scale、OOD、wall-clock、coupling confound）。质量高于平均水平。\n\n### Format\n- `\\enlargethispage{10\\baselineskip}` 违规（C4）。\n- `\\label{sec:14b}` 在 `\\paragraph` 后，`\\ref{sec:14b}` 解析为父级 section 编号。\n- Table 2 caption \"50% uniform PPL 3-seed (11.92±0.07)\" 与 body 中 11.96 不一致。\n- Appendix C Figure 3 可能为 placeholder（lagrangian_dynamics.pdf）。",
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
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
    "report": "# 审稿报告 — Round 8 (Fresh Review)\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh review（两位 Reviewer 独立初审 + 交叉分享，1 轮收敛）\n\n---\n\n## Summary\n\n本文研究用 forward KL 蒸馏替代 per-neuron BCE 训练 SwiGLU LLM 的激活稀疏性预测器。核心论点：BCE 梯度对每个 neuron 独立（Eq. 9-10），而 KL 梯度通过下游层 Jacobian 耦合所有 neuron（Eq. 11），更适合 TEAL 的 global top-k 推理分配。在 LLaMA-3.1-8B 上，轻量预测器（75.9M 参数，<1% base）在 30-70% 稀疏度下 PPL 优于 TEAL 18-82%，使补偿网络（+67.2M 参数）冗余。跨架构验证覆盖 Mistral-7B 和 Qwen-2.5-14B。论文还分析了三个 allocation-dependent 的 operating regions。\n\n---\n\n## Strengths\n\n**S1.** 梯度结构分析清晰有力（§3.6）：BCE gradient 仅依赖 neuron j，KL gradient 通过 factor (b) 耦合所有 neuron。简洁且有启发性。\n\n**S2.** F1-PPL 反向解耦是有说服力的实证发现：BCE 在 oracle F1 上领先 +7pp 却 PPL 差 139%（Table 3），说明 per-neuron accuracy 是错误的代理指标。\n\n**S3.** 诚实报告负面结果：14B MMLU gap（-8.1pp）、无 wall-clock speedup、30% global allocation seed 不稳定性（σ=9.5pp）均如实报告。\n\n**S4.** 消融设计较完整（Table 3）：覆盖 divergence direction、relaxation method、loss isolation、compensation redundancy。\n\n**S5.** 跨架构 PPL 优势一致（Table 6）：LLaMA-8B、Mistral-7B、Qwen-14B 三架构 30-70% 稀疏度优势比 1.22-5.59×。\n\n**S6.** 写作质量高：结构紧凑，数学符号一致，表格信息密度高，自我定位准确（\"primarily empirical\"）。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. Coupling vs oracle quality confound 未隔离** [R1-N1 + R2-W5, 交叉全 AGREE]\n- BCE 使用 magnitude-based oracle masks，KL 直接优化输出分布——gradient coupling 和 optimization target 两个变量同时变化。\n- 论文在 §4.3 自行承认 \"an ablation using KL-derived masks as BCE targets would isolate the effect\" 但未执行。\n- Oracle F1 分析不能区分是 coupling 还是 target quality 的贡献。BCE isolation ablation（BCE+Gumbel+Penalty = 38.02 vs vanilla BCE 27.97）反而说明 Gumbel+Penalty 框架与 BCE 不兼容，非有效隔离。\n- 这是 contribution 1 和 2 的根基。如果改善主要来自 target quality，核心叙事需重构。\n- **所需修改**: 执行 KL-derived masks as BCE targets 消融。\n\n**C2. 14B MMLU 反转与核心叙事矛盾** [R1-N3 + R2-N2, 交叉全 AGREE]\n- Qwen-2.5-14B 30%: KL PPL 7.62（最优）但 MMLU 63.72 vs TEAL 71.83（-8.1pp），GSM8K 48.82 vs BCE 53.07（-4.3pp）。Uniform 仅恢复 +0.8pp。\n- 核心叙事 \"output-distribution preservation beats per-neuron classification\" 在 14B downstream 上被反驳。\n- §4.6 \"knowledge density\" 解释是未验证推测。\n- Abstract \"confirms the PPL advantage across 7-14B\" 是 selective reporting——PPL 确认但 downstream 反转。\n- **所需修改**: (1) Abstract/Intro 将 scope 限定为 7-8B，14B 作为 limitation 而非 confirmation；(2) 14B 补充 per-layer retention 分析和更多稀疏度点。\n\n**C3. Three Operating Regions 证据不足** [R1-N2, R2 AGREE with nuance]\n- 每个 regime 仅一个数据点（30%/40%/50%），40% 为单 seed。\n- 30% global MMLU σ=9.5pp，40% 的 global-uniform 差异 7.4pp 可能在 seed variance 内。\n- 边界（35%? 45%?）完全未知。论文承认需 denser sampling（L151）但 framing 仍为确定性 \"three operating regions\"。\n- **所需修改**: 补充 25%/35%/45% 至少 2-seed 实验，或将 framing 弱化为 \"non-monotonic allocation preference observed at sampled sparsity levels\"。\n\n**C4. `\\enlargethispage{10\\baselineskip}` 格式违规** [R2-N3 critical + R1-W1 high warning]\n- experiments.tex L253 人为扩展第 8 页约 10 行。第 8 页内容密度远超其他页（Tables 5-7、regime 分析、SPON、cross-arch、14B、latency、Conclusion）。\n- ACL 模板禁止修改 margins/layout。R2 认为有 desk reject 风险，R1 认为更可能要求修改。两人一致要求移除。\n- **所需修改**: 移除 `\\enlargethispage`，将 SPON 详细分析或部分 Table 移至 appendix。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. 方法论新颖性有限** [R2-N1 critical, R1 AGREE with nuance]\n- Forward KL、Gumbel-Sigmoid、adaptive penalty 均为成熟技术。MaskLLM 已将 frozen weights + learnable masks + KL + Gumbel 用于 LLM sparsity。\n- R1 指出 MaskLLM 是 static N:M weight sparsity，与本文 dynamic per-token activation sparsity 是不同问题，技术栈重叠是表面层面的。\n- 共识：方法论创新不足以支撑 Main Conference；作为 empirical contribution 适合 Findings。\n\n**W2. 50% downstream collapse 与 Abstract framing 不一致** [R2-W1, R1 AGREE]\n- Abstract 突出 \"PPL advantage widens to 49%\" 但 50% MMLU ≈ 28%（≈random）、GSM8K <2.2%。\n- 后半句 hedge 不足。读者首先记住 \"49% advantage\"。\n\n**W3. BCE 30% baseline 缺失** [R1-W2, R2 AGREE]\n- 30% 是 recommended operating point，但 Table 2 无 BCE 30% 行。且 BCE 和 KL 的 allocation protocol 不同（FastForward compensation + no TEAL vs TEAL allocation）。\n\n**W4. 训练/评估域重叠** [R1-W3 + R2-W2, 全 AGREE]\n- WikiText-103 训练 → WikiText-2 评估（同族）。C4 OOD 在 30% 退化 1.74× vs WikiText-2 1.47×。C4 30% 仅 2-seed，无 downstream。\n\n**W5. SNR 分析覆盖不足** [R1-W4, R2 AGREE]\n- SNR 仅测到 step 300（训练 1000 步），但 PPL 在 step 800+ 才收敛。Step 300 称 \"convergence\" 不准确。Non-monotonic trajectory 可能在 300 步后再次反转。Bootstrap 参数未报告。\n\n**W6. 无实际推理加速** [R1-W6 + R2-W4, 全 AGREE]\n- Pipeline +6.4% overhead，unstructured masks 无硬件加速。Limitations 讨论了但 Introduction 应更早 set expectations。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 在交叉分享后达成一致 [AGREE]：\n1. Coupling vs oracle quality confound 是核心 claim 的关键缺陷（C1）\n2. 14B MMLU 反转与 output-preservation 叙事矛盾（C2）\n3. 格式操纵需移除（C4）\n4. 无实际推理加速（W6）\n5. 训练/评估域重叠（W4）\n6. 论文作为 empirical contribution 适合 Findings 而非 Main（W1）\n\n## Reviewer Divergence\n\n1. **格式操纵严重性**: R2 评为 Critical（desk reject 风险），R1 评为 high-priority Warning（AC 更可能要求修改）。→ 本报告采纳 Critical，因 ARR desk reject checklist 明确列出 margin 修改。\n2. **引用数量**: R2 认为 39 篇偏少，R1 REBUT 认为对聚焦论文足够。→ 不列为 issue。\n3. **Penalty controller 28.5% 偏差**: R1 列为 Warning（unfair 1.5% sparsity 优势），R2 partial REBUT（interpolation 论证合理，<0.3 PPL 影响）。→ 降为 Info。\n\n---\n\n## Questions for Authors\n\n1. 能否提供 KL-derived masks 作为 BCE targets 的消融？这是隔离 gradient coupling vs target quality 的关键实验。\n2. 14B per-layer retention 分布是否与 8B 有质的不同？Late-layer starvation pattern 是否在 14B 上更严重？\n3. 论文承认 \"PPL is a poor proxy for reasoning\"，那为什么核心对比仍以 PPL 为主？是否考虑过以 downstream 为主要指标重新组织叙事？\n4. 40% regime 的 global-uniform MMLU 差异（7.4pp）在 multi-seed 下是否可复现？\n5. BCE 在 30% 稀疏度下使用 TEAL allocation 的 PPL 和 downstream 是多少？\n\n---\n\n## Missing References\n\n两位 Reviewer 在引用覆盖上有分歧（R2 认为偏少，R1 认为足够）。39 篇引用基本覆盖了关键方向。可考虑补充：\n- Expert Choice routing（MoE 方向与 activation sparsity 的交叉）\n- Griffin / gated linear unit variants 的稀疏性工作\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。项目 `external_review.paperreview_ai.enabled` 未启用。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 — Findings**（两位 Reviewer 一致）\n\n**置信度: 4/5**（两位 Reviewer 均熟悉 activation sparsity 和 KL distillation 方向）\n\n**理由**:\n8B 上的实证贡献扎实且有启发性——F1-PPL 反向解耦、compensation 冗余性验证、regime 分析定性观察——足以进入 Findings。但三个问题阻止进入 Main Conference：(1) 核心因果 claim（gradient coupling 解释性能差异）存在已知且可解的混淆变量；(2) 14B downstream 结果反转核心叙事（PPL 好但 MMLU -8pp），限制了 generalization claim；(3) 方法是成熟技术的工程组合，无方法论创新。格式违规（`\\enlargethispage`）需在提交前修复以避免 desk reject 风险。\n\n**EMNLP 2026 评分标准映射**:\n- 3.0 = Findings（可被 Findings 接收）\n- 论文的 empirical insights（KL > BCE for sparsity prediction、compensation redundancy、allocation-dependent behavior）对社区有参考价值，但 claim 的因果强度和 scale generalization 不足以支撑 Main。\n\n---\n\n## Detailed Comments\n\n### Abstract (abstract.tex)\n- 7 句包含 ~11 个数字，密度偏高。建议减至 3-4 个关键数字。\n- \"confirms the PPL advantage across 7-14B\" 是 selective reporting；downstream 在 14B 反转。\n- 50% \"PPL advantage widens to 49%\" 的强调与 downstream collapse 不匹配。\n\n### Introduction (introduction.tex)\n- 叙事线清晰：mismatch → gradient analysis → KL → results → contributions。\n- Contribution 1 \"Empirical observation and quantification\" 定位准确。\n- 缺少对推理加速的早期 expectation setting。\n\n### Method (method.tex)\n- §3.3 Gumbel-Sigmoid relaxation 使用合理。但 Appendix B.1 显示 fixed τ=0.5 略优于 default annealing（PPL 11.861 vs 11.963），与 annealing 动机（exploration→exploitation）矛盾。\n- §3.5 Adaptive penalty controller：footnote 诚实承认非 formal dual method。但 30% 处 λ 命中 cap、actual sparsity 28.5% 的影响应在正文注明。\n- §3.6 Gradient analysis 数学正确，但本质是 \"end-to-end gradient couples variables\" 这一公知原则在 sparsity prediction 场景的实例化，analytical novelty 有限。\n- Table 1 Taxonomy：在自定义坐标系中填充空白 cell，positioning 价值 > 独立贡献价值。\n\n### Experiments (experiments.tex)\n- Table 2 main results 在 multi-seed 覆盖上有进步（30% KL global 3-seed, 50% MMLU 3-seed, BCE 3-seed），但 30% KL uniform PPL（recommended config）仍为单 seed，40% 全部单 seed。\n- §4.3 Extended Training Analysis（原 iso-compute）：wall-clock 匹配合理（~46 vs ~45 min），但未报告 BCE 2700 步是否已 converge（training loss plateau？）。\n- §4.5 Table 5 三区域分析：定性观察有价值但统计证据不足以支撑 \"three operating regions\" 的确定性表述。\n- §4.6 14B：最弱的一节。\"knowledge density\" 解释是 post-hoc 推测，无实证。建议大幅弱化 claim scope。\n- L253 `\\enlargethispage{10\\baselineskip}`：必须移除。\n\n### Conclusion (conclusion.tex)\n- 3 句，长度合适但内容聚焦 positive findings。\"scale-dependent tradeoff warranting further investigation\" 对 14B MMLU -8pp 的 hedge 不够。\n\n### Limitations (limitations.tex)\n- 覆盖了关键局限（PPL proxy、单目标 predictor、scale、OOD、wall-clock、coupling confound）。质量高于平均水平。\n\n### Format\n- `\\enlargethispage{10\\baselineskip}` 违规（C4）。\n- `\\label{sec:14b}` 在 `\\paragraph` 后，`\\ref{sec:14b}` 解析为父级 section 编号。\n- Table 2 caption \"50% uniform PPL 3-seed (11.92±0.07)\" 与 body 中 11.96 不一致。\n- Appendix C Figure 3 可能为 placeholder（lagrangian_dynamics.pdf）。",
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-18T14:28:02.712217+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4137
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-18T14:28:15.133664+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6: 外部审稿线', 'status': 'completed', 'activeForm': '外部审稿未启用，跳过'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '两位 Reviewer 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '两位 Reviewer 完成交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '已收敛，无需第二轮'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6: 外部审稿线', 'status': 'completed', 'activeForm': '外部审稿未启用，跳过'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '两位 Reviewer 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '两位 Reviewer 完成交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '已收敛，无需第二轮'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-18T14:28:15.184284+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 748 · 2026-05-18T14:28:23.302853+00:00_

---

**审稿圆桌会议完成。**

报告已投递至 Research Director。

**结论：3.0 — Findings**（两位 Reviewer 一致）

**4 个 Critical 问题：**
1. **Coupling vs oracle quality confound** — 论文自己提出的 KL-derived masks 消融未执行，核心因果 claim 无法确立
2. **14B MMLU 反转** — PPL 最优但 MMLU -8.1pp，output-preservation 叙事在 scale up 时被反驳
3. **Three Operating Regions 证据不足** — 每个 regime 仅 1 个数据点，40% 单 seed
4. **`\enlargethispage{10\baselineskip}`** — 格式违规，有 desk reject 风险

**6 个 Should-Fix**：方法论新颖性有限、50% framing 不一致、BCE 30% 缺失、训练/评估域重叠、SNR 覆盖不足、无实际推理加速

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 57

## Round 57

2 recorded events


### User

_source line 749 · 2026-05-18T14:28:24.809719+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

与 R1 在 6/7 个 should-fix 和 3/3 个 must-fix 上达成共识。唯一分歧是 W5（penalty controller sparsity deviation）——我认为论文的 interpolation 论证合理，1.5% 偏差不足以解释 18% PPL 优势。两位 reviewer 的共识 critical issues：(1) causal confound 未隔离；(2) 14B 叙事矛盾；(3) 格式违规。共同支撑 3.0 Findings 评分。

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

_source line 750 · 2026-05-18T14:28:35.749466+00:00_

审稿圆桌会议已完成。

**最终结果：3.0 — Findings**（两位 Reviewer 一致，1 轮收敛）

审稿报告已投递给 Research Director。Issue Tracker 已同步更新（12 个新 issue：4 Critical + 6 Warning + 2 Info）。

**核心问题摘要：**
- **C1**: Coupling vs oracle quality confound 未隔离（需执行 KL-derived masks as BCE targets 消融）
- **C2**: 14B MMLU -8.1pp 反转核心叙事（需限定 scope 为 7-8B）
- **C3**: 三 regime 仅 3 个数据点，40% 单 seed（需补数据或弱化 framing）
- **C4**: `\enlargethispage{10\baselineskip}` 格式违规（需移除，desk reject 风险）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 58

## Round 58

64 recorded events


### User

_source line 751 · 2026-05-19T01:33:59.030756+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (ARR May cycle)
- 截止日期: 2026-05-25

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

_source line 752 · 2026-05-19T01:34:06.145204+00:00_

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

_source line 753 · 2026-05-19T01:34:06.196191+00:00_

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
…[truncated 2458 chars]

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

_source line 754 · 2026-05-19T01:34:09.871620+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch,WebFetch",
  "max_results": "4"
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
    "query": "select:director_get_project_overview,read_project_file,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-19T01:34:09.922372+00:00_



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

_source line 756 · 2026-05-19T01:34:18.164189+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_local_file",
  "max_results": "8"
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
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_local_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-19T01:34:18.164620+00:00_

No matching deferred tools found

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

_source line 758 · 2026-05-19T01:34:21.931611+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "8"
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-19T01:34:21.932109+00:00_



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

_source line 760 · 2026-05-19T01:34:27.460303+00:00_

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

_source line 761 · 2026-05-19T01:34:29.324185+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (214 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- c1_ablation_30pct_eval_34887: C1@30% eval on 34887 where checkpoint exists. TEAL uniform 30%, PPL+ARC+WinoGrande+MMLU+GSM8K. Compare vs KL 30% uniform (PPL=8.82, ARC=50.3%, Wino=72.1%, MMLU=44.8%, GSM8K=14.3%).（已分配 ? GPU:?，等待提交）\n- bce_isocompute_hellaswag_piqa_v2（准备中）\n- kl_sparsity40_s42_eval_teal_uniform: KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.（准备中）\n- c4_download（准备中）\n- kl50_s456_train_eval（准备中）\n- mag_preservation_reg（准备中）\n- longbench_dense_v5（准备中）\n- kl_lagrangian_v2（准备中）\n- kl_norm_v3_quicktest（准备中）\n- mvp_kl_norm_s456（准备中）\n- …另有 4 项\n\n## 近期结论\n- **c1_ablation_30pct_s42_eval_v2** (success): C1@30% eval on 34887 (checkpoint confirmed there). PPL already measured: 9.4463. Running full downstream (ARC, WinoGrande, MMLU, GSM8K) with TEAL uniform 30%. ← 基于 c1_ablation_30pct_s42_v2\n- **kl30_uniform_hellaswag_piqa** (failed): KL 30% uniform predictor should maintain near-dense performance on HellaSwag (10-shot) and PIQA (0-shot) at the recommended 30% operating point, consistent with graceful degradation observed on ARC/Winogrande
…[truncated 1797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1863
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-19T01:34:29.478371+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex",
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
    "pattern": "**/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-19T01:34:30.740371+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 1262
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-19T01:34:31.041549+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR May cycle site:aclweb.org"
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
    "query": "EMNLP 2026 call for papers submission guidelines ARR May cycle site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 765 · 2026-05-19T01:34:31.092236+00:00_

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

_source line 766 · 2026-05-19T01:34:38.003535+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR May cycle site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

I found search results related to EMNLP 2026 and ARR submission guidelines, but these results mostly show information about workshops and related events. The search did not return a direct link to the m
…[truncated 940 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6961
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-19T01:34:38.004472+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 6912
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-19T01:34:43.599304+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 submission deadline guidelines"
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
    "query": "ACL Rolling Review ARR May 2026 submission deadline guidelines"
  }
}
```

</details>

---


### Tool call

_source line 769 · 2026-05-19T01:34:44.106215+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission format page limit"
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
    "query": "EMNLP 2026 call for papers submission format page limit"
  }
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-19T01:34:44.459721+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR 2026 author guidelines page limit template anonymity"
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
    "query": "ARR 2026 author guidelines page limit template anonymity"
  }
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-19T01:34:50.146364+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 submission deadline guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) May 2026 submission deadline and guidelines:

## Submission Schedule

ARR switched from 8-week to 10-week review cycles starting in May 2025, which continues through May 2026. The submission deadline is always the 15th of the month, so the May 2026 ARR submission deadline would be **May 15, 2026**.

## Key Submission Guidelines

**Formatting and Templates:**

…[truncated 928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6547
}
```

</details>

---


### Tool result

_source line 772 · 2026-05-19T01:34:50.348145+00:00_

Web search results for query: "EMNLP 2026 call for papers submission format page limit"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here's information about EMNLP 2026 submission format and page limits:

**Main Conference Papers:**
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

**Industry Track Papers:**
Authors are invited to submit original, full-length (maximum of 6 pages) industry track papers that are not previously published, accepted to be published, or under consideration for publication in any other forum.

**Additional Requirements:**
- The mandatory Limitations section is required, placed after the conclusion.
- Manuscripts should be submitted electronically, in PDF format and formatted using the templates available here.
- Submissions that do not conform to the required styles, including paper size, margin width, and font size restrictions, will be desk-rejected.

All submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026.


REMIND
…[truncated 94 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6241
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-19T01:34:51.252300+00:00_

Web search results for query: "ARR 2026 author guidelines page limit template anonymity"

Links: [{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"CVPR 2026 Author Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"}]

Based on the search results, here's information about ARR 2026 author guidelines regarding page limits, templates, and anonymity:

## Page Limits

ARR papers should not exceed the page limit: 4 pages for short papers and 8 pages for long papers, excluding ethical considerations and limitations. Submissions must adhere to the formatting in the submission templates, which is available as an Overleaf template.

## Anonymity Policy

Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review. However, the new policy incentivizes anonymous submissions by special paper awards and priority in acceptance decisions for borderline papers.

Papers must not include authors' names and affiliations, and self-references that reveal the authors' identities must be a
…[truncated 379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6792
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-19T01:34:57.219160+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission requirements: page limits (long/short), template, anonymity rules, appendix rules, mandatory sections (limitations, ethics), deadline for ARR May cycle, commitment deadline. Include all formatting details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission requirements: page limits (long/short), template, anonymity rules, appendix rules, mandatory sections (limitations, ethics), deadline for ARR May cycle, commitment deadline. Include all formatting details."
  }
}
```

</details>

---


### Tool call

_source line 775 · 2026-05-19T01:34:58.525236+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract: submission deadline for May 2026 cycle, page limits (long/short), template requirements, anonymity policy, mandatory sections, desk reject criteria, supplementary material rules. Include all author-facing requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract: submission deadline for May 2026 cycle, page limits (long/short), template requirements, anonymity policy, mandatory sections, desk reject criteria, supplementary material rules. Include all author-facing requirements."
  }
}
```

</details>

---


### Tool result

_source line 776 · 2026-05-19T01:35:02.267660+00:00_

# EMNLP 2026 Submission Requirements Summary

## Page Limits
- **Long Papers:** 8 pages of content
- **Short Papers:** 4 pages of content
- **Final versions:** One additional page allowed (9 pages for long, 5 pages for short) to address reviewer feedback

## Key Deadlines
- **ARR May Cycle Submission:** May 25, 2026
- **Reviewer Registration:** May 27, 2026
- **EMNLP Commitment:** August 2, 2026
- All deadlines are 11:59PM UTC-12:00

## Anonymity & Review Process
The submission process maintains "double-blind" review standards. Authors cannot identify reviewers, and reviewers do not see authorship information. "Following the ACL and ARR policies, there is no anonymity period requirement."

## Mandatory Sections & Requirements
- **Limitations section** required (per ARR guidelines)
- **Ethics checklist** compliance mandatory
- **Two-way anonymized review** instructions must be followed
- All submissions must adhere to ACL Publication Ethics Policy

## Templates & Formatting
Submissions must follow "all of the ARR submission requirements" including official paper templates available through ARR's platform.

## Appendices & Supplementary Materials
Optional supplementary materials, appendices, software, and data submissions are permitted under ARR's guidelines.

## Author List Rules
During commitment phase, "it is not allowed to modify the author list" (no additions/deletions), though author order adjustments are permitted.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "elapsed_ms": 5048
}
```

</details>

---


### Tool result

_source line 777 · 2026-05-19T01:35:06.756597+00:00_

# ACL Rolling Review (ARR) – May 2026 Submission Requirements

## Submission Deadline
The May 2026 cycle submission deadline is **May 19, 2026**. Author registration must be completed within 48 hours of submission.

## Page Limits

**Long Papers:**
- "up to eight (8) pages of content"
- Unlimited space for limitations section and ethical considerations
- Unlimited reference pages

**Short Papers:**
- "up to four (4) pages of content"
- Unlimited space for limitations section and ethical considerations
- Unlimited reference pages

## Template & Formatting Requirements

Submissions must adhere to official ACL style guidelines. Authors should use the "official ACL style template, which is available here" from the ACL GitHub repository and follow formatting standards at acl-org.github.io/ACLPUB/formatting.html. Papers not conforming to required styles will be rejected without review.

## Anonymity Policy

Papers must be fully anonymized for two-way review. This means:
- No author names or affiliations
- Avoid self-references like "We previously showed..."
- Use third-person citations: "Smith previously showed (Smith, 1991)..."
- Anonymize supplementary materials and repository links
- Avoid file-sharing services that track downloads (Dropbox prohibited)

Anonymity violations result in desk rejection.

## Mandatory Sections

**Limitations Section (Required):**
- Dedicated section titled "Limitations" 
- Placed before references, doesn't count toward page limit
- Papers lacking this section face desk rejection
- Should not introduce new methods or results

**Responsible NLP Checklist:**
Must be completed during submission. Incorrect or misleading information can trigger desk rejection.

## Desk Rejection Criteria

Papers are desk-rejected for:
- Format/anonymity violations
- Exceeding page limits
- Missing limitations section
- Dual submissions (simultaneous ARR + other venues)
- Incomplete or false responsible checklist entries
- Resubmissions lacking revision explanatio
…[truncated 509 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "elapsed_ms": 8231
}
```

</details>

---


### Tool call

_source line 778 · 2026-05-19T01:35:22.778281+00:00_

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

_source line 779 · 2026-05-19T01:35:23.385450+00:00_

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
  "elapsed_ms": 607
}
```

</details>

---


### Tool call

_source line 780 · 2026-05-19T01:35:23.791074+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "paper_framing.md",
  "max_chars": "6000"
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
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 781 · 2026-05-19T01:35:24.049559+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md\", \"content\": \"# Paper Framing — distill_sparse_swiglu\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\\n- Deadline: 2026-05-25 (ARR submission)\\n- Track: Efficient Methods for NLP\\n\\n## Core Claims\\n\\n1. **KL distillation discovers fundamentally different (and superior) neuron importance patterns that magnitude-based oracles miss**: The C1 causal ablation (D059) proves that KL's advantage comes **entirely** from target quality (which neurons to keep), with gradient coupling contributing ≈0 across **both PPL and all downstream tasks**. **Controlled eval (TEAL 50% uniform, matched protocol)**: BCE+KL-targets PPL = **11.9638**, KL predictor PPL = **11.9638** (exact match). **Downstream confirmation (full-spectrum)**: All 4 downstream tasks (ARC-c, WinoGrande, MMLU, GSM8K) also match within <1pp delta, confirming gradient coupling = 0 across PPL + reasoning + knowledge + math dimensions. Standard BCE (magnitude masks) PPL ≈ 22.51. Target quality alone accounts for KL's full advantage. *Additional evidence from training eval (Gumbel hard mask)*: BCE+KL-targets PPL 9.29 @60.9% ≈ KL 9.21 @60.6%, consistent with controlled eval. The 53% mask divergence between KL-derived and magnitude-based masks is the core empirical finding: KL discovers a qualitatively different neuron importance landscape. **Implication**: The gradient coupling analysis (§3.6) provides mathematical intuition for *why* KL can discover better targets (coupled gradients explore joint neuron interaction patterns), but the causal driver is the resulting mask quality, not the gradient pathway per se. This shifts the contribution from \\\"engineering a better loss\\\" to \\\"discovering that output-distribution distillation reveals hidden neuron importance structure.\\\" **Supporting evidence**: (a) Iso-compute ablation: BCE with 
…[truncated 4358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 258
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-19T01:35:24.201319+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review_issues.yaml",
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
    "pattern": "**/artifacts/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-19T01:35:24.252012+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml

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

_source line 784 · 2026-05-19T01:35:29.586736+00:00_

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

_source line 785 · 2026-05-19T01:35:29.938889+00:00_

1	We show that KL-trained sparsity predictors for SwiGLU LLMs discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%) at 50\% sparsity.
2	A causal ablation confirms that these mask patterns, not gradient coupling, drive quality across the full sparsity range: BCE trained on KL-derived targets reproduces KL quality at both 50\% (max $\Delta$=0.59pp, 2-seed) and 30\% (max $\Delta$=1.68pp), while magnitude-trained BCE achieves 28.13$\pm$0.20 at 50\%.
3	The resulting predictor ($<$1\% of base parameters), trained with forward KL and Gumbel-Sigmoid relaxation on LLaMA-3.1-8B, renders post-hoc compensation (+67.2M params) redundant at both 30\% and 50\% sparsity.
4	At 30\%, KL reduces PPL degradation 18\% over TEAL; uniform allocation provides $7.5\times$ smaller cross-seed downstream $\sigma$.
5	At 50\%, the PPL advantage widens to 49\% but downstream tasks collapse to near-random regardless of allocation.
6	Evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms the PPL advantage across 7--14B, though at 14B, MMLU falls 8pp below TEAL (63.7\% vs.\ 71.8\%), a scale-dependent gap not resolved by allocation strategy.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-19T01:35:29.939375+00:00_

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

_source line 787 · 2026-05-19T01:35:30.395649+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: TEAL's top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
9	This suggests KL should outperform BCE under global allocation.
10	The empirical picture, however, reveals something more fundamental: KL-trained predictors discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%), and a causal ablation confirms that these learned mask patterns, not gradient coupling, are the primary quality driver.
11	Under controlled 50\% evaluation, BCE trained on KL-derived targets exactly matches KL across perplexity and all downstream tasks (max $\Delta$=0.59pp, 2-seed), while magnitude-trained BCE achieves 28.13$\pm$0.20.
12	
13	We instantiate a lightweight predictor (75.9M params, $<$1\% of base) trained with forward KL and Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} on LLaMA-3.1-8B~\cite{grattafiori2024llama3}.
14	With uniform allocation, the predictor achieves PPL 11.92 at 50\% sparsity (3
…[truncated 1419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-19T01:35:30.396209+00:00_

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

_source line 789 · 2026-05-19T01:35:30.900211+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
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
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden sta
…[truncated 11208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-19T01:35:30.900849+00:00_

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

_source line 791 · 2026-05-19T01:35:31.353542+00:00_

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
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor} (DejaVu-style~\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distri
…[truncated 16917 chars]

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

_source line 792 · 2026-05-19T01:35:31.354248+00:00_

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

_source line 793 · 2026-05-19T01:35:31.908013+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
13	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
14	MaskLLM~\cite{fang2024maskllm} shares the principle of frozen weights + learnable masks + KL training, but the two methods differ in three fundamental ways.
15	First, \emph{sparsity type}: MaskLLM targets N:M semi-structured \emph{weight} sparsity (static 2:4 patterns), while we target \emph{activation} sparsity (dynamic per-token masks). Weight masks are fixed after training; our masks vary with each input token.
16	Second, \emph{mask generation}: MaskLLM
…[truncated 3704 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-19T01:35:31.908541+00:00_

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

_source line 795 · 2026-05-19T01:35:32.866807+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	\vspace{-4pt}
4	
5	KL distillation discovers neuron importance patterns that diverge 68\% from magnitude-based masks; a causal ablation confirms target quality, not gradient coupling, as the primary driver.
6	A predictor ($<$1\% of base) halves TEAL's perplexity across 7--14B, rendering compensation (+67.2M params) redundant; at 30\%, uniform allocation delivers $7.5\times$ smaller cross-seed $\sigma$.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 796 · 2026-05-19T01:35:32.867296+00:00_

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

_source line 797 · 2026-05-19T01:35:33.320356+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, suggesting 30\% as the best-quality sparsity level for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	The 30\% sparsity analysis is validated at 7--8B scale; at 14B, the MMLU gap persists regardless of allocation strategy (Appendix~\ref{app:14b}). Scaling to 70B remains untested.
6	Out-of-distribution evaluation on C4 (Appendix~\ref{app:ood}) shows the KL advantage transfers but with a wider gap: C4 PPL at 30\% is $1.74\times$ dense vs.\ $1.46\times$ on in-domain WikiText-2, indicating that the predictor partially overfits to training-domain activation patterns. Extending OOD evaluation to 70\% sparsity is left to future work.
7	The causal ablation (\S\ref{sec:mask_analysis}) confirms that mask target quality, not gradient coupling, is the primary driver of KL's advantage. However, the mechanism by which KL's coupled gradient discovers superior mask patterns during training remains incompletely characterized; future work could trace per-layer mask divergence trajectories across training to identify when and where the patterns diverge.
8	At 30\% sparsity, global allocation exhibits 9.5pp cross-seed MMLU standard deviation (3-seed); allocation strategy interacts with predictor initialization in task-specific ways. This variance is MMLU-specific, as ARC, WinoGrande, and GSM8K show stable performance across seeds under both allocation strategies.
9	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on 
…[truncated 253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-19T01:35:33.321337+00:00_

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

_source line 799 · 2026-05-19T01:35:33.774533+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--8B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 is released under the Llama 3.1 Community License; Mistral-7B under Apache 2.0. WikiText a
…[truncated 1840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-19T01:35:33.875502+00:00_

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

_source line 801 · 2026-05-19T01:35:34.028329+00:00_

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
…[truncated 19203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-19T01:35:34.028765+00:00_

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

_source line 803 · 2026-05-19T01:35:34.081518+00:00_

1	issues:
2	  # === Round 8 (fresh review) findings ===
3	
4	  - id: "R8-N1"
5	    summary: "Coupling vs oracle quality confound: KL-derived masks as BCE targets ablation missing"
6	    category: method
7	    severity: critical
8	    status: resolved
9	    first_raised_round: 8
10	    last_seen_round: 8
11	    mentions:
12	      - {round: 8, reviewers: [1, 2], note: "R1-N1 raise critical, R2-W5 raise should-fix then upgraded to critical in cross-response. Full consensus."}
13	    action_items:
14	      - {round: 8, action: "Decision: NOT running ablation. Risk asymmetric (may undermine C1 if target quality is driver). Findings-level does not require causal isolation. Mitigation: weaken §3.6 analytical language to 'suggestive analysis'.", assigned_to: "paper_agent", status: done}
15	      - {round: 8, action: "C1 causal ablation executed (D059): BCE trained on KL-derived oracle masks achieves PPL 9.29 @60.9% sparsity vs KL 9.21 @60.6%. Confirms target quality is main driver, not gradient coupling. 53% mask divergence from magnitude oracles.", assigned_to: "main_agent", status: done}
16	      - {round: 8, action: "D061: Full-spectrum confirmation. Under controlled eval (TEAL 50% uniform), PPL 11.9638=11.9638 exact match + all 4 downstream tasks <1pp delta. Gradient coupling = 0 across all dimensions.", assigned_to: "main_agent", status: done}
17	    resolution: "RESOLVED by C1 ablation (D059/D061). Full-spectrum: PPL exact match (11.9638=11.9638) + ARC-c/WG/MMLU/GSM8K all <1pp delta. Target quality is sole driver. Paper reframed (commits 6abafc3, b66e8c3, 13418e6, 406f40a)."
18	    resolution_round: 8
19	
20	  - id: "R8-N2"
21	    summary: "14B MMLU reversal: KL PPL best (7.62) but MMLU -8.1pp vs TEAL, contradicts output-preservation narrative"
22	    category: experiment
23	    severity: critical
24	    status: in_progress
25	    first_raised_round: 8
26	    last_seen_round: 8
27	    mentions:
28	      - {round: 8, reviewers: [1, 2], note: "R1-N3 + R2-N2, full AGREE.
…[truncated 13720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 804 · 2026-05-19T01:36:05.585183+00:00_

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

_source line 805 · 2026-05-19T01:36:06.891500+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (214 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- c1_ablation_30pct_eval_34887: C1@30% eval on 34887 where checkpoint exists. TEAL uniform 30%, PPL+ARC+WinoGrande+MMLU+GSM8K. Compare vs KL 30% uniform (PPL=8.82, ARC=50.3%, Wino=72.1%, MMLU=44.8%, GSM8K=14.3%).（已分配 ? GPU:?，等待提交）\n- bce_isocompute_hellaswag_piqa_v2（准备中）\n- kl_sparsity40_s42_eval_teal_uniform: KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.（准备中）\n- c4_download（准备中）\n- kl50_s456_train_eval（准备中）\n- mag_preservation_reg（准备中）\n- longbench_dense_v5（准备中）\n- kl_lagrangian_v2（准备中）\n- kl_norm_v3_quicktest（准备中）\n- mvp_kl_norm_s456（准备中）\n- …另有 4 项\n\n## 近期结论\n- **c1_ablation_30pct_s42_eval_v2** (success): C1@30% eval on 34887 (checkpoint confirmed there). PPL already measured: 9.4463. Running full downstream (ARC, WinoGrande, MMLU, GSM8K) with TEAL uniform 30%. ← 基于 c1_ablation_30pct_s42_v2\n- **kl30_uniform_hellaswag_piqa** (failed): KL 30% uniform predictor should maintain near-dense performance on HellaSwag (10-shot) and PIQA (0-shot) at the recommended 30% operating point, consistent with graceful degradation observed on ARC/Winogrande
…[truncated 1797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool call

_source line 806 · 2026-05-19T01:36:07.495432+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-19T01:36:07.799845+00:00_

&lt;persisted-output>
Output too large (30KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-director-e331551e/44e48a40-c07d-4f86-9496-b69e9d1feac6/tool-results/toolu_01FetVhJ5M9B7SJpHXyNvZ4A.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_8.md:132:未配置。项目 `external_review.paperreview_ai.enabled` 未启用。
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_5.md:186:外部审稿：未配置（项目未启用 paperreview.ai）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md:188:外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未启用）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_1.md:170:外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未启用）。
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:152:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:152:`director_get_project_o
…[truncated 253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 304
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-19T01:36:07.801862+00:00_

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

_source line 809 · 2026-05-19T01:36:07.903517+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 17761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-19T01:37:01.024270+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## 投稿信息\n- **论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n- **Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **截止**: 2026-05-25\n- **格式要求**: ACL 模板, Long paper (8 页正文, unlimited references/limitations/ethics), double-blind\n- **论文路径**: `projects/distill_sparse_swiglu/paper/main.tex` (含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex)\n\n## 你的审查侧重\n\n### 1. 方法正确性\n- KL divergence objective (Eq. 4-5) 的数学推导是否正确？Forward KL 的选择是否有充分理由？\n- Gumbel-Sigmoid relaxation (Eq. 3) 的应用是否标准？与 Gumbel-Softmax/Concrete distribution 的关系是否正确？\n- Adaptive penalty controller (Eq. 6-7) 是否有理论保证？与 augmented Lagrangian 的区别是否准确？\n- §3.6 gradient analysis: BCE vs KL 的梯度结构对比是否正确？\"downstream Jacobian\" 的论述是否准确？\n\n### 2. 实验设计严谨性\n- **Causal ablation (C1, Table 3)**: BCE trained on KL-derived targets 的设计是否能真正 disentangle target quality vs gradient coupling？有无混淆变量？2-seed 统计效力是否足够？\n- **Baseline 公平性**: BCE baseline 训练 2700 steps vs KL 1000 steps (iso-compute claim), 是否真正公平？\"approximately equal wall-clock time\" 是否可信？\n- **Main results (Table 1)**: 30% 和 50% 的 BCE baseline 设置不同（30% 用 TEAL global, 50% 用 compensation 无 TEAL），是否 confounded？\n- **Statistical power**: 哪些数字是 3-seed，哪些是单 seed？Table 1 的 annotation 是否清晰？\n- **Cross-architecture (Mistral, Qwen-14B)**: 只报 PPL + 部分 downstream，实验是否充分？14B MMLU reversal 的讨论是否足够？\n\n### 3. Ablation 完整性\n- Table 4 ablation 是否覆盖所有关键 design choices？\n- 缺失的 ablation: 不同训练数据？不同 predictor 架构？不同 allocation 策略与 loss 的交互？\n- SPON 贡献只有 2.4%，是否应该从 method 中移除？\n\n### 4. 数值一致性\n- 检查 Table 1-4 数字是否内部一致（cross-reference between tables）\n- Abstract/Intro 中引用的数字是否与 tables 匹配\n- Appendix 数据与正文数据是否一致\n\n### 5. 评分标准 (EMNLP 2026 ARR)\n5 = Consider for Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n请按 **Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Overall Assessment (含评分和置信度)** 格式输出。Weaknesses 部分需要详细、具体、引用论文中的具体 Section/Table/Figure，不要含糊。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu",
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
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## 投稿信息\n- **论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n- **Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **截止**: 2026-05-25\n- **格式要求**: ACL 模板, Long paper (8 页正文, unlimited references/limitations/ethics), double-blind\n- **论文路径**: `projects/distill_sparse_swiglu/paper/main.tex` (含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex)\n\n## 你的审查侧重\n\n### 1. 方法正确性\n- KL divergence objective (Eq. 4-5) 的数学推导是否正确？Forward KL 的选择是否有充分理由？\n- Gumbel-Sigmoid relaxation (Eq. 3) 的应用是否标准？与 Gumbel-Softmax/Concrete distribution 的关系是否正确？\n- Adaptive penalty controller (Eq. 6-7) 是否有理论保证？与 augmented Lagrangian 的区别是否准确？\n- §3.6 gradient analysis: BCE vs KL 的梯度结构对比是否正确？\"downstream Jacobian\" 的论述是否准确？\n\n### 2. 实验设计严谨性\n- **Causal ablation (C1, Table 3)**: BCE trained on KL-derived targets 的设计是否能真正 disentangle target quality vs gradient coupling？有无混淆变量？2-seed 统计效力是否足够？\n- **Baseline 公平性**: BCE baseline 训练 2700 steps vs KL 1000 steps (iso-compute claim), 是否真正公平？\"approximately equal wall-clock time\" 是否可信？\n- **Main results (Table 1)**: 30% 和 50% 的 BCE baseline 设置不同（30% 用 TEAL global, 50% 用 compensation 无 TEAL），是否 confounded？\n- **Statistical power**: 哪些数字是 3-seed，哪些是单 seed？Table 1 的 annotation 是否清晰？\n- **Cross-architecture (Mistral, Qwen-14B)**: 只报 PPL + 部分 downstream，实验是否充分？14B MMLU reversal 的讨论是否足够？\n\n### 3. Ablation 完整性\n- Table 4 ablation 是否覆盖所有关键 design choices？\n- 缺失的 ablation: 不同训练数据？不同 predictor 架构？不同 allocation 策略与 loss 的交互？\n- SPON 贡献只有 2.4%，是否应该从 method 中移除？\n\n### 4. 数值一致性\n- 检查 Table 1-4 数字是否内部一致（cross-reference between tables）\n- Abstract/Intro 中引用的数字是否与 tables 匹配\n- Appendix 数据与正文数据是否一致\n\n### 5. 评分标准 (EMNLP 2026 ARR)\n5 = Consider for Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n请按 **Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Overall Assessment (含评分和置信度)** 格式输出。Weaknesses 部分需要详细、具体、引用论文中的具体 Section/Table/Figure，不要含糊。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-19T01:37:30.105212+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29080
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-19T01:37:30.257272+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 格式合规**审查。\n\n## 投稿信息\n- **论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n- **Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **截止**: 2026-05-25\n- **格式要求**: ACL 模板, Long paper (8 页正文, unlimited references/limitations/ethics), double-blind, Limitations section mandatory (不计入 8 页)\n- **论文路径**: `projects/distill_sparse_swiglu/paper/main.tex` (含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex)\n- **References**: `references.bib`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 核心方法 = KL distillation + Gumbel-Sigmoid + predictor for activation sparsity。每个组件都是已有技术 (KL distillation from Hinton et al., Gumbel from Jang et al., predictor from DejaVu)。**组合的新颖性是否足够 EMNLP Main？**\n- **与 MaskLLM (Fang et al., NeurIPS 2024) 的区别**: 论文声称区别在 sparsity type (weight vs activation)、mask generation (learnable params vs predictor)、allocation (N:M vs global top-k)。这些区别是否构成足够的 novelty，还是 straightforward adaptation？\n- **C1 causal ablation finding**: \"KL discovers mask patterns diverging 68% from magnitude\" — 这是否算新的 empirical insight？\n- **Taxonomy (Table 2, §3.7)**: \"Per-token × Coupled\" 空白格被填充。taxonomy 本身是否有足够的学术贡献？\n\n### 2. Related Work 完整性\n- 是否遗漏重要相关工作？特别检查:\n  - 2025-2026 年最新 activation sparsity 论文\n  - MoE-based sparse computation (beyond Switch Transformer)\n  - Attention sparsity methods (Polar Sparsity 已引用，还有？)\n  - Hardware-aware sparsity (N:M structured)\n- 引用密度是否符合 EMNLP 标准？\n- positioning 是否准确（是否过度 claim novelty）？\n\n### 3. Framing 一致性 (全文主线)\n- Abstract → Intro → Method → Experiments → Conclusion 是否讲同一个故事？\n- 核心 claim 是否一致？特别注意:\n  - \"gradient coupling\" 在 §3.6 被呈现为 \"suggestive analysis\"，但 Intro 和 Method 中是否语言一致？\n  - 14B MMLU reversal 在 Abstract/Intro 中如何处理？scope 是否诚实？\n  - \"no actual speedup\" 的 caveat 是否贯穿全文？\n  - 30% 作为 recommended operating point 但 50% 获得更多正文篇幅——重心是否合理？\n\n### 4. 写作质量 + AI 风格检查\n- 执行以下检查:\n  - em-dash (—) 和解释性 en-dash (–) 数量\n  - -ing 分词短语结尾 (\"..., demonstrating/highlighting/indicating...\")\n  - 过度分段（是否有太多 2-3 句的短段落）\n  - \"Furthermore/Moreover/Additionally\" 连续使用\n  - \"It is worth noting\"/\"Notably\" 等模式\n  - \"leverage\"/\"utilize\"/\"facilitate\"/\"delve\" 等 AI 用词\n  - 代词指代是否清晰 (this, that, it)\n\n### 5. 格式合规\n- **页数**: 正文是否 ≤ 8 页？检查是否有 `\\enlargethispage` 或修改 margin 的命令\n- **模板**: `\\usepackage[review]{acl}` 是否正确？\n- **匿名**: 是否有泄露作者身份的内容？检查 acknowledgments、GitHub links、自我引用\n- **Limitations section**: 是否在 references 之前？内容是否实质性？\n- **Ethics/Checklist**: 是否完整填写？\n- **图表**: caption 是否自包含？数字精度是否统一？最优加粗？\n\n### 6. 评分标准 (EMNLP 2026 ARR)\n5 = Consider for Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n请按 **Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Missing References → Questions → Overall Assessment (含评分和置信度)** 格式输出。Weaknesses 部分需要详细、具体、引用论文中的具体 Section/Table/Figure/行号，不要含糊。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu",
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
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 格式合规**审查。\n\n## 投稿信息\n- **论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n- **Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **截止**: 2026-05-25\n- **格式要求**: ACL 模板, Long paper (8 页正文, unlimited references/limitations/ethics), double-blind, Limitations section mandatory (不计入 8 页)\n- **论文路径**: `projects/distill_sparse_swiglu/paper/main.tex` (含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex)\n- **References**: `references.bib`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 核心方法 = KL distillation + Gumbel-Sigmoid + predictor for activation sparsity。每个组件都是已有技术 (KL distillation from Hinton et al., Gumbel from Jang et al., predictor from DejaVu)。**组合的新颖性是否足够 EMNLP Main？**\n- **与 MaskLLM (Fang et al., NeurIPS 2024) 的区别**: 论文声称区别在 sparsity type (weight vs activation)、mask generation (learnable params vs predictor)、allocation (N:M vs global top-k)。这些区别是否构成足够的 novelty，还是 straightforward adaptation？\n- **C1 causal ablation finding**: \"KL discovers mask patterns diverging 68% from magnitude\" — 这是否算新的 empirical insight？\n- **Taxonomy (Table 2, §3.7)**: \"Per-token × Coupled\" 空白格被填充。taxonomy 本身是否有足够的学术贡献？\n\n### 2. Related Work 完整性\n- 是否遗漏重要相关工作？特别检查:\n  - 2025-2026 年最新 activation sparsity 论文\n  - MoE-based sparse computation (beyond Switch Transformer)\n  - Attention sparsity methods (Polar Sparsity 已引用，还有？)\n  - Hardware-aware sparsity (N:M structured)\n- 引用密度是否符合 EMNLP 标准？\n- positioning 是否准确（是否过度 claim novelty）？\n\n### 3. Framing 一致性 (全文主线)\n- Abstract → Intro → Method → Experiments → Conclusion 是否讲同一个故事？\n- 核心 claim 是否一致？特别注意:\n  - \"gradient coupling\" 在 §3.6 被呈现为 \"suggestive analysis\"，但 Intro 和 Method 中是否语言一致？\n  - 14B MMLU reversal 在 Abstract/Intro 中如何处理？scope 是否诚实？\n  - \"no actual speedup\" 的 caveat 是否贯穿全文？\n  - 30% 作为 recommended operating point 但 50% 获得更多正文篇幅——重心是否合理？\n\n### 4. 写作质量 + AI 风格检查\n- 执行以下检查:\n  - em-dash (—) 和解释性 en-dash (–) 数量\n  - -ing 分词短语结尾 (\"..., demonstrating/highlighting/indicating...\")\n  - 过度分段（是否有太多 2-3 句的短段落）\n  - \"Furthermore/Moreover/Additionally\" 连续使用\n  - \"It is worth noting\"/\"Notably\" 等模式\n  - \"leverage\"/\"utilize\"/\"facilitate\"/\"delve\" 等 AI 用词\n  - 代词指代是否清晰 (this, that, it)\n\n### 5. 格式合规\n- **页数**: 正文是否 ≤ 8 页？检查是否有 `\\enlargethispage` 或修改 margin 的命令\n- **模板**: `\\usepackage[review]{acl}` 是否正确？\n- **匿名**: 是否有泄露作者身份的内容？检查 acknowledgments、GitHub links、自我引用\n- **Limitations section**: 是否在 references 之前？内容是否实质性？\n- **Ethics/Checklist**: 是否完整填写？\n- **图表**: caption 是否自包含？数字精度是否统一？最优加粗？\n\n### 6. 评分标准 (EMNLP 2026 ARR)\n5 = Consider for Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n请按 **Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Missing References → Questions → Overall Assessment (含评分和置信度)** 格式输出。Weaknesses 部分需要详细、具体、引用论文中的具体 Section/Table/Figure/行号，不要含糊。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-19T01:37:31.900191+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1642
}
```

</details>

---


### Assistant

_source line 814 · 2026-05-19T01:37:42.282594+00:00_

Round 9 初审任务已分配：
- **Reviewer 1** → 方法严谨性 + 实验设计
- **Reviewer 2** → 新颖性 + 完整性 + 格式合规

等待两位 Reviewer 独立审稿返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 59

## Round 59

2 recorded events


### User

_source line 815 · 2026-05-19T01:44:42.848328+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**审查侧重**: 新颖性 + 完整性 + 格式合规 + 写作质量 + Framing 一致性

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 扎实的实证工作，C1 causal ablation 是有价值的发现，但核心方法是已有技术的直接组合（KL + Gumbel + predictor），novelty 不足以支撑 Main Conference；50% sparsity 下 downstream 全面崩溃、无 wall-clock speedup、14B scale 失败等问题进一步削弱了实际价值。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 主要 claim 有实验支撑，但 C1 ablation（最核心 claim）仅 2-seed；50% sparsity 下 downstream collapse 削弱 PPL-based claim 的说服力；30% 实际 sparsity 是 28.5%（5% deviation），与 TEAL baseline 对比不严格公平 |
| Excitement | 2.5/5 | 每个组件（KL distill, Gumbel-Sigmoid, predictor）都是现有技术；与 MaskLLM 的区别主要是应用场景切换而非方法论创新；C1 ablation 的经验发现有价值但不够 exciting |
| Reproducibility | 4/5 | 超参数、训练细节、GPU 规格均详细报告；3-seed 评估（主要实验）；缺少代码发布承诺 |
| Overall Assessment | 3.0 | Findings 级别：实证贡献扎实但方法新颖性不够 Main |
| Confidence | 4/5 | 对 activation sparsity 和 KL distillation 领域比较熟悉 |

---

## 主要优势 (Strengths)

**S1. C1 Causal Ablation 设计精巧 (§4.4, Table 3)**
将 mask target quality 和 gradient coupling 解耦的实验设计值得肯定。BCE 在 KL-derived targets 上复现 KL 质量（50% 时 max Δ=0.59pp），而 magnitude-based BCE 为 28.13±0.20，这有力地证明了 "是 mask patterns 而非 gradient coupling 驱动质量"。这是论文最有说服力的贡献。

**S2. 实验设计系统、全面**
Ablation 覆盖了 divergence direction（Forward KL vs JSD vs Reverse KL）、relaxation（Gumbel vs STE）、loss isolation（BCE+Gumbel+Penalty）、compensation redundancy、超参数鲁棒性（$d_b$, $\tau$, training steps），形成了完整的 ablation 矩阵。Regime analysis（§4.6, Table 5）对 allocation 策略的非单调偏好提供了有价值的实践指导。

**S3. 诚实的 Scope 界定**
论文在 Introduction（L17）明确声明 "Our contribution is empirical" 和 "Wall-clock speedup requires sparse kernel support not addressed here"；14B MMLU gap 在 Abstract、Intro 和 Experiments 中均被报告；50% downstream collapse 被明确标注为 capacity-limited regime。这种诚实的叙事值得赞赏。

**S4. 跨架构验证**
在 Mistral-7B-v0.3 和 Qwen-2.5-14B 上验证（Appendix §K, §J），KL advantage ratio 跨架构一致（within 8% at ≤50%），增强了结论的普适性。

**S5. 写作质量整体较好**
无 em-dash/en-dash AI 痕迹。段落长度合理。术语首次出现时有定义。全文主线（mask pattern discovery → causal ablation → practical implications）连贯。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **新颖性不足以支撑 Main Conference**
- 具体位置：§3 (Method), Table 2 (§3.7)
- 问题：核心方法是三个已有技术的直接组合——(1) KL distillation (Hinton et al. 2015), (2) Gumbel-Sigmoid relaxation (Jang et al. 2017), (3) per-layer MLP predictor (DejaVu, Liu et al. 2023)。MaskLLM (Fang et al., NeurIPS 2024) 已经组合了 frozen weights + learnable masks + KL training + Gumbel relaxation。论文声称的三点区别（activation vs weight sparsity, predictor vs learnable params, global vs N:M）是 sparsity paradigm 的切换，而非方法论创新。
- Table 2 (§3.7) 的 taxonomy 是 2×3 格，填充一个 "Per-token × Coupled" 空白格，学术贡献有限——这不是从数据中发现的 taxonomy，而是为了 positioning 自己而构建的。
- 为什么影响接收：EMNLP Main Conference (Overall 4.0+) 通常要求方法论或经验发现的显著创新。本文的贡献主要是 "把已有的 KL distillation 范式应用到 activation sparsity predictor 上，发现效果好"。C1 ablation 是有价值的经验发现，但不够支撑 Main。
- 建议：如果补充理论分析（为什么 KL 的 mask patterns 在下游任务上优于 magnitude，而非仅仅展示 Jaccard divergence），或者展示实际 wall-clock speedup，novelty 评估会显著不同。目前更适合 Findings track。

**N2** [critical] **50% Sparsity 下 Downstream 全面崩溃，核心 PPL Claim 实际价值存疑**
- 具体位置：Table 1 (§4.2), §4.6 L218-219
- 问题：论文最强的数字是 "PPL 49% improvement at 50% sparsity"（11.79 vs 23.31），这在 Abstract 中突出呈现。但 Table 1 同时显示：MMLU 28.1±0.2%（接近 random 25%）、GSM8K 1.29%、ARC-c 32.85%（vs dense 58.28%）。PPL 的巨大改善完全无法反映到下游任务质量上。
- 论文在 §4.6 承认 "capacity-limited regime where no allocation strategy can recover"，但 Abstract 和 Introduction 仍然以 50% PPL 改善作为核心卖点。这构成了 framing 偏差：读者第一印象是 "方法在 50% sparsity 很强"，但实际可用范围仅限于 ≤30%。
- 为什么影响接收：如果方法的实际可用范围仅为 30%（PPL 8.81 vs TEAL 10.97, 18% improvement），这是一个更温和的 claim，对应的 excitement 也更低。
- 建议：将 framing 重心从 50% PPL 转向 30% 的 downstream-preserved quality；或者补充 30% 下的完整 downstream 评估（当前 Table 1 的 30% 下游数据不够完整——ARC-c 和 WG 仅有 3-seed 但 MMLU 高 variance 9.5pp）。

**N3** [critical] **无 Wall-Clock Speedup，反而增加 6.4% Overhead**
- 具体位置：§4.6 (L229-231), Appendix A (Table 6)
- 问题：论文动机是 "exploit contextual sparsity for efficient inference"，但 Table 6 显示方法实际增加 6.4% 推理延迟（126.78 vs 119.11 ms/forward）。所有 sparsity-based pruning 都使用 unstructured element-wise masks，PyTorch 无法加速。论文声称 "actual speedup requires sparse kernel integration" (Appendix A)，但没有任何 structured sparsity (N:M) 或 Triton kernel 实验。
- 这不仅仅是 "future work"——如果方法选择的 mask patterns 恰好不利于 structured sparsity 转换（KL masks 与 magnitude 有 68% divergence，而 N:M 通常基于 magnitude），那么 KL 的 PPL 优势可能在实际部署中完全消失。
- 为什么影响接收：一篇以 inference efficiency 为动机的论文必须提供至少初步的 speedup 证据，或者明确论证 mask patterns 与 hardware-friendly formats 的兼容性。
- 建议：至少补充 N:M 格式下 KL vs magnitude masks 的 PPL 对比，或 Triton block-sparse 的初步 benchmark。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **C1 Ablation 仅 2-seed 验证，作为最核心 claim 的统计力度不足**
- 具体位置：Table 3 (§4.4), caption "seed 42; 50% also validated with seed 123"
- 问题：C1 ablation 是论文最重要的 claim（mask target quality > gradient coupling），但 50% 仅有 seed 42 + seed 123 (2-seed)，30% 仅有 seed 42 (1-seed)。主实验用 3-seed。核心 claim 的统计验证反而弱于常规结果，这是不合理的。max Δ=0.59pp 在 2-seed 条件下的可靠性存疑。
- 建议：至少补充到 3-seed；理想情况下 5-seed 以增强说服力。

**W2** [warning] **30% Sparsity 实际为 28.5%（5% deviation），与 TEAL baseline 对比不严格**
- 具体位置：Appendix C (Table 8), L148
- 问题：Adaptive penalty controller 在 30% target 下 actual sparsity 是 28.5%（5% deviation），但 TEAL baseline 在精确 30% 下评估。论文在 Appendix C 辩称 "interpolated 28.5% TEAL PPL ≈ 10.7 vs 10.97 at exact 30%"，但这是作者自己的估算，不是严格对照实验。
- 在 70% target 下 deviation 是 1.7%，30% target 下反而最大（5%），这表明 controller 在低 sparsity 下不够精确。
- 建议：在 TEAL baseline 的 28.5% 实际 sparsity 点上重新评估，或改进 controller 使 deviation <2%。

**W3** [warning] **14B Scale 的 MMLU Gap 未被充分解释**
- 具体位置：Appendix J (Table 12), §4.6 L225
- 问题：Qwen-2.5-14B 上 KL 的 MMLU 为 63.7% vs TEAL 71.8%（-8.1pp），ARC-c KL 57.17 vs BCE 57.59，WG KL 72.06 vs TEAL 72.69。KL 在 PPL 上胜出（7.62 vs 8.73）但在几乎所有 downstream 上劣于 TEAL 或 BCE。这不仅仅是 "MMLU gap"——是全面的 downstream 劣势。
- 论文仅称 "a scale-dependent gap not resolved by allocation strategy"，但没有提供任何机制解释。如果 KL 的 mask patterns 在 14B 上系统性地损害 downstream，这是一个根本性的 scalability 问题。
- 建议：需要至少提出可检验的假设（例如：14B 的 FFN 维度/层数比例不同导致 global allocation 行为变化）。

**W4** [warning] **训练/评估数据同域，OOD 泛化存疑**
- 具体位置：§4.1, Appendix D (Table 9)
- 问题：训练在 WikiText-103，主要评估在 WikiText-2——这是同一个数据集的不同 split，不是真正的 domain shift。C4 OOD 评估（Appendix D）显示 30% PPL 从 in-domain 1.46× dense 扩大到 OOD 1.74× dense，说明存在显著的 domain overfitting。
- 论文未在 C4 上报告 downstream metrics——仅报告 PPL。如果 C4 PPL 16.03 对应的 downstream quality 更差（类似 50% 的 PPL-downstream 解耦现象），OOD 价值更低。
- 建议：补充 C4 上的 downstream metrics；或在 C4/OpenWebText 等不同域上训练 predictor 并报告对比。

**W5** [warning] **-ing 分词短语偏多（AI 写作痕迹）**
- 具体位置：全文多处
- 问题：grep 发现大量 -ing 分词短语用于句尾修饰：
  - "enabling the predictor to discover..." (experiments.tex L84)
  - "confirming OOD generalization" (appendix.tex L175)
  - "confirming that KL-trained predictions generalize..." (appendix.tex L176)
  - "rendering compensation redundant" (conclusion.tex L6)
  - "confirming moderate degradation" (appendix.tex L235)
  - "suggesting that output-distribution prediction may generalize" (related_work.tex L40)
  - "creating the inter-neuron dependencies that motivate coupled training" (related_work.tex L17)
  - "making uniform allocation preferable for stability" (introduction.tex L15)
  - "indicating that the predictor partially overfits" (limitations.tex L6)
  - 共约 15+ 处 "-ing clause" 句尾修饰
- 虽然不是 desk-reject 级别，但模式化的 -ing 短语结尾是 AI 辅助写作的典型痕迹。
- 建议：逐一改写为独立句或用其他句式替代。

---

## 小问题（不影响接收）

- **M1**: Float spacing 被手动压缩（main.tex L18-20: `\setlength{\textfloatsep}{8pt}`），conclusion 有 `\vspace{-4pt}`。虽然不违规，但暗示空间紧张。
- **M2**: Ethics 声明遗漏 Qwen-2.5-14B（ethics.tex L3 仅提 LLaMA-3.1-8B 和 Mistral-7B-v0.3）。
- **M3**: Table 1 caption 较长（38 words + 注解），建议精简。
- **M4**: "predictor-TEAL" 术语在 §4.1 L19 引入但后文很少使用，可以统一。
- **M5**: Reference 中 `de2024griffin` (Griffin) 未通过 OpenAlex 在线验证（可能索引滞后）；`loshchilov2019adamw` 年份 bib=2019 vs API=2017 有 mismatch。这些是 minor bib 问题，不影响内容。

---

## 可能遗漏的相关工作 (Missing References)

1. **SeerAttention** (2024, arXiv 2410.13276)：学习 LLM 内在 sparse attention pattern——与本文的 "learn sparsity pattern via distillation" 有方法论联系。
2. **Enabling Dynamic Sparsity in Quantized LLMs** (2025, arXiv 2511.04477)：quantization + activation sparsity 协同设计，是当前缺失的方向。
3. **Mixture of Neuron Experts** (2025, arXiv 2510.05781)：将 dense MLP 转换为 neuron-level MoE，与 D2DMoE 类似但更新。
4. **DeepSeek-V3 / DeepSeekMoE**：shared + routed expert 的 MoE routing 策略，与 TEAL 的 global allocation 有概念联系。Related Work 仅提 Switch Transformer 和 Expert Choice，对 2024-2025 MoE 进展覆盖不足。

---

## 提问 (Questions for Authors)

**Q1**: C1 ablation 中，BCE 在 KL-derived targets 上训练时，oracle masks 是从 KL predictor 的哪个 checkpoint 提取的？如果是最终 checkpoint，那 BCE 看到的是 KL 1000 步优化后的 "最优" targets——这是否构成信息不对等？

**Q2**: 50% downstream collapse 下，KL 的 MMLU (28.1%) 与 TEAL (28.32%) 差异在 noise range 内。如果 downstream 是最终目标，30% 是实际推荐的 operating point，为什么 Abstract 和 Introduction 以 50% PPL improvement (49%) 而非 30% downstream preservation 作为核心叙事？

**Q3**: 14B 实验中 BCE 的 MMLU (71.67%) 与 TEAL (71.83%) 几乎相同，但 KL 降到 63.72%。这是否暗示 KL 的 coupled training 在 14B 下产生了有害的 mask patterns（而非更好的 patterns）？

**Q4**: Appendix C 显示 30% target 的 actual sparsity 是 28.5%（$\lambda$ 达到 cap 5000）。如果将 $\lambda_{max}$ 提高到 10000 或更高，actual sparsity 能否更精确地达到 30%？这是否会改变 PPL 结果？

---

## Overall Assessment

**分数: 3.0 (Findings)**

这篇论文是一项认真、系统的实证研究。C1 causal ablation（§4.4）提供了 "mask target quality vs gradient coupling" 的有价值解耦证据，regime analysis（§4.6）对实践者有指导意义。写作质量整体不错，scope 界定诚实。

但有三个核心问题阻碍 Main Conference 接收：(1) 方法是 KL + Gumbel + predictor 的直接组合，MaskLLM 已在 weight sparsity 上做了几乎相同的组合，novelty 有限；(2) 50% sparsity 下 downstream 全面崩溃，实际可用范围仅 ≤30%，核心数字的实际价值被夸大；(3) 无 wall-clock speedup 证据，反而增加 6.4% overhead。

建议以 Findings 轨道投稿，或在补充 N:M structured sparsity 实验、扩展至更大 scale、提供理论分析后重新投稿 Main。

**Confidence: 4/5** — 对 activation sparsity 和 KL distillation 相关文献较为熟悉，仔细阅读了全文和附录。


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

_source line 816 · 2026-05-19T01:44:58.921449+00:00_

Reviewer 2 审稿意见已收到。评分 3.0 (Findings)，核心问题集中在方法新颖性不足 (N1)、50% downstream 崩溃 (N2)、无实际 speedup (N3)。

等待 Reviewer 1 (方法严谨性 + 实验设计) 返回后，进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 60

## Round 60

2 recorded events


### User

_source line 817 · 2026-05-19T01:45:01.551637+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论**: Overall 3.0 (Findings)

核心判断：

- **新颖性不足** (N1)：KL + Gumbel + predictor 三个组件均为已有技术，MaskLLM 已在 weight sparsity 上做了几乎相同的组合。C1 causal ablation 是有价值的经验发现，但不够支撑 Main。
- **50% downstream 崩溃** (N2)：最强数字 (49% PPL improvement) 对应的 downstream 接近 random，实际可用范围仅 ≤30%，Abstract/Intro framing 偏向 50% 构成叙事偏差。
- **无 wall-clock speedup** (N3)：反而增加 6.4% overhead，且未验证 KL masks 是否兼容 N:M structured sparsity。

主要优势：C1 ablation 实验设计精巧、ablation 矩阵系统全面、scope 界定诚实、写作整体干净。

5 个 Should-Fix (C1 仅 2-seed、30% actual sparsity deviation 5%、14B MMLU gap 无解释、同域训评、-ing 短语偏多) 和 5 个 Minor issues。

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

_source line 818 · 2026-05-19T01:45:07.523412+00:00_

收到 Reviewer 2 报告。等待 Reviewer 1 报告后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 61

## Round 61

6 recorded events


### User

_source line 819 · 2026-05-19T01:46:37.567518+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1: 方法严谨性 + 实验设计审查

**论文**: "Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"
**Venue**: EMNLP 2026 Main Conference (ARR May 2026)

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 论文提出了一个清晰的 KL 蒸馏框架用于 SwiGLU 稀疏预测，C1 因果消融提供了有价值的发现（mask pattern 比 gradient coupling 更重要），但实验设计存在多处混淆变量，实际可用范围窄（≤30%），且 14B 规模的 downstream 反转削弱了方法的泛化性。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 方法公式正确，但 C1 因果声明过度（2-seed），BCE baseline 在 30% 和 50% 使用不同 pipeline 引入混淆变量，adaptive penalty 公式与问题定义不一致 |
| Excitement | 3/5 | KL-trained masks 与 magnitude masks 的 68% 发散是有趣发现，但实际加速未实现，实用操作区间窄 |
| Reproducibility | 4/5 | 超参数完整，训练设置清晰，但部分关键实验只有单 seed |
| Confidence | 4/5 | 熟悉 activation sparsity、知识蒸馏、Gumbel relaxation 文献 |

---

## 主要优势

**S1. 清晰的核心发现**：KL-trained masks 与 magnitude-based masks 的 68% 发散（per-layer Jaccard 32%，§4.3，Figure 3）以及 C1 因果消融表明 mask target quality 是主要驱动力，这是一个非显而易见且有价值的 empirical finding。

**S2. 方法公式化简洁正确**：Gumbel-Sigmoid relaxation（Eq. 3）的数学形式是标准 Binary Concrete distribution 的正确应用；forward KL objective（Eq. 4）的推导无误；predictor 架构轻量（<1% base params）且不需要推理时 compensation network，简化了部署。

**S3. 全面的消融研究**：Table 4 系统地消融了 divergence 方向（forward KL > JSD +6.4% > reverse KL +8.6%）、relaxation 方法（Gumbel vs STE, 34.5% improvement）、compensation 冗余性、以及超参数鲁棒性（Appendix A-B），覆盖面较好。

**S4. 诚实报告负面结果**：50% downstream collapse（MMLU ≈ random，Table 1）、14B MMLU reversal（63.7% vs TEAL 71.8%，Table 7）、30% global MMLU 高方差（σ=9.5pp）——这些对方法的局限性提供了透明的刻画。

**S5. 写作组织清晰**：Taxonomy（Table 2）有效定位了方法的新颖性；gradient analysis（§3.6）在声称 "suggestive" 后正确指向因果验证；正文 8 页的信息密度较高。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] C1 因果消融的声明力度与统计效力不匹配

- **具体位置**：§4.3 (Table 3), Abstract line 2, Introduction line 10, Conclusion
- **问题**：
  - 论文多处使用 "causal ablation" 和 "proves that mask target quality...determines quality" 的措辞（Abstract: "A causal ablation confirms"; Introduction: "a causal ablation confirms"; Conclusion: "a causal ablation confirms target quality, not gradient coupling, as the primary driver"）。然而，C1 实验仅使用 2-seed 验证（seeds 42 和 123），Table 3 caption 明确写 "Seed 42; 50% also validated with seed 123"。对于一个 **因果** 声明（在标题级别的核心贡献中反复引用），2 个 seed 的统计效力严重不足。
  - 在 30% sparsity 条件下，C1 与 KL 之间存在不可忽略的 PPL 差距（9.45 vs 8.82 = +7.1%），论文将此归因于 "residual 2.5% mask disagreement"（§4.3 最后一段）。但如果 mask agreement 已达 97.5%，为何 PPL gap 仍为 7.1%？这暗示 gradient coupling 在低稀疏度可能仍然重要，与 "target quality, not gradient coupling, drives KL's advantage **across the full sparsity range**" 的声明矛盾。
  - C1 实验设计本身存在潜在混淆：KL predictor 在训练期间使用 soft Gumbel-Sigmoid masks（连续放松），而 C1 的 BCE predictor 使用 hard binary targets。因此 C1 不仅改变了 gradient coupling，也改变了训练时的 mask 特性（soft vs hard）。这意味着 C1 并未完全 disentangle 所声称的两个因素。
- **为什么影响接收**："因果消融证明 mask quality > gradient coupling" 是论文最核心的新颖贡献（Abstract 和 Introduction 的主要 claim），如果这个 claim 的证据不充分，整篇论文的贡献降级为 "KL 比 BCE 好" 这个较为 incremental 的发现。
- **建议修改方向**：(1) 增加到至少 5-seed 的 C1 验证并报告 confidence interval；(2) 将措辞从 "causal ablation proves" 降级为 "ablation suggests" 或 "provides evidence"；(3) 在 30% 条件下讨论 gradient coupling 可能的残余贡献，不要声称 "across the full sparsity range"；(4) 讨论 soft-vs-hard mask 训练差异作为 C1 设计的局限。

---

**N2** [critical] 14B 规模 downstream 反转削弱泛化声明

- **具体位置**：§4.5 (Cross-Architecture and Scale), Table 7 (Appendix H), Abstract line 6
- **问题**：
  - Qwen-2.5-14B 在 30% sparsity 下，KL 实现 PPL 优势（7.62 vs TEAL 8.73）但 MMLU 显著低于 TEAL（63.7 vs 71.8，差 8.1pp）和 BCE（63.7 vs 71.7）。Table 7 还显示 BCE 在 ARC-c（57.59）和 GSM8K（53.07）上优于 KL（57.17, 48.82）。
  - 这个结果直接质疑论文的核心叙事：如果 KL 发现的 "superior mask patterns" 在更大规模上导致更差的 downstream 性能，那么 PPL 优势的实际意义何在？论文在正文中仅用半句带过（"MMLU falls 8pp below TEAL...a scale-dependent gap not resolved by allocation strategy"），没有提供机制解释。
  - Uniform allocation 的 14B 结果（Table 7 下半部分）显示同样的趋势：KL MMLU 64.49 vs TEAL 66.34，进一步排除了 allocation strategy 作为解释。
  - Abstract 写 "confirms the PPL advantage across 7-14B" 但刻意轻描淡写了 downstream degradation，读者容易误读为 KL 在所有指标上都优于 TEAL。
- **为什么影响接收**：EMNLP 社区高度重视方法在更大规模上的泛化性。PPL 改善但 downstream 变差的 reversal pattern 暗示 KL 可能在优化一个与实际能力不一致的 proxy。如果方法只在 8B 有效而在 14B 反转，实用价值大幅降低。
- **建议修改方向**：(1) 在正文而非仅 Appendix 中充分讨论 14B reversal（至少一段）；(2) 分析哪些层的 mask divergence 在 14B 最大，是否与 MMLU degradation 相关；(3) 将 Abstract 改为明确表述 "PPL advantage generalizes but downstream performance reverses at 14B"；(4) 提供可能的机制假设（例如 KL 在 14B 的 mask pattern 是否过度偏离 magnitude ranking 导致某些 capability 层被错误剪裁）。

---

**N3** [critical] BCE baseline 在不同稀疏度使用不同实验管线，导致跨 sparsity 比较不可靠

- **具体位置**：Table 1 及其 footnotes, §4.2 (Extended Training Analysis)
- **问题**：
  - 30% BCE baseline（Table 1, $^\dagger$标注）：TEAL global allocation, **no compensation**, 2700 steps → PPL 11.25
  - 50% BCE baseline（Table 1, $^\ast$标注）：**DejaVu pipeline with compensation (+67.2M params)**, **no TEAL allocation**, 2700 steps → PPL 28.13±0.20
  - 这意味着两个 BCE baseline 使用了完全不同的推理管线（有/无 compensation，有/无 TEAL allocation）。论文的 Table 4 ablation 显示 "BCE + Compensation" PPL=25.44 vs "BCE (no compensation)" PPL=27.97，差距 2.53——说明 compensation 对 BCE 有显著影响。
  - 关键遗漏：**没有报告 50% BCE + TEAL global（无 compensation）的结果**。这才是与 50% KL global 最直接可比的 baseline。Table 4 的 "BCE (no compensation)" PPL=27.97 看起来用的也不是 TEAL allocation（没有标注）。
  - 如果 BCE 在 30% 用 TEAL global 得到 11.25，在 50% 也应该测 TEAL global（无 compensation）。现有设置使得 KL 的优势可能被 allocation strategy 的差异放大。
- **为什么影响接收**：Baseline 公平性是实验驱动论文的生命线。不同 pipeline 的 BCE baseline 使得 Table 1 的跨 sparsity 比较不可靠，读者无法判断 KL 的优势有多少来自 objective、多少来自 allocation strategy。
- **建议修改方向**：(1) 在 50% 条件下增加 "BCE + TEAL global（no compensation）" baseline；(2) 统一 30% 和 50% BCE baseline 使用相同推理管线；(3) 在 Table 1 caption 中更显著地标注这些差异。

---

**N4** [critical] 实际可用操作区间极窄，削弱论文贡献的实用意义

- **具体位置**：Table 1, Table 5, §4.4, Limitations
- **问题**：
  - **50%**：MMLU 28.1±0.2%（≈random 25%），GSM8K <2.2%——论文自己确认 "capacity-limited regime where no allocation strategy can recover"（§4.1）。KL 的 49% PPL 优势在 downstream 上完全无法体现。
  - **30%**：KL uniform PPL 8.81±0.02 vs TEAL 10.97（18% improvement），但 downstream 差异很小——MMLU 40.7±1.3 vs TEAL 38.61（+2.1pp），ARC-c 43.7±2.5 vs 42.32（+1.4pp），GSM8K 7.5±0.1 vs 7.88（-0.4pp，TEAL 反而更好）。在考虑 3-seed 标准差后，多数 downstream 差异不显著。
  - 论文的 headline number "49% PPL improvement" 来自一个 downstream 已经崩塌的操作点（50%），而实际有用的操作点（30%）的改进幅度小得多。
  - 更根本地：论文承认 "wall-clock speedup requires sparse kernel support not addressed here"（Introduction 最后一句，Appendix A）。当前实现 **增加** 6.4% 延迟。即使在 30% 的 PPL 改进也没有对应的实际加速。
- **为什么影响接收**：ACL ARR 的 excitement 维度评估 "practical significance"。当方法在唯一实用的操作点（30%）仅提供 ~2pp downstream 改进、且无实际加速时，贡献的实用价值有限。
- **建议修改方向**：(1) 坦诚讨论 30% 作为唯一实用操作点，downstream 改进幅度小；(2) 不要将 50% 的 headline PPL number 放在 Abstract 最显眼位置，因为该操作点 downstream 无意义；(3) 在 Introduction 的 contribution 列表中更精确地 scope 贡献："characterize when KL helps and when it doesn't"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 缺少训练数据消融

- **具体位置**：§4.1 (Training), Limitations
- **问题**：所有 predictor 均在 WikiText-103 上训练（1000 steps × batch 4 × seq 2048 ≈ 8M tokens），评估主要在 WikiText-2 上——同一 Wikipedia 域。C4 OOD 评估（Appendix C）显示 30% PPL 从 in-domain 1.46×dense 恶化到 OOD 1.74×dense，Limitations 自己承认 "the predictor partially overfits to training-domain activation patterns"。
- 缺乏消融：训练数据量（8M vs 80M tokens）、训练域（WikiText vs C4 vs mixed）对 mask quality 的影响未知。KL-discovered mask patterns 有多少是 domain-specific 的？
- **建议**：至少增加一组 C4-trained predictor 在 WikiText-2 上的评估，验证 mask patterns 的 domain 依赖性。

**W2** [warning] Adaptive penalty 公式与问题定义不一致

- **具体位置**：§3.5, Eq. 5-7, Appendix B (Table 6)
- **问题**：Eq. 5 定义不等式约束 $\bar{s} \leq 1-\rho$，但 Eq. 6 使用绝对值 $|\bar{s} - (1-\rho)|$，将其转化为等式约束（双向惩罚）。这与 Eq. 5 的问题定义不一致。虽然实际上等式约束更合理（过少的稀疏浪费计算），但形式化推导应保持一致。
- 更重要的是：30% target 的实际稀疏度为 28.5%（5% deviation, Table 6），$\lambda$ 饱和在 $\lambda_{max}=5000$。论文声称 "does not affect conclusions" 因为 "TEAL at interpolated 28.5% actual sparsity yields PPL≈10.7"（Appendix B），但这个 interpolated baseline 没有实际跑出来，只是估计。
- **建议**：(1) 统一 Eq. 5 和 Eq. 6 的约束类型；(2) 报告 28.5% 实际稀疏度对应的真实 TEAL PPL（而非估算）。

**W3** [warning] "PPL degradation 18%" 的计算方式与措辞不匹配

- **具体位置**：Abstract line 4, §4.1 第一段
- **问题**：Abstract 写 "KL reduces PPL degradation 18% over TEAL"。语义上 "reduces PPL degradation" 应指缩小 dense-to-sparse 的 PPL gap，计算应为 (TEAL degradation - KL degradation) / TEAL degradation = (4.85 - 2.84) / 4.85 = **41%**。但论文实际计算的是 relative PPL improvement: (10.97 - 8.96) / 10.97 = **18%**。
- 同样地，"49% at 50%" 用的是 (23.31 - 11.79) / 23.31 = 49%，同为 relative PPL improvement。如果改用 degradation reduction，50% 的数字会是 (17.19 - 5.67) / 17.19 = 67%。
- 两种计算方式本身都可以，但 "reduces PPL degradation" 的措辞与 relative PPL improvement 的计算不匹配。
- **建议**：统一措辞为 "reduces PPL by 18% relative to TEAL" 或改为 degradation reduction 计算。

**W4** [warning] Mistral-7B 缺少 downstream 评估

- **具体位置**：§4.5, Table 8 (Appendix G)
- **问题**：Mistral-7B 只报告了 PPL（Table 8），没有任何 downstream benchmark。鉴于 14B 出现了 PPL 改善但 MMLU 反转的现象（N2），仅凭 PPL 无法判断 Mistral 上的 downstream 表现。论文声称 "the KL advantage ratio is consistent across architectures"（§4.5），但这仅基于 PPL。
- **建议**：补充 Mistral-7B 在至少 MMLU 和 ARC-c 上的评估。

**W5** [warning] 缺少 predictor 架构的比较实验

- **具体位置**：§3.2, Table 2
- **问题**：论文只测试了 2-layer MLP（$d_b=128$）predictor。ShadowLLM 使用 attention-based routing，D2DMoE 使用不同的 predictor 设计。Table 2 taxonomy 暗示 KL objective 可以与任何 predictor 架构组合，但论文没有验证这一点。$d_b$ sensitivity（Appendix A, Table 5）只改变瓶颈宽度，不改变架构。
- **建议**：至少讨论为什么选择 2-layer MLP 而非更复杂架构（如带 attention 的 predictor），以及是否预期 KL advantage 对架构选择鲁棒。

**W6** [warning] SPON 的边际贡献（2.4%）与其在方法中的位置不匹配

- **具体位置**：§4.4 (SPON Contribution), Appendix I
- **问题**：SPON bias correction 仅贡献 2.4% PPL 改善（12.08→11.79），且与 KL predictor 弱相关（cosine 0.196, R²=0.038）。论文将 SPON 包含在方法和实验中，但其贡献微乎其微。
- **建议**：在方法中明确标注 SPON 为可选组件，或在 ablation 中更突出地展示其边际性。（不建议完全移除——2.4% 虽小但方向正确。）

---

## 小问题（不影响接收）

- **M1**: Gumbel-Sigmoid relaxation（§3.3）主要引用 Jang et al. (2017) 的 Gumbel-Softmax，但实际使用的二元形式更直接对应 Maddison et al. (2017) 的 Concrete distribution 和 Louizos et al. (2018) 的 L₀ regularization。虽然 Related Work 中引用了后两者，§3.3 本身应将它们作为主要引用。

- **M2**: §3.4 称 forward KL 为 "mean-seeking"，standard terminology 更常用 "mass-covering" 或 "inclusive"。"Mean-seeking" 多用于 moment matching 语境。

- **M3**: §3.6 的 "downstream Jacobian" 表述为 $\partial \mathbf{z}_{sparse} / \partial \mathbf{h}^{(\ell)}$，但实际出现在梯度链中的应该是 $\partial \mathbf{z}_{sparse} / \partial \tilde{m}_j^{(\ell)}$（对 mask 的 Jacobian，不是对 hidden state 的）。核心论点（gradient coupling）不受影响，但形式化表述可以更精确。

- **M4**: Table 4 的 SPON analysis 脚注提到使用 `evaluate.py` 而非 unified benchmark。如果 PPL 数值依赖于评估脚本的差异，应明确说明。

- **M5**: Table 1 的 KL global 50% 行中，MMLU 是 28.1±0.2（3-seed 标注），但 GSM8K 是 1.29（无 ± 标注，似乎是单 seed）。在同一行中混合不同的统计报告方式容易造成混淆。

---

## 数值一致性检查

跨表交叉验证结果：
- Abstract "18%": (10.97-8.96)/10.97=18.3% ✓（但措辞问题见 W3）
- Abstract "49%": (23.31-11.79)/23.31=49.4% ✓
- Abstract "7.5× smaller σ": 9.5/1.3=7.3×（接近 7.5×，可接受）
- Abstract "max Δ=0.59pp, 2-seed" vs Table 3: 50% 各 downstream max diff 确认 ✓
- Abstract "max Δ=1.68pp" at 30%: Table 3 MMLU 42.3-40.6=1.7pp ✓
- Table 1 KL uniform 50% PPL 11.92±0.07 vs Table 3 KL predictor 50% PPL 11.96: Table 1 是 3-seed mean, Table 3 是 seed 42, 一致 ✓
- Table 4 "Ours" PPL 11.79 vs Table 1 KL global 50% PPL 11.79 ✓
- Introduction "PPL 11.92 at 50% (3-seed)" vs Table 1 uniform ✓
- Appendix E 50% uniform 3-seed: 11.92±0.07 vs Table 1 ✓

引用验证：44 条引用全部在 bib 中，39 条在线验证通过。`de2024griffin` (Griffin) 在 OpenAlex 未找到匹配但论文真实存在。少数年份 mismatch（publication year vs preprint year），属正常范围。

---

## Questions for Authors

**Q1**: C1 ablation 中 "KL-derived oracle masks" 具体如何生成？是从 seed 42 的 fully-trained KL predictor 做 inference（hard top-k threshold）得到的吗？如果是，那么 C1 的 target quality 依赖于 KL predictor 的特定 seed——用另一个 seed 的 KL predictor 生成 masks 是否会得到不同结果？

**Q2**: 14B MMLU reversal 是否在多个 seed 上验证过？Table 7 仅报告 seed 42。如果该 reversal 在不同 seed 间不稳定，则可能只是噪声。

**Q3**: 30% sparsity 下 KL predictor 的 actual sparsity 为 28.5%（Table 6, 5% deviation）。Table 1 的 TEAL baseline 是在 exact 30% 还是也有偏差？如果 TEAL 在 exact 30% 而 KL 在 28.5%，那 KL 的一部分 PPL 优势来自于实际剪枝更少的 neurons。

**Q4**: 为什么没有报告 "BCE + TEAL global allocation（no compensation）" 在 50% sparsity 下的结果？这是与 KL global 最直接可比的 baseline。

**Q5**: 训练数据仅用 ~8M tokens of WikiText-103。在如此少的数据上，KL-discovered mask patterns 的 domain specificity 有多大？如果在 C4 上训练 predictor，mask divergence 从 magnitude 的幅度是否类似？

---

## Overall Assessment

**Overall**: 3.0 — Findings

**理由**：论文的核心发现（KL-trained masks diverge 68% from magnitude ranking, mask quality > gradient coupling）是有价值的 empirical contribution，方法公式化正确，消融较全面。但存在四个 critical 问题：(1) C1 因果声明统计效力不足（2-seed）且措辞过强；(2) 14B 规模出现 downstream reversal 但未充分讨论；(3) BCE baseline pipeline 在不同 sparsity 间不一致导致比较混淆；(4) 实际可用操作范围窄（仅 30%，downstream 改进 ~2pp），且无实际加速。

论文适合 Findings track：empirical insight 有贡献价值，但实验证据的说服力和方法的实用意义未达到 Conference 标准。若能修复 N1（增加 seed 并降低声明力度）、N2（充分讨论 14B reversal）和 N3（统一 BCE baseline），可以考虑 3.5 Borderline Conference。

**Confidence**: 4/5


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

_source line 820 · 2026-05-19T01:47:39.922248+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength、Must-Fix (N1-N3)、Should-Fix (W1-W5) 和 Question (Q1-Q4)，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（引用论文中的具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n**Overall**: 3.0 (Findings)\n\n## 主要优势 (Strengths)\n\n**S1. C1 Causal Ablation 设计精巧 (§4.4, Table 3)**\n将 mask target quality 和 gradient coupling 解耦的实验设计值得肯定。BCE 在 KL-derived targets 上复现 KL 质量（50% 时 max Δ=0.59pp），而 magnitude-based BCE 为 28.13±0.20，这有力地证明了 \"是 mask patterns 而非 gradient coupling 驱动质量\"。\n\n**S2. 实验设计系统、全面**\nAblation 覆盖了 divergence direction、relaxation、loss isolation、compensation redundancy、超参数鲁棒性，形成完整 ablation 矩阵。Regime analysis 对 allocation 策略的非单调偏好提供了有价值的实践指导。\n\n**S3. 诚实的 Scope 界定**\nIntroduction（L17）明确声明 \"Our contribution is empirical\" 和 \"Wall-clock speedup requires sparse kernel support not addressed here\"；14B MMLU gap 在 Abstract、Intro 和 Experiments 中均被报告；50% downstream collapse 被明确标注。\n\n**S4. 跨架构验证**\nMistral-7B-v0.3 和 Qwen-2.5-14B 验证，KL advantage ratio 跨架构一致（within 8% at ≤50%）。\n\n**S5. 写作质量整体较好**\n无 em-dash/en-dash AI 痕迹。段落长度合理。术语首次出现时有定义。全文主线连贯。\n\n## Must-Fix 问题\n\n**N1** [critical] 新颖性不足以支撑 Main Conference\n核心方法是三个已有技术的直接组合——KL distillation + Gumbel-Sigmoid + per-layer MLP predictor。MaskLLM 已组合 frozen weights + learnable masks + KL training + Gumbel relaxation。Table 2 taxonomy 学术贡献有限。\n\n**N2** [critical] 50% Sparsity 下 Downstream 全面崩溃，核心 PPL Claim 实际价值存疑\n最强数字 \"PPL 49% improvement at 50% sparsity\" 对应 MMLU 28.1±0.2%（≈random）、GSM8K 1.29%。Abstract 和 Introduction 仍以 50% PPL 改善作为核心卖点，构成 framing 偏差。\n\n**N3** [critical] 无 Wall-Clock Speedup，反而增加 6.4% Overhead\nTable 6 显示 126.78 vs 119.11 ms/forward。且未验证 KL masks 是否兼容 N:M structured sparsity。\n\n## Should-Fix 问题\n\n**W1** C1 Ablation 仅 2-seed 验证，统计力度不足\n**W2** 30% Sparsity 实际为 28.5%（5% deviation）\n**W3** 14B Scale 的 MMLU Gap 未被充分解释\n**W4** 训练/评估数据同域，OOD 泛化存疑\n**W5** -ing 分词短语偏多（AI 写作痕迹），约 15+ 处\n\n## Missing References\n1. SeerAttention (2024)\n2. Enabling Dynamic Sparsity in Quantized LLMs (2025)\n3. Mixture of Neuron Experts (2025)\n4. DeepSeek-V3 / DeepSeekMoE\n\n## Questions\n**Q1**: C1 ablation 的 oracle masks 从 KL predictor 哪个 checkpoint 提取？是否构成信息不对等？\n**Q2**: 为什么以 50% PPL improvement 而非 30% downstream preservation 作为核心叙事？\n**Q3**: 14B 的 KL MMLU=63.72% 而 BCE=71.67%、TEAL=71.83%，是否暗示 KL 在 14B 产生有害 mask patterns？\n**Q4**: 30% target 的 $\\lambda_{max}$ 提高到 10000+ 能否改善 sparsity precision？\n\n---\n\n请逐条回应。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu",
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
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength、Must-Fix (N1-N3)、Should-Fix (W1-W5) 和 Question (Q1-Q4)，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（引用论文中的具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n**Overall**: 3.0 (Findings)\n\n## 主要优势 (Strengths)\n\n**S1. C1 Causal Ablation 设计精巧 (§4.4, Table 3)**\n将 mask target quality 和 gradient coupling 解耦的实验设计值得肯定。BCE 在 KL-derived targets 上复现 KL 质量（50% 时 max Δ=0.59pp），而 magnitude-based BCE 为 28.13±0.20，这有力地证明了 \"是 mask patterns 而非 gradient coupling 驱动质量\"。\n\n**S2. 实验设计系统、全面**\nAblation 覆盖了 divergence direction、relaxation、loss isolation、compensation redundancy、超参数鲁棒性，形成完整 ablation 矩阵。Regime analysis 对 allocation 策略的非单调偏好提供了有价值的实践指导。\n\n**S3. 诚实的 Scope 界定**\nIntroduction（L17）明确声明 \"Our contribution is empirical\" 和 \"Wall-clock speedup requires sparse kernel support not addressed here\"；14B MMLU gap 在 Abstract、Intro 和 Experiments 中均被报告；50% downstream collapse 被明确标注。\n\n**S4. 跨架构验证**\nMistral-7B-v0.3 和 Qwen-2.5-14B 验证，KL advantage ratio 跨架构一致（within 8% at ≤50%）。\n\n**S5. 写作质量整体较好**\n无 em-dash/en-dash AI 痕迹。段落长度合理。术语首次出现时有定义。全文主线连贯。\n\n## Must-Fix 问题\n\n**N1** [critical] 新颖性不足以支撑 Main Conference\n核心方法是三个已有技术的直接组合——KL distillation + Gumbel-Sigmoid + per-layer MLP predictor。MaskLLM 已组合 frozen weights + learnable masks + KL training + Gumbel relaxation。Table 2 taxonomy 学术贡献有限。\n\n**N2** [critical] 50% Sparsity 下 Downstream 全面崩溃，核心 PPL Claim 实际价值存疑\n最强数字 \"PPL 49% improvement at 50% sparsity\" 对应 MMLU 28.1±0.2%（≈random）、GSM8K 1.29%。Abstract 和 Introduction 仍以 50% PPL 改善作为核心卖点，构成 framing 偏差。\n\n**N3** [critical] 无 Wall-Clock Speedup，反而增加 6.4% Overhead\nTable 6 显示 126.78 vs 119.11 ms/forward。且未验证 KL masks 是否兼容 N:M structured sparsity。\n\n## Should-Fix 问题\n\n**W1** C1 Ablation 仅 2-seed 验证，统计力度不足\n**W2** 30% Sparsity 实际为 28.5%（5% deviation）\n**W3** 14B Scale 的 MMLU Gap 未被充分解释\n**W4** 训练/评估数据同域，OOD 泛化存疑\n**W5** -ing 分词短语偏多（AI 写作痕迹），约 15+ 处\n\n## Missing References\n1. SeerAttention (2024)\n2. Enabling Dynamic Sparsity in Quantized LLMs (2025)\n3. Mixture of Neuron Experts (2025)\n4. DeepSeek-V3 / DeepSeekMoE\n\n## Questions\n**Q1**: C1 ablation 的 oracle masks 从 KL predictor 哪个 checkpoint 提取？是否构成信息不对等？\n**Q2**: 为什么以 50% PPL improvement 而非 30% downstream preservation 作为核心叙事？\n**Q3**: 14B 的 KL MMLU=63.72% 而 BCE=71.67%、TEAL=71.83%，是否暗示 KL 在 14B 产生有害 mask patterns？\n**Q4**: 30% target 的 $\\lambda_{max}$ 提高到 10000+ 能否改善 sparsity precision？\n\n---\n\n请逐条回应。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-19T01:48:10.967376+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 31045
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-19T01:48:11.369667+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength、Must-Fix (N1-N4)、Should-Fix (W1-W6) 和 Question (Q1-Q5)，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（引用论文中的具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告\n\n**Overall**: 3.0 (Findings)\n\n## 主要优势\n\n**S1. 清晰的核心发现**：KL-trained masks 与 magnitude-based masks 的 68% 发散以及 C1 因果消融表明 mask target quality 是主要驱动力，有价值的 empirical finding。\n\n**S2. 方法公式化简洁正确**：Gumbel-Sigmoid、forward KL、predictor 架构轻量且不需 compensation network。\n\n**S3. 全面的消融研究**：Table 4 系统消融 divergence direction、relaxation、compensation 冗余性、超参数鲁棒性。\n\n**S4. 诚实报告负面结果**：50% downstream collapse、14B MMLU reversal、30% global MMLU 高方差。\n\n**S5. 写作组织清晰**：Taxonomy 有效定位，gradient analysis 在声称 \"suggestive\" 后正确指向因果验证。\n\n## Must-Fix 问题\n\n**N1** [critical] C1 因果消融的声明力度与统计效力不匹配\n- 多处使用 \"causal ablation proves\"，但仅 2-seed\n- 30% PPL gap 9.45 vs 8.82 (+7.1%) 与 97.5% mask agreement 矛盾，暗示 gradient coupling 在低稀疏度可能仍然重要\n- C1 设计本身存在混淆：KL 训练时用 soft Gumbel-Sigmoid masks，C1 的 BCE 用 hard binary targets。改变了 gradient coupling 也改变了 mask 特性（soft vs hard）\n\n**N2** [critical] 14B 规模 downstream 反转削弱泛化声明\n- KL PPL 优势（7.62 vs TEAL 8.73）但 MMLU -8.1pp (63.7 vs 71.8)，ARC-c/GSM8K 也劣于 BCE\n- Uniform allocation 同样趋势（64.49 vs 66.34）\n- Abstract \"confirms PPL advantage across 7-14B\" 轻描淡写 downstream degradation\n\n**N3** [critical] BCE baseline 在不同稀疏度使用不同实验管线\n- 30% BCE: TEAL global, no compensation, 2700 steps\n- 50% BCE: DejaVu pipeline + compensation (+67.2M), no TEAL, 2700 steps\n- 缺少 \"50% BCE + TEAL global (no compensation)\" 这个最直接可比的 baseline\n\n**N4** [critical] 实际可用操作区间极窄\n- 50%: MMLU≈random, 无实用价值\n- 30%: downstream improvement ~2pp (多数不显著)\n- 无实际加速，反而 +6.4% overhead\n- Headline \"49% PPL improvement\" 来自 downstream 已崩塌的操作点\n\n## Should-Fix 问题\n\n**W1** 缺少训练数据消融（~8M tokens WikiText-103，domain specificity 未知）\n**W2** Adaptive penalty Eq.5 不等式约束 vs Eq.6 绝对值（等式约束）不一致；28.5% actual vs 30% target\n**W3** \"PPL degradation 18%\" 措辞与计算不匹配（实际是 relative PPL improvement）\n**W4** Mistral-7B 缺少 downstream 评估\n**W5** 缺少 predictor 架构比较实验\n**W6** SPON 边际贡献（2.4%）与其在方法中的位置不匹配\n\n## Minor Issues\n**M1**: Gumbel-Sigmoid 在 §3.3 应优先引用 Concrete/L₀ 而非 Gumbel-Softmax\n**M2**: \"mean-seeking\" 应为 \"mass-covering\"/\"inclusive\"\n**M3**: §3.6 Jacobian 形式化不精确\n**M4**: Table 4 SPON 脚注 evaluate.py vs unified benchmark\n**M5**: Table 1 同行混合不同统计报告\n\n## Questions\n**Q1**: C1 oracle masks 如何生成？seed 依赖性？\n**Q2**: 14B MMLU reversal 是否多 seed 验证？\n**Q3**: 30% TEAL baseline 是否在 exact 30%？KL 在 28.5%？\n**Q4**: 为什么没有 50% BCE + TEAL global（no comp）baseline？\n**Q5**: 在 C4 上训练 predictor 的 mask divergence 是否类似？\n\n---\n\n请逐条回应。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu",
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
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength、Must-Fix (N1-N4)、Should-Fix (W1-W6) 和 Question (Q1-Q5)，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（引用论文中的具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告\n\n**Overall**: 3.0 (Findings)\n\n## 主要优势\n\n**S1. 清晰的核心发现**：KL-trained masks 与 magnitude-based masks 的 68% 发散以及 C1 因果消融表明 mask target quality 是主要驱动力，有价值的 empirical finding。\n\n**S2. 方法公式化简洁正确**：Gumbel-Sigmoid、forward KL、predictor 架构轻量且不需 compensation network。\n\n**S3. 全面的消融研究**：Table 4 系统消融 divergence direction、relaxation、compensation 冗余性、超参数鲁棒性。\n\n**S4. 诚实报告负面结果**：50% downstream collapse、14B MMLU reversal、30% global MMLU 高方差。\n\n**S5. 写作组织清晰**：Taxonomy 有效定位，gradient analysis 在声称 \"suggestive\" 后正确指向因果验证。\n\n## Must-Fix 问题\n\n**N1** [critical] C1 因果消融的声明力度与统计效力不匹配\n- 多处使用 \"causal ablation proves\"，但仅 2-seed\n- 30% PPL gap 9.45 vs 8.82 (+7.1%) 与 97.5% mask agreement 矛盾，暗示 gradient coupling 在低稀疏度可能仍然重要\n- C1 设计本身存在混淆：KL 训练时用 soft Gumbel-Sigmoid masks，C1 的 BCE 用 hard binary targets。改变了 gradient coupling 也改变了 mask 特性（soft vs hard）\n\n**N2** [critical] 14B 规模 downstream 反转削弱泛化声明\n- KL PPL 优势（7.62 vs TEAL 8.73）但 MMLU -8.1pp (63.7 vs 71.8)，ARC-c/GSM8K 也劣于 BCE\n- Uniform allocation 同样趋势（64.49 vs 66.34）\n- Abstract \"confirms PPL advantage across 7-14B\" 轻描淡写 downstream degradation\n\n**N3** [critical] BCE baseline 在不同稀疏度使用不同实验管线\n- 30% BCE: TEAL global, no compensation, 2700 steps\n- 50% BCE: DejaVu pipeline + compensation (+67.2M), no TEAL, 2700 steps\n- 缺少 \"50% BCE + TEAL global (no compensation)\" 这个最直接可比的 baseline\n\n**N4** [critical] 实际可用操作区间极窄\n- 50%: MMLU≈random, 无实用价值\n- 30%: downstream improvement ~2pp (多数不显著)\n- 无实际加速，反而 +6.4% overhead\n- Headline \"49% PPL improvement\" 来自 downstream 已崩塌的操作点\n\n## Should-Fix 问题\n\n**W1** 缺少训练数据消融（~8M tokens WikiText-103，domain specificity 未知）\n**W2** Adaptive penalty Eq.5 不等式约束 vs Eq.6 绝对值（等式约束）不一致；28.5% actual vs 30% target\n**W3** \"PPL degradation 18%\" 措辞与计算不匹配（实际是 relative PPL improvement）\n**W4** Mistral-7B 缺少 downstream 评估\n**W5** 缺少 predictor 架构比较实验\n**W6** SPON 边际贡献（2.4%）与其在方法中的位置不匹配\n\n## Minor Issues\n**M1**: Gumbel-Sigmoid 在 §3.3 应优先引用 Concrete/L₀ 而非 Gumbel-Softmax\n**M2**: \"mean-seeking\" 应为 \"mass-covering\"/\"inclusive\"\n**M3**: §3.6 Jacobian 形式化不精确\n**M4**: Table 4 SPON 脚注 evaluate.py vs unified benchmark\n**M5**: Table 1 同行混合不同统计报告\n\n## Questions\n**Q1**: C1 oracle masks 如何生成？seed 依赖性？\n**Q2**: 14B MMLU reversal 是否多 seed 验证？\n**Q3**: 30% TEAL baseline 是否在 exact 30%？KL 在 28.5%？\n**Q4**: 为什么没有 50% BCE + TEAL global（no comp）baseline？\n**Q5**: 在 C4 上训练 predictor 的 mask divergence 是否类似？\n\n---\n\n请逐条回应。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 823 · 2026-05-19T01:48:13.083871+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1714
}
```

</details>

---


### Assistant

_source line 824 · 2026-05-19T01:48:16.151690+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 62

## Round 62

2 recorded events


### User

_source line 825 · 2026-05-19T01:48:18.770515+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：**Overall 3.0 (Findings)**。识别了 4 个 critical 问题：

1. **N1**: C1 因果消融仅 2-seed 验证，"causal ablation proves" 的声明力度与统计效力严重不匹配；30% PPL gap (9.45 vs 8.82) 暗示 gradient coupling 仍有残余贡献
2. **N2**: Qwen-14B 出现 PPL 改善但 MMLU 反转 (63.7 vs TEAL 71.8)，削弱跨规模泛化声明，正文讨论不充分
3. **N3**: BCE baseline 在 30%（TEAL global, no comp）和 50%（compensation, no TEAL）使用不同 pipeline，缺少最直接可比的 "BCE + TEAL global @ 50%" baseline
4. **N4**: 实际可用操作区间仅 ≤30%（50% downstream 全部崩塌），30% 的 downstream 改进仅 ~2pp，且当前实现增加 6.4% latency

6 个 should-fix（训练数据消融缺失、penalty 公式不一致、PPL degradation 措辞误导、Mistral 缺 downstream、predictor 架构未对比、SPON 边际贡献）和 5 个 minor issues。数值一致性验证通过，引用全部 verified。

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

_source line 826 · 2026-05-19T01:48:26.614714+00:00_

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


## Round 63

## Round 63

2 recorded events


### User

_source line 827 · 2026-05-19T01:50:29.625718+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Strengths 回应

**[AGREE] S1 (C1 Causal Ablation 设计精巧)**
同意设计本身的精巧性。但需补充限制条件（见我的 N1）：C1 仅 2-seed 验证，且 soft-vs-hard mask 训练差异是未控制的混淆变量。30% 条件下 PPL gap（9.45 vs 8.82 = +7.1%）也暗示 gradient coupling 可能在低稀疏度仍有残余贡献，R2 的评价未涉及此点。

**[AGREE] S2 (实验设计系统全面)**
同意。我在 S3 中也给出了类似评价。Table 4 的消融矩阵覆盖面确实较好，regime analysis（Table 5，§4.4）的非单调发现有实践价值。

**[AGREE] S3 (诚实的 Scope 界定)**
同意。Introduction L17 的 "Our contribution is empirical" 和 "Wall-clock speedup requires sparse kernel support not addressed here" 是难得的诚实表述。但诚实 scope 界定不能替代解决 scope 本身过窄的问题。

**[REBUT] S4 (跨架构验证)**
R2 将 Mistral-7B 和 Qwen-14B 同时列为验证跨架构泛化的证据，但这两个结果传达了矛盾信号：
- Mistral-7B（Table 8, Appendix G）：仅报告 PPL，**完全没有 downstream evaluation**。鉴于 14B 出现了 PPL↑但 MMLU↓ 的反转，仅有 PPL 的 Mistral 结果不能称为 "验证"。
- Qwen-14B（Table 7, Appendix H）：MMLU 63.7% vs TEAL 71.8%（-8.1pp），GSM8K 48.82% vs TEAL 49.51%，ARC-c 和 WG 上 KL 也均略低于 BCE。这更像是一个 **负面结果** 而非 "验证"。
- "KL advantage ratio 跨架构一致（within 8%）" 仅针对 PPL ratio 成立（Table 8），不是跨所有指标的一致性。

结论：跨架构的 **PPL** 优势是一致的，但跨架构的 **downstream** 泛化未被验证（Mistral 缺失数据，14B 反转）。R2 对 S4 的评价过于宽松。

**[AGREE] S5 (写作质量)**
同意无明显 AI 痕迹（em-dash/en-dash）。R2 在 W5 指出 -ing 短语偏多，但这属于文体偏好，不影响学术判断。

---

## Must-Fix 回应

**[REBUT] R2-N1 (新颖性不足以支撑 Main Conference)**

R2 认为方法是 "三个已有技术的直接组合"，并以 MaskLLM 作为优先性论据。这一判断需要细化：

1. **MaskLLM 对比不准确**：论文 Related Work（lines 14-17）明确区分了三个维度：(a) sparsity type（MaskLLM = N:M 静态 weight sparsity, 本文 = 动态 per-token activation sparsity），(b) mask generation（MaskLLM = 直接可学习参数, 本文 = predictor network 生成），(c) allocation（MaskLLM = fixed N:M groups, 本文 = global top-k cross-layer budget）。这不是同一个方法的简单迁移——global top-k allocation 下的 inter-neuron dependency 是 MaskLLM 不存在的问题。

2. **核心贡献是 empirical finding，不是方法组件**：论文自己明确定位 "Our contribution is empirical"（Introduction L17）。核心发现是：(a) KL-trained masks diverge 68% from magnitude（§4.3），(b) C1 ablation 证据表明 mask quality > gradient coupling。即使方法组件都是已知的，这个实证发现本身在文献中没有先例。

3. **Table 2 taxonomy 的价值**：R2 认为 taxonomy "学术贡献有限"。我部分同意——taxonomy 本身不是主要贡献。但它有效地 positioning 了方法在 correction granularity × training signal coupling 空间中的位置，帮助读者理解本文填补了 "per-token × coupled" 这个空白。

4. **EMNLP Findings vs Main 标准**：R2 的 N1 结论是 "不支撑 Main Conference"。我同意方法新颖性不足以支撑 Main，但 empirical finding 的价值足以支撑 Findings。不过，N1 本身不应是 "Must-Fix"——新颖性不是可以 "fix" 的问题，而是定位问题。我在 Overall Assessment 中也给出 3.0 (Findings)，理由主要是实验证据问题（N1-N4），而非方法新颖性。

**[AGREE] R2-N2 (50% Downstream 崩溃，PPL Claim 实际价值存疑)**

完全同意，这与我的 N4 一致。补充具体证据：

- Table 1, 50%: KL global MMLU 28.1±0.2% vs dense 65.27%（保留率仅 43%，接近 random 25%/38%）；GSM8K 1.29% vs dense 48.75%（几乎归零）。
- Abstract 的叙事结构问题：前 3 行建立 C1 ablation 证据 → 第 4 行 "At 30%, KL reduces PPL degradation 18%" → 第 5 行 **"At 50%, the PPL advantage widens to 49%"** → 第 6 行讲跨架构。读者的注意力被引导到 50% 的 "49% improvement"，但这个数字对应的是 downstream 已经崩塌的操作点。
- 更根本的问题（我在 N4 中也提到）：30% 作为唯一实用操作点，downstream 改进幅度很小——MMLU +2.1pp（40.7 vs 38.6），ARC-c +1.4pp，GSM8K 反而低 0.4pp。考虑 3-seed σ，多数差异不显著。

R2 准确地将此识别为 "framing 偏差"，我同意。

**[AGREE] R2-N3 (无 Wall-Clock Speedup)**

同意这限制了论文的实用价值，但我认为严重程度低于 R2 的评估：

- 论文在 Introduction L17 已明确 scope："Wall-clock speedup requires sparse kernel support not addressed here"。Appendix A 对 6.4% overhead 做了详细分析（predictor 3.17ms = 2.7%，mask application 占其余）。
- 论文的定位是 prediction quality 研究，不是 systems paper。在 activation sparsity 领域，prediction quality 和 kernel implementation 通常由不同的工作解决（TEAL 本身也面临类似问题——unstructured sparsity 需要 sparse kernel）。
- 但 R2 指出的 "未验证 KL masks 是否兼容 N:M structured sparsity" 是一个有效的 should-fix 问题。如果 KL masks 的 pattern 与 N:M structure 不兼容，则即使有 sparse kernel 也无法实现加速。Limitations 中虽提到 "N:M structured sparsity" 作为 future work，但未讨论兼容性问题。

我将此定级为 should-fix 而非 must-fix，因为论文已诚实 scope 界定；但 N:M 兼容性讨论应当补充。

---

## Should-Fix 回应

**[AGREE] R2-W1 (C1 仅 2-seed)**
完全同意，这与我的 N1 一致。2-seed 对于论文最核心的 "causal" claim 不够。我在 N1 中将此列为 must-fix，因为 C1 是论文在 Abstract 和 Introduction 中反复引用的核心证据。

**[AGREE] R2-W2 (28.5% 实际稀疏度)**
同意，与我的 W2 一致。补充：Appendix B (Table 6) 显示 30% target 的 $\lambda$ 饱和在 $\lambda_{max}=5000$，actual sparsity 28.5%（5% deviation）。论文用估算的 "TEAL at interpolated 28.5% yields PPL≈10.7" 来辩护，但这个 interpolated 数字没有实际跑出来。KL 在 28.5% actual sparsity 下 PPL=8.96 vs TEAL at exact 30% PPL=10.97，如果 TEAL 在 28.5% 可能只有 ~10.5-10.7，那 KL 的 "18% improvement" 中有一部分来自剪枝更少的 neurons。

**[AGREE] R2-W3 (14B MMLU Gap 未充分解释)**
完全同意，与我的 N2 一致。我将此列为 must-fix 级别。Table 7 显示 KL 在 14B 的 MMLU (63.7%) 不仅低于 TEAL (71.8%)，还低于 BCE (71.7%)——后者使用的是 magnitude-based masks。这直接质疑了 "KL discovers superior mask patterns" 的核心叙事：在 14B 上，KL 的 mask patterns 似乎是 inferior 的（至少对 MMLU 能力而言）。论文仅用 "scale-dependent gap not resolved by allocation strategy" 一句带过（§4.5, Introduction L16），没有提供机制解释。

**[AGREE] R2-W4 (训练/评估同域)**
同意，与我的 W1 一致。训练 WikiText-103 → 评估 WikiText-2 是同域。C4 OOD 评估（Appendix C）显示 degradation 从 in-domain 1.46×dense 恶化到 1.74×dense，Limitations 自己承认 "partially overfits"。缺少训练数据消融（不同域/不同量）。

**[REBUT] R2-W5 (-ing 分词短语偏多)**
R2 称 "约 15+ 处 -ing 分词短语"，我认为这一指控需要具体化。学术论文中 -ing 短语的使用本身不是问题，问题是 -ing 短语结尾的 filler pattern（如 "..., highlighting the applicability of..."）。通读论文后，我认为：
- 论文的 -ing 使用大部分是标准学术用法（如 "training", "coupling", "conditioning on"），不是 AI 典型的 -ing 结尾 filler
- 少数可优化处存在（如 §3.3 "permitting gradient flow" 可改为 "permits gradient flow"），但数量不构成系统性问题
- "AI 写作痕迹" 的判断应基于整体文风，不应仅凭 -ing 出现次数。全文无 em-dash/en-dash、无过度分段、术语有定义——整体文风合格

这是 minor issue 级别，不应列为 should-fix。

---

## Missing References 回应

**[REBUT] SeerAttention (2024)**：SeerAttention 针对 attention sparsity（注意力稀疏），本文针对 FFN activation sparsity。两者优化的模块不同（attention vs FFN），技术方案不同（attention pattern prediction vs neuron importance prediction）。Related Work 的 Polar Sparsity 引用（§Related Work line 32）已覆盖 attention sparsity 方向。加入 SeerAttention 不会改变论文的 positioning。

**[AGREE] Enabling Dynamic Sparsity in Quantized LLMs (2025)**：同意应引用。量化 + 稀疏的交互是重要的实用方向，尤其论文未讨论 KL masks 在量化模型上的行为。

**[AGREE] Mixture of Neuron Experts (2025)**：同意应引用。该工作将 FFN neurons 组织为 expert groups，与本文的 per-neuron prediction 形成有意义的对比。

**[REBUT] DeepSeek-V3 / DeepSeekMoE**：DeepSeek 是 native MoE 架构（训练时就是稀疏的），本文处理的是从 dense SwiGLU 模型中提取 activation sparsity。两者的问题定义不同。Related Work 已引用 Switch Transformers 和 Expert Choice Routing 作为 MoE routing 的代表，足以覆盖该方向。

---

## Questions 回应

**[AGREE] R2-Q1 (C1 oracle masks 的 checkpoint 和信息不对等)**
重要问题，与我的 Q1 完全一致。论文未说明 KL-derived masks 从哪个 checkpoint 提取。如果是 fully-converged KL predictor (step 1000) 的 hard top-k masks，则 C1 BCE predictor 享受了 KL 完整训练过程的 "成果"，而标准 BCE 只能从 magnitude 信息出发。这不是 "信息不对等" 问题——这正是 C1 要测试的（给 BCE 最好的 targets 看它能否匹配 KL）——但论文应明确说明 checkpoint 选择和 mask 生成过程。

**[AGREE] R2-Q2 (为何以 50% PPL 而非 30% downstream 作为核心叙事)**
同意这是 framing 问题。Abstract 的叙事高潮放在 "At 50%, the PPL advantage widens to 49%"，但 50% 是 downstream-dead zone。30% 的 downstream preservation 更有实用价值（MMLU 40.7% vs dense 65.3% = 62% 保留率），应该作为核心叙事的重心。

**[AGREE] R2-Q3 (14B KL 是否产生有害 mask patterns)**
这是我 N2 的核心关切。Table 7 数据支持 "有害" 假说：KL MMLU=63.72% vs BCE=71.67% vs TEAL=71.83%。BCE 使用 magnitude-based masks 且在 14B 上保持了 MMLU 性能，而 KL 的 divergent mask patterns 导致 MMLU 下降 8pp。一种假设：14B 模型的 MMLU 关键 neurons 可能与 activation magnitude 高度相关（即 magnitude ranking 在 14B 上是一个更好的 proxy），KL 的 divergent patterns 错误地剪裁了这些 neurons。但论文未提供任何层级分析来支持或反驳此假设。

**[REBUT] R2-Q4 ($\lambda_{max}$ 提高到 10000+ 能否改善 sparsity precision)**
这个问题方向正确但可能无法解决根本问题。Appendix B (Table 6) 显示 30% target 的 $\lambda$ 已饱和在 $\lambda_{max}=5000$，actual sparsity=28.5%。提高 $\lambda_{max}$ 理论上可以进一步压低 sparsity，但：
- 过高的 $\lambda$ 会使 penalty term 主导 loss，导致 KL 质量下降（predictor 优先满足 sparsity 约束而非 output-distribution fidelity）
- 论文的 penalty 是 quadratic（Eq. 6 的平方项），$\lambda=5000$ 时 penalty 已经很大，再翻倍可能导致数值不稳定
- 更根本的问题可能是 SwiGLU gate 的自然激活分布在 30% sparsity 附近有一个 "硬边界"——迫使过多 neurons 关闭超出了 Gumbel-Sigmoid 的调节能力

更好的解决方案可能是直接在 sparsity-matched 条件下评估（即 TEAL 也在 28.5% 下评估），而非试图强制 controller 精确收敛。

---

## 与我的审稿意见的主要分歧

| 议题 | R1 (我的评价) | R2 评价 | 分歧 |
|------|--------------|---------|------|
| N1 新颖性 | Should-fix (方法新颖性有限但 empirical finding 有价值) | Must-fix (不支撑 Main) | R2 更严格；我认为 empirical finding 足以支撑 Findings |
| C1 统计效力 | Must-fix (N1) | Should-fix (W1) | **我更严格**；C1 是论文核心 claim 的唯一直接证据 |
| 14B reversal | Must-fix (N2) | Should-fix (W3) | **我更严格**；这直接质疑方法的 scalability |
| Wall-clock overhead | Should-fix (论文已诚实 scope) | Must-fix (N3) | R2 更严格；论文明确表示不是 systems contribution |
| -ing 短语 | 不认为是问题 | Should-fix (W5) | R2 过于严格 |
| BCE baseline 混淆 | Must-fix (我的 N3) | 未提及 | **R2 遗漏了重要问题** |

**R2 遗漏的关键问题**：R2 没有指出 Table 1 中 BCE baseline 在 30% 和 50% 使用不同 pipeline 的混淆变量（我的 N3）。30% BCE 用 TEAL global / no compensation / 2700 steps；50% BCE 用 DejaVu pipeline / compensation / no TEAL。这使得跨 sparsity 的 KL vs BCE 比较不可靠。R2 也没有指出 Abstract 中 "reduces PPL degradation 18%" 的措辞与实际计算方式不匹配（我的 W3）。

**总体评分一致**：R1 和 R2 均给出 3.0 (Findings)，核心理由略有不同（R1 侧重实验证据强度，R2 侧重方法新颖性），但结论趋同。


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

_source line 828 · 2026-05-19T01:50:50.182968+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 64

## Round 64

2 recorded events


### User

_source line 829 · 2026-05-19T01:50:52.826341+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。主要结论：

- **与 R2 评分一致**（均 3.0 Findings），核心分歧在问题定级
- **我比 R2 更严格的点**：C1 统计效力（我列 Must-fix，R2 列 Should-fix）、14B reversal（同上）
- **R2 比我更严格的点**：方法新颖性（R2 列 Must-fix，我认为 empirical finding 足以支撑 Findings）、wall-clock overhead（R2 列 Must-fix，但论文已诚实 scope 界定）
- **R2 遗漏的关键问题**：BCE baseline 在 30% vs 50% 使用不同 pipeline 的混淆变量（我的 N3）、PPL degradation 措辞不匹配（我的 W3）

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

_source line 830 · 2026-05-19T01:51:01.794548+00:00_

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


## Round 65

## Round 65

12 recorded events


### User

_source line 831 · 2026-05-19T01:51:12.479738+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 的逐条交叉回应

## 概要

R1 的审稿意见质量高、技术细节扎实。在 23 个 issue 中我同意 20 个（包括所有 4 个 Must-Fix），反驳 3 个（W5, W6, M3）。

两位 Reviewer 共同指向 **Overall 3.0 (Findings)**，核心理由一致：方法新颖性有限（已有组件的直接组合）、实际可用范围极窄（50% downstream collapse, 30% modest improvement, no speedup）、C1 ablation 统计效力不足。

## Must-Fix 共识（4/4 同意）

- **N1 [AGREE]**: C1 ablation 2-seed + R1 新发现的 soft vs hard mask confound——后者是我 Round 1 遗漏的关键问题
- **N2 [AGREE]**: 14B downstream reversal，补充发现 BCE 在 14B 上 MMLU 正常 (71.67%)，问题特定于 KL coupled training
- **N3 [AGREE]**: BCE baseline 管线不一致是我 Round 1 遗漏的重要问题——50% BCE 未使用 TEAL allocation，与 KL 不可比
- **N4 [AGREE]**: 实际可用区间极窄，与我的 N2+N3 一致

## Should-Fix（4/6 同意，2 反驳）

- **W1-W4 [AGREE]**: 训练数据消融、Eq.5/6不一致、PPL phrasing 误导、Mistral 缺 downstream
- **W5 [REBUT]**: predictor 架构比较——论文贡献在 objective 而非 architecture，$d_b$ sweep 已提供，降级为 minor
- **W6 [REBUT]**: SPON positioning——Related Work 段落是必要的 positioning，2.4% 结果是有价值的正交性证据

## Minor（4/5 同意，1 反驳）

- **M1, M2, M4, M5 [AGREE]**
- **M3 [REBUT]**: §3.6 已标注 "suggestive"，对 suggestive analysis 要求完整形式化不合理

## R1 比我额外发现的关键问题

1. N3（BCE 管线不一致）和 N1(c)（soft vs hard confound）是我 Round 1 遗漏的重要发现，直接影响核心 claim 可信度
2. W2（Eq.5 vs Eq.6 不一致）是有效的技术细节问题

## 最终评估：维持 Overall 3.0 (Findings)

R1 的发现（尤其 N3 和 N1(c)）进一步强化了我对论文的判断。建议 Findings track 接收，不建议 Main Conference。


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

_source line 832 · 2026-05-19T01:52:22.982576+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\\\\\enlargethispage",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\\\\\enlargethispage",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-19T01:52:23.133609+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-19T01:52:25.193230+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && cat main.tex introduction.tex method.tex experiments.tex related_work.tex conclusion.tex limitations.tex ethics.tex appendix.tex abstract.tex | grep -c '\\\\\\\\' | head -1; echo \"---\"; wc -l main.tex introduction.tex method.tex experiments.tex related_work.tex conclusion.tex limitations.tex ethics.tex appendix.tex abstract.tex",
  "description": "Count lines in paper source files"
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
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && cat main.tex introduction.tex method.tex experiments.tex related_work.tex conclusion.tex limitations.tex ethics.tex appendix.tex abstract.tex | grep -c '\\\\\\\\' | head -1; echo \"---\"; wc -l main.tex introduction.tex method.tex experiments.tex related_work.tex conclusion.tex limitations.tex ethics.tex appendix.tex abstract.tex",
    "description": "Count lines in paper source files"
  }
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-19T01:52:25.395219+00:00_

101
---
   45 main.tex
   24 introduction.tex
  160 method.tex
  232 experiments.tex
   40 related_work.tex
    6 conclusion.tex
   10 limitations.tex
   43 ethics.tex
  369 appendix.tex
    6 abstract.tex
  935 total
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-19T01:53:00.135878+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__update_review_issues",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-19T01:53:00.487699+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-19T01:54:59.536397+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 9 (fresh review) findings\n  # ============================================================\n\n  - id: \"R9-N1\"\n    summary: \"C1 causal ablation: 2-seed insufficient for 'proves' claim + soft-vs-hard mask confound uncontrolled\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1 raised as Must-Fix N1 (2-seed + soft-vs-hard confound + 30% PPL gap). R2 initially Should-Fix W1, upgraded to AGREE with R1 in cross-response. Full consensus: C1 is core claim but evidence insufficient.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-N2\"\n    summary: \"BCE baseline pipeline inconsistent across sparsity levels: 30% uses TEAL/no-comp, 50% uses DejaVu+comp/no-TEAL\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1 raised as Must-Fix N3. R2 missed in initial review, AGREE in cross-response. Missing key baseline: 50% BCE + TEAL global (no comp).\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-N3\"\n    summary: \"Narrow usable range (only 30%, ~2pp downstream gain) + 50% framing bias in Abstract + no wall-clock speedup (+6.4% overhead)\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1-N4 + R2-N2 + R2-N3 converged. Both agree 50% PPL headline misleading given downstream collapse. R1 rates no-speedup as should-fix (honest scope), R2 rates must-fix. Consensus: framing needs rebalancing toward 30%.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-N4\"\n    summary: \"Method novelty insufficient for Main: KL+Gumbel+predictor = existing components, MaskLLM overlap\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R2 raised as Must-Fix N1. R1 REBUT on severity (empirical finding has value for Findings, novelty not fixable) but AGREE on substance. Consensus: Findings-appropriate, not Main.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W1\"\n    summary: \"PPL degradation 18% wording mismatch: text says 'reduces PPL degradation' but calculates relative PPL improvement\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1], note: \"R1-W3. R2 did not raise. Factual mismatch in Abstract line 4.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W2\"\n    summary: \"Mistral-7B missing all downstream evaluation; cross-arch claim based on PPL only\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1], note: \"R1-W4. Given 14B PPL-vs-downstream reversal, Mistral PPL-only evidence insufficient for cross-arch generalization claim.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W3\"\n    summary: \"Eq.5 defines inequality constraint but Eq.6 uses absolute value (equality constraint); formalization inconsistent\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1-W2. R2 AGREE in cross-response.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W4\"\n    summary: \"Training data ablation missing: all predictors trained on ~8M tokens WikiText-103, domain specificity of KL masks unknown\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1-W1 + R2-W4 converged. C4 OOD shows 1.46x->1.74x degradation. No C4-trained predictor comparison.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-I1\"\n    summary: \"Minor writing/format issues: -ing phrases (~15), float spacing compression, Ethics missing Qwen-14B, Gumbel citation priority, forward KL terminology\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R2-W5 (-ing phrases, R1 rebuts as minor), R2-M1/M2/M3/M4/M5, R1-M1/M2/M3/M4/M5 collected.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Recurring issues from prior rounds (updated with R9 status)\n  # ============================================================\n\n  - id: \"R8-N2\"\n    summary: \"14B MMLU reversal: KL PPL best (7.62) but MMLU -8.1pp vs TEAL, contradicts output-preservation narrative\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-N3 + R2-N2, full AGREE. Abstract 'confirms across 7-14B' is selective reporting.\"}\n      - {round: 9, reviewers: [1, 2], note: \"R1-N2 + R2-W3 reconfirmed. R1 notes BCE MMLU=71.67 normal at 14B, problem specific to KL coupled training. Abstract now states gap but no mechanism explanation. Both AGREE must-fix.\"}\n    action_items:\n      - {round: 8, action: \"Restrict Abstract/Intro scope to 7-8B primary; 14B as exploratory/mixed.\", assigned_to: \"paper_agent\", status: done}\n      - {round: 8, action: \"14B additional analysis: NOT doing.\", assigned_to: \"\", status: wont_fix}\n    resolution: \"Paper reframed with explicit 14B gap statement, but R9 finds discussion still insufficient — no mechanism hypothesis provided.\"\n    resolution_round: null\n\n  - id: \"R8-W4\"\n    summary: \"Training/eval domain overlap: WikiText-103 to WikiText-2, C4 OOD limited\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W3 + R2-W2, full AGREE.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Reconfirmed as R9-W4. C4 30% PPL 1.74x dense (vs in-domain 1.46x). No C4 downstream metrics.\"}\n    action_items:\n      - {round: 8, action: \"Covered in Limitations. No additional action.\", assigned_to: \"\", status: wont_fix}\n    resolution: \"Covered in Limitations. C4 OOD PPL at 30% + 50% already reported.\"\n    resolution_round: 8\n\n  - id: \"R8-I1\"\n    summary: \"Penalty controller lambda hits cap at 30% (actual 28.5%)\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W5 raise warning, R2 partial REBUT. Consensus: impact negligible.\"}\n      - {round: 9, reviewers: [1, 2], note: \"R1-W2 + R2-W2 reconfirm. Additionally R9 identifies Eq.5 vs Eq.6 formalization inconsistency (inequality vs equality constraint). Upgraded from info to warning.\"}\n    action_items:\n      - {round: 8, action: \"Already addressed in Appendix D with TEAL@28.5% comparison (<0.3 PPL).\", assigned_to: \"\", status: wont_fix}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W1\"\n    summary: \"Method novelty limited: mature techniques, MaskLLM overlap\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R2-N1 critical, R1 AGREE with nuance. Consensus: Findings-appropriate.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Reconfirmed as R9-N4. R2 must-fix, R1 agrees on substance but rebuts severity. Both agree: Findings, not Main.\"}\n    action_items:\n      - {round: 8, action: \"C1 finding provides new empirical novelty. Reframe Contribution 1 around mask pattern discovery.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper reframed around mask pattern discovery (commit 6abafc3). R9 acknowledges C1 value but still rates novelty as Findings-level.\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Statistical power: key comparisons partially single-seed\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 9\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Improved: 30% KL global 3-seed, 50% KL MMLU 3-seed.\"}\n      - {round: 8, reviewers: [1, 2], note: \"30% KL uniform now 3-seed. 40% still single seed.\"}\n      - {round: 9, reviewers: [1, 2], note: \"C1 ablation (core claim) only 2-seed at 50%, 1-seed at 30%. See R9-N1.\"}\n    action_items:\n      - {round: 8, action: \"30% uniform upgraded to 3-seed. C1 s123 in progress.\", assigned_to: \"\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # R8 issues resolved or not raised in R9\n  # ============================================================\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound: KL-derived masks as BCE targets ablation missing\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Full consensus.\"}\n      - {round: 9, reviewers: [1, 2], note: \"C1 ablation executed and reported. Original confound resolved. But R9 finds C1 itself has new issues (2-seed, soft-vs-hard confound) — tracked as R9-N1.\"}\n    action_items:\n      - {round: 8, action: \"C1 causal ablation executed (D059/D061).\", assigned_to: \"main_agent\", status: done}\n    resolution: \"RESOLVED by C1 ablation. New issues with C1 itself tracked as R9-N1.\"\n    resolution_round: 8\n\n  - id: \"R8-N3\"\n    summary: \"Three Operating Regions: only 3 data points, 40% single seed, boundaries unknown\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-N2 raise critical, R2 AGREE.\"}\n      - {round: 9, reviewers: [], note: \"Not specifically raised in R9 fresh review. Table 5 now has 6 sparsity levels (25-50%). 40% uniform still missing.\"}\n    action_items:\n      - {round: 8, action: \"Running 3 new sparsity points to expand from 3 to 6.\", assigned_to: \"main_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-N4\"\n    summary: \"\\\\enlargethispage format manipulation — desk reject risk\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R2-N3 critical.\"}\n      - {round: 9, reviewers: [], note: \"Confirmed removed. grep finds no \\\\enlargethispage in paper/*.tex.\"}\n    action_items:\n      - {round: 8, action: \"Remove \\\\enlargethispage.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Removed. Verified in R9.\"\n    resolution_round: 9\n\n  - id: \"R8-W2\"\n    summary: \"50% downstream collapse contradicts Abstract emphasis on 49% PPL advantage\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R2-W1, R1 AGREE.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Abstract now mentions collapse but narrative still leads with 50% PPL. R9 reconfirms as part of R9-N3.\"}\n    action_items:\n      - {round: 8, action: \"Abstract: give downstream collapse equal prominence.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Abstract line 5 mentions collapse, but R9 finds framing still biased toward 50% as highlight. Tracked in R9-N3.\"\n    resolution_round: null\n\n  - id: \"R8-W3\"\n    summary: \"BCE baseline missing at 30% (recommended operating point)\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W2, R2 AGREE.\"}\n      - {round: 9, reviewers: [1, 2], note: \"BCE 30% now in Table 1 (PPL 11.25). But R9 identifies broader issue: BCE pipelines differ at 30% vs 50%. See R9-N2.\"}\n    action_items:\n      - {round: 8, action: \"bce_30pct_s42_eval RUNNING.\", assigned_to: \"main_agent\", status: in_progress}\n    resolution: \"BCE 30% added. But pipeline inconsistency across sparsity levels remains — tracked as R9-N2.\"\n    resolution_round: null\n\n  - id: \"R8-W5\"\n    summary: \"SNR analysis only to step 300 (30% of training)\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W4, R2 AGREE.\"}\n      - {round: 9, reviewers: [], note: \"Not raised in R9 fresh review.\"}\n    action_items:\n      - {round: 8, action: \"Add caveat about 300-step window.\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W6\"\n    summary: \"No actual inference speedup; Introduction should set expectations\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Full AGREE.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Intro now disclaims speedup. R9 reconfirms as part of R9-N3 (combined with narrow usable range).\"}\n    action_items:\n      - {round: 8, action: \"Add speedup disclaimer in Introduction.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Intro L17 disclaims speedup. R9 acknowledges honest scope but incorporates into broader R9-N3.\"\n    resolution_round: 8\n\n  - id: \"R8-I2\"\n    summary: \"Minor: Table 2 PPL inconsistency, label cross-ref, Figure placeholder\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Collection of minor issues.\"}\n      - {round: 9, reviewers: [1], note: \"R1-M5 identifies Table 1 mixed statistical reporting (MMLU 3-seed but GSM8K single-seed in same row). Folded into R9-I1.\"}\n    action_items:\n      - {round: 8, action: \"Paper Agent reframe addressed number consistency.\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Fully resolved prior issues (compact)\n  # ============================================================\n\n  - id: \"R2-N1\"\n    summary: \"Limitations section format\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Fixed Round 1\"\n    resolution_round: 1\n\n  - id: \"R6-N1\"\n    summary: \"KL+compensation control experiment\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Done: 30% 2-seed + 50% identical.\"\n    resolution_round: 7\n\n  - id: \"R3-C3\"\n    summary: \"No wall-clock speedup, efficiency framing\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    resolution: \"Reframed as understanding paper. Intro disclaims speedup.\"\n    resolution_round: 7\n\n  - id: \"R3-S2\"\n    summary: \"BCE vs KL comparison is pipeline difference\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: \"Resolved via R8-N1. C1 full-spectrum ablation confirms target quality > coupling.\"\n    resolution_round: 8\n\n  - id: \"R3-C2\"\n    summary: \"PPL-downstream disconnect\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: \"Abstract gives downstream collapse equal prominence. 14B MMLU gap stated.\"\n    resolution_round: 8\n\n  - id: \"R3-S1\"\n    summary: \"Core novelty vs MaskLLM distinction insufficient\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: \"Resolved via R8-W1. Mask pattern discovery reframe.\"\n    resolution_round: 8\n\n  - id: \"R7-W2\"\n    summary: \"\\\\enlargethispage format manipulation\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: \"Removed. Verified in R9.\"\n    resolution_round: 9\n\n  - id: \"R7-N1\"\n    summary: \"14B MMLU reversal exposes limitation\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: \"Resolved via R8-N2. Abstract/Intro state limitation.\"\n    resolution_round: 8\n"
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
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 9 (fresh review) findings\n  # ============================================================\n\n  - id: \"R9-N1\"\n    summary: \"C1 causal ablation: 2-seed insufficient for 'proves' claim + soft-vs-hard mask confound uncontrolled\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1 raised as Must-Fix N1 (2-seed + soft-vs-hard confound + 30% PPL gap). R2 initially Should-Fix W1, upgraded to AGREE with R1 in cross-response. Full consensus: C1 is core claim but evidence insufficient.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-N2\"\n    summary: \"BCE baseline pipeline inconsistent across sparsity levels: 30% uses TEAL/no-comp, 50% uses DejaVu+comp/no-TEAL\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1 raised as Must-Fix N3. R2 missed in initial review, AGREE in cross-response. Missing key baseline: 50% BCE + TEAL global (no comp).\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-N3\"\n    summary: \"Narrow usable range (only 30%, ~2pp downstream gain) + 50% framing bias in Abstract + no wall-clock speedup (+6.4% overhead)\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1-N4 + R2-N2 + R2-N3 converged. Both agree 50% PPL headline misleading given downstream collapse. R1 rates no-speedup as should-fix (honest scope), R2 rates must-fix. Consensus: framing needs rebalancing toward 30%.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-N4\"\n    summary: \"Method novelty insufficient for Main: KL+Gumbel+predictor = existing components, MaskLLM overlap\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R2 raised as Must-Fix N1. R1 REBUT on severity (empirical finding has value for Findings, novelty not fixable) but AGREE on substance. Consensus: Findings-appropriate, not Main.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W1\"\n    summary: \"PPL degradation 18% wording mismatch: text says 'reduces PPL degradation' but calculates relative PPL improvement\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1], note: \"R1-W3. R2 did not raise. Factual mismatch in Abstract line 4.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W2\"\n    summary: \"Mistral-7B missing all downstream evaluation; cross-arch claim based on PPL only\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1], note: \"R1-W4. Given 14B PPL-vs-downstream reversal, Mistral PPL-only evidence insufficient for cross-arch generalization claim.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W3\"\n    summary: \"Eq.5 defines inequality constraint but Eq.6 uses absolute value (equality constraint); formalization inconsistent\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1-W2. R2 AGREE in cross-response.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W4\"\n    summary: \"Training data ablation missing: all predictors trained on ~8M tokens WikiText-103, domain specificity of KL masks unknown\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1-W1 + R2-W4 converged. C4 OOD shows 1.46x->1.74x degradation. No C4-trained predictor comparison.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-I1\"\n    summary: \"Minor writing/format issues: -ing phrases (~15), float spacing compression, Ethics missing Qwen-14B, Gumbel citation priority, forward KL terminology\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R2-W5 (-ing phrases, R1 rebuts as minor), R2-M1/M2/M3/M4/M5, R1-M1/M2/M3/M4/M5 collected.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Recurring issues from prior rounds (updated with R9 status)\n  # ============================================================\n\n  - id: \"R8-N2\"\n    summary: \"14B MMLU reversal: KL PPL best (7.62) but MMLU -8.1pp vs TEAL, contradicts output-preservation narrative\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-N3 + R2-N2, full AGREE. Abstract 'confirms across 7-14B' is selective reporting.\"}\n      - {round: 9, reviewers: [1, 2], note: \"R1-N2 + R2-W3 reconfirmed. R1 notes BCE MMLU=71.67 normal at 14B, problem specific to KL coupled training. Abstract now states gap but no mechanism explanation. Both AGREE must-fix.\"}\n    action_items:\n      - {round: 8, action: \"Restrict Abstract/Intro scope to 7-8B primary; 14B as exploratory/mixed.\", assigned_to: \"paper_agent\", status: done}\n      - {round: 8, action: \"14B additional analysis: NOT doing.\", assigned_to: \"\", status: wont_fix}\n    resolution: \"Paper reframed with explicit 14B gap statement, but R9 finds discussion still insufficient — no mechanism hypothesis provided.\"\n    resolution_round: null\n\n  - id: \"R8-W4\"\n    summary: \"Training/eval domain overlap: WikiText-103 to WikiText-2, C4 OOD limited\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W3 + R2-W2, full AGREE.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Reconfirmed as R9-W4. C4 30% PPL 1.74x dense (vs in-domain 1.46x). No C4 downstream metrics.\"}\n    action_items:\n      - {round: 8, action: \"Covered in Limitations. No additional action.\", assigned_to: \"\", status: wont_fix}\n    resolution: \"Covered in Limitations. C4 OOD PPL at 30% + 50% already reported.\"\n    resolution_round: 8\n\n  - id: \"R8-I1\"\n    summary: \"Penalty controller lambda hits cap at 30% (actual 28.5%)\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W5 raise warning, R2 partial REBUT. Consensus: impact negligible.\"}\n      - {round: 9, reviewers: [1, 2], note: \"R1-W2 + R2-W2 reconfirm. Additionally R9 identifies Eq.5 vs Eq.6 formalization inconsistency (inequality vs equality constraint). Upgraded from info to warning.\"}\n    action_items:\n      - {round: 8, action: \"Already addressed in Appendix D with TEAL@28.5% comparison (<0.3 PPL).\", assigned_to: \"\", status: wont_fix}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W1\"\n    summary: \"Method novelty limited: mature techniques, MaskLLM overlap\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R2-N1 critical, R1 AGREE with nuance. Consensus: Findings-appropriate.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Reconfirmed as R9-N4. R2 must-fix, R1 agrees on substance but rebuts severity. Both agree: Findings, not Main.\"}\n    action_items:\n      - {round: 8, action: \"C1 finding provides new empirical novelty. Reframe Contribution 1 around mask pattern discovery.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper reframed around mask pattern discovery (commit 6abafc3). R9 acknowledges C1 value but still rates novelty as Findings-level.\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Statistical power: key comparisons partially single-seed\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 9\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Improved: 30% KL global 3-seed, 50% KL MMLU 3-seed.\"}\n      - {round: 8, reviewers: [1, 2], note: \"30% KL uniform now 3-seed. 40% still single seed.\"}\n      - {round: 9, reviewers: [1, 2], note: \"C1 ablation (core claim) only 2-seed at 50%, 1-seed at 30%. See R9-N1.\"}\n    action_items:\n      - {round: 8, action: \"30% uniform upgraded to 3-seed. C1 s123 in progress.\", assigned_to: \"\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # R8 issues resolved or not raised in R9\n  # ============================================================\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound: KL-derived masks as BCE targets ablation missing\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Full consensus.\"}\n      - {round: 9, reviewers: [1, 2], note: \"C1 ablation executed and reported. Original confound resolved. But R9 finds C1 itself has new issues (2-seed, soft-vs-hard confound) — tracked as R9-N1.\"}\n    action_items:\n      - {round: 8, action: \"C1 causal ablation executed (D059/D061).\", assigned_to: \"main_agent\", status: done}\n    resolution: \"RESOLVED by C1 ablation. New issues with C1 itself tracked as R9-N1.\"\n    resolution_round: 8\n\n  - id: \"R8-N3\"\n    summary: \"Three Operating Regions: only 3 data points, 40% single seed, boundaries unknown\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-N2 raise critical, R2 AGREE.\"}\n      - {round: 9, reviewers: [], note: \"Not specifically raised in R9 fresh review. Table 5 now has 6 sparsity levels (25-50%). 40% uniform still missing.\"}\n    action_items:\n      - {round: 8, action: \"Running 3 new sparsity points to expand from 3 to 6.\", assigned_to: \"main_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-N4\"\n    summary: \"\\\\enlargethispage format manipulation — desk reject risk\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R2-N3 critical.\"}\n      - {round: 9, reviewers: [], note: \"Confirmed removed. grep finds no \\\\enlargethispage in paper/*.tex.\"}\n    action_items:\n      - {round: 8, action: \"Remove \\\\enlargethispage.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Removed. Verified in R9.\"\n    resolution_round: 9\n\n  - id: \"R8-W2\"\n    summary: \"50% downstream collapse contradicts Abstract emphasis on 49% PPL advantage\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R2-W1, R1 AGREE.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Abstract now mentions collapse but narrative still leads with 50% PPL. R9 reconfirms as part of R9-N3.\"}\n    action_items:\n      - {round: 8, action: \"Abstract: give downstream collapse equal prominence.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Abstract line 5 mentions collapse, but R9 finds framing still biased toward 50% as highlight. Tracked in R9-N3.\"\n    resolution_round: null\n\n  - id: \"R8-W3\"\n    summary: \"BCE baseline missing at 30% (recommended operating point)\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W2, R2 AGREE.\"}\n      - {round: 9, reviewers: [1, 2], note: \"BCE 30% now in Table 1 (PPL 11.25). But R9 identifies broader issue: BCE pipelines differ at 30% vs 50%. See R9-N2.\"}\n    action_items:\n      - {round: 8, action: \"bce_30pct_s42_eval RUNNING.\", assigned_to: \"main_agent\", status: in_progress}\n    resolution: \"BCE 30% added. But pipeline inconsistency across sparsity levels remains — tracked as R9-N2.\"\n    resolution_round: null\n\n  - id: \"R8-W5\"\n    summary: \"SNR analysis only to step 300 (30% of training)\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W4, R2 AGREE.\"}\n      - {round: 9, reviewers: [], note: \"Not raised in R9 fresh review.\"}\n    action_items:\n      - {round: 8, action: \"Add caveat about 300-step window.\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W6\"\n    summary: \"No actual inference speedup; Introduction should set expectations\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Full AGREE.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Intro now disclaims speedup. R9 reconfirms as part of R9-N3 (combined with narrow usable range).\"}\n    action_items:\n      - {round: 8, action: \"Add speedup disclaimer in Introduction.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Intro L17 disclaims speedup. R9 acknowledges honest scope but incorporates into broader R9-N3.\"\n    resolution_round: 8\n\n  - id: \"R8-I2\"\n    summary: \"Minor: Table 2 PPL inconsistency, label cross-ref, Figure placeholder\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Collection of minor issues.\"}\n      - {round: 9, reviewers: [1], note: \"R1-M5 identifies Table 1 mixed statistical reporting (MMLU 3-seed but GSM8K single-seed in same row). Folded into R9-I1.\"}\n    action_items:\n      - {round: 8, action: \"Paper Agent reframe addressed number consistency.\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Fully resolved prior issues (compact)\n  # ============================================================\n\n  - id: \"R2-N1\"\n    summary: \"Limitations section format\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Fixed Round 1\"\n    resolution_round: 1\n\n  - id: \"R6-N1\"\n    summary: \"KL+compensation control experiment\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Done: 30% 2-seed + 50% identical.\"\n    resolution_round: 7\n\n  - id: \"R3-C3\"\n    summary: \"No wall-clock speedup, efficiency framing\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    resolution: \"Reframed as understanding paper. Intro disclaims speedup.\"\n    resolution_round: 7\n\n  - id: \"R3-S2\"\n    summary: \"BCE vs KL comparison is pipeline difference\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: \"Resolved via R8-N1. C1 full-spectrum ablation confirms target quality > coupling.\"\n    resolution_round: 8\n\n  - id: \"R3-C2\"\n    summary: \"PPL-downstream disconnect\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: \"Abstract gives downstream collapse equal prominence. 14B MMLU gap stated.\"\n    resolution_round: 8\n\n  - id: \"R3-S1\"\n    summary: \"Core novelty vs MaskLLM distinction insufficient\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: \"Resolved via R8-W1. Mask pattern discovery reframe.\"\n    resolution_round: 8\n\n  - id: \"R7-W2\"\n    summary: \"\\\\enlargethispage format manipulation\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: \"Removed. Verified in R9.\"\n    resolution_round: 9\n\n  - id: \"R7-N1\"\n    summary: \"14B MMLU reversal exposes limitation\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: \"Resolved via R8-N2. Abstract/Intro state limitation.\"\n    resolution_round: 8\n"
  }
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-19T01:54:59.587442+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 16949}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-19T01:57:56.539807+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "report": "# Round 9 Consolidated Review Report (Fresh)\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 格式合规)\n**审稿模式**: Fresh (无先前轮次记忆)\n\n---\n\n## Summary\n\n论文提出用 KL 散度（替代标准 BCE）训练 SwiGLU LLM 的上下文稀疏性预测器，通过 Gumbel-Sigmoid relaxation 实现可微分 mask 优化。核心实证发现是 KL 训练的 mask 与 magnitude-based mask 有 68% 的差异，且因果消融（C1）表明 mask 目标质量（而非梯度耦合）驱动质量优势。在 LLaMA-3.1-8B 上，KL 在 30% 和 50% 稀疏度下 PPL 分别优于 TEAL 18% 和 49%，但 50% 下游任务全面崩溃至接近随机水平，14B 规模出现 MMLU 反转（-8.1pp vs TEAL）。\n\n---\n\n## Strengths\n\n**S1. C1 因果消融设计精巧** [R1+R2 共识]\n将 mask target quality 与 gradient coupling 解耦的实验设计值得肯定。BCE 在 KL-derived targets 上复现 KL 质量（50% max Δ=0.59pp），而 magnitude-based BCE 为 28.13±0.20，有力地表明 mask patterns 是主要驱动力。这是论文最有价值的贡献。\n\n**S2. 全面系统的消融研究** [R1+R2 共识]\nAblation 覆盖 divergence direction（Forward KL > JSD +6.4% > Reverse KL +8.6%）、relaxation（Gumbel vs STE, 34.5%）、compensation redundancy、loss isolation、超参数鲁棒性（$d_b$, $\\tau$, training steps），形成完整矩阵。Regime analysis（Table 5）的非单调 allocation 偏好提供实践指导。\n\n**S3. 诚实的 Scope 界定** [R1+R2 共识]\nIntroduction 明确声明 \"Our contribution is empirical\" 和 \"Wall-clock speedup requires sparse kernel support not addressed here\"；14B MMLU gap、50% downstream collapse 均被报告。这种透明度值得赞赏。\n\n**S4. 方法公式化简洁正确** [R1]\nGumbel-Sigmoid relaxation 是 Binary Concrete distribution 的正确应用；forward KL objective 推导无误；predictor 架构轻量（<1% base params）且不需推理时 compensation network。\n\n**S5. 写作整体干净** [R2, R1 同意]\n无 em-dash/en-dash AI 痕迹。术语首次出现时有定义。全文主线（mask pattern discovery → causal ablation → practical implications）连贯。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. C1 因果消融的声明力度与证据强度严重不匹配** [R1 Must-Fix, R2 升级同意]\n- C1 是论文最核心贡献（Abstract/Intro/Conclusion 反复引用 \"causal ablation confirms/proves\"），但仅 2-seed 验证（50%: s42+s123; 30%: 仅 s42）。核心 claim 的统计验证反而弱于常规实验（主实验 3-seed）。\n- 30% 条件下 C1 PPL gap（9.45 vs 8.82 = +7.1%）与 97.5% mask agreement 不相称，暗示 gradient coupling 在低稀疏度可能仍有残余贡献，与 \"across the full sparsity range\" 的声明矛盾。\n- **R1 新发现的混淆变量**（R2 在交叉回应中确认）：KL predictor 训练时使用 soft Gumbel-Sigmoid masks（连续放松），C1 的 BCE predictor 使用 hard binary targets。C1 不仅改变了 gradient coupling，也改变了训练时的 mask 特性（soft vs hard），未完全 disentangle。\n- **影响**：如果 C1 evidence 不充分，论文贡献降级为 \"KL 比 BCE 好\" 这个较 incremental 的发现。\n- **建议**：增加到至少 5-seed；降级措辞为 \"provides evidence\" 而非 \"proves\"；讨论 30% gradient coupling 残余贡献；讨论 soft-vs-hard confound 作为 C1 设计局限。\n\n**N2. 14B 规模 downstream 全面反转，削弱泛化声明** [R1 Must-Fix, R2 Must-Fix（W3→升级）]\n- Qwen-2.5-14B 30%: KL PPL 最优（7.62 vs TEAL 8.73）但 MMLU 63.7% vs TEAL 71.8%（-8.1pp）、vs BCE 71.7%（-8.0pp）。ARC-c、GSM8K 上 KL 也均低于 BCE。Uniform allocation 同样趋势（64.49 vs 66.34）。\n- BCE 使用 magnitude-based masks 在 14B 上 MMLU 正常（71.67%），问题特定于 KL 的 coupled training——直接质疑 \"KL discovers superior mask patterns\" 的核心叙事：在 14B 上 KL 的 mask patterns 对 MMLU 是 **有害** 的。\n- Abstract \"confirms the PPL advantage across 7-14B\" 轻描淡写 downstream degradation。正文仅半句带过（§4.5），无任何机制解释。\n- **建议**：正文（非仅 Appendix）充分讨论 14B reversal（至少一段）；提出可检验的机制假设；将 Abstract 改为明确表述 downstream reversal。\n\n**N3. BCE baseline 在不同稀疏度使用不同实验管线，跨 sparsity 比较不可靠** [R1 Must-Fix, R2 交叉确认]\n- 30% BCE（Table 1 $^\\dagger$）：TEAL global allocation, no compensation, 2700 steps → PPL 11.25\n- 50% BCE（Table 1 $^\\ast$）：DejaVu pipeline + compensation (+67.2M params), no TEAL allocation → PPL 28.13±0.20\n- **关键遗漏**：没有 \"50% BCE + TEAL global (no compensation)\" baseline——这才是与 50% KL global 最直接可比的设置。\n- Table 4 \"BCE + Compensation\" PPL=25.44 vs \"BCE (no comp)\" PPL=27.97，差距 2.53，说明 compensation 对 BCE 有显著影响。但两者是否均使用 TEAL allocation 未明确标注。\n- **影响**：Baseline 公平性是实验驱动论文的生命线。读者无法判断 KL 优势有多少来自 objective、多少来自 allocation strategy 差异。\n- **建议**：增加 \"50% BCE + TEAL global (no comp)\" baseline；统一管线；Table 1 caption 更显著标注差异。\n\n**N4. 实际可用操作区间极窄 + Abstract framing 偏向 50%** [R1 Must-Fix, R2 Must-Fix (N2+N3)]\n- **50%**：MMLU 28.1±0.2%（≈random 25%），GSM8K <2.2%——论文自己确认 \"capacity-limited regime\"。KL 的 49% PPL 优势在 downstream 上完全无法体现。\n- **30%**：KL uniform PPL 8.81 vs TEAL 10.97（18%）。但 downstream 差异很小——MMLU +2.1pp, ARC-c +1.4pp, GSM8K -0.4pp（TEAL 更好）。考虑 3-seed σ，多数差异不显著。\n- **无实际加速**：当前实现增加 6.4% 延迟（126.78 vs 119.11 ms/forward）。即使 30% PPL 改进也没有对应的 wall-clock benefit。未验证 KL masks 是否兼容 N:M structured sparsity。\n- Abstract 叙事高潮放在 \"At 50%, the PPL advantage widens to 49%\"，但 50% 是 downstream-dead zone。\n- **建议**：将叙事重心转向 30% downstream-preserved quality；坦诚讨论 30% 的 modest downstream improvement；补充 N:M 兼容性讨论或初步实验。\n\n**N5. 方法新颖性不足以支撑 Main Conference** [R2 Must-Fix, R1 同意实质但 REBUT 定级]\n- 核心方法 = KL distillation (Hinton 2015) + Gumbel-Sigmoid (Jang 2017) + per-layer MLP predictor (DejaVu 2023)。每个组件均为成熟技术。\n- MaskLLM (NeurIPS 2024) 已组合 frozen weights + learnable masks + KL + Gumbel relaxation。论文声称的三点区别（activation vs weight sparsity, predictor vs learnable params, global vs N:M）是应用场景切换，非方法论创新。\n- Table 2 taxonomy 填充一个 \"Per-token × Coupled\" 空白格，学术贡献有限。\n- **共识**：两位 Reviewer 均认为论文适合 Findings track。C1 empirical finding 有价值，但方法本身缺乏足够创新支撑 Main。R1 指出新颖性不可 \"fix\"，属于定位问题而非缺陷。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. PPL degradation 措辞与计算方式不匹配** [R1]\n- Abstract \"KL reduces PPL degradation 18% over TEAL\"：语义上应指缩小 dense-to-sparse gap（= 41%），实际计算是 relative PPL improvement (10.97-8.96)/10.97 = 18%。\n- 建议统一为 \"reduces PPL by 18% relative to TEAL\"。\n\n**W2. Mistral-7B 缺少全部 downstream 评估** [R1, R2 交叉确认]\n- Table 8 (Appendix G) 仅报告 PPL。鉴于 14B 出现 PPL↑但 MMLU↓ 的反转，Mistral PPL-only 不能支撑跨架构泛化声明。\n- 建议补充至少 MMLU 和 ARC-c。\n\n**W3. Adaptive penalty Eq.5/6 形式化不一致** [R1, R2 交叉确认]\n- Eq. 5 定义不等式约束 $\\bar{s} \\leq 1-\\rho$，Eq. 6 使用绝对值 $|\\bar{s}-(1-\\rho)|$（等式约束）。实际上等式约束更合理，但推导应保持一致。\n- 30% target actual sparsity 28.5%（5% deviation），interpolated TEAL baseline 未实际测量。\n\n**W4. 训练数据消融缺失** [R1+R2 共识]\n- 所有 predictor 在 WikiText-103 上训练（~8M tokens），主要评估在 WikiText-2（同域）。C4 OOD 显示 degradation 从 1.46× 恶化到 1.74× dense。\n- KL-discovered mask patterns 的 domain specificity 未知。缺少 C4-trained predictor 对比。\n\n**W5. SPON 边际贡献（2.4%）在方法中位置偏重** [R1, R2 部分 REBUT]\n- 仅 2.4% PPL improvement，cosine similarity 0.196, R²=0.038。R1 建议标注为可选组件；R2 认为 Related Work 段落是必要 positioning。\n- 共识：不需要移除，但可以在 ablation 中更突出其边际性。\n\n### Minor（不影响接收）\n\n**M1.** -ing 分词短语偏多（~15 处），部分可改写（如 \"enabling...discover\" → 拆分独立句）。R1 认为不构成系统问题，R2 认为应 fix。[轻微分歧]\n**M2.** Float spacing 被手动压缩（`\\textfloatsep{8pt}`），conclusion 有 `\\vspace{-4pt}`——不违规但暗示空间紧张。\n**M3.** Ethics 声明遗漏 Qwen-2.5-14B（仅提 LLaMA-8B 和 Mistral-7B）。\n**M4.** §3.3 Gumbel-Sigmoid 应优先引用 Concrete distribution (Maddison 2017) 和 L₀ (Louizos 2018)，而非 Gumbel-Softmax (Jang 2017)。\n**M5.** §3.4 \"mean-seeking\" 术语不标准，应为 \"mass-covering\" 或 \"inclusive\"。\n**M6.** §3.6 Jacobian 形式化应为 $\\partial \\mathbf{z}/\\partial \\tilde{m}_j$（对 mask），非 $\\partial \\mathbf{z}/\\partial \\mathbf{h}$（对 hidden state）。R2 认为 suggestive analysis 不需完整形式化。\n**M7.** Table 1 同行混合不同统计报告（MMLU 3-seed 带 ±，GSM8K 单 seed 无 ±），易造成混淆。\n**M8.** Table 4 SPON 脚注使用 `evaluate.py` 而非 unified benchmark，数值可比性需说明。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n| 议题 | 共识 |\n|------|------|\n| C1 ablation 2-seed 不够 | 两位均同意，核心 claim 需更强统计支撑 |\n| Soft-vs-hard mask confound | R1 发现，R2 交叉确认 |\n| 14B downstream reversal 需讨论 | 两位均 Must-Fix |\n| BCE pipeline 不一致 | R1 发现，R2 交叉确认（Round 1 遗漏） |\n| 50% downstream 崩溃 + framing 偏差 | 两位一致 |\n| 无 wall-clock speedup | 两位一致（定级有分歧，见下） |\n| 方法新颖性 → Findings 级别 | 两位结论一致 |\n| Overall 3.0 (Findings) | 完全一致 |\n\n## Reviewer Divergence [REBUT]\n\n| 议题 | R1 | R2 | 状态 |\n|------|----|----|------|\n| Wall-clock speedup 定级 | Should-fix（论文已诚实 scope） | Must-fix | 不影响评分 |\n| 方法新颖性定级 | 属于定位问题非缺陷 | Must-fix | 不影响评分（都认为 Findings） |\n| -ing 短语 | 不构成问题 | Should-fix | Minor 分歧 |\n| Predictor 架构比较 | Should-fix | 不需要（贡献在 objective） | Minor 分歧 |\n| §3.6 Jacobian 形式化 | Minor issue | 不需修改（suggestive analysis） | Minor 分歧 |\n\n**分歧评估**：所有分歧仅涉及问题定级（must-fix vs should-fix, should-fix vs minor），不涉及问题是否存在。核心判断完全一致。无需进入 Round 2。\n\n---\n\n## Questions for Authors\n\n**Q1** [R1+R2 共识]: C1 ablation 的 \"KL-derived oracle masks\" 具体如何生成？从哪个 checkpoint（step）、哪个 seed 的 KL predictor 提取？用另一个 seed 的 KL predictor 生成 masks 是否会得到不同 C1 结果？\n\n**Q2** [R1+R2 共识]: 14B MMLU reversal 是否在多个 seed 上验证？Table 7 仅报告 seed 42。如果该 reversal 在不同 seed 间不稳定，可能只是噪声。\n\n**Q3** [R1+R2 共识]: 30% sparsity 下 KL 的 actual sparsity 为 28.5%（Table 6）。Table 1 的 TEAL baseline 是在 exact 30% 还是也有偏差？如果 KL 在 28.5% 而 TEAL 在 30%，那 KL 的一部分 PPL 优势来自剪枝更少的 neurons。\n\n**Q4** [R1]: 为什么没有报告 \"50% BCE + TEAL global (no compensation)\" 的结果？这是与 KL global 最直接可比的 baseline。\n\n**Q5** [R1]: 在 C4 上训练 predictor 时，mask divergence from magnitude 的幅度是否类似？KL masks 的 domain specificity 有多大？\n\n**Q6** [R2]: 50% downstream collapse 下 KL MMLU (28.1%) 与 TEAL (28.32%) 差异在 noise range 内。如果 downstream 是最终目标且 30% 是推荐操作点，为何以 50% PPL improvement 而非 30% downstream preservation 作为核心叙事？\n\n---\n\n## Missing References\n\n**应引用** [R1+R2 共识]:\n1. **Enabling Dynamic Sparsity in Quantized LLMs** (2025, arXiv 2511.04477) — 量化 + activation sparsity 协同设计\n2. **Mixture of Neuron Experts** (2025, arXiv 2510.05781) — neuron-level MoE 转换，与 D2DMoE 互补\n\n**可选引用** [有分歧]:\n3. SeerAttention (2024) — R2 建议, R1 REBUT（attention sparsity vs FFN sparsity，已有 Polar Sparsity 覆盖）\n4. DeepSeek-V3/DeepSeekMoE — R2 建议, R1 REBUT（native MoE 架构，非 dense→sparse 问题）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。项目 `external_review.paperreview_ai.enabled` 未启用。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n### 支撑 Findings 接收的理由\n\n1. **C1 因果消融**是有价值的 empirical finding——mask target quality > gradient coupling 在文献中没有先例，即使统计效力需加强，方向和设计都值得发表。\n2. **Regime analysis**（非单调 allocation 偏好）对实践者有指导意义，Table 5 的 6-level 数据提供了有用参考。\n3. **68% mask divergence** 从 magnitude ranking 是非显而易见的发现，揭示了 KL 训练发现了不同的 neuron importance landscape。\n4. 方法公式化简洁正确，消融系统全面，写作清晰诚实。\n\n### 阻碍 Main Conference 接收的理由\n\n1. **方法新颖性有限**：KL + Gumbel + predictor 均为成熟组件的直接组合，MaskLLM 已在高度类似的框架下发表。\n2. **C1 核心 claim 证据不充分**：\"causal ablation proves\" 仅 2-seed，存在 soft-vs-hard confound，30% PPL gap 暗示 gradient coupling 残余贡献。\n3. **14B downstream reversal**未被充分讨论，直接质疑方法的 scalability。\n4. **实际可用范围极窄**：50% downstream 全面崩溃，30% 的 downstream 改进仅 ~2pp（多数不显著），无 wall-clock 加速。\n5. **BCE baseline pipeline 不一致**使跨 sparsity 比较不可靠。\n\n### 升级到 3.5 (Borderline Conference) 的路径\n\n若能修复以下问题，可考虑升级：\n- **N1**: C1 增加到 5-seed + 降级 \"proves\" 措辞 + 讨论 soft-vs-hard confound\n- **N2**: 正文充分讨论 14B reversal + 提供机制假设\n- **N3**: 增加 \"50% BCE + TEAL global (no comp)\" baseline\n- **N4**: 将叙事重心从 50% PPL 转向 30% downstream quality\n\n---\n\n## Detailed Comments (Per-Section)\n\n### Abstract\n- 第 2 行 \"causal ablation confirms\" → 降级为 \"ablation provides evidence\"\n- 第 4 行 \"reduces PPL degradation 18%\" → 改为 \"reduces PPL by 18% relative to TEAL\"（措辞与计算不匹配）\n- 第 5 行 50% PPL 作为叙事高潮但 downstream 已崩溃 → 将 30% downstream quality 放在更突出位置\n- 第 6 行 \"confirms PPL advantage across 7-14B\" → 必须同等突出 downstream reversal\n\n### Introduction\n- L10 \"a causal ablation confirms\" → 降级措辞\n- L10-11 \"the primary quality driver\" → 加 caveat：30% 条件下可能有残余 gradient coupling 贡献\n- L16 14B 提及过于简略 → 增加 1-2 句讨论 downstream reversal 的含义\n\n### Method\n- §3.3 优先引用 Concrete distribution (Maddison 2017) 和 L₀ (Louizos 2018)\n- §3.4 \"mean-seeking\" → \"mass-covering\" 或 \"inclusive\"\n- §3.5 Eq. 5 vs Eq. 6 约束类型统一\n- §3.6 Jacobian 表述修正；\"suggestive\" 定位保持\n\n### Experiments\n- Table 1: 统一 30% 和 50% BCE 使用相同推理管线；增加 50% BCE+TEAL global baseline\n- Table 1: 统一同行的统计报告格式（避免 MMLU 有 ± 而 GSM8K 无）\n- Table 3: C1 增加 seed 数量；添加 confidence intervals\n- §4.4 最后一段: 讨论 30% PPL gap 与 gradient coupling 的可能联系\n- §4.5: 增加至少 1 段 14B reversal 的机制讨论\n- §4.5: 补充 Mistral-7B downstream evaluation\n\n### Related Work\n- 增加 Enabling Dynamic Sparsity in Quantized LLMs (2025) 和 Mixture of Neuron Experts (2025)\n\n### Conclusion\n- 第 1 行 \"confirms target quality, not gradient coupling\" → 降级措辞\n\n### Limitations\n- 已较完善。可增加：C1 的 soft-vs-hard confound 作为方法论局限。\n\n### Ethics\n- 补充 Qwen-2.5-14B 模型引用和 license 信息。\n\n### Appendix\n- Table 4 SPON 脚注: 说明 evaluate.py vs unified benchmark 的数值差异影响。",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)"
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
    "report": "# Round 9 Consolidated Review Report (Fresh)\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 格式合规)\n**审稿模式**: Fresh (无先前轮次记忆)\n\n---\n\n## Summary\n\n论文提出用 KL 散度（替代标准 BCE）训练 SwiGLU LLM 的上下文稀疏性预测器，通过 Gumbel-Sigmoid relaxation 实现可微分 mask 优化。核心实证发现是 KL 训练的 mask 与 magnitude-based mask 有 68% 的差异，且因果消融（C1）表明 mask 目标质量（而非梯度耦合）驱动质量优势。在 LLaMA-3.1-8B 上，KL 在 30% 和 50% 稀疏度下 PPL 分别优于 TEAL 18% 和 49%，但 50% 下游任务全面崩溃至接近随机水平，14B 规模出现 MMLU 反转（-8.1pp vs TEAL）。\n\n---\n\n## Strengths\n\n**S1. C1 因果消融设计精巧** [R1+R2 共识]\n将 mask target quality 与 gradient coupling 解耦的实验设计值得肯定。BCE 在 KL-derived targets 上复现 KL 质量（50% max Δ=0.59pp），而 magnitude-based BCE 为 28.13±0.20，有力地表明 mask patterns 是主要驱动力。这是论文最有价值的贡献。\n\n**S2. 全面系统的消融研究** [R1+R2 共识]\nAblation 覆盖 divergence direction（Forward KL > JSD +6.4% > Reverse KL +8.6%）、relaxation（Gumbel vs STE, 34.5%）、compensation redundancy、loss isolation、超参数鲁棒性（$d_b$, $\\tau$, training steps），形成完整矩阵。Regime analysis（Table 5）的非单调 allocation 偏好提供实践指导。\n\n**S3. 诚实的 Scope 界定** [R1+R2 共识]\nIntroduction 明确声明 \"Our contribution is empirical\" 和 \"Wall-clock speedup requires sparse kernel support not addressed here\"；14B MMLU gap、50% downstream collapse 均被报告。这种透明度值得赞赏。\n\n**S4. 方法公式化简洁正确** [R1]\nGumbel-Sigmoid relaxation 是 Binary Concrete distribution 的正确应用；forward KL objective 推导无误；predictor 架构轻量（<1% base params）且不需推理时 compensation network。\n\n**S5. 写作整体干净** [R2, R1 同意]\n无 em-dash/en-dash AI 痕迹。术语首次出现时有定义。全文主线（mask pattern discovery → causal ablation → practical implications）连贯。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. C1 因果消融的声明力度与证据强度严重不匹配** [R1 Must-Fix, R2 升级同意]\n- C1 是论文最核心贡献（Abstract/Intro/Conclusion 反复引用 \"causal ablation confirms/proves\"），但仅 2-seed 验证（50%: s42+s123; 30%: 仅 s42）。核心 claim 的统计验证反而弱于常规实验（主实验 3-seed）。\n- 30% 条件下 C1 PPL gap（9.45 vs 8.82 = +7.1%）与 97.5% mask agreement 不相称，暗示 gradient coupling 在低稀疏度可能仍有残余贡献，与 \"across the full sparsity range\" 的声明矛盾。\n- **R1 新发现的混淆变量**（R2 在交叉回应中确认）：KL predictor 训练时使用 soft Gumbel-Sigmoid masks（连续放松），C1 的 BCE predictor 使用 hard binary targets。C1 不仅改变了 gradient coupling，也改变了训练时的 mask 特性（soft vs hard），未完全 disentangle。\n- **影响**：如果 C1 evidence 不充分，论文贡献降级为 \"KL 比 BCE 好\" 这个较 incremental 的发现。\n- **建议**：增加到至少 5-seed；降级措辞为 \"provides evidence\" 而非 \"proves\"；讨论 30% gradient coupling 残余贡献；讨论 soft-vs-hard confound 作为 C1 设计局限。\n\n**N2. 14B 规模 downstream 全面反转，削弱泛化声明** [R1 Must-Fix, R2 Must-Fix（W3→升级）]\n- Qwen-2.5-14B 30%: KL PPL 最优（7.62 vs TEAL 8.73）但 MMLU 63.7% vs TEAL 71.8%（-8.1pp）、vs BCE 71.7%（-8.0pp）。ARC-c、GSM8K 上 KL 也均低于 BCE。Uniform allocation 同样趋势（64.49 vs 66.34）。\n- BCE 使用 magnitude-based masks 在 14B 上 MMLU 正常（71.67%），问题特定于 KL 的 coupled training——直接质疑 \"KL discovers superior mask patterns\" 的核心叙事：在 14B 上 KL 的 mask patterns 对 MMLU 是 **有害** 的。\n- Abstract \"confirms the PPL advantage across 7-14B\" 轻描淡写 downstream degradation。正文仅半句带过（§4.5），无任何机制解释。\n- **建议**：正文（非仅 Appendix）充分讨论 14B reversal（至少一段）；提出可检验的机制假设；将 Abstract 改为明确表述 downstream reversal。\n\n**N3. BCE baseline 在不同稀疏度使用不同实验管线，跨 sparsity 比较不可靠** [R1 Must-Fix, R2 交叉确认]\n- 30% BCE（Table 1 $^\\dagger$）：TEAL global allocation, no compensation, 2700 steps → PPL 11.25\n- 50% BCE（Table 1 $^\\ast$）：DejaVu pipeline + compensation (+67.2M params), no TEAL allocation → PPL 28.13±0.20\n- **关键遗漏**：没有 \"50% BCE + TEAL global (no compensation)\" baseline——这才是与 50% KL global 最直接可比的设置。\n- Table 4 \"BCE + Compensation\" PPL=25.44 vs \"BCE (no comp)\" PPL=27.97，差距 2.53，说明 compensation 对 BCE 有显著影响。但两者是否均使用 TEAL allocation 未明确标注。\n- **影响**：Baseline 公平性是实验驱动论文的生命线。读者无法判断 KL 优势有多少来自 objective、多少来自 allocation strategy 差异。\n- **建议**：增加 \"50% BCE + TEAL global (no comp)\" baseline；统一管线；Table 1 caption 更显著标注差异。\n\n**N4. 实际可用操作区间极窄 + Abstract framing 偏向 50%** [R1 Must-Fix, R2 Must-Fix (N2+N3)]\n- **50%**：MMLU 28.1±0.2%（≈random 25%），GSM8K <2.2%——论文自己确认 \"capacity-limited regime\"。KL 的 49% PPL 优势在 downstream 上完全无法体现。\n- **30%**：KL uniform PPL 8.81 vs TEAL 10.97（18%）。但 downstream 差异很小——MMLU +2.1pp, ARC-c +1.4pp, GSM8K -0.4pp（TEAL 更好）。考虑 3-seed σ，多数差异不显著。\n- **无实际加速**：当前实现增加 6.4% 延迟（126.78 vs 119.11 ms/forward）。即使 30% PPL 改进也没有对应的 wall-clock benefit。未验证 KL masks 是否兼容 N:M structured sparsity。\n- Abstract 叙事高潮放在 \"At 50%, the PPL advantage widens to 49%\"，但 50% 是 downstream-dead zone。\n- **建议**：将叙事重心转向 30% downstream-preserved quality；坦诚讨论 30% 的 modest downstream improvement；补充 N:M 兼容性讨论或初步实验。\n\n**N5. 方法新颖性不足以支撑 Main Conference** [R2 Must-Fix, R1 同意实质但 REBUT 定级]\n- 核心方法 = KL distillation (Hinton 2015) + Gumbel-Sigmoid (Jang 2017) + per-layer MLP predictor (DejaVu 2023)。每个组件均为成熟技术。\n- MaskLLM (NeurIPS 2024) 已组合 frozen weights + learnable masks + KL + Gumbel relaxation。论文声称的三点区别（activation vs weight sparsity, predictor vs learnable params, global vs N:M）是应用场景切换，非方法论创新。\n- Table 2 taxonomy 填充一个 \"Per-token × Coupled\" 空白格，学术贡献有限。\n- **共识**：两位 Reviewer 均认为论文适合 Findings track。C1 empirical finding 有价值，但方法本身缺乏足够创新支撑 Main。R1 指出新颖性不可 \"fix\"，属于定位问题而非缺陷。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. PPL degradation 措辞与计算方式不匹配** [R1]\n- Abstract \"KL reduces PPL degradation 18% over TEAL\"：语义上应指缩小 dense-to-sparse gap（= 41%），实际计算是 relative PPL improvement (10.97-8.96)/10.97 = 18%。\n- 建议统一为 \"reduces PPL by 18% relative to TEAL\"。\n\n**W2. Mistral-7B 缺少全部 downstream 评估** [R1, R2 交叉确认]\n- Table 8 (Appendix G) 仅报告 PPL。鉴于 14B 出现 PPL↑但 MMLU↓ 的反转，Mistral PPL-only 不能支撑跨架构泛化声明。\n- 建议补充至少 MMLU 和 ARC-c。\n\n**W3. Adaptive penalty Eq.5/6 形式化不一致** [R1, R2 交叉确认]\n- Eq. 5 定义不等式约束 $\\bar{s} \\leq 1-\\rho$，Eq. 6 使用绝对值 $|\\bar{s}-(1-\\rho)|$（等式约束）。实际上等式约束更合理，但推导应保持一致。\n- 30% target actual sparsity 28.5%（5% deviation），interpolated TEAL baseline 未实际测量。\n\n**W4. 训练数据消融缺失** [R1+R2 共识]\n- 所有 predictor 在 WikiText-103 上训练（~8M tokens），主要评估在 WikiText-2（同域）。C4 OOD 显示 degradation 从 1.46× 恶化到 1.74× dense。\n- KL-discovered mask patterns 的 domain specificity 未知。缺少 C4-trained predictor 对比。\n\n**W5. SPON 边际贡献（2.4%）在方法中位置偏重** [R1, R2 部分 REBUT]\n- 仅 2.4% PPL improvement，cosine similarity 0.196, R²=0.038。R1 建议标注为可选组件；R2 认为 Related Work 段落是必要 positioning。\n- 共识：不需要移除，但可以在 ablation 中更突出其边际性。\n\n### Minor（不影响接收）\n\n**M1.** -ing 分词短语偏多（~15 处），部分可改写（如 \"enabling...discover\" → 拆分独立句）。R1 认为不构成系统问题，R2 认为应 fix。[轻微分歧]\n**M2.** Float spacing 被手动压缩（`\\textfloatsep{8pt}`），conclusion 有 `\\vspace{-4pt}`——不违规但暗示空间紧张。\n**M3.** Ethics 声明遗漏 Qwen-2.5-14B（仅提 LLaMA-8B 和 Mistral-7B）。\n**M4.** §3.3 Gumbel-Sigmoid 应优先引用 Concrete distribution (Maddison 2017) 和 L₀ (Louizos 2018)，而非 Gumbel-Softmax (Jang 2017)。\n**M5.** §3.4 \"mean-seeking\" 术语不标准，应为 \"mass-covering\" 或 \"inclusive\"。\n**M6.** §3.6 Jacobian 形式化应为 $\\partial \\mathbf{z}/\\partial \\tilde{m}_j$（对 mask），非 $\\partial \\mathbf{z}/\\partial \\mathbf{h}$（对 hidden state）。R2 认为 suggestive analysis 不需完整形式化。\n**M7.** Table 1 同行混合不同统计报告（MMLU 3-seed 带 ±，GSM8K 单 seed 无 ±），易造成混淆。\n**M8.** Table 4 SPON 脚注使用 `evaluate.py` 而非 unified benchmark，数值可比性需说明。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n| 议题 | 共识 |\n|------|------|\n| C1 ablation 2-seed 不够 | 两位均同意，核心 claim 需更强统计支撑 |\n| Soft-vs-hard mask confound | R1 发现，R2 交叉确认 |\n| 14B downstream reversal 需讨论 | 两位均 Must-Fix |\n| BCE pipeline 不一致 | R1 发现，R2 交叉确认（Round 1 遗漏） |\n| 50% downstream 崩溃 + framing 偏差 | 两位一致 |\n| 无 wall-clock speedup | 两位一致（定级有分歧，见下） |\n| 方法新颖性 → Findings 级别 | 两位结论一致 |\n| Overall 3.0 (Findings) | 完全一致 |\n\n## Reviewer Divergence [REBUT]\n\n| 议题 | R1 | R2 | 状态 |\n|------|----|----|------|\n| Wall-clock speedup 定级 | Should-fix（论文已诚实 scope） | Must-fix | 不影响评分 |\n| 方法新颖性定级 | 属于定位问题非缺陷 | Must-fix | 不影响评分（都认为 Findings） |\n| -ing 短语 | 不构成问题 | Should-fix | Minor 分歧 |\n| Predictor 架构比较 | Should-fix | 不需要（贡献在 objective） | Minor 分歧 |\n| §3.6 Jacobian 形式化 | Minor issue | 不需修改（suggestive analysis） | Minor 分歧 |\n\n**分歧评估**：所有分歧仅涉及问题定级（must-fix vs should-fix, should-fix vs minor），不涉及问题是否存在。核心判断完全一致。无需进入 Round 2。\n\n---\n\n## Questions for Authors\n\n**Q1** [R1+R2 共识]: C1 ablation 的 \"KL-derived oracle masks\" 具体如何生成？从哪个 checkpoint（step）、哪个 seed 的 KL predictor 提取？用另一个 seed 的 KL predictor 生成 masks 是否会得到不同 C1 结果？\n\n**Q2** [R1+R2 共识]: 14B MMLU reversal 是否在多个 seed 上验证？Table 7 仅报告 seed 42。如果该 reversal 在不同 seed 间不稳定，可能只是噪声。\n\n**Q3** [R1+R2 共识]: 30% sparsity 下 KL 的 actual sparsity 为 28.5%（Table 6）。Table 1 的 TEAL baseline 是在 exact 30% 还是也有偏差？如果 KL 在 28.5% 而 TEAL 在 30%，那 KL 的一部分 PPL 优势来自剪枝更少的 neurons。\n\n**Q4** [R1]: 为什么没有报告 \"50% BCE + TEAL global (no compensation)\" 的结果？这是与 KL global 最直接可比的 baseline。\n\n**Q5** [R1]: 在 C4 上训练 predictor 时，mask divergence from magnitude 的幅度是否类似？KL masks 的 domain specificity 有多大？\n\n**Q6** [R2]: 50% downstream collapse 下 KL MMLU (28.1%) 与 TEAL (28.32%) 差异在 noise range 内。如果 downstream 是最终目标且 30% 是推荐操作点，为何以 50% PPL improvement 而非 30% downstream preservation 作为核心叙事？\n\n---\n\n## Missing References\n\n**应引用** [R1+R2 共识]:\n1. **Enabling Dynamic Sparsity in Quantized LLMs** (2025, arXiv 2511.04477) — 量化 + activation sparsity 协同设计\n2. **Mixture of Neuron Experts** (2025, arXiv 2510.05781) — neuron-level MoE 转换，与 D2DMoE 互补\n\n**可选引用** [有分歧]:\n3. SeerAttention (2024) — R2 建议, R1 REBUT（attention sparsity vs FFN sparsity，已有 Polar Sparsity 覆盖）\n4. DeepSeek-V3/DeepSeekMoE — R2 建议, R1 REBUT（native MoE 架构，非 dense→sparse 问题）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。项目 `external_review.paperreview_ai.enabled` 未启用。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n### 支撑 Findings 接收的理由\n\n1. **C1 因果消融**是有价值的 empirical finding——mask target quality > gradient coupling 在文献中没有先例，即使统计效力需加强，方向和设计都值得发表。\n2. **Regime analysis**（非单调 allocation 偏好）对实践者有指导意义，Table 5 的 6-level 数据提供了有用参考。\n3. **68% mask divergence** 从 magnitude ranking 是非显而易见的发现，揭示了 KL 训练发现了不同的 neuron importance landscape。\n4. 方法公式化简洁正确，消融系统全面，写作清晰诚实。\n\n### 阻碍 Main Conference 接收的理由\n\n1. **方法新颖性有限**：KL + Gumbel + predictor 均为成熟组件的直接组合，MaskLLM 已在高度类似的框架下发表。\n2. **C1 核心 claim 证据不充分**：\"causal ablation proves\" 仅 2-seed，存在 soft-vs-hard confound，30% PPL gap 暗示 gradient coupling 残余贡献。\n3. **14B downstream reversal**未被充分讨论，直接质疑方法的 scalability。\n4. **实际可用范围极窄**：50% downstream 全面崩溃，30% 的 downstream 改进仅 ~2pp（多数不显著），无 wall-clock 加速。\n5. **BCE baseline pipeline 不一致**使跨 sparsity 比较不可靠。\n\n### 升级到 3.5 (Borderline Conference) 的路径\n\n若能修复以下问题，可考虑升级：\n- **N1**: C1 增加到 5-seed + 降级 \"proves\" 措辞 + 讨论 soft-vs-hard confound\n- **N2**: 正文充分讨论 14B reversal + 提供机制假设\n- **N3**: 增加 \"50% BCE + TEAL global (no comp)\" baseline\n- **N4**: 将叙事重心从 50% PPL 转向 30% downstream quality\n\n---\n\n## Detailed Comments (Per-Section)\n\n### Abstract\n- 第 2 行 \"causal ablation confirms\" → 降级为 \"ablation provides evidence\"\n- 第 4 行 \"reduces PPL degradation 18%\" → 改为 \"reduces PPL by 18% relative to TEAL\"（措辞与计算不匹配）\n- 第 5 行 50% PPL 作为叙事高潮但 downstream 已崩溃 → 将 30% downstream quality 放在更突出位置\n- 第 6 行 \"confirms PPL advantage across 7-14B\" → 必须同等突出 downstream reversal\n\n### Introduction\n- L10 \"a causal ablation confirms\" → 降级措辞\n- L10-11 \"the primary quality driver\" → 加 caveat：30% 条件下可能有残余 gradient coupling 贡献\n- L16 14B 提及过于简略 → 增加 1-2 句讨论 downstream reversal 的含义\n\n### Method\n- §3.3 优先引用 Concrete distribution (Maddison 2017) 和 L₀ (Louizos 2018)\n- §3.4 \"mean-seeking\" → \"mass-covering\" 或 \"inclusive\"\n- §3.5 Eq. 5 vs Eq. 6 约束类型统一\n- §3.6 Jacobian 表述修正；\"suggestive\" 定位保持\n\n### Experiments\n- Table 1: 统一 30% 和 50% BCE 使用相同推理管线；增加 50% BCE+TEAL global baseline\n- Table 1: 统一同行的统计报告格式（避免 MMLU 有 ± 而 GSM8K 无）\n- Table 3: C1 增加 seed 数量；添加 confidence intervals\n- §4.4 最后一段: 讨论 30% PPL gap 与 gradient coupling 的可能联系\n- §4.5: 增加至少 1 段 14B reversal 的机制讨论\n- §4.5: 补充 Mistral-7B downstream evaluation\n\n### Related Work\n- 增加 Enabling Dynamic Sparsity in Quantized LLMs (2025) 和 Mixture of Neuron Experts (2025)\n\n### Conclusion\n- 第 1 行 \"confirms target quality, not gradient coupling\" → 降级措辞\n\n### Limitations\n- 已较完善。可增加：C1 的 soft-vs-hard confound 作为方法论局限。\n\n### Ethics\n- 补充 Qwen-2.5-14B 模型引用和 license 信息。\n\n### Appendix\n- Table 4 SPON 脚注: 说明 evaluate.py vs unified benchmark 的数值差异影响。",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)"
  }
}
```

</details>

---


### Tool result

_source line 841 · 2026-05-19T01:58:01.667218+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 5127
}
```

</details>

---


### Assistant

_source line 842 · 2026-05-19T01:58:17.307493+00:00_

**Round 9 审稿完成。**

汇总报告已投递至 Research Director。核心结论：

**Overall: 3.0 (Findings)** — 两位 Reviewer 评分完全一致，交叉回应后所有关键问题达成共识。

**5 个 Must-Fix（共识）**：
1. **C1 因果消融**：仅 2-seed + soft-vs-hard mask confound 未控制 + "proves" 措辞过强
2. **14B downstream 全面反转**：KL MMLU -8.1pp vs TEAL，正文讨论不充分，无机制解释
3. **BCE baseline 管线不一致**：30% 和 50% 使用不同 pipeline（TEAL/comp），缺少最直接可比的 baseline
4. **实际可用范围极窄**：50% downstream 崩溃，30% 改进 ~2pp（多数不显著），无 wall-clock 加速，Abstract framing 偏向 50%
5. **方法新颖性**：已有组件直接组合，MaskLLM overlap，适合 Findings 不适合 Main

**升级到 3.5 的路径**：C1 增加到 5-seed + 降级 "proves" 措辞、正文讨论 14B reversal、统一 BCE baseline pipeline、将叙事重心从 50% PPL 转向 30% downstream。

Issue Tracker 已同步更新（9 个新 R9 issue + 既有 issue 状态更新）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 66

## Round 66

2 recorded events


### User

_source line 843 · 2026-05-19T01:58:19.976452+00:00_

[Reviewer 2 审稿结果]:
已完成对 R1 全部意见的逐条回应，核心结论：

- **4/4 Must-Fix 全部同意**，其中 N3（BCE 管线不一致）和 N1(c)（soft vs hard mask confound）是我 Round 1 遗漏的重要发现
- **4/6 Should-Fix 同意**，反驳 W5（架构比较非核心贡献方向）和 W6（SPON positioning 合理）
- **4/5 Minor 同意**，反驳 M3（suggestive analysis 不需完整形式化）
- **维持 Overall 3.0 (Findings)**，R1 的发现进一步强化了这一判断

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

_source line 844 · 2026-05-19T01:58:40.142918+00:00_

审稿报告已投递至 Research Director。

**Round 9 审稿完成总结**：

- **评分**: 3.0 (Findings)，两位 Reviewer 完全一致
- **Confidence**: 4/5

**5 个 Must-Fix**:
1. C1 因果消融仅 2-seed + "proves" 措辞过强 + soft-vs-hard mask 训练差异构成未控制混淆变量
2. 14B downstream 全面反转（MMLU -8.1pp vs TEAL），正文讨论严重不足
3. BCE baseline 在 30% 和 50% 使用不同推理管线，缺少最关键的 "50% BCE + TEAL global" baseline
4. 实际可用区间仅 ≤30%（~2pp downstream gain），Abstract 叙事偏向 50% PPL headline
5. 方法新颖性为已有组件直接组合，适合 Findings 而非 Main

**核心共识**：C1 empirical finding 有发表价值（Findings 级别），但证据强度、baseline 公平性、scalability 和实用范围均未达 Conference 标准。若修复 N1-N4（增加 C1 seed 数 + 统一 BCE pipeline + 正文讨论 14B reversal + 重新平衡 framing），可考虑 3.5 Borderline Conference。

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`（9 个 R9 新条目 + 历史条目状态更新）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 67

## Round 67

60 recorded events


### User

_source line 845 · 2026-05-19T06:21:14.114052+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25

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

_source line 846 · 2026-05-19T06:21:20.698569+00:00_

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

_source line 847 · 2026-05-19T06:21:20.699219+00:00_

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
…[truncated 2458 chars]

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

_source line 848 · 2026-05-19T06:21:23.912751+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
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
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-19T06:21:23.963648+00:00_



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

_source line 850 · 2026-05-19T06:21:28.540113+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_local_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
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
    "query": "select:director_get_project_overview,read_local_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-19T06:21:28.592221+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-19T06:21:32.061280+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-19T06:21:32.162217+00:00_



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

_source line 854 · 2026-05-19T06:21:34.928193+00:00_

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

_source line 855 · 2026-05-19T06:21:35.917361+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (227 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| mistral_dense_hellaswag_piqa | Mistral-7B-v0.3 Dense baseline on HellaSwag (10-shot) and PIQA (0-shot). Required to complete Dense row in tab:mistral_downstream. Parent: lm_eval_mistral_dense. | — | — | — |\n\n## 待处理\n- c1_eval_30pct_s456（准备中）\n- kl_sparsity40_s42_eval_teal_uniform: KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.（准备中）\n- c4_download（准备中）\n- kl50_s456_train_eval（准备中）\n- mag_preservation_reg（准备中）\n- longbench_dense_v5（准备中）\n- kl_lagrangian_v2（准备中）\n- kl_norm_v3_quicktest（准备中）\n- mvp_kl_norm_s456（准备中）\n- spon_kl_s42（准备中）\n- …另有 3 项\n\n## 近期结论\n- **mistral_kl30_hellaswag_piqa** (success): KL 30% predictor on Mistral-7B evaluated on HellaSwag (10-shot) and PIQA (0-shot) with TEAL uniform allocation. Completes the 7-task Mistral comparison table (KL vs TEAL). TEAL 30% baseline: HS=60.1%, PIQA=72.1%. Required for W2 cross-architecture claim. ← 基于 mistral_kl30_downstream\n- **eval_c1_retrain_30pct_s456** (success): C1 retrain eval s456: BCE predictor trained on kl_30pct_s45
…[truncated 1797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 989
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-19T06:21:36.069128+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 call for papers submission guidelines author instructions"
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
    "query": "ACL Rolling Review ARR May 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 857 · 2026-05-19T06:21:39.231927+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex",
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
    "pattern": "**/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 858 · 2026-05-19T06:21:39.282702+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex

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

_source line 859 · 2026-05-19T06:21:39.283181+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.pdf",
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
    "pattern": "**/paper/main.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 860 · 2026-05-19T06:21:39.333958+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf

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


### Tool result

_source line 861 · 2026-05-19T06:21:54.826392+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) submission guidelines and author instructions:

## Key Submission Requirements

All submitted papers are expected to describe original, completed and unpublished work. Papers must not include authors' names and affiliations.

## Author Registration and Reviewer Requirements

ACL has adopted a policy similar to that of CVPR, requiring all authors to sign up as reviewers, with assignments made based on
…[truncated 1462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 18757
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-19T06:22:01.167944+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 page limits long short paper format requirements template"
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
    "query": "ACL Rolling Review 2026 page limits long short paper format requirements template"
  }
}
```

</details>

---


### Tool call

_source line 863 · 2026-05-19T06:22:01.672283+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers commitment deadline ARR cycle"
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
    "query": "EMNLP 2026 call for papers commitment deadline ARR cycle"
  }
}
```

</details>

---


### Tool call

_source line 864 · 2026-05-19T06:22:02.628388+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "150"
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
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 865 · 2026-05-19T06:22:03.081533+00:00_

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
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-19T06:22:03.236396+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "paper_framing.md",
  "max_chars": "12000"
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
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-19T06:22:08.273155+00:00_

Web search results for query: "EMNLP 2026 call for papers commitment deadline ARR cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here's the key information about EMNLP 2026's call for papers commitment deadline and ARR cycle:

## ARR Submission Deadline

Papers must be submitted, at latest, by the ARR 2026 May cycle. More spe
…[truncated 934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6600
}
```

</details>

---


### Tool result

_source line 868 · 2026-05-19T06:22:08.575540+00:00_

Web search results for query: "ACL Rolling Review 2026 page limits long short paper format requirements template"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's the information about ACL Rolling Review 2026 page limits and format requirements:

## Page Limits

Long papers may consist of up to 8 pages of content, plus unlimited pages for references and appendices. Upon acceptance, long papers will be given one additional page of content (i.e. up to 9 pages) in the proceedings.

Final versions of short papers may have up to five (5) pages, plus unlimited pages for acknowledgments and references.

## Format Requirements

Manuscripts should be submitted electronically, in PDF format and formatted using
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7407
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-19T06:22:08.576580+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md\", \"content\": \"# Paper Framing — distill_sparse_swiglu\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\\n- Deadline: 2026-05-25 (ARR submission)\\n- Track: Efficient Methods for NLP\\n\\n## Core Claims\\n\\n1. **KL distillation discovers fundamentally different (and superior) neuron importance patterns that magnitude-based oracles miss**: The C1 causal ablation (D059) proves that KL's advantage comes **entirely** from target quality (which neurons to keep), with gradient coupling contributing ≈0 across **both PPL and all downstream tasks**. **Controlled eval (TEAL 50% uniform, matched protocol)**: BCE+KL-targets PPL = **11.9638**, KL predictor PPL = **11.9638** (exact match). **Downstream confirmation (full-spectrum)**: All 4 downstream tasks (ARC-c, WinoGrande, MMLU, GSM8K) also match within <1pp delta, confirming gradient coupling = 0 across PPL + reasoning + knowledge + math dimensions. Standard BCE (magnitude masks) PPL ≈ 22.51. Target quality alone accounts for KL's full advantage. *Additional evidence from training eval (Gumbel hard mask)*: BCE+KL-targets PPL 9.29 @60.9% ≈ KL 9.21 @60.6%, consistent with controlled eval. The 53% mask divergence between KL-derived and magnitude-based masks is the core empirical finding: KL discovers a qualitatively different neuron importance landscape. **Implication**: The gradient coupling analysis (§3.6) provides mathematical intuition for *why* KL can discover better targets (coupled gradients explore joint neuron interaction patterns), but the causal driver is the resulting mask quality, not the gradient pathway per se. This shifts the contribution from \\\"engineering a better loss\\\" to \\\"discovering that output-distribution distillation reveals hidden neuron importance structure.\\\" **Supporting evidence**: (a) Iso-compute ablation: BCE with 
…[truncated 10492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5340
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-19T06:22:13.405129+00:00_

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

_source line 871 · 2026-05-19T06:22:13.909246+00:00_

1	We show that KL-trained sparsity predictors for SwiGLU LLMs discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%) at 50\% sparsity.
2	A causal ablation provides evidence that these mask patterns, not gradient coupling, drive quality across the full sparsity range: BCE trained on KL-derived targets reproduces KL quality at both 50\% (max $\Delta$=0.59pp, 2-seed) and 30\% (max $\Delta$=1.70pp, 3-seed), while magnitude-trained BCE achieves 28.13$\pm$0.20 at 50\%.
3	The resulting predictor ($<$1\% of base parameters), trained with forward KL and Gumbel-Sigmoid relaxation on LLaMA-3.1-8B, renders post-hoc compensation (+67.2M params) redundant at both 30\% and 50\% sparsity.
4	At 30\%, KL reduces PPL by 18\% relative to TEAL; uniform allocation provides $7.5\times$ smaller cross-seed downstream $\sigma$, with HellaSwag (86.0\% retention) and PIQA (92.5\%) preserving non-reasoning quality.
5	At 50\%, the PPL advantage widens to 49\%, though downstream reasoning tasks collapse to near-random regardless of allocation.
6	PPL and downstream advantages hold on most tasks across architectures (Mistral-7B: KL wins
7	5 of 6 downstream tasks vs.\ TEAL at 30\%, largest ARC +9.0pp; GSM8K reverses), though downstream reversal at 14B (Qwen MMLU 63.7\% vs.\ TEAL's 71.8\%) warrants further investigation.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-19T06:22:13.909998+00:00_

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

_source line 873 · 2026-05-19T06:22:14.412844+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: TEAL's top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
9	This suggests KL should outperform BCE under global allocation.
10	The empirical picture, however, reveals something more fundamental: KL-trained predictors discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%), and a causal ablation provides evidence that these learned mask patterns, not gradient coupling, are the primary quality driver.
11	Under controlled 50\% evaluation, BCE trained on KL-derived targets exactly matches KL across perplexity and all downstream tasks (max $\Delta$=0.59pp, 2-seed), while magnitude-trained BCE achieves 28.13$\pm$0.20.
12	
13	We instantiate a lightweight predictor (75.9M params, $<$1\% of base) trained with forward KL and Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} on LLaMA-3.1-8B~\cite{grattafiori2024llama3}.
14	With uniform allocation, the predictor achieves PPL 11.92 at 50\% sp
…[truncated 1479 chars]

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

_source line 874 · 2026-05-19T06:22:14.413364+00:00_

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

_source line 875 · 2026-05-19T06:22:14.865508+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
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
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden sta
…[truncated 11270 chars]

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

_source line 876 · 2026-05-19T06:22:14.866051+00:00_

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

_source line 877 · 2026-05-19T06:22:15.320817+00:00_

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
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor} (DejaVu-style~\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distri
…[truncated 17463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-19T06:22:15.372062+00:00_

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

_source line 879 · 2026-05-19T06:22:15.875728+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address the interaction between dynamic sparsity and quantization with zigzag-patterned weight layouts.
7	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
8	
9	\paragraph{Predictor-Based Contextual Sparsity.}
10	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
11	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
12	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
13	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
14	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
15	MaskLLM~\cite{fang2024maskllm} shares the principle of frozen weights + learnable masks + KL training, but the two methods differ in three fundamental ways.
16	First, \emph{sparsity type}: MaskLLM targets N:M semi-structured \emph{weight} sparsity (static 2:4 patterns), while we target \emph{activation} sparsit
…[truncated 4059 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-19T06:22:15.876241+00:00_

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

_source line 881 · 2026-05-19T06:22:16.328871+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	\vspace{-4pt}
4	
5	KL distillation discovers neuron importance patterns that diverge 68\% from magnitude-based masks; a causal ablation supports target quality, not gradient coupling, as the primary driver.
6	A predictor ($<$1\% of base) halves TEAL's perplexity across 7--14B and renders compensation (+67.2M params) redundant; at 30\%, uniform allocation delivers $7.5\times$ smaller cross-seed $\sigma$.
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

_source line 882 · 2026-05-19T06:22:16.380149+00:00_

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

_source line 883 · 2026-05-19T06:22:16.832490+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades; 30\% appears to be the best-quality sparsity level for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	On Mistral-7B, KL wins 5 of 6 downstream tasks at 30\% but GSM8K reverses (11.1\% vs.\ TEAL's 15.9\%), consistent with GSM8K's sensitivity to the sparsity objective: reasoning tasks may require different optimization targets than knowledge and commonsense benchmarks.
6	The 30\% sparsity analysis is validated at 7--8B scale; at 14B, the MMLU gap persists regardless of allocation strategy (Appendix~\ref{app:14b}). Scaling to 70B remains untested.
7	Out-of-distribution evaluation on C4 (Appendix~\ref{app:ood}) shows the KL advantage transfers but with a wider gap: C4 PPL at 30\% is $1.74\times$ dense vs.\ $1.46\times$ on in-domain WikiText-2, which indicates that the predictor partially overfits to training-domain activation patterns. Extending OOD evaluation to 70\% sparsity is left to future work.
8	The causal ablation (\S\ref{sec:mask_analysis}) provides evidence that mask target quality, not gradient coupling, is the primary driver of KL's advantage. However, the mechanism by which KL's coupled gradient discovers superior mask patterns during training remains incompletely characterized; future work could trace per-layer mask divergence trajectories across training to identify when and where the patterns diverge.
9	At 30\% sparsity, global allocation exhibits 9.5pp cross-seed MMLU standard deviation (3-seed); allocation strategy interacts with predictor initialization in task-specific ways. This variance is MMLU-specific, as ARC, WinoGrande, and GSM8K show stable pe
…[truncated 538 chars]

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

_source line 884 · 2026-05-19T06:22:16.832849+00:00_

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

_source line 885 · 2026-05-19T06:22:17.385418+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--8B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}, Qwen-2.5-14B~\cite{qwen2024qwen25}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 i
…[truncated 1961 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-19T06:22:17.385915+00:00_

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

_source line 887 · 2026-05-19T06:22:17.487206+00:00_

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
…[truncated 20224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-19T06:22:23.763418+00:00_

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

_source line 889 · 2026-05-19T06:22:24.065578+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 18430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-19T06:22:24.567974+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-19T06:22:25.572258+00:00_

issues:
  # ============================================================
  # Round 10 (fresh review) — Action Matrix dispatched
  # ============================================================

  - id: "R9-N1"
    summary: "C1 causal ablation: 2-seed insufficient for 'proves' claim + soft-vs-hard mask confound uncontrolled"
    category: experiment
    severity: critical
    status: in_progress
    first_raised_round: 9
    last_seen_round: 10
    mentions:
      - {round: 9, reviewers: [1, 2], note: "R1 raised as Must-Fix N1 (2-seed + soft-vs-hard confound + 30% PPL gap). R2 initially Should-Fix W1, upgraded to AGREE with R1 in cross-response."}
      - {round: 10, reviewers: [1, 2], note: "Reconfirmed. R1 new finding: soft-vs-hard confound (KL uses soft Gumbel, C1 BCE uses hard targets). 30% PPL gap +0.63 flagged."}
    action_items:
      - {round: 10, action: "C1@30% s123 + s456 experiments dispatched (41718:0,1). Achieves 3-seed at 30%.", assigned_to: "main_agent", status: in_progress}
      - {round: 10, action: "全文 proves/confirms → provides evidence/supports", assigned_to: "paper_agent", status: in_progress}
      - {round: 10, action: "§4.4 新增 soft-vs-hard confound 讨论 + bce_gumbel PPL=38.02 反证", assigned_to: "paper_agent", status: in_progress}
    resolution: ""
    resolution_round: null

  - id: "R9-N2"
    summary: "BCE baseline pipeline inconsistent across sparsity levels: 30% uses TEAL/no-comp, 50% uses DejaVu+comp/no-TEAL"
    category: experiment
    severity: critical
    status: in_progress
    first_raised_round: 9
    last_seen_round: 10
    mentions:
      - {round: 9, reviewers: [1, 2], note: "R1 raised as Must-Fix N3. R2 missed in initial review, AGREE in cross-response."}
      - {round: 10, reviewers: [1, 2], note: "Reconfirmed. Missing 50% BCE+TEAL global baseline."}
    action_items:
      - {round: 10, action: "bce_50pct_teal_global_unified eval dispatched (34887:0). Uses benchmark_eval.py unified protocol.", assigned_to: "main_agent", st
…[truncated 13847 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-19T06:22:26.074603+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"\\\\\\\\section\\|\\\\\\\\subsection\\|\\\\\\\\paragraph\\|\\\\\\\\begin{table\\|\\\\\\\\begin{figure\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/*.tex 2>/dev/null",
  "description": "Count sections, tables, and figures in paper"
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
    "command": "grep -c \"\\\\\\\\section\\|\\\\\\\\subsection\\|\\\\\\\\paragraph\\|\\\\\\\\begin{table\\|\\\\\\\\begin{figure\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/*.tex 2>/dev/null",
    "description": "Count sections, tables, and figures in paper"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-19T06:22:27.030237+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex:32
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex:7
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex:29
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex:13
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex:7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 894 · 2026-05-19T06:22:27.030731+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && grep -c \"\\\\\\\\cite{\" *.tex | awk -F: '{s+=$2} END{print \"Total citations:\", s}'",
  "description": "Count total citations in paper"
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
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && grep -c \"\\\\\\\\cite{\" *.tex | awk -F: '{s+=$2} END{print \"Total citations:\", s}'",
    "description": "Count total citations in paper"
  }
}
```

</details>

---


### Tool result

_source line 895 · 2026-05-19T06:22:27.131491+00:00_

Total citations: 57
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-19T06:22:47.068181+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/*.yml 2>/dev/null || echo \"NOT_FOUND_IN_PROJECT_ROOT\"; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/*.yaml 2>/dev/null || echo \"NOT_FOUND_IN_AGENT_DIR\"",
  "description": "Check external review config"
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
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/*.yml 2>/dev/null || echo \"NOT_FOUND_IN_PROJECT_ROOT\"; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/*.yaml 2>/dev/null || echo \"NOT_FOUND_IN_AGENT_DIR\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-19T06:22:47.872322+00:00_

NOT_FOUND_IN_PROJECT_ROOT
NOT_FOUND_IN_AGENT_DIR

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 898 · 2026-05-19T06:22:47.923109+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && pdfinfo main.pdf 2>/dev/null | grep \"Pages:\" || echo \"pdfinfo not available\"",
  "description": "Count PDF pages"
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
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && pdfinfo main.pdf 2>/dev/null | grep \"Pages:\" || echo \"pdfinfo not available\"",
    "description": "Count PDF pages"
  }
}
```

</details>

---


### Tool result

_source line 899 · 2026-05-19T06:22:48.025263+00:00_

Pages:           17
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-19T06:23:38.518597+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- **路径**: projects/distill_sparse_swiglu/paper/main.tex（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, related_work.tex）\n- **目标 venue**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL template with [review], Long paper ≤8 pages content + unlimited refs/appendix, double-blind, Limitations section required (不计入页数), Ethics encouraged (不计入页数)\n\n## 你的审查重点\n\n### A. Claims vs Evidence 对应\n逐条检查以下核心 claims 是否被实验充分支撑：\n1. \"KL-trained predictors discover neuron importance patterns diverging 68% from magnitude-based masks\" — 数据来源？统计量级？\n2. \"Causal ablation (C1) provides evidence that mask target quality, not gradient coupling, drives quality\" — C1 实验设计是否能真正解耦？confound 是否被讨论？seed 数量是否足够？\n3. \"Compensation (+67.2M params) redundant\" — 在哪些条件下验证？seed 数量？\n4. \"Non-monotonic allocation preference with three regimes\" — 数据点是否足够支撑 regime boundary？\n5. \"Cross-architecture generalization\" — Mistral 和 Qwen 结果全面吗？downstream 完整吗？\n\n### B. Baseline 公平性\n- BCE baseline 在 30% 和 50% 是否使用一致的 pipeline（allocation、compensation、step count）？\n- TEAL 是否是最强的 training-free baseline？\n- 有无遗漏的关键 baseline（如其他 KL-based methods、MSE predictors）？\n\n### C. 统计效力\n- 哪些关键比较只有单 seed？\n- multi-seed 的 claim 是否标准差支撑结论？\n- 30% global 的 MMLU σ=9.5pp — 这是否 undermines 30% claim？\n\n### D. 消融充分性\n- Table 3 (ablation) 是否涵盖所有重要 design choices？\n- C1 ablation 的 soft-vs-hard mask confound 是否被 adequately addressed？\n- SPON 的贡献 (2.4%) 是否在 noise 范围内？\n\n### E. 数学/公式正确性\n- 检查 Eq.1-6 的一致性\n- Gradient analysis (§3.6) 的 claim 是否 overstate？\n- Lagrangian controller 的 convergence guarantee\n\n### F. 可复现性\n- 所有超参数是否完整报告？\n- 训练 setup 是否清楚到可以复现？\n\n请按以下格式输出：\n```\n## Summary (2-3 sentences)\n## Strengths (bulleted)\n## Weaknesses (bulleted, severity: Must-Fix / Should-Fix / Minor)\n## Questions for Authors\n## Missing References (if any)\n## Detailed Comments (per section)\n## Overall Assessment (score + confidence)\n```\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- **路径**: projects/distill_sparse_swiglu/paper/main.tex（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, related_work.tex）\n- **目标 venue**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL template with [review], Long paper ≤8 pages content + unlimited refs/appendix, double-blind, Limitations section required (不计入页数), Ethics encouraged (不计入页数)\n\n## 你的审查重点\n\n### A. Claims vs Evidence 对应\n逐条检查以下核心 claims 是否被实验充分支撑：\n1. \"KL-trained predictors discover neuron importance patterns diverging 68% from magnitude-based masks\" — 数据来源？统计量级？\n2. \"Causal ablation (C1) provides evidence that mask target quality, not gradient coupling, drives quality\" — C1 实验设计是否能真正解耦？confound 是否被讨论？seed 数量是否足够？\n3. \"Compensation (+67.2M params) redundant\" — 在哪些条件下验证？seed 数量？\n4. \"Non-monotonic allocation preference with three regimes\" — 数据点是否足够支撑 regime boundary？\n5. \"Cross-architecture generalization\" — Mistral 和 Qwen 结果全面吗？downstream 完整吗？\n\n### B. Baseline 公平性\n- BCE baseline 在 30% 和 50% 是否使用一致的 pipeline（allocation、compensation、step count）？\n- TEAL 是否是最强的 training-free baseline？\n- 有无遗漏的关键 baseline（如其他 KL-based methods、MSE predictors）？\n\n### C. 统计效力\n- 哪些关键比较只有单 seed？\n- multi-seed 的 claim 是否标准差支撑结论？\n- 30% global 的 MMLU σ=9.5pp — 这是否 undermines 30% claim？\n\n### D. 消融充分性\n- Table 3 (ablation) 是否涵盖所有重要 design choices？\n- C1 ablation 的 soft-vs-hard mask confound 是否被 adequately addressed？\n- SPON 的贡献 (2.4%) 是否在 noise 范围内？\n\n### E. 数学/公式正确性\n- 检查 Eq.1-6 的一致性\n- Gradient analysis (§3.6) 的 claim 是否 overstate？\n- Lagrangian controller 的 convergence guarantee\n\n### F. 可复现性\n- 所有超参数是否完整报告？\n- 训练 setup 是否清楚到可以复现？\n\n请按以下格式输出：\n```\n## Summary (2-3 sentences)\n## Strengths (bulleted)\n## Weaknesses (bulleted, severity: Must-Fix / Should-Fix / Minor)\n## Questions for Authors\n## Missing References (if any)\n## Detailed Comments (per section)\n## Overall Assessment (score + confidence)\n```\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
````

</details>

---


### Tool result

_source line 901 · 2026-05-19T06:24:02.581967+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24063
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-19T06:24:03.184809+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性/贡献显著性 + 写作质量 + Related Work 完整性 + 格式合规**。\n\n## 论文信息\n- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- **路径**: projects/distill_sparse_swiglu/paper/main.tex（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, related_work.tex）\n- **目标 venue**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL template with [review], Long paper ≤8 pages content + unlimited refs/appendix, double-blind, Limitations section required (不计入页数), Ethics encouraged (不计入页数)\n\n## 你的审查重点\n\n### A. 新颖性评估\n1. 核心方法 = KL divergence + Gumbel-Sigmoid + lightweight predictor — 每个组件都是已有技术。它们的组合是否构成足够的 novelty？\n2. 与 MaskLLM (Fang et al., 2024) 的区别是否充分？MaskLLM 也用 frozen weights + learnable masks + KL training。论文声称的三个区别（sparsity type, mask generation, allocation）是否 convincing？\n3. \"Empirical discovery\" framing（mask pattern divergence + causal ablation）是否足够作为 EMNLP Main 的贡献？还是更适合 Findings？\n4. Two-dimensional taxonomy (Table 1) 是否真正 insightful，还是人为构建来 position 论文？\n\n### B. 写作质量（严格按 CLAUDE.md paper-writing-norms 检查）\n1. **AI 写作痕迹**：\n   - `grep \"—\"` 和 `grep \" – \"` 检查解释性 em-dash/en-dash（§5.1 硬规则，必须全部删除）\n   - `-ing` 分词短语结尾（如 \"..., demonstrating the effectiveness of...\"）\n   - 过度分段（每 2-3 句换段）\n   - 连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"\n   - 用词黑名单：delve into, leverage, utilize, facilitate, a myriad of, paradigm shift\n2. **叙事结构**：\n   - Abstract 是否回答四个必答问题？\n   - Introduction 是否遵循五段结构？\n   - 全文主线是否统一（Abstract→Intro→Method→Results→Conclusion 是否讲同一个故事）？\n3. **专有名词**：首次出现是否都有定义/解释？\n4. **图表质量**：信息密度是否高？caption 是否自包含？数值精度是否统一？\n\n### C. Related Work 完整性\n1. 是否覆盖所有直接竞争方法？\n2. 是否有遗漏的重要近期工作（2024-2026）？\n3. 引用密度是否与 EMNLP 近年录用论文量级匹配？\n4. positioning 是否准确（本文相对已有工作的真实增量）？\n\n### D. 格式合规\n1. 正文是否 ≤8 页？\n2. ACL template [review] option 是否正确使用？\n3. Limitations section 位置是否正确（conclusion 后、references 前）？\n4. 行号是否开启？\n5. 引用格式是否一致（natbib）？\n6. 匿名化是否完整？\n7. 图表字体 ≥7pt？\n8. 所有附录内容在正文中是否被引用？\n\n### E. 贡献显著性\n1. 对 NLP/efficient inference 社区的实际影响有多大？\n2. 在没有 wall-clock speedup 的情况下，prediction quality improvement 的价值如何？\n3. 30% sparsity 的 practical benefit 是否 convincing？\n\n请按以下格式输出：\n```\n## Summary (2-3 sentences)\n## Strengths (bulleted)\n## Weaknesses (bulleted, severity: Must-Fix / Should-Fix / Minor)\n## Questions for Authors\n## Missing References (if any)\n## Detailed Comments (per section)\n## Overall Assessment (score + confidence)\n```\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性/贡献显著性 + 写作质量 + Related Work 完整性 + 格式合规**。\n\n## 论文信息\n- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- **路径**: projects/distill_sparse_swiglu/paper/main.tex（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, related_work.tex）\n- **目标 venue**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL template with [review], Long paper ≤8 pages content + unlimited refs/appendix, double-blind, Limitations section required (不计入页数), Ethics encouraged (不计入页数)\n\n## 你的审查重点\n\n### A. 新颖性评估\n1. 核心方法 = KL divergence + Gumbel-Sigmoid + lightweight predictor — 每个组件都是已有技术。它们的组合是否构成足够的 novelty？\n2. 与 MaskLLM (Fang et al., 2024) 的区别是否充分？MaskLLM 也用 frozen weights + learnable masks + KL training。论文声称的三个区别（sparsity type, mask generation, allocation）是否 convincing？\n3. \"Empirical discovery\" framing（mask pattern divergence + causal ablation）是否足够作为 EMNLP Main 的贡献？还是更适合 Findings？\n4. Two-dimensional taxonomy (Table 1) 是否真正 insightful，还是人为构建来 position 论文？\n\n### B. 写作质量（严格按 CLAUDE.md paper-writing-norms 检查）\n1. **AI 写作痕迹**：\n   - `grep \"—\"` 和 `grep \" – \"` 检查解释性 em-dash/en-dash（§5.1 硬规则，必须全部删除）\n   - `-ing` 分词短语结尾（如 \"..., demonstrating the effectiveness of...\"）\n   - 过度分段（每 2-3 句换段）\n   - 连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"\n   - 用词黑名单：delve into, leverage, utilize, facilitate, a myriad of, paradigm shift\n2. **叙事结构**：\n   - Abstract 是否回答四个必答问题？\n   - Introduction 是否遵循五段结构？\n   - 全文主线是否统一（Abstract→Intro→Method→Results→Conclusion 是否讲同一个故事）？\n3. **专有名词**：首次出现是否都有定义/解释？\n4. **图表质量**：信息密度是否高？caption 是否自包含？数值精度是否统一？\n\n### C. Related Work 完整性\n1. 是否覆盖所有直接竞争方法？\n2. 是否有遗漏的重要近期工作（2024-2026）？\n3. 引用密度是否与 EMNLP 近年录用论文量级匹配？\n4. positioning 是否准确（本文相对已有工作的真实增量）？\n\n### D. 格式合规\n1. 正文是否 ≤8 页？\n2. ACL template [review] option 是否正确使用？\n3. Limitations section 位置是否正确（conclusion 后、references 前）？\n4. 行号是否开启？\n5. 引用格式是否一致（natbib）？\n6. 匿名化是否完整？\n7. 图表字体 ≥7pt？\n8. 所有附录内容在正文中是否被引用？\n\n### E. 贡献显著性\n1. 对 NLP/efficient inference 社区的实际影响有多大？\n2. 在没有 wall-clock speedup 的情况下，prediction quality improvement 的价值如何？\n3. 30% sparsity 的 practical benefit 是否 convincing？\n\n请按以下格式输出：\n```\n## Summary (2-3 sentences)\n## Strengths (bulleted)\n## Weaknesses (bulleted, severity: Must-Fix / Should-Fix / Minor)\n## Questions for Authors\n## Missing References (if any)\n## Detailed Comments (per section)\n## Overall Assessment (score + confidence)\n```\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
````

</details>

---


### Tool result

_source line 903 · 2026-05-19T06:24:04.749779+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1564
}
```

</details>

---


### Assistant

_source line 904 · 2026-05-19T06:24:14.808839+00:00_

两位 Reviewer 已分配，等待独立审稿结果返回。

- **Reviewer 1**: 方法严谨性 + 实验有效性
- **Reviewer 2**: 新颖性/贡献显著性 + 写作质量 + Related Work + 格式

审稿进行中，收到结果后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 68

## Round 68

2 recorded events


### User

_source line 905 · 2026-05-19T06:32:14.398667+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — 方法严谨性 + 实验有效性审查

## Summary (2-3 sentences)

本文提出用 KL 散度蒸馏（替代传统 BCE）训练 SwiGLU LLM 的轻量级稀疏性预测器，核心发现是 KL 训练产生的 mask 模式与 magnitude-based mask 存在 68% 偏离，且因果消融实验 (C1) 表明 mask 目标质量而非梯度耦合是性能提升的主要驱动力。方法设计合理、实验覆盖面较好，但关键比较依赖单 seed 结果、因果消融存在未充分解决的混淆因子、跨架构泛化结果部分反向，这些统计和实验设计上的不足削弱了核心 claims 的可信度。

---

## Strengths (bulleted)

- **清晰的问题定义与方法动机**：将稀疏预测从 per-neuron 分类问题重新定义为输出分布匹配问题，动机自然，理论推导（§3.6 梯度分析）为方法选择提供了直觉支撑。
- **有洞察力的核心发现**：KL 训练产生的 mask 与 magnitude-based mask 68% 偏离 (§4.4)，这不是一个显而易见的结果，表明训练目标的选择对 mask 质量有本质性影响。
- **系统化的消融设计 (Table 4)**：涵盖 Gumbel vs STE、Forward vs Reverse KL、SPON 贡献、compensation 冗余等多个关键设计选择，实验逻辑清晰。
- **因果消融 (C1) 是有创意的实验设计**：训练 BCE 预测器使用 KL 导出的 oracle mask 来试图解耦 mask 质量和训练目标，方向正确。
- **训练效率极高**：单 GPU ~45 分钟，1000 步即收敛，预测器参数仅占 base model 的 <1%，工程实用性好。
- **Taxonomy (Table 1)** 对现有方法按 correction granularity × training signal coupling 分类，有助于定位本文贡献。
- **引用完整性好**：46 条引用全部通过交叉验证（OpenAlex），无虚构引用，覆盖了 training-free、predictor-based、MoE-based 等所有主要方向。

---

## Weaknesses (bulleted, severity tagged)

### Must-Fix 问题（影响接收决定）

**N1 [critical] 主结果表 (Table 2) 过度依赖单 seed，统计效力不足**
- 具体位置：Table 2 (p6), §4.1, Appendix F (p14)
- 问题：Table 2 中的绝大多数结果使用单一 seed (seed 42)。论文声称 "remaining single-seed entries use seed 42" 并引用 Appendix F 的 3-seed 稳定性验证，但 Appendix F 仅覆盖 50% uniform allocation 的 PPL (CV=0.6%)。
  - 30% sparsity 的 KL vs BCE 比较：BCE 显示 PPL 8.96±0.02 (3-seed)，但 KL 的对应 3-seed 结果未在 Table 2 主表清晰呈现
  - 50% sparsity 的 headline 结果 (KL PPL 11.79 vs BCE 28.13)：BCE 有 3-seed (28.13±0.20)，但 KL 的 11.79 是单 seed 还是 3-seed 不完全清楚
  - 所有 downstream task (ARC, WinoGrande, MMLU, GSM8K) 在 Table 2 中无 multi-seed 标注
- 为什么影响接收：对于一篇核心 claim 是 "KL > BCE" 的论文，方法之间的比较必须有充分的统计支撑。单 seed 结果不能排除特定初始化偶然有利的可能。
- 建议：Table 2 中所有 KL vs BCE 的关键比较点至少 3 seed，报告 mean±std；或者至少对 headline numbers (30% uniform, 50% uniform) 提供完整 multi-seed 数据。

**N2 [critical] C1 因果消融存在未充分解决的混淆因子**
- 具体位置：Table 3 (p7), §4.4-4.5
- 问题 1 — 因果推断的逻辑链条断裂：C1 实验训练 BCE 预测器使用 KL 导出的 oracle mask。论文将 C1 ≈ KL 的结果解读为 "mask target quality, not gradient coupling, drives quality"。但 KL-derived masks 本身就是通过梯度耦合训练发现的。因此 C1 实际上证明的是："KL 训练发现的 mask 可以迁移到 BCE 训练"，而非"梯度耦合不重要"。梯度耦合在 mask 发现阶段是必要的，C1 仅证明在 mask 已知后可用更简单的训练方式。论文的 framing 过度归因于 mask quality 而低估了 KL 训练在发现过程中的不可替代性。
- 问题 2 — Soft-vs-Hard confound 结果反常：§4.5 报告 BCE + Gumbel-Sigmoid = PPL 38.02，反而比 vanilla BCE (27.97) 更差。论文仅说 "softness alone does not explain KL's advantage"，但没有解释为什么 soft relaxation 会**恶化** BCE 的表现。这是一个意外的反向结果，需要分析。如果 Gumbel-Sigmoid relaxation 在 BCE 框架下有害，那么 KL 的优势可能部分来自 KL loss 与 Gumbel 的特殊交互，而非单纯的 "mask quality"。
- 问题 3 — Seed 数量：30% 仅 3 seed，50% 仅 2 seed。对于因果推断性质的实验，这偏少。
- 为什么影响接收：C1 是论文最核心的 claim（Abstract、Introduction、Conclusion 都反复引用），但因果推断的逻辑和实验设计都有明显缺陷。
- 建议：(a) 修正 framing，将 C1 解读为 "mask transferability" 而非 "gradient coupling unimportant"；(b) 分析 BCE+Gumbel 为何恶化——是否因为 Gumbel noise 干扰了 BCE 的 per-neuron 分类目标？(c) 增加 seed 数至至少 5。

**N3 [critical] 跨架构泛化 claim 与实际结果矛盾**
- 具体位置：§4.6 (p8), Abstract, Introduction §1 contributions list
- 问题：
  - Qwen-2.5-14B：PPL 泛化但 MMLU 严重反转 (63.7% vs TEAL 71.8%)，这是 8.1pp 的退步。论文在 §4.6 用一句话带过 ("this reversal is absent at 7B on both architectures, suggesting scale-dependent effects")，但未充分讨论原因。
  - Mistral-7B："wins 5 of 6 downstream tasks at 30%"——第 6 个 task 输了多少？具体数字仅散落在正文中而非结构化表格。
  - Abstract 称 "cross-architecture advantages hold on most tasks across architectures (Mistral-7B, Qwen-2.5-14B)"，但 Qwen 上 MMLU 的严重退步与 "advantages hold" 的描述不符。
- 为什么影响接收：Cross-architecture generalization 是明确列出的 contribution (#4)。当结果部分矛盾时，conclusion 和 abstract 中的 claims 必须准确反映实际情况。
- 建议：(a) 提供 Mistral 和 Qwen 的完整结构化结果表（包含所有 downstream tasks）；(b) 讨论 Qwen MMLU 反转的可能原因（规模效应？Qwen 的 attention 结构差异？训练数据分布？）；(c) 修正 Abstract 和 Introduction 中的 cross-architecture claims，准确反映限制条件。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] "Three regimes" 分析过度拟合稀疏数据点**
- 具体位置：§4.6 (p8), Table 5
- 问题：Table 5 仅包含 4 个 sparsity levels (25%, 30%, 40%, 50%)。从 4 个数据点中识别出 3 个 "regimes"（budget-surplus ≤30%、budget-constrained 35-40%、capacity-limited ≥45%），regime 边界本身就在数据点之间，缺乏统计支撑。
- 建议：增加中间 sparsity 点（35%, 45%）以验证 regime 边界，或弱化 language 为 "trend" 而非 "three distinct regimes"。

**W2 [warning] 无实际推理加速证据**
- 具体位置：Appendix A (p11-12), Table 8
- 问题：Appendix A 明确显示 KL-sparse pipeline 增加了 6.4% 的推理开销（比 dense 更慢）。论文承认 "actual acceleration requires kernel-level sparse computation optimizations" 但声称加速是 "out of scope"。对于标题含 "Contextual Sparsity Prediction" 的论文，不展示实际加速是显著缺陷。
- 建议：至少用 Triton block-sparse 或 cuSPARSE 做一个 proof-of-concept speedup 实验，哪怕是 prototype 级别。

**W3 [warning] SPON 贡献 (2.4%) 可能在噪声范围内**
- 具体位置：Table 4 (p7), §4.5
- 问题：SPON 将 PPL 从 12.08 降至 11.79 (2.4%)，但这是单 seed (seed 42) 在 50% sparsity 下的结果。Appendix F 的 3-seed PPL std 为 ±0.07，2.4% 的改善约为 0.29 PPL points，约 4 倍 std——勉强显著但不够稳健。然而 SPON 被作为方法的标准组成部分。
- 建议：提供 SPON ablation 的 multi-seed 结果，或降低 SPON 在方法中的地位（例如作为 optional component）。

**W4 [warning] PPL 作为主要指标的局限性未在实验分析中充分体现**
- 具体位置：Limitations (p8-9), Table 2, Table 5
- 问题：论文自己在 Limitations 中承认 "perplexity is a poor proxy for reasoning ability at moderate sparsity"。在 50% sparsity 下，所有方法的 MMLU 都坍塌至近随机 (~28%)，但 PPL 仍显示 KL (11.79) 大幅优于 TEAL (23.13)。这意味着 PPL 改善不一定反映实际能力保留。但论文的 headline claims (如 "49% improvement over TEAL") 完全基于 PPL。
- 建议：在 main results 讨论中明确说明 50% sparsity 下 PPL 改善的局限性，引导读者关注 30% 的更可靠结论。

**W5 [warning] Compensation 冗余仅在 50% 验证**
- 具体位置：Table 4 (p7), Appendix I (p14)
- 问题：Table 4 的 ablation 全部在 50% sparsity 下进行。Compensation 冗余的结论是否在 30% 也成立？30% 下 KL 和 BCE 的差距更小 (PPL 8.81 vs 8.96)，compensation 可能在此 regime 下有不同影响。
- 建议：在 30% sparsity 下重复 compensation ablation。

---

### Minor Issues（不影响接收）

- **68% divergence 无置信区间**：§4.4 报告 68% 偏离度测量于 50% sparsity、WikiText-2、单一模型，未报告 bootstrap CI 或 sample variation。
- **Table 2 脚注信息密度过高**：3-seed 范围、seed 编号、Appendix 引用全部挤在脚注中，不如用明确的 ± 标注。
- **§3.6 梯度分析是经验观察而非理论证明**：SNR 5.14x 是实验测量值，但论文的行文方式 ("Gradient analysis reveals a structural asymmetry") 暗示了理论结论。建议明确标注为 empirical observation。
- **Adaptive penalty controller (§3.5) 在 30% target 偏差 5.9% (Table 12)**：虽然 50% 仅 0.8%，但 30% 的偏差较大，正文未提及。
- **Appendix D (OOD evaluation) 仅 2 seed**：Table 13 标注 "2-seed mean±std"，对于 OOD generalization claim 略薄。
- **引用年份小问题**：`loshchilov2019adamw` 在 OpenAlex 记录为 2017 但 bib 写 2019（ICLR 发表年 vs arXiv 年）；`de2024griffin` 在 OpenAlex 未找到精确匹配但确认为真实论文。

---

## Questions for Authors

1. **C1 的反事实问题**：如果从一个随机初始化（而非 KL-trained）的预测器导出 oracle mask 来训练 BCE，质量会如何？这才是真正测试 "mask quality vs gradient coupling" 的控制实验。
2. **BCE + Gumbel 为何恶化**：§4.5 报告 BCE + Gumbel-Sigmoid = 38.02，比 vanilla BCE (27.97) 差。能否解释机制？是 Gumbel noise 与 BCE 的 binary cross-entropy 目标冲突，还是 soft relaxation 导致的梯度问题？
3. **Qwen MMLU 反转的根因**：是 Qwen-2.5-14B 的特殊之处（vocabulary 大小？attention 结构？训练分布？），还是 scale-dependent 的系统性问题？如果是后者，对更大模型意味着什么？
4. **30% vs 50% 的推荐 setting**：论文在不同位置推荐不同 sparsity level（Abstract 同时宣传两者，§4.6 推荐 30%），能否明确在什么条件下推荐哪个？
5. **训练数据的影响**：训练仅使用 WikiText-103，评估使用 WikiText-2 和 downstream tasks。如果换成更大/更多样的训练数据（如 C4），mask 质量和泛化性会如何变化？

---

## Missing References

无重大遗漏。可考虑补充：
- **Dettmers et al. (2022)**: "LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale" — 量化与稀疏的正交关系讨论
- **Xia et al. (2023)**: "Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning" — structured pruning 与 contextual sparsity 的对比

---

## Detailed Comments (per section)

### Abstract
- "diverging 68% from magnitude-based masks" — 应注明仅在 50% sparsity/WikiText-2 上测量
- "cross-architecture advantages hold on most tasks" — 与 Qwen MMLU 反转矛盾，需要限定语

### Introduction (§1)
- Contributions #4 "cross-architecture generalization" 的措辞应反映 Qwen 上的 mixed results
- 逻辑流畅，从问题到方法的过渡自然

### Related Work (§2)
- 组织清晰，Taxonomy 分类有价值
- SPON 和 D2DMoE 的 positioning 准确
- 引用覆盖全面，无明显遗漏

### Method (§3)
- §3.1-3.4 公式定义清晰，Eq.1-6 一致性可验证
- §3.5 Adaptive controller：ε=0.02 deadzone 的选择依据未说明
- §3.6 Gradient analysis：行文风格暗示理论结论但实际是经验观察，应更明确
- §3.7 Taxonomy 很好地定位了贡献

### Experiments (§4)
- §4.1 Setup 详细，超参数基本完整
- §4.2 Main results：Table 2 的 multi-seed 标注不够清晰（N1）
- §4.3 Extended training：BCE 2700 步仍劣于 KL 1000 步，有力支撑 KL 优势
- §4.4 Mask pattern analysis：68% 偏离是有洞察的发现，但统计支撑不足
- §4.5 Ablation：设计全面，但 SPON 贡献和 soft-vs-hard confound 需加强
- §4.6 Scaling & cross-architecture：regime 分析过度拟合，Qwen 结果不支持 claim

### Conclusion (§5)
- 较准确总结了结论，但 "renders compensation redundant" 和 "cross-architecture generalization" 的措辞应加限定

### Limitations
- 诚实指出了 PPL 局限性和 sparse kernel 缺失
- 缺少对统计效力（seed 数量）局限的讨论

### Appendix
- A-I 覆盖了补充实验和鲁棒性分析，组织合理
- 关键: Appendix F 的 3-seed 数据应上浮至主表

---

## Overall Assessment

**Overall**: **3.0 — Findings**

**一句话总结**：核心 idea (KL distillation for sparsity prediction) 有价值，mask 偏离发现有洞察力，但统计支撑不足（单 seed 主结果）、因果消融逻辑有缺陷、跨架构泛化 claim 与数据矛盾，整体处于 Findings 水平。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 方法设计合理，但 C1 因果推断逻辑有缺陷（N2），主结果统计效力不足（N1），cross-architecture claim 与数据矛盾（N3） |
| Excitement | 3/5 | KL 训练发现偏离 magnitude 68% 的 mask 是有洞察力的发现，但无实际推理加速（W2），50% sparsity 下 downstream 能力全面坍塌限制了实用价值 |
| Overall Assessment | 3.0 | Findings 水平。核心方向正确，实验覆盖面尚可，但三个 critical issues (N1-N3) 需要解决才能达到 Conference 级别 |
| Confidence | 4/5 | 熟悉 LLM 推理加速、知识蒸馏、activation sparsity 相关文献 |
| Reproducibility | 3/5 | 超参数和训练配置基本完整，但 evaluation protocol 细节（few-shot 设置、exact prompt templates）不够清晰，代码未开源 |

---

**升级到 Conference (3.5+) 的路径**：
1. Table 2 关键比较加 3+ seed（最高优先级）
2. 修正 C1 framing 或补充更强的控制实验
3. 提供 Mistral/Qwen 完整结构化结果表并诚实讨论局限
4. 弱化 regime 分析为 "observed trend"


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

_source line 906 · 2026-05-19T06:32:22.522459+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 69

## Round 69

2 recorded events


### User

_source line 907 · 2026-05-19T06:32:25.172204+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交至 Review Director。

核心结论：**Overall 3.0 (Findings)**。论文方向正确、mask 偏离发现有洞察，但三个 critical issues 需要解决：(1) 主结果表单 seed 统计效力不足；(2) C1 因果消融逻辑链有缺陷且 soft-vs-hard confound 未解释；(3) 跨架构泛化 claim 与 Qwen MMLU 8.1pp 退步矛盾。解决这些问题后有望升至 Borderline Conference (3.5)。

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

_source line 908 · 2026-05-19T06:32:30.916351+00:00_

Reviewer 1 已返回，评分 3.0 (Findings)。等待 Reviewer 2 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 70

## Round 70

6 recorded events


### User

_source line 909 · 2026-05-19T06:32:45.288265+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2: Round 1 审稿意见

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 via ARR May 2026 cycle
**审查侧重**: 新颖性/贡献显著性 + 写作质量 + Related Work 完整性 + 格式合规

---

## Summary (2-3 sentences)

本文提出用 forward KL divergence + Gumbel-Sigmoid 松弛训练轻量 sparsity predictor，替代传统 BCE 目标，用于 SwiGLU LLM 的 activation sparsity 预测。核心发现是 KL 训练发现了与 magnitude 偏离 68% 的 mask pattern，causal ablation 表明 mask target 质量（而非梯度耦合）是质量优势的主要驱动力。实验覆盖 3 个架构（7B-14B），但实际加速未实现，且 14B 规模出现 downstream 反转。

---

## Strengths

- **设计精良的 causal ablation (C1)**：用 BCE 在 KL-derived targets 上训练来分离 target quality 和 gradient coupling，是论文最有说服力的实验设计（Table 3，§4.4）。50% sparsity 下 C1 与 KL 完全匹配（max Δ=0.59pp），有力支撑了核心 claim。
- **多维度实验覆盖**：3 个架构（LLaMA-8B, Mistral-7B, Qwen-14B），6 个 sparsity 级别（25%-70%），3-seed 评估，两种 allocation 策略，消融覆盖 divergence 方向/relaxation/compensation/hyperparameter，实验系统性强。
- **诚实的 claim 边界**：论文明确承认 "Our contribution is empirical"（Introduction L18），诚实报告了 50% downstream collapse、14B MMLU 反转、无 wall-clock speedup、C4 OOD gap 等负面结果。这在同类论文中少见。
- **mask divergence 发现有洞察力**：KL mask 与 magnitude mask 68% 偏离、U-shaped per-layer divergence pattern（Figure 6, §4.4）是对 sparsity prediction 文献的有用贡献。
- **写作无 AI 痕迹**：em-dash 0 处、en-dash 0 处、黑名单词 0 处、过度过渡词 0 处。在当前审稿环境下这是显著优势。
- **Related Work 全面且有组织**：6 个段落覆盖 training-free、predictor-based、static bias、activation engineering、weight pruning/distillation、MoE routing，positioning 清晰。与 MaskLLM 的三点区分（sparsity type、mask generation、allocation）具体且令人信服。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1** [critical] Abstract 严重数据堆砌，叙事被淹没
- 具体位置：abstract.tex 全文
- 问题：Abstract 约 170 词中塞入了至少 15 个数字（68%、32%、0.59pp、1.70pp、28.13±0.20、18%、7.5×、86.0%、92.5%、49%、9.0pp、63.7%、71.8% 等）。Abstract 读起来像 results 的缩写而非独立叙事单元。按论文写作规范 §2.2："Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim"。
- 为什么影响接收：审稿人在 30 秒内无法从这个 Abstract 判断论文的核心价值。"方法是否清楚"和"贡献是否可信"两项检验均因数字过密而失败。
- 建议修改方向：保留 3 个最关键数字（mask 68% 偏离、PPL 49% 改善、compensation 冗余），其余用定性描述替代。重写为 problem → insight → method → key finding 的四段式叙事。

**N2** [critical] 49% PPL improvement 的 headline 数字具有误导性
- 具体位置：Abstract L5, Introduction L14, §4.2 (Table 2)
- 问题：49% PPL 改善来自 50% sparsity（11.79 vs 23.31），但在这个 regime 下所有方法的 MMLU 均崩溃至随机水平（28.1% vs 28.0%），GSM8K < 2.2%。论文自身在 §4.2 和 §4.6 承认这是 "capacity-limited regime where no allocation strategy can recover"。实际可用的操作点是 30%，改善仅为 18%。将 49% 放在 Abstract 和 Introduction 最显眼位置，而将 30% 的 18% 放在次要位置，会误导读者对方法实际价值的判断。
- 为什么影响接收：reviewer 会认为 framing 不诚实，即使数据本身是正确的。这是 claim overclaiming 而非数据造假，但对信任损害很大。
- 建议修改方向：以 30% sparsity 作为主要 claim 支撑点（这是实际有用的 regime），50% 作为分析补充。Abstract 和 Introduction 的主叙事应围绕 30% 展开。

**N3** [critical] 14B scale-dependent downstream 反转未被充分分析
- 具体位置：§4.6 最后一段, Appendix Table 8
- 问题：Qwen-2.5-14B 上 KL 的 MMLU 从 TEAL 的 71.8% 降至 63.7%（-8.1pp），但 PPL 仍从 8.73 改善到 7.62。这是一个 PPL-downstream disconnect，论文仅用 "warrants further investigation" 一笔带过。然而 Contribution 3 声称分析了 "scale-dependent effects at 14B"，实际只是报告了现象而未提供解释机制。
- 为什么影响接收：如果方法在规模放大时 downstream 性能系统性反转，那么方法的实际价值和可推广性就存在根本问题。14B 上 BCE 的 MMLU 也是 71.67%（接近 TEAL），说明 KL 的 mask pattern 在更大模型上可能系统性地损害需要精确知识检索的任务。这不是一个可以推迟到 future work 的问题。
- 建议修改方向：(1) 分析 14B 上 KL mask 与 magnitude mask 的 per-layer divergence pattern 是否与 8B 不同；(2) 检查 14B 上 KL 的 layer retention 分布；(3) 至少提供一个假说并用已有数据验证/排除。

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] C1 ablation 的 soft-vs-hard confound 削弱因果推断强度
- 具体位置：§4.4 "Soft-vs-Hard Confound" 段落
- 问题：C1 同时改变了 target quality 和 mask representation（hard binary vs soft Gumbel-Sigmoid）。论文用 BCE+Gumbel（PPL 38.02）作为控制，证明 softness alone 不够，但这只排除了一个替代假说，未完全分离。如果 KL 的优势部分来自 soft mask 在特定 target 上的 gradient landscape 优势，而非 target quality 本身，C1 无法检测到。论文诚实承认 "Disentangling target quality from gradient representation remains for future work"，但 claim 的措辞（"provides evidence that...target quality...is the primary driver"）暗示的确定性高于实际证据强度。
- 建议：将措辞从 "provides evidence that target quality is the primary driver" 弱化为 "is consistent with target quality as a major contributing factor"，或补充一个实验：用 KL targets + Gumbel-Sigmoid BCE 训练，与 KL targets + hard BCE (C1) 对比。

**W2** [warning] 实际可用 sparsity 窗口狭窄
- 具体位置：§4.2, §4.6, Limitations
- 问题：30% 是唯一 downstream 性能合理的 sparsity 级别。25% 改善微小（PPL 差 0.06），35%+ 开始 MMLU 下降，50% 彻底崩溃。这意味着方法的 practical operating window 非常窄，且 30% sparsity 的实际推理加速（不考虑 sparse kernel）几乎为零。
- 建议：在 Conclusion 或 Limitations 中明确讨论 practical operating window，而非让读者自行从分散的数据中推断。

**W3** [warning] 30% global allocation 的 MMLU 高 seed variance
- 具体位置：Table 2, §4.2
- 问题：30% global 的 MMLU σ=9.5pp（3-seed，范围 25.3-43.5%），这是异常高的方差。论文建议使用 uniform allocation 来规避，但这意味着 global allocation（论文的主要推理协议）在最有用的 sparsity 级别上是不可靠的。
- 建议：报告 30% global 的 per-seed MMLU 具体数值（而不仅是均值±std），分析 seed-dependent failure mode。

**W4** [warning] 主表缺少 HellaSwag 和 PIQA
- 具体位置：Table 2 (§4.2)
- 问题：HellaSwag 和 PIQA 是评估 LLM 非推理能力的核心 benchmark，论文在正文中引用了它们的 retention 率（86.0%, 92.5%），但数据放在 Appendix Table 6。主表只有 ARC-c、WG、MMLU、GSM8K。对于声称分析 "allocation-to-downstream interactions" 的论文，6 个 benchmark 中只在主表展示 4 个不够完整。
- 建议：用 6-column 表或 split 表在主表中包含所有 6 个 downstream benchmark。

**W5** [warning] BCE 和 PPL 在 Abstract 中未定义
- 具体位置：abstract.tex L2 ("BCE"), L4 ("PPL")
- 问题：Abstract 是独立阅读单元，首次出现的缩写必须展开。BCE (binary cross-entropy) 和 PPL (perplexity) 在 Abstract 中直接使用未定义。虽然 PPL 在 NLP 社区广泛理解，但 BCE 在 Abstract 上下文中可能被误解（信息论中 BCE 还有其他含义）。
- 建议：Abstract 中用全称 "binary cross-entropy (BCE)" 和 "perplexity (PPL)"。

**W6** [warning] Taxonomy (Table 1) 人为构建感
- 具体位置：§3.7, Table 1
- 问题："Intermediate (MSE)" 列只有 2 个方法（ShadowLLM, D2DMoE），Static×Decomposed 和 Static×Intermediate 格为空。这个 2×3 矩阵中只有 4 个格被填充，三分之一为空。更重要的是，MSE "intermediate coupling" 与 KL "coupled" 的边界不够清晰：为什么 layer-local MSE 不算 coupled？D2DMoE 在 layer 内部的 expert routing 也涉及 inter-neuron 依赖。
- 建议：(1) 讨论空格为什么为空（是理论上不可能还是尚未探索？）；(2) 更清晰地定义 "coupling" 的边界（单层内 vs 跨层）。

### Minor 问题（不影响接收）

- **M1**: 符号不一致——§3.1 用 $\mathbf{x}^{(\ell)}$ 表示 "hidden state after attention"，§3.2 用 $\mathbf{h}$ 表示 "pre-FFN hidden state"。两者应为同一量，但符号切换造成混淆。
- **M2**: "KL" (Kullback-Leibler) 全文未展开定义。虽然广泛使用，但作为核心方法术语应在首次出现时给出全称。
- **M3**: TEAL、SPON 作为缩写仅通过引用出现，未展开。建议至少在 Related Work 首次出现时给出全称。
- **M4**: Table 3 (C1 ablation) 在 30% 的 KL 行中 ARC-c、WG、GSM8K 显示 "---"。缺失的数据削弱了 C1 ablation 在 30% 下的说服力。如果这些数据存在，应补充；如果不存在，需要解释原因。
- **M5**: Introduction 第 2 段和贡献列表之间有轻微冗余——mask divergence 68%、causal ablation、compensation redundancy 各出现两次。
- **M6**: §3.5 adaptive penalty controller 的 footnote 声明 "resembles the augmented Lagrangian method"，但正文称 "Adaptive Penalty Sparsity Controller"。terminology 不够统一——建议统一为一个名称并明确声明不是 formal Lagrangian。
- **M7**: references.bib 中 `gu2024minillm` 的标题与 OpenAlex 记录不完全匹配（bib: "Knowledge Distillation" vs API: "On-Policy Distillation"），可能是论文后来改标题。

---

## Questions for Authors

1. **14B MMLU 反转的机制**：Qwen-14B 上 KL 的 PPL 优于 TEAL (7.62 vs 8.73) 但 MMLU 显著劣于 TEAL (63.7% vs 71.8%)。这种 PPL-downstream disconnect 是否在 14B 的其他 downstream tasks 上也存在？能否提供 14B per-layer mask divergence 数据与 8B 对比？
2. **C1 完整数据**：Table 3 的 30% KL 行缺少 ARC-c、WG、GSM8K。这些数据是否可用？如果 C1 在某些 task 上偏离 KL 超过 1.70pp，会影响 "target quality is the primary driver" 的 claim。
3. **Mask divergence 的训练动态**：68% divergence 是训练结束时测量的。KL mask 是从训练一开始就偏离 magnitude，还是在训练过程中逐渐偏离？early checkpoint 的 Jaccard 数据能帮助理解机制。
4. **为什么不评估 N:M structured sparsity？** 论文在 Limitations 提到 N:M 作为 future work，但 MaskLLM 已经证明 KL 在 N:M 上有效。如果方法能泛化到 N:M，practical impact 会大幅提升。
5. **Penalty controller 在 30% 的 5% deviation**：实际 sparsity 28.5% vs target 30%。虽然论文论证了这对 TEAL baseline 比较影响很小，但这意味着 KL predictor 实际上在更低的 sparsity 下运行——公平比较要求 TEAL 也在 28.5% 评估。

---

## Missing References

引用覆盖总体充分（46 条，通过 OpenAlex 验证 40 条确认真实存在）。以下可能遗漏的工作供参考：

- **Griffin (de2024griffin)** 在 OpenAlex 中未找到匹配，但 arXiv 上确实存在（2402.19427）。这是一个 verification tool 的限制而非引用问题。
- 未引用 **FLAP** (An et al., ICML 2024) 和 **OWL** (Yin et al., 2024)——两者是 structured pruning 方法，与本文 activation sparsity 方向不同，但如果 Related Work 声称覆盖 weight pruning，可以考虑补充。
- 未引用 **Deja Vu 2.0 / SpInfer** 等更近期的 predictor-based contextual sparsity 工作（如果存在的话）。
- MaskLLM 之外，**SparseFlow** (Zhang et al., 2025) 等 learnable mask + KL training 的工作是否存在？建议作者确认。

总体引用密度与 EMNLP 近年录用论文量级匹配。

---

## Detailed Comments (per section)

### Abstract
- 数据堆砌问题见 N1。
- 缺 BCE/PPL 展开（W5）。
- 叙事弧度不清：读者无法在 30 秒内回答 "这篇论文为什么重要"。

### Introduction
- 五段结构基本完整：背景(P1) → 问题(P1-2) → 洞察(P2) → 方法实例化(P3) → 贡献列表。
- P2-P3 之间的过渡略显突兀：从 "mask pattern divergence" 直接跳到 "We instantiate..."，缺少一个 "Therefore, we propose..." 的桥接。
- Contribution 3 ("Analysis of allocation-to-downstream interactions at 7-14B") 在前文没有铺垫。按写作规范 §3.3："Contribution 列表中不能出现未在前文铺垫过的概念"。
- 49% headline 问题见 N2。

### Related Work
- 组织结构清晰，6 段落主题分明。
- 与 MaskLLM 的区分（三点）是论文最重要的 positioning，写得具体且有说服力。
- D2DMoE 的 positioning 可以更精确：论文说 "intermediate coupling (MSE on hidden states) but not end-to-end output effects"，但 D2DMoE 实际上将 dense layer 转换为 MoE，这不仅仅是 MSE supervision 的问题。
- 最后一段（MoE Routing）的 Griffin 引用感觉勉强——RG-LRU 的 gating 与 SwiGLU activation sparsity 的关系很间接。

### Method
- 数学叙述清晰，公式推导合理。
- §3.5 adaptive penalty controller 是非标准方法（非正式 Lagrangian），footnote 的 disclaimer 是好的做法。
- §3.6 gradient analysis 的定位恰当——"suggestive; §4.4 provides causal evidence" 避免了 overclaiming。
- Table 1 taxonomy 见 W6。
- Figure 1 信息密度适中，但 caption 可以更自包含（当前不解释 "TEAL's global top-k allocation"）。

### Experiments
- Table 2 格式清晰，bold/footnote 使用得当。但 caption 过长（5 行），建议精简。
- §4.3 extended training analysis 是有用的控制实验（iso-compute comparison）。
- §4.4 mask pattern analysis 和 C1 ablation 是论文的核心贡献，分析质量高。
- §4.6 allocation behavior 的三 regime 划分（budget-surplus / budget-constrained / capacity-limited）有洞察力。
- 缺少统计显著性检验：多处比较（如 C1 vs KL）仅报告点估计差异，未做 paired test。

### Conclusion
- 简洁（2 句话），涵盖核心发现。但过于压缩——缺少对方法局限性和未来方向的一句话总结。

### Limitations
- 全面且诚实，覆盖了几乎所有主要弱点。
- 14B 反转在这里被承认但分析不足（见 N3）。
- 对 OOD 的讨论很好（C4 gap = 1.74× vs 1.46×）。

### Ethics & Checklist
- 完整且认真填写，未发现遗漏。

---

## 格式合规检查

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 正文 ≤8 页 | ✅ | Section 5 (Conclusion) 结束于 p8 上半，Limitations 从 p8 开始 |
| ACL template [review] | ✅ | `\usepackage[review]{acl}` (main.tex L2) |
| Limitations 位置 | ✅ | Conclusion 之后、References 之前 |
| 行号开启 | ✅ | PDF 渲染确认可见 |
| 引用格式 (natbib) | ✅ | 一致使用 `\cite{}` |
| 匿名化 | ✅ | `\author{Anonymous}`，正文无 de-anonymization |
| 图表字体 ≥7pt | ✅ | 视觉检查 Figure 1, 2 和所有 Tables 字体可读 |
| 附录内容在正文中被引用 | ✅ | 所有 13 个 Appendix section 均在正文中有 explicit reference |
| 引用交叉检查 | ✅ | 46 bib entries 全部被引用，0 orphan，0 missing |
| 双栏格式 | ✅ | 符合 ACL 标准 |

---

## Overall Assessment

**Overall**: **3.0 (Findings)**
**Confidence**: 4/5

**一句话总结**: 实验设计周密、分析诚实的 empirical study，但方法新颖性有限（已知组件的自然组合）、实际可用窗口狭窄（仅 30%）、无 wall-clock speedup、且在更大规模出现未解释的 downstream 反转，更适合 Findings。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 核心 claim 有实验支撑，C1 ablation 设计精良，但 soft-vs-hard confound 未完全解决，14B 反转未分析，49% headline 来自 downstream-collapsed regime |
| **Excitement** | 2.5/5 | Mask divergence 发现有分析价值，但方法是 KL+Gumbel+MLP 的直接组合，无 wall-clock speedup，practical window 仅 30%，对社区的实际推动有限 |
| **Reproducibility** | 4/5 | 超参数完整报告，3-seed 评估，GPU 型号/训练时间/batch size 均明确。代码未发布但信息足以复现 |
| **Confidence** | 4/5 | 熟悉 activation sparsity 和 KD 文献，仔细核实了核心实验数据和 claim |

### 评分理由展开

**为什么不是 3.5 (Borderline Conference)**：
- 方法新颖性不足以支撑 Main：每个组件（KL distillation、Gumbel-Sigmoid、MLP predictor、global top-k）都是已有技术，组合虽然合理但缺少技术 surprise。
- 没有 wall-clock speedup 意味着这是一个"分析为主"的论文，但分析的 actionable insight 有限——实践者从论文中学到的是"用 KL 替代 BCE"，这是一个 recipe 而非 principle。
- 14B downstream 反转是一个 red flag：方法在最有价值的方向（更大模型）上表现退化。

**为什么不是 2.5 (Borderline Findings)**：
- C1 causal ablation 的实验设计有 genuine intellectual merit。
- 实验系统性和诚实度在同类论文中属上游。
- Mask divergence 的发现和三 regime allocation 分析对后续工作有参考价值。
- 写作质量高，无 AI 痕迹，格式完全合规。

**如果以下问题在 rebuttal 中得到解决，评分可上调至 3.5**：
1. 14B 反转有合理解释和初步数据支撑（N3）
2. Abstract 重写为叙事驱动（N1）
3. 主 claim 重新围绕 30% sparsity 构建（N2）


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

_source line 910 · 2026-05-19T06:33:22.559345+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。特别关注你们观点有分歧的地方。\n\n---\n\n# Reviewer 2 完整审稿意见\n\n## Summary\n本文提出用 forward KL divergence + Gumbel-Sigmoid 松弛训练轻量 sparsity predictor，替代传统 BCE 目标，用于 SwiGLU LLM 的 activation sparsity 预测。核心发现是 KL 训练发现了与 magnitude 偏离 68% 的 mask pattern，causal ablation 表明 mask target 质量（而非梯度耦合）是质量优势的主要驱动力。实验覆盖 3 个架构（7B-14B），但实际加速未实现，且 14B 规模出现 downstream 反转。\n\n## Strengths\n- 设计精良的 causal ablation (C1)\n- 多维度实验覆盖\n- 诚实的 claim 边界\n- mask divergence 发现有洞察力\n- 写作无 AI 痕迹\n- Related Work 全面且有组织\n\n## Weaknesses\n\n### Must-Fix\n\n**N1** [critical] Abstract 严重数据堆砌，叙事被淹没\n- Abstract 约 170 词中塞入至少 15 个数字。读起来像 results 缩写而非独立叙事单元。审稿人 30 秒内无法判断论文核心价值。\n\n**N2** [critical] 49% PPL improvement 的 headline 数字具有误导性\n- 49% PPL 改善来自 50% sparsity（11.79 vs 23.31），但此 regime 下所有方法 MMLU 崩溃至随机水平。实际可用操作点是 30%，改善仅 18%。将 49% 放在最显眼位置会误导读者。\n\n**N3** [critical] 14B scale-dependent downstream 反转未被充分分析\n- Qwen-14B MMLU 从 TEAL 71.8% 降至 KL 63.7%（-8.1pp），但 PPL 仍改善。Contribution 3 声称分析 \"scale-dependent effects\" 但实际只报告现象未解释机制。\n\n### Should-Fix\n\n**W1** C1 ablation 的 soft-vs-hard confound 削弱因果推断强度\n**W2** 实际可用 sparsity 窗口狭窄（仅 30%）\n**W3** 30% global allocation 的 MMLU 高 seed variance (σ=9.5pp)\n**W4** 主表缺少 HellaSwag 和 PIQA\n**W5** BCE 和 PPL 在 Abstract 中未定义\n**W6** Taxonomy (Table 1) 人为构建感\n\n### Minor\n- M1: 符号不一致 (x^(ℓ) vs h)\n- M2: KL 未展开定义\n- M3: TEAL/SPON 缩写未展开\n- M4: Table 3 30% KL 行缺 ARC-c/WG/GSM8K\n- M5: Introduction 冗余\n- M6: Penalty controller terminology 不统一\n- M7: bib 标题不完全匹配\n\n## Questions for Authors\n1. 14B MMLU 反转机制 + per-layer mask divergence 数据？\n2. Table 3 30% KL 行缺失数据？\n3. Mask divergence 训练动态（early checkpoint Jaccard）？\n4. 为什么不评估 N:M structured sparsity？\n5. Penalty controller 30% 的 5% deviation 对公平比较的影响？\n\n## Missing References\n- FLAP (An et al., ICML 2024), OWL (Yin et al., 2024)\n- SparseFlow (Zhang et al., 2025) — 如存在\n\n## Overall Assessment\n**3.0 (Findings)**, Confidence 4/5\nSoundness 3.5, Excitement 2.5, Reproducibility 4\n\n---\n\n请对以上每个 N/W/M/Q 逐条回应 [AGREE] 或 [REBUT]。",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
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
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。特别关注你们观点有分歧的地方。\n\n---\n\n# Reviewer 2 完整审稿意见\n\n## Summary\n本文提出用 forward KL divergence + Gumbel-Sigmoid 松弛训练轻量 sparsity predictor，替代传统 BCE 目标，用于 SwiGLU LLM 的 activation sparsity 预测。核心发现是 KL 训练发现了与 magnitude 偏离 68% 的 mask pattern，causal ablation 表明 mask target 质量（而非梯度耦合）是质量优势的主要驱动力。实验覆盖 3 个架构（7B-14B），但实际加速未实现，且 14B 规模出现 downstream 反转。\n\n## Strengths\n- 设计精良的 causal ablation (C1)\n- 多维度实验覆盖\n- 诚实的 claim 边界\n- mask divergence 发现有洞察力\n- 写作无 AI 痕迹\n- Related Work 全面且有组织\n\n## Weaknesses\n\n### Must-Fix\n\n**N1** [critical] Abstract 严重数据堆砌，叙事被淹没\n- Abstract 约 170 词中塞入至少 15 个数字。读起来像 results 缩写而非独立叙事单元。审稿人 30 秒内无法判断论文核心价值。\n\n**N2** [critical] 49% PPL improvement 的 headline 数字具有误导性\n- 49% PPL 改善来自 50% sparsity（11.79 vs 23.31），但此 regime 下所有方法 MMLU 崩溃至随机水平。实际可用操作点是 30%，改善仅 18%。将 49% 放在最显眼位置会误导读者。\n\n**N3** [critical] 14B scale-dependent downstream 反转未被充分分析\n- Qwen-14B MMLU 从 TEAL 71.8% 降至 KL 63.7%（-8.1pp），但 PPL 仍改善。Contribution 3 声称分析 \"scale-dependent effects\" 但实际只报告现象未解释机制。\n\n### Should-Fix\n\n**W1** C1 ablation 的 soft-vs-hard confound 削弱因果推断强度\n**W2** 实际可用 sparsity 窗口狭窄（仅 30%）\n**W3** 30% global allocation 的 MMLU 高 seed variance (σ=9.5pp)\n**W4** 主表缺少 HellaSwag 和 PIQA\n**W5** BCE 和 PPL 在 Abstract 中未定义\n**W6** Taxonomy (Table 1) 人为构建感\n\n### Minor\n- M1: 符号不一致 (x^(ℓ) vs h)\n- M2: KL 未展开定义\n- M3: TEAL/SPON 缩写未展开\n- M4: Table 3 30% KL 行缺 ARC-c/WG/GSM8K\n- M5: Introduction 冗余\n- M6: Penalty controller terminology 不统一\n- M7: bib 标题不完全匹配\n\n## Questions for Authors\n1. 14B MMLU 反转机制 + per-layer mask divergence 数据？\n2. Table 3 30% KL 行缺失数据？\n3. Mask divergence 训练动态（early checkpoint Jaccard）？\n4. 为什么不评估 N:M structured sparsity？\n5. Penalty controller 30% 的 5% deviation 对公平比较的影响？\n\n## Missing References\n- FLAP (An et al., ICML 2024), OWL (Yin et al., 2024)\n- SparseFlow (Zhang et al., 2025) — 如存在\n\n## Overall Assessment\n**3.0 (Findings)**, Confidence 4/5\nSoundness 3.5, Excitement 2.5, Reproducibility 4\n\n---\n\n请对以上每个 N/W/M/Q 逐条回应 [AGREE] 或 [REBUT]。",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 911 · 2026-05-19T06:33:48.535690+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25976
}
```

</details>

---


### Tool call

_source line 912 · 2026-05-19T06:33:49.190664+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。特别关注你们观点有分歧的地方。\n\n---\n\n# Reviewer 1 完整审稿意见\n\n## Summary\n本文提出用 KL 散度蒸馏训练 SwiGLU LLM 的轻量级稀疏性预测器，核心发现是 KL 训练产生的 mask 模式与 magnitude-based mask 存在 68% 偏离，且 C1 因果消融表明 mask 目标质量而非梯度耦合是性能提升主要驱动力。方法设计合理、实验覆盖面较好，但关键比较依赖单 seed、因果消融存在未充分解决的混淆因子、跨架构泛化结果部分反向。\n\n## Strengths\n- 清晰的问题定义与方法动机\n- 有洞察力的核心发现（68% mask 偏离）\n- 系统化消融设计\n- 因果消融 C1 实验设计有创意\n- 训练效率高（单 GPU 45min）\n- Taxonomy 分类有价值\n- 引用完整（46条全验证）\n\n## Weaknesses\n\n### Must-Fix\n\n**N1** [critical] 主结果表 (Table 2) 过度依赖单 seed，统计效力不足\n- Table 2 绝大多数结果使用 seed 42。Appendix F 仅覆盖 50% uniform PPL。30% KL vs BCE、50% KL headline 的 multi-seed 标注不清楚。下游 task 无 multi-seed 标注。\n\n**N2** [critical] C1 因果消融存在未充分解决的混淆因子\n- 问题 1：因果推断逻辑链断裂——KL-derived masks 本身通过梯度耦合训练发现，C1 仅证明 mask 可迁移到 BCE，不等于\"梯度耦合不重要\"\n- 问题 2：BCE+Gumbel=38.02 比 vanilla BCE (27.97) 更差，未解释为何 soft relaxation 恶化 BCE\n- 问题 3：30% 仅 3 seed，50% 仅 2 seed\n\n**N3** [critical] 跨架构泛化 claim 与实际结果矛盾\n- Qwen MMLU -8.1pp\n- Mistral GSM8K 反转\n- Abstract \"advantages hold on most tasks\" 与数据不符\n\n### Should-Fix\n\n**W1** \"Three regimes\" 从 4 个数据点过度拟合（Table 5 仅 25/30/40/50%）\n**W2** 无实际推理加速（+6.4% overhead）\n**W3** SPON 贡献 2.4% 可能在噪声范围内\n**W4** PPL 作为主要指标的局限性未在实验分析中充分体现\n**W5** Compensation 冗余仅在 50% 验证\n\n### Minor\n- 68% divergence 无置信区间\n- Table 2 脚注过长\n- §3.6 SNR 是经验观察非理论证明\n- Adaptive penalty 30% 偏差 5%\n- OOD 仅 2 seed\n- 引用年份小问题\n\n## Questions for Authors\n1. C1 反事实：随机初始化预测器导出 oracle mask 训练 BCE 结果？\n2. BCE+Gumbel 为何恶化的机制？\n3. Qwen MMLU 反转根因？\n4. 30% vs 50% 推荐设置？\n5. 训练数据影响（WikiText-103 vs C4）？\n\n## Missing References\n- Dettmers et al. (2022) LLM.int8()\n- Xia et al. (2023) Sheared LLaMA\n\n## Overall Assessment\n**3.0 (Findings)**, Confidence 4/5\nSoundness 3, Excitement 3, Reproducibility 3\n\n---\n\n请对以上每个 N/W/M/Q 逐条回应 [AGREE] 或 [REBUT]。",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
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
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。特别关注你们观点有分歧的地方。\n\n---\n\n# Reviewer 1 完整审稿意见\n\n## Summary\n本文提出用 KL 散度蒸馏训练 SwiGLU LLM 的轻量级稀疏性预测器，核心发现是 KL 训练产生的 mask 模式与 magnitude-based mask 存在 68% 偏离，且 C1 因果消融表明 mask 目标质量而非梯度耦合是性能提升主要驱动力。方法设计合理、实验覆盖面较好，但关键比较依赖单 seed、因果消融存在未充分解决的混淆因子、跨架构泛化结果部分反向。\n\n## Strengths\n- 清晰的问题定义与方法动机\n- 有洞察力的核心发现（68% mask 偏离）\n- 系统化消融设计\n- 因果消融 C1 实验设计有创意\n- 训练效率高（单 GPU 45min）\n- Taxonomy 分类有价值\n- 引用完整（46条全验证）\n\n## Weaknesses\n\n### Must-Fix\n\n**N1** [critical] 主结果表 (Table 2) 过度依赖单 seed，统计效力不足\n- Table 2 绝大多数结果使用 seed 42。Appendix F 仅覆盖 50% uniform PPL。30% KL vs BCE、50% KL headline 的 multi-seed 标注不清楚。下游 task 无 multi-seed 标注。\n\n**N2** [critical] C1 因果消融存在未充分解决的混淆因子\n- 问题 1：因果推断逻辑链断裂——KL-derived masks 本身通过梯度耦合训练发现，C1 仅证明 mask 可迁移到 BCE，不等于\"梯度耦合不重要\"\n- 问题 2：BCE+Gumbel=38.02 比 vanilla BCE (27.97) 更差，未解释为何 soft relaxation 恶化 BCE\n- 问题 3：30% 仅 3 seed，50% 仅 2 seed\n\n**N3** [critical] 跨架构泛化 claim 与实际结果矛盾\n- Qwen MMLU -8.1pp\n- Mistral GSM8K 反转\n- Abstract \"advantages hold on most tasks\" 与数据不符\n\n### Should-Fix\n\n**W1** \"Three regimes\" 从 4 个数据点过度拟合（Table 5 仅 25/30/40/50%）\n**W2** 无实际推理加速（+6.4% overhead）\n**W3** SPON 贡献 2.4% 可能在噪声范围内\n**W4** PPL 作为主要指标的局限性未在实验分析中充分体现\n**W5** Compensation 冗余仅在 50% 验证\n\n### Minor\n- 68% divergence 无置信区间\n- Table 2 脚注过长\n- §3.6 SNR 是经验观察非理论证明\n- Adaptive penalty 30% 偏差 5%\n- OOD 仅 2 seed\n- 引用年份小问题\n\n## Questions for Authors\n1. C1 反事实：随机初始化预测器导出 oracle mask 训练 BCE 结果？\n2. BCE+Gumbel 为何恶化的机制？\n3. Qwen MMLU 反转根因？\n4. 30% vs 50% 推荐设置？\n5. 训练数据影响（WikiText-103 vs C4）？\n\n## Missing References\n- Dettmers et al. (2022) LLM.int8()\n- Xia et al. (2023) Sheared LLaMA\n\n## Overall Assessment\n**3.0 (Findings)**, Confidence 4/5\nSoundness 3, Excitement 3, Reproducibility 3\n\n---\n\n请对以上每个 N/W/M/Q 逐条回应 [AGREE] 或 [REBUT]。",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 913 · 2026-05-19T06:33:50.699191+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1508
}
```

</details>

---


### Assistant

_source line 914 · 2026-05-19T06:33:54.311864+00:00_

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


## Round 71

## Round 71

2 recorded events


### User

_source line 915 · 2026-05-19T06:33:56.963925+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**: Overall 3.0 (Findings)，Soundness 3.5，Excitement 2.5，Confidence 4/5。

**三个 Must-Fix 问题**：
1. Abstract 严重数据堆砌（15+ 个数字），叙事被淹没
2. 49% PPL improvement 的 headline 来自 downstream 全面崩溃的 50% regime，实际可用的 30% 仅改善 18%，framing 有误导性
3. 14B Qwen 上 MMLU -8.1pp 反转仅用 "warrants further investigation" 带过，缺乏机制分析

**主要优势**：C1 causal ablation 设计精良，实验系统全面且诚实，写作干净无 AI 痕迹，格式完全合规。

**判断**：方法是已知组件的自然组合（KL+Gumbel+MLP），无 wall-clock speedup，practical window 仅 30%，更适合 Findings 而非 Main。若 rebuttal 能解释 14B 反转并重构叙事，可上调至 3.5。

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

_source line 916 · 2026-05-19T06:34:02.307951+00:00_

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


## Round 72

## Round 72

2 recorded events


### User

_source line 917 · 2026-05-19T06:36:56.765298+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 → Reviewer 1 交叉回应

---

## Must-Fix 问题

### [REBUT] R1-N1: 主结果表 (Table 2) 过度依赖单 seed

R1 的描述部分不准确。Table 2 的 seed 覆盖情况如下：

**30% sparsity**（论文实际推荐的操作点）：
- KL global: 8.96±0.02, ARC 43.8±3.6, WG 70.2±0.9, MMLU 35.7±9.5, GSM8K 8.0±0.7 — **全部 3-seed**
- KL uniform: 8.81±0.02, ARC 43.7±2.5, WG 68.9±0.4, MMLU 40.7±1.3, GSM8K 7.5±0.1 — **全部 3-seed**
- BCE global†: 单 seed — 这是 baseline 比较，合理

**50% sparsity**：
- KL global: PPL 11.79 报告 seed 42，但 Appendix E 提供完整 3-seed 数据：PPL CV<1%, MMLU 28.1±0.2（s42=27.89, s123=28.34, s456=27.94），加上 downstream ARC 33.8±1.2, WG 62.9±0.1, GSM8K 2.2±0.1
- BCE+comp: 28.13±0.20 — **3-seed**

**TEAL vanilla**: 确定性方法（training-free），无 seed 变异，单次运行即完整。

因此 R1 说"绝大多数结果使用 seed 42"不准确。30% 的所有 KL 行（8 个 metric-method 组合）均为 3-seed；50% 的 3-seed 数据在 Appendix E 中完整呈现。真正的 gap 是 30% BCE baseline 为单 seed 和 50% KL 在主表中仅报告 seed 42（虽然 appendix 有完整 3-seed）。

**我的评价**：R1 对统计严谨性的关注是合理的，但将问题严重程度定为 "critical" 过重。建议降级为 Should-Fix：作者应将 50% KL 的 3-seed 数据从 Appendix E 提升到主表，并补充 30% BCE 的 multi-seed 数据。

---

### [AGREE] R1-N2: C1 因果消融存在未充分解决的混淆因子

同意这是论文最核心的方法论弱点。与我的 W1 一致。

**R1-N2-Issue 1（因果推断逻辑链断裂）**：[AGREE] 这是比我的表述更精确的批评。论文的推理是：KL 发现好 masks → C1 证明 BCE 在这些 masks 上匹配 KL → 因此 target quality 而非 gradient coupling 是 driver。但 gradient coupling 是发现这些好 masks 的 *必要条件*，所以它在训练阶段仍然 "重要"。论文的 claim 应更精确地限定为：**在 inference 时的质量**由 mask target quality 决定，而非 training 时 gradient coupling 不重要。论文 §4.4 的措辞 "target quality, not gradient coupling, as the primary driver" 确实没有区分这两个阶段。

**R1-N2-Issue 2（BCE+Gumbel 恶化）**：[REBUT] 论文 §4.5 "Loss Function Isolation" 段落确实给出了解释："the penalty interferes with per-neuron optimization without global coordination"。逻辑是：Gumbel-Sigmoid 需要配合 global penalty controller 来强制 sparsity，但 BCE 的 per-neuron 独立梯度无法有效响应这个 global penalty，导致两者冲突。这个解释虽然简短但合理。不过我同意 R1 的隐含观点——这个解释缺少实验验证（例如：如果去掉 penalty 只保留 Gumbel，BCE 表现如何？）。

**R1-N2-Issue 3（seed 数量）**：[AGREE] 30% 3-seed, 50% 2-seed 确实偏少，尤其是 C1 是论文的核心 claim 支撑。但需注意 Table 3 在 30% 已有 3 个完整 seed（s42, s123, s456），其中 max Δ=1.70pp (s42 MMLU)。这不是"仅 3 seed"——对于这种消融实验 3 seed 是合理下限。50% 的 2 seed 确实薄弱。

**总结**：N2 是有效的 critical issue，但 R1 三个子问题中 Issue 2 的严重程度被高估（论文有解释，只是不够充分）。

---

### [AGREE] R1-N3: 跨架构泛化 claim 与实际结果矛盾

完全同意，与我的 N3 一致。补充一个 R1 未提及的细节：

Qwen-14B 上不仅 KL MMLU 反转（63.7% vs TEAL 71.8%），**BCE 在 14B 上 MMLU 达到 71.67%**（Appendix Table 8），几乎匹配 TEAL。这说明在 14B 规模上，magnitude-based masks（BCE 和 TEAL 共享的 target）对 MMLU 这类知识密集型任务更有效。KL 的 mask divergence 在大模型上可能系统性地伤害知识检索任务。这不是简单的噪声或 architecture-specific artifact，而是一个需要正面应对的 scaling concern。

Abstract 的 "advantages hold on most tasks" 措辞确实有问题，但值得公平地指出：Abstract 紧接着就用分号列出了两个反转（Mistral GSM8K 和 Qwen MMLU）。不是隐藏了负面结果，而是 framing 的轻重缓急有偏差。

---

## Should-Fix 问题

### [REBUT] R1-W1: "Three regimes" 从 4 个数据点过度拟合

R1 说 Table 5 仅有 25/30/40/50% 共 4 个数据点。这不准确。

Table 5（主文 §4.6）展示 25%、30%、35%、50% 四个代表性 sparsity 级别，但论文明确引导读者查看完整数据："full 6-level data with all downstream metrics in Appendix Table 7"（Table 5 caption）。Appendix Table 7（app:alloc_full）报告了 **25%、30%、35%、40%、45%、50%** 共 6 个 sparsity 级别的全部 downstream metrics（PPL + ARC + WG + MMLU + GSM8K）。

6 个数据点支撑 3 个 regime 的划分：
- Budget-surplus (25-30%): 2 点
- Budget-constrained (35-40%): 2 点
- Capacity-limited (45-50%): 2 点

每个 regime 有 2 个内部数据点佐证，加上 regime 之间的 transition 可观察，这在 sparsity 分析中是合理的分辨率。R1 应阅读 Appendix Table 7 后再评价。

---

### [AGREE] R1-W2: 无实际推理加速

与我的审查意见完全一致。论文诚实承认这一点（Appendix A, Limitations），但作为 efficiency 论文无 speedup 确实是显著弱点。

---

### [AGREE] R1-W3: SPON 贡献 2.4% 可能在噪声范围内

同意。§4.5 报告 SPON 贡献为 12.08→11.79 (0.29 PPL absolute, 2.4% relative)，但这是单 seed 比较，无置信区间。footnote 进一步指出这 0.29 gap "reflects allocation protocol"（evaluate.py per-token vs benchmark_eval.py TEAL allocation），暗示测量协议差异可能混入。

不过论文的 framing 已经是 "optional, marginal component (2.4%)"（§4.6），并未将 SPON 作为核心贡献宣传。降级为 Minor 更合适。

---

### [AGREE] R1-W4: PPL 作为主要指标的局限性未在实验分析中充分体现

同意。论文在 Limitations 中承认 "perplexity is a poor proxy for reasoning ability at moderate sparsity"，但实验分析中仍以 PPL 为主要 metric 驱动 claim（如 49% 改善、regime 分析）。§4.6 的 three regime 分析同时包含 PPL 和 MMLU，这是好的做法，但 §4.2 main results 的叙事过度依赖 PPL 优势。

---

### [REBUT] R1-W5: Compensation 冗余仅在 50% 验证

这是一个事实错误。§4.5 "Compensation Redundancy" 明确写道：

> "Adding compensation (+67.2M params) to KL provides no benefit at **either tested sparsity**: at 50%, all five metrics are identical to KL-only; **at 30%, PPL 8.97±0.01 vs. 8.96±0.03 (2-seed)**."

Compensation 冗余在 30% 和 50% **两个** sparsity level 均得到验证，且 30% 有 2-seed（s42 和 s456，对应 exp_id: kl_comp_30_s42, kl_comp_30_s456）。R1 似乎遗漏了这一句。

---

## Minor 问题

**[AGREE] 68% divergence 无置信区间**：合理关注。§4.4 报告 "64 samples, 131K tokens" 的均值但无 CI。作者应补充 bootstrap CI。

**[AGREE] Table 2 脚注过长**：与我的审查一致。5 行 caption 信息过载。

**[REBUT] §3.6 SNR 是经验观察非理论证明**：论文 §3.6 已明确定位为 "suggestive; §4.4 provides causal evidence"，且 SNR 在脚注中给出了严格数学定义。论文没有声称 SNR 是理论证明，而是作为 gradient structure 的经验度量辅助 intuition。R1 对此的期望超出了论文实际 claim 的范围。

**[REBUT] Adaptive penalty 30% 偏差 5%**：Appendix C 已详细分析：TEAL 在插值 28.5% 实际 sparsity 下 PPL≈10.7（vs 30% 的 10.97），差距 <0.3 PPL，远小于 KL vs TEAL 的差距（8.96 vs 10.97）。论文提供了定量论证这个偏差可忽略。

**[AGREE] OOD 仅 2 seed**：合理。C4 评估（Appendix D）30% 为 2-seed (16.03±0.01)，50% 为单 seed。

**[AGREE] 引用年份小问题**：Minor，不影响实质。

---

## Questions for Authors

**Q1（随机 mask 的 C1 反事实）**：[AGREE] 这是一个很好的控制实验建议。如果随机初始化预测器的 oracle mask 训练 BCE 也能匹配 KL，那么 "KL discovers better targets" 的 claim 就会被严重削弱。如果（更可能的结果）随机 mask BCE 很差，则进一步支撑 KL target 的质量确实来自 KL 训练过程。建议作者在 rebuttal 中补充这个实验。

**Q2（BCE+Gumbel 恶化机制）**：[AGREE] 如上述 N2-Issue 2 的回应。论文有解释但不够充分。

**Q3（Qwen MMLU 反转根因）**：[AGREE] 与我的 N3 完全一致。这是最需要在 rebuttal 中回答的问题。

**Q4（30% vs 50% 推荐设置）**：[AGREE] 论文数据明确指向 30% 是实际可用的操作点，但没有明确声明。实践者读完论文会困惑应该用哪个设置。

**Q5（训练数据影响）**：[AGREE] WikiText-103 作为训练集的局限性值得探讨。C4 OOD 数据（Appendix D）显示 gap 从 1.46× 扩大到 1.74×，说明训练域确实影响泛化。

---

## Missing References

**[REBUT] LLM.int8() (Dettmers et al., 2022)**：这是量化（quantization）论文，不是 activation sparsity。论文的 scope 是 "contextual sparsity prediction"，Related Work 覆盖的是 sparsity methods，不需要覆盖量化文献。Wang et al. (2025) 已被引用来处理 sparsity-quantization 交叉。

**[AGREE] Sheared LLaMA (Xia et al., 2023)**：与已引用的 MiniTron (Muralidharan et al., 2024) 方向相同（structured pruning + continued pretraining/distillation），可以补充但非关键遗漏。

---

## Overall Assessment 对比

| 维度 | R1 | R2 (我) | 差异分析 |
|------|-----|---------|----------|
| Overall | 3.0 | 3.0 | 一致：Findings |
| Soundness | 3.0 | 3.5 | R1 偏低：30% 的 3-seed 覆盖和 C1 ablation 的设计质量未被充分认可。N1 对 seed 的批评部分基于对 Table 2 caption 和 Appendix E 的不完整阅读 |
| Excitement | 3.0 | 2.5 | 我偏低：方法是已知组件组合，无 speedup，practical window 狭窄 |
| Reproducibility | 3.0 | 4.0 | R1 偏低：论文报告了完整的 hyperparameters（db=128, τ schedule, lr, wd, batch, seq_len, GPU 型号），3-seed 覆盖核心实验，training time 精确到分钟。Reproducibility 3 对这种报告水平不公平 |
| Confidence | 4 | 4 | 一致 |

**综合判断**：两位 reviewer 在 Overall 3.0 (Findings) 上完全一致。主要分歧在于 R1 对 seed 覆盖的批评过于严厉（N1 可降级为 Should-Fix），以及 R1 对 Reproducibility 的评分偏低。核心一致点：C1 confound (N2)、跨架构泛化问题 (N3)、无实际加速 (W2) 是论文最大的弱点。

建议 Director 将 N2（C1 confound）和 N3（14B 反转）作为 rebuttal 的最高优先级要求。


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

_source line 918 · 2026-05-19T06:37:02.479556+00:00_

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


## Round 73

## Round 73

2 recorded events


### User

_source line 919 · 2026-05-19T06:37:08.570489+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结关键分歧和共识：

**与 R1 一致**（7 条 AGREE）：
- N2 (C1 confound) — 论文最核心的方法论弱点，因果推断链断裂
- N3 (跨架构泛化矛盾) — 14B MMLU 反转未充分分析
- W2 (无加速), W3 (SPON 噪声), W4 (PPL 局限), Q1-Q5

**反驳 R1**（4 条 REBUT）：
- **N1 (单 seed)**：R1 低估了 Table 2 的 multi-seed 覆盖——30% KL 全部 8 个 metric-method 组合均为 3-seed，50% 在 Appendix E 有完整 3-seed 数据。建议从 critical 降为 should-fix。
- **W1 (三 regime 过拟合)**：R1 说 4 个数据点，实际 Appendix Table 7 有 6 个 sparsity 级别的完整数据。
- **W5 (compensation 仅 50%)**：事实错误——§4.5 明确报告 30% 和 50% 两个 sparsity level 的结果。
- **Missing ref (LLM.int8())**：量化论文，不在 activation sparsity scope 内。

**Overall 一致**：3.0 Findings。建议 rebuttal 优先回应 C1 confound 和 14B 反转。

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

_source line 920 · 2026-05-19T06:37:14.204486+00:00_

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


## Round 74

## Round 74

10 recorded events


### User

_source line 921 · 2026-05-19T06:38:21.650250+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条交叉回应

---

## Must-Fix

### R2-N1: Abstract 严重数据堆砌

**[REBUT] 同意现象，不同意严重性。**

R2 的观察是准确的——我重新计数，Abstract ~170 词中包含约 20+ 个数字（68%、50%、0.99pp、2-seed、30%、1.7pp、3-seed、28.13±0.20、<1%、+67.2M、18%、7.5×、86.0%、92.5%、49%、5/6、14B、63.7%、71.8% 等），确实高于正常密度。

但我不同意将此升级为 **Must-Fix (critical)**：
1. **不影响技术正确性或可信度**——这是 presentation 问题而非 soundness 问题。将其与 N2（misleading framing）和 N3（generalization claim 与数据矛盾）并列为 critical 不合比例。
2. **信息本身是有用的**——Abstract 中的数字虽多，但每个都服务于一个 claim（mask divergence、C1 验证、compensation 冗余、两个 sparsity 级别的结果、cross-architecture）。问题不在于数字太多，而在于 claim 太多——作者试图在 Abstract 中塞入了所有贡献。
3. **真正的修复方向**：削减 contribution 数量（从 4 个 claims 砍到 2-3 个核心 claims），数字自然减少。这是 Should-Fix 级别。

**建议调整为 Should-Fix。**

---

### R2-N2: 49% PPL improvement 的 headline 数字具有误导性

**[AGREE] 完全同意，且我在 R1-W4 中提出了类似但更温和的版本。**

R2 的分析比我更到位。核心矛盾：
- 50% sparsity 下 PPL 确实改善 49%（11.79 vs 23.31），但 MMLU 对所有方法均坍塌至 ~28%（近随机）
- 30% sparsity 是实际可用操作点，PPL 改善仅 18%
- Abstract 和 Introduction 均将 49% 放在最显眼位置（§1: "PPL improves to 11.79 (49% over TEAL)"）

我补充一点证据支持 R2：论文自己在 Limitations (p9) 承认 "perplexity is a poor proxy for reasoning ability at moderate sparsity"。如果作者自己认为 PPL 在 50% 下不可靠，那么将 50% 的 PPL 改善作为 headline 就存在内部矛盾。

**同意 Must-Fix 级别。** 建议：将 30% 的结果（18% PPL + downstream 保持 86-92% retention）作为 headline，50% 结果降级为补充发现。

---

### R2-N3: 14B scale-dependent downstream 反转未被充分分析

**[AGREE] 完全同意，与我的 R1-N3 一致。**

补充我的发现：
- Conclusion (p9) 写 "PPL generalizes but downstream reversal at 14B (Qwen MMLU 63.7% vs. TEAL's 71.8%) warrants further investigation"——但 "warrants further investigation" 是审稿人写 review 时的措辞，不是作者应该写在论文里的话。
- Introduction (p2) Contribution #4 声称 "cross-architecture generalization"，但 p8 §4.6 仅用一句话处理 Qwen 反转（"this reversal is absent at 7B on both architectures, suggesting scale-dependent effects"）。
- Mistral-7B 的结果散落在正文中（"wins 5 of 6 downstream tasks, HellaSwag +8.5pp, ARC +0.9pp, WG +5.6pp, PIQA +1.1pp"）而非结构化表格，第 6 个 task 的输赢未报告。

R2 和我的一致诊断：这是一个 **claim-evidence mismatch**——contribution 声称 generalization，但数据部分反向，且反向结果未被充分解释。

---

## Should-Fix

### R2-W1: C1 ablation 的 soft-vs-hard confound 削弱因果推断强度

**[AGREE] 同意，且我在 R1-N2 中将此问题的严重性评估更高（critical）。**

R2 将此列为 Should-Fix，但我认为这应该是 Must-Fix：
- C1 实验是论文最核心的因果 claim（Abstract、Introduction、Conclusion 反复引用）
- §4.5 报告 BCE + Gumbel-Sigmoid = PPL 38.02，比 vanilla BCE (27.97) **更差**。论文未解释为什么 soft relaxation 会恶化 BCE。这不是小细节——如果 Gumbel 在 BCE 下有害，那 KL 的优势可能部分来自 KL loss 与 Gumbel 的特殊协同效应，而非纯粹的 "mask target quality"
- C1 的因果推断逻辑也有问题：KL-derived masks 本身就是通过梯度耦合训练发现的，所以 C1 证明的是 "mask transferability" 而非 "gradient coupling unimportant"

**建议 R2 将此从 Should-Fix 升级为 Must-Fix。**

---

### R2-W2: 实际可用 sparsity 窗口狭窄（仅 30%）

**[REBUT] 部分同意观察，不同意这是独立的 weakness。**

R2 的观察本身准确：50% 下 MMLU 坍塌，30% 是唯一 "safe" 操作点。但：
1. 这不是本方法的特殊缺陷——**所有方法**（包括 TEAL、BCE）在 50% 下 MMLU 都坍塌。这是 activation sparsity 在当前 LLM 上的固有限制。
2. 论文在 §4.6 和 Limitations 中明确推荐 30% 作为最佳操作点，并说明 40% 是 "best-quality sparsity level for downstream fidelity"。
3. 本文的贡献在于改善了给定 sparsity 水平下的质量，而非扩展可用 sparsity 范围。

这与 N2（misleading headline）有重叠——如果修复了 N2（不再以 49%/50% 为 headline），W2 的担忧自然减轻。**建议合并入 N2 的修改建议中。**

---

### R2-W3: 30% global allocation 的 MMLU 高 seed variance (σ=9.5pp)

**[REBUT] 现象准确，但论文已明确回应了这一问题。**

验证 R2 的数据：Table 5 脚注 "High seed variance 25.5-43.5%"——3 seed MMLU 范围为 25.5%~43.5%，σ≈9.5pp，R2 计算正确。

但论文的处理是合理的：
- §4.6 (p8) 的核心分析点就是 global vs uniform allocation 的比较
- 论文明确指出：uniform allocation 在 30% 下 MMLU σ = 1.3pp（7.5× 更小），推荐使用 uniform
- 高 seed variance 是 **global allocation 的问题**，不是 KL 方法的问题——它反映了 global top-k 在低 sparsity 下的不稳定性
- 论文将此作为 "why uniform is preferable at 30%" 的证据，而非隐藏它

真正的问题是：**TEAL 在 30% global 下的 seed variance 是多少？** 如果 TEAL global 的 variance 同样高，那这是 allocation 策略的固有问题；如果 TEAL 更稳定，那 KL predictor 的 global allocation 可能有特殊的不稳定性。论文没有报告这个对照数据。

**建议弱化为 Minor + 要求补充 TEAL global 30% 的 seed variance 数据。**

---

### R2-W4: 主表缺少 HellaSwag 和 PIQA

**[AGREE] 合理要求。**

Abstract (p1) 引用了 HellaSwag (86.0% retention) 和 PIQA (92.5%)，但 Table 2 (p6) 仅包含 ARC-c、WinoGrande、MMLU、GSM8K。Appendix H (Table 14) 有 HellaSwag 和 PIQA 数据。

如果一个指标重要到出现在 Abstract 中，它应该在主表中。这是 internal consistency 问题。

---

### R2-W5: BCE 和 PPL 在 Abstract 中未定义

**[REBUT] 不同意这是一个实际问题。**

BCE (Binary Cross-Entropy) 和 PPL (Perplexity) 是 NLP/ML 社区的标准缩写，使用频率与 SGD、MLP、GPU 同级。在 ACL/EMNLP 投稿中，无需在 Abstract 中展开这两个缩写。

我检查了 3 篇 EMNLP 2024/2025 录用论文（activation sparsity 相关），均直接使用 PPL 而不展开。

更合理的缩写问题是 **KL** 本身——论文全文（包括标题 "Output-Distribution Distillation"）从未在 Abstract 或 Introduction 中写出 "Kullback-Leibler divergence" 的完整形式（仅在 §3.4 标题 "KL Divergence Training Objective" 首次暗示）。同样，**TEAL** 和 **SPON** 也从未展开。这些比 BCE/PPL 更需要定义，因为它们是特定系统名称。

**建议将 W5 替换为：KL、TEAL、SPON 应在首次使用时展开。BCE/PPL 无需展开。**

---

### R2-W6: Taxonomy (Table 1) 人为构建感

**[REBUT] 不同意是实质性问题。**

Table 1 沿 "correction granularity（per-layer vs per-token）× training signal coupling（decoupled BCE / intermediate MSE / coupled KL）" 分类现有方法。R2 说它有 "人为构建感"。

我的评价不同：
1. **分类本身合理**——correction granularity 和 training signal 确实是区分现有方法的两个有意义的维度。DejaVu (per-token, BCE) vs SPON (per-layer, independent) vs D2DMoE (per-layer, MSE) 确实落在不同格子里。
2. **"我填空缺格"是标准的 positioning 技巧**——几乎所有提出新方法的论文都会构建一个让自己位于独特位置的 taxonomy。只要分类维度本身合理，这不是问题。
3. **替代方案更差**——如果没有 Table 1，读者更难理解本方法与 DejaVu/FastForward/ShadowLLM/SPON 的差异。

Table 1 实际上是本文 Related Work 组织得当的体现，不是缺陷。**建议删除此条。**

---

## Minor Issues

### R2-M1: 符号不一致 (x^(ℓ) vs h)

**[AGREE]** 如果存在，应统一。我在审阅中未特别注意到此处不一致，但如果 h 用于 hidden state 而 x^(l) 用于层输入且两者指代相同概念，则应统一。

### R2-M2: KL 未展开定义

**[AGREE]** 如上（W5 回应中）所述，KL 应在首次使用时展开为 "Kullback-Leibler (KL) divergence"。

### R2-M3: TEAL/SPON 缩写未展开

**[AGREE]** 同 M2。TEAL 和 SPON 是特定系统名，应在首次引用时展开（如有 acronym 含义的话）。

### R2-M4: Table 3 30% KL 行缺 ARC-c/WG/GSM8K

**[AGREE]** 因果消融 (C1) 声称比较 C1 vs KL，但如果 KL 行在 30% 只报告了 PPL 和 MMLU 而缺少 ARC-c/WG/GSM8K，则比较不完整。Table 3 caption 声称 "Max Δ±1.7pp (+42 MMLU) at 30%"——如果其他 downstream tasks 的 Δ 更大或方向不同，这可能改变 C1 的结论。

### R2-M5: Introduction 冗余

**[REBUT]** 我认为 Introduction 的结构合理——从 SwiGLU FFN 的 sparsity 现象出发，到 BCE 的局限，到 KL 的提出，到贡献列表。~1.5 页的 Introduction 对于 long paper 是正常长度。可能有个别句子重复 Abstract 内容，但不构成结构性冗余。

### R2-M6: Penalty controller terminology 不统一

**[AGREE]** §3.5 标题 "Adaptive Penalty Sparsity Controller"，脚注 4 说 "We term it an adaptive penalty controller"，但 Appendix C 标题 "Adaptive Penalty Controller Dynamics"。如果这几处名称不一致（例如有时叫 "Lagrangian controller"），应统一。

### R2-M7: bib 标题不完全匹配

**[AGREE]** 我的引用验证发现 5 条 OpenAlex mismatch（主要是作者名格式），属于 minor 但应修复。

---

## Questions for Authors 回应

### R2-Q1: 14B MMLU 反转机制 + per-layer mask divergence

**[AGREE]** 这是非常好的问题，我在 R1-Q3 中提出了几乎相同的问题。per-layer mask divergence 分析（Qwen vs LLaMA 对比）可能揭示反转是否来自特定层的 mask 质量退化。

### R2-Q2: Table 3 30% KL 行缺失数据

**[AGREE]** 同 M4。如果 KL 行缺失 3 个 downstream metrics，应补全。

### R2-Q3: Mask divergence 训练动态（early checkpoint Jaccard）

**[AGREE]** 好问题。论文报告了最终 Jaccard (68% divergence)，但未展示训练过程中 mask 如何从 magnitude-similar 逐渐偏离。这会强化 "KL discovers novel patterns" 的叙事——如果偏离在训练前期就出现，说明这不是 overfitting；如果只在后期出现，机制解释不同。Appendix G 有 SNR 动态但没有 Jaccard 动态。

### R2-Q4: 为什么不评估 N:M structured sparsity

**[REBUT] 范围问题，不是遗漏。**

N:M structured sparsity（如 NVIDIA 2:4）是一个有意义的方向，但与本文研究的 unstructured activation sparsity 是不同的问题设置：
- N:M 是 weight-level 的静态结构化剪枝，硬件有原生支持（Ampere Tensor Cores）
- 本文研究的是 activation-level 的 input-dependent 动态稀疏，目前没有硬件原生支持
- 两者的 oracle mask 定义、训练目标、推理协议都不同

论文 Conclusion (p9) 已将此列为 future work（"structured sparsity for hardware-native acceleration"）。作为 reviewer，我认为不能要求一篇论文同时解决 unstructured 和 structured sparsity。

### R2-Q5: Penalty controller 30% 的 5% deviation 对公平比较的影响

**[AGREE]** 我在 Minor issues 中也指出了这点。Table 12 显示 30% target 实际达到 28.5%（偏差 5.9%）。如果 TEAL 严格执行 30%，而 KL predictor 实际只剪 28.5%，那 KL 在 30% 的 PPL 优势有部分来自"少剪了一些"。论文应报告 TEAL 在 28.5% 下的 PPL 作为 sanity check，或在 Table 2 中标注实际 sparsity。

---

## Missing References 回应

### FLAP (An et al., ICML 2024)

**[REBUT]** FLAP 是 structured weight pruning 方法（对 weight 做 structured column removal），与本文的 unstructured activation sparsity 不在同一问题空间。Related Work §2 已包含对 weight pruning 类别的讨论（"Weight Pruning, Distillation, and Routing"），引用了 Wanda、SparseGPT 等。FLAP 的缺失不构成 coverage gap。

### OWL (Yin et al., 2024)

**[AGREE]** OWL 研究 non-uniform layerwise sparsity allocation，与本文 §4.6 的 global vs uniform allocation 分析直接相关。OWL 发现不同 layer 对剪枝的敏感度不同，应使用 non-uniform 分配——这正是本文 global allocation 的理论基础。缺少 OWL 的引用是一个遗漏。

### SparseFlow (Zhang et al., 2025)

**[REBUT]** R2 自己注明"如存在"。我未找到该论文的可靠引用。不应将不确定是否存在的论文列为 missing reference。

---

## 综合评估与 R2 评分对比

| 维度 | R1 评分 | R2 评分 | 差异分析 |
|------|---------|---------|----------|
| Soundness | 3/5 | 3.5/5 | R2 偏高——C1 confound 和 single-seed 问题值得更低的 soundness |
| Excitement | 3/5 | 2.5/5 | R2 偏低——mask divergence 发现有真正的洞察价值 |
| Overall | 3.0 | 3.0 | **一致** |
| Confidence | 4/5 | 4/5 | 一致 |
| Reproducibility | 3/5 | 4/5 | R2 偏高——evaluation protocol 细节（few-shot 设置、prompt templates）未充分报告 |

**关键分歧**：
1. **R2 对 C1 confound 的严重性低估**：R2 列为 Should-Fix (W1)，我列为 Must-Fix (N2)。鉴于 C1 是论文最核心的因果 claim，soft-vs-hard confound 和因果推断逻辑问题应为 critical。
2. **R2 对 Abstract 写作问题的严重性高估**：R2 列为 Must-Fix (N1)，我认为应为 Should-Fix。Presentation 问题不应与 soundness/methodology 问题并列为同一严重级别。
3. **R2 对 Excitement 偏低 (2.5)**：mask divergence 发现（68% 偏离 magnitude masks）是一个非显然的实证结果，对理解 sparsity prediction 有真正价值。即使实际加速未实现，这一发现本身值得高于 2.5 的 excitement。


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

_source line 922 · 2026-05-19T06:38:58.673372+00:00_

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

_source line 923 · 2026-05-19T06:38:58.724091+00:00_

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

_source line 924 · 2026-05-19T06:39:01.592547+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
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
    "query": "read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-19T06:39:01.694279+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 926 · 2026-05-19T06:41:49.741119+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 11 (fresh review) — New and recurring issues\n  # ============================================================\n\n  - id: \"R11-N1\"\n    summary: \"C1 causal ablation: inference logic flawed (mask transferability ≠ gradient coupling unimportant) + soft-vs-hard confound + BCE+Gumbel反常未解释\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. R1 raised as N2 (Must-Fix), R2 raised as W1 (Should-Fix) then upgraded in cross-response. Core issue: C1 proves mask transferability, not that gradient coupling is unimportant — KL gradient coupling is necessary to discover the masks in the first place. BCE+Gumbel=38.02 (worse than vanilla BCE 27.97) unexplained. 50% only 2-seed.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-N2\"\n    summary: \"14B Qwen MMLU -8.1pp reversal: only 'warrants further investigation', no mechanism analysis; Contribution 3 claim-evidence mismatch\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. BCE on 14B achieves MMLU 71.67% (matching TEAL 71.83%), suggesting KL mask patterns systematically harm knowledge-intensive tasks at scale. PPL-downstream disconnect at 14B is not noise. Abstract 'advantages hold on most tasks' contradicts data.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-N3\"\n    summary: \"49% PPL headline from downstream-collapsed 50% regime is misleading; actual useful 30% improvement is only 18%\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. R2 raised as N2, R1 fully agreed in cross-response citing internal contradiction with Limitations section. Paper itself says 'PPL is poor proxy' but leads with 49% PPL claim from regime where MMLU≈random.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W1\"\n    summary: \"Abstract severe data overload: ~15+ numbers in 170 words, reads like results summary not narrative\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"R2 raised as Must-Fix N1, R1 rebuts to Should-Fix (presentation not soundness). Director resolves as Should-Fix: real fix is reducing claim count from 4 to 2-3, numbers follow. Both agree Abstract fails 30-second readability test.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W2\"\n    summary: \"50% KL 3-seed data buried in Appendix E; main table reports seed 42 only. 30% BCE baseline single-seed.\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"R1 raised as Must-Fix N1, R2 rebuts: 30% KL rows ARE all 3-seed (8 metric-method combinations), TEAL is deterministic. Real gap: 50% KL main table only shows s42 (appendix has 3-seed), 30% BCE is single-seed. Director resolves as Should-Fix.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W3\"\n    summary: \"No wall-clock speedup: pipeline adds 6.4% overhead; sparse kernel integration absent\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. Paper honestly disclaims but for a sparsity prediction paper, no speedup demo is significant weakness.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W4\"\n    summary: \"PPL as primary metric limitation not reflected in experimental narrative (50% claims based on PPL only)\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. Overlaps with N3. Paper acknowledges in Limitations but experimental narrative §4.2 still PPL-driven.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W5\"\n    summary: \"HellaSwag and PIQA cited in Abstract (86.0%, 92.5%) but absent from main Table 2; internal consistency issue\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. If metric important enough for Abstract, should be in main table.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W6\"\n    summary: \"Table 3 C1 ablation at 30%: KL rows missing ARC-c, WG, GSM8K — incomplete causal comparison\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. Max Δ=1.70pp claim based on MMLU only; other tasks could show larger delta.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-M1\"\n    summary: \"Minor writing issues: symbol inconsistency (x^ℓ vs h), KL/TEAL/SPON never expanded, Table 2 caption overloaded, penalty controller terminology inconsistent\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Collection of minor issues. Both agree KL should be expanded as Kullback-Leibler at first use. TEAL/SPON are system names needing expansion. §3.1 x^(ℓ) and §3.2 h refer to same quantity.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-M2\"\n    summary: \"68% mask divergence lacks confidence interval; SPON 2.4% contribution possibly within noise (single-seed)\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"R1 raised both. R2 agrees on 68% CI, agrees SPON is minor since paper frames as optional. Bootstrap CI on Jaccard needed.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Prior issues — status updates from Round 11 fresh review\n  # ============================================================\n\n  - id: \"R9-N1\"\n    summary: \"C1 causal ablation: 2-seed insufficient for 'proves' claim + soft-vs-hard mask confound uncontrolled\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1 raised as Must-Fix N1 (2-seed + soft-vs-hard confound + 30% PPL gap). R2 initially Should-Fix W1, upgraded to AGREE with R1 in cross-response.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed. R1 new finding: soft-vs-hard confound (KL uses soft Gumbel, C1 BCE uses hard targets). 30% PPL gap +0.63 flagged.\"}\n      - {round: 11, reviewers: [1, 2], note: \"Reconfirmed as R11-N1. C1 now 3-seed at 30% and 2-seed at 50%. soft-vs-hard confound paragraph added (§4.5) but logic issue remains: paper claims 'target quality not gradient coupling' but gradient coupling is necessary to discover the targets. BCE+Gumbel=38.02 反常 still unexplained mechanistically.\"}\n    action_items:\n      - {round: 10, action: \"C1@30% s123 + s456 experiments dispatched (41718:0,1). Achieves 3-seed at 30%.\", assigned_to: \"main_agent\", status: done}\n      - {round: 10, action: \"全文 proves/confirms → provides evidence/supports\", assigned_to: \"paper_agent\", status: done}\n      - {round: 10, action: \"§4.4 新增 soft-vs-hard confound 讨论 + bce_gumbel PPL=38.02 反证\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-N2\"\n    summary: \"BCE baseline pipeline inconsistent across sparsity levels: 30% uses TEAL/no-comp, 50% uses DejaVu+comp/no-TEAL\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1 raised as Must-Fix N3. R2 missed in initial review, AGREE in cross-response.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed. Missing 50% BCE+TEAL global baseline.\"}\n      - {round: 11, reviewers: [], note: \"Not explicitly raised as separate issue in R11 fresh review. Table 2 now has clearer footnotes distinguishing pipelines. Pipeline difference remains but is documented.\"}\n    action_items:\n      - {round: 10, action: \"bce_50pct_teal_global_unified eval dispatched (34887:0). Uses benchmark_eval.py unified protocol.\", assigned_to: \"main_agent\", status: in_progress}\n      - {round: 10, action: \"Table 1 caption 显著标注 pipeline 差异\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-N3\"\n    summary: \"Narrow usable range (only 30%, ~2pp downstream gain) + 50% framing bias in Abstract + no wall-clock speedup\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1-N4 + R2-N2 + R2-N3 converged.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed. Abstract still leads with 50% PPL as narrative climax.\"}\n      - {round: 11, reviewers: [1, 2], note: \"Reconfirmed as R11-N3. Abstract now includes 30% results but still foregrounds 49% PPL from 50% regime. Both reviewers flag internal contradiction with Limitations section.\"}\n    action_items:\n      - {round: 10, action: \"Abstract 二次调整：30% downstream quality 为核心 take-away，50% PPL 降为次要\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-N4\"\n    summary: \"Method novelty insufficient for Main: KL+Gumbel+predictor = existing components, MaskLLM overlap\"\n    category: method\n    severity: critical\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R2 raised as Must-Fix N1. R1 REBUT on severity but AGREE on substance.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed. Both agree Findings-appropriate, not Main. Positioning issue, not fixable.\"}\n      - {round: 11, reviewers: [2], note: \"R2 reconfirms: 'method is natural combination of known components, no technical surprise'. R1 acknowledges but values empirical contribution higher. Both agree Findings-appropriate.\"}\n    action_items: []\n    resolution: \"Positioning issue — not addressable through revision. Findings accepted as realistic target.\"\n    resolution_round: 10\n\n  - id: \"R8-N2\"\n    summary: \"14B MMLU reversal: KL PPL best but MMLU -8.1pp vs TEAL\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Full consensus.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Reconfirmed. Abstract now states gap but no mechanism.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Must-Fix N2. Needs full paragraph + mechanism hypotheses.\"}\n      - {round: 11, reviewers: [1, 2], note: \"Reconfirmed as R11-N2. R2 adds: BCE on 14B MMLU=71.67% matches TEAL, suggesting magnitude-based masks systematically better for knowledge tasks at scale. 'warrants further investigation' is reviewer language, not author language. Still no mechanism analysis.\"}\n    action_items:\n      - {round: 8, action: \"Restrict scope to 7-8B primary.\", assigned_to: \"paper_agent\", status: done}\n      - {round: 10, action: \"§4.5 新增 1 段 14B mechanism discussion (knowledge density + domain bias hypotheses)\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 10, action: \"Abstract 明确提及 downstream reversal\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W2\"\n    summary: \"50% downstream collapse contradicts Abstract emphasis on 49% PPL advantage\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R2-W1, R1 AGREE.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Narrative still leads with 50%. R9-N3.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed. Abstract二次调整 dispatched.\"}\n      - {round: 11, reviewers: [1, 2], note: \"Still present. Abstract includes 30% results now but 49%/50% remains prominent. Tracked in R11-N3.\"}\n    action_items:\n      - {round: 8, action: \"Give downstream collapse equal prominence.\", assigned_to: \"paper_agent\", status: done}\n      - {round: 10, action: \"Abstract 二次调整：30% 为核心，50% 降级\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Statistical power: key comparisons partially single-seed\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 11\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Improved: 30% KL global 3-seed.\"}\n      - {round: 8, reviewers: [1, 2], note: \"30% KL uniform now 3-seed.\"}\n      - {round: 9, reviewers: [1, 2], note: \"C1 only 2-seed at 50%, 1-seed at 30%.\"}\n      - {round: 10, reviewers: [1, 2], note: \"C1@30% s123+s456 dispatched → 3-seed.\"}\n      - {round: 11, reviewers: [1, 2], note: \"30% now fully 3-seed (KL global + uniform). C1 30% now 3-seed. 50% KL 3-seed in Appendix but main table shows s42 only. R2 rebuts R1's 'critical' to 'should-fix' with evidence. Tracked in R11-W2.\"}\n    action_items:\n      - {round: 10, action: \"C1@30% s123 + s456 running. Will achieve 3-seed at 30%.\", assigned_to: \"main_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W1\"\n    summary: \"PPL degradation 18% wording mismatch\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 10\n    mentions:\n      - {round: 9, reviewers: [1], note: \"R1-W3.\"}\n      - {round: 10, reviewers: [1], note: \"Reconfirmed.\"}\n      - {round: 11, reviewers: [], note: \"Not raised in R11 fresh review. §4.2 now reads 'reduces TEAL degradation from dense (10.97 → 8.96, an 18% improvement)' — possibly fixed.\"}\n    action_items:\n      - {round: 10, action: \"reduces PPL degradation → reduces PPL by 18% relative to TEAL\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W2\"\n    summary: \"Mistral-7B missing all downstream evaluation; cross-arch claim based on PPL only\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - {round: 9, reviewers: [1], note: \"R1-W4.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed.\"}\n      - {round: 11, reviewers: [1, 2], note: \"Partially addressed: Mistral downstream now in Table 10 (Appendix K) with 6 tasks. But data scattered in text, not in main table. R1 notes 'wins 5/6 but 6th task loss not clearly reported'. Improvement from R9 but still not fully structured.\"}\n    action_items:\n      - {round: 10, action: \"mistral_kl30_downstream eval dispatched (34887:1). ARC+WG+MMLU+GSM8K.\", assigned_to: \"main_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W3\"\n    summary: \"Eq.5 defines inequality constraint but Eq.6 uses absolute value (equality constraint)\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 10\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1-W2. R2 AGREE.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed.\"}\n      - {round: 11, reviewers: [], note: \"Not raised in R11 fresh review. Eq.5 now uses equality constraint matching Eq.6. Possibly fixed.\"}\n    action_items:\n      - {round: 10, action: \"统一为等式约束\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W4\"\n    summary: \"Training data ablation missing: domain specificity of KL masks unknown\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1-W1 + R2-W4.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed.\"}\n      - {round: 11, reviewers: [1], note: \"R1-Q5 re-raises. C4 OOD data shows gap (1.74× vs 1.46×), suggesting partial domain overfitting. Discussed in Limitations.\"}\n    action_items:\n      - {round: 10, action: \"讨论 in Limitations. C4-trained predictor 实验成本过高不在 DDL 内做.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Discussed in Limitations. Full training data ablation deferred to future work.\"\n    resolution_round: 10\n\n  - id: \"R9-I1\"\n    summary: \"Minor writing/format: -ing phrases, Ethics Qwen-14B, Gumbel citation, mean-seeking, Jacobian, Table stats, SPON footnote\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"M1-M8 collected.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed.\"}\n      - {round: 11, reviewers: [2], note: \"R2 confirms 0 em-dash, 0 en-dash, 0 blacklisted words. AI writing markers eliminated. Some symbol inconsistencies remain (R11-M1).\"}\n    action_items:\n      - {round: 10, action: \"Paper Agent P6 batch: M1-M8 all dispatched\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-N3\"\n    summary: \"Regime curve data points insufficient\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Only 3 data points.\"}\n      - {round: 9, reviewers: [], note: \"Not raised in R9 fresh. Table 5 now 6 levels.\"}\n      - {round: 11, reviewers: [], note: \"R1 initially claimed 4 points, R2 rebuts: Appendix Table 7 has 6 levels (25-50%). R1 did not persist objection. Resolved.\"}\n    action_items:\n      - {round: 8, action: \"Expanded to 6 sparsity levels.\", assigned_to: \"main_agent\", status: done}\n    resolution: \"6-point regime curve complete (25-50%). Confirmed in R11 cross-response.\"\n    resolution_round: 11\n\n  - id: \"R8-W1\"\n    summary: \"Method novelty limited: MaskLLM overlap\"\n    category: method\n    severity: warning\n    status: wont_fix\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Consensus: Findings-appropriate.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Reconfirmed as R9-N4.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed. Positioning issue.\"}\n      - {round: 11, reviewers: [1, 2], note: \"R2 reconfirms. R1 values empirical contribution but agrees Findings-appropriate. MaskLLM distinction (3 points) now convincing per R2.\"}\n    action_items:\n      - {round: 8, action: \"Reframe around mask pattern discovery.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Positioning issue. Findings accepted as realistic target. Tracked in R9-N4.\"\n    resolution_round: 10\n\n  - id: \"R8-I1\"\n    summary: \"Penalty controller lambda hits cap at 30% (actual 28.5%)\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W5.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Eq.5 vs Eq.6 inconsistency identified.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed. Eq fix dispatched.\"}\n      - {round: 11, reviewers: [1, 2], note: \"R1 re-raises as minor (30% deviation 5%). R2 rebuts: Appendix C provides quantitative argument that deviation is negligible. R1 agrees in cross-response but suggests TEAL at 28.5% sanity check.\"}\n    action_items:\n      - {round: 8, action: \"Addressed in Appendix D.\", assigned_to: \"\", status: done}\n      - {round: 10, action: \"Eq.5/6 constraint type unified.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W5\"\n    summary: \"SNR analysis only to step 300\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W4.\"}\n      - {round: 11, reviewers: [1], note: \"R1 notes SNR is empirical observation not theoretical proof. Paper §3.6 already correctly frames as 'suggestive'. R2 rebuts R1's concern: paper doesn't claim theoretical proof.\"}\n    action_items:\n      - {round: 8, action: \"Caveat in paper.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-I2\"\n    summary: \"Minor: Table PPL inconsistency, labels, figures\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Collection of minor issues.\"}\n      - {round: 10, reviewers: [1], note: \"Table 1 mixed stats. Folded into R9-I1.\"}\n      - {round: 11, reviewers: [1], note: \"Table 2 caption still 5 lines. R1 suggests simplification.\"}\n    action_items:\n      - {round: 10, action: \"Covered by Paper Agent P6 batch.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Fully resolved prior issues (compact)\n  # ============================================================\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 9\n    resolution: \"RESOLVED by C1 ablation. New C1 issues tracked as R9-N1 / R11-N1.\"\n    resolution_round: 8\n\n  - id: \"R8-N4\"\n    summary: \"\\\\enlargethispage format manipulation\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 9\n    resolution: \"Removed. Verified in R9.\"\n    resolution_round: 9\n\n  - id: \"R8-W6\"\n    summary: \"No actual inference speedup disclaimer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"Intro disclaims speedup. R11 both reviewers confirm paper is honest about this. Remains a weakness (R11-W3) but is disclosed.\"\n    resolution_round: 8\n\n  - id: \"R8-W4\"\n    summary: \"Training/eval domain overlap\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 8\n    last_seen_round: 9\n    resolution: \"Covered in Limitations. C4 OOD reported.\"\n    resolution_round: 8\n\n  - id: \"R2-N1\"\n    summary: \"Limitations section format\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Fixed Round 1\"\n    resolution_round: 1\n\n  - id: \"R6-N1\"\n    summary: \"KL+compensation control experiment\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Done: 30% 2-seed + 50% identical.\"\n    resolution_round: 7\n\n  - id: \"R3-C3\"\n    summary: \"No wall-clock speedup framing\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    resolution: \"Reframed as understanding paper.\"\n    resolution_round: 7\n\n  - id: \"R3-S2\"\n    summary: \"BCE vs KL pipeline difference\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: \"Resolved via C1 ablation.\"\n    resolution_round: 8\n\n  - id: \"R3-C2\"\n    summary: \"PPL-downstream disconnect\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: \"Abstract gives downstream collapse equal prominence.\"\n    resolution_round: 8\n\n  - id: \"R3-S1\"\n    summary: \"MaskLLM distinction insufficient\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: \"Mask pattern discovery reframe.\"\n    resolution_round: 8\n\n  - id: \"R7-W2\"\n    summary: \"\\\\enlargethispage format\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: \"Removed.\"\n    resolution_round: 9\n\n  - id: \"R7-N1\"\n    summary: \"14B MMLU reversal\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: \"Abstract/Intro state limitation.\"\n    resolution_round: 8\n\n  - id: \"R8-W3\"\n    summary: \"BCE baseline missing at 30%\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"BCE 30% now in Table 2 (11.25, global, 2700 steps). Pipeline difference documented in caption.\"\n    resolution_round: 11"
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
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 11 (fresh review) — New and recurring issues\n  # ============================================================\n\n  - id: \"R11-N1\"\n    summary: \"C1 causal ablation: inference logic flawed (mask transferability ≠ gradient coupling unimportant) + soft-vs-hard confound + BCE+Gumbel反常未解释\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. R1 raised as N2 (Must-Fix), R2 raised as W1 (Should-Fix) then upgraded in cross-response. Core issue: C1 proves mask transferability, not that gradient coupling is unimportant — KL gradient coupling is necessary to discover the masks in the first place. BCE+Gumbel=38.02 (worse than vanilla BCE 27.97) unexplained. 50% only 2-seed.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-N2\"\n    summary: \"14B Qwen MMLU -8.1pp reversal: only 'warrants further investigation', no mechanism analysis; Contribution 3 claim-evidence mismatch\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. BCE on 14B achieves MMLU 71.67% (matching TEAL 71.83%), suggesting KL mask patterns systematically harm knowledge-intensive tasks at scale. PPL-downstream disconnect at 14B is not noise. Abstract 'advantages hold on most tasks' contradicts data.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-N3\"\n    summary: \"49% PPL headline from downstream-collapsed 50% regime is misleading; actual useful 30% improvement is only 18%\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. R2 raised as N2, R1 fully agreed in cross-response citing internal contradiction with Limitations section. Paper itself says 'PPL is poor proxy' but leads with 49% PPL claim from regime where MMLU≈random.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W1\"\n    summary: \"Abstract severe data overload: ~15+ numbers in 170 words, reads like results summary not narrative\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"R2 raised as Must-Fix N1, R1 rebuts to Should-Fix (presentation not soundness). Director resolves as Should-Fix: real fix is reducing claim count from 4 to 2-3, numbers follow. Both agree Abstract fails 30-second readability test.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W2\"\n    summary: \"50% KL 3-seed data buried in Appendix E; main table reports seed 42 only. 30% BCE baseline single-seed.\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"R1 raised as Must-Fix N1, R2 rebuts: 30% KL rows ARE all 3-seed (8 metric-method combinations), TEAL is deterministic. Real gap: 50% KL main table only shows s42 (appendix has 3-seed), 30% BCE is single-seed. Director resolves as Should-Fix.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W3\"\n    summary: \"No wall-clock speedup: pipeline adds 6.4% overhead; sparse kernel integration absent\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. Paper honestly disclaims but for a sparsity prediction paper, no speedup demo is significant weakness.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W4\"\n    summary: \"PPL as primary metric limitation not reflected in experimental narrative (50% claims based on PPL only)\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. Overlaps with N3. Paper acknowledges in Limitations but experimental narrative §4.2 still PPL-driven.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W5\"\n    summary: \"HellaSwag and PIQA cited in Abstract (86.0%, 92.5%) but absent from main Table 2; internal consistency issue\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. If metric important enough for Abstract, should be in main table.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W6\"\n    summary: \"Table 3 C1 ablation at 30%: KL rows missing ARC-c, WG, GSM8K — incomplete causal comparison\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. Max Δ=1.70pp claim based on MMLU only; other tasks could show larger delta.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-M1\"\n    summary: \"Minor writing issues: symbol inconsistency (x^ℓ vs h), KL/TEAL/SPON never expanded, Table 2 caption overloaded, penalty controller terminology inconsistent\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Collection of minor issues. Both agree KL should be expanded as Kullback-Leibler at first use. TEAL/SPON are system names needing expansion. §3.1 x^(ℓ) and §3.2 h refer to same quantity.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-M2\"\n    summary: \"68% mask divergence lacks confidence interval; SPON 2.4% contribution possibly within noise (single-seed)\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"R1 raised both. R2 agrees on 68% CI, agrees SPON is minor since paper frames as optional. Bootstrap CI on Jaccard needed.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Prior issues — status updates from Round 11 fresh review\n  # ============================================================\n\n  - id: \"R9-N1\"\n    summary: \"C1 causal ablation: 2-seed insufficient for 'proves' claim + soft-vs-hard mask confound uncontrolled\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1 raised as Must-Fix N1 (2-seed + soft-vs-hard confound + 30% PPL gap). R2 initially Should-Fix W1, upgraded to AGREE with R1 in cross-response.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed. R1 new finding: soft-vs-hard confound (KL uses soft Gumbel, C1 BCE uses hard targets). 30% PPL gap +0.63 flagged.\"}\n      - {round: 11, reviewers: [1, 2], note: \"Reconfirmed as R11-N1. C1 now 3-seed at 30% and 2-seed at 50%. soft-vs-hard confound paragraph added (§4.5) but logic issue remains: paper claims 'target quality not gradient coupling' but gradient coupling is necessary to discover the targets. BCE+Gumbel=38.02 反常 still unexplained mechanistically.\"}\n    action_items:\n      - {round: 10, action: \"C1@30% s123 + s456 experiments dispatched (41718:0,1). Achieves 3-seed at 30%.\", assigned_to: \"main_agent\", status: done}\n      - {round: 10, action: \"全文 proves/confirms → provides evidence/supports\", assigned_to: \"paper_agent\", status: done}\n      - {round: 10, action: \"§4.4 新增 soft-vs-hard confound 讨论 + bce_gumbel PPL=38.02 反证\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-N2\"\n    summary: \"BCE baseline pipeline inconsistent across sparsity levels: 30% uses TEAL/no-comp, 50% uses DejaVu+comp/no-TEAL\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1 raised as Must-Fix N3. R2 missed in initial review, AGREE in cross-response.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed. Missing 50% BCE+TEAL global baseline.\"}\n      - {round: 11, reviewers: [], note: \"Not explicitly raised as separate issue in R11 fresh review. Table 2 now has clearer footnotes distinguishing pipelines. Pipeline difference remains but is documented.\"}\n    action_items:\n      - {round: 10, action: \"bce_50pct_teal_global_unified eval dispatched (34887:0). Uses benchmark_eval.py unified protocol.\", assigned_to: \"main_agent\", status: in_progress}\n      - {round: 10, action: \"Table 1 caption 显著标注 pipeline 差异\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-N3\"\n    summary: \"Narrow usable range (only 30%, ~2pp downstream gain) + 50% framing bias in Abstract + no wall-clock speedup\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1-N4 + R2-N2 + R2-N3 converged.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed. Abstract still leads with 50% PPL as narrative climax.\"}\n      - {round: 11, reviewers: [1, 2], note: \"Reconfirmed as R11-N3. Abstract now includes 30% results but still foregrounds 49% PPL from 50% regime. Both reviewers flag internal contradiction with Limitations section.\"}\n    action_items:\n      - {round: 10, action: \"Abstract 二次调整：30% downstream quality 为核心 take-away，50% PPL 降为次要\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-N4\"\n    summary: \"Method novelty insufficient for Main: KL+Gumbel+predictor = existing components, MaskLLM overlap\"\n    category: method\n    severity: critical\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R2 raised as Must-Fix N1. R1 REBUT on severity but AGREE on substance.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed. Both agree Findings-appropriate, not Main. Positioning issue, not fixable.\"}\n      - {round: 11, reviewers: [2], note: \"R2 reconfirms: 'method is natural combination of known components, no technical surprise'. R1 acknowledges but values empirical contribution higher. Both agree Findings-appropriate.\"}\n    action_items: []\n    resolution: \"Positioning issue — not addressable through revision. Findings accepted as realistic target.\"\n    resolution_round: 10\n\n  - id: \"R8-N2\"\n    summary: \"14B MMLU reversal: KL PPL best but MMLU -8.1pp vs TEAL\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Full consensus.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Reconfirmed. Abstract now states gap but no mechanism.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Must-Fix N2. Needs full paragraph + mechanism hypotheses.\"}\n      - {round: 11, reviewers: [1, 2], note: \"Reconfirmed as R11-N2. R2 adds: BCE on 14B MMLU=71.67% matches TEAL, suggesting magnitude-based masks systematically better for knowledge tasks at scale. 'warrants further investigation' is reviewer language, not author language. Still no mechanism analysis.\"}\n    action_items:\n      - {round: 8, action: \"Restrict scope to 7-8B primary.\", assigned_to: \"paper_agent\", status: done}\n      - {round: 10, action: \"§4.5 新增 1 段 14B mechanism discussion (knowledge density + domain bias hypotheses)\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 10, action: \"Abstract 明确提及 downstream reversal\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W2\"\n    summary: \"50% downstream collapse contradicts Abstract emphasis on 49% PPL advantage\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R2-W1, R1 AGREE.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Narrative still leads with 50%. R9-N3.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed. Abstract二次调整 dispatched.\"}\n      - {round: 11, reviewers: [1, 2], note: \"Still present. Abstract includes 30% results now but 49%/50% remains prominent. Tracked in R11-N3.\"}\n    action_items:\n      - {round: 8, action: \"Give downstream collapse equal prominence.\", assigned_to: \"paper_agent\", status: done}\n      - {round: 10, action: \"Abstract 二次调整：30% 为核心，50% 降级\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Statistical power: key comparisons partially single-seed\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 11\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Improved: 30% KL global 3-seed.\"}\n      - {round: 8, reviewers: [1, 2], note: \"30% KL uniform now 3-seed.\"}\n      - {round: 9, reviewers: [1, 2], note: \"C1 only 2-seed at 50%, 1-seed at 30%.\"}\n      - {round: 10, reviewers: [1, 2], note: \"C1@30% s123+s456 dispatched → 3-seed.\"}\n      - {round: 11, reviewers: [1, 2], note: \"30% now fully 3-seed (KL global + uniform). C1 30% now 3-seed. 50% KL 3-seed in Appendix but main table shows s42 only. R2 rebuts R1's 'critical' to 'should-fix' with evidence. Tracked in R11-W2.\"}\n    action_items:\n      - {round: 10, action: \"C1@30% s123 + s456 running. Will achieve 3-seed at 30%.\", assigned_to: \"main_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W1\"\n    summary: \"PPL degradation 18% wording mismatch\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 10\n    mentions:\n      - {round: 9, reviewers: [1], note: \"R1-W3.\"}\n      - {round: 10, reviewers: [1], note: \"Reconfirmed.\"}\n      - {round: 11, reviewers: [], note: \"Not raised in R11 fresh review. §4.2 now reads 'reduces TEAL degradation from dense (10.97 → 8.96, an 18% improvement)' — possibly fixed.\"}\n    action_items:\n      - {round: 10, action: \"reduces PPL degradation → reduces PPL by 18% relative to TEAL\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W2\"\n    summary: \"Mistral-7B missing all downstream evaluation; cross-arch claim based on PPL only\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - {round: 9, reviewers: [1], note: \"R1-W4.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed.\"}\n      - {round: 11, reviewers: [1, 2], note: \"Partially addressed: Mistral downstream now in Table 10 (Appendix K) with 6 tasks. But data scattered in text, not in main table. R1 notes 'wins 5/6 but 6th task loss not clearly reported'. Improvement from R9 but still not fully structured.\"}\n    action_items:\n      - {round: 10, action: \"mistral_kl30_downstream eval dispatched (34887:1). ARC+WG+MMLU+GSM8K.\", assigned_to: \"main_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W3\"\n    summary: \"Eq.5 defines inequality constraint but Eq.6 uses absolute value (equality constraint)\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 10\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1-W2. R2 AGREE.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed.\"}\n      - {round: 11, reviewers: [], note: \"Not raised in R11 fresh review. Eq.5 now uses equality constraint matching Eq.6. Possibly fixed.\"}\n    action_items:\n      - {round: 10, action: \"统一为等式约束\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R9-W4\"\n    summary: \"Training data ablation missing: domain specificity of KL masks unknown\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R1-W1 + R2-W4.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed.\"}\n      - {round: 11, reviewers: [1], note: \"R1-Q5 re-raises. C4 OOD data shows gap (1.74× vs 1.46×), suggesting partial domain overfitting. Discussed in Limitations.\"}\n    action_items:\n      - {round: 10, action: \"讨论 in Limitations. C4-trained predictor 实验成本过高不在 DDL 内做.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Discussed in Limitations. Full training data ablation deferred to future work.\"\n    resolution_round: 10\n\n  - id: \"R9-I1\"\n    summary: \"Minor writing/format: -ing phrases, Ethics Qwen-14B, Gumbel citation, mean-seeking, Jacobian, Table stats, SPON footnote\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"M1-M8 collected.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed.\"}\n      - {round: 11, reviewers: [2], note: \"R2 confirms 0 em-dash, 0 en-dash, 0 blacklisted words. AI writing markers eliminated. Some symbol inconsistencies remain (R11-M1).\"}\n    action_items:\n      - {round: 10, action: \"Paper Agent P6 batch: M1-M8 all dispatched\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-N3\"\n    summary: \"Regime curve data points insufficient\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Only 3 data points.\"}\n      - {round: 9, reviewers: [], note: \"Not raised in R9 fresh. Table 5 now 6 levels.\"}\n      - {round: 11, reviewers: [], note: \"R1 initially claimed 4 points, R2 rebuts: Appendix Table 7 has 6 levels (25-50%). R1 did not persist objection. Resolved.\"}\n    action_items:\n      - {round: 8, action: \"Expanded to 6 sparsity levels.\", assigned_to: \"main_agent\", status: done}\n    resolution: \"6-point regime curve complete (25-50%). Confirmed in R11 cross-response.\"\n    resolution_round: 11\n\n  - id: \"R8-W1\"\n    summary: \"Method novelty limited: MaskLLM overlap\"\n    category: method\n    severity: warning\n    status: wont_fix\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Consensus: Findings-appropriate.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Reconfirmed as R9-N4.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed. Positioning issue.\"}\n      - {round: 11, reviewers: [1, 2], note: \"R2 reconfirms. R1 values empirical contribution but agrees Findings-appropriate. MaskLLM distinction (3 points) now convincing per R2.\"}\n    action_items:\n      - {round: 8, action: \"Reframe around mask pattern discovery.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Positioning issue. Findings accepted as realistic target. Tracked in R9-N4.\"\n    resolution_round: 10\n\n  - id: \"R8-I1\"\n    summary: \"Penalty controller lambda hits cap at 30% (actual 28.5%)\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W5.\"}\n      - {round: 9, reviewers: [1, 2], note: \"Eq.5 vs Eq.6 inconsistency identified.\"}\n      - {round: 10, reviewers: [1, 2], note: \"Reconfirmed. Eq fix dispatched.\"}\n      - {round: 11, reviewers: [1, 2], note: \"R1 re-raises as minor (30% deviation 5%). R2 rebuts: Appendix C provides quantitative argument that deviation is negligible. R1 agrees in cross-response but suggests TEAL at 28.5% sanity check.\"}\n    action_items:\n      - {round: 8, action: \"Addressed in Appendix D.\", assigned_to: \"\", status: done}\n      - {round: 10, action: \"Eq.5/6 constraint type unified.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-W5\"\n    summary: \"SNR analysis only to step 300\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"R1-W4.\"}\n      - {round: 11, reviewers: [1], note: \"R1 notes SNR is empirical observation not theoretical proof. Paper §3.6 already correctly frames as 'suggestive'. R2 rebuts R1's concern: paper doesn't claim theoretical proof.\"}\n    action_items:\n      - {round: 8, action: \"Caveat in paper.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R8-I2\"\n    summary: \"Minor: Table PPL inconsistency, labels, figures\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - {round: 8, reviewers: [1, 2], note: \"Collection of minor issues.\"}\n      - {round: 10, reviewers: [1], note: \"Table 1 mixed stats. Folded into R9-I1.\"}\n      - {round: 11, reviewers: [1], note: \"Table 2 caption still 5 lines. R1 suggests simplification.\"}\n    action_items:\n      - {round: 10, action: \"Covered by Paper Agent P6 batch.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Fully resolved prior issues (compact)\n  # ============================================================\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 9\n    resolution: \"RESOLVED by C1 ablation. New C1 issues tracked as R9-N1 / R11-N1.\"\n    resolution_round: 8\n\n  - id: \"R8-N4\"\n    summary: \"\\\\enlargethispage format manipulation\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 9\n    resolution: \"Removed. Verified in R9.\"\n    resolution_round: 9\n\n  - id: \"R8-W6\"\n    summary: \"No actual inference speedup disclaimer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"Intro disclaims speedup. R11 both reviewers confirm paper is honest about this. Remains a weakness (R11-W3) but is disclosed.\"\n    resolution_round: 8\n\n  - id: \"R8-W4\"\n    summary: \"Training/eval domain overlap\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 8\n    last_seen_round: 9\n    resolution: \"Covered in Limitations. C4 OOD reported.\"\n    resolution_round: 8\n\n  - id: \"R2-N1\"\n    summary: \"Limitations section format\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Fixed Round 1\"\n    resolution_round: 1\n\n  - id: \"R6-N1\"\n    summary: \"KL+compensation control experiment\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Done: 30% 2-seed + 50% identical.\"\n    resolution_round: 7\n\n  - id: \"R3-C3\"\n    summary: \"No wall-clock speedup framing\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    resolution: \"Reframed as understanding paper.\"\n    resolution_round: 7\n\n  - id: \"R3-S2\"\n    summary: \"BCE vs KL pipeline difference\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: \"Resolved via C1 ablation.\"\n    resolution_round: 8\n\n  - id: \"R3-C2\"\n    summary: \"PPL-downstream disconnect\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: \"Abstract gives downstream collapse equal prominence.\"\n    resolution_round: 8\n\n  - id: \"R3-S1\"\n    summary: \"MaskLLM distinction insufficient\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: \"Mask pattern discovery reframe.\"\n    resolution_round: 8\n\n  - id: \"R7-W2\"\n    summary: \"\\\\enlargethispage format\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: \"Removed.\"\n    resolution_round: 9\n\n  - id: \"R7-N1\"\n    summary: \"14B MMLU reversal\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: \"Abstract/Intro state limitation.\"\n    resolution_round: 8\n\n  - id: \"R8-W3\"\n    summary: \"BCE baseline missing at 30%\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"BCE 30% now in Table 2 (11.25, global, 2700 steps). Pipeline difference documented in caption.\"\n    resolution_round: 11"
  }
}
```

</details>

---


### Tool result

_source line 927 · 2026-05-19T06:41:49.844107+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 25322}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-19T06:44:59.140418+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 11 (Fresh Review)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 via ARR May 2026 cycle\n**Reviewers**: R1 (方法严谨性+实验有效性), R2 (新颖性+写作+格式)\n**流程**: Round 1 独立审稿 → 交叉分享 + 逐条回应 → 收敛汇总\n\n---\n\n## Summary\n\n本文提出用 forward KL divergence + Gumbel-Sigmoid 松弛训练轻量 sparsity predictor（75.9M params, <1% of base），替代传统 BCE 目标，用于 SwiGLU LLM 的 activation sparsity 预测。核心发现：KL 训练发现的 mask 与 magnitude-based mask 偏离 68%（per-layer Jaccard 32%），causal ablation (C1) 表明 mask target 质量是 KL 质量优势的主要来源。方法在 LLaMA-3.1-8B 30% sparsity 下 PPL 改善 18%（vs TEAL），消除了 67.2M 参数的 compensation network，并在 Mistral-7B 上泛化（5/6 downstream tasks 胜出）。但 50% sparsity 下 downstream 全面崩溃、14B Qwen 上 MMLU 反转 -8.1pp、无 wall-clock speedup、C1 因果推断存在逻辑缺陷。\n\n---\n\n## Strengths\n\n1. **有洞察力的核心发现**：KL mask 与 magnitude mask 68% 偏离不是显而易见的结果，对 sparsity prediction 文献有分析价值。U-shaped per-layer divergence pattern 提供了可操作的信号。[R1, R2 consensus]\n\n2. **设计精良的 C1 causal ablation**：用 BCE 在 KL-derived targets 训练来分离 target quality 和 training objective，50% 下 max Δ=0.59pp (2-seed)，30% 下 max Δ=1.70pp (3-seed)。实验设计有 genuine intellectual merit。[R1, R2 consensus]\n\n3. **系统化的实验覆盖**：3 架构（LLaMA-8B, Mistral-7B, Qwen-14B），6 个 sparsity 级别（25%-70%），两种 allocation 策略，消融涵盖 divergence 方向/relaxation/compensation/hyperparameter，3-seed 评估覆盖核心实验。[R2]\n\n4. **诚实的 claim 边界**：明确声明 \"Our contribution is empirical\"，诚实报告 50% downstream collapse、14B 反转、无 speedup、C4 OOD gap 等负面结果。在同类论文中属上游。[R1, R2 consensus]\n\n5. **训练效率高**：单 GPU 45 分钟，1000 步收敛，predictor <1% base model 参数，工程实用性好。[R1]\n\n6. **写作干净无 AI 痕迹**：em-dash 0 处、en-dash 0 处、黑名单词 0 处、过度过渡词 0 处。格式完全合规（ACL [review]、行号、匿名化、Limitations 位置、双栏）。[R2 验证]\n\n7. **引用完整**：46 条引用全部通过交叉验证，无虚构引用，Related Work 6 段覆盖所有主要方向，与 MaskLLM 的三点区分具体且有说服力。[R1, R2 consensus]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical, consensus] C1 因果消融推断逻辑有缺陷**\n- **因果链断裂**：C1 训练 BCE 在 KL-derived masks 上，匹配 KL 质量。论文推断\"target quality, not gradient coupling, drives quality\"。但 KL gradient coupling 是 *发现* 这些 superior masks 的必要条件。C1 证明的是 mask transferability（已知好 masks 可迁移到更简单的训练），而非 gradient coupling 在训练阶段不重要。论文的 framing 混淆了 mask discovery 阶段和 inference 阶段。\n- **Soft-vs-Hard confound 反常未解释**：BCE + Gumbel-Sigmoid = PPL 38.02，比 vanilla BCE (27.97) 更差。§4.5 给出的解释（\"penalty interferes with per-neuron optimization without global coordination\"）缺乏实验验证。如果 Gumbel 在 BCE 下有害，KL 的优势可能部分来自 KL loss 与 Gumbel 的特殊协同，而非纯粹的 target quality。\n- **建议**：(a) 修正 framing 为 \"mask transferability\" 而非 \"gradient coupling unimportant\"，明确区分 training-stage 和 inference-stage 的 coupling 角色；(b) 补充实验：去掉 penalty 只保留 Gumbel 的 BCE 作为控制；(c) 50% C1 增加至 3-seed。\n\n**N2 [critical, consensus] 14B Qwen MMLU 反转未被充分分析**\n- Qwen-2.5-14B 上 KL PPL 优于 TEAL (7.62 vs 8.73) 但 MMLU 严重反转 (63.7% vs 71.8%, -8.1pp)。BCE 在 14B 上 MMLU=71.67% 接近 TEAL，说明 KL mask patterns 在大模型上可能系统性损害知识检索任务。\n- Contribution #3 声称分析了 \"scale-dependent effects at 14B\"，但 §4.6 仅用一句话处理 (\"warrants further investigation\")。这不是可推迟到 future work 的问题——如果方法在最有价值的方向（更大模型）上 downstream 退化，实际可推广性存在根本质疑。\n- Abstract \"advantages hold on most tasks across architectures\" 与数据矛盾。\n- **建议**：(a) 分析 14B per-layer mask divergence 与 8B 对比；(b) 检查 14B layer retention 分布；(c) 提供至少一个假说并用已有数据验证/排除；(d) 修正 Abstract 和 Introduction 中的 cross-architecture claims。\n\n**N3 [critical, consensus] 49% PPL headline 来自 downstream 全面崩溃的 regime，framing 有误导性**\n- 49% PPL 改善 (11.79 vs 23.31) 来自 50% sparsity，但此 regime 下 MMLU≈28%（近随机）、GSM8K<2.2%。论文自身在 Limitations 承认 \"PPL is poor proxy for reasoning ability\"。将 49% 放在 Abstract 和 Introduction 最显眼位置，而 30% 的 18% PPL 改善放在次要位置，产生内部矛盾。\n- 实际可用操作点是 30%（downstream 保持 86-92% retention），但这个 regime 的改善幅度远不如 headline 宣传的 49%。\n- **建议**：以 30% sparsity 为 Abstract/Introduction 的主叙事支撑点，50% 降为分析补充。保留最多 2-3 个关键数字（mask 68% 偏离、30% PPL 18% 改善、compensation 冗余），删除其余。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [warning, consensus] Abstract 数据堆砌**\n- ~170 词中 15+ 个数字，读起来像 results 缩写而非独立叙事。审稿人 30 秒内难以判断核心价值。\n- R2 评为 Must-Fix，R1 评为 Should-Fix（presentation 非 soundness）。Director 判定为 Should-Fix：实质修复方向是削减 claim 数量（4→2-3），数字自然减少。\n\n**W2 [warning, consensus after correction] 50% KL 3-seed 数据未上浮至主表**\n- Table 2 中 50% KL 仅显示 seed 42 (PPL 11.79)，完整 3-seed 数据 (PPL 11.92±0.07, CV<1%) 在 Appendix E。30% BCE baseline 为单 seed。\n- R1 初始评为 critical 但描述不准确（30% KL 实际全部 3-seed），R2 用证据纠正。Director 判定 Should-Fix：50% 3-seed 应上浮至主表，30% BCE 应补充 multi-seed。\n\n**W3 [warning, consensus] 无 wall-clock speedup**\n- Pipeline 增加 6.4% overhead（126.78 vs 119.11 ms/forward）。论文诚实承认 sparse kernel 不在 scope 内，但作为 sparsity prediction 论文无加速演示是显著弱点。\n\n**W4 [warning, consensus] PPL 局限性未充分反映在实验叙事中**\n- Limitations 承认 PPL 是 poor proxy，但 §4.2 main results 叙事仍以 PPL 驱动。与 N3 overlapping。\n\n**W5 [warning, consensus] HellaSwag 和 PIQA 在 Abstract 引用但不在主表**\n- Abstract 引用 86.0%/92.5% retention，但 Table 2 仅含 ARC-c、WG、MMLU、GSM8K。如果指标重要到出现在 Abstract，应在主表中。\n\n**W6 [warning, consensus] Table 3 C1 ablation 30% KL 行缺 ARC-c/WG/GSM8K**\n- Max Δ=1.70pp claim 基于 MMLU 单一 metric，其他 downstream 可能有更大偏差。C1 作为核心 claim 支撑，比较应完整。\n\n### Minor Issues\n\n**M1** [info] 符号不一致：§3.1 $\\mathbf{x}^{(\\ell)}$ (\"hidden state after attention\") vs §3.2 $\\mathbf{h}$ (\"pre-FFN hidden state\")，指代同一量但符号切换。\n**M2** [info] KL (Kullback-Leibler)、TEAL、SPON 在首次使用时未展开定义。\n**M3** [info] 68% mask divergence 无 bootstrap confidence interval（64 samples, 131K tokens 的均值无 CI）。\n**M4** [info] SPON 2.4% PPL 改善 (12.08→11.79) 为单 seed，可能在噪声范围内（3-seed std≈0.07）。论文已 frame 为 \"optional, marginal\"。\n**M5** [info] Table 2 caption 5 行，信息密度过高。\n**M6** [info] Penalty controller terminology 不统一（\"Adaptive Penalty Sparsity Controller\" vs \"adaptive penalty controller\" vs footnote \"resembles augmented Lagrangian\"）。\n**M7** [info] §3.6 gradient analysis 中 SNR 5.14× 是经验度量，论文定位为 \"suggestive\" 是恰当的（R1 初始质疑 overclaiming，R2 rebut 指出论文未声称理论证明）。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 在交叉回应中达成明确共识：\n\n1. **C1 因果推断逻辑有缺陷** [R1-N2, R2-W1→upgraded]：C1 证明 mask transferability，不等于 gradient coupling 在训练阶段不重要。Framing 需修正。\n2. **14B MMLU 反转分析不足** [R1-N3, R2-N3]：BCE 14B MMLU=71.67% 接近 TEAL=71.83%，说明 magnitude masks 在大模型上对知识任务更优。需要 mechanism 分析。\n3. **49% PPL headline 有误导性** [R2-N2, R1 cross-AGREE]：50% regime downstream 崩溃但 PPL 大幅改善，作为 headline 有内部矛盾。\n4. **方法新颖性适合 Findings** [R1, R2 consensus]：KL+Gumbel+MLP predictor 是已有组件的自然组合，无技术 surprise，但 empirical findings 有价值。两位 Reviewer 均评 3.0 (Findings)。\n5. **无 wall-clock speedup 是显著弱点** [R1-W2, R2-W2]。\n6. **实验诚实度在同类论文中属上游** [R1, R2 consensus]：负面结果均被报告。\n7. **写作质量高，格式完全合规** [R2 验证，R1 agree]。\n\n---\n\n## Reviewer Divergence [REBUT]\n\n以下问题两位 Reviewer 存在分歧，经交叉回应后部分解决：\n\n1. **Single-seed 严重性** [R1: Must-Fix → R2 rebut with evidence → Director: Should-Fix]\n   - R1 声称 \"绝大多数结果 seed 42\"，R2 逐条反驳：30% KL 全部 8 个 metric-method 组合均为 3-seed，TEAL 是 deterministic 无需 multi-seed。实际 gap 仅在 50% 主表呈现和 30% BCE baseline。Director 采纳 R2 的纠正，降级为 Should-Fix。\n\n2. **Abstract 数据堆砌严重性** [R2: Must-Fix vs R1: Should-Fix]\n   - R2 认为 15+ 数字的 Abstract 无法通过 \"30 秒可读性测试\"；R1 认为这是 presentation 问题不应与 soundness 并列。Director 采纳 R1 的分级逻辑，判定 Should-Fix。\n\n3. **Three regime 分析** [R1: overfitting 4 points → R2 rebut: 6 points in Appendix]\n   - R1 未阅读 Appendix Table 7（6 个 sparsity 级别完整数据），R2 纠正后 R1 未坚持。Director 判定：regime 分析有 6 点数据支撑，不构成独立 weakness。\n\n4. **Compensation 验证范围** [R1: 仅 50% → R2 rebut: 事实错误]\n   - §4.5 明确报告 30% 和 50% 两个 sparsity level 的 compensation 冗余结果。R1 遗漏。Director 判定：不构成 weakness。\n\n5. **Taxonomy 质量** [R2: 人为构建感 vs R1: 有价值的 positioning]\n   - R1 论证 taxonomy 维度合理且帮助读者理解方法差异。Director 判定：不构成 weakness，但 MSE \"intermediate coupling\" 定义可更清晰。\n\n6. **Soundness 评分** [R1: 3.0 vs R2: 3.5]\n   - R1 因 C1 confound + seed 问题评 3.0；R2 因 C1 设计精良 + 30% 3-seed 完整评 3.5。Director 综合判定 Soundness 3.0（C1 逻辑缺陷是实质问题，不被 seed 覆盖率缓解）。\n\n7. **Excitement 评分** [R1: 3.0 vs R2: 2.5]\n   - R1 认为 mask divergence 发现有真正洞察价值（3.0）；R2 认为无 speedup + 窄 window + 已知组件组合限制实际影响（2.5）。Director 综合判定 Excitement 2.5（mask divergence 有分析价值但 practical impact 有限）。\n\n---\n\n## Questions for Authors\n\n1. **C1 反事实控制**：如果用随机初始化预测器（而非 KL-trained）导出 oracle mask 训练 BCE，质量如何？这才是测试 \"target quality vs gradient coupling\" 的完整控制。[R1-Q1, R2 cross-AGREE]\n\n2. **BCE+Gumbel 恶化机制**：为何 soft relaxation 使 BCE 从 27.97 恶化到 38.02？是 Gumbel noise 与 BCE binary target 冲突，还是 penalty controller 与 per-neuron 独立梯度冲突？去掉 penalty 只保留 Gumbel 的 BCE 表现如何？[R1-Q2, R2 cross-AGREE]\n\n3. **14B MMLU 反转根因**：BCE 在 14B MMLU=71.67% 接近 TEAL=71.83%，而 KL=63.7%。是否 KL 的 coupled gradient 在大模型上发现了牺牲知识检索的 mask patterns？14B per-layer mask divergence 数据能否澄清？[R1-Q3, R2-Q1, consensus]\n\n4. **Table 3 缺失数据**：30% KL 行缺 ARC-c/WG/GSM8K。如果这些 task 的 Δ 超过 1.70pp 或方向反转，会影响 C1 的结论。这些数据是否可用？[R2-Q2, R1 cross-AGREE]\n\n5. **Mask divergence 训练动态**：68% 偏离是训练终点测量。early checkpoint 的 Jaccard 数据能帮助理解 KL mask 何时、如何偏离 magnitude。[R2-Q3, R1 cross-AGREE]\n\n6. **Penalty controller 30% 公平性**：实际 sparsity 28.5% vs target 30%（偏差 5%）。TEAL 在 28.5% 下的 PPL 数据可作为 sanity check。[R2-Q5, R1 cross-AGREE]\n\n---\n\n## Missing References\n\n**共识遗漏**：\n- **OWL (Yin et al., 2024)**：研究 non-uniform layerwise sparsity allocation，与 §4.6 global vs uniform allocation 分析直接相关。[R1 cross-AGREE]\n\n**可选补充**（不影响评分）：\n- Sheared LLaMA (Xia et al., 2023)：structured pruning + distillation，与 MiniTron 方向相同。\n\n**排除项**：\n- LLM.int8() (Dettmers et al., 2022)：量化论文，不在 activation sparsity scope 内。[R2 cross-REBUT]\n- FLAP (An et al., ICML 2024)：structured weight pruning，与本文问题空间不同。[R1 cross-REBUT]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目未启用 `external_review.paperreview_ai`）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Soundness: 3.0/5** — 方法设计合理，C1 ablation 方向正确但因果推断逻辑有缺陷（mask transferability ≠ gradient coupling unimportant），soft-vs-hard confound 反常结果未充分解释。14B cross-architecture claim 与数据矛盾。30% 核心实验统计效力充分（3-seed），50% 主表呈现不完整。\n\n**Excitement: 2.5/5** — Mask divergence 发现有分析价值，三 regime allocation 分析对后续工作有参考意义。但方法是已知组件的自然组合（KL + Gumbel + MLP predictor），无技术 surprise；无 wall-clock speedup；practical window 仅 30%（实际加速更窄）；14B downstream 反转限制可推广性。实践者从论文学到的 actionable insight 有限——\"用 KL 替代 BCE\" 是一个 recipe 而非 principle。\n\n**Reproducibility: 3.5/5** — 超参数完整报告（d_b=128, τ schedule, lr, wd, batch, seq_len），GPU 型号和训练时间精确到分钟，3-seed 覆盖核心实验。但 evaluation protocol 细节（few-shot 设置、exact prompt templates）未完全明确，代码未开源。\n\n**Confidence: 4/5** — 两位 Reviewer 均熟悉 LLM activation sparsity、knowledge distillation 和 efficient inference 文献，仔细核实了核心实验数据和 claim 对应关系。\n\n### 判断理由\n\n**为什么是 Findings (3.0) 而非 Borderline Conference (3.5)**：\n1. 方法新颖性不足以支撑 Main：每个组件均为已有技术，组合合理但缺乏技术 surprise。两位 Reviewer 一致认为 Findings-appropriate。\n2. C1 因果推断——论文最核心的 claim——存在逻辑缺陷和未解释的反常结果。\n3. 14B downstream 反转是 scaling concern，不是可推迟到 future work 的问题。\n4. 无 wall-clock speedup，practical operating window 仅 30%。\n\n**为什么不低于 Findings (2.5)**：\n1. C1 causal ablation 实验设计有 genuine intellectual merit。\n2. 实验系统性和诚实度在同类论文中属上游。\n3. Mask divergence 发现和 allocation regime 分析对后续工作有参考价值。\n4. 写作质量高，格式完全合规，无 AI 痕迹。\n5. 引用完整无遗漏。\n\n### Rebuttal 优先级\n\n1. **最高优先级**：修正 C1 framing（区分 mask discovery 和 inference-stage quality）+ 补充 BCE+Gumbel 无 penalty 控制实验\n2. **高优先级**：14B MMLU 反转 mechanism 分析（per-layer divergence 对比 + layer retention 对比）\n3. **高优先级**：Abstract/Introduction 重构——30% 为主叙事，50% 降级；削减至 2-3 个核心 claim\n4. **中优先级**：50% KL 3-seed 上浮至主表；Table 3 补全 30% KL downstream 数据\n5. **低优先级**：符号统一、缩写展开、caption 精简\n\n---\n\n## Detailed Comments (per section)\n\n### Abstract\n- 15+ 数字在 170 词中，信息过载。删减至 3 个关键数字。[W1]\n- BCE/PPL 未展开（标准缩写可接受，但 KL/TEAL/SPON 应展开）。[M2]\n- \"advantages hold on most tasks across architectures\" 与 Qwen MMLU 反转矛盾。[N2]\n- 49% headline 来自 downstream 崩溃的 regime。[N3]\n\n### Introduction\n- 五段结构基本完整。从 SwiGLU sparsity → BCE 局限 → KL 提出 → C1 发现 → 贡献列表，逻辑流畅。\n- P2→P3 过渡略突兀：缺少 \"Therefore, we propose...\" 桥接。[R2]\n- Contribution #3 \"allocation-to-downstream interactions at 7-14B\" 在前文无铺垫。[R2]\n- 49% headline 在 L14 位置过于突出。[N3]\n\n### Related Work\n- 6 段组织清晰，positioning 准确。\n- MaskLLM 三点区分（sparsity type / mask generation / allocation）具体且有说服力。[R1, R2 consensus]\n- D2DMoE 的 \"intermediate coupling\" 描述可更精确（不仅是 MSE supervision）。[R2]\n- Griffin 引用感觉勉强（RG-LRU gating 与 SwiGLU 关系间接）。[R2]\n- 缺少 OWL (Yin et al., 2024) 的引用。[consensus]\n\n### Method (§3)\n- 数学叙述清晰，Eq.1-6 内部一致。\n- §3.5 adaptive penalty controller 设计合理，footnote disclaimer 是好做法。\n- §3.6 gradient analysis 定位恰当（\"suggestive\"）。SNR 5.14× 作为经验度量辅助 intuition。[R2 rebut R1 overclaiming 质疑]\n- ε=0.02 deadzone 选择依据未说明。[R1]\n- Figure 1 caption 可更自包含。[R2]\n\n### Experiments (§4)\n- §4.2 Main results：Table 2 中 30% 全部 3-seed，50% 主表仅 s42（appendix 有 3-seed）。Caption 5 行过长。[W2, M5]\n- §4.3 Extended training：iso-compute comparison (BCE 2.71× steps still worse) 有力支撑 KL 优势。\n- §4.4 Mask analysis + C1 ablation：论文核心贡献，设计精良但因果推断逻辑有缺陷。[N1]\n- §4.5 Ablation：Table 4 全面，但 SPON 2.4% 可能在噪声内，BCE+Gumbel 反常未充分解释。\n- §4.6 Scaling & cross-architecture：三 regime 分析有 6 点数据支撑（R2 纠正 R1 的 \"4 points\" 误读）。14B 结果仅一句话处理。[N2]\n\n### Conclusion\n- 极简（2 句话），核心发现覆盖。但过于压缩，缺少 limitations 和 future directions 的一句话总结。\n\n### Limitations\n- 全面且诚实。覆盖 PPL 局限性、sparse kernel 缺失、14B 反转、OOD gap、seed variance。\n- 14B 反转在此处被承认但分析不足。[N2]\n- 缺少对 C1 confound 局限性的讨论。[N1]\n\n### Ethics & Checklist\n- 完整且认真填写，无遗漏。Qwen-2.5-14B 的 license 信息已包含。\n\n### Appendix\n- 13 个 section 全部在正文中有 explicit reference。组织合理，补充了 hyperparameter sensitivity、OOD、stability、SNR、mask visualization 等完整数据。\n- Appendix E 的 3-seed 数据应上浮至主表。[W2]\n\n### 格式合规\n| 检查项 | 状态 |\n|--------|------|\n| 正文 ≤8 页 | ✅ |\n| ACL template [review] | ✅ |\n| Limitations 位置 | ✅ |\n| 行号开启 | ✅ |\n| 引用格式 (natbib) | ✅ |\n| 匿名化 | ✅ |\n| 图表字体 ≥7pt | ✅ |\n| 附录被正文引用 | ✅ |\n| 双栏格式 | ✅ |",
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 Findings",
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
    "report": "# 审稿报告 — Round 11 (Fresh Review)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 via ARR May 2026 cycle\n**Reviewers**: R1 (方法严谨性+实验有效性), R2 (新颖性+写作+格式)\n**流程**: Round 1 独立审稿 → 交叉分享 + 逐条回应 → 收敛汇总\n\n---\n\n## Summary\n\n本文提出用 forward KL divergence + Gumbel-Sigmoid 松弛训练轻量 sparsity predictor（75.9M params, <1% of base），替代传统 BCE 目标，用于 SwiGLU LLM 的 activation sparsity 预测。核心发现：KL 训练发现的 mask 与 magnitude-based mask 偏离 68%（per-layer Jaccard 32%），causal ablation (C1) 表明 mask target 质量是 KL 质量优势的主要来源。方法在 LLaMA-3.1-8B 30% sparsity 下 PPL 改善 18%（vs TEAL），消除了 67.2M 参数的 compensation network，并在 Mistral-7B 上泛化（5/6 downstream tasks 胜出）。但 50% sparsity 下 downstream 全面崩溃、14B Qwen 上 MMLU 反转 -8.1pp、无 wall-clock speedup、C1 因果推断存在逻辑缺陷。\n\n---\n\n## Strengths\n\n1. **有洞察力的核心发现**：KL mask 与 magnitude mask 68% 偏离不是显而易见的结果，对 sparsity prediction 文献有分析价值。U-shaped per-layer divergence pattern 提供了可操作的信号。[R1, R2 consensus]\n\n2. **设计精良的 C1 causal ablation**：用 BCE 在 KL-derived targets 训练来分离 target quality 和 training objective，50% 下 max Δ=0.59pp (2-seed)，30% 下 max Δ=1.70pp (3-seed)。实验设计有 genuine intellectual merit。[R1, R2 consensus]\n\n3. **系统化的实验覆盖**：3 架构（LLaMA-8B, Mistral-7B, Qwen-14B），6 个 sparsity 级别（25%-70%），两种 allocation 策略，消融涵盖 divergence 方向/relaxation/compensation/hyperparameter，3-seed 评估覆盖核心实验。[R2]\n\n4. **诚实的 claim 边界**：明确声明 \"Our contribution is empirical\"，诚实报告 50% downstream collapse、14B 反转、无 speedup、C4 OOD gap 等负面结果。在同类论文中属上游。[R1, R2 consensus]\n\n5. **训练效率高**：单 GPU 45 分钟，1000 步收敛，predictor <1% base model 参数，工程实用性好。[R1]\n\n6. **写作干净无 AI 痕迹**：em-dash 0 处、en-dash 0 处、黑名单词 0 处、过度过渡词 0 处。格式完全合规（ACL [review]、行号、匿名化、Limitations 位置、双栏）。[R2 验证]\n\n7. **引用完整**：46 条引用全部通过交叉验证，无虚构引用，Related Work 6 段覆盖所有主要方向，与 MaskLLM 的三点区分具体且有说服力。[R1, R2 consensus]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical, consensus] C1 因果消融推断逻辑有缺陷**\n- **因果链断裂**：C1 训练 BCE 在 KL-derived masks 上，匹配 KL 质量。论文推断\"target quality, not gradient coupling, drives quality\"。但 KL gradient coupling 是 *发现* 这些 superior masks 的必要条件。C1 证明的是 mask transferability（已知好 masks 可迁移到更简单的训练），而非 gradient coupling 在训练阶段不重要。论文的 framing 混淆了 mask discovery 阶段和 inference 阶段。\n- **Soft-vs-Hard confound 反常未解释**：BCE + Gumbel-Sigmoid = PPL 38.02，比 vanilla BCE (27.97) 更差。§4.5 给出的解释（\"penalty interferes with per-neuron optimization without global coordination\"）缺乏实验验证。如果 Gumbel 在 BCE 下有害，KL 的优势可能部分来自 KL loss 与 Gumbel 的特殊协同，而非纯粹的 target quality。\n- **建议**：(a) 修正 framing 为 \"mask transferability\" 而非 \"gradient coupling unimportant\"，明确区分 training-stage 和 inference-stage 的 coupling 角色；(b) 补充实验：去掉 penalty 只保留 Gumbel 的 BCE 作为控制；(c) 50% C1 增加至 3-seed。\n\n**N2 [critical, consensus] 14B Qwen MMLU 反转未被充分分析**\n- Qwen-2.5-14B 上 KL PPL 优于 TEAL (7.62 vs 8.73) 但 MMLU 严重反转 (63.7% vs 71.8%, -8.1pp)。BCE 在 14B 上 MMLU=71.67% 接近 TEAL，说明 KL mask patterns 在大模型上可能系统性损害知识检索任务。\n- Contribution #3 声称分析了 \"scale-dependent effects at 14B\"，但 §4.6 仅用一句话处理 (\"warrants further investigation\")。这不是可推迟到 future work 的问题——如果方法在最有价值的方向（更大模型）上 downstream 退化，实际可推广性存在根本质疑。\n- Abstract \"advantages hold on most tasks across architectures\" 与数据矛盾。\n- **建议**：(a) 分析 14B per-layer mask divergence 与 8B 对比；(b) 检查 14B layer retention 分布；(c) 提供至少一个假说并用已有数据验证/排除；(d) 修正 Abstract 和 Introduction 中的 cross-architecture claims。\n\n**N3 [critical, consensus] 49% PPL headline 来自 downstream 全面崩溃的 regime，framing 有误导性**\n- 49% PPL 改善 (11.79 vs 23.31) 来自 50% sparsity，但此 regime 下 MMLU≈28%（近随机）、GSM8K<2.2%。论文自身在 Limitations 承认 \"PPL is poor proxy for reasoning ability\"。将 49% 放在 Abstract 和 Introduction 最显眼位置，而 30% 的 18% PPL 改善放在次要位置，产生内部矛盾。\n- 实际可用操作点是 30%（downstream 保持 86-92% retention），但这个 regime 的改善幅度远不如 headline 宣传的 49%。\n- **建议**：以 30% sparsity 为 Abstract/Introduction 的主叙事支撑点，50% 降为分析补充。保留最多 2-3 个关键数字（mask 68% 偏离、30% PPL 18% 改善、compensation 冗余），删除其余。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [warning, consensus] Abstract 数据堆砌**\n- ~170 词中 15+ 个数字，读起来像 results 缩写而非独立叙事。审稿人 30 秒内难以判断核心价值。\n- R2 评为 Must-Fix，R1 评为 Should-Fix（presentation 非 soundness）。Director 判定为 Should-Fix：实质修复方向是削减 claim 数量（4→2-3），数字自然减少。\n\n**W2 [warning, consensus after correction] 50% KL 3-seed 数据未上浮至主表**\n- Table 2 中 50% KL 仅显示 seed 42 (PPL 11.79)，完整 3-seed 数据 (PPL 11.92±0.07, CV<1%) 在 Appendix E。30% BCE baseline 为单 seed。\n- R1 初始评为 critical 但描述不准确（30% KL 实际全部 3-seed），R2 用证据纠正。Director 判定 Should-Fix：50% 3-seed 应上浮至主表，30% BCE 应补充 multi-seed。\n\n**W3 [warning, consensus] 无 wall-clock speedup**\n- Pipeline 增加 6.4% overhead（126.78 vs 119.11 ms/forward）。论文诚实承认 sparse kernel 不在 scope 内，但作为 sparsity prediction 论文无加速演示是显著弱点。\n\n**W4 [warning, consensus] PPL 局限性未充分反映在实验叙事中**\n- Limitations 承认 PPL 是 poor proxy，但 §4.2 main results 叙事仍以 PPL 驱动。与 N3 overlapping。\n\n**W5 [warning, consensus] HellaSwag 和 PIQA 在 Abstract 引用但不在主表**\n- Abstract 引用 86.0%/92.5% retention，但 Table 2 仅含 ARC-c、WG、MMLU、GSM8K。如果指标重要到出现在 Abstract，应在主表中。\n\n**W6 [warning, consensus] Table 3 C1 ablation 30% KL 行缺 ARC-c/WG/GSM8K**\n- Max Δ=1.70pp claim 基于 MMLU 单一 metric，其他 downstream 可能有更大偏差。C1 作为核心 claim 支撑，比较应完整。\n\n### Minor Issues\n\n**M1** [info] 符号不一致：§3.1 $\\mathbf{x}^{(\\ell)}$ (\"hidden state after attention\") vs §3.2 $\\mathbf{h}$ (\"pre-FFN hidden state\")，指代同一量但符号切换。\n**M2** [info] KL (Kullback-Leibler)、TEAL、SPON 在首次使用时未展开定义。\n**M3** [info] 68% mask divergence 无 bootstrap confidence interval（64 samples, 131K tokens 的均值无 CI）。\n**M4** [info] SPON 2.4% PPL 改善 (12.08→11.79) 为单 seed，可能在噪声范围内（3-seed std≈0.07）。论文已 frame 为 \"optional, marginal\"。\n**M5** [info] Table 2 caption 5 行，信息密度过高。\n**M6** [info] Penalty controller terminology 不统一（\"Adaptive Penalty Sparsity Controller\" vs \"adaptive penalty controller\" vs footnote \"resembles augmented Lagrangian\"）。\n**M7** [info] §3.6 gradient analysis 中 SNR 5.14× 是经验度量，论文定位为 \"suggestive\" 是恰当的（R1 初始质疑 overclaiming，R2 rebut 指出论文未声称理论证明）。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 在交叉回应中达成明确共识：\n\n1. **C1 因果推断逻辑有缺陷** [R1-N2, R2-W1→upgraded]：C1 证明 mask transferability，不等于 gradient coupling 在训练阶段不重要。Framing 需修正。\n2. **14B MMLU 反转分析不足** [R1-N3, R2-N3]：BCE 14B MMLU=71.67% 接近 TEAL=71.83%，说明 magnitude masks 在大模型上对知识任务更优。需要 mechanism 分析。\n3. **49% PPL headline 有误导性** [R2-N2, R1 cross-AGREE]：50% regime downstream 崩溃但 PPL 大幅改善，作为 headline 有内部矛盾。\n4. **方法新颖性适合 Findings** [R1, R2 consensus]：KL+Gumbel+MLP predictor 是已有组件的自然组合，无技术 surprise，但 empirical findings 有价值。两位 Reviewer 均评 3.0 (Findings)。\n5. **无 wall-clock speedup 是显著弱点** [R1-W2, R2-W2]。\n6. **实验诚实度在同类论文中属上游** [R1, R2 consensus]：负面结果均被报告。\n7. **写作质量高，格式完全合规** [R2 验证，R1 agree]。\n\n---\n\n## Reviewer Divergence [REBUT]\n\n以下问题两位 Reviewer 存在分歧，经交叉回应后部分解决：\n\n1. **Single-seed 严重性** [R1: Must-Fix → R2 rebut with evidence → Director: Should-Fix]\n   - R1 声称 \"绝大多数结果 seed 42\"，R2 逐条反驳：30% KL 全部 8 个 metric-method 组合均为 3-seed，TEAL 是 deterministic 无需 multi-seed。实际 gap 仅在 50% 主表呈现和 30% BCE baseline。Director 采纳 R2 的纠正，降级为 Should-Fix。\n\n2. **Abstract 数据堆砌严重性** [R2: Must-Fix vs R1: Should-Fix]\n   - R2 认为 15+ 数字的 Abstract 无法通过 \"30 秒可读性测试\"；R1 认为这是 presentation 问题不应与 soundness 并列。Director 采纳 R1 的分级逻辑，判定 Should-Fix。\n\n3. **Three regime 分析** [R1: overfitting 4 points → R2 rebut: 6 points in Appendix]\n   - R1 未阅读 Appendix Table 7（6 个 sparsity 级别完整数据），R2 纠正后 R1 未坚持。Director 判定：regime 分析有 6 点数据支撑，不构成独立 weakness。\n\n4. **Compensation 验证范围** [R1: 仅 50% → R2 rebut: 事实错误]\n   - §4.5 明确报告 30% 和 50% 两个 sparsity level 的 compensation 冗余结果。R1 遗漏。Director 判定：不构成 weakness。\n\n5. **Taxonomy 质量** [R2: 人为构建感 vs R1: 有价值的 positioning]\n   - R1 论证 taxonomy 维度合理且帮助读者理解方法差异。Director 判定：不构成 weakness，但 MSE \"intermediate coupling\" 定义可更清晰。\n\n6. **Soundness 评分** [R1: 3.0 vs R2: 3.5]\n   - R1 因 C1 confound + seed 问题评 3.0；R2 因 C1 设计精良 + 30% 3-seed 完整评 3.5。Director 综合判定 Soundness 3.0（C1 逻辑缺陷是实质问题，不被 seed 覆盖率缓解）。\n\n7. **Excitement 评分** [R1: 3.0 vs R2: 2.5]\n   - R1 认为 mask divergence 发现有真正洞察价值（3.0）；R2 认为无 speedup + 窄 window + 已知组件组合限制实际影响（2.5）。Director 综合判定 Excitement 2.5（mask divergence 有分析价值但 practical impact 有限）。\n\n---\n\n## Questions for Authors\n\n1. **C1 反事实控制**：如果用随机初始化预测器（而非 KL-trained）导出 oracle mask 训练 BCE，质量如何？这才是测试 \"target quality vs gradient coupling\" 的完整控制。[R1-Q1, R2 cross-AGREE]\n\n2. **BCE+Gumbel 恶化机制**：为何 soft relaxation 使 BCE 从 27.97 恶化到 38.02？是 Gumbel noise 与 BCE binary target 冲突，还是 penalty controller 与 per-neuron 独立梯度冲突？去掉 penalty 只保留 Gumbel 的 BCE 表现如何？[R1-Q2, R2 cross-AGREE]\n\n3. **14B MMLU 反转根因**：BCE 在 14B MMLU=71.67% 接近 TEAL=71.83%，而 KL=63.7%。是否 KL 的 coupled gradient 在大模型上发现了牺牲知识检索的 mask patterns？14B per-layer mask divergence 数据能否澄清？[R1-Q3, R2-Q1, consensus]\n\n4. **Table 3 缺失数据**：30% KL 行缺 ARC-c/WG/GSM8K。如果这些 task 的 Δ 超过 1.70pp 或方向反转，会影响 C1 的结论。这些数据是否可用？[R2-Q2, R1 cross-AGREE]\n\n5. **Mask divergence 训练动态**：68% 偏离是训练终点测量。early checkpoint 的 Jaccard 数据能帮助理解 KL mask 何时、如何偏离 magnitude。[R2-Q3, R1 cross-AGREE]\n\n6. **Penalty controller 30% 公平性**：实际 sparsity 28.5% vs target 30%（偏差 5%）。TEAL 在 28.5% 下的 PPL 数据可作为 sanity check。[R2-Q5, R1 cross-AGREE]\n\n---\n\n## Missing References\n\n**共识遗漏**：\n- **OWL (Yin et al., 2024)**：研究 non-uniform layerwise sparsity allocation，与 §4.6 global vs uniform allocation 分析直接相关。[R1 cross-AGREE]\n\n**可选补充**（不影响评分）：\n- Sheared LLaMA (Xia et al., 2023)：structured pruning + distillation，与 MiniTron 方向相同。\n\n**排除项**：\n- LLM.int8() (Dettmers et al., 2022)：量化论文，不在 activation sparsity scope 内。[R2 cross-REBUT]\n- FLAP (An et al., ICML 2024)：structured weight pruning，与本文问题空间不同。[R1 cross-REBUT]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目未启用 `external_review.paperreview_ai`）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Soundness: 3.0/5** — 方法设计合理，C1 ablation 方向正确但因果推断逻辑有缺陷（mask transferability ≠ gradient coupling unimportant），soft-vs-hard confound 反常结果未充分解释。14B cross-architecture claim 与数据矛盾。30% 核心实验统计效力充分（3-seed），50% 主表呈现不完整。\n\n**Excitement: 2.5/5** — Mask divergence 发现有分析价值，三 regime allocation 分析对后续工作有参考意义。但方法是已知组件的自然组合（KL + Gumbel + MLP predictor），无技术 surprise；无 wall-clock speedup；practical window 仅 30%（实际加速更窄）；14B downstream 反转限制可推广性。实践者从论文学到的 actionable insight 有限——\"用 KL 替代 BCE\" 是一个 recipe 而非 principle。\n\n**Reproducibility: 3.5/5** — 超参数完整报告（d_b=128, τ schedule, lr, wd, batch, seq_len），GPU 型号和训练时间精确到分钟，3-seed 覆盖核心实验。但 evaluation protocol 细节（few-shot 设置、exact prompt templates）未完全明确，代码未开源。\n\n**Confidence: 4/5** — 两位 Reviewer 均熟悉 LLM activation sparsity、knowledge distillation 和 efficient inference 文献，仔细核实了核心实验数据和 claim 对应关系。\n\n### 判断理由\n\n**为什么是 Findings (3.0) 而非 Borderline Conference (3.5)**：\n1. 方法新颖性不足以支撑 Main：每个组件均为已有技术，组合合理但缺乏技术 surprise。两位 Reviewer 一致认为 Findings-appropriate。\n2. C1 因果推断——论文最核心的 claim——存在逻辑缺陷和未解释的反常结果。\n3. 14B downstream 反转是 scaling concern，不是可推迟到 future work 的问题。\n4. 无 wall-clock speedup，practical operating window 仅 30%。\n\n**为什么不低于 Findings (2.5)**：\n1. C1 causal ablation 实验设计有 genuine intellectual merit。\n2. 实验系统性和诚实度在同类论文中属上游。\n3. Mask divergence 发现和 allocation regime 分析对后续工作有参考价值。\n4. 写作质量高，格式完全合规，无 AI 痕迹。\n5. 引用完整无遗漏。\n\n### Rebuttal 优先级\n\n1. **最高优先级**：修正 C1 framing（区分 mask discovery 和 inference-stage quality）+ 补充 BCE+Gumbel 无 penalty 控制实验\n2. **高优先级**：14B MMLU 反转 mechanism 分析（per-layer divergence 对比 + layer retention 对比）\n3. **高优先级**：Abstract/Introduction 重构——30% 为主叙事，50% 降级；削减至 2-3 个核心 claim\n4. **中优先级**：50% KL 3-seed 上浮至主表；Table 3 补全 30% KL downstream 数据\n5. **低优先级**：符号统一、缩写展开、caption 精简\n\n---\n\n## Detailed Comments (per section)\n\n### Abstract\n- 15+ 数字在 170 词中，信息过载。删减至 3 个关键数字。[W1]\n- BCE/PPL 未展开（标准缩写可接受，但 KL/TEAL/SPON 应展开）。[M2]\n- \"advantages hold on most tasks across architectures\" 与 Qwen MMLU 反转矛盾。[N2]\n- 49% headline 来自 downstream 崩溃的 regime。[N3]\n\n### Introduction\n- 五段结构基本完整。从 SwiGLU sparsity → BCE 局限 → KL 提出 → C1 发现 → 贡献列表，逻辑流畅。\n- P2→P3 过渡略突兀：缺少 \"Therefore, we propose...\" 桥接。[R2]\n- Contribution #3 \"allocation-to-downstream interactions at 7-14B\" 在前文无铺垫。[R2]\n- 49% headline 在 L14 位置过于突出。[N3]\n\n### Related Work\n- 6 段组织清晰，positioning 准确。\n- MaskLLM 三点区分（sparsity type / mask generation / allocation）具体且有说服力。[R1, R2 consensus]\n- D2DMoE 的 \"intermediate coupling\" 描述可更精确（不仅是 MSE supervision）。[R2]\n- Griffin 引用感觉勉强（RG-LRU gating 与 SwiGLU 关系间接）。[R2]\n- 缺少 OWL (Yin et al., 2024) 的引用。[consensus]\n\n### Method (§3)\n- 数学叙述清晰，Eq.1-6 内部一致。\n- §3.5 adaptive penalty controller 设计合理，footnote disclaimer 是好做法。\n- §3.6 gradient analysis 定位恰当（\"suggestive\"）。SNR 5.14× 作为经验度量辅助 intuition。[R2 rebut R1 overclaiming 质疑]\n- ε=0.02 deadzone 选择依据未说明。[R1]\n- Figure 1 caption 可更自包含。[R2]\n\n### Experiments (§4)\n- §4.2 Main results：Table 2 中 30% 全部 3-seed，50% 主表仅 s42（appendix 有 3-seed）。Caption 5 行过长。[W2, M5]\n- §4.3 Extended training：iso-compute comparison (BCE 2.71× steps still worse) 有力支撑 KL 优势。\n- §4.4 Mask analysis + C1 ablation：论文核心贡献，设计精良但因果推断逻辑有缺陷。[N1]\n- §4.5 Ablation：Table 4 全面，但 SPON 2.4% 可能在噪声内，BCE+Gumbel 反常未充分解释。\n- §4.6 Scaling & cross-architecture：三 regime 分析有 6 点数据支撑（R2 纠正 R1 的 \"4 points\" 误读）。14B 结果仅一句话处理。[N2]\n\n### Conclusion\n- 极简（2 句话），核心发现覆盖。但过于压缩，缺少 limitations 和 future directions 的一句话总结。\n\n### Limitations\n- 全面且诚实。覆盖 PPL 局限性、sparse kernel 缺失、14B 反转、OOD gap、seed variance。\n- 14B 反转在此处被承认但分析不足。[N2]\n- 缺少对 C1 confound 局限性的讨论。[N1]\n\n### Ethics & Checklist\n- 完整且认真填写，无遗漏。Qwen-2.5-14B 的 license 信息已包含。\n\n### Appendix\n- 13 个 section 全部在正文中有 explicit reference。组织合理，补充了 hyperparameter sensitivity、OOD、stability、SNR、mask visualization 等完整数据。\n- Appendix E 的 3-seed 数据应上浮至主表。[W2]\n\n### 格式合规\n| 检查项 | 状态 |\n|--------|------|\n| 正文 ≤8 页 | ✅ |\n| ACL template [review] | ✅ |\n| Limitations 位置 | ✅ |\n| 行号开启 | ✅ |\n| 引用格式 (natbib) | ✅ |\n| 匿名化 | ✅ |\n| 图表字体 ≥7pt | ✅ |\n| 附录被正文引用 | ✅ |\n| 双栏格式 | ✅ |",
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 Findings",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 929 · 2026-05-19T06:45:03.945999+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4805
}
```

</details>

---


### Assistant

_source line 930 · 2026-05-19T06:45:14.039651+00:00_

审稿报告已投递至 Research Director。

---

**圆桌审稿完成 — Round 11 (Fresh)**

| 项目 | 结果 |
|---|---|
| **Overall Score** | **3.0 (Findings)** |
| **Soundness** | 3.0/5 |
| **Excitement** | 2.5/5 |
| **Reproducibility** | 3.5/5 |
| **Confidence** | 4/5 |
| **Reviewer 一致性** | 两人均给 3.0，核心问题高度收敛 |

**3 个 Must-Fix（共识）**：
1. C1 因果推断逻辑缺陷（mask transferability ≠ gradient coupling unimportant）+ BCE+Gumbel 反常未解释
2. 14B Qwen MMLU -8.1pp 反转无 mechanism 分析，cross-architecture claim 与数据矛盾
3. 49% PPL headline 来自 downstream 崩溃的 50% regime，framing 有误导性

**6 个 Should-Fix**：Abstract 数据堆砌、50% 3-seed 未上浮主表、无 wall-clock speedup、PPL 叙事偏重、HellaSwag/PIQA 不在主表、Table 3 缺失数据

**Rebuttal 最高优先级**：修正 C1 framing + 14B mechanism 分析 + Abstract/Introduction 重构围绕 30%

Issue Tracker 已同步更新（`artifacts/review_issues.yaml`）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 75

## Round 75

2 recorded events


### User

_source line 931 · 2026-05-19T06:45:16.752207+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。汇总关键分歧点：

1. **C1 confound 严重性**：我认为 Must-Fix，R2 认为 Should-Fix。C1 是论文最核心因果 claim，BCE+Gumbel 恶化至 38.02 的反常结果未被解释，应为 critical。
2. **Abstract 数据堆砌严重性**：R2 认为 Must-Fix，我认为 Should-Fix。Presentation 问题不应与 methodology 缺陷并列为同级。
3. **Excitement 评分差异**：我给 3/5，R2 给 2.5/5。mask divergence 发现有真正洞察价值，即使缺乏实际加速。
4. **总分一致**：两位 Reviewer 均给 3.0 (Findings level)。

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

_source line 932 · 2026-05-19T06:45:27.963226+00:00_

审稿报告已投递至 Research Director。

**Round 11 (Fresh Review) 总结：**

- **Overall: 3.0 (Findings)**，两位 Reviewer 完全一致
- **3 个 Must-Fix**：(1) C1 因果推断逻辑缺陷——证明的是 mask transferability 而非 gradient coupling 不重要；(2) 14B MMLU -8.1pp 反转缺乏 mechanism 分析；(3) 49% PPL headline 来自 downstream 崩溃的 regime，framing 有误导性
- **6 个 Should-Fix**：Abstract 数据堆砌、50% 3-seed 未上浮主表、无 wall-clock speedup、PPL 局限性未反映在叙事中、HellaSwag/PIQA 不在主表、Table 3 C1 缺失数据
- **格式完全合规**，写作无 AI 痕迹，引用完整无遗漏
- Issue Tracker 已同步更新（R11-N1~N3, W1~W6, M1~M2）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 76

## Round 76

68 recorded events


### User

_source line 933 · 2026-05-19T07:46:40.909640+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25

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

_source line 934 · 2026-05-19T07:46:48.665969+00:00_

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

_source line 935 · 2026-05-19T07:46:48.718863+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 936 · 2026-05-19T07:46:51.460275+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
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
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 937 · 2026-05-19T07:46:51.460707+00:00_



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

_source line 938 · 2026-05-19T07:46:56.388404+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
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
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 939 · 2026-05-19T07:46:56.388752+00:00_

No matching deferred tools found

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

_source line 940 · 2026-05-19T07:46:59.905982+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 941 · 2026-05-19T07:46:59.957206+00:00_



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

_source line 942 · 2026-05-19T07:47:02.970636+00:00_

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

_source line 943 · 2026-05-19T07:47:03.924799+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (230 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- c1_eval_30pct_s456（准备中）\n- kl_sparsity40_s42_eval_teal_uniform: KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.（准备中）\n- c4_download（准备中）\n- kl50_s456_train_eval（准备中）\n- mag_preservation_reg（准备中）\n- longbench_dense_v5（准备中）\n- kl_lagrangian_v2（准备中）\n- kl_norm_v3_quicktest（准备中）\n- mvp_kl_norm_s456（准备中）\n- spon_kl_s42（准备中）\n- …另有 3 项\n\n## 近期结论\n- **teal_28.5pct_sanity** (success): TEAL vanilla at 28.5% sparsity (matching KL predictor's actual achieved sparsity) produces similar PPL to TEAL at 30%, confirming the 1.5pp sparsity gap does not meaningfully affect the KL vs TEAL comparison. If PPL difference is < 0.1, the comparison is fair.\n- **mistral_dense_hellaswag_piqa** (success): Mistral-7B-v0.3 Dense baseline on HellaSwag (10-shot) and PIQA (0-shot). Required to complete Dense row in tab:mistral_downstream. Parent: lm_eval_mistral_dense. ← 基于 lm_eval_mistral_dense\n- **bce_gumbel_no_penalty_s42** (success): BCE+Gumbel without adaptive penalty controller isolates the effect of Gumbel relaxation from Lagrangian sparsity control. If PPL degrades
…[truncated 1726 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 944 · 2026-05-19T07:47:04.075902+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 call for papers submission guidelines"
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
    "query": "ACL Rolling Review ARR May 2026 call for papers submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 945 · 2026-05-19T07:47:05.584329+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex",
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
    "pattern": "**/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 946 · 2026-05-19T07:47:05.887198+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 947 · 2026-05-19T07:47:05.937801+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.pdf",
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
    "pattern": "**/paper/main.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 948 · 2026-05-19T07:47:05.988438+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf

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


### Tool result

_source line 949 · 2026-05-19T07:47:13.031401+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 call for papers submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review (ARR) in May 2026:

## Key Submission Requirements

All submitted papers are expected to describe original, completed and unpublished work. Submissions that exceed the length requirements, or are missing a limitations section, will be desk rejected.

Papers must not include authors' names and affiliations. Submitted papers must be prepared for two-way anonymized review.

## Reuse of Text and Ove
…[truncated 993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 8955
}
```

</details>

---


### Tool call

_source line 950 · 2026-05-19T07:47:18.862185+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission page limit format requirements long short paper"
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
    "query": "EMNLP 2026 submission page limit format requirements long short paper"
  }
}
```

</details>

---


### Tool call

_source line 951 · 2026-05-19T07:47:19.831464+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limit anonymization template",
  "allowed_domains": "['aclrollingreview.org', '2026.emnlp.org', 'aclweb.org']"
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
    "query": "ACL Rolling Review 2026 author guidelines page limit anonymization template",
    "allowed_domains": "['aclrollingreview.org', '2026.emnlp.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-19T07:47:20.434779+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR submission deadline May 2026 exact date",
  "allowed_domains": "['aclrollingreview.org']"
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
    "query": "ARR submission deadline May 2026 exact date",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-19T07:47:23.909711+00:00_

Web search results for query: "ARR submission deadline May 2026 exact date"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"Submission dates and process for 2024 Conferences","url":"http://aclrollingreview.org/submission-dates-for-2024/"},{"title":"Dates","url":"http://aclrollingreview.org/some-important-dates/"},{"title":"Submission Form Fields","url":"http://aclrollingreview.org/submissionform"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, the ARR submission deadline is always the 15th of the month. For May 2026, other dates vary due to the length of months, timing of weekends, etc., but the exact date for the May 2026 ARR submission deadline would be **May 15, 2026**.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 3474
}
```

</details>

---


### Tool result

_source line 954 · 2026-05-19T07:47:24.213335+00:00_

Web search results for query: "EMNLP 2026 submission page limit format requirements long short paper"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"}]

Based on the search results, here are the EMNLP 2026 submission page limit and format requirements for long and short papers:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Format Requirements

Manuscripts should be submitted electronically, in PDF format and formatted using the templates available on the conference website. Authors should not modify the style files nor use templates designed for other conferences. Submissions that do not conform to the required styles, including paper size, ma
…[truncated 521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 5351
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-19T07:47:26.173290+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines page limit anonymization template"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

Based on the search results, here's what I found about ACL Rolling Review 2026 author guidelines:

## Page Limits
Short papers have a maximum of 4 content pages, and long papers have a maximum of 8 content pages. Sections on ethical considerations and limitations do not count towards the page limit.

## Anonymization
Papers must not include authors' names and affiliations, and self-references that reveal the authors' identities (e.g., "We previousl
…[truncated 767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6341
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-19T07:47:31.195306+00:00_

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

_source line 957 · 2026-05-19T07:47:31.598766+00:00_

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
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 958 · 2026-05-19T07:47:32.402461+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "paper_framing.md",
  "max_chars": "12000"
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
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-19T07:47:32.453558+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md\", \"content\": \"# Paper Framing — distill_sparse_swiglu\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\\n- Deadline: 2026-05-25 (ARR submission)\\n- Track: Efficient Methods for NLP\\n\\n## Core Claims\\n\\n1. **KL distillation discovers fundamentally different (and superior) neuron importance patterns that magnitude-based oracles miss**: The C1 causal ablation (D059) proves that KL's advantage comes **entirely** from target quality (which neurons to keep), with gradient coupling contributing ≈0 across **both PPL and all downstream tasks**. **Controlled eval (TEAL 50% uniform, matched protocol)**: BCE+KL-targets PPL = **11.9638**, KL predictor PPL = **11.9638** (exact match). **Downstream confirmation (full-spectrum)**: All 4 downstream tasks (ARC-c, WinoGrande, MMLU, GSM8K) also match within <1pp delta, confirming gradient coupling = 0 across PPL + reasoning + knowledge + math dimensions. Standard BCE (magnitude masks) PPL ≈ 22.51. Target quality alone accounts for KL's full advantage. *Additional evidence from training eval (Gumbel hard mask)*: BCE+KL-targets PPL 9.29 @60.9% ≈ KL 9.21 @60.6%, consistent with controlled eval. The 53% mask divergence between KL-derived and magnitude-based masks is the core empirical finding: KL discovers a qualitatively different neuron importance landscape. **Implication**: The gradient coupling analysis (§3.6) provides mathematical intuition for *why* KL can discover better targets (coupled gradients explore joint neuron interaction patterns), but the causal driver is the resulting mask quality, not the gradient pathway per se. This shifts the contribution from \\\"engineering a better loss\\\" to \\\"discovering that output-distribution distillation reveals hidden neuron importance structure.\\\" **Supporting evidence**: (a) Iso-compute ablation: BCE with 
…[truncated 10492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-19T07:47:32.453930+00:00_

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

_source line 961 · 2026-05-19T07:47:32.504438+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 962 · 2026-05-19T07:47:38.187517+00:00_

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

_source line 963 · 2026-05-19T07:47:38.489169+00:00_

1	Learned sparsity predictors for SwiGLU LLMs universally use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train predictors with Kullback-Leibler (KL) divergence, coupling all mask decisions through the output distribution.
3	At 30\% sparsity on LLaMA-3.1-8B, the KL predictor ($<$1\% of base parameters) reduces perplexity by 18\% relative to TEAL with moderate downstream degradation, and renders post-hoc compensation (+67.2M params) redundant.
4	KL-derived masks diverge 68\% from magnitude-based masks; a causal ablation confirms that these mask targets, discovered through KL's coupled gradients, are the proximate quality driver when transferred to simpler objectives.
5	On Mistral-7B-v0.3, KL outperforms TEAL on 5 of 6 downstream tasks at 30\%; at 14B, perplexity generalizes but MMLU reverses.
6	At 50\% sparsity the perplexity advantage widens, though downstream reasoning collapses to near-random regardless of method, revealing a capacity phase transition.
7	

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

_source line 964 · 2026-05-19T07:47:38.489539+00:00_

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

_source line 965 · 2026-05-19T07:47:38.540127+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
9	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
10	A causal ablation confirms that these discovered mask targets are the proximate quality driver at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$=0.59pp at 50\%, 2-seed), while magnitude-trained BCE achieves 28.13$\pm$0.20. Gradient coupling remains necessary at the discovery stage.
11	
12	We instantiate a lightweight predictor (75.9M params, $<$1\% of base) trained with forward KL and Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} on LLaMA-3.1-8B~\cite{grattafiori2024llama3}.
13	At 30\% sparsity, the predictor reduces TEAL's perplexity by 18\% (8.96 vs.\ 10.97) with stable downstream under uniform allocation (MMLU 40.7$\pm$1.3\%, 3-seed); global top-$k$ amplifie
…[truncated 1505 chars]

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

_source line 966 · 2026-05-19T07:47:38.942900+00:00_

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

_source line 967 · 2026-05-19T07:47:39.899548+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
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
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from $\mathbf{x}^{
…[truncated 11376 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 968 · 2026-05-19T07:47:39.900670+00:00_

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

_source line 969 · 2026-05-19T07:47:40.354487+00:00_

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
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor} (DejaVu-style~\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distri
…[truncated 17862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 970 · 2026-05-19T07:47:40.405231+00:00_

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

_source line 971 · 2026-05-19T07:47:40.907834+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address the interaction between dynamic sparsity and quantization with zigzag-patterned weight layouts.
7	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
8	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
9	
10	\paragraph{Predictor-Based Contextual Sparsity.}
11	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
12	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
13	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
14	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
15	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
16	MaskLLM~\cite{fang2024maskllm} shares the principle of frozen weights + learnable masks + KL training, but the two methods differ in three fundamental ways.
17	First, \emph{spar
…[truncated 4220 chars]

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

_source line 972 · 2026-05-19T07:47:40.908336+00:00_

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

_source line 973 · 2026-05-19T07:47:41.360724+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	\vspace{-8pt}
4	
5	KL distillation discovers neuron importance patterns that diverge 68\% from magnitude-based masks; a causal ablation confirms that these mask targets, discovered via coupled gradients, are the proximate driver of inference-stage quality.
6	A predictor ($<$1\% of base) reduces TEAL's perplexity by 18\% at 30\% sparsity and renders compensation (+67.2M params) redundant; uniform allocation delivers $7.5\times$ smaller cross-seed $\sigma$.
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

_source line 974 · 2026-05-19T07:47:41.361211+00:00_

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

_source line 975 · 2026-05-19T07:47:41.813249+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades; 30\% appears to be the best-quality sparsity level for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	On Mistral-7B, KL wins 5 of 6 downstream tasks at 30\% but GSM8K reverses (11.1\% vs.\ TEAL's 15.9\%), consistent with GSM8K's sensitivity to the sparsity objective: reasoning tasks may require different optimization targets than knowledge and commonsense benchmarks.
6	The 30\% sparsity analysis is validated at 7--8B scale; at 14B, the MMLU gap persists regardless of allocation strategy (Appendix~\ref{app:14b}). Scaling to 70B remains untested.
7	Out-of-distribution evaluation on C4 (Appendix~\ref{app:ood}) shows the KL advantage transfers but with a wider gap: C4 PPL at 30\% is $1.74\times$ dense vs.\ $1.46\times$ on in-domain WikiText-2, which indicates that the predictor partially overfits to training-domain activation patterns. Extending OOD evaluation to 70\% sparsity is left to future work.
8	The causal ablation (\S\ref{sec:mask_analysis}) confirms that mask quality is the proximate driver of inference-stage quality, with KL's coupled gradients necessary at the discovery stage. C1 demonstrates mask transferability but does not fully resolve whether gradient coupling has additional benefits beyond target discovery. The mechanism by which KL's coupled gradient discovers superior mask patterns during training remains incompletely characterized; future work could trace per-layer mask divergence trajectories across training to identify when and where the patterns diverge.
9	At 30\% sparsity, global allocation exhibits 9.5pp cross-seed MMLU standard deviation (3-see
…[truncated 701 chars]

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

_source line 976 · 2026-05-19T07:47:41.863867+00:00_

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

_source line 977 · 2026-05-19T07:47:42.166937+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--14B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}, Qwen-2.5-14B~\cite{qwen2024qwen25}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 
…[truncated 1962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 978 · 2026-05-19T07:47:42.217725+00:00_

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

_source line 979 · 2026-05-19T07:47:42.268633+00:00_

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
…[truncated 20264 chars]

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

_source line 980 · 2026-05-19T07:47:54.824503+00:00_

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

_source line 981 · 2026-05-19T07:47:55.638138+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 18976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 813
}
```

</details>

---


### Tool call

_source line 982 · 2026-05-19T07:47:56.041840+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && cat main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex conclusion.tex limitations.tex ethics.tex appendix.tex 2>/dev/null | wc -l",
  "description": "Count total lines of paper content"
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
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && cat main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex conclusion.tex limitations.tex ethics.tex appendix.tex 2>/dev/null | wc -l",
    "description": "Count total lines of paper content"
  }
}
```

</details>

---


### Tool result

_source line 983 · 2026-05-19T07:47:56.393553+00:00_

966
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 984 · 2026-05-19T07:47:56.494407+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 985 · 2026-05-19T07:47:56.545673+00:00_

issues:
  # ============================================================
  # Round 11 (fresh review) — Active issues with action items
  # ============================================================

  - id: "R11-N1"
    summary: "C1 causal ablation: inference logic flawed (mask transferability ≠ gradient coupling unimportant) + soft-vs-hard confound + BCE+Gumbel反常未解释"
    category: method
    severity: critical
    status: in_progress
    first_raised_round: 11
    last_seen_round: 11
    mentions:
      - {round: 11, reviewers: [1, 2], note: "Full consensus. C1 proves mask transferability, not that gradient coupling is unimportant. BCE+Gumbel=38.02 unexplained. 50% only 2-seed."}
    action_items:
      - {round: 11, action: "Reframe C1 narrative: 'mask transferability' not 'gradient coupling unimportant'. Distinguish training-stage coupling (discovers masks) vs inference-stage quality (mask quality). Modify §4.4 + Abstract + Intro.", assigned_to: "paper_agent", status: in_progress}
      - {round: 11, action: "BCE+Gumbel no-penalty control experiment (bce_gumbel_no_penalty_s42) to isolate Gumbel vs penalty effects. ~1h GPU.", assigned_to: "main_agent", status: in_progress}
    resolution: ""
    resolution_round: null

  - id: "R11-N2"
    summary: "14B Qwen MMLU -8.1pp reversal: only 'warrants further investigation', no mechanism analysis; Contribution 3 claim-evidence mismatch"
    category: experiment
    severity: critical
    status: in_progress
    first_raised_round: 11
    last_seen_round: 11
    mentions:
      - {round: 11, reviewers: [1, 2], note: "Full consensus. BCE 14B MMLU=71.67% matches TEAL=71.83%, suggesting KL masks systematically harm knowledge tasks at scale. Abstract 'advantages hold on most tasks' contradicts data."}
    action_items:
      - {round: 11, action: "14B per-layer mask divergence analysis (qwen14b_mask_divergence_analysis) + layer retention distribution, compare with 8B. ~1-2h GPU.", assigned_to: "main_agent", status: in_progr
…[truncated 21981 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 986 · 2026-05-19T07:48:10.711656+00:00_

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

_source line 987 · 2026-05-19T07:48:10.812426+00:00_

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

_source line 988 · 2026-05-19T07:48:13.223174+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
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
    "query": "read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-19T07:48:13.273815+00:00_



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

_source line 990 · 2026-05-19T07:48:18.046211+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/distill_sparse_swiglu/config.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
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
    "pattern": "**/distill_sparse_swiglu/config.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
  }
}
```

</details>

---


### Tool result

_source line 991 · 2026-05-19T07:48:18.146987+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 992 · 2026-05-19T07:48:18.247830+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/distill_sparse_swiglu/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects"
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
    "pattern": "**/distill_sparse_swiglu/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects"
  }
}
```

</details>

---


### Tool result

_source line 993 · 2026-05-19T07:48:18.650201+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/registry.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 994 · 2026-05-19T07:48:25.450220+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null; grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -5",
  "description": "Search for external review config"
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
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null; grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -5",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-19T07:48:25.701663+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-19T07:49:06.301233+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验可靠性**的审查。\n\n## 论文信息\n- 标题: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n- 路径: projects/distill_sparse_swiglu/paper/main.tex（各章节分文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- 目标 venue: EMNLP 2026（ARR May 2026 cycle）\n\n## Venue 要求\n- Long paper: 8页正文（references/limitations/ethics/appendix 不计入）\n- 模板: ACL 官方模板，`[review]` 选项\n- 匿名: Double-blind（two-way anonymized）\n- Limitations section 必需，缺失会 desk reject\n- 评分标准（ARR Overall Assessment）: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查重点\n1. **方法严谨性**: §3 梯度分析（BCE vs KL gradient）的数学正确性和推理逻辑；Gumbel-Sigmoid 松弛的理论依据；自适应惩罚控制器的收敛性质\n2. **实验可靠性**: 统计功效（seed 数量、标准差报告）；baseline 公平性（BCE/KL 训练步数、计算量是否可比）；C1 因果消融的实验设计是否能支撑其 claim\n3. **核心 claim 验证**: \"68% mask divergence\"、\"compensation redundancy\"、\"phase transition\" 三个核心发现的证据链是否完整\n4. **数据一致性**: 检查正文、表格、附录中的数字是否自洽；Abstract/Intro 中引用的数字是否与实验部分对应\n\n## 输出格式\n```\n## Summary (2-3句)\n\n## Strengths (逐条)\n\n## Weaknesses (逐条，标注严重程度: [Must-Fix] / [Should-Fix] / [Minor])\n\n## Questions (需要作者回答的)\n\n## Missing References\n\n## Detailed Comments (逐节)\n\n## Overall Assessment\n- Score: X.X (使用 ARR 评分标准)\n- Confidence: X/5\n- 推荐: Main / Findings / Reject\n```\n\n请阅读完整论文后给出严格、客观的审稿意见。"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验可靠性**的审查。\n\n## 论文信息\n- 标题: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n- 路径: projects/distill_sparse_swiglu/paper/main.tex（各章节分文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- 目标 venue: EMNLP 2026（ARR May 2026 cycle）\n\n## Venue 要求\n- Long paper: 8页正文（references/limitations/ethics/appendix 不计入）\n- 模板: ACL 官方模板，`[review]` 选项\n- 匿名: Double-blind（two-way anonymized）\n- Limitations section 必需，缺失会 desk reject\n- 评分标准（ARR Overall Assessment）: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查重点\n1. **方法严谨性**: §3 梯度分析（BCE vs KL gradient）的数学正确性和推理逻辑；Gumbel-Sigmoid 松弛的理论依据；自适应惩罚控制器的收敛性质\n2. **实验可靠性**: 统计功效（seed 数量、标准差报告）；baseline 公平性（BCE/KL 训练步数、计算量是否可比）；C1 因果消融的实验设计是否能支撑其 claim\n3. **核心 claim 验证**: \"68% mask divergence\"、\"compensation redundancy\"、\"phase transition\" 三个核心发现的证据链是否完整\n4. **数据一致性**: 检查正文、表格、附录中的数字是否自洽；Abstract/Intro 中引用的数字是否与实验部分对应\n\n## 输出格式\n```\n## Summary (2-3句)\n\n## Strengths (逐条)\n\n## Weaknesses (逐条，标注严重程度: [Must-Fix] / [Should-Fix] / [Minor])\n\n## Questions (需要作者回答的)\n\n## Missing References\n\n## Detailed Comments (逐节)\n\n## Overall Assessment\n- Score: X.X (使用 ARR 评分标准)\n- Confidence: X/5\n- 推荐: Main / Findings / Reject\n```\n\n请阅读完整论文后给出严格、客观的审稿意见。"
  }
}
````

</details>

---


### Tool result

_source line 997 · 2026-05-19T07:49:18.733685+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12432
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-19T07:49:18.888992+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**的审查。\n\n## 论文信息\n- 标题: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n- 路径: projects/distill_sparse_swiglu/paper/main.tex（各章节分文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- 目标 venue: EMNLP 2026（ARR May 2026 cycle）\n\n## Venue 要求\n- Long paper: 8页正文（references/limitations/ethics/appendix 不计入）\n- 模板: ACL 官方模板，`[review]` 选项\n- 匿名: Double-blind（two-way anonymized）\n- Limitations section 必需，缺失会 desk reject\n- 评分标准（ARR Overall Assessment）: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查重点\n1. **新颖性评估**: 相对于 MaskLLM、SPON、FastForward、DejaVu 等已有工作，本文的真正增量贡献是什么？Table 1 的 taxonomy 是否准确？\"Per-token × Coupled\" 这个 cell 的填充是否构成足够新颖的贡献？\n2. **叙事完整性**: Abstract → Introduction → Method → Experiments → Conclusion 是否形成连贯主线？核心 claim（mask pattern discovery）是否在各章节一致体现？贡献列表中的每条是否有对应的实验支撑？\n3. **写作质量**: 检查 AI 写作痕迹（em-dash、-ing phrases、过度分段、黑名单用词如 leverage/delve/utilize）；专有名词是否首次出现时定义；符号一致性\n4. **格式合规**: 页数限制；匿名化（是否泄露身份信息）；引用格式（natbib）；图表规范（caption 自包含、字体大小、知识密度）\n5. **引用覆盖**: Related Work 是否遗漏直接相关方法？baseline 论文、benchmark 论文、理论基础是否都有引用？\n\n## 输出格式\n```\n## Summary (2-3句)\n\n## Strengths (逐条)\n\n## Weaknesses (逐条，标注严重程度: [Must-Fix] / [Should-Fix] / [Minor])\n\n## Questions (需要作者回答的)\n\n## Missing References\n\n## Detailed Comments (逐节)\n\n## Overall Assessment\n- Score: X.X (使用 ARR 评分标准)\n- Confidence: X/5\n- 推荐: Main / Findings / Reject\n```\n\n请阅读完整论文后给出严格、客观的审稿意见。"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**的审查。\n\n## 论文信息\n- 标题: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n- 路径: projects/distill_sparse_swiglu/paper/main.tex（各章节分文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- 目标 venue: EMNLP 2026（ARR May 2026 cycle）\n\n## Venue 要求\n- Long paper: 8页正文（references/limitations/ethics/appendix 不计入）\n- 模板: ACL 官方模板，`[review]` 选项\n- 匿名: Double-blind（two-way anonymized）\n- Limitations section 必需，缺失会 desk reject\n- 评分标准（ARR Overall Assessment）: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查重点\n1. **新颖性评估**: 相对于 MaskLLM、SPON、FastForward、DejaVu 等已有工作，本文的真正增量贡献是什么？Table 1 的 taxonomy 是否准确？\"Per-token × Coupled\" 这个 cell 的填充是否构成足够新颖的贡献？\n2. **叙事完整性**: Abstract → Introduction → Method → Experiments → Conclusion 是否形成连贯主线？核心 claim（mask pattern discovery）是否在各章节一致体现？贡献列表中的每条是否有对应的实验支撑？\n3. **写作质量**: 检查 AI 写作痕迹（em-dash、-ing phrases、过度分段、黑名单用词如 leverage/delve/utilize）；专有名词是否首次出现时定义；符号一致性\n4. **格式合规**: 页数限制；匿名化（是否泄露身份信息）；引用格式（natbib）；图表规范（caption 自包含、字体大小、知识密度）\n5. **引用覆盖**: Related Work 是否遗漏直接相关方法？baseline 论文、benchmark 论文、理论基础是否都有引用？\n\n## 输出格式\n```\n## Summary (2-3句)\n\n## Strengths (逐条)\n\n## Weaknesses (逐条，标注严重程度: [Must-Fix] / [Should-Fix] / [Minor])\n\n## Questions (需要作者回答的)\n\n## Missing References\n\n## Detailed Comments (逐节)\n\n## Overall Assessment\n- Score: X.X (使用 ARR 评分标准)\n- Confidence: X/5\n- 推荐: Main / Findings / Reject\n```\n\n请阅读完整论文后给出严格、客观的审稿意见。"
  }
}
````

</details>

---


### Tool result

_source line 999 · 2026-05-19T07:49:20.532751+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1643
}
```

</details>

---


### Assistant

_source line 1000 · 2026-05-19T07:49:28.256623+00:00_

Round 1 独立审稿任务已分配：
- **Reviewer 1**（方法严谨性 + 实验可靠性）— 已派发
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）— 已派发

等待两位 Reviewer 返回审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 77

## Round 77

2 recorded events


### User

_source line 1001 · 2026-05-19T07:54:29.980313+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见

## Summary (2-3句)

本文提出用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器，核心发现是 KL 的耦合梯度能发现与激活幅值差异 68% 的神经元重要性模式，且因果消融（C1）证实这些 mask target 是推理质量的近因驱动力。在 LLaMA-3.1-8B 上 30% 稀疏度下 PPL 降低 18%（8.96 vs 10.97），并使补偿网络（+67.2M 参数）变得冗余；但方法在 14B 上出现 MMLU 逆转（-8.1pp），且未实现任何 wall-clock 加速。

## Strengths (逐条)

**S1. 问题定义清晰且有洞察力。** BCE 逐神经元训练与 TEAL 全局 top-k 推理分配之间的 mismatch 是一个真实且未被正式分析的问题（§1, §2.6）。梯度分析（§2.6, Eq. 推导）从结构上解释了两种目标的差异，为实验提供了理论动机。

**S2. C1 因果消融设计巧妙。** Table 3 的 C1 ablation 将 mask target quality 与 gradient coupling 解耦，是本文最有价值的实验设计。BCE 在 KL-derived masks 上训练后能复现 KL 质量（50% 稀疏度 max Δ=0.59pp），而 magnitude-trained BCE 则差 2.4×，令人信服地证明了 mask 质量而非训练机制本身是关键因素。

**S3. 消融实验系统且覆盖面广。** Table 4 系统隔离了 divergence direction（forward/reverse/JSD）、relaxation method（Gumbel vs STE）、compensation redundancy 等设计选择的贡献，实验设计规范。

**S4. 跨架构评估诚实。** 在 Mistral-7B（5/6 tasks KL 胜出）和 Qwen-2.5-14B（MMLU 逆转 -8.1pp）上的评估，包括负面结果的坦诚报告（§4.6, Table 8, Table 10），体现了科学诚信。

**S5. 写作质量高，无明显 AI 痕迹。** 全文无 em-dash（—）、无解释性 en-dash（–）、无黑名单用词（leverage/delve/utilize/facilitate）、无过度分段。叙事从 mismatch → gradient analysis → mask discovery → causal ablation 形成连贯主线。唯一轻微问题是 method.tex 中 "in context of"（应为 "in the context of"），但这不是 AI 标志。

**S6. Taxonomy（Table 1）定位准确。** 沿 correction granularity × training signal coupling 两个轴组织先前工作，每个 cell 的分类有文献支撑。Per-token × Coupled 确实是未被探索的组合。

**S7. 超参数鲁棒性充分。** Appendix B-D 展示了 bottleneck dimension（<3% 变化）、temperature schedule（<1.8%）、training convergence（800 步即饱和）的敏感性分析。

## Weaknesses (逐条)

### Must-Fix

**N1. [Must-Fix] 新颖性有限：核心贡献是 loss function 替换，与 MaskLLM 的技术距离较小**
- MaskLLM [Fang et al., 2024] 已经实现了 frozen weights + learnable masks + KL divergence + Gumbel relaxation 的组合。本文与 MaskLLM 的三个区别（activation vs weight sparsity, predictor network vs direct mask parameters, global top-k vs N:M allocation）是重要的工程差异，但不构成方法论创新。
- §3 的 Related Work 详细区分了本文与 MaskLLM，但缺乏直接实验对比。即使稀疏类型不同，在相同评估协议下对比两者（例如将 MaskLLM 的 2:4 weight sparsity 应用于同一模型并比较 PPL/downstream）可以更有说服力地展示 activation sparsity + KL 的独特价值。
- 填充 taxonomy 中的空白 cell（Per-token × Coupled）是自然的组合，本身不构成足够的新颖性。论文的核心 claim "KL discovers superior mask targets" 是一个有价值的实证发现，但方法层面缺乏创新。
- 建议：强化 C1 ablation 的独特贡献（这确实是新的分析方法），明确将论文定位为 empirical study 而非方法创新。

**N2. [Must-Fix] 未实现 wall-clock 加速，且当前实现增加 6.4% 开销**
- Table 6 (Appendix A) 显示 KL predictor 增加 6.4% 推理延迟（126.78 vs 119.11 ms/forward）。对于一篇稀疏性论文，这是根本性缺陷——稀疏预测的全部价值主张在于推理加速。
- §1 最后一段和 Appendix A 坦诚承认"actual speedup requires sparse kernel integration"，但这使得论文的 practical impact 不完整。
- 在 EMNLP 投稿中，如果论文定位为"prediction quality study"而非"systems paper"，这可以接受，但需要在 Abstract 和 Introduction 中更明确地框定贡献范围，避免给审稿人造成"这是加速方法但没加速"的印象。
- 当前 Abstract 第 3 句已提到 "renders post-hoc compensation redundant"，但读者自然期望看到因此带来的加速——建议在 Abstract 中明确说明 wall-clock speedup 不在本文范围内。

**N3. [Must-Fix] 14B 实验结果动摇方法的可扩展性**
- Qwen-2.5-14B 上 MMLU 63.7% vs TEAL 71.8%（-8.1pp, Table 10），且这一逆转在 uniform allocation 下同样存在（64.49% vs 66.34%），不是 allocation 策略的问题。
- §4.6 提出"KL's PPL-optimal reallocation redirects resources from early knowledge-encoding layers"作为假设，但承认"Verification requires layer-wise probing beyond our current scope"。这不是一个合格的解释——它是一个未验证的猜测。
- 从 7B → 14B 就出现质量逆转，对 70B（未测试）的前景是一个严重警告。对于 EMNLP 2026，审稿人会期望至少在一个 13B+ 模型上看到一致的改进。
- 建议：要么进行 layer-wise probing 验证假设，要么将 14B 结果作为核心 limitation 在 Introduction 中提前交代，而不是仅在 §4.6 末尾和 Limitations 中提及。

### Should-Fix

**W1. [Should-Fix] 30% 全局分配下 MMLU 种子方差极高（σ=9.5pp）**
- Table 2: KL global 30% MMLU 35.7±9.5%（3-seed）。个别 seed 从 25.3% 到 43.5%（Table 7 脚注），跨越近 20pp。
- 虽然 uniform allocation 解决了这个问题（40.7±1.3%），但这说明 KL predictor 的 mask 与全局 top-k 分配的交互在某些初始化下是不稳定的。论文将此归因于"late-layer starvation (L31 retention 28.4%) interacting with predictor initialization"（§4.2），但未提出解决方案。
- 建议：补充分析哪些 seed 导致极端值及其 per-layer retention 差异。

**W2. [Should-Fix] C1 ablation 存在已承认但未解决的 soft-vs-hard confound**
- §4.4 Soft-vs-Hard Confound 段：C1 同时改变了 gradient coupling 和 mask representation（hard binary vs soft Gumbel-Sigmoid），但仅用 BCE+Gumbel 的失败（PPL 32.22）来论证"softness alone does not explain KL's advantage"。
- 这个反证是不完整的：BCE+Gumbel 失败可能是因为 BCE loss + Gumbel 的组合本身有问题（Table 4 证实 BCE+Gumbel 比 vanilla BCE 更差），而不是 softness 不重要。
- 正确的消融应该是：KL 训练但用 hard mask forward pass（STE），与 KL + Gumbel 对比。Table 4 中 STE 的 PPL 15.77 vs Gumbel 的 11.79 部分回答了这个问题，但方向相反：这说明 softness 对 KL 也很重要。
- 建议：承认 C1 ablation 无法完全解耦 target quality 和 gradient representation，降低 "mask quality is the proximate driver" 的 claim 强度。

**W3. [Should-Fix] 训练集/评估集同源（WikiText-103 → WikiText-2）**
- 主要结果基于 WikiText-2 PPL，训练在 WikiText-103 上进行。两者来自同一数据源（Wikipedia），存在分布重叠。
- C4 OOD 评估（Appendix D）显示 gap 更大：30% 稀疏度 C4 PPL 为 1.74× dense vs WikiText-2 的 1.46× dense。论文在 Limitations 中承认"predictor partially overfits to training-domain activation patterns"。
- 对于主结果，建议至少在 main table 中加入 C4 PPL 一列，让读者直接看到 OOD 性能。

**W4. [Should-Fix] Downstream 在 "best quality" 30% 稀疏度下仍然严重退化**
- 论文定位 30% 为"best-quality sparsity level for downstream fidelity"（Limitations），但 GSM8K 从 48.75% 降到 8.0±0.7%（84% 退化），MMLU 从 65.27% 降到 40.7±1.3%（uniform, 38% 退化）。
- ARC-c 从 58.28% 到 43.7±2.5%（25% 退化），WinoGrande 从 78.06% 到 68.9±0.4%（12% 退化）。
- 这些退化幅度在 30% 稀疏度下是相当大的。论文 focused on PPL improvement 但对 downstream 退化的讨论不够充分。
- 建议：将 "30% is the best-quality level" 改为 "30% is the least-degraded level"，并讨论这种退化是否对实际部署有影响。

**W5. [Should-Fix] Conclusion（§6）仅两句话，过于简短**
- Conclusion 只有两句话：重复了 68% divergence 和 C1 ablation 的结果，没有 future work 讨论、没有 broader impact 分析、没有对研究方向的展望。
- 对比：Limitations section 倒是写得很充分（12 行），但 Conclusion 作为论文的收尾部分，不应该比 Limitations 还短。
- 建议：扩展 Conclusion 到 4-6 句，加入未来方向（N:M structured sparsity, 70B scaling, single-predictor-multi-target）。

**W6. [Should-Fix] Introduction 中 "68% divergence" 重复三次**
- §1 第 2 段、第 3 段末、贡献列表第 1 条都提到了 "68% divergence from magnitude-based masks"。Abstract 也有一次。
- 这种重复在短 Introduction 中显得冗余，建议在 Abstract 和 Contributions 中各提一次即可。

### Minor

**M1.** method.tex L116: "in context of the full sparse computation" — 语法应为 "in the context of"。

**M2.** LaTeX 源码中遗留了大量 `% exp_id: xxx` 注释（如 `% exp_id: kl30_3seed_global`），camera-ready 前应清理。

**M3.** §4.1 Evaluation 段只列出 ARC-c, WG, MMLU, GSM8K 的 few-shot 设置，但 Appendix F 还评估了 HellaSwag (10-shot) 和 PIQA (0-shot)。HellaSwag/PIQA 应在 §4.1 中提及，且保持一致。

**M4.** Table 3 (C1): s42† 使用"an earlier oracle checkpoint"，脚注解释不充分——为什么不用相同 checkpoint？如果不可用，应解释原因。

**M5.** Abstract 第 1 句在 Abstract 内未定义 SwiGLU 的全称（虽然 SwiGLU 在 NLP 社区中已较常见，但按规范应在 Abstract 首次出现时定义）。

**M6.** §2.5 自适应惩罚控制器用了大量篇幅描述一个本质上标准的技术（multiplicative penalty with deadzone）。脚注已承认其与 augmented Lagrangian 的关系，但该 section 占据了 Method 中不成比例的空间。

**M7.** Figure 1 caption 说 "Method overview" 但我无法验证图片内容（仅从 tex 可读）。如果 fig1_overview.pdf 只是一个简单的 pipeline 图（predictor → scores → top-k → sparse FFN），则信息密度可能不足以占据整栏宽度。

## Questions (需要作者回答)

**Q1.** 14B MMLU 逆转（-8.1pp）是否在其他 seed 下也一致出现？Table 10 只报告了 seed 42 的结果。

**Q2.** KL predictor 发现的 mask 与 magnitude mask 有 68% divergence，但 KL mask 中被选中的低幅值神经元对输出的实际贡献是什么？是否有 ablation 验证这些"KL-only"神经元确实对 output distribution 有不可替代的贡献？

**Q3.** GSM8K 在 Mistral-7B 上逆转（11.1% vs TEAL 15.9%）、在 LLaMA-8B 上接近（8.0% vs TEAL 7.88%）。是否有结构性原因解释 reasoning tasks 对 KL objective 的敏感性？

**Q4.** §4.6 提到 30% penalty controller 有 5% residual deviation（实际 28.5% vs 目标 30%），论文声称"negligible relative to KL vs TEAL gap"。但 TEAL at 28.5% 与 TEAL at 30% 的 PPL 差 0.67——这是否意味着部分 KL 优势来自于实际评估在更低稀疏度？

**Q5.** 有没有考虑在 C4 或其他非 WikiText 数据上训练 predictor 以减少 domain overfitting？

## Missing References

引用整体覆盖较好，但以下方面可考虑补充：
1. **Dettmers et al. (2022), "LLM.int8()"** — 量化与稀疏的交互是一个相关方向，论文引用了 Wang et al. 2025 但没引用更基础的量化工作。
2. **Kurtic et al. (2023/2024), "Sparse Fine-Tuning"** — 稀疏+微调的交叉方向。
3. 无明显遗漏直接竞争方法。TEAL, DejaVu, FastForward, SPON, MaskLLM, ShadowLLM, D2DMoE 均已引用。

## Detailed Comments (逐节)

**Abstract**: 结构合理，四个必答问题都有回答。但"renders post-hoc compensation redundant"的表述可能误导读者期望速度提升。"capacity phase transition"在 Abstract 中出现但未定义，读者可能困惑。

**Introduction**: 叙事线清晰（mismatch → gradient analysis → experiments → contributions），但"68% divergence"重复过多（见 W6）。Contribution 第 3 条"non-monotonic allocation preference at 8B and scale-dependent effects at 14B"相对较弱，更像是 observation 而非 contribution。

**Related Work**: 覆盖全面，与 MaskLLM 的区分详细（§3 para 2）。MoE routing 段落（§3 最后一段）与主线关系稍远但可接受。

**Method**: 整体清晰。§2.6 gradient analysis 的 suggestive/evidence distinction 处理得当。Taxonomy (§2.7) 有用但 "Intermediate (MSE)" 列只有 ShadowLLM 和 D2DMoE 两个方法支撑，分类粒度是否过细？

**Experiments**: 最强的部分。C1 ablation (§4.4)、ablation table (§4.5)、regime analysis (§4.6) 都是扎实的实验设计。但 main table (Table 2) 缺少 HellaSwag/PIQA，且 30% downstream degradation 讨论不足。

**Limitations**: 全面、诚实，是本文的优点之一。

**Appendix**: 内容丰富（latency, sensitivity, OOD, cross-arch），所有附录在正文中都有引用。

## Overall Assessment

- **Score: 3.0** (Findings)
- **Confidence: 4/5** (Quite sure)
- **推荐: Findings**

**理由**: 论文是一篇扎实的实证研究，实验设计规范（特别是 C1 ablation），结果报告诚实（包括 14B 逆转和 downstream collapse）。但核心贡献是 loss function 替换（BCE → KL），方法新颖性有限；未实现 wall-clock 加速使实际影响不完整；14B 实验结果动摇可扩展性。论文的分析价值（KL discovers different masks, mask quality is the driver, allocation regime analysis）足以支撑 Findings 接收，但新颖性和影响力不足以支撑 Main conference。

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计规范，C1 ablation 巧妙，但 soft-vs-hard confound 未完全解决，14B 逆转未解释 |
| Excitement | 2.5/5 | 核心贡献是 loss swap，方法层面创新有限；分析有价值但影响力受限于无实际加速 |
| Reproducibility | 4/5 | 超参数完整，3-seed 评估，GPU 和训练细节齐全；但未开源代码 |
| Overall | 3.0/5 | Findings 水平：扎实的实证研究，但新颖性和实际影响力不足以进入主会议 |


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

_source line 1002 · 2026-05-19T07:54:38.555534+00:00_

Reviewer 2 审稿意见已收到（Score: 3.0 Findings）。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 78

## Round 78

2 recorded events


### User

_source line 1003 · 2026-05-19T07:54:45.567256+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交。

总结：给出 **Overall 3.0 (Findings)** 评分，Confidence 4/5。

核心判断：
- **优势**：C1 因果消融设计巧妙，实验系统且诚实（含负面结果报告），写作质量高无 AI 痕迹
- **主要问题**：(1) 方法新颖性有限，核心是 BCE→KL 的 loss swap，与 MaskLLM 技术距离小；(2) 未实现 wall-clock 加速，当前反而增加 6.4% 开销；(3) 14B 上 MMLU 逆转 -8.1pp 动摇可扩展性
- **推荐 Findings 而非 Main**：分析价值（mask divergence discovery, C1 ablation, allocation regime analysis）足以支撑 Findings，但新颖性和实际影响力不够 Main conference

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

_source line 1004 · 2026-05-19T07:54:55.293292+00:00_

Reviewer 2 审稿收到，核心判断：Findings 3.0。等待 Reviewer 1 完成独立审稿后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 79

## Round 79

6 recorded events


### User

_source line 1005 · 2026-05-19T07:58:20.892593+00:00_

[Reviewer 1 审稿意见]:
## Summary (2-3句)

本文提出用 forward KL 散度替代传统 BCE 训练 SwiGLU LLM 的稀疏预测器，通过 Gumbel-Sigmoid 松弛实现端到端可微训练。实验在 LLaMA-3.1-8B 上表明 KL 预测器在 30% 稀疏度下相比 TEAL 降低 18% PPL，并且使补偿网络冗余。论文提供了系统的消融研究和跨架构验证（Mistral-7B、Qwen-14B），但存在数据不一致、因果声明过度和缺乏实际加速等问题。

---

## Strengths (逐条)

**S1. 问题定义清晰，动机合理。** BCE 的逐神经元独立训练与全局 top-k 推理分配之间的 mismatch 被准确识别（§1, §3.6）。这个观察本身就是一个有价值的 contribution。

**S2. 消融设计全面。** Table 3（§4.4）系统隔离了每个设计选择的贡献：divergence 方向（forward KL > JSD > reverse KL）、松弛方式（Gumbel > STE，Δ=3.98）、loss function（KL vs BCE 效果是松弛效果的 5.1×）。这种层层剥离的实验设计在同类工作中少见。

**S3. 诚实报告负面结果。** GSM8K 在 Mistral 上的反转（11.1% vs TEAL 15.9%，Table 8）、14B MMLU 反转（63.7% vs TEAL 71.8%，Table 7）、50% 稀疏度下推理能力全面崩溃（MMLU ≈ 28%，Table 1）均被正面讨论，没有回避。

**S4. C1 因果消融是创造性的实验设计。** 用 BCE 训练在 KL 导出的 mask 上（§4.4, Table 2），将 mask 质量与梯度耦合解耦，思路巧妙。尽管存在 confound（下文讨论），这个实验框架本身值得肯定。

**S5. 超参数鲁棒性有据可查。** Appendix B 显示 $d_b$ 敏感度 <3%、温度敏感度 <1.8%、训练在 800 步即饱和（Table 4-6）。这些结果增强了方法的可信度。

**S6. 跨架构验证覆盖 3 种模型。** LLaMA-3.1-8B（主实验）、Mistral-7B-v0.3（5/6 downstream tasks 优势）、Qwen-2.5-14B（PPL 优势 + MMLU 反转），覆盖不同的 attention 机制（GQA、GQA+sliding window）和参数规模（7B-14B）。

---

## Weaknesses (逐条)

### Must-Fix

**W1. [Must-Fix] C1 消融 50% 稀疏度 max Δ 数值错误。**
- 具体位置：§4.4 第2段 + Table 2 caption
- 问题：论文声称 "max Δ=0.59pp at 50% (2-seed)"，但 Table 2 中 50% s42 的 WinoGrande 差异为 |63.14 − 62.35| = 0.79pp，超过声称的 0.59pp。ARC-c 差异 |32.17 − 32.59| = 0.42pp 也不等于 0.59pp。0.59pp 这个数字无法从 Table 2 中任何一列推导出来。
- 为什么影响接收：C1 消融是论文的核心 contribution 之一（"mask quality is the proximate driver"），支撑该 claim 的定量证据存在错误，直接削弱可信度。
- 建议：更正为实际 max Δ=0.79pp，并相应调整 Abstract 和 Introduction 中引用该数字的段落。

**W2. [Must-Fix] BCE+Compensation 在 Table 1 与 Table 3 之间存在不可调和的数值矛盾。**
- 具体位置：Table 1（"BCE + comp.∗"，50%，PPL 28.13±0.20）vs Table 3（"BCE + Compensation (hard mask)"，PPL 25.44）
- 问题：Table 1 标注 "∗BCE 50%: DejaVu/FastForward pipeline with compensation (67.2M params)"，3-seed 平均 PPL 28.13±0.20（std=0.20 意味着所有 seed 都在 27.93-28.33 范围内）。但 Table 3 的 BCE + Compensation（seed 42）PPL 为 25.44，远低于 Table 1 的 3-seed 范围。如果 Table 1 的 seed 42 也是 25.44，则 3-seed std 不可能是 0.20。如果两个 table 使用不同的训练配置（如不同的 step 数），论文必须明确说明。
- 为什么影响接收：§4.4 "Compensation Redundancy" 段引用 "BCE requires compensation (27.97→25.44)"，而 §4.3 用 28.13 作为 BCE 的 anchor number，两处基线数字不一致使得 "KL renders compensation redundant" 的 claim 定量基础不明。
- 建议：明确 Table 1 和 Table 3 中 BCE 条目的训练步数、seed、以及是否为同一实验配置。如果不同，在 caption 或正文中标注。

**W3. [Must-Fix] 缺少与 intermediate-coupling baseline 的实验对比。**
- 具体位置：§3.7 Table 1 (taxonomy) + §4
- 问题：论文提出 2D 分类法将方法分为 Decomposed/Intermediate/Coupled，自己占据 "Per-token × Coupled" 格子。但实验只对比了 Decomposed（BCE）和无预测器基线（TEAL），完全没有对比 Intermediate（MSE）方法。ShadowLLM（Per-token × Intermediate）和 D2DMoE（Per-token × Intermediate）都在 Related Work 中讨论，但没有实验数据。如果不对比 Intermediate 基线，分类法的核心 claim——"coupled 优于 intermediate 优于 decomposed"——缺乏实验支撑。
- 为什么影响接收：缺少直接竞争者的对比是 ARR reviewer 常见的高权重 concern（对应 R3: missing comparisons with relevant baselines）。
- 建议：至少对比 hidden-state MSE 目标（ShadowLLM 风格的逐层 MSE），使用相同的预测器架构和训练配置。如果无法重现 ShadowLLM 的完整 attention-based 路由，一个简化版的 per-layer MSE baseline 也足以验证分类法。

### Should-Fix

**W4. [Should-Fix] C1 消融的 soft-vs-hard confound 未被充分解决，"因果" 措辞过强。**
- 具体位置：§4.4 "Soft-vs-Hard Confound" 段 + "Causal Ablation" 标题
- 问题：C1 同时改变了两个变量：(a) 训练目标的梯度结构（BCE vs KL）和 (b) mask 表征（hard binary vs soft Gumbel-Sigmoid）。论文用 "BCE + Gumbel (no penalty) → PPL 32.22" 来论证 "softness alone does not explain KL's advantage"。但这个论证不充分：softness 伤害 BCE 不意味着 softness 不帮助 KL。Loss function 与 relaxation 之间可能存在交互效应。
- 论文自己也承认 "Disentangling target quality from gradient representation remains for future work"，但标题和行文仍使用 "Causal Ablation" 一词，暗示因果推断的严格性。
- 建议：(1) 将 "Causal Ablation" 改为更保守的 "Target-Swap Ablation" 或 "Interventional Ablation"；(2) 在讨论中明确 C1 的 confound 边界。

**W5. [Should-Fix] 跨架构结果（Mistral、Qwen）均为单 seed，统计效力不足。**
- 具体位置：Table 8（Mistral downstream）、Table 7（Qwen 14B）
- 问题：Mistral 和 Qwen 的所有结果均为 seed 42 单次运行，没有 std 报告。考虑到论文在 LLaMA 上展示了 MMLU 高达 9.5pp 的跨 seed 方差（Table 1, 30% global），单 seed 结果无法排除同样的变异。特别是 14B MMLU 反转（-8.1pp）可能仅仅是 seed 效应。
- 建议：至少对 Mistral 30% 和 Qwen 30% 各运行 3 seed，报告 mean±std。如果计算资源不允许，需在正文而非仅 Limitations 中明确注明跨架构结论的统计局限性。

**W6. [Should-Fix] 无实际 wall-clock 加速，系统增加 6.4% 开销。**
- 具体位置：§4.5 最后一段 + Appendix A
- 问题：当前实现使用非结构化逐元素 mask，实际增加 6.4% 推理延迟（Table 9）。论文明确承认 "actual speedup requires sparse kernel integration not addressed here"。对于一篇以推理效率为动机的论文，没有任何形式的加速演示是实质性缺陷。
- 与同类工作对比：DejaVu、FastForward、Polar Sparsity 均报告了端到端加速；TEAL 也展示了实际 throughput 提升。本文仅提供"预测质量"改进。
- 建议：在 Introduction 和 Conclusion 中更显著地下调效率 framing，或者提供 Triton block-sparse 的概念验证。如果选择前者，建议 reframe 为 "understanding how training objectives shape sparsity prediction quality" 而非 efficiency 方向。

**W7. [Should-Fix] 自适应惩罚控制器在 30% 目标下 λ 饱和且偏差 5%，主文未讨论。**
- 具体位置：Appendix B (Table 10) + §3.5
- 问题：30% 稀疏度目标下，λ 饱和在 cap（5000），实际训练稀疏度为 28.5%（偏差 5%）。虽然推理时 TEAL 的 top-k 保证精确 30% 稀疏度，但训练时的 1.5% 偏差意味着预测器在 28.5% 的操作点上被优化，推理时被强制到 30%。这个 train-test mismatch 可能导致次优的 mask 排名。
- Appendix B 讨论了这个问题但论证 "negligible relative to the KL vs. TEAL gap"，这不能替代在主文中报告。
- 建议：在 §4.1 或 §4.2 中添加一句话明确训练时实际稀疏度，并讨论 train-inference mismatch 的潜在影响。

### Minor

**W8. [Minor] Baselines 列表中包含 WINA 但无实验数据。**
- 具体位置：§4.1 Baselines 段
- 问题："(4) WINA [liu2025teal], an importance-weighted variant" 被列为 baseline，但所有实验 table 中均未出现 WINA 结果。
- 建议：添加 WINA 实验数据或从 baselines 列表中移除。

**W9. [Minor] "Phase transition" 术语使用过于宽松。**
- 具体位置：Abstract 第6句 + §4.5
- 问题：论文将 50% 稀疏度下 MMLU 从 ~38%（40%稀疏度）降至 ~28%（50%稀疏度）称为 "capacity phase transition"。但实际数据点仅有 5% 间隔的离散测量（Table 5），缺乏精细扫描来定位相变点。真正的 phase transition 应在 40%-50% 之间以 1-2% 为间隔扫描，展示 sharp boundary。
- 建议：改用 "capacity cliff" 或 "sharp degradation regime"，除非补充更精细的扫描数据。

**W10. [Minor] 梯度 SNR 测量在 step 300 而非收敛点（1000 步）。**
- 具体位置：§3.6 脚注 + Appendix F
- 问题：SNR 测量截止 step 300，但训练运行 1000 步。Appendix F 显示 SNR 轨迹是非单调的（BCE 在 steps 100-250 超过 KL），step 300 的 5.14× 优势可能不代表最终收敛状态。
- 建议：报告 step 1000 的 SNR，或在正文中明确 "step 300" 而非使用 "at convergence"。

**W11. [Minor] PPL 11.79 vs 11.80 小数不一致。**
- 具体位置：§4.5 "PPL 8.17 at 25% to 11.80 at 50%" vs Table 1 "11.79"
- 建议：统一。

---

## Questions (需要作者回答的)

**Q1.** Table 1 的 "BCE + comp.∗" (50%, PPL 28.13±0.20) 与 Table 3 的 "BCE + Compensation" (PPL 25.44) 使用相同的训练配置吗？如果不同（如 step 数不同），请明确两者的区别。

**Q2.** C1 消融 50% 的 max Δ 在 Table 2 中为 0.79pp (WG)，而非论文声称的 0.59pp。0.59pp 是如何计算的？

**Q3.** 30% 稀疏度训练时实际稀疏度为 28.5%（Appendix B），推理用 TEAL top-k 强制 30%。这个 1.5% 的 train-inference gap 是否被纳入超参数调优？即预测器是否在 30% 推理条件下被验证/选择的？

**Q4.** 论文声称 "gradient coupling remains necessary at the discovery stage"。如果对 BCE 在 magnitude-based masks 上训练 2700 步（iso-compute），然后用该 BCE 预测器的 scores 做 global top-k，PPL 是多少？这与 TEAL vanilla 的差距能解释多少 BCE 的劣势来自 mask target vs 学习效率？

**Q5.** Mistral 上 GSM8K 反转（KL 11.1% vs TEAL 15.9%）的机制假设是什么？论文提到 "reasoning tasks may require different optimization targets" 但没有进一步分析。Forward KL 的 mass-covering 性质是否导致稀疏模型在 mode-seeking 任务上表现不佳？

**Q6.** 14B 的 MMLU 反转是否在多 seed 下稳定？当前仅 seed 42 结果无法排除 variance。

---

## Missing References

- 无重大遗漏。引用覆盖了直接相关方法（TEAL、DejaVu、FastForward、ShadowLLM、D2DMoE、MaskLLM、SPON）、评测基准（WikiText、C4、MMLU 等）和理论基础（Gumbel-Sigmoid、KL distillation）。
- 47 篇引用，密度合理。
- `de2024griffin` 在 OpenAlex 中未验证到，但该论文真实存在（Google DeepMind, 2024），可能是 API 匹配问题，不影响引用质量。

---

## Detailed Comments (逐节)

### Abstract
- 信息密度高，四个必答问题均覆盖。
- "68% mask divergence" 来自 50% 稀疏度但未注明，而主要 PPL claim 在 30%，存在轻微误导。
- "capacity phase transition" 措辞过强（见 W9）。

### Introduction
- 从 BCE-vs-global-allocation mismatch 切入，逻辑清晰。
- 第2段梯度分析和第3段实验结果过于紧凑，读起来像 result listing 而非叙事推进。建议将数字密度降低，把部分数据移到 §4。
- Contribution list 的第3点 "non-monotonic allocation preference at 8B and scale-dependent effects at 14B" 在前文没有铺垫，突然出现。

### Related Work
- 结构清晰（Training-Free / Predictor-Based / Bias Correction / Activation Engineering / Weight Pruning / MoE Routing），覆盖全面。
- MaskLLM 的三点区分（sparsity type / mask generation / allocation）写得好，避免了审稿人提出 "how is this different from MaskLLM" 的问题。
- 建议：D2DMoE 和 ShadowLLM 的区分可以更精确，目前只说 "intermediate coupling" 但没有量化 intermediate vs coupled 的差距。

### Method (§3)
- §3.3 Gumbel-Sigmoid 松弛：公式和描述清晰。STE 对比段的 "discontinuous gradient signals" 描述过于绝对——STE 在量化等场景广泛使用且效果不差。建议改为 "in our setting, STE produces..."（实际上已经是这样写的，OK）。
- §3.5 自适应惩罚控制器：脚注诚实地区分了与正式 augmented Lagrangian 的区别。但缺少收敛性质讨论——几何加倍是否保证在有限步内达到目标？当 λ 饱和在 cap 时（如 30% 目标），5% 偏差是否可接受？
- §3.6 梯度分析：论文正确标注 "This analysis is suggestive"。但行文中 "reveals a structural asymmetry" 的用词仍暗示了强于 "suggestive" 的结论。

### Experiments (§4)
- 总体实验量充足，覆盖 perplexity + 6 个 downstream tasks + 3 个 model + 2 种 allocation + 多个 sparsity level。
- Table 1 结构清晰，caption 解释充分。
- §4.3（Extended Training Analysis）的 iso-compute 对比有说服力。
- §4.5（Regime Analysis）的三段式分析（budget-surplus / budget-constrained / capacity-limited）是论文的一个 highlight。

### Conclusion
- 过于简短（2句话），没有讨论 future work 或 broader impact。建议至少补充 1-2 句关于 N:M 结构化稀疏或更大规模的展望。

### Limitations
- 覆盖全面（PPL-vs-downstream gap、训练成本、GSM8K 反转、OOD 泛化、C1 confound、seed variance、wall-clock speedup）。
- "30% appears to be the best-quality sparsity level for downstream fidelity" 的自我评估是诚实的。

---

## Overall Assessment

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 核心方法论正确，但 C1 max Δ 数值错误（0.59 vs 实际 0.79）和 Table 1/3 BCE 数据矛盾削弱信任。梯度分析被正确标注为 suggestive，但 "causal ablation" 措辞过强。 |
| Excitement | 3.0/5 | KL 发现完全不同的 mask pattern（68% divergence）且性能更优，这个发现本身有趣。但缺乏实际加速、规模限于 14B、contribution 偏增量（替换 loss function）。 |
| Reproducibility | 4/5 | 超参数、seed、GPU 型号、训练步数均有报告。未释放代码但方法描述足够详细。 |
| Overall Assessment | **3.0** (Findings) | |
| Confidence | 4/5 | 仔细阅读了全文和 appendix，逐项验证了数字。对 gradient analysis 的数学部分有合理信心，但未手动推导完整 Jacobian。 |

**一句话总结**：论文提出了一个合理且有趣的实证研究方向（KL 替代 BCE 训练稀疏预测器），实验设计总体扎实，但数据不一致（W1、W2）、缺少 intermediate-coupling baseline（W3）和无实际加速（W6）将其定位为 Findings 水平。

**推荐**：Findings（修复 W1-W3 后）。当前状态为 Borderline Findings (2.5-3.0)，因为数据错误直接影响核心 claim 的可信度。修复后可稳定在 3.0。

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

_source line 1006 · 2026-05-19T07:59:03.457230+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（引用具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的完整审稿意见\n\n**Summary**: 本文提出用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器，核心发现是 KL 的耦合梯度能发现与激活幅值差异 68% 的神经元重要性模式，且因果消融（C1）证实这些 mask target 是推理质量的近因驱动力。在 LLaMA-3.1-8B 上 30% 稀疏度下 PPL 降低 18%（8.96 vs 10.97），并使补偿网络（+67.2M 参数）变得冗余；但方法在 14B 上出现 MMLU 逆转（-8.1pp），且未实现任何 wall-clock 加速。\n\n**Strengths**:\nS1. 问题定义清晰且有洞察力。BCE 逐神经元训练与 TEAL 全局 top-k 推理分配之间的 mismatch 是真实问题。\nS2. C1 因果消融设计巧妙（50% max Δ=0.59pp），mask quality vs gradient coupling 解耦。\nS3. 消融实验系统且覆盖面广（Table 4）。\nS4. 跨架构评估诚实，含负面结果（14B MMLU、GSM8K 反转）。\nS5. 写作质量高，无明显 AI 痕迹。\nS6. Taxonomy（Table 1）定位准确。\nS7. 超参数鲁棒性充分。\n\n**Weaknesses**:\n\nN1. [Must-Fix] 新颖性有限：核心贡献是 loss function 替换，与 MaskLLM 技术距离较小。MaskLLM 已实现 frozen weights + learnable masks + KL + Gumbel 组合。Per-token × Coupled 是自然组合，不构成足够新颖性。建议强化 C1 ablation 贡献，定位为 empirical study。\n\nN2. [Must-Fix] 未实现 wall-clock 加速，当前增加 6.4% 开销。Abstract 中 \"renders compensation redundant\" 让读者期望加速但未交付。\n\nN3. [Must-Fix] 14B MMLU 逆转 -8.1pp 动摇可扩展性。§4.6 的 layer-wise probing 假设未验证。从 7B→14B 就出现逆转对 70B 前景堪忧。\n\nW1. [Should-Fix] 30% 全局分配 MMLU 种子方差极高（σ=9.5pp），未提解决方案。\nW2. [Should-Fix] C1 soft-vs-hard confound：BCE+Gumbel 失败不证明 softness 不重要。\nW3. [Should-Fix] WikiText-103→WikiText-2 同源，C4 OOD gap 更大（1.74× vs 1.46×）。\nW4. [Should-Fix] 30% \"best quality\" 下 GSM8K 仍 84% 退化，downstream 讨论不足。\nW5. [Should-Fix] Conclusion 仅两句话过于简短。\nW6. [Should-Fix] \"68% divergence\" 在 Introduction 中重复三次。\n\nM1-M7: 语法、exp_id 注释清理、HellaSwag/PIQA 未在 §4.1 提及、s42† checkpoint 解释不足、SwiGLU 未在 Abstract 定义、§2.5 篇幅过长、Figure 1 信息密度存疑。\n\n**Questions**: Q1-Q5 涉及 14B 多 seed、KL-only 神经元贡献验证、GSM8K 反转机制、28.5% 训练偏差、C4 训练可能性。\n\n**Missing References**: LLM.int8()、Sparse Fine-Tuning。\n\n**Overall**: Score 3.0 (Findings), Confidence 4/5。\n\n---\n\n请对以上每个 Weakness（N1-N3, W1-W6, M1-M7）和 Questions（Q1-Q5）逐条回应 [AGREE] 或 [REBUT]。"
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
    "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（引用具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的完整审稿意见\n\n**Summary**: 本文提出用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器，核心发现是 KL 的耦合梯度能发现与激活幅值差异 68% 的神经元重要性模式，且因果消融（C1）证实这些 mask target 是推理质量的近因驱动力。在 LLaMA-3.1-8B 上 30% 稀疏度下 PPL 降低 18%（8.96 vs 10.97），并使补偿网络（+67.2M 参数）变得冗余；但方法在 14B 上出现 MMLU 逆转（-8.1pp），且未实现任何 wall-clock 加速。\n\n**Strengths**:\nS1. 问题定义清晰且有洞察力。BCE 逐神经元训练与 TEAL 全局 top-k 推理分配之间的 mismatch 是真实问题。\nS2. C1 因果消融设计巧妙（50% max Δ=0.59pp），mask quality vs gradient coupling 解耦。\nS3. 消融实验系统且覆盖面广（Table 4）。\nS4. 跨架构评估诚实，含负面结果（14B MMLU、GSM8K 反转）。\nS5. 写作质量高，无明显 AI 痕迹。\nS6. Taxonomy（Table 1）定位准确。\nS7. 超参数鲁棒性充分。\n\n**Weaknesses**:\n\nN1. [Must-Fix] 新颖性有限：核心贡献是 loss function 替换，与 MaskLLM 技术距离较小。MaskLLM 已实现 frozen weights + learnable masks + KL + Gumbel 组合。Per-token × Coupled 是自然组合，不构成足够新颖性。建议强化 C1 ablation 贡献，定位为 empirical study。\n\nN2. [Must-Fix] 未实现 wall-clock 加速，当前增加 6.4% 开销。Abstract 中 \"renders compensation redundant\" 让读者期望加速但未交付。\n\nN3. [Must-Fix] 14B MMLU 逆转 -8.1pp 动摇可扩展性。§4.6 的 layer-wise probing 假设未验证。从 7B→14B 就出现逆转对 70B 前景堪忧。\n\nW1. [Should-Fix] 30% 全局分配 MMLU 种子方差极高（σ=9.5pp），未提解决方案。\nW2. [Should-Fix] C1 soft-vs-hard confound：BCE+Gumbel 失败不证明 softness 不重要。\nW3. [Should-Fix] WikiText-103→WikiText-2 同源，C4 OOD gap 更大（1.74× vs 1.46×）。\nW4. [Should-Fix] 30% \"best quality\" 下 GSM8K 仍 84% 退化，downstream 讨论不足。\nW5. [Should-Fix] Conclusion 仅两句话过于简短。\nW6. [Should-Fix] \"68% divergence\" 在 Introduction 中重复三次。\n\nM1-M7: 语法、exp_id 注释清理、HellaSwag/PIQA 未在 §4.1 提及、s42† checkpoint 解释不足、SwiGLU 未在 Abstract 定义、§2.5 篇幅过长、Figure 1 信息密度存疑。\n\n**Questions**: Q1-Q5 涉及 14B 多 seed、KL-only 神经元贡献验证、GSM8K 反转机制、28.5% 训练偏差、C4 训练可能性。\n\n**Missing References**: LLM.int8()、Sparse Fine-Tuning。\n\n**Overall**: Score 3.0 (Findings), Confidence 4/5。\n\n---\n\n请对以上每个 Weakness（N1-N3, W1-W6, M1-M7）和 Questions（Q1-Q5）逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1007 · 2026-05-19T07:59:23.480597+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20023
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-19T07:59:25.908234+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（引用具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的完整审稿意见\n\n**Summary**: 本文用 forward KL 散度替代 BCE 训练 SwiGLU LLM 稀疏预测器，Gumbel-Sigmoid 松弛实现端到端可微。LLaMA-3.1-8B 上 30% PPL 降 18%，补偿网络冗余。系统消融和跨架构验证（Mistral-7B、Qwen-14B），但存在数据不一致、因果声明过度和缺乏实际加速。\n\n**Strengths**:\nS1. 问题定义清晰。S2. 消融设计全面（Table 3）。S3. 诚实报告负面结果。S4. C1 因果消融创造性。S5. 超参数鲁棒性。S6. 跨架构 3 种模型。\n\n**Weaknesses**:\n\nW1. [Must-Fix] C1 消融 50% max Δ 数值错误：论文声称 0.59pp，但 Table 2 中 WG 差异 |63.14−62.35|=0.79pp，超过声称值。核心 claim 的定量证据存在错误。\n\nW2. [Must-Fix] BCE+Compensation 在 Table 1（PPL 28.13±0.20）与 Table 3（PPL 25.44）存在不可调和矛盾。Table 1 是 3-seed 均值（std=0.20 意味所有 seed 在 27.93-28.33 范围），但 Table 3 seed 42 为 25.44，远低于此范围。两个表格的 BCE 基线不一致。\n\nW3. [Must-Fix] 缺少 intermediate-coupling baseline（MSE）实验对比。Taxonomy 声称 Coupled > Intermediate > Decomposed，但只对比了 Decomposed（BCE）和无预测器基线（TEAL），没有 MSE baseline。ShadowLLM、D2DMoE 均讨论但无数据。\n\nW4. [Should-Fix] C1 soft-vs-hard confound 未充分解决，\"Causal Ablation\" 措辞过强。建议改为 \"Target-Swap Ablation\"。\n\nW5. [Should-Fix] 跨架构结果（Mistral、Qwen）均单 seed，统计效力不足。14B MMLU 反转可能仅为 seed 效应。\n\nW6. [Should-Fix] 无 wall-clock 加速，反增 6.4% 开销。DejaVu/FastForward/Polar Sparsity/TEAL 均报告了实际加速。\n\nW7. [Should-Fix] 30% λ 饱和且偏差 5%（实际 28.5%），train-test mismatch 未在主文讨论。\n\nW8. [Minor] WINA 列为 baseline 但无实验数据。\nW9. [Minor] \"Phase transition\" 术语过于宽松，缺精细扫描。\nW10. [Minor] SNR 在 step 300 而非收敛点测量，用 \"at convergence\" 措辞不当。\nW11. [Minor] PPL 11.79 vs 11.80 小数不一致。\n\n**Questions**: Q1（Table 1/3 BCE 配置差异）、Q2（C1 50% max Δ 计算来源）、Q3（28.5% 训练偏差是否纳入调优）、Q4（BCE 2700步 + global top-k 结果）、Q5（Mistral GSM8K 反转机制）、Q6（14B 多 seed 稳定性）。\n\n**Missing References**: 无重大遗漏。47 篇引用密度合理。\n\n**Overall**: Score 3.0 (Findings), Confidence 4/5。修复 W1-W3 后可稳定 3.0。当前为 Borderline Findings (2.5-3.0)。\n\n---\n\n请对以上每个 Weakness（W1-W11）和 Questions（Q1-Q6）逐条回应 [AGREE] 或 [REBUT]。"
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
    "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（引用具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的完整审稿意见\n\n**Summary**: 本文用 forward KL 散度替代 BCE 训练 SwiGLU LLM 稀疏预测器，Gumbel-Sigmoid 松弛实现端到端可微。LLaMA-3.1-8B 上 30% PPL 降 18%，补偿网络冗余。系统消融和跨架构验证（Mistral-7B、Qwen-14B），但存在数据不一致、因果声明过度和缺乏实际加速。\n\n**Strengths**:\nS1. 问题定义清晰。S2. 消融设计全面（Table 3）。S3. 诚实报告负面结果。S4. C1 因果消融创造性。S5. 超参数鲁棒性。S6. 跨架构 3 种模型。\n\n**Weaknesses**:\n\nW1. [Must-Fix] C1 消融 50% max Δ 数值错误：论文声称 0.59pp，但 Table 2 中 WG 差异 |63.14−62.35|=0.79pp，超过声称值。核心 claim 的定量证据存在错误。\n\nW2. [Must-Fix] BCE+Compensation 在 Table 1（PPL 28.13±0.20）与 Table 3（PPL 25.44）存在不可调和矛盾。Table 1 是 3-seed 均值（std=0.20 意味所有 seed 在 27.93-28.33 范围），但 Table 3 seed 42 为 25.44，远低于此范围。两个表格的 BCE 基线不一致。\n\nW3. [Must-Fix] 缺少 intermediate-coupling baseline（MSE）实验对比。Taxonomy 声称 Coupled > Intermediate > Decomposed，但只对比了 Decomposed（BCE）和无预测器基线（TEAL），没有 MSE baseline。ShadowLLM、D2DMoE 均讨论但无数据。\n\nW4. [Should-Fix] C1 soft-vs-hard confound 未充分解决，\"Causal Ablation\" 措辞过强。建议改为 \"Target-Swap Ablation\"。\n\nW5. [Should-Fix] 跨架构结果（Mistral、Qwen）均单 seed，统计效力不足。14B MMLU 反转可能仅为 seed 效应。\n\nW6. [Should-Fix] 无 wall-clock 加速，反增 6.4% 开销。DejaVu/FastForward/Polar Sparsity/TEAL 均报告了实际加速。\n\nW7. [Should-Fix] 30% λ 饱和且偏差 5%（实际 28.5%），train-test mismatch 未在主文讨论。\n\nW8. [Minor] WINA 列为 baseline 但无实验数据。\nW9. [Minor] \"Phase transition\" 术语过于宽松，缺精细扫描。\nW10. [Minor] SNR 在 step 300 而非收敛点测量，用 \"at convergence\" 措辞不当。\nW11. [Minor] PPL 11.79 vs 11.80 小数不一致。\n\n**Questions**: Q1（Table 1/3 BCE 配置差异）、Q2（C1 50% max Δ 计算来源）、Q3（28.5% 训练偏差是否纳入调优）、Q4（BCE 2700步 + global top-k 结果）、Q5（Mistral GSM8K 反转机制）、Q6（14B 多 seed 稳定性）。\n\n**Missing References**: 无重大遗漏。47 篇引用密度合理。\n\n**Overall**: Score 3.0 (Findings), Confidence 4/5。修复 W1-W3 后可稳定 3.0。当前为 Borderline Findings (2.5-3.0)。\n\n---\n\n请对以上每个 Weakness（W1-W11）和 Questions（Q1-Q6）逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-19T07:59:27.520163+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1611
}
```

</details>

---


### Assistant

_source line 1010 · 2026-05-19T07:59:30.255337+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 80

## Round 80

2 recorded events


### User

_source line 1011 · 2026-05-19T07:59:32.977497+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心发现：

1. **数据错误**：C1 消融 50% 的 max Δ 论文声称 0.59pp，实际从 Table 2 计算为 0.79pp（WG 列）。
2. **数据矛盾**：BCE+Compensation 在 Table 1（28.13±0.20）与 Table 3（25.44）之间不一致，无法用 seed 方差解释。
3. **缺少关键 baseline**：论文提出 Decomposed/Intermediate/Coupled 分类法，但完全没有对比 Intermediate（MSE）方法。
4. **C1 "因果消融" 措辞过强**：存在 soft-vs-hard confound，论文自己承认未解决但仍用 "causal" 标题。
5. **无实际加速**：系统增加 6.4% 延迟，没有任何 wall-clock speedup 演示。

评分：**Overall 3.0（Findings）**，Soundness 3.0/5，Excitement 3.0/5。修复 W1-W3 后可稳定 Findings；当前因数据错误在 Borderline Findings 边缘。

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

_source line 1012 · 2026-05-19T07:59:39.043998+00:00_

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


## Round 81

## Round 81

2 recorded events


### User

_source line 1013 · 2026-05-19T08:01:31.159467+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 Round 1 意见的逐条回应

---

### Strengths

**[AGREE] S1-S5, S7.** 与我的评估一致。

**[REBUT] S2.** R2 接受了 "50% max Δ=0.59pp" 这个数字，但该数字有误。Table 2 中 50% s42 的 WinoGrande 差异为 |63.14 − 62.35| = 0.79pp，超过论文声称的 0.59pp。我在 Round 1 中已将此标记为 W1 [Must-Fix]。C1 设计本身确实巧妙，但支撑 claim 的定量证据存在错误，R2 不应未经验证就接受。

**[AGREE with caveat] S6.** Taxonomy 定位准确是事实，但如果没有 Intermediate（MSE）baseline 的实验对比，taxonomy 的价值仅限于概念组织，不能支撑 "coupled > intermediate > decomposed" 的隐含主张。我在 Round 1 W3 中标记此问题为 [Must-Fix]。

---

### Must-Fix Weaknesses

**[REBUT] N1. "新颖性有限，与 MaskLLM 技术距离较小"**

R2 低估了两个方法之间的结构性差异。论文 §2 Related Work 明确列出三个关键区别：
1. **Sparsity type**: MaskLLM 做 N:M weight sparsity（静态 2:4 pattern），本文做 activation sparsity（动态 per-token mask）。这不是微调而是根本不同的问题设定——weight mask 训练后固定，activation mask 每 token 变化。
2. **Mask generation**: MaskLLM 的 mask 是直接可学参数（每个 weight group 一个），通过 Gumbel-Softmax 从离散集合中选择；本文训练一个 predictor network（75.9M params），从 hidden state 推断 mask。一个是 look-up，另一个是 function approximation。
3. **Allocation**: MaskLLM 在固定 N:M group 内优化，无跨 group 竞争；本文的 mask 在全局 top-k budget 下排名，所有层的所有神经元相互竞争。这个全局竞争正是 inter-neuron coupling 的动机。

"frozen weights + learnable masks + KL + Gumbel" 是对两个方法的过度抽象。用同样的逻辑，所有用 Transformer 的方法都 "技术距离较小"。

**但我部分同意**：论文的方法论新颖性确实是增量的（替换 loss function + 标准松弛技术）。论文的真正贡献在于实证发现（mask divergence、C1 ablation、compensation redundancy、allocation regime analysis），而非方法本身。论文已经在 §1 和 §2 中将自己定位为 "primarily empirical"，这个定位是恰当的。建议作者进一步强化 empirical contribution framing，弱化 method novelty 的暗示。

**[AGREE] N2. "未实现 wall-clock 加速"**

完全同意。这在我的 Round 1 也是 W6 [Should-Fix]（我将其定为 Should-Fix 是因为论文已在 §1 最后一段和 Appendix A 中明确承认此局限）。但 R2 指出 Abstract 中 "renders compensation redundant" 确实会误导读者期望加速——redundancy 在参数和 PPL 层面成立，但在 latency 层面只节省了 ~2.7% 开销（Appendix A: 126.78ms vs 129.71ms）。建议 Abstract 改为 "renders compensation redundant in prediction quality" 以避免歧义。

**[AGREE with nuance] N3. "14B MMLU 逆转 -8.1pp 动摇可扩展性"**

同意这是严重 concern。我在 Round 1 W5 中也指出 14B 结果为单 seed，统计效力不足。但需要区分两个层面：

1. **事实层面**：14B 上 PPL 优势确实泛化（KL 7.62 vs TEAL 8.73，Table 7）。MMLU 反转是任务特异性的，不是全面失败——ARC-c 和 WG 差距很小（Table 7: ARC KL 57.17 vs TEAL 56.83，WG KL 72.06 vs TEAL 72.69）。

2. **解释层面**：§4.6 提出了 "per-layer mask divergence 结构差异" 假设（14B variance 2.4× that of 8B），这是一个合理的 starting hypothesis。论文诚实地写 "Verification requires layer-wise probing beyond our current scope" 而不是编造解释。

R2 说 "从 7B→14B 就出现逆转对 70B 前景堪忧" 是合理推断，但也可能 14B 是特殊情况（Qwen-2.5 的 architecture/tokenizer/pretraining 与 LLaMA 系列差异大）。**至少需要 3-seed 确认 14B 反转的稳定性后才能下定论。**

---

### Should-Fix Weaknesses

**[AGREE] W1. "30% 全局分配 MMLU 种子方差极高（σ=9.5pp）"**

同意。论文报告了问题但未提解决方案。Table 5 显示 uniform allocation 将 MMLU σ 降到 1.3pp（7.5× smaller），这本身就是一个解决方案的线索。论文可以更明确地推荐 uniform allocation 作为 30% 稀疏度的默认策略，而不仅仅是报告两种策略的对比。

**[AGREE] W2. "C1 soft-vs-hard confound"**

完全同意。这与我 Round 1 W4 一致。论文用 "BCE+Gumbel 失败" 反驳 "softness 解释 KL 优势"，但逻辑不成立：softness 与 BCE 的交互效应负面，不意味着 softness 与 KL 的交互效应也负面。Loss function 和 relaxation method 之间可能存在 interaction effect，单独测试一个因素无法推断联合效应。

**[AGREE] W3. "WikiText-103→WikiText-2 同源"**

同意。我在 Round 1 也注意到了这个问题。C4 OOD 评估缓解了部分担忧，但 1.74× vs 1.46× 的 gap 表明 predictor 确实对训练域有 partial overfitting。论文 Limitations 中承认了这一点。

**[AGREE] W4. "30% GSM8K 仍 84% 退化"**

同意且补充数据：Dense GSM8K = 48.75%，KL 30% uniform = 7.5±0.1%（Table 1），退化 = (48.75-7.5)/48.75 = 84.6%。KL 30% global = 8.0±0.7%，退化 = 83.6%。TEAL 30% = 7.88%，退化 = 83.8%。所有方法在 GSM8K 上退化程度相近，说明这是 30% 稀疏度对 reasoning 任务的固有限制，不是 KL 的特有问题。但论文确实应讨论这意味着 30% 可能不是 "best quality" 对所有任务类型都成立。

**[AGREE] W5. "Conclusion 仅两句话过于简短"**

同意。我在 Round 1 Detailed Comments 中也指出了这一点。至少应补充 future work 方向（N:M 结构化稀疏、更大规模验证）。

**[REBUT partial] W6. "'68% divergence' 在 Introduction 中重复三次"**

R2 声称 Introduction 中重复三次。实际检查 Introduction 全文：
1. ¶2: "KL's coupled gradients discover neuron importance patterns that diverge 68% from magnitude-based masks (per-layer Jaccard 32%)" — 首次出现，引入核心发现
2. ¶3: 讨论 C1 ablation，提到 "max Δ=0.59pp" 但**未重复 68%**
3. Contribution item 1: "KL's coupled gradients discover neuron importance patterns diverging 68% from magnitude-based masks" — 第二次出现

加上 Abstract 的一次，total = 3 次（Abstract 1次 + Introduction 2次），其中 Introduction 内部为 2 次，非 3 次。¶2 是叙事引入，Contribution list 是结构化总结，功能不同。但同意有轻微冗余感，建议 Contribution list 改用 "the discovered mask patterns (§4.3)" 指代而不重复数字。

---

### Minor Issues (M1-M7)

**[AGREE] M1-M7 全部同意。** 这些都是合理的写作/编辑问题，不影响技术判断。特别是：
- **M4 (s42† checkpoint 解释不足)**: 这与我 Round 1 对 C1 30% s42 pair 的 concern 一致——使用不同 oracle checkpoint 导致 max 7.85pp variation (ARC-c)，严重弱化 s42 数据的可用性。
- **M3 (HellaSwag/PIQA 未在 §4.1 提及)**: Introduction 引用了这些结果但 Evaluation 段未列出，读者无法找到对应的评估协议。

---

### Questions

**[AGREE] Q1 (14B 多 seed):** 与我 Round 1 Q6 一致。这是验证 14B MMLU 反转稳定性的最低要求。

**[AGREE] Q2 (KL-only 神经元贡献验证):** 有价值的问题。检查 KL 选择但 magnitude 不选择的神经元是否确实对 output distribution 有较大贡献，可以直接验证 "KL 发现了不同的重要性模式" 这个 claim。

**[AGREE] Q3 (GSM8K 反转机制):** 与我 Round 1 Q5 一致。Forward KL 的 mass-covering 性质是否在 reasoning 任务上不如 mode-seeking 策略，是一个值得分析的问题。

**[AGREE] Q4 (28.5% 训练偏差):** 与我 Round 1 W7 和 Q3 一致。训练时 28.5%、推理时 30% 的 gap 需要在主文讨论。

**[AGREE] Q5 (C4 训练可能性):** 合理的建议。如果 predictor 在 C4 上训练、WikiText-2 上评估，可以直接检验 OOD 泛化方向是否可逆。

---

### Missing References

**[REBUT partial]** R2 建议引用 LLM.int8() 和 Sparse Fine-Tuning：
- **LLM.int8() (Dettmers et al., 2022):** 这是量化方法，不是 activation sparsity 方法。论文的 scope 是 activation sparsity prediction，不涉及量化。除非 R2 的意图是讨论 sparsity + quantization 交互（如 Wang et al. 2025 [wang2025dynamicsparse] 已被引用），否则 LLM.int8() 不属于 missing reference。
- **Sparse Fine-Tuning:** R2 未指定具体论文，无法判断。如果指 SparseLoRA (Khaki et al., 2025)，已被引用。如果指其他工作，需要 R2 提供具体引用。

---

### Overall Assessment 对比

| | R1 (我) | R2 |
|---|---|---|
| Soundness | 3.0/5 | 未单独打分 |
| Excitement | 3.0/5 | 未单独打分 |
| Overall | 3.0 (Findings) | 3.0 (Findings) |
| Confidence | 4/5 | 4/5 |

**两位 Reviewer 在 Overall 评分上一致（3.0 Findings）。**

**关键分歧：**
1. **N1 (新颖性):** R2 认为新颖性不足是 Must-Fix，我认为论文已正确定位为 empirical study，新颖性限制是固有属性而非写作缺陷。建议作者进一步强化 empirical framing 但不认为需要 Must-Fix 级别的改动。
2. **W3 (MSE baseline):** 我将缺少 intermediate-coupling baseline 定为 Must-Fix (我的 W3)，R2 未明确提出这一点。这是两份 review 最大的差异——R2 接受了 taxonomy 但没有要求实验验证 taxonomy 中的 gap。
3. **数据错误:** R2 未发现 C1 50% max Δ 的数值错误（0.59pp vs 实际 0.79pp），也未发现 Table 1 vs Table 3 的 BCE+comp 数据矛盾。这两个问题是我认为最影响可信度的发现。

**综合建议给 Director：**
- 数据错误（C1 max Δ、Table 1/3 矛盾）必须修复后才能定稿
- 缺少 MSE intermediate baseline 是最大的实验空白
- 14B 至少需要 3-seed 确认
- 论文定位为 Findings 是合理的，当前状态 2.5-3.0，修复后可稳定在 3.0

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

_source line 1014 · 2026-05-19T08:01:40.216982+00:00_

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


## Round 82

## Round 82

2 recorded events


### User

_source line 1015 · 2026-05-19T08:01:43.047139+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Director。

核心结论：
- 与 R2 在 Overall 3.0 (Findings) 上一致
- 对 R2 的 N1（MaskLLM 距离近）进行了部分反驳——两方法存在结构性差异但技术新颖性确实有限
- 指出 R2 未发现的两个数据错误：C1 50% max Δ 实为 0.79pp（非 0.59pp）、Table 1/3 BCE+comp 数值矛盾
- 补充了 R2 遗漏的关键 concern：缺少 intermediate-coupling (MSE) baseline 的实验对比，这是 taxonomy claim 的实验空白

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

_source line 1016 · 2026-05-19T08:02:01.882371+00:00_

R1 交叉回应已收到。等待 R2 对 R1 意见的交叉回应到达后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 83

## Round 83

6 recorded events


### User

_source line 1017 · 2026-05-19T08:03:00.140762+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 的逐条交叉回应

---

## Strengths 回应

[AGREE] S1-S6: 与 R1 对 Strengths 的评估完全一致。这些与我自己 Round 1 审稿中识别的 S1-S7 高度重叠。不再赘述。

---

## Weaknesses 逐条回应

### W1. C1 消融 50% max Δ 数值错误（0.59pp vs 实际 0.79pp）

**[AGREE] R1-W1: 数值确实有误，但严重性可降级。**

核实 Table 3 数据：50% s42 的 WG |63.14−62.35|=0.79pp，确实超过论文声称的 max Δ=0.59pp。论文 caption 写 "max Δ=0.59pp at 50% (2-seed)"，但表格只展示了 1 个 seed pair（s42），第二个 seed 的数据未在表格中呈现。这有两个问题：(1) 可见数据中 max Δ=0.79pp≠0.59pp；(2) "2-seed" 声称但只展示 1 seed 的数据。

不过，0.79pp 仍然是很小的差异（WG 精度范围内），不影响 C1 ablation 的核心结论（C1 ≈ KL，magnitude-BCE 差 2.4×）。建议将此定为 **数据勘误** 而非方法论缺陷。但作为核心 claim 的数值支撑出错，仍然需要修正。

### W2. BCE+Compensation PPL 不一致（Table 2: 28.13±0.20 vs Table 4: 25.44）

**[AGREE] R1-W2: 这是一个严重的数据一致性问题，我的独立审查也发现了矛盾。**

详细核实：
- Table 2: "BCE + comp.$^\ast$" → PPL 28.13±0.20 (3-seed)。脚注：DejaVu/FastForward pipeline with compensation (67.2M params)。exp_id: `bce50_3seed`
- Table 4: "BCE + Compensation (hard mask)" → PPL 25.44。exp_id: `bce_comp_staged_s42`
- §4.5: "BCE requires compensation (27.97→25.44)" — 明确说明 compensation 将 PPL 从 27.97 降到 25.44

矛盾：如果 Table 2 的 28.13±0.20 确实包含 compensation（如脚注所述），那么 seed 42 应接近 25.44 而非 ~28.13。std=0.20 意味着三个 seed 都在 27.93-28.33 范围内，与 25.44 相差 2.69pp。

最可能的解释：Table 2 的 "BCE + comp.$^\ast$" 实际上是 **BCE without compensation**（2700 步扩展训练），脚注标注错误。§4.3 的表述 "The BCE predictor achieves PPL 28.13±0.20 (3-seed)" 也支持这一推断——这里说的是"BCE predictor"而不是"BCE + compensation"。

这是一个影响审稿信任度的错误：读者无法确定哪个数字是真实的 BCE+compensation baseline。R1 的 Must-Fix 定级合理。

### W3. 缺少 MSE intermediate-coupling baseline

**[AGREE] R1-W3: Taxonomy 的核心主张缺乏中间级别的实验验证。**

Table 1 的 taxonomy 明确划分三个 coupling 级别（Decomposed/Intermediate/Coupled），暗示 Coupled > Intermediate > Decomposed 的递进关系。但实验只对比了两端（BCE=Decomposed, KL=Coupled），完全跳过了 Intermediate（MSE on hidden states）。

我在自己的审稿中虽未将此列为独立 weakness，但这确实是 taxonomy claim 的一个实验空白。即使不实现完整的 ShadowLLM/D2DMoE pipeline，一个简单的 per-layer MSE 目标（最小化 sparse 与 dense 隐藏状态的 MSE）也应该测试，以验证 taxonomy 中的递进关系。

不过，我认为这不影响论文的核心 claim（KL > BCE），而是影响 taxonomy 的完整性。建议 **Should-Fix**（R1 定为 Must-Fix 稍显严格）。

### W4. C1 soft-vs-hard confound，"Causal Ablation" 命名过强

**[AGREE] R1-W4: 与我自己审稿中的 W2 一致。**

"Causal ablation" 暗示完全的因果推断，但实验同时改变了两个变量（gradient coupling + mask representation）。§4.4 的 soft-vs-hard confound 段尝试用 BCE+Gumbel 的失败来反证，但论证不完整（我在 Round 1 中已详述）。"Target-Swap Ablation" 或 "Target Transfer Experiment" 是更准确的命名。

### W5. 跨架构单 seed 统计效力不足

**[AGREE] R1-W5: 与我自己审稿中的 N3（14B 部分）和 Q1 一致。**

Mistral-7B 和 Qwen-14B 结果均为 seed 42 单次运行。14B MMLU 逆转（-8.1pp）尤其需要多 seed 验证——如果这仅是 seed 效应，则论文的 scalability concern 被过度放大；如果多 seed 一致逆转，则问题更严重。无论哪种结果，单 seed 都不足以支撑当前的结论。

### W6. 无 wall-clock 加速

**[AGREE] R1-W6: 与我自己审稿中的 N2 完全一致。**

补充一点：R1 提到 DejaVu/FastForward/Polar Sparsity/TEAL 均报告了实际加速——这是一个重要的 framing 问题。本文的 related work 对比了这些方法，但在加速维度上完全缺席，会让审稿人质疑"如果不加速，为什么要用 predictor？"。论文的 contribution statement 需要更明确地限定为 quality analysis。

### W7. 30% λ 饱和且偏差 5%

**[AGREE] R1-W7: 但程度上我认为这是 Should-Fix 而非 Must-Fix。**

Appendix C 已经做了 TEAL@28.5% vs TEAL@30% 的对比（PPL 10.30 vs 10.97），论证 0.67 PPL 差异相对于 KL 优势（8.96 vs 10.97 = 2.01 PPL）是可忽略的。这个 defense 是合理的，但 R1 正确指出应在主文而非仅在附录中讨论。

此外，R1 提出的一个隐含问题是：如果 KL predictor 实际在 28.5% 稀疏度下运行，那么与 TEAL 在 30% 下的对比不是 apple-to-apple 的。严格来说，应该对比 KL@28.5% vs TEAL@28.5%（而非 TEAL@30%）。Appendix 已提供 TEAL@28.5% = 10.30 的数据，KL@(实际28.5%) = 8.96，差异仍然显著（13.0% improvement），但比宣称的 18% 要小。

### W8. WINA 列为 baseline 但无实验数据

**[AGREE] R1-W8: Minor 但确实是写作疏忽。**

§4.1 Baselines 段列出 "(4) WINA~\cite{liu2025teal}, an importance-weighted variant"，但 Table 2 中无 WINA 行。要么移除 WINA 的 baseline 提及，要么补充数据。

### W9. "Phase transition" 术语过于宽松

**[AGREE] R1-W9: 同意这不是严格的 phase transition。**

论文在 Abstract 中用 "capacity phase transition" 描述 50% 下游 collapse，但 Figure 2 显示 PPL 是连续单调上升的。"Phase transition" 在物理学中意味着某个 order parameter 的不连续变化或分歧，但这里的 MMLU 退化是渐进的（30% 40.7% → 50% 28.0%）。"Capacity threshold" 或 "regime boundary" 更准确。

### W10. SNR "at convergence" 在 step 300 测量

**[AGREE] R1-W10: 这是一个精确性问题。**

Appendix F 显示 SNR 只测到 step 300（共 7 个 checkpoint: 0, 50, 100, 150, 200, 250, 300），但训练总共 1000 步。Table 7（training convergence）显示 PPL 在 step 600-800 才真正收敛（step 300 PPL=15.158 远高于 step 1000 的 11.906）。所以 step 300 不是"convergence"，称其为 "at convergence" 不当。

但 R1 将此定为 Minor 是合理的——SNR 分析是 suggestive evidence（§2.6 已明确说明），不是核心 claim 的唯一支撑。

### W11. PPL 11.79 vs 11.80 不一致

**[AGREE] R1-W11: Minor 编辑问题。**

Table 2 报告 11.79（exp_id: bench_kl50_global），§4.6 写 "11.80 at 50%"。差异 0.01 可能是四舍五入，但应统一。

---

## Questions 逐条回应

**Q1（Table 2/4 BCE 配置差异）**
[AGREE] 见 W2 分析。这是必须澄清的问题。

**Q2（C1 50% max Δ 计算来源）**
[AGREE] 见 W1 分析。论文声称的 0.59pp 与可见数据中的 0.79pp 不符。

**Q3（28.5% 训练偏差是否纳入调优）**
[AGREE] 合理问题。如果 KL predictor 在 28.5% 实际稀疏度下运行但与 TEAL@30% 对比，存在轻微的不公平性。见 W7 中的定量分析。

**Q4（BCE 2700步 + global top-k 结果）**
[AGREE] 合理问题。Table 2 显示 "BCE global†" 在 30% 有数据（PPL 11.25, 2700 steps），但 50% 的 BCE 条目似乎也是 2700 步（§4.3）。确认 2700 步 BCE 是否在 global/uniform 两种分配下都测试过，有助于理解 BCE 的 ceiling。

**Q5（Mistral GSM8K 反转机制）**
[AGREE] 与我自己的 Q3 一致。GSM8K 在 Mistral 和 LLaMA 上表现不同（Mistral 反转 11.1% vs 15.9%，LLaMA 接近 8.0% vs 7.88%），暗示 KL objective 与 chain-of-thought reasoning 的交互可能与架构相关。论文应至少提出假设。

**Q6（14B 多 seed 稳定性）**
[AGREE] 与我自己的 Q1 完全一致。14B MMLU 逆转是否为 seed 效应是影响论文结论的关键问题。

---

## 总结

我与 R1 在所有 11 条 Weakness 上达成一致，无需反驳。具体来说：

**完全一致**：W1, W2, W4, W5, W6, W8, W9, W10, W11
**一致但建议降级**：W3（R1 定 Must-Fix，我建议 Should-Fix，因为 taxonomy 完整性不影响核心 KL>BCE claim）、W7（论文在 appendix 中有合理 defense，建议主文讨论即可）

**R1 发现了我 Round 1 中遗漏的重要问题**：
- W1（数值勘误）：我未独立验证 0.59pp 这个具体数字
- W2（Table 2/4 不一致）：我未发现 BCE+comp 的 PPL 矛盾（28.13 vs 25.44）
- W8（WINA 幽灵 baseline）：我未注意到这个遗漏
- W10（SNR step 300 ≠ convergence）：我未核查 SNR 测量时间点

**两位审稿人独立发现的共同问题**（增强严重性判断）：
- 无 wall-clock 加速（R1-W6 = R2-N2）
- C1 soft-vs-hard confound（R1-W4 = R2-W2）
- 14B 单 seed + MMLU 逆转（R1-W5 = R2-N3/Q1）
- "Causal ablation" 命名过强（R1-W4 ∩ R2-W2）

**评分维持**：基于 R1 的额外发现（特别是 W2 的数据不一致），我对论文的信心略有下降，但整体评估维持 **Overall 3.0 (Findings)**。W1/W2 是必须修正的勘误/标注错误，但不改变方法论层面的判断；W3（MSE baseline 缺失）如果补上可能强化论文的 taxonomy claim，但不补也不致命。


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
