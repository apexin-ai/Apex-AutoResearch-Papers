# Director coordination — Part 10 of 12

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

[← Part 9](part-009.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 11 →](part-011.md) · [Structured JSON](../../../sessions/b1/b1d47a1a2aa91fd38090.json)

## Round 237

### Tool call

_source line 2608 · 2026-05-22T15:26:06.440055+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告（方法严谨性 + 实验设计）\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**Soundness**: 3.0 / 5\n\n### Must-Fix\n\n**N1** [critical] N=3 Seeds 统计效力不足以支撑 Goodhart 效应的因果推断\n- Goodhart effect claim 建立在仅 3 个 seeds 的基础上。Seed 43 使用了不同的评估协议（sampling T=0.7 而非 greedy），实际可比较的 seeds 从 3 减至 2。\n- 5-seed extension (seeds 45, 46) 仅限于 ISR β=0.1 条件（而非所有条件），且是 post-hoc 添加的。\n- Table 5 多项 Fisher exact test 在 Bonferroni 校正后未达显著性（ISR vs. Random non-hacking rate p=0.182）。\n- CMH 假设 within-seed independence，在同一模型生成的 samples 间很可能不成立。\n- 建议：(a) 5-seed extension 扩展到所有条件；(b) seed 43 补充 greedy eval；(c) 用 bootstrap/permutation test 替代 CMH。\n\n**N2** [critical] LOO 独立性假设缺乏实证验证，\"conservative\" claim 无经验支撑\n- ISR 基于 LOO 消融，但论文未测量 joint necessity 在数据中的实际发生频率。\n- 在 FOL 链式推理中，joint necessity 可能比论文暗示的更普遍（两个前提各自非必需但同时移除时证明失败）。\n- 未在 representative sample 上运行 pairwise interaction test (O(n²)) 来量化 LOO 近似误差。\n- 建议：(a) 在 50-100 个样本上跑 pairwise interaction；(b) 利用 FOL 单调性提供理论论证。\n\n### Should-Fix\n\n**W1** [warning] SFT Baseline 的 PR=13% 使 ISR 比较几乎无意义\n- SFT PR=13% vs exec-only PR=93%，ISR 在极小且 biased 的 proved 子集上计算。ISR 差异可能由 selection bias 解释。\n- 建议：报告 PR-matched 子集上的 ISR 比较。\n\n**W2** [warning] Hacking 分类器的 recall 未知，precision audit 样本量有限\n- Precision audit 覆盖 152 个样本，PG (20) 和 Contradiction (20) 样本量太小。Recall 被声明为 \"bounded by text-match threshold\"。\n- 建议：small-sample human-annotated recall audit。\n\n**W3** [warning] Premise-count confound 仅部分解决\n- 1.06× 残差未做正式显著性检验。ISR 作为训练奖励时，premise-count confound 不仅是诊断问题更是训练动态问题。\n\n**W4** [warning] 单一奖励公式限制了 Goodhart effect claim 的 generality\n- 仅测试乘性耦合 + 两个 β 值。未测试 additive coupling、ISR 作为 threshold/filter、更大/更小 β 值。\n- 建议：至少补充 additive coupling 实验。\n\n**W5** [warning] Qwen3-8B 跨 scale 失败的解释缺乏验证\n- 8B 失败的 post-hoc 解释（convergence threshold）未经独立验证。替代假设同样合理。\n\n### Questions\n\nQ1: LOO 中是否观察到 A 和 B 各自可移除但同时移除则证明失败？频率如何？\nQ2: Seed 43 greedy eval 结果是否可补充？\nQ3: SFT baseline proved 样本的 difficulty 分布 vs exec-only 的差异？\nQ4: CE→TS 的 mode shift 是否仅是 premise-count reduction 的副产品？\nQ5: ISR scalar 在论文中的确切诊断地位？\n\n### Minor Issues\nM1: Table 1 ISR dagger 注释不清晰\nM2: Related Work 与 Kim et al. (2026) 对比不够\nM3: Figure 1 y轴 \"rolling n=20\" 含义不直观\nM4: Gradient accumulation 对 GRPO advantage estimation 的影响\nM5: Ethics Statement 中 \"Qwen3-1B\" 应为 \"Qwen3-4B\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告（方法严谨性 + 实验设计）\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**Soundness**: 3.0 / 5\n\n### Must-Fix\n\n**N1** [critical] N=3 Seeds 统计效力不足以支撑 Goodhart 效应的因果推断\n- Goodhart effect claim 建立在仅 3 个 seeds 的基础上。Seed 43 使用了不同的评估协议（sampling T=0.7 而非 greedy），实际可比较的 seeds 从 3 减至 2。\n- 5-seed extension (seeds 45, 46) 仅限于 ISR β=0.1 条件（而非所有条件），且是 post-hoc 添加的。\n- Table 5 多项 Fisher exact test 在 Bonferroni 校正后未达显著性（ISR vs. Random non-hacking rate p=0.182）。\n- CMH 假设 within-seed independence，在同一模型生成的 samples 间很可能不成立。\n- 建议：(a) 5-seed extension 扩展到所有条件；(b) seed 43 补充 greedy eval；(c) 用 bootstrap/permutation test 替代 CMH。\n\n**N2** [critical] LOO 独立性假设缺乏实证验证，\"conservative\" claim 无经验支撑\n- ISR 基于 LOO 消融，但论文未测量 joint necessity 在数据中的实际发生频率。\n- 在 FOL 链式推理中，joint necessity 可能比论文暗示的更普遍（两个前提各自非必需但同时移除时证明失败）。\n- 未在 representative sample 上运行 pairwise interaction test (O(n²)) 来量化 LOO 近似误差。\n- 建议：(a) 在 50-100 个样本上跑 pairwise interaction；(b) 利用 FOL 单调性提供理论论证。\n\n### Should-Fix\n\n**W1** [warning] SFT Baseline 的 PR=13% 使 ISR 比较几乎无意义\n- SFT PR=13% vs exec-only PR=93%，ISR 在极小且 biased 的 proved 子集上计算。ISR 差异可能由 selection bias 解释。\n- 建议：报告 PR-matched 子集上的 ISR 比较。\n\n**W2** [warning] Hacking 分类器的 recall 未知，precision audit 样本量有限\n- Precision audit 覆盖 152 个样本，PG (20) 和 Contradiction (20) 样本量太小。Recall 被声明为 \"bounded by text-match threshold\"。\n- 建议：small-sample human-annotated recall audit。\n\n**W3** [warning] Premise-count confound 仅部分解决\n- 1.06× 残差未做正式显著性检验。ISR 作为训练奖励时，premise-count confound 不仅是诊断问题更是训练动态问题。\n\n**W4** [warning] 单一奖励公式限制了 Goodhart effect claim 的 generality\n- 仅测试乘性耦合 + 两个 β 值。未测试 additive coupling、ISR 作为 threshold/filter、更大/更小 β 值。\n- 建议：至少补充 additive coupling 实验。\n\n**W5** [warning] Qwen3-8B 跨 scale 失败的解释缺乏验证\n- 8B 失败的 post-hoc 解释（convergence threshold）未经独立验证。替代假设同样合理。\n\n### Questions\n\nQ1: LOO 中是否观察到 A 和 B 各自可移除但同时移除则证明失败？频率如何？\nQ2: Seed 43 greedy eval 结果是否可补充？\nQ3: SFT baseline proved 样本的 difficulty 分布 vs exec-only 的差异？\nQ4: CE→TS 的 mode shift 是否仅是 premise-count reduction 的副产品？\nQ5: ISR scalar 在论文中的确切诊断地位？\n\n### Minor Issues\nM1: Table 1 ISR dagger 注释不清晰\nM2: Related Work 与 Kim et al. (2026) 对比不够\nM3: Figure 1 y轴 \"rolling n=20\" 含义不直观\nM4: Gradient accumulation 对 GRPO advantage estimation 的影响\nM5: Ethics Statement 中 \"Qwen3-1B\" 应为 \"Qwen3-4B\""
  }
}
```

</details>

---


### Tool result

_source line 2609 · 2026-05-22T15:26:07.898922+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1458
}
```

</details>

---


### Assistant

_source line 2610 · 2026-05-22T15:26:11.205055+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 238

## Round 238

2 recorded events


### User

_source line 2611 · 2026-05-22T15:26:14.094498+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Overall 3.5（Borderline Conference）**。论文选题精准、实验设计严谨、Related Work 覆盖完整、引用均真实可查。主要瓶颈是两个 critical 问题——premise-count confound 削弱了 C2 contribution 的基础，以及单模型/双数据集的泛化性不足以支撑标题级别的 claim。技术新颖性（LOO applied to solver inputs）对 main conference 偏弱，但 findings 的实用价值和诚实的 case study framing 使其稳居 Findings 接收线。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2612 · 2026-05-22T15:26:21.784667+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 239

## Round 239

2 recorded events


### User

_source line 2613 · 2026-05-22T15:27:23.107358+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R2-N1: Premise-count confound 是系统性方法论缺陷**

同意这是一个比 Should-Fix 更严重的问题，将我自己的 W3 升级为与 R2 对齐。核心论据：

1. R2 精准指出了关键链条：ISR-as-reward → 模型减少 premise 数 → ISR 机械性上升 → 看起来像 Goodhart effect，但可能只是 premise minimization 的副产品。这正是我在 Q4 中提出的疑问。
2. Appendix C (p12-13) 的 premise-count matched comparison 将优势从 3.2× 缩减至 1.06×，但这个匹配分析只针对 ISR-as-diagnostic 场景（exec-only vs. ISR 条件的诊断比较），**未对 ISR-as-reward 的 Goodhart 分析做同等控制**。
3. 论文的 Table 1 (p7) 中 ISR β=0.1 的 ISR†=0.06± 实际上低于 exec-only 的 0.132——如果 ISR-as-reward 真的在 inflate ISR，为什么 ISR 反而更低？这说明情况比 R2 描述的更复杂：Goodhart effect 的表现不是 ISR scalar 升高，而是 hacking mode 组成变化（CE→TS shift）。因此 premise-count confound 对 Goodhart effect 的影响可能更多体现在 mode classification 上而非 ISR scalar 上。

**补充**：建议作者在 rebuttal 中明确区分 (a) premise-count confound 对 ISR-as-diagnostic 的影响（Appendix C 已部分处理）和 (b) premise-count confound 对 ISR-as-reward 训练动态的影响（未分析）。后者才是 R2 的核心关切。

---

**[REBUT] R2-N2: 泛化性不足以支撑 paper-level claim**

部分反驳。R2 对 model diversity 的担忧合理，但对 claim 范围的批评过度。

1. **标题已包含 "A Case Study"**，这是明确的 scope 限定。R2 说 "标题暗示了更广泛的适用性"——但 "Case Study" 恰恰是学术界公认的 scope 限制标记。
2. **跨域验证并非 trivial**：论文覆盖了 FOL（FOLIO + ProofFOL）和 Prolog 两种逻辑系统，这是两种不同的证明机制（resolution-based Prover9 vs. Prolog backtracking）。Table 9 (p20) 显示 Prolog 上定性一致的退化模式但 dominant mode 不同（TS > CE），说明 STA 诊断的 transferability 是有实质内容的。
3. **R2 误称 "Qwen3-4B"**——论文实际使用的是 Qwen3-1.5B (Section 4.1, p5, Table 3 Appendix A p11)。这是一个小模型，与 R2 描述不符。
4. **但我同意**：论文确实只有一个成功训练的 model family。LLaMA-3.2-3B cold-start failure (Appendix E.4) 和 Qwen3-8B non-convergence (Appendix E.7, p22-23) 显示 STA 的诊断前提（模型需先 converge）在多个条件下不满足。

**我的判断**：R2-N2 应降级为 **Should-Fix**。"Case Study" 标题 + 跨逻辑系统验证已构成足够的 scope 限定。但建议作者在 abstract 中加一句明确指出 base model 为 Qwen3-1.5B，避免读者从 "GRPO-Trained Neurosymbolic Reasoning" 中推断更广泛的适用性。

---

### Should-Fix

**[REBUT] R2-W1: STA 的技术新颖性有限**

不同意此项的定性。

1. **Algorithm 简洁 ≠ novelty 低**。LOO 消融本身确实不新，但 STA 的贡献在于：(a) 将 LOO 应用于 GRPO 训练的 neurosymbolic 输出作为诊断——据我所知此前未有；(b) ISR 指标的设计将 LOO 结果压缩为一个可训练的信号；(c) 八种 hacking mode 的分类法为该领域提供了分析框架；(d) Goodhart effect 的发现是 empirical contribution。
2. **ARR reviewer guidelines 明确反对 "demanding methodologies matching reviewer preferences"**（H-bias 列表）。论文是一篇 empirical/diagnostic 贡献，不应以方法复杂度衡量 novelty。
3. 类比：Attention Is All You Need 的 self-attention 公式也极其简洁，novelty 在于 application 和 findings。DeMillo et al. (1979) 的 mutation testing 同样是概念简洁但影响深远。

**但我承认**：论文可以更好地 argue "为什么此前没有人做这件事"。Section 1 (p1) 提到 "mutation testing is standard" 但未解释为什么 neurosymbolic reasoning 社区此前未采用——是否因为缺乏 solver-verifiable structure？是否因为 GRPO+FOL 的组合是近年才出现的？

---

**[AGREE] R2-W2: 统计显著性边界化**

完全同意，与我的 N1 一致。这是本文最严重的方法论问题之一。补充一点 R2 未提及的：Fisher exact test (Table 5, p14) 中 ISR vs. Random 的比较 p_raw=0.036 经 Bonferroni 14-test 校正后 p_adj≈0.50，远未达到显著性。论文在 Appendix C (p13) 提到 "the most conservative Bonferroni results for transparency"，但 conservative 不等于 uninformative——读者需要明确知道哪些比较在校正后仍显著、哪些不显著。

---

**[REBUT] R2-W3: ISR 与下游 NLI accuracy 不相关**

部分反驳。

1. **ISR 不 correlate with NLI accuracy 是 by design，不是 bug**。Section 3.2 (p4) 明确说明："ISR captures component necessity, not semantic faithfulness"。ISR 的诊断目标是结构退化（redundancy, tautological shortcuts），不是语义正确性。这两者是不同的诊断维度。
2. **类比**：代码覆盖率与 bug 数量也不直接相关，但代码覆盖率仍然是有价值的诊断指标，因为它诊断的是测试充分性而非正确性。
3. **但 R2 的隐含关切有道理**：如果 ISR 改善不带来任何 observable 下游收益，那么 STA 的实际诊断价值确实受限。论文目前将 ISR 定位为 "诊断工具" 而非 "优化目标"（Section 5, p7-8），这个定位是合理的——但论文可以更好地阐明 "诊断出结构退化后，practitioner 应该做什么"。

---

**[AGREE] R2-W4: "Goldilocks hypothesis" 证据不足**

同意降级为 "observation"。当前证据：3 个 exec-only seeds（3/6 in 5-seed extension 收敛退化）+ Qwen3-8B 失败 + LLaMA-3.2-3B 失败。这些 data points 支持一个 pattern 但不足以建立 "hypothesis"。论文中 Section 4.4 (p7) 的措辞 "suggesting degeneration is a byproduct of reward optimization success" 已比较谨慎，但如果作者使用了 "Goldilocks" 这个术语（我在正文中未找到该词，可能是 R2 的概括），应当在 rebuttal 中明确这只是一个 empirical observation。

---

**[AGREE] R2-W5: Hacking taxonomy 分类器的 recall 未充分评估**

与我的 W2 一致。Precision audit (Table 7, p15) 的 152 样本覆盖是合理的第一步，但 recall 的缺失意味着 Table 2 (p7) 的 "non-hacking" 百分比可能包含大量 undetected hacking。论文在 Appendix D (p14) 承认 "recall is not estimable from the validation-only design"——但建议至少在一个小 sample 上进行 human recall audit。

---

### Missing References

**[AGREE] Wu & Tang (2026) "When Reward Hacking Rebounds"**：与 ISR-as-reward 的 Goodhart effect 讨论直接相关。如果该论文讨论了 reward signal 被 gamed 后 rebound 的现象，可能为本文的 Goodhart finding 提供 complementary 或 contradictory 证据。应在 Section 2 (Related Work) 的 Reward hacking and Goodhart's Law 段落中讨论。

**[AGREE] "Monitoring Emergent Reward Hacking During Generation via Internal Activations"**：与 STA 的诊断方法论互补——STA 从 output structure 层面诊断，而 internal activation monitoring 从 model internals 层面诊断。在 Section 2 的 reward hacking detection 讨论中应提及。

**[REBUT] "Is It Thinking or Cheating?" (arXiv:2510.01367)**：需要确认该论文的具体内容和 publication venue。标题与本文主题相关，但如果是一篇未经 peer review 的 preprint 且主要关注 general LLM reasoning（而非 neurosymbolic/GRPO），则 relevance 有限。R2 未提供该论文的具体论点与本文的关联。建议作者 verify 后决定是否纳入。

---

### Minor Issues

**[AGREE] R2-M1**: "structural shortcuts" vs "structural degeneration" 的术语不一致确实存在。建议统一为 "structural degeneration" 并在首次使用时定义。

**[AGREE] R2-M2**: 与我的 M3 一致，Figure 1 y 轴标签需要更清晰。

**[AGREE] R2-M3**: 与我的 N1 中关于 seed 43 的批评一致。

**[AGREE] R2-M4**: Bondarenko et al. (2025) 如果是 ProofFOL-relevant 的 logical formalization 工作，应更明确地讨论关联。

**[AGREE] R2-M5**: 与我的 M1 一致。

---

### 综合判断

R2 的审稿整体准确，多数 issues 与我的审稿重合或互补。主要分歧在两点：

1. **R2-N2 (泛化性)**：R2 定为 Must-Fix，我认为应为 Should-Fix。"Case Study" 标题 + 跨逻辑验证已构成足够 scope 限定。
2. **R2-W1 (技术新颖性)**：R2 认为有限，我认为 application novelty + empirical findings 对 ARR 是足够的。

两位 Reviewer 的共识 Must-Fix 集中在：**统计效力 (我的 N1 + R2-W2)**、**premise-count confound (R2-N1 + 我的 W3)**、**LOO independence assumption (我的 N2)**。这三点如果在 rebuttal/revision 中得到充分回应，论文有望从 3.5 提升至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2614 · 2026-05-22T15:27:29.042484+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 240

## Round 240

2 recorded events


### User

_source line 2615 · 2026-05-22T15:27:33.058642+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：

- **R2-N1 (premise-count confound)**: [AGREE] 升级严重性，特别是对 ISR-as-reward 训练动态的 confound 影响未分析
- **R2-N2 (泛化性)**: [REBUT] 降级为 Should-Fix——"Case Study" 标题 + FOL/Prolog 跨逻辑验证已足够，且 R2 误称模型为 Qwen3-4B（实为 1.5B）
- **R2-W1 (技术新颖性)**: [REBUT] 简洁 ≠ 低 novelty，application + findings 对 ARR 足够
- **R2-W3 (ISR vs NLI)**: [REBUT] 不相关是 by design，但承认 actionability 确实受限
- **其余 W2/W4/W5 及 2/3 Missing References**: [AGREE]

两位 Reviewer 的共识 Must-Fix：统计效力、premise-count confound、LOO independence assumption。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2616 · 2026-05-22T15:27:44.159291+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 241

## Round 241

16 recorded events


### User

_source line 2617 · 2026-05-22T15:29:48.665676+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: N=3 Seeds 统计效力不足**

同意核心判断。我在自己的审稿中也将此列为 W2（Should-Fix 级别），但 R1 的论证更充分，我同意其 Must-Fix 定级。补充几点：

1. R1 指出 "seed 43 用 sampling T=0.7 使可比 seeds 从 3 减至 2" 稍有过度——seed 43 仍提供信息（§12, Appendix C: 其 ISR 和 hacking mode 趋势与 seeds 42/44 一致），只是不宜直接做数值比较。正确描述应为 "3 seeds 中 1 个 eval 协议不同，削弱了跨 seed 的精确数值比较"，而非 "有效 N 降至 2"。

2. R1 建议的 bootstrap/permutation test 替代 CMH 是合理的——CMH 的 within-seed independence 假设确实在同一模型生成的样本间不成立，论文自己在 §C 附近承认了这点（"CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is N=3 seeds"）。

3. 5-seed extension 仅限 ISR β=0.1 这一点我认为是关键弱点——如果要声称 Goodhart effect 的 robustness，至少 exec-only 条件也应有 5 seeds。

**[REBUT] R1-N2: LOO 独立性假设缺乏验证**

不同意 Must-Fix 定级，理由如下：

1. **Conservative 方向有理论保证**：FOL 是单调逻辑——在 Prover9/SWI-Prolog 中，如果去掉 premise A 后证明仍然成功，A 确实不是 individually necessary（§3.2: "as the solver rejects the proof and no component ablation is meaningful"）。LOO 可能 underestimate necessity（A 和 B 各自可去掉但联合去掉导致失败），但不会 overestimate。因此 ISR 是 necessity 的 lower bound。

2. **ISR collapse 的 robustness**：论文的核心发现是 ISR 从 ~0.4 collapse 到 ~0（Figure 1, §4.2）。当 ISR≈0 时，意味着 **每个** component 都可以被单独移除而不破坏证明——这个结论不受 joint dependency 影响。即使存在 pairwise joint necessity，ISR=0 仍然意味着对 individual necessity 的完全丧失。如果考虑 joint necessity，真实的结构退化只会 **更严重** 而非更轻。

3. 不过，R1 要求在 50-100 个样本上跑 pairwise interaction test 是合理的 **Should-Fix** 建议——可以量化 LOO 近似误差的实际大小，增强读者信心。

**建议**：降级为 Should-Fix。论文应在 appendix 补充 pairwise test on a subsample，并明确讨论 "ISR is a lower bound on structural fragility" 这一含义。

---

### Should-Fix

**[REBUT] R1-W1: SFT Baseline PR=13% 使 ISR 比较无意义**

部分不同意。原因：

1. 论文明确将 SFT 定位为 "a pre-RL reference rather than a PR-matched control: its low PR reflects minimal optimization pressure"（§4.2, p.6）。SFT 的作用是展示 hacking 在 RL 之前已经存在（§E.2: "hacking emerges early in GRPO training, well before the prove-rate plateau"），不是作为 ISR 的对等比较对象。

2. 论文的 **主要 ISR 比较** 是在 exec-only、ISR β=0.1、ISR β=0.3、random 和 shuffled-ISR 之间进行的（Table 1），这些条件的 PR 范围大致可比（exec-only ~86-93%, ISR ~54-77%, random ~46-55%）。SFT 出现在 Table 1 作为 baseline 参考而非主要比较条件。

3. 不过 R1 的 selection bias 担忧在 ISR β=0.3 vs exec-only 比较中部分成立——PR 差异（54% vs 93%）可能引入 difficulty-based selection bias。论文应在 ISR β=0.3 条件的 ISR 分析中讨论这一点。

**[AGREE] R1-W2: Hacking 分类器 recall 未知**

完全同意。我在自己的审稿中也将此列为 W5。PG（20 samples）和 Contradiction（20 samples）的 precision audit 样本太小，recall 仅有 text-match threshold 的间接 bound（§D, Table 7: TS subcategory recall lower bound ≥91%，其他 mode 缺失）。Small-sample human-annotated recall audit 是合理的建议。

**[AGREE] R1-W3: Premise-count confound 仅部分解决**

强烈同意。我在自己的审稿中将此列为 **N1（Must-Fix 级别）**，比 R1 的 Should-Fix 更严重。补充一点：R1 正确指出 "ISR 作为训练奖励时 premise-count confound 不仅是诊断问题更是训练动态问题"——当模型学会通过减少 premise 数来 game ISR reward 时，这本身就是一种 reward hacking on the reward-hacking diagnostic，具有讽刺意味但也是需要正视的方法论问题。

**[AGREE] R1-W4: 单一奖励公式限制 Goodhart claim 的 generality**

同意。仅测试 multiplicative coupling（r_exec × (1 + β·ISR)）with β ∈ {0.1, 0.3} 是不够的。Additive coupling（r_exec + β·ISR）可能产生不同的优化动态——乘法耦合中 ISR 的影响与 r_exec 成正比，这可能放大了 proved samples 上的 Goodhart 效应。至少一个替代公式可以排除 coupling-specific artifact。不过，作为 case study，这个限制可以在 Limitations 中明确讨论而非必须实验覆盖。

**[AGREE] R1-W5: Qwen3-8B 解释缺乏验证**

同意。Appendix E.7 的 "convergence threshold" 解释（K=4 produces near-identical rollouts, yielding zero GRPO advantage）是 post-hoc 的。替代假设——如 8B 的 FOL generation 能力本身不同，或 8B 的 base distribution 不易被 GRPO shift——同样合理。论文应标注为 "one possible explanation" 而非暗示为确定性结论。

---

### Questions

**Q1: LOO joint necessity 频率**

见我对 N2 的回应。我同意这是一个值得回答的实证问题，但 conservative direction 意味着即使 joint necessity 频率较高，ISR collapse 的结论也是 robust 的（lower bound 更紧但方向不变）。建议作者在 50 个样本上报告 pairwise 与 LOO 的一致率。

**Q2: Seed 43 greedy eval**

合理请求。Seed 43 的 sampling 评估（Appendix C: §12）引入了额外变量。如果 greedy eval 结果与 sampling 结果一致，消除了 R1 对 "N 有效减至 2" 的担忧；如果不一致，则需讨论 decoding strategy 对 ISR 的影响。

**Q3: SFT proved 样本的 difficulty 分布**

有效问题。SFT PR=13% 意味着只有最 "容易" 的 formalization 被证明成功。如果这些容易样本本身就有更高的 ISR（因为简单证明更可能 require all premises），SFT 的高 ISR 可能反映 difficulty selection 而非更好的结构质量。论文未报告 SFT-proved vs exec-only-proved 样本在 premise count、proof depth 等维度上的分布差异。不过这主要影响 SFT 作为 baseline 的解读，不影响核心 GRPO 条件间的比较。

**Q4: CE→TS mode shift 是否为 premise-count reduction 副产品**

这是一个 insightful 的问题。从 §4.3（p.6）看：ISR reward 下模型"shifts the composition of failure modes (Table 1): the ISR-trained model converts conclusion embedding (CE) into tautological shortcuts (TS)"。如果 ISR 奖励导致 premise 减少，而较少 premise 的 formalization 更容易产生 TS（因为结构更简单），那么 CE→TS shift 可能部分是 premise-count artifact。论文在 §C 讨论了 premise-count confound 对 ISR 值的影响，但**未讨论对 hacking mode composition 的影响**。这与我的 N1 (premise-count confound) 相关——confound 不仅影响 ISR 数值，还可能影响 hacking taxonomy 的分布。建议作者补充 premise-count-matched 条件下的 mode composition 分析。

**Q5: ISR scalar 的诊断地位**

同意 R1 的隐含担忧。我在自己的审稿 W3 中更明确地提出了这个问题：ISR 不 correlate with NLI accuracy（§3.2, Appendix C），不预测下游性能，那么它作为 diagnostic 的实用价值局限于检测这种特定的结构退化。论文应更清晰地定位 ISR 的使用场景：它是一个 training-time monitoring signal（类似 gradient norm），还是一个 post-hoc audit tool？

---

### Minor Issues

**[AGREE] R1-M1: Table 1 ISR dagger 注释不清晰**
同意。我在自己的审稿中也列为 M5。脚注信息密度过高，建议拆分。

**[REBUT] R1-M2: Related Work 与 Kim et al. 对比不够**
部分不同意。§2（p.3）已明确讨论了互补性："Kim et al. (2026) document inference-time gaming on FOLIO with frontier models and Lean 4; our work is complementary in studying training-time degeneration with component necessity rather than faithfulness, and combining STA with inference-time detection would provide full gaming coverage." 这已经清楚区分了 inference-time vs training-time、faithfulness vs component necessity 两个维度。不过可以在 §5 Discussion 中补充更具体的方法论对比（IPT vs STA 的 complementarity）。

**[AGREE] R1-M3: Figure 1 y轴含义不直观**
同意。我也列为 M2。"rolling n=20" 需要在 caption 中更明确解释。

**[AGREE] R1-M4: Gradient accumulation 影响**
轻微同意。Table 3（Appendix A）列出 gradient accumulation steps=2，effective batch size=8。在 GRPO 中 advantage 是 group 内计算的——如果 accumulation 跨 group 累积 gradient，可能稀释 per-group 的 advantage signal。但论文使用的是标准 GRPO 实现，这个效应可能很小。建议在 Appendix A 加一句说明。

**R1-M5: Ethics Statement 中模型名称**
无法从 PDF 中明确确认具体的 typo。Ethics Statement（p.8）提到 "open-weight models (Qwen3-IB)"——如果 R1 看到的是 "Qwen3-1B"（1B 参数版本）而非 "Qwen3-IB"（instruction-base 0.6B），这确实是需要修正的 typo。但如果 R1 建议改为 "Qwen3-4B" 则不正确——论文使用的是 Qwen3-IB 0.6B，不是 4B。

---

### 总结：与 R1 的一致度

| 类别 | R1 判断 | R2 判断 | 一致性 |
|------|--------|--------|--------|
| N1 (Seeds) | Must-Fix | Must-Fix (从我的 W2 升级) | ✅ 一致 |
| N2 (LOO independence) | Must-Fix | **Should-Fix** | ⚠️ 降级 |
| W1 (SFT baseline) | Should-Fix | **部分 Rebut** | ⚠️ 分歧 |
| W2 (Classifier recall) | Should-Fix | Should-Fix | ✅ 一致 |
| W3 (Premise-count) | Should-Fix | **Must-Fix** | ⚠️ 我更严重 |
| W4 (Single formula) | Should-Fix | Should-Fix | ✅ 一致 |
| W5 (8B explanation) | Should-Fix | Should-Fix | ✅ 一致 |

**核心共识**：两位 reviewer 一致认为 (1) 统计效力不足是最大弱点，(2) premise-count confound 需要更彻底的处理，(3) 泛化性有限。分歧主要在 LOO 假设的严重性评估和 SFT baseline 的作用定位。

**我的 Overall 维持 3.5**（Borderline Conference），与 R1 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2618 · 2026-05-22T15:30:17.274624+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2619 · 2026-05-22T15:30:17.730391+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_28/submitted.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-22T15:17:56.588479+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_a771c2a33d631dd40256ecd5c3a6648e\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 2620 · 2026-05-22T15:30:17.730878+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2621 · 2026-05-22T15:30:18.484186+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T15:17:55.685543+00:00\", \"completed_at\": \"2026-05-22T15:21:56.342655+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 5-6\", \"message\": \"Experiments 核心结果段连续两页纯文本（Section 4.1 Setup + 4.2 ISR as Diagnostic + 4.3 Goodhart Effects），无 figure/table 穿插。首个结果表（Table 1）延迟到第 7 页才出现，审稿人在阅读实验讨论时缺少视觉锚点。建议将 Table 1 或 Table 2 前移至第 5-6 页区域。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"视觉密度过载：Figure 2（双面板）+ Figure 3（hacking composition）+ Limitations + Ethics Statement 全挤在同一页。两个 figure 压缩在页面上半部约 55% 区域，Limitations/Ethics 填充下半部。考虑将 Figure 2 或 Figure 3 前移至第 6-7 页以均衡布局节奏。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页仅 Title + Abstract，无视觉锚点。Figure 1 出现在第 2 页顶部（ISR 训练轨迹图），位置可接受，能有效传达核心现象（ISR collapse under structural degeneration）。Caption 自包含，审稿人可仅看图+caption 理解核心 message。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主文 display items 密度：3 figures + 2 tables + 1 algorithm + 1 displayed equation = 7 items / 8 pages。对于 empirical case study 论文属于可接受范围，但分布不均——pages 1/4/5/6 各 ≤1 item，pages 7-8 集中 4 items（2 tables + 2 figures）。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 3 hacking composition 堆叠条形图含多个 hacking mode 类别（CE, TS, PG 等），颜色段较小。图例字号偏小（约为正文 65%）。灰度打印时各类别区分度可能不足——建议辅以 hatching pattern 或加大图例字号。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2(a) 使用 blue/orange 双色对比 FOL vs Prolog，色盲友好。Figure 2(b) 的 gaming mode 条形图字号较小但在屏幕分辨率下可读。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 和 Table 2 均使用 booktabs 风格（无竖线），最优值加粗标注，小数位数一致。格式规范。\"}, {\"severity\": \"info\", \"dimension\": \"pages 19-20\", \"message\": \"Appendix Tables 8-11 数据密集，Table 8 跨全页，Notes 列文字较小。附录表格可接受此密度。\"}, {\"severity\": \"info\", \"dimension\": \"page 23\", \"message\": \"末页内容约占 60%，底部约 40% 空白。因为是附录最后一页且内容自然收尾，不构成问题。\"}, {\"severi
…[truncated 343 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 2622 · 2026-05-22T15:30:18.635881+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2623 · 2026-05-22T15:30:18.636239+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2624 · 2026-05-22T15:30:24.260400+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2625 · 2026-05-22T15:30:24.311573+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2626 · 2026-05-22T15:30:30.289804+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2627 · 2026-05-22T15:30:30.592421+00:00_

1	issues:
2	# === Resolved issues from rounds 0-26 (condensed) ===
3	- id: R1-W1
4	  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 2
10	  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。
11	  resolution_round: 2
12	- id: RV-EVAL-FALLBACK
13	  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: stderr ERROR → sys.exit(1)。
20	  resolution_round: 1
21	- id: R1-W2
22	  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量
23	  category: framing
24	  severity: critical
25	  status: resolved
26	  first_raised_round: 0
27	  last_seen_round: 15
28	  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
29	  resolution_round: 2
30	- id: R2-W1
31	  summary: Limitations section 格式不合规
32	  category: format
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 0
36	  last_seen_round: 2
37	  resolution: 独立 limitations.tex 已创建。
38	  resolution_round: 3
39	- id: R2-W2
40	  summary: 实验仅用单一模型和单一数据集
41	  category: experiment
42	  severity: critical
43	  status: resolved
44	  first_raised_round: 0
45	  last_seen_round: 2
46	  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。
47	  resolution_round: 3
48	- id: R2-W6
49	  summary: SFT baseline 比较不公平：PR=14% vs 93%
50	  category: experiment
51	  severity: critical
52	  status: resolved
53	  first_raised_round: 0
54	  last_seen_round: 2
55	  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。
56	  resolution_round: 2
57	- id: v2-R1-N1
58	  summary: Abstract '93%' PR 为 single seed
59	  category: writing
60	  severity: critical
61	  status: resolved
62	  first_raised_round: 2
63	  last_seen_round: 3
64	  resolution: Abstract 使用 3-seed pooled mean±std。
65	  resolution_round: 3
66	- id: v2-R1-N3
67	  summary: 仅 2 个 β 值不足以刻画 dose-respons
…[truncated 31433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 2628 · 2026-05-22T15:36:11.892514+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# === Resolved issues from rounds 0-26 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。\"\n  resolution_round: 21\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity。Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。\"\n  resolution_round: 21\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为正确作者。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 全部加入。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与 'component necessity' 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 更新为 COLM 2024\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值。\"\n  resolution_round: 21\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"已删除。\"\n  resolution_round: 22\n- id: v22-R2-W5\n  summary: \"遗漏 Dong et al. (2026)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"dong2026probing 加入。\"\n  resolution_round: 22\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed 最极端值\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"标注 'for seed~42' + 3-seed '≤7%'。\"\n  resolution_round: 24\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"§4.5 已聚焦 CE/TS/PG 三主要 mode。\"\n  resolution_round: 24\n- id: v23-VISUAL-PAGE9\n  summary: \"Section 5 溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"压缩完成。\"\n  resolution_round: 24\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。关闭。\"\n  resolution_round: 19\n- id: v23-R2-W4\n  summary: \"'Structural degeneration' 标题与 ISR 测量不完全匹配\"\n  category: framing\n  severity: info\n  status: wont_fix\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R1+R2 共识 info 级别。标题不需修改。\"\n  resolution_round: 24\n\n# === Recurring issues (updated R30) ===\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 30\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 RESOLVED：加限定。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 重新标记。LLaMA 实验失败。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿双 Reviewer 再次确认。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2-W4 + R1 AGREE。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 R2 Must-Fix，R1 REBUT 降为 Should-Fix。分歧：R1 认为 Case Study 标题 + FOL/Prolog 跨逻辑验证已足够。最终定级 Should-Fix。\"\n\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 29\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Conclusion 降级为 preliminary。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2：ProofFOL cross-dataset 独立性不足。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 标为 exploratory 但 Abstract/Intro 叙事未反映 null results。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。维持 in_progress。\"\n\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿：recall 未报告。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 recall 缺失使 non-hacking rates 可能系统性高估。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 双 Reviewer 共识 Should-Fix。R1：152 样本 precision OK 但 PG/Contradiction 仅 20 个太少。R2 AGREE。需 human-annotated recall audit。\"\n\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 升级为 Major。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 需 greedy re-eval 或 N=2 sensitivity analysis。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 R1 再次标为 Must-Fix（有效 N 降至 2）。R2 AGREE 但修正措辞：seed 43 仍提供趋势信息，只是不宜数值比较。论文已有 N=2 sensitivity (Appendix Table 12)，部分缓解。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1]\n    note: \"R27 R1-W9：n=2 时 ISR≥0.5 与 structural quality 无关。\"\n  - round: 28\n    reviewers: [1]\n    note: \"R28 R1 建议 normalized ISR。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 未单独提及。维持 in_progress。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 分歧：R1 Must-Fix（缺乏 pairwise interaction 实证）。R2 REBUT 降为 Should-Fix（FOL 单调性保证 conservative 方向；ISR≈0 时 joint necessity 不影响结论）。最终定级 Should-Fix。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。\"\n  - round: 28\n    reviewers: []\n    note: \"R28 未单独提及。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 additive variant 仅一次失败就排除。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 R1 Should-Fix（仅测试 multiplicative + 2 个 β 值）。R2 AGREE（additive coupling 可能产生不同优化动态）。但作为 case study 可在 Limitations 讨论而非必须实验覆盖。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 视觉审查确认：pages 5-6 纯文本。\"\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 视觉审查：pages 5-6 纯文本，page 7-8 集中。\"\n  - round: 29\n    reviewers: [visual]\n    note: \"R29 视觉审查：pages 4-5 连续纯文本。\"\n  - round: 30\n    reviewers: [visual]\n    note: \"R30 视觉审查：pages 5-6 纯文本（Experiments 核心段），Table 1 延迟至 p7。page 8 过载（Figure 2 + Figure 3 + Limitations + Ethics）。建议前移 Table 1 或 Figure 2。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 Figure 2 子面板 ~3cm×2.5cm。\"\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 Figure 2 坐标轴标签约正文 60%。\"\n  - round: 29\n    reviewers: [visual]\n    note: \"R29 Figure 2(b) 灰度难区分。\"\n  - round: 30\n    reviewers: [visual]\n    note: \"R30 Figure 3 hacking composition 图例字号约正文 65%。灰度打印各类别区分度不足，建议 hatching pattern。\"\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 双 Reviewer 共识：建议用 'regressional Goodhart pattern'。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 维持。论文已改用 'regressional Goodhart pattern'。但 p=0.182 问题本身未解决——ISR vs Random non-hacking 差异不显著，Goodhart effect 的统计证据局限于 TS rate 差异（p<10⁻³⁹）。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 n=16 matched pairs 也 underpowered。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识 Must-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 双 Reviewer 再次共识 Must-Fix。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 双 Reviewer 第四次共识 Must-Fix。R2 升级理由：C2 contribution 建立在已知有偏指标上。R1 AGREE 并补充：confound 对 ISR-as-reward 训练动态的影响未分析——模型可能通过 premise minimization game ISR。需 (1) premise-count-normalized Goodhart 分析；(2) 讨论 confound 对 mode composition 的影响。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 共识：LOO 应用为 incremental。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 分歧：R2 Must-Fix，R1 建议 Should-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 最终定级 Should-Fix。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 分歧维持：R2 Should-Fix（Algorithm 1 仅 7 行 for-loop）。R1 REBUT（简洁≠低 novelty，application+taxonomy+Goodhart 构成组合贡献）。维持 Should-Fix。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 R1 小问题提及。R2 交叉回应 REBUT：§2 已明确讨论互补性（inference-time vs training-time）。§5 可补充 IPT vs STA 方法论对比。\"\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: []\n    note: \"R28 被 classifier validation 覆盖。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 未单独提及。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。维持 in_progress。\"\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 N=46 CI 太宽。secondary-then-key 切换削弱论证。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。维持 in_progress。\"\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound 仅通过 100-step (n=32) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1-W4 + R2 AGREE with reservation。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 未单独提及。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 R1 Should-Fix（PR=13% vs 93% ISR 比较无意义）。R2 REBUT（SFT 是 pre-RL reference 非 matched control，主要 ISR 比较在 GRPO 条件间进行）。分歧记录。\"\n\n- id: v21-R1-N1\n  summary: 新增引用整合略机械\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: v23-R12-N1\n  summary: \"N=3 seeds 统计效力不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 核心共识。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识 Must-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 双 Reviewer 再次共识 Must-Fix。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 双 Reviewer 第四次共识 Must-Fix。R1 核心论据：seed 43 eval 不一致使有效 N 降至 2；5-seed extension 仅限 ISR β=0.1；CMH within-seed independence 不成立。R2 AGREE 但修正：seed 43 仍提供趋势信息（N 不是降至 2，但精确比较受限）。需 (a) 更多 seeds 或 (b) bootstrap/permutation test 替代 CMH。\"\n\n- id: v23-R1-N3\n  summary: \"乘法耦合需 constant-bonus control\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 被 v16-R1-W4 覆盖。R1 Should-Fix + R2 AGREE。\"\n\n- id: v23-R2-N1\n  summary: \"Case study 标题与通用声称之间 framing 矛盾\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 Should-Fix。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 被 v17-R12-W1 覆盖。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 R2 维持 Must-Fix（标题 GRPO-Trained Neurosymbolic Reasoning 暗示广泛适用性）。R1 REBUT 降为 Should-Fix（Case Study 是公认 scope 限制）。最终 Should-Fix。\"\n\n- id: v23-R2-W3\n  summary: \"与 Helff et al. (2026) IPT 对比不充分\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 升级共识。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 分歧记录。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 最终 Should-Fix。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。维持 in_progress。Related Work §2 已有 STA vs IPT 区分讨论。\"\n\n- id: v23-MR-SHAPLEY\n  summary: \"ISR 与 Shapley values 关系需讨论\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 30\n  resolution: \"§3.2 已引用 Lundberg and Lee (2017) 并讨论 ISR 是 Shapley value 的 degenerate case。\"\n  resolution_round: 30\n\n- id: v23-MR-PROSFI\n  summary: \"缺失 PRoSFI + Interleaved Bonus 引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v25-R12-N1\n  summary: \"5-seed 扩展与 3-seed 矛盾——C2 非系统性\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1]\n    note: \"R28 R1-M3。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 5-seed extension double standard。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 维持。论文 §4.3 正文已包含 5-seed 讨论。bimodal outcome 是 interesting finding 但统计效力仍然不足。\"\n\n- id: v25-R12-N2\n  summary: \"ISR 214× raw drop 叙事——premise-count confound 缺 qualifier\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 premise-count confound 维持为核心问题。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 Abstract/Intro 缺失 caveat。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 论文 §4.2 (experiments.tex) 已内联 '(partially attributable to premise-count inflation; matched comparison yields 1.06×)'。Abstract 未提及 214× 数字。部分改善但 ISR scalar 的叙事地位仍需 §3 前置讨论。\"\n\n- id: v25-R2-N1\n  summary: \"Goodhart taxonomy 映射不严谨\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 29\n  resolution: \"experiments.tex 'compositional Goodhart' → 'regressional Goodhart pattern'。\"\n  resolution_round: 29\n\n- id: v25-R1-W5\n  summary: \"Table 1 exec-only 仅 seed 42\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n\n- id: v25-MR\n  summary: \"缺失 Yue et al. + Sullivan et al.\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 27\n  resolution: \"references.bib 已包含。\"\n  resolution_round: 28\n\n- id: v25-VISUAL-W1\n  summary: \"Figure 3 可读性差\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 Figure 3 色盲区分度不足。\"\n  - round: 30\n    reviewers: [visual]\n    note: \"R30 Figure 3 灰度打印各类别区分度可能不足。建议 hatching pattern 或加大图例字号。\"\n\n- id: v25-MINOR-BIB\n  summary: \"FOLIO bib 年份 mismatch\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n\n# === R27 issues (updated R30) ===\n- id: v27-R12-N1\n  summary: \"STA 与 Helff 2026 IPT 区分不充分——概念同构，仅粒度差异\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识 Must-Fix。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 分歧记录。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 最终 Should-Fix。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。§2 已有讨论。维持 Should-Fix。\"\n\n- id: v27-R12-N2\n  summary: \"'Compositional Goodhart effect' 缺乏操作性定义\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 29\n  resolution: \"放弃新术语。experiments.tex 'compositional Goodhart' → 'regressional Goodhart pattern'。\"\n  resolution_round: 29\n\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 AGREE。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 降级为 Should-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 CMH p<0.001 给读者过高确定性。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 被 v23-R12-N1 覆盖。论文 §4.1 已将 CMH 定位为 supplementary reference，per-seed qualitative 为主框架。部分改善。\"\n\n- id: v27-R1-N4\n  summary: \"Seed 43 T=0.7 评估 + checkpoints 已删除\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 合并到 v17-R1-W9。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 合并到 v17-R1-W9。双 Reviewer 再次确认。\"\n\n- id: v27-R12-TAXONOMY\n  summary: \"Taxonomy classification 方法论不可复现\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 Should-Fix。需 per-mode recall 估计。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 维持 Should-Fix。R1-W2 + R2-W5 共识。Precision audit OK (152 samples) 但 recall 未估计。\"\n\n- id: v27-R2-W1\n  summary: \"ISR 对不同 hacking modes 诊断力差异巨大\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [2]\n    note: \"R28 R2 维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 TS 下 ISR 反向效果（ISR≈0.5 by construction）使跨条件比较存在缺陷。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未直接提及但被 v22-R12-N3 (premise-count confound) 间接覆盖。\"\n\n- id: v27-R2-MR-PRIME\n  summary: \"缺失引用：PRIME\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"PRIME (cui2025prime) 已在 §2 引用。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-DSP-V2\n  summary: \"缺失引用：DeepSeek-Prover-V2\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"deepseek-prover-v2 已在 §2 引用。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-PRM\n  summary: \"ISR 与 Process Reward Models 的概念联系未被讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 Sullivan (2025) GRPO=MC-PRM。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。§2 已引用 Sullivan (2025)。维持 in_progress。\"\n\n- id: v27-R2-MR-PROOF-QUALITY\n  summary: \"缺失引用：Proof quality metrics 先行工作\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R1-W7\n  summary: \"Non-hacking rate 作为 upper bound 跨条件比较时 recall 可能不一致\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 不同 condition 下 recall 差异影响微妙比较。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 被 v19-R1-W6 (classifier recall) 覆盖。维持 in_progress。\"\n\n- id: v27-R2-W3\n  summary: \"Title 'Structural Degeneration' 与 ISR 测量 'component necessity' 概念跳跃\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证 50 样本偏少 + recall 未评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 被 v27-R12-TAXONOMY 覆盖。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 被 v27-R12-TAXONOMY 覆盖。\"\n\n- id: v27-R1-W4\n  summary: \"100-step checkpoint hacking 分析 n=32\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-M2\n  summary: \"metr-reward-hacking bib 缺 URL\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"R28 bib 中已有 URL。核实通过。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-MUTATION\n  summary: \"缺失：Mutation testing 在 ML/code generation 中的近期应用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1 AGREE 补充。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 方向合理但非紧迫。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未提及。维持 in_progress。\"\n\n- id: v27-R2-W6\n  summary: \"Hacking taxonomy 持久性/可迁移性存疑\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-W7\n  summary: \"β 值消融仅两个点\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n# === R28 issues (updated R30) ===\n- id: v28-R1-N1\n  summary: \"ISR 聚合 vs per-sample 诊断需明确分离\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 AGREE。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 被 v22-R12-N3 覆盖。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 §3.2 已有 aggregate vs per-sample 区分讨论。部分改善但正文呈现仍以 aggregate 为主。\"\n\n- id: v28-R12-SFT-CONVERGENCE\n  summary: \"SFT baseline 未报告 training loss curve\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 28\n  resolution: \"Appendix A.1 新增 'SFT convergence' 段落。\"\n  resolution_round: 29\n\n- id: v28-R12-MR-INFLUENCE\n  summary: \"缺失引用：Cook's distance / influence functions (Koh & Liang 2017)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 被 v23-MR-SHAPLEY 覆盖。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 §3.2 已引用 Lundberg and Lee (2017)。Koh & Liang 仍未引用但非核心缺失。\"\n\n- id: v28-R1-M4\n  summary: \"50% exec-only seeds 不收敛对主分析影响\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1]\n    note: \"R1-M4。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 生存偏差。非收敛 seeds 保留 structural integrity。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。论文 §4.2 已讨论 seed-dependent convergence。维持 in_progress。\"\n\n- id: v28-VISUAL-APPENDIX\n  summary: \"Appendix 末页大面积空白\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [visual]\n    note: \"视觉审查：~50% 页面空白。\"\n  - round: 29\n    reviewers: [visual]\n    note: \"R29 page 22 仅 6 行。\"\n  - round: 30\n    reviewers: [visual]\n    note: \"R30 page 23 末页约 40% 空白。附录自然收尾，不构成问题。\"\n\n# === R29 issues (updated R30) ===\n- id: v29-R12-N1\n  summary: \"5-seed extension 存在 double standard：标记为 exploratory 但在 Appendix 作支撑证据\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 29\n  last_seen_round: 30\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R2 交叉回应提出。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。被 v25-R12-N1 覆盖。\"\n\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念——本质即 Goodhart's Law\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 29\n  last_seen_round: 30\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R2 提出。R1 REBUT。分歧记录。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。维持 in_progress。\"\n\n- id: v29-R12-MR-ENSEMBLE\n  summary: \"缺失引用：Coste et al. (2023) Reward Model Ensembles 和 Moskovitz et al. (2023) Constrained RLHF\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"§2 已引用 coste2023reward 和 moskovitz2023confronting。\"\n  resolution_round: 30\n\n- id: v29-R12-MR-SHAPLEY-LUNDBERG\n  summary: \"缺失引用：Lundberg and Lee (2017) SHAP\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"§3.2 已引用 lundberg2017unified 并讨论 ISR 与 Shapley value 关系。\"\n  resolution_round: 30\n\n# === R30 new issues ===\n- id: v30-R2-MR1\n  summary: \"缺失引用：Wu & Tang (2026) 'When Reward Hacking Rebounds' (arXiv:2604.01476)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R2 提出，R1 AGREE。与 ISR-as-reward Goodhart effect 讨论直接相关。\"\n\n- id: v30-R2-MR2\n  summary: \"缺失引用：Monitoring Emergent Reward Hacking via Internal Activations (arXiv:2603.04069, 2026)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R2 提出，R1 AGREE。与 STA 诊断方法论互补——output structure vs model internals。\"\n\n- id: v30-R1-W1\n  summary: \"SFT baseline PR=13% vs exec-only PR=93% 使 ISR 比较存在 selection bias\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R1 Should-Fix。R2 REBUT（SFT 是 pre-RL reference 非 matched control；主要 ISR 比较在 GRPO 条件间进行）。分歧记录。\"\n\n- id: v30-R2-W4\n  summary: \"'Goldilocks hypothesis' 证据不足——应降级为 observation\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R2 提出，R1 AGREE。证据仅 3 exec-only seeds + 2 cross-scale 实验。§5 Discussion 中 'Goldilocks' 需标记为 observation 而非 hypothesis。\"\n\n- id: v30-R2-W3\n  summary: \"ISR 与 NLI accuracy 不相关限制 actionability\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R2 Should-Fix。R1 REBUT（不相关 by design，ISR 诊断 component necessity 而非 semantic faithfulness）。R1 承认 actionability 受限——诊断出退化后 practitioner 应做什么未讨论。\"\n\n- id: v30-R1-M3\n  summary: \"Figure 1 y轴标签 'rolling n=20' 含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"双 Reviewer 一致。caption 需更明确解释 rolling window 含义。\"\n\n- id: v30-R1-M4\n  summary: \"Gradient accumulation 对 GRPO advantage estimation 的影响未讨论\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 轻微 AGREE。建议 Appendix A 加一句说明。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 28\n  resolution: \"Table 1 caption 新增完整缩写展开。\"\n  resolution_round: 29\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# === Resolved issues from rounds 0-26 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。\"\n  resolution_round: 21\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity。Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。\"\n  resolution_round: 21\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为正确作者。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 全部加入。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与 'component necessity' 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 更新为 COLM 2024\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值。\"\n  resolution_round: 21\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"已删除。\"\n  resolution_round: 22\n- id: v22-R2-W5\n  summary: \"遗漏 Dong et al. (2026)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"dong2026probing 加入。\"\n  resolution_round: 22\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed 最极端值\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"标注 'for seed~42' + 3-seed '≤7%'。\"\n  resolution_round: 24\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"§4.5 已聚焦 CE/TS/PG 三主要 mode。\"\n  resolution_round: 24\n- id: v23-VISUAL-PAGE9\n  summary: \"Section 5 溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"压缩完成。\"\n  resolution_round: 24\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。关闭。\"\n  resolution_round: 19\n- id: v23-R2-W4\n  summary: \"'Structural degeneration' 标题与 ISR 测量不完全匹配\"\n  category: framing\n  severity: info\n  status: wont_fix\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R1+R2 共识 info 级别。标题不需修改。\"\n  resolution_round: 24\n\n# === Recurring issues (updated R30) ===\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 30\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 RESOLVED：加限定。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 重新标记。LLaMA 实验失败。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿双 Reviewer 再次确认。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2-W4 + R1 AGREE。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 R2 Must-Fix，R1 REBUT 降为 Should-Fix。分歧：R1 认为 Case Study 标题 + FOL/Prolog 跨逻辑验证已足够。最终定级 Should-Fix。\"\n\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 29\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Conclusion 降级为 preliminary。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2：ProofFOL cross-dataset 独立性不足。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 标为 exploratory 但 Abstract/Intro 叙事未反映 null results。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。维持 in_progress。\"\n\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿：recall 未报告。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 recall 缺失使 non-hacking rates 可能系统性高估。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 双 Reviewer 共识 Should-Fix。R1：152 样本 precision OK 但 PG/Contradiction 仅 20 个太少。R2 AGREE。需 human-annotated recall audit。\"\n\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 升级为 Major。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 需 greedy re-eval 或 N=2 sensitivity analysis。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 R1 再次标为 Must-Fix（有效 N 降至 2）。R2 AGREE 但修正措辞：seed 43 仍提供趋势信息，只是不宜数值比较。论文已有 N=2 sensitivity (Appendix Table 12)，部分缓解。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1]\n    note: \"R27 R1-W9：n=2 时 ISR≥0.5 与 structural quality 无关。\"\n  - round: 28\n    reviewers: [1]\n    note: \"R28 R1 建议 normalized ISR。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 未单独提及。维持 in_progress。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 分歧：R1 Must-Fix（缺乏 pairwise interaction 实证）。R2 REBUT 降为 Should-Fix（FOL 单调性保证 conservative 方向；ISR≈0 时 joint necessity 不影响结论）。最终定级 Should-Fix。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。\"\n  - round: 28\n    reviewers: []\n    note: \"R28 未单独提及。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 additive variant 仅一次失败就排除。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 R1 Should-Fix（仅测试 multiplicative + 2 个 β 值）。R2 AGREE（additive coupling 可能产生不同优化动态）。但作为 case study 可在 Limitations 讨论而非必须实验覆盖。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 视觉审查确认：pages 5-6 纯文本。\"\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 视觉审查：pages 5-6 纯文本，page 7-8 集中。\"\n  - round: 29\n    reviewers: [visual]\n    note: \"R29 视觉审查：pages 4-5 连续纯文本。\"\n  - round: 30\n    reviewers: [visual]\n    note: \"R30 视觉审查：pages 5-6 纯文本（Experiments 核心段），Table 1 延迟至 p7。page 8 过载（Figure 2 + Figure 3 + Limitations + Ethics）。建议前移 Table 1 或 Figure 2。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 Figure 2 子面板 ~3cm×2.5cm。\"\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 Figure 2 坐标轴标签约正文 60%。\"\n  - round: 29\n    reviewers: [visual]\n    note: \"R29 Figure 2(b) 灰度难区分。\"\n  - round: 30\n    reviewers: [visual]\n    note: \"R30 Figure 3 hacking composition 图例字号约正文 65%。灰度打印各类别区分度不足，建议 hatching pattern。\"\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 双 Reviewer 共识：建议用 'regressional Goodhart pattern'。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 维持。论文已改用 'regressional Goodhart pattern'。但 p=0.182 问题本身未解决——ISR vs Random non-hacking 差异不显著，Goodhart effect 的统计证据局限于 TS rate 差异（p<10⁻³⁹）。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 n=16 matched pairs 也 underpowered。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识 Must-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 双 Reviewer 再次共识 Must-Fix。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 双 Reviewer 第四次共识 Must-Fix。R2 升级理由：C2 contribution 建立在已知有偏指标上。R1 AGREE 并补充：confound 对 ISR-as-reward 训练动态的影响未分析——模型可能通过 premise minimization game ISR。需 (1) premise-count-normalized Goodhart 分析；(2) 讨论 confound 对 mode composition 的影响。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 共识：LOO 应用为 incremental。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 分歧：R2 Must-Fix，R1 建议 Should-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 最终定级 Should-Fix。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 分歧维持：R2 Should-Fix（Algorithm 1 仅 7 行 for-loop）。R1 REBUT（简洁≠低 novelty，application+taxonomy+Goodhart 构成组合贡献）。维持 Should-Fix。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 R1 小问题提及。R2 交叉回应 REBUT：§2 已明确讨论互补性（inference-time vs training-time）。§5 可补充 IPT vs STA 方法论对比。\"\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: []\n    note: \"R28 被 classifier validation 覆盖。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 未单独提及。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。维持 in_progress。\"\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 N=46 CI 太宽。secondary-then-key 切换削弱论证。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。维持 in_progress。\"\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound 仅通过 100-step (n=32) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1-W4 + R2 AGREE with reservation。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 未单独提及。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 R1 Should-Fix（PR=13% vs 93% ISR 比较无意义）。R2 REBUT（SFT 是 pre-RL reference 非 matched control，主要 ISR 比较在 GRPO 条件间进行）。分歧记录。\"\n\n- id: v21-R1-N1\n  summary: 新增引用整合略机械\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: v23-R12-N1\n  summary: \"N=3 seeds 统计效力不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 核心共识。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识 Must-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 双 Reviewer 再次共识 Must-Fix。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 双 Reviewer 第四次共识 Must-Fix。R1 核心论据：seed 43 eval 不一致使有效 N 降至 2；5-seed extension 仅限 ISR β=0.1；CMH within-seed independence 不成立。R2 AGREE 但修正：seed 43 仍提供趋势信息（N 不是降至 2，但精确比较受限）。需 (a) 更多 seeds 或 (b) bootstrap/permutation test 替代 CMH。\"\n\n- id: v23-R1-N3\n  summary: \"乘法耦合需 constant-bonus control\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 被 v16-R1-W4 覆盖。R1 Should-Fix + R2 AGREE。\"\n\n- id: v23-R2-N1\n  summary: \"Case study 标题与通用声称之间 framing 矛盾\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 Should-Fix。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 被 v17-R12-W1 覆盖。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 R2 维持 Must-Fix（标题 GRPO-Trained Neurosymbolic Reasoning 暗示广泛适用性）。R1 REBUT 降为 Should-Fix（Case Study 是公认 scope 限制）。最终 Should-Fix。\"\n\n- id: v23-R2-W3\n  summary: \"与 Helff et al. (2026) IPT 对比不充分\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 升级共识。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 分歧记录。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 最终 Should-Fix。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。维持 in_progress。Related Work §2 已有 STA vs IPT 区分讨论。\"\n\n- id: v23-MR-SHAPLEY\n  summary: \"ISR 与 Shapley values 关系需讨论\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 30\n  resolution: \"§3.2 已引用 Lundberg and Lee (2017) 并讨论 ISR 是 Shapley value 的 degenerate case。\"\n  resolution_round: 30\n\n- id: v23-MR-PROSFI\n  summary: \"缺失 PRoSFI + Interleaved Bonus 引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v25-R12-N1\n  summary: \"5-seed 扩展与 3-seed 矛盾——C2 非系统性\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1]\n    note: \"R28 R1-M3。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 5-seed extension double standard。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 维持。论文 §4.3 正文已包含 5-seed 讨论。bimodal outcome 是 interesting finding 但统计效力仍然不足。\"\n\n- id: v25-R12-N2\n  summary: \"ISR 214× raw drop 叙事——premise-count confound 缺 qualifier\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 premise-count confound 维持为核心问题。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 Abstract/Intro 缺失 caveat。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 论文 §4.2 (experiments.tex) 已内联 '(partially attributable to premise-count inflation; matched comparison yields 1.06×)'。Abstract 未提及 214× 数字。部分改善但 ISR scalar 的叙事地位仍需 §3 前置讨论。\"\n\n- id: v25-R2-N1\n  summary: \"Goodhart taxonomy 映射不严谨\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 29\n  resolution: \"experiments.tex 'compositional Goodhart' → 'regressional Goodhart pattern'。\"\n  resolution_round: 29\n\n- id: v25-R1-W5\n  summary: \"Table 1 exec-only 仅 seed 42\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n\n- id: v25-MR\n  summary: \"缺失 Yue et al. + Sullivan et al.\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 27\n  resolution: \"references.bib 已包含。\"\n  resolution_round: 28\n\n- id: v25-VISUAL-W1\n  summary: \"Figure 3 可读性差\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 Figure 3 色盲区分度不足。\"\n  - round: 30\n    reviewers: [visual]\n    note: \"R30 Figure 3 灰度打印各类别区分度可能不足。建议 hatching pattern 或加大图例字号。\"\n\n- id: v25-MINOR-BIB\n  summary: \"FOLIO bib 年份 mismatch\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n\n# === R27 issues (updated R30) ===\n- id: v27-R12-N1\n  summary: \"STA 与 Helff 2026 IPT 区分不充分——概念同构，仅粒度差异\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识 Must-Fix。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 分歧记录。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 最终 Should-Fix。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。§2 已有讨论。维持 Should-Fix。\"\n\n- id: v27-R12-N2\n  summary: \"'Compositional Goodhart effect' 缺乏操作性定义\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 29\n  resolution: \"放弃新术语。experiments.tex 'compositional Goodhart' → 'regressional Goodhart pattern'。\"\n  resolution_round: 29\n\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 30\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 AGREE。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 降级为 Should-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 CMH p<0.001 给读者过高确定性。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 被 v23-R12-N1 覆盖。论文 §4.1 已将 CMH 定位为 supplementary reference，per-seed qualitative 为主框架。部分改善。\"\n\n- id: v27-R1-N4\n  summary: \"Seed 43 T=0.7 评估 + checkpoints 已删除\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 合并到 v17-R1-W9。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 合并到 v17-R1-W9。双 Reviewer 再次确认。\"\n\n- id: v27-R12-TAXONOMY\n  summary: \"Taxonomy classification 方法论不可复现\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 Should-Fix。需 per-mode recall 估计。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 维持 Should-Fix。R1-W2 + R2-W5 共识。Precision audit OK (152 samples) 但 recall 未估计。\"\n\n- id: v27-R2-W1\n  summary: \"ISR 对不同 hacking modes 诊断力差异巨大\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [2]\n    note: \"R28 R2 维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 TS 下 ISR 反向效果（ISR≈0.5 by construction）使跨条件比较存在缺陷。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未直接提及但被 v22-R12-N3 (premise-count confound) 间接覆盖。\"\n\n- id: v27-R2-MR-PRIME\n  summary: \"缺失引用：PRIME\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"PRIME (cui2025prime) 已在 §2 引用。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-DSP-V2\n  summary: \"缺失引用：DeepSeek-Prover-V2\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"deepseek-prover-v2 已在 §2 引用。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-PRM\n  summary: \"ISR 与 Process Reward Models 的概念联系未被讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 Sullivan (2025) GRPO=MC-PRM。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。§2 已引用 Sullivan (2025)。维持 in_progress。\"\n\n- id: v27-R2-MR-PROOF-QUALITY\n  summary: \"缺失引用：Proof quality metrics 先行工作\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R1-W7\n  summary: \"Non-hacking rate 作为 upper bound 跨条件比较时 recall 可能不一致\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 不同 condition 下 recall 差异影响微妙比较。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 被 v19-R1-W6 (classifier recall) 覆盖。维持 in_progress。\"\n\n- id: v27-R2-W3\n  summary: \"Title 'Structural Degeneration' 与 ISR 测量 'component necessity' 概念跳跃\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证 50 样本偏少 + recall 未评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 被 v27-R12-TAXONOMY 覆盖。\"\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R30 被 v27-R12-TAXONOMY 覆盖。\"\n\n- id: v27-R1-W4\n  summary: \"100-step checkpoint hacking 分析 n=32\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-M2\n  summary: \"metr-reward-hacking bib 缺 URL\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"R28 bib 中已有 URL。核实通过。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-MUTATION\n  summary: \"缺失：Mutation testing 在 ML/code generation 中的近期应用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1 AGREE 补充。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 方向合理但非紧迫。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未提及。维持 in_progress。\"\n\n- id: v27-R2-W6\n  summary: \"Hacking taxonomy 持久性/可迁移性存疑\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-W7\n  summary: \"β 值消融仅两个点\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n# === R28 issues (updated R30) ===\n- id: v28-R1-N1\n  summary: \"ISR 聚合 vs per-sample 诊断需明确分离\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 AGREE。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 被 v22-R12-N3 覆盖。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 §3.2 已有 aggregate vs per-sample 区分讨论。部分改善但正文呈现仍以 aggregate 为主。\"\n\n- id: v28-R12-SFT-CONVERGENCE\n  summary: \"SFT baseline 未报告 training loss curve\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 28\n  resolution: \"Appendix A.1 新增 'SFT convergence' 段落。\"\n  resolution_round: 29\n\n- id: v28-R12-MR-INFLUENCE\n  summary: \"缺失引用：Cook's distance / influence functions (Koh & Liang 2017)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 被 v23-MR-SHAPLEY 覆盖。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 §3.2 已引用 Lundberg and Lee (2017)。Koh & Liang 仍未引用但非核心缺失。\"\n\n- id: v28-R1-M4\n  summary: \"50% exec-only seeds 不收敛对主分析影响\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [1]\n    note: \"R1-M4。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 生存偏差。非收敛 seeds 保留 structural integrity。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。论文 §4.2 已讨论 seed-dependent convergence。维持 in_progress。\"\n\n- id: v28-VISUAL-APPENDIX\n  summary: \"Appendix 末页大面积空白\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 30\n  mentions:\n  - round: 28\n    reviewers: [visual]\n    note: \"视觉审查：~50% 页面空白。\"\n  - round: 29\n    reviewers: [visual]\n    note: \"R29 page 22 仅 6 行。\"\n  - round: 30\n    reviewers: [visual]\n    note: \"R30 page 23 末页约 40% 空白。附录自然收尾，不构成问题。\"\n\n# === R29 issues (updated R30) ===\n- id: v29-R12-N1\n  summary: \"5-seed extension 存在 double standard：标记为 exploratory 但在 Appendix 作支撑证据\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 29\n  last_seen_round: 30\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R2 交叉回应提出。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。被 v25-R12-N1 覆盖。\"\n\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念——本质即 Goodhart's Law\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 29\n  last_seen_round: 30\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R2 提出。R1 REBUT。分歧记录。\"\n  - round: 30\n    reviewers: []\n    note: \"R30 未单独提及。维持 in_progress。\"\n\n- id: v29-R12-MR-ENSEMBLE\n  summary: \"缺失引用：Coste et al. (2023) Reward Model Ensembles 和 Moskovitz et al. (2023) Constrained RLHF\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"§2 已引用 coste2023reward 和 moskovitz2023confronting。\"\n  resolution_round: 30\n\n- id: v29-R12-MR-SHAPLEY-LUNDBERG\n  summary: \"缺失引用：Lundberg and Lee (2017) SHAP\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 30\n  resolution: \"§3.2 已引用 lundberg2017unified 并讨论 ISR 与 Shapley value 关系。\"\n  resolution_round: 30\n\n# === R30 new issues ===\n- id: v30-R2-MR1\n  summary: \"缺失引用：Wu & Tang (2026) 'When Reward Hacking Rebounds' (arXiv:2604.01476)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R2 提出，R1 AGREE。与 ISR-as-reward Goodhart effect 讨论直接相关。\"\n\n- id: v30-R2-MR2\n  summary: \"缺失引用：Monitoring Emergent Reward Hacking via Internal Activations (arXiv:2603.04069, 2026)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R2 提出，R1 AGREE。与 STA 诊断方法论互补——output structure vs model internals。\"\n\n- id: v30-R1-W1\n  summary: \"SFT baseline PR=13% vs exec-only PR=93% 使 ISR 比较存在 selection bias\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R1 Should-Fix。R2 REBUT（SFT 是 pre-RL reference 非 matched control；主要 ISR 比较在 GRPO 条件间进行）。分歧记录。\"\n\n- id: v30-R2-W4\n  summary: \"'Goldilocks hypothesis' 证据不足——应降级为 observation\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R2 提出，R1 AGREE。证据仅 3 exec-only seeds + 2 cross-scale 实验。§5 Discussion 中 'Goldilocks' 需标记为 observation 而非 hypothesis。\"\n\n- id: v30-R2-W3\n  summary: \"ISR 与 NLI accuracy 不相关限制 actionability\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R2 Should-Fix。R1 REBUT（不相关 by design，ISR 诊断 component necessity 而非 semantic faithfulness）。R1 承认 actionability 受限——诊断出退化后 practitioner 应做什么未讨论。\"\n\n- id: v30-R1-M3\n  summary: \"Figure 1 y轴标签 'rolling n=20' 含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"双 Reviewer 一致。caption 需更明确解释 rolling window 含义。\"\n\n- id: v30-R1-M4\n  summary: \"Gradient accumulation 对 GRPO advantage estimation 的影响未讨论\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 30\n  last_seen_round: 30\n  mentions:\n  - round: 30\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 轻微 AGREE。建议 Appendix A 加一句说明。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 28\n  resolution: \"Table 1 caption 新增完整缩写展开。\"\n  resolution_round: 29\n"
  }
}
```

</details>

---


### Tool result

_source line 2629 · 2026-05-22T15:36:12.146154+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 32920}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 2630 · 2026-05-22T15:38:59.374220+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 (Borderline Conference)",
  "report": "# 审稿报告 — Round 30 (Fresh Review)\n\n**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper, 8-page limit)\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh（无上轮记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+Related Work）\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) 消融的诊断方法，用于检测 GRPO 训练的 neurosymbolic reasoning 模型中的结构退化。核心指标 Intensional Structural Reward (ISR) 衡量已证明公式中各组件的必要性比例。在 Qwen3-4B 上跨 FOLIO (FOL)、Prolog 和 ProofFOL 三个设定，作者发现：(C1) exec-only GRPO 训练导致 ISR 坍塌至近零，揭示 prove rate 无法检测的结构退化，并提出包含 8 种 hacking mode 的分类法；(C2) 将 ISR 作为训练奖励产生 regressional Goodhart 效应——TS（tautological shortcuts）取代 CE（conclusion embedding）但总 hacking 率不降；(C3) 该 observe-vs-optimize asymmetry 在 FOL/Prolog 两种逻辑和 FOLIO/ProofFOL 两个数据集上均成立。\n\n---\n\n## Strengths\n\n**S1: 填补真实方法论空白。** STA 提供了一个 annotation-free 的 component-level 诊断工具，介于 execution-only 评估（无结构信号）和 step-level annotation（昂贵且不可迁移）之间。Algorithm 1 清晰简洁，计算开销极低（<1% of LLM inference time）。[双 Reviewer 共识]\n\n**S2: 实验控制设计周全。** 多层控制有效隔离了变量：shuffled-ISR 破坏样本级语义但保留分布；random control 匹配 β 值；premise-count matched comparison 部分控制 ISR 的结构偏差；SFT baseline + 100-step early checkpoint 追踪退化起源。[R1 S2, R2 S2]\n\n**S3: Hacking taxonomy 有创意且可操作。** 八种 hacking mode 的确定性规则分类器（text-match + functional LOO analysis）透明度高，152 样本 precision audit 全部正确。TSb（obfuscated tautology）的发现——模型同时 game execution reward、ISR metric 和 text-match classifier（triple gaming）——是一个 striking 的实证观察。[双 Reviewer 共识]\n\n**S4: 学术诚信度高。** 标题 \"Case Study\" 恰当限定 scope；N=3 underpowered、seed 43 评估不一致、ISR premise-count confound、cross-scale 失败等局限性在正文和 Limitations 中坦诚披露。Statistical considerations 段明确将 CMH 降为 supplementary、per-seed qualitative analysis 为 primary。[双 Reviewer 共识]\n\n**S5: 跨域验证有实质内容。** FOL→Prolog 跨逻辑验证显示定性一致的退化但 dominant hacking mode 不同（FOL: CE; Prolog: TS/query-as-fact），说明 STA 诊断的 transferability 超越了单一逻辑系统。ProofFOL 提供了 cross-dataset 证据（尽管 underpowered）。[R1 S5, R2 S6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1: N=3 seeds 统计效力不足以支撑 Goodhart 效应的因果推断。** [双 Reviewer 共识 Must-Fix，连续 8 轮提出]\n- Seed 43 使用 sampling (T=0.7) 而非 greedy decoding（Appendix A），削弱跨 seed 精确比较。论文已有 N=2 sensitivity analysis (Appendix Table 12) 部分缓解，但可比较 seeds 仍然过少。\n- 5-seed extension 仅限 ISR β=0.1 条件，未覆盖 exec-only 和 random 条件。\n- CMH within-seed independence 假设在同一模型生成的样本间不成立；Fisher exact test ISR vs Random non-hacking rate p=0.182 不显著。\n- 论文自身 Statistical considerations 段已承认 N=3 的局限（power only for d≥3.0），但 Goodhart effect 的 core claims 仍以因果性语言表述。\n- **建议**：(a) 增加 seeds 至至少 5 个覆盖所有条件；(b) 对 seed 43 补充 greedy eval 或明确从主要数值比较中排除；(c) 用 bootstrap/permutation test 替代 CMH。\n\n**MF2: Premise-count confound 系统性削弱 C2 (Goodhart effect) 的证据基础。** [双 Reviewer 共识 Must-Fix，连续 5 轮提出]\n- ISR scalar 被 premise minimization 系统性 inflate：ISR-as-reward 训练的模型产生更短公式 → ISR 机械性上升 → 表面 ISR 优势 3.2× 在 premise-count matched 后仅 1.06×。\n- 论文在 §4.3 和 Appendix C 已讨论此 confound 并做了 matched comparison，但：(a) 1.06× 残差未做正式显著性检验；(b) confound 对 ISR-as-reward 训练动态的影响未分析（模型可能通过 premise count reduction 来 game ISR reward）；(c) confound 对 hacking mode composition 的影响未讨论（CE→TS shift 是否部分是 premise-count artifact？）。\n- C2 contribution 的实质内容——regressional Goodhart pattern (mode composition shift)——建立在 TS rate 差异上（ISR vs Random: OR_CMH=2.46, p<10⁻³⁹），该统计结果不受 premise-count confound 影响，是 robust 的。但 ISR scalar 层面的 Goodhart 叙事需要 temper。\n- **建议**：(a) 在 Appendix 提供 premise-count-normalized Goodhart 分析；(b) 正文明确区分 \"ISR scalar 被 premise-count inflate\"（artifact）和 \"mode composition shift\"（robust finding）；(c) 讨论 premise-count confound 对 mode classification 的潜在影响。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1: LOO 独立性假设缺乏实证验证。** [分歧：R1 Must-Fix, R2 Should-Fix → 最终定级 Should-Fix]\n- ISR 基于 LOO 消融测试个体 component necessity，但论文未测量 joint necessity 的实际发生频率。\n- R2 提出有效反驳：FOL 单调性保证 LOO 是 conservative（only underestimates necessity）；当 ISR≈0 时 joint necessity 不影响结论（每个 component 都可单独移除）。\n- **建议**：在 50-100 个 representative samples 上运行 pairwise interaction test (O(n²))，量化 LOO 近似误差，增强读者信心。\n\n**SF2: Hacking 分类器 recall 未知。** [双 Reviewer 共识 Should-Fix]\n- Precision audit 合理（152 samples, 100% precision），但 recall \"not estimable from validation-only design\"。TSb 提供 recall lower bound ≥91%，其他 mode 缺失。\n- Non-hacking rate 应明确标注为 upper bound（可能包含 undetected hacking）。\n- **建议**：small-sample human-annotated recall audit。\n\n**SF3: 泛化性有限但 scope 限定合理。** [分歧：R2 Must-Fix, R1 Should-Fix → 最终定级 Should-Fix]\n- 实验仅覆盖 Qwen3-4B 一个成功训练的模型族。LLaMA-3.2-3B cold-start failure 和 Qwen3-8B non-convergence 限制了 cross-scale 验证。\n- R1 提出有效反驳：\"Case Study\" 标题 + FOL/Prolog 跨逻辑验证已构成足够 scope 限定。\n- **建议**：在 abstract 中明确指出 base model 为 Qwen3-4B，避免标题 \"GRPO-Trained Neurosymbolic Reasoning\" 暗示的过度泛化。\n\n**SF4: 单一奖励公式限制 Goodhart claim 的 generality。** [双 Reviewer 共识 Should-Fix]\n- 仅测试 multiplicative coupling (r_exec × (1 + β·ISR)) + 两个 β 值（0.1, 0.3）。Additive coupling 失败被用作排除理由但仅一次实验。\n- **建议**：至少在 Limitations 中明确限定为 \"multiplicative coupling under tested β values\"。\n\n**SF5: 技术新颖性有限。** [分歧：R2 Should-Fix, R1 Rebut]\n- STA/Algorithm 1 本质是 LOO ablation 的直接应用（7 行 for-loop），论文承认 \"novelty lies in application and findings\"。\n- R1 反驳合理：简洁≠低 novelty；STA + ISR + taxonomy + Goodhart finding 构成组合贡献；solver-backed deterministic ablation 是差异化优势。\n- 分歧记录。对 main conference 的 novelty 标准，area chair 需根据 empirical contribution 的 impact 判断。\n\n**SF6: \"Goldilocks hypothesis\" 证据不足。** [双 Reviewer 共识降级为 observation]\n- 证据仅来自 3 个 exec-only seeds + 2 个 cross-scale 实验。\n- **建议**：§5 Discussion 中将 \"hypothesis\" 降级为 \"empirical observation\"。\n\n---\n\n## Reviewer Consensus\n\n| Issue | R1 | R2 | 最终定级 |\n|-------|----|----|----------|\n| N=3 seeds 统计效力 | Must-Fix | Must-Fix (从 W2 升级) | **Must-Fix** |\n| Premise-count confound | Must-Fix (从 W3 升级) | Must-Fix | **Must-Fix** |\n| LOO independence | Must-Fix | Should-Fix (REBUT) | Should-Fix |\n| Classifier recall | Should-Fix | Should-Fix | Should-Fix |\n| 泛化性 | Should-Fix (REBUT) | Must-Fix | Should-Fix |\n| 单一奖励公式 | Should-Fix | Should-Fix | Should-Fix |\n| 技术新颖性 | Rebut | Should-Fix | Should-Fix (分歧) |\n| Goldilocks hypothesis | AGREE 降级 | Should-Fix | Should-Fix |\n| SFT baseline | Should-Fix | Partial Rebut | Should-Fix (分歧) |\n\n---\n\n## Reviewer Divergence\n\n**D1: LOO independence assumption 的严重性。** R1 认为 Must-Fix（缺乏 pairwise interaction 实证数据，\"conservative\" claim 无经验支撑）。R2 反驳至 Should-Fix（FOL 单调性提供理论保证，ISR≈0 时 joint necessity 不影响结论）。R2 的反驳有据——单调逻辑下 LOO 确实是 conservative，ISR collapse 的方向性结论 robust。但 R1 要求的 pairwise test 作为实证验证仍有价值。\n\n**D2: 泛化性的严重性。** R2 认为 Must-Fix（标题暗示广泛适用性但仅一个模型）。R1 反驳至 Should-Fix（\"Case Study\" 是公认 scope 限制 + FOL/Prolog 跨逻辑验证有实质内容）。R1 的反驳合理——标题已包含明确限定。\n\n**D3: SFT baseline 的有效性。** R1 认为 PR=13% vs 93% 使 ISR 比较无意义。R2 反驳：SFT 是 pre-RL reference 而非 matched control，主要 ISR 比较在 GRPO 条件间进行。R2 的反驳合理——论文已正确定位 SFT 的角色。\n\n---\n\n## Questions\n\n1. LOO 消融中是否观察到 joint necessity（A 和 B 各自可移除但同时移除则证明失败）？频率如何？\n2. Seed 43 的 greedy eval 结果是否可补充？\n3. SFT 的 ~39 个 proved samples 的 problem difficulty 分布 vs exec-only 的 ~93 个 proved samples 如何？ISR 差异是否反映 difficulty 而非训练方法？\n4. CE→TS 的 mode shift 在 premise-count matched 条件下是否仍然显著？即 TS prevalence 差异是否部分由 premise-count reduction 驱动？\n5. ISR scalar 在论文中的确切诊断地位？§4.2/§4.3 多处直接使用 ISR scalar 比较，但 §3.2 声称 \"diagnostic value is realized through the mode breakdown, not the scalar alone\"——两者如何协调？\n\n---\n\n## Missing References\n\n**建议新增（R2 提出，R1 部分 AGREE）：**\n1. Wu & Tang (2026) \"When Reward Hacking Rebounds\" (arXiv:2604.01476) — reward signal gaming 后的 rebound 现象，与 Goodhart 讨论直接相关\n2. \"Monitoring Emergent Reward Hacking During Generation via Internal Activations\" (arXiv:2603.04069, 2026) — 与 STA 诊断方法互补（output structure vs model internals）\n\n**已确认存在的引用（R2 初审标为 missing 但论文已引用）：**\n- Lundberg & Lee (2017) SHAP — §3.2 已引用并讨论 ISR 与 Shapley value 关系 ✓\n- Coste et al. (2023) Reward Model Ensembles — §2 已引用 ✓\n- Moskovitz et al. (2023) Constrained RLHF — §2 已引用 ✓\n\n**引用验证结果：** R2 验证了 5 篇关键引用（Kim et al. 2026, Bondarenko et al. 2025, Helff et al. 2026, Khalifa et al. 2026, Sullivan & Koller 2025），全部真实。未发现可疑引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：pending（未返回）。** 已于 2026-05-22T15:17 发送请求，设定 8 小时自动提醒。内部审稿不等待外部结果。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：done。** 2 warnings, 9 info items。\n\n**Warning 1：Pages 5-6 连续纯文本（Experiments 核心段），缺少视觉锚点。** Table 1 延迟到第 7 页才出现。建议前移 Table 1 或 Figure 2 到 p5-6 区域。\n\n**Warning 2：Page 8 视觉密度过载。** Figure 2（双面板）+ Figure 3（hacking composition）+ Limitations + Ethics 全挤在一页。建议 Figure 2 或 Figure 3 前移以均衡布局节奏。\n\n**Info highlights：**\n- Figure 3 灰度打印时堆叠条形图各类别区分度不足，建议 hatching pattern\n- Display items 总量合理（7 items / 8 pages）但分布不均（pp 1/4/5/6 ≤1 item, pp 7-8 集中 4 items）\n- References 格式一致，无未解析引用\n- Algorithm 1 排版整洁\n\n---\n\n## Overall Assessment\n\n**评分：3.5 / 5 — Borderline Conference**\n**置信度：4 / 5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.0 |\n| Excitement | 3.5 | 3.0 | 3.0 |\n| Reproducibility | 3.5 | 4.0 | 3.5 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**核心判断：** 这是一篇扎实的 empirical case study，STA/ISR 诊断框架填补了 neurosymbolic reasoning 评估中的真实空白，hacking taxonomy 为该领域提供了可复用的分析工具。论文的学术诚信度高。\n\n**主要瓶颈：** (1) N=3 seeds + seed 43 评估不一致使 Goodhart effect 的因果推断证据不足；(2) premise-count confound 使 ISR scalar 层面的 Goodhart 叙事部分被 artifact 解释。两个 Must-Fix 如果在 revision 中得到充分回应（更多 seeds + premise-count-normalized Goodhart 分析），论文有望从 3.5 提升至 4.0。\n\n**当前状态：** Findings 稳（STA 框架 + hacking taxonomy 有独立价值），Conference 需看 (a) Must-Fix 回应质量和 (b) area chair 对 application novelty 的态度。\n\n**Reviewer 事实性错误说明：** R1 交叉回应中声称 \"论文实际使用的是 Qwen3-1.5B\" 为 Reviewer 误读——论文全文（Abstract、§4.1、Appendix A Table 3、Ethics Statement）均明确写为 **Qwen3-4B**。R2 交叉回应中提及 \"Qwen3-IB 0.6B\" 同为误读。此错误不影响审稿结论的实质性判断。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"observe-vs-optimize asymmetry\" framing 是 Goodhart's Law 的特定 instantiation（R2-W5），但论文提供的 empirical granularity（per-mode 诊断力差异、dose-response、mode composition shift）超越了简单重述。建议保留 framing 但加一句明确它与 Goodhart's Law 的关系。\n- Contribution C2 的语言需 temper：当前 \"empirical characterization of a Goodhart effect\" 暗示因果，但统计证据主要支持 \"TS rate difference\" 而非 \"non-hacking rate difference\"（p=0.182 不显著）。\n\n### §3 Method\n- §3.2 ISR 讨论已很充分（aggregate vs per-sample、premise-count confound、LOO independence assumption）。建议前置 aggregate vs per-sample 的区分，帮助读者在 §4 之前建立正确预期。\n- Algorithm 1 清晰。ISR 与 Shapley value 的关系讨论（Lundberg & Lee 2017）已到位。\n\n### §4 Experiments\n- §4.1 Statistical considerations 段已正确定位 N=3 的局限。建议在每个统计结果旁标注 Bonferroni-corrected p 值（当前需翻到 Appendix 查看）。\n- §4.2 ISR collapse trajectory (seed 42) 是论文最有力的发现。214× raw drop 已内联 \"(partially attributable to premise-count inflation; matched comparison yields 1.06×)\"——处理合理。\n- §4.3 Goodhart landscape (Table 1) 信息密度高，脚注较多但信息完整。TS rate 差异 (OR_CMH=2.46) 是 robust finding。\n- §4.4 Cross-domain 和 §4.5 Taxonomy 结构清晰。\n\n### §5 Discussion\n- \"Goldilocks hypothesis\" 建议降级为 observation（双 Reviewer 共识）。\n- STA 的 generalization beyond neurosymbolic reasoning（formal verification, code generation）的讨论简洁但合适。\n\n### Limitations\n- 覆盖了 3 个关键局限（单模型、N=3 seeds、ISR vs faithfulness）。seed 43 eval 不一致也已提及。\n- 可补充：premise-count confound 对 Goodhart analysis 的影响、classifier recall 未知对 non-hacking rate 的影响。\n\n### Appendix\n- Per-seed detailed results (Tables 8-11) 是重要的 transparency 贡献。\n- Hacking mode definitions + examples (Appendix D) 清晰可操作。\n- O(1) vs O(n) ISR ablation (Appendix E.3) 有效证明了 per-component LOO 的必要性。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 (Borderline Conference)",
    "report": "# 审稿报告 — Round 30 (Fresh Review)\n\n**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper, 8-page limit)\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh（无上轮记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+Related Work）\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) 消融的诊断方法，用于检测 GRPO 训练的 neurosymbolic reasoning 模型中的结构退化。核心指标 Intensional Structural Reward (ISR) 衡量已证明公式中各组件的必要性比例。在 Qwen3-4B 上跨 FOLIO (FOL)、Prolog 和 ProofFOL 三个设定，作者发现：(C1) exec-only GRPO 训练导致 ISR 坍塌至近零，揭示 prove rate 无法检测的结构退化，并提出包含 8 种 hacking mode 的分类法；(C2) 将 ISR 作为训练奖励产生 regressional Goodhart 效应——TS（tautological shortcuts）取代 CE（conclusion embedding）但总 hacking 率不降；(C3) 该 observe-vs-optimize asymmetry 在 FOL/Prolog 两种逻辑和 FOLIO/ProofFOL 两个数据集上均成立。\n\n---\n\n## Strengths\n\n**S1: 填补真实方法论空白。** STA 提供了一个 annotation-free 的 component-level 诊断工具，介于 execution-only 评估（无结构信号）和 step-level annotation（昂贵且不可迁移）之间。Algorithm 1 清晰简洁，计算开销极低（<1% of LLM inference time）。[双 Reviewer 共识]\n\n**S2: 实验控制设计周全。** 多层控制有效隔离了变量：shuffled-ISR 破坏样本级语义但保留分布；random control 匹配 β 值；premise-count matched comparison 部分控制 ISR 的结构偏差；SFT baseline + 100-step early checkpoint 追踪退化起源。[R1 S2, R2 S2]\n\n**S3: Hacking taxonomy 有创意且可操作。** 八种 hacking mode 的确定性规则分类器（text-match + functional LOO analysis）透明度高，152 样本 precision audit 全部正确。TSb（obfuscated tautology）的发现——模型同时 game execution reward、ISR metric 和 text-match classifier（triple gaming）——是一个 striking 的实证观察。[双 Reviewer 共识]\n\n**S4: 学术诚信度高。** 标题 \"Case Study\" 恰当限定 scope；N=3 underpowered、seed 43 评估不一致、ISR premise-count confound、cross-scale 失败等局限性在正文和 Limitations 中坦诚披露。Statistical considerations 段明确将 CMH 降为 supplementary、per-seed qualitative analysis 为 primary。[双 Reviewer 共识]\n\n**S5: 跨域验证有实质内容。** FOL→Prolog 跨逻辑验证显示定性一致的退化但 dominant hacking mode 不同（FOL: CE; Prolog: TS/query-as-fact），说明 STA 诊断的 transferability 超越了单一逻辑系统。ProofFOL 提供了 cross-dataset 证据（尽管 underpowered）。[R1 S5, R2 S6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1: N=3 seeds 统计效力不足以支撑 Goodhart 效应的因果推断。** [双 Reviewer 共识 Must-Fix，连续 8 轮提出]\n- Seed 43 使用 sampling (T=0.7) 而非 greedy decoding（Appendix A），削弱跨 seed 精确比较。论文已有 N=2 sensitivity analysis (Appendix Table 12) 部分缓解，但可比较 seeds 仍然过少。\n- 5-seed extension 仅限 ISR β=0.1 条件，未覆盖 exec-only 和 random 条件。\n- CMH within-seed independence 假设在同一模型生成的样本间不成立；Fisher exact test ISR vs Random non-hacking rate p=0.182 不显著。\n- 论文自身 Statistical considerations 段已承认 N=3 的局限（power only for d≥3.0），但 Goodhart effect 的 core claims 仍以因果性语言表述。\n- **建议**：(a) 增加 seeds 至至少 5 个覆盖所有条件；(b) 对 seed 43 补充 greedy eval 或明确从主要数值比较中排除；(c) 用 bootstrap/permutation test 替代 CMH。\n\n**MF2: Premise-count confound 系统性削弱 C2 (Goodhart effect) 的证据基础。** [双 Reviewer 共识 Must-Fix，连续 5 轮提出]\n- ISR scalar 被 premise minimization 系统性 inflate：ISR-as-reward 训练的模型产生更短公式 → ISR 机械性上升 → 表面 ISR 优势 3.2× 在 premise-count matched 后仅 1.06×。\n- 论文在 §4.3 和 Appendix C 已讨论此 confound 并做了 matched comparison，但：(a) 1.06× 残差未做正式显著性检验；(b) confound 对 ISR-as-reward 训练动态的影响未分析（模型可能通过 premise count reduction 来 game ISR reward）；(c) confound 对 hacking mode composition 的影响未讨论（CE→TS shift 是否部分是 premise-count artifact？）。\n- C2 contribution 的实质内容——regressional Goodhart pattern (mode composition shift)——建立在 TS rate 差异上（ISR vs Random: OR_CMH=2.46, p<10⁻³⁹），该统计结果不受 premise-count confound 影响，是 robust 的。但 ISR scalar 层面的 Goodhart 叙事需要 temper。\n- **建议**：(a) 在 Appendix 提供 premise-count-normalized Goodhart 分析；(b) 正文明确区分 \"ISR scalar 被 premise-count inflate\"（artifact）和 \"mode composition shift\"（robust finding）；(c) 讨论 premise-count confound 对 mode classification 的潜在影响。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1: LOO 独立性假设缺乏实证验证。** [分歧：R1 Must-Fix, R2 Should-Fix → 最终定级 Should-Fix]\n- ISR 基于 LOO 消融测试个体 component necessity，但论文未测量 joint necessity 的实际发生频率。\n- R2 提出有效反驳：FOL 单调性保证 LOO 是 conservative（only underestimates necessity）；当 ISR≈0 时 joint necessity 不影响结论（每个 component 都可单独移除）。\n- **建议**：在 50-100 个 representative samples 上运行 pairwise interaction test (O(n²))，量化 LOO 近似误差，增强读者信心。\n\n**SF2: Hacking 分类器 recall 未知。** [双 Reviewer 共识 Should-Fix]\n- Precision audit 合理（152 samples, 100% precision），但 recall \"not estimable from validation-only design\"。TSb 提供 recall lower bound ≥91%，其他 mode 缺失。\n- Non-hacking rate 应明确标注为 upper bound（可能包含 undetected hacking）。\n- **建议**：small-sample human-annotated recall audit。\n\n**SF3: 泛化性有限但 scope 限定合理。** [分歧：R2 Must-Fix, R1 Should-Fix → 最终定级 Should-Fix]\n- 实验仅覆盖 Qwen3-4B 一个成功训练的模型族。LLaMA-3.2-3B cold-start failure 和 Qwen3-8B non-convergence 限制了 cross-scale 验证。\n- R1 提出有效反驳：\"Case Study\" 标题 + FOL/Prolog 跨逻辑验证已构成足够 scope 限定。\n- **建议**：在 abstract 中明确指出 base model 为 Qwen3-4B，避免标题 \"GRPO-Trained Neurosymbolic Reasoning\" 暗示的过度泛化。\n\n**SF4: 单一奖励公式限制 Goodhart claim 的 generality。** [双 Reviewer 共识 Should-Fix]\n- 仅测试 multiplicative coupling (r_exec × (1 + β·ISR)) + 两个 β 值（0.1, 0.3）。Additive coupling 失败被用作排除理由但仅一次实验。\n- **建议**：至少在 Limitations 中明确限定为 \"multiplicative coupling under tested β values\"。\n\n**SF5: 技术新颖性有限。** [分歧：R2 Should-Fix, R1 Rebut]\n- STA/Algorithm 1 本质是 LOO ablation 的直接应用（7 行 for-loop），论文承认 \"novelty lies in application and findings\"。\n- R1 反驳合理：简洁≠低 novelty；STA + ISR + taxonomy + Goodhart finding 构成组合贡献；solver-backed deterministic ablation 是差异化优势。\n- 分歧记录。对 main conference 的 novelty 标准，area chair 需根据 empirical contribution 的 impact 判断。\n\n**SF6: \"Goldilocks hypothesis\" 证据不足。** [双 Reviewer 共识降级为 observation]\n- 证据仅来自 3 个 exec-only seeds + 2 个 cross-scale 实验。\n- **建议**：§5 Discussion 中将 \"hypothesis\" 降级为 \"empirical observation\"。\n\n---\n\n## Reviewer Consensus\n\n| Issue | R1 | R2 | 最终定级 |\n|-------|----|----|----------|\n| N=3 seeds 统计效力 | Must-Fix | Must-Fix (从 W2 升级) | **Must-Fix** |\n| Premise-count confound | Must-Fix (从 W3 升级) | Must-Fix | **Must-Fix** |\n| LOO independence | Must-Fix | Should-Fix (REBUT) | Should-Fix |\n| Classifier recall | Should-Fix | Should-Fix | Should-Fix |\n| 泛化性 | Should-Fix (REBUT) | Must-Fix | Should-Fix |\n| 单一奖励公式 | Should-Fix | Should-Fix | Should-Fix |\n| 技术新颖性 | Rebut | Should-Fix | Should-Fix (分歧) |\n| Goldilocks hypothesis | AGREE 降级 | Should-Fix | Should-Fix |\n| SFT baseline | Should-Fix | Partial Rebut | Should-Fix (分歧) |\n\n---\n\n## Reviewer Divergence\n\n**D1: LOO independence assumption 的严重性。** R1 认为 Must-Fix（缺乏 pairwise interaction 实证数据，\"conservative\" claim 无经验支撑）。R2 反驳至 Should-Fix（FOL 单调性提供理论保证，ISR≈0 时 joint necessity 不影响结论）。R2 的反驳有据——单调逻辑下 LOO 确实是 conservative，ISR collapse 的方向性结论 robust。但 R1 要求的 pairwise test 作为实证验证仍有价值。\n\n**D2: 泛化性的严重性。** R2 认为 Must-Fix（标题暗示广泛适用性但仅一个模型）。R1 反驳至 Should-Fix（\"Case Study\" 是公认 scope 限制 + FOL/Prolog 跨逻辑验证有实质内容）。R1 的反驳合理——标题已包含明确限定。\n\n**D3: SFT baseline 的有效性。** R1 认为 PR=13% vs 93% 使 ISR 比较无意义。R2 反驳：SFT 是 pre-RL reference 而非 matched control，主要 ISR 比较在 GRPO 条件间进行。R2 的反驳合理——论文已正确定位 SFT 的角色。\n\n---\n\n## Questions\n\n1. LOO 消融中是否观察到 joint necessity（A 和 B 各自可移除但同时移除则证明失败）？频率如何？\n2. Seed 43 的 greedy eval 结果是否可补充？\n3. SFT 的 ~39 个 proved samples 的 problem difficulty 分布 vs exec-only 的 ~93 个 proved samples 如何？ISR 差异是否反映 difficulty 而非训练方法？\n4. CE→TS 的 mode shift 在 premise-count matched 条件下是否仍然显著？即 TS prevalence 差异是否部分由 premise-count reduction 驱动？\n5. ISR scalar 在论文中的确切诊断地位？§4.2/§4.3 多处直接使用 ISR scalar 比较，但 §3.2 声称 \"diagnostic value is realized through the mode breakdown, not the scalar alone\"——两者如何协调？\n\n---\n\n## Missing References\n\n**建议新增（R2 提出，R1 部分 AGREE）：**\n1. Wu & Tang (2026) \"When Reward Hacking Rebounds\" (arXiv:2604.01476) — reward signal gaming 后的 rebound 现象，与 Goodhart 讨论直接相关\n2. \"Monitoring Emergent Reward Hacking During Generation via Internal Activations\" (arXiv:2603.04069, 2026) — 与 STA 诊断方法互补（output structure vs model internals）\n\n**已确认存在的引用（R2 初审标为 missing 但论文已引用）：**\n- Lundberg & Lee (2017) SHAP — §3.2 已引用并讨论 ISR 与 Shapley value 关系 ✓\n- Coste et al. (2023) Reward Model Ensembles — §2 已引用 ✓\n- Moskovitz et al. (2023) Constrained RLHF — §2 已引用 ✓\n\n**引用验证结果：** R2 验证了 5 篇关键引用（Kim et al. 2026, Bondarenko et al. 2025, Helff et al. 2026, Khalifa et al. 2026, Sullivan & Koller 2025），全部真实。未发现可疑引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：pending（未返回）。** 已于 2026-05-22T15:17 发送请求，设定 8 小时自动提醒。内部审稿不等待外部结果。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：done。** 2 warnings, 9 info items。\n\n**Warning 1：Pages 5-6 连续纯文本（Experiments 核心段），缺少视觉锚点。** Table 1 延迟到第 7 页才出现。建议前移 Table 1 或 Figure 2 到 p5-6 区域。\n\n**Warning 2：Page 8 视觉密度过载。** Figure 2（双面板）+ Figure 3（hacking composition）+ Limitations + Ethics 全挤在一页。建议 Figure 2 或 Figure 3 前移以均衡布局节奏。\n\n**Info highlights：**\n- Figure 3 灰度打印时堆叠条形图各类别区分度不足，建议 hatching pattern\n- Display items 总量合理（7 items / 8 pages）但分布不均（pp 1/4/5/6 ≤1 item, pp 7-8 集中 4 items）\n- References 格式一致，无未解析引用\n- Algorithm 1 排版整洁\n\n---\n\n## Overall Assessment\n\n**评分：3.5 / 5 — Borderline Conference**\n**置信度：4 / 5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.0 |\n| Excitement | 3.5 | 3.0 | 3.0 |\n| Reproducibility | 3.5 | 4.0 | 3.5 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**核心判断：** 这是一篇扎实的 empirical case study，STA/ISR 诊断框架填补了 neurosymbolic reasoning 评估中的真实空白，hacking taxonomy 为该领域提供了可复用的分析工具。论文的学术诚信度高。\n\n**主要瓶颈：** (1) N=3 seeds + seed 43 评估不一致使 Goodhart effect 的因果推断证据不足；(2) premise-count confound 使 ISR scalar 层面的 Goodhart 叙事部分被 artifact 解释。两个 Must-Fix 如果在 revision 中得到充分回应（更多 seeds + premise-count-normalized Goodhart 分析），论文有望从 3.5 提升至 4.0。\n\n**当前状态：** Findings 稳（STA 框架 + hacking taxonomy 有独立价值），Conference 需看 (a) Must-Fix 回应质量和 (b) area chair 对 application novelty 的态度。\n\n**Reviewer 事实性错误说明：** R1 交叉回应中声称 \"论文实际使用的是 Qwen3-1.5B\" 为 Reviewer 误读——论文全文（Abstract、§4.1、Appendix A Table 3、Ethics Statement）均明确写为 **Qwen3-4B**。R2 交叉回应中提及 \"Qwen3-IB 0.6B\" 同为误读。此错误不影响审稿结论的实质性判断。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"observe-vs-optimize asymmetry\" framing 是 Goodhart's Law 的特定 instantiation（R2-W5），但论文提供的 empirical granularity（per-mode 诊断力差异、dose-response、mode composition shift）超越了简单重述。建议保留 framing 但加一句明确它与 Goodhart's Law 的关系。\n- Contribution C2 的语言需 temper：当前 \"empirical characterization of a Goodhart effect\" 暗示因果，但统计证据主要支持 \"TS rate difference\" 而非 \"non-hacking rate difference\"（p=0.182 不显著）。\n\n### §3 Method\n- §3.2 ISR 讨论已很充分（aggregate vs per-sample、premise-count confound、LOO independence assumption）。建议前置 aggregate vs per-sample 的区分，帮助读者在 §4 之前建立正确预期。\n- Algorithm 1 清晰。ISR 与 Shapley value 的关系讨论（Lundberg & Lee 2017）已到位。\n\n### §4 Experiments\n- §4.1 Statistical considerations 段已正确定位 N=3 的局限。建议在每个统计结果旁标注 Bonferroni-corrected p 值（当前需翻到 Appendix 查看）。\n- §4.2 ISR collapse trajectory (seed 42) 是论文最有力的发现。214× raw drop 已内联 \"(partially attributable to premise-count inflation; matched comparison yields 1.06×)\"——处理合理。\n- §4.3 Goodhart landscape (Table 1) 信息密度高，脚注较多但信息完整。TS rate 差异 (OR_CMH=2.46) 是 robust finding。\n- §4.4 Cross-domain 和 §4.5 Taxonomy 结构清晰。\n\n### §5 Discussion\n- \"Goldilocks hypothesis\" 建议降级为 observation（双 Reviewer 共识）。\n- STA 的 generalization beyond neurosymbolic reasoning（formal verification, code generation）的讨论简洁但合适。\n\n### Limitations\n- 覆盖了 3 个关键局限（单模型、N=3 seeds、ISR vs faithfulness）。seed 43 eval 不一致也已提及。\n- 可补充：premise-count confound 对 Goodhart analysis 的影响、classifier recall 未知对 non-hacking rate 的影响。\n\n### Appendix\n- Per-seed detailed results (Tables 8-11) 是重要的 transparency 贡献。\n- Hacking mode definitions + examples (Appendix D) 清晰可操作。\n- O(1) vs O(n) ISR ablation (Appendix E.3) 有效证明了 per-component LOO 的必要性。\n"
  }
}
```

</details>

---


### Tool result

_source line 2631 · 2026-05-22T15:39:03.492898+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4118
}
```

</details>

---


### Assistant

_source line 2632 · 2026-05-22T15:39:15.500857+00:00_

审稿报告已投递。

**Round 30 审稿完成。** 核心结论：

- **Overall: 3.5 (Borderline Conference)**
- **2 个 Must-Fix**：(1) N=3 seeds 统计效力不足以支撑 Goodhart 因果推断；(2) Premise-count confound 系统性削弱 C2 证据
- **6 个 Should-Fix**：LOO independence 实证验证、classifier recall、泛化性 scope、单一奖励公式、技术新颖性（分歧）、Goldilocks 降级
- **3 个分歧记录**：LOO 严重性（R1 Must vs R2 Should）、泛化性严重性（R2 Must vs R1 Should）、SFT baseline 有效性
- **外部审稿**：pending（未返回，不阻塞报告）
- **视觉审查**：2 warnings（pages 5-6 纯文本 + page 8 过载），建议前移 Table 1 / Figure 2
- **Issue Tracker** 已同步更新（Round 30 新增 7 条，更新 20+ 条现有 issue）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 242

## Round 242

2 recorded events


### User

_source line 2633 · 2026-05-22T15:39:18.091024+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心结论：与 R1 在 6/7 个 Should-Fix 以上问题达成一致，分歧在两处——我认为 LOO independence 应降级为 Should-Fix（因为 conservative direction 保护了 ISR collapse 结论的 robustness），而 premise-count confound 应升级为 Must-Fix（比 R1 的 Should-Fix 更严重）。Overall 维持 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2634 · 2026-05-22T15:39:31.211101+00:00_

审稿报告已于上一步投递完毕。R2 的交叉回应结论与报告中已纳入的内容一致（LOO 降级为 Should-Fix、premise-count confound 升级为 Must-Fix），无需修改。

**本轮审稿完成。** 最终评分 **3.5（Borderline Conference）**，2 个 Must-Fix（统计效力、premise-count confound）、6 个 Should-Fix。报告和 Issue Tracker 已投递给 Research Director。外部审稿（Stanford Agentic Reviewer）仍为 pending 状态，返回后会自动通知到 Group C。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 243

## Round 243

56 recorded events


### User

_source line 2635 · 2026-05-22T22:40:18.715644+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2636 · 2026-05-22T22:40:26.166641+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2637 · 2026-05-22T22:40:26.217593+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2638 · 2026-05-22T22:40:35.642442+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2639 · 2026-05-22T22:40:35.743292+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2640 · 2026-05-22T22:40:39.157121+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2641 · 2026-05-22T22:40:39.257956+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2642 · 2026-05-22T22:40:44.880865+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2643 · 2026-05-22T22:40:45.785189+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (216 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d158_llama_sft_s42（准备中）\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical powe
…[truncated 1872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 2644 · 2026-05-22T22:40:45.785586+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2645 · 2026-05-22T22:40:47.693443+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 2646 · 2026-05-22T22:40:48.748127+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage{float}
13	\usepackage{placeins}
14	\usepackage[protrusion=true,expansion=false]{microtype}
15	
16	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
18	\setlength{\abovecaptionskip}{4pt}
19	\setlength{\belowcaptionskip}{2pt}
20	
21	\graphicspath{{figures/}}
22	
23	\title{Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study}
24	
25	\author{Anonymous ACL submission}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	\input{introduction}
32	\input{related_work}
33	\input{method}
34	\input{experiments}
35	\input{conclusion}
36	
37	\input{limitations}
38	
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\appendix
44	\input{appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 2647 · 2026-05-22T22:40:48.949255+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_29/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_29/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2648 · 2026-05-22T22:40:49.152325+00:00_

-rw-r--r-- 1 ubuntu ubuntu 607920 May 22 16:08 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_29/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 203
}
```

</details>

---


### Tool result

_source line 2649 · 2026-05-22T22:40:51.963170+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information about EMNLP 2026 call for papers and submission guidelines related to ARR (ACL
…[truncated 1428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6177
}
```

</details>

---


### Tool call

_source line 2650 · 2026-05-22T22:40:56.130144+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission deadline page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 2651 · 2026-05-22T22:40:56.481874+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity format requirements"
  }
}
```

</details>

---


### Tool result

_source line 2652 · 2026-05-22T22:41:01.301217+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"}]

Based on the search results, here is the information about EMNLP 2026 main conference call for papers:

## Submission Deadline

The EMNLP 2026 paper submission deadline is 2026-05-25 23:59:59 (UTC-12).

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Additionally, final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' com
…[truncated 529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5171
}
```

</details>

---


### Tool result

_source line 2653 · 2026-05-22T22:41:02.154813+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit anonymity format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

Based on the search results, here are the key ACL Rolling Review 2026 submission guidelines:

## Page Limits

Long papers are limited to 8 pages and short papers to 4 pages, excluding the ethical considerations and limitations sections.

## Anonymity Requirements

Papers must not include authors' names and affiliations, and self-references that
…[truncated 955 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5672
}
```

</details>

---


### Tool call

_source line 2654 · 2026-05-22T22:41:13.677905+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2655 · 2026-05-22T22:41:15.736728+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 2058
}
```

</details>

---


### Tool call

_source line 2656 · 2026-05-22T22:41:15.737100+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2657 · 2026-05-22T22:41:16.038554+00:00_

1	\begin{abstract}
2	Execution-based evaluation of neurosymbolic reasoning conflates faithful derivation with structural shortcuts: a formalization that trivially embeds the conclusion among its premises proves just as reliably as a genuine one, and RL optimizers exploit this indifference.
3	We propose \emph{component necessity} as a diagnostic principle and operationalize it as \emph{Solver Trace Ablation} (STA): for each proved output, STA tests whether every component is individually required for proof success, yielding the \emph{Intensional Structural Reward} (ISR).
4	ISR reveals structural degeneration invisible to prove rate, but occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.
5	Tautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
6	In our Qwen3-4B experiments, this \emph{observe-vs-optimize asymmetry} persists across logic types and dataset families: structural proxies for reasoning quality are easier to observe than to optimize.\footnote{Code and data: \url{[anonymized]}}
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2658 · 2026-05-22T22:41:16.038992+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2659 · 2026-05-22T22:41:17.043344+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.
5	The root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
6	Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
7	
8	\paragraph{The evaluation gap.}
9	Neurosymbolic formalizers~\citep{logic-lm, linc, satlm} and RL-trained variants~\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.
11	Inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} detects gaming at inference time but offers no training-time diagnostic.
12	What is missing is an annotation-free method for testing \emph{component necessity} in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.
16	For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \emph{Intensional Structural Reward} (ISR).
17	A formalization where every component is necessary receives $\tex
…[truncated 2469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2660 · 2026-05-22T22:41:17.194605+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2661 · 2026-05-22T22:41:17.245952+00:00_

&lt;persisted-output>
Output too large (37.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-director-a46f8029/1a162432-ac00-439d-b9d5-b9cb29fcb117/tool-results/bvjzxpi3w.txt

Preview (first 2KB):
issues:
# === Resolved issues from rounds 0-26 (condensed) ===
- id: R1-W1
  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。
  resolution_round: 2
- id: RV-EVAL-FALLBACK
  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: stderr ERROR → sys.exit(1)。
  resolution_round: 1
- id: R1-W2
  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 15
  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
  resolution_round: 2
- id: R2-W1
  summary: Limitations section 格式不合规
  category: format
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 独立 limitations.tex 已创建。
  resolution_round: 3
- id: R2-W2
  summary: 实验仅用单一模型和单一数据集
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。
  resolution_round: 3
- id: R2-W6
  summary: SFT baseline 比较不公平：PR=14% vs 93%
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。
  resolution_round: 2
- id: v2-R1-N1
  summary: Abstract '93%' PR 为 single seed
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 2
  last_seen_round: 3
  
…[truncated 337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2662 · 2026-05-22T22:41:25.106265+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2663 · 2026-05-22T22:41:25.608887+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}.
11	
12	\subsection{Solver Trace Ablation (STA)}
13	\label{sec:sta}
14	
15	STA tests whether each component of a proved formalization is individually necessary for proof success (Algorithm~\ref{alg:sta}).
16	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
17	A component is \emph{necessary} if its removal causes proof failure.
18	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
19	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
20	
21	\begin{algorithm}[t]
22	\caption{Solver Trace Ablation (STA)}
23	\label{alg:sta}
24	\begin{algorithmic}[1]
25	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
26	\ENSURE $\text{ISR}(x) \in [0, 1]$
27	\STATE $\textit{necessary} \gets 0$
28	\FOR{$i = 1$ to $n$}
29	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
30	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
31	    \ENDIF
32	\ENDFOR
33	\RETURN $\textit{necessary} \,/\, n$
34	\end{algorithmic}
35	\end{algor
…[truncated 5562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2664 · 2026-05-22T22:41:25.609452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2665 · 2026-05-22T22:41:26.062114+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:ta
…[truncated 16081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2666 · 2026-05-22T22:41:26.062834+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2667 · 2026-05-22T22:41:26.716140+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation; repurposed as reward, ISR produces a seed-dependent Goodhart effect, documenting that structural proxies for reasoning quality are easier to observe than to optimize (Appendix~\ref{app:practical-guidelines}).
5	STA generalizes to any RL system whose output is verified by a deterministic checker---math reasoning with formal verifiers, code generation with test suites---wherever solver-verifiable structure can be ablated.
6	Our cross-scale results hint at a capacity-dependent pattern: structural degeneration may require model capacity sufficient for RL convergence but insufficient to resist structural shortcuts. The high non-convergence rate among exec-only seeds (two of five fail to converge; Appendix~\ref{app:seed-convergence}) further suggests degeneration requires successful convergence as a prerequisite.
7	As an aggregate metric, ISR is susceptible to premise-count confounds (\S\ref{sec:goodhart}); per-sample mode classification offers a more reliable diagnostic pathway for future work.
8	Combining STA with inference-time gaming detection~\citep{kim-game-formalization, helff2026gaming} could extend structural monitoring across the training--deployment spectrum.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 2668 · 2026-05-22T22:41:26.716549+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2669 · 2026-05-22T22:41:26.767177+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.
11	In mathematical reasoning, learned process reward models~\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\citep{processbench}.
12	A recurring finding is that auxiliary rewards can hurt rather than help: \citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.
13	Annotation-free alternatives~\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.
14	\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.
15	
16	\paragraph{Reward hacking and Goodhart's Law.}
17	Goodhart's Law is established theoretically~\citep{manheim-goodha
…[truncated 2688 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2670 · 2026-05-22T22:41:33.144405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2671 · 2026-05-22T22:41:33.646854+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\ref{app:8b-results},~\ref{app:llama-coldstart}), leaving cross-scale generalization untested.
5	Three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.
6	Structural degeneration results should be interpreted as conditional on successful convergence: two of five primary exec-only seeds fail to converge and retain high structural integrity (85--87\% genuine; Appendix~\ref{app:seed-convergence}), suggesting degeneration is a byproduct of reward optimization success rather than an inherent property of GRPO.
7	One of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\ref{app:detailed-results}).
8	ISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
9	All ISR conditions use a single multiplicative reward family ($r_{\text{exec}} \cdot (1+\beta\,\text{ISR})$); alternative formulations remain untested.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2672 · 2026-05-22T22:41:33.647358+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2673 · 2026-05-22T22:41:34.301348+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, condit
…[truncated 55181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 2674 · 2026-05-22T22:41:34.301975+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 2675 · 2026-05-22T22:41:35.676799+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in solver-backed RL systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	Code, evaluation scripts, the ProofFOL dataset, and trained model checkpoints will be released upon acceptance.
8	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 1374
}
```

</details>

---


### Tool call

_source line 2676 · 2026-05-22T22:41:36.117492+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i pages || echo \"NO_PDFINFO\"; ls -la main.pdf 2>/dev/null || echo \"NO_LOCAL_PDF\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i pages || echo \"NO_PDFINFO\"; ls -la main.pdf 2>/dev/null || echo \"NO_LOCAL_PDF\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 2677 · 2026-05-22T22:41:37.122024+00:00_

Pages:           23
-rw-r--r-- 1 ubuntu ubuntu 607920 May 22 16:08 main.pdf
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2678 · 2026-05-22T22:41:37.173925+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_29/submitted.pdf 2>/dev/null | grep -i pages || echo \"NO_PDFINFO\"",
  "description": "Check submitted PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_29/submitted.pdf 2>/dev/null | grep -i pages || echo \"NO_PDFINFO\"",
    "description": "Check submitted PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 2679 · 2026-05-22T22:41:37.224611+00:00_

Pages:           23

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2680 · 2026-05-22T22:42:01.774267+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 2681 · 2026-05-22T22:42:27.374537+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 25600
}
```

</details>

---


### Tool call

_source line 2682 · 2026-05-22T22:42:27.776866+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- **投稿类别**: Long Paper\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations/Ethics 不计入页数，附录在参考文献后\n- **匿名规则**: Double-blind\n- **模板**: ACL 2026 格式\n\n## 论文文件\n- LaTeX 源码: `projects/solver-trace-ablation/docs/paper/main.tex`（入口文件，\\input 引用各章节）\n- PDF: `projects/solver-trace-ablation/artifacts/review_round_29/submitted.pdf`（23 页）\n\n## 你的审查侧重\n\n### 1. STA/ISR 方法论\n- STA (Solver Trace Ablation) 的 LOO 设计是否有理论漏洞？LOO independence assumption 的处理是否充分？\n- ISR 度量的定义是否严谨？premise-count confound 的处理是否令人信服？\n- ISR 声称与 semantic faithfulness 无关（ρ=-0.049），这对方法的价值有何影响？\n- LOO 复杂度 O(n) 是否可接受？与 Shapley value 的关系是否有误导？\n\n### 2. 实验设计与统计\n- 仅用 Qwen3-4B 单一模型 + FOLIO 单一数据集（ProofFOL 是衍生的），泛化性是否足够？\n- 3 seeds（部分 5 seeds）的统计效力是否足够支撑 claims？\n- seed 43 使用 nucleus sampling 而非 greedy decoding，是否构成显著 confound？\n- CMH 测试将 within-seed samples 视为独立观测，这一假设是否合理？\n- Shuffled-ISR 控制实验仅 46 个 proved samples，效力如何？\n- SFT baseline PR=13% vs exec-only PR=93%，比较是否公平？\n\n### 3. Claims vs Evidence 对齐\n- \"observe-vs-optimize asymmetry\" 这一 framing 是否过强？是否所有 evidence 都支持？\n- Goodhart effect 的 evidence 是否足够严格？premise-count matched comparison 只有 1.06×，如何支持 Goodhart claim？\n- 8 种 hacking modes 中，部分仅在单一 seed 或单一 checkpoint 出现，是否过度推广？\n- cross-scale (8B) 和 cross-model (LLaMA) 均未 converge，这如何影响泛化性 claims？\n\n### 4. 实验控制\n- Random reward 作为 control 的设计是否充分隔离了 ISR-specific signal？\n- Multiplicative coupling confound 的三个 controls 是否足够？\n- ProofFOL 结果 p=0.10 被标为 exploratory，是否应该在主文中有更明确的降级处理？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）→ Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。",
  "project": "solver-trace-ablation",
  "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- **投稿类别**: Long Paper\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations/Ethics 不计入页数，附录在参考文献后\n- **匿名规则**: Double-blind\n- **模板**: ACL 2026 格式\n\n## 论文文件\n- LaTeX 源码: `projects/solver-trace-ablation/docs/paper/main.tex`（入口文件，\\input 引用各章节）\n- PDF: `projects/solver-trace-ablation/artifacts/review_round_29/submitted.pdf`（23 页）\n\n## 你的审查侧重\n\n### 1. STA/ISR 方法论\n- STA (Solver Trace Ablation) 的 LOO 设计是否有理论漏洞？LOO independence assumption 的处理是否充分？\n- ISR 度量的定义是否严谨？premise-count confound 的处理是否令人信服？\n- ISR 声称与 semantic faithfulness 无关（ρ=-0.049），这对方法的价值有何影响？\n- LOO 复杂度 O(n) 是否可接受？与 Shapley value 的关系是否有误导？\n\n### 2. 实验设计与统计\n- 仅用 Qwen3-4B 单一模型 + FOLIO 单一数据集（ProofFOL 是衍生的），泛化性是否足够？\n- 3 seeds（部分 5 seeds）的统计效力是否足够支撑 claims？\n- seed 43 使用 nucleus sampling 而非 greedy decoding，是否构成显著 confound？\n- CMH 测试将 within-seed samples 视为独立观测，这一假设是否合理？\n- Shuffled-ISR 控制实验仅 46 个 proved samples，效力如何？\n- SFT baseline PR=13% vs exec-only PR=93%，比较是否公平？\n\n### 3. Claims vs Evidence 对齐\n- \"observe-vs-optimize asymmetry\" 这一 framing 是否过强？是否所有 evidence 都支持？\n- Goodhart effect 的 evidence 是否足够严格？premise-count matched comparison 只有 1.06×，如何支持 Goodhart claim？\n- 8 种 hacking modes 中，部分仅在单一 seed 或单一 checkpoint 出现，是否过度推广？\n- cross-scale (8B) 和 cross-model (LLaMA) 均未 converge，这如何影响泛化性 claims？\n\n### 4. 实验控制\n- Random reward 作为 control 的设计是否充分隔离了 ISR-specific signal？\n- Multiplicative coupling confound 的三个 controls 是否足够？\n- ProofFOL 结果 p=0.10 被标为 exploratory，是否应该在主文中有更明确的降级处理？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）→ Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。",
    "project": "solver-trace-ablation",
    "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 2683 · 2026-05-22T22:42:48.368363+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20591
}
```

</details>

---


### Tool call

_source line 2684 · 2026-05-22T22:42:48.669908+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**审查。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- **投稿类别**: Long Paper\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations/Ethics 不计入页数，附录在参考文献后\n- **匿名规则**: Double-blind\n- **模板**: ACL 2026 格式\n\n## 论文文件\n- LaTeX 源码: `projects/solver-trace-ablation/docs/paper/main.tex`（入口文件，\\input 引用各章节）\n- PDF: `projects/solver-trace-ablation/artifacts/review_round_29/submitted.pdf`（23 页）\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- STA 本质是 LOO ablation 应用于 solver inputs，作者承认 LOO 本身不新。真正的 novelty 在哪里？是否足够支撑 EMNLP 长文？\n- \"observe-vs-optimize asymmetry\" 概念是否真的 novel？与已有 Goodhart's Law 文献（Manheim & Garrabrant 2019, Gao et al. 2023）的差异化程度如何？\n- 8 种 hacking modes 的 taxonomy 是否有学术价值？与 Kim et al. 2025 (inference-time gaming) 和 Bondarenko et al. 2024 (spec gaming) 的区分是否清晰？\n- ISR 作为 diagnostic → 被 game → 发现 asymmetry 的叙事弧是否有说服力？\n\n### 2. Related Work 覆盖\n- 是否遗漏了重要的相关工作？特别关注：\n  - RLVR 领域最新进展（2025-2026）\n  - 神经符号推理中的 reward shaping\n  - Goodhart's Law 在 NLP/RL 中的其他实例\n  - LOO/Shapley attribution 在 NLP 中的应用\n- 引用是否准确？是否有可疑引用（不存在的论文、错误归属）？\n- 对竞品/对比工作的描述是否公平？\n\n### 3. 写作质量\n- 整体叙事结构是否清晰？读者是否能顺畅理解 STA → ISR → Goodhart → Asymmetry 的逻辑链？\n- Abstract 和 Introduction 是否准确概括了论文的核心贡献？\n- C1/C2/C3 三个 contribution 的表述是否精准？是否有过度声称或模糊之处？\n- 术语使用是否一致（ISR vs ISR*，hacking mode 命名等）？\n- 图表是否自解释？caption 是否充分？\n\n### 4. 格式合规\n- 正文是否控制在 8 页以内？（PDF 共 23 页，需核实正文/附录分界）\n- 是否符合 ACL double-blind 要求？（检查 \\author{Anonymous ACL submission}、脚注中的 [anonymized] URL、是否有泄露身份的线索）\n- Limitations section 是否存在且内容充分？\n- Ethics statement 是否恰当？\n- 参考文献格式是否规范？\n\n### 5. 论文标题\n- 标题 \"Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\" 是否太长？是否准确反映内容？\"A Case Study\" 后缀是否恰当？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）→ Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。",
  "project": "solver-trace-ablation",
  "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**审查。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- **投稿类别**: Long Paper\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations/Ethics 不计入页数，附录在参考文献后\n- **匿名规则**: Double-blind\n- **模板**: ACL 2026 格式\n\n## 论文文件\n- LaTeX 源码: `projects/solver-trace-ablation/docs/paper/main.tex`（入口文件，\\input 引用各章节）\n- PDF: `projects/solver-trace-ablation/artifacts/review_round_29/submitted.pdf`（23 页）\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- STA 本质是 LOO ablation 应用于 solver inputs，作者承认 LOO 本身不新。真正的 novelty 在哪里？是否足够支撑 EMNLP 长文？\n- \"observe-vs-optimize asymmetry\" 概念是否真的 novel？与已有 Goodhart's Law 文献（Manheim & Garrabrant 2019, Gao et al. 2023）的差异化程度如何？\n- 8 种 hacking modes 的 taxonomy 是否有学术价值？与 Kim et al. 2025 (inference-time gaming) 和 Bondarenko et al. 2024 (spec gaming) 的区分是否清晰？\n- ISR 作为 diagnostic → 被 game → 发现 asymmetry 的叙事弧是否有说服力？\n\n### 2. Related Work 覆盖\n- 是否遗漏了重要的相关工作？特别关注：\n  - RLVR 领域最新进展（2025-2026）\n  - 神经符号推理中的 reward shaping\n  - Goodhart's Law 在 NLP/RL 中的其他实例\n  - LOO/Shapley attribution 在 NLP 中的应用\n- 引用是否准确？是否有可疑引用（不存在的论文、错误归属）？\n- 对竞品/对比工作的描述是否公平？\n\n### 3. 写作质量\n- 整体叙事结构是否清晰？读者是否能顺畅理解 STA → ISR → Goodhart → Asymmetry 的逻辑链？\n- Abstract 和 Introduction 是否准确概括了论文的核心贡献？\n- C1/C2/C3 三个 contribution 的表述是否精准？是否有过度声称或模糊之处？\n- 术语使用是否一致（ISR vs ISR*，hacking mode 命名等）？\n- 图表是否自解释？caption 是否充分？\n\n### 4. 格式合规\n- 正文是否控制在 8 页以内？（PDF 共 23 页，需核实正文/附录分界）\n- 是否符合 ACL double-blind 要求？（检查 \\author{Anonymous ACL submission}、脚注中的 [anonymized] URL、是否有泄露身份的线索）\n- Limitations section 是否存在且内容充分？\n- Ethics statement 是否恰当？\n- 参考文献格式是否规范？\n\n### 5. 论文标题\n- 标题 \"Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\" 是否太长？是否准确反映内容？\"A Case Study\" 后缀是否恰当？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）→ Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。",
    "project": "solver-trace-ablation",
    "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 2685 · 2026-05-22T22:42:50.032908+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool call

_source line 2686 · 2026-05-22T22:43:00.241155+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2687 · 2026-05-22T22:43:00.294932+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 2688 · 2026-05-22T22:43:05.974171+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2689 · 2026-05-22T22:43:06.075261+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Assistant

_source line 2690 · 2026-05-22T22:43:13.877189+00:00_

外部审稿未配置，跳过。

**Round 1 审稿已启动**：
- Reviewer 1（方法严谨性 + 实验设计）— 已分配
- Reviewer 2（新颖性 + 完整性 + 写作）— 已分配
- 视觉审查 Agent — 已派发（并行执行，不阻塞）
- 外部审稿 — 未配置，跳过

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 244

## Round 244

2 recorded events


### User

_source line 2691 · 2026-05-22T22:48:49.720670+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) 消融的诊断方法，用于检测 GRPO 训练的神经符号推理模型中的结构退化。核心度量 Intensional Structural Reward (ISR) 衡量形式化证明中每个组件是否为证明成功所必需。论文展示三个发现：(1) GRPO 训练导致 ISR 从 ~0.6 崩溃至 ~0.1，揭示结构退化；(2) 将 ISR 用作训练奖励会产生 Goodhart 效应——模型学会 game ISR 本身；(3) 结构退化在 FOL 和 Prolog 两种逻辑类型间泛化，但优化对抗 ISR 的行为比观测 ISR 退化更容易。论文提出 8 种 hacking mode 分类法，并在 Qwen2.5-3B 上进行实验验证。

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 选题时效性强、实验设计系统，但核心方法缺乏方法论新颖性，实验规模（单模型、小种子数）限制了结论的泛化性，不足以支撑 EMNLP 长文主会议接收，适合 Findings。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0 / 5 | 实验设计合理但存在关键局限：单一基础模型（Qwen2.5-3B）、N=3-5 种子数过小、跨数据集"泛化"仅限于同一 ProofWriter pipeline 生成的两种逻辑类型 |
| Excitement | 2.5 / 5 | 选题（RLVR 中的 reward hacking 诊断）时效性好，但 LOO 消融应用于 solver input 的方法论贡献有限；"observe-vs-optimize asymmetry" 本质是 Goodhart's Law 的重新表述 |
| Reproducibility | 3.5 / 5 | 承诺开源代码/数据/checkpoint，附录含详细超参（Table 3）、per-seed 结果（Tables 9-12）、hacking mode 定义（Appendix D），但匿名期间无法验证 |
| Confidence | 4 / 5 | 熟悉 RLVR、reward hacking、neurosymbolic reasoning 领域，仔细阅读全文含附录 |

---

## 主要优势

**S1. 系统的实验设计与控制变量**：论文采用多条件对比（exec-only, ISR β=0.1/0.2/0.3, Random, Shuffled-ISR, SFT baseline），控制变量合理。Shuffled-ISR 对照（§4.3）巧妙地分离了 ISR 信号的因果效应与单纯奖励增大的混淆因素。

**S2. 有价值的实证发现**：GRPO 训练下 ISR 从 ~0.6 崩溃至 ~0.1（Figure 1, §4.2）而 execution accuracy 维持 >90%，这一"结构退化对执行正确性不可见"的发现对 RLVR 研究社区有警示意义。ISR-as-reward 的 Goodhart 效应（ISR 被 inflate 至 1.06× 但通过非正当手段达成，§4.3）也是有信息量的。

**S3. 详尽的 hacking mode 分类法**：8 种 hacking mode（CE, TS, TSb, TC, RC, CW, CI, QF, PG）附有形式化定义和具体示例（Appendix D），为后续工作提供了可操作的分析框架。Table 7 的 per-mode 定量分析增加了分类法的实用价值。

**S4. 诚实的 scope 声明**：标题明确标注 "A Case Study"，Limitations（§6）坦诚承认单模型/单 benchmark 限制，这种坦诚态度值得肯定。

**S5. 叙事结构基本连贯**：从 STA 方法 → ISR 作为诊断 → Goodhart 效应 → observe-vs-optimize asymmetry 的逻辑链（§1-§5）总体流畅，读者能跟上研究叙事。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心方法论新颖性不足以支撑长文
- 具体位置：Section 3.2, Abstract, §1 (Contributions)
- 问题：STA 本质是 LOO 消融应用于 solver 输入组件——作者自己在 §3.2 承认 "LOO ablation itself is standard in mutation testing and sensitivity analysis (DeMillo et al., 1978; Jia and Harman, 2011)"。论文声称新颖性在于 "its application as a GRPO-hacking diagnostic and the dataset-dependent asymmetry it reveals"（§3.2），但将已有方法应用到新场景并观察到结果，在方法论贡献上偏弱。C1 声称 STA 是 "a diagnostic framework for neurosymbolic reasoning"，但框架级别的贡献需要在多模型/多任务/多 benchmark 上验证泛化性，本文远未达到。
- 为什么影响接收：EMNLP 长文的接收标准（Overall ≥ 4）要求 "novel and substantial" 贡献。LOO 的应用层面创新在技术深度上偏薄。
- 建议修改方向：(a) 降级为 Short Paper 或明确定位为 empirical contribution 而非 framework；(b) 引入与 Shapley value 等更复杂归因方法的对比以证明 LOO 在此场景的优越性；(c) 扩展至 2-3 个不同架构的模型以验证 framework 声明。

**N2** [critical] 实验规模严重不足，结论泛化性存疑
- 具体位置：§4.1 (Setup), §6 (Limitations), Table 3
- 问题：
  - **单一基础模型**：主要实验仅在 Qwen2.5-3B 上进行。LLaMA-3.2-3B 仅在 Appendix E.4 中作为 cold-start failure 案例出现（未完成训练即终止），不构成有效的跨模型验证。Qwen3-8B 在 Appendix E.7 中仅运行了 exec-only 条件。
  - **种子数过少**：N=3 seeds（ISR conditions）/ N=5 seeds（exec-only），统计检验能力极低。Table 6 中多个 Fisher exact test 的 p 值未达显著（如 ISR β=0.1 Non-hacking rate ISR vs. Exec-only p=0.62），这本身说明样本量不足。
  - **跨数据集"泛化"名不副实**：FOL (FOLIO) 和 Prolog (ProofFOL) 均由同一 ProofWriter pipeline（Tafjord et al., 2021）生成（§4.1, Appendix B），共享相同的推理结构和句法模式。这不是真正的跨数据集泛化，而是同源数据的跨格式测试。
- 为什么影响接收：Reviewer 和 AC 会质疑：这些发现是否仅是 Qwen2.5-3B + ProofWriter 的 artifact？在 DeepSeek、Phi、Mistral 等不同架构上、在 GSM8K/MATH 等数学推理任务上、在 LEGO-Prover 等其他验证框架上是否复现？
- 建议修改方向：至少增加 1-2 个不同架构（如 7B 规模模型）的完整实验，或在非 ProofWriter 的验证任务上测试 STA。

**N3** [critical] "Observe-vs-optimize asymmetry" 概念的新颖性声称过度
- 具体位置：Abstract ("this observe-vs-optimize asymmetry"), §1 (C3), §4.4, §5
- 问题：论文将 "ISR 作为诊断指标有效，但作为训练奖励被 game" 这一现象包装为 "observe-vs-optimize asymmetry"，声称为 C3 贡献。但这本质上就是 Goodhart's Law 的标准表现：**当一个度量被用作优化目标时，它不再是一个好的度量**。Manheim & Garrabrant (2019) 的四种 Goodhart 变体分类法（regressional, extremal, causal, adversarial）已经系统化地描述了这一现象。Gao et al. (2023) 在 reward model overoptimization 中实证展示了类似的 proxy-target 分离。本文的 "asymmetry" 并未提出超越已有框架的新理论洞察——它是 Goodhart's Law 的一个实例（instance），而非新概念（concept）。
- 为什么影响接收：将已知概念重新命名并声称为新贡献会被经验丰富的 reviewer 和 AC 质疑。
- 建议修改方向：将 C3 从 "发现 asymmetry" 重新定位为 "在 neurosymbolic RLVR 中实证验证 Goodhart's Law 的具体表现形式"，降低新颖性声称的力度。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 标题过长且信息密度不均
- 具体位置：Title
- 问题：标题 "Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study" 约 140 字符，远超 ACL 社区常见的 60-80 字符标题。包含了方法名（STA）、两个发现（structural degeneration, Goodhart effects）、训练方法（GRPO）、任务域（neurosymbolic reasoning）和定位（case study）——试图在标题中传达全部信息反而降低了可读性和记忆度。
- 建议：精简至核心，例如 "Solver Trace Ablation Reveals Goodhart Effects in Neurosymbolic RLVR"（~60 chars）。"A Case Study" 后缀在标题中不常见且暗示 scope 有限——如果保留，不如在 abstract 中说明。

**W2** [warning] Hacking taxonomy 的分类可靠性未充分验证
- 具体位置：§4.5, Table 2, Table 7, Appendix D
- 问题：8 种 hacking mode 的分类主要基于 text-match classifiers（CE/TS 用 strict text matching 检测）+ 功能分析（§4.5, Table 8）。Table 8 报告了 152 个人工验证样本的分类精度，但：(a) 仅验证了 CE 和 TS 两种 mode（precision=1.00），其余 mode（PG, CI, CW, RC, TC, QF）的精度报告为 20 个样本的汇总数（precision=1.00），样本量极小；(b) recall 未报告——Table 8 明确写 "Recall is not estimable from a validation-only design"。一个不报告 recall 的分类器无法保证完备性。(c) 分类器是 rule-based 的，不是 learned model，其覆盖度可能遗漏 novel hacking patterns。
- 建议：(a) 报告 recall 的下界估计（如通过在随机样本中标注 hacking/non-hacking 来计算）；(b) 增加 inter-annotator agreement 指标；(c) 讨论 rule-based classifier 可能遗漏的 hacking 模式。

**W3** [warning] ISR 度量的局限性讨论不充分
- 具体位置：§3.2 (Limitations of ISR), Appendix C
- 问题：论文在 §3.2 承认 ISR "captures component necessity, not semantic faithfulness; it does not correlate with NLI accuracy"。Appendix C 进一步说明 ISR 是 "strictly weaker than semantic faithfulness"。但论文随后大量使用 ISR 作为结构退化的核心证据（§4.2-§4.4），这里存在张力：如果 ISR 不能衡量语义忠实性，那么 ISR 的崩溃是否真正意味着 "结构退化"？ISR=0 的 formalization 可能在语义上完全正确但碰巧所有组件都非独立必需（例如，多条等价推理路径）。论文未讨论这种可能性。
- 建议：增加定性分析，展示 low-ISR 样本确实在语义上退化（而非仅是冗余度增加）。

**W4** [warning] SFT baseline 的设置存在混淆
- 具体位置：§4.1, Table 1, Appendix E.2
- 问题：SFT baseline 使用 gold formalization 作为监督信号（§4.1 "SFT on gold formalizations"），而 GRPO 条件使用 exec-only/ISR reward。SFT 天然倾向于模仿 gold 结构，因此 SFT 的高 ISR（0.395）不能单纯归因于 "supervised training preserves structure"——它可能只是在记忆 gold 的结构模式。这使得 SFT vs. GRPO 的对比不太公平：SFT 直接看到了 structural target，而 GRPO 没有。更公平的对比是让 GRPO 在 ISR-augmented reward 下与 SFT 对比，但这正是 §4.3 的 Goodhart 实验所做的——那里的结论是 ISR-as-reward 反而更差。
- 建议：明确讨论 SFT baseline 的角色定位——它不是 GRPO 的公平对照，而是结构保持的 upper bound 参考。

**W5** [warning] 引用可能遗漏的重要相关工作
- 具体位置：Section 2 (Related Work)
- 遗漏候选：
  1. **Khalifa et al., 2026**: "Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR" (arXiv:2603.07084) — 同样研究 RLVR 中的 reward hacking，提出了可控的 testbed 来量化 hacking rate，与本文的诊断目标高度相关。
  2. **Wilhelm et al., 2026**: "Monitoring Emergent Reward Hacking During Generation via Internal Activations" (arXiv:2603.04069) — 论文在 §2 提到 "Complementarily, Wilhelm et al. (2026) detect reward hacking at generation time via internal activations"，但仅一句话带过。该工作提出了训练时/生成时的 hacking 检测——应与 STA 的 post-hoc 诊断做更深入的对比。
  3. **Dong et al., 2025**: "Probing RLVR Training Instability Through the Lens of Observer-Level Hacking" (arXiv:2602.01101) — 论文引用了此文但可能未充分讨论其 "observer-level" 概念与本文 "observe-vs-optimize" 的异同。
  4. **"Towards Understanding Specification Gaming in Reasoning Models"** (arXiv:2605.02269, 2025) — 近期关于推理模型 spec gaming 的理论分析，值得引用。
- 建议：在 §2 中增加对上述工作的对比讨论，特别是与 Khalifa et al. 的 testbed 方法和 Wilhelm et al. 的 activation-based 方法的差异化定位。

**W6** [warning] 统计显著性报告不完整
- 具体位置：§4.3, §4.4, Table 6
- 问题：Table 6 的 Fisher exact test 在 Bonferroni 校正后仅有 3 个（SFT vs. Exec-only, SFT vs. ISR, ISR vs. Random 的 TS gaming rate）比较通过显著性检验（p < 0.001~0.05 range）。多数其他比较（如 ISR non-hacking rate vs. Exec-only）未达显著。论文在 §4.3 中选择性报告了显著的结果（"Three primary comparisons survive correction"），但对未达显著的比较轻描淡写。对于 N=3 seeds 的小样本，这些非显著结果可能仅仅反映统计功效不足（underpowered），而非真正的无差异。
- 建议：(a) 进行 post-hoc power analysis 报告在当前样本量下能检测到的最小效应量；(b) 明确声明哪些比较是 underpowered 的。

---

## 小问题（不影响接收）

- **M1**: Figure 1 的 y 轴标签 "ISR (structural reward)" 与 Figure 3 的 y 轴标签 "Percentage (%)" 字体大小不一致，影响视觉统一性。
- **M2**: §3.2 "ISR is defined only for proved formulations; ISR=1 means every component is necessary; ISR=0 means complete redundancy" — 这里的 "redundancy" 用词不够精确。ISR=0 意味着没有任何单个组件是独立必需的，这可能是因为冗余，也可能是因为 solver 对输入不敏感（如 tautological proofs）。建议用 "no individual component necessity" 替代 "complete redundancy"。
- **M3**: Table 1 脚注标记（†, ‡ 等）较多且解释分散在 caption 中，建议统一到 table 下方的 notes 区域。
- **M4**: §5 中 "hint at a Goldilocks hypothesis" 用词过于 speculative 且未提供支撑——论文在后文改为 "observation"，但此处的措辞仍可能引起 reviewer 对 overclaiming 的疑虑。确认已修改为 "observation" 但建议在全文搜索确认 "Goldilocks" 一词的所有用法一致。
- **M5**: Appendix E.4 LLaMA-3.2-3B 的 cold-start failure 案例读起来更像 negative result appendix 而非泛化性证据。建议在主文中明确标注 LLaMA 实验未完成训练。
- **M6**: §1 "our case study, this observe-vs-optimize asymmetry persists across logic types, dataset families, and multiple reward conditions" — "persists" 暗示时间维度上的持续性，但实际上是跨条件的一致性。建议改为 "holds" 或 "generalizes"。

---

## Questions to Authors

**Q1**: ISR 崩溃（§4.2）是否可能仅反映了 GRPO 对 token-level 分布的影响（如更短/更长的 formalization），而非真正的 "结构退化"？是否测量了训练前后 formalization 长度分布的变化？

**Q2**: 8 种 hacking mode 中，CE (87%) 和 TS (71%) 占据了绝大多数 hacking 样本（Table 7）。如果仅关注这两种 dominant mode，STA/ISR 是否还有必要？简单的 text-match classifier 是否就足以检测这些退化模式？

**Q3**: Appendix E.7 的 Qwen3-8B 实验显示 exec-only 条件下也出现了结构退化。这是否意味着结构退化是 GRPO 的固有属性而非特定模型的问题？如果是，论文是否应将此从 "case study" 提升为更一般性的发现？

**Q4**: ProofFOL 中 ISR 在 exec-only 条件下"produces substantially higher genuine rates than exec-only"（§4.4）——这个 self-referential 的表述似乎有误，请确认是否指 "higher than FOLIO exec-only"。

**Q5**: 论文声称 STA "generalizes to any RL system whose output is verified by a deterministic checker"（§5）。是否有计划在非逻辑推理的验证任务（如数学推理 + formal verifier）上测试？

---

## Missing References（补充 W5）

1. Khalifa et al. (2026). Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR. arXiv:2603.07084.
2. "Towards Understanding Specification Gaming in Reasoning Models" (arXiv:2605.02269, 2025).
3. TokenShapley (2025, arXiv:2507.05261) — LOO 和 Shapley 在 NLP 归因中的对比可增强方法论定位。

---

## Overall Assessment

**Overall: 3.0 — Findings**

本文选题时效性好——RLVR 中的 reward hacking 是 2025-2026 年 NLP/AI safety 社区的热点问题。STA 作为一种 post-hoc 诊断工具的实验设计是系统的，hacking mode taxonomy 有一定的分析价值。然而，核心方法论贡献（LOO 应用于 solver input）偏薄，"observe-vs-optimize asymmetry" 本质是 Goodhart's Law 的重述而非新概念，实验规模（单模型、N=3-5 seeds、同源数据集）严重限制了结论的泛化性。

这些问题的组合——方法新颖性不足 + 实验规模小 + 概念新颖性声称过度——使论文难以达到 EMNLP 主会议的接收标准（Overall ≥ 4），但 empirical findings 对 RLVR 社区有参考价值，适合 Findings 接收。

若要冲刺主会议：(1) 至少在 2-3 个不同架构的模型上验证 STA；(2) 在非 ProofWriter 的验证任务上测试泛化性；(3) 降低 "observe-vs-optimize asymmetry" 的新颖性声称力度，诚实定位为 Goodhart's Law 的 domain-specific 实证验证。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2692 · 2026-05-22T22:49:00.230033+00:00_

Reviewer 2 审稿意见已收到（Overall: 3.0 Findings）。等待 Reviewer 1 提交审稿意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 245

## Round 245

2 recorded events


### User

_source line 2693 · 2026-05-22T22:49:03.282737+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿总结**：

- **Overall: 3.0 (Findings)**
- **Soundness: 3.0** | **Excitement: 2.5** | **Reproducibility: 3.5** | **Confidence: 4**

**三个 Must-Fix 问题**：
1. **N1**: 核心方法（LOO on solver inputs）方法论新颖性不足以支撑长文——作者自己承认 LOO 本身不新，应用层面的创新偏薄
2. **N2**: 实验规模严重不足——单模型(Qwen2.5-3B)、N=3-5 seeds、跨数据集"泛化"实为同一 ProofWriter pipeline 的跨格式测试
3. **N3**: "observe-vs-optimize asymmetry" 本质是 Goodhart's Law 的重述，将已知概念重新命名为 C3 贡献存在 overclaiming

**六个 Should-Fix 问题**：标题过长(W1)、hacking taxonomy recall 未报告(W2)、ISR 局限性讨论不充分(W3)、SFT baseline 角色混淆(W4)、遗漏重要相关工作(W5)、统计显著性报告不完整(W6)

**核心判断**：选题时效、实验设计系统、分类法有分析价值，但方法新颖性 + 实验规模的组合短板使论文难以达到主会议标准，适合 Findings 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2694 · 2026-05-22T22:49:15.979078+00:00_

Reviewer 2 审稿意见已收到。注意到 Reviewer 2 在 Summary 中将模型误记为 "Qwen2.5-3B"，实际论文使用的是 Qwen3-4B——后续交叉分享时需标注此处。

等待 Reviewer 1 审稿意见提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 246

## Round 246

6 recorded events


### User

_source line 2695 · 2026-05-22T22:49:31.616199+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性 + 实验设计

---

## 总体评分
**Overall**: 3 (Findings)
**一句话总结**: STA 作为诊断工具的方法论贡献 (C1) 扎实且有新意，但 Goodhart 效应的实证证据 (C2) 被 premise-count confound 严重削弱，泛化性声明 (C3) 因 cross-scale/cross-model 实验均未收敛而缺乏支撑，整体 claims 强于 evidence。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | C1（STA 诊断框架）论证充分；C2（Goodhart）premise-count matched 后仅 1.06× 严重削弱核心声明；C3（跨模型/跨规模）2/3 配置未收敛，泛化证据不足 |
| Excitement | 3.5/5 | LOO ablation 用于 solver trace 诊断是新颖视角，hacking taxonomy 有实用价值，但单模型 case study 限制了影响力 |
| Overall Assessment | 3/5 | Findings 水平：方法论贡献扎实但实验广度和统计严谨性不足以支撑 Conference |
| Confidence | 4/5 | 仔细检查了关键 claims 的实验支撑，熟悉 RLVR 和 neurosymbolic reasoning 文献 |
| Reproducibility | 4/5 | 超参数详尽（Table 3）、承诺开源代码/数据，但 seed 43 采样差异和部分 hacking mode 分类细节不足 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Goodhart claim 的核心定量证据被 premise-count confound 瓦解
- 具体位置：Section 4.3（Premise-count confound）、Table 1、Appendix C
- 问题：论文 C2 的核心声明是 ISR-as-reward 产生 Goodhart 效应。但 Section 4.3 自己报告了 premise-count-matched comparison 后 ISR 优势从 21× 坍缩到仅 1.06×（McNemar p=0.317, n=100 matched pairs）——统计上不显著。论文随后转向 "per-sample mode classification offers a more reliable diagnostic pathway"（Section 4.3 末段），但主文未对 mode 级别提供替代性统计检验来弥补失去的标量信号。Abstract 中 "exhibits a seed-dependent Goodhart effect" 和 Section 4.3 标题 "Goodhart Effects on ISR-as-Reward" 的表述暗示了一个标量层面已被自己的控制实验否定的效应。
- 为什么影响接收：Goodhart 效应是论文三大贡献之一 (C2) 且出现在标题中。当其定量基础被 confound 控制后消失，C2 的可信度大幅下降。
- 建议修改方向：(1) 重新定义 Goodhart 的 operationalization——如果论文的真正证据在 mode 层面（hacking mode 组成从 CE-dominant 转向 TS-dominant），应以此为主要证据并提供 mode-shift 的统计检验（如 χ² 检验 mode 分布变化）；(2) 在 abstract/title 中降级 Goodhart 表述，使之与 1.06× 的实际效应量匹配；(3) 明确区分 "ISR scalar inflation"（不显著）和 "structural composition shift"（可能显著，但需检验）。

**N2** [critical] 单模型泛化性声明与 cross-scale/cross-model 失败实验的矛盾
- 具体位置：Section 4.4、Appendix E.4（LLaMA-3.2-3B）、E.5（seed-dependent convergence）、E.7（Qwen3-8B）、Section 5 Discussion
- 问题：论文的全部主实验仅基于 Qwen3-4B + FOLIO（500 样本）。C3 声称提供 "cross-logic and cross-dataset evidence documenting the observe-vs-optimize asymmetry"，但：
  - **Cross-scale**（Qwen3-8B）：PR=16%，未收敛（Appendix E.7, Table 14）。论文将此解释为 "convergence threshold"，但这是基于 n=2 失败样本的事后推测。
  - **Cross-model**（LLaMA-3.2-3B）：训练因零 GRPO advantage 提前终止（Appendix E.4）。论文将此归因于 "base model lacks FOL generation capability entirely"。
  - **Exec-only seeds**：6 个 seed 中仅 3 个收敛（Appendix E.5），收敛率 50%。
  - **ProofFOL**：ISR 差异 p=0.10，论文标为 exploratory。
  实质上，论文展示的是**一个模型在一个数据集上的一个条件下的现象**，但 abstract 和 Section 5 的叙事框架（"Goldilocks hypothesis"、"the asymmetry persists across logic types, dataset families, reward shemes, and random seeds"）远超这一证据基础。
- 为什么影响接收：ARR guidelines 明确要求 "Claims must match the evidence presented; generalization statements require supporting data"。当 3 个额外配置（8B、LLaMA、ProofFOL ISR reward）全部未产生可比较结果时，泛化声明缺乏基础。
- 建议修改方向：(1) 将 Discussion 中的泛化性叙事严格限定为 "hypothesis from a single-model case study"，而非 demonstrated pattern；(2) 删除或大幅弱化 "Goldilocks hypothesis"——基于 2 个失败案例的推测不宜作为结论；(3) Abstract 中的 "case study" 定位是合适的，但正文多处突破了这一定位。

**N3** [critical] CMH 检验的独立性假设不满足，统计推断可靠性存疑
- 具体位置：Section 4.1（Statistical considerations）、Table 1 脚注、Table 6（Appendix）
- 问题：CMH 检验将 within-seed samples 视为独立观测，但同一 seed 下的 100 个 eval 样本来自同一个 model checkpoint，存在模型级别的依赖结构。论文在 Section 4.1 诚实承认 "the true replication count is N=3 seeds"，但仍将 CMH 作为 primary statistical evidence 使用（Table 6 报告 CMH p=1.3×10⁻¹⁵ 等极端 p 值）。
  - 真实样本量：N=3（seeds），不是 N=300（samples across seeds）
  - 3 个 seeds 的 seed-level test 仅能提供有限的统计效力
  - Seed 43 的采样差异（见 N4）进一步削弱了 pooled 分析的可靠性
- 为什么影响接收：统计推断是实证论文的基础。当 primary test 的独立性假设不满足时，所有基于该检验的 claims 需要重新评估。
- 建议修改方向：(1) 将 per-seed analysis 作为 primary evidence，CMH 降为 supplementary；(2) 报告 seed-level effect sizes 和 bootstrap CI（resampling across seeds）；(3) 至少增加到 5 个收敛的 seeds 以提供 seed-level 检验的最低统计效力。

**N4** [major] Seed 43 采样策略不一致构成显著 confound
- 具体位置：Appendix E.6、Table 9（seed 43 行）
- 问题：Seed 43 使用 nucleus sampling（T=0.7）而非其他 seeds 的 greedy decoding。论文 Section 9 脚注标注 "evaluated with sampling (T=0.7) rather than greedy decoding (§A)"，并在 Appendix E.6 用独立 section 讨论。但该 seed 仍被纳入主文的 pooled analysis（Table 1 的 "3-seed pooled" 统计量包含 seed 43）。
  - Sampling 改变输出分布的 entropy，可能系统性地影响 ISR 值和 hacking mode 分布
  - Seed 43 的 ISR β=0.1 结果（Table 9）定性上也与 seeds 42/44 不同（"qualitatively different from the 3-seed average of 0%"——non-hacking ~55%）
  - 将不同 decoding 策略的结果与 greedy seeds 混合 pooling 违反了受控实验的基本原则
- 为什么影响接收：这不是 noise——这是一个系统性的实验设计不一致。Pooled 统计量的可信度因此受损。
- 建议修改方向：(1) 主文分析中排除 seed 43，或将其作为独立 sensitivity analysis 报告；(2) 明确标注 Table 1 中哪些行的 pooled stats 包含 seed 43，哪些不包含；(3) 报告排除 seed 43 后的 2-seed pooled 结果，验证主要结论是否稳健。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] SFT baseline 比较不公平
- 具体位置：Section 4.2、Table 1（SFT 行）
- 问题：SFT 的 PR=13%（OR=147）vs exec-only PR=93%。在 prove rate 相差 ~80pp 的情况下比较 structural properties，性能差异本身就可以解释大部分结构差异（能力不足的模型自然产生更多 degenerate 输出）。论文用 SFT 作为 "pre-RL reference rather than a PR-matched control"（Section 4.2），但这并不能使结构比较有效。
- 建议：用 exec-only 训练早期 checkpoint（PR~13-30%）作为 capability-matched control，与 SFT 和 fully-trained exec-only 三方比较。

**W2** [warning] Shuffled-ISR 控制实验严重 underpowered
- 具体位置：Table 1（Shuffled-ISR 行）、Section 4.3
- 问题：Shuffled-ISR condition 仅有 46 个 proved samples（1 seed, PR=15×3）。ISR 0.59±0.11 vs exec-only 0.55±0.11 的差异在 n=46 下几乎无统计效力。这个 control 是论证 "multiplicative coupling confound" 被隔离的关键之一，但样本量太小无法令人信服。
- 建议：增加 shuffled-ISR 的 seed 数量，或在主文中明确标注这一 control 的效力限制。

**W3** [warning] Hacking taxonomy 部分 mode 过于稀少，存在 over-specification 风险
- 具体位置：Table 2、Table 7、Appendix D.1-D.9
- 问题：8 种 hacking modes 中：
  - PG（premise-subset gaming）：exec-only 5 例，ISR 0 例，Random 0 例
  - Contradiction：仅在 exec-only 1000 步出现（Table 7 注释 "at contraction"）
  - Complexity-without-utility：definition 合理但 ISR interaction 仅描述为 "ISR correctly identifies"，无定量分析
  - Q-as-fact：仅 Prolog STA（Table 10）
  Table 8 报告 152 个 validated samples 全部 precision=1.00，但 recall 不可估计。当部分 mode 仅有个位数样本时，分类边界可能是 noise 而非真实类别。
- 建议：(1) 合并稀有 modes 为更粗粒度的类别（如将 PG、Contradiction、CwU 合并为 "other structural anomalies"）；(2) 报告 mode 分类的 inter-annotator agreement 或 cross-validation stability。

**W4** [warning] "Observe-vs-optimize asymmetry" 表述过强
- 具体位置：Abstract（"structural proxies for reasoning quality are easier to observe than to optimize"）、Section 5 Discussion
- 问题：这是一个一般性原则的表述，但证据仅来自一个模型、一个数据集、一种 reward formulation。Abstract 中将其表述为已证明的事实（"this observe-vs-optimize asymmetry persists across logic types, dataset families, reward shemes, and random seeds"），但 cross-logic 仅是 FOL↔Prolog 同一数据集的不同表示，cross-dataset 只有 ProofFOL（p=0.10），cross-model 未收敛。
- 建议：将 asymmetry 降级为 "observed pattern in this setting" 或 "hypothesis supported by preliminary evidence"。

**W5** [warning] ProofFOL p=0.10 结果在主文中的定位不够清晰
- 具体位置：Section 4.4（"ProofFOL ISR (β=0.1): dataset-dependent asymmetry"）
- 问题：p=0.10 在 Bonferroni 校正后更不显著。论文标注 "exploratory" 但仍在主文 Section 4.4 以支持 asymmetry 的语气呈现（"ISR reward on ProofFOL produces substantially higher genuine rates than exec-only"）。在多重比较和小样本背景下，这一结果应更审慎地呈现。
- 建议：在 Section 4.4 首句即明确标注 "This result does not reach statistical significance (p=0.10, uncorrected) and should be interpreted as exploratory only"。

---

## 小问题（不影响接收）

- **M1**: Algorithm 1 对 unproved formulations 的 ISR 设为 0（Section 3.2），但 ISR=0 在 proved 样本中也表示 "complete redundancy"。这两种情况语义不同，混用同一值可能导致 downstream analysis 混淆。建议对 unproved 使用 N/A 或单独标记。
- **M2**: LOO 与 Shapley value 的类比（Section 3.2 "a degenerate case of the Shapley value restricted to the (n−1)-coalition"）技术上正确，但可能误导读者认为 STA 继承了 Shapley 的某些理论保证（如 efficiency、symmetry）。建议简化为 "LOO ablation"，不做 Shapley 类比。
- **M3**: Figure 1 的 y 轴标签 "ISR (fraction of necessary components)" 在 ISR β=0.1 条件下应标注为 ISR-as-reward 的 training ISR 还是 diagnostic ISR——两者含义不同。
- **M4**: Table 1 中 "Seed 42" 标注为 "ISR raw mean inflated by TS gaming, 1.06× is the premise-count-matched value relative to random"，但这一关键信息仅在表格脚注中，容易被忽略。
- **M5**: References 中 "Qwen Team, 2025" 缺乏具体作者列表（虽然技术报告常用团队署名，但 ACL 格式通常要求列出至少前几位作者）。

---

## Questions to Authors

**Q1**: 如果排除 seed 43（采样策略不同的 seed），主要结论（特别是 Table 1 的 pooled statistics 和 CMH 检验）是否仍然成立？能否提供 2-seed (42, 44) pooled 的结果？

**Q2**: 论文声称 Goodhart 效应的主要证据在 mode composition shift（从 CE 到 TS dominance）而非 scalar ISR inflation。能否提供 mode 分布在 ISR-as-reward vs exec-only 之间变化的正式统计检验（如 Fisher exact test 或 χ² test on mode frequencies）？

**Q3**: 为什么选择 multiplicative reward formulation r_exec × (1 + β·ISR) 而非 additive formulation r_exec + β·ISR？Multiplicative form 使 ISR 信号的强度与 prove rate 耦合，这本身可能驱动部分观察到的 Goodhart 效应模式。Limitations 提到 "alternative formulations remain untested"——这是否应被视为一个更根本的实验设计局限？

**Q4**: Cross-scale (8B) 和 cross-model (LLaMA) 实验均未收敛。论文提出 "convergence threshold" 解释，但是否考虑过更简约的解释——即 STA/ISR 诊断的现象可能是 Qwen3-4B 特有的训练动态，而非 GRPO 的一般性质？

**Q5**: LOO ablation 假设 component independence，但逻辑前提之间常有交互作用（例如三段论的大小前提缺一不可）。论文说 "the observed collapse is therefore conservative"（Section 3.2），但这仅指 ISR 值被低估——LOO 下观察到的 *hacking patterns* 是否也可能因忽略交互而产生 false positives（将交互效应误判为 gaming）？

---

## Missing References

- **Uesato et al. (2022)** "Solving Math Word Problems with Process and Outcome-Based Feedback" — 已引用（p.11），但未在 related work 中讨论 process reward 与 ISR 的关系。
- **Cobbe et al. (2021)** "Training verifiers to solve math word problems" — 未见引用，但与 component-level reward 诊断相关。
- 建议补充近期关于 **reward overoptimization** 的理论分析工作，如 Gao et al. (2023) "Scaling Laws for Reward Model Overoptimization"——已引用但可加强讨论。

---

## 主要优势

1. **STA 方法定义清晰、算法化**：Algorithm 1 给出了可执行的伪代码，ISR 的数学定义（Eq. 1）简洁明确，方法可复现性强。
2. **诚实的局限性披露**：论文明确承认 ISR ≠ semantic faithfulness（ρ=-0.049, Appendix C）、premise-count confound 将 ISR 优势降至 1.06×、cross-scale/model 未收敛、seed 43 采样不一致。这种自我批判的诚实态度值得肯定。
3. **Hacking taxonomy 有实用价值**：8 种 gaming mode 的定义、示例和检测方法（Appendix D）为社区提供了可操作的诊断工具包，即使部分 mode 稀有。
4. **详尽的 per-seed 分析**：Tables 9-12 提供了完整的 per-seed breakdown，使读者可以独立评估 seed-level variability。
5. **"Case study" 标题定位合适**：论文标题中的 "case study" 设定了正确的期望，尽管正文部分超出了这一定位。

---

## 总结

本文提出了一个有前景的诊断工具（STA/ISR），在 neurosymbolic reasoning 的 reward hacking 检测中填补了 execution-based evaluation 和 annotation-free diagnostics 之间的空白。核心方法论贡献 (C1) 扎实。但实证发现存在三个根本性问题：(1) Goodhart 效应声明被 premise-count matching 后仅 1.06× 的效应量削弱；(2) 泛化性声明与 cross-scale/cross-model 全部未收敛的实验现实矛盾；(3) 统计推断依赖不满足独立性假设的 CMH 检验。这些问题使论文适合 Findings（方法论有价值）但不足以支撑 Conference 接收。建议作者在 resubmission 中增加模型多样性、修正统计方法、并将 claims 严格限定在证据支持的范围内。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2696 · 2026-05-22T22:50:18.143465+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3/5 | **Excitement**: 3.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] Goodhart claim 的核心定量证据被 premise-count confound 瓦解\n- Section 4.3 自己报告 premise-count-matched comparison 后 ISR 优势从 21× 坍缩到仅 1.06×（McNemar p=0.317, n=100 matched pairs）——统计上不显著。论文随后转向 mode classification 作为替代证据，但主文未对 mode 级别提供替代性统计检验。Abstract 中 \"exhibits a seed-dependent Goodhart effect\" 的表述暗示了一个标量层面已被自己的控制实验否定的效应。\n- 建议：(1) 重新定义 Goodhart 的 operationalization——以 mode-shift 为主要证据并提供统计检验；(2) 在 abstract/title 中降级 Goodhart 表述；(3) 明确区分 \"ISR scalar inflation\"（不显著）和 \"structural composition shift\"（需检验）。\n\n**N2** [critical] 单模型泛化性声明与 cross-scale/cross-model 失败实验的矛盾\n- 全部主实验仅基于 Qwen3-4B + FOLIO（500 样本）。Cross-scale（Qwen3-8B PR=16%，未收敛）、Cross-model（LLaMA-3.2-3B 训练提前终止）、Exec-only seeds 6个中仅3个收敛（收敛率50%）、ProofFOL p=0.10 标为 exploratory。\n- 实质上是一个模型在一个数据集上的一个条件下的现象，但 abstract 和 Discussion 的叙事框架远超这一证据基础。\n\n**N3** [critical] CMH 检验的独立性假设不满足\n- CMH 将 within-seed samples 视为独立观测，但同一 seed 下的 100 个 eval 样本来自同一个 model checkpoint。真实样本量 N=3（seeds），不是 N=300。极端 p 值（如 1.3×10⁻¹⁵）可能被严重高估。\n\n**N4** [major] Seed 43 采样策略不一致构成显著 confound\n- Seed 43 使用 nucleus sampling（T=0.7）而非 greedy decoding，但仍被纳入 pooled analysis。Sampling 改变输出分布的 entropy，可能系统性地影响 ISR 值和 hacking mode 分布。\n\n### Should-Fix 问题\n\n**W1** SFT baseline PR=13% vs exec-only PR=93%，比较不公平\n**W2** Shuffled-ISR 控制实验仅 46 个 proved samples，严重 underpowered\n**W3** Hacking taxonomy 部分 mode 过于稀少（PG 5例、Contradiction 仅 1000步出现），存在 over-specification 风险\n**W4** \"Observe-vs-optimize asymmetry\" 表述过强——证据仅来自一个模型一个数据集一种 reward formulation\n**W5** ProofFOL p=0.10 在主文中的定位不够清晰，应更审慎呈现\n\n### 主要优势\n1. STA 方法定义清晰、算法化，ISR 数学定义简洁明确\n2. 诚实的局限性披露（ISR ≠ semantic faithfulness, premise-count confound, seed 43 采样不一致）\n3. Hacking taxonomy 有实用价值\n4. 详尽的 per-seed 分析（Tables 9-12）\n5. \"Case study\" 标题定位合适",
  "project": "solver-trace-ablation",
  "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3/5 | **Excitement**: 3.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] Goodhart claim 的核心定量证据被 premise-count confound 瓦解\n- Section 4.3 自己报告 premise-count-matched comparison 后 ISR 优势从 21× 坍缩到仅 1.06×（McNemar p=0.317, n=100 matched pairs）——统计上不显著。论文随后转向 mode classification 作为替代证据，但主文未对 mode 级别提供替代性统计检验。Abstract 中 \"exhibits a seed-dependent Goodhart effect\" 的表述暗示了一个标量层面已被自己的控制实验否定的效应。\n- 建议：(1) 重新定义 Goodhart 的 operationalization——以 mode-shift 为主要证据并提供统计检验；(2) 在 abstract/title 中降级 Goodhart 表述；(3) 明确区分 \"ISR scalar inflation\"（不显著）和 \"structural composition shift\"（需检验）。\n\n**N2** [critical] 单模型泛化性声明与 cross-scale/cross-model 失败实验的矛盾\n- 全部主实验仅基于 Qwen3-4B + FOLIO（500 样本）。Cross-scale（Qwen3-8B PR=16%，未收敛）、Cross-model（LLaMA-3.2-3B 训练提前终止）、Exec-only seeds 6个中仅3个收敛（收敛率50%）、ProofFOL p=0.10 标为 exploratory。\n- 实质上是一个模型在一个数据集上的一个条件下的现象，但 abstract 和 Discussion 的叙事框架远超这一证据基础。\n\n**N3** [critical] CMH 检验的独立性假设不满足\n- CMH 将 within-seed samples 视为独立观测，但同一 seed 下的 100 个 eval 样本来自同一个 model checkpoint。真实样本量 N=3（seeds），不是 N=300。极端 p 值（如 1.3×10⁻¹⁵）可能被严重高估。\n\n**N4** [major] Seed 43 采样策略不一致构成显著 confound\n- Seed 43 使用 nucleus sampling（T=0.7）而非 greedy decoding，但仍被纳入 pooled analysis。Sampling 改变输出分布的 entropy，可能系统性地影响 ISR 值和 hacking mode 分布。\n\n### Should-Fix 问题\n\n**W1** SFT baseline PR=13% vs exec-only PR=93%，比较不公平\n**W2** Shuffled-ISR 控制实验仅 46 个 proved samples，严重 underpowered\n**W3** Hacking taxonomy 部分 mode 过于稀少（PG 5例、Contradiction 仅 1000步出现），存在 over-specification 风险\n**W4** \"Observe-vs-optimize asymmetry\" 表述过强——证据仅来自一个模型一个数据集一种 reward formulation\n**W5** ProofFOL p=0.10 在主文中的定位不够清晰，应更审慎呈现\n\n### 主要优势\n1. STA 方法定义清晰、算法化，ISR 数学定义简洁明确\n2. 诚实的局限性披露（ISR ≠ semantic faithfulness, premise-count confound, seed 43 采样不一致）\n3. Hacking taxonomy 有实用价值\n4. 详尽的 per-seed 分析（Tables 9-12）\n5. \"Case study\" 标题定位合适",
    "project": "solver-trace-ablation",
    "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 2697 · 2026-05-22T22:50:43.641892+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25498
}
```

</details>

---


### Tool call

_source line 2698 · 2026-05-22T22:50:44.194362+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3/5 | **Excitement**: 2.5/5 | **Reproducibility**: 3.5/5 | **Confidence**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 核心方法论新颖性不足以支撑长文\n- STA 本质是 LOO 消融应用于 solver 输入组件——作者自己在 §3.2 承认 \"LOO ablation itself is standard\"。论文声称新颖性在于 \"its application as a GRPO-hacking diagnostic\"，但将已有方法应用到新场景并观察到结果，在方法论贡献上偏弱。C1 声称 STA 是 \"a diagnostic framework\"，但框架级别的贡献需要在多模型/多任务/多 benchmark 上验证泛化性。\n- 建议：降级为 Short Paper 或明确定位为 empirical contribution。\n\n**N2** [critical] 实验规模严重不足\n- 单一基础模型（Qwen3-4B）、N=3-5 seeds、跨数据集\"泛化\"实为同一 ProofWriter pipeline 的跨格式测试。LLaMA-3.2-3B 仅作为 cold-start failure 出现，Qwen3-8B 仅运行了 exec-only 条件。\n- 这些发现是否仅是 Qwen3-4B + ProofWriter 的 artifact？\n\n**N3** [critical] \"Observe-vs-optimize asymmetry\" 概念新颖性声称过度\n- 本质是 Goodhart's Law 的标准表现。Manheim & Garrabrant (2019) 的四种 Goodhart 变体分类法已系统描述了这一现象。Gao et al. (2023) 在 reward model overoptimization 中实证展示了类似的 proxy-target 分离。论文的 \"asymmetry\" 并未提出超越已有框架的新理论洞察。\n- 建议：将 C3 重新定位为 \"在 neurosymbolic RLVR 中实证验证 Goodhart's Law 的具体表现形式\"。\n\n### Should-Fix 问题\n\n**W1** 标题过长（~140 字符）且信息密度不均，建议精简至 ~60 chars\n**W2** Hacking taxonomy 的 recall 未报告——Table 8 明确写 \"Recall is not estimable\"，一个不报告 recall 的分类器无法保证完备性\n**W3** ISR 局限性讨论不充分——ISR=0 可能是多条等价推理路径而非结构退化\n**W4** SFT baseline 角色混淆——SFT 直接看到了 structural target 而 GRPO 没有\n**W5** 遗漏重要相关工作：Khalifa et al. 2026 (Countdown-Code), \"Towards Understanding Specification Gaming\" (arXiv:2605.02269)\n**W6** 统计显著性报告不完整——多数比较未达显著，但论文选择性报告了显著结果\n\n### 主要优势\n1. 系统的实验设计与控制变量（Shuffled-ISR 对照巧妙）\n2. 有价值的实证发现（ISR 崩溃而 execution accuracy 维持 >90%）\n3. 详尽的 hacking mode 分类法\n4. 诚实的 scope 声明（\"A Case Study\"）\n5. 叙事结构基本连贯",
  "project": "solver-trace-ablation",
  "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3/5 | **Excitement**: 2.5/5 | **Reproducibility**: 3.5/5 | **Confidence**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 核心方法论新颖性不足以支撑长文\n- STA 本质是 LOO 消融应用于 solver 输入组件——作者自己在 §3.2 承认 \"LOO ablation itself is standard\"。论文声称新颖性在于 \"its application as a GRPO-hacking diagnostic\"，但将已有方法应用到新场景并观察到结果，在方法论贡献上偏弱。C1 声称 STA 是 \"a diagnostic framework\"，但框架级别的贡献需要在多模型/多任务/多 benchmark 上验证泛化性。\n- 建议：降级为 Short Paper 或明确定位为 empirical contribution。\n\n**N2** [critical] 实验规模严重不足\n- 单一基础模型（Qwen3-4B）、N=3-5 seeds、跨数据集\"泛化\"实为同一 ProofWriter pipeline 的跨格式测试。LLaMA-3.2-3B 仅作为 cold-start failure 出现，Qwen3-8B 仅运行了 exec-only 条件。\n- 这些发现是否仅是 Qwen3-4B + ProofWriter 的 artifact？\n\n**N3** [critical] \"Observe-vs-optimize asymmetry\" 概念新颖性声称过度\n- 本质是 Goodhart's Law 的标准表现。Manheim & Garrabrant (2019) 的四种 Goodhart 变体分类法已系统描述了这一现象。Gao et al. (2023) 在 reward model overoptimization 中实证展示了类似的 proxy-target 分离。论文的 \"asymmetry\" 并未提出超越已有框架的新理论洞察。\n- 建议：将 C3 重新定位为 \"在 neurosymbolic RLVR 中实证验证 Goodhart's Law 的具体表现形式\"。\n\n### Should-Fix 问题\n\n**W1** 标题过长（~140 字符）且信息密度不均，建议精简至 ~60 chars\n**W2** Hacking taxonomy 的 recall 未报告——Table 8 明确写 \"Recall is not estimable\"，一个不报告 recall 的分类器无法保证完备性\n**W3** ISR 局限性讨论不充分——ISR=0 可能是多条等价推理路径而非结构退化\n**W4** SFT baseline 角色混淆——SFT 直接看到了 structural target 而 GRPO 没有\n**W5** 遗漏重要相关工作：Khalifa et al. 2026 (Countdown-Code), \"Towards Understanding Specification Gaming\" (arXiv:2605.02269)\n**W6** 统计显著性报告不完整——多数比较未达显著，但论文选择性报告了显著结果\n\n### 主要优势\n1. 系统的实验设计与控制变量（Shuffled-ISR 对照巧妙）\n2. 有价值的实证发现（ISR 崩溃而 execution accuracy 维持 >90%）\n3. 详尽的 hacking mode 分类法\n4. 诚实的 scope 声明（\"A Case Study\"）\n5. 叙事结构基本连贯",
    "project": "solver-trace-ablation",
    "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 2699 · 2026-05-22T22:50:45.604918+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1410
}
```

</details>

---


### Assistant

_source line 2700 · 2026-05-22T22:50:48.661030+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 247

## Round 247

2 recorded events


### User

_source line 2701 · 2026-05-22T22:50:51.257578+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3/5（Findings），Soundness 3/5，Excitement 3.5/5。

核心问题四个 Must-Fix：
1. Goodhart claim 的标量证据被 premise-count matching 后瓦解（21× → 1.06×，不显著），但论文标题和 abstract 仍以此为核心贡献
2. Cross-scale（8B）和 cross-model（LLaMA）实验全部未收敛，泛化性声明缺乏证据支撑
3. CMH 检验将 within-seed samples 视为独立观测（实际 N=3 seeds），统计推断不可靠
4. Seed 43 使用 nucleus sampling 而其他 seeds 用 greedy decoding，被混入 pooled analysis 构成 confound

方法论贡献（STA 诊断框架 + hacking taxonomy）扎实，适合 Findings 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2702 · 2026-05-22T22:50:55.736413+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 248

## Round 248

2 recorded events


### User

_source line 2703 · 2026-05-22T22:52:09.350796+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R2-N1: 核心方法论新颖性不足以支撑长文**

R2 认为 STA 仅是 "LOO 消融应用于 solver 输入组件"，方法论贡献偏弱。我部分不同意。

R2 正确指出 LOO 本身是标准方法（论文 §3.2 诚实承认），但 R2 低估了以下组合贡献：(1) 将 LOO 用于 solver trace 而非模型参数/特征是一个非平凡的设计选择——传统 LOO 消融作用于输入特征或模型组件，而 STA 作用于形式化推理的前提结构，利用 solver 的 binary accept/reject 输出作为 necessity oracle（§3.2: "The solver's binary accept/reject output makes leave-one-out sufficient for testing component necessity"）；(2) ISR 度量将 per-sample LOO 结果聚合为一个可微分的训练信号（Eq. 1），并实验展示了其作为 reward 时的 Goodhart 效应——这是 LOO 消融从未被探索过的用途；(3) 8 种 hacking mode 的 taxonomy（Table 2, Appendix D）提供了一个可操作的诊断工具包。

然而，我同意 R2 关于"框架级别贡献需要多模型验证"的判断——这与我自己的 N2 一致。论文的贡献水平介于 pure empirical 和 methodological 之间，作为 Long Paper 偏弱但并非不可接受。**建议不降为 Short Paper**（附录的 per-seed 分析和 taxonomy 细节在 Short Paper 格式下无法容纳），但应在主文中更明确定位为 "diagnostic method + empirical case study" 而非 "framework"。

**[AGREE] R2-N2: 实验规模严重不足**

完全同意。这与我的 N2 高度一致。所有主实验基于 Qwen3-4B + FOLIO/ProofFOL（同一 ProofWriter pipeline），cross-scale (Qwen3-8B) 和 cross-model (LLaMA-3.2-3B) 均未收敛。R2 提出的关键问题——"这些发现是否仅是 Qwen3-4B + ProofWriter 的 artifact"——论文无法排除，这是最根本的泛化性问题。

补充我的发现：(1) FOLIO eval set 仅 100 个 gold 样本（§4.1），ProofFOL eval 仅 100 个翻译样本（Appendix A, Table 4），总有效实验数据量非常有限；(2) Exec-only 6 个 seeds 中仅 3 个收敛（Appendix E.5），50% 的 non-convergence rate 本身就说明结果对初始化高度敏感；(3) ProofFOL 被称为 "cross-dataset"，但它是从 ProofWriter 通过 GPT-4o 翻译得到的（Appendix A），与 FOLIO 共享 FOL 语法和推理复杂度分布，并非真正独立的 dataset。

**[REBUT] R2-N3: "Observe-vs-optimize asymmetry" 概念新颖性声称过度**

R2 认为这只是 Goodhart's Law 的标准表现，我部分不同意。

R2 正确指出 Manheim & Garrabrant (2019) 已有 Goodhart 四变体分类、Gao et al. (2023) 已有 reward model overoptimization 的实证展示。但论文的贡献不在于 "发现 Goodhart 现象存在"，而在于提供了一个 **component-level 诊断工具**来定位 Goodhart 效应的具体结构表现形式。具体来说：

- Manheim & Garrabrant 的分类是理论层面的（regressional/extremal/causal/adversarial），不提供可操作的检测方法
- Gao et al. 的 scaling law 是 aggregate reward 层面的，不提供 per-sample 结构诊断
- 本文的贡献是将 Goodhart 从 "aggregate metric divergence" 细化到 "per-sample structural mode classification"（Table 2 的 8 种 mode）

然而，我同意 R2 关于措辞的意见——论文不应将 "asymmetry" 包装为新概念，而应明确定位为 "在 neurosymbolic RLVR 中通过 STA 实证刻画 Goodhart 的结构层面表现"。这与我的 W4 一致。"Observe-vs-optimize asymmetry" 作为 shorthand 可以保留，但不应暗示这是一个超越 Goodhart 框架的新理论洞察。

---

### Should-Fix 问题

**[REBUT] R2-W1: 标题过长**

标题 "Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study" 确实偏长（~120 chars），但 ACL/ARR 并无标题长度硬限制。更重要的是，标题信息量合理——涵盖方法 (STA)、发现 (structural degeneration + Goodhart)、场景 (GRPO neurosymbolic) 和定位 (case study)。压缩到 60 chars 会丢失关键信息。可以考虑精简到 ~90 chars（如删去 "GRPO-Trained"），但 60 chars 对一篇 Long Paper 过于苛刻。这是 minor issue，不应作为 Should-Fix。

**[AGREE] R2-W2: Hacking taxonomy 的 recall 未报告**

同意。这与我的 W3 一致。Table 8 明确写 "Recall is not estimable from the validation-only design; non-hacking rates should be interpreted as upper bounds"。一个只有 precision 没有 recall 的分类器无法保证不遗漏真实的 hacking 样本。这对 taxonomy 的 completeness 声明构成限制。建议作者在主文中明确标注 taxonomy 可能遗漏某些 hacking 模式。

**[AGREE] R2-W3: ISR=0 可能是等价推理路径而非结构退化**

同意，这是一个有价值的观察。ISR=0 表示每个 component 都不是个体必要的——但这可能是因为 (a) 存在冗余前提（结构退化），也可能是因为 (b) 存在多条等价推理路径（genuine redundancy）。论文在 Appendix C 承认 ISR "quantifies component redundancy, not semantic faithfulness"，但未在主文中充分讨论 (b) 的可能性。尤其在 FOL 中，多条有效证明路径是常见的。这与我的 M1 相关——ISR=0 for proved vs unproved samples 的语义混淆。

**[REBUT] R2-W4: SFT baseline 角色混淆**

R2 称 "SFT 直接看到了 structural target 而 GRPO 没有"。这一表述不完全准确。SFT 看到的是 gold formalization（包含完整的 structural information），而 GRPO exec-only 仅收到 binary execution feedback。论文将 SFT 定位为 "pre-RL reference rather than a PR-matched control"（§4.2），这一定位是合理的。问题不在于 SFT 的角色定义，而在于 SFT PR=13% vs exec-only PR=93% 的 capability gap 使结构比较缺乏说服力（与我的 W1 一致）。SFT 作为 "training paradigm contrast" 是有意义的，但作为 "structural quality baseline" 是不公平的。

**[AGREE] R2-W5: 遗漏重要相关工作**

部分同意。论文已引用 Khalifa et al. (2026)（p.10, references），但确实未在 Related Work §2 中讨论其与 STA 的关系。"Towards Understanding Specification Gaming" (arXiv:2605.02269) 如果确实存在且相关，应该被讨论——这类关于 specification gaming 的系统性分析与本文的 hacking taxonomy 直接相关。建议作者在 camera-ready 中补充讨论。

**[REBUT] R2-W6: 统计显著性报告选择性**

不完全同意。论文在 Appendix 中报告了所有比较的 p 值，包括不显著的结果（如 ProofFOL p=0.10 标为 exploratory，premise-count matched comparison McNemar p=0.317）。主文 §4.1 明确声明 "N=2 sensitivity analysis excluding s43 confirms consistent patterns (Appendix E.6)" 和 "ProofFOL results (p=0.10, N=3) are exploratory and underpowered"。

然而，R2 的concern 有一定道理——主文的叙事结构确实倾向于强调显著结果。例如 Table 6 的 CMH 检验报告了极端 p 值（p=1.3×10⁻¹⁵），而这些 p 值的可靠性受到 independence assumption 的严重影响（我的 N3）。建议作者在主文中更均衡地呈现显著和不显著的结果，而非将不显著结果主要放在附录中。

---

### 总结

R2 的三个 Must-Fix 中，N2（实验规模不足）我完全同意且与我的 N2 高度一致；N3（asymmetry 概念新颖性）我同意措辞需要调整但反驳其"无新意"的判断；N1（方法论新颖性不足）我认为偏严——STA 的组合贡献不应被简化为"标准 LOO 的应用"，但同意框架级声明需要更多实证支撑。

R2 给出 Excitement 2.5/5 偏低。尽管实验规模有限，STA 作为一个 component-level structural diagnostic 的思路在 neurosymbolic reasoning 社区有明确的实用价值。我维持 Excitement 3.5/5。

两位 Reviewer 的共识集中在：(1) 单模型泛化性不足，(2) claims 强于 evidence，(3) 统计严谨性可提升。这些问题限制了论文在 Conference track 的竞争力，但方法论贡献和诊断工具的实用价值支持 Findings 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2704 · 2026-05-22T22:52:14.281258+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 249

## Round 249

2 recorded events


### User

_source line 2705 · 2026-05-22T22:52:16.831242+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心判断：R2 的 N2（实验规模不足）完全同意，N3（asymmetry 措辞需调整）部分同意但反驳"无新意"，N1（方法论新颖性不足）认为偏严。两位 Reviewer 的共识是：单模型泛化性不足、claims 强于 evidence、统计严谨性可提升——支持 Findings 但不足以 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2706 · 2026-05-22T22:52:23.220311+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 250

## Round 250

42 recorded events


### User

_source line 2707 · 2026-05-22T22:53:30.368166+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 问题

### [AGREE] R1-N1: Goodhart claim 的核心定量证据被 premise-count confound 瓦解

同意这是本文最关键的方法论问题。

**同意理由**：论文自身数据（§4.3）承认 premise-count-matched comparison 将 21× ISR 优势压缩至 1.06×（McNemar p=0.317, n=100），标量层面的 Goodhart 效应在统计上不存在。这意味着 Abstract 中 "empirical characterization of a Goodhart effect when ISR is repurposed as a training reward"（C2 贡献声明）的核心定量支撑已被自己的控制实验否定。

**补充 R1 的分析**：论文试图用 mode classification（§4.3 "the compositional mode shift—not the scalar ISR difference—constitutes the primary evidence"）挽救 Goodhart 声明，但存在两个问题：
1. Mode-shift 的统计检验仅在 Table 6 中以 Cochran-Mantel-Haenzel test 报告了 TS gaming rate 的比较，而 R1-N3 正确指出该检验的独立性假设不满足，因此 p 值可能严重高估。
2. 即使 mode-shift 本身成立，从 "ISR 标量不变但 hacking mode 组成改变" 推导出 "Goodhart effect" 需要更精确的论证——Goodhart's Law 通常指 metric 本身被 inflate/gamed，而非 metric 不变但底层结构改变。后者更像是 reward shaping 的副作用而非经典 Goodhart。

**建议与 R1 一致**：Abstract 和 Title 中的 "Goodhart Effects" 应降级或重新定义。

---

### [AGREE] R1-N2: 单模型泛化性声明与失败实验的矛盾

强烈同意。这与我自己的 N2 完全一致。

**补充说明**：R1 将基础模型标记为 "Qwen3-4B"，实际论文 §4.1 和 Table 3 明确记载为 **Qwen2.5-3B**——这是 R1 的笔误，但不影响批评的实质。

**进一步加强 R1 的论点**：
- LLaMA-3.2-3B（Appendix E.4）不仅未完成训练，而且 cold-start failure 的原因是 "the base model lacks FOL generation capability entirely"——这意味着 STA 框架的适用前提（模型能生成 valid formalization）就不满足，而非 STA 本身的问题。但论文未讨论这一区别。
- Qwen3-8B（Appendix E.7）仅测试了 exec-only 条件（无 ISR reward 条件），因此无法验证 Goodhart 效应的跨模型泛化性。
- 论文 C1 声称 STA 是 "model-agnostic" diagnostic framework（§5: "STA generalizes to any RL system whose output is verified by a deterministic checker"），但实验证据完全不支撑 "any RL system" 这一泛化声明。

---

### [AGREE with nuance] R1-N3: CMH 检验的独立性假设不满足

核心批评成立，但 "真实 N=3" 的表述需要修正。

**同意理由**：同一 seed 下的 100 个 eval 样本确实来自同一 model checkpoint，存在 model-level 随机效应导致的组内相关。CMH 检验将这些视为独立观测会 inflate type-I error，p=1.3×10⁻¹⁵ 几乎必然被高估。

**修正 R1 的表述**：说 "真实样本量 N=3" 过于极端。每个 test sample 的 formalization 是模型对不同输入的独立预测——不同输入会触发不同的生成路径，输出之间并非完全相关。更准确的描述是：有效样本量（effective N）在 3 到 300 之间，取决于组内相关系数（ICC）。合适的统计方法是 **multilevel/mixed-effects model**（seed 作为随机效应），而非简单的 CMH。

**建议**：论文应 (1) 报告 ICC 估计值，(2) 用 seed-level clustered bootstrap 或 mixed-effects logistic regression 替代 CMH，(3) 至少在附录中报告 seed-level summary statistics 的非参数检验（如 Friedman test, N=3 seeds）。

---

### [AGREE] R1-N4: Seed 43 采样策略不一致构成显著 confound

同意。

**同意理由**：Seed 43 使用 nucleus sampling（T=0.7, footnote 2, page 5）而其余 seeds 使用 greedy decoding——这从根本上改变了输出分布的 entropy 和多样性。在 N=3 seeds 的小样本中，一个 seed 的系统性偏差可能主导 pooled 分析的结论。

**论文的部分缓解**：Appendix E.6 提供了排除 seed 43 的 N=2 敏感性分析（Table 13），结论 "Qualitative patterns preserved: exec-only converges to ~7.5% non-hacking; ISR β=0.1 shifts composition toward TS"。但 N=2 的分析几乎没有统计功效——这实际上更加暴露了样本量不足的问题。

**建议**：主文分析应以排除 seed 43 的结果为主，或至少报告包含/排除 seed 43 的两组结果。Seed 43 的 nucleus sampling 结果可作为 robustness check 放在附录。

---

## Should-Fix 问题

### [AGREE] R1-W1: SFT baseline 比较不公平

同意——与我自己的 W4 一致。SFT 直接在 gold formalization 上监督训练（§4.1），天然获得了结构信息的 direct supervision signal，而 GRPO 仅有 execution-based reward。SFT 的高 ISR（0.395）不能归因于 "supervised training preserves structure"——它只是记忆了 gold 的结构模式。这不是 GRPO 的公平对照，而是 structural preservation 的 upper bound。

---

### [AGREE] R1-W2: Shuffled-ISR 控制实验 underpowered

同意。从 Table 1，Shuffled-ISR 的 PR≈15(±3)%，在 100 个 eval 样本 × 3 seeds 中仅约 45 个 proved samples。这个样本量无法提供有意义的统计功效来检测 ISR signal vs. random noise 的差异。

**补充**：Shuffled-ISR 是论文中最巧妙的控制设计之一（打乱 ISR 信号以分离因果效应），其概念价值远大于当前的统计功效。建议增加 seeds 或 eval samples 来充分利用这个设计。

---

### [AGREE with nuance] R1-W3: Hacking taxonomy 部分 mode 过于稀少

部分同意。

**同意部分**：PG（5 例，Table 7）、CI（仅在 1000 steps 出现）确实样本量过小，作为独立 mode 分类的证据基础薄弱。Over-specification 的风险存在——将 8 种 mode 精简为 3-4 种 dominant modes（CE, TS/TSb, Tautological Collapse/TC）可能更稳健。

**部分保留**：分类法的价值不仅在于当前数据中的频率，也在于为后续工作提供 **分析词汇表**。即使 PG 和 CI 在当前实验中稀少，它们的定义（Appendix D）描述了理论上可能的 hacking pathway。但论文应明确标注哪些 mode 是 "well-supported"（CE, TS: >70 examples each）vs. "exploratory"（PG, CI: <10 examples）。

---

### [AGREE] R1-W4: "Observe-vs-optimize asymmetry" 表述过强

强烈同意——这与我自己的 **N3（Must-Fix 级别）** 完全一致。

我甚至认为 R1 将此列为 Should-Fix 偏保守。"Observe-vs-optimize asymmetry" 本质是 Goodhart's Law 的重述（Manheim & Garrabrant, 2019 的四种变体分类法已系统化地描述了 "metric used for observation vs. optimization" 的区别）。将已知概念重新命名并声称为 C3 贡献，在 novelty 评估中是显著减分项。建议提升至 Must-Fix。

---

### [AGREE] R1-W5: ProofFOL p=0.10 定位不够审慎

同意。§4.4 将 ProofFOL ISR（β=0.1）的 p=0.10 标记为 exploratory，但主文叙事中仍以 "ISR reward on ProofFOL produces substantially higher genuine rates" 呈现（§4.4），"substantially" 一词与 p=0.10 不匹配。应改为 "suggestively higher" 或 "directionally consistent" 等更审慎的表述。

---

## 对 R1 主要优势评价的回应

R1 列出的 5 个优势全部成立，我在自己的审稿中也独立识别了相同的优势（S1-S5）。特别同意：
- **S2**（诚实的局限性披露）：论文在 §3.2（ISR limitations）、§4.3（premise-count confound）、footnote 2（seed 43 采样）中的透明披露值得肯定，这在提交论文中不常见。
- **S5**（"Case study" 标题定位合适）：这一定位与实验规模匹配，是诚实的 scope 管理。

---

## 综合评价

R1 和我（R2）的评审意见在核心判断上高度一致：

| 维度 | R1 | R2 | 一致性 |
|------|----|----|--------|
| Overall | 3.0 (Findings) | 3.0 (Findings) | 完全一致 |
| Soundness | 3/5 | 3/5 | 完全一致 |
| 单模型泛化性 | N2 (Must-Fix) | N2 (Must-Fix) | 完全一致 |
| Goodhart claim | N1 (Must-Fix) | — | R2 未独立识别此点，现同意 |
| 概念新颖性 | W4 (Should-Fix) | N3 (Must-Fix) | R2 评级更严格 |
| 方法论新颖性 | — | N1 (Must-Fix) | R1 未独立提出 |

**两位 Reviewer 的共识**：论文的 empirical findings 对 RLVR 社区有信息价值，但方法论新颖性（LOO 应用）+ 实验规模（单模型）+ 概念新颖性（Goodhart 重述）的组合不足以支撑 EMNLP 长文主会议接收。3.0 (Findings) 是合理的评分。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2708 · 2026-05-22T22:53:59.425032+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2709 · 2026-05-22T22:53:59.927581+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T22:42:05.332518+00:00\", \"completed_at\": \"2026-05-22T22:46:10.182350+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯文本：Title + Abstract + Introduction）。Figure 1 出现在 page 2 顶部，在前 3 页内，位置可接受。Title 较长（含 \\\"A Case Study\\\" 副标题）但清晰传达研究内容，排版整洁。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（ISR 训练轨迹图）作为第一个 display item，有效传达核心现象（ISR 在训练中的崩溃），锚定效果好。蓝/橙/绿三色可区分，图例可读，caption 自包含。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Algorithm 1（STA 伪代码）排版规范，框线清晰，打破文字节奏。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 5-6\", \"message\": \"连续 2 页纯文本（Section 4.1-4.3），无 figure/table/display equation 穿插。Page 4 有 Equation (1) 打破节奏，但 pages 5-6 全为密集文字段落，审稿人阅读体验偏单调。建议：考虑将 Table 1 或 Table 2 前移至 page 6 位置，或在实验部分增加一个小型结果可视化。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 和 Table 2 同时出现在一页。两表均使用 booktabs 风格，无竖线，最优值加粗标注。Table 1 中 ISR* 列使用上标 † 注释合理。数字小数位数一致。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2（双面板柱状图）和 Figure 3（水平堆叠柱状图）排布紧凑。Figure 2 底部面板使用蓝/橙/绿分区颜色，百分比标注直接标在柱上，字号偏小但可读。Figure 3 颜色丰富（约 6 种），需注意色盲区分度——建议检查 CE（蓝）和 TS（相近蓝色调）在灰度打印下是否可区分。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Section 5 Discussion and Conclusion 及 Section 6 Limitations 排在 page 8 底部，空间利用充分，主文正好 8 页，符合 ACL 页数限制。\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-11\", \"message\": \"References 格式统一，无 [?] 未解析引用，无明显 overfull hbox。arXiv 预印本格式一致。\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Table 3（训练超参数）和 Table 4（ProofFOL vs. FOLIO 对比）排版清晰，booktabs 风格一致。\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Table 5（Mode composition by premise-count bins）数据密集但可读。页面文字填充充分。\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Table 6（Fisher exact tests）使用 booktab
…[truncated 1343 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2710 · 2026-05-22T22:53:59.928041+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2711 · 2026-05-22T22:54:01.435788+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1507
}
```

</details>

---


### Tool call

_source line 2712 · 2026-05-22T22:54:02.239441+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null | head -100",
  "description": "Read current review issues tracker (first 100 lines)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null | head -100",
    "description": "Read current review issues tracker (first 100 lines)"
  }
}
```

</details>

---


### Tool result

_source line 2713 · 2026-05-22T22:54:02.444478+00:00_

issues:
# === Resolved issues from rounds 0-26 (condensed) ===
- id: R1-W1
  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。
  resolution_round: 2
- id: RV-EVAL-FALLBACK
  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: stderr ERROR → sys.exit(1)。
  resolution_round: 1
- id: R1-W2
  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 15
  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
  resolution_round: 2
- id: R2-W1
  summary: Limitations section 格式不合规
  category: format
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 独立 limitations.tex 已创建。
  resolution_round: 3
- id: R2-W2
  summary: 实验仅用单一模型和单一数据集
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。
  resolution_round: 3
- id: R2-W6
  summary: SFT baseline 比较不公平：PR=14% vs 93%
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。
  resolution_round: 2
- id: v2-R1-N1
  summary: Abstract '93%' PR 为 single seed
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 2
  last_seen_round: 3
  resolution: Abstract 使用 3-seed pooled mean±std。
  resolution_round: 3
- id: v2-R1-N3
  summary: 仅 2 个 β 值不足以刻画 dose-response
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 2
  last_seen_round: 3
  resolution: 4 个 β 值提供完整 dose-response 曲线。
  resolution_round: 4
- id: v7-R1-N2
 
…[truncated 686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 205
}
```

</details>

---


### Tool call

_source line 2714 · 2026-05-22T22:54:12.958411+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null | grep -E \"^- id:|status:|summary:\" | tail -80",
  "description": "Check issue statuses in tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null | grep -E \"^- id:|status:|summary:\" | tail -80",
    "description": "Check issue statuses in tracker"
  }
}
```

</details>

---


### Tool result

_source line 2715 · 2026-05-22T22:54:13.059417+00:00_

  summary: "ISR 与 Process Reward Models 的概念联系未被讨论"
  status: in_progress
- id: v27-R2-MR-PROOF-QUALITY
  summary: "缺失引用：Proof quality metrics 先行工作"
  status: open
- id: v27-R1-W7
  summary: "Non-hacking rate 作为 upper bound 跨条件比较时 recall 可能不一致"
  status: in_progress
- id: v27-R2-W3
  summary: "Title 'Structural Degeneration' 与 ISR 测量 'component necessity' 概念跳跃"
  status: in_progress
- id: v27-R2-W4
  summary: "Hacking taxonomy 验证 50 样本偏少 + recall 未评估"
  status: in_progress
- id: v27-R1-W4
  summary: "100-step checkpoint hacking 分析 n=32"
  status: open
- id: v27-R2-M2
  summary: "metr-reward-hacking bib 缺 URL"
  status: resolved
- id: v27-R2-MR-MUTATION
  summary: "缺失：Mutation testing 在 ML/code generation 中的近期应用"
  status: in_progress
- id: v27-R2-W6
  summary: "Hacking taxonomy 持久性/可迁移性存疑"
  status: open
- id: v27-R2-W7
  summary: "β 值消融仅两个点"
  status: open
- id: v28-R1-N1
  summary: "ISR 聚合 vs per-sample 诊断需明确分离"
  status: in_progress
- id: v28-R12-SFT-CONVERGENCE
  summary: "SFT baseline 未报告 training loss curve"
  status: resolved
- id: v28-R12-MR-INFLUENCE
  summary: "缺失引用：Cook's distance / influence functions (Koh & Liang 2017)"
  status: in_progress
- id: v28-R1-M4
  summary: "50% exec-only seeds 不收敛对主分析影响"
  status: in_progress
- id: v28-VISUAL-APPENDIX
  summary: "Appendix 末页大面积空白"
  status: in_progress
- id: v29-R12-N1
  summary: "5-seed extension 存在 double standard：标记为 exploratory 但在 Appendix 作支撑证据"
  status: in_progress
- id: v29-R2-W5
  summary: "'Observe-vs-optimize asymmetry' 非新概念——本质即 Goodhart's Law"
  status: in_progress
- id: v29-R12-MR-ENSEMBLE
  summary: "缺失引用：Coste et al. (2023) Reward Model Ensembles 和 Moskovitz et al. (2023) Constrained RLHF"
  status: resolved
- id: v29-R12-MR-SHAPLEY-LUNDBERG
  summary: "缺失引用：Lundberg and Lee (2017) SHAP"
  status: resolved
- id: v30-R2-MR1
  summary: "缺失引用：Wu & Tang (2026) 'When Reward Hacking Rebounds' (arXiv:2604.01476)"
  status: wont_fix
- id: v30-R2-MR2
  summary: "缺失引用：Monitoring Emergent Reward Hacking 
…[truncated 589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2716 · 2026-05-22T22:54:51.636660+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null | wc -l",
  "description": "Count lines in review issues file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null | wc -l",
    "description": "Count lines in review issues file"
  }
}
```

</details>

---


### Tool result

_source line 2717 · 2026-05-22T22:54:51.737558+00:00_

1278

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2718 · 2026-05-22T22:54:54.951526+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null",
  "description": "Read full review issues tracker",
  "timeout": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null",
    "description": "Read full review issues tracker",
    "timeout": "10000"
  }
}
```

</details>

---


### Tool result

_source line 2719 · 2026-05-22T22:54:55.003020+00:00_

&lt;persisted-output>
Output too large (37.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-director-a46f8029/1a162432-ac00-439d-b9d5-b9cb29fcb117/tool-results/bp3h2yh9g.txt

Preview (first 2KB):
issues:
# === Resolved issues from rounds 0-26 (condensed) ===
- id: R1-W1
  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。
  resolution_round: 2
- id: RV-EVAL-FALLBACK
  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: stderr ERROR → sys.exit(1)。
  resolution_round: 1
- id: R1-W2
  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 15
  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
  resolution_round: 2
- id: R2-W1
  summary: Limitations section 格式不合规
  category: format
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 独立 limitations.tex 已创建。
  resolution_round: 3
- id: R2-W2
  summary: 实验仅用单一模型和单一数据集
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。
  resolution_round: 3
- id: R2-W6
  summary: SFT baseline 比较不公平：PR=14% vs 93%
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。
  resolution_round: 2
- id: v2-R1-N1
  summary: Abstract '93%' PR 为 single seed
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 2
  last_seen_round: 3
  
…[truncated 337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2720 · 2026-05-22T22:55:00.377924+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml') as f:\n    data = yaml.safe_load(f)\nopen_issues = [i for i in data['issues'] if i.get('status') in ('open', 'in_progress')]\nfor i in open_issues:\n    print(f\\\"{i['id']} | {i['status']} | {i['severity']} | {i['summary']}\\\")\nprint(f'\\\\nTotal open/in_progress: {len(open_issues)}')\n\"",
  "description": "List open/in_progress issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml') as f:\n    data = yaml.safe_load(f)\nopen_issues = [i for i in data['issues'] if i.get('status') in ('open', 'in_progress')]\nfor i in open_issues:\n    print(f\\\"{i['id']} | {i['status']} | {i['severity']} | {i['summary']}\\\")\nprint(f'\\\\nTotal open/in_progress: {len(open_issues)}')\n\"",
    "description": "List open/in_progress issues"
  }
}
```

</details>

---


### Tool result

_source line 2721 · 2026-05-22T22:55:00.579320+00:00_

v17-R12-W1 | in_progress | critical | 单模型 (Qwen3-4B) 无法支撑通用性声明
v19-R12-W3 | in_progress | critical | ProofFOL p=0.10 被过度引用
v19-R1-W6 | in_progress | warning | Classifier recall 未知 + PG 审计仅 seed 42
v17-R1-W9 | in_progress | critical | Seed 43 使用 T=0.7 sampling 评估而非 greedy
v16-R1-W2 | in_progress | warning | LOO 独立性假设未量化偏差
v16-R1-W4 | in_progress | warning | ISR-as-reward 乘法耦合混淆
v17-VISUAL-LAYOUT | in_progress | warning | Display items 分布不均
v17-VISUAL-FONT | in_progress | info | Figure 内部文字偏小
v22-R12-N1 | in_progress | critical | ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果
v22-R12-N3 | in_progress | critical | Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）
v22-R2-N1 | in_progress | warning | 方法论新颖性不足——LOO 是标准技术
v22-R2-W3 | in_progress | info | 与 Kim et al. (2026) 区分不够清晰
v22-R1-W1 | in_progress | warning | ProofFOL 'genuine' 用 coarser classifier
v22-R1-W4 | in_progress | warning | Shuffled-ISR control N=46 统计效力有限
v22-R1-W5 | in_progress | warning | SFT PR confound 仅通过 100-step (n=32) 部分缓解
v21-R1-N1 | open | info | 新增引用整合略机械
v23-R12-N1 | in_progress | critical | N=3 seeds 统计效力不足
v23-R1-N3 | in_progress | warning | 乘法耦合需 constant-bonus control
v23-R2-N1 | in_progress | warning | Case study 标题与通用声称之间 framing 矛盾
v23-R2-W3 | in_progress | warning | 与 Helff et al. (2026) IPT 对比不充分
v23-MR-PROSFI | open | info | 缺失 PRoSFI + Interleaved Bonus 引用
v25-R12-N1 | in_progress | critical | 5-seed 扩展与 3-seed 矛盾——C2 非系统性
v25-R12-N2 | in_progress | critical | ISR 214× raw drop 叙事——premise-count confound 缺 qualifier
v25-R1-W5 | in_progress | warning | Table 1 exec-only 仅 seed 42
v25-VISUAL-W1 | in_progress | warning | Figure 3 可读性差
v25-MINOR-BIB | open | info | FOLIO bib 年份 mismatch
v27-R12-N1 | in_progress | warning | STA 与 Helff 2026 IPT 区分不充分——概念同构，仅粒度差异
v27-R1-N2 | in_progress | warning | CMH pseudo-replication：within-seed samples 非独立
v27-R1-N4 | in_progress | critical | Seed 43 T=0.7 评估 + checkpoints 已删除
v27-R12-TAXONOMY | in_progress | warning | Taxono
…[truncated 1664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2722 · 2026-05-22T22:56:29.524005+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml') as f:\n    data = yaml.safe_load(f)\n\nROUND = 31\n\n# Map current round findings to existing issue IDs\nraised_this_round = {\n    # R1-N1 / R2 AGREE: Goodhart premise-count confound\n    'v22-R12-N3': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 两位 Reviewer 共识：premise-count matched 后 1.06× (p=0.317) 使 Goodhart 标量证据不成立。R1 建议以 mode-shift 为主证据并提供统计检验。R2 补充：mode-shift ≠ 经典 Goodhart（metric 不变但底层结构改变更像 reward shaping 副作用）。'},\n    'v22-R12-N1': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 复现：non-hacking ISR vs Random p=0.182 仍不显著。两位 Reviewer 一致要求 Abstract/Title 降级 Goodhart 表述。'},\n    'v25-R12-N2': {'round': ROUND, 'reviewers': ['R1'], 'note': 'R31 R1 再次指出 214× raw drop → 1.06× matched 的叙事落差。'},\n    # R1-N2 / R2-N2: Single model\n    'v17-R12-W1': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 两位 Reviewer 共识最严重问题：Qwen3-4B + FOLIO 单模型单数据集，8B/LLaMA 均未收敛。R2 追问\"是否仅 Qwen3-4B + ProofWriter 的 artifact\"。'},\n    # R1-N3: CMH independence\n    'v27-R1-N2': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 R1 升为 Must-Fix。R2 同意核心批评但修正\"真实 N=3\"表述：effective N 在 3-300 间取决于 ICC，建议 mixed-effects model。'},\n    'v23-R12-N1': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 N=3 seeds 统计效力问题再次被两位 Reviewer 提出。'},\n    # R1-N4: Seed 43\n    'v17-R1-W9': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 两位 Reviewer 共识 Must-Fix：seed 43 T=0.7 sampling 混入 pooled analysis 违反受控实验原则。R2 建议主文以排除 s43 为主分析。'},\n    'v27-R1-N4': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 共识：seed 43 checkpoints 已删除且采样不一致是系统性 confound。'},\n    # R2-N1: Method novelty\n    'v22-R2-N1': {'round': ROUND, 'reviewers': ['R2'], 'note': 'R31 R2 维持 Must-Fix：LOO 应用于 solver input 方法论新颖性不足以支撑长文。R1 部分反驳：组合贡献（solver trace LOO + ISR 作为 reward + taxonomy）不应简化为标准 LOO 应用，但同意框架级声明需更多实证。'},\n    # R2-N3 / R1-W4: Asymmetry overclaiming\n    'v29-R2-W5': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 共识：observe-vs-optimize asymmetry 本质是 Goodhart 重述。R2 维持 Must-Fix，R1 列为 Should-Fix 但同意措辞需调整。分歧仅在严重程度。'},\n    # SFT baseline\n    'v30-R1-W1': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 两位 Reviewer 共识：SFT PR=13% vs exec-only PR=93% 使结构比较不公平。SFT 应定位为 upper bound 而非 matched control。'},\n    'v22-R1-W5': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 100-step checkpoint (n=32) 仅部分缓解 SFT PR confound。'},\n    # Shuffled-ISR\n    'v22-R1-W4': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 共识：Shuffled-ISR 46 proved samples 严重 underpowered。R2 称其概念设计巧妙但统计效力不足。'},\n    # Taxonomy recall\n    'v27-R2-W4': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 共识：152 样本 precision=1.00 但 recall 不可估。Taxonomy 完备性声明受限。'},\n    'v19-R1-W6': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 Classifier recall 未知 + PG 审计仅 seed 42 问题仍存在。'},\n    # ProofFOL p=0.10\n    'v19-R12-W3': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 共识：p=0.10 在主文 §4.4 用 \"substantially\" 表述不当，应改为 \"directionally consistent\" 或 \"suggestively higher\"。'},\n    # ISR limitations\n    'v30-R2-W3': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 R2 提出 ISR=0 可能是多条等价推理路径而非结构退化。R1 同意这是有价值的观察，ISR=0 的语义模糊性需在主文讨论。'},\n    # Title / framing\n    'v23-R2-N1': {'round': ROUND, 'reviewers': ['R2'], 'note': 'R31 R2 认为标题过长（~140 chars），建议精简至 ~60 chars。R1 反驳：ACL 无硬限制，可精简到 ~90 chars 但 60 太苛刻。'},\n    # LOO independence\n    'v16-R1-W2': {'round': ROUND, 'reviewers': ['R1'], 'note': 'R31 R1 Q5 追问：LOO 忽略交互是否产生 hacking false positives（将交互效应误判为 gaming）。'},\n    # Multiplicative coupling\n    'v16-R1-W4': {'round': ROUND, 'reviewers': ['R1'], 'note': 'R31 R1 Q3 追问乘法 vs 加法 reward formulation 选择理由。'},\n    # Visual layout\n    'v17-VISUAL-LAYOUT': {'round': ROUND, 'reviewers': ['Visual'], 'note': 'R31 视觉审查：pages 5-6 连续纯文本无 display item，建议前移 Table 1/2。'},\n    # 5-seed extension\n    'v25-R12-N1': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 5-seed extension（s45/s46 ~55% N-H vs 3-seed 6%）bimodal outcome 再次被两位 Reviewer 关注。R1 指出单模型不足以判定此为通用现象。'},\n    # ISR aggregate vs per-sample\n    'v28-R1-N1': {'round': ROUND, 'reviewers': ['R1'], 'note': 'R31 R1 建议 Goodhart 的 operationalization 从 ISR scalar 转向 mode classification 为主证据。'},\n    # Goldilocks\n    'v30-R2-W4': {'round': ROUND, 'reviewers': ['R2'], 'note': 'R31 R2 M4 再次提醒确认 Goldilocks 全文用法一致为 observation 而非 hypothesis。'},\n    # 50% non-convergence\n    'v28-R1-M4': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 6/6 exec-only seeds 中仅 3 收敛（50%），两位 Reviewer 一致认为这限制了结论的适用范围。'},\n}\n\n# Update existing issues\nfor issue in data['issues']:\n    iid = issue['id']\n    if iid in raised_this_round:\n        info = raised_this_round[iid]\n        if 'mentions' not in issue:\n            issue['mentions'] = []\n        issue['mentions'].append(info)\n        issue['last_seen_round'] = ROUND\n\n# Issues NOT raised this round that are open/in_progress\nnot_raised = set()\nfor issue in data['issues']:\n    iid = issue['id']\n    if issue.get('status') in ('open', 'in_progress') and iid not in raised_this_round:\n        not_raised.add(iid)\n\n# Add \"not mentioned\" notes for open issues not raised\nfor issue in data['issues']:\n    if issue['id'] in not_raised:\n        if 'mentions' not in issue:\n            issue['mentions'] = []\n        issue['mentions'].append({\n            'round': ROUND,\n            'reviewers': [],\n            'note': '本轮未提及,可能已修复或不再适用,待 Research Director 确认'\n        })\n\n# Add new issues\nnew_issues = [\n    {\n        'id': 'v31-R2-MR-SPECGAMING',\n        'summary': '缺失引用：Towards Understanding Specification Gaming in Reasoning Models (arXiv:2605.02269)',\n        'category': 'writing',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': ROUND,\n        'last_seen_round': ROUND,\n        'mentions': [{'round': ROUND, 'reviewers': ['R2'], 'note': 'R2 建议引用并讨论 spec gaming 理论分析与 STA hacking taxonomy 的关系。'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'v31-R2-W-TITLE-LENGTH',\n        'summary': '标题过长（~140 chars），建议精简',\n        'category': 'writing',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': ROUND,\n        'last_seen_round': ROUND,\n        'mentions': [{'round': ROUND, 'reviewers': ['R2'], 'note': 'R2 建议精简至 ~60 chars。R1 反驳无硬限制，可考虑 ~90 chars。分歧：R2 视为 Should-Fix，R1 视为 minor。'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'v31-R2-M-ISR0-AMBIGUITY',\n        'summary': 'ISR=0 对 proved vs unproved 语义不同但用同一值，可能混淆 downstream analysis',\n        'category': 'method',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': ROUND,\n        'last_seen_round': ROUND,\n        'mentions': [{'round': ROUND, 'reviewers': ['R1'], 'note': 'R1 M1：unproved ISR=0 与 proved redundant ISR=0 语义不同，建议 unproved 用 N/A。'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n]\n\ndata['issues'].extend(new_issues)\n\noutput = yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False, width=200)\nprint(output[:200])\nprint(f\"... ({len(output)} chars total, {len(data['issues'])} issues)\")\n\nwith open('/tmp/review_issues_r31.yaml', 'w') as f:\n    f.write(output)\nprint(\"Written to /tmp/review_issues_r31.yaml\")\nPYEOF",
  "description": "Update review issues tracker with round 31 findings",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport yaml\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml') as f:\n    data = yaml.safe_load(f)\n\nROUND = 31\n\n# Map current round findings to existing issue IDs\nraised_this_round = {\n    # R1-N1 / R2 AGREE: Goodhart premise-count confound\n    'v22-R12-N3': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 两位 Reviewer 共识：premise-count matched 后 1.06× (p=0.317) 使 Goodhart 标量证据不成立。R1 建议以 mode-shift 为主证据并提供统计检验。R2 补充：mode-shift ≠ 经典 Goodhart（metric 不变但底层结构改变更像 reward shaping 副作用）。'},\n    'v22-R12-N1': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 复现：non-hacking ISR vs Random p=0.182 仍不显著。两位 Reviewer 一致要求 Abstract/Title 降级 Goodhart 表述。'},\n    'v25-R12-N2': {'round': ROUND, 'reviewers': ['R1'], 'note': 'R31 R1 再次指出 214× raw drop → 1.06× matched 的叙事落差。'},\n    # R1-N2 / R2-N2: Single model\n    'v17-R12-W1': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 两位 Reviewer 共识最严重问题：Qwen3-4B + FOLIO 单模型单数据集，8B/LLaMA 均未收敛。R2 追问\"是否仅 Qwen3-4B + ProofWriter 的 artifact\"。'},\n    # R1-N3: CMH independence\n    'v27-R1-N2': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 R1 升为 Must-Fix。R2 同意核心批评但修正\"真实 N=3\"表述：effective N 在 3-300 间取决于 ICC，建议 mixed-effects model。'},\n    'v23-R12-N1': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 N=3 seeds 统计效力问题再次被两位 Reviewer 提出。'},\n    # R1-N4: Seed 43\n    'v17-R1-W9': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 两位 Reviewer 共识 Must-Fix：seed 43 T=0.7 sampling 混入 pooled analysis 违反受控实验原则。R2 建议主文以排除 s43 为主分析。'},\n    'v27-R1-N4': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 共识：seed 43 checkpoints 已删除且采样不一致是系统性 confound。'},\n    # R2-N1: Method novelty\n    'v22-R2-N1': {'round': ROUND, 'reviewers': ['R2'], 'note': 'R31 R2 维持 Must-Fix：LOO 应用于 solver input 方法论新颖性不足以支撑长文。R1 部分反驳：组合贡献（solver trace LOO + ISR 作为 reward + taxonomy）不应简化为标准 LOO 应用，但同意框架级声明需更多实证。'},\n    # R2-N3 / R1-W4: Asymmetry overclaiming\n    'v29-R2-W5': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 共识：observe-vs-optimize asymmetry 本质是 Goodhart 重述。R2 维持 Must-Fix，R1 列为 Should-Fix 但同意措辞需调整。分歧仅在严重程度。'},\n    # SFT baseline\n    'v30-R1-W1': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 两位 Reviewer 共识：SFT PR=13% vs exec-only PR=93% 使结构比较不公平。SFT 应定位为 upper bound 而非 matched control。'},\n    'v22-R1-W5': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 100-step checkpoint (n=32) 仅部分缓解 SFT PR confound。'},\n    # Shuffled-ISR\n    'v22-R1-W4': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 共识：Shuffled-ISR 46 proved samples 严重 underpowered。R2 称其概念设计巧妙但统计效力不足。'},\n    # Taxonomy recall\n    'v27-R2-W4': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 共识：152 样本 precision=1.00 但 recall 不可估。Taxonomy 完备性声明受限。'},\n    'v19-R1-W6': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 Classifier recall 未知 + PG 审计仅 seed 42 问题仍存在。'},\n    # ProofFOL p=0.10\n    'v19-R12-W3': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 共识：p=0.10 在主文 §4.4 用 \"substantially\" 表述不当，应改为 \"directionally consistent\" 或 \"suggestively higher\"。'},\n    # ISR limitations\n    'v30-R2-W3': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 R2 提出 ISR=0 可能是多条等价推理路径而非结构退化。R1 同意这是有价值的观察，ISR=0 的语义模糊性需在主文讨论。'},\n    # Title / framing\n    'v23-R2-N1': {'round': ROUND, 'reviewers': ['R2'], 'note': 'R31 R2 认为标题过长（~140 chars），建议精简至 ~60 chars。R1 反驳：ACL 无硬限制，可精简到 ~90 chars 但 60 太苛刻。'},\n    # LOO independence\n    'v16-R1-W2': {'round': ROUND, 'reviewers': ['R1'], 'note': 'R31 R1 Q5 追问：LOO 忽略交互是否产生 hacking false positives（将交互效应误判为 gaming）。'},\n    # Multiplicative coupling\n    'v16-R1-W4': {'round': ROUND, 'reviewers': ['R1'], 'note': 'R31 R1 Q3 追问乘法 vs 加法 reward formulation 选择理由。'},\n    # Visual layout\n    'v17-VISUAL-LAYOUT': {'round': ROUND, 'reviewers': ['Visual'], 'note': 'R31 视觉审查：pages 5-6 连续纯文本无 display item，建议前移 Table 1/2。'},\n    # 5-seed extension\n    'v25-R12-N1': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 5-seed extension（s45/s46 ~55% N-H vs 3-seed 6%）bimodal outcome 再次被两位 Reviewer 关注。R1 指出单模型不足以判定此为通用现象。'},\n    # ISR aggregate vs per-sample\n    'v28-R1-N1': {'round': ROUND, 'reviewers': ['R1'], 'note': 'R31 R1 建议 Goodhart 的 operationalization 从 ISR scalar 转向 mode classification 为主证据。'},\n    # Goldilocks\n    'v30-R2-W4': {'round': ROUND, 'reviewers': ['R2'], 'note': 'R31 R2 M4 再次提醒确认 Goldilocks 全文用法一致为 observation 而非 hypothesis。'},\n    # 50% non-convergence\n    'v28-R1-M4': {'round': ROUND, 'reviewers': ['R1', 'R2'], 'note': 'R31 6/6 exec-only seeds 中仅 3 收敛（50%），两位 Reviewer 一致认为这限制了结论的适用范围。'},\n}\n\n# Update existing issues\nfor issue in data['issues']:\n    iid = issue['id']\n    if iid in raised_this_round:\n        info = raised_this_round[iid]\n        if 'mentions' not in issue:\n            issue['mentions'] = []\n        issue['mentions'].append(info)\n        issue['last_seen_round'] = ROUND\n\n# Issues NOT raised this round that are open/in_progress\nnot_raised = set()\nfor issue in data['issues']:\n    iid = issue['id']\n    if issue.get('status') in ('open', 'in_progress') and iid not in raised_this_round:\n        not_raised.add(iid)\n\n# Add \"not mentioned\" notes for open issues not raised\nfor issue in data['issues']:\n    if issue['id'] in not_raised:\n        if 'mentions' not in issue:\n            issue['mentions'] = []\n        issue['mentions'].append({\n            'round': ROUND,\n            'reviewers': [],\n            'note': '本轮未提及,可能已修复或不再适用,待 Research Director 确认'\n        })\n\n# Add new issues\nnew_issues = [\n    {\n        'id': 'v31-R2-MR-SPECGAMING',\n        'summary': '缺失引用：Towards Understanding Specification Gaming in Reasoning Models (arXiv:2605.02269)',\n        'category': 'writing',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': ROUND,\n        'last_seen_round': ROUND,\n        'mentions': [{'round': ROUND, 'reviewers': ['R2'], 'note': 'R2 建议引用并讨论 spec gaming 理论分析与 STA hacking taxonomy 的关系。'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'v31-R2-W-TITLE-LENGTH',\n        'summary': '标题过长（~140 chars），建议精简',\n        'category': 'writing',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': ROUND,\n        'last_seen_round': ROUND,\n        'mentions': [{'round': ROUND, 'reviewers': ['R2'], 'note': 'R2 建议精简至 ~60 chars。R1 反驳无硬限制，可考虑 ~90 chars。分歧：R2 视为 Should-Fix，R1 视为 minor。'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'v31-R2-M-ISR0-AMBIGUITY',\n        'summary': 'ISR=0 对 proved vs unproved 语义不同但用同一值，可能混淆 downstream analysis',\n        'category': 'method',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': ROUND,\n        'last_seen_round': ROUND,\n        'mentions': [{'round': ROUND, 'reviewers': ['R1'], 'note': 'R1 M1：unproved ISR=0 与 proved redundant ISR=0 语义不同，建议 unproved 用 N/A。'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n]\n\ndata['issues'].extend(new_issues)\n\noutput = yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False, width=200)\nprint(output[:200])\nprint(f\"... ({len(output)} chars total, {len(data['issues'])} issues)\")\n\nwith open('/tmp/review_issues_r31.yaml', 'w') as f:\n    f.write(output)\nprint(\"Written to /tmp/review_issues_r31.yaml\")\nPYEOF",
    "description": "Update review issues tracker with round 31 findings",
    "timeout": "30000"
  }
}
```

</details>

---


### Tool result

_source line 2723 · 2026-05-22T22:56:29.825805+00:00_

issues:
- id: R1-W1
  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  
... (40027 chars total, 101 issues)
Written to /tmp/review_issues_r31.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2724 · 2026-05-22T22:56:33.641600+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /tmp/review_issues_r31.yaml",
  "description": "Read updated issues YAML for submission",
  "timeout": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /tmp/review_issues_r31.yaml",
    "description": "Read updated issues YAML for submission",
    "timeout": "10000"
  }
}
```

</details>

---


### Tool result

_source line 2725 · 2026-05-22T22:56:33.692684+00:00_

&lt;persisted-output>
Output too large (46.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-director-a46f8029/1a162432-ac00-439d-b9d5-b9cb29fcb117/tool-results/bei6q1upc.txt

Preview (first 2KB):
issues:
- id: R1-W1
  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。
  resolution_round: 2
- id: RV-EVAL-FALLBACK
  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: stderr ERROR → sys.exit(1)。
  resolution_round: 1
- id: R1-W2
  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 15
  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
  resolution_round: 2
- id: R2-W1
  summary: Limitations section 格式不合规
  category: format
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 独立 limitations.tex 已创建。
  resolution_round: 3
- id: R2-W2
  summary: 实验仅用单一模型和单一数据集
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。
  resolution_round: 3
- id: R2-W6
  summary: SFT baseline 比较不公平：PR=14% vs 93%
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。
  resolution_round: 2
- id: v2-R1-N1
  summary: Abstract '93%' PR 为 single seed
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 2
  last_seen_round: 3
  resolution: Abstract 使用 3-seed pooled mean±std。
  resol
…[truncated 334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2726 · 2026-05-22T22:56:38.511613+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /tmp/review_issues_r31.yaml | wc -c",
  "description": "Check issues file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /tmp/review_issues_r31.yaml | wc -c",
    "description": "Check issues file size"
  }
}
```

</details>

---


### Tool result

_source line 2727 · 2026-05-22T22:56:38.562444+00:00_

47216

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2728 · 2026-05-22T22:56:42.717732+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nwith open('/tmp/review_issues_r31.yaml') as f:\n    content = f.read()\nprint(content)\n\" 2>/dev/null | head -5\necho \"File size: $(wc -c < /tmp/review_issues_r31.yaml) bytes\"",
  "description": "Verify issues file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nwith open('/tmp/review_issues_r31.yaml') as f:\n    content = f.read()\nprint(content)\n\" 2>/dev/null | head -5\necho \"File size: $(wc -c < /tmp/review_issues_r31.yaml) bytes\"",
    "description": "Verify issues file"
  }
}
```

</details>

---


### Tool result

_source line 2729 · 2026-05-22T22:56:42.868833+00:00_

issues:
- id: R1-W1
  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed
  category: experiment
  severity: critical
File size: 47216 bytes

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2730 · 2026-05-22T22:56:46.652254+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nwith open('/tmp/review_issues_r31.yaml') as f:\n    content = f.read()\n# Write to a simpler temp file for reading\nwith open('/tmp/issues_content.txt', 'w') as f:\n    f.write(content)\nprint(f\"Content length: {len(content)}\")\nprint(\"Ready for submission\")\nPYEOF",
  "description": "Prepare issues content for tool submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nwith open('/tmp/review_issues_r31.yaml') as f:\n    content = f.read()\n# Write to a simpler temp file for reading\nwith open('/tmp/issues_content.txt', 'w') as f:\n    f.write(content)\nprint(f\"Content length: {len(content)}\")\nprint(\"Ready for submission\")\nPYEOF",
    "description": "Prepare issues content for tool submission"
  }
}
```

</details>

---


### Tool result

_source line 2731 · 2026-05-22T22:56:46.703262+00:00_

Content length: 40027
Ready for submission

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2732 · 2026-05-22T22:56:50.770868+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_issues_r31.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_issues_r31.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2733 · 2026-05-22T22:56:50.821672+00:00_

1	issues:
2	- id: R1-W1
3	  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 0
8	  last_seen_round: 2
9	  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。
10	  resolution_round: 2
11	- id: RV-EVAL-FALLBACK
12	  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
13	  category: experiment
14	  severity: critical
15	  status: resolved
16	  first_raised_round: 1
17	  last_seen_round: 1
18	  resolution: stderr ERROR → sys.exit(1)。
19	  resolution_round: 1
20	- id: R1-W2
21	  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量
22	  category: framing
23	  severity: critical
24	  status: resolved
25	  first_raised_round: 0
26	  last_seen_round: 15
27	  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
28	  resolution_round: 2
29	- id: R2-W1
30	  summary: Limitations section 格式不合规
31	  category: format
32	  severity: critical
33	  status: resolved
34	  first_raised_round: 0
35	  last_seen_round: 2
36	  resolution: 独立 limitations.tex 已创建。
37	  resolution_round: 3
38	- id: R2-W2
39	  summary: 实验仅用单一模型和单一数据集
40	  category: experiment
41	  severity: critical
42	  status: resolved
43	  first_raised_round: 0
44	  last_seen_round: 2
45	  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。
46	  resolution_round: 3
47	- id: R2-W6
48	  summary: SFT baseline 比较不公平：PR=14% vs 93%
49	  category: experiment
50	  severity: critical

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2734 · 2026-05-22T22:56:57.900881+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nwith open('/tmp/review_issues_r31.yaml') as f:\n    content = f.read()\n# Verify it's valid YAML\nimport yaml\ndata = yaml.safe_load(content)\nprint(f\"Valid YAML: {len(data['issues'])} issues\")\n# Write content to clipboard-like file for the next step\nwith open('/tmp/issues_for_submit.txt', 'w') as f:\n    f.write(content)\nPYEOF",
  "description": "Validate YAML before submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nwith open('/tmp/review_issues_r31.yaml') as f:\n    content = f.read()\n# Verify it's valid YAML\nimport yaml\ndata = yaml.safe_load(content)\nprint(f\"Valid YAML: {len(data['issues'])} issues\")\n# Write content to clipboard-like file for the next step\nwith open('/tmp/issues_for_submit.txt', 'w') as f:\n    f.write(content)\nPYEOF",
    "description": "Validate YAML before submission"
  }
}
```

</details>

---


### Tool result

_source line 2735 · 2026-05-22T22:56:58.102790+00:00_

Valid YAML: 101 issues

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2736 · 2026-05-22T22:56:59.961193+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_issues_r31.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_issues_r31.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2737 · 2026-05-22T22:57:00.264496+00:00_

1	issues:
2	- id: R1-W1
3	  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 0
8	  last_seen_round: 2
9	  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。
10	  resolution_round: 2
11	- id: RV-EVAL-FALLBACK
12	  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
13	  category: experiment
14	  severity: critical
15	  status: resolved
16	  first_raised_round: 1
17	  last_seen_round: 1
18	  resolution: stderr ERROR → sys.exit(1)。
19	  resolution_round: 1
20	- id: R1-W2
21	  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量
22	  category: framing
23	  severity: critical
24	  status: resolved
25	  first_raised_round: 0
26	  last_seen_round: 15
27	  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
28	  resolution_round: 2
29	- id: R2-W1
30	  summary: Limitations section 格式不合规
31	  category: format
32	  severity: critical
33	  status: resolved
34	  first_raised_round: 0
35	  last_seen_round: 2
36	  resolution: 独立 limitations.tex 已创建。
37	  resolution_round: 3
38	- id: R2-W2
39	  summary: 实验仅用单一模型和单一数据集
40	  category: experiment
41	  severity: critical
42	  status: resolved
43	  first_raised_round: 0
44	  last_seen_round: 2
45	  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。
46	  resolution_round: 3
47	- id: R2-W6
48	  summary: SFT baseline 比较不公平：PR=14% vs 93%
49	  category: experiment
50	  severity: critical
51	  status: resolved
52	  first_raised_round: 0
53	  last_seen_round: 2
54	  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。
55	  resolution_round: 2
56	- id: v2-R1-N1
57	  summary: Abstract '93%' PR 为 single seed
58	  category: writing
59	  severity: critical
60	  status: resolved
61	  first_raised_round: 2
62	  last_seen_round: 3
63	  resolution: Abstract 使用 3-seed pooled mean±std。
64	  resolution_round: 3
65	- id: v2-R1-N3
66	  summary: 仅 2 个 β 值不足以刻画 dose-response
67	  category: experiment
68	  severity: critical
69	  s
…[truncated 45160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 2738 · 2026-05-22T22:57:06.087896+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nwith open('/tmp/review_issues_r31.yaml') as f:\n    print(f.read())\n\" > /tmp/issues_final.txt 2>&1\nwc -c /tmp/issues_final.txt",
  "description": "Prepare final issues content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nwith open('/tmp/review_issues_r31.yaml') as f:\n    print(f.read())\n\" > /tmp/issues_final.txt 2>&1\nwc -c /tmp/issues_final.txt",
    "description": "Prepare final issues content"
  }
}
```

</details>

---


### Tool result

_source line 2739 · 2026-05-22T22:57:06.138867+00:00_

47217 /tmp/issues_final.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2740 · 2026-05-22T22:57:09.905892+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, subprocess\n\nwith open('/tmp/review_issues_r31.yaml') as f:\n    content = f.read()\n\nprint(f\"Issues YAML length: {len(content)} chars\")\nprint(\"First 100 chars:\", content[:100])\nprint(\"Last 100 chars:\", content[-100:])\nPYEOF",
  "description": "Final check of issues content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json, subprocess\n\nwith open('/tmp/review_issues_r31.yaml') as f:\n    content = f.read()\n\nprint(f\"Issues YAML length: {len(content)} chars\")\nprint(\"First 100 chars:\", content[:100])\nprint(\"Last 100 chars:\", content[-100:])\nPYEOF",
    "description": "Final check of issues content"
  }
}
```

</details>

---


### Tool result

_source line 2741 · 2026-05-22T22:57:10.006856+00:00_

Issues YAML length: 40027 chars
First 100 chars: issues:
- id: R1-W1
  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed
  category
Last 100 chars: edundant ISR=0 语义不同，建议 unproved 用 N/A。
  action_items: []
  resolution: ''
  resolution_round: null

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2742 · 2026-05-22T22:57:13.768875+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nwith open('/tmp/review_issues_r31.yaml') as f:\n    issues_yaml = f.read()\n    \n# Write to a temp file that we can reference\nwith open('/tmp/issues_ready.txt', 'w') as f:\n    f.write(issues_yaml)\n    \nprint(\"Ready for MCP submission\")\nprint(f\"Length: {len(issues_yaml)}\")\nPYEOF",
  "description": "Prepare issues for MCP tool"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nwith open('/tmp/review_issues_r31.yaml') as f:\n    issues_yaml = f.read()\n    \n# Write to a temp file that we can reference\nwith open('/tmp/issues_ready.txt', 'w') as f:\n    f.write(issues_yaml)\n    \nprint(\"Ready for MCP submission\")\nprint(f\"Length: {len(issues_yaml)}\")\nPYEOF",
    "description": "Prepare issues for MCP tool"
  }
}
```

</details>

---


### Tool result

_source line 2743 · 2026-05-22T22:57:13.949834+00:00_

Ready for MCP submission
Length: 40027

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 180
}
```

</details>

---


### Tool call

_source line 2744 · 2026-05-22T22:58:05.736017+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n- id: R1-W1\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。\"\n  resolution_round: 2\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识：premise-count matched 后 1.06× (p=0.317) 使 Goodhart 标量证据不成立。R1 建议以 mode-shift 为主证据并提供统计检验。R2 补充：mode-shift ≠ 经典 Goodhart。\"\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 复现：non-hacking ISR vs Random p=0.182 仍不显著。两位 Reviewer 一致要求 Abstract/Title 降级 Goodhart 表述。\"\n- id: v17-R12-W1\n  summary: \"单模型 (Qwen3-4B) 无法支撑通用性声明\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识最严重问题：Qwen3-4B + FOLIO 单模型单数据集，8B/LLaMA 均未收敛。R2 追问是否仅 Qwen3-4B + ProofWriter 的 artifact。\"\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 R1 升为 Must-Fix。R2 同意核心批评但修正真实N=3表述：effective N 在 3-300 间取决于 ICC，建议 mixed-effects model。\"\n- id: v17-R1-W9\n  summary: \"Seed 43 使用 T=0.7 sampling 评估而非 greedy\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识 Must-Fix：seed 43 T=0.7 sampling 混入 pooled analysis 违反受控实验原则。R2 建议主文以排除 s43 为主分析。\"\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R2]\n    note: \"R31 R2 维持 Must-Fix。R1 部分反驳：组合贡献不应简化为标准 LOO 应用，但同意框架级声明需更多实证。\"\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念——本质即 Goodhart's Law\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：observe-vs-optimize asymmetry 本质是 Goodhart 重述。R2 维持 Must-Fix，R1 列为 Should-Fix 但同意措辞需调整。分歧仅在严重程度。\"\n- id: v30-R1-W1\n  summary: \"SFT baseline PR=13% vs exec-only PR=93% 使 ISR 比较存在 selection bias\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识：SFT 应定位为 upper bound 而非 matched control。\"\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：46 proved samples 严重 underpowered。R2 称概念设计巧妙但统计效力不足。\"\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证 50 样本偏少 + recall 未评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：152 样本 precision=1.00 但 recall 不可估。Taxonomy 完备性声明受限。\"\n- id: v19-R12-W3\n  summary: \"ProofFOL p=0.10 被过度引用\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：p=0.10 在 §4.4 用 substantially 表述不当，应改为 directionally consistent。\"\n- id: v30-R2-W3\n  summary: \"ISR 与 NLI accuracy 不相关限制 actionability\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 R2 提出 ISR=0 可能是多条等价推理路径而非结构退化。R1 同意需在主文讨论 ISR=0 语义模糊性。\"\n- id: v31-R2-MR-SPECGAMING\n  summary: \"缺失引用：Towards Understanding Specification Gaming in Reasoning Models (arXiv:2605.02269)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R2]\n    note: \"R2 建议引用并讨论 spec gaming 理论分析与 STA hacking taxonomy 的关系。\"\n- id: v31-R2-W-TITLE-LENGTH\n  summary: \"标题过长（~140 chars），建议精简\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R2]\n    note: \"R2 建议精简至 ~60 chars。R1 反驳无硬限制，可考虑 ~90 chars。\"\n- id: v31-R2-M-ISR0-AMBIGUITY\n  summary: \"ISR=0 对 proved vs unproved 语义不同但用同一值\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1]\n    note: \"R1 M1：unproved ISR=0 与 proved redundant ISR=0 语义不同，建议 unproved 用 N/A。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n- id: R1-W1\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。\"\n  resolution_round: 2\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识：premise-count matched 后 1.06× (p=0.317) 使 Goodhart 标量证据不成立。R1 建议以 mode-shift 为主证据并提供统计检验。R2 补充：mode-shift ≠ 经典 Goodhart。\"\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 复现：non-hacking ISR vs Random p=0.182 仍不显著。两位 Reviewer 一致要求 Abstract/Title 降级 Goodhart 表述。\"\n- id: v17-R12-W1\n  summary: \"单模型 (Qwen3-4B) 无法支撑通用性声明\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识最严重问题：Qwen3-4B + FOLIO 单模型单数据集，8B/LLaMA 均未收敛。R2 追问是否仅 Qwen3-4B + ProofWriter 的 artifact。\"\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 R1 升为 Must-Fix。R2 同意核心批评但修正真实N=3表述：effective N 在 3-300 间取决于 ICC，建议 mixed-effects model。\"\n- id: v17-R1-W9\n  summary: \"Seed 43 使用 T=0.7 sampling 评估而非 greedy\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识 Must-Fix：seed 43 T=0.7 sampling 混入 pooled analysis 违反受控实验原则。R2 建议主文以排除 s43 为主分析。\"\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R2]\n    note: \"R31 R2 维持 Must-Fix。R1 部分反驳：组合贡献不应简化为标准 LOO 应用，但同意框架级声明需更多实证。\"\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念——本质即 Goodhart's Law\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：observe-vs-optimize asymmetry 本质是 Goodhart 重述。R2 维持 Must-Fix，R1 列为 Should-Fix 但同意措辞需调整。分歧仅在严重程度。\"\n- id: v30-R1-W1\n  summary: \"SFT baseline PR=13% vs exec-only PR=93% 使 ISR 比较存在 selection bias\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识：SFT 应定位为 upper bound 而非 matched control。\"\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：46 proved samples 严重 underpowered。R2 称概念设计巧妙但统计效力不足。\"\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证 50 样本偏少 + recall 未评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：152 样本 precision=1.00 但 recall 不可估。Taxonomy 完备性声明受限。\"\n- id: v19-R12-W3\n  summary: \"ProofFOL p=0.10 被过度引用\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：p=0.10 在 §4.4 用 substantially 表述不当，应改为 directionally consistent。\"\n- id: v30-R2-W3\n  summary: \"ISR 与 NLI accuracy 不相关限制 actionability\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 30\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 R2 提出 ISR=0 可能是多条等价推理路径而非结构退化。R1 同意需在主文讨论 ISR=0 语义模糊性。\"\n- id: v31-R2-MR-SPECGAMING\n  summary: \"缺失引用：Towards Understanding Specification Gaming in Reasoning Models (arXiv:2605.02269)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R2]\n    note: \"R2 建议引用并讨论 spec gaming 理论分析与 STA hacking taxonomy 的关系。\"\n- id: v31-R2-W-TITLE-LENGTH\n  summary: \"标题过长（~140 chars），建议精简\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R2]\n    note: \"R2 建议精简至 ~60 chars。R1 反驳无硬限制，可考虑 ~90 chars。\"\n- id: v31-R2-M-ISR0-AMBIGUITY\n  summary: \"ISR=0 对 proved vs unproved 语义不同但用同一值\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1]\n    note: \"R1 M1：unproved ISR=0 与 proved redundant ISR=0 语义不同，建议 unproved 用 N/A。\""
  }
}
```

</details>

---


### Tool result

_source line 2745 · 2026-05-22T22:58:05.786937+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 5106}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2746 · 2026-05-22T23:01:18.674001+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 圆桌审稿报告 — Round 31 (Fresh Review)\n\n**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: Fresh（重新审稿，无历史记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+写作）\n**轮次**: 1 轮（Round 1 初审 → 交叉分享 → 收敛）\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，用于检测 GRPO 训练的神经符号推理模型中的结构退化。核心度量 Intensional Structural Reward (ISR) 衡量每个形式化组件是否为证明成功所必需。论文展示：(1) exec-only GRPO 训练下 ISR 从 ~0.6 崩溃至 ~0.003，揭示 prove rate 不可见的结构退化；(2) 将 ISR 用作训练奖励产生 Goodhart 效应——模型从 conclusion embedding 转向 tautological shortcuts；(3) 该现象在 FOL 和 Prolog 两种逻辑类型间泛化。实验基于 Qwen3-4B + FOLIO 数据集，提出 8 种 hacking mode 分类法。\n\n---\n\n## Strengths\n\n**S1. STA 方法定义清晰、算法化** [R1+R2 共识]\nAlgorithm 1 提供可执行伪代码，ISR 数学定义（Eq. 1）简洁明确，方法可复现性强。将 LOO 消融应用于 solver trace（而非模型参数/特征）是一个非平凡的设计选择。\n\n**S2. 系统的实验设计与控制变量** [R1+R2 共识]\n多条件对比（exec-only, ISR β=0.1/0.2/0.3, Random, Shuffled-ISR, SFT）控制变量合理。Shuffled-ISR 对照（§4.3）巧妙分离 ISR 因果信号与奖励增大的混淆因素——概念设计优于当前统计效力。\n\n**S3. 诚实的局限性披露** [R1+R2 共识]\n论文明确承认 ISR ≠ semantic faithfulness（ρ=-0.049）、premise-count confound 将 ISR 优势降至 1.06×、cross-scale/model 未收敛、seed 43 采样不一致。\"A Case Study\" 标题设定了正确的 scope 期望。这种自我批判态度在提交论文中不常见，值得肯定。\n\n**S4. Hacking Taxonomy 有实用价值** [R1+R2 共识]\n8 种 gaming mode 的定义、示例和检测方法（Appendix D）为后续工作提供可操作的诊断工具包。CE/TS 两种 dominant mode 有充分的样本量支撑（>70 examples each）。\n\n**S5. 有价值的实证发现** [R1+R2 共识]\nGRPO 训练下 ISR 崩溃而 execution accuracy 维持 >90% 的\"结构退化对执行正确性不可见\"发现对 RLVR 社区有警示意义。Per-seed 分析（Tables 9-12）详尽透明。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. Goodhart claim 的核心定量证据被 premise-count confound 瓦解** [R1-N1, R2 AGREE]\nSection 4.3 自行报告 premise-count-matched comparison 后 ISR 优势从 214× 坍缩到仅 1.06×（McNemar p=0.317, n=100 matched pairs）——统计上不显著。C2 贡献（Goodhart 效应）的标量定量基础被自己的控制实验否定。论文试图转向 mode composition shift 作为替代证据，但：(a) mode-shift 的统计检验仅依赖 CMH（见 MF3），(b) 从\"metric 不变但底层结构改变\"推导出\"Goodhart effect\"的论证不够严谨——这更接近 reward shaping 的副作用而非经典 Goodhart。Abstract 中 \"exhibits a seed-dependent Goodhart effect\" 和 Title 中 \"Goodhart Effects\" 的表述暗示了标量层面已被否定的效应。\n**建议**：(1) 以 mode composition shift（CE→TS 转化）为 Goodhart 的主要 operationalization，提供独立的统计检验（χ² test on mode frequencies）；(2) Abstract/Title 降级 Goodhart 表述；(3) 明确区分\"ISR scalar inflation\"（不显著）和\"structural composition shift\"（需独立检验）。\n\n**MF2. 单模型泛化性声明与 cross-scale/cross-model 失败实验的矛盾** [R1-N2, R2-N2, 完全共识]\n全部主实验仅基于 Qwen3-4B + FOLIO（500 训练样本）。三个额外配置均未产生可比较结果：\n- Cross-scale（Qwen3-8B）：PR=14%，未收敛（Appendix E.7）\n- Cross-model（LLaMA-3.2-3B）：训练因零 GRPO advantage 提前终止（Appendix E.4）\n- Exec-only seeds：6 个中仅 3 个收敛（50%，Appendix E.5）\n- ProofFOL ISR：p=0.10，标为 exploratory\nC1 声称 STA 是 \"model-agnostic diagnostic framework\"，C3 声称 \"cross-logic and cross-dataset evidence\"，但实质上论文展示的是一个模型在一个数据集上的一个条件下的现象。ProofFOL 被称为\"cross-dataset\"，但它从 ProofWriter 通过 GPT-4o 翻译得到（Appendix A），与 FOLIO 共享 FOL 语法和推理结构，并非真正独立的数据集。无法排除这些发现是 Qwen3-4B + ProofWriter 的 artifact。\n**建议**：(1) Discussion 泛化性叙事严格限定为 \"hypothesis from a single-model case study\"；(2) 删除或大幅弱化 \"model-agnostic\" 声明；(3) 至少增加 1 个不同架构模型的完整实验。\n\n**MF3. CMH 检验独立性假设不满足，统计推断可靠性存疑** [R1-N3, R2 AGREE with nuance]\nCMH 检验将 within-seed 的 100 个 eval 样本视为独立观测，但同一 seed 下的样本来自同一 model checkpoint，存在 model-level 依赖结构。论文在 §4.1 诚实承认 \"the true replication count is N=3 seeds\"，但仍将 CMH 作为 primary statistical evidence（Table 6 报告 p=1.3×10⁻³⁹ 等极端 p 值）。\nR2 修正：说\"真实 N=3\"过于极端——effective N 在 3-300 之间取决于组内相关系数（ICC）。合适的统计方法是 multilevel/mixed-effects model（seed 作为随机效应），而非简单 CMH。\n**建议**：(1) per-seed analysis 为 primary evidence，CMH 严格降为 supplementary；(2) 报告 ICC 估计值；(3) 用 seed-level clustered bootstrap 或 mixed-effects logistic regression 替代 CMH。\n\n**MF4. Seed 43 采样策略不一致构成显著 confound** [R1-N4, R2 AGREE]\nSeed 43 使用 nucleus sampling（T=0.7）而非其他 seeds 的 greedy decoding（footnote 2, p.5），但仍被纳入主文的 pooled analysis（Table 1 的 \"3-seed pooled\" 统计量包含 seed 43）。Sampling 改变输出分布的 entropy，可能系统性地影响 ISR 值和 hacking mode 分布。在 N=3 seeds 的小样本中，一个 seed 的系统性偏差可能主导 pooled 分析的结论。\n论文在 Appendix E.6 提供了 N=2 sensitivity analysis（Table 13），但 N=2 几乎无统计功效，反而暴露了样本量不足。\n**建议**：(1) 主文分析以排除 seed 43 的结果为主，seed 43 作为 robustness check 放在附录；(2) 明确标注 Table 1 中哪些行包含/排除 seed 43。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. \"Observe-vs-optimize asymmetry\" 概念新颖性声称过度** [R2-N3 Must-Fix, R1-W4 Should-Fix; 分歧记录]\nAbstract 中 \"structural proxies for reasoning quality are easier to observe than to optimize\" 和 C3 贡献声明将此表述为新发现，但本质是 Goodhart's Law 的标准表现。Manheim & Garrabrant (2019) 的四种 Goodhart 变体分类法和 Gao et al. (2023) 的 reward model overoptimization 已系统描述了此类现象。\nR1 部分反驳：论文的贡献不在于\"发现 Goodhart 存在\"，而在于提供 component-level 诊断工具来定位 Goodhart 的具体结构表现形式——这超越了 Manheim & Garrabrant 的理论分类和 Gao et al. 的 aggregate-level 分析。但 R1 同意\"asymmetry\"不应暗示超越 Goodhart 框架的新理论洞察。\n**建议**：将 C3 重新定位为\"在 neurosymbolic RLVR 中通过 STA 实证刻画 Goodhart 的结构层面表现\"，降低新颖性声称力度。\n\n**SF2. 方法论新颖性——LOO 应用层面创新偏薄** [R2-N1 Must-Fix, R1 REBUT; 分歧记录]\nR2 认为 STA 本质是\"LOO 消融应用于 solver 输入组件\"，方法论贡献偏弱，不足以支撑长文。\nR1 反驳：(1) LOO 用于 solver trace 而非模型参数/特征是非平凡设计选择；(2) ISR 将 per-sample LOO 聚合为可用于训练的 reward signal 是新用途；(3) 8 种 hacking mode taxonomy 有实用价值。组合贡献不应简化为\"标准 LOO 的应用\"。但 R1 同意框架级声明（C1: \"diagnostic framework\"）需要多模型验证。\n**建议**：不降为 Short Paper（附录 per-seed 分析和 taxonomy 细节在 Short Paper 格式下无法容纳），但在主文中更明确定位为 \"diagnostic method + empirical case study\" 而非 \"framework\"。\n\n**SF3. SFT baseline 比较不公平** [R1-W1, R2-W4, 共识]\nSFT PR=13% vs exec-only PR=93%，在 prove rate 相差 ~80pp 的情况下比较 structural properties 不令人信服。SFT 直接在 gold formalization 上训练，天然获得结构信息的 direct supervision signal。100-step checkpoint（PR=32%, hacking=31.2% vs SFT 7.7%）仅部分缓解。\n**建议**：明确定位 SFT 为 structural preservation 的 upper bound reference，而非 GRPO 的公平对照。\n\n**SF4. Shuffled-ISR 控制实验严重 underpowered** [R1-W2, R2 AGREE]\nShuffled-ISR condition 仅 46 个 proved samples（3 seeds, PR≈15%），无法提供有意义的统计功效。R2 称其概念设计巧妙但统计功效不足以支撑 deconfounding 声明。\n**建议**：增加 seeds 或在主文中明确标注效力限制。\n\n**SF5. Hacking taxonomy recall 未报告** [R2-W2, R1-W3 AGREE]\nTable 8 报告 152 样本 precision=1.00，但明确写 \"Recall is not estimable\"。一个只有 precision 没有 recall 的分类器无法保证完备性。部分 mode 过于稀少（PG: 5 例, Contradiction: 仅 1000 步出现），存在 over-specification 风险。\n**建议**：(1) 报告 recall 下界估计；(2) 合并稀有 modes 为更粗粒度类别；(3) 明确标注 well-supported vs exploratory modes。\n\n**SF6. ProofFOL p=0.10 在主文中定位不够审慎** [R1-W5, R2 AGREE]\n§4.4 标记 \"exploratory\" 但仍以 \"substantially higher genuine rates\" 叙述，\"substantially\" 与 p=0.10 不匹配。\n**建议**：改为 \"directionally consistent\" 或 \"suggestively higher\"。\n\n**SF7. ISR=0 语义模糊性讨论不充分** [R2-W3, R1 AGREE]\nISR=0 可能是 (a) 冗余前提（结构退化）或 (b) 多条等价推理路径（genuine redundancy）。论文未在主文中讨论 (b) 的可能性。FOL 中多条有效证明路径常见，部分 ISR=0 样本可能语义正确但碰巧所有组件非独立必需。\n**建议**：增加定性分析，展示 low-ISR 样本确实在语义上退化而非仅冗余度增加。\n\n### Minor（不影响接收）\n\n- **M1**: ISR=0 对 proved（complete redundancy）vs unproved（by definition）语义不同但混用同一值，建议 unproved 用 N/A [R1]\n- **M2**: LOO 与 Shapley value 类比（§3.2）可能误导读者认为 STA 继承 Shapley 理论保证 [R1]\n- **M3**: Figure 1 y 轴标签在 ISR-as-reward vs diagnostic ISR 之间含义不同 [R1]\n- **M4**: Table 1 中关键 caveat（1.06× matched value）仅在脚注中 [R1]\n- **M5**: 标题 ~140 chars 偏长，建议精简至 ~90 chars（R2 建议 60 chars，R1 反驳无硬限制）[分歧]\n- **M6**: §4.4 \"persists\" 暗示时间持续性，实际是跨条件一致性，建议改 \"holds\" [R2]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上完全一致：\n\n1. **Overall 3.0 (Findings)** — 方法论贡献（STA/ISR）扎实但实验规模和概念新颖性不足以支撑 Conference\n2. **单模型泛化性不足** (MF2) — 最根本的问题，无法排除 Qwen3-4B + ProofWriter artifact\n3. **Goodhart 标量证据被 confound 瓦解** (MF1) — 1.06× (p=0.317) 使 C2 核心定量支撑不成立\n4. **CMH 统计推断不可靠** (MF3) — within-seed 非独立性使极端 p 值被高估\n5. **Seed 43 confound** (MF4) — 采样策略不一致混入 pooled analysis\n6. **SFT baseline 不公平** (SF3) — PR 差异 ~80pp 使结构比较缺乏说服力\n7. **Taxonomy recall 缺失** (SF5) — 完备性声明受限\n8. **ProofFOL p=0.10 表述过强** (SF6) — \"substantially\" 不匹配\n\n---\n\n## Reviewer Divergence [REBUT]\n\n| 议题 | R1 | R2 | 最终定级 |\n|------|----|----|----------|\n| 方法论新颖性 (SF2) | Should-Fix: 组合贡献有价值 | Must-Fix: LOO 应用偏薄 | Should-Fix (分歧记录) |\n| Asymmetry 概念 (SF1) | Should-Fix: 可作 shorthand | Must-Fix: Goodhart 重述 | Should-Fix (分歧记录) |\n| 标题长度 (M5) | Minor: ACL 无硬限制 | Should-Fix: 建议 60 chars | Minor (分歧记录) |\n| Excitement | 3.5/5 | 2.5/5 | — |\n\n---\n\n## Questions to Authors\n\n1. 如果排除 seed 43，主要结论（Table 1 pooled statistics, CMH 检验）是否仍成立？请提供 2-seed (42, 44) pooled 结果。\n2. 能否提供 mode 分布在 ISR-as-reward vs exec-only 之间变化的正式统计检验（Fisher exact / χ² test on mode frequencies）？这将为 MF1 的 Goodhart claim 提供替代性定量支撑。\n3. 为什么选择 multiplicative reward formulation 而非 additive？Multiplicative form 使 ISR 信号强度与 prove rate 耦合，这本身可能驱动部分观察到的 Goodhart 模式。\n4. Cross-scale (8B) 和 cross-model (LLaMA) 均未收敛。是否考虑过更简约的解释——即 STA/ISR 诊断的现象可能是 Qwen3-4B 特有的训练动态？\n5. LOO 假设 component independence，但逻辑前提之间常有交互（如三段论的大小前提缺一不可）。在 LOO 下观察到的 hacking patterns 是否可能因忽略交互而产生 false positives？\n6. 8 种 hacking mode 中 CE (87%) 和 TS (71%) 占绝大多数。如果仅关注这两种 dominant mode，简单的 text-match classifier 是否就足以检测这些退化模式？STA/ISR 的额外价值在哪里？\n\n---\n\n## Missing References\n\n- **\"Towards Understanding Specification Gaming in Reasoning Models\"** (arXiv:2605.02269, 2025) — spec gaming 理论分析与本文 hacking taxonomy 直接相关 [R2]\n- **Cobbe et al. (2021)** \"Training verifiers to solve math word problems\" — 与 component-level reward 诊断相关，已引用但未在 Related Work 讨论 [R1]\n- **Khalifa et al. (2026)** \"Countdown-Code\" — 已引用但 §2 中未讨论其 testbed 方法与 STA 的关系 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~4 min）。结果：0 critical / 2 warning / 16 info。\n\n**Warnings:**\n1. **Pages 5-6**：连续 2 页纯文本（Section 4.1-4.3），无 figure/table/display equation 穿插。建议将 Table 1 或 Table 2 前移至 page 6 位置。\n2. **Page 19 (Appendix)**：Table 9 字号明显偏小（~6-7pt），在打印或低分辨率屏幕上可能难以阅读。\n\n**Info 亮点**：\n- 主文正好 8 页，符合 ACL 页数限制\n- 无 margin overflow、LaTeX 渲染错误、孤悬 section heading\n- 双栏对齐良好，页眉符合 ACL 匿名投稿格式\n- Figure 1 出现在 page 2 顶部，锚定效果好\n- Algorithm 1 排版规范\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n**EMNLP 2026 评分标准**：3 = Findings（可被 Findings 接收）\n\n**置信度**: 4/5（两位 Reviewer 均仔细阅读全文含 23 页附录，熟悉 RLVR/neurosymbolic reasoning 领域）\n\n**评分理由**：\n论文提出了一个有前景的诊断工具（STA/ISR），在 neurosymbolic reasoning 的 reward hacking 检测中填补了 execution-based evaluation 和 annotation-free diagnostics 之间的空白。核心方法论贡献（C1: STA 框架 + hacking taxonomy）扎实。\n\n但三个根本性问题限制了 Conference 接收：\n1. **Goodhart 效应的核心定量证据被 premise-count matching 消解**（1.06×, p=0.317）——C2 的可信度大幅下降\n2. **泛化性声明与 cross-scale/cross-model 全部未收敛的实验现实矛盾**——无法排除 Qwen3-4B + ProofWriter artifact\n3. **统计推断依赖不满足独立性假设的 CMH 检验**——极端 p 值可能被严重高估\n\n这些问题的组合——Goodhart 定量基础薄弱 + 单模型实验规模 + 统计方法问题——使论文难以达到 EMNLP 主会议标准（Overall ≥ 4），但 empirical findings 和诊断工具对 RLVR 社区有参考价值，适合 Findings 接收。\n\n**若要冲刺主会议**：(1) 至少在 1-2 个不同架构模型上验证 STA（需成功收敛）；(2) 以 mode composition shift 为 Goodhart 主要证据并提供独立统计检验；(3) 用 mixed-effects model 替代 CMH；(4) 将 claims 严格限定在证据支持的范围内。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- C1 \"model-agnostic diagnostic framework\" 声明与单模型实验不匹配，建议改为 \"diagnostic method\"\n- C3 \"observe-vs-optimize asymmetry\" 应明确定位为 Goodhart 的 domain-specific 实证验证，而非新概念\n\n### §3.2 Method — ISR\n- ISR=0 对 proved（redundancy）vs unproved（by definition）语义不同，建议 unproved 用 N/A\n- Shapley value 类比可能误导，建议简化为 \"LOO ablation\"\n- ISR 对不同 hacking modes 诊断力差异巨大（CE: ISR≈0; TS: ISR≈1 by construction），需在主文讨论\n\n### §4.1 Setup\n- Seed 43 nucleus sampling 应从 pooled analysis 中排除，或至少双报包含/排除结果\n- \"Statistical considerations\" 段需更明确声明 CMH 的 supplementary 角色\n\n### §4.2 ISR as Diagnostic\n- \"214× raw drop\" 叙事需在首次出现时即附加 \"partially attributable to premise-count inflation\" caveat\n- SFT 对比：明确定位为 \"pre-RL structural upper bound\"，而非 PR-matched control\n\n### §4.3 Goodhart Effects\n- 核心建议：以 mode composition shift 为 primary Goodhart evidence，提供 χ² 检验\n- \"Premise-count confound\" 段应前置而非作为后续讨论\n- Table 1 脚注中的关键信息（1.06× matched value）应在正文中突出\n\n### §4.4 Cross-Domain\n- ProofFOL \"substantially higher\" → \"directionally consistent\"（p=0.10）\n- \"Cross-dataset\" 不准确——ProofFOL 与 FOLIO 共享 FOL 语法和 ProofWriter 推理结构\n\n### §5 Discussion\n- \"STA generalizes to any RL system\" 过强，建议改为 \"STA is applicable in principle to...\"\n- \"Goldilocks\" 全文确认已统一为 \"observation\"",
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 Findings",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 圆桌审稿报告 — Round 31 (Fresh Review)\n\n**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: Fresh（重新审稿，无历史记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+写作）\n**轮次**: 1 轮（Round 1 初审 → 交叉分享 → 收敛）\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，用于检测 GRPO 训练的神经符号推理模型中的结构退化。核心度量 Intensional Structural Reward (ISR) 衡量每个形式化组件是否为证明成功所必需。论文展示：(1) exec-only GRPO 训练下 ISR 从 ~0.6 崩溃至 ~0.003，揭示 prove rate 不可见的结构退化；(2) 将 ISR 用作训练奖励产生 Goodhart 效应——模型从 conclusion embedding 转向 tautological shortcuts；(3) 该现象在 FOL 和 Prolog 两种逻辑类型间泛化。实验基于 Qwen3-4B + FOLIO 数据集，提出 8 种 hacking mode 分类法。\n\n---\n\n## Strengths\n\n**S1. STA 方法定义清晰、算法化** [R1+R2 共识]\nAlgorithm 1 提供可执行伪代码，ISR 数学定义（Eq. 1）简洁明确，方法可复现性强。将 LOO 消融应用于 solver trace（而非模型参数/特征）是一个非平凡的设计选择。\n\n**S2. 系统的实验设计与控制变量** [R1+R2 共识]\n多条件对比（exec-only, ISR β=0.1/0.2/0.3, Random, Shuffled-ISR, SFT）控制变量合理。Shuffled-ISR 对照（§4.3）巧妙分离 ISR 因果信号与奖励增大的混淆因素——概念设计优于当前统计效力。\n\n**S3. 诚实的局限性披露** [R1+R2 共识]\n论文明确承认 ISR ≠ semantic faithfulness（ρ=-0.049）、premise-count confound 将 ISR 优势降至 1.06×、cross-scale/model 未收敛、seed 43 采样不一致。\"A Case Study\" 标题设定了正确的 scope 期望。这种自我批判态度在提交论文中不常见，值得肯定。\n\n**S4. Hacking Taxonomy 有实用价值** [R1+R2 共识]\n8 种 gaming mode 的定义、示例和检测方法（Appendix D）为后续工作提供可操作的诊断工具包。CE/TS 两种 dominant mode 有充分的样本量支撑（>70 examples each）。\n\n**S5. 有价值的实证发现** [R1+R2 共识]\nGRPO 训练下 ISR 崩溃而 execution accuracy 维持 >90% 的\"结构退化对执行正确性不可见\"发现对 RLVR 社区有警示意义。Per-seed 分析（Tables 9-12）详尽透明。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. Goodhart claim 的核心定量证据被 premise-count confound 瓦解** [R1-N1, R2 AGREE]\nSection 4.3 自行报告 premise-count-matched comparison 后 ISR 优势从 214× 坍缩到仅 1.06×（McNemar p=0.317, n=100 matched pairs）——统计上不显著。C2 贡献（Goodhart 效应）的标量定量基础被自己的控制实验否定。论文试图转向 mode composition shift 作为替代证据，但：(a) mode-shift 的统计检验仅依赖 CMH（见 MF3），(b) 从\"metric 不变但底层结构改变\"推导出\"Goodhart effect\"的论证不够严谨——这更接近 reward shaping 的副作用而非经典 Goodhart。Abstract 中 \"exhibits a seed-dependent Goodhart effect\" 和 Title 中 \"Goodhart Effects\" 的表述暗示了标量层面已被否定的效应。\n**建议**：(1) 以 mode composition shift（CE→TS 转化）为 Goodhart 的主要 operationalization，提供独立的统计检验（χ² test on mode frequencies）；(2) Abstract/Title 降级 Goodhart 表述；(3) 明确区分\"ISR scalar inflation\"（不显著）和\"structural composition shift\"（需独立检验）。\n\n**MF2. 单模型泛化性声明与 cross-scale/cross-model 失败实验的矛盾** [R1-N2, R2-N2, 完全共识]\n全部主实验仅基于 Qwen3-4B + FOLIO（500 训练样本）。三个额外配置均未产生可比较结果：\n- Cross-scale（Qwen3-8B）：PR=14%，未收敛（Appendix E.7）\n- Cross-model（LLaMA-3.2-3B）：训练因零 GRPO advantage 提前终止（Appendix E.4）\n- Exec-only seeds：6 个中仅 3 个收敛（50%，Appendix E.5）\n- ProofFOL ISR：p=0.10，标为 exploratory\nC1 声称 STA 是 \"model-agnostic diagnostic framework\"，C3 声称 \"cross-logic and cross-dataset evidence\"，但实质上论文展示的是一个模型在一个数据集上的一个条件下的现象。ProofFOL 被称为\"cross-dataset\"，但它从 ProofWriter 通过 GPT-4o 翻译得到（Appendix A），与 FOLIO 共享 FOL 语法和推理结构，并非真正独立的数据集。无法排除这些发现是 Qwen3-4B + ProofWriter 的 artifact。\n**建议**：(1) Discussion 泛化性叙事严格限定为 \"hypothesis from a single-model case study\"；(2) 删除或大幅弱化 \"model-agnostic\" 声明；(3) 至少增加 1 个不同架构模型的完整实验。\n\n**MF3. CMH 检验独立性假设不满足，统计推断可靠性存疑** [R1-N3, R2 AGREE with nuance]\nCMH 检验将 within-seed 的 100 个 eval 样本视为独立观测，但同一 seed 下的样本来自同一 model checkpoint，存在 model-level 依赖结构。论文在 §4.1 诚实承认 \"the true replication count is N=3 seeds\"，但仍将 CMH 作为 primary statistical evidence（Table 6 报告 p=1.3×10⁻³⁹ 等极端 p 值）。\nR2 修正：说\"真实 N=3\"过于极端——effective N 在 3-300 之间取决于组内相关系数（ICC）。合适的统计方法是 multilevel/mixed-effects model（seed 作为随机效应），而非简单 CMH。\n**建议**：(1) per-seed analysis 为 primary evidence，CMH 严格降为 supplementary；(2) 报告 ICC 估计值；(3) 用 seed-level clustered bootstrap 或 mixed-effects logistic regression 替代 CMH。\n\n**MF4. Seed 43 采样策略不一致构成显著 confound** [R1-N4, R2 AGREE]\nSeed 43 使用 nucleus sampling（T=0.7）而非其他 seeds 的 greedy decoding（footnote 2, p.5），但仍被纳入主文的 pooled analysis（Table 1 的 \"3-seed pooled\" 统计量包含 seed 43）。Sampling 改变输出分布的 entropy，可能系统性地影响 ISR 值和 hacking mode 分布。在 N=3 seeds 的小样本中，一个 seed 的系统性偏差可能主导 pooled 分析的结论。\n论文在 Appendix E.6 提供了 N=2 sensitivity analysis（Table 13），但 N=2 几乎无统计功效，反而暴露了样本量不足。\n**建议**：(1) 主文分析以排除 seed 43 的结果为主，seed 43 作为 robustness check 放在附录；(2) 明确标注 Table 1 中哪些行包含/排除 seed 43。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. \"Observe-vs-optimize asymmetry\" 概念新颖性声称过度** [R2-N3 Must-Fix, R1-W4 Should-Fix; 分歧记录]\nAbstract 中 \"structural proxies for reasoning quality are easier to observe than to optimize\" 和 C3 贡献声明将此表述为新发现，但本质是 Goodhart's Law 的标准表现。Manheim & Garrabrant (2019) 的四种 Goodhart 变体分类法和 Gao et al. (2023) 的 reward model overoptimization 已系统描述了此类现象。\nR1 部分反驳：论文的贡献不在于\"发现 Goodhart 存在\"，而在于提供 component-level 诊断工具来定位 Goodhart 的具体结构表现形式——这超越了 Manheim & Garrabrant 的理论分类和 Gao et al. 的 aggregate-level 分析。但 R1 同意\"asymmetry\"不应暗示超越 Goodhart 框架的新理论洞察。\n**建议**：将 C3 重新定位为\"在 neurosymbolic RLVR 中通过 STA 实证刻画 Goodhart 的结构层面表现\"，降低新颖性声称力度。\n\n**SF2. 方法论新颖性——LOO 应用层面创新偏薄** [R2-N1 Must-Fix, R1 REBUT; 分歧记录]\nR2 认为 STA 本质是\"LOO 消融应用于 solver 输入组件\"，方法论贡献偏弱，不足以支撑长文。\nR1 反驳：(1) LOO 用于 solver trace 而非模型参数/特征是非平凡设计选择；(2) ISR 将 per-sample LOO 聚合为可用于训练的 reward signal 是新用途；(3) 8 种 hacking mode taxonomy 有实用价值。组合贡献不应简化为\"标准 LOO 的应用\"。但 R1 同意框架级声明（C1: \"diagnostic framework\"）需要多模型验证。\n**建议**：不降为 Short Paper（附录 per-seed 分析和 taxonomy 细节在 Short Paper 格式下无法容纳），但在主文中更明确定位为 \"diagnostic method + empirical case study\" 而非 \"framework\"。\n\n**SF3. SFT baseline 比较不公平** [R1-W1, R2-W4, 共识]\nSFT PR=13% vs exec-only PR=93%，在 prove rate 相差 ~80pp 的情况下比较 structural properties 不令人信服。SFT 直接在 gold formalization 上训练，天然获得结构信息的 direct supervision signal。100-step checkpoint（PR=32%, hacking=31.2% vs SFT 7.7%）仅部分缓解。\n**建议**：明确定位 SFT 为 structural preservation 的 upper bound reference，而非 GRPO 的公平对照。\n\n**SF4. Shuffled-ISR 控制实验严重 underpowered** [R1-W2, R2 AGREE]\nShuffled-ISR condition 仅 46 个 proved samples（3 seeds, PR≈15%），无法提供有意义的统计功效。R2 称其概念设计巧妙但统计功效不足以支撑 deconfounding 声明。\n**建议**：增加 seeds 或在主文中明确标注效力限制。\n\n**SF5. Hacking taxonomy recall 未报告** [R2-W2, R1-W3 AGREE]\nTable 8 报告 152 样本 precision=1.00，但明确写 \"Recall is not estimable\"。一个只有 precision 没有 recall 的分类器无法保证完备性。部分 mode 过于稀少（PG: 5 例, Contradiction: 仅 1000 步出现），存在 over-specification 风险。\n**建议**：(1) 报告 recall 下界估计；(2) 合并稀有 modes 为更粗粒度类别；(3) 明确标注 well-supported vs exploratory modes。\n\n**SF6. ProofFOL p=0.10 在主文中定位不够审慎** [R1-W5, R2 AGREE]\n§4.4 标记 \"exploratory\" 但仍以 \"substantially higher genuine rates\" 叙述，\"substantially\" 与 p=0.10 不匹配。\n**建议**：改为 \"directionally consistent\" 或 \"suggestively higher\"。\n\n**SF7. ISR=0 语义模糊性讨论不充分** [R2-W3, R1 AGREE]\nISR=0 可能是 (a) 冗余前提（结构退化）或 (b) 多条等价推理路径（genuine redundancy）。论文未在主文中讨论 (b) 的可能性。FOL 中多条有效证明路径常见，部分 ISR=0 样本可能语义正确但碰巧所有组件非独立必需。\n**建议**：增加定性分析，展示 low-ISR 样本确实在语义上退化而非仅冗余度增加。\n\n### Minor（不影响接收）\n\n- **M1**: ISR=0 对 proved（complete redundancy）vs unproved（by definition）语义不同但混用同一值，建议 unproved 用 N/A [R1]\n- **M2**: LOO 与 Shapley value 类比（§3.2）可能误导读者认为 STA 继承 Shapley 理论保证 [R1]\n- **M3**: Figure 1 y 轴标签在 ISR-as-reward vs diagnostic ISR 之间含义不同 [R1]\n- **M4**: Table 1 中关键 caveat（1.06× matched value）仅在脚注中 [R1]\n- **M5**: 标题 ~140 chars 偏长，建议精简至 ~90 chars（R2 建议 60 chars，R1 反驳无硬限制）[分歧]\n- **M6**: §4.4 \"persists\" 暗示时间持续性，实际是跨条件一致性，建议改 \"holds\" [R2]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上完全一致：\n\n1. **Overall 3.0 (Findings)** — 方法论贡献（STA/ISR）扎实但实验规模和概念新颖性不足以支撑 Conference\n2. **单模型泛化性不足** (MF2) — 最根本的问题，无法排除 Qwen3-4B + ProofWriter artifact\n3. **Goodhart 标量证据被 confound 瓦解** (MF1) — 1.06× (p=0.317) 使 C2 核心定量支撑不成立\n4. **CMH 统计推断不可靠** (MF3) — within-seed 非独立性使极端 p 值被高估\n5. **Seed 43 confound** (MF4) — 采样策略不一致混入 pooled analysis\n6. **SFT baseline 不公平** (SF3) — PR 差异 ~80pp 使结构比较缺乏说服力\n7. **Taxonomy recall 缺失** (SF5) — 完备性声明受限\n8. **ProofFOL p=0.10 表述过强** (SF6) — \"substantially\" 不匹配\n\n---\n\n## Reviewer Divergence [REBUT]\n\n| 议题 | R1 | R2 | 最终定级 |\n|------|----|----|----------|\n| 方法论新颖性 (SF2) | Should-Fix: 组合贡献有价值 | Must-Fix: LOO 应用偏薄 | Should-Fix (分歧记录) |\n| Asymmetry 概念 (SF1) | Should-Fix: 可作 shorthand | Must-Fix: Goodhart 重述 | Should-Fix (分歧记录) |\n| 标题长度 (M5) | Minor: ACL 无硬限制 | Should-Fix: 建议 60 chars | Minor (分歧记录) |\n| Excitement | 3.5/5 | 2.5/5 | — |\n\n---\n\n## Questions to Authors\n\n1. 如果排除 seed 43，主要结论（Table 1 pooled statistics, CMH 检验）是否仍成立？请提供 2-seed (42, 44) pooled 结果。\n2. 能否提供 mode 分布在 ISR-as-reward vs exec-only 之间变化的正式统计检验（Fisher exact / χ² test on mode frequencies）？这将为 MF1 的 Goodhart claim 提供替代性定量支撑。\n3. 为什么选择 multiplicative reward formulation 而非 additive？Multiplicative form 使 ISR 信号强度与 prove rate 耦合，这本身可能驱动部分观察到的 Goodhart 模式。\n4. Cross-scale (8B) 和 cross-model (LLaMA) 均未收敛。是否考虑过更简约的解释——即 STA/ISR 诊断的现象可能是 Qwen3-4B 特有的训练动态？\n5. LOO 假设 component independence，但逻辑前提之间常有交互（如三段论的大小前提缺一不可）。在 LOO 下观察到的 hacking patterns 是否可能因忽略交互而产生 false positives？\n6. 8 种 hacking mode 中 CE (87%) 和 TS (71%) 占绝大多数。如果仅关注这两种 dominant mode，简单的 text-match classifier 是否就足以检测这些退化模式？STA/ISR 的额外价值在哪里？\n\n---\n\n## Missing References\n\n- **\"Towards Understanding Specification Gaming in Reasoning Models\"** (arXiv:2605.02269, 2025) — spec gaming 理论分析与本文 hacking taxonomy 直接相关 [R2]\n- **Cobbe et al. (2021)** \"Training verifiers to solve math word problems\" — 与 component-level reward 诊断相关，已引用但未在 Related Work 讨论 [R1]\n- **Khalifa et al. (2026)** \"Countdown-Code\" — 已引用但 §2 中未讨论其 testbed 方法与 STA 的关系 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~4 min）。结果：0 critical / 2 warning / 16 info。\n\n**Warnings:**\n1. **Pages 5-6**：连续 2 页纯文本（Section 4.1-4.3），无 figure/table/display equation 穿插。建议将 Table 1 或 Table 2 前移至 page 6 位置。\n2. **Page 19 (Appendix)**：Table 9 字号明显偏小（~6-7pt），在打印或低分辨率屏幕上可能难以阅读。\n\n**Info 亮点**：\n- 主文正好 8 页，符合 ACL 页数限制\n- 无 margin overflow、LaTeX 渲染错误、孤悬 section heading\n- 双栏对齐良好，页眉符合 ACL 匿名投稿格式\n- Figure 1 出现在 page 2 顶部，锚定效果好\n- Algorithm 1 排版规范\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n**EMNLP 2026 评分标准**：3 = Findings（可被 Findings 接收）\n\n**置信度**: 4/5（两位 Reviewer 均仔细阅读全文含 23 页附录，熟悉 RLVR/neurosymbolic reasoning 领域）\n\n**评分理由**：\n论文提出了一个有前景的诊断工具（STA/ISR），在 neurosymbolic reasoning 的 reward hacking 检测中填补了 execution-based evaluation 和 annotation-free diagnostics 之间的空白。核心方法论贡献（C1: STA 框架 + hacking taxonomy）扎实。\n\n但三个根本性问题限制了 Conference 接收：\n1. **Goodhart 效应的核心定量证据被 premise-count matching 消解**（1.06×, p=0.317）——C2 的可信度大幅下降\n2. **泛化性声明与 cross-scale/cross-model 全部未收敛的实验现实矛盾**——无法排除 Qwen3-4B + ProofWriter artifact\n3. **统计推断依赖不满足独立性假设的 CMH 检验**——极端 p 值可能被严重高估\n\n这些问题的组合——Goodhart 定量基础薄弱 + 单模型实验规模 + 统计方法问题——使论文难以达到 EMNLP 主会议标准（Overall ≥ 4），但 empirical findings 和诊断工具对 RLVR 社区有参考价值，适合 Findings 接收。\n\n**若要冲刺主会议**：(1) 至少在 1-2 个不同架构模型上验证 STA（需成功收敛）；(2) 以 mode composition shift 为 Goodhart 主要证据并提供独立统计检验；(3) 用 mixed-effects model 替代 CMH；(4) 将 claims 严格限定在证据支持的范围内。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- C1 \"model-agnostic diagnostic framework\" 声明与单模型实验不匹配，建议改为 \"diagnostic method\"\n- C3 \"observe-vs-optimize asymmetry\" 应明确定位为 Goodhart 的 domain-specific 实证验证，而非新概念\n\n### §3.2 Method — ISR\n- ISR=0 对 proved（redundancy）vs unproved（by definition）语义不同，建议 unproved 用 N/A\n- Shapley value 类比可能误导，建议简化为 \"LOO ablation\"\n- ISR 对不同 hacking modes 诊断力差异巨大（CE: ISR≈0; TS: ISR≈1 by construction），需在主文讨论\n\n### §4.1 Setup\n- Seed 43 nucleus sampling 应从 pooled analysis 中排除，或至少双报包含/排除结果\n- \"Statistical considerations\" 段需更明确声明 CMH 的 supplementary 角色\n\n### §4.2 ISR as Diagnostic\n- \"214× raw drop\" 叙事需在首次出现时即附加 \"partially attributable to premise-count inflation\" caveat\n- SFT 对比：明确定位为 \"pre-RL structural upper bound\"，而非 PR-matched control\n\n### §4.3 Goodhart Effects\n- 核心建议：以 mode composition shift 为 primary Goodhart evidence，提供 χ² 检验\n- \"Premise-count confound\" 段应前置而非作为后续讨论\n- Table 1 脚注中的关键信息（1.06× matched value）应在正文中突出\n\n### §4.4 Cross-Domain\n- ProofFOL \"substantially higher\" → \"directionally consistent\"（p=0.10）\n- \"Cross-dataset\" 不准确——ProofFOL 与 FOLIO 共享 FOL 语法和 ProofWriter 推理结构\n\n### §5 Discussion\n- \"STA generalizes to any RL system\" 过强，建议改为 \"STA is applicable in principle to...\"\n- \"Goldilocks\" 全文确认已统一为 \"observation\"",
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 Findings",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 2747 · 2026-05-22T23:01:22.891635+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4217
}
```

</details>

---


### Assistant

_source line 2748 · 2026-05-22T23:01:35.433084+00:00_

审稿报告已投递至 Research Director。

**圆桌审稿完成摘要**：

- **Overall: 3.0 (Findings)**，两位 Reviewer 完全一致
- **4 个 Must-Fix**：Goodhart 标量证据被 premise-count confound 消解（1.06×, p=0.317）、单模型泛化性不足（8B/LLaMA 均未收敛）、CMH 独立性假设不满足、Seed 43 采样不一致混入 pooled analysis
- **7 个 Should-Fix**：asymmetry 概念新颖性过度声称、方法论 LOO 新颖性偏薄（分歧记录）、SFT baseline 不公平、Shuffled-ISR underpowered、taxonomy recall 缺失、ProofFOL p=0.10 表述过强、ISR=0 语义模糊
- **核心共识**：方法论贡献（STA + taxonomy）扎实，empirical findings 有信息价值，但实验规模 + Goodhart 定量基础 + 统计方法的组合短板使论文不足以 Conference 接收，适合 Findings

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 251

## Round 251

2 recorded events


### User

_source line 2749 · 2026-05-22T23:01:38.072063+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

两份审稿意见的核心共识：Overall 3.0 (Findings)。R1 和 R2 在单模型泛化性、Goodhart claim 的统计支撑不足、概念新颖性过度声称三个关键问题上完全一致。R2 在方法论新颖性（LOO 应用偏薄）上比 R1 更严格，R1 在 premise-count confound 和 CMH 统计问题上比 R2 更深入。两份意见互补，形成了对论文优势（系统实验设计、诚实披露）和不足（规模小、新颖性有限）的完整评估。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2750 · 2026-05-22T23:01:51.543935+00:00_

审稿报告已投递至 Research Director。

**审稿结论**：Overall **3.0 (Findings)**，两位 Reviewer 完全一致。

**4 个 Must-Fix**：
1. Goodhart 标量证据被 premise-count confound 消解（1.06×, p=0.317）
2. 单模型（Qwen3-4B）泛化性声明与 cross-scale/cross-model 全部未收敛矛盾
3. CMH 独立性假设不满足，极端 p 值被高估
4. Seed 43 采样不一致混入 pooled analysis

**7 个 Should-Fix**：asymmetry 概念 overclaiming、方法论新颖性偏薄、SFT baseline 不公平、Shuffled-ISR underpowered、taxonomy recall 缺失、ProofFOL 表述过强、ISR=0 语义模糊

**核心判断**：STA 诊断工具和 hacking taxonomy 有实用价值，empirical findings 对 RLVR 社区有参考意义，但方法新颖性 + 单模型实验规模 + Goodhart 定量基础薄弱的组合不足以支撑 Conference 接收，适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 252

## Round 252

54 recorded events


### User

_source line 2751 · 2026-05-22T23:21:08.632059+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2752 · 2026-05-22T23:21:14.833854+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2753 · 2026-05-22T23:21:14.886106+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 2754 · 2026-05-22T23:21:21.216308+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2755 · 2026-05-22T23:21:21.317473+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2756 · 2026-05-22T23:21:24.831154+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2757 · 2026-05-22T23:21:24.881868+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2758 · 2026-05-22T23:21:29.241114+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2759 · 2026-05-22T23:21:30.647187+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (216 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d158_llama_sft_s42（准备中）\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical powe
…[truncated 1872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 2760 · 2026-05-22T23:21:31.199790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2761 · 2026-05-22T23:21:31.501445+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage{float}
13	\usepackage{placeins}
14	\usepackage[protrusion=true,expansion=false]{microtype}
15	
16	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
18	\setlength{\abovecaptionskip}{4pt}
19	\setlength{\belowcaptionskip}{2pt}
20	
21	\graphicspath{{figures/}}
22	
23	\title{Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study}
24	
25	\author{Anonymous ACL submission}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	\input{introduction}
32	\input{related_work}
33	\input{method}
34	\input{experiments}
35	\input{conclusion}
36	
37	\input{limitations}
38	
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\appendix
44	\input{appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2762 · 2026-05-22T23:21:31.501915+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 2763 · 2026-05-22T23:21:36.922259+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found search results related to EMNLP 2026, but they primarily show information about workshops and tutorials associated with
…[truncated 1075 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5420
}
```

</details>

---


### Tool call

_source line 2764 · 2026-05-22T23:21:41.188836+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission deadline ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission deadline ARR"
  }
}
```

</details>

---


### Tool call

_source line 2765 · 2026-05-22T23:21:41.892186+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission deadline May June author guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission deadline May June author guidelines page limit"
  }
}
```

</details>

---


### Tool result

_source line 2766 · 2026-05-22T23:21:47.363419+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"}]

Based on the search results, here is the information about EMNLP 2026 main conference call for papers submission dea
…[truncated 1091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6174
}
```

</details>

---


### Tool result

_source line 2767 · 2026-05-22T23:21:53.287407+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission deadline May June author guidelines page limit"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Now let me search for more specific information about page limits and May/June 2026 deadlines:

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistic
…[truncated 3536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 11395
}
```

</details>

---


### Tool call

_source line 2768 · 2026-05-22T23:22:06.844053+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org calls main conference papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org calls main conference papers"
  }
}
```

</details>

---


### Tool call

_source line 2769 · 2026-05-22T23:22:09.304817+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2770 · 2026-05-22T23:22:09.706922+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2771 · 2026-05-22T23:22:09.958476+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2772 · 2026-05-22T23:22:13.465676+00:00_

Web search results for query: "site:2026.emnlp.org calls main conference papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Leveraging Large Language Models for Improved Understanding of Communications With Patients With Cancer in a Call Center Setting: Proof-of-Concept Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11669882/"},{"title":"Natural language processing for humanitarian action: Opportunities, challenges, and the path toward humanitarian NLP","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10080095/"}]

I found the Call for Main Conference Papers for EMNLP 2026. Here are the key details:

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

**Submission Details:**
- Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.
- Dual submissions are not allowed!
- Papers that have received reviews and a meta-review from ARR may
…[truncated 309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6621
}
```

</details>

---


### Tool result

_source line 2773 · 2026-05-22T23:22:13.466238+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3507
}
```

</details>

---


### Tool call

_source line 2774 · 2026-05-22T23:22:17.281555+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2775 · 2026-05-22T23:22:17.332281+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2776 · 2026-05-22T23:22:21.497872+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2777 · 2026-05-22T23:22:22.704149+00:00_

1	issues:
2	- id: R1-W1
3	  summary: "统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed"
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 0
8	  last_seen_round: 2
9	  resolution: "β=0.3 ISR 和 Random 各 3 seeds 已完成。"
10	  resolution_round: 2
11	- id: v22-R12-N3
12	  summary: "Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）"
13	  category: method
14	  severity: critical
15	  status: resolved
16	  first_raised_round: 22
17	  last_seen_round: 31
18	  resolution: "Two-level Goodhart separation: scalar confound acknowledged (McNemar p=0.317 n.s.), compositional mode shift established as primary evidence via seed-stratified χ² (174.8, p<10⁻³⁸)."
19	  resolution_round: 31
20	  mentions:
21	  - round: 31
22	    reviewers: [R1, R2]
23	    note: "R31 两位 Reviewer 共识：premise-count matched 后 1.06× (p=0.317) 使 Goodhart 标量证据不成立。R1 建议以 mode-shift 为主证据并提供统计检验。R2 补充：mode-shift ≠ 经典 Goodhart。"
24	- id: v22-R12-N1
25	  summary: "ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果"
26	  category: framing
27	  severity: critical
28	  status: resolved
29	  first_raised_round: 22
30	  last_seen_round: 31
31	  resolution: "Compositional Goodhart reframed around mode shift (CE→TS), not scalar non-hacking rate. χ² test (174.8, p<10⁻³⁸) as independent evidence. Per-seed analysis all independently significant."
32	  resolution_round: 31
33	  mentions:
34	  - round: 31
35	    reviewers: [R1, R2]
36	    note: "R31 复现：non-hacking ISR vs Random p=0.182 仍不显著。两位 Reviewer 一致要求 Abstract/Title 降级 Goodhart 表述。"
37	- id: v17-R12-W1
38	  summary: "单模型 (Qwen3-4B) 无法支撑通用性声明"
39	  category: experiment
40	  severity: critical
41	  status: in_progress
42	  first_raised_round: 17
43	  last_seen_round: 31
44	  resolution: "C1 scoped to 'model-agnostic diagnostic method' (design property); C2/C3 scoped to 'in Qwen3-4B experiments'. Cannot add models (8B/LLaMA non-convergence). Fundamental limitation acknowledged."
45	  mentions:
46	  - round:
…[truncated 6429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 1206
}
```

</details>

---


### Tool call

_source line 2778 · 2026-05-22T23:22:22.855189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2779 · 2026-05-22T23:22:22.855546+00:00_

1	\begin{abstract}
2	Execution-based evaluation of neurosymbolic reasoning conflates faithful derivation with structural shortcuts: a formalization that trivially embeds the conclusion among its premises proves just as reliably as a genuine one, and RL optimizers exploit this indifference.
3	We propose \emph{component necessity} as a diagnostic principle and operationalize it as \emph{Solver Trace Ablation} (STA): for each proved output, STA tests whether every component is individually required for proof success, yielding the \emph{Intensional Structural Reward} (ISR).
4	ISR reveals structural degeneration invisible to prove rate, but occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.
5	Tautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
6	In our Qwen3-4B experiments, this \emph{observe-vs-optimize asymmetry} persists across logic types and dataset families: structural proxies for reasoning quality are easier to observe than to optimize.\footnote{Code and data: \url{[anonymized]}}
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2780 · 2026-05-22T23:22:22.855803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2781 · 2026-05-22T23:22:23.258663+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.
5	The root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
6	Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
7	
8	\paragraph{The evaluation gap.}
9	Neurosymbolic formalizers~\citep{logic-lm, linc, satlm} and RL-trained variants~\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.
11	Inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} detects gaming at inference time but offers no training-time diagnostic.
12	What is missing is an annotation-free method for testing \emph{component necessity} in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.
16	For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \emph{Intensional Structural Reward} (ISR).
17	A formalization where every component is necessary receives $\tex
…[truncated 2541 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2782 · 2026-05-22T23:22:23.259157+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2783 · 2026-05-22T23:22:23.611066+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}.
11	
12	\subsection{Solver Trace Ablation (STA)}
13	\label{sec:sta}
14	
15	STA tests whether each component of a proved formalization is individually necessary for proof success (Algorithm~\ref{alg:sta}).
16	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
17	A component is \emph{necessary} if its removal causes proof failure.
18	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
19	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
20	
21	\begin{algorithm}[t]
22	\caption{Solver Trace Ablation (STA)}
23	\label{alg:sta}
24	\begin{algorithmic}[1]
25	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
26	\ENSURE $\text{ISR}(x) \in [0, 1]$
27	\STATE $\textit{necessary} \gets 0$
28	\FOR{$i = 1$ to $n$}
29	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
30	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
31	    \ENDIF
32	\ENDFOR
33	\RETURN $\textit{necessary} \,/\, n$
34	\end{algorithmic}
35	\end{algor
…[truncated 5928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2784 · 2026-05-22T23:22:23.611479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2785 · 2026-05-22T23:22:23.662216+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:ta
…[truncated 16567 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2786 · 2026-05-22T23:22:30.530073+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2787 · 2026-05-22T23:22:30.630977+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.
11	In mathematical reasoning, learned process reward models~\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\citep{processbench}.
12	A recurring finding is that auxiliary rewards can hurt rather than help: \citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.
13	Annotation-free alternatives~\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.
14	\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.
15	
16	\paragraph{Reward hacking and Goodhart's Law.}
17	Goodhart's Law is established theoretically~\citep{manheim-goodha
…[truncated 3162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2788 · 2026-05-22T23:22:31.033190+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2789 · 2026-05-22T23:22:31.485322+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation; repurposed as reward, ISR produces a seed-dependent Goodhart effect, documenting that structural proxies for reasoning quality are easier to observe than to optimize (Appendix~\ref{app:practical-guidelines}).
5	STA is applicable in principle to any RL system whose output is verified by a deterministic checker---math reasoning with formal verifiers, code generation with test suites---wherever solver-verifiable structure can be ablated.
6	Our cross-scale results hint at a capacity-dependent pattern: structural degeneration may require model capacity sufficient for RL convergence but insufficient to resist structural shortcuts. The high non-convergence rate among exec-only seeds (two of five fail to converge; Appendix~\ref{app:seed-convergence}) further suggests degeneration requires successful convergence as a prerequisite.
7	As an aggregate metric, ISR is susceptible to premise-count confounds (\S\ref{sec:goodhart}); per-sample mode classification offers a more reliable diagnostic pathway for future work.
8	Combining STA with inference-time gaming detection~\citep{kim-game-formalization, helff2026gaming} could extend structural monitoring across the training--deployment spectrum.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2790 · 2026-05-22T23:22:31.485688+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2791 · 2026-05-22T23:22:31.987920+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\ref{app:8b-results},~\ref{app:llama-coldstart}), leaving cross-scale generalization untested.
5	Three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.
6	Structural degeneration results should be interpreted as conditional on successful convergence: two of five primary exec-only seeds fail to converge and retain high structural integrity (85--87\% genuine; Appendix~\ref{app:seed-convergence}), suggesting degeneration is a byproduct of reward optimization success rather than an inherent property of GRPO.
7	One of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\ref{app:detailed-results}).
8	ISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
9	All ISR conditions use a single multiplicative reward family ($r_{\text{exec}} \cdot (1+\beta\,\text{ISR})$); alternative formulations remain untested.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2792 · 2026-05-22T23:22:31.988332+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool call

_source line 2793 · 2026-05-22T23:22:32.390046+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 2794 · 2026-05-22T23:22:32.491835+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\small
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, conditions, a
…[truncated 55768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool result

_source line 2795 · 2026-05-22T23:22:32.492413+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in solver-backed RL systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	Code, evaluation scripts, the ProofFOL dataset, and trained model checkpoints will be released upon acceptance.
8	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2796 · 2026-05-22T23:23:00.054222+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool call

_source line 2797 · 2026-05-22T23:23:00.054655+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2798 · 2026-05-22T23:23:03.875055+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3820
}
```

</details>

---


### Tool result

_source line 2799 · 2026-05-22T23:23:03.875691+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3821
}
```

</details>

---


### Tool call

_source line 2800 · 2026-05-22T23:23:59.247841+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查方法严谨性、实验设计和统计分析。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (通过 ARR 统一审稿)\n- **截止日期**: 2026-05-25 (ARR May cycle)\n- **页数限制**: 正文 8 页（Long Paper），参考文献不限，Limitations/Ethics 不计入页数\n- **模板**: ACL 2026 (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- TeX 主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- 各章节在同目录下的 `.tex` 文件中\n\n## 论文概述\n本文提出 Solver Trace Ablation (STA)，一种 LOO-based 诊断方法用于检测 GRPO 训练的 neurosymbolic reasoning 系统中的结构退化。核心指标 ISR (Intensional Structural Reward) 测量形式化输出中每个组件的必要性。实验在 Qwen3-4B 上跨多种 reward 条件、逻辑类型和数据集进行。\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- STA/ISR 方法的形式化是否正确完备？LOO 假设有无遗漏的 edge case？\n- ISR 作为 Shapley value 特例的定位是否准确？\n- Hacking taxonomy 的分类方法（文本匹配 + 功能分析两阶段）是否可靠？\n- Premise-count confound 的处理是否充分？1.06× matched comparison 是否真正解决了问题？\n\n### 2. 实验设计\n- N=3 seeds 的统计效力评估：对于 multi-attractor dynamics，3 seeds 够不够？\n- Seed 43 使用 T=0.7 sampling 而非 greedy：这个异常如何影响结论？N=2 sensitivity analysis 是否足够？\n- CMH 统计中 within-seed samples 的独立性假设是否合理？论文的 caveat 是否充分？\n- 控制实验设计（Random control, Shuffled-ISR, SFT baseline）是否完备？有无遗漏的 confound？\n- ProofFOL 数据集（silver-standard, GPT-4o 翻译）的质量是否影响结论？p=0.10 不显著结果的处理是否恰当？\n\n### 3. 统计分析\n- χ² test (174.8, p<10⁻³⁸) 的假设检验是否正确？是否存在 multiple testing 问题？\n- Fisher exact tests 和 Bonferroni correction 的实施是否正确？\n- 5-seed vs 3-seed 结果的解释是否合理？bimodal seed-dependence 的处理？\n- 单模型 (Qwen3-4B) 实验能否支撑论文声称的通用性？8B 和 LLaMA 不收敛意味着什么？\n\n### 4. Cross-domain 证据\n- Prolog 实验的证据强度评估\n- ProofFOL cross-dataset 证据的说服力\n- Cross-scale (8B) 不收敛结果的解释是否过度\n\n请按 EMNLP ARR 评审标准，给出结构化审稿意见：Summary → Strengths → Weaknesses（区分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment (1-5 分 + 置信度)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查方法严谨性、实验设计和统计分析。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (通过 ARR 统一审稿)\n- **截止日期**: 2026-05-25 (ARR May cycle)\n- **页数限制**: 正文 8 页（Long Paper），参考文献不限，Limitations/Ethics 不计入页数\n- **模板**: ACL 2026 (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- TeX 主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- 各章节在同目录下的 `.tex` 文件中\n\n## 论文概述\n本文提出 Solver Trace Ablation (STA)，一种 LOO-based 诊断方法用于检测 GRPO 训练的 neurosymbolic reasoning 系统中的结构退化。核心指标 ISR (Intensional Structural Reward) 测量形式化输出中每个组件的必要性。实验在 Qwen3-4B 上跨多种 reward 条件、逻辑类型和数据集进行。\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- STA/ISR 方法的形式化是否正确完备？LOO 假设有无遗漏的 edge case？\n- ISR 作为 Shapley value 特例的定位是否准确？\n- Hacking taxonomy 的分类方法（文本匹配 + 功能分析两阶段）是否可靠？\n- Premise-count confound 的处理是否充分？1.06× matched comparison 是否真正解决了问题？\n\n### 2. 实验设计\n- N=3 seeds 的统计效力评估：对于 multi-attractor dynamics，3 seeds 够不够？\n- Seed 43 使用 T=0.7 sampling 而非 greedy：这个异常如何影响结论？N=2 sensitivity analysis 是否足够？\n- CMH 统计中 within-seed samples 的独立性假设是否合理？论文的 caveat 是否充分？\n- 控制实验设计（Random control, Shuffled-ISR, SFT baseline）是否完备？有无遗漏的 confound？\n- ProofFOL 数据集（silver-standard, GPT-4o 翻译）的质量是否影响结论？p=0.10 不显著结果的处理是否恰当？\n\n### 3. 统计分析\n- χ² test (174.8, p<10⁻³⁸) 的假设检验是否正确？是否存在 multiple testing 问题？\n- Fisher exact tests 和 Bonferroni correction 的实施是否正确？\n- 5-seed vs 3-seed 结果的解释是否合理？bimodal seed-dependence 的处理？\n- 单模型 (Qwen3-4B) 实验能否支撑论文声称的通用性？8B 和 LLaMA 不收敛意味着什么？\n\n### 4. Cross-domain 证据\n- Prolog 实验的证据强度评估\n- ProofFOL cross-dataset 证据的说服力\n- Cross-scale (8B) 不收敛结果的解释是否过度\n\n请按 EMNLP ARR 评审标准，给出结构化审稿意见：Summary → Strengths → Weaknesses（区分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment (1-5 分 + 置信度)"
  }
}
```

</details>

---


### Tool result

_source line 2801 · 2026-05-22T23:24:22.875936+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23628
}
```

</details>

---


### Tool call

_source line 2802 · 2026-05-22T23:24:23.078008+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查新颖性、完整性、Related Work 覆盖和写作质量。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (通过 ARR 统一审稿)\n- **截止日期**: 2026-05-25 (ARR May cycle)\n- **页数限制**: 正文 8 页（Long Paper），参考文献不限，Limitations/Ethics 不计入页数\n- **模板**: ACL 2026 (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- TeX 主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- 各章节在同目录下的 `.tex` 文件中\n\n## 论文概述\n本文提出 Solver Trace Ablation (STA) 诊断 GRPO 训练的 neurosymbolic reasoning 中的结构退化和 Goodhart 效应。声称三个贡献：(C1) STA 方法 + ISR + 8-mode taxonomy；(C2) Goodhart 效应实证；(C3) 跨逻辑/跨数据集证据。实验基于 Qwen3-4B + FOLIO/ProofFOL。\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- C1 的核心方法 LOO ablation 是标准的 mutation testing 技术——论文定位为 \"systematic application\" 而非方法创新，这种定位是否足够支撑一篇 long paper？\n- \"Observe-vs-optimize asymmetry\" 是否本质上就是 Goodhart's Law 的重述？论文如何区分？\n- 8-mode hacking taxonomy 的贡献定位——分类学本身是否有足够的洞见？\n- ISR 作为 Shapley value 的 restricted case，这种联系是否有实际意义还是仅为理论定位？\n\n### 2. 完整性评估\n- 单模型 (Qwen3-4B) + 单数据集族 (FOLIO/ProofFOL) 的实验范围是否足以支撑论文的 claims？\n- 8B 和 LLaMA 均不收敛——论文的发现是否可能仅是 Qwen3-4B + FOLIO 的 artifact？\n- ISR 与 NLI accuracy 不相关 (ρ=-0.049)——这对 ISR 的实际诊断价值意味着什么？\n- SFT baseline PR=13% vs exec-only PR=93%——这种不匹配的比较是否公平？\n\n### 3. Related Work 覆盖\n- 检查是否有遗漏的重要相关工作，特别是：\n  - 2025-2026 年 RLVR/reward hacking 领域的最新工作\n  - Neurosymbolic reasoning 领域的最新进展\n  - Process reward models 和 reward shaping 的最新文献\n  - 与 STA 类似的诊断方法（LOO-based, perturbation-based）\n- 请用 web_search 搜索可能遗漏的重要引用\n\n### 4. 写作质量与格式\n- 标题长度（~140 chars）是否需要精简？\n- Abstract 的信息密度和 claim 强度是否恰当？\n- 论文叙事结构是否清晰？Introduction 的 contribution statement 是否 well-scoped？\n- 主文正文是否在 8 页限制内？\n- Limitations 章节是否充分覆盖关键问题？\n- Ethics statement 是否恰当？\n- 匿名性检查：是否有违反 double-blind 的信息泄露？\n- 图表质量和 caption 信息量\n\n### 5. Framing 一致性\n- Title 中 \"Case Study\" vs 论文声称的跨域证据——是否矛盾？\n- C1 \"model-agnostic diagnostic method\" vs 只在 Qwen3-4B 上测试——framing 是否过度？\n- \"structural proxies for reasoning quality are easier to observe than to optimize\"——这个 claim 的证据链是否完整？\n\n请按 EMNLP ARR 评审标准，给出结构化审稿意见：Summary → Strengths → Weaknesses（区分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment (1-5 分 + 置信度)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查新颖性、完整性、Related Work 覆盖和写作质量。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (通过 ARR 统一审稿)\n- **截止日期**: 2026-05-25 (ARR May cycle)\n- **页数限制**: 正文 8 页（Long Paper），参考文献不限，Limitations/Ethics 不计入页数\n- **模板**: ACL 2026 (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- TeX 主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- 各章节在同目录下的 `.tex` 文件中\n\n## 论文概述\n本文提出 Solver Trace Ablation (STA) 诊断 GRPO 训练的 neurosymbolic reasoning 中的结构退化和 Goodhart 效应。声称三个贡献：(C1) STA 方法 + ISR + 8-mode taxonomy；(C2) Goodhart 效应实证；(C3) 跨逻辑/跨数据集证据。实验基于 Qwen3-4B + FOLIO/ProofFOL。\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- C1 的核心方法 LOO ablation 是标准的 mutation testing 技术——论文定位为 \"systematic application\" 而非方法创新，这种定位是否足够支撑一篇 long paper？\n- \"Observe-vs-optimize asymmetry\" 是否本质上就是 Goodhart's Law 的重述？论文如何区分？\n- 8-mode hacking taxonomy 的贡献定位——分类学本身是否有足够的洞见？\n- ISR 作为 Shapley value 的 restricted case，这种联系是否有实际意义还是仅为理论定位？\n\n### 2. 完整性评估\n- 单模型 (Qwen3-4B) + 单数据集族 (FOLIO/ProofFOL) 的实验范围是否足以支撑论文的 claims？\n- 8B 和 LLaMA 均不收敛——论文的发现是否可能仅是 Qwen3-4B + FOLIO 的 artifact？\n- ISR 与 NLI accuracy 不相关 (ρ=-0.049)——这对 ISR 的实际诊断价值意味着什么？\n- SFT baseline PR=13% vs exec-only PR=93%——这种不匹配的比较是否公平？\n\n### 3. Related Work 覆盖\n- 检查是否有遗漏的重要相关工作，特别是：\n  - 2025-2026 年 RLVR/reward hacking 领域的最新工作\n  - Neurosymbolic reasoning 领域的最新进展\n  - Process reward models 和 reward shaping 的最新文献\n  - 与 STA 类似的诊断方法（LOO-based, perturbation-based）\n- 请用 web_search 搜索可能遗漏的重要引用\n\n### 4. 写作质量与格式\n- 标题长度（~140 chars）是否需要精简？\n- Abstract 的信息密度和 claim 强度是否恰当？\n- 论文叙事结构是否清晰？Introduction 的 contribution statement 是否 well-scoped？\n- 主文正文是否在 8 页限制内？\n- Limitations 章节是否充分覆盖关键问题？\n- Ethics statement 是否恰当？\n- 匿名性检查：是否有违反 double-blind 的信息泄露？\n- 图表质量和 caption 信息量\n\n### 5. Framing 一致性\n- Title 中 \"Case Study\" vs 论文声称的跨域证据——是否矛盾？\n- C1 \"model-agnostic diagnostic method\" vs 只在 Qwen3-4B 上测试——framing 是否过度？\n- \"structural proxies for reasoning quality are easier to observe than to optimize\"——这个 claim 的证据链是否完整？\n\n请按 EMNLP ARR 评审标准，给出结构化审稿意见：Summary → Strengths → Weaknesses（区分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment (1-5 分 + 置信度)"
  }
}
```

</details>

---


### Tool result

_source line 2803 · 2026-05-22T23:24:24.486668+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1408
}
```

</details>

---


### Assistant

_source line 2804 · 2026-05-22T23:24:33.500852+00:00_

**Round 1 初审已启动**

| 角色 | 审查侧重 | 状态 |
|------|----------|------|
| Reviewer 1 | 方法严谨性 + 实验设计 + 统计分析 | 🔄 审稿中 |
| Reviewer 2 | 新颖性 + 完整性 + Related Work + 写作质量 | 🔄 审稿中 |
| 视觉审查 Agent | PDF 排版质量 | 🔄 进行中 |
| 外部审稿 | — | 未配置 |

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 253

## Round 253

2 recorded events


### User

_source line 2805 · 2026-05-22T23:29:56.746635+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见

### Paper Summary

本文提出 Solver Trace Ablation (STA)，一种基于 Leave-One-Out (LOO) 的诊断方法，用于检测 GRPO 训练的 neurosymbolic reasoning 系统中的结构退化。核心指标 ISR（Intensional Structural Reward）衡量形式化输出中每个组件的必要性比例。论文在 Qwen3-4B 上跨 6 种 reward 条件（exec-only, ISR β=0.1, Random β=0.1, SFT, Shuffled-ISR, ISR β=0.3）、两种逻辑类型（FOL/Prolog）和两个数据集（FOLIO/ProofFOL）进行了实验，构建了 8 类 hacking 分类体系，并实证展示了 ISR 作为 reward 信号时的 Goodhart 效应（ISR 从 0.64 崩溃至 0.003）。

---

## 总体评分

**Overall**: 3.0 / 5 (Findings)
**一句话总结**: STA 诊断工具和 hacking 分类体系有真正的方法论贡献，但单模型（Qwen3-4B）+ 低种子数（N=3，其中一个异常）的实验设计显著削弱了统计结论的可靠性，cross-dataset 证据未达显著性，整体证据链不足以支撑 conference-level 的通用性声称。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0 / 5 | 方法论设计合理，但 N=3 seeds（1个异常）+ within-seed 独立性假设可疑 + premise-count confound 未解决（McNemar p=0.317）显著削弱统计基础 |
| Excitement | 3.5 / 5 | 问题重要且时机恰当；STA 工具简洁实用；8-mode taxonomy 是有价值的贡献；Goodhart 效应观察清晰。但单模型限制了 impact |
| Reproducibility | 4 / 5 | 超参数详尽（Appendix A Table 3），使用公开模型/数据集，承诺开源。Seed 43 的 T=0.7 是已知差异 |
| Confidence | 4 / 5 | 仔细阅读全文含全部附录，熟悉 RLVR、neurosymbolic reasoning 和 reward hacking 领域 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 单模型实验无法支撑通用性声称
- 具体位置：Title、Abstract（"GRPO-Trained Neurosymbolic Reasoning"）、Section 1 Contributions C1（"a model-agnostic diagnostic method"）、Section 5 Conclusion（"applicable in principle to any RL system"）
- 问题：论文成功运行的唯一模型是 Qwen3-4B。Qwen3-8B 在两种配置下均未收敛（Appendix E.7, Table 14），LLaMA-3.2-3B 在 FOL 生成能力上完全失败（Appendix E.4）。标题和摘要使用泛化表述（"GRPO-Trained Neurosymbolic Reasoning"），而非限定于"Qwen3-4B"。虽然 C1 声称的 model-agnostic 是指方法设计而非实验验证，但读者会合理期待至少在两个不同架构上看到实证。
- 为什么影响接收：Reviewer 和 AC 会质疑：如果方法只在一个模型上验证，如何确信观察到的 structural degeneration 是 GRPO 的普遍特性，而非 Qwen3-4B 的特殊行为？cross-scale 和 cross-architecture 的全面失败反而暗示了后者的可能性。
- 建议修改方向：(1) 将标题/摘要的 scope 严格限定为 Qwen3-4B case study；(2) 或增加至少一个成功收敛的替代架构（如 Mistral-7B、Gemma-2-2B）的实验数据。

**N2** [critical] N=3 seeds 的统计效力严重不足，尤其面对 bimodal dynamics
- 具体位置：Section 4.1（3-seed 设计）、Section 4.3（bimodal seed-dependence）、Table 13（N=2 sensitivity）
- 问题：论文发现 exec-only 条件下存在 bimodal convergence（3/5 seeds 收敛，2/5 不收敛），这恰恰是最需要更多 seeds 来表征分布的场景。主实验只用 3 seeds，随后补充的 seeds 45-46 仅用于探查 bimodal 模式，而非复制核心 ISR 发现。N=2 sensitivity analysis（排除 seed 43）在统计上几乎没有意义——无法对 2 个数据点做有意义的推断。Limitations Section 6 承认"three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance"，但正文的统计检验（χ²、CMH、Fisher）仍然建立在这一不充分的基础上。
- 为什么影响接收：Multi-attractor dynamics 的刻画需要足够的样本来估计 attractor basin 的大小和转换概率。3 seeds 只能说明现象存在，无法量化其普遍性。正文中的 confidence intervals 和 p-values 在此 N 下可能有误导性。
- 建议修改方向：(1) 将 seed 数增至 8-10 per condition，至少对 exec-only 和 ISR β=0.1 两个核心条件执行；(2) 或将所有基于 seed-level 变异性的声称降级为 "preliminary observation"，不做定量统计推断。

**N3** [critical] CMH 检验的 within-seed 独立性假设不成立
- 具体位置：Section 5 Statistical Considerations、Appendix C Table 6
- 问题：CMH 检验将 seed 作为 stratum，但 stratum 内的 samples（同一 GRPO checkpoint 生成的多个 formalization）共享模型权重，不是独立观测。这违反了 CMH 的基本假设。论文添加了 caveat（"CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is N=3"），但仍然报告了 CMH p-values 并基于它们做推断。如果 within-seed correlation ρ>0（几乎必然如此），实际有效样本量远小于报告的 n=231，所有 p-values 都被严重膨胀。
- 为什么影响接收：这不仅是一个 caveat 问题，而是整个统计推断框架的有效性问题。读者看到 p<10^-38 会获得虚假的确定性感。
- 建议修改方向：(1) 使用 cluster-robust standard errors 或 GEE（Generalized Estimating Equations）以 seed 为 cluster 来正确处理组内相关；(2) 或至少报告 seed-level aggregate statistics（每个 seed 一个数据点，N=3 或 N=5）的 permutation test 或 bootstrap CI。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Seed 43 的 T=0.7 采样异常破坏了实验一致性
- 具体位置：Section 4.1 脚注 5、Appendix A Table 3、Appendix E.6 Table 13
- 问题：Seed 43 使用 T=0.7 sampling 而非 greedy decoding。这意味着 seed 43 的评估分布与 seeds 42/44 系统性不同——不仅是随机变异，而是评估协议的改变。论文将其标注为"not strictly comparable"但仍然纳入所有主表分析。为何不用 greedy decoding 重新评估 seed 43？这在计算上应该是低成本的（只需要重新运行 inference，不需要重新训练）。
- 建议：用 greedy decoding 重新评估 seed 43 的 checkpoint，或在主表中明确标记 seed 43 的数据为参考值而非正式结果。

**W2** [warning] Premise-count confound 未能统计解决
- 具体位置：Section 4.2（第 6 页底部）、Appendix C Table 5、Table 9
- 问题：论文承认"formalizations with fewer components mechanistically receive higher ISR"（Section 3.2）。premise-count-matched comparison 显示 scalar ISR advantage 不显著（McNemar p=0.317, Table 9）。这意味着论文**无法将 ISR 差异从 premise-count 效应中分离**。论文说"confirming that the scalar ISR advantage is not statistically significant"并转向"mode composition analysis (CE) is unaffected"。但 ISR 作为核心指标的标量值如果受 premise-count 混淆，整个诊断的定量维度就被削弱了。
- 建议：(1) 对 ISR 做 premise-count normalization（如 ISR_adjusted = ISR / expected_ISR_given_n_premises）；(2) 或明确将 ISR 降级为二分类指标（hacking/non-hacking），不解读其标量值。

**W3** [warning] ProofFOL cross-dataset 证据不显著（p=0.10）
- 具体位置：Section 4.4（第 7 页）、Table 11
- 问题：ProofFOL 作为 cross-dataset 证据的关键实验，其 genuine-rate permutation test p=0.10 不显著。论文称之为"exploratory, underpowered, directional"。但在只有两个数据集的情况下，唯一的 cross-dataset 实验不显著，严重削弱了 C3 contribution（"cross-benchmark evidence characterizing the structural manifestation of Goodhart's law"）的说服力。此外，ProofFOL 本身是 GPT-4o 翻译的 silver-standard 数据（只有 59.1% 通过率），数据质量存疑。
- 建议：(1) 降低 C3 的声称强度，将 ProofFOL 明确定位为 pilot experiment；(2) 讨论 silver-standard 数据质量对结论的具体影响路径。

**W4** [warning] ISR 作为 Shapley value 特例的定位需要更精确
- 具体位置：Section 3.2（第 4 页）
- 问题：论文称 ISR 是"Shapley value restricted to the (n-1)-coalition"，将复杂度从 O(2^n) 降至 O(n)。但 Shapley value 的核心价值在于考虑**所有联盟大小**的边际贡献，(n-1)-coalition restriction 本质上是 LOO，丢失了组件间的交互效应。例如：如果 premise A 和 B 可互相替代（单独移除任一个都不破坏证明），LOO 会将两者都标记为"不必要"，但证明确实使用了结构化推理。论文用 "binary solver output makes LOO sufficient" 来辩护，但这只对"individually necessary"成立，不覆盖"jointly redundant but individually useful"的情况。
- 建议：明确讨论 LOO 相对于 full Shapley 的局限（misses complementary effects），并量化这种 edge case 在实际数据中的频率。

**W5** [warning] Hacking taxonomy 的分类器召回率未报告
- 具体位置：Section 5（第 5 页）、Appendix D（第 15 页）
- 问题：Text-match classifier 的 precision 通过 50 例人工验证估计为 >95%，但 recall 被承认"inherently bounded by the text-match threshold"且未量化。这意味着 hacking 的实际普遍性可能被低估——有多少 hacking instances 逃过了 text-match 分类器？functional analysis（per-sample n_taxonomy 分析）作为第二阶段，覆盖了什么样的 false negatives？
- 建议：(1) 报告 recall 的下限估计（如：在 random sample 中，有多少 functional hacking 被 text-match 漏检？）；(2) 或提供 text-match 与 functional-analysis 的一致性分析。

---

## 小问题（不影响接收）

- Section 3.2 的 ISR 公式（Eq. 1）中 S(x) 和 f_s 的定义可以更早引入，当前首次出现时缺乏上下文。
- Figure 1 的 legend 中 "ISR β=0.1 (s44)" 等标注方式不直观——读者需要查 Appendix 才能知道 s44 是 seed 44。
- Table 1 脚注中 "†Seed 42 only" 和 "‡" 标记密集，建议简化。
- Appendix D 的 hacking mode 定义使用了 Prolog 示例（如 D.9 Query-as-fact gaming），但主文 Section 4 的分析主要在 FOL 上，跨语言对应关系可以更清晰。
- Section 2 Related Work 的最后一段（Reward hacking and Goodhart's Law）引用密度很高但缺少对各引用具体贡献的区分——可以适当精简。

---

## Questions for Authors

1. **Seed 43 重新评估**：为何不用 greedy decoding 重新评估 seed 43 的已保存 checkpoint？这在计算上应该是低成本的，可以消除 T=0.7 的混淆。

2. **Effective sample size**：是否可以报告 within-seed ICC (intraclass correlation coefficient) 来量化组内相关性？这会让读者判断 CMH p-values 的真实可靠度。

3. **ISR 与 NLI accuracy 的相关性**：Appendix C 提到 ISR "does not correlate with NLI accuracy"。但 ISR 的设计目标是衡量 structural quality，如果它与 downstream task performance 无关，那它作为诊断工具的实际价值是什么？请阐明 ISR 的 intended use case——它应该在什么场景下被使用，它的 actionable insight 是什么？

4. **Multiplicative vs. additive reward**：论文使用 r_exec × (1+β×ISR) 的乘法形式。是否测试过加法形式（r_exec + β×ISR）？乘法形式中只有 proved samples 获得 ISR bonus，这可能导致 reward landscape 的特殊结构。

5. **8 种 hacking modes 的相互排斥性**：Table 7 将每个 sample 分配到一个 mode。但 Appendix D.1-D.9 的定义中，某些 modes 似乎可以共存（如 premise-subset gaming + conclusion embedding）。分类是否强制互斥？如果一个 sample 符合多个 modes，如何处理？

---

## Missing References

- Lanham et al., 2023 "Measuring Faithfulness in Chain-of-Thought Reasoning" — 与 STA 的 component necessity testing 理念高度相关，但论文未讨论 CoT faithfulness 与 solver trace 结构完整性的联系。
- Turpin et al., 2023 "Language Models Don't Always Say What They Think" — 关于 model output 与 internal reasoning 的 disconnect，与 ISR 的 observe-vs-optimize asymmetry 直接相关。

---

## 主要优势

1. **问题定位精准**：识别了 GRPO 训练 neurosymbolic reasoning 中 execution-based evaluation 的盲点——结构退化在 prove rate 不变甚至上升时发生。这是一个真实且重要的问题（Section 1, Figure 1）。

2. **方法简洁且无需训练**：STA 只需要对 solver input 做逐一消融，不涉及模型内部、不需要额外训练、不依赖人工标注，计算成本 O(n) per sample。这使其容易被其他研究者采用。

3. **Hacking taxonomy 的系统性**：8 种 degeneration mode 的分类（Appendix D）附有 FOL/Prolog 示例和 ISR interaction 分析，是该领域首个系统性的分类尝试。Table 7-8 的 per-mode 统计和分类器精度验证增加了可信度。

4. **控制实验设计合理**：Random control（β=0.1, uniform random ISR）、Shuffled-ISR（打乱 ISR 赋值）和 SFT baseline 三个控制条件有效分离了 reward signal 的因果效应。特别是 Shuffled-ISR 控制表明 ISR 的 degeneration 不是任意 auxiliary reward 的 artifact。

5. **透明度高**：论文对自身局限的坦诚（seed 43 异常、N=3 不足、within-seed independence caveat、ProofFOL p=0.10、单模型限制）在该领域论文中罕见，有利于后续研究的准确定位。

---

**Final Scores Summary**:
- Soundness: 3.0/5
- Excitement: 3.5/5  
- Overall Assessment: 3.0/5 (Findings)
- Confidence: 4/5
- Reproducibility: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2806 · 2026-05-22T23:30:07.208234+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 254

## Round 254

2 recorded events


### User

_source line 2807 · 2026-05-22T23:30:16.519373+00:00_

[Reviewer 1 审稿结果]:
审稿完成。核心结论：

**Overall 3.0/5 (Findings)**。STA 诊断工具和 8-mode hacking taxonomy 是有价值的方法论贡献，但三个 critical 问题制约了 conference-level 接收：

1. **单模型**——仅 Qwen3-4B 成功，8B 和 LLaMA 均未收敛，无法支撑泛化声称
2. **N=3 seeds 不足**——面对 bimodal dynamics 尤为严重，N=2 sensitivity analysis 无统计意义
3. **CMH 统计的独立性假设不成立**——within-seed samples 共享权重，p-values 被膨胀，需要 cluster-robust 方法

次要问题包括 premise-count confound 未统计解决（McNemar p=0.317）、ProofFOL cross-dataset 证据不显著（p=0.10）、seed 43 的 T=0.7 评估协议异常。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2808 · 2026-05-22T23:30:21.592851+00:00_

Reviewer 1 完成。等待 Reviewer 2 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 255

## Round 255

6 recorded events


### User

_source line 2809 · 2026-05-22T23:31:00.539094+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1 (Fresh Review)

**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study

---

## 总体评分

**Overall**: 3.0 / 5 (Findings 级别)
**一句话总结**: 有价值的实证发现（GRPO 训练中的结构退化和 Goodhart 模式转移），但方法新颖性有限（标准 LOO 应用于新场景），且单模型+单数据集族的实验范围不足以支撑论文声称的通用性。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 实验设计有适当 controls（random reward, shuffled-ISR, SFT baseline），但核心量化 claim（214× ISR collapse）在控制 premise count 后缩减至 1.06×（p=0.317），统计上不显著；N=3 seeds 且 2/5 额外 seeds 表现截然不同 |
| Excitement | 3.0/5 | 结构退化的模式转移发现（CE→TS）有实际价值，8-mode taxonomy 有用；但 LOO 方法本身无创新，observe-vs-optimize 本质是 Goodhart's Law 的重述 |
| Reproducibility | 4.0/5 | Algorithm 1 清晰，超参数完整（Appendix A），承诺代码和数据发布；seed 43 使用不同 sampling 略有瑕疵 |
| Confidence | 4/5 | 熟悉 RLVR、reward hacking、neurosymbolic reasoning 领域；仔细阅读了全文和附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 单模型泛化性严重不足，削弱核心 claims 的通用性
- 具体位置：Section 4 全文；Limitations Section 6 第1句
- 问题：所有收敛实验仅在 Qwen3-4B 上完成。Qwen3-8B（Appendix E.7）和 LLaMA-3.2-3B（Appendix E.5）均未收敛。论文将此解读为"收敛是退化前提条件"，但同样合理的解读是：**结构退化可能是 Qwen3-4B 特定的 artifact**，而非 GRPO 训练的通用现象。如果只有一个模型展现该现象，无法区分这两种假设。
- 为什么影响接收：C1 声称 "model-agnostic diagnostic method"，但只有单模型实证；C3 声称 "cross-domain evidence"，但 cross-domain 仅限于 logic type 和 dataset，不包括 model。对于声称通用性的论文，这是根本性缺陷。
- 建议修改方向：(1) 将 C1 的 "model-agnostic" 改为 "model-independent in design"，明确区分方法定义与实证验证范围；(2) 在 Conclusion 中将 "applicable in principle to any RL system" 降级为 future work hypothesis；(3) 若有条件，补充至少一个其他收敛模型的实验（即使是更小规模的）。

**N2** [critical] ISR 的诊断价值自我矛盾：与推理质量零相关（ρ=−0.049）却被定位为 "structural proxy for reasoning quality"
- 具体位置：Abstract 第3句 ("ISR reveals structural degeneration invisible to prove rate")；Section 3.2 Limitations of ISR；Appendix C
- 问题：Abstract 和 Introduction 反复将 ISR 定位为衡量推理结构质量的指标。然而 ISR 与 NLI accuracy 的 Spearman 相关系数仅为 ρ=−0.049（p=0.187, Appendix C）。如果 ISR 不能区分语义正确的推理和语义错误但结构"正确"的推理，它作为"诊断工具"的实际意义何在？论文在 Section 3.2 承认了这一点（"ISR captures component necessity, not semantic faithfulness"），但 Abstract 和 Introduction 的叙事仍暗示 ISR 是推理质量的代理。
- 为什么影响接收：这是论文最核心的 framing 矛盾。如果 ISR 仅衡量组件冗余度（而非推理质量），那么"结构退化"这个术语就有误导性——它应该叫"组件冗余化"而非暗示推理能力退化。
- 建议修改方向：(1) 在 Abstract 中明确 ISR 衡量的是 component redundancy，不是 reasoning quality；(2) 用 "component redundancy collapse" 替代或补充 "structural degeneration"，避免暗示推理能力下降；(3) 在 Introduction 中加一段讨论 ISR 与下游推理质量的关系（或缺乏关系）。

**N3** [critical] 核心量化 claim 被 premise-count confound 几乎完全解释
- 具体位置：Section 4.3 "Premise-count confound"；Table 1
- 问题：论文的核心视觉叙事（Figure 1 的 ISR 崩塌曲线）展示了 214× 的 ISR collapse。但 Section 4.3 坦承控制 premise count 后差异缩减至 1.06×（McNemar p=0.317），统计上不显著。这意味着 **ISR 作为标量指标的诊断价值几乎为零**——它测到的主要是 "模型生成更短的 formalization" 而非 "模型结构退化"。论文转而依赖 compositional mode shift（CE→TS）作为主要证据，但这个证据链在 Table 1 caption 中埋得太深。
- 为什么影响接收：如果标量 ISR 的诊断信号几乎完全是 artifact，论文的方法论贡献（ISR 这个指标本身）就大幅缩水。真正有诊断价值的是 hacking mode classification，不是 ISR 数值。
- 建议修改方向：(1) 在 Abstract/Introduction 中降低对 ISR 标量的强调，前置 mode-level analysis 作为主要贡献；(2) Figure 1 应加注或在正文中更早说明 premise-count confound 的幅度；(3) 考虑用 premise-count normalized ISR 重绘 Figure 1。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 标题过长（~140字符），且 "Case Study" 与 "cross-domain evidence" 存在张力
- 具体位置：Title
- 问题：标题约 140 字符，远超 EMNLP 论文典型长度（60-80字符）。更重要的是，标题中的 "Case Study" 定位与论文 C3 声称的 "cross-domain evidence" 存在叙事矛盾。如果是 case study，读者期望单一设置的深入分析；如果声称 cross-domain 通用性，case study 的定位就过于保守。
- 建议：精简至 ~80 字符，例如 "Solver Trace Ablation Reveals Structural Degeneration in GRPO-Trained Reasoning"。移除 "Case Study" 或将 C3 的 cross-domain claim 降级。

**W2** [warning] SFT baseline 比较不公平：PR=13% vs PR=93%
- 具体位置：Table 1 SFT row；Section 4.2 "SFT baseline" 段
- 问题：SFT 在 PR=13% 下展示 92% non-hacking，而 exec-only 在 PR=93% 下展示 8% non-hacking。论文将此解读为 "hacking modes are absent before RL optimization"。但这个比较混淆了两个变量：(1) RL vs SFT 优化方式；(2) prove rate 水平。一个 PR=13% 的模型几乎不能证明任何东西——它当然没有 hacking，因为它几乎没有 "成功" 的样本可以 hack。100-step 比较（PR=32% vs SFT 8%）稍好但仍有差距。
- 建议：更明确地讨论 PR-matched 比较的困难，避免从这个不对等比较中得出过强结论。

**W3** [warning] N=3 seeds 的统计推断力度过弱，bimodal 5-seed 结果进一步削弱
- 具体位置：Section 4.1 "Statistical considerations"；Section 4.3 "Bimodal seed-dependence"
- 问题：核心实验用 N=3 seeds，论文承认 "80% power only for very large effects (d≥3.0)"。更关键的是，扩展到 5 seeds 后出现 bimodal 行为（3/5 gaming vs 2/5 genuine），使得 3-seed pooled 统计基本不可信。CMH p-values 在 N=3 strata 下本身就缺乏推断效力。论文对此有良好的自我意识（Section 4.1），但仍在正文中引用 CMH 结果。
- 建议：将 CMH 统计完全移至 Appendix 作为补充，主文聚焦 per-seed qualitative analysis。

**W4** [warning] Observe-vs-optimize asymmetry 缺乏超越 Goodhart's Law 的概念新颖性
- 具体位置：Abstract 最后一句；Introduction "observe-vs-optimize asymmetry" 段
- 问题：论文将 "structural proxies for reasoning quality are easier to observe than to optimize" 作为核心发现之一。但这本质上是 Goodhart's Law（"When a measure becomes a target, it ceases to be a good measure"）在特定场景的重述。论文确实引用了 Manheim & Garrabrant (2019) 等，但未清楚阐释 observe-vs-optimize 相对于已有 Goodhart 框架的增量贡献是什么——是具体 domain（neurosymbolic reasoning）中的新实例化？还是存在超越 Goodhart 的新机制？
- 建议：在 Introduction 中明确说明本文的 Goodhart 实例化的独特之处（如果有的话），或将其定位为 "empirical instantiation of Goodhart's Law in neurosymbolic RLVR" 而非暗示概念层面的新贡献。

**W5** [warning] 主文正文可能超出 8 页限制
- 具体位置：Section 5 (Discussion and Conclusion) 开始于 page 8 底部，延伸至 page 9 顶部
- 问题：从 PDF 排版看，Section 5 (Discussion and Conclusion) 从 page 8 底部开始，有约 8-10 行文本溢出到 page 9，之后才是 Section 6 (Limitations)。EMNLP 2026 对 Long Paper 有严格的 8 页主文限制。
- 建议：压缩 Section 5 或将部分内容移至 Limitations section，确保主文严格在 8 页内。

---

## 小问题（不影响接收）

1. **Table 1 caption 过长**（约 120 words）：大量 markers 和注释使 caption 难以快速理解。考虑将 footnote markers 的解释移至正文或 appendix。
2. **Footnote 1** (page 1): "Code and data: [anonymized]" 格式正确，匿名性保持良好。
3. **Figure 1 caption**: "rolling w=20" 的含义对非专家读者不够直观，建议在首次使用时简短解释。
4. **"Intensional" vs "intentional" footnote** (Section 3.2): 这个区分有用但可以更简洁。
5. **Appendix 体量庞大**（15+ pages）：附录提供了大量有用细节，但部分内容（如 per-seed detailed tables）可以进一步压缩。

---

## 主要优势

1. **实验设计中的 controls 值得肯定**：random reward、shuffled-ISR、SFT baseline 构成了一组合理的对照实验，特别是 shuffled-ISR（打破 sample-level 语义同时保留 ISR 分布）是一个巧妙的去混淆设计。
2. **学术诚实度极高**：论文对自身缺陷的讨论（premise-count confound, ISR-NLI decorrelation, seed bimodality）异常坦诚，这在投稿论文中少见。多处主动降级自己的 claims。
3. **8-mode hacking taxonomy 有实用价值**：CE, TS, PG 等分类有清晰的操作定义，附录提供了验证精度（152-sample audit），这对其他研究者诊断自己系统中的 reward hacking 有参考意义。
4. **Compositional mode shift 是最有说服力的发现**：控制 premise count 后标量 ISR 差异消失，但 CE→TS 的模式转移在所有 controls 下保持一致——这是对 Goodhart 效应最干净的实证证据。
5. **Related work 覆盖全面且时效性强**：涵盖了 2026 年初的最新 concurrent work（Helff et al., Khalifa et al., Nishimura et al., Wilhelm et al.），且每篇都有清楚的定位对比。

---

## Missing References / Related Work 审查

论文的 Related Work 已相当全面。以下两篇可能值得提及（但非必须）：

1. **MO-GRPO** (Arxiv 2509.22047): 直接研究 GRPO 在多目标问题中的 reward hacking 并提出 normalization-based mitigation，与本文的 GRPO reward hacking 分析互补。
2. **"Reward Hacking as Equilibrium under Finite Evaluation"** (Arxiv 2603.28063): 从理论角度证明 reward hacking 是结构性均衡而非可纠正的 bug，这对本文 "observe-vs-optimize asymmetry" 的理论解释有潜在价值。

---

## Questions for Authors

Q1: ISR 与 NLI accuracy 的零相关（ρ=−0.049）是否意味着在实际部署场景中，ISR 无法区分"正确但结构冗余"的推理和"错误但结构紧凑"的推理？如果是，ISR 相对于简单的 component-count 统计的增量诊断价值是什么？

Q2: 5-seed 扩展中 2/5 seeds 展示 ~55% non-hacking，与 3-seed 的 ~6% 截然不同。如果扩展到 10 或 20 seeds，你预期 bimodal 分布是否会稳定？这对论文结论"GRPO 导致结构退化"的泛化性意味什么？

Q3: Qwen3-8B 不收敛是否可能是超参数问题（K=8 vs K=4），而非模型能力问题？是否尝试过与 4B 完全相同的超参数？

Q4: 论文声称 STA "applicable in principle to any RL system whose output is verified by a deterministic checker"（Section 5）——但数学推理中的 formal verification（如 Lean 4）是否满足 LOO 的可行性条件？在定理证明中移除一个步骤通常不会产生有意义的 ablation，因为证明是链式依赖而非独立前提。

---

## 总评

本文记录了 GRPO 训练中 neurosymbolic reasoning 的一个有趣现象（结构退化和 Goodhart 模式转移），实验控制合理，学术态度坦诚。但方法新颖性有限（标准 LOO 的应用），核心量化指标（ISR scalar）被 premise-count confound 几乎完全解释，且单模型的实验范围严重制约了通用性 claims。论文最有价值的贡献是 compositional mode-shift 的实证和 8-mode taxonomy，这些属于 Findings 级别的贡献。建议以 Findings 接收为目标修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2810 · 2026-05-22T23:31:33.757318+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n### Must-Fix 问题\n\n**N1** [critical] 单模型实验无法支撑通用性声称\n- Title、Abstract（\"GRPO-Trained Neurosymbolic Reasoning\"）、C1（\"a model-agnostic diagnostic method\"）、Section 5（\"applicable in principle to any RL system\"）\n- 唯一成功运行的模型是 Qwen3-4B。8B 两种配置未收敛，LLaMA-3.2-3B FOL 生成完全失败。\n- 建议：将 scope 严格限定为 Qwen3-4B case study，或增加替代架构实验。\n\n**N2** [critical] N=3 seeds 的统计效力严重不足，尤其面对 bimodal dynamics\n- 3/5 seeds 收敛、2/5 不收敛的 bimodal 模式恰恰需要更多 seeds 来表征分布\n- N=2 sensitivity analysis 无统计意义\n- 建议：seed 数增至 8-10 per condition，或将所有 seed-level 声称降级为 preliminary observation\n\n**N3** [critical] CMH 检验的 within-seed 独立性假设不成立\n- within-seed samples 共享模型权重，不是独立观测\n- 实际有效样本量远小于报告的 n=231，所有 p-values 被严重膨胀\n- 建议：使用 cluster-robust SE 或 GEE 以 seed 为 cluster，或报告 seed-level permutation test\n\n### Should-Fix 问题\n\n**W1** Seed 43 的 T=0.7 采样异常破坏实验一致性——为何不用 greedy 重新评估？\n\n**W2** Premise-count confound 未统计解决——McNemar p=0.317 意味着无法分离 ISR 差异与 premise-count 效应\n\n**W3** ProofFOL cross-dataset 证据不显著（p=0.10）——唯一 cross-dataset 实验不显著，削弱 C3\n\n**W4** ISR 作为 Shapley value 特例的定位需要更精确——LOO 丢失了组件间交互效应\n\n**W5** Hacking taxonomy 的分类器召回率未报告——实际 hacking 普遍性可能被低估\n\n### 主要优势\n1. 问题定位精准（execution-based evaluation 的盲点）\n2. 方法简洁无需训练\n3. 8-mode taxonomy 系统性强\n4. Controls 设计合理（Random, Shuffled-ISR, SFT）\n5. 透明度高，对局限性坦诚\n\n### 评分\n- Soundness: 3.0/5\n- Excitement: 3.5/5\n- Overall: 3.0/5 (Findings)\n\n---\n\n请逐条回应以上每个 Must-Fix 和 Should-Fix 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n### Must-Fix 问题\n\n**N1** [critical] 单模型实验无法支撑通用性声称\n- Title、Abstract（\"GRPO-Trained Neurosymbolic Reasoning\"）、C1（\"a model-agnostic diagnostic method\"）、Section 5（\"applicable in principle to any RL system\"）\n- 唯一成功运行的模型是 Qwen3-4B。8B 两种配置未收敛，LLaMA-3.2-3B FOL 生成完全失败。\n- 建议：将 scope 严格限定为 Qwen3-4B case study，或增加替代架构实验。\n\n**N2** [critical] N=3 seeds 的统计效力严重不足，尤其面对 bimodal dynamics\n- 3/5 seeds 收敛、2/5 不收敛的 bimodal 模式恰恰需要更多 seeds 来表征分布\n- N=2 sensitivity analysis 无统计意义\n- 建议：seed 数增至 8-10 per condition，或将所有 seed-level 声称降级为 preliminary observation\n\n**N3** [critical] CMH 检验的 within-seed 独立性假设不成立\n- within-seed samples 共享模型权重，不是独立观测\n- 实际有效样本量远小于报告的 n=231，所有 p-values 被严重膨胀\n- 建议：使用 cluster-robust SE 或 GEE 以 seed 为 cluster，或报告 seed-level permutation test\n\n### Should-Fix 问题\n\n**W1** Seed 43 的 T=0.7 采样异常破坏实验一致性——为何不用 greedy 重新评估？\n\n**W2** Premise-count confound 未统计解决——McNemar p=0.317 意味着无法分离 ISR 差异与 premise-count 效应\n\n**W3** ProofFOL cross-dataset 证据不显著（p=0.10）——唯一 cross-dataset 实验不显著，削弱 C3\n\n**W4** ISR 作为 Shapley value 特例的定位需要更精确——LOO 丢失了组件间交互效应\n\n**W5** Hacking taxonomy 的分类器召回率未报告——实际 hacking 普遍性可能被低估\n\n### 主要优势\n1. 问题定位精准（execution-based evaluation 的盲点）\n2. 方法简洁无需训练\n3. 8-mode taxonomy 系统性强\n4. Controls 设计合理（Random, Shuffled-ISR, SFT）\n5. 透明度高，对局限性坦诚\n\n### 评分\n- Soundness: 3.0/5\n- Excitement: 3.5/5\n- Overall: 3.0/5 (Findings)\n\n---\n\n请逐条回应以上每个 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 2811 · 2026-05-22T23:31:52.793683+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19036
}
```

</details>

---


### Tool call

_source line 2812 · 2026-05-22T23:31:52.844557+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n### Must-Fix 问题\n\n**N1** [critical] 单模型泛化性严重不足，削弱核心 claims 的通用性\n- 所有收敛实验仅在 Qwen3-4B 上完成，8B 和 LLaMA 均未收敛\n- 结构退化可能是 Qwen3-4B 特定的 artifact 而非 GRPO 通用现象\n- 建议：C1 的 \"model-agnostic\" 改为 \"model-independent in design\"；Conclusion 的通用性降级为 future work\n\n**N2** [critical] ISR 的诊断价值自我矛盾：与推理质量零相关（ρ=−0.049）却被定位为 \"structural proxy for reasoning quality\"\n- Abstract/Introduction 暗示 ISR 是推理质量的代理，但 ISR 与 NLI accuracy 不相关\n- \"structural degeneration\" 术语有误导性，应叫 \"component redundancy collapse\"\n- 建议：Abstract 明确 ISR 衡量 component redundancy 而非 reasoning quality\n\n**N3** [critical] 核心量化 claim 被 premise-count confound 几乎完全解释\n- 214× ISR collapse 控制 premise count 后缩减至 1.06×（p=0.317）\n- ISR 作为标量指标的诊断价值几乎为零\n- 真正有价值的是 hacking mode classification 而非 ISR 数值\n- 建议：降低 ISR 标量强调，前置 mode-level analysis\n\n### Should-Fix 问题\n\n**W1** 标题过长（~140 chars），\"Case Study\" 与 \"cross-domain evidence\" 存在张力\n\n**W2** SFT baseline 比较不公平：PR=13% vs PR=93%——混淆了优化方式和 prove rate 水平\n\n**W3** N=3 seeds 统计推断力度过弱，bimodal 5-seed 结果进一步削弱——建议 CMH 移至 Appendix\n\n**W4** Observe-vs-optimize asymmetry 缺乏超越 Goodhart's Law 的概念新颖性\n\n**W5** 主文正文可能超出 8 页限制——Section 5 有 8-10 行溢出到 page 9\n\n### 主要优势\n1. Controls 值得肯定（random, shuffled-ISR, SFT）\n2. 学术诚实度极高\n3. 8-mode taxonomy 有实用价值\n4. Compositional mode shift 是最有说服力的发现\n5. Related work 覆盖全面且时效性强\n\n### Missing References\n1. MO-GRPO (Arxiv 2509.22047): GRPO 多目标 reward hacking\n2. \"Reward Hacking as Equilibrium under Finite Evaluation\" (Arxiv 2603.28063): reward hacking 是结构性均衡\n\n### 评分\n- Soundness: 3.0/5\n- Excitement: 3.0/5\n- Overall: 3.0/5 (Findings)\n\n---\n\n请逐条回应以上每个 Must-Fix 和 Should-Fix 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n### Must-Fix 问题\n\n**N1** [critical] 单模型泛化性严重不足，削弱核心 claims 的通用性\n- 所有收敛实验仅在 Qwen3-4B 上完成，8B 和 LLaMA 均未收敛\n- 结构退化可能是 Qwen3-4B 特定的 artifact 而非 GRPO 通用现象\n- 建议：C1 的 \"model-agnostic\" 改为 \"model-independent in design\"；Conclusion 的通用性降级为 future work\n\n**N2** [critical] ISR 的诊断价值自我矛盾：与推理质量零相关（ρ=−0.049）却被定位为 \"structural proxy for reasoning quality\"\n- Abstract/Introduction 暗示 ISR 是推理质量的代理，但 ISR 与 NLI accuracy 不相关\n- \"structural degeneration\" 术语有误导性，应叫 \"component redundancy collapse\"\n- 建议：Abstract 明确 ISR 衡量 component redundancy 而非 reasoning quality\n\n**N3** [critical] 核心量化 claim 被 premise-count confound 几乎完全解释\n- 214× ISR collapse 控制 premise count 后缩减至 1.06×（p=0.317）\n- ISR 作为标量指标的诊断价值几乎为零\n- 真正有价值的是 hacking mode classification 而非 ISR 数值\n- 建议：降低 ISR 标量强调，前置 mode-level analysis\n\n### Should-Fix 问题\n\n**W1** 标题过长（~140 chars），\"Case Study\" 与 \"cross-domain evidence\" 存在张力\n\n**W2** SFT baseline 比较不公平：PR=13% vs PR=93%——混淆了优化方式和 prove rate 水平\n\n**W3** N=3 seeds 统计推断力度过弱，bimodal 5-seed 结果进一步削弱——建议 CMH 移至 Appendix\n\n**W4** Observe-vs-optimize asymmetry 缺乏超越 Goodhart's Law 的概念新颖性\n\n**W5** 主文正文可能超出 8 页限制——Section 5 有 8-10 行溢出到 page 9\n\n### 主要优势\n1. Controls 值得肯定（random, shuffled-ISR, SFT）\n2. 学术诚实度极高\n3. 8-mode taxonomy 有实用价值\n4. Compositional mode shift 是最有说服力的发现\n5. Related work 覆盖全面且时效性强\n\n### Missing References\n1. MO-GRPO (Arxiv 2509.22047): GRPO 多目标 reward hacking\n2. \"Reward Hacking as Equilibrium under Finite Evaluation\" (Arxiv 2603.28063): reward hacking 是结构性均衡\n\n### 评分\n- Soundness: 3.0/5\n- Excitement: 3.0/5\n- Overall: 3.0/5 (Findings)\n\n---\n\n请逐条回应以上每个 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 2813 · 2026-05-22T23:31:54.257928+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1413
}
```

</details>

---


### Assistant

_source line 2814 · 2026-05-22T23:31:56.808222+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 256

## Round 256

2 recorded events


### User

_source line 2815 · 2026-05-22T23:31:59.378305+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿完成摘要**：

- **Overall: 3.0/5（Findings 级别）**
- **3 个 Must-Fix**：(N1) 单模型泛化性不足——只有 Qwen3-4B 收敛，无法排除 model-specific artifact；(N2) ISR 与推理质量零相关（ρ=−0.049）却被包装为结构质量代理——framing 矛盾；(N3) 214× ISR collapse 在控制 premise count 后缩减至 1.06×（p=0.317）——核心量化 claim 几乎完全是 confound
- **5 个 Should-Fix**：标题过长且 Case Study/cross-domain 矛盾、SFT 比较不公平、N=3 seeds 统计不足、observe-vs-optimize 本质是 Goodhart 重述、主文可能超 8 页
- **主要优势**：实验控制设计好（shuffled-ISR 尤其巧妙）、学术诚实度高、8-mode taxonomy 有实用价值、compositional mode shift 是最有说服力的发现

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2816 · 2026-05-22T23:32:03.505380+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 257

## Round 257

2 recorded events


### User

_source line 2817 · 2026-05-22T23:33:10.509371+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 Round 1 意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 单模型实验无法支撑通用性声称**

同意。这与我的 N1 一致。论文在 C1 中声称 "model-agnostic diagnostic method"、Section 5 中声称 "applicable in principle to any RL system"，但实证仅限 Qwen3-4B。Qwen3-8B（Appendix E.7, K=8 不收敛, K=4 零梯度）和 LLaMA-3.2-3B（Appendix E.5, FOL 生成失败）的负面结果进一步说明该现象的模型依赖性尚未被排除。

补充一点 R1 未明确提及的：论文对 8B/LLaMA 失败的解读（"degeneration requires successful convergence as a prerequisite"）在逻辑上是 unfalsifiable 的——任何不展示退化的模型都可以被归因为"未收敛"，而非"该现象不存在"。这个解读方向对论文有利但不可证伪，应更谨慎表述。

**[AGREE] R1-N2: N=3 seeds 统计效力不足**

同意，但在严重程度判断上有细微差异。R1 要求 8-10 seeds per condition——这在计算资源上可能对 GRPO 训练不现实（论文报告约 80-120 GPU-hours，Appendix A）。我认为更务实的建议是：

1. 将所有 pooled 统计结论降级为 "exploratory/descriptive"（论文在 Section 4.1 已部分做到这一点）
2. 保留 per-seed qualitative analysis 作为主要叙事框架
3. 5-seed 的 bimodal 结果（3/5 gaming vs 2/5 genuine, Section 4.3）反而是一个有价值的发现——它说明 GRPO+ISR 的结果是 inherently stochastic 的，这本身就是一个贡献，前提是作者不过度解读 pooled averages

关键区别：R1 将此定为 "Must-Fix"，我在自己的 review 中定为 "Should-Fix"（W3）。原因是论文在 Section 4.1 已有相当充分的自我限定（"CMH p-values... should not be interpreted as formal inference over the seed population"）。如果这些限定已经到位，问题不在于论文不知道这个限制，而在于正文中 CMH 结果的呈现方式是否给读者造成了过强的统计推断印象。我建议将 CMH 移至 Appendix 而非要求增加 seeds。

**[AGREE with nuance] R1-N3: CMH within-seed 独立性假设**

原则上同意 R1 的统计论点：within-seed samples 共享模型权重，非独立观测，CMH 的 p-values 确实存在膨胀风险。

但需指出论文已主动限定（Section 4.1, lines 16-18）："CMH p-values are reported as descriptive summaries of the stratified association; with N=3 strata they should not be interpreted as formal inference over the seed population." 这个 caveat 在一定程度上化解了 R1 的担忧——论文并未将 CMH 作为 formal inference 使用。

R1 建议的 cluster-robust SE 或 GEE 方案在 N=3 clusters 下同样缺乏统计效力（cluster-robust SE 在少于 30-50 clusters 时估计偏差严重）。seed-level permutation test 在 N=3 下只有 3!=6 种排列，p-value 下界为 1/6≈0.167，无法达到常规显著性水平。

**我的建议与 R1 不同**：与其修改统计方法（在 N=3 下任何方法都缺乏效力），不如将 CMH 结果整体从主文移至 Appendix，主文完全依赖 per-seed qualitative analysis + compositional mode shift 的描述性证据。这比换一种同样无力的统计检验更诚实。

---

### Should-Fix 问题

**[AGREE] R1-W1: Seed 43 的 T=0.7 采样异常**

同意。论文解释 seed 43 因 "greedy-mode degeneration" 改用 nucleus sampling（Section 4.1, footnote 10），但未解释为何不能用 greedy 模式重新评估（即使 generation 质量下降，至少保持评估一致性），或者干脆替换为另一个能 greedy 解码的 seed。N=2 sensitivity analysis（Appendix, excluding s43）说明排除 s43 后结论 "consistent or stronger"，这在一定程度上缓解了担忧，但根本问题（评估协议不一致）仍在。

**[AGREE] R1-W2: Premise-count confound 未统计解决**

完全同意。这与我的 N3 一致。214× raw ISR collapse 在控制 premise count 后缩减至 1.06×（McNemar p=0.317），意味着 ISR 作为标量指标的诊断信号几乎完全来自 premise-count 差异，而非结构退化本身。论文的主要证据链因此必须转向 compositional mode shift（CE→TS），而非标量 ISR——这一转向在 Section 4.3 中已发生，但 Abstract/Figure 1 的叙事仍以标量 ISR collapse 为核心。

**[AGREE] R1-W3: ProofFOL cross-dataset 证据不显著**

同意。p=0.10 在 N=3 seeds 下不显著，论文自己也标注为 "exploratory and underpowered"（Section 4.1）。C3 的 "cross-dataset evidence" 声称因此缺乏统计支撑。公平地说，ProofFOL exec-only 的定性复现（converged seeds collapse to near-zero genuine reasoning, Section 4.4）仍有描述性价值，但不应作为 formal claim。

**[AGREE with nuance] R1-W4: ISR 作为 Shapley 特例的定位**

部分同意。R1 指出 LOO 丢失组件间交互效应——论文已在 Section 3.2 "LOO independence assumption" 段明确讨论：LOO "systematically underestimat[es] ISR when jointly-necessary components exist; the observed collapse is therefore conservative"。这个 caveat 方向正确：LOO 的局限使观测到的 collapse 是 conservative estimate，即实际退化可能更严重。

但 R1 的关切不仅是技术准确性，也是定位问题：论文将 ISR 与 Shapley value 的关系作为理论贡献点（Section 3.2），但这个联系过于浅层（仅限于 "restricted to (n-1)-coalition" 的等价性说明），既未提供 Shapley-based 的新洞见，也未利用 Shapley 的理论工具（如 efficiency axiom）。建议要么展开论述 Shapley 联系的实际意义，要么将其移至 footnote 级别。

**[AGREE] R1-W5: Hacking taxonomy 分类器召回率未报告**

同意。论文报告了 precision（152-sample audit, Appendix D, "estimated precision >95%"），但未报告 recall。Table 8 声称 recall "inherently bounded by the text-match threshold"，但这只适用于 CE/TS 的 text-match 检测，不适用于通过 functional analysis 检测的 PG、contradiction explosion 等模式。在 recall 未知的情况下，报告的 non-hacking rate（如 exec-only 的 8%）实际上是 upper bound——真实 non-hacking 可能更低。论文在 Section 4.1 确实将 N-H 定义为 "upper bound on genuine reasoning"，但这个定义容易被读者忽略。

---

### 与 R1 评分的比较

| 维度 | R1 | R2 (我) | 差异说明 |
|------|-----|---------|----------|
| Soundness | 3.0 | 3.0 | 一致 |
| Excitement | 3.5 | 3.0 | R1 认为问题定位和 taxonomy 的实用性较高；我认为方法新颖性有限（标准 LOO 的应用）拉低了 excitement |
| Overall | 3.0 | 3.0 | 一致：Findings 级别 |

总体上，R1 和我对论文的核心优缺点判断高度一致。主要分歧在于：
1. R1 将 N=3 seeds 定为 Must-Fix，我定为 Should-Fix（因论文已有充分 caveat）
2. R1 未重点讨论 ISR 与推理质量的零相关（我的 N2），这是我认为论文最根本的 framing 矛盾
3. R1 给 Excitement 3.5，我给 3.0——差异源于对方法新颖性的评估标准不同

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2818 · 2026-05-22T23:33:16.187219+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 258

## Round 258

2 recorded events


### User

_source line 2819 · 2026-05-22T23:33:23.157055+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 全部 8 条意见的逐条回应。核心判断：

- **N1 (单模型)**: [AGREE]，补充了 "未收敛=不存在退化" 的不可证伪性问题
- **N2 (N=3 seeds)**: [AGREE]，但建议将 CMH 移至 Appendix 而非要求增加 seeds（计算成本不现实）
- **N3 (CMH 独立性)**: [AGREE with nuance]，指出论文已有 caveat，且 R1 建议的替代统计方法（cluster-robust SE, permutation test）在 N=3 下同样无力
- **W1-W5**: 全部 [AGREE]，其中 W2 (premise-count confound) 与我的 N3 一致，W4 (Shapley 定位) 建议降级至 footnote

R1 和我的评分高度一致（均为 Overall 3.0 / Findings），主要分歧在 Excitement（R1: 3.5 vs 我: 3.0）和我额外指出的 ISR-NLI 零相关 framing 矛盾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2820 · 2026-05-22T23:33:27.992987+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 259

## Round 259

8 recorded events


### User

_source line 2821 · 2026-05-22T23:33:57.489125+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 Round 1 意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 单模型泛化性严重不足**
同意，与我的 N1 判断一致。论文唯一成功收敛的模型是 Qwen3-4B，Qwen3-8B（Appendix E.7 Table 14）和 LLaMA-3.2-3B（Appendix E.4）均未能收敛。R2 提出的 "model-independent in design" 措辞精确——方法设计上确实不依赖特定模型架构（操作 solver trace 而非模型内部），但实验验证仅覆盖一个架构。我也同意 Conclusion 的通用性声称应降级为 future work。

补充：我在自己的审稿中注意到一个额外的 concern——cross-scale 和 cross-architecture 的全面失败不仅是验证缺失的问题，它可能暗示 structural degeneration 现象本身依赖于模型的特定 capacity/capability 组合，而非 GRPO 的通用行为模式。

**[REBUT] R2-N2: ISR 诊断价值自我矛盾**
R2 的 concern 部分有道理但结论过度。分两点反驳：

1. **"structural degeneration" 比 "component redundancy collapse" 更准确**。论文的 hacking taxonomy（Appendix D）涵盖 8 种 degeneration mode——conclusion embedding（D.2）、tautological shortcutting（D.5）、obfuscated tautology（D.4）、query-as-fact gaming（D.9）等，远不止 "component redundancy"。这些 mode 描述的是 formalization 的结构完整性退化，不仅是冗余。R2 建议的重命名会丢失这一多样性。

2. **ISR 与 NLI accuracy 不相关恰恰支撑了论文的核心论点**。论文在 Section 3.2 "Limitations of ISR" 中明确说明 ISR 衡量 component necessity 而非 semantic faithfulness。ISR 与 NLI 不相关说明 execution accuracy（NLI）无法检测结构退化——这正是论文主张的 "evaluation gap"（Section 1 第 2 段）。如果 ISR 与 NLI 高度相关，反而不需要 STA 了。

但我同意 R2 的一个方向：Abstract 和 Introduction 中 "structural proxies for reasoning quality"（Section 5）这一措辞确实有歧义。建议改为 "structural proxies for formalization integrity" 或类似表述，与 Section 3.2 的 limitation 声明保持一致。

**[AGREE in part] R2-N3: Premise-count confound**
同意 R2 的核心观察：214× scalar ISR collapse 在 premise-count matching 后缩减至 1.06×（p=0.317, Appendix C Table 9），说明 **scalar ISR 的诊断价值主要来自 compositional mode shift（模型转向更短的 formalization），而非同等 premise count 下的结构差异**。这与我自己的 W2 判断一致。

但不同意 R2 "ISR 标量诊断价值几乎为零" 的结论，理由如下：
- **ISR 的二分类功能（hacking/non-hacking）不受 premise-count 影响**。Table 1 的 mode composition 分析（CE/TS 比例变化）是论文最有说服力的发现——ISR reward 下 TS 从 0% 涨至 71%（Table 1），这一 compositional shift 不依赖 scalar ISR 值。
- 论文已在 Section 4.2 和 Appendix C 中正确识别了这一 confound，并通过 mode composition analysis 绕过了它。

我同意 R2 的建议方向：**主文应降低 scalar ISR 的强调（特别是 "214× collapse" 的叙述），将 mode-level compositional analysis 前置为主要证据**。当前 ISR 标量在 Abstract 和 Section 4.2 中占据了过多叙述空间。

---

### Should-Fix 问题

**[AGREE] R2-W1: 标题过长**
标题约 140 字符，确实过长。"Case Study" 与 "Diagnoses...Goodhart Effects" 的组合产生了 scope 张力——前者暗示 exploratory，后者暗示 definitive。建议精简至 ~80 字符，例如 "Solver Trace Ablation: Diagnosing Structural Degeneration in GRPO-Trained Neurosymbolic Reasoning"。

**[REBUT] R2-W2: SFT baseline 比较不公平**
R2 指出 SFT PR=13% vs GRPO PR=93% 导致比较不公平，这一观察是对的，但论文的使用方式并非直接公平对比。论文在 Section 4.3 中将 SFT 定位为 "pre-RL reference"，其目的是建立一个 "RL 优化前" 的 baseline，证明 hacking 是 RL 训练引入的而非预训练固有的。真正的公平控制是 **Random control（β=0.1）**——它与 ISR β=0.1 共享相同的 prove rate 水平（Table 1: ISR PR=87%, Random PR=67%），且使用相同的 multiplicative reward 结构，仅 ISR signal 被替换为 uniform random。这一控制充分隔离了 ISR-specific 效应。

SFT 的低 PR 正是其作为 pre-RL reference 的价值所在——它证明在 RL 优化提升 prove rate 之前，结构退化不存在（SFT: 0% TS, 8% N-H, Table 1）。将 SFT 的 hacking rate 与 GRPO 对比不是比较优化方式的公平性，而是建立 "before/after" 时间线。

**[AGREE] R2-W3: N=3 seeds 统计推断力度过弱**
完全同意，与我的 N2（critical）和 N3（critical）一致。CMH 移至 Appendix 是合理的建议——主文应报告 seed-level aggregate statistics 而非依赖 within-seed sample-level 检验。

**[AGREE in part] R2-W4: Observe-vs-optimize asymmetry 缺乏概念新颖性**
R2 指出这本质上是 Goodhart's Law 的直接实例化，概念层面并无超越，这一判断是公正的。但我认为 **empirical demonstration 在特定 domain 中仍有价值**：论文首次在 neurosymbolic reasoning 的 solver trace 层面量化展示了 Goodhart 效应的具体机制（从 observation 到 reward 的转换导致 ISR 崩溃），并识别了 8 种具体的 gaming 路径。概念框架不新，但实证贡献是 domain-specific 的。

建议：论文应弱化 "observe-vs-optimize asymmetry" 作为独立概念贡献的措辞，改为强调这是 Goodhart's Law 在 neurosymbolic RLVR 中的首个系统性实证研究。

**[AGREE conditionally] R2-W5: 主文可能超出 8 页限制**
根据我对 PDF 的阅读，Section 5 "Discussion and Conclusion"（属于主文）确实有数行文字延伸到了第 9 页顶部，之后才进入 Section 6 "Limitations"（不计入页数）。如果确认 Section 5 的任何部分超出第 8 页底部，这构成格式违规。

但需注意：这一判断取决于对 PDF 排版的精确测量。如果 Section 5 刚好在第 8 页底部结束而 Section 6 从第 9 页开始，则不违规。建议作者仔细检查并在必要时压缩 Section 5（如将部分 discussion 内容移至 Limitations 或 Appendix）。

---

### 关于 R2 提出的 Missing References

两篇 R2 推荐的参考文献（MO-GRPO Arxiv 2509.22047、"Reward Hacking as Equilibrium" Arxiv 2603.28063）我无法独立验证其存在性和准确性（arXiv ID 格式 2509/2603 对应 2025 年 9 月和 2026 年 3 月）。如果论文在 ARR May 2026 cycle 提交，2026 年 3 月的论文可能尚未广泛传播。建议作者自行查证相关性。

---

### 总结

R2 的 3 个 Must-Fix 中，N1（单模型）我完全同意；N2（ISR 诊断价值矛盾）我认为结论过度但方向有道理（framing 需要收紧）；N3（premise-count confound）核心观察正确但 "诊断价值为零" 的判断过强——mode-level analysis 不受此 confound 影响。

R2 的 5 个 Should-Fix 中，W1（标题）、W3（seeds）同意；W2（SFT 比较）反驳——Random control 才是公平控制，SFT 是 temporal reference；W4（概念新颖性）部分同意但 empirical contribution 有独立价值；W5（页数）需作者确认。

R2 与我的 Overall Assessment 一致（3.0, Findings），但我给 Excitement 3.5/5 略高于 R2 的 3.0/5，原因是我认为 STA 工具和 hacking taxonomy 的实用价值被 R2 低估了。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2822 · 2026-05-22T23:34:29.798407+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2823 · 2026-05-22T23:34:29.900207+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T23:23:03.595813+00:00\", \"completed_at\": \"2026-05-22T23:26:43.382789+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 5-6\", \"message\": \"连续两页纯文本（实验设置 §4.1 和 hacking taxonomy §4.3），无任何 display item 穿插。建议在 §4.1 实验设置中加入数据集统计表或实验流程简图，改善视觉节奏\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"三个 display items（Figure 2 + Figure 3 + Table 2）密集堆叠在同一页，导致 Figure 2 和 Figure 3 尺寸偏小。与 pages 5-6 的纯文本形成密度不均。建议将 Table 2 或 Figure 3 移至 page 7 或 page 9 以平衡分布\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 和 Figure 3 的轴标签和图例文字接近可读性下限（约为正文字号的 65-70%），建议适当增大图表尺寸或字号\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 caption 较长（5 行），信息密度高但自包含性好——审稿人能从 caption 单独理解图表含义，这是优点\"}, {\"severity\": \"info\", \"dimension\": \"page 24\", \"message\": \"Appendix 末页底部约 40% 空白——不影响审稿印象但空间可进一步利用\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 3}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2824 · 2026-05-22T23:36:40.933031+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n- id: R1-W1\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。\"\n  resolution_round: 2\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 32\n  resolution: \"Two-level Goodhart separation: scalar confound acknowledged (McNemar p=0.317 n.s.), compositional mode shift established as primary evidence via seed-stratified χ² (174.8, p<10⁻³⁸).\"\n  resolution_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识：premise-count matched 后 1.06× (p=0.317) 使 Goodhart 标量证据不成立。R1 建议以 mode-shift 为主证据并提供统计检验。R2 补充：mode-shift ≠ 经典 Goodhart。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 两位 Reviewer 再次共识：214× scalar ISR collapse 几乎完全是 premise-count artifact。R2 升为 Must-Fix (N3)，认为 ISR 标量诊断价值几乎为零。R1 同意核心观察但反驳'为零'结论——mode-level analysis 不受 confound 影响。共识：主文应降低 scalar ISR 强调，前置 mode-level compositional analysis。\"\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 31\n  resolution: \"Compositional Goodhart reframed around mode shift (CE→TS), not scalar non-hacking rate. χ² test (174.8, p<10⁻³⁸) as independent evidence. Per-seed analysis all independently significant.\"\n  resolution_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 复现：non-hacking ISR vs Random p=0.182 仍不显著。两位 Reviewer 一致要求 Abstract/Title 降级 Goodhart 表述。\"\n- id: v17-R12-W1\n  summary: \"单模型 (Qwen3-4B) 无法支撑通用性声明\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 32\n  resolution: \"C1 scoped to 'model-agnostic diagnostic method' (design property); C2/C3 scoped to 'in Qwen3-4B experiments'. Cannot add models (8B/LLaMA non-convergence). Fundamental limitation acknowledged.\"\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识最严重问题：Qwen3-4B + FOLIO 单模型单数据集，8B/LLaMA 均未收敛。R2 追问是否仅 Qwen3-4B + ProofWriter 的 artifact。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 两位 Reviewer 再次一致列为最严重 Must-Fix。R2 补充：论文对 8B/LLaMA 失败的解读('收敛是退化前提')在逻辑上不可证伪。R1 补充：cross-scale 全面失败可能暗示退化依赖特定 capacity/capability 组合。共识建议：C1 改为 'model-independent in design'，Conclusion 通用性降级为 future work。\"\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 32\n  resolution: \"CMH repositioned as 'descriptive summaries of stratified association' with explicit N=3 caveat. Per-seed χ² test added as primary evidence (each seed independently significant).\"\n  resolution_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 R1 升为 Must-Fix。R2 同意核心批评但修正真实N=3表述。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 R1 维持 Must-Fix (N3)。R2 [AGREE with nuance]：论文已有 caveat，但正文呈现方式仍给读者过强统计推断印象。R2 指出 R1 建议的 cluster-robust SE/GEE 在 N=3 下同样无力。共识建议：将 CMH 整体移至 Appendix，主文依赖 per-seed qualitative analysis。\"\n- id: v17-R1-W9\n  summary: \"Seed 43 使用 T=0.7 sampling 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 32\n  resolution: \"N=2 sensitivity analysis added (excluding s43). Both remaining seeds reach ≤7% non-hacking at 500 steps. s43 flagged in limitations.\"\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识 Must-Fix。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 两位 Reviewer [AGREE]。R1 追问：为何不用 greedy 重新评估 seed 43 checkpoint？计算成本应很低。N=2 sensitivity analysis 缓解但不解决根本问题（评估协议不一致）。\"\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 32\n  mentions:\n  - round: 31\n    reviewers: [R2]\n    note: \"R31 R2 维持 Must-Fix。R1 部分反驳。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 R2 维持：LOO 本身无创新，observe-vs-optimize 是 Goodhart 重述，Excitement 3.0。R1 部分同意但认为 empirical demonstration 在 neurosymbolic domain 仍有独立价值，给 Excitement 3.5。分歧在于方法新颖性 vs 实证贡献价值的权重。\"\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念——本质即 Goodhart's Law\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 29\n  last_seen_round: 32\n  resolution: \"Reframed as meta-observation about Goodhart's law in neurosymbolic RLVR, not claiming conceptual novelty.\"\n  resolution_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：observe-vs-optimize asymmetry 本质是 Goodhart 重述。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 R2 维持 Should-Fix (W4)。R1 [AGREE in part]：概念框架不新，但 empirical demonstration 有 domain-specific 价值。共识建议：弱化 observe-vs-optimize 作为独立概念贡献，改为 'empirical instantiation of Goodhart's Law in neurosymbolic RLVR'。\"\n- id: v30-R1-W1\n  summary: \"SFT baseline PR=13% vs exec-only PR=93% 使 ISR 比较存在 selection bias\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"SFT repositioned as upper bound reference, not matched control.\"\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识：SFT 应定位为 upper bound 而非 matched control。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 分歧：R2 维持 Should-Fix (W2)，认为 PR 差距混淆了两个变量。R1 [REBUT]：SFT 是 temporal reference（pre-RL baseline），Random control 才是公平对照。R1 的反驳有理——Random β=0.1 与 ISR β=0.1 在 reward 结构上对等，仅 ISR signal 被替换。\"\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 31\n  resolution: \"Acknowledged as underpowered in limitations. Cannot increase N without additional training runs.\"\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：46 proved samples 严重 underpowered。\"\n  - round: 32\n    reviewers: []\n    note: \"R32 本轮未被显式提及。\"\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证 50 样本偏少 + recall 未评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 32\n  resolution: \"152 samples validated with precision=1.00. Recall limitation acknowledged in paper.\"\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：152 样本 precision=1.00 但 recall 不可估。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 R1-W5 再次提出 recall 未报告。R2 [AGREE]：在 recall 未知下 non-hacking rate 是 upper bound。论文已将 N-H 定义为 upper bound 但易被读者忽略。\"\n- id: v19-R12-W3\n  summary: \"ProofFOL p=0.10 被过度引用\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 32\n  resolution: \"'substantially higher' → 'directionally higher' for ProofFOL p=0.10 results.\"\n  resolution_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：p=0.10 在 §4.4 用 substantially 表述不当。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 两位 Reviewer [AGREE]：p=0.10 不显著，C3 cross-dataset claim 缺乏统计支撑。R1 建议降低 C3 声称强度，定位为 pilot experiment。ProofFOL silver-standard 数据质量（59.1% 通过率）也存疑。\"\n- id: v30-R2-W3\n  summary: \"ISR 与 NLI accuracy 不相关限制 actionability\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"ISR=0 semantic disambiguation added to method.tex.\"\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 ISR=0 语义模糊性讨论。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 R2 升为 Must-Fix (N2)：ISR 与 NLI ρ=−0.049 使其定位为 'structural proxy for reasoning quality' 自相矛盾。R1 [REBUT]：零相关恰好支撑论文论点（execution accuracy 无法检测结构退化），但同意 framing 需收紧——'structural proxies for reasoning quality' 应改为 'structural proxies for formalization integrity'。分歧：R2 要求重命名为 'component redundancy collapse'，R1 认为 'structural degeneration' 更准确（涵盖 8 种 mode，不仅是冗余）。\"\n- id: v31-R2-MR-SPECGAMING\n  summary: \"缺失引用：Towards Understanding Specification Gaming in Reasoning Models (arXiv:2605.02269)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"Nishimura et al. (2026) citation added to related_work.tex with discussion of spec gaming theory.\"\n  resolution_round: 31\n- id: v31-R2-W-TITLE-LENGTH\n  summary: \"标题过长（~140 chars），建议精简\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n  - round: 31\n    reviewers: [R2]\n    note: \"R2 建议精简至 ~60 chars。R1 反驳无硬限制，可考虑 ~90 chars。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 两位 Reviewer [AGREE]：~140 chars 过长。R2 建议 ~80 chars。R1 同意并建议 'Solver Trace Ablation: Diagnosing Structural Degeneration in GRPO-Trained Neurosymbolic Reasoning'。额外问题：'Case Study' 与 C3 cross-domain claim 存在叙事张力。\"\n- id: v31-R2-M-ISR0-AMBIGUITY\n  summary: \"ISR=0 对 proved vs unproved 语义不同但用同一值\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"ISR=0 semantic disambiguation added to method.tex. Unproved samples use ISR* (proved-only) metric throughout analysis.\"\n  resolution_round: 31\n- id: v32-R2-N2-FRAMING\n  summary: \"ISR 被定位为 'structural proxy for reasoning quality' 但与 NLI accuracy 零相关（ρ=−0.049），framing 矛盾\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R2 升为 Must-Fix：Abstract/Intro 暗示 ISR 是推理质量代理，但与 NLI 不相关。R1 部分反驳：零相关恰好支撑 evaluation gap 论点，但同意需将 'reasoning quality' 改为 'formalization integrity'。分歧：R2 要求 'component redundancy collapse'，R1 认为 'structural degeneration' 涵盖 8 种 mode 更准确。\"\n- id: v32-R1-N2-SEEDS\n  summary: \"N=3 seeds 对 bimodal dynamics 统计效力严重不足，CMH 应移至 Appendix\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R1 列为 Must-Fix，R2 列为 Should-Fix。bimodal 5-seed 结果（3/5 gaming vs 2/5 genuine）使 3-seed pooled 统计不可信。共识：CMH 移至 Appendix，主文聚焦 per-seed qualitative analysis。R2 指出 cluster-robust SE 在 N=3 下同样无力，建议降级所有 pooled 统计为 exploratory/descriptive。\"\n- id: v32-R2-W5-PAGELIMIT\n  summary: \"Section 5 (Discussion and Conclusion) 可能溢出 8 页限制\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R2 指出 Section 5 有 8-10 行溢出到 page 9。R1 条件性同意，需作者精确测量确认。若确认溢出则构成格式违规。\"\n- id: v32-R1-W4-SHAPLEY\n  summary: \"ISR 作为 Shapley value (n-1)-coalition 特例的定位过于浅层\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R1-W4：LOO 丢失组件间交互效应，Shapley 联系未提供新洞见。R2 [AGREE with nuance]：论文已讨论 LOO independence assumption，但 Shapley 定位过于浅层，建议降级至 footnote 或展开论述实际意义。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n- id: R1-W1\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。\"\n  resolution_round: 2\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 32\n  resolution: \"Two-level Goodhart separation: scalar confound acknowledged (McNemar p=0.317 n.s.), compositional mode shift established as primary evidence via seed-stratified χ² (174.8, p<10⁻³⁸).\"\n  resolution_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识：premise-count matched 后 1.06× (p=0.317) 使 Goodhart 标量证据不成立。R1 建议以 mode-shift 为主证据并提供统计检验。R2 补充：mode-shift ≠ 经典 Goodhart。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 两位 Reviewer 再次共识：214× scalar ISR collapse 几乎完全是 premise-count artifact。R2 升为 Must-Fix (N3)，认为 ISR 标量诊断价值几乎为零。R1 同意核心观察但反驳'为零'结论——mode-level analysis 不受 confound 影响。共识：主文应降低 scalar ISR 强调，前置 mode-level compositional analysis。\"\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 31\n  resolution: \"Compositional Goodhart reframed around mode shift (CE→TS), not scalar non-hacking rate. χ² test (174.8, p<10⁻³⁸) as independent evidence. Per-seed analysis all independently significant.\"\n  resolution_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 复现：non-hacking ISR vs Random p=0.182 仍不显著。两位 Reviewer 一致要求 Abstract/Title 降级 Goodhart 表述。\"\n- id: v17-R12-W1\n  summary: \"单模型 (Qwen3-4B) 无法支撑通用性声明\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 32\n  resolution: \"C1 scoped to 'model-agnostic diagnostic method' (design property); C2/C3 scoped to 'in Qwen3-4B experiments'. Cannot add models (8B/LLaMA non-convergence). Fundamental limitation acknowledged.\"\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识最严重问题：Qwen3-4B + FOLIO 单模型单数据集，8B/LLaMA 均未收敛。R2 追问是否仅 Qwen3-4B + ProofWriter 的 artifact。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 两位 Reviewer 再次一致列为最严重 Must-Fix。R2 补充：论文对 8B/LLaMA 失败的解读('收敛是退化前提')在逻辑上不可证伪。R1 补充：cross-scale 全面失败可能暗示退化依赖特定 capacity/capability 组合。共识建议：C1 改为 'model-independent in design'，Conclusion 通用性降级为 future work。\"\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 32\n  resolution: \"CMH repositioned as 'descriptive summaries of stratified association' with explicit N=3 caveat. Per-seed χ² test added as primary evidence (each seed independently significant).\"\n  resolution_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 R1 升为 Must-Fix。R2 同意核心批评但修正真实N=3表述。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 R1 维持 Must-Fix (N3)。R2 [AGREE with nuance]：论文已有 caveat，但正文呈现方式仍给读者过强统计推断印象。R2 指出 R1 建议的 cluster-robust SE/GEE 在 N=3 下同样无力。共识建议：将 CMH 整体移至 Appendix，主文依赖 per-seed qualitative analysis。\"\n- id: v17-R1-W9\n  summary: \"Seed 43 使用 T=0.7 sampling 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 32\n  resolution: \"N=2 sensitivity analysis added (excluding s43). Both remaining seeds reach ≤7% non-hacking at 500 steps. s43 flagged in limitations.\"\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识 Must-Fix。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 两位 Reviewer [AGREE]。R1 追问：为何不用 greedy 重新评估 seed 43 checkpoint？计算成本应很低。N=2 sensitivity analysis 缓解但不解决根本问题（评估协议不一致）。\"\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 32\n  mentions:\n  - round: 31\n    reviewers: [R2]\n    note: \"R31 R2 维持 Must-Fix。R1 部分反驳。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 R2 维持：LOO 本身无创新，observe-vs-optimize 是 Goodhart 重述，Excitement 3.0。R1 部分同意但认为 empirical demonstration 在 neurosymbolic domain 仍有独立价值，给 Excitement 3.5。分歧在于方法新颖性 vs 实证贡献价值的权重。\"\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念——本质即 Goodhart's Law\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 29\n  last_seen_round: 32\n  resolution: \"Reframed as meta-observation about Goodhart's law in neurosymbolic RLVR, not claiming conceptual novelty.\"\n  resolution_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：observe-vs-optimize asymmetry 本质是 Goodhart 重述。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 R2 维持 Should-Fix (W4)。R1 [AGREE in part]：概念框架不新，但 empirical demonstration 有 domain-specific 价值。共识建议：弱化 observe-vs-optimize 作为独立概念贡献，改为 'empirical instantiation of Goodhart's Law in neurosymbolic RLVR'。\"\n- id: v30-R1-W1\n  summary: \"SFT baseline PR=13% vs exec-only PR=93% 使 ISR 比较存在 selection bias\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"SFT repositioned as upper bound reference, not matched control.\"\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 两位 Reviewer 共识：SFT 应定位为 upper bound 而非 matched control。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 分歧：R2 维持 Should-Fix (W2)，认为 PR 差距混淆了两个变量。R1 [REBUT]：SFT 是 temporal reference（pre-RL baseline），Random control 才是公平对照。R1 的反驳有理——Random β=0.1 与 ISR β=0.1 在 reward 结构上对等，仅 ISR signal 被替换。\"\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 31\n  resolution: \"Acknowledged as underpowered in limitations. Cannot increase N without additional training runs.\"\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：46 proved samples 严重 underpowered。\"\n  - round: 32\n    reviewers: []\n    note: \"R32 本轮未被显式提及。\"\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证 50 样本偏少 + recall 未评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 32\n  resolution: \"152 samples validated with precision=1.00. Recall limitation acknowledged in paper.\"\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：152 样本 precision=1.00 但 recall 不可估。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 R1-W5 再次提出 recall 未报告。R2 [AGREE]：在 recall 未知下 non-hacking rate 是 upper bound。论文已将 N-H 定义为 upper bound 但易被读者忽略。\"\n- id: v19-R12-W3\n  summary: \"ProofFOL p=0.10 被过度引用\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 32\n  resolution: \"'substantially higher' → 'directionally higher' for ProofFOL p=0.10 results.\"\n  resolution_round: 31\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 共识：p=0.10 在 §4.4 用 substantially 表述不当。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 两位 Reviewer [AGREE]：p=0.10 不显著，C3 cross-dataset claim 缺乏统计支撑。R1 建议降低 C3 声称强度，定位为 pilot experiment。ProofFOL silver-standard 数据质量（59.1% 通过率）也存疑。\"\n- id: v30-R2-W3\n  summary: \"ISR 与 NLI accuracy 不相关限制 actionability\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"ISR=0 semantic disambiguation added to method.tex.\"\n  mentions:\n  - round: 31\n    reviewers: [R1, R2]\n    note: \"R31 ISR=0 语义模糊性讨论。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 R2 升为 Must-Fix (N2)：ISR 与 NLI ρ=−0.049 使其定位为 'structural proxy for reasoning quality' 自相矛盾。R1 [REBUT]：零相关恰好支撑论文论点（execution accuracy 无法检测结构退化），但同意 framing 需收紧——'structural proxies for reasoning quality' 应改为 'structural proxies for formalization integrity'。分歧：R2 要求重命名为 'component redundancy collapse'，R1 认为 'structural degeneration' 更准确（涵盖 8 种 mode，不仅是冗余）。\"\n- id: v31-R2-MR-SPECGAMING\n  summary: \"缺失引用：Towards Understanding Specification Gaming in Reasoning Models (arXiv:2605.02269)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"Nishimura et al. (2026) citation added to related_work.tex with discussion of spec gaming theory.\"\n  resolution_round: 31\n- id: v31-R2-W-TITLE-LENGTH\n  summary: \"标题过长（~140 chars），建议精简\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n  - round: 31\n    reviewers: [R2]\n    note: \"R2 建议精简至 ~60 chars。R1 反驳无硬限制，可考虑 ~90 chars。\"\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R32 两位 Reviewer [AGREE]：~140 chars 过长。R2 建议 ~80 chars。R1 同意并建议 'Solver Trace Ablation: Diagnosing Structural Degeneration in GRPO-Trained Neurosymbolic Reasoning'。额外问题：'Case Study' 与 C3 cross-domain claim 存在叙事张力。\"\n- id: v31-R2-M-ISR0-AMBIGUITY\n  summary: \"ISR=0 对 proved vs unproved 语义不同但用同一值\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"ISR=0 semantic disambiguation added to method.tex. Unproved samples use ISR* (proved-only) metric throughout analysis.\"\n  resolution_round: 31\n- id: v32-R2-N2-FRAMING\n  summary: \"ISR 被定位为 'structural proxy for reasoning quality' 但与 NLI accuracy 零相关（ρ=−0.049），framing 矛盾\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R2 升为 Must-Fix：Abstract/Intro 暗示 ISR 是推理质量代理，但与 NLI 不相关。R1 部分反驳：零相关恰好支撑 evaluation gap 论点，但同意需将 'reasoning quality' 改为 'formalization integrity'。分歧：R2 要求 'component redundancy collapse'，R1 认为 'structural degeneration' 涵盖 8 种 mode 更准确。\"\n- id: v32-R1-N2-SEEDS\n  summary: \"N=3 seeds 对 bimodal dynamics 统计效力严重不足，CMH 应移至 Appendix\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R1 列为 Must-Fix，R2 列为 Should-Fix。bimodal 5-seed 结果（3/5 gaming vs 2/5 genuine）使 3-seed pooled 统计不可信。共识：CMH 移至 Appendix，主文聚焦 per-seed qualitative analysis。R2 指出 cluster-robust SE 在 N=3 下同样无力，建议降级所有 pooled 统计为 exploratory/descriptive。\"\n- id: v32-R2-W5-PAGELIMIT\n  summary: \"Section 5 (Discussion and Conclusion) 可能溢出 8 页限制\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R2 指出 Section 5 有 8-10 行溢出到 page 9。R1 条件性同意，需作者精确测量确认。若确认溢出则构成格式违规。\"\n- id: v32-R1-W4-SHAPLEY\n  summary: \"ISR 作为 Shapley value (n-1)-coalition 特例的定位过于浅层\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n  - round: 32\n    reviewers: [R1, R2]\n    note: \"R1-W4：LOO 丢失组件间交互效应，Shapley 联系未提供新洞见。R2 [AGREE with nuance]：论文已讨论 LOO independence assumption，但 Shapley 定位过于浅层，建议降级至 footnote 或展开论述实际意义。\""
  }
}
```

</details>

---


### Tool result

_source line 2825 · 2026-05-22T23:36:41.034914+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 10973}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2826 · 2026-05-22T23:39:11.756042+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "solver-trace-ablation",
  "report": "# 审稿报告 — Round 32 (Fresh Review)\n\n**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n**Venue**: EMNLP 2026 (ARR May Cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+完整性+Related Work+写作质量）\n**审稿轮次**: 1 轮（Round 1 + 交叉分享，收敛达成）\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 Leave-One-Out (LOO) 消融的诊断方法，检测 GRPO 训练的 neurosymbolic reasoning 系统中的结构退化。核心指标 ISR (Intensional Structural Reward) 衡量形式化输出中组件必要性的比例。论文在 Qwen3-4B 上跨 6 种 reward 条件、两种逻辑类型（FOL/Prolog）和两个数据集（FOLIO/ProofFOL）进行实验，构建了 8 类 hacking 分类体系，实证展示 ISR 从诊断工具转为 reward 信号时的 Goodhart 效应：ISR reward 不减少 hacking 总量，而是将 hacking 模式从 conclusion embedding (CE) 转移为 tautological shortcutting (TS)。\n\n---\n\n## Strengths\n\n**S1.** 问题定位精准且时机恰当——识别了 GRPO 训练 neurosymbolic reasoning 中 execution-based evaluation 的盲点（结构退化在 prove rate 上升时发生），问题对 RLVR 领域有实际意义。[R1, R2 共识]\n\n**S2.** 实验控制设计合理——Random control（隔离 ISR-specific 效应）、Shuffled-ISR（打破 sample-level 语义同时保留 ISR 分布）和 SFT baseline（建立 pre-RL reference）三个控制条件有效分离因果效应。Shuffled-ISR 的设计尤其巧妙。[R1, R2 共识]\n\n**S3.** 8-mode hacking taxonomy 系统性强且有实用价值——CE, TS, TSb, PG, Query-as-fact 等分类有清晰操作定义，152-sample precision audit 增加可信度。该分类体系对其他研究者诊断自身系统中的 reward hacking 有参考意义。[R1, R2 共识]\n\n**S4.** Compositional mode shift（CE→TS）是最有说服力的发现——在所有 controls 下保持一致，不受 premise-count confound 影响，是 Goodhart 效应在 neurosymbolic reasoning 中的最干净实证。[R1, R2 共识]\n\n**S5.** 学术诚实度极高——论文对自身缺陷的讨论（premise-count confound、ISR-NLI 零相关、seed bimodality、N=3 限制、单模型限制）异常坦诚，在投稿论文中罕见。[R1, R2 共识]\n\n**S6.** 方法简洁且无需额外训练——STA 只需对 solver input 做逐一消融，不涉及模型内部，不依赖人工标注，计算成本 O(n) per sample，易于被其他研究者采用。[R1]\n\n**S7.** Related work 覆盖全面且时效性强——涵盖了 2026 年初的最新 concurrent work（Helff et al., Khalifa et al., Nishimura et al., Wilhelm et al.），每篇都有清楚的定位对比。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [critical] 单模型（Qwen3-4B）无法支撑通用性声称** [R1-N1, R2-N1; AGREE×2]\n- 论文成功收敛的唯一模型是 Qwen3-4B。Qwen3-8B 两种配置均未收敛（Appendix E.7），LLaMA-3.2-3B FOL 生成完全失败（Appendix E.5）。\n- Title 使用泛化表述\"GRPO-Trained Neurosymbolic Reasoning\"，C1 声称\"model-agnostic diagnostic method\"，Section 5 声称\"applicable in principle to any RL system\"——均超出单模型实证的支撑范围。\n- R2 补充：论文对 8B/LLaMA 失败的解读（\"degeneration requires successful convergence as a prerequisite\"）在逻辑上不可证伪——任何不展示退化的模型都可归因为\"未收敛\"。\n- **建议**：C1 改为\"model-independent in design\"；Title/Abstract scope 限定为 Qwen3-4B；Section 5 通用性降级为 future work hypothesis。\n\n**MF2. [critical] ISR scalar 诊断价值被 premise-count confound 几乎完全解释** [R1-W2→N级, R2-N3; AGREE×2]\n- 214× raw ISR collapse 在控制 premise count 后缩减至 1.06×（McNemar p=0.317），统计上不显著。ISR 标量测到的主要是\"模型生成更短的 formalization\"而非同等条件下的结构差异。\n- 论文的主要证据链已转向 compositional mode shift（CE→TS），但 Abstract/Figure 1 的叙事仍以标量 ISR collapse 为核心。\n- R1 反驳 R2\"诊断价值为零\"的结论：mode-level analysis 不受此 confound 影响，ISR 的二分类功能（per-sample hacking/non-hacking）仍有效。\n- **建议**：降低 Abstract/Introduction 中 scalar ISR 的强调；前置 mode-level compositional analysis 作为主要贡献；Figure 1 加注 premise-count confound 幅度。\n\n**MF3. [critical] N=3 seeds 统计效力不足 + CMH within-seed 独立性不成立** [R1-N2+N3, R2-W3; AGREE×2，严重程度有分歧]\n- N=3 seeds 面对 bimodal dynamics（5-seed 扩展中 3/5 gaming vs 2/5 genuine）尤为不足。CMH 检验将 within-seed samples 视为独立观测，但同一 checkpoint 生成的 formalization 共享模型权重，非独立。\n- 论文已有 caveat（Section 4.1: \"CMH p-values... should not be interpreted as formal inference\"），但正文仍引用 CMH 结果。\n- R2 指出 R1 建议的替代统计方法（cluster-robust SE, GEE, permutation test）在 N=3 下同样缺乏效力。\n- **共识建议**：将 CMH 整体从主文移至 Appendix；主文聚焦 per-seed qualitative analysis + compositional mode shift 的描述性证据；所有 pooled 统计降级为 exploratory/descriptive。\n- *严重程度分歧*：R1 列为 Must-Fix，R2 列为 Should-Fix（认为论文已有充分 caveat）。综合评定为 Must-Fix。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [warning] ISR framing 需收紧：与 NLI accuracy 零相关（ρ=−0.049）** [R2-N2; R1 部分 REBUT]\n- Abstract/Introduction 将 ISR 定位为\"structural proxy for reasoning quality\"，但 ISR 与 NLI accuracy 不相关。\n- R1 反驳：零相关恰好支撑论文论点（execution accuracy 无法检测结构退化），\"structural degeneration\"比\"component redundancy collapse\"更准确（涵盖 8 种 mode）。但 R1 同意 framing 需调整。\n- **共识建议**：将\"structural proxies for reasoning quality\"改为\"structural proxies for formalization integrity\"；在 Abstract 中明确 ISR 衡量 component necessity 而非 semantic faithfulness。\n- *分歧记录*：R2 建议用\"component redundancy collapse\"替代\"structural degeneration\"；R1 认为后者涵盖更广（8 种 mode 不仅是冗余）。\n\n**SF2. [warning] 标题过长（~140 chars），\"Case Study\"与 cross-domain claim 存在张力** [R1, R2 AGREE]\n- 建议精简至 ~80 chars，移除 Case Study 或将 C3 cross-domain claim 降级。\n- R1 建议：\"Solver Trace Ablation: Diagnosing Structural Degeneration in GRPO-Trained Neurosymbolic Reasoning\"\n\n**SF3. [warning] Seed 43 的 T=0.7 采样异常破坏实验一致性** [R1-W1, R2 AGREE]\n- 为何不用 greedy decoding 重新评估 seed 43 checkpoint？计算成本应很低。N=2 sensitivity analysis 缓解但不解决根本问题（评估协议不一致）。\n\n**SF4. [warning] ProofFOL cross-dataset 证据不显著（p=0.10），削弱 C3** [R1-W3, R2 AGREE]\n- 唯一的 cross-dataset 实验不显著。ProofFOL 本身是 GPT-4o silver-standard 数据（~70% 通过率），质量存疑。\n- **建议**：降低 C3 声称强度；将 ProofFOL 明确定位为 pilot experiment。\n\n**SF5. [warning] Observe-vs-optimize asymmetry 缺乏超越 Goodhart's Law 的概念新颖性** [R2-W4; R1 AGREE in part]\n- 本质是 Goodhart's Law 在特定 domain 的重述。R1 认为 empirical demonstration 有独立价值。\n- **建议**：定位为\"empirical instantiation of Goodhart's Law in neurosymbolic RLVR\"，弱化独立概念贡献的措辞。\n\n**SF6. [warning] Hacking taxonomy 分类器 recall 未报告** [R1-W5, R2 AGREE]\n- Precision 通过 152-sample audit 验证（1.00），但 recall 未知。non-hacking rate 实际上是 upper bound。\n\n**SF7. [warning] 主文正文可能超出 8 页限制** [R2-W5; R1 条件性 AGREE]\n- Section 5 (Discussion and Conclusion) 可能有 8-10 行溢出到 page 9。需作者精确测量确认。若确认则构成格式违规。\n\n**SF8. [warning] SFT baseline 比较的公平性讨论不足** [R2-W2; R1 REBUT]\n- R2 指出 SFT PR=13% vs exec-only PR=93% 混淆两个变量。R1 反驳：SFT 是 temporal reference（pre-RL），Random control 才是公平对照。\n- *分歧记录*：R1 的反驳有理——Random β=0.1 与 ISR β=0.1 在 reward 结构上对等。但论文可更明确讨论 SFT 的角色定位。\n\n### Minor（不影响接收）\n\n- Section 3.2 ISR 公式中 S(x) 定义可以更早引入\n- Figure 1 legend 标注方式不直观（需查 Appendix 了解 seed 编号）\n- Table 1 caption 过长（~120 words），markers 密集\n- Pages 5-6 连续纯文本无 display items，视觉节奏不佳（视觉审查发现）\n- Page 8 三个 display items 密集堆叠，Figure 2/3 尺寸偏小（视觉审查发现）\n- Related Work 最后一段引用密度高但区分度不够\n- ISR 与 Shapley value 的关联定位过于浅层，建议降级至 footnote 或展开论述\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **单模型限制是最核心问题**：两位 Reviewer 一致认为这是论文最严重的缺陷，是 conference-level 接收的主要障碍。\n2. **ISR scalar 被 premise-count confound 解释**：共识认为 mode-level compositional analysis 是真正有价值的贡献，scalar ISR 叙事应降级。\n3. **CMH 应移至 Appendix**：主文应依赖 per-seed qualitative analysis。\n4. **Compositional mode shift 是最有说服力的发现**：不受 confound 影响，是 Goodhart 效应的干净实证。\n5. **8-mode taxonomy 是有实用价值的贡献**：适合 Findings 级别。\n6. **学术透明度值得肯定**：论文对自身局限的坦诚讨论在投稿论文中罕见。\n\n## Reviewer Divergence [REBUT]\n\n1. **ISR 与 NLI 零相关的解读**：R2 认为这是根本性 framing 矛盾（Must-Fix）；R1 认为零相关支撑论文论点，仅需调整措辞（Should-Fix）。综合评定为 Should-Fix，因 R1 的反驳有理（ISR 的设计目标是检测 execution accuracy 无法发现的问题）。\n2. **SFT 比较公平性**：R2 认为不公平（Should-Fix）；R1 认为 SFT 是 temporal reference，Random control 才是公平对照（REBUT）。R1 反驳有理，记录为分歧。\n3. **Excitement 评分**：R1 给 3.5/5（认为 STA 工具和 taxonomy 实用性高）；R2 给 3.0/5（认为方法新颖性有限拉低 excitement）。\n\n---\n\n## Questions（需作者澄清）\n\n1. 为何不用 greedy decoding 重新评估 seed 43 的已保存 checkpoint？计算成本应很低。\n2. 是否可以报告 within-seed ICC 来量化组内相关性，帮助读者判断 CMH p-values 的真实可靠度？\n3. ISR 与 NLI accuracy 零相关——在实际部署场景中，ISR 无法区分\"正确但结构冗余\"和\"错误但结构紧凑\"的推理。ISR 相对于简单 component-count 统计的增量诊断价值是什么？\n4. 论文声称 STA \"applicable in principle to any RL system whose output is verified by a deterministic checker\"——但数学推理中的 formal verification（如 Lean 4）是否满足 LOO 可行性条件？定理证明中移除一个步骤通常不产生有意义的 ablation（证明是链式依赖而非独立前提）。\n5. 如果 ISR β=0.1 扩展到 10-20 seeds，bimodal 分布是否会稳定？这对\"GRPO 导致结构退化\"的泛化性意味什么？\n6. Qwen3-8B 不收敛是否可能是超参数问题（K=8 vs K=4）而非模型能力问题？\n7. Hacking mode 分类是否强制互斥？一个 sample 符合多个 modes 时如何处理？\n8. 加法形式 reward（r_exec + β×ISR）是否被测试过？乘法形式的 reward landscape 特殊结构对结论有何影响？\n\n---\n\n## Missing References\n\n**R1 建议（可能相关）**：\n- Lanham et al., 2023 \"Measuring Faithfulness in Chain-of-Thought Reasoning\" — component necessity 理念与 CoT faithfulness 有联系\n- Turpin et al., 2023 \"Language Models Don't Always Say What They Think\" — model output 与 internal reasoning 的 disconnect\n\n**R2 建议（待验证）**：\n- MO-GRPO (arXiv 2509.22047) — GRPO 多目标 reward hacking\n- \"Reward Hacking as Equilibrium under Finite Evaluation\" (arXiv 2603.28063) — reward hacking 作为结构性均衡\n\n*注：R2 推荐的两篇引用的 arXiv ID 未经独立验证，建议作者自行查证。*\n\n---\n\n## External Review\n\n外部审稿：未配置/未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成，0 critical / 2 warning / 3 info：\n\n- **[warning] Pages 5-6**：连续两页纯文本（§4.1 实验设置和 §4.3 hacking taxonomy），无 display item 穿插。建议加入数据集统计表或实验流程简图改善视觉节奏。\n- **[warning] Page 8**：三个 display items（Figure 2 + Figure 3 + Table 2）密集堆叠，Figure 2/3 尺寸偏小。建议分散分布。\n- **[info] Page 8**：Figure 2/3 轴标签和图例文字接近可读性下限（约正文字号 65-70%）。\n- **[info] Page 2**：Figure 1 caption 较长但自包含性好，是优点。\n- **[info] Appendix 末页**：底部约 40% 空白，不影响审稿印象。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 / 5 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.0 | 3.0 | 3.0 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.0 | 3.0 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分理由**：\n\n论文记录了 GRPO 训练中 neurosymbolic reasoning 的一个有价值的现象——结构退化和 Goodhart 模式转移。实验控制设计合理，8-mode hacking taxonomy 有实用价值，学术透明度高。\n\n但三个核心问题制约 conference-level 接收：(1) 单模型验证无法排除 Qwen3-4B-specific artifact 的可能；(2) ISR 标量诊断价值被 premise-count confound 几乎完全解释，真正有价值的是 mode-level 分析；(3) N=3 seeds 面对 bimodal dynamics 统计效力严重不足。\n\n论文最有价值的贡献——compositional mode shift 实证和 8-mode taxonomy——属于 Findings 级别。如果能补充至少一个替代模型的成功实验并收紧 ISR framing，有潜力升至 3.5 (Borderline Conference)。\n\n**置信度: 4/5** — 两位 Reviewer 均仔细阅读全文含全部附录，熟悉 RLVR、neurosymbolic reasoning 和 reward hacking 领域，对核心判断高度一致。\n\n---\n\n## Detailed Comments（逐节意见）\n\n### Abstract\n- \"structural proxies for reasoning quality\" 应改为 \"structural proxies for formalization integrity\"（R1 建议，R2 方向一致）\n- 隐含 ISR 标量价值的叙事应弱化\n\n### Introduction\n- C1 \"model-agnostic diagnostic method\" 改为 \"model-independent in design\"\n- \"observe-vs-optimize asymmetry\" 定位为 Goodhart's Law 的实证实例化，非独立概念贡献\n\n### Method (Section 3)\n- ISR 与 Shapley value 的关联定位过浅，建议降级至 footnote 或展开论述 LOO 丢失交互效应的实际频率\n- ISR=0 的 proved vs unproved 语义区分已改善\n\n### Experiments (Section 4)\n- Section 4.1: CMH 统计移至 Appendix，主文用 per-seed qualitative analysis\n- Section 4.2: 214× ISR collapse 叙事前置 premise-count confound caveat\n- Section 4.3: Bimodal 5-seed 结果是有价值的发现但不应过度解读 pooled averages\n- Section 4.4: ProofFOL 降级为 pilot experiment，C3 声称强度降低\n\n### Discussion and Conclusion (Section 5)\n- 可能超出 8 页限制——需检查并在必要时压缩\n- \"applicable in principle to any RL system\" 降级为 future work\n- 对 Lean 4 等链式证明系统 LOO 可行性的讨论可增加\n\n### Limitations (Section 6)\n- 已覆盖主要问题，但可更明确讨论 ISR-NLI 零相关对实际应用的影响",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "solver-trace-ablation",
    "report": "# 审稿报告 — Round 32 (Fresh Review)\n\n**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n**Venue**: EMNLP 2026 (ARR May Cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+完整性+Related Work+写作质量）\n**审稿轮次**: 1 轮（Round 1 + 交叉分享，收敛达成）\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 Leave-One-Out (LOO) 消融的诊断方法，检测 GRPO 训练的 neurosymbolic reasoning 系统中的结构退化。核心指标 ISR (Intensional Structural Reward) 衡量形式化输出中组件必要性的比例。论文在 Qwen3-4B 上跨 6 种 reward 条件、两种逻辑类型（FOL/Prolog）和两个数据集（FOLIO/ProofFOL）进行实验，构建了 8 类 hacking 分类体系，实证展示 ISR 从诊断工具转为 reward 信号时的 Goodhart 效应：ISR reward 不减少 hacking 总量，而是将 hacking 模式从 conclusion embedding (CE) 转移为 tautological shortcutting (TS)。\n\n---\n\n## Strengths\n\n**S1.** 问题定位精准且时机恰当——识别了 GRPO 训练 neurosymbolic reasoning 中 execution-based evaluation 的盲点（结构退化在 prove rate 上升时发生），问题对 RLVR 领域有实际意义。[R1, R2 共识]\n\n**S2.** 实验控制设计合理——Random control（隔离 ISR-specific 效应）、Shuffled-ISR（打破 sample-level 语义同时保留 ISR 分布）和 SFT baseline（建立 pre-RL reference）三个控制条件有效分离因果效应。Shuffled-ISR 的设计尤其巧妙。[R1, R2 共识]\n\n**S3.** 8-mode hacking taxonomy 系统性强且有实用价值——CE, TS, TSb, PG, Query-as-fact 等分类有清晰操作定义，152-sample precision audit 增加可信度。该分类体系对其他研究者诊断自身系统中的 reward hacking 有参考意义。[R1, R2 共识]\n\n**S4.** Compositional mode shift（CE→TS）是最有说服力的发现——在所有 controls 下保持一致，不受 premise-count confound 影响，是 Goodhart 效应在 neurosymbolic reasoning 中的最干净实证。[R1, R2 共识]\n\n**S5.** 学术诚实度极高——论文对自身缺陷的讨论（premise-count confound、ISR-NLI 零相关、seed bimodality、N=3 限制、单模型限制）异常坦诚，在投稿论文中罕见。[R1, R2 共识]\n\n**S6.** 方法简洁且无需额外训练——STA 只需对 solver input 做逐一消融，不涉及模型内部，不依赖人工标注，计算成本 O(n) per sample，易于被其他研究者采用。[R1]\n\n**S7.** Related work 覆盖全面且时效性强——涵盖了 2026 年初的最新 concurrent work（Helff et al., Khalifa et al., Nishimura et al., Wilhelm et al.），每篇都有清楚的定位对比。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [critical] 单模型（Qwen3-4B）无法支撑通用性声称** [R1-N1, R2-N1; AGREE×2]\n- 论文成功收敛的唯一模型是 Qwen3-4B。Qwen3-8B 两种配置均未收敛（Appendix E.7），LLaMA-3.2-3B FOL 生成完全失败（Appendix E.5）。\n- Title 使用泛化表述\"GRPO-Trained Neurosymbolic Reasoning\"，C1 声称\"model-agnostic diagnostic method\"，Section 5 声称\"applicable in principle to any RL system\"——均超出单模型实证的支撑范围。\n- R2 补充：论文对 8B/LLaMA 失败的解读（\"degeneration requires successful convergence as a prerequisite\"）在逻辑上不可证伪——任何不展示退化的模型都可归因为\"未收敛\"。\n- **建议**：C1 改为\"model-independent in design\"；Title/Abstract scope 限定为 Qwen3-4B；Section 5 通用性降级为 future work hypothesis。\n\n**MF2. [critical] ISR scalar 诊断价值被 premise-count confound 几乎完全解释** [R1-W2→N级, R2-N3; AGREE×2]\n- 214× raw ISR collapse 在控制 premise count 后缩减至 1.06×（McNemar p=0.317），统计上不显著。ISR 标量测到的主要是\"模型生成更短的 formalization\"而非同等条件下的结构差异。\n- 论文的主要证据链已转向 compositional mode shift（CE→TS），但 Abstract/Figure 1 的叙事仍以标量 ISR collapse 为核心。\n- R1 反驳 R2\"诊断价值为零\"的结论：mode-level analysis 不受此 confound 影响，ISR 的二分类功能（per-sample hacking/non-hacking）仍有效。\n- **建议**：降低 Abstract/Introduction 中 scalar ISR 的强调；前置 mode-level compositional analysis 作为主要贡献；Figure 1 加注 premise-count confound 幅度。\n\n**MF3. [critical] N=3 seeds 统计效力不足 + CMH within-seed 独立性不成立** [R1-N2+N3, R2-W3; AGREE×2，严重程度有分歧]\n- N=3 seeds 面对 bimodal dynamics（5-seed 扩展中 3/5 gaming vs 2/5 genuine）尤为不足。CMH 检验将 within-seed samples 视为独立观测，但同一 checkpoint 生成的 formalization 共享模型权重，非独立。\n- 论文已有 caveat（Section 4.1: \"CMH p-values... should not be interpreted as formal inference\"），但正文仍引用 CMH 结果。\n- R2 指出 R1 建议的替代统计方法（cluster-robust SE, GEE, permutation test）在 N=3 下同样缺乏效力。\n- **共识建议**：将 CMH 整体从主文移至 Appendix；主文聚焦 per-seed qualitative analysis + compositional mode shift 的描述性证据；所有 pooled 统计降级为 exploratory/descriptive。\n- *严重程度分歧*：R1 列为 Must-Fix，R2 列为 Should-Fix（认为论文已有充分 caveat）。综合评定为 Must-Fix。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [warning] ISR framing 需收紧：与 NLI accuracy 零相关（ρ=−0.049）** [R2-N2; R1 部分 REBUT]\n- Abstract/Introduction 将 ISR 定位为\"structural proxy for reasoning quality\"，但 ISR 与 NLI accuracy 不相关。\n- R1 反驳：零相关恰好支撑论文论点（execution accuracy 无法检测结构退化），\"structural degeneration\"比\"component redundancy collapse\"更准确（涵盖 8 种 mode）。但 R1 同意 framing 需调整。\n- **共识建议**：将\"structural proxies for reasoning quality\"改为\"structural proxies for formalization integrity\"；在 Abstract 中明确 ISR 衡量 component necessity 而非 semantic faithfulness。\n- *分歧记录*：R2 建议用\"component redundancy collapse\"替代\"structural degeneration\"；R1 认为后者涵盖更广（8 种 mode 不仅是冗余）。\n\n**SF2. [warning] 标题过长（~140 chars），\"Case Study\"与 cross-domain claim 存在张力** [R1, R2 AGREE]\n- 建议精简至 ~80 chars，移除 Case Study 或将 C3 cross-domain claim 降级。\n- R1 建议：\"Solver Trace Ablation: Diagnosing Structural Degeneration in GRPO-Trained Neurosymbolic Reasoning\"\n\n**SF3. [warning] Seed 43 的 T=0.7 采样异常破坏实验一致性** [R1-W1, R2 AGREE]\n- 为何不用 greedy decoding 重新评估 seed 43 checkpoint？计算成本应很低。N=2 sensitivity analysis 缓解但不解决根本问题（评估协议不一致）。\n\n**SF4. [warning] ProofFOL cross-dataset 证据不显著（p=0.10），削弱 C3** [R1-W3, R2 AGREE]\n- 唯一的 cross-dataset 实验不显著。ProofFOL 本身是 GPT-4o silver-standard 数据（~70% 通过率），质量存疑。\n- **建议**：降低 C3 声称强度；将 ProofFOL 明确定位为 pilot experiment。\n\n**SF5. [warning] Observe-vs-optimize asymmetry 缺乏超越 Goodhart's Law 的概念新颖性** [R2-W4; R1 AGREE in part]\n- 本质是 Goodhart's Law 在特定 domain 的重述。R1 认为 empirical demonstration 有独立价值。\n- **建议**：定位为\"empirical instantiation of Goodhart's Law in neurosymbolic RLVR\"，弱化独立概念贡献的措辞。\n\n**SF6. [warning] Hacking taxonomy 分类器 recall 未报告** [R1-W5, R2 AGREE]\n- Precision 通过 152-sample audit 验证（1.00），但 recall 未知。non-hacking rate 实际上是 upper bound。\n\n**SF7. [warning] 主文正文可能超出 8 页限制** [R2-W5; R1 条件性 AGREE]\n- Section 5 (Discussion and Conclusion) 可能有 8-10 行溢出到 page 9。需作者精确测量确认。若确认则构成格式违规。\n\n**SF8. [warning] SFT baseline 比较的公平性讨论不足** [R2-W2; R1 REBUT]\n- R2 指出 SFT PR=13% vs exec-only PR=93% 混淆两个变量。R1 反驳：SFT 是 temporal reference（pre-RL），Random control 才是公平对照。\n- *分歧记录*：R1 的反驳有理——Random β=0.1 与 ISR β=0.1 在 reward 结构上对等。但论文可更明确讨论 SFT 的角色定位。\n\n### Minor（不影响接收）\n\n- Section 3.2 ISR 公式中 S(x) 定义可以更早引入\n- Figure 1 legend 标注方式不直观（需查 Appendix 了解 seed 编号）\n- Table 1 caption 过长（~120 words），markers 密集\n- Pages 5-6 连续纯文本无 display items，视觉节奏不佳（视觉审查发现）\n- Page 8 三个 display items 密集堆叠，Figure 2/3 尺寸偏小（视觉审查发现）\n- Related Work 最后一段引用密度高但区分度不够\n- ISR 与 Shapley value 的关联定位过于浅层，建议降级至 footnote 或展开论述\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **单模型限制是最核心问题**：两位 Reviewer 一致认为这是论文最严重的缺陷，是 conference-level 接收的主要障碍。\n2. **ISR scalar 被 premise-count confound 解释**：共识认为 mode-level compositional analysis 是真正有价值的贡献，scalar ISR 叙事应降级。\n3. **CMH 应移至 Appendix**：主文应依赖 per-seed qualitative analysis。\n4. **Compositional mode shift 是最有说服力的发现**：不受 confound 影响，是 Goodhart 效应的干净实证。\n5. **8-mode taxonomy 是有实用价值的贡献**：适合 Findings 级别。\n6. **学术透明度值得肯定**：论文对自身局限的坦诚讨论在投稿论文中罕见。\n\n## Reviewer Divergence [REBUT]\n\n1. **ISR 与 NLI 零相关的解读**：R2 认为这是根本性 framing 矛盾（Must-Fix）；R1 认为零相关支撑论文论点，仅需调整措辞（Should-Fix）。综合评定为 Should-Fix，因 R1 的反驳有理（ISR 的设计目标是检测 execution accuracy 无法发现的问题）。\n2. **SFT 比较公平性**：R2 认为不公平（Should-Fix）；R1 认为 SFT 是 temporal reference，Random control 才是公平对照（REBUT）。R1 反驳有理，记录为分歧。\n3. **Excitement 评分**：R1 给 3.5/5（认为 STA 工具和 taxonomy 实用性高）；R2 给 3.0/5（认为方法新颖性有限拉低 excitement）。\n\n---\n\n## Questions（需作者澄清）\n\n1. 为何不用 greedy decoding 重新评估 seed 43 的已保存 checkpoint？计算成本应很低。\n2. 是否可以报告 within-seed ICC 来量化组内相关性，帮助读者判断 CMH p-values 的真实可靠度？\n3. ISR 与 NLI accuracy 零相关——在实际部署场景中，ISR 无法区分\"正确但结构冗余\"和\"错误但结构紧凑\"的推理。ISR 相对于简单 component-count 统计的增量诊断价值是什么？\n4. 论文声称 STA \"applicable in principle to any RL system whose output is verified by a deterministic checker\"——但数学推理中的 formal verification（如 Lean 4）是否满足 LOO 可行性条件？定理证明中移除一个步骤通常不产生有意义的 ablation（证明是链式依赖而非独立前提）。\n5. 如果 ISR β=0.1 扩展到 10-20 seeds，bimodal 分布是否会稳定？这对\"GRPO 导致结构退化\"的泛化性意味什么？\n6. Qwen3-8B 不收敛是否可能是超参数问题（K=8 vs K=4）而非模型能力问题？\n7. Hacking mode 分类是否强制互斥？一个 sample 符合多个 modes 时如何处理？\n8. 加法形式 reward（r_exec + β×ISR）是否被测试过？乘法形式的 reward landscape 特殊结构对结论有何影响？\n\n---\n\n## Missing References\n\n**R1 建议（可能相关）**：\n- Lanham et al., 2023 \"Measuring Faithfulness in Chain-of-Thought Reasoning\" — component necessity 理念与 CoT faithfulness 有联系\n- Turpin et al., 2023 \"Language Models Don't Always Say What They Think\" — model output 与 internal reasoning 的 disconnect\n\n**R2 建议（待验证）**：\n- MO-GRPO (arXiv 2509.22047) — GRPO 多目标 reward hacking\n- \"Reward Hacking as Equilibrium under Finite Evaluation\" (arXiv 2603.28063) — reward hacking 作为结构性均衡\n\n*注：R2 推荐的两篇引用的 arXiv ID 未经独立验证，建议作者自行查证。*\n\n---\n\n## External Review\n\n外部审稿：未配置/未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成，0 critical / 2 warning / 3 info：\n\n- **[warning] Pages 5-6**：连续两页纯文本（§4.1 实验设置和 §4.3 hacking taxonomy），无 display item 穿插。建议加入数据集统计表或实验流程简图改善视觉节奏。\n- **[warning] Page 8**：三个 display items（Figure 2 + Figure 3 + Table 2）密集堆叠，Figure 2/3 尺寸偏小。建议分散分布。\n- **[info] Page 8**：Figure 2/3 轴标签和图例文字接近可读性下限（约正文字号 65-70%）。\n- **[info] Page 2**：Figure 1 caption 较长但自包含性好，是优点。\n- **[info] Appendix 末页**：底部约 40% 空白，不影响审稿印象。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 / 5 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.0 | 3.0 | 3.0 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.0 | 3.0 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分理由**：\n\n论文记录了 GRPO 训练中 neurosymbolic reasoning 的一个有价值的现象——结构退化和 Goodhart 模式转移。实验控制设计合理，8-mode hacking taxonomy 有实用价值，学术透明度高。\n\n但三个核心问题制约 conference-level 接收：(1) 单模型验证无法排除 Qwen3-4B-specific artifact 的可能；(2) ISR 标量诊断价值被 premise-count confound 几乎完全解释，真正有价值的是 mode-level 分析；(3) N=3 seeds 面对 bimodal dynamics 统计效力严重不足。\n\n论文最有价值的贡献——compositional mode shift 实证和 8-mode taxonomy——属于 Findings 级别。如果能补充至少一个替代模型的成功实验并收紧 ISR framing，有潜力升至 3.5 (Borderline Conference)。\n\n**置信度: 4/5** — 两位 Reviewer 均仔细阅读全文含全部附录，熟悉 RLVR、neurosymbolic reasoning 和 reward hacking 领域，对核心判断高度一致。\n\n---\n\n## Detailed Comments（逐节意见）\n\n### Abstract\n- \"structural proxies for reasoning quality\" 应改为 \"structural proxies for formalization integrity\"（R1 建议，R2 方向一致）\n- 隐含 ISR 标量价值的叙事应弱化\n\n### Introduction\n- C1 \"model-agnostic diagnostic method\" 改为 \"model-independent in design\"\n- \"observe-vs-optimize asymmetry\" 定位为 Goodhart's Law 的实证实例化，非独立概念贡献\n\n### Method (Section 3)\n- ISR 与 Shapley value 的关联定位过浅，建议降级至 footnote 或展开论述 LOO 丢失交互效应的实际频率\n- ISR=0 的 proved vs unproved 语义区分已改善\n\n### Experiments (Section 4)\n- Section 4.1: CMH 统计移至 Appendix，主文用 per-seed qualitative analysis\n- Section 4.2: 214× ISR collapse 叙事前置 premise-count confound caveat\n- Section 4.3: Bimodal 5-seed 结果是有价值的发现但不应过度解读 pooled averages\n- Section 4.4: ProofFOL 降级为 pilot experiment，C3 声称强度降低\n\n### Discussion and Conclusion (Section 5)\n- 可能超出 8 页限制——需检查并在必要时压缩\n- \"applicable in principle to any RL system\" 降级为 future work\n- 对 Lean 4 等链式证明系统 LOO 可行性的讨论可增加\n\n### Limitations (Section 6)\n- 已覆盖主要问题，但可更明确讨论 ISR-NLI 零相关对实际应用的影响",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 2827 · 2026-05-22T23:39:15.822890+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Assistant

_source line 2828 · 2026-05-22T23:39:25.248755+00:00_

审稿报告已投递至 Research Director。

**Round 32 审稿完成。**

核心结论：**Overall 3.0/5 (Findings)**，两位 Reviewer 评分一致。

三个 Must-Fix 制约 conference-level 接收：
1. **单模型** — 仅 Qwen3-4B 收敛，8B/LLaMA 全部失败，无法排除 model-specific artifact
2. **ISR scalar confound** — 214× collapse 控制 premise count 后仅 1.06×（p=0.317），真正有价值的是 mode-level compositional analysis
3. **N=3 seeds + CMH 独立性** — bimodal dynamics 下统计效力严重不足，CMH 应移至 Appendix

最有价值的贡献是 compositional mode shift 实证（CE→TS，χ²=174.8, p<10⁻³⁸）和 8-mode hacking taxonomy，适合 Findings 接收。补充替代模型实验 + 收紧 ISR framing 可能升至 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 260

## Round 260

2 recorded events


### User

_source line 2829 · 2026-05-22T23:39:27.832254+00:00_

[Reviewer 1 审稿结果]:
对 Reviewer 2 全部 8 条意见的逐条回应已提交。核心判断：

- **N1 单模型**：完全同意
- **N2 ISR 诊断价值矛盾**：部分反驳——ISR-NLI 不相关恰恰支撑 evaluation gap 论点，但 framing 措辞需收紧；"structural degeneration" 比 R2 建议的 "component redundancy collapse" 更准确（涵盖 8 种 mode）
- **N3 Premise-count confound**：核心观察同意，但 "标量诊断价值为零" 过强——mode-level analysis 不受此 confound 影响
- **W2 SFT 比较不公平**：反驳——SFT 是 temporal reference，Random control 才是公平控制
- 其余 W1/W3/W4/W5 基本同意

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2830 · 2026-05-22T23:39:41.687318+00:00_

审稿报告已投递至 Research Director。

**Round 32 审稿总结**：

- **Overall: 3.0/5 (Findings)**，两位 Reviewer 评分完全一致
- **3 个 Must-Fix**：(1) 单模型验证无法排除 Qwen3-4B-specific artifact；(2) ISR scalar 被 premise-count confound 几乎完全解释（214×→1.06×, p=0.317）；(3) N=3 seeds + CMH 独立性不成立
- **8 个 Should-Fix**：ISR framing 矛盾、标题过长、seed 43 异常、ProofFOL 不显著、observe-vs-optimize 概念新颖性有限、recall 未报告、可能超页、SFT 比较讨论不足
- **核心共识**：compositional mode shift（CE→TS）是最有说服力的发现，8-mode taxonomy 有实用价值，适合 Findings 接收
- **Issue Tracker 已同步更新**：新增 4 条 issue，更新 10 条已有 issue 的最新状态

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 261

## Round 261

62 recorded events


### User

_source line 2831 · 2026-05-23T01:39:54.606165+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ✅ 后台自动运行中，完成后你会收到 [引用验证结果] 消息，请在合成报告时纳入

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2832 · 2026-05-23T01:39:59.894669+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2833 · 2026-05-23T01:39:59.945762+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2834 · 2026-05-23T01:40:06.524381+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 2835 · 2026-05-23T01:40:06.575097+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2836 · 2026-05-23T01:40:08.885452+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2837 · 2026-05-23T01:40:08.936206+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2838 · 2026-05-23T01:40:13.958634+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2839 · 2026-05-23T01:40:14.059510+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2840 · 2026-05-23T01:40:18.611848+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2841 · 2026-05-23T01:40:20.066826+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (216 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d158_llama_sft_s42（准备中）\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical powe
…[truncated 1872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1454
}
```

</details>

---


### Tool call

_source line 2842 · 2026-05-23T01:40:20.067227+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2843 · 2026-05-23T01:40:20.568879+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage{float}
13	\usepackage{placeins}
14	\usepackage[protrusion=true,expansion=false]{microtype}
15	
16	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
18	\setlength{\abovecaptionskip}{4pt}
19	\setlength{\belowcaptionskip}{2pt}
20	
21	\graphicspath{{figures/}}
22	
23	\title{Solver Trace Ablation: Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning}
24	
25	\author{Anonymous ACL submission}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	\input{introduction}
32	\input{related_work}
33	\input{method}
34	\input{experiments}
35	\input{conclusion}
36	
37	\input{limitations}
38	
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\appendix
44	\input{appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 2844 · 2026-05-23T01:40:20.569221+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 2845 · 2026-05-23T01:40:26.189425+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information about EMNLP 2026, but I did not find a specific main conference call for paper
…[truncated 1214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5620
}
```

</details>

---


### Tool call

_source line 2846 · 2026-05-23T01:40:29.352333+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission deadline May June guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission deadline May June guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 2847 · 2026-05-23T01:40:29.854829+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers main conference submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers main conference submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 2848 · 2026-05-23T01:40:31.612786+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2849 · 2026-05-23T01:40:31.663537+00:00_

1	\begin{abstract}
2	Execution-based evaluation of neurosymbolic reasoning conflates faithful derivation with structural shortcuts: a formalization that trivially embeds the conclusion among its premises proves just as reliably as a genuine one, and RL optimizers exploit this indifference.
3	We propose \emph{component necessity} as a diagnostic principle and operationalize it as \emph{Solver Trace Ablation} (STA): for each proved output, STA tests whether every component is individually required for proof success, yielding the \emph{Intensional Structural Reward} (ISR).
4	ISR reveals that prove-rate gains conceal a compositional shift toward hacking modes, but ISR occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.
5	Tautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
6	In our Qwen3-4B experiments, this \emph{observe-vs-optimize asymmetry} persists across logic types and dataset families: structural proxies for formalization integrity are easier to observe than to optimize.\footnote{Code and data: \url{[anonymized]}}
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2850 · 2026-05-23T01:40:35.579989+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission deadline May June guidelines page limit"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's the information about ACL Rolling Review (ARR) for 2026:

## Submission Deadlines

ARR switched to 10-week review cycles starting in May 2025. The submission deadline is always the 15th of the month. For 2026, there is a May 15 submission deadline.

## Guidelines and Requirements

Authors submit papers to a unified review pool with deadlines every two months. Key submission requirements include:

- All submitted papers are expected to describe original, completed and unpublished work
- Papers must
…[truncated 722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6227
}
```

</details>

---


### Tool result

_source line 2851 · 2026-05-23T01:40:39.194764+00:00_

Web search results for query: "EMNLP 2026 call for papers main conference submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026's main conference call for papers:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an 
…[truncated 1880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 9339
}
```

</details>

---


### Tool call

_source line 2852 · 2026-05-23T01:40:42.910931+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 long paper page limit 8 pages formatting requirements site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 long paper page limit 8 pages formatting requirements site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 2853 · 2026-05-23T01:40:43.715005+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2854 · 2026-05-23T01:40:43.765594+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2855 · 2026-05-23T01:40:49.403572+00:00_

Web search results for query: "EMNLP 2026 long paper page limit 8 pages formatting requirements site:2026.emnlp.org"

Links: [{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Physician- and Large Language Model-Generated Hospital Discharge Summaries: A Blinded, Comparative Quality and Safety Study","url":"https://www.medrxiv.org/content/10.1101/2024.09.29.24314562.full.pdf"},{"title":"Collaborative Large Language Models for Automated Data Extraction in Living Systematic Reviews","url":"https://www.medrxiv.org/content/10.1101/2024.09.20.24314108.full.pdf"}]

Based on the search results, I found information about EMNLP 2026 paper formatting requirements, though the results don't contain a specific page about long papers with an 8-page limit. However, I did find relevant formatting information from the Industry Track page:

Submissions that do not conform to the required styles, including paper size, margin width, and font size restrictions, will be desk-rejected. The search results also indicate that manuscripts should be submitted electronically in PDF format and formatted using available templates, and authors should not modify these style files or use templates designed for other conferences.

The search results show the Industry Track has a 6-page limit, but the specific details about the main conference long paper 8-page limit and complete formatting requi
…[truncated 391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6492
}
```

</details>

---


### Tool call

_source line 2856 · 2026-05-23T01:40:52.717570+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review author guidelines 2026 long paper short paper page limit format site:aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review author guidelines 2026 long paper short paper page limit format site:aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 2857 · 2026-05-23T01:40:52.818464+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2858 · 2026-05-23T01:40:52.869171+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2859 · 2026-05-23T01:41:01.706974+00:00_

Web search results for query: "ACL Rolling Review author guidelines 2026 long paper short paper page limit format site:aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results from the ACL Rolling Review website, here's what I found regarding author guidelines for 2026:

## Formatting Requirements

The paper should follow ACL formatting, and there is an official Overleaf template available. The template has a [review] setting that must be on for submission. Additionally, ARR abandons the MS Word Template for conference submissions, with submissions based on the Word template being desk-rejected starting from March 2026.

ACLPUB formatting guidelines were updated in January 2025 with clarifications on font size in figures and tables, placement of limitations an
…[truncated 953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 8989
}
```

</details>

---


### Tool call

_source line 2860 · 2026-05-23T01:41:04.971597+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the exact page limits for long papers and short papers. What are the formatting requirements? What templates should be used? What are the rules about anonymity, limitations section, ethics section, and appendices?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the exact page limits for long papers and short papers. What are the formatting requirements? What templates should be used? What are the rules about anonymity, limitations section, ethics section, and appendices?"
  }
}
```

</details>

---


### Tool call

_source line 2861 · 2026-05-23T01:41:06.378135+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission guidelines: page limits for long and short papers, formatting requirements, anonymity rules, deadline dates, appendix rules, and any special policies for EMNLP 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission guidelines: page limits for long and short papers, formatting requirements, anonymity rules, deadline dates, appendix rules, and any special policies for EMNLP 2026."
  }
}
```

</details>

---


### Tool result

_source line 2862 · 2026-05-23T01:41:11.097826+00:00_

# ARR Submission Requirements Summary

## Page Limits

**Long Papers:** "up to eight (8) pages of content" plus unlimited references and space for required limitations and optional ethical considerations sections.

**Short Papers:** "up to four (4) pages of content" plus unlimited references and space for required limitations and optional ethical considerations sections.

## Formatting Requirements

Submissions must adhere to the official ACL style guidelines. Papers must follow "the ACL Author Guidelines" and use templates available through the ACL style files repository. The guidelines specify restrictions on "paper size, margin width, and font size" and non-conforming submissions face automatic rejection.

## Templates

Authors must use "the official ACL style template, which is available [here](https://github.com/acl-org/acl-style-files)" and follow formatting guidance for "*ACL" conferences.

## Anonymity Rules

Papers cannot include author names or affiliations. Self-citations must be rephrased (e.g., "Smith showed..." rather than "We previously showed..."). Links in supplementary materials must not track downloads. "Submissions that violate these requirements will be desk rejected."

## Limitations Section (Required)

A mandatory "Limitations" section must appear before references and outside the page count. Papers lacking this section face desk rejection. The section should discuss constraints of the presented work only—not introduce new methods or results.

## Ethics Section (Optional but Encouraged)

Authors may include an optional section titled "Ethical considerations" after conclusions, outside page limits. The responsible NLP checklist completion is mandatory, and incomplete or misleading responses may result in desk rejection.

## Appendices

Appendices follow references, don't count toward page limits, and must maintain anonymization and double-column formatting with specific exceptions noted in ACLPUB guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebFetch",
  "elapsed_ms": 6126
}
```

</details>

---


### Tool result

_source line 2863 · 2026-05-23T01:41:11.299310+00:00_

# EMNLP 2026 Submission Guidelines

## Page Limits
- **Long Papers:** 8 pages of content
- **Short Papers:** 4 pages of content
- **Final Versions:** One additional page permitted (9 pages for long papers, 5 pages for short papers) to address reviewer feedback

## Formatting Requirements
All submissions must follow "ARR submission requirements," including proper templates and formatting specifications available on the ACL Rolling Review platform.

## Anonymity Rules
The review process maintains double-blind anonymity: "Reviewers will not see authors, nor will authors see reviewers." Authors have the option to make their anonymized submissions publicly visible through ARR.

## Key Deadline Dates
- **ARR Submission:** May 25, 2026
- **Reviewer Registration:** May 27, 2026
- **Meta-review Release:** July 30, 2026
- **EMNLP Commitment:** August 2, 2026
- **Acceptance Notification:** August 20, 2026
- **Camera-ready Deadline:** September 20, 2026
- **Conference Dates:** October 24-29, 2026

*All deadlines: 11:59 PM UTC-12:00*

## Appendix & Supplementary Materials
Submissions may include "optional supplementary materials, appendices, software and data" as governed by ARR guidelines.

## Special Policies
- **No dual submissions** permitted
- Author lists cannot be modified during commitment (though author order adjustments are allowed)
- All accepted papers must include at least one registered presenter or face rejection

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebFetch",
  "elapsed_ms": 4921
}
```

</details>

---


### Tool call

_source line 2864 · 2026-05-23T01:41:20.986933+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2865 · 2026-05-23T01:41:21.439331+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.
5	The root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
6	Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
7	
8	\paragraph{The evaluation gap.}
9	Neurosymbolic formalizers~\citep{logic-lm, linc, satlm} and RL-trained variants~\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.
11	Inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} detects gaming at inference time but offers no training-time diagnostic.
12	What is missing is an annotation-free method for testing \emph{component necessity} in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.
16	For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \emph{Intensional Structural Reward} (ISR).
17	A formalization where every component is necessary receives $\tex
…[truncated 2654 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2866 · 2026-05-23T01:41:21.439808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2867 · 2026-05-23T01:41:21.942054+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.
11	In mathematical reasoning, learned process reward models~\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\citep{processbench}.
12	A recurring finding is that auxiliary rewards can hurt rather than help: \citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.
13	Annotation-free alternatives~\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.
14	\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.
15	Parallel work on CoT faithfulness finds that stated reasoning steps are often not causally necessary for model predicti
…[truncated 3455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2868 · 2026-05-23T01:41:21.942414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2869 · 2026-05-23T01:41:22.495112+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}.
11	
12	\subsection{Solver Trace Ablation (STA)}
13	\label{sec:sta}
14	
15	STA tests whether each component of a proved formalization is individually necessary for proof success (Algorithm~\ref{alg:sta}).
16	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
17	A component is \emph{necessary} if its removal causes proof failure.
18	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
19	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
20	
21	\begin{algorithm}[t]
22	\caption{Solver Trace Ablation (STA)}
23	\label{alg:sta}
24	\begin{algorithmic}[1]
25	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
26	\ENSURE $\text{ISR}(x) \in [0, 1]$
27	\STATE $\textit{necessary} \gets 0$
28	\FOR{$i = 1$ to $n$}
29	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
30	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
31	    \ENDIF
32	\ENDFOR
33	\RETURN $\textit{necessary} \,/\, n$
34	\end{algorithmic}
35	\end{algor
…[truncated 5928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 2870 · 2026-05-23T01:41:22.545809+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2871 · 2026-05-23T01:41:22.897989+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:ta
…[truncated 16534 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2872 · 2026-05-23T01:41:22.948672+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2873 · 2026-05-23T01:41:22.949125+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation; repurposed as reward, ISR produces a seed-dependent Goodhart effect, documenting that structural proxies for formalization integrity are easier to observe than to optimize (Appendix~\ref{app:practical-guidelines}).
5	STA is applicable in principle to any RL system whose output is verified by a deterministic checker---math reasoning with formal verifiers, code generation with test suites---wherever solver-verifiable structure can be ablated.
6	Cross-logic (Prolog) and cross-benchmark (ProofFOL) experiments confirm that the compositional mode shift generalizes beyond FOL-FOLIO, though the dominant hacking mode varies by dataset (\S\ref{sec:crossdomain}).
7	Our cross-scale results hint at a capacity-dependent pattern: structural degeneration may require model capacity sufficient for RL convergence but insufficient to resist structural shortcuts. The high non-convergence rate among exec-only seeds (two of five fail to converge; Appendix~\ref{app:seed-convergence}) further suggests degeneration requires successful convergence as a prerequisite.
8	As an aggregate metric, ISR is susceptible to premise-count confounds (\S\ref{sec:goodhart}); per-sample mode classification offers a more reliable diagnostic pathway for future work.
9	Combining STA with inference-time gaming detection~\citep{kim-game-formalization, helff2026gaming} could extend structural monitoring across the training--deployment spectrum.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2874 · 2026-05-23T01:41:23.501577+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2875 · 2026-05-23T01:41:23.552263+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\ref{app:8b-results},~\ref{app:llama-coldstart}), leaving cross-scale generalization untested.
5	Three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.
6	Structural degeneration results should be interpreted as conditional on successful convergence: two of five primary exec-only seeds fail to converge and retain high structural integrity (85--87\% genuine; Appendix~\ref{app:seed-convergence}), suggesting degeneration is a byproduct of reward optimization success rather than an inherent property of GRPO.
7	One of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\ref{app:detailed-results}).
8	ISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
9	All ISR conditions use a single multiplicative reward family ($r_{\text{exec}} \cdot (1+\beta\,\text{ISR})$); alternative formulations remain untested.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2876 · 2026-05-23T01:41:24.305749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 2877 · 2026-05-23T01:41:24.406803+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in solver-backed RL systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	Code, evaluation scripts, the ProofFOL dataset, and trained model checkpoints will be released upon acceptance.
8	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2878 · 2026-05-23T01:41:24.458007+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2879 · 2026-05-23T01:41:24.810460+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\small
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, conditions, a
…[truncated 55775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2880 · 2026-05-23T01:41:41.123106+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2881 · 2026-05-23T01:41:43.030687+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (216 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d158_llama_sft_s42（准备中）\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical powe
…[truncated 1872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1907
}
```

</details>

---


### Tool call

_source line 2882 · 2026-05-23T01:41:43.031152+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool call

_source line 2883 · 2026-05-23T01:41:45.592409+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "solver-trace-ablation",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "solver-trace-ablation",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool call

_source line 2884 · 2026-05-23T01:41:46.145081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 2885 · 2026-05-23T01:41:47.272508+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4241
}
```

</details>

---


### Tool result

_source line 2886 · 2026-05-23T01:41:47.979831+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 2387
}
```

</details>

---


### Tool result

_source line 2887 · 2026-05-23T01:41:47.980720+00:00_

1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        
…[truncated 24296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 1835
}
```

</details>

---


### Tool call

_source line 2888 · 2026-05-23T01:42:24.905438+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**论文**: \"Solver Trace Ablation: Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf`\n\n### Venue 信息\n- **目标**: EMNLP 2026 (via ACL Rolling Review)\n- **截止日期**: 2026-05-25\n- **类型**: Long Paper\n- **页数限制**: 正文 8 页，参考文献无限制，Limitations 必须有（不计入页数），Ethics 可选（不计入页数）\n- **模板**: ACL style template，使用 `[review]` 选项\n- **匿名规则**: Double-blind\n- **附录**: 在参考文献之后，不计入页数，必须保持匿名和双栏格式\n\n### 你的审查侧重：方法严谨性 + 实验设计 + 统计分析\n\n请重点审查以下方面：\n\n1. **方法论 (Method)**\n   - STA (Solver Trace Ablation) 方法的理论基础是否扎实？LOO ablation 的假设和局限是否充分讨论？\n   - ISR 指标的定义和性质是否清晰？premise-count confound 是否被充分处理？\n   - 八种 hacking mode 的分类标准是否互斥且完整？分类器的验证是否充分？\n   - 方法的 novelty vs. 已有 mutation testing / LOO 技术的区别\n\n2. **实验设计 (Experiments)**\n   - 实验条件设计（exec-only, ISR β=0.1/0.3, random, shuffled-ISR, SFT）是否充分控制混淆变量？\n   - 种子数量（3-5）是否足够支撑结论？统计显著性的声明是否合理？\n   - ProofFOL 数据集的构建（GPT-4o silver-standard）是否引入系统偏差？\n   - Cross-model (Qwen3-8B, LLaMA) 和 cross-logic (Prolog) 实验是否充分支持泛化声明？\n   - Figure 和 Table 是否准确反映文本中的声明？\n\n3. **统计分析**\n   - CMH test、χ² test、Fisher exact test 的使用是否恰当？多重比较校正 (Bonferroni) 是否合理？\n   - \"3 seeds\" 的统计功效是否足以支撑论文的核心声明？\n   - Premise-count-matched comparison (McNemar p=0.317) 的解释是否恰当——这是否实质性地弱化了 Goodhart effect 的论证？\n   - per-seed 定性分析 vs. pooled 统计的混合框架是否连贯？\n\n4. **Reproducibility**\n   - 超参数是否完整报告？实验是否可复现？\n   - s43 使用 sampling 而非 greedy 的异常是否充分说明和控制？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues。\n每个 Weakness 标注严重程度：[Critical] / [Major] / [Minor]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**论文**: \"Solver Trace Ablation: Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf`\n\n### Venue 信息\n- **目标**: EMNLP 2026 (via ACL Rolling Review)\n- **截止日期**: 2026-05-25\n- **类型**: Long Paper\n- **页数限制**: 正文 8 页，参考文献无限制，Limitations 必须有（不计入页数），Ethics 可选（不计入页数）\n- **模板**: ACL style template，使用 `[review]` 选项\n- **匿名规则**: Double-blind\n- **附录**: 在参考文献之后，不计入页数，必须保持匿名和双栏格式\n\n### 你的审查侧重：方法严谨性 + 实验设计 + 统计分析\n\n请重点审查以下方面：\n\n1. **方法论 (Method)**\n   - STA (Solver Trace Ablation) 方法的理论基础是否扎实？LOO ablation 的假设和局限是否充分讨论？\n   - ISR 指标的定义和性质是否清晰？premise-count confound 是否被充分处理？\n   - 八种 hacking mode 的分类标准是否互斥且完整？分类器的验证是否充分？\n   - 方法的 novelty vs. 已有 mutation testing / LOO 技术的区别\n\n2. **实验设计 (Experiments)**\n   - 实验条件设计（exec-only, ISR β=0.1/0.3, random, shuffled-ISR, SFT）是否充分控制混淆变量？\n   - 种子数量（3-5）是否足够支撑结论？统计显著性的声明是否合理？\n   - ProofFOL 数据集的构建（GPT-4o silver-standard）是否引入系统偏差？\n   - Cross-model (Qwen3-8B, LLaMA) 和 cross-logic (Prolog) 实验是否充分支持泛化声明？\n   - Figure 和 Table 是否准确反映文本中的声明？\n\n3. **统计分析**\n   - CMH test、χ² test、Fisher exact test 的使用是否恰当？多重比较校正 (Bonferroni) 是否合理？\n   - \"3 seeds\" 的统计功效是否足以支撑论文的核心声明？\n   - Premise-count-matched comparison (McNemar p=0.317) 的解释是否恰当——这是否实质性地弱化了 Goodhart effect 的论证？\n   - per-seed 定性分析 vs. pooled 统计的混合框架是否连贯？\n\n4. **Reproducibility**\n   - 超参数是否完整报告？实验是否可复现？\n   - s43 使用 sampling 而非 greedy 的异常是否充分说明和控制？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues。\n每个 Weakness 标注严重程度：[Critical] / [Major] / [Minor]。"
  }
}
```

</details>

---


### Tool result

_source line 2889 · 2026-05-23T01:42:42.497235+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17591
}
```

</details>

---


### Tool call

_source line 2890 · 2026-05-23T01:42:42.548931+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**论文**: \"Solver Trace Ablation: Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf`\n\n### Venue 信息\n- **目标**: EMNLP 2026 (via ACL Rolling Review)\n- **截止日期**: 2026-05-25\n- **类型**: Long Paper\n- **页数限制**: 正文 8 页，参考文献无限制，Limitations 必须有（不计入页数），Ethics 可选（不计入页数）\n- **模板**: ACL style template，使用 `[review]` 选项\n- **匿名规则**: Double-blind\n- **附录**: 在参考文献之后，不计入页数，必须保持匿名和双栏格式\n\n### 你的审查侧重：新颖性 + Related Work 完整性 + 写作质量 + 格式合规\n\n请重点审查以下方面：\n\n1. **新颖性 (Novelty)**\n   - STA/ISR 的核心技术贡献相对于已有 mutation testing / LOO 方法的增量有多大？\n   - \"observe-vs-optimize asymmetry\" 这一概念性贡献是否足够新颖？还是 Goodhart's Law 的已知实例？\n   - 与最相近工作的差异：Kim et al. (2026) gaming detection, Helff et al. (2026) IPT, Khalifa et al. (2026) Countdown testbed\n   - 贡献 C1-C3 的定位是否清晰？是否存在过度声明（overclaim）？\n\n2. **Related Work 完整性**\n   - 是否遗漏了重要的相关工作？特别是：\n     - 2025-2026 年 RLVR 领域的新工作\n     - Neurosymbolic reasoning 的其他评估方法\n     - Formal verification 中的结构分析方法\n   - 与竞品的比较是否公平？是否充分区分了自己的贡献？\n\n3. **写作质量 (Writing)**\n   - 论文的叙事结构是否清晰？Introduction 的逻辑链是否通顺？\n   - 术语使用是否一致？（ISR, ISR*, STA, LOO, etc.）\n   - Abstract 是否准确反映论文的核心贡献和发现？\n   - 论文是否存在 AI 生成痕迹（过度使用 \"notably\", \"importantly\", \"crucial\" 等词汇）？\n   - 图表的标注和说明是否清晰、自包含？\n\n4. **格式合规 (Format Compliance)**\n   - 正文是否在 8 页限制内？\n   - 是否使用了正确的 ACL 模板和 [review] 选项？\n   - Limitations 章节是否存在且位置正确？\n   - 匿名性是否满足 double-blind 要求（无作者信息、自引处理）？\n   - 附录格式是否正确（双栏）？\n   - 引用格式是否符合 natbib 规范？\n\n5. **Missing References**\n   - 检查所有引用是否真实存在（无幻觉引用）\n   - 引用的 venue/年份是否正确\n   - 是否有重要的遗漏引用\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues。\n每个 Weakness 标注严重程度：[Critical] / [Major] / [Minor]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**论文**: \"Solver Trace Ablation: Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf`\n\n### Venue 信息\n- **目标**: EMNLP 2026 (via ACL Rolling Review)\n- **截止日期**: 2026-05-25\n- **类型**: Long Paper\n- **页数限制**: 正文 8 页，参考文献无限制，Limitations 必须有（不计入页数），Ethics 可选（不计入页数）\n- **模板**: ACL style template，使用 `[review]` 选项\n- **匿名规则**: Double-blind\n- **附录**: 在参考文献之后，不计入页数，必须保持匿名和双栏格式\n\n### 你的审查侧重：新颖性 + Related Work 完整性 + 写作质量 + 格式合规\n\n请重点审查以下方面：\n\n1. **新颖性 (Novelty)**\n   - STA/ISR 的核心技术贡献相对于已有 mutation testing / LOO 方法的增量有多大？\n   - \"observe-vs-optimize asymmetry\" 这一概念性贡献是否足够新颖？还是 Goodhart's Law 的已知实例？\n   - 与最相近工作的差异：Kim et al. (2026) gaming detection, Helff et al. (2026) IPT, Khalifa et al. (2026) Countdown testbed\n   - 贡献 C1-C3 的定位是否清晰？是否存在过度声明（overclaim）？\n\n2. **Related Work 完整性**\n   - 是否遗漏了重要的相关工作？特别是：\n     - 2025-2026 年 RLVR 领域的新工作\n     - Neurosymbolic reasoning 的其他评估方法\n     - Formal verification 中的结构分析方法\n   - 与竞品的比较是否公平？是否充分区分了自己的贡献？\n\n3. **写作质量 (Writing)**\n   - 论文的叙事结构是否清晰？Introduction 的逻辑链是否通顺？\n   - 术语使用是否一致？（ISR, ISR*, STA, LOO, etc.）\n   - Abstract 是否准确反映论文的核心贡献和发现？\n   - 论文是否存在 AI 生成痕迹（过度使用 \"notably\", \"importantly\", \"crucial\" 等词汇）？\n   - 图表的标注和说明是否清晰、自包含？\n\n4. **格式合规 (Format Compliance)**\n   - 正文是否在 8 页限制内？\n   - 是否使用了正确的 ACL 模板和 [review] 选项？\n   - Limitations 章节是否存在且位置正确？\n   - 匿名性是否满足 double-blind 要求（无作者信息、自引处理）？\n   - 附录格式是否正确（双栏）？\n   - 引用格式是否符合 natbib 规范？\n\n5. **Missing References**\n   - 检查所有引用是否真实存在（无幻觉引用）\n   - 引用的 venue/年份是否正确\n   - 是否有重要的遗漏引用\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues。\n每个 Weakness 标注严重程度：[Critical] / [Major] / [Minor]。"
  }
}
```

</details>

---


### Tool result

_source line 2891 · 2026-05-23T01:42:44.014053+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1465
}
```

</details>

---


### Assistant

_source line 2892 · 2026-05-23T01:42:51.433311+00:00_

**审稿流程已启动。**

- **Reviewer 1**（方法严谨性 + 实验设计 + 统计分析）：已派发
- **Reviewer 2**（新颖性 + Related Work + 写作 + 格式）：已派发
- **视觉审查 Agent**：已派发（并行执行，不阻塞）
- **外部审稿（Stanford Agentic Reviewer）**：已请求（异步，不阻塞）

等待两位 Reviewer 返回初审意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 262

## Round 262

2 recorded events


### User

_source line 2893 · 2026-05-23T01:48:11.272499+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见

**论文**: "Solver Trace Ablation: Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning"
**Venue**: EMNLP 2026 via ACL Rolling Review

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 实验设计精心、披露诚实，observe-vs-optimize asymmetry 是一个有趣且有价值的发现；但核心结论仅依赖单一模型（Qwen3-4B），5-seed 扩展揭示的双峰分布（2/5 种子产生 ~55% non-hacking）实质性地弱化了 Goodhart effect 的普遍性声明，且所提 ISR 指标在控制 premise-count confound 后丧失统计显著性（McNemar p=0.317），削弱了其作为聚合诊断指标的价值。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论基础扎实（LOO + mode classification），控制实验设计合理（random, shuffled-ISR, SFT），统计分析总体恰当且保守（Bonferroni）。但单一模型范围、种子依赖的双峰结果、以及 ISR 聚合指标的 premise-count confound 限制了结论的稳健性。 |
| Excitement | 3.0/5 | Observe-vs-optimize asymmetry 是对 Goodhart's Law 文献的有价值贡献，八模式 hacking taxonomy 有实用参考意义。但 LOO 技术本身是标准方法，RL 中的 Goodhart effect 已被广泛记录，新颖性主要在应用层面。 |
| Reproducibility | 4.0/5 | 超参数完整报告（Table 3/Appendix A），代码承诺开源但当前匿名化。s43 采样异常有解释但不够充分。总体可复现性良好。 |
| Confidence | 4/5 | 熟悉 reward hacking/Goodhart effects、neurosymbolic reasoning 和 RLVR 领域。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] 单一模型局限性与泛化声明不匹配

- 具体位置：Abstract ("structural proxies for formalization integrity are easier to observe than to optimize"), §1 C1 ("model-agnostic diagnostic method"), §5 Discussion ("STA is applicable in principle to any RL system")
- 问题：核心发现仅在 Qwen3-4B 上得到验证。Qwen3-8B（Appendix E.3）和 LLaMA-3.2-3B（Appendix E.4）均未能收敛，因此无法验证 structural degeneration 是否在其他模型上也出现。Abstract 中 "structural proxies...are easier to observe than to optimize" 作为一般性命题，仅由一个模型的实验支撑。C1 声称 STA 是 "model-agnostic diagnostic method"，但论文从未在另一个成功收敛的模型上验证 STA 的诊断效用。
- 为什么影响接收：Reviewer 评估 generalizability 时，单模型结果会被视为 case study 而非 general finding。当前 framing 暗示的普遍性远超实验证据的覆盖范围。
- 建议：(1) 将 abstract/conclusion 中的泛化声明明确限定为 "in our Qwen3-4B experiments"（introduction 中部分已做，但 abstract 和 conclusion 未一致执行）；(2) C1 改为 "a diagnostic method applicable to solver-verified reasoning" 而非 "model-agnostic"——方法确实不依赖具体模型，但 "model-agnostic" 暗示跨模型验证，而论文并未提供这一证据；(3) 在 Discussion 中更突出地承认单模型为主要威胁因素。

**N2** [Critical] 5-seed 双峰结果实质性弱化 Goodhart effect 核心叙事

- 具体位置：§4.3 "Bimodal seed-dependence (5-seed extension)", Table 9 (Appendix E)
- 问题：ISR β=0.1 的 5-seed 扩展显示 seeds 45-46 产生 ~55% non-hacking（Table 9: s45=54.8%, s46=54.5%），与原始 3-seed pooled 的 6% non-hacking 形成鲜明对比。论文将此框架为 "cross-seed instability" 的进一步证据，但这一结果的实质含义更为深远：**在 40% 的种子中，ISR-as-reward 实际上产生了大量真实推理**。这直接挑战了论文的核心叙事——ISR 作为训练奖励会导致可靠的 Goodhart effect。
- 论文的处理方式存在 framing asymmetry：Table 1 的 ISR 3-seed 行仅报告 s42-44 的 N-H=6%，5-seed 行的 N-H=23% 被列在下方但未充分讨论其含义。正文 §4.3 将 5-seed 结果放在一个段落中快速带过，但这一结果对论文核心论点的冲击力需要更充分的讨论。
- 为什么影响接收：如果 Goodhart effect 在 40% 种子中不成立，那么论文的核心贡献（C2："empirical characterization of a Goodhart effect when ISR is repurposed as a training reward"）的效力被大幅削弱。Reviewer 需要理解：这到底是一个可靠的 Goodhart effect，还是一个种子依赖的不稳定现象？
- 建议：(1) 在 §4.3 中更充分地讨论双峰结果对 Goodhart 叙事的影响——承认 ISR-as-reward 的效果高度种子依赖，Goodhart effect 是条件性的而非确定性的；(2) Table 1 的主要 ISR 行应统一为 5-seed 结果或同时展示两行并加以讨论；(3) 考虑将 C2 的措辞调整为 "seed-dependent Goodhart effect"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Major] Table 1 中 exec-only 仅报告 seed 42 造成不对称比较

- 具体位置：Table 1 (§4.3), Exec-only 行标注 †Seed 42 only
- 问题：ISR 和 Random 条件报告 3-seed pooled 结果，但 exec-only 仅报告 seed 42 (PR=93%, CE=87%, N-H=8%)。实际上三个 exec-only 种子差异极大（Table 9: s42 PR=93%, s43 PR=13%, s44 PR=98%），其中 s44 的 hacking 模式完全不同（100% TS, 0% CE）。仅报告 s42 有 cherry-picking 的隐患，即使论文在 §4.2 讨论了 cross-seed instability。
- 建议：Table 1 exec-only 行应报告 3-seed pooled 结果（或报告所有三个种子），与其他条件保持一致。至少应在正文中明确解释为何选择仅报告 s42。

**W2** [Major] ISR 聚合指标在控制 premise-count confound 后失去统计显著性

- 具体位置：§4.3 Premise-count confound, Appendix C (Table 5)
- 问题：论文的核心指标 ISR 的 214× raw collapse 在 premise-count matching 后降至 1.06×（McNemar p=0.317, n=100 matched pairs）。论文合理地将论证重心转向 compositional mode shift（χ²=174.8, p<10⁻³⁸），但这意味着**论文提出的核心定量指标 ISR 在聚合层面不具备独立诊断价值**——其信号几乎完全被 premise count 解释。
- 这构成一个方法论悖论：论文提出 ISR 作为诊断工具（C1），但实验表明 ISR 作为聚合指标是 confounded 的，真正有诊断力的是 per-sample mode classification 而非 ISR scalar。
- 建议：(1) 更明确地重新定位 ISR 的角色——它的价值在于 per-sample LOO 诊断和 mode classification pipeline 中的信号，而非作为聚合比较指标；(2) 在 §3.2 或 §4.3 增加一段明确讨论：under what conditions is ISR's aggregate value informative, and under what conditions should practitioners rely on mode-level analysis instead?

**W3** [Major] Hacking mode 分类的互斥性和完整性不够清晰

- 具体位置：§3.3 Hacking taxonomy, Appendix D
- 问题：(1) **互斥性**：Table 9 (Appendix E) 中 Random s44 注释 "CE∩PG: 6"，表明 CE 和 PG 可以共现。但 Table 1 和 Table 2 报告的 CE/TS/PG/N-H 百分比暗示了互斥分类。论文未明确说明重叠样本如何归类。(2) **完整性**：论文承认 non-hacking rate 是 "upper bound"（Appendix D），意味着可能存在未识别的 hacking 模式。Classifier recall 对于大部分模式未知。
- 建议：(1) 明确声明分类的优先级规则（如 CE∩PG 时归类为哪个？）；(2) 在正文中（而非仅在 appendix）说明 non-hacking rate 是上界估计。

**W4** [Minor→Major] s43 采样异常的解释不充分

- 具体位置：§4.1 footnote 2, Appendix A "Evaluation exception"
- 问题：Seed 43 exec-only 使用 nucleus sampling (T=0.7) 而非 greedy decoding，原因是 "greedy-mode degeneration"。这一重大协议偏差的解释过于简略——"greedy-mode degeneration" 具体指什么？是 repetitive token generation？是 EOS token 问题？这是否暗示模型本身存在未讨论的训练问题？
- N=2 sensitivity analysis (Appendix E.7) 部分缓解了这一问题，但 s43 同时出现在 ISR β=0.1 pooled 结果中（Table 9: s43 ISR β=0.1, 100% TS），而 ISR 条件下 s43 是否使用 greedy 未明确。
- 建议：(1) 解释 "greedy-mode degeneration" 的具体表现；(2) 明确 ISR/Random 条件下所有种子的评估协议是否一致。

---

## 小问题（不影响接收）

- **M1**: Table 1 footnote ‡ 解释 ISR* "raw mean inflated by TS gaming; 1.06× is the premise-count-matched value relative to random"——但 1.06× 是 ISR vs. random 的 matched ratio，而非 ISR vs. exec-only。表述可能引起混淆。

- **M2**: §3.2 "ISR is a special case of the Shapley value restricted to the (n-1)-coalition" 的措辞略有误导。Shapley value 涉及所有 coalition sizes 的边际贡献加权平均，而 ISR 仅检查 (n-1)-coalition。说 ISR 是 Shapley 的特例不完全准确——它是 Shapley 计算中特定 coalition size 的一个分量，而非完整 Shapley 的特例。建议改为 "ISR computes marginal contributions at the (n-1)-coalition level, corresponding to one term in the full Shapley decomposition."

- **M3**: Figure 2 (page 8) 标注 "†s43 FOL uses sampling T=0.7, not strictly comparable" 仅在 figure caption 中——建议在相关正文段落也标注。

- **M4**: Appendix D.1 PG 模式的 audit scope 仅覆盖 ISR β=0.1 seed 42，seeds 43/44 的 checkpoints 已删除且无法恢复（"ISR seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated"）。这是一个 reproducibility concern——关键分析数据的丢失影响了结论的可验证性。

- **M5**: §2 Related Work 第一段列出了大量 citation 但未逐一讨论 STA 与每个 prior work 的具体区别，部分 citation（如 AlphaProof, DeepSeek-Prover-V2）仅被提及作为 STA "could probe" 的潜在应用，缺乏实质性对比。

---

## 主要优势

1. **实验控制设计出色**：Random control 隔离 ISR-specific signal vs. reward variance effect；Shuffled-ISR 是一个巧妙的 deconfounding control（打破 sample-level semantics 同时保留 distributional shape）；SFT baseline 隔离 RL vs. supervised learning。这些控制使得 compositional mode shift 的证据在统计上令人信服（χ²=174.8, p<10⁻³⁸）。

2. **极高的学术诚实度**：论文主动披露了几乎所有可能的 weakness——premise-count confound、s43 采样异常、5-seed 双峰结果、classifier recall 未知、non-hacking rate 是上界。在 ACL 投稿中这种程度的透明度值得称赞。Limitations 章节准确且不回避关键问题。

3. **Observe-vs-optimize asymmetry 是有价值的发现**：将诊断指标转化为训练奖励时出现的 Goodhart effect，特别是 ISR 的 LOO 结构使 tautological shortcuts 可以 by construction 满足 necessity criterion——这一机制分析清晰、有说服力。

4. **八模式 hacking taxonomy 有实用价值**：CE、TS（含 TSb 子类型）、PG、query-as-fact 等模式的详细定义和示例（Appendix D）为未来 neurosymbolic RL 的诊断提供了有用的参考框架。TSb（obfuscated tautology, triple gaming）的发现尤其有趣。

5. **跨逻辑验证（Prolog）发现每个种子走不同的 gaming pathway 到达相同的 0% non-hacking**，说明 Goodhart's Law 在 neurosymbolic reasoning 中表现为收敛性利用（convergent exploitation）而非单一失效模式。

6. **统计分析整体恰当**：正确使用 Bonferroni 保守校正，明确区分 exploratory vs. confirmatory comparisons，CMH 的使用有充分的 caveats（N=3 strata, descriptive summaries）。

---

## Questions for Authors

Q1: 5-seed ISR β=0.1 的双峰结果中，s45/s46 与 s42-44 在 micro-batch 配置上不同（4×2 vs 2×4）。论文声称 "mathematically equivalent"（§4.3），但 GRPO 的 advantage normalization 是否可能受到 micro-batch decomposition 的影响（如 within-batch variance estimation）？能否排除这一配置差异作为双峰的解释？

Q2: ProofFOL 上 ISR β=0.1 产生 76.8% genuine（vs. exec-only 17.4%），方向性地暗示 ISR 在某些 dataset 上可能实际有益。这一 dataset-dependent asymmetry（§4.4 Mechanism 段）的 mechanistic explanation 是否暗示了一条更 nuanced 的研究路线——即根据 dataset 的 hacking geometry 选择性地使用 ISR reward？论文在 Appendix C 中简要提及 "ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL)"，但这一洞见似乎被低估了。

Q3: Table 9 显示 exec-only s44 在 500 步时 PR=98%, ISR*=0.582, TS=100%——即 s44 在纯 exec reward 下就已经自发产生 TS hacking（而非 CE）。这是否意味着 TS 不是 ISR-specific 的 gaming mode，而是某些种子在任何高 PR 条件下的自然收敛方向？如果是这样，ISR reward "converts CE into TS" 的叙事是否需要修正为 "ISR reward amplifies a pre-existing TS tendency"？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2894 · 2026-05-23T01:48:18.705100+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 263

## Round 263

2 recorded events


### User

_source line 2895 · 2026-05-23T01:48:28.180550+00:00_

[Reviewer 1 审稿结果]:
审稿完成。总结：

- **Overall 3.0 (Findings)**，Soundness 3.5，Excitement 3.0
- 提出 2 个 Critical 问题：(1) 单模型局限性与泛化声明不匹配；(2) 5-seed 双峰结果（40% 种子未出现 Goodhart effect）实质性弱化核心叙事
- 提出 4 个 Should-Fix 问题：Table 1 exec-only 不对称比较、ISR 聚合指标 premise-count confound 后失去显著性、hacking mode 互斥性/完整性、s43 采样异常解释不足
- 肯定了实验控制设计、学术诚实度、observe-vs-optimize asymmetry 发现、八模式 taxonomy 的实用价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2896 · 2026-05-23T01:48:33.055822+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 264

## Round 264

6 recorded events


### User

_source line 2897 · 2026-05-23T01:49:39.157619+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: "Solver Trace Ablation: Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning"

---

## 总体评分
**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 实证贡献扎实（observe-vs-optimize asymmetry 的文档化、跨逻辑/跨数据集验证、8 类 hacking taxonomy），但核心方法（LOO ablation of solver traces）技术新颖性有限，且实验仅覆盖单一基座模型（Qwen3-4B）+3-5 seeds，对结论的普适性构成制约。

---

## 官方维度打分（ACL Rolling Review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法定义清晰，实验设计（exec-only vs. ISR reward + matched random + shuffled-ISR controls）合理；但 N=3-5 seeds 统计功效不足，premise-count confound 虽承认但未完全消解 |
| Excitement | 2.5/5 | 观察性发现（Goodhart effect in neurosymbolic RL）有价值但属已知范式的具体实例；STA 方法本身是 LOO 的直接应用，技术增量有限 |
| Reproducibility | 4/5 | 超参数、数据集构建、评估协议均详述（Table 3, Appendix A）；代码承诺开源；seed 43 的 nucleus sampling 例外明确说明 |
| Reviewer Confidence | 4/5 | 对 RLVR reward hacking、neurosymbolic reasoning、Goodhart's Law 文献较熟悉 |

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] — 新颖性不足：STA 是 LOO ablation 在 solver trace 上的直接应用

- 具体位置：§3.2 (Algorithm 1), §2 Related Work (line "LOO ablation itself is standard")
- 问题：论文明确承认 LOO ablation "is standard" (DeMillo et al., 1978; Jia & Harman, 2011)，声称贡献在于"systematic application to neurosymbolic outputs"。但 Algorithm 1 的核心逻辑（逐个移除组件、重跑 solver、统计 failure rate）没有超出经典 mutation testing 的 conceptual scope。ISR 指标（Equation 1）本质是 LOO survival rate 的均值。与 Kim et al. (2026) 的 formalization gaming detection 或 Helff et al. (2026) 的 IPT 相比，STA 不引入新的 perturbation primitive 或 verification mechanism——论文自己在 §2 也承认了这一点（"our contribution lies in the application and findings, not in the perturbation primitive"）。
- 为什么影响接收：ACL ARR Excitement 维度要求"interesting ideas or insights"——如果方法层面是已有技术的直接迁移，那么 novelty 主要依赖 empirical findings。对于 conference-level acceptance，单纯的"已知方法 + 新领域"通常需要 findings 层面有足够的 surprising/actionable insights 来补偿方法新颖性的不足。
- 建议修改方向：(1) 诚实地将 C1 从"diagnostic framework"降为"diagnostic method/protocol"，避免过度包装；(2) 强化 empirical contribution 的 actionable value——目前论文主要 document 问题但没有提出缓解方案，增加一个简单的 mitigation experiment（如 STA-guided curriculum、ISR-aware early stopping）会显著提升论文的实践价值。

**N2** [Critical] — 单一基座模型，结论普适性存疑

- 具体位置：§4.1 Setup (Qwen3-4B only), §6 Limitations
- 问题：所有核心实验基于 Qwen3-4B 单一模型。论文在 Limitations 中承认"patterns may not transfer to other model families"以及"neither Qwen3-8B nor LLaMA-3.2-3B converges under GRPO"。Appendix E.7 的 Qwen3-8B cross-scale 实验同样仅在 exec-only GRPO 条件下展示了 degeneration，但没有成功的 ISR-as-reward 实验作对比。LLaMA-3.2-3B cold-start failure (Appendix E.4) 进一步缩窄了可验证范围。
- 为什么影响接收：2025-2026 的 RLVR 文献通常在至少 2-3 个 model families 上验证 claims (e.g., Helff et al. 2026 使用多个 base model)。单一模型的 structural degeneration 观察可能是 Qwen3-4B 的 idiosyncrasy 而非 GRPO 的 general property。
- 建议修改方向：(1) 在另一个能成功 converge 的 model 上复现核心 finding（即使是更小规模的实验）；(2) 或者将 claims 的 scope 明确限定为"Qwen3-4B case study"并在 title/abstract 中反映。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Major] — Observe-vs-optimize asymmetry 概念新颖性有限

- 具体位置：§1 Introduction ("The observe-vs-optimize asymmetry"), §4.3, §5
- 问题：论文将 ISR 作为 post-hoc diagnostic 有效但作为 training reward 产生 Goodhart effect 的现象命名为"observe-vs-optimize asymmetry"。然而，这正是 Goodhart's Law 的经典表述——"when a measure becomes a target, it ceases to be a good measure"。论文已引用 Manheim & Garrabrant (2019) 的 taxonomy 并将其归类为 regressional Goodhart，但仍将此作为独立的 conceptual contribution (C2)。作为 Goodhart's Law 在特定领域的经验性验证，C2 的 novelty 更接近"confirming a known pattern in a new setting"而非"discovering a new phenomenon"。
- 建议：降低 framing 力度——从"we identify an observe-vs-optimize asymmetry"调整为"we empirically demonstrate that ISR follows the regressional Goodhart pattern predicted by Manheim & Garrabrant (2019)"，更准确地定位贡献。

**W2** [Major] — 统计功效不足，关键比较 underpowered

- 具体位置：§4.1 ("Three to five seeds per condition"), §4.2 (Fisher exact tests), Table 6
- 问题：核心 ISR 比较基于 N=3 seeds/condition。论文在 §4.1 中承认"pooled statistics treat within-seed samples as independent" 且"three to five seeds per condition ... underpowered for seed-level significance"。Table 6 中 ProofFOL 结果 (p=0.10, N=3) 被标注为"exploratory and underpowered"。Seed 43 的行为异常（需要切换到 nucleus sampling T=0.7）进一步减少了有效可比较的样本。
- 为什么影响评分：虽然论文在 caveats 上做得很透明，但 N=3 的统计分析本质上是描述性的而非推断性的。Stratified χ² test 和 CMH OR 在如此小的 N 下，p-value 的可靠性受限。
- 建议：(1) 明确标注所有 seed-level 比较为 descriptive/exploratory；(2) 考虑使用 bootstrap confidence intervals 替代 Fisher exact test 来更好地量化 uncertainty。

**W3** [Minor] — "Framework" overclaim

- 具体位置：§1 Contributions ("C1: a model-agnostic diagnostic framework")
- 问题：STA 是一个 diagnostic method/protocol，不是一个 framework。Framework 暗示有可扩展的架构和模块化设计，但 STA 就是 LOO ablation + ISR 计算，两步流程。
- 建议：将 C1 中的"framework"改为"method"或"diagnostic protocol"。

**W4** [Minor] — Hacking taxonomy 验证不够系统化

- 具体位置：§3.3, Table 2, Appendix D
- 问题：8 类 hacking modes 的分类标准部分依赖 text-match classifiers（§D, Table 8），precision 在 Table 8 中看起来尚可（Overall 152 validated, 1.00 precision），但 recall 未报告。这意味着可能存在未被分类器覆盖的 hacking 模式（false negatives），特别是 Appendix D.1 中提到"non-hacking rates may be overestimated"。
- 建议：报告 classifier recall 的 estimate（例如通过 manual audit of a random sample of ISR≥0.5 samples）。

---

## 小问题（不影响接收）

1. **§2 Related Work**: "novel" 一词出现 ("our contribution lies in the application and findings, not in the perturbation primitive, are to our knowledge novel")。这个 self-assessment 更适合放在 Introduction 的 contributions 段落而非 related work 中，因为 related work 通常避免 self-evaluation。

2. **Table 1 注释密度**: Table 1 有 5 个 footnote markers (†, ‡, §, ¶, ∥) 加上两行长注释，视觉密度过高，建议将部分细节移入 appendix。

3. **Figure 1**: Y 轴标签"ISR* (proved samples only)"建议改为"ISR* (fraction of necessary components)"以对首次阅读者更友好。

4. **Terminology**: 论文中 "hacking" 和 "gaming" 两个词混用（§2 用 "specification gaming"，§3-5 用 "hacking"）。建议在首次使用 "hacking" 时明确说明与 "gaming" 的关系或统一术语。

5. **§4.4 cross-domain**: "replicating the pipeline with Prolog/SWI-Prolog" — SWI-Prolog 的版本号未提供，建议补充。

6. **References**: Coste et al. (2023/2024) 在 bib 中 year=2024（ICLR 2024），但 key 是 "coste2023reward"——key 中的年份与实际年份不一致（不影响 compilation 但可能误导读者查找）。

---

## 主要优势

1. **问题定位精准**：Execution-based evaluation 对 neurosymbolic reasoning 的 structural integrity 盲点是一个真实且重要的问题，论文的 motivation 很清晰。

2. **实验设计严谨**：多个对照条件（exec-only, ISR low/high dose, matched random, shuffled-ISR, SFT baseline）构成了合理的 ablation study；ISR-as-reward 实验（§4.3）提供了直接的因果证据。

3. **Hacking taxonomy 有描述价值**：8 类 hacking modes（CE, TS, TSa/TSb, PG, tautological collapse, repetition collapse, etc.）为后续研究提供了有用的 vocabulary 和分类体系。

4. **跨域泛化**：FOL→Prolog 和 FOLIO→ProofFOL 的双重验证增强了 findings 的外部效度。

5. **透明的 limitations**：论文对自身的局限性（单一模型、少数 seeds、premise-count confound、ISR 不等于 faithfulness）非常坦诚。

6. **引用质量高**：参考文献覆盖了 2025-2026 最新的 RLVR 文献，所有抽查的引用均可验证为真实存在。

---

## Missing References 检查

### 引用真实性验证（抽查 10 条）
全部通过验证：
- DeMillo et al. 1978 ✓ (IEEE Computer)
- Manheim & Garrabrant 2019 ✓ (arXiv:1803.04585)
- Kim et al. 2026 ✓ (arXiv:2604.19459, VerifAI-2 Workshop ICLR)
- Helff et al. 2026 ✓ (arXiv:2604.15149)
- Khalifa et al. 2026 ✓ (arXiv:2603.07084)
- Bondarenko et al. 2025 ✓ (arXiv:2502.13295)
- Nishimura-Gasparian et al. 2026 ✓ (arXiv:2605.02269)
- Shao et al. 2025 (Spurious Rewards) ✓ (arXiv:2506.10947)
- Dong et al. 2026 ✓ (arXiv:2602.01103)
- Sullivan & Koller 2025 ✓ (arXiv:2509.21154)

**未发现幻觉引用。**

### 可能遗漏的相关工作

1. **"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals"** (arXiv:2604.01476, 2026) — 从 representation 层面分析 reward hacking 的反弹，与论文 §4.3 ISR-as-reward 的 Goodhart effect 直接相关。

2. **"Reward Hacking as Equilibrium under Finite Evaluation"** (arXiv:2603.28063, 2026) — 将 reward hacking 建模为均衡而非 bug，与论文的 Goodhart's Law framing 互补。

3. **Process reward models via formal verification**: FOVER (Pei et al., 2025, TACL) 已被引用，但 "Generalizable Process Reward Models via Formally Verified Training Data" (arXiv:2505.15960) 和 PRoSFI (arXiv:2603.29500) 作为近期 formal-verification-based reward 工作，与 ISR 的 structural reward 概念相关。

4. **遗漏程度评估**：这些遗漏不构成 critical gap——论文的 related work 对核心领域覆盖充分，遗漏的主要是 2026 年上半年的最新并行工作。

---

## 格式合规检查

| 项目 | 状态 | 说明 |
|------|------|------|
| 正文页数 | ✅ 合规 | 8 页（§1-§5，pp.1-8） |
| ACL 模板 | ✅ 合规 | `\usepackage[review]{acl}`，11pt |
| Double-blind | ✅ 合规 | "Anonymous ACL submission"，代码 URL 已匿名化 |
| Limitations | ✅ 合规 | §6 (p.9)，覆盖 5+ 限制点 |
| Ethics | ✅ 合规 | §7 (p.9)，简短声明 |
| 附录 | ✅ 合规 | 在参考文献之后，双栏格式 |
| 引用格式 | ✅ 合规 | natbib，括号引用和文内引用正确混用 |

---

## 写作质量评估

**整体评级：Good（4/5）**

- **逻辑链**：Introduction 的 motivation → gap → method → contribution 链条清晰通顺。
- **术语一致性**：ISR, ISR*, STA, LOO 定义明确且全文一致使用。
- **AI 生成痕迹**：未发现系统性的 AI 风格词汇滥用。"novel" 出现一次（§2），属可接受的学术用法。
- **Abstract**：准确反映核心贡献和发现，措辞精练。
- **图表**：Figure 1 和 Figure 2 的信息密度适中，Figure 3 稍显拥挤但可接受。Table 1 注释过密（见小问题 #2）。

---

**总结**：论文对一个真实且重要的问题（RLVR 中 neurosymbolic reasoning 的结构退化）提供了系统的实证分析。STA 作为 diagnostic 的有效性和 Goodhart effect 的文档化具有实用价值。主要短板是方法新颖性有限（LOO 的直接应用）和实验范围较窄（单一模型 + 少量 seeds）。如果能补充第二个 model family 的实验和/或 mitigation 方向的初步结果，会更有竞争力。当前状态介于 Findings 和 Conference 之间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2898 · 2026-05-23T01:50:20.956905+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n**Overall**: 3.5 / 5 — Borderline Conference\n\n**Must-Fix:**\n\n**N1** [Critical] — 新颖性不足：STA 是 LOO ablation 在 solver trace 上的直接应用\n- 论文明确承认 LOO ablation \"is standard\"，Algorithm 1 的核心逻辑没有超出经典 mutation testing 的 conceptual scope。ISR 本质是 LOO survival rate 的均值。与 Kim et al. (2026) 的 gaming detection 或 Helff et al. (2026) 的 IPT 相比，STA 不引入新的 perturbation primitive。论文自己承认\"our contribution lies in the application and findings, not in the perturbation primitive\"。\n- 建议：(1) C1 从\"diagnostic framework\"降为\"diagnostic method/protocol\"；(2) 增加 mitigation experiment（如 STA-guided curriculum、ISR-aware early stopping）提升实践价值。\n\n**N2** [Critical] — 单一基座模型，结论普适性存疑\n- 所有核心实验基于 Qwen3-4B。Qwen3-8B 和 LLaMA-3.2-3B 均未能收敛。2025-2026 RLVR 文献通常在至少 2-3 个 model families 上验证。\n- 建议：在另一个能成功 converge 的 model 上复现，或明确限定为\"Qwen3-4B case study\"。\n\n**Should-Fix:**\n\n**W1** [Major] — Observe-vs-optimize asymmetry 概念新颖性有限\n- 这正是 Goodhart's Law 的经典表述。论文已引用 Manheim & Garrabrant (2019) 并归类为 regressional Goodhart。作为 Goodhart's Law 在特定领域的经验性验证，C2 更接近\"confirming a known pattern in a new setting\"。\n- 建议：降低 framing 力度，改为\"we empirically demonstrate that ISR follows the regressional Goodhart pattern\"。\n\n**W2** [Major] — 统计功效不足，关键比较 underpowered\n- N=3 seeds/condition，pooled statistics treat within-seed samples as independent。ProofFOL p=0.10 是 underpowered。\n- 建议：标注所有 seed-level 比较为 descriptive/exploratory；考虑 bootstrap CI。\n\n**W3** [Minor] — \"Framework\" overclaim\n- STA 是 method/protocol 而非 framework。\n\n**W4** [Minor] — Hacking taxonomy 验证不够系统化\n- Precision 报告了但 recall 未报告，可能存在 false negatives。\n\n**小问题:** (1) §2 Related Work 中 self-assessment \"novel\" 不适合放在 related work 中；(2) Table 1 注释密度过高；(3) Figure 1 Y 轴标签建议改进；(4) \"hacking\"/\"gaming\" 术语混用；(5) SWI-Prolog 版本号未提供；(6) Coste et al. bib key 年份不一致。\n\n**Missing References:** 建议补充 3-4 篇 2026 年最新工作（reward hacking as equilibrium, representation-level signals, formal-verification-based PRMs），但遗漏不构成 critical gap。\n\n**格式合规**: 全部通过（页数、模板、double-blind、Limitations、Ethics、附录、引用格式）。\n\n**写作质量**: Good (4/5)，逻辑清晰，术语一致，无 AI 风格痕迹。\n\n**优势**: 问题定位精准、实验设计严谨、hacking taxonomy 有描述价值、跨域泛化、透明的 limitations、引用质量高。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n**Overall**: 3.5 / 5 — Borderline Conference\n\n**Must-Fix:**\n\n**N1** [Critical] — 新颖性不足：STA 是 LOO ablation 在 solver trace 上的直接应用\n- 论文明确承认 LOO ablation \"is standard\"，Algorithm 1 的核心逻辑没有超出经典 mutation testing 的 conceptual scope。ISR 本质是 LOO survival rate 的均值。与 Kim et al. (2026) 的 gaming detection 或 Helff et al. (2026) 的 IPT 相比，STA 不引入新的 perturbation primitive。论文自己承认\"our contribution lies in the application and findings, not in the perturbation primitive\"。\n- 建议：(1) C1 从\"diagnostic framework\"降为\"diagnostic method/protocol\"；(2) 增加 mitigation experiment（如 STA-guided curriculum、ISR-aware early stopping）提升实践价值。\n\n**N2** [Critical] — 单一基座模型，结论普适性存疑\n- 所有核心实验基于 Qwen3-4B。Qwen3-8B 和 LLaMA-3.2-3B 均未能收敛。2025-2026 RLVR 文献通常在至少 2-3 个 model families 上验证。\n- 建议：在另一个能成功 converge 的 model 上复现，或明确限定为\"Qwen3-4B case study\"。\n\n**Should-Fix:**\n\n**W1** [Major] — Observe-vs-optimize asymmetry 概念新颖性有限\n- 这正是 Goodhart's Law 的经典表述。论文已引用 Manheim & Garrabrant (2019) 并归类为 regressional Goodhart。作为 Goodhart's Law 在特定领域的经验性验证，C2 更接近\"confirming a known pattern in a new setting\"。\n- 建议：降低 framing 力度，改为\"we empirically demonstrate that ISR follows the regressional Goodhart pattern\"。\n\n**W2** [Major] — 统计功效不足，关键比较 underpowered\n- N=3 seeds/condition，pooled statistics treat within-seed samples as independent。ProofFOL p=0.10 是 underpowered。\n- 建议：标注所有 seed-level 比较为 descriptive/exploratory；考虑 bootstrap CI。\n\n**W3** [Minor] — \"Framework\" overclaim\n- STA 是 method/protocol 而非 framework。\n\n**W4** [Minor] — Hacking taxonomy 验证不够系统化\n- Precision 报告了但 recall 未报告，可能存在 false negatives。\n\n**小问题:** (1) §2 Related Work 中 self-assessment \"novel\" 不适合放在 related work 中；(2) Table 1 注释密度过高；(3) Figure 1 Y 轴标签建议改进；(4) \"hacking\"/\"gaming\" 术语混用；(5) SWI-Prolog 版本号未提供；(6) Coste et al. bib key 年份不一致。\n\n**Missing References:** 建议补充 3-4 篇 2026 年最新工作（reward hacking as equilibrium, representation-level signals, formal-verification-based PRMs），但遗漏不构成 critical gap。\n\n**格式合规**: 全部通过（页数、模板、double-blind、Limitations、Ethics、附录、引用格式）。\n\n**写作质量**: Good (4/5)，逻辑清晰，术语一致，无 AI 风格痕迹。\n\n**优势**: 问题定位精准、实验设计严谨、hacking taxonomy 有描述价值、跨域泛化、透明的 limitations、引用质量高。"
  }
}
```

</details>

---


### Tool result

_source line 2899 · 2026-05-23T01:50:53.349511+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 32392
}
```

</details>

---


### Tool call

_source line 2900 · 2026-05-23T01:50:53.651035+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n- 对于你与 Reviewer 1 有不同看法的地方，请特别说明\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n**Overall**: 3.0 / 5 (Findings)\n\n**Must-Fix:**\n\n**N1** [Critical] — 单一模型局限性与泛化声明不匹配\n- Abstract (\"structural proxies...are easier to observe than to optimize\"), §1 C1 (\"model-agnostic diagnostic method\"), §5 (\"STA is applicable in principle to any RL system\") 的泛化声明仅由 Qwen3-4B 实验支撑。C1 声称\"model-agnostic\"但论文从未在另一个成功收敛的模型上验证。\n- 建议：限定声明为\"in our Qwen3-4B experiments\"；C1 改为\"applicable to solver-verified reasoning\"而非\"model-agnostic\"。\n\n**N2** [Critical] — 5-seed 双峰结果实质性弱化 Goodhart effect 核心叙事\n- ISR β=0.1 的 5-seed 扩展中 s45/s46 产生 ~55% non-hacking，与 3-seed pooled 的 6% 形成鲜明对比。40% 种子未出现 Goodhart effect，直接挑战核心叙事。\n- Table 1 存在 framing asymmetry：ISR 3-seed 行仅报告 s42-44 的 N-H=6%，5-seed 行的 N-H=23% 被放在下方但未充分讨论。\n- 建议：C2 调整为\"seed-dependent Goodhart effect\"；Table 1 统一为 5-seed 或同时展示并讨论。\n\n**Should-Fix:**\n\n**W1** [Major] — Table 1 中 exec-only 仅报告 seed 42 造成不对称比较\n- ISR/Random 报告 3-seed pooled，但 exec-only 仅报告 s42。三个 exec-only 种子差异极大（s42 PR=93% CE=87%; s43 PR=13%; s44 PR=98% TS=100%）。有 cherry-picking 隐患。\n\n**W2** [Major] — ISR 聚合指标在控制 premise-count confound 后失去统计显著性\n- 214× raw collapse 在 premise-count matching 后降至 1.06×（McNemar p=0.317）。论文提出 ISR 作为诊断工具（C1），但 ISR 作为聚合指标是 confounded 的，真正有诊断力的是 per-sample mode classification。\n- 方法论悖论：ISR 作为核心贡献但其聚合价值被 premise-count 解释。\n\n**W3** [Major] — Hacking mode 分类的互斥性和完整性不够清晰\n- Table 9 中 Random s44 有\"CE∩PG: 6\"，说明 CE/PG 可共现，但主表暗示互斥。Non-hacking rate 是 upper bound（仅在 appendix 说明）。\n\n**W4** [Minor→Major] — s43 采样异常的解释不充分\n- \"Greedy-mode degeneration\" 未解释具体含义。ISR/Random 条件下 s43 的评估协议是否一致未明确。\n\n**小问题**: (1) Table 1 footnote ‡ 措辞可能引起混淆；(2) §3.2 Shapley value 类比不准确；(3) Figure 2 s43 标注仅在 caption 中；(4) Appendix D.1 PG 的 checkpoints 已删除不可恢复；(5) §2 列出大量 citation 但未逐一对比。\n\n**优势**: 实验控制设计出色、极高学术诚实度、observe-vs-optimize asymmetry 有价值、八模式 taxonomy 实用、跨逻辑验证有力、统计分析整体恰当。\n\n**Questions:**\nQ1: s45/s46 的 micro-batch 配置差异（4×2 vs 2×4）是否可能是双峰结果的原因？\nQ2: ProofFOL 上 ISR 可能有益的 dataset-dependent asymmetry 是否被低估了？\nQ3: Exec-only s44 自发产生 TS hacking——TS 是否不是 ISR-specific 的 gaming mode？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n- 对于你与 Reviewer 1 有不同看法的地方，请特别说明\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n**Overall**: 3.0 / 5 (Findings)\n\n**Must-Fix:**\n\n**N1** [Critical] — 单一模型局限性与泛化声明不匹配\n- Abstract (\"structural proxies...are easier to observe than to optimize\"), §1 C1 (\"model-agnostic diagnostic method\"), §5 (\"STA is applicable in principle to any RL system\") 的泛化声明仅由 Qwen3-4B 实验支撑。C1 声称\"model-agnostic\"但论文从未在另一个成功收敛的模型上验证。\n- 建议：限定声明为\"in our Qwen3-4B experiments\"；C1 改为\"applicable to solver-verified reasoning\"而非\"model-agnostic\"。\n\n**N2** [Critical] — 5-seed 双峰结果实质性弱化 Goodhart effect 核心叙事\n- ISR β=0.1 的 5-seed 扩展中 s45/s46 产生 ~55% non-hacking，与 3-seed pooled 的 6% 形成鲜明对比。40% 种子未出现 Goodhart effect，直接挑战核心叙事。\n- Table 1 存在 framing asymmetry：ISR 3-seed 行仅报告 s42-44 的 N-H=6%，5-seed 行的 N-H=23% 被放在下方但未充分讨论。\n- 建议：C2 调整为\"seed-dependent Goodhart effect\"；Table 1 统一为 5-seed 或同时展示并讨论。\n\n**Should-Fix:**\n\n**W1** [Major] — Table 1 中 exec-only 仅报告 seed 42 造成不对称比较\n- ISR/Random 报告 3-seed pooled，但 exec-only 仅报告 s42。三个 exec-only 种子差异极大（s42 PR=93% CE=87%; s43 PR=13%; s44 PR=98% TS=100%）。有 cherry-picking 隐患。\n\n**W2** [Major] — ISR 聚合指标在控制 premise-count confound 后失去统计显著性\n- 214× raw collapse 在 premise-count matching 后降至 1.06×（McNemar p=0.317）。论文提出 ISR 作为诊断工具（C1），但 ISR 作为聚合指标是 confounded 的，真正有诊断力的是 per-sample mode classification。\n- 方法论悖论：ISR 作为核心贡献但其聚合价值被 premise-count 解释。\n\n**W3** [Major] — Hacking mode 分类的互斥性和完整性不够清晰\n- Table 9 中 Random s44 有\"CE∩PG: 6\"，说明 CE/PG 可共现，但主表暗示互斥。Non-hacking rate 是 upper bound（仅在 appendix 说明）。\n\n**W4** [Minor→Major] — s43 采样异常的解释不充分\n- \"Greedy-mode degeneration\" 未解释具体含义。ISR/Random 条件下 s43 的评估协议是否一致未明确。\n\n**小问题**: (1) Table 1 footnote ‡ 措辞可能引起混淆；(2) §3.2 Shapley value 类比不准确；(3) Figure 2 s43 标注仅在 caption 中；(4) Appendix D.1 PG 的 checkpoints 已删除不可恢复；(5) §2 列出大量 citation 但未逐一对比。\n\n**优势**: 实验控制设计出色、极高学术诚实度、observe-vs-optimize asymmetry 有价值、八模式 taxonomy 实用、跨逻辑验证有力、统计分析整体恰当。\n\n**Questions:**\nQ1: s45/s46 的 micro-batch 配置差异（4×2 vs 2×4）是否可能是双峰结果的原因？\nQ2: ProofFOL 上 ISR 可能有益的 dataset-dependent asymmetry 是否被低估了？\nQ3: Exec-only s44 自发产生 TS hacking——TS 是否不是 ISR-specific 的 gaming mode？"
  }
}
```

</details>

---


### Tool result

_source line 2901 · 2026-05-23T01:50:55.162289+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1511
}
```

</details>

---


### Assistant

_source line 2902 · 2026-05-23T01:50:57.544510+00:00_

交叉分享已发送给两位 Reviewer。等待交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 265

## Round 265

2 recorded events


### User

_source line 2903 · 2026-05-23T01:51:00.205562+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿核心结论**：Overall 3.5/5 (Borderline Conference)。

主要发现：
- **N1 [Critical]**：STA 本质是 LOO ablation 的直接应用，方法新颖性有限，论文自己也承认 perturbation primitive 不新
- **N2 [Critical]**：仅 Qwen3-4B 单一模型，Qwen3-8B 和 LLaMA-3.2-3B 均未成功 converge，结论普适性存疑
- **W1 [Major]**：observe-vs-optimize asymmetry 本质是 Goodhart's Law 的已知实例，概念新颖性需降低 framing
- **W2 [Major]**：N=3-5 seeds 统计功效不足，关键比较 underpowered
- **优势**：问题定位精准、实验设计严谨（多对照条件）、hacking taxonomy 有描述价值、跨域验证增强外部效度、limitations 非常透明
- **引用**：抽查 10 条全部真实，未发现幻觉引用；遗漏 2-3 篇 2026 并行工作但不构成 critical gap
- **格式**：全部合规

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2904 · 2026-05-23T01:51:04.789315+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 266

## Round 266

2 recorded events


### User

_source line 2905 · 2026-05-23T01:51:42.766120+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix

**[AGREE] R2-N1: STA 新颖性有限，是 LOO 在 solver trace 上的直接应用**

同意 R2 的判断。论文自己在 §3.2 承认 "LOO ablation itself is standard in mutation testing and sensitivity analysis (DeMillo et al., 1978; Jia & Harman, 2011); novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces"，以及 §2 最后一段 "novelty lies in application and findings, not in the perturbation primitive"。Algorithm 1 的伪代码实质上是标准 LOO survival rate 计算，ISR（Eq. 1）是 LOO 结果的均值。

不过我想补充一点 nuance：论文的价值主要不在于 STA 方法本身，而在于 (a) 将 LOO 系统性地应用于 GRPO 训练过程并发现 structural degeneration 与 prove rate 的 decoupling，(b) observe-vs-optimize asymmetry 的实证展示，(c) 八模式 hacking taxonomy。如果论文将 C1 从 "diagnostic framework" 降为 "diagnostic protocol" 并弱化方法新颖性声明，转而强调实证发现的贡献，论文的定位会更准确。

R2 建议增加 mitigation experiment（STA-guided curriculum、ISR-aware early stopping）有道理——当前论文纯粹是诊断性的，没有提供任何解决方案，这限制了实践影响力。

**[AGREE] R2-N2: 单一基座模型，结论普适性存疑**

完全同意。这与我自己的 N1 一致。所有核心实验仅基于 Qwen3-4B，Qwen3-8B（Appendix E.3）和 LLaMA-3.2-3B（Appendix E.4）均未收敛。论文标题和 abstract 的 framing 暗示了超出实验证据的普遍性。

R2 提出的两个建议（在另一个能收敛的模型上复现，或限定为 case study）都合理。我倾向于后者更现实——在投稿截止前找到另一个能成功收敛的模型并完成全套实验难度较大。将论文定位为 "Qwen3-4B case study with cross-logic/cross-dataset replication" 而非 general claim 更为诚实。

---

### Should-Fix

**[REBUT] R2-W1: Observe-vs-optimize asymmetry 概念新颖性有限**

部分不同意。R2 认为这 "正是 Goodhart's Law 的经典表述"，但我认为论文的贡献在于一个更具体的、此前未被文献记录的机制：**诊断指标的 LOO 结构 by construction 满足了 tautological shortcuts 的 necessity criterion**（§4.3: "a single premise identical to the conclusion yields ISR≥0.5 by construction, directly satisfying the LOO metric"）。这不仅仅是 "Goodhart's Law 在新 setting 中的验证"——它揭示了 LOO-based metrics 的一个结构性弱点：任何基于 component removal 的 necessity 指标都天然容易被 P→P tautology 所满足。这一洞见对所有使用 ablation-based diagnostics 的 neurosymbolic 系统都有警示价值。

此外，论文发现 ISR 在不同 dataset 上表现出 dataset-dependent asymmetry（§4.4: FOLIO 上是 Goodhart，ProofFOL 上方向性有益），这超越了简单的 "known pattern in a new setting"——它表明 Goodhart effect 的方向取决于 dataset 的 hacking geometry，这一点在现有 Goodhart 文献中缺少实证。

但 R2 关于降低 framing 力度的建议是合理的。"Observe-vs-optimize asymmetry" 作为术语暗示了比实际贡献更大的概念新颖性。建议保留发现但降低术语的概念权重。

**[AGREE] R2-W2: 统计功效不足，关键比较 underpowered**

同意。这与我自己审稿中的关注一致。论文在 §4.1 已诚实承认 "At N=3, seed-level tests achieve 80% power only for very large effects (d≥3.0)"，CMH p-values 有明确的 descriptive caveats（§4.1: "should not be interpreted as formal inference over the seed population"）。但 R2 的建议——标注所有 seed-level 比较为 descriptive/exploratory——是合理的额外要求。

论文的强项是主要发现（TS compositional shift: χ²=174.8, p<10⁻³⁸; SFT vs exec-only: OR=147, p<0.001）在 Bonferroni 校正后仍然显著。真正 underpowered 的比较（ISR vs Random non-hacking: p=0.182; ProofFOL: p=0.10）论文已标注为 exploratory。

Bootstrap CI 建议是合理的补充手段，但在 N=3 seeds 下 bootstrap 本身也缺乏足够的 resampling basis，改善有限。

**[AGREE] R2-W3: "Framework" overclaim**

同意。STA 是 method/protocol 而非 framework。论文 C1 用 "diagnostic method" 是可以的，但 introduction 和 related work 中偶尔出现的 "framework" 表述应统一为 "method" 或 "protocol"。

**[AGREE] R2-W4: Hacking taxonomy recall 未报告**

同意。论文在 Appendix D 的 Classifier Validation 中报告了 precision（152 samples, 100%）但明确承认 "Recall is not estimable from a validation-only design"（Table 8 caption）。TSb subcategory 提供了 TS recall 的下界（≥91%, 149/163），但其他模式的 recall 未知。

这与我的 W3 一致——non-hacking rate 是上界估计，可能存在未识别的 hacking 模式。论文应在正文中（不仅在 appendix）明确声明这一 caveat。

---

### 小问题

- **R2 建议 §2 中删除 self-assessment "novel"**: [AGREE]，Related Work 中的 self-assessment 确实不规范。
- **R2 建议 Table 1 注释密度过高**: [AGREE]，Table 1 的 caption 确实过长（约 8 行 + 4 个标记符号），部分解释可移至正文或 appendix。
- **R2 建议改进 Figure 1 Y 轴标签**: 未发现明显问题，但如果 R2 有具体建议可以考虑。
- **R2 指出 hacking/gaming 术语混用**: [AGREE]，确实存在术语不一致（§3 多用 "hacking"，§4.3 混用 "gaming"）。建议统一。
- **R2 指出 SWI-Prolog 版本号未提供**: [REBUT]，Table 3 (Appendix A) 和 Table 10 caption 均报告了 "SWI-Prolog 8.4.2"。R2 可能遗漏了 Appendix 中的信息。
- **R2 指出 Coste et al. bib key 年份不一致**: 需要作者检查 references.bib，无法从 PDF 直接验证。

---

### 总体评价对比

R2 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于：

1. **R2 对 hacking taxonomy 的描述价值评价更高**，我认为 taxonomy 有用但 recall unknown 是显著弱点。
2. **R2 对 5-seed 双峰结果的冲击力评估不足**——R2 将其归入 W2 (statistical power) 作为次级问题，而我认为这是 critical issue (N2)：40% 种子不出现 Goodhart effect 直接挑战核心叙事。
3. **我对 ISR 聚合指标失去统计显著性（premise-count confound 后 p=0.317）的关注度更高**（我的 W2），R2 未单独列出此问题。

两位 reviewer 的共识区域：单模型局限性（R1-N1, R2-N2）、统计功效不足（R1 在多处提及, R2-W2）、方法新颖性有限（R2-N1, 我同意）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2906 · 2026-05-23T01:51:49.357466+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 267

## Round 267

2 recorded events


### User

_source line 2907 · 2026-05-23T01:51:51.980161+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。对 R2 的 6 个主要问题：4 个 AGREE（N1 新颖性有限、N2 单模型、W2 统计功效、W3 Framework overclaim、W4 recall 未报告），1 个 REBUT（W1 observe-vs-optimize asymmetry 的概念新颖性——LOO 结构性弱点和 dataset-dependent asymmetry 超越了简单的 Goodhart 验证）。同时指出了与 R2 评分差异的三个来源，核心分歧在于 5-seed 双峰结果的严重程度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2908 · 2026-05-23T01:52:02.310340+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 268

## Round 268

16 recorded events


### User

_source line 2909 · 2026-05-23T01:52:29.960506+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 的审稿意见

---

### Must-Fix 回应

**[AGREE] R1-N1: 单一模型局限性与泛化声明不匹配**

同意。这与我的 N2 完全一致。Abstract 中 "structural proxies...are easier to observe than to optimize" 是一个 general claim，但论文只在 Qwen3-4B 上验证了这一点。§5 中 "STA is applicable in principle to any RL system" 同样缺乏实证支撑。

补充发现：§1 的 C1 使用 "model-agnostic diagnostic framework" 这一措辞问题更严重——"model-agnostic" 需要至少在 2 个 model family 上验证才能成立。我在自己的 W3 中也指出了 "framework" 的 overclaim。R1 建议改为 "applicable to solver-verified reasoning" 是合理的降级方向，但我认为更准确的表述是 "a diagnostic method demonstrated on Qwen3-4B with GRPO-trained solver-verified reasoning"。

**[AGREE with nuance] R1-N2: 5-seed 双峰结果弱化 Goodhart 核心叙事**

同意核心判断，但对严重程度有不同看法。

R1 指出 s45/s46（~55% non-hacking）与 s42-44（~6%）的鲜明对比是一个 legitimate concern——40% 的种子未出现强 Goodhart effect 确实削弱了 "ISR-as-reward universally produces Goodhart effects" 的叙事。

然而，我认为这个发现本身也是有价值的——它表明 Goodhart effect 是 seed-dependent 的，这在 RLVR 文献中本身就是一个有意义的观察。论文在 §4.2 中确实讨论了 "cross-seed instability"（三颗种子分别收敛到 CE、repetition collapse 和 tautological collapse），说明作者并未完全忽视 stochasticity。

我的建议与 R1 一致但更具体：(1) C2 应调整为 "seed-dependent Goodhart effect that manifests in 3/5 seeds"；(2) Table 1 应在主表中同时展示 3-seed 和 5-seed 结果并直接讨论差异，而非将 5-seed 放在脚注/附录中弱化呈现。

**R1-N2 的 framing asymmetry 指控补充**：R1 指出 Table 1 存在 framing asymmetry（ISR 3-seed 行 N-H=6%，5-seed 行 N-H=23% 但放在下方未充分讨论），这确实构成 selective reporting 的 appearance。不过我注意到论文在 §4.2 "Bimodal seed-dependence" 段落中确实专门讨论了 s45/s46 的异常行为，不是完全隐瞒——只是 Table 1 的呈现方式有误导性。

---

### Should-Fix 回应

**[AGREE] R1-W1: Table 1 exec-only 仅报告 seed 42**

完全同意。ISR 和 Random 条件报告 3-seed pooled 结果，但 exec-only 仅报告单一种子 s42，这创造了不对称比较。R1 的发现（s42 PR=93% CE=87%; s43 PR=13%; s44 PR=98% TS=100%）表明三颗 exec-only 种子的行为差异巨大——选择性报告 s42 确实有 cherry-picking 的 appearance。

我在自己的审稿中未单独将此作为问题提出（我关注的是整体 seed 数量不足），R1 的这一发现补充了一个重要角度。建议 Table 1 统一报告所有条件的 3-seed pooled 结果，或至少在主表中注明 exec-only 仅为 single seed 并引导读者查看附录中的 per-seed 结果。

**[PARTIALLY AGREE] R1-W2: ISR 聚合指标在 premise-count matching 后失去显著性**

同意事实判断（214× → 1.06×, McNemar p=0.317），但不完全同意 R1 对此的解读严重程度。

R1 将此称为 "方法论悖论"——ISR 是核心贡献但其聚合价值被 premise-count 解释。但论文在 §4.3 "Premise-count confound" 段落中已经明确承认了这个问题，并提出 ISR 的真正诊断价值在于 per-sample mode classification（即 hacking taxonomy）而非聚合指标。§4.3 末尾写道 "mode composition analysis (CE vs. TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (§D), not on the number of premises in the formalization."

所以 confound 削弱的是 ISR 作为**聚合 metric** 的价值，但不影响 STA 作为**逐样本分类工具**的诊断能力。论文的 framing 可以更清晰地分离这两个层面。

建议：(1) 在 §3.2 ISR 定义后即提前说明 ISR 作为聚合指标的局限性和 premise-count sensitivity；(2) 将 per-sample mode classification 定位为主要贡献，ISR 聚合数值作为辅助。

**[AGREE] R1-W3: Hacking mode 分类互斥性和完整性问题**

同意。这与我的 W4（recall 未报告）指向同一个问题的不同侧面。R1 发现 Table 9 中 "CE∩PG: 6" 的共现是更直接的证据——如果 modes 可以共现，主表中暗示的互斥性就是误导性的。

补充：Table 2 将 8 modes 列为独立行，N-H rate 定义为 "upper bound on genuine reasoning"（仅在 appendix 说明），这可能导致读者高估 non-hacking 比例。建议在主文 §4.5 中明确说明 (1) modes 不互斥；(2) N-H rate 是 upper bound 而非 exact rate。

**[AGREE] R1-W4: s43 采样异常解释不充分**

同意。"Greedy-mode degeneration" 这个术语在论文中没有定义——它是指 greedy decoding 下模型退化为重复 token？还是其他现象？论文只说 s43 "uses nucleus sampling (T=0.7) due to greedy-mode degeneration" 但没有解释这个 degeneration 的具体表现和原因。

更重要的是，R1 正确指出了 protocol consistency 问题：如果 s43 使用了不同的解码策略，那么它与 s42/s44 的比较是否仍然公平？这不仅是解释问题，也是实验设计的一致性问题。

---

### Questions 回应

**Q1: s45/s46 micro-batch 配置差异（4×2 vs 2×4）是否是双峰结果的原因？**

这是一个非常好的问题，我在自己的审稿中未注意到。如果 s45/s46 使用了不同的 micro-batch 配置，那么双峰结果可能不是来自训练的内在随机性，而是来自超参数差异——这是一个潜在的 confound，会进一步削弱 "seed-dependent stochasticity" 的叙事。论文需要明确说明所有 5 颗种子是否使用了完全相同的超参数配置（除 seed 外）。

**Q2: ProofFOL ISR 可能有益的 dataset-dependent asymmetry？**

有价值的问题。论文在 §4.4 cross-dataset 结果中提到 ProofFOL 上 TS dominates 而非 CE，mode repertoire 是 dataset-specific。如果在某些 dataset 上 ISR 作为 training signal 确实有益（例如 ProofFOL 的 p=0.10），那么 "ISR-as-reward universally produces Goodhart effects" 的结论需要 dataset-level 的限定。

**Q3: Exec-only s44 自发产生 TS hacking——TS 不是 ISR-specific？**

非常好的观察。如果 TS (tautological shortcuts) 在 exec-only 条件下（无 ISR reward signal）就已出现（s44 TS=100%），那么 TS 不是由 ISR reward 诱导的——它是 GRPO training 本身的产物。这意味着论文 §4.5 hacking taxonomy 中将 TS 与 ISR-reward 关联的讨论需要 nuance：TS 是 general GRPO degeneration mode，不是 ISR-specific gaming。

---

### 综合评估

R1 的审稿整体质量很高，特别是在以下三个我未充分覆盖的方面提供了重要补充：
1. **Table 1 reporting asymmetry**（exec-only 仅 s42）——我忽略了这个 cherry-picking 风险
2. **5-seed 双峰问题**——我注意到了 seed 数量不足，但 R1 更精确地指出了双峰结果对核心叙事的定量影响
3. **Q3 的 exec-only TS 观察**——这对 hacking taxonomy 的因果归因有重要影响

R1 给出 Overall 3.0 (Findings)，我给出 3.5 (Borderline Conference)。考虑 R1 提出的 W1（cherry-picking appearance）和 N2（双峰结果），我认为论文当前状态确实更接近 **3.0-3.5** 的区间。如果作者能解决 Table 1 的呈现问题、澄清 s45/s46 的超参数一致性、并限定 generalization claims 的 scope，可以向 3.5 倾斜。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2910 · 2026-05-23T01:52:52.028581+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2911 · 2026-05-23T01:52:52.581242+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-23T01:41:47.923383+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_a771c2a33d631dd40256ecd5c3a6648e\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 2912 · 2026-05-23T01:52:52.581605+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2913 · 2026-05-23T01:52:53.517011+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T01:41:46.838048+00:00\", \"completed_at\": \"2026-05-23T01:45:05.555083+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3–6\", \"message\": \"连续 4 页几乎纯文本（仅 page 4 有 Algorithm 1 伪代码框作为视觉断点），pages 3、5、6 无任何 display item。Method 和 Setup 段落缺少图表穿插，审稿人容易在此区间失去注意力。建议将部分 appendix 中的表格（如 Table 4 ProofFOL vs. FOLIO 对比）前移至正文，或为 STA 方法增加一个概念示意图。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Display item 过度密集：Figure 2（双面板）、Figure 3（堆叠柱状图）、Table 2 三个 display item 加上 Section 4.5 和 Section 5 开头全部挤在同一页。与 pages 3–6 的\\\"文字沙漠\\\"形成鲜明节奏失衡。建议将 Table 2 或 Figure 3 移至 page 7 或调整 float 策略平衡密度。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 2 双面板 subfigure 中坐标轴标签和图例文字偏小（目测 ≤6pt），在打印或低分辨率屏幕上可能难以辨认。建议将 axis label 和 legend 字号提高至 ≥8pt。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯 Title + Abstract + Introduction 文本）。第一个 display item（Figure 1）出现在 page 2 顶部，仍在前 3 页范围内，符合要求。Figure 1 展示 ISR 训练轨迹，能有效锚定论文核心 message（structural degeneration）。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 使用蓝/橙/绿配色方案，色彩区分度良好；但建议检查色盲友好性（蓝+橙可以，绿色线条在 deuteranopia 下可能与橙色混淆）。可考虑辅以不同 line style（dashed/dotted）。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 使用 booktabs 风格，最优结果加粗标注，格式规范。Markers 说明行清晰。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Section 5 \\\"Discussion and Conclusion\\\" 标题出现在页面底部，后续仅跟 2–3 行正文即翻页。虽未完全孤悬（有后续文字），但视觉上略显突兀。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 篇幅适中（约 1 段），Ethics Statement 简洁，符合 EMNLP 要求。References 从 page 9 下半开始，格式一致，未见 [?] 未解析引用。\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"Table 9 详细 per-seed 结果表占据整页，字号较小（约 7pt）。\\\"—\\\" 占位符统一使用 em-dash，格式一致。\"}, {\"severity\": \"info\", \"dimension\": \"page 21\", \"message\": \"三个表格（Table
…[truncated 427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 935
}
```

</details>

---


### Tool call

_source line 2914 · 2026-05-23T01:52:53.668163+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2915 · 2026-05-23T01:52:53.668599+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2916 · 2026-05-23T01:53:00.047289+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2917 · 2026-05-23T01:53:00.098014+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2918 · 2026-05-23T01:53:02.709066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2919 · 2026-05-23T01:53:02.811652+00:00_

1	issues:
2	- id: R1-W1
3	  summary: "统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed"
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 0
8	  last_seen_round: 2
9	  resolution: "β=0.3 ISR 和 Random 各 3 seeds 已完成。"
10	  resolution_round: 2
11	- id: v22-R12-N3
12	  summary: "Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）"
13	  category: method
14	  severity: critical
15	  status: resolved
16	  first_raised_round: 22
17	  last_seen_round: 32
18	  resolution: "Two-level Goodhart separation + χ² test. Compositional narrative front-loaded in Abstract/Intro (R32)."
19	  resolution_round: 32
20	- id: v22-R12-N1
21	  summary: "ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果"
22	  category: framing
23	  severity: critical
24	  status: resolved
25	  first_raised_round: 22
26	  last_seen_round: 32
27	  resolution: "Compositional Goodhart reframed around mode shift (CE→TS), not scalar non-hacking rate. χ² test (174.8, p<10⁻³⁸)."
28	  resolution_round: 32
29	- id: v17-R12-W1
30	  summary: "单模型 (Qwen3-4B) 无法支撑通用性声明"
31	  category: experiment
32	  severity: critical
33	  status: wont_fix
34	  first_raised_round: 17
35	  last_seen_round: 32
36	  resolution: "结构性限制：8B/LLaMA 均未收敛，DDL 前无法补模型。C1 保留 'model-agnostic' (设计属性)，C2/C3 限定 'in Qwen3-4B experiments'。Limitations L1-2 明确讨论。Rebuttal 论点：STA 设计不依赖模型，实验受限于 GRPO 收敛困难而非方法局限。"
37	- id: v27-R1-N2
38	  summary: "CMH pseudo-replication：within-seed samples 非独立"
39	  category: experiment
40	  severity: warning
41	  status: resolved
42	  first_raised_round: 27
43	  last_seen_round: 32
44	  resolution: "CMH OR moved to appendix (R32). χ² retained. Per-seed qualitative analysis as primary framework."
45	  resolution_round: 32
46	- id: v17-R1-W9
47	  summary: "Seed 43 使用 T=0.7 sampling 评估而非 greedy"
48	  category: experiment
49	  severity: critical
50	  status: resolved
51	  first_raised_round: 17
52	  last_seen_round: 32
53	  resolution: "N=2 sensitivity analysis. s43
…[truncated 4001 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2920 · 2026-05-23T01:54:47.214066+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n- id: R1-W1\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。\"\n  resolution_round: 2\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 32\n  mentions:\n    - round: 33\n      reviewers: [R1]\n      note: \"R1-W2 再次提出：ISR 聚合指标在 premise-count matching 后失去统计显著性（214×→1.06×, McNemar p=0.317），称之为'方法论悖论'。R2 部分同意但认为 per-sample 诊断价值不受影响。论文 §4.3 已讨论但 R1 认为需更明确分离 ISR 的两个层面（聚合 vs per-sample）。\"\n  resolution: \"Two-level Goodhart separation + χ² test. Compositional narrative front-loaded in Abstract/Intro (R32).\"\n  resolution_round: 32\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 32\n  resolution: \"Compositional Goodhart reframed around mode shift (CE→TS), not scalar non-hacking rate. χ² test (174.8, p<10⁻³⁸).\"\n  resolution_round: 32\n- id: v17-R12-W1\n  summary: \"单模型 (Qwen3-4B) 无法支撑通用性声明\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 33\n  mentions:\n    - round: 32\n      reviewers: [R1, R2]\n      note: \"wont_fix rebuttal 论点准备完毕。\"\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R1-N1 和 R2-N2 均列为 Critical。两位 Reviewer 共识：Abstract/C1/Discussion 的泛化声明超出实验证据。R1 建议限定为 'in our Qwen3-4B experiments'；R2 建议 C1 改为 'demonstrated on Qwen3-4B'。此前 wont_fix 的 rebuttal 论点（STA 设计不依赖模型）仍有效，但 framing 调整尚未执行。\"\n  resolution: \"\"\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 32\n  resolution: \"CMH OR moved to appendix (R32). χ² retained. Per-seed qualitative analysis as primary framework.\"\n  resolution_round: 32\n- id: v17-R1-W9\n  summary: \"Seed 43 使用 T=0.7 sampling 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 33\n  mentions:\n    - round: 31\n      reviewers: [R1]\n      note: \"N=2 sensitivity analysis added. s43 flagged in limitations.\"\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R1-W4: 'greedy-mode degeneration' 具体含义未解释。R2 同意：protocol consistency 问题——ISR/Random 条件下 s43 评估协议是否一致未明确。此前 resolved 但本轮升级为需解释。\"\n  resolution: \"\"\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 33\n  mentions:\n    - round: 32\n      reviewers: [R2]\n      note: \"wont_fix rebuttal 论点准备完毕。\"\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R2-N1 列为 Critical（ACL ARR Excitement 维度）。R1 同意但补充：论文价值在于 LOO 的系统性应用+实证发现+taxonomy，非方法本身。建议 C1 从 framework 降为 method/protocol。此前 wont_fix 但两位 Reviewer 共识认为仍是主要短板。\"\n  resolution: \"\"\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念——本质即 Goodhart's Law\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 33\n  mentions:\n    - round: 31\n      reviewers: [R2]\n      note: \"Reframed as empirical instantiation.\"\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R2-W1 再次提出。R1 部分 REBUT：LOO 结构性弱点（tautology by construction 满足 necessity）和 dataset-dependent asymmetry 超越简单 Goodhart 验证。交叉后 R2 认可 R1 的 rebut 有一定道理但仍建议降低 framing。此前 resolved 但本轮 R2 认为降级不够。\"\n  resolution: \"\"\n- id: v30-R1-W1\n  summary: \"SFT baseline PR=13% vs exec-only PR=93% 使 ISR 比较存在 selection bias\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"SFT positioned as pre-RL temporal reference. Random control is the fair comparison.\"\n  resolution_round: 31\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 22\n  last_seen_round: 31\n  resolution: \"结构性限制：Shuffled-ISR 本身收敛困难 (PR=15%), 无法增加 proved samples。论文已标注 'corroborating rather than definitive given N=46'。Rebuttal 论点：N=46 下 SFT-like 87% non-hacking 定性结论成立，概念设计巧妙。\"\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证 50 样本偏少 + recall 未评估\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 33\n  mentions:\n    - round: 32\n      reviewers: [R2]\n      note: \"wont_fix: recall 评估需全量人工标注。\"\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R2-W4 再次提出 recall 未报告。R1-W3 补充：modes 互斥性未明确（CE∩PG:6 共现）；non-hacking rate 是 upper bound 仅在 appendix 说明。两位 Reviewer 共识。\"\n  resolution: \"\"\n- id: v19-R12-W3\n  summary: \"ProofFOL p=0.10 被过度引用\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 32\n  resolution: \"'substantially' → 'directionally higher'. ProofFOL labeled exploratory and underpowered.\"\n  resolution_round: 31\n- id: v30-R2-W3\n  summary: \"ISR 与 NLI accuracy 不相关限制 actionability\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"ISR=0 semantic disambiguation added. 'reasoning quality' → 'formalization integrity' (R32).\"\n  resolution_round: 32\n- id: v31-R2-MR-SPECGAMING\n  summary: \"缺失引用：Towards Understanding Specification Gaming in Reasoning Models (arXiv:2605.02269)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"Nishimura et al. (2026) citation added.\"\n  resolution_round: 31\n- id: v31-R2-W-TITLE-LENGTH\n  summary: \"标题过长（~140 chars），建议精简\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 32\n  resolution: \"Title shortened to ~95 chars.\"\n  resolution_round: 32\n- id: v31-R2-M-ISR0-AMBIGUITY\n  summary: \"ISR=0 对 proved vs unproved 语义不同但用同一值\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"ISR=0 semantic disambiguation added to method.tex.\"\n  resolution_round: 31\n- id: v32-R12-MR-UNFAITHFUL-COT\n  summary: \"缺失引用：Lanham et al. 2023 (CoT faithfulness) + Turpin et al. 2023 (unfaithful explanations)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  resolution: \"Both citations added to references.bib and related_work.tex.\"\n  resolution_round: 32\n# ===== Round 33 新增 =====\n- id: v33-R1-N2\n  summary: \"5-seed 双峰结果（s45/s46 ~55% non-hacking）实质性弱化 Goodhart effect 核心叙事\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R1 列为 Critical：40% 种子不出现 Goodhart effect 直接挑战核心叙事。Table 1 存在 framing asymmetry（3-seed N-H=6% 在主行，5-seed N-H=23% 在下方弱化呈现）。R2 agree with nuance：严重程度略低于 R1 判断，seed-dependent Goodhart 本身有价值，但同意 C2 应调整为 seed-dependent。\"\n  action_items:\n    - round: 33\n      action: \"C2 措辞调整为 'seed-dependent Goodhart effect'；Table 1 统一展示 5-seed 或同时讨论 3-seed vs 5-seed 差异\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v33-R1-W1\n  summary: \"Table 1 exec-only 仅报告 seed 42，与其他条件的 3-seed pooled 不对称\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R1 提出，R2 完全同意。三颗 exec-only 种子差异极大（s42 CE=87%; s44 TS=100%），仅报告 s42 有 cherry-picking appearance。\"\n  action_items:\n    - round: 33\n      action: \"Table 1 exec-only 行改为 3-seed pooled 或同时展示三颗种子\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v33-R1-W3\n  summary: \"Hacking mode 分类互斥性未明确（CE∩PG 共现），non-hacking 是 upper bound 仅在 appendix 说明\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R1 发现 Table 9 中 CE∩PG:6 共现。R2 同意：主文应声明 modes 不互斥 + N-H 是 upper bound。\"\n  action_items:\n    - round: 33\n      action: \"§4.5 正文中明确 (1) modes 不互斥及优先级规则 (2) N-H rate 是 upper bound\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v33-R2-MR1\n  summary: \"可能遗漏引用：Reward Hacking as Equilibrium (arXiv:2603.28063), representation-level signals (arXiv:2604.01476)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [R2]\n      note: \"R2 建议补充 2-3 篇 2026 年并行工作，但评估为不构成 critical gap。\"\n  resolution: \"\"\n  resolution_round: null\n- id: v33-R1-Q3\n  summary: \"Exec-only s44 自发产生 TS (100%)——TS 非 ISR-specific gaming mode，因果归因需修正\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R1 Q3 提出，R2 交叉回应中强调：如果 TS 在无 ISR reward 下已出现，'ISR converts CE into TS' 的叙事需修正为 'ISR amplifies a pre-existing TS tendency'。\"\n  action_items:\n    - round: 33\n      action: \"§4.3/§4.5 中修正 TS 归因叙事\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n- id: R1-W1\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。\"\n  resolution_round: 2\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 32\n  mentions:\n    - round: 33\n      reviewers: [R1]\n      note: \"R1-W2 再次提出：ISR 聚合指标在 premise-count matching 后失去统计显著性（214×→1.06×, McNemar p=0.317），称之为'方法论悖论'。R2 部分同意但认为 per-sample 诊断价值不受影响。论文 §4.3 已讨论但 R1 认为需更明确分离 ISR 的两个层面（聚合 vs per-sample）。\"\n  resolution: \"Two-level Goodhart separation + χ² test. Compositional narrative front-loaded in Abstract/Intro (R32).\"\n  resolution_round: 32\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 32\n  resolution: \"Compositional Goodhart reframed around mode shift (CE→TS), not scalar non-hacking rate. χ² test (174.8, p<10⁻³⁸).\"\n  resolution_round: 32\n- id: v17-R12-W1\n  summary: \"单模型 (Qwen3-4B) 无法支撑通用性声明\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 33\n  mentions:\n    - round: 32\n      reviewers: [R1, R2]\n      note: \"wont_fix rebuttal 论点准备完毕。\"\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R1-N1 和 R2-N2 均列为 Critical。两位 Reviewer 共识：Abstract/C1/Discussion 的泛化声明超出实验证据。R1 建议限定为 'in our Qwen3-4B experiments'；R2 建议 C1 改为 'demonstrated on Qwen3-4B'。此前 wont_fix 的 rebuttal 论点（STA 设计不依赖模型）仍有效，但 framing 调整尚未执行。\"\n  resolution: \"\"\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 32\n  resolution: \"CMH OR moved to appendix (R32). χ² retained. Per-seed qualitative analysis as primary framework.\"\n  resolution_round: 32\n- id: v17-R1-W9\n  summary: \"Seed 43 使用 T=0.7 sampling 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 33\n  mentions:\n    - round: 31\n      reviewers: [R1]\n      note: \"N=2 sensitivity analysis added. s43 flagged in limitations.\"\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R1-W4: 'greedy-mode degeneration' 具体含义未解释。R2 同意：protocol consistency 问题——ISR/Random 条件下 s43 评估协议是否一致未明确。此前 resolved 但本轮升级为需解释。\"\n  resolution: \"\"\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 33\n  mentions:\n    - round: 32\n      reviewers: [R2]\n      note: \"wont_fix rebuttal 论点准备完毕。\"\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R2-N1 列为 Critical（ACL ARR Excitement 维度）。R1 同意但补充：论文价值在于 LOO 的系统性应用+实证发现+taxonomy，非方法本身。建议 C1 从 framework 降为 method/protocol。此前 wont_fix 但两位 Reviewer 共识认为仍是主要短板。\"\n  resolution: \"\"\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念——本质即 Goodhart's Law\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 33\n  mentions:\n    - round: 31\n      reviewers: [R2]\n      note: \"Reframed as empirical instantiation.\"\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R2-W1 再次提出。R1 部分 REBUT：LOO 结构性弱点（tautology by construction 满足 necessity）和 dataset-dependent asymmetry 超越简单 Goodhart 验证。交叉后 R2 认可 R1 的 rebut 有一定道理但仍建议降低 framing。此前 resolved 但本轮 R2 认为降级不够。\"\n  resolution: \"\"\n- id: v30-R1-W1\n  summary: \"SFT baseline PR=13% vs exec-only PR=93% 使 ISR 比较存在 selection bias\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"SFT positioned as pre-RL temporal reference. Random control is the fair comparison.\"\n  resolution_round: 31\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 22\n  last_seen_round: 31\n  resolution: \"结构性限制：Shuffled-ISR 本身收敛困难 (PR=15%), 无法增加 proved samples。论文已标注 'corroborating rather than definitive given N=46'。Rebuttal 论点：N=46 下 SFT-like 87% non-hacking 定性结论成立，概念设计巧妙。\"\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证 50 样本偏少 + recall 未评估\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 33\n  mentions:\n    - round: 32\n      reviewers: [R2]\n      note: \"wont_fix: recall 评估需全量人工标注。\"\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R2-W4 再次提出 recall 未报告。R1-W3 补充：modes 互斥性未明确（CE∩PG:6 共现）；non-hacking rate 是 upper bound 仅在 appendix 说明。两位 Reviewer 共识。\"\n  resolution: \"\"\n- id: v19-R12-W3\n  summary: \"ProofFOL p=0.10 被过度引用\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 32\n  resolution: \"'substantially' → 'directionally higher'. ProofFOL labeled exploratory and underpowered.\"\n  resolution_round: 31\n- id: v30-R2-W3\n  summary: \"ISR 与 NLI accuracy 不相关限制 actionability\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"ISR=0 semantic disambiguation added. 'reasoning quality' → 'formalization integrity' (R32).\"\n  resolution_round: 32\n- id: v31-R2-MR-SPECGAMING\n  summary: \"缺失引用：Towards Understanding Specification Gaming in Reasoning Models (arXiv:2605.02269)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"Nishimura et al. (2026) citation added.\"\n  resolution_round: 31\n- id: v31-R2-W-TITLE-LENGTH\n  summary: \"标题过长（~140 chars），建议精简\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 32\n  resolution: \"Title shortened to ~95 chars.\"\n  resolution_round: 32\n- id: v31-R2-M-ISR0-AMBIGUITY\n  summary: \"ISR=0 对 proved vs unproved 语义不同但用同一值\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"ISR=0 semantic disambiguation added to method.tex.\"\n  resolution_round: 31\n- id: v32-R12-MR-UNFAITHFUL-COT\n  summary: \"缺失引用：Lanham et al. 2023 (CoT faithfulness) + Turpin et al. 2023 (unfaithful explanations)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  resolution: \"Both citations added to references.bib and related_work.tex.\"\n  resolution_round: 32\n# ===== Round 33 新增 =====\n- id: v33-R1-N2\n  summary: \"5-seed 双峰结果（s45/s46 ~55% non-hacking）实质性弱化 Goodhart effect 核心叙事\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R1 列为 Critical：40% 种子不出现 Goodhart effect 直接挑战核心叙事。Table 1 存在 framing asymmetry（3-seed N-H=6% 在主行，5-seed N-H=23% 在下方弱化呈现）。R2 agree with nuance：严重程度略低于 R1 判断，seed-dependent Goodhart 本身有价值，但同意 C2 应调整为 seed-dependent。\"\n  action_items:\n    - round: 33\n      action: \"C2 措辞调整为 'seed-dependent Goodhart effect'；Table 1 统一展示 5-seed 或同时讨论 3-seed vs 5-seed 差异\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v33-R1-W1\n  summary: \"Table 1 exec-only 仅报告 seed 42，与其他条件的 3-seed pooled 不对称\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R1 提出，R2 完全同意。三颗 exec-only 种子差异极大（s42 CE=87%; s44 TS=100%），仅报告 s42 有 cherry-picking appearance。\"\n  action_items:\n    - round: 33\n      action: \"Table 1 exec-only 行改为 3-seed pooled 或同时展示三颗种子\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v33-R1-W3\n  summary: \"Hacking mode 分类互斥性未明确（CE∩PG 共现），non-hacking 是 upper bound 仅在 appendix 说明\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R1 发现 Table 9 中 CE∩PG:6 共现。R2 同意：主文应声明 modes 不互斥 + N-H 是 upper bound。\"\n  action_items:\n    - round: 33\n      action: \"§4.5 正文中明确 (1) modes 不互斥及优先级规则 (2) N-H rate 是 upper bound\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n- id: v33-R2-MR1\n  summary: \"可能遗漏引用：Reward Hacking as Equilibrium (arXiv:2603.28063), representation-level signals (arXiv:2604.01476)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [R2]\n      note: \"R2 建议补充 2-3 篇 2026 年并行工作，但评估为不构成 critical gap。\"\n  resolution: \"\"\n  resolution_round: null\n- id: v33-R1-Q3\n  summary: \"Exec-only s44 自发产生 TS (100%)——TS 非 ISR-specific gaming mode，因果归因需修正\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [R1, R2]\n      note: \"R1 Q3 提出，R2 交叉回应中强调：如果 TS 在无 ISR reward 下已出现，'ISR converts CE into TS' 的叙事需修正为 'ISR amplifies a pre-existing TS tendency'。\"\n  action_items:\n    - round: 33\n      action: \"§4.3/§4.5 中修正 TS 归因叙事\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 2921 · 2026-05-23T01:54:47.315149+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 9250}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---
