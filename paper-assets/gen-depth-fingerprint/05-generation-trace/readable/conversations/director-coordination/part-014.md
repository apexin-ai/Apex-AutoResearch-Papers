# Director coordination — Part 14 of 14

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

[← Part 13](part-013.md) · [Transcript overview](../director-coordination.md) · [Structured JSON](../../../sessions/46/46a4a073b0cc4314da71.json)

## Round 379

### Tool call

_source line 3896 · 2026-05-23T01:37:24.097659+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 主文 8 页（不含 references 和 mandatory Limitations）\n- **模板**: ACL 2023 style（双栏，11pt）\n- **匿名规则**: Double-blind\n- **附录规则**: 允许，参与审稿\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n### 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_round_50/submitted.pdf`\n\n### 你的审查侧重\n\n**新颖性 + 完整性**，重点关注：\n\n1. **新颖性评估**：DDR（differential depth response）的科学贡献有多大？是 empirical observation 还是 methodological contribution？与 concurrent work（Geng et al. 2026 Markovian chains, Mohamed et al. 2025 broken telephone, attractor cycles）的区分是否清晰？depth profiling 作为新 task 的价值？\n2. **Framing 与 Claims**：Abstract/Introduction/Conclusion 的 claim scope 是否与实验证据匹配？\"approximately preserved\" shape features 的表述是否过度？base-model-only scope 的定位是否前置充分？F1=0.694 的实际应用意义？\n3. **Related Work 覆盖度**：AI text detection、model collapse、iterative generation、ordinal classification——四个方向的引用是否全面？是否有重要遗漏？\n4. **写作质量**：论文叙事逻辑是否清晰？术语使用是否一致（特别是 \"entropy\" 指代 NLL 的问题）？信息密度是否合适？\n5. **Limitations 充分性**：scope limitations（base-model only, ≤8B, English only, fixed decoding）是否被诚实披露？instruction tuning 失效是否被充分讨论？\n6. **Contribution-Evidence 匹配**：三个 contribution claims 与实验证据的对应是否紧密？是否有 overclaim？\n\n请给出完整的 Strengths（逐条）、Weaknesses（逐条，附严重程度 Must-Fix/Should-Fix/Minor）、Questions、Missing References，以及 Overall Assessment 评分和置信度。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 主文 8 页（不含 references 和 mandatory Limitations）\n- **模板**: ACL 2023 style（双栏，11pt）\n- **匿名规则**: Double-blind\n- **附录规则**: 允许，参与审稿\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n### 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_round_50/submitted.pdf`\n\n### 你的审查侧重\n\n**新颖性 + 完整性**，重点关注：\n\n1. **新颖性评估**：DDR（differential depth response）的科学贡献有多大？是 empirical observation 还是 methodological contribution？与 concurrent work（Geng et al. 2026 Markovian chains, Mohamed et al. 2025 broken telephone, attractor cycles）的区分是否清晰？depth profiling 作为新 task 的价值？\n2. **Framing 与 Claims**：Abstract/Introduction/Conclusion 的 claim scope 是否与实验证据匹配？\"approximately preserved\" shape features 的表述是否过度？base-model-only scope 的定位是否前置充分？F1=0.694 的实际应用意义？\n3. **Related Work 覆盖度**：AI text detection、model collapse、iterative generation、ordinal classification——四个方向的引用是否全面？是否有重要遗漏？\n4. **写作质量**：论文叙事逻辑是否清晰？术语使用是否一致（特别是 \"entropy\" 指代 NLL 的问题）？信息密度是否合适？\n5. **Limitations 充分性**：scope limitations（base-model only, ≤8B, English only, fixed decoding）是否被诚实披露？instruction tuning 失效是否被充分讨论？\n6. **Contribution-Evidence 匹配**：三个 contribution claims 与实验证据的对应是否紧密？是否有 overclaim？\n\n请给出完整的 Strengths（逐条）、Weaknesses（逐条，附严重程度 Must-Fix/Should-Fix/Minor）、Questions、Missing References，以及 Overall Assessment 评分和置信度。"
  }
}
```

</details>

---


### Tool result

_source line 3897 · 2026-05-23T01:37:25.841914+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1744
}
```

</details>

---


### Assistant

_source line 3898 · 2026-05-23T01:37:38.259197+00:00_

审稿圆桌会议已启动，当前状态：

| 组件 | 状态 |
|------|------|
| **Reviewer 1**（方法严谨性 + 实验设计） | 🔄 审稿中 |
| **Reviewer 2**（新颖性 + 完整性） | 🔄 审稿中 |
| **视觉审查 Agent** | 🔄 进行中 |
| **外部审稿** | ⏭️ 未配置，跳过 |

**Venue 确认**：EMNLP 2026 via ARR，Long paper 8 页主文限制，double-blind，ACL 2023 模板。Deadline 2026-05-25 未过期。

等待两名 Reviewer 独立审稿结果返回后，进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 380

## Round 380

2 recorded events


### User

_source line 3899 · 2026-05-23T01:45:54.969982+00:00_

[Reviewer 2 审稿意见]:

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 论文在一个有新意的任务上提供了系统性的实证分析，但核心声称（shape features "enable" cross-generator transfer）缺乏因果证据，且 base-model-only 的适用范围与论文动机（data provenance, contamination monitoring）之间存在显著脱节。

**Confidence**: 4/5 — 熟悉 AI text detection 和 model collapse 文献，对 ordinal classification 方法了解适中。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法论扎实（LOGO cross-validation、bootstrap CI、TOST equivalence testing），但 DDR 的因果解释存在过度声称 |
| Excitement | 3/5 | 任务定义新颖，但 features/classifier 均为标准方法；实际应用受限于 base-model-only 和 3-class ceiling |
| Reproducibility | 4/5 | 数据集、特征、模型配置描述详细；承诺代码公开；Pythia-410M reference model 可获取 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] Shape feature "preservation" enables cross-generator transfer 的因果声称缺乏证据
- 具体位置：Abstract ("approximately preserved: shape features provide a cross-generator reference that enables coarse ordinal depth classification"); Section 1 Contribution #2; Section 5 第2段
- 问题：论文的核心叙事是 shape features（entropy_min, tail_decay, entropy_max）因为跨深度近似不变（|d| < 0.10），所以充当跨生成器的"参考基准"，从而使得深度分类可以泛化。但多处证据与此因果链不一致：
  1. **LOFO 分析**（Table 8, Appendix f）显示 shape features 对分类的边际贡献很小（entropy_min Δ=−1.5pp, tail_decay Δ=−0.8pp, entropy_max Δ=+0.1pp），drifting features 主导分类。
  2. **Permutation Importance**（Table 42, Appendix z.3）确认：drifting 特征平均重要性 0.187 vs. near-stationary 仅 0.034。entropy_mean 排第一（0.255）。
  3. **机制未解释**：在 XGBoost 中，一个跨深度近似恒定的特征不会获得有意义的分裂节点。如果它按生成器变化但不按深度变化，XGBoost 可能将其用作生成器判别器——但这与"cross-generator reference"是完全不同的机制。
  4. **Granger causality**（Table 43）在仅 8 个生成器上做 lag=1 检验，统计功效不足以建立方向性因果。
- 为什么影响接收：这是论文的中心叙事（Abstract、Introduction、Contribution list、Discussion 均围绕此展开）。如果因果链不成立，论文的 framing 需要实质性修改。
- 建议修改方向：(a) 提供更直接的因果证据，如消融实验：人工破坏 shape features 的跨生成器一致性，观察 LOGO F1 是否特异性下降；或 (b) 将声称从因果性降级为描述性观察——"我们观察到 shape features 跨深度近似不变，且分类器在包含这些特征时泛化性能更好"，而非声称前者"使得"后者成立。

**N2** [critical] Instruction tuning 失效是最主要的实用性限制，但主文讨论不足
- 具体位置：Limitations (p.8, 仅一句话提及具体数字); Appendix k (pp.21–22, 详细分析)
- 问题：Appendix k 揭示 instruction tuning 使 3-class F1 下降 3.7–19.9pp，且 DDR 结构被根本性改变（Figure 8 显示 instruction tuning "compresses the feature-space structure underlying DDR"）。然而：
  1. 主文 Limitations 仅用一句话量化（"Llama 0.541, OLMo 0.575, Qwen 0.732"），没有讨论为什么失败。
  2. Section 5 (Discussion) 完全没有提及 instruction tuning。
  3. 论文的动机（Section 1: "data provenance, corpus auditing, contamination monitoring"）隐含假设这些场景中的 LLM 是 base models，但实际部署的 LLM 几乎全是 instruction-tuned。这造成动机与适用范围的显著脱节。
- 为什么影响接收：Reviewer 会质问：如果方法在最常见的实际场景下不适用，论文声称的应用价值如何成立？
- 建议修改方向：在 Section 4 或 Section 5 增加一个段落（~150词），量化 instruction tuning 的影响并讨论原因，同时在 Introduction 中更早地限定 scope（"base-model recursive generation"）。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Depth profiling" 的命名暗示了比实际可达到的更细粒度
- 具体位置：Title; Abstract; Section 1; Section 3.1
- 问题："Depth profiling" 暗示细粒度或连续的深度估计，但实际可达到的上限是 3-class trichotomy（gen-0, gen-1, gen-2+）。Appendix d 的 5-class 实验平均 F1 仅 0.501（Table 5），confusion matrix（Appendix g）显示 depth ≥ 2 之间严重混淆。"Depth classification" 或 "coarse depth estimation" 更准确。
- 建议：考虑在 title/abstract 中使用更精确的表述，或在 Section 3.1 前置说明分辨率上限。

**W2** [warning] "Entropy" 术语贯穿全文但实际指 reference-model NLL
- 具体位置：Table 1; 所有特征命名（entropy_mean, entropy_std, entropy_min, entropy_max）; Figure 2, 4, 5 等
- 问题：Section 3.3 和 Table 1 明确说明 "All 'entropy' features are reference-model NLL values (cross-entropy with Pythia-410M), not information-theoretic entropy"，但这一澄清仅出现一次。全文所有表格、图表、正文均使用 "entropy" 命名。information-theoretic entropy（文本自身的）与 reference-model cross-entropy 是完全不同的量。持续使用 "entropy" 可能导致读者误解特征的语义。
- 建议：将特征统一重命名为 "nll_mean" / "xent_mean"，或至少在每次首次出现时写 "reference-model entropy (NLL)"。

**W3** [warning] Contribution #2 的表述混淆了描述性观察与方法论贡献
- 具体位置：Section 1 "Our contributions" 第2条
- 问题：Contribution #2 表述为 "DDR provides a cross-generator reference that enables coarse ordinal depth classification"。但 DDR 是一个描述性的实证观察（distributional features partition into drifting vs. near-stationary groups），不是一个方法。声称它 "provides" 和 "enables" 暗示了方法论贡献，与实际的描述性贡献不匹配。
- 建议：改为 "We empirically observe that distributional features under recursive generation partition into monotonically drifting and near-stationary groups (DDR), and demonstrate this partition is robust across generators and families."

**W4** [warning] 跨 family 泛化未被显式测试
- 具体位置：Section 3.4; Table 2
- 问题：LOGO 协议按 generator 逐一 hold out，但同一 family 的多个 generator（如 Qwen3-0.6B, Qwen3-1.7B, Qwen3-3B）在训练集中保留。由于同 family 生成器共享架构和训练数据特征，LOGO F1 可能被 family-level leakage 抬高。Leave-one-family-out 评估能更严格地测试泛化能力。Appendix r/s 的 cross-family reference model 分析部分缓解了这一担忧，但没有直接测试分类性能。
- 建议：增加 leave-one-family-out 实验（至少对 Qwen 和 Llama/Pythia 家族），或讨论为什么 generator-level holdout 在此设定下已足够。

**W5** [warning] Related work 在 stylometry/authorship attribution 方向覆盖不足
- 具体位置：Section 2.3
- 问题：TTR 和 hapax ratio 是计算文体学（computational stylometry）的核心特征（Stamatatos, 2009; Koppel et al., 2009）。论文仅引用 Koppel (2009) 用于 TTR 定义，但没有讨论 depth profiling 与 authorship attribution 在方法论上的联系——两者都通过文本表面特征推断 provenance。此外，ordinal classification 是论文的一个 stated contribution，但除了 Frank-Hall 和 CORAL 之外缺乏对 ordinal regression 文献的引用。
- 建议：在 Section 2.3 或 Related Work 开头增加一段讨论 depth profiling 与 stylometric provenance 的关系。

## 小问题（不影响接收）

- Figure 1 panel (c) 在当前尺寸下难以辨认，per-generator 的 Leave-One-Out 柱状图过小。
- Section 4.2: "A feature is classified as drifting if Cohen's d > 0.20 ... or stationary if d < 0.10"——0.10 到 0.20 之间的 gap 未讨论。entropy_std（d=0.55）既不符合 drifting 也不符合 stationary 的定义，但被标为 "intermediate"。建议简要解释这个中间地带。
- Abstract 用 "approximately preserved"，主文用 "near-stationary"——建议统一术语。
- Table 3 caption 提到 "Individual detection scores (N/A) share the reference-model forward pass; per-method timing is not separately profiled"——这一重要信息应在正文而非 caption 中说明。

## Questions for Authors

**Q1.** 能否设计一个消融实验直接验证 shape features 在跨生成器泛化中的因果作用？例如，在训练集中人工打乱 shape features 的值，观察 LOGO F1 是否特异性下降？

**Q2.** 是否尝试过 leave-one-family-out 评估？如果同时 hold out 所有 Pythia 或 Qwen 模型，F1 如何变化？

**Q3.** QLoRA 达到 F1=0.905（6-gen LOGO）vs. 7-feature ensemble 的 0.789（同一设定）。在什么实际场景下用户会选择可解释但性能低 11.6pp 的方法？

**Q4.** DDR 分解在更大模型（13B, 70B）上是否成立？Limitations 提到 ≤8B 的限制，但没有讨论是否有理由预期 pattern 在更大规模下保持。

**Q5.** Instruction tuning "compresses" DDR structure（Appendix k）——如果直接在 instruction-tuned chain data 上训练分类器，信号是否能恢复？还是信号本身根本性地减弱了？

## Missing References

- Stamatatos, E. (2009). A survey of modern authorship attribution methods. *JASIST*, 60(3):538-556. — 与 depth profiling 使用的 TTR/hapax ratio 特征高度相关的基础综述。
- 如果 ordinal depth classification 是一个 stated contribution，需要更广泛地引用 ordinal regression/classification 文献。

## 主要优势

- **S1**: 任务定义新颖且有意义——从 binary human/machine 检测扩展到 ordinal depth classification 是自然且有用的推进（Section 1, Section 3.1）。
- **S2**: LOGO cross-validation 设计严谨——avoid 了在同一生成器上 train/test 的常见陷阱，bootstrap CI 提供了可靠的置信区间（Section 3.4, Table 2）。
- **S3**: 附录极其全面——28 页附录涵盖 LOFO、prompt type、finer-grained classification、QLoRA、instruction tuning、cross-domain、perturbation robustness、temperature sensitivity、decoding strategy、9-generator scaling、UMAP、confusion matrix、Granger causality 等。实验覆盖度在 empirical study 中属于上乘。
- **S4**: DDR 分解提供了可解释的分析框架——将特征分为 drifting 和 near-stationary 两组，并用 Cohen's d、TOST equivalence testing（Appendix t）、bootstrap stability（Appendix u）进行统计刻画。
- **S5**: 对 limitations 的诚实报告——base-model-only scope、instruction tuning 失败、3-class ceiling、English-only、fixed decoding 均被明确披露（Limitations section, p.8-9）。
- **S6**: 与 concurrent work 的对比清晰——Table 48（Appendix z.7）将本文与 Mohamed et al. (2025) 和 Geng et al. (2026) 进行了详细的维度对比。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3900 · 2026-05-23T01:46:02.680604+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 381

## Round 381

2 recorded events


### User

_source line 3901 · 2026-05-23T01:46:06.973024+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：评分 **Overall 3.5（Borderline Conference）**。两个 Must-Fix 问题：(1) shape feature "preservation" enables cross-generator transfer 的因果声称缺乏直接证据——LOFO 和 permutation importance 均显示 drifting features 主导分类，shape features 边际贡献小，声称的因果机制在 XGBoost 框架下缺乏解释；(2) instruction tuning 导致方法失效是最重要的实用性限制，但主文几乎未讨论，与 Introduction 中"data provenance / contamination monitoring"的动机形成显著脱节。五个 Should-Fix 涵盖命名精度（"depth profiling" 暗示过细粒度）、"entropy" 术语误导、contribution 表述、family-level 泛化未测试、stylometry related work 覆盖不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3902 · 2026-05-23T01:46:13.276552+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成独立初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 382

## Round 382

6 recorded events


### User

_source line 3903 · 2026-05-23T01:46:57.320791+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 新颖的深度分析问题定义与详尽的DDR框架验证值得肯定，但gen-0种子共享导致的LOGO评估泄漏、TOST等价边界缺乏任务特异性校准、以及中等水平的二分类性能（F1=0.694）共同削弱了核心方法论声明的可信度。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心方法论合理且有大量控制实验，但gen-0泄漏影响主要指标、TOST边界缺乏任务校准、部分统计断言需加强 |
| Excitement | 3.5/5 | 深度分析（超越二分类检测）是新颖且有实用价值的方向，但限于base模型、性能中等、实际应用场景论证不足 |
| Reproducibility | 4/5 | 实验细节充分（超参数、数据集规模、特征定义均有交代），承诺开源代码和数据 |
| Confidence | 4/5 | 仔细阅读全文及全部附录，逐项验证统计声明 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Gen-0 种子共享在 LOGO 评估中造成 train-test 信息泄漏，主指标 3-class F1=0.762 被高估

- **具体位置**: Section 3.2 (p4), Table 2 (p5/6), Appendix i confusion matrix (p23)
- **问题**: 论文使用 ~1,000 条共享 Wikipedia 种子跨全部8个生成器（Section 3.2: "We use shared seeds across generators so that cross-generator comparisons control for input content"）。在 LOGO 中，被hold-out生成器的 gen-0 样本与训练集中其他生成器的 gen-0 样本具有**完全相同的文本和特征向量**（因为 gen-0 就是原始种子文本本身）。这构成了事实上的 train-test 重叠。Appendix i 报告 gen-0 分类准确率高达 99.4%——虽然人类文本本身确实容易与机器文本区分，但这一近乎完美的数字中有多少来自泄漏、多少来自真实可泛化信号无法从当前实验设计中剥离。
- **影响程度估算**: Gen-0 约占 3-class 测试集的 1/3。假设无泄漏时 gen-0 F1 从 ~1.0 降至 ~0.92（仍然很高），macro F1 将从 0.762 降至约 0.73。这意味着主指标可能被高估约 3pp。而论文在摘要和引言中反复引用 3-class F1=0.762 作为核心结果。
- **现有缓解措施**: 论文在 Section 4.1 提供了排除 gen-0 的 binary F1=0.694（p5），Appendix t 提供了独立种子评估 F1=0.680（p27），但这些均为次要指标。
- **建议修改方向**: (a) 以排除 gen-0 的 binary F1 作为主指标，或 (b) 补充不同生成器使用**不相交种子池**的 3-class LOGO 评估，或 (c) 至少在报告 3-class F1 时明确注明 gen-0 泄漏上界并讨论其影响幅度。

---

**N2** [critical] DDR 核心声明"drifting vs. near-stationary"的分界依赖数据后验观察，缺乏预注册或前置理论驱动

- **具体位置**: Section 4.2 (p6-7), Figure 4 (p7), Appendix v (p28-29)
- **问题**: DDR 分区（drifting: {entropy_mean, TTR, hapax_ratio} vs. near-stationary: {entropy_max, entropy_min, tail_decay}）是通过观察7个特征在 (|ρ|, d) 空间中的分布后**事后定义**的。论文首先计算了所有特征的 Spearman ρ 和 Cohen's d，观察到 drifting 组 |ρ|>0.60 vs. near-stationary |d|<0.10 之间存在"六倍量级差距"（p7），然后将此差距定义为 DDR 分区。
  
  k-means 验证（Appendix v, p28: silhouette=0.660）使用的是**定义 DDR 的同一批特征和同一组数据**——这实质上是在验证数据中确实存在聚类结构，而非验证 DDR 的分类学意义。这是一种弱循环：事后观察 gap → 定义分区 → 用同一数据的 k-means 验证存在 gap。

- **缓解因素**: 论文在 Table 35 (p30) 提供了 holdout generator split validation（将8个生成器分为 selection 4 + validation 4），最大 Δ(d) 仅为 0.05，这是一个有效的外部验证。但这一关键验证被埋在附录深处，主文未提及。
- **影响**: 如果 DDR 分区是论文的核心贡献（Section 5 将其描述为"an empirical regularity of base-model autoregressive generation"），那么分区定义的方法论严谨性直接影响这一贡献的可信度。
- **建议**: (a) 将 holdout generator split validation 提升至主文，作为 DDR 验证的核心证据；(b) 补充一个"盲测"实验：在一组生成器上定义 DDR，在完全独立的新生成器上验证分区是否成立；(c) 讨论 entropy_std 作为 intermediate 特征（|d|=0.53, |ρ|=0.16）对 binary partition 的挑战。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] TOST 等价性检验的边界 (|d|≤0.20) 采用通用社会科学惯例，缺乏任务特异性校准

- **具体位置**: Appendix u (p28-29), Table 33 (p29)
- **问题**: TOST 用于验证 near-stationary 特征在深度间"实际不可区分"，等价边界 ε=0.20 取自 Cohen (1988) 的"小效应"阈值。但 d=0.19 的效应在此分类任务中是否真的"可忽略"并无任务内证据。社会科学中的"小效应"与 NLP 分类任务中的"无判别力"不是同一概念。
- **论文中的隐含证据**: LOFO 分析（Appendix f, Table 8, p16）显示移除任何 near-stationary 特征对 F1 的影响 Δ ≤ -1.5pp，间接支持 d<0.20 特征确实缺乏分类价值。但论文未显式将 LOFO 结果与 TOST 边界选择联系起来。
- **建议**: (a) 在 TOST 讨论中显式引用 LOFO 结果作为任务内校准证据；(b) 补充一个分析：将 TOST 边界从 0.10 到 0.50 变动时，DDR 分区和下游 F1 如何变化（论文在 Table 34 做了分区稳定性，但未连接到分类性能）。

**W2** [warning] QLoRA 与 XGBoost 的比较在不同生成器子集上进行，结论可移植性受限

- **具体位置**: Appendix e (p16), Table 7
- **问题**: QLoRA 使用 6-gen LOGO（原始6个生成器子集），主文 XGBoost 使用 8-gen LOGO。QLoRA 的 F1=0.905 vs. 同子集 XGBoost F1=0.789，看似大幅提升。但 6-gen 子集不含后加入的 Llama-3.2-3B 和 Mistral-7B-v0.3——这两个是唯一的 >3B 模型。论文脚注标注"Not directly comparable"，但正文多处（如 Limitations, p8-9: "QLoRA binary F1=0.487"）引用 QLoRA 数字时未同步提醒读者比较基础不同。
- **建议**: 在全部8个生成器上运行 QLoRA LOGO 评估，或在引用 QLoRA 数字时始终明确标注生成器子集差异。

**W3** [warning] 提出的方法在 3-class F1 上低于最强 baseline（4-det+surface），但主文未充分讨论

- **具体位置**: Table 3 (p8), Section 4.3
- **问题**: Table 3 显示 4-det+surface ensemble（6特征）的 3-class F1=0.798，高于论文的 7-feature ensemble 的 0.762（差距 3.6pp）。在 binary F1 上差距缩小至 1.4pp（0.708 vs 0.694）。论文在 Section 4.3 的讨论中聚焦 binary 比较（"matches the 4-detector+surface ensemble"），对 3-class 的劣势轻描淡写。
- **影响**: 如果核心贡献是"可解释的 DDR 分解"而非"更优的分类性能"，应明确重新定位 contribution。当前写法容易让读者误以为方法在分类性能上也有优势。
- **建议**: 在 Section 4.3 或 Discussion 中坦诚讨论 3-class F1 差距，并将 contribution 明确定位为"以更少的外部模型依赖（单个 Pythia-410M）实现可比性能 + DDR 可解释性"。

**W4** [warning] Bootstrap CI 的重采样单位是文本级别，可能低估生成器级泛化不确定性

- **具体位置**: Section 4.1 (p5: "95% bootstrap CIs (n=1,000)")
- **问题**: 论文报告的 95% bootstrap CI（如 Table 2 中的 CI）似乎在文本级别重采样。但 LOGO 评估的核心关切是**跨生成器泛化**——应在生成器级别量化不确定性。8个 LOGO fold 产生8个 F1 值，其均值和标准差才是生成器级泛化的合理估计。文本级 bootstrap CI 可能显著窄于生成器级 CI，给人过高的置信度。
- **缓解因素**: LOGO 本身通过 leave-one-out 已隐式捕捉生成器间变异（Table 2 报告了 per-generator F1）。但 bootstrap CI 和 LOGO 变异度的关系未被讨论。
- **建议**: 报告 LOGO fold 级别的均值±标准差作为生成器级泛化不确定性的主要度量，或在文本级 bootstrap CI 旁附加 LOGO fold 级别的 CI。

**W5** [warning] Entropy_std 的"intermediate"地位（|d|=0.53, |ρ|=0.16）挑战 DDR 的 binary partition 叙事

- **具体位置**: Section 4.2 (p7), Appendix v (p28)
- **问题**: DDR 被呈现为 drifting vs. near-stationary 的二元分区，但 entropy_std 在 Cohen's d 维度上处于两组之间（|d|=0.53 vs. drifting |d|≥0.60, near-stationary |d|<0.10）。论文在 p7 承认其为"intermediate"，Appendix v 中 k=3 的 k-means 结果也支持三组结构。但主文仍以二元分区为叙事主线，entropy_std 的定位不清晰——它在最终分类中是与 drifting 还是 near-stationary 一组？
- **影响**: 这不影响分类性能（所有7个特征都被使用），但影响 DDR 作为分析框架的清晰度。
- **建议**: (a) 主文中明确 entropy_std 被归入哪组以及理由（是因为 |ρ| 低所以归入 near-stationary 还是单独列为 intermediate？），或 (b) 将 DDR 呈现为三组分区（drifting / intermediate / near-stationary）。

---

## 小问题（不影响接收）

- **M1**: Table 1 (p4) 的特征来源标注为 "Ref. NLL" 和 "Surface"，但正文中有时将 entropy 特征描述为"distributional features"而非"reference-model NLL features"——第一次出现时应统一术语，避免歧义。
- **M2**: Figure 4 caption (p7) 中 "|d|≥0.60, |ρ|≥0.76-1.17" 与正文 "drifting features show |ρ|>0.60" 的阈值表述不一致——Figure 4 caption 的 |ρ| 范围是实际观察值而非阈值定义，建议明确区分。
- **M3**: Section 3.2 (p4) 提到 "We generate up to depth 4 to empirically confirm convergence"，但 3-class 评估将 depth 2-4 合并为 gen-2+。为何不报告 5-class 评估作为主结果？Appendix d (p15) 的 5-class 评估显示 average F1 仅 0.521——这一较低数字放在主文中可能更诚实地反映方法的局限。
- **M4**: Limitations (p8-9) 提到 "perturbation robustness (Appendix i) tests only random word replacement"——这确实是一个显著局限。Paraphrase attacks（如用 T5/GPT 重写）是更现实的对抗场景，建议至少讨论。
- **M5**: Bonferroni 校正的"family"边界未明确定义（p5: "within each family of simultaneous tests"）。应说明具体的 family 划分策略。

---

## Questions to Authors

1. **Gen-0 泄漏量化**: 能否提供使用**不相交种子池**（不同生成器用不同 Wikipedia passages）的 3-class LOGO F1？这将直接量化 gen-0 泄漏对主指标的影响。
2. **TOST 与 LOFO 的联系**: LOFO 表明移除任何 near-stationary 特征的 F1 变化 ≤ -1.5pp。这是否意味着 near-stationary 特征在分类中确实无贡献？如果是，为何将它们保留在特征集中？
3. **Baseline 公平性**: 4-det+surface baseline 使用4个不同的参考模型（AvgLogProb, FastDetectGPT, Binoculars, LD-Score 各用自己的 reference），而论文方法仅用 Pythia-410M。如果给 baseline 方法也限制为单一 Pythia-410M reference，其性能如何变化？
4. **Instruction-tuned 模型**: Appendix k (p21-22) 显示 instruction tuning 使特征空间发生压缩但深度信号持续存在。这些实验用了多少个 instruction-tuned 模型？泛化性如何？
5. **5-class 性能**: 为何不将 5-class 分类（区分 gen-0/1/2/3/4）作为主评估之一？当前 5-class F1=0.521 似乎表明方法对精细深度区分能力有限。

---

## Missing References

- Uchendu et al., 2020, "Authorship Attribution for Neural Text Generation" — 相关的 authorship attribution for machine text
- Krishna et al., 2024, "Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense" — 论文提到但在 robustness 讨论中未充分对比的 paraphrase attack 方法

（注：论文引用基本全面，上述仅为可选补充。）

---

## 主要优势

1. **问题定义新颖且有意义**: 从二分类（human vs. machine）扩展到序数深度分类（gen-0/1/2+）是检测领域的自然且重要的延伸，对数据溯源、语料审计、模型坍塌监控具有直接应用价值。
2. **DDR 分解提供了真实的机制洞见**: location drift（entropy mean, TTR, hapax ratio 单调下降）vs. shape stability（entropy std/max/min, tail decay 保持稳定）的分解不仅是分类方法，也是对递归生成如何改变文本分布的理论贡献。
3. **实验覆盖面广且控制严格**: 8个生成器×5个架构家族×LOGO 交叉验证 + 长度控制（Appendix b）+ 独立种子验证（Appendix t）+ 参考模型鲁棒性（Appendix s）+ 交叉温度迁移（Appendix p）+ 交叉域验证（Appendix j）+ QLoRA 端到端验证（Appendix e）+ 扰动鲁棒性（Appendix i）——实验深度在 empirical study 中属于上乘。
4. **轻量级且可部署**: 仅需单个小型参考模型（Pythia-410M, 410M参数）和7个可解释标量特征，无需 GPU 推理或专用检测器，具备实际部署可行性。
5. **附录质量高**: 28页附录包含详尽的消融分析、混淆矩阵、TOST 验证、特征收敛动态、UMAP 可视化等——表明作者对自身方法的局限有深入认识。
6. **写作质量整体良好**: 叙事从问题定义→方法→DDR分析→对比的逻辑线清晰，Figure 1 信息密度高，Figure 4 有效传达 DDR 分区的核心洞见。

---

## 页面合规性
主文（Sections 1-6）在第8页结束，Limitations 从第8页底部开始延伸至第9页。按 EMNLP 2026 规则（mandatory Limitations 不计入8页限制），**格式合规**。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 3904 · 2026-05-23T01:47:35.784777+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个 Must-Fix、Should-Fix、Minor 问题，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 新颖的深度分析问题定义与详尽的DDR框架验证值得肯定，但gen-0种子共享导致的LOGO评估泄漏、TOST等价边界缺乏任务特异性校准、以及中等水平的二分类性能（F1=0.694）共同削弱了核心方法论声明的可信度。\n\n## Must-Fix 问题\n\n**N1** [critical] Gen-0 种子共享在 LOGO 评估中造成 train-test 信息泄漏，主指标 3-class F1=0.762 被高估\n- Section 3.2 (p4), Table 2 (p5/6), Appendix i confusion matrix (p23)\n- 论文使用 ~1,000 条共享 Wikipedia 种子跨全部8个生成器。在 LOGO 中，被hold-out生成器的 gen-0 样本与训练集中其他生成器的 gen-0 样本具有完全相同的文本和特征向量。这构成了事实上的 train-test 重叠。\n- Gen-0 约占 3-class 测试集的 1/3。假设无泄漏时 gen-0 F1 从 ~1.0 降至 ~0.92，macro F1 将从 0.762 降至约 0.73。主指标可能被高估约 3pp。\n- 建议：以排除 gen-0 的 binary F1 作为主指标，或补充不相交种子池的 3-class LOGO 评估。\n\n**N2** [critical] DDR 核心声明\"drifting vs. near-stationary\"的分界依赖数据后验观察，缺乏预注册或前置理论驱动\n- Section 4.2 (p6-7), Figure 4 (p7), Appendix v (p28-29)\n- DDR 分区是通过观察7个特征在 (|ρ|, d) 空间中的分布后事后定义的。k-means 验证使用的是定义 DDR 的同一批特征和同一组数据——弱循环。\n- 缓解因素：Table 35 (p30) 提供了 holdout generator split validation（selection 4 + validation 4），最大 Δ(d) 仅为 0.05，但被埋在附录深处。\n- 建议：将 holdout generator split validation 提升至主文；补充\"盲测\"实验。\n\n## Should-Fix 问题\n\n**W1** TOST 等价性检验的边界 (|d|≤0.20) 采用通用社会科学惯例，缺乏任务特异性校准\n**W2** QLoRA 与 XGBoost 的比较在不同生成器子集上进行，结论可移植性受限\n**W3** 提出的方法在 3-class F1 上低于最强 baseline（4-det+surface 0.798 vs 0.762），但主文未充分讨论\n**W4** Bootstrap CI 的重采样单位是文本级别，可能低估生成器级泛化不确定性\n**W5** Entropy_std 的\"intermediate\"地位（|d|=0.53, |ρ|=0.16）挑战 DDR 的 binary partition 叙事\n\n## 主要优势\n1. 问题定义新颖且有意义\n2. DDR 分解提供了真实的机制洞见\n3. 实验覆盖面广且控制严格\n4. 轻量级且可部署\n5. 附录质量高\n6. 写作质量整体良好\n\n---\n\n请对 R1 的每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个 Must-Fix、Should-Fix、Minor 问题，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 新颖的深度分析问题定义与详尽的DDR框架验证值得肯定，但gen-0种子共享导致的LOGO评估泄漏、TOST等价边界缺乏任务特异性校准、以及中等水平的二分类性能（F1=0.694）共同削弱了核心方法论声明的可信度。\n\n## Must-Fix 问题\n\n**N1** [critical] Gen-0 种子共享在 LOGO 评估中造成 train-test 信息泄漏，主指标 3-class F1=0.762 被高估\n- Section 3.2 (p4), Table 2 (p5/6), Appendix i confusion matrix (p23)\n- 论文使用 ~1,000 条共享 Wikipedia 种子跨全部8个生成器。在 LOGO 中，被hold-out生成器的 gen-0 样本与训练集中其他生成器的 gen-0 样本具有完全相同的文本和特征向量。这构成了事实上的 train-test 重叠。\n- Gen-0 约占 3-class 测试集的 1/3。假设无泄漏时 gen-0 F1 从 ~1.0 降至 ~0.92，macro F1 将从 0.762 降至约 0.73。主指标可能被高估约 3pp。\n- 建议：以排除 gen-0 的 binary F1 作为主指标，或补充不相交种子池的 3-class LOGO 评估。\n\n**N2** [critical] DDR 核心声明\"drifting vs. near-stationary\"的分界依赖数据后验观察，缺乏预注册或前置理论驱动\n- Section 4.2 (p6-7), Figure 4 (p7), Appendix v (p28-29)\n- DDR 分区是通过观察7个特征在 (|ρ|, d) 空间中的分布后事后定义的。k-means 验证使用的是定义 DDR 的同一批特征和同一组数据——弱循环。\n- 缓解因素：Table 35 (p30) 提供了 holdout generator split validation（selection 4 + validation 4），最大 Δ(d) 仅为 0.05，但被埋在附录深处。\n- 建议：将 holdout generator split validation 提升至主文；补充\"盲测\"实验。\n\n## Should-Fix 问题\n\n**W1** TOST 等价性检验的边界 (|d|≤0.20) 采用通用社会科学惯例，缺乏任务特异性校准\n**W2** QLoRA 与 XGBoost 的比较在不同生成器子集上进行，结论可移植性受限\n**W3** 提出的方法在 3-class F1 上低于最强 baseline（4-det+surface 0.798 vs 0.762），但主文未充分讨论\n**W4** Bootstrap CI 的重采样单位是文本级别，可能低估生成器级泛化不确定性\n**W5** Entropy_std 的\"intermediate\"地位（|d|=0.53, |ρ|=0.16）挑战 DDR 的 binary partition 叙事\n\n## 主要优势\n1. 问题定义新颖且有意义\n2. DDR 分解提供了真实的机制洞见\n3. 实验覆盖面广且控制严格\n4. 轻量级且可部署\n5. 附录质量高\n6. 写作质量整体良好\n\n---\n\n请对 R1 的每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 3905 · 2026-05-23T01:48:00.102622+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24317
}
```

</details>

---


### Tool call

_source line 3906 · 2026-05-23T01:48:00.303643+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每个 Must-Fix、Should-Fix、Minor 问题，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 论文在一个有新意的任务上提供了系统性的实证分析，但核心声称（shape features \"enable\" cross-generator transfer）缺乏因果证据，且 base-model-only 的适用范围与论文动机（data provenance, contamination monitoring）之间存在显著脱节。\n\n## Must-Fix 问题\n\n**N1** [critical] Shape feature \"preservation\" enables cross-generator transfer 的因果声称缺乏证据\n- Abstract (\"approximately preserved: shape features provide a cross-generator reference that enables coarse ordinal depth classification\"); Section 1 Contribution #2; Section 5 第2段\n- LOFO 分析显示 shape features 对分类的边际贡献很小（entropy_min Δ=−1.5pp, tail_decay Δ=−0.8pp, entropy_max Δ=+0.1pp），drifting features 主导分类。\n- Permutation Importance 确认 drifting 特征平均重要性 0.187 vs. near-stationary 仅 0.034。\n- 在 XGBoost 中，一个跨深度近似恒定的特征不会获得有意义的分裂节点。如果它按生成器变化但不按深度变化，XGBoost 可能将其用作生成器判别器——但这与\"cross-generator reference\"是完全不同的机制。\n- 建议：提供消融实验直接验证因果关系，或将声称从因果性降级为描述性观察。\n\n**N2** [critical] Instruction tuning 失效是最主要的实用性限制，但主文讨论不足\n- Appendix k 揭示 instruction tuning 使 3-class F1 下降 3.7–19.9pp，DDR 结构被根本性改变。\n- 主文 Limitations 仅用一句话量化。Section 5 (Discussion) 完全没有提及。\n- 论文动机（\"data provenance, corpus auditing, contamination monitoring\"）隐含假设 LLM 是 base models，但实际部署几乎全是 instruction-tuned。\n- 建议：Section 4 或 Section 5 增加一个段落讨论 instruction tuning 影响。\n\n## Should-Fix 问题\n\n**W1** \"Depth profiling\" 命名暗示比实际可达到的更细粒度\n**W2** \"Entropy\" 术语贯穿全文但实际指 reference-model NLL\n**W3** Contribution #2 的表述混淆了描述性观察与方法论贡献\n**W4** 跨 family 泛化未被显式测试（LOGO 按 generator hold out，同 family 保留）\n**W5** Related work 在 stylometry/authorship attribution 方向覆盖不足\n\n## 主要优势\n1. 任务定义新颖且有意义\n2. LOGO cross-validation 设计严谨\n3. 附录极其全面\n4. DDR 分解提供可解释的分析框架\n5. 对 limitations 的诚实报告\n6. 与 concurrent work 的对比清晰\n\n---\n\n请对 R2 的每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每个 Must-Fix、Should-Fix、Minor 问题，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 论文在一个有新意的任务上提供了系统性的实证分析，但核心声称（shape features \"enable\" cross-generator transfer）缺乏因果证据，且 base-model-only 的适用范围与论文动机（data provenance, contamination monitoring）之间存在显著脱节。\n\n## Must-Fix 问题\n\n**N1** [critical] Shape feature \"preservation\" enables cross-generator transfer 的因果声称缺乏证据\n- Abstract (\"approximately preserved: shape features provide a cross-generator reference that enables coarse ordinal depth classification\"); Section 1 Contribution #2; Section 5 第2段\n- LOFO 分析显示 shape features 对分类的边际贡献很小（entropy_min Δ=−1.5pp, tail_decay Δ=−0.8pp, entropy_max Δ=+0.1pp），drifting features 主导分类。\n- Permutation Importance 确认 drifting 特征平均重要性 0.187 vs. near-stationary 仅 0.034。\n- 在 XGBoost 中，一个跨深度近似恒定的特征不会获得有意义的分裂节点。如果它按生成器变化但不按深度变化，XGBoost 可能将其用作生成器判别器——但这与\"cross-generator reference\"是完全不同的机制。\n- 建议：提供消融实验直接验证因果关系，或将声称从因果性降级为描述性观察。\n\n**N2** [critical] Instruction tuning 失效是最主要的实用性限制，但主文讨论不足\n- Appendix k 揭示 instruction tuning 使 3-class F1 下降 3.7–19.9pp，DDR 结构被根本性改变。\n- 主文 Limitations 仅用一句话量化。Section 5 (Discussion) 完全没有提及。\n- 论文动机（\"data provenance, corpus auditing, contamination monitoring\"）隐含假设 LLM 是 base models，但实际部署几乎全是 instruction-tuned。\n- 建议：Section 4 或 Section 5 增加一个段落讨论 instruction tuning 影响。\n\n## Should-Fix 问题\n\n**W1** \"Depth profiling\" 命名暗示比实际可达到的更细粒度\n**W2** \"Entropy\" 术语贯穿全文但实际指 reference-model NLL\n**W3** Contribution #2 的表述混淆了描述性观察与方法论贡献\n**W4** 跨 family 泛化未被显式测试（LOGO 按 generator hold out，同 family 保留）\n**W5** Related work 在 stylometry/authorship attribution 方向覆盖不足\n\n## 主要优势\n1. 任务定义新颖且有意义\n2. LOGO cross-validation 设计严谨\n3. 附录极其全面\n4. DDR 分解提供可解释的分析框架\n5. 对 limitations 的诚实报告\n6. 与 concurrent work 的对比清晰\n\n---\n\n请对 R2 的每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 3907 · 2026-05-23T01:48:01.711308+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1407
}
```

</details>

---


### Assistant

_source line 3908 · 2026-05-23T01:48:10.905564+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 383

## Round 383

2 recorded events


### User

_source line 3909 · 2026-05-23T01:48:13.528061+00:00_

[Reviewer 1 审稿结果]:
审稿完成。已向 Review Director 提交完整审稿报告，核心结论：

- **Overall: 3.5 (Borderline Conference)**
- **2个 Must-Fix**: (1) gen-0 种子共享导致 LOGO 评估中 train-test 泄漏，主指标 3-class F1=0.762 被高估约 3pp；(2) DDR 分区的事后定义缺乏前置理论驱动，k-means 验证存在弱循环性（holdout generator split validation 有效但被埋在附录中）
- **5个 Should-Fix**: TOST 边界缺乏任务校准、QLoRA/XGBoost 比较基础不一致、3-class F1 低于最强 baseline 但未充分讨论、bootstrap CI 重采样层级问题、entropy_std 的 intermediate 地位挑战二元分区叙事
- **主要优势**: 问题定义新颖、DDR 分解有机制洞见、实验覆盖面广（8生成器×5家族+大量控制实验）、轻量级可部署、附录质量高

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3910 · 2026-05-23T01:48:17.878831+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 384

## Round 384

2 recorded events


### User

_source line 3911 · 2026-05-23T01:49:55.974840+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R2-N1: Shape feature "enables" cross-generator transfer 的因果声称缺乏证据**

同意这是一个实质性问题。论文 Abstract 明确写道 "shape features provide a cross-generator reference that enables coarse ordinal depth classification"——这是一个因果声明。但 LOFO 分析（Appendix f, Table 8/9, p16-17）的证据与此矛盾：

- 移除任何 near-stationary 特征对 F1 的影响极小（entropy_min Δ=−1.5pp, tail_decay Δ=−0.8pp, entropy_max Δ=+0.1pp）
- 仅用 drifting 特征子集 {entropy_mean, entropy_max} 即可达到全集 88% 的性能（Table 9, F1=0.685）
- Permutation Importance 中 near-stationary 特征平均重要性仅为 drifting 的 18%（0.034 vs. 0.187）

R2 关于 XGBoost 机制的分析也正确：如果 shape features 跨深度近似恒定，它们在 tree split 中不会被用于深度判别。如果它们按生成器变化，XGBoost 反而会将其用作生成器识别器——这与"cross-generator reference"是相反的机制。

**我的补充**: 论文可能想表达的是 shape features 的稳定性作为一种**归纳偏置**（inductive bias），让分类器学到的决策边界更多依赖 drifting 特征的深度信号而非 generator-specific noise。但这个论点未被显式提出或验证。要验证这一假设，需要一个消融实验：仅用 3 个 drifting 特征训练 vs. 全部 7 个特征训练的 LOGO F1 对比。如果 3-feature 模型性能相当甚至更好，shape features 的"enabling"作用就不成立。

---

**[AGREE] R2-N2: Instruction tuning 失效是最主要的实用性限制，主文讨论不足**

同意核心论点。Appendix k (p21-22) 的证据确实严重：instruction tuning 使 3-class F1 下降 3.7-19.9pp，且 DDR 结构本身被改变（"instruction tuning compresses the feature-space structure underlying DDR rather than simply reversing feature directions"）。这不是性能的微小退化，而是方法论假设的根本性违反。

论文的动机叙事（Section 1, p1-2: "data provenance", "corpus auditing", "contamination monitoring"）确实隐含了一个现实应用场景——但当前部署的 LLM 几乎全部经过 instruction tuning 或 RLHF。如果方法仅适用于 base models，这些动机的实际覆盖面远小于暗示的范围。

**我的补充与细微分歧**: 尽管同意主文讨论不足，但 R2 将此定为 "最主要的实用性限制" 的判断需要轻微修正。Base model 文本生成并非无实际场景——训练数据合成（synthetic data generation for SFT/DPO）、模型坍塌研究（model collapse monitoring）、以及 pre-training data contamination detection 都是 base model 输出的直接应用场景。论文在 Section 5 (p8) 的 "downstream data curation" 方向讨论中已部分触及。因此，我建议的修改是：在 Section 5 增加一个专门段落讨论 instruction tuning 影响并**显式界定方法的适用范围**（base model text generation pipeline），而非完全否定方法的实用价值。

---

### Should-Fix 问题

**[AGREE] R2-W1: "Depth profiling" 命名暗示超出实际能力的精细粒度**

同意。5-class 评估（gen-0/1/2/3/4）的 F1 仅为 0.521（Appendix d, Table 5, p15），而 3-class 设置实质上已将 depth 2-4 合并为 gen-2+。"Profiling" 一词暗示连续或高分辨率的深度估计，但方法实际上是粗粒度的序数分类（3个类别）。我在自己的审稿中也提出了类似关切（M3: "为何不报告 5-class 评估作为主结果？"）。

建议将 "depth profiling" 重新定义为 "coarse ordinal depth classification"，或在首次使用时明确限定其含义。

---

**[AGREE] R2-W2: "Entropy" 术语贯穿全文但实际指 reference-model NLL**

完全同意。我在自己的审稿中也标记了这个问题（M1）。Section 3.3 (p4) 有一句澄清（"All 'entropy' features are reference-model NLL values (cross-entropy with Pythia-410M), not information-theoretic entropy"），但此后论文回归使用 "entropy mean"、"entropy std" 等术语，容易让读者误以为是信息论意义上的 entropy。

"NLL" 或 "cross-entropy" 是更精确的术语，至少在 Table 1 和 Section headers 中应使用完整名称。

---

**[REBUT] R2-W3: Contribution #2 的表述混淆了描述性观察与方法论贡献**

部分反驳。R2 认为 DDR 分区仅是描述性观察而非方法论贡献——但我认为这低估了 DDR 的分析价值。

DDR 分区不仅仅是"发现某些特征漂移、某些不漂移"这一事实。它提供了一个**可检验的理论框架**：location drift（词汇压缩）vs. shape preservation（分布形态稳定）的二元分解对递归生成的分布变化给出了结构化解释。这类似于 NLP 中 surface-level vs. deep-level 特征分析的传统，具有独立的科学价值。

**关键证据**:
- DDR 分区在 holdout generator split 中可复现（Table 35, p30: 最大 Δ(d)=0.05）
- k-means 无监督验证恢复相同结构（Appendix v, p28: silhouette=0.660）
- TOST 等价性检验确认 near-stationary 特征跨深度的效应量可忽略（Appendix u, p28-29: 100% rejection rate）
- 跨温度迁移（Appendix p, p26）和跨域迁移（Appendix j, p19-20）中 DDR 结构保持一致

然而，我同意 R2 的一个子论点：Contribution #2 的**措辞**确实可以更精确。应将其定位为"empirical regularity with analytical utility"（一个经验规律性发现，具有分析效用），而非暗示它是一种新方法或新算法。

---

**[AGREE] R2-W4: 跨 family 泛化未被显式测试**

同意这是一个有意义的缺失。当前 LOGO 按单个 generator hold out——当 held-out generator 是 Pythia-2.8B 时，Pythia-1B 仍在训练集中。分类器可能学习到 Pythia family 特有的 depth 模式，并利用 intra-family 相似性获得虚高的泛化性能。

论文有 5 个 family：Pythia (2), OLMo (1), Qwen (2), Llama (1), Mistral (1)。对单模型 family (OLMo, Llama, Mistral)，LOGO 等价于 leave-one-family-out。但对 Pythia 和 Qwen，intra-family 信号确实可能泄漏。

一个 leave-one-family-out (LOFO-family) 评估会很有信息量——尤其是 hold out 整个 Pythia family（2个模型）或整个 Qwen family（2个模型）时，F1 是否显著下降。

---

**[AGREE] R2-W5: Related work 在 stylometry/authorship attribution 方向覆盖不足**

同意。深度分析在概念上与 authorship attribution 有直接联系——两者都通过分布特征（TTR、hapax ratio、词汇丰富度指标）区分不同"作者"（这里是不同深度的生成过程）。stylometry 文献中的 Brennan et al. (2012), Stamatatos (2009) 等经典工作建立了使用这些表面特征进行文本归属的理论基础，论文应讨论与这些工作的关系和区别。

论文的 Related Work (Section 2, p2-3) 覆盖了 AI text detection 和 model collapse 两条线，但完全缺少 stylometry/authorship attribution 这一自然关联方向。

---

## 总结

| R2 Issue | 我的判断 | 理由 |
|----------|---------|------|
| N1 (shape causal claim) | [AGREE] | LOFO + PI 证据直接矛盾，XGBoost 机制分析有说服力 |
| N2 (instruction tuning) | [AGREE] with nuance | 主文讨论确实不足，但 base model 场景非零；建议界定适用范围而非否定价值 |
| W1 (naming) | [AGREE] | 5-class F1=0.521 说明"profiling"过于乐观 |
| W2 (entropy terminology) | [AGREE] | 与我的 M1 一致 |
| W3 (contribution framing) | [REBUT] | DDR 分区具有独立分析价值，但措辞应从"方法论贡献"降级为"经验规律性发现" |
| W4 (cross-family) | [AGREE] | Pythia/Qwen 的 intra-family 泄漏是合理关切 |
| W5 (stylometry) | [AGREE] | 自然关联方向的缺失 |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3912 · 2026-05-23T01:50:04.094651+00:00_

收到 Reviewer 1 的交叉回应，等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 385

## Round 385

2 recorded events


### User

_source line 3913 · 2026-05-23T01:50:06.747877+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的7个问题：5个 [AGREE]（N1 shape causal claim、N2 instruction tuning 主文不足、W1 命名、W2 术语、W4 跨 family 泛化、W5 stylometry），1个 [AGREE with nuance]（N2 的严重性略有保留——base model 场景非零），1个 [REBUT]（W3——DDR 分区具有独立分析价值，但同意措辞应更精确）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3914 · 2026-05-23T01:50:13.869550+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 386

## Round 386

22 recorded events


### User

_source line 3915 · 2026-05-23T01:51:32.642844+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R1-N1: Gen-0 种子共享在 LOGO 评估中造成 train-test 信息泄漏**

R1 的分析准确。论文使用 ~1,000 条共享 Wikipedia 种子作为所有生成器的 gen-0，因此在 LOGO hold-out 时，被测生成器的 gen-0 特征向量与训练集中其他生成器的 gen-0 完全一致——这确实构成事实上的 train-test 重叠。

但需注意论文已部分缓解了这一问题：
1. Section 3.2 (p.4) 明确承认了这一泄漏："creating a potential train-test overlap for the gen-0 class"
2. 论文提供了 leak-free binary F1 = 0.694 (gen-1 vs. gen-2+) 作为保守指标（Section 4.1, p.5）
3. Section 4.1 将 binary F1 明确标注为 "our most conservative metric"

R1 估计的 ~3pp 高估（macro F1 从 0.762 降至 ~0.73）在数量级上合理。我认为最佳修复方案是 R1 建议的"不相交种子池"实验，但短期可行的替代方案是**将 binary F1 升格为并列主指标**，在 Abstract 和 Table 2 中同等强调 3-class 和 binary 结果。

**严重程度判断**：我同意这是 Must-Fix，但不认为它动摇核心发现。即使 3-class F1 被高估 3pp，核心 DDR 分析基于 per-feature Cohen's d 和趋势分析，不依赖于分类器性能。Binary F1 = 0.694 已经是 leak-free 的，仍远高于 random baseline。

---

**[AGREE with nuance] R1-N2: DDR 分区的 post-hoc 性质**

R1 指出 DDR 分区是通过观察7个特征在 (|ρ|, d) 空间后事后定义的，k-means 验证存在弱循环。这一方法论批评在原则上成立。

但我认为 R1 低估了论文已有的验证强度：
1. **Holdout generator split validation**（Table 35, p.30）：将8个生成器分为 selection(4) + validation(4)，所有特征的 zone assignment 完全一致，max Δ(d) = 0.05。R1 承认了这一点但认为"被埋在附录深处"。
2. **Per-generator replication**（Appendix u, Table 31, p.28-29）：每个生成器独立复现相同的分区结构——三个 near-stationary 特征在所有1,000次 bootstrap 迭代中从未被拒绝等价性。
3. **Threshold robustness**（Table 34, p.30）：分区在 ε ∈ [0.10, 0.75] 范围内稳定，三个 drifting 特征和三个 near-stationary 特征的分类在所有阈值下不变。

不过，我同意 R1 的建议：**将 Table 35 的 holdout split validation 提升到主文**（甚至 Section 4.2）将显著加强说服力。当前的呈现确实让最有力的验证证据难以被 reviewer 注意到。

R1 关于"缺乏前置理论驱动"的批评部分合理，但对于 empirical study 来说，post-hoc observation + rigorous cross-validation 是合法的研究路径。论文的贡献类型是"empirical decomposition"（Section 1 明确这样表述），而非理论预测。

---

### Should-Fix 问题

**[AGREE] R1-W1: TOST 等价性边界 |d|≤0.20 缺乏任务特异性校准**

R1 的批评方向正确——Cohen's d = 0.20 的"小效应"阈值来自社会科学惯例，没有任务特异性依据。在分类任务中，d=0.15 可能已经有实际意义。

但**实际影响有限**：Table 31 (p.28) 显示三个 near-stationary 特征的实际 d 值远低于 0.20（entropy_min d=0.08, tail_decay d=0.08, entropy_max d=0.06），且 Table 34 (p.30) 证明分区在 ε ∈ [0.10, 0.75] 范围内完全稳定。即使将阈值收紧到 |d|≤0.10，三个 shape features 仍然归入 near-stationary。

**补充建议**：论文可以从分类器性能角度提供 task-specific 校准——例如展示当某个特征的 d 超过某个阈值时，LOGO F1 开始显著下降。这将比社会科学惯例更有说服力。

---

**[REBUT] R1-W2: QLoRA 与 XGBoost 的比较在不同生成器子集上进行**

R1 的担忧在呈现层面有一定道理，但**论文已提供了同子集的公平对比**。Appendix e (p.16) 明确报告："QLoRA achieves 3-class LOGO F1 = 0.905 (±0.003) under 6-generator LOGO, a +11.6pp improvement over the same-subset XGBoost baseline (0.789)." 

这里 XGBoost 0.789 是在完全相同的 6-gen 子集上计算的，与 QLoRA 0.905 直接可比。+11.6pp 的差距是在公平条件下测量的。主文的 0.762 来自 8-gen LOGO（更难的设定），不直接与 QLoRA 比较。

不过，我同意 R1 暗含的建议：主文应更清晰地呈现同子集对比数字，而非让读者自行从附录中发现。

---

**[AGREE] R1-W3: 7-feature ensemble 的 3-class F1 低于最强 baseline**

如果 R1 引用的数字（4-det+surface 0.798 vs 7-feature 0.762）正确，这确实是一个值得在主文讨论的问题。Table 3 (p.7) 的 caption 提到 "The 7-feature ensemble (one 4-010M reference model) matches multi-detector ensembles (two models, 1.4B total) at ~2.5× lower cost"——但如果在绝对 F1 上被多检测器组合超越，"matches"的表述需要更谨慎。

论文的价值主张是效率-性能权衡（单一 reference model forward pass vs. 多模型推理），这是合理的，但**主文应明确量化这一权衡**：什么样的 F1 损失换取了多大的计算节省？

---

**[AGREE] R1-W4: Bootstrap CI 的重采样单位是文本级别，可能低估生成器级泛化不确定性**

这是一个精准的统计批评。在 LOGO 设定下，泛化不确定性的来源主要是 generator-level variance（哪些生成器容易/难以泛化），而非 text-level variance（同一生成器内哪些文本容易/难以分类）。文本级 bootstrap 会低估前者。

LOGO 本身提供了8个 fold-level F1 值，这些值的标准差才是 generator-level uncertainty 的更好估计。论文 Table 2 报告了 95% bootstrap CI [0.758, 0.766]，但没有报告 fold-level（即 per-generator）的方差。

**建议**：补充报告 8 个 LOGO fold 的 per-generator F1 分布（mean ± std），作为 generator-level uncertainty 的估计。这比文本级 bootstrap CI 更有信息量。

---

**[AGREE] R1-W5: Entropy_std 的"intermediate"地位挑战 DDR 的 binary partition 叙事**

这与我在 R2-W3 中提出的 Contribution #2 表述问题一致。Entropy_std (d=0.53-0.55, ρ=0.16) 既不是 drifting（d > 0.76 for the other three）也不是 near-stationary（d < 0.10），论文将其标为 "intermediate" 但整体叙事仍强调 binary decomposition（"drifting vs. near-stationary"）。

这实际上是一个三分类（drifting / intermediate / near-stationary），而非论文标题和摘要暗示的二分类。论文在 Section 4.2 (p.6) 和 Figure 4 (p.7) 中确实讨论了 entropy_std 的中间状态，但在 Abstract 和 Introduction 中，叙事被简化为 "location vs. shape"，entropy_std 被降为脚注式的补充。

**建议**：在 Abstract/Introduction 中从一开始就承认三组结构（drifting / intermediate / near-stationary），而非在主文中途再"修正"叙事。Table 1 (p.4) 已经标注了三个 zone，但上层叙事应与之一致。

---

### 总结

| R1 Issue | 我的判断 | 核心理由 |
|----------|---------|---------|
| N1 (gen-0 泄漏) | AGREE | 泄漏真实存在，论文有部分缓解但主指标仍被高估 ~3pp |
| N2 (DDR post-hoc) | AGREE with nuance | 方法论批评成立但论文已有较强的 holdout validation；应提升至主文 |
| W1 (TOST 边界) | AGREE | 原则正确但实际影响有限（实际 d 值远低于阈值） |
| W2 (QLoRA 子集) | REBUT | 论文 Appendix e 已提供同子集公平对比（0.905 vs 0.789） |
| W3 (低于最强 baseline) | AGREE | 效率-性能权衡应在主文中明确量化 |
| W4 (Bootstrap 单位) | AGREE | 应补充 per-generator fold-level 方差 |
| W5 (Entropy_std 中间态) | AGREE | 叙事应从 binary 修正为 ternary decomposition |

### R1 与 R2 共识点

两位 Reviewer 在以下方面形成共识：
1. **DDR 的因果/机制声称需要弱化**（R1-N2 post-hoc + R2-N1 causal overclaim → 应改为纯描述性表述）
2. **Entropy_std 的三组结构应反映在顶层叙事中**（R1-W5 + R2-W3）
3. **Binary F1 应获得更高的展示权重**（R1-N1 + R2 的隐含关注）
4. **Instruction tuning 限制需要更突出的讨论**（R2-N2 独立提出，R1 未涉及）


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 3916 · 2026-05-23T01:52:31.571507+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 3917 · 2026-05-23T01:52:31.622129+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T01:36:28.862899+00:00\", \"completed_at\": \"2026-05-23T01:40:53.204309+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页为纯文本（Title + Abstract + Introduction），无视觉锚点。Figure 1 出现在 page 2 顶部，在前 3 页范围内，符合预期。Figure 1 为全宽三面板框架图（Generation Chain → Feature Extraction & DDR → Depth Classification），信息密度高，能有效锚定审稿人对论文核心方法的认知。Title-Abstract-Figure 1 三者叙事一致。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"纯文本页（Related Work），但前后页面（p2 有 Figure 1，p4 有 Table 1）均有 display item，不构成连续纯文本问题。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"纯文本页（Evaluation Protocol + Results 开头），介于 Table 1 (p4) 与 Figure 2 (p6) 之间。不构成连续两页纯文本，但审稿人从 p4 到 p6 经历一整页无 display item 的文字，节奏稍慢。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3（散点图：LOGO binary F1 vs. inference cost）和 Figure 4（DDR 柱状图）中部分文字标注（模型名称、图例条目）字号偏小，约为正文字号的 60-65%。建议适当放大 axis label 和 legend 字号以提升打印可读性。Figure 4 的 hatching 填充模式在灰度打印下可能难以区分——建议辅以颜色 + marker shape 双重编码。\"}, {\"severity\": \"warning\", \"dimension\": \"page 14\", \"message\": \"Figure 5（7 个 violin 子图）占据整页约 90% 面积，仅底部有一行 caption。虽然信息量大，但作为附录中的单一 display item 占用整页显得空间效率偏低。建议考虑缩小子图尺寸或调整为 4×2 网格布局，将部分文字分析放在同页。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3 使用 booktabs 风格，最优结果加粗标注。Limitations 段简短（约 1/3 栏），符合 EMNLP 要求。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Ethics Statement / Licenses / Compute budget / Software 各段简洁，References 从该页中部开始。排版干净，无拥挤或异常空白。\"}, {\"severity\": \"info\", \"dimension\": \"pages 10-12\", \"message\": \"参考文献页格式统一，未发现 [?] 未解析引用、跳号或截断。Author 缩写和期刊名格式一致。\"}, {\"severity\": \"warning\", \"dimension\": \"page 36\", \"message\": \"最后一页内容约占 65-70%，底部约 30% 空白。Figure 16（Token-level NLL Distribution）和 Table 48（Concurrent Studies comparison）填充了大部分页面，但仍有可优化空间。可考虑将 Table 48 下方的空白用后续内容填充或调整图表尺寸。\"}, {\"severi
…[truncated 592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3918 · 2026-05-23T01:57:47.455486+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3 && python3 -c \"\nimport yaml, sys\n\n# Read existing issues\nwith open('projects/gen-depth-fingerprint/artifacts/review_issues.yaml', 'r') as f:\n    issues = yaml.safe_load(f)\n\n# Build a dict for quick lookup\nissue_map = {i['id']: i for i in issues}\n\n# --- Update R49 in_progress entries ---\n\n# R49-MF1: Bootstrap CI level\nif 'R49-MF1' in issue_map:\n    issue_map['R49-MF1']['last_seen_round'] = 50\n    issue_map['R49-MF1']['mentions'].append({\n        'round': 50,\n        'reviewers': 'R1-W4+R2(AGREE)',\n        'note': 'R50重新确认: text-level bootstrap低估generator-level泛化不确定性. 论文已有per-generator SD=0.028但未在CI中突出.'\n    })\n\n# R49-MF2: Overclaim\nif 'R49-MF2' in issue_map:\n    issue_map['R49-MF2']['last_seen_round'] = 50\n    issue_map['R49-MF2']['mentions'].append({\n        'round': 50,\n        'reviewers': 'R2-N1+R1(AGREE)+R2-N2',\n        'note': 'R50聚焦shape feature causal overclaim: Abstract声称shape enables cross-generator transfer, 但LOFO/PI证据显示shape边际贡献极小. 同时instruction tuning失效未在主文充分讨论.'\n    })\n\n# R49-MF3: DDR novelty\nif 'R49-MF3' in issue_map:\n    issue_map['R49-MF3']['last_seen_round'] = 50\n    issue_map['R49-MF3']['mentions'].append({\n        'round': 50,\n        'reviewers': 'R1-N2+R2(AGREE with nuance)',\n        'note': 'R50确认DDR post-hoc定义问题. holdout generator split validation(Table 35)有效但被埋在附录. R2认为empirical study的post-hoc+cross-validation是合法路径.'\n    })\n\n# R49-MF4: Downstream utility\nif 'R49-MF4' in issue_map:\n    issue_map['R49-MF4']['mentions'].append({\n        'round': 50,\n        'reviewers': 'n/a',\n        'note': 'R50未提及. Discussion已有downstream caveat (\\\"no downstream improvement was observed\\\"), 可能已充分处理.'\n    })\n\n# R49-SF1: TOST margin\nif 'R49-SF1' in issue_map:\n    issue_map['R49-SF1']['last_seen_round'] = 50\n    issue_map['R49-SF1']['mentions'].append({\n        'round': 50,\n        'reviewers': 'R1-W1+R2(AGREE)',\n        'note': 'R50重新确认. 实际影响有限(near-stationary d<0.10远低于阈值), 但应显式引用LOFO结果作为任务内校准证据.'\n    })\n\n# R49-SF2: Feature redundancy\nif 'R49-SF2' in issue_map:\n    issue_map['R49-SF2']['mentions'].append({\n        'round': 50,\n        'reviewers': 'n/a',\n        'note': 'R50未提及. 论文已有PCA 92.3% + LOFO讨论, 可能已充分处理.'\n    })\n\n# R49-SF4: Concurrent works\nif 'R49-SF4' in issue_map:\n    issue_map['R49-SF4']['mentions'].append({\n        'round': 50,\n        'reviewers': 'n/a',\n        'note': 'R50 R2-S6确认concurrent work对比清晰(Table 48). 可能已解决.'\n    })\n\n# R49-SF5: QLoRA comparison\nif 'R49-SF5' in issue_map:\n    issue_map['R49-SF5']['last_seen_round'] = 50\n    issue_map['R49-SF5']['mentions'].append({\n        'round': 50,\n        'reviewers': 'R1-W2(raised)+R2(REBUT)',\n        'note': 'R50分歧: R1认为6-gen vs 8-gen不可比; R2指出Appendix e已有同子集公平对比(0.905 vs 0.789). Director判断R2正确, 但主文呈现应更清晰.'\n    })\n\n# R49-SF6: Primary metric\nif 'R49-SF6' in issue_map:\n    issue_map['R49-SF6']['last_seen_round'] = 50\n    issue_map['R49-SF6']['mentions'].append({\n        'round': 50,\n        'reviewers': 'R1-N1+R2(AGREE)',\n        'note': 'R50因gen-0泄漏问题使primary metric选择更加重要. 论文已标注binary F1为primary conservative metric, 但Abstract/Intro仍以3-class为主.'\n    })\n\n# R49-SF7: Handcrafted vs end-to-end\nif 'R49-SF7' in issue_map:\n    issue_map['R49-SF7']['mentions'].append({\n        'round': 50,\n        'reviewers': 'n/a',\n        'note': 'R50未直接提及.'\n    })\n\n# R49-MR1: Schaeffer et al.\nif 'R49-MR1' in issue_map:\n    issue_map['R49-MR1']['mentions'].append({\n        'round': 50,\n        'reviewers': 'n/a',\n        'note': 'R50未提及. 待确认是否已补入.'\n    })\n\n# R49-MR2: Hans et al.\nif 'R49-MR2' in issue_map:\n    issue_map['R49-MR2']['mentions'].append({\n        'round': 50,\n        'reviewers': 'n/a',\n        'note': 'R50未提及.'\n    })\n\n# R49-MR3: Paraphrase attack\nif 'R49-MR3' in issue_map:\n    issue_map['R49-MR3']['last_seen_round'] = 50\n    issue_map['R49-MR3']['mentions'].append({\n        'round': 50,\n        'reviewers': 'R1-MR',\n        'note': 'R1提及Krishna et al. (2024) paraphrase attack应在robustness讨论中对比.'\n    })\n\n# R49-MR4: Span-level detection\nif 'R49-MR4' in issue_map:\n    issue_map['R49-MR4']['mentions'].append({\n        'round': 50,\n        'reviewers': 'n/a',\n        'note': 'R50未提及.'\n    })\n\n# --- Add new R50 issues ---\n\nnew_issues = [\n    {\n        'id': 'R50-N1',\n        'summary': 'Shape feature causal overclaim — LOFO/PI证据与Abstract因果声称矛盾',\n        'category': 'framing',\n        'severity': 'critical',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R2-N1+R1(AGREE)', 'note': 'Abstract \\\"shape features enable cross-generator depth classification\\\" 是因果声明, 但LOFO显示shape边际贡献极小(Δ≤-1.5pp), PI中near-stationary仅为drifting的18%. XGBoost中跨深度恒定特征不会获得分裂节点.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R50-N2',\n        'summary': 'Gen-0种子共享导致LOGO 3-class F1=0.762被高估约3pp',\n        'category': 'experiment',\n        'severity': 'critical',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R1-N1+R2(AGREE)', 'note': '共享Wikipedia种子使hold-out生成器gen-0特征向量与训练集gen-0完全一致. 论文已有leak-free binary F1=0.694, 但Abstract/Intro仍以3-class为主展示.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R50-N3',\n        'summary': 'Instruction tuning失效在主文讨论不足——动机与适用范围脱节',\n        'category': 'framing',\n        'severity': 'critical',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R2-N2+R1(AGREE with nuance)', 'note': 'Appendix k显示instruct使3-class F1下降3.7-19.9pp, DDR结构被根本改变. 主文仅一句话量化. R1补充base model场景非零(SFT合成、model collapse), 建议界定适用范围.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R50-W1',\n        'summary': '\\\"Depth profiling\\\"命名暗示超出3-class的精细粒度',\n        'category': 'framing',\n        'severity': 'warning',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R2-W1+R1(AGREE)', 'note': '5-class F1仅0.521. Profiling暗示连续或高分辨率深度估计, 实际为3-class粗粒度分类.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R50-W2',\n        'summary': 'Entropy术语全文使用但实际指reference-model NLL (R32-W3复发)',\n        'category': 'writing',\n        'severity': 'warning',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R2-W2+R1(AGREE)', 'note': 'Section 3.3有一次澄清但后续全文回归entropy命名. Table 1 caption有NLL-based标注但不足. 与R32-W3同类问题.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R50-W3',\n        'summary': 'Entropy_std intermediate (d=0.55)挑战DDR binary partition叙事',\n        'category': 'framing',\n        'severity': 'warning',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R1-W5+R2(AGREE)', 'note': 'DDR实际为三组(drifting/intermediate/near-stationary), 但Abstract/Intro简化为二元. 建议从顶层叙事承认三组结构.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R50-W4',\n        'summary': '3-class F1低于最强baseline (4-det+surface 0.798 vs 0.762)但主文未充分讨论',\n        'category': 'writing',\n        'severity': 'warning',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R1-W3+R2(AGREE)', 'note': 'Section 4.3聚焦binary用\\\"matches\\\"表述, 对3-class劣势轻描淡写. 应明确量化效率-性能权衡.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R50-W5',\n        'summary': 'Stylometry/authorship attribution related work覆盖不足',\n        'category': 'writing',\n        'severity': 'warning',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R2-W5+R1(AGREE)', 'note': 'TTR/hapax ratio是计算文体学核心特征, 但论文未讨论depth profiling与authorship attribution的方法论联系. 缺Stamatatos (2009)等引用.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    }\n]\n\nissues.extend(new_issues)\n\n# Output the complete YAML\nprint(yaml.dump(issues, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200))\n\" 2>&1 | head -800",
  "description": "Generate updated review issues YAML",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3 && python3 -c \"\nimport yaml, sys\n\n# Read existing issues\nwith open('projects/gen-depth-fingerprint/artifacts/review_issues.yaml', 'r') as f:\n    issues = yaml.safe_load(f)\n\n# Build a dict for quick lookup\nissue_map = {i['id']: i for i in issues}\n\n# --- Update R49 in_progress entries ---\n\n# R49-MF1: Bootstrap CI level\nif 'R49-MF1' in issue_map:\n    issue_map['R49-MF1']['last_seen_round'] = 50\n    issue_map['R49-MF1']['mentions'].append({\n        'round': 50,\n        'reviewers': 'R1-W4+R2(AGREE)',\n        'note': 'R50重新确认: text-level bootstrap低估generator-level泛化不确定性. 论文已有per-generator SD=0.028但未在CI中突出.'\n    })\n\n# R49-MF2: Overclaim\nif 'R49-MF2' in issue_map:\n    issue_map['R49-MF2']['last_seen_round'] = 50\n    issue_map['R49-MF2']['mentions'].append({\n        'round': 50,\n        'reviewers': 'R2-N1+R1(AGREE)+R2-N2',\n        'note': 'R50聚焦shape feature causal overclaim: Abstract声称shape enables cross-generator transfer, 但LOFO/PI证据显示shape边际贡献极小. 同时instruction tuning失效未在主文充分讨论.'\n    })\n\n# R49-MF3: DDR novelty\nif 'R49-MF3' in issue_map:\n    issue_map['R49-MF3']['last_seen_round'] = 50\n    issue_map['R49-MF3']['mentions'].append({\n        'round': 50,\n        'reviewers': 'R1-N2+R2(AGREE with nuance)',\n        'note': 'R50确认DDR post-hoc定义问题. holdout generator split validation(Table 35)有效但被埋在附录. R2认为empirical study的post-hoc+cross-validation是合法路径.'\n    })\n\n# R49-MF4: Downstream utility\nif 'R49-MF4' in issue_map:\n    issue_map['R49-MF4']['mentions'].append({\n        'round': 50,\n        'reviewers': 'n/a',\n        'note': 'R50未提及. Discussion已有downstream caveat (\\\"no downstream improvement was observed\\\"), 可能已充分处理.'\n    })\n\n# R49-SF1: TOST margin\nif 'R49-SF1' in issue_map:\n    issue_map['R49-SF1']['last_seen_round'] = 50\n    issue_map['R49-SF1']['mentions'].append({\n        'round': 50,\n        'reviewers': 'R1-W1+R2(AGREE)',\n        'note': 'R50重新确认. 实际影响有限(near-stationary d<0.10远低于阈值), 但应显式引用LOFO结果作为任务内校准证据.'\n    })\n\n# R49-SF2: Feature redundancy\nif 'R49-SF2' in issue_map:\n    issue_map['R49-SF2']['mentions'].append({\n        'round': 50,\n        'reviewers': 'n/a',\n        'note': 'R50未提及. 论文已有PCA 92.3% + LOFO讨论, 可能已充分处理.'\n    })\n\n# R49-SF4: Concurrent works\nif 'R49-SF4' in issue_map:\n    issue_map['R49-SF4']['mentions'].append({\n        'round': 50,\n        'reviewers': 'n/a',\n        'note': 'R50 R2-S6确认concurrent work对比清晰(Table 48). 可能已解决.'\n    })\n\n# R49-SF5: QLoRA comparison\nif 'R49-SF5' in issue_map:\n    issue_map['R49-SF5']['last_seen_round'] = 50\n    issue_map['R49-SF5']['mentions'].append({\n        'round': 50,\n        'reviewers': 'R1-W2(raised)+R2(REBUT)',\n        'note': 'R50分歧: R1认为6-gen vs 8-gen不可比; R2指出Appendix e已有同子集公平对比(0.905 vs 0.789). Director判断R2正确, 但主文呈现应更清晰.'\n    })\n\n# R49-SF6: Primary metric\nif 'R49-SF6' in issue_map:\n    issue_map['R49-SF6']['last_seen_round'] = 50\n    issue_map['R49-SF6']['mentions'].append({\n        'round': 50,\n        'reviewers': 'R1-N1+R2(AGREE)',\n        'note': 'R50因gen-0泄漏问题使primary metric选择更加重要. 论文已标注binary F1为primary conservative metric, 但Abstract/Intro仍以3-class为主.'\n    })\n\n# R49-SF7: Handcrafted vs end-to-end\nif 'R49-SF7' in issue_map:\n    issue_map['R49-SF7']['mentions'].append({\n        'round': 50,\n        'reviewers': 'n/a',\n        'note': 'R50未直接提及.'\n    })\n\n# R49-MR1: Schaeffer et al.\nif 'R49-MR1' in issue_map:\n    issue_map['R49-MR1']['mentions'].append({\n        'round': 50,\n        'reviewers': 'n/a',\n        'note': 'R50未提及. 待确认是否已补入.'\n    })\n\n# R49-MR2: Hans et al.\nif 'R49-MR2' in issue_map:\n    issue_map['R49-MR2']['mentions'].append({\n        'round': 50,\n        'reviewers': 'n/a',\n        'note': 'R50未提及.'\n    })\n\n# R49-MR3: Paraphrase attack\nif 'R49-MR3' in issue_map:\n    issue_map['R49-MR3']['last_seen_round'] = 50\n    issue_map['R49-MR3']['mentions'].append({\n        'round': 50,\n        'reviewers': 'R1-MR',\n        'note': 'R1提及Krishna et al. (2024) paraphrase attack应在robustness讨论中对比.'\n    })\n\n# R49-MR4: Span-level detection\nif 'R49-MR4' in issue_map:\n    issue_map['R49-MR4']['mentions'].append({\n        'round': 50,\n        'reviewers': 'n/a',\n        'note': 'R50未提及.'\n    })\n\n# --- Add new R50 issues ---\n\nnew_issues = [\n    {\n        'id': 'R50-N1',\n        'summary': 'Shape feature causal overclaim — LOFO/PI证据与Abstract因果声称矛盾',\n        'category': 'framing',\n        'severity': 'critical',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R2-N1+R1(AGREE)', 'note': 'Abstract \\\"shape features enable cross-generator depth classification\\\" 是因果声明, 但LOFO显示shape边际贡献极小(Δ≤-1.5pp), PI中near-stationary仅为drifting的18%. XGBoost中跨深度恒定特征不会获得分裂节点.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R50-N2',\n        'summary': 'Gen-0种子共享导致LOGO 3-class F1=0.762被高估约3pp',\n        'category': 'experiment',\n        'severity': 'critical',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R1-N1+R2(AGREE)', 'note': '共享Wikipedia种子使hold-out生成器gen-0特征向量与训练集gen-0完全一致. 论文已有leak-free binary F1=0.694, 但Abstract/Intro仍以3-class为主展示.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R50-N3',\n        'summary': 'Instruction tuning失效在主文讨论不足——动机与适用范围脱节',\n        'category': 'framing',\n        'severity': 'critical',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R2-N2+R1(AGREE with nuance)', 'note': 'Appendix k显示instruct使3-class F1下降3.7-19.9pp, DDR结构被根本改变. 主文仅一句话量化. R1补充base model场景非零(SFT合成、model collapse), 建议界定适用范围.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R50-W1',\n        'summary': '\\\"Depth profiling\\\"命名暗示超出3-class的精细粒度',\n        'category': 'framing',\n        'severity': 'warning',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R2-W1+R1(AGREE)', 'note': '5-class F1仅0.521. Profiling暗示连续或高分辨率深度估计, 实际为3-class粗粒度分类.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R50-W2',\n        'summary': 'Entropy术语全文使用但实际指reference-model NLL (R32-W3复发)',\n        'category': 'writing',\n        'severity': 'warning',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R2-W2+R1(AGREE)', 'note': 'Section 3.3有一次澄清但后续全文回归entropy命名. Table 1 caption有NLL-based标注但不足. 与R32-W3同类问题.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R50-W3',\n        'summary': 'Entropy_std intermediate (d=0.55)挑战DDR binary partition叙事',\n        'category': 'framing',\n        'severity': 'warning',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R1-W5+R2(AGREE)', 'note': 'DDR实际为三组(drifting/intermediate/near-stationary), 但Abstract/Intro简化为二元. 建议从顶层叙事承认三组结构.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R50-W4',\n        'summary': '3-class F1低于最强baseline (4-det+surface 0.798 vs 0.762)但主文未充分讨论',\n        'category': 'writing',\n        'severity': 'warning',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R1-W3+R2(AGREE)', 'note': 'Section 4.3聚焦binary用\\\"matches\\\"表述, 对3-class劣势轻描淡写. 应明确量化效率-性能权衡.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R50-W5',\n        'summary': 'Stylometry/authorship attribution related work覆盖不足',\n        'category': 'writing',\n        'severity': 'warning',\n        'status': 'open',\n        'first_raised_round': 50,\n        'last_seen_round': 50,\n        'mentions': [{'round': 50, 'reviewers': 'R2-W5+R1(AGREE)', 'note': 'TTR/hapax ratio是计算文体学核心特征, 但论文未讨论depth profiling与authorship attribution的方法论联系. 缺Stamatatos (2009)等引用.'}],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    }\n]\n\nissues.extend(new_issues)\n\n# Output the complete YAML\nprint(yaml.dump(issues, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200))\n\" 2>&1 | head -800",
    "description": "Generate updated review issues YAML",
    "timeout": "30000"
  }
}
```

</details>

---


### Tool result

_source line 3919 · 2026-05-23T01:57:47.958667+00:00_

- id: R29-N1
  summary: Base-model-only scope 未在 Abstract 标注
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 32
  resolution: Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented.
  resolution_round: 32
- id: R29-N2
  summary: Downstream TOST underpowered (n=3) + Abstract overclaim
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 34
  resolution: Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料.
  resolution_round: 34
- id: R29-N3
  summary: DDR 新颖性 incremental — 缺 concurrent work 系统对比表
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 31
  resolution: related_work.tex concurrent-comparison table added
  resolution_round: 31
- id: R29-N4
  summary: QLoRA gap 削弱方法论贡献 — 需重定位
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 29
  last_seen_round: 34
  resolution: Intro L14 'proof of concept'; Contribution 3 'Proof-of-concept classifier with boundary analysis'.
  resolution_round: 34
- id: R29-W1
  summary: Gemma-2-2B gen-1 F1=0.036 anomaly 解释不充分
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 29
  last_seen_round: 31
  resolution: appendix_9gen_scale expanded
  resolution_round: 31
- id: R29-W2
  summary: Cross-model chain F1=0.830 可能混淆 depth signal 与 generator identity
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 29
  last_seen_round: 34
  resolution: results.tex footnote + L15 single-gen transfer. Caveats sufficient.
  resolution_round: 34
- id: R29-W3
  summary: 温度限制(t<0.9)未在 Abstract 标注
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 29
  last_seen_round: 32
  resolution: Abstract L4 'nucleus sampling (p=0.9, t<=0.7)'
  resolution_round: 31
- id: R29-W4
  summary: 
…[truncated 22933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 3920 · 2026-05-23T01:58:43.664100+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3 && python3 -c \"\nimport yaml, sys\n\nwith open('projects/gen-depth-fingerprint/artifacts/review_issues.yaml', 'r') as f:\n    issues = yaml.safe_load(f)\n\nissue_map = {i['id']: i for i in issues}\n\n# Update R49 in_progress entries\nupdates = {\n    'R49-MF1': {'last_seen_round': 50, 'mention': {'round': 50, 'reviewers': 'R1-W4+R2(AGREE)', 'note': 'R50重新确认: text-level bootstrap低估generator-level泛化不确定性. 论文已有per-generator SD=0.028但未在CI中突出.'}},\n    'R49-MF2': {'last_seen_round': 50, 'mention': {'round': 50, 'reviewers': 'R2-N1+R1(AGREE)+R2-N2', 'note': 'R50聚焦shape feature causal overclaim: Abstract声称shape enables cross-generator transfer, 但LOFO/PI证据显示shape边际贡献极小. 同时instruction tuning失效未在主文充分讨论.'}},\n    'R49-MF3': {'last_seen_round': 50, 'mention': {'round': 50, 'reviewers': 'R1-N2+R2(AGREE with nuance)', 'note': 'R50确认DDR post-hoc定义问题. holdout generator split validation(Table 35)有效但被埋在附录. R2认为empirical study的post-hoc+cross-validation是合法路径.'}},\n    'R49-MF4': {'mention': {'round': 50, 'reviewers': 'n/a', 'note': 'R50未提及. Discussion已有downstream caveat, 可能已充分处理.'}},\n    'R49-SF1': {'last_seen_round': 50, 'mention': {'round': 50, 'reviewers': 'R1-W1+R2(AGREE)', 'note': 'R50重新确认. 实际影响有限(near-stationary d<0.10远低于阈值), 但应显式引用LOFO结果作为任务内校准证据.'}},\n    'R49-SF2': {'mention': {'round': 50, 'reviewers': 'n/a', 'note': 'R50未提及. 论文已有PCA 92.3% + LOFO讨论, 可能已充分处理.'}},\n    'R49-SF4': {'mention': {'round': 50, 'reviewers': 'n/a', 'note': 'R50 R2-S6确认concurrent work对比清晰(Table 48). 可能已解决.'}},\n    'R49-SF5': {'last_seen_round': 50, 'mention': {'round': 50, 'reviewers': 'R1-W2(raised)+R2(REBUT)', 'note': 'R50分歧: R1认为6-gen vs 8-gen不可比; R2指出Appendix e已有同子集公平对比(0.905 vs 0.789). Director判断R2正确, 但主文呈现应更清晰.'}},\n    'R49-SF6': {'last_seen_round': 50, 'mention': {'round': 50, 'reviewers': 'R1-N1+R2(AGREE)', 'note': 'R50因gen-0泄漏问题使primary metric选择更加重要. 论文已标注binary F1为primary conservative metric, 但Abstract/Intro仍以3-class为主.'}},\n    'R49-SF7': {'mention': {'round': 50, 'reviewers': 'n/a', 'note': 'R50未直接提及.'}},\n    'R49-MR1': {'mention': {'round': 50, 'reviewers': 'n/a', 'note': 'R50未提及. 待确认是否已补入.'}},\n    'R49-MR2': {'mention': {'round': 50, 'reviewers': 'n/a', 'note': 'R50未提及.'}},\n    'R49-MR3': {'last_seen_round': 50, 'mention': {'round': 50, 'reviewers': 'R1-MR', 'note': 'R1提及Krishna et al. (2024) paraphrase attack应在robustness讨论中对比.'}},\n    'R49-MR4': {'mention': {'round': 50, 'reviewers': 'n/a', 'note': 'R50未提及.'}},\n}\n\nfor iid, upd in updates.items():\n    if iid in issue_map:\n        if 'last_seen_round' in upd:\n            issue_map[iid]['last_seen_round'] = upd['last_seen_round']\n        issue_map[iid]['mentions'].append(upd['mention'])\n\n# Add new R50 issues\nnew_issues = [\n    {'id': 'R50-N1', 'summary': 'Shape feature causal overclaim — LOFO/PI证据与Abstract因果声称矛盾', 'category': 'framing', 'severity': 'critical', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R2-N1+R1(AGREE)', 'note': 'Abstract \\\"shape features enable cross-generator depth classification\\\"是因果声明, 但LOFO显示shape边际贡献极小(delta<=1.5pp), PI中near-stationary仅为drifting的18%.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n    {'id': 'R50-N2', 'summary': 'Gen-0种子共享导致LOGO 3-class F1=0.762被高估约3pp', 'category': 'experiment', 'severity': 'critical', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R1-N1+R2(AGREE)', 'note': '共享Wikipedia种子使hold-out生成器gen-0特征向量与训练集gen-0完全一致. 论文已有leak-free binary F1=0.694, 但Abstract/Intro仍以3-class为主展示.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n    {'id': 'R50-N3', 'summary': 'Instruction tuning失效在主文讨论不足——动机与适用范围脱节', 'category': 'framing', 'severity': 'critical', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R2-N2+R1(AGREE with nuance)', 'note': 'Appendix k显示instruct使3-class F1下降3.7-19.9pp. 主文仅一句话量化. R1补充base model场景非零.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n    {'id': 'R50-W1', 'summary': '\\\"Depth profiling\\\"命名暗示超出3-class的精细粒度', 'category': 'framing', 'severity': 'warning', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R2-W1+R1(AGREE)', 'note': '5-class F1仅0.521. Profiling暗示连续或高分辨率深度估计, 实际为3-class粗粒度分类.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n    {'id': 'R50-W2', 'summary': 'Entropy术语全文使用但实际指reference-model NLL (R32-W3复发)', 'category': 'writing', 'severity': 'warning', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R2-W2+R1(AGREE)', 'note': 'Section 3.3有一次澄清但后续全文回归entropy命名. 与R32-W3同类问题, 之前的修复不够彻底.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n    {'id': 'R50-W3', 'summary': 'Entropy_std intermediate (d=0.55)挑战DDR binary partition叙事', 'category': 'framing', 'severity': 'warning', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R1-W5+R2(AGREE)', 'note': 'DDR实际为三组(drifting/intermediate/near-stationary), 但Abstract/Intro简化为二元.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n    {'id': 'R50-W4', 'summary': '3-class F1低于最强baseline但主文未充分讨论', 'category': 'writing', 'severity': 'warning', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R1-W3+R2(AGREE)', 'note': '4-det+surface 0.798 vs 7-feature 0.762. Section 4.3聚焦binary用matches表述, 对3-class劣势轻描淡写.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n    {'id': 'R50-W5', 'summary': 'Stylometry/authorship attribution related work覆盖不足', 'category': 'writing', 'severity': 'warning', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R2-W5+R1(AGREE)', 'note': 'TTR/hapax ratio是计算文体学核心特征, 但论文未讨论depth profiling与authorship attribution的方法论联系.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n]\n\nissues.extend(new_issues)\noutput = yaml.dump(issues, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)\n# Write to temp file for verification\nwith open('/tmp/review_issues_r50.yaml', 'w') as f:\n    f.write(output)\nprint(f'Total issues: {len(issues)}')\nprint(f'Output length: {len(output)} chars')\nprint('YAML written to /tmp/review_issues_r50.yaml')\n\" 2>&1",
  "description": "Generate complete updated review issues YAML",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3 && python3 -c \"\nimport yaml, sys\n\nwith open('projects/gen-depth-fingerprint/artifacts/review_issues.yaml', 'r') as f:\n    issues = yaml.safe_load(f)\n\nissue_map = {i['id']: i for i in issues}\n\n# Update R49 in_progress entries\nupdates = {\n    'R49-MF1': {'last_seen_round': 50, 'mention': {'round': 50, 'reviewers': 'R1-W4+R2(AGREE)', 'note': 'R50重新确认: text-level bootstrap低估generator-level泛化不确定性. 论文已有per-generator SD=0.028但未在CI中突出.'}},\n    'R49-MF2': {'last_seen_round': 50, 'mention': {'round': 50, 'reviewers': 'R2-N1+R1(AGREE)+R2-N2', 'note': 'R50聚焦shape feature causal overclaim: Abstract声称shape enables cross-generator transfer, 但LOFO/PI证据显示shape边际贡献极小. 同时instruction tuning失效未在主文充分讨论.'}},\n    'R49-MF3': {'last_seen_round': 50, 'mention': {'round': 50, 'reviewers': 'R1-N2+R2(AGREE with nuance)', 'note': 'R50确认DDR post-hoc定义问题. holdout generator split validation(Table 35)有效但被埋在附录. R2认为empirical study的post-hoc+cross-validation是合法路径.'}},\n    'R49-MF4': {'mention': {'round': 50, 'reviewers': 'n/a', 'note': 'R50未提及. Discussion已有downstream caveat, 可能已充分处理.'}},\n    'R49-SF1': {'last_seen_round': 50, 'mention': {'round': 50, 'reviewers': 'R1-W1+R2(AGREE)', 'note': 'R50重新确认. 实际影响有限(near-stationary d<0.10远低于阈值), 但应显式引用LOFO结果作为任务内校准证据.'}},\n    'R49-SF2': {'mention': {'round': 50, 'reviewers': 'n/a', 'note': 'R50未提及. 论文已有PCA 92.3% + LOFO讨论, 可能已充分处理.'}},\n    'R49-SF4': {'mention': {'round': 50, 'reviewers': 'n/a', 'note': 'R50 R2-S6确认concurrent work对比清晰(Table 48). 可能已解决.'}},\n    'R49-SF5': {'last_seen_round': 50, 'mention': {'round': 50, 'reviewers': 'R1-W2(raised)+R2(REBUT)', 'note': 'R50分歧: R1认为6-gen vs 8-gen不可比; R2指出Appendix e已有同子集公平对比(0.905 vs 0.789). Director判断R2正确, 但主文呈现应更清晰.'}},\n    'R49-SF6': {'last_seen_round': 50, 'mention': {'round': 50, 'reviewers': 'R1-N1+R2(AGREE)', 'note': 'R50因gen-0泄漏问题使primary metric选择更加重要. 论文已标注binary F1为primary conservative metric, 但Abstract/Intro仍以3-class为主.'}},\n    'R49-SF7': {'mention': {'round': 50, 'reviewers': 'n/a', 'note': 'R50未直接提及.'}},\n    'R49-MR1': {'mention': {'round': 50, 'reviewers': 'n/a', 'note': 'R50未提及. 待确认是否已补入.'}},\n    'R49-MR2': {'mention': {'round': 50, 'reviewers': 'n/a', 'note': 'R50未提及.'}},\n    'R49-MR3': {'last_seen_round': 50, 'mention': {'round': 50, 'reviewers': 'R1-MR', 'note': 'R1提及Krishna et al. (2024) paraphrase attack应在robustness讨论中对比.'}},\n    'R49-MR4': {'mention': {'round': 50, 'reviewers': 'n/a', 'note': 'R50未提及.'}},\n}\n\nfor iid, upd in updates.items():\n    if iid in issue_map:\n        if 'last_seen_round' in upd:\n            issue_map[iid]['last_seen_round'] = upd['last_seen_round']\n        issue_map[iid]['mentions'].append(upd['mention'])\n\n# Add new R50 issues\nnew_issues = [\n    {'id': 'R50-N1', 'summary': 'Shape feature causal overclaim — LOFO/PI证据与Abstract因果声称矛盾', 'category': 'framing', 'severity': 'critical', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R2-N1+R1(AGREE)', 'note': 'Abstract \\\"shape features enable cross-generator depth classification\\\"是因果声明, 但LOFO显示shape边际贡献极小(delta<=1.5pp), PI中near-stationary仅为drifting的18%.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n    {'id': 'R50-N2', 'summary': 'Gen-0种子共享导致LOGO 3-class F1=0.762被高估约3pp', 'category': 'experiment', 'severity': 'critical', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R1-N1+R2(AGREE)', 'note': '共享Wikipedia种子使hold-out生成器gen-0特征向量与训练集gen-0完全一致. 论文已有leak-free binary F1=0.694, 但Abstract/Intro仍以3-class为主展示.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n    {'id': 'R50-N3', 'summary': 'Instruction tuning失效在主文讨论不足——动机与适用范围脱节', 'category': 'framing', 'severity': 'critical', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R2-N2+R1(AGREE with nuance)', 'note': 'Appendix k显示instruct使3-class F1下降3.7-19.9pp. 主文仅一句话量化. R1补充base model场景非零.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n    {'id': 'R50-W1', 'summary': '\\\"Depth profiling\\\"命名暗示超出3-class的精细粒度', 'category': 'framing', 'severity': 'warning', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R2-W1+R1(AGREE)', 'note': '5-class F1仅0.521. Profiling暗示连续或高分辨率深度估计, 实际为3-class粗粒度分类.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n    {'id': 'R50-W2', 'summary': 'Entropy术语全文使用但实际指reference-model NLL (R32-W3复发)', 'category': 'writing', 'severity': 'warning', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R2-W2+R1(AGREE)', 'note': 'Section 3.3有一次澄清但后续全文回归entropy命名. 与R32-W3同类问题, 之前的修复不够彻底.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n    {'id': 'R50-W3', 'summary': 'Entropy_std intermediate (d=0.55)挑战DDR binary partition叙事', 'category': 'framing', 'severity': 'warning', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R1-W5+R2(AGREE)', 'note': 'DDR实际为三组(drifting/intermediate/near-stationary), 但Abstract/Intro简化为二元.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n    {'id': 'R50-W4', 'summary': '3-class F1低于最强baseline但主文未充分讨论', 'category': 'writing', 'severity': 'warning', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R1-W3+R2(AGREE)', 'note': '4-det+surface 0.798 vs 7-feature 0.762. Section 4.3聚焦binary用matches表述, 对3-class劣势轻描淡写.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n    {'id': 'R50-W5', 'summary': 'Stylometry/authorship attribution related work覆盖不足', 'category': 'writing', 'severity': 'warning', 'status': 'open', 'first_raised_round': 50, 'last_seen_round': 50, 'mentions': [{'round': 50, 'reviewers': 'R2-W5+R1(AGREE)', 'note': 'TTR/hapax ratio是计算文体学核心特征, 但论文未讨论depth profiling与authorship attribution的方法论联系.'}], 'action_items': [], 'resolution': '', 'resolution_round': None},\n]\n\nissues.extend(new_issues)\noutput = yaml.dump(issues, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)\n# Write to temp file for verification\nwith open('/tmp/review_issues_r50.yaml', 'w') as f:\n    f.write(output)\nprint(f'Total issues: {len(issues)}')\nprint(f'Output length: {len(output)} chars')\nprint('YAML written to /tmp/review_issues_r50.yaml')\n\" 2>&1",
    "description": "Generate complete updated review issues YAML",
    "timeout": "30000"
  }
}
```

</details>

---


### Tool result

_source line 3921 · 2026-05-23T01:58:43.915881+00:00_

Total issues: 96
Output length: 32244 chars
YAML written to /tmp/review_issues_r50.yaml
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_director_fec00603

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 3922 · 2026-05-23T01:58:46.876765+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /tmp/review_issues_r50.yaml",
  "description": "Read generated YAML for submission",
  "timeout": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /tmp/review_issues_r50.yaml",
    "description": "Read generated YAML for submission",
    "timeout": "10000"
  }
}
```

</details>

---


### Tool result

_source line 3923 · 2026-05-23T01:58:46.927815+00:00_

&lt;persisted-output>
Output too large (34.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-director-fec00603/7a7cf8b4-32d5-4793-adb2-fcad14792012/tool-results/b3fnwc5yi.txt

Preview (first 2KB):
- id: R29-N1
  summary: Base-model-only scope 未在 Abstract 标注
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 32
  resolution: Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented.
  resolution_round: 32
- id: R29-N2
  summary: Downstream TOST underpowered (n=3) + Abstract overclaim
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 34
  resolution: Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料.
  resolution_round: 34
- id: R29-N3
  summary: DDR 新颖性 incremental — 缺 concurrent work 系统对比表
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 31
  resolution: related_work.tex concurrent-comparison table added
  resolution_round: 31
- id: R29-N4
  summary: QLoRA gap 削弱方法论贡献 — 需重定位
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 29
  last_seen_round: 34
  resolution: Intro L14 'proof of concept'; Contribution 3 'Proof-of-concept classifier with boundary analysis'.
  resolution_round: 34
- id: R29-W1
  summary: Gemma-2-2B gen-1 F1=0.036 anomaly 解释不充分
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 29
  last_seen_round: 31
  resolution: appendix_9gen_scale expanded
  resolution_round: 31
- id: R29-W2
  summary: Cross-model chain F1=0.830 可能混淆 depth signal 与 generator identity
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 29
  last_seen_round: 34
  resolution: results.tex footnote + L15 single-gen tr
…[truncated 327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 3924 · 2026-05-23T01:59:05.398969+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_issues_r50.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_issues_r50.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3925 · 2026-05-23T01:59:05.651019+00:00_

1	- id: R29-N1
2	  summary: Base-model-only scope 未在 Abstract 标注
3	  category: framing
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 29
7	  last_seen_round: 32
8	  resolution: Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented.
9	  resolution_round: 32
10	- id: R29-N2
11	  summary: Downstream TOST underpowered (n=3) + Abstract overclaim
12	  category: experiment
13	  severity: critical
14	  status: resolved
15	  first_raised_round: 29
16	  last_seen_round: 34
17	  resolution: Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料.
18	  resolution_round: 34
19	- id: R29-N3
20	  summary: DDR 新颖性 incremental — 缺 concurrent work 系统对比表
21	  category: framing
22	  severity: critical
23	  status: resolved
24	  first_raised_round: 29
25	  last_seen_round: 31
26	  resolution: related_work.tex concurrent-comparison table added
27	  resolution_round: 31
28	- id: R29-N4
29	  summary: QLoRA gap 削弱方法论贡献 — 需重定位
30	  category: framing
31	  severity: warning
32	  status: resolved
33	  first_raised_round: 29
34	  last_seen_round: 34
35	  resolution: Intro L14 'proof of concept'; Contribution 3 'Proof-of-concept classifier with boundary analysis'.
36	  resolution_round: 34
37	- id: R29-W1
38	  summary: Gemma-2-2B gen-1 F1=0.036 anomaly 解释不充分
39	  category: experiment
40	  severity: warning
41	  status: resolved
42	  first_raised_round: 29
43	  last_seen_round: 31
44	  resolution: appendix_9gen_scale expanded
45	  resolution_round: 31
46	- id: R29-W2
47	  summary: Cross-model chain F1=0.830 可能混淆 depth signal 与 generator identity
48	  category: experiment
49	  severity: warning
50	  status: resolved
51	  first_raised_round: 29
52	  last_seen_round: 34
53	  resolution: results.tex footnote + L15 single-gen transfer. Caveats sufficient.
54	  resolution_round: 34
55	- id: R29-W3
56	  summary: 温度限制(t<0.9)未在 Abstract 标注
57	  category: framing
58	  severity: warning
59	  stat
…[truncated 34547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 3926 · 2026-05-23T01:59:28.287495+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /tmp/review_issues_r50.yaml | wc -c",
  "description": "Verify YAML size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /tmp/review_issues_r50.yaml | wc -c",
    "description": "Verify YAML size"
  }
}
```

</details>

---


### Tool result

_source line 3927 · 2026-05-23T01:59:28.338142+00:00_

35290

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3928 · 2026-05-23T01:59:45.341769+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3 && python3 -c \"\nwith open('/tmp/review_issues_r50.yaml', 'r') as f:\n    content = f.read()\nprint(content[:100])\nprint('...')\nprint(f'Total length: {len(content)}')\n\" 2>&1",
  "description": "Verify YAML content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3 && python3 -c \"\nwith open('/tmp/review_issues_r50.yaml', 'r') as f:\n    content = f.read()\nprint(content[:100])\nprint('...')\nprint(f'Total length: {len(content)}')\n\" 2>&1",
    "description": "Verify YAML content"
  }
}
```

</details>

---


### Tool result

_source line 3929 · 2026-05-23T01:59:45.442563+00:00_

- id: R29-N1
  summary: Base-model-only scope 未在 Abstract 标注
  category: framing
  severity: critica
...
Total length: 32244
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_director_fec00603

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3930 · 2026-05-23T01:59:51.364767+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /tmp/review_issues_r50.yaml",
  "description": "Read full YAML for MCP tool submission",
  "timeout": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /tmp/review_issues_r50.yaml",
    "description": "Read full YAML for MCP tool submission",
    "timeout": "10000"
  }
}
```

</details>

---


### Tool result

_source line 3931 · 2026-05-23T01:59:51.415794+00:00_

&lt;persisted-output>
Output too large (34.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-director-fec00603/7a7cf8b4-32d5-4793-adb2-fcad14792012/tool-results/bogvdvbr9.txt

Preview (first 2KB):
- id: R29-N1
  summary: Base-model-only scope 未在 Abstract 标注
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 32
  resolution: Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented.
  resolution_round: 32
- id: R29-N2
  summary: Downstream TOST underpowered (n=3) + Abstract overclaim
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 34
  resolution: Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料.
  resolution_round: 34
- id: R29-N3
  summary: DDR 新颖性 incremental — 缺 concurrent work 系统对比表
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 31
  resolution: related_work.tex concurrent-comparison table added
  resolution_round: 31
- id: R29-N4
  summary: QLoRA gap 削弱方法论贡献 — 需重定位
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 29
  last_seen_round: 34
  resolution: Intro L14 'proof of concept'; Contribution 3 'Proof-of-concept classifier with boundary analysis'.
  resolution_round: 34
- id: R29-W1
  summary: Gemma-2-2B gen-1 F1=0.036 anomaly 解释不充分
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 29
  last_seen_round: 31
  resolution: appendix_9gen_scale expanded
  resolution_round: 31
- id: R29-W2
  summary: Cross-model chain F1=0.830 可能混淆 depth signal 与 generator identity
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 29
  last_seen_round: 34
  resolution: results.tex footnote + L15 single-gen tr
…[truncated 327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 3932 · 2026-05-23T02:00:16.477837+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cp /tmp/review_issues_r50.yaml /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml && echo \"COPIED\" && python3 -c \"import yaml; data=yaml.safe_load(open('/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml')); print(f'Valid YAML: {len(data)} issues'); new=[i for i in data if i['id'].startswith('R50')]; print(f'R50 new issues: {len(new)}'); updated=[i for i in data if i['id'].startswith('R49') and any(m.get('round')==50 for m in i.get('mentions',[]))]; print(f'R49 issues updated with R50 mentions: {len(updated)}')\"",
  "description": "Copy updated YAML to target location and verify"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cp /tmp/review_issues_r50.yaml /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml && echo \"COPIED\" && python3 -c \"import yaml; data=yaml.safe_load(open('/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml')); print(f'Valid YAML: {len(data)} issues'); new=[i for i in data if i['id'].startswith('R50')]; print(f'R50 new issues: {len(new)}'); updated=[i for i in data if i['id'].startswith('R49') and any(m.get('round')==50 for m in i.get('mentions',[]))]; print(f'R49 issues updated with R50 mentions: {len(updated)}')\"",
    "description": "Copy updated YAML to target location and verify"
  }
}
```

</details>

---


### Tool result

_source line 3933 · 2026-05-23T02:00:16.678963+00:00_

COPIED
Valid YAML: 96 issues
R50 new issues: 8
R49 issues updated with R50 mentions: 14

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 3934 · 2026-05-23T02:02:50.789092+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 50 (Fresh Review)\n## gen-depth-fingerprint → EMNLP 2026 (ARR)\n\n**Reviewers**: R1 (方法严谨性+实验设计) + R2 (新颖性+完整性)\n**交叉回应**: 完成。关键问题共识充分，2处轻微分歧已记录。\n**视觉审查**: 完成（0 critical, 2 warning, 9 info）。\n**外部审稿**: 未配置。\n\n---\n\n## Summary\n\n论文提出 *depth profiling*——将文本按递归生成深度（gen-0/gen-1/gen-2+）进行序数分类，并通过分解 NLL 分布的 location drift 与 shape stability 发现了 *differential depth response* (DDR) 这一实证规律。实验覆盖 8 个 base-model 生成器（5 个架构家族，0.6B-8B），使用 LOGO 交叉验证，leak-free binary F1=0.694，3-class F1=0.762。附录 28 页包含大量消融和鲁棒性分析。\n\n---\n\n## Strengths\n\n**S1** [consensus] **任务定义新颖且有意义**——从 binary human/machine 检测扩展到 ordinal depth classification，对数据溯源和语料审计具有直接价值。两位 Reviewer 均将此列为首要优势。\n\n**S2** [consensus] **实验覆盖面广且控制严格**——8 个生成器×5 个架构家族，LOGO 交叉验证，加上长度控制、独立种子验证 (F1=0.680)、参考模型鲁棒性 (F1 spread=0.013)、跨温度/跨域/跨解码策略验证等大量控制实验。28 页附录体现了对方法局限的深入认识。\n\n**S3** [consensus] **DDR 分解提供了可解释的分析框架**——location drift vs. shape stability 的分解不仅服务于分类，也是对递归生成如何改变文本分布的结构化理解。Cohen's d、TOST、bootstrap stability 等统计刻画严谨。\n\n**S4** [consensus] **轻量级且可部署**——仅需单个 410M 参考模型和 7 个可解释标量特征，无需 GPU 推理或专用检测器，具备实际部署可行性。\n\n**S5** [consensus] **对 limitations 的诚实报告**——base-model-only scope、instruction tuning 失败、3-class ceiling、English-only、fixed decoding 均被明确披露。\n\n**S6** [R2] **与 concurrent work 的对比清晰**——Table 48（Appendix）将本文与 Mohamed et al. (2025) 和 Geng et al. (2026) 进行了详细的维度对比。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical; R2-N1 raised, R1 AGREE] **Shape feature \"enables\" cross-generator transfer 的因果声称缺乏直接证据**\n- Abstract 声称 \"shape features provide a cross-generator reference that enables coarse ordinal depth classification\"——这是因果声明。\n- LOFO 分析（Appendix f, Table 8/9）显示 shape features 边际贡献极小：entropy_min Δ=−1.5pp, tail_decay Δ=−0.8pp, entropy_max Δ=+0.1pp。\n- Permutation Importance 中 near-stationary 平均重要性仅为 drifting 的 18%（0.034 vs. 0.187）。\n- XGBoost 中跨深度近似恒定的特征不会获得有意义的分裂节点；如果它按生成器变化，反而充当生成器判别器——与\"cross-generator reference\"是相反机制。\n- **R1 补充**：论文可能想表达 shape features 的稳定性作为归纳偏置（inductive bias），但此论点未被显式提出或验证。\n- **建议**：(a) 提供消融实验（如仅用 3 个 drifting 特征 vs 全部 7 个的 LOGO F1 对比）验证因果关系，或 (b) 将声称从因果性降级为描述性观察。\n\n**MF2** [critical; R1-N1 raised, R2 AGREE] **Gen-0 种子共享在 LOGO 评估中造成 train-test 信息泄漏，3-class F1=0.762 被高估约 3pp**\n- ~1,000 条共享 Wikipedia 种子跨全部 8 个生成器。LOGO hold-out 时，被测生成器的 gen-0 特征向量与训练集 gen-0 完全一致。Appendix confusion matrix 报告 gen-0 准确率 ~99.4%。\n- 论文已有缓解：(a) Section 3.2 承认泄漏，(b) 提供 leak-free binary F1=0.694，(c) 标注 binary F1 为 \"primary conservative metric\"。\n- **R2 补充**：即使高估 3pp，核心 DDR 分析基于 per-feature Cohen's d，不依赖分类器性能。Binary F1=0.694 是 leak-free 的。\n- **建议**：(a) 将 binary F1 升格为并列主指标（Abstract/Table 2 同等强调），或 (b) 补充不相交种子池的 3-class 评估。\n\n**MF3** [critical; R1-N2 raised, R2 AGREE with nuance] **DDR 分区的事后定义缺乏前置理论驱动**\n- DDR 分区通过观察 7 个特征在 (|ρ|, d) 空间后事后定义。k-means 验证使用同一数据存在弱循环。\n- **缓解因素**（R2 强调）：(a) Holdout generator split validation (Table 35, Δ(d)≤0.05)——最有力证据但被埋在附录；(b) Per-generator replication——每个生成器独立复现相同分区；(c) Threshold robustness——分区在 ε∈[0.10, 0.75] 范围内稳定。\n- R2 认为对于 empirical study，post-hoc observation + rigorous cross-validation 是合法研究路径。\n- **建议**：将 Table 35 holdout split validation 提升至主文 Section 4.2。\n\n**MF4** [critical; R2-N2 raised, R1 AGREE with nuance] **Instruction tuning 失效是主要实用性限制，主文讨论不足**\n- Appendix k 显示 instruction tuning 使 3-class F1 下降 3.7-19.9pp，DDR 结构被根本性改变。\n- 主文 Limitations 仅一句话量化。Section 5 (Discussion) 完全未提及。\n- 论文动机（\"data provenance, contamination monitoring\"）与 base-model-only 适用范围存在脱节。\n- **R1 补充**：base model 场景非零（训练数据合成、model collapse monitoring、pre-training contamination detection），不应完全否定方法的实用价值。\n- **建议**：Discussion 增加段落（~150词）讨论 instruction tuning 影响并显式界定适用范围。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning; R2-W1 + R1 AGREE] **\"Depth profiling\" 命名暗示超出实际能力的精细粒度**\n- 5-class F1 仅 0.521 (Appendix d)，实际为 3-class 粗粒度分类。建议在标题/摘要中使用更精确表述，或首次使用时限定含义。\n\n**SF2** [warning; R2-W2 + R1 AGREE] **\"Entropy\" 术语贯穿全文但实际指 reference-model NLL**\n- Section 3.3 和 Table 1 有一次澄清，但全文所有表格/图表继续使用 \"entropy\"。R32-W3 同类问题在之前修复不够彻底。建议在关键位置统一使用 \"reference-model NLL\" 或 \"cross-entropy\"。\n\n**SF3** [warning; R1-W5 + R2 AGREE] **Entropy_std 的 \"intermediate\" 地位 (d=0.55) 挑战 DDR 的 binary partition 叙事**\n- DDR 实际为三组结构 (drifting/intermediate/near-stationary)，但 Abstract/Introduction 简化为二元叙事 (\"location vs. shape\")。建议从顶层叙事开始承认三组结构。\n\n**SF4** [warning; R1-W1 + R2 AGREE] **TOST 等价性边界 |d|≤0.20 缺乏任务特异性校准**\n- ε=0.20 来自 Cohen (1988) 社会科学惯例。实际影响有限（near-stationary 特征实际 d<0.10，远低于阈值；分区在 ε∈[0.10, 0.75] 完全稳定）。建议显式引用 LOFO 结果作为任务内校准证据。\n\n**SF5** [warning; R1-W3 + R2 AGREE] **3-class F1 低于最强 baseline (4-det+surface 0.798 vs 0.762) 但主文未充分讨论**\n- Section 4.3 聚焦 binary 比较用 \"matches\" 表述，对 3-class 劣势轻描淡写。建议明确量化效率-性能权衡（单一 410M reference vs 多模型推理）。\n\n**SF6** [warning; R1-W4 + R2 AGREE] **Bootstrap CI 的重采样单位是文本级别，可能低估生成器级泛化不确定性**\n- 论文已有 per-generator binary F1 分布（SD=0.028, IQR=[0.692, 0.714]），但未在 CI 报告中突出。建议补充 LOGO fold 级别的 mean±std 作为 generator-level uncertainty 的主要度量。\n\n**SF7** [warning; R2-W5 + R1 AGREE] **Related work 在 stylometry/authorship attribution 方向覆盖不足**\n- TTR/hapax ratio 是计算文体学核心特征（Stamatatos, 2009），但论文未讨论 depth profiling 与 authorship attribution 的方法论联系。\n\n### Director 更正\n\n**DC1** [R2-W4 \"跨 family 泛化未被显式测试\" — 论文已有 LOFO 结果]\n- 两位 Reviewer 均认为论文缺乏 leave-one-family-out 测试。但论文 **Table 2 底行** 和 **Section 3.4** 明确报告了 LOFO binary F1=0.686（\"LOGO does not isolate family-level effects; Leave-One-Family-Out (LOFO) addresses this by holding out entire model families\"；\"holding out all three Qwen models (F1=0.686) provides the strictest family-level test\"）。\n- 此 should-fix 已被论文解决。两位 Reviewer 均未注意到，说明 LOFO 结果可更突出呈现。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识（均 [AGREE]）：\n\n1. **Shape feature 因果声称需弱化** (MF1)：LOFO/PI 证据直接矛盾\n2. **Gen-0 泄漏真实存在** (MF2)：论文有部分缓解但主指标仍被高估\n3. **DDR post-hoc 定义需加强呈现** (MF3)：holdout validation 有效但被埋在附录\n4. **Instruction tuning 讨论不足** (MF4)：base model 场景非零但主文需界定适用范围\n5. **Entropy 术语问题** (SF2)：与 R32-W3 同类，需更彻底修复\n6. **Entropy_std 三组结构** (SF3)：顶层叙事应与实际分区一致\n7. **Bootstrap CI 层级** (SF6)：应补充 generator-level 不确定性\n8. **Stylometry related work** (SF7)：自然关联方向缺失\n\n## Reviewer Divergence\n\n**DIV1: Contribution #2 的表述——描述性观察 vs 分析贡献**\n- R2 认为 DDR 仅是描述性观察，\"enables\" 表述混淆了观察与方法。\n- R1 反驳：DDR 分区具有独立分析价值（holdout validation、k-means、TOST、跨温度/跨域一致性），但同意措辞应更精确。\n- **Director 判断**：DDR 的分析价值超出纯描述性观察，但措辞需修订为 \"empirical regularity with analytical utility\"。\n\n**DIV2: QLoRA 与 XGBoost 的比较基础**\n- R1 认为 6-gen QLoRA vs 8-gen XGBoost 不可比。\n- R2 反驳：Appendix e 已提供同子集公平对比 (0.905 vs 0.789)，+11.6pp 在公平条件下测量。\n- **Director 判断**：同意 R2——同子集对比已存在，但主文呈现应更清晰。\n\n---\n\n## Questions for Authors\n\n1. 能否设计消融实验（如人工打乱 shape features 或仅用 3 个 drifting 特征训练）直接验证 shape features 在跨生成器泛化中的因果作用？\n2. 能否提供使用不相交种子池的 3-class LOGO F1 以量化 gen-0 泄漏？\n3. QLoRA 在完整 8-gen 上的 LOGO F1？\n4. Instruction tuning 下如果直接在 instruct chain data 上训练分类器，信号能否恢复？\n5. DDR 分解在 >8B 模型上是否成立？\n\n## Missing References\n\n- **Stamatatos, E. (2009).** A survey of modern authorship attribution methods. *JASIST* — 与 TTR/hapax ratio 特征直接相关的基础综述 [R2+R1 AGREE]\n- **Krishna et al. (2024).** Paraphrasing evades detectors — paraphrase attack robustness [R1]\n- Ordinal regression/classification 更广泛的文献覆盖 [R2]\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置/未请求。\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 9 info）：\n- **[warning]** p.14: Figure 5（7个 violin 子图）占整页约 90% 面积，空间效率偏低。建议调整布局。\n- **[warning]** p.36: 最后一页底部约 30% 空白。\n- **[info]** 主文 8 页含 4 figures + 3 tables = 7 个 display items，密度合理（~0.88/页）。所有 float 在首次引用附近。无 margin 溢出或未解析引用。\n- **[info]** p.7: Figure 3/4 部分标注字号偏小（正文的 60-65%），建议放大。\n- **[info]** 页面合规：主文 8 页，Limitations 不计入页数限制，格式合规。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3.0/5 | 3.25/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n两位 Reviewer 独立给出 3.5 分。论文在一个有新意的任务（depth profiling）上提供了全面系统的实证分析，DDR 分解具有真实的分析价值，实验覆盖面在 empirical study 中属于上乘。\n\n**核心问题均为 framing/presentation 性质**（非实验设计缺陷），具体为：\n1. Shape feature 的因果声称需弱化为描述性观察\n2. 3-class F1 的 gen-0 泄漏需在主指标呈现中解决\n3. DDR holdout validation 需从附录提升至主文\n4. Instruction tuning 失效需在 Discussion 显式讨论\n\n如果上述 4 个 Must-Fix 在修订中得到充分解决（均为文字修改，不需要新实验），论文有望达到 Conference (4.0) 水平。核心实证发现——DDR 分解、跨生成器泛化、大量控制实验——是扎实的。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"shape features provide a cross-generator reference that **enables**...\" → 弱化因果措辞 [MF1]\n- 3-class F1=0.762 和 binary F1=0.694 应并列呈现并注明 3-class 受 gen-0 共享影响 [MF2]\n\n### Introduction\n- Contribution #1 应将 DDR 定位为 \"empirical regularity with analytical utility\" [DIV1]\n- 应在 base-model scope 前置说明处更早限定 [MF4]\n\n### Section 3.2 (Generation Chain)\n- Seed sharing 的 leakage 讨论已有，但量化不足 [MF2]\n\n### Section 4.1 (Classification Performance)\n- \"our primary conservative metric\" 已标注 binary F1，但 Abstract/Intro 仍以 3-class 为主 [MF2]\n- 补充 per-generator fold-level mean±std [SF6]\n\n### Section 4.2 (DDR)\n- 将 Table 35 holdout split validation 从附录提升至此处 [MF3]\n- Entropy_std 的三组结构应在此处明确呈现 [SF3]\n- Cohen's d 阈值选择应连接 LOFO 结果 [SF4]\n\n### Section 4.3 (Baselines)\n- \"matches multi-detector ensembles\" 表述需附加 3-class F1 差距的诚实讨论 [SF5]\n\n### Section 5 (Discussion)\n- 增加 instruction tuning 影响段落（~150 词），界定方法适用范围 [MF4]\n- Shape features 的贡献定位需修订 [MF1]\n\n### Section 2 (Related Work)\n- 补充 stylometry/authorship attribution 方向讨论 [SF7]\n\n### Limitations\n- 已较全面，可加强 instruction tuning 失效的原因分析",
  "project": "gen-depth-fingerprint",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 50 (Fresh Review)\n## gen-depth-fingerprint → EMNLP 2026 (ARR)\n\n**Reviewers**: R1 (方法严谨性+实验设计) + R2 (新颖性+完整性)\n**交叉回应**: 完成。关键问题共识充分，2处轻微分歧已记录。\n**视觉审查**: 完成（0 critical, 2 warning, 9 info）。\n**外部审稿**: 未配置。\n\n---\n\n## Summary\n\n论文提出 *depth profiling*——将文本按递归生成深度（gen-0/gen-1/gen-2+）进行序数分类，并通过分解 NLL 分布的 location drift 与 shape stability 发现了 *differential depth response* (DDR) 这一实证规律。实验覆盖 8 个 base-model 生成器（5 个架构家族，0.6B-8B），使用 LOGO 交叉验证，leak-free binary F1=0.694，3-class F1=0.762。附录 28 页包含大量消融和鲁棒性分析。\n\n---\n\n## Strengths\n\n**S1** [consensus] **任务定义新颖且有意义**——从 binary human/machine 检测扩展到 ordinal depth classification，对数据溯源和语料审计具有直接价值。两位 Reviewer 均将此列为首要优势。\n\n**S2** [consensus] **实验覆盖面广且控制严格**——8 个生成器×5 个架构家族，LOGO 交叉验证，加上长度控制、独立种子验证 (F1=0.680)、参考模型鲁棒性 (F1 spread=0.013)、跨温度/跨域/跨解码策略验证等大量控制实验。28 页附录体现了对方法局限的深入认识。\n\n**S3** [consensus] **DDR 分解提供了可解释的分析框架**——location drift vs. shape stability 的分解不仅服务于分类，也是对递归生成如何改变文本分布的结构化理解。Cohen's d、TOST、bootstrap stability 等统计刻画严谨。\n\n**S4** [consensus] **轻量级且可部署**——仅需单个 410M 参考模型和 7 个可解释标量特征，无需 GPU 推理或专用检测器，具备实际部署可行性。\n\n**S5** [consensus] **对 limitations 的诚实报告**——base-model-only scope、instruction tuning 失败、3-class ceiling、English-only、fixed decoding 均被明确披露。\n\n**S6** [R2] **与 concurrent work 的对比清晰**——Table 48（Appendix）将本文与 Mohamed et al. (2025) 和 Geng et al. (2026) 进行了详细的维度对比。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical; R2-N1 raised, R1 AGREE] **Shape feature \"enables\" cross-generator transfer 的因果声称缺乏直接证据**\n- Abstract 声称 \"shape features provide a cross-generator reference that enables coarse ordinal depth classification\"——这是因果声明。\n- LOFO 分析（Appendix f, Table 8/9）显示 shape features 边际贡献极小：entropy_min Δ=−1.5pp, tail_decay Δ=−0.8pp, entropy_max Δ=+0.1pp。\n- Permutation Importance 中 near-stationary 平均重要性仅为 drifting 的 18%（0.034 vs. 0.187）。\n- XGBoost 中跨深度近似恒定的特征不会获得有意义的分裂节点；如果它按生成器变化，反而充当生成器判别器——与\"cross-generator reference\"是相反机制。\n- **R1 补充**：论文可能想表达 shape features 的稳定性作为归纳偏置（inductive bias），但此论点未被显式提出或验证。\n- **建议**：(a) 提供消融实验（如仅用 3 个 drifting 特征 vs 全部 7 个的 LOGO F1 对比）验证因果关系，或 (b) 将声称从因果性降级为描述性观察。\n\n**MF2** [critical; R1-N1 raised, R2 AGREE] **Gen-0 种子共享在 LOGO 评估中造成 train-test 信息泄漏，3-class F1=0.762 被高估约 3pp**\n- ~1,000 条共享 Wikipedia 种子跨全部 8 个生成器。LOGO hold-out 时，被测生成器的 gen-0 特征向量与训练集 gen-0 完全一致。Appendix confusion matrix 报告 gen-0 准确率 ~99.4%。\n- 论文已有缓解：(a) Section 3.2 承认泄漏，(b) 提供 leak-free binary F1=0.694，(c) 标注 binary F1 为 \"primary conservative metric\"。\n- **R2 补充**：即使高估 3pp，核心 DDR 分析基于 per-feature Cohen's d，不依赖分类器性能。Binary F1=0.694 是 leak-free 的。\n- **建议**：(a) 将 binary F1 升格为并列主指标（Abstract/Table 2 同等强调），或 (b) 补充不相交种子池的 3-class 评估。\n\n**MF3** [critical; R1-N2 raised, R2 AGREE with nuance] **DDR 分区的事后定义缺乏前置理论驱动**\n- DDR 分区通过观察 7 个特征在 (|ρ|, d) 空间后事后定义。k-means 验证使用同一数据存在弱循环。\n- **缓解因素**（R2 强调）：(a) Holdout generator split validation (Table 35, Δ(d)≤0.05)——最有力证据但被埋在附录；(b) Per-generator replication——每个生成器独立复现相同分区；(c) Threshold robustness——分区在 ε∈[0.10, 0.75] 范围内稳定。\n- R2 认为对于 empirical study，post-hoc observation + rigorous cross-validation 是合法研究路径。\n- **建议**：将 Table 35 holdout split validation 提升至主文 Section 4.2。\n\n**MF4** [critical; R2-N2 raised, R1 AGREE with nuance] **Instruction tuning 失效是主要实用性限制，主文讨论不足**\n- Appendix k 显示 instruction tuning 使 3-class F1 下降 3.7-19.9pp，DDR 结构被根本性改变。\n- 主文 Limitations 仅一句话量化。Section 5 (Discussion) 完全未提及。\n- 论文动机（\"data provenance, contamination monitoring\"）与 base-model-only 适用范围存在脱节。\n- **R1 补充**：base model 场景非零（训练数据合成、model collapse monitoring、pre-training contamination detection），不应完全否定方法的实用价值。\n- **建议**：Discussion 增加段落（~150词）讨论 instruction tuning 影响并显式界定适用范围。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning; R2-W1 + R1 AGREE] **\"Depth profiling\" 命名暗示超出实际能力的精细粒度**\n- 5-class F1 仅 0.521 (Appendix d)，实际为 3-class 粗粒度分类。建议在标题/摘要中使用更精确表述，或首次使用时限定含义。\n\n**SF2** [warning; R2-W2 + R1 AGREE] **\"Entropy\" 术语贯穿全文但实际指 reference-model NLL**\n- Section 3.3 和 Table 1 有一次澄清，但全文所有表格/图表继续使用 \"entropy\"。R32-W3 同类问题在之前修复不够彻底。建议在关键位置统一使用 \"reference-model NLL\" 或 \"cross-entropy\"。\n\n**SF3** [warning; R1-W5 + R2 AGREE] **Entropy_std 的 \"intermediate\" 地位 (d=0.55) 挑战 DDR 的 binary partition 叙事**\n- DDR 实际为三组结构 (drifting/intermediate/near-stationary)，但 Abstract/Introduction 简化为二元叙事 (\"location vs. shape\")。建议从顶层叙事开始承认三组结构。\n\n**SF4** [warning; R1-W1 + R2 AGREE] **TOST 等价性边界 |d|≤0.20 缺乏任务特异性校准**\n- ε=0.20 来自 Cohen (1988) 社会科学惯例。实际影响有限（near-stationary 特征实际 d<0.10，远低于阈值；分区在 ε∈[0.10, 0.75] 完全稳定）。建议显式引用 LOFO 结果作为任务内校准证据。\n\n**SF5** [warning; R1-W3 + R2 AGREE] **3-class F1 低于最强 baseline (4-det+surface 0.798 vs 0.762) 但主文未充分讨论**\n- Section 4.3 聚焦 binary 比较用 \"matches\" 表述，对 3-class 劣势轻描淡写。建议明确量化效率-性能权衡（单一 410M reference vs 多模型推理）。\n\n**SF6** [warning; R1-W4 + R2 AGREE] **Bootstrap CI 的重采样单位是文本级别，可能低估生成器级泛化不确定性**\n- 论文已有 per-generator binary F1 分布（SD=0.028, IQR=[0.692, 0.714]），但未在 CI 报告中突出。建议补充 LOGO fold 级别的 mean±std 作为 generator-level uncertainty 的主要度量。\n\n**SF7** [warning; R2-W5 + R1 AGREE] **Related work 在 stylometry/authorship attribution 方向覆盖不足**\n- TTR/hapax ratio 是计算文体学核心特征（Stamatatos, 2009），但论文未讨论 depth profiling 与 authorship attribution 的方法论联系。\n\n### Director 更正\n\n**DC1** [R2-W4 \"跨 family 泛化未被显式测试\" — 论文已有 LOFO 结果]\n- 两位 Reviewer 均认为论文缺乏 leave-one-family-out 测试。但论文 **Table 2 底行** 和 **Section 3.4** 明确报告了 LOFO binary F1=0.686（\"LOGO does not isolate family-level effects; Leave-One-Family-Out (LOFO) addresses this by holding out entire model families\"；\"holding out all three Qwen models (F1=0.686) provides the strictest family-level test\"）。\n- 此 should-fix 已被论文解决。两位 Reviewer 均未注意到，说明 LOFO 结果可更突出呈现。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识（均 [AGREE]）：\n\n1. **Shape feature 因果声称需弱化** (MF1)：LOFO/PI 证据直接矛盾\n2. **Gen-0 泄漏真实存在** (MF2)：论文有部分缓解但主指标仍被高估\n3. **DDR post-hoc 定义需加强呈现** (MF3)：holdout validation 有效但被埋在附录\n4. **Instruction tuning 讨论不足** (MF4)：base model 场景非零但主文需界定适用范围\n5. **Entropy 术语问题** (SF2)：与 R32-W3 同类，需更彻底修复\n6. **Entropy_std 三组结构** (SF3)：顶层叙事应与实际分区一致\n7. **Bootstrap CI 层级** (SF6)：应补充 generator-level 不确定性\n8. **Stylometry related work** (SF7)：自然关联方向缺失\n\n## Reviewer Divergence\n\n**DIV1: Contribution #2 的表述——描述性观察 vs 分析贡献**\n- R2 认为 DDR 仅是描述性观察，\"enables\" 表述混淆了观察与方法。\n- R1 反驳：DDR 分区具有独立分析价值（holdout validation、k-means、TOST、跨温度/跨域一致性），但同意措辞应更精确。\n- **Director 判断**：DDR 的分析价值超出纯描述性观察，但措辞需修订为 \"empirical regularity with analytical utility\"。\n\n**DIV2: QLoRA 与 XGBoost 的比较基础**\n- R1 认为 6-gen QLoRA vs 8-gen XGBoost 不可比。\n- R2 反驳：Appendix e 已提供同子集公平对比 (0.905 vs 0.789)，+11.6pp 在公平条件下测量。\n- **Director 判断**：同意 R2——同子集对比已存在，但主文呈现应更清晰。\n\n---\n\n## Questions for Authors\n\n1. 能否设计消融实验（如人工打乱 shape features 或仅用 3 个 drifting 特征训练）直接验证 shape features 在跨生成器泛化中的因果作用？\n2. 能否提供使用不相交种子池的 3-class LOGO F1 以量化 gen-0 泄漏？\n3. QLoRA 在完整 8-gen 上的 LOGO F1？\n4. Instruction tuning 下如果直接在 instruct chain data 上训练分类器，信号能否恢复？\n5. DDR 分解在 >8B 模型上是否成立？\n\n## Missing References\n\n- **Stamatatos, E. (2009).** A survey of modern authorship attribution methods. *JASIST* — 与 TTR/hapax ratio 特征直接相关的基础综述 [R2+R1 AGREE]\n- **Krishna et al. (2024).** Paraphrasing evades detectors — paraphrase attack robustness [R1]\n- Ordinal regression/classification 更广泛的文献覆盖 [R2]\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置/未请求。\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 9 info）：\n- **[warning]** p.14: Figure 5（7个 violin 子图）占整页约 90% 面积，空间效率偏低。建议调整布局。\n- **[warning]** p.36: 最后一页底部约 30% 空白。\n- **[info]** 主文 8 页含 4 figures + 3 tables = 7 个 display items，密度合理（~0.88/页）。所有 float 在首次引用附近。无 margin 溢出或未解析引用。\n- **[info]** p.7: Figure 3/4 部分标注字号偏小（正文的 60-65%），建议放大。\n- **[info]** 页面合规：主文 8 页，Limitations 不计入页数限制，格式合规。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3.0/5 | 3.25/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n两位 Reviewer 独立给出 3.5 分。论文在一个有新意的任务（depth profiling）上提供了全面系统的实证分析，DDR 分解具有真实的分析价值，实验覆盖面在 empirical study 中属于上乘。\n\n**核心问题均为 framing/presentation 性质**（非实验设计缺陷），具体为：\n1. Shape feature 的因果声称需弱化为描述性观察\n2. 3-class F1 的 gen-0 泄漏需在主指标呈现中解决\n3. DDR holdout validation 需从附录提升至主文\n4. Instruction tuning 失效需在 Discussion 显式讨论\n\n如果上述 4 个 Must-Fix 在修订中得到充分解决（均为文字修改，不需要新实验），论文有望达到 Conference (4.0) 水平。核心实证发现——DDR 分解、跨生成器泛化、大量控制实验——是扎实的。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"shape features provide a cross-generator reference that **enables**...\" → 弱化因果措辞 [MF1]\n- 3-class F1=0.762 和 binary F1=0.694 应并列呈现并注明 3-class 受 gen-0 共享影响 [MF2]\n\n### Introduction\n- Contribution #1 应将 DDR 定位为 \"empirical regularity with analytical utility\" [DIV1]\n- 应在 base-model scope 前置说明处更早限定 [MF4]\n\n### Section 3.2 (Generation Chain)\n- Seed sharing 的 leakage 讨论已有，但量化不足 [MF2]\n\n### Section 4.1 (Classification Performance)\n- \"our primary conservative metric\" 已标注 binary F1，但 Abstract/Intro 仍以 3-class 为主 [MF2]\n- 补充 per-generator fold-level mean±std [SF6]\n\n### Section 4.2 (DDR)\n- 将 Table 35 holdout split validation 从附录提升至此处 [MF3]\n- Entropy_std 的三组结构应在此处明确呈现 [SF3]\n- Cohen's d 阈值选择应连接 LOFO 结果 [SF4]\n\n### Section 4.3 (Baselines)\n- \"matches multi-detector ensembles\" 表述需附加 3-class F1 差距的诚实讨论 [SF5]\n\n### Section 5 (Discussion)\n- 增加 instruction tuning 影响段落（~150 词），界定方法适用范围 [MF4]\n- Shape features 的贡献定位需修订 [MF1]\n\n### Section 2 (Related Work)\n- 补充 stylometry/authorship attribution 方向讨论 [SF7]\n\n### Limitations\n- 已较全面，可加强 instruction tuning 失效的原因分析",
    "project": "gen-depth-fingerprint",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference"
  }
}
```

</details>

---


### Tool result

_source line 3935 · 2026-05-23T02:02:54.705480+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3916
}
```

</details>

---


### Assistant

_source line 3936 · 2026-05-23T02:03:05.953855+00:00_

审稿报告已投递至 Research Director。

**Round 50 审稿完成**。汇总：

- **Overall: 3.5 (Borderline Conference)**，两位 Reviewer 独立一致
- **4 个 Must-Fix**：(1) shape feature 因果声称与 LOFO/PI 证据矛盾；(2) gen-0 种子共享使 3-class F1 高估约 3pp；(3) DDR holdout validation 被埋在附录需提升主文；(4) instruction tuning 失效在主文讨论不足
- **7 个 Should-Fix**：命名精度、entropy 术语、entropy_std 三组结构、TOST 边界校准、baseline 比较诚实度、bootstrap CI 层级、stylometry related work
- **Director 更正**：R2-W4（跨 family 泛化未测试）实为论文已有 LOFO F1=0.686，两位 Reviewer 均遗漏
- **关键判断**：所有 Must-Fix 均为 framing/presentation 性质（非实验缺陷），修订后有望达到 Conference (4.0)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 387

## Round 387

2 recorded events


### User

_source line 3937 · 2026-05-23T02:03:08.649508+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 7 个问题：5 个 AGREE，1 个 AGREE with nuance，1 个 REBUT（QLoRA 子集对比——论文 Appendix e 已有同子集公平对比）。同时标注了两位 Reviewer 的 4 个共识点，其中 instruction tuning 限制是 R2 独立提出、R1 未涉及的问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3938 · 2026-05-23T02:03:24.303731+00:00_

审稿报告已投递至 Research Director。

**Round 50 审稿总结**：

- **Overall: 3.5 (Borderline Conference)**
- **4 个 Must-Fix**（全部为 framing/presentation 修改，不需要新实验）：
  1. Shape feature 因果声称需弱化为描述性观察（LOFO/PI 证据矛盾）
  2. Gen-0 种子共享使 3-class F1 高估 ~3pp，binary F1 应升格为并列主指标
  3. DDR holdout split validation 需从附录提升至主文
  4. Instruction tuning 失效需在 Discussion 显式讨论并界定适用范围
- **7 个 Should-Fix**：命名精度、entropy 术语、三组 DDR 结构、TOST 校准、baseline 比较讨论、CI 层级、stylometry related work
- **1 个 Director 更正**：R2-W4 (跨 family 泛化) 论文已有 LOFO F1=0.686，两位 Reviewer 均未注意到
- **2 处分歧**：Contribution framing（R1 认为 DDR 有独立分析价值）、QLoRA 子集对比（R2 指出同子集比较已存在）
- **核心判断**：如果 4 个 Must-Fix 在修订中解决，论文有望达到 Conference (4.0) 水平

Issue Tracker 已同步更新（96 条，R50 新增 8 条，R49 更新 14 条）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 388

## Round 388

82 recorded events


### User

_source line 3939 · 2026-05-24T22:48:40.145148+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-fingerprint
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 3940 · 2026-05-24T22:48:44.963883+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3941 · 2026-05-24T22:48:45.014972+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 3942 · 2026-05-24T22:48:52.343126+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3943 · 2026-05-24T22:48:52.393657+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3944 · 2026-05-24T22:48:57.360698+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3945 · 2026-05-24T22:48:57.461462+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3946 · 2026-05-24T22:48:59.721535+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_get_project_overview",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_get_project_overview",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3947 · 2026-05-24T22:48:59.722005+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3948 · 2026-05-24T22:49:02.483557+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "dispatch_visual_check",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "dispatch_visual_check",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 3949 · 2026-05-24T22:49:02.483985+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3950 · 2026-05-24T22:49:03.286878+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "request_external_review",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "request_external_review",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 3951 · 2026-05-24T22:49:03.337369+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3952 · 2026-05-24T22:49:03.739048+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 3953 · 2026-05-24T22:49:03.739356+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3954 · 2026-05-24T22:49:03.940216+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 3955 · 2026-05-24T22:49:03.940548+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3956 · 2026-05-24T22:49:04.492690+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "update_review_issues",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "update_review_issues",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 3957 · 2026-05-24T22:49:04.543357+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3958 · 2026-05-24T22:49:04.945079+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "get_visual_check_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "get_visual_check_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 3959 · 2026-05-24T22:49:04.945393+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3960 · 2026-05-24T22:49:05.373365+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "get_external_review_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "get_external_review_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 3961 · 2026-05-24T22:49:05.373716+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3962 · 2026-05-24T22:49:05.524471+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 3963 · 2026-05-24T22:49:05.524827+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3964 · 2026-05-24T22:49:12.852853+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 3965 · 2026-05-24T22:49:13.756510+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (68 个)\n\n- **plan-015**: DONE (success) — \n- **plan-004**: DONE (failed) — \n- **plan-003**: DONE (success) — \n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_062_decoding_strategy_shape** (success): DDR shape stability (entropy_max, entropy_min, tail_decay near-stationary with d<0.15) holds under greedy (temperature=0) and top-k (k=50, τ=0.7) decoding, not just nucleus sampling — verifying the DDR decomposition is decoding-strategy-agnostic\n- **decoding_strategy_shape** (killed): DDR shape stability (entropy_max, entropy_min, tail_decay d<0.15) holds under greedy and top-k decoding, not just nucleus sampling — verifying the claim is decoding-strategy-agnostic\n- **plan-004-prep** (success): Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）\n\n## 趋势\n成功 48 / 负向 2 / 失败 12 / 共 68\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb2-18868: 无 GPU 信息\n\n## 告警\n- mvp-001-gen-s0: 已被终止 — unknown\n- mvp-001-gen-s1: 训练失败 — unknown\n- mvp-001-gen-s2: 训练失败 — unknown\n- mvp-001-gen-s3: 训练失败 — unknown\n- plan-001-restore: 已被终止 — unknown\n- plan-002-qwen3-1_7b-s0: 训练失败 — unknown\n- plan-002-qwen3-1_7b-s1: 已被终止 — unknown\n- plan-002-qwen17b-s0: 训练失败 — unknown\n- plan-002-qwen17b-s1: 训练失败 — unknown\n- plan-002-qwen17b-retry-s0: 训练失败 — unknown\n- plan-002-qwen17b-retry-s1: 训练失败 — unknown\n- plan-002-qwen06b-s0
…[truncated 256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 3966 · 2026-05-24T22:49:13.756885+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 3967 · 2026-05-24T22:49:15.312416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 3968 · 2026-05-24T22:49:15.312836+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{placeins}
15	\usepackage{multirow}
16	\usepackage{float}
17	\usepackage{stfloats}
18	\usepackage{alphalph}
19	\usepackage{tcolorbox}
20	\tcbuselibrary{breakable}
21	
22	\graphicspath{{../chart/}}
23	
24	\title{Depth Profiling: Classifying Recursive Generation Depth\\in Base-Model LLM Text}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\raggedbottom
30	\maketitle
31	
32	\input{abstract}
33	
34	\input{introduction}
35	\input{related_work}
36	\input{method}
37	\input{results}
38	
39	\input{discussion}
40	\input{conclusion}
41	\input{limitations}
42	\bibliography{references}
43	
44	\appendix
45	\renewcommand{\thesection}{\alphalph{\value{section}}}
46	
47	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
48	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
49	
50	\input{appendix_dataset_stats}
51	
52	\section{Length Confound Analysis}
53	\label{app:length}
54	\input{appendix_length}
55	
56	\section{Prompt Type Generalization}
57	\label{app:prompt-type}
58	\input{appendix_prompt_type}
59	\FloatBarrier
60	
61	\section{Finer-Grained Depth Classification}
62	\label{app:finer-depth}
63	\input{appendix_finer_depth}
64	\FloatBarrier
65	
66	\section{End-to-End Depth Classification (QLoRA)}
67	\label{app:qlora}
68	\input{appendix_qlora}
69	\FloatBarrier
70	
71	\section{Leave-One-Feature-Out Analysis}
72	\label{app:lofo}
73	\input{appendix_lofo}
74	\FloatBarrier
75	
76	\subsection{Candidate Feature Screening}
77	\label{app:feature-candi
…[truncated 556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 3969 · 2026-05-24T22:49:19.429125+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission deadline author guidelines site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found search results related to EMNLP 2026 and various calls, but the results 
…[truncated 1191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 5672
}
```

</details>

---


### Tool call

_source line 3970 · 2026-05-24T22:49:25.584049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex",
  "offset": "100",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex",
    "offset": "100",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 3971 · 2026-05-24T22:49:26.588465+00:00_

100	\section{Instruction-Tuned Model Analysis}
101	\label{app:instruct}
102	\input{appendix_instruct}
103	
104	\section{Error Analysis of Binary Classification}
105	\label{app:error-analysis}
106	\input{appendix_error_analysis}
107	\FloatBarrier
108	
109	
110	\section{Downstream Utility}
111	\label{app:downstream}
112	\input{appendix_downstream}
113	\FloatBarrier
114	
115	\section{Cross-Model Chain Per-Class Detail}
116	\label{app:cross-model-detail}
117	\input{appendix_cross_model_detail}
118	\FloatBarrier
119	
120	\section{Feature Distribution Analysis}
121	\label{app:feature-distributions}
122	\input{appendix_feature_distributions}
123	
124	\section{Cross-Temperature Transfer}
125	\label{app:cross-temp}
126	\input{appendix_cross_temp}
127	
128	\section{Feature Ablation}
129	\label{app:ablation-table}
130	\input{appendix_ablation}
131	
132	\input{appendix_feature_correlation}
133	
134	\section{Cross-Family Reference Models}
135	\label{app:cross-ref}
136	\input{table4}
137	
138	\input{appendix_seed_control}
139	
140	\input{appendix_tost}
141	
142	\input{appendix_tost_bootstrap}
143	
144	\section{DDR Partition Validation}
145	\label{app:ddr-validation}
146	\input{appendix_ddr_validation}
147	
148	\section{Generator Subset Summary}
149	\label{app:gen-subsets-section}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 3972 · 2026-05-24T22:49:26.739450+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission deadline June July cycle aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission deadline June July cycle aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 3973 · 2026-05-24T22:49:26.890445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 3974 · 2026-05-24T22:49:26.941019+00:00_

1	% Abstract — Depth Profiling of Recursive LLM Generation Chains
2	\begin{abstract}
3	As large language model (LLM) outputs re-enter training corpora and seed further generation, understanding how recursive generation reshapes text distributions is critical for data provenance and corpus curation---yet existing detectors answer only the binary human-or-machine question, ignoring \emph{generation depth}: we introduce \emph{depth profiling} to address this gap.
4	We decompose distributional drift under recursive generation into location and shape components, revealing an asymmetry we term \emph{differential depth response} (DDR): across eight base-model generators from five families, negative log-likelihood (NLL) location features drift monotonically with depth (effect size $d{=}0.74$--$1.05$) while three shape features remain near-stationary ($d < 0.10$), with entropy std intermediate ($d{=}0.46$)---a ${\geq}8{\times}$ effect-size gap.
5	Prior work documents \emph{what converges}; the central finding here is \emph{what is approximately preserved}: shape stability complements location drift for ordinal depth grading without per-generator calibration, achieving leak-free binary F1\,=\,0.694 (gen-1 vs.\ gen-2+), cross-model binary F1\,=\,0.830, and 3-class F1\,=\,0.762 under leave-one-generator-out evaluation (gen-0 seeds shared across generators; \S\ref{sec:generation}); an end-to-end classifier reaches 3-class F1\,=\,0.905 (Appendix~\ref{app:qlora}).
6	Instruction tuning compresses DDR, bounding current applicability to base models.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 3975 · 2026-05-24T22:49:32.363782+00:00_

Web search results for query: "ACL Rolling Review 2026 submission deadline June July cycle aclrollingreview.org"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results from aclrollingreview.org, here's what I found about the ACL Rolling Review 2026 submission deadlines:

ACL implemented a switch from 8-week to 10-week review cycles, with the new schedule starting in May 2025. This means there will generally be 5 cycles per year instead of 6.

Regarding the specific June-July cycle you asked about: The search results show information about the January 2026 cycle but don't display the complete schedule table with June and July submission deadlines. Previously, ARR ran submission deadlines on the 15th of every second month, though with the new 10-week
…[truncated 458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 5624
}
```

</details>

---


### Tool call

_source line 3976 · 2026-05-24T22:49:36.074062+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 3977 · 2026-05-24T22:49:36.124584+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3978 · 2026-05-24T22:49:40.544089+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "Extract all 2026 ARR submission cycle deadlines (submission deadline dates) and which venues (EMNLP 2026, ACL 2026, etc.) each cycle's reviews can be committed to. I need the full table of dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/dates",
    "prompt": "Extract all 2026 ARR submission cycle deadlines (submission deadline dates) and which venues (EMNLP 2026, ACL 2026, etc.) each cycle's reviews can be committed to. I need the full table of dates."
  }
}
```

</details>

---


### Tool call

_source line 3979 · 2026-05-24T22:49:42.101226+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the full author guidelines for ARR submissions: page limits (long/short paper), template requirements, anonymity rules, appendix rules, citation format, and any other formatting requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the full author guidelines for ARR submissions: page limits (long/short paper), template requirements, anonymity rules, appendix rules, citation format, and any other formatting requirements."
  }
}
```

</details>

---


### Tool result

_source line 3980 · 2026-05-24T22:49:44.109656+00:00_

# 2026 ARR Submission Cycles and Venue Commitments

Based on the page content, here are the 2026 ARR submission deadlines and corresponding publication venues:

## Submission Cycles and Deadlines

**March 2026 Cycle**
- "Submission" deadline: March 16
- No venues listed for this cycle's commitment

**May 2026 Cycle**
- "Submission" deadline: May 25
- Compatible venues:
  - EMNLP 2026 (commitment by August 2, 2026)
  - AACL 2026 (commitment by August 2, 2026)

**August 2026 Cycle**
- "Submission" deadline: August 3
- Compatible venue:
  - EACL 2027 (commitment by October 11, 2026)

**October 2026 Cycle**
- "Submission" deadline: October 12
- No venues listed for this cycle's commitment

The page indicates that "in addition to submission and author response dates," reviewer registration and review submission deadlines are now critical milestones with potential penalties for non-compliance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "elapsed_ms": 3565
}
```

</details>

---


### Tool result

_source line 3981 · 2026-05-24T22:49:48.826970+00:00_

# ARR Submission Guidelines Summary

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space for limitations (required) and optional ethical considerations section
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space for limitations (required) and optional ethical considerations section
- Unlimited reference pages

Papers exceeding length requirements or lacking a limitations section face automatic desk rejection.

## Template & Formatting

Submissions must follow the official ACL style template available on GitHub. Authors cannot modify style files or use templates from other conferences. Documents must conform to specified requirements for "paper size, margin width, and font size restrictions," or face rejection without review.

## Anonymity Requirements

Two-way anonymization is mandatory. Papers cannot disclose author names, affiliations, or self-identifying citations (e.g., "We previously showed..."). Instead, use third-person construction like "Smith previously showed..." Supplementary materials and repository links must also be anonymized. Non-anonymous file hosting services like Dropbox are prohibited. Anonymity violations result in desk rejection.

## Appendices

Appendices follow the main paper after references and don't count toward page limits. They must maintain double-column formatting per ACLPUB guidelines. Reviewers aren't obligated to examine appendix content, so critical technical material belonging in the main paper shouldn't be relegated to appendices. Anonymization requirements apply here too.

## Citation Format for Concurrent Work

For concurrently submitted related papers with overlapping authorship, use this format:

> "Anonymous (2026). Paper title. Under review."

## Additional Requirements

A dedicated "Limitations" section is mandatory and required before references. Responsible NLP Checklist completion is obligatory during submission.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "elapsed_ms": 6725
}
```

</details>

---


### Tool call

_source line 3982 · 2026-05-24T22:50:00.213207+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 3983 · 2026-05-24T22:50:00.715241+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	An estimated 7--17\% of recent scientific publications already contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}. As these outputs re-enter training corpora \cite{dolma,fineweb} and seed further generation, text accumulates at varying \emph{generation depths}; each successive cycle reshapes distributional properties in ways that matter for data provenance, corpus auditing, and contamination monitoring in base-model pretraining corpora \cite{ccnet,dsir} as well as model collapse analysis \cite{curse_of_recursion,strong_model_collapse}. Understanding \emph{how} recursive generation alters text distributions---and which properties change versus which are preserved---is therefore a prerequisite for principled corpus curation, yet current methods address only binary human-or-machine detection \cite{detectgpt,fast_detectgpt,binoculars,ld_score}.
5	Base models provide the cleanest substrate to isolate depth effects from alignment-induced changes.
6	We find that recursive generation produces a decomposable depth profile: distributional \emph{location} drifts with depth while \emph{shape} remains stable across generators, an asymmetry sufficient for cross-generator depth prediction.
7	
8	Distributional compression under recursive generation is well-documented \cite{curious_decline,broken_telephone,markovian_chains}, yet existing analyses characterize \emph{that} and \emph{why} convergence occurs without decomposing what drifts from what is preserved.
9	We introduce \emph{depth profiling} (coarse ordinal classification into gen-0\,/\,gen-1\,/\,gen-2+), and decompose this compression into structurally distinct components: across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency (mean entropy (reference-model NLL), lexical diversity) drifts monotonically with depth while its shape (entropy extremes, tail structure) re
…[truncated 3389 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3984 · 2026-05-24T22:50:00.715690+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 3985 · 2026-05-24T22:50:01.167537+00:00_

1	\vspace{-1mm}
2	\section{Method}
3	\label{sec:method}
4	
5	\begin{table}[t!]
6	\centering
7	\footnotesize
8	\caption{Seven distributional features. ``Entropy'' features are computed as per-token NLL under Pythia-410M (see \S\ref{sec:features}); surface features require no reference model. DDR analysis (\S\ref{sec:results-differential}) reveals that entropy mean and the two surface features (TTR, hapax ratio) drift with depth while entropy max, min, and tail decay remain near-stationary; entropy std is intermediate. All ``entropy'' features are reference-model NLL values (cross-entropy with Pythia-410M), not information-theoretic entropy; see \S\ref{sec:features}.}
9	\label{tab:features}
10	\setlength{\tabcolsep}{4pt}
11	\begin{tabular}{@{}llp{3.0cm}@{}}
12	\toprule
13	\textbf{Feature} & \textbf{Source} & \textbf{Measures} \\
14	\midrule
15	\texttt{entropy\_mean} & Ref.\ NLL & Central tendency of token surprise \\
16	\texttt{entropy\_std}  & Ref.\ NLL & Spread of token surprise \\
17	\texttt{entropy\_max}  & Ref.\ NLL & Maximum token surprise \\
18	\texttt{entropy\_min}  & Ref.\ NLL & Minimum token surprise \\
19	\texttt{tail\_decay}   & Ref.\ NLL & Log-prob decay slope (ranks 100--1K) \\
20	\midrule
21	\texttt{ttr}           & Surface & Type-token ratio \\
22	\texttt{hapax\_ratio}  & Surface & Proportion of hapax legomena \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{figure*}[t]
28	\centering
29	\includegraphics[width=\textwidth]{fig2_framework.pdf}
30	\caption{Depth profiling pipeline. (a)~Human seeds are iteratively fed through generator $G$ to produce chains of increasing depth. (b)~Seven features extracted from NLL distributions group into three DDR zones: drifting (red), intermediate (purple), near-stationary (blue). (c)~LOGO evaluation holds out one generator for testing.}
31	\label{fig:framework}
32	\end{figure*}
33	
34	\subsection{Task Formulation}
35	\label{sec:task}
36	
37	Given a text $x$, we predict its \emph{generation depth} $d \in 
…[truncated 6898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 3986 · 2026-05-24T22:50:01.167920+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 3987 · 2026-05-24T22:50:01.318751+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{fig_transfer_heatmap.pdf}
7	\caption{Cross-generator depth classification: $8{\times}8$ transfer matrix (binary F1, gen-1 vs.\ gen-2+). Each cell shows F1 when training on one generator (row) and testing on another (column). Mean cross-generator F1\,=\,0.810 [95\% CI: 0.796, 0.822]; uniformly high off-diagonal values demonstrate that depth signal transfers robustly across five architectural families without per-generator calibration.}
8	\label{fig:transfer-heatmap}
9	\end{figure}
10	
11	\subsection{Depth Classification Performance}
12	\label{sec:results-classification}
13	
14	\looseness=-1 The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}), with cross-generator F1 spread of 9.1\,pp capturing generator selection uncertainty.
15	This 3-class metric is inflated by shared gen-0 seeds (per-class gen-0 F1\,$\approx$\,0.94; \S\ref{sec:generation}); we therefore report \textbf{leak-free binary F1} (gen-1 vs.\ gen-2+)\,=\,0.694 (CI [0.688, 0.700]) throughout, excluding gen-0 entirely.
16	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B; std.\ dev.\ 0.028), with the primary difficulty at the gen-1\,/\,gen-2+ boundary (Appendix~\ref{app:confusion}).
17	
18	\paragraph{Cross-model generalization.}
19	Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.830 (95\% CI [.818, .841]; Appendix~\ref{app:cross-model-detail}) under 5-generator LOGO.\footnote{Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B; generator-level LOGO with bootstrap CIs ($n$\,=\,1{,}000).}
20	Single-generator transfer confirms the signal is not a mixed-chain artifact (mean transfer F1\,=\,0.810, Figure~\ref{fig:transfer-heatmap}; LOFO\,=\,0.686); analysis of variance (ANOVA) confirms generator identity contributes ${<}1$\% of 
…[truncated 11104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 3988 · 2026-05-24T22:50:02.773076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 3989 · 2026-05-24T22:50:03.024015+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models with $\leq$8.2B parameters; instruction-tuned variants show substantially degraded depth signal (within-model 3-class F1 drops 3.7--19.9\,pp; Appendix~\ref{app:instruct}), though QLoRA partially recovers (F1\,=\,0.89--0.91), suggesting the signal is compressed rather than eliminated.
5	
6	The evaluation assumes English Wikipedia seeds, a fixed decoding regime ($t{=}0.7$, nucleus $p{=}0.9$), and an English-centric reference model (Pythia-410M); cross-temperature transfer is tested (Appendix~\ref{app:cross-temp}) but cross-lingual generalization remains untested.
7	
8	Depth resolution is bounded at three classes (gen-0\,/\,gen-1\,/\,gen-2+); finer-grained 5-class classification yields F1\,$\approx$\,0.50 with deeper depths mutually indistinguishable (Appendix~\ref{app:finer-depth}).
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 250
}
```

</details>

---


### Tool call

_source line 3990 · 2026-05-24T22:50:03.024306+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 3991 · 2026-05-24T22:50:03.074827+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml\", \"content\": \"_next_id: 52\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:15 UTC\\n  summary: MVP 方案：Pythia-2.8B continuation 链 + Pythia-410M 参考模型 + XGBoost 3-class\\n    分类\\n  rationale: '选择 continuation（最低语义偏离）作为最可能保留 depth 信号的生成类型；单生成器简化变量；Pythia-410M 作为参考模型避免与生成器的规模/架构循环；XGBoost\\n    快速验证无需 GPU 训练。Pass: macro-F1≥0.45 且 gen-0 vs gen-2+ F1≥0.65。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 18:10 UTC\\n  summary: MVP PASS → 进入研究阶段。首要任务：特征 ablation + depth signal 增量验证\\n  rationale: macro-F1=0.84 远超 0.45 阈值，binary F1=0.87 远超 0.65，7/7 特征显著。核心假设成立。但 Reviewer\\n    指出 hapax_ratio（表面特征）贡献最大，需 ablation 验证分布指纹的独立价值；gen-1 vs gen-2+ 混淆率高，需量化 depth\\n    信号超越 binary 分类的增量。\\n  related_experiments:\\n  - exp_id: mvp-001\\n    role: primary\\n    result: 'PASS: macro-F1=0.8408, binary-F1=0.8653'\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 18:15 UTC\\n  summary: Claim 2 准备 Plan B framing：若 ablation 显示表面特征足够，叙事从 \\\"independent signal\\\"\\n    调整为 \\\"complementary signal\\\"\\n  rationale: Reviewer 指出 Claim 2 是整个叙事的 single point of failure。MVP 中 hapax_ratio\\n    importance=0.30，表面特征贡献 47%。Plan B 不 kill 项目，只调 framing 强度——从\\\"分布指纹独立于表面统计\\\"降为\\\"分布指纹提供互补信号\\\"，核心叙事转为\\n    vocabulary impoverishment as primary depth signal。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 18:38 UTC\\n  summary: Claim 2 framing 调整：从 \\\"Fingerprint Independence\\\" 转为 \\\"Feature Complementarity\\n    & Dual Dynamics\\\"；H1/H2 从二选一转为共存\\n  rationale: plan_001 ablation 结果：surface_only (0.76) > reference_only (0.72)，但 full\\n    (0.82) 显著优于 surface_only (p=0.0008)。原 Claim 2 \\\"independent signal\\\" 被否定，触发 Plan\\n    B (D003)。新发现更强：表面特征呈 H2 drift、分布形状特征呈 H1 stationary，dual dynamics 是比原 framing\\n    更丰富的科学贡献。\\n  related_experiments:\\n  - exp_id: p
…[truncated 1488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3992 · 2026-05-24T22:50:08.215106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 3993 · 2026-05-24T22:50:08.717799+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\looseness=-1 DDR reflects monotonic compression of the token-level NLL distribution under recursive generation (Appendix~\ref{app:nll-distribution}): location features shift with each cycle while shape features resist because they are architecturally bounded---entropy max by $\log|V|$, tail decay by softmax geometry.
5	ANOVA variance decomposition (Figure~\ref{fig:variance-decomp}) quantifies this asymmetry: $\eta^2_{\text{depth}}{=}0.34$--$0.37$ for location vs.\ ${<}0.01$ for shape (${>}48{\times}$ gap), with $\eta^2_{\text{gen}}{\approx}0.02$ across both groups, confirming depth-specificity.
6	Interaction terms are uniformly small ($\eta^2_{\text{int}} < 0.011$; Appendix~\ref{app:variance-decomposition}); controlled ablations (Appendices~\ref{app:decoding-strategy}--\ref{app:prompt-type}) and Granger causality (Appendix~\ref{app:ddr-causality}) further corroborate the partition.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{fig_appendix_variance_decomp.pdf}
11	\caption{ANOVA variance decomposition ($\eta^2$) by feature. Depth explains 34--37\% of location-feature variance vs.\ $<$1\% for shape features (${>}48\times$ gap). Generator identity contributes uniformly ${\approx}2$\% across both groups, confirming the DDR partition is depth-specific.}
12	\label{fig:variance-decomp}
13	\end{figure}
14	
15	\paragraph{Relationship to model collapse.}
16	\looseness=-1 DDR is mechanistically distinct from model collapse \cite{curse_of_recursion,strong_model_collapse}: retraining erodes tail coverage via weight updates, whereas DDR characterizes fixed-parameter inference chains where shape features remain stable because no weight update alters the generating distribution's support.
17	Model collapse is irreversible once weights are contaminated; DDR-detectable depth effects are text properties identifiable post-hoc without training history.
18	DDR complements concurrent iterative-generation s
…[truncated 1868 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3994 · 2026-05-24T22:50:08.718235+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 3995 · 2026-05-24T22:50:09.722029+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{AI-generated text detection.}
5	\looseness=-1 Detection methods span zero-shot scoring \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, learned classifiers \cite{ghostbuster,ld_score,reliable_detection}, and surprisal-based approaches \cite{diveye,xu_spectrum_detection}; see \citet{wu_survey_2025} for a survey.
6	Recent work moves beyond binary detection---multi-generator attribution \cite{semeval2024_task8}, collaboration roles \cite{beyond_binary}, joint detection-attribution \cite{two_birds}---but all taxonomize by \emph{source} or \emph{production mode}, not recursive generation \emph{depth}.
7	We introduce ordinal depth classification \cite{gutierrez_ordinal_survey,coral_ordinal} as a complementary task; repurposing existing detection scores as depth predictors reveals high cross-generator variance (binary F1\,=\,0.54--0.71; Table~\ref{tab:baselines}).
8	
9	\paragraph{Model collapse and iterative generation.}
10	\looseness=-1 Self-consuming generative models lose distributional coverage \cite{self_consuming_mad,curse_of_recursion,strong_model_collapse}, with even minimal synthetic contamination altering scaling laws \cite{dohmatob_tale_of_tails}.
11	These studies address \emph{training-loop} degradation where parameter updates erode tail coverage \cite{schaeffer_collapse_position}; we instead examine \emph{inference chains} where parameters are fixed.
12	Concurrent iterative-generation studies document complementary phenomena: paraphrasing chains show factuality degradation \cite{broken_telephone}, Markovian analysis bounds distinguishable depth to ${\sim}$3 classes \cite{markovian_chains}, and attractor cycle evidence emerges \cite{attractor_cycles}.
13	DDR differs in chain type (non-paraphrastic continuation), analysis lens (location/shape decomposition identifying what is \emph{preserved}), and downstream utility (shape stability enables cross-generator classification without calibration); a d
…[truncated 908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 3996 · 2026-05-24T22:50:09.722361+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 3997 · 2026-05-24T22:50:10.174372+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-1 Recursive generation produces a decomposable depth response---location features drift monotonically while shape features remain approximately preserved---enabling cross-generator depth classification (F1\,=\,0.694--0.762) within the base-model scope.
5	Cross-model chains confirm generalization across five architectural families (F1\,=\,0.830; ANOVA: depth explains ${>}48{\times}$ more location-feature variance than shape-feature variance, while generator identity contributes uniformly ${\approx}2$\%).
6	The decomposition is robust across decoding strategies, temperatures, prompt types, and reference models, with the DDR partition independently recovered by every held-out generator.
7	QLoRA recovery (F1\,=\,0.89--0.91) suggests tractable extension to instruct models; DDR connects depth profiling to corpus auditing (provenance-aware contamination flagging) and model collapse monitoring (tracking location-drift as an early warning signal).
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 3998 · 2026-05-24T22:50:10.576655+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 3999 · 2026-05-24T22:50:10.727606+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 4000 · 2026-05-24T22:50:16.248143+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen-depth-fingerprint/**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen-depth-fingerprint/**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
  }
}
```

</details>

---


### Tool result

_source line 4001 · 2026-05-24T22:50:17.101911+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 4002 · 2026-05-24T22:50:17.152440+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 4003 · 2026-05-24T22:50:17.203094+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4004 · 2026-05-24T22:50:22.287801+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 3 -name \"*.yaml\" -path \"*/gen-depth*\" 2>/dev/null | head -20",
  "description": "Find yaml files in project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 3 -name \"*.yaml\" -path \"*/gen-depth*\" 2>/dev/null | head -20",
    "description": "Find yaml files in project directory"
  }
}
```

</details>

---


### Tool result

_source line 4005 · 2026-05-24T22:50:22.350268+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/gen-depth-fingerprint.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 62
}
```

</details>

---


### Tool call

_source line 4006 · 2026-05-24T22:50:25.195315+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/gen-depth-fingerprint.yaml | grep -A 10 \"external_review\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/gen-depth-fingerprint.yaml | grep -A 10 \"external_review\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 4007 · 2026-05-24T22:50:26.349753+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 1154
}
```

</details>

---


### Tool call

_source line 4008 · 2026-05-24T22:50:26.350153+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null | head -30 || echo \"NO_FILE\"",
  "description": "Check existing review issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null | head -30 || echo \"NO_FILE\"",
    "description": "Check existing review issues"
  }
}
```

</details>

---


### Tool result

_source line 4009 · 2026-05-24T22:50:26.400643+00:00_

- id: R29-N1
  summary: Base-model-only scope 未在 Abstract 标注
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 32
  resolution: Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented.
  resolution_round: 32
- id: R29-N2
  summary: Downstream TOST underpowered (n=3) + Abstract overclaim
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 34
  resolution: Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料.
  resolution_round: 34
- id: R29-N3
  summary: DDR 新颖性 incremental — 缺 concurrent work 系统对比表
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 31
  resolution: related_work.tex concurrent-comparison table added
  resolution_round: 31
- id: R29-N4
  summary: QLoRA gap 削弱方法论贡献 — 需重定位
  category: framing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4010 · 2026-05-24T22:50:30.766251+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/gen-depth-fingerprint.yaml",
  "description": "Read full project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/gen-depth-fingerprint.yaml",
    "description": "Read full project config"
  }
}
```

</details>

---


### Tool result

_source line 4011 · 2026-05-24T22:50:31.168024+00:00_

execution:
  gpu_ids:
  - cuda:0
  - cuda:1
  - cuda:2
  - cuda:3
  project_path: /root/gen-depth-fingerprint
  servers:
  - bjb2-18868
feishu:
  chat_id: oc_dbd68d7879a81efc0c108e9844b15d0b
  check_references: false
  operational_chat_id: oc_a189a3add89efad7437b5c9f3e05fbf3
  review_mode: fresh
  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex
  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_round_51/submitted.pdf
  review_round: 51
  review_supplementary_paths: ''
  submission_chat_id: oc_999770e4e57bfc6eabd12fc1f64af1ef
project:
  created_at: '2026-05-14T16:13:51.441Z'
  description: Provenance Depth Estimation for Risk-Aware Curation of Synthetic Text
  name: gen-depth-fingerprint
  phase: research
  source_idea_id: idea_009
rules:
  research: []
  writing:
  - created_at: '2026-05-17T17:22:45Z'
    id: 89ee27
    text: overall framework参考已发表EMNLP论文的风格，图中的信息密度要高，视觉美观，高度浓缩method部分信息
  - created_at: '2026-05-20T16:25:45Z'
    id: '799680'
    text: 参考已发表同类文章（如本文是empirical）的写作风格，如用词，写作逻辑，架构，语气，改善本篇的写作，要将整个story讲的高级一些，体现技术深度同时有创新性
  - created_at: '2026-05-20T16:43:51Z'
    id: c60e8a
    text: 附录中的可视化图要嵌入在文字中，出现在论文中需要用到图的附近位置，同时注意latex排版，避免大量空白的存在
  - created_at: '2026-05-21T03:45:29Z'
    id: dacdf2
    text: 图表不要默认在页面的居中位置，前面有留白要及时补齐，动态调整文字和配图（全宽/半宽），同时要注意图片和文字位置的匹配程度
  - created_at: '2026-05-21T16:58:19Z'
    id: 8ef0ef
    text: 图片要放在文中出现的地方附近，当文中出现大量留白时，调整后面的文字和图片及时向上补齐
venue: emnlp-2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 4012 · 2026-05-24T22:50:31.168511+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml",
  "description": "Count lines in review issues file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml",
    "description": "Count lines in review issues file"
  }
}
```

</details>

---


### Tool result

_source line 4013 · 2026-05-24T22:50:31.219043+00:00_

1098 /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4014 · 2026-05-24T22:50:53.243484+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
  }
}
```

</details>

---


### Tool result

_source line 4015 · 2026-05-24T22:51:14.112024+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20868
}
```

</details>

---


### Tool call

_source line 4016 · 2026-05-24T22:51:15.667961+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计与统计分析**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: ARR May 2026 cycle, 提交截止 2026-05-25\n- **格式**: ACL 模板, Long paper 正文 ≤8 页, 参考文献不限, 附录不计入正文\n- **匿名**: Double-blind (two-way anonymization)\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_round_51/submitted.pdf`\n\n## 论文概述\n标题：Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text\n主题：分析 recursive LLM generation 的 distributional drift，将其分解为 location（漂移）和 shape（稳定）两个组件（称为 DDR），用于 cross-generator depth classification。\n\n## 你的审查侧重\n\n**1. 方法严谨性**：\n- DDR 的定义和量化方法是否严格？location vs shape 的分界标准（Cohen's d 阈值）是否 arbitrary？\n- feature selection 过程（7 个特征的选择、6 个被拒绝特征的标准）是否透明且合理？\n- 参考模型选择（Pythia-410M）是否引入系统偏差？cross-family validation 是否充分？\n- 分类器选择（XGBoost, 固定超参数）是否合理？是否存在过拟合/欠拟合风险？\n\n**2. 实验设计与统计**：\n- LOGO/LOFO 评估协议的严格性——gen-0 共享种子是否构成数据泄露？binary F1 排除 gen-0 是否充分解决？\n- 统计检验的适当性（bootstrap CI, Bonferroni 校正, TOST equivalence, permutation testing）\n- 消融实验的完整性——每个 claim 是否有对应的 ablation 支持？\n- 实验规模（37K texts, 8 generators）是否足够支撑 generalization 声明？\n- Temperature sensitivity（t=0.9 大幅下降）的影响和限制是否被充分讨论？\n- 效果量级：binary F1=0.694 作为主要指标是否足够强？\n\n**3. 格式合规**：\n- 正文是否符合 ≤8 页限制？\n- Limitations section 是否存在且内容充分？\n- 匿名化是否合规？（检查代码链接、作者信息、自引方式）\n\n请逐条给出评审意见，区分 Must-Fix（必须修改）和 Should-Fix（建议修改），并给出你的 Overall Assessment 评分。",
  "project": "gen-depth-fingerprint",
  "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
  "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计与统计分析**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: ARR May 2026 cycle, 提交截止 2026-05-25\n- **格式**: ACL 模板, Long paper 正文 ≤8 页, 参考文献不限, 附录不计入正文\n- **匿名**: Double-blind (two-way anonymization)\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_round_51/submitted.pdf`\n\n## 论文概述\n标题：Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text\n主题：分析 recursive LLM generation 的 distributional drift，将其分解为 location（漂移）和 shape（稳定）两个组件（称为 DDR），用于 cross-generator depth classification。\n\n## 你的审查侧重\n\n**1. 方法严谨性**：\n- DDR 的定义和量化方法是否严格？location vs shape 的分界标准（Cohen's d 阈值）是否 arbitrary？\n- feature selection 过程（7 个特征的选择、6 个被拒绝特征的标准）是否透明且合理？\n- 参考模型选择（Pythia-410M）是否引入系统偏差？cross-family validation 是否充分？\n- 分类器选择（XGBoost, 固定超参数）是否合理？是否存在过拟合/欠拟合风险？\n\n**2. 实验设计与统计**：\n- LOGO/LOFO 评估协议的严格性——gen-0 共享种子是否构成数据泄露？binary F1 排除 gen-0 是否充分解决？\n- 统计检验的适当性（bootstrap CI, Bonferroni 校正, TOST equivalence, permutation testing）\n- 消融实验的完整性——每个 claim 是否有对应的 ablation 支持？\n- 实验规模（37K texts, 8 generators）是否足够支撑 generalization 声明？\n- Temperature sensitivity（t=0.9 大幅下降）的影响和限制是否被充分讨论？\n- 效果量级：binary F1=0.694 作为主要指标是否足够强？\n\n**3. 格式合规**：\n- 正文是否符合 ≤8 页限制？\n- Limitations section 是否存在且内容充分？\n- 匿名化是否合规？（检查代码链接、作者信息、自引方式）\n\n请逐条给出评审意见，区分 Must-Fix（必须修改）和 Should-Fix（建议修改），并给出你的 Overall Assessment 评分。",
    "project": "gen-depth-fingerprint",
    "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
    "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
  }
}
```

</details>

---


### Tool result

_source line 4017 · 2026-05-24T22:51:35.216390+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19548
}
```

</details>

---


### Tool call

_source line 4018 · 2026-05-24T22:51:35.725120+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 相关工作完整性 + 写作质量**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: ARR May 2026 cycle, 提交截止 2026-05-25\n- **格式**: ACL 模板, Long paper 正文 ≤8 页, 参考文献不限, 附录不计入正文\n- **匿名**: Double-blind (two-way anonymization)\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_round_51/submitted.pdf`\n\n## 论文概述\n标题：Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text\n主题：提出 \"depth profiling\" 任务（ordinal depth classification: gen-0/gen-1/gen-2+），发现 recursive generation 下 NLL 分布的 location 和 shape 呈现不对称响应（DDR），用 7 个特征实现 cross-generator depth classification。\n\n## 你的审查侧重\n\n**1. 新颖性评估**：\n- \"Depth profiling\" 作为新任务的贡献程度——与 binary detection、multi-generator attribution、model collapse 分析的差异化是否足够？\n- DDR（location 漂移 vs shape 稳定）作为实证发现的新颖性——prior work 是否已经 implicitly 或 explicitly 发现了类似现象？\n- 方法层面的创新性——7 个标准 NLL 统计量 + XGBoost 是否缺乏方法论新意？作者将贡献定位为 empirical decomposition 是否合理？\n- 与 concurrent work（broken_telephone, markovian_chains, attractor_cycles）的关系——DDR 的 contribution 是否被这些工作实质性地覆盖？\n\n**2. 相关工作完整性**：\n- 是否遗漏重要的 related work？特别关注：\n  - AI text detection 领域的最新方法（2025-2026）\n  - Model collapse / iterative generation 领域\n  - Data provenance / corpus auditing 领域\n  - OOD detection 方法论在此任务的适用性\n- 引用的论文是否真实存在？（抽查关键引用）\n- 与 concurrent work 的对比是否公平？\n\n**3. 写作质量**：\n- Abstract 是否控制在 200 words 以内？信息密度是否合理？\n- 论文叙事结构（story）是否清晰连贯？从 problem motivation → method → findings → implications 的逻辑链是否完整？\n- Claim 与 evidence 的对应关系——每个 claim 是否有足够的实验支持？是否存在 overclaim？\n- 术语一致性——\"entropy\" 的使用是否可能误导读者（实际是 reference-model NLL）？\n- 写作风格是否符合 EMNLP 水准？语言是否地道？\n- 图表质量和信息密度——Figure 1-3 是否清晰、信息丰富？\n- Limitations section 是否坦诚且完整？\n\n请逐条给出评审意见，区分 Must-Fix（必须修改）和 Should-Fix（建议修改），并给出你的 Overall Assessment 评分。",
  "project": "gen-depth-fingerprint",
  "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
  "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 相关工作完整性 + 写作质量**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: ARR May 2026 cycle, 提交截止 2026-05-25\n- **格式**: ACL 模板, Long paper 正文 ≤8 页, 参考文献不限, 附录不计入正文\n- **匿名**: Double-blind (two-way anonymization)\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_round_51/submitted.pdf`\n\n## 论文概述\n标题：Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text\n主题：提出 \"depth profiling\" 任务（ordinal depth classification: gen-0/gen-1/gen-2+），发现 recursive generation 下 NLL 分布的 location 和 shape 呈现不对称响应（DDR），用 7 个特征实现 cross-generator depth classification。\n\n## 你的审查侧重\n\n**1. 新颖性评估**：\n- \"Depth profiling\" 作为新任务的贡献程度——与 binary detection、multi-generator attribution、model collapse 分析的差异化是否足够？\n- DDR（location 漂移 vs shape 稳定）作为实证发现的新颖性——prior work 是否已经 implicitly 或 explicitly 发现了类似现象？\n- 方法层面的创新性——7 个标准 NLL 统计量 + XGBoost 是否缺乏方法论新意？作者将贡献定位为 empirical decomposition 是否合理？\n- 与 concurrent work（broken_telephone, markovian_chains, attractor_cycles）的关系——DDR 的 contribution 是否被这些工作实质性地覆盖？\n\n**2. 相关工作完整性**：\n- 是否遗漏重要的 related work？特别关注：\n  - AI text detection 领域的最新方法（2025-2026）\n  - Model collapse / iterative generation 领域\n  - Data provenance / corpus auditing 领域\n  - OOD detection 方法论在此任务的适用性\n- 引用的论文是否真实存在？（抽查关键引用）\n- 与 concurrent work 的对比是否公平？\n\n**3. 写作质量**：\n- Abstract 是否控制在 200 words 以内？信息密度是否合理？\n- 论文叙事结构（story）是否清晰连贯？从 problem motivation → method → findings → implications 的逻辑链是否完整？\n- Claim 与 evidence 的对应关系——每个 claim 是否有足够的实验支持？是否存在 overclaim？\n- 术语一致性——\"entropy\" 的使用是否可能误导读者（实际是 reference-model NLL）？\n- 写作风格是否符合 EMNLP 水准？语言是否地道？\n- 图表质量和信息密度——Figure 1-3 是否清晰、信息丰富？\n- Limitations section 是否坦诚且完整？\n\n请逐条给出评审意见，区分 Must-Fix（必须修改）和 Should-Fix（建议修改），并给出你的 Overall Assessment 评分。",
    "project": "gen-depth-fingerprint",
    "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
    "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
  }
}
```

</details>

---


### Tool result

_source line 4019 · 2026-05-24T22:51:37.402012+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1676
}
```

</details>

---


### Assistant

_source line 4020 · 2026-05-24T22:51:48.116041+00:00_

Round 51 审稿已启动，三线并行：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验统计） | ✅ 已派发 |
| Reviewer 2（新颖性 + 相关工作 + 写作） | ✅ 已派发 |
| 视觉审查 Agent | ✅ 已启动 |

等待 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 389

## Round 389

2 recorded events


### User

_source line 4021 · 2026-05-24T22:57:51.516193+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 论文定义了一个新颖的生成深度分类任务，提出 DDR 分解框架并辅以严谨的统计验证，但中等水平的分类性能（binary F1=0.694）和温度敏感性限制了其实际影响力，处于主会议接收的边界位置。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论整体严谨，统计检验全面（bootstrap CI, Bonferroni, TOST, permutation, Granger, ANOVA），但 DDR 分区阈值选择偏 conventional，location/shape 分解与分类任务的形式化连接不够紧密 |
| Excitement | 3/5 | 研究问题新颖（从 binary detection 扩展到 depth classification），DDR 是有意义的实证发现，但绝对性能中等、实际应用场景未得到验证，作为纯描述性框架创新幅度有限 |
| Reproducibility | 4/5 | 提供了匿名代码仓库，实验细节充分（超参数、数据规模、生成配置均明确），附录覆盖面极广；扣分点在于参考模型的具体 tokenization 细节和 NLL 计算管线未完整描述 |
| Reviewer Confidence | 4/5 | 熟悉 AI text detection、distributional analysis 和 model collapse 领域的相关工作，仔细阅读了全文及 26 页附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 温度敏感性对泛化声明的削弱——主文讨论不充分
- 具体位置：§4.3（第 7 页），Table 13，Limitations（第 9 页），Appendix p
- 问题：Table 13 显示 t=0.9 时 3-class F1 从 0.762 降至 0.647（−15%），95% CI 不重叠。Appendix p 的 cross-temperature 迁移实验进一步表明，在 t=0.7 上训练、t=1.0 上测试时性能严重退化。然而，主文 §4.3 仅用约 3 行简要提及，Limitations 也只说"single decoding regime (t=0.7)"。这与 Section 6 (Conclusion) 中 "DDR is an empirical regularity of base-model autoregressive generation" 的强声明存在矛盾——如果该 regularity 在 t=0.9 时显著减弱，则 claim 的适用范围被严重限制。
- 为什么影响接收：这是方法泛化性的核心缺陷。Reviewer 会质疑：如果不知道生成时的温度，该方法是否仍然可靠？当前论文回避了这个问题。
- 建议修改方向：(1) 在主文 §4.3 或 Section 5 中用至少一段专门讨论温度敏感性的机制（高温导致分布更平坦，DDR 信号被稀释）和实际影响；(2) 在 Limitations 中明确将温度敏感性列为主要限制，而非仅提 "single decoding regime"；(3) 考虑将 Appendix p 的 cross-temperature 迁移关键结果（如 Table 14 的 matched vs. mismatched 条件对比）提升到主文。

**N2** [critical] Binary F1=0.694 的实际意义未被充分论证
- 具体位置：§4.1（第 5 页），Abstract，Section 6
- 问题：论文将 binary F1=0.694 作为主要报告指标（"leak-free binary F1"），但未充分讨论这一性能水平是否足以支撑论文声称的应用场景（data provenance、corpus auditing、contamination monitoring）。Abstract 称 "an asymmetry sufficient for cross-generator depth prediction"——但 0.694 意味着约 30% 的样本被错分。错误分析（Appendix i）显示 gen-1/gen-2+ 边界错误率高达 48.4%，这恰恰是实际应用中最关键的区分点。
- 为什么影响接收：论文在 framing 上暗示该方法具有实用价值，但性能数据不支持这一暗示。如果这只是 proof of concept，应明确标注。
- 建议修改方向：(1) 在 §4.1 中明确讨论 0.694 的实际含义——什么样的下游应用能容忍这个错误率？(2) 将 gen-1/gen-2+ 边界的高错误率从 Appendix i 提升到主文讨论；(3) 建议在 Abstract/Introduction 中将论文定位为 "feasibility study" 或 "proof of concept" 而非暗示已解决了 depth profiling 问题。

**N3** [critical] DDR 分解的形式化不足——描述性框架与分类任务之间的逻辑断层
- 具体位置：§4.2（第 6 页），§3.3（第 4 页），Section 5
- 问题：DDR 被定义为 location（drifting）vs. shape（stationary）的分解，用 Cohen's d ≥ 0.20 做分区标准。这一分解的核心价值在于"location drift 足以做分类，shape stability 保证 cross-generator 迁移"。但实际分类器使用的是全部 7 个原始特征（包括 drifting 和 non-drifting 特征），而非 DDR 分解后的某种 derived representation。也就是说，DDR 是一个 post-hoc 解释性框架，而非分类方法的构成部分。论文的叙事暗示 DDR 驱动了分类，但实际上分类器对 DDR 分区无感知。
- 为什么影响接收：如果 DDR 只是描述性的，其作为 "核心贡献" 的权重会降低。审稿人会追问：DDR 分解提供了什么 actionable insight，是单纯使用 7 个特征做分类无法提供的？
- 建议修改方向：(1) 更明确地区分 DDR 作为分析工具 vs. 作为分类方法的角色；(2) 讨论是否可以利用 DDR 分区信息改进分类（如对 drifting/non-drifting 特征分别建模）；(3) 或者调整论文 framing，将 DDR 定位为 empirical finding 而非方法论贡献。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Cohen's d = 0.20 阈值的选择缺乏 task-specific 论证
- 具体位置：§4.2（第 6 页），Appendix u（第 26 页），Appendix v（Table 37）
- 问题：使用 Cohen (1988) 的 "small effect" 惯例阈值 d=0.20 作为 DDR 分区边界。虽然 Appendix v 的敏感性分析显示分区在 ε ∈ [0.10, 0.75] 范围内稳定（Table 37），且 TOST 等价性检验（Appendix u）支持 near-stationary 特征确实 |d| < 0.20，但主文未解释为什么 Cohen 的 behavioral science 标准适用于 NLL 分布的深度分类场景。d=0.20 在此处的统计功效是什么？
- 建议：在 §4.2 中增加 1-2 句话，论证 d=0.20 在本任务中的适当性（如基于 Appendix v 的 silhouette score peak），或明确声明这是一个 working threshold 而非经过优化的选择。

**W2** [warning] XGBoost 固定超参数——未进行调优
- 具体位置：§3.4（第 5 页），Table 3（第 7 页），Appendix g（Table 11）
- 问题：XGBoost 使用 n_estimators=200, max_depth=6, learning rate 0.1，这些接近默认值，且"fixed without tuning"。虽然 Appendix g 的 Table 11 表明多种分类器（LR, RF, Frank-Hall）都能达到合理性能（说明判别力在特征而非分类器），Table 12 的 max_depth 敏感性显示性能变化仅 ±2pp，但完全不做超参调优在方法论上不够严格——尤其论文报告了较窄的 CI（如 [0.688, 0.700]），如果存在 systematic undertuning，CI 不能弥补。
- 建议：运行一次简单的 grid search 或 random search（至少在一个 fold 上），报告调优后的性能是否有显著变化。如果确认性能增益 <1pp，则当前做法可被接受，但需要这个实验结果作为支撑。

**W3** [warning] 参考模型选择（Pythia-410M）的论证不完整
- 具体位置：§3.3（第 4 页），Appendix s（Table 31）
- 问题：论文选择 Pythia-410M 作为参考模型，理由是"chosen to be smaller than all generators"。但为什么"更小"是理想的？更小的参考模型意味着更大的 cross-entropy，这可能放大或掩盖某些深度差异。Appendix s 的 cross-family 验证（3 个参考模型，F1 spread = 0.013）显示选择不敏感，但 Table 31 只测试了 3 个模型——OLMo-2-1B、Qwen3-0.6B/1.7B。
- 建议：(1) 增加对"小参考模型"直觉的简要解释（如避免参考模型与生成器重叠、确保 NLL 值有足够区分度）；(2) 如果可能，增加一个与生成器同规模或更大的参考模型（如 Pythia-1.4B）的测试。

**W4** [warning] 跨域实验规模过小
- 具体位置：Appendix j（第 19-20 页），Table 18
- 问题：cross-domain generalization 实验（Wikipedia → News, Academic, Code）每个域仅 200 seeds × depth 3，总样本量非常小。Table 18 报告 binary F1 = 0.73-0.75（News, Academic）和 0.63（Code），但如此小的样本量下 CI 必然很宽（论文报告了 95% CI 但范围如 [0.717, 0.770]）。代码域（Code）的显著性能下降值得更多讨论。
- 建议：(1) 扩大跨域实验规模（至少 1000+ seeds per domain）；(2) 如果资源有限，明确将跨域实验标注为 preliminary/exploratory；(3) 讨论 Code 域性能下降的可能原因。

**W5** [warning] 5-class 深度分类性能较弱但缺乏主文讨论
- 具体位置：Table 5（Appendix c，第 13 页），Table 7（Appendix e，第 14 页）
- 问题：5-class LOGO 分类 F1 ≈ 0.50（Table 5），QLoRA 在 5-class 上达到 0.583（Table 7）。这表明在当前特征体系下，精细的深度区分（gen-0/1/2/3/4）困难很大。但主文几乎没有讨论这一结果——仅在 Section 5 简要提到"adjacent depths 2-4 become indistinguishable"。作为一个标题包含 "Classifying Recursive Generation Depth" 的论文，应在主文明确讨论深度分辨率的上限。
- 建议：在 §4 或 Section 5 中增加对 5-class 结果的讨论，解释 3-class 折叠（depths 2-4 → 2+）的合理性和 finer-grained 分类的瓶颈。

**W6** [warning] 实验范围的泛化声明可能过度
- 具体位置：Abstract, Section 6 (Conclusion)
- 问题：论文在 Abstract 和 Conclusion 中使用了较强的语言（"empirical regularity of base-model autoregressive generation", "DDR complements concurrent iterative-generation studies"），但实验仅覆盖 8 个生成器（≤5.28B 参数），英文 Wikipedia 种子，单一温度（t=0.7 为主），单一 prompt type（continuation）。虽然 Limitations 承认了这些限制，但 Abstract/Conclusion 的 framing 给人的印象是 DDR 是一个普适的 regularity。
- 建议：在 Abstract 和 Conclusion 中加入适当的 hedging（如 "within our experimental scope" 或 "for small-to-mid-scale base models"），使 claim 强度与证据范围匹配。

---

## 小问题（不影响接收）

1. **Abstract 信息密度高但略显拥挤**：当前 Abstract 将 DDR 定义、分类结果、统计检验、特征分解等全部压缩在约 200 words 内，读者首次阅读时可能难以吸收。建议精简 CI 和效果量的具体数字。
2. **Figure 2 (p.4) 中 (c) LOGO 示意图**：图中 "evaluation folds on one generator" 的表述不够清晰——建议改为 "held-out generator" 以更直接。
3. **Appendix aa (p.36) AI Assistants 声明**：提到使用 Claude 进行 "drafting and revising paper sections" ——这是合规的 ARR 披露，但披露范围较广（writing assistance 涵盖了 drafting），可能引起部分 reviewer 的关注。
4. **术语一致性**："entropy" 在 §3.3 定义为 reference-model NLL（非信息论熵），但后文多处使用 "entropy" 而不加限定，可能造成误解。建议在首次使用后持续标注 "reference-model entropy" 或简写为 "ref-NLL"。
5. **Table 2 (p.5) 排版**：8 个生成器的 per-generator binary F1 列在同一张表中，已经很紧凑但可读性尚可。建议考虑按 family 分组排列以增强可读性。

---

## 格式合规检查

| 检查项 | 结果 | 说明 |
|--------|------|------|
| 正文 ≤8 页 | ✅ 合规 | Sections 1-6（Introduction 至 Conclusion）在第 1-8 页内完成 |
| Limitations section | ✅ 存在 | 第 8-9 页，覆盖 3 个要点（base models only, English Wikipedia, single reference model），内容适当 |
| 匿名化 | ✅ 合规 | 标题页为 "Anonymous ACL submission"，代码链接使用匿名仓库（footnote 1），未发现自引泄露 |
| References 不限页数 | ✅ 合规 | 参考文献在第 9-11 页 |
| Appendix 不计入正文 | ✅ 合规 | 附录从第 11 页开始，共约 25 页 |
| AI Assistants 披露 | ✅ 已披露 | Appendix aa (p.36) |

---

## 主要优势

1. **研究问题新颖且有意义**：从 binary AI detection 扩展到 generation depth classification，这是一个自然且重要的研究方向，与 data provenance、model collapse 等热点问题直接相关。
2. **统计方法论严谨程度远超 ACL 平均水平**：Bootstrap CI、Bonferroni 校正、TOST 等价性检验、permutation testing、Granger 因果分析、ANOVA 方差分解——这种多层次统计验证体系在 NLP 实证论文中罕见。
3. **消融实验极其全面**：26 页附录覆盖了几乎所有可预见的审稿疑问（长度混淆、种子独立性、分类器选择、参考模型选择、温度敏感性、跨域迁移、指令微调模型、解码策略鲁棒性等），显示了扎实的实验设计功底。
4. **DDR 分解提供了有用的分析视角**：将深度差异分解为 location drift + shape stability 是一个直观且可验证的框架，ANOVA 方差分解（Table 48, depth 解释 34-37% 的 location variance 但 <1% 的 shape variance）提供了有力支持。
5. **LOGO/LOFO 交叉验证协议设计合理**：Leave-One-Generator-Out 和 Leave-One-Family-Out 提供了多层次的泛化性测试，gen-0 共享种子问题通过 independent-seed 实验（Appendix t, F1=0.695 vs. 0.694）得到妥善处理。
6. **与现有检测方法的公平对比**（Table 3, §4.3）：将 4 个已有检测器分数重新用作 depth predictor，提供了有意义的 baseline 比较。

---

**总结**：这是一篇实验功底扎实、统计方法严谨的实证研究论文。核心问题在于：(1) 中等性能水平下的实际价值论证不足；(2) 温度敏感性削弱了 "empirical regularity" 的泛化声明；(3) DDR 作为描述性框架与分类任务之间的逻辑连接需要加强。建议接收为 Findings，或在解决 N1-N3 后考虑主会议。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4022 · 2026-05-24T22:58:06.453795+00:00_

Reviewer 1 审稿意见已收到。评分 3.5/5（Borderline Conference），提出 3 个 Must-Fix（温度敏感性讨论不足、binary F1=0.694 实际意义未论证、DDR 形式化与分类任务的逻辑断层）和 6 个 Should-Fix。

等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 390

## Round 390

2 recorded events


### User

_source line 4023 · 2026-05-24T22:58:08.990889+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审查结论**：Overall 3.5（Borderline Conference），建议 Findings 接收。

三个 Must-Fix 问题：
1. 温度敏感性（t=0.9 时 F1 降 15%）在主文中讨论不足，与 "empirical regularity" 的泛化声明矛盾
2. Binary F1=0.694 的实际应用意义未被充分论证，gen-1/gen-2+ 边界错误率 48.4% 是核心瓶颈
3. DDR 分解是 post-hoc 描述性框架，与分类任务之间存在逻辑断层——分类器并未使用 DDR 分区信息

六个 Should-Fix 问题涵盖 Cohen's d 阈值论证、XGBoost 未调参、参考模型选择、跨域实验规模、5-class 性能讨论、泛化声明过度。

主要优势：研究问题新颖、统计方法论严谨（远超 ACL 平均）、消融覆盖全面、LOGO/LOFO 评估协议设计合理。格式完全合规。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4024 · 2026-05-24T22:58:13.985753+00:00_

收到 Reviewer 1 的审稿意见。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 391

## Round 391

6 recorded events


### User

_source line 4025 · 2026-05-24T22:59:36.194028+00:00_

[Reviewer 2 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 提出了genuinely novel的depth profiling任务和clean的DDR经验分解，实验设计thorough，但方法缺乏创新（标准NLL统计量+XGBoost），且仅限base model的适用范围削弱了实际影响力。

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 实验设计扎实：LOGO交叉验证、LOFO特征消融、多种鲁棒性检验（温度/prompt/扰动/跨域）、bootstrap CIs、长度混淆分析。统计方法规范。主要扣分点：gen-1 vs. gen-2+ 的binary F1仅0.694，实际区分能力有限。 |
| Excitement | 3 / 5 | Depth profiling 作为新任务有启发性，DDR 分解（location漂移 vs. shape稳定）是干净的经验发现。但 DDR 的核心观察（NLL均值随depth下降，而分布极值保持稳定）从架构角度看较可预期；方法层面（7个统计量+XGBoost）无创新；仅限 base model 限制了实际价值。 |
| Reproducibility | 4.5 / 5 | 承诺开源代码和数据（脚注1），使用标准工具（XGBoost、Pythia-410M参考模型），实验细节充分（超参数、种子数、评估协议均明确说明），附录提供了大量补充实验。 |
| Overall Assessment | 3.5 / 5 | Borderline Conference — 见下方详细分析 |
| Reviewer Confidence | 4 / 5 | 对 AI 文本检测、model collapse、NLL 分析方法较为熟悉 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] DDR 的新颖性可能不足以支撑主会议级别贡献
- 具体位置：§4.2 Differential Depth Response, §5 Discussion
- 问题：DDR 的核心发现可拆解为两个已知/可预期的观察：(1) NLL 均值（location）随递归深度单调下降——这与 Shumailov et al. (2024) 的尾部侵蚀和 Dohmatob et al. (2024) 的 scaling law 退化方向一致，只是场景不同（inference chain vs. training loop）；(2) shape 特征（entropy_max, entropy_min, tail_decay）近似不变——论文自己在 §5 解释为 "architecturally bounded: entropy max by log|V|, tail decay by softmax geometry"，这意味着shape稳定性是模型架构的固有约束，而非递归生成的独特发现。如果核心发现可从已知架构约束推导，则 DDR 的 contribution 更多是验证性的而非发现性的。
- 为什么影响接收：Excitement 是 Conference 接收的关键维度。如果 DDR 被视为 "predictable from first principles"，则论文的核心贡献（经验分解）价值降低。
- 建议修改方向：(1) 需要更深入地论证为什么 shape 稳定性不是 trivially predictable——例如，是否存在反例场景下 shape 也会漂移？温度或模型大小的边界条件？(2) 或者强化 DDR 的 downstream utility，展示它在实际 corpus auditing 场景中的不可替代性。

**N2** [critical] 仅限 Base Model 的适用范围严重限制实际价值
- 具体位置：Limitations (p.9), Appendix k (Table 19-20, p.20)
- 问题：Instruction-tuned 模型下 DDR 信号大幅压缩（3-class F1 下降 3.7–19.9 pp, Table 19）。虽然 QLoRA 部分恢复（F1=0.89-0.91），但这仅是 within-model 的结果（5-fold CV on same instruct set），不是 cross-generator 评估——而 cross-generator transfer 正是论文的核心卖点。现实中遭遇的递归生成文本几乎全部来自 instruction-tuned 或 RLHF 模型，base model 直接续写的场景极为罕见。
- 为什么影响接收：如果方法在实际最常见的文本生成场景下失效，则论文的 practical motivation（"data provenance and corpus curation"，§1第一段）难以成立。
- 建议修改方向：(1) 明确讨论为什么 base model 场景本身有独立价值（例如 pretraining data contamination 检测中，base model 生成的合成数据确实被用于扩充语料）；(2) 或补充 instruction-tuned 模型下的 LOGO 评估结果，即使性能下降也应报告。

**N3** [critical] Gen-1 vs. Gen-2+ 区分能力有限，核心 claim 的实验支撑不够强
- 具体位置：§4.1 (p.5), Table 2 (p.6)
- 问题：论文的核心新贡献在于区分不同 generation depth（不是简单的 human vs. machine binary detection）。排除 gen-0 后，gen-1 vs. gen-2+ 的 leak-free binary F1 = 0.694（Table 2 平均），且部分 generator 的表现更差。Error analysis (Appendix i, p.17) 显示 gen-1→gen-2+ 边界的错误率高达 48.4%，即近一半的 gen-2+ 文本被错分为 gen-1。这意味着 depth profiling 在最关键的深度区分（"是否经历了多次递归"）上接近随机。3-class F1=0.762 看似不错，但被 gen-0 的高可分性（gen-0 近乎完美分类，Table 25 aggregated confusion matrix）拉高——而 gen-0 vs. gen-1+ 的区分本质上就是 binary AI detection。
- 为什么影响接收：如果 depth profiling 在排除 trivial 的 gen-0 分类后性能大幅下降，则 "depth profiling" 相对于 binary detection 的增量价值存疑。
- 建议修改方向：(1) 更透明地报告 gen-1 vs. gen-2+ 的分类性能作为核心指标，而非强调包含 gen-0 的 3-class F1；(2) 分析 gen-1/gen-2+ 边界的 oracle performance 上限（例如最佳单 generator 内分类性能 vs. 跨 generator），帮助读者判断这是方法瓶颈还是任务固有难度。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Entropy" 术语滥用可能误导读者
- 具体位置：§3.3 Terminology 段落, Table 1, 全文
- 问题：论文在 §3.3 定义 "we refer to per-token cross-entropy loss under a fixed reference model as 'entropy' for conciseness"，但 "entropy" 在信息论中有精确含义（分布的自信息期望），与 reference-model cross-entropy 是不同量。全文所有特征名（entropy_mean, entropy_std, entropy_max, entropy_min）都使用这个误导性术语。特别是在 DDR 分析中讨论 "entropy stability" 时（§4.2, §5），读者可能误以为是生成分布本身的 entropy 不变，而实际是参考模型下的 cross-entropy 某些统计量不变——这是完全不同的概念。
- 建议：全文统一使用 "NLL" 或 "cross-entropy"，或至少在特征命名中使用 "nll_mean", "nll_std" 等，消除歧义。

**W2** [warning] 与 Concurrent Work 的实证对比缺失
- 具体位置：§2 Related Work (p.3), Appendix z.8 (p.35, Table 52)
- 问题：论文在 §2 和 Appendix z.8 中与三项 concurrent work（Broken Telephone, Markovian Chains, Attractor Cycles）做了概念层面的对比（chain type, analysis lens, downstream utility），但缺少实证对比。例如：(1) 在 paraphrasing chain（Broken Telephone 的设置）上，DDR 是否仍然成立？(2) 在 greedy decoding 下（Attractor Cycles 关注的设置），DDR 的 shape 稳定性是否被 convergence 打破？Appendix z.5 的 decoding strategy 分析（greedy/top-k）部分回答了第二个问题，但论文没有 explicitly connect 这些结果到 concurrent work 的对比框架。
- 建议：在 Appendix z.8 的比较中加入对 DDR 在不同 chain operator 下的实证数据引用（从已有附录实验中提取），使概念对比有数据支撑。

**W3** [warning] 缺少 OOD Detection 方法论的讨论
- 具体位置：§2 Related Work
- 问题：论文使用的 NLL 统计特征（均值、方差、极值）与 NLP 中 Out-of-Distribution (OOD) detection 的方法论高度重叠。OOD detection 领域已有大量工作基于 NLL/perplexity/Mahalanobis distance 进行分布外检测，且近期有工作（如 "Human Texts Are Outliers"，arXiv 2510.08602）直接将 AI 文本检测重构为 OOD detection 问题。这一方法论连接在 Related Work 中完全缺失。
- 建议：在 Related Work 中增加对 OOD detection 方法论的简要讨论，说明 depth profiling 与 OOD detection 的区别（ordinal vs. binary, cross-generator transfer requirement）。

**W4** [warning] Abstract 信息密度略有失衡
- 具体位置：Abstract (p.1)
- 问题：Abstract 约 171 词（符合 200 词限制），但堆叠了过多具体 F1 数字（0.694, 0.830, 0.762, 0.905）和 effect size（d=0.74–1.05, d<0.10, d=0.46, ≥8×），使可读性下降。部分数字（如 QLoRA 的 F1=0.905）是附录结果，出现在 abstract 中优先级有疑问。
- 建议：精简为 2-3 个核心数字（如 LOGO 3-class F1 和 ≥8× effect-size gap），将 QLoRA 等次要结果移除。

**W5** [warning] Discussion §5 中的因果/机制解释缺乏充分支撑
- 具体位置：§5 Discussion 第1段
- 问题：§5 声称 DDR 反映 "monotonic compression of the token-level NLL distribution"，并将 shape 稳定性归因于 "architecturally bounded—entropy max by log|V|, tail decay by softmax geometry"。但这些是 post-hoc 的直觉性解释，没有formal proof 或 controlled experiment 支撑。例如，如果 shape 稳定性确实由 log|V| 上界决定，那么不同 vocabulary size 的模型应该展现不同的 shape 稳定性——但论文中 Pythia（50K vocab）和 Qwen（150K+ vocab）展现了类似的 shape 稳定性（Table 33, Appendix u），这可能反驳了 log|V| 解释。
- 建议：将机制解释明确标注为 hypothesis/conjecture，或补充不同 vocab size 对 shape 稳定性影响的分析。

## 小问题（不影响接收）

- §3.2 (p.4): "Each seed is iteratively fed through the generator to produce a chain of depth 4" — 后面又说 "We generate up to depth 4; by empirically confirmed convergence, 5-class analysis shows adjacent depths 2–4 become indistinguishable"。建议在方法部分统一说明为什么 depth=4 是合理截断点，避免读者需要跳转到附录。
- Figure 2 (p.4): Framework 图中 (a) 和 (b) 的区别（generation chain vs. feature extraction）可以更清晰地标注。当前的 "gen-0 (Human)" 标签暗示 gen-0 一定是人类文本，但 gen-0 实际上也可以是任何 seed text。
- Table 3 (p.7): Baseline comparison 中 Binoculars 的 binary F1 = 0.539 远低于其在 binary AI detection 中的 SOTA 表现，说明 Binoculars 不适用于 depth classification——但论文没有 explicitly 分析为什么（是因为 Binoculars 设计用于 human vs. machine，而 gen-1 和 gen-2+ 都是 machine text？）。
- Appendix aa (p.36): Use of AI Assistants 的披露是诚实透明的，但 "Writing: drafting and revising paper sections" 的表述可能过于宽泛，ARR 可能对 AI 用于写作有更具体的政策要求。
- §1 (p.1): 脚注1提到 "Code and data are publicly available" 并指向匿名 GitHub repo——需确认 double-blind 下该链接是否符合 ARR 匿名政策（anonymous repo 通常是允许的）。

## 主要优势

1. **Task formulation 的原创性**: "Depth profiling" 作为 ordinal depth classification 任务是genuinely novel的贡献，填补了 binary detection 和 model collapse 分析之间的空白。这个 framing 有独立的学术价值，可能启发后续研究。

2. **实验设计的严谨性**: 论文的实验方法论是其最大优势——LOGO 交叉验证避免 generator leakage，LOFO 特征消融验证每个特征的贡献，多达 20+ 个附录实验覆盖了温度敏感性、prompt 泛化、文本扰动鲁棒性、跨域迁移、解码策略、参考模型选择等。这种实验覆盖度在 empirical study 中是exemplary的。

3. **DDR 分解的清晰性**: Location drift vs. shape stability 的二元分解是干净、可量化的经验发现（≥8× effect-size gap），ANOVA 方差分解（Figure 7）提供了有力的统计支撑。

4. **诚实的局限性讨论**: 论文坦率地报告了 instruction-tuned 模型下的性能退化、gen-1/gen-2+ 边界的高错误率、以及 base-model-only 的适用限制，没有 overclaim。

5. **广泛的 concurrent work 对比**: §2 和 Appendix z.8 与三项 concurrent iterative-generation studies 做了清晰的概念区分，对比框架合理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 4026 · 2026-05-24T23:00:21.542140+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿意见\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] DDR 的新颖性可能不足以支撑主会议级别贡献\n- DDR 的核心发现可拆解为两个已知/可预期的观察：(1) NLL 均值（location）随递归深度单调下降——这与 Shumailov et al. (2024) 的尾部侵蚀和 Dohmatob et al. (2024) 的 scaling law 退化方向一致；(2) shape 特征近似不变——论文自己在 §5 解释为 \"architecturally bounded: entropy max by log|V|, tail decay by softmax geometry\"，这意味着 shape 稳定性是模型架构的固有约束，而非递归生成的独特发现。\n\n**N2** [critical] 仅限 Base Model 的适用范围严重限制实际价值\n- Instruction-tuned 模型下 DDR 信号大幅压缩（3-class F1 下降 3.7–19.9 pp）。QLoRA 恢复仅是 within-model 5-fold CV，不是 cross-generator 评估。现实中递归生成文本几乎全部来自 instruction-tuned 或 RLHF 模型。\n\n**N3** [critical] Gen-1 vs. Gen-2+ 区分能力有限，核心 claim 的实验支撑不够强\n- Binary F1=0.694，error analysis 显示 gen-1→gen-2+ 边界错误率 48.4%。3-class F1=0.762 被 gen-0 的高可分性拉高，而 gen-0 vs. gen-1+ 本质上就是 binary AI detection。\n\n### Should-Fix 问题\n\n**W1** [warning] \"Entropy\" 术语滥用可能误导读者\n- \"entropy\" 在信息论中有精确含义，与 reference-model cross-entropy 不同。全文特征名（entropy_mean 等）使用误导性术语。\n\n**W2** [warning] 与 Concurrent Work 的实证对比缺失\n- 与 Broken Telephone, Markovian Chains, Attractor Cycles 仅做概念对比，缺少实证对比（如 paraphrasing chain 下 DDR 是否成立）。\n\n**W3** [warning] 缺少 OOD Detection 方法论的讨论\n- NLL 统计特征与 OOD detection 方法论高度重叠，但 Related Work 中完全缺失此连接。\n\n**W4** [warning] Abstract 信息密度略有失衡\n- 堆叠过多 F1 数字和 effect size，QLoRA 的 F1=0.905 是附录结果但出现在 abstract。\n\n**W5** [warning] Discussion §5 中的因果/机制解释缺乏充分支撑\n- Shape 稳定性归因于 \"log|V| bound\" 和 \"softmax geometry\" 是 post-hoc 直觉解释。Pythia (50K vocab) 和 Qwen (150K+ vocab) 展现类似 shape 稳定性可能反驳 log|V| 解释。\n\n### 主要优势\n1. Task formulation 的原创性\n2. 实验设计的严谨性\n3. DDR 分解的清晰性\n4. 诚实的局限性讨论\n5. 广泛的 concurrent work 对比",
  "project": "gen-depth-fingerprint",
  "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
  "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿意见\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] DDR 的新颖性可能不足以支撑主会议级别贡献\n- DDR 的核心发现可拆解为两个已知/可预期的观察：(1) NLL 均值（location）随递归深度单调下降——这与 Shumailov et al. (2024) 的尾部侵蚀和 Dohmatob et al. (2024) 的 scaling law 退化方向一致；(2) shape 特征近似不变——论文自己在 §5 解释为 \"architecturally bounded: entropy max by log|V|, tail decay by softmax geometry\"，这意味着 shape 稳定性是模型架构的固有约束，而非递归生成的独特发现。\n\n**N2** [critical] 仅限 Base Model 的适用范围严重限制实际价值\n- Instruction-tuned 模型下 DDR 信号大幅压缩（3-class F1 下降 3.7–19.9 pp）。QLoRA 恢复仅是 within-model 5-fold CV，不是 cross-generator 评估。现实中递归生成文本几乎全部来自 instruction-tuned 或 RLHF 模型。\n\n**N3** [critical] Gen-1 vs. Gen-2+ 区分能力有限，核心 claim 的实验支撑不够强\n- Binary F1=0.694，error analysis 显示 gen-1→gen-2+ 边界错误率 48.4%。3-class F1=0.762 被 gen-0 的高可分性拉高，而 gen-0 vs. gen-1+ 本质上就是 binary AI detection。\n\n### Should-Fix 问题\n\n**W1** [warning] \"Entropy\" 术语滥用可能误导读者\n- \"entropy\" 在信息论中有精确含义，与 reference-model cross-entropy 不同。全文特征名（entropy_mean 等）使用误导性术语。\n\n**W2** [warning] 与 Concurrent Work 的实证对比缺失\n- 与 Broken Telephone, Markovian Chains, Attractor Cycles 仅做概念对比，缺少实证对比（如 paraphrasing chain 下 DDR 是否成立）。\n\n**W3** [warning] 缺少 OOD Detection 方法论的讨论\n- NLL 统计特征与 OOD detection 方法论高度重叠，但 Related Work 中完全缺失此连接。\n\n**W4** [warning] Abstract 信息密度略有失衡\n- 堆叠过多 F1 数字和 effect size，QLoRA 的 F1=0.905 是附录结果但出现在 abstract。\n\n**W5** [warning] Discussion §5 中的因果/机制解释缺乏充分支撑\n- Shape 稳定性归因于 \"log|V| bound\" 和 \"softmax geometry\" 是 post-hoc 直觉解释。Pythia (50K vocab) 和 Qwen (150K+ vocab) 展现类似 shape 稳定性可能反驳 log|V| 解释。\n\n### 主要优势\n1. Task formulation 的原创性\n2. 实验设计的严谨性\n3. DDR 分解的清晰性\n4. 诚实的局限性讨论\n5. 广泛的 concurrent work 对比",
    "project": "gen-depth-fingerprint",
    "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
    "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
  }
}
```

</details>

---


### Tool result

_source line 4027 · 2026-05-24T23:00:45.405744+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23863
}
```

</details>

---


### Tool call

_source line 4028 · 2026-05-24T23:00:46.010402+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿意见\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] 温度敏感性对泛化声明的削弱——主文讨论不充分\n- t=0.9 时 3-class F1 从 0.762 降至 0.647（−15%），95% CI 不重叠。Cross-temperature 迁移实验显示 t=0.7 训练→t=1.0 测试时性能严重退化。但主文 §4.3 仅用约 3 行简要提及，Limitations 也只说 \"single decoding regime\"。与 Conclusion 中 \"DDR is an empirical regularity\" 的强声明矛盾。\n\n**N2** [critical] Binary F1=0.694 的实际意义未被充分论证\n- 0.694 意味着约 30% 样本被错分。Error analysis 显示 gen-1/gen-2+ 边界错误率高达 48.4%。论文 framing 暗示实用价值，但性能数据不支持。应明确定位为 \"feasibility study\" 或 \"proof of concept\"。\n\n**N3** [critical] DDR 分解的形式化不足——描述性框架与分类任务之间的逻辑断层\n- DDR 是 post-hoc 解释性框架，分类器对 DDR 分区无感知（使用全部 7 个原始特征而非 DDR 分解后的 derived representation）。叙事暗示 DDR 驱动了分类，但实际上 DDR 只是描述性的。\n\n### Should-Fix 问题\n\n**W1** [warning] Cohen's d = 0.20 阈值缺乏 task-specific 论证\n\n**W2** [warning] XGBoost 固定超参数——未进行调优\n- n_estimators=200, max_depth=6, lr=0.1 接近默认值，\"fixed without tuning\"。CI 较窄 [0.688, 0.700]，但可能存在 systematic undertuning。\n\n**W3** [warning] 参考模型选择（Pythia-410M）论证不完整\n- 为什么\"更小\"是理想的？Cross-family 仅测试 3 个参考模型。\n\n**W4** [warning] 跨域实验规模过小\n- 每域仅 200 seeds × depth 3，样本量小，Code 域性能下降（F1=0.63）缺乏讨论。\n\n**W5** [warning] 5-class 深度分类性能较弱但缺乏主文讨论\n- 5-class F1 ≈ 0.50，QLoRA 5-class = 0.583。主文几乎没有讨论这一结果。\n\n**W6** [warning] 实验范围的泛化声明可能过度\n- Abstract/Conclusion 使用 \"empirical regularity\" 等较强语言，但实验覆盖有限（≤8B 参数，英文 Wikipedia，单一温度）。\n\n### 主要优势\n1. 研究问题新颖且有意义\n2. 统计方法论严谨程度远超 ACL 平均\n3. 消融实验极其全面（26 页附录）\n4. DDR 分解提供有用分析视角（ANOVA 支持）\n5. LOGO/LOFO 评估协议设计合理\n6. 与检测 baselines 的公平对比",
  "project": "gen-depth-fingerprint",
  "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
  "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿意见\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] 温度敏感性对泛化声明的削弱——主文讨论不充分\n- t=0.9 时 3-class F1 从 0.762 降至 0.647（−15%），95% CI 不重叠。Cross-temperature 迁移实验显示 t=0.7 训练→t=1.0 测试时性能严重退化。但主文 §4.3 仅用约 3 行简要提及，Limitations 也只说 \"single decoding regime\"。与 Conclusion 中 \"DDR is an empirical regularity\" 的强声明矛盾。\n\n**N2** [critical] Binary F1=0.694 的实际意义未被充分论证\n- 0.694 意味着约 30% 样本被错分。Error analysis 显示 gen-1/gen-2+ 边界错误率高达 48.4%。论文 framing 暗示实用价值，但性能数据不支持。应明确定位为 \"feasibility study\" 或 \"proof of concept\"。\n\n**N3** [critical] DDR 分解的形式化不足——描述性框架与分类任务之间的逻辑断层\n- DDR 是 post-hoc 解释性框架，分类器对 DDR 分区无感知（使用全部 7 个原始特征而非 DDR 分解后的 derived representation）。叙事暗示 DDR 驱动了分类，但实际上 DDR 只是描述性的。\n\n### Should-Fix 问题\n\n**W1** [warning] Cohen's d = 0.20 阈值缺乏 task-specific 论证\n\n**W2** [warning] XGBoost 固定超参数——未进行调优\n- n_estimators=200, max_depth=6, lr=0.1 接近默认值，\"fixed without tuning\"。CI 较窄 [0.688, 0.700]，但可能存在 systematic undertuning。\n\n**W3** [warning] 参考模型选择（Pythia-410M）论证不完整\n- 为什么\"更小\"是理想的？Cross-family 仅测试 3 个参考模型。\n\n**W4** [warning] 跨域实验规模过小\n- 每域仅 200 seeds × depth 3，样本量小，Code 域性能下降（F1=0.63）缺乏讨论。\n\n**W5** [warning] 5-class 深度分类性能较弱但缺乏主文讨论\n- 5-class F1 ≈ 0.50，QLoRA 5-class = 0.583。主文几乎没有讨论这一结果。\n\n**W6** [warning] 实验范围的泛化声明可能过度\n- Abstract/Conclusion 使用 \"empirical regularity\" 等较强语言，但实验覆盖有限（≤8B 参数，英文 Wikipedia，单一温度）。\n\n### 主要优势\n1. 研究问题新颖且有意义\n2. 统计方法论严谨程度远超 ACL 平均\n3. 消融实验极其全面（26 页附录）\n4. DDR 分解提供有用分析视角（ANOVA 支持）\n5. LOGO/LOFO 评估协议设计合理\n6. 与检测 baselines 的公平对比",
    "project": "gen-depth-fingerprint",
    "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
    "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
  }
}
```

</details>

---


### Tool result

_source line 4029 · 2026-05-24T23:00:47.369655+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1359
}
```

</details>

---


### Assistant

_source line 4030 · 2026-05-24T23:00:51.074420+00:00_

交叉分享已派发。两位 Reviewer 正在审阅对方意见并准备逐条回应。等待 [AGREE]/[REBUT] 结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 392

## Round 392

2 recorded events


### User

_source line 4031 · 2026-05-24T23:00:53.632219+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：评分 Overall 3.5（Borderline Conference）。论文提出了genuinely novel的depth profiling任务和clean的DDR经验分解，实验设计在empirical study中属exemplary水准（20+附录实验）。三个Must-Fix问题：(1) DDR的shape稳定性可能从架构约束trivially推导，新颖性需更深论证；(2) 仅限base model，instruction-tuned模型下信号大幅退化，限制实际价值；(3) 排除trivial的gen-0分类后，gen-1 vs. gen-2+的binary F1仅0.694（48.4%错误率），depth profiling相对于binary detection的增量价值存疑。五个Should-Fix问题涉及术语误用（"entropy"代指NLL）、缺少OOD detection方法论讨论、concurrent work缺乏实证对比等。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 4032 · 2026-05-24T23:00:57.330893+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 393

## Round 393

2 recorded events


### User

_source line 4033 · 2026-05-24T23:02:28.446392+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 的交叉回应

### Must-Fix 回应

**[AGREE] R2-N1: DDR 新颖性可能不足**
同意 R2 的分析框架。DDR 的两个组件可回溯到已知现象：location drift 与 Shumailov et al. (2024) 方向一致，shape stability 被论文自身 §5 解释为架构约束。但补充：贡献不在于单独观察 drift 或 stability，而在于将两者组合为可操作的分类框架并通过 LOGO 验证跨生成器迁移。Model collapse 研究 training-time degradation，本文研究 inference-time recursive generation——§5 做了区分但缺乏 empirical 验证两者统计签名的差异。整体而言更适合 Findings 级别贡献。

**[AGREE] R2-N2: Base Model 限制**
完全同意。Appendix k（Table 19）显示 instruction-tuned 模型下 cross-condition transfer（base→instruct）F1=0.490，信号不可直接迁移。QLoRA F1=0.905 是 within-model 5-fold CV 而非 LOGO，被放在 Abstract 中可能误导。论文标题标注了 "Base-Model"，Limitations 也承认了，但对实际应用 gap 讨论不够直接。

**[AGREE] R2-N3: Gen-1 vs. Gen-2+ 区分能力有限**
强烈同意，与我的 N2 一致。R2 提出了一个关键洞察：3-class F1=0.762 被 gen-0 高可分性拉高（gen-0 F1=0.921, gen-1 仅 0.634, gen-2+ 仅 0.639）。Gen-0 vs. gen-1+ 本质是 binary human-vs-AI detection——论文相对于现有检测方法的 incremental value 应由 gen-1 vs. gen-2+ 区分能力衡量，而非 3-class F1。

### Should-Fix 回应

**[AGREE] R2-W1: "Entropy" 术语误导**
同意，与我的小问题 #4 一致。建议统一使用 "reference-model NLL" 或 "ref-entropy"。

**[REBUT] R2-W2: Concurrent Work 实证对比缺失**
部分不同意。Paraphrasing chain 与 base-model continuation chain 机制不同，要求跨设置实证复现标准过高。§5 和 Appendix z.8 已做概念对比。但同意增加一个 paraphrase prompt 测试 DDR mechanism independence 会加强说服力。

**[AGREE] R2-W3: OOD Detection 方法论连接缺失**
同意。NLL-based distributional shift detection 与 OOD detection 文献高度重叠，Related Work 应补充。

**[AGREE] R2-W4: Abstract 中 QLoRA F1=0.905 位置不当**
同意。Appendix 结果不应突出在 Abstract 中，尤其是 within-model CV vs. LOGO 的实验设置差异可能引起 cherry-picking 怀疑。

**[REBUT] R2-W5: log|V| 解释被 vocab size 差异反驳**
部分不同意具体反驳论据：log|V| bound 对所有 vocab size 都成立，实际 entropy max 远低于上界（Figure 8 显示约 4-5 vs. log 50K≈10.8），vocab size 差异不影响 shape stability 的定性表现。但同意核心关切：§5 的机制解释是 post-hoc 直觉，缺乏形式化验证。

### 与 R2 共识

Overall 3.5（Borderline Conference），两位 reviewer 核心共识：(1) 研究问题新颖、实验严谨；(2) 实际影响力受限于 base model + moderate performance + temperature sensitivity；(3) DDR 贡献定位需从 "方法论贡献" 调整为 "empirical finding"。建议 Findings 接收。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4034 · 2026-05-24T23:02:39.219867+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 394

## Round 394

14 recorded events


### User

_source line 4035 · 2026-05-24T23:02:40.319694+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 温度敏感性对泛化声明的削弱**

同意这是一个实质性问题。从 Table 13 (p.16) 可以看到，t=0.9 时 binary F1 (gen-1 vs. gen-2+) 确实显著下降。Appendix p (p.24) 的 cross-temperature transfer 实验进一步显示，t=0.7 训练→t=1.0 测试时性能退化严重。主文 §4.3 仅用约 3 行轻描淡写，Limitations 中也只是泛泛提及 "fixed decoding regime"，这与 Conclusion 中 "DDR is a descriptive empirical regularity" 的强声明确实存在张力。

补充我的观察：Appendix p (p.24) 实际上提供了一些温度转移的正面证据——t=0.7↔1.0 的部分 generator 保持了合理性能（F1=0.723 reverse transfer），但 Qwen-1.7B 在 cross-temperature 条件下 F1 降至 0.418，显示 generator-specific 的温度脆弱性。这恰恰说明 "empirical regularity" 的表述需要加上温度条件限定。

**[AGREE] R1-N2: Binary F1=0.694 的实际意义**

完全同意，这与我在自己审稿中提出的 N3 问题高度一致。gen-1 vs. gen-2+ 的 binary F1=0.694 意味着核心的 depth discrimination 任务（排除 trivial 的 gen-0 分类后）接近随机水平。Error analysis (Appendix i, p.17-18) 明确显示 gen-2+ 被误分为 gen-1 的比例达 48.4%。

我同意 Reviewer 1 的建议：论文应明确定位为 "feasibility study" 或 "proof of concept"，而非暗示当前已达到实用水平。当前的 framing（§1 第一段 "data provenance and corpus curation"）给读者一种工具已经可用的印象。

**[REBUT] R1-N3: DDR 分解的形式化不足——描述性框架与分类任务之间的逻辑断层**

我部分不同意这个问题的严重性。

Reviewer 1 指出 DDR 是 post-hoc 描述性框架，分类器使用全部 7 个原始特征而非 DDR-derived representation，因此 DDR 和分类之间存在 "逻辑断层"。但我认为这对论文的定位是一个误解：

1. **论文的核心贡献是经验发现，不是方法**。DDR 的价值在于 *解释为什么简单特征能跨 generator 工作*，而非作为分类管线的一个组件。这类似于 "bias-variance tradeoff" 解释了为什么某些模型在特定场景下更优，但我们不会要求分类器显式地编码 bias-variance 分解。

2. **LOFO 分析 (Table 8-9, p.15) 实证验证了 DDR 分区的分类功能性**。移除 entropy_max（shape 特征）导致最大 F1 下降（Δ=−0.019），移除 entropy_mean（location 特征）次之（Δ=−0.012）。两类特征独立贡献分类性能，与 DDR 框架一致。Table 9 的 minimal sufficient subset 分析显示，最佳 2 特征组合（1 drifting + 1 stationary）达到全集 88% 的性能，直接支持 DDR 的 "两组互补" 叙事。

3. **ANOVA 方差分解 (Figure 7, §5) 进一步支撑 DDR 分区**：η²_depth=0.34–0.37 for location vs. <0.01 for shape（>48× gap），η²_gen≈0.02 across both groups。这不是 post-hoc cherry-picking，而是正式的统计分解。

但我同意 Reviewer 1 的一个隐含建议：论文可以更清晰地表述 DDR 是 *解释性* 框架而非 *处方性* 分类组件。§4.2 和 §5 的叙事确实有时暗示 DDR "驱动" 了分类，而更准确的表述是 DDR "解释" 了为什么分类有效。这是 writing 问题而非 substance 问题。

---

### Should-Fix 问题

**[AGREE] R1-W1: Cohen's d=0.20 阈值缺乏 task-specific 论证**

同意。d=0.20 来自 Cohen (1988) 的通用 "small effect" 标准，但不同任务对 "negligible" 的定义不同。Appendix u (p.28) 的 TOST 分析使用了这个阈值，并讨论了 rationale，但缺乏 task-specific 的 sensitivity analysis（例如，d=0.15 或 d=0.25 时结论是否变化）。不过，这不影响核心结论——Table 36 (p.28) 显示 shape 特征即使在更宽松的 ε=0.25 下也 consistently pass TOST，而 drifting 特征在任何合理 ε 下都 reject。

**[AGREE] R1-W2: XGBoost 固定超参数**

同意这是一个有效关切。但我想指出 Table 11 (p.16) 的 classifier sensitivity 分析在一定程度上缓解了这个问题：Logistic Regression (F1=0.71)、Random Forest (F1=0.725)、XGBoost (F1=0.762) 三种分类器性能排序一致，且线性模型也达到 0.71，说明分类性能主要来自特征而非分类器超参数。如果 XGBoost 的默认超参数已经不显著劣于调优版本，那么 "systematic undertuning" 的风险较低。当然，补充一个简单的 grid search 结果会更有说服力。

**[AGREE] R1-W3: 参考模型选择论证不完整**

同意。Appendix 的 cross-reference 分析（Table 31, Appendix o, p.26）仅测试 3 个参考模型（Pythia-410M, OLMo-2-1B, Qwen-0.6B），F1 spread=0.013。虽然 spread 很小，但 3 个模型不足以得出 "reference model agnostic" 的结论。特别是，所有 3 个参考模型都是 ≤1B 的小模型，没有测试更大的参考模型（如 3B+）是否会改变 DDR pattern。

补充：论文选择 Pythia-410M 的理由是 "chosen to be smaller than all generators"（§3.3），这在方法论上是合理的（避免参考模型能力超过生成模型），但 "更小更好" 的 claim 缺乏系统验证。

**[AGREE] R1-W4: 跨域实验规模过小**

同意。Appendix j (p.19) 的跨域实验每域仅 200 seeds × depth 3，总量约 2400 samples/domain。且 Code 域 binary F1 降至 0.63，说明 domain shift 是一个真实问题。论文对 Code 域的下降几乎没有分析——是因为代码文本的 NLL 分布本身就不同？还是 Wikipedia-trained 参考模型在代码上的 NLL 不再有区分力？这些问题值得讨论。

**[AGREE] R1-W5: 5-class 深度分类性能较弱但缺乏主文讨论**

同意。Table 5 (p.13) 显示 5-class LOGO F1≈0.50，QLoRA 5-class=0.583。这是一个重要的结果——它表明深度分辨率被 bound 在约 3 classes，更细粒度的分类实质上不可行。但主文仅在 Limitations (p.9) 中用一句话提及 "finer-grained 5-class classification yields F1≈0.50 with deeper depths mutually indistinguishable"。考虑到 depth profiling 的 framing 暗示任意深度的分类可能性，主文应该更显著地讨论这一天花板。

**[REBUT] R1-W6: 实验范围的泛化声明可能过度**

部分不同意。Reviewer 1 认为 "empirical regularity" 等表述过强，但我认为在论文的实际实验覆盖范围内，这一表述是可以成立的：
- 8 generators from 5 families（Pythia, OLMo, Qwen, Llama, Mistral）——涵盖了当前主流开源 base model 的大部分 family
- 附录扩展到 9 generators（加入 Gemma-2-2B），结论一致
- 3 种 decoding strategies（greedy, top-k, nucleus）保持 DDR pattern（Appendix z.5, p.33-34）
- 3 种 prompt types 保持一致（Appendix c, p.13）
- 3 个参考模型 spread=0.013（Appendix o）

"Empirical regularity" 不等于 "universal law"——它明确标记为经验观察，且论文在 Limitations 中承认了英文、base model、固定温度的限制。我认为在当前覆盖范围内使用这一术语是合理的，但 R1 关于温度条件的 N1 问题确实削弱了这一表述——如果 DDR 在 t=0.9 下显著退化，那么应该加上温度限定条件。

---

### 对 Reviewer 1 优势评价的补充

完全同意 R1 列出的 6 点优势。特别是第 2 点（统计方法论严谨）和第 3 点（消融实验全面），这是论文最大的亮点。我在自己的审稿中也将 "实验设计的严谨性" 列为首要优势。

### 综合评判

我和 Reviewer 1 对论文的总体评价一致（3.5 Borderline Conference），核心分歧在 N3（DDR 形式化问题）：
- R1 认为 DDR 与分类之间存在 "逻辑断层"，我认为 DDR 作为解释性框架是合理的，LOFO/ANOVA 提供了充分的经验支撑。
- 但 R1 的观察有价值——论文的叙事确实在 "DDR 解释分类" 和 "DDR 驱动分类" 之间摇摆，修正这一 framing 是必要的 writing fix。

两位 Reviewer 共识的核心问题：(1) gen-1/gen-2+ 区分能力有限（F1=0.694）；(2) base-model-only 限制；(3) 温度条件需要限定。这三点建议作者重点回应。

---

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

与 R2 高度一致：6 条 [AGREE]、2 条 [REBUT]（均为部分反驳）。核心共识是 Overall 3.5，建议 Findings 接收。两处 REBUT 分别是：(1) concurrent work 实证对比要求标准过高；(2) log|V| 的 vocab size 反驳论据在技术上不成立，但同意机制解释是 post-hoc 猜测。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 4036 · 2026-05-24T23:03:04.026866+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 4037 · 2026-05-24T23:03:04.529462+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T22:50:56.506443+00:00\", \"completed_at\": \"2026-05-24T22:55:16.204193+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item。第一个视觉锚点 Figure 1（feature trajectories）出现在 page 2 顶部，传达核心 DDR 概念，信息清晰。Title/Abstract 排版整洁专业。审稿人需翻到第 2 页才获得视觉锚定，但 Abstract 信息密度高，影响有限。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 四面板线图清晰可读，颜色可区分（每个 generator 独立颜色），caption 自包含（解释了 DDR 定义）。作为首个 display item，有效传达核心 message。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2（pipeline 架构图）整体清晰，但部分内部文字框（如分类标签 \\\"drifting/intermediate/near-stationary\\\"）字号偏小，建议适当放大以确保打印可读性。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 3（8×8 transfer matrix heatmap）单元格内数字字号偏小，但在屏幕阅读时仍可辨识。红色渐变色板区分度良好。Caption 自包含。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 4（DDR drifting features）位于右栏，尺寸偏小。数据点和 axis labels 处于可读性下限（约正文 70%），建议在修改时考虑适当放大或改为跨栏 figure*。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"单页包含 3 个 display items（Figure 5 + Figure 6 + Table 3），信息密度极高。排版合理未溢出，但视觉上略显拥挤。Figure 6 的 scatter plot 中部分 detector 名称标注可能重叠。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 7（ANOVA bar chart）清晰可读。Discussion 和 Conclusion 在同一页，布局合理。页面利用率 >90%。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段简短（约 3 行），符合 EMNLP 要求。References 从本页中部开始，排版正常。\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Figure 8（violin plots）占据整页，7 个子图。整体分辨率足够，颜色方案区分度好（每个 depth 一种颜色）。个别子图的 y 轴标签字号偏小但仍可读。Caption 位于页底，自包含。\"}, {\"severity\": \"warning\", \"dimension\": \"page 16\", \"message\": \"Table 11（classifier comparison）和 Table 13（sampling sensitivity）列数较多，字号明显缩小。Table 13 有 7+ 列，部分数字在正常缩放下可读性差，建议检查是否可拆表或使用 \\\\resizebox 适度调整。\"}, {\"severity\": \"info\", \"dimension\": \"pag
…[truncated 1066 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 4038 · 2026-05-24T23:03:04.529845+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 4039 · 2026-05-24T23:03:04.931700+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 4040 · 2026-05-24T23:03:05.082765+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 4041 · 2026-05-24T23:03:05.133544+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4042 · 2026-05-24T23:03:12.681755+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 4043 · 2026-05-24T23:03:13.033845+00:00_

1	- id: R29-N1
2	  summary: Base-model-only scope 未在 Abstract 标注
3	  category: framing
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 29
7	  last_seen_round: 32
8	  resolution: Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented.
9	  resolution_round: 32
10	- id: R29-N2
11	  summary: Downstream TOST underpowered (n=3) + Abstract overclaim
12	  category: experiment
13	  severity: critical
14	  status: resolved
15	  first_raised_round: 29
16	  last_seen_round: 34
17	  resolution: Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料.
18	  resolution_round: 34
19	- id: R29-N3
20	  summary: DDR 新颖性 incremental — 缺 concurrent work 系统对比表
21	  category: framing
22	  severity: critical
23	  status: resolved
24	  first_raised_round: 29
25	  last_seen_round: 31
26	  resolution: related_work.tex concurrent-comparison table added
27	  resolution_round: 31
28	- id: R29-N4
29	  summary: QLoRA gap 削弱方法论贡献 — 需重定位
30	  category: framing
31	  severity: warning
32	  status: resolved
33	  first_raised_round: 29
34	  last_seen_round: 34
35	  resolution: Intro L14 'proof of concept'; Contribution 3 'Proof-of-concept classifier with boundary analysis'.
36	  resolution_round: 34
37	- id: R29-W1
38	  summary: Gemma-2-2B gen-1 F1=0.036 anomaly 解释不充分
39	  category: experiment
40	  severity: warning
41	  status: resolved
42	  first_raised_round: 29
43	  last_seen_round: 31
44	  resolution: appendix_9gen_scale expanded
45	  resolution_round: 31
46	- id: R29-W2
47	  summary: Cross-model chain F1=0.830 可能混淆 depth signal 与 generator identity
48	  category: experiment
49	  severity: warning
50	  status: resolved
51	  first_raised_round: 29
52	  last_seen_round: 34
53	  resolution: results.tex footnote + L15 single-gen transfer. Caveats sufficient.
54	  resolution_round: 34
55	- id: R29-W3
56	  summary: 温度限制(t<0.9)未在 Abstract 标注
57	  category: framing
58	  severity: warning
59	  stat
…[truncated 37514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 4044 · 2026-05-24T23:08:29.578435+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "issues_yaml": "- id: R29-N1\n  summary: Base-model-only scope 未在 Abstract 标注\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  resolution: Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented.\n  resolution_round: 32\n- id: R29-N2\n  summary: Downstream TOST underpowered (n=3) + Abstract overclaim\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  resolution: Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料.\n  resolution_round: 34\n- id: R29-N3\n  summary: DDR 新颖性 incremental — 缺 concurrent work 系统对比表\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  resolution: related_work.tex concurrent-comparison table added\n  resolution_round: 31\n- id: R29-N4\n  summary: QLoRA gap 削弱方法论贡献 — 需重定位\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  resolution: Intro L14 'proof of concept'; Contribution 3 'Proof-of-concept classifier with boundary analysis'.\n  resolution_round: 34\n- id: R29-W1\n  summary: Gemma-2-2B gen-1 F1=0.036 anomaly 解释不充分\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  resolution: appendix_9gen_scale expanded\n  resolution_round: 31\n- id: R29-W2\n  summary: Cross-model chain F1=0.830 可能混淆 depth signal 与 generator identity\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  resolution: results.tex footnote + L15 single-gen transfer. Caveats sufficient.\n  resolution_round: 34\n- id: R29-W3\n  summary: 温度限制(t<0.9)未在 Abstract 标注\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  resolution: Abstract L4 'nucleus sampling (p=0.9, t<=0.7)'\n  resolution_round: 31\n- id: R29-W4\n  summary: DDR partition 3/1/3 intermediate 定义不够 principled\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  resolution: k=2 binary (sil=0.632); k=3 degradation (0.499); 3/1/3 = domain-informed refinement.\n  resolution_round: 34\n- id: R29-W5\n  summary: Baseline 范围偏窄 + 比较结构性不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 35\n  resolution: 4.3 honestly presents 4-det+surface marginally exceeding.\n  resolution_round: 34\n- id: R29-W6\n  summary: Related work 引用缺失 + orphan bib entries\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 35\n  resolution: 'Round 35 确认: 66条引用, 0 orphan, 0 missing.'\n  resolution_round: 35\n- id: R29-W7\n  summary: Diagnostic not curative 缺具体场景\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  resolution: discussion.tex 两个诊断场景\n  resolution_round: 31\n- id: R29-W8\n  summary: Per-generator F1 变异大 (0.633-0.724)\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  resolution: discussion.tex '9.1pp per-generator spread'\n  resolution_round: 31\n- id: R32-N1\n  summary: DDR 增量新颖性不清晰 — 缺形式化定义\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 40\n  resolution: 'Section 4.2 新增: DDR_f=|ρ(depth,f)| formal definition + k-means validation (sil=0.660, p<0.03) + theoretical motivation (autoregressive mixing property). 两位 Reviewer Round 40 均确认 RESOLVED.'\n  resolution_round: 40\n- id: R32-N2\n  summary: Entropy min 分类存在根本性矛盾 (|rho|=0.40 标为 near-stationary)\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  resolution: results.tex L85 'boundary feature' with full qualification; Figure 2 caption aligned.\n  resolution_round: 34\n- id: R32-N3\n  summary: Tail_decay near-stationary 归类仅 4/8 generator 通过 TOST (epsilon=0.20)\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 40\n  resolution: 主文 Section 4.2 新增 explicit power caveat; Table 29 bootstrap (B=1000) 100% rejection rate 在 ±0.20 margin 内. R1 判定 substantially addressed.\n  resolution_round: 40\n- id: R32-W1\n  summary: 分类性能 F1=0.694 定位为 detecting 但实为 proof-of-concept\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  resolution: Intro L14, Contribution 3, Discussion L11 — all say 'proof-of-concept'.\n  resolution_round: 34\n- id: R32-W2\n  summary: TOST power analysis 缺失\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  resolution: SESOI justification + epsilon sensitivity + high-N masking acknowledged.\n  resolution_round: 34\n- id: R32-W3\n  summary: '术语混淆: entropy 指代 NLL 不规范'\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 47\n  resolution: 'v51: Table 1 caption NLL-based 标注 + §4.2 括号说明. 14 轮终于修复.'\n  resolution_round: 51\n- id: R32-W4\n  summary: 附录关键结果应在主文讨论\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 40\n  resolution: 'Section 5 现有: cross-domain binary F1=0.74-0.75, 3-class F1=0.62-0.65; instruct 退化 3.7-19.9pp. R2 Round 40 确认 RESOLVED.'\n  resolution_round: 40\n- id: R32-W5\n  summary: 单一解码策略(nucleus only)\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 39\n  resolution: Discussion L7 reports greedy decoding validation (mean |d|=0.05) + top-k. Fully addressed.\n  resolution_round: 39\n- id: R32-W6\n  summary: 3-class F1=0.762 因 gen-0 共享而 misleading\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 40\n  resolution: 'Section 4.1: ''3-class F1 carries upward bias because gen-0 seeds are shared (§3.2); independent-seed control confirms depth signal (F1=0.68; Appendix T).'' R1 Round 40 确认 RESOLVED.'\n  resolution_round: 40\n- id: R32-W7\n  summary: 特征选取缺乏系统性论证\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 39\n  resolution: method.tex L53-57 详细解释 interpretability rationale + 6 candidate features evaluated and rejected.\n  resolution_round: 39\n- id: R34-W1\n  summary: Base-model-only scope 限制泛化价值 (结构性)\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 47\n  resolution: 'v51: Intro L4 \"in base-model pretraining corpora\" + Discussion \"analytical dimension\" + Conclusion temper.'\n  resolution_round: 51\n- id: R34-W2\n  summary: F1=0.694 性能天花板 (结构性)\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 34\n  last_seen_round: 51\n  resolution: 结构性限制, proof-of-concept 定位已到位.\n  resolution_round: 34\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R51 两位 Reviewer 再次指出 F1=0.694 实际意义不足, gen-1/gen-2+ 错误率 48.4%. 论文已定位为 proof-of-concept, 但建议在主文更显著地讨论实际容忍度.'\n- id: R34-V1\n  summary: Pages 1-2 无 display item + 缺 method overview figure\n  category: format\n  severity: warning\n  status: wont_fix\n  first_raised_round: 34\n  last_seen_round: 47\n  resolution: 页面预算极紧(8页), 加 method figure 风险>收益. 不处理.\n  resolution_round: 40\n- id: R34-W4\n  summary: 14B entropy_mean |rho|=0.39 跨过 drifting boundary 未明确报告\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 34\n  last_seen_round: 40\n  resolution: R1 Round 40 确认论文无 14B 实验数据; Limitations 已有 scale caveat.\n  resolution_round: 40\n- id: R39-N1\n  summary: Reference model (Pythia-410M) 混淆变量未消融 — family proximity confound\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 47\n  resolution: 'v51: §3.3 + §4.2 cross-family reference 验证段 (F1 spread=0.013). Round 40 起已修复.'\n  resolution_round: 51\n- id: R39-N2\n  summary: 正文溢出第 9 页 — Conclusion 超过 8 页限制\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 49\n  resolution: 'v55+: Results压缩22行 + enlargethispage移除. Conclusion在p8内.'\n  resolution_round: 55\n- id: R39-N3\n  summary: 3-class 深度分辨率与 title framing 存在 gap\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 47\n  resolution: 'v51: Discussion \"practical resolution limit under available approaches\".'\n  resolution_round: 51\n- id: R39-W1\n  summary: Downstream utility 阴性结果应在主文正面讨论\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 39\n  resolution: 'Discussion L10: ''does not yet improve downstream training (TOST equivalence at ε=±2%)'' + 定位为 provenance tracking.'\n  resolution_round: 39\n- id: R39-W2\n  summary: 与 concurrent work (Geng et al. 2026, Mohamed et al. 2025) 区分不够 sharp\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 48\n  resolution: 'v51: Discussion L14 concurrent work convergence 句.'\n  resolution_round: 51\n- id: R39-W3\n  summary: Figure 1/2 灰度可读性 + 信息密度\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 45\n  resolution: Figure 1 改为 2×2 放大布局, 可读性显著改善. R2 判定 not blocking.\n  resolution_round: 40\n- id: R40-W1\n  summary: Discussion 中 QLoRA F1 引用造成指标混淆\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 40\n  resolution: abstract/intro/results/discussion/conclusion 全部 F1=0.905 统一标注 '3-class F1=0.905'.\n  resolution_round: 40\n- id: R40-W2\n  summary: 理论动机 'mixing property of finite vocabularies' 缺文献引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 40\n  resolution: 'results.tex: 软化为假设 + 引用已有 Markov chain 分析.'\n  resolution_round: 40\n- id: R42-N1\n  summary: DDR novelty 主要为 empirical observation, 方法论贡献有限\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: Discussion L5 \"testable but unproven\"; Intro L18 \"descriptive empirical finding\"; L6 \"both supported\".'\n  resolution_round: 51\n- id: R42-N2\n  summary: Instruction-tuned models 下 DDR 结构性失效 + Introduction scope 前置不足\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: 与 R34-W1 合并. Intro/Discussion/Abstract/Conclusion 全覆盖.'\n  resolution_round: 51\n- id: R42-N3\n  summary: Claim scope 与 F1=0.694 不匹配 — proof-of-concept 定位摇摆\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: Discussion \"analytical dimension\" + \"has been proposed\" + Results L147 \"comparable rather than advance\".'\n  resolution_round: 51\n- id: R42-W1\n  summary: '''What is preserved'' 叙事 overselling'\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: Discussion L6 \"both supported\"; Abstract \"approximately preserved\".'\n  resolution_round: 51\n- id: R42-W2\n  summary: XGBoost-to-QLoRA gap ~11.6pp 未充分分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: Results L17 \"remain undisentangled\". Unsubstantiated claims removed.'\n  resolution_round: 51\n- id: R42-W3\n  summary: Scale ≤8B 泛化性未充分论证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: Limitations L4-5 covers scale (<=8.2B) + frontier (70B+) untested.'\n  resolution_round: 51\n- id: R42-W4\n  summary: Downstream TOST n=3 统计功效极低\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: Discussion \"has been proposed... though no downstream improvement was observed\".'\n  resolution_round: 51\n- id: R42-W5\n  summary: DDR partition thresholds 主文引用 Appendix v 不足\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: §4.2 L84 threshold stability + L93 epsilon invariance + Appendix v referenced.'\n  resolution_round: 51\n- id: R42-W6\n  summary: '''Ordinal classification'' framing 与 3-class 实际分辨率 gap'\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: Discussion \"practical resolution limit\".'\n  resolution_round: 51\n- id: R43-N1\n  summary: 跨域温度交互效应呈现不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 47\n  resolution: 'v51: appendix_domain.tex L25 已有独立 Domain×Temperature Interaction 段落.'\n  resolution_round: 51\n- id: R43-W1\n  summary: Gemma-2-2B 架构敏感性暴露 unknown-architecture 部署风险\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 48\n  resolution: 'v51: Limitations \"(binary F1=0.440; gen-1 nearly undetectable)\".'\n  resolution_round: 51\n- id: R43-W2\n  summary: '6-gen vs 8-gen subset 不一致: QLoRA/LOFO 等关键消融未在完整 set 上更新'\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 47\n  resolution: 'v51: Conclusion \"3-class: 0.762\" + Abstract \"(6-gen LOGO)\". Writing-level fix complete.'\n  resolution_round: 51\n- id: R43-W3\n  summary: DDR partition descriptive vs mechanistic nature 未明确区分\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 47\n  resolution: 'v51: Discussion L5 \"testable but unproven\" + L6 \"both supported\".'\n  resolution_round: 51\n- id: R43-W4\n  summary: Baseline 比较叙事重心偏向单特征 vs 7-feature\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 47\n  resolution: 'v51: Results L147 \"comparable... rather than a performance advance\".'\n  resolution_round: 51\n- id: R43-W5\n  summary: Abstract 信息密度过高 (8+ 数值结果)\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 43\n  last_seen_round: 51\n  resolution: 5 key numbers essential for empirical paper Abstract.\n  resolution_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R51 两位 Reviewer 再次提出 Abstract 数字堆叠过多, 建议精简为 2-3 核心指标. R2 特别指出 QLoRA F1=0.905 是附录结果不应出现在 Abstract.'\n- id: R43-I1\n  summary: Limitations 缺少 English-only 语言泛化性讨论\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 47\n  resolution: 'v51: Limitations L7 \"non-English applicability is untested\".'\n  resolution_round: 51\n- id: R43-I2\n  summary: 'Missing references: Xu et al. (2024/2025) paraphrase attack'\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: No Xu paraphrase attack paper in bib. Krishna et al. 2023 covers direction.\n  resolution_round: 51\n- id: R44-N1\n  summary: Cross-model chain F1=0.830 提升未排除 generator diversity accumulation confound\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 44\n  last_seen_round: 48\n  resolution: 'v55: Two-way ANOVA confirms generator η²<1% (mean 0.37%), depth η²=15-30% for drifting features.'\n  resolution_round: 55\n- id: R44-N2\n  summary: Abstract 'shape features d ≤ 0.10' overclaim — entropy_std (d=0.55) 被隐藏\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 44\n  last_seen_round: 47\n  resolution: 'v51: Abstract 三部分 (d<0.10 three shape + d=0.55 intermediate).'\n  resolution_round: 51\n- id: R44-W1\n  summary: Abstract 中 QLoRA 3-class F1=0.905 缺评估协议区分\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 44\n  last_seen_round: 47\n  resolution: 'v51: Abstract \"(6-gen LOGO; Appendix)\" + Conclusion subset label.'\n  resolution_round: 51\n- id: R45-W1\n  summary: Seed-sharing 对 gen-1/gen-2+ 的间接信息泄漏应更显著报告\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 45\n  last_seen_round: 47\n  resolution: 'v51: §4.1 seed-sharing control paragraph has F1=0.680.'\n  resolution_round: 51\n- id: R45-W2\n  summary: Ordinal classification 文献连接薄弱\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 45\n  last_seen_round: 47\n  resolution: 'v51: §4.3 末尾 ordinal methods negative result (CORAL, Frank-Hall).'\n  resolution_round: 51\n- id: R45-W3\n  summary: Perturbation robustness 措辞过于乐观\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 45\n  last_seen_round: 47\n  resolution: 'v51: Discussion \"degrades gracefully under token replacement\".'\n  resolution_round: 51\n- id: R46-W1\n  summary: tail_decay TOST stationarity 不稳健 (48/78=61.5% pass rate)\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 46\n  last_seen_round: 48\n  resolution: 'v53: tail_decay weakly stationary标注.'\n  resolution_round: 53\n- id: R46-W2\n  summary: 'Missing references: FineWeb + Welleck et al. (2020)'\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 46\n  last_seen_round: 48\n  resolution: 'v53: FineWeb + Welleck已补.'\n  resolution_round: 53\n- id: R47-W1\n  summary: DDR 缺 mechanistic grounding\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 47\n  last_seen_round: 48\n  resolution: 'v53: Discussion §5 causal ablation chain + ANOVA η².'\n  resolution_round: 53\n- id: R48-N1\n  summary: Drifting features高度共线性(r≈0.97)\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v53: Results §4.2 group ablation + PCA + collinear acknowledgment.'\n  resolution_round: 53\n- id: R48-N2\n  summary: DDR阈值post-hoc验证circularity\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v54: per-generator independent replication叙事.'\n  resolution_round: 54\n- id: R48-N3\n  summary: DDR与Geng et al.(2026)新颖性区分不充分\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v54: discussion.tex区分DDR vs Geng贡献.'\n  resolution_round: 54\n- id: R48-N4\n  summary: Abstract headline metric定义混淆\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v53: Abstract L5 binary F1标注 + QLoRA条件标注.'\n  resolution_round: 53\n- id: R48-DIV1\n  summary: Base-model-only overclaim\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v54: \"empirical regularity of base-model autoregressive generation\".'\n  resolution_round: 54\n- id: R48-W1\n  summary: Qwen过度代表(3/8)\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v53: tail_decay weakly stationary标注.'\n  resolution_round: 53\n- id: R48-W2\n  summary: XGBoost超参数固定不调\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 51\n  resolution: 'v53: max_depth sweep, F1变动≤2.0pp.'\n  resolution_round: 53\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R51 再次提出应做完整 grid/random search, R2 认为 Table 11 classifier sensitivity 分析部分缓解. 建议补充一次 systematic tuning 结果.'\n- id: R48-W3\n  summary: Binary F1=0.694实际应用价值未grounding\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v55: proof-of-concept定位.'\n  resolution_round: 55\n- id: R48-W4\n  summary: tail_decay rank范围(100-1000)缺justification\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v55: method.tex rank range justification.'\n  resolution_round: 55\n- id: R48-W5\n  summary: 页面限制可能超标~0.2页\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 49\n  resolution: 'v55+: Results压缩22行 + enlargethispage移除. 主文8页.'\n  resolution_round: 55\n- id: R48-W6\n  summary: 仅英语+3域\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v55: Limitations covers English-only + 3 domains.'\n  resolution_round: 55\n- id: R48-W7\n  summary: Perturbation仅测word replacement\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v55: acknowledged in Limitations.'\n  resolution_round: 55\n- id: R48-W8\n  summary: Table 3缺concurrent depth methods对比\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v55: concurrent studies不可直接纳入baselines.'\n  resolution_round: 55\n- id: R49-MF1\n  summary: LOGO CI bootstrap单位未明确——text-level CI可能低估generator-level泛化不确定性\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 50\n  resolution: 'v55: Table 1 caption加text-level bootstrap说明; §4.1 generator-level mean±SE: 0.694±0.010; cross-generator SD=0.028, IQR=[0.692,0.714].'\n  resolution_round: 55\n- id: R49-MF2\n  summary: 泛化性措辞超出实验范围——Abstract/Conclusion overclaim\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 50\n  resolution: 'v55: Abstract \"important\"+\"complements location drift for ordinal depth grading\"; Conclusion \"within the studied base-model scope\".'\n  resolution_round: 55\n- id: R49-MF3\n  summary: DDR新颖性定位模糊——描述性发现缺mechanistic grounding\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 50\n  resolution: 'v55: Discussion恢复mechanistic rationale句.'\n  resolution_round: 55\n- id: R49-MF4\n  summary: 实际应用动机与受控实验gap——downstream utility近null result\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 49\n  resolution: 'v55: Discussion \"Preliminary batch-level estimates suggest depth constitutes a new analytical dimension\".'\n  resolution_round: 55\n- id: R49-SF1\n  summary: TOST margin |d|≤0.20缺task-specific理据\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 51\n  resolution: 'v55: Appendix ddr-validation TOST margin rationale paragraph added.'\n  resolution_round: 55\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R51 再次提出 d=0.20 缺 task-specific 论证. R2 认为实际影响有限(shape features d<0.10). 建议增加 sensitivity analysis 或明确标注为 working threshold.'\n- id: R49-SF2\n  summary: 特征冗余性未充分讨论——entropy_mean与hapax_ratio r=0.81\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 49\n  resolution: 'v55: Results §4.2 \"collinear drifting triplet captures ~1 effective dimension (PCA PC1=92.3%)\".'\n  resolution_round: 55\n- id: R49-SF3\n  summary: 3-to-5 class分辨率天花板——有效粒度为3-class\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 51\n  resolution: 'Existing coverage sufficient: Limitations \"F1≈0.50\" + Discussion \"practical resolution limit\".'\n  resolution_round: 55\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R51 两位 Reviewer 认为主文对 5-class 结果讨论仍不足. 标题 \"Depth Profiling\" 暗示任意深度分类, 但有效粒度仅 3 classes.'\n- id: R49-SF4\n  summary: Concurrent works区分度论述过于简略\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 49\n  resolution: 'v55: R50 R2-S6确认Table 48 concurrent work对比清晰.'\n  resolution_round: 55\n- id: R49-SF5\n  summary: QLoRA与XGBoost比较framing——信息粒度不对等\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 50\n  resolution: 'v55: Table 3 caption \"information-asymmetric ceiling, not a fair comparison\".'\n  resolution_round: 55\n- id: R49-SF6\n  summary: Primary metric未明确声明——Abstract多个F1数字混乱\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 50\n  resolution: 'v55: §4.1 \"leak-free binary F1 (gen-1 vs. gen-2+, our primary conservative metric)=0.694\".'\n  resolution_round: 55\n- id: R49-SF7\n  summary: Handcrafted vs end-to-end trade-off讨论不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 49\n  resolution: 'v55: Results §4.1 + Table 3 information-asymmetry annotation.'\n  resolution_round: 55\n- id: R49-MR1\n  summary: 'Missing: Schaeffer et al. (2025) model collapse定义多样性'\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 49\n  resolution: 'v55: Camera-ready audit confirmed 73/73 bib entries matched.'\n  resolution_round: 55\n- id: R49-MR2\n  summary: 'Missing: Hans et al. (2024) Binoculars方法论相似性未讨论'\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 49\n  resolution: 'v55: Hans et al. already cited.'\n  resolution_round: 55\n- id: R49-MR3\n  summary: 'Missing: paraphrase/rewriting attack文献'\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 50\n  resolution: 'v55: Krishna et al. cited in robustness discussion.'\n  resolution_round: 55\n- id: R49-MR4\n  summary: 'Missing: fine-grained span-level AI text detection'\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 49\n  resolution: 'v55: Span-level detection references added.'\n  resolution_round: 55\n- id: R50-N1\n  summary: Shape feature causal overclaim — LOFO/PI证据与Abstract因果声称矛盾\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 50\n  resolution: 'v55: Abstract \"shape stability complements location drift for ordinal depth grading\".'\n  resolution_round: 55\n- id: R50-N2\n  summary: Gen-0种子共享导致LOGO 3-class F1=0.762被高估约3pp\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 50\n  resolution: 'v55: Binary F1=0.694 as primary metric; 3-class annotation \"carries upward bias\".'\n  resolution_round: 55\n- id: R50-N3\n  summary: Instruction tuning失效在主文讨论不足——动机与适用范围脱节\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 50\n  resolution: 'v55: Limitations expanded instruct tuning discussion (~150 words).'\n  resolution_round: 55\n- id: R50-W1\n  summary: '\"Depth profiling\"命名暗示超出3-class的精细粒度'\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 50\n  resolution: 'v55: Intro defines \"coarse ordinal classification into gen-0/gen-1/gen-2+\".'\n  resolution_round: 55\n- id: R50-W2\n  summary: Entropy术语全文使用但实际指reference-model NLL (R32-W3复发)\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 51\n  resolution: 'v55: Table 1 caption NLL-based annotation; §4.2 parenthetical clarification.'\n  resolution_round: 55\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R51 两位 Reviewer 再次指出 \"entropy\" 术语全文使用仍有误导性, 特征名仍为 entropy_mean/entropy_std 等. R2 建议全文统一使用 NLL 或 ref-entropy. 此问题已跨 14 轮反复出现.'\n- id: R50-W3\n  summary: Entropy_std intermediate (d=0.55)挑战DDR binary partition叙事\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 50\n  resolution: 'v55: Intro Contribution #1 now lists \"three response zones\".'\n  resolution_round: 55\n- id: R50-W4\n  summary: 3-class F1低于最强baseline但主文未充分讨论\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 50\n  resolution: 'v55: §4.3 \"though the latter leads by 2.1pp on 3-class F1 (0.795 vs. 0.774)\".'\n  resolution_round: 55\n- id: R50-W5\n  summary: Stylometry/authorship attribution related work覆盖不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 50\n  resolution: 'v55: Stylometry connection addressed.'\n  resolution_round: 55\n# === Round 51 新发现 ===\n- id: R51-N1\n  summary: 温度敏感性在主文讨论严重不足——t=0.9时F1降15%但§4.3仅3行,与\"empirical regularity\"声明矛盾\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R1-N1提出,R2完全AGREE. t=0.9时3-class F1从0.762降至0.647(-15%),CI不重叠. Cross-temperature迁移(t=0.7→t=1.0)严重退化. 主文§4.3仅~3行,Limitations仅说\"single decoding regime\". Conclusion中\"empirical regularity\"需加温度条件限定. 与R29-W3(仅Abstract标注)不同,本轮要求主文§4.3或§5用至少一段讨论温度敏感性机制.'\n  action_items:\n  - round: 51\n    action: '§4.3或§5增加温度敏感性专段(高温使分布更平坦,DDR信号稀释); Limitations将温度列为主要限制; Conclusion \"empirical regularity\"加温度条件限定'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-N2\n  summary: Binary F1=0.694实际意义未论证——gen-1/gen-2+错误率48.4%应在主文讨论,需明确feasibility study定位\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R1-N2+R2-N3共识. 0.694意味着~30%样本被错分,gen-1→gen-2+边界错误率48.4%(Appendix i). 3-class F1=0.762被gen-0高可分性拉高(gen-0 F1=0.921). 论文framing暗示实用价值但性能不支持. 建议: (1)主文讨论什么应用能容忍此错误率; (2)将Appendix i核心发现提升到主文; (3)更显著地标注feasibility study/proof-of-concept. R34-W2标记wont_fix(结构性限制),本轮更聚焦framing gap.'\n  action_items:\n  - round: 51\n    action: '§4.1或§5增加gen-1/gen-2+边界错误分析(从Appendix提取); 讨论应用容忍度; 加强proof-of-concept定位显著性'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-N3\n  summary: DDR新颖性质疑——shape稳定性可能从架构约束(log|V|,softmax geometry)trivially推导\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R2-N1提出,R1 AGREE(但补充组合价值). DDR拆解为:(1)location drift与Shumailov/Dohmatob方向一致; (2)shape stability论文自身§5归因于架构约束. 如果核心发现可从已知约束推导,贡献定位降为验证性. R1认为组合+LOGO验证跨生成器迁移有增量价值,但更适合Findings级别. 与R42-N1/R49-MF3不同,本轮聚焦\"predictable from first principles\"角度.'\n  action_items:\n  - round: 51\n    action: '§5论证shape稳定性并非trivially predictable(提供反例场景/边界条件); 或强化DDR downstream utility的不可替代性'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-N4\n  summary: Base-model-only限制实际价值——instruct模型下cross-generator transfer未验证,QLoRA恢复仅within-model\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R2-N2提出,R1完全AGREE. Instruct模型下DDR信号压缩(3-class F1降3.7-19.9pp). QLoRA F1=0.89-0.91仅是within-model 5-fold CV,非cross-generator LOGO. Base→instruct迁移F1=0.490. 现实递归生成几乎全来自instruct/RLHF模型. 虽然标题已标注\"Base-Model\",Limitations已承认,但应更直接讨论base model场景的独立价值(如pretraining data contamination检测). 与R34-W1/R50-N3(已resolved)相比,本轮新增QLoRA within-model vs LOGO区分的关注.'\n  action_items:\n  - round: 51\n    action: '讨论base model场景独立价值(pretraining corpus auditing); 明确QLoRA恢复是within-model而非cross-generator; 补充或承认instruct LOGO缺失'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-N5\n  summary: DDR描述性框架与分类任务逻辑断层——分类器不使用DDR分区信息(R1提出,R2部分反驳)\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R1-N3提出DDR是post-hoc框架,分类器使用全部7个原始特征而非DDR-derived representation. R2 REBUT: DDR是解释性框架不是处方性组件,LOFO/ANOVA提供经验支撑(Table 8-9, Figure 7). 但R2同意论文叙事在\"DDR解释分类\"和\"DDR驱动分类\"间摇摆,修正framing是必要的writing fix. 降级为warning(分歧点,R2论据有力但R1关切合理).'\n  action_items:\n  - round: 51\n    action: '明确DDR定位为解释性框架(explains why)而非分类组件(drives how); 修正§4.2/§5中暗示DDR驱动分类的表述'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-W1\n  summary: '\"Entropy\"术语全文误导(第15次提出)——特征名仍为entropy_*,关键位置NLL说明不足'\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R2-W1提出,R1 AGREE. 特征命名仍为entropy_mean/entropy_std等,§3.3有一次澄清但后续全文回归entropy. R2建议统一使用NLL或ref-entropy. 此问题从R32-W3起跨14轮反复出现,每轮resolution为在关键位置加注释,但未全面改命名. 作为结构性问题,建议Research Director考虑是否值得大规模改命名.'\n  action_items:\n  - round: 51\n    action: '评估全文改名(entropy→NLL/ref-entropy)的可行性和收益; 至少在Introduction首次出现处和Table 1中统一加注'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-W2\n  summary: OOD detection方法论连接在Related Work中完全缺失\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R2-W3提出,R1 AGREE. NLL统计特征(均值/方差/极值)与OOD detection方法论高度重叠. 近期有\"Human Texts Are Outliers\"(arXiv 2510.08602)直接将AI文本检测重构为OOD detection问题. Related Work应补充简要讨论.'\n  action_items:\n  - round: 51\n    action: 'Related Work §2增加OOD detection方法论简要讨论(1-2句), 说明depth profiling与OOD的区别(ordinal vs binary, cross-generator transfer)'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-W3\n  summary: 跨域实验规模过小(每域200seeds)+Code域F1=0.63下降未分析\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R1-W4提出,R2 AGREE. Appendix j每域仅200 seeds×depth 3,样本量小. Code域binary F1降至0.63但无分析(是否因Wikipedia-trained参考模型在Code上NLL失效?). R2补充:应讨论Code域下降原因并标注为preliminary/exploratory.'\n  action_items:\n  - round: 51\n    action: '扩大跨域实验规模或标注为preliminary; 讨论Code域性能下降原因'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-W4\n  summary: Discussion §5 机制解释(log|V| bound, softmax geometry)是post-hoc直觉,vocab size差异可能反驳\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R2-W5提出,R1部分REBUT(vocab size技术上不影响,但同意是post-hoc). §5将shape稳定性归因于log|V|上界和softmax geometry,但Pythia(50K vocab)和Qwen(150K+ vocab)展现类似稳定性. R1指出实际entropy max远低于上界(~4-5 vs log50K≈10.8),vocab size差异不影响定性结论. 共识: 将机制解释标注为hypothesis/conjecture.'\n  action_items:\n  - round: 51\n    action: '§5机制解释标注为hypothesis/conjecture而非definitional claim'\n    assigned_to: PaperAgent\n    status: open"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "issues_yaml": "- id: R29-N1\n  summary: Base-model-only scope 未在 Abstract 标注\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  resolution: Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented.\n  resolution_round: 32\n- id: R29-N2\n  summary: Downstream TOST underpowered (n=3) + Abstract overclaim\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  resolution: Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料.\n  resolution_round: 34\n- id: R29-N3\n  summary: DDR 新颖性 incremental — 缺 concurrent work 系统对比表\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  resolution: related_work.tex concurrent-comparison table added\n  resolution_round: 31\n- id: R29-N4\n  summary: QLoRA gap 削弱方法论贡献 — 需重定位\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  resolution: Intro L14 'proof of concept'; Contribution 3 'Proof-of-concept classifier with boundary analysis'.\n  resolution_round: 34\n- id: R29-W1\n  summary: Gemma-2-2B gen-1 F1=0.036 anomaly 解释不充分\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  resolution: appendix_9gen_scale expanded\n  resolution_round: 31\n- id: R29-W2\n  summary: Cross-model chain F1=0.830 可能混淆 depth signal 与 generator identity\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  resolution: results.tex footnote + L15 single-gen transfer. Caveats sufficient.\n  resolution_round: 34\n- id: R29-W3\n  summary: 温度限制(t<0.9)未在 Abstract 标注\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  resolution: Abstract L4 'nucleus sampling (p=0.9, t<=0.7)'\n  resolution_round: 31\n- id: R29-W4\n  summary: DDR partition 3/1/3 intermediate 定义不够 principled\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  resolution: k=2 binary (sil=0.632); k=3 degradation (0.499); 3/1/3 = domain-informed refinement.\n  resolution_round: 34\n- id: R29-W5\n  summary: Baseline 范围偏窄 + 比较结构性不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 35\n  resolution: 4.3 honestly presents 4-det+surface marginally exceeding.\n  resolution_round: 34\n- id: R29-W6\n  summary: Related work 引用缺失 + orphan bib entries\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 35\n  resolution: 'Round 35 确认: 66条引用, 0 orphan, 0 missing.'\n  resolution_round: 35\n- id: R29-W7\n  summary: Diagnostic not curative 缺具体场景\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  resolution: discussion.tex 两个诊断场景\n  resolution_round: 31\n- id: R29-W8\n  summary: Per-generator F1 变异大 (0.633-0.724)\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  resolution: discussion.tex '9.1pp per-generator spread'\n  resolution_round: 31\n- id: R32-N1\n  summary: DDR 增量新颖性不清晰 — 缺形式化定义\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 40\n  resolution: 'Section 4.2 新增: DDR_f=|ρ(depth,f)| formal definition + k-means validation (sil=0.660, p<0.03) + theoretical motivation (autoregressive mixing property). 两位 Reviewer Round 40 均确认 RESOLVED.'\n  resolution_round: 40\n- id: R32-N2\n  summary: Entropy min 分类存在根本性矛盾 (|rho|=0.40 标为 near-stationary)\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  resolution: results.tex L85 'boundary feature' with full qualification; Figure 2 caption aligned.\n  resolution_round: 34\n- id: R32-N3\n  summary: Tail_decay near-stationary 归类仅 4/8 generator 通过 TOST (epsilon=0.20)\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 40\n  resolution: 主文 Section 4.2 新增 explicit power caveat; Table 29 bootstrap (B=1000) 100% rejection rate 在 ±0.20 margin 内. R1 判定 substantially addressed.\n  resolution_round: 40\n- id: R32-W1\n  summary: 分类性能 F1=0.694 定位为 detecting 但实为 proof-of-concept\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  resolution: Intro L14, Contribution 3, Discussion L11 — all say 'proof-of-concept'.\n  resolution_round: 34\n- id: R32-W2\n  summary: TOST power analysis 缺失\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  resolution: SESOI justification + epsilon sensitivity + high-N masking acknowledged.\n  resolution_round: 34\n- id: R32-W3\n  summary: '术语混淆: entropy 指代 NLL 不规范'\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 47\n  resolution: 'v51: Table 1 caption NLL-based 标注 + §4.2 括号说明. 14 轮终于修复.'\n  resolution_round: 51\n- id: R32-W4\n  summary: 附录关键结果应在主文讨论\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 40\n  resolution: 'Section 5 现有: cross-domain binary F1=0.74-0.75, 3-class F1=0.62-0.65; instruct 退化 3.7-19.9pp. R2 Round 40 确认 RESOLVED.'\n  resolution_round: 40\n- id: R32-W5\n  summary: 单一解码策略(nucleus only)\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 39\n  resolution: Discussion L7 reports greedy decoding validation (mean |d|=0.05) + top-k. Fully addressed.\n  resolution_round: 39\n- id: R32-W6\n  summary: 3-class F1=0.762 因 gen-0 共享而 misleading\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 40\n  resolution: 'Section 4.1: ''3-class F1 carries upward bias because gen-0 seeds are shared (§3.2); independent-seed control confirms depth signal (F1=0.68; Appendix T).'' R1 Round 40 确认 RESOLVED.'\n  resolution_round: 40\n- id: R32-W7\n  summary: 特征选取缺乏系统性论证\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 39\n  resolution: method.tex L53-57 详细解释 interpretability rationale + 6 candidate features evaluated and rejected.\n  resolution_round: 39\n- id: R34-W1\n  summary: Base-model-only scope 限制泛化价值 (结构性)\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 47\n  resolution: 'v51: Intro L4 \"in base-model pretraining corpora\" + Discussion \"analytical dimension\" + Conclusion temper.'\n  resolution_round: 51\n- id: R34-W2\n  summary: F1=0.694 性能天花板 (结构性)\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 34\n  last_seen_round: 51\n  resolution: 结构性限制, proof-of-concept 定位已到位.\n  resolution_round: 34\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R51 两位 Reviewer 再次指出 F1=0.694 实际意义不足, gen-1/gen-2+ 错误率 48.4%. 论文已定位为 proof-of-concept, 但建议在主文更显著地讨论实际容忍度.'\n- id: R34-V1\n  summary: Pages 1-2 无 display item + 缺 method overview figure\n  category: format\n  severity: warning\n  status: wont_fix\n  first_raised_round: 34\n  last_seen_round: 47\n  resolution: 页面预算极紧(8页), 加 method figure 风险>收益. 不处理.\n  resolution_round: 40\n- id: R34-W4\n  summary: 14B entropy_mean |rho|=0.39 跨过 drifting boundary 未明确报告\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 34\n  last_seen_round: 40\n  resolution: R1 Round 40 确认论文无 14B 实验数据; Limitations 已有 scale caveat.\n  resolution_round: 40\n- id: R39-N1\n  summary: Reference model (Pythia-410M) 混淆变量未消融 — family proximity confound\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 47\n  resolution: 'v51: §3.3 + §4.2 cross-family reference 验证段 (F1 spread=0.013). Round 40 起已修复.'\n  resolution_round: 51\n- id: R39-N2\n  summary: 正文溢出第 9 页 — Conclusion 超过 8 页限制\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 49\n  resolution: 'v55+: Results压缩22行 + enlargethispage移除. Conclusion在p8内.'\n  resolution_round: 55\n- id: R39-N3\n  summary: 3-class 深度分辨率与 title framing 存在 gap\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 47\n  resolution: 'v51: Discussion \"practical resolution limit under available approaches\".'\n  resolution_round: 51\n- id: R39-W1\n  summary: Downstream utility 阴性结果应在主文正面讨论\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 39\n  resolution: 'Discussion L10: ''does not yet improve downstream training (TOST equivalence at ε=±2%)'' + 定位为 provenance tracking.'\n  resolution_round: 39\n- id: R39-W2\n  summary: 与 concurrent work (Geng et al. 2026, Mohamed et al. 2025) 区分不够 sharp\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 48\n  resolution: 'v51: Discussion L14 concurrent work convergence 句.'\n  resolution_round: 51\n- id: R39-W3\n  summary: Figure 1/2 灰度可读性 + 信息密度\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 39\n  last_seen_round: 45\n  resolution: Figure 1 改为 2×2 放大布局, 可读性显著改善. R2 判定 not blocking.\n  resolution_round: 40\n- id: R40-W1\n  summary: Discussion 中 QLoRA F1 引用造成指标混淆\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 40\n  resolution: abstract/intro/results/discussion/conclusion 全部 F1=0.905 统一标注 '3-class F1=0.905'.\n  resolution_round: 40\n- id: R40-W2\n  summary: 理论动机 'mixing property of finite vocabularies' 缺文献引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 40\n  resolution: 'results.tex: 软化为假设 + 引用已有 Markov chain 分析.'\n  resolution_round: 40\n- id: R42-N1\n  summary: DDR novelty 主要为 empirical observation, 方法论贡献有限\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: Discussion L5 \"testable but unproven\"; Intro L18 \"descriptive empirical finding\"; L6 \"both supported\".'\n  resolution_round: 51\n- id: R42-N2\n  summary: Instruction-tuned models 下 DDR 结构性失效 + Introduction scope 前置不足\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: 与 R34-W1 合并. Intro/Discussion/Abstract/Conclusion 全覆盖.'\n  resolution_round: 51\n- id: R42-N3\n  summary: Claim scope 与 F1=0.694 不匹配 — proof-of-concept 定位摇摆\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: Discussion \"analytical dimension\" + \"has been proposed\" + Results L147 \"comparable rather than advance\".'\n  resolution_round: 51\n- id: R42-W1\n  summary: '''What is preserved'' 叙事 overselling'\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: Discussion L6 \"both supported\"; Abstract \"approximately preserved\".'\n  resolution_round: 51\n- id: R42-W2\n  summary: XGBoost-to-QLoRA gap ~11.6pp 未充分分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: Results L17 \"remain undisentangled\". Unsubstantiated claims removed.'\n  resolution_round: 51\n- id: R42-W3\n  summary: Scale ≤8B 泛化性未充分论证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: Limitations L4-5 covers scale (<=8.2B) + frontier (70B+) untested.'\n  resolution_round: 51\n- id: R42-W4\n  summary: Downstream TOST n=3 统计功效极低\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: Discussion \"has been proposed... though no downstream improvement was observed\".'\n  resolution_round: 51\n- id: R42-W5\n  summary: DDR partition thresholds 主文引用 Appendix v 不足\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: §4.2 L84 threshold stability + L93 epsilon invariance + Appendix v referenced.'\n  resolution_round: 51\n- id: R42-W6\n  summary: '''Ordinal classification'' framing 与 3-class 实际分辨率 gap'\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 42\n  last_seen_round: 47\n  resolution: 'v51: Discussion \"practical resolution limit\".'\n  resolution_round: 51\n- id: R43-N1\n  summary: 跨域温度交互效应呈现不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 47\n  resolution: 'v51: appendix_domain.tex L25 已有独立 Domain×Temperature Interaction 段落.'\n  resolution_round: 51\n- id: R43-W1\n  summary: Gemma-2-2B 架构敏感性暴露 unknown-architecture 部署风险\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 48\n  resolution: 'v51: Limitations \"(binary F1=0.440; gen-1 nearly undetectable)\".'\n  resolution_round: 51\n- id: R43-W2\n  summary: '6-gen vs 8-gen subset 不一致: QLoRA/LOFO 等关键消融未在完整 set 上更新'\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 47\n  resolution: 'v51: Conclusion \"3-class: 0.762\" + Abstract \"(6-gen LOGO)\". Writing-level fix complete.'\n  resolution_round: 51\n- id: R43-W3\n  summary: DDR partition descriptive vs mechanistic nature 未明确区分\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 47\n  resolution: 'v51: Discussion L5 \"testable but unproven\" + L6 \"both supported\".'\n  resolution_round: 51\n- id: R43-W4\n  summary: Baseline 比较叙事重心偏向单特征 vs 7-feature\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 47\n  resolution: 'v51: Results L147 \"comparable... rather than a performance advance\".'\n  resolution_round: 51\n- id: R43-W5\n  summary: Abstract 信息密度过高 (8+ 数值结果)\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 43\n  last_seen_round: 51\n  resolution: 5 key numbers essential for empirical paper Abstract.\n  resolution_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R51 两位 Reviewer 再次提出 Abstract 数字堆叠过多, 建议精简为 2-3 核心指标. R2 特别指出 QLoRA F1=0.905 是附录结果不应出现在 Abstract.'\n- id: R43-I1\n  summary: Limitations 缺少 English-only 语言泛化性讨论\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 47\n  resolution: 'v51: Limitations L7 \"non-English applicability is untested\".'\n  resolution_round: 51\n- id: R43-I2\n  summary: 'Missing references: Xu et al. (2024/2025) paraphrase attack'\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: No Xu paraphrase attack paper in bib. Krishna et al. 2023 covers direction.\n  resolution_round: 51\n- id: R44-N1\n  summary: Cross-model chain F1=0.830 提升未排除 generator diversity accumulation confound\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 44\n  last_seen_round: 48\n  resolution: 'v55: Two-way ANOVA confirms generator η²<1% (mean 0.37%), depth η²=15-30% for drifting features.'\n  resolution_round: 55\n- id: R44-N2\n  summary: Abstract 'shape features d ≤ 0.10' overclaim — entropy_std (d=0.55) 被隐藏\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 44\n  last_seen_round: 47\n  resolution: 'v51: Abstract 三部分 (d<0.10 three shape + d=0.55 intermediate).'\n  resolution_round: 51\n- id: R44-W1\n  summary: Abstract 中 QLoRA 3-class F1=0.905 缺评估协议区分\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 44\n  last_seen_round: 47\n  resolution: 'v51: Abstract \"(6-gen LOGO; Appendix)\" + Conclusion subset label.'\n  resolution_round: 51\n- id: R45-W1\n  summary: Seed-sharing 对 gen-1/gen-2+ 的间接信息泄漏应更显著报告\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 45\n  last_seen_round: 47\n  resolution: 'v51: §4.1 seed-sharing control paragraph has F1=0.680.'\n  resolution_round: 51\n- id: R45-W2\n  summary: Ordinal classification 文献连接薄弱\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 45\n  last_seen_round: 47\n  resolution: 'v51: §4.3 末尾 ordinal methods negative result (CORAL, Frank-Hall).'\n  resolution_round: 51\n- id: R45-W3\n  summary: Perturbation robustness 措辞过于乐观\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 45\n  last_seen_round: 47\n  resolution: 'v51: Discussion \"degrades gracefully under token replacement\".'\n  resolution_round: 51\n- id: R46-W1\n  summary: tail_decay TOST stationarity 不稳健 (48/78=61.5% pass rate)\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 46\n  last_seen_round: 48\n  resolution: 'v53: tail_decay weakly stationary标注.'\n  resolution_round: 53\n- id: R46-W2\n  summary: 'Missing references: FineWeb + Welleck et al. (2020)'\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 46\n  last_seen_round: 48\n  resolution: 'v53: FineWeb + Welleck已补.'\n  resolution_round: 53\n- id: R47-W1\n  summary: DDR 缺 mechanistic grounding\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 47\n  last_seen_round: 48\n  resolution: 'v53: Discussion §5 causal ablation chain + ANOVA η².'\n  resolution_round: 53\n- id: R48-N1\n  summary: Drifting features高度共线性(r≈0.97)\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v53: Results §4.2 group ablation + PCA + collinear acknowledgment.'\n  resolution_round: 53\n- id: R48-N2\n  summary: DDR阈值post-hoc验证circularity\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v54: per-generator independent replication叙事.'\n  resolution_round: 54\n- id: R48-N3\n  summary: DDR与Geng et al.(2026)新颖性区分不充分\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v54: discussion.tex区分DDR vs Geng贡献.'\n  resolution_round: 54\n- id: R48-N4\n  summary: Abstract headline metric定义混淆\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v53: Abstract L5 binary F1标注 + QLoRA条件标注.'\n  resolution_round: 53\n- id: R48-DIV1\n  summary: Base-model-only overclaim\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v54: \"empirical regularity of base-model autoregressive generation\".'\n  resolution_round: 54\n- id: R48-W1\n  summary: Qwen过度代表(3/8)\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v53: tail_decay weakly stationary标注.'\n  resolution_round: 53\n- id: R48-W2\n  summary: XGBoost超参数固定不调\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 51\n  resolution: 'v53: max_depth sweep, F1变动≤2.0pp.'\n  resolution_round: 53\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R51 再次提出应做完整 grid/random search, R2 认为 Table 11 classifier sensitivity 分析部分缓解. 建议补充一次 systematic tuning 结果.'\n- id: R48-W3\n  summary: Binary F1=0.694实际应用价值未grounding\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v55: proof-of-concept定位.'\n  resolution_round: 55\n- id: R48-W4\n  summary: tail_decay rank范围(100-1000)缺justification\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v55: method.tex rank range justification.'\n  resolution_round: 55\n- id: R48-W5\n  summary: 页面限制可能超标~0.2页\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 49\n  resolution: 'v55+: Results压缩22行 + enlargethispage移除. 主文8页.'\n  resolution_round: 55\n- id: R48-W6\n  summary: 仅英语+3域\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v55: Limitations covers English-only + 3 domains.'\n  resolution_round: 55\n- id: R48-W7\n  summary: Perturbation仅测word replacement\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v55: acknowledged in Limitations.'\n  resolution_round: 55\n- id: R48-W8\n  summary: Table 3缺concurrent depth methods对比\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 48\n  last_seen_round: 48\n  resolution: 'v55: concurrent studies不可直接纳入baselines.'\n  resolution_round: 55\n- id: R49-MF1\n  summary: LOGO CI bootstrap单位未明确——text-level CI可能低估generator-level泛化不确定性\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 50\n  resolution: 'v55: Table 1 caption加text-level bootstrap说明; §4.1 generator-level mean±SE: 0.694±0.010; cross-generator SD=0.028, IQR=[0.692,0.714].'\n  resolution_round: 55\n- id: R49-MF2\n  summary: 泛化性措辞超出实验范围——Abstract/Conclusion overclaim\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 50\n  resolution: 'v55: Abstract \"important\"+\"complements location drift for ordinal depth grading\"; Conclusion \"within the studied base-model scope\".'\n  resolution_round: 55\n- id: R49-MF3\n  summary: DDR新颖性定位模糊——描述性发现缺mechanistic grounding\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 50\n  resolution: 'v55: Discussion恢复mechanistic rationale句.'\n  resolution_round: 55\n- id: R49-MF4\n  summary: 实际应用动机与受控实验gap——downstream utility近null result\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 49\n  resolution: 'v55: Discussion \"Preliminary batch-level estimates suggest depth constitutes a new analytical dimension\".'\n  resolution_round: 55\n- id: R49-SF1\n  summary: TOST margin |d|≤0.20缺task-specific理据\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 51\n  resolution: 'v55: Appendix ddr-validation TOST margin rationale paragraph added.'\n  resolution_round: 55\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R51 再次提出 d=0.20 缺 task-specific 论证. R2 认为实际影响有限(shape features d<0.10). 建议增加 sensitivity analysis 或明确标注为 working threshold.'\n- id: R49-SF2\n  summary: 特征冗余性未充分讨论——entropy_mean与hapax_ratio r=0.81\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 49\n  resolution: 'v55: Results §4.2 \"collinear drifting triplet captures ~1 effective dimension (PCA PC1=92.3%)\".'\n  resolution_round: 55\n- id: R49-SF3\n  summary: 3-to-5 class分辨率天花板——有效粒度为3-class\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 51\n  resolution: 'Existing coverage sufficient: Limitations \"F1≈0.50\" + Discussion \"practical resolution limit\".'\n  resolution_round: 55\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R51 两位 Reviewer 认为主文对 5-class 结果讨论仍不足. 标题 \"Depth Profiling\" 暗示任意深度分类, 但有效粒度仅 3 classes.'\n- id: R49-SF4\n  summary: Concurrent works区分度论述过于简略\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 49\n  resolution: 'v55: R50 R2-S6确认Table 48 concurrent work对比清晰.'\n  resolution_round: 55\n- id: R49-SF5\n  summary: QLoRA与XGBoost比较framing——信息粒度不对等\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 50\n  resolution: 'v55: Table 3 caption \"information-asymmetric ceiling, not a fair comparison\".'\n  resolution_round: 55\n- id: R49-SF6\n  summary: Primary metric未明确声明——Abstract多个F1数字混乱\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 50\n  resolution: 'v55: §4.1 \"leak-free binary F1 (gen-1 vs. gen-2+, our primary conservative metric)=0.694\".'\n  resolution_round: 55\n- id: R49-SF7\n  summary: Handcrafted vs end-to-end trade-off讨论不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 49\n  resolution: 'v55: Results §4.1 + Table 3 information-asymmetry annotation.'\n  resolution_round: 55\n- id: R49-MR1\n  summary: 'Missing: Schaeffer et al. (2025) model collapse定义多样性'\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 49\n  resolution: 'v55: Camera-ready audit confirmed 73/73 bib entries matched.'\n  resolution_round: 55\n- id: R49-MR2\n  summary: 'Missing: Hans et al. (2024) Binoculars方法论相似性未讨论'\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 49\n  resolution: 'v55: Hans et al. already cited.'\n  resolution_round: 55\n- id: R49-MR3\n  summary: 'Missing: paraphrase/rewriting attack文献'\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 50\n  resolution: 'v55: Krishna et al. cited in robustness discussion.'\n  resolution_round: 55\n- id: R49-MR4\n  summary: 'Missing: fine-grained span-level AI text detection'\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 49\n  last_seen_round: 49\n  resolution: 'v55: Span-level detection references added.'\n  resolution_round: 55\n- id: R50-N1\n  summary: Shape feature causal overclaim — LOFO/PI证据与Abstract因果声称矛盾\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 50\n  resolution: 'v55: Abstract \"shape stability complements location drift for ordinal depth grading\".'\n  resolution_round: 55\n- id: R50-N2\n  summary: Gen-0种子共享导致LOGO 3-class F1=0.762被高估约3pp\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 50\n  resolution: 'v55: Binary F1=0.694 as primary metric; 3-class annotation \"carries upward bias\".'\n  resolution_round: 55\n- id: R50-N3\n  summary: Instruction tuning失效在主文讨论不足——动机与适用范围脱节\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 50\n  resolution: 'v55: Limitations expanded instruct tuning discussion (~150 words).'\n  resolution_round: 55\n- id: R50-W1\n  summary: '\"Depth profiling\"命名暗示超出3-class的精细粒度'\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 50\n  resolution: 'v55: Intro defines \"coarse ordinal classification into gen-0/gen-1/gen-2+\".'\n  resolution_round: 55\n- id: R50-W2\n  summary: Entropy术语全文使用但实际指reference-model NLL (R32-W3复发)\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 51\n  resolution: 'v55: Table 1 caption NLL-based annotation; §4.2 parenthetical clarification.'\n  resolution_round: 55\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R51 两位 Reviewer 再次指出 \"entropy\" 术语全文使用仍有误导性, 特征名仍为 entropy_mean/entropy_std 等. R2 建议全文统一使用 NLL 或 ref-entropy. 此问题已跨 14 轮反复出现.'\n- id: R50-W3\n  summary: Entropy_std intermediate (d=0.55)挑战DDR binary partition叙事\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 50\n  resolution: 'v55: Intro Contribution #1 now lists \"three response zones\".'\n  resolution_round: 55\n- id: R50-W4\n  summary: 3-class F1低于最强baseline但主文未充分讨论\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 50\n  resolution: 'v55: §4.3 \"though the latter leads by 2.1pp on 3-class F1 (0.795 vs. 0.774)\".'\n  resolution_round: 55\n- id: R50-W5\n  summary: Stylometry/authorship attribution related work覆盖不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 50\n  last_seen_round: 50\n  resolution: 'v55: Stylometry connection addressed.'\n  resolution_round: 55\n# === Round 51 新发现 ===\n- id: R51-N1\n  summary: 温度敏感性在主文讨论严重不足——t=0.9时F1降15%但§4.3仅3行,与\"empirical regularity\"声明矛盾\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R1-N1提出,R2完全AGREE. t=0.9时3-class F1从0.762降至0.647(-15%),CI不重叠. Cross-temperature迁移(t=0.7→t=1.0)严重退化. 主文§4.3仅~3行,Limitations仅说\"single decoding regime\". Conclusion中\"empirical regularity\"需加温度条件限定. 与R29-W3(仅Abstract标注)不同,本轮要求主文§4.3或§5用至少一段讨论温度敏感性机制.'\n  action_items:\n  - round: 51\n    action: '§4.3或§5增加温度敏感性专段(高温使分布更平坦,DDR信号稀释); Limitations将温度列为主要限制; Conclusion \"empirical regularity\"加温度条件限定'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-N2\n  summary: Binary F1=0.694实际意义未论证——gen-1/gen-2+错误率48.4%应在主文讨论,需明确feasibility study定位\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R1-N2+R2-N3共识. 0.694意味着~30%样本被错分,gen-1→gen-2+边界错误率48.4%(Appendix i). 3-class F1=0.762被gen-0高可分性拉高(gen-0 F1=0.921). 论文framing暗示实用价值但性能不支持. 建议: (1)主文讨论什么应用能容忍此错误率; (2)将Appendix i核心发现提升到主文; (3)更显著地标注feasibility study/proof-of-concept. R34-W2标记wont_fix(结构性限制),本轮更聚焦framing gap.'\n  action_items:\n  - round: 51\n    action: '§4.1或§5增加gen-1/gen-2+边界错误分析(从Appendix提取); 讨论应用容忍度; 加强proof-of-concept定位显著性'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-N3\n  summary: DDR新颖性质疑——shape稳定性可能从架构约束(log|V|,softmax geometry)trivially推导\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R2-N1提出,R1 AGREE(但补充组合价值). DDR拆解为:(1)location drift与Shumailov/Dohmatob方向一致; (2)shape stability论文自身§5归因于架构约束. 如果核心发现可从已知约束推导,贡献定位降为验证性. R1认为组合+LOGO验证跨生成器迁移有增量价值,但更适合Findings级别. 与R42-N1/R49-MF3不同,本轮聚焦\"predictable from first principles\"角度.'\n  action_items:\n  - round: 51\n    action: '§5论证shape稳定性并非trivially predictable(提供反例场景/边界条件); 或强化DDR downstream utility的不可替代性'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-N4\n  summary: Base-model-only限制实际价值——instruct模型下cross-generator transfer未验证,QLoRA恢复仅within-model\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R2-N2提出,R1完全AGREE. Instruct模型下DDR信号压缩(3-class F1降3.7-19.9pp). QLoRA F1=0.89-0.91仅是within-model 5-fold CV,非cross-generator LOGO. Base→instruct迁移F1=0.490. 现实递归生成几乎全来自instruct/RLHF模型. 虽然标题已标注\"Base-Model\",Limitations已承认,但应更直接讨论base model场景的独立价值(如pretraining data contamination检测). 与R34-W1/R50-N3(已resolved)相比,本轮新增QLoRA within-model vs LOGO区分的关注.'\n  action_items:\n  - round: 51\n    action: '讨论base model场景独立价值(pretraining corpus auditing); 明确QLoRA恢复是within-model而非cross-generator; 补充或承认instruct LOGO缺失'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-N5\n  summary: DDR描述性框架与分类任务逻辑断层——分类器不使用DDR分区信息(R1提出,R2部分反驳)\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R1-N3提出DDR是post-hoc框架,分类器使用全部7个原始特征而非DDR-derived representation. R2 REBUT: DDR是解释性框架不是处方性组件,LOFO/ANOVA提供经验支撑(Table 8-9, Figure 7). 但R2同意论文叙事在\"DDR解释分类\"和\"DDR驱动分类\"间摇摆,修正framing是必要的writing fix. 降级为warning(分歧点,R2论据有力但R1关切合理).'\n  action_items:\n  - round: 51\n    action: '明确DDR定位为解释性框架(explains why)而非分类组件(drives how); 修正§4.2/§5中暗示DDR驱动分类的表述'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-W1\n  summary: '\"Entropy\"术语全文误导(第15次提出)——特征名仍为entropy_*,关键位置NLL说明不足'\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R2-W1提出,R1 AGREE. 特征命名仍为entropy_mean/entropy_std等,§3.3有一次澄清但后续全文回归entropy. R2建议统一使用NLL或ref-entropy. 此问题从R32-W3起跨14轮反复出现,每轮resolution为在关键位置加注释,但未全面改命名. 作为结构性问题,建议Research Director考虑是否值得大规模改命名.'\n  action_items:\n  - round: 51\n    action: '评估全文改名(entropy→NLL/ref-entropy)的可行性和收益; 至少在Introduction首次出现处和Table 1中统一加注'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-W2\n  summary: OOD detection方法论连接在Related Work中完全缺失\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R2-W3提出,R1 AGREE. NLL统计特征(均值/方差/极值)与OOD detection方法论高度重叠. 近期有\"Human Texts Are Outliers\"(arXiv 2510.08602)直接将AI文本检测重构为OOD detection问题. Related Work应补充简要讨论.'\n  action_items:\n  - round: 51\n    action: 'Related Work §2增加OOD detection方法论简要讨论(1-2句), 说明depth profiling与OOD的区别(ordinal vs binary, cross-generator transfer)'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-W3\n  summary: 跨域实验规模过小(每域200seeds)+Code域F1=0.63下降未分析\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R1-W4提出,R2 AGREE. Appendix j每域仅200 seeds×depth 3,样本量小. Code域binary F1降至0.63但无分析(是否因Wikipedia-trained参考模型在Code上NLL失效?). R2补充:应讨论Code域下降原因并标注为preliminary/exploratory.'\n  action_items:\n  - round: 51\n    action: '扩大跨域实验规模或标注为preliminary; 讨论Code域性能下降原因'\n    assigned_to: PaperAgent\n    status: open\n- id: R51-W4\n  summary: Discussion §5 机制解释(log|V| bound, softmax geometry)是post-hoc直觉,vocab size差异可能反驳\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 51\n  last_seen_round: 51\n  mentions:\n  - round: 51\n    reviewers: [R1, R2]\n    note: 'R2-W5提出,R1部分REBUT(vocab size技术上不影响,但同意是post-hoc). §5将shape稳定性归因于log|V|上界和softmax geometry,但Pythia(50K vocab)和Qwen(150K+ vocab)展现类似稳定性. R1指出实际entropy max远低于上界(~4-5 vs log50K≈10.8),vocab size差异不影响定性结论. 共识: 将机制解释标注为hypothesis/conjecture.'\n  action_items:\n  - round: 51\n    action: '§5机制解释标注为hypothesis/conjecture而非definitional claim'\n    assigned_to: PaperAgent\n    status: open"
  }
}
```

</details>

---


### Tool result

_source line 4045 · 2026-05-24T23:08:29.629666+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml\", \"bytes\": 33574}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4046 · 2026-05-24T23:10:53.781854+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 51 (Fresh Review)\n\n**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh (重新审稿，无前轮记忆)\n**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计; R2: 新颖性+写作质量)\n**轮次**: 1 轮（交叉回应后关键问题达成共识，无需第 2 轮）\n\n---\n\n## Summary\n\n论文定义了 \"depth profiling\" 任务——将文本分类为 gen-0（人类）/ gen-1（首次生成）/ gen-2+（多次递归生成），提出 Differential Depth Response (DDR) 框架：recursive base-model generation 下，NLL 分布的 location 特征（entropy mean, TTR, hapax ratio）随深度单调漂移（Cohen's d = 0.74–1.05），而 shape 特征（entropy max, min, tail decay）近似稳定（d < 0.10）。利用 7 个特征 + XGBoost，在 8 个 base-model 生成器（5 个 family，0.6B–8B）上实现 LOGO 3-class F1 = 0.762, leak-free binary F1 = 0.694。\n\n---\n\n## Strengths\n\n**S1** [R1+R2 共识] **研究问题的原创性**：从 binary AI detection 扩展到 ordinal depth classification 是 genuinely novel 的任务定义，填补了 binary detection 与 model collapse 分析之间的空白。\n\n**S2** [R1+R2 共识] **统计方法论严谨程度远超 ACL 平均水平**：Bootstrap CI、Bonferroni 校正、TOST 等价性检验、permutation testing、Granger 因果分析、ANOVA 方差分解——多层次统计验证体系在 NLP 实证论文中罕见。\n\n**S3** [R1+R2 共识] **消融实验覆盖面 exemplary**：26 页附录涵盖温度敏感性、prompt 泛化、文本扰动鲁棒性、跨域迁移、解码策略、参考模型选择、指令微调、finer-grained depth、classifier sensitivity 等 20+ 实验，覆盖了几乎所有可预见的审稿疑问。\n\n**S4** [R1+R2 共识] **DDR 分解的清晰性**：Location drift vs. shape stability 的二元分解是干净、可量化的经验发现（≥8× effect-size gap），ANOVA 方差分解（η²_depth = 0.34–0.37 for location vs. <0.01 for shape，>48× gap）提供有力统计支撑。\n\n**S5** [R1] **LOGO/LOFO 评估协议设计合理**：Leave-One-Generator-Out 和 Leave-One-Family-Out 提供多层次泛化测试；gen-0 共享种子问题通过 independent-seed 实验（F1 = 0.680 vs. 0.694）得到妥善处理。\n\n**S6** [R1+R2 共识] **诚实的局限性讨论**：坦率报告 instruction-tuned 模型下的性能退化、gen-1/gen-2+ 边界的高错误率、base-model-only 限制，未 overclaim。\n\n**S7** [R1+R2 共识] **可复现性高**：匿名代码仓库、标准工具（XGBoost、Pythia-410M）、详尽实验参数。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [R1+R2 共识] **温度敏感性在主文讨论严重不足**\nt=0.9 时 3-class F1 从 0.762 降至 0.647（−15%），95% CI 不重叠；cross-temperature 迁移（t=0.7 训练→t=1.0 测试）严重退化，部分 generator（如 Qwen-1.7B）F1 降至 0.418。主文 §4.3 仅约 3 行简述，Limitations 仅提 \"single decoding regime\"，与 Conclusion \"DDR is an empirical regularity\" 的强声明矛盾。需要在主文用至少一段讨论温度敏感性的机制和影响，并在 Conclusion 中加温度条件限定。\n\n**N2** [R1+R2 共识] **Binary F1=0.694 的实际意义未被充分论证**\n排除 trivial 的 gen-0 分类后，gen-1 vs. gen-2+ 的核心区分能力仅 F1=0.694（~30% 错分率），gen-1→gen-2+ 边界错误率高达 48.4%（Appendix i）。3-class F1=0.762 被 gen-0 高可分性（F1≈0.921）拉高，实质上 depth profiling 相对于 binary detection 的增量价值应由 gen-1/gen-2+ 区分衡量。论文 framing 暗示实用价值（§1 \"data provenance and corpus curation\"），但性能数据不支持。应将核心错误分析从 Appendix 提升到主文，并更显著地标注 feasibility study 定位。\n\n**N3** [R2 提出, R1 同意] **DDR 新颖性质疑——shape 稳定性可能从架构约束 trivially 推导**\nDDR 核心发现可拆解为：(1) location drift 与 Shumailov et al. (2024) 尾部侵蚀方向一致（场景不同但机制类似）；(2) shape stability 论文自身 §5 归因于 \"architecturally bounded: entropy max by log|V|, tail decay by softmax geometry\"，暗示这是模型固有约束而非递归生成独特发现。R1 补充：组合价值和 LOGO 跨生成器验证有增量贡献，但更适合 Findings 级别。需要论证 shape 稳定性为何不是 trivially predictable（提供反例/边界条件），或强化 DDR 的 downstream utility 不可替代性。\n\n**N4** [R2 提出, R1 同意] **Base-model-only 限制实际价值**\nInstruction-tuned 模型下 DDR 信号大幅压缩（3-class F1 下降 3.7–19.9 pp）；QLoRA 恢复（F1=0.89–0.91）仅是 within-model 5-fold CV，非 cross-generator LOGO——而 cross-generator transfer 正是论文核心卖点。Base→instruct 迁移 F1=0.490（Table 19），实际场景中递归生成几乎全来自 instruct/RLHF 模型。虽然标题已标注 \"Base-Model\"，但应更直接讨论 base model 场景的独立价值（如 pretraining corpus contamination 检测），并明确 QLoRA 恢复的评估局限性。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [R1 提出, R2 部分反驳] **DDR 描述性框架与分类任务之间的逻辑断层**\nDDR 是 post-hoc 解释性框架，分类器使用全部 7 个原始特征而非 DDR 分解后的 derived representation。R2 提供了有力反驳：LOFO 分析（Table 8-9）验证了两类特征独立贡献，ANOVA（Figure 7）量化了分区的统计显著性，DDR 类似于 bias-variance tradeoff 的解释角色。但两位 Reviewer 同意论文叙事在 \"DDR 解释分类\" 和 \"DDR 驱动分类\" 之间摇摆，需要修正 framing。\n\n**W2** [R1+R2 共识] **\"Entropy\" 术语全文误导性使用**\n§3.3 定义 \"entropy\" 为 reference-model NLL，但特征命名始终使用 entropy_mean、entropy_std 等，DDR 分析中讨论 \"entropy stability\" 可能使读者误解为信息论 entropy 的稳定性。此问题从 Round 32 起跨 14 轮反复出现。建议评估全文统一使用 \"NLL\" 或 \"ref-entropy\" 的可行性，至少在 Introduction 首次出现和 Table 1 中加强标注。\n\n**W3** [R2 提出, R1 同意] **OOD Detection 方法论连接缺失**\nNLL 统计特征与 OOD detection 方法论高度重叠，近期有 \"Human Texts Are Outliers\" 直接将 AI 文本检测重构为 OOD 问题。Related Work §2 应补充简要讨论，说明 depth profiling 与 OOD detection 的区别。\n\n**W4** [R1+R2 共识] **跨域实验规模过小 + Code 域性能下降未分析**\nAppendix j 每域仅 200 seeds × depth 3，Code 域 binary F1 降至 0.63 但缺乏原因分析。建议扩大规模或明确标注为 preliminary/exploratory，并讨论 Code 域下降原因。\n\n**W5** [R1+R2 共识] **Discussion §5 机制解释是 post-hoc 直觉**\nShape 稳定性归因于 \"log|V| bound\" 和 \"softmax geometry\" 是直觉性解释，非 formal verification。R1 指出 Pythia (50K vocab) 和 Qwen (150K+ vocab) 类似稳定性并不反驳（实际值远低于上界），但同意应标注为 hypothesis/conjecture。\n\n**W6** [R1 提出, R2 认同] **XGBoost 固定超参数未调优**\nn_estimators=200, max_depth=6, lr=0.1 接近默认值。Table 11 的 classifier sensitivity 分析部分缓解（LR 0.71, RF 0.725, XGBoost 0.762），但应补充一次 systematic tuning 结果。\n\n**W7** [R1+R2 共识] **5-class 深度分类性能主文讨论不足**\n5-class F1≈0.50（Table 5），表明深度分辨率被 bound 在约 3 classes。标题 \"Depth Profiling\" 暗示任意深度分类可能性，但主文几乎未讨论这一天花板。\n\n**W8** [R1 提出, R2 部分反驳] **泛化声明可能过度**\nAbstract/Conclusion 使用 \"empirical regularity\" 等强语言，但实验覆盖有限（≤8B 参数、英文 Wikipedia、主要 t=0.7）。R2 认为在当前覆盖范围内术语合理，但同意应加温度条件限定。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **研究问题新颖、实验设计严谨**——两位 Reviewer 一致认可任务定义的原创性和统计方法论的高水准\n2. **F1=0.694 实际意义有限**——gen-1/gen-2+ 核心区分接近 coin-flip，3-class F1 被 gen-0 拉高\n3. **Base-model-only 限制严重**——instruct 模型下信号退化，QLoRA 恢复非 cross-generator\n4. **温度敏感性削弱泛化声明**——t=0.9 F1 降 15%，主文讨论不足\n5. **DDR 更适合定位为 empirical finding 而非方法论贡献**\n6. **\"Entropy\" 术语需全文修正**\n7. **OOD detection 方法论连接缺失**\n8. **格式完全合规**（正文 ≤8 页、Limitations 存在、匿名化合规、AI 披露完整）\n9. **建议 Findings 接收**\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **DDR 形式化断层的严重性**：R1 认为 DDR 与分类之间存在逻辑断层（critical），R2 反驳认为 DDR 作为解释性框架合理且有 LOFO/ANOVA 支撑（降级为 writing fix）。**Director 判断**：R2 论据更有力（LOFO Table 8-9 确实验证了两组特征的独立贡献），但 R1 的关切合理——论文叙事确实在 \"explains\" 和 \"drives\" 之间摇摆。降级为 Should-Fix (W1)。\n\n2. **泛化声明的合理性**：R1 认为 \"empirical regularity\" 过强，R2 认为在实验覆盖范围内合理但需加温度限定。**Director 判断**：温度限定是关键——加上条件后表述可接受。纳入 N1 的 action item。\n\n---\n\n## Questions\n\n1. 如果论文能展示至少一个 instruction-tuned 模型的 LOGO 评估结果（即使性能下降），是否足以回应 base-model-only 的关切？\n2. DDR 的 shape stability 是否有反例——是否存在某种生成条件（如极高温度 t≥1.2、或特定架构如 MoE）下 shape 也会漂移？\n3. Gen-1/gen-2+ 区分的 oracle 上限是多少？最佳单 generator 内分类性能 vs. 跨 generator 的 gap 有多大？\n\n---\n\n## Missing References\n\n1. **OOD detection 方法论文献**：NLL/perplexity-based OOD detection（如 \"Human Texts Are Outliers\", arXiv 2510.08602）——R2-W3, R1 同意\n2. **注**：R2-W2 建议补充与 concurrent work（Broken Telephone, Markovian Chains）的实证对比，R1 REBUT 认为标准过高。Director 判断：概念对比（Appendix z.8 Table 52）已充分，实证对比为 nice-to-have 而非 must-fix。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置未启用 external_review.paperreview_ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done (完成于 2026-05-24 22:55 UTC)\n**总计**: 0 critical, 1 warning, 15 info\n\n**Warning:**\n- Page 16: Table 11（classifier comparison）和 Table 13（sampling sensitivity）列数较多，字号明显缩小。Table 13 有 7+ 列，部分数字在正常缩放下可读性差，建议检查 `\\resizebox` 调整。\n\n**Info highlights:**\n- Page 1: 首页无 display item，Figure 1 在 page 2 顶部。Abstract 信息密度高，影响有限。\n- Page 4: Figure 2 pipeline 图部分内部文字框字号偏小。\n- Page 6: Figure 4 单栏尺寸偏小，数据点和 axis labels 处于可读性下限，建议改为 figure*。\n- Page 7: 单页 3 个 display items（Figure 5 + Figure 6 + Table 3），信息密度极高但未溢出。\n- Page 36: 末页底部约 1/4 空白，作为附录最后一页可接受。\n\n整体排版质量良好，无 critical 问题。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 — Borderline Conference\n**建议**: Findings 接收\n\n**置信度**: 4/5（两位 Reviewer 均对 AI text detection、distributional analysis 和 model collapse 领域熟悉）\n\n**理由**:\n论文定义了一个 genuinely novel 的任务（depth profiling），提供了 clean 的经验分解（DDR），实验设计和统计方法论的严谨程度在 ACL 社区中属 top-tier。这些优势使其适合 ACL 出版物。\n\n然而，四个核心问题限制了其主会议级别的影响力：(1) 中等性能（binary F1=0.694）下的实际价值论证不足；(2) 仅限 base model，instruct 模型下信号退化且缺 cross-generator 验证；(3) DDR shape stability 的新颖性可能从架构约束 trivially 推导；(4) 温度敏感性（t=0.9 降 15%）与 \"empirical regularity\" 泛化声明矛盾。\n\n综合来看，论文的 task formulation 和 empirical rigor 具有独立学术价值，适合 Findings 接收。若能充分回应 N1-N4（温度讨论、性能定位、新颖性论证、instruct scope），可重新考虑主会议。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"data provenance and corpus curation\" 动机偏强，与当前性能不匹配。建议加 \"feasibility\" 或 \"exploratory\" 限定。\n- 脚注 1 匿名 GitHub repo 合规，无泄露。\n\n### §3 Method\n- Table 1 特征命名建议从 entropy_* 改为 nll_* 或加注。\n- Figure 2 (c) LOGO 示意图中 \"evaluation folds on one generator\" 可改为 \"held-out generator\"。\n- §3.3 \"entropy\" 术语定义后续未一致执行。\n\n### §4 Results\n- §4.1: Binary F1=0.694 作为 primary metric 标注清晰，但应在此处讨论 gen-1/gen-2+ 错误率而非仅引用 Appendix。\n- §4.2: DDR 形式化定义清晰，k-means validation (sil=0.660) 有效。但 Cohen's d=0.20 阈值应注明来源或敏感性。\n- §4.3: 温度敏感性讨论不足，是最需要加强的段落。\n- Table 3: Binoculars binary F1=0.539 远低于其 binary detection SOTA，值得简要分析原因（设计目标不同）。\n\n### §5 Discussion\n- 机制解释（log|V|, softmax geometry）应标注为 hypothesis。\n- 与 model collapse 的区分（fixed parameters vs. weight updates）清晰有效。\n- ANOVA 方差分解（Figure 7）是论文最有力的统计证据之一。\n\n### §6 Conclusion\n- \"empirical regularity\" 需加温度和 base-model 条件限定。\n\n### Limitations\n- 内容充分（3 点：base models, English Wikipedia, depth resolution），但温度敏感性应作为第 4 点显著列出。\n\n### Appendix\n- 覆盖面极广，是论文最大优势之一。\n- Table 13 (p.16) 排版需优化（字号过小）。\n- Appendix i (error analysis) 核心发现应提升到主文。",
  "project": "gen-depth-fingerprint",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference (建议 Findings 接收)",
  "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 51 (Fresh Review)\n\n**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh (重新审稿，无前轮记忆)\n**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计; R2: 新颖性+写作质量)\n**轮次**: 1 轮（交叉回应后关键问题达成共识，无需第 2 轮）\n\n---\n\n## Summary\n\n论文定义了 \"depth profiling\" 任务——将文本分类为 gen-0（人类）/ gen-1（首次生成）/ gen-2+（多次递归生成），提出 Differential Depth Response (DDR) 框架：recursive base-model generation 下，NLL 分布的 location 特征（entropy mean, TTR, hapax ratio）随深度单调漂移（Cohen's d = 0.74–1.05），而 shape 特征（entropy max, min, tail decay）近似稳定（d < 0.10）。利用 7 个特征 + XGBoost，在 8 个 base-model 生成器（5 个 family，0.6B–8B）上实现 LOGO 3-class F1 = 0.762, leak-free binary F1 = 0.694。\n\n---\n\n## Strengths\n\n**S1** [R1+R2 共识] **研究问题的原创性**：从 binary AI detection 扩展到 ordinal depth classification 是 genuinely novel 的任务定义，填补了 binary detection 与 model collapse 分析之间的空白。\n\n**S2** [R1+R2 共识] **统计方法论严谨程度远超 ACL 平均水平**：Bootstrap CI、Bonferroni 校正、TOST 等价性检验、permutation testing、Granger 因果分析、ANOVA 方差分解——多层次统计验证体系在 NLP 实证论文中罕见。\n\n**S3** [R1+R2 共识] **消融实验覆盖面 exemplary**：26 页附录涵盖温度敏感性、prompt 泛化、文本扰动鲁棒性、跨域迁移、解码策略、参考模型选择、指令微调、finer-grained depth、classifier sensitivity 等 20+ 实验，覆盖了几乎所有可预见的审稿疑问。\n\n**S4** [R1+R2 共识] **DDR 分解的清晰性**：Location drift vs. shape stability 的二元分解是干净、可量化的经验发现（≥8× effect-size gap），ANOVA 方差分解（η²_depth = 0.34–0.37 for location vs. <0.01 for shape，>48× gap）提供有力统计支撑。\n\n**S5** [R1] **LOGO/LOFO 评估协议设计合理**：Leave-One-Generator-Out 和 Leave-One-Family-Out 提供多层次泛化测试；gen-0 共享种子问题通过 independent-seed 实验（F1 = 0.680 vs. 0.694）得到妥善处理。\n\n**S6** [R1+R2 共识] **诚实的局限性讨论**：坦率报告 instruction-tuned 模型下的性能退化、gen-1/gen-2+ 边界的高错误率、base-model-only 限制，未 overclaim。\n\n**S7** [R1+R2 共识] **可复现性高**：匿名代码仓库、标准工具（XGBoost、Pythia-410M）、详尽实验参数。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [R1+R2 共识] **温度敏感性在主文讨论严重不足**\nt=0.9 时 3-class F1 从 0.762 降至 0.647（−15%），95% CI 不重叠；cross-temperature 迁移（t=0.7 训练→t=1.0 测试）严重退化，部分 generator（如 Qwen-1.7B）F1 降至 0.418。主文 §4.3 仅约 3 行简述，Limitations 仅提 \"single decoding regime\"，与 Conclusion \"DDR is an empirical regularity\" 的强声明矛盾。需要在主文用至少一段讨论温度敏感性的机制和影响，并在 Conclusion 中加温度条件限定。\n\n**N2** [R1+R2 共识] **Binary F1=0.694 的实际意义未被充分论证**\n排除 trivial 的 gen-0 分类后，gen-1 vs. gen-2+ 的核心区分能力仅 F1=0.694（~30% 错分率），gen-1→gen-2+ 边界错误率高达 48.4%（Appendix i）。3-class F1=0.762 被 gen-0 高可分性（F1≈0.921）拉高，实质上 depth profiling 相对于 binary detection 的增量价值应由 gen-1/gen-2+ 区分衡量。论文 framing 暗示实用价值（§1 \"data provenance and corpus curation\"），但性能数据不支持。应将核心错误分析从 Appendix 提升到主文，并更显著地标注 feasibility study 定位。\n\n**N3** [R2 提出, R1 同意] **DDR 新颖性质疑——shape 稳定性可能从架构约束 trivially 推导**\nDDR 核心发现可拆解为：(1) location drift 与 Shumailov et al. (2024) 尾部侵蚀方向一致（场景不同但机制类似）；(2) shape stability 论文自身 §5 归因于 \"architecturally bounded: entropy max by log|V|, tail decay by softmax geometry\"，暗示这是模型固有约束而非递归生成独特发现。R1 补充：组合价值和 LOGO 跨生成器验证有增量贡献，但更适合 Findings 级别。需要论证 shape 稳定性为何不是 trivially predictable（提供反例/边界条件），或强化 DDR 的 downstream utility 不可替代性。\n\n**N4** [R2 提出, R1 同意] **Base-model-only 限制实际价值**\nInstruction-tuned 模型下 DDR 信号大幅压缩（3-class F1 下降 3.7–19.9 pp）；QLoRA 恢复（F1=0.89–0.91）仅是 within-model 5-fold CV，非 cross-generator LOGO——而 cross-generator transfer 正是论文核心卖点。Base→instruct 迁移 F1=0.490（Table 19），实际场景中递归生成几乎全来自 instruct/RLHF 模型。虽然标题已标注 \"Base-Model\"，但应更直接讨论 base model 场景的独立价值（如 pretraining corpus contamination 检测），并明确 QLoRA 恢复的评估局限性。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [R1 提出, R2 部分反驳] **DDR 描述性框架与分类任务之间的逻辑断层**\nDDR 是 post-hoc 解释性框架，分类器使用全部 7 个原始特征而非 DDR 分解后的 derived representation。R2 提供了有力反驳：LOFO 分析（Table 8-9）验证了两类特征独立贡献，ANOVA（Figure 7）量化了分区的统计显著性，DDR 类似于 bias-variance tradeoff 的解释角色。但两位 Reviewer 同意论文叙事在 \"DDR 解释分类\" 和 \"DDR 驱动分类\" 之间摇摆，需要修正 framing。\n\n**W2** [R1+R2 共识] **\"Entropy\" 术语全文误导性使用**\n§3.3 定义 \"entropy\" 为 reference-model NLL，但特征命名始终使用 entropy_mean、entropy_std 等，DDR 分析中讨论 \"entropy stability\" 可能使读者误解为信息论 entropy 的稳定性。此问题从 Round 32 起跨 14 轮反复出现。建议评估全文统一使用 \"NLL\" 或 \"ref-entropy\" 的可行性，至少在 Introduction 首次出现和 Table 1 中加强标注。\n\n**W3** [R2 提出, R1 同意] **OOD Detection 方法论连接缺失**\nNLL 统计特征与 OOD detection 方法论高度重叠，近期有 \"Human Texts Are Outliers\" 直接将 AI 文本检测重构为 OOD 问题。Related Work §2 应补充简要讨论，说明 depth profiling 与 OOD detection 的区别。\n\n**W4** [R1+R2 共识] **跨域实验规模过小 + Code 域性能下降未分析**\nAppendix j 每域仅 200 seeds × depth 3，Code 域 binary F1 降至 0.63 但缺乏原因分析。建议扩大规模或明确标注为 preliminary/exploratory，并讨论 Code 域下降原因。\n\n**W5** [R1+R2 共识] **Discussion §5 机制解释是 post-hoc 直觉**\nShape 稳定性归因于 \"log|V| bound\" 和 \"softmax geometry\" 是直觉性解释，非 formal verification。R1 指出 Pythia (50K vocab) 和 Qwen (150K+ vocab) 类似稳定性并不反驳（实际值远低于上界），但同意应标注为 hypothesis/conjecture。\n\n**W6** [R1 提出, R2 认同] **XGBoost 固定超参数未调优**\nn_estimators=200, max_depth=6, lr=0.1 接近默认值。Table 11 的 classifier sensitivity 分析部分缓解（LR 0.71, RF 0.725, XGBoost 0.762），但应补充一次 systematic tuning 结果。\n\n**W7** [R1+R2 共识] **5-class 深度分类性能主文讨论不足**\n5-class F1≈0.50（Table 5），表明深度分辨率被 bound 在约 3 classes。标题 \"Depth Profiling\" 暗示任意深度分类可能性，但主文几乎未讨论这一天花板。\n\n**W8** [R1 提出, R2 部分反驳] **泛化声明可能过度**\nAbstract/Conclusion 使用 \"empirical regularity\" 等强语言，但实验覆盖有限（≤8B 参数、英文 Wikipedia、主要 t=0.7）。R2 认为在当前覆盖范围内术语合理，但同意应加温度条件限定。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **研究问题新颖、实验设计严谨**——两位 Reviewer 一致认可任务定义的原创性和统计方法论的高水准\n2. **F1=0.694 实际意义有限**——gen-1/gen-2+ 核心区分接近 coin-flip，3-class F1 被 gen-0 拉高\n3. **Base-model-only 限制严重**——instruct 模型下信号退化，QLoRA 恢复非 cross-generator\n4. **温度敏感性削弱泛化声明**——t=0.9 F1 降 15%，主文讨论不足\n5. **DDR 更适合定位为 empirical finding 而非方法论贡献**\n6. **\"Entropy\" 术语需全文修正**\n7. **OOD detection 方法论连接缺失**\n8. **格式完全合规**（正文 ≤8 页、Limitations 存在、匿名化合规、AI 披露完整）\n9. **建议 Findings 接收**\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **DDR 形式化断层的严重性**：R1 认为 DDR 与分类之间存在逻辑断层（critical），R2 反驳认为 DDR 作为解释性框架合理且有 LOFO/ANOVA 支撑（降级为 writing fix）。**Director 判断**：R2 论据更有力（LOFO Table 8-9 确实验证了两组特征的独立贡献），但 R1 的关切合理——论文叙事确实在 \"explains\" 和 \"drives\" 之间摇摆。降级为 Should-Fix (W1)。\n\n2. **泛化声明的合理性**：R1 认为 \"empirical regularity\" 过强，R2 认为在实验覆盖范围内合理但需加温度限定。**Director 判断**：温度限定是关键——加上条件后表述可接受。纳入 N1 的 action item。\n\n---\n\n## Questions\n\n1. 如果论文能展示至少一个 instruction-tuned 模型的 LOGO 评估结果（即使性能下降），是否足以回应 base-model-only 的关切？\n2. DDR 的 shape stability 是否有反例——是否存在某种生成条件（如极高温度 t≥1.2、或特定架构如 MoE）下 shape 也会漂移？\n3. Gen-1/gen-2+ 区分的 oracle 上限是多少？最佳单 generator 内分类性能 vs. 跨 generator 的 gap 有多大？\n\n---\n\n## Missing References\n\n1. **OOD detection 方法论文献**：NLL/perplexity-based OOD detection（如 \"Human Texts Are Outliers\", arXiv 2510.08602）——R2-W3, R1 同意\n2. **注**：R2-W2 建议补充与 concurrent work（Broken Telephone, Markovian Chains）的实证对比，R1 REBUT 认为标准过高。Director 判断：概念对比（Appendix z.8 Table 52）已充分，实证对比为 nice-to-have 而非 must-fix。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置未启用 external_review.paperreview_ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done (完成于 2026-05-24 22:55 UTC)\n**总计**: 0 critical, 1 warning, 15 info\n\n**Warning:**\n- Page 16: Table 11（classifier comparison）和 Table 13（sampling sensitivity）列数较多，字号明显缩小。Table 13 有 7+ 列，部分数字在正常缩放下可读性差，建议检查 `\\resizebox` 调整。\n\n**Info highlights:**\n- Page 1: 首页无 display item，Figure 1 在 page 2 顶部。Abstract 信息密度高，影响有限。\n- Page 4: Figure 2 pipeline 图部分内部文字框字号偏小。\n- Page 6: Figure 4 单栏尺寸偏小，数据点和 axis labels 处于可读性下限，建议改为 figure*。\n- Page 7: 单页 3 个 display items（Figure 5 + Figure 6 + Table 3），信息密度极高但未溢出。\n- Page 36: 末页底部约 1/4 空白，作为附录最后一页可接受。\n\n整体排版质量良好，无 critical 问题。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 — Borderline Conference\n**建议**: Findings 接收\n\n**置信度**: 4/5（两位 Reviewer 均对 AI text detection、distributional analysis 和 model collapse 领域熟悉）\n\n**理由**:\n论文定义了一个 genuinely novel 的任务（depth profiling），提供了 clean 的经验分解（DDR），实验设计和统计方法论的严谨程度在 ACL 社区中属 top-tier。这些优势使其适合 ACL 出版物。\n\n然而，四个核心问题限制了其主会议级别的影响力：(1) 中等性能（binary F1=0.694）下的实际价值论证不足；(2) 仅限 base model，instruct 模型下信号退化且缺 cross-generator 验证；(3) DDR shape stability 的新颖性可能从架构约束 trivially 推导；(4) 温度敏感性（t=0.9 降 15%）与 \"empirical regularity\" 泛化声明矛盾。\n\n综合来看，论文的 task formulation 和 empirical rigor 具有独立学术价值，适合 Findings 接收。若能充分回应 N1-N4（温度讨论、性能定位、新颖性论证、instruct scope），可重新考虑主会议。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"data provenance and corpus curation\" 动机偏强，与当前性能不匹配。建议加 \"feasibility\" 或 \"exploratory\" 限定。\n- 脚注 1 匿名 GitHub repo 合规，无泄露。\n\n### §3 Method\n- Table 1 特征命名建议从 entropy_* 改为 nll_* 或加注。\n- Figure 2 (c) LOGO 示意图中 \"evaluation folds on one generator\" 可改为 \"held-out generator\"。\n- §3.3 \"entropy\" 术语定义后续未一致执行。\n\n### §4 Results\n- §4.1: Binary F1=0.694 作为 primary metric 标注清晰，但应在此处讨论 gen-1/gen-2+ 错误率而非仅引用 Appendix。\n- §4.2: DDR 形式化定义清晰，k-means validation (sil=0.660) 有效。但 Cohen's d=0.20 阈值应注明来源或敏感性。\n- §4.3: 温度敏感性讨论不足，是最需要加强的段落。\n- Table 3: Binoculars binary F1=0.539 远低于其 binary detection SOTA，值得简要分析原因（设计目标不同）。\n\n### §5 Discussion\n- 机制解释（log|V|, softmax geometry）应标注为 hypothesis。\n- 与 model collapse 的区分（fixed parameters vs. weight updates）清晰有效。\n- ANOVA 方差分解（Figure 7）是论文最有力的统计证据之一。\n\n### §6 Conclusion\n- \"empirical regularity\" 需加温度和 base-model 条件限定。\n\n### Limitations\n- 内容充分（3 点：base models, English Wikipedia, depth resolution），但温度敏感性应作为第 4 点显著列出。\n\n### Appendix\n- 覆盖面极广，是论文最大优势之一。\n- Table 13 (p.16) 排版需优化（字号过小）。\n- Appendix i (error analysis) 核心发现应提升到主文。",
    "project": "gen-depth-fingerprint",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference (建议 Findings 接收)",
    "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
  }
}
```

</details>

---


### Tool result

_source line 4047 · 2026-05-24T23:10:57.594560+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3812
}
```

</details>

---


### Assistant

_source line 4048 · 2026-05-24T23:11:08.877882+00:00_

审稿报告已投递至 Research Director。

**Round 51 审稿完成总结**：

- **评分**: 3.5 / 5 (Borderline Conference)，建议 **Findings 接收**
- **两位 Reviewer 评分一致**（均 3.5），交叉回应后高度共识（12 AGREE / 2 partial REBUT）
- **4 个 Must-Fix**：温度敏感性讨论不足、F1=0.694 实际意义未论证、DDR 新颖性可能不足（shape stability trivially predictable）、base-model-only 限制实际价值
- **8 个 Should-Fix**：DDR 框架定位、entropy 术语、OOD 方法论连接、跨域实验规模、机制解释标注、XGBoost 调参、5-class 讨论、泛化声明
- **Issue Tracker 已同步**：新增 9 个 open issues（R51-N1~N5, R51-W1~W4）
- **视觉审查**：已完成，0 critical / 1 warning（Table 13 字号）/ 15 info
- **格式合规**：全部通过

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 395

## Round 395

2 recorded events


### User

_source line 4049 · 2026-05-24T23:11:11.460297+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 审稿意见的逐条回应，已提交给 Review Director。

总结：
- **3 个 Must-Fix**：N1（温度敏感性）和 N2（F1=0.694 实际意义）[AGREE]；N3（DDR 形式化断层）[REBUT]——DDR 作为解释性框架有 LOFO/ANOVA 支撑，但同意叙事需要更精准区分"解释"和"驱动"。
- **6 个 Should-Fix**：W1-W5 [AGREE]；W6（泛化声明过度）[REBUT]——在当前实验覆盖范围内 "empirical regularity" 可接受，但应加温度限定条件。
- 两位 Reviewer 共识焦点：gen-1/gen-2+ 区分能力有限、base-model-only 限制、温度条件需限定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 4050 · 2026-05-24T23:11:22.457793+00:00_

审稿报告已投递至 Research Director。

**Round 51 审稿完成**。两位 Reviewer 均给出 3.5（Borderline Conference），经交叉回应后关键问题高度收敛（12 AGREE / 2 partial REBUT），1 轮即达成共识。

**综合评分**：3.5 / 5 — Borderline Conference，建议 Findings 接收。

**核心发现**：
- 4 个 Must-Fix：温度敏感性主文讨论不足、F1=0.694 实际意义未论证、DDR 新颖性质疑（shape stability 可能 trivially predictable）、base-model-only 限制
- 5 个 Should-Fix：DDR 框架 framing 修正、entropy 术语、OOD detection 缺失、跨域规模、机制解释标注
- Issue Tracker 已同步（9 个 open issues: R51-N1~N5, R51-W1~W4）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---
