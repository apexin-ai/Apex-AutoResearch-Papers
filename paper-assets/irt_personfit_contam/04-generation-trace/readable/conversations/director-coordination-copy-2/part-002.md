# Director coordination — Part 2 of 3

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/25/25b67938722c16707e2e.json)

## Round 32

### User

_source line 272 · 2026-05-21T18:17:39.171138+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应：对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 问题

### [AGREE] R1-N1: IRT 假设违反的分析不充分，Δℓz* 有效性缺乏理论保证

同意这是一个重要问题。R1 指出的核心逻辑链是成立的：如果污染改变了 item 间的依赖结构（memorized items 的答对不再依赖 θ），则 clean 和 contaminated 条件下的 misfit 结构不再对称，Δℓz* 的差分假设（"shared model misfit cancels", Section 3.2 p3）失效。

我在自己的审稿中将此归入 W3（Δℓz* 假设未充分验证），但 R1 的分析更深入——特别是 Appendix A 模拟验证的循环论证问题（R²=0.957 在假设 IRT 成立的条件下得出）。我同意应升级为 critical。

补充一点：Section 3.2 说 "57 of 60 model-benchmark cells yield ℓz* > 1.96 even absent contamination"，这个数字本身说明 IRT misfit 问题严重。如果 95% 的 clean 模型都被 raw ℓz* flag，那么 Δℓz* 承担了极大的校正负担，其理论保证确实需要更严格的论证。

### [AGREE] R1-N2: 倒 U 型剂量反应削弱实用性主张

同意。我在自己的 N3 中从另一角度提出了类似问题：inverted-U 可从 IRT 天花板效应直接预测（St-Onge et al. 2011 在 bib 中讨论了 aberrance rate 对 person-fit accuracy 的影响）。R1 的补充角度——free-θ vs. fixed-θ 的定位矛盾——也是成立的。

Abstract 宣称 "operating at the minimal-information point: binary response patterns"，但 fixed-θ 实际需要 clean baseline 作为参照（Table 2, p6），这与 "minimal information" 定位矛盾。论文应在 Abstract/Introduction 中明确区分两种操作模式的信息需求。

不过，我对 R1 建议将 inverted-U "从 finding 提升为 fundamental limitation" 持保留意见——它同时是一个 finding（量化了 boundary condition）和一个 limitation，两种定位不冲突。建议保留为 finding 但在 Limitations 中更突出地讨论其实用影响。

### [AGREE] R1-N3: Post-RL 发现统计效力严重不足

完全同意，与我的 N2 一致。补充一个 R1 未提到的点：Figure 4 (p7) 显示 GRPO 训练后 ℓz* gap 在 step 500 后稳定，但论文没有报告稳定阶段的置信区间或 variance across seeds。即使 N=1 模型，如果有多个 GRPO seeds，至少可以给出 seed-level variance 估计。论文 Section 3.3 说 clean baseline 用了 n=10 seeds，但 GRPO 是否也跑了多个 seed 不清楚。

R1 建议 "增加至少 2-3 个 RL seeds" 是必要的最低要求。

### [AGREE] R1-N4: PSN-IRT 参数依赖缺乏敏感性分析

同意，这是我审稿时遗漏的重要问题。R1 提出的三个缺失分析都是合理的：

1. **参数精度/标准误**：Section 3.1 (p3) 仅说 "item parameters are pre-calibrated by PSN-IRT (Zhou et al., 2026) from a large-scale leaderboard dataset"，未给出任何参数质量指标。
2. **参数扰动敏感性**：如果 4PL 参数存在估计误差，ℓz* 的计算会受影响。论文用了 upper asymptote d（Section 3.1 提到 "externally calibrated four-parameter logistic (4PL) item parameters"），4PL 的 d 参数本身估计就不稳定（Barton & Lord, 1981 在 bib 中但未 cite）。
3. **校准样本污染**：R1 指出如果 leaderboard 包含已污染模型，PSN-IRT 参数可能有偏——这是一个尖锐且重要的 concern。

---

## Should-Fix 问题

### [AGREE] R1-W1: QLoRA SFT 作为唯一污染机制过于狭窄

同意，但我认为 R1 将此定为 warning 级别 **不够严格**。这是我审稿中的 N1 (critical)。理由：QLoRA fine-tuning（rank=16, α=32）仅修改低秩适配器，权重变化受限于低秩子空间。Pretraining contamination 影响整个参数空间。两种机制产生的 response pattern 可能有本质差异，直接影响所有 findings 的外推有效性。这不是一个"可以在 Limitations 中提一下"的问题，而是论文 scope 的根本限制。

### [AGREE] R1-W2: 仅两个污染水平不足以支撑剂量反应曲线结论

同意。三个数据点（0%, 15%, 50%）无法区分 inverted-U 和 monotonic decrease。Table 1 (p4) 显示 Qwen 从 |d|=6.56 (15%) 降到 |d|=1.90 (50%)，但没有 5%、10%、25%、35% 等中间点。如果在 5% 时 |d| 已经更高、在 10% 达到峰值然后下降，那是 inverted-U；如果 |d| 一直随污染增加而下降，那是 monotonic decrease with initial high sensitivity。两种解释对方法的实用意义完全不同。

Section 4.2 (p5) 称 "Qwen exhibits a striking inversion"，但两点下降不足以称为 "inversion"——需要看到先升后降的完整曲线。

### [AGREE] R1-W3: Item-level 污染检测接近随机

同意，与我的 W2 一致。Table 8 (p12) 的 ℓz* itemwise AUROC=0.53 基本等同于 random baseline 的 0.50。Section 5 (p7) 说 "ℓz* can be split by item subsets to yield per-item memorization fingerprints" 与这一实际表现存在矛盾。论文应在 main text 中坦诚报告这一负面结果。

### [AGREE] R1-W4: Detection-diagnosis tradeoff 论证需加强

同意。Table 3 (p6) 显示 accuracy z-score 的 |d| 比 ℓz* 大 20-70 倍。论文声称 ℓz* 的价值在于 diagnostic 能力，但没有给出一个具体的 use case 展示这种诊断信息如何改变实际决策。Discussion (p7) 提到 "the 4PL parameterization captures item-level coiling effects"，但 Table 8 的 item-level 结果（AUROC 0.53）恰恰说明这种 item-level 诊断能力很弱。

建议作者提供一个具体 case study：给定一个模型的 ℓz* 分解结果，展示诊断信息如何帮助识别"哪些 item 被记忆"或"污染是通过 SFT 还是 RL 发生的"。

### [AGREE] R1-W5: 57/60 vs 4/60 flagging rate 比较具有误导性

同意。Section 3.2 (p3) 报告 57/60 model-benchmark cells 在 clean 条件下就被 ℓz* flag（> 1.96），这说明 raw ℓz* 的 false positive rate 极高（95%）。论文将此作为 Δℓz* 设计的动机，但 R1 正确指出：如果 ℓz* 几乎对所有模型都 flag，它实际上不区分 contamination 和 general IRT misfit。

进一步地，4/60 的 clean Δℓz* flag rate 虽然远低于 57/60，但这是 **4/60 = 6.7%**，仍高于名义水平 5%（如果用 α=0.05 双侧检验）。论文没有讨论这个残余 false positive rate。

### [REBUT] R1-W6: 缺少与 ConStat、MIA、CoDec 的实证对比

部分不同意。论文定位为 **characterization paper**（Section 6, p8: "the first systematic characterization of IRT person-fit behavior for LLM benchmark contamination detection"），而非提出新的检测方法。要求 characterization paper 与检测方法做性能对比，存在评价标准错配。

ConStat 是 model-level performance-based detection，需要对比多个模型的分数分布；MIA/CoDec 需要 token-level probabilities（非 black-box）。本文的 ℓz* 在信息需求上（仅二值 response pattern）与它们根本不同。Table 3 (p6) 已在内部对比了 ℓz* 与 accuracy z-score 和 HT statistic 的 detection 效力，这对 characterization 目的是充分的。

但我同意，如果论文想声称 practical utility，至少应在 Discussion 中讨论与 ConStat 的互补性（而非竞争性）。当前 Discussion (p7-8) 在这方面确实不够。

---

## 对 R1 Questions 的补充意见

- **Q2 (Mistral n=6)**: 这是一个我遗漏的问题。Table 1 footnote 如果确认 Mistral 只有 n=6 seeds（而非 n=10），bootstrap CI 的可靠性会受影响，且与论文 Section 3.3 声称的 "n=10 clean seeds per family" 不一致。这需要在正文中解释原因。
- **Q5 (Item-level AUROC vs. fingerprint claim)**: 与 R1-W3 一致，这是论文 claim 与 evidence 之间最突出的矛盾。
- **Q6 (Post-RL ℓz* gap 是否只是残留 accuracy difference)**: 好问题。Figure 4 (p7) 显示 GRPO 后 accuracy gap 趋近于零但 ℓz* gap 保留。但如果 accuracy 差异虽小但非零（如 0.5-1% 差异），IRT person-fit 可能只是放大了这个微小差异，而非检测到 "response-pattern structure"。论文需要排除这一替代解释。

---

## 总结

R1 和我的独立审稿在核心判断上高度一致：Overall 3.0 (Findings)，主要问题集中在 (1) 生态效度/污染模拟方式、(2) post-RL under-validation、(3) findings 的新颖性/可预测性。R1 额外贡献了 PSN-IRT 参数敏感性和 IRT 假设违反的深入分析（N1, N4），这些补充了我的审稿视角。

**我认为 R1 最有价值的独特贡献是 N1**（IRT 假设违反分析）——这不仅是技术问题，更是方法论层面的根本性 concern。如果 contamination 改变了 item 依赖结构，整个 Δℓz* 框架的理论基础都需要重新审视。

两位 reviewer 唯一的分歧在 R1-W6（实证对比需求），我认为 characterization paper 不应被要求与检测方法做性能竞赛，但应讨论互补关系。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 273 · 2026-05-21T18:17:43.882494+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 33

## Round 33

2 recorded events


### User

_source line 274 · 2026-05-21T18:17:48.900660+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 4 个 Must-Fix 和 6 个 Should-Fix 逐条回应：

- **N1-N4**: 全部 [AGREE]。N1（IRT 假设违反）是 R1 最有价值的独特贡献，补充了我忽略的理论层面 concern。N4（PSN-IRT 参数敏感性）也是我遗漏的点。
- **W1-W5**: 全部 [AGREE]。其中 W1（QLoRA 作为唯一污染机制）我认为 R1 定级偏低，应从 warning 升至 critical（与我的 N1 一致）。W2（仅两个污染水平）的分析很到位——两点下降无法确定 inverted-U。
- **W6**: [REBUT]。Characterization paper 不应被要求与检测方法做性能对比，但应讨论互补关系。

两位 reviewer 在 Overall 3.0 (Findings) 和核心问题上高度一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 275 · 2026-05-21T18:17:53.657765+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 34

## Round 34

10 recorded events


### User

_source line 276 · 2026-05-21T18:18:10.728729+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: QLoRA fine-tuning 模拟污染的生态效度不足**

同意这是重要问题，但对严重程度的判断与 R2 略有不同。

我在自己的审稿中将其列为 W1（Should-Fix），R2 升级为 N1（Critical）。R2 的理由更充分：QLoRA 只修改低秩 adapter（Section 3.3: "rank=16, α=32"），而 pretraining contamination 的权重变化遍布整个网络。更重要的是 R2 提出的 psychometric 类比——QLoRA 污染类似 "item preknowledge"（答案记忆），而 pretraining 污染更接近 "over-exposure"（重复暴露导致的隐式学习）。这两种机制可能产生不同的 response pattern aberrance 结构，从而影响 ℓz* 的行为。

但我要补充一个缓和因素：论文标题明确使用了 "characterization" 而非 "detection method"，并且在 Section 4.5 的 post-RL 分析中提到 Wang et al. (2025) 的发现——"RL post-training renders MIA-based detectors no better than random"——说明作者意识到不同训练机制会改变检测行为。问题在于论文的四个 findings 被呈现为具有一定泛化性的 "boundary conditions"，但证据基础仅限于 QLoRA SFT。

**建议**：将 R2-N1 和我的 R1-W1 合并处理——作者应在 Section 3.3 明确讨论 QLoRA 作为 pretraining contamination proxy 的合理性和局限性，并将所有 findings 的适用范围限定为 "SFT-based contamination"。

---

**[AGREE] R2-N2: Post-RL finding N=1 严重 under-validated**

完全同意，与我的 R1-N3 一致。

R2 准确指出了核心矛盾：Section 4.5 末尾承认 "We report this as a preliminary characterization"，但 Abstract 将其列为四大 findings 之一且未标注 preliminary。从论文中可直接验证：Abstract 第四个 contribution——"a post-RL residual pattern where GRPO erases the accuracy gap but ℓz* response-pattern gap persists"——与正文的 hedging 不一致。

Figure 4 展示的 GRPO 轨迹仅有一条线，无误差带或置信区间。Section 4.5 的关键数字（"accuracy gap from 11.4pp → 2.1pp", "ℓz* gap remains ≈3.3"）均来自单次实验。N=1 不构成任何 "pattern"。

我与 R2 的唯一分歧是修改建议的力度：R2 可能接受将其降级为 preliminary observation；我认为如果不增加重复实验，应从 Abstract 中完全移除这个 claim，仅在正文中作为 case study 保留。

---

**[REBUT] R2-N3: 核心 findings 可从 IRT 理论直接推导，新颖性被高估**

部分反驳。R2 的批评有理论依据但 overstated——将 "empirical characterization in a new domain" 等同于 "direct derivation from theory" 是不准确的。

逐项分析：

**(a) Inverted-U dose-response (Section 4.2)**：R2 称这是 "IRT 的天花板效应，person-fit 文献中已知"。这只部分正确。经典 IRT ceiling effect 指的是测试在高能力端信息量不足（Lord, 1980）。论文中的倒 U 型来自一个更 specific 的机制：free-θ MLE 重估将污染导致的 accuracy inflation 吸收为 θ̂ 增量，使得原本异常的 response pattern 在新 θ̂ 下变得 "expected"（Section 4.2-4.3 的 θ-shift absorption 分析）。虽然 Sinharay (2017) 讨论了 compromised item 比例对 person-fit detection 的影响，但 **具体的 θ-shift absorption 机制及其与 benchmark size 的交互**（MMLU 14K items 出现倒 U 而 ARC-C 295 items 则单调递增）是新的 empirical finding，无法从已有文献直接推导。Table 1 和 Figure 2 的对比清楚展示了这一 benchmark-dependent pattern。

**(b) θ-shift dynamics (Section 4.3)**：R2 引用 Meijer & Sijtsma (2001) 认为 ability-person fit interaction 是经典议题。同意一般原理是已知的。但 Figure 3 展示的 **baseline accuracy 与 |d| 的负相关关系**（高能力模型 θ-shift headroom 小 → 检测灵敏度低），以及 **ARC-C 上的反转**（高能力模型 ℓz* 变正值 → Figure 3 描述的 sign flip），提供了超越经典理论的量化边界条件。这些量化结果对于判断 IRT person-fit 在具体 LLM 评估场景中是否可用，有直接实践价值。

**(c) Detection-diagnosis tradeoff (Section 4.4)**：R2 称为 "power vs. specificity 基本 tradeoff"。过于简化。论文的贡献不在于发现 tradeoff 存在，而在于 **量化其幅度**（Table 3: accuracy |d|=42-68 vs ℓz* |d|=0.58-1.90，差距 20-70 倍）以及识别 ℓz* 的三个 specific diagnostic capabilities（scoremeness decomposition, θ-shift mechanism, response-pattern sensitivity）。量化信息对于 practitioners 选择方法有实用价值。

**但 R2 的批评也有合理之处**：论文确实未充分 acknowledge prior IRT theory，这使得 findings 显得比实际更 novel。例如，Section 4.2 对倒 U 型的讨论未引用 St-Onge et al. (2011) 或 Sinharay (2017) 中关于 aberrance rate 影响的相关结论（两篇都在 .bib 中但未 cite）。这是写作问题而非方法论缺陷——the findings are legitimate empirical contributions, but their novelty should be framed as "domain-specific characterization" rather than "new discovery"。

**总结**：R2-N3 应从 critical 降级为 should-fix。论文标题已使用 "characterization" 自我定位，但正文和 abstract 的措辞确实倾向于将已知现象的领域适配呈现为新发现。修改建议：(a) 在 Section 4.2-4.4 中增加对 prior IRT person-fit literature 的引用和讨论；(b) 明确区分 "new empirical finding"（如 benchmark size × model ability 的交互效应、量化 tradeoff 幅度）与 "known theoretical prediction verified in new domain"。

---

### Should-Fix 问题

**[AGREE] R2-W1: 模型覆盖范围过窄**

同意。Section 4.3 的 θ-shift dynamics 声称发现 baseline accuracy 与检测灵敏度的系统性关系（Figure 3），但仅基于 3 个 7-8B 模型的数据点。3 个点不足以建立 "negative correlation" 的结论——这可能是巧合。缺少更大规模模型（13B/70B）和不同架构（MoE）的验证。

补充我的相关观察：Table 1 中 Mistral 的 CI 宽度明显大于其他模型（如 MMLU 15%: Mistral [1.5, 7.4] vs Qwen 和 Llama），但论文未解释原因。如果是因为 Mistral 使用了不同数量的 seeds（<10），应在 Section 3.3 中明确标注。

---

**[AGREE] R2-W2: Item-level detection 接近随机 (Table 8)**

完全同意，与我的 R1-W3 一致。ℓz* itemwise AUROC=0.53 说明该方法对 "哪些具体 item 被污染" 的识别能力接近随机猜测。Section 5 中 "ℓz* can be split by item subsets to yield per-item memorization fingerprints" 的说法与 Table 8 的实际数据不匹配。

---

**[AGREE] R2-W3: Δℓz* 差分设计的假设未充分验证**

同意，并且我认为这个问题比 R2 的 "warning" 定级更严重——我在自己的审稿中将其列为 N1（Critical）。

R2 正确指出了部署场景的不清晰性：Δℓz* 需要 clean baseline（ℓz*_clean），但现实中往往没有 clean baseline。论文在 Section 4 中使用的是受控实验条件下的 Δℓz*，Section 3.2 提到 cross-benchmark comparison 作为替代方案（"For deployment without clean baselines, cross-benchmark comparison provides the reference"），但未详细说明这在实践中如何操作。

我要补充 R2 未提及的一个更深层问题：Δℓz* 差分设计的有效性前提是 clean 和 contaminated conditions 下的 model misfit **加性且等量**。如果污染改变了 item 间的依赖结构（memorized items 独立于 θ，non-memorized items 保持原有依赖），则 misfit 不再等量可消，Δℓz* 不是有效的差分估计量。这个问题在 R2-W3 和我的 R1-N1 中从不同角度被提出，合在一起构成对方法论基础的重大质疑。

---

**[AGREE] R2-W4: Figure 2 heatmap 可读性差**

同意。灰色 cells 确实未在 caption 中解释（实际是 Llama 和 Mistral 在 ARC-C 上的缺失条件）。Cohen's d 值跨度从 1.08 到 15.3，线性色彩映射导致中间值（如 2-4 range）难以区分。建议使用对数映射或分段色彩映射。

---

### 综合评价

R2 和我的审稿在多数问题上高度一致：Post-RL N=1 under-validation（R2-N2 ↔ R1-N3）、QLoRA 生态效度（R2-N1 ↔ R1-W1）、item-level detection 无效（R2-W2 ↔ R1-W3）、Δℓz* 假设问题（R2-W3 ↔ R1-N1）。

主要分歧在 **R2-N3**：R2 认为 findings 缺乏新颖性（critical），我认为 empirical characterization in a new domain 有独立价值，应为 should-fix（加强对 prior literature 的引用和定位）而非 critical rejection reason。

两份审稿的交集确认了本文的核心弱点：方法论基础（IRT 假设违反 + PSN-IRT 依赖）和实验范围（单一污染机制 + post-RL N=1）均需显著加强才能达到 main conference 水平。当前证据支持 Findings 接收（Overall 3.0）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 277 · 2026-05-21T18:18:30.463979+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 278 · 2026-05-21T18:18:30.715285+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T18:04:25.864073+00:00\", \"completed_at\": \"2026-05-21T18:06:37.624727+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 12\", \"message\": \"Appendix 最后一页仅有 Table 8（4行×2列小表）占约 15% 面积，其余 ~85% 为空白。建议将 Table 8 合并到 page 11 或重新组织 appendix 布局消除整页空白\"}, {\"severity\": \"warning\", \"dimension\": \"page 4\", \"message\": \"Table 1 主结果表未对最优值加粗标注；Table 2 (p6)、Table 3 (p7) 同样缺少最优值加粗。审稿人快速扫描时难以定位关键数字\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"正文最后一页（p8）为纯文本（Discussion+Limitations+Conclusion+Refs 开头），无 display item。作为结尾页可接受，但如果 Conclusion 前能放一个 summary figure/table 会增强收尾印象\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 子图内坐标轴标签和 legend 字号偏小（约正文 60%），150dpi 下勉强可读，建议放大至正文 70%+ 以提升清晰度\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 热力图中 cell 内数字（|d| 值和 CI）字号较小，密集排列，建议适当增大字号或简化 CI 显示\"}, {\"severity\": \"info\", \"dimension\": \"page 11\", \"message\": \"Tables 4-7 密集堆叠于同一页，表间距略紧；可考虑微调间距或将 Table 8 上移至此页底部（同时解决 p12 空白问题）\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（ACL 模板限制，非硬伤），Abstract 较长占满左栏大部分\"}], \"counts\": {\"critical\": 1, \"warning\": 2, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 279 · 2026-05-21T18:18:30.715686+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 280 · 2026-05-21T18:18:30.766115+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 281 · 2026-05-21T18:22:35.330709+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_personfit_contam",
  "issues_yaml": "## Review Issue Tracker — Round 2 (fresh review, 2026-05-21)\n\n# ===== CRITICAL ISSUES =====\n\n- id: \"R2-N1\"\n  summary: \"IRT 假设违反分析不充分，Δℓz* 有效性缺乏理论保证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-N1 提出，R2 交叉 AGREE 并升级。污染可能改变 item 间依赖结构（memorized items 独立于 θ），导致 clean/contaminated 的 misfit 不对称，Δℓz* 差分假设失效。Appendix A 模拟 R²=0.957 假设 IRT 成立，构成循环论证。57/60 clean cells flagged 说明 IRT misfit 极严重，Δℓz* 承担极大校正负担。\"\n  action_items:\n    - round: 2\n      action: \"(a) 模拟分析引入 local dependence 变化后 Δℓz* 偏差；(b) 检验 clean/contaminated 项目残差相关矩阵差异；(c) 讨论 Snijders 校正在假设违反下的鲁棒性\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"生态效度不足——QLoRA SFT 模拟污染 ≠ pretraining 污染\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-N1 提出，R1 交叉 AGREE。QLoRA (rank=16) 仅修改低秩 adapter，权重变化受限于低秩子空间，与 pretraining contamination 本质不同。Fine-tuning ≈ item preknowledge vs pretraining ≈ over-exposure，可能产生不同 aberrance pattern。所有四个 findings 的外推有效性存疑。\"\n  action_items:\n    - round: 2\n      action: \"(a) 在 Section 3.3 讨论 QLoRA 作为 pretraining proxy 的合理性和局限；(b) 将 findings 适用范围限定为 SFT-based contamination；(c) 或使用已知被污染的真实模型验证\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N3\"\n  summary: \"Post-RL finding (N=1) 统计效力严重不足，Abstract overclaim\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-N3 和 R2-N2 独立提出，交叉完全一致。N=1 (Qwen, 15% MMLU, GRPO only)，Figure 4 无误差条。Abstract 列为四大 findings 之一却未标注 preliminary，与正文 hedging 不一致。R1 建议从 Abstract 移除或降级为 case study。\"\n  action_items:\n    - round: 2\n      action: \"(a) Abstract/Intro 降级为 preliminary observation；(b) 增加 2-3 个 RL seeds 或跨模型重复；(c) 无法增加实验则标注 N=1 no statistical inference\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N4\"\n  summary: \"PSN-IRT 参数依赖缺乏敏感性分析——single point of failure\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-N4 提出，R2 交叉 AGREE（标注为自己遗漏的重要问题）。缺少：(a) PSN-IRT 参数精度/标准误；(b) 参数扰动敏感性分析；(c) 校准样本污染影响讨论。4PL upper asymptote d 参数估计本身不稳定。\"\n  action_items:\n    - round: 2\n      action: \"(a) 参数扰动实验（5-10% 噪声）测 Δℓz* 稳健性；(b) 讨论 leaderboard 校准样本中已有污染模型的影响\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N5\"\n  summary: \"倒 U 型剂量反应削弱 minimal-information 实用性主张\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-N2 提出，R2 AGREE。free-θ 下 Qwen |d| 从 6.58 (15%) 降到 1.90 (50%)——污染越重检测越弱。fixed-θ 需 clean baseline，与 Abstract 'minimal information point' 定位矛盾。R2 补充：inverted-U 可从 IRT 天花板效应预测（St-Onge et al. 2011）。R2 认为可同时作为 finding 和 limitation。\"\n  action_items:\n    - round: 2\n      action: \"(a) Abstract/Intro 区分 free-θ 和 fixed-θ 信息需求；(b) Limitations 突出讨论实用影响；(c) 增加中间污染水平验证曲线形状\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== DIVERGENCE (Reviewers disagree) =====\n\n- id: \"R2-D1\"\n  summary: \"Findings 新颖性定级分歧——IRT 理论可预测 vs empirical characterization 有独立价值\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-N3 认为 3/4 findings 可从 IRT 理论直接推导（inverted-U=天花板效应, θ-shift=经典议题, tradeoff=power vs specificity），novelty 被高估 → critical。R1 REBUT：empirical characterization in new domain 有独立价值，具体量化（|d| 幅度、benchmark size 交互、4PL vs 3PL +27pp power）超越理论预测 → should-fix。双方同意写作应更好 acknowledge prior IRT literature。\"\n  action_items:\n    - round: 2\n      action: \"在 Section 4.2-4.4 增加对 prior IRT person-fit literature 的引用；明确区分 new empirical finding vs known theoretical prediction verified in new domain\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-D2\"\n  summary: \"是否需要与 ConStat/MIA/CoDec 实证对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-W6 要求实证对比（至少 ConStat 同为 performance-based）。R2 REBUT：characterization paper 不应被要求性能竞赛，但应讨论互补关系。\"\n  action_items:\n    - round: 2\n      action: \"在 Discussion 中讨论与 ConStat 的互补性（而非竞争性），或提供理论比较说明实证对比不可行的原因\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== WARNING ISSUES =====\n\n- id: \"R2-W1\"\n  summary: \"模型覆盖范围过窄——仅 3 个 7-8B 模型，θ-shift dynamics 仅 3 数据点\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"缺少 13B/70B、MoE 架构、base vs instruction-tuned 对比。Section 4.3 Figure 3 的 negative correlation 基于 3 点不足以建立系统性关系。\"\n  action_items:\n    - round: 2\n      action: \"增加 1-2 个不同规模/架构模型，或在 Limitations 中明确承认 generalization 未验证\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"仅两个污染水平 (15%, 50%) 不足以支撑 inverted-U 曲线结论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"三个数据点（0%, 15%, 50%）无法区分 inverted-U 和 monotonic decrease。缺少 5%, 10%, 25% 等中间点。R2 交叉同意 R1 分析——两点下降不足以称 inversion。\"\n  action_items:\n    - round: 2\n      action: \"增加中间污染水平（至少 25%），或将 inverted-U 改为 non-monotonic decline\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Item-level detection 接近随机 (AUROC 0.53)，与 fingerprint claim 矛盾\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Table 8 ℓz* itemwise AUROC=0.53 ≈ random。Section 5 声称 per-item memorization fingerprints 与此不一致。应在 main text 坦诚报告负面结果。\"\n  action_items:\n    - round: 2\n      action: \"修改 Section 5 中 item-level diagnostic 表述，使之与 Table 8 一致\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Detection-diagnosis tradeoff 论证不足——缺少具体 use case\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"accuracy |d|≈42-68 vs ℓz* |d|≈0.58-1.90，差距 20-70 倍。论文未展示诊断信息如何改变实际决策。需要具体 case study。\"\n  action_items:\n    - round: 2\n      action: \"提供具体 use case：给定 ℓz* 分解结果，展示诊断信息如何辅助决策\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"57/60 vs 4/60 flagging rate 比较具有误导性\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"57/60 flagging 反映 IRT misfit 普遍性而非检测能力，将 high FPR 作为优势呈现与 Δℓz* 动机矛盾。R2 补充：4/60 clean Δℓz* FPR=6.7% 仍高于 α=0.05。\"\n  action_items:\n    - round: 2\n      action: \"重新表述：57/60 是 IRT 假设违反的普遍性证据（也是 Δℓz* 设计的动机），而非检测能力优势\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"Mistral n=6 seeds 与 Section 3.3 n=10 声称不一致\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Table 1 footnote 标注 Mistral n=6，但 Section 3.3 声称 n=10 per family。CI 宽度差异也反映这一不一致。应在正文中解释原因。\"\n  action_items:\n    - round: 2\n      action: \"在 Section 3.3 明确标注 Mistral n=6 及原因\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W7\"\n  summary: \"缺少代码/数据可用性声明和 reproducibility statement\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1]\n      note: \"ARR 建议提供 reproducibility statement。PSN-IRT 参数可获取性未说明。Bootstrap CI 方法（bias-corrected? percentile?）未说明。\"\n  action_items:\n    - round: 2\n      action: \"添加 reproducibility statement；说明 PSN-IRT 参数获取方式；补充 bootstrap 实现细节\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W8\"\n  summary: \"Orphan bibliography entries (28/59) + 缺少对 bib 中已有但未 cite 的相关文献引用\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Tendeiro & Meijer (2014) 和 St-Onge et al. (2011) 在 bib 中但未 cite，均与核心 findings 直接相关。31 篇实际引用处于顶会下限。\"\n  action_items:\n    - round: 2\n      action: \"引用 Tendeiro & Meijer (2014)、St-Onge et al. (2011)；清理 orphan entries；考虑增加 Magis et al. (2012), Sinharay (2016), Li et al. (2024)\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== PRIOR ROUND ISSUES — STATUS CHECK =====\n# Round 1 issues: This is a fresh review (session reset). Round 1 issues listed below\n# are carried forward for cross-round tracking. Issues that appear resolved based on\n# current paper content are annotated; issues that recur are linked to new Round 2 IDs.\n\n- id: \"ACTUAL-C-W1\"\n  summary: \"HT ≈ lz* — 4PL framework necessity questioned (degradation chain)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"HT matches lz* in detection; degradation chain 4PL→HT→z-score.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Paper now frames as detection-diagnosis tradeoff (Section 4.4). R1 accepts framing; R2 questions novelty. Partially addressed but tradeoff argumentation needs strengthening → linked to R2-W4.\"\n  resolution: \"Partially resolved — reframed as tradeoff, but argumentation incomplete\"\n  resolution_round: null\n\n- id: \"ACTUAL-B-W1\"\n  summary: \"n=3 seeds statistically insufficient\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Must expand to n=10.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Qwen and Llama now n=10. Mistral n=6 (not 10). Partially resolved → linked to R2-W6.\"\n  resolution: \"Mostly resolved — Mistral n=6 still short\"\n  resolution_round: null\n\n- id: \"BEST-W1\"\n  summary: \"0 figures, presentation unacceptable\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Need 3-4 figures, ≥25 references, independent Related Work section.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Paper now has 4 figures, independent Related Work section, 31 citations. Resolved.\"\n  resolution: \"Resolved — figures, Related Work, citations all added\"\n  resolution_round: 2\n\n- id: \"V6-W4\"\n  summary: \"Post-RL failure limits practical scope\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"GRPO result pending.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"GRPO result now in paper (Section 4.5): accuracy gap erased but ℓz* gap persists. However N=1 → linked to R2-N3.\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"V6-THETA-SPECIFICITY\"\n  summary: \"θ-shift model specificity must be main finding\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Must be Results subsection with dedicated figure.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Now Section 4.3 with Figure 3 (θ scatter plot). Resolved.\"\n  resolution: \"Resolved — Section 4.3 + Figure 3 added\"\n  resolution_round: 2\n\n- id: \"ALL-W3\"\n  summary: \"4PL parameter source unclear\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Must clarify PSN-IRT origin.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Section 3.1 now clearly attributes to PSN-IRT (Zhuo et al., 2026). Resolved. But new concern: sensitivity analysis lacking → R2-N4.\"\n  resolution: \"Resolved — PSN-IRT attribution clear\"\n  resolution_round: 2\n\n- id: \"ALL-W1\"\n  summary: \"Systematic positive bias / IRT model misfit for LLMs\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Δlz* as DiD + bootstrap null.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Δℓz* design now in Section 3.2. But R1-N1 raises deeper concern: DiD validity not theoretically guaranteed → linked to R2-N1.\"\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_personfit_contam",
    "issues_yaml": "## Review Issue Tracker — Round 2 (fresh review, 2026-05-21)\n\n# ===== CRITICAL ISSUES =====\n\n- id: \"R2-N1\"\n  summary: \"IRT 假设违反分析不充分，Δℓz* 有效性缺乏理论保证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-N1 提出，R2 交叉 AGREE 并升级。污染可能改变 item 间依赖结构（memorized items 独立于 θ），导致 clean/contaminated 的 misfit 不对称，Δℓz* 差分假设失效。Appendix A 模拟 R²=0.957 假设 IRT 成立，构成循环论证。57/60 clean cells flagged 说明 IRT misfit 极严重，Δℓz* 承担极大校正负担。\"\n  action_items:\n    - round: 2\n      action: \"(a) 模拟分析引入 local dependence 变化后 Δℓz* 偏差；(b) 检验 clean/contaminated 项目残差相关矩阵差异；(c) 讨论 Snijders 校正在假设违反下的鲁棒性\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"生态效度不足——QLoRA SFT 模拟污染 ≠ pretraining 污染\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-N1 提出，R1 交叉 AGREE。QLoRA (rank=16) 仅修改低秩 adapter，权重变化受限于低秩子空间，与 pretraining contamination 本质不同。Fine-tuning ≈ item preknowledge vs pretraining ≈ over-exposure，可能产生不同 aberrance pattern。所有四个 findings 的外推有效性存疑。\"\n  action_items:\n    - round: 2\n      action: \"(a) 在 Section 3.3 讨论 QLoRA 作为 pretraining proxy 的合理性和局限；(b) 将 findings 适用范围限定为 SFT-based contamination；(c) 或使用已知被污染的真实模型验证\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N3\"\n  summary: \"Post-RL finding (N=1) 统计效力严重不足，Abstract overclaim\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-N3 和 R2-N2 独立提出，交叉完全一致。N=1 (Qwen, 15% MMLU, GRPO only)，Figure 4 无误差条。Abstract 列为四大 findings 之一却未标注 preliminary，与正文 hedging 不一致。R1 建议从 Abstract 移除或降级为 case study。\"\n  action_items:\n    - round: 2\n      action: \"(a) Abstract/Intro 降级为 preliminary observation；(b) 增加 2-3 个 RL seeds 或跨模型重复；(c) 无法增加实验则标注 N=1 no statistical inference\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N4\"\n  summary: \"PSN-IRT 参数依赖缺乏敏感性分析——single point of failure\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-N4 提出，R2 交叉 AGREE（标注为自己遗漏的重要问题）。缺少：(a) PSN-IRT 参数精度/标准误；(b) 参数扰动敏感性分析；(c) 校准样本污染影响讨论。4PL upper asymptote d 参数估计本身不稳定。\"\n  action_items:\n    - round: 2\n      action: \"(a) 参数扰动实验（5-10% 噪声）测 Δℓz* 稳健性；(b) 讨论 leaderboard 校准样本中已有污染模型的影响\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N5\"\n  summary: \"倒 U 型剂量反应削弱 minimal-information 实用性主张\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-N2 提出，R2 AGREE。free-θ 下 Qwen |d| 从 6.58 (15%) 降到 1.90 (50%)——污染越重检测越弱。fixed-θ 需 clean baseline，与 Abstract 'minimal information point' 定位矛盾。R2 补充：inverted-U 可从 IRT 天花板效应预测（St-Onge et al. 2011）。R2 认为可同时作为 finding 和 limitation。\"\n  action_items:\n    - round: 2\n      action: \"(a) Abstract/Intro 区分 free-θ 和 fixed-θ 信息需求；(b) Limitations 突出讨论实用影响；(c) 增加中间污染水平验证曲线形状\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== DIVERGENCE (Reviewers disagree) =====\n\n- id: \"R2-D1\"\n  summary: \"Findings 新颖性定级分歧——IRT 理论可预测 vs empirical characterization 有独立价值\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-N3 认为 3/4 findings 可从 IRT 理论直接推导（inverted-U=天花板效应, θ-shift=经典议题, tradeoff=power vs specificity），novelty 被高估 → critical。R1 REBUT：empirical characterization in new domain 有独立价值，具体量化（|d| 幅度、benchmark size 交互、4PL vs 3PL +27pp power）超越理论预测 → should-fix。双方同意写作应更好 acknowledge prior IRT literature。\"\n  action_items:\n    - round: 2\n      action: \"在 Section 4.2-4.4 增加对 prior IRT person-fit literature 的引用；明确区分 new empirical finding vs known theoretical prediction verified in new domain\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-D2\"\n  summary: \"是否需要与 ConStat/MIA/CoDec 实证对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-W6 要求实证对比（至少 ConStat 同为 performance-based）。R2 REBUT：characterization paper 不应被要求性能竞赛，但应讨论互补关系。\"\n  action_items:\n    - round: 2\n      action: \"在 Discussion 中讨论与 ConStat 的互补性（而非竞争性），或提供理论比较说明实证对比不可行的原因\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== WARNING ISSUES =====\n\n- id: \"R2-W1\"\n  summary: \"模型覆盖范围过窄——仅 3 个 7-8B 模型，θ-shift dynamics 仅 3 数据点\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"缺少 13B/70B、MoE 架构、base vs instruction-tuned 对比。Section 4.3 Figure 3 的 negative correlation 基于 3 点不足以建立系统性关系。\"\n  action_items:\n    - round: 2\n      action: \"增加 1-2 个不同规模/架构模型，或在 Limitations 中明确承认 generalization 未验证\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"仅两个污染水平 (15%, 50%) 不足以支撑 inverted-U 曲线结论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"三个数据点（0%, 15%, 50%）无法区分 inverted-U 和 monotonic decrease。缺少 5%, 10%, 25% 等中间点。R2 交叉同意 R1 分析——两点下降不足以称 inversion。\"\n  action_items:\n    - round: 2\n      action: \"增加中间污染水平（至少 25%），或将 inverted-U 改为 non-monotonic decline\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Item-level detection 接近随机 (AUROC 0.53)，与 fingerprint claim 矛盾\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Table 8 ℓz* itemwise AUROC=0.53 ≈ random。Section 5 声称 per-item memorization fingerprints 与此不一致。应在 main text 坦诚报告负面结果。\"\n  action_items:\n    - round: 2\n      action: \"修改 Section 5 中 item-level diagnostic 表述，使之与 Table 8 一致\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Detection-diagnosis tradeoff 论证不足——缺少具体 use case\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"accuracy |d|≈42-68 vs ℓz* |d|≈0.58-1.90，差距 20-70 倍。论文未展示诊断信息如何改变实际决策。需要具体 case study。\"\n  action_items:\n    - round: 2\n      action: \"提供具体 use case：给定 ℓz* 分解结果，展示诊断信息如何辅助决策\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"57/60 vs 4/60 flagging rate 比较具有误导性\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"57/60 flagging 反映 IRT misfit 普遍性而非检测能力，将 high FPR 作为优势呈现与 Δℓz* 动机矛盾。R2 补充：4/60 clean Δℓz* FPR=6.7% 仍高于 α=0.05。\"\n  action_items:\n    - round: 2\n      action: \"重新表述：57/60 是 IRT 假设违反的普遍性证据（也是 Δℓz* 设计的动机），而非检测能力优势\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"Mistral n=6 seeds 与 Section 3.3 n=10 声称不一致\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Table 1 footnote 标注 Mistral n=6，但 Section 3.3 声称 n=10 per family。CI 宽度差异也反映这一不一致。应在正文中解释原因。\"\n  action_items:\n    - round: 2\n      action: \"在 Section 3.3 明确标注 Mistral n=6 及原因\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W7\"\n  summary: \"缺少代码/数据可用性声明和 reproducibility statement\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1]\n      note: \"ARR 建议提供 reproducibility statement。PSN-IRT 参数可获取性未说明。Bootstrap CI 方法（bias-corrected? percentile?）未说明。\"\n  action_items:\n    - round: 2\n      action: \"添加 reproducibility statement；说明 PSN-IRT 参数获取方式；补充 bootstrap 实现细节\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W8\"\n  summary: \"Orphan bibliography entries (28/59) + 缺少对 bib 中已有但未 cite 的相关文献引用\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Tendeiro & Meijer (2014) 和 St-Onge et al. (2011) 在 bib 中但未 cite，均与核心 findings 直接相关。31 篇实际引用处于顶会下限。\"\n  action_items:\n    - round: 2\n      action: \"引用 Tendeiro & Meijer (2014)、St-Onge et al. (2011)；清理 orphan entries；考虑增加 Magis et al. (2012), Sinharay (2016), Li et al. (2024)\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== PRIOR ROUND ISSUES — STATUS CHECK =====\n# Round 1 issues: This is a fresh review (session reset). Round 1 issues listed below\n# are carried forward for cross-round tracking. Issues that appear resolved based on\n# current paper content are annotated; issues that recur are linked to new Round 2 IDs.\n\n- id: \"ACTUAL-C-W1\"\n  summary: \"HT ≈ lz* — 4PL framework necessity questioned (degradation chain)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"HT matches lz* in detection; degradation chain 4PL→HT→z-score.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Paper now frames as detection-diagnosis tradeoff (Section 4.4). R1 accepts framing; R2 questions novelty. Partially addressed but tradeoff argumentation needs strengthening → linked to R2-W4.\"\n  resolution: \"Partially resolved — reframed as tradeoff, but argumentation incomplete\"\n  resolution_round: null\n\n- id: \"ACTUAL-B-W1\"\n  summary: \"n=3 seeds statistically insufficient\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Must expand to n=10.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Qwen and Llama now n=10. Mistral n=6 (not 10). Partially resolved → linked to R2-W6.\"\n  resolution: \"Mostly resolved — Mistral n=6 still short\"\n  resolution_round: null\n\n- id: \"BEST-W1\"\n  summary: \"0 figures, presentation unacceptable\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Need 3-4 figures, ≥25 references, independent Related Work section.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Paper now has 4 figures, independent Related Work section, 31 citations. Resolved.\"\n  resolution: \"Resolved — figures, Related Work, citations all added\"\n  resolution_round: 2\n\n- id: \"V6-W4\"\n  summary: \"Post-RL failure limits practical scope\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"GRPO result pending.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"GRPO result now in paper (Section 4.5): accuracy gap erased but ℓz* gap persists. However N=1 → linked to R2-N3.\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"V6-THETA-SPECIFICITY\"\n  summary: \"θ-shift model specificity must be main finding\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Must be Results subsection with dedicated figure.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Now Section 4.3 with Figure 3 (θ scatter plot). Resolved.\"\n  resolution: \"Resolved — Section 4.3 + Figure 3 added\"\n  resolution_round: 2\n\n- id: \"ALL-W3\"\n  summary: \"4PL parameter source unclear\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Must clarify PSN-IRT origin.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Section 3.1 now clearly attributes to PSN-IRT (Zhuo et al., 2026). Resolved. But new concern: sensitivity analysis lacking → R2-N4.\"\n  resolution: \"Resolved — PSN-IRT attribution clear\"\n  resolution_round: 2\n\n- id: \"ALL-W1\"\n  summary: \"Systematic positive bias / IRT model misfit for LLMs\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Δlz* as DiD + bootstrap null.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Δℓz* design now in Section 3.2. But R1-N1 raises deeper concern: DiD validity not theoretically guaranteed → linked to R2-N1.\"\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 282 · 2026-05-21T18:22:35.431708+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml\", \"bytes\": 13286}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 283 · 2026-05-21T18:25:11.559634+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "irt_personfit_contam",
  "report": "# 审稿报告：IRT Person-Fit for LLM Benchmark Contamination Detection\n\n**项目**: irt_personfit_contam\n**目标 Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿轮次**: Round 2 (fresh)\n**审稿日期**: 2026-05-21\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作格式）\n\n---\n\n## Summary\n\n本文首次系统地将 IRT person-fit 统计量（ℓz*）应用于 LLM benchmark contamination 检测，操作在 minimal-information point（仅需二值 response pattern + 外部校准的 4PL 参数）。通过在三个 7-8B 模型家族（Qwen, Llama, Mistral; n=10 seeds）上的受控实验（QLoRA SFT, 15%/50% 污染）和 MMLU + ARC-Challenge 两个 benchmark，论文识别了四个边界条件：(1) free-θ 下的 inverted-U dose-response，(2) 模型特异性 θ-shift dynamics，(3) detection-diagnosis tradeoff，(4) post-RL residual pattern (N=1)。\n\n---\n\n## Strengths\n\n**S1. 跨学科新颖性** [R1, R2 共识]\n将教育测量学中有 40 年积累的 person-fit 统计量迁移到 LLM contamination 检测，这一视角是 genuinely novel 的。基于\"响应模式异常\"而非\"信息泄露痕迹\"，与现有 MIA/n-gram/probing 方法在理论层面有根本性区别。\n\n**S2. Δℓz* 差分设计务实合理** [R1, R2 共识]\n认识到 LLM 系统性违反 IRT 假设（57/60 cells flagged even absent contamination），提出差分设计消除共享 misfit，是方法论上合理的处理。\n\n**S3. 受控实验设计规范** [R1, R2 共识]\nn=10 seeds × 3 model families × 2 benchmarks × 3 conditions，bootstrap 95% CI（10,000 resamples）提供了统计推断基础。Table 1 所有 CI 不包含零。Cohen's d 作为 effect-size 指标选择恰当。\n\n**S4. θ-shift 机制分析有理论深度** [R1]\n揭示 baseline accuracy 与检测灵敏度的负相关（MMLU 上 Mistral 52.4% → |d|=3.50 > Qwen 67.8% → |d|=1.90），以及 ARC-C 上因天花板效应导致的 sign flip，提供了可解释的机制理解。\n\n**S5. 坦诚的自我定位** [R1, R2 共识]\n以\"characterization\"而非\"detection method\"自居，Discussion 和 Limitations 坦诚讨论了主要局限。Detection-diagnosis tradeoff 的诚实报告（accuracy |d|=42-68 vs ℓz* |d|=0.58-1.90）值得肯定。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1. [Critical] IRT 假设违反分析不充分，Δℓz* 有效性缺乏理论保证** [R1-N1, R2 AGREE]\n\nSection 3.2 承认 LLM 系统性违反 IRT 局部独立性和单维性假设。Δℓz* 差分设计仅在 clean/contaminated conditions 下 misfit 为加性且等量时有效。但论文未分析关键问题：**污染是否改变了 item 间依赖结构？** 如果 memorized items 的答对独立于 θ（纯靠记忆），contaminated condition 下的 misfit 结构与 clean condition 不同，Δℓz* 不再是有效差分估计量。Appendix A 模拟验证（R²=0.957）假设 IRT 模型成立，构成循环论证。57/60 clean cells 被 flag 说明 IRT misfit 极严重，Δℓz* 承担极大校正负担但其理论保证缺失。\n\n**MF-2. [Critical] 生态效度不足——QLoRA SFT ≠ pretraining 污染** [R2-N1, R1 AGREE]\n\nQLoRA (rank=16, α=32) 仅修改低秩 adapter，权重变化受限于低秩子空间，与 pretraining contamination（全参数分布式梯度更新）本质不同。Fine-tuning 污染接近\"item preknowledge\"（教育测试中的作弊），pretraining 污染更接近\"over-exposure\"（重复暴露的隐式学习），两种机制可能产生不同的 aberrance pattern。所有四个 findings 的外推有效性存疑，核心贡献范围被 SFT-specific 所限制。\n\n**MF-3. [Critical] Post-RL finding (N=1) 统计效力严重不足，Abstract overclaim** [R1-N3, R2-N2 共识]\n\nSection 4.5 的 post-RL 发现仅基于 N=1（Qwen, 15% MMLU, GRPO）。Figure 4 无误差条或置信区间。一个 N=1 观察被提升到与 n=10 seeds 验证的其他发现同等地位——Abstract 将其列为四大 findings 之一且未标注 preliminary，与正文末尾 \"We report this as a preliminary characterization\" 的 hedging 不一致。单一实验点无法建立任何 \"pattern\"。R1 建议如不增加实验应从 Abstract 移除。\n\n**MF-4. [Critical] PSN-IRT 参数依赖缺乏敏感性分析** [R1-N4, R2 AGREE]\n\n整个框架的 4PL 参数来自 PSN-IRT，这是 single point of failure。论文未提供：(a) 参数精度/标准误信息；(b) 参数扰动下 ℓz* 的敏感性分析（如 5-10% 噪声）；(c) 与其他估计方法的交叉验证。4PL upper asymptote d 参数本身估计不稳定。如果 leaderboard 校准样本包含已污染模型（很可能），PSN-IRT 参数可能已有偏差。\n\n**MF-5. [Critical] Inverted-U 削弱 minimal-information 实用性主张** [R1-N2, R2 AGREE]\n\nfree-θ 下 Qwen |d| 从 15% 的 6.58 降到 50% 的 1.90——污染越严重检测越弱。fixed-θ anchoring 解决此问题但需要 clean baseline，与 Abstract \"operating at the minimal-information point: binary response patterns\" 的定位相矛盾。方法的宣传定位与实际信息需求之间存在显著落差。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1. 仅两个污染水平不足以支撑 inverted-U 曲线** [R1-W2, R2 AGREE]\n三个数据点（0%, 15%, 50%）无法区分 inverted-U 和 monotonic decrease。缺少 5%, 10%, 25% 等中间点来确认峰值位置和曲线形状。\n\n**SF-2. Item-level detection 接近随机，与 fingerprint claim 矛盾** [R1-W3, R2-W2 共识]\nTable 8: ℓz* itemwise AUROC=0.53 ≈ random。但 Section 5 声称 \"ℓz* can yield per-item memorization fingerprints\"，claim 与 evidence 矛盾。\n\n**SF-3. Detection-diagnosis tradeoff 论证不足** [R1-W4, R2 AGREE]\naccuracy |d| 比 ℓz* 大 20-70 倍，但论文未提供具体 use case 展示诊断信息如何改变实际决策。\n\n**SF-4. 57/60 vs 4/60 比较具有误导性** [R1-W5, R2 AGREE]\n57/60 flagging 反映 IRT misfit 普遍性而非检测能力优势。将 raw ℓz* 的 95% FPR 作为优势呈现，与 Δℓz* 设计动机（正是因为 raw ℓz* 无法区分 contamination 和 general misfit）自相矛盾。\n\n**SF-5. 模型覆盖范围过窄** [R2-W1, R1 AGREE]\n仅 3 个 7-8B 模型。θ-shift dynamics 的 negative correlation 基于 3 个数据点不足以建立系统性关系。缺少更大规模（13B/70B）和不同架构（MoE）验证。\n\n**SF-6. Mistral n=6 与 n=10 声称不一致** [R1-Q2, R2 AGREE]\nTable 1 footnote 标注 Mistral n=6，但 Section 3.3 声称 \"n=10 clean seeds per family\"。应在正文解释原因。\n\n**SF-7. 缺少代码/数据可用性声明** [R1]\nARR 建议提供 reproducibility statement。PSN-IRT 参数可获取性和 bootstrap CI 实现细节（bias-corrected? percentile?）未说明。\n\n**SF-8. Orphan bibliography + 遗漏关键引用** [R1, R2]\nbib 有 28 条 orphan entries。Tendeiro & Meijer (2014) 和 St-Onge et al. (2011) 在 bib 中但未 cite，均与核心 findings 直接相关。总引用 31 篇处于顶会下限。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致（均 [AGREE]）：\n\n1. **MF-1**: IRT 假设违反 + Δℓz* 有效性是方法论根基问题\n2. **MF-2**: QLoRA SFT 的生态效度限制所有 findings 的外推范围\n3. **MF-3**: Post-RL N=1 被 overclaim，应降级或补充实验\n4. **MF-4**: PSN-IRT 参数依赖是 single point of failure\n5. **MF-5**: Inverted-U 与 minimal-information 定位矛盾\n6. **SF-1 至 SF-8**: 所有 Should-Fix 均达成共识\n\n---\n\n## Reviewer Divergence\n\n**分歧 1: Findings 新颖性定级**\n- R2 认为 3/4 findings 可从 IRT 理论直接预测（inverted-U = 天花板效应, θ-shift = 经典议题, tradeoff = power vs specificity），novelty 被高估 → **Critical**\n- R1 反驳（[REBUT]）：empirical characterization in new domain 有独立价值。θ-shift absorption 机制 + benchmark size 交互是 new empirical finding，4PL vs 3PL +27pp power gain 超越理论预测 → **Should-Fix**（加强对 prior literature 的引用即可）\n- **Review Director 判断**：降为 Should-Fix。论文标题已使用 \"characterization\" 定位，findings 的量化结果（|d| 幅度、benchmark size 依赖、4PL advantage）确实超越了理论层面的定性预测。但写作确实应更好 acknowledge prior IRT person-fit literature（特别是 St-Onge et al. 2011, Meijer & Sijtsma 2001 关于 ability-person fit interaction 的讨论）。\n\n**分歧 2: 是否需要与 ConStat/MIA/CoDec 实证对比**\n- R1 要求至少与 ConStat 进行实证对比（两者都基于 benchmark performance）→ **Warning**\n- R2 反驳（[REBUT]）：characterization paper 不应被要求性能竞赛，但应讨论互补关系\n- **Review Director 判断**：采纳 R2 立场。Characterization paper 的评价标准不同于 detection method paper。但 Discussion 确实应讨论与 ConStat 的互补性。\n\n---\n\n## Questions for Authors\n\n1. Appendix A 模拟是否假设 IRT 模型正确拟合？引入 local dependence（testlet 结构）后 ℓz* 的 Type I error rate 和检验力如何变化？\n2. Mistral 实际使用了多少 seeds？为什么与 Qwen/Llama 不同？\n3. PSN-IRT 校准数据是否包含已知被污染的模型？Section 3.1 的 \"rₐ=0.127\" 来自何种实验条件？\n4. Fixed-θ 的 cross-benchmark ability estimation 在实际部署中如何实现？如果多个 benchmark 同时被污染呢？\n5. Table 8 item-level AUROC=0.53 与 Section 5 \"per-item memorization fingerprints\" 如何调和？\n6. Post-RL 后 ℓz* gap 是否只是残留 accuracy difference（0.5-1%）被 IRT 放大的结果，而非独立的 response-pattern information？\n\n---\n\n## Missing References\n\n1. **Tendeiro & Meijer (2014)** — 非参数 person-fit 假设违反下的替代方案（已在 bib 未 cite）\n2. **St-Onge et al. (2011)** — aberrance rate 对 person-fit accuracy 的影响（已在 bib 未 cite）\n3. **Magis et al. (2012)** — person-fit 在 model misfit 下的 robustness 分析\n4. **Sinharay (2016)** — person-fit 在假设违反下的行为\n5. **Li et al. (2024)** — Data Contamination Quiz (TACL)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未配置（项目未启用 external_review.paperreview_ai）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成\n\n| 严重度 | 页码 | 发现 |\n|--------|------|------|\n| Critical | p12 | Appendix 最后一页仅 Table 8（4行×2列小表）占约 15% 面积，~85% 为空白。建议合并至 p11。 |\n| Warning | p4 | Table 1 主结果表未对最优值加粗标注；Table 2 (p6)、Table 3 (p7) 同样缺少加粗。 |\n| Warning | p8 | 正文最后页为纯文本（Discussion+Limitations+Conclusion+Refs 开头），无 display item。 |\n| Info | p2 | Figure 1 子图坐标轴标签和 legend 字号偏小（约正文 60%），建议放大至 70%+。 |\n| Info | p5 | Figure 2 热力图 cell 内数字字号较小，建议增大或简化 CI 显示。 |\n| Info | p11 | Tables 4-7 密集堆叠，表间距略紧。 |\n| Info | p1 | 首页无视觉锚点（ACL 模板限制，非硬伤）。 |\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 — Findings**（可被 Findings 接收）\n\n**置信度: 4/5**\n\n**评分理由**:\n\n跨学科概念桥接（person-fit → contamination）genuinely novel，受控实验设计规范（n=10, 3 families, bootstrap CI），诚实的自我定位（characterization rather than tool）。这些优势使论文达到 Findings 可接收水平。\n\n但五个 critical 问题限制了其达到 main conference 水平（4.0）：\n\n1. **方法论根基不稳**（MF-1）: Δℓz* 有效性依赖 IRT 假设，但 LLM 系统性违反这些假设，且论文未分析污染对 item 依赖结构的影响。\n2. **生态效度受限**（MF-2）: QLoRA SFT 产生的 aberrance pattern 可能与 pretraining contamination 本质不同，所有 findings 的适用范围被限定为 SFT-based contamination。\n3. **核心 claim overclaim**（MF-3）: Post-RL finding 是最具新颖性的贡献，但 N=1 的证据不足以支撑 Abstract 级别的 claim。\n4. **外部依赖未验证**（MF-4）: PSN-IRT 参数是 single point of failure，缺乏敏感性分析。\n5. **实用性定位矛盾**（MF-5）: free-θ 的 inverted-U 问题削弱了 minimal-information 的卖点。\n\n**升级路径**（达到 4.0 所需）:\n- 对 Δℓz* 在 IRT 假设违反下的行为进行理论分析或模拟验证\n- Post-RL 实验扩展至至少 2 个额外模型或 RL 方法\n- PSN-IRT 参数扰动敏感性分析\n- 增加中间污染水平（25%）以验证 dose-response 曲线形状\n- 调整 Abstract/Introduction claim 强度以匹配证据层级\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 逻辑链清晰（问题→现有方法不足→psychometric analogy→本文方法→findings），但第四个 bullet（post-RL）未标注 N=1/preliminary\n- Figure 1 的 clean/contaminated response pattern 示意图有效传达核心 insight\n- \"operating at the minimal-information point\" 的 claim 需与 fixed-θ 的额外信息需求协调\n\n### Section 2 (Related Work)\n- 覆盖三个维度（contamination detection, IRT for LLM, person-fit in psychometrics）结构清晰\n- 引用 31 篇处于顶会下限，bib 中有 28 条 orphan entries 需清理\n- 应引用 Tendeiro & Meijer (2014)（与 tradeoff 相关）、St-Onge et al. (2011)（与 inverted-U 相关）\n\n### Section 3 (Method)\n- 4PL 模型公式和 ℓz* 定义清晰\n- Δℓz* 差分设计的动机论证有力（57/60 flagging），但有效性条件（加性等量 misfit）未充分论证\n- Section 3.3: \"n=10 clean seeds per family\" 与 Mistral 实际 n=6 不一致\n- 缺少 data preprocessing 细节（如何从 benchmark 采样 15%/50%？分层还是随机？）\n\n### Section 4 (Results)\n- Section 4.2 (Inverted-U): 应引用 St-Onge et al. (2011) 讨论 aberrance rate 对 person-fit 的影响；\"inverted-U\" 表述应加限定（仅 2 个非零数据点）\n- Section 4.3 (θ-shift): 仅 3 个模型的 negative correlation 不足以建立系统性关系；ARC-C 反转现象的 ceiling effect 解释 interesting 但同样仅 1 个数据点\n- Section 4.4 (Tradeoff): Table 3 的 accuracy |d|=42-68 需解释为什么如此大（cross-seed variance 极小导致 denominator 很小）\n- Section 4.5 (Post-RL): N=1 无统计推断基础；Figure 4 需误差条；应排除 ℓz* gap 只是残留微小 accuracy difference 被放大的替代解释\n\n### Section 5 (Discussion)\n- \"per-item memorization fingerprints\" 与 Table 8 AUROC=0.53 矛盾\n- 57/60 vs 4/60 比较需重新表述——这是 IRT misfit 普遍性的证据，不是检测能力优势\n- 应讨论与 ConStat 的互补关系\n\n### Limitations\n- 覆盖了模型规模、污染机制、post-RL N=1 三个主要限制\n- **缺失**: IRT 假设违反（应是最重要的 limitation）、PSN-IRT 参数依赖\n- 篇幅适当（3 句话，符合 EMNLP 规范）\n\n### 格式合规\n- ✅ 正文 8 页内\n- ✅ ACL review 模板，双盲匿名\n- ✅ Limitations 章节存在\n- ⚠️ Mistral n=6 标注不一致\n- ⚠️ 无 reproducibility statement\n",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 Findings",
  "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "irt_personfit_contam",
    "report": "# 审稿报告：IRT Person-Fit for LLM Benchmark Contamination Detection\n\n**项目**: irt_personfit_contam\n**目标 Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿轮次**: Round 2 (fresh)\n**审稿日期**: 2026-05-21\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作格式）\n\n---\n\n## Summary\n\n本文首次系统地将 IRT person-fit 统计量（ℓz*）应用于 LLM benchmark contamination 检测，操作在 minimal-information point（仅需二值 response pattern + 外部校准的 4PL 参数）。通过在三个 7-8B 模型家族（Qwen, Llama, Mistral; n=10 seeds）上的受控实验（QLoRA SFT, 15%/50% 污染）和 MMLU + ARC-Challenge 两个 benchmark，论文识别了四个边界条件：(1) free-θ 下的 inverted-U dose-response，(2) 模型特异性 θ-shift dynamics，(3) detection-diagnosis tradeoff，(4) post-RL residual pattern (N=1)。\n\n---\n\n## Strengths\n\n**S1. 跨学科新颖性** [R1, R2 共识]\n将教育测量学中有 40 年积累的 person-fit 统计量迁移到 LLM contamination 检测，这一视角是 genuinely novel 的。基于\"响应模式异常\"而非\"信息泄露痕迹\"，与现有 MIA/n-gram/probing 方法在理论层面有根本性区别。\n\n**S2. Δℓz* 差分设计务实合理** [R1, R2 共识]\n认识到 LLM 系统性违反 IRT 假设（57/60 cells flagged even absent contamination），提出差分设计消除共享 misfit，是方法论上合理的处理。\n\n**S3. 受控实验设计规范** [R1, R2 共识]\nn=10 seeds × 3 model families × 2 benchmarks × 3 conditions，bootstrap 95% CI（10,000 resamples）提供了统计推断基础。Table 1 所有 CI 不包含零。Cohen's d 作为 effect-size 指标选择恰当。\n\n**S4. θ-shift 机制分析有理论深度** [R1]\n揭示 baseline accuracy 与检测灵敏度的负相关（MMLU 上 Mistral 52.4% → |d|=3.50 > Qwen 67.8% → |d|=1.90），以及 ARC-C 上因天花板效应导致的 sign flip，提供了可解释的机制理解。\n\n**S5. 坦诚的自我定位** [R1, R2 共识]\n以\"characterization\"而非\"detection method\"自居，Discussion 和 Limitations 坦诚讨论了主要局限。Detection-diagnosis tradeoff 的诚实报告（accuracy |d|=42-68 vs ℓz* |d|=0.58-1.90）值得肯定。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1. [Critical] IRT 假设违反分析不充分，Δℓz* 有效性缺乏理论保证** [R1-N1, R2 AGREE]\n\nSection 3.2 承认 LLM 系统性违反 IRT 局部独立性和单维性假设。Δℓz* 差分设计仅在 clean/contaminated conditions 下 misfit 为加性且等量时有效。但论文未分析关键问题：**污染是否改变了 item 间依赖结构？** 如果 memorized items 的答对独立于 θ（纯靠记忆），contaminated condition 下的 misfit 结构与 clean condition 不同，Δℓz* 不再是有效差分估计量。Appendix A 模拟验证（R²=0.957）假设 IRT 模型成立，构成循环论证。57/60 clean cells 被 flag 说明 IRT misfit 极严重，Δℓz* 承担极大校正负担但其理论保证缺失。\n\n**MF-2. [Critical] 生态效度不足——QLoRA SFT ≠ pretraining 污染** [R2-N1, R1 AGREE]\n\nQLoRA (rank=16, α=32) 仅修改低秩 adapter，权重变化受限于低秩子空间，与 pretraining contamination（全参数分布式梯度更新）本质不同。Fine-tuning 污染接近\"item preknowledge\"（教育测试中的作弊），pretraining 污染更接近\"over-exposure\"（重复暴露的隐式学习），两种机制可能产生不同的 aberrance pattern。所有四个 findings 的外推有效性存疑，核心贡献范围被 SFT-specific 所限制。\n\n**MF-3. [Critical] Post-RL finding (N=1) 统计效力严重不足，Abstract overclaim** [R1-N3, R2-N2 共识]\n\nSection 4.5 的 post-RL 发现仅基于 N=1（Qwen, 15% MMLU, GRPO）。Figure 4 无误差条或置信区间。一个 N=1 观察被提升到与 n=10 seeds 验证的其他发现同等地位——Abstract 将其列为四大 findings 之一且未标注 preliminary，与正文末尾 \"We report this as a preliminary characterization\" 的 hedging 不一致。单一实验点无法建立任何 \"pattern\"。R1 建议如不增加实验应从 Abstract 移除。\n\n**MF-4. [Critical] PSN-IRT 参数依赖缺乏敏感性分析** [R1-N4, R2 AGREE]\n\n整个框架的 4PL 参数来自 PSN-IRT，这是 single point of failure。论文未提供：(a) 参数精度/标准误信息；(b) 参数扰动下 ℓz* 的敏感性分析（如 5-10% 噪声）；(c) 与其他估计方法的交叉验证。4PL upper asymptote d 参数本身估计不稳定。如果 leaderboard 校准样本包含已污染模型（很可能），PSN-IRT 参数可能已有偏差。\n\n**MF-5. [Critical] Inverted-U 削弱 minimal-information 实用性主张** [R1-N2, R2 AGREE]\n\nfree-θ 下 Qwen |d| 从 15% 的 6.58 降到 50% 的 1.90——污染越严重检测越弱。fixed-θ anchoring 解决此问题但需要 clean baseline，与 Abstract \"operating at the minimal-information point: binary response patterns\" 的定位相矛盾。方法的宣传定位与实际信息需求之间存在显著落差。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1. 仅两个污染水平不足以支撑 inverted-U 曲线** [R1-W2, R2 AGREE]\n三个数据点（0%, 15%, 50%）无法区分 inverted-U 和 monotonic decrease。缺少 5%, 10%, 25% 等中间点来确认峰值位置和曲线形状。\n\n**SF-2. Item-level detection 接近随机，与 fingerprint claim 矛盾** [R1-W3, R2-W2 共识]\nTable 8: ℓz* itemwise AUROC=0.53 ≈ random。但 Section 5 声称 \"ℓz* can yield per-item memorization fingerprints\"，claim 与 evidence 矛盾。\n\n**SF-3. Detection-diagnosis tradeoff 论证不足** [R1-W4, R2 AGREE]\naccuracy |d| 比 ℓz* 大 20-70 倍，但论文未提供具体 use case 展示诊断信息如何改变实际决策。\n\n**SF-4. 57/60 vs 4/60 比较具有误导性** [R1-W5, R2 AGREE]\n57/60 flagging 反映 IRT misfit 普遍性而非检测能力优势。将 raw ℓz* 的 95% FPR 作为优势呈现，与 Δℓz* 设计动机（正是因为 raw ℓz* 无法区分 contamination 和 general misfit）自相矛盾。\n\n**SF-5. 模型覆盖范围过窄** [R2-W1, R1 AGREE]\n仅 3 个 7-8B 模型。θ-shift dynamics 的 negative correlation 基于 3 个数据点不足以建立系统性关系。缺少更大规模（13B/70B）和不同架构（MoE）验证。\n\n**SF-6. Mistral n=6 与 n=10 声称不一致** [R1-Q2, R2 AGREE]\nTable 1 footnote 标注 Mistral n=6，但 Section 3.3 声称 \"n=10 clean seeds per family\"。应在正文解释原因。\n\n**SF-7. 缺少代码/数据可用性声明** [R1]\nARR 建议提供 reproducibility statement。PSN-IRT 参数可获取性和 bootstrap CI 实现细节（bias-corrected? percentile?）未说明。\n\n**SF-8. Orphan bibliography + 遗漏关键引用** [R1, R2]\nbib 有 28 条 orphan entries。Tendeiro & Meijer (2014) 和 St-Onge et al. (2011) 在 bib 中但未 cite，均与核心 findings 直接相关。总引用 31 篇处于顶会下限。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致（均 [AGREE]）：\n\n1. **MF-1**: IRT 假设违反 + Δℓz* 有效性是方法论根基问题\n2. **MF-2**: QLoRA SFT 的生态效度限制所有 findings 的外推范围\n3. **MF-3**: Post-RL N=1 被 overclaim，应降级或补充实验\n4. **MF-4**: PSN-IRT 参数依赖是 single point of failure\n5. **MF-5**: Inverted-U 与 minimal-information 定位矛盾\n6. **SF-1 至 SF-8**: 所有 Should-Fix 均达成共识\n\n---\n\n## Reviewer Divergence\n\n**分歧 1: Findings 新颖性定级**\n- R2 认为 3/4 findings 可从 IRT 理论直接预测（inverted-U = 天花板效应, θ-shift = 经典议题, tradeoff = power vs specificity），novelty 被高估 → **Critical**\n- R1 反驳（[REBUT]）：empirical characterization in new domain 有独立价值。θ-shift absorption 机制 + benchmark size 交互是 new empirical finding，4PL vs 3PL +27pp power gain 超越理论预测 → **Should-Fix**（加强对 prior literature 的引用即可）\n- **Review Director 判断**：降为 Should-Fix。论文标题已使用 \"characterization\" 定位，findings 的量化结果（|d| 幅度、benchmark size 依赖、4PL advantage）确实超越了理论层面的定性预测。但写作确实应更好 acknowledge prior IRT person-fit literature（特别是 St-Onge et al. 2011, Meijer & Sijtsma 2001 关于 ability-person fit interaction 的讨论）。\n\n**分歧 2: 是否需要与 ConStat/MIA/CoDec 实证对比**\n- R1 要求至少与 ConStat 进行实证对比（两者都基于 benchmark performance）→ **Warning**\n- R2 反驳（[REBUT]）：characterization paper 不应被要求性能竞赛，但应讨论互补关系\n- **Review Director 判断**：采纳 R2 立场。Characterization paper 的评价标准不同于 detection method paper。但 Discussion 确实应讨论与 ConStat 的互补性。\n\n---\n\n## Questions for Authors\n\n1. Appendix A 模拟是否假设 IRT 模型正确拟合？引入 local dependence（testlet 结构）后 ℓz* 的 Type I error rate 和检验力如何变化？\n2. Mistral 实际使用了多少 seeds？为什么与 Qwen/Llama 不同？\n3. PSN-IRT 校准数据是否包含已知被污染的模型？Section 3.1 的 \"rₐ=0.127\" 来自何种实验条件？\n4. Fixed-θ 的 cross-benchmark ability estimation 在实际部署中如何实现？如果多个 benchmark 同时被污染呢？\n5. Table 8 item-level AUROC=0.53 与 Section 5 \"per-item memorization fingerprints\" 如何调和？\n6. Post-RL 后 ℓz* gap 是否只是残留 accuracy difference（0.5-1%）被 IRT 放大的结果，而非独立的 response-pattern information？\n\n---\n\n## Missing References\n\n1. **Tendeiro & Meijer (2014)** — 非参数 person-fit 假设违反下的替代方案（已在 bib 未 cite）\n2. **St-Onge et al. (2011)** — aberrance rate 对 person-fit accuracy 的影响（已在 bib 未 cite）\n3. **Magis et al. (2012)** — person-fit 在 model misfit 下的 robustness 分析\n4. **Sinharay (2016)** — person-fit 在假设违反下的行为\n5. **Li et al. (2024)** — Data Contamination Quiz (TACL)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未配置（项目未启用 external_review.paperreview_ai）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成\n\n| 严重度 | 页码 | 发现 |\n|--------|------|------|\n| Critical | p12 | Appendix 最后一页仅 Table 8（4行×2列小表）占约 15% 面积，~85% 为空白。建议合并至 p11。 |\n| Warning | p4 | Table 1 主结果表未对最优值加粗标注；Table 2 (p6)、Table 3 (p7) 同样缺少加粗。 |\n| Warning | p8 | 正文最后页为纯文本（Discussion+Limitations+Conclusion+Refs 开头），无 display item。 |\n| Info | p2 | Figure 1 子图坐标轴标签和 legend 字号偏小（约正文 60%），建议放大至 70%+。 |\n| Info | p5 | Figure 2 热力图 cell 内数字字号较小，建议增大或简化 CI 显示。 |\n| Info | p11 | Tables 4-7 密集堆叠，表间距略紧。 |\n| Info | p1 | 首页无视觉锚点（ACL 模板限制，非硬伤）。 |\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 — Findings**（可被 Findings 接收）\n\n**置信度: 4/5**\n\n**评分理由**:\n\n跨学科概念桥接（person-fit → contamination）genuinely novel，受控实验设计规范（n=10, 3 families, bootstrap CI），诚实的自我定位（characterization rather than tool）。这些优势使论文达到 Findings 可接收水平。\n\n但五个 critical 问题限制了其达到 main conference 水平（4.0）：\n\n1. **方法论根基不稳**（MF-1）: Δℓz* 有效性依赖 IRT 假设，但 LLM 系统性违反这些假设，且论文未分析污染对 item 依赖结构的影响。\n2. **生态效度受限**（MF-2）: QLoRA SFT 产生的 aberrance pattern 可能与 pretraining contamination 本质不同，所有 findings 的适用范围被限定为 SFT-based contamination。\n3. **核心 claim overclaim**（MF-3）: Post-RL finding 是最具新颖性的贡献，但 N=1 的证据不足以支撑 Abstract 级别的 claim。\n4. **外部依赖未验证**（MF-4）: PSN-IRT 参数是 single point of failure，缺乏敏感性分析。\n5. **实用性定位矛盾**（MF-5）: free-θ 的 inverted-U 问题削弱了 minimal-information 的卖点。\n\n**升级路径**（达到 4.0 所需）:\n- 对 Δℓz* 在 IRT 假设违反下的行为进行理论分析或模拟验证\n- Post-RL 实验扩展至至少 2 个额外模型或 RL 方法\n- PSN-IRT 参数扰动敏感性分析\n- 增加中间污染水平（25%）以验证 dose-response 曲线形状\n- 调整 Abstract/Introduction claim 强度以匹配证据层级\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 逻辑链清晰（问题→现有方法不足→psychometric analogy→本文方法→findings），但第四个 bullet（post-RL）未标注 N=1/preliminary\n- Figure 1 的 clean/contaminated response pattern 示意图有效传达核心 insight\n- \"operating at the minimal-information point\" 的 claim 需与 fixed-θ 的额外信息需求协调\n\n### Section 2 (Related Work)\n- 覆盖三个维度（contamination detection, IRT for LLM, person-fit in psychometrics）结构清晰\n- 引用 31 篇处于顶会下限，bib 中有 28 条 orphan entries 需清理\n- 应引用 Tendeiro & Meijer (2014)（与 tradeoff 相关）、St-Onge et al. (2011)（与 inverted-U 相关）\n\n### Section 3 (Method)\n- 4PL 模型公式和 ℓz* 定义清晰\n- Δℓz* 差分设计的动机论证有力（57/60 flagging），但有效性条件（加性等量 misfit）未充分论证\n- Section 3.3: \"n=10 clean seeds per family\" 与 Mistral 实际 n=6 不一致\n- 缺少 data preprocessing 细节（如何从 benchmark 采样 15%/50%？分层还是随机？）\n\n### Section 4 (Results)\n- Section 4.2 (Inverted-U): 应引用 St-Onge et al. (2011) 讨论 aberrance rate 对 person-fit 的影响；\"inverted-U\" 表述应加限定（仅 2 个非零数据点）\n- Section 4.3 (θ-shift): 仅 3 个模型的 negative correlation 不足以建立系统性关系；ARC-C 反转现象的 ceiling effect 解释 interesting 但同样仅 1 个数据点\n- Section 4.4 (Tradeoff): Table 3 的 accuracy |d|=42-68 需解释为什么如此大（cross-seed variance 极小导致 denominator 很小）\n- Section 4.5 (Post-RL): N=1 无统计推断基础；Figure 4 需误差条；应排除 ℓz* gap 只是残留微小 accuracy difference 被放大的替代解释\n\n### Section 5 (Discussion)\n- \"per-item memorization fingerprints\" 与 Table 8 AUROC=0.53 矛盾\n- 57/60 vs 4/60 比较需重新表述——这是 IRT misfit 普遍性的证据，不是检测能力优势\n- 应讨论与 ConStat 的互补关系\n\n### Limitations\n- 覆盖了模型规模、污染机制、post-RL N=1 三个主要限制\n- **缺失**: IRT 假设违反（应是最重要的 limitation）、PSN-IRT 参数依赖\n- 篇幅适当（3 句话，符合 EMNLP 规范）\n\n### 格式合规\n- ✅ 正文 8 页内\n- ✅ ACL review 模板，双盲匿名\n- ✅ Limitations 章节存在\n- ⚠️ Mistral n=6 标注不一致\n- ⚠️ 无 reproducibility statement\n",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 Findings",
    "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209"
  }
}
```

</details>

---


### Tool result

_source line 284 · 2026-05-21T18:25:15.625192+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_9840a7d708128f2f1d02985bd9b8d901:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4065
}
```

</details>

---


### Assistant

_source line 285 · 2026-05-21T18:25:29.566353+00:00_

审稿报告已投递给 Research Director。

**审稿完成总结：**

- **Overall: 3.0 (Findings)**，两位 Reviewer 完全一致
- **5 个 Must-Fix (Critical)**：Δℓz* 理论保证缺失、QLoRA 生态效度不足、Post-RL N=1 overclaim、PSN-IRT 参数无敏感性分析、inverted-U 与 minimal-information 定位矛盾
- **8 个 Should-Fix (Warning)**：污染水平过少、item-level 检测近随机、tradeoff 论证不足、57/60 比较误导性、模型覆盖窄、Mistral n=6 不一致、缺 reproducibility statement、orphan bib entries
- **2 个分歧**：novelty 定级（R2 critical vs R1 should-fix，采纳 R1 降级为 should-fix）和实证对比需求（R1 要求 vs R2 rebut，采纳 R2 立场）
- **视觉审查**：1 critical（p12 空白）、2 warning、4 info
- **Issue Tracker**：已更新 `review_issues.yaml`，Round 1 的 BEST-W1、V6-THETA-SPECIFICITY、ALL-W3 已标记 resolved

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 35

## Round 35

2 recorded events


### User

_source line 286 · 2026-05-21T18:25:32.155840+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **R2-N1 (QLoRA 生态效度)**: [AGREE]，与我的 W1 一致，同意升级理由
- **R2-N2 (Post-RL N=1)**: [AGREE]，与我的 N3 完全一致
- **R2-N3 (新颖性被高估)**: [REBUT]，部分反驳——general phenomena 确实已知，但 domain-specific 量化 characterization（如 benchmark size × model ability 交互、tradeoff 幅度）有独立价值；建议从 critical 降级为 should-fix
- **R2-W1~W4**: 全部 [AGREE]，其中 W3 (Δℓz* 假设) 我认为比 R2 定级更严重（我列为 N1 critical）

两份审稿的核心交集：方法论基础和实验范围均需加强，当前支持 Findings 接收 (Overall 3.0)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 287 · 2026-05-21T18:25:55.235829+00:00_

审稿报告已成功投递至 Research Director。

**圆桌审稿总结**：

- **评分**：Overall 3.0（Findings），两位 Reviewer 完全一致
- **5 个 Must-Fix**（共识 critical）：IRT 假设违反分析不充分、QLoRA 生态效度受限、Post-RL N=1 overclaim、PSN-IRT 参数无敏感性分析、inverted-U 与 minimal-information 定位矛盾
- **8 个 Should-Fix**：污染水平不足、item-level 近随机、tradeoff 论证弱、57/60 比较误导、模型覆盖窄、Mistral n=6 不一致、缺 reproducibility statement、orphan bib entries
- **2 个分歧**（已裁决）：findings 新颖性（降为 should-fix）、实证对比需求（采纳 R2 立场，characterization paper 不需性能竞赛）
- **视觉审查**：已完成（1 critical p12 空白、2 warning）
- **Issue Tracker**：已更新，Round 1 的多个 issue（figures/refs/Related Work/θ-shift 章节）确认 resolved

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 36

## Round 36

76 recorded events


### User

_source line 288 · 2026-05-21T21:05:34.938519+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_personfit_contam
- 论文路径: projects/irt_personfit_contam/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR Long Paper
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 289 · 2026-05-21T21:05:42.174876+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 290 · 2026-05-21T21:05:42.225734+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 291 · 2026-05-21T21:05:48.951421+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch,read_local_file",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch,read_local_file",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 292 · 2026-05-21T21:05:49.002092+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 293 · 2026-05-21T21:05:56.380522+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 294 · 2026-05-21T21:05:56.431215+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 295 · 2026-05-21T21:06:02.605483+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 296 · 2026-05-21T21:06:03.860988+00:00_

{"result":"# 项目 irt_personfit_contam 概况\n\n## 实验状态 (78 个)\n\n- **exp-domain-analysis**: DONE (success) — \n- **exp-ml-classifier-baseline**: DONE (success) — \n- **exp-v1-irt-refit-pilot**: DONE (negative) — \n- **exp-clean-control-delta**: DONE (success) — \n- **exp-fdr-correction**: DONE (success) — \n- **exp-cross-benchmark-analysis**: DONE (success) — \n- **exp-accuracy-zscore-baseline**: DONE (success) — \n- **exp-item-alignment-check**: DONE (negative) — \n- **exp-power-theory**: DONE (success) — \n- **exp-empirical-null**: DONE (negative) — \n- **exp-leaderboard-data-recon**: DONE (success) — \n- **exp-extended-sim**: DONE (success) — \n- **exp-two-sided**: DONE (negative) — \n- **phase_b_personfit**: DONE (success) — \n- **sim_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-arcc-benchmark: ℓz* contamination detection generalizes beyond MMLU to ARC-Challenge, a second benchmark with PSN-IRT 4PL calibration — demonstrating cross-benchmark applicability and addressing reviewer concern about single-benchmark evaluation.（准备中）\n- arcc-clean-s10（准备中）\n- arcc-clean-s9（准备中）\n- arcc-clean-s8（准备中）\n- arcc-clean-s7（准备中）\n- exp-ctrl-contam-qwen-clean-s10: Tenth independent clean Qwen2.5-7B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation（准备中）\n- exp-constat-comparison: ConStat (NeurIPS 2024) requires multi-benchmark performance scores for contamination detection, making it inapplicable or underpowered in single-benchmark scenarios. ℓz* operates on binary response patterns from a single benchmark, demonstrating superior minimal-information detection capability.（准备中）\n- exp-arcc-clean-s1: ARC-Challenge clean baseline (seed=42) for cross-benchmark ℓz* detection — establishing clean lz* distribution on a second benchmark with PSN-IRT 4PL calibration（准备中）\n- exp-mia-mink-comparison: MIA methods (Min-K%/Min-K%++) fail to detect contamination in post-RL (GRPO) models because R
…[truncated 1160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1255
}
```

</details>

---


### Tool call

_source line 297 · 2026-05-21T21:06:04.313199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 298 · 2026-05-21T21:06:05.318000+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\usepackage{enumitem}
16	
17	\newcommand{\irtfit}{\textsc{IRT-FIT}}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{What Can Binary Response Patterns Reveal About Benchmark Contamination? \\
22	An IRT Person-Fit Characterization}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{sections/abstract}
31	\end{abstract}
32	
33	\input{sections/introduction}
34	\input{sections/related_work}
35	\input{sections/method}
36	\input{sections/results}
37	\input{sections/discussion}
38	\input{sections/conclusion}
39	
40	\input{sections/limitations}
41	
42	\section*{Reproducibility Statement}
43	Code and response data will be released upon acceptance.
44	Bootstrap confidence intervals use the percentile method with 10,000 resamples; random seeds are reported for all experiments.
45	Pre-calibrated 4PL item parameters are from the publicly available PSN-IRT item bank \citep{psnirt2026}.
46	
47	\bibliography{references}
48	
49	\appendix
50	\input{sections/appendix}
51	
52	\end{document}
53	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 299 · 2026-05-21T21:06:05.318359+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-21T21:06:05.970730+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_personfit_contam",
    "file": "memory.md"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-21T21:06:10.738807+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I searched for "EMNLP 2026 ARR call f
…[truncated 1173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 5420
}
```

</details>

---


### Tool result

_source line 302 · 2026-05-21T21:06:10.739803+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/memory.md\", \"content\": \"# Memory — irt_personfit_contam\\n\\n## OOM 教训 (2026-05-20)\\n- 7.6GB RAM 机器上，N_SIM×n_items float64 矩阵不能一次性分配。MMLU 10K×14042×8B ≈ 1.07GB 单个矩阵，compute_lz_star 内部创建 ~7 个同尺寸中间数组 → OOM\\n- 解决方案：BATCH_SIZE=500 分批计算 + N_SIM 降至 2000（统计效力足够）\\n- generate_response 和 compute_lz_star 都需要分批\\n\\n## Worker context exhaustion 教训 (2026-05-20)\\n- exp-v1-irt-refit-expanded Worker 跑 1.5 小时后崩溃，无输出。任务是从 HuggingFace 下载 500+ 模型的 per-item 数据并拟合 IRT。\\n- **根因**: 大量 HF API 调用 + 数据处理的累积输出耗尽 Worker context window。\\n- **教训**: 涉及大规模数据下载（100+ datasets）的任务必须分批 + checkpoint 中间结果，或拆成多个 Worker 串行执行。单个 Worker 不适合做 1.5hr+ 的重型数据工程。\\n- **补充 (同日)**: ssh_read_only 读取大 JSON 文件（8MB+ 单行）也会撑爆 context。Worker 操作远程大文件必须用 python 脚本提取摘要，不要 cat/head。\\n- **补充 (同日)**: Worker 无法在进程内长时间等待（~2 min 就退出）。涉及 GPU 训练 + eval 的任务应分阶段处理：训练完成后由 cron 回调触发 eval Worker，或由主 Agent 定时派 Worker 检查。\\n\\n## sim_001 关键发现 (2026-05-20)\\n- **Null check 全通过**：PSN-IRT 神经网络估计的 4PL 参数与经典 IRT 兼容，lz* ≈ N(0,1)\\n  - 大 benchmark（GSM8K/HellaSwag/MMLU）KS p 全部 > 0.01\\n  - 小 benchmark（HumanEval/ARC-C）KS p < 0.01，但属预期（items 太少，CLT 近似弱）\\n- **检测力与 n_items 强正相关**：MMLU(14042)=97.9% >> HellaSwag(10042)=73.3% >> GSM8K(1319)=57.8% >> ARC-C(295)=12.9%\\n- **Inverted-U 所有 benchmark 可观测**：power 在 25-50% contamination 达峰，100% 全部 NaN（全答对 → MLE 不收敛）\\n\\n## PSN-IRT 12 模型身份 (2026-05-20)\\n\\n**来源**：arXiv:2505.15055 (AAAI 2026 Oral)，GitHub repo `Joe-Hall-Lee/PSN-IRT`\\n\\n| student_id | θ | 正确率 | 模型名称 | 类型 |\\n|---|---|---|---|---|\\n| 0 | 1.46 | 80.6% | 360GPT2-Pro | API |\\n| 1 | 3.77 | 85.7% | DeepSeek-V3 | API |\\n| 2 | 1.14 | 78.9% | Doubao-pro | API |\\n| 3 | 0.78 | 84.5% | Gemini-1.5 | API |\\n| 4 | -3.38 | 23.1% | Gemma-2B-it | 开源 2B |\\n| 5 | 1.73 | 82.1% | Hunyuan-Turbo | API |\\n| 6 | -1.37 | 40.0% | Mistral-7B-Instruct-v0.1 | 开源 7B |\\n| 7 | 0.93 | 77.0% | Moonshot-v1 | API |\\n| 8 | 0.96 | 
…[truncated 10860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4769
}
```

</details>

---


### Tool call

_source line 303 · 2026-05-21T21:06:21.580178+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-21T21:06:21.731164+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers deadline submission Budapest"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers deadline submission Budapest"
  }
}
```

</details>

---


### Tool call

_source line 305 · 2026-05-21T21:06:22.133418+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
  }
}
```

</details>

---


### Tool result

_source line 306 · 2026-05-21T21:06:22.183996+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-21T21:06:27.301103+00:00_

Web search results for query: "EMNLP 2026 call for papers deadline submission Budapest"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"}]

B
…[truncated 1032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 5569
}
```

</details>

---


### Tool result

_source line 308 · 2026-05-21T21:06:28.054307+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here are the ACL Rolling Review 2026 submission guidelines for page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references, while review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references. Upon acceptance, final versions of long papers w
…[truncated 1195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 6474
}
```

</details>

---


### Tool call

_source line 309 · 2026-05-21T21:06:32.921981+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
  }
}
```

</details>

---


### Tool result

_source line 310 · 2026-05-21T21:06:33.424238+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 311 · 2026-05-21T21:06:33.474909+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org calls main conference papers submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org calls main conference papers submission guidelines"
  }
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-21T21:06:39.649335+00:00_

Web search results for query: "site:2026.emnlp.org calls main conference papers submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"}]

Based on the search results, here are the main submission guidelines for EMNLP 2026 main conference papers:

**Submission Process:**
Papers must be submitted through the ARR (ACL Rolling Review) system by the ARR 2026 May cycle at the latest.

**ARR Submission Declaration:**
Authors must explicitly declare which conference they intend to commit to at submission time when submitting to the ARR 2026 May cycle, and this choice will be binding for EMNLP 2026.

**Paper Requirements:**
All submitted papers are expected to describe original, completed and unpublished work. There is a requirement on re-use of text from other publications (no more than 10% total tokens).

**AI Use Policy:**
EMNLP 2026 is taking actions against irresponsible AI use in paper submissions, and authors should refer to ACL's guidelines on Generative Assistance in Authorship.

**Reviewer Requirements:**
All authors are expected to sign up to review, or serve as an Area Chair or Senior Area Chair, with assignments based on qualifications.

For more detailed information, the search results recommend checking the ARR Call for Papers directly.


REMINDER: You MUST include t
…[truncated 72 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 6174
}
```

</details>

---


### Tool call

_source line 313 · 2026-05-21T21:06:49.889529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 314 · 2026-05-21T21:06:49.889880+00:00_

1	Benchmark contamination in Large Language Models (LLMs) undermines evaluation validity, yet most detection methods require privileged access to training data, model internals, or output probabilities.
2	We present the first systematic characterization of Item Response Theory (IRT) person-fit statistics for contamination detection, operating at the minimal-information point from the target model: only binary (correct/incorrect) response patterns are required, combined with externally calibrated four-parameter logistic (4PL) item parameters; diagnostic $\theta$-anchoring additionally requires a clean baseline.
3	The core insight is psychometric: a contaminated LLM produces aberrant response patterns analogous to a test-taker with item preknowledge.
4	Using the standardized person-fit statistic $\ell_z^*$ in a difference-in-differences design ($\Delta\ell_z^*$), we identify four IRT-specific behavior boundaries through controlled experiments across three model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B; $n{=}10$ seeds each) on MMLU (14,042 items) and ARC-Challenge (295 items):
5	(1) a non-monotonic dose-response (observed between 15\% and 50\% contamination) where free-$\theta$ estimation attenuates detection at higher contamination ($|d|{=}6.58$ at 15\% vs.\ $|d|{=}1.90$ at 50\% for Qwen);
6	(2) model-specific $\theta$-shift dynamics linking baseline ability to detection sensitivity;
7	(3) a detection-diagnosis tradeoff where simpler statistics (accuracy $z$-scores, HT) yield stronger detection ($|d|$ several-fold to over an order of magnitude larger) but lack the diagnostic capabilities of $\ell_z^*$ (seen/unseen decomposition, mechanistic $\theta$-shift insight, sensitivity to response-pattern structure at 57/60 vs.\ 4/60 flagged cells);
8	and (4) a preliminary post-RL observation ($N{=}1$, single model and RL method) that GRPO erases the accuracy gap but $\ell_z^*$ response-pattern structure persists.
9	These findings clarify what binary response patterns can
…[truncated 101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 315 · 2026-05-21T21:06:49.890084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 316 · 2026-05-21T21:06:50.392166+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation \citep{dodge2021, magar2022, sainz2023}.
4	As training corpora and public benchmarks both expand, the probability of overlap increases structurally \citep{jacovi2023, chang2024survey}.
5	When contamination occurs, benchmark scores no longer reflect genuine capability, undermining the primary mechanism by which the community compares and selects models.
6	
7	A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record.
8	N-gram overlap methods need the training corpus \citep{dodge2021, magar2022}.
9	Membership inference approaches require token-level probabilities \citep{minkprob2024, deng2024}.
10	Probing methods rely on crafted prompts \citep{golchin2024, oren2024}.
11	Performance-based methods require multiple test variants or output logits \citep{constat2024, codec2026}.
12	These methods form a detection frontier ordered by information access.
13	No existing method operates at the bottom of this frontier: binary response patterns alone.
14	
15	The need for minimal-information detection grows more pressing as models evolve.
16	\citet{wang2025fragility} show that all ten log-probability-based methods they evaluate perform at chance level on models trained with reinforcement learning (RL), because RL reshapes internal token distributions while preserving binary correctness patterns.
17	This motivates a fundamental question: \emph{what can binary response patterns reveal about contamination, and under what conditions?}
18	
19	We observe that a contaminated LLM is functionally analogous to a test-taker with item preknowledge: both produce response patterns in which difficult items are answered correctly through memorization rather than genuine ability.
20	This connection points t
…[truncated 3649 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 317 · 2026-05-21T21:06:50.392579+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 318 · 2026-05-21T21:06:51.296191+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Benchmark contamination detection.}
4	Contamination detection methods span a wide range of information requirements.
5	Corpus-search methods match benchmark items directly against pretraining data \citep{dodge2021, magar2022}, but require full corpus access unavailable for closed models.
6	Membership inference attacks (MIA) use token-level log-probabilities to distinguish training from unseen examples \citep{minkprob2024, deng2024}.
7	Generation-based probes elicit benchmark content via prompting \citep{golchin2024, golchin2024quiz, oren2024}.
8	Performance-based methods compare accuracy on target and reference sets \citep{constat2024, codec2026}, requiring multiple evaluations or in-context learning passes.
9	\citet{sainz2023} argue for systematic per-benchmark contamination measurement, and \citet{jacovi2023} propose mitigation strategies including encrypted benchmarks and canary strings.
10	
11	A critical limitation unites all token-level methods: \citet{wang2025fragility} show that RL post-training renders MIA-based detectors no better than random across 10 methods and 4 benchmarks, because RL reshapes token distributions while largely preserving binary correctness patterns.
12	\citet{selfcritique2026} and \citet{zhang2026rlvr} propose RL-specific solutions but require generation-level access.
13	Our approach operates at the minimal information point: binary responses only.
14	
15	\paragraph{IRT for LLM evaluation.}
16	Item Response Theory has seen growing adoption in NLP and ML evaluation.
17	\citet{martinezplumed2019} applied IRT to analyze machine learning classifiers at the instance level, establishing that item difficulty and discrimination parameters capture meaningful variation across models.
18	\citet{lalor2019} proposed estimating IRT parameters from DNN-generated response patterns, removing the need for human annotators.
19	\citet{rodriguez2021} demonstrated that IRT-informed item weighti
…[truncated 1704 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 319 · 2026-05-21T21:06:51.296582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 320 · 2026-05-21T21:06:51.798748+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{IRT Person-Fit Framework}
5	\label{sec:framework}
6	
7	We adopt the four-parameter logistic (4PL) IRT model to characterize contamination-induced aberrance in LLM response patterns.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ difficulty, $c_i$ the lower asymptote (guessing), and $d_i$ the upper asymptote (slip).
14	Item parameters are pre-calibrated by PSN-IRT \citep{psnirt2026} from a large-scale leaderboard dataset; we use these external parameters rather than re-estimating from potentially contaminated data, since our MML-EM refit shows discrimination recovery degrades to $r_a{=}0.127$ on contaminated leaderboard data.
15	
16	Given item parameters and a binary response vector $\mathbf{x} = (x_1, \ldots, x_n)$, we compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized log-likelihood residual quantifying deviation between observed and expected response patterns.
17	The Snijders correction accounts for estimation uncertainty in $\hat{\theta}_{\text{MLE}}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null \citep{drasgow1985, snijders2001}; \citet{magis2012} provide a detailed treatment of how response model selection and ability estimation affect $\ell_z^*$.
18	Large negative $\ell_z^*$ indicates aberrant responding (unexpected failures on easy items or unexpected successes on hard items); large positive values indicate over-consistent patterns.
19	
20	\subsection{$\Delta\ell_z^*$ Difference-in-Differences Design}
21	\label{sec:did}
22	
23	LLM response patterns systematically violate IRT assumptions of local independence and unidimensionality.
24	In our empirical data, 57 of 60 model-benchmark cells yield $|\ell_z^*| > 1.96$ even absent contamination, 
…[truncated 2929 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 321 · 2026-05-21T21:06:51.849491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 322 · 2026-05-21T21:06:52.301858+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Detection Signal Across Model Families}
5	\label{sec:detection}
6	
7	Table~\ref{tab:cohens_d} presents Cohen's $d$ effect sizes for $\ell_z^*$ across three model families and two benchmarks.
8	All confidence intervals exclude zero, confirming that $\Delta\ell_z^*$ reliably separates contaminated from clean models at both contamination levels.
9	
10	On MMLU, effect sizes range from $|d|{=}1.90$ (Qwen at 50\%) to $|d|{=}6.58$ (Qwen at 15\%), with Llama ($|d|{=}2.27$/$2.50$) and Mistral ($|d|{=}2.64$/$3.50$) falling between.
11	On ARC-C (295 items), Qwen yields $|d|{=}3.16$ at 15\% and $|d|{=}5.30$ at 50\%, demonstrating that detection remains feasible even on small benchmarks when contamination is sufficiently concentrated.
12	
13	Clean-model $\ell_z^*$ baselines diverge substantially across families: Qwen ${+}8.68$ ($\text{SD}{=}0.74$), Mistral ${+}4.02$ ($\text{SD}{=}2.05$), Llama ${+}0.29$ ($\text{SD}{=}1.45$), and ARC-C Qwen ${-}5.42$ ($\text{SD}{=}0.16$).
14	Absolute $\ell_z^*$ thresholds would produce contradictory results: Qwen's contaminated $\ell_z^*$ at 15\% (${+}3.85$) is still positive.
15	The $\Delta\ell_z^*$ design normalizes these divergent baselines: Cohen's $d$ yields comparable effect sizes ($|d|{=}1.90$--$6.58$) despite order-of-magnitude baseline differences.
16	Figure~\ref{fig:heatmap} provides a visual summary.
17	
18	\begin{table}[t]
19	\centering
20	\caption{Cohen's $d$ for $\Delta\ell_z^*$ across model families ($n{=}10$ clean seeds, bootstrap 95\% CI, 10,000 resamples). All CIs exclude 0.}
21	\label{tab:cohens_d}
22	\footnotesize
23	\begin{tabular}{@{}llrr@{}}
24	\toprule
25	Model & Benchmark & $d$ (15\%) [CI] & $d$ (50\%) [CI] \\
26	\midrule
27	Qwen & MMLU & $-6.58$ [$-15.2$, $-4.5$] & $-1.90$ [$-5.0$, $-1.0$] \\
28	Llama & MMLU & $-2.27$ [$-4.6$, $-1.6$] & $-2.50$ [$-5.0$, $-1.8$] \\
29	Mistral & MMLU & $-2.64$ [$-7.4$, $-1.5$] & $-3.50$ [$-9.6$, $-2.1$] \\
30	Qwen & ARC-C & $+3.16$
…[truncated 15750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 323 · 2026-05-21T21:06:52.302342+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 324 · 2026-05-21T21:06:52.754382+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The central question of this work is what binary response patterns can reveal about benchmark contamination.
4	Our findings reveal both the strengths and boundaries of IRT person-fit for this task: $\ell_z^*$ reliably detects SFT-stage contamination across model families, but four boundary conditions constrain its practical utility.
5	
6	\paragraph{Characterization over tool.}
7	The detection-diagnosis tradeoff (\S\ref{sec:degradation}) shows that simpler statistics detect contamination more powerfully than $\ell_z^*$: accuracy $z$-scores yield $|d|$ values several-fold to over an order of magnitude larger, and HT generally exceeds $\ell_z^*$.
8	The value of the IRT framework lies not in detection power but in mechanistic understanding: the $\theta$-shift analysis reveals \emph{why} detection sensitivity varies across models and contamination levels, the seen/unseen decomposition identifies \emph{what fraction} of items are memorized, and the 4PL parameterization captures item-level ceiling effects that 3PL misattributes as aberrance.
9	These diagnostic capabilities are invisible to accuracy $z$-scores or HT.
10	
11	\paragraph{Practical implications.}
12	Two results have immediate consequences.
13	Free-$\theta$ estimation can produce misleading dose-response curves; anchoring $\theta$ to a pre-contamination baseline substantially amplifies detection for high-ability models but is unnecessary where free estimation already captures the signal.
14	The benchmark size boundary means $\ell_z^*$ is most informative for large benchmarks ($n > 7{,}000$ items for 80\% power at 15\% contamination); on small benchmarks like ARC-C (295 items), detection relies on concentrated contamination effects.
15	
16	\paragraph{Scope and calibration.}
17	Universal baseline misfit (57/60 cells flagged) confirms systematic IRT violations; the $\Delta\ell_z^*$ design turns this into a feature through within-model differencing, but requires clea
…[truncated 1255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 325 · 2026-05-21T21:06:52.754814+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 326 · 2026-05-21T21:06:53.257392+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We presented the first systematic characterization of IRT person-fit behavior for LLM benchmark contamination detection, operating at the minimal-information point of binary response patterns with externally calibrated item parameters.
4	Controlled experiments across three model families ($n{=}10$ seeds each) establish that $\Delta\ell_z^*$ reliably detects SFT-stage contamination (all bootstrap 95\% CIs exclude zero), while revealing four boundary conditions---non-monotonic dose-response, model-specific $\theta$-shift dynamics, a detection-diagnosis tradeoff, and a preliminary post-RL residual pattern ($N{=}1$)---that determine when binary response patterns carry contamination information beyond aggregate accuracy, and when this information is bounded by model ability, benchmark size, and the $\theta$-estimation strategy.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 327 · 2026-05-21T21:06:53.257739+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 328 · 2026-05-21T21:06:54.663160+00:00_

1	\section*{Limitations}
2	
3	Our controlled experiments cover three model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B) at the 7--8B scale with QLoRA fine-tuning; validation on larger models (13B, 70B), mixture-of-experts architectures, and full-parameter fine-tuning remains future work.
4	The observed negative correlation between baseline ability and detection sensitivity rests on three model families and should be treated as a trend rather than a confirmed relationship.
5	Our findings are scoped to SFT-based contamination and may not generalize to pretraining contamination, which operates through different learning dynamics.
6	The post-RL characterization is $N{=}1$ (Qwen only, GRPO algorithm, 15\% contamination on MMLU); generalization to other model families, RL methods (PPO, DPO), and contamination levels requires further validation.
7	LLMs systematically violate IRT assumptions of local independence and unidimensionality; while the $\Delta\ell_z^*$ design mitigates shared misfit through within-model differencing, the theoretical properties of this correction under severe model misfit remain an open question.
8	The framework depends on pre-calibrated 4PL item parameters from PSN-IRT; parameter estimation errors propagate to $\ell_z^*$ computation, and the approach requires externally maintained parameter banks.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 329 · 2026-05-21T21:06:54.663535+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 330 · 2026-05-21T21:06:54.914812+00:00_

1	\section{Simulation Validation}
2	\label{app:simulation}
3	
4	Under the null (no contamination), bootstrap $\ell_z^*$ tracks $\mathcal{N}(0,1)$: mean bias 0.041 and standard deviation 1.003 on MMLU.
5	Kolmogorov--Smirnov rejection rates vary with benchmark size: 8.3\% for MMLU and HellaSwag ($n > 10{,}000$), 50.0\% for GSM8K ($n = 1{,}319$), 58.3\% for ARC-C ($n = 295$), and 75.0\% for HumanEval ($n = 164$).
6	$\ell_z^*$ is well-calibrated for benchmarks with $n \geq 10{,}000$ items; smaller benchmarks show increasing finite-sample deviations from normality.
7	
8	Two-sided testing eliminates the inverted-U artifact: MMLU achieves 97.8\% power at 15\% contamination and sustains ${>}$93\% at all levels.
9	Power scales with $\sqrt{n}$, as predicted by the noncentrality parameter $\delta \propto \sqrt{n}$.
10	The empirical power function, derived via Gauss--Hermite quadrature ($K=30$) over the ability distribution, achieves $R^2 = 0.957$ against simulated values, with approximate minimum benchmark size of $n \geq 7{,}958$ items for 80\% power at 15\% contamination under MMLU item parameters.
11	
12	\section{4PL vs.\ 3PL Ablation Details}
13	\label{app:4pl_ablation}
14	
15	Table~\ref{tab:4pl_3pl_power} reports detection power (proportion of 2{,}000 simulation replicates rejecting $H_0$ at $\alpha{=}0.05$, two-sided) for 4PL and 3PL parameterizations across five benchmarks and seven contamination levels.
16	The 4PL model yields higher power than 3PL at every non-trivial contamination level on every benchmark.
17	The advantage is largest on MMLU and HellaSwag, where upper-asymptote ($d < 1$) violations are most prevalent, and smallest on ARC-Challenge and HumanEval, where limited item counts constrain power under both parameterizations.
18	
19	Power is non-monotonic at 75\% contamination under 4PL on four of five benchmarks (e.g., MMLU: $.952 \to .938$; GSM8K: $.846 \to .802$).
20	This reflects the $\theta$-shift boundary condition described in \S\ref{sec:inverted_u}: at
…[truncated 14257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 331 · 2026-05-21T21:06:54.915144+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_personfit_contam",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 332 · 2026-05-21T21:06:54.965508+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'irt_personfit_contam'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 333 · 2026-05-21T21:07:01.490612+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 334 · 2026-05-21T21:07:04.000350+00:00_

{"result":"# 项目 irt_personfit_contam 概况\n\n## 实验状态 (78 个)\n\n- **exp-domain-analysis**: DONE (success) — \n- **exp-ml-classifier-baseline**: DONE (success) — \n- **exp-v1-irt-refit-pilot**: DONE (negative) — \n- **exp-clean-control-delta**: DONE (success) — \n- **exp-fdr-correction**: DONE (success) — \n- **exp-cross-benchmark-analysis**: DONE (success) — \n- **exp-accuracy-zscore-baseline**: DONE (success) — \n- **exp-item-alignment-check**: DONE (negative) — \n- **exp-power-theory**: DONE (success) — \n- **exp-empirical-null**: DONE (negative) — \n- **exp-leaderboard-data-recon**: DONE (success) — \n- **exp-extended-sim**: DONE (success) — \n- **exp-two-sided**: DONE (negative) — \n- **phase_b_personfit**: DONE (success) — \n- **sim_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-arcc-benchmark: ℓz* contamination detection generalizes beyond MMLU to ARC-Challenge, a second benchmark with PSN-IRT 4PL calibration — demonstrating cross-benchmark applicability and addressing reviewer concern about single-benchmark evaluation.（准备中）\n- arcc-clean-s10（准备中）\n- arcc-clean-s9（准备中）\n- arcc-clean-s8（准备中）\n- arcc-clean-s7（准备中）\n- exp-ctrl-contam-qwen-clean-s10: Tenth independent clean Qwen2.5-7B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation（准备中）\n- exp-constat-comparison: ConStat (NeurIPS 2024) requires multi-benchmark performance scores for contamination detection, making it inapplicable or underpowered in single-benchmark scenarios. ℓz* operates on binary response patterns from a single benchmark, demonstrating superior minimal-information detection capability.（准备中）\n- exp-arcc-clean-s1: ARC-Challenge clean baseline (seed=42) for cross-benchmark ℓz* detection — establishing clean lz* distribution on a second benchmark with PSN-IRT 4PL calibration（准备中）\n- exp-mia-mink-comparison: MIA methods (Min-K%/Min-K%++) fail to detect contamination in post-RL (GRPO) models because R
…[truncated 1160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2509
}
```

</details>

---


### Tool call

_source line 335 · 2026-05-21T21:07:04.353546+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib 2>/dev/null && wc -l /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib || echo \"NO_BIB\"",
  "description": "Check if references.bib exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib 2>/dev/null && wc -l /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib || echo \"NO_BIB\"",
    "description": "Check if references.bib exists"
  }
}
```

</details>

---


### Tool result

_source line 336 · 2026-05-21T21:07:04.805646+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib
351 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 337 · 2026-05-21T21:07:05.307864+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.pdf 2>/dev/null || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.pdf 2>/dev/null || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 338 · 2026-05-21T21:07:05.810142+00:00_

-rw-r--r-- 1 ubuntu ubuntu 460279 May 21 19:04 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 339 · 2026-05-21T21:07:06.262282+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 340 · 2026-05-21T21:07:07.667869+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 341 · 2026-05-21T21:07:07.818891+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml 2>/dev/null && cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml 2>/dev/null && cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 342 · 2026-05-21T21:07:07.869818+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml
## Review Issue Tracker — Round 2 (fresh review, 2026-05-21)

# ===== CRITICAL ISSUES =====

- id: "R2-N1"
  summary: "IRT 假设违反分析不充分，Δℓz* 有效性缺乏理论保证"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 2
  last_seen_round: 2
  mentions:
    - round: 2
      reviewers: [1, 2]
      note: "R1-N1 提出，R2 交叉 AGREE 并升级。污染可能改变 item 间依赖结构（memorized items 独立于 θ），导致 clean/contaminated 的 misfit 不对称，Δℓz* 差分假设失效。Appendix A 模拟 R²=0.957 假设 IRT 成立，构成循环论证。57/60 clean cells flagged 说明 IRT misfit 极严重，Δℓz* 承担极大校正负担。"
  action_items:
    - round: 2
      action: "Agent: testlet 模拟（引入 local dependence 后测 Δℓz* Type I error + power）; Paper Agent: 引用 Sinharay (2016), Magis et al. (2012) 讨论假设违反下鲁棒性; Limitations 增加 IRT 假设违反条目"
      assigned_to: agent+paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R2-N2"
  summary: "生态效度不足——QLoRA SFT 模拟污染 ≠ pretraining 污染"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 2
  last_seen_round: 2
  mentions:
    - round: 2
      reviewers: [1, 2]
      note: "R2-N1 提出，R1 交叉 AGREE。QLoRA (rank=16) 仅修改低秩 adapter，权重变化受限于低秩子空间，与 pretraining contamination 本质不同。Fine-tuning ≈ item preknowledge vs pretraining ≈ over-exposure，可能产生不同 aberrance pattern。所有四个 findings 的外推有效性存疑。"
  action_items:
    - round: 2
      action: "Paper Agent: Section 3.3 讨论 QLoRA 合理性+局限; findings 限定为 SFT-based; Limitations 增加 pretraining generalization caveat"
      assigned_to: paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R2-N3"
  summary: "Post-RL finding (N=1) 统计效力严重不足，Abstract overclaim"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 2
  last_seen_round: 2
  mentions:
    - round: 2
      reviewers: [1, 2]
      note: "R1-N3 和 R2-N2 独立提出，交叉完全一致。N=1 (Qwen, 15% MMLU, GRPO only)，Figure 4 无误差条。Abstra
…[truncated 10511 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 343 · 2026-05-21T21:07:15.245521+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 344 · 2026-05-21T21:07:15.647416+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 345 · 2026-05-21T21:07:15.647744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 346 · 2026-05-21T21:07:15.698374+00:00_

1	% =============================================================================
2	% references.bib — IRT Person-Fit Contamination Detection Paper
3	% Cleaned: 2026-05-21 | 33 entries (orphan entries removed)
4	% =============================================================================
5	
6	% =============================================================================
7	% Person-Fit Statistics (Psychometrics)
8	% =============================================================================
9	
10	@article{drasgow1985,
11	  title = {Appropriateness Measurement with Polychotomous Item Response Models and Standardized Indices},
12	  author = {Drasgow, F. and Levine, M. V. and Williams, E. A.},
13	  journal = {British Journal of Mathematical and Statistical Psychology},
14	  year = {1985},
15	  volume = {38},
16	  number = {1},
17	  pages = {67--86},
18	  doi = {10.1111/j.2044-8317.1985.tb00817.x},
19	}
20	
21	@article{karabatsos2003,
22	  title = {Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics},
23	  author = {Karabatsos, G.},
24	  journal = {Applied Measurement in Education},
25	  year = {2003},
26	  volume = {16},
27	  number = {4},
28	  pages = {277--298},
29	  doi = {10.1207/S15324818AME1604_2},
30	}
31	
32	@article{meijer2001,
33	  title = {Methodology Review: Evaluating Person Fit},
34	  author = {Meijer, R. R. and Sijtsma, K.},
35	  journal = {Applied Psychological Measurement},
36	  year = {2001},
37	  volume = {25},
38	  number = {2},
39	  pages = {107--135},
40	  doi = {10.1177/01466210122031957},
41	}
42	
43	@article{sinharay2017,
44	  title = {Which Statistic Should Be Used to Detect Item Preknowledge When the Set of Compromised Items Is Known?},
45	  author = {Sinharay, S.},
46	  journal = {Applied Psychological Measurement},
47	  year = {2017},
48	  doi = {10.1177/0146621617698453},
49	}
50	
51	@article{snijders2001,
52	  title = {Asymptotic Null Distribution of Person Fit Statistics with Estimated Person Pa
…[truncated 14216 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 347 · 2026-05-21T21:07:24.781598+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
  "description": "Find YAML config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
    "description": "Find YAML config files in project"
  }
}
```

</details>

---


### Tool result

_source line 348 · 2026-05-21T21:07:24.983050+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/sinharay2017.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/minkprob2024.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/wang2025fragility.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/psnirt2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/karabatsos2003.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/selfcritique2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/constat2024.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/atlas2025.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/hong2021lzm.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/codec2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/dream_registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/writing_plan.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/torchgen/packaged/ATen/native/native_functions.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/torchgen/packaged/ATen/native/tags.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/torchgen/packaged/autograd/derivatives.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/torchgen/packaged/autograd/deprecated.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-05
…[truncated 505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 349 · 2026-05-21T21:07:28.445948+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3 -maxdepth 3 -name \"config.yaml\" 2>/dev/null | grep -v \".venv\" | grep -v \"node_modules\"",
  "description": "Find config.yaml at top levels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3 -maxdepth 3 -name \"config.yaml\" 2>/dev/null | grep -v \".venv\" | grep -v \"node_modules\"",
    "description": "Find config.yaml at top levels"
  }
}
```

</details>

---


### Tool result

_source line 350 · 2026-05-21T21:07:28.546759+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 351 · 2026-05-21T21:07:31.563521+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3 -maxdepth 2 -name \"*.yaml\" 2>/dev/null | grep -v \".venv\" | grep -v \"node_modules\" | grep -i config",
  "description": "Find config YAML files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3 -maxdepth 2 -name \"*.yaml\" 2>/dev/null | grep -v \".venv\" | grep -v \"node_modules\" | grep -i config",
    "description": "Find config YAML files"
  }
}
```

</details>

---


### Tool result

_source line 352 · 2026-05-21T21:07:31.614414+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/config/crons.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/config/approvals.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/config/backend.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/config/feishu.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/config/resources.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 353 · 2026-05-21T21:07:34.726266+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/config/venue_registry.yaml 2>/dev/null | head -40",
  "description": "Read venue registry for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/config/venue_registry.yaml 2>/dev/null | head -40",
    "description": "Read venue registry for external review config"
  }
}
```

</details>

---


### Tool result

_source line 354 · 2026-05-21T21:07:35.579759+00:00_

venues:
  corl-2026:
    display_name: CoRL 2026
  emnlp-2026:
    display_name: EMNLP 2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 355 · 2026-05-21T21:07:35.580334+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/config/ 2>/dev/null",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/config/ 2>/dev/null",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 356 · 2026-05-21T21:07:35.631419+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 357 · 2026-05-21T21:08:08.057472+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_personfit_contam",
  "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_personfit_contam",
    "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209"
  }
}
```

</details>

---


### Tool result

_source line 358 · 2026-05-21T21:08:27.837707+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19780
}
```

</details>

---


### Tool call

_source line 359 · 2026-05-21T21:08:27.888273+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "irt_personfit_contam",
  "text": "你是 Reviewer 1，负责审查**方法严谨性、实验设计、统计推断**。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ACL Rolling Review 投稿）\n- **截止日期**：2026-05-25\n- **格式要求**：Long paper，正文 8 页上限，references 不限页，Limitations 不计入页数\n- **模板**：ACL style template（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n\n## 论文文件\n- LaTeX: `projects/irt_personfit_contam/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.pdf`\n- 各章节在 `projects/irt_personfit_contam/paper/sections/` 下\n\n## 你的审查重点\n\n1. **IRT 框架有效性**：4PL 模型假设（local independence, unidimensionality）在 LLM 上的违反程度及 Δℓz* 差分设计的理论保证。57/60 clean cells flagged 说明 misfit 极严重——Δℓz* 的差分假设是否成立？\n2. **实验设计严谨性**：\n   - QLoRA SFT 作为 contamination proxy 的生态效度（vs pretraining contamination）\n   - n=10 seeds (Qwen/Llama) vs n=6 (Mistral) 的统计效力是否足够\n   - 仅两个污染水平 (15%, 50%) 是否足以支撑 non-monotonic dose-response 结论\n   - Post-RL finding 的 N=1 设计是否足以作为 contribution\n3. **统计推断**：\n   - Cohen's d + bootstrap 95% CI 的使用是否恰当\n   - 参数扰动敏感性分析（Appendix）是否充分\n   - Fixed-θ vs free-θ 的比较是否公平\n4. **Detection-diagnosis tradeoff**：accuracy z-score |d|≈42-68 vs ℓz* |d|≈1.90，差距巨大——论文对 ℓz* 诊断价值的论证是否令人信服？\n5. **PSN-IRT 依赖**：single point of failure，参数估计误差的传播分析是否足够？\n\n请输出完整审稿报告，结构如下：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注严重级别：Must-Fix / Should-Fix / Minor)\n- Questions (需要作者澄清的)\n- Missing References\n- Overall Assessment (评分 + 理由)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "irt_personfit_contam",
    "text": "你是 Reviewer 1，负责审查**方法严谨性、实验设计、统计推断**。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ACL Rolling Review 投稿）\n- **截止日期**：2026-05-25\n- **格式要求**：Long paper，正文 8 页上限，references 不限页，Limitations 不计入页数\n- **模板**：ACL style template（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n\n## 论文文件\n- LaTeX: `projects/irt_personfit_contam/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.pdf`\n- 各章节在 `projects/irt_personfit_contam/paper/sections/` 下\n\n## 你的审查重点\n\n1. **IRT 框架有效性**：4PL 模型假设（local independence, unidimensionality）在 LLM 上的违反程度及 Δℓz* 差分设计的理论保证。57/60 clean cells flagged 说明 misfit 极严重——Δℓz* 的差分假设是否成立？\n2. **实验设计严谨性**：\n   - QLoRA SFT 作为 contamination proxy 的生态效度（vs pretraining contamination）\n   - n=10 seeds (Qwen/Llama) vs n=6 (Mistral) 的统计效力是否足够\n   - 仅两个污染水平 (15%, 50%) 是否足以支撑 non-monotonic dose-response 结论\n   - Post-RL finding 的 N=1 设计是否足以作为 contribution\n3. **统计推断**：\n   - Cohen's d + bootstrap 95% CI 的使用是否恰当\n   - 参数扰动敏感性分析（Appendix）是否充分\n   - Fixed-θ vs free-θ 的比较是否公平\n4. **Detection-diagnosis tradeoff**：accuracy z-score |d|≈42-68 vs ℓz* |d|≈1.90，差距巨大——论文对 ℓz* 诊断价值的论证是否令人信服？\n5. **PSN-IRT 依赖**：single point of failure，参数估计误差的传播分析是否足够？\n\n请输出完整审稿报告，结构如下：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注严重级别：Must-Fix / Should-Fix / Minor)\n- Questions (需要作者澄清的)\n- Missing References\n- Overall Assessment (评分 + 理由)"
  }
}
```

</details>

---


### Tool result

_source line 360 · 2026-05-21T21:08:42.762369+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14874
}
```

</details>

---


### Tool call

_source line 361 · 2026-05-21T21:08:42.863160+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "irt_personfit_contam",
  "text": "你是 Reviewer 2，负责审查**新颖性、完整性、Related Work 覆盖度、写作质量**。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ACL Rolling Review 投稿）\n- **截止日期**：2026-05-25\n- **格式要求**：Long paper，正文 8 页上限，references 不限页，Limitations 不计入页数\n- **模板**：ACL style template（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n\n## 论文文件\n- LaTeX: `projects/irt_personfit_contam/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.pdf`\n- 各章节在 `projects/irt_personfit_contam/paper/sections/` 下\n\n## 你的审查重点\n\n1. **新颖性评估**：\n   - \"首次将 IRT person-fit 统计量应用于 LLM 污染检测\" 是否属实？是否有未引用的相关工作？\n   - 四个 findings (non-monotonic dose-response, θ-shift dynamics, detection-diagnosis tradeoff, post-RL residual) 的新颖性程度——哪些可从 IRT 理论预测，哪些是真正的新发现？\n   - characterization paper 的贡献框架是否恰当？\n2. **Related Work 完整性**：\n   - 是否遗漏重要相关工作？特别关注：\n     - 其他 person-fit 统计量（U3, HT 变体、nonparametric methods）\n     - 近期 LLM contamination 检测方法（2025-2026）\n     - IRT 在 LLM 评估中的其他应用\n   - 33 篇引用对 EMNLP long paper 是否足够？\n3. **写作质量**：\n   - Abstract 是否准确反映论文内容？是否有 overclaim？\n   - 论文叙事结构是否清晰？Section 之间的逻辑流是否连贯？\n   - 术语使用一致性（ℓz*, Δℓz*, θ-shift 等）\n   - 图表质量和信息密度\n   - \"minimal-information point\" 的定位是否准确——fixed-θ 需 clean baseline，这与 minimal information 矛盾吗？\n4. **完整性**：\n   - 是否所有 claim 都有充分的实验/理论支撑？\n   - Limitations 是否涵盖所有重要局限？\n   - 是否有明显遗漏的实验（如 ConStat/MIA 实证对比）？\n5. **格式合规**：\n   - 正文是否在 8 页以内？\n   - 引用格式是否符合 ACL 规范？\n   - Anonymity 是否完整？\n\n请输出完整审稿报告，结构如下：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注严重级别：Must-Fix / Should-Fix / Minor)\n- Questions (需要作者澄清的)\n- Missing References\n- Overall Assessment (评分 + 理由)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "irt_personfit_contam",
    "text": "你是 Reviewer 2，负责审查**新颖性、完整性、Related Work 覆盖度、写作质量**。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ACL Rolling Review 投稿）\n- **截止日期**：2026-05-25\n- **格式要求**：Long paper，正文 8 页上限，references 不限页，Limitations 不计入页数\n- **模板**：ACL style template（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n\n## 论文文件\n- LaTeX: `projects/irt_personfit_contam/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.pdf`\n- 各章节在 `projects/irt_personfit_contam/paper/sections/` 下\n\n## 你的审查重点\n\n1. **新颖性评估**：\n   - \"首次将 IRT person-fit 统计量应用于 LLM 污染检测\" 是否属实？是否有未引用的相关工作？\n   - 四个 findings (non-monotonic dose-response, θ-shift dynamics, detection-diagnosis tradeoff, post-RL residual) 的新颖性程度——哪些可从 IRT 理论预测，哪些是真正的新发现？\n   - characterization paper 的贡献框架是否恰当？\n2. **Related Work 完整性**：\n   - 是否遗漏重要相关工作？特别关注：\n     - 其他 person-fit 统计量（U3, HT 变体、nonparametric methods）\n     - 近期 LLM contamination 检测方法（2025-2026）\n     - IRT 在 LLM 评估中的其他应用\n   - 33 篇引用对 EMNLP long paper 是否足够？\n3. **写作质量**：\n   - Abstract 是否准确反映论文内容？是否有 overclaim？\n   - 论文叙事结构是否清晰？Section 之间的逻辑流是否连贯？\n   - 术语使用一致性（ℓz*, Δℓz*, θ-shift 等）\n   - 图表质量和信息密度\n   - \"minimal-information point\" 的定位是否准确——fixed-θ 需 clean baseline，这与 minimal information 矛盾吗？\n4. **完整性**：\n   - 是否所有 claim 都有充分的实验/理论支撑？\n   - Limitations 是否涵盖所有重要局限？\n   - 是否有明显遗漏的实验（如 ConStat/MIA 实证对比）？\n5. **格式合规**：\n   - 正文是否在 8 页以内？\n   - 引用格式是否符合 ACL 规范？\n   - Anonymity 是否完整？\n\n请输出完整审稿报告，结构如下：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注严重级别：Must-Fix / Should-Fix / Minor)\n- Questions (需要作者澄清的)\n- Missing References\n- Overall Assessment (评分 + 理由)"
  }
}
```

</details>

---


### Tool result

_source line 362 · 2026-05-21T21:08:44.277495+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1414
}
```

</details>

---


### Assistant

_source line 363 · 2026-05-21T21:09:02.709089+00:00_

Round 1 已启动：

- **视觉审查 Agent**：已派发（fire-and-forget）
- **Reviewer 1**（方法严谨性 + 实验设计）：已分配
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）：已分配

等待两位 Reviewer 返回独立审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 37

## Round 37

2 recorded events


### User

_source line 364 · 2026-05-21T21:14:04.865707+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告

### 论文信息
- **标题**: What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization
- **Venue**: EMNLP 2026 (via ACL Rolling Review)

---

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 将心理测量 person-fit 统计量引入 LLM 污染检测是新颖且有意义的 framing，方法论严谨，但实用价值受限——论文自身实验已表明更简单统计量在检测力上全面优于 ℓz*，且实验范围（3 个 7-8B 模型、2 个 benchmark、仅 SFT 污染）偏窄。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | DiD 设计巧妙，bootstrap CI 严格；但 n=6/10 seeds 偏小，部分 CI 极宽（Qwen MMLU 15%: [-15.2, -4.5]）；Post-RL N=1 过于初步 |
| Excitement | 2.5/5 | 跨学科 framing 有新意，但多数发现可从 IRT 理论预测（θ-shift absorption 是教科书知识），且 ℓz* 在检测力上被 accuracy z-score 碾压 |
| Reproducibility | 4/5 | 使用公开 PSN-IRT item bank，报告所有超参数和 seed，承诺 release code；Mistral 丢失 4 个 seed 是小扣分 |
| Overall | 3.5/5 | 方法论扎实的 characterization paper，适合 Findings；距主会议差在实验规模和实用影响力 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] "Minimal-information point" 定位与实际需求矛盾
- 具体位置：Abstract (line 2)、Section 1 (line 13)、Related Work "Our approach operates at the minimal information point: binary responses only"
- 问题：论文反复强调只需 binary response patterns，但实际框架强依赖外部校准的 4PL item parameters（PSN-IRT, 基于 13,000+ 模型的 leaderboard 数据）。Fixed-θ estimation 还需 clean baseline。4PL item bank 本身是对 item population 的大量先验知识。Related Work 直接说 "binary responses only" 是 overclaim。
- 建议：区分 "来自 target model 的信息是 minimal" 和 "来自 item bank 的外部信息是 substantial"，将 framing 改为 "minimal information from the target model"。

**N2** [critical] 缺少与现有检测方法的实证对比
- 具体位置：Section 4.4 (Table 3)、Section 5
- 问题：仅在自己的三种统计量之间对比，完全没有与 ConStat、Min-K% Prob、CoDeC 等现有方法的实证比较。Discussion 仅一句话概念性提及 ConStat。作为 characterization paper，至少应在相同设置下跑 ConStat baseline。
- 建议：加入 ConStat 实证对比；如不可行，至少给出定性分析说明 ℓz* 的 diagnostic 能力何时优于 ConStat。

**N3** [critical] 实验规模偏窄，削弱 generalization claims
- 具体位置：Section 3.3、Limitations
- 问题：仅 3 个 7-8B 模型、2 个 benchmark、2 个非零污染水平、仅 QLoRA SFT 污染。"baseline ability 与 detection sensitivity 负相关" 仅基于 3 个数据点。ARC-C 上只有 Qwen 结果。标题/abstract 措辞暗示泛化性，但 scope 仅限 SFT 污染一隅。
- 建议：增加 1-2 个模型规模；补齐 ARC-C；增加中间污染水平（5%, 25%）；标题/abstract 明确 scope 为 SFT-stage。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Post-RL 发现 (Finding 4) 作为主要 contribution 过于薄弱
- N=1（单一模型 Qwen，单一 RL 方法 GRPO，单一污染水平 15%），无统计推断，但仍被列为 Abstract 四大发现之一和 Conclusion 主要贡献。
- 建议：降级为 preliminary observation 并从 Abstract 列表移除，或增加实验覆盖。

**W2** [warning] 四个 findings 中两个可从 IRT 理论直接预测
- θ-shift absorption 是 IRT 能力估计的标准行为；baseline ability 与 detection sensitivity 的关系本质是 ceiling effect 变体。论文将其呈现为 empirical discoveries，实际更接近 empirical confirmation of theory。
- 建议：承认理论可预测性，将 contribution 重新框架为 "首次在 LLM 场景下量化这些 IRT-predicted 行为的具体边界"。

**W3** [warning] Bootstrap CI 宽度和样本量问题
- 部分 CI 极宽（跨度达 10+），Mistral 仅 n=6 seeds。Llama fixed-θ 15% 的 CI 包含零（不显著）。
- 建议：增加 seeds 数量至 n≥20。

**W4** [warning] Related Work 遗漏若干相关方法
- 遗漏 PaCoST (EMNLP 2024 Findings)、Data Contamination Calibration for Black-box LLMs (2024)、Watermarking-based detection (2025)、MEDIRT (2025)、Don't Make Your LLM an Evaluation Benchmark Cheater (2023)
- 未解释为何从 36 种 person-fit 统计量中仅选 ℓz* 和 HT
- 36 篇引用偏少

**W5** [warning] Abstract 过长（~250 词），前端过载具体数字
- 建议精简至 150-180 词。

## 小问题（不影响接收）
- M1: r_a=0.127 的 MML-EM refit 实验设置未在正文或 appendix 描述
- M2: Figure 1 "red diamonds" 灰度打印不可见
- M3: Mistral seed 丢失原因表述过于口语化
- M4: Conclusion 仅一句话，过于简略
- M5: Table 1 中 MMLU (负值) vs ARC-C (正值) 的 Cohen's d 符号差异缺乏表内注释

## Questions
1. 为什么不使用更多 person-fit 统计量？Karabatsos (2003) 比较了 36 种，选择 ℓz* + HT 的理由是什么？
2. PSN-IRT 的 4PL 参数校准中是否包含本实验模型系列的变体？
3. Cross-benchmark comparison 替代 clean baseline 方案有实验验证吗？
4. Non-monotonic dose-response 仅基于两个非零水平，如何确认真正存在反转？
5. Post-RL 中 ℓz* 从 2.91 增至 7.69——GRPO 是否引入新的 aberrance 而非保留 contamination signal？

## Missing References
1. PaCoST (EMNLP 2024 Findings)
2. Data Contamination Calibration for Black-box LLMs (arXiv 2405.11930)
3. Detecting Benchmark Contamination Through Watermarking (arXiv 2502.17259)
4. MEDIRT: Measuring Competency, Not Performance (arXiv 2509.24186)
5. How Much Can We Forget about Data Contamination? (arXiv 2410.03249)
6. Don't Make Your LLM an Evaluation Benchmark Cheater (Zhou et al., 2023)

## 主要优势
- S1: 跨学科贡献清晰——psychometric person-fit → LLM evaluation 是自然且未被探索的连接
- S2: 方法论严谨——DiD 设计巧妙处理 IRT 假设违反，Appendix robustness analysis 充分
- S3: 诚实的 self-assessment——坦诚展示 accuracy z-scores 的压倒性检测优势，将 ℓz* 价值定位于 diagnosis
- S4: Detection-diagnosis tradeoff 有实用价值，two-stage workflow 清晰可操作
- S5: 写作整体清晰，图表信息密度高

## 格式合规
- ✅ 正文 8 页（Conclusion 在 page 8 结束）
- ✅ \usepackage[review]{acl}
- ✅ Double-blind (Anonymous ACL submission)
- ✅ Limitations section 存在且合理
- ✅ References 格式符合 ACL 规范
- ⚠️ 引用数量偏少（36 篇）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 365 · 2026-05-21T21:14:11.896599+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 38

## Round 38

2 recorded events


### User

_source line 366 · 2026-05-21T21:14:20.560293+00:00_

[Reviewer 2 审稿结果]:
审稿报告已完成并提交给 Review Director。

**核心判断**：Overall 3.5（Borderline Conference），推荐 Findings。

三个 Must-Fix 问题：
1. "Minimal-information point" framing 与实际依赖 4PL item bank 矛盾——overclaim
2. 缺少与 ConStat 等现有方法的实证对比
3. 实验规模偏窄（3 个 7-8B 模型、仅 SFT 污染），标题/abstract 的泛化性措辞超出实验 scope

主要优势在于跨学科连接的新颖性、DiD 设计的方法论严谨性、以及 detection-diagnosis tradeoff 的实用洞察。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 367 · 2026-05-21T21:14:25.621551+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 39

## Round 39

6 recorded events


### User

_source line 368 · 2026-05-21T21:15:49.080713+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性、实验设计、统计推断

### 论文信息
- **标题**: What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization
- **Venue**: EMNLP 2026 (via ACL Rolling Review)

---

## 总体评分

**Overall**: 3.5 — Borderline Conference

**一句话总结**: 将心理测量 person-fit 统计量首次系统性地应用于 LLM 污染检测是新颖且有洞察力的贡献，但"剂量-反应"表征仅基于两个污染水平、QLoRA SFT 的生态效度有限、以及 N=1 的 post-RL 结果被高估为核心 contribution，削弱了整体说服力。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心 claim (Δℓz* 可靠检测 SFT 污染) 有 Table 1 的 CI 支撑；但"non-monotonic dose-response"仅基于 2 个污染水平无法确立曲线形态；DiD 假设在 IRT 严重违反下的理论保证讨论不足 |
| Excitement | 3.5/5 | IRT person-fit → LLM 污染检测的跨学科连接真正新颖；θ-shift absorption 机制有洞察力。但实际检测力远弱于简单 accuracy z-score (10-36×)，实际应用价值存疑 |
| Reproducibility | 4/5 | 实验设置清晰，代码和数据承诺 release，但 PSN-IRT 参数的外部依赖可能影响完全重现 |
| Confidence | 4/5 | 熟悉 IRT 框架和 LLM 评估方法论 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 仅两个污染水平 (15%, 50%) 不足以支撑 "dose-response characterization"

Section 4.2: 论文将 "non-monotonic dose-response" 列为四大发现之首。但 dose-response 关系的经验刻画至少需要 3-4 个剂量水平。仅有两个非零水平时，只能说 "Qwen 在 15% 的 |d| 大于 50%"——这是观察而非曲线刻画。Qwen 15% CI=[-15.2,-4.5] 和 50% CI=[-5.0,-1.0] 存在重叠，两个水平间差异未经正式统计检验。Mistral 和 Llama 实际是单调或近单调的 (Section 4.2 line 54-56)，说明非单调性是模型特异的。QLoRA 微调 7B 模型成本极低，补充 5%/10%/25%/30% 水平完全可行。

**N2** [critical] QLoRA SFT 生态效度与论文的 pretraining contamination 动机脱节

Introduction 以 pretraining contamination 为动机 (line 3-6)，但方法使用 QLoRA SFT (rank=16, α=32) 作为代理。SFT 在低秩空间产生的集中记忆化信号远强于 pretraining 的分布式嵌入。论文报告的高 Cohen's d (Qwen 15% |d|=6.58) 可能反映 SFT 特有效应。Section 3.3 line 57-58 的 scoping 是负责任的，但 Introduction 叙事未对齐。

**N3** [critical] Mistral n=6 seeds 统计效力不足且未补充

因服务器退役丢失 4/10 checkpoints (Section 3.3 line 46)。n=6 bootstrap CI 更宽且更不可靠。Table 2 中 Mistral fixed-θ CI 跨度达 [1.45, 9.00]——约束力极低。QLoRA 微调成本极低，补跑完全可行。

---

## Should-Fix 问题

**W1** [warning] Post-RL finding N=1 不应列为核心 contribution

Section 4.5 的 caveat 充分，但 Abstract/Introduction 将其与 n=10 控制实验并列为四大发现。单一模型×单一 RL 方法×单一污染水平×无统计推断。且 ℓz* 从 2.91 增至 7.69 更像 θ-shift 效应而非 "residual contamination pattern"。

**W2** [warning] ℓz* 的诊断价值论证中 item-level AUROC=0.53 近乎随机

Table 3 中 accuracy z-score |d| 是 ℓz* 的 10-36×。ℓz* 的三个"诊断优势"中：seen/unseen decomposition 的 item-level AUROC=0.53 (Table 8) 接近随机；θ-shift insight 是框架理论而非实操工具；structural sensitivity (57/60 flagged) 反映 IRT 误设。

**W3** [warning] PSN-IRT 参数循环依赖风险

PSN-IRT 基于可能受 contamination 影响的 leaderboard 数据校准。Appendix F 的扰动分析用高斯噪声，但真实偏差可能是结构性的。无替代校准方法对照。

**W4** [warning] Llama/Mistral 缺失 ARC-C 数据，削弱跨 benchmark 泛化

Table 1 仅 Qwen 有 ARC-C。Section 4.3 的 ceiling effect 讨论无 Llama/Mistral 对照。

**W5** [warning] Bootstrap CI 方法类型未说明，小样本下可能 anti-conservative

未区分 percentile/BCa。Appendix C 中 n=3 的 analytic CI 跨零而 bootstrap CI 不跨，可解释为小样本 bootstrap anti-conservatism。

---

## Questions

1. 为何不增加中间污染水平？QLoRA 成本极低。
2. "57/60 model-benchmark cells" 的 60 具体构成？
3. Fixed-θ 的 clean-model mean anchor 在实际部署中不可得——cross-benchmark θ estimation 是否有实验评估？
4. GRPO 后 ℓz* 从 2.91 增至 7.69，与 "residual contamination pattern" 叙事如何一致？
5. Llama/Mistral 为何未评估 ARC-C？
6. Bootstrap 用 percentile 还是 BCa？

---

## Missing References

- Reise (1990) person-fit 作弊检测；Levine & Drasgow (1988) appropriateness indices 分类；Embretson & Reise (2000) IRT 教科书

---

## 主要优势

1. 真正新颖的跨学科连接——psychometric person-fit → LLM contamination detection
2. 诚实定位为 characterization 而非 tool
3. θ-shift absorption 机制洞察力强，fixed-θ 验证有力 (Table 2: |d| 1.90→14.52)
4. DiD 设计优雅处理 57/60 baseline misfit，模拟验证充分 (Appendix A-E)
5. 附录异常充实，每个方法论质疑都有对应分析

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 369 · 2026-05-21T21:16:45.060126+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "irt_personfit_contam",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告（完整原文）\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: 将心理测量 person-fit 统计量引入 LLM 污染检测是新颖且有意义的 framing，方法论严谨，但实用价值受限——论文自身实验已表明更简单统计量在检测力上全面优于 ℓz*，且实验范围（3 个 7-8B 模型、2 个 benchmark、仅 SFT 污染）偏窄。\n\n## Must-Fix 问题\n\n**N1** [critical] \"Minimal-information point\" 定位与实际需求矛盾\n- Abstract (line 2)、Section 1 (line 13)、Related Work \"Our approach operates at the minimal information point: binary responses only\"\n- 论文反复强调只需 binary response patterns，但实际框架强依赖外部校准的 4PL item parameters（PSN-IRT, 基于 13,000+ 模型的 leaderboard 数据）。Fixed-θ 还需 clean baseline。4PL item bank 本身是对 item population 的大量先验知识。Related Work 直接说 \"binary responses only\" 是 overclaim。\n- 建议：区分 \"来自 target model 的信息是 minimal\" 和 \"来自 item bank 的外部信息是 substantial\"，将 framing 改为 \"minimal information from the target model\"。\n\n**N2** [critical] 缺少与现有检测方法的实证对比\n- Section 4.4 (Table 3)、Section 5\n- 仅在自己的三种统计量之间对比，完全没有与 ConStat、Min-K% Prob、CoDeC 等现有方法的实证比较。Discussion 仅一句话概念性提及 ConStat。\n- 建议：加入 ConStat 实证对比。\n\n**N3** [critical] 实验规模偏窄，削弱 generalization claims\n- 仅 3 个 7-8B 模型、2 个 benchmark、2 个非零污染水平、仅 QLoRA SFT 污染。\"baseline ability 与 detection sensitivity 负相关\" 仅基于 3 个数据点。ARC-C 上只有 Qwen 结果。标题/abstract 措辞暗示泛化性，但 scope 仅限 SFT 污染一隅。\n- 建议：增加 1-2 个模型规模；补齐 ARC-C；增加中间污染水平。\n\n## Should-Fix 问题\n\n**W1** [warning] Post-RL 发现 (Finding 4) 作为主要 contribution 过于薄弱\n- N=1（Qwen, GRPO, 15%），无统计推断，但列为 Abstract 四大发现之一。\n- 建议：降级为 preliminary observation。\n\n**W2** [warning] 四个 findings 中两个可从 IRT 理论直接预测\n- θ-shift absorption 是 IRT 能力估计标准行为；baseline ability 与 detection sensitivity 关系是 ceiling effect 变体。\n- 建议：承认理论可预测性，框架为 \"首次在 LLM 场景下量化边界\"。\n\n**W3** [warning] Bootstrap CI 宽度和样本量问题\n- 部分 CI 极宽（跨度达 10+），Mistral 仅 n=6。Llama fixed-θ 15% CI 包含零。\n- 建议：增加 seeds 至 n≥20。\n\n**W4** [warning] Related Work 遗漏若干相关方法\n- 遗漏 PaCoST, Data Contamination Calibration, Watermarking-based detection, MEDIRT, Don't Make Your LLM an Evaluation Benchmark Cheater\n- 未解释从 36 种 person-fit 统计量中仅选 ℓz* 和 HT 的理由\n- 36 篇引用偏少\n\n**W5** [warning] Abstract 过长（~250 词），前端过载具体数字\n\n## Questions\n1. 为什么不使用更多 person-fit 统计量？\n2. PSN-IRT 的 4PL 参数校准中是否包含本实验模型系列的变体？\n3. Cross-benchmark comparison 替代 clean baseline 方案有实验验证吗？\n4. Non-monotonic dose-response 仅基于两个非零水平，如何确认真正存在反转？\n5. Post-RL 中 ℓz* 从 2.91 增至 7.69——GRPO 是否引入新的 aberrance 而非保留 contamination signal？\n\n## Missing References\n1. PaCoST (EMNLP 2024 Findings)\n2. Data Contamination Calibration for Black-box LLMs\n3. Detecting Benchmark Contamination Through Watermarking\n4. MEDIRT\n5. How Much Can We Forget about Data Contamination?\n6. Don't Make Your LLM an Evaluation Benchmark Cheater\n\n## 主要优势\n- S1: 跨学科贡献清晰\n- S2: 方法论严谨\n- S3: 诚实的 self-assessment\n- S4: Detection-diagnosis tradeoff 有实用价值\n- S5: 写作整体清晰"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "irt_personfit_contam",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告（完整原文）\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: 将心理测量 person-fit 统计量引入 LLM 污染检测是新颖且有意义的 framing，方法论严谨，但实用价值受限——论文自身实验已表明更简单统计量在检测力上全面优于 ℓz*，且实验范围（3 个 7-8B 模型、2 个 benchmark、仅 SFT 污染）偏窄。\n\n## Must-Fix 问题\n\n**N1** [critical] \"Minimal-information point\" 定位与实际需求矛盾\n- Abstract (line 2)、Section 1 (line 13)、Related Work \"Our approach operates at the minimal information point: binary responses only\"\n- 论文反复强调只需 binary response patterns，但实际框架强依赖外部校准的 4PL item parameters（PSN-IRT, 基于 13,000+ 模型的 leaderboard 数据）。Fixed-θ 还需 clean baseline。4PL item bank 本身是对 item population 的大量先验知识。Related Work 直接说 \"binary responses only\" 是 overclaim。\n- 建议：区分 \"来自 target model 的信息是 minimal\" 和 \"来自 item bank 的外部信息是 substantial\"，将 framing 改为 \"minimal information from the target model\"。\n\n**N2** [critical] 缺少与现有检测方法的实证对比\n- Section 4.4 (Table 3)、Section 5\n- 仅在自己的三种统计量之间对比，完全没有与 ConStat、Min-K% Prob、CoDeC 等现有方法的实证比较。Discussion 仅一句话概念性提及 ConStat。\n- 建议：加入 ConStat 实证对比。\n\n**N3** [critical] 实验规模偏窄，削弱 generalization claims\n- 仅 3 个 7-8B 模型、2 个 benchmark、2 个非零污染水平、仅 QLoRA SFT 污染。\"baseline ability 与 detection sensitivity 负相关\" 仅基于 3 个数据点。ARC-C 上只有 Qwen 结果。标题/abstract 措辞暗示泛化性，但 scope 仅限 SFT 污染一隅。\n- 建议：增加 1-2 个模型规模；补齐 ARC-C；增加中间污染水平。\n\n## Should-Fix 问题\n\n**W1** [warning] Post-RL 发现 (Finding 4) 作为主要 contribution 过于薄弱\n- N=1（Qwen, GRPO, 15%），无统计推断，但列为 Abstract 四大发现之一。\n- 建议：降级为 preliminary observation。\n\n**W2** [warning] 四个 findings 中两个可从 IRT 理论直接预测\n- θ-shift absorption 是 IRT 能力估计标准行为；baseline ability 与 detection sensitivity 关系是 ceiling effect 变体。\n- 建议：承认理论可预测性，框架为 \"首次在 LLM 场景下量化边界\"。\n\n**W3** [warning] Bootstrap CI 宽度和样本量问题\n- 部分 CI 极宽（跨度达 10+），Mistral 仅 n=6。Llama fixed-θ 15% CI 包含零。\n- 建议：增加 seeds 至 n≥20。\n\n**W4** [warning] Related Work 遗漏若干相关方法\n- 遗漏 PaCoST, Data Contamination Calibration, Watermarking-based detection, MEDIRT, Don't Make Your LLM an Evaluation Benchmark Cheater\n- 未解释从 36 种 person-fit 统计量中仅选 ℓz* 和 HT 的理由\n- 36 篇引用偏少\n\n**W5** [warning] Abstract 过长（~250 词），前端过载具体数字\n\n## Questions\n1. 为什么不使用更多 person-fit 统计量？\n2. PSN-IRT 的 4PL 参数校准中是否包含本实验模型系列的变体？\n3. Cross-benchmark comparison 替代 clean baseline 方案有实验验证吗？\n4. Non-monotonic dose-response 仅基于两个非零水平，如何确认真正存在反转？\n5. Post-RL 中 ℓz* 从 2.91 增至 7.69——GRPO 是否引入新的 aberrance 而非保留 contamination signal？\n\n## Missing References\n1. PaCoST (EMNLP 2024 Findings)\n2. Data Contamination Calibration for Black-box LLMs\n3. Detecting Benchmark Contamination Through Watermarking\n4. MEDIRT\n5. How Much Can We Forget about Data Contamination?\n6. Don't Make Your LLM an Evaluation Benchmark Cheater\n\n## 主要优势\n- S1: 跨学科贡献清晰\n- S2: 方法论严谨\n- S3: 诚实的 self-assessment\n- S4: Detection-diagnosis tradeoff 有实用价值\n- S5: 写作整体清晰"
  }
}
```

</details>

---


### Tool result

_source line 370 · 2026-05-21T21:17:08.102491+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23042
}
```

</details>

---


### Tool call

_source line 371 · 2026-05-21T21:17:08.254616+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "irt_personfit_contam",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告（完整原文）\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: 将心理测量 person-fit 统计量首次系统性地应用于 LLM 污染检测是新颖且有洞察力的贡献，但\"剂量-反应\"表征仅基于两个污染水平、QLoRA SFT 的生态效度有限、以及 N=1 的 post-RL 结果被高估为核心 contribution，削弱了整体说服力。\n\n## Must-Fix 问题\n\n**N1** [critical] 仅两个污染水平 (15%, 50%) 不足以支撑 \"dose-response characterization\"\n- Section 4.2: \"non-monotonic dose-response\" 列为四大发现之首，但仅有两个非零水平。只能说 \"Qwen 在 15% 的 |d| 大于 50%\"——观察而非曲线刻画。Qwen 15% CI=[-15.2,-4.5] 和 50% CI=[-5.0,-1.0] 存在重叠。Mistral 和 Llama 是单调的。QLoRA 补充中间水平完全可行。\n\n**N2** [critical] QLoRA SFT 生态效度与论文的 pretraining contamination 动机脱节\n- Introduction 以 pretraining contamination 为动机 (line 3-6)，但使用 QLoRA SFT (rank=16, α=32) 作代理。SFT 在低秩空间的集中记忆化信号远强于 pretraining 分布式嵌入。论文高 Cohen's d (Qwen 15% |d|=6.58) 可能反映 SFT 特有效应。Section 3.3 scoping 负责任但 Introduction 叙事未对齐。\n\n**N3** [critical] Mistral n=6 seeds 统计效力不足且未补充\n- 因服务器退役丢失 4/10 checkpoints (Section 3.3 line 46)。n=6 bootstrap CI 更宽。Table 2 Mistral fixed-θ CI 跨度 [1.45, 9.00]。QLoRA 成本极低，应补跑。\n\n## Should-Fix 问题\n\n**W1** [warning] Post-RL finding N=1 不应列为核心 contribution\n- Section 4.5 caveat 充分，但 Abstract/Introduction 将其与 n=10 并列为四大发现。单一模型×单一 RL 方法×无统计推断。ℓz* 从 2.91 增至 7.69 更像 θ-shift 效应。\n\n**W2** [warning] ℓz* 的诊断价值论证中 item-level AUROC=0.53 近乎随机\n- accuracy z-score |d| 是 ℓz* 的 10-36×。三个\"诊断优势\"中：seen/unseen decomposition item-level AUROC=0.53 接近随机；θ-shift insight 是框架理论；structural sensitivity (57/60) 反映 IRT 误设。\n\n**W3** [warning] PSN-IRT 参数循环依赖风险\n- PSN-IRT 基于可能受 contamination 影响的 leaderboard 数据校准。Appendix F 扰动分析用高斯噪声，但真实偏差可能是结构性的。\n\n**W4** [warning] Llama/Mistral 缺失 ARC-C 数据\n- Table 1 仅 Qwen 有 ARC-C。Section 4.3 的 ceiling effect 讨论无 Llama/Mistral 对照。\n\n**W5** [warning] Bootstrap CI 方法类型未说明\n- 未区分 percentile/BCa。Appendix C 中 n=3 的 analytic CI 跨零而 bootstrap CI 不跨，可能反映小样本 anti-conservatism。\n\n## Questions\n1. 为何不增加中间污染水平？\n2. \"57/60 model-benchmark cells\" 的 60 具体构成？\n3. Fixed-θ 的 clean-model mean anchor 在部署中不可得——cross-benchmark θ estimation 是否有实验评估？\n4. GRPO 后 ℓz* 从 2.91 增至 7.69 与 \"residual contamination pattern\" 叙事如何一致？\n5. Llama/Mistral 为何未评估 ARC-C？\n6. Bootstrap 用 percentile 还是 BCa？\n\n## Missing References\n- Reise (1990) person-fit 作弊检测\n- Levine &amp; Drasgow (1988) appropriateness indices 分类\n- Embretson &amp; Reise (2000) IRT 教科书\n\n## 主要优势\n1. 真正新颖的跨学科连接\n2. 诚实定位为 characterization 而非 tool\n3. θ-shift absorption 机制洞察力强\n4. DiD 设计优雅处理 baseline misfit\n5. 附录异常充实"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "irt_personfit_contam",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告（完整原文）\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: 将心理测量 person-fit 统计量首次系统性地应用于 LLM 污染检测是新颖且有洞察力的贡献，但\"剂量-反应\"表征仅基于两个污染水平、QLoRA SFT 的生态效度有限、以及 N=1 的 post-RL 结果被高估为核心 contribution，削弱了整体说服力。\n\n## Must-Fix 问题\n\n**N1** [critical] 仅两个污染水平 (15%, 50%) 不足以支撑 \"dose-response characterization\"\n- Section 4.2: \"non-monotonic dose-response\" 列为四大发现之首，但仅有两个非零水平。只能说 \"Qwen 在 15% 的 |d| 大于 50%\"——观察而非曲线刻画。Qwen 15% CI=[-15.2,-4.5] 和 50% CI=[-5.0,-1.0] 存在重叠。Mistral 和 Llama 是单调的。QLoRA 补充中间水平完全可行。\n\n**N2** [critical] QLoRA SFT 生态效度与论文的 pretraining contamination 动机脱节\n- Introduction 以 pretraining contamination 为动机 (line 3-6)，但使用 QLoRA SFT (rank=16, α=32) 作代理。SFT 在低秩空间的集中记忆化信号远强于 pretraining 分布式嵌入。论文高 Cohen's d (Qwen 15% |d|=6.58) 可能反映 SFT 特有效应。Section 3.3 scoping 负责任但 Introduction 叙事未对齐。\n\n**N3** [critical] Mistral n=6 seeds 统计效力不足且未补充\n- 因服务器退役丢失 4/10 checkpoints (Section 3.3 line 46)。n=6 bootstrap CI 更宽。Table 2 Mistral fixed-θ CI 跨度 [1.45, 9.00]。QLoRA 成本极低，应补跑。\n\n## Should-Fix 问题\n\n**W1** [warning] Post-RL finding N=1 不应列为核心 contribution\n- Section 4.5 caveat 充分，但 Abstract/Introduction 将其与 n=10 并列为四大发现。单一模型×单一 RL 方法×无统计推断。ℓz* 从 2.91 增至 7.69 更像 θ-shift 效应。\n\n**W2** [warning] ℓz* 的诊断价值论证中 item-level AUROC=0.53 近乎随机\n- accuracy z-score |d| 是 ℓz* 的 10-36×。三个\"诊断优势\"中：seen/unseen decomposition item-level AUROC=0.53 接近随机；θ-shift insight 是框架理论；structural sensitivity (57/60) 反映 IRT 误设。\n\n**W3** [warning] PSN-IRT 参数循环依赖风险\n- PSN-IRT 基于可能受 contamination 影响的 leaderboard 数据校准。Appendix F 扰动分析用高斯噪声，但真实偏差可能是结构性的。\n\n**W4** [warning] Llama/Mistral 缺失 ARC-C 数据\n- Table 1 仅 Qwen 有 ARC-C。Section 4.3 的 ceiling effect 讨论无 Llama/Mistral 对照。\n\n**W5** [warning] Bootstrap CI 方法类型未说明\n- 未区分 percentile/BCa。Appendix C 中 n=3 的 analytic CI 跨零而 bootstrap CI 不跨，可能反映小样本 anti-conservatism。\n\n## Questions\n1. 为何不增加中间污染水平？\n2. \"57/60 model-benchmark cells\" 的 60 具体构成？\n3. Fixed-θ 的 clean-model mean anchor 在部署中不可得——cross-benchmark θ estimation 是否有实验评估？\n4. GRPO 后 ℓz* 从 2.91 增至 7.69 与 \"residual contamination pattern\" 叙事如何一致？\n5. Llama/Mistral 为何未评估 ARC-C？\n6. Bootstrap 用 percentile 还是 BCa？\n\n## Missing References\n- Reise (1990) person-fit 作弊检测\n- Levine &amp; Drasgow (1988) appropriateness indices 分类\n- Embretson &amp; Reise (2000) IRT 教科书\n\n## 主要优势\n1. 真正新颖的跨学科连接\n2. 诚实定位为 characterization 而非 tool\n3. θ-shift absorption 机制洞察力强\n4. DiD 设计优雅处理 baseline misfit\n5. 附录异常充实"
  }
}
```

</details>

---


### Tool result

_source line 372 · 2026-05-21T21:17:09.664494+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1409
}
```

</details>

---


### Assistant

_source line 373 · 2026-05-21T21:17:13.366646+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 40

## Round 40

2 recorded events


### User

_source line 374 · 2026-05-21T21:17:15.921057+00:00_

[Reviewer 1 审稿结果]:
审稿完成。总结：

- **Overall 3.5 (Borderline Conference)**，IRT person-fit 应用于 LLM 污染检测的跨学科连接新颖，θ-shift absorption 机制分析有深度
- **3 个 Must-Fix**：(1) 仅 2 个污染水平不足以支撑 "dose-response characterization" 的核心 claim；(2) QLoRA SFT 生态效度与 Introduction 的 pretraining contamination 动机脱节；(3) Mistral n=6 seeds 因丢失 checkpoints 导致统计效力不足
- **5 个 Should-Fix**：N=1 post-RL 不应列为核心 contribution、ℓz* item-level AUROC≈0.53 近乎随机、PSN-IRT 循环依赖、ARC-C 缺失两个模型、bootstrap 方法未说明类型

报告已提交给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 375 · 2026-05-21T21:17:20.579749+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 41

## Round 41

2 recorded events


### User

_source line 376 · 2026-05-21T21:18:55.032819+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

### Must-Fix

**[AGREE] R1-N1: 仅两个污染水平不足以支撑 "dose-response characterization"**
同意，与我的 N3/Q4 独立一致。补充：(1) Qwen 15% CI=[-15.2,-4.5] 和 50% CI=[-5.0,-1.0] 存在重叠，统计上不能排除 effect size 相同；(2) Appendix A simulation 覆盖了 7 个水平，说明框架可行但 controlled experiments 选择不做；(3) non-monotonic 仅在 Qwen 一个模型上观察到（Mistral/Llama 单调），泛化性存疑。

**[AGREE] R1-N2: QLoRA SFT 生态效度与 pretraining 动机脱节**
同意 framing 错位存在，但严重程度略低于 R1 评估。Section 3.3 (method.tex lines 56-58) 和 Limitations 的 scoping 是负责任的。核心问题在于 Introduction 叙事策略需调整——前置 SFT scope 即可。

**[REBUT] R1-N3: Mistral n=6 seeds 应降级为 Should-Fix**
Table 1 显示 Mistral 两个条件 CI 均不含零（15%: [-7.4,-1.5]; 50%: [-9.6,-2.1]）。Mistral 不独立支撑任何 unique finding——non-monotonic 主要由 Qwen 体现，θ-shift 由三模型共同支撑。n=6 结论方向与 n=10 的 Qwen/Llama 一致，不构成 reject 理由。应补跑但非 critical。

### Should-Fix

**[AGREE] R1-W1**: 完全同意。补充：ℓz* 从 2.91→7.69 可能是 GRPO-induced θ-shift 而非 contamination residual。需要 clean Qwen + GRPO 作为 control 来 disentangle。

**[AGREE] R1-W2**: 同意 item-level AUROC=0.53 削弱 seen/unseen 诊断价值。但 θ-shift mechanism 不仅是理论——它导出了 fixed-θ 的可操作建议（Section 4.2-4.3），structural sensitivity (57/60) 是 DiD 设计的 motivation（Section 3.2）。ℓz* 诊断价值比论文暗示的弱，但非零。

**[AGREE] R1-W3**: 同意 PSN-IRT 循环依赖风险。Gaussian perturbation 不能模拟 structural bias。但 Section 3.1 提到的 MML-EM refit r_a=0.127 说明作者有意识，需补充该实验细节。

**[AGREE] R1-W4**: 完全同意，与我的 N3 一致。

**[AGREE] R1-W5**: Reproducibility Statement 已回答是 percentile method。但 n=3/6 下 percentile bootstrap 可能过于乐观，应补 BCa sensitivity check。

### 总结
R1 和 R2 核心 concerns 高度一致。唯一分歧：Mistral n=6 严重程度（我认为 Should-Fix）。两位 reviewer 独立给出 3.5 (Borderline Conference)。适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 377 · 2026-05-21T21:19:03.989591+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 42

## Round 42

12 recorded events


### User

_source line 378 · 2026-05-21T21:19:05.178435+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心结论：R1 和 R2 审稿意见高度一致，5 个 Must-Fix/Should-Fix 中 4 个完全重合。唯一分歧是 Mistral n=6 的严重程度（R1 列为 critical，我认为 Should-Fix）。两位 reviewer 独立给出 3.5 (Borderline Conference)，共识是论文适合 Findings。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的逐条回应

---

### R2-N1: "Minimal-information point" overclaim
**[AGREE]** Introduction line 12 ("binary response patterns alone") 和 Related Work line 13 ("binary responses only") 确实未反映 PSN-IRT 4PL 参数的实质信息需求。虽然 Discussion (line 17-19) 和 Limitations (line 8) 承认了依赖，但 framing 不一致。R2 建议的 "minimal information from the target model" 精确且可操作。

### R2-N2: 缺少现有方法实证对比
**[REBUT]** 部分不同意。要求与 Min-K% Prob/CoDeC 对比不合理——它们处于不同信息访问层级（token-level probabilities vs binary responses, Section 1 line 8-11）。但 **ConStat 对比合理且可行**：ConStat 也是 performance-based、不需 token-level access。Discussion line 20 仅一句概念性提及不足。Table 3 在同一信息层级内的对比 (ℓz*, HT, acc z-score) 本身有价值，但应补充 ConStat 实证。

### R2-N3: 实验规模偏窄
**[AGREE]** 与我的 N1 (两个污染水平) 和 N3 (Mistral n=6) 高度一致。但要求增加模型规模可能超出 reasonable revision scope，更紧迫的是补中间污染水平和 ARC-C 缺失数据。

### R2-W1: Post-RL 作为 contribution 过弱
**[AGREE]** 与我的 W1 完全一致。

### R2-W2: 两个 findings 理论可预测
**[REBUT]** 不同意。(1) IRT 文献从未在 LLM 场景量化 θ-shift absorption 幅度（Table 2: Qwen |d| 1.90→14.52, 7.6×）；(2) ARC-C reversal (Section 4.3 line 76-83) 涉及 item count × baseline ability 非线性交互，非教科书可推导；(3) 模型特异性（Qwen 非单调 vs Mistral 单调）不可先验预测。论文定位就是 "首次在 LLM 场景下量化边界"（Introduction line 32），这不是 weakness 而是 contribution 本身。

### R2-W3: Bootstrap CI 和样本量
**[AGREE]** 与我的 N3 和 W5 一致。Llama fixed-θ 15% CI 包含零 (Table 2: [0, 2.37]†) 是实质性问题。n≥20 可能过于保守，但 Mistral n=6 需补充。

### R2-W4: Related Work 遗漏
**[REBUT]** 部分不同意。ℓz* 和 HT 的选择有 Karabatsos (2003) 文献依据（Related Work line 27），但确实应更显式说明。遗漏文献需逐条评估——PaCoST 等 performance-based 方法应讨论，但 Watermarking-based detection 相关性较低。"36 篇偏少"本身不是有效批评。

### R2-W5: Abstract 过长
**[AGREE]** 极小问题，压缩 post-RL 描述即可。

---

**两位 Reviewer 的共识区域**：
1. 污染水平太少 (R1-N1 = R2-N3)
2. Post-RL 不应作为核心 contribution (R1-W1 = R2-W1)
3. Mistral n=6 需补充 (R1-N3 ≈ R2-W3)
4. ARC-C 缺失 Llama/Mistral (R1-W4 ≈ R2-N3)
5. GRPO 后 ℓz* 增加的解释存疑 (R1-Q4 = R2-Q5)

**分歧区域**：
- R2-N2 (现有方法对比): R1 认为 MIA 对比不合理但 ConStat 对比合理
- R2-W2 (理论可预测性): R1 认为这不构成 weakness

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 379 · 2026-05-21T21:19:25.660512+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-21T21:19:25.660997+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T21:08:11.451544+00:00\", \"completed_at\": \"2026-05-21T21:11:24.538346+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 heatmap 中 |d| 值较小的浅蓝单元格上白色注释文字对比度降低，打印或低亮度屏幕下可能不够清晰；考虑对浅色单元格使用深色文字或添加文字描边\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3 为单栏图，轴标签和 legend 文字接近可读性下限（约为正文字号 70%）；若空间允许可稍放大字号\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 4 使用双 y 轴设计（左轴 accuracy、右轴 ζ*），增加认知负荷；caption 已解释，但若拆为上下两个 sub-panel 可更直观\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"单页容纳 5 个表格（Tables 4-8），视觉密度高；作为附录功能上可接受，但审稿人快速浏览时可能感到拥挤\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 中灰色单元格（缺失条件）用 \\\"—\\\" 标记，caption 有说明，但若在图内添加简短注脚（如 \\\"not tested\\\"）可减少审稿人翻看 caption 的需要\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 381 · 2026-05-21T21:19:25.661263+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 382 · 2026-05-21T21:19:25.761895+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 383 · 2026-05-21T21:19:59.689784+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
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

_source line 384 · 2026-05-21T21:19:59.740339+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 385 · 2026-05-21T21:22:06.305828+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_personfit_contam",
  "issues_yaml": "## Review Issue Tracker — Round 3 (fresh review, 2026-05-21)\n## Updated after Round 3 cross-sharing convergence\n\n# ===== CRITICAL ISSUES =====\n\n- id: \"R3-N1\"\n  summary: \"仅两个污染水平 (15%, 50%) 不足以支撑 non-monotonic dose-response 核心 claim\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W2: 三个数据点无法区分 inverted-U 和 monotonic decrease\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1-N1 提出，R2 交叉 AGREE。Qwen 15% CI=[-15.2,-4.5] 和 50% CI=[-5.0,-1.0] 存在重叠；Mistral/Llama 实为单调/近单调；论文将 non-monotonic 列为四大发现之首但仅基于两个非零水平——观察而非曲线刻画。QLoRA 成本极低，补 5%/10%/25%/30% 完全可行。Appendix A simulation 覆盖 7 水平说明框架支持但 controlled experiments 选择不做。\"\n  action_items:\n    - round: 3\n      action: \"补充中间污染水平 (5%, 10%, 25%, 30%)，或将 non-monotonic 措辞降级为 observed difference between two levels\"\n      assigned_to: agent+paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"Minimal-information point framing overclaim——实际强依赖外部 4PL item bank\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-N5: inverted-U 削弱 minimal-information 实用性\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2-N1 提出，R1 交叉 AGREE。Abstract/Introduction/Related Work 反复说 binary responses only，但框架强依赖 PSN-IRT 4PL 参数（13,000+ 模型校准），fixed-θ 还需 clean baseline。来自 target model 的信息确实 minimal，但来自 item bank 的信息 substantial。\"\n  action_items:\n    - round: 3\n      action: \"将 framing 改为 minimal information from the target model；区分 target model access (binary only) 和 external item bank (substantial)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"QLoRA SFT 生态效度与 Introduction pretraining contamination 动机脱节\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-N2: QLoRA 仅修改低秩 adapter，与 pretraining contamination 本质不同\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1-N2 提出，R2 交叉 AGREE（严重程度略低）。Introduction 以 pretraining contamination 为动机 (line 3-6)，但实验用 QLoRA SFT (rank=16)，SFT 在低秩空间的集中记忆化信号远强于 pretraining 分布式嵌入。Section 3.3 scoping 负责任但 Introduction 叙事未对齐。\"\n  action_items:\n    - round: 3\n      action: \"Introduction 前置 SFT scope 限定；明确论文 findings 限于 SFT-stage contamination\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N4\"\n  summary: \"实验规模偏窄——3 个 7-8B 模型、2 个 benchmark、仅 SFT 污染\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W1: 缺少 13B/70B、MoE 架构\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2-N3 提出，R1 交叉 AGREE。ARC-C 仅 Qwen 结果，Llama/Mistral 缺失。baseline ability 与 detection sensitivity 负相关仅基于 3 个数据点。标题/abstract 泛化性措辞超出实验 scope。\"\n  action_items:\n    - round: 3\n      action: \"补齐 Llama/Mistral ARC-C 数据；标题/abstract 明确 SFT scope；补中间污染水平（与 R3-N1 联动）\"\n      assigned_to: agent+paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== SHOULD-FIX ISSUES =====\n\n- id: \"R3-W1\"\n  summary: \"Post-RL finding (N=1) 不应列为核心 contribution\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-N3: Abstract overclaim，未标注 preliminary\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1-W1 和 R2-W1 独立提出，交叉完全一致。N=1 (Qwen, GRPO, 15%) 无统计推断，但 Abstract/Intro 将其与 n=10 控制实验并列。ℓz* 从 2.91→7.69 可能是 GRPO-induced θ-shift 而非 contamination residual——需 clean+GRPO control 来 disentangle。Section 4.5 caveat 充分但 Abstract/Conclusion 未匹配。\"\n  action_items:\n    - round: 3\n      action: \"降级为 preliminary observation；从 Abstract 核心列表移除或明确标注 N=1 preliminary；理想情况补 clean+GRPO control\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Mistral n=6 seeds 统计效力不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W6: Mistral n=6 与 Section 3.3 n=10 声称不一致\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列为 critical，R2 交叉 REBUT 降级为 should-fix——Table 1 CI 均不含零，Mistral 不独立支撑 unique finding。但 Table 2 fixed-θ CI [1.45, 9.00] 约束力极低。两人同意应补跑。\"\n  action_items:\n    - round: 3\n      action: \"补跑 Mistral 至 n=10\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3\"\n  summary: \"ℓz* 诊断价值论证不足——item-level AUROC=0.53 近乎随机\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W3/W4: item-level 接近随机，tradeoff 论证缺具体 use case\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1-W2 提出，R2 交叉 AGREE（但指出 θ-shift 导出 fixed-θ 建议有实操价值）。accuracy z-score |d| 是 ℓz* 的 10-36×。seen/unseen decomposition AUROC=0.53 削弱诊断 claim。诊断价值比论文暗示的弱，但非零。\"\n  action_items:\n    - round: 3\n      action: \"加强 detection-diagnosis tradeoff 论证：增加具体 practitioner use case；诚实报告 item-level near-random\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"PSN-IRT 循环依赖——leaderboard 校准数据本身可能被污染\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-N4: 缺少参数精度/标准误和结构性偏差分析\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1-W3 提出，R2 交叉 AGREE。Appendix F 高斯扰动不能模拟结构性偏差。MML-EM refit r_a=0.127 说明作者有意识但实验细节缺失。\"\n  action_items:\n    - round: 3\n      action: \"补充 MML-EM refit 实验细节；讨论 leaderboard 校准污染影响；考虑结构性扰动分析\"\n      assigned_to: agent+paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W5\"\n  summary: \"缺少与 ConStat 的实证对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-D2: 是否需要实证对比存在分歧\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2-N2 提出要求与 ConStat/MIA/CoDeC 对比。R1 交叉 REBUT 部分不同意——MIA 对比不合理（不同信息层级），但 ConStat 对比合理且可行（同为 performance-based）。两人达成部分共识：至少补 ConStat 实证对比。\"\n  action_items:\n    - round: 3\n      action: \"补充 ConStat 实证对比或详细定性分析说明 ℓz* 互补优势\"\n      assigned_to: agent+paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W6\"\n  summary: \"Bootstrap CI 方法和小样本可靠性问题\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 交叉 AGREE。Reproducibility Statement 已说明 percentile method，但 n=3/6 下 percentile bootstrap 可能过于乐观（Appendix C analytic CI 跨零而 bootstrap 不跨）。Llama fixed-θ 15% CI 包含零 [0, 2.37]†。应补 BCa sensitivity check。\"\n  action_items:\n    - round: 3\n      action: \"补充 BCa bootstrap sensitivity check；正文明确标注 percentile method\"\n      assigned_to: agent+paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W7\"\n  summary: \"Related Work 遗漏若干相关方法\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W8: orphan bib entries 已清理\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2-W4 提出，R1 交叉部分 REBUT。需逐条评估：PaCoST (EMNLP 2024 Findings) 和 Don't Make Your LLM an Evaluation Benchmark Cheater 相关性高应讨论；Watermarking-based 相关性低。未解释为何从 36 种 person-fit 中仅选 ℓz* + HT。R1 补充 Reise (1990), Levine & Drasgow (1988), Embretson & Reise (2000)。\"\n  action_items:\n    - round: 3\n      action: \"补充 PaCoST 等高相关性引用；说明 ℓz*/HT 选择理由；考虑增加 psychometrics 经典引用\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== DIVERGENCE =====\n\n- id: \"R3-D1\"\n  summary: \"Findings 新颖性——IRT 理论可预测 vs empirical quantification 有独立价值\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-D1: 相同分歧\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2-W2 认为 θ-shift absorption 和 ceiling effect 可从 IRT 理论预测。R1 REBUT：IRT 文献未量化 LLM 场景下 θ-shift 幅度（7.6× amplification），ARC-C reversal 涉及非线性交互非教科书可推导，模型特异性（Qwen 非单调 vs Mistral 单调）不可先验预测。R1 认为 empirical quantification 本身就是 contribution。\"\n  action_items:\n    - round: 3\n      action: \"写作中更好 acknowledge prior IRT literature 可预测性，同时突出 LLM 场景的新量化结果\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== MINOR ISSUES =====\n\n- id: \"R3-M1\"\n  summary: \"MML-EM refit (r_a=0.127) 实验设置未描述\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2-M1: Section 3.1 提及但无 appendix 支撑\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M2\"\n  summary: \"Figure 1 red diamonds 灰度打印不可见\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2-M2\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M3\"\n  summary: \"Conclusion 仅一句话过于简略\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2-M4\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M4\"\n  summary: \"Abstract 过长 (~250 词)，前端过载具体数字\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 交叉 AGREE。压缩 post-RL 描述即可。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ===== PRIOR ROUND RESOLVED ISSUES =====\n\n- id: \"BEST-W1\"\n  summary: \"0 figures, presentation unacceptable\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Need 3-4 figures, ≥25 references, independent Related Work section.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Paper now has 4 figures, independent Related Work section, 31 citations.\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"本轮未提及，确认已解决。4 figures, 33 citations, 完整 Related Work。\"\n  resolution: \"Resolved\"\n  resolution_round: 2\n\n- id: \"ACTUAL-B-W1\"\n  summary: \"n=3 seeds statistically insufficient\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Must expand to n=10.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Qwen and Llama now n=10. Mistral n=6.\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"主问题已解决（Qwen/Llama n=10）。Mistral n=6 残留问题独立追踪为 R3-W2。\"\n  resolution: \"Resolved — core n=3→n=10 upgrade done; Mistral n=6 tracked separately\"\n  resolution_round: 3\n\n- id: \"V6-THETA-SPECIFICITY\"\n  summary: \"θ-shift model specificity must be main finding\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Must be Results subsection with dedicated figure.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Now Section 4.3 with Figure 3.\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"本轮未提及，确认已解决。\"\n  resolution: \"Resolved\"\n  resolution_round: 2\n\n- id: \"ALL-W3\"\n  summary: \"4PL parameter source unclear\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Must clarify PSN-IRT origin.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Section 3.1 now clearly attributes to PSN-IRT.\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"本轮未提及，确认已解决。敏感性分析问题独立追踪为 R3-W4。\"\n  resolution: \"Resolved\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"缺少 reproducibility statement\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1]\n      note: \"ARR 建议提供 reproducibility statement。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Reproducibility Statement 已添加，包含 bootstrap percentile method 说明和 seed 报告。确认已解决。\"\n  resolution: \"Resolved\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"Orphan bibliography entries\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"28/59 orphan entries。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"清理至 33 entries，tendeiro2014/stonge2011 已正文引用。新的引用缺失独立追踪为 R3-W7。\"\n  resolution: \"Resolved\"\n  resolution_round: 3\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_personfit_contam",
    "issues_yaml": "## Review Issue Tracker — Round 3 (fresh review, 2026-05-21)\n## Updated after Round 3 cross-sharing convergence\n\n# ===== CRITICAL ISSUES =====\n\n- id: \"R3-N1\"\n  summary: \"仅两个污染水平 (15%, 50%) 不足以支撑 non-monotonic dose-response 核心 claim\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W2: 三个数据点无法区分 inverted-U 和 monotonic decrease\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1-N1 提出，R2 交叉 AGREE。Qwen 15% CI=[-15.2,-4.5] 和 50% CI=[-5.0,-1.0] 存在重叠；Mistral/Llama 实为单调/近单调；论文将 non-monotonic 列为四大发现之首但仅基于两个非零水平——观察而非曲线刻画。QLoRA 成本极低，补 5%/10%/25%/30% 完全可行。Appendix A simulation 覆盖 7 水平说明框架支持但 controlled experiments 选择不做。\"\n  action_items:\n    - round: 3\n      action: \"补充中间污染水平 (5%, 10%, 25%, 30%)，或将 non-monotonic 措辞降级为 observed difference between two levels\"\n      assigned_to: agent+paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"Minimal-information point framing overclaim——实际强依赖外部 4PL item bank\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-N5: inverted-U 削弱 minimal-information 实用性\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2-N1 提出，R1 交叉 AGREE。Abstract/Introduction/Related Work 反复说 binary responses only，但框架强依赖 PSN-IRT 4PL 参数（13,000+ 模型校准），fixed-θ 还需 clean baseline。来自 target model 的信息确实 minimal，但来自 item bank 的信息 substantial。\"\n  action_items:\n    - round: 3\n      action: \"将 framing 改为 minimal information from the target model；区分 target model access (binary only) 和 external item bank (substantial)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"QLoRA SFT 生态效度与 Introduction pretraining contamination 动机脱节\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-N2: QLoRA 仅修改低秩 adapter，与 pretraining contamination 本质不同\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1-N2 提出，R2 交叉 AGREE（严重程度略低）。Introduction 以 pretraining contamination 为动机 (line 3-6)，但实验用 QLoRA SFT (rank=16)，SFT 在低秩空间的集中记忆化信号远强于 pretraining 分布式嵌入。Section 3.3 scoping 负责任但 Introduction 叙事未对齐。\"\n  action_items:\n    - round: 3\n      action: \"Introduction 前置 SFT scope 限定；明确论文 findings 限于 SFT-stage contamination\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N4\"\n  summary: \"实验规模偏窄——3 个 7-8B 模型、2 个 benchmark、仅 SFT 污染\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W1: 缺少 13B/70B、MoE 架构\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2-N3 提出，R1 交叉 AGREE。ARC-C 仅 Qwen 结果，Llama/Mistral 缺失。baseline ability 与 detection sensitivity 负相关仅基于 3 个数据点。标题/abstract 泛化性措辞超出实验 scope。\"\n  action_items:\n    - round: 3\n      action: \"补齐 Llama/Mistral ARC-C 数据；标题/abstract 明确 SFT scope；补中间污染水平（与 R3-N1 联动）\"\n      assigned_to: agent+paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== SHOULD-FIX ISSUES =====\n\n- id: \"R3-W1\"\n  summary: \"Post-RL finding (N=1) 不应列为核心 contribution\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-N3: Abstract overclaim，未标注 preliminary\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1-W1 和 R2-W1 独立提出，交叉完全一致。N=1 (Qwen, GRPO, 15%) 无统计推断，但 Abstract/Intro 将其与 n=10 控制实验并列。ℓz* 从 2.91→7.69 可能是 GRPO-induced θ-shift 而非 contamination residual——需 clean+GRPO control 来 disentangle。Section 4.5 caveat 充分但 Abstract/Conclusion 未匹配。\"\n  action_items:\n    - round: 3\n      action: \"降级为 preliminary observation；从 Abstract 核心列表移除或明确标注 N=1 preliminary；理想情况补 clean+GRPO control\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Mistral n=6 seeds 统计效力不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W6: Mistral n=6 与 Section 3.3 n=10 声称不一致\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列为 critical，R2 交叉 REBUT 降级为 should-fix——Table 1 CI 均不含零，Mistral 不独立支撑 unique finding。但 Table 2 fixed-θ CI [1.45, 9.00] 约束力极低。两人同意应补跑。\"\n  action_items:\n    - round: 3\n      action: \"补跑 Mistral 至 n=10\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3\"\n  summary: \"ℓz* 诊断价值论证不足——item-level AUROC=0.53 近乎随机\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W3/W4: item-level 接近随机，tradeoff 论证缺具体 use case\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1-W2 提出，R2 交叉 AGREE（但指出 θ-shift 导出 fixed-θ 建议有实操价值）。accuracy z-score |d| 是 ℓz* 的 10-36×。seen/unseen decomposition AUROC=0.53 削弱诊断 claim。诊断价值比论文暗示的弱，但非零。\"\n  action_items:\n    - round: 3\n      action: \"加强 detection-diagnosis tradeoff 论证：增加具体 practitioner use case；诚实报告 item-level near-random\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"PSN-IRT 循环依赖——leaderboard 校准数据本身可能被污染\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-N4: 缺少参数精度/标准误和结构性偏差分析\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1-W3 提出，R2 交叉 AGREE。Appendix F 高斯扰动不能模拟结构性偏差。MML-EM refit r_a=0.127 说明作者有意识但实验细节缺失。\"\n  action_items:\n    - round: 3\n      action: \"补充 MML-EM refit 实验细节；讨论 leaderboard 校准污染影响；考虑结构性扰动分析\"\n      assigned_to: agent+paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W5\"\n  summary: \"缺少与 ConStat 的实证对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-D2: 是否需要实证对比存在分歧\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2-N2 提出要求与 ConStat/MIA/CoDeC 对比。R1 交叉 REBUT 部分不同意——MIA 对比不合理（不同信息层级），但 ConStat 对比合理且可行（同为 performance-based）。两人达成部分共识：至少补 ConStat 实证对比。\"\n  action_items:\n    - round: 3\n      action: \"补充 ConStat 实证对比或详细定性分析说明 ℓz* 互补优势\"\n      assigned_to: agent+paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W6\"\n  summary: \"Bootstrap CI 方法和小样本可靠性问题\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 交叉 AGREE。Reproducibility Statement 已说明 percentile method，但 n=3/6 下 percentile bootstrap 可能过于乐观（Appendix C analytic CI 跨零而 bootstrap 不跨）。Llama fixed-θ 15% CI 包含零 [0, 2.37]†。应补 BCa sensitivity check。\"\n  action_items:\n    - round: 3\n      action: \"补充 BCa bootstrap sensitivity check；正文明确标注 percentile method\"\n      assigned_to: agent+paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W7\"\n  summary: \"Related Work 遗漏若干相关方法\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W8: orphan bib entries 已清理\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2-W4 提出，R1 交叉部分 REBUT。需逐条评估：PaCoST (EMNLP 2024 Findings) 和 Don't Make Your LLM an Evaluation Benchmark Cheater 相关性高应讨论；Watermarking-based 相关性低。未解释为何从 36 种 person-fit 中仅选 ℓz* + HT。R1 补充 Reise (1990), Levine & Drasgow (1988), Embretson & Reise (2000)。\"\n  action_items:\n    - round: 3\n      action: \"补充 PaCoST 等高相关性引用；说明 ℓz*/HT 选择理由；考虑增加 psychometrics 经典引用\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== DIVERGENCE =====\n\n- id: \"R3-D1\"\n  summary: \"Findings 新颖性——IRT 理论可预测 vs empirical quantification 有独立价值\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-D1: 相同分歧\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2-W2 认为 θ-shift absorption 和 ceiling effect 可从 IRT 理论预测。R1 REBUT：IRT 文献未量化 LLM 场景下 θ-shift 幅度（7.6× amplification），ARC-C reversal 涉及非线性交互非教科书可推导，模型特异性（Qwen 非单调 vs Mistral 单调）不可先验预测。R1 认为 empirical quantification 本身就是 contribution。\"\n  action_items:\n    - round: 3\n      action: \"写作中更好 acknowledge prior IRT literature 可预测性，同时突出 LLM 场景的新量化结果\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== MINOR ISSUES =====\n\n- id: \"R3-M1\"\n  summary: \"MML-EM refit (r_a=0.127) 实验设置未描述\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2-M1: Section 3.1 提及但无 appendix 支撑\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M2\"\n  summary: \"Figure 1 red diamonds 灰度打印不可见\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2-M2\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M3\"\n  summary: \"Conclusion 仅一句话过于简略\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2-M4\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M4\"\n  summary: \"Abstract 过长 (~250 词)，前端过载具体数字\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 交叉 AGREE。压缩 post-RL 描述即可。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ===== PRIOR ROUND RESOLVED ISSUES =====\n\n- id: \"BEST-W1\"\n  summary: \"0 figures, presentation unacceptable\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Need 3-4 figures, ≥25 references, independent Related Work section.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Paper now has 4 figures, independent Related Work section, 31 citations.\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"本轮未提及，确认已解决。4 figures, 33 citations, 完整 Related Work。\"\n  resolution: \"Resolved\"\n  resolution_round: 2\n\n- id: \"ACTUAL-B-W1\"\n  summary: \"n=3 seeds statistically insufficient\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Must expand to n=10.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Qwen and Llama now n=10. Mistral n=6.\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"主问题已解决（Qwen/Llama n=10）。Mistral n=6 残留问题独立追踪为 R3-W2。\"\n  resolution: \"Resolved — core n=3→n=10 upgrade done; Mistral n=6 tracked separately\"\n  resolution_round: 3\n\n- id: \"V6-THETA-SPECIFICITY\"\n  summary: \"θ-shift model specificity must be main finding\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [reviewer]\n      note: \"Must be Results subsection with dedicated figure.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Now Section 4.3 with Figure 3.\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"本轮未提及，确认已解决。\"\n  resolution: \"Resolved\"\n  resolution_round: 2\n\n- id: \"ALL-W3\"\n  summary: \"4PL parameter source unclear\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Must clarify PSN-IRT origin.\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Section 3.1 now clearly attributes to PSN-IRT.\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"本轮未提及，确认已解决。敏感性分析问题独立追踪为 R3-W4。\"\n  resolution: \"Resolved\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"缺少 reproducibility statement\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1]\n      note: \"ARR 建议提供 reproducibility statement。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Reproducibility Statement 已添加，包含 bootstrap percentile method 说明和 seed 报告。确认已解决。\"\n  resolution: \"Resolved\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"Orphan bibliography entries\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"28/59 orphan entries。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"清理至 33 entries，tendeiro2014/stonge2011 已正文引用。新的引用缺失独立追踪为 R3-W7。\"\n  resolution: \"Resolved\"\n  resolution_round: 3\n"
  }
}
```

</details>

---


### Tool result

_source line 386 · 2026-05-21T21:22:06.356757+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml\", \"bytes\": 13029}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 387 · 2026-05-21T21:24:50.563486+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "irt_personfit_contam",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "report": "# 审稿报告：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n\n**Venue**: EMNLP 2026 (via ACL Rolling Review, Long Paper)\n**Reviewers**: R1 (方法严谨性/实验设计/统计推断) + R2 (新颖性/完整性/写作质量)\n**轮次**: Round 1 (fresh review)\n**日期**: 2026-05-21\n\n---\n\n## Summary\n\n本文首次将心理测量学中的 person-fit 统计量（ℓz*）系统性地应用于 LLM benchmark 污染检测，使用 Δℓz* 差分设计 (DiD) 在三个 7-8B 模型族上进行控制实验，识别出四个 IRT 特有的行为边界：non-monotonic dose-response、model-specific θ-shift dynamics、detection-diagnosis tradeoff、以及 preliminary post-RL residual pattern。论文定位为 characterization 而非 tool，诚实展示了 ℓz* 在检测力上远弱于简单 accuracy z-score 的局限性，将其价值定位于诊断能力。\n\n---\n\n## Strengths\n\n**S1 [共识]** 跨学科连接真正新颖——psychometric person-fit → LLM contamination detection 是自然但尚未被探索的类比，将心理测量学四十年积累的作弊检测理论引入 NLP 评估。\n\n**S2 [共识]** 方法论设计巧妙——Δℓz* DiD 设计优雅处理 57/60 baseline misfit 问题，将 IRT 假设违反从障碍转为可管理的技术条件。Appendix 中的 local dependence 模拟（shared + asymmetric LD）和参数扰动分析提供充分的鲁棒性证据。\n\n**S3 [共识]** 异常诚实的 self-assessment——论文坦诚展示 accuracy z-scores 的压倒性检测优势（|d| 10-36×），将 ℓz* 定位为诊断工具而非检测工具，这种自我克制在竞争性投稿中罕见且值得肯定。\n\n**S4 [共识]** θ-shift absorption 机制洞察力强——fixed-θ 验证效果显著（Qwen |d| 1.90→14.52, 7.6× amplification），且 Table 2 的 free/fixed 对比为实操提供清晰建议。\n\n**S5 [共识]** 附录异常充实——每个方法论质疑（IRT 假设违反、local dependence、参数噪声、seed sensitivity）都有对应的模拟或实验分析，学术严谨性高。\n\n**S6 [R2]** Detection-diagnosis tradeoff 的 two-stage workflow（先 z-score 筛选，后 ℓz* 诊断）清晰可操作，有实用价值。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [共识, R1-N1=R2-N3, 交叉双方 AGREE]** 仅两个污染水平 (15%, 50%) 不足以支撑 \"non-monotonic dose-response characterization\" 的核心 claim。\n- 两个非零水平只能说 \"Qwen 在 15% 的 |d| 大于 50%\"——是观察而非曲线刻画\n- Qwen 15% CI=[-15.2,-4.5] 和 50% CI=[-5.0,-1.0] 存在重叠，两水平间差异未经正式统计检验\n- Non-monotonic 仅在 Qwen 上观察到；Mistral 和 Llama 为单调/近单调——泛化性存疑\n- Appendix A simulation 覆盖 7 个水平，说明框架支持更细粒度采样但 controlled experiments 选择不做\n- QLoRA 7B 模型微调成本极低，补充 5%/10%/25%/30% 完全可行\n- **建议**：补充中间污染水平，或将 \"non-monotonic dose-response\" 降级为 \"observed difference between two levels, consistent with simulation-predicted non-monotonicity\"\n\n**N2 [共识, R2-N1, R1 交叉 AGREE]** \"Minimal-information point\" framing 与实际信息需求矛盾。\n- Abstract/Introduction/Related Work 反复强调 \"binary responses only\"，但框架强依赖 PSN-IRT 4PL item bank（基于 13,000+ 模型的 leaderboard 数据校准）\n- Fixed-θ estimation 还需 clean baseline，进一步提高信息门槛\n- 来自 target model 的信息确实是 minimal，但来自 item population 的外部信息是 substantial\n- **建议**：改 framing 为 \"minimal information from the target model\"，显式区分 target model access（binary only）和 external item bank（substantial prior knowledge）\n\n**N3 [共识, R1-N2, R2 交叉 AGREE (略低严重度)]** QLoRA SFT 生态效度与 Introduction 的 pretraining contamination 动机脱节。\n- Introduction 以 pretraining contamination 为动机（line 3-6），但实验用 QLoRA SFT (rank=16, α=32)\n- SFT 在低秩空间产生的集中记忆化信号远强于 pretraining 的分布式嵌入，报告的高 Cohen's d 可能反映 SFT 特有效应\n- Section 3.3 和 Limitations 的 scoping 负责任，但 Introduction 叙事未对齐\n- **建议**：Introduction 前置 SFT scope 限定，将 pretraining contamination 作为 motivation context 而非 direct target\n\n**N4 [共识, R2-N3=R1-W4, 交叉双方 AGREE]** 实验规模偏窄，削弱 generalization claims。\n- 仅 3 个 7-8B 模型、2 个 benchmark（MMLU + ARC-C）、仅 SFT 污染\n- ARC-C 上仅 Qwen 结果，Llama/Mistral 缺失——Section 4.3 的 ceiling effect 讨论缺乏对照\n- \"Baseline ability 与 detection sensitivity 负相关\" 仅基于 3 个数据点，不足以建立系统性关系\n- 标题/abstract 措辞暗示泛化性，但 scope 仅限 SFT 污染一隅\n- **建议**：补齐 Llama/Mistral ARC-C；标题/abstract 明确 scope 为 SFT-stage characterization\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [共识, R1-W1=R2-W1, 交叉完全一致]** Post-RL finding (N=1) 不应列为核心 contribution。\n- N=1（Qwen, GRPO, 15% MMLU），无统计推断，但 Abstract/Introduction 将其与 n=10 控制实验并列为四大发现\n- ℓz* 从 2.91 增至 7.69——可能是 GRPO-induced θ-shift 或 ability reorganization 而非 contamination residual pattern\n- 需要 clean Qwen + GRPO 作为 control 来 disentangle GRPO 本身的效应\n- Section 4.5 的 caveats 充分但 Abstract/Conclusion 未匹配\n- **建议**：降级为 \"preliminary observation\"，从 Abstract 核心列表移除或显著降低权重\n\n**W2 [R1-N3, R2 交叉 REBUT 降级]** Mistral n=6 seeds 统计效力不足。\n- 因服务器退役丢失 4/10 checkpoints；Table 2 fixed-θ CI 跨度达 [1.45, 9.00]——约束力极低\n- R2 认为降级为 Should-Fix（Table 1 CI 均不含零，Mistral 不独立支撑 unique finding），R1 原列为 critical\n- QLoRA 成本极低，补跑完全可行\n- **建议**：补至 n=10\n\n**W3 [共识, R1-W2, R2 交叉 AGREE]** ℓz* 诊断价值论证不足——item-level AUROC=0.53 近乎随机。\n- Accuracy z-score |d| 是 ℓz* 的 10-36×\n- Seen/unseen decomposition 的 item-level AUROC=0.53 (Table 8) 接近随机，削弱诊断 claim\n- θ-shift mechanism 有洞察力但更像框架理论（导出 fixed-θ 建议有实操价值——R2 补充）\n- Structural sensitivity (57/60 flagged) 反映 IRT misfit 普遍性，论文已正确用作 DiD 设计动机\n- **建议**：加强 tradeoff 论证，增加具体 practitioner use case；诚实报告 item-level near-random\n\n**W4 [共识, R1-W3, R2 交叉 AGREE]** PSN-IRT 参数循环依赖风险。\n- PSN-IRT 基于可能受 contamination 影响的 leaderboard 数据校准\n- Appendix F 的高斯扰动分析有价值但不能模拟结构性偏差\n- Section 3.1 提到 MML-EM refit r_a=0.127 但实验细节缺失\n- **建议**：补充 MML-EM refit 实验描述；讨论 leaderboard 校准污染影响\n\n**W5 [部分共识, R2-N2, R1 交叉 REBUT 部分同意]** 缺少与 ConStat 的实证对比。\n- R2 要求与 ConStat/MIA/CoDeC 对比；R1 指出 MIA 对比不合理（不同信息层级），但 ConStat 对比合理且可行\n- ConStat 同为 performance-based，Discussion 仅一句概念性提及不足\n- **建议**：补充 ConStat 实证对比，或至少给出详细定性分析说明 ℓz* 的互补优势\n\n**W6 [共识, R1-W5, R2 交叉 AGREE]** Bootstrap CI 方法类型和小样本可靠性。\n- Reproducibility Statement 已说明 percentile method，但 n=3/6 下 percentile bootstrap 可能 anti-conservative\n- Appendix C 中 n=3 的 analytic CI 跨零而 bootstrap CI 不跨——可能反映小样本 anti-conservatism\n- **建议**：补充 BCa sensitivity check；Llama fixed-θ 15% CI 包含零 [0, 2.37] 应在正文讨论\n\n**W7 [R2-W4, R1 部分 REBUT]** Related Work 遗漏若干相关方法。\n- PaCoST (EMNLP 2024 Findings)、Don't Make Your LLM an Evaluation Benchmark Cheater (Zhou et al., 2023) 高度相关应讨论\n- 未解释从 36 种 person-fit 统计量中仅选 ℓz* 和 HT 的理由\n- 经典心理测量引用偏少：Reise (1990), Levine &amp; Drasgow (1988), Embretson &amp; Reise (2000)\n- R1 认为 Watermarking-based detection 相关性较低\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全或实质性共识：\n\n1. **[AGREE]** 两个污染水平不足以支撑 non-monotonic dose-response 的核心 claim（R1-N1 = R2-N3）\n2. **[AGREE]** \"Minimal-information point\" framing overclaim（R2-N1, R1 交叉 AGREE）\n3. **[AGREE]** QLoRA SFT 生态效度与 Introduction 叙事脱节（R1-N2, R2 交叉 AGREE）\n4. **[AGREE]** 实验规模偏窄，ARC-C 缺失 Llama/Mistral（R1-W4 = R2-N3）\n5. **[AGREE]** Post-RL N=1 不应列为核心 contribution（R1-W1 = R2-W1）\n6. **[AGREE]** GRPO 后 ℓz* 增加需排除 θ-shift confound（R1-Q4 = R2-Q5）\n7. **[AGREE]** ℓz* 诊断价值比论文暗示的弱，但非零（R1-W2, R2 交叉 AGREE）\n8. **[AGREE]** PSN-IRT 循环依赖和 MML-EM refit 细节缺失（R1-W3, R2 交叉 AGREE）\n9. **[AGREE]** ConStat 实证对比合理且可行（R2-N2, R1 交叉部分 AGREE）\n10. **[AGREE]** Bootstrap percentile 小样本可靠性需验证（R1-W5, R2 交叉 AGREE）\n\n---\n\n## Reviewer Divergence\n\n**D1** Findings 新颖性定级——IRT 理论可预测 vs empirical quantification 有独立价值。\n- R2: θ-shift absorption 是 IRT 教科书知识，ceiling effect 是已知现象——四个 findings 中两个可先验预测\n- R1 [REBUT]: IRT 文献未量化 LLM 场景下 θ-shift 幅度（7.6× amplification）；ARC-C reversal 涉及 item count × baseline ability 非线性交互；模型特异性（Qwen 非单调 vs Mistral 单调）不可先验预测。论文定位就是 \"首次在 LLM 场景下量化边界\"\n- **Director 判断**：R1 反驳有力。理论可预测不等于已被验证——empirical characterization in a new domain 有独立贡献价值，但论文应更好 acknowledge prior IRT literature 的理论基础\n\n**D2** Mistral n=6 严重程度。\n- R1: critical（统计效力不足，应阻止接收）\n- R2: should-fix（CI 不含零，不独立支撑 unique finding，不构成 reject 理由）\n- **Director 判断**：R2 论证更有说服力。Mistral n=6 的 CI 均不含零且结论方向与 n=10 模型一致。定为 Should-Fix，但应优先补跑。\n\n---\n\n## Questions（需作者澄清）\n\n1. 为何不增加中间污染水平（5%/10%/25%/30%）？QLoRA 成本极低，这是有意的 scope 限制还是资源约束？\n2. \"57/60 model-benchmark cells\" 的 60 具体构成是什么？（12 models × 5 benchmarks = 60?）\n3. Fixed-θ 的 clean-model mean anchor 在实际部署中不可得——论文提到的 cross-benchmark θ estimation 替代方案是否有实验评估？\n4. GRPO 后 ℓz* 从 2.91 增至 7.69——这与 \"residual contamination pattern\" 叙事如何一致？是否可能是 GRPO 本身引入新 aberrance？需 clean+GRPO control 排除。\n5. Llama/Mistral 为何未评估 ARC-C？\n6. 从 Karabatsos (2003) 的 36 种 person-fit 统计量中为何仅选 ℓz* 和 HT？是否有系统性比较？\n7. PSN-IRT 的 4PL 参数校准中是否包含本实验模型系列的变体？若包含，是否存在 information leakage？\n8. MML-EM refit 得到 r_a=0.127 的实验设置是什么？数据来源和模型配置？\n\n---\n\n## Missing References\n\n**高相关性（应讨论）**：\n1. PaCoST (EMNLP 2024 Findings) — performance-based 污染检测\n2. Don't Make Your LLM an Evaluation Benchmark Cheater (Zhou et al., 2023)\n3. How Much Can We Forget about Data Contamination? (arXiv 2410.03249)\n4. MEDIRT (arXiv 2509.24186) — IRT 应用于 LLM 评估\n\n**中等相关性（建议引用）**：\n5. Data Contamination Calibration for Black-box LLMs (arXiv 2405.11930)\n6. Reise (1990) — person-fit 作弊检测\n7. Levine &amp; Drasgow (1988) — appropriateness indices 分类\n8. Embretson &amp; Reise (2000) — IRT 教科书\n\n**低相关性（可选）**：\n9. Detecting Benchmark Contamination Through Watermarking (arXiv 2502.17259)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（耗时 ~3 分钟）\n**发现**: 5 项 info 级别，0 项 critical/warning\n\n1. **Page 5**: Figure 2 heatmap 中浅蓝单元格上白色注释文字对比度低，灰度打印可能不清晰——建议对浅色单元格使用深色文字\n2. **Page 6**: Figure 3 单栏图轴标签和 legend 文字接近可读性下限（约正文字号 70%）——若空间允许可放大\n3. **Page 8**: Figure 4 双 y 轴设计增加认知负荷——考虑拆为上下两个 sub-panel\n4. **Page 12**: 单页 5 个表格（Tables 4-8）视觉密度高——作为附录可接受\n5. **Page 5**: Figure 2 灰色缺失单元格建议图内添加 \"not tested\" 注脚\n\n---\n\n## Overall Assessment\n\n**评分**: 3.0 — Findings\n\n**置信度**: 4/5（两位 Reviewer 独立给出一致评分，交叉验证后共识度高）\n\n**理由**:\n\n论文的跨学科连接（IRT person-fit → LLM contamination detection）是真正新颖的贡献，DiD 设计优雅，学术严谨性高。然而，四个核心问题将其推至 Findings 而非主会议：\n\n1. **核心 claim 证据不足**：Non-monotonic dose-response 作为首要发现仅基于两个污染水平，且仅在 Qwen 一个模型上观察到，不构成 characterization\n2. **Framing 偏差**：\"Minimal-information point\" 实际强依赖外部 4PL item bank，fixed-θ 还需 clean baseline——信息需求被系统性低估\n3. **生态效度**：QLoRA SFT 与 Introduction 的 pretraining contamination 动机脱节，高 Cohen's d 可能反映 SFT 特有效应\n4. **Post-RL overclaim**：N=1 结果被列为核心 contribution，与正文的审慎 hedging 不匹配\n\n论文在 characterization 定位、诚实 self-assessment、和方法论严谨性上表现出色（Appendix 充实），适合 Findings 接收。升级至主会议需要：补充中间污染水平、修正 framing、扩展实验规模、降级 post-RL finding。\n\n---\n\n## Detailed Comments\n\n### Abstract/Introduction\n- Abstract ~250 词偏长，建议精简至 150-180 词，压缩 post-RL 描述\n- \"binary response patterns alone\" (Abstract line 2) 改为 \"binary response patterns from the target model, combined with externally calibrated item parameters\"\n- \"the first systematic characterization\" claim 需验证是否确实是首次——建议检查 MEDIRT 等近期工作\n- Introduction 应前置 SFT scope 限定（当前第 57 行才出现）\n\n### Method (Section 3)\n- Section 3.1: MML-EM refit r_a=0.127 实验细节需补充（至少 appendix）\n- Section 3.2: DiD 假设（clean 和 contaminated 共享相同 misfit）的成立条件需更显式讨论——contamination 可能改变 item 间依赖结构\n- Section 3.3: \"n=10 seeds each\" 需在首次出现时标注 Mistral n=6 及原因，不应仅在 Table 脚注\n\n### Results (Section 4)\n- Section 4.2: \"Non-monotonic dose-response\" 标题建议改为 \"Observed dose-response pattern\"；增加 15% vs 50% 的正式统计检验\n- Section 4.3: \"negative correlation\" 基于 3 个数据点——改为 \"observed trend\"\n- Section 4.4: 增加 ConStat 对比或详细定性分析；补充具体 practitioner use case\n- Section 4.5: 标题建议改为 \"Preliminary Observation: Post-RL Residual Pattern (N=1)\"；讨论 ℓz* 增加的可能解释（GRPO-induced θ-shift vs contamination residual）\n\n### Discussion (Section 5)\n- 应显式讨论 ConStat 的互补关系（当前仅一句话）\n- \"minimal information point\" 措辞需与修正后的 Abstract 对齐\n\n### Limitations\n- 当前涵盖充分但可增加：(1) IRT local independence/unidimensionality 违反的具体影响量化引用（Sinharay 2016）；(2) 4PL item bank 作为 critical dependency 的替代方案\n\n### Appendix\n- Appendix C 的 n=3 结果标注 \"superseded by n=10\" 很好——建议考虑移除以节省空间\n- Bootstrap CI: 正文或 Appendix 补充 BCa sensitivity check\n\n### Figures\n- Figure 1: \"red diamonds\" 需确保灰度可辨识——建议改用形状区分（× vs ○）\n- Figure 2: 浅色单元格文字改深色\n- Figure 3: 放大轴标签字号\n- Figure 4: 考虑拆为 sub-panels 减少双 y 轴认知负荷\n\n### References\n- 33 篇引用偏少（EMNLP long paper 常见 40-50 篇），需补充 PaCoST、MEDIRT 等\n- 显式说明 ℓz* + HT 选择理由（引用 Karabatsos 2003）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "irt_personfit_contam",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "report": "# 审稿报告：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n\n**Venue**: EMNLP 2026 (via ACL Rolling Review, Long Paper)\n**Reviewers**: R1 (方法严谨性/实验设计/统计推断) + R2 (新颖性/完整性/写作质量)\n**轮次**: Round 1 (fresh review)\n**日期**: 2026-05-21\n\n---\n\n## Summary\n\n本文首次将心理测量学中的 person-fit 统计量（ℓz*）系统性地应用于 LLM benchmark 污染检测，使用 Δℓz* 差分设计 (DiD) 在三个 7-8B 模型族上进行控制实验，识别出四个 IRT 特有的行为边界：non-monotonic dose-response、model-specific θ-shift dynamics、detection-diagnosis tradeoff、以及 preliminary post-RL residual pattern。论文定位为 characterization 而非 tool，诚实展示了 ℓz* 在检测力上远弱于简单 accuracy z-score 的局限性，将其价值定位于诊断能力。\n\n---\n\n## Strengths\n\n**S1 [共识]** 跨学科连接真正新颖——psychometric person-fit → LLM contamination detection 是自然但尚未被探索的类比，将心理测量学四十年积累的作弊检测理论引入 NLP 评估。\n\n**S2 [共识]** 方法论设计巧妙——Δℓz* DiD 设计优雅处理 57/60 baseline misfit 问题，将 IRT 假设违反从障碍转为可管理的技术条件。Appendix 中的 local dependence 模拟（shared + asymmetric LD）和参数扰动分析提供充分的鲁棒性证据。\n\n**S3 [共识]** 异常诚实的 self-assessment——论文坦诚展示 accuracy z-scores 的压倒性检测优势（|d| 10-36×），将 ℓz* 定位为诊断工具而非检测工具，这种自我克制在竞争性投稿中罕见且值得肯定。\n\n**S4 [共识]** θ-shift absorption 机制洞察力强——fixed-θ 验证效果显著（Qwen |d| 1.90→14.52, 7.6× amplification），且 Table 2 的 free/fixed 对比为实操提供清晰建议。\n\n**S5 [共识]** 附录异常充实——每个方法论质疑（IRT 假设违反、local dependence、参数噪声、seed sensitivity）都有对应的模拟或实验分析，学术严谨性高。\n\n**S6 [R2]** Detection-diagnosis tradeoff 的 two-stage workflow（先 z-score 筛选，后 ℓz* 诊断）清晰可操作，有实用价值。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [共识, R1-N1=R2-N3, 交叉双方 AGREE]** 仅两个污染水平 (15%, 50%) 不足以支撑 \"non-monotonic dose-response characterization\" 的核心 claim。\n- 两个非零水平只能说 \"Qwen 在 15% 的 |d| 大于 50%\"——是观察而非曲线刻画\n- Qwen 15% CI=[-15.2,-4.5] 和 50% CI=[-5.0,-1.0] 存在重叠，两水平间差异未经正式统计检验\n- Non-monotonic 仅在 Qwen 上观察到；Mistral 和 Llama 为单调/近单调——泛化性存疑\n- Appendix A simulation 覆盖 7 个水平，说明框架支持更细粒度采样但 controlled experiments 选择不做\n- QLoRA 7B 模型微调成本极低，补充 5%/10%/25%/30% 完全可行\n- **建议**：补充中间污染水平，或将 \"non-monotonic dose-response\" 降级为 \"observed difference between two levels, consistent with simulation-predicted non-monotonicity\"\n\n**N2 [共识, R2-N1, R1 交叉 AGREE]** \"Minimal-information point\" framing 与实际信息需求矛盾。\n- Abstract/Introduction/Related Work 反复强调 \"binary responses only\"，但框架强依赖 PSN-IRT 4PL item bank（基于 13,000+ 模型的 leaderboard 数据校准）\n- Fixed-θ estimation 还需 clean baseline，进一步提高信息门槛\n- 来自 target model 的信息确实是 minimal，但来自 item population 的外部信息是 substantial\n- **建议**：改 framing 为 \"minimal information from the target model\"，显式区分 target model access（binary only）和 external item bank（substantial prior knowledge）\n\n**N3 [共识, R1-N2, R2 交叉 AGREE (略低严重度)]** QLoRA SFT 生态效度与 Introduction 的 pretraining contamination 动机脱节。\n- Introduction 以 pretraining contamination 为动机（line 3-6），但实验用 QLoRA SFT (rank=16, α=32)\n- SFT 在低秩空间产生的集中记忆化信号远强于 pretraining 的分布式嵌入，报告的高 Cohen's d 可能反映 SFT 特有效应\n- Section 3.3 和 Limitations 的 scoping 负责任，但 Introduction 叙事未对齐\n- **建议**：Introduction 前置 SFT scope 限定，将 pretraining contamination 作为 motivation context 而非 direct target\n\n**N4 [共识, R2-N3=R1-W4, 交叉双方 AGREE]** 实验规模偏窄，削弱 generalization claims。\n- 仅 3 个 7-8B 模型、2 个 benchmark（MMLU + ARC-C）、仅 SFT 污染\n- ARC-C 上仅 Qwen 结果，Llama/Mistral 缺失——Section 4.3 的 ceiling effect 讨论缺乏对照\n- \"Baseline ability 与 detection sensitivity 负相关\" 仅基于 3 个数据点，不足以建立系统性关系\n- 标题/abstract 措辞暗示泛化性，但 scope 仅限 SFT 污染一隅\n- **建议**：补齐 Llama/Mistral ARC-C；标题/abstract 明确 scope 为 SFT-stage characterization\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [共识, R1-W1=R2-W1, 交叉完全一致]** Post-RL finding (N=1) 不应列为核心 contribution。\n- N=1（Qwen, GRPO, 15% MMLU），无统计推断，但 Abstract/Introduction 将其与 n=10 控制实验并列为四大发现\n- ℓz* 从 2.91 增至 7.69——可能是 GRPO-induced θ-shift 或 ability reorganization 而非 contamination residual pattern\n- 需要 clean Qwen + GRPO 作为 control 来 disentangle GRPO 本身的效应\n- Section 4.5 的 caveats 充分但 Abstract/Conclusion 未匹配\n- **建议**：降级为 \"preliminary observation\"，从 Abstract 核心列表移除或显著降低权重\n\n**W2 [R1-N3, R2 交叉 REBUT 降级]** Mistral n=6 seeds 统计效力不足。\n- 因服务器退役丢失 4/10 checkpoints；Table 2 fixed-θ CI 跨度达 [1.45, 9.00]——约束力极低\n- R2 认为降级为 Should-Fix（Table 1 CI 均不含零，Mistral 不独立支撑 unique finding），R1 原列为 critical\n- QLoRA 成本极低，补跑完全可行\n- **建议**：补至 n=10\n\n**W3 [共识, R1-W2, R2 交叉 AGREE]** ℓz* 诊断价值论证不足——item-level AUROC=0.53 近乎随机。\n- Accuracy z-score |d| 是 ℓz* 的 10-36×\n- Seen/unseen decomposition 的 item-level AUROC=0.53 (Table 8) 接近随机，削弱诊断 claim\n- θ-shift mechanism 有洞察力但更像框架理论（导出 fixed-θ 建议有实操价值——R2 补充）\n- Structural sensitivity (57/60 flagged) 反映 IRT misfit 普遍性，论文已正确用作 DiD 设计动机\n- **建议**：加强 tradeoff 论证，增加具体 practitioner use case；诚实报告 item-level near-random\n\n**W4 [共识, R1-W3, R2 交叉 AGREE]** PSN-IRT 参数循环依赖风险。\n- PSN-IRT 基于可能受 contamination 影响的 leaderboard 数据校准\n- Appendix F 的高斯扰动分析有价值但不能模拟结构性偏差\n- Section 3.1 提到 MML-EM refit r_a=0.127 但实验细节缺失\n- **建议**：补充 MML-EM refit 实验描述；讨论 leaderboard 校准污染影响\n\n**W5 [部分共识, R2-N2, R1 交叉 REBUT 部分同意]** 缺少与 ConStat 的实证对比。\n- R2 要求与 ConStat/MIA/CoDeC 对比；R1 指出 MIA 对比不合理（不同信息层级），但 ConStat 对比合理且可行\n- ConStat 同为 performance-based，Discussion 仅一句概念性提及不足\n- **建议**：补充 ConStat 实证对比，或至少给出详细定性分析说明 ℓz* 的互补优势\n\n**W6 [共识, R1-W5, R2 交叉 AGREE]** Bootstrap CI 方法类型和小样本可靠性。\n- Reproducibility Statement 已说明 percentile method，但 n=3/6 下 percentile bootstrap 可能 anti-conservative\n- Appendix C 中 n=3 的 analytic CI 跨零而 bootstrap CI 不跨——可能反映小样本 anti-conservatism\n- **建议**：补充 BCa sensitivity check；Llama fixed-θ 15% CI 包含零 [0, 2.37] 应在正文讨论\n\n**W7 [R2-W4, R1 部分 REBUT]** Related Work 遗漏若干相关方法。\n- PaCoST (EMNLP 2024 Findings)、Don't Make Your LLM an Evaluation Benchmark Cheater (Zhou et al., 2023) 高度相关应讨论\n- 未解释从 36 种 person-fit 统计量中仅选 ℓz* 和 HT 的理由\n- 经典心理测量引用偏少：Reise (1990), Levine &amp; Drasgow (1988), Embretson &amp; Reise (2000)\n- R1 认为 Watermarking-based detection 相关性较低\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全或实质性共识：\n\n1. **[AGREE]** 两个污染水平不足以支撑 non-monotonic dose-response 的核心 claim（R1-N1 = R2-N3）\n2. **[AGREE]** \"Minimal-information point\" framing overclaim（R2-N1, R1 交叉 AGREE）\n3. **[AGREE]** QLoRA SFT 生态效度与 Introduction 叙事脱节（R1-N2, R2 交叉 AGREE）\n4. **[AGREE]** 实验规模偏窄，ARC-C 缺失 Llama/Mistral（R1-W4 = R2-N3）\n5. **[AGREE]** Post-RL N=1 不应列为核心 contribution（R1-W1 = R2-W1）\n6. **[AGREE]** GRPO 后 ℓz* 增加需排除 θ-shift confound（R1-Q4 = R2-Q5）\n7. **[AGREE]** ℓz* 诊断价值比论文暗示的弱，但非零（R1-W2, R2 交叉 AGREE）\n8. **[AGREE]** PSN-IRT 循环依赖和 MML-EM refit 细节缺失（R1-W3, R2 交叉 AGREE）\n9. **[AGREE]** ConStat 实证对比合理且可行（R2-N2, R1 交叉部分 AGREE）\n10. **[AGREE]** Bootstrap percentile 小样本可靠性需验证（R1-W5, R2 交叉 AGREE）\n\n---\n\n## Reviewer Divergence\n\n**D1** Findings 新颖性定级——IRT 理论可预测 vs empirical quantification 有独立价值。\n- R2: θ-shift absorption 是 IRT 教科书知识，ceiling effect 是已知现象——四个 findings 中两个可先验预测\n- R1 [REBUT]: IRT 文献未量化 LLM 场景下 θ-shift 幅度（7.6× amplification）；ARC-C reversal 涉及 item count × baseline ability 非线性交互；模型特异性（Qwen 非单调 vs Mistral 单调）不可先验预测。论文定位就是 \"首次在 LLM 场景下量化边界\"\n- **Director 判断**：R1 反驳有力。理论可预测不等于已被验证——empirical characterization in a new domain 有独立贡献价值，但论文应更好 acknowledge prior IRT literature 的理论基础\n\n**D2** Mistral n=6 严重程度。\n- R1: critical（统计效力不足，应阻止接收）\n- R2: should-fix（CI 不含零，不独立支撑 unique finding，不构成 reject 理由）\n- **Director 判断**：R2 论证更有说服力。Mistral n=6 的 CI 均不含零且结论方向与 n=10 模型一致。定为 Should-Fix，但应优先补跑。\n\n---\n\n## Questions（需作者澄清）\n\n1. 为何不增加中间污染水平（5%/10%/25%/30%）？QLoRA 成本极低，这是有意的 scope 限制还是资源约束？\n2. \"57/60 model-benchmark cells\" 的 60 具体构成是什么？（12 models × 5 benchmarks = 60?）\n3. Fixed-θ 的 clean-model mean anchor 在实际部署中不可得——论文提到的 cross-benchmark θ estimation 替代方案是否有实验评估？\n4. GRPO 后 ℓz* 从 2.91 增至 7.69——这与 \"residual contamination pattern\" 叙事如何一致？是否可能是 GRPO 本身引入新 aberrance？需 clean+GRPO control 排除。\n5. Llama/Mistral 为何未评估 ARC-C？\n6. 从 Karabatsos (2003) 的 36 种 person-fit 统计量中为何仅选 ℓz* 和 HT？是否有系统性比较？\n7. PSN-IRT 的 4PL 参数校准中是否包含本实验模型系列的变体？若包含，是否存在 information leakage？\n8. MML-EM refit 得到 r_a=0.127 的实验设置是什么？数据来源和模型配置？\n\n---\n\n## Missing References\n\n**高相关性（应讨论）**：\n1. PaCoST (EMNLP 2024 Findings) — performance-based 污染检测\n2. Don't Make Your LLM an Evaluation Benchmark Cheater (Zhou et al., 2023)\n3. How Much Can We Forget about Data Contamination? (arXiv 2410.03249)\n4. MEDIRT (arXiv 2509.24186) — IRT 应用于 LLM 评估\n\n**中等相关性（建议引用）**：\n5. Data Contamination Calibration for Black-box LLMs (arXiv 2405.11930)\n6. Reise (1990) — person-fit 作弊检测\n7. Levine &amp; Drasgow (1988) — appropriateness indices 分类\n8. Embretson &amp; Reise (2000) — IRT 教科书\n\n**低相关性（可选）**：\n9. Detecting Benchmark Contamination Through Watermarking (arXiv 2502.17259)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（耗时 ~3 分钟）\n**发现**: 5 项 info 级别，0 项 critical/warning\n\n1. **Page 5**: Figure 2 heatmap 中浅蓝单元格上白色注释文字对比度低，灰度打印可能不清晰——建议对浅色单元格使用深色文字\n2. **Page 6**: Figure 3 单栏图轴标签和 legend 文字接近可读性下限（约正文字号 70%）——若空间允许可放大\n3. **Page 8**: Figure 4 双 y 轴设计增加认知负荷——考虑拆为上下两个 sub-panel\n4. **Page 12**: 单页 5 个表格（Tables 4-8）视觉密度高——作为附录可接受\n5. **Page 5**: Figure 2 灰色缺失单元格建议图内添加 \"not tested\" 注脚\n\n---\n\n## Overall Assessment\n\n**评分**: 3.0 — Findings\n\n**置信度**: 4/5（两位 Reviewer 独立给出一致评分，交叉验证后共识度高）\n\n**理由**:\n\n论文的跨学科连接（IRT person-fit → LLM contamination detection）是真正新颖的贡献，DiD 设计优雅，学术严谨性高。然而，四个核心问题将其推至 Findings 而非主会议：\n\n1. **核心 claim 证据不足**：Non-monotonic dose-response 作为首要发现仅基于两个污染水平，且仅在 Qwen 一个模型上观察到，不构成 characterization\n2. **Framing 偏差**：\"Minimal-information point\" 实际强依赖外部 4PL item bank，fixed-θ 还需 clean baseline——信息需求被系统性低估\n3. **生态效度**：QLoRA SFT 与 Introduction 的 pretraining contamination 动机脱节，高 Cohen's d 可能反映 SFT 特有效应\n4. **Post-RL overclaim**：N=1 结果被列为核心 contribution，与正文的审慎 hedging 不匹配\n\n论文在 characterization 定位、诚实 self-assessment、和方法论严谨性上表现出色（Appendix 充实），适合 Findings 接收。升级至主会议需要：补充中间污染水平、修正 framing、扩展实验规模、降级 post-RL finding。\n\n---\n\n## Detailed Comments\n\n### Abstract/Introduction\n- Abstract ~250 词偏长，建议精简至 150-180 词，压缩 post-RL 描述\n- \"binary response patterns alone\" (Abstract line 2) 改为 \"binary response patterns from the target model, combined with externally calibrated item parameters\"\n- \"the first systematic characterization\" claim 需验证是否确实是首次——建议检查 MEDIRT 等近期工作\n- Introduction 应前置 SFT scope 限定（当前第 57 行才出现）\n\n### Method (Section 3)\n- Section 3.1: MML-EM refit r_a=0.127 实验细节需补充（至少 appendix）\n- Section 3.2: DiD 假设（clean 和 contaminated 共享相同 misfit）的成立条件需更显式讨论——contamination 可能改变 item 间依赖结构\n- Section 3.3: \"n=10 seeds each\" 需在首次出现时标注 Mistral n=6 及原因，不应仅在 Table 脚注\n\n### Results (Section 4)\n- Section 4.2: \"Non-monotonic dose-response\" 标题建议改为 \"Observed dose-response pattern\"；增加 15% vs 50% 的正式统计检验\n- Section 4.3: \"negative correlation\" 基于 3 个数据点——改为 \"observed trend\"\n- Section 4.4: 增加 ConStat 对比或详细定性分析；补充具体 practitioner use case\n- Section 4.5: 标题建议改为 \"Preliminary Observation: Post-RL Residual Pattern (N=1)\"；讨论 ℓz* 增加的可能解释（GRPO-induced θ-shift vs contamination residual）\n\n### Discussion (Section 5)\n- 应显式讨论 ConStat 的互补关系（当前仅一句话）\n- \"minimal information point\" 措辞需与修正后的 Abstract 对齐\n\n### Limitations\n- 当前涵盖充分但可增加：(1) IRT local independence/unidimensionality 违反的具体影响量化引用（Sinharay 2016）；(2) 4PL item bank 作为 critical dependency 的替代方案\n\n### Appendix\n- Appendix C 的 n=3 结果标注 \"superseded by n=10\" 很好——建议考虑移除以节省空间\n- Bootstrap CI: 正文或 Appendix 补充 BCa sensitivity check\n\n### Figures\n- Figure 1: \"red diamonds\" 需确保灰度可辨识——建议改用形状区分（× vs ○）\n- Figure 2: 浅色单元格文字改深色\n- Figure 3: 放大轴标签字号\n- Figure 4: 考虑拆为 sub-panels 减少双 y 轴认知负荷\n\n### References\n- 33 篇引用偏少（EMNLP long paper 常见 40-50 篇），需补充 PaCoST、MEDIRT 等\n- 显式说明 ℓz* + HT 选择理由（引用 Karabatsos 2003）"
  }
}
```

</details>

---


### Tool result

_source line 388 · 2026-05-21T21:24:54.630931+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_9840a7d708128f2f1d02985bd9b8d901:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4067
}
```

</details>

---


### Assistant

_source line 389 · 2026-05-21T21:25:07.010386+00:00_

审稿报告已投递至 Research Director。

**圆桌审稿完成**：

- **Overall 3.0 (Findings)**，两位 Reviewer 独立给出 3.5，交叉验证后共识强化了关键 weaknesses 的严重度
- **4 个 Must-Fix**：(1) 两个污染水平不足以支撑 dose-response 核心 claim；(2) minimal-information framing overclaim；(3) QLoRA SFT 与 pretraining 动机脱节；(4) 实验规模偏窄、ARC-C 缺失
- **7 个 Should-Fix**：Post-RL N=1 降级、Mistral n=6 补跑、ℓz* 诊断论证加强、PSN-IRT 依赖讨论、ConStat 对比、Bootstrap BCa check、Related Work 补充
- **1 个分歧**（findings 新颖性）Director 判为 R1 有力——empirical quantification in new domain 有独立价值
- **视觉审查**：5 项 info 级建议，无 blocking issue
- **Issue Tracker** 已同步更新（18 条 active issues + 5 条 resolved）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 43

## Round 43

2 recorded events


### User

_source line 390 · 2026-05-21T21:25:08.517691+00:00_

[Reviewer 1 审稿结果]:
交叉回应已发送。总结：

**与 R2 一致的 5 条**：minimal-information overclaim (N1)、实验规模偏窄 (N3)、post-RL 降级 (W1)、bootstrap/样本量 (W3)、abstract 过长 (W5)

**反驳的 3 条**：
- N2（MIA 对比不合理，但应补 ConStat）
- W2（理论可预测 ≠ 实证冗余，ARC-C reversal 和模型特异性不可先验推导）
- W4（统计量选择有 Karabatsos 2003 依据，遗漏文献需逐条评估而非批量列举）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 391 · 2026-05-21T21:25:26.232193+00:00_

审稿报告已投递至 Research Director。

**审稿完成总结：**

- **评分**：3.0（Findings）
- **Reviewer 共识**：两位 Reviewer 独立评分 3.5，经交叉验证后共识度高（10 项 AGREE，2 项 divergence）
- **4 个 Must-Fix**：(1) 两个污染水平不足以支撑 non-monotonic dose-response 核心 claim；(2) minimal-information framing overclaim；(3) QLoRA SFT 生态效度与 Introduction 动机脱节；(4) 实验规模偏窄 + ARC-C 缺失两个模型
- **7 个 Should-Fix**：Post-RL N=1 降级、Mistral n=6 补跑、ℓz* 诊断论证加强、PSN-IRT 循环依赖、ConStat 对比、bootstrap BCa check、Related Work 补充
- **升级路径**：补中间污染水平 → 修正 framing → 扩展 ARC-C → 降级 post-RL → 补 ConStat 对比
- **Issue Tracker 已同步更新**（18 条 issue，含 4 critical / 8 warning / 2 divergence / 4 minor + 5 条 prior round resolved）
- **视觉审查**：已完成，5 项 info 级别问题（图表可读性建议）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 44

## Round 44

64 recorded events


### User

_source line 392 · 2026-05-22T04:45:05.502933+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_personfit_contam
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (via ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 393 · 2026-05-22T04:45:11.765538+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 394 · 2026-05-22T04:45:11.816676+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 395 · 2026-05-22T04:45:20.410657+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues,WebSearch",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues,WebSearch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 396 · 2026-05-22T04:45:20.411016+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 397 · 2026-05-22T04:45:26.448380+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 398 · 2026-05-22T04:45:26.549093+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 399 · 2026-05-22T04:45:33.676467+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 400 · 2026-05-22T04:45:35.031780+00:00_

{"result":"# 项目 irt_personfit_contam 概况\n\n## 实验状态 (80 个)\n\n- **exp-domain-analysis**: DONE (success) — \n- **exp-ml-classifier-baseline**: DONE (success) — \n- **exp-v1-irt-refit-pilot**: DONE (negative) — \n- **exp-clean-control-delta**: DONE (success) — \n- **exp-fdr-correction**: DONE (success) — \n- **exp-cross-benchmark-analysis**: DONE (success) — \n- **exp-accuracy-zscore-baseline**: DONE (success) — \n- **exp-item-alignment-check**: DONE (negative) — \n- **exp-power-theory**: DONE (success) — \n- **exp-empirical-null**: DONE (negative) — \n- **exp-leaderboard-data-recon**: DONE (success) — \n- **exp-extended-sim**: DONE (success) — \n- **exp-two-sided**: DONE (negative) — \n- **phase_b_personfit**: DONE (success) — \n- **sim_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-ctrl-contam-qwen-5pct（准备中）\n- exp-arcc-benchmark: ℓz* contamination detection generalizes beyond MMLU to ARC-Challenge, a second benchmark with PSN-IRT 4PL calibration — demonstrating cross-benchmark applicability and addressing reviewer concern about single-benchmark evaluation.（准备中）\n- arcc-clean-s10（准备中）\n- arcc-clean-s9（准备中）\n- arcc-clean-s8（准备中）\n- arcc-clean-s7（准备中）\n- exp-ctrl-contam-qwen-clean-s10: Tenth independent clean Qwen2.5-7B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation（准备中）\n- exp-constat-comparison: ConStat (NeurIPS 2024) requires multi-benchmark performance scores for contamination detection, making it inapplicable or underpowered in single-benchmark scenarios. ℓz* operates on binary response patterns from a single benchmark, demonstrating superior minimal-information detection capability.（准备中）\n- exp-arcc-clean-s1: ARC-Challenge clean baseline (seed=42) for cross-benchmark ℓz* detection — establishing clean lz* distribution on a second benchmark with PSN-IRT 4PL calibration（准备中）\n- exp-mia-mink-comparison: MIA methods (Min-K%/Min-K%++) fail to detect contamination 
…[truncated 1649 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 401 · 2026-05-22T04:45:35.584496+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 402 · 2026-05-22T04:45:35.936178+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\usepackage{enumitem}
16	
17	\newcommand{\irtfit}{\textsc{IRT-FIT}}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{What Can Binary Response Patterns Reveal About Benchmark Contamination? \\
22	An IRT Person-Fit Characterization}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{sections/abstract}
31	\end{abstract}
32	
33	\input{sections/introduction}
34	\input{sections/related_work}
35	\input{sections/method}
36	\input{sections/results}
37	\input{sections/discussion}
38	\input{sections/conclusion}
39	
40	\input{sections/limitations}
41	
42	\section*{Reproducibility Statement}
43	Code and response data will be released upon acceptance.
44	Bootstrap confidence intervals use the percentile method with 10,000 resamples; random seeds are reported for all experiments.
45	Pre-calibrated 4PL item parameters are from the publicly available PSN-IRT item bank \citep{psnirt2026}.
46	
47	\bibliography{references}
48	
49	\appendix
50	\input{sections/appendix}
51	
52	\end{document}
53	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 403 · 2026-05-22T04:45:36.037509+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 404 · 2026-05-22T04:45:41.708913+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found some relevant information about EMNLP 2026, though th
…[truncated 1140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 5671
}
```

</details>

---


### Tool call

_source line 405 · 2026-05-22T04:45:46.427265+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers ARR submission deadline page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers ARR submission deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-22T04:45:47.531845+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity"
  }
}
```

</details>

---


### Tool call

_source line 407 · 2026-05-22T04:45:49.644986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
  "offset": "0",
  "limit": "52"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
    "offset": "0",
    "limit": "52"
  }
}
```

</details>

---


### Tool result

_source line 408 · 2026-05-22T04:45:49.695610+00:00_

0	\documentclass[11pt]{article}
1	\usepackage[review]{acl}
2	\usepackage{times}
3	\usepackage{latexsym}
4	\usepackage[T1]{fontenc}
5	\usepackage[utf8]{inputenc}
6	\usepackage{microtype}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage{enumitem}
15	
16	\newcommand{\irtfit}{\textsc{IRT-FIT}}
17	
18	\graphicspath{{../figures/paper/}}
19	
20	\title{What Can Binary Response Patterns Reveal About Benchmark Contamination? \\
21	An IRT Person-Fit Characterization}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\begin{abstract}
29	\input{sections/abstract}
30	\end{abstract}
31	
32	\input{sections/introduction}
33	\input{sections/related_work}
34	\input{sections/method}
35	\input{sections/results}
36	\input{sections/discussion}
37	\input{sections/conclusion}
38	
39	\input{sections/limitations}
40	
41	\section*{Reproducibility Statement}
42	Code and response data will be released upon acceptance.
43	Bootstrap confidence intervals use the percentile method with 10,000 resamples; random seeds are reported for all experiments.
44	Pre-calibrated 4PL item parameters are from the publicly available PSN-IRT item bank \citep{psnirt2026}.
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-22T04:45:50.900576+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers ARR submission deadline page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results for EMNLP 2026, here's the information about the main conference call for papers:

## Key Information:

**ARR Submission Deadline:** May 25, 2026

**Page Limits:** The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

**Additional Requirements:** The mandatory Limitations section is required, placed after the conclusion.

**Submission Process
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 4473
}
```

</details>

---


### Tool result

_source line 410 · 2026-05-22T04:45:53.159810+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit anonymity"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"}]

Based on the search results for ACL Rolling Review 2026 submission guidelines, here are the key details regarding page limits and anonymity:

## Page Limits

The page limit is 4 pages for short papers and 8 pages for long papers, excluding the ethical considerations and limitations sections.

## Anonymity Requirements

Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the author
…[truncated 675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 5627
}
```

</details>

---


### Tool call

_source line 411 · 2026-05-22T04:46:00.638127+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
  }
}
```

</details>

---


### Tool result

_source line 412 · 2026-05-22T04:46:00.688785+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 413 · 2026-05-22T04:46:03.300013+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
  }
}
```

</details>

---


### Tool result

_source line 414 · 2026-05-22T04:46:03.351539+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 415 · 2026-05-22T04:46:06.163738+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 416 · 2026-05-22T04:46:06.666106+00:00_

1	Benchmark contamination in Large Language Models (LLMs) undermines evaluation validity, yet most detection methods require privileged access to training data, model internals, or output probabilities.
2	We present the first systematic characterization of IRT person-fit statistics for contamination detection under black-box access: the framework requires only binary response patterns from the target model---no access to weights, gradients, logits, or training data---combined with externally calibrated 4PL item parameters from a large-scale item bank; diagnostic $\theta$-anchoring additionally requires a clean baseline.
3	A contaminated LLM produces aberrant response patterns analogous to a test-taker with item preknowledge.
4	Using $\ell_z^*$ in a difference-in-differences design ($\Delta\ell_z^*$) across three 7--8B model families ($n{=}10$ seeds each) on MMLU (14,042 items) and ARC-Challenge (295 items), we identify four behavior boundaries:
5	(1) an empirical inverted-U dose-response in one model family, where detection peaks at 25\% contamination ($|d|{=}8.22$) and declines at 50\% ($|d|{=}1.90$) due to $\theta$-shift absorption;
6	(2) model-specific $\theta$-shift dynamics linking baseline ability to detection sensitivity;
7	(3) a detection-diagnosis tradeoff where simpler statistics yield stronger detection but lack $\ell_z^*$'s diagnostic capabilities (seen/unseen decomposition, mechanistic $\theta$-shift analysis);
8	and (4) a preliminary post-RL observation ($N{=}1$) that GRPO erases the accuracy gap while $\ell_z^*$ response-pattern structure persists.
9	These findings establish when and why binary response patterns carry contamination information beyond aggregate accuracy.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 417 · 2026-05-22T04:46:06.666628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 418 · 2026-05-22T04:46:07.068616+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation \citep{dodge2021, magar2022, sainz2023}.
4	As training corpora and public benchmarks both expand, the probability of overlap increases structurally \citep{jacovi2023, chang2024survey}.
5	When contamination occurs, benchmark scores no longer reflect genuine capability, undermining the primary mechanism by which the community compares and selects models.
6	
7	A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record.
8	N-gram overlap methods need the training corpus \citep{dodge2021, magar2022}.
9	Membership inference approaches require token-level probabilities \citep{minkprob2024, deng2024}.
10	Probing methods rely on crafted prompts \citep{golchin2024, oren2024}.
11	Performance-based methods require multiple test variants or output logits \citep{constat2024, codec2026}.
12	These methods form a detection frontier ordered by information access.
13	No existing method operates under pure black-box access---using only binary response patterns, without model weights, gradients, logits, or training data---though, as we show, effective detection additionally requires externally calibrated item parameters.
14	
15	In this work, we focus on SFT-stage contamination---where benchmark answers are explicitly included in fine-tuning data---for three reasons.
16	First, controlled experiments require known ground-truth contamination sets, achievable through fine-tuning with specific benchmark items.
17	Second, SFT-stage contamination is increasingly relevant as fine-tuning-as-a-service platforms proliferate, creating new pathways for benchmark data to enter training mixtures.
18	Third, SFT provides a methodologically clean setting to characterize detection boundaries before extending to nois
…[truncated 4733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 419 · 2026-05-22T04:46:07.069096+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 420 · 2026-05-22T04:46:08.074188+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Benchmark contamination detection.}
4	Contamination detection methods span a wide range of information requirements.
5	Corpus-search methods match benchmark items directly against pretraining data \citep{dodge2021, magar2022}, but require full corpus access unavailable for closed models.
6	Membership inference attacks (MIA) use token-level log-probabilities to distinguish training from unseen examples \citep{minkprob2024, deng2024}.
7	Generation-based probes elicit benchmark content via prompting \citep{golchin2024, golchin2024quiz, oren2024}.
8	Performance-based methods compare accuracy on target and reference sets \citep{constat2024, pacost2024, codec2026}, requiring multiple evaluations or in-context learning passes.
9	\citet{zhou2023benchmark} and \citet{sainz2023} argue for systematic contamination measurement, \citet{jacovi2023} propose mitigation strategies, and \citet{bordt2025forget} show that contamination can be ``forgotten'' under sufficient continued training.
10	
11	A critical limitation unites all token-level methods: \citet{wang2025fragility} show that RL post-training renders MIA-based detectors no better than random across 10 methods and 4 benchmarks, because RL reshapes token distributions while largely preserving binary correctness patterns.
12	\citet{selfcritique2026} and \citet{zhang2026rlvr} propose RL-specific solutions but require generation-level access.
13	Our approach operates under black-box access---requiring only binary responses, with no access to model weights, logits, or training data---but depends on externally calibrated item parameters from PSN-IRT \citep{psnirt2026}.
14	
15	\paragraph{IRT for LLM evaluation.}
16	Item Response Theory has seen growing adoption in NLP and ML evaluation.
17	\citet{martinezplumed2019} applied IRT to analyze machine learning classifiers at the instance level, establishing that item difficulty and discrimination parameters capture meaning
…[truncated 2093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 421 · 2026-05-22T04:46:08.074618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 422 · 2026-05-22T04:46:08.526725+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{IRT Person-Fit Framework}
5	\label{sec:framework}
6	
7	We adopt the four-parameter logistic (4PL) IRT model to characterize contamination-induced aberrance in LLM response patterns.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ difficulty, $c_i$ the lower asymptote (guessing), and $d_i$ the upper asymptote (slip).
14	Item parameters are pre-calibrated by PSN-IRT \citep{psnirt2026} from a large-scale leaderboard dataset; we use these external parameters rather than re-estimating from potentially contaminated data, since our MML-EM refit shows discrimination recovery degrades to $r_a{=}0.127$ on contaminated leaderboard data.
15	
16	Given item parameters and a binary response vector $\mathbf{x} = (x_1, \ldots, x_n)$, we compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized log-likelihood residual quantifying deviation between observed and expected response patterns.
17	The Snijders correction accounts for estimation uncertainty in $\hat{\theta}_{\text{MLE}}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null \citep{drasgow1985, snijders2001}; \citet{magis2012} provide a detailed treatment of how response model selection and ability estimation affect $\ell_z^*$.
18	Large negative $\ell_z^*$ indicates aberrant responding (unexpected failures on easy items or unexpected successes on hard items); large positive values indicate over-consistent patterns.
19	
20	\subsection{$\Delta\ell_z^*$ Difference-in-Differences Design}
21	\label{sec:did}
22	
23	LLM response patterns systematically violate IRT assumptions of local independence and unidimensionality.
24	In our empirical data, 57 of 60 model-benchmark cells yield $|\ell_z^*| > 1.96$ even absent contamination, 
…[truncated 2929 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 423 · 2026-05-22T04:46:08.527122+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 424 · 2026-05-22T04:46:09.029651+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Detection Signal Across Model Families}
5	\label{sec:detection}
6	
7	Table~\ref{tab:cohens_d} presents Cohen's $d$ effect sizes for $\ell_z^*$ across three model families and two benchmarks.
8	All confidence intervals exclude zero, confirming that $\Delta\ell_z^*$ reliably separates contaminated from clean models at both contamination levels.
9	
10	On MMLU, effect sizes range from $|d|{=}1.90$ (Qwen at 50\%) to $|d|{=}8.22$ (Qwen at 25\%), with Llama ($|d|{=}2.27$/$2.50$) and Mistral ($|d|{=}2.64$/$3.50$) falling between.
11	On ARC-C (295 items), Qwen yields $|d|{=}3.16$ at 15\% and $|d|{=}5.30$ at 50\%, demonstrating that detection remains feasible even on small benchmarks when contamination is sufficiently concentrated.
12	
13	Clean-model $\ell_z^*$ baselines diverge substantially across families: Qwen ${+}8.68$ ($\text{SD}{=}0.74$), Mistral ${+}4.02$ ($\text{SD}{=}2.05$), Llama ${+}0.29$ ($\text{SD}{=}1.45$), and ARC-C Qwen ${-}5.42$ ($\text{SD}{=}0.16$).
14	Absolute $\ell_z^*$ thresholds would produce contradictory results: Qwen's contaminated $\ell_z^*$ at 15\% (${+}3.85$) is still positive.
15	The $\Delta\ell_z^*$ design normalizes these divergent baselines: Cohen's $d$ yields comparable effect sizes ($|d|{=}1.90$--$8.22$) despite order-of-magnitude baseline differences.
16	Figure~\ref{fig:heatmap} provides a visual summary.
17	
18	\begin{table}[t]
19	\centering
20	\caption{Cohen's $d$ for $\Delta\ell_z^*$ across model families ($n{=}10$ clean seeds, bootstrap 95\% CI, 10,000 resamples). All CIs exclude 0.}
21	\label{tab:cohens_d}
22	\footnotesize
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}llrrr@{}}
25	\toprule
26	Model & Bench. & $d$ (15\%) [CI] & $d$ (25\%) [CI] & $d$ (50\%) [CI] \\
27	\midrule
28	Qwen & MMLU & $-6.58$ [$-15.2$, $-4.5$] & $-8.22$ [$-18.9$, $-5.7$] & $-1.90$ [$-5.0$, $-1.0$] \\
29	Llama & MMLU & $-2.27$ [$-4.6$, $-1.6$] & --- & $-2.50$ [$-5.0$, $-1.8$] \\
30	Mistral & MMLU
…[truncated 14715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 425 · 2026-05-22T04:46:09.030164+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 426 · 2026-05-22T04:46:09.482240+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	Our findings reveal both the strengths and boundaries of IRT person-fit for contamination detection: $\ell_z^*$ reliably detects SFT-stage contamination across model families, but four boundary conditions constrain its practical utility.
4	
5	\paragraph{Characterization over tool.}
6	The detection-diagnosis tradeoff (\S\ref{sec:degradation}) shows that simpler statistics detect contamination more powerfully than $\ell_z^*$: accuracy $z$-scores yield $|d|$ values several-fold to over an order of magnitude larger, and HT generally exceeds $\ell_z^*$.
7	The value of the IRT framework lies not in detection power but in mechanistic understanding: the $\theta$-shift analysis reveals \emph{why} detection sensitivity varies across models and contamination levels, the seen/unseen decomposition identifies \emph{what fraction} of items are memorized, and the 4PL parameterization captures item-level ceiling effects that 3PL misattributes as aberrance.
8	These diagnostic capabilities are invisible to accuracy $z$-scores or HT.
9	
10	\paragraph{Practical implications.}
11	Two results have immediate consequences.
12	Free-$\theta$ estimation can produce misleading dose-response curves; anchoring $\theta$ to a pre-contamination baseline substantially amplifies detection for high-ability models but is unnecessary where free estimation already captures the signal.
13	The benchmark size boundary means $\ell_z^*$ is most informative for large benchmarks ($n > 7{,}000$ items for 80\% power at 15\% contamination); on small benchmarks like ARC-C (295 items), detection relies on concentrated contamination effects.
14	
15	\paragraph{Scope and calibration.}
16	Universal baseline misfit (57/60 cells flagged) confirms systematic IRT violations; the $\Delta\ell_z^*$ design turns this into a feature through within-model differencing, but requires clean baselines or cross-benchmark references.
17	PSN-IRT provides pre-calibrated 4PL parameters for o
…[truncated 948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 427 · 2026-05-22T04:46:09.583052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 428 · 2026-05-22T04:46:10.386860+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We presented the first systematic characterization of IRT person-fit statistics for LLM benchmark contamination detection under black-box access.
4	Controlled experiments across three 7--8B model families ($n{=}10$ seeds) establish reliable SFT-stage detection (all bootstrap 95\% CIs exclude zero) while revealing four boundary conditions: an empirical inverted-U dose-response confirmed with three contamination levels, model-specific $\theta$-shift dynamics, a detection-diagnosis tradeoff, and a preliminary post-RL residual pattern ($N{=}1$).
5	Future work should investigate pretraining-stage signatures, calibration-free person-fit approaches, and validation across broader model scales.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 429 · 2026-05-22T04:46:10.487683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 430 · 2026-05-22T04:46:10.588533+00:00_

1	\section*{Limitations}
2	
3	Our controlled experiments cover three model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B) at the 7--8B scale with QLoRA fine-tuning; validation on larger models (13B, 70B), mixture-of-experts architectures, and full-parameter fine-tuning remains future work.
4	The observed negative correlation between baseline ability and detection sensitivity rests on three model families and should be treated as a trend rather than a confirmed relationship.
5	Our findings are scoped to SFT-based contamination and may not generalize to pretraining contamination, which operates through different learning dynamics.
6	The post-RL characterization is $N{=}1$ (Qwen only, GRPO algorithm, 15\% contamination on MMLU); generalization to other model families, RL methods (PPO, DPO), and contamination levels requires further validation.
7	LLMs systematically violate IRT assumptions of local independence and unidimensionality; while the $\Delta\ell_z^*$ design mitigates shared misfit through within-model differencing, the theoretical properties of this correction under severe model misfit remain an open question.
8	The framework depends on pre-calibrated 4PL item parameters from PSN-IRT; parameter estimation errors propagate to $\ell_z^*$ computation, and the approach requires externally maintained parameter banks.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 431 · 2026-05-22T04:46:10.588871+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 432 · 2026-05-22T04:46:10.639618+00:00_

1	\section{Simulation Validation}
2	\label{app:simulation}
3	
4	Under the null (no contamination), bootstrap $\ell_z^*$ tracks $\mathcal{N}(0,1)$: mean bias 0.041 and standard deviation 1.003 on MMLU.
5	Kolmogorov--Smirnov rejection rates vary with benchmark size: 8.3\% for MMLU and HellaSwag ($n > 10{,}000$), 50.0\% for GSM8K ($n = 1{,}319$), 58.3\% for ARC-C ($n = 295$), and 75.0\% for HumanEval ($n = 164$).
6	$\ell_z^*$ is well-calibrated for benchmarks with $n \geq 10{,}000$ items; smaller benchmarks show increasing finite-sample deviations from normality.
7	
8	Two-sided testing eliminates the inverted-U artifact: MMLU achieves 97.8\% power at 15\% contamination and sustains ${>}$93\% at all levels.
9	Power scales with $\sqrt{n}$, as predicted by the noncentrality parameter $\delta \propto \sqrt{n}$.
10	The empirical power function, derived via Gauss--Hermite quadrature ($K=30$) over the ability distribution, achieves $R^2 = 0.957$ against simulated values, with approximate minimum benchmark size of $n \geq 7{,}958$ items for 80\% power at 15\% contamination under MMLU item parameters.
11	
12	\section{4PL vs.\ 3PL Ablation Details}
13	\label{app:4pl_ablation}
14	
15	Table~\ref{tab:4pl_3pl_power} reports detection power (proportion of 2{,}000 simulation replicates rejecting $H_0$ at $\alpha{=}0.05$, two-sided) for 4PL and 3PL parameterizations across five benchmarks and seven contamination levels.
16	The 4PL model yields higher power than 3PL at every non-trivial contamination level on every benchmark.
17	The advantage is largest on MMLU and HellaSwag, where upper-asymptote ($d < 1$) violations are most prevalent, and smallest on ARC-Challenge and HumanEval, where limited item counts constrain power under both parameterizations.
18	
19	Power is non-monotonic at 75\% contamination under 4PL on four of five benchmarks (e.g., MMLU: $.952 \to .938$; GSM8K: $.846 \to .802$).
20	This reflects the $\theta$-shift boundary condition described in \S\ref{sec:inverted_u}: at
…[truncated 16532 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 433 · 2026-05-22T04:46:16.161232+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex",
  "offset": "291"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex",
    "offset": "291"
  }
}
```

</details>

---


### Tool result

_source line 434 · 2026-05-22T04:46:16.864358+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (291). The file has 291 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 435 · 2026-05-22T04:46:16.914947+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 436 · 2026-05-22T04:46:16.965816+00:00_

1	% =============================================================================
2	% references.bib — IRT Person-Fit Contamination Detection Paper
3	% Cleaned: 2026-05-21 | 33 entries (orphan entries removed)
4	% =============================================================================
5	
6	% =============================================================================
7	% Person-Fit Statistics (Psychometrics)
8	% =============================================================================
9	
10	@article{drasgow1985,
11	  title = {Appropriateness Measurement with Polychotomous Item Response Models and Standardized Indices},
12	  author = {Drasgow, F. and Levine, M. V. and Williams, E. A.},
13	  journal = {British Journal of Mathematical and Statistical Psychology},
14	  year = {1985},
15	  volume = {38},
16	  number = {1},
17	  pages = {67--86},
18	  doi = {10.1111/j.2044-8317.1985.tb00817.x},
19	}
20	
21	@article{karabatsos2003,
22	  title = {Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics},
23	  author = {Karabatsos, G.},
24	  journal = {Applied Measurement in Education},
25	  year = {2003},
26	  volume = {16},
27	  number = {4},
28	  pages = {277--298},
29	  doi = {10.1207/S15324818AME1604_2},
30	}
31	
32	@article{meijer2001,
33	  title = {Methodology Review: Evaluating Person Fit},
34	  author = {Meijer, R. R. and Sijtsma, K.},
35	  journal = {Applied Psychological Measurement},
36	  year = {2001},
37	  volume = {25},
38	  number = {2},
39	  pages = {107--135},
40	  doi = {10.1177/01466210122031957},
41	}
42	
43	@article{sinharay2017,
44	  title = {Which Statistic Should Be Used to Detect Item Preknowledge When the Set of Compromised Items Is Known?},
45	  author = {Sinharay, S.},
46	  journal = {Applied Psychological Measurement},
47	  year = {2017},
48	  doi = {10.1177/0146621617698453},
49	}
50	
51	@article{snijders2001,
52	  title = {Asymptotic Null Distribution of Person Fit Statistics with Estimated Person Pa
…[truncated 5848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 437 · 2026-05-22T04:46:27.609972+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib",
  "offset": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib",
    "offset": "200"
  }
}
```

</details>

---


### Tool result

_source line 438 · 2026-05-22T04:46:27.710986+00:00_

200	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
201	  year = {2021},
202	  publisher = {Association for Computational Linguistics},
203	  pages = {4486--4503},
204	  doi = {10.18653/v1/2021.acl-long.346},
205	}
206	
207	% =============================================================================
208	% Benchmark Datasets
209	% =============================================================================
210	
211	@article{clark2018arc,
212	  title = {Think you have Solved Question Answering? Try {ARC}, the {AI2} Reasoning Challenge},
213	  author = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
214	  journal = {arXiv preprint arXiv:1803.05457},
215	  year = {2018},
216	}
217	
218	@inproceedings{hendrycks2021mmlu,
219	  title = {Measuring Massive Multitask Language Understanding},
220	  author = {Hendrycks, D. and Burns, C. and Basart, S. and Zou, A. and Mazeika, M. and Song, D. and Steinhardt, J.},
221	  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},
222	  year = {2021},
223	  url = {https://arxiv.org/abs/2009.03300},
224	}
225	
226	% =============================================================================
227	% LLM Evaluation Infrastructure
228	% =============================================================================
229	
230	@article{chang2024survey,
231	  title = {A Survey on Evaluation of Large Language Models},
232	  author = {Chang, Y. and Wang, X. and Wang, J. and Wu, Y. and Yang, L. and Zhu, K. and Chen, H. and Yi, X. and Wang, C. and Wang, Y. and Ye, W. and Zhang, Y. and Chang, Y. and Yu, P. S. and Yang, Q. and Xie, X.},
233	  journal = {ACM Transactions on Intelligent Systems and Technology},
234	  year = {2024},
235	  doi = {10.1145/3641289},
236	}
237	
238	% =============================================================================
239	% 
…[truncated 8554 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 439 · 2026-05-22T04:46:36.193012+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_personfit_contam",
    "file": "review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 440 · 2026-05-22T04:46:37.599192+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 441 · 2026-05-22T04:46:38.052513+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 442 · 2026-05-22T04:46:38.203768+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 443 · 2026-05-22T04:46:41.918756+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/ -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
  "description": "Find config files in agent directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/ -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
    "description": "Find config files in agent directory"
  }
}
```

</details>

---


### Tool result

_source line 444 · 2026-05-22T04:46:42.672194+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 445 · 2026-05-22T04:46:43.174282+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 446 · 2026-05-22T04:46:43.576609+00:00_

## Review Issue Tracker — Round 3 (fresh review, 2026-05-21)
## Updated after 25% Qwen experiment confirms inverted-U (2026-05-21)

# ===== CRITICAL ISSUES =====

- id: "R3-N1"
  summary: "仅两个污染水平 (15%, 50%) 不足以支撑 non-monotonic dose-response 核心 claim"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 2
  last_seen_round: 3
  mentions:
    - round: 2
      reviewers: [1, 2]
      note: "R2-W2: 三个数据点无法区分 inverted-U 和 monotonic decrease"
    - round: 3
      reviewers: [1, 2]
      note: "R1-N1 提出，R2 交叉 AGREE。Qwen 15% CI=[-15.2,-4.5] 和 50% CI=[-5.0,-1.0] 存在重叠；Mistral/Llama 实为单调/近单调；论文将 non-monotonic 列为四大发现之首但仅基于两个非零水平——观察而非曲线刻画。QLoRA 成本极低，补 5%/10%/25%/30% 完全可行。Appendix A simulation 覆盖 7 水平说明框架支持但 controlled experiments 选择不做。"
  action_items:
    - round: 3
      action: "实证加强：补充 25% Qwen 实验 (d=-8.22, BCa CI [-14.71,-4.94])，3 点 inverted-U 曲线直接确认 θ-shift absorption 机制。Table 1 增加 25% 行，§4.2 叙事升级。Paper Agent patching。"
      assigned_to: agent+paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R3-N2"
  summary: "Minimal-information point framing overclaim——实际强依赖外部 4PL item bank"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 2
  last_seen_round: 3
  mentions:
    - round: 2
      reviewers: [1, 2]
      note: "R2-N5: inverted-U 削弱 minimal-information 实用性"
    - round: 3
      reviewers: [1, 2]
      note: "R2-N1 提出，R1 交叉 AGREE。Abstract/Introduction/Related Work 反复说 binary responses only，但框架强依赖 PSN-IRT 4PL 参数（13,000+ 模型校准），fixed-θ 还需 clean baseline。来自 target model 的信息确实 minimal，但来自 item bank 的信息 substantial。"
  action_items:
    - round: 3
      action: "将 framing 改为 minimal information from the target model；区分 target model access (binary only) 和 external item bank (substantial)"
      assigned_to: paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R3-N3"
  summary: "QLoRA SFT 生态效度与 Introduction pretraining contamination 动机脱节"
…[truncated 11931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 447 · 2026-05-22T04:46:43.677359+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
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

_source line 448 · 2026-05-22T04:46:43.828501+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 449 · 2026-05-22T04:47:33.373295+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_personfit_contam",
  "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_personfit_contam",
    "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209"
  }
}
```

</details>

---


### Tool result

_source line 450 · 2026-05-22T04:47:56.566723+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23193
}
```

</details>

---


### Tool call

_source line 451 · 2026-05-22T04:47:56.718501+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "irt_personfit_contam",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性**。\n\n## 论文信息\n- 标题：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n- 论文路径：/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_3/submitted.pdf\n\n## Venue 要求\n- **Venue**：EMNLP 2026（通过 ACL Rolling Review 提交）\n- **投稿类别**：Long Paper\n- **Deadline**：2026-05-25\n- **页数限制**：正文严格 8 页，参考文献不限页数，Limitations 和 Ethical Considerations 不计入页数（前提是不含过多附加内容）\n- **模板**：ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**：Double-blind，论文不得包含作者姓名和单位\n- **附录**：允许，放在参考文献之后\n- **评分标准**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **实验设计**：\n   - 控制实验设计是否合理（QLoRA SFT 作为污染代理的生态效度）\n   - 样本量（n=10 seeds Qwen/Llama, n=6 Mistral）是否足够支撑统计推断\n   - 污染水平选择（15%, 25%, 50%）是否充分刻画 dose-response\n   - 3 个 7-8B 模型 + 2 个 benchmark 的覆盖面是否足以支撑 claims\n\n2. **统计方法**：\n   - Δℓz* difference-in-differences 设计的合理性\n   - Cohen's d + bootstrap 95% CI (10,000 resamples) 的统计严谨性\n   - 小样本（特别是 Mistral n=6）下 bootstrap CI 的可靠性\n   - Fixed-θ vs free-θ 对比方法的合理性\n\n3. **Claims-Evidence 对齐**：\n   - 四大发现（inverted-U, θ-shift dynamics, detection-diagnosis tradeoff, post-RL residual）是否有充分证据支撑\n   - Post-RL finding (N=1) 的 claim 强度是否与证据匹配\n   - Abstract/Introduction 中的 claim 是否与 Results 中的证据匹配\n   - \"black-box access\" framing 是否准确（考虑对 PSN-IRT 外部 item bank 的依赖）\n\n4. **IRT 理论应用**：\n   - 4PL 模型在 LLM 评估场景下的适用性\n   - Local independence 假设违反的影响和 DiD 设计的缓解效果\n   - PSN-IRT 参数的可靠性和循环依赖问题\n\n5. **格式合规**：\n   - 页数是否符合 8 页限制\n   - 匿名性是否完整\n   - Limitations 章节是否存在\n\n请以严格顶会审稿人的标准输出完整审稿意见，包括 Summary, Strengths, Weaknesses (必须严格), Questions, Missing References, Overall Assessment (使用 EMNLP 评分标准)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "irt_personfit_contam",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性**。\n\n## 论文信息\n- 标题：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n- 论文路径：/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_3/submitted.pdf\n\n## Venue 要求\n- **Venue**：EMNLP 2026（通过 ACL Rolling Review 提交）\n- **投稿类别**：Long Paper\n- **Deadline**：2026-05-25\n- **页数限制**：正文严格 8 页，参考文献不限页数，Limitations 和 Ethical Considerations 不计入页数（前提是不含过多附加内容）\n- **模板**：ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**：Double-blind，论文不得包含作者姓名和单位\n- **附录**：允许，放在参考文献之后\n- **评分标准**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **实验设计**：\n   - 控制实验设计是否合理（QLoRA SFT 作为污染代理的生态效度）\n   - 样本量（n=10 seeds Qwen/Llama, n=6 Mistral）是否足够支撑统计推断\n   - 污染水平选择（15%, 25%, 50%）是否充分刻画 dose-response\n   - 3 个 7-8B 模型 + 2 个 benchmark 的覆盖面是否足以支撑 claims\n\n2. **统计方法**：\n   - Δℓz* difference-in-differences 设计的合理性\n   - Cohen's d + bootstrap 95% CI (10,000 resamples) 的统计严谨性\n   - 小样本（特别是 Mistral n=6）下 bootstrap CI 的可靠性\n   - Fixed-θ vs free-θ 对比方法的合理性\n\n3. **Claims-Evidence 对齐**：\n   - 四大发现（inverted-U, θ-shift dynamics, detection-diagnosis tradeoff, post-RL residual）是否有充分证据支撑\n   - Post-RL finding (N=1) 的 claim 强度是否与证据匹配\n   - Abstract/Introduction 中的 claim 是否与 Results 中的证据匹配\n   - \"black-box access\" framing 是否准确（考虑对 PSN-IRT 外部 item bank 的依赖）\n\n4. **IRT 理论应用**：\n   - 4PL 模型在 LLM 评估场景下的适用性\n   - Local independence 假设违反的影响和 DiD 设计的缓解效果\n   - PSN-IRT 参数的可靠性和循环依赖问题\n\n5. **格式合规**：\n   - 页数是否符合 8 页限制\n   - 匿名性是否完整\n   - Limitations 章节是否存在\n\n请以严格顶会审稿人的标准输出完整审稿意见，包括 Summary, Strengths, Weaknesses (必须严格), Questions, Missing References, Overall Assessment (使用 EMNLP 评分标准)。"
  }
}
```

</details>

---


### Tool result

_source line 452 · 2026-05-22T04:48:15.166542+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18448
}
```

</details>

---


### Tool call

_source line 453 · 2026-05-22T04:48:15.368158+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "irt_personfit_contam",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性/完整性**。\n\n## 论文信息\n- 标题：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n- 论文路径：/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_3/submitted.pdf\n\n## Venue 要求\n- **Venue**：EMNLP 2026（通过 ACL Rolling Review 提交）\n- **投稿类别**：Long Paper\n- **Deadline**：2026-05-25\n- **页数限制**：正文严格 8 页，参考文献不限页数，Limitations 和 Ethical Considerations 不计入页数（前提是不含过多附加内容）\n- **模板**：ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**：Double-blind，论文不得包含作者姓名和单位\n- **附录**：允许，放在参考文献之后\n- **评分标准**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查侧重：新颖性/完整性\n\n请重点审查以下方面：\n\n1. **Contribution 新颖性**：\n   - 将心理测量学 person-fit 统计量迁移到 LLM 污染检测是否有足够新颖性\n   - 四大发现中哪些是真正新颖的 empirical insight，哪些是 IRT 理论可直接预测的\n   - 与现有污染检测方法（ConStat, MIA, generation-based probes）相比，本方法是否填补了真实空白\n   - \"characterization\" 定位是否有足够的 contribution density 支撑长文\n\n2. **Related Work 覆盖**：\n   - 三个领域（contamination detection, IRT for LLM, person-fit in psychometrics）的覆盖是否充分\n   - 是否遗漏重要相关工作（特别是近期 2025-2026 年的工作）\n   - 与最相关 baseline（ConStat, PaCoST, CoDeC）的讨论是否充分\n   - 引用是否真实存在（检查年份、venue、作者是否合理）\n\n3. **评估完整性**：\n   - 实验覆盖面：3 个 7-8B 模型是否足够？是否需要更大/更小模型？\n   - Benchmark 覆盖：MMLU (14,042 items) + ARC-C (295 items) 是否足够？\n   - 与 baseline 方法的对比是否充分（detection-diagnosis tradeoff 中 accuracy z-score 和 HT 的对比是否足以说明问题）\n   - 是否需要与 ConStat 等方法进行实证对比\n\n4. **Framing 准确性**：\n   - \"black-box access\" 的定义和使用是否准确（框架依赖 PSN-IRT 外部参数）\n   - \"minimal information\" 的 claim 是否有 overclaim\n   - Abstract/Introduction 的 scope 声明是否与实际实验范围匹配\n   - Post-RL finding 的定位（列为核心发现 vs. preliminary observation）\n\n5. **写作质量**：\n   - 论文结构和叙事逻辑\n   - Abstract 长度和信息密度\n   - Figure/Table 质量和信息量\n   - Conclusion 是否充分总结\n\n请以严格顶会审稿人的标准输出完整审稿意见，包括 Summary, Strengths, Weaknesses (必须严格), Questions, Missing References, Overall Assessment (使用 EMNLP 评分标准)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "irt_personfit_contam",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性/完整性**。\n\n## 论文信息\n- 标题：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n- 论文路径：/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_3/submitted.pdf\n\n## Venue 要求\n- **Venue**：EMNLP 2026（通过 ACL Rolling Review 提交）\n- **投稿类别**：Long Paper\n- **Deadline**：2026-05-25\n- **页数限制**：正文严格 8 页，参考文献不限页数，Limitations 和 Ethical Considerations 不计入页数（前提是不含过多附加内容）\n- **模板**：ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**：Double-blind，论文不得包含作者姓名和单位\n- **附录**：允许，放在参考文献之后\n- **评分标准**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查侧重：新颖性/完整性\n\n请重点审查以下方面：\n\n1. **Contribution 新颖性**：\n   - 将心理测量学 person-fit 统计量迁移到 LLM 污染检测是否有足够新颖性\n   - 四大发现中哪些是真正新颖的 empirical insight，哪些是 IRT 理论可直接预测的\n   - 与现有污染检测方法（ConStat, MIA, generation-based probes）相比，本方法是否填补了真实空白\n   - \"characterization\" 定位是否有足够的 contribution density 支撑长文\n\n2. **Related Work 覆盖**：\n   - 三个领域（contamination detection, IRT for LLM, person-fit in psychometrics）的覆盖是否充分\n   - 是否遗漏重要相关工作（特别是近期 2025-2026 年的工作）\n   - 与最相关 baseline（ConStat, PaCoST, CoDeC）的讨论是否充分\n   - 引用是否真实存在（检查年份、venue、作者是否合理）\n\n3. **评估完整性**：\n   - 实验覆盖面：3 个 7-8B 模型是否足够？是否需要更大/更小模型？\n   - Benchmark 覆盖：MMLU (14,042 items) + ARC-C (295 items) 是否足够？\n   - 与 baseline 方法的对比是否充分（detection-diagnosis tradeoff 中 accuracy z-score 和 HT 的对比是否足以说明问题）\n   - 是否需要与 ConStat 等方法进行实证对比\n\n4. **Framing 准确性**：\n   - \"black-box access\" 的定义和使用是否准确（框架依赖 PSN-IRT 外部参数）\n   - \"minimal information\" 的 claim 是否有 overclaim\n   - Abstract/Introduction 的 scope 声明是否与实际实验范围匹配\n   - Post-RL finding 的定位（列为核心发现 vs. preliminary observation）\n\n5. **写作质量**：\n   - 论文结构和叙事逻辑\n   - Abstract 长度和信息密度\n   - Figure/Table 质量和信息量\n   - Conclusion 是否充分总结\n\n请以严格顶会审稿人的标准输出完整审稿意见，包括 Summary, Strengths, Weaknesses (必须严格), Questions, Missing References, Overall Assessment (使用 EMNLP 评分标准)。"
  }
}
```

</details>

---


### Tool result

_source line 454 · 2026-05-22T04:48:16.928198+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1560
}
```

</details>

---


### Assistant

_source line 455 · 2026-05-22T04:48:41.046025+00:00_

Round 1 已启动：

- **视觉审查 Agent**：已派发（fire-and-forget，不阻塞审稿）
- **Reviewer 1**（方法严谨性）：已分配，审查实验设计、统计方法、claims-evidence 对齐、IRT 理论应用
- **Reviewer 2**（新颖性/完整性）：已分配，审查 contribution 新颖性、related work 覆盖、评估完整性、framing 准确性

等待两位 Reviewer 返回独立初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 45

## Round 45

2 recorded events


### User

_source line 456 · 2026-05-22T04:53:41.960952+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（侧重：新颖性/完整性）

**论文标题**: What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 跨学科迁移（心理测量 person-fit → LLM 污染表征）有价值，实验设计扎实，但 contribution density 偏薄——四大发现中部分可由 IRT 理论直接预测，实验覆盖面有限（模型规模单一、无直接 baseline 对比），且 "characterization" 定位本身限制了实际影响力。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 方法论框架合理，Δl_z^* 差分设计有效控制 baseline aberrance；但 IRT 假设违反严重（57/60 cells |l_z^*|>1.96, Section 3.2），差分设计为何能在如此大规模违反下仍然有效缺乏理论论证；Finding 4 仅 N=1 |
| Excitement | 2.5/5 | 跨学科桥梁有趣但非变革性；核心发现之一（detection-diagnosis tradeoff）实质上表明简单统计量优于本文提出的框架用于检测；缺乏实际可操作的检测工具或对现有方法的改进 |
| Reproducibility | 4.0/5 | 实验细节充分，使用公开的 PSN-IRT 参数，报告了 bootstrap 95% CI，承诺代码发布 |
| Confidence | 4/5 | 我熟悉 IRT 和 LLM 评测方法论，仔细阅读了全文和附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Finding 4 (Post-RL residual pattern) 作为核心发现缺乏充分支撑

- 具体位置：Section 4.5, Figure 4, Abstract ("a preliminary post-RL residual pattern")
- 问题：该发现仅基于 N=1（单一模型族 Qwen+GRPO，单一污染水平 15%），作者自己也标注为 "preliminary"。但 Abstract 将其列为四大核心贡献之一（"(4) a preliminary post-RL residual pattern"），与其他三个有 3×3 factorial design 支撑的发现并列，造成 contribution scope 膨胀。Section 4.5 末尾承认 "no statistical inference is drawn"，但这与将其列为核心 Finding 的定位矛盾。
- 为什么影响接收：核心贡献数量膨胀会误导 AC 对论文实际贡献量的评估。一个无统计推断的 N=1 观察不应与系统性实验发现并列。
- 建议修改方向：(a) 将 Finding 4 从核心贡献列表移至 Discussion 中的 "preliminary observation" 或 "future direction"；(b) 在 Abstract 中明确只列三个有充分支撑的发现；(c) 或者增加更多 post-RL 条件（不同 RL 方法如 PPO/DPO、不同模型族、不同污染水平）使之成为正式 Finding。

**N2** [critical] 缺乏与现有 detection 方法的实证对比

- 具体位置：Section 4.4 (Detection-Diagnosis Tradeoff), Section 5 Discussion
- 问题：论文声称 l_z^* 与 ConStat 互补（Section 5: "The approach is complementary to ConStat"），但这仅是文字论述，没有实证验证。Section 4.4 仅对比了 accuracy z-score、HT 和 l_z^* 三个 person-fit 相关统计量的内部对比，未将 Δl_z^* 与 ConStat (Dekoninck et al., 2024)、PaCoST (Zhang et al., 2024)、CoDeC (Zawalski et al., 2024) 等方法在相同实验设置下对比。更关键的是，Section 4.4 的结论是 **simpler statistics (accuracy z-scores) yield stronger detection**——这实质上表明论文自身的核心工具 l_z^* 在检测任务上劣于更简单的方法。
- 为什么影响接收：对于一个将自身定位为 contamination detection 领域贡献的论文，不与该领域的主要方法进行实证对比是重大缺陷。"互补性" 的声明无法仅凭文字论证成立。
- 建议修改方向：(a) 至少在 MMLU 上与 ConStat 进行实证对比（ConStat 代码已开源）；(b) 如果时间不够做完整实证，应在论文中明确将缺乏对比列为主要 limitation，而非仅在 Discussion 中用一句 "complementary" 带过。

**N3** [critical] 模型规模覆盖不足，削弱发现的普适性

- 具体位置：Section 3.3 Experimental Setup, Table 1
- 问题：全部 3 个模型族都在 7-8B 参数范围。Finding 2（model-specific θ-shift dynamics）的核心主张是 "baseline ability modulates detection sensitivity"，但这一结论仅在同一规模档的三个模型间建立。没有更大（13B、70B）或更小（1-3B）模型，无法区分发现是 ability-driven 还是 scale-driven。例如，同一模型族不同规模（Qwen-1.8B vs Qwen-7B vs Qwen-72B）可能提供更 clean 的 ability 梯度。
- 为什么影响接收：顶会论文的 empirical claims 需要足够的实验覆盖来支撑普适性。仅 7-8B 模型的实验不足以支撑 Section 5 中 "across broader model scales" 的 future work 定位——这是一个应在当前论文中至少部分解决的问题。
- 建议修改方向：(a) 增加至少一个较大（≥13B）和一个较小（≤3B）模型；(b) 如资源有限，至少在 Limitations 中将模型规模单一性列为核心限制，并讨论可能的影响方向。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Black-box access" framing 有 overclaim 嫌疑

- 具体位置：Abstract ("the framework requires only binary response patterns from the target model—no access to weights, gradients, logits, or training data"), Section 3.1, Appendix H
- 问题：Abstract 强调 "only binary response patterns"，但框架实际上**严重依赖** PSN-IRT 提供的外部预校准 4PL 参数（来自 13,000+ 模型的校准结果）。Appendix H 自己证明了没有 PSN-IRT 时，经典 MML-EM 估计的 discrimination 参数相关性仅 r_s=0.127，本质上无效。这意味着 "black-box" 只对目标模型成立，但对整体框架而言，需要一个庞大的外部校准基础设施。此外，Section 3.2 的 Δl_z^* 设计需要 n=10 个 clean seed baseline，这也是非平凡的前提条件。
- 建议：在 Abstract 中加入对 PSN-IRT 依赖的简短说明（如 "combined with externally calibrated item parameters"），避免给读者造成 "仅需二值响应即可使用" 的印象。当前 Abstract 虽然提到了 "externally calibrated 4PL item parameters"，但这句嵌在长句中不够突出。

**W2** [warning] 部分发现可由 IRT 理论直接预测，novelty 有限

- 具体位置：Finding 2 (Section 4.3), Finding 3 (Section 4.4)
- 问题：
  - **Finding 2**（θ-shift dynamics）：高能力模型接近 4PL 上渐近线，留给 aberrance 信号的空间更小——这是 IRT 中众所周知的天花板效应（ceiling effect）。论文称之为 "θ-shift absorption mechanism"，但本质是 ability 接近 upper asymptote 时 residual 信号被压缩的数学必然。
  - **Finding 3**（detection-diagnosis tradeoff）：l_z^* 是专门设计用于 response pattern 诊断而非 level detection 的统计量（Snijders, 2001），因此它在检测任务上不如 accuracy z-score 几乎是 by design 的结果。
- 建议：在论文中更明确地区分哪些发现是 "empirical validation of IRT predictions in a new domain"（有价值但 novelty 有限），哪些是 "genuinely surprising findings that IRT theory alone cannot predict"。Finding 1（inverted-U dose-response）和 Finding 4（if properly supported）更可能属于后者。

**W3** [warning] Inverted-U dose-response 的普适性声明过强

- 具体位置：Section 4.2, Finding 1
- 问题：三点 inverted-U 形态仅在 Qwen（free-θ estimation）上清晰观察到（l_z^* 从 6.58 升至 8.22 再降至 1.90）。Llama 和 Mistral 均显示 monotonic dose-response（Section 4.2: "Llama and Mistral show monotonic dose-response, consistent with their lower baseline ability"）。论文将此归因于 baseline ability 差异，但 2/3 模型不展示 inverted-U 意味着这不是一个 robust finding。
- 建议：在 Abstract 和 Section 4.2 的标题中增加限定词，如 "ability-dependent inverted-U dose-response" 而非暗示所有模型都有 inverted-U。

**W4** [warning] Benchmark 覆盖面偏窄

- 具体位置：Section 3.3
- 问题：仅使用 MMLU（14,042 items）和 ARC-C（295 items）两个 benchmark。虽然两者规模差异大，提供了有用对比，但缺少其他常用 benchmark（如 HellaSwag、GSM8K、WinoGrande）。特别是 ARC-C 仅 295 items，论文自己在 Section 4.1 承认 "the small item count amplifies this concentration"。这限制了 ARC-C 上发现的统计可靠性。
- 建议：增加 1-2 个中等规模的 benchmark（如 HellaSwag ~10K items）以验证发现的跨 benchmark 稳健性。

**W5** [warning] 遗漏直接相关的近期工作

- 具体位置：Section 2 Related Work
- 问题：Han et al. (2025/2026) "Quantifying Data Contamination in Psychometric Evaluations of LLMs"（EACL 2026 Findings, arXiv 2510.07175）直接处于 psychometrics 和 contamination 的交叉点，提出了系统化的心理测量评估污染框架，但未被引用。虽然该工作侧重 personality inventories 而非 ability benchmarks，但方法论上高度相关。另外，RADAR (Zawalski et al., 2025, arXiv 2510.08931) 作为近期有影响力的 mechanistic contamination detection 工作也值得讨论（与本文的 "behavioral characterization" 形成对比）。
- 建议：在 Related Work 中补充上述工作的讨论，特别是 Han et al. 与本文的方法论对比。

---

## 小问题（不影响接收）

- Section 3.1: "We adopt the four-parameter logistic (4PL) IRT model" — 4PL model 的 upper asymptote d 在 contamination 场景下的行为值得一提（contaminated model 可能有 d<1，但这被 PSN-IRT 固定参数忽略了）
- Figure 2: 灰色 cells 标注 "missing conditions (Llama and Mistral on ARC-C not included in the current study)" — 为什么排除这些条件？应简要说明原因
- Table 2: fixed-θ vs free-θ 的对比非常有信息量，但 "fixed-θ estimation can recover monotonicity by eliminating the absorption mechanism (§4.3)" 的因果论述缺乏统计检验支撑
- Section 4.4 Table 3: "l_z^* provides unique diagnostic capabilities (§4.4)" — 但论文未展示这种 diagnostic capability 的具体应用场景（即在什么实际 workflow 中需要 item-level diagnosis 而非 detection）

---

## 主要优势

1. **跨学科桥梁构建得当**：将 educational testing 中成熟的 person-fit 统计量（l_z^*）系统性地迁移到 LLM 污染检测是一个自然且有价值的联系。论文对心理测量学文献的引用准确且全面（Snijders 2001, Karabatsos 2003, Meijer & Sijtsma 2001）。
2. **实验设计严谨**：3 contamination levels × 3 model families × n=10 seeds × 2 benchmarks 的 factorial design 配合 bootstrap 95% CI 和 Cohen's d 效应量，统计报告质量高于多数 NLP 论文。Δl_z^* 差分设计是对 IRT 假设违反的巧妙应对。
3. **Finding 1（inverted-U dose-response）是真正新颖的 empirical insight**：θ-shift absorption 导致高污染水平下检测信号反而减弱，这一现象不能从 IRT 理论直接预测（需要知道 SFT 对 ability 的具体影响方式），对污染检测方法设计有实际启示。
4. **诚实的 framing**：论文将自身定位为 "characterization" 而非 "detection tool"，并在 Limitations 中诚实列出了范围限制。这种学术诚实值得肯定。
5. **Appendix H 的自我审视**：主动验证了 PSN-IRT 依赖性的必要性，展示了经典 MML-EM 在少量模型下的失效（r_s=0.127），增强了方法选择的说服力。

---

## 关于 "characterization" 定位是否支撑 Long Paper

论文定位为 characterization study 而非 detection method，这在学术上诚实但在 contribution density 上有风险。四大发现中：
- Finding 1 是真正新颖的（但仅在 1/3 模型上完整展示）
- Finding 2 和 3 部分可由 IRT 理论预测
- Finding 4 是 N=1 的 preliminary observation

对于一个 8 页的 long paper，这个 contribution density 更接近 Findings 水平。如果 Finding 4 能获得充分实验支撑（多模型族 × 多 RL 方法），或者 N2（baseline 对比）能得到解决，论文可达到 3.5（Borderline Conference）。

---

## 总评

本文做了一个有价值的跨学科迁移工作，将心理测量学的 person-fit 统计量引入 LLM 污染检测领域。实验设计严谨，统计报告质量高。然而，作为 long paper 投稿，存在几个实质性问题：(1) 四大核心发现中 Finding 4 缺乏充分支撑，(2) 未与 ConStat 等现有方法进行实证对比，(3) 模型规模覆盖过窄（全部 7-8B），(4) 部分发现（Finding 2, 3）的 novelty 受限于 IRT 理论的可预测性。这些问题使得论文目前更适合 Findings 而非主会议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 457 · 2026-05-22T04:53:52.179432+00:00_

Reviewer 2 审稿意见已收到。评分 3.0 (Findings)，3 个 critical issues（Post-RL N=1 overclaim、缺乏实证 baseline 对比、模型规模单一），5 个 should-fix。

等待 Reviewer 1 提交审稿意见后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 46

## Round 46

2 recorded events


### User

_source line 458 · 2026-05-22T04:54:00.505728+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：评分 Overall 3.0（Findings 级别）。主要问题：(1) Finding 4 (post-RL) 仅 N=1 却列为核心贡献；(2) 未与 ConStat 等方法实证对比；(3) 模型全部 7-8B，规模覆盖不足。主要优势：跨学科迁移有价值、实验设计严谨、Finding 1 (inverted-U dose-response) 是真正新颖的 empirical insight。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 459 · 2026-05-22T04:54:07.923703+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 47

## Round 47

6 recorded events


### User

_source line 460 · 2026-05-22T04:56:02.237150+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性审查

**论文**: What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审查侧重**: 方法严谨性（实验设计、统计方法、Claims-Evidence对齐、IRT理论应用）

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 将心理测量学 person-fit 统计量迁移到 LLM 污染检测是有原创性的贡献，但核心发现的证据基础偏薄——inverted-U 仅依赖 1 个模型 3 个数据点、实验设计矩阵不完整、25% 污染条件未在实验设置中描述，这些方法论问题削弱了可信度。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心检测有效性（Table 1 所有 CI 排除零）有充分支撑，但 inverted-U 和 post-RL 两个发现证据薄弱；实验矩阵有缺失 |
| Excitement | 3/5 | IRT person-fit → LLM 污染的连接新颖且有启发性，但实际检测能力不如简单 accuracy z-score（论文自己承认），实用价值有限 |
| Reproducibility | 4/5 | QLoRA 配置、bootstrap 参数、PSN-IRT 来源均有报告；代码承诺开源；但 25% 条件的实验设置未完整描述 |
| Confidence | 4/5 | 我熟悉 IRT 方法论和 LLM 评估领域，仔细阅读了全文及全部附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 25% 污染条件未在实验设置中描述，存在方法论透明性问题

- 具体位置：§3.3 (Experimental Setup) vs. Table 1 & §4.2
- 问题：§3.3 明确写道 "Each is fine-tuned with QLoRA... under **three conditions**: clean, 15% contamination, and 50% contamination"，但 Table 1 包含 Qwen 25% 污染的 Cohen's d 数据（d=−8.22），且 inverted-U 发现（论文第一大贡献）完全依赖这个数据点。这个条件仅在 Qwen 上运行，Llama 和 Mistral 的 25% 列为 "---"。
- 关键疑问：25% 条件是先验计划还是看到 15% 和 50% 的非单调趋势后追加的？如果是后者，这构成 researcher degrees of freedom，必须在 §3.3 透明披露，并在解读中标注为 post-hoc 探索。
- 为什么影响接收：inverted-U 是四大发现之首，其核心证据（25% 峰值）的实验来源不透明，直接损害可信度。
- 建议修改方向：在 §3.3 明确描述所有实验条件（包括 25%），说明运行 25% 的动机和时间顺序，如果是 post-hoc 则标注。

**N2** [critical] Inverted-U 证据不足以支撑其作为第一大发现的地位

- 具体位置：Abstract Finding (1), §4.2, Figure 3
- 问题：inverted-U dose-response 仅基于 **1 个模型家族（Qwen）的 3 个数据点**（15%, 25%, 50%）。Llama 和 Mistral 显示单调 dose-response（与 inverted-U 相反），且未测试 25% 条件，因此无法判断 inverted-U 是 Qwen 特异性现象还是仅因其他模型缺少中间数据点而未观察到。3 个点的非单调性也可能由噪声产生——尤其考虑到 bootstrap CI 极宽（d(25%) CI: [−18.9, −5.7]，跨度 13.2）。
- 为什么影响接收：作为论文第一大贡献，证据强度与 claim 突出度严重不匹配。论文虽在正文中限定为 "specific to Qwen"，但 abstract 和 introduction 将其列为首要发现，读者会认为这是经过充分验证的结论。
- 建议修改方向：(a) 补充 Llama/Mistral 的 25% 数据以验证模型特异性假说；或 (b) 将 inverted-U 从 "empirical finding" 降级为 "preliminary observation"，调整其在 abstract/introduction 中的位次和表述强度。

**N3** [critical] 实验设计矩阵不完整，削弱跨模型/跨基准的通用性 claim

- 具体位置：Table 1, Figure 2, §3.3
- 问题：论文声称在 "three model families" 和 "two benchmarks" 上验证，但实际设计矩阵严重不完整：
  - ARC-C 仅在 Qwen 上测试（Llama/Mistral 缺失）
  - 25% 污染仅在 Qwen 上测试（Llama/Mistral 缺失）
  - Mistral 仅 n=6 seeds（vs. Qwen/Llama n=10）
  完整的 3×2×3 设计应有 18 个实验条件（3 模型 × 2 基准 × 3 污染水平），实际仅完成约 8 个。Figure 2 heatmap 的灰色格子直观地暴露了这一问题。
- 为什么影响接收：跨模型通用性和跨基准的 benchmark size effect（§4.3 第 70-73 行关于 ARC-C ceiling effect 的讨论）无法在其他模型上验证。Abstract 中 "across three 7–8B model families" 的表述暗示了完整覆盖。
- 建议修改方向：至少补充 Llama/Mistral 在 ARC-C 上的实验，或在 abstract 和 claims 中明确限定覆盖范围。

**N4** [critical] Abstract 事实错误："n=10 seeds each"

- 具体位置：Abstract 第 4 行
- 问题：Abstract 写 "across three 7–8B model families (n=10 seeds each)"，但 §3.3 明确说 Mistral 仅 n=6（"four checkpoints were lost when a training server was decommissioned"）。这是事实性错误。
- 建议修改方向：改为 "(n=10 seeds for Qwen and Llama, n=6 for Mistral)" 或 "(n≥6 seeds each)"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] QLoRA SFT 作为污染代理的生态效度有限

- 具体位置：§3.3 "Contamination model" 段落
- 问题：论文使用 QLoRA SFT（rank=16, α=32）模拟污染，但实际 SFT 污染可能使用不同 LoRA rank、全参数微调、或更复杂的数据混合策略。更关键的是，最常见的污染形式是预训练阶段污染（pretraining contamination），其学习动态与 SFT 根本不同。论文标题 "What Can Binary Response Patterns Reveal About Benchmark Contamination?" 的范围远大于 SFT-only 的实验证据。§3.3 最后一句和 Limitations 都承认了这一限制，但 title/abstract 的 framing 未充分反映。
- 建议：在 title 或 abstract 中加入 "SFT-stage" 限定词，或在 introduction 更显著地讨论这一范围限制。

**W2** [warning] "Black-box access" framing 有误导性

- 具体位置：Title, Abstract, §1 (多处)
- 问题：论文反复强调 "black-box access"（"no access to weights, gradients, logits, or training data"），但方法实际依赖：(a) PSN-IRT 预校准的 4PL item parameters（外部 item bank），(b) 知道目标模型使用了哪个 benchmark，(c) θ-fixed 方法还需要 clean baseline models。Abstract 确实做了 qualify（"combined with externally calibrated 4PL item parameters"），但 "black-box" 这个标签在论文中使用了至少 5 次，给读者的印象是方法仅需模型输出。更准确的描述是 "binary-response + external item bank" access level。
- 建议：考虑使用更精确的术语替代 "black-box"，或在首次使用时明确定义 "black-box" 在本文语境下的含义（指对模型本身的 black-box，不含对 item parameters 的要求）。

**W3** [warning] Bootstrap CI 在小样本下的可靠性

- 具体位置：§3.2, Table 1, Table 2
- 问题：主要结果使用 n=10（Mistral n=6）seeds 的 bootstrap percentile CI（10,000 resamples）。有限样本下 bootstrap percentile CI 的覆盖率已知不可靠（Efron & Tibshirani 1993, Ch. 12）。CI 极宽（如 Qwen 25%: [−18.9, −5.7]，跨度 13.2）反映了这一不确定性。Appendix G 提供了 BCa 校正作为 sensitivity check（CI 平均缩窄 22%），这很好，但主文结果仍基于 percentile CI。
- 特别关注 Mistral（n=6）：从 6 个数据点进行 10,000 次 bootstrap resampling，实际上只有 C(6+5,5)=462 种可能的 bootstrap 样本，bootstrap 分布是离散的，percentile CI 的精度受限。
- 建议：主文报告 BCa CI 而非 percentile CI；或至少讨论小样本 bootstrap 的局限性。

**W4** [warning] Post-RL 发现（N=1）在论文中的权重过大

- 具体位置：Abstract Finding (4), §1 Contribution (4), §4.5, Figure 4
- 问题：Post-RL 结果基于单一模型（Qwen）、单一污染水平（15%）、单一 RL 方法（GRPO），且论文明确声明 "No statistical inference is drawn"（§4.5）。但它仍被列为四大贡献之一，占据完整的 §4.5 和 Figure 4。论文在正文中的 hedging 是恰当的（"preliminary observation"），但 abstract 中 "(N=1)" 的标注容易被忽略，在 introduction 中作为第四个 enumerated finding 的突出位置暗示了它与其他三个发现同等份量。
- 建议：考虑将 §4.5 移入附录或缩短为 Discussion 中的一段，在 abstract 中降级其表述。

**W5** [warning] PSN-IRT 校准循环性——随机扰动分析未覆盖系统性偏差

- 具体位置：Discussion "Scope and calibration" 段, Appendix F.2
- 问题：PSN-IRT 的 13,000+ 模型校准样本可能包含已被污染的模型。Appendix F.2 通过 ±10% 随机噪声扰动测试鲁棒性，但被污染模型引入的偏差是**系统性**的（高估 θ → 偏移 item difficulty 参数），而非随机的。随机扰动分析无法覆盖系统性偏差的场景。
- 建议：讨论系统性偏差与随机噪声的区别；或设计一个模拟实验，在校准样本中注入不同比例的被污染模型，观察 item parameters 和下游 ℓz* 的偏移。

**W6** [warning] Cohen's d 计算将被污染模型视为固定点

- 具体位置：§3.2, Table 1
- 问题：Δℓz* 设计将每个被污染模型的 ℓz* 视为固定值，仅通过 clean seeds 的变异计算 Cohen's d。但被污染模型本身也有 seed-dependent variability（不同随机初始化、数据顺序等会产生不同的污染 ℓz*）。当前设计低估了真实不确定性。如果每个污染条件只有 1 次运行，则 d 的点估计完全取决于该次运行的随机性。
- 建议：明确报告每个污染条件的运行次数；如仅 1 次，讨论这一限制；理想情况应有多次被污染运行以估计双方变异。

**W7** [warning] Local dependence 模拟可能未捕捉真实 LLM 依赖结构

- 具体位置：Appendix F.1
- 问题：LD 鲁棒性分析使用 testlet 模型（Gaussian random effects）模拟局部依赖。真实 LLM 响应的依赖结构可能更复杂（共享推理链、in-context learning、训练数据相关性等），不一定服从 testlet+Gaussian 假设。模拟在一类偏离下提供了保证，但不能推广到任意依赖结构。
- 建议：在 Appendix F.1 或 Discussion 中讨论模拟假设的局限性，以及在何种依赖结构下 ΔlZ* 可能失效。

---

## 小问题（不影响接收）

- Table 1 的 25% 列应更清晰地标注仅适用于 Qwen（当前通过 "---" 表示缺失，但列头未说明）
- §4.2 第 47 行 "4.3× reduction from peak to high contamination"：这个倍数是 d(25%)/d(50%) = 8.22/1.90 = 4.33，从 peak 到 high 的描述准确，但也可解释为 noise
- Figure 3 caption 提到 "three-point trajectory"，但实验设置中未描述 25% 条件，caption 应加注
- §4.3 第 66 行关于 MMLU 50% 处 accuracy vs. |d| 的负相关只有 3 个数据点，不应称为 "correlation"——这是 3 个点的排序一致性
- Reproducibility Statement 中 "random seeds are reported for all experiments" 但正文中未列出具体 seed 值
- §4.4 第 124 行 accuracy z-score 的 |d|=68.7 反映的是 near-zero cross-seed accuracy variance（SD≈0.0003），正文已解释但可能仍会误导读者认为 z-score 是更好的检测器

---

## 主要优势

1. **原创性贡献**：将心理测量学 person-fit 统计量（ℓz*）迁移到 LLM 污染检测，连接了两个此前独立的研究领域。类比关系（被污染 LLM ≈ 作弊考生）自然且有说服力。

2. **DiD 设计巧妙**：57/60 model-benchmark cells 在无污染下即产生 |ℓz*| > 1.96，说明绝对阈值不可用。Δℓz* differencing 设计将系统性 IRT 违反转化为可控特征，模拟验证（Appendix F.1）支持其在 shared LD 下的鲁棒性（d_ratio ≥ 0.93 for σ_τ ≤ 0.5）。

3. **诚实的 framing**：论文将自己定位为 "characterization" 而非 "detection tool"，明确承认简单 accuracy z-score 检测力更强（Table 3），ℓz* 的价值在于诊断而非检测。这种自我批评的诚实态度在投稿论文中不常见。

4. **Detection-diagnosis tradeoff 是有实际价值的洞见**：§4.4 和 Table 3 系统对比了 ℓz*、HT、accuracy z-score 的检测力和诊断力，two-stage workflow 建议（先 z-score 筛查，再 ℓz* 诊断）具有实际指导意义。

5. **附录鲁棒性分析较全面**：4PL vs. 3PL ablation（Appendix B）、LD 模拟（Appendix F.1）、参数扰动（Appendix F.2）、BCa 校正（Appendix G）、MML-EM refit 失败分析（Appendix H）覆盖了多个潜在质疑方向。

6. **θ-shift absorption 机制解释有理论深度**：高能力模型在高污染下检测信号反而减弱的现象（Qwen d=6.58@15% → 1.90@50%）不是显而易见的，论文从 IRT 理论（MLE θ 估计吸收异常信号）给出了清晰的因果解释，并通过 fixed-θ vs. free-θ 对比（Table 2）验证了机制。

---

## 格式合规检查

| 项目 | 状态 | 说明 |
|------|------|------|
| 正文页数 | ✅ 合规 | 主文（§1-§6 + Conclusion）在第 8 页结束 |
| 模板 | ✅ 合规 | `\usepackage[review]{acl}` |
| 匿名性 | ✅ 合规 | 作者 "Anonymous"，未见去匿名化信息 |
| Limitations | ✅ 存在 | 第 9 页，覆盖模型规模、SFT 范围、N=1 post-RL、IRT 假设违反、PSN-IRT 依赖 |
| 参考文献 | ✅ | 第 9-10 页，不计入页数 |
| 附录 | ✅ | 第 11-14 页，放在参考文献之后 |

---

## 总结

这是一篇有明确原创贡献的论文，将 IRT person-fit 引入 LLM 污染检测是新颖且有潜力的研究方向。DiD 设计和 detection-diagnosis tradeoff 分析是论文的核心亮点。然而，方法论上的问题较为集中：(1) 第一大发现 inverted-U 的证据基础过于薄弱（1 模型 × 3 点），(2) 实验设计矩阵不完整导致跨模型/跨基准的通用性 claim 缺乏支撑，(3) 25% 污染条件的实验来源不透明。如果能补充实验数据填充设计矩阵，并调整 inverted-U 和 post-RL 发现的 claim 强度，本文有望达到 Conference（4.0）水准。当前状态更适合 Findings。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 461 · 2026-05-22T04:56:41.858254+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "irt_personfit_contam",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性）— Overall 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 25% 污染条件未在实验设置中描述，存在方法论透明性问题\n- §3.3 明确写道 \"three conditions: clean, 15% contamination, and 50% contamination\"，但 Table 1 包含 Qwen 25% 数据（d=−8.22），且 inverted-U 发现完全依赖这个数据点。25% 条件仅在 Qwen 上运行。关键疑问：25% 是先验计划还是看到 15%/50% 非单调趋势后追加的？如果是 post-hoc，构成 researcher degrees of freedom。\n\n**N2** [critical] Inverted-U 证据不足以支撑其作为第一大发现的地位\n- 仅基于 1 个模型家族（Qwen）的 3 个数据点。Llama/Mistral 显示单调 dose-response（与 inverted-U 相反），且未测试 25%。CI 极宽（d(25%) CI: [−18.9, −5.7]，跨度 13.2）。\n\n**N3** [critical] 实验设计矩阵不完整，削弱跨模型/跨基准的通用性 claim\n- 完整 3×2×3 设计应有 18 个条件，实际仅完成约 8 个。ARC-C 仅 Qwen，25% 仅 Qwen，Mistral n=6。\n\n**N4** [critical] Abstract 事实错误：\"n=10 seeds each\"\n- Mistral 实际 n=6。\n\n### Should-Fix 问题\n\n**W1** QLoRA SFT 作为污染代理的生态效度有限——title/abstract framing 范围超出实验证据\n**W2** \"Black-box access\" framing 有误导性——方法依赖 PSN-IRT 外部 item bank + clean baseline\n**W3** Bootstrap CI 在小样本下的可靠性——Mistral n=6 仅 462 种可能 bootstrap 样本\n**W4** Post-RL 发现（N=1）权重过大\n**W5** PSN-IRT 校准循环性——随机扰动分析未覆盖系统性偏差\n**W6** Cohen's d 计算将被污染模型视为固定点——低估真实不确定性\n**W7** Local dependence 模拟可能未捕捉真实 LLM 依赖结构\n\n### 主要优势\n1. 原创性贡献（IRT person-fit → LLM 污染检测）\n2. DiD 设计巧妙\n3. 诚实的 framing（characterization 而非 tool）\n4. Detection-diagnosis tradeoff 有实际价值\n5. 附录鲁棒性分析全面\n6. θ-shift absorption 机制解释有理论深度\n\n---\n\n请逐条回应上述 Must-Fix 和 Should-Fix 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "irt_personfit_contam",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性）— Overall 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 25% 污染条件未在实验设置中描述，存在方法论透明性问题\n- §3.3 明确写道 \"three conditions: clean, 15% contamination, and 50% contamination\"，但 Table 1 包含 Qwen 25% 数据（d=−8.22），且 inverted-U 发现完全依赖这个数据点。25% 条件仅在 Qwen 上运行。关键疑问：25% 是先验计划还是看到 15%/50% 非单调趋势后追加的？如果是 post-hoc，构成 researcher degrees of freedom。\n\n**N2** [critical] Inverted-U 证据不足以支撑其作为第一大发现的地位\n- 仅基于 1 个模型家族（Qwen）的 3 个数据点。Llama/Mistral 显示单调 dose-response（与 inverted-U 相反），且未测试 25%。CI 极宽（d(25%) CI: [−18.9, −5.7]，跨度 13.2）。\n\n**N3** [critical] 实验设计矩阵不完整，削弱跨模型/跨基准的通用性 claim\n- 完整 3×2×3 设计应有 18 个条件，实际仅完成约 8 个。ARC-C 仅 Qwen，25% 仅 Qwen，Mistral n=6。\n\n**N4** [critical] Abstract 事实错误：\"n=10 seeds each\"\n- Mistral 实际 n=6。\n\n### Should-Fix 问题\n\n**W1** QLoRA SFT 作为污染代理的生态效度有限——title/abstract framing 范围超出实验证据\n**W2** \"Black-box access\" framing 有误导性——方法依赖 PSN-IRT 外部 item bank + clean baseline\n**W3** Bootstrap CI 在小样本下的可靠性——Mistral n=6 仅 462 种可能 bootstrap 样本\n**W4** Post-RL 发现（N=1）权重过大\n**W5** PSN-IRT 校准循环性——随机扰动分析未覆盖系统性偏差\n**W6** Cohen's d 计算将被污染模型视为固定点——低估真实不确定性\n**W7** Local dependence 模拟可能未捕捉真实 LLM 依赖结构\n\n### 主要优势\n1. 原创性贡献（IRT person-fit → LLM 污染检测）\n2. DiD 设计巧妙\n3. 诚实的 framing（characterization 而非 tool）\n4. Detection-diagnosis tradeoff 有实际价值\n5. 附录鲁棒性分析全面\n6. θ-shift absorption 机制解释有理论深度\n\n---\n\n请逐条回应上述 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 462 · 2026-05-22T04:57:01.944448+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20086
}
```

</details>

---


### Tool call

_source line 463 · 2026-05-22T04:57:02.145751+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "irt_personfit_contam",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性/完整性）— Overall 3.0 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] Finding 4 (Post-RL residual pattern) 作为核心发现缺乏充分支撑\n- N=1（Qwen+GRPO, 15%），无统计推断。但 Abstract 将其列为四大核心贡献之一，与 3×3 factorial design 支撑的发现并列。建议从核心贡献列表移除或降级。\n\n**N2** [critical] 缺乏与现有 detection 方法的实证对比\n- 仅对比 accuracy z-score、HT、ℓz* 三个 person-fit 相关统计量，未与 ConStat/PaCoST/CoDeC 在相同设置下对比。Section 4.4 的结论是 simpler statistics yield stronger detection——论文自身核心工具 ℓz* 在检测任务上劣于更简单方法。\n\n**N3** [critical] 模型规模覆盖不足\n- 全部 3 个模型族在 7-8B 范围。Finding 2（baseline ability modulates detection sensitivity）仅在同一规模档的三个模型间建立，无法区分 ability-driven vs. scale-driven。\n\n### Should-Fix 问题\n\n**W1** \"Black-box access\" framing 有 overclaim 嫌疑——框架严重依赖 PSN-IRT 外部参数\n**W2** 部分发现可由 IRT 理论直接预测，novelty 有限（Finding 2 天花板效应，Finding 3 ℓz* by design 不是最佳检测器）\n**W3** Inverted-U dose-response 普适性声明过强——仅 Qwen 展示完整 inverted-U\n**W4** Benchmark 覆盖面偏窄——仅 MMLU + ARC-C\n**W5** 遗漏直接相关近期工作——Han et al. (EACL 2026 Findings) 心理测量×污染交叉点；RADAR (Zawalski et al., 2025)\n\n### 主要优势\n1. 跨学科桥梁构建得当\n2. 实验设计严谨（3×3 factorial + bootstrap CI）\n3. Finding 1（inverted-U）是真正新颖的 empirical insight\n4. 诚实的 framing\n5. Appendix H 自我审视\n\n### 关于 contribution density\n- Finding 1 真正新颖但仅 1/3 模型完整展示\n- Finding 2, 3 部分可 IRT 理论预测\n- Finding 4 是 N=1 preliminary\n- Contribution density 更接近 Findings 水平\n\n---\n\n请逐条回应上述 Must-Fix 和 Should-Fix 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "irt_personfit_contam",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性/完整性）— Overall 3.0 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] Finding 4 (Post-RL residual pattern) 作为核心发现缺乏充分支撑\n- N=1（Qwen+GRPO, 15%），无统计推断。但 Abstract 将其列为四大核心贡献之一，与 3×3 factorial design 支撑的发现并列。建议从核心贡献列表移除或降级。\n\n**N2** [critical] 缺乏与现有 detection 方法的实证对比\n- 仅对比 accuracy z-score、HT、ℓz* 三个 person-fit 相关统计量，未与 ConStat/PaCoST/CoDeC 在相同设置下对比。Section 4.4 的结论是 simpler statistics yield stronger detection——论文自身核心工具 ℓz* 在检测任务上劣于更简单方法。\n\n**N3** [critical] 模型规模覆盖不足\n- 全部 3 个模型族在 7-8B 范围。Finding 2（baseline ability modulates detection sensitivity）仅在同一规模档的三个模型间建立，无法区分 ability-driven vs. scale-driven。\n\n### Should-Fix 问题\n\n**W1** \"Black-box access\" framing 有 overclaim 嫌疑——框架严重依赖 PSN-IRT 外部参数\n**W2** 部分发现可由 IRT 理论直接预测，novelty 有限（Finding 2 天花板效应，Finding 3 ℓz* by design 不是最佳检测器）\n**W3** Inverted-U dose-response 普适性声明过强——仅 Qwen 展示完整 inverted-U\n**W4** Benchmark 覆盖面偏窄——仅 MMLU + ARC-C\n**W5** 遗漏直接相关近期工作——Han et al. (EACL 2026 Findings) 心理测量×污染交叉点；RADAR (Zawalski et al., 2025)\n\n### 主要优势\n1. 跨学科桥梁构建得当\n2. 实验设计严谨（3×3 factorial + bootstrap CI）\n3. Finding 1（inverted-U）是真正新颖的 empirical insight\n4. 诚实的 framing\n5. Appendix H 自我审视\n\n### 关于 contribution density\n- Finding 1 真正新颖但仅 1/3 模型完整展示\n- Finding 2, 3 部分可 IRT 理论预测\n- Finding 4 是 N=1 preliminary\n- Contribution density 更接近 Findings 水平\n\n---\n\n请逐条回应上述 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 464 · 2026-05-22T04:57:03.707640+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1561
}
```

</details>

---


### Assistant

_source line 465 · 2026-05-22T04:57:06.761487+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 48

## Round 48

2 recorded events


### User

_source line 466 · 2026-05-22T04:57:09.403816+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审查结论**：Overall 3.5（Borderline Conference）。论文将 IRT person-fit 引入 LLM 污染检测具有原创性，DiD 设计和 detection-diagnosis tradeoff 分析是亮点。但方法论有 4 个 Must-Fix 问题：

1. **25% 污染条件未在 §3.3 实验设置中描述**——inverted-U 的核心证据来源不透明
2. **Inverted-U 证据薄弱**——仅 1 个模型 3 个数据点，且 25% 未在其他模型验证
3. **实验矩阵不完整**——ARC-C 仅测 Qwen，25% 仅测 Qwen，完整 3×2×3 设计仅完成约 8/18 格
4. **Abstract 事实错误**——写 "n=10 seeds each" 但 Mistral 实际 n=6

当前状态更适合 Findings；补充实验数据并调整 claim 强度后有望达到 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 467 · 2026-05-22T04:57:22.456841+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 49

## Round 49

2 recorded events


### User

_source line 468 · 2026-05-22T04:58:49.595596+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 25% 污染条件的透明性问题**

同意这是一个严重的方法论透明性缺陷。§3.3 明确列出 "three conditions: clean, 15% contamination, and 50% contamination"，但 Table 1 和 Section 4.2 的 inverted-U 论证完全依赖 Qwen 25% 数据点。论文未在任何位置说明 25% 是预先计划还是事后追加。如果是看到 15%→50% 非单调趋势后追加的 post-hoc 条件，这构成经典的 researcher degrees of freedom 问题，且恰好发生在论文的 Finding 1（最核心发现）上，问题严重。即使不是 post-hoc，§3.3 的描述与实际实验的不一致本身就是方法论写作缺陷。

**[AGREE] R1-N2: Inverted-U 证据不足**

强烈同意。我在自己的审稿中也将此列为 W3。补充 R1 的论证：
- 3 个数据点（15%, 25%, 50%）拟合一条非单调曲线在统计上本质是 underdetermined——任何 3 点都可以拟合二次函数
- Llama 和 Mistral 均显示单调 dose-response（Section 4.2 原文："Llama and Mistral show monotonic dose-response"），即 2/3 模型不支持 inverted-U
- 论文用 baseline ability 差异解释了不一致性（高能力模型 Qwen 展示 inverted-U，低能力模型展示单调），但这个解释本身未经验证——需要在同一模型族的不同 ability 水平（如 Qwen-1.8B vs Qwen-72B）上验证
- 作为 Finding 1 的地位与其证据强度严重不匹配

**[AGREE] R1-N3: 实验设计矩阵不完整**

同意，但我认为问题的严重程度需要分层讨论。Figure 2 中灰色 cells 表明 Llama 和 Mistral 在 ARC-C 上的条件缺失，25% 仅覆盖 Qwen。这意味着：
- 跨 benchmark 的发现（如 Finding 2 的 θ-shift dynamics）在 ARC-C 上仅基于 Qwen，无法声称跨模型普适性
- 但对于 MMLU 上的核心发现（Table 1），3 个模型族 × 2 个污染水平的 6 个基本条件是完整的
- 不完整矩阵的主要后果是削弱了 ARC-C 相关结论和 inverted-U 发现的可信度，而非全面否定论文

我在自己的 N3 中提出了一个互补的关注点：所有模型都在 7-8B 规模，缺乏不同模型规模的覆盖。R1 关注的是实验矩阵内部的完整性，我关注的是矩阵外部的覆盖范围——两者叠加意味着 generalizability claims 的支撑确实不够。

**[AGREE] R1-N4: Abstract 事实错误 "n=10 seeds each"**

完全同意。§3.3 明确写道 "n=6 for Mistral (four checkpoints were lost when a training server was decommissioned during the study)"，但 Abstract 写 "n=10 seeds each"。这是必须修正的事实错误，无论原因如何。修复很简单：Abstract 改为 "n=10 seeds for Qwen and Llama, n=6 for Mistral"。

---

### Should-Fix 问题

**[AGREE] R1-W1: QLoRA SFT 生态效度与 framing 范围**

同意。标题 "What Can Binary Response Patterns Reveal About Benchmark Contamination?" 暗示广泛适用性，但实验仅覆盖 QLoRA SFT 单一污染路径。论文在 Limitations 中承认 "our findings are scoped to SFT-based contamination and may not generalize to pretraining contamination"，但标题和 Abstract 未做此限定。不过我认为这是 Should-Fix 而非 Must-Fix——论文在 Section 1 Introduction 中确实明确了 "we focus on SFT-stage contamination" 的 scope。

**[AGREE] R1-W2: "Black-box access" framing**

强烈同意。我在自己的审稿中将此列为 W1，论证一致：框架依赖 PSN-IRT 外部 item bank（13,000+ 模型校准结果）和 clean baseline seeds，"only binary response patterns" 的表述不够准确。Appendix H 的 MML-EM 实验（r_s=0.127）进一步证实了 PSN-IRT 依赖的不可替代性。

**[REBUT] R1-W3: Bootstrap CI 在 Mistral n=6 下的可靠性**

部分反驳。R1 称 n=6 仅有 "462 种可能 bootstrap 样本"——这个数字对应的是 C(11,6)=462（从 6 个元素有放回抽取 6 个的唯一多重集数），但实际 bootstrap 样本空间是 6^6=46,656（有放回有序抽样）。更重要的是，bootstrap percentile CI 在 n=6 时确实 coverage 较差（BCa 校正可部分缓解），但论文在 Appendix G 报告了 BCa bootstrap CI 作为 sensitivity check，且发现 "BCa CIs were uniformly narrower than the percentile CIs reported in the main text (mean reduction 22%)"。因此：
- n=6 的 CI 确实不如 n=10 可靠——这是事实
- 但论文有 BCa 校正作为补充（Appendix G），且 Mistral 的核心定性结论（l_z^* 在污染条件下显著偏离零）的效应量足够大，不太可能被 CI 不确定性翻转
- 建议在正文中对 Mistral n=6 的 CI 加注 caveat，但不认为这影响核心结论

**[AGREE] R1-W4: Post-RL 发现权重过大**

强烈同意。我在自己的审稿中将此列为 N1（Must-Fix 级别）。Finding 4 基于 N=1（单一模型族+单一 RL 方法+单一污染水平），Section 4.5 自己承认 "no statistical inference is drawn"，但 Abstract 将其与其他三个有 factorial design 支撑的发现并列。这是 contribution scope 膨胀。

**[AGREE] R1-W5: PSN-IRT 校准循环性**

同意 R1 关于系统性偏差未被覆盖的关注。Appendix F.2 的 robustness analysis 通过向参数添加随机噪声验证了对随机扰动的鲁棒性（Table 11-12），但正如 R1 指出的，如果 PSN-IRT 校准样本中包含已被污染的模型（这在 13,000+ 模型中几乎必然），item 参数可能存在系统性偏差（如 difficulty 被低估）。Appendix H 也承认 "a further concern is that PSN-IRT's calibration data may itself contain contaminated models"，但仅将此作为 future concern 提及而未定量评估。建议：至少讨论系统性偏差的可能方向和预期影响量级。

**[REBUT] R1-W6: Cohen's d 将污染模型视为固定点**

部分反驳。R1 的关注在概念上有道理——如果污染条件也有 training randomness 导致的变异性，将其视为固定点会低估不确定性。但从论文的实验设计看：
- §3.3 说 "We train n=10 clean seeds for Qwen and Llama"，clean seeds 用于建立 baseline 分布
- 每个污染水平（15%, 50%）也应该有对应的训练 run，但论文未明确报告污染条件的 seed 数量
- 如果每个污染条件只有 1 个 model（这从 Δl_z^* 的定义看似乎如此——Section 3.2: "the target benchmark's l_z^* is compared against benchmarks presumed clean from the same model"），R1 的关注成立
- 但 Table 1 报告的 Cohen's d 效应量极大（|d|=1.90 到 8.22），即使考虑额外的变异性，定性结论（"显著偏离零"）不太可能改变

建议在 Appendix 中增加对此设计选择的讨论，但这不太可能改变论文的核心结论。

**[AGREE] R1-W7: Local dependence 模拟的代表性**

同意。Appendix E.1 使用 shared LD（clean 和 contaminated 条件共享相同 tetrachoric 结构）和 asymmetric LD（contamination-specific LD）两种模拟条件，但正如 R1 所指，真实 LLM 的 item 依赖结构可能远比这些模拟复杂（例如，LLM 的 attention 机制导致的序列位置效应、topic cluster 内的依赖等）。论文的 Δl_z^* 设计在理论上可以 cancel 掉 shared LD，但 contamination-specific LD（Table 9-10）的模拟是否捕捉了真实结构是一个开放问题。这是一个 inherent limitation，不太可能在当前论文中完全解决，但应在 Limitations 中更明确讨论。

---

### 总体评价

R1 的审稿质量很高，多数 Must-Fix 问题我都同意。特别是 N1（25% 透明性）和 N3（矩阵不完整）是我审稿时未充分强调的重要问题——N1 尤其严重，因为它直接质疑了论文最核心发现的方法论诚实性。

两份审稿的共识问题（按重要性排序）：
1. **Post-RL Finding 4 证据不足**（R1-W4 + R2-N1）
2. **Inverted-U 证据不足**（R1-N2 + R2-W3）
3. **缺乏与 ConStat 等方法的实证对比**（R2-N2）
4. **模型覆盖不足**（R1-N3 矩阵不完整 + R2-N3 规模单一）
5. **"Black-box" framing overclaim**（R1-W2 + R2-W1）
6. **25% 条件透明性**（R1-N1，R2 未独立发现但完全同意）

我维持 **Overall 3.0 (Findings)** 的评分。R1 给出 3.5（Borderline Conference），考虑到两份审稿的共识问题数量，我认为当前版本更适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 469 · 2026-05-22T04:59:00.437580+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 审稿意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 50

## Round 50

10 recorded events


### User

_source line 470 · 2026-05-22T04:59:01.593036+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题回应

**[AGREE] R2-N1: Post-RL (N=1) 作为核心发现缺乏支撑**

同意。我在自己的审稿意见中也将此列为 W4（Should-Fix）。§4.5 明确声明 "No statistical inference is drawn from this observation"（第 181 行），但 Abstract 第 8 行和 Introduction Finding (4) 仍将其与其他三个经 factorial design 验证的发现并列。这种 framing 不匹配确实存在。

不过我认为完全从论文中移除不是最佳选择——post-RL 是一个有价值的探索方向，关键在于调整其呈现位次。建议将 §4.5 内容缩减为 Discussion 中的一段（约 150 词），从 Abstract/Introduction 的 enumerated findings 中移除，改为 Discussion 中 "open question" 的形式呈现。

**[REBUT] R2-N2: 缺乏与 ConStat/PaCoST/CoDeC 的实证对比**

部分不同意此条作为 Must-Fix 的定级。原因如下：

1. **信息访问层级不同，直接对比不公平**。论文 §1（第 7-12 行）和 §2（第 1-12 行）明确构建了按信息访问排序的 detection frontier：ConStat 需要跨多个 benchmark 的性能比较（§2 第 8 行引用 constat2024），PaCoST 需要 in-context learning passes，CoDeC 需要 "multiple test variants or output logits"（§2 第 8 行引用 codec2026）。这些方法在 binary-response-only 约束下无法运行。要求在相同设置下对比，要么需要给 ℓz* 额外的信息（不公平地帮助它），要么需要限制 ConStat 等方法的信息访问（使其无法正常运行）。

2. **论文已自我揭示了 ℓz* 的检测劣势**。Table 3（§4.4）直接展示了 accuracy z-score 的 |d| 比 ℓz* 高一个数量级（Qwen 50%: 68.7 vs. 1.90）。论文的 claim 不是 "ℓz* 是最佳检测器"，而是 "ℓz* 提供检测之外的诊断能力"（seen/unseen decomposition、θ-shift mechanism analysis）。这个自我批评已经回答了 "ℓz* 检测力如何" 的问题。

3. **但我同意论文应更明确地讨论这一对比缺失的原因**。当前 §5 Discussion 提到 ConStat 是 "complementary"（第 20 行），但未系统解释为什么不做直接对比。建议在 §5 或 §2 Related Work 中增加一段讨论，明确说明信息访问层级差异，以及在何种访问层级下各方法适用。

因此建议将此条从 Must-Fix 降级为 Should-Fix。

**[AGREE] R2-N3: 模型规模覆盖不足**

同意这是显著弱点。三个模型均为 7-8B，Finding 2 声称 "baseline model ability modulates detection sensitivity"（§4.3 第 60-77 行），但 baseline ability 的变化（Mistral 52.4% → Llama 59.3% → Qwen 67.8%）与模型架构差异完全混淆。无法区分是 ability-driven（如论文所声称的 θ-shift mechanism）还是 architecture-driven（不同模型家族的响应模式本质不同）。

我在自己的审稿中也指出了类似问题（N3 实验矩阵不完整）。Limitations §1（第 3-4 行）承认 "validation on larger models (13B, 70B)... remains future work"，但这不改变当前 claim 的支撑不足。

不过，我对此条的严重性评估略低于 R2。论文的核心贡献是 "characterization under what conditions IRT person-fit works"，即使只在 7-8B 上建立，boundary conditions 的定性方向（θ-shift absorption、benchmark size effect）仍有指导价值。建议论文在 Finding 2 的表述中加入 "within the 7-8B scale" 的限定，而非要求补充大规模实验（这在审稿周期内可能不现实）。

---

## Should-Fix 问题回应

**[AGREE] R2-W1: Black-box framing overclaim**

完全同意，与我的 W2 一致。PSN-IRT 的 4PL item parameters 是一个非平凡的外部依赖。Appendix H 展示 MML-EM 从 leaderboard 数据重新估计时 discrimination 参数几乎不可恢复（r_a=0.127），说明此依赖不可替代。"Black-box" 标签确实过度简化了实际访问需求。

**[REBUT] R2-W2: 部分发现可由 IRT 理论预测，novelty 有限**

部分不同意。

- **Finding 2（θ-shift dynamics）**：R2 认为高能力模型的 θ 吸收效应可从 IRT 理论直接预测。理论上**方向**是可预测的，但**经验幅度和非平凡的反转**不是。ARC-C 上的 ceiling effect 反转（§4.3 第 70-73 行：Qwen 在 ARC-C 上 baseline accuracy 90%，但 contamination 产生更大而非更小的 |d|）就不是 IRT 理论的直接推论——它依赖于 item count 和 baseline accuracy 的交互作用，需要实证验证。此外，LLM 响应严重违反 IRT 假设（57/60 cells flagged，§3.2 第 24 行），在这种假设违反下理论预测是否仍成立是一个需要实证回答的问题。

- **Finding 3（detection-diagnosis tradeoff）**：ℓz* 的 Snijders correction 会降低检测灵敏度，这在理论上是已知的。但 Table 3 量化了具体幅度（accuracy z: |d|=68.7 vs. ℓz*: |d|=1.90，差距超过一个数量级），且 "57/60 vs. 4/60 flagged cells on real-world data" 的发现（§4.4 第 132-133 行）展示了 ℓz* 对 response-pattern structure 的独特敏感性，这不是理论可以直接预测的经验结果。

因此，这两个 finding 的**定性方向**确实可预测，但**定量结果和边界条件**是新的。论文应更清晰地区分理论预测 vs. 经验验证的部分，但 novelty 评判不应仅基于方向的可预测性。

**[AGREE] R2-W3: Inverted-U 普适性声明过强**

完全同意，与我的 N2 一致。1 个模型 × 3 个点的证据不足以作为 robust finding。

**[AGREE] R2-W4: Benchmark 覆盖面偏窄**

同意。MMLU（14,042 items）和 ARC-C（295 items）确实覆盖了 item count 的两个数量级，但两者都是多选题格式，缺乏 generative benchmark（GSM8K、HumanEval 等）。Appendix B 的 simulation 确实覆盖了 5 个 benchmark（含 GSM8K、HumanEval），但 controlled experiments 仅用了 2 个。值得注意的是 simulation 结果（Table 4）显示小 benchmark 上 4PL power 很低（ARC-C 15%: 0.087, HumanEval 15%: 0.197），暗示 ℓz* 在这些场景下实用性有限，论文应在正文中更明确地讨论这一点。

**[AGREE] R2-W5: 遗漏相关近期工作**

无法直接验证 Han et al. (EACL 2026 Findings) 和 RADAR (Zawalski et al., 2025) 的内容，但如果它们确实处于 psychometrics × contamination 的交叉点，应当引用并对比。Related Work §2 的 IRT for LLM evaluation 段落（第 15-22 行）和 person-fit 段落（第 24-30 行）目前未提及任何将 IRT/psychometrics 用于污染检测的工作——如果 Han et al. 做了类似尝试，不引用是一个明显遗漏。建议作者核实并补充。

---

## 对 R2 总体评估的看法

R2 给出 3.0 (Findings) 的评分，核心依据是 contribution density 不足。我认为这一评估总体合理但略偏严格：

- 同意 Finding 4 (post-RL) 应降级，Finding 1 (inverted-U) 证据不充分
- 但 R2 的 N2（缺乏与 ConStat 等对比）作为 Must-Fix 不够成立——信息访问层级不同使直接对比困难
- Finding 2/3 虽部分可预测，但经验验证在 IRT 假设严重违反的 LLM 场景下仍有价值
- DiD 设计本身的方法论贡献被 R2 低估

综合考虑，我维持 3.5 (Borderline Conference) 的评分。如果 inverted-U 和 post-RL 的 claim 调整到位，且实验矩阵中 ARC-C 的 Llama/Mistral 数据能补充，论文可达 Conference 水平。当前状态下 Findings 也是合理的接收决定。


---

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心结论：R1 的 4 个 Must-Fix 中我全部 AGREE，7 个 Should-Fix 中 5 个 AGREE、2 个 partial REBUT（W3 bootstrap 样本空间计算有误但关注点成立、W6 Cohen's d 效应量足够大不影响定性结论）。两份审稿的最大共识是 Finding 4 证据不足和 inverted-U 证据薄弱。我维持 Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 471 · 2026-05-22T04:59:32.630450+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 472 · 2026-05-22T04:59:32.781558+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T04:47:36.935487+00:00\", \"completed_at\": \"2026-05-22T04:50:51.775135+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item（纯 Abstract + Introduction 文本）。Figure 1 出现在 page 2 左栏顶部，仍在前 3 页范围内，审稿人能快速看到视觉锚点。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（IRT 概率曲线 clean vs contaminated）直接传达核心概念（Δζ' 信号），caption 自包含，Title-Abstract-首图叙事一致。锚定效应正面。\"}, {\"severity\": \"info\", \"dimension\": \"pages 3-4\", \"message\": \"连续两页以文本为主（Related Work → Method）。Page 3 底部有 Eq.(1)（4PL 模型），page 4 有 Δζ' 定义公式，数学内容提供了一定视觉节奏，但整体文本密度较高。鉴于是 IRT 形式化推导部分，可接受但偏密。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1（Cohen's d with 95% CI）位于顶部，booktabs 风格，格式规范。CI 精度一致（小数两位）。表格宽度适配单栏。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2（全宽 heatmap）+ Table 2 共存，display item 密度良好。Heatmap 使用蓝色单色调 sequential 色板——色盲安全、灰度可辨。Grey cells 标注缺失条件，caption 说明充分。\"}, {\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"Figure 2 heatmap 单元格内的数值标注（|d| 及 CI）字号偏小。在标准打印尺寸下可能需要放大才能舒适阅读。建议适当增大 cell 内字号或在 caption/正文中复述关键数值。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3（散点图）+ Table 3（detection-diagnosis tradeoff）+ Figure 4 开始出现——节奏紧凑，display item 密度高。Figure 3 使用不同 marker shape（三角/圆形）区分条件，即使灰度打印也可辨别。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 3 使用 booktabs 风格，数值精度统一。表头清晰。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 4（Post-RL trajectory，4 子图）位于顶部，Discussion + Conclusion 填充下方。主正文恰好 8 页，符合 EMNLP 2026 页数限制。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 4 的 4 个子图排列紧凑，axis label 和 legend 字号偏小（估计接近正文字号 60-65%），建议增大至 ≥70% 正文字号以提升可读性。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落简洁（约 1 段覆盖 3-4 个限制点），符合 EMNLP 2
…[truncated 1180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 473 · 2026-05-22T04:59:32.781995+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 474 · 2026-05-22T04:59:32.883497+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 475 · 2026-05-22T05:02:57.517855+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_personfit_contam",
  "issues_yaml": "## Review Issue Tracker — Round 4 (fresh review, 2026-05-22)\n## Reviewer 1 (方法严谨性, 3.5 Borderline Conference) + Reviewer 2 (新颖性/完整性, 3.0 Findings)\n\n# ===== CRITICAL ISSUES =====\n\n- id: \"R4-N1\"\n  summary: \"25% 污染条件未在 §3.3 实验设置中描述——inverted-U 核心证据来源不透明\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-N1 提出，R2 交叉 AGREE。§3.3 写 three conditions (clean, 15%, 50%)，但 Table 1 含 Qwen 25% 数据 (d=-8.22)。25% 是先验还是 post-hoc？若 post-hoc 则构成 researcher degrees of freedom。Finding 1 (inverted-U) 完全依赖此数据点。\"\n  action_items:\n    - round: 4\n      action: \"§3.3 补充所有实验条件描述（含 25%），说明运行动机和时间顺序，post-hoc 则标注\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N2\"\n  summary: \"Inverted-U 证据不足——仅 1 个模型 3 个数据点，2/3 模型为单调 dose-response\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-N2 提出，R2 交叉 AGREE (升级自 R2-W3)。Qwen 3 点 (15%/25%/50%)，CI 极宽 (d(25%) CI: [-18.9, -5.7])。Llama/Mistral 单调且未测 25%。3 点非单调性可由噪声产生。Abstract/Intro 将其列为首要发现，claim 强度与证据不匹配。\"\n  action_items:\n    - round: 4\n      action: \"补充 Llama/Mistral 25% 验证模型特异性；或降级为 preliminary observation 并调整 Abstract/Intro 位次\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N3\"\n  summary: \"实验设计矩阵不完整——18 条件仅完成约 8 条件\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-N3 提出，R2 交叉 AGREE。ARC-C 仅 Qwen，25% 仅 Qwen，Mistral n=6。Figure 2 灰色格子直观暴露。Abstract 'across three model families' 暗示完整覆盖。R2 补充：模型全部 7-8B，规模覆盖也不足 (R2-N3)。\"\n  action_items:\n    - round: 4\n      action: \"至少补 Llama/Mistral 在 ARC-C 上的实验；或明确限定 Abstract/claims 覆盖范围；Limitations 加 scale caveat\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N4\"\n  summary: \"Abstract 事实错误：'n=10 seeds each' 但 Mistral 实际 n=6\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-N4 提出，R2 交叉 AGREE。§3.3 明确写 Mistral n=6 (four checkpoints lost)，Abstract 'n=10 seeds each' 是事实性错误。\"\n  action_items:\n    - round: 4\n      action: \"Abstract 改为 'n=10 seeds for Qwen and Llama, n=6 for Mistral' 或 'n≥6 seeds each'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N5\"\n  summary: \"Post-RL Finding 4 (N=1) 不应列为核心贡献\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-N1 提出 (Must-Fix)，R1 AGREE (自身列为 W4)。N=1 (Qwen+GRPO, 15%)，§4.5 'no statistical inference is drawn'，但 Abstract/Intro 将其与 factorial-design 发现并列。Contribution scope 膨胀。两人同意降级为 Discussion 中 preliminary observation，从 Abstract enumerated findings 移除。\"\n  action_items:\n    - round: 4\n      action: \"§4.5 缩减为 Discussion 一段 (~150 词)；从 Abstract/Intro 核心发现列表移除；改为 'open question' 形式\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== SHOULD-FIX ISSUES =====\n\n- id: \"R4-W1\"\n  summary: \"'Black-box access' framing overclaim——框架依赖 PSN-IRT 外部 item bank\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W2 和 R2-W1 独立提出，交叉完全一致。Abstract 说 'only binary response patterns' 但依赖 PSN-IRT 预校准 4PL 参数（13,000+ 模型）。Appendix H r_a=0.127 证实依赖不可替代。'black-box' 在论文中使用至少 5 次，给读者错误印象。应区分 target model access (binary only) 和 external item bank (substantial)。\"\n  action_items:\n    - round: 4\n      action: \"Abstract 突出 PSN-IRT 依赖；首次使用 'black-box' 时明确定义语境；考虑用 'binary-response + external item bank' 替代\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"QLoRA SFT 生态效度有限——title/abstract 范围超出 SFT-only 实验\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 AGREE。标题 'Benchmark Contamination' 暗示广泛适用，但实验仅 QLoRA SFT。Limitations 承认 scope 但 title/abstract 未限定。Introduction 有 'we focus on SFT-stage contamination' 但不够突出。\"\n  action_items:\n    - round: 4\n      action: \"title 或 abstract 加 'SFT-stage' 限定；或 introduction 更显著讨论范围限制\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"缺乏与 ConStat 等方法的实证对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-N2 列为 Must-Fix，R1 交叉 REBUT 降级为 Should-Fix——信息访问层级不同使直接对比不公平（ConStat 需跨 benchmark 分数，ℓz* 仅需 binary responses）。论文已自我揭示 ℓz* 检测劣势 (Table 3)。两人达成部分共识：至少在 Discussion/Related Work 中系统解释为何不做直接对比。\"\n  action_items:\n    - round: 4\n      action: \"§5 或 §2 增加一段讨论信息访问层级差异和各方法适用场景；如可行补 ConStat 实证对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W4\"\n  summary: \"PSN-IRT 校准循环性——随机扰动分析未覆盖系统性偏差\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 交叉 AGREE。Appendix F.2 ±10% 随机噪声不能模拟被污染模型引入的系统性偏差（高估 θ → 偏移 difficulty）。Discussion 提及 concern 但未定量评估。\"\n  action_items:\n    - round: 4\n      action: \"讨论系统性偏差 vs 随机噪声区别；或设计模拟实验注入不同比例污染模型到校准样本\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"Bootstrap CI 在小样本下的可靠性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W3 提出，R2 partial REBUT（纠正 bootstrap 样本空间计算：6^6=46,656 非 462，但同意 coverage 较差）。BCa 已在 Appendix G 作为 sensitivity check。定性结论不太可能被翻转。建议主文报告 BCa CI 或加注 caveat。\"\n  action_items:\n    - round: 4\n      action: \"主文改用 BCa CI 或对 Mistral n=6 加注小样本 caveat\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W6\"\n  summary: \"遗漏直接相关近期工作\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 交叉 AGREE。Han et al. (EACL 2026 Findings, arXiv 2510.07175) psychometrics×contamination 交叉点未引用；RADAR (Zawalski et al., 2025, arXiv 2510.08931) mechanistic contamination detection 也值得对比。\"\n  action_items:\n    - round: 4\n      action: \"Related Work 补充 Han et al. 和 RADAR 的讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W7\"\n  summary: \"Cohen's d 将被污染模型视为固定点——低估真实不确定性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W6 提出，R2 partial REBUT——概念上有道理但效应量极大 (|d|=1.90-8.22) 不太可能被翻转。未明确报告每个污染条件的 seed 数量。\"\n  action_items:\n    - round: 4\n      action: \"明确报告每个污染条件的运行次数；Appendix 讨论设计选择\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W8\"\n  summary: \"LD 模拟可能未捕捉真实 LLM 依赖结构\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W7 提出，R2 交叉 AGREE。Appendix F.1 testlet+Gaussian 模拟不一定代表 LLM 的 attention/sequence/topic 依赖结构。Inherent limitation，应在 Limitations 讨论。\"\n  action_items:\n    - round: 4\n      action: \"Limitations 或 Appendix F.1 讨论模拟假设局限性和 Δlz* 可能失效的依赖结构\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== DIVERGENCE =====\n\n- id: \"R4-D1\"\n  summary: \"ConStat 对比——Must-Fix vs Should-Fix 分歧\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2 列为 Must-Fix (N2)：论文定位在 contamination detection 领域却不与主要方法对比。R1 REBUT 降级为 Should-Fix：信息访问层级不同使直接对比不公平，论文已自我揭示 ℓz* 检测劣势 (Table 3)。达成部分共识：至少应系统解释为何不做直接对比。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-D2\"\n  summary: \"Finding 2/3 的 novelty——IRT 理论可预测 vs empirical quantification 有独立价值\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W2 认为 θ-shift dynamics (Finding 2) 和 detection-diagnosis tradeoff (Finding 3) 部分可由 IRT 理论预测，novelty 有限。R1 REBUT：定性方向可预测但定量结果和边界条件是新的——ARC-C ceiling effect 反转非教科书推论，57/60 vs 4/60 flagged cells 是新经验发现，LLM 严重违反 IRT 假设下理论预测是否成立需实证回答。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ===== MINOR ISSUES =====\n\n- id: \"R4-M1\"\n  summary: \"Benchmark 覆盖面偏窄——仅 MMLU + ARC-C 两个多选题格式\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W4 提出，R1 交叉 AGREE。缺 generative benchmark (GSM8K/HumanEval)。Appendix B simulation 覆盖 5 个 benchmark 但 controlled experiments 仅 2 个。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M2\"\n  summary: \"Figure 2 heatmap 单元格数值字号偏小\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [visual_check]\n      note: \"视觉审查发现，标准打印尺寸下可能需要放大阅读\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M3\"\n  summary: \"Figure 4 子图 axis label 和 legend 字号偏小\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [visual_check]\n      note: \"视觉审查发现，估计接近正文字号 60-65%，建议 ≥70%\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ===== PRIOR ROUND ISSUES (STATUS UPDATE) =====\n\n- id: \"R3-N1\"\n  summary: \"仅两个污染水平不足以支撑 non-monotonic dose-response 核心 claim\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W2: 三个数据点无法区分 inverted-U 和 monotonic decrease\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Qwen 15% CI=[-15.2,-4.5] 和 50% CI=[-5.0,-1.0] 存在重叠\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"25% 实验已补充 (d=-8.22)，三点曲线可见。但新问题：25% 未在 §3.3 描述 (R4-N1)；仅 Qwen 展示 inverted-U，Llama/Mistral 单调 (R4-N2)。部分改善但新透明性问题出现。\"\n  resolution: \"Partially addressed — 25% data added but transparency issue (R4-N1) and model-specificity (R4-N2) remain\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"Minimal-information point framing overclaim——实际强依赖外部 4PL item bank\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Abstract/Intro 反复说 binary responses only，但依赖 PSN-IRT 4PL 参数\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Abstract 现包含 'externally calibrated 4PL item parameters' 但嵌在长句中不够突出。'black-box' 仍使用至少 5 次。问题持续存在，独立追踪为 R4-W1。\"\n  resolution: \"Partially improved — qualifier added to Abstract but black-box label still overused\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"QLoRA SFT 生态效度与 Introduction pretraining contamination 动机脱节\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Introduction 以 pretraining contamination 为动机但实验用 QLoRA SFT\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Introduction 现包含 'we focus on SFT-stage contamination' scope 限定，改善明显。但 title 和 abstract 范围仍宽。独立追踪为 R4-W2。\"\n  resolution: \"Partially improved — SFT scope added to Introduction but title/abstract still broad\"\n  resolution_round: null\n\n- id: \"R3-N4\"\n  summary: \"实验规模偏窄——3 个 7-8B 模型、2 个 benchmark、仅 SFT 污染\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"ARC-C 仅 Qwen。标题/abstract 泛化性措辞超出 scope。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"问题持续。R1 指出完整 3×2×3 矩阵仅完成约 8/18 (R4-N3)。R2 指出全部 7-8B 无法区分 ability-driven vs scale-driven (R4-N3)。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1\"\n  summary: \"Post-RL finding (N=1) 不应列为核心 contribution\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"N=1 无统计推断，Abstract/Intro 将其与 n=10 实验并列\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"问题持续，本轮两位 Reviewer 均同意这是关键问题。Abstract 仍列为第四个 enumerated finding (with N=1 tag)。独立追踪为 R4-N5。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W5\"\n  summary: \"缺少与 ConStat 的实证对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两人达成部分共识：至少补 ConStat 实证对比\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"仍无实证对比。R2 维持 Must-Fix，R1 REBUT 降为 Should-Fix (信息访问层级不同)。Discussion 仍仅一句 'complementary'。独立追踪为 R4-W3/R4-D1。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"PSN-IRT 循环依赖——leaderboard 校准数据本身可能被污染\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Appendix F 高斯扰动不能模拟结构性偏差\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"问题持续。独立追踪为 R4-W4。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W6\"\n  summary: \"Bootstrap CI 方法和小样本可靠性问题\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"n=3/6 下 percentile bootstrap 可能过于乐观。应补 BCa。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"BCa 已补充 (Appendix G)。但主文仍用 percentile CI。R2 纠正 R1 的样本空间计算 (6^6=46,656 非 462)。独立追踪为 R4-W5。\"\n  resolution: \"BCa added as sensitivity check in Appendix G; main text still uses percentile CI\"\n  resolution_round: null\n\n- id: \"R3-D1\"\n  summary: \"Findings 新颖性——IRT 理论可预测 vs empirical quantification 有独立价值\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"同分歧\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"分歧持续。R2 认为 Finding 2/3 可 IRT 预测。R1 REBUT：定量结果和边界条件（ARC-C 反转、57/60 vs 4/60）是新的。独立追踪为 R4-D2。\"\n  resolution: \"\"\n  resolution_round: null\n\n# ===== PRIOR ROUND RESOLVED ISSUES (unchanged) =====\n\n- id: \"BEST-W1\"\n  summary: \"0 figures, presentation unacceptable\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"本轮确认已解决。4 figures + 3 tables，视觉审查通过。\"\n  resolution: \"Resolved\"\n  resolution_round: 2\n\n- id: \"ACTUAL-B-W1\"\n  summary: \"n=3 seeds statistically insufficient\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Qwen/Llama n=10 确认。Mistral n=6 残留问题追踪为 R4-N4 (Abstract 事实错误)。\"\n  resolution: \"Resolved\"\n  resolution_round: 3\n\n- id: \"R2-W7\"\n  summary: \"缺少 reproducibility statement\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"确认已解决。Reproducibility Statement 存在，格式正确。\"\n  resolution: \"Resolved\"\n  resolution_round: 3\n\n- id: \"R3-W2\"\n  summary: \"Mistral n=6 seeds 统计效力不足\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"状态不变。Checkpoints 丢失无法补跑。CI 排除零，结论仍成立。\"\n  resolution: \"Checkpoints lost; CI excludes zero; noted as limitation\"\n  resolution_round: 3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_personfit_contam",
    "issues_yaml": "## Review Issue Tracker — Round 4 (fresh review, 2026-05-22)\n## Reviewer 1 (方法严谨性, 3.5 Borderline Conference) + Reviewer 2 (新颖性/完整性, 3.0 Findings)\n\n# ===== CRITICAL ISSUES =====\n\n- id: \"R4-N1\"\n  summary: \"25% 污染条件未在 §3.3 实验设置中描述——inverted-U 核心证据来源不透明\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-N1 提出，R2 交叉 AGREE。§3.3 写 three conditions (clean, 15%, 50%)，但 Table 1 含 Qwen 25% 数据 (d=-8.22)。25% 是先验还是 post-hoc？若 post-hoc 则构成 researcher degrees of freedom。Finding 1 (inverted-U) 完全依赖此数据点。\"\n  action_items:\n    - round: 4\n      action: \"§3.3 补充所有实验条件描述（含 25%），说明运行动机和时间顺序，post-hoc 则标注\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N2\"\n  summary: \"Inverted-U 证据不足——仅 1 个模型 3 个数据点，2/3 模型为单调 dose-response\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-N2 提出，R2 交叉 AGREE (升级自 R2-W3)。Qwen 3 点 (15%/25%/50%)，CI 极宽 (d(25%) CI: [-18.9, -5.7])。Llama/Mistral 单调且未测 25%。3 点非单调性可由噪声产生。Abstract/Intro 将其列为首要发现，claim 强度与证据不匹配。\"\n  action_items:\n    - round: 4\n      action: \"补充 Llama/Mistral 25% 验证模型特异性；或降级为 preliminary observation 并调整 Abstract/Intro 位次\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N3\"\n  summary: \"实验设计矩阵不完整——18 条件仅完成约 8 条件\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-N3 提出，R2 交叉 AGREE。ARC-C 仅 Qwen，25% 仅 Qwen，Mistral n=6。Figure 2 灰色格子直观暴露。Abstract 'across three model families' 暗示完整覆盖。R2 补充：模型全部 7-8B，规模覆盖也不足 (R2-N3)。\"\n  action_items:\n    - round: 4\n      action: \"至少补 Llama/Mistral 在 ARC-C 上的实验；或明确限定 Abstract/claims 覆盖范围；Limitations 加 scale caveat\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N4\"\n  summary: \"Abstract 事实错误：'n=10 seeds each' 但 Mistral 实际 n=6\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-N4 提出，R2 交叉 AGREE。§3.3 明确写 Mistral n=6 (four checkpoints lost)，Abstract 'n=10 seeds each' 是事实性错误。\"\n  action_items:\n    - round: 4\n      action: \"Abstract 改为 'n=10 seeds for Qwen and Llama, n=6 for Mistral' 或 'n≥6 seeds each'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N5\"\n  summary: \"Post-RL Finding 4 (N=1) 不应列为核心贡献\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-N1 提出 (Must-Fix)，R1 AGREE (自身列为 W4)。N=1 (Qwen+GRPO, 15%)，§4.5 'no statistical inference is drawn'，但 Abstract/Intro 将其与 factorial-design 发现并列。Contribution scope 膨胀。两人同意降级为 Discussion 中 preliminary observation，从 Abstract enumerated findings 移除。\"\n  action_items:\n    - round: 4\n      action: \"§4.5 缩减为 Discussion 一段 (~150 词)；从 Abstract/Intro 核心发现列表移除；改为 'open question' 形式\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== SHOULD-FIX ISSUES =====\n\n- id: \"R4-W1\"\n  summary: \"'Black-box access' framing overclaim——框架依赖 PSN-IRT 外部 item bank\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W2 和 R2-W1 独立提出，交叉完全一致。Abstract 说 'only binary response patterns' 但依赖 PSN-IRT 预校准 4PL 参数（13,000+ 模型）。Appendix H r_a=0.127 证实依赖不可替代。'black-box' 在论文中使用至少 5 次，给读者错误印象。应区分 target model access (binary only) 和 external item bank (substantial)。\"\n  action_items:\n    - round: 4\n      action: \"Abstract 突出 PSN-IRT 依赖；首次使用 'black-box' 时明确定义语境；考虑用 'binary-response + external item bank' 替代\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"QLoRA SFT 生态效度有限——title/abstract 范围超出 SFT-only 实验\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 AGREE。标题 'Benchmark Contamination' 暗示广泛适用，但实验仅 QLoRA SFT。Limitations 承认 scope 但 title/abstract 未限定。Introduction 有 'we focus on SFT-stage contamination' 但不够突出。\"\n  action_items:\n    - round: 4\n      action: \"title 或 abstract 加 'SFT-stage' 限定；或 introduction 更显著讨论范围限制\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"缺乏与 ConStat 等方法的实证对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-N2 列为 Must-Fix，R1 交叉 REBUT 降级为 Should-Fix——信息访问层级不同使直接对比不公平（ConStat 需跨 benchmark 分数，ℓz* 仅需 binary responses）。论文已自我揭示 ℓz* 检测劣势 (Table 3)。两人达成部分共识：至少在 Discussion/Related Work 中系统解释为何不做直接对比。\"\n  action_items:\n    - round: 4\n      action: \"§5 或 §2 增加一段讨论信息访问层级差异和各方法适用场景；如可行补 ConStat 实证对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W4\"\n  summary: \"PSN-IRT 校准循环性——随机扰动分析未覆盖系统性偏差\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 交叉 AGREE。Appendix F.2 ±10% 随机噪声不能模拟被污染模型引入的系统性偏差（高估 θ → 偏移 difficulty）。Discussion 提及 concern 但未定量评估。\"\n  action_items:\n    - round: 4\n      action: \"讨论系统性偏差 vs 随机噪声区别；或设计模拟实验注入不同比例污染模型到校准样本\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"Bootstrap CI 在小样本下的可靠性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W3 提出，R2 partial REBUT（纠正 bootstrap 样本空间计算：6^6=46,656 非 462，但同意 coverage 较差）。BCa 已在 Appendix G 作为 sensitivity check。定性结论不太可能被翻转。建议主文报告 BCa CI 或加注 caveat。\"\n  action_items:\n    - round: 4\n      action: \"主文改用 BCa CI 或对 Mistral n=6 加注小样本 caveat\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W6\"\n  summary: \"遗漏直接相关近期工作\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 交叉 AGREE。Han et al. (EACL 2026 Findings, arXiv 2510.07175) psychometrics×contamination 交叉点未引用；RADAR (Zawalski et al., 2025, arXiv 2510.08931) mechanistic contamination detection 也值得对比。\"\n  action_items:\n    - round: 4\n      action: \"Related Work 补充 Han et al. 和 RADAR 的讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W7\"\n  summary: \"Cohen's d 将被污染模型视为固定点——低估真实不确定性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W6 提出，R2 partial REBUT——概念上有道理但效应量极大 (|d|=1.90-8.22) 不太可能被翻转。未明确报告每个污染条件的 seed 数量。\"\n  action_items:\n    - round: 4\n      action: \"明确报告每个污染条件的运行次数；Appendix 讨论设计选择\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W8\"\n  summary: \"LD 模拟可能未捕捉真实 LLM 依赖结构\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W7 提出，R2 交叉 AGREE。Appendix F.1 testlet+Gaussian 模拟不一定代表 LLM 的 attention/sequence/topic 依赖结构。Inherent limitation，应在 Limitations 讨论。\"\n  action_items:\n    - round: 4\n      action: \"Limitations 或 Appendix F.1 讨论模拟假设局限性和 Δlz* 可能失效的依赖结构\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== DIVERGENCE =====\n\n- id: \"R4-D1\"\n  summary: \"ConStat 对比——Must-Fix vs Should-Fix 分歧\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2 列为 Must-Fix (N2)：论文定位在 contamination detection 领域却不与主要方法对比。R1 REBUT 降级为 Should-Fix：信息访问层级不同使直接对比不公平，论文已自我揭示 ℓz* 检测劣势 (Table 3)。达成部分共识：至少应系统解释为何不做直接对比。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-D2\"\n  summary: \"Finding 2/3 的 novelty——IRT 理论可预测 vs empirical quantification 有独立价值\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W2 认为 θ-shift dynamics (Finding 2) 和 detection-diagnosis tradeoff (Finding 3) 部分可由 IRT 理论预测，novelty 有限。R1 REBUT：定性方向可预测但定量结果和边界条件是新的——ARC-C ceiling effect 反转非教科书推论，57/60 vs 4/60 flagged cells 是新经验发现，LLM 严重违反 IRT 假设下理论预测是否成立需实证回答。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ===== MINOR ISSUES =====\n\n- id: \"R4-M1\"\n  summary: \"Benchmark 覆盖面偏窄——仅 MMLU + ARC-C 两个多选题格式\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W4 提出，R1 交叉 AGREE。缺 generative benchmark (GSM8K/HumanEval)。Appendix B simulation 覆盖 5 个 benchmark 但 controlled experiments 仅 2 个。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M2\"\n  summary: \"Figure 2 heatmap 单元格数值字号偏小\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [visual_check]\n      note: \"视觉审查发现，标准打印尺寸下可能需要放大阅读\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M3\"\n  summary: \"Figure 4 子图 axis label 和 legend 字号偏小\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [visual_check]\n      note: \"视觉审查发现，估计接近正文字号 60-65%，建议 ≥70%\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ===== PRIOR ROUND ISSUES (STATUS UPDATE) =====\n\n- id: \"R3-N1\"\n  summary: \"仅两个污染水平不足以支撑 non-monotonic dose-response 核心 claim\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W2: 三个数据点无法区分 inverted-U 和 monotonic decrease\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Qwen 15% CI=[-15.2,-4.5] 和 50% CI=[-5.0,-1.0] 存在重叠\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"25% 实验已补充 (d=-8.22)，三点曲线可见。但新问题：25% 未在 §3.3 描述 (R4-N1)；仅 Qwen 展示 inverted-U，Llama/Mistral 单调 (R4-N2)。部分改善但新透明性问题出现。\"\n  resolution: \"Partially addressed — 25% data added but transparency issue (R4-N1) and model-specificity (R4-N2) remain\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"Minimal-information point framing overclaim——实际强依赖外部 4PL item bank\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Abstract/Intro 反复说 binary responses only，但依赖 PSN-IRT 4PL 参数\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Abstract 现包含 'externally calibrated 4PL item parameters' 但嵌在长句中不够突出。'black-box' 仍使用至少 5 次。问题持续存在，独立追踪为 R4-W1。\"\n  resolution: \"Partially improved — qualifier added to Abstract but black-box label still overused\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"QLoRA SFT 生态效度与 Introduction pretraining contamination 动机脱节\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Introduction 以 pretraining contamination 为动机但实验用 QLoRA SFT\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Introduction 现包含 'we focus on SFT-stage contamination' scope 限定，改善明显。但 title 和 abstract 范围仍宽。独立追踪为 R4-W2。\"\n  resolution: \"Partially improved — SFT scope added to Introduction but title/abstract still broad\"\n  resolution_round: null\n\n- id: \"R3-N4\"\n  summary: \"实验规模偏窄——3 个 7-8B 模型、2 个 benchmark、仅 SFT 污染\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"ARC-C 仅 Qwen。标题/abstract 泛化性措辞超出 scope。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"问题持续。R1 指出完整 3×2×3 矩阵仅完成约 8/18 (R4-N3)。R2 指出全部 7-8B 无法区分 ability-driven vs scale-driven (R4-N3)。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1\"\n  summary: \"Post-RL finding (N=1) 不应列为核心 contribution\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"N=1 无统计推断，Abstract/Intro 将其与 n=10 实验并列\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"问题持续，本轮两位 Reviewer 均同意这是关键问题。Abstract 仍列为第四个 enumerated finding (with N=1 tag)。独立追踪为 R4-N5。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W5\"\n  summary: \"缺少与 ConStat 的实证对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两人达成部分共识：至少补 ConStat 实证对比\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"仍无实证对比。R2 维持 Must-Fix，R1 REBUT 降为 Should-Fix (信息访问层级不同)。Discussion 仍仅一句 'complementary'。独立追踪为 R4-W3/R4-D1。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"PSN-IRT 循环依赖——leaderboard 校准数据本身可能被污染\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Appendix F 高斯扰动不能模拟结构性偏差\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"问题持续。独立追踪为 R4-W4。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W6\"\n  summary: \"Bootstrap CI 方法和小样本可靠性问题\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"n=3/6 下 percentile bootstrap 可能过于乐观。应补 BCa。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"BCa 已补充 (Appendix G)。但主文仍用 percentile CI。R2 纠正 R1 的样本空间计算 (6^6=46,656 非 462)。独立追踪为 R4-W5。\"\n  resolution: \"BCa added as sensitivity check in Appendix G; main text still uses percentile CI\"\n  resolution_round: null\n\n- id: \"R3-D1\"\n  summary: \"Findings 新颖性——IRT 理论可预测 vs empirical quantification 有独立价值\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"同分歧\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"分歧持续。R2 认为 Finding 2/3 可 IRT 预测。R1 REBUT：定量结果和边界条件（ARC-C 反转、57/60 vs 4/60）是新的。独立追踪为 R4-D2。\"\n  resolution: \"\"\n  resolution_round: null\n\n# ===== PRIOR ROUND RESOLVED ISSUES (unchanged) =====\n\n- id: \"BEST-W1\"\n  summary: \"0 figures, presentation unacceptable\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"本轮确认已解决。4 figures + 3 tables，视觉审查通过。\"\n  resolution: \"Resolved\"\n  resolution_round: 2\n\n- id: \"ACTUAL-B-W1\"\n  summary: \"n=3 seeds statistically insufficient\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Qwen/Llama n=10 确认。Mistral n=6 残留问题追踪为 R4-N4 (Abstract 事实错误)。\"\n  resolution: \"Resolved\"\n  resolution_round: 3\n\n- id: \"R2-W7\"\n  summary: \"缺少 reproducibility statement\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"确认已解决。Reproducibility Statement 存在，格式正确。\"\n  resolution: \"Resolved\"\n  resolution_round: 3\n\n- id: \"R3-W2\"\n  summary: \"Mistral n=6 seeds 统计效力不足\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"状态不变。Checkpoints 丢失无法补跑。CI 排除零，结论仍成立。\"\n  resolution: \"Checkpoints lost; CI excludes zero; noted as limitation\"\n  resolution_round: 3"
  }
}
```

</details>

---


### Tool result

_source line 476 · 2026-05-22T05:02:57.619018+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml\", \"bytes\": 16176}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 477 · 2026-05-22T05:05:32.230884+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "irt_personfit_contam",
  "report": "# 审稿报告 — Round 4 (Fresh Review)\n\n**论文**: What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n**Venue**: EMNLP 2026 (via ACL Rolling Review, Long Paper)\n**审稿日期**: 2026-05-22\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）\n**交叉轮数**: 1 轮（关键问题达成共识，无需第二轮）\n\n---\n\n## Summary\n\n本文首次将心理测量学中的 IRT person-fit 统计量（ℓz*）系统性地迁移到 LLM benchmark 污染检测领域，提出 Δℓz* difference-in-differences 设计以应对 LLM 对 IRT 假设的系统性违反。在三个 7-8B 模型家族（Qwen2.5-7B、Llama-3.1-8B、Mistral-7B）和两个 benchmark（MMLU、ARC-Challenge）上，通过 QLoRA SFT 控制实验验证了四个行为边界：inverted-U dose-response、模型特异性 θ-shift dynamics、detection-diagnosis tradeoff、以及初步的 post-RL 残留模式。论文定位为 characterization study 而非 detection tool。\n\n---\n\n## Strengths\n\n**S1.** **跨学科桥梁构建得当**（R1/R2 共识）。将教育测量中成熟的 person-fit 统计量（Snijders 2001, Karabatsos 2003）迁移到 LLM 污染检测，\"被污染 LLM ≈ 作弊考生\" 的类比自然且有说服力。两个此前独立的研究领域被有效连接。\n\n**S2.** **Δℓz* DiD 设计巧妙**（R1/R2 共识）。57/60 model-benchmark cells 在无污染下即产生 |ℓz*| > 1.96，说明绝对阈值不可用。差分设计将系统性 IRT 违反转化为可控特征，模拟验证支持其在 shared LD 下的鲁棒性（d_ratio ≥ 0.93 for σ_τ ≤ 0.5）。\n\n**S3.** **Detection-diagnosis tradeoff 有实际价值**（R1/R2 共识）。Table 3 系统对比了 ℓz*、HT、accuracy z-score 的检测力和诊断力，two-stage workflow 建议（先 z-score 筛查，再 ℓz* 诊断）具有实际指导意义。论文主动揭示 ℓz* 检测力劣于简单统计量，学术诚实。\n\n**S4.** **诚实的 framing 和自我审视**（R1/R2 共识）。论文将自身定位为 \"characterization\" 而非 \"detection tool\"；Appendix H 主动验证 PSN-IRT 依赖的必要性（MML-EM 失败，r_a=0.127）；Limitations 覆盖了主要范围限制。\n\n**S5.** **附录鲁棒性分析全面**（R1/R2 共识）。4PL vs. 3PL ablation、LD 模拟（shared + asymmetric）、参数扰动、BCa 校正、MML-EM refit 等覆盖了多个潜在质疑方向。\n\n**S6.** **θ-shift absorption 机制有理论深度**（R1 特别肯定）。高能力模型在高污染下检测信号反而减弱不是显而易见的，论文从 IRT 理论给出了清晰因果解释，并通过 fixed-θ vs. free-θ 对比验证了机制。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1.** **25% 污染条件未在 §3.3 描述——核心证据来源不透明**（R1-N1, R2 AGREE）\n§3.3 明确写 \"three conditions: clean, 15% contamination, and 50% contamination\"，但 Table 1 包含 Qwen 25% 数据（d=−8.22），inverted-U（Finding 1，论文首要贡献）完全依赖此数据点。25% 是先验计划还是看到非单调趋势后追加的 post-hoc 条件未说明。如果是 post-hoc，构成 researcher degrees of freedom。这是方法论透明性的核心缺陷。\n\n**C2.** **Inverted-U 证据不足以支撑首要发现地位**（R1-N2, R2 AGREE）\n仅基于 1 个模型家族（Qwen）的 3 个数据点（15%, 25%, 50%）。Llama 和 Mistral 均显示单调 dose-response（2/3 模型不支持 inverted-U）。CI 极宽（d(25%) CI: [−18.9, −5.7]）。3 点非单调性可由噪声产生。论文虽限定为 \"specific to Qwen\"，但 Abstract/Introduction 将其列为首要发现，claim 强度与证据不匹配。\n\n**C3.** **实验设计矩阵不完整**（R1-N3, R2 AGREE）\n完整 3 模型 × 2 benchmark × 3 污染水平 = 18 条件，实际仅完成约 8 条。ARC-C 仅 Qwen，25% 仅 Qwen，Mistral n=6。Figure 2 灰色格子直观暴露。此外全部模型为 7-8B（R2-N3），无法区分 Finding 2 的 ability-driven vs. scale-driven 效应。Abstract \"across three 7–8B model families (n=10 seeds each)\" 暗示完整覆盖。\n\n**C4.** **Abstract 事实错误**（R1-N4, R2 AGREE）\nAbstract 写 \"n=10 seeds each\"，但 §3.3 明确写 Mistral 仅 n=6。必须修正。\n\n**C5.** **Post-RL Finding 4 (N=1) 不应列为核心贡献**（R2-N1, R1 AGREE）\nN=1（Qwen+GRPO, 15%），§4.5 自己声明 \"no statistical inference is drawn\"，但 Abstract/Introduction 将其与其他三个经 factorial design 验证的发现并列。应降级为 Discussion 中的 preliminary observation。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1.** **\"Black-box access\" framing overclaim**（R1-W2, R2-W1, 交叉完全一致）\n方法依赖 PSN-IRT 外部 4PL item parameters（13,000+ 模型校准）和 clean baseline seeds。\"only binary response patterns\" 和 \"black-box\" 的标签过度简化了实际访问需求。应区分 target model access (binary only) vs. external item bank (substantial)。\n\n**W2.** **QLoRA SFT 生态效度 vs. 标题范围**（R1-W1, R2 AGREE）\n标题 \"Benchmark Contamination\" 暗示广泛适用性，但实验仅覆盖 QLoRA SFT。Introduction 有 SFT scope 限定但 title/abstract 未充分反映。\n\n**W3.** **缺乏与 ConStat 等方法的实证对比**（R2-N2, R1 partial REBUT → 见 Divergence）\nDiscussion 称与 ConStat \"complementary\" 但无实证验证。论文自身 Table 3 已揭示 ℓz* 检测劣势。至少应系统解释为何不做直接对比。\n\n**W4.** **PSN-IRT 校准循环性**（R1-W5, R2 AGREE）\n校准样本可能包含被污染模型，Appendix F.2 随机扰动分析未覆盖系统性偏差（高估 θ → 偏移 difficulty）。\n\n**W5.** **Bootstrap CI 小样本可靠性**（R1-W3, R2 partial REBUT）\nMistral n=6 下 percentile bootstrap coverage 较差。BCa 已在 Appendix G 但主文未使用。建议主文改用 BCa 或加注 caveat。\n\n**W6.** **遗漏直接相关近期工作**（R2-W5, R1 AGREE）\nHan et al. (EACL 2026 Findings, arXiv 2510.07175) 处于 psychometrics × contamination 交叉点未引用；RADAR (Zawalski et al., 2025) 也值得讨论。\n\n**W7.** **Cohen's d 将被污染模型视为固定点**（R1-W6, R2 partial REBUT）\n未报告每个污染条件的运行次数。如仅 1 次，低估真实不确定性。效应量极大故不影响定性结论。\n\n**W8.** **LD 模拟代表性有限**（R1-W7, R2 AGREE）\nTestlet+Gaussian 模型不一定捕捉真实 LLM 依赖结构（attention 机制、序列效应等）。应在 Limitations 讨论。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致（[AGREE]）：\n\n| # | 问题 | R1 | R2 | 共识 |\n|---|------|----|----|------|\n| 1 | Post-RL N=1 不应为核心贡献 | W4 → AGREE | N1 | 降级为 preliminary observation |\n| 2 | Inverted-U 证据薄弱 | N2 | W3 → AGREE | 降级或补数据 |\n| 3 | 25% 条件透明性 | N1 | — → AGREE | §3.3 必须补充描述 |\n| 4 | 实验矩阵不完整 | N3 | — → AGREE | 补数据或限定 claims |\n| 5 | Abstract n=10 事实错误 | N4 | — → AGREE | 简单修正 |\n| 6 | Black-box framing overclaim | W2 | W1 | 调整术语或明确定义 |\n| 7 | QLoRA SFT 范围 vs. 标题 | W1 | — → AGREE | title/abstract 加限定 |\n| 8 | PSN-IRT 循环性 | W5 | — → AGREE | 讨论系统性偏差 |\n| 9 | LD 模拟代表性 | W7 | — → AGREE | Limitations 讨论 |\n| 10 | 遗漏 Han et al. / RADAR | — → AGREE | W5 | Related Work 补充 |\n\n---\n\n## Reviewer Divergence\n\n**D1. ConStat 对比的严重程度**\n- R2（Must-Fix）：论文定位在 contamination detection 领域却不与主要方法（ConStat/PaCoST/CoDeC）对比是重大缺陷。\n- R1（Should-Fix）：信息访问层级不同使直接对比不公平——ConStat 需跨 benchmark 性能分数，ℓz* 仅需 binary responses。论文已通过 Table 3 自我揭示检测劣势。缺乏对比的原因应在论文中系统解释，但不应要求在不同访问层级的方法间做 apple-to-apple 对比。\n- **部分共识**：两人同意至少应在 Discussion/Related Work 中系统解释为何不做直接对比。\n\n**D2. Finding 2/3 的 novelty 评估**\n- R2：θ-shift dynamics 本质是 IRT 天花板效应，detection-diagnosis tradeoff 是 ℓz* by design 的结果。Novelty 有限。\n- R1：定性方向可预测，但定量结果（7.6× amplification、ARC-C 反转、57/60 vs 4/60 flagged cells）和边界条件是新的。LLM 严重违反 IRT 假设下理论预测是否成立需实证回答，empirical quantification 有独立价值。\n- **未达共识**：两人对 \"empirical validation in a new domain\" 的 contribution 价值评估存在根本性差异。\n\n---\n\n## Questions\n\n1. 25% 污染条件是预先计划的实验条件还是看到 15%/50% 趋势后追加的 post-hoc 探索？请在 §3.3 中透明说明。\n2. 每个污染条件（15%, 25%, 50%）有多少个独立训练 run？如果仅 1 次，Cohen's d 将污染 ℓz* 视为固定点是否合理？\n3. 为什么 ARC-C 仅在 Qwen 上测试而排除了 Llama 和 Mistral？Figure 2 灰色格子应简要说明缺失原因。\n4. Llama/Mistral 是否存在在 25% 污染下也出现 inverted-U 的可能？是否有计划补充这些条件？\n5. PSN-IRT 校准样本中被污染模型的比例是多少？是否可能导致 item difficulty 的系统性偏移？\n6. Reproducibility Statement 说 \"random seeds are reported for all experiments\"，但正文中未列出具体 seed 值。\n\n---\n\n## Missing References\n\n1. **Han et al. (2026)** \"Quantifying Data Contamination in Psychometric Evaluations of LLMs\" (EACL 2026 Findings, arXiv 2510.07175) — 直接处于 psychometrics × contamination 交叉点，虽侧重 personality inventories 但方法论高度相关\n2. **RADAR** (Zawalski et al., 2025, arXiv 2510.08931) — 近期有影响力的 mechanistic contamination detection 工作，与本文 \"behavioral characterization\" 形成对比\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warnings, 16 info）。\n\n**Warnings**:\n- Figure 2 heatmap 单元格内数值标注字号偏小，标准打印尺寸下可能需要放大阅读\n- Figure 4 的 4 个子图 axis label 和 legend 字号偏小（约正文 60-65%），建议增大至 ≥70%\n\n**Positive findings**:\n- 主正文恰好 8 页，符合 EMNLP 2026 页数限制\n- 7 个 display items（4 figures + 3 tables），密度 0.875/页，实证论文合理范围\n- 所有 float 位于首次引用附近，无漂移\n- 颜色方案色盲安全，灰度友好\n- 无 margin 溢出、LaTeX 渲染错误或 section heading 孤悬\n- References 格式一致，无未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0/5 | 3.0/5 | 3.0/5 |\n| Excitement | 3.0/5 | 2.5/5 | 2.75/5 |\n| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |\n| Overall | 3.5 | 3.0 | **3.0** |\n\n**评分理由**：\n\n本文做了一个有价值的跨学科迁移工作，将心理测量学 person-fit 统计量引入 LLM 污染检测。DiD 设计巧妙，detection-diagnosis tradeoff 分析有实际价值，诚实的 framing 值得肯定。\n\n然而，作为 EMNLP 2026 Long Paper 投稿，存在以下实质性问题：\n\n1. **证据基础与 claim 强度不匹配**：首要发现 inverted-U 仅基于 1 个模型 3 个数据点，且 25% 条件未在实验设置中描述（方法论透明性问题）；Post-RL 发现 N=1 却列为核心贡献。\n2. **实验覆盖面有缺口**：18 条件仅完成约 8 条，全部 7-8B 模型无规模多样性，Abstract 存在事实错误。\n3. **Framing 问题**：\"black-box access\" 过度简化了对 PSN-IRT 外部 item bank 的实质性依赖；标题范围超出 SFT-only 的实验证据。\n4. **Contribution density 偏薄**：四大发现中 Finding 4 缺乏支撑，Finding 2/3 的 novelty 存在争议（R2 认为 IRT 理论可预测，R1 认为经验量化有独立价值），仅 Finding 1 被两人认可为真正新颖但证据不足。\n\n综合评估，论文的跨学科贡献和方法论框架有价值，但证据基础和 contribution density 更适合 Findings 而非主会议。如果能：(a) 在 §3.3 透明描述所有实验条件，(b) 补充 Llama/Mistral 25% 数据验证 inverted-U 模型特异性，(c) 将 Post-RL 降级并调整 claims，(d) 修正 Abstract 事实错误和 framing，论文有潜力提升至 3.5 (Borderline Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 第 3-6 行以 pretraining contamination 为动机，但实验仅覆盖 SFT。第 14-18 行的 SFT scope 限定是好的改进，但应更突出。\n- 第 39 行 \"n=10 seeds each\" → 事实错误，Mistral n=6\n- Finding (4) 的 enumerated 位置暗示与其他发现同等份量，建议移除或明确标注 preliminary\n\n### §3.3 Experimental Setup\n- **关键缺陷**：仅描述 clean/15%/50% 三个条件，但 Table 1 和 §4.2 使用了 25% 数据。必须补充 25% 条件的描述和动机。\n- 未报告每个污染条件的独立运行次数\n- 未说明为什么 ARC-C 排除了 Llama/Mistral\n\n### §4.2 Non-Monotonic Dose-Response\n- 证据仅限 Qwen，但 §4.2 标题和叙事暗示更广泛的适用性\n- \"4.3× reduction from peak to high contamination\" 的描述准确但可能被噪声解释\n- 建议标题改为 \"Ability-Dependent Non-Monotonic Dose-Response\" 以反映 Qwen 特异性\n\n### §4.3 θ-Shift Dynamics\n- 第 66 行关于 MMLU 50% 处 accuracy vs. |d| 的 \"negative correlation\" 仅基于 3 个数据点，不应使用 \"correlation\" 一词\n- ARC-C ceiling effect 反转（第 70-73 行）是有价值的观察，但仅基于 Qwen\n\n### §4.4 Detection-Diagnosis Tradeoff\n- Table 3 accuracy z-score |d|=68.7 的解释（near-zero cross-seed variance）在正文中已给出，但可能仍误导读者\n- \"57/60 vs. 4/60 flagged cells\" 是有力对比，但诊断价值的具体应用场景（什么 workflow 需要 item-level diagnosis 而非 detection）未展示\n\n### §4.5 Post-RL\n- 应缩减为 Discussion 中一段。ℓz* 从 2.91→7.69 可能是 GRPO-induced θ-shift 而非 contamination residual——需 clean+GRPO control 来 disentangle。\n\n### §5 Discussion\n- \"complementary to ConStat\" 仅一句带过——应系统解释为何不做直接对比（信息访问层级差异）\n- PSN-IRT 校准循环性讨论不够深入——随机扰动 ≠ 系统性偏差\n\n### Abstract\n- ~250 词偏长，post-RL 部分可压缩\n- \"n=10 seeds each\" 事实错误\n- \"only binary response patterns\" 和 \"externally calibrated 4PL item parameters\" 的关系需更突出\n\n### Limitations\n- 覆盖了主要限制，但缺少对 LD 模拟代表性的讨论\n- 可增加对 PSN-IRT 系统性偏差的讨论\n\n### References\n- 遗漏 Han et al. (EACL 2026 Findings) 和 RADAR (Zawalski et al., 2025)\n- 当前 33 条引用数量对 EMNLP long paper 偏少",
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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "irt_personfit_contam",
    "report": "# 审稿报告 — Round 4 (Fresh Review)\n\n**论文**: What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n**Venue**: EMNLP 2026 (via ACL Rolling Review, Long Paper)\n**审稿日期**: 2026-05-22\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）\n**交叉轮数**: 1 轮（关键问题达成共识，无需第二轮）\n\n---\n\n## Summary\n\n本文首次将心理测量学中的 IRT person-fit 统计量（ℓz*）系统性地迁移到 LLM benchmark 污染检测领域，提出 Δℓz* difference-in-differences 设计以应对 LLM 对 IRT 假设的系统性违反。在三个 7-8B 模型家族（Qwen2.5-7B、Llama-3.1-8B、Mistral-7B）和两个 benchmark（MMLU、ARC-Challenge）上，通过 QLoRA SFT 控制实验验证了四个行为边界：inverted-U dose-response、模型特异性 θ-shift dynamics、detection-diagnosis tradeoff、以及初步的 post-RL 残留模式。论文定位为 characterization study 而非 detection tool。\n\n---\n\n## Strengths\n\n**S1.** **跨学科桥梁构建得当**（R1/R2 共识）。将教育测量中成熟的 person-fit 统计量（Snijders 2001, Karabatsos 2003）迁移到 LLM 污染检测，\"被污染 LLM ≈ 作弊考生\" 的类比自然且有说服力。两个此前独立的研究领域被有效连接。\n\n**S2.** **Δℓz* DiD 设计巧妙**（R1/R2 共识）。57/60 model-benchmark cells 在无污染下即产生 |ℓz*| > 1.96，说明绝对阈值不可用。差分设计将系统性 IRT 违反转化为可控特征，模拟验证支持其在 shared LD 下的鲁棒性（d_ratio ≥ 0.93 for σ_τ ≤ 0.5）。\n\n**S3.** **Detection-diagnosis tradeoff 有实际价值**（R1/R2 共识）。Table 3 系统对比了 ℓz*、HT、accuracy z-score 的检测力和诊断力，two-stage workflow 建议（先 z-score 筛查，再 ℓz* 诊断）具有实际指导意义。论文主动揭示 ℓz* 检测力劣于简单统计量，学术诚实。\n\n**S4.** **诚实的 framing 和自我审视**（R1/R2 共识）。论文将自身定位为 \"characterization\" 而非 \"detection tool\"；Appendix H 主动验证 PSN-IRT 依赖的必要性（MML-EM 失败，r_a=0.127）；Limitations 覆盖了主要范围限制。\n\n**S5.** **附录鲁棒性分析全面**（R1/R2 共识）。4PL vs. 3PL ablation、LD 模拟（shared + asymmetric）、参数扰动、BCa 校正、MML-EM refit 等覆盖了多个潜在质疑方向。\n\n**S6.** **θ-shift absorption 机制有理论深度**（R1 特别肯定）。高能力模型在高污染下检测信号反而减弱不是显而易见的，论文从 IRT 理论给出了清晰因果解释，并通过 fixed-θ vs. free-θ 对比验证了机制。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1.** **25% 污染条件未在 §3.3 描述——核心证据来源不透明**（R1-N1, R2 AGREE）\n§3.3 明确写 \"three conditions: clean, 15% contamination, and 50% contamination\"，但 Table 1 包含 Qwen 25% 数据（d=−8.22），inverted-U（Finding 1，论文首要贡献）完全依赖此数据点。25% 是先验计划还是看到非单调趋势后追加的 post-hoc 条件未说明。如果是 post-hoc，构成 researcher degrees of freedom。这是方法论透明性的核心缺陷。\n\n**C2.** **Inverted-U 证据不足以支撑首要发现地位**（R1-N2, R2 AGREE）\n仅基于 1 个模型家族（Qwen）的 3 个数据点（15%, 25%, 50%）。Llama 和 Mistral 均显示单调 dose-response（2/3 模型不支持 inverted-U）。CI 极宽（d(25%) CI: [−18.9, −5.7]）。3 点非单调性可由噪声产生。论文虽限定为 \"specific to Qwen\"，但 Abstract/Introduction 将其列为首要发现，claim 强度与证据不匹配。\n\n**C3.** **实验设计矩阵不完整**（R1-N3, R2 AGREE）\n完整 3 模型 × 2 benchmark × 3 污染水平 = 18 条件，实际仅完成约 8 条。ARC-C 仅 Qwen，25% 仅 Qwen，Mistral n=6。Figure 2 灰色格子直观暴露。此外全部模型为 7-8B（R2-N3），无法区分 Finding 2 的 ability-driven vs. scale-driven 效应。Abstract \"across three 7–8B model families (n=10 seeds each)\" 暗示完整覆盖。\n\n**C4.** **Abstract 事实错误**（R1-N4, R2 AGREE）\nAbstract 写 \"n=10 seeds each\"，但 §3.3 明确写 Mistral 仅 n=6。必须修正。\n\n**C5.** **Post-RL Finding 4 (N=1) 不应列为核心贡献**（R2-N1, R1 AGREE）\nN=1（Qwen+GRPO, 15%），§4.5 自己声明 \"no statistical inference is drawn\"，但 Abstract/Introduction 将其与其他三个经 factorial design 验证的发现并列。应降级为 Discussion 中的 preliminary observation。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1.** **\"Black-box access\" framing overclaim**（R1-W2, R2-W1, 交叉完全一致）\n方法依赖 PSN-IRT 外部 4PL item parameters（13,000+ 模型校准）和 clean baseline seeds。\"only binary response patterns\" 和 \"black-box\" 的标签过度简化了实际访问需求。应区分 target model access (binary only) vs. external item bank (substantial)。\n\n**W2.** **QLoRA SFT 生态效度 vs. 标题范围**（R1-W1, R2 AGREE）\n标题 \"Benchmark Contamination\" 暗示广泛适用性，但实验仅覆盖 QLoRA SFT。Introduction 有 SFT scope 限定但 title/abstract 未充分反映。\n\n**W3.** **缺乏与 ConStat 等方法的实证对比**（R2-N2, R1 partial REBUT → 见 Divergence）\nDiscussion 称与 ConStat \"complementary\" 但无实证验证。论文自身 Table 3 已揭示 ℓz* 检测劣势。至少应系统解释为何不做直接对比。\n\n**W4.** **PSN-IRT 校准循环性**（R1-W5, R2 AGREE）\n校准样本可能包含被污染模型，Appendix F.2 随机扰动分析未覆盖系统性偏差（高估 θ → 偏移 difficulty）。\n\n**W5.** **Bootstrap CI 小样本可靠性**（R1-W3, R2 partial REBUT）\nMistral n=6 下 percentile bootstrap coverage 较差。BCa 已在 Appendix G 但主文未使用。建议主文改用 BCa 或加注 caveat。\n\n**W6.** **遗漏直接相关近期工作**（R2-W5, R1 AGREE）\nHan et al. (EACL 2026 Findings, arXiv 2510.07175) 处于 psychometrics × contamination 交叉点未引用；RADAR (Zawalski et al., 2025) 也值得讨论。\n\n**W7.** **Cohen's d 将被污染模型视为固定点**（R1-W6, R2 partial REBUT）\n未报告每个污染条件的运行次数。如仅 1 次，低估真实不确定性。效应量极大故不影响定性结论。\n\n**W8.** **LD 模拟代表性有限**（R1-W7, R2 AGREE）\nTestlet+Gaussian 模型不一定捕捉真实 LLM 依赖结构（attention 机制、序列效应等）。应在 Limitations 讨论。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致（[AGREE]）：\n\n| # | 问题 | R1 | R2 | 共识 |\n|---|------|----|----|------|\n| 1 | Post-RL N=1 不应为核心贡献 | W4 → AGREE | N1 | 降级为 preliminary observation |\n| 2 | Inverted-U 证据薄弱 | N2 | W3 → AGREE | 降级或补数据 |\n| 3 | 25% 条件透明性 | N1 | — → AGREE | §3.3 必须补充描述 |\n| 4 | 实验矩阵不完整 | N3 | — → AGREE | 补数据或限定 claims |\n| 5 | Abstract n=10 事实错误 | N4 | — → AGREE | 简单修正 |\n| 6 | Black-box framing overclaim | W2 | W1 | 调整术语或明确定义 |\n| 7 | QLoRA SFT 范围 vs. 标题 | W1 | — → AGREE | title/abstract 加限定 |\n| 8 | PSN-IRT 循环性 | W5 | — → AGREE | 讨论系统性偏差 |\n| 9 | LD 模拟代表性 | W7 | — → AGREE | Limitations 讨论 |\n| 10 | 遗漏 Han et al. / RADAR | — → AGREE | W5 | Related Work 补充 |\n\n---\n\n## Reviewer Divergence\n\n**D1. ConStat 对比的严重程度**\n- R2（Must-Fix）：论文定位在 contamination detection 领域却不与主要方法（ConStat/PaCoST/CoDeC）对比是重大缺陷。\n- R1（Should-Fix）：信息访问层级不同使直接对比不公平——ConStat 需跨 benchmark 性能分数，ℓz* 仅需 binary responses。论文已通过 Table 3 自我揭示检测劣势。缺乏对比的原因应在论文中系统解释，但不应要求在不同访问层级的方法间做 apple-to-apple 对比。\n- **部分共识**：两人同意至少应在 Discussion/Related Work 中系统解释为何不做直接对比。\n\n**D2. Finding 2/3 的 novelty 评估**\n- R2：θ-shift dynamics 本质是 IRT 天花板效应，detection-diagnosis tradeoff 是 ℓz* by design 的结果。Novelty 有限。\n- R1：定性方向可预测，但定量结果（7.6× amplification、ARC-C 反转、57/60 vs 4/60 flagged cells）和边界条件是新的。LLM 严重违反 IRT 假设下理论预测是否成立需实证回答，empirical quantification 有独立价值。\n- **未达共识**：两人对 \"empirical validation in a new domain\" 的 contribution 价值评估存在根本性差异。\n\n---\n\n## Questions\n\n1. 25% 污染条件是预先计划的实验条件还是看到 15%/50% 趋势后追加的 post-hoc 探索？请在 §3.3 中透明说明。\n2. 每个污染条件（15%, 25%, 50%）有多少个独立训练 run？如果仅 1 次，Cohen's d 将污染 ℓz* 视为固定点是否合理？\n3. 为什么 ARC-C 仅在 Qwen 上测试而排除了 Llama 和 Mistral？Figure 2 灰色格子应简要说明缺失原因。\n4. Llama/Mistral 是否存在在 25% 污染下也出现 inverted-U 的可能？是否有计划补充这些条件？\n5. PSN-IRT 校准样本中被污染模型的比例是多少？是否可能导致 item difficulty 的系统性偏移？\n6. Reproducibility Statement 说 \"random seeds are reported for all experiments\"，但正文中未列出具体 seed 值。\n\n---\n\n## Missing References\n\n1. **Han et al. (2026)** \"Quantifying Data Contamination in Psychometric Evaluations of LLMs\" (EACL 2026 Findings, arXiv 2510.07175) — 直接处于 psychometrics × contamination 交叉点，虽侧重 personality inventories 但方法论高度相关\n2. **RADAR** (Zawalski et al., 2025, arXiv 2510.08931) — 近期有影响力的 mechanistic contamination detection 工作，与本文 \"behavioral characterization\" 形成对比\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warnings, 16 info）。\n\n**Warnings**:\n- Figure 2 heatmap 单元格内数值标注字号偏小，标准打印尺寸下可能需要放大阅读\n- Figure 4 的 4 个子图 axis label 和 legend 字号偏小（约正文 60-65%），建议增大至 ≥70%\n\n**Positive findings**:\n- 主正文恰好 8 页，符合 EMNLP 2026 页数限制\n- 7 个 display items（4 figures + 3 tables），密度 0.875/页，实证论文合理范围\n- 所有 float 位于首次引用附近，无漂移\n- 颜色方案色盲安全，灰度友好\n- 无 margin 溢出、LaTeX 渲染错误或 section heading 孤悬\n- References 格式一致，无未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0/5 | 3.0/5 | 3.0/5 |\n| Excitement | 3.0/5 | 2.5/5 | 2.75/5 |\n| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |\n| Overall | 3.5 | 3.0 | **3.0** |\n\n**评分理由**：\n\n本文做了一个有价值的跨学科迁移工作，将心理测量学 person-fit 统计量引入 LLM 污染检测。DiD 设计巧妙，detection-diagnosis tradeoff 分析有实际价值，诚实的 framing 值得肯定。\n\n然而，作为 EMNLP 2026 Long Paper 投稿，存在以下实质性问题：\n\n1. **证据基础与 claim 强度不匹配**：首要发现 inverted-U 仅基于 1 个模型 3 个数据点，且 25% 条件未在实验设置中描述（方法论透明性问题）；Post-RL 发现 N=1 却列为核心贡献。\n2. **实验覆盖面有缺口**：18 条件仅完成约 8 条，全部 7-8B 模型无规模多样性，Abstract 存在事实错误。\n3. **Framing 问题**：\"black-box access\" 过度简化了对 PSN-IRT 外部 item bank 的实质性依赖；标题范围超出 SFT-only 的实验证据。\n4. **Contribution density 偏薄**：四大发现中 Finding 4 缺乏支撑，Finding 2/3 的 novelty 存在争议（R2 认为 IRT 理论可预测，R1 认为经验量化有独立价值），仅 Finding 1 被两人认可为真正新颖但证据不足。\n\n综合评估，论文的跨学科贡献和方法论框架有价值，但证据基础和 contribution density 更适合 Findings 而非主会议。如果能：(a) 在 §3.3 透明描述所有实验条件，(b) 补充 Llama/Mistral 25% 数据验证 inverted-U 模型特异性，(c) 将 Post-RL 降级并调整 claims，(d) 修正 Abstract 事实错误和 framing，论文有潜力提升至 3.5 (Borderline Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 第 3-6 行以 pretraining contamination 为动机，但实验仅覆盖 SFT。第 14-18 行的 SFT scope 限定是好的改进，但应更突出。\n- 第 39 行 \"n=10 seeds each\" → 事实错误，Mistral n=6\n- Finding (4) 的 enumerated 位置暗示与其他发现同等份量，建议移除或明确标注 preliminary\n\n### §3.3 Experimental Setup\n- **关键缺陷**：仅描述 clean/15%/50% 三个条件，但 Table 1 和 §4.2 使用了 25% 数据。必须补充 25% 条件的描述和动机。\n- 未报告每个污染条件的独立运行次数\n- 未说明为什么 ARC-C 排除了 Llama/Mistral\n\n### §4.2 Non-Monotonic Dose-Response\n- 证据仅限 Qwen，但 §4.2 标题和叙事暗示更广泛的适用性\n- \"4.3× reduction from peak to high contamination\" 的描述准确但可能被噪声解释\n- 建议标题改为 \"Ability-Dependent Non-Monotonic Dose-Response\" 以反映 Qwen 特异性\n\n### §4.3 θ-Shift Dynamics\n- 第 66 行关于 MMLU 50% 处 accuracy vs. |d| 的 \"negative correlation\" 仅基于 3 个数据点，不应使用 \"correlation\" 一词\n- ARC-C ceiling effect 反转（第 70-73 行）是有价值的观察，但仅基于 Qwen\n\n### §4.4 Detection-Diagnosis Tradeoff\n- Table 3 accuracy z-score |d|=68.7 的解释（near-zero cross-seed variance）在正文中已给出，但可能仍误导读者\n- \"57/60 vs. 4/60 flagged cells\" 是有力对比，但诊断价值的具体应用场景（什么 workflow 需要 item-level diagnosis 而非 detection）未展示\n\n### §4.5 Post-RL\n- 应缩减为 Discussion 中一段。ℓz* 从 2.91→7.69 可能是 GRPO-induced θ-shift 而非 contamination residual——需 clean+GRPO control 来 disentangle。\n\n### §5 Discussion\n- \"complementary to ConStat\" 仅一句带过——应系统解释为何不做直接对比（信息访问层级差异）\n- PSN-IRT 校准循环性讨论不够深入——随机扰动 ≠ 系统性偏差\n\n### Abstract\n- ~250 词偏长，post-RL 部分可压缩\n- \"n=10 seeds each\" 事实错误\n- \"only binary response patterns\" 和 \"externally calibrated 4PL item parameters\" 的关系需更突出\n\n### Limitations\n- 覆盖了主要限制，但缺少对 LD 模拟代表性的讨论\n- 可增加对 PSN-IRT 系统性偏差的讨论\n\n### References\n- 遗漏 Han et al. (EACL 2026 Findings) 和 RADAR (Zawalski et al., 2025)\n- 当前 33 条引用数量对 EMNLP long paper 偏少",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 478 · 2026-05-22T05:05:36.296167+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_9840a7d708128f2f1d02985bd9b8d901:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4065
}
```

</details>

---


### Assistant

_source line 479 · 2026-05-22T05:05:49.390749+00:00_

审稿报告已投递至 Research Director。

**审稿完成汇总**：

- **Overall Score: 3.0 (Findings)**
- **R1**: 3.5 Borderline Conference | **R2**: 3.0 Findings
- **交叉轮数**: 1 轮（关键问题高度一致，无需第二轮）

**5 个 Must-Fix 共识问题**：
1. 25% 污染条件未在 §3.3 描述（方法论透明性）
2. Inverted-U 证据薄弱（1 模型 × 3 点）
3. 实验矩阵不完整（8/18 条件）+ 模型规模单一（全 7-8B）
4. Abstract 事实错误（"n=10 seeds each"，Mistral 实际 n=6）
5. Post-RL Finding 4 (N=1) 不应列为核心贡献

**1 个分歧**：ConStat 实证对比——R2 认为 Must-Fix，R1 认为信息访问层级不同应降为 Should-Fix

**视觉审查**：通过（2 warnings: Figure 2/4 字号偏小）
**Issue Tracker**：已同步更新至 Round 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 51

## Round 51

2 recorded events


### User

_source line 480 · 2026-05-22T05:05:52.067269+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。总结：

- **N1 (Post-RL N=1)**: [AGREE] — 建议降级为 Discussion 中的 open question
- **N2 (缺乏与 ConStat 等对比)**: [REBUT] — 信息访问层级不同，直接对比不公平；建议降为 Should-Fix
- **N3 (模型规模不足)**: [AGREE] — 但建议通过限定 claim 范围而非要求补充大规模实验
- **W1-W5**: 除 W2 部分反驳（经验验证在 IRT 假设违反下仍有价值）外，其余均同意

维持 Overall 3.5 (Borderline Conference) 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 481 · 2026-05-22T05:06:10.832559+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **Reviewer 1**（方法严谨性）：3.5 Borderline Conference
- **Reviewer 2**（新颖性/完整性）：3.0 Findings
- **综合评分**：**3.0 (Findings)**

**关键共识问题**（按优先级）：
1. 25% 污染条件未在 §3.3 描述——inverted-U 核心证据来源不透明
2. Inverted-U 仅 1 模型 3 点，2/3 模型为单调——证据与 claim 不匹配
3. Post-RL (N=1) 列为核心贡献——应降级为 preliminary observation
4. 实验矩阵不完整（8/18 条件）+ 全部 7-8B 无规模多样性
5. Abstract 事实错误 "n=10 seeds each"（Mistral 实际 n=6）
6. "Black-box access" framing overclaim

**唯一分歧**：ConStat 实证对比的严重程度（R2: Must-Fix vs R1: Should-Fix）

Issue Tracker 已同步更新至 `review_issues.yaml`（Round 4，5 critical + 8 warning + 3 info + 2 divergence）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 52

## Round 52

82 recorded events


### User

_source line 482 · 2026-05-22T07:37:05.955164+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_personfit_contam
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (via ACL Rolling Review)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 483 · 2026-05-22T07:37:11.380557+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 484 · 2026-05-22T07:37:11.381145+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 485 · 2026-05-22T07:37:22.481979+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 486 · 2026-05-22T07:37:22.532640+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 487 · 2026-05-22T07:37:32.018351+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 488 · 2026-05-22T07:37:33.273450+00:00_

{"result":"# 项目 irt_personfit_contam 概况\n\n## 实验状态 (81 个)\n\n- **exp-domain-analysis**: DONE (success) — \n- **exp-ml-classifier-baseline**: DONE (success) — \n- **exp-v1-irt-refit-pilot**: DONE (negative) — \n- **exp-clean-control-delta**: DONE (success) — \n- **exp-fdr-correction**: DONE (success) — \n- **exp-cross-benchmark-analysis**: DONE (success) — \n- **exp-accuracy-zscore-baseline**: DONE (success) — \n- **exp-item-alignment-check**: DONE (negative) — \n- **exp-power-theory**: DONE (success) — \n- **exp-empirical-null**: DONE (negative) — \n- **exp-leaderboard-data-recon**: DONE (success) — \n- **exp-extended-sim**: DONE (success) — \n- **exp-two-sided**: DONE (negative) — \n- **phase_b_personfit**: DONE (success) — \n- **sim_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-ctrl-contam-qwen-5pct: 5% MMLU contamination produces smaller |d| than 15% (d=-6.58), confirming the ascending portion of the inverted-U dose-response curve. Combined with 15%/25%/50% data points, this yields a 4-point curve showing lz* detection power rising from 5%→25% then falling 25%→50% due to θ-shift absorption.（准备中）\n- exp-arcc-benchmark: ℓz* contamination detection generalizes beyond MMLU to ARC-Challenge, a second benchmark with PSN-IRT 4PL calibration — demonstrating cross-benchmark applicability and addressing reviewer concern about single-benchmark evaluation.（准备中）\n- arcc-clean-s10（准备中）\n- arcc-clean-s9（准备中）\n- arcc-clean-s8（准备中）\n- arcc-clean-s7（准备中）\n- exp-ctrl-contam-qwen-clean-s10: Tenth independent clean Qwen2.5-7B-Instruct baseline (seed=307) for n=10 Cohen's d variance estimation（准备中）\n- exp-constat-comparison: ConStat (NeurIPS 2024) requires multi-benchmark performance scores for contamination detection, making it inapplicable or underpowered in single-benchmark scenarios. ℓz* operates on binary response patterns from a single benchmark, demonstrating superior minimal-information detec
…[truncated 1809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1255
}
```

</details>

---


### Tool call

_source line 489 · 2026-05-22T07:37:33.775778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 490 · 2026-05-22T07:37:34.228036+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\usepackage{enumitem}
16	
17	\newcommand{\irtfit}{\textsc{IRT-FIT}}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{What Can Binary Response Patterns Reveal About Benchmark Contamination? \\
22	An IRT Person-Fit Characterization}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{sections/abstract}
31	\end{abstract}
32	
33	\input{sections/introduction}
34	\input{sections/related_work}
35	\input{sections/method}
36	\input{sections/results}
37	\input{sections/discussion}
38	\input{sections/conclusion}
39	
40	\input{sections/limitations}
41	
42	\section*{Reproducibility Statement}
43	Code and response data will be released upon acceptance.
44	Bootstrap confidence intervals use the percentile method with 10,000 resamples.
45	Clean baseline seeds: Qwen and Llama use seeds 0--9; Mistral uses seeds 0--5 (seeds 6--9 were lost due to server decommissioning).
46	Pre-calibrated 4PL item parameters are from the publicly available PSN-IRT item bank \citep{psnirt2026}.
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{sections/appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 491 · 2026-05-22T07:37:34.228573+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
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

_source line 492 · 2026-05-22T07:37:34.279105+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 493 · 2026-05-22T07:37:38.998499+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ACL Rolling Review call for papers submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ACL Rolling Review call for papers submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-22T07:37:41.910830+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_4/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_4/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-22T07:37:42.262493+00:00_

-rw-r--r-- 1 ubuntu ubuntu 474775 May 22 07:19 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_4/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-22T07:37:42.513711+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-22T07:37:42.564242+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 498 · 2026-05-22T07:37:51.749972+00:00_

Web search results for query: "EMNLP 2026 ACL Rolling Review call for papers submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about EMNLP 2026 submission guidelines through the ACL Rolling Review (ARR):

## Submission Process

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. Authors will follow a two-step process: Authors submit articles to ARR, where submissions receive reviews and meta-reviews from ARR reviewers and action editors; Authors commit their reviewed articles to a publication venue (e.g., EMNLP 2026), where Senior Area Chairs and Program Chairs make acceptance d
…[truncated 963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 12751
}
```

</details>

---


### Tool call

_source line 499 · 2026-05-22T07:37:58.975782+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
  }
}
```

</details>

---


### Tool result

_source line 500 · 2026-05-22T07:37:59.126888+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 501 · 2026-05-22T07:37:59.127219+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limit anonymity policy formatting requirements",
  "allowed_domains": "['aclrollingreview.org', 'aclweb.org', '2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines page limit anonymity policy formatting requirements",
    "allowed_domains": "['aclrollingreview.org', 'aclweb.org', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-22T07:38:17.897767+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines page limit anonymity policy formatting requirements"

Links: [{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, here's information about ACL Rolling Review 2026 author guidelines:

## Anonymity Policy

Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities must be avoided. Instead, use citations such as "Smith previously showed (Smith, 1991)…" Additionally, supplementary materials, including any links to repositories, should also b
…[truncated 895 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 18770
}
```

</details>

---


### Tool call

_source line 503 · 2026-05-22T07:38:30.049333+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 504 · 2026-05-22T07:38:31.003255+00:00_

1	Benchmark contamination in Large Language Models (LLMs) undermines evaluation validity, yet most detection methods require privileged access to training data, model internals, or output probabilities.
2	We present the first systematic characterization of IRT person-fit statistics for detecting SFT-stage contamination: the framework requires only binary response patterns from the target model---no access to weights, gradients, logits, or training data---combined with externally calibrated 4PL item parameters from a large-scale item bank; diagnostic $\theta$-anchoring additionally requires a clean baseline.
3	A contaminated LLM produces aberrant response patterns analogous to a test-taker with item preknowledge.
4	Using $\ell_z^*$ in a difference-in-differences design ($\Delta\ell_z^*$) across three 7--8B model families ($n{=}10$ independent seeds per condition; $n{=}6$ for Mistral) on MMLU (14,042 items) and ARC-Challenge (295 items), we identify three behavior boundaries:
5	(1) model-specific $\theta$-shift dynamics linking baseline ability to detection sensitivity, where higher-ability models show weaker free-$\theta$ detection due to $\theta$-shift absorption;
6	(2) a detection-diagnosis tradeoff where simpler statistics yield stronger detection but lack $\ell_z^*$'s diagnostic capabilities (seen/unseen decomposition, mechanistic $\theta$-shift analysis);
7	and (3) an ability-dependent non-monotonic dose-response, most pronounced in high-ability models (Qwen: $|d|$ peaks at 25\%, 4.3$\times$ decline to 50\%; Llama: directionally consistent, attenuated), empirically confirming $\theta$-shift absorption.
8	A preliminary single-model observation suggests $\ell_z^*$ patterns may persist after GRPO alignment, though this requires further investigation.
9	These findings establish when and why binary response patterns carry contamination information beyond aggregate accuracy.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 505 · 2026-05-22T07:38:31.003664+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 506 · 2026-05-22T07:38:31.907337+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation \citep{dodge2021, magar2022, sainz2023}.
4	As training corpora and public benchmarks both expand, the probability of overlap increases structurally \citep{jacovi2023, chang2024survey}.
5	When contamination occurs, benchmark scores no longer reflect genuine capability, undermining the primary mechanism by which the community compares and selects models.
6	
7	A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record.
8	N-gram overlap methods need the training corpus \citep{dodge2021, magar2022}.
9	Membership inference approaches require token-level probabilities \citep{minkprob2024, deng2024}.
10	Probing methods rely on crafted prompts \citep{golchin2024, oren2024}.
11	Performance-based methods require multiple test variants or output logits \citep{constat2024, codec2026}.
12	These methods form a detection frontier ordered by information access.
13	No existing method operates using only binary response patterns, without model weights, gradients, logits, or training data---though, as we show, effective detection additionally requires externally calibrated item parameters.
14	
15	In this work, we focus on SFT-stage contamination---where benchmark answers are explicitly included in fine-tuning data---for three reasons.
16	First, controlled experiments require known ground-truth contamination sets, achievable through fine-tuning with specific benchmark items.
17	Second, SFT-stage contamination is increasingly relevant as fine-tuning-as-a-service platforms proliferate, creating new pathways for benchmark data to enter training mixtures.
18	Third, SFT provides a methodologically clean setting to characterize detection boundaries before extending to noisier pretraining scenarios.
19	
…[truncated 4461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-22T07:38:32.108560+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-22T07:38:32.410143+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{IRT Person-Fit Framework}
5	\label{sec:framework}
6	
7	We adopt the four-parameter logistic (4PL) IRT model to characterize contamination-induced aberrance in LLM response patterns.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ difficulty, $c_i$ the lower asymptote (guessing), and $d_i$ the upper asymptote (slip).
14	Item parameters are pre-calibrated by PSN-IRT \citep{psnirt2026} from a large-scale leaderboard dataset; we use these external parameters rather than re-estimating from potentially contaminated data, since our MML-EM refit shows discrimination recovery degrades to $r_a{=}0.127$ on contaminated leaderboard data.
15	
16	Given item parameters and a binary response vector $\mathbf{x} = (x_1, \ldots, x_n)$, we compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized log-likelihood residual quantifying deviation between observed and expected response patterns.
17	The Snijders correction accounts for estimation uncertainty in $\hat{\theta}_{\text{MLE}}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null \citep{drasgow1985, snijders2001}; \citet{magis2012} provide a detailed treatment of how response model selection and ability estimation affect $\ell_z^*$.
18	Large negative $\ell_z^*$ indicates aberrant responding (unexpected failures on easy items or unexpected successes on hard items); large positive values indicate over-consistent patterns.
19	
20	\subsection{$\Delta\ell_z^*$ Difference-in-Differences Design}
21	\label{sec:did}
22	
23	LLM response patterns systematically violate IRT assumptions of local independence and unidimensionality.
24	In our empirical data, 57 of 60 model-benchmark cells yield $|\ell_z^*| > 1.96$ even absent contamination, 
…[truncated 3614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 509 · 2026-05-22T07:38:32.511020+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_personfit_contam",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 510 · 2026-05-22T07:38:32.612030+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/decisions.yaml\", \"content\": \"_next_id: 37\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 07:13 UTC\\n  summary: 'MVP 采用两阶段验证: Phase A 模拟验证（无GPU）+ Phase B 真实数据探测'\\n  rationale: '核心假设（person-fit stats 检测 contamination）可在理想化 IRT 模拟中先验证——如果模拟中都检测不到，真实数据更不可能。Phase\\n    A 零 GPU 成本、1-2 天即可得到 go/no-go 信号，避免在假设不成立时浪费 GPU 资源。Pass 标准: 15% contamination\\n    下 lz* 检测率 > 80%（α=0.05）且 inverted-U shape 可观测。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 07:16 UTC\\n  summary: '根据 Reviewer 审查细化 MVP: 加入 PSN-IRT 参数 null distribution sanity check + 按\\n    benchmark 规模分层 pass/fail + Phase B 量化标准'\\n  rationale: 'Reviewer 指出三个 warning: (1) Phase B 无 pass/fail 标准导致不可证伪; (2) 6 个 benchmark\\n    item 数差异巨大(164~14K)，统一 80% 检测率不合理; (3) PSN-IRT 用神经网络估参，经典 lz* 的 N(0,1) 渐近性质未必成立。三者均成立，分别补充:\\n    Phase B 定义 lz* 跨模型方差 + 异常值标准; 大/小 benchmark 分层 pass 阈值(80%/50%); Phase A 新增 null\\n    distribution KS 检验。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 07:22 UTC\\n  summary: '修正 benchmark 分类: ARC-C 降为小(295 items); MVP 不混用 TruthfulQA 3PL; 加入 a≤0\\n    item 过滤'\\n  rationale: 'Reviewer critical: PSN-IRT 中 ARC-C 仅 295 items（非预期的 ~1,172），不满足大 benchmark\\n    ≥1000 阈值。TruthfulQA 无 PSN-IRT 4PL 参数（仅 ATLAS 3PL），混用引入方法论不一致。部分 items a < 0（负判别度）违反\\n    IRT 假设需过滤。MVP 改为只用 5 个 PSN-IRT benchmark，大 benchmark 仅 MMLU/HellaSwag/GSM8K 三个。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 08:11 UTC\\n  summary: 'Phase A Partial Pass: 方法机制验证成功，power 随 n_items 递减为预期行为，推进 Phase B'\\n  rationale: sim_001 结果：(1) Null check 全通过（MMLU/HellaSwag/GSM8K KS p>0.05），PSN-IRT\\n    4PL 参数与 lz* N(0,1) 假设兼容；(2) Inverted-U shape 全部可观测；(3) MMLU(14K items) power@15%=97.9%\\n    远超 80% 阈值。未达标项：HellaSwag 73.3%（差 6.7pp）、GSM8K 57.8%。但 3 个大 benchmark 均>50%，不触发\\n    global fail。Power 与 
…[truncated 1440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 511 · 2026-05-22T07:38:40.390808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 512 · 2026-05-22T07:38:40.792729+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Detection Signal Across Model Families}
5	\label{sec:detection}
6	
7	Table~\ref{tab:cohens_d} presents Cohen's $d$ effect sizes for $\ell_z^*$ across three model families and two benchmarks.
8	All confidence intervals exclude zero, confirming that $\Delta\ell_z^*$ reliably separates contaminated from clean models at both contamination levels.
9	
10	On MMLU, effect sizes range from $|d|{=}1.90$ (Qwen at 50\%) to $|d|{=}8.22$ (Qwen at 25\%), with Llama ($|d|{=}2.27$/$2.97$/$2.50$) and Mistral ($|d|{=}2.64$/$3.50$) falling between.
11	On ARC-C (295 items), Qwen yields $|d|{=}3.16$ at 15\% and $|d|{=}5.30$ at 50\%, demonstrating that detection remains feasible even on small benchmarks when contamination is sufficiently concentrated.
12	
13	Clean-model $\ell_z^*$ baselines diverge substantially across families: Qwen ${+}8.68$ ($\text{SD}{=}0.74$), Mistral ${+}4.02$ ($\text{SD}{=}2.05$), Llama ${+}0.29$ ($\text{SD}{=}1.45$), and ARC-C Qwen ${-}5.42$ ($\text{SD}{=}0.16$).
14	Absolute $\ell_z^*$ thresholds would produce contradictory results: Qwen's contaminated $\ell_z^*$ at 15\% (${+}3.85$) is still positive.
15	The $\Delta\ell_z^*$ design normalizes these divergent baselines: Cohen's $d$ yields comparable effect sizes ($|d|{=}1.90$--$8.22$) despite order-of-magnitude baseline differences.
16	Figure~\ref{fig:heatmap} provides a visual summary.
17	
18	\begin{table}[t]
19	\centering
20	\caption{Cohen's $d$ for $\Delta\ell_z^*$ across model families ($n{=}10$ clean seeds, bootstrap 95\% CI, 10,000 resamples). All CIs exclude 0.}
21	\label{tab:cohens_d}
22	\footnotesize
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}llrrr@{}}
25	\toprule
26	Model & Bench. & $d$ (15\%) [CI] & $d$ (25\%) [CI] & $d$ (50\%) [CI] \\
27	\midrule
28	Qwen & MMLU & $-6.58$ [$-15.2$, $-4.5$] & $-8.22$ [$-18.9$, $-5.7$] & $-1.90$ [$-5.0$, $-1.0$] \\
29	Llama & MMLU & $-2.27$ [$-4.6$, $-1.6$] & $-2.97$ [$-6.1$, $-2.0$] & $-2.50$ [$-5.0$, 
…[truncated 12760 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 513 · 2026-05-22T07:38:40.793061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 514 · 2026-05-22T07:38:41.295168+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	Our findings reveal both the strengths and boundaries of IRT person-fit for contamination detection: $\ell_z^*$ reliably detects SFT-stage contamination across model families, but three boundary conditions constrain its practical utility.
4	
5	\paragraph{Characterization over tool.}
6	The detection-diagnosis tradeoff (\S\ref{sec:degradation}) shows that simpler statistics detect contamination more powerfully than $\ell_z^*$: accuracy $z$-scores yield $|d|$ values several-fold to over an order of magnitude larger, and HT generally exceeds $\ell_z^*$.
7	The value of the IRT framework lies not in detection power but in mechanistic understanding: the $\theta$-shift analysis reveals \emph{why} detection sensitivity varies across models and contamination levels, the seen/unseen decomposition identifies \emph{what fraction} of items are memorized, and the 4PL parameterization captures item-level ceiling effects that 3PL misattributes as aberrance.
8	These diagnostic capabilities are invisible to accuracy $z$-scores or HT.
9	
10	\paragraph{Practical implications.}
11	Two results have immediate consequences.
12	Free-$\theta$ estimation can produce misleading dose-response curves; anchoring $\theta$ to a pre-contamination baseline substantially amplifies detection for high-ability models but is unnecessary where free estimation already captures the signal.
13	The benchmark size boundary means $\ell_z^*$ is most informative for large benchmarks ($n > 7{,}000$ items for 80\% power at 15\% contamination); on small benchmarks like ARC-C (295 items), detection relies on concentrated contamination effects.
14	
15	\paragraph{Scope and calibration.}
16	Universal baseline misfit (57/60 cells flagged) confirms systematic IRT violations; the $\Delta\ell_z^*$ design turns this into a feature through within-model differencing, but requires clean baselines or cross-benchmark references.
17	PSN-IRT provides pre-calibrated 4PL parameters for 
…[truncated 2181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 515 · 2026-05-22T07:38:41.295565+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 516 · 2026-05-22T07:38:42.701058+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Benchmark contamination detection.}
4	Contamination detection methods span a wide range of information requirements.
5	Corpus-search methods match benchmark items directly against pretraining data \citep{dodge2021, magar2022}, but require full corpus access unavailable for closed models.
6	Membership inference attacks (MIA) use token-level log-probabilities to distinguish training from unseen examples \citep{minkprob2024, deng2024}.
7	Generation-based probes elicit benchmark content via prompting \citep{golchin2024, golchin2024quiz, oren2024}.
8	Performance-based methods compare accuracy on target and reference sets \citep{constat2024, pacost2024, codec2026}, requiring multiple evaluations or in-context learning passes.
9	\citet{zhou2023benchmark} and \citet{sainz2023} argue for systematic contamination measurement, \citet{jacovi2023} propose mitigation strategies, and \citet{bordt2025forget} show that contamination can be ``forgotten'' under sufficient continued training.
10	\citet{han2026quantifying} quantify contamination in psychometric evaluations of LLMs, demonstrating that memorization effects extend beyond standard benchmarks.
11	\citet{kattamuri2025radar} take a mechanistic interpretability approach, using activation patterns to distinguish recall-based from reasoning-based responses; our work instead operates purely on behavioral response patterns without access to model internals.
12	
13	A critical limitation unites all token-level methods: \citet{wang2025fragility} show that RL post-training renders MIA-based detectors no better than random across 10 methods and 4 benchmarks, because RL reshapes token distributions while largely preserving binary correctness patterns.
14	\citet{selfcritique2026} and \citet{zhang2026rlvr} propose RL-specific solutions but require generation-level access.
15	Our approach requires no access to model weights, logits, or training data---only binary response patt
…[truncated 2476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 517 · 2026-05-22T07:38:42.852109+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 518 · 2026-05-22T07:38:43.053270+00:00_

1	\section*{Limitations}
2	
3	Our controlled experiments cover three model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B) at the 7--8B scale with QLoRA fine-tuning; validation on larger models (13B, 70B), mixture-of-experts architectures, and full-parameter fine-tuning remains future work.
4	The observed negative correlation between baseline ability and detection sensitivity rests on three model families and should be treated as a trend rather than a confirmed relationship.
5	Our findings are scoped to SFT-based contamination and may not generalize to pretraining contamination, which operates through different learning dynamics.
6	The post-RL characterization is $N{=}1$ (Qwen only, GRPO algorithm, 15\% contamination on MMLU); generalization to other model families, RL methods (PPO, DPO), and contamination levels requires further validation.
7	LLMs systematically violate IRT assumptions of local independence and unidimensionality; while the $\Delta\ell_z^*$ design mitigates shared misfit through within-model differencing, the theoretical properties of this correction under severe model misfit remain an open question.
8	Our local dependence simulations employ testlet and Gaussian models that may not fully capture the dependency structures induced by attention mechanisms and sequential processing in LLMs; validating robustness under more realistic dependency structures remains an open question.
9	The framework depends on pre-calibrated 4PL item parameters from PSN-IRT; parameter estimation errors propagate to $\ell_z^*$ computation, and the approach requires externally maintained parameter banks.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 519 · 2026-05-22T07:38:43.053639+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_personfit_contam",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 520 · 2026-05-22T07:38:43.104108+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'irt_personfit_contam'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 521 · 2026-05-22T07:38:48.575635+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 522 · 2026-05-22T07:38:48.576036+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We presented the first systematic characterization of IRT person-fit statistics for LLM benchmark contamination detection.
4	Controlled experiments across three 7--8B model families ($n{=}10$ seeds; $n{=}6$ for Mistral) establish reliable SFT-stage detection from binary response patterns (all bootstrap 95\% CIs exclude zero) while revealing three boundary conditions: $\theta$-shift dynamics linking baseline ability to detection sensitivity, a detection-diagnosis tradeoff favoring simpler statistics for detection but $\ell_z^*$ for mechanistic insight, and ability-dependent non-monotonic dose-response.
5	Future work should investigate pretraining-stage signatures, calibration-free approaches, and validation across broader model scales.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 523 · 2026-05-22T07:38:48.927568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 524 · 2026-05-22T07:38:49.881578+00:00_

1	\section{Simulation Validation}
2	\label{app:simulation}
3	
4	Under the null (no contamination), bootstrap $\ell_z^*$ tracks $\mathcal{N}(0,1)$: mean bias 0.041 and standard deviation 1.003 on MMLU.
5	Kolmogorov--Smirnov rejection rates vary with benchmark size: 8.3\% for MMLU and HellaSwag ($n > 10{,}000$), 50.0\% for GSM8K ($n = 1{,}319$), 58.3\% for ARC-C ($n = 295$), and 75.0\% for HumanEval ($n = 164$).
6	$\ell_z^*$ is well-calibrated for benchmarks with $n \geq 10{,}000$ items; smaller benchmarks show increasing finite-sample deviations from normality.
7	
8	Two-sided testing eliminates the inverted-U artifact: MMLU achieves 97.8\% power at 15\% contamination and sustains ${>}$93\% at all levels.
9	Power scales with $\sqrt{n}$, as predicted by the noncentrality parameter $\delta \propto \sqrt{n}$.
10	The empirical power function, derived via Gauss--Hermite quadrature ($K=30$) over the ability distribution, achieves $R^2 = 0.957$ against simulated values, with approximate minimum benchmark size of $n \geq 7{,}958$ items for 80\% power at 15\% contamination under MMLU item parameters.
11	
12	\section{4PL vs.\ 3PL Ablation Details}
13	\label{app:4pl_ablation}
14	
15	Table~\ref{tab:4pl_3pl_power} reports detection power (proportion of 2{,}000 simulation replicates rejecting $H_0$ at $\alpha{=}0.05$, two-sided) for 4PL and 3PL parameterizations across five benchmarks and seven contamination levels.
16	The 4PL model yields higher power than 3PL at every non-trivial contamination level on every benchmark.
17	The advantage is largest on MMLU and HellaSwag, where upper-asymptote ($d < 1$) violations are most prevalent, and smallest on ARC-Challenge and HumanEval, where limited item counts constrain power under both parameterizations.
18	
19	Power is non-monotonic at 75\% contamination under 4PL on four of five benchmarks (e.g., MMLU: $.952 \to .938$; GSM8K: $.846 \to .802$).
20	This reflects the $\theta$-shift boundary condition described in \S\ref{sec:inverted_u}: at
…[truncated 5312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 525 · 2026-05-22T07:38:49.982520+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 526 · 2026-05-22T07:38:50.636808+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 527 · 2026-05-22T07:38:50.687436+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 528 · 2026-05-22T07:38:50.738082+00:00_

1	% =============================================================================
2	% references.bib — IRT Person-Fit Contamination Detection Paper
3	% Cleaned: 2026-05-21 | 33 entries (orphan entries removed)
4	% =============================================================================
5	
6	% =============================================================================
7	% Person-Fit Statistics (Psychometrics)
8	% =============================================================================
9	
10	@article{drasgow1985,
11	  title = {Appropriateness Measurement with Polychotomous Item Response Models and Standardized Indices},
12	  author = {Drasgow, F. and Levine, M. V. and Williams, E. A.},
13	  journal = {British Journal of Mathematical and Statistical Psychology},
14	  year = {1985},
15	  volume = {38},
16	  number = {1},
17	  pages = {67--86},
18	  doi = {10.1111/j.2044-8317.1985.tb00817.x},
19	}
20	
21	@article{karabatsos2003,
22	  title = {Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics},
23	  author = {Karabatsos, G.},
24	  journal = {Applied Measurement in Education},
25	  year = {2003},
26	  volume = {16},
27	  number = {4},
28	  pages = {277--298},
29	  doi = {10.1207/S15324818AME1604_2},
30	}
31	
32	@article{meijer2001,
33	  title = {Methodology Review: Evaluating Person Fit},
34	  author = {Meijer, R. R. and Sijtsma, K.},
35	  journal = {Applied Psychological Measurement},
36	  year = {2001},
37	  volume = {25},
38	  number = {2},
39	  pages = {107--135},
40	  doi = {10.1177/01466210122031957},
41	}
42	
43	@article{sinharay2017,
44	  title = {Which Statistic Should Be Used to Detect Item Preknowledge When the Set of Compromised Items Is Known?},
45	  author = {Sinharay, S.},
46	  journal = {Applied Psychological Measurement},
47	  year = {2017},
48	  doi = {10.1177/0146621617698453},
49	}
50	
51	@article{snijders2001,
52	  title = {Asymptotic Null Distribution of Person Fit Statistics with Estimated Person Pa
…[truncated 1659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 529 · 2026-05-22T07:38:58.215299+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/ -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
  "description": "Find config files in agent directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/ -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
    "description": "Find config files in agent directory"
  }
}
```

</details>

---


### Tool result

_source line 530 · 2026-05-22T07:38:59.169085+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 531 · 2026-05-22T07:38:59.320058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 532 · 2026-05-22T07:38:59.320554+00:00_

100	\midrule
101	Llama & 15\% & $-$2.95 & [$-$8.70, 2.80] & [$-$5.89, $-$2.29] \\
102	 & 50\% & $-$3.31 & [$-$9.63, 3.01] & [$-$6.47, $-$2.59] \\
103	\bottomrule
104	\end{tabular}}
105	\end{table}
106	
107	\paragraph{Cross-family consistency.}
108	Table~\ref{tab:cross_family} confirms that both model families produce large negative Cohen's $d$ under contamination.
109	The $|\Delta d| = 2.32$ gap at 50\% contamination reflects Qwen's non-monotonic dose-response (the $\theta$-shift boundary condition; \S\ref{sec:inverted_u}), not a failure of detection robustness---both families remain well above conventional large-effect thresholds ($|d| > 0.8$) at both contamination levels.
110	
111	\begin{table}[t]
112	\centering
113	\caption{Cross-family consistency of contamination detection ($n{=}3$ pilot). Both families show large negative $d$ under contamination. Superseded by $n{=}10$ results in \S\ref{sec:detection}; retained for methodological transparency.}
114	\label{tab:cross_family}
115	\small
116	\begin{tabular}{@{}lcccl@{}}
117	\toprule
118	Condition & Qwen $d$ & Llama $d$ & $|\Delta d|$ & Consistent? \\
119	\midrule
120	15\% contam. & $-$3.42 & $-$2.95 & 0.47 & Yes \\
121	50\% contam. & $-$0.99 & $-$3.31 & 2.32 & Yes \\
122	\bottomrule
123	\end{tabular}
124	\end{table}
125	
126	\section{Baseline $\ell_z^*$ Interpretation}
127	\label{app:baseline_meaning}
128	
129	The baseline $\ell_z^*$ value reflects a model's difficulty-ordering consistency under the 4PL model, not its accuracy alone.
130	In the empirical data, Mistral ($\text{acc}{=}0.514$, lowest among the 12 models) exhibits $\ell_z^*{=}{+}5.42$ (second highest), because its response pattern follows the IRT-predicted difficulty ordering more closely than higher-accuracy models whose responses violate the assumed item structure.
131	This dissociation explains why Mistral produces the strongest contamination signal despite the lowest accuracy: its lower baseline ability ($\hat{\theta}{=}{-}1.16$) provides greater 
…[truncated 9232 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 533 · 2026-05-22T07:39:06.398508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex",
  "offset": "290"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex",
    "offset": "290"
  }
}
```

</details>

---


### Tool result

_source line 534 · 2026-05-22T07:39:06.900949+00:00_

290	\end{table}
291	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 535 · 2026-05-22T07:39:07.152485+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
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

_source line 536 · 2026-05-22T07:39:07.303448+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 537 · 2026-05-22T07:39:12.624508+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 538 · 2026-05-22T07:39:13.478310+00:00_

## Review Issue Tracker — Round 4 (fresh review, 2026-05-22)
## Reviewer 1 (方法严谨性, 3.5 Borderline Conference) + Reviewer 2 (新颖性/完整性, 3.0 Findings)

# ===== CRITICAL ISSUES =====

- id: "R4-N1"
  summary: "25% 污染条件未在 §3.3 实验设置中描述——inverted-U 核心证据来源不透明"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 4
  last_seen_round: 4
  mentions:
    - round: 4
      reviewers: [1, 2]
      note: "R1-N1 提出，R2 交叉 AGREE。§3.3 写 three conditions (clean, 15%, 50%)，但 Table 1 含 Qwen 25% 数据 (d=-8.22)。25% 是先验还是 post-hoc？若 post-hoc 则构成 researcher degrees of freedom。Finding 1 (inverted-U) 完全依赖此数据点。"
  action_items:
    - round: 4
      action: "§3.3 补充所有实验条件描述（含 25%），说明运行动机和时间顺序，post-hoc 则标注"
      assigned_to: paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R4-N2"
  summary: "Inverted-U 证据不足——仅 1 个模型 3 个数据点，2/3 模型为单调 dose-response"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 4
  last_seen_round: 4
  mentions:
    - round: 4
      reviewers: [1, 2]
      note: "R1-N2 提出，R2 交叉 AGREE (升级自 R2-W3)。Qwen 3 点 (15%/25%/50%)，CI 极宽 (d(25%) CI: [-18.9, -5.7])。Llama/Mistral 单调且未测 25%。3 点非单调性可由噪声产生。Abstract/Intro 将其列为首要发现，claim 强度与证据不匹配。"
  action_items:
    - round: 4
      action: "降级 inverted-U 为 Qwen-specific observation，调整 Abstract/Intro 位次"
      assigned_to: paper_agent
      status: in_progress
    - round: 4
      action: "Llama 25% MMLU 实验验证 dose-response 单调性"
      assigned_to: agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R4-N3"
  summary: "实验设计矩阵不完整——18 条件仅完成约 8 条件"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 4
  last_seen_round: 4
  mentions:
    - round: 4
      reviewers: [1, 2]
      note: "R1-N3 提出，R2 交叉 AGREE。ARC-C 仅 Qwen，25% 仅 Qwen，Mistral n=6。Figure 2 灰色格子直观暴露。Abstract 'across three model families' 暗示完整覆盖。R2 补充：模型全部 7-8B，规模覆盖也不足 (R2-N3)。"
  action_items:
    - round: 4
      action:
…[truncated 14736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 539 · 2026-05-22T07:39:13.980558+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_reports/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check existing review reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_reports/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check existing review reports"
  }
}
```

</details>

---


### Tool result

_source line 540 · 2026-05-22T07:39:14.482749+00:00_

round_0.md
round_1.md
round_2.md
round_3.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 541 · 2026-05-22T07:39:14.734050+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/ -type f 2>/dev/null | head -20",
  "description": "List agent directory files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/agent/ -type f 2>/dev/null | head -20",
    "description": "List agent directory files"
  }
}
```

</details>

---


### Tool result

_source line 542 · 2026-05-22T07:39:14.784714+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 543 · 2026-05-22T07:39:45.355258+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 544 · 2026-05-22T07:39:46.509886+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1154
}
```

</details>

---


### Tool call

_source line 545 · 2026-05-22T07:39:46.661052+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/ -name \"config.yaml\" -path \"*/irt_personfit_contam/*\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/ -name \"config.yaml\" -path \"*/irt_personfit_contam/*\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 546 · 2026-05-22T07:39:46.862181+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 547 · 2026-05-22T07:39:52.180808+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/ -name \"config.yaml\" -not -path \"*/.git/*\" 2>/dev/null | head -10",
  "description": "Find all config.yaml files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/ -name \"config.yaml\" -not -path \"*/.git/*\" 2>/dev/null | head -10",
    "description": "Find all config.yaml files"
  }
}
```

</details>

---


### Tool result

_source line 548 · 2026-05-22T07:39:52.382051+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 549 · 2026-05-22T07:39:55.996492+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/ -name \"*.yaml\" -path \"*/irt_personfit_contam/*\" -not -path \"*artifacts*\" -not -path \"*/.git/*\" 2>/dev/null | head -10",
  "description": "Find yaml files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/ -name \"*.yaml\" -path \"*/irt_personfit_contam/*\" -not -path \"*artifacts*\" -not -path \"*/.git/*\" 2>/dev/null | head -10",
    "description": "Find yaml files in project"
  }
}
```

</details>

---


### Tool result

_source line 550 · 2026-05-22T07:39:56.298883+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/sinharay2017.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/minkprob2024.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/wang2025fragility.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/psnirt2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/karabatsos2003.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/selfcritique2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/constat2024.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/atlas2025.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/hong2021lzm.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/distill_tmp/codec2026.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 551 · 2026-05-22T07:40:00.114209+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/ -name \"config.*\" -not -path \"*/.git/*\" -not -path \"*/node_modules/*\" 2>/dev/null | head -10",
  "description": "Find all config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/ -name \"config.*\" -not -path \"*/.git/*\" -not -path \"*/node_modules/*\" 2>/dev/null | head -10",
    "description": "Find all config files"
  }
}
```

</details>

---


### Tool result

_source line 552 · 2026-05-22T07:40:00.316672+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/torchgen/static_runtime/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/torchgen/static_runtime/config.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/coverage/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/coverage/config.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/datasets/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/datasets/config.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/util/config.h
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/config.h
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/python/config.h
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.venv/lib/python3.14/site-packages/pyarrow/src/arrow/python/config.cc

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 553 · 2026-05-22T07:40:07.047535+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_4/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_4/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 554 · 2026-05-22T07:40:07.148305+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Fri May 22 07:19:07 2026 UTC
ModDate:         Fri May 22 07:19:07 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           14
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       474775 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 555 · 2026-05-22T07:40:13.975968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_4/submitted.pdf",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_4/submitted.pdf",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 556 · 2026-05-22T07:40:14.581699+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_4/submitted.pdf (463.6KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 557 · 2026-05-22T07:41:09.711800+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_personfit_contam",
  "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_personfit_contam",
    "review_chat_id": "oc_6c76a266d9f5997de21a1604bc79c209"
  }
}
```

</details>

---


### Tool result

_source line 558 · 2026-05-22T07:41:33.465972+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23754
}
```

</details>

---


### Tool call

_source line 559 · 2026-05-22T07:41:33.616932+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性** 审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 via ACL Rolling Review\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页（ACL 双栏格式），参考文献无限制，Limitations 不计入页数\n- **匿名规则**：Double-blind\n- **评分标准**：ARR Overall Assessment (1-5 scale)：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文信息\n- **标题**：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n- **论文文件**：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex`\n- **PDF**：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **实验设计合理性**\n   - 控制污染实验的设计是否科学（QLoRA SFT 作为污染模型、clean/contaminated 对比）\n   - 样本量是否充分（n=10 seeds Qwen/Llama, n=6 Mistral）\n   - 实验矩阵的完整性（3 模型 × 2 benchmark × 3-4 污染水平——是否有重要条件缺失）\n   - 5%/15%/25%/50% 各污染条件的描述是否透明\n\n2. **统计方法学**\n   - Δℓz* 差分设计的合理性——能否有效消除 IRT 模型误设\n   - Cohen's d + bootstrap 95% CI 在小样本下的可靠性（特别是 Mistral n=6）\n   - BCa 与 percentile CI 的对比是否充分\n   - 每个污染条件只用单次训练运行（vs clean 的多 seed），这种设计的统计效力\n\n3. **IRT 框架有效性**\n   - 4PL 模型假设在 LLM 上的适用性（local independence, unidimensionality 违反的影响）\n   - PSN-IRT 预校准参数的循环依赖问题（校准样本可能包含被污染模型）\n   - θ-shift absorption 的机制性解释是否自洽\n   - Fixed-θ vs free-θ 估计的适用条件\n\n4. **可复现性**\n   - 实验细节是否足够复现（QLoRA 超参数、训练细节、评估流程）\n   - 代码和数据承诺（\"released upon acceptance\"）\n   - Reproducibility Statement 的充分性\n\n5. **Results 解读**\n   - Inverted-U dose-response 的证据强度（仅 Qwen 3 点，CI 是否重叠）\n   - Detection-diagnosis tradeoff 的论证逻辑\n   - Post-RL 观察（N=1）的定位是否恰当\n   - ARC-C ceiling effect 解释的说服力\n\n请按照 ARR 审稿标准，输出完整审稿报告，包含：Summary、Strengths、Weaknesses（区分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（含评分和置信度）。严格客观，不留情面。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性** 审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 via ACL Rolling Review\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页（ACL 双栏格式），参考文献无限制，Limitations 不计入页数\n- **匿名规则**：Double-blind\n- **评分标准**：ARR Overall Assessment (1-5 scale)：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文信息\n- **标题**：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n- **论文文件**：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex`\n- **PDF**：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **实验设计合理性**\n   - 控制污染实验的设计是否科学（QLoRA SFT 作为污染模型、clean/contaminated 对比）\n   - 样本量是否充分（n=10 seeds Qwen/Llama, n=6 Mistral）\n   - 实验矩阵的完整性（3 模型 × 2 benchmark × 3-4 污染水平——是否有重要条件缺失）\n   - 5%/15%/25%/50% 各污染条件的描述是否透明\n\n2. **统计方法学**\n   - Δℓz* 差分设计的合理性——能否有效消除 IRT 模型误设\n   - Cohen's d + bootstrap 95% CI 在小样本下的可靠性（特别是 Mistral n=6）\n   - BCa 与 percentile CI 的对比是否充分\n   - 每个污染条件只用单次训练运行（vs clean 的多 seed），这种设计的统计效力\n\n3. **IRT 框架有效性**\n   - 4PL 模型假设在 LLM 上的适用性（local independence, unidimensionality 违反的影响）\n   - PSN-IRT 预校准参数的循环依赖问题（校准样本可能包含被污染模型）\n   - θ-shift absorption 的机制性解释是否自洽\n   - Fixed-θ vs free-θ 估计的适用条件\n\n4. **可复现性**\n   - 实验细节是否足够复现（QLoRA 超参数、训练细节、评估流程）\n   - 代码和数据承诺（\"released upon acceptance\"）\n   - Reproducibility Statement 的充分性\n\n5. **Results 解读**\n   - Inverted-U dose-response 的证据强度（仅 Qwen 3 点，CI 是否重叠）\n   - Detection-diagnosis tradeoff 的论证逻辑\n   - Post-RL 观察（N=1）的定位是否恰当\n   - ARC-C ceiling effect 解释的说服力\n\n请按照 ARR 审稿标准，输出完整审稿报告，包含：Summary、Strengths、Weaknesses（区分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（含评分和置信度）。严格客观，不留情面。"
  }
}
```

</details>

---


### Tool result

_source line 560 · 2026-05-22T07:41:50.617510+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17000
}
```

</details>

---


### Tool call

_source line 561 · 2026-05-22T07:41:50.868842+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性/完整性** 审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 via ACL Rolling Review\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页（ACL 双栏格式），参考文献无限制，Limitations 不计入页数\n- **匿名规则**：Double-blind\n- **评分标准**：ARR Overall Assessment (1-5 scale)：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文信息\n- **标题**：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n- **论文文件**：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex`\n- **PDF**：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **Novelty 评估**\n   - 将 IRT person-fit 从教育测量迁移到 LLM 污染检测，其新颖性有多大？\n   - 三个 findings（θ-shift dynamics, detection-diagnosis tradeoff, non-monotonic dose-response）中，哪些是 IRT 理论可预测的（因此 novelty 有限），哪些是真正新的经验发现？\n   - 与现有检测方法（ConStat, MIA, generation-based probes）的区分度是否足够？\n   - \"characterization\" paper 在 NLP venue 的定位是否合适？\n\n2. **Framing 准确性**\n   - Abstract/Introduction 的 claim 是否与实际实验范围匹配？\n   - \"binary response patterns\" 的 minimal-information framing 是否准确？（论文依赖 PSN-IRT 4PL 参数）\n   - 标题暗示广泛的 \"benchmark contamination\"，实验仅 SFT-stage QLoRA——scope mismatch？\n   - Post-RL finding（N=1）在 Abstract/Intro 中的定位是否过度？\n\n3. **Related Work 完整性**\n   - Psychometrics 文献是否充分覆盖（person-fit, IRT 在 ML 中的应用）\n   - Contamination detection 领域的近期工作是否遗漏（特别是 2025-2026 年的）\n   - 是否有应引用但未引用的直接相关工作？\n\n4. **论文完整性**\n   - 实验覆盖是否足以支撑 claims（模型多样性、benchmark 多样性、规模多样性）\n   - 与 baseline methods 的对比是否充分（Table 3 的 detection-diagnosis 对比够不够？缺少与 ConStat 等的实证对比？）\n   - Limitations 是否诚实、完整、但不过长（EMNLP 要求 Limitations 简洁，~3 个点）\n   - Appendix 内容是否必要且信息丰富\n\n5. **写作质量**\n   - 论文结构是否清晰\n   - 数学符号是否一致\n   - Figure/Table 的呈现质量\n   - 是否有冗余或缺失的内容\n\n请按照 ARR 审稿标准，输出完整审稿报告，包含：Summary、Strengths、Weaknesses（区分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（含评分和置信度）。严格客观，不留情面。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性/完整性** 审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 via ACL Rolling Review\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页（ACL 双栏格式），参考文献无限制，Limitations 不计入页数\n- **匿名规则**：Double-blind\n- **评分标准**：ARR Overall Assessment (1-5 scale)：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文信息\n- **标题**：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n- **论文文件**：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex`\n- **PDF**：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **Novelty 评估**\n   - 将 IRT person-fit 从教育测量迁移到 LLM 污染检测，其新颖性有多大？\n   - 三个 findings（θ-shift dynamics, detection-diagnosis tradeoff, non-monotonic dose-response）中，哪些是 IRT 理论可预测的（因此 novelty 有限），哪些是真正新的经验发现？\n   - 与现有检测方法（ConStat, MIA, generation-based probes）的区分度是否足够？\n   - \"characterization\" paper 在 NLP venue 的定位是否合适？\n\n2. **Framing 准确性**\n   - Abstract/Introduction 的 claim 是否与实际实验范围匹配？\n   - \"binary response patterns\" 的 minimal-information framing 是否准确？（论文依赖 PSN-IRT 4PL 参数）\n   - 标题暗示广泛的 \"benchmark contamination\"，实验仅 SFT-stage QLoRA——scope mismatch？\n   - Post-RL finding（N=1）在 Abstract/Intro 中的定位是否过度？\n\n3. **Related Work 完整性**\n   - Psychometrics 文献是否充分覆盖（person-fit, IRT 在 ML 中的应用）\n   - Contamination detection 领域的近期工作是否遗漏（特别是 2025-2026 年的）\n   - 是否有应引用但未引用的直接相关工作？\n\n4. **论文完整性**\n   - 实验覆盖是否足以支撑 claims（模型多样性、benchmark 多样性、规模多样性）\n   - 与 baseline methods 的对比是否充分（Table 3 的 detection-diagnosis 对比够不够？缺少与 ConStat 等的实证对比？）\n   - Limitations 是否诚实、完整、但不过长（EMNLP 要求 Limitations 简洁，~3 个点）\n   - Appendix 内容是否必要且信息丰富\n\n5. **写作质量**\n   - 论文结构是否清晰\n   - 数学符号是否一致\n   - Figure/Table 的呈现质量\n   - 是否有冗余或缺失的内容\n\n请按照 ARR 审稿标准，输出完整审稿报告，包含：Summary、Strengths、Weaknesses（区分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（含评分和置信度）。严格客观，不留情面。"
  }
}
```

</details>

---


### Tool result

_source line 562 · 2026-05-22T07:41:52.536788+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1667
}
```

</details>

---


### Assistant

_source line 563 · 2026-05-22T07:42:05.760935+00:00_

Round 1 已启动：
- 视觉审查 Agent：已派发（fire-and-forget）
- Reviewer 1（方法严谨性）：已分配
- Reviewer 2（新颖性/完整性）：已分配

等待两名 Reviewer 返回独立审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 53

## Round 53

2 recorded events


### User

_source line 564 · 2026-05-22T07:47:44.959719+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：Novelty / Completeness

**论文**：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization
**Venue**：EMNLP 2026 via ACL Rolling Review

---

## 总体评分
**Overall**: 3.0 (Findings)
**Confidence**: 4/5
**一句话总结**: 方法论上严谨的 characterization 研究，但核心发现大部分可从 IRT 理论预测，novelty 有限；实验范围窄（3 个 7-8B 模型、1 种污染机制），且缺少与现有检测方法的实证对比。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | DiD 设计合理，统计分析严谨（bootstrap CI, Cohen's d, 鲁棒性分析充分），但实验范围窄、Post-RL 仅 N=1、缺少与竞争方法的实证对比 |
| Excitement | 2.5/5 | 将 person-fit 迁移到 LLM 污染检测是 incremental transfer，三个 findings 中两个（θ-shift 天花板效应、detection-diagnosis tradeoff）可从 IRT 理论直接预测 |
| Reproducibility | 4/5 | 承诺开源代码和数据，PSN-IRT item bank 公开可用，实验细节充分（Appendix A-H），种子敏感性分析完善 |
| Overall Assessment | 3.0/5 | 技术上 sound 的 Findings 级别论文，缺乏主会议所需的 novelty 或 impact |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Novelty 有限：三个核心 findings 大部分可从 IRT 理论预测

- 具体位置：Section 4.1-4.4, Abstract
- 问题：
  - **Finding 1（θ-shift dynamics, §4.2）**：高能力模型的 θ-shift 吸收效应本质上是 IRT 能力估计的天花板效应（ceiling effect）。当模型已经接近答对所有题目时，污染带来的信号被 θ 吸收，这在 IRT 文献中是 well-known 的性质（参见 Embretson & Reise, 2000 关于信息函数在极端 θ 处递减的论述）。论文将其描述为 empirical finding，但更准确地说这是 IRT 理论的直接推论。
  - **Finding 2（detection-diagnosis tradeoff, §4.3）**：简单统计量（accuracy z-score）检测力强于复杂统计量（l_z^*），但后者提供更丰富的诊断信息——这是统计学中 power vs. richness 的经典权衡，不构成新发现。
  - **Finding 3（non-monotonic dose-response, §4.4）**：在 free-θ 估计下的非单调关系是 Finding 1（θ-shift absorption）的直接推论——当 θ 自由估计时，高污染水平导致 θ 大幅上升，从而"吸收"掉 l_z^* 的异常信号。论文自身在 §4.2 已经建立了这一机制。
  - 唯一真正具有经验价值的发现是定量层面的：具体到哪些模型/benchmark/污染水平组合下，person-fit 统计量的 effect size 达到可用水平。但这属于 "useful calibration" 而非 "new insight"。
- 为什么影响接收：NLP 主会议对 novelty 的要求是 "exciting / field-changing"（ARR 4-5 分）。将已知理论工具应用于新领域并确认其行为符合理论预期，novelty 不足以支撑主会议接收。
- 建议修改方向：(1) 明确定位为 "empirical validation and calibration" 而非 "first characterization"，降低 novelty claim；(2) 增加 IRT 理论无法预测的经验发现（例如，跨 benchmark/跨规模的定量交互效应）；(3) 或将重心转向提出可操作的检测 pipeline（而非纯 characterization）。

**N2** [critical] 缺少与现有检测方法的实证对比

- 具体位置：Table 3 (§4.3), Section 5 (Discussion, p.8)
- 问题：Table 3 仅在论文自身框架内对比 l_z^*、HT、accuracy 三个统计量，但完全没有与已有的专用污染检测方法进行实证对比。论文在 Discussion (p.8) 承认 "Direct comparison with ConStat (Dekoninck et al., 2024) is complicated by different information requirements"，但这一理由不充分——ConStat 同样基于性能数据，信息需求并非根本不兼容。此外，MIA-based 方法（Shi et al., 2024）虽然需要 logits，但论文的 experimental setup 完全可以获取 logits（QLoRA 微调意味着有 model access）。
- 为什么影响接收：一篇声称 characterize contamination detection 的论文，不与任何现有检测方法做头对头比较，使得读者无法判断 IRT person-fit 在实际应用中的价值。"Detection-diagnosis tradeoff" 的 claim 在没有与真正的 competing methods 对比的情况下是 incomplete 的。
- 建议修改方向：至少在 MMLU 上运行 ConStat 和一种 MIA-based 方法，展示它们与 l_z^* 在 detection power 和 diagnostic capability 上的实际差异。

**N3** [critical] 标题和 framing 存在 scope mismatch

- 具体位置：Title, Abstract, §1 Introduction
- 问题：
  - **"Binary response patterns"** 的 framing 暗示方法仅需最小信息（正确/错误二值模式），但实际上方法关键依赖于 PSN-IRT 的预校准 4PL item parameters（来自 13,000+ 模型的大规模 item bank）。没有这些外部参数，l_z^* 无法计算。这不是 "binary response patterns reveal"，而是 "binary response patterns + externally calibrated item parameters reveal"。
  - **"Benchmark Contamination"** 标题暗示广泛适用性，但实验仅覆盖 SFT-stage QLoRA 污染。Pre-training contamination、in-context learning contamination、full fine-tuning contamination 均未涉及。标题应更准确地反映实际范围。
  - Abstract 第一段 "the framework requires only binary response patterns from the target model—no access to weights, gradients, logits, or training data" 技术上正确但具有误导性——省略了对外部 item bank 的核心依赖。
- 为什么影响接收：审稿人和读者会基于标题和 abstract 形成对论文范围的预期。当实际内容远窄于预期时，造成 overclaiming 的印象。
- 建议修改方向：(1) 标题改为类似 "An IRT Person-Fit Characterization of SFT-Stage Benchmark Contamination"；(2) Abstract 明确提及对 pre-calibrated item parameters 的依赖；(3) 或在 Introduction 首段即明确界定 "binary response patterns" 不等于 "zero external information"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 实验规模/多样性不足以支撑 generalization claims

- 具体位置：§3.3, Table 1, §6 Conclusion
- 问题：
  - **模型多样性**：仅 3 个模型家族，全部为 7-8B 规模。无 1-3B（小模型可能有不同的 θ-shift 特征）、无 13B+（规模效应未探索）、无 MoE 架构。Conclusion (p.8) 说 "across broader model scales" 是 future work，但这意味着当前 claims 的外部有效性存疑。
  - **Benchmark 多样性**：仅 MMLU（14,042 items）和 ARC-Challenge（295 items）。ARC-C 的 295 items 导致 l_z^* 统计量的功效显著下降（论文自身在 Appendix A 承认 n>7,000 items 才能达到 80% power at 15% contamination），使得该 benchmark 上的结论统计基础薄弱。
  - **污染机制**：仅 QLoRA（rank=16, r=32）。Full fine-tuning、continued pre-training、data mixing 均未测试。论文的 Limitations 部分承认 "scoped to SFT-based contamination"，但 Section 1 和 Abstract 的 framing 未充分体现这一限制。
- 建议：增加至少 1 个不同规模的模型（如 1-3B 或 13B+）和 1 种不同污染机制，或者大幅弱化 generalization claims。

**W2** [warning] Post-RL 分析（§4.5）证据不足但获得过多篇幅

- 具体位置：§4.5, Figure 4, Abstract
- 问题：Post-RL 扩展仅使用 N=1 模型（Qwen only）、1 个 benchmark（MMLU）、1 个污染水平（15%），且明确声明 "no statistical inference is drawn"。然而这一结果获得了一个完整的 subsection（§4.5）和一个占据 1/4 页的 Figure（Figure 4）。在主文空间有限的 8 页论文中，将 ~0.5 页用于无法做统计推断的 N=1 观察是 space allocation 问题。
- 建议：将 §4.5 和 Figure 4 移入 Appendix，在主文中仅用 1-2 句话提及 "preliminary observation suggests..."。或者增加更多模型/benchmark 的 post-RL 实验使其有统计基础。

**W3** [warning] Related Work 缺少污染检测领域的综述性引用

- 具体位置：§2 Related Work
- 问题：2024-2025 年已有多篇全面的 LLM 污染检测 survey（如 "A Survey on Data Contamination for Large Language Models" [2025], EMNLP 2025 的 "Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation"），但论文未引用任何 survey。对于一篇 characterization 论文，指向 survey 可以帮助读者建立完整的方法论图谱，也能更好地定位本文在检测方法谱系中的位置。
- 建议：在 §2 引用 1-2 篇近期 survey，简要说明 person-fit 方法在检测方法分类学中的位置。

**W4** [warning] Fixed-θ vs. free-θ 选择缺少实用指导

- 具体位置：§4.2, §4.4
- 问题：论文展示了 fixed-θ 消除 inverted-U 的效果（§4.2 末段），free-θ 产生非单调 dose-response（§4.4），但对实际使用者来说，在不知道真实污染水平的情况下，应该用哪种估计方法？论文没有提供明确的 decision rule 或推荐。这对 characterization 论文来说是一个实用性缺口。
- 建议：添加一段讨论或 decision flowchart，指导实践者在不同场景下的 θ 估计策略选择。

---

## 小问题（不影响接收）

- §3.2 DiD 设计的表述 "shared model misfit cancels" 在数学上假设 contamination 对 item-level fit 的影响是 additive 的。如果污染引入的是 multiplicative 或 interaction 效应，DiD 的有效性可能受影响。可考虑简短讨论这一假设。
- Figure 1 caption 可以更清楚地标注 clean vs. contaminated 的视觉编码（目前依赖文字描述，color-blind reader 可能难以区分）。
- Table 1 的 "All CIs exclude 0" 脚注与某些 ARC-C conditions（如 Mistral 15% 的较小 effect sizes）之间的关系可以更明确说明。
- Appendix H（MML-EM vs PSN-IRT）是一个重要的技术贡献，说明了为什么需要外部 item bank。考虑在主文 §3.1 简短提及这一发现。
- §2 "Person-fit statistics in psychometrics" 段落引用了 Karabatsos (2003) 对 36 种 person-fit 统计量的比较，但未解释为什么选择 l_z^* 而非其他统计量（如 U3, W, Ht）。简短的 justification 会增强方法选择的说服力。

---

## Questions to Authors

1. 如果不使用 PSN-IRT item bank，而是用 classical MML-EM 估计的 item parameters（如 Appendix H 所示），l_z^* 的 detection power 会下降多少？这决定了方法对外部资源的依赖程度。
2. 论文的 DiD 设计假设 clean baseline 之间的 model-benchmark 交互效应在不同 seeds 间是稳定的。Table 5 的 seed sensitivity 分析是否支持这一假设？跨 seed 的 ICC（intraclass correlation）是多少？
3. ConStat 的实证对比真的 "complicated" 到无法执行吗？ConStat 需要 reference benchmark，而你们已有 ARC-C 和 MMLU 两个 benchmark——这似乎满足了 ConStat 的最低信息需求。
4. 对于 ARC-Challenge 这种小规模 benchmark（295 items），论文承认 power 不足。那么论文的 claim "reliably detects SFT-stage contamination across three model families" 中的 "across" 是否应该仅限于 MMLU？

---

## Missing References

- **Contamination surveys**：Li, Y. et al. (2025). "A Survey on Data Contamination for Large Language Models." arXiv:2502.14425; Xu et al. (2025). "Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation." EMNLP 2025.
- **Contamination detection meta-analysis**：Dong et al. (2024). "Does Data Contamination Detection Work (Well) for LLMs? A Survey and Evaluation on Detection Assumptions." arXiv:2410.18966. 这篇对检测方法的假设做了系统评估，与本文的 characterization 目标直接相关。

---

## 主要优势

- **实验设计严谨**：DiD（difference-in-differences）设计是 causal inference 的标准方法，在此场景下运用得当。共享基线消除了 model-benchmark 交互的混淆变量。
- **统计分析充分**：Bootstrap CIs、Cohen's d effect sizes、seed sensitivity analysis（Appendix C）、cross-family consistency check（Appendix D）、power analysis（Appendix A）、robustness to local dependence（Appendix F）构成了一套完整的 robustness analysis 体系。
- **诚实的 Limitations**：Limitations 部分（~3 个点）简洁且涵盖了最重要的限制（模型规模、SFT scope、PSN-IRT 依赖），符合 EMNLP 要求。
- **Appendix H 的 item bank 对比**：证明了 classical MML-EM 估计无法替代 PSN-IRT 的预校准参数，这是一个重要的方法论贡献，增强了对 item parameter calibration 的理解。
- **清晰的写作**：论文结构合理，数学符号一致，Figure/Table 呈现质量高。

---

## 格式合规检查

- **页数**：主文 8 页（pp.1-8），符合 EMNLP 2026 long paper 限制 ✓
- **Limitations**：单独章节，~3 个点，不计入页数 ✓
- **匿名**：未发现去匿名化信息 ✓
- **参考文献**：格式一致，无明显缺失（除上述 survey 外）✓
- **Reproducibility Statement**：存在（p.9），承诺开源 ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 565 · 2026-05-22T07:47:52.286703+00:00_

Reviewer 2 报告已收到（Overall: 3.0 Findings）。等待 Reviewer 1 完成初审后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 54

## Round 54

2 recorded events


### User

_source line 566 · 2026-05-22T07:48:08.675180+00:00_

[Reviewer 2 审稿结果]:
Reviewer 2 审稿完成。

**Overall: 3.0 (Findings)**，置信度 4/5。

核心判断：技术执行严谨（DiD 设计、bootstrap CIs、8 个 Appendix 的鲁棒性分析），但三个 Must-Fix 问题制约了评分：

1. **Novelty 有限** — 三个核心 findings（θ-shift ceiling、detection-diagnosis tradeoff、non-monotonic dose-response）大部分可从 IRT 理论直接预测，经验贡献主要在定量校准层面
2. **缺少与现有方法的实证对比** — 未与 ConStat/MIA 做头对头比较，"detection-diagnosis tradeoff" 的 claim 不完整
3. **Title/framing scope mismatch** — "binary response patterns" 掩盖了对 PSN-IRT 外部 item bank 的核心依赖；"benchmark contamination" 标题远宽于 SFT-stage QLoRA 的实际实验范围

报告已提交至 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 567 · 2026-05-22T07:48:16.397550+00:00_

Reviewer 2 审稿已收到（3.0 Findings）。等待 Reviewer 1 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 55

## Round 55

6 recorded events


### User

_source line 568 · 2026-05-22T07:49:13.083962+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性审查

**论文标题**：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization

---

## Paper Summary

本文首次将心理测量学中的 IRT person-fit 统计量（ℓ_z*）系统性地应用于 LLM 基准污染检测。核心思路是：被污染的 LLM 类似于拥有题目预知的考生，会在难题上产生异常正确的作答模式，可被 person-fit 统计量捕获。作者提出 Δℓ_z*（差分设计）消除 IRT 模型误设影响，在 3 个 7-8B 模型族（Qwen2.5-7B、Llama-3.1-8B、Mistral-7B）× 2 个基准（MMLU、ARC-C）× 3 个污染水平（15%/25%/50%）上进行了控制实验。主要发现三个行为边界：(1) 模型特异的 θ-shift absorption；(2) detection-diagnosis tradeoff（简单统计量检测更强，ℓ_z* 诊断更强）；(3) 能力依赖的非单调剂量-效应。

---

## 总体评分

**Overall Assessment**: 3.5 / 5（Borderline Conference）

**一句话总结**：新颖的跨学科视角和扎实的机制分析，但单次污染运行的实验设计和事后扩展的实验矩阵显著削弱了定量结论的可靠性。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.0 / 5 | 核心检测 claim 有支撑（所有 bootstrap CI 排除零），但每个污染条件仅单次运行（n=1）严重限制了 Cohen's d 的统计解释力；实验矩阵事后扩展（先看到 inverted-U 再补 25% 条件）构成循环论证风险；摘要中 "n=10 independent seeds per condition" 措辞具有误导性 |
| **Excitement** | 3.5 / 5 | 首次将心理测量 person-fit 理论引入 NLP 污染检测，θ-shift absorption 机制和 detection-diagnosis tradeoff 均为有洞察力的发现；但论文自身承认简单统计量检测效果更优，削弱了实际应用价值 |
| **Reproducibility** | 3.0 / 5 | 代码和数据承诺 "released upon acceptance"，QLoRA 超参数有交代（rank=16, α=32），但训练 epoch 数、学习率、数据混合细节不够充分；PSN-IRT item bank 为外部依赖 |
| **Reviewer Confidence** | 4 / 5 | 本人熟悉 IRT/心理测量方法论和 LLM 评估领域，对统计方法学和实验设计的评估有较高把握 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 每个污染条件仅单次运行，Cohen's d 统计解释受限

- 具体位置：Section 3.3（method.tex L48-49）："each contaminated model is a single QLoRA run"
- 问题：每个污染水平（15%/25%/50%）仅训练了 ONE 个模型，所有方差估计均来自 clean seeds（n=10 或 n=6）。由此计算的 Cohen's d 本质上是单个观测值相对于参考分布的 z-score，而非两个分布间的标准化均差。QLoRA 微调具有随机性（初始化、数据顺序），不同 seed 可能产生不同的污染模式和 ℓ_z* 值。当前设计无法：(a) 估计污染效果的方差；(b) 判断观测到的 ℓ_z* shift 是否具有代表性；(c) 正确计算需要两组方差的 Cohen's d。这直接影响所有定量比较——包括 Table 1 的 effect size、cross-model 比较、以及 inverted-U 的幅度。
- 为什么影响接收：论文的三个核心 contribution 中，contribution (2)（Δℓ_z* reliably detects）和 (3)（detection-diagnosis tradeoff）的定量证据均建立在这些单次运行的 effect size 上。如果使用不同 seed 训练污染模型，Qwen 50% 的 |d|=1.90 可能变为 3.0 或 0.5，整个 inverted-U 叙事可能不成立。
- 建议修改方向：至少为关键条件（如 Qwen 15%/50% on MMLU）训练 3-5 个污染 seed，报告污染效果的 seed-level 方差。若计算资源不允许，应在正文中明确标注 Cohen's d 为 "single-observation effect size"，并讨论这一限制对结论的影响。

**N2** [critical] 摘要中 "n=10 independent seeds per condition" 措辞具有误导性

- 具体位置：Abstract（abstract.tex L4）
- 问题：摘要写道 "n=10 independent seeds per condition; n=6 for Mistral"，自然阅读理解为每个实验条件（clean/15%/25%/50%）均有 10 个 seed。但 Section 3.3 明确说明 "We train n=10 clean seeds" 且 "each contaminated model is a single QLoRA run"。实际上只有 clean 条件有多 seed，所有污染条件均为 n=1。这构成对读者（和 AC）的误导，夸大了研究的统计功效。
- 为什么影响接收：摘要的准确性是论文可信度的基础。审稿人和 AC 可能基于摘要形成初始印象。如果 "n=10 per condition" 被理解为每条件 10 个独立运行，这与实际情况严重不符。
- 建议修改方向：改为 "n=10 clean baseline seeds per model family (n=6 for Mistral); single contaminated run per condition"，准确反映实验设计。

**N3** [critical] 实验矩阵事后扩展构成循环论证风险

- 具体位置：Section 3.3（method.tex L46-47）："Following initial observation of non-monotonic dose-response for Qwen, we added a 25% contamination condition."
- 问题：实验设计是迭代的而非预注册的：先观察到 Qwen 15% > 50% 的非单调性，再添加 25% 条件以 "确认" inverted-U。这是典型的假设确认式数据收集（hypothesis-confirming data collection）。论文将 inverted-U 作为核心发现之一（contribution 3），但确认该发现的数据点（25%）是在看到初始结果后才添加的。此外，25% 条件仅扩展到 Llama（未覆盖 Mistral），进一步限制了跨模型验证的完整性。
- 为什么影响接收：Inverted-U 是论文三个核心发现之一。如果其证据基于事后选择的数据点，且无独立验证（如 held-out 模型族），该发现的置信度大幅降低。Simulation（Appendix A）虽提供了机制预测，但模拟参数可能也受到实证结果的影响。
- 建议修改方向：(a) 明确标注 25% 条件是事后添加的（当前已做到，但应讨论其对统计推断的影响）；(b) 理想情况下，在 Mistral 上验证 25% 条件；(c) 或者将 inverted-U 定位为 "exploratory finding requiring prospective confirmation" 而非已确立的 "behavior boundary"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 无低污染水平（<15%）的实证实验

- 具体位置：Section 3.3 实验设计，Table 1
- 问题：经验实验的最低污染水平为 15%，这在实际场景中已属相当高的污染率。模拟（Appendix B, Table 4）覆盖了 5%，但 5% 时 MMLU 检测功率仅 47.6%（4PL），ARC-C 仅 5.7%。论文未在实证数据上验证低污染场景的检测能力，而这恰恰是实践中最需要的场景。
- 建议：至少在一个模型族上测试 5% 污染条件，或在 Discussion 中更显著地讨论低污染检测的局限性。

**W2** [warning] ARC-Challenge 实验仅限 Qwen，跨基准泛化证据不足

- 具体位置：Section 3.3（method.tex L54）："ARC-Challenge experiments were conducted on Qwen only"
- 问题：ARC-C（295 items）是论文唯一的小基准测试，且仅在 Qwen 上测试。论文从中得出关于 ceiling effect 和跨基准泛化性的结论（Section 4.1 L57-64），但 n=1 模型族无法支撑泛化性声称。此外，ARC-C 的模拟检测功率极低（5% 污染时仅 5.7%，15% 时 8.7%，Table 4），质疑了该基准上 person-fit 方法的实用性。
- 建议：(a) 弱化关于 ARC-C ceiling effect 的泛化性声称；(b) 在 Limitations 中明确讨论小基准的功率限制。

**W3** [warning] Fixed-θ 在 15% 污染时反而比 free-θ 更差（Qwen），缺乏充分解释

- 具体位置：Table 2（results.tex L84）：Qwen 15% free-θ |d|=6.58, fixed-θ |d|=4.77, ratio=0.7×
- 问题：论文的核心机制叙事是 "θ-shift absorption 削弱检测 → fixed-θ 可恢复信号"。但 Table 2 显示 Qwen 在 15% 污染时 fixed-θ 效果反而更差（0.7×）。这与 50% 时的 7.6× 改善形成强烈对比。论文未充分解释这一反转：为什么在低污染时 free-θ 反而更优？如果 θ-shift absorption 是一般性机制，它应该在所有污染水平上都使 free-θ 劣于 fixed-θ（只是程度不同）。
- 建议：提供 15% 时 free-θ 优于 fixed-θ 的定量解释。可能的原因包括：(a) Snijders correction 在 free-θ 下减少了方差（但这应对检测有利，不应导致 d 更大）；(b) 小幅 θ-shift 实际上增加了某些 item 上异常模式的可检测性。无论原因如何，当前的叙事过于简化。

**W4** [warning] Post-RL 观察（N=1）占据过大篇幅

- 具体位置：Section 5 Discussion（discussion.tex L22-25），Figure 4
- 问题：Post-RL 实验仅使用 Qwen 一个模型、15% 一个污染水平、GRPO 一种 RL 方法。这是一个 anecdote，而非实验证据。但它在 Discussion 中获得了完整段落和一个 Figure 的空间，且在 Abstract（L8）中也被提及。对于一个 N=1 观察，这一比重过高。
- 建议：将 Post-RL 内容移至 Appendix，正文用一句话提及即可。这样释放的空间可用于更重要的分析（如额外污染水平或模型族）。

**W5** [warning] QLoRA 训练细节不足以复现

- 具体位置：Section 3.3（method.tex L45）
- 问题：论文报告了 QLoRA rank=16, α=32，但缺少以下关键超参数：学习率、训练 epoch 数、batch size、warmup 策略、数据混合比例的精确构造方式（benchmark items 如何与非污染数据混合？ Interleaved? Appended?）、序列长度、以及如何处理多选题格式（将 ABCD 选项编码为 SFT 目标的具体方式）。Reproducibility Statement（main.tex L42-45）仅提及 "Code and response data will be released upon acceptance"，对于当前阶段的审稿不构成可复现性保证。
- 建议：在 Appendix 中添加完整的训练配置表，包括所有超参数和数据预处理细节。

**W6** [warning] Cohen's d 的 bootstrap CI 在小样本下的可靠性

- 具体位置：Section 3.2（method.tex L34），Mistral 条件（n=6）
- 问题：对于 Mistral（n=6 seeds），bootstrap resampling from 6 values 产生的 CI 分布非常粗糙（仅 6^6 = 46,656 种可能的重采样组合，远少于 10,000 次 resampling 中的有效独立样本）。BCa 校正（Appendix G）确认 percentile CI 是保守的，但 BCa 本身在 n=6 时也未必可靠。Table 1 中 Mistral 的 CI 确实极宽（如 [-9.6, -2.1]），但论文未讨论这一宽度是否足以支撑有意义的推断。
- 建议：对 Mistral 结果添加关于小样本 bootstrap 局限性的显式讨论；考虑报告 permutation test p-value 作为补充。

---

## 小问题（不影响接收）

- Section 3.2 将 Δℓ_z* 设计称为 "difference-in-differences (DiD)"（method.tex L25），但标准 DiD 设计需要时间维度上的前后对比。此处更准确的描述是 "matched-difference design" 或 "simple differencing"。
- Table 1 的列标题为 "d (15%) [CI]" 等，但 CI 的具体含义（percentile bootstrap, 10,000 resamples）需要在表注中说明（当前仅在 caption 中提及 bootstrap，未说明 percentile vs BCa）。
- Figure 2 的色标（蓝色强度）仅凭 heatmap 难以精确读数，建议在每个 cell 内标注 |d| 值和 CI（当前似乎已做到，但 PDF 分辨率下难以确认）。
- Limitations section 应增加对 "无低污染实验" 和 "单次污染运行" 的显式讨论——当前 Limitations 列举了模型规模和 SFT-scope 限制，但未提及这两个更基础的设计限制。

---

## Questions to Authors

1. 如果为 Qwen 15% 和 50% 各训练 5 个不同 seed 的污染模型，你预期 ℓ_z* 的 seed-level 方差会有多大？你是否有任何 pilot 数据（如两个 seed 的比较）来估计污染效果的可重复性？

2. 25% 条件是在观察到 inverted-U 后添加的。是否考虑过在一个 held-out 模型族（如 Phi-3、Gemma）上进行前瞻性验证？

3. Table 2 中 Qwen 15% 的 fixed-θ 比 free-θ 更差（ratio=0.7×），能否提供更精确的定量解释？特别是，Snijders correction 在此处的具体影响是什么？

4. PSN-IRT 的校准样本（13,000+ 模型）中，估计有多大比例的模型可能存在不同程度的基准污染？Appendix F.2 的 ±10% 随机噪声分析是否能模拟系统性污染偏差？

5. Abstract 中 "n=10 independent seeds per condition" 具体指什么？如果指 "per model family's clean condition"，建议修改措辞以避免歧义。

---

## Missing References

- **Polo et al. (2024)** 在 related work (Section 2, p3) 中被引用用于 IRT-based item selection，但论文未与之进行方法论层面的对比（Polo 用 IRT 选 item，本文用 IRT person-fit 检测污染——角度不同但框架共享，值得讨论）。
- 论文未引用 **Sinharay & Johnson (2017)** "Measures of agreement: reliability, classification accuracy, and classification consistency" 或相关的 IRT person-fit 功效分析文献，这些可为 "多少 item 足够检测" 的 benchmark size boundary 提供理论支撑。
- 缺少与 **EMNLP 2024/2025 年相关 contamination 工作**（如 benchmark leakage detection via perplexity-based methods）的系统对比。

---

## 主要优势

1. **新颖的跨学科桥接**：首次将教育测量学 person-fit 理论系统性引入 NLP 污染检测，类比关系（污染 LLM ↔ 作弊考生）自然且有启发性。

2. **诚实的定位**：论文明确将自身定位为 "characterization"（行为边界刻画）而非 "tool"（现成工具），并坦承简单统计量在纯检测任务上表现更优。这种学术诚实值得肯定。

3. **Δℓ_z* 差分设计**：优雅地解决了绝对 ℓ_z* 阈值在 LLM 上无效的问题（57/60 cells 被标记为异常）。LD simulation（Appendix F.1）提供了合理的鲁棒性证据。

4. **θ-shift absorption 机制分析**：对 "为什么高能力模型检测信号更弱" 的机制解释清晰、有说服力，fixed-θ vs free-θ 对比（Table 2）提供了强支撑证据。

5. **Detection-diagnosis tradeoff**：这一发现对实践有直接指导意义——先用 accuracy z-score 筛选，再用 ℓ_z* 诊断机制。

6. **详尽的 Appendix**：包含 LD 模拟、参数噪声敏感性、BCa 对比、4PL vs 3PL 消融、classical IRT refit、seed sensitivity 等 8 个补充分析，展现了方法论上的严谨态度。

---

## 总结性评价

本文在 NLP-psychometrics 交叉领域做出了有意义的探索，三个行为边界的发现（θ-shift dynamics、detection-diagnosis tradeoff、non-monotonic dose-response）为理解基准污染的统计特征提供了新视角。机制分析（特别是 θ-shift absorption）清晰有力，Appendix 中的鲁棒性分析展现了作者的方法论功底。

然而，实验设计存在两个根本性问题：(1) 每个污染条件仅单次运行，无法估计污染效果的可重复性；(2) 实验矩阵事后扩展，inverted-U 的证据存在循环论证风险。这些问题不是通过修改文字可以解决的——需要额外实验（至少为关键条件增加多个污染 seed）。摘要中的 "n=10 per condition" 措辞需要立即修正。

如果作者能补充关键条件的多 seed 污染实验并修正统计报告，本文有望达到 Conference 水平。当前版本更适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 569 · 2026-05-22T07:50:10.235118+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿报告\n\n**Overall Assessment**: 3.5 / 5（Borderline Conference），置信度 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 每个污染条件仅单次运行，Cohen's d 统计解释受限\n- Section 3.3：\"each contaminated model is a single QLoRA run\"\n- 所有方差估计均来自 clean seeds（n=10 或 n=6），Cohen's d 本质上是单个观测值相对于参考分布的 z-score，而非两个分布间的标准化均差\n- QLoRA 微调具有随机性，不同 seed 可能产生不同的污染模式和 ℓ_z* 值\n- 当前设计无法估计污染效果的方差、判断 ℓ_z* shift 的代表性、正确计算 Cohen's d\n- 影响所有定量比较——Table 1 effect size、cross-model 比较、inverted-U 幅度\n\n**N2** [critical] 摘要中 \"n=10 independent seeds per condition\" 措辞具有误导性\n- Abstract 写 \"n=10 independent seeds per condition; n=6 for Mistral\"，自然理解为每个条件均有 10 个 seed\n- 但实际仅 clean 条件有多 seed，所有污染条件均为 n=1\n- 构成对读者和 AC 的误导，夸大统计功效\n\n**N3** [critical] 实验矩阵事后扩展构成循环论证风险\n- §3.3：\"Following initial observation of non-monotonic dose-response for Qwen, we added a 25% contamination condition.\"\n- 先观察到非单调性再补数据确认——hypothesis-confirming data collection\n- Inverted-U 是核心发现之一，但确认数据点是事后添加的\n- 25% 仅扩展到 Llama，未覆盖 Mistral\n\n### Should-Fix 问题\n\n**W1** 无低污染水平（<15%）的实证实验——模拟显示 5% 时 MMLU 功率仅 47.6%\n**W2** ARC-C 仅限 Qwen，跨基准泛化证据不足\n**W3** Fixed-θ 在 15% 时反而比 free-θ 更差（Qwen ratio=0.7×），缺乏充分解释\n**W4** Post-RL 观察（N=1）占据过大篇幅\n**W5** QLoRA 训练细节不足以复现（缺 LR、epoch、batch size、数据混合方式等）\n**W6** Mistral n=6 的 bootstrap CI 可靠性问题\n\n### 主要优势\n1. 新颖的跨学科桥接（person-fit → 污染检测）\n2. 诚实定位为 characterization 而非 tool\n3. Δℓ_z* 差分设计优雅解决绝对阈值失效问题\n4. θ-shift absorption 机制分析清晰有说服力\n5. Detection-diagnosis tradeoff 有实践指导意义\n6. 8 个 Appendix 展现方法论严谨态度\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 问题逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿报告\n\n**Overall Assessment**: 3.5 / 5（Borderline Conference），置信度 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 每个污染条件仅单次运行，Cohen's d 统计解释受限\n- Section 3.3：\"each contaminated model is a single QLoRA run\"\n- 所有方差估计均来自 clean seeds（n=10 或 n=6），Cohen's d 本质上是单个观测值相对于参考分布的 z-score，而非两个分布间的标准化均差\n- QLoRA 微调具有随机性，不同 seed 可能产生不同的污染模式和 ℓ_z* 值\n- 当前设计无法估计污染效果的方差、判断 ℓ_z* shift 的代表性、正确计算 Cohen's d\n- 影响所有定量比较——Table 1 effect size、cross-model 比较、inverted-U 幅度\n\n**N2** [critical] 摘要中 \"n=10 independent seeds per condition\" 措辞具有误导性\n- Abstract 写 \"n=10 independent seeds per condition; n=6 for Mistral\"，自然理解为每个条件均有 10 个 seed\n- 但实际仅 clean 条件有多 seed，所有污染条件均为 n=1\n- 构成对读者和 AC 的误导，夸大统计功效\n\n**N3** [critical] 实验矩阵事后扩展构成循环论证风险\n- §3.3：\"Following initial observation of non-monotonic dose-response for Qwen, we added a 25% contamination condition.\"\n- 先观察到非单调性再补数据确认——hypothesis-confirming data collection\n- Inverted-U 是核心发现之一，但确认数据点是事后添加的\n- 25% 仅扩展到 Llama，未覆盖 Mistral\n\n### Should-Fix 问题\n\n**W1** 无低污染水平（<15%）的实证实验——模拟显示 5% 时 MMLU 功率仅 47.6%\n**W2** ARC-C 仅限 Qwen，跨基准泛化证据不足\n**W3** Fixed-θ 在 15% 时反而比 free-θ 更差（Qwen ratio=0.7×），缺乏充分解释\n**W4** Post-RL 观察（N=1）占据过大篇幅\n**W5** QLoRA 训练细节不足以复现（缺 LR、epoch、batch size、数据混合方式等）\n**W6** Mistral n=6 的 bootstrap CI 可靠性问题\n\n### 主要优势\n1. 新颖的跨学科桥接（person-fit → 污染检测）\n2. 诚实定位为 characterization 而非 tool\n3. Δℓ_z* 差分设计优雅解决绝对阈值失效问题\n4. θ-shift absorption 机制分析清晰有说服力\n5. Detection-diagnosis tradeoff 有实践指导意义\n6. 8 个 Appendix 展现方法论严谨态度\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 问题逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 570 · 2026-05-22T07:50:30.371522+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20136
}
```

</details>

---


### Tool call

_source line 571 · 2026-05-22T07:50:30.473629+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿报告\n\n**Overall Assessment**: 3.0 / 5（Findings），置信度 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] Novelty 有限：三个核心 findings 大部分可从 IRT 理论预测\n- Finding 1（θ-shift dynamics）：高能力模型的 θ-shift 吸收本质是 IRT 能力估计的天花板效应，IRT 文献中 well-known\n- Finding 2（detection-diagnosis tradeoff）：power vs. richness 的经典权衡，不构成新发现\n- Finding 3（non-monotonic dose-response）：是 Finding 1 的直接推论\n- 唯一经验价值在定量校准层面——\"useful calibration\" 而非 \"new insight\"\n\n**N2** [critical] 缺少与现有检测方法的实证对比\n- Table 3 仅在自身框架内对比 ℓ_z*、HT、accuracy，未与 ConStat/MIA 做头对头比较\n- Discussion 说 ConStat 对比 \"complicated by different information requirements\"——理由不充分\n- 实验设置可获取 logits（QLoRA → model access），MIA 方法可运行\n- 无法判断 IRT person-fit 在实际应用中的价值\n\n**N3** [critical] 标题和 framing 存在 scope mismatch\n- \"Binary response patterns\" 掩盖了对 PSN-IRT 外部 item bank 的核心依赖\n- \"Benchmark Contamination\" 标题远宽于 SFT-stage QLoRA 实验\n- Abstract \"only binary response patterns...no access to weights, gradients, logits, or training data\" 技术上正确但具有误导性\n\n### Should-Fix 问题\n\n**W1** 实验规模/多样性不足（3 个 7-8B 模型、2 个 benchmark、仅 QLoRA SFT）\n**W2** Post-RL 分析占据过多篇幅（N=1 获得完整 subsection + Figure）\n**W3** Related Work 缺少污染检测 survey 引用\n**W4** Fixed-θ vs free-θ 选择缺少实用指导\n\n### 主要优势\n1. DiD 设计是 causal inference 标准方法，运用得当\n2. Bootstrap CIs、seed sensitivity、power analysis 等构成完整鲁棒性体系\n3. 诚实的 Limitations（~3 个点，符合 EMNLP 要求）\n4. Appendix H 的 item bank 对比是重要方法论贡献\n5. 写作清晰，数学符号一致，Figure/Table 质量高\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 问题逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿报告\n\n**Overall Assessment**: 3.0 / 5（Findings），置信度 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] Novelty 有限：三个核心 findings 大部分可从 IRT 理论预测\n- Finding 1（θ-shift dynamics）：高能力模型的 θ-shift 吸收本质是 IRT 能力估计的天花板效应，IRT 文献中 well-known\n- Finding 2（detection-diagnosis tradeoff）：power vs. richness 的经典权衡，不构成新发现\n- Finding 3（non-monotonic dose-response）：是 Finding 1 的直接推论\n- 唯一经验价值在定量校准层面——\"useful calibration\" 而非 \"new insight\"\n\n**N2** [critical] 缺少与现有检测方法的实证对比\n- Table 3 仅在自身框架内对比 ℓ_z*、HT、accuracy，未与 ConStat/MIA 做头对头比较\n- Discussion 说 ConStat 对比 \"complicated by different information requirements\"——理由不充分\n- 实验设置可获取 logits（QLoRA → model access），MIA 方法可运行\n- 无法判断 IRT person-fit 在实际应用中的价值\n\n**N3** [critical] 标题和 framing 存在 scope mismatch\n- \"Binary response patterns\" 掩盖了对 PSN-IRT 外部 item bank 的核心依赖\n- \"Benchmark Contamination\" 标题远宽于 SFT-stage QLoRA 实验\n- Abstract \"only binary response patterns...no access to weights, gradients, logits, or training data\" 技术上正确但具有误导性\n\n### Should-Fix 问题\n\n**W1** 实验规模/多样性不足（3 个 7-8B 模型、2 个 benchmark、仅 QLoRA SFT）\n**W2** Post-RL 分析占据过多篇幅（N=1 获得完整 subsection + Figure）\n**W3** Related Work 缺少污染检测 survey 引用\n**W4** Fixed-θ vs free-θ 选择缺少实用指导\n\n### 主要优势\n1. DiD 设计是 causal inference 标准方法，运用得当\n2. Bootstrap CIs、seed sensitivity、power analysis 等构成完整鲁棒性体系\n3. 诚实的 Limitations（~3 个点，符合 EMNLP 要求）\n4. Appendix H 的 item bank 对比是重要方法论贡献\n5. 写作清晰，数学符号一致，Figure/Table 质量高\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 问题逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 572 · 2026-05-22T07:50:32.138066+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1664
}
```

</details>

---


### Assistant

_source line 573 · 2026-05-22T07:50:36.194493+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 56

## Round 56

2 recorded events


### User

_source line 574 · 2026-05-22T07:50:38.968547+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心评价：**Overall 3.5（Borderline Conference）**。

三个 Must-Fix：
1. **每个污染条件仅 n=1 运行** — Cohen's d 本质是 z-score 而非双组效应量，无法估计污染效果的可重复性
2. **摘要 "n=10 per condition" 误导** — 实际仅 clean 条件有多 seed，污染条件均为单次运行
3. **实验矩阵事后扩展** — 25% 条件在观察到 inverted-U 后才添加，构成假设确认式数据收集

六个 Should-Fix：无 <15% 低污染实验、ARC-C 仅 Qwen、fixed-θ 反转缺乏解释、Post-RL N=1 占篇幅过大、训练细节不足、Mistral n=6 bootstrap 可靠性。

主要优势：跨学科新颖性、诚实定位为 characterization、Δℓ_z* 差分设计优雅、θ-shift mechanism 分析有洞察力、Appendix 鲁棒性检查详尽。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 575 · 2026-05-22T07:50:43.783757+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 57

## Round 57

2 recorded events


### User

_source line 576 · 2026-05-22T07:52:28.827290+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R2-N1: "三个 findings 可从 IRT 理论预测，novelty 有限"**

R2 的论点有一定道理但过于苛刻，需要区分 "理论可推导" 与 "经验已知"。

(a) **Finding 1（θ-shift dynamics）**：θ-shift absorption 确实是 IRT 能力估计的已知性质——当真分数提高时 θ̂ 上升，吸收异常信号。但本文的贡献不在于重新发现这一理论，而在于 **首次量化了其在 LLM 场景中的具体表现**。特别是：Table 2 显示 Qwen 50% 时 free-θ vs fixed-θ 的 7.6× amplification ratio；ARC-C 上 ceiling effect 导致 pattern 反转（Section 4.1, L57-64）。这些模型-基准交互效应无法仅从 IRT 理论推导，需要经验数据校准。我认为这属于 "empirically valuable calibration"，但我 **同意 R2 的判断：这更接近 calibration 而非 new insight**。

(b) **Finding 2（detection-diagnosis tradeoff）**：R2 说 "power vs. richness 是经典权衡"。原则上正确，但本文的具体发现——accuracy z-score 的 |d| 比 ℓ_z* 高出一个数量级（Table 3: 68.7 vs 1.90 for Qwen 50%）——这一 **量级差距** 是经验发现，不是理论预测。此外，57/60 vs 4/60 flagged cells 的对比（Section 4.3, L117-120）展示了两类统计量在 structural sensitivity 上的根本差异。我认为 R2 在此处低估了经验贡献。

(c) **Finding 3（non-monotonic dose-response）**：**同意 R2 这是 Finding 1 的直接推论**。如果 θ-shift absorption 随污染增加而增强，而 aberrance signal 也增加，交叉点自然产生 inverted-U。本文的独立贡献仅在于经验确认了 peak 位置（~25% for Qwen）和跨模型的衰减模式（Llama ratio 1.2× vs Qwen 4.3×）。但如我在 R1-N3 中指出的，25% 条件是事后添加的，进一步削弱了这一发现的独立证据价值。

**总结**：R2 对 novelty 的担忧部分合理——理论贡献有限，主要价值在经验校准。但 "useful calibration" 对一个 characterization paper 而言 **可以构成充分贡献**，关键在于 empirical rigor（这正是我在 R1-N1/N3 中质疑的部分）。如果实验设计更严格（多 seed 污染运行、预注册），calibration 的可信度将大幅提升，novelty 争议也会减弱。

---

**[AGREE] R2-N2: "缺少与现有检测方法的实证对比"**

同意这是一个重要缺陷。具体理由：

1. **论文完全有能力做头对头对比**：作者训练了全部模型（QLoRA），拥有完整的 model access——可以运行 Min-K% Prob、perplexity-based MIA 等方法。选择不做对比是研究设计选择，不是技术限制。

2. **Discussion 中的 "different information requirements" 辩护不充分**（discussion.tex L20）：不同信息需求恰恰是应该对比的原因——读者需要知道 "只用 binary patterns + item bank" 相比 "用 logits" 损失了多少检测能力。Table 3 只在自身框架内对比了 ℓ_z*/HT/accuracy z-score，均为 person-fit 类方法。

3. **但需要补充一个 nuance**：本文明确定位为 "characterization, not tool"（Introduction L37: "Rather than proposing ℓ_z* as a ready-to-deploy detection tool"）。在此定位下，对比的必要性低于一个声称优越性的方法论文。问题在于，**如果不与外部方法对比，"characterization" 的实际价值难以评估**——读者不知道 IRT person-fit 提供的 mechanistic insight 是否比简单查看 logit 分布更有用。

4. 至少应该包含：(a) 对一两种代表性 MIA 方法的 baseline 对比；(b) Wang et al. (2025) 已展示 MIA 在 RL 后失效——本文应在同一 SFT 设置下确认 MIA 的基线性能。

---

**[AGREE] R2-N3: "标题和 framing 存在 scope mismatch"**

同意，且这与我在 R1-N2 中关于摘要措辞的关切一致。

1. **"Binary response patterns" 标题掩盖了 PSN-IRT 依赖**：虽然 Abstract L2 确实提到 "combined with externally calibrated 4PL item parameters from a large-scale item bank"，但标题和核心 framing 强调 "only binary response patterns"。Discussion L18 自己承认 "the PSN-IRT item bank a critical dependency"，且 Appendix H 显示不用 PSN-IRT 时 discrimination 几乎无法恢复（r_a=0.127）。更诚实的标题应反映这一双重需求。

2. **"Benchmark Contamination" 宽于实验覆盖**：实验仅覆盖 SFT-stage QLoRA 污染、3 个 7-8B 模型、2 个基准。标题未限定 scope，读者可能期望更广泛的覆盖（pretraining contamination、更大模型、更多基准）。Section 3.3 L62 自己说 "Our findings are scoped to SFT-based contamination"——标题应反映这一 scope。

3. **但我不认为这 "critical" 到 Must-Fix 级别**：Scope mismatch 在 NLP 论文中很常见，且作者在 Section 3.3 和 Limitations 中做了充分的 scope 声明。这更接近 Should-Fix——修改标题为 "What Can Binary Response Patterns and Calibrated Item Parameters Reveal About SFT-Stage Benchmark Contamination?" 即可解决。

---

### Should-Fix 问题

**[AGREE] R2-W1: "实验规模/多样性不足"**

与我的 R1-W1（无 <15% 污染实验）和 R1-W2（ARC-C 仅 Qwen）一致。补充一点：仅 QLoRA SFT 也是限制——full-parameter SFT 和 continued pretraining 可能产生不同的 ℓ_z* 模式。

**[AGREE] R2-W2: "Post-RL 分析占据过多篇幅"**

与我的 R1-W4 完全一致。N=1 观察不应占据 Discussion 中一个完整段落 + Figure 4 + Abstract 提及。建议移至 Appendix。

**[REBUT] R2-W3: "Related Work 缺少污染检测 survey 引用"**

R2 此处判断有误。论文 Introduction L4（introduction.tex）引用了 "chang2024survey"（Chang et al., 2024 survey），Related Work Section 2（related_work.tex）系统性覆盖了五类方法（corpus-search、MIA、generation-based、performance-based、IRT for LLM），并引用了 Zhou et al. (2023)、Sainz et al. (2023)、Jacovi et al. (2023) 等 systematization 工作。Person-fit 文献也有三段覆盖（Karabatsos 2003 的 36 统计量对比、Embretson & Reise 2000 textbook、Sinharay 2017）。Related Work 的覆盖在同类论文中属于充分水平。

**[AGREE] R2-W4: "Fixed-θ vs free-θ 选择缺少实用指导"**

同意，且与我的 R1-W3 一致。Table 2 显示 fixed-θ 对 Qwen（7.6×@50%）和 Mistral（1.6×@50%）有益，对 Llama 无益甚至有害。但论文未提供决策规则——实践者如何判断应该用哪种估计？Section 4.1 L72 给出了定性指导（"fixed-θ estimation is indicated for models with stable clean baselines and high θ-shift absorption"），但 "stable clean baseline" 和 "high θ-shift absorption" 没有操作化定义。且在 15% 时 fixed-θ 对 Qwen 反而更差（ratio=0.7×），进一步复杂化了实用指导。

---

### 总结

R2 的审稿整体严谨。核心分歧在于 novelty 评估：R2 认为 findings 可从理论预测、缺少方法对比、scope 不匹配，给出 3.0（Findings）。我部分同意 novelty 担忧，但认为 empirical calibration 在一个 characterization paper 中可以构成贡献——前提是实验设计足够严格。

**我维持 3.5（Borderline Conference）**，理由是：
- 与 R2 共识：scope mismatch 需修正、Post-RL 应精简、缺少外部方法对比
- 与 R2 分歧：novelty 评估——R2 将其视为 "known theory applied"，我视为 "first empirical characterization with meaningful calibration value"，但实验设计缺陷（R1-N1/N3）削弱了 calibration 的可信度
- 最终判断：如果作者补充多 seed 污染实验 + 至少一个外部方法对比，可达 Conference；当前版本在 Findings 和 Conference 边界

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 577 · 2026-05-22T07:52:34.541595+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 58

## Round 58

2 recorded events


### User

_source line 578 · 2026-05-22T07:52:37.329383+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 意见的逐条回应。

核心立场：
- **同意** R2-N2（缺外部方法对比）、R2-N3（scope mismatch，但降级为 Should-Fix）、R2-W1/W2/W4
- **部分同意** R2-N1（novelty 有限——理论层面是，但经验校准有价值，关键在实验 rigor）
- **反驳** R2-W3（Related Work 已引用 survey 和系统性覆盖五类方法）
- **维持** Overall 3.5（Borderline Conference），与 R2 的 3.0 有 0.5 分差距，分歧核心在于 empirical characterization 的贡献认定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 579 · 2026-05-22T07:52:41.789807+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 59

## Round 59

10 recorded events


### User

_source line 580 · 2026-05-22T07:53:07.430528+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 每个污染条件仅单次运行，Cohen's d 统计解释受限**

同意这是一个实质性的统计设计问题。论文的 Cohen's d 本质上是 one-sample z-score（单一污染观测值 vs. clean 分布），而非传统的 two-sample 标准化均差。QLoRA 微调的随机性（random seed、data ordering、gradient noise）意味着不同 seed 的污染模型可能产生不同的 l_z^* 值，而当前设计无法估计这一方差。

补充我的观察：Appendix C（Seed Sensitivity Analysis, p.11）对 clean seeds 做了 3-seed 子集分析，证明 clean 基线的 l_z^* 稳定性（ICC 隐含在 seed-specific 方差中）。但这只保证了 denominator（clean 分布）的稳定性，并未触及 R1 的核心问题——numerator（污染效果）的可变性。即使 clean baseline 稳定，如果不同 QLoRA seed 的污染模型在 l_z^* 上有较大方差，Table 1 的 effect sizes 可能不具代表性。

**建议**：作者至少应对 1 个模型/1 个污染水平运行 3-5 个 contaminated seeds，以估计污染效果的方差。若其方差远小于 clean 方差，当前设计仍可接受；若可比，则当前 effect sizes 的解释需要重大修正。

---

**[REBUT] R1-N2: 摘要中 "n=10 independent seeds per condition" 措辞具有误导性**

R1 声称摘要写了 "n=10 independent seeds per condition"，但这与论文原文不符。Abstract（p.1）的原文是：

> "We train n=10 clean seeds for Qwen and Llama and n=6 for Mistral (four checkpoints were lost when a training server was decommissioned during the study) to establish baseline variability and construct bootstrap confidence intervals. Reported CIs reflect variability across a clean baseline seeds, as each contaminated model is a single QLoRA run."

关键事实：
1. 摘要明确说的是 **"clean seeds"**，不是 "seeds per condition"。
2. 同一段落紧接着明确声明 **"each contaminated model is a single QLoRA run"**。
3. "to establish baseline variability" 进一步明确了多 seed 的目的是建立 clean 基线，而非覆盖所有条件。

R1 对摘要的引用是错误的。论文在摘要层面已经对实验设计做了透明披露。这不构成对读者或 AC 的误导。

当然，N1 中关于污染端缺少多 seed 的统计问题仍然成立——但这是一个 **实验设计局限**，而非 **framing 欺骗**。将其归为 misleading 措辞问题是 mischaracterization。

---

**[AGREE，但严重性可降级] R1-N3: 实验矩阵事后扩展构成循环论证风险**

同意事后添加 25% 条件存在 hypothesis-confirming 的方法论风险。§3.3（p.4）明确承认："Following initial observation of non-monotonic dose-response for Qwen, we added a 25% contamination condition."

然而，需要区分两个层次：
1. **循环论证程度**：25% 条件添加在 Qwen 上确实是对同一模型的事后确认。但论文随后将 25% 扩展到 Llama——这提供了**部分独立复制**（不同模型家族）。如果 Llama 也未显示非单调性，那 Qwen 的 finding 可能是噪声。实际上 Llama 的结果（§4.4, p.7："Llama shows a pronounced inverted-U"）支持了 generalization，降低了纯循环论证的风险。
2. **透明度**：论文未隐藏事后扩展的事实，这是加分项。对比之下，许多论文在不透明的情况下做事后分析。

但我同意 R1 的核心论点：**inverted-U 作为三大核心贡献之一，其确认性证据的独立性不足**。Mistral 未测试 25%，且原始发现和确认均来自作者的主动选择。建议作者至少将 inverted-U 的 claim 强度从 "finding" 降级为 "observation requiring further validation"，或补做 Mistral 25%。

---

### Should-Fix 问题

**[AGREE] R1-W1: 无低污染水平（<15%）的实证实验**

完全同意。Appendix A（p.11）的模拟显示 5% 污染时 MMLU 的 power 仅 47.6%（低于 80% 常规阈值）。这意味着论文的方法在真实世界最常见的低污染场景下功效不足。更重要的是，论文的 Discussion（p.8）提到 "detection relies on a pre-contamination baseline"，但如果 baseline 模型本身就有少量污染（这在 leaderboard 模型中很常见），15% 的最低测试阈值可能过高。这一限制与我在 Round 1 报告中提出的 W1（实验规模/多样性不足）一致。

---

**[AGREE] R1-W2: ARC-C 仅限 Qwen，跨基准泛化证据不足**

同意。§3.3（p.4）承认 ARC-C 实验仅在 Qwen 上进行，且 ARC-C 仅有 295 items，l_z^* 统计量的功效显著下降。论文声称 "reliably detects SFT-stage contamination across three model families"（§6, p.8），但 "across" 的支撑证据仅来自 MMLU。将 ARC-C 的 cross-benchmark claim 限定为 Qwen-only observation 是更准确的表述。这与我在 Round 1 中提出的观点一致。

---

**[AGREE] R1-W3: Fixed-θ 在 15% 时反而比 free-θ 更差（Qwen ratio=0.7×）**

同意需要更充分的解释。§4.2（p.5）和 Table 2（p.6）讨论了 fixed-θ vs. free-θ，但对 Qwen 在 15% 时 fixed-θ 效果反而更差这一反直觉现象缺乏深入分析。这直接影响了我在 Round 1 报告中提出的 W4（fixed-θ vs. free-θ 选择缺少实用指导）——如果 fixed-θ 在某些条件下反而降低检测力，实践者该如何选择？论文应至少给出一个 heuristic 或 decision rule。

---

**[AGREE] R1-W4: Post-RL 观察（N=1）占据过大篇幅**

完全同意。我在 Round 1 报告中已将此列为 W2（Should-Fix）：§4.5 和 Figure 4 将 ~0.5 页用于无法做统计推断的 N=1 观察。建议移入 Appendix。两位 reviewer 一致认为这是 space allocation 问题。

---

**[AGREE，部分保留] R1-W5: QLoRA 训练细节不足以复现**

同意训练细节的完整性对 reproducibility 很重要。但需要平衡两点：(1) 论文承诺 "Code and response data will be released upon acceptance"（Reproducibility Statement, p.9），开源代码可弥补论文中的细节缺失；(2) 8 页正文空间有限，QLoRA 作为标准方法，部分细节可放在 Appendix 或 code release 中。

建议在 Appendix 补充完整的 hyperparameter table（LR、epoch、batch size、warmup、data mixing ratio），这不占主文空间但解决 reproducibility 问题。

---

**[AGREE] R1-W6: Mistral n=6 的 bootstrap CI 可靠性问题**

同意。n=6 的 BCa bootstrap CI 在统计理论上可靠性有限（Efron & Tibshirani 推荐 n≥20 以确保 CI coverage 接近 nominal level）。论文透明地解释了 n=6 的原因（"four checkpoints were lost when a training server was decommissioned"），但这并不改变统计功效的客观限制。Table 6（Appendix D, p.12）显示 3-seed 子集的 CIs 在某些条件下包含零，进一步印证了小样本问题。

---

### 总结

9 个问题中，我同意 7 个（含 1 个降级为 observation-level），反驳 1 个（N2 的 misquote），部分保留 1 个（W5）。

**最关键的共识**：R1-N1（单次污染运行）和我在 Round 1 中提出的 N2（缺少实证对比）是本文最核心的两个问题。前者质疑定量结论的统计基础，后者质疑研究的实际价值定位。两者共同将论文锚定在 Findings 水平。

**核心分歧**：R1-N2（摘要误导性）不成立——论文原文清楚区分了 "clean seeds" 和 "single QLoRA run"，R1 的引用有误。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 581 · 2026-05-22T07:53:42.579172+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 582 · 2026-05-22T07:53:42.579559+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T07:41:13.487792+00:00\", \"completed_at\": \"2026-05-22T07:44:16.869232+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯文本），Figure 1 出现在第 2 页——在前 3 页阈值内，但若能将 Figure 1 提升至第 1 页底部（如 Introduction 第一段后），可增强审稿人第一印象锚定\"}, {\"severity\": \"info\", \"dimension\": \"pages 3-4\", \"message\": \"连续 2 页无 display item（Method 段），仅有公式提供视觉节奏。对于方法论描述可接受，但若能在 Section 3 插入一个概念示意图（如 pipeline/framework 图），可帮助审稿人快速理解检测流程\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 热力图 cell 内数字字号偏小（估计 ~6-7pt），在实际打印尺寸下可能需要仔细辨认。建议适当增大 cell 内字号或减少小数位数以提高可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 使用单色蓝梯度——色盲安全 ✓，但 cell 内同时标注数字确保了即使颜色难以区分也能获取信息\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 使用不同填充的三角标记区分 contamination level（15%/25%/50%），可考虑同时变化 marker shape（如 circle/square/triangle）进一步增强灰度打印时的可区分度\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 未对最大 Cohen's d 加粗标记——此表展示不同条件下的效应量而非方法竞争，不加粗尚可理解，但高亮最大效应量可提升 scannability\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 4 轴标签和图例文字字号尚可（~8pt），但 y 轴标签 \\\"accuracy on seen/unseen\\\" 与右轴 \\\"ζ' gap\\\" 双轴设计增加了认知负担，caption 解释充分弥补了这一点\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"末页（附录）内容约占 60-65%，略低于 2/3 阈值，但作为附录末页可接受\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 8}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 583 · 2026-05-22T07:53:42.579742+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 584 · 2026-05-22T07:53:42.680336+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 585 · 2026-05-22T07:56:23.195646+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_personfit_contam",
  "issues_yaml": "## Review Issue Tracker — Round 5 (fresh review, 2026-05-22)\n## Reviewer 1 (方法严谨性, 3.5 Borderline Conference) + Reviewer 2 (新颖性/完整性, 3.0 Findings)\n\n# ===== CRITICAL ISSUES =====\n\n- id: \"R5-N1\"\n  summary: \"每个污染条件仅单次运行——Cohen's d 本质是 one-sample z-score，无法估计污染效果方差\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样指出 Cohen's d 将被污染模型视为固定点\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N1 提出，R2 交叉 AGREE。每个污染水平仅训练 1 个模型，所有方差来自 clean seeds。QLoRA 微调的随机性（seed、data ordering、gradient noise）意味着不同 seed 的污染模型可能产生不同 ℓ_z* 值。Table 1 的 effect sizes 可能不具代表性。Inverted-U 可能因单个 outlier 运行而成立或不成立。\"\n  action_items:\n    - round: 5\n      action: \"至少为 1 个模型/1 个污染水平运行 3-5 个 contaminated seeds，估计污染效果方差\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N2\"\n  summary: \"缺少与现有污染检测方法（ConStat/MIA）的实证对比\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样提出，作者在 Discussion 中仅用一句 'complementary' 带过\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-N2 提出，R1 交叉 AGREE。Table 3 仅在自身框架内对比 ℓ_z*/HT/accuracy。作者拥有完整 model access（QLoRA 训练），可运行 MIA 方法。Discussion 的 'different information requirements' 辩护不充分。R1 补充：不同信息需求恰恰是应该对比的原因。\"\n  action_items:\n    - round: 5\n      action: \"至少在 MMLU 上运行 ConStat 和一种 MIA-based 方法，做头对头对比\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N3\"\n  summary: \"实验矩阵事后扩展——25% 条件在观察到 inverted-U 后才添加，构成假设确认式数据收集\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样指出 25% 未在 §3.3 描述的透明性问题\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N3 提出，R2 交叉 AGREE（建议可降级为 observation-level）。§3.3 明确承认事后添加。Llama 扩展提供部分独立复制，但 Mistral 未测 25%。R2 认为透明披露是加分项，但 inverted-U 作为核心贡献之一，确认性证据的独立性仍不足。\"\n  action_items:\n    - round: 5\n      action: \"将 inverted-U 从 'behavior boundary' 降级为 'exploratory observation requiring prospective confirmation'；或补做 Mistral 25%\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== SHOULD-FIX ISSUES =====\n\n- id: \"R5-W1\"\n  summary: \"Title/framing scope mismatch——'binary response patterns' 掩盖 PSN-IRT 依赖；'benchmark contamination' 宽于 SFT-stage QLoRA 实验\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮 R4-W1（black-box overclaim）和 R4-W2（SFT scope）同一问题\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-N3 提出为 Must-Fix，R1 交叉 AGREE 但降级为 Should-Fix。Abstract 提到 PSN-IRT 依赖但嵌在长句中不够突出。标题未限定 SFT scope。R1 认为 scope mismatch 在 NLP 论文中常见，改标题即可解决。\"\n  action_items:\n    - round: 5\n      action: \"标题加 SFT-stage 限定；Abstract 突出 PSN-IRT 依赖为独立需求\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"Post-RL 观察（N=1）占据过大篇幅——~0.5 页用于无统计推断的单模型观察\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样要求降级为 Discussion preliminary observation\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W4 和 R2-W2 独立提出，交叉完全一致。§5 Discussion 完整段落 + Figure 4 + Abstract 提及。建议移至 Appendix，正文用 1-2 句话提及。\"\n  action_items:\n    - round: 5\n      action: \"Figure 4 和 Post-RL 详述移至 Appendix；正文 Discussion 保留 1-2 句 preliminary observation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"无低污染水平（<15%）的实证实验——模拟显示 5% 时 MMLU power 仅 47.6%\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 交叉 AGREE。实际场景中低污染更常见，15% 最低阈值过高。Discussion 应更显著讨论低污染检测局限性。\"\n  action_items:\n    - round: 5\n      action: \"至少在 1 个模型族测试 5% 污染；或在 Discussion/Limitations 显著讨论低污染功效限制\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"ARC-C 仅限 Qwen，跨基准泛化证据不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样指出实验矩阵不完整\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W2 提出，R2 交叉 AGREE。ARC-C 仅 295 items 且仅 Qwen 测试。'across three model families' claim 的支撑仅来自 MMLU。\"\n  action_items:\n    - round: 5\n      action: \"弱化跨基准泛化 claim；ARC-C ceiling effect 限定为 Qwen-only observation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"Fixed-θ 在 Qwen 15% 时反而更差（ratio=0.7×），缺乏定量解释且无实用决策指导\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮未单独指出此反直觉现象\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W3 提出反直觉现象，R2 交叉 AGREE。R2-W4 提出缺少实用指导，R1 交叉 AGREE。Table 2 Qwen 15% fixed-θ |d|=4.77 < free-θ |d|=6.58。论文的叙事 'fixed-θ recovers signal' 在此条件下不成立。§4.2 末段给出定性指导但无操作化定义。\"\n  action_items:\n    - round: 5\n      action: \"解释 15% 时 fixed-θ 劣于 free-θ 的机制；提供 decision rule 或 heuristic\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W6\"\n  summary: \"实验规模/多样性不足——全部 7-8B，无不同规模模型，仅 QLoRA SFT\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样指出模型规模和污染机制覆盖不足\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-W1 提出，R1 交叉 AGREE。无 1-3B、13B+、MoE 架构。仅 QLoRA SFT，无 full fine-tuning、continued pretraining。Conclusion 承认 'broader model scales' 是 future work。\"\n  action_items:\n    - round: 5\n      action: \"大幅弱化 generalization claims；Limitations 明确列出规模和污染机制限制\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W7\"\n  summary: \"QLoRA 训练细节不足以复现——缺 LR、epoch、batch size、数据混合方式\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 部分 AGREE。§3.3 仅报告 rank=16, α=32。R2 认为开源代码可弥补，但 Appendix 补充 hyperparameter table 更佳。\"\n  action_items:\n    - round: 5\n      action: \"Appendix 补充完整 hyperparameter table（LR、epoch、batch size、warmup、data mixing ratio、序列长度）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W8\"\n  summary: \"Mistral n=6 的 bootstrap CI 可靠性有限\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样讨论了小样本 bootstrap 问题\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W6 提出，R2 交叉 AGREE。Efron & Tibshirani 推荐 n≥20。BCa（Appendix G）确认 percentile CI 保守，但 BCa 自身在 n=6 也未必可靠。建议补充 permutation test p-value。\"\n  action_items:\n    - round: 5\n      action: \"Mistral 结果添加小样本 bootstrap 局限性讨论；考虑补充 permutation test\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== DIVERGENCE =====\n\n- id: \"R5-D1\"\n  summary: \"Novelty 评估分歧——empirical calibration 价值 vs IRT 理论可预测性\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样存在此分歧\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-N1 认为三个 findings 大部分可从 IRT 理论预测（θ-shift ceiling、power-richness tradeoff、inverted-U 是 Finding 1 推论），novelty 有限。R1 部分 REBUT：定量校准有独立价值（Table 2 的 7.6× ratio、ARC-C ceiling reversal、57/60 vs 4/60 flagged cells），但同意 Finding 3 是 Finding 1 的直接推论。R1 认为 'useful calibration' 对 characterization paper 可构成充分贡献。分歧未解决。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ===== RESOLVED FROM R1-N2 =====\n\n- id: \"R5-R1\"\n  summary: \"Abstract 'n=10 per condition' 措辞误导——经核实不成立\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N2 提出 Abstract 写 'n=10 per condition' 具有误导性。R2 交叉 REBUT：原文写的是 'n=10 clean seeds' 并紧接说明 'each contaminated model is a single QLoRA run'，措辞透明。R1 引用有误。\"\n  action_items: []\n  resolution: \"不成立——Abstract 原文已透明披露实验设计\"\n  resolution_round: 5\n\n# ===== MINOR ISSUES =====\n\n- id: \"R5-M1\"\n  summary: \"Figure 2 heatmap cell 内数字字号偏小（~6-7pt）\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [visual_check]\n      note: \"R4 视觉审查同样发现\"\n    - round: 5\n      reviewers: [visual_check]\n      note: \"视觉审查确认，实际打印尺寸下需仔细辨认\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M2\"\n  summary: \"§3.2 DiD 命名不精确——标准 DiD 需时间维度，此处更接近 matched-difference design\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1]\n      note: \"R1 minor：标准 DiD 需时间维度上的前后对比，此处是 matched-difference\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M3\"\n  summary: \"Pages 3-4 连续无 display item，可考虑添加 pipeline/framework 概念图\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [visual_check]\n      note: \"视觉审查建议：Method 段仅有公式，pipeline 图可帮助审稿人快速理解检测流程\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ===== PRIOR ROUND RESOLVED ISSUES (carried forward) =====\n\n- id: \"BEST-W1\"\n  summary: \"0 figures, presentation unacceptable\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"确认已解决。4 figures + 多 tables。\"\n  resolution: \"Resolved\"\n  resolution_round: 2\n\n- id: \"ACTUAL-B-W1\"\n  summary: \"n=3 seeds statistically insufficient\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Qwen/Llama n=10 确认。Mistral n=6 残留问题追踪为 R5-W8。\"\n  resolution: \"Resolved\"\n  resolution_round: 3\n\n- id: \"R2-W7\"\n  summary: \"缺少 reproducibility statement\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"确认已解决。Reproducibility Statement 存在 (p.9)。\"\n  resolution: \"Resolved\"\n  resolution_round: 3\n\n- id: \"R3-W2\"\n  summary: \"Mistral n=6 seeds 统计效力不足\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"状态不变。Checkpoints 丢失无法补跑。CI 排除零，结论仍成立。\"\n  resolution: \"Checkpoints lost; CI excludes zero; noted as limitation\"\n  resolution_round: 3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_personfit_contam",
    "issues_yaml": "## Review Issue Tracker — Round 5 (fresh review, 2026-05-22)\n## Reviewer 1 (方法严谨性, 3.5 Borderline Conference) + Reviewer 2 (新颖性/完整性, 3.0 Findings)\n\n# ===== CRITICAL ISSUES =====\n\n- id: \"R5-N1\"\n  summary: \"每个污染条件仅单次运行——Cohen's d 本质是 one-sample z-score，无法估计污染效果方差\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样指出 Cohen's d 将被污染模型视为固定点\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N1 提出，R2 交叉 AGREE。每个污染水平仅训练 1 个模型，所有方差来自 clean seeds。QLoRA 微调的随机性（seed、data ordering、gradient noise）意味着不同 seed 的污染模型可能产生不同 ℓ_z* 值。Table 1 的 effect sizes 可能不具代表性。Inverted-U 可能因单个 outlier 运行而成立或不成立。\"\n  action_items:\n    - round: 5\n      action: \"至少为 1 个模型/1 个污染水平运行 3-5 个 contaminated seeds，估计污染效果方差\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N2\"\n  summary: \"缺少与现有污染检测方法（ConStat/MIA）的实证对比\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样提出，作者在 Discussion 中仅用一句 'complementary' 带过\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-N2 提出，R1 交叉 AGREE。Table 3 仅在自身框架内对比 ℓ_z*/HT/accuracy。作者拥有完整 model access（QLoRA 训练），可运行 MIA 方法。Discussion 的 'different information requirements' 辩护不充分。R1 补充：不同信息需求恰恰是应该对比的原因。\"\n  action_items:\n    - round: 5\n      action: \"至少在 MMLU 上运行 ConStat 和一种 MIA-based 方法，做头对头对比\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N3\"\n  summary: \"实验矩阵事后扩展——25% 条件在观察到 inverted-U 后才添加，构成假设确认式数据收集\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样指出 25% 未在 §3.3 描述的透明性问题\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N3 提出，R2 交叉 AGREE（建议可降级为 observation-level）。§3.3 明确承认事后添加。Llama 扩展提供部分独立复制，但 Mistral 未测 25%。R2 认为透明披露是加分项，但 inverted-U 作为核心贡献之一，确认性证据的独立性仍不足。\"\n  action_items:\n    - round: 5\n      action: \"将 inverted-U 从 'behavior boundary' 降级为 'exploratory observation requiring prospective confirmation'；或补做 Mistral 25%\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== SHOULD-FIX ISSUES =====\n\n- id: \"R5-W1\"\n  summary: \"Title/framing scope mismatch——'binary response patterns' 掩盖 PSN-IRT 依赖；'benchmark contamination' 宽于 SFT-stage QLoRA 实验\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮 R4-W1（black-box overclaim）和 R4-W2（SFT scope）同一问题\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-N3 提出为 Must-Fix，R1 交叉 AGREE 但降级为 Should-Fix。Abstract 提到 PSN-IRT 依赖但嵌在长句中不够突出。标题未限定 SFT scope。R1 认为 scope mismatch 在 NLP 论文中常见，改标题即可解决。\"\n  action_items:\n    - round: 5\n      action: \"标题加 SFT-stage 限定；Abstract 突出 PSN-IRT 依赖为独立需求\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"Post-RL 观察（N=1）占据过大篇幅——~0.5 页用于无统计推断的单模型观察\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样要求降级为 Discussion preliminary observation\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W4 和 R2-W2 独立提出，交叉完全一致。§5 Discussion 完整段落 + Figure 4 + Abstract 提及。建议移至 Appendix，正文用 1-2 句话提及。\"\n  action_items:\n    - round: 5\n      action: \"Figure 4 和 Post-RL 详述移至 Appendix；正文 Discussion 保留 1-2 句 preliminary observation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"无低污染水平（<15%）的实证实验——模拟显示 5% 时 MMLU power 仅 47.6%\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 交叉 AGREE。实际场景中低污染更常见，15% 最低阈值过高。Discussion 应更显著讨论低污染检测局限性。\"\n  action_items:\n    - round: 5\n      action: \"至少在 1 个模型族测试 5% 污染；或在 Discussion/Limitations 显著讨论低污染功效限制\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"ARC-C 仅限 Qwen，跨基准泛化证据不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样指出实验矩阵不完整\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W2 提出，R2 交叉 AGREE。ARC-C 仅 295 items 且仅 Qwen 测试。'across three model families' claim 的支撑仅来自 MMLU。\"\n  action_items:\n    - round: 5\n      action: \"弱化跨基准泛化 claim；ARC-C ceiling effect 限定为 Qwen-only observation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"Fixed-θ 在 Qwen 15% 时反而更差（ratio=0.7×），缺乏定量解释且无实用决策指导\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮未单独指出此反直觉现象\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W3 提出反直觉现象，R2 交叉 AGREE。R2-W4 提出缺少实用指导，R1 交叉 AGREE。Table 2 Qwen 15% fixed-θ |d|=4.77 < free-θ |d|=6.58。论文的叙事 'fixed-θ recovers signal' 在此条件下不成立。§4.2 末段给出定性指导但无操作化定义。\"\n  action_items:\n    - round: 5\n      action: \"解释 15% 时 fixed-θ 劣于 free-θ 的机制；提供 decision rule 或 heuristic\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W6\"\n  summary: \"实验规模/多样性不足——全部 7-8B，无不同规模模型，仅 QLoRA SFT\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样指出模型规模和污染机制覆盖不足\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-W1 提出，R1 交叉 AGREE。无 1-3B、13B+、MoE 架构。仅 QLoRA SFT，无 full fine-tuning、continued pretraining。Conclusion 承认 'broader model scales' 是 future work。\"\n  action_items:\n    - round: 5\n      action: \"大幅弱化 generalization claims；Limitations 明确列出规模和污染机制限制\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W7\"\n  summary: \"QLoRA 训练细节不足以复现——缺 LR、epoch、batch size、数据混合方式\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 部分 AGREE。§3.3 仅报告 rank=16, α=32。R2 认为开源代码可弥补，但 Appendix 补充 hyperparameter table 更佳。\"\n  action_items:\n    - round: 5\n      action: \"Appendix 补充完整 hyperparameter table（LR、epoch、batch size、warmup、data mixing ratio、序列长度）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W8\"\n  summary: \"Mistral n=6 的 bootstrap CI 可靠性有限\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样讨论了小样本 bootstrap 问题\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W6 提出，R2 交叉 AGREE。Efron & Tibshirani 推荐 n≥20。BCa（Appendix G）确认 percentile CI 保守，但 BCa 自身在 n=6 也未必可靠。建议补充 permutation test p-value。\"\n  action_items:\n    - round: 5\n      action: \"Mistral 结果添加小样本 bootstrap 局限性讨论；考虑补充 permutation test\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== DIVERGENCE =====\n\n- id: \"R5-D1\"\n  summary: \"Novelty 评估分歧——empirical calibration 价值 vs IRT 理论可预测性\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4 轮同样存在此分歧\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-N1 认为三个 findings 大部分可从 IRT 理论预测（θ-shift ceiling、power-richness tradeoff、inverted-U 是 Finding 1 推论），novelty 有限。R1 部分 REBUT：定量校准有独立价值（Table 2 的 7.6× ratio、ARC-C ceiling reversal、57/60 vs 4/60 flagged cells），但同意 Finding 3 是 Finding 1 的直接推论。R1 认为 'useful calibration' 对 characterization paper 可构成充分贡献。分歧未解决。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ===== RESOLVED FROM R1-N2 =====\n\n- id: \"R5-R1\"\n  summary: \"Abstract 'n=10 per condition' 措辞误导——经核实不成立\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N2 提出 Abstract 写 'n=10 per condition' 具有误导性。R2 交叉 REBUT：原文写的是 'n=10 clean seeds' 并紧接说明 'each contaminated model is a single QLoRA run'，措辞透明。R1 引用有误。\"\n  action_items: []\n  resolution: \"不成立——Abstract 原文已透明披露实验设计\"\n  resolution_round: 5\n\n# ===== MINOR ISSUES =====\n\n- id: \"R5-M1\"\n  summary: \"Figure 2 heatmap cell 内数字字号偏小（~6-7pt）\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [visual_check]\n      note: \"R4 视觉审查同样发现\"\n    - round: 5\n      reviewers: [visual_check]\n      note: \"视觉审查确认，实际打印尺寸下需仔细辨认\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M2\"\n  summary: \"§3.2 DiD 命名不精确——标准 DiD 需时间维度，此处更接近 matched-difference design\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1]\n      note: \"R1 minor：标准 DiD 需时间维度上的前后对比，此处是 matched-difference\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M3\"\n  summary: \"Pages 3-4 连续无 display item，可考虑添加 pipeline/framework 概念图\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [visual_check]\n      note: \"视觉审查建议：Method 段仅有公式，pipeline 图可帮助审稿人快速理解检测流程\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ===== PRIOR ROUND RESOLVED ISSUES (carried forward) =====\n\n- id: \"BEST-W1\"\n  summary: \"0 figures, presentation unacceptable\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"确认已解决。4 figures + 多 tables。\"\n  resolution: \"Resolved\"\n  resolution_round: 2\n\n- id: \"ACTUAL-B-W1\"\n  summary: \"n=3 seeds statistically insufficient\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Qwen/Llama n=10 确认。Mistral n=6 残留问题追踪为 R5-W8。\"\n  resolution: \"Resolved\"\n  resolution_round: 3\n\n- id: \"R2-W7\"\n  summary: \"缺少 reproducibility statement\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"确认已解决。Reproducibility Statement 存在 (p.9)。\"\n  resolution: \"Resolved\"\n  resolution_round: 3\n\n- id: \"R3-W2\"\n  summary: \"Mistral n=6 seeds 统计效力不足\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"状态不变。Checkpoints 丢失无法补跑。CI 排除零，结论仍成立。\"\n  resolution: \"Checkpoints lost; CI excludes zero; noted as limitation\"\n  resolution_round: 3"
  }
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-22T07:56:23.297294+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml\", \"bytes\": 11086}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 587 · 2026-05-22T07:59:06.475588+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "irt_personfit_contam",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "report": "# 审稿报告：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n\n**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n**Reviewers**: R1（方法严谨性, 3.5 Borderline Conference）、R2（新颖性/完整性, 3.0 Findings）\n**Overall Assessment**: **3.0 (Findings)**\n**Confidence**: 4/5\n\n---\n\n## Summary\n\n本文首次将心理测量学中的 IRT person-fit 统计量（ℓ_z*）系统性应用于 LLM 基准污染检测。核心思路：被污染的 LLM 类似于拥有题目预知的考生，会在难题上产生异常正确的作答模式。作者提出 Δℓ_z*（差分设计）消除 IRT 模型误设的影响，在 3 个 7-8B 模型族（Qwen2.5-7B、Llama-3.1-8B、Mistral-7B；n=10 clean seeds，Mistral n=6）× 2 个基准（MMLU 14,042 items、ARC-C 295 items）× 3-4 个污染水平（15%/25%/50%）上进行了控制实验（每个污染条件单次 QLoRA 运行）。报告三个行为边界：(1) 模型特异的 θ-shift absorption；(2) detection-diagnosis tradeoff；(3) 能力依赖的非单调剂量-效应。附带 N=1 的 post-RL preliminary observation。\n\n---\n\n## Strengths\n\n1. **新颖的跨学科桥接**：首次将教育测量学 person-fit 理论系统性引入 NLP 污染检测。\"污染 LLM ≈ 作弊考生\" 的类比自然且有启发性，开辟了 psychometrics × NLP 的新方向。[R1 AGREE, R2 AGREE]\n\n2. **Δℓ_z* 差分设计的优雅性**：绝对 ℓ_z* 在 LLM 上完全失效（57/60 cells flagged as aberrant），差分设计通过消除共享模型误设巧妙解决了这一核心障碍。Appendix F 的 local dependence 模拟进一步验证了该设计在现实依赖结构下的鲁棒性（d_ratio ≥ 0.93 for σ_τ ≤ 0.5）。[R1 AGREE, R2 AGREE]\n\n3. **θ-shift absorption 机制分析**：对 \"为什么高能力模型检测信号更弱\" 的机制解释清晰有说服力。Table 2 的 free-θ vs fixed-θ 对比（Qwen 50%: 7.6× amplification）提供了强支撑。ARC-C 的 ceiling effect 反转（高基线反而增强信号）是非教科书式的经验发现。[R1 AGREE, R2 partial AGREE]\n\n4. **诚实定位**：论文明确定位为 \"characterization\"（行为边界刻画）而非 \"tool\"（现成工具），坦承简单统计量在纯检测任务上表现更优（Table 3: accuracy z-score |d|=68.7 vs ℓ_z* |d|=1.90）。这种学术诚实在该领域少见。[R1 AGREE, R2 AGREE]\n\n5. **详尽的鲁棒性分析**：8 个 Appendix 涵盖 simulation validation、4PL vs 3PL ablation、seed sensitivity、cross-family consistency、item-level AUROC、local dependence robustness、parameter perturbation、BCa comparison、MML-EM refit。方法论严谨态度明显。[R1 AGREE, R2 AGREE]\n\n6. **Appendix H 的 MML-EM 对比**：证明 classical MML-EM 估计无法替代 PSN-IRT（r_a=0.127），为 \"为什么需要外部 item bank\" 提供了定量支撑，是重要的方法论贡献。[R2 特别肯定]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[W-MF1] 每个污染条件仅单次运行，Cohen's d 统计解释受限** [R1-N1, R2 AGREE]\n\n论文的 Cohen's d 本质上是单一污染观测值相对于 clean 分布的 one-sample z-score，而非两组分布间的标准化均差。每个污染水平（15%/25%/50%）仅训练了 1 个 QLoRA 模型，所有方差估计均来自 clean seeds。QLoRA 微调具有随机性（初始化、数据顺序、gradient noise），不同 seed 可能产生不同的 ℓ_z* 值。当前设计无法：(a) 估计污染效果的方差；(b) 判断观测到的 ℓ_z* shift 是否具有代表性。Table 1 的全部 effect sizes、inverted-U 的具体幅度（Qwen 4.3× peak-to-trough）、cross-model 比较均可能因单一运行的随机性而不稳定。\n\n*两位 Reviewer 一致认为这是最核心的实验设计缺陷。*\n\n**[W-MF2] 缺少与现有污染检测方法的实证对比** [R2-N2, R1 AGREE]\n\nTable 3 仅在自身框架内对比了 ℓ_z*、HT、accuracy z-score，完全没有与已有的专用污染检测方法（ConStat、MIA-based methods）进行头对头比较。作者拥有完整 model access（QLoRA 训练），可运行 Min-K% Prob 等 MIA 方法。Discussion 中 \"different information requirements\" 的辩护不充分——不同信息需求恰恰是应该对比的原因，读者需要知道 \"只用 binary patterns + item bank\" 相比 \"用 logits\" 损失了多少检测能力。R1 补充：论文定位为 \"characterization, not tool\"，但如果不与外部方法对比，characterization 的实际价值难以评估。\n\n**[W-MF3] 实验矩阵事后扩展构成假设确认风险** [R1-N3, R2 AGREE with severity nuance]\n\n§3.3 明确承认：\"Following initial observation of non-monotonic dose-response for Qwen, we added a 25% contamination condition.\" 这是 hypothesis-confirming data collection。Inverted-U 是论文三大核心贡献之一，但确认该发现的数据点（25%）是在看到初始结果后才添加的。虽然后续扩展到 Llama 提供了部分独立复制，但 Mistral 未测 25%。论文的透明披露是加分项，但 inverted-U 的 claim 强度与证据的独立性不匹配。R2 认为可降级为 \"observation requiring prospective confirmation\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[W-SF1] Title/framing scope mismatch** [R2-N3, R1 AGREE but downgrade]\n\n标题 \"Binary Response Patterns\" 掩盖了对 PSN-IRT 外部 item bank 的核心依赖（Appendix H 证明不用 PSN-IRT 时 r_a=0.127）。\"Benchmark Contamination\" 远宽于 SFT-stage QLoRA 实验范围。Abstract 提到 PSN-IRT 依赖但嵌在长句中不够突出。R1 认为这在 NLP 论文中常见，改标题加 \"SFT-Stage\" 限定 + Abstract 突出 item bank 依赖即可。\n\n**[W-SF2] Post-RL 观察（N=1）占据过大篇幅** [R1-W4, R2-W2, 双方 AGREE]\n\nN=1（Qwen only, GRPO, 15% MMLU）的 post-RL 观察获得了 Discussion 完整段落 + Figure 4（~0.5页），且在 Abstract 中被提及。在 8 页空间限制下，这一比重过高。两位 Reviewer 一致建议移至 Appendix。\n\n**[W-SF3] 无低污染水平（<15%）的实证实验** [R1-W1, R2 AGREE]\n\n经验实验最低污染水平为 15%，模拟（Appendix A）显示 5% 时 MMLU power 仅 47.6%。实际场景中低污染更常见，当前最低测试阈值过高。\n\n**[W-SF4] ARC-C 仅限 Qwen，跨基准泛化证据不足** [R1-W2, R2 AGREE]\n\nARC-C（295 items）仅在 Qwen 上测试。\"across three model families\" claim 的跨基准支撑仅来自 MMLU。\n\n**[W-SF5] Fixed-θ 反直觉现象缺乏解释 + 无实用决策指导** [R1-W3 + R2-W4, 双方 AGREE]\n\nTable 2 显示 Qwen 15% 时 fixed-θ 反而比 free-θ 更差（ratio=0.7×），与 \"fixed-θ recovers signal\" 的核心叙事矛盾。§4.2 末段给出定性指导但缺少操作化定义和 decision rule。\n\n**[W-SF6] 实验规模/多样性不足** [R2-W1, R1 AGREE]\n\n全部 7-8B 规模，无 1-3B/13B+/MoE 架构。仅 QLoRA SFT，无 full fine-tuning/continued pretraining。Generalization claims 超出实验覆盖。\n\n**[W-SF7] QLoRA 训练细节不足** [R1-W5, R2 partial AGREE]\n\n§3.3 仅报告 rank=16, α=32，缺 LR、epoch、batch size、数据混合方式等关键超参数。建议在 Appendix 补充完整 hyperparameter table。\n\n**[W-SF8] Mistral n=6 的 bootstrap CI 可靠性** [R1-W6, R2 AGREE]\n\nn=6 的 bootstrap CI 在统计理论上可靠性有限。BCa（Appendix G）提供了 sensitivity check，但自身在 n=6 也未必可靠。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上达成完全共识：\n\n1. **单次污染运行是最核心的实验设计缺陷**（W-MF1）——需要至少为关键条件补充多 seed 污染实验\n2. **缺少与外部方法的实证对比削弱了论文的价值定位**（W-MF2）——至少应与 1-2 种代表性方法做 baseline 比较\n3. **Post-RL N=1 应精简**（W-SF2）——移至 Appendix\n4. **Framing 应收窄以匹配实验范围**（W-SF1）——标题加 SFT-stage，Abstract 突出 PSN-IRT 依赖\n5. **实验矩阵的事后扩展降低了 inverted-U 的证据强度**（W-MF3）——应降级 claim 或补充独立验证\n\n---\n\n## Reviewer Divergence [REBUT]\n\n**[R5-D1] Novelty 评估**\n\n- **R2 立场（3.0 Findings）**：三个核心 findings 大部分可从 IRT 理论直接预测——θ-shift ceiling effect 是 well-known 的 IRT 性质，detection-diagnosis tradeoff 是 power vs. richness 的经典权衡，inverted-U 是 Finding 1 的直接推论。经验贡献主要在定量校准层面（\"useful calibration, not new insight\"）。\n\n- **R1 立场（3.5 Borderline Conference）**：承认理论方向可预测，但强调：(a) 定量结果和边界条件是新的——ARC-C ceiling effect 反转非教科书推论，57/60 vs 4/60 flagged cells 是新经验发现；(b) LLM 严重违反 IRT 假设，理论预测是否在 LLM 上成立需要经验回答；(c) \"useful calibration\" 对 characterization paper 可构成充分贡献，**前提是实验设计足够严格**（R1-N1/N3 的缺陷削弱了这一前提）。\n\n- **Director 判断**：分歧未解决，但两位 Reviewer 均同意当前实验设计不够严格，这使得 calibration 的可信度本身也受损。实验设计缺陷的修复（多 seed 运行、外部方法对比）可能间接缓解 novelty 争议——如果 calibration 数据更可靠，其独立贡献更容易被接受。\n\n---\n\n## Questions to Authors\n\n1. 如果为 Qwen 15%/50% 各训练 3-5 个不同 seed 的污染模型，预期 ℓ_z* 的 seed-level 方差有多大？是否有任何 pilot 数据估计污染效果的可重复性？\n\n2. ConStat 需要 reference benchmark 分数——你们已有 ARC-C 和 MMLU 两个 benchmark，这似乎满足了 ConStat 的最低信息需求。为什么选择不做对比？\n\n3. Table 2 中 Qwen 15% 的 fixed-θ 比 free-θ 更差（ratio=0.7×），能否提供定量解释？Snijders correction 在此处的具体影响是什么？\n\n4. PSN-IRT 校准样本（13,000+ 模型）中，估计有多大比例可能存在基准污染？Appendix F.2 的 ±10% 随机噪声能否模拟系统性污染偏差？\n\n5. 是否考虑过在 held-out 模型族（如 Phi-3、Gemma）上前瞻性验证 inverted-U？\n\n---\n\n## Missing References\n\n- **污染检测 survey**：虽然论文已引用 Chang et al. (2024) survey，但 R2 建议补充更近期的专题 survey（如 Dong et al. 2024 \"Does Data Contamination Detection Work (Well) for LLMs?\"，对检测方法假设做了系统评估，与本文的 characterization 目标直接相关）。R1 认为当前覆盖已属充分。Director 倾向于：至少补充 Dong et al. (2024)，因其对检测假设的评估与本文高度互补。\n\n- **IRT person-fit 功效分析**：Sinharay & Johnson (2017) 等 person-fit 功效分析文献可为 benchmark size boundary 提供理论支撑。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（8 项 info 级发现，无 critical/warning）：\n\n- **Page 1**：首页纯文本无视觉锚点，Figure 1 在第 2 页（前 3 页阈值内可接受，但若能提升至第 1 页底部可增强第一印象）\n- **Pages 3-4**：连续 2 页无 display item（Method 段），仅有公式。建议添加 pipeline/framework 概念图\n- **Page 6**：Figure 2 heatmap cell 内数字字号偏小（~6-7pt），打印时可能难以辨认\n- **Page 6**：Figure 2 单色蓝梯度，色盲安全 ✓\n- **Page 7**：Figure 3 marker shape 可进一步区分以增强灰度打印可读性\n- **Page 5**：Table 1 未对最大 Cohen's d 加粗，可提升 scannability\n- **Page 8**：Figure 4 双轴设计增加认知负担，caption 解释充分\n- **Page 14**：末页内容约 60-65%，作为附录末页可接受\n\n---\n\n## Overall Assessment\n\n**评分：3.0 (Findings)**\n\n本文在 NLP-psychometrics 交叉领域做出了有意义的探索。Δℓ_z* 差分设计优雅地解决了绝对 person-fit 阈值在 LLM 上失效的核心问题，θ-shift absorption 的机制分析有洞察力，detection-diagnosis tradeoff 对实践有指导意义。8 个 Appendix 展现了扎实的方法论功底，论文定位诚实。\n\n然而，三个 Must-Fix 问题制约了评分：\n\n1. **每个污染条件仅单次运行**——这是实验设计层面的根本缺陷，使得所有定量结论（effect sizes、inverted-U 幅度、cross-model 比较）的统计基础不牢靠。多 seed 污染实验是修复路径。\n\n2. **缺少与现有方法的实证对比**——一篇声称 characterize contamination detection 的论文，不与任何专用检测方法做头对头比较，使读者无法评估 IRT person-fit 的实际价值。至少应与 ConStat 和一种 MIA 方法做 baseline 对比。\n\n3. **实验矩阵事后扩展**——inverted-U 的确认性证据源于事后添加的 25% 条件，且仅在部分模型上验证。论文的透明度是加分项，但 claim 强度需与证据独立性匹配。\n\nNovelty 存在分歧（R1: 3.5, R2: 3.0）。R1 认为经验校准对 characterization paper 有独立价值，R2 认为 findings 大部分可从 IRT 理论预测。Director 认为：当实验设计本身不够严格时，calibration 数据的可信度也受损，novelty 争议因此难以在当前版本中解决。\n\n**修复路径**：(1) 为关键条件补充 3-5 个 contaminated seeds；(2) 与 ConStat + 1 种 MIA 方法做 baseline 对比；(3) 将 inverted-U 降级为 exploratory observation。如果上述修改完成，论文有望达到 3.5（Borderline Conference），结合 framing 调整和 post-RL 精简可能达到 4.0（Conference）。当前版本推荐 Findings。\n\n---\n\n## Detailed Comments\n\n### Abstract (p.1)\n- Abstract 对实验设计的描述实际上是透明的（明确区分 \"clean seeds\" 和 \"single QLoRA run\"），这是方法论诚实的体现\n- 但 \"only binary response patterns\" 的 minimal-information framing 需突出对 PSN-IRT 4PL item bank 的核心依赖\n- Post-RL preliminary observation 可从 enumerated findings 中移除\n\n### Introduction (pp.1-2)\n- Figure 1 的 \"clean vs contaminated\" 类比有效且直观\n- \"Rather than proposing ℓ_z* as a ready-to-deploy detection tool\" 的诚实定位值得肯定\n- SFT-stage 限定（\"we focus on SFT-stage contamination\"）存在但不够突出\n\n### Related Work (pp.2-3)\n- 五类方法的覆盖系统全面\n- Person-fit 文献覆盖充分（Karabatsos 2003、Embretson & Reise 2000、Sinharay 2017）\n- 建议补充 Dong et al. (2024) 对检测方法假设的系统评估\n\n### Method (pp.3-4)\n- Δℓ_z* DiD 设计（Eq. 2）是论文最核心的方法论贡献\n- §3.2 \"DiD\" 命名不够精确——标准 DiD 需时间维度，建议改为 \"matched-difference design\"\n- §3.3 对 25% 条件事后添加的透明披露是加分项，但应进一步讨论对统计推断的影响\n- 缺少完整的 QLoRA hyperparameter table\n\n### Results (pp.5-7)\n- Table 1 的 effect sizes 全部 CI 排除零，基本检测 claim 有支撑\n- §4.2 θ-shift absorption 分析清晰，Table 2 的 free/fixed 对比有说服力\n- §4.3 detection-diagnosis tradeoff（Table 3）的 57/60 vs 4/60 对比是强经验发现\n- §4.4 inverted-U 的证据受事后扩展和单次运行限制\n\n### Discussion (pp.7-8)\n- \"Characterization over tool\" 段落定位准确\n- ConStat 对比仅用一句 \"complicated by different information requirements\" 带过，不充分\n- Post-RL 段落 + Figure 4 的空间分配需重新考虑\n\n### Limitations (p.9)\n- 简洁且涵盖主要限制，符合 EMNLP 要求\n- 应补充对 \"单次污染运行\" 和 \"无 <15% 低污染实验\" 的显式讨论\n- LD 模拟假设局限性（testlet+Gaussian 可能不代表 LLM 依赖结构）已包含，是加分项\n\n### Appendix (pp.10-14)\n- 8 个 Appendix 构成完整的鲁棒性分析体系\n- Appendix H（MML-EM 对比）是重要方法论贡献，建议在主文 §3.1 简短提及\n- Appendix G（BCa 对比）确认 percentile CI 保守，增强了主文结论的可信度"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "irt_personfit_contam",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "report": "# 审稿报告：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n\n**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n**Reviewers**: R1（方法严谨性, 3.5 Borderline Conference）、R2（新颖性/完整性, 3.0 Findings）\n**Overall Assessment**: **3.0 (Findings)**\n**Confidence**: 4/5\n\n---\n\n## Summary\n\n本文首次将心理测量学中的 IRT person-fit 统计量（ℓ_z*）系统性应用于 LLM 基准污染检测。核心思路：被污染的 LLM 类似于拥有题目预知的考生，会在难题上产生异常正确的作答模式。作者提出 Δℓ_z*（差分设计）消除 IRT 模型误设的影响，在 3 个 7-8B 模型族（Qwen2.5-7B、Llama-3.1-8B、Mistral-7B；n=10 clean seeds，Mistral n=6）× 2 个基准（MMLU 14,042 items、ARC-C 295 items）× 3-4 个污染水平（15%/25%/50%）上进行了控制实验（每个污染条件单次 QLoRA 运行）。报告三个行为边界：(1) 模型特异的 θ-shift absorption；(2) detection-diagnosis tradeoff；(3) 能力依赖的非单调剂量-效应。附带 N=1 的 post-RL preliminary observation。\n\n---\n\n## Strengths\n\n1. **新颖的跨学科桥接**：首次将教育测量学 person-fit 理论系统性引入 NLP 污染检测。\"污染 LLM ≈ 作弊考生\" 的类比自然且有启发性，开辟了 psychometrics × NLP 的新方向。[R1 AGREE, R2 AGREE]\n\n2. **Δℓ_z* 差分设计的优雅性**：绝对 ℓ_z* 在 LLM 上完全失效（57/60 cells flagged as aberrant），差分设计通过消除共享模型误设巧妙解决了这一核心障碍。Appendix F 的 local dependence 模拟进一步验证了该设计在现实依赖结构下的鲁棒性（d_ratio ≥ 0.93 for σ_τ ≤ 0.5）。[R1 AGREE, R2 AGREE]\n\n3. **θ-shift absorption 机制分析**：对 \"为什么高能力模型检测信号更弱\" 的机制解释清晰有说服力。Table 2 的 free-θ vs fixed-θ 对比（Qwen 50%: 7.6× amplification）提供了强支撑。ARC-C 的 ceiling effect 反转（高基线反而增强信号）是非教科书式的经验发现。[R1 AGREE, R2 partial AGREE]\n\n4. **诚实定位**：论文明确定位为 \"characterization\"（行为边界刻画）而非 \"tool\"（现成工具），坦承简单统计量在纯检测任务上表现更优（Table 3: accuracy z-score |d|=68.7 vs ℓ_z* |d|=1.90）。这种学术诚实在该领域少见。[R1 AGREE, R2 AGREE]\n\n5. **详尽的鲁棒性分析**：8 个 Appendix 涵盖 simulation validation、4PL vs 3PL ablation、seed sensitivity、cross-family consistency、item-level AUROC、local dependence robustness、parameter perturbation、BCa comparison、MML-EM refit。方法论严谨态度明显。[R1 AGREE, R2 AGREE]\n\n6. **Appendix H 的 MML-EM 对比**：证明 classical MML-EM 估计无法替代 PSN-IRT（r_a=0.127），为 \"为什么需要外部 item bank\" 提供了定量支撑，是重要的方法论贡献。[R2 特别肯定]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[W-MF1] 每个污染条件仅单次运行，Cohen's d 统计解释受限** [R1-N1, R2 AGREE]\n\n论文的 Cohen's d 本质上是单一污染观测值相对于 clean 分布的 one-sample z-score，而非两组分布间的标准化均差。每个污染水平（15%/25%/50%）仅训练了 1 个 QLoRA 模型，所有方差估计均来自 clean seeds。QLoRA 微调具有随机性（初始化、数据顺序、gradient noise），不同 seed 可能产生不同的 ℓ_z* 值。当前设计无法：(a) 估计污染效果的方差；(b) 判断观测到的 ℓ_z* shift 是否具有代表性。Table 1 的全部 effect sizes、inverted-U 的具体幅度（Qwen 4.3× peak-to-trough）、cross-model 比较均可能因单一运行的随机性而不稳定。\n\n*两位 Reviewer 一致认为这是最核心的实验设计缺陷。*\n\n**[W-MF2] 缺少与现有污染检测方法的实证对比** [R2-N2, R1 AGREE]\n\nTable 3 仅在自身框架内对比了 ℓ_z*、HT、accuracy z-score，完全没有与已有的专用污染检测方法（ConStat、MIA-based methods）进行头对头比较。作者拥有完整 model access（QLoRA 训练），可运行 Min-K% Prob 等 MIA 方法。Discussion 中 \"different information requirements\" 的辩护不充分——不同信息需求恰恰是应该对比的原因，读者需要知道 \"只用 binary patterns + item bank\" 相比 \"用 logits\" 损失了多少检测能力。R1 补充：论文定位为 \"characterization, not tool\"，但如果不与外部方法对比，characterization 的实际价值难以评估。\n\n**[W-MF3] 实验矩阵事后扩展构成假设确认风险** [R1-N3, R2 AGREE with severity nuance]\n\n§3.3 明确承认：\"Following initial observation of non-monotonic dose-response for Qwen, we added a 25% contamination condition.\" 这是 hypothesis-confirming data collection。Inverted-U 是论文三大核心贡献之一，但确认该发现的数据点（25%）是在看到初始结果后才添加的。虽然后续扩展到 Llama 提供了部分独立复制，但 Mistral 未测 25%。论文的透明披露是加分项，但 inverted-U 的 claim 强度与证据的独立性不匹配。R2 认为可降级为 \"observation requiring prospective confirmation\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[W-SF1] Title/framing scope mismatch** [R2-N3, R1 AGREE but downgrade]\n\n标题 \"Binary Response Patterns\" 掩盖了对 PSN-IRT 外部 item bank 的核心依赖（Appendix H 证明不用 PSN-IRT 时 r_a=0.127）。\"Benchmark Contamination\" 远宽于 SFT-stage QLoRA 实验范围。Abstract 提到 PSN-IRT 依赖但嵌在长句中不够突出。R1 认为这在 NLP 论文中常见，改标题加 \"SFT-Stage\" 限定 + Abstract 突出 item bank 依赖即可。\n\n**[W-SF2] Post-RL 观察（N=1）占据过大篇幅** [R1-W4, R2-W2, 双方 AGREE]\n\nN=1（Qwen only, GRPO, 15% MMLU）的 post-RL 观察获得了 Discussion 完整段落 + Figure 4（~0.5页），且在 Abstract 中被提及。在 8 页空间限制下，这一比重过高。两位 Reviewer 一致建议移至 Appendix。\n\n**[W-SF3] 无低污染水平（<15%）的实证实验** [R1-W1, R2 AGREE]\n\n经验实验最低污染水平为 15%，模拟（Appendix A）显示 5% 时 MMLU power 仅 47.6%。实际场景中低污染更常见，当前最低测试阈值过高。\n\n**[W-SF4] ARC-C 仅限 Qwen，跨基准泛化证据不足** [R1-W2, R2 AGREE]\n\nARC-C（295 items）仅在 Qwen 上测试。\"across three model families\" claim 的跨基准支撑仅来自 MMLU。\n\n**[W-SF5] Fixed-θ 反直觉现象缺乏解释 + 无实用决策指导** [R1-W3 + R2-W4, 双方 AGREE]\n\nTable 2 显示 Qwen 15% 时 fixed-θ 反而比 free-θ 更差（ratio=0.7×），与 \"fixed-θ recovers signal\" 的核心叙事矛盾。§4.2 末段给出定性指导但缺少操作化定义和 decision rule。\n\n**[W-SF6] 实验规模/多样性不足** [R2-W1, R1 AGREE]\n\n全部 7-8B 规模，无 1-3B/13B+/MoE 架构。仅 QLoRA SFT，无 full fine-tuning/continued pretraining。Generalization claims 超出实验覆盖。\n\n**[W-SF7] QLoRA 训练细节不足** [R1-W5, R2 partial AGREE]\n\n§3.3 仅报告 rank=16, α=32，缺 LR、epoch、batch size、数据混合方式等关键超参数。建议在 Appendix 补充完整 hyperparameter table。\n\n**[W-SF8] Mistral n=6 的 bootstrap CI 可靠性** [R1-W6, R2 AGREE]\n\nn=6 的 bootstrap CI 在统计理论上可靠性有限。BCa（Appendix G）提供了 sensitivity check，但自身在 n=6 也未必可靠。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上达成完全共识：\n\n1. **单次污染运行是最核心的实验设计缺陷**（W-MF1）——需要至少为关键条件补充多 seed 污染实验\n2. **缺少与外部方法的实证对比削弱了论文的价值定位**（W-MF2）——至少应与 1-2 种代表性方法做 baseline 比较\n3. **Post-RL N=1 应精简**（W-SF2）——移至 Appendix\n4. **Framing 应收窄以匹配实验范围**（W-SF1）——标题加 SFT-stage，Abstract 突出 PSN-IRT 依赖\n5. **实验矩阵的事后扩展降低了 inverted-U 的证据强度**（W-MF3）——应降级 claim 或补充独立验证\n\n---\n\n## Reviewer Divergence [REBUT]\n\n**[R5-D1] Novelty 评估**\n\n- **R2 立场（3.0 Findings）**：三个核心 findings 大部分可从 IRT 理论直接预测——θ-shift ceiling effect 是 well-known 的 IRT 性质，detection-diagnosis tradeoff 是 power vs. richness 的经典权衡，inverted-U 是 Finding 1 的直接推论。经验贡献主要在定量校准层面（\"useful calibration, not new insight\"）。\n\n- **R1 立场（3.5 Borderline Conference）**：承认理论方向可预测，但强调：(a) 定量结果和边界条件是新的——ARC-C ceiling effect 反转非教科书推论，57/60 vs 4/60 flagged cells 是新经验发现；(b) LLM 严重违反 IRT 假设，理论预测是否在 LLM 上成立需要经验回答；(c) \"useful calibration\" 对 characterization paper 可构成充分贡献，**前提是实验设计足够严格**（R1-N1/N3 的缺陷削弱了这一前提）。\n\n- **Director 判断**：分歧未解决，但两位 Reviewer 均同意当前实验设计不够严格，这使得 calibration 的可信度本身也受损。实验设计缺陷的修复（多 seed 运行、外部方法对比）可能间接缓解 novelty 争议——如果 calibration 数据更可靠，其独立贡献更容易被接受。\n\n---\n\n## Questions to Authors\n\n1. 如果为 Qwen 15%/50% 各训练 3-5 个不同 seed 的污染模型，预期 ℓ_z* 的 seed-level 方差有多大？是否有任何 pilot 数据估计污染效果的可重复性？\n\n2. ConStat 需要 reference benchmark 分数——你们已有 ARC-C 和 MMLU 两个 benchmark，这似乎满足了 ConStat 的最低信息需求。为什么选择不做对比？\n\n3. Table 2 中 Qwen 15% 的 fixed-θ 比 free-θ 更差（ratio=0.7×），能否提供定量解释？Snijders correction 在此处的具体影响是什么？\n\n4. PSN-IRT 校准样本（13,000+ 模型）中，估计有多大比例可能存在基准污染？Appendix F.2 的 ±10% 随机噪声能否模拟系统性污染偏差？\n\n5. 是否考虑过在 held-out 模型族（如 Phi-3、Gemma）上前瞻性验证 inverted-U？\n\n---\n\n## Missing References\n\n- **污染检测 survey**：虽然论文已引用 Chang et al. (2024) survey，但 R2 建议补充更近期的专题 survey（如 Dong et al. 2024 \"Does Data Contamination Detection Work (Well) for LLMs?\"，对检测方法假设做了系统评估，与本文的 characterization 目标直接相关）。R1 认为当前覆盖已属充分。Director 倾向于：至少补充 Dong et al. (2024)，因其对检测假设的评估与本文高度互补。\n\n- **IRT person-fit 功效分析**：Sinharay & Johnson (2017) 等 person-fit 功效分析文献可为 benchmark size boundary 提供理论支撑。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（8 项 info 级发现，无 critical/warning）：\n\n- **Page 1**：首页纯文本无视觉锚点，Figure 1 在第 2 页（前 3 页阈值内可接受，但若能提升至第 1 页底部可增强第一印象）\n- **Pages 3-4**：连续 2 页无 display item（Method 段），仅有公式。建议添加 pipeline/framework 概念图\n- **Page 6**：Figure 2 heatmap cell 内数字字号偏小（~6-7pt），打印时可能难以辨认\n- **Page 6**：Figure 2 单色蓝梯度，色盲安全 ✓\n- **Page 7**：Figure 3 marker shape 可进一步区分以增强灰度打印可读性\n- **Page 5**：Table 1 未对最大 Cohen's d 加粗，可提升 scannability\n- **Page 8**：Figure 4 双轴设计增加认知负担，caption 解释充分\n- **Page 14**：末页内容约 60-65%，作为附录末页可接受\n\n---\n\n## Overall Assessment\n\n**评分：3.0 (Findings)**\n\n本文在 NLP-psychometrics 交叉领域做出了有意义的探索。Δℓ_z* 差分设计优雅地解决了绝对 person-fit 阈值在 LLM 上失效的核心问题，θ-shift absorption 的机制分析有洞察力，detection-diagnosis tradeoff 对实践有指导意义。8 个 Appendix 展现了扎实的方法论功底，论文定位诚实。\n\n然而，三个 Must-Fix 问题制约了评分：\n\n1. **每个污染条件仅单次运行**——这是实验设计层面的根本缺陷，使得所有定量结论（effect sizes、inverted-U 幅度、cross-model 比较）的统计基础不牢靠。多 seed 污染实验是修复路径。\n\n2. **缺少与现有方法的实证对比**——一篇声称 characterize contamination detection 的论文，不与任何专用检测方法做头对头比较，使读者无法评估 IRT person-fit 的实际价值。至少应与 ConStat 和一种 MIA 方法做 baseline 对比。\n\n3. **实验矩阵事后扩展**——inverted-U 的确认性证据源于事后添加的 25% 条件，且仅在部分模型上验证。论文的透明度是加分项，但 claim 强度需与证据独立性匹配。\n\nNovelty 存在分歧（R1: 3.5, R2: 3.0）。R1 认为经验校准对 characterization paper 有独立价值，R2 认为 findings 大部分可从 IRT 理论预测。Director 认为：当实验设计本身不够严格时，calibration 数据的可信度也受损，novelty 争议因此难以在当前版本中解决。\n\n**修复路径**：(1) 为关键条件补充 3-5 个 contaminated seeds；(2) 与 ConStat + 1 种 MIA 方法做 baseline 对比；(3) 将 inverted-U 降级为 exploratory observation。如果上述修改完成，论文有望达到 3.5（Borderline Conference），结合 framing 调整和 post-RL 精简可能达到 4.0（Conference）。当前版本推荐 Findings。\n\n---\n\n## Detailed Comments\n\n### Abstract (p.1)\n- Abstract 对实验设计的描述实际上是透明的（明确区分 \"clean seeds\" 和 \"single QLoRA run\"），这是方法论诚实的体现\n- 但 \"only binary response patterns\" 的 minimal-information framing 需突出对 PSN-IRT 4PL item bank 的核心依赖\n- Post-RL preliminary observation 可从 enumerated findings 中移除\n\n### Introduction (pp.1-2)\n- Figure 1 的 \"clean vs contaminated\" 类比有效且直观\n- \"Rather than proposing ℓ_z* as a ready-to-deploy detection tool\" 的诚实定位值得肯定\n- SFT-stage 限定（\"we focus on SFT-stage contamination\"）存在但不够突出\n\n### Related Work (pp.2-3)\n- 五类方法的覆盖系统全面\n- Person-fit 文献覆盖充分（Karabatsos 2003、Embretson & Reise 2000、Sinharay 2017）\n- 建议补充 Dong et al. (2024) 对检测方法假设的系统评估\n\n### Method (pp.3-4)\n- Δℓ_z* DiD 设计（Eq. 2）是论文最核心的方法论贡献\n- §3.2 \"DiD\" 命名不够精确——标准 DiD 需时间维度，建议改为 \"matched-difference design\"\n- §3.3 对 25% 条件事后添加的透明披露是加分项，但应进一步讨论对统计推断的影响\n- 缺少完整的 QLoRA hyperparameter table\n\n### Results (pp.5-7)\n- Table 1 的 effect sizes 全部 CI 排除零，基本检测 claim 有支撑\n- §4.2 θ-shift absorption 分析清晰，Table 2 的 free/fixed 对比有说服力\n- §4.3 detection-diagnosis tradeoff（Table 3）的 57/60 vs 4/60 对比是强经验发现\n- §4.4 inverted-U 的证据受事后扩展和单次运行限制\n\n### Discussion (pp.7-8)\n- \"Characterization over tool\" 段落定位准确\n- ConStat 对比仅用一句 \"complicated by different information requirements\" 带过，不充分\n- Post-RL 段落 + Figure 4 的空间分配需重新考虑\n\n### Limitations (p.9)\n- 简洁且涵盖主要限制，符合 EMNLP 要求\n- 应补充对 \"单次污染运行\" 和 \"无 <15% 低污染实验\" 的显式讨论\n- LD 模拟假设局限性（testlet+Gaussian 可能不代表 LLM 依赖结构）已包含，是加分项\n\n### Appendix (pp.10-14)\n- 8 个 Appendix 构成完整的鲁棒性分析体系\n- Appendix H（MML-EM 对比）是重要方法论贡献，建议在主文 §3.1 简短提及\n- Appendix G（BCa 对比）确认 percentile CI 保守，增强了主文结论的可信度"
  }
}
```

</details>

---


### Tool result

_source line 588 · 2026-05-22T07:59:10.993262+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_9840a7d708128f2f1d02985bd9b8d901:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4517
}
```

</details>

---


### Assistant

_source line 589 · 2026-05-22T07:59:23.744143+00:00_

审稿报告已投递至 Research Director。

**审稿结果：3.0 (Findings)**

两位 Reviewer 经过独立初审 + 交叉分享达成以下共识：

**三个 Must-Fix**：
1. 每个污染条件仅单次运行——Cohen's d 统计基础不牢靠
2. 缺少与 ConStat/MIA 的实证对比——论文价值定位难以评估
3. 实验矩阵事后扩展——inverted-U claim 强度与证据独立性不匹配

**八个 Should-Fix**：framing scope mismatch、Post-RL N=1 篇幅过大、无 <15% 低污染实验、ARC-C 仅 Qwen、fixed-θ 反直觉现象未解释、实验规模不足、训练细节缺失、Mistral n=6 bootstrap 可靠性

**一个分歧**：Novelty 评估（R1 认为经验校准有价值 → 3.5；R2 认为 IRT 理论可预测 → 3.0）

**修复路径**：补充多 seed 污染实验 + 外部方法对比 + 降级 inverted-U claim → 有望达到 3.5-4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 60

## Round 60

2 recorded events


### User

_source line 590 · 2026-05-22T07:59:26.553587+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

**总结**：对 R1 的 9 个问题，AGREE 7 个，REBUT 1 个（N2——R1 错误引用了摘要原文，论文实际明确写的是 "clean seeds" 并在同段落披露了 "single QLoRA run"），部分保留 1 个（W5）。与 R1 的最大共识在于单次污染运行的统计限制（N1）和 post-RL 篇幅过大（W4）；最大分歧在于摘要是否具有误导性（N2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 591 · 2026-05-22T07:59:42.864930+00:00_

审稿报告已投递至 Research Director。

**最终评分：3.0 (Findings)**

圆桌审稿完成。两位 Reviewer（R1: 3.5 Borderline Conference, R2: 3.0 Findings）经交叉分享后在以下关键问题上达成共识：

1. **单次污染运行**是最核心的实验设计缺陷——所有定量结论的统计基础不牢靠
2. **缺少与 ConStat/MIA 的实证对比**——论文的 characterization 价值无法评估
3. **Inverted-U 事后确认**——25% 条件在观察到非单调性后才添加，claim 强度与证据独立性不匹配
4. **Post-RL N=1 应精简**至 Appendix
5. **Framing 应收窄**以匹配 SFT-stage QLoRA 的实际实验范围

一个分歧（novelty 评估）未解决，记录在报告中。R1-N2（摘要误导性）经 R2 用原文反驳后被排除。R2-W3（Related Work 缺 survey）经 R1 反驳后被排除。

Issue tracker 已更新至 `review_issues.yaml`（3 个 critical, 8 个 warning, 3 个 minor, 1 个 divergence）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director"
}
```

</details>

---


## Round 61

## Round 61

62 recorded events


### User

_source line 592 · 2026-05-22T22:44:32.079275+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_personfit_contam
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (via ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 593 · 2026-05-22T22:44:37.765375+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 594 · 2026-05-22T22:44:37.766138+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 595 · 2026-05-22T22:44:45.544943+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,read_local_file",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,read_local_file",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 596 · 2026-05-22T22:44:45.645733+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 597 · 2026-05-22T22:44:49.761095+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 598 · 2026-05-22T22:44:49.811700+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 599 · 2026-05-22T22:44:54.278361+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 600 · 2026-05-22T22:44:56.136941+00:00_

{"result":"# 项目 irt_personfit_contam 概况\n\n## 实验状态 (92 个)\n\n- **exp-domain-analysis**: DONE (success) — \n- **exp-ml-classifier-baseline**: DONE (success) — \n- **exp-v1-irt-refit-pilot**: DONE (negative) — \n- **exp-clean-control-delta**: DONE (success) — \n- **exp-fdr-correction**: DONE (success) — \n- **exp-cross-benchmark-analysis**: DONE (success) — \n- **exp-accuracy-zscore-baseline**: DONE (success) — \n- **exp-item-alignment-check**: DONE (negative) — \n- **exp-power-theory**: DONE (success) — \n- **exp-empirical-null**: DONE (negative) — \n- **exp-leaderboard-data-recon**: DONE (success) — \n- **exp-extended-sim**: DONE (success) — \n- **exp-two-sided**: DONE (negative) — \n- **phase_b_personfit**: DONE (success) — \n- **sim_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- eval-contam-25-s3（准备中）\n- exp-ctrl-contam-qwen-50pct-s2（准备中）\n- exp-ctrl-contam-qwen-25pct-s3（准备中）\n- exp-ctrl-contam-qwen-25pct-s2-eval（准备中）\n- eval-ctrl-contam-qwen-15pct-s2（准备中）\n- exp-arcc-benchmark: ℓz* contamination detection generalizes beyond MMLU to ARC-Challenge, a second benchmark with PSN-IRT 4PL calibration — demonstrating cross-benchmark applicability and addressing reviewer concern about single-benchmark evaluation.（准备中）\n- arcc-clean-s10（准备中）\n- arcc-clean-s9（准备中）\n- arcc-clean-s8（准备中）\n- arcc-clean-s7（准备中）\n- …另有 9 项\n\n## 近期结论\n- **exp-ctrl-contam-qwen-25pct-s2** (success): QLoRA 25% contamination with seed=123 produces a consistent lz* anomaly comparable to seed=42, demonstrating reproducibility of the inverted-U peak effect size.\n- **exp-ctrl-contam-qwen-15pct-multiseed** (success): QLoRA contamination training with different random seeds produces consistent lz* effect sizes (low inter-seed variance), demonstrating that the single-run Cohen's d values reported in the paper are representative rather than stochastic outliers. This directly addresses reviewer concern R5-N1 about single-run re
…[truncated 521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1858
}
```

</details>

---


### Tool call

_source line 601 · 2026-05-22T22:44:56.137426+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 602 · 2026-05-22T22:44:56.840281+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\usepackage{enumitem}
16	
17	\newcommand{\irtfit}{\textsc{IRT-FIT}}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{What Can Binary Response Patterns Reveal About Benchmark Contamination? \\
22	An IRT Person-Fit Characterization}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{sections/abstract}
31	\end{abstract}
32	
33	\input{sections/introduction}
34	\input{sections/related_work}
35	\input{sections/method}
36	\input{sections/results}
37	\input{sections/discussion}
38	\input{sections/conclusion}
39	
40	\input{sections/limitations}
41	
42	\section*{Reproducibility Statement}
43	Code and response data will be released upon acceptance.
44	Bootstrap confidence intervals use the percentile method with 10,000 resamples.
45	All three model families use clean baseline seeds 0--9 ($n{=}10$ per family).
46	Pre-calibrated 4PL item parameters are from the publicly available PSN-IRT item bank \citep{psnirt2026}.
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{sections/appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 603 · 2026-05-22T22:44:56.840685+00:00_

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
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 604 · 2026-05-22T22:45:03.676470+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found several results related to EMNLP 2026, though none specifically for the main conference's call for papers with ARR guid
…[truncated 1077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 6835
}
```

</details>

---


### Tool call

_source line 605 · 2026-05-22T22:45:08.494977+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-22T22:45:08.846676+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers deadline submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers deadline submission"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-22T22:45:15.480949+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers deadline submission"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on the search results, he
…[truncated 1354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 6634
}
```

</details>

---


### Tool result

_source line 608 · 2026-05-22T22:45:15.481396+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review (ARR) 2026 regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for r
…[truncated 1106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "WebSearch",
  "elapsed_ms": 6986
}
```

</details>

---


### Tool call

_source line 609 · 2026-05-22T22:45:29.935487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 610 · 2026-05-22T22:45:30.788871+00:00_

1	Benchmark contamination in Large Language Models (LLMs) undermines evaluation validity, yet most detection methods require privileged access to training data, model internals, or output probabilities.
2	We present the first systematic characterization of IRT person-fit statistics for detecting SFT-stage contamination: the framework requires only binary response patterns from the target model---no access to weights, gradients, logits, or training data---combined with externally calibrated 4PL item parameters from a large-scale item bank; diagnostic $\theta$-anchoring additionally requires a clean baseline.
3	A contaminated LLM produces aberrant response patterns analogous to a test-taker with item preknowledge.
4	Using $\ell_z^*$ in a matched-difference design ($\Delta\ell_z^*$) across three 7--8B model families ($n{=}10$ independent seeds per condition) on MMLU (14,042 items) and ARC-Challenge (295 items), we identify three behavior boundaries:
5	(1) model-specific $\theta$-shift dynamics linking baseline ability to detection sensitivity, where higher-ability models show weaker free-$\theta$ detection due to $\theta$-shift absorption;
6	(2) a detection-diagnosis tradeoff where simpler statistics yield stronger detection but lack $\ell_z^*$'s diagnostic capabilities (seen/unseen decomposition, mechanistic $\theta$-shift analysis);
7	and (3) ability-dependent non-monotonic dose-response under free-$\theta$ estimation, driven by $\theta$-shift absorption; $\theta$-anchored analysis reveals stable detection with a strong positive dose-response at higher contamination levels.
8	These findings establish when and why binary response patterns carry contamination information beyond aggregate accuracy.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-22T22:45:30.789283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 612 · 2026-05-22T22:45:31.291516+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation \citep{dodge2021, magar2022, sainz2023}.
4	As training corpora and public benchmarks both expand, the probability of overlap increases structurally \citep{jacovi2023, chang2024survey}.
5	When contamination occurs, benchmark scores no longer reflect genuine capability, undermining the primary mechanism by which the community compares and selects models.
6	
7	A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record.
8	N-gram overlap methods need the training corpus \citep{dodge2021, magar2022}.
9	Membership inference approaches require token-level probabilities \citep{minkprob2024, deng2024}.
10	Probing methods rely on crafted prompts \citep{golchin2024, oren2024}.
11	Performance-based methods require multiple test variants or output logits \citep{constat2024, codec2026}.
12	These methods form a detection frontier ordered by information access.
13	No existing method operates using only binary response patterns, without model weights, gradients, logits, or training data---though, as we show, effective detection additionally requires externally calibrated item parameters.
14	
15	In this work, we focus on SFT-stage contamination---where benchmark answers are explicitly included in fine-tuning data---for three reasons.
16	First, controlled experiments require known ground-truth contamination sets, achievable through fine-tuning with specific benchmark items.
17	Second, SFT-stage contamination is increasingly relevant as fine-tuning-as-a-service platforms proliferate, creating new pathways for benchmark data to enter training mixtures.
18	Third, SFT provides a methodologically clean setting to characterize detection boundaries before extending to noisier pretraining scenarios.
19	
…[truncated 4658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 613 · 2026-05-22T22:45:31.292025+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 614 · 2026-05-22T22:45:32.195511+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{IRT Person-Fit Framework}
5	\label{sec:framework}
6	
7	We adopt the four-parameter logistic (4PL) IRT model to characterize contamination-induced aberrance in LLM response patterns.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ difficulty, $c_i$ the lower asymptote (guessing), and $d_i$ the upper asymptote (slip).
14	Item parameters are pre-calibrated by PSN-IRT \citep{psnirt2026} from a large-scale leaderboard dataset; we use these external parameters rather than re-estimating from potentially contaminated data, since our MML-EM refit shows discrimination recovery degrades to $r_a{=}0.127$ on contaminated leaderboard data.
15	
16	Given item parameters and a binary response vector $\mathbf{x} = (x_1, \ldots, x_n)$, we compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized log-likelihood residual quantifying deviation between observed and expected response patterns.
17	The Snijders correction accounts for estimation uncertainty in $\hat{\theta}_{\text{MLE}}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null \citep{drasgow1985, snijders2001}; \citet{magis2012} provide a detailed treatment of how response model selection and ability estimation affect $\ell_z^*$.
18	Large negative $\ell_z^*$ indicates aberrant responding (unexpected failures on easy items or unexpected successes on hard items); large positive values indicate over-consistent patterns.
19	
20	\subsection{$\Delta\ell_z^*$ Matched-Difference Design}
21	\label{sec:did}
22	
23	LLM response patterns systematically violate IRT assumptions of local independence and unidimensionality.
24	In our empirical data, 57 of 60 model-benchmark cells yield $|\ell_z^*| > 1.96$ even absent contamination, renderi
…[truncated 3753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 615 · 2026-05-22T22:45:32.196016+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 616 · 2026-05-22T22:45:32.748387+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Detection Signal Across Model Families}
5	\label{sec:detection}
6	
7	Table~\ref{tab:cohens_d} presents Cohen's $d$ effect sizes for $\ell_z^*$ across three model families and two benchmarks.
8	All confidence intervals exclude zero, confirming that $\Delta\ell_z^*$ reliably separates contaminated from clean models at both contamination levels.
9	
10	On MMLU, effect sizes range from $|d|{=}1.90$ (Qwen at 50\%) to $|d|{=}8.22$ (Qwen at 25\%), with Qwen at 5\% ($|d|{=}4.15$) confirming detection at the lowest contamination level tested. Llama ($|d|{=}2.27$/$2.97$/$2.50$) and Mistral ($|d|{=}3.01$/$3.50$) fall between.
11	On ARC-C (295 items), Qwen yields $|d|{=}3.16$ at 15\% and $|d|{=}5.30$ at 50\%, demonstrating that detection remains feasible even on small benchmarks when contamination is sufficiently concentrated.
12	
13	Clean-model $\ell_z^*$ baselines diverge substantially across families: Qwen ${+}8.68$ ($\text{SD}{=}0.74$), Mistral ${+}4.02$ ($\text{SD}{=}2.05$), Llama ${+}0.29$ ($\text{SD}{=}1.45$), and ARC-C Qwen ${-}5.42$ ($\text{SD}{=}0.16$).
14	Absolute $\ell_z^*$ thresholds would produce contradictory results: Qwen's contaminated $\ell_z^*$ at 15\% (${+}3.85$) is still positive.
15	The $\Delta\ell_z^*$ design normalizes these divergent baselines: Cohen's $d$ yields comparable effect sizes ($|d|{=}1.90$--$8.22$) despite order-of-magnitude differences.
16	Figure~\ref{fig:heatmap} provides a visual summary.
17	
18	\begin{table}[t]
19	\centering
20	\caption{Cohen's $d$ for $\Delta\ell_z^*$ across model families ($n{=}10$ clean seeds, bootstrap 95\% CI, 10,000 resamples). All CIs exclude 0.}
21	\label{tab:cohens_d}
22	\footnotesize
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}llrrrr@{}}
25	\toprule
26	Model & Bench. & $d$ (5\%) [CI] & $d$ (15\%) [CI] & $d$ (25\%) [CI] & $d$ (50\%) [CI] \\
27	\midrule
28	Qwen$^{\dagger}$ & MMLU & $-4.15$ [$-9.9$, $-2.7$] & $-6.58$ [$-15.2$, $-4.5$] & $-8.22$ [$
…[truncated 14564 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 617 · 2026-05-22T22:45:32.849130+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "memory.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_personfit_contam",
    "file": "memory.md",
    "max_chars": "5000"
  }
}
```

</details>

---
