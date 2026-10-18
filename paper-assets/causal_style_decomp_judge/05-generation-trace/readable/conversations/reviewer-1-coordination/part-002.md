# Reviewer 1 coordination — Part 2 of 3

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-1-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/d5/d51689b3494032df15ac.json)

## Round 18

### User

_source line 541 · 2026-05-21T21:19:24.816044+00:00_

[Round 1 审稿请求]:
以下是 **Reviewer 2** 的完整审稿意见（侧重新颖性 + 完整性 + 写作质量）。请逐条回应其 Weaknesses 和 Questions：对每条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

### 总体评分
Overall: 3.5 (Borderline Conference)
一句话总结: 扎实的实证研究，令人信服地展示了 Likert 和 pairwise 在检测 LLM judge 风格偏差上的敏感度差异，但核心发现的新颖性受限于经典心理测量学已有的理论预测，且论文框架存在系统性的过度声明。

### Strengths
S1: 系统性实验设计和严谨统计分析（Holm-Bonferroni, 7 methods, 11 thresholds, bootstrap attenuation, n=355 replication）
S2: 多维度鲁棒性验证（rewriter independence, NLI ablation, cross-judge, cross-benchmark, negative control, 100-point scale）
S3: GEE per-axis confound structure 是最具原创性贡献
S4: Claude Sonnet 4 负对照增强辨别效度
S5: Limitations 坦诚讨论 construct divergence 和 evaluator-producer bias

### Must-Fix
**W1 [critical]** "The first framework" 声明过度——通过组合限定词构造唯一性。RATE/Qiu/CASSE/FairJudge 各覆盖核心组件。建议改为 "a unified framework"。
**W2 [critical]** "Likert Blindspot" 框架偏颇——construct divergence 替代假说被系统性弱化。Tripathi et al. (2025) 发现 pairwise 更容易被 distractor 操纵（flip rate 35% vs 9%），挑战 pairwise 作为 ground truth 的隐含假设。
**W3 [critical]** 基准多样性不足——主要在 LLMBar n=100，跨 benchmark 仅覆盖少数配置，全部英文单轮对话，n≤355 不足以支撑 "systematic"。

### Should-Fix
**W4 [warning]** Abstract 信息密度过高（7 句 4 组统计括号）
**W5 [warning]** Evaluator-producer bias 处理不充分（register 完全缺 rewriter independence）
**W6 [warning]** 遗漏关键近期文献：Tripathi et al. (2025), Li et al. (2026), "Fairness or Fluency?"
**W7 [warning]** 对 Thurstone (1927) 理论关系定位不清——核心发现可从近百年前理论直接预测

### Questions
Q1: 100-point 连续尺度高 tie rate (51-66%) 是否说明 LLM judge 对 style 变化不敏感（而非工具缺陷）？
Q2: AlpacaEval verbosity (Likert d=0.375, BT=84.1%) 两者均显著——Blindspot 仅在 moderate effect sizes 时存在？
Q3: Position-swap 后 inconsistent pair 比例？是否接近 Tripathi et al. 35% flip rate？
Q4: 不同 rewriter (如 Llama-70B) 下 GEE confound structure 是否保持？

### Missing References
1. Tripathi et al. (2025) "Pairwise or Pointwise?" arXiv:2504.14716
2. Li et al. (2026) "Grading Scale Impact on LLM-as-a-Judge" arXiv:2601.03444
3. "Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory" arXiv:2602.00521

### Format
- ✅ 主正文 8 页 / Limitations 存在 / 匿名 / natbib
- ⚠️ Table 1 第 6 列无列标题
- ⚠️ inconsolata 被注释掉

---

请对以上 W1-W7 和 Q1-Q4 逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-21T21:19:38.400067+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-21T21:19:38.851866+00:00_

1	\begin{abstract}
2	LLM judges are widely deployed for evaluation and alignment, yet style features alone explain judge scores with near-perfect correlation.
3	We introduce Controlled Style Decomposition (CSD), the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison to systematically quantify style bias in LLM judges.
4	Across three target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B) and one negative control (Claude Sonnet 4), three benchmarks, and three style axes, CSD demonstrates the Likert Blindspot: Likert scoring systematically misses style biases that pairwise comparison detects (BT 63--84\%, $p < 0.001$), following a severity spectrum---complete at moderate bias ($d \to 0$ at $n = 355$), exceeding 60\% attenuation at stronger effects---confirmed by seven statistical methods.
5	GEE conditional decomposition demonstrates a per-axis confound structure consistent across all three target judges: verbosity bias is style-dominated, formality exhibits a conditional effect moderated by content quality changes, and register is judge-dependent (originality-dominated to mixed)---determining which estimates are directly interpretable and which require conditional analysis.
6	A fourth judge (Claude Sonnet 4) detects no bias on either axis, supporting discriminative validity.
7	We identify two candidate interpretations---measurement attenuation and construct divergence---and show that both yield the same operational conclusion: Likert-only evaluation systematically misses style-driven preferences that propagate through pairwise-based alignment pipelines.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-21T21:19:38.852352+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-21T21:19:39.354572+00:00_

1	\section{Introduction}
2	
3	LLM judges are central infrastructure for NLP evaluation (AlpacaEval, MT-Bench, Chatbot Arena) and alignment training (RLHF, DPO), where judge-generated preferences serve as reward signals.
4	Any systematic bias in their assessments propagates through both evaluation leaderboards and model development pipelines.
5	
6	Recent work suggests that style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}, motivating systematic measurement of per-axis style bias.
7	\citet{li2026preference} demonstrate that 76--92\% of observed preference signals originate from surface-level style cues rather than substantive quality differences, and \citet{soumik2026judging} report bias scores of 0.76--0.92 across five different judges.
8	Despite this consensus on severity, existing approaches each address individual requirements: CASSE \citep{casse2026concise} and FairJudge \citep{wang2026fairjudge} provide multi-dimensional style analysis, RATE \citep{reber2025rate} introduces interventional design, and length-controlled AlpacaEval \citep{dubois2025lc} offers population-level correction.
9	However, no single framework integrates all four requirements---per-axis decomposition, interventional identification, per-instance diagnostics, and black-box applicability.
10	A further concern compounds these limitations: standard Likert scoring suffers from a measurement efficiency gap---integer discretization produces ${\sim}60\%$ uninformative ties, and even non-tied pairs carry weaker signal than pairwise comparison---a limitation predicted by measurement theory \citep{thurstone1927law} but previously unquantified for LLM judges.
11	
12	We propose Controlled Style Decomposition (CSD), the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison to systematically quantify style bias in LLM judges.
13	Inspired by interventional approaches to text analysis \citep{vei
…[truncated 3128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-21T21:19:39.757133+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
  "offset": "84",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
    "offset": "84",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-21T21:19:39.859571+00:00_

84	
85	\subsection{Measurement Sensitivity: Likert vs.\ Pairwise}
86	\label{sec:likert_pairwise}
87	
88	\paragraph{Head-to-head comparison with RATE.}
89	Applying RATE's Likert ATE methodology \citep{reber2025rate} to our formality style-transformed pairs yields Cohen's $d = 0.10$, $p = 0.33$ (non-significant, $n = 88$); pairwise comparison on identical data reveals a 63.0\% formal preference ($p = 0.0004$, Bradley-Terry on all 173 comparisons), confirmed by a consistency-filtered sign test (73.9\%, $p = 0.006$, $n = 46$ consistent pairs).
90	This is the Likert Blindspot: the same data, the same style intervention, two measurement instruments---one detects bias, the other does not.
91	A $4\times$ scaled replication ($n = 355$) distinguishes measurement attenuation from insufficient power: the Likert effect size shrinks to $d = {-}0.025$ (near zero) while BT remains stable at $67.5\%$ ($p < 0.0001$)---if the gap were merely statistical power, $d$ would remain non-zero at larger $n$.
92	Bootstrap subsampling across seven sample sizes confirms this pattern: $d$ remains flat near zero ($d_{\text{median}} = {-}0.017$) as CIs narrow from ${\pm}0.3$ to ${\pm}0.1$, never excluding zero (Appendix~\ref{app:bootstrap_attenuation}).
93	Attenuation follows a severity spectrum.
94	At moderate bias (BT 63--67\%), it is complete: $d$ converges to ${\approx}0$ even at $n = 355$, rendering the bias invisible to any Likert-based test.
95	At stronger effects (BT ${>}70\%$), Likert partially detects but severely attenuates: MT-Bench formality yields Likert $d \approx 0.15$ for BT ${\sim}70\%$ effects---${>}60\%$ signal compression---explaining why three of eleven bias-positive cells escape the Blindspot (Table~\ref{tab:main_results}, $\ddagger$ rows).
96	
97	The two frameworks are complementary: RATE measures aggregate quality effects via Likert ATE; CSD targets per-axis style preference via forced-choice comparison, which eliminates ties and is more sensitive to ordinal preferences.
98
…[truncated 4696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-21T21:19:47.990330+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
  "offset": "144",
  "limit": "65"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
    "offset": "144",
    "limit": "65"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-21T21:19:48.442557+00:00_

144	\end{figure}
145	
146	\subsection{Cross-Judge Replication}
147	\label{sec:cross_judge}
148	
149	Two independent judges replicate the Blindspot: Qwen3-32B (BT 66.5\%, $p < 0.0001$; Likert $p = 0.908$) and Llama-3.3-70B (BT 69.5\%, $p = 0.0001$; Likert $p = 0.846$), spanning three architectures (proprietary API, open 32B, open 70B).
150	Qwen3-32B's higher GEE estimate may partly reflect evaluator-producer bias (Appendix~\ref{app:rewriter_indep}).
151	
152	\subsection{Cross-Axis Replication: Verbosity}
153	\label{sec:cross_axis}
154	
155	The verbosity axis provides the strongest and cleanest demonstration of the Blindspot.
156	All three target judges show consistent verbosity preference: GPT-4o 76.0\% ($p = 0.0001$), Qwen3-32B 77.3\% ($p < 0.0001$), and Llama-70B 73.5\% ($p = 0.0001$), while Likert ATE remains non-significant for all three ($p = 0.403$, $0.179$, $0.752$).
157	Unlike formality, verbosity is style-dominated across all three judges: GEE decomposition confirms massive style effects (OR $= 8.2$--$13.1$, all $p < .0001$) while originality ORs are below 1 ($0.38$--$0.49$)---though Llama-70B's is the only significant one (OR $= 0.38$, $p = .020$)---indicating any artifact favors rewrites over originals rather than reflecting quality confounding (Table~\ref{tab:gee}).
158	Both rewriting directions favor verbose responses (concise$\to$verbose 90.7\%, verbose$\to$concise 80.6\%); controlling for length leaves the style OR unchanged ($<$2\%), and an independent GPT-4o rewriter bounds evaluator-producer inflation to $22\%$ (Style OR $13.10 \to 10.17$; Appendix~\ref{app:rewriter_indep}).
159	
160	\subsection{Register: Judge-Dependent Confound Structure}
161	\label{sec:negative_control}
162	
163	Register shows judge-dependent heterogeneity: Llama-70B BT 63.5\% ($p = 0.0014$), GPT-4o 57.0\% ($p = 0.04$), Qwen3-32B n.s.\ (55.3\%); all Likert n.s.
164	GEE confirms varying confound structure---Qwen3-32B originality-dominated, GPT-4o and Llama-70B mixed (Table~\ref{ta
…[truncated 3583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-21T21:19:48.543625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "offset": "17",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
    "offset": "17",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-21T21:19:48.644246+00:00_

17	
18	\section{Consistency Filter Robustness}
19	\label{sec:consistency}
20	
21	The position-consistency filter retains 55 of 98 valid pairs (56.1\%); consistent and inconsistent groups show no significant differences across four covariates (NLI score $p = 0.824$, BERTScore $p = 0.12$, text length $p = 0.137$, length diff $p = 0.715$), indicating selection on judge decisiveness rather than text properties.
22	The BT model using all 173 comparisons including inconsistent pairs yields 63.0\% ($p = 0.0004$), consistent with the filtered sign test (73.9\%, $p = 0.006$), confirming no systematic bias from the filter.
23	
24	\section{GEE Model Diagnostics}
25	\label{app:gee_diagnostics}
26	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-21T21:21:34.835072+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### Weaknesses\n\n**[AGREE] R2-W1: \"The first framework\" 声明过度**\n同意 R2 的判断。Abstract line 3 和 Introduction line 12 均使用\"the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison\"——通过组合多个限定词构造 novelty claim 是 ACL 审稿中经常被质疑的做法。虽然该具体组合确实在已有文献中未出现（RATE 用 Likert ATE、CASSE/FairJudge 无 interventional control、Qiu et al. 在 persona 层面操作），但\"first\"的措辞暗示了比实际更高的原创性。改为\"a unified framework\"或\"a framework that integrates\"更准确且不影响论文实质贡献。\n\n**[REBUT] R2-W2: \"Likert Blindspot\" 框架偏颇——construct divergence 被系统性弱化**\n不同意 R2 的核心判断，但同意部分论据有价值。\n\n论文并未系统性弱化 construct divergence。Section 5.2（lines 130–132）明确陈述：\"An equally plausible interpretation is that Likert and pairwise modes measure different constructs—absolute quality vs. ordinal preference—making the divergence a construct difference rather than measurement failure. Both interpretations lead to the same conclusion.\" Abstract line 7 同样并列两种解释：\"We identify two candidate interpretations—measurement attenuation and construct divergence—and show that both yield the same operational conclusion.\" Contribution #2（Introduction line 21）使用\"Whether this reflects measurement attenuation or construct divergence, the operational consequence is identical.\"\n\n这不是弱化，而是 agnosticism + operational equivalence 的论证策略——无论哪种解释成立，Likert-only audits 都会遗漏 pairwise-based alignment pipeline 中的 style-driven preferences。\n\n关于 Tripathi et al. (2025) 的论据：pairwise 的 35% flip rate（vs. pointwise 9%）确实表明 pairwise 对 distractor 更敏感。但这与本文的发现不矛盾——CSD 的 6 项 amplification controls（Section 5.2, Detection vs. amplification: NLI ablation 反转、Claude negative control、cross-axis variation、GEE artifact absorption、debiased prompting、cross-architecture consistency）专门针对这一问题。特别是 control (ii) Claude Sonnet 4 在相同 pairwise format 下不检测到 bias（BT 56.2%/54.1%, n.s.），说明 pairwise format 本身不 uniformly amplify style preferences。\n\n**建议**：Tripathi et al. (2025) 确实应该被引用和讨论——但作为对 amplification risk 的补充证据（与 Jeong et al. 2025 Comparative Trap 并列），而非对 Blindspot 的否定。\n\n**[AGREE] R2-W3: 基准多样性不足**\n同意这是论文的合理局限。LLMBar n=100 是主实验基础，cross-benchmark 仅覆盖部分配置（AlpacaEval 3/9, MT-Bench 2/9），全部英文单轮对话。论文在 Conclusion（Section 6, line 10）承认了这一点：\"Our findings are established on English benchmarks with n ≤ 355; validation on larger corpora, additional languages, and emerging judge architectures remains necessary.\"\n\n但\"systematic\"一词的使用需要辩护：论文的\"systematic\"指的是方法论的系统性（per-axis decomposition + content control + position control），而非数据规模。在当前数据范围内，8/11 bias-positive cells 展示 Blindspot，跨 3 个 benchmark、3 个架构、3 个 style axis——这在 LLM judge bias 文献中已属较高覆盖度。但 R2 的批评在更广义的 generalization claim 层面是成立的：n ≤ 355 在绝对规模上确实有限。\n\n**[AGREE] R2-W4: Abstract 信息密度过高**\n同意。Abstract（lines 2–7）在 7 句内包含 BT 百分比范围、p-value、Cohen's d、n=355、七种统计方法、三个 judge、三个 benchmark、三个 style axis——对首次阅读的读者构成认知负担。建议将具体统计数字移至 Introduction，Abstract 聚焦于定性结论和核心 message。这是写作质量问题，不影响技术贡献。\n\n**[AGREE] R2-W5: Evaluator-producer bias 处理不充分（register 完全缺 rewriter independence）**\n同意，且此问题与我作为 R1 提出的 W1 一致。Cross-rewriter validation（Appendix D）仅覆盖 formality + verbosity 对 Qwen3-32B judge 的配置，register 轴完全缺失，GPT-4o 和 Llama-70B 作为 judge 时也缺失。这是 identification 层面的关键缺陷。\n\n**[REBUT] R2-W6: 遗漏关键近期文献**\n部分同意，部分反驳。\n\n- **Tripathi et al. (2025)**: 同意应引用。如上述 W2 回应所述，该文对 pairwise amplification 提供了重要证据，应在 Section 5.2 的 Detection vs. amplification 段落中与 Jeong et al. (2025) 并列讨论。\n- **Li et al. (2026) \"Grading Scale Impact\"**: 同意应引用。该文研究评分尺度对 LLM judge 的影响，与 Likert Blindspot 的 scale granularity 讨论（100-point scale, Appendix M）直接相关。\n- **\"Fairness or Fluency?\"**: R2 未给出完整引用信息。如果是指特定的 style-fairness trade-off 论文，需要确认具体文献后再判断。\n\n但需要指出：论文的 Related Work（Section 2）已相当全面，覆盖了 Thurstone (1927)、Stevens (1946)、Kiritchenko & Mohammad (2017)、Novikova et al. (2018)、Jeong et al. (2025) 等关键 measurement sensitivity 文献。遗漏 2–3 篇并非\"系统性遗漏\"。\n\n**[REBUT] R2-W7: 对 Thurstone (1927) 理论关系定位不清——核心发现可从近百年前理论直接预测**\n不同意这一批评的核心论断。\n\n论文在 Introduction line 10 已明确标注理论渊源：\"a limitation predicted by measurement theory (Thurstone, 1927) but previously unquantified for LLM judges.\" 这不是定位不清，而是清晰的 positioning：理论预测 ≠ 经验量化。\n\n更具体地说，Thurstone (1927) 预测 pairwise comparison 具有更高 discriminability，但未预测（也无法预测）：\n1. **Severity spectrum** 的具体形态——moderate bias 下完全失灵（d → 0 at n=355）vs. stronger effects 下 >60% 衰减\n2. **Tie rate mechanism**——58–73% ties 在 10-point AND 100-point scale 上同时出现，将 Blindspot 归因于 absolute vs. relative evaluation paradigm 而非 scale granularity\n3. **Per-axis confound structure** 对 measurement sensitivity 的交互作用——verbosity（style-dominated）在 LLMBar 上有 Blindspot 但 AlpacaEval 上没有（BT 84.1%, d=0.375），这种效应量依赖的 threshold behavior 是全新的经验发现\n\n类比：Newton 预测了苹果会掉落，但精确测量 g=9.81 m/s² 仍然是有价值的物理学贡献。本文的贡献不在于\"pairwise 比 Likert 灵敏\"这一定性结论，而在于量化了何时、多大程度、以何种机制。\n\n---\n\n### Questions\n\n**[AGREE with nuance] R2-Q1: 100-point 连续尺度高 tie rate 是否说明 LLM judge 对 style 变化不敏感（而非工具缺陷）？**\n这是一个好问题，但答案需要区分两种情况。100-point scale 的 tie rate（formality 65.9%, verbosity 51.2%, Appendix M Table 13）确实可能反映 LLM judge 在 absolute evaluation mode 下对 style 差异的不敏感性——即 judge 在独立评分时不会因为 formality 差异而给出不同分数。但同一个 judge 在 pairwise mode 下明确偏好 formal/verbose variants（BT 66.5%/77.3%, p < 0.0001）。这支持 construct divergence 解释：绝对评分和相对偏好测量的是不同 construct，而非\"工具缺陷\"。论文在 Section 5.2 line 131 已承认这一点。R2 的观察实际上强化了论文的 operational conclusion——如果 Likert insensitivity 反映的是 judge 的内在行为模式而非测量工具问题，那更说明 pairwise-based alignment pipeline 捕捉到的偏好是 Likert-based audit 无法触及的。\n\n**[AGREE] R2-Q2: AlpacaEval verbosity (Likert d=0.375, BT=84.1%) 两者均显著——Blindspot 仅在 moderate effect sizes 时存在？**\n是的，论文已明确承认这一点。Section 5.6 line 203 报告：\"the same verbosity axis yields a Blindspot on LLMBar (BT 77.3%, Likert n.s.) but not on AlpacaEval (BT 84.1%, d = 0.41), demonstrating a measurement sensitivity boundary rather than a methodological artifact.\" Table 1 的 $\\ddagger$ 行标记了三个 Blindspot 不成立的 cells（BT > 69%, Likert d ≥ 0.14）。Section 5.2 lines 93–95 将此描述为 \"severity spectrum\"——moderate bias 下完全失灵，stronger effects 下部分衰减。论文的处理是 transparent 的，但 R2 的问题提示 Abstract 和 Conclusion 中的措辞可以更明确地限定 Blindspot 的适用条件（effect-size dependent），而非暗示它是 universal 的。\n\n**[AGREE with data] R2-Q3: Position-swap 后 inconsistent pair 比例？是否接近 Tripathi et al. 35% flip rate？**\nAppendix B（Section B, line 21）报告 position-consistency filter retains 55 of 98 valid pairs (56.1%)，即 inconsistent pair 比例为 43/98 = **43.9%**。这高于 Tripathi et al. 的 35% flip rate。但两个数字不直接可比：Tripathi 的 flip rate 来自不同实验设计（distractor manipulation），而本文的 inconsistency 来自 position swap（同一对文本交换顺序后 judge 改变选择）。43.9% 的 inconsistency rate 确实较高，可能反映 (a) position bias（论文的 position swap 旨在控制这一点），(b) style 差异处于 judge 的决策边界附近（近 50% 的 pairs 让 judge 犹豫不决）。论文应在正文中报告和讨论此数字（目前仅在 Appendix B），因为它影响对 BT model 可靠性的判断。\n\n**[AGREE] R2-Q4: 不同 rewriter (如 Llama-70B) 下 GEE confound structure 是否保持？**\n论文未测试此配置。Cross-rewriter validation（Appendix D）仅将 Qwen3-32B 替换为 GPT-4o，且仅对 Qwen3-32B judge。用 Llama-70B 作 rewriter 的数据不存在。这与我作为 R1 的 W1 一致——evaluator-producer confound 的控制覆盖面不足。GEE confound structure 的 cross-rewriter stability 是重要的 open question。\n\n---\n\n### Format Issues\n\n**[AGREE] Table 1 第 6 列无列标题**\n确认。Table 1（Section 4, experiments.tex lines 20–53）的第 6 列包含 Blindspot 分类符号（†, ‡, ---, †_e）但缺少列标题。建议添加\"Status\"或\"Finding\"列标题。\n\n**[AGREE] inconsolata 被注释掉**\n这是排版细节，不影响内容，但建议在最终版本中恢复或移除相关代码。\n\n---\n\n### 总结\n\nR2 的审稿整体质量较高。其最有力的论点是 W2 中关于 Tripathi et al. (2025) 的引入——pairwise 的 higher flip rate 对 CSD 框架构成了需要正面回应的挑战（尽管论文的 6 项 amplification controls 已部分 address）。W7 关于 Thurstone 定位的批评我认为论文已有合理回应（Introduction line 10 明确标注\"predicted but unquantified\"），但 R2 的视角提示论文可以更强调经验量化的具体贡献（severity spectrum, tie rate mechanism, per-axis interaction）而非重复\"first\"的 framing。\n\n与我作为 R1 的评估一致的核心问题：evaluator-producer confound（R1-W1 ≈ R2-W5）和基准多样性（R2-W3 是合理关切）。两位 reviewer 的 Must-Fix 问题有实质重叠，提示这些确实是影响接收决定的关键问题。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### Weaknesses\n\n**[AGREE] R2-W1: \"The first framework\" 声明过度**\n同意 R2 的判断。Abstract line 3 和 Introduction line 12 均使用\"the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison\"——通过组合多个限定词构造 novelty claim 是 ACL 审稿中经常被质疑的做法。虽然该具体组合确实在已有文献中未出现（RATE 用 Likert ATE、CASSE/FairJudge 无 interventional control、Qiu et al. 在 persona 层面操作），但\"first\"的措辞暗示了比实际更高的原创性。改为\"a unified framework\"或\"a framework that integrates\"更准确且不影响论文实质贡献。\n\n**[REBUT] R2-W2: \"Likert Blindspot\" 框架偏颇——construct divergence 被系统性弱化**\n不同意 R2 的核心判断，但同意部分论据有价值。\n\n论文并未系统性弱化 construct divergence。Section 5.2（lines 130–132）明确陈述：\"An equally plausible interpretation is that Likert and pairwise modes measure different constructs—absolute quality vs. ordinal preference—making the divergence a construct difference rather than measurement failure. Both interpretations lead to the same conclusion.\" Abstract line 7 同样并列两种解释：\"We identify two candidate interpretations—measurement attenuation and construct divergence—and show that both yield the same operational conclusion.\" Contribution #2（Introduction line 21）使用\"Whether this reflects measurement attenuation or construct divergence, the operational consequence is identical.\"\n\n这不是弱化，而是 agnosticism + operational equivalence 的论证策略——无论哪种解释成立，Likert-only audits 都会遗漏 pairwise-based alignment pipeline 中的 style-driven preferences。\n\n关于 Tripathi et al. (2025) 的论据：pairwise 的 35% flip rate（vs. pointwise 9%）确实表明 pairwise 对 distractor 更敏感。但这与本文的发现不矛盾——CSD 的 6 项 amplification controls（Section 5.2, Detection vs. amplification: NLI ablation 反转、Claude negative control、cross-axis variation、GEE artifact absorption、debiased prompting、cross-architecture consistency）专门针对这一问题。特别是 control (ii) Claude Sonnet 4 在相同 pairwise format 下不检测到 bias（BT 56.2%/54.1%, n.s.），说明 pairwise format 本身不 uniformly amplify style preferences。\n\n**建议**：Tripathi et al. (2025) 确实应该被引用和讨论——但作为对 amplification risk 的补充证据（与 Jeong et al. 2025 Comparative Trap 并列），而非对 Blindspot 的否定。\n\n**[AGREE] R2-W3: 基准多样性不足**\n同意这是论文的合理局限。LLMBar n=100 是主实验基础，cross-benchmark 仅覆盖部分配置（AlpacaEval 3/9, MT-Bench 2/9），全部英文单轮对话。论文在 Conclusion（Section 6, line 10）承认了这一点：\"Our findings are established on English benchmarks with n ≤ 355; validation on larger corpora, additional languages, and emerging judge architectures remains necessary.\"\n\n但\"systematic\"一词的使用需要辩护：论文的\"systematic\"指的是方法论的系统性（per-axis decomposition + content control + position control），而非数据规模。在当前数据范围内，8/11 bias-positive cells 展示 Blindspot，跨 3 个 benchmark、3 个架构、3 个 style axis——这在 LLM judge bias 文献中已属较高覆盖度。但 R2 的批评在更广义的 generalization claim 层面是成立的：n ≤ 355 在绝对规模上确实有限。\n\n**[AGREE] R2-W4: Abstract 信息密度过高**\n同意。Abstract（lines 2–7）在 7 句内包含 BT 百分比范围、p-value、Cohen's d、n=355、七种统计方法、三个 judge、三个 benchmark、三个 style axis——对首次阅读的读者构成认知负担。建议将具体统计数字移至 Introduction，Abstract 聚焦于定性结论和核心 message。这是写作质量问题，不影响技术贡献。\n\n**[AGREE] R2-W5: Evaluator-producer bias 处理不充分（register 完全缺 rewriter independence）**\n同意，且此问题与我作为 R1 提出的 W1 一致。Cross-rewriter validation（Appendix D）仅覆盖 formality + verbosity 对 Qwen3-32B judge 的配置，register 轴完全缺失，GPT-4o 和 Llama-70B 作为 judge 时也缺失。这是 identification 层面的关键缺陷。\n\n**[REBUT] R2-W6: 遗漏关键近期文献**\n部分同意，部分反驳。\n\n- **Tripathi et al. (2025)**: 同意应引用。如上述 W2 回应所述，该文对 pairwise amplification 提供了重要证据，应在 Section 5.2 的 Detection vs. amplification 段落中与 Jeong et al. (2025) 并列讨论。\n- **Li et al. (2026) \"Grading Scale Impact\"**: 同意应引用。该文研究评分尺度对 LLM judge 的影响，与 Likert Blindspot 的 scale granularity 讨论（100-point scale, Appendix M）直接相关。\n- **\"Fairness or Fluency?\"**: R2 未给出完整引用信息。如果是指特定的 style-fairness trade-off 论文，需要确认具体文献后再判断。\n\n但需要指出：论文的 Related Work（Section 2）已相当全面，覆盖了 Thurstone (1927)、Stevens (1946)、Kiritchenko & Mohammad (2017)、Novikova et al. (2018)、Jeong et al. (2025) 等关键 measurement sensitivity 文献。遗漏 2–3 篇并非\"系统性遗漏\"。\n\n**[REBUT] R2-W7: 对 Thurstone (1927) 理论关系定位不清——核心发现可从近百年前理论直接预测**\n不同意这一批评的核心论断。\n\n论文在 Introduction line 10 已明确标注理论渊源：\"a limitation predicted by measurement theory (Thurstone, 1927) but previously unquantified for LLM judges.\" 这不是定位不清，而是清晰的 positioning：理论预测 ≠ 经验量化。\n\n更具体地说，Thurstone (1927) 预测 pairwise comparison 具有更高 discriminability，但未预测（也无法预测）：\n1. **Severity spectrum** 的具体形态——moderate bias 下完全失灵（d → 0 at n=355）vs. stronger effects 下 >60% 衰减\n2. **Tie rate mechanism**——58–73% ties 在 10-point AND 100-point scale 上同时出现，将 Blindspot 归因于 absolute vs. relative evaluation paradigm 而非 scale granularity\n3. **Per-axis confound structure** 对 measurement sensitivity 的交互作用——verbosity（style-dominated）在 LLMBar 上有 Blindspot 但 AlpacaEval 上没有（BT 84.1%, d=0.375），这种效应量依赖的 threshold behavior 是全新的经验发现\n\n类比：Newton 预测了苹果会掉落，但精确测量 g=9.81 m/s² 仍然是有价值的物理学贡献。本文的贡献不在于\"pairwise 比 Likert 灵敏\"这一定性结论，而在于量化了何时、多大程度、以何种机制。\n\n---\n\n### Questions\n\n**[AGREE with nuance] R2-Q1: 100-point 连续尺度高 tie rate 是否说明 LLM judge 对 style 变化不敏感（而非工具缺陷）？**\n这是一个好问题，但答案需要区分两种情况。100-point scale 的 tie rate（formality 65.9%, verbosity 51.2%, Appendix M Table 13）确实可能反映 LLM judge 在 absolute evaluation mode 下对 style 差异的不敏感性——即 judge 在独立评分时不会因为 formality 差异而给出不同分数。但同一个 judge 在 pairwise mode 下明确偏好 formal/verbose variants（BT 66.5%/77.3%, p < 0.0001）。这支持 construct divergence 解释：绝对评分和相对偏好测量的是不同 construct，而非\"工具缺陷\"。论文在 Section 5.2 line 131 已承认这一点。R2 的观察实际上强化了论文的 operational conclusion——如果 Likert insensitivity 反映的是 judge 的内在行为模式而非测量工具问题，那更说明 pairwise-based alignment pipeline 捕捉到的偏好是 Likert-based audit 无法触及的。\n\n**[AGREE] R2-Q2: AlpacaEval verbosity (Likert d=0.375, BT=84.1%) 两者均显著——Blindspot 仅在 moderate effect sizes 时存在？**\n是的，论文已明确承认这一点。Section 5.6 line 203 报告：\"the same verbosity axis yields a Blindspot on LLMBar (BT 77.3%, Likert n.s.) but not on AlpacaEval (BT 84.1%, d = 0.41), demonstrating a measurement sensitivity boundary rather than a methodological artifact.\" Table 1 的 $\\ddagger$ 行标记了三个 Blindspot 不成立的 cells（BT > 69%, Likert d ≥ 0.14）。Section 5.2 lines 93–95 将此描述为 \"severity spectrum\"——moderate bias 下完全失灵，stronger effects 下部分衰减。论文的处理是 transparent 的，但 R2 的问题提示 Abstract 和 Conclusion 中的措辞可以更明确地限定 Blindspot 的适用条件（effect-size dependent），而非暗示它是 universal 的。\n\n**[AGREE with data] R2-Q3: Position-swap 后 inconsistent pair 比例？是否接近 Tripathi et al. 35% flip rate？**\nAppendix B（Section B, line 21）报告 position-consistency filter retains 55 of 98 valid pairs (56.1%)，即 inconsistent pair 比例为 43/98 = **43.9%**。这高于 Tripathi et al. 的 35% flip rate。但两个数字不直接可比：Tripathi 的 flip rate 来自不同实验设计（distractor manipulation），而本文的 inconsistency 来自 position swap（同一对文本交换顺序后 judge 改变选择）。43.9% 的 inconsistency rate 确实较高，可能反映 (a) position bias（论文的 position swap 旨在控制这一点），(b) style 差异处于 judge 的决策边界附近（近 50% 的 pairs 让 judge 犹豫不决）。论文应在正文中报告和讨论此数字（目前仅在 Appendix B），因为它影响对 BT model 可靠性的判断。\n\n**[AGREE] R2-Q4: 不同 rewriter (如 Llama-70B) 下 GEE confound structure 是否保持？**\n论文未测试此配置。Cross-rewriter validation（Appendix D）仅将 Qwen3-32B 替换为 GPT-4o，且仅对 Qwen3-32B judge。用 Llama-70B 作 rewriter 的数据不存在。这与我作为 R1 的 W1 一致——evaluator-producer confound 的控制覆盖面不足。GEE confound structure 的 cross-rewriter stability 是重要的 open question。\n\n---\n\n### Format Issues\n\n**[AGREE] Table 1 第 6 列无列标题**\n确认。Table 1（Section 4, experiments.tex lines 20–53）的第 6 列包含 Blindspot 分类符号（†, ‡, ---, †_e）但缺少列标题。建议添加\"Status\"或\"Finding\"列标题。\n\n**[AGREE] inconsolata 被注释掉**\n这是排版细节，不影响内容，但建议在最终版本中恢复或移除相关代码。\n\n---\n\n### 总结\n\nR2 的审稿整体质量较高。其最有力的论点是 W2 中关于 Tripathi et al. (2025) 的引入——pairwise 的 higher flip rate 对 CSD 框架构成了需要正面回应的挑战（尽管论文的 6 项 amplification controls 已部分 address）。W7 关于 Thurstone 定位的批评我认为论文已有合理回应（Introduction line 10 明确标注\"predicted but unquantified\"），但 R2 的视角提示论文可以更强调经验量化的具体贡献（severity spectrum, tie rate mechanism, per-axis interaction）而非重复\"first\"的 framing。\n\n与我作为 R1 的评估一致的核心问题：evaluator-producer confound（R1-W1 ≈ R2-W5）和基准多样性（R2-W3 是合理关切）。两位 reviewer 的 Must-Fix 问题有实质重叠，提示这些确实是影响接收决定的关键问题。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-21T21:21:38.449635+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3614
}
```

</details>

---


### Assistant

_source line 554 · 2026-05-21T21:21:49.350063+00:00_

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
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 19

## Round 19

52 recorded events


### User

_source line 555 · 2026-05-22T03:24:53.974947+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性与实验设计**审查。

## Venue 信息
- **目标**: EMNLP 2026 Main Conference (Long Paper via ARR)
- **截止日期**: 2026-05-25
- **页数限制**: 正文 ≤8 页，参考文献不限页数。Limitations 和 Ethics 不计入页数限制（但不能含过多额外内容）。
- **模板**: ACL 双栏格式 (`\usepackage[review]{acl}`)
- **匿名**: Double-blind（作者信息应匿名）
- **Checklist**: ARR Responsible NLP Checklist 在 OpenReview submission form 中填写，不在 PDF 中

## 论文文件
- 主文件: `projects/causal_style_decomp_judge/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf`

## 你的审查侧重

**核心职责：方法论严谨性、实验设计、统计分析**

请重点审查以下方面：

### 1. 方法论 (Method)
- NLI-gated content control 的设计是否合理？NLI 阈值 0.90 的选择是否有充分 justification？
- Direction-aware NLI gating（verbosity 轴）是否引入 systematic bias？
- Controlled Style Decomposition 的因果声明强度是否与 evidence 匹配？DAG (Figure 2) 的识别假设是否完备？
- 同一模型 (Qwen3-32B) 同时作为 rewriter 和 judge 的 evaluator-producer bias 如何处理？cross-rewriter independence test 覆盖是否充分？

### 2. 实验设计 (Experiments)
- 统计框架：primary family 定义（几个 tests？Holm-Bonferroni 校正是否正确？）与 Table 1 标注是否一致？exploratory vs confirmatory 分类是否合理？
- Bradley-Terry 模型假设（IIA 等）是否被检验？GoF 诊断是否充分？
- GEE conditional decomposition：correlation structure 选择是否 robust？interaction test 结果如何？
- 负面控制 (Claude Sonnet 4)：TOST equivalence testing 的 Δ 选择是否合理？统计功效是否足够？
- 样本量：LLMBar n=100（NLI 后 n=88），scaled replication n=355 仅覆盖一个 judge×axis。这对结论的 generalizability 有多大影响？

### 3. 内容完整性
- Rewriting artifact control（same-style double-rewrite）是否充分？
- NLI gate validation：FNR 估计使用同一 rewriter 模型是否存在循环性？GPT-4o cross-validation 的报告是否完整？
- 100-point continuous Likert scale 实验是否排除了 granularity explanation？

### 4. 格式合规
- 正文是否 ≤8 页？
- Limitations 章节是否恰当（覆盖要点但不过长）？
- 参考文献格式是否一致？

请提供：
1. **Summary** (2-3 句)
2. **Strengths** (逐条)
3. **Weaknesses** (逐条，分 Must-Fix / Should-Fix / Minor)
4. **Questions** (需要作者澄清的)
5. **Missing References** (如有)
6. **Overall Assessment** (评分 + 置信度)
7. **Detailed Comments** (逐节)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-22T03:25:02.633215+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 557 · 2026-05-22T03:25:02.683957+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-22T03:25:08.871614+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 559 · 2026-05-22T03:25:09.725124+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR review form scoring dimensions soundness excitement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR review form scoring dimensions soundness excitement"
  }
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-22T03:25:11.988470+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf",
  "pages": "1-8",
  "project": "causal_style_decomp_judge",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf",
    "pages": "1-8",
    "project": "causal_style_decomp_judge",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-22T03:25:15.100347+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form criteria. Here's what I found:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommenda
…[truncated 1149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6228
}
```

</details>

---


### Tool result

_source line 562 · 2026-05-22T03:25:16.468770+00:00_

Web search results for query: "EMNLP 2026 ARR review form scoring dimensions soundness excitement"

Links: [{"title":"TrustNLP","url":"https://trustnlpworkshop.github.io/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Improving Patient Experience: BMBA","url":"https://cdn.clinicaltrials.gov/large-docs/30/NCT05690230/Prot_SAP_000.pdf"}]

Based on the search results, I found relevant information about the ARR review form scoring dimensions:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

These scoring dimensions are defined as follows:

1. **Soundness**: The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

2. **Excitement**: Excitement scores are orthogonal to the assessment of the soundness of the paper, reflecting more subjective preferences. Excitement scores reflect our personal taste, and so do not necessarily come with explicit reasons.

3. **Overall Recommendation**: The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.

The key distinction is that soundness should be objective and well-justifie
…[truncated 260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6743
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-22T03:25:18.331335+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 468.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 565.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.5}], \"total_pages\": 15, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts
…[truncated 68 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6342
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-22T03:25:26.476760+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and descriptions. I need the exact criteria for: Soundness, Excitement, Overall Assessment, Confidence, and any other dimensions. Include the full text of each score level description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and descriptions. I need the exact criteria for: Soundness, Excitement, Overall Assessment, Confidence, and any other dimensions. Include the full text of each score level description."
  }
}
```

</details>

---


### Tool call

_source line 565 · 2026-05-22T03:25:26.878707+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 566 · 2026-05-22T03:25:27.885318+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 567 · 2026-05-22T03:25:27.935993+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-22T03:25:28.439031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-22T03:25:28.796347+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 860
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-22T03:25:28.796776+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-22T03:25:29.909304+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1470
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-22T03:25:29.909724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-22T03:25:30.385792+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1589
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-22T03:25:30.386218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 575 · 2026-05-22T03:25:30.765503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 576 · 2026-05-22T03:25:31.837213+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1927
}
```

</details>

---


### Tool call

_source line 577 · 2026-05-22T03:25:31.895496+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 578 · 2026-05-22T03:25:32.676651+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence (1-5 Scale)
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

## Soundness (1-5 Scale)
- **5:** "Excellent: This study is one of the most thorough I have seen, given its type."
- **4:** "Strong: This study provides sufficient support for all of its claims."
- **3:** "Acceptable: This study provides sufficient support for its main claims."
- **2:** "Poor: Some of the main claims are not sufficiently supported."
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement (1-5 Scale)
- **5:** "Highly Exciting: I would recommend this paper to others."
- **4:** "Exciting: I would mention this paper to others."
- **3:** "Interesting: I might mention some points of this paper to others."
- **2:** "Potentially Interesting: this paper does not resonate with me."
- **1:** "Not Exciting: this paper does not resonate with me."

## Overall Assessment (1-5 Scale)
- **5:** "Consider for Award: top 2.5% papers."
- **4:** "Conference: I think this paper could be accepted."
- **3:** "Findings: I think this paper could be accepted to Findings of ACL."
- **2:** "Resubmit next cycle: paper needs substantial revisions."
- **1:** "Do not resubmit: paper has to be fully redone."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6199
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-22T03:25:32.878701+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2492
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-22T03:25:32.879372+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf",
  "pages": "9-15",
  "project": "causal_style_decomp_judge",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf",
    "pages": "9-15",
    "project": "causal_style_decomp_judge",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-22T03:25:33.031049+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2265
}
```

</details>

---


### Tool result

_source line 582 · 2026-05-22T03:25:33.284029+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1388
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-22T03:25:34.087145+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.7}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 425.5}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 562.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 600.7}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.9}], \"total_pages\": 15, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1207
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-22T03:25:40.763384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 585 · 2026-05-22T03:25:41.167163+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-22T03:25:42.026791+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1263
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-22T03:25:42.027783+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 860
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-22T03:25:42.028071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 589 · 2026-05-22T03:25:42.533476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 590 · 2026-05-22T03:25:42.987266+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 591 · 2026-05-22T03:25:42.987800+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 592 · 2026-05-22T03:25:43.942655+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-22T03:25:43.943772+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-22T03:25:43.994327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 595 · 2026-05-22T03:25:44.147470+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 596 · 2026-05-22T03:25:44.904632+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-22T03:25:45.107958+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-22T03:31:09.429238+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including: what reviewers should evaluate, how to assess soundness, excitement, overall assessment, what constitutes a good review, and any specific criteria for different score levels. Include all scoring rubrics and evaluation dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines including: what reviewers should evaluate, how to assess soundness, excitement, overall assessment, what constitutes a good review, and any specific criteria for different score levels. Include all scoring rubrics and evaluation dimensions."
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-22T03:31:19.381524+00:00_

# ARR Reviewer Guidelines: Comprehensive Overview

## Core Evaluation Framework

ARR reviewers assess papers using three primary scores:

1. **Soundness**: Technical correctness and methodological rigor
2. **Excitement**: Personal interest and perceived impact
3. **Overall Assessment**: Composite recommendation for acceptance

## Soundness Evaluation

Soundness scores must align with review justifications. Low scores require explicit identification of "major faults" in the paper. Reviewers should ensure their assessment reflects actual technical issues rather than unconscious biases.

Key soundness considerations include:
- Validity of assumptions and proofs
- Appropriate experimental design
- Statistical significance reporting
- Reproducibility of results
- Correct methodology execution

## Excitement vs. Soundness

These dimensions are orthogonal. A technically sound paper may generate low excitement if it lacks novelty or personal relevance to the reviewer. Conversely, innovative work should receive high soundness scores despite limited personal interest.

## Overall Assessment Criteria

The composite recommendation balances:
- Technical soundness and reproducibility (mandatory for acceptance)
- Novelty and originality of contribution
- Potential impact within target communities
- Appropriateness to conference scope

Papers can merit acceptance for contributions beyond SOTA improvements: "efficiency improvements...or creating high-quality resources...may not sound very novel" yet deserve acceptance.

## Characteristics of Strong Reviews

Effective reviews demonstrate:

- **Specificity**: "The paper is missing references X, Y, Z" rather than vague critiques
- **Professional tone**: Constructive feedback that assists author improvement
- **Justified scores**: All recommendations supported by detailed evidence
- **Acknowledgment of responses**: Recognition when authors address concerns

## Common Review Pitfalls to Avoid

Reviewers should watch for cognitive biases 
…[truncated 1091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9952
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-22T03:34:37.688823+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：方法严谨性与实验设计\n\n**论文标题**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n**一句话总结**: 论文提出了有价值的发现（Likert 系统性遗漏 pairwise 能检测到的风格偏差），实验框架设计较严谨，但 primary family 构成透明度不足、cross-rewriter 验证覆盖不够、负面控制统计功效偏弱，这些方法论缺口需要修补后才能支撑论文的全部 claims。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验管线（NLI gate → position balancing → BT + GEE）设计合理，多项 robustness check 到位，但 primary family 定义不透明、cross-rewriter 覆盖仅 1/4 judges、TOST 负面控制功效不足构成显著方法论缺口 |\n| Excitement | 3.5/5 | Likert Blindspot 是对 LLM 评估社区有实际影响的发现，per-axis GEE decomposition 增添了新 insight；但 pairwise > Likert 对 subtle effects 更敏感这一结论在测量理论中并不意外，且 attenuation vs. divergence 的歧义未解限制了贡献的清晰度 |\n| Confidence | 4/5 | 仔细阅读了全文含全部 16 个附录，熟悉论文使用的 BT、GEE、TOST 等统计方法 |\n\n---\n\n## Summary\n\n本文引入 Controlled Style Decomposition (CSD)，通过 NLI-gated 内容控制、per-axis 风格改写和位置控制的 pairwise comparison，系统量化 LLM judge 的风格偏差。核心发现\"Likert Blindspot\"表明：标准 Likert 评分在中等效应量下系统性遗漏 pairwise 可检测到的风格偏差，信号损失达 60%+。GEE conditional decomposition 揭示了跨 judge 一致的 per-axis confound structure（verbosity 为 style-dominated，formality 受 original quality 调节）。实验涵盖 5 个 judges、3 个 benchmark、3 个 style axes，统计分析包括 7 种方法。\n\n---\n\n## 主要优势（Strengths）\n\n**S1. 实用性强的核心发现。** Likert Blindspot 对 LLM 评估实践有直接影响：当前 AlpacaEval/MT-Bench 等主流排行榜依赖 Likert 评分，本文提供了系统性证据表明这种方法会遗漏中等强度的风格偏差。Table 1 在 5 个 judges × 3 个 axes 的广泛矩阵中一致展示了这一 pattern。\n\n**S2. 多层验证的实验管线。** NLI gate (DeBERTa-v3-large, threshold 0.90) → consistency filter → position-balanced pairwise → BT + GEE 的管线设计体现了严谨的方法论思维。特别是：\n- 11 个 NLI 阈值扫描（Table 8, Appendix E）验证了阈值选择的稳健性\n- Same-style double-rewrite control（Table 15, Appendix O）隔离了 rewriting artifact\n- 100-point continuous Likert scale（Appendix M）排除了 granularity explanation\n- Formal power analysis（Appendix K, Table 11）量化了 Likert 所需的巨大样本量\n\n**S3. 完善的统计框架。** 论文正确区分了 confirmatory vs. exploratory 分析，应用了 Holm-Bonferroni 校正，报告了 bootstrap 95% CIs。7 种统计方法的 sensitivity hierarchy（Table 2）是一个有说服力的展示——所有 Likert-based 方法均未达到显著性，而 pairwise methods 达到了。\n\n**S4. GEE conditional decomposition 提供新 insight。** Table 3 揭示 verbosity 跨四个 judges 一致为 style-dominated（Style ORs 5.8–13.1），而 formality 展现 conditional confounding（Originality ORs 2.2–5.1 显著），这比简单的\"judges have style bias\"叙事更有深度。Appendix C 的 correlation structure comparison（Table 4）和 interaction test 验证了 GEE specification 的合理性。\n\n**S5. 诚实的局限性讨论。** 论文公开讨论了 evaluator-producer bias（Qwen3-32B 同时作 rewriter 和 judge）、measurement attenuation vs. construct divergence 的歧义、以及样本量约束。这种透明度是受欢迎的。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Primary family 构成缺乏透明度\n- **位置**: Section 4.1\n- **问题**: 论文声明\"a primary family of six hypothesis tests (three judges × two axes)\"并应用 Holm-Bonferroni 校正，但从未明确指出哪三个 judges 被纳入 primary family。论文描述了四个 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）加一个 negative control（Claude Sonnet 4）。如果 primary family 排除了 Gemini，需要明确声明并提供理由。\n- **为什么影响接收**: 如果纳入 Gemini（4 judges × 2 axes = 8 tests），Holm-Bonferroni 校正将更保守，部分结果可能失去 adjusted significance。当前写法存在 post-hoc selection 的嫌疑——reviewer 无法验证 primary family 是否在看到数据前确定。这是 confirmatory analysis 的基本透明度要求。\n- **建议**: 在 Section 4.1 明确列出三个 primary judges 的名称；如果 Gemini 被排除，说明是因为它是\"supplementary architecture validation\"（Section 3.4 的措辞暗示了这一点，但需要显式关联到 primary family 定义）。同时报告 8-test primary family 下的 adjusted p-values 作为 sensitivity analysis。\n\n**N2** [critical] Cross-rewriter independence 验证覆盖不足\n- **位置**: Appendix D (Section D)\n- **问题**: 论文仅测试了一个 judge（Qwen3-32B）配合替代 rewriter（GPT-4o）。四个 target judges 中的另外三个（GPT-4o as judge, Llama-3.3-70B, Gemini）没有 cross-rewriter 验证。\n- **具体缺口**:\n  (a) GPT-4o as judge 使用 Qwen3-32B 作 rewriter——GPT-4o 可能检测到 Qwen3-32B 特有的改写痕迹（artifacts），而这与 style bias 无关。没有用第三方 rewriter 验证 GPT-4o judge 的结果。\n  (b) Llama-3.3-70B 和 Gemini 完全没有 cross-rewriter 检验。\n- **为什么影响接收**: Evaluator-producer bias 是论文自己承认的主要 threat to validity（Limitations 段落）。仅用一个 judge 的 cross-rewriter test 不足以支撑\"Blindspot is rewriter-independent\"这一 generalized claim。\n- **建议**: 至少对一个额外 judge 执行 cross-rewriter validation（优先选 GPT-4o as judge，因为它是最重要的 target judge 且当前使用同一家族外的 rewriter）。如果资源不允许完整复制，至少在 Limitations 中明确承认覆盖不足并 downgrade 相关 claim 的强度。\n\n**N3** [critical] 负面控制（Claude Sonnet 4）的 TOST equivalence testing 功效不足、等价边界过宽\n- **位置**: Appendix G\n- **问题**: \n  (a) 在 Δ = 10pp 下 TOST underpowered（n = 87）。在 Δ = 15pp 下两个 axes 落入等价区间。\n  (b) 论文确认的最小 bias 为 +13pp（GPT-4o formality, BT 60.7%）。Δ = 15pp 的等价边界几乎涵盖了这个已知正效应——这意味着 Claude 可能有高达 ~14pp 的 bias 而 TOST 仍然宣告等价。\n  (c) n = 87 的样本量远低于 Appendix K power analysis 建议的水平。\n- **为什么影响接收**: 负面控制是论文实验设计的重要组成部分（证明 CSD 不是对所有 judges 产生 false positive）。如果等价边界涵盖已知正效应的范围，negative control 的 discriminative power 存疑。\n- **建议**: 三选一：(a) 增加 Claude 的样本量使 Δ = 10pp 有足够功效；(b) 将 Claude 重新定位为\"insufficient evidence for bias\"而非\"negative control\"；(c) 报告 TOST 在 n = 87 下能 reject 的最小 Δ 值，让读者自行判断。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 因果框架表述不一致\n- **位置**: Title, Abstract, Section 3.5, Figure 2\n- **问题**: 框架名称\"Controlled Style Decomposition\"和 DAG（Figure 2）带有因果含义。Section 3.5 正确地 hedge 为\"interventionist rather than formal causal evidence\"并声明不 claim SUTVA。但 Abstract 使用\"controlled\"暗示因果干预，Section 1 引用\"the causal variant\"。论文在因果语言的使用上不一致。\n- **建议**: 统一术语——全文使用\"interventionist\"或\"controlled manipulation\"而非暗示正式因果推断的语言。Figure 2 的 caption 已标注\"design rationale, not a claim of perfect identification\"，这是好的，但需要全文一致。\n\n**W2** [warning] Bradley-Terry 模型的 IIA 假设未讨论\n- **位置**: Section 3.3, Appendix H\n- **问题**: BT 模型假设 Independence of Irrelevant Alternatives。虽然 pairwise 配置下 IIA 问题不如 multi-alternative 严重，但论文未提及此假设。Appendix H 报告了 goodness-of-fit（deviance = 52.86, df = 16, p = 0.185 for formality），但这测试的是模型拟合度而非 IIA。更关键的是，Appendix H 发现 formality 存在显著方向异质性（68.9% vs. 52.6%, Fisher's p = 0.015），表明 BT 的单参数公式可能遗漏了重要的效应异质性。\n- **建议**: (a) 承认 IIA 假设；(b) 考虑 stratified BT（按 original-text direction 分层估计 win probability），检验结论是否在分层后仍然成立。\n\n**W3** [warning] NLI gate FNR 估计基于过小样本\n- **位置**: Section 5.1\n- **问题**: FNR 基于 12 个手动评估的 rejected pairs（\"8 of 12 rejected pairs judged content-preserving\"），得出 FNR ≈ 8.4%。n = 12 的 Wilson 95% CI 约为 [2%, 28%]，区间极宽。GPT-4o cross-validation 报告了 pass precision（92.1% / 82.6%）但未直接报告 FNR 的置信区间。\n- **建议**: 报告 FNR 的 bootstrapped 或 Wilson CI；如果可能，在更大样本上验证。\n\n**W4** [warning] Verbosity 轴的 direction-aware NLI gating 引入不对称过滤\n- **位置**: Section 3.2, Appendix F\n- **问题**: Direction-aware gating 为 verbosity 额外放入 21 个 pairs（比 bidirectional gating 多 32%）。这些 pairs 通过了更宽松的标准（单向 entailment），可能引入 selection bias——这些 pairs 中部分内容变化可能未被 NLI 完全捕获。论文报告 BT estimates\"statistically indistinguishable\"但未检验两组 NLI scores 是否存在系统性差异。\n- **建议**: 报告 direction-aware 额外放入的 pairs 与 bidirectional-pass pairs 在 NLI score 分布上的比较（如 KS test 或分位数对比），确认无系统性质量差异。\n\n**W5** [warning] Measurement attenuation vs. construct divergence 歧义未解\n- **位置**: Section 5.2, Section 5.6, Section 6\n- **问题**: 论文提出两种对 Likert Blindspot 的解释——(1) measurement attenuation（Likert 灵敏度不够），(2) construct divergence（Likert 和 pairwise 测量不同构念）——但未能在两者之间做出判断。Bootstrap attenuation 分析（Appendix J）显示 Likert d 在 n = 355 仍近零，排除了纯 power 问题；100-point continuous scale（Appendix M）排除了 granularity。但如果确实是 construct divergence（Likert 测量 absolute quality，pairwise 测量 ordinal preference），则\"Blindspot\"这一术语暗示 Likert\"遗漏\"了什么，而实际上可能只是\"测量了不同的东西\"——这弱化了论文的核心 narrative。\n- **建议**: 在 Section 6 (Conclusion) 中更明确地定位：如果两种解释都成立，则论文的 practical contribution 在于\"研究者应该同时使用两种方法以获得完整画面\"；如果偏向 attenuation，需要更多 evidence（如在已知有 bias 的 setting 中 Likert 能否在巨大 n 下检测到效应）。\n\n**W6** [warning] 生态效度（ecological validity）讨论不足\n- **位置**: Limitations\n- **问题**: CSD 检测的 bias 来自人工改写的风格变体。自然发生的文本风格变化可能更微妙、更多轴交织，且伴随内容差异。论文的 Limitations 提到了 axis interaction，但未讨论从 controlled manipulation 到 naturalistic evaluation 的 generalizability gap。\n- **建议**: 在 Limitations 中增加一句关于 ecological validity 的讨论：CSD 的发现是否能 generalize 到非实验设置下的自然文本评估。\n\n---\n\n## 小问题（Minor Issues）\n\n- **Table 3 GEE CIs 宽度**: 部分配置的 OR CI 极宽（如 Gemini form: Style OR CI 覆盖 0.58–4.54），表明 GEE 在某些 judge×axis 上估计精度不足。应在 Table 3 附注或正文中 acknowledge。\n- **Figure 1 信息密度**: CSD pipeline overview 流程较密，NLI gate 的 branching logic 不够直观。可考虑分解为两个 sub-figures 或增加视觉层次。\n- **Section 3.4 LLMBar 标签描述**: \"human-verified quality labels\"——简要说明这些 labels 捕获什么维度的 quality（task correctness? response quality?）会有助于读者理解。\n- **\"Blindspot\" 术语标记**: 作为 coined term，建议首次使用时用斜体或引号标记，并给出明确定义。当前定义散布在多处（Abstract: \"Likert scoring systematically misses style biases that pairwise comparison detects\"; Section 1: 更长的描述），建议在 Introduction 给出一次简洁的正式定义。\n\n---\n\n## Questions for Authors\n\n**Q1.** Primary family 包含哪三个 judges？请明确列出并说明排除第四个 target judge 的理由。如果在实验设计阶段已预注册此选择，请引用预注册。\n\n**Q2.** Cross-rewriter independence test 仅覆盖 Qwen3-32B as judge 是否是资源约束？如果是，能否至少对 GPT-4o as judge 用 Llama 或 Gemini 作为替代 rewriter 做一个小规模验证？\n\n**Q3.** 对于 Claude Sonnet 4 的 TOST，在 n = 87 下能 reject 的最小 Δ 具体是多少？如果该 Δ 大于论文中检测到的最小正效应（+13pp），这是否 invalidate negative control 的角色？\n\n**Q4.** Appendix H 发现 formality 存在显著方向异质性（68.9% vs. 52.6%, Fisher's p = 0.015）。是否考虑过 stratified BT（按 original text direction 分层估计 win probability）？如果是，分层后的 BT estimates 是否与 GEE 的 Originality effect 一致？\n\n**Q5.** Table 2 的 sensitivity hierarchy 显示所有 7 种 Likert-based 方法均未达显著性。这是否可能部分归因于 LLMBar 样本量（n ≈ 88 post-NLI）不足，而非 Likert 方法的固有局限？论文的 formal power analysis（Appendix K）显示部分配置需 n > 10,000 才能达到 80% power——这个数量级是否使 Likert vs. pairwise 的比较在方法论上不公平（不同统计效率的方法需要不同样本量才能公平比较）？\n\n---\n\n## Missing References\n\n未发现显著遗漏。Related work 覆盖了近期 LLM judge bias 研究（Shi et al., 2025; Lin et al., 2025; Muragadoss et al., 2025）、RATE 方法论（Reber et al., 2025）、BT 在 NLP 评估中的应用，以及测量理论基础（Thurstone 1927, Stevens 1946, Krosnick 1999）。建议考虑补充：\n- Zheng et al. (2024) \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\" 的更详细讨论（虽已引用但可加强对比）\n- 如有 2025-2026 年关于 Likert scale limitations in NLG evaluation 的新工作，值得补充\n\n---\n\n## 格式合规检查\n\n| 检查项 | 结果 |\n|--------|------|\n| 正文 ≤ 8 页 | ✓ 合规。Sections 1-6 + Limitations 在 8 页内完成 |\n| Double-blind 匿名 | ✓ \"Anonymous ACL submission\"，未见作者信息 |\n| ACL 双栏格式 | ✓ 正确使用 |\n| Limitations 章节 | ✓ 存在，覆盖 3 个要点（evaluator-producer bias、methodology/scale design、ecological validity），篇幅适中 |\n| ARR Checklist | ✓ 不在 PDF 中（符合规定：在 OpenReview form 中填写） |\n| 参考文献格式 | ✓ 一致，未见明显格式问题 |\n\n---\n\n## Detailed Comments by Section\n\n### Section 1 (Introduction)\n- 开头的\"average height for a male\"例子直观有效，但\"causal variant\"措辞暗示了正式的因果推断，与 Section 3.5 的 hedging 不一致（参见 W1）。\n- \"70–92% of observed preferences originate from surface-level style cues\"的引用（Muragadoss et al., 2025; Sournik et al., 2020）——确认这些引用的测量方法是否与本文的 CSD 可比。\n\n### Section 2 (Related Work)\n- 覆盖全面，将 CSD 与 RATE（Reber et al., 2025）的区别阐述清楚（per-axis isolation + NLI gate + forced-choice vs. Likert ATE + post-hoc correction）。\n- \"CASSE (Cho et al., 2026)\"和\"FairJudge (Yang et al., 2026)\"是 concurrent work，能否简要讨论 CSD 与它们的互补性？\n\n### Section 3 (Method)\n- Section 3.1: Style-controlled rewriting 的 prompt 设计（binary classification → opposite pole rewriting）清晰。但\"a distant balanced pair where the rewrite changed only in style\"的表述过强——NLI gate 保证 semantic content 不变，但 writing quality/fluency 可能随改写发生变化（Table 15 的 double-rewrite 数据证实了这一点）。\n- Section 3.2: NLI gate 的 bidirectional entailment 要求合理。Direction-aware verbosity gating 的 rationale（增加内容不违反 forward entailment）在直觉上合理，但需量化其影响（参见 W4）。\n- Section 3.3: BT 使用所有 observations（含 inconsistent pairs）是标准做法，且 Section 3.3 有 justification。但未讨论 inconsistent pair rate——如果 inconsistency 率很高（如 >30%），可能表明 judges 在边界 cases 上 noise 很大。\n- Section 3.5: DAG (Figure 2) 标注为\"design rationale\"是恰当的。三个识别假设清晰。但假设 (iii)（\"style rewrite introduces no systematic differences beyond the target axis\"）是最关键的，且最难验证。Same-style double-rewrite（Appendix O）提供了部分验证，但它只检验了 within-style rewriting artifact，不检验 cross-style rewriting 是否引入了 axis 之外的 confound。\n\n### Section 4 (Experiments)\n- Section 4.1: Primary family 定义的透明度问题（参见 N1）。Exploratory vs. confirmatory 分类的逻辑应更 explicit。\n- Section 3.4 / 4: LLMBar (n = 100, post-NLI n = 88) 是一个小到中等的 benchmark。scaled replication (n = 355) 仅覆盖 formality × Qwen3-32B 一个 cell，对 generalizability 的支持有限。\n\n### Section 5 (Analysis)\n- Section 5.1: NLI gate validation 的 FNR 估计样本量过小（参见 W3）。GPT-4o cross-validation (92.1% / 82.6% precision) 是一个好的补充验证。\n- Section 5.2: Likert vs. Pairwise 灵敏度比较是论文的核心贡献。Figure 4 的 detection probability 曲线直观展示了两种方法的分离——BT 在 n ≈ 62 达到 80% power，而 Likert ATE 在 n = 355 仍然 flat near zero。这是强有力的 evidence。\n- Section 5.3: Cross-judge replication（三个独立 judges replicate the Blindspot）增强了结论的稳健性。\n- Section 5.4: Cross-axis replication for verbosity 跨四个 judges 一致——这是最一致的发现。\n- Section 5.5: Register 作为 judge-dependent confound 的发现有趣但仅为 exploratory。\n- Section 5.6: GEE conditional decomposition 是论文的第二个主要贡献。Table 3 的 per-axis confound structure 是新颖的。但部分 CI 很宽（参见 Minor）。\n\n### Section 6 (Conclusion)\n- 两个主要发现的总结清晰。\"whether this reflects measurement attenuation or construct divergence\"的 framing 诚实但留下了悬念（参见 W5）。\n\n### Limitations\n- 覆盖了关键点。建议增加 ecological validity 讨论（参见 W6）和 cross-rewriter 覆盖不足的明确承认。\n\n---\n\n## 综合判断\n\n本文的核心贡献——Likert Blindspot 的系统性 demonstration——是扎实的。跨 5 个 judges、3 个 benchmarks 和 7 种统计方法的一致性令人信服。GEE decomposition 揭示的 per-axis confound structure 增添了深度。\n\n主要顾虑集中在三个方法论缺口：(1) primary family 构成未透明公开，影响 FWER 控制的可信度；(2) cross-rewriter 验证仅覆盖 1/4 target judges，限制了 rewriter-independence claim 的强度；(3) 负面控制的 TOST 等价边界过宽，无法有效排除中等 bias。\n\n这些问题均可在修改中解决。如果 N1-N3 得到充分回应（特别是 N1 的透明度和 N3 的 TOST re-framing），本文有潜力达到 4.0 (Conference) 的水平。当前评分 3.5 (Borderline Conference) 反映了这些未解决的方法论顾虑。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见：方法严谨性与实验设计\n\n**论文标题**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n**一句话总结**: 论文提出了有价值的发现（Likert 系统性遗漏 pairwise 能检测到的风格偏差），实验框架设计较严谨，但 primary family 构成透明度不足、cross-rewriter 验证覆盖不够、负面控制统计功效偏弱，这些方法论缺口需要修补后才能支撑论文的全部 claims。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验管线（NLI gate → position balancing → BT + GEE）设计合理，多项 robustness check 到位，但 primary family 定义不透明、cross-rewriter 覆盖仅 1/4 judges、TOST 负面控制功效不足构成显著方法论缺口 |\n| Excitement | 3.5/5 | Likert Blindspot 是对 LLM 评估社区有实际影响的发现，per-axis GEE decomposition 增添了新 insight；但 pairwise > Likert 对 subtle effects 更敏感这一结论在测量理论中并不意外，且 attenuation vs. divergence 的歧义未解限制了贡献的清晰度 |\n| Confidence | 4/5 | 仔细阅读了全文含全部 16 个附录，熟悉论文使用的 BT、GEE、TOST 等统计方法 |\n\n---\n\n## Summary\n\n本文引入 Controlled Style Decomposition (CSD)，通过 NLI-gated 内容控制、per-axis 风格改写和位置控制的 pairwise comparison，系统量化 LLM judge 的风格偏差。核心发现\"Likert Blindspot\"表明：标准 Likert 评分在中等效应量下系统性遗漏 pairwise 可检测到的风格偏差，信号损失达 60%+。GEE conditional decomposition 揭示了跨 judge 一致的 per-axis confound structure（verbosity 为 style-dominated，formality 受 original quality 调节）。实验涵盖 5 个 judges、3 个 benchmark、3 个 style axes，统计分析包括 7 种方法。\n\n---\n\n## 主要优势（Strengths）\n\n**S1. 实用性强的核心发现。** Likert Blindspot 对 LLM 评估实践有直接影响：当前 AlpacaEval/MT-Bench 等主流排行榜依赖 Likert 评分，本文提供了系统性证据表明这种方法会遗漏中等强度的风格偏差。Table 1 在 5 个 judges × 3 个 axes 的广泛矩阵中一致展示了这一 pattern。\n\n**S2. 多层验证的实验管线。** NLI gate (DeBERTa-v3-large, threshold 0.90) → consistency filter → position-balanced pairwise → BT + GEE 的管线设计体现了严谨的方法论思维。特别是：\n- 11 个 NLI 阈值扫描（Table 8, Appendix E）验证了阈值选择的稳健性\n- Same-style double-rewrite control（Table 15, Appendix O）隔离了 rewriting artifact\n- 100-point continuous Likert scale（Appendix M）排除了 granularity explanation\n- Formal power analysis（Appendix K, Table 11）量化了 Likert 所需的巨大样本量\n\n**S3. 完善的统计框架。** 论文正确区分了 confirmatory vs. exploratory 分析，应用了 Holm-Bonferroni 校正，报告了 bootstrap 95% CIs。7 种统计方法的 sensitivity hierarchy（Table 2）是一个有说服力的展示——所有 Likert-based 方法均未达到显著性，而 pairwise methods 达到了。\n\n**S4. GEE conditional decomposition 提供新 insight。** Table 3 揭示 verbosity 跨四个 judges 一致为 style-dominated（Style ORs 5.8–13.1），而 formality 展现 conditional confounding（Originality ORs 2.2–5.1 显著），这比简单的\"judges have style bias\"叙事更有深度。Appendix C 的 correlation structure comparison（Table 4）和 interaction test 验证了 GEE specification 的合理性。\n\n**S5. 诚实的局限性讨论。** 论文公开讨论了 evaluator-producer bias（Qwen3-32B 同时作 rewriter 和 judge）、measurement attenuation vs. construct divergence 的歧义、以及样本量约束。这种透明度是受欢迎的。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Primary family 构成缺乏透明度\n- **位置**: Section 4.1\n- **问题**: 论文声明\"a primary family of six hypothesis tests (three judges × two axes)\"并应用 Holm-Bonferroni 校正，但从未明确指出哪三个 judges 被纳入 primary family。论文描述了四个 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）加一个 negative control（Claude Sonnet 4）。如果 primary family 排除了 Gemini，需要明确声明并提供理由。\n- **为什么影响接收**: 如果纳入 Gemini（4 judges × 2 axes = 8 tests），Holm-Bonferroni 校正将更保守，部分结果可能失去 adjusted significance。当前写法存在 post-hoc selection 的嫌疑——reviewer 无法验证 primary family 是否在看到数据前确定。这是 confirmatory analysis 的基本透明度要求。\n- **建议**: 在 Section 4.1 明确列出三个 primary judges 的名称；如果 Gemini 被排除，说明是因为它是\"supplementary architecture validation\"（Section 3.4 的措辞暗示了这一点，但需要显式关联到 primary family 定义）。同时报告 8-test primary family 下的 adjusted p-values 作为 sensitivity analysis。\n\n**N2** [critical] Cross-rewriter independence 验证覆盖不足\n- **位置**: Appendix D (Section D)\n- **问题**: 论文仅测试了一个 judge（Qwen3-32B）配合替代 rewriter（GPT-4o）。四个 target judges 中的另外三个（GPT-4o as judge, Llama-3.3-70B, Gemini）没有 cross-rewriter 验证。\n- **具体缺口**:\n  (a) GPT-4o as judge 使用 Qwen3-32B 作 rewriter——GPT-4o 可能检测到 Qwen3-32B 特有的改写痕迹（artifacts），而这与 style bias 无关。没有用第三方 rewriter 验证 GPT-4o judge 的结果。\n  (b) Llama-3.3-70B 和 Gemini 完全没有 cross-rewriter 检验。\n- **为什么影响接收**: Evaluator-producer bias 是论文自己承认的主要 threat to validity（Limitations 段落）。仅用一个 judge 的 cross-rewriter test 不足以支撑\"Blindspot is rewriter-independent\"这一 generalized claim。\n- **建议**: 至少对一个额外 judge 执行 cross-rewriter validation（优先选 GPT-4o as judge，因为它是最重要的 target judge 且当前使用同一家族外的 rewriter）。如果资源不允许完整复制，至少在 Limitations 中明确承认覆盖不足并 downgrade 相关 claim 的强度。\n\n**N3** [critical] 负面控制（Claude Sonnet 4）的 TOST equivalence testing 功效不足、等价边界过宽\n- **位置**: Appendix G\n- **问题**: \n  (a) 在 Δ = 10pp 下 TOST underpowered（n = 87）。在 Δ = 15pp 下两个 axes 落入等价区间。\n  (b) 论文确认的最小 bias 为 +13pp（GPT-4o formality, BT 60.7%）。Δ = 15pp 的等价边界几乎涵盖了这个已知正效应——这意味着 Claude 可能有高达 ~14pp 的 bias 而 TOST 仍然宣告等价。\n  (c) n = 87 的样本量远低于 Appendix K power analysis 建议的水平。\n- **为什么影响接收**: 负面控制是论文实验设计的重要组成部分（证明 CSD 不是对所有 judges 产生 false positive）。如果等价边界涵盖已知正效应的范围，negative control 的 discriminative power 存疑。\n- **建议**: 三选一：(a) 增加 Claude 的样本量使 Δ = 10pp 有足够功效；(b) 将 Claude 重新定位为\"insufficient evidence for bias\"而非\"negative control\"；(c) 报告 TOST 在 n = 87 下能 reject 的最小 Δ 值，让读者自行判断。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 因果框架表述不一致\n- **位置**: Title, Abstract, Section 3.5, Figure 2\n- **问题**: 框架名称\"Controlled Style Decomposition\"和 DAG（Figure 2）带有因果含义。Section 3.5 正确地 hedge 为\"interventionist rather than formal causal evidence\"并声明不 claim SUTVA。但 Abstract 使用\"controlled\"暗示因果干预，Section 1 引用\"the causal variant\"。论文在因果语言的使用上不一致。\n- **建议**: 统一术语——全文使用\"interventionist\"或\"controlled manipulation\"而非暗示正式因果推断的语言。Figure 2 的 caption 已标注\"design rationale, not a claim of perfect identification\"，这是好的，但需要全文一致。\n\n**W2** [warning] Bradley-Terry 模型的 IIA 假设未讨论\n- **位置**: Section 3.3, Appendix H\n- **问题**: BT 模型假设 Independence of Irrelevant Alternatives。虽然 pairwise 配置下 IIA 问题不如 multi-alternative 严重，但论文未提及此假设。Appendix H 报告了 goodness-of-fit（deviance = 52.86, df = 16, p = 0.185 for formality），但这测试的是模型拟合度而非 IIA。更关键的是，Appendix H 发现 formality 存在显著方向异质性（68.9% vs. 52.6%, Fisher's p = 0.015），表明 BT 的单参数公式可能遗漏了重要的效应异质性。\n- **建议**: (a) 承认 IIA 假设；(b) 考虑 stratified BT（按 original-text direction 分层估计 win probability），检验结论是否在分层后仍然成立。\n\n**W3** [warning] NLI gate FNR 估计基于过小样本\n- **位置**: Section 5.1\n- **问题**: FNR 基于 12 个手动评估的 rejected pairs（\"8 of 12 rejected pairs judged content-preserving\"），得出 FNR ≈ 8.4%。n = 12 的 Wilson 95% CI 约为 [2%, 28%]，区间极宽。GPT-4o cross-validation 报告了 pass precision（92.1% / 82.6%）但未直接报告 FNR 的置信区间。\n- **建议**: 报告 FNR 的 bootstrapped 或 Wilson CI；如果可能，在更大样本上验证。\n\n**W4** [warning] Verbosity 轴的 direction-aware NLI gating 引入不对称过滤\n- **位置**: Section 3.2, Appendix F\n- **问题**: Direction-aware gating 为 verbosity 额外放入 21 个 pairs（比 bidirectional gating 多 32%）。这些 pairs 通过了更宽松的标准（单向 entailment），可能引入 selection bias——这些 pairs 中部分内容变化可能未被 NLI 完全捕获。论文报告 BT estimates\"statistically indistinguishable\"但未检验两组 NLI scores 是否存在系统性差异。\n- **建议**: 报告 direction-aware 额外放入的 pairs 与 bidirectional-pass pairs 在 NLI score 分布上的比较（如 KS test 或分位数对比），确认无系统性质量差异。\n\n**W5** [warning] Measurement attenuation vs. construct divergence 歧义未解\n- **位置**: Section 5.2, Section 5.6, Section 6\n- **问题**: 论文提出两种对 Likert Blindspot 的解释——(1) measurement attenuation（Likert 灵敏度不够），(2) construct divergence（Likert 和 pairwise 测量不同构念）——但未能在两者之间做出判断。Bootstrap attenuation 分析（Appendix J）显示 Likert d 在 n = 355 仍近零，排除了纯 power 问题；100-point continuous scale（Appendix M）排除了 granularity。但如果确实是 construct divergence（Likert 测量 absolute quality，pairwise 测量 ordinal preference），则\"Blindspot\"这一术语暗示 Likert\"遗漏\"了什么，而实际上可能只是\"测量了不同的东西\"——这弱化了论文的核心 narrative。\n- **建议**: 在 Section 6 (Conclusion) 中更明确地定位：如果两种解释都成立，则论文的 practical contribution 在于\"研究者应该同时使用两种方法以获得完整画面\"；如果偏向 attenuation，需要更多 evidence（如在已知有 bias 的 setting 中 Likert 能否在巨大 n 下检测到效应）。\n\n**W6** [warning] 生态效度（ecological validity）讨论不足\n- **位置**: Limitations\n- **问题**: CSD 检测的 bias 来自人工改写的风格变体。自然发生的文本风格变化可能更微妙、更多轴交织，且伴随内容差异。论文的 Limitations 提到了 axis interaction，但未讨论从 controlled manipulation 到 naturalistic evaluation 的 generalizability gap。\n- **建议**: 在 Limitations 中增加一句关于 ecological validity 的讨论：CSD 的发现是否能 generalize 到非实验设置下的自然文本评估。\n\n---\n\n## 小问题（Minor Issues）\n\n- **Table 3 GEE CIs 宽度**: 部分配置的 OR CI 极宽（如 Gemini form: Style OR CI 覆盖 0.58–4.54），表明 GEE 在某些 judge×axis 上估计精度不足。应在 Table 3 附注或正文中 acknowledge。\n- **Figure 1 信息密度**: CSD pipeline overview 流程较密，NLI gate 的 branching logic 不够直观。可考虑分解为两个 sub-figures 或增加视觉层次。\n- **Section 3.4 LLMBar 标签描述**: \"human-verified quality labels\"——简要说明这些 labels 捕获什么维度的 quality（task correctness? response quality?）会有助于读者理解。\n- **\"Blindspot\" 术语标记**: 作为 coined term，建议首次使用时用斜体或引号标记，并给出明确定义。当前定义散布在多处（Abstract: \"Likert scoring systematically misses style biases that pairwise comparison detects\"; Section 1: 更长的描述），建议在 Introduction 给出一次简洁的正式定义。\n\n---\n\n## Questions for Authors\n\n**Q1.** Primary family 包含哪三个 judges？请明确列出并说明排除第四个 target judge 的理由。如果在实验设计阶段已预注册此选择，请引用预注册。\n\n**Q2.** Cross-rewriter independence test 仅覆盖 Qwen3-32B as judge 是否是资源约束？如果是，能否至少对 GPT-4o as judge 用 Llama 或 Gemini 作为替代 rewriter 做一个小规模验证？\n\n**Q3.** 对于 Claude Sonnet 4 的 TOST，在 n = 87 下能 reject 的最小 Δ 具体是多少？如果该 Δ 大于论文中检测到的最小正效应（+13pp），这是否 invalidate negative control 的角色？\n\n**Q4.** Appendix H 发现 formality 存在显著方向异质性（68.9% vs. 52.6%, Fisher's p = 0.015）。是否考虑过 stratified BT（按 original text direction 分层估计 win probability）？如果是，分层后的 BT estimates 是否与 GEE 的 Originality effect 一致？\n\n**Q5.** Table 2 的 sensitivity hierarchy 显示所有 7 种 Likert-based 方法均未达显著性。这是否可能部分归因于 LLMBar 样本量（n ≈ 88 post-NLI）不足，而非 Likert 方法的固有局限？论文的 formal power analysis（Appendix K）显示部分配置需 n > 10,000 才能达到 80% power——这个数量级是否使 Likert vs. pairwise 的比较在方法论上不公平（不同统计效率的方法需要不同样本量才能公平比较）？\n\n---\n\n## Missing References\n\n未发现显著遗漏。Related work 覆盖了近期 LLM judge bias 研究（Shi et al., 2025; Lin et al., 2025; Muragadoss et al., 2025）、RATE 方法论（Reber et al., 2025）、BT 在 NLP 评估中的应用，以及测量理论基础（Thurstone 1927, Stevens 1946, Krosnick 1999）。建议考虑补充：\n- Zheng et al. (2024) \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\" 的更详细讨论（虽已引用但可加强对比）\n- 如有 2025-2026 年关于 Likert scale limitations in NLG evaluation 的新工作，值得补充\n\n---\n\n## 格式合规检查\n\n| 检查项 | 结果 |\n|--------|------|\n| 正文 ≤ 8 页 | ✓ 合规。Sections 1-6 + Limitations 在 8 页内完成 |\n| Double-blind 匿名 | ✓ \"Anonymous ACL submission\"，未见作者信息 |\n| ACL 双栏格式 | ✓ 正确使用 |\n| Limitations 章节 | ✓ 存在，覆盖 3 个要点（evaluator-producer bias、methodology/scale design、ecological validity），篇幅适中 |\n| ARR Checklist | ✓ 不在 PDF 中（符合规定：在 OpenReview form 中填写） |\n| 参考文献格式 | ✓ 一致，未见明显格式问题 |\n\n---\n\n## Detailed Comments by Section\n\n### Section 1 (Introduction)\n- 开头的\"average height for a male\"例子直观有效，但\"causal variant\"措辞暗示了正式的因果推断，与 Section 3.5 的 hedging 不一致（参见 W1）。\n- \"70–92% of observed preferences originate from surface-level style cues\"的引用（Muragadoss et al., 2025; Sournik et al., 2020）——确认这些引用的测量方法是否与本文的 CSD 可比。\n\n### Section 2 (Related Work)\n- 覆盖全面，将 CSD 与 RATE（Reber et al., 2025）的区别阐述清楚（per-axis isolation + NLI gate + forced-choice vs. Likert ATE + post-hoc correction）。\n- \"CASSE (Cho et al., 2026)\"和\"FairJudge (Yang et al., 2026)\"是 concurrent work，能否简要讨论 CSD 与它们的互补性？\n\n### Section 3 (Method)\n- Section 3.1: Style-controlled rewriting 的 prompt 设计（binary classification → opposite pole rewriting）清晰。但\"a distant balanced pair where the rewrite changed only in style\"的表述过强——NLI gate 保证 semantic content 不变，但 writing quality/fluency 可能随改写发生变化（Table 15 的 double-rewrite 数据证实了这一点）。\n- Section 3.2: NLI gate 的 bidirectional entailment 要求合理。Direction-aware verbosity gating 的 rationale（增加内容不违反 forward entailment）在直觉上合理，但需量化其影响（参见 W4）。\n- Section 3.3: BT 使用所有 observations（含 inconsistent pairs）是标准做法，且 Section 3.3 有 justification。但未讨论 inconsistent pair rate——如果 inconsistency 率很高（如 >30%），可能表明 judges 在边界 cases 上 noise 很大。\n- Section 3.5: DAG (Figure 2) 标注为\"design rationale\"是恰当的。三个识别假设清晰。但假设 (iii)（\"style rewrite introduces no systematic differences beyond the target axis\"）是最关键的，且最难验证。Same-style double-rewrite（Appendix O）提供了部分验证，但它只检验了 within-style rewriting artifact，不检验 cross-style rewriting 是否引入了 axis 之外的 confound。\n\n### Section 4 (Experiments)\n- Section 4.1: Primary family 定义的透明度问题（参见 N1）。Exploratory vs. confirmatory 分类的逻辑应更 explicit。\n- Section 3.4 / 4: LLMBar (n = 100, post-NLI n = 88) 是一个小到中等的 benchmark。scaled replication (n = 355) 仅覆盖 formality × Qwen3-32B 一个 cell，对 generalizability 的支持有限。\n\n### Section 5 (Analysis)\n- Section 5.1: NLI gate validation 的 FNR 估计样本量过小（参见 W3）。GPT-4o cross-validation (92.1% / 82.6% precision) 是一个好的补充验证。\n- Section 5.2: Likert vs. Pairwise 灵敏度比较是论文的核心贡献。Figure 4 的 detection probability 曲线直观展示了两种方法的分离——BT 在 n ≈ 62 达到 80% power，而 Likert ATE 在 n = 355 仍然 flat near zero。这是强有力的 evidence。\n- Section 5.3: Cross-judge replication（三个独立 judges replicate the Blindspot）增强了结论的稳健性。\n- Section 5.4: Cross-axis replication for verbosity 跨四个 judges 一致——这是最一致的发现。\n- Section 5.5: Register 作为 judge-dependent confound 的发现有趣但仅为 exploratory。\n- Section 5.6: GEE conditional decomposition 是论文的第二个主要贡献。Table 3 的 per-axis confound structure 是新颖的。但部分 CI 很宽（参见 Minor）。\n\n### Section 6 (Conclusion)\n- 两个主要发现的总结清晰。\"whether this reflects measurement attenuation or construct divergence\"的 framing 诚实但留下了悬念（参见 W5）。\n\n### Limitations\n- 覆盖了关键点。建议增加 ecological validity 讨论（参见 W6）和 cross-rewriter 覆盖不足的明确承认。\n\n---\n\n## 综合判断\n\n本文的核心贡献——Likert Blindspot 的系统性 demonstration——是扎实的。跨 5 个 judges、3 个 benchmarks 和 7 种统计方法的一致性令人信服。GEE decomposition 揭示的 per-axis confound structure 增添了深度。\n\n主要顾虑集中在三个方法论缺口：(1) primary family 构成未透明公开，影响 FWER 控制的可信度；(2) cross-rewriter 验证仅覆盖 1/4 target judges，限制了 rewriter-independence claim 的强度；(3) 负面控制的 TOST 等价边界过宽，无法有效排除中等 bias。\n\n这些问题均可在修改中解决。如果 N1-N3 得到充分回应（特别是 N1 的透明度和 N3 的 TOST re-framing），本文有潜力达到 4.0 (Conference) 的水平。当前评分 3.5 (Borderline Conference) 反映了这些未解决的方法论顾虑。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-22T03:34:41.858427+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4169
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-22T03:34:48.872451+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 603 · 2026-05-22T03:34:48.872796+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-22T03:34:54.093618+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-22T03:34:54.144410+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 606 · 2026-05-22T03:35:09.993756+00:00_

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
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 20

## Round 20

16 recorded events


### User

_source line 607 · 2026-05-22T03:35:48.532588+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿意见（完整原文）

**Overall Assessment**: 3.5 (Borderline Conference)

### Strengths
- S1. 实验设计严谨，控制充分（NLI gate + negative control + position control + cross-benchmark replication + cross-rewriter independence）
- S2. 7 种统计方法 sensitivity hierarchy + GEE per-axis confound decomposition 是 genuinely novel
- S3. Measurement attenuation vs. construct divergence 两种解释的公平讨论
- S4. 100-point continuous Likert 是关键控制实验
- S5. Claude Sonnet 4 negative control 的 discriminative validity
- S6. 与 RATE 的对比公平且建设性

### Must-Fix
- **N1 [critical]**: Novelty 定位不够诚实——Likert Blindspot 本质是 Thurstone (1927) forced-choice > rating 原理在 LLM judge 领域的 empirical demonstration，非概念新发现。论文整体叙事给人 "全新发现" 印象。需重新定位 novelty：从 "discovering the Blindspot" 调整为 "providing the first controlled, per-axis quantification of this psychometric phenomenon in LLM judges"。
- **N2 [critical]**: Detection vs. Amplification 问题未充分解决，缺少 human validation。六个独立 controls 虽然排除了部分 artifactual 解释，但不能在根本上区分 "pairwise 检测了真实偏差" vs. "pairwise 放大了微弱偏好"。需 human evaluation（至少 50 pairs）建立 baseline。

### Should-Fix
- **W1**: 仅 3 个风格轴（formality, verbosity, register）难以支撑 "framework" 级别泛化声明。
- **W2**: Table 1 信息密度过高，可读性差——5 judges × 3 benchmarks × 3 axes × 2 metrics，读者难以快速抓住核心 pattern。
- **W3**: Claude Sonnet 4 统计功效不足（n=87, TOST Δ=15pp 过宽）。
- **W4**: Rewriting artifact 处理略显草率——same-style double-rewrite 只控制 style-neutral polishing，style-specific polishing interaction 未讨论。
- **W5**: Introduction motivating example 准确性值得推敲——formality 改变可能合法影响 perceived quality，需 acknowledge 这一 nuance。

### Questions
- Q1: NLI threshold 0.98 的选择依据？（注：论文实际用的是 0.90，R2 可能笔误）
- Q2: 100-point continuous Likert 仅用 Qwen3-32B，其他 judges 是否也显示相同 pattern？
- Q3: GEE Table 3 中 formality confound 的 interaction 方向和强度？
- Q4: LLMBar 100 pairs 的 selection criteria？
- Q5: 后续研究计划区分 attenuation vs. divergence？

### Missing References
1. Girrbach et al. (2025/2026) "Likert or Not" — 研究 LLM 在 Likert scale 上的评分行为
2. PRePair (Jeong et al., 2025) — pairwise + pointwise 整合方法
3. Kambhatla et al. (2024/2025) — calibration/scoring bias

### Detailed Comments
- Abstract: 第一句 "near-perfect correlation" 过于绝对（76-92% ≠ near-perfect）
- Introduction: "black-box controlled framework" 可能 overclaim（NLI gate 需要 model probabilities？）
- §2 Related Work: 遗漏 acquiescence bias 和 central tendency bias
- §3.2: NLI threshold "0.98" 在主文缺 justification（注：实际为 0.90）
- §4.1: Primary family 选择标准需 justification
- §5.5: Register 叙述过于压缩
- §6: 结论适当但 practical implications 可再展开
- Limitations: 遗漏 human validation、3 轴限制、base sample 仅 100 pairs

---

请对以上每个 Must-Fix (N1-N2)、Should-Fix (W1-W5)、Questions (Q1-Q5) 逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-22T03:36:37.441446+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf",
  "pages": "1-2,5,8",
  "project": "causal_style_decomp_judge",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf",
    "pages": "1-2,5,8",
    "project": "causal_style_decomp_judge",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-22T03:36:38.245450+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 468.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.5}], \"total_pages\": 15, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-22T03:36:40.805268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-22T03:36:41.309481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 612 · 2026-05-22T03:36:42.264158+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1458
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-22T03:36:42.265370+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-22T03:36:42.265682+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 615 · 2026-05-22T03:36:42.517482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 616 · 2026-05-22T03:36:43.070452+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-22T03:36:43.372343+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-22T03:39:16.857133+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: Novelty 定位不够诚实**\n\n同意方向，但认为 R2 略有过度。论文 Section 2 (\"Measurement Sensitivity in NLG Evaluation\") 已明确引用 Thurstone (1927)、Stevens (1946)、Hoening and Heisey (2001)，承认 forced-choice > rating 是已知原理。但 R2 的核心批评成立：论文标题 \"The Likert Blindspot\" 和 Abstract 整体叙事确实给出\"全新发现\"的印象，而非\"已知心理测量原理在 LLM judge 领域的首次系统实证\"。\n\n不过需要补充一个 nuance：LLM judges 并非人类 rater——它们的内部评分机制不同。LLM judges 表现出与人类相同的 psychometric 脆弱性这一事实本身不是 trivial 的。并且论文的贡献不仅是\"验证已知原理\"，还包括：(1) per-axis 量化（severity spectrum from complete attenuation to >60% signal loss）, (2) GEE conditional decomposition 揭示的 confound structure（Table 3），(3) 100-point continuous scale 排除 granularity（Appendix M）。这些是超越 Thurstone (1927) 的新 empirical insight。\n\nR2 建议的 reframing（\"providing the first controlled, per-axis quantification of this psychometric phenomenon in LLM judges\"）是精准的，我支持这一修改方向。\n\n**[AGREE] R2-N2: Detection vs. Amplification 缺 human validation**\n\n同意这是一个 genuine gap。论文的六个 controls 排除了 specific artifacts：\n- NLI gate → 内容变化\n- Position balancing → 顺序效应\n- Consistency filter → 随机噪声\n- Cross-rewriter (Appendix D) → rewriter-specific artifacts\n- Negative control (Appendix G) → false positives\n- Same-style double-rewrite (Appendix O) → polishing artifact\n\n但没有一个 control 能回答：pairwise 检测到的偏好是否对应人类也能感知到的 bias？论文 Section 5.6 和 Conclusion 正确地将此定义为开放问题（\"whether this reflects measurement attenuation or construct divergence\"），但这个歧义是论文结论的根基性不确定性。\n\n不过，我认为 R2 要求\"至少 50 pairs 的 human evaluation\"作为 Must-Fix 可能过高。原因：(1) 论文的核心贡献是 methodology + empirical demonstration，不是 resolve the interpretive question；(2) 50 pairs 的人类评估如果质量不高（inter-annotator agreement 低），反而可能引入更多噪声。建议将此 **降级为 Strong Should-Fix**：论文应在 Limitations 中明确承认缺少 human baseline 是主要局限，并 acknowledge 当前无法区分 detection vs. amplification。如果作者能在 rebuttal 中提供哪怕 30 pairs 的 pilot human evaluation 数据，将显著增强说服力。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: 3 个风格轴限制 \"framework\" 泛化声明**\n\n同意。Section 2 contribution 列表中 \"A black-box controlled framework for per-axis style bias detection\" 的 \"framework\" 措辞暗示了广泛适用性，但仅 3 个轴的实证覆盖有限。特别是 register 仅为 exploratory（Section 5.5），实质上只有 2 个轴有 confirmatory evidence。\n\n但 CSD 的方法论设计确实是 axis-agnostic 的（给定任何可改写的风格轴，pipeline 均可运行），3 个轴作为初始 demonstration 不算不合理。建议作者在 contribution 中将 \"framework\" 修改为 \"methodology\"（降低泛化预期），并在 Limitations 中明确讨论未覆盖的重要轴（如 tone/politeness, complexity, specificity）。\n\n**[AGREE] R2-W2: Table 1 信息密度过高**\n\n同意。5 judges × 3 benchmarks × 3 axes × 2 metrics + significance markers + footnotes 在一张表中确实 overloaded。读者需要花大量时间才能提取核心 pattern（即\"BT significant where Likert non-significant\"）。\n\n建议：(1) 将 Table 1 拆分为两个子表（main benchmark LLMBar + scaled replications），或 (2) 增加一个 summary visualization（如 Figure 3 的 BT probability 图已部分承担了这个角色，但缺少 Likert 对比）。\n\n**[AGREE] R2-W3: Claude Sonnet 4 统计功效不足**\n\n强烈同意。这与我的 N3 完全一致。n = 87、Δ = 15pp 的 TOST 无法有效区分\"无 bias\"和\"中等 bias\"。论文确认的最小 bias 为 +13pp（GPT-4o formality, Table 1: BT 60.7%），而 Δ = 15pp 几乎涵盖这一范围。\n\n补充一个 R2 未提及的细节：Appendix G 明确承认\"Δ = 10pp is underpowered at n = 87\"，这意味着作者知道功效不足但选择了更宽的 Δ 来让结果 \"work\"。这不是统计上的 best practice。\n\n**[PARTIALLY AGREE] R2-W4: Rewriting artifact 的 style-specific polishing interaction 未讨论**\n\n部分同意。R2 的关切有道理：same-style double-rewrite（Appendix O, Table 15）控制了 style-neutral polishing（LLM 改写普遍提升质量），但未控制 style-specific polishing（LLM 改写到不同风格时质量提升是否不同，如改写为 formal 可能比改写为 casual 产生更高质量的输出）。\n\n但需要指出：论文的实验设计中，main comparison 的 BT estimate 对 polishing artifact 是 robust 的——因为两个方向的改写（formal→casual 和 casual→formal）在 balanced design 中 polishing 效果应相互抵消。Appendix H 的 stratified analysis 部分地检验了这一点：verbosity 无方向异质性（Fisher's p = 0.43），但 formality 有（68.9% vs. 52.6%, Fisher's p = 0.015）。这个 formality 方向异质性可能部分来自 style-specific polishing interaction，而不仅是 R1 和论文归因的 originality confound。\n\n建议：在 Limitations 或 Appendix O 中明确讨论 style-specific polishing interaction 的可能性，并承认 formality 方向异质性可能混合了 originality confound 和 style-specific polishing 两种机制。\n\n**[AGREE] R2-W5: Introduction motivating example 需 acknowledge formality-quality nuance**\n\n同意。Introduction 第一段的 \"average height\" 例子暗示 formality bias 是完全不合理的（\"Same judge, same text, opposite conclusions\"）。但论文自己的 GEE 结果（Table 3）显示 formality 存在 significant Originality effect——即 formality 与 original content quality 存在 conditional relationship。这意味着 judge 偏好 formal 文本可能部分反映了合理的质量判断（formal writing 确实在某些场景下更精确、更结构化），而非纯粹的\"bias\"。\n\nIntroduction 应 acknowledge 这一 nuance：not all formality preference is irrational bias, and the paper's own GEE decomposition quantifies the rational vs. irrational components.\n\n---\n\n### Questions\n\n**[AGREE] R2-Q1**: R2 写的\"NLI threshold 0.98\"应为论文实际使用的 0.90（Section 3.2）。这是 R2 的笔误。但底层问题有效：论文主文确实没有对 0.90 的选择给出充分 inline justification，需要读者翻到 Appendix E (Table 8) 的 11-threshold sweep 才能理解。建议在 Section 3.2 增加一句简要 justification（如\"chosen as the plateau onset in a sweep across 11 thresholds, Appendix E\"）。\n\n**[AGREE] R2-Q2**: 100-point continuous Likert（Appendix M）仅测试 Qwen3-32B，generalizability 未验证。这与我在 Round 1 中对 appendix 分析覆盖面的关切一致。至少再测试一个 judge（如 GPT-4o）会显著增强此控制实验的说服力。\n\n**[AGREE] R2-Q3**: GEE interaction direction — Appendix C 明确报告\"no significant interactions in any of the nine judge×axis cells (all p > 0.13, range 0.14–0.96)\"，但确实没有报告 interaction 的 point estimates 和 direction。对于 formality 这个已知有 conditional confounding 的轴，报告 interaction term 的 coefficients（即使不显著）会有信息价值。\n\n**[AGREE] R2-Q4**: LLMBar 100 pairs 的 selection criteria — Section 3.4 引用 Zeng et al. (2024) 并描述为\"n = 100 instruction-response pairs spanning diverse task types, designed to test LLM judges' ability to distinguish response quality with human-verified quality labels\"。但没有说明是从 LLMBar 全集中 sample 还是用了完整 benchmark。如果是 subsample，selection criteria 很重要；如果是完整 benchmark，应明确声明。\n\n**[AGREE] R2-Q5**: 后续区分 attenuation vs. divergence — 这是一个好的 forward-looking question。如果作者能在 response 中概述计划（如 human evaluation protocol、更大样本量的 Likert 实验、或 within-subject design 同时收集两种 measurement），会增强论文的 contribution positioning。\n\n---\n\n### Missing References\n\n**[PARTIALLY AGREE]** R2 建议的三篇参考文献方向合理：\n1. **Girrbach et al. \"Likert or Not\"**: 如果确实研究 LLM 在 Likert scale 上的评分行为，与本文直接相关，应引用。\n2. **PRePair (Jeong et al., 2025)**: 论文已在 Section 2 引用了 Jeong et al. (2025) 关于 Comparative Trap，但 PRePair 的 pairwise + pointwise 整合方法如果不同于 Jeong et al. (2025)，值得补充。\n3. **Kambhatla et al.**: calibration/scoring bias 相关，合理补充。\n\n需要确认这些文献是否真实存在且已发表/预印——reviewer 建议的 missing references 有时也需要 verify。\n\n---\n\n### Detailed Comments\n\n**[AGREE]** Abstract \"near-perfect correlation\": 论文引用 \"70–92% of observed preferences originate from surface-level style cues\"。70% 不是 \"near-perfect\"（通常暗示 >95%）。应修改为 \"strong correlation\" 或 \"high correlation\"。\n\n**[REBUT]** \"black-box controlled framework\" overclaim: R2 怀疑 NLI gate 需要 model probabilities，暗示 CSD 不是 black-box。但这是对论文的误读——\"black-box\"指的是 **judge** 是 black-box（CSD 不需要访问 judge 的内部状态），而非整个 pipeline。NLI gate 使用的是独立的 DeBERTa 模型（Section 3.2），不涉及 judge 的 probabilities。论文明确说\"requires no access to judge internals and applies post-hoc to any black-box judge\"（Section 1）。这一表述准确。\n\n**[AGREE]** §2 遗漏 acquiescence bias 和 central tendency bias: 这是 Likert scale 的经典心理测量问题，与论文讨论的 Likert limitations 直接相关。一句话的 mention 即可（不需要大篇幅讨论）。\n\n**[AGREE]** §4.1 Primary family 选择标准: 与我的 N1 一致，需要明确哪三个 judges 在 primary family 中及排除理由。\n\n**[AGREE]** §5.5 Register 叙述压缩: Register 结果确实过于压缩，但在 8 页限制下可以理解。如果空间允许，增加 1-2 句关于 register 的 judge-dependent pattern 会有帮助。\n\n---\n\n### 综合评估\n\nR2 的审稿整体质量高，大部分关切有据。最有力的两个点是 **N1（novelty 定位）** 和 **N2（detection vs. amplification）**——前者是 framing 问题（可修复），后者是 fundamental limitation（难以在本文完全解决但可通过 Limitations 重写和 pilot human data 部分 mitigate）。\n\nR2 的 Should-Fix 中 **W3（TOST 功效）** 与我的 N3 完全吻合，**W4（style-specific polishing）** 和 **W5（formality-quality nuance）** 是我 Round 1 未充分覆盖的有价值补充。\n\n我与 R2 的主要分歧在于：\n1. **N2 的严重程度**：R2 列为 Must-Fix 要求 human evaluation，我认为应降为 Strong Should-Fix——论文可以通过更诚实的 Limitations 讨论部分 mitigate，完整的 human evaluation 更适合作为 follow-up work。\n2. **\"black-box\" 表述**：R2 认为 overclaim，我认为论文对\"black-box\"的使用是准确的（指 judge 而非 pipeline）。\n\n**维持我的 Overall Assessment: 3.5 (Borderline Conference)**，与 R2 一致。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: Novelty 定位不够诚实**\n\n同意方向，但认为 R2 略有过度。论文 Section 2 (\"Measurement Sensitivity in NLG Evaluation\") 已明确引用 Thurstone (1927)、Stevens (1946)、Hoening and Heisey (2001)，承认 forced-choice > rating 是已知原理。但 R2 的核心批评成立：论文标题 \"The Likert Blindspot\" 和 Abstract 整体叙事确实给出\"全新发现\"的印象，而非\"已知心理测量原理在 LLM judge 领域的首次系统实证\"。\n\n不过需要补充一个 nuance：LLM judges 并非人类 rater——它们的内部评分机制不同。LLM judges 表现出与人类相同的 psychometric 脆弱性这一事实本身不是 trivial 的。并且论文的贡献不仅是\"验证已知原理\"，还包括：(1) per-axis 量化（severity spectrum from complete attenuation to >60% signal loss）, (2) GEE conditional decomposition 揭示的 confound structure（Table 3），(3) 100-point continuous scale 排除 granularity（Appendix M）。这些是超越 Thurstone (1927) 的新 empirical insight。\n\nR2 建议的 reframing（\"providing the first controlled, per-axis quantification of this psychometric phenomenon in LLM judges\"）是精准的，我支持这一修改方向。\n\n**[AGREE] R2-N2: Detection vs. Amplification 缺 human validation**\n\n同意这是一个 genuine gap。论文的六个 controls 排除了 specific artifacts：\n- NLI gate → 内容变化\n- Position balancing → 顺序效应\n- Consistency filter → 随机噪声\n- Cross-rewriter (Appendix D) → rewriter-specific artifacts\n- Negative control (Appendix G) → false positives\n- Same-style double-rewrite (Appendix O) → polishing artifact\n\n但没有一个 control 能回答：pairwise 检测到的偏好是否对应人类也能感知到的 bias？论文 Section 5.6 和 Conclusion 正确地将此定义为开放问题（\"whether this reflects measurement attenuation or construct divergence\"），但这个歧义是论文结论的根基性不确定性。\n\n不过，我认为 R2 要求\"至少 50 pairs 的 human evaluation\"作为 Must-Fix 可能过高。原因：(1) 论文的核心贡献是 methodology + empirical demonstration，不是 resolve the interpretive question；(2) 50 pairs 的人类评估如果质量不高（inter-annotator agreement 低），反而可能引入更多噪声。建议将此 **降级为 Strong Should-Fix**：论文应在 Limitations 中明确承认缺少 human baseline 是主要局限，并 acknowledge 当前无法区分 detection vs. amplification。如果作者能在 rebuttal 中提供哪怕 30 pairs 的 pilot human evaluation 数据，将显著增强说服力。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: 3 个风格轴限制 \"framework\" 泛化声明**\n\n同意。Section 2 contribution 列表中 \"A black-box controlled framework for per-axis style bias detection\" 的 \"framework\" 措辞暗示了广泛适用性，但仅 3 个轴的实证覆盖有限。特别是 register 仅为 exploratory（Section 5.5），实质上只有 2 个轴有 confirmatory evidence。\n\n但 CSD 的方法论设计确实是 axis-agnostic 的（给定任何可改写的风格轴，pipeline 均可运行），3 个轴作为初始 demonstration 不算不合理。建议作者在 contribution 中将 \"framework\" 修改为 \"methodology\"（降低泛化预期），并在 Limitations 中明确讨论未覆盖的重要轴（如 tone/politeness, complexity, specificity）。\n\n**[AGREE] R2-W2: Table 1 信息密度过高**\n\n同意。5 judges × 3 benchmarks × 3 axes × 2 metrics + significance markers + footnotes 在一张表中确实 overloaded。读者需要花大量时间才能提取核心 pattern（即\"BT significant where Likert non-significant\"）。\n\n建议：(1) 将 Table 1 拆分为两个子表（main benchmark LLMBar + scaled replications），或 (2) 增加一个 summary visualization（如 Figure 3 的 BT probability 图已部分承担了这个角色，但缺少 Likert 对比）。\n\n**[AGREE] R2-W3: Claude Sonnet 4 统计功效不足**\n\n强烈同意。这与我的 N3 完全一致。n = 87、Δ = 15pp 的 TOST 无法有效区分\"无 bias\"和\"中等 bias\"。论文确认的最小 bias 为 +13pp（GPT-4o formality, Table 1: BT 60.7%），而 Δ = 15pp 几乎涵盖这一范围。\n\n补充一个 R2 未提及的细节：Appendix G 明确承认\"Δ = 10pp is underpowered at n = 87\"，这意味着作者知道功效不足但选择了更宽的 Δ 来让结果 \"work\"。这不是统计上的 best practice。\n\n**[PARTIALLY AGREE] R2-W4: Rewriting artifact 的 style-specific polishing interaction 未讨论**\n\n部分同意。R2 的关切有道理：same-style double-rewrite（Appendix O, Table 15）控制了 style-neutral polishing（LLM 改写普遍提升质量），但未控制 style-specific polishing（LLM 改写到不同风格时质量提升是否不同，如改写为 formal 可能比改写为 casual 产生更高质量的输出）。\n\n但需要指出：论文的实验设计中，main comparison 的 BT estimate 对 polishing artifact 是 robust 的——因为两个方向的改写（formal→casual 和 casual→formal）在 balanced design 中 polishing 效果应相互抵消。Appendix H 的 stratified analysis 部分地检验了这一点：verbosity 无方向异质性（Fisher's p = 0.43），但 formality 有（68.9% vs. 52.6%, Fisher's p = 0.015）。这个 formality 方向异质性可能部分来自 style-specific polishing interaction，而不仅是 R1 和论文归因的 originality confound。\n\n建议：在 Limitations 或 Appendix O 中明确讨论 style-specific polishing interaction 的可能性，并承认 formality 方向异质性可能混合了 originality confound 和 style-specific polishing 两种机制。\n\n**[AGREE] R2-W5: Introduction motivating example 需 acknowledge formality-quality nuance**\n\n同意。Introduction 第一段的 \"average height\" 例子暗示 formality bias 是完全不合理的（\"Same judge, same text, opposite conclusions\"）。但论文自己的 GEE 结果（Table 3）显示 formality 存在 significant Originality effect——即 formality 与 original content quality 存在 conditional relationship。这意味着 judge 偏好 formal 文本可能部分反映了合理的质量判断（formal writing 确实在某些场景下更精确、更结构化），而非纯粹的\"bias\"。\n\nIntroduction 应 acknowledge 这一 nuance：not all formality preference is irrational bias, and the paper's own GEE decomposition quantifies the rational vs. irrational components.\n\n---\n\n### Questions\n\n**[AGREE] R2-Q1**: R2 写的\"NLI threshold 0.98\"应为论文实际使用的 0.90（Section 3.2）。这是 R2 的笔误。但底层问题有效：论文主文确实没有对 0.90 的选择给出充分 inline justification，需要读者翻到 Appendix E (Table 8) 的 11-threshold sweep 才能理解。建议在 Section 3.2 增加一句简要 justification（如\"chosen as the plateau onset in a sweep across 11 thresholds, Appendix E\"）。\n\n**[AGREE] R2-Q2**: 100-point continuous Likert（Appendix M）仅测试 Qwen3-32B，generalizability 未验证。这与我在 Round 1 中对 appendix 分析覆盖面的关切一致。至少再测试一个 judge（如 GPT-4o）会显著增强此控制实验的说服力。\n\n**[AGREE] R2-Q3**: GEE interaction direction — Appendix C 明确报告\"no significant interactions in any of the nine judge×axis cells (all p > 0.13, range 0.14–0.96)\"，但确实没有报告 interaction 的 point estimates 和 direction。对于 formality 这个已知有 conditional confounding 的轴，报告 interaction term 的 coefficients（即使不显著）会有信息价值。\n\n**[AGREE] R2-Q4**: LLMBar 100 pairs 的 selection criteria — Section 3.4 引用 Zeng et al. (2024) 并描述为\"n = 100 instruction-response pairs spanning diverse task types, designed to test LLM judges' ability to distinguish response quality with human-verified quality labels\"。但没有说明是从 LLMBar 全集中 sample 还是用了完整 benchmark。如果是 subsample，selection criteria 很重要；如果是完整 benchmark，应明确声明。\n\n**[AGREE] R2-Q5**: 后续区分 attenuation vs. divergence — 这是一个好的 forward-looking question。如果作者能在 response 中概述计划（如 human evaluation protocol、更大样本量的 Likert 实验、或 within-subject design 同时收集两种 measurement），会增强论文的 contribution positioning。\n\n---\n\n### Missing References\n\n**[PARTIALLY AGREE]** R2 建议的三篇参考文献方向合理：\n1. **Girrbach et al. \"Likert or Not\"**: 如果确实研究 LLM 在 Likert scale 上的评分行为，与本文直接相关，应引用。\n2. **PRePair (Jeong et al., 2025)**: 论文已在 Section 2 引用了 Jeong et al. (2025) 关于 Comparative Trap，但 PRePair 的 pairwise + pointwise 整合方法如果不同于 Jeong et al. (2025)，值得补充。\n3. **Kambhatla et al.**: calibration/scoring bias 相关，合理补充。\n\n需要确认这些文献是否真实存在且已发表/预印——reviewer 建议的 missing references 有时也需要 verify。\n\n---\n\n### Detailed Comments\n\n**[AGREE]** Abstract \"near-perfect correlation\": 论文引用 \"70–92% of observed preferences originate from surface-level style cues\"。70% 不是 \"near-perfect\"（通常暗示 >95%）。应修改为 \"strong correlation\" 或 \"high correlation\"。\n\n**[REBUT]** \"black-box controlled framework\" overclaim: R2 怀疑 NLI gate 需要 model probabilities，暗示 CSD 不是 black-box。但这是对论文的误读——\"black-box\"指的是 **judge** 是 black-box（CSD 不需要访问 judge 的内部状态），而非整个 pipeline。NLI gate 使用的是独立的 DeBERTa 模型（Section 3.2），不涉及 judge 的 probabilities。论文明确说\"requires no access to judge internals and applies post-hoc to any black-box judge\"（Section 1）。这一表述准确。\n\n**[AGREE]** §2 遗漏 acquiescence bias 和 central tendency bias: 这是 Likert scale 的经典心理测量问题，与论文讨论的 Likert limitations 直接相关。一句话的 mention 即可（不需要大篇幅讨论）。\n\n**[AGREE]** §4.1 Primary family 选择标准: 与我的 N1 一致，需要明确哪三个 judges 在 primary family 中及排除理由。\n\n**[AGREE]** §5.5 Register 叙述压缩: Register 结果确实过于压缩，但在 8 页限制下可以理解。如果空间允许，增加 1-2 句关于 register 的 judge-dependent pattern 会有帮助。\n\n---\n\n### 综合评估\n\nR2 的审稿整体质量高，大部分关切有据。最有力的两个点是 **N1（novelty 定位）** 和 **N2（detection vs. amplification）**——前者是 framing 问题（可修复），后者是 fundamental limitation（难以在本文完全解决但可通过 Limitations 重写和 pilot human data 部分 mitigate）。\n\nR2 的 Should-Fix 中 **W3（TOST 功效）** 与我的 N3 完全吻合，**W4（style-specific polishing）** 和 **W5（formality-quality nuance）** 是我 Round 1 未充分覆盖的有价值补充。\n\n我与 R2 的主要分歧在于：\n1. **N2 的严重程度**：R2 列为 Must-Fix 要求 human evaluation，我认为应降为 Strong Should-Fix——论文可以通过更诚实的 Limitations 讨论部分 mitigate，完整的 human evaluation 更适合作为 follow-up work。\n2. **\"black-box\" 表述**：R2 认为 overclaim，我认为论文对\"black-box\"的使用是准确的（指 judge 而非 pipeline）。\n\n**维持我的 Overall Assessment: 3.5 (Borderline Conference)**，与 R2 一致。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-22T03:39:20.923892+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-22T03:39:27.616006+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-22T03:39:27.616626+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 622 · 2026-05-22T03:39:34.777628+00:00_

已完成对 Reviewer 2 全部意见的逐条回应并提交给 Director。

核心判断：R2 的 N1（novelty 定位）和 N2（detection vs. amplification）是有力的批评；W3（TOST 功效）与我的 N3 完全吻合。主要分歧在两点：(1) N2 我认为应降为 Strong Should-Fix 而非 Must-Fix；(2) R2 对"black-box"的 overclaim 质疑我明确反驳——论文的"black-box"指 judge 而非整个 pipeline，表述准确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 21

## Round 21

70 recorded events


### User

_source line 623 · 2026-05-22T09:12:59.941502+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查 **方法严谨性、实验设计、统计方法论**。

## 投稿信息
- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 提交）
- **Deadline**: 2026-05-25
- **格式要求**: ACL template, double-blind, 正文 8 页限制, references 不限页, Limitations 必须有但不计入页数
- **匿名规则**: double-blind（作者信息不可出现）
- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各章节在 `sections/` 子目录）
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf`

## 论文概述
题目: "The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition"
核心claim: Likert评分系统性地遗漏了pairwise comparison能检测到的风格偏差（Likert Blindspot），提出CSD框架（NLI-gated content control + per-axis style decomposition + position-controlled pairwise comparison）来量化LLM judges的风格偏差。

## 你的审查重点

### 1. 方法论严谨性
- CSD pipeline 的因果推断框架是否合理？§3.5 Design Rationale 中的 DAG 是否自洽？三个 identification assumptions 是否充分？
- NLI gate (DeBERTa-v3-large, threshold 0.90) 作为 content preservation 的唯一门控是否足够？单向/双向 entailment 的 axis-dependent 策略是否有理论依据？
- Style-controlled rewriting 是否真正只改变一个 style axis？是否有其他 confound 未被控制（例如 style axis 之间的 interaction）？
- Evaluator-producer overlap (Qwen3-32B 同时做 rewriter 和 judge) 的处理是否充分？

### 2. 统计方法论
- Holm-Bonferroni correction 的 family 定义（6-test primary + Gemini confirmatory 排除）是否合理？
- Bradley-Terry model 的使用是否恰当？IIA assumption 在这个 context 下是否成立？
- GEE conditional decomposition 的 exchangeable working correlation 假设是否合理？interaction test 是否充分？
- Power analysis 和 bootstrap attenuation analysis 的设计是否正确？
- 负对照 (Claude Sonnet 4) 的 TOST equivalence testing 是否设计合理？Δ=15pp margin 是否过宽？

### 3. 实验设计
- LLMBar (n=100) 作为主要 benchmark 的代表性如何？样本量是否足够支撑 claims？
- Cross-benchmark (AlpacaEval, MT-Bench) 验证是否充分？为什么只做了部分 judge×axis 组合？
- Register axis 作为 exploratory 的定位是否诚实？与 formality/verbosity 的方法论差异（缺少 cross-rewriter validation）是否被充分 disclose？
- 负对照 (Claude Sonnet 4) 只在两个 axis 上测试是否足够？

### 4. 格式检查
- 正文是否在 8 页以内
- 是否 double-blind（无作者泄露信息）
- Limitations section 是否存在且合理
- 引用格式是否符合 ACL 规范

请按 ARR review form 格式输出你的审稿意见：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (1-5 scale per EMNLP 2026 ARR guidelines), Confidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-22T09:13:10.261513+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search ARR review form",
  "prompt": "Search the web for the official ACL Rolling Review (ARR) reviewer guidelines and review form criteria for 2026. I need:\n1. The exact dimensions/criteria reviewers score on (e.g., soundness, excitement, reproducibility, etc.)\n2. The scoring scales for each dimension\n3. Any specific instructions for reviewers\n\nTry these searches:\n- \"ACL Rolling Review reviewer guidelines 2026\"\n- \"ARR review form criteria dimensions\"\n- \"aclrollingreview.org reviewer guidelines\"\n\nReturn the full list of scoring dimensions with their scales and descriptions.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Search ARR review form",
    "prompt": "Search the web for the official ACL Rolling Review (ARR) reviewer guidelines and review form criteria for 2026. I need:\n1. The exact dimensions/criteria reviewers score on (e.g., soundness, excitement, reproducibility, etc.)\n2. The scoring scales for each dimension\n3. Any specific instructions for reviewers\n\nTry these searches:\n- \"ACL Rolling Review reviewer guidelines 2026\"\n- \"ARR review form criteria dimensions\"\n- \"aclrollingreview.org reviewer guidelines\"\n\nReturn the full list of scoring dimensions with their scales and descriptions.",
    "model": "sonnet"
  }
}
```

</details>

---


### Tool call

_source line 625 · 2026-05-22T09:13:12.670926+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 626 · 2026-05-22T09:13:12.771551+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 627 · 2026-05-22T09:13:16.289260+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer guidelines 2026 review form criteria",
  "allowed_domains": "['aclrollingreview.org', 'softconf.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer guidelines 2026 review form criteria",
    "allowed_domains": "['aclrollingreview.org', 'softconf.com']"
  }
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-22T09:13:16.741494+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR review form dimensions soundness excitement reproducibility scoring scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR review form dimensions soundness excitement reproducibility scoring scale"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-22T09:13:23.433347+00:00_

Web search results for query: "ACL Rolling Review reviewer guidelines 2026 review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

I found information about ACL Rolling Review (ARR) for 2026. Here's what the search results show about reviewer guidelines and review form criteria:

## Reviewer Guidelines

Reviewers are asked to read the paper and get the first impression, then search for related work. If qualified to review some aspects but not others, reviewers should state in the review if they did not check major parts, which helps the Area Chair understand what aspects were reviewed.

Reviewers are provided with a checkl
…[truncated 1048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7144
}
```

</details>

---


### Tool result

_source line 630 · 2026-05-22T09:13:26.246257+00:00_

Web search results for query: "ARR review form dimensions soundness excitement reproducibility scoring scale"

Links: [{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"}]

Based on the search results, here's information about the ARR (ACL Rolling Review) review form dimensions:

## Review Dimensions and Scoring

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness
The "soundness" score is meant to reflect the technical merit of the submission, and low soundness should be backed up with serious objections to the work. The soundness scores must be justified by the text of the review.

### Excitement
The "excitement" score is more subjective, and its justification may not be reflected in the text. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

### Overall Recommendation
The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also ot
…[truncated 559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9504
}
```

</details>

---


### Tool call

_source line 631 · 2026-05-22T09:13:31.364536+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract all review form dimensions/criteria, their scoring scales with full descriptions for each score level, and any specific instructions for reviewers. Include all fields and their complete descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract all review form dimensions/criteria, their scoring scales with full descriptions for each score level, and any specific instructions for reviewers. Include all fields and their complete descriptions."
  }
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-22T09:13:32.018933+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract all reviewer guidelines, including scoring dimensions, scales, and specific instructions for reviewers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract all reviewer guidelines, including scoring dimensions, scales, and specific instructions for reviewers."
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-22T09:13:38.189036+00:00_

# ARR Reviewer Guidelines: Scoring & Instructions

## Scoring Dimensions (as of February 2025)

ARR reviewers provide three scores:

1. **Soundness** - Technical validity and correctness. Must be justified by review text. "Low soundness scores without finding major faults" indicates an unfaithful assessment.

2. **Excitement** - Personal interest and appeal. Described as "subjective" and "orthogonal to soundness." Doesn't require explicit justification.

3. **Overall Assessment** - Composite recommendation reflecting soundness, excitement, novelty, and impact. "All papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible."

## Core Review Tasks

**Task 1:** Allocate calendar time for reviewing and discussion periods

**Task 2:** Verify assignment suitability
- Check expertise match and potential conflicts of interest
- Complete desk-rejection checklist (anonymity, ethics, style compliance, etc.)

**Task 3:** Write substantive reviews
- Read paper twice (skim, then in-depth)
- Be specific with criticisms
- Avoid common review pitfalls (listed as H1-H17)
- Watch for NLP paper problems (coded M1-M5, T1-T2, R1-R5, G1-G5)
- Ensure scores align with written assessment

**Task 4:** Engage after author response
- Acknowledge and address author rebuttals
- Participate in reviewer discussions
- Update scores if warranted

## Key Principles

- Maintain professional, neutral tone throughout
- Distinguish between fundamental weaknesses and suggestions
- Recognize valid contribution types beyond empirical SOTA improvements

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6170
}
```

</details>

---


### Tool result

_source line 634 · 2026-05-22T09:13:41.156047+00:00_

# ACL Rolling Review Form Dimensions & Criteria

## Review Form Dimensions

### 1. **Paper Summary**
Instruction to describe paper topic, highlighting understanding and potential misunderstandings for action editors and area chairs.

### 2. **Summary of Strengths**
Identifies major publication reasons: novel methodology, empirical results, theoretical analysis, literature organization, or reader value.

### 3. **Summary of Weaknesses**
Numbered concerns about correctness, limited impact, clarity, or reasons prioritizing other papers under consideration.

### 4. **Comments/Suggestions/Typos**
Space for improvement suggestions beyond addressing stated concerns.

### 5. **Reviewer Confidence** (1-5 Scale)
- **5**: "Positive that my evaluation is correct"
- **4**: "Quite sure" with unlikely but conceivable missed details
- **3**: "Pretty sure" but potentially missed specifics
- **2**: "Willing to defend" evaluation despite probable missed details
- **1**: Outside expertise or incomprehensible paper

### 6. **Soundness** (1-5 Scale with half-points)
- **5**: "one of the most thorough"
- **4**: Sufficient support with optional enhancements
- **3**: Sufficient main claims support, minor details needed
- **2**: "Main claims not sufficiently supported," major problems
- **1**: "not yet sufficiently thorough to warrant publication"

### 7. **Excitement** (1-5 Scale with half-points)
- **5**: "Highly Exciting" - recommend to others
- **4**: Mention to others, attempt conference attendance
- **3**: "Interesting" - potential selective mention
- **2**: May resonate with broader community
- **1**: "Not Exciting" - limited community relevance

### 8. **Overall Assessment** (1-5 Scale with half-points)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Substantial revisions needed
- **1**: "Do not resubmit" or irrelevant work

### 9. **Best Paper Justification**
Brief explanation for Award or Borderline Award ratings.

### 10.
…[truncated 1331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9791
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-22T09:14:03.809812+00:00_

以下是 ARR 官方 Review Form 的完整评分维度与标准：

---

## ARR Review Form 评分维度（2025-2026 有效）

### 核心评分维度（影响接收决定）

**Soundness**（技术可靠性，1-5，支持半分）
- 5 = Excellent：最严谨的工作之一
- 4 = Strong：所有 claim 均有充分支撑
- 3 = Good：主要 claim 有支撑，少量细节需补充
- 2 = Borderline：主要 claim 支撑不足，存在重大技术问题
- 1 = Poor：尚不足以达到发表水准

**Excitement**（个人兴趣/影响力，1-5，支持半分，主观，无需文字支撑）
- 5 = Highly Exciting：会主动推荐给他人
- 4 = Exciting：会向他人提及，愿意参加相关报告
- 3 = Interesting：选择性提及
- 2 = Borderline：可能与更广泛社区相关
- 1 = Not Exciting：社区相关度有限

**Overall Assessment**（综合推荐，1-5，支持半分）
- 5 = Consider for Award（约前 2.5%）
- 4.5 = Borderline Award
- 4 = Conference（可接收至主会议）
- 3.5 = Borderline Conference
- 3 = Findings（可接收至 Findings）
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle（需大幅修改）
- 1.5 = Resubmit after next cycle
- 1 = Do not resubmit

**Reviewer Confidence**（1-5）
- 5 = 完全确信评估正确
- 4 = 相当确信
- 3 = 大致确信但可能遗漏细节
- 2 = 愿意捍卫但可能有遗漏
- 1 = 不在专业领域或论文难以理解

---

### 资源与可复现性维度

**Reproducibility**（1-5）
- 5 = 可轻易复现结果
- 4 = 大致可复现，有少量差异
- 3 = 复现有些困难，参数未充分说明
- 2 = 数据不可获取，难以复现
- 1 = 无法复现

**Datasets**（1-5）
- 5 = Enabling（会影响研究项目选择）
- 4 = Useful
- 3 = Potentially useful
- 2 = Documentary utility
- 1 = 无可用数据集

**Software**（1-5）
- 5 = Enabling
- 4 = Useful
- 3 = Potentially useful
- 2 = Documentary utility
- 1 = 无可用软件

---

### 文字/结构性字段

- **Paper Summary**：描述论文主题，指出可能的理解偏差
- **Summary of Strengths**：列出主要优势（方法创新、实验结果、理论分析等）
- **Summary of Weaknesses**：编号列出主要问题
- **Comments/Suggestions/Typos**：小建议，不影响接收
- **Limitations and Societal Impact**：评估作者是否充分讨论了局限性和社会影响
- **Ethical Concerns**：对照 ACL Code of Ethics
- **Needs Ethics Review**：是否需要专项伦理委员会审查
- **Author Identity Knowledge**：是否已知作者身份（双盲合规性）
- **Best Paper Justification**：仅当 Overall = 5 或 4.5 时填写

---

### 关键原则（来自 Reviewer Guidelines）

1. Soundness 低分必须有具体技术缺陷支撑，不能无理由给低分
2. Excitement 是主观评分，与 Soundness 正交，不强制文字说明
3. Overall Assessment 综合 Soundness + Excitement + Novelty + Impact
4. Findings 接收标准主要看 Soundness 和 Reproducibility；主会议还额外看 Novelty 和 Impact
5. 作者 rebuttal 后需重新评估分数

Sources:
- [Review Form – ACL Rolling Review]
…[truncated 301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 53548
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-22T09:14:11.099148+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-22T09:14:11.149934+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-22T09:14:16.675729+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-22T09:14:17.983240+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 572.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p9.png\", \"w
…[truncated 515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1307
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-22T09:14:23.963114+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 641 · 2026-05-22T09:14:24.968485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 642 · 2026-05-22T09:14:25.321021+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool call

_source line 643 · 2026-05-22T09:14:25.321452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-22T09:14:25.874183+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-22T09:14:25.875445+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool result

_source line 646 · 2026-05-22T09:14:26.430242+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1108
}
```

</details>

---


### Tool call

_source line 647 · 2026-05-22T09:14:26.430674+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 648 · 2026-05-22T09:14:26.833015+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-22T09:14:27.235208+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-22T09:14:32.153907+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 651 · 2026-05-22T09:14:32.707791+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 652 · 2026-05-22T09:14:32.708967+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-22T09:14:33.613416+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-22T09:14:33.613851+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 655 · 2026-05-22T09:14:34.065637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 656 · 2026-05-22T09:14:34.519712+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 657 · 2026-05-22T09:14:34.520178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 658 · 2026-05-22T09:14:34.876795+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 811
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-22T09:14:35.279881+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 759
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-22T09:14:43.667412+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-22T09:14:44.369960+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 414.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 618.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 599.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 101.6}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 662 · 2026-05-22T09:14:48.593431+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-22T09:14:49.403473+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 810
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-22T09:14:49.504349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-22T09:14:49.504794+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-22T09:14:49.856107+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-22T09:14:50.308009+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-22T09:14:50.308414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-22T09:14:50.358809+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-22T09:14:51.262059+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-22T09:14:51.413154+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-22T09:14:51.463896+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-22T09:14:51.464402+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-22T09:14:55.426351+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/",
  "description": "List PDF image files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/",
    "description": "List PDF image files"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-22T09:14:55.577251+00:00_

Exit code 2
ls: cannot access '/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/': No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-22T09:15:01.759324+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "12-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "12-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-22T09:15:02.659552+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 414.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 618.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 599.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 101.6}], \"total_pages\": 16, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 900
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-22T09:15:12.606232+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-22T09:15:13.362144+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-22T09:15:13.462877+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 681 · 2026-05-22T09:15:14.015566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 682 · 2026-05-22T09:15:14.368911+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 683 · 2026-05-22T09:15:14.570464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 684 · 2026-05-22T09:15:14.872586+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 685 · 2026-05-22T09:15:14.973391+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 686 · 2026-05-22T09:15:14.975411+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-22T09:15:15.227158+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-22T09:16:59.904148+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-22T09:16:59.956452+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-22T09:18:55.525547+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 审稿意见 — 方法严谨性、实验设计、统计方法论\n\n### Paper Summary\n\n本文提出\"Likert Blindspot\"现象：Likert 评分系统性地遗漏 pairwise comparison 能检测到的 LLM judge 风格偏差。作者设计了 Controlled Style Decomposition (CSD) 框架——通过 NLI-gated content control、per-axis style rewriting、position-controlled pairwise comparison——在 4 个 target judge、3 个 benchmark、3 个 style axis 上量化该现象。七种统计方法一致确认：pairwise BT 概率在 formality 和 verbosity 上显著偏离 0.50（最高 BT 77.3%），而同一干预下 Likert ATE 始终不显著。Claude Sonnet 4 作为负对照未检出偏差，支持因果解读。\n\n---\n\n### Summary of Strengths\n\n**S1. 研究问题新颖且有实际影响。** Likert 与 pairwise 评估格式的系统性灵敏度差异此前被直觉认知但从未被控制实验量化。这一发现对依赖 Likert 评分的 leaderboard 和 alignment pipeline 有直接警示意义。\n\n**S2. 统计方法论严谨且多层次。** 七种统计方法（BT model、sign test、Likert ATE/t-test、binomial、ordinal regression、GEE、Wilcoxon signed-rank）交叉验证同一结论（Table 2），排除了结论对单一检验方法的依赖。Holm-Bonferroni correction 的 family 定义清晰（§4.1），exploratory/confirmatory 分类合理。\n\n**S3. 因果推断框架诚实定位。** §3.5 Design Rationale 明确表示 DAG 是\"design rationale, not a claim of perfect identification\"，三个 operational assumptions 逐一列出并在附录中提供了经验验证（NLI threshold sweep Appendix E, direction-aware gate Appendix F, cross-rewriter Appendix D/Tables 7-8），没有过度声称因果识别。\n\n**S4. 负对照设计有效。** Claude Sonnet 4 作为负对照（§5.4, Appendix G），在 formality 和 verbosity 上 BT ≈ 54-56%，TOST 确认等价性——为其他 judge 的显著偏差提供了有力的因果对比。\n\n**S5. 充分的 robustness 分析。** Bootstrap attenuation analysis（Appendix J, d = −0.017）排除了 measurement attenuation 解释；power analysis（Appendix K）量化了 Likert 达到 80% power 所需样本量（1,473–6,737），有力地论证了 Blindspot 的结构性本质。GEE exchangeable vs. independence working correlation 在 Appendix C 中报告了一致结果。\n\n**S6. 跨 benchmark/rewriter/judge 验证体系。** 主实验（LLMBar）+ cross-benchmark（AlpacaEval, MT-Bench）+ cross-rewriter（GPT-4o 独立 rewriter, Tables 7-8）+ cross-architecture（4 judge families）+ 负对照，形成了较完整的验证矩阵。\n\n---\n\n### Summary of Weaknesses\n\n**N1** [critical] **NLI gate 作为 content preservation 的唯一门控缺乏人工验证**\n- 具体位置：§3.2, Limitations (p.8)\n- 问题：CSD 的因果推断完全依赖 NLI gate（DeBERTa-v3-large, threshold 0.90）保证 content 不变。然而 NLI 模型本身可能存在系统性盲区——例如对隐含推理链的改变、对论证结构重组的不敏感。论文未报告对 NLI-gated pairs 的任何人工抽样验证（human evaluation of content preservation quality）。Limitations 中承认\"cannot block quality perception shifts mediated by style itself\"，但这一局限的严重性需要实证数据来界定——至少应抽样 50-100 对，让人工标注者判断 content 是否实质等价。\n- 为什么影响接收：这是 CSD 因果推断链条的最薄弱环节。如果 NLI gate 系统性地放过了某些 content 变化（例如 formal 改写倾向于增加 hedging 从而实质改变 claim 强度），则观测到的\"style bias\"可能部分是 content bias 的伪装。\n- 建议修改方向：对 NLI-passed 和 NLI-failed pairs 各抽样 50 对，收集 3 名标注者的 content equivalence 判断（binary: equivalent/not equivalent），报告 agreement 和 false-pass rate。\n\n**N2** [critical] **\"Likert Blindspot\" 的 framing 过于强势，忽视了 ordinal vs. forced-choice 灵敏度差异的已知理论背景**\n- 具体位置：Title, Abstract, §1 (\"This is the Likert Blindspot\"), §5.1\n- 问题：Likert（绝对评分）与 pairwise comparison（强制选择）的灵敏度差异是测量理论中的经典结论——Thurstone (1927) 已经指出 forced-choice 比 absolute rating 更能识别微小差异，Preston and Colman (2000) 等研究也系统探讨了 scale granularity 对 discriminability 的影响。论文在 §2 和 §5.1 确实引用了这些文献，也在 §5.1 讨论了\"measurement attenuation vs. construct divergence\"的两种解释，但标题和 abstract 的措辞将此现象包装为一个全新发现（\"Likert Blindspot\"），而实质上核心发现更准确地说是：**在 LLM judge 的具体场景下，对 style bias 这一特定效应，Likert 的灵敏度损失从理论预期升级为实践中的严重盲区**。论文的 bootstrap attenuation analysis（Appendix J）确实试图区分这两种解释，但 d = −0.017 的 attenuation 估计是在 n = 355 的 pairwise 数据上做的 subsampling，无法排除 Likert 和 pairwise 在construct 层面的差异。\n- 为什么影响接收：如果 reviewer 或 AC 认为论文的 novelty 建立在\"发现了一个新现象\"上，但该现象实际上是已知测量理论效应在新领域的实例化，则 novelty 评估会显著降低。\n- 建议修改方向：(1) 在 Abstract/Intro 中更明确地将 Blindspot 定位为 measurement theory 预测的在 LLM judge 场景下的**首次系统量化**，而非一个全新发现；(2) 在 §5.1 加强对 construct divergence vs. attenuation 的讨论，考虑是否 Likert 和 pairwise 实际测量的是不同构念（absolute quality vs. relative preference）。\n\n**W1** [warning] **NLI filtering 后样本量有限，cross-benchmark 覆盖不完整**\n- 具体位置：Table 1, §3.4, §5.3\n- 问题：LLMBar 原始 n=100，NLI filtering 后有效样本降至 55-88 对（取决于 axis 和 judge）。Cross-benchmark 验证（AlpacaEval n=50 sampled, MT-Bench 80 pairs）中 Table 1 有多个空白单元格（\"—\"），说明某些 judge×axis×benchmark 组合未被测试。论文未解释为何缺失这些组合——是因为 NLI pass rate 太低？还是 benchmark 不适用？\n- 建议：(1) 补充说明 Table 1 缺失单元格的原因；(2) 如果 NLI pass rate 是瓶颈，报告各 benchmark×axis 的 raw→filtered 样本量变化。\n\n**W2** [warning] **Style axis 之间的 interaction 和 cross-contamination 未被直接测试**\n- 具体位置：§3.1, §3.5 assumption (iii), Table 5\n- 问题：CSD 的第三个假设是 style rewrite 不引入 target axis 之外的系统性变化。Table 5 的 GEE interaction test（Style × Originality）显示无显著交互，但这只测试了 style 与 originality 的交互，而非 style axis 之间的交互（例如：formal 改写是否系统性地改变了 verbosity？verbose 改写是否改变了 formality？）。Appendix L (Verbosity Sensitivity Hierarchy) 中 register axis 的 attenuation pattern 与 formality/verbosity 不一致（\"inconsistent with uniform format amplification\"），暗示 cross-axis contamination 的可能。\n- 建议：(1) 对每个 axis 的改写样本，测量其他 axis 的变化幅度（例如用 classifier 或 LLM 打分）；(2) 或者至少讨论为什么 axis isolation 的假设在当前设计下是合理的。\n\n**W3** [warning] **负对照（Claude Sonnet 4）仅覆盖 2/3 axes，TOST Δ=15pp margin 偏宽**\n- 具体位置：§5.4, Appendix G\n- 问题：Claude Sonnet 4 的等价性测试仅覆盖 formality 和 verbosity，未覆盖 register。Δ=15pp 的 equivalence margin 意味着 Claude 可能存在高达 15pp 的 style preference 而仍被判定为\"无偏差\"——考虑到 GPT-4o formality 的 BT 偏差仅约 13pp，15pp 的 margin 已经与 target judges 的效应量相当接近。论文确认 minimum margin achieving 80% power at n=87 is Δ=15.7pp，说明当前设计对 Δ=15pp 的 TOST 是 underpowered 的。\n- 建议：(1) 讨论 Δ=15pp 的实质意义——是否足够\"小\"以构成有意义的负对照？(2) 增加 Claude 在 register axis 的测试；(3) 或者增加 Claude 的样本量以支持更窄的 equivalence margin。\n\n**W4** [warning] **Evaluator-producer overlap 的处理力度有限**\n- 具体位置：§5.3, Tables 7-8, Appendix D\n- 问题：Qwen3-32B 同时作为 rewriter 和 judge，存在 evaluator-producer overlap。Cross-rewriter 验证（GPT-4o 作为独立 rewriter）显示 Style OR 下降 22%（verbosity），但 Blindspot 持续存在。然而：(a) cross-rewriter 验证仅限于 Qwen3-32B judge，未覆盖其他 judges；(b) GPT-4o rewriter 产出的 formality BT 64.4% [56.1, 72.8] 的 CI 较宽，置信度有限。\n- 建议：明确量化 evaluator-producer overlap 的上界效应（例如：如果所有 judge 都使用独立 rewriter，效应量的预期衰减范围是多少？）。\n\n---\n\n### Questions for Authors\n\n**Q1.** NLI gate 的 false-pass rate 是多少？是否有人工验证数据？即便小规模抽样（e.g., 50 pairs），也能大幅增强 content preservation 声称的可信度。\n\n**Q2.** Table 1 中 cross-benchmark 结果的缺失单元格（\"—\"）代表什么？是未测试、NLI pass rate 为 0、还是其他原因？\n\n**Q3.** Bootstrap attenuation analysis（Appendix J）的 d = −0.017 如何排除 Likert 和 pairwise 在 construct 层面的根本差异？换言之，如果 Likert 测量的是 absolute quality 而 pairwise 测量的是 relative preference，那么二者对 style 的灵敏度差异可能反映的是 construct 差异而非 measurement deficiency。\n\n**Q4.** Formal 改写是否系统性地改变了文本的 verbosity 或 register？是否有定量证据支持 axis isolation？\n\n**Q5.** 为什么 Claude Sonnet 4 负对照不覆盖 register axis？是否有技术限制？\n\n---\n\n### Missing References\n\n- Preston, C. C., & Colman, A. M. (2000). Optimal number of response categories in rating scales. *Acta Psychologica* — 已引用 ✓\n- Thurstone, L. L. (1927) — 已引用 ✓\n- Krosnick, J. A. (1999). Survey research. *Annual Review of Psychology* — 已引用 ✓\n- 建议补充：Simms, L. J., Zelazny, K., Williams, T. F., & Bernstein, L. (2019). Does the number of response options matter? *Psychological Assessment* — 讨论 rating scale granularity 对 discriminability 的影响，与 Blindspot 现象直接相关。\n- 建议补充：Funke, F. (2016). A web experiment showing negative effects of slider scales compared to visual analogue scales and radio button scales. *Social Science Computer Research* — 涉及 response format 对 measurement sensitivity 的影响。\n\n---\n\n### Limitations and Societal Impact\n\nLimitations section（p.8）涵盖了关键局限：quality-style confounding, NLI gate 的边界, validation methodology and scale design。内容简洁覆盖了核心问题。但建议补充：(1) style axis 之间的 potential interaction；(2) 将 measurement theory 背景（ordinal vs. forced-choice sensitivity）作为一个 limitation 显式列出。\n\nSocietal影响未单独讨论，但考虑到论文性质（评估方法论研究），这不构成显著遗漏。\n\n---\n\n### Ethical Concerns\n\n无。论文使用公开 benchmark 数据，不涉及人类受试者，匿名合规。\n\n---\n\n### Author Identity Knowledge\n\n未知作者身份。论文 double-blind 合规，标题页标注\"Anonymous ACL submission\"，正文中未发现身份泄露。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论总体严谨，七种统计方法交叉验证，但 NLI gate 缺乏人工验证是因果链的关键缺口；Likert Blindspot 的 framing 未充分区分 measurement attenuation vs. construct divergence |\n| Excitement | 3.5/5 | 研究问题对 NLP evaluation 社区有实际价值，但核心发现部分可归于已知的 measurement theory 效应在新领域的实例化，novelty 略打折扣 |\n| Reproducibility | 4/5 | 实验细节充分（prompt template, NLI threshold, seed, bootstrap参数均报告），承诺代码和数据公开发布；但 NLI gate 的具体 prompt 和 style rewriting prompt 的完整模板未在论文中给出（可能在 appendix 但未完整覆盖） |\n| Overall Assessment | 3.5 | Borderline Conference — 方法严谨、发现有价值，但 NLI gate 人工验证缺失和 novelty framing 问题需要在 rebuttal 中充分回应 |\n| Confidence | 4/5 | 统计方法论和实验设计是我的专业领域，相当确信评估正确 |\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法论严谨、统计分析充分的 evaluation 方法论工作，核心发现（Likert 对 style bias 的结构性不敏感）有实际价值，但因果推断链的关键环节（NLI content preservation）缺乏人工验证，且\"Blindspot\"的 novelty framing 未充分处理与经典 measurement theory 的关系。\n",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 审稿意见 — 方法严谨性、实验设计、统计方法论\n\n### Paper Summary\n\n本文提出\"Likert Blindspot\"现象：Likert 评分系统性地遗漏 pairwise comparison 能检测到的 LLM judge 风格偏差。作者设计了 Controlled Style Decomposition (CSD) 框架——通过 NLI-gated content control、per-axis style rewriting、position-controlled pairwise comparison——在 4 个 target judge、3 个 benchmark、3 个 style axis 上量化该现象。七种统计方法一致确认：pairwise BT 概率在 formality 和 verbosity 上显著偏离 0.50（最高 BT 77.3%），而同一干预下 Likert ATE 始终不显著。Claude Sonnet 4 作为负对照未检出偏差，支持因果解读。\n\n---\n\n### Summary of Strengths\n\n**S1. 研究问题新颖且有实际影响。** Likert 与 pairwise 评估格式的系统性灵敏度差异此前被直觉认知但从未被控制实验量化。这一发现对依赖 Likert 评分的 leaderboard 和 alignment pipeline 有直接警示意义。\n\n**S2. 统计方法论严谨且多层次。** 七种统计方法（BT model、sign test、Likert ATE/t-test、binomial、ordinal regression、GEE、Wilcoxon signed-rank）交叉验证同一结论（Table 2），排除了结论对单一检验方法的依赖。Holm-Bonferroni correction 的 family 定义清晰（§4.1），exploratory/confirmatory 分类合理。\n\n**S3. 因果推断框架诚实定位。** §3.5 Design Rationale 明确表示 DAG 是\"design rationale, not a claim of perfect identification\"，三个 operational assumptions 逐一列出并在附录中提供了经验验证（NLI threshold sweep Appendix E, direction-aware gate Appendix F, cross-rewriter Appendix D/Tables 7-8），没有过度声称因果识别。\n\n**S4. 负对照设计有效。** Claude Sonnet 4 作为负对照（§5.4, Appendix G），在 formality 和 verbosity 上 BT ≈ 54-56%，TOST 确认等价性——为其他 judge 的显著偏差提供了有力的因果对比。\n\n**S5. 充分的 robustness 分析。** Bootstrap attenuation analysis（Appendix J, d = −0.017）排除了 measurement attenuation 解释；power analysis（Appendix K）量化了 Likert 达到 80% power 所需样本量（1,473–6,737），有力地论证了 Blindspot 的结构性本质。GEE exchangeable vs. independence working correlation 在 Appendix C 中报告了一致结果。\n\n**S6. 跨 benchmark/rewriter/judge 验证体系。** 主实验（LLMBar）+ cross-benchmark（AlpacaEval, MT-Bench）+ cross-rewriter（GPT-4o 独立 rewriter, Tables 7-8）+ cross-architecture（4 judge families）+ 负对照，形成了较完整的验证矩阵。\n\n---\n\n### Summary of Weaknesses\n\n**N1** [critical] **NLI gate 作为 content preservation 的唯一门控缺乏人工验证**\n- 具体位置：§3.2, Limitations (p.8)\n- 问题：CSD 的因果推断完全依赖 NLI gate（DeBERTa-v3-large, threshold 0.90）保证 content 不变。然而 NLI 模型本身可能存在系统性盲区——例如对隐含推理链的改变、对论证结构重组的不敏感。论文未报告对 NLI-gated pairs 的任何人工抽样验证（human evaluation of content preservation quality）。Limitations 中承认\"cannot block quality perception shifts mediated by style itself\"，但这一局限的严重性需要实证数据来界定——至少应抽样 50-100 对，让人工标注者判断 content 是否实质等价。\n- 为什么影响接收：这是 CSD 因果推断链条的最薄弱环节。如果 NLI gate 系统性地放过了某些 content 变化（例如 formal 改写倾向于增加 hedging 从而实质改变 claim 强度），则观测到的\"style bias\"可能部分是 content bias 的伪装。\n- 建议修改方向：对 NLI-passed 和 NLI-failed pairs 各抽样 50 对，收集 3 名标注者的 content equivalence 判断（binary: equivalent/not equivalent），报告 agreement 和 false-pass rate。\n\n**N2** [critical] **\"Likert Blindspot\" 的 framing 过于强势，忽视了 ordinal vs. forced-choice 灵敏度差异的已知理论背景**\n- 具体位置：Title, Abstract, §1 (\"This is the Likert Blindspot\"), §5.1\n- 问题：Likert（绝对评分）与 pairwise comparison（强制选择）的灵敏度差异是测量理论中的经典结论——Thurstone (1927) 已经指出 forced-choice 比 absolute rating 更能识别微小差异，Preston and Colman (2000) 等研究也系统探讨了 scale granularity 对 discriminability 的影响。论文在 §2 和 §5.1 确实引用了这些文献，也在 §5.1 讨论了\"measurement attenuation vs. construct divergence\"的两种解释，但标题和 abstract 的措辞将此现象包装为一个全新发现（\"Likert Blindspot\"），而实质上核心发现更准确地说是：**在 LLM judge 的具体场景下，对 style bias 这一特定效应，Likert 的灵敏度损失从理论预期升级为实践中的严重盲区**。论文的 bootstrap attenuation analysis（Appendix J）确实试图区分这两种解释，但 d = −0.017 的 attenuation 估计是在 n = 355 的 pairwise 数据上做的 subsampling，无法排除 Likert 和 pairwise 在construct 层面的差异。\n- 为什么影响接收：如果 reviewer 或 AC 认为论文的 novelty 建立在\"发现了一个新现象\"上，但该现象实际上是已知测量理论效应在新领域的实例化，则 novelty 评估会显著降低。\n- 建议修改方向：(1) 在 Abstract/Intro 中更明确地将 Blindspot 定位为 measurement theory 预测的在 LLM judge 场景下的**首次系统量化**，而非一个全新发现；(2) 在 §5.1 加强对 construct divergence vs. attenuation 的讨论，考虑是否 Likert 和 pairwise 实际测量的是不同构念（absolute quality vs. relative preference）。\n\n**W1** [warning] **NLI filtering 后样本量有限，cross-benchmark 覆盖不完整**\n- 具体位置：Table 1, §3.4, §5.3\n- 问题：LLMBar 原始 n=100，NLI filtering 后有效样本降至 55-88 对（取决于 axis 和 judge）。Cross-benchmark 验证（AlpacaEval n=50 sampled, MT-Bench 80 pairs）中 Table 1 有多个空白单元格（\"—\"），说明某些 judge×axis×benchmark 组合未被测试。论文未解释为何缺失这些组合——是因为 NLI pass rate 太低？还是 benchmark 不适用？\n- 建议：(1) 补充说明 Table 1 缺失单元格的原因；(2) 如果 NLI pass rate 是瓶颈，报告各 benchmark×axis 的 raw→filtered 样本量变化。\n\n**W2** [warning] **Style axis 之间的 interaction 和 cross-contamination 未被直接测试**\n- 具体位置：§3.1, §3.5 assumption (iii), Table 5\n- 问题：CSD 的第三个假设是 style rewrite 不引入 target axis 之外的系统性变化。Table 5 的 GEE interaction test（Style × Originality）显示无显著交互，但这只测试了 style 与 originality 的交互，而非 style axis 之间的交互（例如：formal 改写是否系统性地改变了 verbosity？verbose 改写是否改变了 formality？）。Appendix L (Verbosity Sensitivity Hierarchy) 中 register axis 的 attenuation pattern 与 formality/verbosity 不一致（\"inconsistent with uniform format amplification\"），暗示 cross-axis contamination 的可能。\n- 建议：(1) 对每个 axis 的改写样本，测量其他 axis 的变化幅度（例如用 classifier 或 LLM 打分）；(2) 或者至少讨论为什么 axis isolation 的假设在当前设计下是合理的。\n\n**W3** [warning] **负对照（Claude Sonnet 4）仅覆盖 2/3 axes，TOST Δ=15pp margin 偏宽**\n- 具体位置：§5.4, Appendix G\n- 问题：Claude Sonnet 4 的等价性测试仅覆盖 formality 和 verbosity，未覆盖 register。Δ=15pp 的 equivalence margin 意味着 Claude 可能存在高达 15pp 的 style preference 而仍被判定为\"无偏差\"——考虑到 GPT-4o formality 的 BT 偏差仅约 13pp，15pp 的 margin 已经与 target judges 的效应量相当接近。论文确认 minimum margin achieving 80% power at n=87 is Δ=15.7pp，说明当前设计对 Δ=15pp 的 TOST 是 underpowered 的。\n- 建议：(1) 讨论 Δ=15pp 的实质意义——是否足够\"小\"以构成有意义的负对照？(2) 增加 Claude 在 register axis 的测试；(3) 或者增加 Claude 的样本量以支持更窄的 equivalence margin。\n\n**W4** [warning] **Evaluator-producer overlap 的处理力度有限**\n- 具体位置：§5.3, Tables 7-8, Appendix D\n- 问题：Qwen3-32B 同时作为 rewriter 和 judge，存在 evaluator-producer overlap。Cross-rewriter 验证（GPT-4o 作为独立 rewriter）显示 Style OR 下降 22%（verbosity），但 Blindspot 持续存在。然而：(a) cross-rewriter 验证仅限于 Qwen3-32B judge，未覆盖其他 judges；(b) GPT-4o rewriter 产出的 formality BT 64.4% [56.1, 72.8] 的 CI 较宽，置信度有限。\n- 建议：明确量化 evaluator-producer overlap 的上界效应（例如：如果所有 judge 都使用独立 rewriter，效应量的预期衰减范围是多少？）。\n\n---\n\n### Questions for Authors\n\n**Q1.** NLI gate 的 false-pass rate 是多少？是否有人工验证数据？即便小规模抽样（e.g., 50 pairs），也能大幅增强 content preservation 声称的可信度。\n\n**Q2.** Table 1 中 cross-benchmark 结果的缺失单元格（\"—\"）代表什么？是未测试、NLI pass rate 为 0、还是其他原因？\n\n**Q3.** Bootstrap attenuation analysis（Appendix J）的 d = −0.017 如何排除 Likert 和 pairwise 在 construct 层面的根本差异？换言之，如果 Likert 测量的是 absolute quality 而 pairwise 测量的是 relative preference，那么二者对 style 的灵敏度差异可能反映的是 construct 差异而非 measurement deficiency。\n\n**Q4.** Formal 改写是否系统性地改变了文本的 verbosity 或 register？是否有定量证据支持 axis isolation？\n\n**Q5.** 为什么 Claude Sonnet 4 负对照不覆盖 register axis？是否有技术限制？\n\n---\n\n### Missing References\n\n- Preston, C. C., & Colman, A. M. (2000). Optimal number of response categories in rating scales. *Acta Psychologica* — 已引用 ✓\n- Thurstone, L. L. (1927) — 已引用 ✓\n- Krosnick, J. A. (1999). Survey research. *Annual Review of Psychology* — 已引用 ✓\n- 建议补充：Simms, L. J., Zelazny, K., Williams, T. F., & Bernstein, L. (2019). Does the number of response options matter? *Psychological Assessment* — 讨论 rating scale granularity 对 discriminability 的影响，与 Blindspot 现象直接相关。\n- 建议补充：Funke, F. (2016). A web experiment showing negative effects of slider scales compared to visual analogue scales and radio button scales. *Social Science Computer Research* — 涉及 response format 对 measurement sensitivity 的影响。\n\n---\n\n### Limitations and Societal Impact\n\nLimitations section（p.8）涵盖了关键局限：quality-style confounding, NLI gate 的边界, validation methodology and scale design。内容简洁覆盖了核心问题。但建议补充：(1) style axis 之间的 potential interaction；(2) 将 measurement theory 背景（ordinal vs. forced-choice sensitivity）作为一个 limitation 显式列出。\n\nSocietal影响未单独讨论，但考虑到论文性质（评估方法论研究），这不构成显著遗漏。\n\n---\n\n### Ethical Concerns\n\n无。论文使用公开 benchmark 数据，不涉及人类受试者，匿名合规。\n\n---\n\n### Author Identity Knowledge\n\n未知作者身份。论文 double-blind 合规，标题页标注\"Anonymous ACL submission\"，正文中未发现身份泄露。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论总体严谨，七种统计方法交叉验证，但 NLI gate 缺乏人工验证是因果链的关键缺口；Likert Blindspot 的 framing 未充分区分 measurement attenuation vs. construct divergence |\n| Excitement | 3.5/5 | 研究问题对 NLP evaluation 社区有实际价值，但核心发现部分可归于已知的 measurement theory 效应在新领域的实例化，novelty 略打折扣 |\n| Reproducibility | 4/5 | 实验细节充分（prompt template, NLI threshold, seed, bootstrap参数均报告），承诺代码和数据公开发布；但 NLI gate 的具体 prompt 和 style rewriting prompt 的完整模板未在论文中给出（可能在 appendix 但未完整覆盖） |\n| Overall Assessment | 3.5 | Borderline Conference — 方法严谨、发现有价值，但 NLI gate 人工验证缺失和 novelty framing 问题需要在 rebuttal 中充分回应 |\n| Confidence | 4/5 | 统计方法论和实验设计是我的专业领域，相当确信评估正确 |\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法论严谨、统计分析充分的 evaluation 方法论工作，核心发现（Likert 对 style bias 的结构性不敏感）有实际价值，但因果推断链的关键环节（NLI content preservation）缺乏人工验证，且\"Blindspot\"的 novelty framing 未充分处理与经典 measurement theory 的关系。\n",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-22T09:18:59.495813+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3970
}
```

</details>

---


### Assistant

_source line 692 · 2026-05-22T09:19:10.562473+00:00_

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
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 22

## Round 22

4 recorded events


### User

_source line 693 · 2026-05-22T09:22:09.450361+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应每个 Weakness 和 Question：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 的 Weaknesses

**N1** [critical] **新颖性定位：核心发现是"实证确认"而非"新发现"**
- 论文将 Likert Blindspot 包装为一个新发现（"reveal"），但 Thurstone (1927) 以来的测量理论已建立了 pairwise 相对于 rating scale 的敏感性优势。更准确的定位是：设计了一个框架（CSD）来在 LLM judge 场景下系统性地量化一个理论预测的测量敏感性差距，并在此过程中发现了 per-axis confound structure。
- 建议：从"我们发现了 Likert Blindspot"转向"我们设计 CSD 框架首次量化了这个理论预测的敏感性差距"，将 per-axis confound structure 提升为与 Blindspot quantification 平行的核心贡献。

**N2** [critical] **Pairwise "检测" vs. Pairwise "放大"：核心解释性歧义未充分解决**
- 论文的核心叙事假设 pairwise comparison 检测到了真实的风格偏差，而 Likert 遗漏了它。但替代解释是：pairwise comparison 放大了微小的、无关紧要的风格微偏好。论文在 §5.4 讨论了 6 个 experimental controls 来 bound this risk，但论证存在循环性：
  (a) 用 RLHF/DPO pipeline 的 pairwise preference 来论证 pairwise 检测到的是"真实"偏差——但这预设了 RLHF/DPO 的偏好反映真实偏差。
  (b) Bootstrap attenuation 排除了"纯粹是统计功效差异"，但不能排除 pairwise 系统性放大微小偏好。
  (c) "Both interpretations lead to the same conclusion" 不完全成立——如果 pairwise 放大噪声，用 pairwise 审计就会产生 false positives。
- 最理想方案：增加 human ground-truth 验证；次优方案：更 prominently 承认限制，避免 Conclusion 中使用 "reveal" 等暗示单一解释的语言。

**W1** [warning] **Style axis 覆盖面过窄，confound structure claim 的泛化基础不足**
- 仅 2 primary + 1 replication axes。LLM judge 的已知风格偏差远不止这些（bullet-point vs. prose、hedging level 等）。基于 3 个 axis 声称发现"per-axis confound structure"，分类法的泛化性缺乏支撑。

**W2** [warning] **NLI gate 高拒绝率（~44%）的选择偏差分析不足**
- NLI consistency filter 保留 55/98 pairs (56.1%)。Appendix B 报告 4 个 covariates 无显著差异，但可能不够全面。通过 NLI gate 的 pairs 可能系统性偏向内容更简单、风格变化更容易分离的文本。

**W3** [warning] **100-point continuous Likert 实验仅用单一 judge**
- Appendix M 旨在排除"Blindspot 是整数刻度粒度的人为产物"，但仅使用 Qwen3-32B。如果其他 judge 在 100-point scale 下表现不同，则该结论不成立。

**W4** [warning] **因果语言与实际方法论之间的张力**
- 标题中的 "Controlled" 和方法描述中的 "interventional" 语言暗示了比实际更强的因果识别。NLI gating 是近似的内容控制，而非 do-operator。Figure 2 的 DAG notation 也可能让因果推断背景的读者期望更严格的 identification strategy。

---

## Reviewer 2 的 Questions

**Q1.** 关于 N2（检测 vs. 放大）：是否有计划收集 human preference 判断来 ground-truth pairwise 检测到的风格偏差？

**Q2.** 关于 W1（style axes）：选择 formality 和 verbosity 作为 primary axes 的先验理由是什么？

**Q3.** 关于 Appendix D（rewriter independence）：GPT-4o 作为替代 rewriter 时，Style OR 下降 22%。这种下降是否暗示 Blindspot 的效应量部分依赖于 rewriter 的具体风格？

**Q4.** 关于 Section 5.4（Comparative Trap）：6 个 controls 只能排除"大规模放大"，无法排除"中等程度放大"。是否有办法量化 pairwise 的放大倍数？

---

请对以上每一条 Weakness（N1, N2, W1-W4）和 Question（Q1-Q4）逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-22T09:24:16.895573+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R2-N1: 新颖性定位：核心发现是\"实证确认\"而非\"新发现\"**\n\n同意，且与我自己的 N2 高度一致。论文的核心贡献更准确地说是：(1) 设计了 CSD 框架首次在 LLM judge 场景下系统量化了经典测量理论预测的 Likert/pairwise 灵敏度差距；(2) 发现了 per-axis confound structure（formality 是 style-dominated，register 是 judge-dependent）。将 Thurstone (1927) 以来已知的理论效应包装为\"reveal\"确实夸大了 novelty。论文在 §5.1 引用了 Thurstone 和 Preston & Colman (2000) 并讨论了 measurement attenuation vs. construct divergence，说明作者**意识到**这一理论背景，但 framing 选择（Title/Abstract/Conclusion 中的 \"reveal\"）未能准确反映这一关系。建议作者采纳 R2 的重新定位方案——将 CSD 框架设计和 per-axis confound structure 提升为并列核心贡献，\"Blindspot quantification\" 作为 empirical result 而非 discovery。\n\n---\n\n**[REBUT] R2-N2: Pairwise \"检测\" vs. Pairwise \"放大\"——部分反驳**\n\nR2 提出了一个合理的认识论问题，但我认为其论证力度被高估了，原因如下：\n\n(1) **负对照是反驳\"放大\"解释的最强证据。** Claude Sonnet 4 在相同的 pairwise comparison 设计下 BT ≈ 54-56%（§5.4, Appendix G），TOST 确认等价。如果 pairwise 的灵敏度本身系统性地放大了微小偏好，那么**所有 judge 都应表现出放大效应**，包括 Claude。Claude 的阴性结果证明 pairwise 检测到的是 judge-specific 的偏差，而非 format-induced 的普遍放大。R2 的 critique 未直接回应这一反驳。\n\n(2) **R2 对循环论证的指控部分成立但非致命。** R2 指出\"用 RLHF/DPO pipeline 的 pairwise preference 来论证 pairwise 检测到的是真实偏差\"存在循环性。我同意这在**本体论**层面是循环的（什么是\"真实\"偏差？），但在**操作层面**不循环：如果真实 alignment pipeline（RLHF/DPO）确实使用 pairwise comparison 格式，那么 pairwise 检测到的偏差就是**操作上相关的**偏差，无论它们在哲学层面是否\"真实\"。论文在 §5.4 也明确提到了 Comparative Trap（Jeong et al., 2025），说明作者意识到 pairwise 可能放大偏好。\n\n(3) **但我同意 R2 的一个核心关切：论文的 Conclusion 语言应更谨慎。** \"reveal\" 和 \"systematically misses\" 暗示了单一解释。更诚实的 framing 是：\"pairwise comparison detects style-correlated judge preferences that Likert scoring does not; whether these preferences represent genuine bias or format-amplified micro-preferences remains an open question with practical implications for both interpretations.\"\n\n(4) **关于 R2 的 \"both interpretations\" 批评：** R2 说 \"Both interpretations lead to the same conclusion 不完全成立——如果 pairwise 放大噪声，用 pairwise 审计就会产生 false positives\"。这一点在逻辑上是对的。但论文的论证不需要排除**所有**放大——它需要表明放大的上界是有限的。Cross-rewriter validation（Tables 7-8）中 Style OR 下降 22% 可被视为对 rewriter-specific amplification 的上界估计。\n\n**综合判断：** N2 提出的解释性歧义是真实存在的，但论文已通过负对照、cross-rewriter validation 和 Comparative Trap 讨论提供了充分的缓解。将其定为 critical 偏严——should-fix (warning) 更合适，主要修改是 Conclusion 语言的谨慎化。\n\n---\n\n**[AGREE] R2-W1: Style axis 覆盖面过窄**\n\n同意方向，但不同意严重程度。3 个 axis（2 primary + 1 exploratory）对于一篇**方法论论文**而言是合理的——CSD 框架的价值在于其通用性（可应用于任意 axis），而非穷举所有可能的偏差。论文在 Conclusion（p.8）也明确建议\"additional axes, larger benchmarks, and further judges are needed\"。但 R2 的核心关切——\"per-axis confound structure\" 这一 claim 基于仅 3 个 axis 的泛化基础不足——是合理的。建议作者将 \"per-axis confound structure\" 降级为 \"preliminary evidence of axis-dependent confound patterns\"，或增加 1-2 个 axis 的数据来加强泛化论证。\n\n---\n\n**[AGREE] R2-W2: NLI gate 高拒绝率的选择偏差分析不足**\n\n同意，且与我的 N1 相关联。44% 的拒绝率意味着分析结果只代表 NLI-filterable 的子集，而非全部文本。Appendix B 的 4 个 covariates（BERT score, text length, length difference, NLI score）检查了表面特征，但未检查更深层的特征——例如 filtered-in pairs 是否系统性偏向论证结构更简单（因此内容更容易保持不变）的文本。如果更复杂的文本在 rewriting 时更容易产生 content 变化从而被 NLI gate 拒绝，则保留的样本可能低估了 style bias 在复杂文本上的表现，或高估了 NLI gate 的有效性。建议补充对 filtered-in vs. filtered-out pairs 的语言复杂度（syntactic complexity, argument depth）对比分析。\n\n---\n\n**[AGREE] R2-W3: 100-point continuous Likert 仅用单一 judge**\n\n同意。Appendix M 的 100-point Likert 实验仅使用 Qwen3-32B，这限制了\"Blindspot 不是刻度粒度的产物\"这一结论的泛化性。如果 GPT-4o 或 Llama-3.3-70B 在 100-point scale 下 ATE 变为显著，则 Blindspot 对某些 judge 可能**确实**是粒度问题而非结构性问题。虽然补充所有 judge 的 100-point 实验可能成本较高，但至少应增加 1 个 judge（例如 GPT-4o，因为它是最常用的 benchmark judge）来增强结论的可信度。\n\n---\n\n**[REBUT] R2-W4: 因果语言与实际方法论的张力——部分反驳**\n\nR2 认为 \"Controlled\" 和 \"interventional\" 语言暗示了过强的因果识别。我认为论文在 §3.5 已经做了充分的对冲：\n\n- \"This DAG is a design rationale, not a claim of perfect identification\"（§3.5, p.4）\n- \"nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework\"（§3.5, p.4）\n- \"Our identification rests on three operational assumptions\"（§3.5, p.4）\n\n这些表述明确将因果 claim 降级为 \"operational assumptions\" 而非 formal identification。Figure 2 的 DAG 标注了 \"Assumed data-generating process (design rationale, not a claim of perfect identification)\"。\n\n但我同意 **Title 和 Abstract** 的语言（\"Controlled Style Decomposition\"）与 §3.5 的谨慎对冲之间存在张力。标题中的 \"Controlled\" 容易让因果推断背景的读者期望 do-calculus 层面的识别。建议：在 Abstract 中增加一句明确说明 \"controlled\" 指的是 \"experimentally controlled rewriting\" 而非 formal causal identification。\n\n**严重程度：** Warning 而非 critical。§3.5 的 disclaimer 足够明确，问题主要在 Title/Abstract 的措辞选择而非方法论本身。\n\n---\n\n### Questions 回应\n\n**[AGREE] R2-Q1: Human preference ground-truth**\n\n同意这是最理想的验证方案。与我的 N1 一致——NLI gate 作为 content preservation 的唯一门控，缺乏任何 human validation。收集 human preference 判断（例如让人类标注者对 NLI-gated pairs 进行 pairwise comparison，看人类是否也检测到 style bias）能同时验证两个假设：(a) NLI gate 确实保持了 content；(b) pairwise 检测到的偏差对人类也可观测。这将大幅增强论文的说服力。\n\n---\n\n**[REBUT] R2-Q2: Primary axes 的先验理由**\n\nR2 质疑 formality 和 verbosity 的选择缺乏先验理由。我认为论文在 §2（Related Work）已提供了充分的文献支撑：\n\n- Verbosity bias 是 LLM judge 文献中最 well-documented 的偏差（Zheng et al., 2023; Park et al., 2024; Dubois et al., 2025 均有报告）\n- Formality 与 RLHF preference 的关联在 Reber et al. (2025) 和 Shi et al. (2025) 中被讨论\n- 这两个 axis 有明确的可操作性（可通过 instruction 控制 rewriting），且与实际 deployment 场景直接相关\n\n选择 well-studied 的 axis 作为 primary 恰恰是正确的方法论策略——先在已知存在偏差的 axis 上验证框架的有效性，再扩展到探索性 axis（register）。这不是 weakness，而是合理的研究设计。\n\n---\n\n**[AGREE] R2-Q3: Style OR 下降 22% 的含义**\n\n同意这一观察的重要性。Tables 7-8 显示 GPT-4o 作为替代 rewriter 时 verbosity 的 Style OR 从~14 降至~10（约 22%），说明效应量确实部分依赖于 rewriter 身份。这意味着：(a) Blindspot 现象本身是 robust 的（跨 rewriter 持续存在），但 (b) 效应量的精确估计受 rewriter 风格影响。论文应更显著地承认这一点——\"Blindspot 的存在性是 robust 的，但其效应量有 ±20-25% 的 rewriter-dependent 变异\"。这与我的 W4 一致。\n\n---\n\n**[REBUT] R2-Q4: 量化 pairwise 放大倍数**\n\nR2 问是否有办法量化 pairwise 的放大倍数。我认为论文已提供了一个间接的上界估计：\n\n- Claude Sonnet 4 的 BT ≈ 54-56% 可被视为 pairwise format 的\"基线放大\"（如果存在的话）。这意味着 pairwise 在无偏差 judge 上的\"放大\"最多产生 ~6pp 的偏离（从 50% 到 56%）。\n- GPT-4o 的 BT 63-66% 与 Claude 的 54-56% 之间的差距（~8-10pp）则反映了 judge-specific bias 的下界。\n\n但我同意精确量化放大倍数需要 human ground-truth——如果人类对同一 pairs 的 pairwise preference 是 BT = X%，而 LLM judge 是 BT = Y%，则 Y/X 就是放大倍数。当前设计无法提供这一数据。这是 future work 而非当前论文的致命缺陷。\n\n---\n\n### 总结\n\nR2 的审稿意见整体质量高，与我的审查存在多处共鸣（novelty framing、NLI gate 验证、因果语言谨慎性）。核心分歧在 N2 的严重程度判定：R2 将 \"检测 vs. 放大\" 定为 critical，而我认为负对照已提供了充分缓解，应降为 warning。两份审稿意见共同指向的最大可 actionable 改进是：**增加 human evaluation 数据**（同时验证 content preservation 和 pairwise bias 的人类可观测性）。\n",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R2-N1: 新颖性定位：核心发现是\"实证确认\"而非\"新发现\"**\n\n同意，且与我自己的 N2 高度一致。论文的核心贡献更准确地说是：(1) 设计了 CSD 框架首次在 LLM judge 场景下系统量化了经典测量理论预测的 Likert/pairwise 灵敏度差距；(2) 发现了 per-axis confound structure（formality 是 style-dominated，register 是 judge-dependent）。将 Thurstone (1927) 以来已知的理论效应包装为\"reveal\"确实夸大了 novelty。论文在 §5.1 引用了 Thurstone 和 Preston & Colman (2000) 并讨论了 measurement attenuation vs. construct divergence，说明作者**意识到**这一理论背景，但 framing 选择（Title/Abstract/Conclusion 中的 \"reveal\"）未能准确反映这一关系。建议作者采纳 R2 的重新定位方案——将 CSD 框架设计和 per-axis confound structure 提升为并列核心贡献，\"Blindspot quantification\" 作为 empirical result 而非 discovery。\n\n---\n\n**[REBUT] R2-N2: Pairwise \"检测\" vs. Pairwise \"放大\"——部分反驳**\n\nR2 提出了一个合理的认识论问题，但我认为其论证力度被高估了，原因如下：\n\n(1) **负对照是反驳\"放大\"解释的最强证据。** Claude Sonnet 4 在相同的 pairwise comparison 设计下 BT ≈ 54-56%（§5.4, Appendix G），TOST 确认等价。如果 pairwise 的灵敏度本身系统性地放大了微小偏好，那么**所有 judge 都应表现出放大效应**，包括 Claude。Claude 的阴性结果证明 pairwise 检测到的是 judge-specific 的偏差，而非 format-induced 的普遍放大。R2 的 critique 未直接回应这一反驳。\n\n(2) **R2 对循环论证的指控部分成立但非致命。** R2 指出\"用 RLHF/DPO pipeline 的 pairwise preference 来论证 pairwise 检测到的是真实偏差\"存在循环性。我同意这在**本体论**层面是循环的（什么是\"真实\"偏差？），但在**操作层面**不循环：如果真实 alignment pipeline（RLHF/DPO）确实使用 pairwise comparison 格式，那么 pairwise 检测到的偏差就是**操作上相关的**偏差，无论它们在哲学层面是否\"真实\"。论文在 §5.4 也明确提到了 Comparative Trap（Jeong et al., 2025），说明作者意识到 pairwise 可能放大偏好。\n\n(3) **但我同意 R2 的一个核心关切：论文的 Conclusion 语言应更谨慎。** \"reveal\" 和 \"systematically misses\" 暗示了单一解释。更诚实的 framing 是：\"pairwise comparison detects style-correlated judge preferences that Likert scoring does not; whether these preferences represent genuine bias or format-amplified micro-preferences remains an open question with practical implications for both interpretations.\"\n\n(4) **关于 R2 的 \"both interpretations\" 批评：** R2 说 \"Both interpretations lead to the same conclusion 不完全成立——如果 pairwise 放大噪声，用 pairwise 审计就会产生 false positives\"。这一点在逻辑上是对的。但论文的论证不需要排除**所有**放大——它需要表明放大的上界是有限的。Cross-rewriter validation（Tables 7-8）中 Style OR 下降 22% 可被视为对 rewriter-specific amplification 的上界估计。\n\n**综合判断：** N2 提出的解释性歧义是真实存在的，但论文已通过负对照、cross-rewriter validation 和 Comparative Trap 讨论提供了充分的缓解。将其定为 critical 偏严——should-fix (warning) 更合适，主要修改是 Conclusion 语言的谨慎化。\n\n---\n\n**[AGREE] R2-W1: Style axis 覆盖面过窄**\n\n同意方向，但不同意严重程度。3 个 axis（2 primary + 1 exploratory）对于一篇**方法论论文**而言是合理的——CSD 框架的价值在于其通用性（可应用于任意 axis），而非穷举所有可能的偏差。论文在 Conclusion（p.8）也明确建议\"additional axes, larger benchmarks, and further judges are needed\"。但 R2 的核心关切——\"per-axis confound structure\" 这一 claim 基于仅 3 个 axis 的泛化基础不足——是合理的。建议作者将 \"per-axis confound structure\" 降级为 \"preliminary evidence of axis-dependent confound patterns\"，或增加 1-2 个 axis 的数据来加强泛化论证。\n\n---\n\n**[AGREE] R2-W2: NLI gate 高拒绝率的选择偏差分析不足**\n\n同意，且与我的 N1 相关联。44% 的拒绝率意味着分析结果只代表 NLI-filterable 的子集，而非全部文本。Appendix B 的 4 个 covariates（BERT score, text length, length difference, NLI score）检查了表面特征，但未检查更深层的特征——例如 filtered-in pairs 是否系统性偏向论证结构更简单（因此内容更容易保持不变）的文本。如果更复杂的文本在 rewriting 时更容易产生 content 变化从而被 NLI gate 拒绝，则保留的样本可能低估了 style bias 在复杂文本上的表现，或高估了 NLI gate 的有效性。建议补充对 filtered-in vs. filtered-out pairs 的语言复杂度（syntactic complexity, argument depth）对比分析。\n\n---\n\n**[AGREE] R2-W3: 100-point continuous Likert 仅用单一 judge**\n\n同意。Appendix M 的 100-point Likert 实验仅使用 Qwen3-32B，这限制了\"Blindspot 不是刻度粒度的产物\"这一结论的泛化性。如果 GPT-4o 或 Llama-3.3-70B 在 100-point scale 下 ATE 变为显著，则 Blindspot 对某些 judge 可能**确实**是粒度问题而非结构性问题。虽然补充所有 judge 的 100-point 实验可能成本较高，但至少应增加 1 个 judge（例如 GPT-4o，因为它是最常用的 benchmark judge）来增强结论的可信度。\n\n---\n\n**[REBUT] R2-W4: 因果语言与实际方法论的张力——部分反驳**\n\nR2 认为 \"Controlled\" 和 \"interventional\" 语言暗示了过强的因果识别。我认为论文在 §3.5 已经做了充分的对冲：\n\n- \"This DAG is a design rationale, not a claim of perfect identification\"（§3.5, p.4）\n- \"nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework\"（§3.5, p.4）\n- \"Our identification rests on three operational assumptions\"（§3.5, p.4）\n\n这些表述明确将因果 claim 降级为 \"operational assumptions\" 而非 formal identification。Figure 2 的 DAG 标注了 \"Assumed data-generating process (design rationale, not a claim of perfect identification)\"。\n\n但我同意 **Title 和 Abstract** 的语言（\"Controlled Style Decomposition\"）与 §3.5 的谨慎对冲之间存在张力。标题中的 \"Controlled\" 容易让因果推断背景的读者期望 do-calculus 层面的识别。建议：在 Abstract 中增加一句明确说明 \"controlled\" 指的是 \"experimentally controlled rewriting\" 而非 formal causal identification。\n\n**严重程度：** Warning 而非 critical。§3.5 的 disclaimer 足够明确，问题主要在 Title/Abstract 的措辞选择而非方法论本身。\n\n---\n\n### Questions 回应\n\n**[AGREE] R2-Q1: Human preference ground-truth**\n\n同意这是最理想的验证方案。与我的 N1 一致——NLI gate 作为 content preservation 的唯一门控，缺乏任何 human validation。收集 human preference 判断（例如让人类标注者对 NLI-gated pairs 进行 pairwise comparison，看人类是否也检测到 style bias）能同时验证两个假设：(a) NLI gate 确实保持了 content；(b) pairwise 检测到的偏差对人类也可观测。这将大幅增强论文的说服力。\n\n---\n\n**[REBUT] R2-Q2: Primary axes 的先验理由**\n\nR2 质疑 formality 和 verbosity 的选择缺乏先验理由。我认为论文在 §2（Related Work）已提供了充分的文献支撑：\n\n- Verbosity bias 是 LLM judge 文献中最 well-documented 的偏差（Zheng et al., 2023; Park et al., 2024; Dubois et al., 2025 均有报告）\n- Formality 与 RLHF preference 的关联在 Reber et al. (2025) 和 Shi et al. (2025) 中被讨论\n- 这两个 axis 有明确的可操作性（可通过 instruction 控制 rewriting），且与实际 deployment 场景直接相关\n\n选择 well-studied 的 axis 作为 primary 恰恰是正确的方法论策略——先在已知存在偏差的 axis 上验证框架的有效性，再扩展到探索性 axis（register）。这不是 weakness，而是合理的研究设计。\n\n---\n\n**[AGREE] R2-Q3: Style OR 下降 22% 的含义**\n\n同意这一观察的重要性。Tables 7-8 显示 GPT-4o 作为替代 rewriter 时 verbosity 的 Style OR 从~14 降至~10（约 22%），说明效应量确实部分依赖于 rewriter 身份。这意味着：(a) Blindspot 现象本身是 robust 的（跨 rewriter 持续存在），但 (b) 效应量的精确估计受 rewriter 风格影响。论文应更显著地承认这一点——\"Blindspot 的存在性是 robust 的，但其效应量有 ±20-25% 的 rewriter-dependent 变异\"。这与我的 W4 一致。\n\n---\n\n**[REBUT] R2-Q4: 量化 pairwise 放大倍数**\n\nR2 问是否有办法量化 pairwise 的放大倍数。我认为论文已提供了一个间接的上界估计：\n\n- Claude Sonnet 4 的 BT ≈ 54-56% 可被视为 pairwise format 的\"基线放大\"（如果存在的话）。这意味着 pairwise 在无偏差 judge 上的\"放大\"最多产生 ~6pp 的偏离（从 50% 到 56%）。\n- GPT-4o 的 BT 63-66% 与 Claude 的 54-56% 之间的差距（~8-10pp）则反映了 judge-specific bias 的下界。\n\n但我同意精确量化放大倍数需要 human ground-truth——如果人类对同一 pairs 的 pairwise preference 是 BT = X%，而 LLM judge 是 BT = Y%，则 Y/X 就是放大倍数。当前设计无法提供这一数据。这是 future work 而非当前论文的致命缺陷。\n\n---\n\n### 总结\n\nR2 的审稿意见整体质量高，与我的审查存在多处共鸣（novelty framing、NLI gate 验证、因果语言谨慎性）。核心分歧在 N2 的严重程度判定：R2 将 \"检测 vs. 放大\" 定为 critical，而我认为负对照已提供了充分缓解，应降为 warning。两份审稿意见共同指向的最大可 actionable 改进是：**增加 human evaluation 数据**（同时验证 content preservation 和 pairwise bias 的人类可观测性）。\n",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-22T09:24:20.707741+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3812
}
```

</details>

---


### Assistant

_source line 696 · 2026-05-22T09:24:33.204635+00:00_

已提交对 Reviewer 2 全部 Weaknesses (N1, N2, W1-W4) 和 Questions (Q1-Q4) 的逐条回应。核心判断：

- **N1 (novelty framing)**: AGREE — 与我的 N2 一致
- **N2 (检测 vs. 放大)**: REBUT — 负对照已充分缓解，建议降为 warning
- **W1-W3**: AGREE — axis 覆盖、NLI 选择偏差、100-point Likert 单 judge 均为合理关切
- **W4 (因果语言)**: REBUT — §3.5 的 disclaimer 已足够明确，问题仅在 Title/Abstract 措辞
- 两份审稿共同指向的最大改进方向：增加 human evaluation 数据

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 23

## Round 23

54 recorded events


### User

_source line 697 · 2026-05-22T16:34:35.441695+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。

## 投稿信息
- **Venue**: EMNLP 2026 via ARR（May cycle）
- **Deadline**: 2026-05-25
- **格式要求**: Long paper，正文 ≤8 页，无限参考文献，ACL template，double-blind
- **Limitations 章节**: 不计入页数，但不能包含新实验/图表/分析
- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各 section 在 `sections/` 子目录）
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf`

## 你的审查侧重

重点评估以下方面，严格、不留情面：

1. **NLI Quality Gate 设计**：阈值选择依据、false positive/negative rate 报告、gate 引入的 selection bias 是否充分讨论
2. **统计方法**：Bradley-Terry 模型假设（IIA）是否检验、Holm-Bonferroni 校正是否正确、GEE 分解的 confounding 处理、TOST equivalence testing 参数选择
3. **因果声明强度**：论文使用 "controlled"/"interventional" 等术语是否与实际方法论强度匹配，是否有 overclaim
4. **实验设计**：样本量充分性（n=100 LLMBar 基准）、cross-benchmark validation 覆盖面、evaluator-producer confound（同一模型既当 rewriter 又当 judge）
5. **人工评估**：是否有人工标注验证 rewriting 质量和 NLI gate 准确性
6. **可复现性**：实验细节是否足够复现（prompt、模型版本、随机种子等）

输出格式：
- **Summary** (2-3句)
- **Strengths** (逐条)
- **Weaknesses** (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])
- **Questions** (需要作者澄清的)
- **Missing References**
- **Overall Assessment** (评分 + 置信度)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-22T16:34:44.577924+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-22T16:34:45.832914+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1254
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-22T16:34:45.983791+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 701 · 2026-05-22T16:34:46.385370+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-22T16:34:50.157737+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 703 · 2026-05-22T16:34:52.517119+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 704 · 2026-05-22T16:35:00.203090+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Review Criteria

The Overall assessment score is an explicit recommendation for the outcome of this pa
…[truncated 1428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 10045
}
```

</details>

---


### Tool result

_source line 705 · 2026-05-22T16:35:01.508006+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.5}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 558.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p9.png\", \"w
…[truncated 515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8990
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-22T16:35:08.897797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 707 · 2026-05-22T16:35:09.249638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 708 · 2026-05-22T16:35:10.205212+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1307
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-22T16:35:10.206535+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-22T16:35:10.206820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 711 · 2026-05-22T16:35:10.658688+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 712 · 2026-05-22T16:35:11.162322+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 713 · 2026-05-22T16:35:11.162748+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 714 · 2026-05-22T16:35:12.119233+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1460
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-22T16:35:12.120571+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-22T16:35:12.120885+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 717 · 2026-05-22T16:35:12.624748+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 718 · 2026-05-22T16:35:13.029172+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 719 · 2026-05-22T16:35:13.029620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 720 · 2026-05-22T16:35:13.991643+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1366
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-22T16:35:13.992822+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 963
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-22T16:35:13.993278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 723 · 2026-05-22T16:35:14.495392+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 724 · 2026-05-22T16:35:14.948112+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-22T16:35:16.002504+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1507
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-22T16:35:16.002936+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-22T16:35:23.320330+00:00_

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
- **5**: Exceptionally thorough study for its type
- **4**: "This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential."
- **3**: Adequate support with minor gaps
- **2**: Major claims lack sufficient support
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award"
- **4**: "Conference: I think this paper could be accepted"
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL"
- **2**: "Resubmit next cycle"
- **1**: "Do not resubmit"

## 5. **Reproducibility**
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with some difficulty
- **2**: Results difficult to reproduce
- **1**: Results cannot be reproduced

## 6. **Datasets & Software Value**
Scale: 1-5 each
- **5**: "Enabling" resource
- **4**: "Useful" for ongoing work
- *
…[truncated 155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7317
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-22T16:35:32.064877+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "11-17",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "11-17",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-22T16:35:33.417731+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 437.9}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 608.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 610.0}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 211.3}], \"total_pages\": 17, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1352
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-22T16:35:38.647580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 731 · 2026-05-22T16:35:39.602336+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-22T16:35:39.602796+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-22T16:35:40.206135+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-22T16:35:40.206617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 735 · 2026-05-22T16:35:40.658851+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 736 · 2026-05-22T16:35:41.463433+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1256
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-22T16:35:41.466595+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-22T16:35:41.517259+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 739 · 2026-05-22T16:35:42.022491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 740 · 2026-05-22T16:35:42.426966+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 741 · 2026-05-22T16:35:42.427482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 742 · 2026-05-22T16:35:42.981745+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-22T16:35:43.083281+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 744 · 2026-05-22T16:40:18.690617+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — 方法严谨性 + 实验设计审查\n\n**论文**: *The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition*\n**Venue**: EMNLP 2026 via ARR (May cycle)\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 — Borderline Conference\n**一句话总结**: 论文识别了一个重要的评估方法学问题（Likert vs. pairwise 对风格偏差的灵敏度差异），统计框架扎实，但 Bradley-Terry IIA 假设未检验、人工验证规模不足、TOST 等价边界缺乏严格论证，这些方法论缺口削弱了核心声明的可信度。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计框架（BT + GEE + Holm-Bonferroni + TOST + Bootstrap）相当完整，但 IIA 假设仅承认未检验（脚注1, p.5），人工验证仅50对，TOST Δ=15pp 偏宽松 |\n| Excitement | 3.5/5 | Likert Blindspot 现象对 NLG 评估社区有实际意义，但相对 RATE (Reber et al., 2025) 增量有限，且 measurement attenuation vs. construct divergence 的根本模糊性限制了贡献深度 |\n| Reproducibility | 3.5/5 | Appendix P 提供了模型版本、温度参数、统计库信息；代码/数据承诺接收后公开；但 rewriting prompt 原文未在论文中展示 |\n| Confidence | 4/5 | 熟悉 BT 模型、GEE、因果推断和 NLG 评估文献，仔细检查了统计方法 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Bradley-Terry IIA 假设未经验证\n\n- 具体位置：Section 4.1, 脚注1 (p.5); Appendix B\n- 问题：Bradley-Terry 模型的核心假设是 Independence of Irrelevant Alternatives (IIA)。论文在脚注1中承认 \"The BT model assumes IIA\"，但仅此一句，**未做任何经验性检验**（如 Hausman-McFadden test）。论文的实验设计中，同一 base text 经 style transformation 后生成多组配对，这些配对并非独立——同源文本在多个比较中重复出现，IIA 可能被系统性违反。Appendix B 报告的 formality 方向不对称性（formal→casual vs. casual→formal BT 估计显著不同）进一步暗示 IIA 违反的可能性。\n- 为什么影响接收：BT 是论文检测 Blindspot 的核心统计工具。若 IIA 被违反，BT 估计的 bias 和 confidence intervals 均不可靠，整个 pairwise 检测框架的有效性成疑。\n- 建议修改方向：(1) 执行 Hausman-McFadden test 或类似诊断；(2) 作为 robustness check，拟合 Thurstone-Mosteller Model V（不要求 IIA）并报告结论是否一致；(3) 对 direction asymmetry 提供更深入的解释——如果 asymmetry 源于 IIA 违反而非真实效应差异，应如何区分？\n\n**N2** [critical] NLI Quality Gate 的选择偏差未充分量化\n\n- 具体位置：Section 3.2; Appendix E (Table 9); Appendix N (NLI Gate Ablation); Section 5.4\n- 问题：NLI gate 是整个框架的关键组件——通过 DeBERTa-v3-large 以 0.90 阈值过滤内容变化的配对。但论文存在以下缺口：\n  - **FPR/FNR 未系统报告**：Section 5.4 报告了 50 对人工标注（25 对 gate-passed），precision=100%，但 (a) 50 对样本量太小（Wilson CI 下界仅 86.3%）；(b) 未报告 recall——多少内容保持的配对被错误拒绝？这个 false negative rate 直接决定 selection bias 的程度。\n  - **Selection bias 的方向性未分析**：gate 过滤掉了约 12-35% 的配对（Table 1 脚注，因 axis 而异），被过滤配对的风格分布是什么？如果 gate 系统性地排除某种风格变换方向（如 casual→formal 比 formal→casual 更容易触发内容变化），则保留的样本不再代表完整的风格效应。\n  - **Appendix N 的 ablation 不充分**：NLI-fail 样本的分析（Table 15）显示 NLI-fail pairs BT 仍在 75% 左右，但该分析仅涉及 verbosity 和 formality 两个 axis，且 NLI-fail 样本量很小（n 约 12-21），统计效力不足以支持 \"gate removes content-confounded pairs rather than amplifying style signal\" 的结论。\n- 为什么影响接收：如果 NLI gate 引入了系统性的 selection bias（例如只保留了「容易做风格变换」的简单文本），则 Blindspot 可能是数据子集的 artifact 而非 Likert 量表的固有缺陷。\n- 建议修改方向：(1) 扩大人工标注到至少 200 对，覆盖 gate-passed 和 gate-rejected 两侧；(2) 报告 recall/FNR；(3) 分析被过滤配对的特征（文本长度、复杂度、风格变换方向）与保留配对的系统性差异。\n\n**N3** [critical] 样本量充分性与 power 解读存在循环论证风险\n\n- 具体位置：Section 5.1; Appendix L (Table 12); Appendix K\n- 问题：论文的核心发现是 \"Likert 在 n≈88-355 时检测不到风格偏差，但 pairwise 可以\"。Appendix L 的 formal power analysis 显示，Likert ATE 达到 80% power 需要 n=336 到 1200+ 不等的样本量——远超当前实验规模。这产生了一个根本性的解读困境：\n  - **论文的解读**（§5.1）：这证明 Likert 量表存在 measurement attenuation，是方法论缺陷\n  - **替代解读**：Likert 效应量本身较小（d ≈ 0.03-0.10），在当前样本量下 Likert 的 null 结果仅仅反映 insufficient power，不能得出 \"Blindspot\" 的结论。Pairwise 方法之所以检测到，是因为 forced-choice 范式天然放大了微小偏好差异\n  - 论文在 §5.1 确实讨论了 \"measurement attenuation vs. construct divergence\" 二元性，但结论部分（§6）的表述 \"Likert scoring systematically misses style biases\" 偏向了前者，未保留足够的 hedging\n- 为什么影响接收：如果 Blindspot 本质上是 power 问题而非方法论缺陷，则论文的核心贡献——CSD 框架作为 \"检测隐藏偏差\" 工具的必要性——被显著削弱。Reviewer 和 AC 会认为这是 overclaim。\n- 建议修改方向：(1) 在更大样本量（≥500）上验证 Likert ATE 是否仍然 non-significant，或至少在 Conclusion 中明确声明当前结果不能排除 power 不足的解释；(2) 将 TOST 等价检验作为更有力的证据——但前提是 Δ 的选择需要更严格的论证（见 W1）；(3) 考虑在 AlpacaEval（样本量更大）上做 Likert sub-study。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] TOST 等价边界 Δ = 15pp 缺乏严格论证\n\n- 具体位置：Section 5.1 (p.6, bottom); Appendix G\n- 问题：TOST equivalence testing 的结论完全依赖于等价边界 Δ 的选择。论文选择 Δ = 15pp（win probability 百分点），理由是 \"the largest effect magnitude across the CSD style axes\"——这是循环论证，用自己观测到的效应量来定义 \"什么算无差异\"。15pp 对应约 d ≈ 0.43（Cohen's d），属于 medium effect size，这个等价边界相当宽松。如果采用 Δ = 5pp 或 10pp，TOST 的等价结论可能不成立。\n- 建议：(1) 基于领域先验知识或实际决策后果论证 Δ 的选择（如 \"低于多少 pp 的偏差不会影响 leaderboard 排名\"）；(2) 报告 TOST 在不同 Δ 值（5pp, 10pp, 15pp, 20pp）下的结论 sensitivity。\n\n**W2** [warning] Evaluator-producer confound 的控制实验范围有限\n\n- 具体位置：Section 5.3; Appendix D (Tables 6-7)\n- 问题：所有 style-controlled rewriting 均使用 Qwen3-32B（Appendix P），而 Qwen3-32B 同时是四个 target judge 之一。Table 7 的 independence test 仅在 verbosity axis 上用 GPT-4o 作为替代 rewriter，且仅针对 Qwen3-32B judge。存在以下缺口：(1) 未在 formality axis 上做替代 rewriter 测试；(2) 未检验其他 judge（GPT-4o, Llama-70B, Gemini）是否也受 Qwen3-32B rewriting style 的系统性影响（即 rewriter 的 \"文风指纹\" 是否被所有 judge 以相同方式感知）；(3) 仅一个替代 rewriter 不足以排除 rewriter-specific artifact。\n- 建议：至少在两个 axis × 两个 judge 组合上做替代 rewriter 实验，或论证为何单个控制实验足够。\n\n**W3** [warning] 因果术语与方法论强度不完全匹配\n\n- 具体位置：Title; Section 3.1; Section 5 (p.5); Figure 2\n- 问题：论文标题使用 \"Controlled Style Decomposition\"，Section 3 使用 \"interventional\"，Figure 2 画出 DAG 并标注 \"blocked by NLI\"。虽然 Section 5 (p.5) 有明确 disclaimer（\"we do not claim that this DAG is a complete structural causal model\"），但整体叙事给读者的印象是这是一个因果推断研究。实际上：(1) rewriting 不是真正的随机干预——LLM rewriter 的行为不受研究者精确控制；(2) NLI gate 不能保证 do-calculus 意义上的 \"blocking\"——它是一个统计过滤器，有 false positive/negative；(3) GEE decomposition 是关联性分析而非因果识别。\n- 建议：(1) 在 Introduction 或 Method 中更早地设定预期，明确 \"controlled\" 指实验条件控制而非 formal causal identification；(2) 避免在 Figure 2 中使用 do-calculus 风格的 DAG notation（如 blocked path），或明确标注为 \"assumed data-generating process\" 而非因果图。\n\n**W4** [warning] 负控制模型仅一个（Claude Sonnet 4），且验证深度有限\n\n- 具体位置：Section 4.1; Appendix G\n- 问题：Claude Sonnet 4 作为唯一的负控制，其 BT 结果（56.2%/54.19%, n.s.）确实支持 \"无 Blindspot\" 的结论。但 (1) 仅一个负控制不足以论证 Blindspot 是特定架构/训练方式的产物而非普遍现象；(2) 未讨论 Claude Sonnet 4 为何不受影响的机制假设——是架构差异、RLHF 策略、还是偶然？\n- 建议：增加至少一个其他可能的负控制（如不同版本的 GPT 或开源 judge），或在 Discussion 中提出可检验的机制假设。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 1 脚注标注 \"Scaled replication (n = 355, other settings same)\" 但 main text 对 n=355 replication 的讨论分散在多处（§5.1, Appendix J, K），不易追踪。建议在 Section 4 统一说明两个实验规模。\n- **M2**: Figure 1 的 pipeline overview 可读性可改进——stage 之间的 sample attrition（n=100 → n=88 → ...）如果能标注具体数字会更清晰。\n- **M3**: Appendix Q (Holm-Bonferroni sensitivity analysis) 报告 \"All results remain significant under the expanded family\"——但 8-test family 仅包含 4 judges × 2 axes，未包含不同 benchmark 的 comparisons。如果将 cross-benchmark tests 也纳入 family，校正后是否仍 significant？\n- **M4**: Register axis 仅出现在 Table 1 和少量讨论中，结果均 non-significant。建议明确说明 register axis 的 n 值和 power，避免读者误解为 \"register 无偏差\" 而非 \"power 不足\"。\n\n---\n\n## Questions（需要作者澄清）\n\n1. **IIA 诊断**：是否尝试过 Thurstone Model V 或其他不要求 IIA 的配对比较模型？如果 BT 在 IIA 违反下仍给出一致结论，这将大大增强论文可信度。\n2. **NLI gate recall**：在 50 对人工标注中，有多少 gate-rejected 的配对实际上内容是保持的（即 false negatives）？这个数据是否已收集但未报告？\n3. **Likert prompt 变体**：当前 Likert 评估使用固定的 1-10 量表。是否尝试过其他量表设计（如 5 点量表、descriptive anchors、rubric-based scoring）？如果不同 Likert 变体均显示 Blindspot，结论更有力。\n4. **AlpacaEval/MT-Bench 的完整结果**：Table 1 仅报告 LLMBar 的详细 BT 和 Likert d 值。AlpacaEval 和 MT-Bench 的 per-judge per-axis 结果在哪个 Appendix？是否所有 judge 在这些 benchmark 上也一致复现 Blindspot？\n5. **Bootstrap attenuation 估计的 convergence**：Appendix J 报告 attenuation δ̄ ≈ -0.017 across sample sizes (n ∈ [0.3n to 1.0n])。但 bootstrap 置信区间从 ±0.3 到 ±0.1——这个范围是否足以排除 δ̄ = 0（即无 attenuation）？\n\n---\n\n## Missing References\n\n1. **Thurstone (1927)** 已引用，但未讨论 Thurstone Model V 作为 BT 的替代方案——在 IIA 可能违反的情况下，至少应引用并讨论。\n2. **Agresti (2002) 或类似 GEE 方法论参考**：GEE decomposition 的统计细节可引用 Liang & Zeger (1986) 之外的教材级参考，帮助不熟悉 GEE 的读者。（Liang & Zeger 已引用，这一条为可选。）\n3. **Bojar et al. (2016) 或 WMT human evaluation**: 作为大规模 pairwise vs. Likert 方法比较的先例，与本文主题高度相关但未引用。\n4. **Karpinska et al. (2021)** 或其他关于 LLM 评估中 scale design 影响的工作，可补充 §2.1 \"Measurement Sensitivity in NLG Evaluation\" 的讨论。\n\n---\n\n## 主要优势\n\n1. **问题重要且及时**：Likert vs. pairwise 的灵敏度差异对整个 NLG 评估社区有直接影响——如果 Likert 确实系统性地低估风格偏差，现有大量评估研究需要重新审视。\n2. **统计框架完整性**：BT + GEE + Holm-Bonferroni + TOST + Bootstrap + sensitivity analysis 的组合在 NLP 评估论文中罕见，显示了认真的统计思考。\n3. **控制实验设计**：NLI quality gate + direction-aware gating + 负控制（Claude Sonnet 4）+ evaluator-producer independence test（Table 7）构成了多层控制，即使每层单独看有缺口，整体设计仍优于大部分同类工作。\n4. **GEE confound decomposition 是真正的贡献**：将 verbosity 识别为 style-dominated、formality 为 conditionally style-driven，比简单的 \"有偏差/无偏差\" 二分法信息量更大。\n5. **Appendix 的深度令人印象深刻**：17 个附录（A-R）覆盖了几乎所有可预见的 robustness concern，说明作者在统计设计上投入了大量思考。\n6. **100-point continuous scale robustness check**（Appendix M）有效反驳了 \"Blindspot 仅因离散量表粒度不足\" 的替代解释。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — 方法严谨性 + 实验设计审查\n\n**论文**: *The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition*\n**Venue**: EMNLP 2026 via ARR (May cycle)\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 — Borderline Conference\n**一句话总结**: 论文识别了一个重要的评估方法学问题（Likert vs. pairwise 对风格偏差的灵敏度差异），统计框架扎实，但 Bradley-Terry IIA 假设未检验、人工验证规模不足、TOST 等价边界缺乏严格论证，这些方法论缺口削弱了核心声明的可信度。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计框架（BT + GEE + Holm-Bonferroni + TOST + Bootstrap）相当完整，但 IIA 假设仅承认未检验（脚注1, p.5），人工验证仅50对，TOST Δ=15pp 偏宽松 |\n| Excitement | 3.5/5 | Likert Blindspot 现象对 NLG 评估社区有实际意义，但相对 RATE (Reber et al., 2025) 增量有限，且 measurement attenuation vs. construct divergence 的根本模糊性限制了贡献深度 |\n| Reproducibility | 3.5/5 | Appendix P 提供了模型版本、温度参数、统计库信息；代码/数据承诺接收后公开；但 rewriting prompt 原文未在论文中展示 |\n| Confidence | 4/5 | 熟悉 BT 模型、GEE、因果推断和 NLG 评估文献，仔细检查了统计方法 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Bradley-Terry IIA 假设未经验证\n\n- 具体位置：Section 4.1, 脚注1 (p.5); Appendix B\n- 问题：Bradley-Terry 模型的核心假设是 Independence of Irrelevant Alternatives (IIA)。论文在脚注1中承认 \"The BT model assumes IIA\"，但仅此一句，**未做任何经验性检验**（如 Hausman-McFadden test）。论文的实验设计中，同一 base text 经 style transformation 后生成多组配对，这些配对并非独立——同源文本在多个比较中重复出现，IIA 可能被系统性违反。Appendix B 报告的 formality 方向不对称性（formal→casual vs. casual→formal BT 估计显著不同）进一步暗示 IIA 违反的可能性。\n- 为什么影响接收：BT 是论文检测 Blindspot 的核心统计工具。若 IIA 被违反，BT 估计的 bias 和 confidence intervals 均不可靠，整个 pairwise 检测框架的有效性成疑。\n- 建议修改方向：(1) 执行 Hausman-McFadden test 或类似诊断；(2) 作为 robustness check，拟合 Thurstone-Mosteller Model V（不要求 IIA）并报告结论是否一致；(3) 对 direction asymmetry 提供更深入的解释——如果 asymmetry 源于 IIA 违反而非真实效应差异，应如何区分？\n\n**N2** [critical] NLI Quality Gate 的选择偏差未充分量化\n\n- 具体位置：Section 3.2; Appendix E (Table 9); Appendix N (NLI Gate Ablation); Section 5.4\n- 问题：NLI gate 是整个框架的关键组件——通过 DeBERTa-v3-large 以 0.90 阈值过滤内容变化的配对。但论文存在以下缺口：\n  - **FPR/FNR 未系统报告**：Section 5.4 报告了 50 对人工标注（25 对 gate-passed），precision=100%，但 (a) 50 对样本量太小（Wilson CI 下界仅 86.3%）；(b) 未报告 recall——多少内容保持的配对被错误拒绝？这个 false negative rate 直接决定 selection bias 的程度。\n  - **Selection bias 的方向性未分析**：gate 过滤掉了约 12-35% 的配对（Table 1 脚注，因 axis 而异），被过滤配对的风格分布是什么？如果 gate 系统性地排除某种风格变换方向（如 casual→formal 比 formal→casual 更容易触发内容变化），则保留的样本不再代表完整的风格效应。\n  - **Appendix N 的 ablation 不充分**：NLI-fail 样本的分析（Table 15）显示 NLI-fail pairs BT 仍在 75% 左右，但该分析仅涉及 verbosity 和 formality 两个 axis，且 NLI-fail 样本量很小（n 约 12-21），统计效力不足以支持 \"gate removes content-confounded pairs rather than amplifying style signal\" 的结论。\n- 为什么影响接收：如果 NLI gate 引入了系统性的 selection bias（例如只保留了「容易做风格变换」的简单文本），则 Blindspot 可能是数据子集的 artifact 而非 Likert 量表的固有缺陷。\n- 建议修改方向：(1) 扩大人工标注到至少 200 对，覆盖 gate-passed 和 gate-rejected 两侧；(2) 报告 recall/FNR；(3) 分析被过滤配对的特征（文本长度、复杂度、风格变换方向）与保留配对的系统性差异。\n\n**N3** [critical] 样本量充分性与 power 解读存在循环论证风险\n\n- 具体位置：Section 5.1; Appendix L (Table 12); Appendix K\n- 问题：论文的核心发现是 \"Likert 在 n≈88-355 时检测不到风格偏差，但 pairwise 可以\"。Appendix L 的 formal power analysis 显示，Likert ATE 达到 80% power 需要 n=336 到 1200+ 不等的样本量——远超当前实验规模。这产生了一个根本性的解读困境：\n  - **论文的解读**（§5.1）：这证明 Likert 量表存在 measurement attenuation，是方法论缺陷\n  - **替代解读**：Likert 效应量本身较小（d ≈ 0.03-0.10），在当前样本量下 Likert 的 null 结果仅仅反映 insufficient power，不能得出 \"Blindspot\" 的结论。Pairwise 方法之所以检测到，是因为 forced-choice 范式天然放大了微小偏好差异\n  - 论文在 §5.1 确实讨论了 \"measurement attenuation vs. construct divergence\" 二元性，但结论部分（§6）的表述 \"Likert scoring systematically misses style biases\" 偏向了前者，未保留足够的 hedging\n- 为什么影响接收：如果 Blindspot 本质上是 power 问题而非方法论缺陷，则论文的核心贡献——CSD 框架作为 \"检测隐藏偏差\" 工具的必要性——被显著削弱。Reviewer 和 AC 会认为这是 overclaim。\n- 建议修改方向：(1) 在更大样本量（≥500）上验证 Likert ATE 是否仍然 non-significant，或至少在 Conclusion 中明确声明当前结果不能排除 power 不足的解释；(2) 将 TOST 等价检验作为更有力的证据——但前提是 Δ 的选择需要更严格的论证（见 W1）；(3) 考虑在 AlpacaEval（样本量更大）上做 Likert sub-study。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] TOST 等价边界 Δ = 15pp 缺乏严格论证\n\n- 具体位置：Section 5.1 (p.6, bottom); Appendix G\n- 问题：TOST equivalence testing 的结论完全依赖于等价边界 Δ 的选择。论文选择 Δ = 15pp（win probability 百分点），理由是 \"the largest effect magnitude across the CSD style axes\"——这是循环论证，用自己观测到的效应量来定义 \"什么算无差异\"。15pp 对应约 d ≈ 0.43（Cohen's d），属于 medium effect size，这个等价边界相当宽松。如果采用 Δ = 5pp 或 10pp，TOST 的等价结论可能不成立。\n- 建议：(1) 基于领域先验知识或实际决策后果论证 Δ 的选择（如 \"低于多少 pp 的偏差不会影响 leaderboard 排名\"）；(2) 报告 TOST 在不同 Δ 值（5pp, 10pp, 15pp, 20pp）下的结论 sensitivity。\n\n**W2** [warning] Evaluator-producer confound 的控制实验范围有限\n\n- 具体位置：Section 5.3; Appendix D (Tables 6-7)\n- 问题：所有 style-controlled rewriting 均使用 Qwen3-32B（Appendix P），而 Qwen3-32B 同时是四个 target judge 之一。Table 7 的 independence test 仅在 verbosity axis 上用 GPT-4o 作为替代 rewriter，且仅针对 Qwen3-32B judge。存在以下缺口：(1) 未在 formality axis 上做替代 rewriter 测试；(2) 未检验其他 judge（GPT-4o, Llama-70B, Gemini）是否也受 Qwen3-32B rewriting style 的系统性影响（即 rewriter 的 \"文风指纹\" 是否被所有 judge 以相同方式感知）；(3) 仅一个替代 rewriter 不足以排除 rewriter-specific artifact。\n- 建议：至少在两个 axis × 两个 judge 组合上做替代 rewriter 实验，或论证为何单个控制实验足够。\n\n**W3** [warning] 因果术语与方法论强度不完全匹配\n\n- 具体位置：Title; Section 3.1; Section 5 (p.5); Figure 2\n- 问题：论文标题使用 \"Controlled Style Decomposition\"，Section 3 使用 \"interventional\"，Figure 2 画出 DAG 并标注 \"blocked by NLI\"。虽然 Section 5 (p.5) 有明确 disclaimer（\"we do not claim that this DAG is a complete structural causal model\"），但整体叙事给读者的印象是这是一个因果推断研究。实际上：(1) rewriting 不是真正的随机干预——LLM rewriter 的行为不受研究者精确控制；(2) NLI gate 不能保证 do-calculus 意义上的 \"blocking\"——它是一个统计过滤器，有 false positive/negative；(3) GEE decomposition 是关联性分析而非因果识别。\n- 建议：(1) 在 Introduction 或 Method 中更早地设定预期，明确 \"controlled\" 指实验条件控制而非 formal causal identification；(2) 避免在 Figure 2 中使用 do-calculus 风格的 DAG notation（如 blocked path），或明确标注为 \"assumed data-generating process\" 而非因果图。\n\n**W4** [warning] 负控制模型仅一个（Claude Sonnet 4），且验证深度有限\n\n- 具体位置：Section 4.1; Appendix G\n- 问题：Claude Sonnet 4 作为唯一的负控制，其 BT 结果（56.2%/54.19%, n.s.）确实支持 \"无 Blindspot\" 的结论。但 (1) 仅一个负控制不足以论证 Blindspot 是特定架构/训练方式的产物而非普遍现象；(2) 未讨论 Claude Sonnet 4 为何不受影响的机制假设——是架构差异、RLHF 策略、还是偶然？\n- 建议：增加至少一个其他可能的负控制（如不同版本的 GPT 或开源 judge），或在 Discussion 中提出可检验的机制假设。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 1 脚注标注 \"Scaled replication (n = 355, other settings same)\" 但 main text 对 n=355 replication 的讨论分散在多处（§5.1, Appendix J, K），不易追踪。建议在 Section 4 统一说明两个实验规模。\n- **M2**: Figure 1 的 pipeline overview 可读性可改进——stage 之间的 sample attrition（n=100 → n=88 → ...）如果能标注具体数字会更清晰。\n- **M3**: Appendix Q (Holm-Bonferroni sensitivity analysis) 报告 \"All results remain significant under the expanded family\"——但 8-test family 仅包含 4 judges × 2 axes，未包含不同 benchmark 的 comparisons。如果将 cross-benchmark tests 也纳入 family，校正后是否仍 significant？\n- **M4**: Register axis 仅出现在 Table 1 和少量讨论中，结果均 non-significant。建议明确说明 register axis 的 n 值和 power，避免读者误解为 \"register 无偏差\" 而非 \"power 不足\"。\n\n---\n\n## Questions（需要作者澄清）\n\n1. **IIA 诊断**：是否尝试过 Thurstone Model V 或其他不要求 IIA 的配对比较模型？如果 BT 在 IIA 违反下仍给出一致结论，这将大大增强论文可信度。\n2. **NLI gate recall**：在 50 对人工标注中，有多少 gate-rejected 的配对实际上内容是保持的（即 false negatives）？这个数据是否已收集但未报告？\n3. **Likert prompt 变体**：当前 Likert 评估使用固定的 1-10 量表。是否尝试过其他量表设计（如 5 点量表、descriptive anchors、rubric-based scoring）？如果不同 Likert 变体均显示 Blindspot，结论更有力。\n4. **AlpacaEval/MT-Bench 的完整结果**：Table 1 仅报告 LLMBar 的详细 BT 和 Likert d 值。AlpacaEval 和 MT-Bench 的 per-judge per-axis 结果在哪个 Appendix？是否所有 judge 在这些 benchmark 上也一致复现 Blindspot？\n5. **Bootstrap attenuation 估计的 convergence**：Appendix J 报告 attenuation δ̄ ≈ -0.017 across sample sizes (n ∈ [0.3n to 1.0n])。但 bootstrap 置信区间从 ±0.3 到 ±0.1——这个范围是否足以排除 δ̄ = 0（即无 attenuation）？\n\n---\n\n## Missing References\n\n1. **Thurstone (1927)** 已引用，但未讨论 Thurstone Model V 作为 BT 的替代方案——在 IIA 可能违反的情况下，至少应引用并讨论。\n2. **Agresti (2002) 或类似 GEE 方法论参考**：GEE decomposition 的统计细节可引用 Liang & Zeger (1986) 之外的教材级参考，帮助不熟悉 GEE 的读者。（Liang & Zeger 已引用，这一条为可选。）\n3. **Bojar et al. (2016) 或 WMT human evaluation**: 作为大规模 pairwise vs. Likert 方法比较的先例，与本文主题高度相关但未引用。\n4. **Karpinska et al. (2021)** 或其他关于 LLM 评估中 scale design 影响的工作，可补充 §2.1 \"Measurement Sensitivity in NLG Evaluation\" 的讨论。\n\n---\n\n## 主要优势\n\n1. **问题重要且及时**：Likert vs. pairwise 的灵敏度差异对整个 NLG 评估社区有直接影响——如果 Likert 确实系统性地低估风格偏差，现有大量评估研究需要重新审视。\n2. **统计框架完整性**：BT + GEE + Holm-Bonferroni + TOST + Bootstrap + sensitivity analysis 的组合在 NLP 评估论文中罕见，显示了认真的统计思考。\n3. **控制实验设计**：NLI quality gate + direction-aware gating + 负控制（Claude Sonnet 4）+ evaluator-producer independence test（Table 7）构成了多层控制，即使每层单独看有缺口，整体设计仍优于大部分同类工作。\n4. **GEE confound decomposition 是真正的贡献**：将 verbosity 识别为 style-dominated、formality 为 conditionally style-driven，比简单的 \"有偏差/无偏差\" 二分法信息量更大。\n5. **Appendix 的深度令人印象深刻**：17 个附录（A-R）覆盖了几乎所有可预见的 robustness concern，说明作者在统计设计上投入了大量思考。\n6. **100-point continuous scale robustness check**（Appendix M）有效反驳了 \"Blindspot 仅因离散量表粒度不足\" 的替代解释。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-22T16:40:22.307647+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3617
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-22T16:40:28.088924+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 747 · 2026-05-22T16:40:28.139595+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-22T16:40:40.433101+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-22T16:40:40.494051+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 60
}
```

</details>

---


### Assistant

_source line 750 · 2026-05-22T16:40:51.774603+00:00_

Round 1 审稿完成，已提交至 Review Director。

**评分摘要**：Overall 3.5（Borderline Conference），Soundness 3.5，Excitement 3.5，Confidence 4。

**三个 Must-Fix**：
1. Bradley-Terry IIA 假设未做经验性检验（脚注1仅承认，无 Hausman-McFadden test 或替代模型对比）
2. NLI Quality Gate 的 selection bias 未充分量化（50 对人工验证太少，未报告 recall/FNR，被过滤配对特征未分析）
3. 样本量与 power 的循环论证风险（Likert null 结果可能仅反映 power 不足而非方法论缺陷，Conclusion 的 hedging 不够）

**四个 Should-Fix**：TOST Δ=15pp 论证不足、evaluator-producer confound 控制实验范围有限（仅一个 axis × 一个 judge）、因果术语偏强、负控制仅一个模型。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 24

## Round 24

4 recorded events


### User

_source line 751 · 2026-05-22T16:43:13.086690+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。

---

## Reviewer 2 — 新颖性 + 写作完整性 + 格式合规审查

**Overall Assessment**: 3.5 — Borderline Conference

### Must-Fix

**N1** [critical] 新颖性定位过度——核心发现有深厚心理测量学先例
- Pairwise > Likert sensitivity 是 Thurstone (1927) 经典结论。Mohammad (2017)、Novikova et al. (2018) 已在 NLG 评估中实证验证。论文叙事将已知现象包装为新发现——"The Likert Blindspot"、"reveals" 等措辞。
- 建议：定位为"LLM judge 场景下首次系统量化"，"first" 限定为 "first for LLM judges specifically"。

**N2** [critical] Detection vs. Amplification 无法分离
- §5.4 六项控制 bound 了 amplification 但未 eliminate。缺独立 ground-truth bias measure。100-point continuous Likert 排除 scale granularity 但未排除 amplification。
- 建议：设计合成实验或诚实 reframe 为 "divergent signals"。

### Should-Fix

**W1** Abstract 信息密度过高，数字堆砌
**W2** 主实验 n=100（gate 后 ≈88），scope 偏少
**W3** 标题预设 ground truth 在 pairwise 侧，未充分考虑 construct 差异
**W4** Register 轴未做 rewriter independence test

### Minor
- Limitations 的 tone 轴实验应移至 Appendix
- BT IIA 假设讨论不足
- Figure 2 DAG 与正文因果语言不统一
- 格式合规：✓

### Questions
1. 能否设计 ground-truth 已知的合成实验？
2. 100-point continuous Likert 是否说明 absolute vs. relative 是根本区分？
3. Rewriter independence test Style OR 下降 22% 如何解读？
4. 是否考虑 human annotators 做 Likert + pairwise？

### Missing References
未显式列出

### 主要优势
- 控制设计严谨
- GEE per-axis decomposition 有真正洞察
- 诚实讨论 Comparative Trap 和 alternative interpretation
- CSD 作为 black-box framework 有即时可用性

---

请对以上每一条给出你的 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-22T16:45:06.574281+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: 新颖性定位过度**\n\n同意 R2 的核心判断。Pairwise 优于 Likert 在灵敏度上的优势确实是 Thurstone (1927) 以来的经典结论，且 Mohammad (2017)、Novikova et al. (2018) 已在 NLG 评估中做过实证验证。论文 Abstract 中 \"reveals\" 和标题中 \"Detecting Hidden Style Bias\" 的措辞确实给人「发现新现象」的印象，而实际贡献是将已知现象在 LLM judge 场景下做了首次系统性、per-axis 的量化。\n\n补充我的观察：论文的真正新颖贡献是 (1) CSD 框架本身（NLI gate + style-controlled rewriting + position-controlled pairwise），(2) GEE per-axis decomposition 区分 style-dominated vs. conditionally style-driven 轴。这些方法论贡献是 solid 的，但被 \"Blindspot\" 这个过度戏剧化的命名所遮蔽。R2 建议的 reframe——\"first systematic quantification for LLM judges specifically\"——是恰当的。\n\n**[AGREE] R2-N2: Detection vs. Amplification 无法分离**\n\n完全同意，这与我在 N3 中提出的 \"measurement attenuation vs. construct divergence 循环论证\" 本质上是同一个问题的不同表述。\n\n论文的 §5.4 提供了六项控制（human annotation, NLI gate, negative control 等），但正如 R2 所指出的，这些控制 bound 了 amplification 的程度但未 eliminate 它。关键缺口是：缺乏一个 **ground-truth bias 已知** 的验证场景。在没有 ground truth 的情况下，我们无法区分：\n- 解读 A：Likert 量表有 attenuation，pairwise 才是「真实」灵敏度 → Blindspot 存在\n- 解读 B：pairwise 的 forced-choice 范式放大了微小偏好差异，Likert 的 null 结果才是「真实」的 → Blindspot 是 artifact\n\n论文在 §5.1 和 §6 中确实讨论了这个二元性，但结论的 hedging 不充分——§6 开头 \"Likert scoring systematically misses style biases\" 直接预设了解读 A。\n\n补充一个 R2 未提到的角度：Appendix M 的 100-point continuous Likert 实验虽然排除了 scale granularity 解释，但实际上 **支持** R2 的 concern——因为即使在连续量表上 Blindspot 仍存在，这更可能反映 absolute vs. relative measurement 的根本差异（construct divergence），而非 Likert 的技术缺陷（measurement attenuation）。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: Abstract 信息密度过高**\n\n同意。Abstract 中 \"complete at moderate bias (d→0 at n=355), >60% attenuation at stronger effects\" 等表述对首次接触本文的读者过于密集。建议精简数字，突出核心 message。这是写作问题，不影响技术判断。\n\n**[AGREE] R2-W2: 主实验 n=100 scope 偏少**\n\n同意，这与我的 N3 一致。n=100（gate 后 ≈88）在 Appendix L 的 formal power analysis 中已被证明对 Likert ATE 的 power 不足（需 n=336-1200+）。虽然 n=355 的 scaled replication 部分弥补了这一点，但 Likert 在 n=355 时仍 non-significant 的解读仍受 power 限制。\n\n**[AGREE] R2-W3: 标题预设 ground truth 在 pairwise 侧**\n\n同意。\"Detecting Hidden Style Bias\" 隐含假设 pairwise 检测到的就是 \"真实偏差\"，Likert 错过的就是 \"隐藏偏差\"。这与 N2 的 detection vs. amplification 问题直接相关。标题应更中性，如 \"Divergent Style Sensitivity between Likert and Pairwise Evaluation in LLM Judges\" 之类。\n\n补充：我在 W3 中也提出了类似问题——Figure 2 的 DAG notation 和 \"interventional\" 等术语进一步强化了这种预设。\n\n**[AGREE] R2-W4: Register 轴未做 rewriter independence test**\n\n同意。Table 1 中 register 轴的 BT 结果对大部分 judge 为 non-significant（BT 接近 0.5），但论文未讨论这是 \"register 确实无偏差\" 还是 \"register rewriting 质量不佳/power 不足\"。缺乏 rewriter independence test 使得无法排除后者。\n\n补充：我在 M4 中也标记了同一问题——register axis 的 n 值和 power 未明确报告。\n\n---\n\n### Minor\n\n**[REBUT] R2-Minor-1: Limitations 的 tone 轴实验应移至 Appendix**\n\n不同意。重新检查论文 p.8-9 的 Limitations section，tone axis 的讨论仅有一句话提及 pass rate (~5.07%) 来解释为何该轴被排除——这是对设计决策的说明，不构成 \"新实验/图表/分析\"。EMNLP 2026 规则允许 Limitations section 包含合理的定性讨论，只要不含 \"excessive additional content\"。一个 pass rate 数字不构成 excessive content。\n\n**[AGREE] R2-Minor-2: BT IIA 假设讨论不足**\n\n强烈同意，且我将此问题升级为 **Must-Fix**（我的 N1）。论文仅在脚注1中一句话承认 IIA，未做任何经验性检验。考虑到同源文本在多个比较中重复出现，IIA 违反风险实质性存在。Appendix B 的方向不对称性进一步暗示此问题。仅标为 Minor 低估了其严重性。\n\n**[AGREE] R2-Minor-3: Figure 2 DAG 与因果语言不统一**\n\n同意，与我的 W3 一致。Figure 2 使用因果图 notation（blocked path, do-intervention 风格），但 §5 的 disclaimer 承认这不是 formal causal model。二者之间存在张力。\n\n**[AGREE] R2-Minor-4: 格式合规 ✓**\n\n确认。主文 8 页，参考文献无限，Limitations 不计入页数。ACL template, double-blind 格式均合规。\n\n---\n\n### Questions\n\n**[AGREE] R2-Q1: 合成实验（ground-truth 已知）**\n\n强烈支持。这是解决 N2 (detection vs. amplification) 的最直接路径。例如：构造一组文本，其中人工注入已知程度的 style bias（如 formality 偏移），然后比较 Likert 和 pairwise 的检测灵敏度。如果 pairwise 在 ground-truth 为 0 的场景下仍 \"检测到\" bias，则说明 amplification 存在。\n\n**[AGREE] R2-Q2: 100-point continuous Likert 与 absolute vs. relative 区分**\n\n同意这是一个关键问题。如上述 N2 回应中所述，Appendix M 的结果实际上支持 construct divergence 解读——问题不在量表粒度，而在 absolute vs. relative 范式的根本差异。作者应在 rebuttal 中明确表态。\n\n**[AGREE] R2-Q3: Rewriter independence test Style OR 下降 22%**\n\n同意需要澄清。Table 7（Appendix D）显示 GPT-4o 作为替代 rewriter 时 Style OR 下降约 22%，这可能意味着 (a) Qwen3-32B 的 rewriting style 本身携带了一部分被检测到的 \"bias\"（即 rewriter artifact），或 (b) GPT-4o 的 rewriting 质量不同导致 style transformation 强度不同。22% 的幅度不可忽略。我在 W2 中也要求扩大替代 rewriter 实验的覆盖面。\n\n**[AGREE] R2-Q4: Human annotators 做 Likert + pairwise**\n\n同意这将是最有力的验证。如果人类评估者在相同材料上也显示 Likert-pairwise divergence，则 Blindspot 是范式级现象而非 LLM 特有。反之，如果人类 Likert 能检测到 bias 而 LLM Likert 不能，则问题在 LLM judge 而非量表本身。\n\n---\n\n### Missing References\n\nR2 未显式列出缺失引用。补充我在 Round 1 中标记的：\n- **Bojar et al. (2016)** 或 WMT human evaluation 工作——大规模 pairwise vs. rating 比较的重要先例\n- **Karpinska et al. (2021)** 或类似 scale design 影响的研究\n\n---\n\n### 对 R2 优势识别的补充\n\n同意 R2 对论文优势的识别，特别是 GEE per-axis decomposition 和 Comparative Trap 的诚实讨论。补充一点 R2 未提到的优势：**Appendix 的深度和覆盖面**（17 个附录 A-R）在 NLP 评估论文中罕见，展示了作者在 robustness concern 上的系统性思考。\n\n---\n\n### 总结\n\nR2 的两个 Must-Fix（N1 新颖性过度、N2 detection vs. amplification）与我的核心关切高度一致。我与 R2 的唯一分歧是 BT IIA 的严重性定级——R2 列为 Minor，我认为应为 Must-Fix。两位 Reviewer 在以下三点形成共识：\n1. 论文无法区分 detection 与 amplification（R2-N2 ≈ R1-N3）\n2. 标题/措辞预设了 pairwise 为 ground truth（R2-W3 ≈ R1-W3）\n3. 样本量不足限制了 Likert null 结果的解读（R2-W2 ≈ R1-N3）",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: 新颖性定位过度**\n\n同意 R2 的核心判断。Pairwise 优于 Likert 在灵敏度上的优势确实是 Thurstone (1927) 以来的经典结论，且 Mohammad (2017)、Novikova et al. (2018) 已在 NLG 评估中做过实证验证。论文 Abstract 中 \"reveals\" 和标题中 \"Detecting Hidden Style Bias\" 的措辞确实给人「发现新现象」的印象，而实际贡献是将已知现象在 LLM judge 场景下做了首次系统性、per-axis 的量化。\n\n补充我的观察：论文的真正新颖贡献是 (1) CSD 框架本身（NLI gate + style-controlled rewriting + position-controlled pairwise），(2) GEE per-axis decomposition 区分 style-dominated vs. conditionally style-driven 轴。这些方法论贡献是 solid 的，但被 \"Blindspot\" 这个过度戏剧化的命名所遮蔽。R2 建议的 reframe——\"first systematic quantification for LLM judges specifically\"——是恰当的。\n\n**[AGREE] R2-N2: Detection vs. Amplification 无法分离**\n\n完全同意，这与我在 N3 中提出的 \"measurement attenuation vs. construct divergence 循环论证\" 本质上是同一个问题的不同表述。\n\n论文的 §5.4 提供了六项控制（human annotation, NLI gate, negative control 等），但正如 R2 所指出的，这些控制 bound 了 amplification 的程度但未 eliminate 它。关键缺口是：缺乏一个 **ground-truth bias 已知** 的验证场景。在没有 ground truth 的情况下，我们无法区分：\n- 解读 A：Likert 量表有 attenuation，pairwise 才是「真实」灵敏度 → Blindspot 存在\n- 解读 B：pairwise 的 forced-choice 范式放大了微小偏好差异，Likert 的 null 结果才是「真实」的 → Blindspot 是 artifact\n\n论文在 §5.1 和 §6 中确实讨论了这个二元性，但结论的 hedging 不充分——§6 开头 \"Likert scoring systematically misses style biases\" 直接预设了解读 A。\n\n补充一个 R2 未提到的角度：Appendix M 的 100-point continuous Likert 实验虽然排除了 scale granularity 解释，但实际上 **支持** R2 的 concern——因为即使在连续量表上 Blindspot 仍存在，这更可能反映 absolute vs. relative measurement 的根本差异（construct divergence），而非 Likert 的技术缺陷（measurement attenuation）。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: Abstract 信息密度过高**\n\n同意。Abstract 中 \"complete at moderate bias (d→0 at n=355), >60% attenuation at stronger effects\" 等表述对首次接触本文的读者过于密集。建议精简数字，突出核心 message。这是写作问题，不影响技术判断。\n\n**[AGREE] R2-W2: 主实验 n=100 scope 偏少**\n\n同意，这与我的 N3 一致。n=100（gate 后 ≈88）在 Appendix L 的 formal power analysis 中已被证明对 Likert ATE 的 power 不足（需 n=336-1200+）。虽然 n=355 的 scaled replication 部分弥补了这一点，但 Likert 在 n=355 时仍 non-significant 的解读仍受 power 限制。\n\n**[AGREE] R2-W3: 标题预设 ground truth 在 pairwise 侧**\n\n同意。\"Detecting Hidden Style Bias\" 隐含假设 pairwise 检测到的就是 \"真实偏差\"，Likert 错过的就是 \"隐藏偏差\"。这与 N2 的 detection vs. amplification 问题直接相关。标题应更中性，如 \"Divergent Style Sensitivity between Likert and Pairwise Evaluation in LLM Judges\" 之类。\n\n补充：我在 W3 中也提出了类似问题——Figure 2 的 DAG notation 和 \"interventional\" 等术语进一步强化了这种预设。\n\n**[AGREE] R2-W4: Register 轴未做 rewriter independence test**\n\n同意。Table 1 中 register 轴的 BT 结果对大部分 judge 为 non-significant（BT 接近 0.5），但论文未讨论这是 \"register 确实无偏差\" 还是 \"register rewriting 质量不佳/power 不足\"。缺乏 rewriter independence test 使得无法排除后者。\n\n补充：我在 M4 中也标记了同一问题——register axis 的 n 值和 power 未明确报告。\n\n---\n\n### Minor\n\n**[REBUT] R2-Minor-1: Limitations 的 tone 轴实验应移至 Appendix**\n\n不同意。重新检查论文 p.8-9 的 Limitations section，tone axis 的讨论仅有一句话提及 pass rate (~5.07%) 来解释为何该轴被排除——这是对设计决策的说明，不构成 \"新实验/图表/分析\"。EMNLP 2026 规则允许 Limitations section 包含合理的定性讨论，只要不含 \"excessive additional content\"。一个 pass rate 数字不构成 excessive content。\n\n**[AGREE] R2-Minor-2: BT IIA 假设讨论不足**\n\n强烈同意，且我将此问题升级为 **Must-Fix**（我的 N1）。论文仅在脚注1中一句话承认 IIA，未做任何经验性检验。考虑到同源文本在多个比较中重复出现，IIA 违反风险实质性存在。Appendix B 的方向不对称性进一步暗示此问题。仅标为 Minor 低估了其严重性。\n\n**[AGREE] R2-Minor-3: Figure 2 DAG 与因果语言不统一**\n\n同意，与我的 W3 一致。Figure 2 使用因果图 notation（blocked path, do-intervention 风格），但 §5 的 disclaimer 承认这不是 formal causal model。二者之间存在张力。\n\n**[AGREE] R2-Minor-4: 格式合规 ✓**\n\n确认。主文 8 页，参考文献无限，Limitations 不计入页数。ACL template, double-blind 格式均合规。\n\n---\n\n### Questions\n\n**[AGREE] R2-Q1: 合成实验（ground-truth 已知）**\n\n强烈支持。这是解决 N2 (detection vs. amplification) 的最直接路径。例如：构造一组文本，其中人工注入已知程度的 style bias（如 formality 偏移），然后比较 Likert 和 pairwise 的检测灵敏度。如果 pairwise 在 ground-truth 为 0 的场景下仍 \"检测到\" bias，则说明 amplification 存在。\n\n**[AGREE] R2-Q2: 100-point continuous Likert 与 absolute vs. relative 区分**\n\n同意这是一个关键问题。如上述 N2 回应中所述，Appendix M 的结果实际上支持 construct divergence 解读——问题不在量表粒度，而在 absolute vs. relative 范式的根本差异。作者应在 rebuttal 中明确表态。\n\n**[AGREE] R2-Q3: Rewriter independence test Style OR 下降 22%**\n\n同意需要澄清。Table 7（Appendix D）显示 GPT-4o 作为替代 rewriter 时 Style OR 下降约 22%，这可能意味着 (a) Qwen3-32B 的 rewriting style 本身携带了一部分被检测到的 \"bias\"（即 rewriter artifact），或 (b) GPT-4o 的 rewriting 质量不同导致 style transformation 强度不同。22% 的幅度不可忽略。我在 W2 中也要求扩大替代 rewriter 实验的覆盖面。\n\n**[AGREE] R2-Q4: Human annotators 做 Likert + pairwise**\n\n同意这将是最有力的验证。如果人类评估者在相同材料上也显示 Likert-pairwise divergence，则 Blindspot 是范式级现象而非 LLM 特有。反之，如果人类 Likert 能检测到 bias 而 LLM Likert 不能，则问题在 LLM judge 而非量表本身。\n\n---\n\n### Missing References\n\nR2 未显式列出缺失引用。补充我在 Round 1 中标记的：\n- **Bojar et al. (2016)** 或 WMT human evaluation 工作——大规模 pairwise vs. rating 比较的重要先例\n- **Karpinska et al. (2021)** 或类似 scale design 影响的研究\n\n---\n\n### 对 R2 优势识别的补充\n\n同意 R2 对论文优势的识别，特别是 GEE per-axis decomposition 和 Comparative Trap 的诚实讨论。补充一点 R2 未提到的优势：**Appendix 的深度和覆盖面**（17 个附录 A-R）在 NLP 评估论文中罕见，展示了作者在 robustness concern 上的系统性思考。\n\n---\n\n### 总结\n\nR2 的两个 Must-Fix（N1 新颖性过度、N2 detection vs. amplification）与我的核心关切高度一致。我与 R2 的唯一分歧是 BT IIA 的严重性定级——R2 列为 Minor，我认为应为 Must-Fix。两位 Reviewer 在以下三点形成共识：\n1. 论文无法区分 detection 与 amplification（R2-N2 ≈ R1-N3）\n2. 标题/措辞预设了 pairwise 为 ground truth（R2-W3 ≈ R1-W3）\n3. 样本量不足限制了 Likert null 结果的解读（R2-W2 ≈ R1-N3）",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-22T16:45:10.137074+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3562
}
```

</details>

---


### Assistant

_source line 754 · 2026-05-22T16:45:16.154833+00:00_

交叉回应已提交。与 R2 在 7/8 条 Must-Fix 和 Should-Fix 上达成一致，唯一分歧是 BT IIA 问题的严重性——R2 列为 Minor，我认为应升级为 Must-Fix。两位 Reviewer 的共识聚焦于三个核心问题：detection vs. amplification 不可分离、标题预设 pairwise 为 ground truth、样本量限制 Likert null 的解读。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 25

## Round 25

62 recorded events


### User

_source line 755 · 2026-05-22T18:08:16.587173+00:00_

[Round 10 审稿请求]:
你是 Reviewer 1，负责审查本论文的**方法严谨性、实验设计和统计分析**。

## 论文信息
- 标题：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
- 主文件：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf

## Venue 要求
- **EMNLP 2026**（ARR May cycle），截止 2026-05-25
- Long paper：正文 ≤8 页 + 无限参考文献（ACL 模板）
- Limitations + Ethical Considerations 不计入页数限制
- Double-blind 匿名审稿
- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 你的审查侧重

**方法严谨性**（重点）：
1. NLI gate 作为 content preservation 验证的有效性——阈值选择、false positive/negative 率、是否引入 selection bias
2. Style-controlled rewriting 方法：Qwen3-32B 既做 rewriter 又做 judge 的 evaluator-producer overlap 问题
3. Direction-aware NLI 对 verbosity 的特殊处理是否方法论合理
4. DAG/因果框架的声明强度与实际方法论强度是否匹配
5. GEE conditional decomposition 的统计假设（exchangeable correlation、IIA for BT）是否得到检验和满足

**实验设计**：
6. 样本量（n=88 主实验，n=355 scaled replication）是否足以支撑论文的 claims
7. 多重比较校正（Holm-Bonferroni 6 tests）是否合理
8. 负控制（Claude Sonnet 4）的 TOST 等价检验——Δ=15pp 是否合理
9. Cross-benchmark replication（AlpacaEval, MT-Bench）的覆盖面是否充分
10. 人工标注验证规模（50 对）是否足够

**统计分析**：
11. Bradley-Terry 模型的 IIA 假设是否被检验（formality 方向不对称暗示可能违反）
12. Bootstrap CI 方法（10,000 pair-level resamples）是否恰当
13. Power analysis 的呈现方式（post-hoc vs. prospective）
14. Detection vs. amplification 的六项控制是否充分回应 Comparative Trap 的关切

请给出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准）。

对每个 Weakness 标注严重程度：
- **Must-Fix (critical)**：不修复则不可接收
- **Should-Fix (warning)**：显著改善论文质量
- **Minor (info)**：建议改进

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-22T18:08:32.589469+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 757 · 2026-05-22T18:08:32.790443+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-22T18:08:37.388712+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 759 · 2026-05-22T18:08:39.581731+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf",
  "pages": "1-10",
  "project": "causal_style_decomp_judge",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf",
    "pages": "1-10",
    "project": "causal_style_decomp_judge",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 760 · 2026-05-22T18:08:44.815856+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found relevant information about ACL ARR 2026 reviewer guidelines and review form criteria. Here are the key findings:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility, while conference recommendations
…[truncated 1207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7427
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-22T18:08:46.173493+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 578.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.1}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 547.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p9.p
…[truncated 526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6591
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-22T18:08:53.200467+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 763 · 2026-05-22T18:08:53.250991+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-22T18:08:57.166982+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include every field that a reviewer must fill in."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include every field that a reviewer must fill in."
  }
}
```

</details>

---


### Tool call

_source line 765 · 2026-05-22T18:08:57.668906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 766 · 2026-05-22T18:08:58.222184+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-22T18:08:59.131153+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1462
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-22T18:08:59.131631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 769 · 2026-05-22T18:08:59.334719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 770 · 2026-05-22T18:08:59.388244+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1166
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-22T18:09:02.163842+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3032
}
```

</details>

---


### Tool result

_source line 772 · 2026-05-22T18:09:02.166604+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2831
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-22T18:09:07.092348+00:00_

# ACL Rolling Review Form - Complete Structure

## Core Review Sections

**Paper Summary**
Reviewer describes the paper's topic and scope.

**Summary of Strengths**
Reviewer identifies reasons for publication, including "novel and useful methodology, insightful empirical results or theoretical analysis, clear organization."

**Summary of Weaknesses**
Numbered concerns about correctness, impact, clarity, or other factors affecting publication priority.

**Comments/Suggestions/Typos**
Additional improvement suggestions beyond main concerns.

## Scoring Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: Positive evaluation; careful reading and familiarity with related work
- 4: Quite sure with unlikely oversight
- 3: Pretty sure; general area familiarity but incomplete detail checking
- 2: Willing to defend but likely missed details or novelty assessment
- 1: Outside expertise area or paper is very difficult

**Soundness** (1-5 scale with .5 increments)
- 5: "one of the most thorough I have seen"
- 4: Sufficient support; extra experiments not essential
- 3: Adequate support for main claims; minor points need details
- 2: Major claims lack support; significant technical problems
- 1: Insufficient thoroughness or ACL relevance

**Excitement** (1-5 scale with .5 increments)
- 5: Would recommend and attend presentation
- 4: Would mention to others; effort to attend
- 3: Might mention points; attend if time permits
- 2: Doesn't resonate personally but may interest others
- 1: Lacks resonance; no community relevance

**Overall Assessment** (1-5 scale with .5 increments)
- 5: Consider for Award (top 2.5%)
- 4.5: Borderline Award
- 4: Conference acceptance
- 3.5: Borderline Conference
- 3: Findings acceptance
- 2.5: Borderline Findings
- 2: Resubmit next cycle
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

**Best Paper Justification**
Required if rating is "Consider for Award" or "Borderline Award"

## Further Questions Section

**Limitations and Societal Impact**
As
…[truncated 1267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9925
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-22T18:09:20.109669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 775 · 2026-05-22T18:09:20.613317+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 776 · 2026-05-22T18:09:21.519420+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool result

_source line 777 · 2026-05-22T18:09:21.520729+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 778 · 2026-05-22T18:09:21.521163+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 779 · 2026-05-22T18:09:21.822462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 780 · 2026-05-22T18:09:22.275837+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool result

_source line 781 · 2026-05-22T18:09:22.628177+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-22T18:09:34.933478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-22T18:09:36.138645+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1205
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-22T18:09:36.239483+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-22T18:09:37.294010+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-22T18:09:37.394979+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf",
  "pages": "11-17",
  "project": "causal_style_decomp_judge",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf",
    "pages": "11-17",
    "project": "causal_style_decomp_judge",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-22T18:09:38.197566+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.9}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 583.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 595.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 549.5}], \"total_pages\": 17, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 802
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-22T18:09:43.470405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-22T18:09:44.426352+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-22T18:09:44.426767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 791 · 2026-05-22T18:09:45.235490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 792 · 2026-05-22T18:09:45.235939+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 793 · 2026-05-22T18:09:45.388221+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---


### Tool result

_source line 794 · 2026-05-22T18:09:46.395089+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1159
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-22T18:09:46.446117+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1210
}
```

</details>

---


### Tool call

_source line 796 · 2026-05-22T18:09:52.422633+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-22T18:09:53.378212+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-22T18:09:53.428890+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 799 · 2026-05-22T18:09:53.732909+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 800 · 2026-05-22T18:09:54.591388+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1162
}
```

</details>

---


### Tool result

_source line 801 · 2026-05-22T18:09:54.996755+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1263
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-22T18:10:04.496321+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 803 · 2026-05-22T18:10:04.547056+00:00_

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
…[truncated 3715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 804 · 2026-05-22T18:10:09.466828+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 805 · 2026-05-22T18:10:09.467264+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 806 · 2026-05-22T18:10:13.081952+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 807 · 2026-05-22T18:10:13.183872+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-22T18:10:17.550825+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-22T18:10:17.802260+00:00_

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
…[truncated 6101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-22T18:10:17.802738+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-22T18:10:17.853425+00:00_

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
12	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.\footnote{In binary-choice BT models, IIA is structurally satisfied; the direction asymmetry in Appendix~\ref{app:bt_gof} (formality: formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$; verbosity: $p = 0.453$) reflects heterogeneous treatment effects across style directions rather than IIA violation.}
13	All bootstrap confidence intervals use 10{,}000 pair-level resamples with seed 42.
14	GEE models use exchangeable working correlation, justified by near-zero estimated within-pair correlations ($\hat{\alpha} \in [-0.25, +0.11]$; Appendix~\ref{app:gee_diagnostics}).
15	
16	\paragraph{Model selection
…[truncated 16421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-22T18:10:25.085076+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-22T18:10:25.387351+00:00_

1	\appendix
2	
3	\noindent\emph{Organization: confound analysis (A--B), model diagnostics (C), independence tests (D), gate validation (E--F), equivalence testing (G), statistical details (H--K), sensitivity analyses (L--N), artifact controls (O), implementation (P), multiplicity (Q), cross-axis contamination (R), human annotation agreement (S).}
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
16	The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect mag
…[truncated 29298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-22T18:15:08.627590+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告\n\n**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审查侧重**: 方法严谨性、实验设计、统计分析\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法论扎实、现象定义清晰的实证研究，verbosity 轴结果令人信服，但 formality 轴的 quality-style 混淆显著削弱核心 claim，TOST 等价检验边界偏宽，整体贡献介于 Findings 和 Conference 之间。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法设计合理，统计框架严谨，但 formality 轴 GEE 显示 Originality OR ≥ Style OR（多配置），\"style bias\" 的 claim 对该轴偏强；verbosity 轴 (OR 8–13, Orig ns) 方法论上无可挑剔 |\n| Excitement | 3.5/5 | Likert Blindspot 现象有明确的实践意义（RLHF/DPO 依赖 pairwise，但审计依赖 Likert），七种方法的 sensitivity hierarchy 是有价值的方法论贡献，但缺乏下游影响的实证 |\n| Reproducibility | 4/5 | 实现细节完整（模型版本、温度、种子），统计方法描述清晰，代码/数据承诺开源；扣分点：部分 GEE 配置缺少 QIC 绝对值 |\n| Reviewer Confidence | 4/5 | 熟悉 Bradley-Terry 模型、GEE、因果推断框架和 LLM 评估文献 |\n\n---\n\n## 主要优势\n\n1. **现象定义清晰且可复现**：Likert Blindspot 在 4 个 judge × 2 个主轴 × 3 个 benchmark 上一致出现（11 个 bias-positive cell 中 8 个），且用 7 种统计方法验证了 sensitivity hierarchy（Table 2），形成了强有力的证据链。\n\n2. **因果声明诚实克制**：Section 3.5 明确声明\"we do not claim that this DAG is a complete structural causal model\"，Figure 2 DAG 中用虚线橙色箭头标注 residual confounding，避免了过度因果宣称。这在该领域的论文中少见且值得肯定。\n\n3. **统计方法论严谨**：\n   - Holm-Bonferroni 校正 6 测试家族 + 8 测试敏感性分析（Appendix Q），全部保持显著\n   - BT 拟合优度检验（Appendix H：formality deviance p=0.198, verbosity p=0.905）\n   - GEE 诊断完整：exchangeable vs independence 对比（|ΔQIC| < 0.001）、交互项检验（所有 p > 0.13）、95% CI 完整报告\n   - Bootstrap attenuation analysis（Appendix J）区分 measurement attenuation 与 insufficient power，优于简单 post-hoc power\n\n4. **控制变量设计周全**：NLI 阈值 11 点 sweep（BT ≤ 3pp 变动）、cross-rewriter 验证（22% OR 下降但 Blindspot 持续）、same-style double-rewrite artifact control、Claude 负控制——形成多层防线。\n\n5. **Verbosity 轴证据链极强**：Style OR 8.2–13.1（四个 judge 一致），Originality OR 0.38–0.49（均不显著或边缘），direction-aware NLI 有理论和实证依据（Appendix F），cross-rewriter 验证完整（Appendix D Table 7）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Formality 轴 quality-style 混淆严重，核心 claim 对该轴偏强\n\n- 具体位置：Table 3（GEE decomposition）、Section 5.2\n- 问题：GEE 分解显示 formality 的 Originality OR 在多个配置中 ≥ Style OR：\n  - GPT-4o: Style 2.58 vs Orig 2.32（几乎相等）\n  - Qwen3 n=355: Style 2.15 vs Orig 4.99（originality 是 style 的 2.3 倍）\n  - Gemini: Style 1.64 (ns!) vs Orig 2.51\n  - Direction asymmetry（Appendix H: formal-origin 88.9% vs casual-origin 52.6%, Fisher p=0.015）进一步确认混淆存在\n\n  这意味着 pairwise 检测到的 formality \"bias\" 有相当部分是 quality-formality 相关性的反映，而非纯粹的 style bias。论文标题和 abstract 用 \"Detecting Hidden Style Bias\" 统一描述所有轴的发现，但 formality 轴检测到的更多是 quality confound + style effect 的混合信号。\n\n  Appendix H 的 stratified analysis（限制 Likert 等分对，BT=67.3%）作为 robustness check 有说服力，但存在一个 circularity 问题：论文的核心 claim 正是 Likert 对 style bias 不敏感，因此用 \"Likert 等分\" 作为 \"质量无差异\" 的代理变量存在逻辑矛盾。\n\n- 为什么影响接收：如果 formality 的 Blindspot 本质上是 pairwise 对 quality-style correlation 的放大，而非 Likert 遗漏了 style bias，则论文的核心叙事（\"hidden style bias\"）被削弱约一半。\n- 建议修改方向：\n  (a) 在 abstract/introduction 中区分 verbosity（纯 style-driven）和 formality（style + quality confound），不要统一称为 \"style bias\"\n  (b) 考虑将 formality 的发现重新定性为 \"measurement sensitivity divergence\" 而非 \"hidden bias detection\"\n  (c) 补充讨论 stratified analysis 的 circularity 并提出替代验证方案\n\n**N2** [critical] Bootstrap CI 的 pair-level resampling 在 GEE 语境下的合理性未论证\n\n- 具体位置：Section 4.1, \"All bootstrap CIs use 10,000 pair-level resamples\"\n- 问题：论文将 pair-level bootstrap 同时用于 BT 估计和 GEE 分解。对 BT 模型，pair-level resampling 是标准做法。但 GEE 使用 exchangeable working correlation 对 pair 内观测建模，其 CI 来自 sandwich standard errors（Appendix P），而非 bootstrap。这两套 CI 方法在论文中的分工不够清晰——Table 3 的 CI（Appendix C Table 6）使用哪种方法？如果是 sandwich SE，则与 Section 4.1 的 bootstrap 声明不一致；如果是 bootstrap，则需要论证 pair-level resampling 是否保持了 GEE 的 cluster 结构。\n- 为什么影响接收：CI 方法的不清晰可能影响 GEE OR 的统计推断可靠性。\n- 建议修改方向：明确区分 BT bootstrap CI 和 GEE sandwich CI 的适用范围，如果 GEE 也用 bootstrap，需论证 resampling 单位（pair vs cluster）的选择。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] TOST 等价检验边界 Δ=15pp 偏宽，负控制说服力有限\n\n- 具体位置：Section 5.4（Detection vs. amplification, control ii）、Appendix G\n- 问题：Claude Sonnet 4 的 TOST 在 Δ=15pp 时达到 p<0.05（76% power），但这意味着 Claude 可能存在高达 ~15pp 的未检测 style preference。GPT-4o formality 检测到的 bias 为 BT 63.0%（即 13pp 偏离 50%），与 TOST 边界几乎重叠。因此，Claude 负控制无法区分 \"真正无 bias\" 和 \"moderate bias but below detection threshold\"。\n  论文声称 Claude 的 bound 与 GPT-4o (13–23pp) \"substantively distinct\"，但 13pp 和 15pp 的差距仅 2pp，且 CI 大量重叠。\n- 建议：(a) 降低 claim 强度，承认 Δ=15pp 是 power 限制下的妥协而非 substantive bound; (b) 报告 Δ=10pp 时的 TOST power 和 p 值供读者判断; (c) 或增加 Claude 样本量以收紧边界。\n\n**W2** [warning] 人工标注验证规模偏小，inter-annotator agreement 仅 moderate\n\n- 具体位置：Section 5.4（Content preservation）、Appendix S\n- 问题：50 对（25 pass + 25 reject）由 2 名标注员评估，Cohen's κ=0.44（moderate）。A1 认为全部 25 pass 对保内容（precision 100%），A2 认为 21/25（84%）。4 个分歧全在 verbosity condensation 对上——而 verbosity 正是论文最强 claim 的支撑轴。这意味着 verbosity NLI gate 的 content preservation 标准在标注员间有实质性分歧。\n  Wilson CI [86.7%, 100%] 和 [65.3%, 93.6%] 的重叠区间说明精度估计本身不够精确。\n- 建议：(a) 增加标注量（至少 100 对）以收紧 CI; (b) 增加第三名标注员; (c) 讨论 verbosity condensation 的 content preservation 标准模糊性对结论的影响。\n\n**W3** [warning] Cross-benchmark replication 覆盖面有限\n\n- 具体位置：Table 1, Section 5.3\n- 问题：\n  - AlpacaEval 仅测 3 个配置（2 judges × formality + 1 verbosity）\n  - MT-Bench 仅测 2 个配置（2 judges × formality），无 verbosity\n  - Llama-70B 和 Gemini 未做 cross-benchmark 验证\n  - Register 轴无 cross-benchmark 验证\n  论文 claim \"cross-benchmark replication\" 但实际覆盖面较窄，尤其 verbosity（最强轴）仅在 AlpacaEval 有 1 个 cross-benchmark 数据点，且该点是 ‡（both sig，非 Blindspot）。\n- 建议：至少补充 MT-Bench verbosity 的 1-2 个 judge 数据；或降低 cross-benchmark claim 的强度。\n\n**W4** [warning] Cross-axis contamination中 formality→verbosity 的 word count shift (d=−0.23) 非 negligible\n\n- 具体位置：Appendix R, Table 18\n- 问题：formality 改写导致 word count 变化 d=−0.23，按 Cohen 标准属 \"small\" 但非 negligible（论文自设的 negligible 标准是 d<0.20）。论文以 \"directionally symmetric (formal→casual −5.0%, casual→formal +5.6%)\" 辩护，但 dataset-level 对称不等于 pair-level 对称——如果 formal→casual 方向的 pairs 和 casual→formal 方向的 pairs 在 quality 或 judge preference 上有系统差异（direction asymmetry 已经证明确实如此），则 cross-axis 污染可能不会在 aggregate 中抵消。\n- 建议：在 pair level 验证 word count 变化与 BT outcome 的相关性，或在 GEE 中加入 word count 变化作为 covariate。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 1 符号系统偏复杂**：†, ‡, †_e, †_c, --- 共 5 种标记，且 †_e 和 †_c 仅在脚注中解释。建议在正文首次出现时给出完整定义。\n\n2. **Figure 4（power curve）标题**：虽正文已引用 Hoenig & Hesse (2001) 避免 post-hoc power 误用，但 Figure caption 中 \"Detection probability at observed effect magnitudes\" 的表述仍可能被误读为 post-hoc power。建议在 caption 中加注 \"prospective sample-size planning\"。\n\n3. **Section 4.1 脚注 3（IIA）**：关于 binary-choice BT 模型中 IIA structurally satisfied 的声明是正确的，但脚注篇幅较长（~60 words），建议移至 Appendix H 与 GoF 检验合并讨论。\n\n4. **Register 轴定位不够清晰**：在 Table 1 中 register 占 6 行，但正文 Section 5.3 仅用一句话提及 register 是 \"exploratory and judge-dependent\"。建议将 register 结果移至 appendix 或更明确地标注为 exploratory pilot。\n\n5. **Limitations 段落\"Validation methodology and scale design\"**：提到 \"100-point experiment was tested with a single judge\" 但未在 Appendix M 中讨论为何仅选 Qwen3-32B（作为 evaluator-producer overlap 最严重的 judge）而非选无 overlap 的 GPT-4o。\n\n---\n\n## 问题（供作者回应）\n\n**Q1**: Appendix H 的 stratified analysis 用 Likert 等分对作为 \"无质量差异\" 的代理变量来验证 style bias 存在——但论文的核心 claim 是 Likert 对 style 不敏感。如何排除这一 circularity？是否考虑过使用外部质量指标（如人工评分或参考答案匹配度）替代 Likert 作为 quality proxy？\n\n**Q2**: 对于 formality 轴，Qwen3 n=355 的 GEE 分解显示 Originality OR (4.99) 是 Style OR (2.15) 的 2.3 倍。在这种 confound structure 下，\"formality bias\" 的表述是否仍然恰当？是否应改为 \"formality-related preference divergence\"？\n\n**Q3**: TOST Δ=15pp 的选择基准是什么？是否是 smallest effect of interest (SESOI) 的估计，还是纯粹由 power 限制决定？如果是后者，论文是否应报告基于 SESOI 的 Δ 而非 power-driven 的 Δ？\n\n**Q4**: Verbosity direction-aware NLI gate 恢复了 21 对（从 65% 到 86% pass rate），但这些恢复的对是否在 content quality 上与 bidirectional-pass 对系统不同？Appendix F 报告了 BT 的一致性，但未报告这两组在 Likert 质量分或 NLI 分数分布上的差异。\n\n**Q5**: 论文声称 Blindspot 对 RLHF/DPO pipeline 有重要启示，但未给出任何下游影响的实证。是否有初步实验表明 style bias 实际影响了 alignment 结果？\n\n---\n\n## Missing References\n\n未发现明显缺失的关键引用。论文对相关工作覆盖全面，包括 RATE (Reber et al., 2025)、Comparative Trap (Jeong et al., 2025)、self-preference (Panickssery et al., 2024) 等关键近期工作。\n\n建议考虑引用：\n- Stureborg et al. (2024) 关于 LLM judge calibration 的工作，与 Section 2 的 measurement sensitivity 讨论相关\n\n---\n\n## Overall Assessment 详细理由\n\n**3.5 (Borderline Conference)**\n\n这是一篇方法论扎实的实证研究，其核心发现（Likert Blindspot）有明确的实践意义。论文在因果声明的克制性、统计方法的严谨性、robustness check 的全面性上均优于同类工作。\n\n**推荐 Conference 的理由**：\n- Verbosity 轴的证据链完整且令人信服（Style OR 8–13, Orig ns, cross-rewriter validated, 4 judges consistent）\n- Sensitivity hierarchy（7 种方法）是有价值的方法论贡献\n- 对 LLM 评估社区（RLHF/DPO pipeline）有直接的 actionable implications\n\n**犹豫的理由**：\n- Formality 轴——论文的另一半核心 claim——受 quality confound 严重影响（N1），削弱了 \"detecting hidden style bias\" 的叙事统一性\n- 负控制说服力有限（W1, Δ=15pp 与 GPT-4o 最小 bias 几乎重叠）\n- 缺乏下游影响实证（Q5），限制了对 alignment 社区的直接贡献\n- 论文在 \"measurement attenuation vs construct divergence\" 之间保持 agnostic（Section 5.1），这虽然诚实，但也意味着 Blindspot 的 mechanistic interpretation 尚不明确\n\n如果作者能在 rebuttal 中：(1) 调整 formality claim 的措辞，区分 style-driven 和 confound-mixed 的发现；(2) 澄清 GEE CI 方法；(3) 讨论 stratified analysis 的 circularity——我愿意上调至 4.0。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告\n\n**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审查侧重**: 方法严谨性、实验设计、统计分析\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法论扎实、现象定义清晰的实证研究，verbosity 轴结果令人信服，但 formality 轴的 quality-style 混淆显著削弱核心 claim，TOST 等价检验边界偏宽，整体贡献介于 Findings 和 Conference 之间。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法设计合理，统计框架严谨，但 formality 轴 GEE 显示 Originality OR ≥ Style OR（多配置），\"style bias\" 的 claim 对该轴偏强；verbosity 轴 (OR 8–13, Orig ns) 方法论上无可挑剔 |\n| Excitement | 3.5/5 | Likert Blindspot 现象有明确的实践意义（RLHF/DPO 依赖 pairwise，但审计依赖 Likert），七种方法的 sensitivity hierarchy 是有价值的方法论贡献，但缺乏下游影响的实证 |\n| Reproducibility | 4/5 | 实现细节完整（模型版本、温度、种子），统计方法描述清晰，代码/数据承诺开源；扣分点：部分 GEE 配置缺少 QIC 绝对值 |\n| Reviewer Confidence | 4/5 | 熟悉 Bradley-Terry 模型、GEE、因果推断框架和 LLM 评估文献 |\n\n---\n\n## 主要优势\n\n1. **现象定义清晰且可复现**：Likert Blindspot 在 4 个 judge × 2 个主轴 × 3 个 benchmark 上一致出现（11 个 bias-positive cell 中 8 个），且用 7 种统计方法验证了 sensitivity hierarchy（Table 2），形成了强有力的证据链。\n\n2. **因果声明诚实克制**：Section 3.5 明确声明\"we do not claim that this DAG is a complete structural causal model\"，Figure 2 DAG 中用虚线橙色箭头标注 residual confounding，避免了过度因果宣称。这在该领域的论文中少见且值得肯定。\n\n3. **统计方法论严谨**：\n   - Holm-Bonferroni 校正 6 测试家族 + 8 测试敏感性分析（Appendix Q），全部保持显著\n   - BT 拟合优度检验（Appendix H：formality deviance p=0.198, verbosity p=0.905）\n   - GEE 诊断完整：exchangeable vs independence 对比（|ΔQIC| < 0.001）、交互项检验（所有 p > 0.13）、95% CI 完整报告\n   - Bootstrap attenuation analysis（Appendix J）区分 measurement attenuation 与 insufficient power，优于简单 post-hoc power\n\n4. **控制变量设计周全**：NLI 阈值 11 点 sweep（BT ≤ 3pp 变动）、cross-rewriter 验证（22% OR 下降但 Blindspot 持续）、same-style double-rewrite artifact control、Claude 负控制——形成多层防线。\n\n5. **Verbosity 轴证据链极强**：Style OR 8.2–13.1（四个 judge 一致），Originality OR 0.38–0.49（均不显著或边缘），direction-aware NLI 有理论和实证依据（Appendix F），cross-rewriter 验证完整（Appendix D Table 7）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Formality 轴 quality-style 混淆严重，核心 claim 对该轴偏强\n\n- 具体位置：Table 3（GEE decomposition）、Section 5.2\n- 问题：GEE 分解显示 formality 的 Originality OR 在多个配置中 ≥ Style OR：\n  - GPT-4o: Style 2.58 vs Orig 2.32（几乎相等）\n  - Qwen3 n=355: Style 2.15 vs Orig 4.99（originality 是 style 的 2.3 倍）\n  - Gemini: Style 1.64 (ns!) vs Orig 2.51\n  - Direction asymmetry（Appendix H: formal-origin 88.9% vs casual-origin 52.6%, Fisher p=0.015）进一步确认混淆存在\n\n  这意味着 pairwise 检测到的 formality \"bias\" 有相当部分是 quality-formality 相关性的反映，而非纯粹的 style bias。论文标题和 abstract 用 \"Detecting Hidden Style Bias\" 统一描述所有轴的发现，但 formality 轴检测到的更多是 quality confound + style effect 的混合信号。\n\n  Appendix H 的 stratified analysis（限制 Likert 等分对，BT=67.3%）作为 robustness check 有说服力，但存在一个 circularity 问题：论文的核心 claim 正是 Likert 对 style bias 不敏感，因此用 \"Likert 等分\" 作为 \"质量无差异\" 的代理变量存在逻辑矛盾。\n\n- 为什么影响接收：如果 formality 的 Blindspot 本质上是 pairwise 对 quality-style correlation 的放大，而非 Likert 遗漏了 style bias，则论文的核心叙事（\"hidden style bias\"）被削弱约一半。\n- 建议修改方向：\n  (a) 在 abstract/introduction 中区分 verbosity（纯 style-driven）和 formality（style + quality confound），不要统一称为 \"style bias\"\n  (b) 考虑将 formality 的发现重新定性为 \"measurement sensitivity divergence\" 而非 \"hidden bias detection\"\n  (c) 补充讨论 stratified analysis 的 circularity 并提出替代验证方案\n\n**N2** [critical] Bootstrap CI 的 pair-level resampling 在 GEE 语境下的合理性未论证\n\n- 具体位置：Section 4.1, \"All bootstrap CIs use 10,000 pair-level resamples\"\n- 问题：论文将 pair-level bootstrap 同时用于 BT 估计和 GEE 分解。对 BT 模型，pair-level resampling 是标准做法。但 GEE 使用 exchangeable working correlation 对 pair 内观测建模，其 CI 来自 sandwich standard errors（Appendix P），而非 bootstrap。这两套 CI 方法在论文中的分工不够清晰——Table 3 的 CI（Appendix C Table 6）使用哪种方法？如果是 sandwich SE，则与 Section 4.1 的 bootstrap 声明不一致；如果是 bootstrap，则需要论证 pair-level resampling 是否保持了 GEE 的 cluster 结构。\n- 为什么影响接收：CI 方法的不清晰可能影响 GEE OR 的统计推断可靠性。\n- 建议修改方向：明确区分 BT bootstrap CI 和 GEE sandwich CI 的适用范围，如果 GEE 也用 bootstrap，需论证 resampling 单位（pair vs cluster）的选择。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] TOST 等价检验边界 Δ=15pp 偏宽，负控制说服力有限\n\n- 具体位置：Section 5.4（Detection vs. amplification, control ii）、Appendix G\n- 问题：Claude Sonnet 4 的 TOST 在 Δ=15pp 时达到 p<0.05（76% power），但这意味着 Claude 可能存在高达 ~15pp 的未检测 style preference。GPT-4o formality 检测到的 bias 为 BT 63.0%（即 13pp 偏离 50%），与 TOST 边界几乎重叠。因此，Claude 负控制无法区分 \"真正无 bias\" 和 \"moderate bias but below detection threshold\"。\n  论文声称 Claude 的 bound 与 GPT-4o (13–23pp) \"substantively distinct\"，但 13pp 和 15pp 的差距仅 2pp，且 CI 大量重叠。\n- 建议：(a) 降低 claim 强度，承认 Δ=15pp 是 power 限制下的妥协而非 substantive bound; (b) 报告 Δ=10pp 时的 TOST power 和 p 值供读者判断; (c) 或增加 Claude 样本量以收紧边界。\n\n**W2** [warning] 人工标注验证规模偏小，inter-annotator agreement 仅 moderate\n\n- 具体位置：Section 5.4（Content preservation）、Appendix S\n- 问题：50 对（25 pass + 25 reject）由 2 名标注员评估，Cohen's κ=0.44（moderate）。A1 认为全部 25 pass 对保内容（precision 100%），A2 认为 21/25（84%）。4 个分歧全在 verbosity condensation 对上——而 verbosity 正是论文最强 claim 的支撑轴。这意味着 verbosity NLI gate 的 content preservation 标准在标注员间有实质性分歧。\n  Wilson CI [86.7%, 100%] 和 [65.3%, 93.6%] 的重叠区间说明精度估计本身不够精确。\n- 建议：(a) 增加标注量（至少 100 对）以收紧 CI; (b) 增加第三名标注员; (c) 讨论 verbosity condensation 的 content preservation 标准模糊性对结论的影响。\n\n**W3** [warning] Cross-benchmark replication 覆盖面有限\n\n- 具体位置：Table 1, Section 5.3\n- 问题：\n  - AlpacaEval 仅测 3 个配置（2 judges × formality + 1 verbosity）\n  - MT-Bench 仅测 2 个配置（2 judges × formality），无 verbosity\n  - Llama-70B 和 Gemini 未做 cross-benchmark 验证\n  - Register 轴无 cross-benchmark 验证\n  论文 claim \"cross-benchmark replication\" 但实际覆盖面较窄，尤其 verbosity（最强轴）仅在 AlpacaEval 有 1 个 cross-benchmark 数据点，且该点是 ‡（both sig，非 Blindspot）。\n- 建议：至少补充 MT-Bench verbosity 的 1-2 个 judge 数据；或降低 cross-benchmark claim 的强度。\n\n**W4** [warning] Cross-axis contamination中 formality→verbosity 的 word count shift (d=−0.23) 非 negligible\n\n- 具体位置：Appendix R, Table 18\n- 问题：formality 改写导致 word count 变化 d=−0.23，按 Cohen 标准属 \"small\" 但非 negligible（论文自设的 negligible 标准是 d<0.20）。论文以 \"directionally symmetric (formal→casual −5.0%, casual→formal +5.6%)\" 辩护，但 dataset-level 对称不等于 pair-level 对称——如果 formal→casual 方向的 pairs 和 casual→formal 方向的 pairs 在 quality 或 judge preference 上有系统差异（direction asymmetry 已经证明确实如此），则 cross-axis 污染可能不会在 aggregate 中抵消。\n- 建议：在 pair level 验证 word count 变化与 BT outcome 的相关性，或在 GEE 中加入 word count 变化作为 covariate。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 1 符号系统偏复杂**：†, ‡, †_e, †_c, --- 共 5 种标记，且 †_e 和 †_c 仅在脚注中解释。建议在正文首次出现时给出完整定义。\n\n2. **Figure 4（power curve）标题**：虽正文已引用 Hoenig & Hesse (2001) 避免 post-hoc power 误用，但 Figure caption 中 \"Detection probability at observed effect magnitudes\" 的表述仍可能被误读为 post-hoc power。建议在 caption 中加注 \"prospective sample-size planning\"。\n\n3. **Section 4.1 脚注 3（IIA）**：关于 binary-choice BT 模型中 IIA structurally satisfied 的声明是正确的，但脚注篇幅较长（~60 words），建议移至 Appendix H 与 GoF 检验合并讨论。\n\n4. **Register 轴定位不够清晰**：在 Table 1 中 register 占 6 行，但正文 Section 5.3 仅用一句话提及 register 是 \"exploratory and judge-dependent\"。建议将 register 结果移至 appendix 或更明确地标注为 exploratory pilot。\n\n5. **Limitations 段落\"Validation methodology and scale design\"**：提到 \"100-point experiment was tested with a single judge\" 但未在 Appendix M 中讨论为何仅选 Qwen3-32B（作为 evaluator-producer overlap 最严重的 judge）而非选无 overlap 的 GPT-4o。\n\n---\n\n## 问题（供作者回应）\n\n**Q1**: Appendix H 的 stratified analysis 用 Likert 等分对作为 \"无质量差异\" 的代理变量来验证 style bias 存在——但论文的核心 claim 是 Likert 对 style 不敏感。如何排除这一 circularity？是否考虑过使用外部质量指标（如人工评分或参考答案匹配度）替代 Likert 作为 quality proxy？\n\n**Q2**: 对于 formality 轴，Qwen3 n=355 的 GEE 分解显示 Originality OR (4.99) 是 Style OR (2.15) 的 2.3 倍。在这种 confound structure 下，\"formality bias\" 的表述是否仍然恰当？是否应改为 \"formality-related preference divergence\"？\n\n**Q3**: TOST Δ=15pp 的选择基准是什么？是否是 smallest effect of interest (SESOI) 的估计，还是纯粹由 power 限制决定？如果是后者，论文是否应报告基于 SESOI 的 Δ 而非 power-driven 的 Δ？\n\n**Q4**: Verbosity direction-aware NLI gate 恢复了 21 对（从 65% 到 86% pass rate），但这些恢复的对是否在 content quality 上与 bidirectional-pass 对系统不同？Appendix F 报告了 BT 的一致性，但未报告这两组在 Likert 质量分或 NLI 分数分布上的差异。\n\n**Q5**: 论文声称 Blindspot 对 RLHF/DPO pipeline 有重要启示，但未给出任何下游影响的实证。是否有初步实验表明 style bias 实际影响了 alignment 结果？\n\n---\n\n## Missing References\n\n未发现明显缺失的关键引用。论文对相关工作覆盖全面，包括 RATE (Reber et al., 2025)、Comparative Trap (Jeong et al., 2025)、self-preference (Panickssery et al., 2024) 等关键近期工作。\n\n建议考虑引用：\n- Stureborg et al. (2024) 关于 LLM judge calibration 的工作，与 Section 2 的 measurement sensitivity 讨论相关\n\n---\n\n## Overall Assessment 详细理由\n\n**3.5 (Borderline Conference)**\n\n这是一篇方法论扎实的实证研究，其核心发现（Likert Blindspot）有明确的实践意义。论文在因果声明的克制性、统计方法的严谨性、robustness check 的全面性上均优于同类工作。\n\n**推荐 Conference 的理由**：\n- Verbosity 轴的证据链完整且令人信服（Style OR 8–13, Orig ns, cross-rewriter validated, 4 judges consistent）\n- Sensitivity hierarchy（7 种方法）是有价值的方法论贡献\n- 对 LLM 评估社区（RLHF/DPO pipeline）有直接的 actionable implications\n\n**犹豫的理由**：\n- Formality 轴——论文的另一半核心 claim——受 quality confound 严重影响（N1），削弱了 \"detecting hidden style bias\" 的叙事统一性\n- 负控制说服力有限（W1, Δ=15pp 与 GPT-4o 最小 bias 几乎重叠）\n- 缺乏下游影响实证（Q5），限制了对 alignment 社区的直接贡献\n- 论文在 \"measurement attenuation vs construct divergence\" 之间保持 agnostic（Section 5.1），这虽然诚实，但也意味着 Blindspot 的 mechanistic interpretation 尚不明确\n\n如果作者能在 rebuttal 中：(1) 调整 formality claim 的措辞，区分 style-driven 和 confound-mixed 的发现；(2) 澄清 GEE CI 方法；(3) 讨论 stratified analysis 的 circularity——我愿意上调至 4.0。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-22T18:15:12.291167+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3663
}
```

</details>

---


### Assistant

_source line 816 · 2026-05-22T18:15:23.444350+00:00_

审稿报告已提交给 Review Director。

**评分摘要**：Overall 3.5 (Borderline Conference)

**核心判断**：
- **Verbosity 轴**证据极强（Style OR 8–13, Orig ns, 四个 judge 一致），方法论无可挑剔
- **Formality 轴**受 quality-style 混淆严重影响（Qwen3 n=355: Orig OR 4.99 vs Style OR 2.15），论文标题 "Detecting Hidden Style Bias" 对该轴偏强
- 统计方法论整体严谨（Holm-Bonferroni、BT GoF、GEE 诊断、NLI sweep），是该领域少见的高标准工作
- 两个 Must-Fix：(1) formality claim 需降级或重新措辞；(2) bootstrap vs sandwich CI 在 GEE 语境下的分工需澄清
- 四个 Should-Fix：TOST Δ=15pp 偏宽、人工标注规模偏小、cross-benchmark 覆盖有限、cross-axis 污染非 negligible

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 26

## Round 26

4 recorded events


### User

_source line 817 · 2026-05-22T18:16:31.684521+00:00_

[Round 10 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿报告：The Likert Blindspot

### Summary

本文提出 Controlled Style Decomposition (CSD)，一个黑盒框架，通过 NLI 门控内容保持、单轴风格改写和位控 pairwise 比较来量化 LLM judge 的风格偏差。核心发现为"Likert Blindspot"：Likert 评分系统性地衰减 pairwise 比较能检测到的风格偏差信号——在中等偏差时完全衰减（d → 0），在较强效应时信号损失 >60%。在 4 个目标 judge + 1 个负控制、3 个风格轴、3 个 benchmark 上验证。GEE 条件分解揭示了逐轴混淆结构。

---

### Strengths

**S1. 实验设计严谨，控制充分。** 六项独立的放大控制（NLI gate ablation、负控制 judge、跨轴变异、rewriting artifact 吸收、debiased prompting、跨架构复现）显示出对 "Comparative Trap" 反面论证的充分意识。Position swap 双向评估 + consistent pairs sign test 设计合理。(§5.1, §5.4)

**S2. 统计分析多层次且透明。** 七种测量方法的灵敏度层级（Table 2）、Holm-Bonferroni 校正、探索性与验证性分析的明确区分、bootstrap 衰减分析和形式化功效分析（Appendix K），体现了高标准的统计实践。

**S3. 跨 judge 一致性强。** 四个独立架构一致复现 Blindspot（Table 1），GEE 混淆结构跨 judge 一致（verbosity 全部 Style OR 8–13，formality 全部条件显著）。

**S4. Limitations 坦诚全面。** 对 quality-style confounding、evaluator-producer overlap、construct divergence 的歧义性进行了充分讨论。

**S5. GEE 混淆分解有实用价值。** 将风格效应与 originality 效应分离，对从业者有直接指导意义。

---

### Must-Fix 问题（critical）

**N1 [critical] 核心歧义未解决，但标题和 framing 隐式预设 pairwise 为 ground truth**

论文标题 "Detecting Hidden Style Bias" 和 "Blindspot" 命名隐式假定 pairwise 检测到的是真实偏差、Likert 遗漏了它。然而论文自身承认三种等效解释：(a) Likert 测量衰减，(b) pairwise 放大（Comparative Trap），(c) 构念分歧。六项放大控制必要但非充分——负控制的 TOST Δ=15pp 实质性过宽（14pp win probability 差异会被判为"等价"），且仅一个负控制模型。建议标题改为更中性的表述，Abstract 前置三种解释。

**N2 [critical] 新颖性定位不足："Likert Blindspot" 本质是 Thurstone (1927) 在 LLM judge 领域的实证确认**

Forced-choice 比 rating scale 灵敏度更高是心理测量学经典结论（Thurstone 1927, Preston & Colman 2000, DeCoster & Iselin 2011），论文自己引用了这些文献。"unquantified" 的声明技术上正确，但核心机制完全可从已有理论预测。增量贡献是实证量化——有价值，但不足以支撑 "demonstrates"/"identifies" 等发现性措辞。建议明确定位为"首次在 LLM judge 下的系统性实证量化"，并深度对比 LLM judge 场景是否超越传统理论预测。

---

### Should-Fix 问题（warning）

**W1 [warning] Formality 轴的 GEE 结果削弱 "style bias" 叙事。** Table 3 中多个 judge 的 Orig OR ≥ Style OR（GPT-4o: 2.32 vs 2.58; Qwen3: 4.70 vs 4.20），pairwise 检测到的可能更多是与 formality 相关的质量差异而非纯粹的 style bias。

**W2 [warning] Register 轴 evaluator-producer overlap 严重且无跨改写器验证。** Register 所有改写用 Qwen3-32B 且无交叉验证，BT 结果也较弱。建议降级为 "exploratory pilot axis"。

**W3 [warning] 三个风格轴不足以支撑 "framework" 泛化。** 第四轴（tone）因 NLI gate 拒绝率过高放弃，表明适用性受限。建议软化为 "methodology for content-preserving style axes"。

**W4 [warning] 跨 benchmark 覆盖稀疏。** AlpacaEval 3 配置、MT-Bench 2 配置，verbosity 仅跨 benchmark 验证了 Qwen3 一个 judge。"three benchmarks" 声明名义上成立但实际覆盖很低。

**W5 [warning] 负控制 TOST Δ=15pp 过宽且仅一个模型。** 建议报告不同 Δ 下的 TOST 结果（10pp, 5pp），讨论 15pp 的实际含义。

---

### Minor 问题

- M1: Abstract 数字密度过高
- M2: Introduction 开头单实例不能代表系统性模式，caveat 应前置
- M3: 对 RATE 的批评措辞过于直接
- M4: Figure 2 DAG 中 orange dashed arrow 标注字号过小
- M5: Table 1 五种标记系统认知负担高
- M6: Limitations 约 1.5 页可适当精简

---

### Missing References

1. Carterette et al. (2008) — forced-choice vs. graded relevance 判断灵敏度差异（ECIR）
2. Sedoc & Ungar (2020) — IRT 模型应用于 chatbot 评估（ACL）
3. Deutsch et al. (2023) — tie 处理对评估指标灵敏度的影响（EMNLP）

---

### 官方维度打分（ACL ARR）

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3.5/5 | 方法严谨但核心歧义未解决；formality 混淆结构削弱叙事；TOST Δ 过宽 |
| Excitement | 2.5/5 | 经典心理测量学结论的领域迁移，非新发现；GEE 分解有增量贡献 |
| Reproducibility | 4/5 | 代码数据承诺发布；统计方法详细；模型版本固定 |

### Overall Assessment

**Overall: 3.0 — Findings**

实验设计严谨、统计分析透明的实证工作，但核心发现（Likert 对风格偏差的灵敏度低于 pairwise）本质是心理测量学经典理论在 LLM judge 场景的实证确认而非新发现，detection vs. amplification 核心歧义未解决，新颖性和 excitement 不足以达到主会议水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-22T18:18:08.913643+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Strengths\n\n**[AGREE] S1–S5**: R2 对论文优势的概括准确全面，与我的评估一致。特别是 S2（统计分析多层次且透明）和 S4（Limitations 坦诚全面）是本文优于同类工作的突出特点。\n\n---\n\n### Must-Fix 问题\n\n**[AGREE with nuance] R2-N1: 核心歧义未解决，标题/framing 预设 pairwise 为 ground truth**\n\n同意标题 \"Detecting Hidden Style Bias\" 和 \"Blindspot\" 命名存在隐式偏向。我在自己的审稿中也将此列为 critical issue（R1-N1），理由相似但侧重不同：我从 formality 轴 GEE 数据出发（Qwen3 n=355: Style OR 2.15 vs Orig OR 4.99, Table 3），指出检测到的并非纯粹 style bias，R2 从更高层次指出三种等效解释未被 resolve。\n\n不过，我认为 R2 的措辞略有过度。论文在 Section 5.1 已明确呈现三种解释并保持 agnostic（\"Both interpretations lead to the same conclusion\"），Limitations 第一段也直接讨论了 construct divergence。问题不在于论文 body 回避了歧义，而在于**标题和 abstract 的 framing 与正文的 agnostic 态度不匹配**。这是一个 framing 调整问题，而非方法论缺陷。\n\n建议：标题改为 \"The Likert Blindspot: Measurement Sensitivity Divergence in LLM Judge Style Evaluation\" 或类似中性措辞即可回应此批评，不需要大改方法论。\n\n---\n\n**[REBUT] R2-N2: \"Likert Blindspot\" 本质是 Thurstone (1927) 的实证确认，新颖性不足**\n\nR2 认为 forced-choice 比 rating scale 更灵敏是心理测量学经典结论（Thurstone 1927, Preston & Colman 2000），论文只是该理论在 LLM judge 领域的实证确认。我不同意将此评为 critical 级别，理由如下：\n\n1. **效应幅度远超理论预测**：传统心理测量学的灵敏度差异是 gradual 的（效应更小、需要更大 n），但论文发现的是 **categorical failure**——Likert 在 n=88 到 n=355 的范围内 d 始终趋近于零（bootstrap attenuation analysis, Appendix J, Table 11: d_median = −0.017），而 pairwise BT 在同一数据上达 63–77%。七种 Likert 方法全部失败（Table 2），tie rate 高达 58–73%。这不是 \"灵敏度较低\"，而是 \"系统性完全失效\"——这一幅度在传统心理测量学中没有先例，因为人类评分者不会产生如此极端的 tie rate。\n\n2. **GEE 条件分解是方法论增量贡献**：R2 自己在 S5 中肯定了 \"GEE 混淆分解有实用价值\"。将 style 效应从 originality 混淆中分离的逐轴分解（Table 3），以及由此揭示的 verbosity 纯 style-driven vs formality quality-confounded 的轴间差异，是经典 Thurstone 理论完全未涉及的。\n\n3. **实践影响不可从理论推导**：即使理论上可预测 \"pairwise 更灵敏\"，但 **RLHF/DPO pipeline 依赖 pairwise 而审计依赖 Likert** 这一具体 gap 在本文之前并未被 *CL 社区系统性识别或量化。Thurstone 的理论不能告诉你 \"GPT-4o 在 formality 上有 13pp 的 pairwise bias 但 Likert d=0.10\"。\n\n4. **实证量化本身在 *CL 会议中有先例被接收**：大量 *CL best paper 的核心贡献是对已知现象的首次系统性量化（如 position bias 的量化、self-preference 的量化）。R2 的标准如果严格执行，会 dismiss 许多已发表的重要工作。\n\n**结论**：将此评为 critical 不恰当。建议作者在 Introduction 中加一段 \"Our contribution beyond classical measurement theory\" 的定位，承认 Thurstone 的理论基础但强调 LLM judge 的独特性（极端 tie rate、系统性 categorical failure、GEE 分解），将 N2 降级为 Should-Fix 级别的 framing 建议。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Formality 轴 GEE 结果削弱 \"style bias\" 叙事**\n\n完全同意，与我的 R1-N1 一致。GPT-4o formality Style OR 2.58 vs Orig OR 2.32 几乎相等，Qwen3 n=355 的 Orig OR (4.99) 更是 Style OR (2.15) 的 2.3 倍（Table 3）。需要在正文中显著区分 verbosity（纯 style-driven）和 formality（style + quality confound）。\n\n**[AGREE] R2-W2: Register 轴无跨改写器验证**\n\n完全同意。Limitations 已承认（\"register conclusions remain tentative pending independent rewriter validation\"），但 Table 1 中 register 仍占 6 行主结果空间。建议移至 appendix 或明确标注 \"exploratory pilot\"，我在自己审稿的小问题第 4 条中也提出了同样建议。\n\n**[AGREE with nuance] R2-W3: 三个风格轴不足以支撑 \"framework\" 泛化**\n\n同意 tone 轴因 NLI gate 拒绝率过高被放弃，表明 CSD 的适用范围限于 content-preserving style axes。但论文并未声称 CSD 适用于所有 style axes——Section 3.1 已限定为 style-controlled rewriting，且 tone 轴的失败本身被 Limitations 引用为 NLI gate 有效性的积极证据（\"confirming that the quality gate prevents content-altering manipulations\"）。R2 的建议（软化为 \"methodology for content-preserving style axes\"）合理，但严重性应为 minor 而非 warning。\n\n**[AGREE] R2-W4: 跨 benchmark 覆盖稀疏**\n\n完全同意，与我的 R1-W3 一致。特别是 verbosity 作为最强轴在 MT-Bench 上无数据点。\n\n**[AGREE] R2-W5: 负控制 TOST Δ=15pp 过宽**\n\n完全同意，与我的 R1-W1 一致。GPT-4o formality bias 为 13pp（BT 63.0%），与 TOST Δ=15pp 仅差 2pp。R2 关于报告 Δ=10pp 和 5pp 的 TOST 结果的建议可操作且有价值。\n\n---\n\n### Minor 问题\n\n**[AGREE] R2-M1 (Abstract 数字密度)**: 同意，abstract 中 \"n=88\", \"69%\", \"BT > 0.50\" 等数字堆叠影响可读性。\n\n**[REBUT] R2-M2 (Introduction 开头单实例)**: 论文开头 \"What is the average height of a male?\" 例子用于直觉引入 Likert vs pairwise 的灵敏度差异，是 motivating example 而非 evidence。紧接着的正文明确用系统性数据支撑 claim。这种写法在顶会论文中常见且有效。\n\n**[AGREE] R2-M3 (对 RATE 的批评措辞)**: Section 5.1 的 \"Head-to-head comparison with RATE\" 可能给人 adversarial 感。建议改为 \"Complementary analysis with RATE\" 或 \"Extending RATE's framework\"。\n\n**[AGREE] R2-M4–M6**: Figure 2 标注字号、Table 1 符号系统（我也提出了同样意见）、Limitations 篇幅均为合理的排版改进建议。\n\n---\n\n### Missing References\n\n**[AGREE] R2 建议的三篇文献**:\n- Carterette et al. (2008) — forced-choice vs graded relevance 在 IR 领域的比较，与 Table 2 sensitivity hierarchy 直接相关\n- Sedoc & Ungar (2020) — IRT 用于 chatbot 评估，与 Likert scale 的心理测量特性讨论相关\n- Deutsch et al. (2023) — tie 处理对评估灵敏度的影响，与论文发现的 58–73% tie rate 直接相关\n\n均为有价值的补充引用，特别是 Deutsch et al. (2023) 可以加强 Section 5.1 关于 tie rate 驱动 Blindspot 的论证。\n\n---\n\n### Overall Assessment 差异讨论\n\nR2 给出 **3.0 (Findings)**，我给出 **3.5 (Borderline Conference)**。0.5 分差异主要来自对 N2（新颖性）的分歧。\n\nR2 将 novelty concern 升级为 critical，认为 Likert Blindspot 是 \"经典心理测量学结论的领域迁移\"。如上所述，我认为这低估了：(a) 效应幅度的 categorical nature（非 gradual attenuation），(b) GEE 分解的方法论贡献，(c) 实践影响（RLHF/DPO 审计 gap）的独立价值。\n\n如果将 N2 从 critical 降至 warning（我认为更恰当），R2 的实际审评只有 N1 一个 critical issue（framing），与我的评估基本一致。在这种情况下，论文经过 framing 调整后应处于 3.5 (Borderline Conference) 的水平。\n\n维持我的 **3.5 (Borderline Conference)** 评分，条件性上调至 4.0 取决于 rebuttal 中对 formality confounding framing（R1-N1 / R2-N1 / R2-W1）的回应质量。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Strengths\n\n**[AGREE] S1–S5**: R2 对论文优势的概括准确全面，与我的评估一致。特别是 S2（统计分析多层次且透明）和 S4（Limitations 坦诚全面）是本文优于同类工作的突出特点。\n\n---\n\n### Must-Fix 问题\n\n**[AGREE with nuance] R2-N1: 核心歧义未解决，标题/framing 预设 pairwise 为 ground truth**\n\n同意标题 \"Detecting Hidden Style Bias\" 和 \"Blindspot\" 命名存在隐式偏向。我在自己的审稿中也将此列为 critical issue（R1-N1），理由相似但侧重不同：我从 formality 轴 GEE 数据出发（Qwen3 n=355: Style OR 2.15 vs Orig OR 4.99, Table 3），指出检测到的并非纯粹 style bias，R2 从更高层次指出三种等效解释未被 resolve。\n\n不过，我认为 R2 的措辞略有过度。论文在 Section 5.1 已明确呈现三种解释并保持 agnostic（\"Both interpretations lead to the same conclusion\"），Limitations 第一段也直接讨论了 construct divergence。问题不在于论文 body 回避了歧义，而在于**标题和 abstract 的 framing 与正文的 agnostic 态度不匹配**。这是一个 framing 调整问题，而非方法论缺陷。\n\n建议：标题改为 \"The Likert Blindspot: Measurement Sensitivity Divergence in LLM Judge Style Evaluation\" 或类似中性措辞即可回应此批评，不需要大改方法论。\n\n---\n\n**[REBUT] R2-N2: \"Likert Blindspot\" 本质是 Thurstone (1927) 的实证确认，新颖性不足**\n\nR2 认为 forced-choice 比 rating scale 更灵敏是心理测量学经典结论（Thurstone 1927, Preston & Colman 2000），论文只是该理论在 LLM judge 领域的实证确认。我不同意将此评为 critical 级别，理由如下：\n\n1. **效应幅度远超理论预测**：传统心理测量学的灵敏度差异是 gradual 的（效应更小、需要更大 n），但论文发现的是 **categorical failure**——Likert 在 n=88 到 n=355 的范围内 d 始终趋近于零（bootstrap attenuation analysis, Appendix J, Table 11: d_median = −0.017），而 pairwise BT 在同一数据上达 63–77%。七种 Likert 方法全部失败（Table 2），tie rate 高达 58–73%。这不是 \"灵敏度较低\"，而是 \"系统性完全失效\"——这一幅度在传统心理测量学中没有先例，因为人类评分者不会产生如此极端的 tie rate。\n\n2. **GEE 条件分解是方法论增量贡献**：R2 自己在 S5 中肯定了 \"GEE 混淆分解有实用价值\"。将 style 效应从 originality 混淆中分离的逐轴分解（Table 3），以及由此揭示的 verbosity 纯 style-driven vs formality quality-confounded 的轴间差异，是经典 Thurstone 理论完全未涉及的。\n\n3. **实践影响不可从理论推导**：即使理论上可预测 \"pairwise 更灵敏\"，但 **RLHF/DPO pipeline 依赖 pairwise 而审计依赖 Likert** 这一具体 gap 在本文之前并未被 *CL 社区系统性识别或量化。Thurstone 的理论不能告诉你 \"GPT-4o 在 formality 上有 13pp 的 pairwise bias 但 Likert d=0.10\"。\n\n4. **实证量化本身在 *CL 会议中有先例被接收**：大量 *CL best paper 的核心贡献是对已知现象的首次系统性量化（如 position bias 的量化、self-preference 的量化）。R2 的标准如果严格执行，会 dismiss 许多已发表的重要工作。\n\n**结论**：将此评为 critical 不恰当。建议作者在 Introduction 中加一段 \"Our contribution beyond classical measurement theory\" 的定位，承认 Thurstone 的理论基础但强调 LLM judge 的独特性（极端 tie rate、系统性 categorical failure、GEE 分解），将 N2 降级为 Should-Fix 级别的 framing 建议。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Formality 轴 GEE 结果削弱 \"style bias\" 叙事**\n\n完全同意，与我的 R1-N1 一致。GPT-4o formality Style OR 2.58 vs Orig OR 2.32 几乎相等，Qwen3 n=355 的 Orig OR (4.99) 更是 Style OR (2.15) 的 2.3 倍（Table 3）。需要在正文中显著区分 verbosity（纯 style-driven）和 formality（style + quality confound）。\n\n**[AGREE] R2-W2: Register 轴无跨改写器验证**\n\n完全同意。Limitations 已承认（\"register conclusions remain tentative pending independent rewriter validation\"），但 Table 1 中 register 仍占 6 行主结果空间。建议移至 appendix 或明确标注 \"exploratory pilot\"，我在自己审稿的小问题第 4 条中也提出了同样建议。\n\n**[AGREE with nuance] R2-W3: 三个风格轴不足以支撑 \"framework\" 泛化**\n\n同意 tone 轴因 NLI gate 拒绝率过高被放弃，表明 CSD 的适用范围限于 content-preserving style axes。但论文并未声称 CSD 适用于所有 style axes——Section 3.1 已限定为 style-controlled rewriting，且 tone 轴的失败本身被 Limitations 引用为 NLI gate 有效性的积极证据（\"confirming that the quality gate prevents content-altering manipulations\"）。R2 的建议（软化为 \"methodology for content-preserving style axes\"）合理，但严重性应为 minor 而非 warning。\n\n**[AGREE] R2-W4: 跨 benchmark 覆盖稀疏**\n\n完全同意，与我的 R1-W3 一致。特别是 verbosity 作为最强轴在 MT-Bench 上无数据点。\n\n**[AGREE] R2-W5: 负控制 TOST Δ=15pp 过宽**\n\n完全同意，与我的 R1-W1 一致。GPT-4o formality bias 为 13pp（BT 63.0%），与 TOST Δ=15pp 仅差 2pp。R2 关于报告 Δ=10pp 和 5pp 的 TOST 结果的建议可操作且有价值。\n\n---\n\n### Minor 问题\n\n**[AGREE] R2-M1 (Abstract 数字密度)**: 同意，abstract 中 \"n=88\", \"69%\", \"BT > 0.50\" 等数字堆叠影响可读性。\n\n**[REBUT] R2-M2 (Introduction 开头单实例)**: 论文开头 \"What is the average height of a male?\" 例子用于直觉引入 Likert vs pairwise 的灵敏度差异，是 motivating example 而非 evidence。紧接着的正文明确用系统性数据支撑 claim。这种写法在顶会论文中常见且有效。\n\n**[AGREE] R2-M3 (对 RATE 的批评措辞)**: Section 5.1 的 \"Head-to-head comparison with RATE\" 可能给人 adversarial 感。建议改为 \"Complementary analysis with RATE\" 或 \"Extending RATE's framework\"。\n\n**[AGREE] R2-M4–M6**: Figure 2 标注字号、Table 1 符号系统（我也提出了同样意见）、Limitations 篇幅均为合理的排版改进建议。\n\n---\n\n### Missing References\n\n**[AGREE] R2 建议的三篇文献**:\n- Carterette et al. (2008) — forced-choice vs graded relevance 在 IR 领域的比较，与 Table 2 sensitivity hierarchy 直接相关\n- Sedoc & Ungar (2020) — IRT 用于 chatbot 评估，与 Likert scale 的心理测量特性讨论相关\n- Deutsch et al. (2023) — tie 处理对评估灵敏度的影响，与论文发现的 58–73% tie rate 直接相关\n\n均为有价值的补充引用，特别是 Deutsch et al. (2023) 可以加强 Section 5.1 关于 tie rate 驱动 Blindspot 的论证。\n\n---\n\n### Overall Assessment 差异讨论\n\nR2 给出 **3.0 (Findings)**，我给出 **3.5 (Borderline Conference)**。0.5 分差异主要来自对 N2（新颖性）的分歧。\n\nR2 将 novelty concern 升级为 critical，认为 Likert Blindspot 是 \"经典心理测量学结论的领域迁移\"。如上所述，我认为这低估了：(a) 效应幅度的 categorical nature（非 gradual attenuation），(b) GEE 分解的方法论贡献，(c) 实践影响（RLHF/DPO 审计 gap）的独立价值。\n\n如果将 N2 从 critical 降至 warning（我认为更恰当），R2 的实际审评只有 N1 一个 critical issue（framing），与我的评估基本一致。在这种情况下，论文经过 framing 调整后应处于 3.5 (Borderline Conference) 的水平。\n\n维持我的 **3.5 (Borderline Conference)** 评分，条件性上调至 4.0 取决于 rebuttal 中对 formality confounding framing（R1-N1 / R2-N1 / R2-W1）的回应质量。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-22T18:18:12.530530+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3616
}
```

</details>

---


### Assistant

_source line 820 · 2026-05-22T18:18:19.352594+00:00_

交叉回应已提交。核心分歧在 R2-N2（新颖性）：R2 认为是 Thurstone 的领域迁移，我认为 categorical failure 的幅度（d→0 vs BT 63–77%）、GEE 分解、实践影响超越了简单理论确认，不应评为 critical。对 R2 的其余意见（N1 framing、W1–W5）基本同意，与我自己的审稿一致。维持 3.5 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 27

## Round 27

50 recorded events


### User

_source line 821 · 2026-05-22T19:30:49.331410+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 统计方法 + 实验设计**。

## 投稿信息
- **Venue**: EMNLP 2026（通过 ARR 统一审稿）
- **Deadline**: 2026-05-25
- **格式要求**: ACL 模板，Long paper 正文 ≤8 页，参考文献不限，Limitations 不计入页数
- **匿名规则**: Double-blind
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf`

## 论文概要
标题：*The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation*
核心发现：Likert 评分和 pairwise comparison 在检测 LLM judge 风格偏差时产生系统性分歧——pairwise 检测到 Likert 完全遗漏的偏好（BT > 60%, p < 0.001; Likert d → 0, p > 0.17）。提出 CSD 框架（NLI-gated 内容控制 + per-axis 风格分解 + position-controlled pairwise comparison），跨 4 个 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 个负控制（Claude Sonnet 4）+ 3 个 benchmark + 7 种统计方法验证。GEE 条件分解揭示 per-axis 混淆结构差异（verbosity = style-dominated, formality = conditional effect, register = judge-dependent）。

## 你的审查侧重

### 1. 统计方法严谨性
- Bradley-Terry 模型的 IIA 假设在该数据中是否成立？脚注 3 声称 binary-choice BT 中 IIA "structurally satisfied"，是否正确？Appendix H 的 direction asymmetry (formality: 88.9% vs 52.6%) 对 BT 估计的影响？
- GEE 使用 exchangeable working correlation + sandwich SE 是否合适？Appendix C 的模型诊断是否充分？
- Bootstrap CI（10,000 pair-level resamples）与 GEE sandwich SE 的分工是否清晰？Table 3 CI 来源？
- Holm-Bonferroni 校正的 test family 定义（§4.1 "six tests"）是否合理？Gemini 作为 confirmatory 排除在外的理由？
- TOST 等价检验 Δ=15pp 的合理性？与 GPT-4o formality 最小 bias (13pp) 几乎重叠——Claude 可能有未检测的 moderate bias？

### 2. 实验设计
- NLI gate（DeBERTa-v3-large, τ=0.90）：44% 拒绝率造成的选择偏差？Appendix B 的 4 个 surface covariate 检查是否充分？
- Direction-aware NLI gate 恢复的 21 对在 content quality 上是否与 bidirectional-pass 对系统不同？
- 人工标注（50 对，2 名标注员，κ=0.44）：规模是否足够？Wilson CI 下界 86.3% 的 precision 是否支撑核心 claim？
- Cross-axis contamination：formality→verbosity word count shift d=−0.23 超过论文自设 negligible 标准 (d<0.20)——是否需要在 GEE 中加 word count covariate？
- 100-point continuous Likert 仅用 Qwen3-32B judge，存在 evaluator-producer overlap，选择理由？

### 3. 因果/方法论声明
- §3.5 Design Rationale 的因果免责声明是否充分？论文标题中 "Measurement-Mode Divergence" 是否中性？
- DAG（Figure 2）的残余混淆路径（S→Q dashed）讨论是否充分？
- "Controlled Style Decomposition" 中 "Controlled" 是否给人过强的因果推断印象？

### 4. 格式合规
- 正文是否 ≤8 页？
- Double-blind 是否合规（无作者信息泄露）？
- Limitations 是否合理（不含新实验结果）？

请按以下格式输出审稿报告：
1. **Summary** (2-3 句)
2. **Strengths** (逐条)
3. **Weaknesses** (逐条，标注 severity: Must-Fix / Should-Fix / Minor)
4. **Questions** (需要作者回答)
5. **Missing References** (如有)
6. **Novelty** (1-5 分)
7. **Soundness** (1-5 分)
8. **Excitement** (1-5 分)
9. **Overall Assessment** (使用 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-22T19:31:01.028586+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 823 · 2026-05-22T19:31:01.079160+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 824 · 2026-05-22T19:31:09.212753+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 825 · 2026-05-22T19:31:11.722483+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf",
  "pages": "1-10",
  "project": "causal_style_decomp_judge",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf",
    "pages": "1-10",
    "project": "causal_style_decomp_judge",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 826 · 2026-05-22T19:31:16.089472+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results for ACL ARR 2026 reviewer guidelines, here are the key information about the review form criteria and scoring:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Review Form Criteria

The main criteria for Findings are soundness and reproducibility, while
…[truncated 940 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6876
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-22T19:31:17.344226+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 468.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 587.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p9.p
…[truncated 526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5621
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-22T19:31:25.134258+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form fields, scoring dimensions, and their scales. Especially: soundness scale, excitement scale, overall assessment scale with all levels, and any other required fields like confidence, responsible NLP checklist, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form fields, scoring dimensions, and their scales. Especially: soundness scale, excitement scale, overall assessment scale with all levels, and any other required fields like confidence, responsible NLP checklist, etc."
  }
}
```

</details>

---


### Tool call

_source line 829 · 2026-05-22T19:31:26.139053+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-22T19:31:26.641215+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 831 · 2026-05-22T19:31:26.943317+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-22T19:31:27.047479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-22T19:31:27.550600+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-22T19:31:27.652084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-22T19:31:28.208397+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1160
}
```

</details>

---


### Tool result

_source line 836 · 2026-05-22T19:31:28.510263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-22T19:31:33.133710+00:00_

# ACL Rolling Review Form - Complete Structure

## Core Review Fields

**Paper Summary** - Descriptive narrative of paper topic and content

**Summary of Strengths** - Major publication reasons for selective *ACL venues

**Summary of Weaknesses** - Numbered concerns prioritized against competing papers

**Comments/Suggestions/Typos** - Additional improvement recommendations

## Scoring Dimensions

### Reviewer Confidence
Scale 1-5:
- 5 = "Positive that my evaluation is correct"
- 4 = "Quite sure"
- 3 = "Pretty sure, but there's a chance I missed something"
- 2 = "Willing to defend my evaluation, but fairly likely missed details"
- 1 = "Not my area, or paper is very hard to understand"

### Soundness
Scale 1-5 (with .5 increments):
- 5 = "Excellent: one of the most thorough"
- 4 = "Strong: sufficient support for all claims"
- 3 = "Acceptable: sufficient support for main claims"
- 2 = "Poor: main claims not sufficiently supported"
- 1 = "Major Issues: not sufficiently thorough"

### Excitement
Scale 1-5 (with .5 increments):
- 5 = "Highly Exciting: would recommend to others"
- 4 = "Exciting: would mention to others"
- 3 = "Interesting: might mention some points"
- 2 = "Potentially Interesting: doesn't resonate with me"
- 1 = "Not Exciting: doesn't resonate or relate to NLP"

### Overall Assessment
Scale 1-5 (with .5 increments):
- 5 = "Consider for Award: top 2.5% papers"
- 4.5 = "Borderline Award"
- 4 = "Conference: accept to *ACL"
- 3.5 = "Borderline Conference"
- 3 = "Findings: accept to Findings track"
- 2.5 = "Borderline Findings"
- 2 = "Resubmit next cycle"
- 1.5 = "Resubmit after next cycle"
- 1 = "Do not resubmit"

## Additional Required Fields

**Best Paper Justification** - Conditional on Award scores

**Limitations and Societal Impact** - Assessment of author discussion

**Ethical Concerns** - ACL code of ethics compliance review

**Needs Ethics Review** - Flag for ethics committee consideration

**Reproducibility**
Scale 1-5: from "easily reproduce" to "ca
…[truncated 266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7999
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-22T19:31:43.242945+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 839 · 2026-05-22T19:31:43.644896+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 840 · 2026-05-22T19:31:44.198739+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 841 · 2026-05-22T19:31:44.199175+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 842 · 2026-05-22T19:31:45.160193+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1515
}
```

</details>

---


### Tool call

_source line 843 · 2026-05-22T19:31:45.160732+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-22T19:31:45.564008+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-22T19:31:46.018410+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1819
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-22T19:31:46.018809+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 847 · 2026-05-22T19:31:47.076939+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1916
}
```

</details>

---


### Tool result

_source line 848 · 2026-05-22T19:31:47.530979+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1966
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-22T19:31:47.531973+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1513
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-22T19:31:55.864322+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf",
  "pages": "11-18",
  "project": "causal_style_decomp_judge",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf",
    "pages": "11-18",
    "project": "causal_style_decomp_judge",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-22T19:31:56.767742+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 432.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 571.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 581.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 602.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 143.3}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_styl
…[truncated 93 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-22T19:32:00.132213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 853 · 2026-05-22T19:32:00.484063+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 854 · 2026-05-22T19:32:01.542153+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-22T19:32:01.543256+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-22T19:32:01.694222+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 857 · 2026-05-22T19:32:02.196323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 858 · 2026-05-22T19:32:02.548567+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 859 · 2026-05-22T19:32:02.549030+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 860 · 2026-05-22T19:32:03.303942+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1107
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-22T19:32:03.456527+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-22T19:32:03.456955+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 863 · 2026-05-22T19:32:03.808511+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 864 · 2026-05-22T19:32:04.316165+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool call

_source line 865 · 2026-05-22T19:32:04.316702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 866 · 2026-05-22T19:32:04.522186+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 205
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-22T19:32:05.027643+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1219
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-22T19:39:18.280590+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — Round 1 审稿报告\n\n**论文**: *The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation*\n**Venue**: EMNLP 2026 (ACL ARR)\n**审查侧重**: 方法严谨性 + 统计方法 + 实验设计\n\n---\n\n## Summary\n\n本文识别了 \"Likert Blindspot\" 现象：Likert 评分与 pairwise comparison 在检测 LLM judge 风格偏差时产生系统性分歧——BT 检测到显著偏好（BT > 60%, p < 0.001），而 Likert 的 Cohen's d → 0 且 p > 0.17。提出 CSD 框架（NLI-gated 内容控制 + per-axis 风格分解 + position-controlled pairwise comparison），在 4 个 judge + 1 个负控制 + 3 个 benchmark + 7 种统计方法下验证。GEE 条件分解揭示 per-axis 混淆结构差异。方法论整体扎实，核心发现在多重鲁棒性检验下稳健，但人工标注规模、TOST 等价阈值、方向不对称性处理等方面存在可改进空间。\n\n---\n\n## Strengths\n\n**S1. 核心发现新颖且实践意义重大。** Likert Blindspot 对 LLM 评估方法论有直接影响：大量论文使用 Likert 评分审计 LLM judge 偏差，本文表明这种方法可能系统性遗漏通过 pairwise 传播的风格偏好。Table 2 显示 7 种统计方法中 5 种 Likert-based 方法全部失败（p > 0.17–0.90），而两种 pairwise 方法均显著（BT p < 0.001, sign test p = 0.006），证据力强。\n\n**S2. 统计方法覆盖全面。** 7 种方法（BT, sign test, Likert ATE/t-test, Bayesian t, ordinal regression, GEE, Wilcoxon signed-rank）构成\"sensitivity hierarchy\"，从不同假设族独立验证同一结论。Holm-Bonferroni 校正覆盖 6 个主检验，且 §4.1 明确标注了 8 个检验全通过扩展族的结果。这种多方法三角验证在该领域论文中不常见。\n\n**S3. 负控制设计严谨。** Claude Sonnet 4 作为负控制（n = 87, BT 50.2%/54.1%, n.s.），TOST 等价检验确认 Δ = 15pp 处等价（76% power），验证了 CSD pipeline 不会凭空制造偏差。Appendix G 的形式化处理充分。\n\n**S4. GEE 条件分解贡献重大。** Table 3 的 Style OR vs. Originality OR 分离揭示了 per-axis 混淆结构差异（verbosity = style-dominated, formality = conditional effect, register = judge-dependent），这比简单的\"有/无偏差\"结论更有方法论价值。exchangeable working correlation + sandwich SE 的选择经 Appendix C 的 independence 对照验证（差异 <0.02），模型诊断充分。\n\n**S5. 鲁棒性检验链完整。** NLI 阈值敏感性分析（Appendix E, 11 个阈值 0.60–0.95），bootstrap 衰减分析（Appendix J, d → 0 across all n），rewriter 独立性检验（Appendix D, GPT-4o rewriter 替换），cross-axis 污染分析（Appendix R），功效分析（Figure 4），方向感知 NLI gate（Appendix F）。这些构成多层防御，使核心发现难以归因于单一方法论 artifact。\n\n**S6. 因果声明审慎。** §3.5 Design Rationale 明确免责：\"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\"。\"Controlled\" 限定为实验控制而非因果识别。Figure 2 的 DAG 标注 S → Q 虚线路径并讨论残余混淆。论文标题 \"Measurement-Mode Divergence\" 是中性表述。\n\n---\n\n## Weaknesses\n\n### Should-Fix\n\n**W1 [Should-Fix] 人工标注规模不足，inter-annotator agreement 偏低（§5.4, Appendix S）**\n- **位置**: §5.4 第一段，Appendix S\n- **问题**: 50 对 NLI-scored pairs，仅 2 名标注员，κ = 0.44（moderate agreement）。Annotator 1 precision = 93.6%，Annotator 2 = 84.3%（§5.4: \"CI [65.3%, 93.6%]\"），两者差距近 10pp。论文称 κ = 0.44 反映 \"calibrating a cohesion-difference rather than random noise\"，但 50 对样本无法可靠区分系统性分歧与噪声。Wilson CI 下界 86.3% 基于合并数据；若按标注员分开，Annotator 2 的下界会明显低于此值。\n- **为什么影响评分**: NLI gate 是 CSD 框架的核心假设保障组件——44% 拒绝率意味着大量数据依赖该 gate 的正确性。仅 50 对验证不足以支撑对该 gate 的信心，尤其是当两名标注员对 \"content preservation\" 的理解存在实质分歧（4 对 gate-rejected pairs 上的全部分歧集中在 verbosity-axis 的 subjective meaning 判断）。\n- **建议**: 增加标注规模至 ≥100 对，增加第 3 名标注员以计算 Fleiss' κ，并分析分歧案例的特征分布（是否集中在特定 axis/instruction type）。\n\n**W2 [Should-Fix] TOST 等价阈值 Δ = 15pp 与 GPT-4o 最小偏差重叠（§4.1, Limitations, Appendix G）**\n- **位置**: §4.1 脚注，Limitations 第 3 段，Appendix G\n- **问题**: TOST 设 Δ = 15pp（\"a judge that agrees with the style-manipulated version on ≥65% of pairs\"）。但 GPT-4o formality 的 BT = 63.0%（即 13pp above chance）——刚好在 Δ 之下。这意味着一个具有 10–14pp moderate bias 的 judge 会被 TOST 宣布为 \"equivalent to no bias\"。Claude 的实际 BT（50.2–54.1%）远低于此阈值，所以当前结论不受影响；但 Δ = 15pp 的选择依据不够充分——论文仅说 \"would alter benchmark rankings in typical n ≈ 500 evaluations\" 但未提供计算细节。\n- **为什么影响评分**: 负控制的可信度依赖 TOST 阈值的合理性。若 Δ 过大，可能遗漏 Claude 的 moderate bias。\n- **建议**: (1) 提供 Δ = 15pp 的定量推导（多大偏差会改变 benchmark ranking？用具体 benchmark 模拟）; (2) 增加 Δ 敏感性分析（Δ = 10pp, 12pp, 15pp, 20pp 下 TOST 结果如何变化）; (3) 在 Limitations 中明确 \"moderate bias (10–14pp) 可能逃脱检测\"。\n\n**W3 [Should-Fix] 方向不对称性对 Table 1 BT 估计的影响未充分讨论（Appendix A/H）**\n- **位置**: Appendix A（第 9 页底部），Appendix H（第 12 页），Table 1\n- **问题**: Formality 方向不对称显著：formal→casual 方向 judge 保留原文 88.9%，casual→formal 方向仅 52.6%（Appendix H）。这暗示 formality BT 估计中混合了真实风格偏好和 \"原文偏好 × 原文恰好是 formal\" 的混淆。Appendix A 的 GEE 控制原文偏好后 formality 仍显著（OR = 2.58, p = 0.032），但主文 Table 1 的 BT 数值（GPT-4o form: 63.0%）是未调整的聚合值。读者可能将 Table 1 的数值直接解读为 \"style preference magnitude\"，而实际上其中包含质量混淆。\n- **为什么影响评分**: Table 1 是论文的核心证据表，其数值的可解释性直接影响主 claim 的说服力。\n- **建议**: (1) 在 Table 1 或正文中添加脚注，提示 formality BT 包含方向不对称效应，指向 Appendix A 的调整分析; (2) 考虑在 Table 1 旁增加 GEE-adjusted style OR 对照列; (3) 在 §5.1 讨论中更明确地区分 \"BT detects real style preference\" 和 \"BT detects a mix of style + quality confounding that Likert attenuates\"。\n\n**W4 [Should-Fix] NLI gate 选择偏差检查覆盖面有限（§3.2, Appendix B）**\n- **位置**: §3.2, Appendix B\n- **问题**: 44% 拒绝率下，仅检查 4 个 surface covariates（word count, sentence count, TTR, FK grade）的 NLI-pass vs NLI-reject 分布。这些都是表面文本特征，未覆盖：(a) 语义/话题分布（某些 instruction types 是否被不成比例地过滤？），(b) 句法复杂度（parse tree depth），(c) 原始文本质量分布。Appendix E 的 NLI 阈值 sweep 显示 Blindspot 在所有阈值下持续——这是强鲁棒性证据，但不等同于选择偏差不存在。\n- **建议**: 增加 instruction type/topic 分布对比；或论证为何 4 个 surface covariates 足以排除选择偏差。\n\n**W5 [Should-Fix] Construct validity 讨论不充分（§5.1）**\n- **位置**: §5.1 \"Measurement attention vs. construct divergence\"\n- **问题**: 论文框架将 pairwise 定位为 \"检测到\" Likert \"遗漏的\" 偏差，隐含 pairwise 是更准确的测量。但 §5.1 自己承认 Likert 和 pairwise 可能测量不同 construct（absolute quality vs. comparative sensitivity）。如果 pairwise 的 forced-choice 设计人为放大微小风格差异为可测偏好（Comparative Trap, Jeong et al. 2025），而 Likert 正确反映了风格对绝对质量判断的可忽略影响，则两者都是\"正确的\"——只是对不同问题的回答。\n- **论文已有的辩护**（§5.1 末段, §6）：RLHF/DPO 使用 pairwise comparison，所以 pairwise-detected biases 是对 alignment pipeline 实际传播的偏差的正确测量。这个实践论证是有效的，但在正文中不够显式——目前主要在 Conclusion 的一句话中提及。\n- **建议**: 在 §5.1 中增加一段，明确区分 \"measurement sensitivity gap\"（同一 construct, pairwise 更灵敏）和 \"construct divergence\"（不同 construct, 各有效度），并论证为何在 RLHF 语境下前者更重要。\n\n### Minor\n\n**M1 [Minor] Cross-axis 污染超过自设阈值（Appendix R）**\n- Formality 改写产生 word count shift d = −0.23，超过论文自设 d < 0.20 的 \"negligible\" 标准。Appendix R 的 GEE covariate check（加入 word count 后 Style OR 变化 < 12%, p > .28）有效缓解了这一问题，但主文仅在 Appendix 引用中一笔带过（§5.4 倒数第二句引用 Appendix R），未明确承认阈值违反。建议在主文中添加一句明确说明并引导读者到 Appendix R 的缓解分析。\n\n**M2 [Minor] 100-point continuous Likert 仅用 Qwen3-32B（Appendix M）**\n- Qwen3-32B 同时担任 rewriter 和 100-point Likert judge，存在 evaluator-producer overlap。虽然这一 overlap 应偏向让 Likert 更容易检测偏差（judge 评价自己的改写），反而强化了 Blindspot 结论，但应在 Appendix M 中注明这一设计限制。\n\n**M3 [Minor] BT IIA 脚注简化过度（脚注 3）**\n- 脚注 3 声称 \"In binary-choice BT, IIA is structurally satisfied: each observation involves exactly two alternatives, so no third alternative can violate the axiom.\" 这在单次比较层面技术上正确，但 BT 模型跨 pairs 聚合时隐含的一维性假设（所有偏好可由单一潜在维度解释）未讨论。论文本身用 per-axis 分解证明偏好是多维的（Table 3），这与 BT 的一维假设存在张力——虽然每个 axis 分开建模缓解了问题。建议在脚注中补充一句关于一维性假设的说明。\n\n**M4 [Minor] Bootstrap CI 方法未指定**\n- Table 10（Appendix I）的 95% CI 基于 10,000 pair-level resamples，但未指定 percentile bootstrap 还是 BCa bootstrap。BT 概率在边界附近可能有偏度，BCa 更合适。\n\n**M5 [Minor] Table 2 的 GEE 与 Table 3 的 GEE 是不同模型**\n- Table 2 第 6 行 \"GEE (exchangeable)\" 以 Likert 评分为因变量，Table 3 以 pairwise 选择为因变量——两者性质完全不同。建议在 Table 2 标注 \"GEE (Likert-outcome)\" 以区分。\n\n---\n\n## Questions\n\n**Q1.** 对于 formality 方向不对称（88.9% vs 52.6%），是否考虑过分方向拟合 BT 模型（formal→casual 和 casual→formal 分开估计），而非聚合？分方向估计可以帮助区分真实风格偏好与原文质量混淆。\n\n**Q2.** NLI gate pass vs. reject 的 instruction type/topic 分布是否有系统差异？某些特定类型的 instruction（如创意写作 vs. 技术说明）是否被不成比例地过滤？\n\n**Q3.** Direction-aware NLI gate 恢复的 21 对（Appendix F）的 content quality 分布是否与 bidirectional-pass 对一致？这些恢复对是否集中在某一 axis？\n\n**Q4.** Table 2 的 GEE 与 Table 3 的 GEE 使用不同因变量（Likert score vs. pairwise choice）——能否在正文中明确区分？\n\n**Q5.** 是否考虑过使用 BCa bootstrap 而非 percentile bootstrap 计算 BT 置信区间？尤其对于 BT 估计接近 0.5 或接近 1 的情况。\n\n**Q6.** TOST Δ = 15pp 的定量依据是什么？\"would alter benchmark rankings\" 的具体模拟条件（benchmark size, number of models, score distribution）是否可以补充？\n\n---\n\n## Missing References\n\n无必须添加的遗漏引用。以下为可选增强引用：\n- **Measurement invariance**: Millsap (2011), *Statistical Approaches to Measurement Invariance* — 可强化 \"measurement-mode divergence\" 的心理测量学理论基础\n- **BT model diagnostics**: Cattelan (2012), *Models for Paired Comparison Data: A Review with Emphasis on Dependent Data* — 可补充 BT 模型假设讨论\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5 / 5 | 主 claim 有多方法、多 judge、负控制支撑，统计方法选择合理且经鲁棒性检验。但人工标注规模（50 对, κ=0.44）不足以充分验证 NLI gate，TOST Δ=15pp 与最小观测偏差重叠，方向不对称对 Table 1 估计的影响在主文中讨论不足。 |\n| **Excitement** | 3.5 / 5 | Likert Blindspot 对 LLM 评估方法论有直接实践影响——用 Likert 审计 judge 风格偏差的论文需重新审视结论。但范围限于 LLM judge 风格偏差检测，对更广泛 NLP 社区影响有限。 |\n| **Reproducibility** | 4 / 5 | §P（Appendix P）提供完整实现细节（模型、API 版本、温度、NLI 阈值）。代码和数据承诺接收后公开。统计方法描述足够复现。 |\n| **Confidence** | 4 / 5 | 统计方法和实验设计是我的核心审查方向，对 BT/GEE/TOST 方法论有充分把握。对 NLI gate 的 NLP 评估有合理理解。 |\n\n---\n\n## 总体评分\n\n**Overall**: **3.5** — Borderline Conference\n\n**一句话总结**: 核心发现新颖且证据充分（7 种方法 × 4 judges × 3 benchmarks 三角验证），但人工标注规模不足（50 对, κ=0.44）、TOST 等价阈值与最小观测偏差重叠（Δ=15pp vs. 13pp）、以及 construct validity 讨论的不完整性，使评分停留在 Borderline Conference——若 should-fix 问题得到解决（尤其 W1 和 W5），可以上调至 Conference (4.0)。\n\n---\n\n## 格式合规\n\n- **正文页数**: 合规。§1–§6（Conclusion）结束于第 8 页上半部分，Limitations 从第 8 页下半部开始延续至第 9 页——Limitations 不计入 8 页限制。✓\n- **Double-blind**: 合规。首页标注 \"Anonymous ACL submission\"，无作者信息、致谢或可识别 URL 泄露。✓\n- **Limitations**: 合规。覆盖 quality-style confounding and construct validity、evaluator-producer bias、scope and ecological validity 三个维度，简洁且未包含新实验结果。✓\n- **参考文献**: 格式规范，无明显遗漏。✓\n",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — Round 1 审稿报告\n\n**论文**: *The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation*\n**Venue**: EMNLP 2026 (ACL ARR)\n**审查侧重**: 方法严谨性 + 统计方法 + 实验设计\n\n---\n\n## Summary\n\n本文识别了 \"Likert Blindspot\" 现象：Likert 评分与 pairwise comparison 在检测 LLM judge 风格偏差时产生系统性分歧——BT 检测到显著偏好（BT > 60%, p < 0.001），而 Likert 的 Cohen's d → 0 且 p > 0.17。提出 CSD 框架（NLI-gated 内容控制 + per-axis 风格分解 + position-controlled pairwise comparison），在 4 个 judge + 1 个负控制 + 3 个 benchmark + 7 种统计方法下验证。GEE 条件分解揭示 per-axis 混淆结构差异。方法论整体扎实，核心发现在多重鲁棒性检验下稳健，但人工标注规模、TOST 等价阈值、方向不对称性处理等方面存在可改进空间。\n\n---\n\n## Strengths\n\n**S1. 核心发现新颖且实践意义重大。** Likert Blindspot 对 LLM 评估方法论有直接影响：大量论文使用 Likert 评分审计 LLM judge 偏差，本文表明这种方法可能系统性遗漏通过 pairwise 传播的风格偏好。Table 2 显示 7 种统计方法中 5 种 Likert-based 方法全部失败（p > 0.17–0.90），而两种 pairwise 方法均显著（BT p < 0.001, sign test p = 0.006），证据力强。\n\n**S2. 统计方法覆盖全面。** 7 种方法（BT, sign test, Likert ATE/t-test, Bayesian t, ordinal regression, GEE, Wilcoxon signed-rank）构成\"sensitivity hierarchy\"，从不同假设族独立验证同一结论。Holm-Bonferroni 校正覆盖 6 个主检验，且 §4.1 明确标注了 8 个检验全通过扩展族的结果。这种多方法三角验证在该领域论文中不常见。\n\n**S3. 负控制设计严谨。** Claude Sonnet 4 作为负控制（n = 87, BT 50.2%/54.1%, n.s.），TOST 等价检验确认 Δ = 15pp 处等价（76% power），验证了 CSD pipeline 不会凭空制造偏差。Appendix G 的形式化处理充分。\n\n**S4. GEE 条件分解贡献重大。** Table 3 的 Style OR vs. Originality OR 分离揭示了 per-axis 混淆结构差异（verbosity = style-dominated, formality = conditional effect, register = judge-dependent），这比简单的\"有/无偏差\"结论更有方法论价值。exchangeable working correlation + sandwich SE 的选择经 Appendix C 的 independence 对照验证（差异 <0.02），模型诊断充分。\n\n**S5. 鲁棒性检验链完整。** NLI 阈值敏感性分析（Appendix E, 11 个阈值 0.60–0.95），bootstrap 衰减分析（Appendix J, d → 0 across all n），rewriter 独立性检验（Appendix D, GPT-4o rewriter 替换），cross-axis 污染分析（Appendix R），功效分析（Figure 4），方向感知 NLI gate（Appendix F）。这些构成多层防御，使核心发现难以归因于单一方法论 artifact。\n\n**S6. 因果声明审慎。** §3.5 Design Rationale 明确免责：\"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\"。\"Controlled\" 限定为实验控制而非因果识别。Figure 2 的 DAG 标注 S → Q 虚线路径并讨论残余混淆。论文标题 \"Measurement-Mode Divergence\" 是中性表述。\n\n---\n\n## Weaknesses\n\n### Should-Fix\n\n**W1 [Should-Fix] 人工标注规模不足，inter-annotator agreement 偏低（§5.4, Appendix S）**\n- **位置**: §5.4 第一段，Appendix S\n- **问题**: 50 对 NLI-scored pairs，仅 2 名标注员，κ = 0.44（moderate agreement）。Annotator 1 precision = 93.6%，Annotator 2 = 84.3%（§5.4: \"CI [65.3%, 93.6%]\"），两者差距近 10pp。论文称 κ = 0.44 反映 \"calibrating a cohesion-difference rather than random noise\"，但 50 对样本无法可靠区分系统性分歧与噪声。Wilson CI 下界 86.3% 基于合并数据；若按标注员分开，Annotator 2 的下界会明显低于此值。\n- **为什么影响评分**: NLI gate 是 CSD 框架的核心假设保障组件——44% 拒绝率意味着大量数据依赖该 gate 的正确性。仅 50 对验证不足以支撑对该 gate 的信心，尤其是当两名标注员对 \"content preservation\" 的理解存在实质分歧（4 对 gate-rejected pairs 上的全部分歧集中在 verbosity-axis 的 subjective meaning 判断）。\n- **建议**: 增加标注规模至 ≥100 对，增加第 3 名标注员以计算 Fleiss' κ，并分析分歧案例的特征分布（是否集中在特定 axis/instruction type）。\n\n**W2 [Should-Fix] TOST 等价阈值 Δ = 15pp 与 GPT-4o 最小偏差重叠（§4.1, Limitations, Appendix G）**\n- **位置**: §4.1 脚注，Limitations 第 3 段，Appendix G\n- **问题**: TOST 设 Δ = 15pp（\"a judge that agrees with the style-manipulated version on ≥65% of pairs\"）。但 GPT-4o formality 的 BT = 63.0%（即 13pp above chance）——刚好在 Δ 之下。这意味着一个具有 10–14pp moderate bias 的 judge 会被 TOST 宣布为 \"equivalent to no bias\"。Claude 的实际 BT（50.2–54.1%）远低于此阈值，所以当前结论不受影响；但 Δ = 15pp 的选择依据不够充分——论文仅说 \"would alter benchmark rankings in typical n ≈ 500 evaluations\" 但未提供计算细节。\n- **为什么影响评分**: 负控制的可信度依赖 TOST 阈值的合理性。若 Δ 过大，可能遗漏 Claude 的 moderate bias。\n- **建议**: (1) 提供 Δ = 15pp 的定量推导（多大偏差会改变 benchmark ranking？用具体 benchmark 模拟）; (2) 增加 Δ 敏感性分析（Δ = 10pp, 12pp, 15pp, 20pp 下 TOST 结果如何变化）; (3) 在 Limitations 中明确 \"moderate bias (10–14pp) 可能逃脱检测\"。\n\n**W3 [Should-Fix] 方向不对称性对 Table 1 BT 估计的影响未充分讨论（Appendix A/H）**\n- **位置**: Appendix A（第 9 页底部），Appendix H（第 12 页），Table 1\n- **问题**: Formality 方向不对称显著：formal→casual 方向 judge 保留原文 88.9%，casual→formal 方向仅 52.6%（Appendix H）。这暗示 formality BT 估计中混合了真实风格偏好和 \"原文偏好 × 原文恰好是 formal\" 的混淆。Appendix A 的 GEE 控制原文偏好后 formality 仍显著（OR = 2.58, p = 0.032），但主文 Table 1 的 BT 数值（GPT-4o form: 63.0%）是未调整的聚合值。读者可能将 Table 1 的数值直接解读为 \"style preference magnitude\"，而实际上其中包含质量混淆。\n- **为什么影响评分**: Table 1 是论文的核心证据表，其数值的可解释性直接影响主 claim 的说服力。\n- **建议**: (1) 在 Table 1 或正文中添加脚注，提示 formality BT 包含方向不对称效应，指向 Appendix A 的调整分析; (2) 考虑在 Table 1 旁增加 GEE-adjusted style OR 对照列; (3) 在 §5.1 讨论中更明确地区分 \"BT detects real style preference\" 和 \"BT detects a mix of style + quality confounding that Likert attenuates\"。\n\n**W4 [Should-Fix] NLI gate 选择偏差检查覆盖面有限（§3.2, Appendix B）**\n- **位置**: §3.2, Appendix B\n- **问题**: 44% 拒绝率下，仅检查 4 个 surface covariates（word count, sentence count, TTR, FK grade）的 NLI-pass vs NLI-reject 分布。这些都是表面文本特征，未覆盖：(a) 语义/话题分布（某些 instruction types 是否被不成比例地过滤？），(b) 句法复杂度（parse tree depth），(c) 原始文本质量分布。Appendix E 的 NLI 阈值 sweep 显示 Blindspot 在所有阈值下持续——这是强鲁棒性证据，但不等同于选择偏差不存在。\n- **建议**: 增加 instruction type/topic 分布对比；或论证为何 4 个 surface covariates 足以排除选择偏差。\n\n**W5 [Should-Fix] Construct validity 讨论不充分（§5.1）**\n- **位置**: §5.1 \"Measurement attention vs. construct divergence\"\n- **问题**: 论文框架将 pairwise 定位为 \"检测到\" Likert \"遗漏的\" 偏差，隐含 pairwise 是更准确的测量。但 §5.1 自己承认 Likert 和 pairwise 可能测量不同 construct（absolute quality vs. comparative sensitivity）。如果 pairwise 的 forced-choice 设计人为放大微小风格差异为可测偏好（Comparative Trap, Jeong et al. 2025），而 Likert 正确反映了风格对绝对质量判断的可忽略影响，则两者都是\"正确的\"——只是对不同问题的回答。\n- **论文已有的辩护**（§5.1 末段, §6）：RLHF/DPO 使用 pairwise comparison，所以 pairwise-detected biases 是对 alignment pipeline 实际传播的偏差的正确测量。这个实践论证是有效的，但在正文中不够显式——目前主要在 Conclusion 的一句话中提及。\n- **建议**: 在 §5.1 中增加一段，明确区分 \"measurement sensitivity gap\"（同一 construct, pairwise 更灵敏）和 \"construct divergence\"（不同 construct, 各有效度），并论证为何在 RLHF 语境下前者更重要。\n\n### Minor\n\n**M1 [Minor] Cross-axis 污染超过自设阈值（Appendix R）**\n- Formality 改写产生 word count shift d = −0.23，超过论文自设 d < 0.20 的 \"negligible\" 标准。Appendix R 的 GEE covariate check（加入 word count 后 Style OR 变化 < 12%, p > .28）有效缓解了这一问题，但主文仅在 Appendix 引用中一笔带过（§5.4 倒数第二句引用 Appendix R），未明确承认阈值违反。建议在主文中添加一句明确说明并引导读者到 Appendix R 的缓解分析。\n\n**M2 [Minor] 100-point continuous Likert 仅用 Qwen3-32B（Appendix M）**\n- Qwen3-32B 同时担任 rewriter 和 100-point Likert judge，存在 evaluator-producer overlap。虽然这一 overlap 应偏向让 Likert 更容易检测偏差（judge 评价自己的改写），反而强化了 Blindspot 结论，但应在 Appendix M 中注明这一设计限制。\n\n**M3 [Minor] BT IIA 脚注简化过度（脚注 3）**\n- 脚注 3 声称 \"In binary-choice BT, IIA is structurally satisfied: each observation involves exactly two alternatives, so no third alternative can violate the axiom.\" 这在单次比较层面技术上正确，但 BT 模型跨 pairs 聚合时隐含的一维性假设（所有偏好可由单一潜在维度解释）未讨论。论文本身用 per-axis 分解证明偏好是多维的（Table 3），这与 BT 的一维假设存在张力——虽然每个 axis 分开建模缓解了问题。建议在脚注中补充一句关于一维性假设的说明。\n\n**M4 [Minor] Bootstrap CI 方法未指定**\n- Table 10（Appendix I）的 95% CI 基于 10,000 pair-level resamples，但未指定 percentile bootstrap 还是 BCa bootstrap。BT 概率在边界附近可能有偏度，BCa 更合适。\n\n**M5 [Minor] Table 2 的 GEE 与 Table 3 的 GEE 是不同模型**\n- Table 2 第 6 行 \"GEE (exchangeable)\" 以 Likert 评分为因变量，Table 3 以 pairwise 选择为因变量——两者性质完全不同。建议在 Table 2 标注 \"GEE (Likert-outcome)\" 以区分。\n\n---\n\n## Questions\n\n**Q1.** 对于 formality 方向不对称（88.9% vs 52.6%），是否考虑过分方向拟合 BT 模型（formal→casual 和 casual→formal 分开估计），而非聚合？分方向估计可以帮助区分真实风格偏好与原文质量混淆。\n\n**Q2.** NLI gate pass vs. reject 的 instruction type/topic 分布是否有系统差异？某些特定类型的 instruction（如创意写作 vs. 技术说明）是否被不成比例地过滤？\n\n**Q3.** Direction-aware NLI gate 恢复的 21 对（Appendix F）的 content quality 分布是否与 bidirectional-pass 对一致？这些恢复对是否集中在某一 axis？\n\n**Q4.** Table 2 的 GEE 与 Table 3 的 GEE 使用不同因变量（Likert score vs. pairwise choice）——能否在正文中明确区分？\n\n**Q5.** 是否考虑过使用 BCa bootstrap 而非 percentile bootstrap 计算 BT 置信区间？尤其对于 BT 估计接近 0.5 或接近 1 的情况。\n\n**Q6.** TOST Δ = 15pp 的定量依据是什么？\"would alter benchmark rankings\" 的具体模拟条件（benchmark size, number of models, score distribution）是否可以补充？\n\n---\n\n## Missing References\n\n无必须添加的遗漏引用。以下为可选增强引用：\n- **Measurement invariance**: Millsap (2011), *Statistical Approaches to Measurement Invariance* — 可强化 \"measurement-mode divergence\" 的心理测量学理论基础\n- **BT model diagnostics**: Cattelan (2012), *Models for Paired Comparison Data: A Review with Emphasis on Dependent Data* — 可补充 BT 模型假设讨论\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5 / 5 | 主 claim 有多方法、多 judge、负控制支撑，统计方法选择合理且经鲁棒性检验。但人工标注规模（50 对, κ=0.44）不足以充分验证 NLI gate，TOST Δ=15pp 与最小观测偏差重叠，方向不对称对 Table 1 估计的影响在主文中讨论不足。 |\n| **Excitement** | 3.5 / 5 | Likert Blindspot 对 LLM 评估方法论有直接实践影响——用 Likert 审计 judge 风格偏差的论文需重新审视结论。但范围限于 LLM judge 风格偏差检测，对更广泛 NLP 社区影响有限。 |\n| **Reproducibility** | 4 / 5 | §P（Appendix P）提供完整实现细节（模型、API 版本、温度、NLI 阈值）。代码和数据承诺接收后公开。统计方法描述足够复现。 |\n| **Confidence** | 4 / 5 | 统计方法和实验设计是我的核心审查方向，对 BT/GEE/TOST 方法论有充分把握。对 NLI gate 的 NLP 评估有合理理解。 |\n\n---\n\n## 总体评分\n\n**Overall**: **3.5** — Borderline Conference\n\n**一句话总结**: 核心发现新颖且证据充分（7 种方法 × 4 judges × 3 benchmarks 三角验证），但人工标注规模不足（50 对, κ=0.44）、TOST 等价阈值与最小观测偏差重叠（Δ=15pp vs. 13pp）、以及 construct validity 讨论的不完整性，使评分停留在 Borderline Conference——若 should-fix 问题得到解决（尤其 W1 和 W5），可以上调至 Conference (4.0)。\n\n---\n\n## 格式合规\n\n- **正文页数**: 合规。§1–§6（Conclusion）结束于第 8 页上半部分，Limitations 从第 8 页下半部开始延续至第 9 页——Limitations 不计入 8 页限制。✓\n- **Double-blind**: 合规。首页标注 \"Anonymous ACL submission\"，无作者信息、致谢或可识别 URL 泄露。✓\n- **Limitations**: 合规。覆盖 quality-style confounding and construct validity、evaluator-producer bias、scope and ecological validity 三个维度，简洁且未包含新实验结果。✓\n- **参考文献**: 格式规范，无明显遗漏。✓\n",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-22T19:39:22.152612+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3872
}
```

</details>

---


### Assistant

_source line 870 · 2026-05-22T19:39:34.216097+00:00_

审稿报告已提交给 Review Director。

总结：

- **Overall: 3.5 (Borderline Conference)**
- 核心 Likert Blindspot 发现证据充分（7 种统计方法 × 4 judges × 3 benchmarks 交叉验证，负控制设计严谨），GEE 条件分解的 per-axis 混淆结构分析具有方法论贡献
- 5 个 Should-Fix 问题：(1) 人工标注仅 50 对且 κ=0.44；(2) TOST Δ=15pp 与 GPT-4o 最小偏差 13pp 重叠；(3) formality 方向不对称（88.9% vs 52.6%）对 Table 1 未调整 BT 的影响讨论不足；(4) NLI gate 44% 拒绝率下仅 4 个 surface covariate 检查；(5) construct validity 讨论中 pairwise 为何优于 Likert 的实践论证不够显式
- 5 个 Minor 问题：cross-axis 污染超阈值、100-point Likert 的 evaluator-producer overlap、BT IIA 脚注过度简化、bootstrap CI 类型未指定、Table 2 vs Table 3 的 GEE 模型区分不清

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 28

## Round 28

4 recorded events


### User

_source line 871 · 2026-05-22T19:40:56.583278+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Must-Fix、Should-Fix 和主要 Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。

---

# Reviewer 2 审稿报告（Round 1）

## 总体评分
**Overall**: 3.0 (Findings)

## 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验控制周密（NLI gate、position control、7 种统计方法、GEE 分解），但 framing 不对称——无法充分区分 "Likert misses real signal" vs "pairwise amplifies micro-preferences"；单一负控制不足以支撑架构特异性声明 |
| Excitement | 3/5 | 对 LLM judge 审计实践有直接价值，但核心洞察对熟悉心理测量学的读者不意外；GEE per-axis 分解有趣但应用场景窄 |
| Novelty | 3/5 | 核心发现是 established knowledge 的 domain transfer；CSD + GEE 分解是增量贡献 |
| Overall | 3.0 | Findings 水平——方法学扎实但新颖性有限且 framing 问题需修正 |

## Strengths

**S1. 实验控制层次感出色。** CSD 三层控制——NLI gate (§3.2)、same-style double-rewrite (§5.4)、position swapping (§3.3)——在 LLM judge 风格偏差文献中属最周密的实验设计之一。

**S2. 统计方法多元互补。** 七种方法覆盖不同假设，Table 2 sensitivity hierarchy 清晰展示 Likert-based 方法一致失败。GEE 条件分解 (Table 3) 将 style OR 与 originality OR 分离是独立的方法论贡献。

**S3. Robustness 检查详尽。** §5.4 六项 amplification controls + Appendices A-S 大量补充分析（bootstrap CI、formal power analysis、100-point continuous Likert、cross-axis contamination 等）。

**S4. GEE per-axis confound 分解是真正的增量贡献。** Table 3 揭示 verbosity style-dominated (Style OR 8-15) vs formality conditional 的结构性差异。

**S5. 跨 judge 覆盖合理。** 4 target judges + 1 negative control 覆盖主流架构。

## Must-Fix 问题

**N1** [critical] **标题与 framing 隐式预设 pairwise 为 ground truth**
- 位置：Title、Abstract ("signal loss exceeding 60%")、§6 ("Likert-only audits miss style-driven preferences")
- "The Likert Blindspot" 将 Likert 定位为"盲区"，但论文自身在 §5.4 引用 Jeong et al. (2025) Comparative Trap 承认 pairwise 可能放大偏好，Limitations 提出 construct divergence 解释。这些 caveat 被隔离在末尾，未进入标题/摘要/结论。在缺乏外部 ground truth 的情况下，无法区分 measurement attenuation vs format amplification vs construct divergence 三种解释，但叙事 90% 倾向第一种。
- 建议：标题改为中性（如直接用副标题）；Abstract/Conclusion 给三种解释同等权重。

**N2** [critical] **新颖性定位模糊**
- 位置：§1、§6（"identifies"/"demonstrates"）
- Likert vs pairwise 灵敏度差异是 Thurstone (1927) 以来的经典结论。论文真正贡献是"首次受控量化 + GEE 分解方法"，但措辞有时像是声称发现了现象本身。
- 建议：§1 明确声明 "sensitivity gap is well-established; our contribution is first controlled quantification + decomposition methodology"。

**N3** [critical] **单一负控制不足以支撑架构特异性声明**
- 位置：§5.3、§6、Limitations
- Claude Sonnet 4 是唯一负控制。论文未探讨为何 Claude 不受影响（RLHF 差异？评估策略？），也未测试同系列其他模型。可能 Claude 只是整体风格不敏感而非"正确地不受影响"。
- 建议：讨论可能机制；降格为 "one model does not show this pattern"。

## Should-Fix 问题

**W1** [warning] **主实验仅用 LLMBar (n=100)，cross-benchmark 覆盖稀疏** — Table 2 的 AlpacaEval/MT-Bench 仅测试 formality pairwise，不足以支撑 "across three benchmarks" 泛化声明。

**W2** [warning] **Register 轴 evaluator-producer overlap 最严重，结果应降级** — Qwen3-32B 同时作为 rewriter 和 judge，BT 仅 51.4%。应标注为 exploratory。

**W3** [warning] **Abstract 数字密度过高** — ~200 词中堆砌过多数字和术语，影响核心信息传达。

**W4** [warning] **Introduction motivating example 未 acknowledge formality-quality nuance** — GPT-4o 偏好 formal 的例子暗示 Likert 偏好 casual 是"错误"的，但直到 Limitations/Appendix A 才讨论 formality 可能反映真实 quality 差异。

**W5** [warning] **"Framework" 设定过高预期** — CSD 更准确地说是 experimental protocol，3 个成功轴 + 1 个失败轴不足以支撑 "framework" 级别声明。

## 小问题
- §3-4 脚注密度高，打断阅读流
- Figure 2 (DAG) 偏小，blocked/open paths 区分不够直观
- Tone axis 失败值得 2-3 句更详细的分析
- §5.2 GEE 术语首次出现时缺乏直觉解释
- References 置于 Appendices 之后（非标准顺序）

## Questions

**Q1.** 六项 amplification controls 中哪一项最直接排除 "pairwise amplifies micro-preferences" 解释？无人类 ground truth 如何区分 attenuation vs amplification？

**Q2.** Claude 不表现 Blindspot 的可能机制？是否检查过 Claude 的 Likert/pairwise 评分分布（ceiling/floor effects, tie rates）？

**Q3.** 如果用更大 benchmark (n>1000)，Likert Type II error 是否因功效提升而缩小？Appendix K 报告 required n >1200——Blindspot 是否部分是 power issue？

**Q4.** Register 轴是否做了 rewriter 替换测试（类似 Appendix D 对 verbosity/formality 的测试）？

**Q5.** Tone axis NLI gate 通过率 56%——失败案例中 NLI 判定"内容改变"是正确的还是误判？

## Missing References
无重大遗漏。可考虑补充 Bai et al. (2022/2023) RLHF preference model 的 comparison vs rating 差异、Rafailov et al. (2023) DPO 中 pairwise preference 的理论性质。

## 格式检查
- ✅ 正文 ≤8 页合规
- ✅ Double-blind 合规
- ✅ Limitations 覆盖充分、长度适中
- ✅ Appendix A-S 组织合理
- ⚠️ References 置于 Appendices 之后（非标准）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-22T19:44:17.231885+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — 交叉回应 Reviewer 2 审稿意见\n\n---\n\n## Must-Fix 逐条回应\n\n### [AGREE] R2-N1: 标题与 framing 隐式预设 pairwise 为 ground truth\n**同意存在问题，但不同意 severity 为 Must-Fix，应为 Should-Fix。**\n\nR2 的核心观察是正确的：论文叙事重心偏向 \"Likert misses real signal\"，而 §5.1 的 construct divergence 讨论和 Limitations 的 Comparative Trap 引用被隔离在末尾。我在自己的审稿中也提出了类似问题（我的 W5: construct validity 讨论不充分）。\n\n但 R2 将此升级为 Must-Fix 过重，原因如下：\n1. **论文标题 \"Measurement-Mode Divergence\" 副标题本身是中性的**——\"Blindspot\" 是主标题的隐喻，但副标题准确描述了现象。\n2. **§5.1 已明确讨论三种解释**：\"Both Likert and pairwise may be 'correct' for their respective constructs\"（§5.1 倒数第三段），引用 Tripathi et al. (2025) 独立确认 construct divergence。问题是权重分配不均，而非完全缺失。\n3. **实践论证是有效的**：RLHF/DPO 使用 pairwise comparison，因此 pairwise-detected biases 是对 alignment pipeline 实际传播偏差的正确度量——这个论点在 §1 和 §6 均有涉及（\"Likert-only audits miss style-driven preferences that propagate through pairwise-based alignment pipelines\"），只是不够显式。\n\n**建议折中**：不必改标题（\"Blindspot\" 是有效的注意力锚点），但 Abstract 和 §6 应给 construct divergence 解释 1-2 句同等权重的空间。\n\n---\n\n### [REBUT] R2-N2: 新颖性定位模糊\n**不同意此为 Must-Fix。论文已在 §1 明确界定了贡献边界。**\n\nR2 称 \"Likert vs pairwise 灵敏度差异是 Thurstone (1927) 以来的经典结论\"——这在一般心理测量学层面成立，但在 LLM judge 风格偏差的特定语境中，**此前无受控实验量化过这一差异**。论文 §1 第 2 页明确声明：\n\n> \"Our contribution is the first controlled quantification of this per-axis sensitivity gap in the LLM judge setting; identifying the two-layer mechanism the inflation plus residual signal attenuation that drives it.\"\n\n> \"we previously sequentially conjectured for LLM judges\"（§2 末段，引用 Koh et al. 2025 作为先前猜测）\n\n论文区分了三层贡献：(1) 受控量化（vs. 先前的 observational 报告），(2) CSD 方法论（NLI gate + per-axis decomposition），(3) GEE 条件分解揭示 per-axis 混淆结构。R2 将 (3) 评价为 \"真正的增量贡献\"（R2-S4），却又在 N2 中称整体贡献为 \"domain transfer\"——这两个判断相互矛盾。\n\nR2 举 Thurstone (1927) 为前序工作，但 Thurstone 的 Law of Comparative Judgment 讨论的是心理物理学中刺激量级判断，与 LLM judge 在 NLG evaluation 中的风格偏好检测是不同 task。将\"一般性测量理论预测\"等同于\"特定领域的受控实验验证\"，忽视了 empirical science 中领域验证的价值。\n\n**结论**：论文措辞可局部收紧（如 §1 \"This is the Likert Blindspot\" 可改为 \"We term this the Likert Blindspot\"），但 N2 不构成 Must-Fix——因为贡献界定已在 §1 完成。\n\n---\n\n### [REBUT] R2-N3: 单一负控制不足以支撑架构特异性声明\n**不同意此为 Must-Fix。R2 对论文 claim 的解读超出了论文实际声明。**\n\n论文使用 Claude Sonnet 4 的目的是 **pipeline validation**（CSD 不会凭空制造偏差），**不是** architecture comparison。关键文本证据：\n\n- §4.1: \"Claude Sonnet 4 serves as confirmatory replication and is excluded from FWER control; as a sanity check, all eight tests remain significant under the expanded family.\"\n- §5.3: \"A negative control judge shows no divergence on either primary axis, supporting discriminative validity.\"\n- §6: \"including a negative control judge showing no pairwise divergence\"\n\n论文从未声明 \"only certain architectures show the Blindspot\" 或 \"the Blindspot is architecture-specific\"。Claude 的作用是证明 **CSD 具有 discriminative validity**——当真实偏差不存在时，pipeline 不报假阳性。这与 \"探讨为何 Claude 不受影响\" 是完全不同的研究问题。\n\nR2 要求 \"讨论可能机制\" 和 \"测试同系列其他模型\"——这是要求论文回答一个它未提出的问题。将此升级为 Must-Fix 要求论文做超出其 scope 的工作。\n\n**补充证据**：Appendix D（rewriter independence test）用 GPT-4o 替换 Qwen3-32B 作为 rewriter，Blindspot 持续存在——这进一步表明 Blindspot 不依赖特定 evaluator-producer 组合，是 pipeline 鲁棒性而非架构特异性的证据。\n\n**结论**：R2 的关切可以通过在 Limitations 增加 1-2 句（\"the mechanism behind Claude's null result remains unexplored\"）解决，不构成 Must-Fix。\n\n---\n\n## Should-Fix 逐条回应\n\n### [AGREE] R2-W1: 主实验仅用 LLMBar, cross-benchmark 覆盖稀疏\n**部分同意。**\n\nTable 1 的 AlpacaEval 和 MT-Bench 确实仅覆盖 formality + verbosity 的部分 judge 组合。\"across three benchmarks\" 的泛化声明需要限定。\n\n但须注意两点缓解因素：\n1. AlpacaEval 的 scaled replication (n = 355) 是独立的大样本验证，且 Appendix K（formal power analysis）和 Appendix J（bootstrap attenuation）均基于此样本。\n2. §5.3 的 cross-judge 和 cross-axis replication 在 LLMBar 内部已用 4 个 judge × 3 个 axis = 12 个 cell 验证，8/11 显著（Table 1）。\n\n建议将 \"across three benchmarks\" 限定为 \"with primary results on LLMBar and confirmatory replication on AlpacaEval and MT-Bench for selected configurations\"。\n\n---\n\n### [AGREE] R2-W2: Register 轴 evaluator-producer overlap\n**部分同意。** Qwen3-32B 作为 rewriter + judge 的 overlap 应在论文中标注。我在自己的 M2 中也提出了类似问题（Appendix M 的 100-point Likert 用 Qwen3-32B）。\n\n但须注意：register 的主要 Blindspot 结果来自 **其他 judge**（GPT-4o register n.s., Llama-70B register 63.1% BT significant——Table 1），这些 judge 与 rewriter 无 overlap。论文的核心 claim 建立在 verbosity 和 formality 上，register 是补充。\"降级为 exploratory\" 过强，标注 overlap 即可。\n\n---\n\n### [REBUT] R2-W3: Abstract 数字密度过高\n**不同意。** 对于一篇以 \"7 种统计方法 × 4 judges × 3 benchmarks\" 为核心卖点的实证论文，Abstract 中的定量具体性（BT > 60%, p < 0.001; d → 0, p > 0.17）是必要的——它精确传达了 Blindspot 的 magnitude 和统计证据强度。去除这些数字会使 Abstract 变为无法验证的 qualitative assertion。\n\nARR reviewer guidelines 未对 Abstract 数字密度设限。Empirical NLP 论文（如 Wang et al. 2024 Chatbot Arena, Zheng et al. 2023 MT-Bench）的 Abstract 同样包含定量结果。\n\n---\n\n### [AGREE] R2-W4: Introduction motivating example 未 acknowledge formality-quality nuance\n**同意，minor 级别修正即可。** §1 开头的 GPT-4o 例子（Likert 评 casual 为 8, formal 为 5，但 pairwise 一致选 formal）确实隐含了 \"Likert 的判断是错误的\"，而 formality 与 perceived quality 的关联直到 Appendix A 才讨论。在例子后添加一句 caveat（\"whether this reflects a genuine quality difference or a stylistic preference is itself a question we address in §5.1\"）即可解决。\n\n---\n\n### [REBUT] R2-W5: \"Framework\" 设定过高预期\n**不同意。** \"Framework\" 在 NLP 文献中常用于描述 multi-stage experimental protocols（例如 RATE: Reber et al. 2025 称自己为 \"framework\"；Chatbot Arena 称自己为 \"platform\"/\"framework\"）。CSD 包含三个独立组件（NLI gate, per-axis decomposition, position-controlled pairwise），每个组件可独立复用——这是 framework 而非 one-off protocol 的定义特征。\n\n3 个成功轴 + 1 个失败轴（tone）恰恰证明 framework 有 discriminative validity：它不是对所有输入都报阳性的 trivial pipeline。\n\n---\n\n## Questions 回应\n\n### R2-Q1: 哪项 amplification control 最直接排除 \"pairwise amplifies micro-preferences\"？\n\n这是好问题。最直接的证据组合：\n1. **负控制（Claude）**：如果 pairwise 系统性放大微偏好，Claude 也应显示 inflated BT。Claude BT ≈ 50%（Table 1）证明 pairwise 不 uniformly amplify。\n2. **Same-style double-rewrite control（§5.4, Appendix O）**：original vs. same-style rewrite 的 BT 被 GEE originality term 吸收，证明 rewriting artifact ≠ style signal。\n3. **Rewriter independence（Appendix D）**：GPT-4o rewriter 替换后 Blindspot 持续——排除了 Qwen3-32B rewriter 特有的 style 注入。\n\n但 R2 的核心问题——\"无人类 ground truth 如何区分 attenuation vs amplification\"——确实没有被完全回答。论文 §5.1 承认这一点。我同意这是论文的 inherent limitation，但不是 paper-breaking 问题，因为实践论证（RLHF 用 pairwise → pairwise-detected biases 实际传播）提供了 pragmatic ground truth。\n\n### R2-Q2: Claude 机制？\n同意这是开放问题。我在自己的审稿中未专门提出，但认为在 Limitations 增加 1-2 句讨论（可能与 Claude 的 RLHF 训练策略或内部评估策略有关）是合理的。\n\n### [REBUT] R2-Q3: 大样本下 Likert Type II error 是否因功效提升而缩小？\n**论文已明确回答此问题。** R2 似乎未充分考虑 Appendix J 和 K 的证据：\n\n- **Appendix J（Bootstrap Attenuation Analysis）**：subsample BT 在所有样本量下稳定在 BT 76-77%（p < 0.001），而 Likert d 随 n 增大 **converges to zero**——不是 converge to a small nonzero value，是趋向零（Table 11: d remains flat near zero across sample sizes while BT is stable at 66.5%）。这直接证明 Blindspot 是 structural measurement difference，不是 power issue。\n- **Appendix K（Formal Power Analysis）**: 对于 Likert 达到 80% power 所需 n > 1,200（Qwen3-32B verbosity），代表 \"far beyond typical evaluation budgets\"。但关键不在于 n 大小——即使 n = ∞，如果 d → 0，Likert 永远无法检测到 effect。\n\nR2 提出 \"Blindspot 是否部分是 power issue\" 的问题，论文给出了明确否定回答。\n\n### R2-Q4: Register 轴是否做了 rewriter 替换测试？\n合理问题。查 Appendix D，rewriter independence test 仅覆盖 verbosity 和 formality（Table 7/8），register 未做替换测试。建议作者补充或在 Limitations 中注明。\n\n### R2-Q5: Tone axis NLI gate 失败案例分析？\n合理问题。论文对 tone axis 的失败仅用 \"tone axis NLI gate pass rate was too low for meaningful analysis\" 一句带过。2-3 句分析（NLI 判定内容改变是正确的 vs 误判；tone manipulation 是否 inherently content-altering）会有价值。\n\n---\n\n## 对 R2 总体评分的看法\n\nR2 给 **3.0 (Findings)**，主要基于三个 Must-Fix（N1 framing, N2 novelty, N3 negative control）和 novelty/excitement 评分偏低。我认为：\n\n1. **N1（framing）**实质上是 Should-Fix，不是 Must-Fix——修正 Abstract/Conclusion 的权重分配即可。\n2. **N2（novelty）**与 R2 自己的 S4（\"GEE per-axis decomposition 是真正增量贡献\"）矛盾——如果最核心方法论贡献被承认，整体 novelty 不应降到 3/5。\n3. **N3（negative control）**基于对论文 claim 的过度解读——论文从未声明架构特异性。\n\nR2 的 Excitement 3/5（\"对熟悉心理测量学的读者不意外\"）以错误的受众为标准——EMNLP 的读者是 NLP 研究者，不是心理测量学家。对于 routinely 使用 Likert 评分审计 LLM judges 的 NLP 社区，Blindspot 现象的受控量化具有直接实践价值。\n\n**我维持 Overall 3.5（Borderline Conference）。** 若 R2 的 N1-N3 全部为 Must-Fix，3.0 合理；但我认为 N2 和 N3 不构成 Must-Fix，N1 降为 Should-Fix 后，论文处于 Borderline Conference 区间。\n",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — 交叉回应 Reviewer 2 审稿意见\n\n---\n\n## Must-Fix 逐条回应\n\n### [AGREE] R2-N1: 标题与 framing 隐式预设 pairwise 为 ground truth\n**同意存在问题，但不同意 severity 为 Must-Fix，应为 Should-Fix。**\n\nR2 的核心观察是正确的：论文叙事重心偏向 \"Likert misses real signal\"，而 §5.1 的 construct divergence 讨论和 Limitations 的 Comparative Trap 引用被隔离在末尾。我在自己的审稿中也提出了类似问题（我的 W5: construct validity 讨论不充分）。\n\n但 R2 将此升级为 Must-Fix 过重，原因如下：\n1. **论文标题 \"Measurement-Mode Divergence\" 副标题本身是中性的**——\"Blindspot\" 是主标题的隐喻，但副标题准确描述了现象。\n2. **§5.1 已明确讨论三种解释**：\"Both Likert and pairwise may be 'correct' for their respective constructs\"（§5.1 倒数第三段），引用 Tripathi et al. (2025) 独立确认 construct divergence。问题是权重分配不均，而非完全缺失。\n3. **实践论证是有效的**：RLHF/DPO 使用 pairwise comparison，因此 pairwise-detected biases 是对 alignment pipeline 实际传播偏差的正确度量——这个论点在 §1 和 §6 均有涉及（\"Likert-only audits miss style-driven preferences that propagate through pairwise-based alignment pipelines\"），只是不够显式。\n\n**建议折中**：不必改标题（\"Blindspot\" 是有效的注意力锚点），但 Abstract 和 §6 应给 construct divergence 解释 1-2 句同等权重的空间。\n\n---\n\n### [REBUT] R2-N2: 新颖性定位模糊\n**不同意此为 Must-Fix。论文已在 §1 明确界定了贡献边界。**\n\nR2 称 \"Likert vs pairwise 灵敏度差异是 Thurstone (1927) 以来的经典结论\"——这在一般心理测量学层面成立，但在 LLM judge 风格偏差的特定语境中，**此前无受控实验量化过这一差异**。论文 §1 第 2 页明确声明：\n\n> \"Our contribution is the first controlled quantification of this per-axis sensitivity gap in the LLM judge setting; identifying the two-layer mechanism the inflation plus residual signal attenuation that drives it.\"\n\n> \"we previously sequentially conjectured for LLM judges\"（§2 末段，引用 Koh et al. 2025 作为先前猜测）\n\n论文区分了三层贡献：(1) 受控量化（vs. 先前的 observational 报告），(2) CSD 方法论（NLI gate + per-axis decomposition），(3) GEE 条件分解揭示 per-axis 混淆结构。R2 将 (3) 评价为 \"真正的增量贡献\"（R2-S4），却又在 N2 中称整体贡献为 \"domain transfer\"——这两个判断相互矛盾。\n\nR2 举 Thurstone (1927) 为前序工作，但 Thurstone 的 Law of Comparative Judgment 讨论的是心理物理学中刺激量级判断，与 LLM judge 在 NLG evaluation 中的风格偏好检测是不同 task。将\"一般性测量理论预测\"等同于\"特定领域的受控实验验证\"，忽视了 empirical science 中领域验证的价值。\n\n**结论**：论文措辞可局部收紧（如 §1 \"This is the Likert Blindspot\" 可改为 \"We term this the Likert Blindspot\"），但 N2 不构成 Must-Fix——因为贡献界定已在 §1 完成。\n\n---\n\n### [REBUT] R2-N3: 单一负控制不足以支撑架构特异性声明\n**不同意此为 Must-Fix。R2 对论文 claim 的解读超出了论文实际声明。**\n\n论文使用 Claude Sonnet 4 的目的是 **pipeline validation**（CSD 不会凭空制造偏差），**不是** architecture comparison。关键文本证据：\n\n- §4.1: \"Claude Sonnet 4 serves as confirmatory replication and is excluded from FWER control; as a sanity check, all eight tests remain significant under the expanded family.\"\n- §5.3: \"A negative control judge shows no divergence on either primary axis, supporting discriminative validity.\"\n- §6: \"including a negative control judge showing no pairwise divergence\"\n\n论文从未声明 \"only certain architectures show the Blindspot\" 或 \"the Blindspot is architecture-specific\"。Claude 的作用是证明 **CSD 具有 discriminative validity**——当真实偏差不存在时，pipeline 不报假阳性。这与 \"探讨为何 Claude 不受影响\" 是完全不同的研究问题。\n\nR2 要求 \"讨论可能机制\" 和 \"测试同系列其他模型\"——这是要求论文回答一个它未提出的问题。将此升级为 Must-Fix 要求论文做超出其 scope 的工作。\n\n**补充证据**：Appendix D（rewriter independence test）用 GPT-4o 替换 Qwen3-32B 作为 rewriter，Blindspot 持续存在——这进一步表明 Blindspot 不依赖特定 evaluator-producer 组合，是 pipeline 鲁棒性而非架构特异性的证据。\n\n**结论**：R2 的关切可以通过在 Limitations 增加 1-2 句（\"the mechanism behind Claude's null result remains unexplored\"）解决，不构成 Must-Fix。\n\n---\n\n## Should-Fix 逐条回应\n\n### [AGREE] R2-W1: 主实验仅用 LLMBar, cross-benchmark 覆盖稀疏\n**部分同意。**\n\nTable 1 的 AlpacaEval 和 MT-Bench 确实仅覆盖 formality + verbosity 的部分 judge 组合。\"across three benchmarks\" 的泛化声明需要限定。\n\n但须注意两点缓解因素：\n1. AlpacaEval 的 scaled replication (n = 355) 是独立的大样本验证，且 Appendix K（formal power analysis）和 Appendix J（bootstrap attenuation）均基于此样本。\n2. §5.3 的 cross-judge 和 cross-axis replication 在 LLMBar 内部已用 4 个 judge × 3 个 axis = 12 个 cell 验证，8/11 显著（Table 1）。\n\n建议将 \"across three benchmarks\" 限定为 \"with primary results on LLMBar and confirmatory replication on AlpacaEval and MT-Bench for selected configurations\"。\n\n---\n\n### [AGREE] R2-W2: Register 轴 evaluator-producer overlap\n**部分同意。** Qwen3-32B 作为 rewriter + judge 的 overlap 应在论文中标注。我在自己的 M2 中也提出了类似问题（Appendix M 的 100-point Likert 用 Qwen3-32B）。\n\n但须注意：register 的主要 Blindspot 结果来自 **其他 judge**（GPT-4o register n.s., Llama-70B register 63.1% BT significant——Table 1），这些 judge 与 rewriter 无 overlap。论文的核心 claim 建立在 verbosity 和 formality 上，register 是补充。\"降级为 exploratory\" 过强，标注 overlap 即可。\n\n---\n\n### [REBUT] R2-W3: Abstract 数字密度过高\n**不同意。** 对于一篇以 \"7 种统计方法 × 4 judges × 3 benchmarks\" 为核心卖点的实证论文，Abstract 中的定量具体性（BT > 60%, p < 0.001; d → 0, p > 0.17）是必要的——它精确传达了 Blindspot 的 magnitude 和统计证据强度。去除这些数字会使 Abstract 变为无法验证的 qualitative assertion。\n\nARR reviewer guidelines 未对 Abstract 数字密度设限。Empirical NLP 论文（如 Wang et al. 2024 Chatbot Arena, Zheng et al. 2023 MT-Bench）的 Abstract 同样包含定量结果。\n\n---\n\n### [AGREE] R2-W4: Introduction motivating example 未 acknowledge formality-quality nuance\n**同意，minor 级别修正即可。** §1 开头的 GPT-4o 例子（Likert 评 casual 为 8, formal 为 5，但 pairwise 一致选 formal）确实隐含了 \"Likert 的判断是错误的\"，而 formality 与 perceived quality 的关联直到 Appendix A 才讨论。在例子后添加一句 caveat（\"whether this reflects a genuine quality difference or a stylistic preference is itself a question we address in §5.1\"）即可解决。\n\n---\n\n### [REBUT] R2-W5: \"Framework\" 设定过高预期\n**不同意。** \"Framework\" 在 NLP 文献中常用于描述 multi-stage experimental protocols（例如 RATE: Reber et al. 2025 称自己为 \"framework\"；Chatbot Arena 称自己为 \"platform\"/\"framework\"）。CSD 包含三个独立组件（NLI gate, per-axis decomposition, position-controlled pairwise），每个组件可独立复用——这是 framework 而非 one-off protocol 的定义特征。\n\n3 个成功轴 + 1 个失败轴（tone）恰恰证明 framework 有 discriminative validity：它不是对所有输入都报阳性的 trivial pipeline。\n\n---\n\n## Questions 回应\n\n### R2-Q1: 哪项 amplification control 最直接排除 \"pairwise amplifies micro-preferences\"？\n\n这是好问题。最直接的证据组合：\n1. **负控制（Claude）**：如果 pairwise 系统性放大微偏好，Claude 也应显示 inflated BT。Claude BT ≈ 50%（Table 1）证明 pairwise 不 uniformly amplify。\n2. **Same-style double-rewrite control（§5.4, Appendix O）**：original vs. same-style rewrite 的 BT 被 GEE originality term 吸收，证明 rewriting artifact ≠ style signal。\n3. **Rewriter independence（Appendix D）**：GPT-4o rewriter 替换后 Blindspot 持续——排除了 Qwen3-32B rewriter 特有的 style 注入。\n\n但 R2 的核心问题——\"无人类 ground truth 如何区分 attenuation vs amplification\"——确实没有被完全回答。论文 §5.1 承认这一点。我同意这是论文的 inherent limitation，但不是 paper-breaking 问题，因为实践论证（RLHF 用 pairwise → pairwise-detected biases 实际传播）提供了 pragmatic ground truth。\n\n### R2-Q2: Claude 机制？\n同意这是开放问题。我在自己的审稿中未专门提出，但认为在 Limitations 增加 1-2 句讨论（可能与 Claude 的 RLHF 训练策略或内部评估策略有关）是合理的。\n\n### [REBUT] R2-Q3: 大样本下 Likert Type II error 是否因功效提升而缩小？\n**论文已明确回答此问题。** R2 似乎未充分考虑 Appendix J 和 K 的证据：\n\n- **Appendix J（Bootstrap Attenuation Analysis）**：subsample BT 在所有样本量下稳定在 BT 76-77%（p < 0.001），而 Likert d 随 n 增大 **converges to zero**——不是 converge to a small nonzero value，是趋向零（Table 11: d remains flat near zero across sample sizes while BT is stable at 66.5%）。这直接证明 Blindspot 是 structural measurement difference，不是 power issue。\n- **Appendix K（Formal Power Analysis）**: 对于 Likert 达到 80% power 所需 n > 1,200（Qwen3-32B verbosity），代表 \"far beyond typical evaluation budgets\"。但关键不在于 n 大小——即使 n = ∞，如果 d → 0，Likert 永远无法检测到 effect。\n\nR2 提出 \"Blindspot 是否部分是 power issue\" 的问题，论文给出了明确否定回答。\n\n### R2-Q4: Register 轴是否做了 rewriter 替换测试？\n合理问题。查 Appendix D，rewriter independence test 仅覆盖 verbosity 和 formality（Table 7/8），register 未做替换测试。建议作者补充或在 Limitations 中注明。\n\n### R2-Q5: Tone axis NLI gate 失败案例分析？\n合理问题。论文对 tone axis 的失败仅用 \"tone axis NLI gate pass rate was too low for meaningful analysis\" 一句带过。2-3 句分析（NLI 判定内容改变是正确的 vs 误判；tone manipulation 是否 inherently content-altering）会有价值。\n\n---\n\n## 对 R2 总体评分的看法\n\nR2 给 **3.0 (Findings)**，主要基于三个 Must-Fix（N1 framing, N2 novelty, N3 negative control）和 novelty/excitement 评分偏低。我认为：\n\n1. **N1（framing）**实质上是 Should-Fix，不是 Must-Fix——修正 Abstract/Conclusion 的权重分配即可。\n2. **N2（novelty）**与 R2 自己的 S4（\"GEE per-axis decomposition 是真正增量贡献\"）矛盾——如果最核心方法论贡献被承认，整体 novelty 不应降到 3/5。\n3. **N3（negative control）**基于对论文 claim 的过度解读——论文从未声明架构特异性。\n\nR2 的 Excitement 3/5（\"对熟悉心理测量学的读者不意外\"）以错误的受众为标准——EMNLP 的读者是 NLP 研究者，不是心理测量学家。对于 routinely 使用 Likert 评分审计 LLM judges 的 NLP 社区，Blindspot 现象的受控量化具有直接实践价值。\n\n**我维持 Overall 3.5（Borderline Conference）。** 若 R2 的 N1-N3 全部为 Must-Fix，3.0 合理；但我认为 N2 和 N3 不构成 Must-Fix，N1 降为 Should-Fix 后，论文处于 Borderline Conference 区间。\n",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 873 · 2026-05-22T19:44:21.553483+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4321
}
```

</details>

---


### Assistant

_source line 874 · 2026-05-22T19:44:30.969426+00:00_

交叉回应已提交。核心判断：

- **N1（framing）**：同意实质问题，但降级为 Should-Fix——叙事权重不均但非完全缺失
- **N2（novelty）**：反驳——§1 已明确界定贡献为"首次受控量化"，且 R2 自己承认 GEE 分解是真正增量贡献，两个判断矛盾
- **N3（负控制）**：反驳——论文用 Claude 做 pipeline validation 而非 architecture comparison，R2 读入了论文未提出的 claim
- **Q3（power issue）**：反驳——Appendix J/K 明确证明 Likert d → 0 at all n，是结构性差异非功效问题

维持 Overall 3.5（Borderline Conference），认为 R2 的 3.0 偏低。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 29

## Round 29

58 recorded events


### User

_source line 875 · 2026-05-22T22:40:09.870633+00:00_

[Round 1 审稿请求]:
你负责**方法严谨性 + 统计方法学 + 实验设计**的审查。

## 论文信息
- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation
- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf`

## Venue 要求（EMNLP 2026 via ARR）
- **格式**: ACL 模板，double-blind
- **页数**: 正文 ≤8 页，参考文献不限
- **Limitations**: 不计入页数限制，需在 conclusion 后、references 前
- **匿名**: 必须匿名，作者写 "Anonymous"
- **截止日期**: 2026-05-25 (ARR May cycle)
- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）

## 你的审查侧重
请重点审查以下方面：

1. **统计方法的正确性与完整性**：
   - BT 模型的 IIA 假设是否充分讨论？
   - GEE 模型选择（exchangeable correlation + sandwich SE）是否合理？
   - Bootstrap CI 方法（percentile vs BCa）是否指明？
   - TOST 等价检验的 Δ=15pp 是否有充分的外部依据？
   - Holm-Bonferroni 校正范围是否合理？

2. **实验设计的严谨性**：
   - NLI gate 的内容保持验证是否充分（50 对人工标注 κ=0.44）？
   - Cross-rewriter independence test 的覆盖范围？
   - 负控制（Claude Sonnet 4）的论证力度？
   - Direction-aware NLI gate 恢复的 21 对的内容质量验证？

3. **可重复性与透明度**：
   - 模型版本、超参数、随机种子是否完整报告？
   - 统计检验的前提假设是否满足并报告？

4. **格式合规**：
   - 正文是否 ≤8 页？
   - 是否使用 ACL 模板？
   - 是否匿名？
   - Limitations section 是否在正确位置？

请给出结构化审稿意见：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 876 · 2026-05-22T22:40:19.920680+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 877 · 2026-05-22T22:40:19.921178+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-22T22:40:25.711123+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 879 · 2026-05-22T22:40:26.617935+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer form dimensions scoring 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer form dimensions scoring 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-22T22:40:28.879575+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-22T22:40:32.042373+00:00_

Web search results for query: "ACL Rolling Review reviewer form dimensions scoring 2025 2026"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here's what I found about the ACL Rolling Review reviewer form dimensions and scoring for 2025-2026:

## Reviewer Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendatio
…[truncated 938 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5424
}
```

</details>

---


### Tool result

_source line 882 · 2026-05-22T22:40:33.348384+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found relevant information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's what the search results show:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility, while conference recom
…[truncated 1498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7637
}
```

</details>

---


### Tool result

_source line 883 · 2026-05-22T22:40:34.703484+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 586.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p9.p
…[truncated 526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5823
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-22T22:40:41.479646+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment scales and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment scales and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 885 · 2026-05-22T22:40:42.504472+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, scoring criteria, best practices, and any specific instructions about soundness, excitement, reproducibility, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, scoring criteria, best practices, and any specific instructions about soundness, excitement, reproducibility, etc."
  }
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-22T22:40:43.424610+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 887 · 2026-05-22T22:40:44.032991+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-22T22:40:44.863465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 889 · 2026-05-22T22:40:45.581624+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-22T22:40:45.983325+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-22T22:40:46.989579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3564
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-22T22:40:46.990047+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-22T22:40:47.596449+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3563
}
```

</details>

---


### Tool call

_source line 894 · 2026-05-22T22:40:47.596899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 895 · 2026-05-22T22:40:47.949023+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 896 · 2026-05-22T22:40:49.007551+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4144
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-22T22:40:49.460612+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3878
}
```

</details>

---


### Tool result

_source line 898 · 2026-05-22T22:40:49.511343+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough"

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper"
- **2**: "Potentially Interesting: does not resonate with me, but might with others"
- **1**: "Not Exciting: does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award: could be considered for outstanding paper award"
- **4**: "Conference: could be accepted to an ACL conference"
- **3**: "Findings: could be accepted to Findings of the ACL"
- **2**: "Resubmit next cycle: needs substantial revisions"
- **1**: "Do not resubmit: has to be fully redone"

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results"
- **4**: "They could mostly reproduce the results"
- **3**: "They could reproduce with some difficulty"
- **2**: "They would be hard pressed to reproduce the results"
- **1**: "They would not be able to reproduce the results"

## 
…[truncated 905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8031
}
```

</details>

---


### Tool result

_source line 899 · 2026-05-22T22:40:49.766866+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3783
}
```

</details>

---


### Tool result

_source line 900 · 2026-05-22T22:40:50.425260+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3435
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-22T22:40:50.577530+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2628
}
```

</details>

---


### Tool result

_source line 902 · 2026-05-22T22:40:50.578597+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2981
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-22T22:40:56.451037+00:00_

# ARR Reviewer Guidelines: Complete Summary

## Core Evaluation Framework

ARR reviewers assess papers using **three scores** (as of February 2025):

1. **Soundness**: Technical correctness and methodological rigor. Scores must be justified by review text—low soundness scores require substantial evidence of flaws.

2. **Excitement**: Personal interest and perceived impact, orthogonal to soundness. Reflects subjective preferences without requiring explicit justification.

3. **Overall Recommendation**: Composite assessment reflecting soundness, excitement, novelty, and potential impact. Papers recommended for conferences must demonstrate sufficient soundness and reproducibility.

## Key Review Tasks

### Task 1: Calendar Planning
Block time for reviewing, discussion periods, and potential revisions. Reviewers should clock their actual time to estimate future workload accurately.

### Task 2: Assignment Verification
- **Expertise check**: Confirm qualification to review assigned papers; flag significant expertise gaps
- **Anonymity check**: Disclose any knowledge of author identity to the area chair
- **COI assessment**: Request reassignment for conflicts of interest
- **Desk-rejection screening**: Evaluate for hallucinated references, anonymity violations, style non-compliance, missing limitations sections, and ethics concerns

### Task 3: Writing Strong Reviews

**Reading Strategy**: Review papers twice—first skim to adjust expectations and understand research questions, then in-depth reading for technical evaluation.

**Specificity Requirements**: Avoid vague criticisms. Instead of "missing relevant references," cite specific works (e.g., "missing references X, Y, Z").

**Common Review Pitfalls** (Heuristics H1-H17):
- Dismissing results as "unsurprising" despite lack of prior empirical validation
- Rejecting negative results (valid contributions)
- Penalizing simplicity in solutions
- Requiring SOTA results when not claimed
- Over-generalizing from limited languag
…[truncated 2380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 13946
}
```

</details>

---


### Tool call

_source line 904 · 2026-05-22T22:41:04.495843+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "11-18",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "11-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 905 · 2026-05-22T22:41:05.950975+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 440.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 437.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 591.2}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 598.2}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 355.1}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_styl
…[truncated 93 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-22T22:41:05.951696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 907 · 2026-05-22T22:41:06.202946+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 908 · 2026-05-22T22:41:06.756088+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-22T22:41:07.158254+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-22T22:41:11.077316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 911 · 2026-05-22T22:41:11.582468+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 912 · 2026-05-22T22:41:12.689267+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1611
}
```

</details>

---


### Tool call

_source line 913 · 2026-05-22T22:41:12.689742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 914 · 2026-05-22T22:41:13.191605+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 915 · 2026-05-22T22:41:13.446504+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1864
}
```

</details>

---


### Tool call

_source line 916 · 2026-05-22T22:41:13.446948+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-22T22:41:14.411169+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1721
}
```

</details>

---


### Tool call

_source line 918 · 2026-05-22T22:41:14.411630+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 919 · 2026-05-22T22:41:14.864111+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1672
}
```

</details>

---


### Tool result

_source line 920 · 2026-05-22T22:41:14.867378+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1420
}
```

</details>

---


### Tool call

_source line 921 · 2026-05-22T22:41:14.867742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 922 · 2026-05-22T22:41:15.320634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 923 · 2026-05-22T22:41:15.573341+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1161
}
```

</details>

---


### Tool result

_source line 924 · 2026-05-22T22:41:16.279928+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-22T22:41:16.433067+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1112
}
```

</details>

---


### Tool call

_source line 926 · 2026-05-22T22:48:11.148116+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 核心发现（Likert Blindspot）由7种方法×4个judge×3个benchmark交叉验证支撑充分，GEE分解框架有方法论创新；但NLI gate人工验证标注一致性偏低（κ=0.44）、TOST等价检验SESOI缺乏外部校准，削弱了measurement methodology论文应有的方法论严密度。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心claim有7种方法交叉验证，GEE诊断完善（Appendix C/H）；但NLI gate标注一致性弱（κ=0.44）、TOST SESOI缺乏外部校准、bootstrap CI类型未指明 |\n| Excitement | 3.5/5 | Likert Blindspot发现对NLG评估实践有直接影响；GEE per-axis decomposition揭示了style vs originality confound的轴间异质性，是genuine insight |\n| Reproducibility | 4/5 | 模型版本（GPT-4o-2024-08-06等）、种子（seed 42）、代码/数据release承诺完整；bootstrap CI类型和LLM rewriting随机种子是两个报告缺口 |\n| Confidence | 4/5 | 统计方法学和实验设计是我的专长领域 |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] NLI Gate人工验证标注一致性不足，样本量偏小\n- 具体位置：Section 5.4 (Robustness), Appendix S\n- 问题：NLI gate是CSD pipeline的核心内容保持机制——如果gate不可靠，整条因果推断链的前提就不成立。两名标注者在50对样本上的Cohen's κ=0.44（moderate agreement）。论文指出Gwet's AC1=0.63缓解了prevalence效应，但AC1=0.63仍仅为\"substantial\"下限而非strong agreement。Gate-passed pairs的precision在majority vote下达到100%（Wilson CI [86.76, 100%]），这一数字看似优秀，但：(1) 仅基于25对gate-passed样本，置信区间下界86.76%意味着true precision可能低至87%；(2) κ=0.44的overall disagreement表明\"内容保持\"这一判断存在系统性主观分歧，gate threshold 0.90的calibration可靠性存疑。\n- 为什么影响接收：对于以measurement methodology为核心贡献的论文，pipeline核心组件的validation标准应更高。如果有~13%的gate-passed pairs实际存在语义变化（precision下界暗示的可能性），则观测到的style bias可能部分被content差异contaminate。\n- 建议修改方向：(1) 增加标注者至3人以上，报告Fleiss' κ；(2) 对A1-A2 disagreement cases进行定性error analysis——区分\"真正语义变化\"vs\"风格变化被标注者误判为语义变化\"；(3) 在不同NLI threshold（0.85, 0.90, 0.95）上报告precision和downstream BT结果的sensitivity（Appendix E已有Table 9的threshold sweep，但缺少human precision在不同threshold下的变化）。\n\n**N2** [critical] TOST等价检验的SESOI Δ=15pp缺乏外部校准，负控制论证力不足\n- 具体位置：Appendix G (Table 10), Section 5.1\n- 问题：论文选择Δ=15pp（对应BT 65%）作为smallest effect size of interest，理由是\"approximately where format preference would materially affect model rankings\"——这是循环论证，用未经验证的实践判断来设定统计检验阈值。Table 10显示：在Δ=10pp下Claude Sonnet 4未通过等价检验（p=0.156, power=82%），BT仍为56.2%（高于50%）。这意味着\"负控制\"实际展现了non-trivial的format preference（6.2pp偏离chance），只是在一个相当宽松的Δ=15pp下才被判定为\"等价\"。论文对此是transparent的，但framing为\"negative control\"可能误导读者认为该judge不存在style bias。\n- 为什么影响接收：负控制的有效性直接影响Likert Blindspot作为systematic phenomenon而非judge-specific artifact的论证强度。如果Claude Sonnet 4也存在中等偏好但只是在宽松阈值下被判为\"等价\"，那么论文的narrative需要调整。\n- 建议修改方向：(1) 引用measurement theory或prior LLM evaluation文献中的effect size benchmarks来校准SESOI——例如参考Thurstone (1927)的JND框架或LLM evaluation中公认的meaningful effect thresholds；(2) 明确讨论Δ=10pp下的失败意味着什么；(3) 将Claude Sonnet 4从\"negative control\"重新framing为\"weak-effect/attenuated-bias control\"，更准确反映BT=56.2%的实际效应。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Bootstrap CI方法类型未报告\n- 具体位置：Section P (Implementation Details), Appendix I (Table 11)\n- 问题：论文报告\"All bootstrap CIs use 10,000 pair-level resamples with seed 42\"但未指明percentile method、BCa（bias-corrected and accelerated）还是其他变体。对于BT win probability这类bounded [0,1]参数，percentile intervals在小样本或偏斜分布下覆盖率可能不足，而BCa可纠正偏差和偏度。Table 11报告了大量CI，但读者无法评估其coverage properties。\n- 建议：明确报告bootstrap CI类型。如果使用percentile method，至少在一个edge-case配置（如smallest n的condition）上与BCa对比。\n\n**W2** [warning] Cross-rewriter independence验证仅覆盖一个轴\n- 具体位置：Section 5.3, Appendix D, Tables 7-8\n- 问题：Cross-rewriter验证（GPT-4o rewriter × Qwen3-32B judge）仅在verbosity轴完成。Formality轴——论文最核心的Blindspot发现轴——缺乏cross-rewriter验证。鉴于Qwen3-32B同时作为rewriter和judge存在evaluator-producer overlap（Appendix D估计Style OR降低22%），formality轴上的独立性验证对排除自我偏好混淆尤为重要。Table 7仅报告verbosity轴的NLI pass rate和BT。\n- 建议：补充至少一个formality轴的cross-rewriter实验（如GPT-4o rewrite formality → Qwen3-32B judge），或充分论证为何verbosity轴的验证可泛化到formality轴。\n\n**W3** [warning] Direction-aware NLI gate恢复的21对未经人工验证\n- 具体位置：Appendix F (Direction-Aware Gate Validation)\n- 问题：Direction-aware gating放宽了bidirectional entailment标准（仅要求forward entailment），从rejection中恢复了21对（3.2%）。论文通过统计一致性验证其合理性（BT方向一致，Δ=-1.1pp，95% CI含零），但这21对未经任何人工标注。主pipeline的gate-passed pairs至少有50对人工验证——放宽标准的部分理应接受至少同等水平的人工检查。\n- 建议：对这21对进行人工抽检（至少1名标注者），报告content preservation precision。\n\n**W4** [warning] BT模型unidimensionality假设仅在脚注讨论\n- 具体位置：Page 6, Footnote 1\n- 问题：BT模型假设单一潜在\"quality\"维度决定偏好。脚注承认此假设\"standard in evaluation contexts but not empirically verified here\"。但LLM judge在pairwise comparison中的决策可能同时受质量、流畅度、风格偏好等多维因素驱动。对于以measurement methodology为核心贡献的论文，这一假设的讨论不应止于脚注。如果judge在比较中同时权衡多个维度，BT参数的解释（\"style bias的大小\"）可能被confound。\n- 建议：(1) 将IIA/unidimensionality讨论从脚注提升到Limitations或正文Section 3.5；(2) 讨论multi-dimensional preference下BT参数解释的变化。\n\n**W5** [warning] 样本外部效度论证不足\n- 具体位置：Section 3.4 (Experimental Setup)\n- 问题：实验基于LLMBar的100个instruction-response pairs。LLMBar是一个用于检测LLM judge能否区分response质量的benchmark，其task分布（主要是短instruction-following tasks）可能不代表LLM judge的所有典型使用场景（如长文本摘要评估、对话质量评估、创意写作评估）。虽然LLMBar有human-verified quality labels且moderate size允许exhaustive pairwise evaluation，但论文仅通过AlpacaEval和MT-Bench的\"confirmatory replication on selected configurations\"来论证泛化性（Table 1脚注），且这些replication是partial的。\n- 建议：在Limitations中更明确地讨论task domain的局限性，以及在哪些场景下Blindspot效应可能更强或更弱。\n\n## 小问题（不影响接收）\n\n- **M1** [format]: 正文可能微超8页——Conclusion (Section 6)最后一句\"modes is the key next step.\"溢出到第9页Limitations之前。建议微调排版确保conclusion完整收在第8页内。\n- **M2** [reproducibility]: LLM rewriting使用temperature=0.7（Section 3.1），但未报告是否固定decoding seed或使用多次采样取最佳结果。这影响exact reproducibility。\n- **M3** [clarity]: Table 1中\"Likert not\"列和\"1 = Blindspot case\"标记逻辑需要对照正文才能理解，caption自解释性不足。\n- **M4** [clarity]: Figure 4的y轴\"Significance proxy\"的定义在caption中模糊——如果是power-like的度量，应明确计算公式（如1 - p value的某种transformation）。\n- **M5** [notation]: Table 3中Originality OR的asterisk标注与Style OR的不完全一致——建议统一显著性标记格式。\n\n## Questions for Authors\n\n1. **NLI threshold sensitivity的极端情况**：Appendix E (Table 9)显示所有44种judge×axis×threshold配置的BT都significant (p < 0.05)。能否确认是否存在**任何**NLI threshold使某些Blindspot case消失？如果所有threshold都robust，这实际上是论文的一个强优势，但当前呈现方式不够突出。\n\n2. **Formality Style OR <1的解释**：Table 3中部分formality配置的Style OR<1（如GPT-4o form: OR=2.58但Qwen3 form: OR=2.31，Gemini form: OR=1.64）。更关键的是正文提到\"formality is a conditional effect, register is style OR <1\"。Style OR<1意味着style transformation反而**降低**了被选中的概率——这一反直觉结果如何机制性解释？\n\n3. **Bootstrap attenuation的interpretation**：Appendix J显示d_median ≈ -0.017在所有样本量下近乎恒定。这是否意味着在此数据上Likert ATE是**真正的零效应**而非merely underpowered？如果是true null，这对\"Blindspot的机制是attenuation还是amplification\"的讨论意味着什么？\n\n4. **GEE model的causal interpretation**：论文多处使用\"causal\"语言（如\"Controlled Style Decomposition\"中的\"controlled\"），但GEE模型本身是associational的。控制来自实验设计（rewriting保持content），而非统计模型。能否更精确地界定哪些inference是causal的、哪些是conditional association？\n\n## Missing References\n\n论文的相关工作覆盖面较好。建议补充：\n- **Luce (1959)** \"Individual Choice Behavior\" — BT模型的理论基础文献，与论文对BT IIA假设的讨论直接相关\n- **Bowman et al. (2015)** SNLI或**Williams et al. (2018)** MNLI — NLI gate是pipeline核心组件，但当前引用集中在DeBERTa技术文献，缺少对NLI任务本身局限性（如entailment与semantic equivalence的distinction）的文献支撑\n- 最新版本的pairwise evaluation方法论综述（如有），特别是关于BT model在LLM evaluation中的validity conditions\n\n## 主要优势\n\n1. **多方法交叉验证的说服力**：Table 2中7种测量方法——3种Likert-based（interval scaling, ordinal regression, nonparametric rank）、2种pairwise-based（BT, signed-rank）——全部Likert方法fail、全部pairwise方法pass。这种一致性不太可能是统计偶然。\n\n2. **GEE per-axis decomposition的方法论价值**：Table 3揭示verbosity是style-dominated（Style OR 5-13）而formality是conditional effect（受originality confound调节），这不仅描述了bias，更提供了可操作的诊断框架——告诉practitioners哪些轴的评估结果可以直接解读、哪些需要decomposition。\n\n3. **统计诊断的深度远超typical submission**：GEE correlation structure comparison（Appendix C, 9个judge×axis cells的QIC对比）、Bradley-Terry goodness-of-fit（Appendix H, chi-squared tests + direction asymmetry）、formal power analysis（Appendix K, required n for 80% power）、bootstrap attenuation curve（Appendix J, 7个subsample sizes）——每一项都不是走流程，而是genuine diagnostic。\n\n4. **实验设计的控制意识**：position-controlled comparison（Section 3.3, 每对出现两次消除position bias）、NLI gate（虽有验证不足的问题，但设计意图正确）、cross-rewriter validation（虽然范围有限）、negative control（虽然效应未完全消除）——展现了对confound识别的系统性思考。\n\n5. **实际影响清晰**：论文明确指出\"Likert-only audits may fail to register surface style-driven preferences that drive pairwise-based alignment pipelines (RLHF, DPO)\"（Section 6），为NLG evaluation pipeline设计提供了直接可操作的警示。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 核心发现（Likert Blindspot）由7种方法×4个judge×3个benchmark交叉验证支撑充分，GEE分解框架有方法论创新；但NLI gate人工验证标注一致性偏低（κ=0.44）、TOST等价检验SESOI缺乏外部校准，削弱了measurement methodology论文应有的方法论严密度。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心claim有7种方法交叉验证，GEE诊断完善（Appendix C/H）；但NLI gate标注一致性弱（κ=0.44）、TOST SESOI缺乏外部校准、bootstrap CI类型未指明 |\n| Excitement | 3.5/5 | Likert Blindspot发现对NLG评估实践有直接影响；GEE per-axis decomposition揭示了style vs originality confound的轴间异质性，是genuine insight |\n| Reproducibility | 4/5 | 模型版本（GPT-4o-2024-08-06等）、种子（seed 42）、代码/数据release承诺完整；bootstrap CI类型和LLM rewriting随机种子是两个报告缺口 |\n| Confidence | 4/5 | 统计方法学和实验设计是我的专长领域 |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] NLI Gate人工验证标注一致性不足，样本量偏小\n- 具体位置：Section 5.4 (Robustness), Appendix S\n- 问题：NLI gate是CSD pipeline的核心内容保持机制——如果gate不可靠，整条因果推断链的前提就不成立。两名标注者在50对样本上的Cohen's κ=0.44（moderate agreement）。论文指出Gwet's AC1=0.63缓解了prevalence效应，但AC1=0.63仍仅为\"substantial\"下限而非strong agreement。Gate-passed pairs的precision在majority vote下达到100%（Wilson CI [86.76, 100%]），这一数字看似优秀，但：(1) 仅基于25对gate-passed样本，置信区间下界86.76%意味着true precision可能低至87%；(2) κ=0.44的overall disagreement表明\"内容保持\"这一判断存在系统性主观分歧，gate threshold 0.90的calibration可靠性存疑。\n- 为什么影响接收：对于以measurement methodology为核心贡献的论文，pipeline核心组件的validation标准应更高。如果有~13%的gate-passed pairs实际存在语义变化（precision下界暗示的可能性），则观测到的style bias可能部分被content差异contaminate。\n- 建议修改方向：(1) 增加标注者至3人以上，报告Fleiss' κ；(2) 对A1-A2 disagreement cases进行定性error analysis——区分\"真正语义变化\"vs\"风格变化被标注者误判为语义变化\"；(3) 在不同NLI threshold（0.85, 0.90, 0.95）上报告precision和downstream BT结果的sensitivity（Appendix E已有Table 9的threshold sweep，但缺少human precision在不同threshold下的变化）。\n\n**N2** [critical] TOST等价检验的SESOI Δ=15pp缺乏外部校准，负控制论证力不足\n- 具体位置：Appendix G (Table 10), Section 5.1\n- 问题：论文选择Δ=15pp（对应BT 65%）作为smallest effect size of interest，理由是\"approximately where format preference would materially affect model rankings\"——这是循环论证，用未经验证的实践判断来设定统计检验阈值。Table 10显示：在Δ=10pp下Claude Sonnet 4未通过等价检验（p=0.156, power=82%），BT仍为56.2%（高于50%）。这意味着\"负控制\"实际展现了non-trivial的format preference（6.2pp偏离chance），只是在一个相当宽松的Δ=15pp下才被判定为\"等价\"。论文对此是transparent的，但framing为\"negative control\"可能误导读者认为该judge不存在style bias。\n- 为什么影响接收：负控制的有效性直接影响Likert Blindspot作为systematic phenomenon而非judge-specific artifact的论证强度。如果Claude Sonnet 4也存在中等偏好但只是在宽松阈值下被判为\"等价\"，那么论文的narrative需要调整。\n- 建议修改方向：(1) 引用measurement theory或prior LLM evaluation文献中的effect size benchmarks来校准SESOI——例如参考Thurstone (1927)的JND框架或LLM evaluation中公认的meaningful effect thresholds；(2) 明确讨论Δ=10pp下的失败意味着什么；(3) 将Claude Sonnet 4从\"negative control\"重新framing为\"weak-effect/attenuated-bias control\"，更准确反映BT=56.2%的实际效应。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Bootstrap CI方法类型未报告\n- 具体位置：Section P (Implementation Details), Appendix I (Table 11)\n- 问题：论文报告\"All bootstrap CIs use 10,000 pair-level resamples with seed 42\"但未指明percentile method、BCa（bias-corrected and accelerated）还是其他变体。对于BT win probability这类bounded [0,1]参数，percentile intervals在小样本或偏斜分布下覆盖率可能不足，而BCa可纠正偏差和偏度。Table 11报告了大量CI，但读者无法评估其coverage properties。\n- 建议：明确报告bootstrap CI类型。如果使用percentile method，至少在一个edge-case配置（如smallest n的condition）上与BCa对比。\n\n**W2** [warning] Cross-rewriter independence验证仅覆盖一个轴\n- 具体位置：Section 5.3, Appendix D, Tables 7-8\n- 问题：Cross-rewriter验证（GPT-4o rewriter × Qwen3-32B judge）仅在verbosity轴完成。Formality轴——论文最核心的Blindspot发现轴——缺乏cross-rewriter验证。鉴于Qwen3-32B同时作为rewriter和judge存在evaluator-producer overlap（Appendix D估计Style OR降低22%），formality轴上的独立性验证对排除自我偏好混淆尤为重要。Table 7仅报告verbosity轴的NLI pass rate和BT。\n- 建议：补充至少一个formality轴的cross-rewriter实验（如GPT-4o rewrite formality → Qwen3-32B judge），或充分论证为何verbosity轴的验证可泛化到formality轴。\n\n**W3** [warning] Direction-aware NLI gate恢复的21对未经人工验证\n- 具体位置：Appendix F (Direction-Aware Gate Validation)\n- 问题：Direction-aware gating放宽了bidirectional entailment标准（仅要求forward entailment），从rejection中恢复了21对（3.2%）。论文通过统计一致性验证其合理性（BT方向一致，Δ=-1.1pp，95% CI含零），但这21对未经任何人工标注。主pipeline的gate-passed pairs至少有50对人工验证——放宽标准的部分理应接受至少同等水平的人工检查。\n- 建议：对这21对进行人工抽检（至少1名标注者），报告content preservation precision。\n\n**W4** [warning] BT模型unidimensionality假设仅在脚注讨论\n- 具体位置：Page 6, Footnote 1\n- 问题：BT模型假设单一潜在\"quality\"维度决定偏好。脚注承认此假设\"standard in evaluation contexts but not empirically verified here\"。但LLM judge在pairwise comparison中的决策可能同时受质量、流畅度、风格偏好等多维因素驱动。对于以measurement methodology为核心贡献的论文，这一假设的讨论不应止于脚注。如果judge在比较中同时权衡多个维度，BT参数的解释（\"style bias的大小\"）可能被confound。\n- 建议：(1) 将IIA/unidimensionality讨论从脚注提升到Limitations或正文Section 3.5；(2) 讨论multi-dimensional preference下BT参数解释的变化。\n\n**W5** [warning] 样本外部效度论证不足\n- 具体位置：Section 3.4 (Experimental Setup)\n- 问题：实验基于LLMBar的100个instruction-response pairs。LLMBar是一个用于检测LLM judge能否区分response质量的benchmark，其task分布（主要是短instruction-following tasks）可能不代表LLM judge的所有典型使用场景（如长文本摘要评估、对话质量评估、创意写作评估）。虽然LLMBar有human-verified quality labels且moderate size允许exhaustive pairwise evaluation，但论文仅通过AlpacaEval和MT-Bench的\"confirmatory replication on selected configurations\"来论证泛化性（Table 1脚注），且这些replication是partial的。\n- 建议：在Limitations中更明确地讨论task domain的局限性，以及在哪些场景下Blindspot效应可能更强或更弱。\n\n## 小问题（不影响接收）\n\n- **M1** [format]: 正文可能微超8页——Conclusion (Section 6)最后一句\"modes is the key next step.\"溢出到第9页Limitations之前。建议微调排版确保conclusion完整收在第8页内。\n- **M2** [reproducibility]: LLM rewriting使用temperature=0.7（Section 3.1），但未报告是否固定decoding seed或使用多次采样取最佳结果。这影响exact reproducibility。\n- **M3** [clarity]: Table 1中\"Likert not\"列和\"1 = Blindspot case\"标记逻辑需要对照正文才能理解，caption自解释性不足。\n- **M4** [clarity]: Figure 4的y轴\"Significance proxy\"的定义在caption中模糊——如果是power-like的度量，应明确计算公式（如1 - p value的某种transformation）。\n- **M5** [notation]: Table 3中Originality OR的asterisk标注与Style OR的不完全一致——建议统一显著性标记格式。\n\n## Questions for Authors\n\n1. **NLI threshold sensitivity的极端情况**：Appendix E (Table 9)显示所有44种judge×axis×threshold配置的BT都significant (p < 0.05)。能否确认是否存在**任何**NLI threshold使某些Blindspot case消失？如果所有threshold都robust，这实际上是论文的一个强优势，但当前呈现方式不够突出。\n\n2. **Formality Style OR <1的解释**：Table 3中部分formality配置的Style OR<1（如GPT-4o form: OR=2.58但Qwen3 form: OR=2.31，Gemini form: OR=1.64）。更关键的是正文提到\"formality is a conditional effect, register is style OR <1\"。Style OR<1意味着style transformation反而**降低**了被选中的概率——这一反直觉结果如何机制性解释？\n\n3. **Bootstrap attenuation的interpretation**：Appendix J显示d_median ≈ -0.017在所有样本量下近乎恒定。这是否意味着在此数据上Likert ATE是**真正的零效应**而非merely underpowered？如果是true null，这对\"Blindspot的机制是attenuation还是amplification\"的讨论意味着什么？\n\n4. **GEE model的causal interpretation**：论文多处使用\"causal\"语言（如\"Controlled Style Decomposition\"中的\"controlled\"），但GEE模型本身是associational的。控制来自实验设计（rewriting保持content），而非统计模型。能否更精确地界定哪些inference是causal的、哪些是conditional association？\n\n## Missing References\n\n论文的相关工作覆盖面较好。建议补充：\n- **Luce (1959)** \"Individual Choice Behavior\" — BT模型的理论基础文献，与论文对BT IIA假设的讨论直接相关\n- **Bowman et al. (2015)** SNLI或**Williams et al. (2018)** MNLI — NLI gate是pipeline核心组件，但当前引用集中在DeBERTa技术文献，缺少对NLI任务本身局限性（如entailment与semantic equivalence的distinction）的文献支撑\n- 最新版本的pairwise evaluation方法论综述（如有），特别是关于BT model在LLM evaluation中的validity conditions\n\n## 主要优势\n\n1. **多方法交叉验证的说服力**：Table 2中7种测量方法——3种Likert-based（interval scaling, ordinal regression, nonparametric rank）、2种pairwise-based（BT, signed-rank）——全部Likert方法fail、全部pairwise方法pass。这种一致性不太可能是统计偶然。\n\n2. **GEE per-axis decomposition的方法论价值**：Table 3揭示verbosity是style-dominated（Style OR 5-13）而formality是conditional effect（受originality confound调节），这不仅描述了bias，更提供了可操作的诊断框架——告诉practitioners哪些轴的评估结果可以直接解读、哪些需要decomposition。\n\n3. **统计诊断的深度远超typical submission**：GEE correlation structure comparison（Appendix C, 9个judge×axis cells的QIC对比）、Bradley-Terry goodness-of-fit（Appendix H, chi-squared tests + direction asymmetry）、formal power analysis（Appendix K, required n for 80% power）、bootstrap attenuation curve（Appendix J, 7个subsample sizes）——每一项都不是走流程，而是genuine diagnostic。\n\n4. **实验设计的控制意识**：position-controlled comparison（Section 3.3, 每对出现两次消除position bias）、NLI gate（虽有验证不足的问题，但设计意图正确）、cross-rewriter validation（虽然范围有限）、negative control（虽然效应未完全消除）——展现了对confound识别的系统性思考。\n\n5. **实际影响清晰**：论文明确指出\"Likert-only audits may fail to register surface style-driven preferences that drive pairwise-based alignment pipelines (RLHF, DPO)\"（Section 6），为NLG evaluation pipeline设计提供了直接可操作的警示。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 927 · 2026-05-22T22:48:14.914920+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3766
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-22T22:48:29.131139+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 929 · 2026-05-22T22:48:29.181716+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 930 · 2026-05-22T22:48:32.546714+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 931 · 2026-05-22T22:48:32.598916+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 52
}
```

</details>

---


### Assistant

_source line 932 · 2026-05-22T22:48:34.542746+00:00_

已清理完毕。审稿完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 30

## Round 30

4 recorded events


### User

_source line 933 · 2026-05-22T22:49:15.950419+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿意见

**Overall**: 3.5 (Borderline Conference)
**Soundness**: 4/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5

### Must-Fix 问题

**N1** [critical] "Framework" 泛化声明与实际覆盖不匹配
- Section 1 contributions 第一条；Section 6 Conclusion
- CSD 定位为通用 per-axis style bias detection "framework"，但仅测试 formality、verbosity、register 三条轴（均为文本表层属性）。遇到 semantic-level 风格轴（hedging, humor, technicality）时 NLI 门控可能系统性拒绝合法 rewrite。
- 建议：降级为 "methodology" 或增加非表面风格轴实验。

**N2** [critical] 标题 "Blindspot" 隐含 attenuation 偏向，与三种解释并列的中立定位矛盾
- Title, Abstract 第一句, Section 6 Conclusion
- "Blindspot" 预设了 attenuation 解释，排斥 amplification 和 construct divergence。Introduction motivating example 暗示 Likert 判断是"错误的"。
- 建议：考虑更中性标题；Introduction 的例子后立即引入替代解释。

**N3** [critical] 核心发现的增量新颖性论证不足
- Section 1, Section 2 (Measurement Sensitivity)
- Forced-choice > absolute rating 是 Thurstone (1927) 经典结论。论文未充分论证在 LLM judge 领域"重新发现"这个现象的独立新颖性。
- 建议：强调 GEE decomposition 的 per-axis confound structure 差异作为 LLM-specific finding；将 novelty 重心从"发现 divergence"转向"quantifying and decomposing"。

### Should-Fix 问题

**W1** Abstract 数字密度过高
**W2** 与 RATE 的差异化论证薄弱
**W3** LLMBar 样本量小（n=100）对统计推断的限制
**W4** Construct divergence 解释发展不足
**W5** Claude Sonnet 4 负控制结果的讨论不充分

### Minor
1. Table 1 信息密度过高
2. Figure 2 DAG S→Q path 标注可能误导
3. "style bias" vs "style preference" vs "style sensitivity" 术语混用
4. Section 3.5 Design Rationale 位置突兀
5. Appendix 过多（A-S, 19个）

### Missing References
- Kim et al. (2024) "Prometheus 2"
- Luce (1959) "Individual Choice Behavior"
- Stureborg et al. (2024) 的 Likert inconsistency 发现

### 主要优势
1. 方法论严谨（三重控制）
2. 统计分析全面
3. GEE per-axis confound 结构差异是最有价值的增量发现
4. 跨4个独立judge复现
5. 诚实的 Limitations

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 934 · 2026-05-22T22:51:19.948879+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: \"Framework\"泛化声明与实际覆盖不匹配**\n同意这是一个实质性overclaim问题。论文仅测试formality、verbosity、register三条表层文本属性轴，但Section 1 contributions第一条将CSD定位为通用\"black-box framework for per-axis style bias detection\"。R2指出的NLI gate对semantic-level风格轴（hedging, humor, technicality）的系统性拒绝风险是真实的——这类rewriting必然改变语义内容，NLI entailment threshold 0.90会大面积过滤。Limitations（page 9）虽提到\"NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself\"，但这讨论的是gate的false negative问题（放过了quality shift），而非R2指出的false positive问题（拒绝了合法的semantic-style rewriting）。这是两个不同的限制维度，论文只覆盖了一个。\n\n降级为\"methodology\"或明确限定适用范围（\"surface-level stylistic attributes amenable to content-preserving rewriting\"）是合理建议。\n\n**[REBUT] R2-N2: 标题\"Blindspot\"隐含attenuation偏向**\n部分不同意R2对标题倾向性的判断。\"Blindspot\"描述的是观测层面的现象——Likert系统性地无法检测到pairwise能检测到的效应——而非机制层面的解释。无论底层机制是attenuation、amplification还是construct divergence，从practitioners的视角看，只用Likert就是存在一个\"盲区\"。这一术语选择类似于\"survivorship bias\"——它命名的是可观测模式，不预设产生机制。\n\n然而，R2指出Introduction的motivating example（page 1: \"What is the average height for a male?\"的Likert vs pairwise比较）确实暗示Likert判断是\"错误的\"而pairwise是\"正确的\"，这一点我同意存在framing bias。Section 5.1 \"Interpreting the divergence\"列出了三种non-exclusive解释（Likert attenuation、pairwise amplification、construct divergence），但这个三方并列出现在全文第7页，距离读者形成第一印象已太晚。\n\n建议保留标题\"Blindspot\"但在Introduction的motivating example之后**立即**（而非等到Section 5.1）简要引入三种解释的可能性，避免读者在前6页形成单向认知。这比改标题的成本更低且更有效。\n\n**[AGREE] R2-N3: 核心发现的增量新颖性论证不足**\n同意R2的判断，但程度上有所保留。R2正确指出forced-choice > absolute rating是Thurstone (1927)经典结论，\"Likert Blindspot\"在概念层面不是全新发现。Section 2 (Measurement Sensitivity in NLG Evaluation)引用了Stevens (1946)、Preston and Colman (2000)、Simms et al. (2019)、Krosnick (1999)等measurement theory文献，但**未充分论证在LLM judge这一特定领域重新量化此现象的independent contribution**。\n\n不过，R2自己在\"主要优势\"第3条中承认\"GEE per-axis confound结构差异是最有价值的增量发现\"。我认为论文的真正novelty确实在于：(1) GEE decomposition揭示style vs originality confound的轴间异质性（Table 3: verbosity Style OR 5-13 vs formality conditional effect）；(2) 这种异质性对practitioners的可操作含义（哪些轴的评估结果可直接解读，哪些需要decomposition）。论文当前的framing将novelty重心放在\"发现divergence\"（标题和Abstract前两句），而非\"quantifying and decomposing per-axis confound structures\"。\n\n建议按R2建议重构novelty narrative：标题和Abstract应突出decomposition的方法论贡献，将divergence发现降为motivating observation。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Abstract数字密度过高**\nAbstract包含η=0.17、>60%、7种统计方法、3个benchmark等密集数字。对于一篇以methodology为贡献的论文，Abstract应侧重conceptual message而非exhaustive数字。具体数字可移入Section 5的results presentation。\n\n**[REBUT] R2-W2: 与RATE差异化论证薄弱**\n不完全同意。论文在Section 2 (Style Bias Detection and Mitigation)和Section 1 contributions中对RATE的差异化论述包含三个维度：(1) CSD targets individual style axes rather than general attributes（Section 1: \"per-axis style decomposition\"）；(2) CSD measures bias through position-controlled pairwise comparison rather than Likert ATE（Section 3.3: Measurement Protocol详细描述了position-controlled design）；(3) CSD enforces content preservation via NLI entailment gating rather than post-hoc correction（Section 3.2: Content Preservation Verification，NLI gate的设计与RATE的post-hoc校正是根本性差异）。Section 5.1还直接与RATE对比了实验结果：\"Applying RATE's Likert ATE methodology... yields Cohen's d = 0.10, p = 0.33 (non-significant)\"，而CSD的pairwise方法检测到63.0% formal preference (p = 0.001)。\n\n差异化论证的问题更多在于Section 2的organization——RATE在Related Work中被分散在两处讨论，而非在一个dedicated对比段落中系统性地论证差异。建议在Section 2末尾增加一段集中对比，但认为现有内容已足够支撑差异化claim。\n\n**[AGREE] R2-W3: LLMBar样本量（n=100）对统计推断的限制**\n同意，且与我的审稿意见W5（样本外部效度论证不足）一致。100个instruction-response pairs虽然足以在统计上检测到observed effect sizes（Appendix K的power analysis确认了这一点），但LLMBar的task分布（短instruction-following tasks with human-verified quality labels）不代表LLM judge的全部使用场景。AlpacaEval和MT-Bench的partial replication（Table 1: \"confirmatory replication on selected configurations\"）提供了一定泛化支持，但这些replication是选择性的而非全面的。\n\n**[AGREE] R2-W4: Construct divergence解释发展不足**\n同意。Section 5.1列出了三种non-exclusive解释：(a) Likert attenuation, (b) pairwise amplification/forced-choice contamination, (c) construct divergence。但(c)仅用一句话概括（\"the two formats measure different constructs: Likert captures absolute quality difference, while pairwise captures ordinal preference\"），未发展为可检验的假说。如果construct divergence是正确解释，那么\"Blindspot\"就不是Likert的缺陷而是两种工具测量不同对象的自然结果——这对论文的practical implication narrative影响重大。论文应更深入地讨论在construct divergence解释下，practitioners应如何选择evaluation format。\n\n**[AGREE] R2-W5: Claude Sonnet 4负控制结果的讨论不充分**\n同意，且与我的N2（TOST Δ=15pp缺乏外部校准）直接相关。Claude Sonnet 4的BT=56.2%不是null effect，只是在Δ=15pp的宽松阈值下被判为\"等价\"。Appendix G对此是transparent的，但正文（Section 5.1后半部分提到Claude Sonnet 4时）的framing确实可能给读者留下\"该judge无style bias\"的印象。\n\n---\n\n### Minor Issues\n\n**[AGREE] R2-Minor-1: Table 1信息密度过高**\nTable 1在单个表中呈现5个judge × 3个axis × 3个benchmark × 4个统计量，确实需要仔细解码。拆分为per-benchmark子表或使用visual encoding（如heatmap）可提高可读性。\n\n**[REBUT] R2-Minor-2: Figure 2 DAG S→Q path标注可能误导**\n不认为这是误导。Figure 2 caption明确说明\"Assumed data-generating process (design rationale, not a claim of perfect identification)\"。DAG中S→Q path（style→quality）表示style rewriting可能inadvertently改变content quality——这正是NLI gate要阻断的通道。虚线标注已区分了被控制的vs未被控制的path。不过，如果R2指的是\"S→Q\"可能被误读为\"style causes quality\"（而非\"rewriting mechanism may alter quality\"），那一个更精确的edge label（如\"rewriting mechanism\"而非仅\"S→Q\"）可以澄清。\n\n**[AGREE] R2-Minor-3: 术语混用**\n\"style bias\"、\"style preference\"、\"style sensitivity\"在论文中确实未严格区分使用。作为measurement methodology论文，术语一致性对精确传达含义很重要。\n\n**[AGREE] R2-Minor-4: Section 3.5 Design Rationale位置突兀**\nDesign Rationale放在Method末尾（Section 3.5, page 5）确实打断了从Method到Experiments的自然流。内容上是必要的（解释DAG假设和causal identification strategy），但位置可移到Section 3.1-3.2之间作为设计动机，或合并到一个introductory paragraph。\n\n**[AGREE] R2-Minor-5: Appendix过多（A-S, 19个）**\n19个appendix确实过多。但这与论文的统计严谨度是trade-off的两面——许多appendix包含重要的robustness checks和diagnostics。建议合并同类appendix（如将C/H合为\"Model Diagnostics\"，将E/F/N合为\"NLI Gate Analyses\"）以减少数量而不丢失内容。\n\n---\n\n### Missing References\n\n**[AGREE]** Luce (1959) \"Individual Choice Behavior\" — 与我的审稿意见一致，这是BT模型的理论基础文献，直接相关于论文对IIA假设的讨论。\n\n**[AGREE]** Stureborg et al. (2024) 的Likert inconsistency发现 — 论文在Section 2已引用Stureborg et al. (2024)讨论了\"inconsistency and bias across evaluation formats\"，但可以更深入地对比其specific findings与本文的Blindspot现象。\n\n**[REBUT]** Kim et al. (2024) \"Prometheus 2\" — 该文献与本文的研究问题（measurement mode divergence）关联度有限。Prometheus 2聚焦于open-source judge model的evaluation quality，而非Likert-pairwise divergence问题。如果引用，应放在Section 2的judge model开发部分作为additional context，而非作为直接相关工作。\n\n---\n\n### 总结\n\nR2的三个Must-Fix中，N1（framework overclaim）和N3（novelty framing）我完全同意，N2（标题bias）我部分反驳——\"Blindspot\"描述现象而非机制，但同意Introduction的framing确实偏向attenuation解释，应提前引入替代解释。Should-Fix中W2（RATE差异化）我认为现有论证已基本充分但organization可改善，其余W1/W3/W4/W5我均同意。\n\n值得注意的是，R2给出Excitement 3/5（我给3.5/5），主要差异在于R2更重视novelty gap（Thurstone经典结论的重新发现），而我更看重GEE decomposition的方法论价值和practical implications。我认为如果论文按N3建议重构novelty narrative（从\"发现divergence\"转向\"quantifying and decomposing per-axis confound structures\"），Excitement评分可以提升。\n\n两位Reviewer的共识区域：(1) framework overclaim需要降级或限定范围；(2) 负控制讨论不充分；(3) 样本外部效度有限；(4) GEE decomposition是最有价值的贡献。分歧主要在标题选择和novelty定位。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: \"Framework\"泛化声明与实际覆盖不匹配**\n同意这是一个实质性overclaim问题。论文仅测试formality、verbosity、register三条表层文本属性轴，但Section 1 contributions第一条将CSD定位为通用\"black-box framework for per-axis style bias detection\"。R2指出的NLI gate对semantic-level风格轴（hedging, humor, technicality）的系统性拒绝风险是真实的——这类rewriting必然改变语义内容，NLI entailment threshold 0.90会大面积过滤。Limitations（page 9）虽提到\"NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself\"，但这讨论的是gate的false negative问题（放过了quality shift），而非R2指出的false positive问题（拒绝了合法的semantic-style rewriting）。这是两个不同的限制维度，论文只覆盖了一个。\n\n降级为\"methodology\"或明确限定适用范围（\"surface-level stylistic attributes amenable to content-preserving rewriting\"）是合理建议。\n\n**[REBUT] R2-N2: 标题\"Blindspot\"隐含attenuation偏向**\n部分不同意R2对标题倾向性的判断。\"Blindspot\"描述的是观测层面的现象——Likert系统性地无法检测到pairwise能检测到的效应——而非机制层面的解释。无论底层机制是attenuation、amplification还是construct divergence，从practitioners的视角看，只用Likert就是存在一个\"盲区\"。这一术语选择类似于\"survivorship bias\"——它命名的是可观测模式，不预设产生机制。\n\n然而，R2指出Introduction的motivating example（page 1: \"What is the average height for a male?\"的Likert vs pairwise比较）确实暗示Likert判断是\"错误的\"而pairwise是\"正确的\"，这一点我同意存在framing bias。Section 5.1 \"Interpreting the divergence\"列出了三种non-exclusive解释（Likert attenuation、pairwise amplification、construct divergence），但这个三方并列出现在全文第7页，距离读者形成第一印象已太晚。\n\n建议保留标题\"Blindspot\"但在Introduction的motivating example之后**立即**（而非等到Section 5.1）简要引入三种解释的可能性，避免读者在前6页形成单向认知。这比改标题的成本更低且更有效。\n\n**[AGREE] R2-N3: 核心发现的增量新颖性论证不足**\n同意R2的判断，但程度上有所保留。R2正确指出forced-choice > absolute rating是Thurstone (1927)经典结论，\"Likert Blindspot\"在概念层面不是全新发现。Section 2 (Measurement Sensitivity in NLG Evaluation)引用了Stevens (1946)、Preston and Colman (2000)、Simms et al. (2019)、Krosnick (1999)等measurement theory文献，但**未充分论证在LLM judge这一特定领域重新量化此现象的independent contribution**。\n\n不过，R2自己在\"主要优势\"第3条中承认\"GEE per-axis confound结构差异是最有价值的增量发现\"。我认为论文的真正novelty确实在于：(1) GEE decomposition揭示style vs originality confound的轴间异质性（Table 3: verbosity Style OR 5-13 vs formality conditional effect）；(2) 这种异质性对practitioners的可操作含义（哪些轴的评估结果可直接解读，哪些需要decomposition）。论文当前的framing将novelty重心放在\"发现divergence\"（标题和Abstract前两句），而非\"quantifying and decomposing per-axis confound structures\"。\n\n建议按R2建议重构novelty narrative：标题和Abstract应突出decomposition的方法论贡献，将divergence发现降为motivating observation。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Abstract数字密度过高**\nAbstract包含η=0.17、>60%、7种统计方法、3个benchmark等密集数字。对于一篇以methodology为贡献的论文，Abstract应侧重conceptual message而非exhaustive数字。具体数字可移入Section 5的results presentation。\n\n**[REBUT] R2-W2: 与RATE差异化论证薄弱**\n不完全同意。论文在Section 2 (Style Bias Detection and Mitigation)和Section 1 contributions中对RATE的差异化论述包含三个维度：(1) CSD targets individual style axes rather than general attributes（Section 1: \"per-axis style decomposition\"）；(2) CSD measures bias through position-controlled pairwise comparison rather than Likert ATE（Section 3.3: Measurement Protocol详细描述了position-controlled design）；(3) CSD enforces content preservation via NLI entailment gating rather than post-hoc correction（Section 3.2: Content Preservation Verification，NLI gate的设计与RATE的post-hoc校正是根本性差异）。Section 5.1还直接与RATE对比了实验结果：\"Applying RATE's Likert ATE methodology... yields Cohen's d = 0.10, p = 0.33 (non-significant)\"，而CSD的pairwise方法检测到63.0% formal preference (p = 0.001)。\n\n差异化论证的问题更多在于Section 2的organization——RATE在Related Work中被分散在两处讨论，而非在一个dedicated对比段落中系统性地论证差异。建议在Section 2末尾增加一段集中对比，但认为现有内容已足够支撑差异化claim。\n\n**[AGREE] R2-W3: LLMBar样本量（n=100）对统计推断的限制**\n同意，且与我的审稿意见W5（样本外部效度论证不足）一致。100个instruction-response pairs虽然足以在统计上检测到observed effect sizes（Appendix K的power analysis确认了这一点），但LLMBar的task分布（短instruction-following tasks with human-verified quality labels）不代表LLM judge的全部使用场景。AlpacaEval和MT-Bench的partial replication（Table 1: \"confirmatory replication on selected configurations\"）提供了一定泛化支持，但这些replication是选择性的而非全面的。\n\n**[AGREE] R2-W4: Construct divergence解释发展不足**\n同意。Section 5.1列出了三种non-exclusive解释：(a) Likert attenuation, (b) pairwise amplification/forced-choice contamination, (c) construct divergence。但(c)仅用一句话概括（\"the two formats measure different constructs: Likert captures absolute quality difference, while pairwise captures ordinal preference\"），未发展为可检验的假说。如果construct divergence是正确解释，那么\"Blindspot\"就不是Likert的缺陷而是两种工具测量不同对象的自然结果——这对论文的practical implication narrative影响重大。论文应更深入地讨论在construct divergence解释下，practitioners应如何选择evaluation format。\n\n**[AGREE] R2-W5: Claude Sonnet 4负控制结果的讨论不充分**\n同意，且与我的N2（TOST Δ=15pp缺乏外部校准）直接相关。Claude Sonnet 4的BT=56.2%不是null effect，只是在Δ=15pp的宽松阈值下被判为\"等价\"。Appendix G对此是transparent的，但正文（Section 5.1后半部分提到Claude Sonnet 4时）的framing确实可能给读者留下\"该judge无style bias\"的印象。\n\n---\n\n### Minor Issues\n\n**[AGREE] R2-Minor-1: Table 1信息密度过高**\nTable 1在单个表中呈现5个judge × 3个axis × 3个benchmark × 4个统计量，确实需要仔细解码。拆分为per-benchmark子表或使用visual encoding（如heatmap）可提高可读性。\n\n**[REBUT] R2-Minor-2: Figure 2 DAG S→Q path标注可能误导**\n不认为这是误导。Figure 2 caption明确说明\"Assumed data-generating process (design rationale, not a claim of perfect identification)\"。DAG中S→Q path（style→quality）表示style rewriting可能inadvertently改变content quality——这正是NLI gate要阻断的通道。虚线标注已区分了被控制的vs未被控制的path。不过，如果R2指的是\"S→Q\"可能被误读为\"style causes quality\"（而非\"rewriting mechanism may alter quality\"），那一个更精确的edge label（如\"rewriting mechanism\"而非仅\"S→Q\"）可以澄清。\n\n**[AGREE] R2-Minor-3: 术语混用**\n\"style bias\"、\"style preference\"、\"style sensitivity\"在论文中确实未严格区分使用。作为measurement methodology论文，术语一致性对精确传达含义很重要。\n\n**[AGREE] R2-Minor-4: Section 3.5 Design Rationale位置突兀**\nDesign Rationale放在Method末尾（Section 3.5, page 5）确实打断了从Method到Experiments的自然流。内容上是必要的（解释DAG假设和causal identification strategy），但位置可移到Section 3.1-3.2之间作为设计动机，或合并到一个introductory paragraph。\n\n**[AGREE] R2-Minor-5: Appendix过多（A-S, 19个）**\n19个appendix确实过多。但这与论文的统计严谨度是trade-off的两面——许多appendix包含重要的robustness checks和diagnostics。建议合并同类appendix（如将C/H合为\"Model Diagnostics\"，将E/F/N合为\"NLI Gate Analyses\"）以减少数量而不丢失内容。\n\n---\n\n### Missing References\n\n**[AGREE]** Luce (1959) \"Individual Choice Behavior\" — 与我的审稿意见一致，这是BT模型的理论基础文献，直接相关于论文对IIA假设的讨论。\n\n**[AGREE]** Stureborg et al. (2024) 的Likert inconsistency发现 — 论文在Section 2已引用Stureborg et al. (2024)讨论了\"inconsistency and bias across evaluation formats\"，但可以更深入地对比其specific findings与本文的Blindspot现象。\n\n**[REBUT]** Kim et al. (2024) \"Prometheus 2\" — 该文献与本文的研究问题（measurement mode divergence）关联度有限。Prometheus 2聚焦于open-source judge model的evaluation quality，而非Likert-pairwise divergence问题。如果引用，应放在Section 2的judge model开发部分作为additional context，而非作为直接相关工作。\n\n---\n\n### 总结\n\nR2的三个Must-Fix中，N1（framework overclaim）和N3（novelty framing）我完全同意，N2（标题bias）我部分反驳——\"Blindspot\"描述现象而非机制，但同意Introduction的framing确实偏向attenuation解释，应提前引入替代解释。Should-Fix中W2（RATE差异化）我认为现有论证已基本充分但organization可改善，其余W1/W3/W4/W5我均同意。\n\n值得注意的是，R2给出Excitement 3/5（我给3.5/5），主要差异在于R2更重视novelty gap（Thurstone经典结论的重新发现），而我更看重GEE decomposition的方法论价值和practical implications。我认为如果论文按N3建议重构novelty narrative（从\"发现divergence\"转向\"quantifying and decomposing per-axis confound structures\"），Excitement评分可以提升。\n\n两位Reviewer的共识区域：(1) framework overclaim需要降级或限定范围；(2) 负控制讨论不充分；(3) 样本外部效度有限；(4) GEE decomposition是最有价值的贡献。分歧主要在标题选择和novelty定位。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 935 · 2026-05-22T22:51:23.564198+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3615
}
```

</details>

---


### Assistant

_source line 936 · 2026-05-22T22:51:31.595596+00:00_

交叉回应已提交。

R2的三个Must-Fix中：N1（framework overclaim）和N3（novelty framing）完全同意，N2（标题"Blindspot"隐含attenuation偏向）部分反驳——"Blindspot"描述可观测现象而非机制，但同意Introduction应提前引入替代解释。Should-Fix中仅W2（RATE差异化）部分反驳，其余均同意。

两位Reviewer的共识：framework需降级、负控制讨论不足、样本泛化性有限、GEE decomposition是核心贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 31

## Round 31

66 recorded events


### User

_source line 937 · 2026-05-23T05:25:29.140263+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计方法**。

## 论文信息
- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf`
- **目标 venue**: EMNLP 2026 (ARR May cycle)
- **Deadline**: 2026-05-25
- **格式**: Long paper, 8页正文限制 + 无限参考文献, ACL模板, double-blind
- **Limitations**: mandatory, 不计入页数限制
- **匿名规则**: double-blind（论文中不能有作者身份信息）

## 你的审查侧重

请重点评估以下方面：

1. **方法论严谨性**：
   - CSD pipeline 的设计是否合理？NLI gate 作为 content preservation 的验证手段是否充分？
   - 因果推断框架（DAG）的假设是否合理？"interventional rather than formal causal evidence" 这个定位是否准确？
   - Style-controlled rewriting 是否真的能隔离单一 style axis？cross-axis contamination 的处理是否充分？

2. **实验设计**：
   - 4 个 target judges + 1 个 negative control 的选择是否合理？样本量（n=88, n=355）是否充分？
   - 3 个 benchmark（LLMBar n=100, AlpacaEval n=100, MT-Bench n=80）的选择和覆盖范围
   - Evaluator-producer overlap（Qwen3-32B 同时做 rewriter 和 judge）的处理是否充分？
   - Negative control (Claude Sonnet 4) 的 equivalence testing 是否严谨？

3. **统计方法**：
   - Bradley-Terry model 的使用是否合理？IIA 假设的处理？
   - GEE conditional decomposition 的模型选择（exchangeable correlation）是否合理？
   - Holm-Bonferroni 多重比较校正的 family 定义是否恰当？
   - Bootstrap CI 的方法和参数选择
   - Power analysis 的合理性

4. **可重复性**：
   - 实验细节是否充分？是否有足够信息让其他研究者重复实验？
   - 代码和数据承诺 "released upon acceptance"——是否有任何重复性隐患？

请按 EMNLP 2026 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Minor Issues。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 938 · 2026-05-23T05:25:37.702421+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 939 · 2026-05-23T05:25:37.753092+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 940 · 2026-05-23T05:25:42.127243+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 941 · 2026-05-23T05:25:42.680066+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR review form scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR review form scoring dimensions"
  }
}
```

</details>

---


### Tool call

_source line 942 · 2026-05-23T05:25:44.796831+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 943 · 2026-05-23T05:25:46.958551+00:00_

Web search results for query: "EMNLP 2026 ARR review form scoring dimensions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, I found information about the ARR review form scoring dimensions for EMNLP 2026:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

The search results indicate these are the main scoring dimensions used in the ARR review form. Additionally, reviewers are able to indicate their confidence score in the ARR form, and reproducibility scores should be justified, suggesting these are additional dimensions reviewers may address in their evaluations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 4278
}
```

</details>

---


### Tool result

_source line 944 · 2026-05-23T05:25:52.840107+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

I found information about ACL ARR 2026 reviewer guidelines and review form criteria. Here are the key findings:

## Review Form Criteria

For main papers, the main criteria include soundness and novelty, while for Findings papers the main criteria are soundness and reproducibility, with conference recomm
…[truncated 1283 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 10712
}
```

</details>

---


### Tool result

_source line 945 · 2026-05-23T05:25:53.898397+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 588.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 553.4}], \"total_pages\": 19, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/a
…[truncated 77 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9101
}
```

</details>

---


### Tool call

_source line 946 · 2026-05-23T05:26:01.485602+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 or other), descriptions for each score level, and any other required fields. I need the exact criteria for Soundness, Excitement, Overall Assessment, Confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 or other), descriptions for each score level, and any other required fields. I need the exact criteria for Soundness, Excitement, Overall Assessment, Confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 947 · 2026-05-23T05:26:01.837096+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 948 · 2026-05-23T05:26:02.493514+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-23T05:26:03.297622+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1460
}
```

</details>

---


### Tool call

_source line 950 · 2026-05-23T05:26:03.400127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 951 · 2026-05-23T05:26:03.905338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-23T05:26:03.905784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-23T05:26:04.611536+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1211
}
```

</details>

---


### Tool result

_source line 954 · 2026-05-23T05:26:04.963322+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1057
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-23T05:26:10.079802+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. Reviewer Confidence
**Scale: 1-5**
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

## 2. Soundness
**Scale: 1-5 (with half-point increments)**
- **5:** "Excellent: This study is one of the most thorough I have seen, given its type."
- **4:** "Strong: This study provides sufficient support for all of its claims."
- **3:** "Acceptable: This study provides sufficient support for its main claims."
- **2:** "Poor: Some of the main claims are not sufficiently supported."
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. Excitement
**Scale: 1-5 (with half-point increments)**
- **5:** "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4:** "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3:** "Interesting: I might mention some points of this paper to others."
- **2:** "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1:** "Not Exciting: this paper does not resonate with me."

## 4. Overall Assessment
**Scale: 1-5 (with half-point increments)**
- **5:** "Consider for Award: up to top 2.5% papers"
- **4.5:** "Borderline Award"
- **4:** "Conference: could be accepted to an ACL conference"
- **3.5:** "Borderline Conference"
- **3:** "Findings: could be accepted to the Findings of the ACL"
- **2.5:** "Borderline Findings"
- **2:** "Resubmit next cycle: needs substantial revisions"
- **1.5:** "Resubmit after next cycle: needs revisions that cannot be completed by next ARR cycle"
- **1:** 
…[truncated 427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8594
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-23T05:26:15.863942+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 957 · 2026-05-23T05:26:16.416604+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 958 · 2026-05-23T05:26:16.770495+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 959 · 2026-05-23T05:26:16.770968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 960 · 2026-05-23T05:26:17.324014+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 961 · 2026-05-23T05:26:17.324429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 962 · 2026-05-23T05:26:17.776282+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool result

_source line 963 · 2026-05-23T05:26:18.129701+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 964 · 2026-05-23T05:26:25.370268+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "9-19",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "9-19",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 965 · 2026-05-23T05:26:26.576785+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 536.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.7}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 447.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 431.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.6}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images
…[truncated 767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1206
}
```

</details>

---


### Tool call

_source line 966 · 2026-05-23T05:26:29.438476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 967 · 2026-05-23T05:26:29.990773+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 968 · 2026-05-23T05:26:30.845490+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool result

_source line 969 · 2026-05-23T05:26:30.848113+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 970 · 2026-05-23T05:26:30.848490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 971 · 2026-05-23T05:26:31.202235+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 972 · 2026-05-23T05:26:32.058619+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1210
}
```

</details>

---


### Tool result

_source line 973 · 2026-05-23T05:26:32.512448+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1310
}
```

</details>

---


### Tool call

_source line 974 · 2026-05-23T05:26:38.303958+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 975 · 2026-05-23T05:26:39.108736+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 976 · 2026-05-23T05:26:39.109098+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 977 · 2026-05-23T05:26:39.611455+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 978 · 2026-05-23T05:26:39.914350+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 979 · 2026-05-23T05:26:39.914829+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 980 · 2026-05-23T05:26:40.474330+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 862
}
```

</details>

---


### Tool result

_source line 981 · 2026-05-23T05:26:41.430089+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1515
}
```

</details>

---


### Tool call

_source line 982 · 2026-05-23T05:26:46.164462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 983 · 2026-05-23T05:26:46.819180+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 984 · 2026-05-23T05:26:47.220753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 985 · 2026-05-23T05:26:47.472693+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool result

_source line 986 · 2026-05-23T05:26:48.129805+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool result

_source line 987 · 2026-05-23T05:26:48.130566+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-23T05:30:02.999713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-23T05:30:03.050501+00:00_

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
19	\title{The Likert Blindspot: Measurement-Mode Divergence\\in LLM Judge Style Evaluation}
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
45	The primary open question is whether pairwise comparison detects genuine style bias or amplifies micro-preferences inherent in the format.
…[truncated 4649 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 990 · 2026-05-23T05:30:11.740877+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 991 · 2026-05-23T05:30:11.741407+00:00_

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
12	Bradley-Terry parameters \citep{bradley1952rank,luce1959individual} are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.\footnote{In binary-choice BT models, IIA is structurally satisfied; the direction asymmetry in Appendix~\ref{app:bt_gof} (formality: formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$; verbosity: $p = 0.453$) reflects heterogeneous treatment effects across style directions rather than IIA violation.}
13	All bootstrap confidence intervals are percentile CIs from 10{,}000 pair-level resamples with seed 42.
14	GEE models use exchangeable working correlation with sandwich standard errors (robust to correlation misspecification), justified by near-zero estimat
…[truncated 17463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 992 · 2026-05-23T05:30:11.841931+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 993 · 2026-05-23T05:30:11.992884+00:00_

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
18	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large fine-tuned on MNLI \citep{williams2018broad} with an entailment threshold of 0.90, selected as the threshold above which NLI performance plateaus (Appendix~\ref{app:nli_sweep}).
19	For axes that preserve information density (formality, register), we apply standard bidirectional entailment: both NLI(original $\to$ rewrite) and NLI(rewrite $\to$ original) must exc
…[truncated 5213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 994 · 2026-05-23T05:30:18.115664+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-23T05:30:18.166255+00:00_

1	\appendix
2	
3	\noindent\emph{Organization: design rationale (A$^*$), confound analysis (A--B), model diagnostics (C), independence tests (D), gate validation (E--F), equivalence testing (G), statistical details (H--K), sensitivity analyses (L--N), artifact controls (O), implementation (P), multiplicity (Q), cross-axis contamination (R), human annotation agreement (S), Claude cross-benchmark (T).}
4	
5	\section{Design Rationale}
6	\label{app:design_rationale}
7	
8	Three variables govern the observed judge score $Y$: the style attribute $S$ (e.g., formality), the original content quality $Q$, and the judge's internal scoring function.
9	Both $S$ and $Q$ causally influence $Y$; the goal of CSD is to approximate the effect $S \to Y$ while blocking confounding through $Q$.
10	Style-controlled rewriting generates a text pair that differs along a single style axis, but any rewriting operation risks inadvertently altering content quality ($R \to Q$).
11	The NLI gate (\S\ref{sec:nli_gate}) blocks this path, yielding a controlled estimate of the $S \to Y$ effect.
12	Our approach provides interventional rather than formal causal evidence: we do not claim that the DAG in Figure~\ref{fig:dag} is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework.
13	``Controlled'' in this context refers to experimentally controlled rewriting conditions, not formal causal identification in the potential-outcomes sense.
14	Our identification rests on three operational assumptions: (i)~the NLI gate approximates content preservation, blocking the $R \to Q$ path; (ii)~position swapping controls for presentation-order effects; and (iii)~the style rewrite introduces no systematic differences beyond the target axis.
15	
16	\section{Direction Asymmetry and Quality Confounding}
17	\label{app:direction}
18	
19	The formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\% of formal-is-r
…[truncated 8523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-23T05:30:23.284754+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "offset": "150",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
    "offset": "150",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 997 · 2026-05-23T05:30:23.335474+00:00_

150	GEE Orig OR ($p$) & 1.61 (n.s.) & 0.49 (n.s.) \\
151	\bottomrule
152	\end{tabular}
153	\end{table}
154	
155	\paragraph{Formality (Table~\ref{tab:rewriter_indep_form}).}
156	GPT-4o rewriter produces formality-manipulated pairs yielding BT $64.4\%$ $[56.1, 72.8]$, statistically indistinguishable from the Qwen3-32B baseline ($66.5\%$ $[58.5, 73.9]$; $\Delta = -2.1$pp).
157	The Likert Blindspot replicates with the independent rewriter ($p = 0.184$, n.s.).
158	
159	\begin{table}[h]
160	\centering
161	\small
162	\caption{Rewriter independence test: formality axis, Qwen3-32B judge.}
163	\label{tab:rewriter_indep_form}
164	\begin{tabular}{lcc}
165	\toprule
166	 & GPT-4o Rewriter & Qwen3 Rewriter \\
167	\midrule
168	NLI pass rate & 90/100 (90\%) & 88/100 (88\%) \\
169	BT $P$ [95\% CI] & .644 [.561, .728] & .665 [.585, .739] \\
170	Likert $d$ ($p$) & $-$.081 (.184) & .011 (.908) \\
171	Blindspot & Yes & Yes \\
172	\bottomrule
173	\end{tabular}
174	\end{table}
175	
176	\section{NLI Threshold Sensitivity Sweep}
177	\label{app:nli_sweep}
178	
179	Table~\ref{tab:nli_sweep} reports BT win probabilities across 11 NLI entailment thresholds for all four judge$\times$axis configurations.
180	All 44 combinations are significant ($p < 0.05$), and within each configuration BT varies by at most 3pp, ruling out threshold selection bias.
181	The stability reflects the bimodal NLI score distribution: most pairs score above 0.95 or below 0.30, so thresholds between 0.50 and 0.95 admit nearly identical pair sets.
182	
183	\begin{table}[h]
184	\centering
185	\small
186	\caption{BT win probability across NLI thresholds. All 44 cells significant ($p < 0.05$). $n$: pairs passing threshold.}
187	\label{tab:nli_sweep}
188	\begin{tabular}{@{}rcccc@{}}
189	\toprule
190	Thresh & \multicolumn{2}{c}{Formality BT} & \multicolumn{2}{c}{Verbosity BT} \\
191	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
192	 & Qwen3 & GPT-4o & Qwen3 & GPT-4o \\
193	\midrule
194	.50 & .648 & .615 & .770 & .768 \\
195	.55 & .648 &
…[truncated 9375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-23T05:32:32.904082+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 方法论扎实、统计处理详尽的诊断性工作，核心发现（Likert-pairwise divergence）有实证支撑且具实践意义，但对 divergence 的因果归因不够审慎、negative control 等效检验统计力不足、style axis 覆盖有限，使得结论的普适性存疑。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5 / 5 | 核心方法（CSD pipeline + GEE decomposition）设计合理，7 种统计方法互相验证；但 NLI gate 与人工标注的一致性仅 moderate（κ=0.32-0.44），negative control 的 TOST 在 Δ=10pp 时失效（power≈42%），且对 divergence 的三种解释（attenuation / amplification / construct divergence）未能决定性区分，削弱了 \"Likert Blindspot\" 这一因果性命名的合理性。 |\n| **Excitement** | 3.5 / 5 | 问题重要且切中实践痛点（RLHF/DPO 依赖 pairwise，evaluation 依赖 Likert），CSD 方法具有 reusable tool 价值；但论文主要 *诊断* 了问题而未提供 mitigation 路径，且仅覆盖 2 个 primary style axis，对社区的指导性有限。 |\n| **Reproducibility** | 4 / 5 | 实现细节充分（Appendix R 列出模型版本、温度、seed 等），BT CI 和 GEE CI 均完整报告；代码和数据承诺 \"released upon acceptance\" 但当前不可用。 |\n| **Confidence** | 4 / 5 | 本人熟悉 Bradley-Terry 模型、GEE、等效检验等统计方法，仔细核查了论文中的统计声明。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Likert Blindspot 的因果归因过度——论文自身证据无法排除 \"construct divergence\" 解释\n\n- **具体位置**：Section 5.1（§95-101 experiments.tex）、Title、Abstract line 1-4\n- **问题**：论文命名为 \"The Likert Blindspot\"，暗示 Likert 有 *缺陷*（blindspot = 盲区），但 Section 5.1 自己列出了三种 non-exclusive 解释：(a) Likert attenuation, (b) pairwise amplification, (c) construct divergence。论文承认 \"the attenuation evidence (d→0 at n=355) is necessary but not sufficient for causal identification\"，也承认 \"definitive resolution requires human evaluation comparing Likert and pairwise judgments on identical pairs\"（Limitations）。在这种无法区分的情况下，Title 和 framing 强烈偏向解释 (a)（Likert 有缺陷），而非中性的 \"measurement-mode divergence\"（虽然副标题包含此词，但 \"Blindspot\" 的修辞效果远强于副标题）。\n  \n  更关键的是：pairwise comparison 相比 absolute rating 具有更高判别力是 psychometrics 自 Thurstone (1927) 以来的已知现象——论文自身也引用了此文。power analysis 显示 Likert 需要 4-206× 的样本量才能检测到 BT 捕获的效应——这 *完全一致于* 相对判断 vs 绝对判断的已知灵敏度差异，不需要 \"blindspot\" 这一因果性解释。论文需要更充分地论证：为什么观察到的 divergence *不仅仅是* 已知的 format sensitivity 差异？\n  \n- **为什么影响接收**：标题和核心 framing 的因果暗示超出了实验证据的支撑范围，是 overclaiming。\n- **建议修改方向**：\n  1. 在 Introduction 和 Analysis 中给 construct divergence 解释同等的篇幅和权重，而非将其作为 Limitations 的一个段落\n  2. 明确讨论 Thurstone (1927) 的 discriminability 差异如何与本文发现对齐或区分\n  3. 考虑将 \"Blindspot\" 改为更中性的术语（如 \"Likert-Pairwise Gap\"），或在正文中明确定义 \"Blindspot\" 为一个操作性描述（divergence 现象的名称）而非因果性声明\n\n---\n\n**N2** [critical] Negative control (Claude Sonnet 4) 的等效检验统计力严重不足\n\n- **具体位置**：Appendix G（Table 9, app:claude_tost）；Section 5.1 第 97 行\n- **问题**：Claude Sonnet 4 作为 negative control 是实验设计的关键支柱——用于证明 \"有的 judge 不展示 Blindspot，因此 Blindspot 不是 format 的固有属性\"。但 TOST 等效检验在 Δ=15pp 时才达到显著（p=0.010），而 15pp 对应的 BT=65% 在实践中是一个 *相当大* 的偏好差异。在 Δ=10pp（一个更合理的实际显著性门槛）时，TOST 不显著（p=0.156, power≈42%）。论文自己承认 \"the minimum equivalence margin achieving 80% power at n=88 is Δ=15.7pp\"。\n\n  这意味着：我们无法在 n=88 的情况下区分 \"Claude 没有 style bias\" 和 \"Claude 有 10pp 的 style bias\"。Claude 的 BT 值为 56.2%（formality）和 54.1%（verbosity），虽然接近 50%，但 6.2pp 的偏差在 n=88 下完全可能反映真实的 moderate effect。\n  \n- **为什么影响接收**：negative control 的有效性直接关系到 \"Blindspot 是 judge-specific 而非 format-inherent\" 这一核心论点。如果 negative control 失效，则 N1 中的 \"construct divergence\" 解释变得更强。\n- **建议修改方向**：\n  1. 扩大 negative control 样本量至少到 n=200+，使 Δ=10pp 的 TOST 达到合理 power\n  2. 或者诚实地将 negative control 结论降级为 \"suggestive but underpowered\"，不将其作为排除 format-inherent 解释的主要证据\n  3. 增加第二个 negative control judge 以增强说服力\n\n---\n\n**N3** [critical] 样本量 n=88 下 GEE decomposition 的可靠性存疑\n\n- **具体位置**：Table 2（主文 p.7）；Section 4.1；Appendix D\n- **问题**：GEE conditional decomposition 是本文方法的核心创新之一——将 BT 的整体偏好分解为 style 和 originality 两个分量。但在 n=88（176 observations for binary outcome）的条件下，logistic GEE 需要估计的参数虽然少（intercept + 2 predictors），但 CI 极宽：例如 Qwen3 verbosity Style OR = 13.10 [5.62, 30.55]——95% CI 跨越了将近 6 倍的范围。Gemini formality Style OR = 1.64 [0.91, 2.98] 的 CI 包含 1.0，即不显著。\n\n  更重要的是，n=88 下交互效应检验的 power 极低。Table 4 报告所有交互项 p > 0.13，但 OR 值波动很大（0.45 到 2.60），这些 p 值更可能反映 power 不足而非真正的 null。论文不能基于 non-significant interaction 就断言 additive model 正确。\n  \n- **为什么影响接收**：GEE 是区分 \"style-dominated\" vs \"quality-confounded\" 的唯一工具。如果在 n=88 下 GEE 的 effect size 估计不稳定（n=88 到 n=355 的 Qwen3 formality Style OR 从 4.20 降到 2.15，缩水 49%），那么基于小样本 GEE 得出的 per-judge regime classification 的可靠性令人怀疑。\n- **建议修改方向**：\n  1. 对所有 judge×axis 组合进行 n=355 级别的 scaled replication（目前只有 Qwen3 formality 做了）\n  2. 至少报告 GEE 的 power analysis 或 minimum detectable OR\n  3. 讨论 n=88→n=355 时 Qwen3 Style OR 缩水 49% 的含义——是否其他 judge 的 OR 也可能被高估？\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Style axis 覆盖窄（2 个 primary + 1 个 exploratory），限制了方法的普适性声明\n\n- **具体位置**：Section 3.1；Limitations 段落 3（line 56-62 main.tex）\n- **问题**：CSD 作为 \"black-box diagnostic methodology\" 被提出，但仅在 formality 和 verbosity 上充分验证。Register 是 exploratory pilot（且有 evaluator-producer overlap）。论文 Limitations 承认 hedging/humor/technicality 等语义级 axes 会被 NLI gate 系统性拒绝（55% rejection rate for tone axis pilot），这实际上将 CSD 限制在 surface-level stylistic attributes。但 Abstract 和 Introduction 的 framing 没有充分反映这一限制。\n- **建议**：在 Abstract 中加入 \"surface-level style axes\" 的限定语；讨论 CSD 对语义密集型 style axes 的 fundamental limitation。\n\n**W2** [warning] Cross-axis contamination 中 FK grade 变化的处理不够严谨\n\n- **具体位置**：Appendix T (Table 19)\n- **问题**：Verbosity rewrites 导致 FK grade d=0.50（medium effect），论文将其归因于 \"sentence length dependence\"。但 FK grade 同时反映 formality 相关的词汇复杂度，d=0.50 的 cross-axis 泄漏对于一个声称隔离单一 axis 的方法来说并非 trivial。论文的解释（句子长度的 artifact）是合理的但未被正式验证——例如，可以在控制句子长度后重新计算 FK grade shift。\n- **建议**：对 FK grade 做 length-controlled 分析，或至少讨论这个 d=0.50 对 formality×verbosity 交互的潜在影响。\n\n**W3** [warning] Evaluator-producer overlap 的 mitigation 只测试了一个替代 rewriter\n\n- **具体位置**：Appendix E (Table 6, Table 7)\n- **问题**：Qwen3-32B 同时做 rewriter 和 judge 是一个 known confound。论文用 GPT-4o 作为替代 rewriter 进行 independence test——结果显示 Style OR 下降 22%（13.10→10.17 for verbosity）。这是一个有意义的 check，但：(a) 只测试了一个替代配置；(b) 22% 的 OR 下降并不小；(c) 没有用第三个 rewriter 确认趋势是否稳定。\n- **建议**：增加至少一个额外的 rewriter（如 Llama 或 Gemini）做 independence test，或至少讨论 22% 下降的上界含义。\n\n**W4** [warning] IIA assumption 的讨论不充分\n\n- **具体位置**：Section 4.1 footnote（experiments.tex line 12）\n- **问题**：论文在脚注中声称 \"In binary-choice BT models, IIA is structurally satisfied\"，然后将 formality 的 direction asymmetry 解释为 \"heterogeneous treatment effects across style directions rather than IIA violation\"。但 IIA 的 structural satisfaction 仅在每对选手只比一次的情况下成立。在本文设计中，同一文本对在不同 style conditions 下反复出现，共享 source text 带来的依赖性可能系统性违反 IIA。GEE 部分用了 exchangeable correlation 来处理组内相关，但 BT model 本身没有类似的修正。\n- **建议**：在正文而非脚注中讨论 IIA，并明确说明 GEE 如何补充 BT 在这方面的不足。\n\n**W5** [warning] 100-point continuous Likert scale 实验仅用了一个 judge\n\n- **具体位置**：Appendix O\n- **问题**：100-point scale 实验（旨在排除 scale granularity 解释）仅在 Qwen3-32B 上进行。如果 Blindspot 的表现因 judge 而异（如 Gemini 的 formality 就明显更弱），单一 judge 的 100-point 实验不足以支持 \"granularity is not the issue\" 的一般性结论。\n- **建议**：至少在两个 judge 上 replicate 100-point scale 实验。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 1 排版密度过高**：15 行结果 + 6 行脚注在一个 Table 中，阅读体验较差。建议将 LLMBar primary results 和 cross-benchmark replication 分为两个表。\n2. **\"style bias\" vs \"style sensitivity\" 措辞不一致**：两个术语在文中交替使用但含义略有不同（bias 暗示方向性，sensitivity 暗示双向的响应性）。建议统一或明确区分。\n3. **Figure 2 (DAG) 的 dashed orange S→Q path** 标为 \"residual confound\"，但 caption 说 \"style may influence perceived quality through channels the NLI gate cannot block\"——这条路径实际上是一个 *acknowledged unblocked confounder*，建议在 caption 中更明确地标示其含义。\n4. **Appendix 编号**：组织标记为 A*-T，但部分 appendix 在 PDF 中的实际编号难以跟踪（如 \"Appendix T\" 实际是 \"Cross-Axis Contamination\"），建议统一命名和交叉引用。\n5. **Section 3.5 Design Rationale** 位置偏后——读者在读完 Section 3.1-3.4 后才看到实验设计的 causal justification。建议提前到 Section 3.1 之前或合并为 Section 3 的开头段落。\n\n---\n\n## 主要优势\n\n1. **统计处理的深度和透明度是本文最大的亮点**。7 种统计方法（BT, sign test, Likert ATE, ordinal regression, GEE, Wilcoxon, Mann-Whitney）互相验证，bootstrap CI 10,000 次 resamples，power analysis，bootstrap attenuation analysis，NLI threshold sweep——这在 NLP 论文中罕见，树立了方法论论文的高标准。\n2. **GEE conditional decomposition 是一个有价值的分析工具**，将 BT 的整体偏好分解为 style 和 originality 两个分量，揭示了 verbosity（style-dominated）和 formality（conditionally style-driven）的结构性差异。即使 n=88 的 CI 较宽，这个分析框架本身有独立的方法论贡献。\n3. **实验设计的 confounder control 策略周全**：NLI gate + position swap + same-style double-rewrite control + direction-aware gating for verbosity——形成了多层防线。每一层都有对应的 validation（human annotation for NLI, consistency filter robustness for position swap 等）。\n4. **Six controls for amplification risk (§5.4)** 是对 Comparative Trap (Jeong et al., 2025) 的直接回应，体现了对潜在反驳的主动防御。\n5. **Bootstrap attenuation analysis (Appendix K)** 提供了区分 power limitation 和 measurement attenuation 的巧妙方法——d 收敛到 0 而非保持 non-zero 是 Likert signal genuinely absent 的强证据。\n6. **Limitations 部分坦诚且全面**，主动列出了 quality-style confounding、evaluator-producer bias、ecological validity 等限制，没有试图掩盖弱点。\n",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 方法论扎实、统计处理详尽的诊断性工作，核心发现（Likert-pairwise divergence）有实证支撑且具实践意义，但对 divergence 的因果归因不够审慎、negative control 等效检验统计力不足、style axis 覆盖有限，使得结论的普适性存疑。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5 / 5 | 核心方法（CSD pipeline + GEE decomposition）设计合理，7 种统计方法互相验证；但 NLI gate 与人工标注的一致性仅 moderate（κ=0.32-0.44），negative control 的 TOST 在 Δ=10pp 时失效（power≈42%），且对 divergence 的三种解释（attenuation / amplification / construct divergence）未能决定性区分，削弱了 \"Likert Blindspot\" 这一因果性命名的合理性。 |\n| **Excitement** | 3.5 / 5 | 问题重要且切中实践痛点（RLHF/DPO 依赖 pairwise，evaluation 依赖 Likert），CSD 方法具有 reusable tool 价值；但论文主要 *诊断* 了问题而未提供 mitigation 路径，且仅覆盖 2 个 primary style axis，对社区的指导性有限。 |\n| **Reproducibility** | 4 / 5 | 实现细节充分（Appendix R 列出模型版本、温度、seed 等），BT CI 和 GEE CI 均完整报告；代码和数据承诺 \"released upon acceptance\" 但当前不可用。 |\n| **Confidence** | 4 / 5 | 本人熟悉 Bradley-Terry 模型、GEE、等效检验等统计方法，仔细核查了论文中的统计声明。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Likert Blindspot 的因果归因过度——论文自身证据无法排除 \"construct divergence\" 解释\n\n- **具体位置**：Section 5.1（§95-101 experiments.tex）、Title、Abstract line 1-4\n- **问题**：论文命名为 \"The Likert Blindspot\"，暗示 Likert 有 *缺陷*（blindspot = 盲区），但 Section 5.1 自己列出了三种 non-exclusive 解释：(a) Likert attenuation, (b) pairwise amplification, (c) construct divergence。论文承认 \"the attenuation evidence (d→0 at n=355) is necessary but not sufficient for causal identification\"，也承认 \"definitive resolution requires human evaluation comparing Likert and pairwise judgments on identical pairs\"（Limitations）。在这种无法区分的情况下，Title 和 framing 强烈偏向解释 (a)（Likert 有缺陷），而非中性的 \"measurement-mode divergence\"（虽然副标题包含此词，但 \"Blindspot\" 的修辞效果远强于副标题）。\n  \n  更关键的是：pairwise comparison 相比 absolute rating 具有更高判别力是 psychometrics 自 Thurstone (1927) 以来的已知现象——论文自身也引用了此文。power analysis 显示 Likert 需要 4-206× 的样本量才能检测到 BT 捕获的效应——这 *完全一致于* 相对判断 vs 绝对判断的已知灵敏度差异，不需要 \"blindspot\" 这一因果性解释。论文需要更充分地论证：为什么观察到的 divergence *不仅仅是* 已知的 format sensitivity 差异？\n  \n- **为什么影响接收**：标题和核心 framing 的因果暗示超出了实验证据的支撑范围，是 overclaiming。\n- **建议修改方向**：\n  1. 在 Introduction 和 Analysis 中给 construct divergence 解释同等的篇幅和权重，而非将其作为 Limitations 的一个段落\n  2. 明确讨论 Thurstone (1927) 的 discriminability 差异如何与本文发现对齐或区分\n  3. 考虑将 \"Blindspot\" 改为更中性的术语（如 \"Likert-Pairwise Gap\"），或在正文中明确定义 \"Blindspot\" 为一个操作性描述（divergence 现象的名称）而非因果性声明\n\n---\n\n**N2** [critical] Negative control (Claude Sonnet 4) 的等效检验统计力严重不足\n\n- **具体位置**：Appendix G（Table 9, app:claude_tost）；Section 5.1 第 97 行\n- **问题**：Claude Sonnet 4 作为 negative control 是实验设计的关键支柱——用于证明 \"有的 judge 不展示 Blindspot，因此 Blindspot 不是 format 的固有属性\"。但 TOST 等效检验在 Δ=15pp 时才达到显著（p=0.010），而 15pp 对应的 BT=65% 在实践中是一个 *相当大* 的偏好差异。在 Δ=10pp（一个更合理的实际显著性门槛）时，TOST 不显著（p=0.156, power≈42%）。论文自己承认 \"the minimum equivalence margin achieving 80% power at n=88 is Δ=15.7pp\"。\n\n  这意味着：我们无法在 n=88 的情况下区分 \"Claude 没有 style bias\" 和 \"Claude 有 10pp 的 style bias\"。Claude 的 BT 值为 56.2%（formality）和 54.1%（verbosity），虽然接近 50%，但 6.2pp 的偏差在 n=88 下完全可能反映真实的 moderate effect。\n  \n- **为什么影响接收**：negative control 的有效性直接关系到 \"Blindspot 是 judge-specific 而非 format-inherent\" 这一核心论点。如果 negative control 失效，则 N1 中的 \"construct divergence\" 解释变得更强。\n- **建议修改方向**：\n  1. 扩大 negative control 样本量至少到 n=200+，使 Δ=10pp 的 TOST 达到合理 power\n  2. 或者诚实地将 negative control 结论降级为 \"suggestive but underpowered\"，不将其作为排除 format-inherent 解释的主要证据\n  3. 增加第二个 negative control judge 以增强说服力\n\n---\n\n**N3** [critical] 样本量 n=88 下 GEE decomposition 的可靠性存疑\n\n- **具体位置**：Table 2（主文 p.7）；Section 4.1；Appendix D\n- **问题**：GEE conditional decomposition 是本文方法的核心创新之一——将 BT 的整体偏好分解为 style 和 originality 两个分量。但在 n=88（176 observations for binary outcome）的条件下，logistic GEE 需要估计的参数虽然少（intercept + 2 predictors），但 CI 极宽：例如 Qwen3 verbosity Style OR = 13.10 [5.62, 30.55]——95% CI 跨越了将近 6 倍的范围。Gemini formality Style OR = 1.64 [0.91, 2.98] 的 CI 包含 1.0，即不显著。\n\n  更重要的是，n=88 下交互效应检验的 power 极低。Table 4 报告所有交互项 p > 0.13，但 OR 值波动很大（0.45 到 2.60），这些 p 值更可能反映 power 不足而非真正的 null。论文不能基于 non-significant interaction 就断言 additive model 正确。\n  \n- **为什么影响接收**：GEE 是区分 \"style-dominated\" vs \"quality-confounded\" 的唯一工具。如果在 n=88 下 GEE 的 effect size 估计不稳定（n=88 到 n=355 的 Qwen3 formality Style OR 从 4.20 降到 2.15，缩水 49%），那么基于小样本 GEE 得出的 per-judge regime classification 的可靠性令人怀疑。\n- **建议修改方向**：\n  1. 对所有 judge×axis 组合进行 n=355 级别的 scaled replication（目前只有 Qwen3 formality 做了）\n  2. 至少报告 GEE 的 power analysis 或 minimum detectable OR\n  3. 讨论 n=88→n=355 时 Qwen3 Style OR 缩水 49% 的含义——是否其他 judge 的 OR 也可能被高估？\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Style axis 覆盖窄（2 个 primary + 1 个 exploratory），限制了方法的普适性声明\n\n- **具体位置**：Section 3.1；Limitations 段落 3（line 56-62 main.tex）\n- **问题**：CSD 作为 \"black-box diagnostic methodology\" 被提出，但仅在 formality 和 verbosity 上充分验证。Register 是 exploratory pilot（且有 evaluator-producer overlap）。论文 Limitations 承认 hedging/humor/technicality 等语义级 axes 会被 NLI gate 系统性拒绝（55% rejection rate for tone axis pilot），这实际上将 CSD 限制在 surface-level stylistic attributes。但 Abstract 和 Introduction 的 framing 没有充分反映这一限制。\n- **建议**：在 Abstract 中加入 \"surface-level style axes\" 的限定语；讨论 CSD 对语义密集型 style axes 的 fundamental limitation。\n\n**W2** [warning] Cross-axis contamination 中 FK grade 变化的处理不够严谨\n\n- **具体位置**：Appendix T (Table 19)\n- **问题**：Verbosity rewrites 导致 FK grade d=0.50（medium effect），论文将其归因于 \"sentence length dependence\"。但 FK grade 同时反映 formality 相关的词汇复杂度，d=0.50 的 cross-axis 泄漏对于一个声称隔离单一 axis 的方法来说并非 trivial。论文的解释（句子长度的 artifact）是合理的但未被正式验证——例如，可以在控制句子长度后重新计算 FK grade shift。\n- **建议**：对 FK grade 做 length-controlled 分析，或至少讨论这个 d=0.50 对 formality×verbosity 交互的潜在影响。\n\n**W3** [warning] Evaluator-producer overlap 的 mitigation 只测试了一个替代 rewriter\n\n- **具体位置**：Appendix E (Table 6, Table 7)\n- **问题**：Qwen3-32B 同时做 rewriter 和 judge 是一个 known confound。论文用 GPT-4o 作为替代 rewriter 进行 independence test——结果显示 Style OR 下降 22%（13.10→10.17 for verbosity）。这是一个有意义的 check，但：(a) 只测试了一个替代配置；(b) 22% 的 OR 下降并不小；(c) 没有用第三个 rewriter 确认趋势是否稳定。\n- **建议**：增加至少一个额外的 rewriter（如 Llama 或 Gemini）做 independence test，或至少讨论 22% 下降的上界含义。\n\n**W4** [warning] IIA assumption 的讨论不充分\n\n- **具体位置**：Section 4.1 footnote（experiments.tex line 12）\n- **问题**：论文在脚注中声称 \"In binary-choice BT models, IIA is structurally satisfied\"，然后将 formality 的 direction asymmetry 解释为 \"heterogeneous treatment effects across style directions rather than IIA violation\"。但 IIA 的 structural satisfaction 仅在每对选手只比一次的情况下成立。在本文设计中，同一文本对在不同 style conditions 下反复出现，共享 source text 带来的依赖性可能系统性违反 IIA。GEE 部分用了 exchangeable correlation 来处理组内相关，但 BT model 本身没有类似的修正。\n- **建议**：在正文而非脚注中讨论 IIA，并明确说明 GEE 如何补充 BT 在这方面的不足。\n\n**W5** [warning] 100-point continuous Likert scale 实验仅用了一个 judge\n\n- **具体位置**：Appendix O\n- **问题**：100-point scale 实验（旨在排除 scale granularity 解释）仅在 Qwen3-32B 上进行。如果 Blindspot 的表现因 judge 而异（如 Gemini 的 formality 就明显更弱），单一 judge 的 100-point 实验不足以支持 \"granularity is not the issue\" 的一般性结论。\n- **建议**：至少在两个 judge 上 replicate 100-point scale 实验。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 1 排版密度过高**：15 行结果 + 6 行脚注在一个 Table 中，阅读体验较差。建议将 LLMBar primary results 和 cross-benchmark replication 分为两个表。\n2. **\"style bias\" vs \"style sensitivity\" 措辞不一致**：两个术语在文中交替使用但含义略有不同（bias 暗示方向性，sensitivity 暗示双向的响应性）。建议统一或明确区分。\n3. **Figure 2 (DAG) 的 dashed orange S→Q path** 标为 \"residual confound\"，但 caption 说 \"style may influence perceived quality through channels the NLI gate cannot block\"——这条路径实际上是一个 *acknowledged unblocked confounder*，建议在 caption 中更明确地标示其含义。\n4. **Appendix 编号**：组织标记为 A*-T，但部分 appendix 在 PDF 中的实际编号难以跟踪（如 \"Appendix T\" 实际是 \"Cross-Axis Contamination\"），建议统一命名和交叉引用。\n5. **Section 3.5 Design Rationale** 位置偏后——读者在读完 Section 3.1-3.4 后才看到实验设计的 causal justification。建议提前到 Section 3.1 之前或合并为 Section 3 的开头段落。\n\n---\n\n## 主要优势\n\n1. **统计处理的深度和透明度是本文最大的亮点**。7 种统计方法（BT, sign test, Likert ATE, ordinal regression, GEE, Wilcoxon, Mann-Whitney）互相验证，bootstrap CI 10,000 次 resamples，power analysis，bootstrap attenuation analysis，NLI threshold sweep——这在 NLP 论文中罕见，树立了方法论论文的高标准。\n2. **GEE conditional decomposition 是一个有价值的分析工具**，将 BT 的整体偏好分解为 style 和 originality 两个分量，揭示了 verbosity（style-dominated）和 formality（conditionally style-driven）的结构性差异。即使 n=88 的 CI 较宽，这个分析框架本身有独立的方法论贡献。\n3. **实验设计的 confounder control 策略周全**：NLI gate + position swap + same-style double-rewrite control + direction-aware gating for verbosity——形成了多层防线。每一层都有对应的 validation（human annotation for NLI, consistency filter robustness for position swap 等）。\n4. **Six controls for amplification risk (§5.4)** 是对 Comparative Trap (Jeong et al., 2025) 的直接回应，体现了对潜在反驳的主动防御。\n5. **Bootstrap attenuation analysis (Appendix K)** 提供了区分 power limitation 和 measurement attenuation 的巧妙方法——d 收敛到 0 而非保持 non-zero 是 Likert signal genuinely absent 的强证据。\n6. **Limitations 部分坦诚且全面**，主动列出了 quality-style confounding、evaluator-producer bias、ecological validity 等限制，没有试图掩盖弱点。\n",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 999 · 2026-05-23T05:32:36.668603+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3764
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-23T05:32:41.796030+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-23T05:32:41.846596+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1002 · 2026-05-23T05:32:55.306230+00:00_

审稿意见已提交给 Review Director。

**总结**：Overall 3.5（Borderline Conference），Soundness 3.5，Excitement 3.5。

核心问题三个：
1. **N1**："Likert Blindspot" 的因果归因超出证据——论文自身承认三种解释无法区分，但标题和 framing 强烈偏向 "Likert 有缺陷"，而 pairwise vs absolute rating 的灵敏度差异是 Thurstone (1927) 以来的已知现象
2. **N2**：Negative control (Claude Sonnet 4) 的 TOST 在 Δ=10pp 时失效（power≈42%），无法排除 Claude 有 moderate style bias 的可能
3. **N3**：n=88 下 GEE decomposition 的 CI 极宽（Style OR CI 跨 6 倍），且 n=88→n=355 时 Qwen3 Style OR 缩水 49%，其他 judge 的 regime classification 可靠性存疑

主要优势：统计处理深度罕见（7 种方法互验证 + bootstrap attenuation + power analysis），GEE decomposition 框架有独立方法论价值，confounder control 策略周全。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 32

## Round 32

4 recorded events


### User

_source line 1003 · 2026-05-23T05:33:17.574187+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix / Should-Fix / Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 的审稿意见

**Overall**: 3.5 / 5 (Borderline Conference)

### Must-Fix 问题

**N1** [critical] 仅两个风格轴无法支撑 "Likert Blindspot" 的通用性 claim
- Abstract ("systematically divergent style sensitivity"), Section 1 ("a systematic pattern"), Title ("LLM Judge Style Evaluation")
- 论文标题和摘要将 Likert Blindspot 定位为 LLM judge style 评估的通用现象，但实验仅覆盖 formality 和 verbosity + 探索性的 register。这三个轴均属表层文体属性，Limitations 承认 semantic-level axes 因 NLI gate 限制无法覆盖。仅基于两个高度相关的表层轴就声称 systematic pattern，存在过度概括风险。

**N2** [critical] 三种机制解释未能区分，限制了理论贡献
- Section 5.1 ("three non-exclusive explanations"), Limitations paragraph 1
- 论文提出 attenuation/amplification/construct divergence 三种解释但明确表示无法区分。这三种解释有截然不同的实践含义。一篇 diagnostic 论文如果无法判断被诊断的现象究竟是什么，其理论贡献和实践指导价值大打折扣。

**N3** [critical] 与 RATE (Reber et al., 2025) 的增量贡献需更清晰界定
- Section 2, Section 5.1 ("Head-to-head comparison with RATE")
- RATE 已建立 style-rewriting + ATE 框架。CSD 核心区别在于引入 pairwise + GEE + NLI gating。但 head-to-head 比较仅用 1 段文字，且 claim RATE "may underestimate" 需更强证据。

### Should-Fix 问题

**W1** Table 1 信息密度过高，可读性不佳
**W2** Figure 2 的 DAG 假设未充分讨论
**W3** Negative control (Claude Sonnet 4) 的解释不够深入
**W4** Human annotation 验证的规模偏小（50 pairs, κ=0.44）

### Minor Issues
**M1** Rewriting prompt 完整文本未给出
**M2** Table 2 "Orig OR" 首次出现时未解释
**M3** Cross-benchmark BT 效应量差异未讨论
**M4** References 格式不完全一致
**M5** 100-point scale 仅测试一个 judge
**M6** Abstract 中 judge 数量表述与正文不一致

---

请对以上每个问题逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1004 · 2026-05-23T05:35:07.033563+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 仅两个风格轴无法支撑通用性 claim**\n\n同意。这与我自己审稿的 W1 一致。论文仅在 formality 和 verbosity 两个 primary axis 上进行了充分验证，register 为 exploratory 且存在 evaluator-producer overlap（Limitations line 52: \"Register results carry the highest evaluator-producer risk\"）。Limitations 还承认 semantic-level axes（hedging, humor, technicality）会被 NLI gate 系统性拒绝（line 57-58: \"the NLI gate correctly rejected 55% of rewrites because epistemic commitment changes violate content equivalence\"）。在仅有 2 个 surface-level axis 的证据下，Abstract 的 \"systematically divergent style sensitivity\" 和 Title 的 \"LLM Judge Style Evaluation\" 的确存在过度概括。\n\n补充我的发现：这两个 axis 本身也并非完全独立——Appendix T (Table 19) 显示 verbosity 操纵导致 FK grade d=0.50 的 cross-axis 泄漏（我在 W2 中提出），说明 formality 和 verbosity 之间有结构性相关，进一步削弱了仅凭两个 axis 支撑通用性声明的合理性。\n\n---\n\n**[AGREE] R2-N2: 三种机制解释未能区分，限制理论贡献**\n\n强烈同意。这是我自己审稿 N1 的核心论点。论文在 Section 5.1 (experiments.tex line 95) 明确列出三种 non-exclusive 解释，并承认 \"the attenuation evidence (d→0 at n=355) is necessary but not sufficient for causal identification\"（line 96）。Limitations 进一步承认 \"definitive resolution requires human evaluation comparing Likert and pairwise judgments on identical pairs\"（line 45）。\n\n在无法区分三种机制的情况下，\"Blindspot\" 这一命名暗示 Likert 有缺陷（解释 a），而非中性地描述 divergence 现象。如果最终解释是 construct divergence（解释 c），那么 Likert 和 pairwise 只是在测量不同的东西，没有任何一方有 \"盲区\"——实践含义截然不同。论文的理论贡献因此受限于 \"诊断出了 divergence 现象\" 而非 \"解释了 divergence 机制\"。\n\n---\n\n**[REBUT] R2-N3: 与 RATE 的增量贡献需更清晰界定**\n\n不完全同意。R2 称 \"head-to-head 比较仅用 1 段文字\" 且增量贡献不清晰，但论文实际上在多个层面展示了与 RATE 的结构性差异：\n\n1. **RATE 在设计上无法检测 Blindspot**：RATE 仅使用 Likert ATE（Section 5.1, line 80），因此从结构上不可能发现 Likert-pairwise divergence——这正是 CSD 的核心发现。head-to-head 比较（同一数据：RATE d=0.10 n.s. vs CSD BT=63% p=0.0004）不是 \"仅用 1 段文字\" 的简单比较，而是一个 *构造性* 的论证：同一数据在不同 measurement mode 下给出截然不同的结论。\n\n2. **GEE conditional decomposition 是方法论层面的新贡献**：RATE 不提供 per-axis confound structure 分析。Table 2 的 GEE 分解揭示了 verbosity（Style OR 8-13, Orig OR <1, style-dominated）和 formality（Style OR 2-5, Orig OR 2-5, conditionally style-driven）的结构性差异——这一发现无法从 RATE 框架中获得。\n\n3. **NLI gating 策略不同**：CSD 使用 DeBERTa-v3-large + axis-dependent 方向感知 gating（Section 3.2, Appendix G），RATE 使用不同的 content preservation 方法。\n\n4. **Related Work (Section 2)** 明确定位了差异：CSD \"intervenes on specific style axes rather than general attributes\" 且 \"uses a sign test with position control rather than parametric aggregation.\"\n\n但我同意 R2 的一个 subpoint：论文关于 RATE \"may underestimate\" 的 claim（Section 2: \"RATE's own style-related findings may underestimate the true magnitude of attribute effects\"）确实需要更谨慎的措辞——这是一个 *推测*，不是经过 controlled comparison 验证的结论。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Table 1 信息密度过高**\n\n同意。这与我的 Minor Issue #1 一致。15 行结果 + 6 行脚注挤在一个 Table 中，跨 3 个 benchmark、5 个 judge、3 个 axis，读者很难快速提取关键 pattern。建议拆分为 primary (LLMBar) 和 cross-benchmark replication 两个表。\n\n---\n\n**[REBUT] R2-W2: Figure 2 DAG 假设未充分讨论**\n\n不完全同意。论文实际上在多个位置讨论了 DAG 的假设和局限性：\n\n- Figure 2 caption 明确声明 \"design rationale, not a claim of perfect identification\"\n- Appendix A (Design Rationale, appendix.tex line 12) 明确说明 \"we do not claim that the DAG in Figure 2 is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\"\n- 识别条件三条假设在 Appendix A line 13-14 中列出\n- Limitations paragraph 1 (main.tex line 41-46) 详细讨论了 quality-style confounding 的不可分性\n- Dashed orange S→Q path 在 caption 中标为 \"residual confounding\"\n\nDAG 的每条路径——R→Q (NLI gate blocked), R→Y (double-rewrite control), P→Y (position swap), S→Q (residual confound, acknowledged)——都有对应的 control 或 acknowledgment。我认为讨论已足够充分。不过我同意 DAG 中 S→Q 的 dashed orange path 可以在 caption 中更明确地说明为 \"acknowledged unblocked confounder\"（这是我 Minor Issue #3 中提到的点）。\n\n---\n\n**[AGREE] R2-W3: Negative control 解释不够深入**\n\n强烈同意，且我认为这应升级为 Must-Fix。这是我自己审稿中的 N2。TOST 在 Δ=10pp 时失效（p=0.156, power≈42%; Appendix G Table 9），15pp 的等效边界在实践中过宽。Claude BT=56.2%/54.1% 虽接近 50%，但在 n=88 下无法排除 moderate effect。论文自己承认 minimum equivalence margin achieving 80% power 是 Δ=15.7pp（appendix.tex line 227）。\n\n---\n\n**[AGREE] R2-W4: Human annotation 规模偏小**\n\n部分同意。50 pairs 的标注量确实偏小，且 κ=0.44（moderate）和 Gwet's AC1=0.65（substantial）之间的差距主要由 prevalence effect 解释（Section 5.4, line 177）。但关键指标是 pass precision：A1 100% [86.7%, 100%], A2 84% [65.3%, 93.6%]（experiments.tex line 176）。A2 的 84% 下界仅 65.3%，这意味着在 worst case 下，最多有约 1/3 的 gate-passed pairs 可能包含内容变化——这对 style-only intervention 的声明有实质性影响。\n\n我的补充：论文还报告了 GPT-4o cross-validation 的 pass precision（main.tex line 66: \"92.1% formality / 82.6% verbosity\"），但这是 LLM cross-validation 而非独立人工验证。总体而言，50 pairs 的标注规模对于一篇以 content preservation 为核心假设的论文来说偏小，建议至少增加到 100 pairs 并覆盖所有 axis。\n\n---\n\n### Minor Issues\n\n**[AGREE] R2-M1**: Rewriting prompt 完整文本确实应在 Appendix 中给出。Section 3.1 仅给出了一个 paraphrase-level 的示例（method.tex line 9: \"Rewrite the following text to be more formal/casual while preserving the exact same content and meaning\"），不确定这是否是实际使用的完整 prompt。\n\n**[AGREE] R2-M2**: \"Orig OR\" 在 Table 2 中首次出现时，虽然 caption 提到 \"originality effects\"，但 \"Orig OR\" 的缩写未解释。建议在 caption 或正文中首次引用时展开为 \"Originality OR (original-preference odds ratio)\"。\n\n**[REBUT] R2-M3**: 不同意 \"cross-benchmark BT 效应量差异未讨论\"。论文在 Section 5.3 (experiments.tex line 164-165) 明确讨论了 severity spectrum：\"Llama-70B formality on AlpacaEval (BT 75.6%, d=1.12, p<.001) is strong enough for Likert detection\"，并在 Section 5.1 line 84 说明 \"at stronger effects (BT>70%), Likert partially detects but attenuates >60%\"。三个 exceptions（Table 1 中的 ‡ rows）被解释为 effect-size dependent escape from the Blindspot。这个讨论是充分的。\n\n**[AGREE] R2-M4**: References 格式一致性应检查。\n\n**[AGREE] R2-M5**: 与我的 W5 一致。100-point scale 实验仅在 Qwen3-32B 上进行，至少应在 2 个 judge 上 replicate。\n\n**[REBUT] R2-M6**: 不同意 \"Abstract 中 judge 数量表述与正文不一致\"。Abstract 明确说 \"Across four judges from independent providers, one negative control\"（PDF p.1），正文 Section 4.1 (experiments.tex line 17) 列出 4 个 target judges + Claude Sonnet 4 作为 negative control = 5 个 judge，与 Abstract 一致。如果 R2 指的是其他不一致之处，请指明具体位置。\n",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 仅两个风格轴无法支撑通用性 claim**\n\n同意。这与我自己审稿的 W1 一致。论文仅在 formality 和 verbosity 两个 primary axis 上进行了充分验证，register 为 exploratory 且存在 evaluator-producer overlap（Limitations line 52: \"Register results carry the highest evaluator-producer risk\"）。Limitations 还承认 semantic-level axes（hedging, humor, technicality）会被 NLI gate 系统性拒绝（line 57-58: \"the NLI gate correctly rejected 55% of rewrites because epistemic commitment changes violate content equivalence\"）。在仅有 2 个 surface-level axis 的证据下，Abstract 的 \"systematically divergent style sensitivity\" 和 Title 的 \"LLM Judge Style Evaluation\" 的确存在过度概括。\n\n补充我的发现：这两个 axis 本身也并非完全独立——Appendix T (Table 19) 显示 verbosity 操纵导致 FK grade d=0.50 的 cross-axis 泄漏（我在 W2 中提出），说明 formality 和 verbosity 之间有结构性相关，进一步削弱了仅凭两个 axis 支撑通用性声明的合理性。\n\n---\n\n**[AGREE] R2-N2: 三种机制解释未能区分，限制理论贡献**\n\n强烈同意。这是我自己审稿 N1 的核心论点。论文在 Section 5.1 (experiments.tex line 95) 明确列出三种 non-exclusive 解释，并承认 \"the attenuation evidence (d→0 at n=355) is necessary but not sufficient for causal identification\"（line 96）。Limitations 进一步承认 \"definitive resolution requires human evaluation comparing Likert and pairwise judgments on identical pairs\"（line 45）。\n\n在无法区分三种机制的情况下，\"Blindspot\" 这一命名暗示 Likert 有缺陷（解释 a），而非中性地描述 divergence 现象。如果最终解释是 construct divergence（解释 c），那么 Likert 和 pairwise 只是在测量不同的东西，没有任何一方有 \"盲区\"——实践含义截然不同。论文的理论贡献因此受限于 \"诊断出了 divergence 现象\" 而非 \"解释了 divergence 机制\"。\n\n---\n\n**[REBUT] R2-N3: 与 RATE 的增量贡献需更清晰界定**\n\n不完全同意。R2 称 \"head-to-head 比较仅用 1 段文字\" 且增量贡献不清晰，但论文实际上在多个层面展示了与 RATE 的结构性差异：\n\n1. **RATE 在设计上无法检测 Blindspot**：RATE 仅使用 Likert ATE（Section 5.1, line 80），因此从结构上不可能发现 Likert-pairwise divergence——这正是 CSD 的核心发现。head-to-head 比较（同一数据：RATE d=0.10 n.s. vs CSD BT=63% p=0.0004）不是 \"仅用 1 段文字\" 的简单比较，而是一个 *构造性* 的论证：同一数据在不同 measurement mode 下给出截然不同的结论。\n\n2. **GEE conditional decomposition 是方法论层面的新贡献**：RATE 不提供 per-axis confound structure 分析。Table 2 的 GEE 分解揭示了 verbosity（Style OR 8-13, Orig OR <1, style-dominated）和 formality（Style OR 2-5, Orig OR 2-5, conditionally style-driven）的结构性差异——这一发现无法从 RATE 框架中获得。\n\n3. **NLI gating 策略不同**：CSD 使用 DeBERTa-v3-large + axis-dependent 方向感知 gating（Section 3.2, Appendix G），RATE 使用不同的 content preservation 方法。\n\n4. **Related Work (Section 2)** 明确定位了差异：CSD \"intervenes on specific style axes rather than general attributes\" 且 \"uses a sign test with position control rather than parametric aggregation.\"\n\n但我同意 R2 的一个 subpoint：论文关于 RATE \"may underestimate\" 的 claim（Section 2: \"RATE's own style-related findings may underestimate the true magnitude of attribute effects\"）确实需要更谨慎的措辞——这是一个 *推测*，不是经过 controlled comparison 验证的结论。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Table 1 信息密度过高**\n\n同意。这与我的 Minor Issue #1 一致。15 行结果 + 6 行脚注挤在一个 Table 中，跨 3 个 benchmark、5 个 judge、3 个 axis，读者很难快速提取关键 pattern。建议拆分为 primary (LLMBar) 和 cross-benchmark replication 两个表。\n\n---\n\n**[REBUT] R2-W2: Figure 2 DAG 假设未充分讨论**\n\n不完全同意。论文实际上在多个位置讨论了 DAG 的假设和局限性：\n\n- Figure 2 caption 明确声明 \"design rationale, not a claim of perfect identification\"\n- Appendix A (Design Rationale, appendix.tex line 12) 明确说明 \"we do not claim that the DAG in Figure 2 is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\"\n- 识别条件三条假设在 Appendix A line 13-14 中列出\n- Limitations paragraph 1 (main.tex line 41-46) 详细讨论了 quality-style confounding 的不可分性\n- Dashed orange S→Q path 在 caption 中标为 \"residual confounding\"\n\nDAG 的每条路径——R→Q (NLI gate blocked), R→Y (double-rewrite control), P→Y (position swap), S→Q (residual confound, acknowledged)——都有对应的 control 或 acknowledgment。我认为讨论已足够充分。不过我同意 DAG 中 S→Q 的 dashed orange path 可以在 caption 中更明确地说明为 \"acknowledged unblocked confounder\"（这是我 Minor Issue #3 中提到的点）。\n\n---\n\n**[AGREE] R2-W3: Negative control 解释不够深入**\n\n强烈同意，且我认为这应升级为 Must-Fix。这是我自己审稿中的 N2。TOST 在 Δ=10pp 时失效（p=0.156, power≈42%; Appendix G Table 9），15pp 的等效边界在实践中过宽。Claude BT=56.2%/54.1% 虽接近 50%，但在 n=88 下无法排除 moderate effect。论文自己承认 minimum equivalence margin achieving 80% power 是 Δ=15.7pp（appendix.tex line 227）。\n\n---\n\n**[AGREE] R2-W4: Human annotation 规模偏小**\n\n部分同意。50 pairs 的标注量确实偏小，且 κ=0.44（moderate）和 Gwet's AC1=0.65（substantial）之间的差距主要由 prevalence effect 解释（Section 5.4, line 177）。但关键指标是 pass precision：A1 100% [86.7%, 100%], A2 84% [65.3%, 93.6%]（experiments.tex line 176）。A2 的 84% 下界仅 65.3%，这意味着在 worst case 下，最多有约 1/3 的 gate-passed pairs 可能包含内容变化——这对 style-only intervention 的声明有实质性影响。\n\n我的补充：论文还报告了 GPT-4o cross-validation 的 pass precision（main.tex line 66: \"92.1% formality / 82.6% verbosity\"），但这是 LLM cross-validation 而非独立人工验证。总体而言，50 pairs 的标注规模对于一篇以 content preservation 为核心假设的论文来说偏小，建议至少增加到 100 pairs 并覆盖所有 axis。\n\n---\n\n### Minor Issues\n\n**[AGREE] R2-M1**: Rewriting prompt 完整文本确实应在 Appendix 中给出。Section 3.1 仅给出了一个 paraphrase-level 的示例（method.tex line 9: \"Rewrite the following text to be more formal/casual while preserving the exact same content and meaning\"），不确定这是否是实际使用的完整 prompt。\n\n**[AGREE] R2-M2**: \"Orig OR\" 在 Table 2 中首次出现时，虽然 caption 提到 \"originality effects\"，但 \"Orig OR\" 的缩写未解释。建议在 caption 或正文中首次引用时展开为 \"Originality OR (original-preference odds ratio)\"。\n\n**[REBUT] R2-M3**: 不同意 \"cross-benchmark BT 效应量差异未讨论\"。论文在 Section 5.3 (experiments.tex line 164-165) 明确讨论了 severity spectrum：\"Llama-70B formality on AlpacaEval (BT 75.6%, d=1.12, p<.001) is strong enough for Likert detection\"，并在 Section 5.1 line 84 说明 \"at stronger effects (BT>70%), Likert partially detects but attenuates >60%\"。三个 exceptions（Table 1 中的 ‡ rows）被解释为 effect-size dependent escape from the Blindspot。这个讨论是充分的。\n\n**[AGREE] R2-M4**: References 格式一致性应检查。\n\n**[AGREE] R2-M5**: 与我的 W5 一致。100-point scale 实验仅在 Qwen3-32B 上进行，至少应在 2 个 judge 上 replicate。\n\n**[REBUT] R2-M6**: 不同意 \"Abstract 中 judge 数量表述与正文不一致\"。Abstract 明确说 \"Across four judges from independent providers, one negative control\"（PDF p.1），正文 Section 4.1 (experiments.tex line 17) 列出 4 个 target judges + Claude Sonnet 4 作为 negative control = 5 个 judge，与 Abstract 一致。如果 R2 指的是其他不一致之处，请指明具体位置。\n",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1005 · 2026-05-23T05:35:10.496365+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3462
}
```

</details>

---


### Assistant

_source line 1006 · 2026-05-23T05:35:24.679571+00:00_

审稿回应已提交。对 R2 的 13 个问题：

- **5 项 AGREE**（N1 style axis 覆盖窄、N2 三种机制未区分、W1 Table 1 密度、W3 negative control 不足、W4 标注规模小）
- **3 项 REBUT**（N3 与 RATE 增量贡献实际已充分展示、W2 DAG 假设讨论已足够、M3 cross-benchmark 差异已讨论、M6 Abstract 数量一致）
- **5 项 Minor AGREE**（M1 prompt 文本、M2 术语解释、M4 引用格式、M5 100-point 单 judge）

关键交叉发现：R2-N1 和 R2-N2 与我的 N1 和 W1 高度一致，形成两位 reviewer 的共识——论文的核心弱点在于 (1) style axis 覆盖有限导致通用性 claim 过强，(2) 三种机制解释未能区分导致 "Blindspot" 命名的因果暗示超出证据范围。R2-W3 与我的 N2 一致，negative control 的统计力问题也是共识。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 33

## Round 33

62 recorded events


### User

_source line 1007 · 2026-05-23T06:41:45.054021+00:00_

[Round 1 审稿请求]:
你负责**方法严谨性**审查。

## Venue 信息
- **EMNLP 2026 via ARR** (May cycle)，截止 2026-05-25
- 正文 ≤8 页（不含 Limitations 和 References），ACL 模板，double-blind
- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit
- Limitations 章节必须有但不计入页数

## 论文路径
- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`（sections/ 子目录有各章节）
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf`

## 审查侧重
请重点审查以下方面，给出逐条 Strengths / Weaknesses / Questions：

1. **CSD pipeline 设计合理性**：style-controlled rewriting → NLI gate → pairwise measurement 的因果推理链条是否完整？NLI gate 的 content preservation 保证是否充分？direction-aware gating 的理论依据？

2. **统计框架严谨性**：
   - Holm-Bonferroni 多重比较校正策略（6-test primary family + confirmatory + exploratory 的三层分类）是否合理？
   - Bradley-Terry 模型假设（IIA, unidimensionality）在此场景下是否满足？
   - GEE conditional decomposition 的 additive model 假设是否得到充分验证？交互效应检验 power 是否足够？
   - 在 n=88 下 GEE OR 的 CI 宽度和 n=88→n=355 的 49% OR shrinkage 对结论的影响

3. **Negative control (Claude Sonnet 4) 有效性**：
   - TOST 等价性检验在 Δ=10pp 时仅 power≈42%，negative control 的证据强度是否足够？
   - 三条收敛证据（TOST, GEE Style OR cross-benchmark consistency, GPT-4o contrast）的论证层级

4. **Robustness 分析**：
   - Human annotation 验证（50 pairs, κ=0.44, A2 pass precision 下界 65.3%）规模和质量
   - 100-point continuous Likert 实验仅在一个 judge 上测试
   - Cross-axis contamination（FK grade d=0.50）的处理
   - Evaluator-producer overlap 缓解（仅一个替代 rewriter，22% OR 降幅）

5. **格式合规**：页数限制、匿名规则、Limitations 章节完整性

请严格评审，不留情面。输出格式：
```
## Summary
（2-3 句论文概述）

## Strengths
S1. ...
S2. ...

## Weaknesses
W1. [Must-Fix / Should-Fix / Minor] ...
W2. ...

## Questions
Q1. ...

## Missing References
...

## Overall Assessment
Score: X.X
Confidence: X/5
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-23T06:41:54.549301+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-23T06:41:54.549744+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-23T06:41:58.738259+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 1011 · 2026-05-23T06:42:01.197591+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1012 · 2026-05-23T06:42:10.298234+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria and Dimensions

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors for main papers.

The review recommendation scale includes the following dimensions:

- 5 = Consider for Award: papers that could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)
-
…[truncated 877 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 11559
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-23T06:42:11.405320+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 578.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 502.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 545.2}], \"total_pages\": 20, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/a
…[truncated 77 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 10207
}
```

</details>

---


### Tool call

_source line 1014 · 2026-05-23T06:42:17.485727+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract ALL review form dimensions, scoring scales, and criteria descriptions. I need the complete list of dimensions reviewers must score, their scale ranges, and what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract ALL review form dimensions, scoring scales, and criteria descriptions. I need the complete list of dimensions reviewers must score, their scale ranges, and what each score means."
  }
}
```

</details>

---


### Tool call

_source line 1015 · 2026-05-23T06:42:17.888525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1016 · 2026-05-23T06:42:19.300393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1017 · 2026-05-23T06:42:19.501768+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1018 · 2026-05-23T06:42:19.908868+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2020
}
```

</details>

---


### Tool call

_source line 1019 · 2026-05-23T06:42:19.909263+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-23T06:42:20.919483+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-23T06:42:21.422416+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2122
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-23T06:42:21.422816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1023 · 2026-05-23T06:42:21.878227+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2376
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-23T06:42:21.878637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1025 · 2026-05-23T06:42:22.536147+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2626
}
```

</details>

---


### Tool call

_source line 1026 · 2026-05-23T06:42:22.536568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-23T06:42:22.741094+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1821
}
```

</details>

---


### Tool result

_source line 1028 · 2026-05-23T06:42:23.098250+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1675
}
```

</details>

---


### Tool result

_source line 1029 · 2026-05-23T06:42:23.752627+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1873
}
```

</details>

---


### Tool result

_source line 1030 · 2026-05-23T06:42:24.007259+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1470
}
```

</details>

---


### Tool result

_source line 1031 · 2026-05-23T06:42:24.161934+00:00_

# ACL Rolling Review Form Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: "Quite sure. I tried to check the important points carefully"
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- 5: "This study is one of the most thorough I have seen"
- 4: "This study provides sufficient support for all of its claims"
- 3: "This study provides sufficient support for its main claims"
- 2: "Some of the main claims are not sufficiently supported"
- 1: "This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- 5: "I would recommend this paper to others and/or attend its presentation"
- 4: "I would mention this paper to others"
- 3: "I might mention some points of this paper to others"
- 2: "This paper does not resonate with me, but it might with others"
- 1: "This paper does not resonate with me, and I don't think it would with others"

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- 5: Consider for Award
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- 5: "They could easily reproduce the results"
- 4: "They could mostly reproduce the results"
- 3: "They could reproduce the results with some difficulty"
- 2: "They would be hard pressed to reproduce the results"
- 1: "They would not be able to reproduce the results"

## 6. **Datasets**
Scale: 1-5
- 5: Enabling new research choices
- 4: Useful for ongoing work
- 3: Potentially useful
- 2: Documentary value only
- 1: No usable datasets

## 7. **Software**
Scale: 1-5
- 5: Enabling new research choices
- 4: Useful for ongoing work
- 3: Potentially u
…[truncated 306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6676
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-23T06:42:31.401439+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "9-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "9-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-23T06:42:32.556815+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 536.9}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 470.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 431.9}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.7}], \"total_pages\": 20, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_
…[truncated 91 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-23T06:42:35.375762+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1035 · 2026-05-23T06:42:35.930591+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1036 · 2026-05-23T06:42:36.938132+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1562
}
```

</details>

---


### Tool call

_source line 1037 · 2026-05-23T06:42:36.938566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1038 · 2026-05-23T06:42:37.444832+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1514
}
```

</details>

---


### Tool call

_source line 1039 · 2026-05-23T06:42:37.445258+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-23T06:42:37.801469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-23T06:42:39.060056+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2121
}
```

</details>

---


### Tool call

_source line 1042 · 2026-05-23T06:42:39.060481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 1043 · 2026-05-23T06:42:39.463469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1044 · 2026-05-23T06:42:39.865157+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---
