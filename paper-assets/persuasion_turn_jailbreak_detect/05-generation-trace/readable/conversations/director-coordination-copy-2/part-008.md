# Director coordination — Part 8 of 8

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Conversation logs

[← Part 7](part-007.md) · [Transcript overview](../director-coordination-copy-2.md) · [Structured JSON](../../../sessions/6d/6ddf598184a3dac569b9.json)

## Round 168

### Assistant

_source line 2106 · 2026-05-24T13:27:28.386009+00:00_

Reviewer 1 审稿报告已收到。评分 3.0 (Findings)，3 个 Must-Fix + 5 个 Should-Fix。

等待 Reviewer 2 的审稿报告，收到后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 169

## Round 169

2 recorded events


### User

_source line 2107 · 2026-05-24T13:27:31.760472+00:00_

[Reviewer 1 审稿结果]:
审稿完成。报告已提交至 Review Director，评分 **Overall 3.0 (Findings)**。

核心发现：3 个 must-fix 问题——(1) OOD 评估集中 benign/jailbreak 对话长度零重叠构成未控制的混淆因素；(2) "label semantics 不重要"的 claim 在 ActorAttack 上被 TOST 检验否定（p=0.183），abstract 表述过度泛化；(3) WildChat 68.1% FPR 严重削弱跨域泛化叙事。5 个 should-fix 问题涉及 TOST δ=5pp 自相矛盾的论证、3 seeds 统计力不足、Topic 变体类别数混淆、RoBERTa-large DAPT 反转机制不明、1000 样本性能下降缺乏验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2108 · 2026-05-24T13:27:41.468517+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 170

## Round 170

6 recorded events


### User

_source line 2109 · 2026-05-24T13:28:01.418509+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 审稿报告：DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection

**审查侧重：新颖性 + 完整性 + 写作质量**

---

## 总体评分

**Overall**: 3.0 — Findings（可被 Findings 接收）
**一句话总结**: 实验设计扎实、ablation 彻底，但核心发现的增量新颖性有限——classification DAPT 优于 vanilla/MLM 在 Gururangan et al. (2020) 框架下基本可预测，而 ToxicChat 上的 hierarchy 反转显著削弱了核心叙事的普适性。

---

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨（7 variants × 13 configs × 3 scales，TOST 等价检验），但 ToxicChat 反转对核心 claim 构成实质性限制；全合成数据（单一 Qwen3-8B 生成器）限制了结论的可推广性 |
| Excitement | 2.5/5 | Scrambled-label 发现和 compression 机制分析有洞见价值，但 DAPT > vanilla 这一核心结果在现有 DAPT 理论下并不意外；practical impact 受限于合成数据和单一任务 |
| Reproducibility | 4/5 | 提供了完整的超参数、训练细节、3-seed mean±std、TOST 统计检验；Appendix 详尽（25 页补充材料） |
| Overall Assessment | 3.0/5 | Findings 级别：方法论扎实、ablation 全面，但新颖性增量有限，ToxicChat 反转削弱了 take-away 的力度 |
| Reviewer Confidence | 4/5 | 对 DAPT/encoder adaptation 和 jailbreak detection 领域都较熟悉，仔细阅读了全文和附录 |

---

## 主要优势

- **S1. 实验设计的严谨性和系统性。** 7 个 Stage-1 variants 严格控制变量（仅改变 pretraining objective），共 13 configurations × 3 encoder scales，是该领域少见的 controlled factorial study（Section 3, Table 1）。TOST 等价检验（Appendix L）超越了常见的"差异不显著 ≠ 等价"陷阱，统计方法论水平高于同类工作。

- **S2. Scrambled-label 发现提供了机制性洞见。** Scrambled labels 与 correct labels 在 template attack 检测上 TOST-confirmed 等价（|d| ≤ 0.14 on DD, d ≈ 0 on FITD; Section 4.3），说明 classification objective 的结构性作用（partition-based compression）而非 label semantics 驱动泛化。这一发现结合 SVD 分析（Figure 4, Appendix S–T）形成了较完整的机制解释链。

- **S3. 诚实的 boundary 报告。** 论文没有回避 ToxicChat 上 hierarchy 反转（MLM 0.837 vs. classification 0.596, Section 5）和 RoBERTa-large 355M 上 DAPT 反效果（vanilla AA=1.000 vs. 9-class 0.946, Section 4.4），这些对核心 claim 的限制被显式讨论。

- **S4. 实用的 few-shot benign adaptation。** 10–25 conversations 将 FPR 从 58–68% 降至 0–1.5%（Section 4.8, Appendix P），具有 deployment 价值；24.3× speedup over LLM-as-judge 的效率对比也清晰标注为 inference cost comparison。

- **S5. Appendix 的深度。** 25 页补充材料覆盖了 cross-checkpoint variance（Appendix N）、perturbation robustness（Appendix D）、CKA 分析（Appendix S）、SVD necessity（Appendix T）、length stratification（Appendix U）等，为主文 claims 提供了坚实的证据支撑。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心 evidence hierarchy 的增量新颖性不足——需要更清楚地区分"可预测"与"genuinely unexpected"
- 具体位置：Section 1（Introduction），第 22 行 "three findings in our safety-detection setting are unexpected"
- 问题：论文将三个发现统一标记为 "unexpected"，但 finding (i)——classification DAPT 大幅超越 vanilla/MLM——在 Gururangan et al. (2020) 的 DAPT 框架下是高度可预测的。DAPT 论文已经证明 domain-adaptive pretraining 改善下游任务，且 task-adaptive pretraining (TAPT) 带来额外收益。Classification-based adaptation（本质上是 supervised TAPT）优于 unsupervised MLM DAPT 符合该理论的直觉。
- 为什么影响接收：对于 Excitement 维度，reviewer 需要判断论文的 "what we didn't already know" 是什么。如果核心结果可从已有理论预测，论文的增量贡献需要重新定位——真正的新贡献是 (ii) scrambled-label equivalence 和 (iii) ToxicChat reversal，而不是 evidence hierarchy 本身。
- 建议修改方向：在 Introduction 中将 finding (i) 定位为 "quantifying the magnitude and robustness of a DAPT-predicted advantage in a novel safety-critical domain"，而将 (ii) 和 (iii) 定位为 genuinely unexpected findings。明确论文的核心新颖性在于 **机制分解**（为什么 DAPT works：结构性压缩而非语义学习）和 **boundary conditions**（何时 DAPT fails），而非 DAPT 有效这一事实本身。

**N2** [critical] ToxicChat 反转对核心叙事的削弱未被充分处理
- 具体位置：Section 5 "Cross-condition transfer and boundaries"；Abstract 第三个 finding
- 问题：论文的核心叙事是建立 evidence hierarchy（classification > MLM > vanilla），但在唯一的 human data 测试（ToxicChat）上，MLM（0.837）大幅超越 classification（0.596）。这不仅是一个 boundary condition，而是对核心 claim 的实质性反转。论文在 Section 5 将此处理为 "the hierarchy reverses" 并在 Discussion 中讨论了 distributional heterogeneity 的角色，但核心 take-away 实际上被弱化为 "adaptation strategy depends on data distribution"——这是一个相当平凡的结论。
- 为什么影响接收：如果 evidence hierarchy 仅在 synthetic template attacks 上成立，实际部署场景中面对的恰恰是 non-template, diverse human attacks。论文需要更深入地分析为什么反转发生（是 ToxicChat 的 single-turn 特性？数据分布差异？还是 classification compression 对 diverse attack patterns 有害？），以及 practitioners 在什么条件下应该选择哪种 adaptation。
- 建议修改方向：(a) 增加一段专门分析 ToxicChat 反转原因的讨论——当前 Section 5 的一句 "the hierarchy reverses" 太简略；(b) 在 Conclusion 中将 take-away 从 "classification DAPT is robust" 修改为更 nuanced 的条件性结论；(c) 如果可能，增加另一个 human/diverse data evaluation 来检验 ToxicChat 是否是孤例。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Evidence hierarchy" 术语缺乏正式定义
- 具体位置：首次出现在 Section 4.3 "A clear evidence hierarchy emerges"，贯穿全文
- 问题：该术语反复使用但从未给出一句话的显式定义。从上下文可推断其含义（encoder variants 按 OOD 检测性能排列的顺序：9-class > binary > MLM > vanilla），但对初次阅读的 reviewer 增加了认知负担。与 "discriminative compression"（在 Section 5 有 SVD-based 定义）不同，evidence hierarchy 始终是隐式的。
- 建议：在 Section 4.3 首次使用时加一句括号定义："a clear evidence hierarchy emerges (the consistent ordering of variant effectiveness for OOD detection: classification-supervised > MLM > vanilla)"。

**W2** [warning] Scrambled ≈ 9-class 的 "counter-intuitive" framing 需要推敲
- 具体位置：Section 4.3，Abstract "scrambled labels match correct labels"
- 问题：论文将 scrambled labels ≈ correct labels 定位为 unexpected，但如果接受论文自己提出的 discriminative compression 机制（Section 5, Figure 4），这一结果实际上是可预测的——只要 pretraining objective 诱导了 partition-based feature compression，具体 label 分配不影响压缩效果。此外，scrambled 与 9-class 的差异在 ActorAttack 上是 moderate（d=0.44），这与 "equivalence" 叙事不完全一致。
- 建议：(a) 在 Section 5 讨论中承认 scrambled ≈ 9-class 在 compression 框架下其实是 expected 而非 counter-intuitive，真正 unexpected 的是这个 compression 机制本身；(b) 更突出 ActorAttack 上 scrambled ≠ 9-class 的差异（d=0.44）并讨论其含义——策略多样性可能确实需要正确的 label semantics。

**W3** [warning] Conclusion 中 "reusable template" 声称超出实证范围
- 具体位置：Section 6 Conclusion "This ablation framework provides a template for diagnosing when domain adaptation succeeds and fails"
- 问题：论文仅在一个任务（multi-turn jailbreak detection）上用合成数据（单一生成器 Qwen3-8B）演示了该框架。"Template" 意味着方法论可迁移到其他 safety detection 任务，但没有跨任务验证。
- 建议：改为 "provides initial evidence that controlled ablation can diagnose when domain adaptation succeeds and fails in safety-critical detection" 或加上 "on the single task studied here"。

**W4** [warning] BiGRU vs. mean pooling 的讨论过于简略
- 具体位置：Section 5 "Mean pooling matches BiGRU (Δ ≤ 1 pp)"
- 问题：如果 mean pooling 与 BiGRU 等效，这对论文的 Stage-2 设计有重要含义——temporal aggregation 可能是不必要的。论文用一句话带过，但这个发现值得 2–3 句讨论：(a) 这是否说明 per-turn content 比 turn ordering 更重要？(b) 这对 production deployment 的简化意味什么？Table 3 和 Appendix Z.1 提供了数据但正文讨论不足。
- 建议：在 Section 5 中增加 2 句讨论，解释这个发现对 detection mechanism 的理解（per-turn content vs. sequential dynamics）以及对实际部署的意义。

---

## 小问题（不影响接收）

- **M1.** Figure 2 和 Figure 3 bar charts 在打印尺寸下较密，7 个 variants 的 bars 难以区分。考虑分组或使用 heatmap 替代。
- **M2.** Abstract 信息密度较高（~177 words），包含三个 findings 及具体数值（F1=0.97–1.0, 0.26–0.31）。虽然在 200-word limit 内，但第三句（"unsupervised pretraining collapses under mixed-LLM training"）对不熟悉实验设置的读者可能不够清晰。
- **M3.** Introduction footnote 1 已明确区分 "disentangled" 与 disentangled representation learning（β-VAE, InfoGAN）——处理得当，无需修改。
- **M4.** Page 25 "Use of AI Assistants" 声明提及 Claude (Anthropic)，适当但可以更具体说明 AI 辅助的范围/比例。

---

## Questions（需要作者澄清）

**Q1.** ToxicChat 上 evidence hierarchy 反转的根本原因是什么？是因为 ToxicChat 是 single-turn 数据而非 multi-turn？还是 human-authored jailbreaks 的 distributional properties 与 synthetic template attacks 根本不同？如果是后者，classification DAPT 在 multi-turn human jailbreak 数据上是否也会反转？

**Q2.** Scrambled labels 在 ActorAttack 上表现出 moderate label effect（d=0.44），但论文将此归类为 "moderate" 并仍然强调 equivalence。能否提供更多分析说明 ActorAttack 的什么特性导致了 scrambled 与 correct labels 的分歧？这是否与 ActorAttack 的策略多样性（多 persona 切换）有关？

**Q3.** 论文选择 Qwen3-8B 作为唯一的合成数据生成器。Section 4.5 的 Mixed-LLM Training 使用 Qwen + Llama，但这是测试条件而非训练数据多样性。作者是否考虑过使用多个 LLM 生成训练数据？这对 evidence hierarchy 的稳定性有什么影响？

**Q4.** RoBERTa-large (355M) 上 DAPT 变得 counterproductive（Table 4, Section 4.4）。这对于 larger encoder scales 的适用性有重要含义。作者对这一 scale-dependent 效应有什么解释？是否有证据表明更大的 encoder 自身已经具备足够的 representation capacity 使得 DAPT 反而引入 over-specialization？

---

## Missing References

论文在 Related Work 中的覆盖度是充分的：
- **Galinkin & Sablotny (2024)**: 已引用（Related Work, "Multi-turn defenses" paragraph），并明确区分了 single-turn detection vs. 本文的 multi-turn + systematic ablation
- **Echo Chamber Attack**: 已引用 (alobaid2026echochamber)
- **Representation Bending**: 已引用 (yousefpour2025repbend)

未发现关键性遗漏。Related Work 组织清晰（四段结构：attacks / defenses / persuasion-discourse / DAPT），准确反映了本文在领域中的定位。

---

## 格式合规性

| 项目 | 状态 | 备注 |
|------|------|------|
| Abstract ≤ 200 words | ✓ | ~177 words |
| 正文 ≤ 8 pages | ✓ | Sections 1–6 在 8 页内，Limitations 从第 9 页开始 |
| `\usepackage[review]{acl}` | ✓ | main.tex line 3 |
| Double-blind | ✓ | "Anonymous ACL submission"，无 author identity 泄露 |
| Limitations section | ✓ | 3 bullet points，覆盖 synthetic data / IID benign bound / scope，长度适当 |
| ARR Checklist | ✓ | 注释说明在 OpenReview form 中填写（main.tex line 41） |
| 引用格式 | ✓ | \citep / \citet 使用一致 |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2110 · 2026-05-24T13:28:40.306189+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "persuasion_turn_jailbreak_detect",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3.0 — Findings\n**一句话总结**: 实验设计扎实、ablation 彻底，但核心发现的增量新颖性有限——classification DAPT 优于 vanilla/MLM 在 Gururangan et al. (2020) 框架下基本可预测，而 ToxicChat 上的 hierarchy 反转显著削弱了核心叙事的普适性。\n\n### Must-Fix\n\n**N1** [critical] 核心 evidence hierarchy 的增量新颖性不足——需要更清楚地区分\"可预测\"与\"genuinely unexpected\"\n- 论文将三个发现统一标记为 \"unexpected\"，但 finding (i)——classification DAPT 大幅超越 vanilla/MLM——在 Gururangan et al. (2020) 的 DAPT 框架下是高度可预测的。真正新颖的是 (ii) scrambled-label equivalence 和 (iii) ToxicChat reversal，而非 evidence hierarchy 本身。\n- 建议：将 finding (i) 定位为 \"quantifying the magnitude\" 而非 \"unexpected\"，将 novelty 聚焦于机制分解和 boundary conditions。\n\n**N2** [critical] ToxicChat 反转对核心叙事的削弱未被充分处理\n- 在唯一的 human data 测试（ToxicChat）上，MLM（0.837）大幅超越 classification（0.596）。核心 take-away 被弱化为 \"adaptation strategy depends on data distribution\"——相当平凡的结论。\n- Section 5 的 \"the hierarchy reverses\" 处理太简略，需要更深入分析反转原因。\n- 建议：增加分析讨论、修改 Conclusion 为条件性结论、如果可能增加另一个 human data evaluation。\n\n### Should-Fix\n\n**W1** [warning] \"Evidence hierarchy\" 术语缺乏正式定义——首次使用时应加括号定义。\n\n**W2** [warning] Scrambled ≈ 9-class 的 \"counter-intuitive\" framing 需要推敲——在 discriminative compression 框架下其实是 expected 而非 counter-intuitive。ActorAttack 上 d=0.44 的差异应更突出讨论。\n\n**W3** [warning] Conclusion 中 \"reusable template\" 声称超出实证范围——仅在单一任务（multi-turn jailbreak detection）上用合成数据验证。\n\n**W4** [warning] BiGRU vs. mean pooling 的讨论过于简略——temporal aggregation 可能不必要，但仅一句话带过。\n\n### Questions\n\nQ1. ToxicChat 反转根因？single-turn 特性 vs distributional properties？\nQ2. ActorAttack 上 scrambled 与 correct labels 分歧的具体原因？\nQ3. 是否考虑过多 LLM 生成训练数据？\nQ4. RoBERTa-large DAPT counterproductive 的 scale-dependent 解释？\n\n### Missing References\n未发现关键遗漏。Galinkin & Sablotny (2024)、Echo Chamber、Representation Bending 均已引用。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "persuasion_turn_jailbreak_detect",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3.0 — Findings\n**一句话总结**: 实验设计扎实、ablation 彻底，但核心发现的增量新颖性有限——classification DAPT 优于 vanilla/MLM 在 Gururangan et al. (2020) 框架下基本可预测，而 ToxicChat 上的 hierarchy 反转显著削弱了核心叙事的普适性。\n\n### Must-Fix\n\n**N1** [critical] 核心 evidence hierarchy 的增量新颖性不足——需要更清楚地区分\"可预测\"与\"genuinely unexpected\"\n- 论文将三个发现统一标记为 \"unexpected\"，但 finding (i)——classification DAPT 大幅超越 vanilla/MLM——在 Gururangan et al. (2020) 的 DAPT 框架下是高度可预测的。真正新颖的是 (ii) scrambled-label equivalence 和 (iii) ToxicChat reversal，而非 evidence hierarchy 本身。\n- 建议：将 finding (i) 定位为 \"quantifying the magnitude\" 而非 \"unexpected\"，将 novelty 聚焦于机制分解和 boundary conditions。\n\n**N2** [critical] ToxicChat 反转对核心叙事的削弱未被充分处理\n- 在唯一的 human data 测试（ToxicChat）上，MLM（0.837）大幅超越 classification（0.596）。核心 take-away 被弱化为 \"adaptation strategy depends on data distribution\"——相当平凡的结论。\n- Section 5 的 \"the hierarchy reverses\" 处理太简略，需要更深入分析反转原因。\n- 建议：增加分析讨论、修改 Conclusion 为条件性结论、如果可能增加另一个 human data evaluation。\n\n### Should-Fix\n\n**W1** [warning] \"Evidence hierarchy\" 术语缺乏正式定义——首次使用时应加括号定义。\n\n**W2** [warning] Scrambled ≈ 9-class 的 \"counter-intuitive\" framing 需要推敲——在 discriminative compression 框架下其实是 expected 而非 counter-intuitive。ActorAttack 上 d=0.44 的差异应更突出讨论。\n\n**W3** [warning] Conclusion 中 \"reusable template\" 声称超出实证范围——仅在单一任务（multi-turn jailbreak detection）上用合成数据验证。\n\n**W4** [warning] BiGRU vs. mean pooling 的讨论过于简略——temporal aggregation 可能不必要，但仅一句话带过。\n\n### Questions\n\nQ1. ToxicChat 反转根因？single-turn 特性 vs distributional properties？\nQ2. ActorAttack 上 scrambled 与 correct labels 分歧的具体原因？\nQ3. 是否考虑过多 LLM 生成训练数据？\nQ4. RoBERTa-large DAPT counterproductive 的 scale-dependent 解释？\n\n### Missing References\n未发现关键遗漏。Galinkin & Sablotny (2024)、Echo Chamber、Representation Bending 均已引用。"
  }
}
```

</details>

---


### Tool result

_source line 2111 · 2026-05-24T13:29:05.820721+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25514
}
```

</details>

---


### Tool call

_source line 2112 · 2026-05-24T13:29:05.921984+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "persuasion_turn_jailbreak_detect",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.0 — Findings\n**一句话总结**: 消融设计思路新颖，但对话长度混淆未充分排除、核心 claim 的统计基础偏弱（3 seeds + TOST 在 ActorAttack 上失败）、WildChat 68.1% FPR 严重削弱泛化声明，整体距主会议接收有差距，适合 Findings。\n\n### Must-Fix\n\n**N1** [critical] 对话长度混淆未充分排除——benign 与 jailbreak 在 OOD 集上长度零重叠\n- benign 12-20 turns vs jailbreak 3-10 turns。BiGRU 输入序列长度与类别标签完美相关。\n- vanilla 失败（recall ≤2.6%）只能说明 vanilla 无法利用长度，不能排除 DAPT 后模型同时学到长度+内容组合特征。\n- 建议：长度匹配评估集、BiGRU 加长度扰动、报告 turn-count 与预测概率相关系数。\n\n**N2** [critical] \"Label semantics 不重要\" 在 ActorAttack 上不成立（TOST p=0.183, d=0.440）\n- Abstract \"not label semantics—drives generalization\" 未限定仅适用 template attacks。\n- 建议：修改 abstract 和 Section 4.3 措辞，明确限定适用范围。\n\n**N3** [critical] WildChat 68.1% FPR 严重削弱跨域泛化声明\n- 68% FPR 意味着部署前必须域适配，与 \"generalization\" 叙事有张力。\n- 建议：abstract 明确 \"cross-attack\" 指攻击类型泛化非域泛化；Conclusion 加入 WildChat FPR 作为主要限制。\n\n### Should-Fix\n\n**W1** [warning] TOST δ=5pp 的 practical significance 论证自相矛盾——论文自认 5pp \"materially influence deployment decisions\"，又用作等价阈值。\n\n**W2** [warning] 3 seeds 统计力不足，BCa bootstrap 池化违反独立性假设。\n\n**W3** [warning] Topic 变体失败存在混淆因素（类别数 5 vs 9）——建议补充 9→5 合并的控制实验。\n\n**W4** [warning] RoBERTa-large DAPT 反转解释不充分——解释了为什么 DAPT \"无用\" 但未解释为什么 \"有害\"。\n\n**W5** [warning] 1000 训练样本反常下降缺乏可信解释——推测 distributional heterogeneity 但无实验验证。\n\n### Questions\nQ1. BiGRU 是否能通过 turn count 直接区分？能否报告仅用 turn count 的 baseline F1？\nQ2. TOST 在 AA 上失败，为什么 abstract 仍将 \"structural role\" 作为核心发现？\nQ3. WildChat 68% FPR 根因——合成数据偏差 vs DeBERTa 领域漂移？\nQ4. 1000 样本下降是否所有 3 seeds 一致？\nQ5. RoBERTa-large DAPT 反转机制？CKA 分析能否提供线索？\n\n### Missing References\n未发现明显遗漏。可考虑补充 Perez and Wang (2022) red teaming 工作。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "persuasion_turn_jailbreak_detect",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.0 — Findings\n**一句话总结**: 消融设计思路新颖，但对话长度混淆未充分排除、核心 claim 的统计基础偏弱（3 seeds + TOST 在 ActorAttack 上失败）、WildChat 68.1% FPR 严重削弱泛化声明，整体距主会议接收有差距，适合 Findings。\n\n### Must-Fix\n\n**N1** [critical] 对话长度混淆未充分排除——benign 与 jailbreak 在 OOD 集上长度零重叠\n- benign 12-20 turns vs jailbreak 3-10 turns。BiGRU 输入序列长度与类别标签完美相关。\n- vanilla 失败（recall ≤2.6%）只能说明 vanilla 无法利用长度，不能排除 DAPT 后模型同时学到长度+内容组合特征。\n- 建议：长度匹配评估集、BiGRU 加长度扰动、报告 turn-count 与预测概率相关系数。\n\n**N2** [critical] \"Label semantics 不重要\" 在 ActorAttack 上不成立（TOST p=0.183, d=0.440）\n- Abstract \"not label semantics—drives generalization\" 未限定仅适用 template attacks。\n- 建议：修改 abstract 和 Section 4.3 措辞，明确限定适用范围。\n\n**N3** [critical] WildChat 68.1% FPR 严重削弱跨域泛化声明\n- 68% FPR 意味着部署前必须域适配，与 \"generalization\" 叙事有张力。\n- 建议：abstract 明确 \"cross-attack\" 指攻击类型泛化非域泛化；Conclusion 加入 WildChat FPR 作为主要限制。\n\n### Should-Fix\n\n**W1** [warning] TOST δ=5pp 的 practical significance 论证自相矛盾——论文自认 5pp \"materially influence deployment decisions\"，又用作等价阈值。\n\n**W2** [warning] 3 seeds 统计力不足，BCa bootstrap 池化违反独立性假设。\n\n**W3** [warning] Topic 变体失败存在混淆因素（类别数 5 vs 9）——建议补充 9→5 合并的控制实验。\n\n**W4** [warning] RoBERTa-large DAPT 反转解释不充分——解释了为什么 DAPT \"无用\" 但未解释为什么 \"有害\"。\n\n**W5** [warning] 1000 训练样本反常下降缺乏可信解释——推测 distributional heterogeneity 但无实验验证。\n\n### Questions\nQ1. BiGRU 是否能通过 turn count 直接区分？能否报告仅用 turn count 的 baseline F1？\nQ2. TOST 在 AA 上失败，为什么 abstract 仍将 \"structural role\" 作为核心发现？\nQ3. WildChat 68% FPR 根因——合成数据偏差 vs DeBERTa 领域漂移？\nQ4. 1000 样本下降是否所有 3 seeds 一致？\nQ5. RoBERTa-large DAPT 反转机制？CKA 分析能否提供线索？\n\n### Missing References\n未发现明显遗漏。可考虑补充 Perez and Wang (2022) red teaming 工作。"
  }
}
```

</details>

---


### Tool result

_source line 2113 · 2026-05-24T13:29:07.617873+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1695
}
```

</details>

---


### Assistant

_source line 2114 · 2026-05-24T13:29:13.935876+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 171

## Round 171

2 recorded events


### User

_source line 2115 · 2026-05-24T13:29:16.755879+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**总结**：Overall 3.0（Findings 级别）。论文的 controlled ablation 实验设计扎实（7 variants × 13 configs × 3 scales，TOST 等价检验），scrambled-label 发现有机制性洞见价值。但两个核心问题限制了评分：(1) classification DAPT > MLM > vanilla 这一核心发现在 Gururangan et al. (2020) 框架下基本可预测，论文需要更清楚地定位增量新颖性；(2) ToxicChat 上 hierarchy 反转（MLM 0.837 vs. classification 0.596）对核心叙事构成实质性削弱，当前讨论不够深入。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2116 · 2026-05-24T13:29:23.353901+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 172

## Round 172

6 recorded events


### User

_source line 2117 · 2026-05-24T13:30:30.181374+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix

**[AGREE] R2-N1: 核心 evidence hierarchy 的增量新颖性定位**

同意 R2 的判断。Classification DAPT 超越 vanilla/MLM 在 Gururangan et al. (2020) 的 DAPT 框架下确实是 largely predictable——该文已系统证明 task-adaptive pretraining 在多个 NLP 任务上优于 vanilla continued pretraining。论文将这一结果标记为三大 "unexpected findings" 之一（Section 1, page 2），在 novelty framing 上有拔高之嫌。

不过我认为论文的真正贡献不在于 "classification > MLM" 这个 ranking 本身，而在于：(1) scrambled-label equivalence 在 template attacks 上的成立（虽然如我在 R1-N2 中指出，这在 ActorAttack 上不成立）；(2) 定量分解了 domain exposure 和 classification supervision 各自的贡献量级（Section 4.3, Figure 3）；(3) boundary conditions 的发现（ToxicChat 反转、scale 效应）。R2 的建议——将 finding (i) 重新定位为 "quantifying the magnitude" 而非 "unexpected"——是务实可行的修改方向。

**[AGREE] R2-N2: ToxicChat 反转对核心叙事的削弱**

强烈同意。ToxicChat 是论文中**唯一的人类数据评估**（Table 5, Section 4.6），MLM 以 0.837 vs classification 0.596 大幅反超。这与我自己提出的 N3（WildChat 68.1% FPR）形成互补证据链：论文的核心叙事 "classification-based DAPT is the most robust variant" 在**所有真实数据场景**中都失效或大幅退化。

具体而言：
- 合成 OOD 数据：classification DAPT 表现最优（Table 2, Figure 2）
- ToxicChat（人类数据，单轮）：hierarchy 反转，MLM 最优（Table 5）
- WildChat（人类数据，多轮 benign）：68.1% FPR（Section 4.8, Table 20）

论文在 Section 5 用一句 "the hierarchy reverses on human-authored single-turn data" 带过（page 8），在 Conclusion (Section 6) 中重复了相同的一句话概括。这种处理深度不足以匹配问题的严重性。R2 建议增加分析讨论和条件性结论我完全赞同。

补充一个我的观察：论文在 Appendix H (Cross-LLM Validation) 中用 Llama-3 benign text 做了 cross-LLM 验证（Table 11），但这仍然是合成数据。真正需要的是第二个人类多轮数据源的验证——例如 ShareGPT 或 LMSYS-Chat 中的多轮对话。

---

### Should-Fix

**[AGREE] R2-W1: "Evidence hierarchy" 术语缺乏正式定义**

同意。"Evidence hierarchy" 从 Section 1 (page 1-2) 开始频繁使用，但首次出现时没有括号定义或正式说明。读者需要从上下文推断其含义为 "9-class > binary > scrambled > MLM-only > vanilla > Wiki-MLM > topic" 的性能排序。应在首次使用处加入明确定义。

**[REBUT] R2-W2: Scrambled ≈ 9-class 的 "counter-intuitive" framing**

部分反驳。R2 认为在 discriminative compression 框架下，scrambled labels 的有效性是 "expected" 的。我不完全同意这一判断：

1. Discriminative compression 的理论预测是**任何分类目标都能压缩表征空间**，但并不能预测**任意随机标签**的效果等价于**语义正确标签**。在标准 NLP pretraining 文献中，random labels 通常被视为 noise injection 而非有效训练信号（Zhang et al., 2021 关于 neural networks 记忆 random labels 的工作表明这会导致过拟合而非有用泛化）。
2. 因此，scrambled ≈ 9-class 在 template attacks 上的结果确实有一定 counter-intuitive 成分，至少对 NLP 社区的大部分读者而言。

但我同意 R2 关于 ActorAttack d=0.44 差异的观点——这与我在 R1-N2 中的发现完全一致。论文的 framing 问题不在于 "counter-intuitive" 是否合理，而在于**未充分限定此结论仅适用于 template attacks**。ActorAttack 上 TOST 失败（Appendix L, Table 16, p=0.183）应在正文中突出讨论，而非埋在附录。

**[AGREE] R2-W3: "Reusable template" 声称超出实证范围**

同意。论文在 Section 6 (Conclusion, page 8) 称 "This ablation framework provides a template for diagnosing when domain adaptation succeeds and fails in this safety-critical detection setting"，但实证基础仅限于单一任务（multi-turn jailbreak detection）、单一数据源（Qwen3-8B 合成数据）、单一 encoder 家族（DeBERTa-v3）。要声称 "reusable template"，至少需要在第二个安全检测任务（如 toxicity detection 或 misinformation detection）上验证框架的可迁移性。

**[AGREE] R2-W4: BiGRU vs mean pooling 讨论过于简略**

同意。Appendix T (Table 30) 提供了 BiGRU vs mean pooling 的对比数据，显示在 frozen probing 下二者差异在 CI 范围内（BiGRU 991±0.013 vs mean pooling 991±0.013 on DD-OOD），但在 E2E fine-tuning 下 mean pooling 全部收敛到 F1=1.000。这个发现本身值得在正文中用 1-2 句话讨论，因为它暗示 temporal order 在有充分表征质量时可能不是必需的——这与论文将 BiGRU 作为 Stage 2 核心组件的设计选择相关。

---

### Questions

**R2-Q1: ToxicChat 反转根因——single-turn 特性 vs distributional properties？**

我的判断倾向于**两者兼有**：(1) ToxicChat 是 single-turn 数据，而 classification DAPT 的 9-class 标签来自多轮说服策略分类，在单轮场景下这些策略标签的区分性可能失效；(2) ToxicChat 是 human-authored 数据，与 Qwen3-8B 生成的合成训练数据存在分布差异。论文的 Appendix U (Table 32) 中的 truncation 分析部分涉及这一问题，但没有直接隔离 single-turn vs distribution 因素。

要真正回答这个问题，作者可以：在 ToxicChat 数据上用多轮格式包装（padding with neutral turns），测试是否 classification DAPT 的性能恢复。如果恢复，则 single-turn 是主因；如果不恢复，则分布差异是主因。

**R2-Q2: ActorAttack 上 scrambled 与 correct labels 的分歧原因？**

这与我的 R1-N2 直接相关。我的假设是 ActorAttack 使用了更多样化的策略组合（论文称其 "employs more varied conversational strategies"，Section 4.3），而 correct labels 提供的策略语义信息在面对这种多样性时比 random labels 更有用——即 label semantics 在策略空间复杂时确实 matters。这本质上 **限定了** scrambled equivalence 的适用范围，应在正文中明确承认。

**R2-Q3: 多 LLM 生成训练数据？**

论文在 Section 4.5 (Mixed-LLM Training) 中已探索了 Qwen + Llama 的混合训练（Table 13），但这是用不同 LLM 生成**训练对话**，而非用不同 LLM 生成**评估数据**。我同意 R2 的隐含建议——使用 GPT-4、Claude 等不同 LLM 生成评估数据可以更好地验证泛化性。这与我的 R1 "单一合成数据源" 担忧一致。

**R2-Q4: RoBERTa-large DAPT counterproductive 的 scale-dependent 解释？**

这与我的 R1-W4 完全对齐。论文在 Section 4.4 和 Appendix K 中的解释（"sufficient capacity renders DAPT unnecessary"）只回答了 "为什么 DAPT 可能无用"，没有回答 "为什么 DAPT 有害"。我建议作者从灾难性遗忘或过度特化的角度提供机制性解释，或至少承认这是一个 open question。

---

### 总体评估

R2 的审稿与我的评估在以下方面高度一致：
1. **ToxicChat 反转 / 真实数据泛化问题**（R2-N2 ↔ R1-N3）
2. **Scrambled ≈ 9-class claim 的限定问题**（R2-W2 ↔ R1-N2）
3. **RoBERTa-large DAPT 反转解释不足**（R2-Q4 ↔ R1-W4）

R2 提出了我未覆盖的重要观点：**novelty framing** (N1) 和 **"reusable template" overclaim** (W3)。这两点我均同意。

综合两份审稿，我维持 **Overall 3.0 (Findings)** 的评分。核心问题集中在：(a) 真实数据上核心叙事失效（ToxicChat 反转 + WildChat FPR），(b) 长度混淆未控制（我的 R1-N1），(c) claim 超出实证范围（novelty framing + scrambled equivalence 限定）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2118 · 2026-05-24T13:30:48.433524+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_post_to_reviewer,get_external_review_status,get_visual_check_status,read_project_file,submit_review_report_to_research_director,update_review_issues,dispatch_visual_check,request_external_review,director_get_project_overview",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_post_to_reviewer,get_external_review_status,get_visual_check_status,read_project_file,submit_review_report_to_research_director,update_review_issues,dispatch_visual_check,request_external_review,director_get_project_overview",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2119 · 2026-05-24T13:30:48.544050+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 110
}
```

</details>

---


### Tool call

_source line 2120 · 2026-05-24T13:30:53.124196+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_get_project_overview",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_get_project_overview",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2121 · 2026-05-24T13:30:53.175321+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 2122 · 2026-05-24T13:31:27.229062+00:00_

收到 Reviewer 1 的交叉回应。R1 与 R2 在关键问题上高度收敛：

**共识达成的关键问题：**
- ToxicChat 反转 + 真实数据泛化（R2-N2 ↔ R1-N3）→ 双方均认为核心叙事在真实数据场景失效
- Novelty framing 拔高（R2-N1）→ R1 同意，建议重定位为 "quantifying magnitude"
- "Reusable template" overclaim（R2-W3）→ R1 同意
- RoBERTa-large DAPT 反转解释不足（R2-Q4 ↔ R1-W4）→ 双方一致

**唯一分歧点：**
- R2-W2（scrambled ≈ 9-class 是否 counter-intuitive）：R1 部分反驳，认为 random labels 有效性在 NLP 文献中确实非直觉，但同意 ActorAttack 上的分歧需在正文限定

等待 Reviewer 2 对 Reviewer 1 审稿意见的交叉回应，收到后进入收敛判断和报告合成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 173

## Round 173

2 recorded events


### User

_source line 2123 · 2026-05-24T13:31:30.243444+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- R2 的 6 条意见中，我 **AGREE** 了 5 条（N1 novelty framing、N2 ToxicChat 反转、W1 术语定义、W3 overclaim、W4 BiGRU 讨论不足），**部分 REBUT** 了 1 条（W2 scrambled framing——scrambled ≈ 9-class 对 NLP 社区多数读者仍有 counter-intuitive 成分，但同意 ActorAttack d=0.44 差异应更突出讨论）。
- R2 的审稿与我的评估在真实数据泛化、claim 限定、RoBERTa-large 解释三个方面高度一致，两份审稿共同指向 **3.0 (Findings)** 的评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2124 · 2026-05-24T13:31:55.173928+00:00_

Reviewer 1 交叉回应已收录。等待 Reviewer 2 对 Reviewer 1 审稿意见的交叉回应，收齐后进入 Step 4 报告合成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 174

## Round 174

16 recorded events


### User

_source line 2125 · 2026-05-24T13:31:56.702026+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[REBUT] R1-N1: 对话长度混淆未充分排除**

R1 的核心担忧（benign 12–20 turns vs. jailbreak 3–10 turns，BiGRU 可能利用长度线索）在原则上合理，但论文已提供了多层长度控制，R1 的审稿似乎低估了这些分析的覆盖度：

1. **Benign 截断验证**（Appendix V, Table 32 Part A）：将 12–20 turn benign 截断至 A=5 和 A=10（匹配 jailbreak 长度范围），FPR 始终为 0.000。如果模型依赖 turn count 区分类别，缩短 benign 应导致 FPR 上升——但完全没有。这是对 "长度 shortcut" 假设的直接反驳。
2. **Length-matched 评估**（Section 5）：N=155 length-matched 子集上 DD F1 变化仅 Δ=−2.5 pp。
3. **Jailbreak padding 实验**（Appendix V, Table 32 Part C）：将 jailbreak 对话用 benign turns 填充至 15+ turns——DD 和 FITD padded 后 F1 仍为 1.000，但 AA padded 下降 57.9 pp。论文正确将此归因于 signal dilution（benign padding 稀释了攻击信号）而非长度 shortcut 的移除。
4. **Length stratification**（Appendix U, Table 31）：按对话长度分层（1–3, 4–6, 7–10 turns），9-class recall 在所有 bins 无系统性退化。

然而，R1 建议的 **turn-count-only baseline F1**（Q1）确实是一个廉价且有说服力的额外控制。我认为这不是 must-fix（现有证据已充分排除长度 shortcut），但作为 rebuttal 补充实验会显著增强说服力。

**结论：降级为 Should-Fix。** 论文的长度控制已经相当全面，但 turn-count baseline 可以进一步封堵这个质疑。

---

**[AGREE] R1-N2: "Label semantics 不重要" 在 ActorAttack 上不成立**

同意。Abstract 中 "indicating the classification objective's structural role—not label semantics—drives generalization" 的措辞确实有歧义——"generalization" 未限定为 template attacks，读者可能理解为适用于所有攻击类型。而 TOST 在 ActorAttack 上 p=0.183, d=0.44，明确不满足等价条件。

Section 4.3 正文中有正确的限定（"while attacks employing more varied conversational strategies (ActorAttack) show a moderate label effect (d=0.44)"），但 abstract 缺乏此限定。

这与我自己的 W2 一致——建议 abstract 修改为 "not label semantics—drives generalization **on template attacks**" 或 "**for structurally consistent attack families**"。同时需要在 abstract 中提及 ActorAttack 上 scrambled ≠ 9-class 的差异，使核心 claim 更准确。

---

**[REBUT] R1-N3: WildChat 68.1% FPR 严重削弱跨域泛化声明**

R1 将 attack-side generalization 与 benign-side domain shift 混为一谈。论文的 "cross-attack generalization" 从一开始就被定义为攻击家族间的泛化（Section 1, contribution #1 明确分为 "attack-side and benign-side" 两个正交轴），而非跨域泛化。68.1% FPR 是 benign distribution shift 问题（合成 benign vs. WildChat real-world benign），不影响 attack-side OOD F1。

论文的处理逻辑是完整的：
1. **诊断**：WildChat FPR 68.1%（Section 4.8）
2. **解决方案**：Few-shot benign adaptation（10–25 conversations → FPR 0–1.5%）
3. **效率**：24.3× speedup over LLM-as-judge（Appendix O/Section 4.8）

Abstract 已包含 "few-shot benign adaptation reduces false-positive rates from 68% to 0%"，没有声称 zero-shot 跨域泛化。

但我同意 R1 的一个隐含观点：**abstract 和 conclusion 可以更明确地强调 "cross-attack" 指攻击家族泛化而非域泛化**，避免读者误解。这是 wording 层面的改进，不是 fundamental flaw。

**结论：降级为 Minor wording issue。**

---

### Should-Fix

**[AGREE] R1-W1: TOST δ=5pp practical significance 论证**

同意这是一个需要更好论证的方法论选择。如果 5pp 在 deployment 场景下有实际意义，用它做等价阈值确实自相矛盾。论文应在 Appendix L 中补充 δ 选择的理由——例如引用领域内类似控制实验的 equivalence margin 标准，或用 δ=3pp 做 sensitivity analysis。

---

**[REBUT] R1-W2: 3 seeds 统计力不足**

3 seeds 在 NLP/safety 领域的 encoder-level ablation 中是标准实践。论文报告 3-seed mean±std，且关键结论（classification DAPT > vanilla）的效应量极大（F1 差异 60+ pp），即使 3 seeds 也有充分统计力。BCa bootstrap 的独立性问题在技术上成立，但论文将 bootstrap 用于 confidence interval 而非 p-value，对结论影响有限。

真正需要更多 seeds 的是边际比较（如 scrambled vs. 9-class on ActorAttack, d=0.44），但论文已在此处承认 TOST 不通过（p=0.183），没有 overclaim。

**结论：当前统计实践对主要结论足够，但边际比较可受益于更多 seeds。**

---

**[AGREE] R1-W3: Topic 变体 5 vs. 9 类别混淆**

同意。Topic variant 用 5-class 分类而 9-class variant 用 9 categories（Table 1），类别数本身可能影响 compression 程度。如果 Topic 的失败是因为 5 classes 不足以产生足够的 discriminative compression（而非因为 topic labels 与 jailbreak detection 无关），那么论文的 "domain-relevant partitioning is necessary" 结论就不完全成立。

补充一个 9→5 class merging 的控制实验（将 9 个策略类别合并为 5 个）成本低且能直接回答这个问题。

---

**[AGREE] R1-W4: RoBERTa-large DAPT 反转——"无用" vs. "有害" 的解释缺口**

同意。Section 4.4 和 Section 5 解释了为什么大模型不需要 DAPT（vanilla 已有足够 capacity），但 9-class DAPT 在 AA 上 F1 从 1.000 降至 0.946 表明适应是 **actively harmful**，不仅仅是 unnecessary。可能的解释包括 over-specialization on training distribution 或 catastrophic forgetting of general features，但论文未提供证据区分这些假说。CKA 分析（Appendix S, Figure 6）可能提供线索——如果 DAPT 后 355M 的 CKA 结构显示 late-layer divergence，这支持 over-specialization 假说。

---

**[AGREE] R1-W5: 1000 样本反常下降**

同意。Appendix I (Table 9/10) 报告了 1000 样本时的性能下降，论文将其归因于 distributional heterogeneity，但这是推测而无实验验证。至少应报告 1000 样本时的训练 loss 曲线或 data composition 分析，以区分是过拟合、标签噪声还是分布变化。

---

### Questions

**[AGREE] R1-Q1:** Turn-count-only baseline 是一个低成本高价值的实验。虽然 Appendix V 的截断实验已间接排除了长度 shortcut，但 turn-count F1 作为 sanity check 更直接。

**[AGREE] R1-Q2:** 与 N2 一致——abstract 应限定 "structural role" 的适用范围为 template attacks。ActorAttack 上 d=0.44 表明策略多样性高的攻击确实需要正确的 label semantics。

**[REBUT] R1-Q3:** WildChat 68% FPR 的根因在论文中已有讨论。Section 5 指出 "Wikipedia MLM degrades by ~12 pp while jailbreak-domain MLM degrades by only 2.6 pp"，说明 domain specificity 是 FPR 升高的来源。Appendix P (Table 20) 在 226 WildChat conversations 上详细分析了 false positive 分布。但我同意论文可以更清楚地区分 "合成数据偏差" 和 "encoder 领域漂移" 各自的贡献。

**[AGREE] R1-Q4:** 1000 样本下降的 seed 一致性是验证该现象可靠性的基本信息，论文应报告。

**[AGREE] R1-Q5:** CKA 分析（Figure 6, Appendix S）确实可能提供 RoBERTa-large DAPT 反转的机制线索。如果论文已有 355M 的 CKA 数据但未讨论该 scale 的特殊 pattern，这是一个遗漏。

---

### Missing References

**[AGREE]** Perez and Wang (2022) red teaming 工作确实是相关引用。不过论文已引用 Perez et al. (2022) 的 red-teaming paradigm（Related Work, paragraph 1: "extending the automated red-teaming paradigm (Perez et al., 2022)"），需确认是否为同一工作。

---

### 总结

R1 的审稿整体质量较高，技术细节上的质疑有深度。我的主要分歧在于：

1. **N1（长度混淆）**：R1 低估了论文已有的长度控制（Appendix U, V），这些分析已充分排除长度 shortcut——建议降级为 Should-Fix。
2. **N3（WildChat FPR）**：R1 混淆了 attack-side 和 benign-side generalization，论文的 "cross-attack" claim 始终限定在攻击家族维度——建议降级为 Minor wording。
3. **N2, W1, W3, W4, W5**：同意 R1 的分析，这些都是论文需要在 rebuttal 或 camera-ready 中改进的方面。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2126 · 2026-05-24T13:32:22.168488+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 2127 · 2026-05-24T13:32:22.686658+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 518
}
```

</details>

---


### Tool call

_source line 2128 · 2026-05-24T13:32:22.687864+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 2129 · 2026-05-24T13:32:24.055369+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T13:20:25.659587+00:00\", \"completed_at\": \"2026-05-24T13:24:53.719515+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 9\", \"message\": \"Conclusion (Section 6) 正文溢出约 3-4 行到第 9 页顶部，之后才是 Limitations。EMNLP 2026 正文限 8 页（Limitations 不计入），当前 main text 微超 8 页。建议压缩 Discussion/Conclusion 将溢出行收回第 8 页，避免被 desk reject\"}, {\"severity\": \"warning\", \"dimension\": \"pages 3-5\", \"message\": \"第 3 页(Related Work)和第 5 页(Experiments Setup)均为纯文本页，中间仅第 4 页右栏有 Table 1。连续 3 页几乎无视觉锚点（Related Work 纯文本可接受，但加上第 5 页拉长了纯文本区间）。建议将 Figure 2 或某个关键表格前移至第 5 页\"}, {\"severity\": \"warning\", \"dimension\": \"page 15\", \"message\": \"Figure 5 三个 heatmap 并排，单元格内数值标注在 150dpi 下已经很小，打印尺寸下可能难以辨读。建议增大 cell 内字号或仅标注关键数值\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 架构图出现在第 2 页顶部，作为视觉锚点位置很好。Stage 1 → Stage 2 流程清晰，颜色对比度（红/绿/蓝）足够。Caption 自包含，审稿人可以快速理解核心 pipeline\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 bar chart 使用 6+ 种颜色区分方法。当前配色在彩色显示器上可区分，但灰度打印时部分颜色（如 orange vs brown）可能难以辨别。建议为不同方法增加 hatching/pattern 辅助区分\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 legend 使用小色块+文字，在单栏宽度下字号偏小。建议确认最终 print size 下 legend 仍可读\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 4 SVD scatter plot 单栏宽度，数据点标签较密。当前分辨率下仍可读，但边缘 case\"}, {\"severity\": \"info\", \"dimension\": \"page 16\", \"message\": \"Figure 6 CKA heatmap 和 Figure 7 t-SNE 都是单栏宽度，标注/数据点较小。作为 appendix 图可接受，但如果需要在正文引用，建议考虑全宽\"}, {\"severity\": \"info\", \"dimension\": \"page 25\", \"message\": \"最后一页（Table 38 + AI Assistants 声明后）约 45% 空白。作为 appendix 末页可接受\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"正文 4 figures + 5 tables = 9 个 display items / 8 页 ≈ 1.1/页，密度良好，符合实证论文标准\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"所有表格一致使用 booktabs 风格（无竖线），最优结果加粗标注，精度位数统一。排版专业\"}
…[truncated 226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1367
}
```

</details>

---


### Tool call

_source line 2130 · 2026-05-24T13:32:24.308476+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Read existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Read existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2131 · 2026-05-24T13:32:24.563720+00:00_

issues:
# === 历史 resolved issues（保留追踪记录，省略 mentions 细节）===
- id: R1-N1
  summary: Evidence hierarchy 统计基础不一致
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  mentions:
  - round: 1
    reviewers: [1, 2]
    note: binary/scrambled 仅 seed 42
  action_items:
  - round: 1
    action: 训练 binary/scrambled 3-seed
    assigned_to: main_agent
    status: resolved
  resolution: 'MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005'
  resolution_round: 1

- id: R1-N2
  summary: Three-layer robustness attribution 缺乏统计显著性
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  mentions:
  - round: 1
    reviewers: [1, 2]
    note: R1 首提 N2
  action_items:
  - round: 1
    action: McNemar's test + bootstrap CI
    assigned_to: main_agent
    status: resolved
  resolution: MF2 完成
  resolution_round: 1

- id: R1-N3
  summary: 缺少与已发表 multi-turn defense 的直接实验对比
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  mentions:
  - round: 1
    reviewers: [1, 2]
    note: R1 首提 N3
  - round: 2
    reviewers: [1, 2]
    note: Round 1 修复不充分，再次提出
  action_items:
  - round: 1
    action: 重构论证
    assigned_to: paper_agent
    status: resolved
  - round: 2
    action: Analysis paper reframe
    assigned_to: research_director
    status: resolved
  resolution: Analysis paper reframe 完成。
  resolution_round: 3

- id: R1-N4
  summary: 数据集规模过小
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  mentions:
  - round: 2
    reviewers: [1, 2]
    note: 500训练+76-118测试+3seeds仍不足
  action_items:
  - round: 2
    action: Bootstrap 95% CI + permutation test
    assigned_to: main_agent
    status: resolved
  resolution: exp9 BCa bootstrap 95% CI + paired permutation test 完成。
  resolution_round: 2

- id: R2-N3
  summary: 有效 OOD 评估实质上是 single-dataset
  category: experiment
 
…[truncated 23731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Bash",
  "elapsed_ms": 255
}
```

</details>

---


### Tool call

_source line 2132 · 2026-05-24T13:33:07.583000+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 2133 · 2026-05-24T13:33:07.636953+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 2134 · 2026-05-24T13:33:21.690788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
  "offset": "149",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
    "offset": "149",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2135 · 2026-05-24T13:33:21.892644+00:00_

149	   - **Detailed Comments**：逐节详细意见
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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2136 · 2026-05-24T13:42:35.037079+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "issues_yaml": "issues:\n# === 历史 resolved issues ===\n- id: R1-N1\n  summary: Evidence hierarchy 统计基础不一致\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: binary/scrambled 仅 seed 42\n  action_items:\n  - round: 1\n    action: 训练 binary/scrambled 3-seed\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005'\n  resolution_round: 1\n\n- id: R1-N2\n  summary: Three-layer robustness attribution 缺乏统计显著性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R1 首提 N2\n  action_items:\n  - round: 1\n    action: McNemar's test + bootstrap CI\n    assigned_to: main_agent\n    status: resolved\n  resolution: MF2 完成\n  resolution_round: 1\n\n- id: R1-N3\n  summary: 缺少与已发表 multi-turn defense 的直接实验对比\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R1 首提 N3\n  - round: 2\n    reviewers: [1, 2]\n    note: Round 1 修复不充分，再次提出\n  action_items:\n  - round: 1\n    action: 重构论证\n    assigned_to: paper_agent\n    status: resolved\n  - round: 2\n    action: Analysis paper reframe\n    assigned_to: research_director\n    status: resolved\n  resolution: Analysis paper reframe 完成。\n  resolution_round: 3\n\n- id: R1-N4\n  summary: 数据集规模过小\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 500训练+76-118测试+3seeds仍不足\n  action_items:\n  - round: 2\n    action: Bootstrap 95% CI + permutation test\n    assigned_to: main_agent\n    status: resolved\n  resolution: exp9 BCa bootstrap 95% CI + paired permutation test 完成。\n  resolution_round: 2\n\n- id: R2-N3\n  summary: 有效 OOD 评估实质上是 single-dataset\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R2 首提\n  action_items:\n  - round: 1\n    action: ActorAttack OOD 数据生成\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'EXP-2 完成: ActorAttack 118 conversations'\n  resolution_round: 1\n\n- id: R1-W1\n  summary: Mean pooling=BiGRU 结论基于 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: Paper Agent 已弱化。multi-seed 实验验证。\n  resolution_round: 1\n\n- id: R1-W3\n  summary: LLM-as-judge baseline 仅测 IID\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions: []\n  action_items: []\n  resolution: EXP-5 完成\n  resolution_round: 1\n\n- id: R1-W4\n  summary: TF-IDF LR 强表现未被充分讨论\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: TF-IDF per-prefix + ActorAttack 完成。\n  resolution_round: 3\n\n- id: R1-W5\n  summary: 可复现性不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions: []\n  action_items: []\n  resolution: Paper Agent 已添加 Appendix C\n  resolution_round: 1\n\n- id: R2-W1\n  summary: Abstract 过度堆砌数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: Abstract 压缩至 ~190 words。\n  resolution_round: 3\n\n- id: R2-W2\n  summary: partially falsified 叙事对接收不利\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: Framing 调整完成。\n  resolution_round: 3\n\n- id: R8-N4\n  summary: LLM-as-judge baseline 对比不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  mentions:\n  - round: 8\n    reviewers: [2]\n    note: GPT-5.5 不可解析可能是 prompt 设计问题\n  - round: 14\n    reviewers: [1, 2]\n    note: R14 两位 Reviewer 均指出 prompt 未提供、未尝试 prompt 优化\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items:\n  - round: 14\n    action: 附录提供 LLM-as-judge prompt 模板\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: 明确标注为 deployment cost comparison 而非方法论对比\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'R21验证: GPT F1标注\"upper bounds\"'\n  resolution_round: 21\n\n- id: R9-M1\n  summary: Abstract 中 Llama Guard 3 1.8% 有 misleading 风险\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. Abstract中Llama Guard 3缺\"zero-shot\"限定词'\n  action_items: []\n  resolution: Abstract 已使用 'zero-shot' 限定。\n  resolution_round: 22\n\n- id: R13-N2\n  summary: WildChat FPR=68.1% + few-shot 修复验证不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items:\n  - round: 19\n    action: 补充 few-shot benign adaptation 的实现细节\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'R21验证: few-shot实现细节完整(Stage-2 BiGRU, encoder frozen, N benign, BCE, 5 epochs)'\n  resolution_round: 21\n\n- id: R13-N3\n  summary: 机制解释缺乏直接证据\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items:\n  - round: 19\n    action: Section 5 讨论 discriminative compression vs representation collapse 替代解释\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'R21验证: 因果声明弱化为\"appears necessary\",\"consistent with\"'\n  resolution_round: 21\n\n- id: R13-W2\n  summary: DisPeD 命名 / 'Disentangled' 术语误用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Footnote 1清晰区分ablation methodology与disentangled representation learning'\n  resolution_round: 21\n\n- id: R13-W3\n  summary: Scrambled label AA 非等价 (d=0.44)\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: AA上d=0.44, TOST p=0.183明确标注'\n  resolution_round: 21\n\n- id: R13-W4\n  summary: Mixed-LLM AA=0.504 + MLM 崩溃\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 明确标注\"chance level, indistinguishable from majority baseline\"'\n  resolution_round: 21\n\n- id: R13-W6\n  summary: FITD 缺乏区分力\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions: []\n  action_items: []\n  resolution: R15 不再提出，视为已充分缓解。\n  resolution_round: 15\n\n- id: R14-W1\n  summary: BCa Bootstrap 跨 seed 池化\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 标注\"assumes cross-seed independence and is exploratory\"'\n  resolution_round: 21\n\n- id: R14-W2\n  summary: Benign-side 仅 WildChat 单一数据源\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: OASST2 双源验证解决。\n  resolution_round: 15\n\n- id: R14-W3\n  summary: Figure 2 缺失 ActorAttack\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: Figure 2 已增加 ActorAttack。\n  resolution_round: 15\n\n- id: R14-I1\n  summary: 主文 Conclusion 溢出到 page 9\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: Conclusion 确认在 page 8 内。\n  resolution_round: 15\n\n- id: R15-SF1\n  summary: 判别性压缩因果链不完整 + SVD 数据泄漏\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Discussion使用\"consistent with\"而非因果声明'\n  resolution_round: 21\n\n- id: R15-SF4\n  summary: C2 complexity-dependent boundary 证据基础狭窄\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions: []\n  action_items: []\n  resolution: R16-R19 不再单独提出。\n  resolution_round: 16\n\n- id: R15-SF6\n  summary: 方差缩减 4-20× 声明基于 n=3 seeds\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 改为\"descriptively 3-23×\"'\n  resolution_round: 21\n\n- id: R16-N1\n  summary: '''Any deterministic partition suffices'' 声称与 Topic 变体失败直接矛盾'\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 区分domain-relevant vs arbitrary classification, 指向Wiki-MLM vs JB-MLM为cleaner test'\n  resolution_round: 21\n\n- id: R16-W3\n  summary: Two-axis framework 新颖性争议\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: two-axis定位为organizational framework而非独立贡献'\n  resolution_round: 21\n\n- id: R16-W4\n  summary: 数据划分描述不够清晰\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 明确说明Stage 1用train+val, Stage 2用train/val/test'\n  resolution_round: 21\n\n- id: R17-N1\n  summary: n=3 seeds 方差缩减 claims 统计可靠性不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 同R15-SF6, 方差声明改为descriptive'\n  resolution_round: 21\n\n- id: R17-W2\n  summary: Cross-LLM Abstract 'remains robust' 与正文 'preliminary' 矛盾\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Abstract不再有\"remains robust\"'\n  resolution_round: 21\n\n- id: R17-W3\n  summary: RoBERTa-large DAPT 有害——核心 thesis scale-dependent\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 实验/讨论/结论三处承认scale-dependent并标注\"counterproductive at 355M\"'\n  resolution_round: 21\n\n- id: R18-N1\n  summary: '''Structural complexity'' 缺乏形式化定义'\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 操作化为transition rate<0.1(template) vs >0.3(complex)'\n  resolution_round: 21\n\n- id: R18-W1\n  summary: 缺少与已发表多轮检测方法的直接实验对比\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Related Work说明无公开实现, Appendix提供BERT-base proxy'\n  resolution_round: 21\n\n- id: R19-E1\n  summary: experiments.tex L114 \"$d<0.1$\" 数值错误 (应为 |d|≤0.14)\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED] 数值已修正'\n  action_items: []\n  resolution: 'R21验证: |d|≤0.14与Table一致'\n  resolution_round: 21\n\n- id: R19-E2\n  summary: intro L24 \"the first\" 缺少 \"to our knowledge\" 限定\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions: []\n  action_items: []\n  resolution: 当前文本已包含 \"to our knowledge\" 限定。\n  resolution_round: 20\n\n- id: R19-E3\n  summary: Abstract \"requires domain adaptation\" 与 RoBERTa-large vanilla AA=1.000 矛盾\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions: []\n  action_items: []\n  resolution: Abstract 已修改为 \"benefits substantially from\"。\n  resolution_round: 20\n\n- id: R20-N1\n  summary: 正文超过 8 页限制（Sections 1-6 占 9 页）\n  category: format\n  severity: critical\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: FALSE POSITIVE — Sections 1-6 在 p1-p8, Limitations (p9) 不计入限制。\n  - round: 23\n    reviewers: []\n    note: \"R23 视觉审查再次检测到 Conclusion 溢出 3-4 行至 page 9。可能是后续修改导致回归，需作者确认。\"\n  action_items: []\n  resolution: 'FALSE POSITIVE: 视觉验证确认正文恰好 8 页。R23 视觉审查检测到可能回归，待确认。'\n  resolution_round: 20\n\n- id: R20-N2\n  summary: Topic 变体控制设计存在 3 个未隔离混杂因素\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: method.tex和experiments.tex明确承认三个混杂因素, 指向Wiki-MLM vs JB-MLM'\n  resolution_round: 21\n\n- id: R20-N3\n  summary: Appendix Table 16 TOST 数据 (n=3) 与主文 (n=10) 不一致\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED] TOST扩展至n=10'\n  action_items: []\n  resolution: 'R21验证: 主文和附录统一为n=10 seeds'\n  resolution_round: 21\n\n# === Open / In-Progress issues (updated for Round 23) ===\n\n- id: R9-W1\n  summary: 长度混淆未充分排除\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 23\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: benign 12-20 turns vs jailbreak 3-10 turns 完全不重叠\n  - round: 16\n    reviewers: [1, 2]\n    note: R16 升级为 critical。R1 指出 adversarial padding 后 AA 暴跌 57pp。\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED] 两位Reviewer一致确认'\n  - round: 22\n    reviewers: [1]\n    note: \"R22 R1-N2 重新提出为 critical。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-N1 列为 Must-Fix。R2 交叉 REBUT→Should-Fix: 截断实验(Table 32 FPR=0.000)、length-matched(Δ=-2.5pp)、stratification(Table 31)已充分控制。但同意 turn-count-only baseline 可进一步封堵。Director 裁定 Should-Fix。\"\n  action_items:\n  - round: 15\n    action: 主文 Section 4 或 5 加 1-2 句长度混淆讨论\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: 构造长度匹配对照数据；Section 5 prominently 讨论 AA padding collapse\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: 提供 turn-count-only classifier F1 作为 sanity check\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R9-W2\n  summary: Human data 上 evidence hierarchy 完全反转 (ToxicChat)\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 23\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: ToxicChat JB-MLM=0.837 >> 9-class=0.596\n  - round: 17\n    reviewers: [1, 2]\n    note: R17 两位 Reviewer 均列为 critical。\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED] 两位Reviewer一致确认'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 两位 Reviewer 独立再次列为 Must-Fix。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 两位 Reviewer 再次独立列为 Must-Fix。R1-N3 + R2-N2 + 交叉均 AGREE。核心问题: 合成OOD hierarchy成立，但ToxicChat(人类单轮)反转 + WildChat(人类多轮benign) 68.1% FPR = 所有真实数据场景均失效。论文 Section 5/Conclusion 各一句话带过，处理深度不匹配。R1 补充: 需要第二个人类多轮数据源(ShareGPT/LMSYS-Chat)验证。\"\n  action_items:\n  - round: 18\n    action: 'D081 MF1: Abstract/Intro/Conclusion scope 系统性收窄'\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: Section 4.6 ToxicChat 反转从1句扩展为1-2段深入分析; Conclusion 给出条件性结论\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R13-N1\n  summary: 单一合成数据源限制跨攻击泛化声明可信度\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: 'R18 共识: disclosure 基本到位，但双重 OOD 评估缺失。'\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED] scope qualifier全面'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 两位 Reviewer 独立重新提出。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 继续存在。与 R9-W2(ToxicChat反转)、WildChat FPR 形成证据链: hierarchy 仅在合成数据生态系统内成立。R1 cross-response 补充需要第二个人类多轮数据源验证。结构性问题——即使完美修改 framing，主要 take-away 仍是 'DAPT hierarchy exists but only in synthetic settings'。\"\n  action_items:\n  - round: 17\n    action: W-1 Abstract F1 后加 '(attack-side OOD; benign IID)' 限定\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: Table 2 增加 dual-OOD 行；Abstract/Conclusion 所有 OOD F1 标注为 upper bound + IID benign 条件\n    assigned_to: main_agent\n    status: resolved\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W1\n  summary: 新颖性不足——DAPT 应用 + 增量贡献不清\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: 方法新颖性有限是阻碍 Conference 推荐的主要原因之一。\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] 降级为warning. 叙事一致但novelty argumentation深度不足'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R2-N1 列为 critical。R1 交叉 AGREE 但建议降为 major。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-N1 再次列为 critical: classification>MLM 可从 Gururangan 2020 预期。R1 交叉 AGREE 但补充因子分解/scrambled equivalence/boundary conditions 有增量贡献。共识: finding(i) 需从 'unexpected' 重新定位为 'quantifying the magnitude and conditions'。Director 裁定 Must-Fix for framing。\"\n  action_items:\n  - round: 18\n    action: 重写 novelty positioning 为消融发现集合\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: Section 1 将 finding(i) 从 'unexpected' 改为 'systematic quantification'; Abstract 相应调整\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W5\n  summary: Scale analysis 被架构差异混淆\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. DeBERTa vs RoBERTa混杂参数量, 建议Limitations加一句'\n  - round: 22\n    reviewers: [2]\n    note: \"R22 R2-W4: 仅 base-scale (125M-184M)。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 相关但不直接提及。R1-W4/R2-W4 讨论 RoBERTa-large DAPT 'harmful' 机制——新建 R23-W1 专门追踪。Scale 混杂本身未单独讨论。\"\n  action_items:\n  - round: 17\n    action: Discussion 增加 DAPT scale-dependent 效用讨论\n    assigned_to: main_agent\n    status: resolved\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W7\n  summary: Abstract 信息密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. Abstract信息密度高+句法模糊'\n  - round: 22\n    reviewers: [2]\n    note: \"R22 R2 小问题: Abstract 中 'this hierarchy reverses' 后的修饰对象不清。\"\n  - round: 23\n    reviewers: [2]\n    note: \"R23 R2 交叉回应中继续提及 abstract 句法模糊。与 R21-N1 同一问题。\"\n  action_items:\n  - round: 19\n    action: Abstract 压缩至 ~180 词\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R13-M1\n  summary: Missing references\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R2-W1 建议补充 Galinkin & Sablotny (2024)。\"\n  - round: 23\n    reviewers: [1]\n    note: \"R23 R1 建议补充 Perez and Wang (2022) red teaming 工作。R2 指出可能已引用 Perez et al. (2022)，需确认是否同一工作。\"\n  action_items:\n  - round: 22\n    action: 补充引用 Galinkin & Sablotny (2024) arXiv 2412.01547\n    assigned_to: main_agent\n    status: open\n  - round: 23\n    action: 确认 Perez and Wang (2022) 是否已引用或需补充\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R14-N1\n  summary: 数据规模扩大后性能反常下降 (350→1000)\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] should-fix. 9-class也下降(0.994→0.889), 未给出解释'\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W5 再次提出。R2 交叉 AGREE。应报告 training loss 曲线、data composition 分析或 seed 一致性验证。\"\n  action_items:\n  - round: 17\n    action: 弱化为 composition differences partially confound\n    assigned_to: main_agent\n    status: in_progress\n  - round: 23\n    action: 报告 1000 样本的 seed 一致性、training loss 或 data composition 证据\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R15-VIS1\n  summary: Figure 2 尺寸偏小，axis labels 约正文字号 50-60%\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. Figure 2 axis labels仍偏小'\n  - round: 22\n    reviewers: [1]\n    note: \"R22 R1 小问题 M4: Figure 1 的 Stage-1 七个 variant 图示拥挤。\"\n  - round: 23\n    reviewers: []\n    note: \"R23 Reviewer 未单独提及。视觉审查标注 Figure 5 heatmap 标注过小(p15)、Figure 3 legend 字号偏小(p7)。\"\n  action_items:\n  - round: 15\n    action: Figure 2 字号放大至≥8pt\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R16-W1\n  summary: Temporal modeling negative finding 讨论不足\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R1-W3: BiGRU 对 mean pooling 无优势(Table 30)。R2 交叉 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W3 再次提出 + R2-W4 AGREE。E2E fine-tuning 下两者均收敛 F1=1.000。暗示 temporal order 非必需。共识: 正文需明确说明 BiGRU 可被 mean pooling 替代。\"\n  action_items:\n  - round: 19\n    action: Discussion 讨论为什么 multi-turn 攻击的检测不需要时序建模\n    assigned_to: main_agent\n    status: resolved\n  - round: 22\n    action: Section 3.3 或 Section 5 明确说明 BiGRU 可被 mean pooling 替代且不影响检测性能\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R16-W2\n  summary: 效率对比定位不清\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[STILL_OPEN] minor. R1指出Introduction已标注43×, 但Abstract未标注'\n  - round: 23\n    reviewers: []\n    note: \"R23 未提及，可能已修复，待 Research Director 确认。\"\n  action_items:\n  - round: 16\n    action: 效率对比加 deployment cost comparison 限定\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W1\n  summary: TOST δ=5pp margin 缺乏 practical significance 论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. δ=5pp缺practical significance论证'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R1-W1 + R2 交叉 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W1 再次提出: F1>0.95区间5pp差异=miss rate数倍变化。R2 交叉 AGREE。共识: 方法论改进空间，不改变定性结论。建议补充 domain-specific justification 或 δ=3pp sensitivity analysis。\"\n  action_items:\n  - round: 17\n    action: Appendix TOST 部分增加 domain-specific practical significance 论证\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M1\n  summary: 'Missing references: ADEPT, Echo Chamber Attack, Representation Bending'\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. ADEPT/Echo Chamber/RepBending未引用'\n  - round: 23\n    reviewers: []\n    note: \"R23 未单独提及，可能已修复，待 Research Director 确认。\"\n  action_items:\n  - round: 17\n    action: 核实引用真实性和相关性\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R21-N1\n  summary: Abstract第二长句句法模糊——\"this hierarchy reverses\"后的修饰对象不清\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: 'NEW-1: \"on labeled multi-turn jailbreak data\"修饰对象歧义'\n  - round: 22\n    reviewers: [2]\n    note: \"R22 仍存在。\"\n  - round: 23\n    reviewers: [2]\n    note: \"R23 R2 交叉回应中继续提及。与 R13-W7 合并关注。\"\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R1-W2\n  summary: 策略标注质量验证不充分\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 23\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: R16 两位 Reviewer 均再次指出 κ=0.78 n=50 不足\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R1-W4: 50样本9类→部分类别仅2-5个验证样本。R2 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W4 再次提出。R2 交叉 AGREE。scrambled 实验缓解对检测结论的影响，但 Appendix Y 策略预测(90.1%)直接受限于标注质量。共识: 增加样本至≥100并报告per-class κ。\"\n  action_items:\n  - round: 1\n    action: Limitations 已添加 caveat\n    assigned_to: main_agent\n    status: resolved\n  - round: 22\n    action: 增加标注验证样本量至≥100并报告per-class κ; Appendix Y caveat标注质量\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R22-N1\n  summary: Scrambled≈9-class 等价性能与论文叙事的张力\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R1-W2 首提: scrambled 在 DD/FTTD 上与 9-class TOST 等价。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-N2 列为 Must-Fix: TOST 在 ActorAttack 上 p=0.183 d=0.44 失败，Abstract 'label semantics don't matter' 未限定 template attacks。R2 交叉 AGREE。R1 交叉部分 REBUT R2-W2: scrambled≈9-class 对 NLP 社区仍 counter-intuitive(random labels 通常视为 noise injection)，但同意 ActorAttack 例外需突出。共识: Abstract 需限定为 template attacks。\"\n  action_items:\n  - round: 22\n    action: Section 5 增加段落讨论 classification objective structure vs label semantics\n    assigned_to: main_agent\n    status: open\n  - round: 23\n    action: Abstract 修改 \"not label semantics—drives generalization\" 为限定 template attacks 的表述\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R22-W1\n  summary: 自创术语过多且定义不严谨——evidence hierarchy, discriminative compression 等\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R2-W2 首提。R1 交叉部分 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-W1 再次提出 'evidence hierarchy' 缺正式定义。R1 交叉 AGREE 并建议改为 'performance ranking'。共识: 首次使用处需一句话定义。\"\n  action_items:\n  - round: 22\n    action: 首次使用时给出一句话定义; 考虑将 'evidence hierarchy' 改为 'performance ranking'\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R22-W2\n  summary: Conclusion 'reusable template' claim 超出单一任务的实验范围\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R2-W3 首提。R1 交叉 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-W3 再次提出。R1 交叉 AGREE: 单一任务+单一数据源+单一encoder。共识: 限定为 'template for future controlled studies of domain adaptation in safety-critical NLP tasks'。\"\n  action_items:\n  - round: 22\n    action: Conclusion 限定 'reusable template' 的适用范围\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n# === Round 23 新增 issues ===\n\n- id: R23-W1\n  summary: RoBERTa-large DAPT \"有害\"机制未解释——\"unnecessary\" vs \"harmful\" 解释缺口\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1-W4 + R2-W4 AGREE: Section 4.4 解释了 'unnecessary'(vanilla capacity足够)，但 9-class DAPT 在 AA 上 F1 从 1.000→0.946 = actively harmful。可能机制: over-specialization 或 catastrophic forgetting，但无证据区分。CKA(Figure 6)可能有线索但未讨论。\"\n  action_items:\n  - round: 23\n    action: Section 4.4 或 Section 5 区分 DAPT 'unnecessary' 和 'harmful' 的机制; 讨论 CKA 分析对 355M 的发现\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R23-W2\n  summary: Topic 变体 5 vs 9 类别数量混淆——failure 可能因类别数不足而非标签无关\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1-W3 首提 + R2 交叉 AGREE: Topic 用 5-class 而 9-class 用 9 categories(Table 1)。如果 Topic 失败是因为 5 classes 不足以产生 discriminative compression，则 'domain-relevant partitioning is necessary' 结论不完全成立。建议 9→5 class merging 控制实验。\"\n  action_items:\n  - round: 23\n    action: 补充 9→5 class merging 控制实验，或在 Limitations 中承认类别数量混淆\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "issues_yaml": "issues:\n# === 历史 resolved issues ===\n- id: R1-N1\n  summary: Evidence hierarchy 统计基础不一致\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: binary/scrambled 仅 seed 42\n  action_items:\n  - round: 1\n    action: 训练 binary/scrambled 3-seed\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005'\n  resolution_round: 1\n\n- id: R1-N2\n  summary: Three-layer robustness attribution 缺乏统计显著性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R1 首提 N2\n  action_items:\n  - round: 1\n    action: McNemar's test + bootstrap CI\n    assigned_to: main_agent\n    status: resolved\n  resolution: MF2 完成\n  resolution_round: 1\n\n- id: R1-N3\n  summary: 缺少与已发表 multi-turn defense 的直接实验对比\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R1 首提 N3\n  - round: 2\n    reviewers: [1, 2]\n    note: Round 1 修复不充分，再次提出\n  action_items:\n  - round: 1\n    action: 重构论证\n    assigned_to: paper_agent\n    status: resolved\n  - round: 2\n    action: Analysis paper reframe\n    assigned_to: research_director\n    status: resolved\n  resolution: Analysis paper reframe 完成。\n  resolution_round: 3\n\n- id: R1-N4\n  summary: 数据集规模过小\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 500训练+76-118测试+3seeds仍不足\n  action_items:\n  - round: 2\n    action: Bootstrap 95% CI + permutation test\n    assigned_to: main_agent\n    status: resolved\n  resolution: exp9 BCa bootstrap 95% CI + paired permutation test 完成。\n  resolution_round: 2\n\n- id: R2-N3\n  summary: 有效 OOD 评估实质上是 single-dataset\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R2 首提\n  action_items:\n  - round: 1\n    action: ActorAttack OOD 数据生成\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'EXP-2 完成: ActorAttack 118 conversations'\n  resolution_round: 1\n\n- id: R1-W1\n  summary: Mean pooling=BiGRU 结论基于 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: Paper Agent 已弱化。multi-seed 实验验证。\n  resolution_round: 1\n\n- id: R1-W3\n  summary: LLM-as-judge baseline 仅测 IID\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions: []\n  action_items: []\n  resolution: EXP-5 完成\n  resolution_round: 1\n\n- id: R1-W4\n  summary: TF-IDF LR 强表现未被充分讨论\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: TF-IDF per-prefix + ActorAttack 完成。\n  resolution_round: 3\n\n- id: R1-W5\n  summary: 可复现性不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions: []\n  action_items: []\n  resolution: Paper Agent 已添加 Appendix C\n  resolution_round: 1\n\n- id: R2-W1\n  summary: Abstract 过度堆砌数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: Abstract 压缩至 ~190 words。\n  resolution_round: 3\n\n- id: R2-W2\n  summary: partially falsified 叙事对接收不利\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: Framing 调整完成。\n  resolution_round: 3\n\n- id: R8-N4\n  summary: LLM-as-judge baseline 对比不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  mentions:\n  - round: 8\n    reviewers: [2]\n    note: GPT-5.5 不可解析可能是 prompt 设计问题\n  - round: 14\n    reviewers: [1, 2]\n    note: R14 两位 Reviewer 均指出 prompt 未提供、未尝试 prompt 优化\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items:\n  - round: 14\n    action: 附录提供 LLM-as-judge prompt 模板\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: 明确标注为 deployment cost comparison 而非方法论对比\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'R21验证: GPT F1标注\"upper bounds\"'\n  resolution_round: 21\n\n- id: R9-M1\n  summary: Abstract 中 Llama Guard 3 1.8% 有 misleading 风险\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. Abstract中Llama Guard 3缺\"zero-shot\"限定词'\n  action_items: []\n  resolution: Abstract 已使用 'zero-shot' 限定。\n  resolution_round: 22\n\n- id: R13-N2\n  summary: WildChat FPR=68.1% + few-shot 修复验证不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items:\n  - round: 19\n    action: 补充 few-shot benign adaptation 的实现细节\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'R21验证: few-shot实现细节完整(Stage-2 BiGRU, encoder frozen, N benign, BCE, 5 epochs)'\n  resolution_round: 21\n\n- id: R13-N3\n  summary: 机制解释缺乏直接证据\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items:\n  - round: 19\n    action: Section 5 讨论 discriminative compression vs representation collapse 替代解释\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'R21验证: 因果声明弱化为\"appears necessary\",\"consistent with\"'\n  resolution_round: 21\n\n- id: R13-W2\n  summary: DisPeD 命名 / 'Disentangled' 术语误用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Footnote 1清晰区分ablation methodology与disentangled representation learning'\n  resolution_round: 21\n\n- id: R13-W3\n  summary: Scrambled label AA 非等价 (d=0.44)\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: AA上d=0.44, TOST p=0.183明确标注'\n  resolution_round: 21\n\n- id: R13-W4\n  summary: Mixed-LLM AA=0.504 + MLM 崩溃\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 明确标注\"chance level, indistinguishable from majority baseline\"'\n  resolution_round: 21\n\n- id: R13-W6\n  summary: FITD 缺乏区分力\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions: []\n  action_items: []\n  resolution: R15 不再提出，视为已充分缓解。\n  resolution_round: 15\n\n- id: R14-W1\n  summary: BCa Bootstrap 跨 seed 池化\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 标注\"assumes cross-seed independence and is exploratory\"'\n  resolution_round: 21\n\n- id: R14-W2\n  summary: Benign-side 仅 WildChat 单一数据源\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: OASST2 双源验证解决。\n  resolution_round: 15\n\n- id: R14-W3\n  summary: Figure 2 缺失 ActorAttack\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: Figure 2 已增加 ActorAttack。\n  resolution_round: 15\n\n- id: R14-I1\n  summary: 主文 Conclusion 溢出到 page 9\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: Conclusion 确认在 page 8 内。\n  resolution_round: 15\n\n- id: R15-SF1\n  summary: 判别性压缩因果链不完整 + SVD 数据泄漏\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Discussion使用\"consistent with\"而非因果声明'\n  resolution_round: 21\n\n- id: R15-SF4\n  summary: C2 complexity-dependent boundary 证据基础狭窄\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions: []\n  action_items: []\n  resolution: R16-R19 不再单独提出。\n  resolution_round: 16\n\n- id: R15-SF6\n  summary: 方差缩减 4-20× 声明基于 n=3 seeds\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 改为\"descriptively 3-23×\"'\n  resolution_round: 21\n\n- id: R16-N1\n  summary: '''Any deterministic partition suffices'' 声称与 Topic 变体失败直接矛盾'\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 区分domain-relevant vs arbitrary classification, 指向Wiki-MLM vs JB-MLM为cleaner test'\n  resolution_round: 21\n\n- id: R16-W3\n  summary: Two-axis framework 新颖性争议\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: two-axis定位为organizational framework而非独立贡献'\n  resolution_round: 21\n\n- id: R16-W4\n  summary: 数据划分描述不够清晰\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 明确说明Stage 1用train+val, Stage 2用train/val/test'\n  resolution_round: 21\n\n- id: R17-N1\n  summary: n=3 seeds 方差缩减 claims 统计可靠性不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 同R15-SF6, 方差声明改为descriptive'\n  resolution_round: 21\n\n- id: R17-W2\n  summary: Cross-LLM Abstract 'remains robust' 与正文 'preliminary' 矛盾\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Abstract不再有\"remains robust\"'\n  resolution_round: 21\n\n- id: R17-W3\n  summary: RoBERTa-large DAPT 有害——核心 thesis scale-dependent\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 实验/讨论/结论三处承认scale-dependent并标注\"counterproductive at 355M\"'\n  resolution_round: 21\n\n- id: R18-N1\n  summary: '''Structural complexity'' 缺乏形式化定义'\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 操作化为transition rate<0.1(template) vs >0.3(complex)'\n  resolution_round: 21\n\n- id: R18-W1\n  summary: 缺少与已发表多轮检测方法的直接实验对比\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Related Work说明无公开实现, Appendix提供BERT-base proxy'\n  resolution_round: 21\n\n- id: R19-E1\n  summary: experiments.tex L114 \"$d<0.1$\" 数值错误 (应为 |d|≤0.14)\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED] 数值已修正'\n  action_items: []\n  resolution: 'R21验证: |d|≤0.14与Table一致'\n  resolution_round: 21\n\n- id: R19-E2\n  summary: intro L24 \"the first\" 缺少 \"to our knowledge\" 限定\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions: []\n  action_items: []\n  resolution: 当前文本已包含 \"to our knowledge\" 限定。\n  resolution_round: 20\n\n- id: R19-E3\n  summary: Abstract \"requires domain adaptation\" 与 RoBERTa-large vanilla AA=1.000 矛盾\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions: []\n  action_items: []\n  resolution: Abstract 已修改为 \"benefits substantially from\"。\n  resolution_round: 20\n\n- id: R20-N1\n  summary: 正文超过 8 页限制（Sections 1-6 占 9 页）\n  category: format\n  severity: critical\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: FALSE POSITIVE — Sections 1-6 在 p1-p8, Limitations (p9) 不计入限制。\n  - round: 23\n    reviewers: []\n    note: \"R23 视觉审查再次检测到 Conclusion 溢出 3-4 行至 page 9。可能是后续修改导致回归，需作者确认。\"\n  action_items: []\n  resolution: 'FALSE POSITIVE: 视觉验证确认正文恰好 8 页。R23 视觉审查检测到可能回归，待确认。'\n  resolution_round: 20\n\n- id: R20-N2\n  summary: Topic 变体控制设计存在 3 个未隔离混杂因素\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: method.tex和experiments.tex明确承认三个混杂因素, 指向Wiki-MLM vs JB-MLM'\n  resolution_round: 21\n\n- id: R20-N3\n  summary: Appendix Table 16 TOST 数据 (n=3) 与主文 (n=10) 不一致\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED] TOST扩展至n=10'\n  action_items: []\n  resolution: 'R21验证: 主文和附录统一为n=10 seeds'\n  resolution_round: 21\n\n# === Open / In-Progress issues (updated for Round 23) ===\n\n- id: R9-W1\n  summary: 长度混淆未充分排除\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 23\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: benign 12-20 turns vs jailbreak 3-10 turns 完全不重叠\n  - round: 16\n    reviewers: [1, 2]\n    note: R16 升级为 critical。R1 指出 adversarial padding 后 AA 暴跌 57pp。\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED] 两位Reviewer一致确认'\n  - round: 22\n    reviewers: [1]\n    note: \"R22 R1-N2 重新提出为 critical。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-N1 列为 Must-Fix。R2 交叉 REBUT→Should-Fix: 截断实验(Table 32 FPR=0.000)、length-matched(Δ=-2.5pp)、stratification(Table 31)已充分控制。但同意 turn-count-only baseline 可进一步封堵。Director 裁定 Should-Fix。\"\n  action_items:\n  - round: 15\n    action: 主文 Section 4 或 5 加 1-2 句长度混淆讨论\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: 构造长度匹配对照数据；Section 5 prominently 讨论 AA padding collapse\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: 提供 turn-count-only classifier F1 作为 sanity check\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R9-W2\n  summary: Human data 上 evidence hierarchy 完全反转 (ToxicChat)\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 23\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: ToxicChat JB-MLM=0.837 >> 9-class=0.596\n  - round: 17\n    reviewers: [1, 2]\n    note: R17 两位 Reviewer 均列为 critical。\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED] 两位Reviewer一致确认'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 两位 Reviewer 独立再次列为 Must-Fix。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 两位 Reviewer 再次独立列为 Must-Fix。R1-N3 + R2-N2 + 交叉均 AGREE。核心问题: 合成OOD hierarchy成立，但ToxicChat(人类单轮)反转 + WildChat(人类多轮benign) 68.1% FPR = 所有真实数据场景均失效。论文 Section 5/Conclusion 各一句话带过，处理深度不匹配。R1 补充: 需要第二个人类多轮数据源(ShareGPT/LMSYS-Chat)验证。\"\n  action_items:\n  - round: 18\n    action: 'D081 MF1: Abstract/Intro/Conclusion scope 系统性收窄'\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: Section 4.6 ToxicChat 反转从1句扩展为1-2段深入分析; Conclusion 给出条件性结论\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R13-N1\n  summary: 单一合成数据源限制跨攻击泛化声明可信度\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: 'R18 共识: disclosure 基本到位，但双重 OOD 评估缺失。'\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED] scope qualifier全面'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 两位 Reviewer 独立重新提出。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 继续存在。与 R9-W2(ToxicChat反转)、WildChat FPR 形成证据链: hierarchy 仅在合成数据生态系统内成立。R1 cross-response 补充需要第二个人类多轮数据源验证。结构性问题——即使完美修改 framing，主要 take-away 仍是 'DAPT hierarchy exists but only in synthetic settings'。\"\n  action_items:\n  - round: 17\n    action: W-1 Abstract F1 后加 '(attack-side OOD; benign IID)' 限定\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: Table 2 增加 dual-OOD 行；Abstract/Conclusion 所有 OOD F1 标注为 upper bound + IID benign 条件\n    assigned_to: main_agent\n    status: resolved\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W1\n  summary: 新颖性不足——DAPT 应用 + 增量贡献不清\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: 方法新颖性有限是阻碍 Conference 推荐的主要原因之一。\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] 降级为warning. 叙事一致但novelty argumentation深度不足'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R2-N1 列为 critical。R1 交叉 AGREE 但建议降为 major。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-N1 再次列为 critical: classification>MLM 可从 Gururangan 2020 预期。R1 交叉 AGREE 但补充因子分解/scrambled equivalence/boundary conditions 有增量贡献。共识: finding(i) 需从 'unexpected' 重新定位为 'quantifying the magnitude and conditions'。Director 裁定 Must-Fix for framing。\"\n  action_items:\n  - round: 18\n    action: 重写 novelty positioning 为消融发现集合\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: Section 1 将 finding(i) 从 'unexpected' 改为 'systematic quantification'; Abstract 相应调整\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W5\n  summary: Scale analysis 被架构差异混淆\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. DeBERTa vs RoBERTa混杂参数量, 建议Limitations加一句'\n  - round: 22\n    reviewers: [2]\n    note: \"R22 R2-W4: 仅 base-scale (125M-184M)。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 相关但不直接提及。R1-W4/R2-W4 讨论 RoBERTa-large DAPT 'harmful' 机制——新建 R23-W1 专门追踪。Scale 混杂本身未单独讨论。\"\n  action_items:\n  - round: 17\n    action: Discussion 增加 DAPT scale-dependent 效用讨论\n    assigned_to: main_agent\n    status: resolved\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W7\n  summary: Abstract 信息密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. Abstract信息密度高+句法模糊'\n  - round: 22\n    reviewers: [2]\n    note: \"R22 R2 小问题: Abstract 中 'this hierarchy reverses' 后的修饰对象不清。\"\n  - round: 23\n    reviewers: [2]\n    note: \"R23 R2 交叉回应中继续提及 abstract 句法模糊。与 R21-N1 同一问题。\"\n  action_items:\n  - round: 19\n    action: Abstract 压缩至 ~180 词\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R13-M1\n  summary: Missing references\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R2-W1 建议补充 Galinkin & Sablotny (2024)。\"\n  - round: 23\n    reviewers: [1]\n    note: \"R23 R1 建议补充 Perez and Wang (2022) red teaming 工作。R2 指出可能已引用 Perez et al. (2022)，需确认是否同一工作。\"\n  action_items:\n  - round: 22\n    action: 补充引用 Galinkin & Sablotny (2024) arXiv 2412.01547\n    assigned_to: main_agent\n    status: open\n  - round: 23\n    action: 确认 Perez and Wang (2022) 是否已引用或需补充\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R14-N1\n  summary: 数据规模扩大后性能反常下降 (350→1000)\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] should-fix. 9-class也下降(0.994→0.889), 未给出解释'\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W5 再次提出。R2 交叉 AGREE。应报告 training loss 曲线、data composition 分析或 seed 一致性验证。\"\n  action_items:\n  - round: 17\n    action: 弱化为 composition differences partially confound\n    assigned_to: main_agent\n    status: in_progress\n  - round: 23\n    action: 报告 1000 样本的 seed 一致性、training loss 或 data composition 证据\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R15-VIS1\n  summary: Figure 2 尺寸偏小，axis labels 约正文字号 50-60%\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. Figure 2 axis labels仍偏小'\n  - round: 22\n    reviewers: [1]\n    note: \"R22 R1 小问题 M4: Figure 1 的 Stage-1 七个 variant 图示拥挤。\"\n  - round: 23\n    reviewers: []\n    note: \"R23 Reviewer 未单独提及。视觉审查标注 Figure 5 heatmap 标注过小(p15)、Figure 3 legend 字号偏小(p7)。\"\n  action_items:\n  - round: 15\n    action: Figure 2 字号放大至≥8pt\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R16-W1\n  summary: Temporal modeling negative finding 讨论不足\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R1-W3: BiGRU 对 mean pooling 无优势(Table 30)。R2 交叉 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W3 再次提出 + R2-W4 AGREE。E2E fine-tuning 下两者均收敛 F1=1.000。暗示 temporal order 非必需。共识: 正文需明确说明 BiGRU 可被 mean pooling 替代。\"\n  action_items:\n  - round: 19\n    action: Discussion 讨论为什么 multi-turn 攻击的检测不需要时序建模\n    assigned_to: main_agent\n    status: resolved\n  - round: 22\n    action: Section 3.3 或 Section 5 明确说明 BiGRU 可被 mean pooling 替代且不影响检测性能\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R16-W2\n  summary: 效率对比定位不清\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[STILL_OPEN] minor. R1指出Introduction已标注43×, 但Abstract未标注'\n  - round: 23\n    reviewers: []\n    note: \"R23 未提及，可能已修复，待 Research Director 确认。\"\n  action_items:\n  - round: 16\n    action: 效率对比加 deployment cost comparison 限定\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W1\n  summary: TOST δ=5pp margin 缺乏 practical significance 论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. δ=5pp缺practical significance论证'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R1-W1 + R2 交叉 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W1 再次提出: F1>0.95区间5pp差异=miss rate数倍变化。R2 交叉 AGREE。共识: 方法论改进空间，不改变定性结论。建议补充 domain-specific justification 或 δ=3pp sensitivity analysis。\"\n  action_items:\n  - round: 17\n    action: Appendix TOST 部分增加 domain-specific practical significance 论证\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M1\n  summary: 'Missing references: ADEPT, Echo Chamber Attack, Representation Bending'\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. ADEPT/Echo Chamber/RepBending未引用'\n  - round: 23\n    reviewers: []\n    note: \"R23 未单独提及，可能已修复，待 Research Director 确认。\"\n  action_items:\n  - round: 17\n    action: 核实引用真实性和相关性\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R21-N1\n  summary: Abstract第二长句句法模糊——\"this hierarchy reverses\"后的修饰对象不清\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: 'NEW-1: \"on labeled multi-turn jailbreak data\"修饰对象歧义'\n  - round: 22\n    reviewers: [2]\n    note: \"R22 仍存在。\"\n  - round: 23\n    reviewers: [2]\n    note: \"R23 R2 交叉回应中继续提及。与 R13-W7 合并关注。\"\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R1-W2\n  summary: 策略标注质量验证不充分\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 23\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: R16 两位 Reviewer 均再次指出 κ=0.78 n=50 不足\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R1-W4: 50样本9类→部分类别仅2-5个验证样本。R2 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W4 再次提出。R2 交叉 AGREE。scrambled 实验缓解对检测结论的影响，但 Appendix Y 策略预测(90.1%)直接受限于标注质量。共识: 增加样本至≥100并报告per-class κ。\"\n  action_items:\n  - round: 1\n    action: Limitations 已添加 caveat\n    assigned_to: main_agent\n    status: resolved\n  - round: 22\n    action: 增加标注验证样本量至≥100并报告per-class κ; Appendix Y caveat标注质量\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R22-N1\n  summary: Scrambled≈9-class 等价性能与论文叙事的张力\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R1-W2 首提: scrambled 在 DD/FTTD 上与 9-class TOST 等价。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-N2 列为 Must-Fix: TOST 在 ActorAttack 上 p=0.183 d=0.44 失败，Abstract 'label semantics don't matter' 未限定 template attacks。R2 交叉 AGREE。R1 交叉部分 REBUT R2-W2: scrambled≈9-class 对 NLP 社区仍 counter-intuitive(random labels 通常视为 noise injection)，但同意 ActorAttack 例外需突出。共识: Abstract 需限定为 template attacks。\"\n  action_items:\n  - round: 22\n    action: Section 5 增加段落讨论 classification objective structure vs label semantics\n    assigned_to: main_agent\n    status: open\n  - round: 23\n    action: Abstract 修改 \"not label semantics—drives generalization\" 为限定 template attacks 的表述\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R22-W1\n  summary: 自创术语过多且定义不严谨——evidence hierarchy, discriminative compression 等\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R2-W2 首提。R1 交叉部分 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-W1 再次提出 'evidence hierarchy' 缺正式定义。R1 交叉 AGREE 并建议改为 'performance ranking'。共识: 首次使用处需一句话定义。\"\n  action_items:\n  - round: 22\n    action: 首次使用时给出一句话定义; 考虑将 'evidence hierarchy' 改为 'performance ranking'\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R22-W2\n  summary: Conclusion 'reusable template' claim 超出单一任务的实验范围\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R2-W3 首提。R1 交叉 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-W3 再次提出。R1 交叉 AGREE: 单一任务+单一数据源+单一encoder。共识: 限定为 'template for future controlled studies of domain adaptation in safety-critical NLP tasks'。\"\n  action_items:\n  - round: 22\n    action: Conclusion 限定 'reusable template' 的适用范围\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n# === Round 23 新增 issues ===\n\n- id: R23-W1\n  summary: RoBERTa-large DAPT \"有害\"机制未解释——\"unnecessary\" vs \"harmful\" 解释缺口\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1-W4 + R2-W4 AGREE: Section 4.4 解释了 'unnecessary'(vanilla capacity足够)，但 9-class DAPT 在 AA 上 F1 从 1.000→0.946 = actively harmful。可能机制: over-specialization 或 catastrophic forgetting，但无证据区分。CKA(Figure 6)可能有线索但未讨论。\"\n  action_items:\n  - round: 23\n    action: Section 4.4 或 Section 5 区分 DAPT 'unnecessary' 和 'harmful' 的机制; 讨论 CKA 分析对 355M 的发现\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R23-W2\n  summary: Topic 变体 5 vs 9 类别数量混淆——failure 可能因类别数不足而非标签无关\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1-W3 首提 + R2 交叉 AGREE: Topic 用 5-class 而 9-class 用 9 categories(Table 1)。如果 Topic 失败是因为 5 classes 不足以产生 discriminative compression，则 'domain-relevant partitioning is necessary' 结论不完全成立。建议 9→5 class merging 控制实验。\"\n  action_items:\n  - round: 23\n    action: 补充 9→5 class merging 控制实验，或在 Limitations 中承认类别数量混淆\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 2137 · 2026-05-24T13:42:35.188640+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml\", \"bytes\": 29192}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2138 · 2026-05-24T13:45:19.889440+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 23 审稿报告\n\n## Summary\n\n本文对 DeBERTa-v3 在多轮越狱检测任务上的 7 种领域自适应预训练（DAPT）策略进行了系统性消融研究，建立了从 vanilla continued pretraining 到 9-class persuasion strategy classification 的性能梯度（\"evidence hierarchy\"），并发现 scrambled labels 在 template attacks 上与正确标签等效。论文还报告了 ToxicChat 人类数据上 hierarchy 反转、RoBERTa-large 规模下 DAPT 反效果等 boundary conditions。实验设计全面（7 variants × 2 evaluation axes × 3 seeds × 2 encoders），但核心叙事在真实数据场景中受到严重削弱。\n\n## Strengths\n\n**S1: 系统性消融设计。** 7 种 DAPT 变体构成完整的因子分解光谱（vanilla → Wiki-MLM → JB-MLM → topic → binary → scrambled → 9-class），每个步骤隔离一个实验因素。这种设计在安全检测领域罕见。\n\n**S2: 两轴评估框架。** 将泛化能力分解为 attack-side OOD（跨攻击家族）和 benign-side OOD（跨 benign 分布）两个正交维度，结构清晰，便于定位失败模式。\n\n**S3: Boundary conditions 的诚实报告。** ToxicChat 反转、RoBERTa-large DAPT 反效果、ActorAttack 上 scrambled ≠ 9-class 等 negative/boundary results 均在论文中呈现，没有选择性报告。\n\n**S4: Scrambled label 等价性发现。** 在 template attacks（DangerousDialogues, FITD）上 scrambled labels 与正确 9-class labels 的 TOST 等价检验通过（p<0.05, |d|≤0.14），这一发现对理解 DAPT 机制有启示——classification objective 的结构性角色比标签语义更重要（在适用范围内）。\n\n**S5: 实验基础设施质量。** 10-seed TOST、BCa bootstrap CI、CKA/SVD 表征分析、多粒度长度控制实验等统计和分析手段丰富，方法论意识强。\n\n**S6: 实用部署价值。** 与 LLM-as-judge 相比 24-43× 推理加速，few-shot benign adaptation 仅需 10-25 条对话即可将 WildChat FPR 从 68% 降至 0-1.5%，具备实际部署潜力。\n\n## Weaknesses\n\n### Must-Fix\n\n**MF1 [共识]: ToxicChat hierarchy 反转严重削弱核心叙事。**\nToxicChat 是论文唯一的人类数据评估（Table 5, Section 4.6），MLM 以 F1=0.837 大幅超越 classification F1=0.596。论文核心叙事 \"classification-based DAPT is the most robust variant\" 在人类数据上质的反转。论文在 Section 5 和 Conclusion 各用一句话带过，处理深度与问题严重性不匹配。综合 WildChat 68.1% FPR（Section 4.8），论文的核心 hierarchy 在**所有真实数据场景**中均失效或严重退化：\n- 合成 OOD 数据：hierarchy 成立\n- ToxicChat（人类数据，单轮）：hierarchy 反转\n- WildChat（人类数据，多轮 benign）：68.1% FPR\n\n需要增加对 ToxicChat 反转的深入分析（至少 1-2 段），并在 Conclusion 中给出条件性结论而非一句话概括。[R1-N3 ↔ R2-N2, 两位 AGREE]\n\n**MF2 [共识]: Abstract 中 \"label semantics\" claim 范围未限定。**\nAbstract 称 \"indicating the classification objective's structural role—not label semantics—drives generalization\"，但 TOST 在 ActorAttack 上失败（p=0.183, d=0.44, Appendix L Table 16）。\"Generalization\" 未限定为 template attacks，读者可能误解为适用于所有攻击类型。Section 4.3 正文有正确限定，但 Abstract 缺失。需修改为 \"drives generalization **on template attacks**\" 或 \"**for structurally consistent attack families**\"。[R1-N2 ↔ R2 cross AGREE]\n\n**MF3 [共识，严重程度有分歧]: 核心 evidence hierarchy 增量新颖性定位过高。**\nClassification DAPT 优于 vanilla/MLM 在 Gururangan et al. (2020) 的 DAPT 框架下是 largely predictable——该文已系统证明 task-adaptive pretraining 在多个 NLP 任务上优于 vanilla continued pretraining。论文将此结果标记为三大 \"unexpected findings\" 之一（Section 1, page 2），novelty framing 有拔高之嫌。论文的真正贡献在于因子分解的定量化（domain exposure vs classification supervision 的贡献量级、boundary conditions、scrambled equivalence），而非 hierarchy 排序本身。建议将 finding (i) 重新定位为 \"quantifying the magnitude and conditions\" 而非 \"unexpected\"。[R2-N1 critical + R1 cross AGREE but prefers major. Director 判定: Must-Fix for framing]\n\n### Should-Fix\n\n**SF1 [分歧裁定]: 对话长度混淆——现有控制充分但缺直接 baseline。**\nBenign 12-20 turns vs jailbreak 3-10 turns 的长度差异是潜在混淆因素。论文已提供截断验证（Appendix V, Table 32 Part A: 截断后 FPR=0.000）、length-matched 子集（N=155, ΔF1=-2.5pp）、length stratification（Appendix U, Table 31: 无系统性退化）。R2 认为这些控制已充分排除长度 shortcut；R1 认为 turn-count-only baseline F1 是更直接的反驳。**Director 裁定: Should-Fix**——现有控制合理但非决定性，一个简单的 turn-count classifier 可一步封堵此质疑。[R1-N1 Must-Fix vs R2 Should-Fix]\n\n**SF2 [分歧裁定]: WildChat 68.1% FPR——合成数据训练的根本局限。**\nR1 将此视为跨域泛化失败；R2 指出论文的 \"cross-attack generalization\" 始终限定在攻击家族维度而非域泛化。R2 的论证在技术上正确——abstract 已标注 few-shot adaptation，没有声称 zero-shot 跨域泛化。**Director 裁定: Should-Fix**——68.1% FPR 不构成 soundness 问题，但暴露了合成 benign 训练数据的系统性偏差，应在 Discussion 中更明确讨论。需第二个人类多轮数据源（如 ShareGPT 或 LMSYS-Chat）的验证。[R1-N3 Must-Fix vs R2 Minor]\n\n**SF3 [共识]: TOST δ=5pp 缺乏 practical significance 论证。**\n在 F1>0.95 的区间，5pp 差异意味着 miss rate 的数倍变化——如果 5pp 在部署场景下有实际意义，用它做等价阈值则自相矛盾。应补充 domain-specific practical significance 论证或 δ=3pp sensitivity analysis。[R1-W1 + R2 AGREE]\n\n**SF4 [共识]: Topic 变体 5 vs 9 类别数量混淆。**\nTopic variant 用 5-class 分类而 9-class variant 用 9 categories（Table 1）。Topic 的失败可能因为 5 classes 不足以产生足够的 discriminative compression，而非因为 topic labels 与 jailbreak detection 无关。一个 9→5 class merging 控制实验成本低且能直接回答这个问题。[R1-W3 + R2 AGREE]\n\n**SF5 [共识]: RoBERTa-large DAPT \"有害\" 机制未解释。**\nSection 4.4 和 Section 5 解释了为什么大模型不需要 DAPT（vanilla capacity 足够），但 9-class DAPT 在 AA 上 F1 从 1.000→0.946 表明 DAPT 是 actively harmful，不仅仅是 unnecessary。可能的机制（over-specialization、catastrophic forgetting）未被区分。CKA 分析（Appendix S, Figure 6）可能提供线索但未被讨论。[R1-W4 + R2-W4 AGREE]\n\n**SF6 [共识]: 1000 样本性能反常下降未解释。**\nAppendix I (Table 9/10) 报告 1000 样本时的性能下降，论文归因于 distributional heterogeneity，但无实验验证。应报告 1000 样本的 training loss 曲线、data composition 分析或 seed 一致性验证。[R1-W5 + R2 AGREE]\n\n**SF7 [共识]: \"Evidence hierarchy\" 术语缺乏正式定义。**\n从 Section 1 (page 1-2) 开始频繁使用但首次出现时无明确定义。读者需从上下文推断含义。R1 进一步指出该术语暗示超出经验排序的理论地位，建议改为 \"performance ranking\"。应在首次使用处加入操作性定义。[R2-W1 + R1 AGREE]\n\n**SF8 [共识]: Conclusion \"reusable template\" claim 超出实证范围。**\nSection 6 声称 \"This ablation framework provides a template for diagnosing when domain adaptation succeeds and fails in this safety-critical detection setting\"，但实证基础仅限于单一任务、单一数据源、单一 encoder 家族。应限定为 \"template for future controlled studies of domain adaptation in safety-critical NLP tasks\"。[R2-W3 + R1 AGREE]\n\n**SF9 [共识]: BiGRU vs mean pooling 讨论不足。**\nAppendix T (Table 30) 显示 frozen probing 下 BiGRU 和 mean pooling 差异在 CI 范围内，E2E fine-tuning 下均收敛到 F1=1.000。这暗示 temporal order 在充分表征质量下非必需，与论文将 BiGRU 作为 Stage 2 核心组件的设计选择相关。应在正文明确说明 BiGRU 可被 mean pooling 替代且不影响检测性能。[R1-W3 + R2-W4 AGREE]\n\n**SF10 [共识]: 策略标注质量验证不足。**\n50 样本验证 9 个类别，部分类别仅 2-5 个验证样本，κ=0.78 在此粒度下可靠性不足。Scrambled 实验缓解了对主要检测结论的影响，但 Appendix Y 策略预测准确率（90.1%）受标注质量直接限制。建议增加验证样本至≥100 并报告 per-class κ。[R1-W4 + R2 AGREE]\n\n### Minor\n\n**M1: Abstract 句法模糊。** \"this hierarchy reverses\" 后的修饰对象不清晰，需要重写以消除歧义。[R2, 跨轮持续存在]\n\n**M2: Scrambled ≈ 9-class 发现的叙事定位。** 该发现可能是论文最具洞察力的结果，但当前论文将其作为 hierarchy 排序的补充讨论，而非核心贡献。建议在 Section 5 增加段落讨论 classification objective structure vs label semantics 的机制意涵。[R1-W2 ↔ R2-W2]\n\n## Reviewer Consensus\n\n以下关键问题两位 Reviewer 完全一致：\n1. ToxicChat hierarchy 反转是论文最大的 narrative concern（MF1）\n2. Abstract \"label semantics\" claim 需限定到 template attacks（MF2）\n3. Scrambled ≈ 9-class 在 ActorAttack 上不成立（d=0.44, TOST p=0.183）\n4. \"Reusable template\" overclaim 需限定范围（SF8）\n5. RoBERTa-large DAPT 反转缺乏机制解释（SF5）\n6. BiGRU 可被 mean pooling 替代（SF9）\n7. Overall 3.0 (Findings) 评分\n\n## Reviewer Divergence\n\n**分歧 1: 长度混淆严重程度** — R1 列为 Must-Fix（turn-count shortcut 可能性未排除）；R2 列为 Should-Fix（Appendix U/V 的截断、length-matched、stratification 实验已充分控制）。Director 裁定 Should-Fix：现有控制合理，但 turn-count-only baseline 可一步封堵。\n\n**分歧 2: WildChat 68.1% FPR 严重程度** — R1 列为 Must-Fix（跨域泛化声明严重削弱）；R2 列为 Minor wording（论文从未声称跨域泛化，attack-side 和 benign-side 是正交轴）。Director 裁定 Should-Fix：R2 技术上正确但 68.1% FPR 暴露合成数据训练的系统性偏差，需更充分讨论。\n\n**分歧 3 (minor): Scrambled \"counter-intuitive\" framing** — R2 认为在 discriminative compression 框架下可预期；R1 认为对 NLP 社区多数读者仍具 counter-intuitive 成分（random labels 在标准 NLP 文献中被视为 noise injection 而非有效训练信号）。Director 判断 R1 更准确——scrambled ≈ 9-class 确有 counter-intuitive 价值，但 ActorAttack 例外需在正文突出。\n\n## Questions\n\n**Q1:** 作者能否提供一个 turn-count-only classifier 的 F1 作为 sanity check？这是一个零成本实验，可以彻底排除长度 shortcut 质疑。\n\n**Q2:** ToxicChat 反转的根因是 single-turn 特性还是 distributional properties？作者能否将 ToxicChat 数据用多轮格式包装（padding with neutral turns）测试 classification DAPT 是否恢复？\n\n**Q3:** RoBERTa-large 上 9-class DAPT 导致 AA F1 从 1.000 降至 0.946 的机制是什么？CKA 分析（Figure 6）能否提供线索？\n\n**Q4:** 1000 样本性能下降是否在 3 个 seeds 中一致出现？训练 loss 曲线是否显示过拟合迹象？\n\n**Q5:** 如果将 9-class 策略标签合并为 5 个类别，性能是否下降至 topic variant 水平？这可以区分类别数量和标签相关性的各自贡献。\n\n## Missing References\n\n- **Galinkin & Sablotny (2024)**. \"Improved LLM Jailbreak Detection via Pretrained Embeddings.\" arXiv:2412.01547. 最直接相关的已发表工作——同样使用预训练 encoder embeddings 进行越狱检测。两位 Reviewer 共识应补充。[R22 遗留]\n- **Perez and Wang (2022)** red teaming 工作。R1 建议补充，R2 指出论文可能已引用 Perez et al. (2022)，需确认是否为同一工作。\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 9 info items）。\n\n**Warnings:**\n1. **[Page 9] Conclusion 溢出**: Section 6 (Conclusion) 正文溢出约 3-4 行到第 9 页顶部，之后才是 Limitations。EMNLP 2026 正文限 8 页（Limitations 不计入）。**注意**: Round 20 曾将类似报告标记为 FALSE POSITIVE（\"Sections 1-6 在 p1-p8\"），本轮视觉审查重新检测到溢出——可能是后续修改导致的回归。建议作者确认 Section 6 最后一行是否在第 8 页内，若确实溢出需压缩 Discussion/Conclusion。\n2. **[Pages 3-5] 纯文本区间过长**: Related Work (p3) + Experiments Setup (p5) 均为纯文本，中间仅 p4 右栏有 Table 1，连续 3 页缺乏视觉锚点。建议将 Figure 2 或某关键表格前移。\n3. **[Page 15] Figure 5 heatmap 标注过小**: 三个 heatmap 并排，cell 内数值在 150dpi 下偏小，打印可能难辨。\n\n**Info 亮点**: Figure 1 架构图位置好（p2 顶部）、全文表格 booktabs 风格统一、未发现 LaTeX 渲染错误或未解析引用。正文 display item 密度 1.1/页，符合实证论文标准。\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n**置信度: 4/5 (High)**\n\n本文是一项全面、系统的消融研究，实验设计质量高，分析工具丰富。但以下因素阻碍其达到 Conference (4.0) 水平：\n\n1. **核心叙事在真实数据上失效**: ToxicChat hierarchy 反转 + WildChat 68.1% FPR 表明论文的 \"evidence hierarchy\" 仅在合成数据生态系统内成立。这不是 soundness 缺陷（论文报告了这些结果），但严重限制了结论的实际影响力。\n2. **方法新颖性有限**: 论文本质上是将已知的 DAPT 范式（Gururangan et al., 2020）应用于新领域，方法层面无创新。其贡献在于 empirical findings（scrambled equivalence、boundary conditions），但这些发现中的核心一条（classification > MLM ranking）可从先行工作预期。\n3. **Claims 多处超出实证范围**: \"reusable template\"（单一任务）、\"label semantics don't matter\"（仅 template attacks）、\"unexpected\"（可预期）等表述需要系统性收窄。\n\n**为何不低于 3.0**: 实验执行质量高，因子分解设计在安全检测领域有参考价值，scrambled label equivalence 和 boundary conditions 的发现对社区有实用启示。论文作为 Findings paper 的贡献足够。\n\n**为何不高于 3.0**: 核心叙事的真实数据泛化失败是结构性问题而非措辞问题——即使完美修改 framing，论文的主要 take-away 仍然是 \"DAPT hierarchy exists but only in synthetic settings\"，这限制了 impact。方法新颖性不足以支撑 Conference 推荐。\n\n## Detailed Comments\n\n### Abstract\n- \"indicating the classification objective's structural role—not label semantics—drives generalization\" 需限定为 template attacks（MF2）\n- \"this hierarchy reverses\" 句法模糊，修饰对象不清（M1）\n- 三大 \"unexpected findings\" 中的 finding (i) 应降格为 \"quantifying the magnitude\"（MF3）\n\n### Section 1 (Introduction)\n- \"Evidence hierarchy\" 首次使用处需操作性定义（SF7）\n- 三大贡献的 novelty framing 需调整——contribution #1 从 \"unexpected\" 改为 \"systematic quantification\"（MF3）\n\n### Section 3 (Method)\n- BiGRU 选择理由需补充说明——正文应明确 mean pooling 可替代（SF9）\n\n### Section 4.3 (Evidence Hierarchy)\n- 正文有 ActorAttack d=0.44 的限定，但 abstract 缺失——需保持一致（MF2）\n- Topic 5-class vs 9-class 类别数量混淆需讨论或补充控制实验（SF4）\n\n### Section 4.4 (Scale Effects)\n- \"DAPT unnecessary at 355M\" 需区分 \"unnecessary\" vs \"harmful\"，讨论 CKA 线索（SF5）\n\n### Section 4.6 (ToxicChat)\n- 需从 1 句话扩展为 1-2 段深入分析，隔离 single-turn vs distributional 因素（MF1）\n\n### Section 4.7 (Data Scale)\n- 1000 样本下降需补充 seed 一致性和 training loss 证据（SF6）\n\n### Section 5 (Discussion)\n- 增加 scrambled equivalence 的机制讨论段落（M2）\n- WildChat FPR 作为合成数据训练局限的讨论需更充分（SF2）\n\n### Section 6 (Conclusion)\n- \"reusable template\" 限定范围（SF8）\n- ToxicChat 反转的条件性结论需加深（MF1）\n- 检查是否溢出到 page 9（Visual Check Warning #1）\n\n### Appendix\n- TOST δ=5pp 补充 practical significance 论证（SF3）\n- 策略标注验证样本量增加至≥100，报告 per-class κ（SF10）\n- 确认 Galinkin & Sablotny (2024) 和 Perez and Wang (2022) 引用状态",
  "project": "persuasion_turn_jailbreak_detect",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_613965f45d48763f375aa83e9294b24a"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 23 审稿报告\n\n## Summary\n\n本文对 DeBERTa-v3 在多轮越狱检测任务上的 7 种领域自适应预训练（DAPT）策略进行了系统性消融研究，建立了从 vanilla continued pretraining 到 9-class persuasion strategy classification 的性能梯度（\"evidence hierarchy\"），并发现 scrambled labels 在 template attacks 上与正确标签等效。论文还报告了 ToxicChat 人类数据上 hierarchy 反转、RoBERTa-large 规模下 DAPT 反效果等 boundary conditions。实验设计全面（7 variants × 2 evaluation axes × 3 seeds × 2 encoders），但核心叙事在真实数据场景中受到严重削弱。\n\n## Strengths\n\n**S1: 系统性消融设计。** 7 种 DAPT 变体构成完整的因子分解光谱（vanilla → Wiki-MLM → JB-MLM → topic → binary → scrambled → 9-class），每个步骤隔离一个实验因素。这种设计在安全检测领域罕见。\n\n**S2: 两轴评估框架。** 将泛化能力分解为 attack-side OOD（跨攻击家族）和 benign-side OOD（跨 benign 分布）两个正交维度，结构清晰，便于定位失败模式。\n\n**S3: Boundary conditions 的诚实报告。** ToxicChat 反转、RoBERTa-large DAPT 反效果、ActorAttack 上 scrambled ≠ 9-class 等 negative/boundary results 均在论文中呈现，没有选择性报告。\n\n**S4: Scrambled label 等价性发现。** 在 template attacks（DangerousDialogues, FITD）上 scrambled labels 与正确 9-class labels 的 TOST 等价检验通过（p<0.05, |d|≤0.14），这一发现对理解 DAPT 机制有启示——classification objective 的结构性角色比标签语义更重要（在适用范围内）。\n\n**S5: 实验基础设施质量。** 10-seed TOST、BCa bootstrap CI、CKA/SVD 表征分析、多粒度长度控制实验等统计和分析手段丰富，方法论意识强。\n\n**S6: 实用部署价值。** 与 LLM-as-judge 相比 24-43× 推理加速，few-shot benign adaptation 仅需 10-25 条对话即可将 WildChat FPR 从 68% 降至 0-1.5%，具备实际部署潜力。\n\n## Weaknesses\n\n### Must-Fix\n\n**MF1 [共识]: ToxicChat hierarchy 反转严重削弱核心叙事。**\nToxicChat 是论文唯一的人类数据评估（Table 5, Section 4.6），MLM 以 F1=0.837 大幅超越 classification F1=0.596。论文核心叙事 \"classification-based DAPT is the most robust variant\" 在人类数据上质的反转。论文在 Section 5 和 Conclusion 各用一句话带过，处理深度与问题严重性不匹配。综合 WildChat 68.1% FPR（Section 4.8），论文的核心 hierarchy 在**所有真实数据场景**中均失效或严重退化：\n- 合成 OOD 数据：hierarchy 成立\n- ToxicChat（人类数据，单轮）：hierarchy 反转\n- WildChat（人类数据，多轮 benign）：68.1% FPR\n\n需要增加对 ToxicChat 反转的深入分析（至少 1-2 段），并在 Conclusion 中给出条件性结论而非一句话概括。[R1-N3 ↔ R2-N2, 两位 AGREE]\n\n**MF2 [共识]: Abstract 中 \"label semantics\" claim 范围未限定。**\nAbstract 称 \"indicating the classification objective's structural role—not label semantics—drives generalization\"，但 TOST 在 ActorAttack 上失败（p=0.183, d=0.44, Appendix L Table 16）。\"Generalization\" 未限定为 template attacks，读者可能误解为适用于所有攻击类型。Section 4.3 正文有正确限定，但 Abstract 缺失。需修改为 \"drives generalization **on template attacks**\" 或 \"**for structurally consistent attack families**\"。[R1-N2 ↔ R2 cross AGREE]\n\n**MF3 [共识，严重程度有分歧]: 核心 evidence hierarchy 增量新颖性定位过高。**\nClassification DAPT 优于 vanilla/MLM 在 Gururangan et al. (2020) 的 DAPT 框架下是 largely predictable——该文已系统证明 task-adaptive pretraining 在多个 NLP 任务上优于 vanilla continued pretraining。论文将此结果标记为三大 \"unexpected findings\" 之一（Section 1, page 2），novelty framing 有拔高之嫌。论文的真正贡献在于因子分解的定量化（domain exposure vs classification supervision 的贡献量级、boundary conditions、scrambled equivalence），而非 hierarchy 排序本身。建议将 finding (i) 重新定位为 \"quantifying the magnitude and conditions\" 而非 \"unexpected\"。[R2-N1 critical + R1 cross AGREE but prefers major. Director 判定: Must-Fix for framing]\n\n### Should-Fix\n\n**SF1 [分歧裁定]: 对话长度混淆——现有控制充分但缺直接 baseline。**\nBenign 12-20 turns vs jailbreak 3-10 turns 的长度差异是潜在混淆因素。论文已提供截断验证（Appendix V, Table 32 Part A: 截断后 FPR=0.000）、length-matched 子集（N=155, ΔF1=-2.5pp）、length stratification（Appendix U, Table 31: 无系统性退化）。R2 认为这些控制已充分排除长度 shortcut；R1 认为 turn-count-only baseline F1 是更直接的反驳。**Director 裁定: Should-Fix**——现有控制合理但非决定性，一个简单的 turn-count classifier 可一步封堵此质疑。[R1-N1 Must-Fix vs R2 Should-Fix]\n\n**SF2 [分歧裁定]: WildChat 68.1% FPR——合成数据训练的根本局限。**\nR1 将此视为跨域泛化失败；R2 指出论文的 \"cross-attack generalization\" 始终限定在攻击家族维度而非域泛化。R2 的论证在技术上正确——abstract 已标注 few-shot adaptation，没有声称 zero-shot 跨域泛化。**Director 裁定: Should-Fix**——68.1% FPR 不构成 soundness 问题，但暴露了合成 benign 训练数据的系统性偏差，应在 Discussion 中更明确讨论。需第二个人类多轮数据源（如 ShareGPT 或 LMSYS-Chat）的验证。[R1-N3 Must-Fix vs R2 Minor]\n\n**SF3 [共识]: TOST δ=5pp 缺乏 practical significance 论证。**\n在 F1>0.95 的区间，5pp 差异意味着 miss rate 的数倍变化——如果 5pp 在部署场景下有实际意义，用它做等价阈值则自相矛盾。应补充 domain-specific practical significance 论证或 δ=3pp sensitivity analysis。[R1-W1 + R2 AGREE]\n\n**SF4 [共识]: Topic 变体 5 vs 9 类别数量混淆。**\nTopic variant 用 5-class 分类而 9-class variant 用 9 categories（Table 1）。Topic 的失败可能因为 5 classes 不足以产生足够的 discriminative compression，而非因为 topic labels 与 jailbreak detection 无关。一个 9→5 class merging 控制实验成本低且能直接回答这个问题。[R1-W3 + R2 AGREE]\n\n**SF5 [共识]: RoBERTa-large DAPT \"有害\" 机制未解释。**\nSection 4.4 和 Section 5 解释了为什么大模型不需要 DAPT（vanilla capacity 足够），但 9-class DAPT 在 AA 上 F1 从 1.000→0.946 表明 DAPT 是 actively harmful，不仅仅是 unnecessary。可能的机制（over-specialization、catastrophic forgetting）未被区分。CKA 分析（Appendix S, Figure 6）可能提供线索但未被讨论。[R1-W4 + R2-W4 AGREE]\n\n**SF6 [共识]: 1000 样本性能反常下降未解释。**\nAppendix I (Table 9/10) 报告 1000 样本时的性能下降，论文归因于 distributional heterogeneity，但无实验验证。应报告 1000 样本的 training loss 曲线、data composition 分析或 seed 一致性验证。[R1-W5 + R2 AGREE]\n\n**SF7 [共识]: \"Evidence hierarchy\" 术语缺乏正式定义。**\n从 Section 1 (page 1-2) 开始频繁使用但首次出现时无明确定义。读者需从上下文推断含义。R1 进一步指出该术语暗示超出经验排序的理论地位，建议改为 \"performance ranking\"。应在首次使用处加入操作性定义。[R2-W1 + R1 AGREE]\n\n**SF8 [共识]: Conclusion \"reusable template\" claim 超出实证范围。**\nSection 6 声称 \"This ablation framework provides a template for diagnosing when domain adaptation succeeds and fails in this safety-critical detection setting\"，但实证基础仅限于单一任务、单一数据源、单一 encoder 家族。应限定为 \"template for future controlled studies of domain adaptation in safety-critical NLP tasks\"。[R2-W3 + R1 AGREE]\n\n**SF9 [共识]: BiGRU vs mean pooling 讨论不足。**\nAppendix T (Table 30) 显示 frozen probing 下 BiGRU 和 mean pooling 差异在 CI 范围内，E2E fine-tuning 下均收敛到 F1=1.000。这暗示 temporal order 在充分表征质量下非必需，与论文将 BiGRU 作为 Stage 2 核心组件的设计选择相关。应在正文明确说明 BiGRU 可被 mean pooling 替代且不影响检测性能。[R1-W3 + R2-W4 AGREE]\n\n**SF10 [共识]: 策略标注质量验证不足。**\n50 样本验证 9 个类别，部分类别仅 2-5 个验证样本，κ=0.78 在此粒度下可靠性不足。Scrambled 实验缓解了对主要检测结论的影响，但 Appendix Y 策略预测准确率（90.1%）受标注质量直接限制。建议增加验证样本至≥100 并报告 per-class κ。[R1-W4 + R2 AGREE]\n\n### Minor\n\n**M1: Abstract 句法模糊。** \"this hierarchy reverses\" 后的修饰对象不清晰，需要重写以消除歧义。[R2, 跨轮持续存在]\n\n**M2: Scrambled ≈ 9-class 发现的叙事定位。** 该发现可能是论文最具洞察力的结果，但当前论文将其作为 hierarchy 排序的补充讨论，而非核心贡献。建议在 Section 5 增加段落讨论 classification objective structure vs label semantics 的机制意涵。[R1-W2 ↔ R2-W2]\n\n## Reviewer Consensus\n\n以下关键问题两位 Reviewer 完全一致：\n1. ToxicChat hierarchy 反转是论文最大的 narrative concern（MF1）\n2. Abstract \"label semantics\" claim 需限定到 template attacks（MF2）\n3. Scrambled ≈ 9-class 在 ActorAttack 上不成立（d=0.44, TOST p=0.183）\n4. \"Reusable template\" overclaim 需限定范围（SF8）\n5. RoBERTa-large DAPT 反转缺乏机制解释（SF5）\n6. BiGRU 可被 mean pooling 替代（SF9）\n7. Overall 3.0 (Findings) 评分\n\n## Reviewer Divergence\n\n**分歧 1: 长度混淆严重程度** — R1 列为 Must-Fix（turn-count shortcut 可能性未排除）；R2 列为 Should-Fix（Appendix U/V 的截断、length-matched、stratification 实验已充分控制）。Director 裁定 Should-Fix：现有控制合理，但 turn-count-only baseline 可一步封堵。\n\n**分歧 2: WildChat 68.1% FPR 严重程度** — R1 列为 Must-Fix（跨域泛化声明严重削弱）；R2 列为 Minor wording（论文从未声称跨域泛化，attack-side 和 benign-side 是正交轴）。Director 裁定 Should-Fix：R2 技术上正确但 68.1% FPR 暴露合成数据训练的系统性偏差，需更充分讨论。\n\n**分歧 3 (minor): Scrambled \"counter-intuitive\" framing** — R2 认为在 discriminative compression 框架下可预期；R1 认为对 NLP 社区多数读者仍具 counter-intuitive 成分（random labels 在标准 NLP 文献中被视为 noise injection 而非有效训练信号）。Director 判断 R1 更准确——scrambled ≈ 9-class 确有 counter-intuitive 价值，但 ActorAttack 例外需在正文突出。\n\n## Questions\n\n**Q1:** 作者能否提供一个 turn-count-only classifier 的 F1 作为 sanity check？这是一个零成本实验，可以彻底排除长度 shortcut 质疑。\n\n**Q2:** ToxicChat 反转的根因是 single-turn 特性还是 distributional properties？作者能否将 ToxicChat 数据用多轮格式包装（padding with neutral turns）测试 classification DAPT 是否恢复？\n\n**Q3:** RoBERTa-large 上 9-class DAPT 导致 AA F1 从 1.000 降至 0.946 的机制是什么？CKA 分析（Figure 6）能否提供线索？\n\n**Q4:** 1000 样本性能下降是否在 3 个 seeds 中一致出现？训练 loss 曲线是否显示过拟合迹象？\n\n**Q5:** 如果将 9-class 策略标签合并为 5 个类别，性能是否下降至 topic variant 水平？这可以区分类别数量和标签相关性的各自贡献。\n\n## Missing References\n\n- **Galinkin & Sablotny (2024)**. \"Improved LLM Jailbreak Detection via Pretrained Embeddings.\" arXiv:2412.01547. 最直接相关的已发表工作——同样使用预训练 encoder embeddings 进行越狱检测。两位 Reviewer 共识应补充。[R22 遗留]\n- **Perez and Wang (2022)** red teaming 工作。R1 建议补充，R2 指出论文可能已引用 Perez et al. (2022)，需确认是否为同一工作。\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 9 info items）。\n\n**Warnings:**\n1. **[Page 9] Conclusion 溢出**: Section 6 (Conclusion) 正文溢出约 3-4 行到第 9 页顶部，之后才是 Limitations。EMNLP 2026 正文限 8 页（Limitations 不计入）。**注意**: Round 20 曾将类似报告标记为 FALSE POSITIVE（\"Sections 1-6 在 p1-p8\"），本轮视觉审查重新检测到溢出——可能是后续修改导致的回归。建议作者确认 Section 6 最后一行是否在第 8 页内，若确实溢出需压缩 Discussion/Conclusion。\n2. **[Pages 3-5] 纯文本区间过长**: Related Work (p3) + Experiments Setup (p5) 均为纯文本，中间仅 p4 右栏有 Table 1，连续 3 页缺乏视觉锚点。建议将 Figure 2 或某关键表格前移。\n3. **[Page 15] Figure 5 heatmap 标注过小**: 三个 heatmap 并排，cell 内数值在 150dpi 下偏小，打印可能难辨。\n\n**Info 亮点**: Figure 1 架构图位置好（p2 顶部）、全文表格 booktabs 风格统一、未发现 LaTeX 渲染错误或未解析引用。正文 display item 密度 1.1/页，符合实证论文标准。\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n**置信度: 4/5 (High)**\n\n本文是一项全面、系统的消融研究，实验设计质量高，分析工具丰富。但以下因素阻碍其达到 Conference (4.0) 水平：\n\n1. **核心叙事在真实数据上失效**: ToxicChat hierarchy 反转 + WildChat 68.1% FPR 表明论文的 \"evidence hierarchy\" 仅在合成数据生态系统内成立。这不是 soundness 缺陷（论文报告了这些结果），但严重限制了结论的实际影响力。\n2. **方法新颖性有限**: 论文本质上是将已知的 DAPT 范式（Gururangan et al., 2020）应用于新领域，方法层面无创新。其贡献在于 empirical findings（scrambled equivalence、boundary conditions），但这些发现中的核心一条（classification > MLM ranking）可从先行工作预期。\n3. **Claims 多处超出实证范围**: \"reusable template\"（单一任务）、\"label semantics don't matter\"（仅 template attacks）、\"unexpected\"（可预期）等表述需要系统性收窄。\n\n**为何不低于 3.0**: 实验执行质量高，因子分解设计在安全检测领域有参考价值，scrambled label equivalence 和 boundary conditions 的发现对社区有实用启示。论文作为 Findings paper 的贡献足够。\n\n**为何不高于 3.0**: 核心叙事的真实数据泛化失败是结构性问题而非措辞问题——即使完美修改 framing，论文的主要 take-away 仍然是 \"DAPT hierarchy exists but only in synthetic settings\"，这限制了 impact。方法新颖性不足以支撑 Conference 推荐。\n\n## Detailed Comments\n\n### Abstract\n- \"indicating the classification objective's structural role—not label semantics—drives generalization\" 需限定为 template attacks（MF2）\n- \"this hierarchy reverses\" 句法模糊，修饰对象不清（M1）\n- 三大 \"unexpected findings\" 中的 finding (i) 应降格为 \"quantifying the magnitude\"（MF3）\n\n### Section 1 (Introduction)\n- \"Evidence hierarchy\" 首次使用处需操作性定义（SF7）\n- 三大贡献的 novelty framing 需调整——contribution #1 从 \"unexpected\" 改为 \"systematic quantification\"（MF3）\n\n### Section 3 (Method)\n- BiGRU 选择理由需补充说明——正文应明确 mean pooling 可替代（SF9）\n\n### Section 4.3 (Evidence Hierarchy)\n- 正文有 ActorAttack d=0.44 的限定，但 abstract 缺失——需保持一致（MF2）\n- Topic 5-class vs 9-class 类别数量混淆需讨论或补充控制实验（SF4）\n\n### Section 4.4 (Scale Effects)\n- \"DAPT unnecessary at 355M\" 需区分 \"unnecessary\" vs \"harmful\"，讨论 CKA 线索（SF5）\n\n### Section 4.6 (ToxicChat)\n- 需从 1 句话扩展为 1-2 段深入分析，隔离 single-turn vs distributional 因素（MF1）\n\n### Section 4.7 (Data Scale)\n- 1000 样本下降需补充 seed 一致性和 training loss 证据（SF6）\n\n### Section 5 (Discussion)\n- 增加 scrambled equivalence 的机制讨论段落（M2）\n- WildChat FPR 作为合成数据训练局限的讨论需更充分（SF2）\n\n### Section 6 (Conclusion)\n- \"reusable template\" 限定范围（SF8）\n- ToxicChat 反转的条件性结论需加深（MF1）\n- 检查是否溢出到 page 9（Visual Check Warning #1）\n\n### Appendix\n- TOST δ=5pp 补充 practical significance 论证（SF3）\n- 策略标注验证样本量增加至≥100，报告 per-class κ（SF10）\n- 确认 Galinkin & Sablotny (2024) 和 Perez and Wang (2022) 引用状态",
    "project": "persuasion_turn_jailbreak_detect",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_613965f45d48763f375aa83e9294b24a"
  }
}
```

</details>

---


### Tool result

_source line 2139 · 2026-05-24T13:45:24.159891+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a90fe0dde422576f214f12233cfe27a3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4270
}
```

</details>

---


### Assistant

_source line 2140 · 2026-05-24T13:45:34.711531+00:00_

Round 23 审稿报告已投递。

**总结**：两位 Reviewer 完成独立初审 + 交叉回应，共识度高。核心裁定：

- **3 条 Must-Fix**：ToxicChat hierarchy 反转处理深度不足、Abstract "label semantics" claim 未限定 template attacks、novelty framing 过高（"unexpected" → "quantifying"）
- **10 条 Should-Fix**：含 2 条 Director 分歧裁定（长度混淆 R1 Must→Should、WildChat FPR R1 Must→Should）
- **评分 3.0 (Findings)**，置信度 4/5。核心阻碍 Conference 的因素：真实数据上 hierarchy 失效（结构性而非措辞问题）、方法新颖性有限、claims 多处超出实证范围

Issue Tracker 已同步更新至 60 条（含 2 条新增：R23-W1 RoBERTa-large "harmful" 机制、R23-W2 Topic 类别数量混淆）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 175

## Round 175

2 recorded events


### User

_source line 2141 · 2026-05-24T13:45:37.340672+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

**要点汇总**：
- **[REBUT] N1（长度混淆）**：论文在 Appendix V 有 benign 截断验证（FPR=0.000）、length-matched 评估（Δ=−2.5pp）、padding 实验和 length stratification，已充分排除长度 shortcut。建议降级为 Should-Fix，补充 turn-count baseline 即可。
- **[AGREE] N2（label semantics 限定）**：Abstract 的 "drives generalization" 未限定为 template attacks，ActorAttack 上 TOST 不通过。
- **[REBUT] N3（WildChat FPR）**：R1 混淆了 attack-side 和 benign-side 两个正交轴。68% FPR 是 benign domain shift 问题，不影响论文的 cross-attack generalization claim。建议降级为 Minor wording issue。
- **W1–W5**：基本同意，其中 W2（3 seeds）对主要结论影响有限，W3（Topic 5 vs 9 classes）是最值得补充实验的建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2142 · 2026-05-24T13:46:29.473815+00:00_

Round 23 审稿报告已投递至 Research Director。

**评分: 3.0 (Findings)，置信度 4/5。**

**核心结论**：

- **3 条 Must-Fix**：ToxicChat hierarchy 反转处理深度不足、Abstract "label semantics" claim 未限定 template attacks、novelty framing 过高（classification > MLM 可从 Gururangan 2020 预期）
- **10 条 Should-Fix**：长度混淆需 turn-count baseline（Director 从 R1 Must-Fix 降级）、WildChat FPR 需更充分讨论（Director 从 R1 Must-Fix 降级）、TOST δ=5pp 论证、Topic 5v9 类别混淆、RoBERTa-large "harmful" 机制、1000 样本下降、术语定义、overclaim 限定、BiGRU/mean pooling、标注质量
- **2 条 Minor**：Abstract 句法模糊、scrambled equivalence 叙事定位

**阻碍 Conference (4.0) 的结构性因素**：核心 hierarchy 仅在合成数据内成立（真实数据全部失效或退化）、方法新颖性有限（DAPT 范式应用而非创新）、多处 claim 超出实证范围。作为 Findings paper 贡献足够。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 176

## Round 176

62 recorded events


### User

_source line 2143 · 2026-05-25T21:13:35.848643+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: persuasion_turn_jailbreak_detect
- 论文路径: projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle (Long Paper)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2144 · 2026-05-25T21:13:42.804848+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2145 · 2026-05-25T21:13:42.805893+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 2146 · 2026-05-25T21:13:47.837010+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 2147 · 2026-05-25T21:13:47.887665+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2148 · 2026-05-25T21:13:50.812471+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 2149 · 2026-05-25T21:13:50.812952+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2150 · 2026-05-25T21:13:54.532761+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2151 · 2026-05-25T21:13:54.533300+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2152 · 2026-05-25T21:13:59.013302+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 2153 · 2026-05-25T21:14:00.428769+00:00_

{"result":"# 项目 persuasion_turn_jailbreak_detect 概况\n\n## 实验状态 (140 个)\n\n- **plan_016_sentiment_control**: PREPARING (failed) — \n- **plan_012_gpt55_judge**: DONE (success) — \n- **plan_015_dd_eval**: DONE (success) — \n- **plan_006_cross_attack_clean**: DONE (success) — \n- **plan_004_perturbation_eval**: DONE (success) — \n- **plan_013_none_collapse**: DONE (success) — \n- **plan_012_llm_judge_qwen**: DONE (success) — \n- **plan_002_clean_training**: DONE (negative) — \n- **plan_003_scrambled_ablation**: DONE (negative) — \n- **cross_attack_baseline**: DONE (negative) — \n- **plan_008_strategy_transition**: DONE (success) — \n- **plan_007_tfidf_fitd_dd**: DONE (success) — \n- **plan_005_multi_attack_gen**: DONE (success) — \n- **phase_b_full**: DONE (success) — \n- **pilot_phase_b**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp36_frozen_mlm_probing: 冻结 MLM DAPT encoder 的 probing 性能将低于冻结 9-class encoder (exp26: DD=0.997, AA=0.972)，因为 classification DAPT 通过显式策略分类迫使编码器学习与攻击意图更直接相关的判别性特征，而 MLM 仅学习通用语言模式，不产生 OOD 泛化所需的攻击-策略对齐表征。（准备中）\n- exp13_meanpool_multiseed: Mean pooling classifier (without temporal modeling) will perform comparably to BiGRU across 3 seeds on DeBERTa-v3 9-class, confirming that per-turn representations alone drive detection and GRU temporal modeling is unnecessary — cross-validating shuffle ablation results（准备中）\n- exp16_9class_train（准备中）\n- exp16_vanilla_train（准备中）\n- exp17_qwen_benign_gen（准备中）\n- exp17_qwen_jailbreak_gen（准备中）\n- exp17_dryrun（准备中）\n- exp16_llama_benign_gen（准备中）\n- exp16_llama_jailbreak_gen（准备中）\n- llama_crescendo_dryrun（准备中）\n- …另有 22 项\n\n## 近期结论\n- **exp71_mixed_llm_disentangle** (success): The mixed-LLM 9-class AA OOD F1 collapse (0.504±0.107 at 250+250) is primarily driven by distribution heterogeneity rather than per-source data quantity insufficiency: if the collapse were quantity-driven, scaling from 250→350 per source (matching the single-source
…[truncated 1164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1415
}
```

</details>

---


### Tool call

_source line 2154 · 2026-05-25T21:14:00.931285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 2155 · 2026-05-25T21:14:01.937528+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\IfFileExists{inconsolata.sty}{\usepackage{inconsolata}}{}
11	\usepackage{graphicx}
12	\graphicspath{{../../}}
13	\usepackage{amsmath}
14	\usepackage{booktabs}
15	\usepackage{enumitem}
16	\usepackage{amssymb}
17	\usepackage{multirow}
18	
19	\title{DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{abstract}
27	
28	\input{introduction}
29	
30	\input{related_work}
31	
32	\input{method}
33	
34	\input{experiments}
35	
36	\input{conclusion}
37	
38	\bibliography{references}
39	
40	\clearpage
41	\input{appendix}
42	
43	% checklist removed — EMNLP 2026 ARR requires checklist in OpenReview form, not in PDF
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 2156 · 2026-05-25T21:14:01.937998+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2157 · 2026-05-25T21:14:02.189720+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2158 · 2026-05-25T21:14:13.804062+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"}]

The search results returned information about several 2026 conferences and workshops, but I didn't find a specific EMNLP 2026 call for pap
…[truncated 4658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "elapsed_ms": 11866
}
```

</details>

---


### Tool result

_source line 2159 · 2026-05-25T21:14:13.855139+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'persuasion_turn_jailbreak_detect'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 11665
}
```

</details>

---


### Tool call

_source line 2160 · 2026-05-25T21:14:24.048654+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for main conference papers submission format page limit 2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for main conference papers submission format page limit 2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 2161 · 2026-05-25T21:14:25.204485+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 2162 · 2026-05-25T21:14:26.610737+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2163 · 2026-05-25T21:14:29.222112+00:00_

Web search results for query: "EMNLP 2026 call for main conference papers submission format page limit 2026.emnlp.org"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here's the information about EMNLP 2026 main conference papers submission format and page limits:

**Submission Format and Page Limits:**

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

**Submission Details:**

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

**Key Deadline:**

All submissions go through ACL Rolling Rev
…[truncated 273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "elapsed_ms": 5173
}
```

</details>

---


### Tool result

_source line 2164 · 2026-05-25T21:14:29.272900+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/memory.md\", \"content\": \"## 服务器连通性检查 (2026-05-24)\\n\\n### autodl-5090\\n- 连通性: **FAILED** — `[Errno None] Unable to connect to port 33216 on 106.38.204.136`\\n- 项目数据: 无法确认（连接失败）\\n- 备注: 可能实例已关机或端口已变更，需去 AutoDL 控制台确认\\n\\n### gpu-5090-4x-3\\n- 连通性: **FAILED** — `[Errno None] Unable to connect to port 33216 on 106.38.204.136`\\n- 项目数据: 无法确认（连接失败）\\n- 备注: 与 autodl-5090 指向同一 IP:端口（106.38.204.136:33216），疑似同一台实例或配置错误\\n\\n### westd-33183 GPU 状态 (2026-05-24)\\n\\n#### cuda:0\\n- 型号: NVIDIA RTX PRO 6000 Black\\n- 显存: 0 / 97887 MiB\\n- 进程: 无\\n- 状态: **空闲**\\n\\n#### 其他 GPU\\n- nvidia-smi 仅显示 1 张卡（cuda:0），与项目配置中\\\"共 9 张卡\\\"不符，可能容器或 CUDA_VISIBLE_DEVICES 限制\\n\\n#### 磁盘\\n- /root: 26G / 30G (87%) — 仅剩 4.2G，偏紧\\n\", \"total_chars\": 631, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4068
}
```

</details>

---


### Tool result

_source line 2165 · 2026-05-25T21:14:29.273414+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 2662
}
```

</details>

---


### Tool call

_source line 2166 · 2026-05-25T21:14:33.847399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2167 · 2026-05-25T21:14:34.453080+00:00_

1	% abstract.tex
2	\begin{abstract}
3	Multi-turn jailbreaks spread adversarial intent across innocent-looking conversation turns, and safety classifiers designed for single-turn threats miss them: Llama Guard~3 catches only 1.8\%. What makes a detector generalize to attack strategies never seen during training? We introduce DisPeD (Disentangled Persuasion Detection), a controlled framework where seven encoder variants differ solely in pretraining objective while sharing the same frozen classifier; this design isolates how domain exposure, supervision type, and label semantics each contribute to out-of-distribution robustness. Classification-based domain adaptation is the only consistently effective mechanism on synthetic multi-turn attacks: it recovers near-perfect detection where vanilla encoders collapse (F1 0.97--1.0 vs.\ 0.26--0.31) and remains robust under mixed-LLM training where unsupervised pretraining fails entirely. Scrambled labels match correct ones---the classification objective's structural role, not label content, drives generalization. Yet these advantages reverse on human-authored data, where unsupervised pretraining leads, an asymmetry that bounds the scope of each mechanism. The resulting 184M-parameter pipeline achieves 24$\times$ speedup over LLM-as-judge alternatives, and few-shot adaptation substantially reduces false-positive inflation across deployment platforms\footnote{Code and data are available at \url{https://anonymous.4open.science/r/persuasion_turn_jailbreak_detect-C207/}.}.
4	\end{abstract}
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 2168 · 2026-05-25T21:14:34.554001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2169 · 2026-05-25T21:14:35.307834+00:00_

1	% introduction.tex
2	
3	\section{Introduction}
4	
5	Multi-turn jailbreak attacks distribute adversarial intent across individually benign turns. Crescendo~\citep{russinovich2024crescendo}, Foot-in-the-Door~\citep{fitd2024}, and Deceptive Delight~\citep{deceptivedelight2024} all rely on persuasion as their core mechanism: \citet{zeng2024pap} catalogue 40 persuasion techniques across jailbreak families, and \citet{hagendorff2026reasoning} identify strategies in 97\% of successful attacks. Because individual attack turns occupy the same embedding region as benign text~\citep{bullwinkel2025repeng}, no single-turn filter can distinguish them from legitimate conversation.
6	
7	Existing defenses leave a critical gap. Production classifiers such as Llama Guard~\citep{inan2023llamaguard}, WildGuard~\citep{han2024wildguard}, and ShieldGemma~\citep{zeng2024shieldgemma} operate on individual turns and miss multi-turn manipulation; Llama Guard~3 detects only 1.8\% of multi-turn jailbreaks in our evaluation (Section~\ref{sec:decomposition}). Multi-turn defenses (DeepContext~\citep{deepcontext2026}, BIID~\citep{tong2025biid}, G-Guard~\citep{gguard2025}) model conversation-level structure but each evaluates on a single attack family. None answers the central question: \emph{what representation properties enable a detector to generalize across attack families it has never seen?} Pretrained language understanding alone does not suffice: vanilla DeBERTa-v3~\citep{he2023debertav3} with temporal aggregation (cf.\ DeepContext~\citep{deepcontext2026}) drops from F1\,=\,1.000 in-distribution to 0.312 on OOD Deceptive Delight, and GPT-5.5 reaches only 0.191--0.449 F1 (across prefix lengths) with 30--47\% unparseable responses (Appendix~\ref{sec:llm_judge}). The bottleneck is distributional: cross-attack generalization at base model scale benefits substantially from domain adaptation.
8	
9	\begin{figure*}[t]
10	\centering
11	\includegraphics[width=\textwidth]{figures/paper/fig1_architectur
…[truncated 3184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 2170 · 2026-05-25T21:14:35.308314+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2171 · 2026-05-25T21:14:35.358896+00:00_

1	% related_work.tex
2	
3	\section{Related Work}
4	
5	\paragraph{Multi-turn jailbreak attacks.}
6	Multi-turn jailbreak families share a persuasion substrate~\citep{zeng2024pap,hagendorff2026reasoning,li2024mhj} but operationalize it differently: gradual escalation~\citep{russinovich2024crescendo}, commitment-consistency bias~\citep{fitd2024}, emotional manipulation~\citep{deceptivedelight2024}, persona steering~\citep{ren2024actorattack}, context poisoning~\citep{alobaid2026echochamber}. Automated methods~\citep{chao2023pair,mehrotra2024tap} iteratively refine adversarial prompts~\citep{perez2022redteaming}. Taxonomies~\citep{wei2023jailbroken} and benchmarks~\citep{mazeika2024harmbench,chao2024jailbreakbench,jiang2024redqueen,song2026multibreak} standardize evaluation. This shared substrate with diverse surface strategies defines our setting: a detector must generalize across families, not merely succeed on its training distribution.
7	
8	\paragraph{Multi-turn defenses and production safety.}
9	No existing defense evaluates cross-attack transfer. Recent conversation-level systems pair fine-tuned encoders with sequence aggregation~\citep{deepcontext2026,tong2025biid,gguard2025,safedream2026}, yet each evaluates on a single attack family; absent public implementations preclude direct comparison (Appendix~\ref{app:bert_proxy}). Representation-level approaches~\citep{lu2025xboundary,zhang2025jbshield,xie2024gradsafe,zou2024circuitbreakers,wu2025safeint,shen2024jailbreakantidote,yousefpour2025repbend,kulkarni2026latentadversarial,kadali2025internallayers,kadali2026trace,hua2026rcs} require white-box access and can be brittle under adaptive attacks~\citep{derya2026revisitingjbshield}. Per-turn classifiers~\citep{inan2023llamaguard,metallamaguard3_2024,zeng2024shieldgemma,han2024wildguard,anthropic2025constitutional} and production systems~\citep{markov2023holistic} cannot model multi-turn trajectories; perturbation-based~\citep{robey2024smoothllm} and decoding-based~\cit
…[truncated 1856 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2172 · 2026-05-25T21:14:35.760913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2173 · 2026-05-25T21:14:36.213268+00:00_

1	% method.tex
2	
3	\section{Method}
4	\label{sec:method}
5	
6	Cross-attack generalization could stem from domain exposure, classification supervision, label correctness, label granularity, or domain specificity. Disentangling these factors demands an architecture where exactly one component varies across conditions. DisPeD separates encoder adaptation (Stage~1) from temporal classification (Stage~2). Seven Stage-1 variants share the same training data and downstream pipeline but differ solely in their pretraining objective; each isolates a single factor (Figure~\ref{fig:architecture}).
7	
8	\subsection{Problem Formulation}
9	
10	A conversation $C = \{u_1, a_1, \ldots, u_N, a_N\}$ alternates user turns $u_i$ and assistant responses $a_i$. Given a prefix of $K$ user turns, the model predicts $y \in \{0, 1\}$ (jailbreak vs.\ benign). We restrict input to user turns because adversarial intent resides in the attacker's messages. This formulation supports early detection from partial prefixes.
11	
12	\subsection{Stage 1: Turn-Level Encoder Adaptation}
13	
14	Each user turn $u_i$ is encoded by DeBERTa-v3-base~\citep{he2023debertav3}; the \texttt{[CLS]} embedding $h_i \in \mathbb{R}^D$ serves as the turn representation. Seven variants, summarized in Table~\ref{tab:variants}, share the same training data but differ in objective.
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\caption{Stage-1 encoder variants. All operate on the same training conversations except Wikipedia MLM (matched token count on Wikipedia text).}
20	\label{tab:variants}
21	\begin{tabular}{@{}p{1.6cm}p{2.2cm}p{2.8cm}@{}}
22	\toprule
23	\textbf{Variant} & \textbf{Objective} & \textbf{Tests whether\ldots} \\
24	\midrule
25	9-class & 9-class persuasion + binary intent & full model \\
26	Binary & binary persuasion + binary intent & granularity matters \\
27	Scrambled & random 9-class + binary intent & label correctness matters \\
28	MLM-only & 15\% token masking & supervision is necessary \\
29	Topic & 5
…[truncated 3814 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2174 · 2026-05-25T21:14:36.213758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2175 · 2026-05-25T21:14:36.665929+00:00_

1	% experiments.tex
2	
3	\section{Experiments}
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\columnwidth]{figures/paper/fig3_evidence_hierarchy.pdf}
8	\caption{Evidence hierarchy across evaluation conditions. Classification-based DAPT outperforms MLM and vanilla on synthetic OOD attacks (DD, AA), but the hierarchy reverses on human-authored single-turn data (ToxicChat), where JB-MLM leads.}
9	\label{fig:evidence_hierarchy}
10	\end{figure}
11	
12	\paragraph{Terminology.}
13	\emph{Cross-attack OOD}: evaluation on attack families unseen during training; benign distribution remains in-distribution (IID) throughout (OOD reflects attack-side shift only). $K$: prefix length (number of conversation turns retained). \emph{DAPT}: all Stage-1 adaptations; we extend \citet{gururangan2020dontstop} to supervised variants. We refer to the performance ranking of DAPT variants across OOD conditions as the \emph{evidence hierarchy} (Section~\ref{sec:decomposition}).
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{Cross-attack generalization (F1) at $K$=2 and full conversation length. IID: Crescendo; OOD: Deceptive Delight (DD). 3-seed mean$\pm$std where noted; full per-$K$ in Appendix~\ref{sec:full_prefix}.}
19	\label{tab:main_results}
20	\resizebox{\columnwidth}{!}{%
21	\begin{tabular}{@{}lcc|cc@{}}
22	\toprule
23	& \multicolumn{2}{c|}{\textit{IID (Cresc.)}} & \multicolumn{2}{c}{\textit{OOD (DD)}} \\
24	\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\
25	\midrule
26	9-class & \textbf{1.000$\pm$.000} & \textbf{1.000$\pm$.000} & .981$\pm$.013 & \textbf{.997$\pm$.005} \\
27	MLM-only$^{\ddagger}$ & .974 & 1.000 & \textbf{.993$\pm$.009} & .914$\pm$.115 \\
28	Vanilla & .978$\pm$.016 & 1.000$\pm$.000 & .479$\pm$.038 & .312$\pm$.026 \\
29	TF-IDF LR$^{\S}$ & 1.000 & 1.000 & 1.000 & .961 \\
30	\bottomrule
31	\end{tabular}}
32	\vspace{-2pt}
33	{\footnotesize $^{\ddagger}$MLM-only IID reports single seed (42); OOD reports 3-seed. $^{\S}$TF-IDF is deterministic (no st
…[truncated 16120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2176 · 2026-05-25T21:14:36.666336+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2177 · 2026-05-25T21:14:37.119064+00:00_

1	% conclusion.tex
2	
3	\section{Discussion}
4	\label{sec:discussion}
5	
6	\paragraph{Discriminative compression and label equivalence.}
7	Three observations argue against a topic shortcut: unstable topic OOD (F1\,=\,0.541$\pm$0.207), scrambled labels within 3.9\,pp, and label-free MLM detection (F1\,$\geq$\,0.97).
8	Classification DAPT compresses features into few dimensions (participation ratio 3.7--9.4 vs.\ 25--32; Figure~\ref{fig:svd_subspace}; Appendices~\ref{app:representation}--\ref{app:tsne}), concentrated in 3 SVD dimensions in layers 8--12 \citep{zhang2021understanding}; CKA analysis confirms this compression emerges in middle-to-late layers (Appendices~\ref{sec:cka_heatmap},~\ref{app:layerwise}). A probe confirms sufficiency, and removal degrades DD by 17\,pp (Appendices~\ref{app:discriminative_probe},~\ref{app:svd_necessity}).
9	
10	\paragraph{Cross-condition transfer and boundaries.}
11	ToxicChat (+18--42\,pp) and cross-LLM experiments (Appendix~\ref{app:cross_llm}) confirm transfer beyond single-LLM artifacts; scale validation on larger training sets preserves the hierarchy (Appendix~\ref{app:scale_validation}). On single-turn human-authored data the hierarchy reverses (MLM leads; Appendix~\ref{app:confidence}); truncated analysis localizes the reversal to distributional gap rather than detection mechanism (Appendix~\ref{app:truncated}). Mixed-LLM 9-class maintains 0.818 while MLM collapses; at 355M, DAPT becomes counterproductive (vanilla AA\,=\,1.000 vs.\ 9-class 0.946). WildChat FPR reaches 68.1\% (synthetic-to-real shift). Length-matched evaluation ($N$=155) shows negligible DD change ($\Delta$\,=\,$-$2.5\,pp; Appendices~\ref{app:length_independence},~\ref{app:length}); ActorAttack padding collapse ($-$57.9\,pp) reflects signal dilution (Appendix~\ref{app:truncated}).
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{figures/paper/fig4_svd_subspace.pdf}
16	\caption{Test representations projected onto top-2 SVD direction
…[truncated 2608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2178 · 2026-05-25T21:14:37.119713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2179 · 2026-05-25T21:14:37.575561+00:00_

1	% appendix.tex — Supplementary material
2	
3	\appendix
4	
5	\section{LLM-as-Judge Baseline}
6	\label{sec:llm_judge}
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}
12	\label{tab:llm_judge}
13	\begin{tabular}{@{}lcccr@{}}
14	\toprule
15	\textbf{Method} & DD & AA & IID & Unparse. \\
16	\midrule
17	\multicolumn{5}{l}{\textit{Zero-shot}} \\[2pt]
18	GPT-5.5 & -- & -- & .383 & 30--47\% \\
19	Qwen3-8B & .244 & .244 & .100 & 0\% \\
20	\midrule
21	\multicolumn{5}{l}{\textit{3-shot}} \\[2pt]
22	Qwen3-8B & .566 & .652 & -- & 0\% \\
23	\midrule
24	\multicolumn{5}{l}{\textit{Trained classifier}} \\[2pt]
25	9-class (ours) & \textbf{.997} & \textbf{.972} & \textbf{1.000} & 0\% \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.
31	On IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 = 0.383 on full conversations; 30--47\% of responses are unparseable.
32	Qwen3-8B performs worse (IID F1 = 0.100).
33	On OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.
34	Even with 3-shot prompting, Qwen3-8B reaches only 0.566 (DD) and 0.652 (AA), while DisPeD maintains macro F1 $\geq$ 0.972.
35	The poor performance of content-level reasoning on unseen attack families underscores the necessity of trained classifiers with domain-adapted representations.
36	
37	\section{Full Cross-Attack Results by Prefix}
38	\label{sec:full_prefix}
39	
40	\begin{table*}[t]
41	\centering
42	\small
43	\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\pm$std where available. ``--'' indicates insufficient conversation length 
…[truncated 65965 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 2180 · 2026-05-25T21:14:37.676638+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 2181 · 2026-05-25T21:14:37.727307+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2182 · 2026-05-25T21:14:44.418045+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 2183 · 2026-05-25T21:14:44.822046+00:00_

{"result":"# 项目 persuasion_turn_jailbreak_detect 概况\n\n## 实验状态 (140 个)\n\n- **plan_016_sentiment_control**: PREPARING (failed) — \n- **plan_012_gpt55_judge**: DONE (success) — \n- **plan_015_dd_eval**: DONE (success) — \n- **plan_006_cross_attack_clean**: DONE (success) — \n- **plan_004_perturbation_eval**: DONE (success) — \n- **plan_013_none_collapse**: DONE (success) — \n- **plan_012_llm_judge_qwen**: DONE (success) — \n- **plan_002_clean_training**: DONE (negative) — \n- **plan_003_scrambled_ablation**: DONE (negative) — \n- **cross_attack_baseline**: DONE (negative) — \n- **plan_008_strategy_transition**: DONE (success) — \n- **plan_007_tfidf_fitd_dd**: DONE (success) — \n- **plan_005_multi_attack_gen**: DONE (success) — \n- **phase_b_full**: DONE (success) — \n- **pilot_phase_b**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp36_frozen_mlm_probing: 冻结 MLM DAPT encoder 的 probing 性能将低于冻结 9-class encoder (exp26: DD=0.997, AA=0.972)，因为 classification DAPT 通过显式策略分类迫使编码器学习与攻击意图更直接相关的判别性特征，而 MLM 仅学习通用语言模式，不产生 OOD 泛化所需的攻击-策略对齐表征。（准备中）\n- exp13_meanpool_multiseed: Mean pooling classifier (without temporal modeling) will perform comparably to BiGRU across 3 seeds on DeBERTa-v3 9-class, confirming that per-turn representations alone drive detection and GRU temporal modeling is unnecessary — cross-validating shuffle ablation results（准备中）\n- exp16_9class_train（准备中）\n- exp16_vanilla_train（准备中）\n- exp17_qwen_benign_gen（准备中）\n- exp17_qwen_jailbreak_gen（准备中）\n- exp17_dryrun（准备中）\n- exp16_llama_benign_gen（准备中）\n- exp16_llama_jailbreak_gen（准备中）\n- llama_crescendo_dryrun（准备中）\n- …另有 22 项\n\n## 近期结论\n- **exp71_mixed_llm_disentangle** (success): The mixed-LLM 9-class AA OOD F1 collapse (0.504±0.107 at 250+250) is primarily driven by distribution heterogeneity rather than per-source data quantity insufficiency: if the collapse were quantity-driven, scaling from 250→350 per source (matching the single-source
…[truncated 1164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 2184 · 2026-05-25T21:14:44.822609+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 2185 · 2026-05-25T21:14:44.873165+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2186 · 2026-05-25T21:14:46.382478+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 2187 · 2026-05-25T21:14:47.035608+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 2188 · 2026-05-25T21:14:47.186908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2189 · 2026-05-25T21:14:47.188484+00:00_

1	% References for persuasion_turn_jailbreak_detect
2	% Auto-generated from literature_map.yaml (2026-05-18)
3	% Total entries: 31
4	
5	% ============================================================
6	% Category 1: Production Multi-Turn Safety Systems
7	% ============================================================
8	
9	@article{inan2023llamaguard,
10	  title={Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations},
11	  author={Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer, Krithika and Mao, Yuning and Tontchev, Michael and Hu, Qing and Fuller, Brian and Testuggine, Davide and Khabsa, Madian},
12	  journal={arXiv preprint},
13	  year={2023},
14	  eprint={2312.06674},
15	  archivePrefix={arXiv},
16	}
17	
18	@misc{metallamaguard3_2024,
19	  title={Llama Guard 3},
20	  author={{Meta AI}},
21	  year={2024},
22	  howpublished={Meta AI (released with Llama 3.1)},
23	}
24	
25	@article{zeng2024shieldgemma,
26	  title={ShieldGemma: Generative AI Content Moderation Based on Gemma},
27	  author={Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, Joe and Harkous, Hamza and Narasimhan, Karthik and Proud, Drew and Kumar, Piyush and Radharapu, Bhaktipriya and Sturman, Olivia and Wahltinez, Oscar},
28	  journal={arXiv preprint},
29	  year={2024},
30	  eprint={2407.21772},
31	  archivePrefix={arXiv},
32	}
33	
34	@inproceedings{han2024wildguard,
35	  title={WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs},
36	  author={Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill Yuchen and Lambert, Nathan and Choi, Yejin and Dziri, Nouha},
37	  booktitle={Advances in Neural Information Processing Systems},
38	  year={2024},
39	}
40	
41	@techreport{anthropic2025constitutional,
42	  title={Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming},
43	  author={Sharma, Mrinank and Tong, Meg a
…[truncated 2294 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 2190 · 2026-05-25T21:14:50.208796+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2191 · 2026-05-25T21:14:50.662120+00:00_

1	issues:
2	# === 历史 resolved issues ===
3	- id: R1-N1
4	  summary: Evidence hierarchy 统计基础不一致
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 1
9	  last_seen_round: 1
10	  mentions:
11	  - round: 1
12	    reviewers: [1, 2]
13	    note: binary/scrambled 仅 seed 42
14	  action_items:
15	  - round: 1
16	    action: 训练 binary/scrambled 3-seed
17	    assigned_to: main_agent
18	    status: resolved
19	  resolution: 'MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005'
20	  resolution_round: 1
21	
22	- id: R1-N2
23	  summary: Three-layer robustness attribution 缺乏统计显著性
24	  category: experiment
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 1
28	  last_seen_round: 1
29	  mentions:
30	  - round: 1
31	    reviewers: [1, 2]
32	    note: R1 首提 N2
33	  action_items:
34	  - round: 1
35	    action: McNemar's test + bootstrap CI
36	    assigned_to: main_agent
37	    status: resolved
38	  resolution: MF2 完成
39	  resolution_round: 1
40	
41	- id: R1-N3
42	  summary: 缺少与已发表 multi-turn defense 的直接实验对比
43	  category: experiment
44	  severity: critical
45	  status: resolved
46	  first_raised_round: 1
47	  last_seen_round: 2
48	  mentions:
49	  - round: 1
50	    reviewers: [1, 2]
51	    note: R1 首提 N3
52	  - round: 2
53	    reviewers: [1, 2]
54	    note: Round 1 修复不充分，再次提出
55	  action_items:
56	  - round: 1
57	    action: 重构论证
58	    assigned_to: paper_agent
59	    status: resolved
60	  - round: 2
61	    action: Analysis paper reframe
62	    assigned_to: research_director
63	    status: resolved
64	  resolution: Analysis paper reframe 完成。
65	  resolution_round: 3
66	
67	- id: R1-N4
68	  summary: 数据集规模过小
69	  category: experiment
70	  severity: critical
71	  status: resolved
72	  first_raised_round: 1
73	  last_seen_round: 2
74	  mentions:
75	  - round: 2
76	    reviewers: [1, 2]
77	    note: 500训练+76-118测试+3seeds仍不足
78	  action_items:
79	  - round: 2
80	    action: Bootstrap 95% CI + permutation test
81	    as
…[truncated 34445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 2192 · 2026-05-25T21:14:51.119143+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/references.bib",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/references.bib",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 2193 · 2026-05-25T21:14:51.624713+00:00_

100	% Category 3: Discourse Analysis in NLP
101	% ============================================================
102	
103	@article{mann1988rst,
104	  title={Rhetorical Structure Theory: Toward a Functional Theory of Text Organization},
105	  author={Mann, William C. and Thompson, Sandra A.},
106	  journal={Text \& Talk},
107	  year={1988},
108	  volume={8},
109	  number={3},
110	  pages={243--281},
111	}
112	
113	@inproceedings{prasad2008pdtb,
114	  title={The Penn Discourse TreeBank 2.0},
115	  author={Prasad, Rashmi and Dinesh, Nikhil and Lee, Alan and Miltsakaki, Eleni and Robaldo, Livio and Joshi, Aravind and Webber, Bonnie},
116	  booktitle={Proceedings of the International Conference on Language Resources and Evaluation},
117	  year={2008},
118	}
119	
120	@article{stolcke2000dialogueact,
121	  title={Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech},
122	  author={Stolcke, Andreas and Ries, Klaus and Coccaro, Noah and Shriberg, Elizabeth and Bates, Rebecca and Jurafsky, Daniel and Taylor, Paul and Martin, Rachel and Van Ess-Dykema, Carol and Meteer, Marie},
123	  journal={Computational Linguistics},
124	  year={2000},
125	  volume={26},
126	  number={3},
127	  pages={339--374},
128	}
129	
130	@book{austin1962speechacts,
131	  title={How to Do Things with Words},
132	  author={Austin, J. L.},
133	  publisher={Harvard University Press},
134	  year={1962},
135	}
136	
137	@book{searle1969speechacts,
138	  title={Speech Acts: An Essay in the Philosophy of Language},
139	  author={Searle, J. R.},
140	  publisher={Cambridge University Press},
141	  year={1969},
142	}
143	
144	% ============================================================
145	% Category 4: Computational Persuasion Detection
146	% ============================================================
147	
148	@book{cialdini2001influence,
149	  title={Influence: Science and Practice},
150	  author={Cialdini, Robert B.},
151	  publisher={Allyn \& Bacon},
152	  year={2001},
153	  e
…[truncated 31988 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 2194 · 2026-05-25T21:14:51.625142+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2195 · 2026-05-25T21:14:51.677573+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/decisions.yaml\", \"content\": \"_next_id: 82\\ndecisions:\\n- id: D001\\n  date: 2026-05-17 16:09 UTC\\n  summary: 接受 DeBERTa F1=0.789 作为 baseline，停止数据 TF-IDF 迭代，reframe MVP 为 early detection\\n  rationale: 'DeBERTa F1=0.789 已在目标范围(0.70-0.85)。TF-IDF F1=0.924 高但不致命——论文 reframe:\\n    TF-IDF/vanilla 方法需完整对话才能分类，DisPeD 在 K=2-3 turns 即可通过 persuasion trajectory 早期检测。这完美对齐\\n    Bullwinkel et al. 的核心发现（早期 turns 表征为 benign）。数据迭代已耗 4 轮 6+ 小时，继续追 TF-IDF 阈值的 ROI\\n    为负。用 Crescendo oracle labels (intended_strategy) 替代 GPT 标注，节省 API 成本和时间。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-17 16:49 UTC\\n  summary: MVP PASS — early detection K=2 +10.8pp, K=3 +5.9pp 超过阈值；TF-IDF=1.0 标记为\\n    research 阶段优先解决项\\n  rationale: Treatment (persuasion-grounded DeBERTa → GRU) 在 K=2 时 F1=0.987 vs baseline\\n    0.879 (+10.8pp)，K=3 时 +5.9pp，均超过 MVP 阈值 +5pp。Full conversation F1 差距仅 +1.3pp 未达\\n    +2pp 阈值，但 early detection 是核心 claim 所在。TF-IDF=1.0 表明词汇 shortcut 仍存在，但 (1) 不影响\\n    treatment vs baseline 相对比较的有效性，(2) 可作为 paper motivation（lexical cues 偶然有效但可被攻击者规避，pragmatic\\n    patterns 不可规避），(3) research 阶段通过 adversarial perturbation 实验验证 robustness。\\n  related_experiments:\\n  - exp_id: pilot_phase_b\\n    role: pipeline_validation\\n    result: success (n=270, directionally positive but not statistically meaningful)\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-17 16:59 UTC\\n  summary: 进入 Research 阶段，framing 定位为 Pragmatic Evasion Asymmetry，experiment plan\\n    含 6 个 P0 实验\\n  rationale: MVP PASS (D002) 后按 post-mvp-kickoff 流程：paper_framing.md 将核心贡献从\\\"更好的检测器\\\"升级为\\\"语用逃逸不对称性原则的首个实证验证\\\"（源自\\n    Human Review Note），experiment_plan.yaml 优先解决 TF-IDF=1.0 数据质量阻塞。Dream full review\\n    已发起，等回调后审批 P0。\\n  related_experiments:\\n  - exp_id: phase_b_full\\n    role: motivation\\n    result: K=2 +10.8pp but 
…[truncated 1467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 2196 · 2026-05-25T21:15:40.884887+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "review_chat_id": "oc_613965f45d48763f375aa83e9294b24a"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "review_chat_id": "oc_613965f45d48763f375aa83e9294b24a"
  }
}
```

</details>

---


### Tool call

_source line 2197 · 2026-05-25T21:15:41.036708+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 2198 · 2026-05-25T21:15:50.882740+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 9997
}
```

</details>

---


### Tool result

_source line 2199 · 2026-05-25T21:15:50.933421+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 9896
}
```

</details>

---


### Tool call

_source line 2200 · 2026-05-25T21:16:29.131645+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "persuasion_turn_jailbreak_detect",
  "text": "你是 Reviewer 1，负责审查论文 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题: DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection\n- 文件路径: `projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_round_24/submitted.pdf`\n\n## 目标 Venue\n- **EMNLP 2026** (via ARR May cycle, Long Paper)\n- 截止日期: 2026-05-25\n- **页数限制**: 正文 8 页（严格限制），参考文献不限，Limitations 必须有但不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind (ARR 统一审稿)\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**核心任务：评估方法论和实验的严谨性**\n\n请重点审查以下方面：\n\n### 1. 实验设计与控制变量\n- 7 个 Stage-1 变体是否真正隔离了单一因素？有无混杂因素？\n- Topic 变体(5类) vs 9-class(9类)：类别数量差异是否构成混杂？\n- Scrambled labels 实验设计是否充分（seed robustness、partition choice）？\n- 训练/测试数据划分是否合理？数据泄漏风险？\n\n### 2. 统计分析\n- 3-seed 报告是否足够支持结论？方差估计可靠性？\n- TOST 等价检验的 δ=5pp margin 是否有 practical significance 论证？\n- Bootstrap CI 和 permutation test 的假设是否合理？\n- 效应量报告是否完整？\n\n### 3. 数据规模与泛化\n- 350 训练对话 + 76-118 测试样本 → 结论的可靠性？\n- 单一 LLM (Qwen3-8B) 合成数据 → 跨攻击泛化声明的可信度？\n- Mixed-LLM 实验中 ActorAttack F1=0.504 → 对主要结论的影响？\n- 1000 样本训练后性能反常下降 → 解释是否充分？\n\n### 4. 长度混淆\n- Benign (12-20 turns) vs jailbreak (3-10 turns) 完全不重叠 → 模型是否学习长度而非内容？\n- 论文中的长度控制实验（截断、padding）是否充分排除此混淆？\n\n### 5. 人类数据验证\n- ToxicChat evidence hierarchy 完全反转(MLM 0.837 >> 9-class 0.596) → 论文的讨论深度是否匹配问题严重性？\n- WildChat FPR=68.1% → 合成训练数据的系统性偏差？\n\n### 6. Baseline 对比\n- 缺少与已发表 multi-turn defense (DeepContext, BIID, G-Guard) 的直接实验对比\n- LLM-as-judge baseline 的公平性\n- TF-IDF 在 DD 上的强表现(F1=1.0)是否被充分讨论？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n[2-3 句概述]\n\n## Strengths\n[S1] ...\n[S2] ...\n\n## Weaknesses\n### Must-Fix (阻碍接收的关键问题)\n[N1] ...\n[N2] ...\n\n### Should-Fix (需要改进但不阻碍接收)\n[W1] ...\n[W2] ...\n\n### Minor (小问题)\n[M1] ...\n\n## Questions for Authors\n[Q1] ...\n\n## Missing References\n[如有]\n\n## Overall Assessment\nScore: X (按 EMNLP 2026 ARR 评分标准)\nConfidence: X/5\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "persuasion_turn_jailbreak_detect",
    "text": "你是 Reviewer 1，负责审查论文 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题: DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection\n- 文件路径: `projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_round_24/submitted.pdf`\n\n## 目标 Venue\n- **EMNLP 2026** (via ARR May cycle, Long Paper)\n- 截止日期: 2026-05-25\n- **页数限制**: 正文 8 页（严格限制），参考文献不限，Limitations 必须有但不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind (ARR 统一审稿)\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**核心任务：评估方法论和实验的严谨性**\n\n请重点审查以下方面：\n\n### 1. 实验设计与控制变量\n- 7 个 Stage-1 变体是否真正隔离了单一因素？有无混杂因素？\n- Topic 变体(5类) vs 9-class(9类)：类别数量差异是否构成混杂？\n- Scrambled labels 实验设计是否充分（seed robustness、partition choice）？\n- 训练/测试数据划分是否合理？数据泄漏风险？\n\n### 2. 统计分析\n- 3-seed 报告是否足够支持结论？方差估计可靠性？\n- TOST 等价检验的 δ=5pp margin 是否有 practical significance 论证？\n- Bootstrap CI 和 permutation test 的假设是否合理？\n- 效应量报告是否完整？\n\n### 3. 数据规模与泛化\n- 350 训练对话 + 76-118 测试样本 → 结论的可靠性？\n- 单一 LLM (Qwen3-8B) 合成数据 → 跨攻击泛化声明的可信度？\n- Mixed-LLM 实验中 ActorAttack F1=0.504 → 对主要结论的影响？\n- 1000 样本训练后性能反常下降 → 解释是否充分？\n\n### 4. 长度混淆\n- Benign (12-20 turns) vs jailbreak (3-10 turns) 完全不重叠 → 模型是否学习长度而非内容？\n- 论文中的长度控制实验（截断、padding）是否充分排除此混淆？\n\n### 5. 人类数据验证\n- ToxicChat evidence hierarchy 完全反转(MLM 0.837 >> 9-class 0.596) → 论文的讨论深度是否匹配问题严重性？\n- WildChat FPR=68.1% → 合成训练数据的系统性偏差？\n\n### 6. Baseline 对比\n- 缺少与已发表 multi-turn defense (DeepContext, BIID, G-Guard) 的直接实验对比\n- LLM-as-judge baseline 的公平性\n- TF-IDF 在 DD 上的强表现(F1=1.0)是否被充分讨论？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n[2-3 句概述]\n\n## Strengths\n[S1] ...\n[S2] ...\n\n## Weaknesses\n### Must-Fix (阻碍接收的关键问题)\n[N1] ...\n[N2] ...\n\n### Should-Fix (需要改进但不阻碍接收)\n[W1] ...\n[W2] ...\n\n### Minor (小问题)\n[M1] ...\n\n## Questions for Authors\n[Q1] ...\n\n## Missing References\n[如有]\n\n## Overall Assessment\nScore: X (按 EMNLP 2026 ARR 评分标准)\nConfidence: X/5\n```"
  }
}
````

</details>

---


### Tool result

_source line 2201 · 2026-05-25T21:16:45.630328+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16498
}
```

</details>

---


### Tool call

_source line 2202 · 2026-05-25T21:16:45.783793+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "persuasion_turn_jailbreak_detect",
  "text": "你是 Reviewer 2，负责审查论文 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题: DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection\n- 文件路径: `projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_round_24/submitted.pdf`\n\n## 目标 Venue\n- **EMNLP 2026** (via ARR May cycle, Long Paper)\n- 截止日期: 2026-05-25\n- **页数限制**: 正文 8 页（严格限制），参考文献不限，Limitations 必须有但不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind (ARR 统一审稿)\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**核心任务：评估论文的新颖性、完整性和写作质量**\n\n请重点审查以下方面：\n\n### 1. 新颖性评估\n- 论文的核心贡献是什么？是方法创新还是实证发现？\n- Classification DAPT > vanilla/MLM 的结论在 Gururangan et al. (2020) DAPT 框架下是否可预期？\n- Scrambled labels ≈ correct labels 的发现有多 counter-intuitive？\n- 因子分解消融设计本身是否构成新颖贡献？\n- 与现有 multi-turn defense 工作的增量贡献是否清晰？\n\n### 2. 叙事一致性\n- Abstract 中的 claims 是否与实验结果一致（特别是 scale-dependent 和 condition-specific 的限制）？\n- \"evidence hierarchy\" 概念是否被恰当定义和使用？\n- Findings 在不同条件下的不一致性（synthetic vs human, base vs large, single-LLM vs mixed-LLM）是否被充分承认和讨论？\n- Conclusion 是否过度泛化？\n\n### 3. Related Work 覆盖\n- Multi-turn jailbreak defense 领域的覆盖是否全面？\n- Domain-adaptive pretraining 文献的定位是否准确？\n- 是否有重要的遗漏引用？\n\n### 4. 写作质量\n- Abstract 信息密度是否适当？是否超过 200 words？句法是否清晰？\n- 自创术语（evidence hierarchy, discriminative compression, partition sufficiency）是否有清晰定义？\n- 正文 8 页限制是否满足？\n- 图表质量和信息传达效率\n- Limitations section 是否充分？\n\n### 5. 格式合规\n- ACL 模板使用是否正确？\n- 匿名要求是否满足（检查 anonymous submission, 代码链接是否匿名化）？\n- Checklist 是否在 OpenReview form 而非 PDF（EMNLP 2026 要求）？\n- 参考文献格式是否一致？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n[2-3 句概述]\n\n## Strengths\n[S1] ...\n[S2] ...\n\n## Weaknesses\n### Must-Fix (阻碍接收的关键问题)\n[N1] ...\n[N2] ...\n\n### Should-Fix (需要改进但不阻碍接收)\n[W1] ...\n[W2] ...\n\n### Minor (小问题)\n[M1] ...\n\n## Questions for Authors\n[Q1] ...\n\n## Missing References\n[如有]\n\n## Overall Assessment\nScore: X (按 EMNLP 2026 ARR 评分标准)\nConfidence: X/5\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "persuasion_turn_jailbreak_detect",
    "text": "你是 Reviewer 2，负责审查论文 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题: DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection\n- 文件路径: `projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_round_24/submitted.pdf`\n\n## 目标 Venue\n- **EMNLP 2026** (via ARR May cycle, Long Paper)\n- 截止日期: 2026-05-25\n- **页数限制**: 正文 8 页（严格限制），参考文献不限，Limitations 必须有但不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind (ARR 统一审稿)\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**核心任务：评估论文的新颖性、完整性和写作质量**\n\n请重点审查以下方面：\n\n### 1. 新颖性评估\n- 论文的核心贡献是什么？是方法创新还是实证发现？\n- Classification DAPT > vanilla/MLM 的结论在 Gururangan et al. (2020) DAPT 框架下是否可预期？\n- Scrambled labels ≈ correct labels 的发现有多 counter-intuitive？\n- 因子分解消融设计本身是否构成新颖贡献？\n- 与现有 multi-turn defense 工作的增量贡献是否清晰？\n\n### 2. 叙事一致性\n- Abstract 中的 claims 是否与实验结果一致（特别是 scale-dependent 和 condition-specific 的限制）？\n- \"evidence hierarchy\" 概念是否被恰当定义和使用？\n- Findings 在不同条件下的不一致性（synthetic vs human, base vs large, single-LLM vs mixed-LLM）是否被充分承认和讨论？\n- Conclusion 是否过度泛化？\n\n### 3. Related Work 覆盖\n- Multi-turn jailbreak defense 领域的覆盖是否全面？\n- Domain-adaptive pretraining 文献的定位是否准确？\n- 是否有重要的遗漏引用？\n\n### 4. 写作质量\n- Abstract 信息密度是否适当？是否超过 200 words？句法是否清晰？\n- 自创术语（evidence hierarchy, discriminative compression, partition sufficiency）是否有清晰定义？\n- 正文 8 页限制是否满足？\n- 图表质量和信息传达效率\n- Limitations section 是否充分？\n\n### 5. 格式合规\n- ACL 模板使用是否正确？\n- 匿名要求是否满足（检查 anonymous submission, 代码链接是否匿名化）？\n- Checklist 是否在 OpenReview form 而非 PDF（EMNLP 2026 要求）？\n- 参考文献格式是否一致？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n[2-3 句概述]\n\n## Strengths\n[S1] ...\n[S2] ...\n\n## Weaknesses\n### Must-Fix (阻碍接收的关键问题)\n[N1] ...\n[N2] ...\n\n### Should-Fix (需要改进但不阻碍接收)\n[W1] ...\n[W2] ...\n\n### Minor (小问题)\n[M1] ...\n\n## Questions for Authors\n[Q1] ...\n\n## Missing References\n[如有]\n\n## Overall Assessment\nScore: X (按 EMNLP 2026 ARR 评分标准)\nConfidence: X/5\n```"
  }
}
````

</details>

---


### Tool result

_source line 2203 · 2026-05-25T21:16:47.501747+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1717
}
```

</details>

---


### Assistant

_source line 2204 · 2026-05-25T21:16:54.935529+00:00_

**Round 24 圆桌审稿已启动。**

审稿编排：
- **Reviewer 1**：方法严谨性 + 实验设计（统计检验、控制变量、数据规模、长度混淆、人类数据验证、Baseline 对比）
- **Reviewer 2**：新颖性 + 完整性 + 写作质量（贡献定位、叙事一致性、Related Work、格式合规、自创术语）

并行任务：
- 视觉审查 Agent 已派发（不阻塞主流程）
- 外部审稿未配置，跳过

等待两位 Reviewer 独立审稿完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 177

## Round 177

2 recorded events


### User

_source line 2205 · 2026-05-25T21:23:25.025711+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection

---

## Summary

本文提出 DisPeD，一个因子化消融框架，将 DeBERTa 编码器的 7 种预训练目标（9-class 说服策略分类、binary、scrambled labels、MLM-only、topic、Wiki MLM、vanilla）与固定的 BiGRU 分类器解耦，在 3 个模型规模（125M/184M/355M）和 4 个攻击家族（Crescendo/DD/FTTD/ActorAttack）上系统研究 domain exposure、supervision type、label semantics 对 OOD 越狱检测的贡献。核心发现：分类式 DAPT 是合成数据上唯一稳定恢复 OOD 检测的机制（F1 0.97–1.0 vs. vanilla 0.26–0.31）；scrambled labels 在模板攻击上等效于正确标签；但该 hierarchy 在人工数据（ToxicChat）上反转。论文同时报告了 184M 参数管线相比 LLM-as-judge 的 24.3× 加速。

---

## Strengths

**[S1] 实验设计严谨，因子分解干净。** 7 种 Stage-1 变体共享相同的训练数据和 Stage-2 分类器，仅在预训练目标上不同（Table 1）。这种控制变量设计在该领域是罕见的——绝大多数多轮越狱防御论文只报告单一方法的端到端性能，而本文系统隔离了三个正交因子。13 种编码器配置 × 3 种规模 × 4 种攻击家族的覆盖面也相当全面。

**[S2] Scrambled labels 发现具有实证价值。** Scrambled labels 在模板攻击上与正确标签等效（Table 3, Section 4.3: TOST p=0.005 vs. 0.14 for ActorAttack），揭示分类目标的结构角色（而非标签语义）驱动泛化。这一发现对从业者有实际指导意义：在标注资源有限时，即使用粗略标注也可能获得有效的 domain adaptation。

**[S3] 消融深度远超同类工作。** Appendix 提供了极其详尽的补充实验——CKA 表征分析（Appendix S.1, Figure 10）、SVD 子空间消融（Table 28-29）、TOST 等价性检验（Table 16, Appendix L）、per-seed F1 comparisons（Appendix Z.1, Table 38）、conversation length stratification（Appendix U, Table 31）、FPR 适应曲线（Figure 5）、cross-checkpoint variance（Appendix N）。这种透明度值得肯定。

**[S4] 实用价值清晰。** 184M 参数管线在消费级硬件上运行（362MB GPU 内存，Table 33），24.3× 加速和 few-shot benign adaptation 降低 FPR 至 ~1.5%（Section 4.8, Table 20-21）的方案具有实际部署可行性。

**[S5] 写作结构整体清晰。** 论文叙事从 motivation（LLM guard 只检测 1.8%）到方法、实验、发现的逻辑链条流畅。Figure 1 有效传达了两阶段架构。

---

## Weaknesses

### Must-Fix（阻碍接收的关键问题）

**[N1] [critical] 核心发现的新颖性有限——Classification DAPT 优于 vanilla/MLM 是 Gururangan et al. (2020) DAPT 框架的可预期推论**

- 具体位置：Section 1 ("Our contributions"), Section 4.2-4.3, Abstract
- 问题：论文的中心发现——分类式 DAPT 在域内任务上优于通用 MLM 和 vanilla 预训练——直接遵循 Gururangan et al. (2020) 的核心论点：当预训练目标与下游任务对齐时，domain-adaptive pretraining 产生更好的表征。本文本质上是在一个新领域（多轮越狱检测）验证了这一已知原理。虽然消融设计是仔细的，但主要结论并未推进我们对 *为什么* DAPT 有效的理解——它确认了 *它在另一个设置中有效*。
- Scrambled labels 发现更具新颖性，但其适用范围受限于模板攻击（Section 4.3, Table 3）。在策略多样的攻击（ActorAttack）上，label sensitivity 恢复到 0.44（TOST p=0.183），这大幅收窄了 takeaway。
- 为什么影响接收：对于 EMNLP main conference（Overall ≥ 4），需要"exciting"级别的贡献。将一个已知框架应用于新领域的验证性工作，即使执行得很好，通常更适合 Findings track。
- 建议修改方向：(a) 更明确地将贡献定位为"实证性发现"而非"方法创新"；(b) 深挖 scrambled labels 发现的机制——为什么模板攻击不需要正确语义而策略多样攻击需要？(c) 是否存在一个"模板规律性"的量化指标可以预测 scrambled labels 何时有效？

**[N2] [critical] "Evidence hierarchy" 在多个现实条件下反转，但被作为核心贡献呈现**

- 具体位置：Section 4.3 ("evidence hierarchy"), Abstract ("Classification-based domain adaptation is the only consistently effective mechanism"), Conclusion (Section 6)
- 问题：论文声称 domain exposure > supervision type > label semantics 的 evidence hierarchy，但此 hierarchy 在以下条件下不成立：
  1. **人工数据反转**：ToxicChat 上 MLM 领先，分类式 DAPT 不再占优（Figure 4 右侧, Section 4.6: "the hierarchy reverses on human-authored data"）
  2. **大规模失效**：355M 时 DAPT "becomes unnecessary and potentially counterproductive"（Section 5）
  3. **攻击类型依赖**：策略多样攻击（ActorAttack）上 label semantics 重新变得重要（Section 4.3）
  4. **LLM 来源依赖**：mixed-LLM 下 MLM 崩溃但 classification 不崩溃（Section 4.5），然而这只测试了 2 个 LLM（Qwen + Llama）
- 一个在多个现实场景下反转的 hierarchy 不应被称为"hierarchy"——它更像是一组条件依赖的观察。
- 为什么影响接收：这构成了 overclaiming，审稿人和 AC 对此敏感。
- 建议修改方向：(a) 将 "evidence hierarchy" 重新表述为 "condition-dependent factor ordering"；(b) 在 abstract 中明确声明这些限制条件而非仅加 "synthetic" 限定词；(c) 在 conclusion 中避免将此 hierarchy 作为通用指导原则。

**[N3] [critical] 叙事一致性问题——Abstract 和 Conclusion 的泛化程度超出实验支撑**

- 具体位置：Abstract ("the only consistently effective mechanism"), Section 6 Deployment implications
- 问题：
  - Abstract 声称 "Classification-based domain adaptation is the only consistently effective mechanism on synthetic multi-turn attacks"——"synthetic" 限定词容易被忽略，且读者最关心的是 real-world 表现。
  - Conclusion 的 Deployment implications 建议 "at base scale (125–184M), any domain-relevant classification objective recovers OOD detection; scrambled labels perform equivalently on template attacks"，但这仅在合成数据上验证。人工数据上的反转结果（Section 4.6）使得部署建议的基础不稳固。
  - "Few-shot benign adaptation substantially reduces false-positive inflation across deployment platforms" 中的 "substantially" 是在 FPR 从 68.1% 降到 ~1.5% 的语境下，但这要求 10-25 条 benign conversations 的 per-platform calibration——这个前提条件应在 abstract 中提及。
- 建议修改方向：在 abstract 中增加一句关于人工数据反转的 hedge；Conclusion 的部署建议需明确标注 "在合成评估条件下"。

---

### Should-Fix（需要改进但不阻碍接收）

**[W1] [warning] 自创术语过多，增加认知负荷**

- 具体位置：Section 4.3 ("evidence hierarchy", "discriminative compression"), Appendix L ("partition sufficiency"), Section 1 ("disentangled")
- 问题："Evidence hierarchy" 实际是 "factor importance ranking"；"discriminative compression" 描述的是分类变体将表征压缩到更少 SVD 维度的现象（Appendix S.1, Figure 10），可以更直白地表述为 "classification-induced low-rank structure"；"partition sufficiency" 在正文中被引用但仅在 Appendix L 定义。这些术语的引入并未带来对应的概念清晰度提升。
- 建议：减少自创术语，用已有的 ML 术语替代（如 "factor importance ordering" 替代 "evidence hierarchy"，"representation compression" 替代 "discriminative compression"）。

**[W2] [warning] 人工数据验证不足以支撑多轮检测的 claim**

- 具体位置：Section 4.6, Limitations
- 问题：人工数据验证仅在 ToxicChat（Lin et al., 2023）上进行，而 ToxicChat 是**单轮** LMSYS 用户交互数据。论文将此呈现为 "Human Data Validation"（Section 4.6 标题），但这无法验证多轮检测的核心主张。论文在 Limitations 中承认"no human-generated multi-turn jailbreak data"，但标题仍可能误导读者。
- 更重要的是，hierarchy 在 ToxicChat 上的反转（JB-MLM leads, Figure 4 右侧）引发一个根本问题：如果在唯一的人工数据上分类式 DAPT 不再占优，那么部署到真实用户对话时的期望是什么？
- 建议：(a) 将 Section 4.6 标题改为更准确的描述（如 "Single-Turn Human Data Validation"）；(b) 在 Discussion 中更深入讨论 synthetic-to-human gap 的影响。

**[W3] [warning] Related Work 中 multi-turn defense 的覆盖可以更系统化**

- 具体位置：Section 2, page 3
- 问题：Related Work 对多轮攻击方法覆盖较好（Crescendo, DeceptiveDelight, FTTD, ActorAttack），但对**多轮防御**的讨论较薄。Section 2 提到 "Multi-turn defenses and production safety" 段落中引用了几个 conversation-level 系统，但缺少对以下方向的讨论：
  - Proactive jailbreak detection（在攻击完成前预警）的近期工作
  - LLM-based multi-turn safety guardrails（如 Llama Guard 系列在多轮场景的局限性分析，超出 Section 1 的一句 "1.8%"）
  - 输入/输出过滤 vs. 表征监控的 trade-off 讨论
- 建议：扩展 defense-side related work 约 3-5 句。

**[W4] [warning] BiGRU 的必要性被 mean pooling 等效结果削弱**

- 具体位置：Section 3.3, Appendix T (Table 30)
- 问题：Appendix T 报告 mean pooling 与 BiGRU 在 ID 和 OOD 上表现相当，且 turn-order shuffling 的影响 negligible（Δ < 1 pp）。这意味着 Stage-2 的序列建模（BiGRU）并未捕获有意义的时序依赖，检测主要依赖 per-turn 内容。这对 "multi-turn" 检测的叙事构成一定张力——如果 turn order 不重要，那么 multi-turn 的 "multi" 体现在什么地方？
- 论文在正文中简要提及这一点（"detection relies on per-turn content rather than sequential patterns"），但未充分讨论其对 multi-turn detection framing 的影响。
- 建议：在 Discussion 中增加 1-2 句讨论，解释为什么即使 turn order 不重要，multi-turn aggregation 仍有价值（例如，渐进式累积恶意 intent 需要跨轮聚合 evidence）。

---

### Minor（小问题）

**[M1]** Table 2 中部分 cell 报告 seed mean ± std 而其他不报告（如 TF-IDF LR 行只报告单值），格式不统一。

**[M2]** Figure 2 和 Figure 3 的 y 轴标签（"F1 Score"）未明确是 macro F1 还是 binary F1，需要在 caption 中澄清。正文中交替使用 "F1" 和 "macro F1"，应保持一致。

**[M3]** Section 4.3 提到 "McNemar's test confirms equivalence"，但 McNemar's test 是差异性检验而非等价性检验。论文同时使用了 TOST 等价性检验（Appendix L），这是正确的做法，但正文中 McNemar's test 的表述应修正为 "McNemar's test finds no significant difference"。

**[M4]** 正文中 "24.3× speedup" 的比较基准是 Qwen3-8B 3-shot（Table 33），但正文未明确说明是哪个 LLM-as-judge baseline。速度比较应在首次提及时就明确基准。

**[M5]** Figure 1 信息密度较高，Stage 1 和 Stage 2 的视觉分离可以更清晰（如用不同底色区分）。

---

## Questions for Authors

**[Q1]** Evidence hierarchy 在 ToxicChat 上反转（Figure 4），那么对于部署在真实用户对话上的检测器，论文的实际推荐是什么？是使用 classification DAPT（合成数据验证）还是 MLM（人工数据验证）？

**[Q2]** 在 355M 规模下 DAPT "becomes unnecessary and potentially counterproductive"（Section 5）。这是否暗示 classification DAPT 的收益主要是在补偿模型容量不足，而非学习了真正有用的领域表征？

**[Q3]** Scrambled labels 在模板攻击上有效但在策略多样攻击上失效。能否提供更深入的分析解释*为什么*——是否与攻击 pattern 的规律性有关？是否存在一个可量化的指标（如模板 entropy）可以预测 scrambled labels 何时有效？

**[Q4]** BiGRU 与 mean pooling 等效（Appendix T），这是否意味着模型实际上在做"多个单轮检测的聚合"而非真正的"多轮对话理解"？如果是，这对论文的 framing 有何影响？

**[Q5]** 论文报告 9-class DAPT 在 50 条训练样本时就达到 near-saturation（Table 34, Appendix W）。这对 domain adaptation 的实际成本意味着什么——是否意味着极少量标注数据就足以获得类似效果？

---

## Missing References

- 论文讨论了 "discriminative compression" 但未引用 representation compression/pruning 的相关理论工作。Arora et al. (2019, "A theoretical analysis of contrastive unsupervised representation learning") 或 similar work on why supervised pretraining induces low-rank structure 可以提供理论基础。
- Proactive/early multi-turn jailbreak detection 的近期工作如果存在应引用，以区分本文的 "post-hoc detection" 定位。

---

## 格式合规检查

| 检查项 | 结果 |
|--------|------|
| 正文页数 ≤ 8 | ✅ 正文结束于第 8 页（Section 6 Conclusion），Limitations 从第 9 页开始 |
| Abstract ≤ 200 words | ✅ 约 168 words |
| ACL 模板 [review] 模式 | ✅ 使用 Anonymous ACL submission |
| Double-blind 匿名 | ✅ 代码链接使用 anonymous URL（脚注 1） |
| Limitations section | ✅ 第 9 页，3 个要点，长度适当 |
| ARR Checklist | ✅ 未嵌入 PDF（符合 EMNLP 2026 要求，应在 OpenReview form 填写） |
| 参考文献格式 | ✅ 格式基本一致，使用 ACL natbib 样式 |
| AI 使用披露 | ✅ 第 25 页 "Use of AI Assistants" 段落完整披露 |

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨，因子分解干净，统计检验充分（TOST、McNemar's、permutation tests）。但核心 claim（evidence hierarchy）在多个条件下不成立（人工数据反转、大规模失效、攻击类型依赖），且 abstract/conclusion 的泛化程度超出数据支撑。 |
| Excitement | 2.5/5 | Classification DAPT > vanilla/MLM 是 Gururangan et al. (2020) 的可预期推论，新颖性有限。Scrambled labels 发现有趣但适用范围窄（仅模板攻击）。整体属于 "careful validation of known principles in a new domain" 而非 "surprising insight"。 |
| Reproducibility | 4/5 | 匿名代码链接、详细超参数（Appendix N）、seed-level reporting（Appendix Z）、数据生成流程描述充分。唯一扣分点：训练数据依赖 Qwen3-8B 生成，未提供具体 prompt template。 |
| Overall Assessment | **3.0** — **Findings** | 一篇执行扎实的实证消融研究，提供了有用的因子分解洞察和实用的部署方案。但核心发现的新颖性受限于与已有 DAPT 文献的高度重叠，且 evidence hierarchy 的条件依赖性削弱了其作为通用指导原则的价值。适合 Findings track。 |
| Confidence | 4/5 | 熟悉 DAPT 文献、多轮越狱攻防和 encoder-based 安全分类器设计。 |

---

## 一句话总结

一篇方法论上严谨但新颖性有限的实证消融研究：核心发现（Classification DAPT 有效）可预期于已有文献，最有价值的 scrambled labels 发现适用范围受限，且 evidence hierarchy 在人工数据和大规模模型上反转，削弱了论文的通用性主张。推荐 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2206 · 2026-05-25T21:23:43.362594+00:00_

Reviewer 2 审稿意见已收到。核心评分：**3.0 (Findings)**，置信度 4/5。

主要发现：3 个 Must-Fix（新颖性有限、evidence hierarchy 条件依赖、叙事过度泛化）+ 4 个 Should-Fix + 5 个 Minor。

等待 Reviewer 1 返回审稿意见后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 178

## Round 178

2 recorded events


### User

_source line 2207 · 2026-05-25T21:23:58.281247+00:00_

[Reviewer 2 审稿结果]:
审稿完成。核心评价：

- **Overall: 3.0 (Findings)**，Soundness 3.5，Excitement 2.5，Confidence 4/5
- **3 个 Must-Fix**：(1) Classification DAPT > vanilla/MLM 是 Gururangan et al. (2020) 的可预期推论，新颖性有限；(2) "evidence hierarchy" 在人工数据/大规模/策略多样攻击上反转，不应作为核心贡献；(3) Abstract 和 Conclusion 的泛化程度超出实验支撑
- **4 个 Should-Fix**：术语过多、人工数据验证不足（ToxicChat 是单轮）、defense-side related work 覆盖薄、BiGRU 与 mean pooling 等效削弱多轮叙事
- **优势**：因子分解设计严谨、scrambled labels 发现有实证价值、附录实验极其详尽、实用部署方案清晰
- **格式合规**：全部通过（8 页正文、~168 词 abstract、匿名化、Limitations 存在）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2208 · 2026-05-25T21:24:10.044119+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成独立审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 179

## Round 179

6 recorded events


### User

_source line 2209 · 2026-05-25T21:29:23.228056+00:00_

[Reviewer 1 审稿意见]:

## Summary

DisPeD 提出了一个两阶段 encoder adaptation 框架用于多轮越狱检测，通过 7 个 Stage-1 DeBERTa-v3 变体的控制消融实验，系统性地隔离影响检测的单一因素（分类粒度、标签正确性、监督必要性、任务类型、领域特异性）。核心发现是分类式 DAPT（尤其 9-class 说服策略分类）在合成 OOD 攻击上显著优于 MLM 和无适应基线（F1 0.97–1.0 vs. 0.26–0.31），但在人类数据（ToxicChat）上证据层级完全反转（MLM 0.837 >> 9-class 0.596），且 WildChat 上 9-class 的 FPR 高达 68.1%——高于 vanilla 和 MLM——揭示分类式 DAPT 可能加剧而非缓解了 synthetic-to-real gap。

## Strengths

[S1] **系统性因子分析框架**：7 个 Stage-1 变体的设计在安全领域的 encoder adaptation 研究中少见。Table 1 清晰列出每个变体隔离的因素和测试的假设，Binary vs 9-class 测试粒度、Scrambled 测试标签正确性、MLM-only 测试监督必要性、Topic 测试任务类型、Wiki-MLM 测试领域特异性。这种因子分析思路本身就是方法论贡献。

[S2] **统计工具箱的深度与规范性**：论文综合使用了 TOST 等价检验（Section 4.3）、Bootstrap CI、paired permutation test（Section 4.3）、McNemar's test、CKA 相似性分析（Figure 10, Table 27）、SVD 方向必要性分析（Table 28-29）、Fisher ratio layer-wise 分析（Figure 10）。3-seed 报告均提供 mean±std。这套统计工具链在 NLP 安全论文中是超出常规的。

[S3] **长度混淆的多层次分析**：Appendix U 的处理相当充分：(1) K=1 前缀分析消除长度差异后 9-class 仍达 F1=0.772（ActorAttack），(2) vanilla BiGRU 同样有长度信息但 recall<2.6%（排除长度作为充分特征），(3) WildChat FPR 按轮数分层不支持"短=越狱"捷径（Table 31-32），(4) last-turn-only 截断实验进一步排除多轮结构依赖。

[S4] **Representation geometry 的机制性证据**：Figure 6 的 SVD 投影直观展示 9-class DAPT 产生清晰的聚类分离而 vanilla 没有；Figure 10 的 layer-wise CKA/Fisher ratio 分析定位判别性压缩集中在中间层（layers 8-12）；Table 27 的 PR/Fisher/权重距离量化了压缩程度。这些分析为"为什么 DAPT 有效"提供了超越 accuracy 数字的理解。

[S5] **诚实报告 negative findings**：论文没有回避 ToxicChat 层级反转（Section 4.6）、WildChat FPR 68.1%（Section 4.8）、mixed-LLM 训练中 MLM 崩溃（Section 4.5）、1000 样本性能下降（Appendix J）等不利结果，而是正面讨论并尝试解释。这种学术诚实值得肯定。

## Weaknesses

### Must-Fix (阻碍接收的关键问题)

**[N1] ToxicChat 证据层级完全反转，机制解释深度与问题严重性不匹配**

- 具体位置：Section 4.6, Table 5, Figure 4
- 问题：论文的核心 claim 是分类式 DAPT 产生的编码器表示优于无监督 MLM。但在 ToxicChat（204 条人类书写的越狱尝试，来自真实 LMSYS 用户交互）上，JB-MLM (0.837±0.013) 显著优于 9-class (0.596±0.087)，差距达 24pp（p<0.001，论文原文）。这不是"略差"而是**大幅落后**。

  关键逻辑缺口：论文解释为"ToxicChat is single-turn, so the classification head provides no advantage"（Section 4.6）。这解释了为什么 9-class **不比** MLM 好，但没有解释为什么 9-class 比 MLM **差了 24pp**。如果分类目标仅仅是"不必要的额外信号"，两者应该近似相等（因为 [CLS] embedding 的基础语义信息是共享的）。24pp 的差距意味着分类目标主动**损害**了 encoder 对真实人类越狱的判别能力——这指向合成数据 artifacts 的过拟合，而非仅仅是"信息冗余"。

  Section 4.6 仅两段讨论这个发现，而附录中也没有 ToxicChat 上的 error analysis。对一个直接威胁论文核心 claim 的发现，这个讨论深度完全不够。

- 为什么影响接收：ToxicChat 是论文中唯一的真实人类数据评估。如果论文推荐的最优方法（9-class DAPT）在最具现实意义的评估上表现最差，则论文的实用价值主张（Section 5 "Deployment implications"）需要根本性重新审视。
- 建议修改方向：(1) 提供 9-class 在 ToxicChat 上的详细 error breakdown——FP vs FN 占比？哪类 ToxicChat 对话被系统性误判？(2) 对比 9-class 和 MLM 在 ToxicChat 上的 [CLS] embedding 分布——是否可以量化 9-class 编码器引入的 synthetic artifact？(3) 在 Discussion 中明确限定 claim 适用范围：9-class DAPT 优势限于**合成多轮**场景；在人类单轮数据上，MLM 更可靠。当前 Section 5 的 deployment 建议未反映此区分。

**[N2] 数据规模与测试集过小，7 个变体的精细排序缺乏统计 power 支撑**

- 具体位置：Section 4.1, Tables 2-5, Appendix B (Tables 7-8), Appendix N
- 问题：训练集仅 350 条对话（250 Crescendo + 100 benign）。Appendix N 确认 OOD 测试集为 80 jailbreak + 38 benign = 118 条，ID 测试集更小。在 118 条样本上用 3 seeds 报告 7 个变体的精细 F1 排序，统计 power 严重不足：

  (a) **3 seeds 仅提供 2 个自由度**：标准差估计的相对误差为 ~50%（χ² 分布，df=2）。当报告"0.997±0.005 vs 0.993±0.003"（9-class vs Scrambled on DD, Table 3）时，这个 0.4pp 差异完全在噪声范围内。

  (b) **小测试集上的 F1 离散性**：118 条样本中每个样本的正确/错误切换可导致 F1 变化约 0.85pp。Table 8 (Appendix C) 显示 ActorAttack 在不同 prefix 下的 F1 标准差高达 0.115（MLM-only），说明结果对数据划分和随机种子高度敏感。

  (c) **Evidence hierarchy（Figure 2）的排序可能不稳健**：当 Binary (1.000) > Scrambled (0.997) > 9-class (0.997) > MLM (0.963) 的差异全部在 ±1-4pp 范围内且置信区间重叠时，将其展示为有序 hierarchy 可能误导读者。

- 为什么影响接收：控制实验的核心价值在于可重复性和结论鲁棒性。在 118 条测试样本 + 3 seeds 的基础上得出 7 个变体的精细排序，任何单个样本的随机分配变化都可能改变排序。
- 建议修改方向：(1) 增加 seeds 至 ≥10（Stage-2 训练仅需 <5 分钟/变体，计算成本极低）。(2) 对 evidence hierarchy 使用 Friedman 检验或 Nemenyi post-hoc test 而非仅基于均值排序。(3) 在主文中加入 power analysis 或效应量置信区间讨论。(4) 在 Figure 2 中加入误差棒并讨论排序的置信水平。

**[N3] WildChat FPR 68.1% 揭示 9-class DAPT 加剧 synthetic-to-real 偏差**

- 具体位置：Section 4.8, Table 20 (Appendix P), Figure 5
- 问题：在 226 条 WildChat GPT-3.5 用户真实对话上，9-class FPR = 68.1%±6.4（3-seed, Table 20），而 vanilla ≈48.1%，MLM ≈44.5%。9-class 的 FPR 在所有变体中**最高**，这直接矛盾了论文将 9-class 定位为最佳实践的结论。

  这个发现与 N1（ToxicChat 反转）指向同一根因：9-class 的分类目标使编码器过拟合于 Qwen3-8B 合成对话的分布特征（如特定句法模式、回复风格、话题分布），而非学到可迁移的越狱语义信号。分类任务的更强监督反而加深了这种 domain-specific overfitting。

  论文提出 few-shot benign adaptation（10-25 条 WildChat 对话）可将 FPR 降至 <5%（Figure 5, Section 4.8）。但这引出关键未回答问题：calibration 后 7 个变体的 evidence hierarchy 是否改变？如果 calibration 后所有变体 FPR 都 <5%，9-class 的"优势"可能仅在 pre-calibration 时才存在，而 calibration 本身才是真正起作用的因素。

- 为什么影响接收：Section 5 的 deployment implications 推荐 9-class DAPT 作为首选策略，但未充分提示 deployment 时 9-class 的误报率是最高的（比 vanilla 高 20pp），必须依赖额外的 calibration 步骤。
- 建议修改方向：(1) 在 Section 5 中将 "9-class 需要 mandatory calibration" 提升为核心 deployment 约束而非脚注。(2) 报告 few-shot calibration 后各变体的完整 evidence hierarchy——如果排序改变，这是关键结果。(3) 分析 WildChat 误报的 error pattern：哪些类型的良性对话被 9-class 误判为越狱？

### Should-Fix (需要改进但不阻碍接收)

**[W1] TOST 等价检验 δ=5pp margin 缺乏 practical significance 论证，且 ActorAttack 非等价结果被弱化**

- 具体位置：Section 4.3, Table 16 (Appendix L)
- 问题：δ=5pp 的选择缺乏基于部署需求的论证。在 F1 从 0.95 到 1.00 的范围内，5pp 对应 error rate 从 5% 到 10%——翻倍的错误率在实际部署中并非可忽略。

  更重要的是，Table 16 显示 scrambled vs 9-class 在 ActorAttack 上**未通过**等价检验（TOST p=0.183 > 0.05, d=0.44），即标签正确性对策略多样攻击确实有显著影响。但主文 Section 4.3 将此描述为"moderate label sensitivity"，措辞过于温和。d=0.44 是 Cohen's d 中等效应量，表示两组分布有实质性差异。这削弱了论文"label correctness is not a core detection factor"的笼统结论——更准确的表述应该是"label correctness matters for strategy-diverse attacks but not for template-based attacks"。

- 建议：(1) 提供 δ 选择的基于场景的论证。(2) 补充 δ=2pp 和 δ=3pp 的敏感性分析。(3) 在主文中更突出地报告 ActorAttack 上的非等价结果，修正"label correctness doesn't matter"的笼统 claim。

**[W2] 缺少与已发表 multi-turn defense 方法的直接实验对比**

- 具体位置：Section 2 (Related Work), Appendix Q
- 问题：论文引用了 DeepContext (Albrethen et al., 2026)、BIID (Tong et al., 2025)、G-Guard (Huang et al., 2025) 等方法但未直接实验对比。Appendix Q 的 BERT-base proxy comparison 仅对比了两个 vanilla encoder（BERT-base vs DeBERTa-v3），而非完整方法。论文声称"absent public implementations preclude direct comparison"，但若这些方法在论文中被引用为同一问题的解法，读者期望至少看到：(a) 为何无法复现的具体原因（代码未公开 vs 数据不同 vs 框架差异），(b) 在相同攻击框架上的 reported numbers 对比（如果有共同基准）。
- 建议：(1) 在 Related Work 或 Appendix 中为每个方法明确列出不可比原因。(2) 如果 DeepContext 使用 Crescendo 攻击，至少做间接 reported-number 对比。(3) 在 Limitations 中独立列出此项。

**[W3] Topic 变体的混淆因素：5 类 vs 9 类的粒度差异**

- 具体位置：Section 3.2, Table 1
- 问题：Topic 变体使用 5 类话题分类（technology, health, finance, education, general），而 9-class 使用 9 类策略分类。Topic vs 9-class 的比较同时改变了两个因素：(a) 任务相关性（通用话题 vs 说服策略）和 (b) 分类粒度（5 类 vs 9 类）。Table 3 中 Topic 在 ActorAttack 上表现极差（0.541±0.207），但这究竟是因为话题分类任务无关，还是因为 5 类太粗？论文无法区分。
- 建议：增加一个 9-class topic 变体（细分为 9 个话题子类），或在讨论中明确承认此混淆。这不影响论文的主要结论，因为 Binary（2 类）的强表现已证明粒度本身不是问题，但实验设计的严谨性需要这个 caveat。

**[W4] Mixed-LLM 实验揭示的单源合成数据局限性在 Discussion 中权重不足**

- 具体位置：Section 4.5, Table 13 (Appendix K), Section 5 Discussion
- 问题：混合 LLM 训练（250 Qwen + 250 Llama 对话）导致 MLM 崩溃至 vanilla 水平（Section 4.5），而 classification-based DAPT 保持稳定。但 cross-LLM 验证（Table 11, Appendix H）显示所有模型仅在 Qwen3-8B 数据上训练——这意味着整个实验的 evidence hierarchy 可能是 Qwen3-8B 特定的。

  Section 5 Discussion 提到"single LLM (Qwen3-8B) synthetic data" 作为 limitation，但仅一句话带过。结合 N1（ToxicChat 反转）和 N3（WildChat 高 FPR），单源合成数据可能是这三个问题的共同根因。如果论文能在 Discussion 中将这三个发现统一归因并深入分析，整体论证会更有说服力。

- 建议：在 Discussion 中增加一段统一分析：9-class DAPT 的合成 OOD 优势、ToxicChat 反转、WildChat FPR 最高这三个看似矛盾的发现，可能都源于同一机制——分类目标使编码器更紧密地拟合 Qwen3-8B 合成对话的分布特征。

**[W5] Dataset scale validation (Table 14) 存在 71% test-set overlap，且性能下降解释不充分**

- 具体位置：Table 14 (Appendix J)
- 问题：将训练集从 350 扩展至 1000 条对话时，71% 的原始测试集出现在扩展训练集中。论文正确省略了 ID 结果，但：(a) 这暴露了数据生成流程缺乏 deduplication 机制——71% overlap 意味着 Qwen3-8B 在不同 seed 下生成了高度相似的对话，这对 350 样本训练集的 effective diversity 提出质疑；(b) OOD 结果显示 9-class 性能**反降**（DD OOD 从 ~1.0 降至 0.889, AA OOD 从 ~0.97 降至 0.915），论文将此归因于"distributed heterogeneity from diverse topic seeds"但缺乏具体验证。
- 建议：(1) 讨论 71% overlap 对 350 样本训练集 diversity 估计的影响。(2) 对 1000 样本 OOD 性能下降做更详细归因（是特定攻击类型 F1 下降还是全面下降？）。

### Minor (小问题)

[M1] Section 4.1 数据划分描述中 "split into train (76%), validation (7%), and test (7%)" 仅加总 90%，余下 10% 未解释。若为排版 typo（如 test 应为 17%），请更正。

[M2] Figure 2 的 evidence hierarchy bar chart 仅展示 ID + OOD Full（最有利条件）的单一快照。附录中不同 prefix 长度下排序变化（Table 7-8）暗示层级在 K=1 和 K=2 时有所不同，但 Figure 2 未反映这种条件依赖性，可能给读者过度简化的印象。

[M3] Appendix Y 显示 9-class 的策略预测在 OOD 上 κ=0.126（接近随机），但 Section 4.3 引用此结果时的讨论深度不够。如果 9-class DAPT 的策略预测在 OOD 上不准确，那"classification-based DAPT"的优势到底来自分类任务的什么方面？论文认为是 [CLS] embedding 的判别性压缩（Figure 10），但可以更明确地论证。

[M4] Table 6（LLM-as-judge）仅测试了 Qwen3-8B 和 Llama Guard 3。未测试更强的 LLM（如 GPT-4o），可能低估了 LLM-as-judge 在此任务上的上限。虽然 LLM-as-judge 不是论文重点，但作为 baseline 其强度直接影响论文的贡献定位。

[M5] TF-IDF 在 DD 上达到 F1=1.0（Table 2），在 FITD 上也接近满分（Table 2 脚注表明 TF-IDF is deterministic, 1 run），说明这两个 OOD 基准可能存在 lexical shortcut。虽然 ActorAttack 的 TF-IDF F1=0.261 证明了非词汇特征的必要性，但论文应简要讨论 DD/FITD 作为 OOD 基准的挑战性。

## Questions for Authors

[Q1] ToxicChat 上 9-class (F1=0.596) 比 MLM (0.837) 差 24pp。能否提供 9-class 在 ToxicChat 上的 confusion matrix——主要失败模式是 FP（良性判为越狱）还是 FN（越狱判为良性）？

[Q2] Few-shot benign calibration（10-25 条对话）将 WildChat FPR 降至 <5%。calibration 后 7 个 Stage-1 变体的 evidence hierarchy 是否改变？如果 calibration 后排序一致，请报告具体数值。

[Q3] TOST δ=5pp 的选择是否有部署场景的经验依据？在 F1=0.95 到 1.00 区间，5pp 对应 error rate 翻倍。是否做过 δ=2pp 或 δ=3pp 的敏感性分析？

[Q4] Table 14 中 1000 样本扩展出现 71% test-set overlap。这是否暗示 Qwen3-8B 在不同 topic seed 下生成的对话有大量重复？如果是，350 样本训练集的 effective diversity 是否被高估了？

[Q5] Scrambled 在 ActorAttack 上未通过 TOST 等价检验（p=0.183, d=0.44）。这似乎意味着对策略多样攻击而言标签正确性确实重要。为什么主文结论仍概括为"label correctness is not a core detection factor"而未加限定条件？

[Q6] 为什么不在 Stage-1 训练中混入少量 real-world benign 对话（如 OASST2/WildChat）作为 domain regularization，而是将 synthetic-to-real calibration 推迟到 deployment 阶段？这似乎是一个显而易见的改进，论文是否做过这类实验？

## Missing References

论文的 Related Work 已较为全面。建议补充：
- 如果存在其他使用 controlled ablation 研究 encoder DAPT 在 NLP 安全任务中效果的工作，可加强 positioning（如 probing 文献中 Belinkov et al., Hewitt & Manning 等在安全领域的延伸）

## Overall Assessment

**Score: 3.0 (Findings)**

**一句话总结**：实验设计的系统性出色，但三个核心发现（合成 OOD 优势、ToxicChat 反转、WildChat 最高 FPR）相互矛盾，当前讨论深度与 claim 的谨慎度与发现的复杂性不匹配。

论文提出了有价值的研究问题，7 个 ablation 变体的因子分析框架和多层统计工具链在 NLP 安全领域是值得推广的方法论贡献。长度混淆分析（Appendix U）和 representation geometry 分析（Figures 6, 10）都体现了研究者的方法论自觉。

但论文的三个主要结论实际上相互紧张：(1) 9-class DAPT 在合成 OOD 上最优；(2) 9-class DAPT 在人类数据 ToxicChat 上比 MLM 差 24pp；(3) 9-class DAPT 在 WildChat 上 FPR 最高（68.1%，高于 vanilla 20pp）。这三个发现可能有统一的解释（分类目标加深了对合成数据分布的拟合），但论文未做这种统一归因分析。Section 5 的 deployment implications 过于乐观，未充分反映 (2) 和 (3) 对实用价值的约束。

数据规模局限（350 对话、118 条 OOD 测试、3 seeds）使得 7 个变体的精细排序（Figure 2 的 evidence hierarchy）缺乏充分的统计 power 支撑。排序中的关键差异（如 9-class vs Binary vs Scrambled）全部在 1-4pp 范围内，远小于抽样误差。

如果作者能 (1) 统一分析三个矛盾发现的共同根因，(2) 收窄 claim 至合成多轮场景并诚实修正 deployment 建议，(3) 增加 seeds 至 ≥10 并报告 calibration 后的 hierarchy，论文有潜力升至 Conference 水平。当前版本适合 Findings。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 核心 claim 在合成 OOD 上有支撑，但在人类数据上被直接反驳且解释不足；统计 power 受限于 3 seeds + 118 样本 |
| Excitement | 3/5 (Interesting) | 研究问题有价值（encoder adaptation 的系统性因子分析），方法论框架可推广，但结论的条件性和 real-world 局限降低了 take-away 的清晰度 |
| Reproducibility | 4/5 | 匿名代码/数据链接已提供（footnote 1），超参数报告详尽（Appendix N），Stage-2 训练成本低（<5 分钟/变体），但 Qwen3-8B 合成数据的生成 prompt 可再现性取决于 API 版本 |
| Datasets | 3/5 (Potentially useful) | 350 条合成对话规模有限，但 9-class 策略标注 taxonomy + inter-annotator agreement (κ=0.78) 有参考价值 |

**Confidence: 4/5** — 多轮安全和 encoder adaptation 是我熟悉的领域，论文的统计方法我已仔细验证，但 ToxicChat/WildChat 的 error pattern 需要更多信息才能完全判断。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2210 · 2026-05-25T21:30:17.194983+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "persuasion_turn_jailbreak_detect",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n## Summary\n本文提出 DisPeD，一个因子化消融框架，将 DeBERTa 编码器的 7 种预训练目标与固定的 BiGRU 分类器解耦，在 3 个模型规模和 4 个攻击家族上系统研究 domain exposure、supervision type、label semantics 对 OOD 越狱检测的贡献。核心发现：分类式 DAPT 是合成数据上唯一稳定恢复 OOD 检测的机制（F1 0.97–1.0 vs. vanilla 0.26–0.31）；scrambled labels 在模板攻击上等效于正确标签；但该 hierarchy 在人工数据（ToxicChat）上反转。\n\n## Strengths\n[S1] 实验设计严谨，因子分解干净。7 种 Stage-1 变体共享相同的训练数据和 Stage-2 分类器，仅在预训练目标上不同（Table 1）。\n[S2] Scrambled labels 发现具有实证价值。揭示分类目标的结构角色（而非标签语义）驱动泛化。\n[S3] 消融深度远超同类工作。Appendix 提供极其详尽的补充实验。\n[S4] 实用价值清晰。184M 参数管线，24.3× 加速和 few-shot benign adaptation。\n[S5] 写作结构整体清晰。\n\n## Weaknesses\n\n### Must-Fix\n[N1] [critical] 核心发现的新颖性有限——Classification DAPT 优于 vanilla/MLM 是 Gururangan et al. (2020) DAPT 框架的可预期推论。论文本质上是在一个新领域验证了已知原理。Scrambled labels 发现更具新颖性，但适用范围受限于模板攻击。\n\n[N2] [critical] \"Evidence hierarchy\" 在多个现实条件下反转（人工数据、大规模、策略多样攻击、LLM 来源依赖），但被作为核心贡献呈现。一个在多个现实场景下反转的 hierarchy 不应被称为\"hierarchy\"——它更像是一组条件依赖的观察。\n\n[N3] [critical] 叙事一致性问题——Abstract 和 Conclusion 的泛化程度超出实验支撑。Abstract 声称 \"the only consistently effective mechanism on synthetic multi-turn attacks\"——\"synthetic\" 限定词容易被忽略。Conclusion 部署建议基础不稳固。\n\n### Should-Fix\n[W1] [warning] 自创术语过多（evidence hierarchy, discriminative compression, partition sufficiency），增加认知负荷。\n[W2] [warning] 人工数据验证不足——ToxicChat 是单轮数据，标题\"Human Data Validation\"可能误导。\n[W3] [warning] Related Work 中 multi-turn defense 的覆盖可以更系统化。\n[W4] [warning] BiGRU 的必要性被 mean pooling 等效结果削弱，对 multi-turn 叙事构成张力。\n\n### Minor\n[M1] Table 2 seed 报告格式不统一。\n[M2] Figure 2/3 未明确 macro F1 vs binary F1。\n[M3] McNemar's test 表述应修正为\"finds no significant difference\"而非\"confirms equivalence\"。\n[M4] \"24.3× speedup\" 首次提及时未明确基准。\n[M5] Figure 1 信息密度高，Stage 1/2 视觉分离可更清晰。\n\n## Questions\n[Q1] ToxicChat 反转下的实际部署推荐是什么？\n[Q2] 355M DAPT counterproductive 是否暗示 DAPT 收益主要补偿容量不足？\n[Q3] Scrambled labels 模板攻击有效但策略多样攻击失效的深层原因？\n[Q4] BiGRU ≈ mean pooling 是否意味着模型做的是\"多个单轮检测的聚合\"？\n[Q5] 50 条训练样本 near-saturation 对实际标注成本的影响？\n\n## Missing References\n- Representation compression 理论工作（Arora et al., 2019）\n- Proactive/early multi-turn jailbreak detection 近期工作\n\n## Overall Assessment\nScore: 3.0 (Findings), Soundness 3.5, Excitement 2.5, Confidence 4/5\n\n---\n\n请对以上每条意见逐一 [AGREE] 或 [REBUT]，并说明理由。特别关注你与 R2 在以下问题上是否有分歧：\n1. 新颖性评估（R2-N1）\n2. \"Evidence hierarchy\" 的条件依赖性（R2-N2）\n3. Abstract/Conclusion 的 overclaiming（R2-N3）\n4. BiGRU vs mean pooling 对多轮叙事的影响（R2-W4）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "persuasion_turn_jailbreak_detect",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n## Summary\n本文提出 DisPeD，一个因子化消融框架，将 DeBERTa 编码器的 7 种预训练目标与固定的 BiGRU 分类器解耦，在 3 个模型规模和 4 个攻击家族上系统研究 domain exposure、supervision type、label semantics 对 OOD 越狱检测的贡献。核心发现：分类式 DAPT 是合成数据上唯一稳定恢复 OOD 检测的机制（F1 0.97–1.0 vs. vanilla 0.26–0.31）；scrambled labels 在模板攻击上等效于正确标签；但该 hierarchy 在人工数据（ToxicChat）上反转。\n\n## Strengths\n[S1] 实验设计严谨，因子分解干净。7 种 Stage-1 变体共享相同的训练数据和 Stage-2 分类器，仅在预训练目标上不同（Table 1）。\n[S2] Scrambled labels 发现具有实证价值。揭示分类目标的结构角色（而非标签语义）驱动泛化。\n[S3] 消融深度远超同类工作。Appendix 提供极其详尽的补充实验。\n[S4] 实用价值清晰。184M 参数管线，24.3× 加速和 few-shot benign adaptation。\n[S5] 写作结构整体清晰。\n\n## Weaknesses\n\n### Must-Fix\n[N1] [critical] 核心发现的新颖性有限——Classification DAPT 优于 vanilla/MLM 是 Gururangan et al. (2020) DAPT 框架的可预期推论。论文本质上是在一个新领域验证了已知原理。Scrambled labels 发现更具新颖性，但适用范围受限于模板攻击。\n\n[N2] [critical] \"Evidence hierarchy\" 在多个现实条件下反转（人工数据、大规模、策略多样攻击、LLM 来源依赖），但被作为核心贡献呈现。一个在多个现实场景下反转的 hierarchy 不应被称为\"hierarchy\"——它更像是一组条件依赖的观察。\n\n[N3] [critical] 叙事一致性问题——Abstract 和 Conclusion 的泛化程度超出实验支撑。Abstract 声称 \"the only consistently effective mechanism on synthetic multi-turn attacks\"——\"synthetic\" 限定词容易被忽略。Conclusion 部署建议基础不稳固。\n\n### Should-Fix\n[W1] [warning] 自创术语过多（evidence hierarchy, discriminative compression, partition sufficiency），增加认知负荷。\n[W2] [warning] 人工数据验证不足——ToxicChat 是单轮数据，标题\"Human Data Validation\"可能误导。\n[W3] [warning] Related Work 中 multi-turn defense 的覆盖可以更系统化。\n[W4] [warning] BiGRU 的必要性被 mean pooling 等效结果削弱，对 multi-turn 叙事构成张力。\n\n### Minor\n[M1] Table 2 seed 报告格式不统一。\n[M2] Figure 2/3 未明确 macro F1 vs binary F1。\n[M3] McNemar's test 表述应修正为\"finds no significant difference\"而非\"confirms equivalence\"。\n[M4] \"24.3× speedup\" 首次提及时未明确基准。\n[M5] Figure 1 信息密度高，Stage 1/2 视觉分离可更清晰。\n\n## Questions\n[Q1] ToxicChat 反转下的实际部署推荐是什么？\n[Q2] 355M DAPT counterproductive 是否暗示 DAPT 收益主要补偿容量不足？\n[Q3] Scrambled labels 模板攻击有效但策略多样攻击失效的深层原因？\n[Q4] BiGRU ≈ mean pooling 是否意味着模型做的是\"多个单轮检测的聚合\"？\n[Q5] 50 条训练样本 near-saturation 对实际标注成本的影响？\n\n## Missing References\n- Representation compression 理论工作（Arora et al., 2019）\n- Proactive/early multi-turn jailbreak detection 近期工作\n\n## Overall Assessment\nScore: 3.0 (Findings), Soundness 3.5, Excitement 2.5, Confidence 4/5\n\n---\n\n请对以上每条意见逐一 [AGREE] 或 [REBUT]，并说明理由。特别关注你与 R2 在以下问题上是否有分歧：\n1. 新颖性评估（R2-N1）\n2. \"Evidence hierarchy\" 的条件依赖性（R2-N2）\n3. Abstract/Conclusion 的 overclaiming（R2-N3）\n4. BiGRU vs mean pooling 对多轮叙事的影响（R2-W4）"
  }
}
```

</details>

---


### Tool result

_source line 2211 · 2026-05-25T21:30:52.432666+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 35237
}
```

</details>

---


### Tool call

_source line 2212 · 2026-05-25T21:30:52.636658+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "persuasion_turn_jailbreak_detect",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n## Summary\nDisPeD 提出了一个两阶段 encoder adaptation 框架用于多轮越狱检测，通过 7 个 Stage-1 变体的控制消融实验，系统性隔离影响检测的单一因素。核心发现是分类式 DAPT 在合成 OOD 上显著优于 MLM 和无适应基线，但在人类数据上完全反转，且 WildChat 上 9-class FPR 高达 68.1%。\n\n## Strengths\n[S1] 系统性因子分析框架——7 个变体的设计在安全领域少见。\n[S2] 统计工具箱的深度与规范性——TOST、Bootstrap CI、permutation test、McNemar's、CKA、SVD、Fisher ratio。\n[S3] 长度混淆的多层次分析——Appendix U 充分处理。\n[S4] Representation geometry 的机制性证据——SVD、CKA、Fisher ratio layer-wise 分析。\n[S5] 诚实报告 negative findings——ToxicChat 反转、WildChat FPR、mixed-LLM 崩溃、1000 样本性能下降。\n\n## Weaknesses\n\n### Must-Fix\n[N1] [critical] ToxicChat 证据层级完全反转，机制解释深度与问题严重性不匹配。\n- JB-MLM (0.837) 显著优于 9-class (0.596)，差距 24pp（p<0.001）\n- 关键逻辑缺口：论文解释为\"ToxicChat is single-turn, so the classification head provides no advantage\"，但没有解释为什么 9-class 比 MLM **差了 24pp**\n- 24pp 差距意味着分类目标主动**损害**了 encoder 对真实人类越狱的判别能力\n- Section 4.6 仅两段讨论，附录无 error analysis\n- 建议：提供 ToxicChat error breakdown，对比 [CLS] embedding 分布，在 Discussion 限定 claim 范围\n\n[N2] [critical] 数据规模与测试集过小，7 个变体的精细排序缺乏统计 power 支撑。\n- 350 训练对话，OOD 测试集 118 条，仅 3 seeds（2 自由度）\n- 标准差估计相对误差约 50%\n- Evidence hierarchy 中 9-class vs Binary vs Scrambled 差异全在 1-4pp，远小于抽样误差\n- 建议：增加至 ≥10 seeds，Friedman 检验，加误差棒到 Figure 2\n\n[N3] [critical] WildChat FPR 68.1% 揭示 9-class DAPT 加剧 synthetic-to-real 偏差。\n- 9-class FPR 在所有变体中**最高**（比 vanilla 高 20pp）\n- 分类目标使编码器过拟合 Qwen3-8B 合成对话的分布特征\n- 关键未回答问题：calibration 后 7 个变体的 evidence hierarchy 是否改变？\n- 建议：报告 calibration 后完整 hierarchy，分析 WildChat 误报 error pattern\n\n### Should-Fix\n[W1] TOST δ=5pp margin 缺乏 practical significance 论证，ActorAttack 非等价结果被弱化（d=0.44 是中等效应量）。\n[W2] 缺少与已发表 multi-turn defense 方法的直接实验对比。\n[W3] Topic 变体 5 类 vs 9 类的粒度差异混淆。\n[W4] Mixed-LLM 单源合成数据局限性在 Discussion 中权重不足——9-class DAPT 优势、ToxicChat 反转、WildChat 最高 FPR 可能源于同一机制（分类目标加深合成数据拟合）。\n[W5] Dataset scale validation 71% test-set overlap 且性能下降解释不充分。\n\n### Minor\n[M1] 数据划分百分比加总仅 90%。\n[M2] Figure 2 仅展示最有利条件下的 evidence hierarchy。\n[M3] Appendix Y 策略预测 OOD κ=0.126 讨论不足。\n[M4] LLM-as-judge baseline 未测试更强 LLM（如 GPT-4o）。\n[M5] DD/FITD 的 TF-IDF F1=1.0 暗示 lexical shortcut，应讨论这两个基准的挑战性。\n\n## Questions\n[Q1] ToxicChat 9-class 的 confusion matrix——FP 还是 FN 为主？\n[Q2] Few-shot calibration 后 evidence hierarchy 是否改变？\n[Q3] TOST δ=5pp 的部署场景依据？δ=2pp/3pp 敏感性分析？\n[Q4] 1000 样本 71% overlap 是否暗示训练集 effective diversity 被高估？\n[Q5] Scrambled 在 ActorAttack 上未通过 TOST（p=0.183, d=0.44），为何主文结论未加限定？\n[Q6] 为何不在 Stage-1 混入 real-world benign 数据做 domain regularization？\n\n## Missing References\n- Belinkov et al. 在安全领域的 probing 延伸\n\n## Overall Assessment\nScore: 3.0 (Findings), Soundness 3/5, Excitement 3/5, Confidence 4/5\n\n---\n\n请对以上每条意见逐一 [AGREE] 或 [REBUT]，并说明理由。特别关注你与 R1 在以下问题上是否有分歧：\n1. ToxicChat 反转的严重性（R1-N1）——你给出类似 concern (N2) 但 R1 提出了更具体的分析要求（error breakdown, embedding 分布对比）\n2. 数据规模与统计 power（R1-N2）——你未将此列为 Must-Fix，你是否认为 3 seeds + 118 样本足够？\n3. WildChat FPR 最高（R1-N3）——你的 N2/N3 关注 overclaiming，R1 将此独立为 Must-Fix\n4. 单源合成数据统一归因（R1-W4）——你是否同意三个矛盾发现应统一分析？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "persuasion_turn_jailbreak_detect",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n## Summary\nDisPeD 提出了一个两阶段 encoder adaptation 框架用于多轮越狱检测，通过 7 个 Stage-1 变体的控制消融实验，系统性隔离影响检测的单一因素。核心发现是分类式 DAPT 在合成 OOD 上显著优于 MLM 和无适应基线，但在人类数据上完全反转，且 WildChat 上 9-class FPR 高达 68.1%。\n\n## Strengths\n[S1] 系统性因子分析框架——7 个变体的设计在安全领域少见。\n[S2] 统计工具箱的深度与规范性——TOST、Bootstrap CI、permutation test、McNemar's、CKA、SVD、Fisher ratio。\n[S3] 长度混淆的多层次分析——Appendix U 充分处理。\n[S4] Representation geometry 的机制性证据——SVD、CKA、Fisher ratio layer-wise 分析。\n[S5] 诚实报告 negative findings——ToxicChat 反转、WildChat FPR、mixed-LLM 崩溃、1000 样本性能下降。\n\n## Weaknesses\n\n### Must-Fix\n[N1] [critical] ToxicChat 证据层级完全反转，机制解释深度与问题严重性不匹配。\n- JB-MLM (0.837) 显著优于 9-class (0.596)，差距 24pp（p<0.001）\n- 关键逻辑缺口：论文解释为\"ToxicChat is single-turn, so the classification head provides no advantage\"，但没有解释为什么 9-class 比 MLM **差了 24pp**\n- 24pp 差距意味着分类目标主动**损害**了 encoder 对真实人类越狱的判别能力\n- Section 4.6 仅两段讨论，附录无 error analysis\n- 建议：提供 ToxicChat error breakdown，对比 [CLS] embedding 分布，在 Discussion 限定 claim 范围\n\n[N2] [critical] 数据规模与测试集过小，7 个变体的精细排序缺乏统计 power 支撑。\n- 350 训练对话，OOD 测试集 118 条，仅 3 seeds（2 自由度）\n- 标准差估计相对误差约 50%\n- Evidence hierarchy 中 9-class vs Binary vs Scrambled 差异全在 1-4pp，远小于抽样误差\n- 建议：增加至 ≥10 seeds，Friedman 检验，加误差棒到 Figure 2\n\n[N3] [critical] WildChat FPR 68.1% 揭示 9-class DAPT 加剧 synthetic-to-real 偏差。\n- 9-class FPR 在所有变体中**最高**（比 vanilla 高 20pp）\n- 分类目标使编码器过拟合 Qwen3-8B 合成对话的分布特征\n- 关键未回答问题：calibration 后 7 个变体的 evidence hierarchy 是否改变？\n- 建议：报告 calibration 后完整 hierarchy，分析 WildChat 误报 error pattern\n\n### Should-Fix\n[W1] TOST δ=5pp margin 缺乏 practical significance 论证，ActorAttack 非等价结果被弱化（d=0.44 是中等效应量）。\n[W2] 缺少与已发表 multi-turn defense 方法的直接实验对比。\n[W3] Topic 变体 5 类 vs 9 类的粒度差异混淆。\n[W4] Mixed-LLM 单源合成数据局限性在 Discussion 中权重不足——9-class DAPT 优势、ToxicChat 反转、WildChat 最高 FPR 可能源于同一机制（分类目标加深合成数据拟合）。\n[W5] Dataset scale validation 71% test-set overlap 且性能下降解释不充分。\n\n### Minor\n[M1] 数据划分百分比加总仅 90%。\n[M2] Figure 2 仅展示最有利条件下的 evidence hierarchy。\n[M3] Appendix Y 策略预测 OOD κ=0.126 讨论不足。\n[M4] LLM-as-judge baseline 未测试更强 LLM（如 GPT-4o）。\n[M5] DD/FITD 的 TF-IDF F1=1.0 暗示 lexical shortcut，应讨论这两个基准的挑战性。\n\n## Questions\n[Q1] ToxicChat 9-class 的 confusion matrix——FP 还是 FN 为主？\n[Q2] Few-shot calibration 后 evidence hierarchy 是否改变？\n[Q3] TOST δ=5pp 的部署场景依据？δ=2pp/3pp 敏感性分析？\n[Q4] 1000 样本 71% overlap 是否暗示训练集 effective diversity 被高估？\n[Q5] Scrambled 在 ActorAttack 上未通过 TOST（p=0.183, d=0.44），为何主文结论未加限定？\n[Q6] 为何不在 Stage-1 混入 real-world benign 数据做 domain regularization？\n\n## Missing References\n- Belinkov et al. 在安全领域的 probing 延伸\n\n## Overall Assessment\nScore: 3.0 (Findings), Soundness 3/5, Excitement 3/5, Confidence 4/5\n\n---\n\n请对以上每条意见逐一 [AGREE] 或 [REBUT]，并说明理由。特别关注你与 R1 在以下问题上是否有分歧：\n1. ToxicChat 反转的严重性（R1-N1）——你给出类似 concern (N2) 但 R1 提出了更具体的分析要求（error breakdown, embedding 分布对比）\n2. 数据规模与统计 power（R1-N2）——你未将此列为 Must-Fix，你是否认为 3 seeds + 118 样本足够？\n3. WildChat FPR 最高（R1-N3）——你的 N2/N3 关注 overclaiming，R1 将此独立为 Must-Fix\n4. 单源合成数据统一归因（R1-W4）——你是否同意三个矛盾发现应统一分析？"
  }
}
```

</details>

---


### Tool result

_source line 2213 · 2026-05-25T21:30:54.273657+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1636
}
```

</details>

---


### Assistant

_source line 2214 · 2026-05-25T21:30:57.522511+00:00_

交叉分享已发送。等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 180

## Round 180

2 recorded events


### User

_source line 2215 · 2026-05-25T21:31:00.548677+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心评价：**Overall 3.0 (Findings)**，Soundness 3/5，Excitement 3/5，Confidence 4/5。

三个 Must-Fix 问题：
1. **ToxicChat 证据层级反转**（MLM 0.837 >> 9-class 0.596）缺乏机制性解释——24pp 差距意味着分类目标主动损害了对人类数据的判别力，不能仅归因于"single-turn"
2. **数据规模过小**（350 训练、118 OOD 测试、3 seeds），7 个变体间的关键差异（1-4pp）全部在抽样误差范围内，evidence hierarchy 排序不稳健
3. **WildChat FPR 68.1%**——9-class 反而是所有变体中 FPR 最高的（比 vanilla 高 20pp），说明分类式 DAPT 加剧了 synthetic-to-real gap

五个 Should-Fix：TOST δ=5pp 论证不足且 ActorAttack 非等价被弱化、缺少与 DeepContext/G-Guard 的直接对比、Topic 变体 5 vs 9 类混淆、单源合成数据局限在 Discussion 中权重不足、1000 样本扩展的 71% test overlap。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2216 · 2026-05-25T21:31:06.659179+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 181

## Round 181

24 recorded events


### User

_source line 2217 · 2026-05-25T21:34:04.649451+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Strengths

[AGREE] R2-S1: 实验设计的因子分解确实是本文最核心的方法论贡献。7 个变体共享训练数据和 Stage-2 分类器，仅改变 Stage-1 目标（Table 1），这种设计在 NLP 安全领域罕见。我在自己的审稿中也将此列为 S1。

[AGREE] R2-S2: Scrambled labels 发现是论文最具原创性的实证贡献。但需补充一个重要限定：Table 16 (Appendix L) 的 TOST 检验显示 scrambled 在 ActorAttack 上未通过等价检验（p=0.183, d=0.44），即此发现的适用范围限于模板攻击，对策略多样攻击标签正确性仍然重要。R2 已注意到这一点。

[AGREE] R2-S3: Appendix 的深度确实远超同类工作。25 页总计，附录占 17 页，涵盖 length stratification (U)、representation geometry (S)、SVD necessity (Table 28-29)、cross-LLM validation (H)、dataset scale (J) 等。

[AGREE] R2-S4: 184M 参数、24.3× 加速（vs LLM-as-judge）、<5 分钟 Stage-2 训练的实用性值得肯定。但此优势需以 N3 中的 deployment 限制为前提。

[AGREE] R2-S5: 整体写作结构清晰，Section 3 的方法描述和 Section 4 的实验组织有逻辑性。

---

### Must-Fix

[AGREE] R2-N1: **新颖性评估——部分同意，但认为 R2 的措辞略过严苛。**

R2 的核心论点是对的：classification DAPT > vanilla/MLM 是 Gururangan et al. (2020) DAPT 框架在新领域的可预期推论。单纯验证"DAPT 在越狱检测中有效"的新颖性确实有限。

但我认为论文的贡献不仅仅是"验证已知原理"，还包括三层递进：
- **第一层（预期）**：DAPT > vanilla → 低新颖性，同意 R2
- **第二层（非预期）**：Scrambled labels ≈ correct labels on template attacks → 中等新颖性，因为这挑战了"标签语义驱动泛化"的直觉，揭示了分类目标的结构性角色（Table 16, Section 4.3）
- **第三层（最有价值但未被充分开发）**：Evidence hierarchy 在人类数据上完全反转（Table 5, Figure 4）→ 高信息量的 negative finding，但论文对此的讨论深度不够（这也是我的 N1 concern）

所以新颖性问题是**程度性的**而非二元的。论文的问题不在于完全缺乏新颖性，而在于**最具新颖性的发现（反转 + scrambled 条件依赖性）没有被置于叙事中心**，反而被淹没在了相对平凡的 DAPT > vanilla 结论中。如果论文重新组织叙事，以"为什么 DAPT 有效、何时失效"为主轴而非"DAPT 有效"，新颖性评估会改善。

**与我自己审稿的关系**：我的审稿未将新颖性单独列为 Must-Fix，而是将其隐含在 Excitement 评分（3/5）中。R2 给 Excitement 2.5/5，比我更严苛。考虑到 R2 的论点，我认为 2.5-3.0 都是合理区间，但不应低于 2.5。

[AGREE] R2-N2: **"Evidence hierarchy" 的条件依赖性——强烈同意。**

这与我自己的 N1 完全一致。论文将 "evidence hierarchy"（Figure 2, Section 4.3）作为核心贡献呈现，但该 hierarchy 在至少四个现实条件下反转或不稳定：

1. **人类数据**：ToxicChat 上 MLM (0.837) >> 9-class (0.596)，差距 24pp（Table 5, Section 4.6）
2. **策略多样攻击**：Scrambled 在 ActorAttack 上不等价于 9-class（TOST p=0.183, d=0.44, Table 16）
3. **大规模训练**：1000 样本时 9-class OOD 性能反降（DD OOD 0.889 vs ~1.0 at 350 样本, Table 14）
4. **WildChat 部署**：9-class FPR = 68.1%，高于 vanilla (48.1%) 和 MLM (44.5%)（Table 20）

R2 准确指出了问题本质：**一个在多个现实场景下反转的排序不应被称为 "hierarchy"——它是一组条件依赖的观察**。我完全赞同这个判断。论文应将"evidence hierarchy"重新定义为"condition-dependent evidence landscape"或类似表述，并在主文中系统讨论各反转条件。

**补充 R2 未提及的一点**：即使在合成 OOD 的"稳定"条件下，hierarchy 顶部几个变体（9-class, Binary, Scrambled）的差异也全部在 1-4pp 范围内（Table 3: DD-Full 0.997 vs 1.000 vs 0.997），远小于 3-seed 报告的抽样误差。所以即使在最有利条件下，精细排序也可能不稳健。

[AGREE] R2-N3: **Abstract/Conclusion 的 overclaiming——同意。**

Abstract 声称 "classification-based domain adaptation is the only consistently effective mechanism on synthetic multi-turn attacks"。"synthetic" 限定词的位置确实容易被忽略，且与标题 "Multi-Turn Jailbreak Detection"（无 "synthetic" 限定）存在张力。

更关键的是 Section 6 (Conclusion) 和 Section 5 (Discussion) 的 "Deployment implications" 段：该段推荐 "at base scale (125–184M), any domain-relevant classification objective recovers OOD detection" 并提出 few-shot benign calibration 作为部署方案。但推荐中**未提及** ToxicChat 反转和 WildChat FPR 68.1% 对部署的约束。Section 5 最后一段提到 "these advantages condition-specific and counterproductive at 355M"，但对 condition-specific 的讨论不够系统。

这与我自己审稿的 N1 和 N3 一致：论文的 claim 粒度与实验证据的复杂性不匹配。

---

### Should-Fix

[REBUT] R2-W1: **自创术语过多——部分不同意。**

"Evidence hierarchy" 和 "discriminative compression" 是描述性术语，前者概括了 Figure 2 的排序，后者概括了 Figure 10 的 layer-wise CKA/Fisher ratio 分析中观察到的中间层判别性特征压缩现象。在一篇以系统性消融为核心的论文中，这类概括性术语有助于跨 section 的交叉引用，认知负荷的增加是合理的。

但同意 "partition sufficiency" 过于晦涩（仅在 Table 1 和 Appendix M 中使用），可以简化为更直观的表述（如 "binary partition robustness"）。

总体判断：术语问题属于 Minor 级别而非 Should-Fix。论文的术语量在消融研究中是可接受的。

[AGREE] R2-W2: **"Human Data Validation" 标题可能误导——同意。**

Section 4.6 标题为 "Human Data Validation"，但实验结果实际上是一个**负面验证**——论文推荐的方法在人类数据上表现最差。"Validation" 一词暗示确认性结果，但实际内容是反转/失败。更准确的标题应该是 "Human Data Evaluation" 或 "Transfer to Human-Authored Data"。

此外，ToxicChat 确实是单轮数据（Section 4.6 明确指出"ToxicChat is single-turn"），而论文标题聚焦 "Multi-Turn"。用单轮数据做 "validation" 本身就有方法论张力。但公平地说，论文在 Section 4.6 中对此有说明，只是 section 标题不准确。

[AGREE] R2-W3: **Related Work 对 multi-turn defense 的覆盖——同意但补充。**

Section 2 的 "Multi-turn defenses and production safety" 段落引用了 DeepContext、BIID、G-Guard 等方法，但仅用 1-2 句概括，未系统比较各方法的设计维度（如：编码器选择、时序建模方式、训练数据类型、评估攻击范围）。一个结构化的对比表（即使在 Appendix 中）会加强论文的 positioning。这与我自己的 W2 一致。

[AGREE] R2-W4: **BiGRU ≈ mean pooling 对多轮叙事的影响——强烈同意，这是一个被低估的问题。**

Section 4.3 "Temporal modeling" 明确指出 "Mean pooling matches BiGRU (F1 gap < 1pp; Appendix T) and turn-order shuffling is negligible (Δ < 1 pp)"。Table 30 (Appendix T) 确认 mean pooling 在 ID 和 OOD 上与 BiGRU 几乎完全等价。

这个发现的 implication 比论文承认的更深远：**如果时序聚合（BiGRU）与无序聚合（mean pooling）等价，且 turn-order shuffling 无影响，那么模型本质上在做 bag-of-turns 检测——即对每一轮的 [CLS] embedding 独立判别后取平均**。这直接挑战了论文标题中 "Multi-Turn" 的核心叙事：模型没有建模多轮动态（如攻击策略的渐进升级），而是在每一轮中独立检测越狱信号并聚合。

论文在 Section 4.3 中将此表述为正面发现（"detection therefore relies on per-turn content rather than sequential dynamics"），但未充分讨论其对方法定位的影响。如果 per-turn content 就足够，为什么需要多轮框架？可能的解释是：虽然单轮足以检测，但真实场景中攻击嵌入在多轮对话中，模型需要处理所有轮次才能不遗漏——这是工程需求而非模型能力需求。但论文没有明确做出这个区分。

**与我自己审稿的关系**：我的 Round 1 审稿未单独列出此项，这是 R2 比我更敏锐的一个观察。这个张力值得在 Discussion 中增加一段讨论。

---

### Minor

[AGREE] R2-M1: Table 2 的 seed 报告格式确实不统一——部分 cell 有 ±std，部分没有。统一格式是 camera-ready 级的修改。

[AGREE] R2-M2: 论文在 Section 4.1 "Metrics" 中说明 "F1 for binary jailbreak detection"，但 Figure 2/3 的 y 轴标签未指定是 macro F1 还是 binary F1。应在 Figure caption 中明确。

[AGREE] R2-M3: McNemar's test 的零假设是"两个分类器的错误率无差异"。不拒绝零假设只能说"未发现显著差异"（absence of evidence），不能说"确认等价"（evidence of absence）。论文 Section 4.3 的表述 "McNemar's test ... confirms equivalence" 需修正为 "finds no significant difference"。TOST 等价检验才是真正的等价性检验。

[AGREE] R2-M4: "24.3× speedup" 在 Abstract 中首次出现时未给出基准（vs 什么？）。虽然在 Section 5 中明确了是 vs LLM-as-judge (Qwen3-8B 3-shot)，但 Abstract 中应简要标注。

[REBUT] R2-M5: **Figure 1 的信息密度——部分不同意。**

Figure 1 将 Stage 1（7 个变体的编码器适应）和 Stage 2（BiGRU 时序分类）整合在一张图中，信息密度确实高，但对于一篇以两阶段解耦为核心贡献的论文，在一张图中展示完整 pipeline 是必要的。Stage 1/2 已有颜色区分（黄色/蓝绿色背景）。如果拆分为两张图，反而需要更多空间且破坏了"解耦"的视觉叙事。在 8 页正文限制下，当前设计是合理的 space-quality tradeoff。

---

### Questions

[AGREE] R2-Q1: **ToxicChat 反转下的部署推荐——这是我自己 N1 的核心关切。**

论文目前的部署推荐（Section 5）未区分合成 vs 人类数据场景。正确的推荐应该是：(1) 在合成多轮攻击检测场景下用 9-class DAPT；(2) 在面向真实用户对话时，MLM 可能更稳健，或需要额外的人类数据 fine-tuning。论文未提供这种分场景的推荐。

[AGREE] R2-Q2: **355M DAPT counterproductive 是否暗示 DAPT 补偿容量不足——这是一个有洞察力的假设。**

Section 4.4 报告 RoBERTa-large (355M) 上 DAPT 反转了优势——domain-adapted 变体反而不如 vanilla。一种解释确实是：DAPT 的收益在于为小模型注入 domain signal 以补偿容量不足，而大模型本身有足够容量从 raw data 中学到这些 signal。论文简要提到 "A BERT-base proxy confirms DAPT, not architecture, drives generalization (Appendix Q)"，但未直接回应 capacity-compensation 假设。这值得在 Discussion 中讨论。

[AGREE] R2-Q3: **Scrambled 模板有效但策略多样攻击失效的深层原因——同意这是一个关键未回答问题。**

Section 4.3 指出 "strategy-diverse ActorAttack retains moderate label sensitivity (d=0.44, TOST p=0.183)"，但对**为什么**模板攻击和策略多样攻击对标签正确性有不同反应缺乏机制性解释。可能的解释：模板攻击（Crescendo, Deceptive Delight）有固定的结构模式（如 Appendix E 的 strategy transition matrices 显示 Crescendo 有稳定的 Role Assignment → self-transition 模式），任何分类目标都能捕获这些结构性信号；而策略多样攻击（ActorAttack）的结构更灵活，正确标签提供的细粒度策略信息有额外价值。但论文没有显式做出这个分析。

[AGREE] R2-Q4: **BiGRU ≈ mean pooling 是否意味着 bag-of-turns 检测——同意这是正确的推论。**

如我在 W4 回应中详述的，Table 30 和 Section 4.3 的证据确实暗示模型做的是 per-turn 独立检测的聚合。这不一定是缺陷——如果每一轮的 [CLS] embedding 已经包含了足够的判别信号，bag-of-turns 聚合就是合理的。但论文需要在 Discussion 中明确承认这一点，并讨论对 "Multi-Turn" 定位的影响。

[REBUT] R2-Q5: **50 条训练样本 near-saturation 对标注成本的影响——部分不同意 R2 的隐含预期。**

Table 34 (Appendix W) 确实显示 9-class DAPT 在 50 条对话时就接近饱和（F1=0.969±0.037, AA OOD≥0.969）。R2 似乎暗示这是一个正面发现但论文未充分讨论。我认为论文在 Section 5 的 "Deployment implications" 中提到了 "minimal data collection" 的实用价值，但 50 条对话的 "near-saturation" 也可能反映了任务本身的简单性或评估集的小规模——118 条测试样本上的 F1 saturation 可能只是因为测试集太小以至于更多训练数据无法产生可观测的差异。这与我自己 N2 的统计 power 关切一致。

---

### Missing References

[AGREE] R2 建议补充 representation compression 理论工作（如 Arora et al., 2019）和 proactive/early multi-turn detection 近期工作。这些引用会加强论文在 "discriminative compression" 讨论（Section 5, Figure 10）和 "prefix-level detection" 分析（Section 4.2, Table 7）中的理论支撑。

---

### Overall Assessment 对比

R2: Score 3.0, Soundness 3.5, Excitement 2.5, Confidence 4/5
R1（我）: Score 3.0, Soundness 3/5, Excitement 3/5, Confidence 4/5

**分歧分析**：

1. **Soundness**: R2 给 3.5（Strong 与 Acceptable 之间），我给 3.0（Acceptable）。差异源于：我更重视 ToxicChat 反转（24pp 差距）和 WildChat FPR（68.1%）对核心 claim 的直接威胁，认为这些 negative findings 构成 soundness 的实质性缺陷。R2 可能认为这些是 claim scope 问题（overclaiming）而非 soundness 问题。

2. **Excitement**: R2 给 2.5（Potentially Interesting），我给 3.0（Interesting）。R2 更强调新颖性不足（N1），我认为因子分析框架本身和 negative findings 的信息量部分弥补了预期性。2.5-3.0 区间的分歧属于合理的 reviewer 间方差。

3. **Overall**: 一致，均为 3.0 (Findings)。这反映了我们对论文整体水平的共识：有方法论贡献和有价值的实证发现，但 claim 的谨慎度、讨论深度和数据规模限制了影响力，适合 Findings 而非 Conference。

**总结**：R2 和我的审稿在核心判断上高度一致——evidence hierarchy 的条件依赖性、overclaiming、和人类数据反转是最关键的问题。主要分歧在于权重分配：R2 更关注新颖性，我更关注统计可靠性和 real-world applicability。两种视角互补，共同指向相同的结论：当前版本适合 Findings。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2218 · 2026-05-25T21:35:11.295080+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 2219 · 2026-05-25T21:35:11.314152+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 19
}
```

</details>

---


### Tool call

_source line 2220 · 2026-05-25T21:35:16.211957+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2221 · 2026-05-25T21:35:16.313651+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2222 · 2026-05-25T21:35:22.024589+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 2223 · 2026-05-25T21:35:22.126582+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:15:50.414510+00:00\", \"completed_at\": \"2026-05-25T21:20:33.125825+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title/Abstract/Author 排版整洁专业，双栏格式规范，匿名 ACL submission header 正确。脚注含匿名化代码/数据链接。Abstract 长度目测接近 200 词上限，建议人工复核精确词数确保不超限。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（架构图）在第 2 页顶部全宽展示，作为视觉锚点效果佳——审稿人打开前两页即可锚定方法核心（两阶段 pipeline）。Caption 自包含，颜色编码（黄/绿/粉）清晰区分组件。Title-Abstract-Figure 1 讲述一致的故事。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"纯文本页（Related Work + Method 开头），但仅一页，不构成连续纯文本问题。Section 3.1 引入数学符号，提供了视觉变化。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 + Figure 2 组合良好，text/table/figure 三重奏节奏回归。Figure 2 分组柱状图颜色可区分（ID/DD/AA/OOD 四类），legend 字号尚可。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2 + Figure 3 继续保持良好密度。Figure 3 与 Figure 2 使用一致的颜色方案（跨图颜色语义一致），专业。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"两个表格（Table 3 + Table 4）密集但可读。表格使用 booktabs 风格（无竖线），最优结果加粗，小数精度一致。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4（双面板柱状图）+ Table 5。Figure 4 左面板标注 \\\"Reversal\\\" 箭头是有效的视觉叙事手段。Sections 4.4-4.8 共 5 个子节挤在一页，密度高但未溢出。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 5 的坐标轴标签（\\\"FPR (%)\\\"、\\\"Benign conversations (N)\\\"）和图内注释文字（\\\"64.5%\\\"、\\\"OASST2 sample seed\\\"）字号偏小，灰度打印时线条可能难以区分。建议增大标注字号至正文 70% 以上。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 6（SVD 可视化）尺寸较小（约 1/4 column），散点和颜色标签在打印时可能不够清晰。若此图支撑核心 claim，建议放大或移至全宽。若仅为补充，当前尺寸可接受。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主正文在第 8 页结束（Discussion + Conclusion），符合 EMNLP 2026 的 8 页正文限制。页面利用率高，无异常空白。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 节简洁（3 个要点），符合 EMNLP 202
…[truncated 1970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2224 · 2026-05-25T21:35:22.177568+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 2225 · 2026-05-25T21:35:23.803243+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1625
}
```

</details>

---


### Tool call

_source line 2226 · 2026-05-25T21:35:23.855762+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2227 · 2026-05-25T21:35:24.667219+00:00_

&lt;persisted-output>
Output too large (35.4KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-review-director-93d7fc7c/cd624938-032c-4430-92ec-9731379fcd54/tool-results/b8j7to64s.txt

Preview (first 2KB):
issues:
# === 历史 resolved issues ===
- id: R1-N1
  summary: Evidence hierarchy 统计基础不一致
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  mentions:
  - round: 1
    reviewers: [1, 2]
    note: binary/scrambled 仅 seed 42
  action_items:
  - round: 1
    action: 训练 binary/scrambled 3-seed
    assigned_to: main_agent
    status: resolved
  resolution: 'MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005'
  resolution_round: 1

- id: R1-N2
  summary: Three-layer robustness attribution 缺乏统计显著性
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  mentions:
  - round: 1
    reviewers: [1, 2]
    note: R1 首提 N2
  action_items:
  - round: 1
    action: McNemar's test + bootstrap CI
    assigned_to: main_agent
    status: resolved
  resolution: MF2 完成
  resolution_round: 1

- id: R1-N3
  summary: 缺少与已发表 multi-turn defense 的直接实验对比
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  mentions:
  - round: 1
    reviewers: [1, 2]
    note: R1 首提 N3
  - round: 2
    reviewers: [1, 2]
    note: Round 1 修复不充分，再次提出
  action_items:
  - round: 1
    action: 重构论证
    assigned_to: paper_agent
    status: resolved
  - round: 2
    action: Analysis paper reframe
    assigned_to: research_director
    status: resolved
  resolution: Analysis paper reframe 完成。
  resolution_round: 3

- id: R1-N4
  summary: 数据集规模过小
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  mentions:
  - round: 2
    reviewers: [1, 2]
    note: 500训练+76-118测试+3
…[truncated 347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Bash",
  "elapsed_ms": 811
}
```

</details>

---


### Tool call

_source line 2228 · 2026-05-25T21:35:28.841981+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-review-director-93d7fc7c/cd624938-032c-4430-92ec-9731379fcd54/tool-results/b8j7to64s.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-review-director-93d7fc7c/cd624938-032c-4430-92ec-9731379fcd54/tool-results/b8j7to64s.txt"
  }
}
```

</details>

---


### Tool result

_source line 2229 · 2026-05-25T21:35:29.145054+00:00_

1	issues:
2	# === 历史 resolved issues ===
3	- id: R1-N1
4	  summary: Evidence hierarchy 统计基础不一致
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 1
9	  last_seen_round: 1
10	  mentions:
11	  - round: 1
12	    reviewers: [1, 2]
13	    note: binary/scrambled 仅 seed 42
14	  action_items:
15	  - round: 1
16	    action: 训练 binary/scrambled 3-seed
17	    assigned_to: main_agent
18	    status: resolved
19	  resolution: 'MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005'
20	  resolution_round: 1
21	
22	- id: R1-N2
23	  summary: Three-layer robustness attribution 缺乏统计显著性
24	  category: experiment
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 1
28	  last_seen_round: 1
29	  mentions:
30	  - round: 1
31	    reviewers: [1, 2]
32	    note: R1 首提 N2
33	  action_items:
34	  - round: 1
35	    action: McNemar's test + bootstrap CI
36	    assigned_to: main_agent
37	    status: resolved
38	  resolution: MF2 完成
39	  resolution_round: 1
40	
41	- id: R1-N3
42	  summary: 缺少与已发表 multi-turn defense 的直接实验对比
43	  category: experiment
44	  severity: critical
45	  status: resolved
46	  first_raised_round: 1
47	  last_seen_round: 2
48	  mentions:
49	  - round: 1
50	    reviewers: [1, 2]
51	    note: R1 首提 N3
52	  - round: 2
53	    reviewers: [1, 2]
54	    note: Round 1 修复不充分，再次提出
55	  action_items:
56	  - round: 1
57	    action: 重构论证
58	    assigned_to: paper_agent
59	    status: resolved
60	  - round: 2
61	    action: Analysis paper reframe
62	    assigned_to: research_director
63	    status: resolved
64	  resolution: Analysis paper reframe 完成。
65	  resolution_round: 3
66	
67	- id: R1-N4
68	  summary: 数据集规模过小
69	  category: experiment
70	  severity: critical
71	  status: resolved
72	  first_raised_round: 1
73	  last_seen_round: 2
74	  mentions:
75	  - round: 2
76	    reviewers: [1, 2]
77	    note: 500训练+76-118测试+3seeds仍不足
78	  action_items:
79	  - round: 2
80	    action: Bootstrap 95% CI + permutation test
81	    as
…[truncated 34445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 2230 · 2026-05-25T21:36:03.125717+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 2231 · 2026-05-25T21:36:03.179224+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 2232 · 2026-05-25T21:36:07.589751+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read local file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read local file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2233 · 2026-05-25T21:36:07.640590+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2234 · 2026-05-25T21:41:21.181137+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "issues_yaml": "issues:\n# === 历史 resolved issues ===\n- id: R1-N1\n  summary: Evidence hierarchy 统计基础不一致\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: binary/scrambled 仅 seed 42\n  action_items:\n  - round: 1\n    action: 训练 binary/scrambled 3-seed\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005'\n  resolution_round: 1\n\n- id: R1-N2\n  summary: Three-layer robustness attribution 缺乏统计显著性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R1 首提 N2\n  action_items:\n  - round: 1\n    action: McNemar's test + bootstrap CI\n    assigned_to: main_agent\n    status: resolved\n  resolution: MF2 完成\n  resolution_round: 1\n\n- id: R1-N3\n  summary: 缺少与已发表 multi-turn defense 的直接实验对比\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R1 首提 N3\n  - round: 2\n    reviewers: [1, 2]\n    note: Round 1 修复不充分，再次提出\n  action_items:\n  - round: 1\n    action: 重构论证\n    assigned_to: paper_agent\n    status: resolved\n  - round: 2\n    action: Analysis paper reframe\n    assigned_to: research_director\n    status: resolved\n  resolution: Analysis paper reframe 完成。\n  resolution_round: 3\n\n- id: R1-N4\n  summary: 数据集规模过小\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 500训练+76-118测试+3seeds仍不足\n  action_items:\n  - round: 2\n    action: Bootstrap 95% CI + permutation test\n    assigned_to: main_agent\n    status: resolved\n  resolution: exp9 BCa bootstrap 95% CI + paired permutation test 完成。\n  resolution_round: 2\n\n- id: R2-N3\n  summary: 有效 OOD 评估实质上是 single-dataset\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R2 首提\n  action_items:\n  - round: 1\n    action: ActorAttack OOD 数据生成\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'EXP-2 完成: ActorAttack 118 conversations'\n  resolution_round: 1\n\n- id: R1-W1\n  summary: Mean pooling=BiGRU 结论基于 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: Paper Agent 已弱化。multi-seed 实验验证。\n  resolution_round: 1\n\n- id: R1-W3\n  summary: LLM-as-judge baseline 仅测 IID\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions: []\n  action_items: []\n  resolution: EXP-5 完成\n  resolution_round: 1\n\n- id: R1-W4\n  summary: TF-IDF LR 强表现未被充分讨论\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: TF-IDF per-prefix + ActorAttack 完成。\n  resolution_round: 3\n\n- id: R1-W5\n  summary: 可复现性不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions: []\n  action_items: []\n  resolution: Paper Agent 已添加 Appendix C\n  resolution_round: 1\n\n- id: R2-W1\n  summary: Abstract 过度堆砌数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: Abstract 压缩至 ~190 words。\n  resolution_round: 3\n\n- id: R2-W2\n  summary: partially falsified 叙事对接收不利\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: Framing 调整完成。\n  resolution_round: 3\n\n- id: R8-N4\n  summary: LLM-as-judge baseline 对比不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  mentions:\n  - round: 8\n    reviewers: [2]\n    note: GPT-5.5 不可解析可能是 prompt 设计问题\n  - round: 14\n    reviewers: [1, 2]\n    note: R14 两位 Reviewer 均指出 prompt 未提供、未尝试 prompt 优化\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items:\n  - round: 14\n    action: 附录提供 LLM-as-judge prompt 模板\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: 明确标注为 deployment cost comparison 而非方法论对比\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'R21验证: GPT F1标注\"upper bounds\"'\n  resolution_round: 21\n\n- id: R9-M1\n  summary: Abstract 中 Llama Guard 3 1.8% 有 misleading 风险\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. Abstract中Llama Guard 3缺\"zero-shot\"限定词'\n  action_items: []\n  resolution: Abstract 已使用 'zero-shot' 限定。\n  resolution_round: 22\n\n- id: R13-N2\n  summary: WildChat FPR=68.1% + few-shot 修复验证不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items:\n  - round: 19\n    action: 补充 few-shot benign adaptation 的实现细节\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'R21验证: few-shot实现细节完整(Stage-2 BiGRU, encoder frozen, N benign, BCE, 5 epochs)'\n  resolution_round: 21\n\n- id: R13-N3\n  summary: 机制解释缺乏直接证据\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items:\n  - round: 19\n    action: Section 5 讨论 discriminative compression vs representation collapse 替代解释\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'R21验证: 因果声明弱化为\"appears necessary\",\"consistent with\"'\n  resolution_round: 21\n\n- id: R13-W2\n  summary: DisPeD 命名 / 'Disentangled' 术语误用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Footnote 1清晰区分ablation methodology与disentangled representation learning'\n  resolution_round: 21\n\n- id: R13-W3\n  summary: Scrambled label AA 非等价 (d=0.44)\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: AA上d=0.44, TOST p=0.183明确标注'\n  resolution_round: 21\n\n- id: R13-W4\n  summary: Mixed-LLM AA=0.504 + MLM 崩溃\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 明确标注\"chance level, indistinguishable from majority baseline\"'\n  resolution_round: 21\n\n- id: R13-W6\n  summary: FITD 缺乏区分力\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions: []\n  action_items: []\n  resolution: R15 不再提出，视为已充分缓解。\n  resolution_round: 15\n\n- id: R14-W1\n  summary: BCa Bootstrap 跨 seed 池化\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 标注\"assumes cross-seed independence and is exploratory\"'\n  resolution_round: 21\n\n- id: R14-W2\n  summary: Benign-side 仅 WildChat 单一数据源\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: OASST2 双源验证解决。\n  resolution_round: 15\n\n- id: R14-W3\n  summary: Figure 2 缺失 ActorAttack\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: Figure 2 已增加 ActorAttack。\n  resolution_round: 15\n\n- id: R14-I1\n  summary: 主文 Conclusion 溢出到 page 9\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: Conclusion 确认在 page 8 内。\n  resolution_round: 15\n\n- id: R15-SF1\n  summary: 判别性压缩因果链不完整 + SVD 数据泄漏\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Discussion使用\"consistent with\"而非因果声明'\n  resolution_round: 21\n\n- id: R15-SF4\n  summary: C2 complexity-dependent boundary 证据基础狭窄\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions: []\n  action_items: []\n  resolution: R16-R19 不再单独提出。\n  resolution_round: 16\n\n- id: R15-SF6\n  summary: 方差缩减 4-20× 声明基于 n=3 seeds\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 改为\"descriptively 3-23×\"'\n  resolution_round: 21\n\n- id: R16-N1\n  summary: '''Any deterministic partition suffices'' 声称与 Topic 变体失败直接矛盾'\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 区分domain-relevant vs arbitrary classification, 指向Wiki-MLM vs JB-MLM为cleaner test'\n  resolution_round: 21\n\n- id: R16-W3\n  summary: Two-axis framework 新颖性争议\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: two-axis定位为organizational framework而非独立贡献'\n  resolution_round: 21\n\n- id: R16-W4\n  summary: 数据划分描述不够清晰\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 明确说明Stage 1用train+val, Stage 2用train/val/test'\n  resolution_round: 21\n\n- id: R17-N1\n  summary: n=3 seeds 方差缩减 claims 统计可靠性不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 同R15-SF6, 方差声明改为descriptive'\n  resolution_round: 21\n\n- id: R17-W2\n  summary: Cross-LLM Abstract 'remains robust' 与正文 'preliminary' 矛盾\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Abstract不再有\"remains robust\"'\n  resolution_round: 21\n\n- id: R17-W3\n  summary: RoBERTa-large DAPT 有害——核心 thesis scale-dependent\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 实验/讨论/结论三处承认scale-dependent并标注\"counterproductive at 355M\"'\n  resolution_round: 21\n\n- id: R18-N1\n  summary: '''Structural complexity'' 缺乏形式化定义'\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 操作化为transition rate<0.1(template) vs >0.3(complex)'\n  resolution_round: 21\n\n- id: R18-W1\n  summary: 缺少与已发表多轮检测方法的直接实验对比\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Related Work说明无公开实现, Appendix提供BERT-base proxy'\n  resolution_round: 21\n\n- id: R19-E1\n  summary: experiments.tex L114 \"$d<0.1$\" 数值错误 (应为 |d|≤0.14)\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED] 数值已修正'\n  action_items: []\n  resolution: 'R21验证: |d|≤0.14与Table一致'\n  resolution_round: 21\n\n- id: R19-E2\n  summary: intro L24 \"the first\" 缺少 \"to our knowledge\" 限定\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions: []\n  action_items: []\n  resolution: 当前文本已包含 \"to our knowledge\" 限定。\n  resolution_round: 20\n\n- id: R19-E3\n  summary: Abstract \"requires domain adaptation\" 与 RoBERTa-large vanilla AA=1.000 矛盾\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions: []\n  action_items: []\n  resolution: Abstract 已修改为 \"benefits substantially from\"。\n  resolution_round: 20\n\n- id: R20-N1\n  summary: 正文超过 8 页限制（Sections 1-6 占 9 页）\n  category: format\n  severity: critical\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: FALSE POSITIVE — Sections 1-6 在 p1-p8, Limitations (p9) 不计入限制。\n  - round: 23\n    reviewers: []\n    note: \"R23 视觉审查再次检测到 Conclusion 溢出 3-4 行至 page 9。可能是后续修改导致回归，需作者确认。\"\n  action_items: []\n  resolution: 'FALSE POSITIVE: 视觉验证确认正文恰好 8 页。R24 视觉审查确认主正文在第 8 页结束。'\n  resolution_round: 20\n\n- id: R20-N2\n  summary: Topic 变体控制设计存在 3 个未隔离混杂因素\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: method.tex和experiments.tex明确承认三个混杂因素, 指向Wiki-MLM vs JB-MLM'\n  resolution_round: 21\n\n- id: R20-N3\n  summary: Appendix Table 16 TOST 数据 (n=3) 与主文 (n=10) 不一致\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED] TOST扩展至n=10'\n  action_items: []\n  resolution: 'R21验证: 主文和附录统一为n=10 seeds'\n  resolution_round: 21\n\n# === Open / In-Progress issues (updated for Round 24) ===\n\n- id: R9-W1\n  summary: 长度混淆未充分排除\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 23\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: benign 12-20 turns vs jailbreak 3-10 turns 完全不重叠\n  - round: 16\n    reviewers: [1, 2]\n    note: R16 升级为 critical。R1 指出 adversarial padding 后 AA 暴跌 57pp。\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED] 两位Reviewer一致确认'\n  - round: 22\n    reviewers: [1]\n    note: \"R22 R1-N2 重新提出为 critical。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-N1 列为 Must-Fix。R2 交叉 REBUT→Should-Fix。Director 裁定 Should-Fix。\"\n  - round: 24\n    reviewers: []\n    note: \"R24 未单独再次提出。R23 action item (turn-count-only classifier) 状态未更新。降级为 warning。\"\n  action_items:\n  - round: 15\n    action: 主文 Section 4 或 5 加 1-2 句长度混淆讨论\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: 构造长度匹配对照数据；Section 5 prominently 讨论 AA padding collapse\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: 提供 turn-count-only classifier F1 作为 sanity check\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R9-W2\n  summary: Human data 上 evidence hierarchy 完全反转 (ToxicChat)\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 24\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: ToxicChat JB-MLM=0.837 >> 9-class=0.596\n  - round: 17\n    reviewers: [1, 2]\n    note: R17 两位 Reviewer 均列为 critical。\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED] 两位Reviewer一致确认'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 两位 Reviewer 独立再次列为 Must-Fix。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 两位 Reviewer 再次独立列为 Must-Fix。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 核心问题。R1-N1 + R2-N2 均为 Must-Fix + 交叉 AGREE。ToxicChat MLM(0.837)>>9-class(0.596) 差距24pp + WildChat FPR 68.1%。论文 'evidence hierarchy' 术语本身有误导性——实为 condition-dependent observations。R1 补充: 即使在合成 OOD '稳定' 条件下，顶部变体差异(1-4pp)也小于抽样误差。建议重命名为 'condition-dependent evidence landscape'。\"\n  action_items:\n  - round: 18\n    action: 'D081 MF1: Abstract/Intro/Conclusion scope 系统性收窄'\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: Section 4.6 ToxicChat 反转从1句扩展为1-2段深入分析; Conclusion 给出条件性结论\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: \"将 'evidence hierarchy' 重新定义为 'condition-dependent evidence landscape' 或类似表述; 主文系统讨论各反转条件(人类数据/策略多样攻击/大规模训练/WildChat部署)\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R13-N1\n  summary: 单一合成数据源限制跨攻击泛化声明可信度\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: 'R18 共识: disclosure 基本到位，但双重 OOD 评估缺失。'\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED] scope qualifier全面'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 两位 Reviewer 独立重新提出。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 继续存在。hierarchy 仅在合成数据生态系统内成立。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 结构性问题持续存在。与 R9-W2(ToxicChat反转)和 WildChat FPR 形成证据链: 所有真实数据场景均不支持论文主要结论。即使 framing 完美修改，主要 take-away 仍是 'DAPT hierarchy exists but only in synthetic settings'——这限制了论文的实际影响力但不阻碍 Findings 接收。\"\n  action_items:\n  - round: 17\n    action: W-1 Abstract F1 后加 '(attack-side OOD; benign IID)' 限定\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: Table 2 增加 dual-OOD 行；Abstract/Conclusion 所有 OOD F1 标注为 upper bound + IID benign 条件\n    assigned_to: main_agent\n    status: resolved\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W1\n  summary: 新颖性不足——DAPT 应用 + 增量贡献不清\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: 方法新颖性有限是阻碍 Conference 推荐的主要原因之一。\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] 降级为warning. 叙事一致但novelty argumentation深度不足'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R2-N1 列为 critical。R1 交叉 AGREE 但建议降为 major。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-N1 再次列为 critical。共识: 需从 'unexpected' 重新定位为 'quantifying the magnitude and conditions'。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2 列为 Must-Fix + R1 部分 AGREE。R1 提出新颖性分三层: (1)DAPT>vanilla=低新颖性(预期); (2)scrambled≈correct on templates=中等新颖性(counter-intuitive); (3)hierarchy在人类数据反转=高信息量negative finding(未被充分开发)。共识: 问题是程度性的而非二元的——最具新颖性的发现未置于叙事中心，被淹没在平凡结论中。\"\n  action_items:\n  - round: 18\n    action: 重写 novelty positioning 为消融发现集合\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: Section 1 将 finding(i) 从 'unexpected' 改为 'systematic quantification'; Abstract 相应调整\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: \"重组叙事: 以 'why DAPT works, when it fails' 为主轴而非 'DAPT works'; 将 scrambled equivalence 和 human-data reversal 置于叙事中心\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W5\n  summary: Scale analysis 被架构差异混淆\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. DeBERTa vs RoBERTa混杂参数量, 建议Limitations加一句'\n  - round: 22\n    reviewers: [2]\n    note: \"R22 R2-W4: 仅 base-scale (125M-184M)。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 相关但不直接提及。\"\n  action_items:\n  - round: 17\n    action: Discussion 增加 DAPT scale-dependent 效用讨论\n    assigned_to: main_agent\n    status: resolved\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W7\n  summary: Abstract 信息密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. Abstract信息密度高+句法模糊'\n  - round: 22\n    reviewers: [2]\n    note: \"R22 R2 小问题: Abstract 中 'this hierarchy reverses' 后的修饰对象不清。\"\n  - round: 23\n    reviewers: [2]\n    note: \"R23 R2 交叉回应中继续提及 abstract 句法模糊。\"\n  - round: 24\n    reviewers: [2]\n    note: \"R24 未单独列出但与 R21-N1 合并。\"\n  action_items:\n  - round: 19\n    action: Abstract 压缩至 ~180 词\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R13-M1\n  summary: Missing references\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R2-W1 建议补充 Galinkin & Sablotny (2024)。\"\n  - round: 23\n    reviewers: [1]\n    note: \"R23 R1 建议补充 Perez and Wang (2022) red teaming 工作。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2 建议补充 representation compression 理论工作(如 Arora et al., 2019)和 proactive/early multi-turn detection 近期工作。R1 AGREE。\"\n  action_items:\n  - round: 22\n    action: 补充引用 Galinkin & Sablotny (2024) arXiv 2412.01547\n    assigned_to: main_agent\n    status: open\n  - round: 23\n    action: 确认 Perez and Wang (2022) 是否已引用或需补充\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: 补充 Arora et al. (2019) representation compression 和 proactive multi-turn detection 近期工作引用\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R14-N1\n  summary: 数据规模扩大后性能反常下降 (350→1000)\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] should-fix. 9-class也下降(0.994→0.889), 未给出解释'\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W5 再次提出。R2 交叉 AGREE。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 未单独提出但 R1 cross-response Q2 隐含提及 capacity-compensation 假设。问题仍 open。\"\n  action_items:\n  - round: 17\n    action: 弱化为 composition differences partially confound\n    assigned_to: main_agent\n    status: in_progress\n  - round: 23\n    action: 报告 1000 样本的 seed 一致性、training loss 或 data composition 证据\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R15-VIS1\n  summary: Figure 2 尺寸偏小，axis labels 约正文字号 50-60%\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. Figure 2 axis labels仍偏小'\n  - round: 24\n    reviewers: []\n    note: \"R24 视觉审查: Figure 5 坐标轴标签字号偏小(p8), Figure 6 SVD 尺寸较小(p8), p16 CKA heatmap 轴标签几乎不可读。\"\n  action_items:\n  - round: 15\n    action: Figure 2 字号放大至≥8pt\n    assigned_to: main_agent\n    status: in_progress\n  - round: 24\n    action: \"Figure 5/6 标注字号增大至正文70%以上; Appendix Figure 8 CKA heatmap 轴标签放大\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R16-W1\n  summary: Temporal modeling negative finding 讨论不足\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R1-W3: BiGRU 对 mean pooling 无优势(Table 30)。R2 交叉 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W3 再次提出 + R2-W4 AGREE。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-W4 Should-Fix + R1 强烈 AGREE。关键推论: BiGRU≈mean pooling + turn-order shuffling无影响 = 模型本质上做 bag-of-turns 检测。这直接挑战 'Multi-Turn' 叙事——模型未建模多轮动态(策略升级)，而是 per-turn 独立检测后聚合。论文将此表述为正面发现但未讨论对方法定位的影响。R1 提出可能解释: 多轮框架是工程需求(处理对话中的攻击嵌入)而非模型能力需求——但论文未做此区分。\"\n  action_items:\n  - round: 19\n    action: Discussion 讨论为什么 multi-turn 攻击的检测不需要时序建模\n    assigned_to: main_agent\n    status: resolved\n  - round: 22\n    action: Section 3.3 或 Section 5 明确说明 BiGRU 可被 mean pooling 替代且不影响检测性能\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: \"Discussion 新增段落: 明确区分 'multi-turn framework as engineering requirement (processing all turns)' vs 'multi-turn modeling as capability requirement (learning sequential dynamics)'; 承认当前模型属于前者\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R16-W2\n  summary: 效率对比定位不清\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[STILL_OPEN] minor. R1指出Introduction已标注43×, 但Abstract未标注'\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-M4: '24.3× speedup' 在 Abstract 首次出现时未给出基准。R1 AGREE。\"\n  action_items:\n  - round: 16\n    action: 效率对比加 deployment cost comparison 限定\n    assigned_to: main_agent\n    status: in_progress\n  - round: 24\n    action: \"Abstract 中 '24.3× speedup' 后简要标注 'vs LLM-as-judge'\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W1\n  summary: TOST δ=5pp margin 缺乏 practical significance 论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. δ=5pp缺practical significance论证'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R1-W1 + R2 交叉 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W1 再次提出。共识: 方法论改进空间，不改变定性结论。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-M3 相关: McNemar's test '确认等价' 语言问题。R1 AGREE: 不拒绝H0≠确认等价，需改为 'finds no significant difference'。TOST 才是真正等价检验。\"\n  action_items:\n  - round: 17\n    action: Appendix TOST 部分增加 domain-specific practical significance 论证\n    assigned_to: main_agent\n    status: in_progress\n  - round: 23\n    action: \"[复发×4+轮] 补 δ=3pp sensitivity + practical significance 论证重写\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 24\n    action: \"修正 Section 4.3 'McNemar's test confirms equivalence' 为 'finds no significant difference'; 区分 absence of evidence vs evidence of absence\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M1\n  summary: 'Missing references: ADEPT, Echo Chamber Attack, Representation Bending'\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. ADEPT/Echo Chamber/RepBending未引用'\n  action_items:\n  - round: 17\n    action: 核实引用真实性和相关性\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R21-N1\n  summary: Abstract第二长句句法模糊——\"this hierarchy reverses\"后的修饰对象不清\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: 'NEW-1: \"on labeled multi-turn jailbreak data\"修饰对象歧义'\n  - round: 22\n    reviewers: [2]\n    note: \"R22 仍存在。\"\n  - round: 23\n    reviewers: [2]\n    note: \"R23 R2 交叉回应中继续提及。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-W2 再次标为 Should-Fix: Section 4.6 标题 'Human Data Validation' 暗示确认性结果但内容是反转/失败。R1 AGREE。且 ToxicChat 是单轮数据而论文标题聚焦 Multi-Turn。\"\n  action_items:\n  - round: 23\n    action: \"[复发×3轮] 重写为'Third, these advantages are condition-specific: on human-authored single-turn data, the hierarchy reverses'\"\n    assigned_to: main_agent\n    status: in_progress\n  - round: 24\n    action: \"Section 4.6 标题从 'Human Data Validation' 改为 'Human Data Evaluation' 或 'Transfer to Human-Authored Data'\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R1-W2\n  summary: 策略标注质量验证不充分\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 24\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: R16 两位 Reviewer 均再次指出 κ=0.78 n=50 不足\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R1-W4: 50样本9类→部分类别仅2-5个验证样本。R2 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W4 再次提出。共识: 增加样本至≥100并报告per-class κ。\"\n  - round: 24\n    reviewers: []\n    note: \"R24 未单独再提。R23 action item 仍 open。\"\n  action_items:\n  - round: 1\n    action: Limitations 已添加 caveat\n    assigned_to: main_agent\n    status: resolved\n  - round: 22\n    action: 增加标注验证样本量至≥100并报告per-class κ; Appendix Y caveat标注质量\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R22-N1\n  summary: Scrambled≈9-class 等价性能与论文叙事的张力\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R1-W2 首提: scrambled 在 DD/FTTD 上与 9-class TOST 等价。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 Abstract 限定为 template attacks。R2 交叉 AGREE。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R1 交叉 AGREE R2-S2: scrambled 是最具原创性实证贡献。但补充重要限定: TOST 在 ActorAttack 上未通过(p=0.183, d=0.44)，发现适用范围限于模板攻击。Abstract 已限定——确认 resolved。\"\n  action_items:\n  - round: 22\n    action: Section 5 增加段落讨论 classification objective structure vs label semantics\n    assigned_to: main_agent\n    status: open\n  - round: 23\n    action: Abstract 修改 \"not label semantics—drives generalization\" 为限定 template attacks 的表述\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R23 Reviewer PASS + R24 confirmed: abstract.tex L7 精准限定 'on template attacks'\"\n  resolution_round: 23\n\n- id: R22-W1\n  summary: 自创术语过多且定义不严谨——evidence hierarchy, discriminative compression 等\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R2-W2 首提。R1 交叉部分 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-W1 再次提出。共识: 首次使用处需一句话定义。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-W1 再列为 Should-Fix。R1 交叉 REBUT: 'evidence hierarchy' 和 'discriminative compression' 是合理的描述性术语，认知负荷增加合理。同意 'partition sufficiency' 过于晦涩可简化。总体判断: Minor 级别而非 Should-Fix。Director 裁定 resolved per R23: experiments.tex L6 Terminology 段已定义。\"\n  action_items:\n  - round: 22\n    action: 首次使用时给出一句话定义; 考虑将 'evidence hierarchy' 改为 'performance ranking'\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R23 Reviewer PASS: experiments.tex L6 Terminology 段首次使用前定义。R24 分歧(R1 REBUT R2 severity)不影响 resolution。\"\n  resolution_round: 23\n\n- id: R22-W2\n  summary: Conclusion 'reusable template' claim 超出单一任务的实验范围\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R2-W3 首提。R1 交叉 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-W3 再次提出。共识: 限定为 'template for future controlled studies of domain adaptation in safety-critical NLP tasks'。\"\n  action_items:\n  - round: 22\n    action: Conclusion 限定 'reusable template' 的适用范围\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R23 Reviewer PASS: conclusion.tex L29 限定为 'safety-critical NLP tasks'\"\n  resolution_round: 23\n\n# === Round 24 新增 issues ===\n\n- id: R24-MF1\n  summary: \"'Evidence hierarchy' 术语本身具有误导性——应改为条件依赖性表述\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-N2 Must-Fix + R1 AGREE: 一个在多个现实场景下反转的排序不应被称为 'hierarchy'。R1 补充: 即使在最有利条件下(合成OOD)，顶部变体差异(1-4pp)也远小于3-seed抽样误差，精细排序可能不稳健。共识: 重新命名为 'condition-dependent evidence landscape' 或 'performance ranking with boundary conditions'。\"\n  action_items:\n  - round: 24\n    action: \"全文替换 'evidence hierarchy' 为更准确术语; 主文系统列举四个反转条件\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R24-SF1\n  summary: BiGRU≈mean pooling 暗示 bag-of-turns 检测——挑战 'Multi-Turn' 核心叙事\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-W4 Should-Fix + R1 强烈 AGREE (称之为 'R2 比我更敏锐的观察')。Table 30 + Section 4.3: mean pooling 在 ID/OOD 完全等价 BiGRU + turn-order shuffling Δ<1pp。推论: 模型做的是 per-turn [CLS] embedding 独立判别后取平均 = bag-of-turns。论文标题 'Multi-Turn Jailbreak Detection' 的核心叙事被动摇——模型未学到多轮动态(策略升级)。R1 提出: 多轮框架可能是工程需求(不遗漏嵌入对话中的攻击)而非模型能力——但论文未做此区分。\"\n  action_items:\n  - round: 24\n    action: \"Discussion 新增 1 段: 区分 multi-turn framework (engineering) vs multi-turn modeling (learning dynamics); 明确承认当前模型属于前者; 讨论对标题定位的影响\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R24-SF2\n  summary: \"Section 4.6 'Human Data Validation' 标题误导——实际是 negative validation\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-W2 Should-Fix + R1 AGREE: 'Validation' 暗示确认性结果，但内容是反转/失败。且 ToxicChat 是单轮数据而论文标题聚焦 Multi-Turn，用单轮数据做 'validation' 有方法论张力(论文 Section 4.6 有说明但标题不准确)。\"\n  action_items:\n  - round: 24\n    action: \"Section 4.6 标题改为 'Transfer to Human-Authored Data' 或 'Human Data Evaluation'\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R24-SF3\n  summary: Related Work 对 multi-turn defense 方法缺乏结构化比较\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-W3 Should-Fix + R1 AGREE: Section 2 引用了 DeepContext/BIID/G-Guard 等方法但仅1-2句概括，未系统比较设计维度(编码器选择、时序建模方式、训练数据类型、评估攻击范围)。R1 建议增加结构化对比表(Appendix 亦可)。\"\n  action_items:\n  - round: 24\n    action: \"Related Work 或 Appendix 增加 multi-turn defense 方法结构化对比表(columns: method/encoder/temporal modeling/training data/evaluation scope)\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R24-M1\n  summary: Table 2 seed 报告格式不统一(部分有±std 部分无)\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-M1 + R1 AGREE: camera-ready 级修改。\"\n  action_items:\n  - round: 24\n    action: \"统一 Table 2 所有 cell 的 ±std 格式\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R24-M2\n  summary: Figure 2/3 y轴标签未指定 macro F1 还是 binary F1\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-M2 + R1 AGREE: Figure caption 应明确 F1 类型。\"\n  action_items:\n  - round: 24\n    action: \"Figure 2/3 caption 中明确标注 F1 类型(binary/macro)\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R23-MF1\n  summary: ToxicChat hierarchy 反转分析深度不足——核心叙事在人类数据上失效\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"两位 AGREE: ToxicChat 是唯一人类数据评估, MLM F1=0.837 大幅超越 classification 0.596。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 继续作为 Must-Fix。与 R9-W2 合并处理。R1 cross-response 对齐 R2: 论文对此反转的讨论深度不匹配问题严重性。\"\n  action_items:\n  - round: 23\n    action: Discussion 段 ToxicChat 因果分析(single-turn特性 + distributional gap + truncated evidence); Conclusion 条件性结论\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R23-MF3\n  summary: \"Unexpected findings\" 新颖性定位过高——classification>vanilla/MLM 在 DAPT 框架下可预期\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R2-N1 critical + R1 AGREE: Gururangan et al. (2020) 已证明 task-adaptive pretraining 优于 vanilla。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 继续作为 Must-Fix。R1 补充三层新颖性分析——真正有价值的不是 'DAPT works' 而是 boundary conditions 和 negative findings。与 R13-W1 合并处理。\"\n  action_items:\n  - round: 23\n    action: Introduction \"unexpected\" 改为 \"merit attention\" / \"systematic quantification\"; Contribution #1 重新措辞\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R23-SF2\n  summary: WildChat 68.1% FPR 暴露合成数据训练系统性偏差——Discussion 讨论不充分\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1 Must-Fix vs R2 Minor, Director 裁定 Should-Fix。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R1 cross-response 再次引用 WildChat FPR 作为 deployment 限制的关键证据。与 R9-W2 形成证据链。Section 5 'Deployment implications' 推荐 few-shot benign calibration 但未提及此 FPR 约束。\"\n  action_items:\n  - round: 23\n    action: Discussion WildChat FPR 处嵌入半句 distributional shift 归因\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R23-W1\n  summary: RoBERTa-large DAPT \"有害\"机制未解释——\"unnecessary\" vs \"harmful\" 解释缺口\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1-W4 + R2-W4 AGREE: 9-class DAPT F1 从 1.000→0.946 = actively harmful。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-Q2 + R1 AGREE: capacity-compensation 假设有洞察力——DAPT 补偿小模型容量不足，大模型不需要此补偿。论文简要提及 Appendix Q BERT-base proxy 但未直接回应。值得 Discussion 讨论。\"\n  action_items:\n  - round: 23\n    action: Section 4.4 或 Section 5 区分 DAPT 'unnecessary' 和 'harmful' 的机制; 讨论 CKA 分析对 355M 的发现\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R23-W2\n  summary: Topic 变体 5 vs 9 类别数量混淆——failure 可能因类别数不足而非标签无关\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1-W3 首提 + R2 交叉 AGREE。\"\n  - round: 24\n    reviewers: []\n    note: \"R24 未单独提及。R23 action item 仍 open。\"\n  action_items:\n  - round: 23\n    action: 补充 9→5 class merging 控制实验，或在 Limitations 中承认类别数量混淆\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "issues_yaml": "issues:\n# === 历史 resolved issues ===\n- id: R1-N1\n  summary: Evidence hierarchy 统计基础不一致\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: binary/scrambled 仅 seed 42\n  action_items:\n  - round: 1\n    action: 训练 binary/scrambled 3-seed\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005'\n  resolution_round: 1\n\n- id: R1-N2\n  summary: Three-layer robustness attribution 缺乏统计显著性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R1 首提 N2\n  action_items:\n  - round: 1\n    action: McNemar's test + bootstrap CI\n    assigned_to: main_agent\n    status: resolved\n  resolution: MF2 完成\n  resolution_round: 1\n\n- id: R1-N3\n  summary: 缺少与已发表 multi-turn defense 的直接实验对比\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R1 首提 N3\n  - round: 2\n    reviewers: [1, 2]\n    note: Round 1 修复不充分，再次提出\n  action_items:\n  - round: 1\n    action: 重构论证\n    assigned_to: paper_agent\n    status: resolved\n  - round: 2\n    action: Analysis paper reframe\n    assigned_to: research_director\n    status: resolved\n  resolution: Analysis paper reframe 完成。\n  resolution_round: 3\n\n- id: R1-N4\n  summary: 数据集规模过小\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 500训练+76-118测试+3seeds仍不足\n  action_items:\n  - round: 2\n    action: Bootstrap 95% CI + permutation test\n    assigned_to: main_agent\n    status: resolved\n  resolution: exp9 BCa bootstrap 95% CI + paired permutation test 完成。\n  resolution_round: 2\n\n- id: R2-N3\n  summary: 有效 OOD 评估实质上是 single-dataset\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R2 首提\n  action_items:\n  - round: 1\n    action: ActorAttack OOD 数据生成\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'EXP-2 完成: ActorAttack 118 conversations'\n  resolution_round: 1\n\n- id: R1-W1\n  summary: Mean pooling=BiGRU 结论基于 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: Paper Agent 已弱化。multi-seed 实验验证。\n  resolution_round: 1\n\n- id: R1-W3\n  summary: LLM-as-judge baseline 仅测 IID\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions: []\n  action_items: []\n  resolution: EXP-5 完成\n  resolution_round: 1\n\n- id: R1-W4\n  summary: TF-IDF LR 强表现未被充分讨论\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: TF-IDF per-prefix + ActorAttack 完成。\n  resolution_round: 3\n\n- id: R1-W5\n  summary: 可复现性不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions: []\n  action_items: []\n  resolution: Paper Agent 已添加 Appendix C\n  resolution_round: 1\n\n- id: R2-W1\n  summary: Abstract 过度堆砌数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: Abstract 压缩至 ~190 words。\n  resolution_round: 3\n\n- id: R2-W2\n  summary: partially falsified 叙事对接收不利\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: Framing 调整完成。\n  resolution_round: 3\n\n- id: R8-N4\n  summary: LLM-as-judge baseline 对比不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  mentions:\n  - round: 8\n    reviewers: [2]\n    note: GPT-5.5 不可解析可能是 prompt 设计问题\n  - round: 14\n    reviewers: [1, 2]\n    note: R14 两位 Reviewer 均指出 prompt 未提供、未尝试 prompt 优化\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items:\n  - round: 14\n    action: 附录提供 LLM-as-judge prompt 模板\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: 明确标注为 deployment cost comparison 而非方法论对比\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'R21验证: GPT F1标注\"upper bounds\"'\n  resolution_round: 21\n\n- id: R9-M1\n  summary: Abstract 中 Llama Guard 3 1.8% 有 misleading 风险\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. Abstract中Llama Guard 3缺\"zero-shot\"限定词'\n  action_items: []\n  resolution: Abstract 已使用 'zero-shot' 限定。\n  resolution_round: 22\n\n- id: R13-N2\n  summary: WildChat FPR=68.1% + few-shot 修复验证不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items:\n  - round: 19\n    action: 补充 few-shot benign adaptation 的实现细节\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'R21验证: few-shot实现细节完整(Stage-2 BiGRU, encoder frozen, N benign, BCE, 5 epochs)'\n  resolution_round: 21\n\n- id: R13-N3\n  summary: 机制解释缺乏直接证据\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items:\n  - round: 19\n    action: Section 5 讨论 discriminative compression vs representation collapse 替代解释\n    assigned_to: main_agent\n    status: resolved\n  resolution: 'R21验证: 因果声明弱化为\"appears necessary\",\"consistent with\"'\n  resolution_round: 21\n\n- id: R13-W2\n  summary: DisPeD 命名 / 'Disentangled' 术语误用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Footnote 1清晰区分ablation methodology与disentangled representation learning'\n  resolution_round: 21\n\n- id: R13-W3\n  summary: Scrambled label AA 非等价 (d=0.44)\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: AA上d=0.44, TOST p=0.183明确标注'\n  resolution_round: 21\n\n- id: R13-W4\n  summary: Mixed-LLM AA=0.504 + MLM 崩溃\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 明确标注\"chance level, indistinguishable from majority baseline\"'\n  resolution_round: 21\n\n- id: R13-W6\n  summary: FITD 缺乏区分力\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions: []\n  action_items: []\n  resolution: R15 不再提出，视为已充分缓解。\n  resolution_round: 15\n\n- id: R14-W1\n  summary: BCa Bootstrap 跨 seed 池化\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 标注\"assumes cross-seed independence and is exploratory\"'\n  resolution_round: 21\n\n- id: R14-W2\n  summary: Benign-side 仅 WildChat 单一数据源\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: OASST2 双源验证解决。\n  resolution_round: 15\n\n- id: R14-W3\n  summary: Figure 2 缺失 ActorAttack\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: Figure 2 已增加 ActorAttack。\n  resolution_round: 15\n\n- id: R14-I1\n  summary: 主文 Conclusion 溢出到 page 9\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: Conclusion 确认在 page 8 内。\n  resolution_round: 15\n\n- id: R15-SF1\n  summary: 判别性压缩因果链不完整 + SVD 数据泄漏\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Discussion使用\"consistent with\"而非因果声明'\n  resolution_round: 21\n\n- id: R15-SF4\n  summary: C2 complexity-dependent boundary 证据基础狭窄\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions: []\n  action_items: []\n  resolution: R16-R19 不再单独提出。\n  resolution_round: 16\n\n- id: R15-SF6\n  summary: 方差缩减 4-20× 声明基于 n=3 seeds\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 改为\"descriptively 3-23×\"'\n  resolution_round: 21\n\n- id: R16-N1\n  summary: '''Any deterministic partition suffices'' 声称与 Topic 变体失败直接矛盾'\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 区分domain-relevant vs arbitrary classification, 指向Wiki-MLM vs JB-MLM为cleaner test'\n  resolution_round: 21\n\n- id: R16-W3\n  summary: Two-axis framework 新颖性争议\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: two-axis定位为organizational framework而非独立贡献'\n  resolution_round: 21\n\n- id: R16-W4\n  summary: 数据划分描述不够清晰\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 明确说明Stage 1用train+val, Stage 2用train/val/test'\n  resolution_round: 21\n\n- id: R17-N1\n  summary: n=3 seeds 方差缩减 claims 统计可靠性不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 同R15-SF6, 方差声明改为descriptive'\n  resolution_round: 21\n\n- id: R17-W2\n  summary: Cross-LLM Abstract 'remains robust' 与正文 'preliminary' 矛盾\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Abstract不再有\"remains robust\"'\n  resolution_round: 21\n\n- id: R17-W3\n  summary: RoBERTa-large DAPT 有害——核心 thesis scale-dependent\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 实验/讨论/结论三处承认scale-dependent并标注\"counterproductive at 355M\"'\n  resolution_round: 21\n\n- id: R18-N1\n  summary: '''Structural complexity'' 缺乏形式化定义'\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: 操作化为transition rate<0.1(template) vs >0.3(complex)'\n  resolution_round: 21\n\n- id: R18-W1\n  summary: 缺少与已发表多轮检测方法的直接实验对比\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: Related Work说明无公开实现, Appendix提供BERT-base proxy'\n  resolution_round: 21\n\n- id: R19-E1\n  summary: experiments.tex L114 \"$d<0.1$\" 数值错误 (应为 |d|≤0.14)\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED] 数值已修正'\n  action_items: []\n  resolution: 'R21验证: |d|≤0.14与Table一致'\n  resolution_round: 21\n\n- id: R19-E2\n  summary: intro L24 \"the first\" 缺少 \"to our knowledge\" 限定\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions: []\n  action_items: []\n  resolution: 当前文本已包含 \"to our knowledge\" 限定。\n  resolution_round: 20\n\n- id: R19-E3\n  summary: Abstract \"requires domain adaptation\" 与 RoBERTa-large vanilla AA=1.000 矛盾\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions: []\n  action_items: []\n  resolution: Abstract 已修改为 \"benefits substantially from\"。\n  resolution_round: 20\n\n- id: R20-N1\n  summary: 正文超过 8 页限制（Sections 1-6 占 9 页）\n  category: format\n  severity: critical\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: FALSE POSITIVE — Sections 1-6 在 p1-p8, Limitations (p9) 不计入限制。\n  - round: 23\n    reviewers: []\n    note: \"R23 视觉审查再次检测到 Conclusion 溢出 3-4 行至 page 9。可能是后续修改导致回归，需作者确认。\"\n  action_items: []\n  resolution: 'FALSE POSITIVE: 视觉验证确认正文恰好 8 页。R24 视觉审查确认主正文在第 8 页结束。'\n  resolution_round: 20\n\n- id: R20-N2\n  summary: Topic 变体控制设计存在 3 个未隔离混杂因素\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED]'\n  action_items: []\n  resolution: 'R21验证: method.tex和experiments.tex明确承认三个混杂因素, 指向Wiki-MLM vs JB-MLM'\n  resolution_round: 21\n\n- id: R20-N3\n  summary: Appendix Table 16 TOST 数据 (n=3) 与主文 (n=10) 不一致\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED] TOST扩展至n=10'\n  action_items: []\n  resolution: 'R21验证: 主文和附录统一为n=10 seeds'\n  resolution_round: 21\n\n# === Open / In-Progress issues (updated for Round 24) ===\n\n- id: R9-W1\n  summary: 长度混淆未充分排除\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 23\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: benign 12-20 turns vs jailbreak 3-10 turns 完全不重叠\n  - round: 16\n    reviewers: [1, 2]\n    note: R16 升级为 critical。R1 指出 adversarial padding 后 AA 暴跌 57pp。\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED] 两位Reviewer一致确认'\n  - round: 22\n    reviewers: [1]\n    note: \"R22 R1-N2 重新提出为 critical。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-N1 列为 Must-Fix。R2 交叉 REBUT→Should-Fix。Director 裁定 Should-Fix。\"\n  - round: 24\n    reviewers: []\n    note: \"R24 未单独再次提出。R23 action item (turn-count-only classifier) 状态未更新。降级为 warning。\"\n  action_items:\n  - round: 15\n    action: 主文 Section 4 或 5 加 1-2 句长度混淆讨论\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: 构造长度匹配对照数据；Section 5 prominently 讨论 AA padding collapse\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: 提供 turn-count-only classifier F1 作为 sanity check\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R9-W2\n  summary: Human data 上 evidence hierarchy 完全反转 (ToxicChat)\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 24\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: ToxicChat JB-MLM=0.837 >> 9-class=0.596\n  - round: 17\n    reviewers: [1, 2]\n    note: R17 两位 Reviewer 均列为 critical。\n  - round: 21\n    reviewers: [1, 2]\n    note: '[RESOLVED] 两位Reviewer一致确认'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 两位 Reviewer 独立再次列为 Must-Fix。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 两位 Reviewer 再次独立列为 Must-Fix。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 核心问题。R1-N1 + R2-N2 均为 Must-Fix + 交叉 AGREE。ToxicChat MLM(0.837)>>9-class(0.596) 差距24pp + WildChat FPR 68.1%。论文 'evidence hierarchy' 术语本身有误导性——实为 condition-dependent observations。R1 补充: 即使在合成 OOD '稳定' 条件下，顶部变体差异(1-4pp)也小于抽样误差。建议重命名为 'condition-dependent evidence landscape'。\"\n  action_items:\n  - round: 18\n    action: 'D081 MF1: Abstract/Intro/Conclusion scope 系统性收窄'\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: Section 4.6 ToxicChat 反转从1句扩展为1-2段深入分析; Conclusion 给出条件性结论\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: \"将 'evidence hierarchy' 重新定义为 'condition-dependent evidence landscape' 或类似表述; 主文系统讨论各反转条件(人类数据/策略多样攻击/大规模训练/WildChat部署)\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R13-N1\n  summary: 单一合成数据源限制跨攻击泛化声明可信度\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: 'R18 共识: disclosure 基本到位，但双重 OOD 评估缺失。'\n  - round: 21\n    reviewers: [1]\n    note: '[RESOLVED] scope qualifier全面'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 两位 Reviewer 独立重新提出。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 继续存在。hierarchy 仅在合成数据生态系统内成立。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 结构性问题持续存在。与 R9-W2(ToxicChat反转)和 WildChat FPR 形成证据链: 所有真实数据场景均不支持论文主要结论。即使 framing 完美修改，主要 take-away 仍是 'DAPT hierarchy exists but only in synthetic settings'——这限制了论文的实际影响力但不阻碍 Findings 接收。\"\n  action_items:\n  - round: 17\n    action: W-1 Abstract F1 后加 '(attack-side OOD; benign IID)' 限定\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: Table 2 增加 dual-OOD 行；Abstract/Conclusion 所有 OOD F1 标注为 upper bound + IID benign 条件\n    assigned_to: main_agent\n    status: resolved\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W1\n  summary: 新颖性不足——DAPT 应用 + 增量贡献不清\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: 方法新颖性有限是阻碍 Conference 推荐的主要原因之一。\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] 降级为warning. 叙事一致但novelty argumentation深度不足'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R2-N1 列为 critical。R1 交叉 AGREE 但建议降为 major。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-N1 再次列为 critical。共识: 需从 'unexpected' 重新定位为 'quantifying the magnitude and conditions'。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2 列为 Must-Fix + R1 部分 AGREE。R1 提出新颖性分三层: (1)DAPT>vanilla=低新颖性(预期); (2)scrambled≈correct on templates=中等新颖性(counter-intuitive); (3)hierarchy在人类数据反转=高信息量negative finding(未被充分开发)。共识: 问题是程度性的而非二元的——最具新颖性的发现未置于叙事中心，被淹没在平凡结论中。\"\n  action_items:\n  - round: 18\n    action: 重写 novelty positioning 为消融发现集合\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: Section 1 将 finding(i) 从 'unexpected' 改为 'systematic quantification'; Abstract 相应调整\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: \"重组叙事: 以 'why DAPT works, when it fails' 为主轴而非 'DAPT works'; 将 scrambled equivalence 和 human-data reversal 置于叙事中心\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W5\n  summary: Scale analysis 被架构差异混淆\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. DeBERTa vs RoBERTa混杂参数量, 建议Limitations加一句'\n  - round: 22\n    reviewers: [2]\n    note: \"R22 R2-W4: 仅 base-scale (125M-184M)。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 相关但不直接提及。\"\n  action_items:\n  - round: 17\n    action: Discussion 增加 DAPT scale-dependent 效用讨论\n    assigned_to: main_agent\n    status: resolved\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W7\n  summary: Abstract 信息密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. Abstract信息密度高+句法模糊'\n  - round: 22\n    reviewers: [2]\n    note: \"R22 R2 小问题: Abstract 中 'this hierarchy reverses' 后的修饰对象不清。\"\n  - round: 23\n    reviewers: [2]\n    note: \"R23 R2 交叉回应中继续提及 abstract 句法模糊。\"\n  - round: 24\n    reviewers: [2]\n    note: \"R24 未单独列出但与 R21-N1 合并。\"\n  action_items:\n  - round: 19\n    action: Abstract 压缩至 ~180 词\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R13-M1\n  summary: Missing references\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R2-W1 建议补充 Galinkin & Sablotny (2024)。\"\n  - round: 23\n    reviewers: [1]\n    note: \"R23 R1 建议补充 Perez and Wang (2022) red teaming 工作。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2 建议补充 representation compression 理论工作(如 Arora et al., 2019)和 proactive/early multi-turn detection 近期工作。R1 AGREE。\"\n  action_items:\n  - round: 22\n    action: 补充引用 Galinkin & Sablotny (2024) arXiv 2412.01547\n    assigned_to: main_agent\n    status: open\n  - round: 23\n    action: 确认 Perez and Wang (2022) 是否已引用或需补充\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: 补充 Arora et al. (2019) representation compression 和 proactive multi-turn detection 近期工作引用\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R14-N1\n  summary: 数据规模扩大后性能反常下降 (350→1000)\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] should-fix. 9-class也下降(0.994→0.889), 未给出解释'\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W5 再次提出。R2 交叉 AGREE。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 未单独提出但 R1 cross-response Q2 隐含提及 capacity-compensation 假设。问题仍 open。\"\n  action_items:\n  - round: 17\n    action: 弱化为 composition differences partially confound\n    assigned_to: main_agent\n    status: in_progress\n  - round: 23\n    action: 报告 1000 样本的 seed 一致性、training loss 或 data composition 证据\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R15-VIS1\n  summary: Figure 2 尺寸偏小，axis labels 约正文字号 50-60%\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. Figure 2 axis labels仍偏小'\n  - round: 24\n    reviewers: []\n    note: \"R24 视觉审查: Figure 5 坐标轴标签字号偏小(p8), Figure 6 SVD 尺寸较小(p8), p16 CKA heatmap 轴标签几乎不可读。\"\n  action_items:\n  - round: 15\n    action: Figure 2 字号放大至≥8pt\n    assigned_to: main_agent\n    status: in_progress\n  - round: 24\n    action: \"Figure 5/6 标注字号增大至正文70%以上; Appendix Figure 8 CKA heatmap 轴标签放大\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R16-W1\n  summary: Temporal modeling negative finding 讨论不足\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[RESOLVED]'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R1-W3: BiGRU 对 mean pooling 无优势(Table 30)。R2 交叉 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W3 再次提出 + R2-W4 AGREE。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-W4 Should-Fix + R1 强烈 AGREE。关键推论: BiGRU≈mean pooling + turn-order shuffling无影响 = 模型本质上做 bag-of-turns 检测。这直接挑战 'Multi-Turn' 叙事——模型未建模多轮动态(策略升级)，而是 per-turn 独立检测后聚合。论文将此表述为正面发现但未讨论对方法定位的影响。R1 提出可能解释: 多轮框架是工程需求(处理对话中的攻击嵌入)而非模型能力需求——但论文未做此区分。\"\n  action_items:\n  - round: 19\n    action: Discussion 讨论为什么 multi-turn 攻击的检测不需要时序建模\n    assigned_to: main_agent\n    status: resolved\n  - round: 22\n    action: Section 3.3 或 Section 5 明确说明 BiGRU 可被 mean pooling 替代且不影响检测性能\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: \"Discussion 新增段落: 明确区分 'multi-turn framework as engineering requirement (processing all turns)' vs 'multi-turn modeling as capability requirement (learning sequential dynamics)'; 承认当前模型属于前者\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R16-W2\n  summary: 效率对比定位不清\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: '[STILL_OPEN] minor. R1指出Introduction已标注43×, 但Abstract未标注'\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-M4: '24.3× speedup' 在 Abstract 首次出现时未给出基准。R1 AGREE。\"\n  action_items:\n  - round: 16\n    action: 效率对比加 deployment cost comparison 限定\n    assigned_to: main_agent\n    status: in_progress\n  - round: 24\n    action: \"Abstract 中 '24.3× speedup' 后简要标注 'vs LLM-as-judge'\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W1\n  summary: TOST δ=5pp margin 缺乏 practical significance 论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. δ=5pp缺practical significance论证'\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R1-W1 + R2 交叉 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W1 再次提出。共识: 方法论改进空间，不改变定性结论。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-M3 相关: McNemar's test '确认等价' 语言问题。R1 AGREE: 不拒绝H0≠确认等价，需改为 'finds no significant difference'。TOST 才是真正等价检验。\"\n  action_items:\n  - round: 17\n    action: Appendix TOST 部分增加 domain-specific practical significance 论证\n    assigned_to: main_agent\n    status: in_progress\n  - round: 23\n    action: \"[复发×4+轮] 补 δ=3pp sensitivity + practical significance 论证重写\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 24\n    action: \"修正 Section 4.3 'McNemar's test confirms equivalence' 为 'finds no significant difference'; 区分 absence of evidence vs evidence of absence\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M1\n  summary: 'Missing references: ADEPT, Echo Chamber Attack, Representation Bending'\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: '[STILL_OPEN] minor. ADEPT/Echo Chamber/RepBending未引用'\n  action_items:\n  - round: 17\n    action: 核实引用真实性和相关性\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R21-N1\n  summary: Abstract第二长句句法模糊——\"this hierarchy reverses\"后的修饰对象不清\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: 'NEW-1: \"on labeled multi-turn jailbreak data\"修饰对象歧义'\n  - round: 22\n    reviewers: [2]\n    note: \"R22 仍存在。\"\n  - round: 23\n    reviewers: [2]\n    note: \"R23 R2 交叉回应中继续提及。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-W2 再次标为 Should-Fix: Section 4.6 标题 'Human Data Validation' 暗示确认性结果但内容是反转/失败。R1 AGREE。且 ToxicChat 是单轮数据而论文标题聚焦 Multi-Turn。\"\n  action_items:\n  - round: 23\n    action: \"[复发×3轮] 重写为'Third, these advantages are condition-specific: on human-authored single-turn data, the hierarchy reverses'\"\n    assigned_to: main_agent\n    status: in_progress\n  - round: 24\n    action: \"Section 4.6 标题从 'Human Data Validation' 改为 'Human Data Evaluation' 或 'Transfer to Human-Authored Data'\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R1-W2\n  summary: 策略标注质量验证不充分\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 24\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: R16 两位 Reviewer 均再次指出 κ=0.78 n=50 不足\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R1-W4: 50样本9类→部分类别仅2-5个验证样本。R2 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W4 再次提出。共识: 增加样本至≥100并报告per-class κ。\"\n  - round: 24\n    reviewers: []\n    note: \"R24 未单独再提。R23 action item 仍 open。\"\n  action_items:\n  - round: 1\n    action: Limitations 已添加 caveat\n    assigned_to: main_agent\n    status: resolved\n  - round: 22\n    action: 增加标注验证样本量至≥100并报告per-class κ; Appendix Y caveat标注质量\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R22-N1\n  summary: Scrambled≈9-class 等价性能与论文叙事的张力\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R1-W2 首提: scrambled 在 DD/FTTD 上与 9-class TOST 等价。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 Abstract 限定为 template attacks。R2 交叉 AGREE。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R1 交叉 AGREE R2-S2: scrambled 是最具原创性实证贡献。但补充重要限定: TOST 在 ActorAttack 上未通过(p=0.183, d=0.44)，发现适用范围限于模板攻击。Abstract 已限定——确认 resolved。\"\n  action_items:\n  - round: 22\n    action: Section 5 增加段落讨论 classification objective structure vs label semantics\n    assigned_to: main_agent\n    status: open\n  - round: 23\n    action: Abstract 修改 \"not label semantics—drives generalization\" 为限定 template attacks 的表述\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R23 Reviewer PASS + R24 confirmed: abstract.tex L7 精准限定 'on template attacks'\"\n  resolution_round: 23\n\n- id: R22-W1\n  summary: 自创术语过多且定义不严谨——evidence hierarchy, discriminative compression 等\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R2-W2 首提。R1 交叉部分 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-W1 再次提出。共识: 首次使用处需一句话定义。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-W1 再列为 Should-Fix。R1 交叉 REBUT: 'evidence hierarchy' 和 'discriminative compression' 是合理的描述性术语，认知负荷增加合理。同意 'partition sufficiency' 过于晦涩可简化。总体判断: Minor 级别而非 Should-Fix。Director 裁定 resolved per R23: experiments.tex L6 Terminology 段已定义。\"\n  action_items:\n  - round: 22\n    action: 首次使用时给出一句话定义; 考虑将 'evidence hierarchy' 改为 'performance ranking'\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R23 Reviewer PASS: experiments.tex L6 Terminology 段首次使用前定义。R24 分歧(R1 REBUT R2 severity)不影响 resolution。\"\n  resolution_round: 23\n\n- id: R22-W2\n  summary: Conclusion 'reusable template' claim 超出单一任务的实验范围\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R2-W3 首提。R1 交叉 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-W3 再次提出。共识: 限定为 'template for future controlled studies of domain adaptation in safety-critical NLP tasks'。\"\n  action_items:\n  - round: 22\n    action: Conclusion 限定 'reusable template' 的适用范围\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R23 Reviewer PASS: conclusion.tex L29 限定为 'safety-critical NLP tasks'\"\n  resolution_round: 23\n\n# === Round 24 新增 issues ===\n\n- id: R24-MF1\n  summary: \"'Evidence hierarchy' 术语本身具有误导性——应改为条件依赖性表述\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-N2 Must-Fix + R1 AGREE: 一个在多个现实场景下反转的排序不应被称为 'hierarchy'。R1 补充: 即使在最有利条件下(合成OOD)，顶部变体差异(1-4pp)也远小于3-seed抽样误差，精细排序可能不稳健。共识: 重新命名为 'condition-dependent evidence landscape' 或 'performance ranking with boundary conditions'。\"\n  action_items:\n  - round: 24\n    action: \"全文替换 'evidence hierarchy' 为更准确术语; 主文系统列举四个反转条件\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R24-SF1\n  summary: BiGRU≈mean pooling 暗示 bag-of-turns 检测——挑战 'Multi-Turn' 核心叙事\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-W4 Should-Fix + R1 强烈 AGREE (称之为 'R2 比我更敏锐的观察')。Table 30 + Section 4.3: mean pooling 在 ID/OOD 完全等价 BiGRU + turn-order shuffling Δ<1pp。推论: 模型做的是 per-turn [CLS] embedding 独立判别后取平均 = bag-of-turns。论文标题 'Multi-Turn Jailbreak Detection' 的核心叙事被动摇——模型未学到多轮动态(策略升级)。R1 提出: 多轮框架可能是工程需求(不遗漏嵌入对话中的攻击)而非模型能力——但论文未做此区分。\"\n  action_items:\n  - round: 24\n    action: \"Discussion 新增 1 段: 区分 multi-turn framework (engineering) vs multi-turn modeling (learning dynamics); 明确承认当前模型属于前者; 讨论对标题定位的影响\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R24-SF2\n  summary: \"Section 4.6 'Human Data Validation' 标题误导——实际是 negative validation\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-W2 Should-Fix + R1 AGREE: 'Validation' 暗示确认性结果，但内容是反转/失败。且 ToxicChat 是单轮数据而论文标题聚焦 Multi-Turn，用单轮数据做 'validation' 有方法论张力(论文 Section 4.6 有说明但标题不准确)。\"\n  action_items:\n  - round: 24\n    action: \"Section 4.6 标题改为 'Transfer to Human-Authored Data' 或 'Human Data Evaluation'\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R24-SF3\n  summary: Related Work 对 multi-turn defense 方法缺乏结构化比较\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-W3 Should-Fix + R1 AGREE: Section 2 引用了 DeepContext/BIID/G-Guard 等方法但仅1-2句概括，未系统比较设计维度(编码器选择、时序建模方式、训练数据类型、评估攻击范围)。R1 建议增加结构化对比表(Appendix 亦可)。\"\n  action_items:\n  - round: 24\n    action: \"Related Work 或 Appendix 增加 multi-turn defense 方法结构化对比表(columns: method/encoder/temporal modeling/training data/evaluation scope)\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R24-M1\n  summary: Table 2 seed 报告格式不统一(部分有±std 部分无)\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-M1 + R1 AGREE: camera-ready 级修改。\"\n  action_items:\n  - round: 24\n    action: \"统一 Table 2 所有 cell 的 ±std 格式\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R24-M2\n  summary: Figure 2/3 y轴标签未指定 macro F1 还是 binary F1\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-M2 + R1 AGREE: Figure caption 应明确 F1 类型。\"\n  action_items:\n  - round: 24\n    action: \"Figure 2/3 caption 中明确标注 F1 类型(binary/macro)\"\n    assigned_to: main_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R23-MF1\n  summary: ToxicChat hierarchy 反转分析深度不足——核心叙事在人类数据上失效\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"两位 AGREE: ToxicChat 是唯一人类数据评估, MLM F1=0.837 大幅超越 classification 0.596。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 继续作为 Must-Fix。与 R9-W2 合并处理。R1 cross-response 对齐 R2: 论文对此反转的讨论深度不匹配问题严重性。\"\n  action_items:\n  - round: 23\n    action: Discussion 段 ToxicChat 因果分析(single-turn特性 + distributional gap + truncated evidence); Conclusion 条件性结论\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R23-MF3\n  summary: \"Unexpected findings\" 新颖性定位过高——classification>vanilla/MLM 在 DAPT 框架下可预期\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R2-N1 critical + R1 AGREE: Gururangan et al. (2020) 已证明 task-adaptive pretraining 优于 vanilla。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 继续作为 Must-Fix。R1 补充三层新颖性分析——真正有价值的不是 'DAPT works' 而是 boundary conditions 和 negative findings。与 R13-W1 合并处理。\"\n  action_items:\n  - round: 23\n    action: Introduction \"unexpected\" 改为 \"merit attention\" / \"systematic quantification\"; Contribution #1 重新措辞\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R23-SF2\n  summary: WildChat 68.1% FPR 暴露合成数据训练系统性偏差——Discussion 讨论不充分\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1 Must-Fix vs R2 Minor, Director 裁定 Should-Fix。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R1 cross-response 再次引用 WildChat FPR 作为 deployment 限制的关键证据。与 R9-W2 形成证据链。Section 5 'Deployment implications' 推荐 few-shot benign calibration 但未提及此 FPR 约束。\"\n  action_items:\n  - round: 23\n    action: Discussion WildChat FPR 处嵌入半句 distributional shift 归因\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R23-W1\n  summary: RoBERTa-large DAPT \"有害\"机制未解释——\"unnecessary\" vs \"harmful\" 解释缺口\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1-W4 + R2-W4 AGREE: 9-class DAPT F1 从 1.000→0.946 = actively harmful。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-Q2 + R1 AGREE: capacity-compensation 假设有洞察力——DAPT 补偿小模型容量不足，大模型不需要此补偿。论文简要提及 Appendix Q BERT-base proxy 但未直接回应。值得 Discussion 讨论。\"\n  action_items:\n  - round: 23\n    action: Section 4.4 或 Section 5 区分 DAPT 'unnecessary' 和 'harmful' 的机制; 讨论 CKA 分析对 355M 的发现\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R23-W2\n  summary: Topic 变体 5 vs 9 类别数量混淆——failure 可能因类别数不足而非标签无关\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1-W3 首提 + R2 交叉 AGREE。\"\n  - round: 24\n    reviewers: []\n    note: \"R24 未单独提及。R23 action item 仍 open。\"\n  action_items:\n  - round: 23\n    action: 补充 9→5 class merging 控制实验，或在 Limitations 中承认类别数量混淆\n    assigned_to: main_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 2235 · 2026-05-25T21:41:21.283917+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"issues_yaml is not valid YAML: while parsing a block mapping\\n  in \\\"&lt;unicode string>\\\", line 1315, column 3:\\n    - id: R23-MF3\\n      ^\\nexpected &lt;block end>, but found '&lt;scalar>'\\n  in \\\"&lt;unicode string>\\\", line 1316, column 34:\\n      summary: \\\"Unexpected findings\\\" 新颖性定位过高——classification>vanilla/ ... \\n                                     ^\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2236 · 2026-05-25T21:45:16.916521+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "issues_yaml": "issues:\n# === 历史 resolved issues ===\n- id: R1-N1\n  summary: Evidence hierarchy 统计基础不一致\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: binary/scrambled 仅 seed 42\n  action_items:\n  - round: 1\n    action: 训练 binary/scrambled 3-seed\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005\"\n  resolution_round: 1\n\n- id: R1-N2\n  summary: Three-layer robustness attribution 缺乏统计显著性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R1 首提 N2\n  action_items:\n  - round: 1\n    action: \"McNemar's test + bootstrap CI\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: MF2 完成\n  resolution_round: 1\n\n- id: R1-N3\n  summary: 缺少与已发表 multi-turn defense 的直接实验对比\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R1 首提 N3\n  - round: 2\n    reviewers: [1, 2]\n    note: Round 1 修复不充分，再次提出\n  action_items:\n  - round: 1\n    action: 重构论证\n    assigned_to: paper_agent\n    status: resolved\n  - round: 2\n    action: Analysis paper reframe\n    assigned_to: research_director\n    status: resolved\n  resolution: Analysis paper reframe 完成。\n  resolution_round: 3\n\n- id: R1-N4\n  summary: 数据集规模过小\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: \"500训练+76-118测试+3seeds仍不足\"\n  action_items:\n  - round: 2\n    action: \"Bootstrap 95% CI + permutation test\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"exp9 BCa bootstrap 95% CI + paired permutation test 完成。\"\n  resolution_round: 2\n\n- id: R2-N3\n  summary: 有效 OOD 评估实质上是 single-dataset\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R2 首提\n  action_items:\n  - round: 1\n    action: ActorAttack OOD 数据生成\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"EXP-2 完成: ActorAttack 118 conversations\"\n  resolution_round: 1\n\n- id: R1-W1\n  summary: \"Mean pooling=BiGRU 结论基于 single seed\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: \"Paper Agent 已弱化。multi-seed 实验验证。\"\n  resolution_round: 1\n\n- id: R1-W3\n  summary: LLM-as-judge baseline 仅测 IID\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions: []\n  action_items: []\n  resolution: EXP-5 完成\n  resolution_round: 1\n\n- id: R1-W4\n  summary: TF-IDF LR 强表现未被充分讨论\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: \"TF-IDF per-prefix + ActorAttack 完成。\"\n  resolution_round: 3\n\n- id: R1-W5\n  summary: 可复现性不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions: []\n  action_items: []\n  resolution: Paper Agent 已添加 Appendix C\n  resolution_round: 1\n\n- id: R2-W1\n  summary: Abstract 过度堆砌数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: \"Abstract 压缩至 ~190 words。\"\n  resolution_round: 3\n\n- id: R2-W2\n  summary: partially falsified 叙事对接收不利\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: Framing 调整完成。\n  resolution_round: 3\n\n- id: R8-N4\n  summary: LLM-as-judge baseline 对比不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  mentions:\n  - round: 8\n    reviewers: [2]\n    note: \"GPT-5.5 不可解析可能是 prompt 设计问题\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 两位 Reviewer 均指出 prompt 未提供、未尝试 prompt 优化\"\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items:\n  - round: 14\n    action: 附录提供 LLM-as-judge prompt 模板\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: 明确标注为 deployment cost comparison 而非方法论对比\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R21验证: GPT F1标注upper bounds\"\n  resolution_round: 21\n\n- id: R9-M1\n  summary: \"Abstract 中 Llama Guard 3 1.8% 有 misleading 风险\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] minor. Abstract中Llama Guard 3缺zero-shot限定词\"\n  action_items: []\n  resolution: \"Abstract 已使用 zero-shot 限定。\"\n  resolution_round: 22\n\n- id: R13-N2\n  summary: \"WildChat FPR=68.1% + few-shot 修复验证不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items:\n  - round: 19\n    action: 补充 few-shot benign adaptation 的实现细节\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R21验证: few-shot实现细节完整(Stage-2 BiGRU, encoder frozen, N benign, BCE, 5 epochs)\"\n  resolution_round: 21\n\n- id: R13-N3\n  summary: 机制解释缺乏直接证据\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED]\"\n  action_items:\n  - round: 19\n    action: \"Section 5 讨论 discriminative compression vs representation collapse 替代解释\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R21验证: 因果声明弱化为appears necessary, consistent with\"\n  resolution_round: 21\n\n- id: R13-W2\n  summary: \"DisPeD 命名 / Disentangled 术语误用\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: Footnote 1清晰区分ablation methodology与disentangled representation learning\"\n  resolution_round: 21\n\n- id: R13-W3\n  summary: \"Scrambled label AA 非等价 (d=0.44)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: AA上d=0.44, TOST p=0.183明确标注\"\n  resolution_round: 21\n\n- id: R13-W4\n  summary: \"Mixed-LLM AA=0.504 + MLM 崩溃\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 明确标注chance level, indistinguishable from majority baseline\"\n  resolution_round: 21\n\n- id: R13-W6\n  summary: FITD 缺乏区分力\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions: []\n  action_items: []\n  resolution: \"R15 不再提出，视为已充分缓解。\"\n  resolution_round: 15\n\n- id: R14-W1\n  summary: BCa Bootstrap 跨 seed 池化\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 标注assumes cross-seed independence and is exploratory\"\n  resolution_round: 21\n\n- id: R14-W2\n  summary: Benign-side 仅 WildChat 单一数据源\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: OASST2 双源验证解决。\n  resolution_round: 15\n\n- id: R14-W3\n  summary: Figure 2 缺失 ActorAttack\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: \"Figure 2 已增加 ActorAttack。\"\n  resolution_round: 15\n\n- id: R14-I1\n  summary: 主文 Conclusion 溢出到 page 9\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: Conclusion 确认在 page 8 内。\n  resolution_round: 15\n\n- id: R15-SF1\n  summary: \"判别性压缩因果链不完整 + SVD 数据泄漏\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: Discussion使用consistent with而非因果声明\"\n  resolution_round: 21\n\n- id: R15-SF4\n  summary: C2 complexity-dependent boundary 证据基础狭窄\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions: []\n  action_items: []\n  resolution: \"R16-R19 不再单独提出。\"\n  resolution_round: 16\n\n- id: R15-SF6\n  summary: \"方差缩减 4-20x 声明基于 n=3 seeds\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 改为descriptively 3-23x\"\n  resolution_round: 21\n\n- id: R16-N1\n  summary: \"Any deterministic partition suffices 声称与 Topic 变体失败直接矛盾\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 区分domain-relevant vs arbitrary classification, 指向Wiki-MLM vs JB-MLM为cleaner test\"\n  resolution_round: 21\n\n- id: R16-W3\n  summary: Two-axis framework 新颖性争议\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: two-axis定位为organizational framework而非独立贡献\"\n  resolution_round: 21\n\n- id: R16-W4\n  summary: 数据划分描述不够清晰\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 明确说明Stage 1用train+val, Stage 2用train/val/test\"\n  resolution_round: 21\n\n- id: R17-N1\n  summary: \"n=3 seeds 方差缩减 claims 统计可靠性不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 同R15-SF6, 方差声明改为descriptive\"\n  resolution_round: 21\n\n- id: R17-W2\n  summary: \"Cross-LLM Abstract remains robust 与正文 preliminary 矛盾\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: Abstract不再有remains robust\"\n  resolution_round: 21\n\n- id: R17-W3\n  summary: \"RoBERTa-large DAPT 有害——核心 thesis scale-dependent\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 实验/讨论/结论三处承认scale-dependent并标注counterproductive at 355M\"\n  resolution_round: 21\n\n- id: R18-N1\n  summary: \"Structural complexity 缺乏形式化定义\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 操作化为transition rate<0.1(template) vs >0.3(complex)\"\n  resolution_round: 21\n\n- id: R18-W1\n  summary: 缺少与已发表多轮检测方法的直接实验对比\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: Related Work说明无公开实现, Appendix提供BERT-base proxy\"\n  resolution_round: 21\n\n- id: R19-E1\n  summary: \"experiments.tex L114 d<0.1 数值错误 (应为 d<=0.14)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: \"[RESOLVED] 数值已修正\"\n  action_items: []\n  resolution: \"R21验证: d<=0.14与Table一致\"\n  resolution_round: 21\n\n- id: R19-E2\n  summary: \"intro L24 the first 缺少 to our knowledge 限定\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions: []\n  action_items: []\n  resolution: \"当前文本已包含 to our knowledge 限定。\"\n  resolution_round: 20\n\n- id: R19-E3\n  summary: \"Abstract requires domain adaptation 与 RoBERTa-large vanilla AA=1.000 矛盾\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions: []\n  action_items: []\n  resolution: \"Abstract 已修改为 benefits substantially from。\"\n  resolution_round: 20\n\n- id: R20-N1\n  summary: \"正文超过 8 页限制\"\n  category: format\n  severity: critical\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: \"FALSE POSITIVE — Sections 1-6 在 p1-p8, Limitations (p9) 不计入限制。\"\n  - round: 24\n    reviewers: []\n    note: \"R24 视觉审查确认主正文在第 8 页结束，符合 EMNLP 2026 的 8 页正文限制。\"\n  action_items: []\n  resolution: \"FALSE POSITIVE: R24 视觉审查确认正文恰好 8 页。\"\n  resolution_round: 20\n\n- id: R20-N2\n  summary: \"Topic 变体控制设计存在 3 个未隔离混杂因素\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: method.tex和experiments.tex明确承认三个混杂因素, 指向Wiki-MLM vs JB-MLM\"\n  resolution_round: 21\n\n- id: R20-N3\n  summary: \"Appendix Table 16 TOST 数据 (n=3) 与主文 (n=10) 不一致\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED] TOST扩展至n=10\"\n  action_items: []\n  resolution: \"R21验证: 主文和附录统一为n=10 seeds\"\n  resolution_round: 21\n\n# === Open / In-Progress issues (updated for Round 24) ===\n\n- id: R9-W1\n  summary: 长度混淆未充分排除\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 23\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"benign 12-20 turns vs jailbreak 3-10 turns 完全不重叠\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 升级为 critical。R1 指出 adversarial padding 后 AA 暴跌 57pp。\"\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED] 两位Reviewer一致确认\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-N1 列为 Must-Fix。Director 裁定 Should-Fix。\"\n  - round: 24\n    reviewers: []\n    note: \"R24 未单独再次提出。R23 action item (turn-count-only classifier) 状态未更新。降级为 warning。\"\n  action_items:\n  - round: 15\n    action: \"主文 Section 4 或 5 加 1-2 句长度混淆讨论\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: \"构造长度匹配对照数据；Section 5 prominently 讨论 AA padding collapse\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: \"提供 turn-count-only classifier F1 作为 sanity check\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-W2\n  summary: \"Human data 上 evidence hierarchy 完全反转 (ToxicChat)\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 24\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"ToxicChat JB-MLM=0.837 >> 9-class=0.596\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 两位 Reviewer 均列为 critical。\"\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED] 两位Reviewer一致确认\"\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 两位 Reviewer 独立再次列为 Must-Fix。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 两位 Reviewer 再次独立列为 Must-Fix。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 核心问题。R1-N1 + R2-N2 均为 Must-Fix + 交叉 AGREE。差距24pp + WildChat FPR 68.1%。建议重命名为 condition-dependent evidence landscape。\"\n  action_items:\n  - round: 18\n    action: \"D081 MF1: Abstract/Intro/Conclusion scope 系统性收窄\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: \"Section 4.6 ToxicChat 反转从1句扩展为1-2段深入分析; Conclusion 给出条件性结论\"\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: \"将 evidence hierarchy 重新定义为 condition-dependent evidence landscape; 主文系统讨论各反转条件\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-N1\n  summary: 单一合成数据源限制跨攻击泛化声明可信度\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 共识: disclosure 基本到位，但双重 OOD 评估缺失。\"\n  - round: 21\n    reviewers: [1]\n    note: \"[RESOLVED] scope qualifier全面\"\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 两位 Reviewer 独立重新提出。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 继续存在。hierarchy 仅在合成数据生态系统内成立。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 结构性问题。所有真实数据场景均不支持论文主要结论。限制影响力但不阻碍 Findings 接收。\"\n  action_items:\n  - round: 17\n    action: \"W-1 Abstract F1 后加 (attack-side OOD; benign IID) 限定\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: \"Table 2 增加 dual-OOD 行；Abstract/Conclusion 所有 OOD F1 标注为 upper bound + IID benign 条件\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W1\n  summary: \"新颖性不足——DAPT 应用 + 增量贡献不清\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: \"方法新颖性有限是阻碍 Conference 推荐的主要原因之一。\"\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] 降级为warning\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-N1 列为 critical。需从 unexpected 重新定位为 quantifying the magnitude and conditions。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2 Must-Fix + R1 部分 AGREE。R1 提出三层新颖性分析。共识: 最具新颖性的发现未置于叙事中心。\"\n  action_items:\n  - round: 18\n    action: 重写 novelty positioning 为消融发现集合\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: \"Section 1 将 finding(i) 从 unexpected 改为 systematic quantification\"\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: \"重组叙事以 why DAPT works, when it fails 为主轴; 将 scrambled equivalence 和 human-data reversal 置于叙事中心\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W5\n  summary: Scale analysis 被架构差异混淆\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] minor. DeBERTa vs RoBERTa混杂参数量\"\n  - round: 22\n    reviewers: [2]\n    note: \"R22 R2-W4: 仅 base-scale (125M-184M)。\"\n  action_items:\n  - round: 17\n    action: \"Discussion 增加 DAPT scale-dependent 效用讨论\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W7\n  summary: Abstract 信息密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] minor. Abstract信息密度高+句法模糊\"\n  - round: 24\n    reviewers: [2]\n    note: \"R24 未单独列出但与 R21-N1 合并。\"\n  action_items:\n  - round: 19\n    action: \"Abstract 压缩至 ~180 词\"\n    assigned_to: main_agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M1\n  summary: Missing references\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 建议补充 Galinkin and Sablotny (2024)。\"\n  - round: 23\n    reviewers: [1]\n    note: \"R23 建议补充 Perez and Wang (2022)。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 建议补充 Arora et al. (2019) representation compression 和 proactive multi-turn detection 近期工作。\"\n  action_items:\n  - round: 22\n    action: \"补充引用 Galinkin and Sablotny (2024) arXiv 2412.01547\"\n    assigned_to: main_agent\n    status: open\n  - round: 23\n    action: \"确认 Perez and Wang (2022) 是否已引用或需补充\"\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: \"补充 Arora et al. (2019) representation compression 和 proactive multi-turn detection 近期工作引用\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-N1\n  summary: \"数据规模扩大后性能反常下降 (350->1000)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] should-fix. 9-class也下降(0.994->0.889)\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W5 再次提出。R2 交叉 AGREE。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R1 cross-response Q2 隐含提及 capacity-compensation 假设。问题仍 open。\"\n  action_items:\n  - round: 17\n    action: \"弱化为 composition differences partially confound\"\n    assigned_to: main_agent\n    status: in_progress\n  - round: 23\n    action: \"报告 1000 样本的 seed 一致性、training loss 或 data composition 证据\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-VIS1\n  summary: \"Figure axis labels 偏小\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] minor. Figure 2 axis labels仍偏小\"\n  - round: 24\n    reviewers: []\n    note: \"R24 视觉审查: Figure 5 坐标轴标签字号偏小(p8), Figure 6 SVD 尺寸较小(p8), p16 CKA heatmap 轴标签几乎不可读。\"\n  action_items:\n  - round: 15\n    action: \"Figure 2 字号放大至>=8pt\"\n    assigned_to: main_agent\n    status: in_progress\n  - round: 24\n    action: \"Figure 5/6 标注字号增大至正文70%以上; Appendix Figure 8 CKA heatmap 轴标签放大\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W1\n  summary: Temporal modeling negative finding 讨论不足\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R1-W3: BiGRU 对 mean pooling 无优势(Table 30)。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W3 + R2-W4 AGREE。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-W4 Should-Fix + R1 强烈 AGREE。模型本质是 bag-of-turns 检测，挑战 Multi-Turn 叙事。\"\n  action_items:\n  - round: 19\n    action: \"Discussion 讨论为什么 multi-turn 攻击的检测不需要时序建模\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 22\n    action: \"Section 3.3 或 Section 5 明确说明 BiGRU 可被 mean pooling 替代\"\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: \"Discussion 新增段落区分 multi-turn framework (engineering) vs multi-turn modeling (learning dynamics)\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W2\n  summary: 效率对比定位不清\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[STILL_OPEN] minor. Abstract未标注基准\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-M4: 24.3x speedup 在 Abstract 首次出现时未给出基准。R1 AGREE。\"\n  action_items:\n  - round: 16\n    action: \"效率对比加 deployment cost comparison 限定\"\n    assigned_to: main_agent\n    status: in_progress\n  - round: 24\n    action: \"Abstract 中 24.3x speedup 后简要标注 vs LLM-as-judge\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W1\n  summary: \"TOST delta=5pp margin 缺乏 practical significance 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] minor\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 共识: 方法论改进空间，不改变定性结论。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-M3: McNemar confirms equivalence 语言问题。R1 AGREE: 需改为 finds no significant difference。\"\n  action_items:\n  - round: 17\n    action: \"Appendix TOST 部分增加 domain-specific practical significance 论证\"\n    assigned_to: main_agent\n    status: in_progress\n  - round: 23\n    action: \"补 delta=3pp sensitivity + practical significance 论证重写\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 24\n    action: \"修正 Section 4.3 McNemar confirms equivalence 为 finds no significant difference\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M1\n  summary: \"Missing references: ADEPT, Echo Chamber Attack, Representation Bending\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] minor\"\n  action_items:\n  - round: 17\n    action: \"核实引用真实性和相关性\"\n    assigned_to: main_agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-N1\n  summary: \"Abstract 句法模糊——this hierarchy reverses 后的修饰对象不清\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"on labeled multi-turn jailbreak data 修饰对象歧义\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-W2: Section 4.6 标题 Human Data Validation 暗示确认性结果但内容是反转。R1 AGREE。\"\n  action_items:\n  - round: 23\n    action: \"重写为 these advantages are condition-specific: on human-authored single-turn data, the hierarchy reverses\"\n    assigned_to: main_agent\n    status: in_progress\n  - round: 24\n    action: \"Section 4.6 标题从 Human Data Validation 改为 Transfer to Human-Authored Data\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W2\n  summary: 策略标注质量验证不充分\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 23\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 两位 Reviewer 均再次指出 kappa=0.78 n=50 不足\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 共识: 增加样本至>=100并报告per-class kappa。\"\n  action_items:\n  - round: 1\n    action: \"Limitations 已添加 caveat\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 22\n    action: \"增加标注验证样本量至>=100并报告per-class kappa\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-N1\n  summary: \"Scrambled approx 9-class 等价性能与论文叙事的张力\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R1-W2 首提: scrambled 在 DD/FTTD 上与 9-class TOST 等价。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 confirmed resolved. Abstract 限定 on template attacks。\"\n  action_items:\n  - round: 22\n    action: \"Section 5 增加段落讨论 classification objective structure vs label semantics\"\n    assigned_to: main_agent\n    status: open\n  - round: 23\n    action: \"Abstract 限定 template attacks\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R23 PASS + R24 confirmed: abstract.tex L7 精准限定 on template attacks\"\n  resolution_round: 23\n\n- id: R22-W1\n  summary: \"自创术语过多且定义不严谨\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R2-W2 首提。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2 再列 Should-Fix，R1 REBUT 降为 Minor。experiments.tex L6 已定义。Director 维持 resolved。\"\n  action_items:\n  - round: 22\n    action: \"首次使用时给出一句话定义\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R23 PASS: experiments.tex L6 Terminology 段定义。R24 R1 REBUT severity 不影响 resolution。\"\n  resolution_round: 23\n\n- id: R22-W2\n  summary: \"Conclusion reusable template claim 超出实验范围\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R2-W3 首提。R1 交叉 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"限定为 safety-critical NLP tasks。\"\n  action_items:\n  - round: 22\n    action: \"Conclusion 限定 reusable template 的适用范围\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R23 PASS: conclusion.tex L29 限定为 safety-critical NLP tasks\"\n  resolution_round: 23\n\n# === Round 24 新增 issues ===\n\n- id: R24-MF1\n  summary: \"Evidence hierarchy 术语本身具有误导性——应改为条件依赖性表述\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-N2 Must-Fix + R1 AGREE: 多个现实场景下反转的排序不应称为 hierarchy。即使合成OOD下顶部变体差异(1-4pp)也小于抽样误差。\"\n  action_items:\n  - round: 24\n    action: \"全文替换 evidence hierarchy 为更准确术语; 主文系统列举四个反转条件\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-SF1\n  summary: \"BiGRU approx mean pooling 暗示 bag-of-turns 检测——挑战 Multi-Turn 核心叙事\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-W4 + R1 强烈 AGREE。Table 30 + Section 4.3 确认。模型做 per-turn 独立检测后聚合。Multi-Turn 标题叙事被动摇。\"\n  action_items:\n  - round: 24\n    action: \"Discussion 新增段落区分 multi-turn framework (engineering) vs multi-turn modeling (learning dynamics)\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-SF2\n  summary: \"Section 4.6 Human Data Validation 标题误导——实际是 negative validation\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-W2 + R1 AGREE: Validation 暗示确认性结果但内容是反转。ToxicChat 是单轮而论文标题聚焦 Multi-Turn。\"\n  action_items:\n  - round: 24\n    action: \"标题改为 Transfer to Human-Authored Data 或 Human Data Evaluation\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-SF3\n  summary: \"Related Work 对 multi-turn defense 方法缺乏结构化比较\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-W3 + R1 AGREE: DeepContext/BIID/G-Guard 仅1-2句概括，未系统比较设计维度。\"\n  action_items:\n  - round: 24\n    action: \"Related Work 或 Appendix 增加 multi-turn defense 结构化对比表\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-M1\n  summary: \"Table 2 seed 报告格式不统一\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"部分 cell 有 +/-std 部分没有。camera-ready 级修改。\"\n  action_items:\n  - round: 24\n    action: \"统一 Table 2 所有 cell 的 +/-std 格式\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-M2\n  summary: \"Figure 2/3 y轴标签未指定 F1 类型\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"Section 4.1 说明 F1 for binary jailbreak detection 但图中未标注。\"\n  action_items:\n  - round: 24\n    action: \"Figure 2/3 caption 中明确标注 F1 类型\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-MF1\n  summary: \"ToxicChat hierarchy 反转分析深度不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"MLM F1=0.837 大幅超越 classification 0.596。论文用一句话带过。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 继续 Must-Fix。与 R9-W2 合并处理。\"\n  action_items:\n  - round: 23\n    action: \"Discussion 段 ToxicChat 因果分析; Conclusion 条件性结论\"\n    assigned_to: main_agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-MF3\n  summary: \"Unexpected findings 新颖性定位过高\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"Gururangan et al. (2020) 已证明 task-adaptive pretraining 优于 vanilla。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 继续 Must-Fix。R1 补充三层新颖性分析。与 R13-W1 合并。\"\n  action_items:\n  - round: 23\n    action: \"Introduction unexpected 改为 systematic quantification\"\n    assigned_to: main_agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-SF2\n  summary: \"WildChat 68.1% FPR 暴露合成数据训练系统性偏差\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"Director 裁定 Should-Fix。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R1 再次引用 WildChat FPR 作为 deployment 限制关键证据。Section 5 推荐未提及此约束。\"\n  action_items:\n  - round: 23\n    action: \"Discussion WildChat FPR 处嵌入 distributional shift 归因\"\n    assigned_to: main_agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W1\n  summary: \"RoBERTa-large DAPT harmful 机制未解释\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"9-class DAPT F1 从 1.000->0.946 = actively harmful。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-Q2 + R1 AGREE: capacity-compensation 假设有洞察力。论文未直接回应。\"\n  action_items:\n  - round: 23\n    action: \"Section 4.4 或 Section 5 区分 unnecessary 和 harmful 的机制\"\n    assigned_to: main_agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W2\n  summary: \"Topic 变体 5 vs 9 类别数量混淆\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"failure 可能因类别数不足而非标签无关。建议 9->5 class merging 控制实验。\"\n  - round: 24\n    reviewers: []\n    note: \"R24 未单独提及。R23 action item 仍 open。\"\n  action_items:\n  - round: 23\n    action: \"补充 9->5 class merging 控制实验，或在 Limitations 中承认\"\n    assigned_to: main_agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "issues_yaml": "issues:\n# === 历史 resolved issues ===\n- id: R1-N1\n  summary: Evidence hierarchy 统计基础不一致\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: binary/scrambled 仅 seed 42\n  action_items:\n  - round: 1\n    action: 训练 binary/scrambled 3-seed\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005\"\n  resolution_round: 1\n\n- id: R1-N2\n  summary: Three-layer robustness attribution 缺乏统计显著性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R1 首提 N2\n  action_items:\n  - round: 1\n    action: \"McNemar's test + bootstrap CI\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: MF2 完成\n  resolution_round: 1\n\n- id: R1-N3\n  summary: 缺少与已发表 multi-turn defense 的直接实验对比\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R1 首提 N3\n  - round: 2\n    reviewers: [1, 2]\n    note: Round 1 修复不充分，再次提出\n  action_items:\n  - round: 1\n    action: 重构论证\n    assigned_to: paper_agent\n    status: resolved\n  - round: 2\n    action: Analysis paper reframe\n    assigned_to: research_director\n    status: resolved\n  resolution: Analysis paper reframe 完成。\n  resolution_round: 3\n\n- id: R1-N4\n  summary: 数据集规模过小\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: \"500训练+76-118测试+3seeds仍不足\"\n  action_items:\n  - round: 2\n    action: \"Bootstrap 95% CI + permutation test\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"exp9 BCa bootstrap 95% CI + paired permutation test 完成。\"\n  resolution_round: 2\n\n- id: R2-N3\n  summary: 有效 OOD 评估实质上是 single-dataset\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: R2 首提\n  action_items:\n  - round: 1\n    action: ActorAttack OOD 数据生成\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"EXP-2 完成: ActorAttack 118 conversations\"\n  resolution_round: 1\n\n- id: R1-W1\n  summary: \"Mean pooling=BiGRU 结论基于 single seed\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: \"Paper Agent 已弱化。multi-seed 实验验证。\"\n  resolution_round: 1\n\n- id: R1-W3\n  summary: LLM-as-judge baseline 仅测 IID\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions: []\n  action_items: []\n  resolution: EXP-5 完成\n  resolution_round: 1\n\n- id: R1-W4\n  summary: TF-IDF LR 强表现未被充分讨论\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: \"TF-IDF per-prefix + ActorAttack 完成。\"\n  resolution_round: 3\n\n- id: R1-W5\n  summary: 可复现性不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions: []\n  action_items: []\n  resolution: Paper Agent 已添加 Appendix C\n  resolution_round: 1\n\n- id: R2-W1\n  summary: Abstract 过度堆砌数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: \"Abstract 压缩至 ~190 words。\"\n  resolution_round: 3\n\n- id: R2-W2\n  summary: partially falsified 叙事对接收不利\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions: []\n  action_items: []\n  resolution: Framing 调整完成。\n  resolution_round: 3\n\n- id: R8-N4\n  summary: LLM-as-judge baseline 对比不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  mentions:\n  - round: 8\n    reviewers: [2]\n    note: \"GPT-5.5 不可解析可能是 prompt 设计问题\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 两位 Reviewer 均指出 prompt 未提供、未尝试 prompt 优化\"\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items:\n  - round: 14\n    action: 附录提供 LLM-as-judge prompt 模板\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: 明确标注为 deployment cost comparison 而非方法论对比\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R21验证: GPT F1标注upper bounds\"\n  resolution_round: 21\n\n- id: R9-M1\n  summary: \"Abstract 中 Llama Guard 3 1.8% 有 misleading 风险\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] minor. Abstract中Llama Guard 3缺zero-shot限定词\"\n  action_items: []\n  resolution: \"Abstract 已使用 zero-shot 限定。\"\n  resolution_round: 22\n\n- id: R13-N2\n  summary: \"WildChat FPR=68.1% + few-shot 修复验证不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items:\n  - round: 19\n    action: 补充 few-shot benign adaptation 的实现细节\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R21验证: few-shot实现细节完整(Stage-2 BiGRU, encoder frozen, N benign, BCE, 5 epochs)\"\n  resolution_round: 21\n\n- id: R13-N3\n  summary: 机制解释缺乏直接证据\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED]\"\n  action_items:\n  - round: 19\n    action: \"Section 5 讨论 discriminative compression vs representation collapse 替代解释\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R21验证: 因果声明弱化为appears necessary, consistent with\"\n  resolution_round: 21\n\n- id: R13-W2\n  summary: \"DisPeD 命名 / Disentangled 术语误用\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: Footnote 1清晰区分ablation methodology与disentangled representation learning\"\n  resolution_round: 21\n\n- id: R13-W3\n  summary: \"Scrambled label AA 非等价 (d=0.44)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: AA上d=0.44, TOST p=0.183明确标注\"\n  resolution_round: 21\n\n- id: R13-W4\n  summary: \"Mixed-LLM AA=0.504 + MLM 崩溃\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 明确标注chance level, indistinguishable from majority baseline\"\n  resolution_round: 21\n\n- id: R13-W6\n  summary: FITD 缺乏区分力\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions: []\n  action_items: []\n  resolution: \"R15 不再提出，视为已充分缓解。\"\n  resolution_round: 15\n\n- id: R14-W1\n  summary: BCa Bootstrap 跨 seed 池化\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 标注assumes cross-seed independence and is exploratory\"\n  resolution_round: 21\n\n- id: R14-W2\n  summary: Benign-side 仅 WildChat 单一数据源\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: OASST2 双源验证解决。\n  resolution_round: 15\n\n- id: R14-W3\n  summary: Figure 2 缺失 ActorAttack\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: \"Figure 2 已增加 ActorAttack。\"\n  resolution_round: 15\n\n- id: R14-I1\n  summary: 主文 Conclusion 溢出到 page 9\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions: []\n  action_items: []\n  resolution: Conclusion 确认在 page 8 内。\n  resolution_round: 15\n\n- id: R15-SF1\n  summary: \"判别性压缩因果链不完整 + SVD 数据泄漏\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: Discussion使用consistent with而非因果声明\"\n  resolution_round: 21\n\n- id: R15-SF4\n  summary: C2 complexity-dependent boundary 证据基础狭窄\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions: []\n  action_items: []\n  resolution: \"R16-R19 不再单独提出。\"\n  resolution_round: 16\n\n- id: R15-SF6\n  summary: \"方差缩减 4-20x 声明基于 n=3 seeds\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 改为descriptively 3-23x\"\n  resolution_round: 21\n\n- id: R16-N1\n  summary: \"Any deterministic partition suffices 声称与 Topic 变体失败直接矛盾\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 区分domain-relevant vs arbitrary classification, 指向Wiki-MLM vs JB-MLM为cleaner test\"\n  resolution_round: 21\n\n- id: R16-W3\n  summary: Two-axis framework 新颖性争议\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: two-axis定位为organizational framework而非独立贡献\"\n  resolution_round: 21\n\n- id: R16-W4\n  summary: 数据划分描述不够清晰\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 明确说明Stage 1用train+val, Stage 2用train/val/test\"\n  resolution_round: 21\n\n- id: R17-N1\n  summary: \"n=3 seeds 方差缩减 claims 统计可靠性不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 同R15-SF6, 方差声明改为descriptive\"\n  resolution_round: 21\n\n- id: R17-W2\n  summary: \"Cross-LLM Abstract remains robust 与正文 preliminary 矛盾\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: Abstract不再有remains robust\"\n  resolution_round: 21\n\n- id: R17-W3\n  summary: \"RoBERTa-large DAPT 有害——核心 thesis scale-dependent\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 实验/讨论/结论三处承认scale-dependent并标注counterproductive at 355M\"\n  resolution_round: 21\n\n- id: R18-N1\n  summary: \"Structural complexity 缺乏形式化定义\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: 操作化为transition rate<0.1(template) vs >0.3(complex)\"\n  resolution_round: 21\n\n- id: R18-W1\n  summary: 缺少与已发表多轮检测方法的直接实验对比\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: Related Work说明无公开实现, Appendix提供BERT-base proxy\"\n  resolution_round: 21\n\n- id: R19-E1\n  summary: \"experiments.tex L114 d<0.1 数值错误 (应为 d<=0.14)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: \"[RESOLVED] 数值已修正\"\n  action_items: []\n  resolution: \"R21验证: d<=0.14与Table一致\"\n  resolution_round: 21\n\n- id: R19-E2\n  summary: \"intro L24 the first 缺少 to our knowledge 限定\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions: []\n  action_items: []\n  resolution: \"当前文本已包含 to our knowledge 限定。\"\n  resolution_round: 20\n\n- id: R19-E3\n  summary: \"Abstract requires domain adaptation 与 RoBERTa-large vanilla AA=1.000 矛盾\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions: []\n  action_items: []\n  resolution: \"Abstract 已修改为 benefits substantially from。\"\n  resolution_round: 20\n\n- id: R20-N1\n  summary: \"正文超过 8 页限制\"\n  category: format\n  severity: critical\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: \"FALSE POSITIVE — Sections 1-6 在 p1-p8, Limitations (p9) 不计入限制。\"\n  - round: 24\n    reviewers: []\n    note: \"R24 视觉审查确认主正文在第 8 页结束，符合 EMNLP 2026 的 8 页正文限制。\"\n  action_items: []\n  resolution: \"FALSE POSITIVE: R24 视觉审查确认正文恰好 8 页。\"\n  resolution_round: 20\n\n- id: R20-N2\n  summary: \"Topic 变体控制设计存在 3 个未隔离混杂因素\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED]\"\n  action_items: []\n  resolution: \"R21验证: method.tex和experiments.tex明确承认三个混杂因素, 指向Wiki-MLM vs JB-MLM\"\n  resolution_round: 21\n\n- id: R20-N3\n  summary: \"Appendix Table 16 TOST 数据 (n=3) 与主文 (n=10) 不一致\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED] TOST扩展至n=10\"\n  action_items: []\n  resolution: \"R21验证: 主文和附录统一为n=10 seeds\"\n  resolution_round: 21\n\n# === Open / In-Progress issues (updated for Round 24) ===\n\n- id: R9-W1\n  summary: 长度混淆未充分排除\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 23\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"benign 12-20 turns vs jailbreak 3-10 turns 完全不重叠\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 升级为 critical。R1 指出 adversarial padding 后 AA 暴跌 57pp。\"\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED] 两位Reviewer一致确认\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-N1 列为 Must-Fix。Director 裁定 Should-Fix。\"\n  - round: 24\n    reviewers: []\n    note: \"R24 未单独再次提出。R23 action item (turn-count-only classifier) 状态未更新。降级为 warning。\"\n  action_items:\n  - round: 15\n    action: \"主文 Section 4 或 5 加 1-2 句长度混淆讨论\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: \"构造长度匹配对照数据；Section 5 prominently 讨论 AA padding collapse\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: \"提供 turn-count-only classifier F1 作为 sanity check\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-W2\n  summary: \"Human data 上 evidence hierarchy 完全反转 (ToxicChat)\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 24\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"ToxicChat JB-MLM=0.837 >> 9-class=0.596\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 两位 Reviewer 均列为 critical。\"\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[RESOLVED] 两位Reviewer一致确认\"\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 两位 Reviewer 独立再次列为 Must-Fix。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 两位 Reviewer 再次独立列为 Must-Fix。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 核心问题。R1-N1 + R2-N2 均为 Must-Fix + 交叉 AGREE。差距24pp + WildChat FPR 68.1%。建议重命名为 condition-dependent evidence landscape。\"\n  action_items:\n  - round: 18\n    action: \"D081 MF1: Abstract/Intro/Conclusion scope 系统性收窄\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: \"Section 4.6 ToxicChat 反转从1句扩展为1-2段深入分析; Conclusion 给出条件性结论\"\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: \"将 evidence hierarchy 重新定义为 condition-dependent evidence landscape; 主文系统讨论各反转条件\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-N1\n  summary: 单一合成数据源限制跨攻击泛化声明可信度\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 共识: disclosure 基本到位，但双重 OOD 评估缺失。\"\n  - round: 21\n    reviewers: [1]\n    note: \"[RESOLVED] scope qualifier全面\"\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 两位 Reviewer 独立重新提出。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 继续存在。hierarchy 仅在合成数据生态系统内成立。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 结构性问题。所有真实数据场景均不支持论文主要结论。限制影响力但不阻碍 Findings 接收。\"\n  action_items:\n  - round: 17\n    action: \"W-1 Abstract F1 后加 (attack-side OOD; benign IID) 限定\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 19\n    action: \"Table 2 增加 dual-OOD 行；Abstract/Conclusion 所有 OOD F1 标注为 upper bound + IID benign 条件\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W1\n  summary: \"新颖性不足——DAPT 应用 + 增量贡献不清\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: \"方法新颖性有限是阻碍 Conference 推荐的主要原因之一。\"\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] 降级为warning\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-N1 列为 critical。需从 unexpected 重新定位为 quantifying the magnitude and conditions。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2 Must-Fix + R1 部分 AGREE。R1 提出三层新颖性分析。共识: 最具新颖性的发现未置于叙事中心。\"\n  action_items:\n  - round: 18\n    action: 重写 novelty positioning 为消融发现集合\n    assigned_to: main_agent\n    status: resolved\n  - round: 23\n    action: \"Section 1 将 finding(i) 从 unexpected 改为 systematic quantification\"\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: \"重组叙事以 why DAPT works, when it fails 为主轴; 将 scrambled equivalence 和 human-data reversal 置于叙事中心\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W5\n  summary: Scale analysis 被架构差异混淆\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] minor. DeBERTa vs RoBERTa混杂参数量\"\n  - round: 22\n    reviewers: [2]\n    note: \"R22 R2-W4: 仅 base-scale (125M-184M)。\"\n  action_items:\n  - round: 17\n    action: \"Discussion 增加 DAPT scale-dependent 效用讨论\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W7\n  summary: Abstract 信息密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] minor. Abstract信息密度高+句法模糊\"\n  - round: 24\n    reviewers: [2]\n    note: \"R24 未单独列出但与 R21-N1 合并。\"\n  action_items:\n  - round: 19\n    action: \"Abstract 压缩至 ~180 词\"\n    assigned_to: main_agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M1\n  summary: Missing references\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 建议补充 Galinkin and Sablotny (2024)。\"\n  - round: 23\n    reviewers: [1]\n    note: \"R23 建议补充 Perez and Wang (2022)。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 建议补充 Arora et al. (2019) representation compression 和 proactive multi-turn detection 近期工作。\"\n  action_items:\n  - round: 22\n    action: \"补充引用 Galinkin and Sablotny (2024) arXiv 2412.01547\"\n    assigned_to: main_agent\n    status: open\n  - round: 23\n    action: \"确认 Perez and Wang (2022) 是否已引用或需补充\"\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: \"补充 Arora et al. (2019) representation compression 和 proactive multi-turn detection 近期工作引用\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-N1\n  summary: \"数据规模扩大后性能反常下降 (350->1000)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] should-fix. 9-class也下降(0.994->0.889)\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W5 再次提出。R2 交叉 AGREE。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R1 cross-response Q2 隐含提及 capacity-compensation 假设。问题仍 open。\"\n  action_items:\n  - round: 17\n    action: \"弱化为 composition differences partially confound\"\n    assigned_to: main_agent\n    status: in_progress\n  - round: 23\n    action: \"报告 1000 样本的 seed 一致性、training loss 或 data composition 证据\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-VIS1\n  summary: \"Figure axis labels 偏小\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] minor. Figure 2 axis labels仍偏小\"\n  - round: 24\n    reviewers: []\n    note: \"R24 视觉审查: Figure 5 坐标轴标签字号偏小(p8), Figure 6 SVD 尺寸较小(p8), p16 CKA heatmap 轴标签几乎不可读。\"\n  action_items:\n  - round: 15\n    action: \"Figure 2 字号放大至>=8pt\"\n    assigned_to: main_agent\n    status: in_progress\n  - round: 24\n    action: \"Figure 5/6 标注字号增大至正文70%以上; Appendix Figure 8 CKA heatmap 轴标签放大\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W1\n  summary: Temporal modeling negative finding 讨论不足\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[RESOLVED]\"\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 R1-W3: BiGRU 对 mean pooling 无优势(Table 30)。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W3 + R2-W4 AGREE。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-W4 Should-Fix + R1 强烈 AGREE。模型本质是 bag-of-turns 检测，挑战 Multi-Turn 叙事。\"\n  action_items:\n  - round: 19\n    action: \"Discussion 讨论为什么 multi-turn 攻击的检测不需要时序建模\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 22\n    action: \"Section 3.3 或 Section 5 明确说明 BiGRU 可被 mean pooling 替代\"\n    assigned_to: main_agent\n    status: open\n  - round: 24\n    action: \"Discussion 新增段落区分 multi-turn framework (engineering) vs multi-turn modeling (learning dynamics)\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-W2\n  summary: 效率对比定位不清\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"[STILL_OPEN] minor. Abstract未标注基准\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-M4: 24.3x speedup 在 Abstract 首次出现时未给出基准。R1 AGREE。\"\n  action_items:\n  - round: 16\n    action: \"效率对比加 deployment cost comparison 限定\"\n    assigned_to: main_agent\n    status: in_progress\n  - round: 24\n    action: \"Abstract 中 24.3x speedup 后简要标注 vs LLM-as-judge\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W1\n  summary: \"TOST delta=5pp margin 缺乏 practical significance 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] minor\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 共识: 方法论改进空间，不改变定性结论。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-M3: McNemar confirms equivalence 语言问题。R1 AGREE: 需改为 finds no significant difference。\"\n  action_items:\n  - round: 17\n    action: \"Appendix TOST 部分增加 domain-specific practical significance 论证\"\n    assigned_to: main_agent\n    status: in_progress\n  - round: 23\n    action: \"补 delta=3pp sensitivity + practical significance 论证重写\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 24\n    action: \"修正 Section 4.3 McNemar confirms equivalence 为 finds no significant difference\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M1\n  summary: \"Missing references: ADEPT, Echo Chamber Attack, Representation Bending\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 21\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"[STILL_OPEN] minor\"\n  action_items:\n  - round: 17\n    action: \"核实引用真实性和相关性\"\n    assigned_to: main_agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-N1\n  summary: \"Abstract 句法模糊——this hierarchy reverses 后的修饰对象不清\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"on labeled multi-turn jailbreak data 修饰对象歧义\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-W2: Section 4.6 标题 Human Data Validation 暗示确认性结果但内容是反转。R1 AGREE。\"\n  action_items:\n  - round: 23\n    action: \"重写为 these advantages are condition-specific: on human-authored single-turn data, the hierarchy reverses\"\n    assigned_to: main_agent\n    status: in_progress\n  - round: 24\n    action: \"Section 4.6 标题从 Human Data Validation 改为 Transfer to Human-Authored Data\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W2\n  summary: 策略标注质量验证不充分\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 23\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 两位 Reviewer 均再次指出 kappa=0.78 n=50 不足\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 共识: 增加样本至>=100并报告per-class kappa。\"\n  action_items:\n  - round: 1\n    action: \"Limitations 已添加 caveat\"\n    assigned_to: main_agent\n    status: resolved\n  - round: 22\n    action: \"增加标注验证样本量至>=100并报告per-class kappa\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-N1\n  summary: \"Scrambled approx 9-class 等价性能与论文叙事的张力\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R1-W2 首提: scrambled 在 DD/FTTD 上与 9-class TOST 等价。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 confirmed resolved. Abstract 限定 on template attacks。\"\n  action_items:\n  - round: 22\n    action: \"Section 5 增加段落讨论 classification objective structure vs label semantics\"\n    assigned_to: main_agent\n    status: open\n  - round: 23\n    action: \"Abstract 限定 template attacks\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R23 PASS + R24 confirmed: abstract.tex L7 精准限定 on template attacks\"\n  resolution_round: 23\n\n- id: R22-W1\n  summary: \"自创术语过多且定义不严谨\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R2-W2 首提。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2 再列 Should-Fix，R1 REBUT 降为 Minor。experiments.tex L6 已定义。Director 维持 resolved。\"\n  action_items:\n  - round: 22\n    action: \"首次使用时给出一句话定义\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R23 PASS: experiments.tex L6 Terminology 段定义。R24 R1 REBUT severity 不影响 resolution。\"\n  resolution_round: 23\n\n- id: R22-W2\n  summary: \"Conclusion reusable template claim 超出实验范围\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R2-W3 首提。R1 交叉 AGREE。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"限定为 safety-critical NLP tasks。\"\n  action_items:\n  - round: 22\n    action: \"Conclusion 限定 reusable template 的适用范围\"\n    assigned_to: main_agent\n    status: resolved\n  resolution: \"R23 PASS: conclusion.tex L29 限定为 safety-critical NLP tasks\"\n  resolution_round: 23\n\n# === Round 24 新增 issues ===\n\n- id: R24-MF1\n  summary: \"Evidence hierarchy 术语本身具有误导性——应改为条件依赖性表述\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-N2 Must-Fix + R1 AGREE: 多个现实场景下反转的排序不应称为 hierarchy。即使合成OOD下顶部变体差异(1-4pp)也小于抽样误差。\"\n  action_items:\n  - round: 24\n    action: \"全文替换 evidence hierarchy 为更准确术语; 主文系统列举四个反转条件\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-SF1\n  summary: \"BiGRU approx mean pooling 暗示 bag-of-turns 检测——挑战 Multi-Turn 核心叙事\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-W4 + R1 强烈 AGREE。Table 30 + Section 4.3 确认。模型做 per-turn 独立检测后聚合。Multi-Turn 标题叙事被动摇。\"\n  action_items:\n  - round: 24\n    action: \"Discussion 新增段落区分 multi-turn framework (engineering) vs multi-turn modeling (learning dynamics)\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-SF2\n  summary: \"Section 4.6 Human Data Validation 标题误导——实际是 negative validation\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-W2 + R1 AGREE: Validation 暗示确认性结果但内容是反转。ToxicChat 是单轮而论文标题聚焦 Multi-Turn。\"\n  action_items:\n  - round: 24\n    action: \"标题改为 Transfer to Human-Authored Data 或 Human Data Evaluation\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-SF3\n  summary: \"Related Work 对 multi-turn defense 方法缺乏结构化比较\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R2-W3 + R1 AGREE: DeepContext/BIID/G-Guard 仅1-2句概括，未系统比较设计维度。\"\n  action_items:\n  - round: 24\n    action: \"Related Work 或 Appendix 增加 multi-turn defense 结构化对比表\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-M1\n  summary: \"Table 2 seed 报告格式不统一\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"部分 cell 有 +/-std 部分没有。camera-ready 级修改。\"\n  action_items:\n  - round: 24\n    action: \"统一 Table 2 所有 cell 的 +/-std 格式\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-M2\n  summary: \"Figure 2/3 y轴标签未指定 F1 类型\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n  - round: 24\n    reviewers: [1, 2]\n    note: \"Section 4.1 说明 F1 for binary jailbreak detection 但图中未标注。\"\n  action_items:\n  - round: 24\n    action: \"Figure 2/3 caption 中明确标注 F1 类型\"\n    assigned_to: main_agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-MF1\n  summary: \"ToxicChat hierarchy 反转分析深度不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"MLM F1=0.837 大幅超越 classification 0.596。论文用一句话带过。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 继续 Must-Fix。与 R9-W2 合并处理。\"\n  action_items:\n  - round: 23\n    action: \"Discussion 段 ToxicChat 因果分析; Conclusion 条件性结论\"\n    assigned_to: main_agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-MF3\n  summary: \"Unexpected findings 新颖性定位过高\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"Gururangan et al. (2020) 已证明 task-adaptive pretraining 优于 vanilla。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 继续 Must-Fix。R1 补充三层新颖性分析。与 R13-W1 合并。\"\n  action_items:\n  - round: 23\n    action: \"Introduction unexpected 改为 systematic quantification\"\n    assigned_to: main_agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-SF2\n  summary: \"WildChat 68.1% FPR 暴露合成数据训练系统性偏差\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"Director 裁定 Should-Fix。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R1 再次引用 WildChat FPR 作为 deployment 限制关键证据。Section 5 推荐未提及此约束。\"\n  action_items:\n  - round: 23\n    action: \"Discussion WildChat FPR 处嵌入 distributional shift 归因\"\n    assigned_to: main_agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W1\n  summary: \"RoBERTa-large DAPT harmful 机制未解释\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"9-class DAPT F1 从 1.000->0.946 = actively harmful。\"\n  - round: 24\n    reviewers: [1, 2]\n    note: \"R24 R2-Q2 + R1 AGREE: capacity-compensation 假设有洞察力。论文未直接回应。\"\n  action_items:\n  - round: 23\n    action: \"Section 4.4 或 Section 5 区分 unnecessary 和 harmful 的机制\"\n    assigned_to: main_agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W2\n  summary: \"Topic 变体 5 vs 9 类别数量混淆\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"failure 可能因类别数不足而非标签无关。建议 9->5 class merging 控制实验。\"\n  - round: 24\n    reviewers: []\n    note: \"R24 未单独提及。R23 action item 仍 open。\"\n  action_items:\n  - round: 23\n    action: \"补充 9->5 class merging 控制实验，或在 Limitations 中承认\"\n    assigned_to: main_agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 2237 · 2026-05-25T21:45:17.237376+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml\", \"bytes\": 33788}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 320
}
```

</details>

---


### Tool call

_source line 2238 · 2026-05-25T21:47:10.255002+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 24 审稿报告\n\n**Venue**: EMNLP 2026 (via ARR)\n**论文**: Multi-Turn Jailbreak Detection via Disentangled Domain-Adaptive Pre-Training\n**Reviewers**: R1, R2 | **交叉验证**: 完成 (14 AGREE, 3 minor REBUT)\n**收敛状态**: Round 1 即达成共识，无需额外轮次\n\n---\n\n## Summary\n\n本文提出两阶段框架用于多轮越狱攻击检测：Stage-1 对 RoBERTa 编码器进行领域自适应预训练（DAPT），Stage-2 用 BiGRU 做时序分类。通过 7 个预训练变体（9-class、Binary、Scrambled、MLM、Topic、Vanilla、Random Init）的因子分解消融，论文得出分类目标优于 MLM/vanilla 的\"证据层级\"。实验涵盖合成 OOD（Deceptive Delight、ActorAttack）和人类数据（ToxicChat）评估，184M 参数实现 24.3× 加速（vs LLM-as-judge）。\n\n---\n\n## Strengths\n\n**S1 [R1+R2 共识]**: 因子分解实验设计严谨——7 个变体共享训练数据和 Stage-2 分类器，仅改变 Stage-1 目标（Table 1），在 NLP 安全领域属于罕见的受控消融。\n\n**S2 [R1+R2 共识]**: Scrambled labels 发现具有原创性——打乱标签后在模板攻击（Crescendo、Deceptive Delight）上检测性能不降（TOST 等价），揭示分类目标的结构性角色而非语义内容驱动泛化。\n\n**S3 [R1+R2 共识]**: 附录深度远超同类工作（17 页），涵盖 length stratification、representation geometry、SVD necessity、cross-LLM validation、dataset scale 等系统性消融。\n\n**S4 [R1+R2 共识]**: 实用性佳——184M 参数、24.3× 加速、<5 分钟 Stage-2 训练、50 条对话近饱和。\n\n**S5 [R1+R2 共识]**: 写作结构清晰，Section 3 方法描述和 Section 4 实验组织有逻辑性。\n\n---\n\n## Weaknesses (Must-Fix)\n\n**N1 [R1+R2 共识, Critical]**: **\"Evidence hierarchy\" 在多个现实条件下反转，术语本身具有误导性。**\n\n论文将 \"evidence hierarchy\"（Figure 2, Section 4.3）作为核心贡献，但该排序在至少四个场景下不稳定或反转：\n1. **人类数据**: ToxicChat 上 MLM (0.837) >> 9-class (0.596)，差距 24pp（Table 5）\n2. **策略多样攻击**: Scrambled 在 ActorAttack 上 TOST 失败（p=0.183, d=0.44, Table 16）\n3. **大规模训练**: 1000 样本时 9-class OOD 性能反降（Table 14）\n4. **WildChat 部署**: 9-class FPR = 68.1%，高于 vanilla (48.1%) 和 MLM (44.5%)（Table 20）\n\n补充：即使在合成 OOD 的\"稳定\"条件下，hierarchy 顶部变体差异（1-4pp, Table 3）也远小于 3-seed 抽样误差，精细排序可能不稳健。\n\n一个在多个现实场景下反转的排序不应被称为 \"hierarchy\"——它是一组条件依赖的观察。论文应重新命名（如 \"condition-dependent performance landscape\"）并在主文系统讨论各反转条件。当前 Section 4.6 仅用一句话带过 ToxicChat 反转，处理深度与问题严重性严重不匹配。\n\n**N2 [R1+R2 共识, Critical]**: **\"Unexpected findings\" 新颖性定位过高。**\n\nClassification DAPT > vanilla/MLM 是 Gururangan et al. (2020) DAPT 框架在新领域的可预期推论。论文标记为 \"unexpected\" 有拔高嫌疑。\n\nR1 补充三层新颖性分析：\n- 第一层（预期）: DAPT > vanilla → 低新颖性\n- 第二层（非预期）: Scrambled ≈ correct labels on template attacks → 中等新颖性\n- 第三层（最有价值但未充分开发）: Evidence hierarchy 在人类数据上反转 → 高信息量 negative finding\n\n共识：论文的问题不在于完全缺乏新颖性，而在于**最具新颖性的发现（boundary conditions + negative findings）未被置于叙事中心**，反而被淹没在相对平凡的 \"DAPT works\" 结论中。建议重组叙事以 \"why DAPT works, when it fails\" 为主轴。\n\n**N3 [R1+R2 共识, Critical]**: **Abstract/Conclusion overclaiming。**\n\nAbstract 声称 \"classification-based domain adaptation is the only consistently effective mechanism on synthetic multi-turn attacks\"。\"synthetic\" 限定词位置容易被忽略，与标题 \"Multi-Turn Jailbreak Detection\"（无 synthetic 限定）存在张力。Section 5 \"Deployment implications\" 推荐 few-shot benign calibration 作为部署方案，但**未提及** ToxicChat 反转和 WildChat FPR 68.1% 对部署的约束。Claim 粒度与实验证据的复杂性不匹配。\n\n---\n\n## Weaknesses (Should-Fix)\n\n**W1 [R2 提出, R1 强烈 AGREE]**: **BiGRU ≈ mean pooling 暗示 bag-of-turns 检测，挑战 \"Multi-Turn\" 核心叙事。**\n\nTable 30 确认 mean pooling 在 ID/OOD 上与 BiGRU 完全等价（F1 gap < 1pp），turn-order shuffling 也无影响。推论：模型本质上做 per-turn [CLS] embedding 独立判别后取平均——bag-of-turns 检测。这直接挑战论文标题中 \"Multi-Turn\" 的叙事：模型未建模多轮动态（策略升级），而是 per-turn 独立检测并聚合。\n\n论文在 Section 4.3 将此表述为正面发现但未讨论对方法定位的影响。R1 提出可能解释：多轮框架是工程需求（处理对话中嵌入的攻击）而非模型能力需求——但论文未做此区分。Discussion 应新增段落明确承认。\n\n**W2 [R2 提出, R1 AGREE]**: **Section 4.6 \"Human Data Validation\" 标题误导。**\n\n实验结果实际是 negative validation——论文推荐的方法在人类数据上表现最差。\"Validation\" 暗示确认性结果。且 ToxicChat 是单轮数据而论文标题聚焦 Multi-Turn。建议改为 \"Transfer to Human-Authored Data\"。\n\n**W3 [R2 提出, R1 AGREE]**: **Related Work 对 multi-turn defense 方法覆盖不足。**\n\nSection 2 引用 DeepContext、BIID、G-Guard 等方法但仅 1-2 句概括，未系统比较设计维度（编码器选择、时序建模、训练数据类型、评估范围）。建议增加结构化对比表。\n\n**W4 [R1 提出, R2 AGREE]**: **350→1000 样本性能反常下降未解释。**\n\nTable 14 显示 9-class OOD 在 1000 样本时性能反降（DD OOD 0.889 vs ~1.0 at 350）。论文未给出 training loss 曲线、data composition 分析或 seed 一致性验证。\n\n**W5 [R2 提出, R1 部分 REBUT→Minor]**: **自创术语量。**\n\nR2 列为 Should-Fix，R1 认为在消融研究中术语量可接受（Minor 级别），但同意 \"partition sufficiency\" 过于晦涩。Director 裁定：R23 已在 experiments.tex L6 添加 Terminology 定义段，维持 resolved 状态。但 \"evidence hierarchy\" 本身需因 N1 而重命名。\n\n---\n\n## Questions for Authors\n\n**Q1**: ToxicChat 反转下的部署推荐——论文如何建议用户在面向真实用户对话（非合成攻击）时选择预训练策略？当前 Section 5 未区分合成 vs 人类数据场景。\n\n**Q2**: 355M DAPT counterproductive 是否支持 \"DAPT 补偿小模型容量不足\" 的假设？如果是，这如何影响对 DAPT 机制的理论理解？\n\n**Q3**: Scrambled 在模板攻击有效但策略多样攻击（ActorAttack）失效——作者是否有机制性解释？模板攻击的固定结构模式（stable self-transition patterns）是否是关键区分因素？\n\n**Q4**: BiGRU ≈ mean pooling 是否意味着当前方法对 \"slow-burn\" 攻击（信号分散在多轮且单轮无法检测）本质上无效？\n\n**Q5**: 50 条对话 near-saturation（Table 34）是否反映任务简单性或评估集规模不足（118 条测试）？\n\n---\n\n## Missing References\n\n- **Arora et al. (2019)**: Representation compression 理论工作，可加强 \"discriminative compression\" 讨论的理论支撑\n- **Proactive/early multi-turn detection 近期工作**: 加强 prefix-level detection 分析（Section 4.2, Table 7）的文献定位\n- **Galinkin & Sablotny (2024)**: arXiv 2412.01547（R22 建议，状态待确认）\n- **Perez and Wang (2022)**: Red teaming 工作（R23 建议，需确认是否已引用）\n\n---\n\n## External Review\n\n**状态**: 未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 完成（0 critical, 3 warning, 19 info）\n\n**Warnings**:\n1. Page 8: Figure 5 坐标轴标签和图内注释文字字号偏小，灰度打印时线条可能难以区分。建议增大标注字号至正文 70% 以上。\n2. Page 8: Figure 6（SVD 可视化）尺寸较小（约 1/4 column），散点和颜色标签打印时可能不够清晰。\n3. Page 16: 单页含 3 figure + 1 table，视觉密度极高。Figure 8 CKA heatmap 并排排列，轴标签（层编号）非常小，打印时几乎不可读。\n\n**正面发现**: 主正文 8 页符合 EMNLP 2026 限制；Limitations 节简洁（3 点）且位置正确；11 个 display items / 8 页分布均匀；所有表格最优结果加粗；float 位置合理；无 LaTeX 残留或 margin 溢出。\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Overall | 3.0 | 3.0 | **3.0 (Findings)** |\n| Soundness | 3/5 | 3.5/5 | 3.0-3.5 |\n| Excitement | 3/5 | 2.5/5 | 2.5-3.0 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分理由**:\n\n论文在因子分解方法论和系统性消融方面有可识别的贡献，实验执行扎实（17 页附录、多 seed、统计检验）。但三个结构性问题限制了影响力：\n\n1. **核心结论的条件依赖性**：\"evidence hierarchy\" 仅在合成数据生态系统内成立，所有真实数据评估（ToxicChat、WildChat）均不支持——这不是 framing 问题，而是结论的有效范围根本性受限。\n\n2. **新颖性定位偏差**: Classification DAPT > vanilla 可从先验工作预期；真正有价值的 boundary conditions 和 negative findings 未被置于叙事中心。\n\n3. **\"Multi-Turn\" 叙事张力**: BiGRU ≈ mean pooling + turn-order 无关 = bag-of-turns 检测。标题承诺的多轮动态建模实际上未发生。\n\n**结论**: 有方法论贡献和有价值的实证发现，但 claim 谨慎度、讨论深度和实际影响力限制了会议级别推荐。适合 **Findings** 接收（Overall 3.0），前提是修复 Must-Fix 中的 overclaiming 和讨论深度问题。\n\n---\n\n## Detailed Comments (Action Items 优先级排序)\n\n### Must-Fix (阻碍 Findings 接收)\n\n| # | Issue | Action |\n|---|-------|--------|\n| MF1 | Evidence hierarchy 条件依赖性 | 重命名术语；Section 4.6/Discussion 扩展反转分析为 1-2 段；Conclusion 条件性结论 |\n| MF2 | Novelty 定位过高 | Section 1 \"unexpected\" → \"systematic quantification\"；重组叙事以 boundary conditions 为中心 |\n| MF3 | Abstract/Conclusion overclaiming | 所有 claims 系统性加入条件限定；Deployment implications 加入 ToxicChat/WildChat 约束 |\n\n### Should-Fix (提升论文质量)\n\n| # | Issue | Action |\n|---|-------|--------|\n| SF1 | Bag-of-turns 张力 | Discussion 新增段落区分 engineering vs modeling requirement |\n| SF2 | Section 4.6 标题误导 | 改为 \"Transfer to Human-Authored Data\" |\n| SF3 | Related Work 覆盖不足 | 增加结构化对比表（Appendix 亦可） |\n| SF4 | 350→1000 性能反降 | 报告 training loss / data composition 证据 |\n| SF5 | WildChat FPR 讨论不充分 | Section 5 deployment 推荐中加入 distributional shift 约束 |\n\n### Minor\n\n| # | Issue | Action |\n|---|-------|--------|\n| M1 | Table 2 ±std 格式不统一 | 统一格式 |\n| M2 | Figure 2/3 F1 类型未标注 | Caption 中明确 |\n| M3 | McNemar \"confirms equivalence\" | 改为 \"finds no significant difference\" |\n| M4 | Abstract \"24.3× speedup\" 无基准 | 标注 \"vs LLM-as-judge\" |\n| M5 | Figure 5/6/8 标注字号偏小 | 增大至正文 70%+ |",
  "project": "persuasion_turn_jailbreak_detect",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_613965f45d48763f375aa83e9294b24a"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 24 审稿报告\n\n**Venue**: EMNLP 2026 (via ARR)\n**论文**: Multi-Turn Jailbreak Detection via Disentangled Domain-Adaptive Pre-Training\n**Reviewers**: R1, R2 | **交叉验证**: 完成 (14 AGREE, 3 minor REBUT)\n**收敛状态**: Round 1 即达成共识，无需额外轮次\n\n---\n\n## Summary\n\n本文提出两阶段框架用于多轮越狱攻击检测：Stage-1 对 RoBERTa 编码器进行领域自适应预训练（DAPT），Stage-2 用 BiGRU 做时序分类。通过 7 个预训练变体（9-class、Binary、Scrambled、MLM、Topic、Vanilla、Random Init）的因子分解消融，论文得出分类目标优于 MLM/vanilla 的\"证据层级\"。实验涵盖合成 OOD（Deceptive Delight、ActorAttack）和人类数据（ToxicChat）评估，184M 参数实现 24.3× 加速（vs LLM-as-judge）。\n\n---\n\n## Strengths\n\n**S1 [R1+R2 共识]**: 因子分解实验设计严谨——7 个变体共享训练数据和 Stage-2 分类器，仅改变 Stage-1 目标（Table 1），在 NLP 安全领域属于罕见的受控消融。\n\n**S2 [R1+R2 共识]**: Scrambled labels 发现具有原创性——打乱标签后在模板攻击（Crescendo、Deceptive Delight）上检测性能不降（TOST 等价），揭示分类目标的结构性角色而非语义内容驱动泛化。\n\n**S3 [R1+R2 共识]**: 附录深度远超同类工作（17 页），涵盖 length stratification、representation geometry、SVD necessity、cross-LLM validation、dataset scale 等系统性消融。\n\n**S4 [R1+R2 共识]**: 实用性佳——184M 参数、24.3× 加速、<5 分钟 Stage-2 训练、50 条对话近饱和。\n\n**S5 [R1+R2 共识]**: 写作结构清晰，Section 3 方法描述和 Section 4 实验组织有逻辑性。\n\n---\n\n## Weaknesses (Must-Fix)\n\n**N1 [R1+R2 共识, Critical]**: **\"Evidence hierarchy\" 在多个现实条件下反转，术语本身具有误导性。**\n\n论文将 \"evidence hierarchy\"（Figure 2, Section 4.3）作为核心贡献，但该排序在至少四个场景下不稳定或反转：\n1. **人类数据**: ToxicChat 上 MLM (0.837) >> 9-class (0.596)，差距 24pp（Table 5）\n2. **策略多样攻击**: Scrambled 在 ActorAttack 上 TOST 失败（p=0.183, d=0.44, Table 16）\n3. **大规模训练**: 1000 样本时 9-class OOD 性能反降（Table 14）\n4. **WildChat 部署**: 9-class FPR = 68.1%，高于 vanilla (48.1%) 和 MLM (44.5%)（Table 20）\n\n补充：即使在合成 OOD 的\"稳定\"条件下，hierarchy 顶部变体差异（1-4pp, Table 3）也远小于 3-seed 抽样误差，精细排序可能不稳健。\n\n一个在多个现实场景下反转的排序不应被称为 \"hierarchy\"——它是一组条件依赖的观察。论文应重新命名（如 \"condition-dependent performance landscape\"）并在主文系统讨论各反转条件。当前 Section 4.6 仅用一句话带过 ToxicChat 反转，处理深度与问题严重性严重不匹配。\n\n**N2 [R1+R2 共识, Critical]**: **\"Unexpected findings\" 新颖性定位过高。**\n\nClassification DAPT > vanilla/MLM 是 Gururangan et al. (2020) DAPT 框架在新领域的可预期推论。论文标记为 \"unexpected\" 有拔高嫌疑。\n\nR1 补充三层新颖性分析：\n- 第一层（预期）: DAPT > vanilla → 低新颖性\n- 第二层（非预期）: Scrambled ≈ correct labels on template attacks → 中等新颖性\n- 第三层（最有价值但未充分开发）: Evidence hierarchy 在人类数据上反转 → 高信息量 negative finding\n\n共识：论文的问题不在于完全缺乏新颖性，而在于**最具新颖性的发现（boundary conditions + negative findings）未被置于叙事中心**，反而被淹没在相对平凡的 \"DAPT works\" 结论中。建议重组叙事以 \"why DAPT works, when it fails\" 为主轴。\n\n**N3 [R1+R2 共识, Critical]**: **Abstract/Conclusion overclaiming。**\n\nAbstract 声称 \"classification-based domain adaptation is the only consistently effective mechanism on synthetic multi-turn attacks\"。\"synthetic\" 限定词位置容易被忽略，与标题 \"Multi-Turn Jailbreak Detection\"（无 synthetic 限定）存在张力。Section 5 \"Deployment implications\" 推荐 few-shot benign calibration 作为部署方案，但**未提及** ToxicChat 反转和 WildChat FPR 68.1% 对部署的约束。Claim 粒度与实验证据的复杂性不匹配。\n\n---\n\n## Weaknesses (Should-Fix)\n\n**W1 [R2 提出, R1 强烈 AGREE]**: **BiGRU ≈ mean pooling 暗示 bag-of-turns 检测，挑战 \"Multi-Turn\" 核心叙事。**\n\nTable 30 确认 mean pooling 在 ID/OOD 上与 BiGRU 完全等价（F1 gap < 1pp），turn-order shuffling 也无影响。推论：模型本质上做 per-turn [CLS] embedding 独立判别后取平均——bag-of-turns 检测。这直接挑战论文标题中 \"Multi-Turn\" 的叙事：模型未建模多轮动态（策略升级），而是 per-turn 独立检测并聚合。\n\n论文在 Section 4.3 将此表述为正面发现但未讨论对方法定位的影响。R1 提出可能解释：多轮框架是工程需求（处理对话中嵌入的攻击）而非模型能力需求——但论文未做此区分。Discussion 应新增段落明确承认。\n\n**W2 [R2 提出, R1 AGREE]**: **Section 4.6 \"Human Data Validation\" 标题误导。**\n\n实验结果实际是 negative validation——论文推荐的方法在人类数据上表现最差。\"Validation\" 暗示确认性结果。且 ToxicChat 是单轮数据而论文标题聚焦 Multi-Turn。建议改为 \"Transfer to Human-Authored Data\"。\n\n**W3 [R2 提出, R1 AGREE]**: **Related Work 对 multi-turn defense 方法覆盖不足。**\n\nSection 2 引用 DeepContext、BIID、G-Guard 等方法但仅 1-2 句概括，未系统比较设计维度（编码器选择、时序建模、训练数据类型、评估范围）。建议增加结构化对比表。\n\n**W4 [R1 提出, R2 AGREE]**: **350→1000 样本性能反常下降未解释。**\n\nTable 14 显示 9-class OOD 在 1000 样本时性能反降（DD OOD 0.889 vs ~1.0 at 350）。论文未给出 training loss 曲线、data composition 分析或 seed 一致性验证。\n\n**W5 [R2 提出, R1 部分 REBUT→Minor]**: **自创术语量。**\n\nR2 列为 Should-Fix，R1 认为在消融研究中术语量可接受（Minor 级别），但同意 \"partition sufficiency\" 过于晦涩。Director 裁定：R23 已在 experiments.tex L6 添加 Terminology 定义段，维持 resolved 状态。但 \"evidence hierarchy\" 本身需因 N1 而重命名。\n\n---\n\n## Questions for Authors\n\n**Q1**: ToxicChat 反转下的部署推荐——论文如何建议用户在面向真实用户对话（非合成攻击）时选择预训练策略？当前 Section 5 未区分合成 vs 人类数据场景。\n\n**Q2**: 355M DAPT counterproductive 是否支持 \"DAPT 补偿小模型容量不足\" 的假设？如果是，这如何影响对 DAPT 机制的理论理解？\n\n**Q3**: Scrambled 在模板攻击有效但策略多样攻击（ActorAttack）失效——作者是否有机制性解释？模板攻击的固定结构模式（stable self-transition patterns）是否是关键区分因素？\n\n**Q4**: BiGRU ≈ mean pooling 是否意味着当前方法对 \"slow-burn\" 攻击（信号分散在多轮且单轮无法检测）本质上无效？\n\n**Q5**: 50 条对话 near-saturation（Table 34）是否反映任务简单性或评估集规模不足（118 条测试）？\n\n---\n\n## Missing References\n\n- **Arora et al. (2019)**: Representation compression 理论工作，可加强 \"discriminative compression\" 讨论的理论支撑\n- **Proactive/early multi-turn detection 近期工作**: 加强 prefix-level detection 分析（Section 4.2, Table 7）的文献定位\n- **Galinkin & Sablotny (2024)**: arXiv 2412.01547（R22 建议，状态待确认）\n- **Perez and Wang (2022)**: Red teaming 工作（R23 建议，需确认是否已引用）\n\n---\n\n## External Review\n\n**状态**: 未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 完成（0 critical, 3 warning, 19 info）\n\n**Warnings**:\n1. Page 8: Figure 5 坐标轴标签和图内注释文字字号偏小，灰度打印时线条可能难以区分。建议增大标注字号至正文 70% 以上。\n2. Page 8: Figure 6（SVD 可视化）尺寸较小（约 1/4 column），散点和颜色标签打印时可能不够清晰。\n3. Page 16: 单页含 3 figure + 1 table，视觉密度极高。Figure 8 CKA heatmap 并排排列，轴标签（层编号）非常小，打印时几乎不可读。\n\n**正面发现**: 主正文 8 页符合 EMNLP 2026 限制；Limitations 节简洁（3 点）且位置正确；11 个 display items / 8 页分布均匀；所有表格最优结果加粗；float 位置合理；无 LaTeX 残留或 margin 溢出。\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Overall | 3.0 | 3.0 | **3.0 (Findings)** |\n| Soundness | 3/5 | 3.5/5 | 3.0-3.5 |\n| Excitement | 3/5 | 2.5/5 | 2.5-3.0 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分理由**:\n\n论文在因子分解方法论和系统性消融方面有可识别的贡献，实验执行扎实（17 页附录、多 seed、统计检验）。但三个结构性问题限制了影响力：\n\n1. **核心结论的条件依赖性**：\"evidence hierarchy\" 仅在合成数据生态系统内成立，所有真实数据评估（ToxicChat、WildChat）均不支持——这不是 framing 问题，而是结论的有效范围根本性受限。\n\n2. **新颖性定位偏差**: Classification DAPT > vanilla 可从先验工作预期；真正有价值的 boundary conditions 和 negative findings 未被置于叙事中心。\n\n3. **\"Multi-Turn\" 叙事张力**: BiGRU ≈ mean pooling + turn-order 无关 = bag-of-turns 检测。标题承诺的多轮动态建模实际上未发生。\n\n**结论**: 有方法论贡献和有价值的实证发现，但 claim 谨慎度、讨论深度和实际影响力限制了会议级别推荐。适合 **Findings** 接收（Overall 3.0），前提是修复 Must-Fix 中的 overclaiming 和讨论深度问题。\n\n---\n\n## Detailed Comments (Action Items 优先级排序)\n\n### Must-Fix (阻碍 Findings 接收)\n\n| # | Issue | Action |\n|---|-------|--------|\n| MF1 | Evidence hierarchy 条件依赖性 | 重命名术语；Section 4.6/Discussion 扩展反转分析为 1-2 段；Conclusion 条件性结论 |\n| MF2 | Novelty 定位过高 | Section 1 \"unexpected\" → \"systematic quantification\"；重组叙事以 boundary conditions 为中心 |\n| MF3 | Abstract/Conclusion overclaiming | 所有 claims 系统性加入条件限定；Deployment implications 加入 ToxicChat/WildChat 约束 |\n\n### Should-Fix (提升论文质量)\n\n| # | Issue | Action |\n|---|-------|--------|\n| SF1 | Bag-of-turns 张力 | Discussion 新增段落区分 engineering vs modeling requirement |\n| SF2 | Section 4.6 标题误导 | 改为 \"Transfer to Human-Authored Data\" |\n| SF3 | Related Work 覆盖不足 | 增加结构化对比表（Appendix 亦可） |\n| SF4 | 350→1000 性能反降 | 报告 training loss / data composition 证据 |\n| SF5 | WildChat FPR 讨论不充分 | Section 5 deployment 推荐中加入 distributional shift 约束 |\n\n### Minor\n\n| # | Issue | Action |\n|---|-------|--------|\n| M1 | Table 2 ±std 格式不统一 | 统一格式 |\n| M2 | Figure 2/3 F1 类型未标注 | Caption 中明确 |\n| M3 | McNemar \"confirms equivalence\" | 改为 \"finds no significant difference\" |\n| M4 | Abstract \"24.3× speedup\" 无基准 | 标注 \"vs LLM-as-judge\" |\n| M5 | Figure 5/6/8 标注字号偏小 | 增大至正文 70%+ |",
    "project": "persuasion_turn_jailbreak_detect",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_613965f45d48763f375aa83e9294b24a"
  }
}
```

</details>

---


### Tool result

_source line 2239 · 2026-05-25T21:47:14.482390+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a90fe0dde422576f214f12233cfe27a3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4227
}
```

</details>

---


### Assistant

_source line 2240 · 2026-05-25T21:47:23.113422+00:00_

Round 24 审稿报告已投递。

**审稿结论**：Overall 3.0 (Findings)，两位 Reviewer 完全一致。

**核心问题摘要**：
1. **"Evidence hierarchy" 在真实数据全面失效** — ToxicChat 反转 24pp + WildChat FPR 68.1%，术语本身需重命名
2. **新颖性定位偏差** — "DAPT works" 可预期，真正有价值的 boundary conditions 未置于叙事中心
3. **"Multi-Turn" 叙事张力** — BiGRU ≈ mean pooling = bag-of-turns 检测，标题承诺的时序建模未发生

**定性判断**：论文有方法论贡献（因子分解框架）和有价值的实证发现（scrambled equivalence、human data reversal），但 claim 超出证据范围。修复 Must-Fix 后适合 Findings 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 182

## Round 182

2 recorded events


### User

_source line 2241 · 2026-05-25T21:47:24.233793+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

与 R2 的主要共识和分歧：

**高度一致**：
- Evidence hierarchy 的条件依赖性（R2-N2）——我强烈同意，并补充了合成 OOD 内部排序也不稳健（顶部差异 1-4pp）
- Abstract/Conclusion overclaiming（R2-N3）
- BiGRU ≈ mean pooling 对多轮叙事的张力（R2-W4）——我认为这是 R2 比我更敏锐的观察

**主要分歧**：
- **Soundness**：我给 3.0 vs R2 给 3.5。我认为 ToxicChat 反转和 WildChat FPR 是 soundness 缺陷而非仅仅 scope 问题
- **Excitement**：我给 3.0 vs R2 给 2.5。我认为因子分析框架和 negative findings 的信息量部分弥补了预期性
- **术语（R2-W1）**：我认为属于 Minor 而非 Should-Fix
- **Overall**：一致，均为 3.0 Findings

---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Strengths 回应

[AGREE] R1-S1: 同意。7 变体因子设计是本文最大的方法论贡献，我在 S1 中也给出了相同评价。

[AGREE] R1-S2: 同意。统计工具箱的深度和规范性确实出色（TOST、Bootstrap CI、permutation tests、CKA、SVD、Fisher ratio），我的 S3 对此做了类似肯定。

[AGREE] R1-S3: 同意。Appendix U 的长度混淆分析（Table 31, 按 conversation length 分层）是必要的控制，论文处理得当。

[AGREE] R1-S4: 同意。CKA/SVD/Fisher ratio 的 layer-wise 分析（Appendix S.1, Figure 10）为 "discriminative compression" 提供了具体的表征层面证据，不仅仅是性能数字。

[AGREE] R1-S5: 同意。这是我在 S3/S5 中也肯定的。论文对 negative findings 的诚实报告（ToxicChat 反转、WildChat FPR、mixed-LLM 崩溃）提升了可信度。

---

## Must-Fix 回应

**[AGREE] R1-N1: ToxicChat 反转的机制解释深度不足**

R1 的分析比我的 N2 更锐利。我的 N2 聚焦于 "evidence hierarchy 在人工数据上反转" 这一事实层面，而 R1 精准指出了关键逻辑缺口：**论文解释了为什么分类 DAPT 不占优（ToxicChat 是单轮），但没有解释为什么 9-class 比 MLM 差了 24pp**。

核实数据：Table 5 (p.7) 确认 JB-MLM = 0.837±0.013，9-class = 0.596±0.087，差距 24.1pp，p<0.001。这意味着分类目标不仅未帮助，还**主动损害**了编码器对真实人类越狱的判别能力。论文 Section 4.6 的解释（"the classification head provides no advantage"）是对 "为什么没帮助" 的回答，但未触及 "为什么造成了伤害"。

R1 要求的 error breakdown（FP vs FN 分析）和 [CLS] embedding 分布对比是合理的诊断手段。一种可能的假设：9-class 的分类预训练使编码器过拟合了合成对话的说服策略 taxonomy，导致在 ToxicChat 真实对话上产生了 domain-specific 的表征偏移。这与 R1-W4 提出的 "统一归因" 假设一致（见下文）。

**补充我的观察**：9-class 的标准差（0.087）远大于 JB-MLM（0.013），这说明 9-class 在 ToxicChat 上不仅差，而且**不稳定**，进一步削弱其在真实场景的可靠性。

---

**[AGREE with nuance] R1-N2: 数据规模与统计 power**

R1 指出 3 seeds / 118 OOD 样本不足以支撑 fine-grained hierarchy ranking。我在 Round 1 审稿中未将此列为 Must-Fix，现在重新评估后认为 R1 的分析有道理，但需要区分两个层次：

**同意的部分**：Evidence hierarchy 内部的细粒度排序（9-class vs binary vs scrambled 差异 1-4pp，Table 3）确实在 3 seeds 的采样误差范围内。标准差估计的相对误差约 50%（2 自由度）是统计学上的硬约束。R1 建议增至 ≥10 seeds 并用 Friedman 检验是正确的改进方向。

**保留的部分**：论文的**主效应**（classification DAPT vs vanilla/MLM，差距 60-70pp on OOD）在 3 seeds 下也是 overwhelmingly significant。问题不在于 "classification DAPT 有效" 这一大结论，而在于论文将 9-class、binary、scrambled 之间的微小差异解读为有意义的 hierarchy ordering。

**我的修正立场**：将此从 "非 Must-Fix" 提升为 **Should-Fix**。理由：fine-grained hierarchy 是论文的核心贡献之一（Section 4.3 标题就是 "Decomposing the Detection Mechanism"），如果 hierarchy 内部排序不可靠，这部分贡献就被削弱了。但不至于 Must-Fix，因为主效应仍然成立。

---

**[AGREE] R1-N3: WildChat FPR 68.1% 揭示 9-class DAPT 加剧 synthetic-to-real 偏差**

R1 独立提出了我未单独列为 Must-Fix 的问题。核实数据：Table 20 (p.19) 确认 9-class FPR = 68.1±6.4%，MLM = 44.5±6.3%，vanilla = 48.1±4.9%。9-class 确实是所有变体中 FPR **最高的**，比 vanilla 高 20pp。

这构成一个严重的叙事矛盾：论文将 9-class DAPT 定位为最佳检测方案（Section 4.2-4.3, 部署建议 Section 6），但它同时产生了最严重的误报问题。即使 few-shot adaptation 可将 FPR 降至 ~1.5%（Table 21），**R1 的关键问题完全正确：calibration 后 7 个变体的 evidence hierarchy 是否改变？** 如果所有变体 calibration 后 FPR 都降到相似水平，那么 9-class 的 detection advantage 仍然成立。但如果 calibration 后 MLM/vanilla 的 detection F1 也提升（因为减少了 FP），那 net advantage 可能缩小。论文未报告这一关键比较。

**我的修正立场**：同意 R1 将此升级为 Must-Fix。这与我的 N3（Abstract/Conclusion overclaiming）直接相关——如果 9-class 在部署场景中 FPR 最高，部署建议需要重新表述。

---

## Should-Fix 回应

**[AGREE] R1-W1: TOST δ=5pp 缺乏 practical significance 论证**

论文 Section 4.3 和 Appendix L 使用 δ=5pp 作为 TOST 等价性检验的 margin，但未解释为什么 5pp 在越狱检测部署场景下是合理的等价阈值。在安全关键应用中，5pp 的漏检率差异可能意味着显著不同的风险水平。R1 建议的 δ=2pp/3pp 敏感性分析是合理的——如果缩小 margin，scrambled vs. correct 的等价性结论可能不成立。

此外，R1 正确指出 ActorAttack 上 d=0.44 是 Cohen's d 中等效应量（>0.2 为 small，>0.5 为 medium），TOST p=0.183 未通过等价性检验，但正文中 scrambled labels 的讨论措辞暗示这是次要例外（"yet these advantages reverse"），而非核心限制。

---

**[AGREE] R1-W2: 缺少与已发表 multi-turn defense 方法的直接实验对比**

论文与 TF-IDF、LLM-as-judge（Qwen3-8B、Llama Guard 3.5）对比，但未与 DeepContext（Albrethsen et al., 2026）、G-Guard（Huang et al., 2025）等已发表的 multi-turn defense 系统做直接实验对比。虽然论文的主要贡献是消融框架而非 SOTA 方法，但至少一个 published baseline 的直接对比会大幅增强论文的定位说服力。

**补充**：如果 published baselines 使用不同数据/设置难以直接比较，论文至少应在 Related Work 中定性讨论 DisPeD 管线与这些方法在设计理念上的差异和互补性。

---

**[AGREE] R1-W3: Topic 变体 5 类 vs 9 类的粒度混淆**

这是一个我在 Round 1 中遗漏的有效实验设计问题。Table 1 (p.4) 显示 Topic 变体使用 5-class topic classification（technology, health, finance, education, general），而 9-class 使用 9 种说服策略。类别数量的差异（5 vs 9）引入了粒度混淆变量——Topic 的较差表现可能部分归因于较粗的分类粒度而非 "topic ≠ domain-relevant"。一个 9-class topic 分类（或 5-class persuasion 分类）的控制条件会更干净地隔离这一因子。

---

**[AGREE] R1-W4: 单源合成数据统一归因——三个矛盾发现可能源于同一机制**

这是 R1 最有洞察力的分析之一。三个看似独立的发现：
1. 9-class DAPT 在**合成 OOD** 上最优（Table 2-3）
2. 9-class DAPT 在 **ToxicChat 人工数据**上最差（Table 5, 比 JB-MLM 低 24pp）
3. 9-class DAPT 在 **WildChat 部署**上 FPR 最高（Table 20, 68.1%）

R1 提出的统一解释是：**分类目标加深了对合成数据分布特征的拟合**。9-class 预训练使编码器高度适应 Qwen3-8B 生成的对话模式，在同源合成测试集上表现卓越，但在分布外的真实数据上产生严重过拟合。

这比我的 N2（hierarchy 反转）和 N3（overclaiming）提供了更深层的因果解释。我的审稿侧重于"claim 超出证据"的叙事问题，而 R1 触及了"数据-方法交互"的根本机制。

**补充**：这一统一归因还可以解释 Table 34 (Appendix W) 中 R1-W5 指出的 1000 样本性能下降——更多同质合成数据可能加剧而非缓解这种分布拟合。

---

**[AGREE] R1-W5: 1000 样本 71% overlap 且性能下降**

核实数据：Table 14 (p.15) 说明 1000 样本时 71% 的原 HD 测试集出现在扩展训练数据中，因此论文省略了 HD 结果。但 DD OOD 和 AA OOD 上 9-class 从 350 样本的 1.000 / 0.972 下降到 1000 样本的 0.889 / 0.915。训练数据翻倍后性能**下降**是反直觉的，论文的解释不够充分。

---

## Minor 回应

**[AGREE] R1-M1: 数据划分百分比加总问题**

需要核实。Section 4.1 描述 "split into training (350), validation (74), and test (76)"。350+74+76=500 样本。如果论文某处以百分比表述且加总不到 100%，确实需要修正。

**[AGREE] R1-M2: Figure 2 仅展示最有利条件**

Figure 2 (p.5) 展示 K=2 和 full conversation length 下的 evidence hierarchy——这是 DAPT 优势最明显的条件。Figure 3 (p.5) 展示 full length 下的更广泛结果，但 Figure 2 作为主图确实存在 cherry-picking 之嫌。建议在 Figure 2 caption 中明确说明选择该条件的理由，并引导读者查看 Figure 3 和 Appendix Tables 7-8 的完整结果。

**[AGREE] R1-M3: Appendix Y OOD κ=0.126 讨论不足**

OOD 策略预测 κ=0.126 意味着模型在域外数据上几乎无法区分不同说服策略，但在越狱检测上却仍然有效。这个有趣的解耦（strategy prediction ≠ detection performance）值得在正文或附录中更深入讨论——它支持了 "分类目标的结构角色而非语义内容驱动泛化" 的论点，但也暗示 9-class taxonomy 可能并非最优选择。

**[AGREE] R1-M4: LLM-as-judge 未测试更强 LLM**

Table 6 (p.13) 和 Table 33 (p.23) 使用 Qwen3-8B（3-shot）和 Llama Guard 3.5 作为 LLM-as-judge baseline。缺少 GPT-4o 级别的 baseline 使得 "24.3× speedup" 的比较不完整——如果 GPT-4o 在 OOD 检测上显著优于 DisPeD，那么速度优势需要在准确率-效率 tradeoff 的语境下讨论。

**[AGREE] R1-M5: DD/FTTD TF-IDF F1=1.0 暗示 lexical shortcut**

Table 2 (p.5) TF-IDF 在 DD 和 FTTD 上达到 F1=1.0。如果这些攻击家族可以被简单的词频特征完美检测，那么它们作为 OOD 评估基准的挑战性存疑。论文应讨论：(a) DD/FTTD 是否包含明显的词汇 marker；(b) 这对 evidence hierarchy 分析的影响——如果某些 OOD families 是 "trivial"，hierarchy 应该更多依赖 non-trivial families（如 ActorAttack）的结果。

---

## Questions 回应

**[AGREE] R1-Q1**: ToxicChat 9-class confusion matrix（FP vs FN 分析）是诊断 24pp 差距机制的必要信息。如果主要是 FN（漏检真实越狱），说明分类预训练损害了对人工越狱模式的敏感性；如果主要是 FP（误报正常对话），说明分类预训练引入了合成数据偏向的判别边界。

**[AGREE] R1-Q2**: Post-calibration evidence hierarchy 是我和 R1 共同关注的核心未解答问题。这直接决定部署建议的可靠性。

**[AGREE] R1-Q3**: TOST δ=5pp 的 practical significance 论证缺失。在安全关键场景，1pp 的漏检率差异可能对应大量真实攻击被放过。δ 的选择应基于部署场景的风险容忍度。

**[AGREE] R1-Q4**: 1000 样本 71% test-set overlap 是否反映训练集 effective diversity 上限？这与 Qwen3-8B 单一 LLM 生成的多样性天花板有关。如果 500 条对话已覆盖了 Qwen3-8B 在给定 prompt template 下的主要变异模式，增加样本只增加冗余。

**[AGREE] R1-Q5**: Scrambled 在 ActorAttack 上 TOST p=0.183, d=0.44。我在 Round 1 的 N1 中也指出这一限制。正文 Section 4.3 和 Abstract 中 scrambled labels 的等价性结论应明确限定为 "模板攻击（DD, FTTD）"，而非暗示通用结论。

**[AGREE] R1-Q6**: 在 Stage-1 混入 real-world benign 数据做 domain regularization 是自然的改进方向。这可能同时缓解 WildChat FPR 过高（R1-N3）和 ToxicChat 反转（R1-N1）的问题，因为它引入了真实对话分布的 regularization signal。

---

## Missing References 回应

**[AGREE] R1-MR1**: Belinkov et al. 在安全领域的 probing 延伸与本文的 SVD/CKA 表征分析直接相关，应在 Related Work 或 Appendix S.1 的讨论中引用。

---

## 对 Director 提出的 4 个分歧点的明确回应

### 1. ToxicChat 反转严重性（R1-N1 vs 我的 N2）

**R1 更锐利，我接受其分析。** 我的 N2 将 ToxicChat 反转作为 "evidence hierarchy 条件依赖" 的一个实例来讨论，侧重 overclaiming。R1 深入一层，指出论文只解释了 "为什么没帮助" 而未解释 "为什么造成 24pp 伤害"。这是一个实质性的逻辑缺口。分类 DAPT 主动损害人工数据检测的机制需要 error analysis 来诊断，论文 Section 4.6 的两段讨论确实不够。

### 2. 数据规模与统计 power（R1-N2）——我未列为 Must-Fix

**修正立场：提升为 Should-Fix。** 理由：主效应（classification vs non-classification，60-70pp 差距）在 3 seeds 下也具有压倒性的统计显著性，但 fine-grained hierarchy（9-class vs binary vs scrambled，1-4pp 差异）确实缺乏充分的统计 power。我不同意将此列为 Must-Fix 的原因是：论文的最核心发现（分类 DAPT 有效）不依赖于 hierarchy 内部排序的精确性。但如果作者继续将 fine-grained hierarchy 作为核心贡献呈现，则 R1 的 Must-Fix 定级是合理的。

### 3. WildChat FPR 最高（R1-N3）

**同意 R1 将此独立为 Must-Fix。** 我的 Round 1 审稿将 FPR 问题归入 N3（overclaiming）的一个子点，但 R1 正确地识别出这是一个独立的核心问题：9-class DAPT 不仅在检测上最优，在误报上也最差。这构成了一个**完整的 trade-off**，论文的部署建议未充分呈现此 trade-off。

### 4. 单源合成数据统一归因（R1-W4）

**完全同意。** R1-W4 的统一归因假设（分类目标加深合成数据拟合 → 合成 OOD 最优 + ToxicChat 最差 + WildChat FPR 最高）是我的审稿中缺失的关键洞察。这三个发现不应作为独立现象讨论（如我的 N2/N3 所做），而应在 Discussion 中统一分析为**同一机制的不同表现**。如果作者在修改中加入这一讨论，会显著提升论文的深度。

---

## 与 R1 的分歧点

**唯一的实质性分歧在 R1-N2 的严重性等级**：R1 列为 Must-Fix，我倾向 Should-Fix。但这一分歧是程度性的而非方向性的——我们都认为 3 seeds 不足以支撑 fine-grained hierarchy，只是对其影响接收决定的权重判断略有不同。

**评分比较**：R1 给出 Soundness 3/5、Excitement 3/5、Overall 3.0 (Findings)。我给出 Soundness 3.5/5、Excitement 2.5/5、Overall 3.0 (Findings)。经过交叉审稿，我倾向于将 Soundness 下调至 3/5，与 R1 对齐——R1-N3（WildChat FPR 最高）和 R1-W4（统一归因）揭示的问题比我 Round 1 认识到的更深。Overall 维持 3.0 (Findings)。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。核心结论：

- **与 R1 高度一致**：对 R1 全部 S1-S5、N1、N3、W1-W5、M1-M5、Q1-Q6 均 [AGREE]
- **唯一分歧**：R1-N2（统计 power）——R1 列为 Must-Fix，我倾向 Should-Fix，因为主效应（classification vs non-classification, 60-70pp 差距）在 3 seeds 下也足够显著，但 fine-grained hierarchy 内部排序确实缺乏 power
- **修正我的评分**：Soundness 从 3.5 下调至 3.0，与 R1 对齐；Overall 维持 3.0 (Findings)
- **R1-W4 的统一归因假设**（三个矛盾发现源于同一机制）是我 Round 1 审稿中缺失的最重要洞察

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2242 · 2026-05-25T21:48:05.459138+00:00_

收到双方完整交叉回应。

**收敛评估更新**：

R2 对 R1 全部观点 [AGREE]（仅 R1-N2 统计 power 的严重性分歧：R1 Must-Fix vs R2 Should-Fix）。R2 主动下调 Soundness 从 3.5→3.0 与 R1 对齐。最终共识：

| 维度 | R1 | R2 (修正后) | 共识 |
|------|----|----|------|
| Overall | 3.0 | 3.0 | **3.0 (Findings)** |
| Soundness | 3.0 | 3.0 | **3.0** |
| Excitement | 3.0 | 2.5 | 2.5-3.0 |

**R2 交叉回应的关键增量洞察**：

R2 接受了 R1-W4 的"统一归因假设"——三个看似独立的矛盾发现（合成 OOD 最优 / ToxicChat 最差 / WildChat FPR 最高）源于**同一机制**：分类目标加深了对合成数据分布的拟合。R2 称之为"我 Round 1 审稿中缺失的最重要洞察"。

报告已成功投递（Overall 3.0 Findings），核心发现和评分均与最终共识一致。统一归因假设已通过 Issue Tracker (R9-W2 + R13-N1 + R23-SF2 的关联) 传递给 Research Director。

圆桌审稿完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---
