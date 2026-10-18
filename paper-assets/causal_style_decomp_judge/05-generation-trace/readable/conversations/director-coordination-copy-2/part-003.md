# Director coordination — Part 3 of 7

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/9d/9db2d5c10f518e51ec86.json)

## Round 56

### User

_source line 589 · 2026-05-21T21:18:01.055677+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性 + 实验设计）

---

## Summary

本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated content control、per-axis style rewriting 和 position-controlled pairwise comparison 检测 LLM judge 的风格偏差。核心发现有二：(1) Likert Blindspot——Likert 评分系统性地遗漏 pairwise comparison 可以检测到的风格偏差（BT 63–84%, p < 0.001 vs. Likert n.s.），在中等效应量下完全失灵（d → 0 at n=355），在较强效应量下衰减超 60%；(2) GEE 条件分解揭示 per-axis confound 结构——verbosity 为 style-dominated，formality 为 conditional，register 为 judge-dependent。实验覆盖 4 个 judge、3 个 benchmark、3 个 style axis，方法论总体较为严谨，但在 evaluator-producer confound 控制和部分统计论证上存在可修复的不足。

---

## Strengths

**S1** [方法设计] CSD 的三阶段流水线设计（rewriting → NLI gating → position-controlled comparison）逻辑清晰，每一步都有明确的 confound blocking 目标。DAG（Figure 2）的呈现方式值得肯定——明确标注了"design rationale, not a claim of perfect identification"，并在 caption 中注明 residual confounding 路径（S→Q, dashed orange），避免了 overclaim。Section 3.5 明确声明"interventional rather than formal causal evidence"且不援引 SUTVA/consistency assumptions，因果语言的校准在同类论文中属于上乘。

**S2** [统计方法层次感] 七种统计方法的 sensitivity hierarchy（Table 2）是亮点——不仅证明了 Likert Blindspot 不是特定检验的 artifact，还揭示了从 BT model 到 Wilcoxon signed-rank 的完整 sensitivity spectrum。Verbosity 轴的复制（Appendix L, Table 12）进一步确认该 pattern 在更强效应量下依然成立。100-point continuous Likert（Appendix M）排除了 scale granularity 解释，将 Blindspot 归因于 absolute vs. relative evaluation 范式差异——这是超出简单"Likert 不灵敏"结论的有价值发现。

**S3** [Cross-judge replication 的说服力] 三个 target judge（GPT-4o, Qwen3-32B, Llama-3.3-70B）涵盖 proprietary API、open 32B、open 70B 三种架构，加上 Claude Sonnet 4 作为 negative control。GEE confound structure 在三个 target judge 上的一致性（verbosity: Style OR 8–13, Orig OR < 1; formality: both significant）提升了结果的可推广性。Claude Sonnet 4 在相同 pairwise format 下检测不到 bias（BT 56.2%/54.1%, n.s.）是有力的 discriminative validity 证据。

**S4** [NLI gate 的多层验证] Threshold sensitivity sweep（11 thresholds, ≤3pp variation, Appendix E）、bimodal NLI score distribution（plateau 而非 cliff edge）、GPT-4o full-scale validation（200 decisions）、NLI-fail pair ablation（formality 反转至 41.7%, Appendix N）、以及 direction-aware vs. bidirectional gating 的 empirical justification（Appendix F）——这些构成了对 NLI gate 的系统性 robustness 检验，在同类工作中罕见。

**S5** [Blindspot 的 severity spectrum 刻画] 不仅展示了 Blindspot 的存在，还量化了其效应量依赖性：moderate bias 下完全失灵（d → 0 at n=355），stronger effects 下部分衰减（>60%）。Bootstrap attenuation 分析（Appendix J, Table 10）的 d_median = -0.017 随 n 增大 CI 收窄但始终包含零，结合 BT 稳定在 66.5%，有力区分了 measurement attenuation 和 power limitation。这是论文中分析最精细的部分。

---

## Weaknesses

**W1** [Must-Fix] **Evaluator-producer confound 控制不充分**
- 具体位置：Section 3.1, Appendix D, Limitations
- 问题：Qwen3-32B 同时担任所有实验的 rewriter，三个 target judge 全部在 Qwen3-32B 重写的文本上评估。Cross-rewriter validation（Appendix D）仅对 Qwen3-32B judge 进行了 GPT-4o rewriter 替换（verbosity: Style OR 从 13.10 降至 10.17, -22%; formality: BT 从 66.5% 降至 64.4%）。GPT-4o 和 Llama-70B 作为 judge 时，我们不知道它们检测到的"formality bias"有多少来自对 Qwen3-32B 特定重写风格的反应而非 formality 本身。22% 的 Style OR 下降（verbosity）表明 evaluator-producer 效应是 non-trivial 的。
- 为什么影响接收：这是核心 identification 问题。如果三个 judge 的"cross-judge replication"（Section 5.3）实际上部分反映了对同一 rewriter 风格的共同反应，那么 replication 的独立性被削弱。论文的 contribution #3（per-axis confound structure consistent across three architectures）的可信度取决于此。
- 建议修改方向：至少对 GPT-4o judge 执行一次完整的 cross-rewriter validation（用 GPT-4o 或 Llama 作为 rewriter），证明 confound structure 在不同 rewriter 下也一致。如果资源有限，至少对主要发现（formality + verbosity on LLMBar）做一个 rewriter 进行对比。

**W2** [Must-Fix] **Section 4.1 与 Table 1 关于 register 分类的矛盾**
- 具体位置：Section 4.1 第 8 行; Table 1 footnote
- 问题：Section 4.1 明确定义 primary family 为 8 个检验（"three judges × formality and verbosity, plus register for GPT-4o and Qwen3-32B"），但 Table 1 将 GPT-4o register 和 Qwen3 register 标记为 "†_e"（exploratory）。如果 register 在 primary family 内，Holm-Bonferroni 校正基于 8 个检验；如果在外，校正基于 6 个检验。这直接影响 adjusted p-values 和哪些结果被标记为 significant。
- 为什么影响接收：多重比较校正的不一致是方法论硬伤，审稿人和 AC 会质疑结果的 validity。
- 建议修改方向：统一分类。建议将 register 从 primary family 移出（因为 register 结果确实较弱且解释性有限），将 Section 4.1 改为 6-test primary family，或者保留 8-test family 但修正 Table 1 标注。

**W3** [Should-Fix] **TOST equivalence testing 的 Δ=15pp margin 过宽**
- 具体位置：Appendix G
- 问题：对 Claude Sonnet 4 的 equivalence testing 在 Δ=10pp 下 underpowered（n=87），在 Δ=15pp 下才 confirm equivalence。但 Δ=15pp 意味着 Claude 可以有 BT 高达 65%（15pp above 50%）仍被判定为"无偏差"。而论文将 GPT-4o formality 的 +13pp（BT 63%）认定为 genuine bias。Δ=15pp 的 equivalence zone 与最小确认偏差（+13pp）之间仅有 2pp 的 gap，discriminative power 很弱。
- 建议：(a) 明确说明在当前样本量下 TOST 的局限性；(b) 不要声称 Claude"不存在偏差"，而是说"在 Δ=15pp 精度下未检测到偏差"；(c) 增加 Claude 样本量或在 Limitations 中标记此为 open question。

**W4** [Should-Fix] **NLI gate validation 的 FNR 估计存在循环性**
- 具体位置：Section 5.1
- 问题：主要的 FNR 估计（8/95 = 8.4%）使用 Qwen3-32B 作为 LLM annotator——这与 rewriter 是同一模型。Qwen3-32B 可能系统性地认为自己的改写保留了内容（self-consistency bias）。虽然论文也提供了 GPT-4o 的 full-scale validation，但 GPT-4o validation 报告的是 precision（92.1% formality, 82.6% verbosity），而非 FNR，两个指标描述不同方向的错误。
- 建议：报告 GPT-4o validation 对应的 FNR（而非仅报告 precision），或在正文中明确标注 8.4% FNR 来自与 rewriter 相同的模型并讨论其上限/下限含义。

**W5** [Should-Fix] **Verbosity 的 direction-aware NLI gate 有 17.4% FPR**
- 具体位置：Section 5.1, Appendix F
- 问题：GPT-4o validation 显示 verbosity 的 direction-aware gate pass precision 仅 82.6%（即 17.4% 的通过 pairs 实际上内容保存失败）。在 n=86 的样本中，约 15 对可能包含 content confound。虽然 NLI ablation（Appendix N）显示 NLI-fail pairs 的 BT 仍为 75.0%——表明 verbosity bias 足够强大以 overwhelm content noise——但这也意味着 verbosity 的效应量可能被轻度高估。
- 为什么影响评分：17.4% FPR 对于一个声称"blocking the R→Q path"的 content preservation gate 来说偏高。虽然不足以否定结论，但削弱了"lower bound"的论证。
- 建议：在正文（而非仅 Appendix）中报告此 FPR 数字，并量化其对 BT 估计的 potential bias（e.g., 通过加权分析或 sensitivity analysis）。

**W6** [Should-Fix] **缺乏任何人工验证**
- 具体位置：全文
- 问题：整个流水线完全依赖自动化系统（DeBERTa for NLI, LLMs for rewriting/judging/validation）。没有任何人工评估来验证 (a) 重写是否确实只改变了目标 style axis, (b) NLI gate decisions 是否与人类判断一致, (c) pairwise preference 方向是否 align with human perception。在一篇关于 LLM judge bias 的论文中，完全依赖 LLM 进行验证存在方法论上的 irony。
- 建议：至少对 50 对 NLI gate decisions 进行人工 annotation，报告 human-NLI agreement 和 human-LLM annotator agreement。如果资源不足，在 Limitations 中明确标注此为关键局限。

**W7** [Minor] **Cross-benchmark 选择性测试**
- 具体位置：Table 1
- 问题：AlpacaEval 仅测试 3 个 judge×axis 组合，MT-Bench 仅测试 2 个。Table 1 footnote 说"cross-benchmark validation focuses on strongest-evidence configurations"，但这引入了 selection bias：只在预期效应最强的配置上做 replication，自然容易成功。缺失的组合（e.g., Llama-70B on AlpacaEval, verbosity on MT-Bench）可能提供不同的证据。
- 建议：明确列出选择标准（pre-registered or post-hoc），或将 cross-benchmark 部分明确标注为 exploratory。

**W8** [Minor] **Bradley-Terry 模型的 within-pair 依赖**
- 具体位置：Section 3.3, Section 4.1
- 问题：Position swap 产生每对 2 个观测，但 BT model 假设观测独立。Pair-level bootstrap 在 CI 估计中处理了此依赖，但 point estimate 和 p-value 来自假设独立的 BT model。论文未讨论此 violation 的影响。Sign test（仅用 consistent pairs）作为 robustness check 部分缓解了此问题。
- 建议：添加一句说明 pair-level bootstrap 如何处理 within-pair 依赖，以及为何 point estimate 的 bias 可忽略（因为 BT model 本质上在估计一个 binomial proportion）。

---

## Questions

**Q1**: Table 3 中 GPT-4o verbosity 和 GPT-4o formality 的 GEE CI 缺失（仅报告 point estimate），而其他配置有 CI。这是排版遗漏还是有意为之？如果是遗漏，请补充。

**Q2**: Section 5.2 报告 Likert tie rate 在 58–73% 之间。这些 tie rate 是否考虑了 judge 的 temperature=0 设置？如果 judge 倾向于给出相似分数（例如系统性地给 7/10），tie rate 高可能反映 judge 的 calibration 问题而非 Likert 本身的测量局限。是否尝试过分析 non-tied pairs 的 Likert 效应量？

**Q3**: 论文声明 Claude Sonnet 4 作为 negative control "detects no bias"（Abstract, Section 5.3）。但 Appendix G 的 TOST 结果显示在 Δ=10pp 下 underpowered。这两种说法之间如何调和？Claude 是"没有 bias"还是"我们无法在当前样本量下排除 moderate bias"？

**Q4**: GEE 的 Originality OR < 1 for verbosity（Table 3: 0.38–0.49）被解释为"any artifact favors rewrites over originals"（Section 5.4）。但 Orig OR < 1 也可能意味着 judge 在 verbose=original 时更倾向于选择 rewrite——这不一定是"artifact favoring rewrites"，也可能是 verbose originals 的 quality 较低。能否澄清 Originality OR 的确切语义？

**Q5**: Rewriter independence test（Appendix D）仅替换了 rewriter 而保持 Qwen3-32B 作为 judge。是否有计划或可能性测试反向配置（Qwen3-32B rewrite + GPT-4o judge vs. GPT-4o rewrite + GPT-4o judge），以完全分离 evaluator-producer 效应？

---

## Missing References

1. **Shankar et al. (2024)** "Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences" — 与本文的 meta-evaluation 视角直接相关，讨论了 LLM 评估器验证的循环性问题。

2. **Huang et al. (2024)** "Bias and Fairness in Large Language Models: A Survey" — 更广泛的 LLM bias survey，本文的 Related Work 聚焦于 judge bias 但缺少与 general LLM bias literature 的连接。

3. **Zheng et al. (2024)** "On the Limitations of LLM-as-a-Judge" (若存在此方向的综述)——更全面地讨论 LLM-as-judge 的局限性。

---

## Overall Assessment

**Overall**: **3.5** (Borderline Conference)

**一句话总结**: 方法论设计精良、统计分析层次丰富，Likert Blindspot 是对 LLM evaluation 社区有实际价值的发现，但 evaluator-producer confound 的不充分控制和缺乏人工验证削弱了核心 identification claim 的可信度。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 总体方法论严谨，GEE 分解和多层 sensitivity analysis 令人印象深刻。但 evaluator-producer confound 仅对 1/3 judge 做了 cross-rewriter 验证（W1），Section 4.1 与 Table 1 的 register 分类矛盾影响多重比较校正的可信度（W2），verbosity NLI gate 的 17.4% FPR 削弱了 content preservation claim（W5）。 |
| Excitement | 3.5/5 | Likert Blindspot 的量化对 LLM evaluation 社区有直接实践意义（特别是 RLHF/DPO pipeline 依赖 pairwise preference），per-axis confound structure 是有启发性的分析框架。但核心洞察（pairwise > Likert sensitivity）在 measurement theory 中已有理论预测，本文的贡献主要在于 empirical quantification 和 LLM 评估场景的具体化。 |
| Reproducibility | 3/5 | 方法描述详尽（Implementation Details, Appendix P），统计方法可复现（choix library, statsmodels, seed=42）。但代码和数据尚未发布（"released upon acceptance"），NLI gate 的 axis-specific thresholding 策略需要实现细节，cross-rewriter validation 的不完整性意味着部分结果难以独立验证。 |
| Confidence | 4/5 | 本审稿人在 LLM evaluation、因果推断方法论和统计建模方面有较强背景。仔细阅读了全文含全部 Appendix，对统计方法和实验设计进行了逐项检查。 |

---

## Detailed Comments（逐节）

### Title & Abstract
- 标题准确反映内容，"Likert Blindspot"命名有记忆点。
- Abstract 中"the first framework combining..."的 novelty claim 在 Related Work 中得到了合理支撑，每个组件的先行工作都有引用。
- Abstract 提到 "seven statistical methods" confirm the effect is structural——这个数字在正文中得到了完整展开（Table 2）。

### Section 1 (Introduction)
- 开篇对 style bias 问题的 motivation 清晰有力，引用了 li2026preference（76–92%）和 soumik2026judging（0.76–0.92）量化了问题的严重性。
- "no single framework integrates all four requirements"的 gap statement 合理，但"per-instance diagnostics"这个 requirement 在后续实验中体现得不够——主要结果都是 aggregate 的（BT win probability, GEE OR），per-instance diagnostic 能力（CSD 可以标记每个 pair 是否 biased）仅在 NLI gate 层面体现。
- Figure 1（pipeline diagram）清晰展示了 sample attrition，这是好的实验报告实践。

### Section 2 (Related Work)
- 结构清晰，三个 paragraph 分别覆盖 interventional approaches、measurement sensitivity、style bias detection。
- 对 RATE 的批判性分析（Likert ATE vulnerability）是有见地的，但措辞可以更 balanced——RATE 和 CSD 测量的是不同的东西（aggregate quality effect vs. per-axis style preference），直接说 RATE 的 findings "may underestimate" 需要更多 caveat。
- Bradley-Terry 段落的 positioning 清楚说明了 BT 在 evaluation 生态系统中的位置。

### Section 3 (Method)
- Style-controlled rewriting（Section 3.1）的描述清晰。Temperature 0.7 的选择未 justify——是否做过 temperature sensitivity analysis？
- NLI gate（Section 3.2）的 direction-aware 设计是 well-motivated 的 innovation。但正文中 pass rate 的变化（65% → 86%）仅给出了 verbosity 数据，formality 的 pass rate（88%）需要从 Table 1 footnote 间接推导。建议在正文直接报告各 axis 的 pass rate。
- Section 3.5 的 identification 声明是全文最精确的因果语言——值得在 abstract 中也使用类似的 calibrated language（目前 abstract 更偏 assertive）。

### Section 4 (Experiments)
- Table 1 信息密度高但可读性可改进。建议：(a) 为 Blindspot/both sig./neither 使用颜色编码而非仅符号；(b) 分离 LLMBar/AEval/MTB 为独立子表或添加水平分隔线（目前有但不够明显）。
- Holm-Bonferroni 的 family 定义（Section 4.1）需要与 Table 1 标注统一（W2）。
- Section 4.1 将 consistency filter validation 和 NLI threshold sweep 分类为"confirmatory"和"exploratory"——这个 pre-registration 式的分类值得肯定，但未说明这些分类是 pre-registered 还是 post-hoc。

### Section 5 (Analysis)
- Section 5.1（NLI Gate Validation）是全文最 thorough 的 validation 部分。Gwet's AC1 vs. Cohen's κ 的 prevalence skew 讨论表明作者对 inter-rater agreement 指标的理解深入。
- Section 5.2（Likert vs. Pairwise）的 "measurement attenuation vs. construct divergence" 双重解释框架是成熟的科学态度。但建议在 Abstract 和 Conclusion 中也保持这种 agnosticism——目前 Abstract 的措辞更偏向 "Likert misses bias"（暗示 measurement failure），而非 "Likert measures something different"。
- Section 5.2 的 detection vs. amplification 分析（6 controls bounding amplification risk）是对 Jeong et al. (2025) Comparative Trap 的直接回应，structure 清晰。但 control (ii)（Claude shows no bias）的逻辑有弱点——Claude 可能确实没有 style preference，而非 pairwise format 不 amplify。
- Section 5.6（GEE Conditional Decomposition）是重要的分析贡献。Per-axis confound structure 的 regime classification（style-dominated/conditional/judge-dependent）为后续研究提供了可操作的框架。但 regime classification 的 threshold 未明确定义——什么 Style OR / Orig OR 比值构成 "style-dominated" vs. "conditional"？

### Limitations
- 覆盖了三个关键点：(a) evaluator-producer bias, (b) validation methodology and scale, (c) NLI gate 的 identifiability limit。
- 但 Limitations 中关于 cross-rewriter validation 的说法令人困惑："All experiments use the same Qwen3-32B rewriter without the cross-rewriter validation applied to formality and verbosity (Appendix D)"——但 Appendix D 确实对 formality AND verbosity 都做了 cross-rewriter validation（Tables 6-7）。这句话的意思是其他 benchmark（AEval, MTB）上没有做 cross-rewriter validation？需要澄清。

### Appendix
- Appendix 的覆盖面令人印象深刻（A-P, 共 16 个附录项），几乎每个可能被质疑的方法论选择都有对应的 robustness check。
- Table 5（GEE CI）中 GPT-4o formality 和 GPT-4o verbosity 缺失 CI 是排版疏忽（Q1）。
- Appendix H 的 BT GOF test 和 stratified analysis 是 solid 的 model validation。Likert-tied subset analysis（formality BT=67.3%, verbosity BT=76.0%）有力排除了 originality confounding 的替代解释。

### 页数合规
主正文（Title → Conclusion）结束于第 8 页底部，Limitations 从第 9 页开始。**符合 EMNLP 2026 Long Paper 8 页限制。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 590 · 2026-05-21T21:18:11.975438+00:00_

Reviewer 1 审稿意见已收到。评分 3.5（Borderline Conference），核心关切集中在 evaluator-producer confound 控制不充分（W1, Must-Fix）和 register 分类矛盾（W2, Must-Fix）。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 57

## Round 57

2 recorded events


### User

_source line 591 · 2026-05-21T21:18:14.468250+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心结论：**Overall 3.5（Borderline Conference）**。

主要发现：
- **2 个 Must-Fix**：(1) evaluator-producer confound——Qwen3-32B 同时做 rewriter，cross-rewriter validation 仅覆盖 1/3 judge，22% Style OR 下降表明此效应 non-trivial；(2) Section 4.1 定义 8-test primary family 含 register，但 Table 1 把 register 标为 exploratory，多重比较校正不一致。
- **5 个 Should-Fix**：TOST Δ=15pp 过宽、NLI FNR 估计的循环性（Qwen3-32B 自己验证自己的改写）、verbosity gate 17.4% FPR、无任何人工验证、cross-benchmark 选择性测试。
- **优势方面**：方法设计严谨（DAG 因果语言校准好）、7 种统计方法的 sensitivity hierarchy 是亮点、cross-judge replication 覆盖 3 种架构、NLI gate 多层验证罕见、Blindspot severity spectrum 刻画精细。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 592 · 2026-05-21T21:18:20.609152+00:00_

收到 Reviewer 1 的意见。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 58

## Round 58

6 recorded events


### User

_source line 593 · 2026-05-21T21:18:32.914763+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1 (Fresh Review)

**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 扎实的实证研究，令人信服地展示了 Likert 和 pairwise 在检测 LLM judge 风格偏差上的敏感度差异，但核心发现的新颖性受限于经典心理测量学已有的理论预测，且论文框架存在系统性的过度声明。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论整体稳健，统计检验充分，多重校正恰当；但 Likert Blindspot 的因果解释存在替代假说（construct divergence），论文承认但框架和标题倾向性过强 |
| Excitement | 3/5 | 结果对实践有用，但核心发现（pairwise 比 Likert 更灵敏）可从 Thurstone (1927) 的理论直接预期；增量贡献，非范式级创新 |
| Reproducibility | 4/5 | 方法描述详尽，承诺 release 代码数据；使用公开 benchmark (LLMBar) 和标准统计工具 |
| Confidence | 4/5 | 我对 LLM-as-Judge 评估方法论和心理测量学文献较为熟悉 |

---

## Strengths

**S1. 系统性的实验设计和严谨的统计分析。** CSD pipeline 将风格控制重写、NLI 语义保留门控、位置控制的 pairwise 比较整合为一个完整框架。统计分析特别出色：Holm-Bonferroni 多重校正、七种统计方法的敏感度层次验证 (Table 2)、11 个 NLI 阈值的 sweep、bootstrap 衰减分析、4× 样本量复制 (n=355)。

**S2. 多维度的鲁棒性验证。** 对几乎每一个可能的混淆因素都做了控制：rewriter independence、NLI gate ablation、cross-judge replication (3 architectures)、cross-benchmark replication、negative control (Claude Sonnet 4)、100-point continuous scale。六个独立控制有效约束了 Comparative Trap 放大效应的风险。

**S3. GEE 条件分解揭示了 per-axis 的混淆结构差异。** Table 3 展示 verbosity 是 style-dominated (Style OR 8–13)、formality 是 conditional、register 是 judge-dependent。这是论文最具原创性的贡献。

**S4. 负对照设计增强了辨别效度。** Claude Sonnet 4 在同一 pairwise 格式下未检测到偏差，排除了"pairwise 格式本身产生虚假信号"的解释。

**S5. 论文写作的诚实性。** Limitations section 坦诚讨论了 construct divergence 替代解释、evaluator-producer bias 等问题。

---

## Must-Fix 问题

**W1 [critical] "The first framework" 声明过度。** Abstract、Introduction 中声称 CSD 是 "the first framework combining..."——这是通过组合限定词构造唯一性的策略。RATE、Qiu et al. (2025)、CASSE、FairJudge 各自覆盖了核心组件。建议改为 "a unified framework"。

**W2 [critical] "Likert Blindspot" 框架偏颇——construct divergence 替代假说被系统性弱化。** 标题和核心叙事将 Likert 框架为有缺陷，但 Section 5.2 承认 construct divergence 是同样合理的解释。更重要的是，Tripathi et al. (2025, arXiv:2504.14716) 发现 pairwise 更容易被 distractor features 操纵（flip rate 35% vs. 9%），直接挑战了将 pairwise 信号视为 ground truth 的隐含假设。建议给予 construct divergence 同等权重。

**W3 [critical] 基准多样性不足。** 主要实验在 LLMBar (n=100) 上进行。跨 benchmark 验证仅覆盖少数配置。所有实验均为英文单轮对话。样本基础 (n≤355) 不足以支撑 "systematic" 的结论。

---

## Should-Fix 问题

**W4 [warning] Abstract 信息密度过高**，7 句话中嵌入了 4 组括号内统计数据，可读性差。建议重写为两层结构。

**W5 [warning] Evaluator-producer bias 处理不充分。** 所有三个 target judge 的 rewriting 都由 Qwen3-32B 完成。Register 轴完全未做 rewriter independence 验证。

**W6 [warning] 遗漏关键近期文献：** (1) Tripathi et al. (2025) "Pairwise or Pointwise?" — 直接挑战 pairwise 信号的可靠性假设；(2) Li et al. (2026) "Grading Scale Impact on LLM-as-a-Judge" — 评分尺度对 LLM judge 的影响；(3) "Fairness or Fluency?" (arXiv:2601.13649)。

**W7 [warning] 对 Thurstone (1927) 的理论关系定位不清。** 核心发现（pairwise > Likert 的灵敏度）可从近百年前的理论直接预测。论文需更清楚地说明 LLM-specific quantification 的增量价值。

---

## Questions

Q1. 100-point 连续尺度的高 tie rate (51-66%) 是否说明 LLM judge 在绝对评分时对 style 变化确实不敏感（而非 Likert 工具有缺陷）？

Q2. AlpacaEval verbosity (Likert d=0.375, BT=84.1%) 两者均显著——Blindspot 是否仅在 moderate effect sizes 时存在？

Q3. Position-swap 后 inconsistent pair 比例是多少？是否接近 Tripathi et al. 的 35% flip rate？

Q4. 如果用不同 rewriter (如 Llama-70B)，GEE confound structure 是否保持一致？

---

## Missing References

1. Tripathi et al. (2025). "Pairwise or Pointwise?" arXiv:2504.14716
2. Li et al. (2026). "Grading Scale Impact on LLM-as-a-Judge" arXiv:2601.03444
3. "Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory" arXiv:2602.00521

---

## Format Compliance
- ✅ 主正文 8 页
- ✅ Limitations section 存在且合理
- ✅ 匿名 (Anonymous, review mode)
- ✅ natbib 引用格式
- ⚠️ Table 1 第 6 列无列标题
- ⚠️ `\usepackage{inconsolata}` 被注释掉，提交前需确认

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-21T21:19:10.542199+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "以下是 **Reviewer 1** 的完整审稿意见（侧重方法严谨性 + 实验设计）。请逐条回应其 Weaknesses 和 Questions：对每条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Summary\n本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated content control、per-axis style rewriting 和 position-controlled pairwise comparison 检测 LLM judge 的风格偏差。核心发现有二：(1) Likert Blindspot——Likert 评分系统性地遗漏 pairwise comparison 可以检测到的风格偏差（BT 63–84%, p < 0.001 vs. Likert n.s.），在中等效应量下完全失灵（d → 0 at n=355），在较强效应量下衰减超 60%；(2) GEE 条件分解揭示 per-axis confound 结构——verbosity 为 style-dominated，formality 为 conditional，register 为 judge-dependent。实验覆盖 4 个 judge、3 个 benchmark、3 个 style axis，方法论总体较为严谨，但在 evaluator-producer confound 控制和部分统计论证上存在可修复的不足。\n\n### Strengths\nS1: CSD 三阶段流水线设计逻辑清晰，DAG 标注精准，因果语言校准上乘。\nS2: 七种统计方法的 sensitivity hierarchy（Table 2）是亮点，100-point continuous Likert 排除 granularity 解释。\nS3: Cross-judge replication 覆盖三种架构 + Claude negative control 提供 discriminative validity。\nS4: NLI gate 多层验证（11-threshold sweep, GPT-4o validation, NLI-fail ablation）罕见。\nS5: Blindspot severity spectrum 刻画精细（d→0 at n=355, >60% attenuation at stronger effects）。\n\n### Weaknesses\n**W1 [Must-Fix]** Evaluator-producer confound 控制不充分——Qwen3-32B 同时做所有 rewriter，cross-rewriter validation 仅对 Qwen3-32B judge 做了 GPT-4o rewriter 替换（verbosity Style OR 降 22%），GPT-4o 和 Llama-70B judge 未做 cross-rewriter validation。\n**W2 [Must-Fix]** Section 4.1 定义 8-test primary family 含 register，但 Table 1 把 register 标为 exploratory（†_e），多重比较校正不一致。\n**W3 [Should-Fix]** TOST Δ=15pp 过宽——Claude BT 可达 65% 仍判定\"无偏差\"，与 GPT-4o formality +13pp (BT 63%) 被认定为 genuine bias 仅差 2pp。\n**W4 [Should-Fix]** NLI FNR 估计循环性——8.4% FNR 由同一 Qwen3-32B 评估。\n**W5 [Should-Fix]** Verbosity direction-aware NLI gate 有 17.4% FPR（GPT-4o validation）。\n**W6 [Should-Fix]** 全文零人工验证。\n**W7 [Minor]** Cross-benchmark 选择性测试——仅在预期效应最强的配置做 replication。\n**W8 [Minor]** BT model 的 within-pair 依赖处理未讨论。\n\n### Questions\nQ1: Table 3 GPT-4o verbosity/formality GEE CI 缺失？\nQ2: Likert 58-73% tie rate 是否反映 judge calibration 而非 Likert 局限？\nQ3: Claude \"no bias\" vs TOST Δ=10pp underpowered 如何调和？\nQ4: GEE Originality OR < 1 的确切语义？\nQ5: 是否有 Qwen3-32B rewrite + GPT-4o judge vs GPT-4o rewrite + GPT-4o judge 的计划？\n\n### Missing References\n1. Shankar et al. (2024) — LLM 评估器验证的循环性\n2. Huang et al. (2024) — LLM bias 综述\n3. Zheng et al. (2024) — LLM-as-judge 局限性\n\n---\n\n请对以上 W1-W8 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "以下是 **Reviewer 1** 的完整审稿意见（侧重方法严谨性 + 实验设计）。请逐条回应其 Weaknesses 和 Questions：对每条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Summary\n本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated content control、per-axis style rewriting 和 position-controlled pairwise comparison 检测 LLM judge 的风格偏差。核心发现有二：(1) Likert Blindspot——Likert 评分系统性地遗漏 pairwise comparison 可以检测到的风格偏差（BT 63–84%, p < 0.001 vs. Likert n.s.），在中等效应量下完全失灵（d → 0 at n=355），在较强效应量下衰减超 60%；(2) GEE 条件分解揭示 per-axis confound 结构——verbosity 为 style-dominated，formality 为 conditional，register 为 judge-dependent。实验覆盖 4 个 judge、3 个 benchmark、3 个 style axis，方法论总体较为严谨，但在 evaluator-producer confound 控制和部分统计论证上存在可修复的不足。\n\n### Strengths\nS1: CSD 三阶段流水线设计逻辑清晰，DAG 标注精准，因果语言校准上乘。\nS2: 七种统计方法的 sensitivity hierarchy（Table 2）是亮点，100-point continuous Likert 排除 granularity 解释。\nS3: Cross-judge replication 覆盖三种架构 + Claude negative control 提供 discriminative validity。\nS4: NLI gate 多层验证（11-threshold sweep, GPT-4o validation, NLI-fail ablation）罕见。\nS5: Blindspot severity spectrum 刻画精细（d→0 at n=355, >60% attenuation at stronger effects）。\n\n### Weaknesses\n**W1 [Must-Fix]** Evaluator-producer confound 控制不充分——Qwen3-32B 同时做所有 rewriter，cross-rewriter validation 仅对 Qwen3-32B judge 做了 GPT-4o rewriter 替换（verbosity Style OR 降 22%），GPT-4o 和 Llama-70B judge 未做 cross-rewriter validation。\n**W2 [Must-Fix]** Section 4.1 定义 8-test primary family 含 register，但 Table 1 把 register 标为 exploratory（†_e），多重比较校正不一致。\n**W3 [Should-Fix]** TOST Δ=15pp 过宽——Claude BT 可达 65% 仍判定\"无偏差\"，与 GPT-4o formality +13pp (BT 63%) 被认定为 genuine bias 仅差 2pp。\n**W4 [Should-Fix]** NLI FNR 估计循环性——8.4% FNR 由同一 Qwen3-32B 评估。\n**W5 [Should-Fix]** Verbosity direction-aware NLI gate 有 17.4% FPR（GPT-4o validation）。\n**W6 [Should-Fix]** 全文零人工验证。\n**W7 [Minor]** Cross-benchmark 选择性测试——仅在预期效应最强的配置做 replication。\n**W8 [Minor]** BT model 的 within-pair 依赖处理未讨论。\n\n### Questions\nQ1: Table 3 GPT-4o verbosity/formality GEE CI 缺失？\nQ2: Likert 58-73% tie rate 是否反映 judge calibration 而非 Likert 局限？\nQ3: Claude \"no bias\" vs TOST Δ=10pp underpowered 如何调和？\nQ4: GEE Originality OR < 1 的确切语义？\nQ5: 是否有 Qwen3-32B rewrite + GPT-4o judge vs GPT-4o rewrite + GPT-4o judge 的计划？\n\n### Missing References\n1. Shankar et al. (2024) — LLM 评估器验证的循环性\n2. Huang et al. (2024) — LLM bias 综述\n3. Zheng et al. (2024) — LLM-as-judge 局限性\n\n---\n\n请对以上 W1-W8 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-21T21:19:23.396125+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12853
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-21T21:19:23.749714+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "以下是 **Reviewer 2** 的完整审稿意见（侧重新颖性 + 完整性 + 写作质量）。请逐条回应其 Weaknesses 和 Questions：对每条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### 总体评分\nOverall: 3.5 (Borderline Conference)\n一句话总结: 扎实的实证研究，令人信服地展示了 Likert 和 pairwise 在检测 LLM judge 风格偏差上的敏感度差异，但核心发现的新颖性受限于经典心理测量学已有的理论预测，且论文框架存在系统性的过度声明。\n\n### Strengths\nS1: 系统性实验设计和严谨统计分析（Holm-Bonferroni, 7 methods, 11 thresholds, bootstrap attenuation, n=355 replication）\nS2: 多维度鲁棒性验证（rewriter independence, NLI ablation, cross-judge, cross-benchmark, negative control, 100-point scale）\nS3: GEE per-axis confound structure 是最具原创性贡献\nS4: Claude Sonnet 4 负对照增强辨别效度\nS5: Limitations 坦诚讨论 construct divergence 和 evaluator-producer bias\n\n### Must-Fix\n**W1 [critical]** \"The first framework\" 声明过度——通过组合限定词构造唯一性。RATE/Qiu/CASSE/FairJudge 各覆盖核心组件。建议改为 \"a unified framework\"。\n**W2 [critical]** \"Likert Blindspot\" 框架偏颇——construct divergence 替代假说被系统性弱化。Tripathi et al. (2025) 发现 pairwise 更容易被 distractor 操纵（flip rate 35% vs 9%），挑战 pairwise 作为 ground truth 的隐含假设。\n**W3 [critical]** 基准多样性不足——主要在 LLMBar n=100，跨 benchmark 仅覆盖少数配置，全部英文单轮对话，n≤355 不足以支撑 \"systematic\"。\n\n### Should-Fix\n**W4 [warning]** Abstract 信息密度过高（7 句 4 组统计括号）\n**W5 [warning]** Evaluator-producer bias 处理不充分（register 完全缺 rewriter independence）\n**W6 [warning]** 遗漏关键近期文献：Tripathi et al. (2025), Li et al. (2026), \"Fairness or Fluency?\"\n**W7 [warning]** 对 Thurstone (1927) 理论关系定位不清——核心发现可从近百年前理论直接预测\n\n### Questions\nQ1: 100-point 连续尺度高 tie rate (51-66%) 是否说明 LLM judge 对 style 变化不敏感（而非工具缺陷）？\nQ2: AlpacaEval verbosity (Likert d=0.375, BT=84.1%) 两者均显著——Blindspot 仅在 moderate effect sizes 时存在？\nQ3: Position-swap 后 inconsistent pair 比例？是否接近 Tripathi et al. 35% flip rate？\nQ4: 不同 rewriter (如 Llama-70B) 下 GEE confound structure 是否保持？\n\n### Missing References\n1. Tripathi et al. (2025) \"Pairwise or Pointwise?\" arXiv:2504.14716\n2. Li et al. (2026) \"Grading Scale Impact on LLM-as-a-Judge\" arXiv:2601.03444\n3. \"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory\" arXiv:2602.00521\n\n### Format\n- ✅ 主正文 8 页 / Limitations 存在 / 匿名 / natbib\n- ⚠️ Table 1 第 6 列无列标题\n- ⚠️ inconsolata 被注释掉\n\n---\n\n请对以上 W1-W7 和 Q1-Q4 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "以下是 **Reviewer 2** 的完整审稿意见（侧重新颖性 + 完整性 + 写作质量）。请逐条回应其 Weaknesses 和 Questions：对每条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### 总体评分\nOverall: 3.5 (Borderline Conference)\n一句话总结: 扎实的实证研究，令人信服地展示了 Likert 和 pairwise 在检测 LLM judge 风格偏差上的敏感度差异，但核心发现的新颖性受限于经典心理测量学已有的理论预测，且论文框架存在系统性的过度声明。\n\n### Strengths\nS1: 系统性实验设计和严谨统计分析（Holm-Bonferroni, 7 methods, 11 thresholds, bootstrap attenuation, n=355 replication）\nS2: 多维度鲁棒性验证（rewriter independence, NLI ablation, cross-judge, cross-benchmark, negative control, 100-point scale）\nS3: GEE per-axis confound structure 是最具原创性贡献\nS4: Claude Sonnet 4 负对照增强辨别效度\nS5: Limitations 坦诚讨论 construct divergence 和 evaluator-producer bias\n\n### Must-Fix\n**W1 [critical]** \"The first framework\" 声明过度——通过组合限定词构造唯一性。RATE/Qiu/CASSE/FairJudge 各覆盖核心组件。建议改为 \"a unified framework\"。\n**W2 [critical]** \"Likert Blindspot\" 框架偏颇——construct divergence 替代假说被系统性弱化。Tripathi et al. (2025) 发现 pairwise 更容易被 distractor 操纵（flip rate 35% vs 9%），挑战 pairwise 作为 ground truth 的隐含假设。\n**W3 [critical]** 基准多样性不足——主要在 LLMBar n=100，跨 benchmark 仅覆盖少数配置，全部英文单轮对话，n≤355 不足以支撑 \"systematic\"。\n\n### Should-Fix\n**W4 [warning]** Abstract 信息密度过高（7 句 4 组统计括号）\n**W5 [warning]** Evaluator-producer bias 处理不充分（register 完全缺 rewriter independence）\n**W6 [warning]** 遗漏关键近期文献：Tripathi et al. (2025), Li et al. (2026), \"Fairness or Fluency?\"\n**W7 [warning]** 对 Thurstone (1927) 理论关系定位不清——核心发现可从近百年前理论直接预测\n\n### Questions\nQ1: 100-point 连续尺度高 tie rate (51-66%) 是否说明 LLM judge 对 style 变化不敏感（而非工具缺陷）？\nQ2: AlpacaEval verbosity (Likert d=0.375, BT=84.1%) 两者均显著——Blindspot 仅在 moderate effect sizes 时存在？\nQ3: Position-swap 后 inconsistent pair 比例？是否接近 Tripathi et al. 35% flip rate？\nQ4: 不同 rewriter (如 Llama-70B) 下 GEE confound structure 是否保持？\n\n### Missing References\n1. Tripathi et al. (2025) \"Pairwise or Pointwise?\" arXiv:2504.14716\n2. Li et al. (2026) \"Grading Scale Impact on LLM-as-a-Judge\" arXiv:2601.03444\n3. \"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory\" arXiv:2602.00521\n\n### Format\n- ✅ 主正文 8 页 / Limitations 存在 / 匿名 / natbib\n- ⚠️ Table 1 第 6 列无列标题\n- ⚠️ inconsolata 被注释掉\n\n---\n\n请对以上 W1-W7 和 Q1-Q4 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-21T21:19:25.019250+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1269
}
```

</details>

---


### Assistant

_source line 598 · 2026-05-21T21:19:28.067630+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 59

## Round 59

2 recorded events


### User

_source line 599 · 2026-05-21T21:19:30.523390+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿总结**：给出 Overall 3.5 (Borderline Conference)。

**主要优势**：统计方法论极其严谨（七种方法交叉验证、多重鲁棒性检验）、GEE per-axis confound structure 分解有原创性、Claude 负对照设计强化了辨别效度。

**三个 Must-Fix**：
1. "The first framework" 声明过度——核心组件均有先行工作，建议改为 "a unified framework"
2. "Likert Blindspot" 框架系统性偏向 measurement failure 叙事，弱化了 construct divergence 这一同样合理的替代解释；且遗漏了 Tripathi et al. (2025) 关于 pairwise 更易被 distractor 操纵的发现
3. 基准多样性不足——主要在 LLMBar (n=100) 上做实验，跨 benchmark 验证覆盖有限

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 600 · 2026-05-21T21:19:36.873684+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 60

## Round 60

2 recorded events


### User

_source line 601 · 2026-05-21T21:21:39.910882+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### Weaknesses

**[AGREE] R2-W1: "The first framework" 声明过度**
同意 R2 的判断。Abstract line 3 和 Introduction line 12 均使用"the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison"——通过组合多个限定词构造 novelty claim 是 ACL 审稿中经常被质疑的做法。虽然该具体组合确实在已有文献中未出现（RATE 用 Likert ATE、CASSE/FairJudge 无 interventional control、Qiu et al. 在 persona 层面操作），但"first"的措辞暗示了比实际更高的原创性。改为"a unified framework"或"a framework that integrates"更准确且不影响论文实质贡献。

**[REBUT] R2-W2: "Likert Blindspot" 框架偏颇——construct divergence 被系统性弱化**
不同意 R2 的核心判断，但同意部分论据有价值。

论文并未系统性弱化 construct divergence。Section 5.2（lines 130–132）明确陈述："An equally plausible interpretation is that Likert and pairwise modes measure different constructs—absolute quality vs. ordinal preference—making the divergence a construct difference rather than measurement failure. Both interpretations lead to the same conclusion." Abstract line 7 同样并列两种解释："We identify two candidate interpretations—measurement attenuation and construct divergence—and show that both yield the same operational conclusion." Contribution #2（Introduction line 21）使用"Whether this reflects measurement attenuation or construct divergence, the operational consequence is identical."

这不是弱化，而是 agnosticism + operational equivalence 的论证策略——无论哪种解释成立，Likert-only audits 都会遗漏 pairwise-based alignment pipeline 中的 style-driven preferences。

关于 Tripathi et al. (2025) 的论据：pairwise 的 35% flip rate（vs. pointwise 9%）确实表明 pairwise 对 distractor 更敏感。但这与本文的发现不矛盾——CSD 的 6 项 amplification controls（Section 5.2, Detection vs. amplification: NLI ablation 反转、Claude negative control、cross-axis variation、GEE artifact absorption、debiased prompting、cross-architecture consistency）专门针对这一问题。特别是 control (ii) Claude Sonnet 4 在相同 pairwise format 下不检测到 bias（BT 56.2%/54.1%, n.s.），说明 pairwise format 本身不 uniformly amplify style preferences。

**建议**：Tripathi et al. (2025) 确实应该被引用和讨论——但作为对 amplification risk 的补充证据（与 Jeong et al. 2025 Comparative Trap 并列），而非对 Blindspot 的否定。

**[AGREE] R2-W3: 基准多样性不足**
同意这是论文的合理局限。LLMBar n=100 是主实验基础，cross-benchmark 仅覆盖部分配置（AlpacaEval 3/9, MT-Bench 2/9），全部英文单轮对话。论文在 Conclusion（Section 6, line 10）承认了这一点："Our findings are established on English benchmarks with n ≤ 355; validation on larger corpora, additional languages, and emerging judge architectures remains necessary."

但"systematic"一词的使用需要辩护：论文的"systematic"指的是方法论的系统性（per-axis decomposition + content control + position control），而非数据规模。在当前数据范围内，8/11 bias-positive cells 展示 Blindspot，跨 3 个 benchmark、3 个架构、3 个 style axis——这在 LLM judge bias 文献中已属较高覆盖度。但 R2 的批评在更广义的 generalization claim 层面是成立的：n ≤ 355 在绝对规模上确实有限。

**[AGREE] R2-W4: Abstract 信息密度过高**
同意。Abstract（lines 2–7）在 7 句内包含 BT 百分比范围、p-value、Cohen's d、n=355、七种统计方法、三个 judge、三个 benchmark、三个 style axis——对首次阅读的读者构成认知负担。建议将具体统计数字移至 Introduction，Abstract 聚焦于定性结论和核心 message。这是写作质量问题，不影响技术贡献。

**[AGREE] R2-W5: Evaluator-producer bias 处理不充分（register 完全缺 rewriter independence）**
同意，且此问题与我作为 R1 提出的 W1 一致。Cross-rewriter validation（Appendix D）仅覆盖 formality + verbosity 对 Qwen3-32B judge 的配置，register 轴完全缺失，GPT-4o 和 Llama-70B 作为 judge 时也缺失。这是 identification 层面的关键缺陷。

**[REBUT] R2-W6: 遗漏关键近期文献**
部分同意，部分反驳。

- **Tripathi et al. (2025)**: 同意应引用。如上述 W2 回应所述，该文对 pairwise amplification 提供了重要证据，应在 Section 5.2 的 Detection vs. amplification 段落中与 Jeong et al. (2025) 并列讨论。
- **Li et al. (2026) "Grading Scale Impact"**: 同意应引用。该文研究评分尺度对 LLM judge 的影响，与 Likert Blindspot 的 scale granularity 讨论（100-point scale, Appendix M）直接相关。
- **"Fairness or Fluency?"**: R2 未给出完整引用信息。如果是指特定的 style-fairness trade-off 论文，需要确认具体文献后再判断。

但需要指出：论文的 Related Work（Section 2）已相当全面，覆盖了 Thurstone (1927)、Stevens (1946)、Kiritchenko & Mohammad (2017)、Novikova et al. (2018)、Jeong et al. (2025) 等关键 measurement sensitivity 文献。遗漏 2–3 篇并非"系统性遗漏"。

**[REBUT] R2-W7: 对 Thurstone (1927) 理论关系定位不清——核心发现可从近百年前理论直接预测**
不同意这一批评的核心论断。

论文在 Introduction line 10 已明确标注理论渊源："a limitation predicted by measurement theory (Thurstone, 1927) but previously unquantified for LLM judges." 这不是定位不清，而是清晰的 positioning：理论预测 ≠ 经验量化。

更具体地说，Thurstone (1927) 预测 pairwise comparison 具有更高 discriminability，但未预测（也无法预测）：
1. **Severity spectrum** 的具体形态——moderate bias 下完全失灵（d → 0 at n=355）vs. stronger effects 下 >60% 衰减
2. **Tie rate mechanism**——58–73% ties 在 10-point AND 100-point scale 上同时出现，将 Blindspot 归因于 absolute vs. relative evaluation paradigm 而非 scale granularity
3. **Per-axis confound structure** 对 measurement sensitivity 的交互作用——verbosity（style-dominated）在 LLMBar 上有 Blindspot 但 AlpacaEval 上没有（BT 84.1%, d=0.375），这种效应量依赖的 threshold behavior 是全新的经验发现

类比：Newton 预测了苹果会掉落，但精确测量 g=9.81 m/s² 仍然是有价值的物理学贡献。本文的贡献不在于"pairwise 比 Likert 灵敏"这一定性结论，而在于量化了何时、多大程度、以何种机制。

---

### Questions

**[AGREE with nuance] R2-Q1: 100-point 连续尺度高 tie rate 是否说明 LLM judge 对 style 变化不敏感（而非工具缺陷）？**
这是一个好问题，但答案需要区分两种情况。100-point scale 的 tie rate（formality 65.9%, verbosity 51.2%, Appendix M Table 13）确实可能反映 LLM judge 在 absolute evaluation mode 下对 style 差异的不敏感性——即 judge 在独立评分时不会因为 formality 差异而给出不同分数。但同一个 judge 在 pairwise mode 下明确偏好 formal/verbose variants（BT 66.5%/77.3%, p < 0.0001）。这支持 construct divergence 解释：绝对评分和相对偏好测量的是不同 construct，而非"工具缺陷"。论文在 Section 5.2 line 131 已承认这一点。R2 的观察实际上强化了论文的 operational conclusion——如果 Likert insensitivity 反映的是 judge 的内在行为模式而非测量工具问题，那更说明 pairwise-based alignment pipeline 捕捉到的偏好是 Likert-based audit 无法触及的。

**[AGREE] R2-Q2: AlpacaEval verbosity (Likert d=0.375, BT=84.1%) 两者均显著——Blindspot 仅在 moderate effect sizes 时存在？**
是的，论文已明确承认这一点。Section 5.6 line 203 报告："the same verbosity axis yields a Blindspot on LLMBar (BT 77.3%, Likert n.s.) but not on AlpacaEval (BT 84.1%, d = 0.41), demonstrating a measurement sensitivity boundary rather than a methodological artifact." Table 1 的 $\ddagger$ 行标记了三个 Blindspot 不成立的 cells（BT > 69%, Likert d ≥ 0.14）。Section 5.2 lines 93–95 将此描述为 "severity spectrum"——moderate bias 下完全失灵，stronger effects 下部分衰减。论文的处理是 transparent 的，但 R2 的问题提示 Abstract 和 Conclusion 中的措辞可以更明确地限定 Blindspot 的适用条件（effect-size dependent），而非暗示它是 universal 的。

**[AGREE with data] R2-Q3: Position-swap 后 inconsistent pair 比例？是否接近 Tripathi et al. 35% flip rate？**
Appendix B（Section B, line 21）报告 position-consistency filter retains 55 of 98 valid pairs (56.1%)，即 inconsistent pair 比例为 43/98 = **43.9%**。这高于 Tripathi et al. 的 35% flip rate。但两个数字不直接可比：Tripathi 的 flip rate 来自不同实验设计（distractor manipulation），而本文的 inconsistency 来自 position swap（同一对文本交换顺序后 judge 改变选择）。43.9% 的 inconsistency rate 确实较高，可能反映 (a) position bias（论文的 position swap 旨在控制这一点），(b) style 差异处于 judge 的决策边界附近（近 50% 的 pairs 让 judge 犹豫不决）。论文应在正文中报告和讨论此数字（目前仅在 Appendix B），因为它影响对 BT model 可靠性的判断。

**[AGREE] R2-Q4: 不同 rewriter (如 Llama-70B) 下 GEE confound structure 是否保持？**
论文未测试此配置。Cross-rewriter validation（Appendix D）仅将 Qwen3-32B 替换为 GPT-4o，且仅对 Qwen3-32B judge。用 Llama-70B 作 rewriter 的数据不存在。这与我作为 R1 的 W1 一致——evaluator-producer confound 的控制覆盖面不足。GEE confound structure 的 cross-rewriter stability 是重要的 open question。

---

### Format Issues

**[AGREE] Table 1 第 6 列无列标题**
确认。Table 1（Section 4, experiments.tex lines 20–53）的第 6 列包含 Blindspot 分类符号（†, ‡, ---, †_e）但缺少列标题。建议添加"Status"或"Finding"列标题。

**[AGREE] inconsolata 被注释掉**
这是排版细节，不影响内容，但建议在最终版本中恢复或移除相关代码。

---

### 总结

R2 的审稿整体质量较高。其最有力的论点是 W2 中关于 Tripathi et al. (2025) 的引入——pairwise 的 higher flip rate 对 CSD 框架构成了需要正面回应的挑战（尽管论文的 6 项 amplification controls 已部分 address）。W7 关于 Thurstone 定位的批评我认为论文已有合理回应（Introduction line 10 明确标注"predicted but unquantified"），但 R2 的视角提示论文可以更强调经验量化的具体贡献（severity spectrum, tie rate mechanism, per-axis interaction）而非重复"first"的 framing。

与我作为 R1 的评估一致的核心问题：evaluator-producer confound（R1-W1 ≈ R2-W5）和基准多样性（R2-W3 是合理关切）。两位 reviewer 的 Must-Fix 问题有实质重叠，提示这些确实是影响接收决定的关键问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 602 · 2026-05-21T21:21:50.903426+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 61

## Round 61

2 recorded events


### User

_source line 603 · 2026-05-21T21:21:53.380643+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **W1 (first framework)**: [AGREE] — 组合限定词构造 novelty claim，改为 "a unified framework" 更合适
- **W2 (construct divergence 弱化)**: [REBUT] — 论文在 Section 5.2、Abstract、Contribution #2 三处明确并列两种解释，不构成系统性弱化；但 Tripathi et al. 应被引用
- **W3 (基准多样性)**: [AGREE] — n ≤ 355、全英文是合理局限，但论文已覆盖 3 benchmark × 3 架构 × 3 axis
- **W4 (Abstract 密度过高)**: [AGREE] — 写作建议，不影响技术贡献
- **W5 (evaluator-producer)**: [AGREE] — 与 R1-W1 一致，核心 identification 缺陷
- **W6 (遗漏文献)**: 部分同意 Tripathi 和 Li (2026) 应引用，但非"系统性遗漏"
- **W7 (Thurstone 定位)**: [REBUT] — 论文已明确标注 "predicted but unquantified"，severity spectrum 和 per-axis interaction 是全新经验发现
- **Q1–Q4**: 均提供了基于论文证据的具体回应，其中 Q3 揭示了 43.9% inconsistency rate 值得在正文讨论

两位 reviewer 的 must-fix 交集：evaluator-producer confound 控制不充分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 604 · 2026-05-21T21:21:58.531624+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 62

## Round 62

10 recorded events


### User

_source line 605 · 2026-05-21T21:22:10.813475+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条回应

---

### Weaknesses 回应

**[AGREE] R1-W1: Evaluator-producer confound 控制不充分**
同意。Appendix D (Table 5-6) 仅验证了 Qwen3-32B judge 配置。GPT-4o 和 Llama-70B judge 的结果全部依赖 Qwen3-32B rewrite，从未用替代 rewriter 验证。verbosity Style OR 降 22% (13.10→10.17) 说明 inflation 确实存在，GPT-4o formality (BT 63.0%) 作为最弱效应配置尤其需要 cross-rewriter validation。与我的 R2-W5 独立一致。

**[AGREE] R1-W2: Primary family 定义与 Table 1 标注不一致**
明确矛盾。Section 4.1 定义 "eight hypothesis tests...plus register for GPT-4o and Qwen3-32B"（register 属于 primary family），但 Table 1 将 register 标为 †_e (exploratory)。两种解读都需要修改：要么 primary family 改为 six tests，要么 register 接受 Holm-Bonferroni 校正并更新 Table 1 标记。

**[AGREE] R1-W3: TOST Δ=15pp 过宽**
同意。15pp 等价区间与 GPT-4o formality 确认偏差 +13pp 仅差 2pp。不过补充：论文核心论证不依赖 TOST——Claude 的主要价值在于 pairwise 格式不产生虚假信号 (BT 56.2%/54.1% n.s.)。建议将语言从 "equivalence confirmed" 改为 "failed to detect bias; TOST provides an upper bound"。

**[AGREE] R1-W4: NLI FNR 循环性**
部分同意。初始 FNR 8.4% 使用 Qwen3-32B annotator 确有循环风险。但论文做了 GPT-4o cross-validation (Section 5.1: 92.1% formality / 82.6% verbosity pass precision)，部分打破循环。问题在于正文突出报告了循环的 Qwen3-32B 数据而非 GPT-4o 交叉验证。建议提升 GPT-4o 验证为主要数据。

**[AGREE] R1-W5: Verbosity direction-aware NLI gate 17.4% FPR**
同意是实质性 trade-off。部分缓解因素：GEE 的 Originality OR < 1 表明内容变化方向不利于 style direction，可部分吸收 FPR 引入的噪声。

**[AGREE] R1-W6: 全文零人工验证**
完全同意。content preservation 和 style bias 验证完全依赖 LLM，涉及测量工具敏感度的论文却用同类工具验证，存在认识论问题。

**[REBUT] R1-W7: Cross-benchmark 选择性测试**
部分反驳。formality 不是最强效应（verbosity 更强），且覆盖了两个 judge 和两个额外 benchmark。真正的问题是覆盖面不足（Llama-70B 无跨 benchmark、register 无跨 benchmark），而非 cherry-picking。与我的 R2-W3 从基准多样性角度提出了更精准的批评。

**[REBUT] R1-W8: BT within-pair 依赖处理**
反驳。Section 4.1 明确使用 "pair-level resamples"（以 text pair 为单位 bootstrap），正确处理了 within-pair 依赖。BT model 自然吸收 position effects。Section 3.3 区分了 sign test（仅用 consistent pairs）和 BT（用全部观测）两种策略。

---

### Questions 回应

**[AGREE] R1-Q1**: 确认 Appendix C Table (tab:gee_ci) 中 GPT-4o verb/form/reg 和 Qwen3 form Orig OR 共 7 个 CI 缺失。必须补全。

**[AGREE] R1-Q2**: 与我的 R2-W2/R2-Q1 高度一致。58-73% tie rate（含 100-point scale 的 51-66%）支持 construct divergence 解释：judge 正确判定 style-only 变化不影响 absolute quality。论文严重弱化了这个同等合理的解释。

**[AGREE] R1-Q3**: "detects no bias" ≠ "failed to detect bias"。TOST at Δ=10pp underpowered 意味着无法排除 moderate bias 的存在。

**[REBUT] R1-Q4**: 论文已解释。Originality OR < 1 = 控制 style 后 judge 偏好 rewrite over original（rewriting artifact）。Section 5.4 + Appendix P (tab:artifact) BT P(orig) = 0.08-0.17 进一步确认。方向对 style bias 估计是保守的。

**[AGREE] R1-Q5**: GPT-4o judge 的 cross-rewriter validation 是重要缺口，特别是 GPT-4o formality (BT 63.0%) 为最弱配置。

---

### 两位 Reviewer 的共识与分歧总结

**共识（两人独立一致）**:
1. Evaluator-producer confound 是主要不足 (R1-W1 = R2-W5)
2. 零人工验证 (R1-W6 ≈ R2 隐含关注)
3. Construct divergence 解释未获同等权重 (R1-Q2 = R2-W2)
4. Benchmark 覆盖面不足 (R1-W7 ≈ R2-W3)

**R2 独立补充的关键问题**:
1. "The first framework" overclaim (R2-W1)
2. 遗漏 Tripathi et al. (2025) 等关键文献 (R2-W6)
3. Abstract 信息密度过高 (R2-W4)
4. Thurstone 理论关系定位不清 (R2-W7)

**分歧**:
- R1-W7 (selective testing): R1 认为 cherry-picking，我认为是覆盖面不足但非刻意选择
- R1-W8 (BT dependency): R1 认为未处理，我认为 pair-level bootstrap 已充分处理

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-21T21:22:33.751889+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-21T21:22:33.953206+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T21:10:47.825659+00:00\", \"completed_at\": \"2026-05-21T21:10:51.266091+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets May 25, 8am (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-21T21:22:34.104213+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-21T21:22:34.155499+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-21T21:26:47.143910+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"因果语言降级问题在 Round 3 以新形式复发，见 R3-N1\"\n      - round: 4\n        reviewers: [1]\n        note: \"R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2\"\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4-SF8: Honest novelty positioning applied.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。\"\n      - round: 7\n        reviewers: [2]\n        note: \"R2 再次指出核心发现可从 Thurstone (1927) 理论直接预测。R1 反驳称 severity spectrum 和 per-axis interaction 是全新经验发现。分歧未完全解决。\"\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Round 2 发现并修复。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Round 6 再次发现：Section 6 (Conclusion) 约 5-6 行溢出到 page 9。两位 Reviewer 共识 Must-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Round 7 两位 Reviewer 均确认主正文 8 页合规。页数问题已修复。\"\n    action_items:\n      - round: 6\n        action: \"压缩 §5.5 Register 段落（~7→3 行）+ §6 Conclusion 精简，确保主文 ≤8 页\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Independence test 仅覆盖 verbosity，formality 缺 test。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Formality rewriter independence 已补。Register 仍缺。Style OR 下降 22% 非可忽略。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R5 两位 Reviewer 均再次指出。R1 定为 critical（self-preference bias 无法排除），R2 认为 should-fix（GPT-4o 不受影响）。交叉后共识：should-fix。主文 Section 5 缺 caveat。见 R5-SF2。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix：22% OR 下降处理不充分 + register 轴完全缺失 cross-rewriter test。R6-R2 同意 22% non-trivial 但注意 Blindspot pattern 在 GPT-4o rewriter 下完全保持。共识：Must-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 独立标注为核心问题（R1-W1, R2-W5），交叉后双方 [AGREE]。cross-rewriter validation 仅覆盖 Qwen3-32B judge，GPT-4o/Llama-70B judge 未验证。22% Style OR 下降确认 inflation 存在。共识 Must-Fix。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"Register independence test — acknowledged as limitation\"\n        assigned_to: paper_agent\n        status: wont_fix\n      - round: 6\n        action: \"§5.4 加 cross-ref sentence：22% OR 下降 + NLI pass rate argument + register caveat in Limitations\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 'approximates the do-operator' 残留。见 R5-MF2。\"\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'. n=355 d->0 evidence.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"attenuation framing 已改善，但 'construct difference' 替代解释在主文中仍不足。见 R5-SF6。\"\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Cross-rewriter consistency + 200-pair GPT-4o validation provide partial proxy. Acknowledged in Limitations.\"\n      - round: 5\n        reviewers: []\n        note: \"Round 5 未被任何 Reviewer 显式提及，但仍 inherently open（无人工评估数据）。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix。R6-R2 同意但建议降级为 strong Should-Fix。交叉后共识：Must-Fix，50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 列为 Should-Fix (W6)，R7-R2 完全同意。两位 Reviewer 共识：全文零人工验证，涉及测量工具敏感度的论文却用同类工具验证，存在认识论循环。共识 Should-Fix。\"\n    action_items:\n      - round: 6\n        action: \"准备 50 对 NLI pass/fail 样本 + 标注模板，用户标注后报告 agreement + Cohen's κ\"\n        assigned_to: user\n        status: pending\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"术语已改善，但 verbosity 'confound-free' 措辞仍过强。见 R5-SF4。\"\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"引用量已改善，但遗漏了 Jeong et al. (2025) Comparative Trap 等关键文献。见 R5-MF1。\"\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"TOST at Delta=10pp underpowered (n=87). 措辞仍需更审慎。见 R5-M3。\"\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"仍指出 Abstract 信息密度过高。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均再次指出 Abstract 过密。Minor issue。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 列为 Should-Fix；R6-R1 建议降级 Minor。交叉后分歧。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 再次一致指出（R1-Detailed, R2-W4）：7 句含 4 组括号统计数据，首次阅读认知负担过重。共识 Should-Fix。\"\n    action_items:\n      - round: 7\n        action: \"将具体统计数字移至 Introduction，Abstract 聚焦定性结论和核心 message\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues (all resolved)\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    resolution: \"GoF chi2 deviance test + stratified BT + originality-minimal subset. IIA trivially satisfied in paired comparison.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再次提出 IIA 未检验，R2 技术性反驳。交叉后共识：降级 minor。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"交叉后共识：Minor。\"\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)——pairwise amplification vs detection sensitivity 张力未讨论\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 首先识别，R1 交叉完全同意。Jeong et al. (2025) 证明 pairwise 放大 style bias，与 Section 6 'adopt pairwise' 建议矛盾。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"论文已在 §2 和 §5.2 加入 Jeong et al. 讨论。但 §6 Conclusion 'should adopt' 仍过强。共识 Should-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 确认论文已在 Section 5.2 加入 6 项 amplification controls 回应 Comparative Trap。R7-R2 补充要求引用 Tripathi et al. (2025) 作为额外 amplification evidence。已从 critical 降级为 Should-Fix。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap\"\n        assigned_to: paper_agent\n        status: done\n      - round: 6\n        action: \"在 §6 Conclusion 加入 pairwise amplification caveat\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强——selection/conditioning ≠ intervention\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§3.2 原文 'approximates the do-operator' 过强。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§3.2 已改为 'filtering-based confounder control'，但 Intro/Abstract 仍用 'interventional framework'。共识 Should-Fix。\"\n      - round: 7\n        reviewers: [1]\n        note: \"R7-R1 (S1) 正面评价 §3.5 的因果语言校准（'interventional rather than formal causal evidence'，不援引 SUTVA），认为因果声明在同类论文中属上乘。原始 'do-operator' 语言已修复。\"\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"'first' 需限定到 CSD 具体方法组合的 novelty。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 Must-Fix vs R6-R1 Should-Fix。Director 判定 Should-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W1) 列为 Must-Fix：'the first framework combining...' 通过组合限定词构造唯一性。R7-R1 交叉 [AGREE]，建议改为 'a unified framework'。共识 Must-Fix。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework' 或 'a framework that integrates'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 定 critical，R2 should-fix。交叉后共识：should-fix。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RD2-SF1 涵盖此项。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1 讨论。仍为 in_progress。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Llama-70B 加入后现有 3 target judges 全部展示 Blindspot (6/6 cells + register 7/9)。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"论文已使用 'style-dominated' 而非 'confound-free'。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示——缺 verbosity 验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现严重不平衡\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"需在 §5.2 给两种解释同等篇幅。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§5.2 末尾已加入讨论段落。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W2) 列为 Must-Fix，认为框架系统性偏向 measurement failure。R7-R1 [REBUT]：论文在 Section 5.2、Abstract、Contribution #2 三处明确并列两种解释，属于 'agnosticism + operational equivalence' 论证策略。分歧：R2 认为标题和核心叙事偏颇，R1 认为已合理平衡。Director 判定：Should-Fix（标题和 Abstract 措辞可微调以减少 bias 感知，但论文实质上已提供 balanced discussion）。\"\n\n  - id: \"R5-SF7\"\n    summary: \"Formality confound 在 Abstract/Conclusion 中未与 verbosity 区分\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Abstract 和 Conclusion 中已有 per-axis differentiation。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点（0.50-0.98）。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Register 是最弱轴，恰是 rewriter identity 最可能影响结论的轴。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Acknowledged as limitation 但未补实验。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 在 evaluator-producer 讨论中再次确认 register 缺失。已在 Limitations 标注。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Equivalence bound Delta=15pp 缺外部 justification。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 Should-Fix，R6-R2 同意。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W3) 再次标注 TOST Δ=15pp 过宽（与 GPT-4o formality +13pp 仅差 2pp）。R7-R2 交叉 [AGREE] 但补充论文核心论证不依赖 TOST。共识 Should-Fix：改语言为 'failed to detect bias; TOST provides upper bound'。\"\n    action_items:\n      - round: 7\n        action: \"将 Claude 相关语言从 'equivalence confirmed' / 'no bias' 改为 'failed to detect bias at Δ=15pp precision'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"每个缺失 cell 应在 footnote 或 Appendix 说明原因。\"\n      - round: 6\n        reviewers: [2]\n        note: \"Table 1 第 6 列无 header。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 格式检查确认第 6 列仍无列标题。R7-R1 交叉 [AGREE]。\"\n    action_items:\n      - round: 7\n        action: \"Table 1 第 6 列添加列标题（如 'Status' 或 'Finding'）\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"建议颜色 + 线型双重编码。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Figure 2/3 灰度区分问题再次提及。\"\n    action_items:\n      - round: 6\n        action: \"Figure 2/3 增加颜色+线型双重编码\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025), Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound (Delta=15pp) 缺乏独立外部 justification\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"需引用外部基准设定 equivalence bound。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3 讨论。TOST Δ=15pp 与 GPT-4o formality +13pp 仅差 2pp。\"\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 讨论不充分\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1]\n        note: \"same-style control 只检测 rewriting artifact 但无法检测 axis-specific confounds。\"\n      - round: 7\n        reviewers: []\n        note: \"Round 7 未被显式提及。\"\n    action_items:\n      - round: 6\n        action: \"在 Limitations 补充讨论 axis-specific confounds\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄——n=355 仅限 Qwen3-32B formality\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"LLMBar n=100 为主数据源，MT-Bench n=30。n=355 仅覆盖一个 judge×axis。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W3) 列为 Must-Fix：全部英文单轮对话，n≤355。R7-R1 交叉 [AGREE] 但指出 8/11 bias-positive cells 展示 Blindspot 已属较高覆盖度。共识 Should-Fix（程度有分歧但方向一致）。\"\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"GPT-4o formality/verbosity/register 和 Qwen3 formality Orig OR 只有点估计无 CI。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (Q1) 和 R7-R2 交叉回应均确认 7 个 CI 缺失。必须补全。\"\n    action_items:\n      - round: 7\n        action: \"补全 Appendix Table 5 所有 GEE CI\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"非必须但高度相关。\"\n    action_items:\n      - round: 6\n        action: \"添加引用到 Related Work\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  # ============================================================\n  # Round 7 new issues\n  # ============================================================\n\n  - id: \"R7-W2\"\n    summary: \"Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 含 register (8 tests) vs Table 1 标 register 为 exploratory (†_e)\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W2) 列为 Must-Fix。R7-R2 交叉 [AGREE]：明确矛盾，直接影响 Holm-Bonferroni 校正的 adjusted p-values。需统一为 6-test 或 8-test family。\"\n    action_items:\n      - round: 7\n        action: \"统一 Section 4.1 primary family 定义与 Table 1 标注——建议将 register 移出 primary family（改为 6-test），或保留 8-test 但修正 Table 1 exploratory 标记\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R7-W4\"\n    summary: \"NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型（与 rewriter 相同），存在循环性\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W4) 提出。R7-R2 交叉部分同意：GPT-4o cross-validation 存在但仅报告 precision 而非 FNR。建议提升 GPT-4o 验证为主要数据。\"\n    action_items:\n      - round: 7\n        action: \"报告 GPT-4o validation 对应的 FNR（而非仅 precision），或在正文标注 8.4% FNR 来自 rewriter 同模型\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R7-W5\"\n    summary: \"Verbosity direction-aware NLI gate GPT-4o validation 显示 17.4% FPR，正文未报告\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W5) 提出。R7-R2 交叉 [AGREE]。GEE Orig OR < 1 可部分吸收，但 17.4% 对 content preservation claim 是实质性 trade-off。需在正文报告并量化对 BT 估计的 potential bias。\"\n    action_items:\n      - round: 7\n        action: \"在正文 Section 5.1 报告 verbosity 17.4% FPR 数字并讨论其影响\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R7-REF1\"\n    summary: \"遗漏引用：Tripathi et al. (2025) 'Pairwise or Pointwise?'——pairwise 更易被 distractor 操纵，挑战 pairwise 信号可靠性\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W6) 提出。R7-R1 交叉同意应引用，建议在 Section 5.2 Detection vs. amplification 段落与 Jeong et al. (2025) 并列讨论。两位均建议同时引用 Li et al. (2026) 'Grading Scale Impact'。\"\n    action_items:\n      - round: 7\n        action: \"在 Section 5.2 或 Related Work 引用 Tripathi et al. (2025) 和 Li et al. (2026)\"\n        assigned_to: paper_agent\n        status: pending\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"因果语言降级问题在 Round 3 以新形式复发，见 R3-N1\"\n      - round: 4\n        reviewers: [1]\n        note: \"R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2\"\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4-SF8: Honest novelty positioning applied.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。\"\n      - round: 7\n        reviewers: [2]\n        note: \"R2 再次指出核心发现可从 Thurstone (1927) 理论直接预测。R1 反驳称 severity spectrum 和 per-axis interaction 是全新经验发现。分歧未完全解决。\"\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Round 2 发现并修复。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Round 6 再次发现：Section 6 (Conclusion) 约 5-6 行溢出到 page 9。两位 Reviewer 共识 Must-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Round 7 两位 Reviewer 均确认主正文 8 页合规。页数问题已修复。\"\n    action_items:\n      - round: 6\n        action: \"压缩 §5.5 Register 段落（~7→3 行）+ §6 Conclusion 精简，确保主文 ≤8 页\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Independence test 仅覆盖 verbosity，formality 缺 test。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Formality rewriter independence 已补。Register 仍缺。Style OR 下降 22% 非可忽略。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R5 两位 Reviewer 均再次指出。R1 定为 critical（self-preference bias 无法排除），R2 认为 should-fix（GPT-4o 不受影响）。交叉后共识：should-fix。主文 Section 5 缺 caveat。见 R5-SF2。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix：22% OR 下降处理不充分 + register 轴完全缺失 cross-rewriter test。R6-R2 同意 22% non-trivial 但注意 Blindspot pattern 在 GPT-4o rewriter 下完全保持。共识：Must-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 独立标注为核心问题（R1-W1, R2-W5），交叉后双方 [AGREE]。cross-rewriter validation 仅覆盖 Qwen3-32B judge，GPT-4o/Llama-70B judge 未验证。22% Style OR 下降确认 inflation 存在。共识 Must-Fix。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"Register independence test — acknowledged as limitation\"\n        assigned_to: paper_agent\n        status: wont_fix\n      - round: 6\n        action: \"§5.4 加 cross-ref sentence：22% OR 下降 + NLI pass rate argument + register caveat in Limitations\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 'approximates the do-operator' 残留。见 R5-MF2。\"\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'. n=355 d->0 evidence.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"attenuation framing 已改善，但 'construct difference' 替代解释在主文中仍不足。见 R5-SF6。\"\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Cross-rewriter consistency + 200-pair GPT-4o validation provide partial proxy. Acknowledged in Limitations.\"\n      - round: 5\n        reviewers: []\n        note: \"Round 5 未被任何 Reviewer 显式提及，但仍 inherently open（无人工评估数据）。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix。R6-R2 同意但建议降级为 strong Should-Fix。交叉后共识：Must-Fix，50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 列为 Should-Fix (W6)，R7-R2 完全同意。两位 Reviewer 共识：全文零人工验证，涉及测量工具敏感度的论文却用同类工具验证，存在认识论循环。共识 Should-Fix。\"\n    action_items:\n      - round: 6\n        action: \"准备 50 对 NLI pass/fail 样本 + 标注模板，用户标注后报告 agreement + Cohen's κ\"\n        assigned_to: user\n        status: pending\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"术语已改善，但 verbosity 'confound-free' 措辞仍过强。见 R5-SF4。\"\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"引用量已改善，但遗漏了 Jeong et al. (2025) Comparative Trap 等关键文献。见 R5-MF1。\"\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"TOST at Delta=10pp underpowered (n=87). 措辞仍需更审慎。见 R5-M3。\"\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"仍指出 Abstract 信息密度过高。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均再次指出 Abstract 过密。Minor issue。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 列为 Should-Fix；R6-R1 建议降级 Minor。交叉后分歧。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 再次一致指出（R1-Detailed, R2-W4）：7 句含 4 组括号统计数据，首次阅读认知负担过重。共识 Should-Fix。\"\n    action_items:\n      - round: 7\n        action: \"将具体统计数字移至 Introduction，Abstract 聚焦定性结论和核心 message\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues (all resolved)\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    resolution: \"GoF chi2 deviance test + stratified BT + originality-minimal subset. IIA trivially satisfied in paired comparison.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再次提出 IIA 未检验，R2 技术性反驳。交叉后共识：降级 minor。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"交叉后共识：Minor。\"\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)——pairwise amplification vs detection sensitivity 张力未讨论\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 首先识别，R1 交叉完全同意。Jeong et al. (2025) 证明 pairwise 放大 style bias，与 Section 6 'adopt pairwise' 建议矛盾。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"论文已在 §2 和 §5.2 加入 Jeong et al. 讨论。但 §6 Conclusion 'should adopt' 仍过强。共识 Should-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 确认论文已在 Section 5.2 加入 6 项 amplification controls 回应 Comparative Trap。R7-R2 补充要求引用 Tripathi et al. (2025) 作为额外 amplification evidence。已从 critical 降级为 Should-Fix。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap\"\n        assigned_to: paper_agent\n        status: done\n      - round: 6\n        action: \"在 §6 Conclusion 加入 pairwise amplification caveat\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强——selection/conditioning ≠ intervention\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§3.2 原文 'approximates the do-operator' 过强。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§3.2 已改为 'filtering-based confounder control'，但 Intro/Abstract 仍用 'interventional framework'。共识 Should-Fix。\"\n      - round: 7\n        reviewers: [1]\n        note: \"R7-R1 (S1) 正面评价 §3.5 的因果语言校准（'interventional rather than formal causal evidence'，不援引 SUTVA），认为因果声明在同类论文中属上乘。原始 'do-operator' 语言已修复。\"\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"'first' 需限定到 CSD 具体方法组合的 novelty。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 Must-Fix vs R6-R1 Should-Fix。Director 判定 Should-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W1) 列为 Must-Fix：'the first framework combining...' 通过组合限定词构造唯一性。R7-R1 交叉 [AGREE]，建议改为 'a unified framework'。共识 Must-Fix。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework' 或 'a framework that integrates'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 定 critical，R2 should-fix。交叉后共识：should-fix。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RD2-SF1 涵盖此项。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1 讨论。仍为 in_progress。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Llama-70B 加入后现有 3 target judges 全部展示 Blindspot (6/6 cells + register 7/9)。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"论文已使用 'style-dominated' 而非 'confound-free'。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示——缺 verbosity 验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现严重不平衡\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"需在 §5.2 给两种解释同等篇幅。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§5.2 末尾已加入讨论段落。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W2) 列为 Must-Fix，认为框架系统性偏向 measurement failure。R7-R1 [REBUT]：论文在 Section 5.2、Abstract、Contribution #2 三处明确并列两种解释，属于 'agnosticism + operational equivalence' 论证策略。分歧：R2 认为标题和核心叙事偏颇，R1 认为已合理平衡。Director 判定：Should-Fix（标题和 Abstract 措辞可微调以减少 bias 感知，但论文实质上已提供 balanced discussion）。\"\n\n  - id: \"R5-SF7\"\n    summary: \"Formality confound 在 Abstract/Conclusion 中未与 verbosity 区分\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Abstract 和 Conclusion 中已有 per-axis differentiation。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点（0.50-0.98）。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Register 是最弱轴，恰是 rewriter identity 最可能影响结论的轴。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Acknowledged as limitation 但未补实验。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 在 evaluator-producer 讨论中再次确认 register 缺失。已在 Limitations 标注。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Equivalence bound Delta=15pp 缺外部 justification。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 Should-Fix，R6-R2 同意。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W3) 再次标注 TOST Δ=15pp 过宽（与 GPT-4o formality +13pp 仅差 2pp）。R7-R2 交叉 [AGREE] 但补充论文核心论证不依赖 TOST。共识 Should-Fix：改语言为 'failed to detect bias; TOST provides upper bound'。\"\n    action_items:\n      - round: 7\n        action: \"将 Claude 相关语言从 'equivalence confirmed' / 'no bias' 改为 'failed to detect bias at Δ=15pp precision'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"每个缺失 cell 应在 footnote 或 Appendix 说明原因。\"\n      - round: 6\n        reviewers: [2]\n        note: \"Table 1 第 6 列无 header。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 格式检查确认第 6 列仍无列标题。R7-R1 交叉 [AGREE]。\"\n    action_items:\n      - round: 7\n        action: \"Table 1 第 6 列添加列标题（如 'Status' 或 'Finding'）\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"建议颜色 + 线型双重编码。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Figure 2/3 灰度区分问题再次提及。\"\n    action_items:\n      - round: 6\n        action: \"Figure 2/3 增加颜色+线型双重编码\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025), Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound (Delta=15pp) 缺乏独立外部 justification\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"需引用外部基准设定 equivalence bound。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3 讨论。TOST Δ=15pp 与 GPT-4o formality +13pp 仅差 2pp。\"\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 讨论不充分\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1]\n        note: \"same-style control 只检测 rewriting artifact 但无法检测 axis-specific confounds。\"\n      - round: 7\n        reviewers: []\n        note: \"Round 7 未被显式提及。\"\n    action_items:\n      - round: 6\n        action: \"在 Limitations 补充讨论 axis-specific confounds\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄——n=355 仅限 Qwen3-32B formality\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"LLMBar n=100 为主数据源，MT-Bench n=30。n=355 仅覆盖一个 judge×axis。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W3) 列为 Must-Fix：全部英文单轮对话，n≤355。R7-R1 交叉 [AGREE] 但指出 8/11 bias-positive cells 展示 Blindspot 已属较高覆盖度。共识 Should-Fix（程度有分歧但方向一致）。\"\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"GPT-4o formality/verbosity/register 和 Qwen3 formality Orig OR 只有点估计无 CI。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (Q1) 和 R7-R2 交叉回应均确认 7 个 CI 缺失。必须补全。\"\n    action_items:\n      - round: 7\n        action: \"补全 Appendix Table 5 所有 GEE CI\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"非必须但高度相关。\"\n    action_items:\n      - round: 6\n        action: \"添加引用到 Related Work\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  # ============================================================\n  # Round 7 new issues\n  # ============================================================\n\n  - id: \"R7-W2\"\n    summary: \"Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 含 register (8 tests) vs Table 1 标 register 为 exploratory (†_e)\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W2) 列为 Must-Fix。R7-R2 交叉 [AGREE]：明确矛盾，直接影响 Holm-Bonferroni 校正的 adjusted p-values。需统一为 6-test 或 8-test family。\"\n    action_items:\n      - round: 7\n        action: \"统一 Section 4.1 primary family 定义与 Table 1 标注——建议将 register 移出 primary family（改为 6-test），或保留 8-test 但修正 Table 1 exploratory 标记\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R7-W4\"\n    summary: \"NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型（与 rewriter 相同），存在循环性\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W4) 提出。R7-R2 交叉部分同意：GPT-4o cross-validation 存在但仅报告 precision 而非 FNR。建议提升 GPT-4o 验证为主要数据。\"\n    action_items:\n      - round: 7\n        action: \"报告 GPT-4o validation 对应的 FNR（而非仅 precision），或在正文标注 8.4% FNR 来自 rewriter 同模型\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R7-W5\"\n    summary: \"Verbosity direction-aware NLI gate GPT-4o validation 显示 17.4% FPR，正文未报告\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W5) 提出。R7-R2 交叉 [AGREE]。GEE Orig OR < 1 可部分吸收，但 17.4% 对 content preservation claim 是实质性 trade-off。需在正文报告并量化对 BT 估计的 potential bias。\"\n    action_items:\n      - round: 7\n        action: \"在正文 Section 5.1 报告 verbosity 17.4% FPR 数字并讨论其影响\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R7-REF1\"\n    summary: \"遗漏引用：Tripathi et al. (2025) 'Pairwise or Pointwise?'——pairwise 更易被 distractor 操纵，挑战 pairwise 信号可靠性\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W6) 提出。R7-R1 交叉同意应引用，建议在 Section 5.2 Detection vs. amplification 段落与 Jeong et al. (2025) 并列讨论。两位均建议同时引用 Li et al. (2026) 'Grading Scale Impact'。\"\n    action_items:\n      - round: 7\n        action: \"在 Section 5.2 或 Related Work 引用 Tripathi et al. (2025) 和 Li et al. (2026)\"\n        assigned_to: paper_agent\n        status: pending\n"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-21T21:26:47.295754+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 34765}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-21T21:29:15.543662+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "report": "# 审稿报告 — Round 7 (Fresh Review)\n\n**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**Venue**: EMNLP 2026 (ARR), Long Paper\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）\n**审稿模式**: Fresh（初审）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated content control、per-axis style rewriting 和 position-controlled pairwise comparison 检测 LLM judge 的风格偏差。核心发现：(1) Likert Blindspot——Likert 评分系统性遗漏 pairwise comparison 检测到的风格偏差（BT 63–84% vs. Likert n.s.），moderate bias 下完全失灵（d→0 at n=355）；(2) GEE 条件分解揭示 per-axis confound 结构差异（verbosity: style-dominated, formality: conditional, register: judge-dependent）。实验覆盖 4 judge × 3 benchmark × 3 style axis。\n\n---\n\n## Strengths\n\n1. **方法论设计精良**：CSD 三阶段流水线（rewriting → NLI gating → position-controlled comparison）逻辑清晰，DAG 因果语言校准上乘——§3.5 明确声明\"interventional rather than formal causal evidence\"，在同类论文中属罕见的诚实定位。\n2. **统计分析层次丰富**：七种统计方法的 sensitivity hierarchy (Table 2) 系统展示了 Likert Blindspot 非特定检验的 artifact；100-point continuous Likert (Appendix M) 排除 scale granularity 解释。\n3. **GEE per-axis confound structure 分解**：Table 3 的 regime classification（style-dominated / conditional / judge-dependent）是论文最具原创性的分析贡献，为后续研究提供可操作框架。\n4. **NLI gate 多层验证**：11-threshold sweep、GPT-4o full-scale validation (200 decisions)、NLI-fail ablation (formality 反转至 41.7%)、direction-aware vs. bidirectional 对比——系统性 robustness 在同类工作中罕见。\n5. **Cross-judge replication + negative control**：3 target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B) + Claude Sonnet 4 negative control 提供了有说服力的 discriminative validity。\n6. **Blindspot severity spectrum 量化精细**：不仅证明存在，还刻画了效应量依赖性——moderate bias 完全失灵，stronger effects >60% 衰减——超出简单\"Likert 不灵敏\"结论。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. Evaluator-producer confound 控制不充分** [共识: R1-W1 = R2-W5, 双方交叉 AGREE]\n- Qwen3-32B 同时担任所有实验的 rewriter。Cross-rewriter validation (Appendix D) 仅对 Qwen3-32B judge 做了 GPT-4o rewriter 替换（verbosity Style OR 降 22%: 13.10→10.17）。GPT-4o 和 Llama-70B 作为 judge 时从未用替代 rewriter 验证。22% 下降表明 evaluator-producer 效应 non-trivial，论文的 Contribution #3（cross-architecture consistency）可信度受损。Register 轴完全缺失 cross-rewriter test。\n- **建议**: 至少对 GPT-4o judge 执行完整 cross-rewriter validation（用 GPT-4o 或 Llama 作 rewriter），证明 confound structure 在不同 rewriter 下一致。\n\n**MF2. Section 4.1 与 Table 1 关于 register 分类的矛盾** [共识: R1-W2, R2 交叉 AGREE]\n- Section 4.1 定义 primary family 为 8 tests（含 register），但 Table 1 将 register 标为 †_e (exploratory)。这直接影响 Holm-Bonferroni adjusted p-values（6-test vs 8-test family）。\n- **建议**: 统一——建议将 register 从 primary family 移出（6-test family），因为 register 结果较弱且 evaluator-producer confound 最高。\n\n**MF3. \"The first framework\" 声明过度** [共识: R2-W1, R1 交叉 AGREE]\n- Abstract/Introduction 中\"the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison\"通过组合限定词构造唯一性。RATE、CASSE、FairJudge、Qiu et al. 各覆盖核心组件。\n- **建议**: 改为\"a unified framework\"或\"a framework that integrates\"。\n\n### Should-Fix（不阻塞接收但显著改善论文）\n\n**SF1. Construct divergence 替代解释在框架层面未获同等权重** [分歧: R2 认为系统性弱化(Must-Fix), R1 REBUT 认为论文已在 §5.2/Abstract/Contribution#2 合理并列两种解释。Director 判定: Should-Fix]\n- 论文标题 \"Likert Blindspot\" 和核心叙事框架倾向 measurement failure 解释。虽然 §5.2 讨论了 construct divergence，但标题和 Abstract 的第一印象偏颇。Tripathi et al. (2025) 发现 pairwise 更易被 distractor 操纵（flip rate 35% vs 9%），对 pairwise 作为 ground truth 的隐含假设构成挑战。\n- **建议**: 在 Abstract 增加一句明确承认两种解释等权重；引用 Tripathi et al. 作为补充 evidence。\n\n**SF2. TOST Δ=15pp 过宽** [共识: R1-W3, R2 交叉 AGREE]\n- Claude Sonnet 4 的 TOST 在 Δ=10pp 下 underpowered (n=87)，在 Δ=15pp 下才 confirm equivalence。而 GPT-4o formality 确认偏差仅 +13pp (BT 63%)——与 equivalence zone 仅差 2pp。\n- **建议**: 将语言从 \"equivalence confirmed\"/\"no bias\" 改为 \"failed to detect bias; TOST provides an upper bound at Δ=15pp\"。\n\n**SF3. NLI FNR 估计存在循环性** [共识: R1-W4, R2 部分同意]\n- 主要 FNR 8.4% 使用 Qwen3-32B annotator（与 rewriter 同模型）。GPT-4o cross-validation 存在但仅报告 precision，未报告 FNR。\n- **建议**: 报告 GPT-4o validation 对应的 FNR，或将 8.4% 标注为\"upper/lower bound\"并提升 GPT-4o 验证为主要数据。\n\n**SF4. Verbosity direction-aware NLI gate 17.4% FPR** [共识: R1-W5, R2 AGREE]\n- GPT-4o validation 显示 verbosity pass precision 仅 82.6%（17.4% 通过 pairs 内容保存失败）。GEE Orig OR < 1 可部分吸收，但对 \"blocking R→Q path\" 的 content preservation claim 是实质性削弱。\n- **建议**: 在正文 §5.1 报告此 FPR 数字并量化对 BT 估计的 potential bias。\n\n**SF5. 全文零人工验证** [共识: R1-W6, R2 完全同意]\n- 整个流水线完全依赖 LLM 系统（DeBERTa NLI + LLM rewriting/judging/validation）。在一篇关于 LLM judge bias 的论文中，完全用同类工具验证存在认识论循环。\n- **建议**: 至少对 50 对 NLI gate decisions 做人工 annotation，报告 human-NLI agreement。如资源不足，在 Limitations 更明确标注此为关键局限（当前 Limitations 已部分覆盖但不够突出）。\n\n**SF6. 基准多样性不足** [共识: R2-W3, R1 AGREE]\n- 主要实验在 LLMBar (n=100) 上进行，cross-benchmark 验证仅覆盖少数配置（AlpacaEval 3/9, MT-Bench 2/9），全部英文单轮对话。n≤355 在绝对规模上有限。\n- **建议**: 在 Conclusion 更明确标注 generalizability 边界条件。\"Systematic\"指方法论系统性而非数据规模系统性——需在措辞上区分。\n\n**SF7. Abstract 信息密度过高** [共识: R1-detailed, R2-W4]\n- 7 句中嵌入 4 组括号内统计数据（BT 范围, p-value, Cohen's d, n=355），首次阅读认知负担过重。\n- **建议**: 将具体统计数字移至 Introduction，Abstract 聚焦定性结论和核心 message。\n\n**SF8. 遗漏关键近期文献** [部分共识: R2-W6, R1 同意 Tripathi 和 Li 应引用]\n- Tripathi et al. (2025) \"Pairwise or Pointwise?\" — pairwise 更易被 distractor 操纵，直接相关\n- Li et al. (2026) \"Grading Scale Impact on LLM-as-a-Judge\" — 评分尺度影响，与 Likert Blindspot 讨论相关\n- **建议**: 在 §5.2 Detection vs. amplification 段落引用 Tripathi et al. 与 Jeong et al. 并列；在 §2 或 §5.2 引用 Li et al.\n\n### Minor\n\n**M1. Cross-benchmark 选择性测试** [分歧: R1 认为 cherry-picking, R2 认为是覆盖面不足而非刻意选择]\n- 仅在预期效应最强的配置做 replication。建议明确列出选择标准或标注 cross-benchmark 为 exploratory。\n\n**M2. Table 1 第 6 列缺列标题** [共识: R1-R2]\n- 包含 Blindspot/both sig./neither 标记的列无标题。建议添加 \"Status\" 或 \"Finding\"。\n\n**M3. Appendix Table 5 (GEE CI) 7 个条目缺失 95% CI** [共识: R1-Q1, R2 AGREE]\n- GPT-4o formality/verbosity/register 和 Qwen3 formality Orig OR 仅有点估计无 CI。必须补全。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Evaluator-producer confound 是核心不足**——两位 Reviewer 独立标注为最关键问题，交叉后双方 AGREE。22% Style OR 下降确认 inflation 存在，GPT-4o/Llama-70B judge 从未做 cross-rewriter validation。\n2. **\"First framework\" overclaim 需修改**——改为 \"a unified framework\"。\n3. **零人工验证是方法论缺陷**——在一篇关于 LLM judge 评估的论文中完全依赖 LLM 验证，存在循环论证风险。\n4. **TOST 措辞过强**——\"no bias\" 应改为 \"failed to detect bias\"。\n5. **Section 4.1 vs Table 1 register 分类矛盾**——直接影响多重比较校正的可信度。\n6. **Abstract 过密**——需简化。\n\n## Reviewer Divergence [REBUT]\n\n1. **Construct divergence 的处理程度**: R2 认为论文框架系统性偏向 measurement failure（Must-Fix级别），R1 认为论文已在 §5.2、Abstract、Contribution #2 三处合理并列两种解释（Should-Fix即可）。**Director 判定**: Should-Fix——标题和核心叙事确有倾向性，但论文实质讨论已提供 balanced coverage。\n2. **Thurstone (1927) 理论关系**: R2 认为核心发现可从近百年理论直接预测（novelty ceiling），R1 反驳称 severity spectrum、tie rate mechanism、per-axis interaction 是全新经验发现。**Director 判定**: 论文已在 Introduction 标注\"predicted but unquantified\"，Excitement 评分已内化此限制（3/5 和 3.5/5）。\n3. **Cross-benchmark \"selective testing\" vs \"coverage gap\"**: R1 认为是选择性测试（cherry-picking），R2 认为是覆盖面不足但非刻意。**Director 判定**: 倾向 R2——实验覆盖确有限制但设计意图非 cherry-picking。\n\n---\n\n## Questions（需要作者回答）\n\n1. GPT-4o 和 Llama-70B 作为 judge 时，是否有计划用非 Qwen3-32B rewriter 进行验证？如有，预期时间？\n2. Section 4.1 的 primary family 是 6 还是 8 tests？register 的正式统计地位是什么？\n3. 100-point continuous scale 的高 tie rate (51-66%) 是否支持 construct divergence 解释（judge 在 absolute mode 下对 style 确实不敏感）而非 measurement tool 缺陷？\n4. Position-swap 后 43.9% inconsistency rate 为何未在正文讨论？是否影响 BT model reliability 判断？\n5. NLI FNR 的 GPT-4o 对应数字是多少？是否可以替代 Qwen3-32B 自评估的 8.4%？\n6. GEE confound structure 在不同 rewriter 下是否保持一致？是否有实验计划？\n\n---\n\n## Missing References\n\n**两位 Reviewer 共识应补充：**\n1. Tripathi et al. (2025). \"Pairwise or Pointwise? Optimizing Evaluation Approaches for LLM-as-Judge.\" arXiv:2504.14716\n2. Li et al. (2026). \"Grading Scale Impact on LLM-as-a-Judge.\" arXiv:2601.03444\n\n**单一 Reviewer 建议：**\n3. Shankar et al. (2024). \"Who Validates the Validators?\" — LLM 评估验证循环性 [R1]\n4. \"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory.\" arXiv:2602.00521 [R2]\n5. Huang et al. (2024). \"Bias and Fairness in Large Language Models: A Survey\" [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：error。** 视觉审查 Agent 因配额限制未能完成（\"You've hit your limit · resets May 25, 8am UTC\"）。无排版审查数据。用户可在配额重置后重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Overall | 3.5 | 3.5 | 3.5 |\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3/5 | 3.25/5 |\n| Reproducibility | 3/5 | 4/5 | 3.5/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合评价**：\n\n论文在方法论设计和统计分析上表现出色——七种方法的 sensitivity hierarchy、NLI gate 的多层验证、GEE per-axis confound structure 分解在同类论文中属于上乘水准。Likert Blindspot 的量化对 LLM evaluation 社区有直接实践价值。\n\n但三个 Must-Fix 问题需要关注：(1) evaluator-producer confound 的不充分控制削弱了 cross-architecture replication 的可信度；(2) primary family 定义与 Table 1 标注的矛盾是方法论硬伤；(3) \"first framework\" overclaim 需要措辞修正。前两者中 MF1 涉及补充实验（可能需要额外计算资源），MF2 和 MF3 是纯文本修改。\n\n核心 novelty 受限于经典 measurement theory 已有的理论预测（Thurstone 1927），论文的增量贡献在于 LLM judge 场景的具体量化——severity spectrum、per-axis interaction、tie rate mechanism。这足以支撑 Findings 级别接收，Conference 级别需要 MF1 的充分回应（cross-rewriter validation 覆盖至少 2/3 judges）和人工验证的补充。\n\n**可行修改路径**：\n- MF2 + MF3：纯文本修改，<1h\n- SF1-SF8：文本调整 + 补充 2 篇引用，<2h\n- MF1（cross-rewriter validation）：需额外实验，~4-8h GPU 时间\n- SF5（人工验证）：需用户标注，~1-2 天\n- M1-M3：排版修正，<30min\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"the first framework\" → \"a unified framework\" [MF3]\n- 4 组括号统计数据造成认知负担 → 保留 1-2 个核心数字，其余移至 Introduction [SF7]\n- 两种解释的并列(\"measurement attenuation and construct divergence\")处理得当\n\n### Introduction\n- Gap statement 合理但\"per-instance diagnostics\"requirement 在实验中体现不足——主要结果为 aggregate\n- Figure 1 (pipeline diagram) 清晰展示 sample attrition，好的实验报告实践\n\n### Related Work (§2)\n- 覆盖全面，Jeong et al. (2025) 已引用\n- 缺 Tripathi et al. (2025) 和 Li et al. (2026) [SF8]\n- 对 RATE 的批判性分析可更 balanced\n\n### Method (§3)\n- §3.5 因果语言校准上乘 [S1]\n- §3.2 已修改为 \"filtering-based confounder control\"，与 §3.5 hedging 一致\n- Temperature 0.7 选择未 justify\n- 各 axis pass rate 需在正文直接报告（目前需从 Table 1 footnote 间接推导）\n\n### Experiments (§4)\n- Section 4.1 primary family 定义需与 Table 1 统一 [MF2]\n- Table 1 第 6 列需添加列标题 [M2]\n- pre-registration vs post-hoc 分类值得肯定但未说明分类时点\n\n### Analysis (§5)\n- §5.1 NLI Gate Validation 最为 thorough；Gwet's AC1 vs κ 讨论专业\n- §5.2 Likert vs Pairwise 的 dual interpretation 框架成熟；6 controls 回应 Comparative Trap 结构清晰\n- §5.4 (Rewriter Independence) 覆盖面不足 [MF1]\n- §5.6 (GEE) regime classification threshold 未明确定义\n\n### Conclusion (§6)\n- \"should adopt pairwise\" 措辞仍偏强，需加 amplification risk caveat\n- Generalizability 边界需更明确\n\n### Limitations\n- 三个关键点覆盖合理\n- 可增加：人工验证缺失的显式标注、register 轴 evaluator-producer risk 的更强措辞\n\n### Format Compliance\n- ✅ 主正文 ≤ 8 页\n- ✅ Limitations section 存在\n- ✅ 匿名 (Anonymous, review mode)\n- ✅ natbib 引用格式\n- ⚠️ Table 1 第 6 列缺列标题\n- ⚠️ Appendix Table 5 缺 7 个 CI\n",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "report": "# 审稿报告 — Round 7 (Fresh Review)\n\n**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**Venue**: EMNLP 2026 (ARR), Long Paper\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）\n**审稿模式**: Fresh（初审）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated content control、per-axis style rewriting 和 position-controlled pairwise comparison 检测 LLM judge 的风格偏差。核心发现：(1) Likert Blindspot——Likert 评分系统性遗漏 pairwise comparison 检测到的风格偏差（BT 63–84% vs. Likert n.s.），moderate bias 下完全失灵（d→0 at n=355）；(2) GEE 条件分解揭示 per-axis confound 结构差异（verbosity: style-dominated, formality: conditional, register: judge-dependent）。实验覆盖 4 judge × 3 benchmark × 3 style axis。\n\n---\n\n## Strengths\n\n1. **方法论设计精良**：CSD 三阶段流水线（rewriting → NLI gating → position-controlled comparison）逻辑清晰，DAG 因果语言校准上乘——§3.5 明确声明\"interventional rather than formal causal evidence\"，在同类论文中属罕见的诚实定位。\n2. **统计分析层次丰富**：七种统计方法的 sensitivity hierarchy (Table 2) 系统展示了 Likert Blindspot 非特定检验的 artifact；100-point continuous Likert (Appendix M) 排除 scale granularity 解释。\n3. **GEE per-axis confound structure 分解**：Table 3 的 regime classification（style-dominated / conditional / judge-dependent）是论文最具原创性的分析贡献，为后续研究提供可操作框架。\n4. **NLI gate 多层验证**：11-threshold sweep、GPT-4o full-scale validation (200 decisions)、NLI-fail ablation (formality 反转至 41.7%)、direction-aware vs. bidirectional 对比——系统性 robustness 在同类工作中罕见。\n5. **Cross-judge replication + negative control**：3 target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B) + Claude Sonnet 4 negative control 提供了有说服力的 discriminative validity。\n6. **Blindspot severity spectrum 量化精细**：不仅证明存在，还刻画了效应量依赖性——moderate bias 完全失灵，stronger effects >60% 衰减——超出简单\"Likert 不灵敏\"结论。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. Evaluator-producer confound 控制不充分** [共识: R1-W1 = R2-W5, 双方交叉 AGREE]\n- Qwen3-32B 同时担任所有实验的 rewriter。Cross-rewriter validation (Appendix D) 仅对 Qwen3-32B judge 做了 GPT-4o rewriter 替换（verbosity Style OR 降 22%: 13.10→10.17）。GPT-4o 和 Llama-70B 作为 judge 时从未用替代 rewriter 验证。22% 下降表明 evaluator-producer 效应 non-trivial，论文的 Contribution #3（cross-architecture consistency）可信度受损。Register 轴完全缺失 cross-rewriter test。\n- **建议**: 至少对 GPT-4o judge 执行完整 cross-rewriter validation（用 GPT-4o 或 Llama 作 rewriter），证明 confound structure 在不同 rewriter 下一致。\n\n**MF2. Section 4.1 与 Table 1 关于 register 分类的矛盾** [共识: R1-W2, R2 交叉 AGREE]\n- Section 4.1 定义 primary family 为 8 tests（含 register），但 Table 1 将 register 标为 †_e (exploratory)。这直接影响 Holm-Bonferroni adjusted p-values（6-test vs 8-test family）。\n- **建议**: 统一——建议将 register 从 primary family 移出（6-test family），因为 register 结果较弱且 evaluator-producer confound 最高。\n\n**MF3. \"The first framework\" 声明过度** [共识: R2-W1, R1 交叉 AGREE]\n- Abstract/Introduction 中\"the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison\"通过组合限定词构造唯一性。RATE、CASSE、FairJudge、Qiu et al. 各覆盖核心组件。\n- **建议**: 改为\"a unified framework\"或\"a framework that integrates\"。\n\n### Should-Fix（不阻塞接收但显著改善论文）\n\n**SF1. Construct divergence 替代解释在框架层面未获同等权重** [分歧: R2 认为系统性弱化(Must-Fix), R1 REBUT 认为论文已在 §5.2/Abstract/Contribution#2 合理并列两种解释。Director 判定: Should-Fix]\n- 论文标题 \"Likert Blindspot\" 和核心叙事框架倾向 measurement failure 解释。虽然 §5.2 讨论了 construct divergence，但标题和 Abstract 的第一印象偏颇。Tripathi et al. (2025) 发现 pairwise 更易被 distractor 操纵（flip rate 35% vs 9%），对 pairwise 作为 ground truth 的隐含假设构成挑战。\n- **建议**: 在 Abstract 增加一句明确承认两种解释等权重；引用 Tripathi et al. 作为补充 evidence。\n\n**SF2. TOST Δ=15pp 过宽** [共识: R1-W3, R2 交叉 AGREE]\n- Claude Sonnet 4 的 TOST 在 Δ=10pp 下 underpowered (n=87)，在 Δ=15pp 下才 confirm equivalence。而 GPT-4o formality 确认偏差仅 +13pp (BT 63%)——与 equivalence zone 仅差 2pp。\n- **建议**: 将语言从 \"equivalence confirmed\"/\"no bias\" 改为 \"failed to detect bias; TOST provides an upper bound at Δ=15pp\"。\n\n**SF3. NLI FNR 估计存在循环性** [共识: R1-W4, R2 部分同意]\n- 主要 FNR 8.4% 使用 Qwen3-32B annotator（与 rewriter 同模型）。GPT-4o cross-validation 存在但仅报告 precision，未报告 FNR。\n- **建议**: 报告 GPT-4o validation 对应的 FNR，或将 8.4% 标注为\"upper/lower bound\"并提升 GPT-4o 验证为主要数据。\n\n**SF4. Verbosity direction-aware NLI gate 17.4% FPR** [共识: R1-W5, R2 AGREE]\n- GPT-4o validation 显示 verbosity pass precision 仅 82.6%（17.4% 通过 pairs 内容保存失败）。GEE Orig OR < 1 可部分吸收，但对 \"blocking R→Q path\" 的 content preservation claim 是实质性削弱。\n- **建议**: 在正文 §5.1 报告此 FPR 数字并量化对 BT 估计的 potential bias。\n\n**SF5. 全文零人工验证** [共识: R1-W6, R2 完全同意]\n- 整个流水线完全依赖 LLM 系统（DeBERTa NLI + LLM rewriting/judging/validation）。在一篇关于 LLM judge bias 的论文中，完全用同类工具验证存在认识论循环。\n- **建议**: 至少对 50 对 NLI gate decisions 做人工 annotation，报告 human-NLI agreement。如资源不足，在 Limitations 更明确标注此为关键局限（当前 Limitations 已部分覆盖但不够突出）。\n\n**SF6. 基准多样性不足** [共识: R2-W3, R1 AGREE]\n- 主要实验在 LLMBar (n=100) 上进行，cross-benchmark 验证仅覆盖少数配置（AlpacaEval 3/9, MT-Bench 2/9），全部英文单轮对话。n≤355 在绝对规模上有限。\n- **建议**: 在 Conclusion 更明确标注 generalizability 边界条件。\"Systematic\"指方法论系统性而非数据规模系统性——需在措辞上区分。\n\n**SF7. Abstract 信息密度过高** [共识: R1-detailed, R2-W4]\n- 7 句中嵌入 4 组括号内统计数据（BT 范围, p-value, Cohen's d, n=355），首次阅读认知负担过重。\n- **建议**: 将具体统计数字移至 Introduction，Abstract 聚焦定性结论和核心 message。\n\n**SF8. 遗漏关键近期文献** [部分共识: R2-W6, R1 同意 Tripathi 和 Li 应引用]\n- Tripathi et al. (2025) \"Pairwise or Pointwise?\" — pairwise 更易被 distractor 操纵，直接相关\n- Li et al. (2026) \"Grading Scale Impact on LLM-as-a-Judge\" — 评分尺度影响，与 Likert Blindspot 讨论相关\n- **建议**: 在 §5.2 Detection vs. amplification 段落引用 Tripathi et al. 与 Jeong et al. 并列；在 §2 或 §5.2 引用 Li et al.\n\n### Minor\n\n**M1. Cross-benchmark 选择性测试** [分歧: R1 认为 cherry-picking, R2 认为是覆盖面不足而非刻意选择]\n- 仅在预期效应最强的配置做 replication。建议明确列出选择标准或标注 cross-benchmark 为 exploratory。\n\n**M2. Table 1 第 6 列缺列标题** [共识: R1-R2]\n- 包含 Blindspot/both sig./neither 标记的列无标题。建议添加 \"Status\" 或 \"Finding\"。\n\n**M3. Appendix Table 5 (GEE CI) 7 个条目缺失 95% CI** [共识: R1-Q1, R2 AGREE]\n- GPT-4o formality/verbosity/register 和 Qwen3 formality Orig OR 仅有点估计无 CI。必须补全。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Evaluator-producer confound 是核心不足**——两位 Reviewer 独立标注为最关键问题，交叉后双方 AGREE。22% Style OR 下降确认 inflation 存在，GPT-4o/Llama-70B judge 从未做 cross-rewriter validation。\n2. **\"First framework\" overclaim 需修改**——改为 \"a unified framework\"。\n3. **零人工验证是方法论缺陷**——在一篇关于 LLM judge 评估的论文中完全依赖 LLM 验证，存在循环论证风险。\n4. **TOST 措辞过强**——\"no bias\" 应改为 \"failed to detect bias\"。\n5. **Section 4.1 vs Table 1 register 分类矛盾**——直接影响多重比较校正的可信度。\n6. **Abstract 过密**——需简化。\n\n## Reviewer Divergence [REBUT]\n\n1. **Construct divergence 的处理程度**: R2 认为论文框架系统性偏向 measurement failure（Must-Fix级别），R1 认为论文已在 §5.2、Abstract、Contribution #2 三处合理并列两种解释（Should-Fix即可）。**Director 判定**: Should-Fix——标题和核心叙事确有倾向性，但论文实质讨论已提供 balanced coverage。\n2. **Thurstone (1927) 理论关系**: R2 认为核心发现可从近百年理论直接预测（novelty ceiling），R1 反驳称 severity spectrum、tie rate mechanism、per-axis interaction 是全新经验发现。**Director 判定**: 论文已在 Introduction 标注\"predicted but unquantified\"，Excitement 评分已内化此限制（3/5 和 3.5/5）。\n3. **Cross-benchmark \"selective testing\" vs \"coverage gap\"**: R1 认为是选择性测试（cherry-picking），R2 认为是覆盖面不足但非刻意。**Director 判定**: 倾向 R2——实验覆盖确有限制但设计意图非 cherry-picking。\n\n---\n\n## Questions（需要作者回答）\n\n1. GPT-4o 和 Llama-70B 作为 judge 时，是否有计划用非 Qwen3-32B rewriter 进行验证？如有，预期时间？\n2. Section 4.1 的 primary family 是 6 还是 8 tests？register 的正式统计地位是什么？\n3. 100-point continuous scale 的高 tie rate (51-66%) 是否支持 construct divergence 解释（judge 在 absolute mode 下对 style 确实不敏感）而非 measurement tool 缺陷？\n4. Position-swap 后 43.9% inconsistency rate 为何未在正文讨论？是否影响 BT model reliability 判断？\n5. NLI FNR 的 GPT-4o 对应数字是多少？是否可以替代 Qwen3-32B 自评估的 8.4%？\n6. GEE confound structure 在不同 rewriter 下是否保持一致？是否有实验计划？\n\n---\n\n## Missing References\n\n**两位 Reviewer 共识应补充：**\n1. Tripathi et al. (2025). \"Pairwise or Pointwise? Optimizing Evaluation Approaches for LLM-as-Judge.\" arXiv:2504.14716\n2. Li et al. (2026). \"Grading Scale Impact on LLM-as-a-Judge.\" arXiv:2601.03444\n\n**单一 Reviewer 建议：**\n3. Shankar et al. (2024). \"Who Validates the Validators?\" — LLM 评估验证循环性 [R1]\n4. \"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory.\" arXiv:2602.00521 [R2]\n5. Huang et al. (2024). \"Bias and Fairness in Large Language Models: A Survey\" [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：error。** 视觉审查 Agent 因配额限制未能完成（\"You've hit your limit · resets May 25, 8am UTC\"）。无排版审查数据。用户可在配额重置后重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Overall | 3.5 | 3.5 | 3.5 |\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3/5 | 3.25/5 |\n| Reproducibility | 3/5 | 4/5 | 3.5/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合评价**：\n\n论文在方法论设计和统计分析上表现出色——七种方法的 sensitivity hierarchy、NLI gate 的多层验证、GEE per-axis confound structure 分解在同类论文中属于上乘水准。Likert Blindspot 的量化对 LLM evaluation 社区有直接实践价值。\n\n但三个 Must-Fix 问题需要关注：(1) evaluator-producer confound 的不充分控制削弱了 cross-architecture replication 的可信度；(2) primary family 定义与 Table 1 标注的矛盾是方法论硬伤；(3) \"first framework\" overclaim 需要措辞修正。前两者中 MF1 涉及补充实验（可能需要额外计算资源），MF2 和 MF3 是纯文本修改。\n\n核心 novelty 受限于经典 measurement theory 已有的理论预测（Thurstone 1927），论文的增量贡献在于 LLM judge 场景的具体量化——severity spectrum、per-axis interaction、tie rate mechanism。这足以支撑 Findings 级别接收，Conference 级别需要 MF1 的充分回应（cross-rewriter validation 覆盖至少 2/3 judges）和人工验证的补充。\n\n**可行修改路径**：\n- MF2 + MF3：纯文本修改，<1h\n- SF1-SF8：文本调整 + 补充 2 篇引用，<2h\n- MF1（cross-rewriter validation）：需额外实验，~4-8h GPU 时间\n- SF5（人工验证）：需用户标注，~1-2 天\n- M1-M3：排版修正，<30min\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"the first framework\" → \"a unified framework\" [MF3]\n- 4 组括号统计数据造成认知负担 → 保留 1-2 个核心数字，其余移至 Introduction [SF7]\n- 两种解释的并列(\"measurement attenuation and construct divergence\")处理得当\n\n### Introduction\n- Gap statement 合理但\"per-instance diagnostics\"requirement 在实验中体现不足——主要结果为 aggregate\n- Figure 1 (pipeline diagram) 清晰展示 sample attrition，好的实验报告实践\n\n### Related Work (§2)\n- 覆盖全面，Jeong et al. (2025) 已引用\n- 缺 Tripathi et al. (2025) 和 Li et al. (2026) [SF8]\n- 对 RATE 的批判性分析可更 balanced\n\n### Method (§3)\n- §3.5 因果语言校准上乘 [S1]\n- §3.2 已修改为 \"filtering-based confounder control\"，与 §3.5 hedging 一致\n- Temperature 0.7 选择未 justify\n- 各 axis pass rate 需在正文直接报告（目前需从 Table 1 footnote 间接推导）\n\n### Experiments (§4)\n- Section 4.1 primary family 定义需与 Table 1 统一 [MF2]\n- Table 1 第 6 列需添加列标题 [M2]\n- pre-registration vs post-hoc 分类值得肯定但未说明分类时点\n\n### Analysis (§5)\n- §5.1 NLI Gate Validation 最为 thorough；Gwet's AC1 vs κ 讨论专业\n- §5.2 Likert vs Pairwise 的 dual interpretation 框架成熟；6 controls 回应 Comparative Trap 结构清晰\n- §5.4 (Rewriter Independence) 覆盖面不足 [MF1]\n- §5.6 (GEE) regime classification threshold 未明确定义\n\n### Conclusion (§6)\n- \"should adopt pairwise\" 措辞仍偏强，需加 amplification risk caveat\n- Generalizability 边界需更明确\n\n### Limitations\n- 三个关键点覆盖合理\n- 可增加：人工验证缺失的显式标注、register 轴 evaluator-producer risk 的更强措辞\n\n### Format Compliance\n- ✅ 主正文 ≤ 8 页\n- ✅ Limitations section 存在\n- ✅ 匿名 (Anonymous, review mode)\n- ✅ natbib 引用格式\n- ⚠️ Table 1 第 6 列缺列标题\n- ⚠️ Appendix Table 5 缺 7 个 CI\n",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-21T21:29:19.359493+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Assistant

_source line 614 · 2026-05-21T21:29:35.970113+00:00_

审稿报告已投递至 Research Director。

---

**Round 7 审稿完成。** 核心结论：

- **Overall: 3.5 (Borderline Conference)**
- **3 个 Must-Fix**：evaluator-producer confound 控制不充分、Section 4.1 vs Table 1 register 分类矛盾、"first framework" overclaim
- **8 个 Should-Fix**：construct divergence 平衡、TOST 措辞、NLI FNR 循环性、verbosity 17.4% FPR、零人工验证、基准多样性、Abstract 密度、遗漏引用
- **可行修改路径**：MF2+MF3 为纯文本修改（<1h），MF1 需补充实验（~4-8h GPU）

Issue Tracker 已同步更新（新增 4 条 Round 7 issue，更新 12 条既有 issue 的 Round 7 mentions）。视觉审查因配额限制未完成，外部审稿未配置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 63

## Round 63

2 recorded events


### User

_source line 615 · 2026-05-21T21:29:38.460704+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **W1-W6**: 5 条 AGREE，1 条部分 AGREE（W4 循环性有 GPT-4o cross-validation 部分缓解）
- **W7-W8**: 2 条 REBUT（W7 是覆盖面不足而非 cherry-picking；W8 pair-level bootstrap 已处理依赖）
- **Q1-Q5**: 3 条 AGREE（Q1 CI 缺失、Q2 tie rate 支持 construct divergence、Q3/Q5 措辞和实验缺口），1 条 REBUT（Q4 论文已解释 Originality OR 语义）

两位 Reviewer 在 evaluator-producer confound、零人工验证、construct divergence 弱化、benchmark 覆盖面上形成了独立共识。我额外指出了 "first framework" overclaim、遗漏关键文献 (Tripathi et al. 2025)、Abstract 可读性三个 R1 未覆盖的问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 616 · 2026-05-21T21:29:52.395612+00:00_

审稿报告已投递至 Research Director。

**Round 7 审稿完成。** 两位 Reviewer 独立评分 3.5 (Borderline Conference)，综合维持 3.5。

核心结论：
- **3 个 Must-Fix**：evaluator-producer confound 控制不充分（需补 cross-rewriter validation）、Section 4.1 vs Table 1 register 分类矛盾、"first framework" overclaim
- **8 个 Should-Fix**：construct divergence 框架平衡、TOST 措辞、NLI FNR 循环性、verbosity 17.4% FPR、零人工验证、基准多样性、Abstract 密度、遗漏文献
- **3 个 Minor**：cross-benchmark 选择标准、Table 1 列标题、GEE CI 缺失

Issue Tracker 已同步更新（含 5 个新增 Round 7 issue + 历史 issue 状态更新）。视觉审查因配额限制未完成，外部审稿未配置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 64

## Round 64

80 recorded events


### User

_source line 617 · 2026-05-22T03:21:56.002972+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (Long Paper via ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-22T03:22:02.376765+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-22T03:22:02.427885+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-22T03:22:09.655473+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,read_local_file",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,read_local_file",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-22T03:22:09.655908+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-22T03:22:12.819266+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_local_file",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_local_file",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-22T03:22:12.870056+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-22T03:22:17.036969+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-22T03:22:17.087679+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-22T03:22:22.007670+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-22T03:22:23.566122+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (54 个)\n\n- **verbosity_32b**: DONE (success) — \n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **register_100_cf** (killed): Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality\n- **gemini_flash_fourth_judge** (success): Gemini Flash as a fourth judge will also exhibit style blindspot (BT-significant but Likert-NS) on formality and verbosity axes, consistent with GPT-4o, Qwen-32B, and Claude judges, confirming the blindspot is judge-universal rather than model-specific.\n- **llama70b_register** (success): Llama-70B register axis shows weak style bias (~55% BT, consistent with GPT-4o 57% and Qwen3-32B 55.3%), confirming register as originality-dominated across three independent judge architectures\n  [llama70b_register_summary](/api/workspace-files/projects/causal_style_decomp_judge/artifacts/llama70b_register/data/llama70b_register_summary.json)\n\n## 趋势\n成功 38 / 负向 12 / 失败 0 / 共 54\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- register_100_cf: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1558
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-22T03:22:23.566665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-22T03:22:24.320240+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Detecting Hidden Style Bias\\in LLM Judges via Controlled Style Decomposition}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding and construct validity.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
43	Although the formality effect survives logistic adjustment for original preference ($\text{OR} = 2.32$, $p = 0.006$; Appendix~\ref{app:direction}), residual confounding is not fully eliminated.
44	An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure. The Comparative Trap \citep{jeong2025comparative} lends support to this alternative; six experimental controls bound this risk (\S\ref{sec:amplification}), though definitive separation would require human ground-truth ratings.
45	
46	\paragraph{Evaluator-producer bias and generalizability.}
47	Qwen3-32B serves as both rewriter and judge, raising s
…[truncated 2106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-22T03:22:24.320659+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 631 · 2026-05-22T03:22:24.421248+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 632 · 2026-05-22T03:22:29.702716+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information related to EMNLP 2026, though the specifi
…[truncated 1143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5382
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-22T03:22:29.753490+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 5332
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-22T03:22:34.520622+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline page limit author guidelines 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission deadline page limit author guidelines 2026"
  }
}
```

</details>

---


### Tool call

_source line 635 · 2026-05-22T03:22:34.922494+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-22T03:22:36.077060+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-22T03:22:36.378643+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-22T03:22:36.880695+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-22T03:22:41.197208+00:00_

Web search results for query: "EMNLP 2026 ARR submission deadline page limit author guidelines 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Information For Authors | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/information/authors"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here's the information about EMNLP 2026 submission guidelines and deadlines:

## Key Deadlines

The ARR submission deadline is May 25, 2026. All authors must complete the author registration form by May 27, 2026. The EMNLP commitment deadline is August 2, 2026, with notification of acceptance on August 20, 2026.

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted pap
…[truncated 919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6676
}
```

</details>

---


### Tool result

_source line 640 · 2026-05-22T03:22:44.208205+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"

Links: [{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.02279v1"}]

Based on the search results, here are the key ACL Rolling Review 2026 submission guidelines regarding page limits and formatting requirements:

## Page Limits

Short papers must be 4 content pages maximum, and long papers must be 8 content pages maximum. Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages o
…[truncated 1295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 9285
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-22T03:22:44.258952+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/decisions.yaml\", \"content\": \"_next_id: 63\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 14:09 UTC\\n  summary: '文献蒸馏审视：研究方向无需调整，CSD 填补 #1 空白（多维 style 因果分解），post-MVP 需扩展 judge/benchmark/baseline\\n    覆盖'\\n  rationale: '10 篇论文蒸馏显示：(1) 多维 style 联合因果分解是领域 #1 空白，与 CSD 核心 claim 完全对齐；(2) 竞品 claim\\n    无直接重叠（FairJudge=white-box, Pref Leakage=family-based, Soumik=prompt-dependent）；(3)\\n    同行标准要求 3-5 异构 judge + AlpacaEval/Arena-Hard/MT-Bench + Bootstrap CIs + 对比 LC-AlpacaEval\\n    baseline。当前 MVP 方案足够，research 阶段需按蒸馏标准扩展。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 14:19 UTC\\n  summary: MVP 全量评分 + 分层分析：score 全部 100 条，按 BERTScore 阈值 0.88/0.90/0.92 分层算 ATE，不降低阈值\\n  rationale: 36% pass rate (BERTScore≥0.92) 偏低但 NLI 均值 0.9422 说明语义保留好。降阈值是数据操作，不如保留完整信息。全量评分\\n    (n=100) 保证统计 power，分层分析同时回答\\\"严格阈值下效应是否存在\\\"和\\\"宽松阈值下效应是否增强\\\"。8B H1 fail 不消耗迭代配额（ROADMAP\\n    规则），32B 备用。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 14:20 UTC\\n  summary: H1 content verification 改为 NLI-only gate（≥0.90），BERTScore 降为监控指标，不作为过滤条件\\n  rationale: Reviewer 诊断：36% pass rate 的根因是 BERTScore 惩罚 style transfer 预期的词汇变化（contractions→full\\n    forms 等），而非内容泄漏。NLI 均值 0.9422、抽样 >0.99 证明语义保留良好。BERTScore 作为 token-level 相似度指标与\\n    style transfer 评估目标矛盾（改的就是 token）。Double-rewrite pass rate 更低（21/100）进一步印证。NLI-only\\n    gate 是度量校准（不消耗 8B 迭代配额），与 D002 全量评分兼容——primary ATE 用 NLI≥0.90 子集，secondary 按 BERTScore\\n    分层。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 14:32 UTC\\n  summary: 8B 初步 ATE≈0.028 不可见，归因三因素：Likert 粒度 + 8B rewriter 质量 + RATE corruption。不计入\\n    kill criteria，等 n=100 + 32B\\n  rationale: 36/100 初步数据 Cohen's d=0.055 远低于 0.3 门槛，但三个叠加因素解释了结果：(1) 83% 零差异源于 integer\\n    Likert 无法捕捉 sub-integer 效应；(2) 22% identical rewrites 稀释 ATE；
…[truncated 1456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7378
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-22T03:22:49.681053+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-22T03:22:49.832117+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-22T03:22:50.133795+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-22T03:22:50.586061+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-22T03:22:50.686872+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "report.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "report.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-22T03:22:50.787710+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **register_100_cf** (killed): Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality\\n- **gemini_flash_fourth_judge** (success): Gemini Flash as a fourth judge will also exhibit style blindspot (BT-significant but Likert-NS) on formality and verbosity axes, consistent with GPT-4o, Qwen-32B, and Claude judges, confirming the blindspot is judge-universal rather than model-specific.\\n- **llama70b_register** (success): Llama-70B register axis shows weak style bias (~55% BT, consistent with GPT-4o 57% and Qwen3-32B 55.3%), confirming register as originality-dominated across three independent judge architectures\\n  [llama70b_register_summary](/api/workspace-files/projects/causal_style_decomp_judge/artifacts/llama70b_register/data/llama70b_register_summary.json)\\n\\n## 趋势\\n成功 38 / 负向 12 / 失败 0 / 共 54\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestb-29275: 无 GPU 信息\\n\\n## 告警\\n- exp-013: 已被终止 — unknown\\n- register_100_cf: 已被终止 — unknown\\n- exp-015: 已被终止 — unknown\\n- exp-016: 已被终止 — unknown\\n\", \"total_chars\": 1247, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-22T03:22:54.653693+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-22T03:22:55.005524+00:00_

1	\begin{abstract}
2	LLM judges are widely deployed for evaluation and alignment, yet style features alone explain judge scores with near-perfect correlation.
3	We introduce Controlled Style Decomposition (CSD), a unified framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison to systematically quantify style bias in LLM judges.
4	Across four target judges from four independent organizations, one negative control, three benchmarks, and three style axes, CSD demonstrates the Likert Blindspot: Likert scoring systematically misses style biases that pairwise comparison detects, following a severity spectrum from complete attenuation at moderate bias to over 60\% signal loss at stronger effects, confirmed by seven statistical methods.
5	GEE conditional decomposition reveals a per-axis confound structure consistent across all four target judges: verbosity bias is style-dominated, formality exhibits a conditional effect moderated by content quality, and register is judge-dependent---determining which estimates are directly interpretable and which require conditional analysis.
6	A negative-control judge shows no detectable bias on either primary axis, supporting discriminative validity.
7	Whether measurement attenuation or construct divergence, the operational conclusion is the same: Likert-only evaluation systematically misses style-driven preferences that propagate through pairwise-based alignment pipelines.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-22T03:22:55.156604+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-22T03:22:55.458201+00:00_

1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} --- given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions.
5	This is the \emph{Likert Blindspot}.
6	
7	LLM judges are central infrastructure for NLP evaluation and alignment training (RLHF, DPO), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.
8	Style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}: 76--92\% of observed preferences originate from surface-level style cues \citep{li2026preference}, with bias scores of 0.76--0.92 across five judges \citep{soumik2026judging}.
9	Despite this consensus, existing approaches each address individual requirements---multi-dimensional style analysis \citep{casse2026concise,wang2026fairjudge}, interventional design \citep{reber2025rate}, population-level correction \citep{dubois2025lc}---but no single framework integrates per-axis decomposition, interventional identification, per-instance diagnostics, and black-box applicability.
10	A further concern: standard Likert scoring produces ${\sim}60\%$ uninformative ties, and even non-tied pairs carry weaker signal than pairwise comparison---a limitation predicted by measurement theory \citep{thurstone1927law} but previously unquantified for LLM judges.
11	
12	We propose Controlled Style Decomposition (CSD), combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
13	Inspired by interventional text analysis \citep{veitch2020adapting}, CSD operates in three stages: style-controlled rewriting along a single axis, NLI entailment verification, and bias measurement via forced-choice com
…[truncated 2042 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-22T03:22:55.458614+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-22T03:22:55.910803+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Interventional Approaches to Judge Bias}
7	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
8	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
9	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
10	If this Likert Blindspot generalizes beyond our setting, RATE's own style-related findings may underestimate the true magnitude of attribute effects.
11	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
12	\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
13	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control rather than parametric aggregation.
14	
15	\paragrap
…[truncated 5035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-22T03:22:55.961628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-22T03:22:56.363369+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Style-Controlled Rewriting}
5	\label{sec:rewriting}
6	
7	We isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
8	For each text, an instruction-tuned LLM (Qwen3-32B) first classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification), then rewrites it toward the opposite pole (temperature 0.7) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
9	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
10	Each operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
11	To control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
12	
13	\subsection{Content Preservation Verification}
14	\label{sec:nli_gate}
15	
16	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
17	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with an entailment threshold of 0.90.
18	For axes that preserve information density (formality, register), we apply standard bidirectional entailment: both NLI(original $\to$ rewrite) and NLI(rewrite $\to$ original) must exceed this value.
19	For axes that inherently change information density (e.g., verbosity), bidirectional verification is inappropriate---expansion 
…[truncated 5706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-22T03:22:56.363775+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-22T03:22:57.418223+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	We designate a primary family of six hypothesis tests (three judges $\times$ two axes: formality and verbosity) and control the family-wise error rate with Holm-Bonferroni correction at $\alpha = 0.05$.
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.
13	All bootstrap confidence intervals use 10{,}000 pair-level resamples with seed 42.
14	
15	\paragraph{Model selection.}
16	Target judges span four architectures: GPT-4o (2024-08-06), the dominant judge powering AlpacaEval and MT-Bench leaderboards; Qwen3-32B-Instruct, also serving as rewriter for methodological consistency; Llama-3.3-70B-Instruct, the latest dense Llama model (Llama~4's MoE architecture introduces an additional confound); and Gemini-2.5-Flash as a confirmatory fourth architecture. Claude Sonnet~4 serves as negative control.
17	We pin versions for reproducibility; CSD applies to any black-box judge.
18	
19	\begin{table}[t]
20	\centering
21	\small
22	\caption{Main results across five judges, three style axes, and three benchmarks. BT: Bradley-Terry win probability (10{,}000 pair
…[truncated 16372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-22T03:22:57.669585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-22T03:22:57.669953+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	CSD, a black-box framework, yields two findings across five judges, three benchmarks, and three style axes.
5	First, the \emph{Likert Blindspot}: Likert scoring systematically misses style biases that pairwise comparison detects---complete at moderate bias ($d \to 0$ at $n = 355$), ${>}60\%$ attenuation at stronger effects---confirmed by seven statistical methods; whether this reflects measurement attenuation or construct divergence, Likert-only audits miss style-driven preferences that propagate through alignment pipelines.
6	Second, GEE conditional decomposition reveals per-axis confound structure---verbosity style-dominated, formality conditional, register judge-dependent---determining which estimates require conditional analysis.
7	Existing Likert-based null findings may reflect measurement insensitivity; pairwise comparison with amplification controls (\S\ref{sec:amplification}) offers superior detection sensitivity.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-22T03:22:57.870793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-22T03:22:57.971707+00:00_

1	\appendix
2	
3	\section{Direction Asymmetry and Quality Confounding}
4	\label{app:direction}
5	
6	The formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\% of formal-is-rewrite pairs ($p = 0.001$) but only 54.5\% of casual-is-rewrite pairs ($p = 0.83$).
7	This asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.
8	To quantify this, we fit a GEE logistic model (exchangeable correlation) with both formality and original-preference as predictors.
9	After controlling for original preference, the formality effect remains significant ($\text{OR} = 2.58$, $p = 0.002$), and the original-preference effect is also significant ($\text{OR} = 2.32$, $p = 0.006$).
10	The formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.
11	
12	At $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exceeded the GPT-4o estimate ($2.58$), but a scaled replication ($n = 355$) corrects this to $2.15$ ($p < 0.0001$), comparable to GPT-4o and consistent with small-sample upward bias rather than evaluator-producer inflation of the style effect.
13	The originality confound remains stronger ($4.99$ vs.\ $2.32$), consistent with evaluator-producer bias inflating the originality component (Limitations).
14	The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.
15	
16	The NLI gate blocks \emph{content} changes but cannot block quality perception shifts that are themselves mediated by style---a fundamental identifiability limit of any text-rewriting approach.
17	
18	\section{Consistency Filter Robustness}
19	\label{sec:consistenc
…[truncated 21573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 662 · 2026-05-22T03:23:13.781835+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-22T03:23:15.689176+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'causal_style_decomp_judge'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1907
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-22T03:23:15.790134+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_EXISTS\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_EXISTS\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-22T03:23:17.095563+00:00_

&lt;persisted-output>
Output too large (38KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/20db643a-00c6-4206-9b6a-b09a518d423b/tool-results/bke0tlooo.txt

Preview (first 2KB):
issues:
  # ============================================================
  # Round 1-4 issues (all resolved unless noted)
  # ============================================================

  - id: "R1-N1"
    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
    resolution_round: 4
    mentions:
      - round: 3
        reviewers: [1, 2]
        note: "因果语言降级问题在 Round 3 以新形式复发，见 R3-N1"
      - round: 4
        reviewers: [1]
        note: "R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。"
      - round: 5
        reviewers: [1, 2]
        note: "标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2"

  - id: "R2-N1"
    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
    category: framing
    severity: warning
    status: in_progress
    first_raised_round: 1
    last_seen_round: 7
    resolution: null
    resolution_round: null
    mentions:
      - round: 3
        reviewers: [1, 2]
        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
      - round: 4
        reviewers: [1, 2]
        note: "R4-SF8: Honest novelty positioning applied."
      - round: 5
        reviewers: [1, 2]
        note: "Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。"
      - round: 7
        reviewers: [2]
        note: "R2 再次指出核心发现可从 Thurstone (1927) 理论直接预测。R1 反驳称 severity spectrum 和 per-axis interaction 是全新经验发现。分歧未完全解决。"

  - id: "R1-N2"
    summary:
…[truncated 338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 1305
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-22T03:23:17.196365+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-22T03:23:17.548054+00:00_

-rw-r--r-- 1 ubuntu ubuntu 368095 May 22 01:13 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-22T03:23:18.101481+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-22T03:23:19.507222+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-22T03:23:19.708443+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib 2>/dev/null && echo \"---\" && head -100 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib 2>/dev/null",
  "description": "Check references.bib existence and content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib 2>/dev/null && echo \"---\" && head -100 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib 2>/dev/null",
    "description": "Check references.bib existence and content"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-22T03:23:19.759245+00:00_

467 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib
---
@inproceedings{tripathi2025pairwise,
  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},
  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},
  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},
  year={2025},
  url={https://arxiv.org/abs/2504.14716}
}

@inproceedings{murugadoss2025sos,
  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},
  author={Murugadoss, Aakanksha and others},
  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2025},
  url={https://arxiv.org/abs/2409.15268}
}

@inproceedings{li2026preference,
  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},
  author={Li, Dawei and others},
  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2026},
  url={https://arxiv.org/abs/2502.01534}
}

@article{wang2026fairjudge,
  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},
  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},
  journal={arXiv preprint arXiv:2602.06625},
  year={2026},
  url={https://arxiv.org/abs/2602.06625}
}


@inproceedings{dubois2025lc,
  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},
  author={Dubois, Yann and others},
  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2025},
  url={https://arxiv.org/abs/2404.04475}
}

@article{casse2026concise,
  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},
  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},
  journal={arXiv preprint arXiv:2601.10809},
  year={2026},
  url={ht
…[truncated 2012 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-22T03:23:23.725514+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge -name \"config.*\" -o -name \"project.yaml\" -o -name \"project.json\" 2>/dev/null | head -10",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge -name \"config.*\" -o -name \"project.yaml\" -o -name \"project.json\" 2>/dev/null | head -10",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-22T03:23:24.077188+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pandas/_config/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pandas/_config/config.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-22T03:23:24.278462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-22T03:23:24.329157+00:00_

0	issues:
1	  # ============================================================
2	  # Round 1-4 issues (all resolved unless noted)
3	  # ============================================================
4	
5	  - id: "R1-N1"
6	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
7	    category: framing
8	    severity: critical
9	    status: resolved
10	    first_raised_round: 1
11	    last_seen_round: 5
12	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
13	    resolution_round: 4
14	    mentions:
15	      - round: 3
16	        reviewers: [1, 2]
17	        note: "因果语言降级问题在 Round 3 以新形式复发，见 R3-N1"
18	      - round: 4
19	        reviewers: [1]
20	        note: "R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。"
21	      - round: 5
22	        reviewers: [1, 2]
23	        note: "标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2"
24	
25	  - id: "R2-N1"
26	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
27	    category: framing
28	    severity: warning
29	    status: in_progress
30	    first_raised_round: 1
31	    last_seen_round: 7
32	    resolution: null
33	    resolution_round: null
34	    mentions:
35	      - round: 3
36	        reviewers: [1, 2]
37	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
38	      - round: 4
39	        reviewers: [1, 2]
40	        note: "R4-SF8: Honest novelty positioning applied."
41	      - round: 5
42	        reviewers: [1, 2]
43	        note: "Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。"
44	      - round: 7
45	        reviewers: [2]
46	        note: "R2 再次指出核心发现可从 Thurstone (1927) 理论直接预测。R1 反驳称 severity spectrum 和 per-axis interaction 是全新经验发现。分歧未完全解决。"
47	
48	  - id: "R1-N2"
49	    summary: "NLI gate 67% false-negative rate 造成选择偏差未分析"
50	    category: method
51	    severity: critical
52	    status: resolved
53	    first_raised_round: 1
54	    last_seen_round: 1
55
…[truncated 4162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-22T03:23:27.423815+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "offset": "200",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "offset": "200",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-22T03:23:27.438876+00:00_

200	    summary: "Likert ATE 方向反转"
201	    category: experiment
202	    severity: warning
203	    status: resolved
204	    first_raised_round: 1
205	    last_seen_round: 1
206	    resolution: "Magnitude gap framing"
207	    resolution_round: 1
208	
209	  - id: "CROSS-4"
210	    summary: "Ordinal regression 必要"
211	    category: method
212	    severity: critical
213	    status: resolved
214	    first_raised_round: 1
215	    last_seen_round: 1
216	    resolution: "Definitively resolved"
217	    resolution_round: 1
218	
219	  - id: "RD2-MF2"
220	    summary: "Holm-Bonferroni 'nine tests' 错误"
221	    category: method
222	    severity: critical
223	    status: resolved
224	    first_raised_round: 2
225	    last_seen_round: 2
226	    resolution: "Text fixed to '6 tests'. Holm 6-test: 4/6 significant."
227	    resolution_round: 2
228	
229	  - id: "RD2-MF3"
230	    summary: "单一 benchmark (LLMBar n=100) 不支撑全称论断"
231	    category: experiment
232	    severity: critical
233	    status: resolved
234	    first_raised_round: 2
235	    last_seen_round: 4
236	    resolution: "3 benchmarks x 3 judges. 6/7 biased cells BT significant."
237	    resolution_round: 2
238	
239	  - id: "RD2-MF4"
240	    summary: "Abstract overclaim: 'dominant source' + verbosity category error"
241	    category: framing
242	    severity: critical
243	    status: resolved
244	    first_raised_round: 2
245	    last_seen_round: 2
246	    resolution: "Overclaim replaced in intro. Verbosity category error removed."
247	    resolution_round: 2
248	
249	  - id: "RD2-VIS"
250	    summary: "主正文超 8 页限制"
251	    category: format
252	    severity: critical
253	    status: resolved
254	    first_raised_round: 2
255	    last_seen_round: 7
256	    resolution: "Round 7 两位 Reviewer 均确认主正文 8 页合规。§5.5 Register 压缩 + §6 Conclusion 精简。"
257	    resolution_round: 7
258	    mentions:
259	      - round: 2
260	        reviewers: [1, 2]
261	        note: "Round 2 发现并修复。"
262	      - round: 6
263	        reviewers: [1, 2]
264	        
…[truncated 8272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 15
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-22T03:23:30.518010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "offset": "500",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "offset": "500",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-22T03:23:30.518549+00:00_

500	    first_raised_round: 3
501	    last_seen_round: 7
502	    resolution: null
503	    resolution_round: null
504	    mentions:
505	      - round: 4
506	        reviewers: [1, 2]
507	        note: "Cross-rewriter consistency + 200-pair GPT-4o validation provide partial proxy. Acknowledged in Limitations."
508	      - round: 5
509	        reviewers: []
510	        note: "Round 5 未被任何 Reviewer 显式提及，但仍 inherently open（无人工评估数据）。"
511	      - round: 6
512	        reviewers: [1, 2]
513	        note: "R6-R1 列为 Must-Fix。R6-R2 同意但建议降级为 strong Should-Fix。交叉后共识：Must-Fix，50 对 pass/fail 样本 2+ annotator 评估即可满足。"
514	      - round: 7
515	        reviewers: [1, 2]
516	        note: "R7-R1 列为 Should-Fix (W6)，R7-R2 完全同意。两位 Reviewer 共识：全文零人工验证，涉及测量工具敏感度的论文却用同类工具验证，存在认识论循环。共识 Should-Fix。"
517	    action_items:
518	      - round: 6
519	        action: "准备 50 对 NLI pass/fail 样本 + 标注模板，用户标注后报告 agreement + Cohen's κ"
520	        assigned_to: user
521	        status: pending
522	
523	  - id: "R3-W4"
524	    summary: "Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性"
525	    category: method
526	    severity: warning
527	    status: resolved
528	    first_raised_round: 3
529	    last_seen_round: 4
530	    resolution: "Limitations 新增相关段落。"
531	    resolution_round: 4
532	
533	  - id: "R3-W5"
534	    summary: "GEE 'decomposition' 在残余 confounding 下有误导性"
535	    category: framing
536	    severity: warning
537	    status: resolved
538	    first_raised_round: 3
539	    last_seen_round: 5
540	    resolution: "Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'."
541	    resolution_round: 4
542	    mentions:
543	      - round: 5
544	        reviewers: [1, 2]
545	        note: "术语已改善，但 verbosity 'confound-free' 措辞仍过强。见 R5-SF4。"
546	
547	  - id: "R3-W6"
548	    summary: "小样本 OR 估计不稳定"
549	    category: experiment
550	    severity: warning
551	    status: resolved
552	    first_raised_round: 3
553	    last_seen_round: 4
554	    resolution: "n=355
…[truncated 8518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-22T03:23:35.543955+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "offset": "800",
  "limit": "400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "offset": "800",
    "limit": "400"
  }
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-22T03:23:35.595021+00:00_

800	        note: "合并入 RD2-SF1 讨论。仍为 in_progress。"
801	
802	  - id: "R5-SF3"
803	    summary: "Judge 覆盖面 framing 'across three judges' 有误导性"
804	    category: framing
805	    severity: warning
806	    status: resolved
807	    first_raised_round: 5
808	    last_seen_round: 5
809	    resolution: "Llama-70B 加入后现有 3 target judges 全部展示 Blindspot (6/6 cells + register 7/9)。Round 6 未再被提及。"
810	    resolution_round: 6
811	
812	  - id: "R5-SF4"
813	    summary: "GEE verbosity 'confound-free' 措辞过强"
814	    category: method
815	    severity: warning
816	    status: resolved
817	    first_raised_round: 5
818	    last_seen_round: 5
819	    resolution: "论文已使用 'style-dominated' 而非 'confound-free'。Round 6 未再被提及。"
820	    resolution_round: 6
821	
822	  - id: "R5-SF5"
823	    summary: "Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示——缺 verbosity 验证"
824	    category: experiment
825	    severity: warning
826	    status: resolved
827	    first_raised_round: 5
828	    last_seen_round: 6
829	    resolution: "Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。"
830	    resolution_round: 6
831	
832	  - id: "R5-SF6"
833	    summary: "Measurement attenuation vs construct difference 主文呈现严重不平衡"
834	    category: framing
835	    severity: warning
836	    status: in_progress
837	    first_raised_round: 5
838	    last_seen_round: 7
839	    resolution: null
840	    resolution_round: null
841	    mentions:
842	      - round: 5
843	        reviewers: [1, 2]
844	        note: "需在 §5.2 给两种解释同等篇幅。"
845	      - round: 6
846	        reviewers: [1, 2]
847	        note: "§5.2 末尾已加入讨论段落。"
848	      - round: 7
849	        reviewers: [1, 2]
850	        note: "R7-R2 (W2) 列为 Must-Fix，认为框架系统性偏向 measurement failure。R7-R1 [REBUT]：论文在 Section 5.2、Abstract、Contribution #2 三处明确并列两种解释，属于 'agnosticism + operational equivalence' 论证策略。分歧：R2 认为标题和核心叙事偏颇，R1 认为已合理平衡。Director 判定：Should-Fix（标题和 Abstract 措辞可微调以减少 bias 感知，但论文实质上已提供 balanced discussion）。"
851	
852	  - id: "R5-SF7"
853	    summary: "Formality 
…[truncated 10627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-22T03:24:01.893943+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 3 -name \"*.yaml\" -path \"*/causal_style_decomp_judge/*\" ! -path \"*/.venv/*\" ! -path \"*/artifacts/*\" 2>/dev/null",
  "description": "Find project config YAML files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 3 -name \"*.yaml\" -path \"*/causal_style_decomp_judge/*\" ! -path \"*/.venv/*\" ! -path \"*/artifacts/*\" 2>/dev/null",
    "description": "Find project config YAML files"
  }
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-22T03:24:01.994946+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-22T03:24:04.906732+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 2 -name \"config.*\" ! -path \"*/.venv/*\" 2>/dev/null",
  "description": "Find config files in workspace root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 2 -name \"config.*\" ! -path \"*/.venv/*\" 2>/dev/null",
    "description": "Find config files in workspace root"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-22T03:24:04.958386+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-22T03:24:08.823327+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 1 -name \"*.yaml\" -o -name \"*.json\" 2>/dev/null | head -20",
  "description": "Find top-level config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 1 -name \"*.yaml\" -o -name \"*.json\" 2>/dev/null | head -20",
    "description": "Find top-level config files"
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-22T03:24:08.874058+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-22T03:24:11.635173+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/workspace.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/workspace.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-22T03:24:11.685760+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-22T03:24:30.025041+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-22T03:24:52.320523+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22295
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-22T03:24:52.521607+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Main Conference (Long Paper via ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，参考文献不限页数。Limitations 和 Ethics 不计入页数限制（但不能含过多额外内容）。\n- **模板**: ACL 双栏格式 (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind（作者信息应匿名）\n- **Checklist**: ARR Responsible NLP Checklist 在 OpenReview submission form 中填写，不在 PDF 中\n\n## 论文文件\n- 主文件: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf`\n\n## 你的审查侧重\n\n**核心职责：方法论严谨性、实验设计、统计分析**\n\n请重点审查以下方面：\n\n### 1. 方法论 (Method)\n- NLI-gated content control 的设计是否合理？NLI 阈值 0.90 的选择是否有充分 justification？\n- Direction-aware NLI gating（verbosity 轴）是否引入 systematic bias？\n- Controlled Style Decomposition 的因果声明强度是否与 evidence 匹配？DAG (Figure 2) 的识别假设是否完备？\n- 同一模型 (Qwen3-32B) 同时作为 rewriter 和 judge 的 evaluator-producer bias 如何处理？cross-rewriter independence test 覆盖是否充分？\n\n### 2. 实验设计 (Experiments)\n- 统计框架：primary family 定义（几个 tests？Holm-Bonferroni 校正是否正确？）与 Table 1 标注是否一致？exploratory vs confirmatory 分类是否合理？\n- Bradley-Terry 模型假设（IIA 等）是否被检验？GoF 诊断是否充分？\n- GEE conditional decomposition：correlation structure 选择是否 robust？interaction test 结果如何？\n- 负面控制 (Claude Sonnet 4)：TOST equivalence testing 的 Δ 选择是否合理？统计功效是否足够？\n- 样本量：LLMBar n=100（NLI 后 n=88），scaled replication n=355 仅覆盖一个 judge×axis。这对结论的 generalizability 有多大影响？\n\n### 3. 内容完整性\n- Rewriting artifact control（same-style double-rewrite）是否充分？\n- NLI gate validation：FNR 估计使用同一 rewriter 模型是否存在循环性？GPT-4o cross-validation 的报告是否完整？\n- 100-point continuous Likert scale 实验是否排除了 granularity explanation？\n\n### 4. 格式合规\n- 正文是否 ≤8 页？\n- Limitations 章节是否恰当（覆盖要点但不过长）？\n- 参考文献格式是否一致？\n\n请提供：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，分 Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (评分 + 置信度)\n7. **Detailed Comments** (逐节)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Main Conference (Long Paper via ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，参考文献不限页数。Limitations 和 Ethics 不计入页数限制（但不能含过多额外内容）。\n- **模板**: ACL 双栏格式 (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind（作者信息应匿名）\n- **Checklist**: ARR Responsible NLP Checklist 在 OpenReview submission form 中填写，不在 PDF 中\n\n## 论文文件\n- 主文件: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf`\n\n## 你的审查侧重\n\n**核心职责：方法论严谨性、实验设计、统计分析**\n\n请重点审查以下方面：\n\n### 1. 方法论 (Method)\n- NLI-gated content control 的设计是否合理？NLI 阈值 0.90 的选择是否有充分 justification？\n- Direction-aware NLI gating（verbosity 轴）是否引入 systematic bias？\n- Controlled Style Decomposition 的因果声明强度是否与 evidence 匹配？DAG (Figure 2) 的识别假设是否完备？\n- 同一模型 (Qwen3-32B) 同时作为 rewriter 和 judge 的 evaluator-producer bias 如何处理？cross-rewriter independence test 覆盖是否充分？\n\n### 2. 实验设计 (Experiments)\n- 统计框架：primary family 定义（几个 tests？Holm-Bonferroni 校正是否正确？）与 Table 1 标注是否一致？exploratory vs confirmatory 分类是否合理？\n- Bradley-Terry 模型假设（IIA 等）是否被检验？GoF 诊断是否充分？\n- GEE conditional decomposition：correlation structure 选择是否 robust？interaction test 结果如何？\n- 负面控制 (Claude Sonnet 4)：TOST equivalence testing 的 Δ 选择是否合理？统计功效是否足够？\n- 样本量：LLMBar n=100（NLI 后 n=88），scaled replication n=355 仅覆盖一个 judge×axis。这对结论的 generalizability 有多大影响？\n\n### 3. 内容完整性\n- Rewriting artifact control（same-style double-rewrite）是否充分？\n- NLI gate validation：FNR 估计使用同一 rewriter 模型是否存在循环性？GPT-4o cross-validation 的报告是否完整？\n- 100-point continuous Likert scale 实验是否排除了 granularity explanation？\n\n### 4. 格式合规\n- 正文是否 ≤8 页？\n- Limitations 章节是否恰当（覆盖要点但不过长）？\n- 参考文献格式是否一致？\n\n请提供：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，分 Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (评分 + 置信度)\n7. **Detailed Comments** (逐节)"
  }
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-22T03:25:14.447982+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21926
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-22T03:25:14.649200+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "你是 Reviewer 2，负责**新颖性、完整性与写作质量**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Main Conference (Long Paper via ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，参考文献不限页数。Limitations 和 Ethics 不计入页数限制（但不能含过多额外内容）。\n- **模板**: ACL 双栏格式 (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind（作者信息应匿名）\n- **Checklist**: ARR Responsible NLP Checklist 在 OpenReview submission form 中填写，不在 PDF 中\n\n## 论文文件\n- 主文件: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf`\n\n## 你的审查侧重\n\n**核心职责：新颖性评估、Related Work 完整性、叙事质量与论文呈现**\n\n请重点审查以下方面：\n\n### 1. 新颖性与贡献 (Novelty & Contribution)\n- \"Likert Blindspot\" 是否为 genuine novel finding？还是 Thurstone (1927) 心理测量学已知现象在 LLM judge domain 的 transfer？novelty 如何正确定位？\n- CSD framework 的独立贡献——将 NLI-gated control + per-axis decomposition + position-controlled pairwise comparison 组合为统一框架，这是否有足够增量价值？\n- GEE conditional decomposition 揭示的 per-axis confound structure 是否构成独立贡献？\n- 论文的 claim 强度是否与 evidence 匹配？是否存在 overclaim（如 \"first framework\" 等措辞）？\n\n### 2. Related Work 完整性\n- 是否充分覆盖以下领域：\n  - LLM-as-Judge style bias（SOS-Bench, Preference Leakage, FairJudge, CASSE 等）\n  - Interventional text analysis（CausalM, Polyjuice, RATE 等）\n  - Measurement theory（Thurstone, Stevens, Likert scale literature）\n  - Pairwise vs pointwise evaluation（Comparative Trap, Tripathi et al.）\n  - Position bias（Zheng et al., Wang et al., Shi et al.）\n- 是否有重要遗漏的相关工作？\n- 对 RATE 的批评是否公平？\n\n### 3. 写作质量与呈现 (Presentation)\n- Abstract 是否清晰、简洁、信息密度适当？\n- Introduction 的叙事逻辑是否流畅？motivating example 是否有效？\n- 图表质量：Figure 1 (pipeline), Figure 2 (DAG), Figure 3 (forest plot), Figure 4 (power curve)——是否清晰、专业、信息丰富？\n- Table 1 (main results) 的设计是否易读？列标题/footnotes 是否完整？\n- Conclusion 是否适当总结了贡献而不 overclaim？\n- 整体叙事：measurement attenuation vs construct divergence 两种解释是否获得平等讨论？\n\n### 4. 完整性 (Completeness)\n- 实验覆盖面：4 target judges + 1 negative control, 3 benchmarks, 3 style axes——是否充分？\n- 缺失的实验或分析：有哪些可合理预期但未做的？\n- Limitations 是否坦诚并覆盖主要 weak points？\n- Code and Data availability statement 是否合规？\n\n### 5. 格式与匿名\n- 匿名化是否完整（无自引泄漏、无 acknowledgment）？\n- 正文是否 ≤8 页？\n- 引用格式是否一致（natbib 风格，年份括号等）？\n\n请提供：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，分 Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (评分 + 置信度)\n7. **Detailed Comments** (逐节)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "你是 Reviewer 2，负责**新颖性、完整性与写作质量**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Main Conference (Long Paper via ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，参考文献不限页数。Limitations 和 Ethics 不计入页数限制（但不能含过多额外内容）。\n- **模板**: ACL 双栏格式 (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind（作者信息应匿名）\n- **Checklist**: ARR Responsible NLP Checklist 在 OpenReview submission form 中填写，不在 PDF 中\n\n## 论文文件\n- 主文件: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf`\n\n## 你的审查侧重\n\n**核心职责：新颖性评估、Related Work 完整性、叙事质量与论文呈现**\n\n请重点审查以下方面：\n\n### 1. 新颖性与贡献 (Novelty & Contribution)\n- \"Likert Blindspot\" 是否为 genuine novel finding？还是 Thurstone (1927) 心理测量学已知现象在 LLM judge domain 的 transfer？novelty 如何正确定位？\n- CSD framework 的独立贡献——将 NLI-gated control + per-axis decomposition + position-controlled pairwise comparison 组合为统一框架，这是否有足够增量价值？\n- GEE conditional decomposition 揭示的 per-axis confound structure 是否构成独立贡献？\n- 论文的 claim 强度是否与 evidence 匹配？是否存在 overclaim（如 \"first framework\" 等措辞）？\n\n### 2. Related Work 完整性\n- 是否充分覆盖以下领域：\n  - LLM-as-Judge style bias（SOS-Bench, Preference Leakage, FairJudge, CASSE 等）\n  - Interventional text analysis（CausalM, Polyjuice, RATE 等）\n  - Measurement theory（Thurstone, Stevens, Likert scale literature）\n  - Pairwise vs pointwise evaluation（Comparative Trap, Tripathi et al.）\n  - Position bias（Zheng et al., Wang et al., Shi et al.）\n- 是否有重要遗漏的相关工作？\n- 对 RATE 的批评是否公平？\n\n### 3. 写作质量与呈现 (Presentation)\n- Abstract 是否清晰、简洁、信息密度适当？\n- Introduction 的叙事逻辑是否流畅？motivating example 是否有效？\n- 图表质量：Figure 1 (pipeline), Figure 2 (DAG), Figure 3 (forest plot), Figure 4 (power curve)——是否清晰、专业、信息丰富？\n- Table 1 (main results) 的设计是否易读？列标题/footnotes 是否完整？\n- Conclusion 是否适当总结了贡献而不 overclaim？\n- 整体叙事：measurement attenuation vs construct divergence 两种解释是否获得平等讨论？\n\n### 4. 完整性 (Completeness)\n- 实验覆盖面：4 target judges + 1 negative control, 3 benchmarks, 3 style axes——是否充分？\n- 缺失的实验或分析：有哪些可合理预期但未做的？\n- Limitations 是否坦诚并覆盖主要 weak points？\n- Code and Data availability statement 是否合规？\n\n### 5. 格式与匿名\n- 匿名化是否完整（无自引泄漏、无 acknowledgment）？\n- 正文是否 ≤8 页？\n- 引用格式是否一致（natbib 风格，年份括号等）？\n\n请提供：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，分 Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (评分 + 置信度)\n7. **Detailed Comments** (逐节)"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-22T03:25:16.259973+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1610
}
```

</details>

---


### Assistant

_source line 696 · 2026-05-22T03:25:28.578417+00:00_

**Round 1 已启动：**
- 视觉审查 Agent：已派发（fire-and-forget）
- Reviewer 1（方法严谨性/实验设计）：已分配
- Reviewer 2（新颖性/完整性/写作质量）：已分配

等待两位 Reviewer 返回初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 65

## Round 65

2 recorded events


### User

_source line 697 · 2026-05-22T03:33:37.455405+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：新颖性、完整性与写作质量

**论文**: "The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition"
**Venue**: EMNLP 2026 Main Conference (Long Paper via ARR)

---

## 总体评分

**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 实验设计严谨、实用价值高的 empirical study，但核心发现（Likert Blindspot）的概念新颖性有限——本质上是 Thurstone (1927) 已确立的心理测量原理在 LLM judge 领域的系统性验证，论文需更诚实地定位 novelty 边界；同时缺少 human validation 来解决 "detection vs. amplification" 的根本性问题。

---

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论设计严谨（NLI gate、负面控制、position control、7种统计方法），但 "pairwise 检测 vs. 放大" 的核心区分未完全解决；无人类标注验证 ground truth |
| Excitement | 3/5 | 发现实用且对 LLM evaluation 社区有价值，但概念层面是已知心理测量原理的领域迁移，增量贡献为主 |
| Reproducibility | 4/5 | 承诺开源代码和数据；实验细节在附录 P 中描述充分；统计方法清晰可复现 |
| Reviewer Confidence | 4/5 | 熟悉 LLM-as-Judge、measurement theory、interventional text analysis 相关文献 |

---

## Summary

本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated 内容控制、逐轴风格分解和位置控制的 pairwise comparison，系统量化 LLM judge 中的风格偏差。核心发现 "Likert Blindspot" 表明 Likert 评分系统性地遗漏了 pairwise comparison 能检测到的风格偏差，在中等效应量下信号衰减超 60%。GEE 条件分解揭示了 per-axis 的 confound 结构（verbosity = style-dominated，formality = conditional，register = judge-dependent）。实验覆盖 4 个 target judges + 1 个 negative control、3 个 benchmark、3 个风格轴，附录提供了大量 robustness checks。

---

## 主要优势

**S1. 实验设计严谨，控制充分。** NLI gate（DeBERTa-v3-large, threshold 0.98）、negative control judge（Claude Sonnet 4）、position-controlled pairwise、cross-benchmark replication（LLMBar/AlpacaEval/MT-Bench）构成多层验证体系。Appendix D 还用独立 rewriter（GPT-4o）验证了框架鲁棒性。这种控制层次在该领域论文中属于上乘。

**S2. 统计分析全面且层次分明。** 七种统计方法（BT、Sign test、Likert ATE、Binomial、Ordinal regression、GEE、Wilcoxon）形成 sensitivity hierarchy（Table 2），清晰展示 pairwise 方法与 Likert 方法的系统性灵敏度差异。GEE 条件分解（Table 3）揭示不同风格轴具有不同的 confound 结构，这是一个 genuinely novel 的分析贡献。

**S3. 对 "measurement attenuation vs. construct divergence" 两种解释的公平讨论。** 论文没有武断地声称 pairwise 一定"更好"，而是诚实地承认两种解释并存（§5.2, §6, Limitations），这种学术诚实值得肯定。

**S4. Appendix M（100-point continuous Likert）是一个关键控制实验。** 证明 Blindspot 不是 scale granularity 问题（即使 101 个可能值，tie rate 仍高达 51-64%），而是 absolute vs. relative evaluation paradigm 的根本差异。这大大增强了核心论点。

**S5. 负面控制的 discriminative validity。** Claude Sonnet 4 作为 negative control 在两个主要轴上未检测到显著偏差（formality p = 0.091, verbosity p = 0.284），支持框架的 discriminative validity——并非所有 judge 都会被标记为有偏差。

**S6. 与 RATE 的对比公平且建设性。** 论文不是简单否定 RATE，而是定位两者为互补框架（§5.2: "the frameworks are complementary"），并具体说明 CSD 如何在三个方面（per-axis targeting、pairwise measurement、NLI entailment gating）提供增量价值。

---

## Must-Fix 问题（影响接收决定）

**N1 [critical] Novelty 定位不够诚实：Likert Blindspot 的概念基础已有近百年历史**

- 具体位置：Section 2 ("Measurement Sensitivity in NLG Evaluation"), Section 1 (Introduction)
- 问题：论文在 §2 中提到 Thurstone (1927) 和 Stevens (1946)，承认 "the superiority of pairwise comparison over rating scales for eliciting reliable human judgments has been established since Thurstone (1927)"。然而论文整体叙事——从标题中的 "Detecting Hidden Style Bias"，到 Abstract 中将 Likert Blindspot 作为主要发现呈现，到 Introduction 的 motivating example——给读者的印象是这是一个**全新发现**。
  
  实际上，forced-choice methods 优于 rating scales 在心理测量学中已是教科书级共识（Thurstone 1927; Bradley & Terry 1952; Preston & Colman 2000，论文均已引用）。Likert Blindspot 本质上是这一已知原理在 LLM judge 领域的**系统性 empirical demonstration**，而非概念层面的新发现。
  
- 为什么影响接收：ARR Reviewer Guidelines 明确指出 novelty 要求 "demonstrating that work isn't highly similar [to] published [work]"。虽然 LLM-specific 的 empirical evidence 有价值，但如果 novelty 定位模糊，reviewers（尤其是熟悉 psychometrics 的）会认为 contribution 被 overclaim。
  
- 建议修改方向：
  1. 在 Introduction 中更早、更明确地承认 psychometric baseline："While the superiority of forced-choice over rating scales is well-established in psychometrics (Thurstone, 1927), whether and to what extent this phenomenon manifests in LLM judges—and what its practical consequences are for evaluation pipelines—has not been systematically studied."
  2. 将 novelty claim 从 "discovering the Blindspot" 调整为 "providing the first controlled, per-axis quantification of this psychometric phenomenon in LLM judges, revealing a severity spectrum and judge-dependent confound structures that psychometric theory alone cannot predict."
  3. 更突出 GEE conditional decomposition 作为独立贡献——这是论文中真正 novel 的分析发现。

**N2 [critical] "Detection vs. Amplification" 问题未充分解决，缺少 human validation**

- 具体位置：Section 5.2, Section 3 (对 Jeong et al. 2025 Comparative Trap 的回应)
- 问题：论文在 §3 (page 3) 正确地指出 Jeong et al. (2025) 的 Comparative Trap 论点——pairwise comparison 可能放大（而非仅检测）style biases。§5.2 回应了六个 "independent controls" 来 bound this risk：(i) NLI gate ablation, (ii) Claude Sonnet 4 negative control, (iii) cross-BT variation, (iv) debiased prompting, (v) rewriting independence, (vi) consistent GEE structure。
  
  然而这些控制虽然排除了一些 artifactual 解释，**并不能在根本上区分 "pairwise 检测了 Likert 遗漏的真实偏差" 和 "pairwise 放大了微弱但合理的 style preferences"。** 唯一能真正解决这个问题的是 human evaluation——让人类标注者在 Likert 和 pairwise 模式下评估同样的 style-transformed pairs，看 human pairwise 是否也能检测到 Likert 遗漏的偏差。如果 human pairwise 也显示 Blindspot，那 Blindspot 是测量范式的根本特性；如果 human Likert 能检测但 LLM Likert 不能，那问题出在 LLM 的 Likert 能力而非 Likert 本身。
  
- 为什么影响接收：没有 human validation，论文的核心 claim（"Likert scoring systematically misses style biases"）的解释空间仍然模糊。这是一个 soundness 问题——不是说结论错了，而是 evidence 不足以区分两种核心解释。
  
- 建议修改方向：
  1. 至少对一个 style axis（如 verbosity，效应量最大）的一个 subset（如 50 pairs）进行 human evaluation（Likert + pairwise），建立 human baseline
  2. 如果时间/资源不允许，应在 Limitations 中将此列为最主要的 open question，而非仅一笔带过

---

## Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] 风格轴覆盖面有限：仅 3 个轴难以支撑 "framework" 级别的泛化声明**

- 具体位置：Section 3.1, Section 6
- 问题：CSD 仅测试了 formality、verbosity、register 三个风格轴。虽然这三个轴是文献中最常讨论的，但 style bias 的类型远不止这些——complexity/readability、hedging/confidence、emoji/punctuation use、paragraph structure、bullet-point formatting 等均可能影响 judge 评分。论文标题和 abstract 使用 "framework" 一词暗示更广的适用性，但仅 3 轴的实验不足以支撑这一泛化。
- 建议：在 Limitations 中明确列出未覆盖的风格维度；或在修改时增加 1-2 个轴（如 complexity、hedging）来增强 generalizability evidence。

**W2 [warning] Table 1 设计可读性较差**

- 具体位置：Table 1 (page 5)
- 问题：Table 1 是论文最核心的结果表，但信息密度过高：5 个 judges × 3 benchmarks × 3 axes × 2 metrics (BT + Likert)，加上 footnotes 和 significance markers，读者很难快速抓住核心 pattern。"Cat." 列（Blindspot 分类）虽然有用但缩写不直观（↑, ↓, =）。"Likert d" 列的负值含义需要额外认知负荷。
- 建议：考虑将 Table 1 拆分为两个表（一个按 style axis 组织，一个按 judge 组织），或用 heatmap 可视化 BT vs. Likert 的差异模式。至少应在 caption 中添加一句 "how to read this table" 的指引。

**W3 [warning] Negative control（Claude Sonnet 4）的统计功效不足**

- 具体位置：Section 5.1 (最后一段), Appendix G
- 问题：Claude Sonnet 4 作为 negative control 是一个 excellent design choice，但当前样本量（n = 87 for formality, p = 0.091; n = 82 for verbosity, p = 0.284）的统计功效可能不足以 conclusively 排除偏差。论文在 Appendix G 中进行了 equivalence testing（TOST），表明效应在 ±13pp 等价区间内，但 ±13pp 对于实际应用来说仍是一个相当宽的区间。
- 为什么重要：如果 negative control 的 power 不足，"discriminative validity" 的论点就被削弱——可能 Claude 确实有某种程度的偏差，只是当前样本检测不到。
- 建议：明确报告 Claude Sonnet 4 在当前样本量下检测特定效应量（如 BT = 55%）的统计功效（1-β）；如果功效不足，应 acknowledge 这一限制。

**W4 [warning] Rewriting artifact 的处理略显草率**

- 具体位置：Appendix O (Rewriting Artifact Control), Section 3.2
- 问题：Appendix O（Table 15）显示同一风格方向的 double-rewrite 对中，judges 系统性偏好 LLM-polished 文本（BT P(orig) < 0.5）。这意味着 rewriting 本身就引入了 "polishing" artifact——即使风格不变，rewritten 文本也会被偏好。论文承认了这一点，但认为 same-style double-rewrite controls 能排除此 artifact（"confirming a rewriting artifact…that separates style from artifact effects"）。
  
  然而，same-style double-rewrite 只能控制 style-neutral 的 polishing effect；如果 polishing effect 与 style change 存在交互（即 formal rewriting 的 polishing 程度与 casual rewriting 不同），那么 style-specific 的 artifact 仍可能存在。
  
- 建议：在 Limitations 中讨论 style-specific polishing interaction 的可能性；或报告不同风格方向上 polishing effect 的大小是否一致。

**W5 [warning] Introduction motivating example 的准确性值得推敲**

- 具体位置：Section 1, paragraph 1
- 问题：开头的 "What is the average height for a male?" 例子声称 GPT-4o 在 1-10 Likert 上 "consistently selects the formal variant higher"。这是一个有效的 motivating example，但读者可能会问：(1) 这个例子是否是 cherry-picked？(2) "near-perfect correlation" 的 NLI 验证仅限于 content，但 formality 的改变本身可能影响 perceived answer quality（例如正式回答可能被认为更 authoritative）。如果这种感知是合理的，那它是否构成 "bias"？
- 建议：在 motivating example 旁边简短 acknowledge 这一 nuance——风格改变可能合法地影响 perceived quality，这正是为什么需要 controlled decomposition 来区分 style effect 和 quality effect。

---

## 小问题（不影响接收）

- **M1**: Section 4.1 的 statistical framework 描述较为压缩，hypothesis family 的 primary vs. exploratory 分类标准（"Analyses outside this grid are classified as either exploratory...or confirmatory"）需要更清晰的 justification——为什么这些特定假设被选为 primary？
  
- **M2**: Figure 2 (DAG) 中 R → Q 和 S → Q 的路径箭头在 150 DPI 下略难辨认颜色编码（红色 dashed vs. 黑色实线）。建议在打印版中增强对比度。

- **M3**: Section 5.6 (GEE Conditional Decomposition) 对 "exchangeable correlation" 假设的 justification 较弱。Appendix C 验证了 correlation robustness，但主文应至少一句话解释为何这个假设在此场景下合理。

- **M4**: References 格式整体一致，但部分条目的 venue 信息不完整（如一些 arXiv preprints 缺少版本号或提交日期）。

- **M5**: Limitations 段落提到 "evaluator-producer bias"，但该术语此前未出现过且未定义。建议在首次使用时简短解释或引用来源。

---

## Questions（需要作者澄清）

**Q1.** NLI threshold 0.98 的选择依据是什么？Appendix E 提供了 sensitivity sweep（11 个 thresholds），但主文未报告结果的 threshold 依赖性。在 threshold 从 0.98 降至 0.90 时，核心发现（BT significance + Likert non-significance）是否稳健？

**Q2.** Appendix M 的 100-point continuous Likert 实验仅用了 Qwen3-32B 一个 judge。其他 judges（尤其是 GPT-4o）是否也显示相同模式？如果是，这将大大加强论点。

**Q3.** GEE conditional decomposition（Table 3）显示 formality 的 confound 结构是 "conditional"——style effect 被 content quality 调节。这意味着在高质量内容上，formality bias 可能消失。作者是否探索了这种交互的方向和强度？

**Q4.** 论文使用 LLMBar 的 100 个 instruction-response pairs 作为 base dataset。这 100 个 pairs 是如何从 LLMBar 的完整数据集中选择的？selection criteria 是什么？是否可能引入 selection bias？

**Q5.** 对于 "measurement attenuation vs. construct divergence" 这一 open question，作者是否有后续研究计划来区分这两种解释？

---

## Missing References

1. **Girrbach et al. (2025/2026)**, "Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales" — 直接研究 LLM 在 Likert scale 上的评分行为，与 Appendix M 的 100-point continuous scale 实验高度相关。

2. **PRePair** (Jeong et al., 2025 中提出) — 论文引用了 Comparative Trap 但未讨论其提出的 PRePair 方法（在 pairwise 框架中整合 pointwise reasoning）。这可能是缓解 Blindspot 的替代方案，值得在 Related Work 或 Discussion 中提及。

3. 建议检查是否需要引用 **Kambhatla et al. (2024/2025)** 或类似的 calibration/scoring bias 工作，因为论文的核心论点涉及 scoring methodology 的 calibration 问题。

---

## Overall Assessment

**Overall**: 3.5 / 5 — **Borderline Conference**
**Confidence**: 4 / 5 — Quite sure; carefully read paper and checked key claims

### 判断理由

**支持 Conference (4.0) 的因素：**
- 实验设计异常严谨，控制层次远超该领域平均水平
- Likert Blindspot 的 empirical quantification 对 LLM evaluation 社区有直接实用价值
- GEE per-axis confound decomposition 是 genuinely novel 的分析贡献
- 7 种统计方法的 sensitivity hierarchy 是 compelling evidence
- 100-point continuous Likert 控制实验有力排除了 scale granularity 解释
- 附录 A-P 展示了出色的 rigor

**拉向 Findings (3.0) 的因素：**
- 核心概念（forced-choice > rating）在 psychometrics 中已有近百年历史；论文的 novelty 定位不够诚实
- 缺少 human validation 来区分 "detection vs. amplification"——这是 soundness 层面的 gap
- 仅 3 个风格轴限制了 generalizability
- Rewriting artifact 的处理不够彻底

**净判断：** 论文接近 Conference 门槛，但 N1（novelty 定位）和 N2（human validation）两个 Must-Fix 问题需要在 camera-ready 之前解决。如果作者能在修改中：(1) 重新定位 novelty narrative，(2) 补充哪怕一小组 human evaluation，(3) 增加 1-2 个风格轴——本文可以达到 4.0 (Conference) 水平。

---

## Detailed Comments（逐节）

### Abstract
信息密度高，核心数字（60% signal loss, 76-92% style variance）传递了关键 message。但第一句 "yet style features correlate with judge scores with near-perfect correlation" 过于绝对——76-92% explained variance 虽然很高但不是 "near-perfect"。建议措辞更 precise。

### Section 1 (Introduction)
Opening example 有效且令人印象深刻——height question 的 formal vs. casual variant 直觉上 should have identical quality，但 judge 评分不同。叙事逻辑清晰：problem → gap → our approach → findings → contributions。Contributions 列表（4 items）清晰但 item 1 的 "black-box controlled framework" 措辞可能被认为 overclaim——NLI gate 需要 access model probabilities，这不完全是 "black-box"。

### Section 2 (Related Work)
覆盖面广且组织良好。"Interventional Approaches to Judge Bias"、"Style Bias Detection and Mitigation"、"Measurement Sensitivity in NLG Evaluation"、"Bradley-Terry Models in Evaluation" 四个子节覆盖了主要相关领域。对 RATE 的讨论（最后两段）公平且 constructive。
- 遗漏：未讨论 Likert scale 的 methodological literature（如 Krosnick 1999 在 §2 cited 但仅一处），尤其是 acquiescence bias 和 central tendency bias——这些是 Likert scale 在社会科学中的 known problems，与 Likert Blindspot 直接相关。
- Section 2 与 Section 3 之间的过渡可以更平滑——从 "why existing methods are insufficient" 到 "here's our approach" 的逻辑跳跃稍显突兀。

### Section 3 (Method)
- §3.1 (Style-Controlled Rewriting): 设计合理。温度 0.7 的选择有 justification 吗？
- §3.2 (Content Preservation Verification): NLI gate 设计精巧，bidirectional entailment + forward-only direction-aware verification 是一个 well-thought-out protocol。但 "entailment threshold of 0.98" 这个 magic number 在主文中缺乏 justification（虽然 Appendix E 有 sweep）。
- §3.3 (Measurement Protocol): 清晰。Position control（每对评估两次 swapping order）是 good practice。
- §3.5 (Design Rationale): Figure 2 的 DAG 是论文的亮点之一——清晰展示了因果假设和 blocking 策略。"We do not claim that this DAG is a complete structural causal model" 的 caveat 是诚实且必要的。

### Section 4 (Experiments)
- §4.1 (Statistical Framework): 略显压缩。"Primary family of six hypotheses" 的选择标准需要更明确的 justification。Holm-Bonferroni correction 是 appropriate，但为什么选择 family-wise error rate 而不是 false discovery rate (FDR)？对于 exploratory analyses，FDR 可能更合适。

### Section 5 (Analysis)
- §5.1 (NLI Gate Validation): Thorough。92.1% formality / 82.6% verbosity pass precision 数据 convincing。但 FNR = 8.4% 可能意味着 gate 过滤掉了一些有效的 style transformations，creating survivorship bias。
- §5.2 (Measurement Sensitivity): 核心发现清晰呈现。Figure 3 (forest plot) 是 excellent visualization。对 Comparative Trap 的回应（六个独立控制）是 reasonable 但不 definitive（见 N2）。
- §5.3 (Cross-Axis Replication): 三个独立 judges replicate the Blindspot 是 strong evidence。
- §5.4 (Verbosity): 四个 judges 一致显示 Blindspot——最 robust 的结果。
- §5.5 (Register): Judge-dependent confound 的发现有趣但叙述过于压缩。这值得更多篇幅讨论 why register 表现不同。
- §5.6 (GEE Conditional Decomposition): 这是论文最 novel 的分析部分。Table 3 清晰展示 per-axis confound structure。但 "exchangeable correlation" 假设的 justification 几乎缺失。

### Section 6 (Conclusion)
适当总结了两个主要发现。"whether this reflects measurement attenuation or construct divergence" 的 open question 处理得当——诚实但不过度 hedge。最后一段关于 practical implications 简洁有力。

### Limitations
覆盖了主要 weak points，但遗漏了：(1) 缺少 human validation；(2) 仅 3 个风格轴的 coverage limitation；(3) base sample 仅 100 pairs。建议补充这三点。

### 格式与匿名
- **页数**: 正文 8 页（§1-§6 + Limitations），符合限制 ✓
- **匿名**: Title page 显示 "Anonymous ACL submission"，未发现自引泄漏或 acknowledgment ✓
- **引用格式**: natbib 括号风格，整体一致 ✓
- **ARR Checklist**: 未在 PDF 中（符合规定，应在 OpenReview form 中填写）✓


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 698 · 2026-05-22T03:33:57.101653+00:00_

Reviewer 2 审稿意见已收到。记录关键发现：

**R2 评分**: 3.5/5 (Borderline Conference)

**Must-Fix**:
- N1: Novelty 定位不够诚实（Thurstone 1927 已知现象的 domain transfer）
- N2: 缺 human validation 区分 detection vs. amplification

**Should-Fix**: W1 仅 3 轴覆盖面窄, W2 Table 1 可读性差, W3 Claude 负面控制功效不足, W4 rewriting artifact 处理不充分, W5 motivating example 需 nuance

**注意**: R2 在 S1 和 Q1 中将 NLI threshold 错误记为 0.98，论文实际使用 0.90（§3.2 明确写明）。交叉分享时需标注此误读。

等待 Reviewer 1 审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 66

## Round 66

2 recorded events


### User

_source line 699 · 2026-05-22T03:33:59.880506+00:00_

[Reviewer 2 审稿结果]:
Reviewer 2 审稿报告已提交至 Review Director。

**核心判断：Overall 3.5 (Borderline Conference)**

两个 Must-Fix 问题：
1. **Novelty 定位不诚实** — Likert Blindspot 本质是 Thurstone (1927) 已确立的 forced-choice > rating 原理在 LLM judge 领域的 empirical demonstration，论文叙事给人"全新发现"的印象，需重新定位 novelty 边界
2. **缺少 human validation** — 无法区分 pairwise 是"检测了真实偏差"还是"放大了微弱偏好"（Comparative Trap 问题），需至少一小组 human evaluation 建立 baseline

主要优势：实验控制层次出色（NLI gate + negative control + 7 种统计方法 + 100-point continuous Likert 控制实验），GEE per-axis confound decomposition 是 genuinely novel 的分析贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 700 · 2026-05-22T03:34:12.021517+00:00_

Reviewer 2 报告已收到。核心判断 3.5 (Borderline Conference)，两个 Must-Fix：novelty 定位 + 缺少 human validation。

等待 Reviewer 1（方法严谨性侧重）报告返回后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 67

## Round 67

6 recorded events


### User

_source line 701 · 2026-05-22T03:34:43.358605+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性与实验设计

**论文标题**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition

---

## 总体评分

**Overall Assessment**: 3.5 (Borderline Conference)
**一句话总结**: 论文提出了有价值的发现（Likert 系统性遗漏 pairwise 能检测到的风格偏差），实验框架设计较严谨，但 primary family 构成透明度不足、cross-rewriter 验证覆盖不够、负面控制统计功效偏弱，这些方法论缺口需要修补后才能支撑论文的全部 claims。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验管线（NLI gate → position balancing → BT + GEE）设计合理，多项 robustness check 到位，但 primary family 定义不透明、cross-rewriter 覆盖仅 1/4 judges、TOST 负面控制功效不足构成显著方法论缺口 |
| Excitement | 3.5/5 | Likert Blindspot 是对 LLM 评估社区有实际影响的发现，per-axis GEE decomposition 增添了新 insight；但 pairwise > Likert 对 subtle effects 更敏感这一结论在测量理论中并不意外，且 attenuation vs. divergence 的歧义未解限制了贡献的清晰度 |
| Confidence | 4/5 | 仔细阅读了全文含全部 16 个附录，熟悉论文使用的 BT、GEE、TOST 等统计方法 |

---

## Summary

本文引入 Controlled Style Decomposition (CSD)，通过 NLI-gated 内容控制、per-axis 风格改写和位置控制的 pairwise comparison，系统量化 LLM judge 的风格偏差。核心发现"Likert Blindspot"表明：标准 Likert 评分在中等效应量下系统性遗漏 pairwise 可检测到的风格偏差，信号损失达 60%+。GEE conditional decomposition 揭示了跨 judge 一致的 per-axis confound structure（verbosity 为 style-dominated，formality 受 original quality 调节）。实验涵盖 5 个 judges、3 个 benchmark、3 个 style axes，统计分析包括 7 种方法。

---

## 主要优势（Strengths）

**S1. 实用性强的核心发现。** Likert Blindspot 对 LLM 评估实践有直接影响：当前 AlpacaEval/MT-Bench 等主流排行榜依赖 Likert 评分，本文提供了系统性证据表明这种方法会遗漏中等强度的风格偏差。Table 1 在 5 个 judges × 3 个 axes 的广泛矩阵中一致展示了这一 pattern。

**S2. 多层验证的实验管线。** NLI gate (DeBERTa-v3-large, threshold 0.90) → consistency filter → position-balanced pairwise → BT + GEE 的管线设计体现了严谨的方法论思维。特别是：
- 11 个 NLI 阈值扫描（Table 8, Appendix E）验证了阈值选择的稳健性
- Same-style double-rewrite control（Table 15, Appendix O）隔离了 rewriting artifact
- 100-point continuous Likert scale（Appendix M）排除了 granularity explanation
- Formal power analysis（Appendix K, Table 11）量化了 Likert 所需的巨大样本量

**S3. 完善的统计框架。** 论文正确区分了 confirmatory vs. exploratory 分析，应用了 Holm-Bonferroni 校正，报告了 bootstrap 95% CIs。7 种统计方法的 sensitivity hierarchy（Table 2）是一个有说服力的展示——所有 Likert-based 方法均未达到显著性，而 pairwise methods 达到了。

**S4. GEE conditional decomposition 提供新 insight。** Table 3 揭示 verbosity 跨四个 judges 一致为 style-dominated（Style ORs 5.8–13.1），而 formality 展现 conditional confounding（Originality ORs 2.2–5.1 显著），这比简单的"judges have style bias"叙事更有深度。Appendix C 的 correlation structure comparison（Table 4）和 interaction test 验证了 GEE specification 的合理性。

**S5. 诚实的局限性讨论。** 论文公开讨论了 evaluator-producer bias（Qwen3-32B 同时作 rewriter 和 judge）、measurement attenuation vs. construct divergence 的歧义、以及样本量约束。这种透明度是受欢迎的。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Primary family 构成缺乏透明度
- **位置**: Section 4.1
- **问题**: 论文声明"a primary family of six hypothesis tests (three judges × two axes)"并应用 Holm-Bonferroni 校正，但从未明确指出哪三个 judges 被纳入 primary family。论文描述了四个 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）加一个 negative control（Claude Sonnet 4）。如果 primary family 排除了 Gemini，需要明确声明并提供理由。
- **为什么影响接收**: 如果纳入 Gemini（4 judges × 2 axes = 8 tests），Holm-Bonferroni 校正将更保守，部分结果可能失去 adjusted significance。当前写法存在 post-hoc selection 的嫌疑——reviewer 无法验证 primary family 是否在看到数据前确定。这是 confirmatory analysis 的基本透明度要求。
- **建议**: 在 Section 4.1 明确列出三个 primary judges 的名称；如果 Gemini 被排除，说明是因为它是"supplementary architecture validation"（Section 3.4 的措辞暗示了这一点，但需要显式关联到 primary family 定义）。同时报告 8-test primary family 下的 adjusted p-values 作为 sensitivity analysis。

**N2** [critical] Cross-rewriter independence 验证覆盖不足
- **位置**: Appendix D (Section D)
- **问题**: 论文仅测试了一个 judge（Qwen3-32B）配合替代 rewriter（GPT-4o）。四个 target judges 中的另外三个（GPT-4o as judge, Llama-3.3-70B, Gemini）没有 cross-rewriter 验证。
- **具体缺口**:
  (a) GPT-4o as judge 使用 Qwen3-32B 作 rewriter——GPT-4o 可能检测到 Qwen3-32B 特有的改写痕迹（artifacts），而这与 style bias 无关。没有用第三方 rewriter 验证 GPT-4o judge 的结果。
  (b) Llama-3.3-70B 和 Gemini 完全没有 cross-rewriter 检验。
- **为什么影响接收**: Evaluator-producer bias 是论文自己承认的主要 threat to validity（Limitations 段落）。仅用一个 judge 的 cross-rewriter test 不足以支撑"Blindspot is rewriter-independent"这一 generalized claim。
- **建议**: 至少对一个额外 judge 执行 cross-rewriter validation（优先选 GPT-4o as judge，因为它是最重要的 target judge 且当前使用同一家族外的 rewriter）。如果资源不允许完整复制，至少在 Limitations 中明确承认覆盖不足并 downgrade 相关 claim 的强度。

**N3** [critical] 负面控制（Claude Sonnet 4）的 TOST equivalence testing 功效不足、等价边界过宽
- **位置**: Appendix G
- **问题**: 
  (a) 在 Δ = 10pp 下 TOST underpowered（n = 87）。在 Δ = 15pp 下两个 axes 落入等价区间。
  (b) 论文确认的最小 bias 为 +13pp（GPT-4o formality, BT 60.7%）。Δ = 15pp 的等价边界几乎涵盖了这个已知正效应——这意味着 Claude 可能有高达 ~14pp 的 bias 而 TOST 仍然宣告等价。
  (c) n = 87 的样本量远低于 Appendix K power analysis 建议的水平。
- **为什么影响接收**: 负面控制是论文实验设计的重要组成部分（证明 CSD 不是对所有 judges 产生 false positive）。如果等价边界涵盖已知正效应的范围，negative control 的 discriminative power 存疑。
- **建议**: 三选一：(a) 增加 Claude 的样本量使 Δ = 10pp 有足够功效；(b) 将 Claude 重新定位为"insufficient evidence for bias"而非"negative control"；(c) 报告 TOST 在 n = 87 下能 reject 的最小 Δ 值，让读者自行判断。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 因果框架表述不一致
- **位置**: Title, Abstract, Section 3.5, Figure 2
- **问题**: 框架名称"Controlled Style Decomposition"和 DAG（Figure 2）带有因果含义。Section 3.5 正确地 hedge 为"interventionist rather than formal causal evidence"并声明不 claim SUTVA。但 Abstract 使用"controlled"暗示因果干预，Section 1 引用"the causal variant"。论文在因果语言的使用上不一致。
- **建议**: 统一术语——全文使用"interventionist"或"controlled manipulation"而非暗示正式因果推断的语言。Figure 2 的 caption 已标注"design rationale, not a claim of perfect identification"，这是好的，但需要全文一致。

**W2** [warning] Bradley-Terry 模型的 IIA 假设未讨论
- **位置**: Section 3.3, Appendix H
- **问题**: BT 模型假设 Independence of Irrelevant Alternatives。虽然 pairwise 配置下 IIA 问题不如 multi-alternative 严重，但论文未提及此假设。Appendix H 报告了 goodness-of-fit（deviance = 52.86, df = 16, p = 0.185 for formality），但这测试的是模型拟合度而非 IIA。更关键的是，Appendix H 发现 formality 存在显著方向异质性（68.9% vs. 52.6%, Fisher's p = 0.015），表明 BT 的单参数公式可能遗漏了重要的效应异质性。
- **建议**: (a) 承认 IIA 假设；(b) 考虑 stratified BT（按 original-text direction 分层估计 win probability），检验结论是否在分层后仍然成立。

**W3** [warning] NLI gate FNR 估计基于过小样本
- **位置**: Section 5.1
- **问题**: FNR 基于 12 个手动评估的 rejected pairs（"8 of 12 rejected pairs judged content-preserving"），得出 FNR ≈ 8.4%。n = 12 的 Wilson 95% CI 约为 [2%, 28%]，区间极宽。GPT-4o cross-validation 报告了 pass precision（92.1% / 82.6%）但未直接报告 FNR 的置信区间。
- **建议**: 报告 FNR 的 bootstrapped 或 Wilson CI；如果可能，在更大样本上验证。

**W4** [warning] Verbosity 轴的 direction-aware NLI gating 引入不对称过滤
- **位置**: Section 3.2, Appendix F
- **问题**: Direction-aware gating 为 verbosity 额外放入 21 个 pairs（比 bidirectional gating 多 32%）。这些 pairs 通过了更宽松的标准（单向 entailment），可能引入 selection bias——这些 pairs 中部分内容变化可能未被 NLI 完全捕获。论文报告 BT estimates"statistically indistinguishable"但未检验两组 NLI scores 是否存在系统性差异。
- **建议**: 报告 direction-aware 额外放入的 pairs 与 bidirectional-pass pairs 在 NLI score 分布上的比较（如 KS test 或分位数对比），确认无系统性质量差异。

**W5** [warning] Measurement attenuation vs. construct divergence 歧义未解
- **位置**: Section 5.2, Section 5.6, Section 6
- **问题**: 论文提出两种对 Likert Blindspot 的解释——(1) measurement attenuation（Likert 灵敏度不够），(2) construct divergence（Likert 和 pairwise 测量不同构念）——但未能在两者之间做出判断。Bootstrap attenuation 分析（Appendix J）显示 Likert d 在 n = 355 仍近零，排除了纯 power 问题；100-point continuous scale（Appendix M）排除了 granularity。但如果确实是 construct divergence（Likert 测量 absolute quality，pairwise 测量 ordinal preference），则"Blindspot"这一术语暗示 Likert"遗漏"了什么，而实际上可能只是"测量了不同的东西"——这弱化了论文的核心 narrative。
- **建议**: 在 Section 6 (Conclusion) 中更明确地定位：如果两种解释都成立，则论文的 practical contribution 在于"研究者应该同时使用两种方法以获得完整画面"；如果偏向 attenuation，需要更多 evidence（如在已知有 bias 的 setting 中 Likert 能否在巨大 n 下检测到效应）。

**W6** [warning] 生态效度（ecological validity）讨论不足
- **位置**: Limitations
- **问题**: CSD 检测的 bias 来自人工改写的风格变体。自然发生的文本风格变化可能更微妙、更多轴交织，且伴随内容差异。论文的 Limitations 提到了 axis interaction，但未讨论从 controlled manipulation 到 naturalistic evaluation 的 generalizability gap。
- **建议**: 在 Limitations 中增加一句关于 ecological validity 的讨论：CSD 的发现是否能 generalize 到非实验设置下的自然文本评估。

---

## 小问题（Minor Issues）

- **Table 3 GEE CIs 宽度**: 部分配置的 OR CI 极宽（如 Gemini form: Style OR CI 覆盖 0.58–4.54），表明 GEE 在某些 judge×axis 上估计精度不足。应在 Table 3 附注或正文中 acknowledge。
- **Figure 1 信息密度**: CSD pipeline overview 流程较密，NLI gate 的 branching logic 不够直观。可考虑分解为两个 sub-figures 或增加视觉层次。
- **Section 3.4 LLMBar 标签描述**: "human-verified quality labels"——简要说明这些 labels 捕获什么维度的 quality（task correctness? response quality?）会有助于读者理解。
- **"Blindspot" 术语标记**: 作为 coined term，建议首次使用时用斜体或引号标记，并给出明确定义。当前定义散布在多处（Abstract: "Likert scoring systematically misses style biases that pairwise comparison detects"; Section 1: 更长的描述），建议在 Introduction 给出一次简洁的正式定义。

---

## Questions for Authors

**Q1.** Primary family 包含哪三个 judges？请明确列出并说明排除第四个 target judge 的理由。如果在实验设计阶段已预注册此选择，请引用预注册。

**Q2.** Cross-rewriter independence test 仅覆盖 Qwen3-32B as judge 是否是资源约束？如果是，能否至少对 GPT-4o as judge 用 Llama 或 Gemini 作为替代 rewriter 做一个小规模验证？

**Q3.** 对于 Claude Sonnet 4 的 TOST，在 n = 87 下能 reject 的最小 Δ 具体是多少？如果该 Δ 大于论文中检测到的最小正效应（+13pp），这是否 invalidate negative control 的角色？

**Q4.** Appendix H 发现 formality 存在显著方向异质性（68.9% vs. 52.6%, Fisher's p = 0.015）。是否考虑过 stratified BT（按 original text direction 分层估计 win probability）？如果是，分层后的 BT estimates 是否与 GEE 的 Originality effect 一致？

**Q5.** Table 2 的 sensitivity hierarchy 显示所有 7 种 Likert-based 方法均未达显著性。这是否可能部分归因于 LLMBar 样本量（n ≈ 88 post-NLI）不足，而非 Likert 方法的固有局限？论文的 formal power analysis（Appendix K）显示部分配置需 n > 10,000 才能达到 80% power——这个数量级是否使 Likert vs. pairwise 的比较在方法论上不公平（不同统计效率的方法需要不同样本量才能公平比较）？

---

## Missing References

未发现显著遗漏。Related work 覆盖了近期 LLM judge bias 研究（Shi et al., 2025; Lin et al., 2025; Muragadoss et al., 2025）、RATE 方法论（Reber et al., 2025）、BT 在 NLP 评估中的应用，以及测量理论基础（Thurstone 1927, Stevens 1946, Krosnick 1999）。建议考虑补充：
- Zheng et al. (2024) "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" 的更详细讨论（虽已引用但可加强对比）
- 如有 2025-2026 年关于 Likert scale limitations in NLG evaluation 的新工作，值得补充

---

## 格式合规检查

| 检查项 | 结果 |
|--------|------|
| 正文 ≤ 8 页 | ✓ 合规。Sections 1-6 + Limitations 在 8 页内完成 |
| Double-blind 匿名 | ✓ "Anonymous ACL submission"，未见作者信息 |
| ACL 双栏格式 | ✓ 正确使用 |
| Limitations 章节 | ✓ 存在，覆盖 3 个要点（evaluator-producer bias、methodology/scale design、ecological validity），篇幅适中 |
| ARR Checklist | ✓ 不在 PDF 中（符合规定：在 OpenReview form 中填写） |
| 参考文献格式 | ✓ 一致，未见明显格式问题 |

---

## Detailed Comments by Section

### Section 1 (Introduction)
- 开头的"average height for a male"例子直观有效，但"causal variant"措辞暗示了正式的因果推断，与 Section 3.5 的 hedging 不一致（参见 W1）。
- "70–92% of observed preferences originate from surface-level style cues"的引用（Muragadoss et al., 2025; Sournik et al., 2020）——确认这些引用的测量方法是否与本文的 CSD 可比。

### Section 2 (Related Work)
- 覆盖全面，将 CSD 与 RATE（Reber et al., 2025）的区别阐述清楚（per-axis isolation + NLI gate + forced-choice vs. Likert ATE + post-hoc correction）。
- "CASSE (Cho et al., 2026)"和"FairJudge (Yang et al., 2026)"是 concurrent work，能否简要讨论 CSD 与它们的互补性？

### Section 3 (Method)
- Section 3.1: Style-controlled rewriting 的 prompt 设计（binary classification → opposite pole rewriting）清晰。但"a distant balanced pair where the rewrite changed only in style"的表述过强——NLI gate 保证 semantic content 不变，但 writing quality/fluency 可能随改写发生变化（Table 15 的 double-rewrite 数据证实了这一点）。
- Section 3.2: NLI gate 的 bidirectional entailment 要求合理。Direction-aware verbosity gating 的 rationale（增加内容不违反 forward entailment）在直觉上合理，但需量化其影响（参见 W4）。
- Section 3.3: BT 使用所有 observations（含 inconsistent pairs）是标准做法，且 Section 3.3 有 justification。但未讨论 inconsistent pair rate——如果 inconsistency 率很高（如 >30%），可能表明 judges 在边界 cases 上 noise 很大。
- Section 3.5: DAG (Figure 2) 标注为"design rationale"是恰当的。三个识别假设清晰。但假设 (iii)（"style rewrite introduces no systematic differences beyond the target axis"）是最关键的，且最难验证。Same-style double-rewrite（Appendix O）提供了部分验证，但它只检验了 within-style rewriting artifact，不检验 cross-style rewriting 是否引入了 axis 之外的 confound。

### Section 4 (Experiments)
- Section 4.1: Primary family 定义的透明度问题（参见 N1）。Exploratory vs. confirmatory 分类的逻辑应更 explicit。
- Section 3.4 / 4: LLMBar (n = 100, post-NLI n = 88) 是一个小到中等的 benchmark。scaled replication (n = 355) 仅覆盖 formality × Qwen3-32B 一个 cell，对 generalizability 的支持有限。

### Section 5 (Analysis)
- Section 5.1: NLI gate validation 的 FNR 估计样本量过小（参见 W3）。GPT-4o cross-validation (92.1% / 82.6% precision) 是一个好的补充验证。
- Section 5.2: Likert vs. Pairwise 灵敏度比较是论文的核心贡献。Figure 4 的 detection probability 曲线直观展示了两种方法的分离——BT 在 n ≈ 62 达到 80% power，而 Likert ATE 在 n = 355 仍然 flat near zero。这是强有力的 evidence。
- Section 5.3: Cross-judge replication（三个独立 judges replicate the Blindspot）增强了结论的稳健性。
- Section 5.4: Cross-axis replication for verbosity 跨四个 judges 一致——这是最一致的发现。
- Section 5.5: Register 作为 judge-dependent confound 的发现有趣但仅为 exploratory。
- Section 5.6: GEE conditional decomposition 是论文的第二个主要贡献。Table 3 的 per-axis confound structure 是新颖的。但部分 CI 很宽（参见 Minor）。

### Section 6 (Conclusion)
- 两个主要发现的总结清晰。"whether this reflects measurement attenuation or construct divergence"的 framing 诚实但留下了悬念（参见 W5）。

### Limitations
- 覆盖了关键点。建议增加 ecological validity 讨论（参见 W6）和 cross-rewriter 覆盖不足的明确承认。

---

## 综合判断

本文的核心贡献——Likert Blindspot 的系统性 demonstration——是扎实的。跨 5 个 judges、3 个 benchmarks 和 7 种统计方法的一致性令人信服。GEE decomposition 揭示的 per-axis confound structure 增添了深度。

主要顾虑集中在三个方法论缺口：(1) primary family 构成未透明公开，影响 FWER 控制的可信度；(2) cross-rewriter 验证仅覆盖 1/4 target judges，限制了 rewriter-independence claim 的强度；(3) 负面控制的 TOST 等价边界过宽，无法有效排除中等 bias。

这些问题均可在修改中解决。如果 N1-N3 得到充分回应（特别是 N1 的透明度和 N3 的 TOST re-framing），本文有潜力达到 4.0 (Conference) 的水平。当前评分 3.5 (Borderline Conference) 反映了这些未解决的方法论顾虑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-22T03:35:18.814093+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（完整原文）\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n\n### Strengths\n- S1. Likert Blindspot 对 LLM 评估实践有直接影响，Table 1 在 5 judges × 3 axes 矩阵中一致展示\n- S2. 多层验证管线（NLI gate → consistency filter → position-balanced pairwise → BT + GEE），含 11 NLI 阈值扫描、double-rewrite control、100-point continuous Likert、formal power analysis\n- S3. 统计框架完善：confirmatory vs. exploratory 区分、Holm-Bonferroni 校正、7 种方法 sensitivity hierarchy\n- S4. GEE conditional decomposition 揭示 per-axis confound structure（verbosity style-dominated, formality conditional）\n- S5. 诚实的局限性讨论\n\n### Must-Fix\n- **N1 [critical]**: Primary family 构成缺乏透明度——Section 4.1 声明 \"six hypothesis tests (three judges × two axes)\" 但未指明哪三个 judges。四个 target judges 中排除哪一个？如果纳入 Gemini（4×2=8 tests），Holm-Bonferroni 更保守，部分结果可能失去 adjusted significance。存在 post-hoc selection 嫌疑。\n- **N2 [critical]**: Cross-rewriter independence 验证仅覆盖 1/4 judges（Qwen3-32B judge + GPT-4o rewriter）。GPT-4o as judge、Llama-70B、Gemini 均无 cross-rewriter 检验。不足以支撑 \"Blindspot is rewriter-independent\" 的 generalized claim。\n- **N3 [critical]**: 负面控制 TOST Δ=15pp 过宽——论文最小 confirmed bias 为 +13pp（GPT-4o formality），Claude 可能有高达 ~14pp bias 而 TOST 仍宣告等价。n=87 功效不足。\n\n### Should-Fix\n- **W1**: 因果框架表述不一致——\"Controlled Style Decomposition\" 和 DAG 带因果含义，但 §3.5 hedge 为 \"interventionist\"。全文术语需统一。\n- **W2**: BT 模型 IIA 假设未讨论。Appendix H 发现 formality 存在显著方向异质性（68.9% vs 52.6%, Fisher p=0.015），BT 单参数公式可能遗漏效应异质性。\n- **W3**: NLI gate FNR 估计基于仅 12 个 rejected pairs（Wilson 95% CI ≈ [2%, 28%]），样本量过小。\n- **W4**: Verbosity direction-aware NLI gating 额外放入 21 pairs（多 32%），可能引入 selection bias。\n- **W5**: Measurement attenuation vs. construct divergence 歧义未解——如果是 construct divergence，\"Blindspot\" 术语暗示 Likert \"遗漏\" 了什么，实际上可能只是 \"测量了不同的东西\"。\n- **W6**: 生态效度讨论不足——controlled manipulation 到 naturalistic evaluation 的 generalizability gap。\n\n### Questions\n- Q1: Primary family 包含哪三个 judges？\n- Q2: Cross-rewriter test 仅覆盖 Qwen3-32B 是否资源约束？\n- Q3: Claude TOST 在 n=87 下能 reject 的最小 Δ 是多少？\n- Q4: 是否考虑过 stratified BT（按 original text direction 分层）？\n- Q5: Likert vs pairwise 比较是否在方法论上不公平（不同统计效率需要不同样本量）？\n\n### Missing References\n无显著遗漏。建议补充 Zheng et al. (2024) 更详细讨论。\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、Questions (Q1-Q5) 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（完整原文）\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n\n### Strengths\n- S1. Likert Blindspot 对 LLM 评估实践有直接影响，Table 1 在 5 judges × 3 axes 矩阵中一致展示\n- S2. 多层验证管线（NLI gate → consistency filter → position-balanced pairwise → BT + GEE），含 11 NLI 阈值扫描、double-rewrite control、100-point continuous Likert、formal power analysis\n- S3. 统计框架完善：confirmatory vs. exploratory 区分、Holm-Bonferroni 校正、7 种方法 sensitivity hierarchy\n- S4. GEE conditional decomposition 揭示 per-axis confound structure（verbosity style-dominated, formality conditional）\n- S5. 诚实的局限性讨论\n\n### Must-Fix\n- **N1 [critical]**: Primary family 构成缺乏透明度——Section 4.1 声明 \"six hypothesis tests (three judges × two axes)\" 但未指明哪三个 judges。四个 target judges 中排除哪一个？如果纳入 Gemini（4×2=8 tests），Holm-Bonferroni 更保守，部分结果可能失去 adjusted significance。存在 post-hoc selection 嫌疑。\n- **N2 [critical]**: Cross-rewriter independence 验证仅覆盖 1/4 judges（Qwen3-32B judge + GPT-4o rewriter）。GPT-4o as judge、Llama-70B、Gemini 均无 cross-rewriter 检验。不足以支撑 \"Blindspot is rewriter-independent\" 的 generalized claim。\n- **N3 [critical]**: 负面控制 TOST Δ=15pp 过宽——论文最小 confirmed bias 为 +13pp（GPT-4o formality），Claude 可能有高达 ~14pp bias 而 TOST 仍宣告等价。n=87 功效不足。\n\n### Should-Fix\n- **W1**: 因果框架表述不一致——\"Controlled Style Decomposition\" 和 DAG 带因果含义，但 §3.5 hedge 为 \"interventionist\"。全文术语需统一。\n- **W2**: BT 模型 IIA 假设未讨论。Appendix H 发现 formality 存在显著方向异质性（68.9% vs 52.6%, Fisher p=0.015），BT 单参数公式可能遗漏效应异质性。\n- **W3**: NLI gate FNR 估计基于仅 12 个 rejected pairs（Wilson 95% CI ≈ [2%, 28%]），样本量过小。\n- **W4**: Verbosity direction-aware NLI gating 额外放入 21 pairs（多 32%），可能引入 selection bias。\n- **W5**: Measurement attenuation vs. construct divergence 歧义未解——如果是 construct divergence，\"Blindspot\" 术语暗示 Likert \"遗漏\" 了什么，实际上可能只是 \"测量了不同的东西\"。\n- **W6**: 生态效度讨论不足——controlled manipulation 到 naturalistic evaluation 的 generalizability gap。\n\n### Questions\n- Q1: Primary family 包含哪三个 judges？\n- Q2: Cross-rewriter test 仅覆盖 Qwen3-32B 是否资源约束？\n- Q3: Claude TOST 在 n=87 下能 reject 的最小 Δ 是多少？\n- Q4: 是否考虑过 stratified BT（按 original text direction 分层）？\n- Q5: Likert vs pairwise 比较是否在方法论上不公平（不同统计效率需要不同样本量）？\n\n### Missing References\n无显著遗漏。建议补充 Zheng et al. (2024) 更详细讨论。\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、Questions (Q1-Q5) 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-22T03:35:46.995826+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 28181
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-22T03:35:47.146955+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（完整原文）\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n\n### Strengths\n- S1. 实验设计严谨，控制充分（NLI gate + negative control + position control + cross-benchmark replication + cross-rewriter independence）\n- S2. 7 种统计方法 sensitivity hierarchy + GEE per-axis confound decomposition 是 genuinely novel\n- S3. Measurement attenuation vs. construct divergence 两种解释的公平讨论\n- S4. 100-point continuous Likert 是关键控制实验\n- S5. Claude Sonnet 4 negative control 的 discriminative validity\n- S6. 与 RATE 的对比公平且建设性\n\n### Must-Fix\n- **N1 [critical]**: Novelty 定位不够诚实——Likert Blindspot 本质是 Thurstone (1927) forced-choice > rating 原理在 LLM judge 领域的 empirical demonstration，非概念新发现。论文整体叙事给人 \"全新发现\" 印象。需重新定位 novelty：从 \"discovering the Blindspot\" 调整为 \"providing the first controlled, per-axis quantification of this psychometric phenomenon in LLM judges\"。\n- **N2 [critical]**: Detection vs. Amplification 问题未充分解决，缺少 human validation。六个独立 controls 虽然排除了部分 artifactual 解释，但不能在根本上区分 \"pairwise 检测了真实偏差\" vs. \"pairwise 放大了微弱偏好\"。需 human evaluation（至少 50 pairs）建立 baseline。\n\n### Should-Fix\n- **W1**: 仅 3 个风格轴（formality, verbosity, register）难以支撑 \"framework\" 级别泛化声明。\n- **W2**: Table 1 信息密度过高，可读性差——5 judges × 3 benchmarks × 3 axes × 2 metrics，读者难以快速抓住核心 pattern。\n- **W3**: Claude Sonnet 4 统计功效不足（n=87, TOST Δ=15pp 过宽）。\n- **W4**: Rewriting artifact 处理略显草率——same-style double-rewrite 只控制 style-neutral polishing，style-specific polishing interaction 未讨论。\n- **W5**: Introduction motivating example 准确性值得推敲——formality 改变可能合法影响 perceived quality，需 acknowledge 这一 nuance。\n\n### Questions\n- Q1: NLI threshold 0.98 的选择依据？（注：论文实际用的是 0.90，R2 可能笔误）\n- Q2: 100-point continuous Likert 仅用 Qwen3-32B，其他 judges 是否也显示相同 pattern？\n- Q3: GEE Table 3 中 formality confound 的 interaction 方向和强度？\n- Q4: LLMBar 100 pairs 的 selection criteria？\n- Q5: 后续研究计划区分 attenuation vs. divergence？\n\n### Missing References\n1. Girrbach et al. (2025/2026) \"Likert or Not\" — 研究 LLM 在 Likert scale 上的评分行为\n2. PRePair (Jeong et al., 2025) — pairwise + pointwise 整合方法\n3. Kambhatla et al. (2024/2025) — calibration/scoring bias\n\n### Detailed Comments\n- Abstract: 第一句 \"near-perfect correlation\" 过于绝对（76-92% ≠ near-perfect）\n- Introduction: \"black-box controlled framework\" 可能 overclaim（NLI gate 需要 model probabilities？）\n- §2 Related Work: 遗漏 acquiescence bias 和 central tendency bias\n- §3.2: NLI threshold \"0.98\" 在主文缺 justification（注：实际为 0.90）\n- §4.1: Primary family 选择标准需 justification\n- §5.5: Register 叙述过于压缩\n- §6: 结论适当但 practical implications 可再展开\n- Limitations: 遗漏 human validation、3 轴限制、base sample 仅 100 pairs\n\n---\n\n请对以上每个 Must-Fix (N1-N2)、Should-Fix (W1-W5)、Questions (Q1-Q5) 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（完整原文）\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n\n### Strengths\n- S1. 实验设计严谨，控制充分（NLI gate + negative control + position control + cross-benchmark replication + cross-rewriter independence）\n- S2. 7 种统计方法 sensitivity hierarchy + GEE per-axis confound decomposition 是 genuinely novel\n- S3. Measurement attenuation vs. construct divergence 两种解释的公平讨论\n- S4. 100-point continuous Likert 是关键控制实验\n- S5. Claude Sonnet 4 negative control 的 discriminative validity\n- S6. 与 RATE 的对比公平且建设性\n\n### Must-Fix\n- **N1 [critical]**: Novelty 定位不够诚实——Likert Blindspot 本质是 Thurstone (1927) forced-choice > rating 原理在 LLM judge 领域的 empirical demonstration，非概念新发现。论文整体叙事给人 \"全新发现\" 印象。需重新定位 novelty：从 \"discovering the Blindspot\" 调整为 \"providing the first controlled, per-axis quantification of this psychometric phenomenon in LLM judges\"。\n- **N2 [critical]**: Detection vs. Amplification 问题未充分解决，缺少 human validation。六个独立 controls 虽然排除了部分 artifactual 解释，但不能在根本上区分 \"pairwise 检测了真实偏差\" vs. \"pairwise 放大了微弱偏好\"。需 human evaluation（至少 50 pairs）建立 baseline。\n\n### Should-Fix\n- **W1**: 仅 3 个风格轴（formality, verbosity, register）难以支撑 \"framework\" 级别泛化声明。\n- **W2**: Table 1 信息密度过高，可读性差——5 judges × 3 benchmarks × 3 axes × 2 metrics，读者难以快速抓住核心 pattern。\n- **W3**: Claude Sonnet 4 统计功效不足（n=87, TOST Δ=15pp 过宽）。\n- **W4**: Rewriting artifact 处理略显草率——same-style double-rewrite 只控制 style-neutral polishing，style-specific polishing interaction 未讨论。\n- **W5**: Introduction motivating example 准确性值得推敲——formality 改变可能合法影响 perceived quality，需 acknowledge 这一 nuance。\n\n### Questions\n- Q1: NLI threshold 0.98 的选择依据？（注：论文实际用的是 0.90，R2 可能笔误）\n- Q2: 100-point continuous Likert 仅用 Qwen3-32B，其他 judges 是否也显示相同 pattern？\n- Q3: GEE Table 3 中 formality confound 的 interaction 方向和强度？\n- Q4: LLMBar 100 pairs 的 selection criteria？\n- Q5: 后续研究计划区分 attenuation vs. divergence？\n\n### Missing References\n1. Girrbach et al. (2025/2026) \"Likert or Not\" — 研究 LLM 在 Likert scale 上的评分行为\n2. PRePair (Jeong et al., 2025) — pairwise + pointwise 整合方法\n3. Kambhatla et al. (2024/2025) — calibration/scoring bias\n\n### Detailed Comments\n- Abstract: 第一句 \"near-perfect correlation\" 过于绝对（76-92% ≠ near-perfect）\n- Introduction: \"black-box controlled framework\" 可能 overclaim（NLI gate 需要 model probabilities？）\n- §2 Related Work: 遗漏 acquiescence bias 和 central tendency bias\n- §3.2: NLI threshold \"0.98\" 在主文缺 justification（注：实际为 0.90）\n- §4.1: Primary family 选择标准需 justification\n- §5.5: Register 叙述过于压缩\n- §6: 结论适当但 practical implications 可再展开\n- Limitations: 遗漏 human validation、3 轴限制、base sample 仅 100 pairs\n\n---\n\n请对以上每个 Must-Fix (N1-N2)、Should-Fix (W1-W5)、Questions (Q1-Q5) 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 705 · 2026-05-22T03:35:48.708686+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1561
}
```

</details>

---


### Assistant

_source line 706 · 2026-05-22T03:35:51.859535+00:00_

交叉分享已派发，等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 68

## Round 68

2 recorded events


### User

_source line 707 · 2026-05-22T03:35:54.557485+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断**: Overall 3.5 (Borderline Conference)，Soundness 3.5/5，Excitement 3.5/5。

**三个 Must-Fix 问题**:
1. Primary family（6 tests = 3 judges × 2 axes）未明确列出哪三个 judges，存在 post-hoc selection 嫌疑
2. Cross-rewriter independence test 仅覆盖 Qwen3-32B 一个 judge，其余三个 target judges 无验证
3. Claude Sonnet 4 负面控制的 TOST Δ=15pp 过宽，几乎涵盖已检测到的最小正效应（+13pp）

**五个 Should-Fix**: 因果框架表述不一致、BT IIA 假设未讨论、NLI gate FNR 样本过小（n=12）、verbosity direction-aware gating 的不对称过滤、measurement attenuation vs. construct divergence 歧义未解。

格式合规，正文 ≤8 页，double-blind 匿名正确。如果 N1-N3 在 revision 中解决，论文有潜力升至 4.0 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 708 · 2026-05-22T03:35:59.519682+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 69

## Round 69

2 recorded events


### User

_source line 709 · 2026-05-22T03:38:06.550882+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix

**[AGREE] R1-N1: Primary family 构成缺乏透明度**

同意这是一个严重的透明度问题。Section 4.1 明确声明 "six hypothesis tests (three judges × two axes)" 但四个 target judges 中哪三个被纳入 primary family 完全没有说明。这一遗漏在 Table 1 中也未注明。如果被排除的 judge 是 Gemini（其 formality confound 在 Table 3 中表现为 originality-dominated 而非 style-dominated，行为模式与其他三个 judge 不同），则存在 post-hoc cherry-picking 的嫌疑——先观察结果再选择 primary family 会 inflate Type I error rate。

补充我自己的观察：即使作者有 pre-registration 理由（如 Gemini 被归为 exploratory 是因为它是唯一的 Flash-tier 模型），也必须在 §4.1 中明确说明选择标准和理由。当前写法让 reviewer 无法验证 multiple comparison correction 的有效性。

**[AGREE] R1-N2: Cross-rewriter independence 验证覆盖面不足**

同意 Appendix D 仅测试了一个 judge（Qwen3-32B）+一个替代 rewriter（GPT-4o），覆盖面确实不足以支撑 generalized claim。

但我要补充一个 nuance：R1 的关注点（"不足以支撑 rewriter-independent 的 generalized claim"）是正确的，但严重性需要 contextualize。论文的核心 claim 不是 "Blindspot is rewriter-independent"，而是 "Likert systematically misses what pairwise detects"——这一 claim 在全部四个 judges 上用同一 rewriter（Qwen3-32B）得到了 consistent confirmation（Table 1）。Appendix D 的 cross-rewriter check 是一个 supplementary robustness test，其单 judge 覆盖削弱的是 robustness 论证的 generalizability，而非核心 finding 本身。

建议修改：将 Appendix D 的结论从 "the Blindspot persists with an independent rewriter" 修改为 "the Blindspot persists with an independent rewriter for at least one judge configuration; broader cross-rewriter validation remains for future work"。

**[AGREE] R1-N3: 负面控制 TOST Δ 过宽，n=87 功效不足**

完全同意。这与我在自己的审稿中提出的 W3 一致。

R1 精确地指出了核心矛盾：论文最小 confirmed bias 约 +13pp（GPT-4o formality BT），而 TOST 等价区间 Δ=±13pp（Appendix G），意味着 Claude 可能有接近 confirmed bias 阈值的偏差而仍被宣告等价。这严重削弱了 "discriminative validity" 论点。

进一步补充：Appendix G 报告 TOST 通过的前提下，n=87 对 BT=55%（中等偏差）的检测功效应被明确报告。如果 power < 80%，论文需要 acknowledge negative control 的 conclusive power 不足，而非将 TOST 通过作为 strong evidence of absence。

---

## Should-Fix

**[REBUT] R1-W1: 因果框架表述不一致**

R1 认为 "Controlled Style Decomposition" 和 DAG 暗示因果声明，与 §3.5 的 "interventionist" 定位不一致。我认为这个批评过于严格。

论文在 §3.5 (page 4-5) 做了清晰的 caveat："our approach provides interventionist rather than true causal evidence: we do not claim that this DAG is a complete structural causal model." 在因果推断文献中，"controlled intervention" 和 "DAG" 的使用不等同于声称 full causal identification——DAG 常被用作 design rationale 来阐释哪些路径被 blocked 和哪些假设被 relied upon（参见 Pearl 2009 的 interventionist interpretation）。"Controlled" 在标题中指 controlled experimental manipulation（NLI-gated content control），这是准确的描述，不是因果 overclaim。

我的判断：术语使用基本一致，§3.5 的 hedge 恰到好处。唯一值得改进的是在 §3.5 开头明确一句 "We adopt an interventionist, not structural-causal, interpretation throughout"，但这是 minor polish 而非 inconsistency。

**[AGREE] R1-W2: BT 模型 IIA 假设未讨论**

同意。Appendix H 报告 formality 存在显著方向异质性（原文方向 68.9% vs 52.6%, Fisher p=0.015），BT 模型的 IIA 假设（一次比较的结果不受其他替代品影响）在此受到挑战。单参数 BT 可能掩盖效应的方向依赖性结构。

R1 提出的 stratified BT（Q4）是合理的补充分析方向。至少应在主文或附录中讨论 IIA violation 的影响，并报告 direction-stratified BT estimates。

**[AGREE] R1-W3: NLI gate FNR 样本量过小**

同意。12 个 rejected pairs 的 FNR 估计 CI 极宽（Wilson 95% CI ≈ [2%, 28%]），论文自己也承认 "FNR may be optimistic"（§5.1）。这不是一个 fatal flaw（GPT-4o cross-validation 提供了 model-independent check），但 FNR 的不确定性应在主文中被量化（报告 CI），而非仅在 Appendix 中定性提及。

**[AGREE] R1-W4: Verbosity direction-aware gating 可能引入 selection bias**

同意这是一个合理的 concern。Appendix F 报告 direction-aware gate 额外放入 21 pairs（从 65 增至 86, +32%），这些 pairs 的特征可能与 bidirectional-pass pairs 不同（例如它们可能是 verbosity change 更 aggressive 的 pairs）。如果 direction-aware 放入的 pairs 系统性地有更大的 style effect，这会 inflate verbosity 的 BT estimate。

建议作者报告：(1) bidirectional-pass only subset 的 BT estimate，(2) direction-aware only 新增 pairs 的 BT estimate，看两组是否一致。如果一致，selection bias concern 可以被缓解。

**[AGREE] R1-W5: "Blindspot" 术语的 loaded nature**

强烈同意——这与我自己的 N1（novelty 定位）高度相关。"Blindspot" 一词暗示 Likert 有缺陷、遗漏了重要信息。但如果 construct divergence 解释成立（Likert 测量 absolute quality，pairwise 测量 relative preference），那么 Likert 并非 "盲"，而是在看不同的东西。

论文在 §6 和 Limitations 中公平讨论了两种解释，但标题和 Abstract 的 framing 偏向 measurement attenuation 解释（即 Likert 遗漏了真实偏差）。这种 framing bias 应当被 acknowledge。如果不改标题，至少应在 Abstract 结尾加一句 caveat："whether this reflects measurement attenuation or construct divergence remains an open question."

**[AGREE] R1-W6: 生态效度讨论不足**

同意。论文的 style manipulation 是 controlled（由 LLM rewriter 执行），这与 naturalistic text 中 style 和 content 自然共变的情况有本质区别。在真实评估场景中，style 差异通常伴随 content quality 差异，CSD 的 NLI gate 在那种场景下无法直接应用。

论文 Limitations 中提到了 NLI gate 的局限（"cannot block quality-style perception shifts"），但未明确讨论 controlled → naturalistic 的 generalization gap。这应该作为一个独立的 limitation point。

---

## Questions

**[AGREE] R1-Q1: Primary family 包含哪三个 judges？**
同 N1。必须明确回答。

**[AGREE] R1-Q2: Cross-rewriter test 仅覆盖 Qwen3-32B 是否资源约束？**
合理的问题。如果是资源约束导致只测了一个 judge，应明确说明。如果有方法论理由（如 Qwen3-32B 作为 primary rewriter 和 judge 的 overlap 最需要排除），也应说明。

**[AGREE] R1-Q3: Claude TOST 在 n=87 下能 reject 的最小 Δ？**
同 N3。这个数字直接决定 negative control 结论的 informativeness。作者应报告 minimum detectable Δ at 80% power。

**[AGREE] R1-Q4: 是否考虑过 stratified BT？**
同 W2。Direction-stratified BT 是一个有价值的补充分析，尤其在 Appendix H 已发现方向异质性的情况下。即使作为 Appendix 中的 exploratory analysis，也能大大增强结果的 interpretability。

**[REBUT] R1-Q5: Likert vs pairwise 比较是否方法论不公平？**

R1 提出一个合理但可以反驳的 concern：Likert 和 pairwise 的统计效率不同，直接在同一样本量下比较可能对 Likert 不公平。

然而，论文已通过两个途径部分回应了这个问题：

1. **Appendix K (Formal Power Analysis) & Figure 4**: 明确展示了在不同效应量下 Likert 和 pairwise 各自需要的样本量。对于 verbosity（效应量最大），Likert 需要 n ≈ 1,206-18,157 pairs 才能在 p < 0.001 下达到 80% power（Table 11），而当前 n=100 远远不够。论文并不否认 Likert 在足够大样本下可能检测到偏差——它的 claim 是 "at practical sample sizes, Likert systematically underestimates"。

2. **Appendix M (100-point Continuous Likert)**: 更关键的是，即使给 Likert 最有利的条件（100-point scale, eliminating granularity constraint），tie rate 仍高达 51-64%，p 值仍不显著。这表明问题不仅仅是统计效率——Likert 模式下 judges 根本不在 style-transformed pairs 上产生 score variance，这是 paradigmatic limitation 而非 power limitation。

因此，虽然 Q5 提出了方法论公平性的合理 concern，论文的 power analysis + 100-point Likert 双重证据已较充分地表明问题超越了简单的样本量差异。建议在 §5.2 中更明确地回应这一点。

---

## 总结

在 R1 的 14 个具体 issues 中，我 **AGREE 12 条，REBUT 2 条**：

| Issue | 判断 | 核心理由 |
|-------|------|----------|
| N1 (primary family) | AGREE | Post-hoc selection 嫌疑，必须透明化 |
| N2 (cross-rewriter) | AGREE | 覆盖面不足，但严重性应 contextualize |
| N3 (TOST Δ) | AGREE | 与我的 W3 一致，功效不足 |
| W1 (causal terminology) | **REBUT** | §3.5 的 hedge 恰当，"controlled" 不等于 "causal" |
| W2 (BT IIA) | AGREE | 方向异质性需要讨论 |
| W3 (FNR sample) | AGREE | CI 过宽，应量化报告 |
| W4 (direction-aware bias) | AGREE | 需要 subset 对比验证 |
| W5 (Blindspot 术语) | AGREE | 与我的 N1 (novelty) 呼应 |
| W6 (生态效度) | AGREE | 缺少 controlled→naturalistic gap 讨论 |
| Q1 | AGREE | 同 N1 |
| Q2 | AGREE | 需要说明理由 |
| Q3 | AGREE | 需要报告 minimum detectable Δ |
| Q4 | AGREE | Stratified BT 有分析价值 |
| Q5 | **REBUT** | Power analysis + 100-point Likert 双重证据已回应 |

**与我自己审稿意见的对齐情况**：R1 的 N3 与我的 W3 完全一致；R1 的 W5 与我的 N1（novelty positioning）高度相关；R1 的 W6 补充了我未充分展开的生态效度问题。R1 独特贡献的 N1（primary family selection）和 W2（BT IIA）是我审稿中遗漏的重要技术问题——尤其 N1，我认为应提升为影响接收决定的 critical issue。

**综合两位 reviewer 意见后，我维持 Overall 3.5 (Borderline Conference) 的判断。** 核心结论：论文实验设计优秀但存在多个透明度和方法论问题（primary family selection、TOST power、BT IIA），加上概念 novelty 定位和 human validation 的缺失，使其处于 Conference 和 Findings 的边界。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 710 · 2026-05-22T03:38:17.935587+00:00_

R2 交叉回应已收到（12 AGREE / 2 REBUT）。等待 R1 对 R2 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 70

## Round 70

2 recorded events


### User

_source line 711 · 2026-05-22T03:38:20.589521+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 全部 14 条意见的逐条交叉回应，AGREE 12 条，REBUT 2 条（W1 因果术语、Q5 方法论公平性）。已提交至 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 712 · 2026-05-22T03:38:34.871497+00:00_

R2 交叉回应已收到（AGREE 12/14，REBUT 2/14）。等待 R1 对 R2 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 71

## Round 71

12 recorded events


### User

_source line 713 · 2026-05-22T03:39:22.386447+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R2-N1: Novelty 定位不够诚实**

同意方向，但认为 R2 略有过度。论文 Section 2 ("Measurement Sensitivity in NLG Evaluation") 已明确引用 Thurstone (1927)、Stevens (1946)、Hoening and Heisey (2001)，承认 forced-choice > rating 是已知原理。但 R2 的核心批评成立：论文标题 "The Likert Blindspot" 和 Abstract 整体叙事确实给出"全新发现"的印象，而非"已知心理测量原理在 LLM judge 领域的首次系统实证"。

不过需要补充一个 nuance：LLM judges 并非人类 rater——它们的内部评分机制不同。LLM judges 表现出与人类相同的 psychometric 脆弱性这一事实本身不是 trivial 的。并且论文的贡献不仅是"验证已知原理"，还包括：(1) per-axis 量化（severity spectrum from complete attenuation to >60% signal loss）, (2) GEE conditional decomposition 揭示的 confound structure（Table 3），(3) 100-point continuous scale 排除 granularity（Appendix M）。这些是超越 Thurstone (1927) 的新 empirical insight。

R2 建议的 reframing（"providing the first controlled, per-axis quantification of this psychometric phenomenon in LLM judges"）是精准的，我支持这一修改方向。

**[AGREE] R2-N2: Detection vs. Amplification 缺 human validation**

同意这是一个 genuine gap。论文的六个 controls 排除了 specific artifacts：
- NLI gate → 内容变化
- Position balancing → 顺序效应
- Consistency filter → 随机噪声
- Cross-rewriter (Appendix D) → rewriter-specific artifacts
- Negative control (Appendix G) → false positives
- Same-style double-rewrite (Appendix O) → polishing artifact

但没有一个 control 能回答：pairwise 检测到的偏好是否对应人类也能感知到的 bias？论文 Section 5.6 和 Conclusion 正确地将此定义为开放问题（"whether this reflects measurement attenuation or construct divergence"），但这个歧义是论文结论的根基性不确定性。

不过，我认为 R2 要求"至少 50 pairs 的 human evaluation"作为 Must-Fix 可能过高。原因：(1) 论文的核心贡献是 methodology + empirical demonstration，不是 resolve the interpretive question；(2) 50 pairs 的人类评估如果质量不高（inter-annotator agreement 低），反而可能引入更多噪声。建议将此 **降级为 Strong Should-Fix**：论文应在 Limitations 中明确承认缺少 human baseline 是主要局限，并 acknowledge 当前无法区分 detection vs. amplification。如果作者能在 rebuttal 中提供哪怕 30 pairs 的 pilot human evaluation 数据，将显著增强说服力。

---

### Should-Fix

**[AGREE] R2-W1: 3 个风格轴限制 "framework" 泛化声明**

同意。Section 2 contribution 列表中 "A black-box controlled framework for per-axis style bias detection" 的 "framework" 措辞暗示了广泛适用性，但仅 3 个轴的实证覆盖有限。特别是 register 仅为 exploratory（Section 5.5），实质上只有 2 个轴有 confirmatory evidence。

但 CSD 的方法论设计确实是 axis-agnostic 的（给定任何可改写的风格轴，pipeline 均可运行），3 个轴作为初始 demonstration 不算不合理。建议作者在 contribution 中将 "framework" 修改为 "methodology"（降低泛化预期），并在 Limitations 中明确讨论未覆盖的重要轴（如 tone/politeness, complexity, specificity）。

**[AGREE] R2-W2: Table 1 信息密度过高**

同意。5 judges × 3 benchmarks × 3 axes × 2 metrics + significance markers + footnotes 在一张表中确实 overloaded。读者需要花大量时间才能提取核心 pattern（即"BT significant where Likert non-significant"）。

建议：(1) 将 Table 1 拆分为两个子表（main benchmark LLMBar + scaled replications），或 (2) 增加一个 summary visualization（如 Figure 3 的 BT probability 图已部分承担了这个角色，但缺少 Likert 对比）。

**[AGREE] R2-W3: Claude Sonnet 4 统计功效不足**

强烈同意。这与我的 N3 完全一致。n = 87、Δ = 15pp 的 TOST 无法有效区分"无 bias"和"中等 bias"。论文确认的最小 bias 为 +13pp（GPT-4o formality, Table 1: BT 60.7%），而 Δ = 15pp 几乎涵盖这一范围。

补充一个 R2 未提及的细节：Appendix G 明确承认"Δ = 10pp is underpowered at n = 87"，这意味着作者知道功效不足但选择了更宽的 Δ 来让结果 "work"。这不是统计上的 best practice。

**[PARTIALLY AGREE] R2-W4: Rewriting artifact 的 style-specific polishing interaction 未讨论**

部分同意。R2 的关切有道理：same-style double-rewrite（Appendix O, Table 15）控制了 style-neutral polishing（LLM 改写普遍提升质量），但未控制 style-specific polishing（LLM 改写到不同风格时质量提升是否不同，如改写为 formal 可能比改写为 casual 产生更高质量的输出）。

但需要指出：论文的实验设计中，main comparison 的 BT estimate 对 polishing artifact 是 robust 的——因为两个方向的改写（formal→casual 和 casual→formal）在 balanced design 中 polishing 效果应相互抵消。Appendix H 的 stratified analysis 部分地检验了这一点：verbosity 无方向异质性（Fisher's p = 0.43），但 formality 有（68.9% vs. 52.6%, Fisher's p = 0.015）。这个 formality 方向异质性可能部分来自 style-specific polishing interaction，而不仅是 R1 和论文归因的 originality confound。

建议：在 Limitations 或 Appendix O 中明确讨论 style-specific polishing interaction 的可能性，并承认 formality 方向异质性可能混合了 originality confound 和 style-specific polishing 两种机制。

**[AGREE] R2-W5: Introduction motivating example 需 acknowledge formality-quality nuance**

同意。Introduction 第一段的 "average height" 例子暗示 formality bias 是完全不合理的（"Same judge, same text, opposite conclusions"）。但论文自己的 GEE 结果（Table 3）显示 formality 存在 significant Originality effect——即 formality 与 original content quality 存在 conditional relationship。这意味着 judge 偏好 formal 文本可能部分反映了合理的质量判断（formal writing 确实在某些场景下更精确、更结构化），而非纯粹的"bias"。

Introduction 应 acknowledge 这一 nuance：not all formality preference is irrational bias, and the paper's own GEE decomposition quantifies the rational vs. irrational components.

---

### Questions

**[AGREE] R2-Q1**: R2 写的"NLI threshold 0.98"应为论文实际使用的 0.90（Section 3.2）。这是 R2 的笔误。但底层问题有效：论文主文确实没有对 0.90 的选择给出充分 inline justification，需要读者翻到 Appendix E (Table 8) 的 11-threshold sweep 才能理解。建议在 Section 3.2 增加一句简要 justification（如"chosen as the plateau onset in a sweep across 11 thresholds, Appendix E"）。

**[AGREE] R2-Q2**: 100-point continuous Likert（Appendix M）仅测试 Qwen3-32B，generalizability 未验证。这与我在 Round 1 中对 appendix 分析覆盖面的关切一致。至少再测试一个 judge（如 GPT-4o）会显著增强此控制实验的说服力。

**[AGREE] R2-Q3**: GEE interaction direction — Appendix C 明确报告"no significant interactions in any of the nine judge×axis cells (all p > 0.13, range 0.14–0.96)"，但确实没有报告 interaction 的 point estimates 和 direction。对于 formality 这个已知有 conditional confounding 的轴，报告 interaction term 的 coefficients（即使不显著）会有信息价值。

**[AGREE] R2-Q4**: LLMBar 100 pairs 的 selection criteria — Section 3.4 引用 Zeng et al. (2024) 并描述为"n = 100 instruction-response pairs spanning diverse task types, designed to test LLM judges' ability to distinguish response quality with human-verified quality labels"。但没有说明是从 LLMBar 全集中 sample 还是用了完整 benchmark。如果是 subsample，selection criteria 很重要；如果是完整 benchmark，应明确声明。

**[AGREE] R2-Q5**: 后续区分 attenuation vs. divergence — 这是一个好的 forward-looking question。如果作者能在 response 中概述计划（如 human evaluation protocol、更大样本量的 Likert 实验、或 within-subject design 同时收集两种 measurement），会增强论文的 contribution positioning。

---

### Missing References

**[PARTIALLY AGREE]** R2 建议的三篇参考文献方向合理：
1. **Girrbach et al. "Likert or Not"**: 如果确实研究 LLM 在 Likert scale 上的评分行为，与本文直接相关，应引用。
2. **PRePair (Jeong et al., 2025)**: 论文已在 Section 2 引用了 Jeong et al. (2025) 关于 Comparative Trap，但 PRePair 的 pairwise + pointwise 整合方法如果不同于 Jeong et al. (2025)，值得补充。
3. **Kambhatla et al.**: calibration/scoring bias 相关，合理补充。

需要确认这些文献是否真实存在且已发表/预印——reviewer 建议的 missing references 有时也需要 verify。

---

### Detailed Comments

**[AGREE]** Abstract "near-perfect correlation": 论文引用 "70–92% of observed preferences originate from surface-level style cues"。70% 不是 "near-perfect"（通常暗示 >95%）。应修改为 "strong correlation" 或 "high correlation"。

**[REBUT]** "black-box controlled framework" overclaim: R2 怀疑 NLI gate 需要 model probabilities，暗示 CSD 不是 black-box。但这是对论文的误读——"black-box"指的是 **judge** 是 black-box（CSD 不需要访问 judge 的内部状态），而非整个 pipeline。NLI gate 使用的是独立的 DeBERTa 模型（Section 3.2），不涉及 judge 的 probabilities。论文明确说"requires no access to judge internals and applies post-hoc to any black-box judge"（Section 1）。这一表述准确。

**[AGREE]** §2 遗漏 acquiescence bias 和 central tendency bias: 这是 Likert scale 的经典心理测量问题，与论文讨论的 Likert limitations 直接相关。一句话的 mention 即可（不需要大篇幅讨论）。

**[AGREE]** §4.1 Primary family 选择标准: 与我的 N1 一致，需要明确哪三个 judges 在 primary family 中及排除理由。

**[AGREE]** §5.5 Register 叙述压缩: Register 结果确实过于压缩，但在 8 页限制下可以理解。如果空间允许，增加 1-2 句关于 register 的 judge-dependent pattern 会有帮助。

---

### 综合评估

R2 的审稿整体质量高，大部分关切有据。最有力的两个点是 **N1（novelty 定位）** 和 **N2（detection vs. amplification）**——前者是 framing 问题（可修复），后者是 fundamental limitation（难以在本文完全解决但可通过 Limitations 重写和 pilot human data 部分 mitigate）。

R2 的 Should-Fix 中 **W3（TOST 功效）** 与我的 N3 完全吻合，**W4（style-specific polishing）** 和 **W5（formality-quality nuance）** 是我 Round 1 未充分覆盖的有价值补充。

我与 R2 的主要分歧在于：
1. **N2 的严重程度**：R2 列为 Must-Fix 要求 human evaluation，我认为应降为 Strong Should-Fix——论文可以通过更诚实的 Limitations 讨论部分 mitigate，完整的 human evaluation 更适合作为 follow-up work。
2. **"black-box" 表述**：R2 认为 overclaim，我认为论文对"black-box"的使用是准确的（指 judge 而非 pipeline）。

**维持我的 Overall Assessment: 3.5 (Borderline Conference)**，与 R2 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 714 · 2026-05-22T03:39:50.308814+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-22T03:39:50.363346+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T03:24:34.035595+00:00\", \"completed_at\": \"2026-05-22T03:27:41.003915+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-4\", \"message\": \"连续 2 页纯文本（Related Work → Method → Experiments 4.1），无 figure/table/equation 穿插。虽然方法描述段落传统上以文字为主，但审稿人快速翻阅时这两页视觉单调，建议考虑：(a) 将 Figure 2（causal DAG，当前在 p5）前移至 Method §3.5 Design Rationale 首次引用处（p4），或 (b) 在 Method 段加入一个 key equation block 打破纯文本节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1（主结果表）信息密度极高：5 judges × 3 benchmarks × 3 axes × 4 指标列，单元格数量 ~180。审稿人首次扫读时可能感到 overwhelming。表内 p-value 字号偏小但仍可读。建议在 caption 中增加一句 reading guide（如\\\"rows grouped by benchmark; bold = p < 0.05\\\"）帮助快速定位\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2（causal DAG）尺寸偏小（约占左栏 1/4 高度），作为方法理论基础的核心图示，可适当放大以增强视觉权重\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3（BT win probabilities dot plot）使用 filled/open diamond 区分显著性，清晰有效；颜色区分度良好\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4（detection probability curves）多条曲线使用不同 line style + marker，灰度打印时仍可区分——好的实践\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 脚注使用编号标注说明（1. Blindspot; 2. Scaled replication），自包含性好\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-12\", \"message\": \"附录连续 4 页共 12 张表格（Tables 4–15），密度极高。每张表格单独看格式规范（booktabs 风格、无竖线），但整体形成\\\"表格墙\\\"。建议对关键 ablation 结果（如 Table 14 NLI Gate Ablation）考虑用 bar chart 可视化以增加附录视觉多样性\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"所有表格均使用 booktabs 风格（toprule/midrule/bottomrule），无竖线，格式统一规范\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"最优结果加粗标注，方向性指示清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Section \\\"6 Conclusion\\\" 标题后有充足正文内容（约 15 行），无孤悬问题\"}, {\"severity\": \"info\", \"dimension\": \"pages 13-15\", \
…[truncated 147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 54
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-22T03:39:50.498837+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-22T03:39:50.566597+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 67
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-22T03:40:18.895268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "offset": "1075",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "offset": "1075",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-22T03:40:18.946162+00:00_

1075	  # ============================================================
1076	  # Round 7 new issues
1077	  # ============================================================
1078	
1079	  - id: "R7-W2"
1080	    summary: "Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 含 register (8 tests) vs Table 1 标 register 为 exploratory (†_e)"
1081	    category: method
1082	    severity: critical
1083	    status: in_progress
1084	    first_raised_round: 7
1085	    last_seen_round: 7
1086	    resolution: null
1087	    resolution_round: null
1088	    mentions:
1089	      - round: 7
1090	        reviewers: [1, 2]
1091	        note: "R7-R1 (W2) 列为 Must-Fix。R7-R2 交叉 [AGREE]：明确矛盾，直接影响 Holm-Bonferroni 校正的 adjusted p-values。需统一为 6-test 或 8-test family。"
1092	    action_items:
1093	      - round: 7
1094	        action: "统一 Section 4.1 primary family 定义与 Table 1 标注——建议将 register 移出 primary family（改为 6-test），或保留 8-test 但修正 Table 1 exploratory 标记"
1095	        assigned_to: paper_agent
1096	        status: in_progress
1097	
1098	  - id: "R7-W4"
1099	    summary: "NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型（与 rewriter 相同），存在循环性"
1100	    category: method
1101	    severity: warning
1102	    status: in_progress
1103	    first_raised_round: 7
1104	    last_seen_round: 7
1105	    resolution: null
1106	    resolution_round: null
1107	    mentions:
1108	      - round: 7
1109	        reviewers: [1, 2]
1110	        note: "R7-R1 (W4) 提出。R7-R2 交叉部分同意：GPT-4o cross-validation 存在但仅报告 precision 而非 FNR。建议提升 GPT-4o 验证为主要数据。"
1111	    action_items:
1112	      - round: 7
1113	        action: "报告 GPT-4o validation 对应的 FNR（而非仅 precision），或在正文标注 8.4% FNR 来自 rewriter 同模型"
1114	        assigned_to: paper_agent
1115	        status: in_progress
1116	
1117	  - id: "R7-W5"
1118	    summary: "Verbosity direction-aware NLI gate GPT-4o validation 显示 17.4% FPR，正文未报告"
1119	    category: method
1120	    severity: warning
1121	    status: in_progress
1122	    first_raised_round: 7
1123	    last_seen_round: 7
1124	    resolution: null
11
…[truncated 1260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-22T03:45:05.460989+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"因果语言降级问题在 Round 3 以新形式复发，见 R3-N1\"\n      - round: 4\n        reviewers: [1]\n        note: \"R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2\"\n      - round: 8\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4-SF8: Honest novelty positioning applied.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。\"\n      - round: 7\n        reviewers: [2]\n        note: \"R2 再次指出核心发现可从 Thurstone (1927) 理论直接预测。R1 反驳称 severity spectrum 和 per-axis interaction 是全新经验发现。分歧未完全解决。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix，R8-R1 交叉 AGREE（但补充 LLM 非人类 rater，表现相同脆弱性非 trivial；per-axis quantification + GEE decomposition + 100-point scale 超越 Thurstone）。共识：novelty 定位需从'discovering the Blindspot'调整为'first controlled per-axis quantification in LLM judges'。\"\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 7\n    resolution: \"Round 7 两位 Reviewer 均确认主正文 8 页合规。§5.5 Register 压缩 + §6 Conclusion 精简。\"\n    resolution_round: 7\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Round 2 发现并修复。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Round 6 再次发现：Section 6 (Conclusion) 约 5-6 行溢出到 page 9。两位 Reviewer 共识 Must-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Round 7 两位 Reviewer 均确认主正文 8 页合规。页数问题已修复。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 两位 Reviewer 均确认正文 ≤8 页合规。\"\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Independence test 仅覆盖 verbosity，formality 缺 test。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Formality rewriter independence 已补。Register 仍缺。Style OR 下降 22% 非可忽略。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R5 两位 Reviewer 均再次指出。R1 定为 critical（self-preference bias 无法排除），R2 认为 should-fix（GPT-4o 不受影响）。交叉后共识：should-fix。主文 Section 5 缺 caveat。见 R5-SF2。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix：22% OR 下降处理不充分 + register 轴完全缺失 cross-rewriter test。R6-R2 同意 22% non-trivial 但注意 Blindspot pattern 在 GPT-4o rewriter 下完全保持。共识：Must-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 独立标注为核心问题（R1-W1, R2-W5），交叉后双方 [AGREE]。cross-rewriter validation 仅覆盖 Qwen3-32B judge，GPT-4o/Llama-70B judge 未验证。22% Style OR 下降确认 inflation 存在。共识 Must-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 列为 Must-Fix (N2)：仅 1/4 judges 有 cross-rewriter 验证。R8-R2 交叉 AGREE 但补充核心 claim 不依赖 rewriter-independence（Blindspot 在 4 judges 上用同一 rewriter 一致确认）。共识：Must-Fix，但 claim scope 应 downgrade。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"Register independence test — acknowledged as limitation\"\n        assigned_to: paper_agent\n        status: wont_fix\n      - round: 6\n        action: \"§5.4 加 cross-ref sentence：22% OR 下降 + NLI pass rate argument + register caveat in Limitations\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 8\n        action: \"将 Appendix D 结论从 'Blindspot persists with independent rewriter' 改为 'persists for at least one judge configuration; broader validation remains for future work'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 'approximates the do-operator' 残留。见 R5-MF2。\"\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'. n=355 d->0 evidence.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"attenuation framing 已改善，但 'construct difference' 替代解释在主文中仍不足。见 R5-SF6。\"\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Cross-rewriter consistency + 200-pair GPT-4o validation provide partial proxy. Acknowledged in Limitations.\"\n      - round: 5\n        reviewers: []\n        note: \"Round 5 未被任何 Reviewer 显式提及，但仍 inherently open（无人工评估数据）。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix。R6-R2 同意但建议降级为 strong Should-Fix。交叉后共识：Must-Fix，50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 列为 Should-Fix (W6)，R7-R2 完全同意。两位 Reviewer 共识：全文零人工验证，涉及测量工具敏感度的论文却用同类工具验证，存在认识论循环。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix（需至少 50 pairs human evaluation 区分 detection vs amplification）。R8-R1 交叉 AGREE 方向但建议降级为 Strong Should-Fix（论文可通过 Limitations 讨论部分 mitigate，完整 human eval 更适合 follow-up）。Director 判定 Strong Should-Fix。\"\n    action_items:\n      - round: 6\n        action: \"准备 50 对 NLI pass/fail 样本 + 标注模板，用户标注后报告 agreement + Cohen's κ\"\n        assigned_to: user\n        status: pending\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"术语已改善，但 verbosity 'confound-free' 措辞仍过强。见 R5-SF4。\"\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"引用量已改善，但遗漏了 Jeong et al. (2025) Comparative Trap 等关键文献。见 R5-MF1。\"\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"TOST at Delta=10pp underpowered (n=87). 措辞仍需更审慎。见 R5-M3。\"\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"仍指出 Abstract 信息密度过高。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均再次指出 Abstract 过密。Minor issue。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 列为 Should-Fix；R6-R1 建议降级 Minor。交叉后分歧。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 再次一致指出（R1-Detailed, R2-W4）：7 句含 4 组括号统计数据，首次阅读认知负担过重。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 指出 Abstract 首句 'near-perfect correlation' 过于绝对（76-92% ≠ near-perfect）。R8-R1 交叉 AGREE。\"\n    action_items:\n      - round: 7\n        action: \"将具体统计数字移至 Introduction，Abstract 聚焦定性结论和核心 message\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues (all resolved)\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再次提出 IIA 未检验，R2 技术性反驳。交叉后共识：降级 minor。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"交叉后共识：Minor。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 列为 Should-Fix (W2)：Appendix H formality 方向异质性 (68.9% vs 52.6%, Fisher p=0.015) 挑战 IIA。R8-R2 交叉 AGREE，建议报告 direction-stratified BT。\"\n    action_items:\n      - round: 8\n        action: \"在主文或附录中承认 IIA 假设，报告 direction-stratified BT estimates\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)——pairwise amplification vs detection sensitivity 张力未讨论\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 首先识别，R1 交叉完全同意。Jeong et al. (2025) 证明 pairwise 放大 style bias，与 Section 6 'adopt pairwise' 建议矛盾。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"论文已在 §2 和 §5.2 加入 Jeong et al. 讨论。但 §6 Conclusion 'should adopt' 仍过强。共识 Should-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 确认论文已在 Section 5.2 加入 6 项 amplification controls 回应 Comparative Trap。R7-R2 补充要求引用 Tripathi et al. (2025) 作为额外 amplification evidence。已从 critical 降级为 Should-Fix。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及此 issue。论文 §5.2 已含 6 项 amplification controls 和 Jeong et al. 讨论。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap\"\n        assigned_to: paper_agent\n        status: done\n      - round: 6\n        action: \"在 §6 Conclusion 加入 pairwise amplification caveat\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强——selection/conditioning ≠ intervention\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§3.2 原文 'approximates the do-operator' 过强。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§3.2 已改为 'filtering-based confounder control'，但 Intro/Abstract 仍用 'interventional framework'。共识 Should-Fix。\"\n      - round: 7\n        reviewers: [1]\n        note: \"R7-R1 (S1) 正面评价 §3.5 的因果语言校准。原始 'do-operator' 语言已修复。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 列为 Should-Fix (W1)：全文因果术语不一致。R8-R2 REBUT：§3.5 hedge 恰当，'controlled' 指实验操控而非因果推断，'interventionist' 在因果推断文献中有明确含义。Director 判定：R2 REBUT 成立，但建议在 §3.5 开头加一句统一声明。\"\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"'first' 需限定到 CSD 具体方法组合的 novelty。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 Must-Fix vs R6-R1 Should-Fix。Director 判定 Should-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W1) 列为 Must-Fix：'the first framework combining...' 通过组合限定词构造唯一性。R7-R1 交叉 [AGREE]，建议改为 'a unified framework'。共识 Must-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (N1) 再次要求 novelty reframing。R8-R1 AGREE 但指出论文确有超越 Thurstone 的 empirical contributions (per-axis quantification, GEE decomposition, 100-point scale)。共识：将 'the first' 改为 'a unified framework'。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework' 或 'a framework that integrates'\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 定 critical，R2 should-fix。交叉后共识：should-fix。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RD2-SF1 涵盖此项。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1 讨论。仍为 in_progress。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R8 两位 Reviewer 均再次确认。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Llama-70B 加入后现有 3 target judges 全部展示 Blindspot (6/6 cells + register 7/9)。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"论文已使用 'style-dominated' 而非 'confound-free'。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示——缺 verbosity 验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现严重不平衡\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"需在 §5.2 给两种解释同等篇幅。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§5.2 末尾已加入讨论段落。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W2) 列为 Must-Fix。R7-R1 [REBUT]。Director 判定 Should-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (W5) 再次指出 'Blindspot' 术语偏向 attenuation 解释。R8-R2 交叉 AGREE（与自己 N1 novelty 呼应）。建议至少在 Abstract 结尾加 caveat。R8-R1 确认论文 §5.2/§6/Limitations 已有 balanced discussion，但标题和 Abstract framing 偏颇。\"\n\n  - id: \"R5-SF7\"\n    summary: \"Formality confound 在 Abstract/Conclusion 中未与 verbosity 区分\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Abstract 和 Conclusion 中已有 per-axis differentiation。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点（0.50-0.98）。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Register 是最弱轴，恰是 rewriter identity 最可能影响结论的轴。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Acknowledged as limitation 但未补实验。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 在 evaluator-producer 讨论中再次确认 register 缺失。已在 Limitations 标注。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1 cross-rewriter 讨论。Register 仍为最高风险轴。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Equivalence bound Delta=15pp 缺外部 justification。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 Should-Fix，R6-R2 同意。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W3) 再次标注 TOST Δ=15pp 过宽。R7-R2 交叉 [AGREE] 但补充论文核心论证不依赖 TOST。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 升级为 Must-Fix (N3)：Δ=15pp 几乎涵盖最小 confirmed bias (+13pp GPT-4o formality)。R8-R2 交叉完全 AGREE，补充 Appendix G 承认 Δ=10pp underpowered 但选择了更宽 Δ 让结果 'work'。共识 Must-Fix：需 reframe Claude 为 'insufficient evidence' 或报告 minimum detectable Δ at 80% power。\"\n    action_items:\n      - round: 7\n        action: \"将 Claude 相关语言从 'equivalence confirmed' / 'no bias' 改为 'failed to detect bias at Δ=15pp precision'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 8\n        action: \"三选一：(a) 增加 Claude n 使 Δ=10pp 有功效；(b) reframe 为 'insufficient evidence for bias'；(c) 报告 n=87 下能 reject 的最小 Δ\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"每个缺失 cell 应在 footnote 或 Appendix 说明原因。\"\n      - round: 6\n        reviewers: [2]\n        note: \"Table 1 第 6 列无 header。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 格式检查确认第 6 列仍无列标题。R7-R1 交叉 [AGREE]。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (W2) 再次指出 Table 1 信息密度过高、可读性差。R8-R1 交叉 AGREE，建议拆分或增加 reading guide。\"\n    action_items:\n      - round: 7\n        action: \"Table 1 第 6 列添加列标题（如 'Status' 或 'Finding'）\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"建议颜色 + 线型双重编码。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Figure 2/3 灰度区分问题再次提及。\"\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 (M2) 再次指出 Figure 2 颜色编码在 150 DPI 下辨认困难。\"\n    action_items:\n      - round: 6\n        action: \"Figure 2/3 增加颜色+线型双重编码\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025), Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound (Delta=15pp) 缺乏独立外部 justification\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"需引用外部基准设定 equivalence bound。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3 讨论。TOST Δ=15pp 与 GPT-4o formality +13pp 仅差 2pp。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3/R8 Must-Fix 讨论。\"\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 讨论不充分\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1]\n        note: \"same-style control 只检测 rewriting artifact 但无法检测 axis-specific confounds。\"\n      - round: 7\n        reviewers: []\n        note: \"Round 7 未被显式提及。\"\n      - round: 8\n        reviewers: [1]\n        note: \"R8-R1 在 Detailed Comments §3.5 中再次指出假设(iii)最难验证，same-style DR 只检验 within-style artifact 不检验 cross-style confound。R8-R2 (W4) 补充 style-specific polishing interaction 问题。\"\n    action_items:\n      - round: 6\n        action: \"在 Limitations 补充讨论 axis-specific confounds\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄——n=355 仅限 Qwen3-32B formality\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"LLMBar n=100 为主数据源，MT-Bench n=30。n=355 仅覆盖一个 judge×axis。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W3) 列为 Must-Fix。R7-R1 交叉 [AGREE] 但指出 8/11 bias-positive cells 展示 Blindspot 已属较高覆盖度。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 (W1) 指出仅 3 轴难以支撑 framework 级别泛化。R8-R1 交叉 AGREE 但指出 CSD 方法论 axis-agnostic，3 轴作为初始 demonstration 合理。共识 Should-Fix。\"\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"GPT-4o formality/verbosity/register 和 Qwen3 formality Orig OR 只有点估计无 CI。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (Q1) 和 R7-R2 交叉回应均确认 7 个 CI 缺失。必须补全。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。Appendix Table 5 现已有完整 CI（Table tab:gee_ci 12 行均含 CI）。可能已修复，待确认。\"\n    action_items:\n      - round: 7\n        action: \"补全 Appendix Table 5 所有 GEE CI\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"论文 Related Work §2 已引用 Shi et al. (2024) 和 Bavaresco et al. (2025)。\"\n    resolution_round: 8\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"非必须但高度相关。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 确认 §2 已含两篇引用。\"\n\n  # ============================================================\n  # Round 7 issues\n  # ============================================================\n\n  - id: \"R7-W2\"\n    summary: \"Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 含 register (8 tests) vs Table 1 标 register 为 exploratory (†_e)\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W2) 列为 Must-Fix。R7-R2 交叉 [AGREE]：明确矛盾，直接影响 Holm-Bonferroni 校正的 adjusted p-values。需统一为 6-test 或 8-test family。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (N1) 列为 Must-Fix：§4.1 声明 'six tests (three judges × two axes)' 但未指明哪三个 judges。R8-R2 交叉 AGREE：如果被排除的是 Gemini（行为模式不同），存在 post-hoc cherry-picking 嫌疑。共识 Must-Fix。\"\n    action_items:\n      - round: 7\n        action: \"统一 Section 4.1 primary family 定义与 Table 1 标注\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 8\n        action: \"在 §4.1 明确列出三个 primary judges 名称及排除理由；报告 8-test family 下 adjusted p-values 作为 sensitivity analysis\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R7-W4\"\n    summary: \"NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型（与 rewriter 相同），存在循环性\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W4) 提出。R7-R2 交叉部分同意。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (W3) 独立指出 FNR 基于仅 12 个 rejected pairs（Wilson 95% CI ≈ [2%, 28%]），样本量过小。R8-R2 交叉 AGREE。应报告 CI 而非仅点估计。\"\n\n  - id: \"R7-W5\"\n    summary: \"Verbosity direction-aware NLI gate GPT-4o validation 显示 17.4% FPR，正文未报告\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W5) 提出。R7-R2 交叉 [AGREE]。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (W4) 指出 direction-aware gating 额外放入 21 pairs (+32%)，可能引入 selection bias。R8-R2 交叉 AGREE，建议报告 bidirectional-pass only subset BT vs direction-aware only 新增 pairs BT 对比。\"\n\n  - id: \"R7-REF1\"\n    summary: \"遗漏引用：Tripathi et al. (2025) 'Pairwise or Pointwise?'\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W6) 提出。R7-R1 交叉同意。\"\n      - round: 8\n        reviewers: [1]\n        note: \"R8-R1 确认论文 §5.2 已引用 Tripathi et al. (2025)。此 issue 可能已修复。\"\n\n  # ============================================================\n  # Round 8 new issues\n  # ============================================================\n\n  - id: \"R8-W1\"\n    summary: \"3 个风格轴限制 'framework' 级别的泛化声明——需从 'framework' 降为 'methodology'\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (W1) 提出：仅 formality/verbosity/register 3 轴，register 还只是 exploratory。R8-R1 交叉 AGREE 但指出 CSD 方法论 axis-agnostic。共识 Should-Fix：将 'framework' 改为 'methodology'，在 Limitations 中列出未覆盖轴。\"\n    action_items:\n      - round: 8\n        action: \"在 Contribution 中将 'framework' 改为 'methodology'；Limitations 中列出未覆盖轴（tone, complexity, hedging 等）\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R8-W2\"\n    summary: \"生态效度（ecological validity）讨论不足——controlled manipulation 到 naturalistic evaluation 的 generalizability gap\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (W6) 提出。R8-R2 交叉 AGREE。在自然文本中 style 和 content 共变，NLI gate 无法直接应用。Limitations 中应增加独立 point。\"\n    action_items:\n      - round: 8\n        action: \"在 Limitations 中新增生态效度讨论段落\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R8-W3\"\n    summary: \"Rewriting artifact 的 style-specific polishing interaction 未讨论——formal rewriting polishing 可能不同于 casual rewriting polishing\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (W4) 提出。R8-R1 PARTIALLY AGREE：balanced design 应使 polishing 抵消，但 Appendix H formality 方向异质性 (68.9% vs 52.6%) 可能混合 originality confound 和 style-specific polishing。\"\n    action_items:\n      - round: 8\n        action: \"在 Limitations 或 Appendix O 中讨论 style-specific polishing interaction 可能性\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R8-W4\"\n    summary: \"Introduction motivating example ('average height') 未 acknowledge formality-quality nuance\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (W5) 提出。R8-R1 交叉 AGREE：论文自己的 GEE 结果 (Table 3) 显示 formality 存在 significant Originality effect，judge 偏好 formal 文本可能部分反映合理质量判断。Introduction 应 acknowledge 此 nuance。\"\n    action_items:\n      - round: 8\n        action: \"在 motivating example 旁简短 acknowledge formality 与 perceived quality 的合理关联\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R8-REF1\"\n    summary: \"建议补充引用：Girrbach et al. (2025/2026) 'Likert or Not'\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 建议。R8-R1 PARTIALLY AGREE，需验证文献真实性。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"因果语言降级问题在 Round 3 以新形式复发，见 R3-N1\"\n      - round: 4\n        reviewers: [1]\n        note: \"R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2\"\n      - round: 8\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4-SF8: Honest novelty positioning applied.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。\"\n      - round: 7\n        reviewers: [2]\n        note: \"R2 再次指出核心发现可从 Thurstone (1927) 理论直接预测。R1 反驳称 severity spectrum 和 per-axis interaction 是全新经验发现。分歧未完全解决。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix，R8-R1 交叉 AGREE（但补充 LLM 非人类 rater，表现相同脆弱性非 trivial；per-axis quantification + GEE decomposition + 100-point scale 超越 Thurstone）。共识：novelty 定位需从'discovering the Blindspot'调整为'first controlled per-axis quantification in LLM judges'。\"\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 7\n    resolution: \"Round 7 两位 Reviewer 均确认主正文 8 页合规。§5.5 Register 压缩 + §6 Conclusion 精简。\"\n    resolution_round: 7\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Round 2 发现并修复。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Round 6 再次发现：Section 6 (Conclusion) 约 5-6 行溢出到 page 9。两位 Reviewer 共识 Must-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Round 7 两位 Reviewer 均确认主正文 8 页合规。页数问题已修复。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 两位 Reviewer 均确认正文 ≤8 页合规。\"\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Independence test 仅覆盖 verbosity，formality 缺 test。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Formality rewriter independence 已补。Register 仍缺。Style OR 下降 22% 非可忽略。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R5 两位 Reviewer 均再次指出。R1 定为 critical（self-preference bias 无法排除），R2 认为 should-fix（GPT-4o 不受影响）。交叉后共识：should-fix。主文 Section 5 缺 caveat。见 R5-SF2。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix：22% OR 下降处理不充分 + register 轴完全缺失 cross-rewriter test。R6-R2 同意 22% non-trivial 但注意 Blindspot pattern 在 GPT-4o rewriter 下完全保持。共识：Must-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 独立标注为核心问题（R1-W1, R2-W5），交叉后双方 [AGREE]。cross-rewriter validation 仅覆盖 Qwen3-32B judge，GPT-4o/Llama-70B judge 未验证。22% Style OR 下降确认 inflation 存在。共识 Must-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 列为 Must-Fix (N2)：仅 1/4 judges 有 cross-rewriter 验证。R8-R2 交叉 AGREE 但补充核心 claim 不依赖 rewriter-independence（Blindspot 在 4 judges 上用同一 rewriter 一致确认）。共识：Must-Fix，但 claim scope 应 downgrade。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"Register independence test — acknowledged as limitation\"\n        assigned_to: paper_agent\n        status: wont_fix\n      - round: 6\n        action: \"§5.4 加 cross-ref sentence：22% OR 下降 + NLI pass rate argument + register caveat in Limitations\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 8\n        action: \"将 Appendix D 结论从 'Blindspot persists with independent rewriter' 改为 'persists for at least one judge configuration; broader validation remains for future work'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 'approximates the do-operator' 残留。见 R5-MF2。\"\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'. n=355 d->0 evidence.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"attenuation framing 已改善，但 'construct difference' 替代解释在主文中仍不足。见 R5-SF6。\"\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Cross-rewriter consistency + 200-pair GPT-4o validation provide partial proxy. Acknowledged in Limitations.\"\n      - round: 5\n        reviewers: []\n        note: \"Round 5 未被任何 Reviewer 显式提及，但仍 inherently open（无人工评估数据）。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix。R6-R2 同意但建议降级为 strong Should-Fix。交叉后共识：Must-Fix，50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 列为 Should-Fix (W6)，R7-R2 完全同意。两位 Reviewer 共识：全文零人工验证，涉及测量工具敏感度的论文却用同类工具验证，存在认识论循环。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix（需至少 50 pairs human evaluation 区分 detection vs amplification）。R8-R1 交叉 AGREE 方向但建议降级为 Strong Should-Fix（论文可通过 Limitations 讨论部分 mitigate，完整 human eval 更适合 follow-up）。Director 判定 Strong Should-Fix。\"\n    action_items:\n      - round: 6\n        action: \"准备 50 对 NLI pass/fail 样本 + 标注模板，用户标注后报告 agreement + Cohen's κ\"\n        assigned_to: user\n        status: pending\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"术语已改善，但 verbosity 'confound-free' 措辞仍过强。见 R5-SF4。\"\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"引用量已改善，但遗漏了 Jeong et al. (2025) Comparative Trap 等关键文献。见 R5-MF1。\"\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"TOST at Delta=10pp underpowered (n=87). 措辞仍需更审慎。见 R5-M3。\"\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"仍指出 Abstract 信息密度过高。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均再次指出 Abstract 过密。Minor issue。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 列为 Should-Fix；R6-R1 建议降级 Minor。交叉后分歧。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 再次一致指出（R1-Detailed, R2-W4）：7 句含 4 组括号统计数据，首次阅读认知负担过重。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 指出 Abstract 首句 'near-perfect correlation' 过于绝对（76-92% ≠ near-perfect）。R8-R1 交叉 AGREE。\"\n    action_items:\n      - round: 7\n        action: \"将具体统计数字移至 Introduction，Abstract 聚焦定性结论和核心 message\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues (all resolved)\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再次提出 IIA 未检验，R2 技术性反驳。交叉后共识：降级 minor。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"交叉后共识：Minor。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 列为 Should-Fix (W2)：Appendix H formality 方向异质性 (68.9% vs 52.6%, Fisher p=0.015) 挑战 IIA。R8-R2 交叉 AGREE，建议报告 direction-stratified BT。\"\n    action_items:\n      - round: 8\n        action: \"在主文或附录中承认 IIA 假设，报告 direction-stratified BT estimates\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)——pairwise amplification vs detection sensitivity 张力未讨论\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 首先识别，R1 交叉完全同意。Jeong et al. (2025) 证明 pairwise 放大 style bias，与 Section 6 'adopt pairwise' 建议矛盾。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"论文已在 §2 和 §5.2 加入 Jeong et al. 讨论。但 §6 Conclusion 'should adopt' 仍过强。共识 Should-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 确认论文已在 Section 5.2 加入 6 项 amplification controls 回应 Comparative Trap。R7-R2 补充要求引用 Tripathi et al. (2025) 作为额外 amplification evidence。已从 critical 降级为 Should-Fix。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及此 issue。论文 §5.2 已含 6 项 amplification controls 和 Jeong et al. 讨论。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap\"\n        assigned_to: paper_agent\n        status: done\n      - round: 6\n        action: \"在 §6 Conclusion 加入 pairwise amplification caveat\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强——selection/conditioning ≠ intervention\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§3.2 原文 'approximates the do-operator' 过强。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§3.2 已改为 'filtering-based confounder control'，但 Intro/Abstract 仍用 'interventional framework'。共识 Should-Fix。\"\n      - round: 7\n        reviewers: [1]\n        note: \"R7-R1 (S1) 正面评价 §3.5 的因果语言校准。原始 'do-operator' 语言已修复。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 列为 Should-Fix (W1)：全文因果术语不一致。R8-R2 REBUT：§3.5 hedge 恰当，'controlled' 指实验操控而非因果推断，'interventionist' 在因果推断文献中有明确含义。Director 判定：R2 REBUT 成立，但建议在 §3.5 开头加一句统一声明。\"\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"'first' 需限定到 CSD 具体方法组合的 novelty。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 Must-Fix vs R6-R1 Should-Fix。Director 判定 Should-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W1) 列为 Must-Fix：'the first framework combining...' 通过组合限定词构造唯一性。R7-R1 交叉 [AGREE]，建议改为 'a unified framework'。共识 Must-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (N1) 再次要求 novelty reframing。R8-R1 AGREE 但指出论文确有超越 Thurstone 的 empirical contributions (per-axis quantification, GEE decomposition, 100-point scale)。共识：将 'the first' 改为 'a unified framework'。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework' 或 'a framework that integrates'\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 定 critical，R2 should-fix。交叉后共识：should-fix。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RD2-SF1 涵盖此项。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1 讨论。仍为 in_progress。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R8 两位 Reviewer 均再次确认。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Llama-70B 加入后现有 3 target judges 全部展示 Blindspot (6/6 cells + register 7/9)。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"论文已使用 'style-dominated' 而非 'confound-free'。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示——缺 verbosity 验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现严重不平衡\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"需在 §5.2 给两种解释同等篇幅。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§5.2 末尾已加入讨论段落。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W2) 列为 Must-Fix。R7-R1 [REBUT]。Director 判定 Should-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (W5) 再次指出 'Blindspot' 术语偏向 attenuation 解释。R8-R2 交叉 AGREE（与自己 N1 novelty 呼应）。建议至少在 Abstract 结尾加 caveat。R8-R1 确认论文 §5.2/§6/Limitations 已有 balanced discussion，但标题和 Abstract framing 偏颇。\"\n\n  - id: \"R5-SF7\"\n    summary: \"Formality confound 在 Abstract/Conclusion 中未与 verbosity 区分\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Abstract 和 Conclusion 中已有 per-axis differentiation。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点（0.50-0.98）。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Register 是最弱轴，恰是 rewriter identity 最可能影响结论的轴。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Acknowledged as limitation 但未补实验。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 在 evaluator-producer 讨论中再次确认 register 缺失。已在 Limitations 标注。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1 cross-rewriter 讨论。Register 仍为最高风险轴。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Equivalence bound Delta=15pp 缺外部 justification。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 Should-Fix，R6-R2 同意。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W3) 再次标注 TOST Δ=15pp 过宽。R7-R2 交叉 [AGREE] 但补充论文核心论证不依赖 TOST。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 升级为 Must-Fix (N3)：Δ=15pp 几乎涵盖最小 confirmed bias (+13pp GPT-4o formality)。R8-R2 交叉完全 AGREE，补充 Appendix G 承认 Δ=10pp underpowered 但选择了更宽 Δ 让结果 'work'。共识 Must-Fix：需 reframe Claude 为 'insufficient evidence' 或报告 minimum detectable Δ at 80% power。\"\n    action_items:\n      - round: 7\n        action: \"将 Claude 相关语言从 'equivalence confirmed' / 'no bias' 改为 'failed to detect bias at Δ=15pp precision'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 8\n        action: \"三选一：(a) 增加 Claude n 使 Δ=10pp 有功效；(b) reframe 为 'insufficient evidence for bias'；(c) 报告 n=87 下能 reject 的最小 Δ\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"每个缺失 cell 应在 footnote 或 Appendix 说明原因。\"\n      - round: 6\n        reviewers: [2]\n        note: \"Table 1 第 6 列无 header。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 格式检查确认第 6 列仍无列标题。R7-R1 交叉 [AGREE]。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (W2) 再次指出 Table 1 信息密度过高、可读性差。R8-R1 交叉 AGREE，建议拆分或增加 reading guide。\"\n    action_items:\n      - round: 7\n        action: \"Table 1 第 6 列添加列标题（如 'Status' 或 'Finding'）\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"建议颜色 + 线型双重编码。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Figure 2/3 灰度区分问题再次提及。\"\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 (M2) 再次指出 Figure 2 颜色编码在 150 DPI 下辨认困难。\"\n    action_items:\n      - round: 6\n        action: \"Figure 2/3 增加颜色+线型双重编码\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025), Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound (Delta=15pp) 缺乏独立外部 justification\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"需引用外部基准设定 equivalence bound。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3 讨论。TOST Δ=15pp 与 GPT-4o formality +13pp 仅差 2pp。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3/R8 Must-Fix 讨论。\"\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 讨论不充分\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1]\n        note: \"same-style control 只检测 rewriting artifact 但无法检测 axis-specific confounds。\"\n      - round: 7\n        reviewers: []\n        note: \"Round 7 未被显式提及。\"\n      - round: 8\n        reviewers: [1]\n        note: \"R8-R1 在 Detailed Comments §3.5 中再次指出假设(iii)最难验证，same-style DR 只检验 within-style artifact 不检验 cross-style confound。R8-R2 (W4) 补充 style-specific polishing interaction 问题。\"\n    action_items:\n      - round: 6\n        action: \"在 Limitations 补充讨论 axis-specific confounds\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄——n=355 仅限 Qwen3-32B formality\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"LLMBar n=100 为主数据源，MT-Bench n=30。n=355 仅覆盖一个 judge×axis。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W3) 列为 Must-Fix。R7-R1 交叉 [AGREE] 但指出 8/11 bias-positive cells 展示 Blindspot 已属较高覆盖度。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 (W1) 指出仅 3 轴难以支撑 framework 级别泛化。R8-R1 交叉 AGREE 但指出 CSD 方法论 axis-agnostic，3 轴作为初始 demonstration 合理。共识 Should-Fix。\"\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"GPT-4o formality/verbosity/register 和 Qwen3 formality Orig OR 只有点估计无 CI。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (Q1) 和 R7-R2 交叉回应均确认 7 个 CI 缺失。必须补全。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。Appendix Table 5 现已有完整 CI（Table tab:gee_ci 12 行均含 CI）。可能已修复，待确认。\"\n    action_items:\n      - round: 7\n        action: \"补全 Appendix Table 5 所有 GEE CI\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"论文 Related Work §2 已引用 Shi et al. (2024) 和 Bavaresco et al. (2025)。\"\n    resolution_round: 8\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"非必须但高度相关。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 确认 §2 已含两篇引用。\"\n\n  # ============================================================\n  # Round 7 issues\n  # ============================================================\n\n  - id: \"R7-W2\"\n    summary: \"Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 含 register (8 tests) vs Table 1 标 register 为 exploratory (†_e)\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W2) 列为 Must-Fix。R7-R2 交叉 [AGREE]：明确矛盾，直接影响 Holm-Bonferroni 校正的 adjusted p-values。需统一为 6-test 或 8-test family。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (N1) 列为 Must-Fix：§4.1 声明 'six tests (three judges × two axes)' 但未指明哪三个 judges。R8-R2 交叉 AGREE：如果被排除的是 Gemini（行为模式不同），存在 post-hoc cherry-picking 嫌疑。共识 Must-Fix。\"\n    action_items:\n      - round: 7\n        action: \"统一 Section 4.1 primary family 定义与 Table 1 标注\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 8\n        action: \"在 §4.1 明确列出三个 primary judges 名称及排除理由；报告 8-test family 下 adjusted p-values 作为 sensitivity analysis\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R7-W4\"\n    summary: \"NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型（与 rewriter 相同），存在循环性\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W4) 提出。R7-R2 交叉部分同意。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (W3) 独立指出 FNR 基于仅 12 个 rejected pairs（Wilson 95% CI ≈ [2%, 28%]），样本量过小。R8-R2 交叉 AGREE。应报告 CI 而非仅点估计。\"\n\n  - id: \"R7-W5\"\n    summary: \"Verbosity direction-aware NLI gate GPT-4o validation 显示 17.4% FPR，正文未报告\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W5) 提出。R7-R2 交叉 [AGREE]。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (W4) 指出 direction-aware gating 额外放入 21 pairs (+32%)，可能引入 selection bias。R8-R2 交叉 AGREE，建议报告 bidirectional-pass only subset BT vs direction-aware only 新增 pairs BT 对比。\"\n\n  - id: \"R7-REF1\"\n    summary: \"遗漏引用：Tripathi et al. (2025) 'Pairwise or Pointwise?'\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W6) 提出。R7-R1 交叉同意。\"\n      - round: 8\n        reviewers: [1]\n        note: \"R8-R1 确认论文 §5.2 已引用 Tripathi et al. (2025)。此 issue 可能已修复。\"\n\n  # ============================================================\n  # Round 8 new issues\n  # ============================================================\n\n  - id: \"R8-W1\"\n    summary: \"3 个风格轴限制 'framework' 级别的泛化声明——需从 'framework' 降为 'methodology'\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (W1) 提出：仅 formality/verbosity/register 3 轴，register 还只是 exploratory。R8-R1 交叉 AGREE 但指出 CSD 方法论 axis-agnostic。共识 Should-Fix：将 'framework' 改为 'methodology'，在 Limitations 中列出未覆盖轴。\"\n    action_items:\n      - round: 8\n        action: \"在 Contribution 中将 'framework' 改为 'methodology'；Limitations 中列出未覆盖轴（tone, complexity, hedging 等）\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R8-W2\"\n    summary: \"生态效度（ecological validity）讨论不足——controlled manipulation 到 naturalistic evaluation 的 generalizability gap\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (W6) 提出。R8-R2 交叉 AGREE。在自然文本中 style 和 content 共变，NLI gate 无法直接应用。Limitations 中应增加独立 point。\"\n    action_items:\n      - round: 8\n        action: \"在 Limitations 中新增生态效度讨论段落\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R8-W3\"\n    summary: \"Rewriting artifact 的 style-specific polishing interaction 未讨论——formal rewriting polishing 可能不同于 casual rewriting polishing\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (W4) 提出。R8-R1 PARTIALLY AGREE：balanced design 应使 polishing 抵消，但 Appendix H formality 方向异质性 (68.9% vs 52.6%) 可能混合 originality confound 和 style-specific polishing。\"\n    action_items:\n      - round: 8\n        action: \"在 Limitations 或 Appendix O 中讨论 style-specific polishing interaction 可能性\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R8-W4\"\n    summary: \"Introduction motivating example ('average height') 未 acknowledge formality-quality nuance\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (W5) 提出。R8-R1 交叉 AGREE：论文自己的 GEE 结果 (Table 3) 显示 formality 存在 significant Originality effect，judge 偏好 formal 文本可能部分反映合理质量判断。Introduction 应 acknowledge 此 nuance。\"\n    action_items:\n      - round: 8\n        action: \"在 motivating example 旁简短 acknowledge formality 与 perceived quality 的合理关联\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R8-REF1\"\n    summary: \"建议补充引用：Girrbach et al. (2025/2026) 'Likert or Not'\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 建议。R8-R1 PARTIALLY AGREE，需验证文献真实性。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-22T03:45:05.562826+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 41578}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-22T03:47:42.954455+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 8 (Fresh Review)\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\"\n**Venue**: EMNLP 2026 Main Conference (Long Paper via ARR)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh（独立初审）\n**Reviewer 编排**: 2 人（R1 方法严谨性/实验设计，R2 新颖性/完整性/写作质量）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated 内容控制、per-axis 风格分解和位置控制的 pairwise comparison，系统量化 LLM judge 的风格偏差。核心发现 \"Likert Blindspot\" 表明 Likert 评分在中等效应量下系统性遗漏 pairwise comparison 能检测到的风格偏差（信号损失 >60%），在四个 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、一个 negative control（Claude Sonnet 4）、三个 benchmark（LLMBar, AlpacaEval, MT-Bench）和三个风格轴（formality, verbosity, register）上得到验证。GEE conditional decomposition 揭示 per-axis confound structure：verbosity 为 style-dominated（OR 8–13），formality 受 content quality 调节，register 为 judge-dependent。\n\n---\n\n## Strengths\n\n**S1. 多层验证的实验管线（两位 Reviewer 一致认可）。** NLI gate (DeBERTa-v3-large, τ=0.90) → consistency filter → position-balanced pairwise → BT + GEE 的管线设计体现了出色的方法论思维。11 个 NLI 阈值扫描（Appendix E）、same-style double-rewrite control（Appendix O）、100-point continuous Likert（Appendix M）和 formal power analysis（Appendix K）构成严密的验证层次。\n\n**S2. 七种统计方法的 sensitivity hierarchy。** Table 2 清晰展示：所有 Likert-based 方法（ATE, binarized, ordinal regression, GEE, Wilcoxon）均未达显著性，而 pairwise 方法（BT, sign test）达到。这是对 Likert Blindspot 的 compelling evidence，且 Appendix P 的 verbosity 复制进一步加强。\n\n**S3. GEE conditional decomposition 是 genuinely novel 的分析贡献。** Table 3 揭示跨 judge 一致的 per-axis confound structure——verbosity style-dominated、formality conditional、register judge-dependent——超越了 \"judges have style bias\" 的简单叙事。Appendix C 的 correlation structure robustness 和 interaction test 验证了 GEE specification。\n\n**S4. 100-point continuous Likert 是关键控制实验。** Appendix M 证明 Blindspot 不是 scale granularity 问题（101 值下 tie rate 仍 51–64%），而是 absolute vs. relative evaluation paradigm 差异。\n\n**S5. 负面控制的 discriminative validity。** Claude Sonnet 4 在两个主要轴上未检测到显著偏差，支持框架不对所有 judges 产生 false positive。\n\n**S6. 对 RATE 的比较公平且建设性。** 论文将两者定位为互补框架（§5.2），而非简单否定。\n\n**S7. 诚实的局限性讨论。** 公开讨论了 evaluator-producer bias、measurement attenuation vs. construct divergence 歧义、样本量约束。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1 [critical, 共识] Primary family 构成缺乏透明度。**\nSection 4.1 声明 \"a primary family of six hypothesis tests (three judges × two axes)\" 并应用 Holm-Bonferroni 校正，但未指明哪三个 judges 被纳入 primary family。四个 target judges 中排除哪一个（很可能是 Gemini，其 formality GEE 行为与其他三个不同）未说明。如果纳入 Gemini（8 tests），校正更保守，部分结果可能失去 adjusted significance。Table 1 将 register 标为 exploratory (†_e) 而正文说 \"three judges × two axes\"（不含 register），这与 Round 7 发现的 register 分类矛盾一脉相承。需在 §4.1 明确列出三个 primary judges 名称及排除理由，并报告 8-test family 下 adjusted p-values 作为 sensitivity analysis。\n— R1 提出，R2 AGREE\n\n**MF2 [critical, 共识] Cross-rewriter independence 验证覆盖面不足。**\nAppendix D 仅测试了一个 judge（Qwen3-32B）配合替代 rewriter（GPT-4o），四个 target judges 中另外三个无 cross-rewriter 验证。GPT-4o as judge 使用 Qwen3-32B 作 rewriter，可能检测到 Qwen3-32B 特有改写痕迹；Llama-70B 和 Gemini 完全无验证。R2 补充：核心 claim 不依赖 rewriter-independence（Blindspot 在全部四个 judges 上用同一 rewriter 一致确认），cross-rewriter 是 supplementary robustness，但 claim scope 应相应 downgrade。\n— R1 提出，R2 AGREE（含 contextualization）\n\n**MF3 [critical, 共识] 负面控制 TOST Δ=15pp 过宽，n=87 功效不足。**\n论文最小 confirmed bias 为 +13pp（GPT-4o formality, BT 63.0%），而 TOST Δ=±15pp 几乎涵盖此范围——Claude 可能有高达 ~14pp bias 而 TOST 仍宣告等价。Appendix G 自承 Δ=10pp underpowered。建议三选一：(a) 增加 Claude 样本量使 Δ=10pp 有功效；(b) 将 Claude 重新定位为 \"insufficient evidence for bias\" 而非 \"negative control\"；(c) 报告 n=87 下能 reject 的最小 Δ。\n— R1 提出 (N3)，R2 完全 AGREE (= R2-W3)\n\n**MF4 [critical→should-fix, 分歧后降级] Novelty 定位需更诚实。**\nLikert Blindspot 的概念基础（forced-choice > rating scales）在心理测量学中已有近百年历史（Thurstone 1927, Bradley & Terry 1952）。论文整体叙事——标题、Abstract、Introduction——给人 \"全新发现\" 印象，而非 \"已知原理在 LLM judge 领域的首次系统性实证\"。R1 补充 nuance：LLM 非人类 rater，表现相同心理测量脆弱性非 trivial；per-axis quantification + GEE decomposition + 100-point scale 超越 Thurstone。共识：将 novelty 从 \"discovering the Blindspot\" 调整为 \"providing the first controlled, per-axis quantification of this psychometric phenomenon in LLM judges\"；将 \"the first framework\" 改为 \"a unified framework\"。\n— R2 提出 (N1)，R1 AGREE（含 nuance）。Director 判定 Must-Fix（framing 层面可修复）\n\n### Strong Should-Fix（不一票否决但显著影响评分）\n\n**SF1 [warning, 分歧] 缺少 human validation，detection vs. amplification 未充分解决。**\n论文六个 controls 排除了 specific artifacts，但无法在根本上区分 \"pairwise 检测了真实偏差\" 和 \"pairwise 放大了微弱偏好\"（Comparative Trap, Jeong et al. 2025）。唯一能解决此问题的是 human evaluation（至少一小组 pairs 的 Likert + pairwise 人类评估）。R2 列为 Must-Fix，R1 同意方向但建议降为 Strong Should-Fix（论文核心贡献是 methodology + empirical demonstration，非 resolve interpretive question）。Director 判定 Strong Should-Fix：Limitations 中应明确承认此为主要开放问题。\n— R2 提出 (N2)，R1 AGREE 方向但降级\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [warning, 共识] BT 模型 IIA 假设未讨论。**\nAppendix H 发现 formality 存在显著方向异质性（68.9% vs. 52.6%, Fisher p=0.015），BT 单参数公式可能遗漏效应异质性。需承认 IIA 假设并报告 direction-stratified BT。\n— R1 提出 (W2)，R2 AGREE\n\n**W2 [warning, 共识] NLI gate FNR 估计样本量过小。**\nFNR 基于仅 12 个 rejected pairs（Wilson 95% CI ≈ [2%, 28%]），CI 极宽。GPT-4o cross-validation 报告了 precision 但未报告 FNR CI。需量化报告。\n— R1 提出 (W3)，R2 AGREE\n\n**W3 [warning, 共识] Verbosity direction-aware gating 可能引入 selection bias。**\nDirection-aware gate 额外放入 21 pairs (+32%)，但这些 pairs 与 bidirectional-pass pairs 的特征可能不同。需报告两组分别的 BT estimates 作对比。\n— R1 提出 (W4)，R2 AGREE\n\n**W4 [warning, 共识] 3 个风格轴限制 \"framework\" 泛化声明。**\nRegister 仅 exploratory，实质只有 2 轴有 confirmatory evidence。CSD 方法论 axis-agnostic，但 \"framework\" 措辞暗示更广适用性。建议改为 \"methodology\"，Limitations 中列出未覆盖轴。\n— R2 提出 (W1)，R1 AGREE\n\n**W5 [warning, 共识] Measurement attenuation vs. construct divergence 歧义影响核心叙事。**\n\"Blindspot\" 术语偏向 attenuation 解释。如果 construct divergence 成立，Likert 并非 \"盲\"，而是测量不同构念。论文 §5.2/§6/Limitations 已有 balanced discussion，但标题和 Abstract framing 偏颇。至少在 Abstract 结尾加 caveat。\n— R1 提出 (W5)，R2 AGREE\n\n**W6 [warning, 共识] 生态效度讨论不足。**\nControlled manipulation → naturalistic evaluation 的 generalizability gap 未讨论。自然文本中 style 和 content 共变，NLI gate 无法直接应用。\n— R1 提出 (W6)，R2 AGREE\n\n**W7 [warning, 部分共识] Rewriting artifact 的 style-specific polishing interaction 未讨论。**\nSame-style double-rewrite 控制 style-neutral polishing，但 formal rewriting 的 polishing 可能不同于 casual rewriting。Formality 方向异质性可能混合 originality confound 和 style-specific polishing。\n— R2 提出 (W4)，R1 PARTIALLY AGREE\n\n**W8 [warning, 共识] Introduction motivating example 需 acknowledge formality-quality nuance。**\n\"Average height\" 例子暗示 formality bias 完全不合理，但论文自己的 GEE 结果显示 formality 存在 significant Originality effect——偏好 formal 文本可能部分反映合理质量判断。\n— R2 提出 (W5)，R1 AGREE\n\n### Minor\n\n- **M1**: Abstract 首句 \"near-perfect correlation\" 过于绝对（76–92% ≠ near-perfect）。改为 \"strong correlation\"。（R2 提出，R1 AGREE）\n- **M2**: Figure 2 (DAG) 尺寸偏小，颜色编码在低 DPI 下辨认困难。（Visual Check + R2）\n- **M3**: Pages 3–4 连续纯文本无 figure/table 穿插，视觉单调。建议将 Figure 2 前移。（Visual Check）\n- **M4**: Table 1 信息密度过高，建议增加 reading guide 或拆分。（R2 提出，R1 AGREE）\n- **M5**: §4.1 GEE exchangeable correlation 假设 justification 缺失。（R2-M3）\n- **M6**: Appendix 连续 4 页 12 张表格形成 \"表格墙\"。（Visual Check）\n- **M7**: NLI threshold 0.90 在主文缺 inline justification，需读者翻到 Appendix E。建议 §3.2 加一句简要说明。（R2-Q1，R1 AGREE）\n\n---\n\n## Reviewer Consensus\n\n| Issue | R1 | R2 | 共识 |\n|-------|----|----|------|\n| MF1: Primary family transparency | 提出 (N1) | AGREE | **Must-Fix** |\n| MF2: Cross-rewriter coverage | 提出 (N2) | AGREE (contextualize) | **Must-Fix** |\n| MF3: TOST Δ too wide | 提出 (N3) | AGREE (= W3) | **Must-Fix** |\n| MF4: Novelty positioning | AGREE (nuance) | 提出 (N1) | **Must-Fix** |\n| SF1: Human validation gap | AGREE (downgrade) | 提出 (N2) | **Strong Should-Fix** |\n| W1-W8: 8 Should-Fix issues | 见上 | 见上 | **Should-Fix** |\n| M1-M7: 7 Minor issues | 见上 | 见上 | **Minor** |\n\n---\n\n## Reviewer Divergence\n\n**分歧 1：因果框架表述一致性（R1-W1）**\nR1 认为全文因果术语不一致（\"Controlled Style Decomposition\" + DAG 暗示因果，§3.5 hedge 为 interventionist）。R2 REBUT：§3.5 的 caveat 恰当，\"controlled\" 指实验操控而非因果推断，DAG 常被用作 design rationale。**Director 判定：R2 REBUT 成立。** §3.5 的 hedge 措辞清晰，\"controlled\" 在实验设计语境下准确。仅建议在 §3.5 开头加一句统一声明。降为 Minor。\n\n**分歧 2：Likert vs. pairwise 比较的方法论公平性（R1-Q5）**\nR1 担忧不同统计效率的方法在同一样本量下比较对 Likert 不公平。R2 REBUT：Power analysis（Appendix K）+ 100-point continuous Likert（Appendix M）双重证据已表明问题超越简单样本量差异——Likert 模式下 judges 根本不产生 score variance，是 paradigmatic limitation 而非 power limitation。**Director 判定：R2 REBUT 成立。** 但建议在 §5.2 更明确回应此公平性 concern。\n\n---\n\n## Questions（需要作者澄清）\n\n1. Primary family 包含哪三个 judges？排除第四个的理由？是否有 pre-registration？\n2. Cross-rewriter independence test 仅覆盖 Qwen3-32B 是否资源约束？能否至少对 GPT-4o as judge 补一个小规模验证？\n3. Claude Sonnet 4 TOST 在 n=87 下能 reject 的最小 Δ 是多少？\n4. 是否考虑过 direction-stratified BT（按 original text direction 分层估计 win probability）？\n5. LLMBar 100 pairs 是从完整 benchmark 中 sample 还是用了全集？\n6. 100-point continuous Likert 仅用 Qwen3-32B，其他 judges 是否也显示相同 pattern？\n7. GEE formality interaction term 的 point estimates 和 direction？（即使不显著）\n\n---\n\n## Missing References\n\n1. **Girrbach et al. (2025/2026)** \"Likert or Not\" — LLM Likert 评分行为研究，与 Appendix M 直接相关（R2 建议，需验证真实性）\n2. **PRePair** (Jeong et al., 2025) — pairwise + pointwise 整合方法，可能是缓解 Blindspot 的替代方案（R2 建议）\n3. **Acquiescence bias / central tendency bias** — Likert scale 经典问题，§2 中一句话 mention 即可（R2 建议，R1 AGREE）\n\n---\n\n## External Review\n\n**外部审稿：未启用。** 本轮未配置 Stanford Agentic Reviewer。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (done, 耗时 ~3 min)\n\n| 严重度 | 数量 | 主要发现 |\n|--------|------|----------|\n| Critical | 0 | — |\n| Warning | 1 | Pages 3–4 连续纯文本无图表穿插，视觉单调。建议将 Figure 2 (DAG) 前移至 §3.5 首次引用处 |\n| Info | 10 | Table 1 信息密度高但可读；Figure 2 尺寸偏小；Figure 3/4 灰度区分良好；Appendix \"表格墙\"；booktabs 格式规范统一；参考文献无未解析引用 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | — | 4.0 | 4.0 |\n| Confidence | 4 | 4 | 4 |\n\n**支持 Conference (4.0) 的因素：**\n- 实验设计严谨度远超该领域平均水平（NLI gate + negative control + 7 种统计方法 + 100-point Likert + cross-benchmark + cross-rewriter + formal power analysis）\n- Likert Blindspot 的 empirical quantification 对 LLM evaluation 社区有直接实用价值\n- GEE per-axis confound decomposition 是 genuinely novel 的分析贡献\n- 五个 judges 跨三个 benchmark 的一致性令人信服\n- Appendix A–P 展示了出色的 rigor\n\n**拉向 Findings (3.0) 的因素：**\n- 核心概念（forced-choice > rating）在 psychometrics 中已有近百年历史；novelty 定位需更诚实\n- Primary family 构成透明度不足，影响 FWER 控制可信度\n- Cross-rewriter 验证仅覆盖 1/4 judges，限制 rewriter-independence claim\n- TOST negative control 功效不足（Δ=15pp 几乎涵盖最小 confirmed bias）\n- 缺少 human validation 区分 detection vs. amplification\n- 仅 3 个风格轴限制 framework 级别泛化\n\n**净判断：** 论文处于 Conference 和 Findings 边界。实验执行质量高，但多个方法论透明度问题（MF1 primary family、MF3 TOST）和 novelty 定位（MF4）需要在修改中解决。MF1/MF3 是纯写作/分析补充问题，可在一轮修改中完成。MF4（novelty reframing）需要调整叙事策略但不改变实验。SF1（human validation）是结构性限制，可通过 Limitations 重写部分 mitigate。如果 MF1–MF4 均得到充分回应，论文有潜力达到 4.0 (Conference)。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n信息密度高但可接受。\"near-perfect correlation\" 应改为 \"strong correlation\"（76–92% ≠ near-perfect）。GEE per-axis confound structure 的描述清晰且增量准确。建议移除部分括号内统计数字以降低认知负荷。\n\n### Section 1 (Introduction)\nOpening example 直观有效。但需 acknowledge formality-quality nuance：formality 改变可能合法影响 perceived quality（论文自己的 GEE 结果支持此点）。\"black-box controlled framework\" 表述准确（black-box 指 judge 而非 pipeline），但 \"framework\" 可改为 \"methodology\"。Contributions 列表清晰，item 1 的 \"the first\" 应改为 \"a unified\"。\n\n### Section 2 (Related Work)\n覆盖面广且组织良好。对 RATE 的对比公平。可补充 Likert scale 在社会科学中的经典问题（acquiescence bias, central tendency bias）一句话。\n\n### Section 3 (Method)\n§3.1 rewriting protocol 清晰。§3.2 NLI gate 设计精巧（bidirectional + direction-aware）。§3.3 measurement protocol 标准。§3.5 Design Rationale 的 DAG 和三个识别假设清晰，caveat 措辞恰当。假设 (iii)（style rewrite 不引入 target axis 之外的系统差异）最难验证，same-style DR 仅部分检验。\n\n### Section 4 (Experiments)\n§4.1 statistical framework 需明确 primary family 组成（MF1）。LLMBar n=100（NLI 后 n=88）是 moderate 样本；scaled replication n=355 仅覆盖一个 cell，对 generalizability 支持有限。\n\n### Section 5 (Analysis)\n§5.1 NLI gate validation thorough（FNR 8.4%, precision 98.9%, AC1=0.89），但 FNR 样本过小（n=12, CI 宽）。§5.2 核心发现清晰呈现；七方法 sensitivity hierarchy 有说服力。§5.3–5.4 cross-judge 和 cross-axis replication 增强结论稳健性。§5.5 register 过于压缩但在 8 页限制下可理解。§5.6 GEE decomposition 是论文第二主要贡献。\n\n### Section 6 (Conclusion)\n适当总结两个主要发现。\"whether measurement attenuation or construct divergence\" 的 open question 处理诚实。\n\n### Limitations\n覆盖了关键 weak points（evaluator-producer bias, methodology/scale, validation）。遗漏项：(1) 缺少 human validation 作为最主要的 open question；(2) 3 轴 coverage limitation；(3) 生态效度；(4) style-specific polishing interaction。\n\n### 格式合规\n- 正文 ≤8 页 ✓\n- Double-blind 匿名 ✓（\"Anonymous ACL submission\"，未发现自引泄漏）\n- ACL 双栏格式 ✓\n- Limitations 章节 ✓（3 段，覆盖适当，不过长）\n- ARR Checklist 不在 PDF 中 ✓\n- 参考文献格式一致 ✓",
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 8 (Fresh Review)\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\"\n**Venue**: EMNLP 2026 Main Conference (Long Paper via ARR)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh（独立初审）\n**Reviewer 编排**: 2 人（R1 方法严谨性/实验设计，R2 新颖性/完整性/写作质量）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated 内容控制、per-axis 风格分解和位置控制的 pairwise comparison，系统量化 LLM judge 的风格偏差。核心发现 \"Likert Blindspot\" 表明 Likert 评分在中等效应量下系统性遗漏 pairwise comparison 能检测到的风格偏差（信号损失 >60%），在四个 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、一个 negative control（Claude Sonnet 4）、三个 benchmark（LLMBar, AlpacaEval, MT-Bench）和三个风格轴（formality, verbosity, register）上得到验证。GEE conditional decomposition 揭示 per-axis confound structure：verbosity 为 style-dominated（OR 8–13），formality 受 content quality 调节，register 为 judge-dependent。\n\n---\n\n## Strengths\n\n**S1. 多层验证的实验管线（两位 Reviewer 一致认可）。** NLI gate (DeBERTa-v3-large, τ=0.90) → consistency filter → position-balanced pairwise → BT + GEE 的管线设计体现了出色的方法论思维。11 个 NLI 阈值扫描（Appendix E）、same-style double-rewrite control（Appendix O）、100-point continuous Likert（Appendix M）和 formal power analysis（Appendix K）构成严密的验证层次。\n\n**S2. 七种统计方法的 sensitivity hierarchy。** Table 2 清晰展示：所有 Likert-based 方法（ATE, binarized, ordinal regression, GEE, Wilcoxon）均未达显著性，而 pairwise 方法（BT, sign test）达到。这是对 Likert Blindspot 的 compelling evidence，且 Appendix P 的 verbosity 复制进一步加强。\n\n**S3. GEE conditional decomposition 是 genuinely novel 的分析贡献。** Table 3 揭示跨 judge 一致的 per-axis confound structure——verbosity style-dominated、formality conditional、register judge-dependent——超越了 \"judges have style bias\" 的简单叙事。Appendix C 的 correlation structure robustness 和 interaction test 验证了 GEE specification。\n\n**S4. 100-point continuous Likert 是关键控制实验。** Appendix M 证明 Blindspot 不是 scale granularity 问题（101 值下 tie rate 仍 51–64%），而是 absolute vs. relative evaluation paradigm 差异。\n\n**S5. 负面控制的 discriminative validity。** Claude Sonnet 4 在两个主要轴上未检测到显著偏差，支持框架不对所有 judges 产生 false positive。\n\n**S6. 对 RATE 的比较公平且建设性。** 论文将两者定位为互补框架（§5.2），而非简单否定。\n\n**S7. 诚实的局限性讨论。** 公开讨论了 evaluator-producer bias、measurement attenuation vs. construct divergence 歧义、样本量约束。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1 [critical, 共识] Primary family 构成缺乏透明度。**\nSection 4.1 声明 \"a primary family of six hypothesis tests (three judges × two axes)\" 并应用 Holm-Bonferroni 校正，但未指明哪三个 judges 被纳入 primary family。四个 target judges 中排除哪一个（很可能是 Gemini，其 formality GEE 行为与其他三个不同）未说明。如果纳入 Gemini（8 tests），校正更保守，部分结果可能失去 adjusted significance。Table 1 将 register 标为 exploratory (†_e) 而正文说 \"three judges × two axes\"（不含 register），这与 Round 7 发现的 register 分类矛盾一脉相承。需在 §4.1 明确列出三个 primary judges 名称及排除理由，并报告 8-test family 下 adjusted p-values 作为 sensitivity analysis。\n— R1 提出，R2 AGREE\n\n**MF2 [critical, 共识] Cross-rewriter independence 验证覆盖面不足。**\nAppendix D 仅测试了一个 judge（Qwen3-32B）配合替代 rewriter（GPT-4o），四个 target judges 中另外三个无 cross-rewriter 验证。GPT-4o as judge 使用 Qwen3-32B 作 rewriter，可能检测到 Qwen3-32B 特有改写痕迹；Llama-70B 和 Gemini 完全无验证。R2 补充：核心 claim 不依赖 rewriter-independence（Blindspot 在全部四个 judges 上用同一 rewriter 一致确认），cross-rewriter 是 supplementary robustness，但 claim scope 应相应 downgrade。\n— R1 提出，R2 AGREE（含 contextualization）\n\n**MF3 [critical, 共识] 负面控制 TOST Δ=15pp 过宽，n=87 功效不足。**\n论文最小 confirmed bias 为 +13pp（GPT-4o formality, BT 63.0%），而 TOST Δ=±15pp 几乎涵盖此范围——Claude 可能有高达 ~14pp bias 而 TOST 仍宣告等价。Appendix G 自承 Δ=10pp underpowered。建议三选一：(a) 增加 Claude 样本量使 Δ=10pp 有功效；(b) 将 Claude 重新定位为 \"insufficient evidence for bias\" 而非 \"negative control\"；(c) 报告 n=87 下能 reject 的最小 Δ。\n— R1 提出 (N3)，R2 完全 AGREE (= R2-W3)\n\n**MF4 [critical→should-fix, 分歧后降级] Novelty 定位需更诚实。**\nLikert Blindspot 的概念基础（forced-choice > rating scales）在心理测量学中已有近百年历史（Thurstone 1927, Bradley & Terry 1952）。论文整体叙事——标题、Abstract、Introduction——给人 \"全新发现\" 印象，而非 \"已知原理在 LLM judge 领域的首次系统性实证\"。R1 补充 nuance：LLM 非人类 rater，表现相同心理测量脆弱性非 trivial；per-axis quantification + GEE decomposition + 100-point scale 超越 Thurstone。共识：将 novelty 从 \"discovering the Blindspot\" 调整为 \"providing the first controlled, per-axis quantification of this psychometric phenomenon in LLM judges\"；将 \"the first framework\" 改为 \"a unified framework\"。\n— R2 提出 (N1)，R1 AGREE（含 nuance）。Director 判定 Must-Fix（framing 层面可修复）\n\n### Strong Should-Fix（不一票否决但显著影响评分）\n\n**SF1 [warning, 分歧] 缺少 human validation，detection vs. amplification 未充分解决。**\n论文六个 controls 排除了 specific artifacts，但无法在根本上区分 \"pairwise 检测了真实偏差\" 和 \"pairwise 放大了微弱偏好\"（Comparative Trap, Jeong et al. 2025）。唯一能解决此问题的是 human evaluation（至少一小组 pairs 的 Likert + pairwise 人类评估）。R2 列为 Must-Fix，R1 同意方向但建议降为 Strong Should-Fix（论文核心贡献是 methodology + empirical demonstration，非 resolve interpretive question）。Director 判定 Strong Should-Fix：Limitations 中应明确承认此为主要开放问题。\n— R2 提出 (N2)，R1 AGREE 方向但降级\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [warning, 共识] BT 模型 IIA 假设未讨论。**\nAppendix H 发现 formality 存在显著方向异质性（68.9% vs. 52.6%, Fisher p=0.015），BT 单参数公式可能遗漏效应异质性。需承认 IIA 假设并报告 direction-stratified BT。\n— R1 提出 (W2)，R2 AGREE\n\n**W2 [warning, 共识] NLI gate FNR 估计样本量过小。**\nFNR 基于仅 12 个 rejected pairs（Wilson 95% CI ≈ [2%, 28%]），CI 极宽。GPT-4o cross-validation 报告了 precision 但未报告 FNR CI。需量化报告。\n— R1 提出 (W3)，R2 AGREE\n\n**W3 [warning, 共识] Verbosity direction-aware gating 可能引入 selection bias。**\nDirection-aware gate 额外放入 21 pairs (+32%)，但这些 pairs 与 bidirectional-pass pairs 的特征可能不同。需报告两组分别的 BT estimates 作对比。\n— R1 提出 (W4)，R2 AGREE\n\n**W4 [warning, 共识] 3 个风格轴限制 \"framework\" 泛化声明。**\nRegister 仅 exploratory，实质只有 2 轴有 confirmatory evidence。CSD 方法论 axis-agnostic，但 \"framework\" 措辞暗示更广适用性。建议改为 \"methodology\"，Limitations 中列出未覆盖轴。\n— R2 提出 (W1)，R1 AGREE\n\n**W5 [warning, 共识] Measurement attenuation vs. construct divergence 歧义影响核心叙事。**\n\"Blindspot\" 术语偏向 attenuation 解释。如果 construct divergence 成立，Likert 并非 \"盲\"，而是测量不同构念。论文 §5.2/§6/Limitations 已有 balanced discussion，但标题和 Abstract framing 偏颇。至少在 Abstract 结尾加 caveat。\n— R1 提出 (W5)，R2 AGREE\n\n**W6 [warning, 共识] 生态效度讨论不足。**\nControlled manipulation → naturalistic evaluation 的 generalizability gap 未讨论。自然文本中 style 和 content 共变，NLI gate 无法直接应用。\n— R1 提出 (W6)，R2 AGREE\n\n**W7 [warning, 部分共识] Rewriting artifact 的 style-specific polishing interaction 未讨论。**\nSame-style double-rewrite 控制 style-neutral polishing，但 formal rewriting 的 polishing 可能不同于 casual rewriting。Formality 方向异质性可能混合 originality confound 和 style-specific polishing。\n— R2 提出 (W4)，R1 PARTIALLY AGREE\n\n**W8 [warning, 共识] Introduction motivating example 需 acknowledge formality-quality nuance。**\n\"Average height\" 例子暗示 formality bias 完全不合理，但论文自己的 GEE 结果显示 formality 存在 significant Originality effect——偏好 formal 文本可能部分反映合理质量判断。\n— R2 提出 (W5)，R1 AGREE\n\n### Minor\n\n- **M1**: Abstract 首句 \"near-perfect correlation\" 过于绝对（76–92% ≠ near-perfect）。改为 \"strong correlation\"。（R2 提出，R1 AGREE）\n- **M2**: Figure 2 (DAG) 尺寸偏小，颜色编码在低 DPI 下辨认困难。（Visual Check + R2）\n- **M3**: Pages 3–4 连续纯文本无 figure/table 穿插，视觉单调。建议将 Figure 2 前移。（Visual Check）\n- **M4**: Table 1 信息密度过高，建议增加 reading guide 或拆分。（R2 提出，R1 AGREE）\n- **M5**: §4.1 GEE exchangeable correlation 假设 justification 缺失。（R2-M3）\n- **M6**: Appendix 连续 4 页 12 张表格形成 \"表格墙\"。（Visual Check）\n- **M7**: NLI threshold 0.90 在主文缺 inline justification，需读者翻到 Appendix E。建议 §3.2 加一句简要说明。（R2-Q1，R1 AGREE）\n\n---\n\n## Reviewer Consensus\n\n| Issue | R1 | R2 | 共识 |\n|-------|----|----|------|\n| MF1: Primary family transparency | 提出 (N1) | AGREE | **Must-Fix** |\n| MF2: Cross-rewriter coverage | 提出 (N2) | AGREE (contextualize) | **Must-Fix** |\n| MF3: TOST Δ too wide | 提出 (N3) | AGREE (= W3) | **Must-Fix** |\n| MF4: Novelty positioning | AGREE (nuance) | 提出 (N1) | **Must-Fix** |\n| SF1: Human validation gap | AGREE (downgrade) | 提出 (N2) | **Strong Should-Fix** |\n| W1-W8: 8 Should-Fix issues | 见上 | 见上 | **Should-Fix** |\n| M1-M7: 7 Minor issues | 见上 | 见上 | **Minor** |\n\n---\n\n## Reviewer Divergence\n\n**分歧 1：因果框架表述一致性（R1-W1）**\nR1 认为全文因果术语不一致（\"Controlled Style Decomposition\" + DAG 暗示因果，§3.5 hedge 为 interventionist）。R2 REBUT：§3.5 的 caveat 恰当，\"controlled\" 指实验操控而非因果推断，DAG 常被用作 design rationale。**Director 判定：R2 REBUT 成立。** §3.5 的 hedge 措辞清晰，\"controlled\" 在实验设计语境下准确。仅建议在 §3.5 开头加一句统一声明。降为 Minor。\n\n**分歧 2：Likert vs. pairwise 比较的方法论公平性（R1-Q5）**\nR1 担忧不同统计效率的方法在同一样本量下比较对 Likert 不公平。R2 REBUT：Power analysis（Appendix K）+ 100-point continuous Likert（Appendix M）双重证据已表明问题超越简单样本量差异——Likert 模式下 judges 根本不产生 score variance，是 paradigmatic limitation 而非 power limitation。**Director 判定：R2 REBUT 成立。** 但建议在 §5.2 更明确回应此公平性 concern。\n\n---\n\n## Questions（需要作者澄清）\n\n1. Primary family 包含哪三个 judges？排除第四个的理由？是否有 pre-registration？\n2. Cross-rewriter independence test 仅覆盖 Qwen3-32B 是否资源约束？能否至少对 GPT-4o as judge 补一个小规模验证？\n3. Claude Sonnet 4 TOST 在 n=87 下能 reject 的最小 Δ 是多少？\n4. 是否考虑过 direction-stratified BT（按 original text direction 分层估计 win probability）？\n5. LLMBar 100 pairs 是从完整 benchmark 中 sample 还是用了全集？\n6. 100-point continuous Likert 仅用 Qwen3-32B，其他 judges 是否也显示相同 pattern？\n7. GEE formality interaction term 的 point estimates 和 direction？（即使不显著）\n\n---\n\n## Missing References\n\n1. **Girrbach et al. (2025/2026)** \"Likert or Not\" — LLM Likert 评分行为研究，与 Appendix M 直接相关（R2 建议，需验证真实性）\n2. **PRePair** (Jeong et al., 2025) — pairwise + pointwise 整合方法，可能是缓解 Blindspot 的替代方案（R2 建议）\n3. **Acquiescence bias / central tendency bias** — Likert scale 经典问题，§2 中一句话 mention 即可（R2 建议，R1 AGREE）\n\n---\n\n## External Review\n\n**外部审稿：未启用。** 本轮未配置 Stanford Agentic Reviewer。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (done, 耗时 ~3 min)\n\n| 严重度 | 数量 | 主要发现 |\n|--------|------|----------|\n| Critical | 0 | — |\n| Warning | 1 | Pages 3–4 连续纯文本无图表穿插，视觉单调。建议将 Figure 2 (DAG) 前移至 §3.5 首次引用处 |\n| Info | 10 | Table 1 信息密度高但可读；Figure 2 尺寸偏小；Figure 3/4 灰度区分良好；Appendix \"表格墙\"；booktabs 格式规范统一；参考文献无未解析引用 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | — | 4.0 | 4.0 |\n| Confidence | 4 | 4 | 4 |\n\n**支持 Conference (4.0) 的因素：**\n- 实验设计严谨度远超该领域平均水平（NLI gate + negative control + 7 种统计方法 + 100-point Likert + cross-benchmark + cross-rewriter + formal power analysis）\n- Likert Blindspot 的 empirical quantification 对 LLM evaluation 社区有直接实用价值\n- GEE per-axis confound decomposition 是 genuinely novel 的分析贡献\n- 五个 judges 跨三个 benchmark 的一致性令人信服\n- Appendix A–P 展示了出色的 rigor\n\n**拉向 Findings (3.0) 的因素：**\n- 核心概念（forced-choice > rating）在 psychometrics 中已有近百年历史；novelty 定位需更诚实\n- Primary family 构成透明度不足，影响 FWER 控制可信度\n- Cross-rewriter 验证仅覆盖 1/4 judges，限制 rewriter-independence claim\n- TOST negative control 功效不足（Δ=15pp 几乎涵盖最小 confirmed bias）\n- 缺少 human validation 区分 detection vs. amplification\n- 仅 3 个风格轴限制 framework 级别泛化\n\n**净判断：** 论文处于 Conference 和 Findings 边界。实验执行质量高，但多个方法论透明度问题（MF1 primary family、MF3 TOST）和 novelty 定位（MF4）需要在修改中解决。MF1/MF3 是纯写作/分析补充问题，可在一轮修改中完成。MF4（novelty reframing）需要调整叙事策略但不改变实验。SF1（human validation）是结构性限制，可通过 Limitations 重写部分 mitigate。如果 MF1–MF4 均得到充分回应，论文有潜力达到 4.0 (Conference)。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n信息密度高但可接受。\"near-perfect correlation\" 应改为 \"strong correlation\"（76–92% ≠ near-perfect）。GEE per-axis confound structure 的描述清晰且增量准确。建议移除部分括号内统计数字以降低认知负荷。\n\n### Section 1 (Introduction)\nOpening example 直观有效。但需 acknowledge formality-quality nuance：formality 改变可能合法影响 perceived quality（论文自己的 GEE 结果支持此点）。\"black-box controlled framework\" 表述准确（black-box 指 judge 而非 pipeline），但 \"framework\" 可改为 \"methodology\"。Contributions 列表清晰，item 1 的 \"the first\" 应改为 \"a unified\"。\n\n### Section 2 (Related Work)\n覆盖面广且组织良好。对 RATE 的对比公平。可补充 Likert scale 在社会科学中的经典问题（acquiescence bias, central tendency bias）一句话。\n\n### Section 3 (Method)\n§3.1 rewriting protocol 清晰。§3.2 NLI gate 设计精巧（bidirectional + direction-aware）。§3.3 measurement protocol 标准。§3.5 Design Rationale 的 DAG 和三个识别假设清晰，caveat 措辞恰当。假设 (iii)（style rewrite 不引入 target axis 之外的系统差异）最难验证，same-style DR 仅部分检验。\n\n### Section 4 (Experiments)\n§4.1 statistical framework 需明确 primary family 组成（MF1）。LLMBar n=100（NLI 后 n=88）是 moderate 样本；scaled replication n=355 仅覆盖一个 cell，对 generalizability 支持有限。\n\n### Section 5 (Analysis)\n§5.1 NLI gate validation thorough（FNR 8.4%, precision 98.9%, AC1=0.89），但 FNR 样本过小（n=12, CI 宽）。§5.2 核心发现清晰呈现；七方法 sensitivity hierarchy 有说服力。§5.3–5.4 cross-judge 和 cross-axis replication 增强结论稳健性。§5.5 register 过于压缩但在 8 页限制下可理解。§5.6 GEE decomposition 是论文第二主要贡献。\n\n### Section 6 (Conclusion)\n适当总结两个主要发现。\"whether measurement attenuation or construct divergence\" 的 open question 处理诚实。\n\n### Limitations\n覆盖了关键 weak points（evaluator-producer bias, methodology/scale, validation）。遗漏项：(1) 缺少 human validation 作为最主要的 open question；(2) 3 轴 coverage limitation；(3) 生态效度；(4) style-specific polishing interaction。\n\n### 格式合规\n- 正文 ≤8 页 ✓\n- Double-blind 匿名 ✓（\"Anonymous ACL submission\"，未发现自引泄漏）\n- ACL 双栏格式 ✓\n- Limitations 章节 ✓（3 段，覆盖适当，不过长）\n- ARR Checklist 不在 PDF 中 ✓\n- 参考文献格式一致 ✓",
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-22T03:47:47.328952+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4374
}
```

</details>

---


### Assistant

_source line 724 · 2026-05-22T03:47:57.525450+00:00_

审稿报告已投递至 Research Director。

**圆桌审稿 Round 8 完成总结：**

| 项目 | 结果 |
|------|------|
| **Overall Score** | **3.5 / 5 — Borderline Conference** |
| **Reviewer 一致性** | R1: 3.5, R2: 3.5, 交叉后均维持 |
| **Must-Fix** | 4 项（primary family 透明度、cross-rewriter 覆盖、TOST 功效不足、novelty 定位） |
| **Strong Should-Fix** | 1 项（human validation / detection vs amplification） |
| **Should-Fix** | 8 项（BT IIA、FNR 样本量、direction-aware gating、3 轴限制、attenuation vs divergence、生态效度、polishing interaction、motivating example） |
| **Minor** | 7 项 |
| **交叉共识率** | 86%（14 issues 中 12 条 AGREE，2 条 REBUT 已裁定） |
| **格式合规** | 全部通过（8 页、匿名、ACL 格式、Limitations） |
| **视觉审查** | 0 critical, 1 warning（pages 3-4 纯文本单调），10 info |

**核心判断**：论文实验执行质量属该领域上乘，但方法论透明度问题（primary family、TOST）和 novelty 定位需在修改中解决。如果 MF1–MF4 均得到充分回应，有潜力达到 4.0 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 72

## Round 72

2 recorded events


### User

_source line 725 · 2026-05-22T03:48:00.210250+00:00_

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部意见的逐条回应并提交给 Director。

核心判断：R2 的 N1（novelty 定位）和 N2（detection vs. amplification）是有力的批评；W3（TOST 功效）与我的 N3 完全吻合。主要分歧在两点：(1) N2 我认为应降为 Strong Should-Fix 而非 Must-Fix；(2) R2 对"black-box"的 overclaim 质疑我明确反驳——论文的"black-box"指 judge 而非整个 pipeline，表述准确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 726 · 2026-05-22T03:48:11.066586+00:00_

审稿报告已投递至 Research Director。

**Round 8 审稿完成。**

**最终评分：3.5 / 5 — Borderline Conference**

核心结论：
- **4 个 Must-Fix**：primary family 透明度、cross-rewriter 覆盖不足、TOST Δ 过宽、novelty 定位需更诚实
- **1 个 Strong Should-Fix**：缺少 human validation 区分 detection vs. amplification
- **8 个 Should-Fix**：BT IIA、NLI FNR 样本小、direction-aware gating bias、3 轴泛化限制、attenuation vs. divergence 歧义、生态效度、rewriting artifact interaction、motivating example nuance
- **7 个 Minor**：Abstract 措辞、Figure 2 尺寸、Table 1 密度等

MF1–MF3 均为写作/分析补充问题，可在一轮修改中完成。MF4 需调整叙事策略但不改变实验。如果全部 Must-Fix 得到充分回应，论文有潜力达到 4.0 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 73

## Round 73

62 recorded events


### User

_source line 727 · 2026-05-22T09:10:40.114193+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-22T09:10:46.709623+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-22T09:10:46.710268+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-22T09:10:53.935755+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "9"
  }
}
```

</details>

---


### Tool result

_source line 731 · 2026-05-22T09:10:53.936129+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-22T09:11:00.067992+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-22T09:11:00.118626+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-22T09:11:03.884440+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 735 · 2026-05-22T09:11:05.297235+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (54 个)\n\n- **verbosity_32b**: DONE (success) — \n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **register_100_cf** (killed): Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality\n- **gemini_flash_fourth_judge** (success): Gemini Flash as a fourth judge will also exhibit style blindspot (BT-significant but Likert-NS) on formality and verbosity axes, consistent with GPT-4o, Qwen-32B, and Claude judges, confirming the blindspot is judge-universal rather than model-specific.\n- **llama70b_register** (success): Llama-70B register axis shows weak style bias (~55% BT, consistent with GPT-4o 57% and Qwen3-32B 55.3%), confirming register as originality-dominated across three independent judge architectures\n  [llama70b_register_summary](/api/workspace-files/projects/causal_style_decomp_judge/artifacts/llama70b_register/data/llama70b_register_summary.json)\n\n## 趋势\n成功 38 / 负向 12 / 失败 0 / 共 54\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- register_100_cf: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool call

_source line 736 · 2026-05-22T09:11:05.297658+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-22T09:11:06.252042+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Detecting Hidden Style Bias\\in LLM Judges via Controlled Style Decomposition}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding and construct validity.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
43	Although the formality effect survives logistic adjustment for original preference ($\text{OR} = 2.32$, $p = 0.006$; Appendix~\ref{app:direction}), residual confounding is not fully eliminated.
44	An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure. The Comparative Trap \citep{jeong2025comparative} lends support to this alternative; six experimental controls bound this risk (\S\ref{sec:amplification}), though definitive separation would require human ground-truth ratings.
45	The primary open question is whether pairwise comparison detects genuine style bias or amplifies micro-preferences inhe
…[truncated 2559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-22T09:11:06.252462+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 739 · 2026-05-22T09:11:06.553837+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "report.md"
  }
}
```

</details>

---


### Tool result

_source line 740 · 2026-05-22T09:11:13.330190+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the web search results, I found information about EMNLP 2026 but the results prim
…[truncated 1143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 7077
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-22T09:11:13.380967+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **register_100_cf** (killed): Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality\\n- **gemini_flash_fourth_judge** (success): Gemini Flash as a fourth judge will also exhibit style blindspot (BT-significant but Likert-NS) on formality and verbosity axes, consistent with GPT-4o, Qwen-32B, and Claude judges, confirming the blindspot is judge-universal rather than model-specific.\\n- **llama70b_register** (success): Llama-70B register axis shows weak style bias (~55% BT, consistent with GPT-4o 57% and Qwen3-32B 55.3%), confirming register as originality-dominated across three independent judge architectures\\n  [llama70b_register_summary](/api/workspace-files/projects/causal_style_decomp_judge/artifacts/llama70b_register/data/llama70b_register_summary.json)\\n\\n## 趋势\\n成功 38 / 负向 12 / 失败 0 / 共 54\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestb-29275: 无 GPU 信息\\n\\n## 告警\\n- exp-013: 已被终止 — unknown\\n- register_100_cf: 已被终止 — unknown\\n- exp-015: 已被终止 — unknown\\n- exp-016: 已被终止 — unknown\\n\", \"total_chars\": 1247, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6827
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-22T09:11:20.407633+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline ARR cycle paper format guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline ARR cycle paper format guidelines"
  }
}
```

</details>

---


### Tool call

_source line 743 · 2026-05-22T09:11:21.311488+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 744 · 2026-05-22T09:11:21.713567+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 745 · 2026-05-22T09:11:21.713906+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 746 · 2026-05-22T09:11:27.485170+00:00_

Web search results for query: "EMNLP 2026 submission deadline ARR cycle paper format guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here is the information about EMNLP 2026 submission deadlines, ARR cycle, and paper format guidelines:

## ARR Submission Deadline

The ARR submission deadline for long and short papers is May 25, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Important Dates

Additional key deadlines include:
- Reviewer registration deadline for ALL authors: May 27, 2026
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026

## Paper Format Guidelines

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. 

Specific formatting requirements:
- The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers
- The mandatory Limitations
…[truncated 537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 7077
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-22T09:11:27.485573+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'causal_style_decomp_judge'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5771
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-22T09:11:32.254013+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections"
  }
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-22T09:11:32.404998+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-22T09:11:32.706610+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org call for main conference papers submission format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org call for main conference papers submission format"
  }
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-22T09:11:39.284193+00:00_

Web search results for query: "site:2026.emnlp.org call for main conference papers submission format"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here's the information about the EMNLP 2026 main conference papers submission format:

## Paper Types and Format

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL c
…[truncated 989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6577
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-22T09:11:43.099193+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-22T09:11:43.451064+00:00_

1	\begin{abstract}
2	Likert scoring---the default evaluation mode for LLM judges---systematically misses style biases that pairwise comparison detects.
3	We introduce Controlled Style Decomposition (CSD), a black-box framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison to quantify style bias in LLM judges.
4	Across four target judges from four independent organizations, one negative control, three benchmarks, and three style axes, CSD reveals the Likert Blindspot: a severity spectrum from complete attenuation at moderate bias to over 60\% signal loss at stronger effects, confirmed by seven statistical methods.
5	GEE conditional decomposition reveals a per-axis confound structure consistent across all four target judges: verbosity bias is style-dominated, formality exhibits a conditional effect moderated by content quality, and register is judge-dependent---determining which estimates are directly interpretable and which require conditional analysis.
6	A negative-control judge shows no detectable bias on either primary axis, supporting discriminative validity.
7	Whether the Blindspot reflects measurement attenuation or genuine construct divergence between absolute and comparative evaluation remains an open question; under either interpretation, Likert-only evaluation systematically misses style-driven preferences that propagate through pairwise-based alignment pipelines.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-22T09:11:43.451440+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-22T09:11:43.903535+00:00_

1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} --- given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions.
5	This is the \emph{Likert Blindspot}.
6	We note that formality preferences may partially reflect legitimate quality judgments---our GEE decomposition (\S\ref{sec:direction}) quantifies this originality component.
7	This example reflects a systematic pattern.
8	
9	LLM judges are central infrastructure for NLP evaluation and alignment training (RLHF, DPO), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.
10	Style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}: 76--92\% of observed preferences originate from surface-level style cues \citep{li2026preference}, with bias scores of 0.76--0.92 across five judges \citep{soumik2026judging}.
11	Despite this consensus, existing approaches address individual requirements (multi-dimensional style analysis \citep{casse2026concise,wang2026fairjudge}, interventional design \citep{reber2025rate}, population-level correction \citep{dubois2025lc}), but no single framework integrates per-axis decomposition, interventional identification, per-instance diagnostics, and black-box applicability.
12	A further concern: standard Likert scoring produces ${\sim}60\%$ uninformative ties, and even non-tied pairs carry weaker signal than pairwise comparison---a limitation predicted by measurement theory \citep{thurstone1927law} but previously unquantified for LLM judges.
13	
14	We propose Controlled Style Decomposition (CSD), combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
15	I
…[truncated 2116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-22T09:11:43.904054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-22T09:11:44.406241+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Interventional Approaches to Judge Bias}
7	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
8	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
9	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
10	If this Likert Blindspot generalizes beyond our setting, RATE's own style-related findings may underestimate the true magnitude of attribute effects.
11	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
12	\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
13	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control rather than parametric aggregation.
14	
15	\paragrap
…[truncated 5015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-22T09:11:44.406745+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-22T09:11:45.310743+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Style-Controlled Rewriting}
5	\label{sec:rewriting}
6	
7	We isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
8	For each text, an instruction-tuned LLM (Qwen3-32B) classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification).
9	It then rewrites the text toward the opposite pole (temperature 0.7) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
10	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
11	Each operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
12	To control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
13	
14	\subsection{Content Preservation Verification}
15	\label{sec:nli_gate}
16	
17	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
18	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with an entailment threshold of 0.90, selected as the threshold above which NLI performance plateaus (Appendix~\ref{app:nli_sweep}).
19	For axes that preserve information density (formality, register), we apply standard bidirectional entailment: both NLI(original $\to$ rewrite) and NLI(rewrite $\to$ original) must exceed this value.
20	For axes that inherently c
…[truncated 5691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-22T09:11:45.311096+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-22T09:11:45.813549+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	The primary family comprises six tests---three target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B) $\times$ two axes (formality, verbosity)---corrected via Holm-Bonferroni at $\alpha = 0.05$; Gemini-2.5-Flash serves as confirmatory replication and is excluded from FWER control; as a sensitivity check, all eight tests remain significant under the expanded family (Appendix~\ref{app:holm8}).
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.\footnote{The BT model assumes IIA (independence of irrelevant alternatives). Direction-stratified BT estimates (Appendix~\ref{app:bt_gof}) show significant direction asymmetry for formality (formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$) but not verbosity ($p = 0.453$).}
13	All bootstrap confidence intervals use 10{,}000 pair-level resamples with seed 42.
14	GEE models use exchangeable working correlation, justified by near-zero estimated within-pair correlations ($\hat{\alpha} \in [-0.25, +0.11]$; Appendix~\ref{app:gee_diagnostics}).
15	
16	\paragraph{Model selection.}
17	Target judges span 
…[truncated 15409 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-22T09:11:45.813923+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-22T09:11:46.015546+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	CSD yields two findings.
5	First, the \emph{Likert Blindspot}: Likert scoring systematically misses style biases that pairwise comparison detects---complete at moderate bias ($d \to 0$ at $n = 355$), ${>}60\%$ attenuation at stronger effects---confirmed by seven statistical methods; whether this reflects measurement attenuation or construct divergence, Likert-only audits miss style-driven preferences that propagate through alignment pipelines.
6	Second, GEE conditional decomposition reveals per-axis confound structure---verbosity style-dominated, formality conditional, register judge-dependent---determining which estimates require conditional analysis.
7	
8	Existing Likert-based null findings may reflect measurement insensitivity rather than absence of bias; pairwise comparison with amplification controls (\S\ref{sec:amplification}) offers superior detection sensitivity.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-22T09:11:46.066231+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-22T09:11:46.368717+00:00_

1	\appendix
2	
3	\noindent\emph{Organization: confound analysis (A--B), model diagnostics (C), independence tests (D), gate validation (E--F), equivalence testing (G), statistical details (H--K), sensitivity analyses (L--N), artifact controls (O), implementation (P).}
4	
5	\section{Direction Asymmetry and Quality Confounding}
6	\label{app:direction}
7	
8	The formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\% of formal-is-rewrite pairs ($p = 0.001$) but only 54.5\% of casual-is-rewrite pairs ($p = 0.83$).
9	This asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.
10	To quantify this, we fit a GEE logistic model (exchangeable correlation) with both formality and original-preference as predictors.
11	After controlling for original preference, the formality effect remains significant ($\text{OR} = 2.58$, $p = 0.002$), and the original-preference effect is also significant ($\text{OR} = 2.32$, $p = 0.006$).
12	The formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.
13	
14	At $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exceeded the GPT-4o estimate ($2.58$), but a scaled replication ($n = 355$) corrects this to $2.15$ ($p < 0.0001$), comparable to GPT-4o and consistent with small-sample upward bias rather than evaluator-producer inflation of the style effect.
15	The originality confound remains stronger ($4.99$ vs.\ $2.32$), consistent with evaluator-producer bias inflating the originality component (Limitations).
16	The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.
17	
18	The NL
…[truncated 24918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 766 · 2026-05-22T09:11:53.296716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "offset": "468"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
    "offset": "468"
  }
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-22T09:11:54.150273+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (468). The file has 468 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-22T09:11:54.602443+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 769 · 2026-05-22T09:11:55.104902+00:00_

-rw-r--r-- 1 ubuntu ubuntu 379388 May 22 09:08 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-22T09:11:56.059483+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-22T09:11:56.462958+00:00_

&lt;persisted-output>
Output too large (45.9KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/ac32e3f2-434b-434d-b640-29531c2ffb24/tool-results/b3b4h0xo9.txt

Preview (first 2KB):
issues:
  # ============================================================
  # Round 1-4 issues (all resolved unless noted)
  # ============================================================

  - id: "R1-N1"
    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
    resolution_round: 4
    mentions:
      - round: 3
        reviewers: [1, 2]
        note: "因果语言降级问题在 Round 3 以新形式复发，见 R3-N1"
      - round: 4
        reviewers: [1]
        note: "R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。"
      - round: 5
        reviewers: [1, 2]
        note: "标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2"
      - round: 8
        reviewers: []
        note: "本轮未提及，可能已修复，待 Research Director 确认"

  - id: "R2-N1"
    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
    category: framing
    severity: warning
    status: in_progress
    first_raised_round: 1
    last_seen_round: 8
    resolution: null
    resolution_round: null
    mentions:
      - round: 3
        reviewers: [1, 2]
        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
      - round: 4
        reviewers: [1, 2]
        note: "R4-SF8: Honest novelty positioning applied."
      - round: 5
        reviewers: [1, 2]
        note: "Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。"
      - round: 7
        reviewers: [2]
        note: "R2 再次指出核心发现可从 Thurstone (1927) 理论直接预测。R1 
…[truncated 129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-22T09:11:56.463368+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-22T09:11:56.564345+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/decisions.yaml\", \"content\": \"_next_id: 66\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 14:09 UTC\\n  summary: '文献蒸馏审视：研究方向无需调整，CSD 填补 #1 空白（多维 style 因果分解），post-MVP 需扩展 judge/benchmark/baseline\\n    覆盖'\\n  rationale: '10 篇论文蒸馏显示：(1) 多维 style 联合因果分解是领域 #1 空白，与 CSD 核心 claim 完全对齐；(2) 竞品 claim\\n    无直接重叠（FairJudge=white-box, Pref Leakage=family-based, Soumik=prompt-dependent）；(3)\\n    同行标准要求 3-5 异构 judge + AlpacaEval/Arena-Hard/MT-Bench + Bootstrap CIs + 对比 LC-AlpacaEval\\n    baseline。当前 MVP 方案足够，research 阶段需按蒸馏标准扩展。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 14:19 UTC\\n  summary: MVP 全量评分 + 分层分析：score 全部 100 条，按 BERTScore 阈值 0.88/0.90/0.92 分层算 ATE，不降低阈值\\n  rationale: 36% pass rate (BERTScore≥0.92) 偏低但 NLI 均值 0.9422 说明语义保留好。降阈值是数据操作，不如保留完整信息。全量评分\\n    (n=100) 保证统计 power，分层分析同时回答\\\"严格阈值下效应是否存在\\\"和\\\"宽松阈值下效应是否增强\\\"。8B H1 fail 不消耗迭代配额（ROADMAP\\n    规则），32B 备用。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 14:20 UTC\\n  summary: H1 content verification 改为 NLI-only gate（≥0.90），BERTScore 降为监控指标，不作为过滤条件\\n  rationale: Reviewer 诊断：36% pass rate 的根因是 BERTScore 惩罚 style transfer 预期的词汇变化（contractions→full\\n    forms 等），而非内容泄漏。NLI 均值 0.9422、抽样 >0.99 证明语义保留良好。BERTScore 作为 token-level 相似度指标与\\n    style transfer 评估目标矛盾（改的就是 token）。Double-rewrite pass rate 更低（21/100）进一步印证。NLI-only\\n    gate 是度量校准（不消耗 8B 迭代配额），与 D002 全量评分兼容——primary ATE 用 NLI≥0.90 子集，secondary 按 BERTScore\\n    分层。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 14:32 UTC\\n  summary: 8B 初步 ATE≈0.028 不可见，归因三因素：Likert 粒度 + 8B rewriter 质量 + RATE corruption。不计入\\n    kill criteria，等 n=100 + 32B\\n  rationale: 36/100 初步数据 Cohen's d=0.055 远低于 0.3 门槛，但三个叠加因素解释了结果：(1) 83% 零差异源于 integer\\n    Likert 无法捕捉 sub-integer 效应；(2) 22% identical rewrites 稀释 ATE；
…[truncated 1456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-22T09:12:01.162998+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 775 · 2026-05-22T09:12:01.514907+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 776 · 2026-05-22T09:12:01.716131+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 777 · 2026-05-22T09:12:01.766841+00:00_

1	@inproceedings{tripathi2025pairwise,
2	  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},
3	  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},
4	  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},
5	  year={2025},
6	  url={https://arxiv.org/abs/2504.14716}
7	}
8	
9	@inproceedings{murugadoss2025sos,
10	  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},
11	  author={Murugadoss, Aakanksha and others},
12	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
13	  year={2025},
14	  url={https://arxiv.org/abs/2409.15268}
15	}
16	
17	@inproceedings{li2026preference,
18	  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},
19	  author={Li, Dawei and others},
20	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
21	  year={2026},
22	  url={https://arxiv.org/abs/2502.01534}
23	}
24	
25	@article{wang2026fairjudge,
26	  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},
27	  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},
28	  journal={arXiv preprint arXiv:2602.06625},
29	  year={2026},
30	  url={https://arxiv.org/abs/2602.06625}
31	}
32	
33	
34	@inproceedings{dubois2025lc,
35	  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},
36	  author={Dubois, Yann and others},
37	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
38	  year={2025},
39	  url={https://arxiv.org/abs/2404.04475}
40	}
41	
42	@article{casse2026concise,
43	  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},
44	  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},
45	  journal={arXiv preprint arXiv:2601.10809},
46	  year={2026
…[truncated 97 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 778 · 2026-05-22T09:12:05.234124+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge -name \"config.*\" -o -name \"*.yaml\" -maxdepth 2 2>/dev/null | head -20",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge -name \"config.*\" -o -name \"*.yaml\" -maxdepth 2 2>/dev/null | head -20",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 779 · 2026-05-22T09:12:05.284880+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/lc_alpacaeval_2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/rate_icml_2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/casse_2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/preference_leakage_2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/dml_chernozhukov_2018.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/counterfactual_rhetorical_2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/fairjudge_2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/soumik_2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/sos_bench_2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/veitch_uai_2020.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/decisions.yaml
/h
…[truncated 101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 780 · 2026-05-22T09:12:09.653102+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -name \"project_configs*\" -o -name \"projects_config*\" -maxdepth 3 2>/dev/null | head -5; grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/ --include=\"*.yaml\" --include=\"*.json\" -l 2>/dev/null | head -5; grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_5/ --include=\"*.yaml\" --include=\"*.json\" -l 2>/dev/null | head -5",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -name \"project_configs*\" -o -name \"projects_config*\" -maxdepth 3 2>/dev/null | head -5; grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/ --include=\"*.yaml\" --include=\"*.json\" -l 2>/dev/null | head -5; grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_5/ --include=\"*.yaml\" --include=\"*.json\" -l 2>/dev/null | head -5",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 781 · 2026-05-22T09:12:09.856975+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-22T09:12:34.499658+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-22T09:12:58.428670+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23929
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-22T09:12:58.553029+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性、实验设计、统计方法论**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL template, double-blind, 正文 8 页限制, references 不限页, Limitations 必须有但不计入页数\n- **匿名规则**: double-blind（作者信息不可出现）\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf`\n\n## 论文概述\n题目: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\"\n核心claim: Likert评分系统性地遗漏了pairwise comparison能检测到的风格偏差（Likert Blindspot），提出CSD框架（NLI-gated content control + per-axis style decomposition + position-controlled pairwise comparison）来量化LLM judges的风格偏差。\n\n## 你的审查重点\n\n### 1. 方法论严谨性\n- CSD pipeline 的因果推断框架是否合理？§3.5 Design Rationale 中的 DAG 是否自洽？三个 identification assumptions 是否充分？\n- NLI gate (DeBERTa-v3-large, threshold 0.90) 作为 content preservation 的唯一门控是否足够？单向/双向 entailment 的 axis-dependent 策略是否有理论依据？\n- Style-controlled rewriting 是否真正只改变一个 style axis？是否有其他 confound 未被控制（例如 style axis 之间的 interaction）？\n- Evaluator-producer overlap (Qwen3-32B 同时做 rewriter 和 judge) 的处理是否充分？\n\n### 2. 统计方法论\n- Holm-Bonferroni correction 的 family 定义（6-test primary + Gemini confirmatory 排除）是否合理？\n- Bradley-Terry model 的使用是否恰当？IIA assumption 在这个 context 下是否成立？\n- GEE conditional decomposition 的 exchangeable working correlation 假设是否合理？interaction test 是否充分？\n- Power analysis 和 bootstrap attenuation analysis 的设计是否正确？\n- 负对照 (Claude Sonnet 4) 的 TOST equivalence testing 是否设计合理？Δ=15pp margin 是否过宽？\n\n### 3. 实验设计\n- LLMBar (n=100) 作为主要 benchmark 的代表性如何？样本量是否足够支撑 claims？\n- Cross-benchmark (AlpacaEval, MT-Bench) 验证是否充分？为什么只做了部分 judge×axis 组合？\n- Register axis 作为 exploratory 的定位是否诚实？与 formality/verbosity 的方法论差异（缺少 cross-rewriter validation）是否被充分 disclose？\n- 负对照 (Claude Sonnet 4) 只在两个 axis 上测试是否足够？\n\n### 4. 格式检查\n- 正文是否在 8 页以内\n- 是否 double-blind（无作者泄露信息）\n- Limitations section 是否存在且合理\n- 引用格式是否符合 ACL 规范\n\n请按 ARR review form 格式输出你的审稿意见：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (1-5 scale per EMNLP 2026 ARR guidelines), Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性、实验设计、统计方法论**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL template, double-blind, 正文 8 页限制, references 不限页, Limitations 必须有但不计入页数\n- **匿名规则**: double-blind（作者信息不可出现）\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf`\n\n## 论文概述\n题目: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\"\n核心claim: Likert评分系统性地遗漏了pairwise comparison能检测到的风格偏差（Likert Blindspot），提出CSD框架（NLI-gated content control + per-axis style decomposition + position-controlled pairwise comparison）来量化LLM judges的风格偏差。\n\n## 你的审查重点\n\n### 1. 方法论严谨性\n- CSD pipeline 的因果推断框架是否合理？§3.5 Design Rationale 中的 DAG 是否自洽？三个 identification assumptions 是否充分？\n- NLI gate (DeBERTa-v3-large, threshold 0.90) 作为 content preservation 的唯一门控是否足够？单向/双向 entailment 的 axis-dependent 策略是否有理论依据？\n- Style-controlled rewriting 是否真正只改变一个 style axis？是否有其他 confound 未被控制（例如 style axis 之间的 interaction）？\n- Evaluator-producer overlap (Qwen3-32B 同时做 rewriter 和 judge) 的处理是否充分？\n\n### 2. 统计方法论\n- Holm-Bonferroni correction 的 family 定义（6-test primary + Gemini confirmatory 排除）是否合理？\n- Bradley-Terry model 的使用是否恰当？IIA assumption 在这个 context 下是否成立？\n- GEE conditional decomposition 的 exchangeable working correlation 假设是否合理？interaction test 是否充分？\n- Power analysis 和 bootstrap attenuation analysis 的设计是否正确？\n- 负对照 (Claude Sonnet 4) 的 TOST equivalence testing 是否设计合理？Δ=15pp margin 是否过宽？\n\n### 3. 实验设计\n- LLMBar (n=100) 作为主要 benchmark 的代表性如何？样本量是否足够支撑 claims？\n- Cross-benchmark (AlpacaEval, MT-Bench) 验证是否充分？为什么只做了部分 judge×axis 组合？\n- Register axis 作为 exploratory 的定位是否诚实？与 formality/verbosity 的方法论差异（缺少 cross-rewriter validation）是否被充分 disclose？\n- 负对照 (Claude Sonnet 4) 只在两个 axis 上测试是否足够？\n\n### 4. 格式检查\n- 正文是否在 8 页以内\n- 是否 double-blind（无作者泄露信息）\n- Limitations section 是否存在且合理\n- 引用格式是否符合 ACL 规范\n\n请按 ARR review form 格式输出你的审稿意见：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (1-5 scale per EMNLP 2026 ARR guidelines), Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-22T09:13:18.148233+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19595
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-22T09:13:18.299565+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "你是 Reviewer 2，负责审查 **新颖性、完整性、related work 覆盖、写作质量**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL template, double-blind, 正文 8 页限制, references 不限页, Limitations 必须有但不计入页数\n- **匿名规则**: double-blind（作者信息不可出现）\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf`\n\n## 论文概述\n题目: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\"\n核心claim: Likert评分系统性地遗漏了pairwise comparison能检测到的风格偏差（Likert Blindspot），提出CSD框架（NLI-gated content control + per-axis style decomposition + position-controlled pairwise comparison）来量化LLM judges的风格偏差。跨四个独立 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、一个负对照（Claude Sonnet 4）、三个 benchmark、三个 style axis 验证。\n\n## 你的审查重点\n\n### 1. 新颖性评估\n- \"Likert Blindspot\" 作为核心发现：这是否真正是新发现？Thurstone (1927) 的 Law of Comparative Judgment 已经预测了 pairwise > Likert 的敏感性差异。本文的 empirical contribution 是否足以构成顶会水平的 novelty？\n- CSD 框架的各个组件（NLI gating, style rewriting, BT model）都是已有技术的组合——组合本身是否构成足够 novelty？\n- 与 RATE (Reber et al., 2025) 的区分是否清晰？本文是否主要是 RATE 的 measurement mode upgrade（从 Likert 换成 pairwise）？\n- Per-axis confound structure（GEE decomposition 揭示 verbosity=style-dominated, formality=conditional, register=judge-dependent）是否是独立的 novel contribution？\n\n### 2. Related Work 覆盖\n- 是否遗漏重要的相关工作？特别是：\n  - LLM-as-judge bias 的最新工作（2025-2026）\n  - 因果文本分析方法（CausalM, CausalNLP 等）\n  - 风格偏差检测和缓解\n  - 测量理论在 NLP 评估中的应用\n- 与竞品的定位是否准确？（RATE, CASSE, FairJudge, Preference Leakage, Soumik 2026 等）\n- 引用是否完整和准确？\n\n### 3. 完整性\n- 论文的 story line 是否连贯？从 problem → method → experiments → analysis 的逻辑链是否完整？\n- 是否有 claims 缺乏足够支撑？\n- Limitations section 是否诚实和完整？是否有重大缺陷被忽略？\n- Conclusion 是否过于 strong / weak relative to evidence?\n\n### 4. 写作质量\n- 论文的可读性如何？结构是否清晰？\n- 术语使用是否一致？\n- 图表是否有效传达信息？\n- Abstract 是否准确概括论文内容？\n- 是否有 AI 生成痕迹（过度使用 hedging, boilerplate phrases 等）？\n\n### 5. 对 EMNLP community 的影响力\n- 这个 work 的 target audience 是谁？\n- 对 LLM evaluation 实践有什么直接 actionable takeaway？\n- 是否会激发 follow-up research？\n\n请按 ARR review form 格式输出你的审稿意见：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (1-5 scale per EMNLP 2026 ARR guidelines), Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "你是 Reviewer 2，负责审查 **新颖性、完整性、related work 覆盖、写作质量**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL template, double-blind, 正文 8 页限制, references 不限页, Limitations 必须有但不计入页数\n- **匿名规则**: double-blind（作者信息不可出现）\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf`\n\n## 论文概述\n题目: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\"\n核心claim: Likert评分系统性地遗漏了pairwise comparison能检测到的风格偏差（Likert Blindspot），提出CSD框架（NLI-gated content control + per-axis style decomposition + position-controlled pairwise comparison）来量化LLM judges的风格偏差。跨四个独立 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、一个负对照（Claude Sonnet 4）、三个 benchmark、三个 style axis 验证。\n\n## 你的审查重点\n\n### 1. 新颖性评估\n- \"Likert Blindspot\" 作为核心发现：这是否真正是新发现？Thurstone (1927) 的 Law of Comparative Judgment 已经预测了 pairwise > Likert 的敏感性差异。本文的 empirical contribution 是否足以构成顶会水平的 novelty？\n- CSD 框架的各个组件（NLI gating, style rewriting, BT model）都是已有技术的组合——组合本身是否构成足够 novelty？\n- 与 RATE (Reber et al., 2025) 的区分是否清晰？本文是否主要是 RATE 的 measurement mode upgrade（从 Likert 换成 pairwise）？\n- Per-axis confound structure（GEE decomposition 揭示 verbosity=style-dominated, formality=conditional, register=judge-dependent）是否是独立的 novel contribution？\n\n### 2. Related Work 覆盖\n- 是否遗漏重要的相关工作？特别是：\n  - LLM-as-judge bias 的最新工作（2025-2026）\n  - 因果文本分析方法（CausalM, CausalNLP 等）\n  - 风格偏差检测和缓解\n  - 测量理论在 NLP 评估中的应用\n- 与竞品的定位是否准确？（RATE, CASSE, FairJudge, Preference Leakage, Soumik 2026 等）\n- 引用是否完整和准确？\n\n### 3. 完整性\n- 论文的 story line 是否连贯？从 problem → method → experiments → analysis 的逻辑链是否完整？\n- 是否有 claims 缺乏足够支撑？\n- Limitations section 是否诚实和完整？是否有重大缺陷被忽略？\n- Conclusion 是否过于 strong / weak relative to evidence?\n\n### 4. 写作质量\n- 论文的可读性如何？结构是否清晰？\n- 术语使用是否一致？\n- 图表是否有效传达信息？\n- Abstract 是否准确概括论文内容？\n- 是否有 AI 生成痕迹（过度使用 hedging, boilerplate phrases 等）？\n\n### 5. 对 EMNLP community 的影响力\n- 这个 work 的 target audience 是谁？\n- 对 LLM evaluation 实践有什么直接 actionable takeaway？\n- 是否会激发 follow-up research？\n\n请按 ARR review form 格式输出你的审稿意见：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (1-5 scale per EMNLP 2026 ARR guidelines), Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-22T09:13:19.911177+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1611
}
```

</details>

---


### Assistant

_source line 788 · 2026-05-22T09:13:27.692247+00:00_

Round 1 已启动，三项任务并行执行中：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 统计方法论） | 已派发 |
| Reviewer 2（新颖性 + 完整性 + 写作） | 已派发 |
| 视觉审查 Agent | 已启动 |

等待 Reviewer 返回初审意见后进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 74

## Round 74

2 recorded events


### User

_source line 789 · 2026-05-22T09:19:00.947676+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见 — 方法严谨性、实验设计、统计方法论

### Paper Summary

本文提出"Likert Blindspot"现象：Likert 评分系统性地遗漏 pairwise comparison 能检测到的 LLM judge 风格偏差。作者设计了 Controlled Style Decomposition (CSD) 框架——通过 NLI-gated content control、per-axis style rewriting、position-controlled pairwise comparison——在 4 个 target judge、3 个 benchmark、3 个 style axis 上量化该现象。七种统计方法一致确认：pairwise BT 概率在 formality 和 verbosity 上显著偏离 0.50（最高 BT 77.3%），而同一干预下 Likert ATE 始终不显著。Claude Sonnet 4 作为负对照未检出偏差，支持因果解读。

---

### Summary of Strengths

**S1. 研究问题新颖且有实际影响。** Likert 与 pairwise 评估格式的系统性灵敏度差异此前被直觉认知但从未被控制实验量化。这一发现对依赖 Likert 评分的 leaderboard 和 alignment pipeline 有直接警示意义。

**S2. 统计方法论严谨且多层次。** 七种统计方法（BT model、sign test、Likert ATE/t-test、binomial、ordinal regression、GEE、Wilcoxon signed-rank）交叉验证同一结论（Table 2），排除了结论对单一检验方法的依赖。Holm-Bonferroni correction 的 family 定义清晰（§4.1），exploratory/confirmatory 分类合理。

**S3. 因果推断框架诚实定位。** §3.5 Design Rationale 明确表示 DAG 是"design rationale, not a claim of perfect identification"，三个 operational assumptions 逐一列出并在附录中提供了经验验证（NLI threshold sweep Appendix E, direction-aware gate Appendix F, cross-rewriter Appendix D/Tables 7-8），没有过度声称因果识别。

**S4. 负对照设计有效。** Claude Sonnet 4 作为负对照（§5.4, Appendix G），在 formality 和 verbosity 上 BT ≈ 54-56%，TOST 确认等价性——为其他 judge 的显著偏差提供了有力的因果对比。

**S5. 充分的 robustness 分析。** Bootstrap attenuation analysis（Appendix J, d = −0.017）排除了 measurement attenuation 解释；power analysis（Appendix K）量化了 Likert 达到 80% power 所需样本量（1,473–6,737），有力地论证了 Blindspot 的结构性本质。GEE exchangeable vs. independence working correlation 在 Appendix C 中报告了一致结果。

**S6. 跨 benchmark/rewriter/judge 验证体系。** 主实验（LLMBar）+ cross-benchmark（AlpacaEval, MT-Bench）+ cross-rewriter（GPT-4o 独立 rewriter, Tables 7-8）+ cross-architecture（4 judge families）+ 负对照，形成了较完整的验证矩阵。

---

### Summary of Weaknesses

**N1** [critical] **NLI gate 作为 content preservation 的唯一门控缺乏人工验证**
- 具体位置：§3.2, Limitations (p.8)
- 问题：CSD 的因果推断完全依赖 NLI gate（DeBERTa-v3-large, threshold 0.90）保证 content 不变。然而 NLI 模型本身可能存在系统性盲区——例如对隐含推理链的改变、对论证结构重组的不敏感。论文未报告对 NLI-gated pairs 的任何人工抽样验证（human evaluation of content preservation quality）。Limitations 中承认"cannot block quality perception shifts mediated by style itself"，但这一局限的严重性需要实证数据来界定——至少应抽样 50-100 对，让人工标注者判断 content 是否实质等价。
- 为什么影响接收：这是 CSD 因果推断链条的最薄弱环节。如果 NLI gate 系统性地放过了某些 content 变化（例如 formal 改写倾向于增加 hedging 从而实质改变 claim 强度），则观测到的"style bias"可能部分是 content bias 的伪装。
- 建议修改方向：对 NLI-passed 和 NLI-failed pairs 各抽样 50 对，收集 3 名标注者的 content equivalence 判断（binary: equivalent/not equivalent），报告 agreement 和 false-pass rate。

**N2** [critical] **"Likert Blindspot" 的 framing 过于强势，忽视了 ordinal vs. forced-choice 灵敏度差异的已知理论背景**
- 具体位置：Title, Abstract, §1 ("This is the Likert Blindspot"), §5.1
- 问题：Likert（绝对评分）与 pairwise comparison（强制选择）的灵敏度差异是测量理论中的经典结论——Thurstone (1927) 已经指出 forced-choice 比 absolute rating 更能识别微小差异，Preston and Colman (2000) 等研究也系统探讨了 scale granularity 对 discriminability 的影响。论文在 §2 和 §5.1 确实引用了这些文献，也在 §5.1 讨论了"measurement attenuation vs. construct divergence"的两种解释，但标题和 abstract 的措辞将此现象包装为一个全新发现（"Likert Blindspot"），而实质上核心发现更准确地说是：**在 LLM judge 的具体场景下，对 style bias 这一特定效应，Likert 的灵敏度损失从理论预期升级为实践中的严重盲区**。论文的 bootstrap attenuation analysis（Appendix J）确实试图区分这两种解释，但 d = −0.017 的 attenuation 估计是在 n = 355 的 pairwise 数据上做的 subsampling，无法排除 Likert 和 pairwise 在construct 层面的差异。
- 为什么影响接收：如果 reviewer 或 AC 认为论文的 novelty 建立在"发现了一个新现象"上，但该现象实际上是已知测量理论效应在新领域的实例化，则 novelty 评估会显著降低。
- 建议修改方向：(1) 在 Abstract/Intro 中更明确地将 Blindspot 定位为 measurement theory 预测的在 LLM judge 场景下的**首次系统量化**，而非一个全新发现；(2) 在 §5.1 加强对 construct divergence vs. attenuation 的讨论，考虑是否 Likert 和 pairwise 实际测量的是不同构念（absolute quality vs. relative preference）。

**W1** [warning] **NLI filtering 后样本量有限，cross-benchmark 覆盖不完整**
- 具体位置：Table 1, §3.4, §5.3
- 问题：LLMBar 原始 n=100，NLI filtering 后有效样本降至 55-88 对（取决于 axis 和 judge）。Cross-benchmark 验证（AlpacaEval n=50 sampled, MT-Bench 80 pairs）中 Table 1 有多个空白单元格（"—"），说明某些 judge×axis×benchmark 组合未被测试。论文未解释为何缺失这些组合——是因为 NLI pass rate 太低？还是 benchmark 不适用？
- 建议：(1) 补充说明 Table 1 缺失单元格的原因；(2) 如果 NLI pass rate 是瓶颈，报告各 benchmark×axis 的 raw→filtered 样本量变化。

**W2** [warning] **Style axis 之间的 interaction 和 cross-contamination 未被直接测试**
- 具体位置：§3.1, §3.5 assumption (iii), Table 5
- 问题：CSD 的第三个假设是 style rewrite 不引入 target axis 之外的系统性变化。Table 5 的 GEE interaction test（Style × Originality）显示无显著交互，但这只测试了 style 与 originality 的交互，而非 style axis 之间的交互（例如：formal 改写是否系统性地改变了 verbosity？verbose 改写是否改变了 formality？）。Appendix L (Verbosity Sensitivity Hierarchy) 中 register axis 的 attenuation pattern 与 formality/verbosity 不一致（"inconsistent with uniform format amplification"），暗示 cross-axis contamination 的可能。
- 建议：(1) 对每个 axis 的改写样本，测量其他 axis 的变化幅度（例如用 classifier 或 LLM 打分）；(2) 或者至少讨论为什么 axis isolation 的假设在当前设计下是合理的。

**W3** [warning] **负对照（Claude Sonnet 4）仅覆盖 2/3 axes，TOST Δ=15pp margin 偏宽**
- 具体位置：§5.4, Appendix G
- 问题：Claude Sonnet 4 的等价性测试仅覆盖 formality 和 verbosity，未覆盖 register。Δ=15pp 的 equivalence margin 意味着 Claude 可能存在高达 15pp 的 style preference 而仍被判定为"无偏差"——考虑到 GPT-4o formality 的 BT 偏差仅约 13pp，15pp 的 margin 已经与 target judges 的效应量相当接近。论文确认 minimum margin achieving 80% power at n=87 is Δ=15.7pp，说明当前设计对 Δ=15pp 的 TOST 是 underpowered 的。
- 建议：(1) 讨论 Δ=15pp 的实质意义——是否足够"小"以构成有意义的负对照？(2) 增加 Claude 在 register axis 的测试；(3) 或者增加 Claude 的样本量以支持更窄的 equivalence margin。

**W4** [warning] **Evaluator-producer overlap 的处理力度有限**
- 具体位置：§5.3, Tables 7-8, Appendix D
- 问题：Qwen3-32B 同时作为 rewriter 和 judge，存在 evaluator-producer overlap。Cross-rewriter 验证（GPT-4o 作为独立 rewriter）显示 Style OR 下降 22%（verbosity），但 Blindspot 持续存在。然而：(a) cross-rewriter 验证仅限于 Qwen3-32B judge，未覆盖其他 judges；(b) GPT-4o rewriter 产出的 formality BT 64.4% [56.1, 72.8] 的 CI 较宽，置信度有限。
- 建议：明确量化 evaluator-producer overlap 的上界效应（例如：如果所有 judge 都使用独立 rewriter，效应量的预期衰减范围是多少？）。

---

### Questions for Authors

**Q1.** NLI gate 的 false-pass rate 是多少？是否有人工验证数据？即便小规模抽样（e.g., 50 pairs），也能大幅增强 content preservation 声称的可信度。

**Q2.** Table 1 中 cross-benchmark 结果的缺失单元格（"—"）代表什么？是未测试、NLI pass rate 为 0、还是其他原因？

**Q3.** Bootstrap attenuation analysis（Appendix J）的 d = −0.017 如何排除 Likert 和 pairwise 在 construct 层面的根本差异？换言之，如果 Likert 测量的是 absolute quality 而 pairwise 测量的是 relative preference，那么二者对 style 的灵敏度差异可能反映的是 construct 差异而非 measurement deficiency。

**Q4.** Formal 改写是否系统性地改变了文本的 verbosity 或 register？是否有定量证据支持 axis isolation？

**Q5.** 为什么 Claude Sonnet 4 负对照不覆盖 register axis？是否有技术限制？

---

### Missing References

- Preston, C. C., & Colman, A. M. (2000). Optimal number of response categories in rating scales. *Acta Psychologica* — 已引用 ✓
- Thurstone, L. L. (1927) — 已引用 ✓
- Krosnick, J. A. (1999). Survey research. *Annual Review of Psychology* — 已引用 ✓
- 建议补充：Simms, L. J., Zelazny, K., Williams, T. F., & Bernstein, L. (2019). Does the number of response options matter? *Psychological Assessment* — 讨论 rating scale granularity 对 discriminability 的影响，与 Blindspot 现象直接相关。
- 建议补充：Funke, F. (2016). A web experiment showing negative effects of slider scales compared to visual analogue scales and radio button scales. *Social Science Computer Research* — 涉及 response format 对 measurement sensitivity 的影响。

---

### Limitations and Societal Impact

Limitations section（p.8）涵盖了关键局限：quality-style confounding, NLI gate 的边界, validation methodology and scale design。内容简洁覆盖了核心问题。但建议补充：(1) style axis 之间的 potential interaction；(2) 将 measurement theory 背景（ordinal vs. forced-choice sensitivity）作为一个 limitation 显式列出。

Societal影响未单独讨论，但考虑到论文性质（评估方法论研究），这不构成显著遗漏。

---

### Ethical Concerns

无。论文使用公开 benchmark 数据，不涉及人类受试者，匿名合规。

---

### Author Identity Knowledge

未知作者身份。论文 double-blind 合规，标题页标注"Anonymous ACL submission"，正文中未发现身份泄露。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论总体严谨，七种统计方法交叉验证，但 NLI gate 缺乏人工验证是因果链的关键缺口；Likert Blindspot 的 framing 未充分区分 measurement attenuation vs. construct divergence |
| Excitement | 3.5/5 | 研究问题对 NLP evaluation 社区有实际价值，但核心发现部分可归于已知的 measurement theory 效应在新领域的实例化，novelty 略打折扣 |
| Reproducibility | 4/5 | 实验细节充分（prompt template, NLI threshold, seed, bootstrap参数均报告），承诺代码和数据公开发布；但 NLI gate 的具体 prompt 和 style rewriting prompt 的完整模板未在论文中给出（可能在 appendix 但未完整覆盖） |
| Overall Assessment | 3.5 | Borderline Conference — 方法严谨、发现有价值，但 NLI gate 人工验证缺失和 novelty framing 问题需要在 rebuttal 中充分回应 |
| Confidence | 4/5 | 统计方法论和实验设计是我的专业领域，相当确信评估正确 |

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 方法论严谨、统计分析充分的 evaluation 方法论工作，核心发现（Likert 对 style bias 的结构性不敏感）有实际价值，但因果推断链的关键环节（NLI content preservation）缺乏人工验证，且"Blindspot"的 novelty framing 未充分处理与经典 measurement theory 的关系。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 790 · 2026-05-22T09:19:12.509757+00:00_

Reviewer 1 审稿意见已收到。核心发现：

- **Overall 3.5** (Borderline Conference)
- 2 个 critical issue：NLI gate 缺乏人工验证 (N1)、Blindspot framing 相对已知测量理论过于强势 (N2)
- 4 个 warning：样本量/cross-benchmark 不完整 (W1)、cross-axis interaction 未测试 (W2)、负对照 TOST margin 偏宽 (W3)、evaluator-producer overlap 处理有限 (W4)

等待 Reviewer 2 审稿意见返回后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 75

## Round 75

2 recorded events


### User

_source line 791 · 2026-05-22T09:19:15.172366+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交。

**核心判断：Overall 3.5 (Borderline Conference)**

两个 critical 问题：
1. NLI gate 作为 content preservation 唯一门控缺乏人工验证——这是因果推断链最薄弱环节
2. "Likert Blindspot" 的 novelty framing 过于强势，核心发现部分可归于 Thurstone (1927) 以来已知的 ordinal vs. forced-choice 灵敏度差异

四个 warning 问题：样本量有限且 cross-benchmark 覆盖不完整、style axis 交叉污染未直接测试、负对照仅覆盖 2/3 axes 且 TOST margin 偏宽、evaluator-producer overlap 处理力度有限。

主要优势：七种统计方法交叉验证、因果框架诚实定位、Claude 负对照有效、bootstrap attenuation 排除 power 不足解释。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 792 · 2026-05-22T09:19:21.117321+00:00_

Reviewer 1 已返回。等待 Reviewer 2。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 76

## Round 76

6 recorded events


### User

_source line 793 · 2026-05-22T09:20:56.430237+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见 — Round 1 (Fresh Review)

**论文**: "The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 新颖性、完整性、Related Work 覆盖、写作质量

---

## Paper Summary

本文提出 Controlled Style Decomposition (CSD) 框架，用于检测 LLM judge 中被 Likert 评分遗漏但可被 pairwise comparison 捕获的风格偏差（称为 "Likert Blindspot"）。CSD 由三部分组成：NLI-gated content control（确保风格重写不改变内容）、per-axis style decomposition（逐轴分离风格效应）、position-controlled pairwise comparison + Bradley-Terry 建模。实验跨 4 个 target judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、1 个负对照（Claude Sonnet 4）、3 个 benchmark（LLMBar, AlpacaEval, MT-Bench）、2+1 个 style axis（formality, verbosity + register replication）验证。核心发现：(1) Likert 在中等效应量时完全失效（d → 0），在较强效应时衰减 >60%；(2) per-axis confound structure 不同——verbosity 是 style-dominated，formality 是 conditional on originality，register 是 judge-dependent。

## Summary of Strengths

**S1. 实验设计的严谨性与多维度复制。** 4+1 judges × 3 benchmarks × 2+1 style axes 的实验矩阵，加上 7 种统计方法交叉验证（Table 2），在该领域的 empirical 工作中不常见。负对照（Claude Sonnet 4 显示弱/无偏差）增强了因果推断的可信度。

**S2. Sensitivity hierarchy 的干净结果。** Table 2 的全有或全无模式极具说服力：所有 pairwise 方法（BT model, sign test）达到显著性，所有 Likert 方法（ATE t-test, binarized Likert, ordinal regression, GEE, Wilcoxon signed-rank）均不显著。这种一致性比单一统计检验更有说服力。

**S3. Per-axis confound structure 是独立的有价值发现。** Section 5.2 和 Table 3 的 GEE conditional decomposition 揭示 verbosity = style-dominated（Style OR 8.2–13.1, all p < 0.001）、formality = conditional on originality preference、register = judge-dependent。这对 LLM judge 用户有直接 actionable value——对 verbosity 可以做 universal debiasing，对 formality 需要 per-judge conditional analysis。

**S4. Robustness 分析的深度几乎回答了每个合理质疑。** Appendix A–Q 覆盖：方向非对称性（A）、NLI consistency filter（B）、GEE model diagnostics（C）、rewriter independence（D, Tables 7-8）、NLI threshold sensitivity sweep（E, Table 9）、direction-aware gate validation（F）、Claude Sonnet 4 equivalence testing（G）、bootstrap attenuation（H）、BT goodness-of-fit（I）、verbosity sensitivity hierarchy（L）、100-point continuous Likert（M）、NLI gate ablation（N）、rewriting artifact control（O）。这种系统性的 robustness checking 值得肯定。

**S5. Black-box 框架设计。** CSD 不需要 judge 内部访问权限（no access to judge internals），可 post-hoc 应用于任何 black-box judge，实用性强。

**S6. Figure 3 和 Figure 4 的可视化效果好。** Figure 3 的 Bradley-Terry win probability plot 清晰地展示了跨 judge-axis 的 Blindspot 模式；Figure 4 的 detection probability vs. effect magnitude 曲线直观地说明了 Likert 和 pairwise 在不同效应量下的灵敏度差异。

## Summary of Weaknesses

**N1** [critical] **新颖性定位：核心发现是"实证确认"而非"新发现"**

- 具体位置：Abstract（"We ... reveal the Likert Blindspot"）、Section 1 第2段、Section 2 最后一段、Section 5.1 标题（"The Likert Blindspot"）
- 问题：论文将 Likert Blindspot 包装为一个新发现。但 Thurstone (1927) 的 Law of Comparative Judgment 和后续测量理论研究（Preston & Colman, 2000；Krosnick, 1999——论文自己引用的；Louviere et al., 2015——论文也引用的）早已建立了 pairwise comparison 相对于 rating scale 的敏感性优势。论文在 Section 2（第2页）也明确承认："the superiority of pairwise comparison over rating scales for eliciting reliable human judgments has been established since Thurstone (1927)." 紧接着又声称 "Our contribution is the first controlled, per-axis quantification of this sensitivity gap for LLM judge style bias"（第3页）。

  问题不在于贡献不存在，而在于叙事框架。当论文用 "reveal" 和 "Blindspot" 这类带有发现色彩的词汇时，暗示这是一个意外的新发现（unexpected finding）。但考虑到 measurement theory 的预测，更准确的定位是：**设计了一个框架（CSD）来在 LLM judge 场景下系统性地量化一个理论预测的测量敏感性差距，并在此过程中发现了 per-axis confound structure。** 后者（per-axis confound structure）才是真正没有被先验理论预测的 novel finding。

- 为什么影响接收：ARR reviewer guidelines 明确说，如果 reviewer 认为 novelty 不足，必须提供具体 prior art。这里 Thurstone (1927)、Preston & Colman (2000) 就是直接的 prior art。当前 framing 让有测量理论背景的 reviewer 容易 dismiss 整篇论文，即使 empirical 贡献本身有价值。
- 建议修改方向：
  (1) 重新定位 narrative：从"我们发现了 Likert Blindspot"转向"我们设计 CSD 框架首次在 LLM judge 风格偏差中量化了这个理论预测的敏感性差距，量化结果显示其严重性超出预期（complete attenuation at moderate effects），且发现了 per-axis confound structure 这一新模式"。
  (2) 将 per-axis confound structure 提升为与 Blindspot quantification 平行的核心贡献。
  (3) Abstract 第一句可改为承认理论预测，第二句说明本文的 empirical contribution。

**N2** [critical] **Pairwise "检测" vs. Pairwise "放大"：核心解释性歧义未充分解决**

- 具体位置：Section 5.4（第6–7页）、Section 6 (Conclusion)、Limitations
- 问题：论文的核心叙事假设 pairwise comparison 检测到了真实的风格偏差，而 Likert 遗漏了它。但存在一个对等的替代解释：**pairwise comparison 放大了微小的、实际上无关紧要的风格微偏好**，使其达到统计显著性，而 Likert 的"不显著"才反映了真实的效应大小。

  论文在 Section 5.4 引用了 Jeong et al. (2025) 的 Comparative Trap（pairwise comparison amplifies style biases relative to positive-scoring），并在第6页讨论了 "measurement attenuation vs. construct divergence"。但论文的论证有循环性问题：

  (a) 论文说 "Likert audits miss style preferences that drive pairwise-based alignment pipelines (RLHF, DPO)"（第6页），用这一点来论证 pairwise 检测到的是"真实"偏差。但这个论证预设了 RLHF/DPO pipeline 中的 pairwise preference 反映了真实偏差——而这恰恰是需要证明的。
  (b) Bootstrap attenuation analysis (Appendix H) 排除了"纯粹是统计功效差异"的解释，但不能排除 "pairwise 系统性放大微小偏好" 的可能——BT 在小样本时仍显著，可能恰恰是因为 pairwise 的放大效应。
  (c) 第6页的 "Both interpretations lead to the same conclusion" 论证也不完全成立——如果 pairwise 是在放大噪声，那么用 pairwise 来"审计" judges 就可能产生大量 false positives。

- 为什么影响接收：这个解释性歧义直接影响论文发现的实际意义。如果读者接受"放大"解释，论文的 practical implication（"用 pairwise 来审计 LLM judge 风格偏差"）就可能被认为是误导性的。
- 建议修改方向：
  (1) 最理想的方案：增加一个基于 human ground-truth 的验证——对 style-manipulated pairs 收集人类偏好判断，比较 pairwise 和 Likert 哪个更接近人类判断。即使是小规模验证也能大幅增强论文的说服力。
  (2) 次优方案：在 Section 5.4 或 Discussion 中更 prominently 地承认这个限制，明确说明当前证据无法区分两种解释，并讨论在什么条件下每种解释的 implication 是什么。避免在 Conclusion 中使用 "reveal" 等暗示单一解释的语言。

**W1** [warning] **Style axis 覆盖面过窄，confound structure claim 的泛化基础不足**

- 具体位置：Section 3.1、Section 4、Section 5.2
- 问题：论文仅测试 2 个 primary axes (formality, verbosity) + 1 个 replication (register)。LLM judge 的已知风格偏差远不止这些（例如 bullet-point vs. prose、hedging/confidence level、response length distribution 的 long-tail 效应等）。基于 3 个 axis 声称发现了 "per-axis confound structure"，这种分类法（style-dominated / conditional / judge-dependent）的泛化性缺乏支撑——读者无法判断新的 style axis 会属于哪种类型。
- 建议：(1) 在正文明确限定 confound structure claim 的适用范围（"for the three axes we tested"）；(2) 在 Limitations 中讨论 axis 覆盖的局限性；(3) 简要说明 axis 选择的先验理由（如 pilot study 或文献依据）。

**W2** [warning] **NLI gate 高拒绝率（~44%）的选择偏差分析不足**

- 具体位置：Section 3.2、Appendix B
- 问题：NLI consistency filter 保留 55/98 pairs (56.1%)。Appendix B 报告 "no significant differences across four covariates (NLI score p = 0.824, BERTS p = 0.12, text length p = 0.137, length diff p = 0.715)"，但这 4 个 covariates 可能不够全面。通过 NLI gate 的 pairs 可能系统性地偏向内容更简单、风格变化更容易分离的文本。这意味着 Blindspot 的效应量 estimate 可能在更复杂的文本上不可靠。
- 建议：(1) 分析被拒绝 pairs 的文本特征（例如原始 style 距离、话题复杂度、指令类型）vs. 保留 pairs；(2) 讨论 selection bias 对 external validity 的影响。

**W3** [warning] **100-point continuous Likert 实验仅用单一 judge**

- 具体位置：Appendix M（第12页）
- 问题：此实验旨在排除"Blindspot 是整数刻度粒度的人为产物"这一替代解释，但仅使用 Qwen3-32B 一个 judge。如果 GPT-4o 或其他 judge 在 100-point scale 下表现不同（例如 fine-grained scale 确实能检测到偏差），则该结论不成立。
- 建议：至少在一个额外 judge 上复制此实验，或明确标注为 preliminary evidence。

**W4** [warning] **因果语言与实际方法论之间的张力**

- 具体位置：Title ("Controlled Style Decomposition")、Section 3 开头、Figure 2
- 问题：论文在 Section 4（第4页）给出了合理的 disclaimer ("we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions")，这值得肯定。但标题中的 "Controlled" 和方法描述中的 "interventional" 语言仍然暗示了比实际更强的因果识别——NLI gating 是一种近似的内容控制（approximate content preservation），而非因果推断文献中的 do-operator。Figure 2 的 DAG notation 也可能让有因果推断背景的读者期望看到正式的 identification strategy。
- 建议：在 Method 开头更早地明确说明这是 "approximately controlled comparison" 而非 "causally identified effect"，以管理读者预期。

## Questions for Authors

Q1. 关于 N2（检测 vs. 放大）：是否有计划收集 human preference 判断来 ground-truth pairwise 检测到的风格偏差？即使是一个小规模的 pilot（例如 50 pairs × 3 annotators）也能大幅增强论文的说服力。

Q2. 关于 W1（style axes）：选择 formality 和 verbosity 作为 primary axes 的先验理由是什么？是否有 pilot study 表明这两个 axis 的效应最大？如果选择了不同的 axes（例如 bullet-point usage, hedging level），Blindspot 是否仍然存在？

Q3. 关于 Appendix D（rewriter independence）：GPT-4o 作为替代 rewriter 时（Table 7），verbosity 的 Style OR 从 Qwen3-32B rewriter 的高值下降了 22%。这种下降是否暗示 Blindspot 的效应量部分依赖于 rewriter 的具体风格？如果使用完全不同的 rewriting 方法（例如 rule-based rewriting），结果会如何变化？

Q4. 关于 Section 5.4（Comparative Trap）：论文引用了 6 个 experimental controls 来 bound the risk of amplification（NLI gate ablation、Claude Sonnet 4 equivalence、TOST equivalence at Δ = 13pp 等）。但这些 controls 只能排除"大规模放大"，无法排除"中等程度放大"。是否有办法量化 pairwise 的放大倍数（amplification factor），而不仅仅是定性地论证？

## Missing References

1. **Item Response Theory (IRT) 在 LLM/NLP 评估中的应用**：论文讨论了 Likert vs. pairwise 的测量属性，但没有引用 IRT 文献。Polo et al. (2024, "tinyBenchmarks: evaluating LLMs with fewer examples") 和 Otani et al. (2023) 从测量理论角度分析 LLM 评估的可靠性和效度，与本文的 measurement sensitivity 主题直接相关。
2. **Kocmi and Federmann (2023)** "Large Language Models Are Not Fair Multilingual Evaluators" — 虽然聚焦 MT 评估，但其关于 LLM judge bias 在不同评估格式下的表现差异与本文主题相关。
3. 建议验证 Stureborg et al. (2024) 是否在参考文献列表中完整列出（正文有引用但 references 部分需确认）。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由 |
|------|------|------|
| **Soundness** | 4/5 (Strong) | 实验设计严谨，多维度复制和 7 种统计方法交叉验证是 strong evidence。扣分原因：NLI gate ~44% rejection rate 的 selection bias 未充分分析；核心解释性歧义（检测 vs. 放大）未解决 |
| **Excitement** | 3/5 (Interesting) | 对 LLM 评估社区有实用价值，per-axis confound structure 有新意。核心 Blindspot 发现主要是已有测量理论的实证确认，降低了 excitement |
| **Reproducibility** | 4/5 (Mostly reproducible) | 方法描述清晰，超参数完整（Appendix P），承诺释放代码和数据。NLI gate 的具体 threshold tuning 和 style rewriting 的 prompt templates 可能影响 exact reproduction |
| **Overall Assessment** | **3.5** (Borderline Conference) | 实验工作扎实，结果清晰，对社区有实用价值。但核心发现的新颖性受限于已有测量理论预测，且"检测 vs. 放大"的核心解释性歧义未充分解决。如果 reframe novelty narrative 并增加 human ground-truth validation，可以更有信心地推荐 Conference |
| **Confidence** | 4/5 (Quite sure) | 熟悉 LLM-as-judge evaluation、measurement theory 和 causal NLP 文献。可能遗漏的点：对 GEE 模型选择的技术细节不够深入 |

## 主要优势（总结）

1. 实验设计的多维度复制（4+1 judges × 3 benchmarks × 2+1 axes × 7 statistical methods）在该领域罕见
2. Table 2 的 sensitivity hierarchy 是一个极其干净的 all-or-nothing 结果
3. Per-axis confound structure（S5.2, Table 3）是独立的有价值发现
4. Robustness 分析（Appendix A–Q）几乎回答了每个合理质疑
5. Black-box 框架设计有强 practical applicability
6. 写作整体清晰，Figure 3/4 有效传达核心信息


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-22T09:21:45.827223+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应每个 Weakness 和 Question：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Weaknesses\n\n**N1** [critical] **NLI gate 作为 content preservation 的唯一门控缺乏人工验证**\n- CSD 的因果推断完全依赖 NLI gate（DeBERTa-v3-large, threshold 0.90）保证 content 不变。然而 NLI 模型本身可能存在系统性盲区——例如对隐含推理链的改变、对论证结构重组的不敏感。论文未报告对 NLI-gated pairs 的任何人工抽样验证（human evaluation of content preservation quality）。Limitations 中承认\"cannot block quality perception shifts mediated by style itself\"，但这一局限的严重性需要实证数据来界定——至少应抽样 50-100 对，让人工标注者判断 content 是否实质等价。\n- 为什么影响接收：这是 CSD 因果推断链条的最薄弱环节。如果 NLI gate 系统性地放过了某些 content 变化（例如 formal 改写倾向于增加 hedging 从而实质改变 claim 强度），则观测到的\"style bias\"可能部分是 content bias 的伪装。\n\n**N2** [critical] **\"Likert Blindspot\" 的 framing 过于强势，忽视了 ordinal vs. forced-choice 灵敏度差异的已知理论背景**\n- Likert（绝对评分）与 pairwise comparison（强制选择）的灵敏度差异是测量理论中的经典结论——Thurstone (1927) 已经指出 forced-choice 比 absolute rating 更能识别微小差异。论文在 §2 确实引用了这些文献，也在 §5.1 讨论了\"measurement attenuation vs. construct divergence\"的两种解释，但标题和 abstract 的措辞将此现象包装为一个全新发现。\n- 建议：在 Abstract/Intro 中更明确地将 Blindspot 定位为 measurement theory 预测的在 LLM judge 场景下的首次系统量化，而非全新发现。\n\n**W1** [warning] **NLI filtering 后样本量有限，cross-benchmark 覆盖不完整**\n- LLMBar 原始 n=100，NLI filtering 后有效样本降至 55-88 对。Cross-benchmark 验证（AlpacaEval, MT-Bench）中 Table 1 有多个空白单元格。论文未解释为何缺失这些组合。\n\n**W2** [warning] **Style axis 之间的 interaction 和 cross-contamination 未被直接测试**\n- CSD 的第三个假设是 style rewrite 不引入 target axis 之外的系统性变化。Table 5 的 GEE interaction test（Style × Originality）只测试了 style 与 originality 的交互，而非 style axis 之间的交互。\n\n**W3** [warning] **负对照（Claude Sonnet 4）仅覆盖 2/3 axes，TOST Δ=15pp margin 偏宽**\n- Δ=15pp 的 equivalence margin 意味着 Claude 可能存在高达 15pp 的 style preference 而仍被判定为\"无偏差\"——考虑到 GPT-4o formality 的 BT 偏差仅约 13pp。\n\n**W4** [warning] **Evaluator-producer overlap 的处理力度有限**\n- Cross-rewriter 验证仅限于 Qwen3-32B judge，未覆盖其他 judges。\n\n---\n\n## Reviewer 1 的 Questions\n\n**Q1.** NLI gate 的 false-pass rate 是多少？是否有人工验证数据？\n\n**Q2.** Table 1 中 cross-benchmark 结果的缺失单元格代表什么？\n\n**Q3.** Bootstrap attenuation analysis（Appendix J）的 d = −0.017 如何排除 Likert 和 pairwise 在 construct 层面的根本差异？\n\n**Q4.** Formal 改写是否系统性地改变了文本的 verbosity 或 register？是否有定量证据支持 axis isolation？\n\n**Q5.** 为什么 Claude Sonnet 4 负对照不覆盖 register axis？\n\n---\n\n请对以上每一条 Weakness（N1, N2, W1-W4）和 Question（Q1-Q5）逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应每个 Weakness 和 Question：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Weaknesses\n\n**N1** [critical] **NLI gate 作为 content preservation 的唯一门控缺乏人工验证**\n- CSD 的因果推断完全依赖 NLI gate（DeBERTa-v3-large, threshold 0.90）保证 content 不变。然而 NLI 模型本身可能存在系统性盲区——例如对隐含推理链的改变、对论证结构重组的不敏感。论文未报告对 NLI-gated pairs 的任何人工抽样验证（human evaluation of content preservation quality）。Limitations 中承认\"cannot block quality perception shifts mediated by style itself\"，但这一局限的严重性需要实证数据来界定——至少应抽样 50-100 对，让人工标注者判断 content 是否实质等价。\n- 为什么影响接收：这是 CSD 因果推断链条的最薄弱环节。如果 NLI gate 系统性地放过了某些 content 变化（例如 formal 改写倾向于增加 hedging 从而实质改变 claim 强度），则观测到的\"style bias\"可能部分是 content bias 的伪装。\n\n**N2** [critical] **\"Likert Blindspot\" 的 framing 过于强势，忽视了 ordinal vs. forced-choice 灵敏度差异的已知理论背景**\n- Likert（绝对评分）与 pairwise comparison（强制选择）的灵敏度差异是测量理论中的经典结论——Thurstone (1927) 已经指出 forced-choice 比 absolute rating 更能识别微小差异。论文在 §2 确实引用了这些文献，也在 §5.1 讨论了\"measurement attenuation vs. construct divergence\"的两种解释，但标题和 abstract 的措辞将此现象包装为一个全新发现。\n- 建议：在 Abstract/Intro 中更明确地将 Blindspot 定位为 measurement theory 预测的在 LLM judge 场景下的首次系统量化，而非全新发现。\n\n**W1** [warning] **NLI filtering 后样本量有限，cross-benchmark 覆盖不完整**\n- LLMBar 原始 n=100，NLI filtering 后有效样本降至 55-88 对。Cross-benchmark 验证（AlpacaEval, MT-Bench）中 Table 1 有多个空白单元格。论文未解释为何缺失这些组合。\n\n**W2** [warning] **Style axis 之间的 interaction 和 cross-contamination 未被直接测试**\n- CSD 的第三个假设是 style rewrite 不引入 target axis 之外的系统性变化。Table 5 的 GEE interaction test（Style × Originality）只测试了 style 与 originality 的交互，而非 style axis 之间的交互。\n\n**W3** [warning] **负对照（Claude Sonnet 4）仅覆盖 2/3 axes，TOST Δ=15pp margin 偏宽**\n- Δ=15pp 的 equivalence margin 意味着 Claude 可能存在高达 15pp 的 style preference 而仍被判定为\"无偏差\"——考虑到 GPT-4o formality 的 BT 偏差仅约 13pp。\n\n**W4** [warning] **Evaluator-producer overlap 的处理力度有限**\n- Cross-rewriter 验证仅限于 Qwen3-32B judge，未覆盖其他 judges。\n\n---\n\n## Reviewer 1 的 Questions\n\n**Q1.** NLI gate 的 false-pass rate 是多少？是否有人工验证数据？\n\n**Q2.** Table 1 中 cross-benchmark 结果的缺失单元格代表什么？\n\n**Q3.** Bootstrap attenuation analysis（Appendix J）的 d = −0.017 如何排除 Likert 和 pairwise 在 construct 层面的根本差异？\n\n**Q4.** Formal 改写是否系统性地改变了文本的 verbosity 或 register？是否有定量证据支持 axis isolation？\n\n**Q5.** 为什么 Claude Sonnet 4 负对照不覆盖 register axis？\n\n---\n\n请对以上每一条 Weakness（N1, N2, W1-W4）和 Question（Q1-Q5）逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-22T09:22:07.892009+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22064
}
```

</details>

---


### Tool call

_source line 796 · 2026-05-22T09:22:08.093222+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应每个 Weakness 和 Question：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Weaknesses\n\n**N1** [critical] **新颖性定位：核心发现是\"实证确认\"而非\"新发现\"**\n- 论文将 Likert Blindspot 包装为一个新发现（\"reveal\"），但 Thurstone (1927) 以来的测量理论已建立了 pairwise 相对于 rating scale 的敏感性优势。更准确的定位是：设计了一个框架（CSD）来在 LLM judge 场景下系统性地量化一个理论预测的测量敏感性差距，并在此过程中发现了 per-axis confound structure。\n- 建议：从\"我们发现了 Likert Blindspot\"转向\"我们设计 CSD 框架首次量化了这个理论预测的敏感性差距\"，将 per-axis confound structure 提升为与 Blindspot quantification 平行的核心贡献。\n\n**N2** [critical] **Pairwise \"检测\" vs. Pairwise \"放大\"：核心解释性歧义未充分解决**\n- 论文的核心叙事假设 pairwise comparison 检测到了真实的风格偏差，而 Likert 遗漏了它。但替代解释是：pairwise comparison 放大了微小的、无关紧要的风格微偏好。论文在 §5.4 讨论了 6 个 experimental controls 来 bound this risk，但论证存在循环性：\n  (a) 用 RLHF/DPO pipeline 的 pairwise preference 来论证 pairwise 检测到的是\"真实\"偏差——但这预设了 RLHF/DPO 的偏好反映真实偏差。\n  (b) Bootstrap attenuation 排除了\"纯粹是统计功效差异\"，但不能排除 pairwise 系统性放大微小偏好。\n  (c) \"Both interpretations lead to the same conclusion\" 不完全成立——如果 pairwise 放大噪声，用 pairwise 审计就会产生 false positives。\n- 最理想方案：增加 human ground-truth 验证；次优方案：更 prominently 承认限制，避免 Conclusion 中使用 \"reveal\" 等暗示单一解释的语言。\n\n**W1** [warning] **Style axis 覆盖面过窄，confound structure claim 的泛化基础不足**\n- 仅 2 primary + 1 replication axes。LLM judge 的已知风格偏差远不止这些（bullet-point vs. prose、hedging level 等）。基于 3 个 axis 声称发现\"per-axis confound structure\"，分类法的泛化性缺乏支撑。\n\n**W2** [warning] **NLI gate 高拒绝率（~44%）的选择偏差分析不足**\n- NLI consistency filter 保留 55/98 pairs (56.1%)。Appendix B 报告 4 个 covariates 无显著差异，但可能不够全面。通过 NLI gate 的 pairs 可能系统性偏向内容更简单、风格变化更容易分离的文本。\n\n**W3** [warning] **100-point continuous Likert 实验仅用单一 judge**\n- Appendix M 旨在排除\"Blindspot 是整数刻度粒度的人为产物\"，但仅使用 Qwen3-32B。如果其他 judge 在 100-point scale 下表现不同，则该结论不成立。\n\n**W4** [warning] **因果语言与实际方法论之间的张力**\n- 标题中的 \"Controlled\" 和方法描述中的 \"interventional\" 语言暗示了比实际更强的因果识别。NLI gating 是近似的内容控制，而非 do-operator。Figure 2 的 DAG notation 也可能让因果推断背景的读者期望更严格的 identification strategy。\n\n---\n\n## Reviewer 2 的 Questions\n\n**Q1.** 关于 N2（检测 vs. 放大）：是否有计划收集 human preference 判断来 ground-truth pairwise 检测到的风格偏差？\n\n**Q2.** 关于 W1（style axes）：选择 formality 和 verbosity 作为 primary axes 的先验理由是什么？\n\n**Q3.** 关于 Appendix D（rewriter independence）：GPT-4o 作为替代 rewriter 时，Style OR 下降 22%。这种下降是否暗示 Blindspot 的效应量部分依赖于 rewriter 的具体风格？\n\n**Q4.** 关于 Section 5.4（Comparative Trap）：6 个 controls 只能排除\"大规模放大\"，无法排除\"中等程度放大\"。是否有办法量化 pairwise 的放大倍数？\n\n---\n\n请对以上每一条 Weakness（N1, N2, W1-W4）和 Question（Q1-Q4）逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应每个 Weakness 和 Question：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Weaknesses\n\n**N1** [critical] **新颖性定位：核心发现是\"实证确认\"而非\"新发现\"**\n- 论文将 Likert Blindspot 包装为一个新发现（\"reveal\"），但 Thurstone (1927) 以来的测量理论已建立了 pairwise 相对于 rating scale 的敏感性优势。更准确的定位是：设计了一个框架（CSD）来在 LLM judge 场景下系统性地量化一个理论预测的测量敏感性差距，并在此过程中发现了 per-axis confound structure。\n- 建议：从\"我们发现了 Likert Blindspot\"转向\"我们设计 CSD 框架首次量化了这个理论预测的敏感性差距\"，将 per-axis confound structure 提升为与 Blindspot quantification 平行的核心贡献。\n\n**N2** [critical] **Pairwise \"检测\" vs. Pairwise \"放大\"：核心解释性歧义未充分解决**\n- 论文的核心叙事假设 pairwise comparison 检测到了真实的风格偏差，而 Likert 遗漏了它。但替代解释是：pairwise comparison 放大了微小的、无关紧要的风格微偏好。论文在 §5.4 讨论了 6 个 experimental controls 来 bound this risk，但论证存在循环性：\n  (a) 用 RLHF/DPO pipeline 的 pairwise preference 来论证 pairwise 检测到的是\"真实\"偏差——但这预设了 RLHF/DPO 的偏好反映真实偏差。\n  (b) Bootstrap attenuation 排除了\"纯粹是统计功效差异\"，但不能排除 pairwise 系统性放大微小偏好。\n  (c) \"Both interpretations lead to the same conclusion\" 不完全成立——如果 pairwise 放大噪声，用 pairwise 审计就会产生 false positives。\n- 最理想方案：增加 human ground-truth 验证；次优方案：更 prominently 承认限制，避免 Conclusion 中使用 \"reveal\" 等暗示单一解释的语言。\n\n**W1** [warning] **Style axis 覆盖面过窄，confound structure claim 的泛化基础不足**\n- 仅 2 primary + 1 replication axes。LLM judge 的已知风格偏差远不止这些（bullet-point vs. prose、hedging level 等）。基于 3 个 axis 声称发现\"per-axis confound structure\"，分类法的泛化性缺乏支撑。\n\n**W2** [warning] **NLI gate 高拒绝率（~44%）的选择偏差分析不足**\n- NLI consistency filter 保留 55/98 pairs (56.1%)。Appendix B 报告 4 个 covariates 无显著差异，但可能不够全面。通过 NLI gate 的 pairs 可能系统性偏向内容更简单、风格变化更容易分离的文本。\n\n**W3** [warning] **100-point continuous Likert 实验仅用单一 judge**\n- Appendix M 旨在排除\"Blindspot 是整数刻度粒度的人为产物\"，但仅使用 Qwen3-32B。如果其他 judge 在 100-point scale 下表现不同，则该结论不成立。\n\n**W4** [warning] **因果语言与实际方法论之间的张力**\n- 标题中的 \"Controlled\" 和方法描述中的 \"interventional\" 语言暗示了比实际更强的因果识别。NLI gating 是近似的内容控制，而非 do-operator。Figure 2 的 DAG notation 也可能让因果推断背景的读者期望更严格的 identification strategy。\n\n---\n\n## Reviewer 2 的 Questions\n\n**Q1.** 关于 N2（检测 vs. 放大）：是否有计划收集 human preference 判断来 ground-truth pairwise 检测到的风格偏差？\n\n**Q2.** 关于 W1（style axes）：选择 formality 和 verbosity 作为 primary axes 的先验理由是什么？\n\n**Q3.** 关于 Appendix D（rewriter independence）：GPT-4o 作为替代 rewriter 时，Style OR 下降 22%。这种下降是否暗示 Blindspot 的效应量部分依赖于 rewriter 的具体风格？\n\n**Q4.** 关于 Section 5.4（Comparative Trap）：6 个 controls 只能排除\"大规模放大\"，无法排除\"中等程度放大\"。是否有办法量化 pairwise 的放大倍数？\n\n---\n\n请对以上每一条 Weakness（N1, N2, W1-W4）和 Question（Q1-Q4）逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-22T09:22:09.659614+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1566
}
```

</details>

---


### Assistant

_source line 798 · 2026-05-22T09:22:12.395594+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 77

## Round 77

2 recorded events


### User

_source line 799 · 2026-05-22T09:22:15.232191+00:00_

[Reviewer 2 审稿结果]:
审稿完成，已提交给 Review Director。

**总结**：Overall 3.5 (Borderline Conference)。两个 critical 问题：(1) 核心 "Likert Blindspot" 发现的新颖性被测量理论（Thurstone 1927）预测，framing 需要从"发现"调整为"首次系统性实证量化 + per-axis confound structure 的新发现"；(2) pairwise "检测真实偏差" vs. "放大微小偏好" 的核心解释性歧义未充分解决，缺乏 human ground-truth validation。四个 should-fix：style axis 覆盖过窄（仅 2+1）、NLI gate 高拒绝率的选择偏差分析不足、100-point Likert 实验仅用单一 judge、因果语言略强于实际方法论。实验设计的严谨性（7 种统计方法 × 4+1 judges × 3 benchmarks）和 per-axis confound structure 是主要优势。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 800 · 2026-05-22T09:22:19.671594+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 78

## Round 78

2 recorded events


### User

_source line 801 · 2026-05-22T09:24:22.164114+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Weaknesses 回应

**[AGREE] R2-N1: 新颖性定位：核心发现是"实证确认"而非"新发现"**

同意，且与我自己的 N2 高度一致。论文的核心贡献更准确地说是：(1) 设计了 CSD 框架首次在 LLM judge 场景下系统量化了经典测量理论预测的 Likert/pairwise 灵敏度差距；(2) 发现了 per-axis confound structure（formality 是 style-dominated，register 是 judge-dependent）。将 Thurstone (1927) 以来已知的理论效应包装为"reveal"确实夸大了 novelty。论文在 §5.1 引用了 Thurstone 和 Preston & Colman (2000) 并讨论了 measurement attenuation vs. construct divergence，说明作者**意识到**这一理论背景，但 framing 选择（Title/Abstract/Conclusion 中的 "reveal"）未能准确反映这一关系。建议作者采纳 R2 的重新定位方案——将 CSD 框架设计和 per-axis confound structure 提升为并列核心贡献，"Blindspot quantification" 作为 empirical result 而非 discovery。

---

**[REBUT] R2-N2: Pairwise "检测" vs. Pairwise "放大"——部分反驳**

R2 提出了一个合理的认识论问题，但我认为其论证力度被高估了，原因如下：

(1) **负对照是反驳"放大"解释的最强证据。** Claude Sonnet 4 在相同的 pairwise comparison 设计下 BT ≈ 54-56%（§5.4, Appendix G），TOST 确认等价。如果 pairwise 的灵敏度本身系统性地放大了微小偏好，那么**所有 judge 都应表现出放大效应**，包括 Claude。Claude 的阴性结果证明 pairwise 检测到的是 judge-specific 的偏差，而非 format-induced 的普遍放大。R2 的 critique 未直接回应这一反驳。

(2) **R2 对循环论证的指控部分成立但非致命。** R2 指出"用 RLHF/DPO pipeline 的 pairwise preference 来论证 pairwise 检测到的是真实偏差"存在循环性。我同意这在**本体论**层面是循环的（什么是"真实"偏差？），但在**操作层面**不循环：如果真实 alignment pipeline（RLHF/DPO）确实使用 pairwise comparison 格式，那么 pairwise 检测到的偏差就是**操作上相关的**偏差，无论它们在哲学层面是否"真实"。论文在 §5.4 也明确提到了 Comparative Trap（Jeong et al., 2025），说明作者意识到 pairwise 可能放大偏好。

(3) **但我同意 R2 的一个核心关切：论文的 Conclusion 语言应更谨慎。** "reveal" 和 "systematically misses" 暗示了单一解释。更诚实的 framing 是："pairwise comparison detects style-correlated judge preferences that Likert scoring does not; whether these preferences represent genuine bias or format-amplified micro-preferences remains an open question with practical implications for both interpretations."

(4) **关于 R2 的 "both interpretations" 批评：** R2 说 "Both interpretations lead to the same conclusion 不完全成立——如果 pairwise 放大噪声，用 pairwise 审计就会产生 false positives"。这一点在逻辑上是对的。但论文的论证不需要排除**所有**放大——它需要表明放大的上界是有限的。Cross-rewriter validation（Tables 7-8）中 Style OR 下降 22% 可被视为对 rewriter-specific amplification 的上界估计。

**综合判断：** N2 提出的解释性歧义是真实存在的，但论文已通过负对照、cross-rewriter validation 和 Comparative Trap 讨论提供了充分的缓解。将其定为 critical 偏严——should-fix (warning) 更合适，主要修改是 Conclusion 语言的谨慎化。

---

**[AGREE] R2-W1: Style axis 覆盖面过窄**

同意方向，但不同意严重程度。3 个 axis（2 primary + 1 exploratory）对于一篇**方法论论文**而言是合理的——CSD 框架的价值在于其通用性（可应用于任意 axis），而非穷举所有可能的偏差。论文在 Conclusion（p.8）也明确建议"additional axes, larger benchmarks, and further judges are needed"。但 R2 的核心关切——"per-axis confound structure" 这一 claim 基于仅 3 个 axis 的泛化基础不足——是合理的。建议作者将 "per-axis confound structure" 降级为 "preliminary evidence of axis-dependent confound patterns"，或增加 1-2 个 axis 的数据来加强泛化论证。

---

**[AGREE] R2-W2: NLI gate 高拒绝率的选择偏差分析不足**

同意，且与我的 N1 相关联。44% 的拒绝率意味着分析结果只代表 NLI-filterable 的子集，而非全部文本。Appendix B 的 4 个 covariates（BERT score, text length, length difference, NLI score）检查了表面特征，但未检查更深层的特征——例如 filtered-in pairs 是否系统性偏向论证结构更简单（因此内容更容易保持不变）的文本。如果更复杂的文本在 rewriting 时更容易产生 content 变化从而被 NLI gate 拒绝，则保留的样本可能低估了 style bias 在复杂文本上的表现，或高估了 NLI gate 的有效性。建议补充对 filtered-in vs. filtered-out pairs 的语言复杂度（syntactic complexity, argument depth）对比分析。

---

**[AGREE] R2-W3: 100-point continuous Likert 仅用单一 judge**

同意。Appendix M 的 100-point Likert 实验仅使用 Qwen3-32B，这限制了"Blindspot 不是刻度粒度的产物"这一结论的泛化性。如果 GPT-4o 或 Llama-3.3-70B 在 100-point scale 下 ATE 变为显著，则 Blindspot 对某些 judge 可能**确实**是粒度问题而非结构性问题。虽然补充所有 judge 的 100-point 实验可能成本较高，但至少应增加 1 个 judge（例如 GPT-4o，因为它是最常用的 benchmark judge）来增强结论的可信度。

---

**[REBUT] R2-W4: 因果语言与实际方法论的张力——部分反驳**

R2 认为 "Controlled" 和 "interventional" 语言暗示了过强的因果识别。我认为论文在 §3.5 已经做了充分的对冲：

- "This DAG is a design rationale, not a claim of perfect identification"（§3.5, p.4）
- "nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework"（§3.5, p.4）
- "Our identification rests on three operational assumptions"（§3.5, p.4）

这些表述明确将因果 claim 降级为 "operational assumptions" 而非 formal identification。Figure 2 的 DAG 标注了 "Assumed data-generating process (design rationale, not a claim of perfect identification)"。

但我同意 **Title 和 Abstract** 的语言（"Controlled Style Decomposition"）与 §3.5 的谨慎对冲之间存在张力。标题中的 "Controlled" 容易让因果推断背景的读者期望 do-calculus 层面的识别。建议：在 Abstract 中增加一句明确说明 "controlled" 指的是 "experimentally controlled rewriting" 而非 formal causal identification。

**严重程度：** Warning 而非 critical。§3.5 的 disclaimer 足够明确，问题主要在 Title/Abstract 的措辞选择而非方法论本身。

---

### Questions 回应

**[AGREE] R2-Q1: Human preference ground-truth**

同意这是最理想的验证方案。与我的 N1 一致——NLI gate 作为 content preservation 的唯一门控，缺乏任何 human validation。收集 human preference 判断（例如让人类标注者对 NLI-gated pairs 进行 pairwise comparison，看人类是否也检测到 style bias）能同时验证两个假设：(a) NLI gate 确实保持了 content；(b) pairwise 检测到的偏差对人类也可观测。这将大幅增强论文的说服力。

---

**[REBUT] R2-Q2: Primary axes 的先验理由**

R2 质疑 formality 和 verbosity 的选择缺乏先验理由。我认为论文在 §2（Related Work）已提供了充分的文献支撑：

- Verbosity bias 是 LLM judge 文献中最 well-documented 的偏差（Zheng et al., 2023; Park et al., 2024; Dubois et al., 2025 均有报告）
- Formality 与 RLHF preference 的关联在 Reber et al. (2025) 和 Shi et al. (2025) 中被讨论
- 这两个 axis 有明确的可操作性（可通过 instruction 控制 rewriting），且与实际 deployment 场景直接相关

选择 well-studied 的 axis 作为 primary 恰恰是正确的方法论策略——先在已知存在偏差的 axis 上验证框架的有效性，再扩展到探索性 axis（register）。这不是 weakness，而是合理的研究设计。

---

**[AGREE] R2-Q3: Style OR 下降 22% 的含义**

同意这一观察的重要性。Tables 7-8 显示 GPT-4o 作为替代 rewriter 时 verbosity 的 Style OR 从~14 降至~10（约 22%），说明效应量确实部分依赖于 rewriter 身份。这意味着：(a) Blindspot 现象本身是 robust 的（跨 rewriter 持续存在），但 (b) 效应量的精确估计受 rewriter 风格影响。论文应更显著地承认这一点——"Blindspot 的存在性是 robust 的，但其效应量有 ±20-25% 的 rewriter-dependent 变异"。这与我的 W4 一致。

---

**[REBUT] R2-Q4: 量化 pairwise 放大倍数**

R2 问是否有办法量化 pairwise 的放大倍数。我认为论文已提供了一个间接的上界估计：

- Claude Sonnet 4 的 BT ≈ 54-56% 可被视为 pairwise format 的"基线放大"（如果存在的话）。这意味着 pairwise 在无偏差 judge 上的"放大"最多产生 ~6pp 的偏离（从 50% 到 56%）。
- GPT-4o 的 BT 63-66% 与 Claude 的 54-56% 之间的差距（~8-10pp）则反映了 judge-specific bias 的下界。

但我同意精确量化放大倍数需要 human ground-truth——如果人类对同一 pairs 的 pairwise preference 是 BT = X%，而 LLM judge 是 BT = Y%，则 Y/X 就是放大倍数。当前设计无法提供这一数据。这是 future work 而非当前论文的致命缺陷。

---

### 总结

R2 的审稿意见整体质量高，与我的审查存在多处共鸣（novelty framing、NLI gate 验证、因果语言谨慎性）。核心分歧在 N2 的严重程度判定：R2 将 "检测 vs. 放大" 定为 critical，而我认为负对照已提供了充分缓解，应降为 warning。两份审稿意见共同指向的最大可 actionable 改进是：**增加 human evaluation 数据**（同时验证 content preservation 和 pairwise bias 的人类可观测性）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 802 · 2026-05-22T09:25:33.145617+00:00_

收到 Reviewer 1 的交叉回应，等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 79

## Round 79

16 recorded events


### User

_source line 803 · 2026-05-22T09:25:35.852703+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部 Weaknesses (N1, N2, W1-W4) 和 Questions (Q1-Q4) 的逐条回应。核心判断：

- **N1 (novelty framing)**: AGREE — 与我的 N2 一致
- **N2 (检测 vs. 放大)**: REBUT — 负对照已充分缓解，建议降为 warning
- **W1-W3**: AGREE — axis 覆盖、NLI 选择偏差、100-point Likert 单 judge 均为合理关切
- **W4 (因果语言)**: REBUT — §3.5 的 disclaimer 已足够明确，问题仅在 Title/Abstract 措辞
- 两份审稿共同指向的最大改进方向：增加 human evaluation 数据

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 804 · 2026-05-22T09:26:35.385493+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 805 · 2026-05-22T09:26:35.789650+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T09:12:38.100700+00:00\", \"completed_at\": \"2026-05-22T09:15:26.453971+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 16\", \"message\": \"末页仅 3 条 reference，约 85% 空白；建议将部分 appendix 内容后移或调整分页，使末页填充更充分\"}, {\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"3 个 display items（Figure 3 + Table 2 + Figure 4）挤在同一页，Figure 3 和 Figure 4 图幅偏小，axis label 接近可读性下限；建议将 Table 2 或 Figure 4 移至 P7 分散密度\"}, {\"severity\": \"info\", \"dimension\": \"page 1-3\", \"message\": \"前 3 页中仅 P2 有 1 个 display item，P1 和 P3 为纯文本；P1→P3 构成约 2 页纯文本区段（P2 的 Figure 1 打断了连续性，但视觉上仍偏\\\"文字墙\\\"）\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 因果 DAG 图节点标签偏小（\\\"S\\\"、\\\"Q\\\"、\\\"style bias\\\" 等），打印后可能需审稿人凑近看\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3 的 filled/open diamond marker 尺寸较小，灰度打印时 significance 区分度可能下降；建议辅以 marker size 或额外视觉编码\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"References 从 P13 底部开始，导致 P13 下方约 1/4 页为 reference 文字与 appendix 表格的过渡区，略显拥挤\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 806 · 2026-05-22T09:26:35.790038+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-22T09:26:41.362581+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 5572
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-22T09:26:43.520622+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/ac32e3f2-434b-434d-b640-29531c2ffb24/tool-results/b3b4h0xo9.txt",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/ac32e3f2-434b-434d-b640-29531c2ffb24/tool-results/b3b4h0xo9.txt",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-22T09:26:43.571427+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-4 issues (all resolved unless noted)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 5
13	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
14	    resolution_round: 4
15	    mentions:
16	      - round: 3
17	        reviewers: [1, 2]
18	        note: "因果语言降级问题在 Round 3 以新形式复发，见 R3-N1"
19	      - round: 4
20	        reviewers: [1]
21	        note: "R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。"
22	      - round: 5
23	        reviewers: [1, 2]
24	        note: "标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2"
25	      - round: 8
26	        reviewers: []
27	        note: "本轮未提及，可能已修复，待 Research Director 确认"
28	
29	  - id: "R2-N1"
30	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
31	    category: framing
32	    severity: warning
33	    status: in_progress
34	    first_raised_round: 1
35	    last_seen_round: 8
36	    resolution: null
37	    resolution_round: null
38	    mentions:
39	      - round: 3
40	        reviewers: [1, 2]
41	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
42	      - round: 4
43	        reviewers: [1, 2]
44	        note: "R4-SF8: Honest novelty positioning applied."
45	      - round: 5
46	        reviewers: [1, 2]
47	        note: "Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。"
48	      - round: 7
49	        reviewers: [2]
50	        note: "R2 再次指出核心发现可从 Thurstone (1927) 理论直接预测。R1 反驳称 severity spectrum 和 per-axis interaction 是全新经验发现。分歧未完全解决。"
51	      - round: 8
52	        reviewers: [1, 2]
53	        note: "R8-R2 列为 Must-Fix，R8-R1 交叉 AGREE（但补充 LLM 非人类 rat
…[truncated 4404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-22T09:26:47.786692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/ac32e3f2-434b-434d-b640-29531c2ffb24/tool-results/b3b4h0xo9.txt",
  "offset": "200",
  "limit": "400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/ac32e3f2-434b-434d-b640-29531c2ffb24/tool-results/b3b4h0xo9.txt",
    "offset": "200",
    "limit": "400"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-22T09:26:47.837635+00:00_

200	    first_raised_round: 1
201	    last_seen_round: 1
202	    resolution: "Per-cell GEE with cross-judge validation"
203	    resolution_round: 1
204	
205	  - id: "CROSS-3"
206	    summary: "Likert ATE 方向反转"
207	    category: experiment
208	    severity: warning
209	    status: resolved
210	    first_raised_round: 1
211	    last_seen_round: 1
212	    resolution: "Magnitude gap framing"
213	    resolution_round: 1
214	
215	  - id: "CROSS-4"
216	    summary: "Ordinal regression 必要"
217	    category: method
218	    severity: critical
219	    status: resolved
220	    first_raised_round: 1
221	    last_seen_round: 1
222	    resolution: "Definitively resolved"
223	    resolution_round: 1
224	
225	  - id: "RD2-MF2"
226	    summary: "Holm-Bonferroni 'nine tests' 错误"
227	    category: method
228	    severity: critical
229	    status: resolved
230	    first_raised_round: 2
231	    last_seen_round: 2
232	    resolution: "Text fixed to '6 tests'. Holm 6-test: 4/6 significant."
233	    resolution_round: 2
234	
235	  - id: "RD2-MF3"
236	    summary: "单一 benchmark (LLMBar n=100) 不支撑全称论断"
237	    category: experiment
238	    severity: critical
239	    status: resolved
240	    first_raised_round: 2
241	    last_seen_round: 4
242	    resolution: "3 benchmarks x 3 judges. 6/7 biased cells BT significant."
243	    resolution_round: 2
244	
245	  - id: "RD2-MF4"
246	    summary: "Abstract overclaim: 'dominant source' + verbosity category error"
247	    category: framing
248	    severity: critical
249	    status: resolved
250	    first_raised_round: 2
251	    last_seen_round: 2
252	    resolution: "Overclaim replaced in intro. Verbosity category error removed."
253	    resolution_round: 2
254	
255	  - id: "RD2-VIS"
256	    summary: "主正文超 8 页限制"
257	    category: format
258	    severity: critical
259	    status: resolved
260	    first_raised_round: 2
261	    last_seen_round: 7
262	    resolution: "Round 7 两位 Reviewer 均确认主正文 8 页合规。§5.5 Register 压缩 + §6 Conclusion 精简。"
263	    resolution_r
…[truncated 12184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-22T09:26:54.058902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/ac32e3f2-434b-434d-b640-29531c2ffb24/tool-results/b3b4h0xo9.txt",
  "offset": "600"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/ac32e3f2-434b-434d-b640-29531c2ffb24/tool-results/b3b4h0xo9.txt",
    "offset": "600"
  }
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-22T09:26:54.110325+00:00_

600	    first_raised_round: 3
601	    last_seen_round: 5
602	    resolution: "TOST equivalence testing added. Abstract changed 'confirms' to 'supports'."
603	    resolution_round: 4
604	    mentions:
605	      - round: 5
606	        reviewers: [2]
607	        note: "TOST at Delta=10pp underpowered (n=87). 措辞仍需更审慎。见 R5-M3。"
608	
609	  - id: "R3-M2"
610	    summary: "Table 1 Holm-Bonferroni p-value 标注不够直觉"
611	    category: format
612	    severity: info
613	    status: resolved
614	    first_raised_round: 3
615	    last_seen_round: 4
616	    resolution: "Table 1 footnotes updated."
617	    resolution_round: 4
618	
619	  - id: "R3-M3"
620	    summary: "Abstract 过长过密"
621	    category: writing
622	    severity: info
623	    status: in_progress
624	    first_raised_round: 3
625	    last_seen_round: 8
626	    resolution: null
627	    resolution_round: null
628	    mentions:
629	      - round: 4
630	        reviewers: [2]
631	        note: "仍指出 Abstract 信息密度过高。"
632	      - round: 5
633	        reviewers: [1, 2]
634	        note: "两位 Reviewer 均再次指出 Abstract 过密。Minor issue。"
635	      - round: 6
636	        reviewers: [1, 2]
637	        note: "R6-R2 列为 Should-Fix；R6-R1 建议降级 Minor。交叉后分歧。"
638	      - round: 7
639	        reviewers: [1, 2]
640	        note: "R7 两位 Reviewer 再次一致指出（R1-Detailed, R2-W4）：7 句含 4 组括号统计数据，首次阅读认知负担过重。共识 Should-Fix。"
641	      - round: 8
642	        reviewers: [2]
643	        note: "R8-R2 指出 Abstract 首句 'near-perfect correlation' 过于绝对（76-92% ≠ near-perfect）。R8-R1 交叉 AGREE。"
644	    action_items:
645	      - round: 7
646	        action: "将具体统计数字移至 Introduction，Abstract 聚焦定性结论和核心 message"
647	        assigned_to: paper_agent
648	        status: in_progress
649	
650	  - id: "R3-M4"
651	    summary: "Orphan bib entries"
652	    category: format
653	    severity: info
654	    status: resolved
655	    first_raised_round: 3
656	    last_seen_round: 4
657	    resolution: "hoenig2001abuse cited via citealt. Not orphan."
658	    resolution_round: 4
659	
660	  # 
…[truncated 24521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-22T09:33:11.416436+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"因果语言降级问题在 Round 3 以新形式复发，见 R3-N1\"\n      - round: 4\n        reviewers: [1]\n        note: \"R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2\"\n      - round: 8\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 9\n        reviewers: []\n        note: \"R9 fresh review 未提及此问题。标题和 §3.5 已修复。\"\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4-SF8: Honest novelty positioning applied.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。\"\n      - round: 7\n        reviewers: [2]\n        note: \"R2 再次指出核心发现可从 Thurstone (1927) 理论直接预测。R1 反驳称 severity spectrum 和 per-axis interaction 是全新经验发现。分歧未完全解决。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix，R8-R1 交叉 AGREE。共识：novelty 定位需从'discovering the Blindspot'调整为'first controlled per-axis quantification in LLM judges'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出（R1-N2, R2-N1）。交叉后 R1 完全 AGREE R2 的 reframe 建议。共识：从 'reveal' 转为 'first systematic quantification'，将 per-axis confound structure 提升为并列核心贡献。Abstract/Title 的 'reveal' 措辞仍未修正。\"\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 2 issues\n  # ============================================================\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 7\n    resolution: \"Round 7 两位 Reviewer 均确认主正文 8 页合规。§5.5 Register 压缩 + §6 Conclusion 精简。\"\n    resolution_round: 7\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Round 2 发现并修复。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Round 6 再次发现：Section 6 (Conclusion) 约 5-6 行溢出到 page 9。两位 Reviewer 共识 Must-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Round 7 两位 Reviewer 均确认主正文 8 页合规。页数问题已修复。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 两位 Reviewer 均确认正文 ≤8 页合规。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 Reviewer 1 格式检查项。正文 8 页合规。\"\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Independence test 仅覆盖 verbosity，formality 缺 test。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Formality rewriter independence 已补。Register 仍缺。Style OR 下降 22% 非可忽略。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R5 两位 Reviewer 均再次指出。R1 定为 critical（self-preference bias 无法排除），R2 认为 should-fix（GPT-4o 不受影响）。交叉后共识：should-fix。主文 Section 5 缺 caveat。见 R5-SF2。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix：22% OR 下降处理不充分 + register 轴完全缺失 cross-rewriter test。R6-R2 同意 22% non-trivial 但注意 Blindspot pattern 在 GPT-4o rewriter 下完全保持。共识：Must-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 独立标注为核心问题（R1-W1, R2-W5），交叉后双方 [AGREE]。cross-rewriter validation 仅覆盖 Qwen3-32B judge，GPT-4o/Llama-70B judge 未验证。22% Style OR 下降确认 inflation 存在。共识 Must-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 列为 Must-Fix (N2)：仅 1/4 judges 有 cross-rewriter 验证。R8-R2 交叉 AGREE 但补充核心 claim 不依赖 rewriter-independence（Blindspot 在 4 judges 上用同一 rewriter 一致确认）。共识：Must-Fix，但 claim scope 应 downgrade。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R1 W4: cross-rewriter 验证仅限 Qwen3-32B judge。R1 交叉同意 R2-Q3（22% OR 下降暗示效应量部分依赖 rewriter）。共识 Should-Fix：Blindspot 存在性 robust，但效应量有 ±20-25% rewriter-dependent 变异，需显式承认。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"Register independence test — acknowledged as limitation\"\n        assigned_to: paper_agent\n        status: wont_fix\n      - round: 6\n        action: \"§5.4 加 cross-ref sentence：22% OR 下降 + NLI pass rate argument + register caveat in Limitations\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 8\n        action: \"将 Appendix D 结论从 'Blindspot persists with independent rewriter' 改为 'persists for at least one judge configuration; broader validation remains for future work'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 'approximates the do-operator' 残留。见 R5-MF2。\"\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'. n=355 d->0 evidence.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"attenuation framing 已改善，但 'construct difference' 替代解释在主文中仍不足。见 R5-SF6。\"\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Cross-rewriter consistency + 200-pair GPT-4o validation provide partial proxy. Acknowledged in Limitations.\"\n      - round: 5\n        reviewers: []\n        note: \"Round 5 未被任何 Reviewer 显式提及，但仍 inherently open（无人工评估数据）。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix。R6-R2 同意但建议降级为 strong Should-Fix。交叉后共识：Must-Fix，50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 列为 Should-Fix (W6)，R7-R2 完全同意。两位 Reviewer 共识：全文零人工验证，涉及测量工具敏感度的论文却用同类工具验证，存在认识论循环。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix（需至少 50 pairs human evaluation 区分 detection vs amplification）。R8-R1 交叉 AGREE 方向但建议降级为 Strong Should-Fix（论文可通过 Limitations 讨论部分 mitigate，完整 human eval 更适合 follow-up）。Director 判定 Strong Should-Fix。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R1 N1 (critical): NLI gate 缺乏人工验证是因果推断链最薄弱环节。R9-R2 Q1 同意。交叉后两位共同指向：增加 human evaluation 是最大可 actionable 改进（同时验证 content preservation 和 pairwise bias 的人类可观测性）。此问题持续 7 轮未解决。\"\n    action_items:\n      - round: 6\n        action: \"准备 50 对 NLI pass/fail 样本 + 标注模板，用户标注后报告 agreement + Cohen's κ\"\n        assigned_to: user\n        status: pending\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"术语已改善，但 verbosity 'confound-free' 措辞仍过强。见 R5-SF4。\"\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"引用量已改善，但遗漏了 Jeong et al. (2025) Comparative Trap 等关键文献。见 R5-MF1。\"\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"TOST at Delta=10pp underpowered (n=87). 措辞仍需更审慎。见 R5-M3。\"\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"仍指出 Abstract 信息密度过高。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均再次指出 Abstract 过密。Minor issue。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 列为 Should-Fix；R6-R1 建议降级 Minor。交叉后分歧。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 再次一致指出（R1-Detailed, R2-W4）：7 句含 4 组括号统计数据，首次阅读认知负担过重。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 指出 Abstract 首句 'near-perfect correlation' 过于绝对（76-92% ≠ near-perfect）。R8-R1 交叉 AGREE。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 fresh review 未显式提出 Abstract 过密问题，但 Abstract 仍包含大量统计数据。\"\n    action_items:\n      - round: 7\n        action: \"将具体统计数字移至 Introduction，Abstract 聚焦定性结论和核心 message\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再次提出 IIA 未检验，R2 技术性反驳。交叉后共识：降级 minor。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"交叉后共识：Minor。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 列为 Should-Fix (W2)：Appendix H formality 方向异质性 (68.9% vs 52.6%, Fisher p=0.015) 挑战 IIA。R8-R2 交叉 AGREE，建议报告 direction-stratified BT。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未显式提及 IIA 问题。论文 §4.1 footnote 已承认 direction asymmetry for formality。\"\n    action_items:\n      - round: 8\n        action: \"在主文或附录中承认 IIA 假设，报告 direction-stratified BT estimates\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)——pairwise amplification vs detection sensitivity 张力未讨论\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 首先识别，R1 交叉完全同意。Jeong et al. (2025) 证明 pairwise 放大 style bias，与 Section 6 'adopt pairwise' 建议矛盾。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"论文已在 §2 和 §5.2 加入 Jeong et al. 讨论。但 §6 Conclusion 'should adopt' 仍过强。共识 Should-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 确认论文已在 Section 5.2 加入 6 项 amplification controls 回应 Comparative Trap。R7-R2 补充要求引用 Tripathi et al. (2025) 作为额外 amplification evidence。已从 critical 降级为 Should-Fix。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及此 issue。论文 §5.2 已含 6 项 amplification controls 和 Jeong et al. 讨论。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R2 N2 (critical): 检测 vs 放大歧义是核心未解决问题。R9-R1 REBUT 部分——负对照是最强反驳证据，应降为 warning。论文 §5.4 已有 6 项 controls，但 Conclusion 语言仍偏向单一解释。分歧记录：R2 定 critical，R1 建议 warning。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap\"\n        assigned_to: paper_agent\n        status: done\n      - round: 6\n        action: \"在 §6 Conclusion 加入 pairwise amplification caveat\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强——selection/conditioning ≠ intervention\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§3.2 原文 'approximates the do-operator' 过强。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§3.2 已改为 'filtering-based confounder control'，但 Intro/Abstract 仍用 'interventional framework'。共识 Should-Fix。\"\n      - round: 7\n        reviewers: [1]\n        note: \"R7-R1 (S1) 正面评价 §3.5 的因果语言校准。原始 'do-operator' 语言已修复。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 列为 Should-Fix (W1)：全文因果术语不一致。R8-R2 REBUT：§3.5 hedge 恰当。Director 判定：建议在 §3.5 开头加一句统一声明。\"\n      - round: 9\n        reviewers: [2]\n        note: \"R9-R2 W4: 'Controlled' 和 'interventional' 语言暗示过强因果识别。R9-R1 部分反驳——§3.5 disclaimer 已足够明确，问题仅在 Title/Abstract 措辞。共识：Title/Abstract 需微调，方法论本身无问题。\"\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"'first' 需限定到 CSD 具体方法组合的 novelty。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 Must-Fix vs R6-R1 Should-Fix。Director 判定 Should-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W1) 列为 Must-Fix：'the first framework combining...' 通过组合限定词构造唯一性。R7-R1 交叉 [AGREE]，建议改为 'a unified framework'。共识 Must-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (N1) 再次要求 novelty reframing。R8-R1 AGREE 但指出论文确有超越 Thurstone 的 empirical contributions。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 两位 Reviewer 再次独立确认 novelty framing 问题。Abstract 中 'reveal' 和 'Blindspot' 作为新发现的措辞仍未修正。共识：需从 'reveal' 转为 'quantify'。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework' 或 'a framework that integrates'\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 定 critical，R2 should-fix。交叉后共识：should-fix。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RD2-SF1 涵盖此项。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1 讨论。仍为 in_progress。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R8 两位 Reviewer 均再次确认。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R9 再次确认。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Llama-70B 加入后现有 3 target judges 全部展示 Blindspot (6/6 cells + register 7/9)。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"论文已使用 'style-dominated' 而非 'confound-free'。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示——缺 verbosity 验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现严重不平衡\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"需在 §5.2 给两种解释同等篇幅。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§5.2 末尾已加入讨论段落。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W2) 列为 Must-Fix。R7-R1 [REBUT]。Director 判定 Should-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (W5) 再次指出 'Blindspot' 术语偏向 attenuation 解释。R8-R2 交叉 AGREE。标题和 Abstract framing 偏颇。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R1 N2 和 R9-R2 N2 均涉及此问题。R9-R1 Q3 直接追问 bootstrap attenuation 如何排除 construct-level 差异。论文 §5.1 已有讨论但 'Blindspot' 术语天然偏向 attenuation 解释。共识：正文讨论已有改善但 Title/Abstract 措辞仍需调整。\"\n\n  - id: \"R5-SF7\"\n    summary: \"Formality confound 在 Abstract/Conclusion 中未与 verbosity 区分\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Abstract 和 Conclusion 中已有 per-axis differentiation。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点（0.50-0.98）。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Register 是最弱轴，恰是 rewriter identity 最可能影响结论的轴。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Acknowledged as limitation 但未补实验。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 在 evaluator-producer 讨论中再次确认 register 缺失。已在 Limitations 标注。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1 cross-rewriter 讨论。Register 仍为最高风险轴。\"\n      - round: 9\n        reviewers: [1]\n        note: \"R9-R1 在 evaluator-producer overlap 讨论中确认仍未覆盖 register。Limitations 已承认但无实验数据。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Equivalence bound Delta=15pp 缺外部 justification。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 Should-Fix，R6-R2 同意。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W3) 再次标注 TOST Δ=15pp 过宽。R7-R2 交叉 [AGREE] 但补充论文核心论证不依赖 TOST。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 升级为 Must-Fix (N3)：Δ=15pp 几乎涵盖最小 confirmed bias (+13pp GPT-4o formality)。共识 Must-Fix。\"\n      - round: 9\n        reviewers: [1]\n        note: \"R9-R1 W3: TOST Δ=15pp margin 偏宽，GPT-4o formality 偏差仅约 13pp，15pp margin 接近 target judges 效应量。Claude 仅覆盖 2/3 axes。论文 Appendix G 承认 Δ=10pp underpowered。\"\n    action_items:\n      - round: 7\n        action: \"将 Claude 相关语言从 'equivalence confirmed' / 'no bias' 改为 'failed to detect bias at Δ=15pp precision'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 8\n        action: \"三选一：(a) 增加 Claude n 使 Δ=10pp 有功效；(b) reframe 为 'insufficient evidence for bias'；(c) 报告 n=87 下能 reject 的最小 Δ\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"每个缺失 cell 应在 footnote 或 Appendix 说明原因。\"\n      - round: 6\n        reviewers: [2]\n        note: \"Table 1 第 6 列无 header。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 格式检查确认第 6 列仍无列标题。R7-R1 交叉 [AGREE]。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (W2) 再次指出 Table 1 信息密度过高、可读性差。R8-R1 交叉 AGREE。\"\n      - round: 9\n        reviewers: [1]\n        note: \"R9-R1 W1 Q2: 缺失单元格（'—'）代表什么？Table 1 footnote 已有 'Empty cells: untested benchmark-axis combinations' 但未解释选择哪些组合的理由。\"\n    action_items:\n      - round: 7\n        action: \"Table 1 第 6 列添加列标题（如 'Status' 或 'Finding'）\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"建议颜色 + 线型双重编码。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Figure 2/3 灰度区分问题再次提及。\"\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 (M2) 再次指出 Figure 2 颜色编码在 150 DPI 下辨认困难。\"\n    action_items:\n      - round: 6\n        action: \"Figure 2/3 增加颜色+线型双重编码\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025), Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound (Delta=15pp) 缺乏独立外部 justification\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"需引用外部基准设定 equivalence bound。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3 讨论。TOST Δ=15pp 与 GPT-4o formality +13pp 仅差 2pp。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3/R8 Must-Fix 讨论。\"\n      - round: 9\n        reviewers: [1]\n        note: \"合并入 R5-M3 讨论。R9-R1 W3 再次确认 Δ=15pp 接近 target judges 效应量。\"\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 讨论不充分\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1]\n        note: \"same-style control 只检测 rewriting artifact 但无法检测 axis-specific confounds。\"\n      - round: 7\n        reviewers: []\n        note: \"Round 7 未被显式提及。\"\n      - round: 8\n        reviewers: [1]\n        note: \"R8-R1 在 Detailed Comments §3.5 中再次指出假设(iii)最难验证。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R1 W2: style axis 之间的 interaction/cross-contamination 未测试（formal 改写是否系统性改变 verbosity？）。R9-R2 在 cross-response 中 AGREE。Table 5 GEE interaction test 只检验 Style×Originality 而非 cross-axis interaction。建议对每个 axis 改写样本测量其他 axis 的变化幅度。\"\n    action_items:\n      - round: 6\n        action: \"在 Limitations 补充讨论 axis-specific confounds\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄——n=355 仅限 Qwen3-32B formality\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"LLMBar n=100 为主数据源，MT-Bench n=30。n=355 仅覆盖一个 judge×axis。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W3) 列为 Must-Fix。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 (W1) 指出仅 3 轴难以支撑 framework 级别泛化。共识 Should-Fix。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R1 W1: NLI filtering 后 n=55-88，cross-benchmark 覆盖不完整。R9-R2 W1: 仅 2+1 axes 限制泛化。交叉后共识 Should-Fix：CSD 方法论 axis-agnostic 但 empirical evidence 仍窄。\"\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"GPT-4o formality/verbosity/register 和 Qwen3 formality Orig OR 只有点估计无 CI。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (Q1) 和 R7-R2 交叉回应均确认 7 个 CI 缺失。必须补全。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。Appendix Table 5 现已有完整 CI（Table tab:gee_ci 12 行均含 CI）。可能已修复。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 检查 Appendix C Table 5 已有完整 12 行 CI。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 7\n        action: \"补全 Appendix Table 5 所有 GEE CI\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"论文 Related Work §2 已引用 Shi et al. (2024) 和 Bavaresco et al. (2025)。\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 7 issues\n  # ============================================================\n\n  - id: \"R7-W2\"\n    summary: \"Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 含 register (8 tests) vs Table 1 标 register 为 exploratory (†_e)\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"明确矛盾，直接影响 Holm-Bonferroni 校正的 adjusted p-values。需统一为 6-test 或 8-test family。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (N1) 列为 Must-Fix：§4.1 声明 'six tests' 但未指明哪三个 judges。如果排除 Gemini 存在 post-hoc cherry-picking 嫌疑。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 检查：§4.1 现在明确 'six tests—three target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B) × two axes (formality, verbosity)—corrected via Holm-Bonferroni'，Gemini 为 confirmatory，Appendix Q 报告 8-test family 下所有结果仍显著。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 7\n        action: \"统一 Section 4.1 primary family 定义与 Table 1 标注\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 8\n        action: \"在 §4.1 明确列出三个 primary judges 名称及排除理由；报告 8-test family 下 adjusted p-values 作为 sensitivity analysis\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R7-W4\"\n    summary: \"NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型（与 rewriter 相同），存在循环性\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W4) 提出。R7-R2 交叉部分同意。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (W3) 独立指出 FNR 基于仅 12 个 rejected pairs（Wilson 95% CI ≈ [2%, 28%]），样本量过小。R8-R2 交叉 AGREE。应报告 CI 而非仅点估计。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 检查：论文 §5.4 第一段报告 'FNR = 8.4% [95% Wilson CI: 3.7%, 15.9%]'。CI 已报告。循环性问题（Qwen3-32B 做 NLI annotator）未在正文讨论——GPT-4o cross-validation (92.1%/82.6%) 部分缓解但非完全解决。\"\n\n  - id: \"R7-W5\"\n    summary: \"Verbosity direction-aware NLI gate GPT-4o validation 显示 17.4% FPR，正文未报告\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W5) 提出。R7-R2 交叉 [AGREE]。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (W4) 指出 direction-aware gating 额外放入 21 pairs (+32%)，可能引入 selection bias。R8-R2 交叉 AGREE。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未显式提及。Appendix F 已有 direction-aware gate validation data。\"\n\n  - id: \"R7-REF1\"\n    summary: \"遗漏引用：Tripathi et al. (2025) 'Pairwise or Pointwise?'\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: \"论文 §5.1 已引用 Tripathi et al. (2025)。\"\n    resolution_round: 9\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W6) 提出。R7-R1 交叉同意。\"\n      - round: 8\n        reviewers: [1]\n        note: \"R8-R1 确认论文 §5.2 已引用 Tripathi et al. (2025)。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 确认 §5.1 含 Tripathi et al. (2025) 引用。已解决。\"\n\n  # ============================================================\n  # Round 8 issues\n  # ============================================================\n\n  - id: \"R8-W1\"\n    summary: \"3 个风格轴限制 'framework' 级别的泛化声明——需从 'framework' 降为 'methodology'\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"仅 formality/verbosity/register 3 轴。共识 Should-Fix：将 'framework' 改为 'methodology'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R2 W1 再次指出 style axis 覆盖过窄。R9-R1 AGREE 方向但认为严重程度为 warning（方法论论文的价值在于通用性而非穷举）。共识：限定 'per-axis confound structure' 为 'preliminary evidence'。\"\n    action_items:\n      - round: 8\n        action: \"在 Contribution 中将 'framework' 改为 'methodology'；Limitations 中列出未覆盖轴\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R8-W2\"\n    summary: \"生态效度（ecological validity）讨论不足——controlled manipulation 到 naturalistic evaluation 的 generalizability gap\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"Limitations 中应增加独立 point。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 检查 Limitations：已有 'Our controlled manipulation design ensures internal validity but may not fully generalize to naturalistic evaluation settings where style and content covary.' 可能已部分处理。\"\n    action_items:\n      - round: 8\n        action: \"在 Limitations 中新增生态效度讨论段落\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R8-W3\"\n    summary: \"Rewriting artifact 的 style-specific polishing interaction 未讨论\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (W4) 提出。R8-R1 PARTIALLY AGREE。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 检查 Appendix O：已有 'Same-style double-rewrite controls for style-neutral polishing artifacts but cannot exclude style-specific polishing interactions.' 可能已部分处理。\"\n    action_items:\n      - round: 8\n        action: \"在 Limitations 或 Appendix O 中讨论 style-specific polishing interaction 可能性\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R8-W4\"\n    summary: \"Introduction motivating example ('average height') 未 acknowledge formality-quality nuance\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"论文自己的 GEE 结果显示 formality 存在 significant Originality effect。Introduction 应 acknowledge。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 检查 §1：motivating example 后有 'We note that formality preferences may partially reflect legitimate quality judgments—our GEE decomposition (§5.2) quantifies this originality component.' 已处理。\"\n\n  - id: \"R8-REF1\"\n    summary: \"建议补充引用：Girrbach et al. (2025/2026) 'Likert or Not'\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 建议。R8-R1 PARTIALLY AGREE，需验证文献真实性。\"\n\n  # ============================================================\n  # Round 9 new issues\n  # ============================================================\n\n  - id: \"R9-N1\"\n    summary: \"100-point continuous Likert 实验仅用单一 judge（Qwen3-32B），泛化性不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R2 W3 提出，R9-R1 交叉 AGREE。Appendix M 100-point Likert 仅 Qwen3-32B，如果 GPT-4o 在 100-point scale 下 ATE 变显著则 Blindspot 对某些 judge 可能确是粒度问题。建议至少增加 GPT-4o 作为第二个 judge。\"\n\n  - id: \"R9-N2\"\n    summary: \"NLI gate 44% 拒绝率的 selection bias 特征分析不足——仅检查 4 个 surface covariates\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R2 W2 提出，R9-R1 交叉 AGREE。Appendix B 报告 4 covariates 无差异（NLI score, BERTScore, text length, length diff），但未检查语言复杂度、论证结构、话题类型等深层特征。Filtered-in pairs 可能系统性偏向内容更简单的文本，影响 external validity。\"\n\n  - id: \"R9-REF1\"\n    summary: \"建议补充引用：IRT 在 LLM 评估中的应用（Polo et al. 2024, Otani et al. 2023）、Kocmi & Federmann (2023)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 9\n        reviewers: [2]\n        note: \"R9-R2 建议补充 IRT 文献（Polo et al. 2024 tinyBenchmarks, Otani et al. 2023）和 Kocmi & Federmann (2023) LLM judge multilingual bias。另建议补充 Simms et al. (2019) rating scale granularity 和 Funke (2016) response format effects。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"因果语言降级问题在 Round 3 以新形式复发，见 R3-N1\"\n      - round: 4\n        reviewers: [1]\n        note: \"R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2\"\n      - round: 8\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 9\n        reviewers: []\n        note: \"R9 fresh review 未提及此问题。标题和 §3.5 已修复。\"\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4-SF8: Honest novelty positioning applied.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。\"\n      - round: 7\n        reviewers: [2]\n        note: \"R2 再次指出核心发现可从 Thurstone (1927) 理论直接预测。R1 反驳称 severity spectrum 和 per-axis interaction 是全新经验发现。分歧未完全解决。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix，R8-R1 交叉 AGREE。共识：novelty 定位需从'discovering the Blindspot'调整为'first controlled per-axis quantification in LLM judges'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出（R1-N2, R2-N1）。交叉后 R1 完全 AGREE R2 的 reframe 建议。共识：从 'reveal' 转为 'first systematic quantification'，将 per-axis confound structure 提升为并列核心贡献。Abstract/Title 的 'reveal' 措辞仍未修正。\"\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 2 issues\n  # ============================================================\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 7\n    resolution: \"Round 7 两位 Reviewer 均确认主正文 8 页合规。§5.5 Register 压缩 + §6 Conclusion 精简。\"\n    resolution_round: 7\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Round 2 发现并修复。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Round 6 再次发现：Section 6 (Conclusion) 约 5-6 行溢出到 page 9。两位 Reviewer 共识 Must-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Round 7 两位 Reviewer 均确认主正文 8 页合规。页数问题已修复。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 两位 Reviewer 均确认正文 ≤8 页合规。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 Reviewer 1 格式检查项。正文 8 页合规。\"\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Independence test 仅覆盖 verbosity，formality 缺 test。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Formality rewriter independence 已补。Register 仍缺。Style OR 下降 22% 非可忽略。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R5 两位 Reviewer 均再次指出。R1 定为 critical（self-preference bias 无法排除），R2 认为 should-fix（GPT-4o 不受影响）。交叉后共识：should-fix。主文 Section 5 缺 caveat。见 R5-SF2。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix：22% OR 下降处理不充分 + register 轴完全缺失 cross-rewriter test。R6-R2 同意 22% non-trivial 但注意 Blindspot pattern 在 GPT-4o rewriter 下完全保持。共识：Must-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 独立标注为核心问题（R1-W1, R2-W5），交叉后双方 [AGREE]。cross-rewriter validation 仅覆盖 Qwen3-32B judge，GPT-4o/Llama-70B judge 未验证。22% Style OR 下降确认 inflation 存在。共识 Must-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 列为 Must-Fix (N2)：仅 1/4 judges 有 cross-rewriter 验证。R8-R2 交叉 AGREE 但补充核心 claim 不依赖 rewriter-independence（Blindspot 在 4 judges 上用同一 rewriter 一致确认）。共识：Must-Fix，但 claim scope 应 downgrade。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R1 W4: cross-rewriter 验证仅限 Qwen3-32B judge。R1 交叉同意 R2-Q3（22% OR 下降暗示效应量部分依赖 rewriter）。共识 Should-Fix：Blindspot 存在性 robust，但效应量有 ±20-25% rewriter-dependent 变异，需显式承认。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"Register independence test — acknowledged as limitation\"\n        assigned_to: paper_agent\n        status: wont_fix\n      - round: 6\n        action: \"§5.4 加 cross-ref sentence：22% OR 下降 + NLI pass rate argument + register caveat in Limitations\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 8\n        action: \"将 Appendix D 结论从 'Blindspot persists with independent rewriter' 改为 'persists for at least one judge configuration; broader validation remains for future work'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 'approximates the do-operator' 残留。见 R5-MF2。\"\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'. n=355 d->0 evidence.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"attenuation framing 已改善，但 'construct difference' 替代解释在主文中仍不足。见 R5-SF6。\"\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Cross-rewriter consistency + 200-pair GPT-4o validation provide partial proxy. Acknowledged in Limitations.\"\n      - round: 5\n        reviewers: []\n        note: \"Round 5 未被任何 Reviewer 显式提及，但仍 inherently open（无人工评估数据）。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix。R6-R2 同意但建议降级为 strong Should-Fix。交叉后共识：Must-Fix，50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 列为 Should-Fix (W6)，R7-R2 完全同意。两位 Reviewer 共识：全文零人工验证，涉及测量工具敏感度的论文却用同类工具验证，存在认识论循环。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix（需至少 50 pairs human evaluation 区分 detection vs amplification）。R8-R1 交叉 AGREE 方向但建议降级为 Strong Should-Fix（论文可通过 Limitations 讨论部分 mitigate，完整 human eval 更适合 follow-up）。Director 判定 Strong Should-Fix。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R1 N1 (critical): NLI gate 缺乏人工验证是因果推断链最薄弱环节。R9-R2 Q1 同意。交叉后两位共同指向：增加 human evaluation 是最大可 actionable 改进（同时验证 content preservation 和 pairwise bias 的人类可观测性）。此问题持续 7 轮未解决。\"\n    action_items:\n      - round: 6\n        action: \"准备 50 对 NLI pass/fail 样本 + 标注模板，用户标注后报告 agreement + Cohen's κ\"\n        assigned_to: user\n        status: pending\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"术语已改善，但 verbosity 'confound-free' 措辞仍过强。见 R5-SF4。\"\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"引用量已改善，但遗漏了 Jeong et al. (2025) Comparative Trap 等关键文献。见 R5-MF1。\"\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"TOST at Delta=10pp underpowered (n=87). 措辞仍需更审慎。见 R5-M3。\"\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"仍指出 Abstract 信息密度过高。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均再次指出 Abstract 过密。Minor issue。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 列为 Should-Fix；R6-R1 建议降级 Minor。交叉后分歧。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 再次一致指出（R1-Detailed, R2-W4）：7 句含 4 组括号统计数据，首次阅读认知负担过重。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 指出 Abstract 首句 'near-perfect correlation' 过于绝对（76-92% ≠ near-perfect）。R8-R1 交叉 AGREE。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 fresh review 未显式提出 Abstract 过密问题，但 Abstract 仍包含大量统计数据。\"\n    action_items:\n      - round: 7\n        action: \"将具体统计数字移至 Introduction，Abstract 聚焦定性结论和核心 message\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再次提出 IIA 未检验，R2 技术性反驳。交叉后共识：降级 minor。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"交叉后共识：Minor。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 列为 Should-Fix (W2)：Appendix H formality 方向异质性 (68.9% vs 52.6%, Fisher p=0.015) 挑战 IIA。R8-R2 交叉 AGREE，建议报告 direction-stratified BT。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未显式提及 IIA 问题。论文 §4.1 footnote 已承认 direction asymmetry for formality。\"\n    action_items:\n      - round: 8\n        action: \"在主文或附录中承认 IIA 假设，报告 direction-stratified BT estimates\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)——pairwise amplification vs detection sensitivity 张力未讨论\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 首先识别，R1 交叉完全同意。Jeong et al. (2025) 证明 pairwise 放大 style bias，与 Section 6 'adopt pairwise' 建议矛盾。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"论文已在 §2 和 §5.2 加入 Jeong et al. 讨论。但 §6 Conclusion 'should adopt' 仍过强。共识 Should-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 确认论文已在 Section 5.2 加入 6 项 amplification controls 回应 Comparative Trap。R7-R2 补充要求引用 Tripathi et al. (2025) 作为额外 amplification evidence。已从 critical 降级为 Should-Fix。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及此 issue。论文 §5.2 已含 6 项 amplification controls 和 Jeong et al. 讨论。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R2 N2 (critical): 检测 vs 放大歧义是核心未解决问题。R9-R1 REBUT 部分——负对照是最强反驳证据，应降为 warning。论文 §5.4 已有 6 项 controls，但 Conclusion 语言仍偏向单一解释。分歧记录：R2 定 critical，R1 建议 warning。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap\"\n        assigned_to: paper_agent\n        status: done\n      - round: 6\n        action: \"在 §6 Conclusion 加入 pairwise amplification caveat\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强——selection/conditioning ≠ intervention\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§3.2 原文 'approximates the do-operator' 过强。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§3.2 已改为 'filtering-based confounder control'，但 Intro/Abstract 仍用 'interventional framework'。共识 Should-Fix。\"\n      - round: 7\n        reviewers: [1]\n        note: \"R7-R1 (S1) 正面评价 §3.5 的因果语言校准。原始 'do-operator' 语言已修复。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 列为 Should-Fix (W1)：全文因果术语不一致。R8-R2 REBUT：§3.5 hedge 恰当。Director 判定：建议在 §3.5 开头加一句统一声明。\"\n      - round: 9\n        reviewers: [2]\n        note: \"R9-R2 W4: 'Controlled' 和 'interventional' 语言暗示过强因果识别。R9-R1 部分反驳——§3.5 disclaimer 已足够明确，问题仅在 Title/Abstract 措辞。共识：Title/Abstract 需微调，方法论本身无问题。\"\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"'first' 需限定到 CSD 具体方法组合的 novelty。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 Must-Fix vs R6-R1 Should-Fix。Director 判定 Should-Fix。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W1) 列为 Must-Fix：'the first framework combining...' 通过组合限定词构造唯一性。R7-R1 交叉 [AGREE]，建议改为 'a unified framework'。共识 Must-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (N1) 再次要求 novelty reframing。R8-R1 AGREE 但指出论文确有超越 Thurstone 的 empirical contributions。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 两位 Reviewer 再次独立确认 novelty framing 问题。Abstract 中 'reveal' 和 'Blindspot' 作为新发现的措辞仍未修正。共识：需从 'reveal' 转为 'quantify'。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework' 或 'a framework that integrates'\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 定 critical，R2 should-fix。交叉后共识：should-fix。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RD2-SF1 涵盖此项。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1 讨论。仍为 in_progress。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R8 两位 Reviewer 均再次确认。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R9 再次确认。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Llama-70B 加入后现有 3 target judges 全部展示 Blindspot (6/6 cells + register 7/9)。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"论文已使用 'style-dominated' 而非 'confound-free'。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示——缺 verbosity 验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现严重不平衡\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"需在 §5.2 给两种解释同等篇幅。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§5.2 末尾已加入讨论段落。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W2) 列为 Must-Fix。R7-R1 [REBUT]。Director 判定 Should-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (W5) 再次指出 'Blindspot' 术语偏向 attenuation 解释。R8-R2 交叉 AGREE。标题和 Abstract framing 偏颇。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R1 N2 和 R9-R2 N2 均涉及此问题。R9-R1 Q3 直接追问 bootstrap attenuation 如何排除 construct-level 差异。论文 §5.1 已有讨论但 'Blindspot' 术语天然偏向 attenuation 解释。共识：正文讨论已有改善但 Title/Abstract 措辞仍需调整。\"\n\n  - id: \"R5-SF7\"\n    summary: \"Formality confound 在 Abstract/Conclusion 中未与 verbosity 区分\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Abstract 和 Conclusion 中已有 per-axis differentiation。Round 6 未再被提及。\"\n    resolution_round: 6\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点（0.50-0.98）。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Register 是最弱轴，恰是 rewriter identity 最可能影响结论的轴。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Acknowledged as limitation 但未补实验。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7 两位 Reviewer 在 evaluator-producer 讨论中再次确认 register 缺失。已在 Limitations 标注。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1 cross-rewriter 讨论。Register 仍为最高风险轴。\"\n      - round: 9\n        reviewers: [1]\n        note: \"R9-R1 在 evaluator-producer overlap 讨论中确认仍未覆盖 register。Limitations 已承认但无实验数据。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Equivalence bound Delta=15pp 缺外部 justification。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 Should-Fix，R6-R2 同意。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W3) 再次标注 TOST Δ=15pp 过宽。R7-R2 交叉 [AGREE] 但补充论文核心论证不依赖 TOST。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 升级为 Must-Fix (N3)：Δ=15pp 几乎涵盖最小 confirmed bias (+13pp GPT-4o formality)。共识 Must-Fix。\"\n      - round: 9\n        reviewers: [1]\n        note: \"R9-R1 W3: TOST Δ=15pp margin 偏宽，GPT-4o formality 偏差仅约 13pp，15pp margin 接近 target judges 效应量。Claude 仅覆盖 2/3 axes。论文 Appendix G 承认 Δ=10pp underpowered。\"\n    action_items:\n      - round: 7\n        action: \"将 Claude 相关语言从 'equivalence confirmed' / 'no bias' 改为 'failed to detect bias at Δ=15pp precision'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 8\n        action: \"三选一：(a) 增加 Claude n 使 Δ=10pp 有功效；(b) reframe 为 'insufficient evidence for bias'；(c) 报告 n=87 下能 reject 的最小 Δ\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"每个缺失 cell 应在 footnote 或 Appendix 说明原因。\"\n      - round: 6\n        reviewers: [2]\n        note: \"Table 1 第 6 列无 header。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 格式检查确认第 6 列仍无列标题。R7-R1 交叉 [AGREE]。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (W2) 再次指出 Table 1 信息密度过高、可读性差。R8-R1 交叉 AGREE。\"\n      - round: 9\n        reviewers: [1]\n        note: \"R9-R1 W1 Q2: 缺失单元格（'—'）代表什么？Table 1 footnote 已有 'Empty cells: untested benchmark-axis combinations' 但未解释选择哪些组合的理由。\"\n    action_items:\n      - round: 7\n        action: \"Table 1 第 6 列添加列标题（如 'Status' 或 'Finding'）\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"建议颜色 + 线型双重编码。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Figure 2/3 灰度区分问题再次提及。\"\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 (M2) 再次指出 Figure 2 颜色编码在 150 DPI 下辨认困难。\"\n    action_items:\n      - round: 6\n        action: \"Figure 2/3 增加颜色+线型双重编码\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025), Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound (Delta=15pp) 缺乏独立外部 justification\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"需引用外部基准设定 equivalence bound。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3 讨论。TOST Δ=15pp 与 GPT-4o formality +13pp 仅差 2pp。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3/R8 Must-Fix 讨论。\"\n      - round: 9\n        reviewers: [1]\n        note: \"合并入 R5-M3 讨论。R9-R1 W3 再次确认 Δ=15pp 接近 target judges 效应量。\"\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 讨论不充分\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1]\n        note: \"same-style control 只检测 rewriting artifact 但无法检测 axis-specific confounds。\"\n      - round: 7\n        reviewers: []\n        note: \"Round 7 未被显式提及。\"\n      - round: 8\n        reviewers: [1]\n        note: \"R8-R1 在 Detailed Comments §3.5 中再次指出假设(iii)最难验证。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R1 W2: style axis 之间的 interaction/cross-contamination 未测试（formal 改写是否系统性改变 verbosity？）。R9-R2 在 cross-response 中 AGREE。Table 5 GEE interaction test 只检验 Style×Originality 而非 cross-axis interaction。建议对每个 axis 改写样本测量其他 axis 的变化幅度。\"\n    action_items:\n      - round: 6\n        action: \"在 Limitations 补充讨论 axis-specific confounds\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄——n=355 仅限 Qwen3-32B formality\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"LLMBar n=100 为主数据源，MT-Bench n=30。n=355 仅覆盖一个 judge×axis。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W3) 列为 Must-Fix。共识 Should-Fix。\"\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 (W1) 指出仅 3 轴难以支撑 framework 级别泛化。共识 Should-Fix。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R1 W1: NLI filtering 后 n=55-88，cross-benchmark 覆盖不完整。R9-R2 W1: 仅 2+1 axes 限制泛化。交叉后共识 Should-Fix：CSD 方法论 axis-agnostic 但 empirical evidence 仍窄。\"\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"GPT-4o formality/verbosity/register 和 Qwen3 formality Orig OR 只有点估计无 CI。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (Q1) 和 R7-R2 交叉回应均确认 7 个 CI 缺失。必须补全。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。Appendix Table 5 现已有完整 CI（Table tab:gee_ci 12 行均含 CI）。可能已修复。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 检查 Appendix C Table 5 已有完整 12 行 CI。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 7\n        action: \"补全 Appendix Table 5 所有 GEE CI\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"论文 Related Work §2 已引用 Shi et al. (2024) 和 Bavaresco et al. (2025)。\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 7 issues\n  # ============================================================\n\n  - id: \"R7-W2\"\n    summary: \"Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 含 register (8 tests) vs Table 1 标 register 为 exploratory (†_e)\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"明确矛盾，直接影响 Holm-Bonferroni 校正的 adjusted p-values。需统一为 6-test 或 8-test family。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (N1) 列为 Must-Fix：§4.1 声明 'six tests' 但未指明哪三个 judges。如果排除 Gemini 存在 post-hoc cherry-picking 嫌疑。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 检查：§4.1 现在明确 'six tests—three target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B) × two axes (formality, verbosity)—corrected via Holm-Bonferroni'，Gemini 为 confirmatory，Appendix Q 报告 8-test family 下所有结果仍显著。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 7\n        action: \"统一 Section 4.1 primary family 定义与 Table 1 标注\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 8\n        action: \"在 §4.1 明确列出三个 primary judges 名称及排除理由；报告 8-test family 下 adjusted p-values 作为 sensitivity analysis\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R7-W4\"\n    summary: \"NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型（与 rewriter 相同），存在循环性\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W4) 提出。R7-R2 交叉部分同意。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (W3) 独立指出 FNR 基于仅 12 个 rejected pairs（Wilson 95% CI ≈ [2%, 28%]），样本量过小。R8-R2 交叉 AGREE。应报告 CI 而非仅点估计。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 检查：论文 §5.4 第一段报告 'FNR = 8.4% [95% Wilson CI: 3.7%, 15.9%]'。CI 已报告。循环性问题（Qwen3-32B 做 NLI annotator）未在正文讨论——GPT-4o cross-validation (92.1%/82.6%) 部分缓解但非完全解决。\"\n\n  - id: \"R7-W5\"\n    summary: \"Verbosity direction-aware NLI gate GPT-4o validation 显示 17.4% FPR，正文未报告\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R1 (W5) 提出。R7-R2 交叉 [AGREE]。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R1 (W4) 指出 direction-aware gating 额外放入 21 pairs (+32%)，可能引入 selection bias。R8-R2 交叉 AGREE。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未显式提及。Appendix F 已有 direction-aware gate validation data。\"\n\n  - id: \"R7-REF1\"\n    summary: \"遗漏引用：Tripathi et al. (2025) 'Pairwise or Pointwise?'\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: \"论文 §5.1 已引用 Tripathi et al. (2025)。\"\n    resolution_round: 9\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"R7-R2 (W6) 提出。R7-R1 交叉同意。\"\n      - round: 8\n        reviewers: [1]\n        note: \"R8-R1 确认论文 §5.2 已引用 Tripathi et al. (2025)。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 确认 §5.1 含 Tripathi et al. (2025) 引用。已解决。\"\n\n  # ============================================================\n  # Round 8 issues\n  # ============================================================\n\n  - id: \"R8-W1\"\n    summary: \"3 个风格轴限制 'framework' 级别的泛化声明——需从 'framework' 降为 'methodology'\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"仅 formality/verbosity/register 3 轴。共识 Should-Fix：将 'framework' 改为 'methodology'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R2 W1 再次指出 style axis 覆盖过窄。R9-R1 AGREE 方向但认为严重程度为 warning（方法论论文的价值在于通用性而非穷举）。共识：限定 'per-axis confound structure' 为 'preliminary evidence'。\"\n    action_items:\n      - round: 8\n        action: \"在 Contribution 中将 'framework' 改为 'methodology'；Limitations 中列出未覆盖轴\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R8-W2\"\n    summary: \"生态效度（ecological validity）讨论不足——controlled manipulation 到 naturalistic evaluation 的 generalizability gap\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"Limitations 中应增加独立 point。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 检查 Limitations：已有 'Our controlled manipulation design ensures internal validity but may not fully generalize to naturalistic evaluation settings where style and content covary.' 可能已部分处理。\"\n    action_items:\n      - round: 8\n        action: \"在 Limitations 中新增生态效度讨论段落\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R8-W3\"\n    summary: \"Rewriting artifact 的 style-specific polishing interaction 未讨论\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 (W4) 提出。R8-R1 PARTIALLY AGREE。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 检查 Appendix O：已有 'Same-style double-rewrite controls for style-neutral polishing artifacts but cannot exclude style-specific polishing interactions.' 可能已部分处理。\"\n    action_items:\n      - round: 8\n        action: \"在 Limitations 或 Appendix O 中讨论 style-specific polishing interaction 可能性\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R8-W4\"\n    summary: \"Introduction motivating example ('average height') 未 acknowledge formality-quality nuance\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"论文自己的 GEE 结果显示 formality 存在 significant Originality effect。Introduction 应 acknowledge。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 检查 §1：motivating example 后有 'We note that formality preferences may partially reflect legitimate quality judgments—our GEE decomposition (§5.2) quantifies this originality component.' 已处理。\"\n\n  - id: \"R8-REF1\"\n    summary: \"建议补充引用：Girrbach et al. (2025/2026) 'Likert or Not'\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [2]\n        note: \"R8-R2 建议。R8-R1 PARTIALLY AGREE，需验证文献真实性。\"\n\n  # ============================================================\n  # Round 9 new issues\n  # ============================================================\n\n  - id: \"R9-N1\"\n    summary: \"100-point continuous Likert 实验仅用单一 judge（Qwen3-32B），泛化性不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R2 W3 提出，R9-R1 交叉 AGREE。Appendix M 100-point Likert 仅 Qwen3-32B，如果 GPT-4o 在 100-point scale 下 ATE 变显著则 Blindspot 对某些 judge 可能确是粒度问题。建议至少增加 GPT-4o 作为第二个 judge。\"\n\n  - id: \"R9-N2\"\n    summary: \"NLI gate 44% 拒绝率的 selection bias 特征分析不足——仅检查 4 个 surface covariates\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-R2 W2 提出，R9-R1 交叉 AGREE。Appendix B 报告 4 covariates 无差异（NLI score, BERTScore, text length, length diff），但未检查语言复杂度、论证结构、话题类型等深层特征。Filtered-in pairs 可能系统性偏向内容更简单的文本，影响 external validity。\"\n\n  - id: \"R9-REF1\"\n    summary: \"建议补充引用：IRT 在 LLM 评估中的应用（Polo et al. 2024, Otani et al. 2023）、Kocmi & Federmann (2023)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 9\n        reviewers: [2]\n        note: \"R9-R2 建议补充 IRT 文献（Polo et al. 2024 tinyBenchmarks, Otani et al. 2023）和 Kocmi & Federmann (2023) LLM judge multilingual bias。另建议补充 Simms et al. (2019) rating scale granularity 和 Funke (2016) response format effects。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-22T09:33:11.568128+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 46625}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---
