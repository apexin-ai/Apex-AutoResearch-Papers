# Research conversation: [PROJECT BOOTSTRAP] 项目: nlp_variance_gtheory | Loop #1 | 阶段: MVP 验证 你刚立项，这是一个新项目的首次启动。 ## 必读: IDEA_BRIEF.md **立刻 Read `w — Part 5 of 6

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../research-conversation-project-bootstrap-nlp-variance-gtheory-loop-1-mvp-idea-brief-md-read-w.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/f7/f77133c922f3bfec7c12.json)

## Round 166

### Tool result

_source line 1295 · 2026-05-21T03:11:58.134Z_

<details><summary>↩ Tool result · `toolu_01CZeDHavSkHvBDD2CFSVZ75`</summary>

```text
Error: result (589,229 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-projects-nlp-variance-gtheory--claude-sessions-director-754d9c1f/10a54869-31d0-4dae-bcb8-806914c682ec/tool-results/mcp-agent-ml-research-feishu_read_chat_history-1779333118130.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-projects-nlp-variance-gtheory--claude-sessions-director-754d9c1f/10a54869-31d0-4dae-bcb8-806914c682ec/tool-results/mcp-agent-ml-research-feishu_read_chat_history-1779333118130.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-projects-nlp-variance-gtheory--claude-sessions-director-754d9c1f/10a54869-31d0-4dae-bcb8-806914c682ec/tool-results/mcp-agent-ml-research-feishu_read_chat_history-1779333118130.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b8ce20c-481a-46f6-98b3-4989722c48c1",
  "isSidechain": false,
  "promptId": "8a5b1a73-827a-4f60-a50c-f013e2c40e39",
  "type": "user",
  "uuid": "2c95eceb-deb6-4a33-92b5-db2ed6459f91",
  "toolUseResult": "Error: result (589,229 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-projects-nlp-variance-gtheory--claude-sessions-director-754d9c1f/10a54869-31d0-4dae-bcb8-806914c682ec/tool-results/mcp-agent-ml-research-feishu_read_chat_history-1779333118130.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-projects-nlp-variance-gtheory--claude-sessions-director-754d9c1f/10a54869-31d0-4dae-bcb8-806914c682ec/tool-results/mcp-agent-ml-research-feishu_read_chat_history-1779333118130.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-projects-nlp-variance-gtheory--claude-sessions-director-754d9c1f/10a54869-31d0-4dae-bcb8-806914c682ec/tool-results/mcp-agent-ml-research-feishu_read_chat_history-1779333118130.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"messages\": [{\"messageId\": \"om_x100b6fd0d51be0a4b4a6594ca10f739\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779321277533\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — worst | dream_20260520T222113]  · Overall: weak reject Review Report: \\\"Variance Decomposition Is a Measurement, Not a Fact\\\" Dream ID:  20260520T222113 |  Review Mode:  Full (2 Reviewers + Roundtable) Reviewer Assignments -  R1  — Methodology & Experiments (Score: 4/6, Confidence: 4/5) -  R2  — Novelty & Related Work (Score: 3/6, Confidence: 4/5) 1. Paper Summary The paper applies Generalizability Theory to LLM evaluation variance across 5 benchmarks, 4–6 models, and multiple infrastructure × methodology factors (172,800–230,400 observations per experiment). It makes three claims: (1) item dominance estimates are sample-unstable (CV=33%), (2) model×item interaction (33%) is the largest overlooked component when model is treated as a crossed facet, and (3) D-study reproducibility budgets converge across benchmarks but carry ±190-item CIs rendering benchmark-specific recommendations meaningless. The framing: \\\"variance decomposition is a measurement, not a fact.\\\" 2. R1 Review: Methodology & Experiments Strengths -  Impressive experimental scale.  ~ 4M total records across 8 experiments, 5 benchmarks, 6 models. The factorial designs are well-constructed and the confound correction (V0 enforce_ eager) is a genuine contribution. -  Model-as-facet reanalysis is well-executed.  The item_ id drop from 37.8%→15.2% with model×item absorbing the difference is a clean, interpretable result that challenges standard practice. -  Separability analysis across hardware.  The infra×method jump from 1.5% (single-GPU) to 5.5% (multi-GPU) is well-demonstrated and practically important. -  D-study projections with uncertainty.  Reporting bootstrap CIs on reproducibility budgets is methodologically sound practice that prior work omits. Weaknesses -  Centerpiece claim rests on thin evidence.  The CV=33% finding (Exp 1b) uses only 3 item samples, 1 model (Llama-3.1-8B), 1 benchmark (MMLU). Three data points cannot reliably estimate a coefficient of variation. The CV itself has enormous uncertainty — it could plausibly be 15% or 50%. A claim that \\\"all prior single-decomposition studies over-commit\\\" requires far more resamples (30+ recommended) and generalization across models and benchmarks. -  Bootstrap validity concern.  Resampling 200 items with replacement creates ~ 127 unique items per bootstrap sample, producing duplicate observations that violate the independence assumptions of the G-theory model. The resulting CIs may be miscalibrated. The paper does not discuss this issue or compare with jackknife/subsampling alternatives. -  Cross-benchmark design asymmetry.  MMLU uses a 3×3 precision-temperature grid while other benchmarks use 2×2. Comparing variance percentages across different factorial structures without matched-design sensitivity analysis is methodologically questionable. -  G-coefficient interpretation.  The paper reports G=0.32 for 200 items as evidence of \\\"inherent low reliability,\\\" but standard MMLU evaluation uses all ~ 14K items. D-study projection to full benchmark size would likely yield G>0.90, substantially weakening the alarm about current practice. -  Zero figures.  A paper about variance decomposition with 18 tables and no figures is a critical presentation failure. Stacked bar charts, waterfall diagrams, and bootstrap density plots (all described in the design context) would dramatically improve comprehension. -  Thin secondary experiments.  Exp 5 (n=2 14B models, scale/architecture confounded) contributes near-zero evidential value. Exp 7 (LayerCast) is a null result that could be a footnote. Exp 6 (RoBERTa fine-tuning) uses encoder-only architecture, making the inference-training comparison apples-to-oranges for the LLM evaluation claim. Questions for Authors 1.  Why only 3 item resamples for the centerpiece claim? What is the bootstrap CI on the CV=0.33 estimate itself? 2.  How do you handle duplicate items in bootstrap resamples given G-theory's independence assumptions? 3.  What would G be for MMLU at its full ~ 14K item size under your D-study projections? 4.  The MMLU experiments use a richer factorial design than other benchmarks — have you verified that the cross-benchmark comparisons aren't confounded by design differences? R1 Score: 4/6 (Weak Accept) | Confidence: 4/5 3. R2 Review: Novelty & Related Work Strengths -  The resampling instability result is novel for ML evaluation.  Even if the concept is known in psychometrics, nobody has empirically demonstrated rank inversions across item samples for LLM evaluation variance decomposition. The qualitative finding (residual > item_ id in Sample 7) is striking. -  The bimodality→item_id correlation  (r=0.95) is an interesting mechanistic hypothesis that could guide benchmark design, even if underpowered (n=5 benchmarks). -  Engine confound correction  (V0 enforce_ eager reducing precision main effect from ~ 7% to 1.6%) is a valuable practical contribution for the community. -  Clear three-contribution structure  in the introduction makes claims easy to evaluate. Weaknesses -  The central conceptual claim is not novel.  \\\"Variance decomposition estimates have sampling variability\\\" is established in psychometric measurement theory (Brennan 2001, Chapter 8; Cardinet et al. 2010). The paper presents this as a discovery (\\\"we set out to build budgets and discovered the budget is unreliable\\\") without acknowledging that measurement theorists have known this for decades. For a measurement-literate audience, the surprise factor is low. -  Missing engagement with psychometric precedent.  The paper cites Shavelson & Webb (1991) and Brennan (2001) for G-theory basics but ignores their extensive discussion of variance component estimation error, sampling variability of G-coefficients, and the known sensitivity to universe definition (fixed vs. random facets). The critique of Mesting (2026) for treating model as fixed is particularly problematic — model-as-fixed is a legitimate design choice when generalizing only to those specific models, not an \\\"error.\\\" -  Three claims are one finding stated three ways.  All three contributions reduce to \\\"variance component estimates are uncertain\\\": (1) they vary across item samples, (2) they vary across model specifications, (3) the D-study projections derived from them are also uncertain. This is a single observation about estimation uncertainty, not three independent contributions. -  Purely diagnostic — no constructive contribution.  The three recommendations (report resampling stability, treat model as crossed, add CIs to budgets) are standard statistical advice. The paper does not provide a corrected estimation procedure, a practical resampling protocol, a software tool, or a concrete recommended minimum number of resamples. Practitioners reading this paper learn that their current approach is wrong but not what to do instead. -  The narrative pivot feels post-hoc.  The experiment design context reveals the paper originally aimed to demonstrate a \\\"cross-benchmark variance gradient\\\" (knowledge→reasoning). When this failed (spread=9pp, wrong direction), the paper reframed around instability. The narrative \\\"we set out to build budgets and discovered they're unreliable\\\" is technically accurate but obscures that the current framing was not the original research question. -  Bimodality correlation is underpowered.  r=0.95 from n=5 benchmarks has a 95% CI of approximately [ 0.63, 0.99 ] — wide enough to be consistent with moderate or near-perfect correlation. Moreover, bimodality mechanistically drives item-level variance almost by definition (bimodal difficulty → high between-item variance), making this partially tautological. -  Overclaiming.  \\\"Every prior study that reports a single variance decomposition... has presented one draw from a high-variance distribution as a finding\\\" is a sweeping claim supported by 3 resamples on 1 model × 1 benchmark. The paper does not test whether other studies' decompositions would show similar instability under their specific designs. -  Paper bloat.  18 tables across 13 pages with zero figures. Experiments 5 (14B extension), 6 (fine-tuning), and 7 (LayerCast) collectively contribute ~ 2 pages of marginal findings. The paper would be stronger at 10 pages with 4 core experiments and actual figures. Missing Related Work -  Cardinet, Johnson, & Pini (2010): \\\"Applying Generalizability Theory Using EduG\\\" — extensive treatment of variance component sampling variability -  Webb, Shavelson, & Haertel (2006): On reliability of G-study variance components -  Marcoulides (1996): On estimating variance components in G-theory -  The IRT literature on item sampling (e.g., Lord & Novick, 1968; van der Linden & Hambleton, 1997) covers similar ground on the instability of item parameter estimates Questions for Authors 1.  How do you respond to the argument that variance component estimation uncertainty is already well-characterized in Brennan (2001, Ch. 8) and Cardinet et al. (2010)? What specifically is new beyond applying known concepts to a new domain? 2.  The critique of model-as-fixed analysis assumes that prior work intended to generalize across models. If Mesting (2026) deliberately fixed model to study judge-specific behavior, how is this an error rather than a design choice? 3.  Can you provide a concrete, actionable resampling protocol? How many resamples, what sample sizes, what estimator? 4.  The r=0.95 bimodality correlation has n=5. Have you considered that this is partially tautological (bimodal item difficulty → high item variance, by construction)? 5.  Would you characterize your contribution as \\\"discovering that measurement error exists\\\" or as \\\"quantifying its magnitude in a specific domain\\\"? If the latter, how robust is the quantification with only 3 resamples? R2 Score: 3/6 (Weak Reject) | Confidence: 4/5 4. Roundtable Discussion Step 2: Cross-Sharing R1 responds to R2's novelty concern:  R1 acknowledges that the conceptual point is known in psychometrics but argues the empirical demonstration in the LLM evaluation context — particularly the rank inversions and the magnitude of model×item interaction — provides actionable new information to the ML community. However, R1 concedes that 3 resamples severely undermines the quantitative claim (CV=33% specifically). R2 responds to R1's methodology points:  R2 agrees that the bootstrap validity concern (duplicate items violating independence) is serious and not addressed. R2 also agrees that the G-coefficient interpretation at 200 items vs. full benchmark size is misleading. Step 3: Convergence Points of agreement (both reviewers): 1.  The zero-figures presentation is unacceptable for a variance decomposition paper. This alone would warrant revision. 2.  The centerpiece claim (CV=33%) rests on only 3 data points from 1 model and 1 benchmark — far too thin for the sweeping conclusion that \\\"all prior single-decomposition studies\\\" are unreliable. 3.  Experiments 5 (14B), 6 (fine-tuning with RoBERTa), and 7 (LayerCast) are bloat that should be cut or moved to appendix. 4.  The model-as-facet reanalysis (Exp 4) is the strongest individual result — the 37.8%→15.2% shift with model×item=33% is clean and important. 5.  The paper is purely diagnostic with no constructive solution beyond standard statistical advice. 6.  The bootstrap methodology needs more careful treatment of independence assumptions. Points of disagreement: -  R1 gives more credit for experimental scale and practical value to the ML community; R2 weights novelty relative to psychometric precedent more heavily. -  R1 sees the paper as publishable with revisions; R2 sees fundamental framing issues that require a major reconceptualization. Step 4: Score Convergence R1 initial: 4 (Weak Accept). R2 initial: 3 (Weak Reject). After discussion, R1 moves to  3–4 , acknowledging that the thin evidence base for the centerpiece claim (3 resamples) is more damaging than initially assessed. R2 holds at  3 , noting that even with more resamples, the conceptual novelty concern remains. Consensus score: 3 (Weak Reject) 5. Consolidated Assessment Overall Score: 3/6 (Weak Reject) Meta-Review Summary This paper attempts an ambitious meta-methodological critique of variance decomposition in LLM evaluation, arguing that decomposition estimates are themselves unreliable measurements. The experimental scale is impressive (~ 4M observations across 8 experiments), and individual results — particularly the model-as-facet reanalysis showing model×item interaction at 33% — are genuinely informative for the ML evaluation community. However, the paper suffers from several compounding weaknesses that collectively prevent acceptance: 1.  The centerpiece claim is underpowered.  CV=33% from 3 item resamples on 1 model × 1 benchmark cannot support the conclusion that all prior single-decomposition studies are unreliable. The CV estimate itself has enormous uncertainty and the generalization across models/benchmarks is untested. 2.  Conceptual novelty is limited.  The central insight — that variance component estimates have sampling variability — is well-established in the psychometric literature the paper builds on. The paper would be stronger if it acknowledged this precedent and focused on quantifying the problem's magnitude in the LLM evaluation domain, rather than framing it as a discovery. 3.  No constructive contribution.  The recommendations (\\\"report CIs,\\\" \\\"treat model as crossed,\\\" \\\"add error bars to budgets\\\") are standard statistical practice. The paper diagnoses a problem but offers no tool, protocol, or corrected estimator. 4.  Presentation is inadequate.  18 tables and zero figures in a variance decomposition paper. Several experiments (5, 6, 7) contribute marginal evidence and inflate the paper without strengthening core claims. 5.  Methodological gaps.  Bootstrap validity under item duplication, G-coefficient interpretation at subsampled vs. full benchmark size, and cross-benchmark design asymmetry are unaddressed. Actionable Revision Guidance To reach acceptance at a top venue, the authors should: -  Increase resamples to 30+ and extend across multiple models/benchmarks  to make the CV estimate credible -  Acknowledge psychometric precedent  (Brennan 2001 Ch. 8, Cardinet et al. 2010) and reframe as \\\"quantifying a known problem in a new, practically important domain\\\" -  Cut Experiments 5, 6, 7  and use the space for figures and deeper analysis of core results -  Add figures : stacked bars for variance decomposition comparison, waterfall for model-fixed→crossed shift, bootstrap density plots, D-study projection curves with CI bands -  Provide a constructive contribution : a concrete resampling protocol, minimum resample recommendations, or a software package -  Address bootstrap methodology : discuss independence violations from item duplication, compare with jackknife/subsampling, report calibration checks -  Reframe the three claims honestly : they are one finding (estimation uncertainty) demonstrated through three lenses, not three independent contributions Scores Summary\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd0dd5054b4b30e0689e9a42d8\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779321146099\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — best | dream_20260520T222113]  · Overall: weak accept (4/6) Reviewer R1: Methodology Soundness and Experimental Rigor 1. Summary This paper applies Generalizability Theory (G-theory) to decompose variance sources in LLM evaluation across five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), six models (4 at 7--9B, 2 at 14B), and approximately 4 million evaluation records. The design crosses infrastructure facets (numerical precision, GPU hardware) with methodology facets (prompt template, random seed, temperature, option ordering) and a measurement facet (item selection). Three claims are advanced: (1) item dominance is benchmark-conditional, following a monotonic 35pp gradient from knowledge retrieval (56%) to complex reasoning (21%); (2) direct infrastructure x methodology interactions are negligible ( <0.3%), confirming separability; (3) D-study reproducibility budgets reverse across task types (MMLU is item-limited, GSM8K is seed-limited), rendering universal evaluation recipes illusory. Eight experiments are presented, including a model-as-facet reanalysis, item resampling stability test, multi-hardware separability test, 14B scale extension, RoBERTa fine-tuning study, LayerCast precision mitigation, and MATH benchmark extension. 2. Methodology Assessment 2.1 G-Theory Application The application of G-theory is broadly correct and represents a natural fit for the research question. The crossed random-effects design, with item as the measurement facet and prompt/seed/temperature/ordering/precision as crossed facets, is the canonical G-theory setup for studying measurement dependability. The paper correctly distinguishes G-studies (variance decomposition) from D-studies (projection under alternative designs), which is the primary advantage of G-theory over standard ANOVA. However, there are several methodological concerns: (a) Object of measurement is underspecified.  In classical G-theory, the \\\"object of measurement\\\" (the entity whose score you want to generalize) must be clearly defined. In educational testing, this is typically the person. Here, the paper appears to treat benchmark accuracy as the object, but accuracy is an aggregate over items -- not a single observation. The paper decomposes item-level binary responses (correct/incorrect), which means the effective object of measurement is the  item-level response . The G coefficient then measures how well item-level responses generalize across facet conditions. This is a valid but nonstandard application. The paper should explicitly state what universe score is being estimated and what generalization is being made. The current framing conflates \\\"reliability of a benchmark score\\\" with \\\"stability of item-level responses across conditions,\\\" and these are different quantities. (b) Model-as-fixed vs. model-as-facet transition is handled well but incompletely.  The paper correctly identifies that pooling across models inflates item_ id (from 56% to 49.2% on MMLU when model is added as a facet). The model x item interaction (10.2%) is properly extracted. However, the paper does not discuss whether model should be treated as random or fixed from a G-theory perspective. With only 4 models drawn from a specific population (7-9B instruction-tuned open-weight models), the \\\"random\\\" assumption implies these 4 are a random sample from some universe of models -- a dubious claim given the deliberate selection. If model is fixed, model x item is not an error component but a systematic interaction, and the G coefficient computation changes. The paper should discuss this inferential scope issue. (c) Henderson Method I vs. III naming inconsistency.  The paper claims \\\"Henderson's Method III (expected mean squares)\\\" in Section 3.1, but the balanced fully-crossed design used here would typically employ Henderson Method I (which uses Type-I sums of squares and expected mean squares for balanced designs). Method III is Searle's approach for unbalanced designs. For the balanced design in exp-001, Method I is both simpler and more appropriate. This is either a naming error or an implementation concern -- the paper should clarify which method was actually used and verify consistency with the code. (d) Binary response variable creates floor/ceiling artifacts.  All primary analyses use binary correct/incorrect as the response. For items near 0% or 100% accuracy across conditions, variance is mechanically compressed (a Bernoulli variable with p near 0 or 1 has low variance). This means item_ id partially reflects the  range  of item difficulties rather than genuine measurement-relevant variance. The logprob analysis in Appendix B (item_ id drops to 42.8%) partially addresses this, but it is relegated to a 4-line appendix rather than being integrated into the main analysis. A continuous response variable would provide a more principled decomposition, and the paper should discuss the implications of using binary outcomes for variance component estimation. 2.2 Crossed/Nested Design Appropriateness The fully crossed design for MMLU (exp-001) is the gold standard for G-theory and is correctly specified. All facet levels are combined with all other facet levels, enabling clean estimation of all main effects and two-way interactions. The reduced designs for non-MMLU benchmarks (2 precisions x 2 temperatures vs. 3 x 3 for MMLU) are a pragmatic budget-driven decision but create a methodological asymmetry that is inadequately discussed. Variance percentages are  relative to total variance , and the total variance changes when you remove facet levels. Removing the FP32 precision level (which shows the highest deviation post-confound-fix) and the third temperature level changes the denominator of all percentage calculations. The cross-benchmark gradient (Table 4) compares percentages from designs with different factorial structures, which is a validity concern. The paper should either: (a) report a sensitivity analysis re-running MMLU with the reduced 2x2 design to confirm the gradient holds under matched designs, or (b) explicitly discuss why the design asymmetry does not invalidate the comparison. 2.3 Bootstrap Procedures The bootstrap procedure (1,000 item-level resamples) is appropriate in principle for constructing CIs on variance components, as parametric CIs for variance components in mixed models are notoriously unreliable. However: (a) Resampling items with replacement in a balanced design creates duplicates.  With 200 items and replacement, each bootstrap draw contains approximately 127 unique items (by the coupon collector / birthday problem). Duplicate items have identical response vectors across all conditions, violating the independence assumption in the ANOVA decomposition. This likely  deflates  the variability of item_ id estimates (making CIs too narrow), because the resampled datasets have artificially correlated item effects. A cluster bootstrap that resamples item-condition blocks without re-indexing duplicates, or a delete-d jackknife, would be more appropriate. The tight CI widths (4-6pp) should be interpreted with this caveat. (b) Nested bootstrap for D-study projections is not described.  The D-study projections in Table 11 presumably require computing variance components for each bootstrap sample and then projecting G under hypothetical designs. This is a two-stage procedure (bootstrap variance components -> project G), and the uncertainty in G projections depends on the joint distribution of all variance components, not just item_ id. The paper reports CIs on item_ id but not on D-study projections. The claim that \\\"420 items suffice for G >= 0.90 on MMLU\\\" has no associated uncertainty -- but given the bootstrap CIs on item_ id (46.1-52.3%), the projected item count for G >= 0.90 could range substantially. This uncertainty should be reported. 3. Experimental Rigor 3.1 Exp 1b: Item Resampling Stability The resampling stability test uses 1 model (Llama-3.1-8B) x 1 benchmark (MMLU) x 3 independent 200-item samples x 54 conditions per sample = 32,400 records. The CV of 4.1% on item_ id across samples is reassuring but has limited generalizability: -  Only 1 model tested.  The paper claims item resampling stability as a general property, but models with different accuracy distributions (e.g., Mistral-7B at 64.1% vs. Gemma-2 at 69.1%) might show different resampling sensitivity. A model near the population mean difficulty could show lower CV than one at the extremes. -  Only 3 samples.  A CV computed from 3 data points has essentially no statistical power. The standard error of a CV from n=3 is enormous. The paper would be better served by reporting the bootstrap distribution of variance components (which they have from exp-004, 1000 resamples) as the stability analysis, rather than the 3-sample CV. -  Only MMLU.  The critical question is whether resampling stability holds for GSM8K and MATH, where item_ id is much lower (21-25%) and closer to competing components. A CV of 4.1% on a 55% estimate is comfortable (55 +/- 2.3pp). But a CV of 4.1% on a 21% estimate would be 21 +/- 0.9pp -- still rank-1, but now within striking distance of temp x item at 20.8%. The resampling stability argument is weakest precisely where it matters most (reasoning benchmarks), and it is not tested there. Recommendation:  Replace the 3-sample CV with the bootstrap CI analysis from exp-004, and extend item resampling stability to at least one reasoning benchmark (GSM8K or MATH). 3.2 200-Item Sample Size Using 200 stratified items per benchmark is a reasonable choice that balances statistical power against computational cost. The stratification (by MMLU subject, presumably by difficulty for other benchmarks) ensures representative coverage. However: -  For MMLU (14K total items), 200 items is 1.4% of the pool -- adequate for stable percentage-based decompositions. -  For GSM8K (1,319 items in the test set), 200 items is 15.2% -- a much larger fraction, which reduces the effective resampling space. -  For MATH (5,000 items in the test set), 200 items is 4% -- again adequate. -  For ARC-Challenge (1,172 items), 200 items is 17.1%. The paper does not discuss how the item pool size interacts with the variance decomposition. When sampling 15-17% of the pool (GSM8K, ARC), the resampling stability results from MMLU (1.4% sampling fraction) may not transfer. This should be acknowledged. 3.3 Hardware Experiment (Exp 3): Confounds The multi-hardware study uses 2 GPU types. This is a minimal design for estimating hardware effects. Specific concerns: -  n=2 GPU types provides 1 degree of freedom for the hardware main effect.  This is barely identifiable in a variance decomposition. The hardware main effect (0.4%) and hardware x item (1.6%) estimates are based on between-GPU differences that could reflect any systematic difference between the two specific GPUs (driver version, cooling, memory controller characteristics, vLLM kernel selection), not hardware architecture per se. -  The paper does not specify the second GPU type.  The review context mentions \\\"RTX PRO 6000 + second GPU\\\" but the paper says only \\\"2 GPU types.\\\" For a claim about hardware separability to be meaningful, readers need to know whether these are architecturally similar (e.g., two Ampere-class GPUs) or substantially different (e.g., Ampere vs. Hopper). Two GPUs from the same architecture family would underestimate hardware variance. -  No confound control for driver/CUDA version differences between GPUs.  If the two GPUs run different CUDA toolkit versions or vLLM builds, observed differences reflect the software stack, not the hardware. Despite these limitations, the separability conclusion (<0.3% direct infra x method) is robust: even if hardware variance is underestimated due to limited GPU diversity, the  interaction  with methodology would need to be orders of magnitude larger to matter. The null result is defensible. 3.4 Fine-Tuning Experiment (Exp 6): RoBERTa Using RoBERTa-large for the fine-tuning study is a significant architectural mismatch. The inference experiments use 7-14B decoder-only autoregressive models on generation tasks; the fine-tuning experiment uses a 355M encoder-only model on classification tasks. The facets are also different (learning rate and data shuffle replace prompt template and temperature). This means: -  The cross-paradigm comparison (Table 13) compares variance percentages from incomparable designs. Item_ id being rank-1 in both does not constitute evidence of cross-paradigm generalization -- it could reflect the fact that any assessment with varying item difficulties will show item dominance, which is a tautological property of the design rather than an empirical finding. -  The claim that \\\"infrastructure effects are negligible in fine-tuning too\\\" is trivially expected for RoBERTa-large, which has no autoregressive error accumulation and was trained in FP32/FP16. -  The 1,728 fine-tuning runs (432 per task x 4 tasks) is a reasonable scale, but the number of  items  per evaluation is not specified. If each run evaluates the full dev/test set, the item-level observation count is much larger than 1,728. The experiment adds limited value to the core narrative.  Fine-tuning a decoder LLM (e.g., Llama-3.1-8B with LoRA on GSM8K, crossing seed x learning rate x data shuffle x items) would directly test cross-paradigm generalization. The current RoBERTa experiment tests a different claim entirely: that G-theory can decompose fine-tuning variance in encoder-only classification, which is unsurprising given that the same framework has been used in educational testing (which also involves classification-like assessments). 3.5 14B Scale Extension (Exp 5) With n=2 models (Qwen3-14B, DeepSeek-R1-Distill-14B), this experiment has minimal statistical power for any claim about scale effects. The two models differ in both scale and architecture: DeepSeek-R1-Distill-14B is a reasoning-distilled model with fundamentally different training objectives than Qwen3-14B. Scale and training methodology are fully confounded. The finding that both 14B models fall within the 8B range for item_ id is reassuring but does not demonstrate scale invariance -- it demonstrates that these two specific 14B models have similar variance profiles to the four 8B models. The elevated temp x item (8.8%) and seed x item (5.2%) for DeepSeek-R1-Distill-14B is attributed to \\\"reasoning distillation introducing implicit chain-of-thought tendencies\\\" (Section 8.1) -- this is a plausible but untestable hypothesis from n=1. The experiment contributes at best weak corroborating evidence. Two more 14B models (ideally from different training paradigms) would make the scale claim credible. 3.6 LayerCast (Exp 7) This is a null result experiment: LayerCast adds 0.03% precision variance, which is negligible. The experiment is methodologically clean but its contribution is marginal -- it confirms that precision is not a major concern (already established by exp-001 post-confound-fix) and evaluates a specific mitigation technique. For the paper's core claims, it is dispensable. Its inclusion creates a breadth-over-depth tradeoff that weakens the overall narrative. 4. Statistical Concerns 4.1 CV = 4.1% from 3 Samples The original review context described CV = 33% from 3 samples -- the paper now reports CV = 4.1%, which is a dramatic improvement, presumably reflecting better stratification and larger item counts in the revised design. However, a CV computed from n=3 is a point estimate with essentially no precision. The 95% CI on a CV from 3 observations is extremely wide (roughly 0.7x to 5x the point estimate under normal assumptions). The paper should not present CV = 4.1% as a precise number but rather as \\\"CV  < 15%\\\" or similar bounded claim. 4.2 Bootstrap with 1,000 Resamples 1,000 bootstrap resamples is adequate for percentile-based 95% CIs (Monte Carlo error approximately 0.5pp for the tail quantiles). The concern is not the number of resamples but the resampling unit: resampling items with replacement in a balanced design creates duplicate observations that violate independence assumptions in the ANOVA decomposition used within each bootstrap iteration. This is a known problem in bootstrap variance component estimation. The bias direction is toward underestimating CI width. 4.3 D-Study Projection Uncertainty D-study projections are deterministic functions of variance components: given estimated components, the projected G under any hypothetical design is a closed-form calculation. The uncertainty comes entirely from the variance component estimates. The paper reports CIs on item_ id (Table 8) but not on D-study projections. This is a significant omission. The practical recommendation \\\"use 420 items for G >= 0.90 on MMLU\\\" has no associated uncertainty band. If item_ id is at the upper end of its CI (52.3%), more items are needed; if at the lower end (46.1%), fewer suffice. The authors should propagate bootstrap uncertainty through the D-study projection to report a CI on the required item count. 4.4 D-Study Projection for GSM8K: Arithmetic Anomaly Table 10 shows that reducing items from 200 to 150 while keeping prompts=3 and seeds=10  increases  G from 0.68 to 0.90. In the G formula, reducing n_ items should  decrease  G (because item-related error terms are divided by n_ items). The only way G can increase with fewer items is if the optimization simultaneously changes other facet counts or if the table presents results from a joint optimization that is not monotonic in each facet individually. This anomaly is not explained and raises questions about the D-study optimization procedure. If the procedure involves multi-facet grid search, it should be documented; if it is an error, it should be corrected. 5. Coverage vs. Depth The paper runs 8 experiments across 20 tables. Several experiments feel thin: -  Exp 5 (14B):  n=2 models, confounded scale/architecture, 1 paragraph of analysis. Contributes weak corroboration. -  Exp 7 (LayerCast):  Null result for a specific mitigation technique. One table, 1 paragraph. Could be a footnote. -  Exp 6 (Fine-tuning):  Architecturally disjoint from the main study. Two tables, 2 paragraphs. The cross-paradigm claim it supports is unsustainable with encoder-only models. Recommendation:  Move Exp 5, 6, and 7 to an appendix. Use the freed space for: (a) figures -- the paper has zero figures, which is a critical presentation weakness for a variance decomposition study; (b) deeper analysis of the core gradient (Exp 1+2+8), including per-item analysis showing which items drive the benchmark-conditional variance shift; (c) D-study sensitivity analysis with propagated bootstrap uncertainty. Fewer, deeper experiments would produce a stronger paper. The current breadth creates an impression of thoroughness but at the cost of inadequate depth on several secondary experiments. 6. Strengths -  Cross-benchmark variance gradient is a genuine contribution.  The monotonic shift from item-dominated (56%) to interaction-dominated (21%) across five benchmarks, with non-overlapping bootstrap CIs, is novel, well-supported, and explanatory. It resolves the apparent contradiction between prior single-benchmark studies. -  Experimental scale is impressive.  Over 1M records for the MMLU full-factorial alone; approximately 3-4M total. This is among the largest factorial designs in the LLM evaluation literature. -  Engine confound discovery is independently valuable.  The identification and correction of the vLLM FP32/BF16 engine routing difference (V1 CUDA graph vs. V0 eager) is a methodological contribution that benefits any researcher using vLLM for precision-sensitive comparisons. -  D-study facet effectiveness inversion is the most actionable finding.  Items:seeds ratio shifting from 14.2:1 (MMLU) to 0.8:1 (GSM8K) has direct practical implications. This is the quantitative crystallization of \\\"no universal recipe.\\\" -  Model-as-facet reanalysis properly handles model heterogeneity.  Extracting model x item (10.2% on MMLU) while preserving item_ id as rank-1 and the gradient is a clean analytical move that addresses a legitimate concern from prior reviews. -  Separability confirmation is useful.  While a null result, confirming  <0.3% direct infrastructure x methodology interaction across all benchmarks provides empirical license for isolated-factor study designs. -  REML vs. Henderson sensitivity analysis  with  <1.4pp divergence and identical component rankings adds robustness. -  Item resampling stability  (despite the n=3 limitation) provides evidence that the variance structure is not an artifact of specific item selection. 7. Weaknesses Major -  (W1) D-study optimization procedure is undocumented.  The joint-optimal allocations in Table 11 (e.g., GSM8K: 150 items, 3 prompts, 10 seeds) appear to come from a multi-facet grid search, but the paper describes only single-facet D-study sweeps. The GSM8K anomaly (150 items yielding G=0.90 while 200 items with the same prompts/seeds yields G=0.68) is unexplained and arithmetically suspicious. Practitioners will use these specific numbers; they must be derived from a transparent procedure. -  (W2) Object of measurement and G coefficient interpretation.  The paper conflates the G coefficient (which measures generalizability over included facets relative to the universe of admissible observations) with overall measurement reliability. G = 0.22 for \\\"current practice\\\" on MMLU does not mean MMLU is unreliable in a practical sense -- it means that item-level binary responses are not stable across prompt/seed/temperature conditions. Since practitioners use  aggregate accuracy  (averaging over 200+ items and potentially multiple conditions), the effective reliability of the aggregate score is much higher. The paper's alarming framing (\\\"below the minimum threshold accepted in any measurement discipline\\\") risks misleading practitioners by applying item-level G to benchmark-level decisions. -  (W3) Bootstrap resampling with replacement in balanced designs.  Duplicate items in bootstrap samples violate the independence assumption of the within-bootstrap ANOVA, likely producing CIs that are too narrow. This affects the statistical significance claims for the gradient (non-overlapping CIs across benchmarks). The paper should report results from a cluster bootstrap or jackknife as sensitivity analysis. -  (W4) Cross-benchmark design asymmetry.  Comparing variance percentages across benchmarks when MMLU uses 3 precisions x 3 temperatures and others use 2 x 2 is methodologically questionable. The total variance denominator differs, and removing facet levels redistributes percentage shares. No sensitivity analysis is provided. -  (W5) Zero figures.  For a paper about variance decomposition across benchmarks, the absence of any visualization is a critical presentation failure. Stacked-bar charts, D-study projection curves, and bootstrap CI forest plots are standard idioms in this literature and would dramatically improve communication of the key findings. Moderate -  (W6) Fine-tuning experiment (Exp 6) is architecturally mismatched.  RoBERTa-large on classification tasks does not test cross-paradigm generalization to decoder-only LLM fine-tuning. The different facet structure (LR/shuffle vs. prompt/temperature) makes the comparison non-parallel. -  (W7) 14B scale extension (Exp 5) has n=2 with confounded scale/architecture.  Cannot separate scale effects from training methodology effects (reasoning distillation). -  (W8) Item resampling stability tested on only 1 model x 1 benchmark x 3 samples.  Not tested on reasoning benchmarks where the stability claim matters most. -  (W9) Hardware experiment uses only 2 unspecified GPU types.  The second GPU is never identified, and n=2 provides minimal diversity for hardware variance claims. -  (W10) Missing comparison with IRT-based benchmarking.  tinyBenchmarks recommends approximately 100 items for MMLU; the D-study recommends 420. This 4x discrepancy is never discussed. Since both address \\\"how many items suffice?\\\", the paper should explain why the answers differ and what each framework optimizes. 8. Questions for Authors 1.  D-study arithmetic:  In Table 10 (GSM8K), how does reducing items from 200 to 150 (with identical prompts=3, seeds=10) increase G from 0.68 to 0.90? This appears to violate the monotonicity of G in n_ items. Please describe the exact optimization procedure and verify these numbers. 2.  Object of measurement:  What is the universe score being estimated? Is it the expected accuracy of a model on the full item population, or the expected item-level response across all facet conditions? These yield different G coefficients, and the practical implications differ substantially. If the former, how do you handle the aggregation from items to benchmark score in the G formula? 3.  Bootstrap validity:  Have you conducted any calibration study (e.g., comparing bootstrap CIs to parametric REML-based CIs or to a delete-d jackknife) to verify that your bootstrap procedure produces correct coverage? Given the duplicate-item concern, what is the effective number of unique items per bootstrap sample, and have you assessed whether this deflation affects CI width? 4.  Design asymmetry:  If you re-run the MMLU analysis using only 2 precisions (BF16/FP16) and 2 temperatures (matching the non-MMLU design), does item_ id remain at approximately 56%, or does it shift? How large is the shift, and does the gradient survive with matched designs across all benchmarks? 5.  G interpretation for practitioners:  Your D-study says MMLU needs 420 items for G >= 0.90. But the standard MMLU evaluation uses the full 14K items with 1 prompt and 1 seed. What is the G coefficient for the full 14K-item, 1-prompt, 1-seed evaluation? If it is already above 0.90 (which it likely is, given that item-related error shrinks with 70x more items), the practical alarm about \\\"current practice being inadequate\\\" is overstated. 9. Score Score: 4/6 (Weak Accept) Justification:  The paper presents a large-scale, technically competent G-theory analysis with a genuinely novel primary finding (the cross-benchmark variance gradient) that has both explanatory and practical value. The engine confound discovery is independently valuable. The D-study facet effectiveness inversion is the most actionable result. However, several methodological concerns prevent a higher score: (a) the D-study optimization procedure contains an unexplained arithmetic anomaly and is not documented; (b) the G coefficient interpretation risks misleading practitioners by conflating item-level generalizability with benchmark-level reliability; (c) the bootstrap procedure has a known bias from duplicate items in balanced designs; (d) the cross-benchmark gradient is derived from designs with different factorial structures; (e) secondary experiments (Exp 5, 6, 7) are thin and architecturally mismatched. The core contribution -- the gradient + D-study reversal -- merits publication, but the paper needs honest scoping of what its G coefficients actually measure, documented D-study optimization, design-matched gradient validation, and figures. 10. Confidence Confidence: 4/5 I have working knowledge of G-theory (Brennan 2001, Shavelson & Webb 1991), variance component estimation methods (Henderson, REML), bootstrap procedures for mixed models, and the LLM evaluation reproducibility literature. My main uncertainty is whether the D-study anomaly in Table 10 reflects a multi-facet optimization procedure that I am not recognizing, and whether the binary-response decomposition introduces biases beyond what I have identified. I am confident in the assessment of the experimental design, the bootstrap validity concern, and the G coefficient interpretation issue.\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd0dfda08a0b359cc70ee2e74a\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779321105605\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — worst | dream_20260520T222113]  · Overall: 3 — Weak Reject Review Report — Reviewer R2 (Novelty, Significance, Positioning, Writing) Paper:  \\\"Variance Decomposition Is a Measurement, Not a Fact: On the Instability of Reproducibility Budgets for LLM Evaluation\\\" Tier:  worst 1. Novelty Assessment 1a. \\\"Variance decomposition is a measurement\\\" framing This framing is  not novel in psychometrics or the broader measurement sciences . The instability of variance component estimates under resampling is a well-known phenomenon in G-theory. Brennan (2001, Ch. 8) explicitly discusses sampling variability of variance components and recommends bootstrap or jackknife standard errors. Shavelson & Webb (1991) note that component estimates depend on facet sample size and the specific levels sampled. The educational measurement literature has used resampling stability checks for decades (e.g., Cardinet, Johnson, & Pini, 2010). The paper presents this as a discovery (\\\"we set out to build budgets and discovered the budget is unreliable\\\"), but anyone trained in G-theory would expect variance component estimates to have sampling distributions. The CV=33% finding is noteworthy in the LLM context, but the epistemological claim is standard measurement theory repackaged as a revelation. Verdict:  The framing is novel  for the ML audience  but risks appearing naive to measurement-literate reviewers. The contribution is empirical (documenting the magnitude of instability in LLM evaluation), not conceptual. 1b. Model-as-facet vs. model-as-fixed This is  standard G-theory practice , not a novel insight. The distinction between random and fixed facets is one of the first topics covered in any G-theory course. Whether to treat a facet as random or fixed depends on whether one wants to generalize beyond the specific levels observed. Mesting (2026) treating model as fixed is a defensible design choice (she studies a specific set of models), not an error. The paper's claim that prior work \\\"inflates\\\" item variance by treating model as fixed conflates a design decision with a methodological flaw. The 22pp shift is informative but expected: adding any large facet as random will redistribute variance from existing components. Verdict:  The finding quantifies a known effect in a new domain. Useful, but cannot be positioned as a methodological contribution. 1c. Item resampling instability This is the paper's strongest novelty claim. To my knowledge,  no prior ML evaluation study has explicitly tested the resampling stability of variance components . Bouthillier et al. (2021) and Mesting (2026) report point estimates without stability analysis. The demonstration that CV=33% with rank inversions across item samples is a genuinely useful empirical contribution. However, the magnitude of the CV depends heavily on design specifics (200 items from a 14,000-item pool with heterogeneous subject difficulty is expected to produce high variability). With 3 resamples, the CV estimate itself is poorly estimated (the standard error of a CV from n=3 is enormous). The paper needs 10+ resamples to make the CV=33% claim credible. Verdict:  Novel for ML evaluation. Underpowered (only 3 resamples to estimate a CV). The contribution is real but the specific numbers are unreliable. 1d. Bimodality-item_ id correlation (r=0.95) This is  potentially interesting but mechanistically trivial  and computed from only 5 data points. An r=0.95 from n=5 has a 95% CI of approximately [ 0.63, 0.99 ] under Fisher's z, so it is not as precise as it appears. More importantly, the relationship is tautological at its core: benchmarks with more variable item difficulties (bimodal = some very easy, some very hard) will necessarily produce more item-level variance. This is a mathematical near-identity, not an empirical finding. Verdict:  The correlation is real but trivially expected from the definition of item variance. Not a meaningful contribution. 2. Positioning Against Related Work 2a. Critique of Mesting (2026) and Brittlebench (2026) The critique is  partially fair but overstated . The paper claims (lines 43-50) that \\\"every prior study that reports a single variance decomposition without resampling stability analysis has, in effect, presented one draw from a high-variance distribution as a finding.\\\" This is true in principle but uncharitable. Mesting's study uses a large item set and reports REML standard errors (which capture estimation uncertainty within a fixed design). Brittlebench uses a different framework entirely (not G-theory). The paper implies these studies are fundamentally flawed rather than acknowledging that they answer different questions with different assumptions. The claim that \\\"if Mesting had used different items, her 43.8% judge-dominance estimate might have been 30% or 55%\\\" (line 245) is speculative. Mesting's study uses different benchmarks with different item pool sizes; the CV from MMLU does not transfer directly. 2b. Missing related work Several important references are absent: -  Cardinet, Johnson, & Pini (2010) : \\\"Applying Generalizability Theory using EduG\\\" — directly addresses variance component stability and CIs in G-theory -  Webb, Shavelson, & Haertel (2006) : Reliability coefficients and G-theory, including sampling variability of components -  Marcoulides (1999) : On the sampling variability of G-theory estimates -  Multiverse analysis literature  (Steegen et al., 2016): The \\\"analyst degrees of freedom\\\" argument has been made more rigorously in the multiverse framework -  Differential item functioning (DIF) literature : The model×item interaction is essentially DIF — items that function differently across subpopulations (here, models). This connection to the psychometric DIF literature is completely unmade. -  Bell (2010)  and other G-theory sampling papers in educational measurement The paper cites Brennan and Shavelson/Webb as canonical references but does not engage with the substantial G-theory literature on exactly the problem it claims to discover (component sampling variability). 2c. Distinction from Bouthillier et al. (2021) Adequately distinguished. The paper correctly notes that Bouthillier uses ANOVA without D-study projections. The distinction is clear. 3. Significance and Impact 3a. Would these findings change evaluation practice? Partially.  The resampling instability finding (Claim 1) should prompt researchers to report bootstrap CIs on variance components — this is a useful methodological recommendation. The model-as-facet finding (Claim 2) is relevant but its practical implication is unclear: most evaluation studies compare specific models, making model-as-fixed appropriate by design. The D-study CI finding (Claim 3) is a legitimate concern but the practical response (\\\"report uncertainty on budgets\\\") is straightforward. 3b. Is \\\"budgets need error bars\\\" actionable? Yes, but it is a modest recommendation.  The paper essentially says: report confidence intervals on your variance component estimates and D-study projections. This is standard statistical practice that has been advocated in psychometrics for decades. The novelty is in showing that the ML community has not been doing it, which is valuable but incremental. 3c. Solutions vs. diagnosis The paper is almost entirely diagnostic.  It identifies problems (instability, model specification sensitivity, CI width) but provides no solutions. It does not propose better estimation methods, more stable designs, or alternative frameworks. The three recommendations in the conclusion (report CIs, use model-as-facet, report uncertainty on budgets) are methodological hygiene points, not solutions to the underlying instability. 4. Writing Quality 4a. Narrative pivot The pivot from \\\"we set out to build budgets\\\" to \\\"the budget itself is unreliable\\\" is  well-executed rhetorically  but raises credibility concerns. Was this genuinely a surprise discovery, or was the \\\"failed hypothesis\\\" narrative constructed post-hoc to make negative results publishable? The paper framing document reveals this was indeed a pivot after the cross-benchmark gradient hypothesis failed. The pivot is honest, but the resulting narrative feels contrived — the paper is essentially a collection of negative/null results (no gradient, unstable components, wide CIs) reframed as meta-methodological insights. 4b. Paper length and bloat The paper is too long for its content density.  8 experiments across what would be 13+ pages is excessive. Specific concerns: -  Experiment 5 (14B extension) : Adds very little. With n=2 models and scale/architecture confounded, the finding that item dominance is \\\"lower for 14B\\\" is uninterpretable. This should be cut or relegated to a 2-line appendix mention. -  Experiment 7 (LayerCast) : Confirms precision is not a first-order concern — a finding already established in Experiment 1 after confound correction. Adds  <2% variance. Should be cut. -  Experiment 6 (fine-tuning) : Uses RoBERTa-large, a fundamentally different setting from LLM inference evaluation. The finding that learning rate dominates (instead of item) in fine-tuning is unsurprising and disconnected from the main narrative. The low correlation between inference and fine-tuning variance structures (r=0.18) is the only noteworthy point, and it could be a 3-sentence appendix finding. The paper would be stronger at 8-9 pages with Experiments 1, 1b, 2, 3, and 4 only. 4c. Table density 18 tables with no figures  is a severe presentation problem. The paper violates its own field's conventions (distilled writing patterns call for stacked-bar decomposition figures as the \\\"signature visual\\\"). The absence of any figure makes the paper visually impenetrable and prevents readers from grasping patterns at a glance. At minimum, the paper needs: (1) a stacked-bar variance decomposition across benchmarks, (2) a D-study projection curve, and (3) a resampling stability visualization. 5. Framing Concerns 5a. Is \\\"measurement error exists in variance decomposition\\\" surprising enough? No, not for a top venue.  This is a well-known concern in psychometrics. The contribution is showing its magnitude in LLM evaluation, which is useful but incremental. The paper would need to either (a) show that the instability is catastrophically worse than expected from theory, or (b) propose a solution that substantially improves practice. It does neither. 5b. Does the paper overclaim? Yes, in several places: -  \\\"Every prior study that reports a single variance decomposition...has presented one draw from a high-variance distribution as a finding\\\" — this over-generalizes from MMLU to all measurement settings -  \\\"Model×item interaction (33%) is the single largest overlooked component\\\" — whether it is \\\"overlooked\\\" depends on the research question; treating model as fixed is a legitimate design choice when comparing specific models -  \\\"Rendering benchmark-specific budget recommendations statistically meaningless\\\" — the CIs are wide but the point estimates are still informative; \\\"meaningless\\\" is too strong -  The title \\\"Variance Decomposition Is a Measurement, Not a Fact\\\" implies prior work treated decompositions as facts — most measurement researchers know they are estimates 6. Strengths and Weaknesses Strengths -  S1.  The resampling instability analysis (Exp 1b) is a genuinely novel contribution to ML evaluation methodology, even if the concept is known in psychometrics -  S2.  Large scale: 4 models, 5 benchmarks, multiple facets crossed — the most comprehensive G-theory study of LLM evaluation to date -  S3.  The engine confound discovery and correction (V0 enforce_ eager) is a valuable methodological contribution that benefits the community -  S4.  The model-as-facet reanalysis, while methodologically standard, provides useful quantification of model×item interaction magnitude in LLM evaluation -  S5.  The bimodality mechanism linking difficulty distribution shape to item dominance is intuitive and potentially useful for benchmark designers -  S6.  The REML vs. Henderson comparison adds a useful sensitivity dimension -  S7.  The pivot narrative is intellectually honest — admitting the gradient hypothesis failed Weaknesses -  W1.  The central framing claim (\\\"variance decomposition is a measurement, not a fact\\\") is well-established in psychometrics; presenting it as a discovery undermines credibility with measurement-literate reviewers -  W2.  Only 3 item resamples to estimate CV — the CV=33% figure is itself highly uncertain; need 10+ resamples for credible estimation -  W3.  No figures at all — 18 tables with zero visualizations makes the paper nearly unreadable -  W4.  Experiments 5, 6, and 7 contribute little and bloat the paper; the fine-tuning study (RoBERTa) is too far from the LLM inference setting -  W5.  The paper is purely diagnostic — no solutions, no improved methods, no practical tools beyond \\\"report CIs\\\" (standard advice) -  W6.  The critique of prior work is uncharitable: treating model as fixed is a design choice, not an error; Mesting reports REML SEs -  W7.  The non-gradient result (Exp 2, 8) is presented as meaningful, but 9pp spread across 5 benchmarks under model-as-fixed is expected given resampling instability — this is a null result, not a finding -  W8.  The bimodality correlation (r=0.95 from n=5) is both statistically underpowered and mechanistically tautological -  W9.  Missing engagement with the substantial psychometric literature on variance component sampling variability (Cardinet et al., Marcoulides, Webb et al.) -  W10.  The paper's three claims are essentially three ways of saying \\\"variance estimates are uncertain\\\" — this is one finding, not three 7. Questions for Authors 1.  On resampling stability : With only 3 item resamples, your CV=33% estimate has enormous uncertainty. What is the bootstrap standard error of the CV itself? Have you considered running 30+ resamples to produce a credible estimate? Would the CV decrease with larger item samples (e.g., 500 items from the 14,000-item MMLU pool)? 2.  On model-as-facet : You argue that treating model as fixed \\\"inflates\\\" item variance. But if a practitioner wants to evaluate a specific model (the common use case), treating model as fixed is correct by design — the goal is not to generalize to unseen models. Under what practical scenario is model-as-random the appropriate specification? How do you respond to the argument that model×item interaction is simply model-specific item difficulty, which is exactly what practitioners care about? 3.  On the non-gradient : Your original hypothesis was a cross-benchmark gradient from knowledge to reasoning. This failed (spread=9pp, non-monotonic). You then pivoted to \\\"the budget itself is unreliable.\\\" If the gradient had been confirmed, would you still have discovered the instability? Does the pivot undermine the claim that instability is the \\\"centerpiece\\\" finding, or was it only noticed because the primary hypothesis failed? 4.  On separability : You report that separability fails on GSM8K (4.5% infra×method) and with hardware (5.5%). But 4-5% is arguably still small in absolute terms. What threshold makes separability \\\"fail\\\"? Is there a principled way to set this threshold, or is the \\\"failure\\\" framing a judgment call? 5.  On engagement with psychometrics : Your central claim — that variance components are estimates with sampling distributions — is standard in the G-theory literature (Brennan 2001 Ch.8, Cardinet et al. 2010). Why does the paper not engage with this prior work? How does the observed CV=33% compare to typical component instability in educational measurement applications of G-theory? 8. Score Score: 3 (Weak Reject) Justification:  The paper addresses a relevant question (stability of variance decomposition in LLM evaluation) and provides useful empirical data at scale. However, the central conceptual contribution — that variance components are estimates with error — is well-established in psychometrics and cannot be claimed as novel. The paper is purely diagnostic with no solutions beyond standard statistical hygiene recommendations. The resampling analysis (the strongest contribution) is underpowered at n=3 samples. The presentation is severely hampered by 18 tables and zero figures. Experiments 5-7 add bulk without proportional insight. The framing overreaches: treating model-as-fixed as an \\\"error\\\" rather than a design choice, claiming prior work treats decompositions as \\\"facts,\\\" and declaring benchmark-specific budgets \\\"meaningless.\\\" For a top venue with ~ 25% acceptance, the paper needs either a substantially novel conceptual contribution or a practical solution, and it provides neither. The empirical findings (resampling CV, model×item magnitude) are useful contributions that would strengthen a paper with a more modest framing, but the current framing invites expert pushback. 9. Confidence Confidence: 4/5 I have substantial familiarity with both G-theory (through educational measurement applications) and LLM evaluation methodology. I have read the primary references (Brennan 2001, Shavelson & Webb 1991, Bouthillier et al. 2021) and am familiar with the variance component sampling variability literature. I am less certain about the specific numerical claims (I cannot verify the 4M observations or the exact variance decomposition numbers), but the methodological assessment is on firm ground.\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd033ed00b0b4a492ca166686c\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779320786148\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — median | dream_20260520T222113]  · Overall: Weak Accept (4/6) Dream Review Report —  dream_20260520T222113  (median tier) Paper Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics Review Panel -  R1 : Methods & Experiments -  R2 : Novelty & Related Work 1. Independent Reviews R1: Methods & Experiments — Score 4/6 (Weak Accept), Confidence 4/5 Summary : The paper conducts a large-scale G-theory analysis crossing infrastructure with methodology facets across 5 benchmarks and 6 models (~ 3M+ observations). The experimental design is ambitious and the numerical results are internally consistent. However, several technical methodology issues undermine confidence. Strengths : 1.  Internal numerical consistency across all 15 tables is excellent — variance components sum correctly, cross-references between tables are coherent, and the model-as-facet correction systematically reduces item_ id by ~ 4pp across all benchmarks. 2.  The cross-benchmark gradient finding (item_ id: 48% MMLU → 28% MATH) is well-supported with bootstrap CIs showing non-overlapping intervals at endpoints (permutation p=0.003). 3.  The engine confound correction (V0 enforce_ eager eliminating the 0.22pp BF16 eager artifact) is a genuine standalone contribution that prevents other researchers from attributing engine-routing variance to precision effects. 4.  Experimental scale is impressive: 9 experiments, 5 benchmarks, 6 models, 2 GPU architectures, 3 scoring metrics. 5.  Item resampling stability analysis (Table 3) honestly quantifies the sampling uncertainty in item_ id estimates (CV=0.19) and correctly reports ranges rather than point estimates. Weaknesses : 1.  D-study optimization procedure is undocumented : Table 9 reports joint-optimal facet allocations (e.g., MMLU: 420 items, 3 prompts, 4 seeds for G≥0.90) but the paper does not describe how joint optimization across multiple facets was performed. Standard D-study sweeps one facet at a time while holding others fixed. If grid search was used, the search space and stopping criteria should be stated. This is critical because practitioners will use these numbers directly. 2.  G coefficient interpretation conflates with overall reliability : The paper presents G=0.37 (binary) as indicating \\\"substantial unreliability\\\" of MMLU. But G-theory's G coefficient measures generalizability over the  facets included in the design , not overall measurement quality. Since the universe of generalization includes only the specific facets crossed, the low G primarily reflects high item-sampling error, not that MMLU is unreliable in practice (where items are fixed). The paper should distinguish G as a design property from reliability as a benchmark property. 3.  Observation count claim : The abstract says \\\"over 3 million\\\" observations. Summing across experiments: MMLU ~ 1.04M + multi-benchmark ~ 1.15M (3×384K) + hardware ~ 1.15M + 14B unclear + fine-tuning ~ 1,728 runs (not observations) + MATH + LayerCast. The total depends on overlap assumptions (exp-004 reanalyzes existing data). The claim should be precisely itemized. 4.  MATH variance decomposition : Table 6 shows item_ id=28% for MATH (model-as-facet), but temp:item (14%) + seed:item (11%) = 25%, nearly matching item_ id. The paper does not adequately discuss that for MATH, item dominance is barely maintained — on a per-model basis, temperature×item may exceed item_ id for some models, weakening the \\\"item_ id always ranks #1\\\" claim. 5.  Missing details for replication : (a) Which 6 prompt templates were used? (b) What stratification procedure for 200 items across 57 MMLU subjects? (c) How were \\\"200 MATH items\\\" selected given MATH's difficulty distribution? (d) What temperature values (three temperatures stated but values not given)? These omissions make exact replication impossible. Questions for Authors : 1.  For the D-study projections, was the optimization over (items, prompts, seeds) done via exhaustive grid search or analytical formula? What were the grid bounds? 2.  Table 6 shows MATH prec:item and precision main as \\\"—\\\" (missing). Is this because the MATH experiment used only BF16/FP16 with insufficient precision levels for stable estimation? 3.  The bootstrap procedure resamples items × conditions. Are conditions resampled with replacement within the factorial structure, or is the bootstrap at the cell level? 4.  How does the G coefficient change if you remove the 3-way and higher interaction terms from the error variance? The 9% \\\"other 2-way/3-way\\\" in Table 1 is non-trivial. R2: Novelty & Related Work — Score 4/6 (Weak Accept), Confidence 4/5 Summary : The paper applies G-theory to multi-benchmark LLM evaluation, discovering a benchmark-conditional variance gradient and producing D-study reproducibility budgets. The cross-benchmark gradient is the genuine novel contribution; the infrastructure×methodology crossing — framed as the key methodological advance — yields near-null results. Strengths : 1.  The cross-benchmark variance gradient (item_ id: 48% → 28% from knowledge to proof reasoning) is genuinely novel. No prior work has positioned multiple benchmarks along a reasoning-intensity continuum and demonstrated a monotonic shift in variance structure. The unifying explanation — that prior single-benchmark studies reached contradictory conclusions because they studied benchmarks at different gradient positions — is insightful. 2.  The D-study budget differentiation is non-obvious and actionable: MMLU is item-limited while GSM8K is seed-limited, directly challenging the assumption that evaluation protocols can be standardized. 3.  Honest positioning of contributions. The paper correctly frames separability as confirmatory, acknowledges that item dominance is psychometrically expected, and scopes infrastructure to numerical precision. This intellectual honesty is appreciated. 4.  The G  < 0.37 finding for standard MMLU evaluation practice is an important indictment of current evaluation norms, framed in measurement-theory language that connects NLP to established psychometric standards. 5.  The experimental scale (3M+ records, 9 experiments) substantially exceeds both Mesting (2026, single benchmark) and all prior isolated-factor studies. Weaknesses : 1.  Infrastructure crossing yields near-null results, hollowing the novelty narrative : The introduction frames \\\"crossing infrastructure with methodology in a unified G-theory framework\\\" as a key gap filled. But infra×method < 0.5% on knowledge benchmarks means this crossing contributes essentially nothing to understanding. The three genuine findings (gradient, D-study reversal, G  < 0.37 indictment) would all emerge from a methodology-only design replicated across 5 benchmarks. The GSM8K exception (3%) partially rescues this, but the paper oversells the infrastructure crossing relative to its contribution. 2.  Missing critical related work :   -  No comparison with IRT-based item selection (tinyBenchmarks recommends ~ 100 items for MMLU vs. this paper's 420 for G≥0.90 — the 4× discrepancy is never discussed)   -  ThinkingMachines (2025) on batch-invariance failure in GEMM/attention kernels is directly relevant to the seed×item interaction mechanism   -  No engagement with Kunievsky & Evans (2025) alternative variance decomposition framework   -  15 references is thin for a venue submission of this scope 3.  \\\"First multi-benchmark G-theory analysis\\\" claim is narrow : Bouthillier et al. (2021) performed ANOVA-based variance decomposition across multiple ML benchmarks. The difference is \\\"G-theory (not ANOVA) applied to LLM evaluation (not ML generally) across multiple benchmarks.\\\" This is a narrow novelty window. 4.  Three-tier benchmark clustering is post-hoc : The ordering (knowledge > commonsense > reasoning) was presumably determined after observing results. An independent measure of \\\"reasoning intensity\\\" (e.g., average CoT length, multi-step count) would make the continuum principled rather than constructed. A 6th benchmark might not fall on the line. 5.  Zero figures is a critical presentation failure : 15 tables and no figures in a variance decomposition paper. Stacked-bar decomposition charts are the expected field idiom. The cross-benchmark gradient demands visualization. D-study projection curves would communicate the budget reversal far more effectively than tables. At a top venue, this is a significant competitive disadvantage. 6.  Fine-tuning G-study (Section 4.10) is architecturally disjoint : RoBERTa-large encoder fine-tuning uses different facets (LR, data shuffle) from the decoder inference study (prompt, temperature). The finding that \\\"infrastructure is negligible in fine-tuning too\\\" is unsurprising. The cross-paradigm generalization claimed is weak. 7.  IRT comparison is a missed opportunity : D-study budgets claim to be \\\"an alternative to IRT subsampling\\\" but never compare against actual IRT recommendations. If tinyBenchmarks and D-study agree, G-theory is confirmatory; if they disagree, the paper must explain why. Questions for Authors : 1.  If you added GPQA or HumanEval as a 6th benchmark, would it fall on the gradient? What would it mean for the claim if it did not? 2.  What mechanism drives the gradient for HellaSwag specifically? It does not involve explicit chain-of-thought. 3.  For MMLU, Polo et al. recommend ~ 100 items via IRT. Your D-study recommends 420. Can you explain the 4× discrepancy? 4.  If a practitioner uses LLM-as-judge evaluation, do D-study budgets still apply, or are they overwhelmed by judge variance (Mesting found judge identity at 43.8%)? 5.  What does the infrastructure crossing add beyond a confirmatory null, given that the three main findings would emerge from methodology-only replication? 2. Roundtable Cross-Sharing Areas of Agreement -  Score : Both reviewers converge on 4/6 (Weak Accept) — paper is at the acceptance threshold -  Core contribution : Both agree the cross-benchmark variance gradient is the paper's genuine and most important novel finding -  Experimental scale : Both praise the comprehensiveness (3M+ obs, 9 experiments, 5 benchmarks) -  Internal consistency : Both note that numerical results are coherent across tables -  Practical value : Both appreciate the D-study budgets as actionable for practitioners -  Item resampling : Both view the CV=0.19 finding as an honest and valuable contribution Areas of Complementary Concern -  R1 technical, R2 positioning : R1 identifies specific methodological gaps (D-study optimization procedure, G interpretation, missing experimental details), while R2 identifies framing gaps (infrastructure crossing as hollow, missing related work, post-hoc clustering) -  Both flag : Insufficient detail for replication (R1: prompts, temperatures, stratification; R2: comparison with IRT baselines) Disagreement Resolved -  R1 and R2 initially emphasized different aspects but neither raised objections to the other's concerns during sharing. R2's concern about \\\"infrastructure crossing as expensive null\\\" and R1's concern about \\\"D-study optimization undocumented\\\" are complementary weaknesses that jointly characterize the paper's limitations. 3. Consolidated Assessment Overall Score: 4/6 (Weak Accept) Confidence: 4/5 Decision Rationale The paper makes a genuine empirical contribution: the cross-benchmark variance gradient showing that item dominance shifts from 48% (knowledge) to 28% (proof reasoning) is novel, well-supported by bootstrap CIs, and provides a unifying explanation for seemingly contradictory findings in prior single-benchmark studies. The D-study reproducibility budgets are practically useful and the benchmark-specific budget differentiation (MMLU item-limited vs. GSM8K seed-limited) is non-obvious. The experimental scale is impressive. However, several issues keep the paper at the acceptance threshold rather than above it: 1.  Novelty concentration : The infrastructure×methodology crossing — framed as the key methodological advance over Mesting (2026) — yields  <0.5% on knowledge benchmarks. The main findings would emerge from methodology-only multi-benchmark replication. The GSM8K 3% exception partially rescues this but is insufficient to carry the infrastructure framing as a primary contribution. 2.  Presentation : Zero figures in a 15-table variance decomposition paper is a critical gap. The gradient and D-study curves practically demand visualization. 3.  Technical documentation gaps : D-study joint-optimization procedure undocumented, experimental details (prompt templates, temperature values, stratification) insufficient for replication, and the observation count claim needs precise itemization. 4.  Positioning gaps : Missing comparison with IRT-based recommendations (tinyBenchmarks 100 items vs. D-study 420 items), thin bibliography (15 refs), post-hoc gradient ordering without external validation. 5.  G coefficient interpretation : The paper somewhat conflates measurement generalizability (a design property) with benchmark reliability (a practical property), risking misinterpretation by practitioners. Actionable Revision Priorities (Ranked) 1.  Add 3-4 figures : (a) Stacked-bar variance decomposition across 5 benchmarks — the signature figure; (b) D-study projection curves (G vs. item count) with CI bands; (c) Forest plot of bootstrap CIs on item_ id across benchmarks; (d) Model-as-facet comparison (before/after stacked bars for MMLU) 2.  Document D-study optimization : State the joint-optimization procedure (grid search vs. analytical), the search bounds, and validate that recommendations are internally consistent 3.  Add IRT comparison : Compare D-study budgets with tinyBenchmarks recommendations and explain discrepancies — this strengthens the contribution 4.  Expand bibliography : Add ThinkingMachines (2025), Kunievsky & Evans (2025), and 3-5 additional relevant references to reach 20+ 5.  Provide experimental details : List all 6 prompt templates, the 3 temperature values, the item stratification procedure, and a precise observation count breakdown 6.  Reframe infrastructure crossing : Position as confirmatory evidence for separability rather than as a primary methodological contribution. Emphasize the GSM8K exception as the genuine finding from infrastructure crossing. 7.  Validate gradient externally : Add an independent measure of reasoning intensity for each benchmark (CoT length, multi-step count) to make the three-tier clustering principled rather than post-hoc 8.  Clarify G interpretation : Distinguish G as a generalizability coefficient over included facets from overall benchmark reliability, noting that practitioners using fixed items face different reliability profiles Experiment Coverage Assessment The paper covers all 9 planned experiments (exp-001 through exp-008 plus exp-001b). Coverage is breadth-oriented: 15 tables in 10 pages means each experiment gets 1-2 paragraphs. The fine-tuning study (exp-006) and LayerCast (exp-007) feel rushed — each could be appendix material to free space for figures and deeper analysis of the core experiments (exp-001, 002, 004). The MATH extension (exp-008) is well-integrated into the cross-benchmark narrative. Strengths Summary -  Cross-benchmark variance gradient: novel, statistically rigorous, explanatory -  D-study budget differentiation: practically actionable, non-obvious -  Experimental scale: ~ 3M observations, 9 experiments, 5 benchmarks, 6 models -  Item resampling stability: honest quantification of estimation uncertainty -  Engine confound correction: standalone methodological contribution -  Internal numerical consistency across all tables Weaknesses Summary -  Infrastructure crossing yields near-null, hollowing the claimed methodological advance -  Zero figures in a heavily quantitative variance decomposition paper -  D-study optimization procedure and experimental details undocumented -  Post-hoc gradient clustering without external validation -  Missing IRT comparison and thin bibliography -  G coefficient interpretation risks practitioner misunderstanding -  Fine-tuning and LayerCast sections are disjoint/rushed\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd03a4578a4b21bbad48007cd6\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779320648684\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — best | dream_20260520T222113]  · Overall: weak accept R1 Review: Methods & Experiments Summary This paper applies Generalizability Theory to LLM evaluation across five benchmarks, six models, and 4M+ records, crossing infrastructure (precision, hardware) with methodology (prompt, seed, temperature, ordering) and measurement (item) facets. The revised version addresses most structural issues from Dream #1: model is now treated as a crossed facet, bootstrap CIs are provided, the bibliography is expanded to 22 references, and the cross-benchmark variance gradient is correctly positioned as the primary contribution. The experimental design is ambitious and largely sound, with internal numerical consistency verified across tables. The paper demonstrates that variance structure shifts systematically from item-dominated (MMLU 56%) to interaction-dominated (MATH 21%), and that D-study optimal allocations reverse across task types. Strengths 1.  Internal numerical consistency is excellent.  Variance components in Table 1 sum to 100.0%. Model-as-facet Table 6 rows all sum to 100.0% (e.g., MMLU: 49.2+10.2+5.9+3.0+6.2+2.8+12.0+10.7=100.0). The interaction gradient in Table 5 is arithmetically consistent with Table 4 (e.g., MMLU sum(int item)=18.4 matches t i+s i+p i+prec i+ord i = 5.9+3.0+6.2+1.8+1.5=18.4). D-study projections in Tables 9-10 are internally consistent with the G_ full and G_ cur values in Table 7. 2.  The engine confound discovery and correction is a genuine methodological contribution.  Identifying that vLLM routes FP32 through V1 CUDA graph vs V0 eager for BF16/FP16, inflating precision* item from 1.8% to 7.2% and creating an 8.5pp accuracy gap, is valuable to any researcher using vLLM. The correction (standardizing all precisions to V0 enforce_ eager) is principled, and the before/after comparison (Table 1 MVP column) is convincing. The freed ~ 5.4% variance redistributing into residual is consistent with confound removal. 3.  Model-as-facet reanalysis (Table 6) addresses the most critical methodological gap from Dream #1.  Item_ id drops by ~ 6-7pp across all benchmarks (MMLU: 56.0->49.2, GSM8K: 25.0->22.6), with model* item absorbing ~ 10% on MMLU. Critically, item_ id remains rank-1 on all benchmarks and the gradient is preserved (49.2->38.4->30.8->22.6). This properly attributes model heterogeneity rather than inflating item estimates. 4.  Item resampling stability (Table 3) is a well-designed robustness check.  Three independent stratified 200-item MMLU samples with CV=4.1% on item_ id and consistent rank ordering across samples. The 30pp margin between item_ id (lowest sample: 52.8%) and the second-largest component eliminates single-sample artifact concerns. 5.  The factorial design for MMLU (exp-001) is densely crossed and large-scale.  4 models x 3 precisions x 6 prompts x 6 seeds x 3 temperatures x 4 orderings x 200 items = 1,036,800 records. This is among the largest factorial designs in the LLM evaluation variance literature. The per-model consistency (Table 2: item_ id 51.6-60.2% across four models) rules out single-model artifacts. 6.  The D-study facet effectiveness inversion (Table 11) is the paper's most practically useful finding.  The items:seeds effectiveness ratio shifting from 14.2:1 (MMLU) to 0.8:1 (GSM8K) has direct implications for evaluation protocol design and explains why prior studies on different benchmarks reached contradictory conclusions. 7.  Bootstrap CIs on item_id (Table 8) with non-overlapping intervals across adjacent benchmarks provide statistical support for the gradient.  The MMLU-ARC gap (CI upper 52.3 vs CI lower 35.6) and ARC-HellaSwag gap (CI upper 41.2 vs CI lower 28.2) show the gradient is not an artifact of sampling variability. Weaknesses Major 1.  Henderson Method I vs Method III discrepancy in the text.  The code ( variance_decomposition.py ) implements Henderson Method I (Type-I SS for balanced designs, solving EMS equations), but Section 3.1 (line 118) claims \\\"Henderson's Method III (expected mean squares)\\\" is used. Henderson's Method I and Method III are distinct estimation procedures -- Method I uses fitting-constants for balanced designs while Method III uses Searle's approach for unbalanced designs. For the balanced crossed design here, Method I is appropriate and the code is correct, but the paper misnames it. Table 1 caption says \\\"SE and 95% CI from Henderson's Method III\\\" -- this is incorrect given the code. Additionally, the paper later references \\\"REML vs Henderson\\\" sensitivity (Section 7.3, line 533) with  <=1.4pp differences and calls this \\\"Henderson Method I\\\" -- contradicting the earlier \\\"Method III\\\" claim. This inconsistency should be resolved. 2.  The D-study projection for GSM8K contains an arithmetically suspicious result.  In Table 10 (D-study GSM8K), the row \\\"150 items, 3 prompts, 10 seeds\\\" achieves G=0.90, while \\\"200 items, 3 prompts, 10 seeds\\\" achieves G=0.93. Yet in Table 7, the \\\"optimal\\\" allocation for GSM8K is listed as 150 items with 10 seeds. The issue: reducing items from 200 to 150 while achieving higher G only makes sense if item_ id variance is already small enough that removing 50 items has negligible impact on item-related error. But the G formula divides item-related variance components by n_ items -- so  fewer  items should yield  lower  G, not the same or higher. This suggests the \\\"150 items\\\" recommendation in Tables 7 and 9 may be from a different optimization (e.g., multi-facet joint optimization with different prompt/seed allocations) rather than a simple projection, but the paper does not explain the optimization procedure. The D-study code ( d_study.py ) sweeps one facet at a time while holding others fixed, which cannot produce the joint-optimization results in Table 9. Either the optimization procedure is undocumented, or the 150-item figure is derived from a different analysis than what the code implements. 3.  The \\\"counter-intuitive G pattern\\\" explanation (Section 5.1, line 283-284) has a logical gap.  The paper claims MMLU has lower G (0.36) than GSM8K (0.55) because \\\"high item_ id means item sampling is the measurement reliability bottleneck.\\\" But G is defined as sigma_ tau / (sigma_ tau + sigma_ delta), where sigma_ tau is universe-score variance (fixed-facet components only: precision, temperature, and their interaction). Looking at the code, sigma_ tau for MMLU would be dominated by precision (0.3%) and temperature (1.4%) main effects -- tiny values. For GSM8K, these would also be small. The G coefficient as implemented measures the ratio of fixed-facet variance to total variance -- so higher G for GSM8K means fixed facets explain proportionally more of the reduced-error variance on GSM8K. This is not the same as \\\"item sampling being the bottleneck.\\\" The paper's narrative explanation conflates the G coefficient with measurement reliability in a way that obscures what G actually measures in this design. Specifically: in a design where the object of measurement is benchmark accuracy and the facets are prompt/seed/ordering/item, the \\\"universe score\\\" is determined by which facets are treated as fixed vs random. The paper's partition (precision and temperature as fixed) means G measures how stable results are across prompt/seed/ordering/item variations  given  a fixed precision and temperature -- not overall measurement reliability. 4.  The paper claims \\\"4 million evaluation records\\\" (abstract, line 32) but the itemized totals fall short.  MMLU: 1,036,800. ARC+HellaSwag+GSM8K: 3 x 460,800 = 1,382,400. MATH: 460,800. Hardware: 691,200. 14B: 345,600. Fine-tuning: 1,728 runs (but unclear record count per run). Item resampling: 32,400. Even summing all inference experiments without double-counting (since hardware/14B experiments likely overlap with MMLU data), the total is closer to ~ 3.9M if MATH and hardware are fully independent, or ~ 3M if there is overlap. The \\\"over 4 million\\\" claim needs verification that these are truly independent records, not overlapping subsets counted multiple times. Moderate 5.  Reduced designs for non-MMLU benchmarks are insufficiently justified.  ARC/HellaSwag/GSM8K/MATH use 2 precisions x 2 temperatures (vs 3x3 for MMLU), but the paper does not explain why. If the reduction is due to GPU budget constraints, this should be stated explicitly. More importantly, the cross-benchmark gradient (Table 4) compares variance percentages from designs with different factorial structure (MMLU: 3 precisions, 3 temperatures vs others: 2 precisions, 2 temperatures). Variance percentages are relative to total variance, which changes with the design. Removing a precision level and a temperature level changes the total variance denominator and redistributes percentage shares. The paper should discuss whether the gradient would hold if all benchmarks used the identical design. 6.  Bootstrap resampling items with replacement while preserving balanced design (bootstrap_ci.py, lines 117-120) creates artificial correlation.  When a bootstrap sample draws the same item twice, the code assigns unique IDs (\\\"boot_ 0\\\", \\\"boot_ 1\\\") and treats them as independent items. But these duplicate items have identical responses across all conditions, violating the independence assumption underlying the ANOVA decomposition. This inflates the stability of item_ id estimates. A cluster bootstrap (resampling items and their complete observation vectors without re-indexing) would be more appropriate, though it would produce an unbalanced design requiring REML rather than Henderson Method I. 7.  The fine-tuning G-study (Section 8.2) uses a qualitatively different experimental paradigm.  RoBERTa-large is an encoder-only model fine-tuned on classification tasks; the inference experiments use decoder-only autoregressive models on generation/MC tasks. The variance hierarchy comparison (Table 13) across paradigms is informative but the claim that \\\"item dominance generalizes beyond inference to training\\\" overstates what this comparison can support. The facets themselves are different (learning rate and data shuffle replace prompt template and temperature), making direct comparison of variance percentages across paradigms questionable. 8.  The paper reports G_cur (current practice) in Table 7 but the definition of \\\"current practice\\\" is not consistent.  Table 7 defines G_ cur values (MMLU 0.22, GSM8K 0.14), and Table 9 shows MMLU with \\\"200 items, 1 prompt, 1 seed\\\" = G=0.22. But \\\"current practice\\\" typically includes a fixed temperature (usually 0) and a single precision -- if these are treated as fixed facets in the D-study, they should not contribute to error variance. The paper should clarify exactly what design parameters constitute \\\"current practice\\\" and whether the G_ cur values assume temperature=0 or marginalize over temperature levels. Questions for Authors 1.  Is the estimation method Henderson Method I (as implemented in the code) or Henderson Method III (as stated in the text)? If Method I, please correct the text. If Method III, please reconcile with the code. 2.  How is the joint D-study optimization (Table 9) computed? The provided D-study code sweeps one facet at a time. The joint recommendations (e.g., GSM8K: 150 items + 3 prompts + 10 seeds) appear to come from a different procedure. Please describe the optimization algorithm. 3.  For the counter-intuitive G pattern: what exactly is sigma_ tau in your D-study? If precision and temperature are treated as fixed, sigma_ tau is their variance plus their mutual interaction -- all tiny values. Doesn't this mean G is measuring something quite narrow (stability across precision/temperature choices) rather than overall measurement reliability? 4.  Can you provide the total observation count broken down by experiment, confirming non-overlap, to support the \\\"4 million\\\" claim? 5.  The abstract says \\\"item selection is the largest single variance source on all benchmarks\\\" with 56% to 21%. But on MATH (Appendix A), Llama-3.1-8B shows temperature item (21.8%) exceeding item_id (20.6%), and Mistral-7B shows temperature item (22.8%) exceeding item_ id (17.8%). How do you reconcile the \\\"all benchmarks\\\" claim when two of four models on MATH show item_ id is  not  the largest source? 6.  What is the effective sample size of the bootstrap after accounting for duplicate items? With 200 items and replacement sampling, each bootstrap draw will have ~ 127 unique items on average (by the birthday problem). Does this deflation affect CI coverage? Minor Issues 1.  The abstract states the item dominance gradient as \\\"56% on knowledge-retrieval tasks (MMLU) down to 21% on complex reasoning (MATH), a 35 percentage-point gradient.\\\" But Table 1 reports 56.0% for the pooled analysis, while Table 6 (model-as-facet, which is the more principled analysis) reports 49.2% for MMLU. The abstract should use the model-as-facet figures. 2.  Table 1 caption refers to \\\"SE\\\" but no standard error column is visible -- the columns are % Var, SE, CI Low, CI Up, MVP. Confirm that the SE column values are present and correctly computed. 3.  The paper uses \\\"infra x method\\\" as a single aggregate value (0.4% in Table 1) but does not list which specific interactions are included. From the 6-facet design (precision is the only infrastructure facet without hardware), the infrastructure x methodology interactions would be: precision x prompt, precision x seed, precision x temperature, precision x ordering. With hardware added (Table 6), this expands. Please enumerate. 4.  Line 118 says \\\"Henderson's Method III\\\" but line 533 says \\\"REML vs Henderson\\\" with no method number specified. Pick one consistent name. 5.  Table 12 (14B vs 8B) shows DeepSeek-R1-Distill-14B with temp item=8.8% and seed item=5.2%, both above the 8B range. The text attributes this to \\\"reasoning distillation introducing implicit chain-of-thought tendencies.\\\" This is speculative -- DeepSeek-R1-Distill-14B is architecturally different (distilled from a reasoning model), and the elevated interaction terms could also reflect the distillation training distribution rather than implicit CoT. The causal claim should be weakened. 6.  No figures. The cross-benchmark gradient and D-study projection curves would be substantially more impactful as visualizations than as tables. This is a presentation weakness, not a methodological one, but at a competitive venue it matters. 7.  The paper does not report effect sizes or practical significance thresholds beyond the 0.3% separability value. For which variance components is the estimate \\\"practically significant\\\"? A threshold framework (e.g., components >1% are \\\"practically relevant\\\") would aid interpretation. 8.  Reference [ 7 ] (Hua et al. 2025) is cited but never discussed in the Related Work section -- it appears only in the design decisions. Either discuss it or remove it. Score: 4/6 Confidence: 4/5\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd02c5700b0b2c790d8247e7bf\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779320361827\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — best | dream_20260520T222113]  · Overall: weak accept Dream Review Report — Consolidated Roundtable Paper:  Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics Dream ID:  20260520T222113\\n Review Mode:  Full (2 Reviewers, 4-Step Roundtable) Roundtable Process -  R1 focus:  Methodology, experimental design, statistical rigor -  R2 focus:  Novelty, related work positioning, significance/impact -  Step 1 (Independent):  Both reviewers scored  4/6 (Weak Accept) , high confidence. -  Steps 2–3 (Cross-sharing & Convergence):  See §7 below. -  Step 4 (Synthesis):  This report. 1. Paper Summary The paper applies Generalizability Theory (G-theory) to LLM evaluation in a multi-benchmark setting. Three facet classes are crossed: measurement (item_ id, 200 stratified-sampled items per benchmark), methodology (prompt template ×6, random seed ×6, temperature ×2–3, option ordering ×4), and infrastructure (numerical precision FP32/BF16/FP16/LayerCast, GPU hardware ×2). Six models (4×7–9B, 2×14B) are evaluated on five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), totaling 4M+ evaluation records. A fine-tuning G-study with RoBERTa-large on four NLU tasks adds cross-paradigm evidence. Three claims: 1.  Cross-benchmark variance gradient:  item_ id dominance is benchmark-conditional — 56% on MMLU down to 21% on MATH, a 35pp monotonic gradient. CoT stochasticity shifts variance into temp×item and seed×item on reasoning tasks. 2.  Confirmatory separability null:  direct infra×methodology interactions  <0.3% under binary scoring on knowledge benchmarks, validating isolated-factor studies at the aggregate level. Both factor types interact substantially with items. 3.  D-study protocol reversal:  optimal evaluation protocol reverses across task types — MMLU is item-limited (420 items for G≥0.90), GSM8K is seed-limited (10 seeds). Current practice G <0.25 everywhere. 2. Novelty Assessment (R2-led, R1-endorsed) Claim 1 (Cross-benchmark variance gradient):  Moderate-to-high novelty. The paper's strongest contribution. No prior work has demonstrated a systematic, monotonic shift in variance structure across multiple benchmarks positioned along a reasoning-intensity continuum. The 35pp gradient (MMLU→MATH) with the CoT stochasticity mechanism unifies apparently contradictory conclusions from prior single-benchmark studies (Sclar on prompt sensitivity, Pezeshkpour on ordering, Yuan on precision). The \\\"unifying explanation\\\" framing is well-executed. However, item_ id dominance per se is expected from measurement theory (Brennan 2001); the contribution is the quantification and the gradient, not the dominance finding itself. Claim 2 (Confirmatory separability):  Low novelty, moderate utility. A confirmatory null. The infrastructure crossing — the paper's methodological advance over Mesting (2026) — yields near-nothing ( <0.3% direct interactions). The nuanced decomposition into direct vs. item-conditional interactions (aggregate separability + item-level coupling) adds value but is not a primary novelty claim. R1 further notes that the separability claim is benchmark-conditional: GSM8K and MATH show 2.5–3.0% infra×method, weakening the generality. Claim 3 (D-study protocol reversal):  Moderate novelty, high practical value. The facet effectiveness ratio inversion (MMLU items:seeds = 14.2:1, GSM8K = 0.8:1) is non-obvious and actionable. The D-study projection grids are the most practically useful output. The G <0.25 finding is an important indictment of current practice. Collective Assessment The three claims are stronger together than individually. The gradient explains the protocol reversal; the separability null validates independent factor study. The paper is best understood as a large-scale empirical study applying a well-established framework (G-theory) to a new domain (multi-benchmark LLM evaluation) and discovering a systematic empirical regularity (the gradient). This is a meaningful contribution, not a methodological breakthrough. Incrementality over Mesting (2026) Clear advance in three dimensions: (a) five benchmarks vs. one, (b) infrastructure crossing, (c) model as crossed facet. The infrastructure crossing yields near-null results, so (b) is confirmatory. The multi-benchmark gradient and model-as-facet analysis are genuine advances. R2 notes that the complementarity with Mesting (who found judge identity dominant at 43.8%) should be discussed more explicitly — this paper fixes the judge and reveals the structure underneath. 3. Methodology Assessment (R1-led, R2-endorsed) 3.1 G-Theory Application Largely correct.  Model-as-facet (Section 7) properly separates model×item interaction (~ 10%) from item variance, addressing a key prior concern. Henderson Method III with REML sensitivity check is appropriate for the nearly-balanced crossed designs. Max divergence of ~ 1.4pp with preserved rankings is reassuring. 3.2 Critical Methodological Concerns (a) Binary data in G-theory (R1, Major).  Standard Henderson III / REML assume continuous, approximately normal responses. Binary 0/1 data violates this. Item variance is mechanically linked to item difficulty via the Bernoulli variance function p(1-p), partially inflating item_ id dominance. The logprob analysis (Appendix B, item_ id = 42.8%) on continuous data is methodologically cleaner and partially mitigates this, but the primary analysis is on binary data. The paper must discuss this limitation. A generalized G-theory approach (Brennan 2001, Ch. 12) or link-function-based decomposition would be more appropriate. (b) Temperature and ordering as random facets (R1, Major).  With 2–3 temperature levels (specific design points, not random draws) and 4 systematic orderings (cyclic rotations of 24 possible permutations), the exchangeability assumption required for random effects is questionable. Misspecification inflates variance estimates for these facets and their interactions. The paper should either justify the random-effects assumption, treat these as fixed, or present both as sensitivity analysis. (c) Asymmetric designs across benchmarks (R1, Moderate).  MMLU uses 3 precisions × 3 temperatures; other benchmarks use 2×2. FP32 is absent from non-MMLU experiments. The cross-benchmark precision gradient (MMLU 3.0% → MATH 0.5%) is confounded with different precision levels tested. A BF16/FP16-only MMLU reanalysis for cross-benchmark comparison is needed. (d) Separability claim overstated (R1, Moderate).  Abstract says \\\" <0.3% under binary scoring\\\" but GSM8K reaches 3.0% and MATH 2.5%. A finding that holds on 3/5 benchmarks is benchmark-conditional, not general. The abstract and conclusions should lead with the conditionality. 3.3 Experimental Design -  MMLU G-study (1,036,800 records):  Strong. V0 enforce_ eager control is excellent experimental hygiene. -  Cross-benchmark (1,382,400 records):  Adequate but reduced design; asymmetry concern above. -  Multi-hardware (691,200 records):  Adequate; 2 GPU types is the minimum, findings are directional. -  Item resampling stability (32,400 records):  Well-designed; CV=4.1% on item_ id is reassuring. -  14B extension (345,600 records):  Useful but underpowered (2 models, 1 df for model effects). -  Fine-tuning (1,728 runs):  Adequate for its scope but architecturally distant from the decoder inference setting. Best framed as preliminary evidence. 3.4 Reproducibility Gaps R1 flags: vLLM version should include commit hash (not just version number); model weight HuggingFace revision hashes needed; exact CUDA/cuDNN/driver versions should be reported; prompt template text should appear in an appendix; item sampling seeds should be released. 4. Related Work Assessment (R2-led) The bibliography has improved dramatically from earlier drafts (7→22 references). Four Related Work paragraphs are well-organized. Positioning against prior work is largely fair and accurate. Missing References (R2) 1.  GeneralizIT (Nalisnick et al., 2024)  — G-theory software for ML. Relevant to tooling discussion. 2.  Kunievsky et al. (2025)  — prompt sensitivity decomposition into intent/articulation/model uncertainty. Relevant to interpreting prompt×item. 3.  Brittlebench (2026)  — prompt brittleness benchmark, ~ 50% prompt variance. Directly relevant. 4.  Bui et al. (2025)  — seed sensitivity in RoBERTa/Llama fine-tuning. Relevant to Section 8.2. 5.  ThinkingMachines (2025)  — batch invariance failure (80/1000 unique completions at T=0). Explains why seed×item is non-zero even at T=0; relevant to the vLLM batch nondeterminism concern. Minor Positioning Issues -  The claim that prior ANOVA studies \\\"lack D-study machinery\\\" is technically true but slightly misleading — bootstrap approaches can achieve similar projections; G-theory's advantage is closed-form projection. -  Vania et al. (2021) is in the bibliography but not discussed in Related Work text. 5. Presentation Assessment (Joint) Strengths -  Clean three-claim structure, well-supported throughout. -  \\\"Unifying explanation\\\" framing for the gradient is effective. -  Balanced Discussion with thorough Limitations paragraph. -  Engine confound discovery presented with appropriate before/after validation. -  Honest framing of infrastructure crossing as confirmatory. Weaknesses -  Zero figures (R2, Major).  This is a serious deficiency for a variance decomposition paper. Stacked-bar charts are an expected field idiom (Mesting 2026). The cross-benchmark gradient, D-study projections, and facet effectiveness inversion all cry out for visualization. With 19 tables and 0 figures, the paper is dense and visually monotonous. This is a competitive disadvantage at a top venue. Easily fixable. -  Title promises \\\"Evaluation Metrics\\\" but delivers only binary scoring (R2, Moderate).  Logprob analysis is a one-paragraph appendix. Either deliver the metric-conditional analysis or adjust the title. -  Fine-tuning section feels bolted on (R2, Moderate).  RoBERTa-large fine-tuning on SST-2/MNLI/RTE/COPA is architecturally distant from 7–14B decoder inference. Cross-paradigm generalization is weak. Should be explicitly qualified as preliminary. -  No cost analysis for recommended budgets (R2, Minor).  The D-study recommends specific allocations but does not estimate GPU-hour costs. Without cost, the budgets remain theoretical. 6. Scope Assessment (Joint) Adequate for claimed scope -  5 benchmarks spanning knowledge-to-reasoning: sufficient for the gradient claim. Non-overlapping bootstrap CIs provide statistical support. -  4×7–9B models showing consistent per-model patterns: gradient is not a single-model artifact. -  14B extension within the 8B range: scale invariance holds at this increment. Limitations that should constrain claims -  No 70B+ models.  Larger models may compress item_ id through higher accuracy and reduce CoT stochasticity through stronger reasoning. Generality claims should be scoped to 7–14B. -  No proprietary API models.  GPT-4/Claude/Gemini have opaque infrastructure. Separability null may not hold when infrastructure is uncontrolled. Mesting studied API models; this paper studies open-weight models. Complementarity should be discussed. -  No non-English benchmarks.  Tokenization effects on item difficulty could alter cross-lingual variance structure. -  No generation-based benchmarks.  All are multiple-choice or short-answer. Open-ended generation may have fundamentally different variance structures. -  200-item samples.  Resampling stability tested only for MMLU. Other benchmarks lack resampling validation. 7. Roundtable: Convergence and Divergence Full Convergence (Both Reviewers) 1.  Score: 4/6 (Weak Accept).  At the acceptance threshold, contingent on addressable revisions. 2.  Cross-benchmark gradient is the paper's strongest, most novel contribution.  Well-supported by data, non-overlapping CIs, per-model consistency. 3.  Separability null is confirmatory, not novel.  Honest framing is appreciated. 4.  D-study budgets are the most practically useful output.  Immediately actionable. 5.  Infrastructure crossing yields near-null results.  The claimed advance over Mesting produces confirmatory rather than discovery findings. 6.  Fine-tuning extension is architecturally distant.  Should be qualified as preliminary. 7.  Zero figures is a serious presentation weakness.  Easily fixable; would materially improve the paper. 8.  Scope limited to 7–14B open-weight models.  Claims should be scoped accordingly. 9.  Engine confound discovery is a standalone methodological contribution.  Valuable to the community. Partial Convergence 10.  Separability conditionality (R1 raised, R2 endorsed after cross-sharing).  The abstract's \\\" <0.3%\\\" is accurate for knowledge benchmarks but not for GSM8K/MATH. Both reviewers agree the abstract should qualify this. 11.  Missing references (R2 raised, R1 endorsed).  Five missing references (GeneralizIT, Kunievsky, Brittlebench, Bui, ThinkingMachines) are relevant and should be added. R1-Only Concerns (Not Contested by R2) 12.  Binary data in G-theory  — a critical methodological point that R2 did not independently flag but endorses as important. The paper's primary analysis uses binary data under methods assuming continuous responses. Must be discussed. 13.  Temperature/ordering as random facets  — 2–3 temperature levels and 4 systematic orderings are dubious as random draws. R2 did not raise this but acknowledges the statistical logic. 14.  Asymmetric designs across benchmarks  — FP32 absent from non-MMLU experiments confounds cross-benchmark precision comparisons. R2-Only Concerns (Not Contested by R1) 15.  Title/metrics mismatch  — \\\"Evaluation Metrics\\\" in title but only binary scoring in main text. R1 did not flag this but agrees the title should match content. 16.  Comparison with IRT approaches  — the D-study budgets should be compared with tinyBenchmarks (Polo et al.) recommendations. What does G-theory add over IRT-based subsampling? 17.  Cost analysis for budgets  — GPU-hour estimates would make recommendations concrete. 8. Consolidated Strengths 1.  Cross-benchmark variance gradient is a genuine, well-supported empirical contribution  that unifies contradictory prior findings. The monotonic 35pp gradient with mechanistic CoT explanation and non-overlapping bootstrap CIs is the paper's signature finding. 2.  Massive experimental scale  (4M+ records, 5 benchmarks, 6 models, fully crossed factorial designs). Few empirical papers in this area match the breadth. 3.  D-study reproducibility budgets are immediately actionable.  Specific item/prompt/seed allocations for G≥0.90, benchmark-specific, with projection grids. 4.  Engine confound discovery and correction  (vLLM V0 vs. V1 routing) is a standalone methodological contribution. 5.  Model-as-facet analysis  cleanly separates model×item interaction (~ 10%) and preserves the gradient after extraction. 6.  Honest framing throughout.  Separability as confirmatory, item dominance as psychometrically expected, gradient as directional with quantified uncertainty. 7.  Comprehensive robustness checks.  Item resampling stability, REML vs. Henderson III, bootstrap CIs, per-model breakdowns, 14B scale validation. 8.  Counter-intuitive G pattern  (knowledge benchmarks yield lower G than reasoning benchmarks) is well-explained and insightful. 9.  Current-practice G<0.25  is an important and alarming finding for the field. 9. Consolidated Weaknesses Major 1.  Binary data in standard G-theory  without discussion of the methodological limitation. Item_ id dominance is partially artifactual from the Bernoulli variance function. Must be addressed in revision. 2.  Zero figures in a variance decomposition paper.  19 tables and 0 figures. Stacked-bar charts, D-study curves, and gradient visualizations are expected idioms. Serious competitive disadvantage at a top venue. 3.  Temperature (2–3 levels) and ordering (4 systematic rotations) as random facets  is statistically dubious. Sensitivity analysis with these as fixed effects is needed. Moderate 4.  Asymmetric designs across benchmarks  confound cross-benchmark precision comparisons (FP32 absent from non-MMLU experiments). 5.  Separability claim overstated in abstract  — holds on knowledge benchmarks but GSM8K (3.0%) and MATH (2.5%) exceed the stated threshold. Should be qualified. 6.  Title promises \\\"Evaluation Metrics\\\" but delivers only binary scoring  in main text. Logprob analysis relegated to one-paragraph appendix. 7.  Infrastructure crossing is the claimed advance over Mesting but yields near-null results.  The main findings would emerge from a Mesting-style design with fixed infrastructure. 8.  No models above 14B.  Generality cannot be claimed beyond this scale range. 9.  Missing references:  GeneralizIT, Kunievsky et al. (2025), Brittlebench (2026), Bui et al. (2025), ThinkingMachines (2025). 10.  Fine-tuning extension (RoBERTa-large, encoder-only)  is architecturally distant from decoder inference. Feels appended rather than integrated. Minor 11.  No cost analysis for recommended D-study budgets. 12.  Residual component (6–18%) is underanalyzed; higher-order interactions mentioned but not tabulated. 13.  14B extension is underpowered (2 models, 1 df for model effects). 14.  Item resampling stability tested only for MMLU, not for other benchmarks. 15.  Prompt template text not provided; reproducibility details (vLLM commit hash, model weight hashes, CUDA versions) insufficient. 10. Consolidated Questions for Authors 1.  Binary data:  How do you address the assumption violation of applying Henderson III / REML to binary (0/1) responses? Have you considered generalized G-theory or a probit/logit link-function decomposition? Does item_ id dominance survive under a method appropriate for binary data? 2.  Temperature as random facet:  What justifies treating 2–3 temperature levels (specific design points: 0, 0.5, 1.0) as a random rather than fixed facet? Have you compared results with temperature as fixed? 3.  Cross-benchmark precision confound:  Have you re-analyzed MMLU restricted to BF16/FP16 only (excluding FP32) for the cross-benchmark comparison? Does the precision gradient survive with matched precision levels? 4.  Gradient under logprob scoring:  Does the full 5-benchmark gradient (MMLU > ARC > HellaSwag > GSM8K > MATH) hold under logprob-based scoring? If not, is the gradient partially an artifact of binary scoring thresholds? 5.  Comparison with IRT:  How do the D-study budgets compare to Polo et al.'s tinyBenchmarks recommendations for MMLU? What does G-theory add over IRT-based efficient subsampling? 6.  Separability scope:  How confident are you that the separability null extends to more diverse hardware (A100 vs. H100 vs. B200) where architectural differences are more substantial? 7.  Judge variance complementarity:  Your entire variance structure sits \\\"underneath\\\" Mesting's judge variance (43.8%). How should practitioners interpret your budgets for LLM-as-judge evaluation? Would the gradient hold if judge were included as a facet? 8.  Negative variance estimates:  How are negative Henderson III estimates handled (set to zero, left negative, redistributed)? This affects the separability claim where infra×method components are near zero. 9.  D-study optimization procedure:  How were the \\\"optimal\\\" prompt and seed counts determined? Formal cost minimization, or chosen by inspection? 10.  Rank instability analysis:  Have you computed what fraction of published leaderboard rankings would change under re-evaluation with different seeds/prompts? This would make G <0.25 more concrete than an abstract coefficient. 11. Recommended Revisions (Priority-Ordered) Must-fix for acceptance 1.  Add 3–5 figures: (a) cross-benchmark stacked-bar gradient, (b) D-study G vs. total evaluations curves, (c) facet effectiveness ratio visualization, (d) bootstrap CI forest plot. 2.  Add a paragraph discussing binary data limitations in G-theory estimation and note that logprob scoring provides the methodologically cleaner decomposition. 3.  Present sensitivity analysis with temperature as fixed facet. 4.  Qualify separability claim in abstract: \\\" <0.3% on knowledge benchmarks; rises to 2–3% on reasoning benchmarks.\\\" Should-fix 5.  Re-analyze MMLU at BF16/FP16 only for the cross-benchmark comparison table. 6.  Add the 5 missing references (GeneralizIT, Kunievsky, Brittlebench, Bui, ThinkingMachines). 7.  Align title with content: either deliver metric-conditional analysis or remove \\\"Evaluation Metrics\\\" from title. 8.  Add prompt template text in an appendix; provide vLLM commit hash, model weight hashes. Nice-to-have 9.  Extend logprob analysis to all 5 benchmarks to test whether the gradient holds under continuous scoring. 10.  Add cost estimates (GPU-hours) for recommended D-study budgets. 11.  Expand higher-order interaction analysis in appendix. 12. Overall Assessment Score: 4/6 (Weak Accept) Confidence: High Meta-Review Justification Both reviewers independently scored this paper 4/6 (Weak Accept) with high confidence, and the roundtable did not identify grounds to change this. The cross-benchmark variance gradient is a genuine novel finding: no prior work has demonstrated the systematic shift from item-dominated (knowledge tasks) to interaction-dominated (reasoning tasks) variance structure, and the 35pp gradient with non-overlapping bootstrap CIs is well-supported. The D-study reproducibility budgets fill a real practical gap, and the G <0.25 indictment of current practice is alarming and important. The paper is held back by addressable issues: (a) zero figures is a serious presentation weakness at a top venue; (b) binary data in standard G-theory requires explicit discussion; (c) temperature/ordering as random facets needs sensitivity analysis; and (d) the separability claim needs scoping. None of these are fatal. If the must-fix revisions are made — especially adding figures and the binary data discussion — the paper would likely move to 5/6 (Accept). The infrastructure crossing, positioned as the key methodological advance over Mesting, yields near-null results. This is intellectually honest (confirmatory null) but means the paper's primary novelty rests on the cross-benchmark gradient and D-study budgets rather than on the infrastructure-methodology crossing. Both reviewers agree this is sufficient for a top venue, given the scale of the empirical contribution and the practical utility of the findings. Bottom line:  A well-executed, large-scale empirical study with a genuine novel finding (the gradient), actionable outputs (D-study budgets), and an important policy implication (G <0.25). At the acceptance threshold; fixable revisions would push it to a clear accept.\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd01811bd38b35a5cb879f659e\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779320173947\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — median | dream_20260520T222113]  · Overall: weak accept dream_ id: dream_ 20260520T222113\\n tier: median\\n overall_ score: weak accept\\n timestamp: 2026-05-20T23:45:00+00:00 Dream Review Report — R1 (Methodology & Experimental Rigor) Paper:  Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics Tier:  Median Review mode:  R1 focus — Methodology, Experimental Design, Statistical Rigor 1. Paper Summary The paper applies Generalizability Theory (G-theory) to LLM evaluation, conducting multi-benchmark crossed-facet variance decompositions across five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), six models (4x7-9B + 2x14B), two GPU architectures, and multiple levels of precision, prompt template, seed, temperature, and answer ordering. Over 3 million evaluation records are analyzed. Three claims are made: (1) a benchmark-conditional variance gradient where item dominance ranges from 48% (MMLU) to 28% (MATH) under model-as-facet analysis; (2) infrastructure x methodology separability at the aggregate level ( <0.5% on knowledge benchmarks, rising to 3% on math-generation benchmarks); (3) metric-conditional, benchmark-specific reproducibility budgets via D-study projections. Extensions cover 14B models, RoBERTa fine-tuning, LayerCast precision mitigation, and three scoring metrics. 2. Methodological Soundness 2.1 G-Theory Framework Application Largely correct, with one significant improvement over Dream #1.  The revised paper treats model as a crossed random facet (Section 4.4 / Table 5), which was the most critical methodological concern in the prior review. This properly separates model×item interaction (16-22%) from pure item variance and residual. The 4pp systematic reduction across all benchmarks is plausible and consistent with psychometric expectation when objects of measurement have heterogeneous difficulty profiles. Henderson Method III vs. REML.  The paper uses Henderson Method III (expected mean squares) as primary estimation with REML as sensitivity check. This is defensible: Henderson III is unbiased for balanced designs, and the design is nearly balanced (fully crossed within each experiment). The reported max divergence of 2.1pp with preserved rank ordering is reassuring. However: -  Concern:  Henderson Method III can produce negative variance component estimates for near-zero components. The MATH table (Table 22 in the imagined experiments) shows a negative \\\"other\\\" entry (-1.5%), which is characteristic of this issue. The paper should explicitly state how negative estimates are handled (set to zero? redistributed? left as-is?). This matters for the separability claim where infra×method components are near zero — a negative estimate truncated to zero looks different from a genuinely zero estimate. -  Concern:  The G-theory formula presented in Equation 2 is simplified. The actual D-study formula for a multi-facet crossed design with 5+ facets involves many more terms. The paper should either present the full formula used or cite a specific implementation (e.g., GeneralizIT package). The simplified formula risks misleading readers about how D-study projections were actually computed. 2.2 Crossed Random-Effects Assumptions Items as random facet:  Justified. The 200 items per benchmark are sampled (stratified) from larger pools (MMLU: 14,042; ARC: 2,590; GSM8K: 1,319; HellaSwag: 10,042; MATH: 5,000). The random-facet assumption requires that observed items are exchangeable draws from a universe of admissible observations. Stratified sampling strengthens this by ensuring subject/topic coverage. Model as random facet:  Partially justified. Four 7-9B models from different families (Qwen, Llama, Gemma, Mistral) are treated as exchangeable draws from the universe of \\\"7-9B instruction-tuned LLMs.\\\" This is defensible but arguable — the model universe is not well-defined, and four models provide limited degrees of freedom for estimating model-related variance components. The 14B extension (2 models) is even more constrained. The paper should acknowledge that model-as-facet with k=4 yields imprecise estimates of model variance components and that the model universe is narrowly defined (open-weight, instruction-tuned, 7-9B). Prompt as random facet:  The 6 prompt templates are described but their generation process matters for the random-effects assumption. If they were systematically designed to vary specific dimensions (e.g., formality, instruction explicitness), they may not represent random draws from a prompt universe. The paper should clarify whether prompt templates were generated to be representative (supporting random effects) or to maximize diversity (which biases variance estimates upward). Seed as random facet:  Clearly justified — seeds are arbitrary integers drawn from a large space. Temperature as random facet:  Problematic. With only 2-3 levels (e.g., 0, 0.5, 1.0), treating temperature as a random facet is statistically dubious — these are specific points chosen to span the parameter range, not random draws from a temperature distribution. Temperature is better modeled as fixed. If treated as random, the variance estimates carry extreme uncertainty with 2-3 df. The paper should address this. Ordering as random facet:  Four orderings (ABCD, BCDA, CDAB, DABC) — these are systematic rotations, not random draws. The random-effects assumption is defensible only if one argues these represent exchangeable draws from the universe of possible orderings, which is reasonable for 4-option MC but should be noted. 2.3 Variance Estimation for Binary Data Critical methodological question.  Binary correct (0/1) data violates the normality assumption underlying standard G-theory variance component estimation. Henderson Method III and REML both assume continuous, approximately normal response variables. For binary data: -  Variance components are bounded by the Bernoulli variance p(1-p), creating ceiling effects for items near p=0 or p=1. -  Item-level variance is mechanically linked to item difficulty — easy and hard items contribute less variance by construction, inflating the apparent dominance of \\\"mid-difficulty\\\" items. -  The paper's finding that item_ id is the largest variance source is partially an artifact of using binary scoring on items with heterogeneous difficulty. This is the well-known \\\"item difficulty confound\\\" in classical test theory. The text-exact-match metric (also binary) and logprob metric (continuous) provide useful sensitivity checks. The logprob result (item_ id = 55%) is methodologically cleaner because the response variable is continuous, avoiding the binary data issue. The paper should discuss the binary data limitation explicitly and note that logprob scoring provides the most methodologically sound variance decomposition. 3. Experimental Design 3.1 Factorial Design Adequacy MMLU (Exp 1): Strong.  4 models × 3 precisions × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 items = 1,036,800 observations. This is the richest design and supports all claimed decompositions. The V0 enforce_ eager control eliminates the engine confound — this is excellent experimental hygiene. Cross-benchmark (Exp 3): Adequate but reduced.  2 precisions × 2 temperatures (vs. 3×3 on MMLU). The reduction is justified by compute constraints but creates an asymmetry: FP32 is absent from cross-benchmark experiments, meaning the precision facet is restricted to BF16/FP16 (which differ minimally). The claimed cross-benchmark gradient in precision effects (MMLU 3.0% vs. GSM8K 1.0%) is confounded with the different precision levels tested. This should be explicitly acknowledged. Multi-hardware (Exp 4): Adequate.  2 GPU types is the minimum for estimating hardware effects. With 1 df for hardware main effect, the estimate is necessarily imprecise. The paper correctly frames hardware findings as directional rather than definitive. Item resampling (Exp 2): Well-designed.  Three independent stratified draws with different seeds. The CV=0.19 (paper) or CV=0.19 (imagined experiments) on item_ id is an important honesty result. However, three draws provide only a rough estimate of resampling variability — 10+ draws would be more convincing, though the compute cost may be prohibitive. Fine-tuning (Exp 7): Adequate for its scope.  432 runs per task × 4 tasks = 1,728 total. The fully crossed design (seed × LR × shuffle × GPU × precision) is clean. The RoBERTa-large choice is acknowledged as a limitation (encoder-only, classification). This experiment is best framed as a conceptual extension rather than a direct generalization. 3.2 Missing Controls and Confounds 1.  Batch size / sequence length confound.  vLLM batches requests dynamically. If different benchmark items produce different output lengths (especially GSM8K/MATH with CoT), batch composition may vary, introducing an unmodeled variance source that gets absorbed into residual or item interactions. The paper uses \\\"default vLLM settings\\\" which is realistic but means batch-level nondeterminism is present. 2.  Prompt template × benchmark interaction.  The same 6 prompt templates are used across benchmarks, but their appropriateness may vary by task. A prompt template that works well for MMLU factual recall may be poorly suited for GSM8K math reasoning. This could inflate prompt×item interactions on some benchmarks for reasons unrelated to the \\\"prompt sensitivity\\\" construct. 3.  Item difficulty distribution differs across benchmarks.  MMLU items span a wide difficulty range; GSM8K items at 8B model scale cluster near 0.4-0.6 accuracy; MATH items are heavily bimodal (trivial or impossible for 8B models). These distributional differences mechanically affect how much variance is attributable to items vs. interactions. The paper's \\\"cognitive complexity\\\" explanation for the cross-benchmark gradient is plausible but not the only explanation — difficulty distribution differences could account for part of the pattern. 4.  Stratified sampling details.  The paper mentions stratified sampling across 57 MMLU subjects, but the stratification scheme for other benchmarks (GSM8K difficulty levels? MATH topics?) is not described. If non-MMLU benchmarks lack stratification, their item samples may be less representative. 5.  Answer extraction method.  For generation-based scoring, the method of extracting answers from generated text is a potential confound. Different regex/parsing strategies could produce different binary scores for the same generation. This is not discussed. 3.3 Item Sampling Strategy The 200-item stratified sample from MMLU's 14,042 items (1.4%) is a reasonable balance between compute cost and representativeness. The resampling stability test (CV=0.19) properly quantifies the sampling uncertainty. For other benchmarks: -  GSM8K: 200/1,319 = 15.2% — much denser sampling, less sampling uncertainty expected. -  ARC-Challenge: 200/2,590 = 7.7% — moderate. -  HellaSwag: 200/10,042 = 2.0% — similar to MMLU. -  MATH: 200/5,000 = 4.0% — moderate. The paper should note that cross-benchmark comparisons of item_ id variance share are confounded with sampling fraction — benchmarks with denser item sampling (GSM8K) mechanically have lower item-sampling uncertainty, which could affect the D-study projections. 4. Statistical Rigor 4.1 Bootstrap Confidence Intervals Construction:  1,000 item×condition resamples. This is a standard nonparametric bootstrap for G-theory (cf. Brennan, 2001, Ch. 10). The resampling unit matters: resampling items treats items as the primary sampling unit, which is appropriate given that item selection is the largest variance source. Concerns: -  The bootstrap resamples items but holds conditions (prompt, seed, temp, precision, ordering) fixed. This captures item-sampling uncertainty but not condition-sampling uncertainty. A more thorough approach would resample both items and conditions (double bootstrap), though this is computationally expensive and rarely done in G-theory applications. The paper should acknowledge this limitation. -  The reported CI widths (~ 0.14 for item_ id) are wide enough that the practical implications change substantially across the CI range. For example, MMLU item_ id [ 0.41, 0.55] maps to different D-study recommendations at each endpoint. The paper handles this well by reporting D-study CIs ([ 350, 510 ] for G≥0.90 on MMLU). 4.2 D-Study Projections Validity:  D-study projections assume that variance components estimated from the G-study generalize to the projected design. This is the standard G-theory assumption and is reasonable when the projected design changes only the number of levels (e.g., more items, more seeds) rather than the nature of the facets. The projections in Table 8 change item counts while holding prompt/seed counts at \\\"optimal\\\" levels — this is valid. Concern — optimal prompt/seed counts.  The D-study recommends \\\"3 prompts / 4 seeds\\\" for MMLU and \\\"4 prompts / 6 seeds\\\" for GSM8K. How are these \\\"optimal\\\" counts determined? If they are chosen to minimize total compute for a target G, the optimization procedure should be described. If they are chosen post-hoc to make the item counts look reasonable, this is problematic. Concern — extrapolation to 420+ items.  The G-study uses 200 items. Projecting to 420 items assumes linear scaling of the error reduction, which holds under the random-sampling model. However, if the additional 220 items are drawn from the same pool, they may not be independent of the original 200 (especially for smaller pools like GSM8K with only 1,319 total items). The finite-population correction should be applied when the projected sample is a large fraction of the universe. 4.3 REML Sensitivity Check Sufficient for its purpose.  The 2.1pp maximum divergence with preserved rankings is adequate evidence that the choice between Henderson III and REML does not affect qualitative conclusions. However, REML is generally preferred for unbalanced designs. Since the within-experiment designs are balanced (fully crossed), Henderson III is appropriate. The sensitivity check confirms this. 4.4 Permutation Test for Gradient The p=0.003 for the gradient direction (MMLU > HellaSwag on item_ id) is properly reported. The paper correctly notes that the CIs overlap partially at the margins ([ 0.38, 0.41 ]), supporting directional but not magnitude claims. This is honest and appropriate. 5. Reproducibility Concerns 1.  vLLM version dependency.  The paper uses vLLM 0.9.2 with V0 enforce_ eager. vLLM's behavior changes across versions (the V0/V1 engine confound demonstrates this). The results may not replicate on vLLM 0.8.x or 1.0.x. The paper should pin the exact vLLM commit hash, not just the version number. 2.  Model weight provenance.  The paper lists model names but not specific weight versions (e.g., HuggingFace revision hashes). Model weights on HuggingFace can be updated without changing the model card name. For reproducibility, exact weight hashes are needed. 3.  CUDA version and driver.  CUDA nondeterminism is a core topic of the paper. The exact CUDA version, cuDNN version, and driver version should be reported. The paper mentions \\\"CUDA 12.8\\\" support for vLLM 0.9.2 but does not pin the exact software stack. 4.  Item sample seeds.  The stratified sampling seeds for the 200-item samples should be released. The resampling stability test uses seeds 0, 7, 99 — are these the only seeds tested? If the main experiments use a single seed (e.g., seed 0), the results are conditional on that particular draw. 5.  Prompt template text.  The 6 prompt templates are critical to reproducibility but their exact text is not provided in the paper. They should appear in an appendix. 6. Strengths -  Comprehensive factorial design.  The MMLU experiment (1,036,800 observations, 5,184 conditions) is one of the largest crossed factorial designs in LLM evaluation research. The systematic approach — full crossing on MMLU, reduced crossing on other benchmarks, explicit confound controls — reflects careful experimental planning. -  Engine confound discovery and fix.  Identifying that default vLLM routes FP32 through a different engine (V1 CUDA graph) than BF16/FP16 (V0 eager) is a standalone methodological contribution. The enforce_ eager fix is simple, actionable, and immediately useful to the community. -  Model-as-facet analysis.  This revision correctly treats model as a crossed random facet, addressing the most fundamental concern from Dream #1. The systematic 4pp reduction across all benchmarks and the extraction of 16-22% model×item interaction is a clean result. -  Multi-benchmark coverage.  Five benchmarks spanning knowledge retrieval (MMLU, ARC), commonsense reasoning (HellaSwag), arithmetic reasoning (GSM8K), and proof reasoning (MATH) provides genuine coverage of the LLM evaluation landscape. The three-tier clustering is more nuanced than a simple monotonic gradient. -  Metric-conditional analysis.  The binary/text-match/logprob comparison (Table 9) is a first-order finding: G ranges from 0.32 to 0.97 depending on the scoring metric. This alone justifies the paper — practitioners cannot discuss \\\"reliability\\\" without specifying the metric. -  Honest uncertainty quantification.  Bootstrap CIs on variance components, D-study CIs on item counts, resampling stability tests, and REML sensitivity checks collectively demonstrate statistical maturity. The paper acknowledges that the gradient is directional rather than precisely quantified. -  Three-tier narrative is stronger than two-cluster.  Including MATH extends the gradient from {MMLU, ARC} vs. {GSM8K, HellaSwag} to a three-tier structure with 20pp spread, providing more evidence for the benchmark-conditional story. -  Separability as confirmatory null.  Reframing infrastructure×methodology separability as a confirmatory result (validating prior isolated-factor studies) rather than a breakthrough is intellectually honest and strengthens the paper's credibility. -  Fine-tuning contrast.  The inverted variance hierarchy (LR/seed dominate in fine-tuning vs. items dominate in inference) adds conceptual depth and explains why different evaluation modes have different reproducibility conventions. 7. Weaknesses Major -  Binary data in G-theory.  Applying standard G-theory variance component estimation (Henderson III / REML) to binary (0/1) data is methodologically questionable. The response variable violates normality and homoscedasticity assumptions. Item variance is mechanically linked to item difficulty via the Bernoulli variance function. This affects the headline item_ id estimates and all downstream D-study projections. The logprob analysis partially mitigates this, but the paper's primary analysis is on binary data. A generalized G-theory approach (Brennan, 2001, Ch. 12) or a link-function-based decomposition would be more appropriate. At minimum, the paper must discuss this limitation and note that item dominance under binary scoring is partially artifactual. -  Temperature and ordering as random facets.  With 2-3 temperature levels and 4 systematic ordering rotations, treating these as random facets is questionable. Random-effects estimation requires the observed levels to be exchangeable draws from a larger universe. Temperature levels (0, 0.5, 1.0) are specific design points, not random draws from a temperature distribution. The 4 orderings are systematic rotations, not random permutations of 4 !=24 possibilities. Misspecifying fixed effects as random inflates the estimated variance components for these facets and their interactions. The paper should either (a) justify the random-effects assumption for these facets, (b) treat them as fixed and re-estimate, or (c) present both analyses as a sensitivity check. -  Asymmetric designs across benchmarks weaken cross-benchmark claims.  MMLU uses 3 precisions × 3 temperatures; other benchmarks use 2 × 2. FP32 is absent from non-MMLU experiments. This means precision-related variance on MMLU includes the FP32 degradation effect that is absent from other benchmarks. The claimed gradient in precision effects (MMLU 3.0% → MATH 0.5%) is confounded with the different precision levels tested. The paper should either (a) re-analyze MMLU restricted to BF16/FP16 for the cross-benchmark comparison, or (b) explicitly state the confound. -  Separability claim is benchmark-conditional but presented as a general finding.  The abstract and contributions list separability as \\\" <0.5% binary\\\" but the body reveals GSM8K reaches 3.0% and MATH reaches 2.5%. A finding that holds on 3/5 benchmarks but fails on 2/5 is not a general separability result — it is a benchmark-conditional one. The abstract and conclusions should lead with the conditionality. Moderate -  D-study \\\"optimal\\\" prompt/seed counts are not derived.  The paper presents specific prompt and seed counts (3/4 for MMLU, 4/6 for GSM8K) as \\\"optimal\\\" without showing the optimization procedure. Are these the minimum counts that don't substantially change the D-study item projection? Are they from a cost-minimization formula? The derivation matters because practitioners will use these numbers directly. -  Residual component is large and underanalyzed.  Residual ranges from 6% to 18% across benchmarks and analyses. Under model-as-facet analysis, the residual on MMLU drops from 14% to 8%, which is progress, but 8% is still substantial. What is in this residual? Higher-order interactions (3-way and above) are mentioned in passing (\\\"3-5% total\\\") but not tabulated. The paper claims higher-order interactions are small, but 3-5% is comparable to many named 2-way interactions (e.g., seed×item at 2.0%). An appendix breaking down the residual would strengthen the paper. -  HellaSwag clustering with GSM8K is not well-explained.  HellaSwag is a commonsense reasoning / sentence completion task, not a math reasoning task. Its item_ id (31%) places it in the same tier as GSM8K (36%), but its infra×method (0.3%) is similar to knowledge benchmarks. The paper groups them in a \\\"mid\\\" tier based on item_ id alone, but the infra×method pattern suggests HellaSwag behaves differently from GSM8K. The three-tier narrative is cleaner than the data fully support. -  14B extension is underpowered.  With only 2 models, model-as-facet analysis has essentially 1 df for model effects. The reported model×item = 25% (vs. 21% at 8B) could reflect the specific model pair chosen (dense vs. reasoning-distilled) rather than a scale effect. The paper should note that the 8B→14B comparison confounds scale with architecture diversity. -  No correction for multiple comparisons.  Many variance components are tested across many benchmarks and metrics. While the bootstrap CIs provide individual component uncertainty, no family-wise error correction is applied. The GSM8K infra×method CI [ 0.012, 0.048 ] excludes zero, but is this still significant after correcting for testing the same hypothesis on 5 benchmarks? Minor -  \\\"Over 3 million\\\" vs. \\\"over 4 million.\\\"  The abstract says \\\"over 3 million\\\"; the best-tier paper says \\\"over 4 million.\\\" The actual count should be computed and reported exactly. -  MATH \\\"other\\\" = -1.5%.  Negative variance component estimates should be flagged and the handling policy stated (see Section 2.1 above). -  LayerCast section (8.3) adds little.  The finding that LayerCast provides marginal benefit over BF16 is expected given that precision effects are already small. This could be condensed to 1-2 sentences or moved to an appendix. -  Table 5 (model-as-facet) shows \\\"---\\\" for MATH precision entries.  If precision was not tested on MATH (only BF16/FP16), this should be noted explicitly rather than with a dash. 8. Questions for Authors 1.  How are negative variance component estimates handled?  Henderson Method III can produce negative estimates for near-zero components. Are these set to zero, left negative, or redistributed? This affects the separability claim. 2.  What justifies treating temperature (2-3 levels) as a random rather than fixed facet?  With 3 specific design points, the random-effects assumption is questionable. Have you compared results with temperature as fixed? 3.  For the cross-benchmark comparison, have you re-analyzed MMLU restricted to BF16/FP16 only (excluding FP32)?  This would make the precision facet comparable across benchmarks and test whether the precision gradient survives. 4.  How were the \\\"optimal\\\" prompt and seed counts in the D-study determined?  Is there a formal optimization procedure, or were these chosen by inspection? 5.  The bootstrap resamples items but not conditions. Have you considered a double bootstrap (resampling both items and conditions)?  This would capture total uncertainty rather than just item-sampling uncertainty. 6.  How do you address the binary data issue in G-theory estimation?  Standard methods assume continuous responses. Have you considered generalized G-theory or a probit/logit link function approach? 7.  The paper claims \\\"current practice G<0.25 everywhere\\\" — what specific \\\"current practice\\\" configuration yields this?  Is this 1 prompt × 1 seed × 200 items × 1 temperature × 1 precision? The baseline should be precisely defined. 8.  For GSM8K and MATH, how were answers extracted from generated text?  The extraction method is a potential confound for binary scoring. 9.  Were the 6 prompt templates the same across all 5 benchmarks?  If so, were they designed for MC format specifically, and how appropriate are they for GSM8K/MATH generation tasks? 10.  The fine-tuning experiment uses item-level accuracy across test set items as the response variable, or run-level aggregate accuracy?  If aggregate, G-theory is applied to a single number per run (N=432), which is a very different statistical regime than item-level analysis (N=432×test_ items). 9. Minor Issues -  The G-theory formula in Eq. 2 uses subscript notation that conflates \\\"conditions\\\" into a single $c$ — for a 5-facet design, the full formula should be shown or a reference to the exact formula used should be provided. -  Table 6 (cross-benchmark) reports 384,000 obs for GSM8K/ARC/HellaSwag but the experimental design (4 models × 2 prec × 6 prompts × 6 seeds × 2 temps × 4 orderings × 200 items) yields 4×2×6×6×2×4×200 = 230,400. The 384,000 figure is inconsistent — please verify. -  The paper switches between \\\"Henderson Method I\\\" (Section 4.6) and \\\"Henderson Method III\\\" (summary). These are different methods — please clarify which was used. -  Several tables show components that do not sum to 100% without explanation. A footnote about rounding and/or the treatment of negative estimates would help. -  The Related Work paragraph on training instability cites Dodge et al. (2020) but the bibliography entry has no venue information beyond \\\"arXiv preprint.\\\" -  The Lu et al. (2022) citation appears to be incorrect — the cited paper is about emergent abilities, not option ordering. Verify this reference. -  The Mesting (2026) bibliography entry says \\\"ACL\\\" but the literature map says \\\"arXiv.\\\" Verify the venue. 10. Score and Confidence Overall Score: 4/6 (Weak Accept) Confidence: High Justification The paper has substantially improved since Dream #1 by: (a) treating model as a crossed facet, (b) adding bootstrap CIs, (c) expanding to 5 benchmarks with a coherent three-tier narrative, (d) reframing infrastructure separability as confirmatory, (e) expanding the bibliography to 18 references (still below the 25+ target but much improved), and (f) acknowledging item dominance as psychometrically expected while emphasizing the benchmark-conditional gradient as the novel contribution. The cross-benchmark variance gradient — the central claim — is well-supported by data across five benchmarks, with honest uncertainty quantification (permutation p=0.003, directional not magnitude claims). The D-study reproducibility budgets fill a genuine practical gap. The metric-conditional finding (G=0.37 vs. G=0.97) is striking and immediately useful. The paper falls short of a clear accept (5/6) due to: (a) binary data in standard G-theory without discussion of the methodological limitation, (b) temperature/ordering as random facets with 2-4 levels is dubious, (c) asymmetric designs across benchmarks confound the cross-benchmark comparison of precision effects, and (d) the separability claim is overstated in the abstract given that 2/5 benchmarks show >2% infra×method interaction. These issues are addressable in revision: -  Add a paragraph discussing binary data limitations and cite generalized G-theory -  Present a sensitivity analysis with temperature as fixed -  Re-analyze MMLU at BF16/FP16 only for the cross-benchmark precision comparison -  Qualify the separability claim in the abstract with \\\"on knowledge benchmarks\\\" If these revisions are made, the paper would be a solid accept (5/6). The experimental scale, honest framing, and actionable D-study budgets make this a useful contribution to the evaluation methodology literature. Comparison to Dream #1 Score (4/6 Borderline Reject → 4/6 Weak Accept) Same numerical score but upgraded from \\\"borderline reject\\\" to \\\"weak accept\\\" in assessment. The Dream #1 review identified 7 actionable revisions; this version addresses 5 of them (model-as-facet, CIs, bibliography expansion, figures described, reframed contributions). The remaining 2 (separability threshold derivation, item dominance tautology acknowledgment) are partially addressed. The net effect is that the paper moves from \\\"below acceptance threshold\\\" to \\\"at the acceptance threshold, contingent on minor revisions.\\\" The methodological concerns raised in this review (binary data, temperature-as-random, asymmetric designs) are new issues not flagged in Dream #1 but are moderate rather than fatal.\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd01b8968a0b35597237b9ce1b\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779320148470\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — best | dream_20260520T222113]  · Overall: weak accept dream_ id: dream_ 20260520T222113\\n tier: best\\n reviewer: R2\\n focus: Novelty, Related Work Positioning, Significance/Impact\\n timestamp: 2026-05-20 Reviewer R2: Novelty, Related Work, and Significance 1. Summary This paper applies Generalizability Theory (G-theory) to LLM evaluation in a multi-benchmark setting, crossing infrastructure facets (numerical precision, GPU hardware) with methodology facets (prompt template, random seed, temperature, option ordering) and a measurement facet (item selection) across five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), six models (7--14B), and 4M+ evaluation records. Three claims are advanced: (1) a cross-benchmark variance gradient where item_ id share drops monotonically from 56% (MMLU) to 21% (MATH), with CoT stochasticity shifting variance into temperature x item and seed x item interactions; (2) a confirmatory separability null -- direct infrastructure x methodology interactions < 0.3%; (3) D-study protocol reversals showing MMLU is item-limited (420 items for G >= 0.90) while GSM8K is seed-limited (10 seeds), with current practice yielding G  < 0.25 everywhere. Extensions include 14B scale validation, a fine-tuning G-study with RoBERTa-large, and LayerCast precision mitigation. 2. Novelty Assessment Claim 1 (Cross-benchmark variance gradient): Moderate-to-high novelty. This is the paper's strongest novel contribution. No prior work has demonstrated a systematic, monotonic shift in variance structure across multiple benchmarks positioned along a reasoning-intensity continuum. The 35pp gradient from MMLU to MATH, with the mechanistic explanation via CoT stochasticity, is a genuine empirical finding that unifies apparently contradictory conclusions from prior single-benchmark studies (Sclar on prompt sensitivity, Pezeshkpour on ordering, Yuan on precision). The \\\"unifying explanation\\\" framing is well-executed: these studies are not contradictory -- they studied different benchmarks at different positions on the gradient. However, the finding that item_ id dominates is expected from measurement theory (Brennan, 2001, Ch. 3). Any assessment instrument with wide difficulty range will show item variance as the largest source. The paper now acknowledges this appropriately (unlike the earlier draft), but the contribution is in the quantification and the gradient, not in item dominance per se. Claim 2 (Confirmatory separability): Low novelty, moderate utility. This is a confirmatory null result. Infrastructure x methodology interactions are  < 0.3% -- meaning that the infrastructure crossing, which the paper positions as a key methodological advance over Mesting (2026), yields almost nothing. The paper is now honest about this (framing it as \\\"confirmatory\\\" rather than \\\"discovery\\\"), which is the right move. The nuanced decomposition into direct vs. item-conditional interactions (Table 6) adds value: aggregate separability holds, but both factor types interact with items. This is useful methodological validation, but it does not constitute a primary novelty claim. The practical implication is clear: researchers running isolated-factor studies (e.g., studying only prompt sensitivity) can trust their aggregate conclusions, but should be cautious about item-level generalizations. This is valuable guidance even if not surprising. Claim 3 (D-study protocol reversal): Moderate novelty, high practical value. The finding that MMLU needs 420 items while GSM8K needs 10 seeds -- and that the facet effectiveness ratio inverts from 14.2:1 (MMLU) to 0.8:1 (GSM8K) -- is actionable and non-obvious. The \\\"no universal recipe\\\" conclusion directly challenges the standardized evaluation protocols being adopted by leaderboards. The D-study projection grids (Tables 9-10) are the most practically useful output of the paper. The current-practice G  < 0.25 finding is alarming and newsworthy, though its impact depends on whether the community adopts G-theory as a reliability metric. The comparison to educational measurement's G >= 0.80 threshold is effective rhetoric. Collective novelty: The three claims together are stronger than any individual claim. The cross-benchmark gradient (Claim 1) explains the protocol reversal (Claim 3), and the separability null (Claim 2) validates the independent study of each factor type. The narrative coherence is good. The paper is best understood as a large-scale empirical study that applies a well-established framework (G-theory) to a new domain (multi-benchmark LLM evaluation) and discovers a systematic empirical regularity (the gradient). This is a meaningful contribution, though not a methodological breakthrough. Incrementality over Mesting (2026). The paper clearly advances over Mesting in three dimensions: (a) five benchmarks vs. one, (b) infrastructure crossing, (c) model as crossed facet. The infrastructure crossing yields near-null results, so (b) is a confirmatory contribution. The multi-benchmark gradient and model-as-facet analysis are the genuine advances. The paper's four stated differences from Mesting (Section 2, paragraph 3) are accurate and honest. One important difference the paper does not sufficiently emphasize: Mesting found judge identity as the dominant variance source (43.8%), while this paper fixes the judge and finds item_ id dominant. These are complementary findings -- Mesting's design includes judge variance that would dominate everything else; this paper's design excludes judge to reveal the item/methodology/infrastructure structure underneath. This complementarity should be discussed more explicitly. 3. Related Work Completeness The bibliography has improved dramatically from the earlier 7-reference draft to 22 references. The four Related Work paragraphs are well-organized and the positioning against prior work is largely fair and accurate. Adequately covered: -  Variance sources in LLM evaluation (Sclar, Pezeshkpour, Lu, Yuan, Biderman) -- good coverage -  ANOVA-based decomposition (Bouthillier, Henderson, Dodge, Sellam, Dehghani) -- well-positioned -  G-theory in NLP (Mesting, Brennan, Shavelson) -- properly cited with explicit differentiation -  IRT in NLP (Lalor, Rodriguez, Polo, Perlitz) -- good, with IRT/G-theory complementarity noted Missing or under-discussed references: 1.  Nalisnick et al. (2024), GeneralizIT  -- a G-theory software package for ML. Directly relevant to the question of whether this paper's analytical framework is novel or already available as a tool. Should be cited in the G-theory paragraph. 2.  Kunievsky et al. (2025), prompt sensitivity decomposition  -- decomposes prompt variance into intent/articulation/model uncertainty. Relevant to interpreting the prompt x item interaction component. The paper's related_ work_ notes mention it but the paper does not cite it. 3.  Brittlebench (2026)  -- prompt brittleness benchmark, ~ 50% prompt variance. In the project's own literature map but absent from the paper. Directly relevant to the prompt facet findings. 4.  Bui et al. (2025), seed sensitivity in fine-tuning  -- RoBERTa/Llama seed sensitivity study. Directly relevant to Section 8.2 (fine-tuning G-study). In the literature map but not cited. 5.  ThinkingMachines (2025), batch invariance failure  -- 80/1000 unique completions at T=0 from batch-size dependence. The paper uses default vLLM settings without batch-invariant kernels; this reference would explain why seed x item effects are non-zero even at T=0. Not cited. 6.  Vania et al. (2021)  -- IRT item properties in NLP. Listed in the bibliography but not discussed in the Related Work text. Should be integrated into the IRT paragraph. 7.  Mizrahi et al. (2024)  -- cited in the introduction but not in Related Work. Multi-prompt evaluation advocacy. Should appear in the variance sources paragraph. Positioning fairness: The paper's positioning against prior work is generally fair. The claim that \\\"each prior study isolates at most two variance sources\\\" is accurate for the cited studies. The differentiation from Mesting is honest and specific. The IRT/G-theory complementarity framing is appropriate and avoids dismissing IRT work. One concern: the paper states that prior ANOVA-based studies \\\"lack the D-study machinery for projecting reliability under alternative designs.\\\" This is technically true but slightly misleading -- bootstrap-based approaches can achieve similar projections without G-theory. The advantage of D-study is its closed-form projections, not that the question is unanswerable otherwise. 4. Significance and Impact Will this paper change how people evaluate LLMs? Partially. The D-study budgets are immediately actionable for benchmark designers and evaluation framework maintainers (e.g., lm-evaluation-harness, HELM). The \\\"G  < 0.25 everywhere\\\" finding is a compelling indictment of current practice. However, adoption depends on: 1.  Whether the community accepts G-theory as the right reliability framework (vs. IRT, bootstrap, or simple confidence intervals) 2.  Whether the computational cost of multi-seed, multi-prompt evaluation is acceptable 3.  Whether leaderboard operators are incentivized to change practices The paper would benefit from a concrete comparison: \\\"Running MMLU with the recommended budget (420 items, 3 prompts, 2 seeds = 2,520 evaluations) costs X GPU-hours per model, compared to Y GPU-hours for current practice.\\\" Without cost estimates, the budgets are theoretical. Are the D-study budgets practically useful? Yes, with caveats. The specific numbers (420 items for MMLU, 10 seeds for GSM8K) are directly useful. The facet effectiveness ratios (Table 12) provide a decision framework. The projection grids (Tables 9-10) allow practitioners to find their own cost-reliability tradeoff. The main limitation is that the budgets are derived from 7-14B open-weight models. API-based models (GPT-4, Claude) may have different variance structures due to opaque infrastructure, quantization, and routing. The paper acknowledges this but does not quantify the risk. Is \\\"no universal recipe\\\" surprising or obvious? Moderately surprising in its specificity. The qualitative intuition that \\\"different benchmarks might need different protocols\\\" is not new. But the quantitative demonstration that the facet effectiveness ratio inverts from 14.2:1 to 0.8:1 across benchmarks, and that the same practitioner should use 420 items + 2 seeds for MMLU but 150 items + 10 seeds for GSM8K, is non-obvious and actionable. The counter-intuitive finding that knowledge benchmarks yield lower G than reasoning benchmarks (MMLU 0.36 vs. GSM8K 0.55 under full factorial) is genuinely surprising and well-explained. 5. Framing and Narrative Strengths: -  The three-claim structure is clean and well-supported. -  The \\\"unifying explanation\\\" framing for the gradient is effective. -  The Discussion section is balanced, with a thorough Limitations paragraph. -  The engine confound discovery is presented with appropriate before/after validation. -  The paper correctly frames infrastructure crossing as confirmatory rather than primary novelty. Weaknesses: -  Zero figures.  This is a serious deficiency for a variance decomposition paper. The distilled writing patterns from this field identify stacked-bar charts as an expected idiom (Mesting, Brittlebench). The cross-benchmark gradient (Table 5) would be far more compelling as a stacked-bar figure. The D-study projections (Tables 9-10) cry out for line plots of G vs. facet allocation. The facet effectiveness inversion (Table 12) would be intuitive as a crossing-lines plot. With 14 tables and 0 figures, the paper is dense and visually monotonous. This is a competitive disadvantage at a top venue. -  The paper title promises \\\"Evaluation Metrics\\\" but delivers only binary scoring.  The abstract and main text focus entirely on binary correct scoring. Logprob-based scoring is relegated to a one-paragraph appendix (Appendix B). The paper framing documents mention \\\"metric-conditional budgets\\\" as a core claim, but the submitted paper has largely abandoned this dimension. Either deliver the metric analysis or remove \\\"Evaluation Metrics\\\" from the title. -  The fine-tuning section (8.2) feels bolted on.  RoBERTa-large fine-tuning on SST-2/MNLI/RTE/COPA is architecturally distant from the 7-14B decoder inference setting. The variance hierarchy comparison (Table 15) is interesting but the cross-paradigm generalization is weak. This section would be stronger as a standalone follow-up study or should be explicitly qualified as \\\"preliminary evidence.\\\" 6. Scope Concerns Is 5 benchmarks x 6 models x 7-14B sufficient? For the cross-benchmark gradient: yes, 5 benchmarks spanning knowledge-to-reasoning is adequate. The monotonic gradient with non-overlapping bootstrap CIs (Table 8) provides statistical support. Adding more benchmarks (e.g., GPQA, TruthfulQA, HumanEval) would strengthen the gradient but is not strictly necessary. For model generality: the 4 x 7-9B models show consistent patterns (per-model tables confirm the gradient within each model), and the 14B extension (Section 8.1) falls within the 8B range. However: 1.  No 70B+ models.  Larger models may have qualitatively different variance structures (e.g., higher accuracy compresses item_ id, stronger reasoning reduces CoT stochasticity). The paper cannot claim generality beyond the 7-14B scale. 2.  No proprietary API models.  GPT-4, Claude, Gemini have opaque infrastructure (unknown precision, routing, batching). The separability null may not hold when infrastructure is uncontrolled. Mesting (2026) studied API models; this paper studies open-weight models. The complementarity is noted but not deeply explored. 3.  No non-English benchmarks.  All five benchmarks are English-only. Cross-lingual variance structure could differ systematically (e.g., tokenization effects on item difficulty). 4.  No generation-based benchmarks.  All benchmarks are multiple-choice or short-answer. Open-ended generation tasks (summarization, translation, creative writing) may have fundamentally different variance structures where temperature and seed effects dominate even more. 5.  Only 200 items per benchmark.  MMLU has ~ 14K items, GSM8K has ~ 8K. The 200-item stratified sample captures the difficulty distribution but may miss tail effects. The resampling stability test (Section 4.3) partially addresses this but only for MMLU. 7. Strengths (bulleted) -  Cross-benchmark variance gradient is a genuine, well-supported empirical contribution  that unifies contradictory findings from prior single-benchmark studies. The monotonic 35pp gradient from MMLU to MATH, with mechanistic explanation via CoT stochasticity, is the paper's signature finding. -  Massive experimental scale : 4M+ evaluation records, 5 benchmarks, 6 models, crossed factorial designs. Few empirical papers in this area match the breadth. -  D-study reproducibility budgets are immediately actionable : specific item/prompt/seed allocations for G >= 0.90, benchmark-specific, with projection grids for cost-reliability tradeoffs. -  Engine confound discovery and correction  (vLLM V0 vs. V1 routing for different precisions) is a standalone methodological contribution valuable to any researcher comparing precision modes. -  Honest framing of the separability null : infrastructure crossing framed as confirmatory rather than primary novelty, with nuanced decomposition into aggregate vs. item-conditional interactions. -  Comprehensive robustness checks : item resampling stability, REML vs. Henderson III comparison, bootstrap CIs, per-model breakdowns, 14B scale validation, cross-estimation-method concordance. -  Bibliography substantially improved  over earlier drafts: 22 references covering variance sources, ANOVA decomposition, G-theory, and IRT literature. -  Counter-intuitive G pattern  (knowledge benchmarks yield lower G than reasoning benchmarks) is well-explained and adds insight beyond the headline gradient finding. 8. Weaknesses (bulleted) -  Zero figures in a variance decomposition paper  is a serious presentation deficiency. Stacked-bar charts, D-study curves, and gradient visualizations are expected field idioms (Mesting 2026, Brittlebench 2026). 14 tables + 0 figures makes the paper dense and hard to scan. -  Infrastructure crossing is the claimed methodological advance over Mesting but yields near-null results  ( < 0.3% direct interactions). The main findings (gradient, D-study budgets) would emerge from a Mesting-style design with fixed infrastructure. The paper is honest about this but it weakens the novelty argument. -  Title promises \\\"Evaluation Metrics\\\" but the paper delivers only binary scoring  in the main text. Logprob analysis is a one-paragraph appendix. The metric-conditional dimension from the paper framing is largely absent. -  No models above 14B.  Larger models may compress item_ id and reduce CoT stochasticity, potentially altering the gradient. Generality claims should be scoped to 7-14B. -  Fine-tuning extension (RoBERTa-large, encoder-only, classification)  is architecturally distant from the decoder inference setting. Cross-paradigm generalization is weak; the section feels appended rather than integrated. -  Missing references : GeneralizIT (2024), Kunievsky et al. (2025), Brittlebench (2026), Bui et al. (2025), ThinkingMachines (2025) -- all in the project's own literature map but absent from the paper. These are relevant to the G-theory tooling, prompt decomposition, and fine-tuning variance discussions. -  No cost analysis for recommended budgets.  The D-study projections recommend specific item/prompt/seed allocations but do not estimate the GPU-hour cost of implementing these recommendations. Without cost, the budgets are theoretical. -  200-item samples from much larger benchmarks.  Resampling stability is tested only for MMLU. The other four benchmarks lack resampling validation, leaving open the possibility that the gradient is partially driven by item sampling artifacts on specific benchmarks. 9. Questions for Authors 1.  The cross-benchmark gradient is your strongest finding. Could you demonstrate that it holds under logprob-based scoring as well? The one-paragraph Appendix B suggests item_ id drops to 42.8% on MMLU, but does the full gradient (MMLU > ARC > HellaSwag > GSM8K > MATH) hold under logprob scoring? If not, is the gradient an artifact of binary scoring thresholds? 2.  Your D-study recommends 420 items + 3 prompts + 2 seeds for MMLU (2,520 total evaluations). How does this compare to Polo et al.'s tinyBenchmarks recommendation for MMLU? If IRT-based subsampling achieves reliable rankings with fewer items, what does G-theory add? 3.  DeepSeek-R1-Distill-14B shows elevated temperature x item (8.8%) and seed x item (5.2%) on MMLU -- above the 8B range (Table 13). You attribute this to \\\"reasoning distillation introducing implicit chain-of-thought tendencies.\\\" Can you verify this mechanistically? Does DeepSeek-R1-Distill-14B produce longer or more variable outputs on MMLU items compared to the other models? 4.  The separability null holds for 2 GPU types (Section 6). How confident are you that this extends to, say, A100 vs. H100 vs. B200 comparisons where the architectural differences (TF32 tensor cores, FP8 support, different memory bandwidth) are more substantial than between two GPUs of similar generation? 5.  You fix the judge model, unlike Mesting who includes judge as a facet. Since Mesting found judge identity as the dominant source (43.8%), your entire variance structure sits \\\"underneath\\\" the judge variance. How should practitioners interpret your budgets if they use LLM-as-judge evaluation (increasingly common)? Would your gradient hold if judge were included as a facet, or would judge variance dominate and flatten the cross-benchmark differences? 6.  The fine-tuning G-study finds item_ id at rank-1 across all tasks (35.8-43.8%). But Bui et al. (2025) report extreme seed variance (RTES variance = 18.22) for RoBERTa on RTE. How do your RTE fine-tuning results compare to Bui et al.? Are the magnitudes consistent? 7.  Current-practice G  < 0.25 is your most alarming finding. Have you computed what fraction of published leaderboard rankings would change if evaluations were repeated with different seeds/prompts? A \\\"rank instability\\\" analysis (e.g., what percentage of model-pair orderings flip under re-evaluation) would make the inadequacy finding more concrete than an abstract G coefficient. 8.  The paper uses Henderson's Method III with REML as sensitivity check and reports they agree within 1.4pp. Have you considered Bayesian variance component estimation (e.g., via Stan or brms)? This would give full posterior distributions on variance components rather than point estimates + bootstrap CIs, and would handle the near-zero infrastructure components more gracefully. 10. Minor Issues -  Table 5 header says \\\"4 models pooled\\\" but the design description mentions \\\"4 models x 2 precisions x ...\\\" -- clarify whether model is pooled or crossed in this analysis. -  Table 7 (5-benchmark gradient) shows G_ full for GSM8K (0.55) higher than MATH (0.50), breaking the monotonic pattern. The text does not explain this reversal; add a brief note. -  The abstract says \\\"over 4 million evaluation records\\\" but summing the reported record counts (1,036,800 + 1,382,400 + 460,800 + 691,200 + 345,600 + 172,800 + fine-tuning) exceeds 4M. Provide an exact total or say \\\"approximately.\\\" -  Section 3.2 says \\\"2-3 levels\\\" for temperature but does not specify which benchmarks use 2 vs. 3 levels. Clarify. -  Table 1 (MMLU variance): the \\\"infra x method\\\" row aggregates multiple interaction terms. Break this out or provide the individual terms in an appendix. -  The paper references \\\"Section 7\\\" (comprehensive analysis) as Section \\\\ref{sec:comprehensive} but the numbering in the LaTeX may not match if figures are added later. Verify cross-references. -  Appendix C on higher-order interactions is interesting (temp x seed x item = 1.8%) but could be expanded. Does this three-way interaction show a benchmark gradient similar to the two-way interactions? 11. Score Score: 4/6 (Weak Accept) This is a well-executed, large-scale empirical study that applies G-theory to multi-benchmark LLM evaluation and discovers a genuine empirical regularity (the cross-benchmark variance gradient). The D-study budgets are practically useful, the experimental scale is impressive, and the paper has improved substantially from earlier drafts -- the bibliography is now adequate, the framing is honest about confirmatory vs. novel contributions, and the robustness checks are thorough. The cross-benchmark gradient as a unifying explanation for contradictory prior findings is the paper's strongest contribution and clears the novelty bar for a top venue. The paper is held back by: (a) zero figures, which is a serious presentation weakness for a variance decomposition paper; (b) the infrastructure crossing being the claimed advance over Mesting yet yielding near-null results; (c) missing metric-conditional analysis despite the title; and (d) scope limitations (7-14B only, no API models, encoder-only fine-tuning). The first issue (figures) is easily fixable and would likely move the paper to a solid accept. The others are structural but not disqualifying. The balance tips toward accept because the cross-benchmark gradient is genuinely novel, the D-study budgets fill a real practical gap, and the \\\"G  < 0.25 everywhere\\\" finding is an important wake-up call for the field. The paper would benefit from another revision addressing the figure deficit and the metric-conditional analysis, but the core contribution is sound. 12. Confidence Confidence: High I am familiar with G-theory (Brennan 2001, Shavelson & Webb 1991), the LLM evaluation reproducibility literature (Sclar, Pezeshkpour, Yuan, Biderman, Mesting), and the IRT/benchmark efficiency literature (Polo, Rodriguez, Perlitz). I have reviewed the full paper text, the related work notes, and the paper framing documents. My main uncertainty is whether models above 14B would substantially alter the gradient pattern -- this is an empirical question the paper cannot answer with its current design.\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd543976ca0b1640e833801bdc\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779306709824\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — worst | dream_20260520T190053]  · Overall: weak reject Dream Review Report — Full Roundtable Paper : \\\"No Universal Reproducibility Recipe: Variance Attribution in LLM Evaluation Is Benchmark-Conditional and Model-Conditional\\\" Review mode : full |  Reviewers : R1 (Methods+Experiments), R2 (Novelty+Related Work) Step 1: Independent Reviews Reviewer 1 — Methods & Experiments Summary : The paper applies G-theory to decompose LLM evaluation variance across 4 models, 5 benchmarks, and 172,800+ inference conditions plus a fine-tuning G-study. The experimental scale is ambitious and the float32 confound discovery is a genuine contribution. However, critical methodological gaps—residual dominance, missing uncertainty quantification, and a blocked hardware experiment—undermine the strength of the claims. Strengths : 1.  Large-scale factorial design : 4 models × 5 benchmarks with multiple crossed facets represents the most comprehensive G-theory study in LLM evaluation to date. The 172,800 MMLU records provide genuine statistical power. 2.  Float32 confound discovery : The identification of vLLM V1/V0 backend routing as a confound that inflated item variance from 24% to 58% is a standalone methodological contribution. The fix (enforce_ eager=True on V0) is immediately actionable. 3.  Honest reporting of failures : The paper transparently reports the blocked hardware experiment (exp-003), partial 14B results, and the confound discovery that invalidated the original hypothesis. This intellectual honesty is commendable. 4.  Fine-tuning G-study is genuinely novel : No prior work has applied G-theory to decompose fine-tuning variance. The finding that learning rate dominates (17.8%) with a 10% lr×seed interaction, and inference-training decorrelation (r=0.15), are new and useful. 5.  D-study projections are practically useful : Showing that optimal allocations diverge qualitatively across benchmarks (MMLU: more items; GSM8K: more seeds) is actionable advice. Weaknesses : 1.  Residual dominance is the paper's Achilles heel  (Tables 1, 3, 5). Residual is the largest component on ALL benchmarks (20–40%). Combined with the opaque \\\"all other\\\" category (26.5% in Table 1), over 54% of MMLU variance is unexplained or aggregated. For a paper whose contribution is variance  attribution , having the majority of variance  unattributed  is a serious problem. The paper does not adequately discuss what these missing sources might be, nor does it attempt higher-order interaction estimation to decompose the residual. 2.  No confidence intervals or uncertainty quantification . Variance component estimates are reported as point estimates without bootstrap CIs, jackknife intervals, or any measure of estimation uncertainty. G-theory provides standard methods for this (Brennan 2001, Ch. 8). Without CIs, we cannot assess whether the differences between benchmarks or models are statistically meaningful or within estimation noise. For example, is item_ id=24% on MMLU vs 22% on ARC a real difference or sampling variability? 3.  Single GPU architecture severely limits \\\"infrastructure\\\" claims . Experiment 3 (multi-hardware) was blocked. The paper's title and framing reference \\\"infrastructure\\\" factors, but only numerical precision on one GPU type was tested. The finding that \\\"direct infrastructure×methodology interaction  < 0.5%\\\" (Table 4) applies only to precision, not hardware broadly. This should be reflected in the title/abstract. 4.  Model is not treated as a G-theory facet . The per-model decompositions (Table 1) show item_ id ranging from 13.8% (Mistral) to 30.2% (Gemma), suggesting strong model×item interaction. But model is analyzed as a stratification variable, not a facet in the G-study design. A model-as-facet reanalysis of the existing MMLU data (no new experiments needed) would properly attribute this variance and likely reduce the residual. 5.  Fine-tuning G-study uses RoBERTa-large  — an encoder-only model from 2019 — on classification tasks. The relevance to modern LLM fine-tuning (decoder-only models, generation tasks, RLHF/DPO) is questionable. The paper acknowledges this in Limitations but the mismatch weakens the \\\"fine-tuning contribution\\\" claim substantially. 6.  200 items per benchmark : While adequate for point estimation, the paper does not report sensitivity analyses (e.g., split-half reliability of the variance decomposition, or bootstrap resampling of items) to establish stability. Different 200-item samples from the same benchmark could yield different decompositions, especially for benchmarks with heterogeneous item pools. 7.  REML vs actual estimation method : The paper states \\\"Variance components are estimated via Restricted Maximum Likelihood (REML)\\\" (Section 3.1) but does not describe the actual implementation. If Henderson Method I (ANOVA-based) was used instead, this is a methodological misrepresentation that matters when variance components are near zero (negative estimates under Henderson are truncated differently than under REML). Questions for Authors : 1.  Can you provide bootstrap CIs (e.g., 1000 resamples of items) for the variance components in Tables 1 and 3? This would address whether cross-benchmark differences are real. 2.  What happens if model is included as a random facet in the MMLU G-study rather than stratified out? How much of \\\"all other\\\" and \\\"residual\\\" is actually model×item interaction? 3.  What specific variance estimation method was implemented? REML, Henderson I, or Henderson III? 4.  Have you examined three-way interactions (e.g., model×prompt×item) that might explain the large residual? Score : 3/6 (Weak Reject)\\n Confidence : 4/5 Reviewer 2 — Novelty & Related Work Summary : The paper extends Mesting [ 2026 ]'s single-benchmark G-theory study to multiple benchmarks and adds a fine-tuning G-study. The central contribution is a negative result (no universal variance structure), which is valid but incrementally novel. The related work section is severely underdeveloped with only 7 references, missing critical prior work on ML reproducibility, IRT-based item analysis, and benchmark efficiency. Strengths : 1.  Cross-benchmark variance gradient is a genuine empirical contribution . Showing that variance structure systematically shifts from item-conditional (MMLU) to seed/temperature-conditional (GSM8K/MATH) as benchmarks move from knowledge retrieval to chain-of-thought reasoning is new and interpretable. 2.  D-study allocation divergence has immediate practical value . The finding that MMLU needs 500 items × 2 prompts × 1 seed while GSM8K needs 250 items × 4 prompts × 4 seeds (Table 7) is directly actionable for benchmark designers. 3.  The confound discovery is a standalone contribution  regardless of the paper's other claims. Documenting that vLLM V0/V1 routing inflates variance estimates warns the community about similar artifacts. 4.  Inference–training decorrelation (r=0.15)  is a novel finding that challenges the assumption that inference-time reproducibility insights transfer to training-time settings. Weaknesses : 1.  Incremental novelty over Mesting [2026] . The paper's claimed advance over Mesting is (a) adding precision as an infrastructure facet and (b) crossing benchmarks. But precision turns out to be a near-null factor ( <1.5% main effect post-fix), so the infrastructure extension yields almost nothing. The paper's strongest findings (benchmark-conditional variance, D-study divergence) would largely emerge from a Mesting-style design without infrastructure crossing. 2.  Severely inadequate bibliography . 7 references for a top-venue submission is far below standards. Critical omissions include:   -  Bouthillier et al. (2021, JMLR) : \\\"Accounting for Variance in Machine Learning Benchmarks\\\" — directly relevant, uses variance decomposition in ML evaluation.   -  Dodge et al. (2020, EMNLP) : Fine-tuning instability — essential context for the fine-tuning G-study.   -  Sellam et al. (2022) : MultiBERTs — multi-seed BERT training, directly relevant to seed variance.   -  Dehghani et al. (2021) : \\\"The Benchmark Lottery\\\" — benchmark selection effects.   -  Polo et al. (2024) : tinyBenchmarks — item subsampling for efficient evaluation, directly relevant to item variance.   -  Rodriguez et al. (2021) : IRT-based evaluation for NLP — alternative item-level analysis framework.   -  Shavelson & Webb (1991) : Foundational G-theory reference beyond Brennan (2001).   -  Henderson et al. (2018) : Deep RL reproducibility — established the multi-factor variance decomposition paradigm in ML.   -  Biderman et al. (2024) : Lessons from evaluation reproducibility.   -  Any ordering effects literature (the paper includes ordering as a facet but cites no prior work on option ordering effects). 3.  \\\"Diagnostic tool\\\" contribution is unsubstantiated . The paper claims G-theory as a \\\"practical diagnostic tool\\\" but releases no software, no analysis pipeline, no reusable framework. The \\\"tool\\\" is just applying G-theory, which Mesting [ 2026 ] already demonstrated. GeneralizIT and similar R packages already exist. Without a released tool, this contribution claim is empty. 4.  The negative result framing needs more work . \\\"No universal recipe\\\" is the central claim, but many practitioners already assume this. The paper confirms a suspicion with data but doesn't offer constructive solutions beyond \\\"diagnose your pipeline\\\" — which requires the very G-theory study the paper just demonstrated is expensive (172,800 conditions for one benchmark). Is the recommendation scalable? 5.  Zero figures is unusual and harmful . For a paper about variance decomposition across benchmarks, visual comparisons (stacked bars, heatmaps, radar charts) would dramatically improve readability. The reliance on 11 tables makes the paper harder to parse and less compelling than it could be. 6.  \\\"Fully crossed\\\" is overstated . Only Experiment 1 (MMLU) uses the full crossing (3 precisions × 6 prompts × 6 seeds × 3 temps × 4 orderings). Experiments 2 and the MATH extension use a reduced crossing (2 precisions × 2 temps). This is fine practically but should not be described as a \\\"fully-crossed design spanning 5 benchmarks\\\" in the abstract. 7.  Item dominance on knowledge benchmarks is partially expected from measurement theory . Items in MMLU span from trivially easy to near-impossible across 57 subjects. A large item variance component is expected given this difficulty range. The paper would benefit from contextualizing this against IRT-based item analysis. Questions for Authors : 1.  How does this work relate to Bouthillier et al. (2021), which also decomposed variance in ML benchmarks? 2.  Is the recommendation to run a full G-study per benchmark practical? What is the computational cost, and is there a lightweight diagnostic alternative? 3.  Why were no figures included? The knowledge-reasoning gradient would be far more compelling as a visualization. 4.  Can you release the analysis code alongside the data to substantiate the \\\"diagnostic tool\\\" claim? Score : 3/6 (Weak Reject)\\n Confidence : 4/5 Step 2: Cross-Sharing R1 → R2 : The methodological concerns (54% unexplained variance, no CIs, model not as facet) mean the \\\"no universal recipe\\\" finding may partly reflect an underspecified decomposition model rather than a genuine property of evaluation variance. If the residual were decomposed further (e.g., via three-way interactions or model-as-facet), the cross-benchmark differences might narrow or change qualitatively. R2 → R1 : The thin related work compounds the experimental concerns. Without positioning against Bouthillier et al., tinyBenchmarks, or IRT-based approaches, it's unclear whether G-theory adds diagnostic power beyond existing methods. The fine-tuning contribution is further weakened because Dodge et al. (2020) already documented seed sensitivity in fine-tuning — the G-theory framing is new but the phenomenon is not. Step 3: Convergence Points of agreement : -  The paper addresses an important problem (evaluation reproducibility diagnosis) -  The float32 confound discovery is a genuine, standalone contribution -  The cross-benchmark variance gradient is an interesting empirical finding -  Residual dominance (largest component everywhere) is the most serious methodological concern -  Missing statistical uncertainty quantification (no CIs) is a critical gap -  Single GPU limits infrastructure claims; the title/abstract overclaim relative to what was tested -  Related work is severely underdeveloped (7 references) -  Zero figures hurts presentation significantly -  Fine-tuning G-study is novel in framing but limited by RoBERTa on classification tasks -  The \\\"diagnostic tool\\\" contribution is claimed but not delivered (no released software) Points of mild disagreement : -  R1 is slightly more positive about the experimental scale and sees the multi-benchmark extension as substantive; R2 views it as more incremental over Mesting -  R2 emphasizes the bibliography gap more; R1 emphasizes the statistical rigor gap more Converged assessment : Both reviewers agree the paper falls below the acceptance threshold for a top ML venue in its current form, despite addressing a real problem with interesting findings. The gap between claims and delivered evidence is too large. Step 4: Consolidated Assessment Overall Score: 3/6 — Weak Reject Headline Assessment An ambitious and honest study that surfaces interesting empirical patterns (benchmark-conditional variance, float32 confound, inference-training decorrelation), but falls short of top-venue standards due to (1) the majority of variance remaining unattributed, (2) no uncertainty quantification on variance estimates, (3) severely thin related work, and (4) overclaiming relative to what was tested (single GPU ≠ \\\"infrastructure\\\"). What Would Change Our Minds (Revision Guidance) Essential (any two would likely move to borderline) : 1.  Bootstrap CIs on all variance components  (Tables 1, 3, 5, 9). This is feasible with existing data and would establish whether cross-benchmark differences are statistically meaningful. 2.  Model-as-facet reanalysis  of MMLU data to properly attribute model×item interaction and reduce the opaque residual/all-other categories. No new experiments needed. 3.  Expand bibliography to ≥25 references , including Bouthillier et al. (2021), Dodge et al. (2020), Sellam et al. (2022), Polo et al. (2024), Rodriguez et al. (2021), Shavelson & Webb (1991), Henderson et al. (2018), and ordering effects literature. Position contributions clearly against each. 4.  Add 3-4 figures : at minimum a stacked bar comparison across benchmarks, and a D-study projection curve. The paper is currently 11 tables and 0 figures. Important (would strengthen but not alone sufficient) :\\n 5. Downscope \\\"infrastructure\\\" claims to \\\"numerical precision\\\" throughout, including title consideration.\\n 6. Release analysis code (not just data) to substantiate the \\\"diagnostic tool\\\" contribution.\\n 7. Discuss what the large residual might contain and whether higher-order interactions or additional facets (e.g., batch size, system prompt) could reduce it.\\n 8. Clarify the exact variance estimation method (REML vs Henderson) and justify the choice. Desirable (for camera-ready) :\\n 9. Fine-tuning extension to at least one decoder-only model on a generation task.\\n 10. Sensitivity analysis: split-half reliability of variance decompositions across different 200-item samples. Contribution Ranking 1.  Float32 confound discovery  — strongest, standalone, immediately actionable ★★★★ 2.  Cross-benchmark variance gradient  — interesting empirical finding, needs CIs ★★★ 3.  D-study allocation divergence  — practically useful, well-presented ★★★ 4.  Inference-training decorrelation  — novel but limited by RoBERTa scope ★★☆ 5.  G-theory as diagnostic tool  — claimed but not delivered (no software) ★★ 6.  \\\"No universal recipe\\\" as central thesis  — valid but not constructive enough ★★ Experiment Coverage Assessment The paper covers 7 of 8 planned experiments (exp-003 blocked, acknowledged). Coverage is thorough. The main gap is not missing experiments but missing  analyses  on existing data (CIs, model-as-facet, higher-order interactions). Venue Fit The paper fits an evaluation/benchmarking track (e.g., NeurIPS Datasets & Benchmarks, COLM, or an EMNLP evaluation workshop). For a main-track top venue, the negative-result framing needs a stronger constructive component (released tool, lightweight diagnostic protocol, or a concrete evaluation standard proposal).\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd54a58a8a0b2863b1f38a3ddc\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779306569451\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — worst | dream_20260520T190053]  · Overall: borderline reject Reviewer R1: Methods and Experiments 1. Summary This paper applies Generalizability Theory (G-theory) to decompose variance in LLM evaluation across infrastructure (numerical precision), methodology (prompt, seed, temperature, ordering), and measurement (item selection) facets. Across 4 models, 5 benchmarks, and 172,800+ records per full-crossing experiment, the authors report that variance attribution is benchmark-conditional and model-conditional: on MMLU item_ id=24% is the largest attributable source after confound correction, while on GSM8K and MATH seed x item and temperature x item interactions dominate. A float32 engine confound in vLLM is identified and corrected. D-study projections show that optimal measurement allocations diverge qualitatively across benchmarks, undermining any universal reproducibility recipe. A fine-tuning extension (RoBERTa-large, 1,728 runs) reveals an inverted variance hierarchy where learning rate (17.8%) and lr x seed interaction (10%) dominate. 2. Strengths 1.  Scale and systematic design.  The fully-crossed factorial on MMLU (4 models x 3 precisions x 6 prompts x 6 seeds x 3 temperatures x 4 orderings x 200 items = 172,800 records) with consistent confound control (V0 enforce_ eager across all precision modes) is a genuinely impressive experimental effort. The extension across 5 benchmarks and 6 models (4x8B + 2x14B) provides breadth rarely seen in evaluation methodology papers. 2.  Float32 engine confound discovery is a standalone contribution.  The identification that vLLM routes float32 to V1 backend versus V0 for BF16/FP16, inflating item variance from 24% to 58% (pre-fix MVP value), is a valuable methodological finding. The before/after comparison (Table 1 vs. MVP) is convincing and has immediate practical implications for any study using vLLM with mixed precision conditions. This finding alone justifies a methods paper. 3.  Honest reframing around negative results.  The title and framing acknowledge that the original hypothesis (item dominance as universal) did not survive cross-benchmark replication. Reporting that item dominance fails on 0/4 benchmarks outside MMLU (Table 4 in cross-benchmark replication) and that variance structure is benchmark-conditional is scientifically responsible. 4.  Benchmark-conditional variance gradient is well-supported.  The systematic pattern across 5 benchmarks -- item_ id declining (MMLU 24% -> GSM8K 12% -> MATH 10%), residual increasing (28% -> 35% -> 40%), temperature x item increasing (5.5% -> 18% -> 15%) -- is a clean empirical finding with a plausible mechanistic account (CoT length amplifies sampling noise, r=0.65). 5.  D-study allocation divergence is practically valuable.  The demonstration that optimal allocation strategies differ qualitatively across benchmarks (MMLU: 500 items x 2 prompts x 1 seed; GSM8K: 250 items x 4 prompts x 4 seeds for a fixed budget of 1000 conditions) is immediately actionable and fills a gap no prior work addresses. 6.  Fine-tuning extension adds genuine novelty.  The first G-theory decomposition of fine-tuning variance with a fully-crossed design (6 seeds x 3 LR x 4 shuffles x 3 GPUs x 2 precisions) reveals learning rate dominance (17.8%) and the lr x seed interaction (10%). The inference-training variance correlation of r=0.15 is a useful negative finding showing that inference-based reproducibility budgets cannot guide training-time decisions. 7.  Generation-based evaluation protocol.  Following Hua et al. (EMNLP 2025) to avoid log-likelihood scoring artifacts that inflate apparent prompt sensitivity reflects careful experimental design awareness. 3. Weaknesses Major (W1) Over 54% of total variance is unexplained or aggregated in the MMLU analysis.  Table 1 shows residual=27.9% and \\\"all other\\\"=26.5%, meaning 54.4% of total variance is either unmodeled or lumped into an opaque category. The \\\"all other\\\" row is not defined -- it presumably aggregates minor two-way interactions and possibly some bookkeeping artifact, but the paper does not specify which components it contains or their individual magnitudes. For a paper whose entire contribution rests on variance attribution, having the majority of variance unattributed is a fundamental problem. The reader cannot assess whether item_ id's 24% is genuinely the \\\"largest attributable source\\\" without knowing what is inside \\\"all other.\\\" If \\\"all other\\\" contains, say, a single three-way interaction at 15%, the variance hierarchy could look quite different. (W2) Model is pooled rather than treated as a G-theory facet.  The paper pools 4 models and decomposes variance across the pooled data, but \\\"model\\\" is not included as a facet in the G-study. In G-theory, model should either be the object of measurement (differentiation facet) or a crossed facet. By pooling, model-level variance and model x item interaction are absorbed into item_ id and residual respectively. The per-model analyses (Table 1 showing Mistral-7B with item=13.8% vs. Gemma-2 with item=30.2%) demonstrate that model x item interaction is substantial, yet this is never estimated as a separate variance component. The Mistral anomaly (residual=38.2%) likely reflects model x higher-order interactions being dumped into residual. This design choice fundamentally undermines the headline variance decomposition. A proper model-as-facet analysis would separate model x item interaction and almost certainly reduce item_ id's attributed share further while revealing how much of the \\\"residual\\\" is actually structured model x condition interaction. (W3) ANOVA-based estimation is used but the paper's methodological framing implies REML.  The code ( variance_decomposition.py ) implements classical ANOVA-based Henderson Method I estimation: it computes Type-I sums of squares, derives mean squares, and solves Expected Mean Square equations for variance components. Negative estimates are truncated to zero. This is not REML. REML uses restricted maximum likelihood via iterative optimization (e.g., Fisher scoring, EM) and handles boundary constraints differently (constrained optimization rather than truncation). The distilled research skill cites Mesting (2026) as using \\\"REML + D-study\\\" and positions this work as methodologically comparable. If the paper claims or implies REML while implementing ANOVA-based estimation, this is a misrepresentation that a psychometrics-aware reviewer would catch immediately. The two methods can yield different results, especially with unbalanced cells or when negative variance components arise (the truncation-to-zero approach inflates other components' relative shares). (W4) Bootstrap CIs are structurally incomplete across experiments.  The code computes bootstrap CIs for all components on MMLU (exp-001), but the paper summary provides CIs only selectively. For the cross-benchmark experiments (exp-002), the 14B extension (exp-005), and the fine-tuning study (exp-006), no confidence intervals are reported. This is especially problematic for: (a) the separability claim, where \\\"direct infra x method < 0.5%\\\" needs a CI to be interpretable -- is the CI [ 0.0%, 3.0%] or [ 0.3%, 0.7%]?; (b) the cross-benchmark gradient, where overlapping CIs on item_ id shares across benchmarks would weaken the \\\"qualitatively different\\\" claim; (c) the fine-tuning lr dominance claim (17.8%), where the CI width determines whether lr is statistically distinguishable from item_ id (13.8%). Without CIs on all reported variance components, the paper is presenting point estimates as if they were precise measurements. (W5) Experiment 3 (multi-hardware) is blocked, fatally weakening the separability claim.  The paper claims to test \\\"infrastructure vs. methodology separability\\\" but the only infrastructure facet actually crossed is numerical precision. Without a second GPU type, the paper cannot distinguish hardware-specific from hardware-universal variance. The separability claim must be scoped to \\\"precision vs. methodology\\\" rather than \\\"infrastructure vs. methodology.\\\" This is not merely a limitation -- it undermines the paper's positioning relative to its stated contribution of being the \\\"first fully-crossed G-theory study spanning infrastructure x methodology.\\\" With only precision as the infrastructure proxy, the study is methodologically closer to Mesting (2026) than advertised, differing primarily in adding precision as a facet rather than adding \\\"infrastructure\\\" broadly. Moderate (W6) Experiment 5 (14B) has no hardware crossing and only 2 models, making scale claims unreliable.  With n=2 (Qwen3-14B and DeepSeek-R1-Distill-14B), the 14B extension cannot separate model scale from architecture effects. DeepSeek-R1-Distill-14B is a reasoning-distilled model with fundamentally different generation characteristics (item=10%, residual=42%), making it an inappropriate comparison partner for studying \\\"scale effects.\\\" The paper acknowledges this but still draws conclusions about scale invariance/variance that are confounded with architecture. (W7) Temperature and precision levels differ across experiments without justification.  Exp-001 uses 3 precisions x 3 temperatures x 4 orderings on MMLU. Exp-002 uses 2 precisions x 2 temperatures on GSM8K/ARC/HellaSwag. This means the cross-benchmark comparison in Tables 3-4 is confounded with design differences: the reduced crossing on non-MMLU benchmarks means fewer levels of temperature and precision, which mechanically reduces their estimated variance shares. A fair cross-benchmark comparison requires identical factorial designs. The paper does not discuss how design asymmetry affects the comparability of variance component estimates. (W8) All three-way and higher interactions are absorbed into the residual.  With 6 facets, there are 20 three-way interactions, 15 four-way, 6 five-way, and 1 six-way -- 42 higher-order terms total, all dumped into \\\"residual.\\\" The residual ranges from 20-40% across experiments. Some of this is likely structured: for instance, precision x temperature x item is plausible given that both precision x item (3.5%) and temperature x item (5.5%) are non-trivial on MMLU. If even one three-way interaction accounts for 5-8% of total variance, the relative ranking of two-way components would shift. The paper neither estimates selected three-way interactions nor discusses this confound in the residual. (W9) D-study projections assume items are sampled from an infinite universe.  The G-theory D-study formula G = sigma_ tau / (sigma_ tau + sigma_ delta/n) assumes random sampling from an infinite item universe. Benchmark items are curated, finite collections. For MATH (G=0.30, recommending 2200 items for G>=0.90 when only 5000 items exist in the full benchmark), the extrapolation is questionable. For GSM8K (recommending 1400 items), similar concerns apply. The paper acknowledges infeasibility but does not discuss the statistical invalidity of extrapolating finite-population variance components to hypothetical infinite-population D-study projections. (W10) Fine-tuning experiment uses RoBERTa-large (355M, encoder-only) rather than a decoder-only model.  The architectural mismatch between the inference experiments (7-14B decoder-only autoregressive models) and the fine-tuning experiment (encoder-only classification model) weakens cross-paradigm generalization claims. Fine-tuning a decoder model (e.g., Llama-3.1-8B with LoRA on a generation task) would make the inference-vs-fine-tuning variance hierarchy comparison far more credible. As designed, the fine-tuning experiment measures a fundamentally different computational process (classification head fine-tuning vs. autoregressive generation), making the r=0.15 correlation between inference and training variance structures potentially an artifact of architectural mismatch rather than a deep insight about variance structure differences. Minor (W11) The Kruskal-Wallis test (H=47.3, p<0.001) is underspecified.  What is being compared? Per-item variance contributions across benchmarks? With k=5 benchmarks and point estimates derived from different experimental designs (different numbers of levels), the test's assumptions (independent samples from the same distribution family) may not hold. The degrees of freedom and sample sizes per group are not reported. (W12) No multiple comparison correction.  Multiple bootstrap CIs and permutation tests are computed without family-wise error rate correction (Bonferroni, Holm, or FDR). With 11+ variance components per experiment and 7+ experiments, the number of implicit hypothesis tests is substantial. (W13) The \\\"all other\\\" category in Table 1 (26.5%) is not decomposed.  This catch-all category is almost as large as residual (27.9%) and larger than item_ id (24.0%). Presenting an aggregated \\\"all other\\\" without itemizing its constituents is unusual for a variance decomposition paper and prevents readers from understanding the full variance structure. 4. Questions for Authors 1.  Why is \\\"model\\\" not included as a facet in the G-study? The per-model results (Table 1) show item_ id ranges from 13.8% (Mistral) to 30.2% (Gemma-2) -- this 16.4pp range suggests substantial model x item interaction. If model were a facet, how much of the current item_ id and residual estimates would be reclassified as model x item interaction? 2.  What exactly is in the \\\"all other\\\" category (26.5% in Table 1)? Please enumerate all components and their individual estimates. Is this a sum of small two-way interactions, or does it include terms that individually exceed 5%? 3.  The code ( variance_decomposition.py ) uses ANOVA-based Henderson Method I estimation with truncation of negative variance components to zero. Does the paper describe this correctly, or does it claim REML? If ANOVA-based, have you verified exact balance (every cell has the same number of observations) across all experiments? 4.  Why do the factorial designs differ between MMLU (3 precisions, 3 temperatures) and the other benchmarks (2 precisions, 2 temperatures)? How does this design asymmetry affect the comparability of cross-benchmark variance component estimates? 5.  Can you provide bootstrap CIs for the total direct infrastructure x methodology interaction on each benchmark? The 0.5% point estimate for separability requires uncertainty quantification. 6.  The D-study recommends 2200 items for MATH to reach G>=0.90, but MATH has only 5000 items total. At what point does the finite-population assumption break the D-study framework? Have you considered finite-population corrections? 7.  Have you tested any three-way interactions (e.g., precision x temperature x item, prompt x seed x item)? Given residual accounts for 28-40% across experiments, some of this may be structured and recoverable. 8.  For the fine-tuning experiment, why was RoBERTa-large chosen instead of fine-tuning one of the same decoder-only models used in the inference experiments (e.g., Llama-3.1-8B with LoRA)? How confident are you that the r=0.15 inference-training correlation reflects a genuine structural difference rather than an architectural mismatch artifact? 9.  The inference-training variance correlation (r=0.15) is computed between what exactly? Variance component shares? G coefficients? Per-item accuracy variance? The operationalization is unclear. 10.  Mistral-7B shows a qualitatively different variance profile (item=13.8%, residual=38.2%) compared to the other three 8B models. Is this anomaly investigated? Could it indicate that the G-theory facet structure is model-inappropriate for certain architectures? 5. Missing Experiments or Analyses 1.  Model as a crossed facet.  Re-analyze the MMLU data with model as a 7th facet (or as the object of measurement). This requires no new data collection and would resolve the most fundamental methodological concern. 2.  Three-way interaction estimation.  Fit at least the theoretically motivated three-way interactions (precision x temperature x item, prompt x seed x item, prompt x temperature x item) to determine how much of the residual is structured. This also requires no new data. 3.  Dual-metric analysis.  Decision D002 describes radically different variance structures for binary correct (item_ id=58.4%) vs. text exact match (prompt x item=37.5%). This analysis appears to have been planned but dropped. Including it would demonstrate metric sensitivity, which strengthens the \\\"no universal recipe\\\" argument. 4.  Sensitivity analysis for the separability threshold.  Rather than a binary pass/fail at 0.5%, report the full bootstrap distribution of total direct infrastructure x methodology interaction and let readers judge. 5.  ANOVA vs. REML comparison.  Run the same data through a proper REML implementation (e.g., lme4 in R, or statsmodels MixedLM in Python) and compare results. This validates or invalidates the ANOVA-based approach and is a single-afternoon analysis task. 6.  Finite-population correction for D-study.  For benchmarks with small item pools (MATH: 5000, ARC: ~ 2590), apply finite-population corrections to the D-study projections and report adjusted G coefficients. 7.  Decoder-only fine-tuning comparison.  Even a small-scale LoRA fine-tuning experiment with Llama-3.1-8B on one task would dramatically strengthen the inference-vs-fine-tuning comparison. 6. Score Score: 3/6 (Weak Reject) The paper presents substantial experimental effort and several genuine contributions (engine confound discovery, benchmark-conditional variance gradient, D-study allocation divergence). However, the methodological execution has fundamental gaps: (1) over 54% of variance is unexplained or aggregated into opaque categories; (2) model is pooled rather than treated as a facet, confounding the core variance decomposition; (3) the estimation method may be misrepresented; (4) the blocked hardware experiment undermines the central \\\"infrastructure vs. methodology\\\" framing; (5) cross-benchmark comparisons use non-identical factorial designs. These are not cosmetic issues -- they affect the validity of all three central claims. The contributions that survive scrutiny (confound fix, benchmark gradient, fine-tuning decomposition) are individually interesting but do not cohere into a unified paper at the current level of methodological rigor. Most concerns are addressable without new experiments (model-as-facet reanalysis, three-way interactions, dual-metric analysis, proper CIs), but the revision scope is substantial. 7. Confidence Confidence: 4/5 (High) I have expertise in experimental design, variance decomposition methods, and G-theory applications. I verified claims against the actual analysis code ( variance_decomposition.py ,  d_study.py ) and cross-referenced the experimental plan against reported results. My main uncertainty is whether the paper text (which I reviewed via summary rather than the full manuscript) accurately represents the estimation method -- the ANOVA-vs-REML concern is based on the code, which is definitive, but the paper's textual claims may differ from what I infer.\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd54aac68a0b2e69f7086a2442\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779306566236\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — best | dream_20260520T190053]  · Overall: weak reject dream_ id: dream_ 20260520T190053\\n tier: best\\n reviewer: R2\\n focus: Novelty and Related Work\\n timestamp: 2026-05-20T20:15:00+00:00 Reviewer R2: Novelty and Related Work 1. Summary This paper applies Generalizability Theory (G-theory) to LLM evaluation, crossing infrastructure facets (hardware, numerical precision) with methodology facets (prompt, seed, temperature, ordering) and item selection as the measurement facet. Across 6 models, 5 benchmarks, and 2M+ evaluation records, it finds that item selection dominates variance (42--58%), infrastructure--methodology interactions are negligible (<0.5%), and current evaluation practices yield G  < 0.40. D-study projections provide reproducibility budgets, and a fine-tuning extension shows an inverted variance hierarchy. A vLLM engine confound (FP32 using a different backend) is identified and corrected. 2. Strengths 1.  The cross-benchmark variance gradient is a genuine empirical contribution.  Showing that item dominance systematically weakens from 58.4% (MMLU) to 42.1% (MATH) as task difficulty and reasoning demands increase, with temperature x item and seed x item interactions correspondingly increasing, is a well-supported quantitative finding. This gradient was intuited but never measured across this many benchmarks in a unified framework. It explains why prior single-benchmark studies reached apparently contradictory conclusions. 2.  The two-level separability decomposition is more nuanced than a binary answer.  Distinguishing aggregate-level separability ( <0.5% direct interaction) from item-conditional interactions (14.2% combined) is a mature analytical move. The \\\"empirical license with caveats\\\" framing -- isolated-factor studies are valid on average but their conclusions are item-conditional -- is the right level of nuance and provides a useful guideline for future work. 3.  D-study reproducibility budgets fill a genuine practical gap.  Translating variance components into concrete recommendations (600 items, 3 prompts, 2 seeds for G >= 0.90 on MMLU; different budgets for other benchmarks) is immediately actionable. The cross-benchmark budget table showing that HellaSwag needs 550 items while MATH needs 1,100 is the kind of task-specific guidance the field lacks. 4.  The engine confound discovery is a standalone methodological contribution.  Identifying that vLLM routes FP32 through a different execution backend (V1 vs V0), inflating precision variance from 0.3% to 7.24% and creating an 8.5pp accuracy gap, is genuinely valuable to any researcher comparing precision modes. The before/after validation is convincing. 5.  The fine-tuning extension adds structural insight.  Demonstrating that the variance hierarchy inverts in fine-tuning (learning rate and seed dominate over items, explaining the \\\"5 seeds, report mean +/- std\\\" convention) is a non-trivial contribution that connects inference and training reproducibility. 6.  Experimental scale is impressive.  7 experiments, 2M+ records, 6 models (7B--14B), 5 benchmarks spanning MC knowledge to multi-step reasoning, plus a fine-tuning scenario. Few empirical papers in this area match the breadth. 3. Weaknesses Major (W1) Incremental novelty over Mesting (2026).  The paper's stated methodological advance over Mesting is the addition of infrastructure facets (hardware, precision) to the G-theory design. But these infrastructure facets contribute negligibly: hardware main effect 1.2% (in Exp 3), precision 0.3%, direct infrastructure x methodology interactions  <0.5%. The paper's strongest findings -- item dominance, the benchmark-dependent variance gradient, D-study budgets, the task-difficulty modulation -- would emerge from a Mesting-style design with fixed infrastructure. The infrastructure extension is effectively a confirmatory null result: infrastructure does not interact with methodology. This is useful information, but it is a confirmation, not a discovery. The paper frames the infrastructure crossing as the primary novelty (\\\"first fully-crossed G-theory study spanning infrastructure and methodology\\\"), yet the results demonstrate that crossing infrastructure was unnecessary for arriving at the main conclusions. The actual novelty lies elsewhere (cross-benchmark gradient, D-study budgets, engine confound), and the paper needs to honestly acknowledge that. (W2) Severely inadequate bibliography.  Seven references is far below the standard for a top-venue submission on evaluation methodology. Critical omissions include: -  Bouthillier et al. (2021, JMLR), \\\"Accounting for Variance in Machine Learning Benchmarks.\\\"  This is the closest ML-native predecessor: it decomposes benchmark variance via ANOVA across hyperparameters, data splits, initialization seeds, and implementation choices. Not citing it inflates the paper's apparent novelty -- the idea of factorial variance decomposition for ML evaluation is not new, and Bouthillier et al. established the template. The paper's claim of being the \\\"first\\\" to decompose variance across multiple factors needs qualification. -  IRT-based item analysis in NLP.  Lalor et al. (2019, NAACL), Rodriguez et al. (2021, ACL), and Vania et al. (2021) have studied item-level properties in NLP benchmarks using Item Response Theory. The paper claims item selection is an overlooked variance source, but IRT researchers have been analyzing item difficulty, discrimination, and selection effects for years. The item dominance finding should be contextualized against this existing body of work. -  Benchmark subsampling literature.  Polo et al. (2024, \\\"tinyBenchmarks\\\"), HELM-Lite, and Perlitz et al. (2023, \\\"Efficient Benchmarking of LLMs\\\") address the same practical question -- how many items suffice for reliable evaluation? -- from a different methodological angle (IRT-based subsampling vs. G-theory D-study). The D-study recommendations should be directly compared against these approaches. -  Henderson et al. (2018), \\\"Deep Reinforcement Learning that Matters.\\\"  A pioneering study on variance sources in ML evaluation (hyperparameters, implementations, environments, seeds). Foundational for the \\\"variance in evaluation\\\" literature that this paper belongs to. -  Shavelson & Webb (1991), \\\"Generalizability Theory: A Primer.\\\"  A canonical G-theory reference. The paper cites only Cronbach et al. (1972) for G-theory foundations, but the Shavelson & Webb primer and the full Brennan (2001) textbook are standard citations in any G-theory paper. The Brennan textbook appears in the task summary but not in the \\\"best\\\" paper's bibliography. -  Lu et al. (2022) and Pezeshkpour & Hruschka (2024) on option ordering effects.  Directly relevant to the ordering facet. The paper includes ordering as a facet but does not cite any prior work on ordering sensitivity. -  Dodge et al. (2020, \\\"Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping.\\\"  Directly relevant to the fine-tuning G-study (Exp 6), which examines seed and data shuffle variance. With only 7 references, the paper creates a misleading impression of operating in a vacuum. Expanding to 25+ references with proper contextualization is essential. (W3) Item dominance is partially expected from measurement theory -- the framing oversells it.  Any assessment instrument with a wide difficulty range will show item variance as the dominant source. This is a well-established property in psychometrics (Brennan, 2001, Chapter 3; Shavelson & Webb, 1991). MMLU spans trivial factual recall to expert-level reasoning; GSM8K spans single-step arithmetic to multi-step word problems. The paper's hook -- \\\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs\\\" -- oversells a finding that is, from a measurement theory perspective, expected. The contribution is in (a) quantifying the magnitude and (b) showing its benchmark-dependence, but the paper should acknowledge: \\\"Item dominance is expected from measurement theory when item difficulty varies widely; our contribution is in quantifying its magnitude (42--58%), demonstrating its systematic variation with task reasoning demands, and deriving D-study implications specific to LLM evaluation.\\\" (W4) The \\\"diagnostic tool\\\" contribution is not substantiated.  Contribution 1 claims G-theory as a \\\"practical diagnostic tool for evaluation pipeline designers\\\" and mentions releasing 172,800+ records. But no software tool, library, or interactive diagnostic is provided. The \\\"tool\\\" is simply running G-theory analysis on evaluation data, which Mesting (2026) and GeneralizIT (2024) already provide. The paper contributes data and analysis, not a tool. Either substantiate the tool claim (e.g., release a pipeline that takes raw evaluation logs and produces variance decompositions + D-study recommendations) or reframe the contribution as \\\"empirical analysis\\\" rather than \\\"diagnostic tool.\\\" Moderate (W5) The fine-tuning extension uses RoBERTa-large (355M, encoder-only, classification), which is architecturally distant from the 7--14B decoder-only autoregressive models in the inference experiments.  The claim that \\\"these findings extend to fine-tuning settings\\\" implies generalization across paradigms, but fine-tuning RoBERTa on SST-2 is a fundamentally different operation than fine-tuning Llama-8B with LoRA on a generation task. The variance hierarchy inversion (LR and seed dominating) may be specific to small encoder-only models on classification tasks with high baseline accuracy. Fine-tuning a decoder model would make the cross-paradigm claim far more credible. At minimum, the paper should explicitly qualify: \\\"Our fine-tuning analysis is limited to encoder-only models on classification tasks and may not generalize to decoder-only fine-tuning.\\\" (W6) The \\\"fully crossed\\\" claim is overstated.  Only MMLU Exp 1 has the richest factorial design (4 models x 3 precisions x 6 prompts x 6 seeds x 3 temperatures x 4 orderings x 200 items). Other benchmarks use reduced designs (Exp 2: 2 precisions, 2 temperatures). The hardware experiment (Exp 3) uses only 2 GPU types with partial crossing (2/4 models on both). The paper's title and abstract claim a \\\"fully-crossed\\\" study, but only one of seven experiments is fully crossed. The other experiments are partially crossed replications with reduced designs, which is fine methodologically but should be honestly described. (W7) Zero figures is a serious presentation weakness for a paper about variance decomposition.  The distilled writing patterns from the field identify stacked-bar variance decomposition charts and D-study projection curves as expected idioms in this literature (Mesting 2026, Brittlebench 2026 both use them). With 11 tables and 0 figures, the paper buries its most visually compelling findings -- the cross-benchmark variance gradient, the D-study cost-effectiveness curves, the before/after engine confound comparison -- in dense tabular format. A stacked-bar chart showing variance components across 5 benchmarks would communicate the benchmark-dependency finding far more effectively than Tables 3--4. D-study projection curves showing G vs. item count for different benchmarks would make the budget recommendations intuitive. This is not cosmetic: at a competitive venue, reviewers have limited time, and visual communication of the key findings would substantially strengthen the paper's impact. (W8) The paper does not adequately address the relationship between its findings and the paper summary title claim.  The paper summary states the central finding is that \\\"variance attribution patterns are benchmark-conditional and model-conditional -- no universal reproducibility recipe exists.\\\" This negative result framing is potentially powerful, but the paper itself leans more toward positive claims (\\\"item selection dominates,\\\" \\\"separability holds,\\\" \\\"here are budgets\\\"). The tension between these two framings is unresolved. If the central message is \\\"no universal recipe,\\\" the paper should lead with how different benchmarks and models require different remediation strategies. If the central message is \\\"item selection dominates,\\\" the paper should explain why this holds despite the benchmark gradient. The current framing tries to claim both simultaneously, which weakens both. Minor (W9)  The inference-fine-tuning correlation of r=0.15 (mentioned in the task summary) is never discussed in the paper text. If this is an actual finding, it reinforces the \\\"no universal recipe\\\" message and deserves discussion. If it was not computed, it should be. (W10)  The paper uses \\\"first\\\" language extensively (\\\"first fully-crossed G-theory study,\\\" \\\"first empirical evidence,\\\" \\\"first formal test of separability\\\"). Priority claims require thorough literature review to sustain, and with only 7 references, these claims are vulnerable. 4. Missing Related Work The following lines of work should be discussed: 5. Questions for Authors 1.  How do your D-study item budget recommendations compare to IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite)? These methods also answer \\\"how many items suffice?\\\" -- what does G-theory add beyond what IRT already provides? 2.  The infrastructure extension is the claimed methodological advance over Mesting (2026), but infrastructure contributes  <1% of variance. If you ran the same study with fixed infrastructure (single GPU, single precision), which of your three contributions would change? Please be specific. 3.  You claim G-theory as a \\\"diagnostic tool\\\" (Contribution 1), but no software or pipeline is released. What exactly is the tool? Is it the G-theory framework itself (which Mesting already applied), the data release, or something else? 4.  Item dominance (42--58%) is expected from psychometric theory when item difficulty varies widely. How do you respond to the concern that this finding is partially tautological? What would it mean for item dominance  not  to hold -- would that indicate a problem with the assessment, the analysis, or the theory? 5.  The fine-tuning experiment uses RoBERTa-large on classification tasks. Would you expect the same inverted variance hierarchy if fine-tuning a 7B decoder model on a generation task (e.g., Llama-8B with LoRA on GSM8K)? What is your basis for generalizing across architectures? 6.  Your literature map includes 10 papers (Bui 2025, \\\"Same Prompt Different Outcomes\\\" 2026, GeneralizIT 2024, etc.), but the paper cites only 7. Why were the other 3 dropped? More critically, why are there no citations to the IRT item analysis literature, the benchmark subsampling literature, or the ML variance decomposition literature (Bouthillier et al., Henderson et al.)? 7.  The paper has zero figures. The distilled writing patterns from your own field analysis identify stacked-bar charts and D-study curves as expected idioms. Was this a deliberate choice? What would a Figure 1 (variance decomposition across benchmarks) add to the narrative? 6. Score Score: 3/6 (Weak Reject) The paper presents a large-scale empirical study with genuine practical value (D-study budgets, engine confound fix, cross-benchmark gradient). However, the novelty claim rests on infrastructure crossing that yields near-null results ( <0.5% variance), the bibliography is severely inadequate (7 references, missing entire lines of relevant work), the item dominance finding is partially expected from measurement theory but oversold, and the \\\"diagnostic tool\\\" contribution is unsubstantiated. The actual novelty -- cross-benchmark variance gradient, task-specific budgets, confound identification -- is real but needs honest reframing and thorough contextualization against related work that currently goes unacknowledged. 7. Confidence Confidence: 4/5 I am familiar with the G-theory literature, the LLM evaluation reproducibility literature, and the IRT/benchmark subsampling work. My main uncertainty is whether the full Bouthillier et al. (2021) framework is sufficiently different in scope that the \\\"first\\\" claims could be partially defended, and whether there are very recent (2026) papers in this space that I have not seen.\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd4a09b68a4b26d494054571fb\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779306213563\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — median | dream_20260520T190053]  · Overall: borderline reject Dream Review Report Paper:  Benchmark-Dependent Variance Structure in LLM Evaluation: A Generalizability Theory Analysis of Infrastructure and Methodological Reproducibility Review mode:  full |  Reviewers:  R1 (Methods + Experiments), R2 (Novelty + Related Work) 1. Paper Summary This paper applies Generalizability Theory (G-theory) to LLM evaluation, crossing infrastructure facets (hardware type, numerical precision) with methodology facets (prompt template, random seed, sampling temperature, option ordering) and item selection as the measurement facet. Across 6 models (4×8B, 2×14B), 5 benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), and over 1 million evaluation records, the paper reports three findings: (1) item selection is the single largest variance source on MC benchmarks (30–46%) but its dominance is benchmark-dependent, weakening on reasoning tasks; (2) infrastructure and methodology are approximately separable at the aggregate level (direct interaction  <1%); (3) D-study projections yield task-specific reproducibility budgets (380–950 items for G≥0.90). A fine-tuning extension with RoBERTa-large shows the variance hierarchy inverts (LR and seed dominate). Eight experiments are presented across 13 pages with 15 tables and zero figures. 2. Roundtable: Independent Assessments R1 — Methods and Experiments (Score: 4/6, Borderline Reject) Strengths: -  Massive fully-crossed factorial design on MMLU (1,036,800 records) with systematic confound control (enforce_ eager fix reducing the FP32 accuracy gap from 8.5pp to  <1pp) -  Cross-benchmark extension (Exp 2–3) revealing the variance gradient from item-dominated (HellaSwag 45%) to residual/interaction-dominated (MATH 30% residual) is methodologically sound -  D-study projections with bootstrap CIs ([ 420, 680 ] for MMLU) provide genuine uncertainty quantification on a policy-relevant number -  Fine-tuning extension adds conceptual value by demonstrating the inverted variance hierarchy -  Statistical toolkit is appropriate: REML, bootstrap, Kruskal-Wallis, permutation tests Major weaknesses: 1.  Model pooled rather than treated as a crossed random facet.  In G-theory, model (the object of measurement) should be treated as a facet. By pooling, model×item interactions get absorbed into the item_ id component, inflating the headline 43% figure. The Gemma-2 sensitivity analysis (removing it raises pooled item_ id to 46%) hints at this, but a proper model-as-facet analysis would separate model×item interaction and likely reduce item_ id's share. This is a fundamental design choice that weakens the central claim. 2.  Bootstrap CIs reported only for item_id in Table 1 ([38%, 48%]).  All other variance components in all tables lack uncertainty intervals. For a paper whose core claim rests on the relative magnitude of variance components, this is a serious gap — particularly for the separability claim (is 0.3% direct Infra×Method significantly different from 0?). 3.  Arbitrary separability threshold.  The 1% threshold for \\\"approximate separability\\\" is not derived from G-theory or psychometric literature. The observed value (0.3–0.5%) lands comfortably below this threshold, but no sensitivity analysis examines what changes at 0.25% or 2%. A bootstrap CI on total direct interaction would be more informative than a pass/fail test. 4.  D-study extrapolation beyond item universe.  MATH has 500 total items; the D-study recommends 950 items for G≥0.90. The paper notes this makes reliable evaluation \\\"effectively unattainable,\\\" which is fair, but the D-study formula assumes sampling from an infinite item universe. When the recommendation exceeds the actual item pool, the projection's validity breaks down — this limitation is acknowledged but under-discussed. Moderate weaknesses: -  Only 2 GPU types with partial crossing (2/4 models fully crossed on hardware); 1 df for hardware main effect makes the separability test directional at best -  Temperature levels differ across experiments (3 levels in Exp 1, 2 in Exp 2) without clear justification -  All 3-way and higher interactions absorbed into residual (14.2–21% depending on experiment) without discussion of which higher-order terms might be substantively meaningful -  Binary accuracy metric on MC tasks inflates item variance (items near 0 or 1 contribute little variation); log-likelihood or calibration-based metrics could yield different decompositions -  Fine-tuning experiment uses only 2 precisions and 3 GPUs but claims to test separability generalization — this is a weaker test than the inference experiments R2 — Novelty and Related Work (Score: 3/6, Weak Reject) Strengths: -  The benchmark-dependent variance gradient (item_ id declining from 45% on HellaSwag to 22% on MATH, with temperature×item and seed×item rising correspondingly) is a genuine quantitative contribution — it quantifies an intuition the field has had but never measured systematically -  The two-level separability decomposition (aggregate  <1% vs. item-conditional 14–18%) is more informative than a binary answer and the \\\"empirical license with caveats\\\" framing is mature -  D-study budgets with cross-benchmark variation (380 items for HellaSwag vs. 950 for MATH) are immediately actionable for practitioners -  The engine confound discovery (enforce_ eager fix) is a standalone methodological contribution -  The fine-tuning contrast (LR+seed dominate, explaining the \\\"5 seeds\\\" convention) adds structural insight Major weaknesses: 1.  Incremental novelty over Mesting (2026).  The core methodological contribution is extending Mesting's G-theory framework by adding infrastructure facets. But these infrastructure facets contribute negligibly (hardware 1.2%, precision 0.8%, direct Infra×Method 0.3–0.5%). The paper's most impactful findings — item dominance, benchmark-dependent variance gradient, D-study budgets — would emerge from a Mesting-style design with fixed infrastructure. The \\\"first fully-crossed\\\" claim is technically true but the marginal value of crossing infrastructure with methodology is a confirmatory null result, not a breakthrough. The paper needs to reframe: the infrastructure extension is valuable as a confirmatory finding; the actual novelty is in the cross-benchmark gradient, D-study budgets, and confound fix. 2.  Severely deficient bibliography.  Only 9 references for a 13-page top-venue submission. Critical omissions include:   -  Bouthillier et al. (2021, JMLR), \\\"Accounting for Variance in Machine Learning Benchmarks\\\"  — the closest ML-native predecessor, decomposing variance via ANOVA across hyperparameters, data splits, and seeds. Not citing it inflates the paper's apparent novelty.   -  IRT-based item analysis in NLP:  Lalor et al. (2019, NAACL), Rodriguez et al. (2021, ACL), Vania et al. (2021) — directly relevant to the item dominance finding. The paper claims item selection is under-studied, but IRT has been analyzing item-level properties for years.   -  Benchmark subsampling literature:  Polo et al. (2024, \\\"tinyBenchmarks\\\"), HELM-Lite, Perlitz et al. (2023) address the same practical question (how many items suffice?) from different angles. The D-study budgets should be contextualized against these.   -  Henderson et al. (2018), \\\"Deep Reinforcement Learning that Matters\\\"  — pioneering work on variance in ML evaluation.   -  Shavelson & Webb (1991)  and full Brennan (2001) textbook — canonical G-theory references that a G-theory paper must cite.   -  Lu et al. (2022)  — ordering effects in MC evaluation, relevant to the ordering facet. 3.  Item dominance is partially tautological.  Any assessment instrument with a wide difficulty range will show item variance as the dominant source — this is a well-known property in psychometrics (Brennan, 2001, Ch. 3). The paper's framing (\\\"researchers are optimizing the wrong knobs\\\") oversells a finding that is expected from measurement theory. The contribution is in quantifying the magnitude and its benchmark-dependence, but the paper should acknowledge: \\\"Item dominance is expected from measurement theory; what we contribute is its precise magnitude, systematic variation with task reasoning demands, and D-study implications.\\\" Moderate weaknesses: -  Fine-tuning extension uses RoBERTa-large (355M, encoder-only, classification) — architecturally distant from the 7–14B decoder-only models in inference experiments. Fine-tuning a decoder model (e.g., Llama-8B with LoRA on a generation task) would make cross-paradigm generalization claims far more credible. -  The \\\"fully crossed\\\" claim is overstated: only MMLU Exp 1 has the richest factorial design. Other benchmarks use reduced designs (2 precisions, 2 temperatures). Hardware crossing is partial (2/4 models). Cross-benchmark separability claims rest on narrower evidence than the framing suggests. -  No figures at all — highly unusual for a top venue paper. D-study projection curves, stacked-bar variance decompositions, and the benchmark gradient would dramatically improve communication. The paper's 15 tables contain rich data that is hard to absorb in tabular form. 3. Roundtable: Cross-Sharing and Convergence Areas of Agreement (both reviewers) 1.  Model-as-facet treatment is the most fundamental methodological concern.  R1 identified it as a G-theory design flaw; R2 flagged it as inflating the headline item_ id number. Both agree that a proper model-as-facet analysis would likely reduce item_ id below 43% and reveal model×item interaction as a substantial component. This directly affects Claim 1. 2.  The separability threshold is arbitrary and the test under-powered.  Both reviewers independently flagged the 1% threshold as unjustified and the hardware crossing as insufficient (2 GPU types, partial). The separability claim is directional evidence, not proof. 3.  D-study budgets are the most actionable contribution.  Both reviewers rate the concrete, benchmark-specific reproducibility budgets as filling a genuine practical gap. The bootstrap CIs on MMLU items ([ 420, 680 ]) demonstrate honest uncertainty quantification (though CIs are needed for other benchmarks too). 4.  The cross-benchmark variance gradient is a genuine empirical contribution.  Both agree the systematic relationship between task reasoning demands and variance structure (item dominance weakening, temperature/seed interactions strengthening) is informative and well-supported by data across 5 benchmarks. 5.  The bibliography is far below top-venue standards.  R2 provided detailed missing references; R1 implicitly relied on broader knowledge that confirms these gaps. Areas of Divergence -  Severity of novelty concern:  R2 weights the incremental novelty over Mesting more heavily (infrastructure extension is a near-null result) → 3/6. R1 is more willing to credit the experimental scale and scope → 4/6. -  Statistical vs. conceptual critique:  R1 focuses on the technical execution (CI coverage, REML specification, residual interpretation). R2 focuses on positioning and framing (overselling item dominance, missing related work, tautological aspects). -  Fine-tuning extension value:  R1 accepts it as an interesting conceptual addition. R2 considers the architectural mismatch (RoBERTa vs. decoder-only) a moderate weakness that undermines cross-paradigm claims. Convergence After cross-sharing, both reviewers converge on: the paper presents a substantial empirical effort with real practical value, but the current version has (a) a fundamental G-theory design issue (model treatment), (b) severely inadequate related work, (c) framing that oversells the infrastructure contribution and item dominance finding, and (d) missing uncertainty quantification across most results. These issues are addressable without new experiments but require significant revision. 4. Consolidated Assessment Overall Score: 4/6 (Borderline Reject) Confidence: High Recommendation: Borderline Reject Verdict Summary The paper tackles an important problem — understanding and quantifying variance sources in LLM evaluation — with impressive experimental scale (1M+ records, 8 experiments, 5 benchmarks, 6 models). The cross-benchmark variance gradient and task-specific D-study budgets are genuine contributions that would be useful to the community. The engine confound discovery (enforce_ eager fix) is a practical contribution in its own right. However, the paper falls short of the acceptance threshold for three main reasons: 1.  Methodological concern:  Model is pooled rather than treated as a G-theory facet, inflating the central item_ id claim. For a paper whose entire framework is G-theory, this is a fundamental design choice that needs addressing. 2.  Novelty and positioning:  The infrastructure extension — the claimed methodological advance over Mesting (2026) — yields near-null results ( <1% variance). The paper's actual novelty (cross-benchmark gradient, D-study budgets, confound fix) does not depend on the infrastructure extension and needs honest reframing. The bibliography (9 references) is far below top-venue standards with critical omissions (Bouthillier et al., IRT literature, benchmark subsampling work). 3.  Presentation:  15 tables, 0 figures. Key uncertainty quantification (CIs) is reported for only one component in one table. The separability threshold is arbitrary. These are fixable but collectively reduce confidence in the claims. Actionable Revisions (no new experiments needed) 1.  Re-analyze with model as a crossed facet  — report model×item interaction separately; adjust item_ id shares and D-study projections accordingly. 2.  Add CIs to all variance component tables  — especially for the direct Infra×Method interaction term. 3.  Expand bibliography to ≥25 references  — must include Bouthillier et al. (2021), IRT item analysis papers, tinyBenchmarks/HELM-Lite, Henderson et al. (2018), Shavelson & Webb (1991). 4.  Add 3–4 figures  — D-study curves, stacked-bar variance decomposition across benchmarks, benchmark gradient visualization. 5.  Reframe contributions honestly  — infrastructure separability as confirmatory null; item dominance as expected from measurement theory but newly quantified; cross-benchmark gradient as the primary novel finding. 6.  Derive or justify the separability threshold  — or replace with bootstrap CI on total direct interaction. 7.  Acknowledge item dominance tautology  — wide difficulty range → large item variance is psychometrically expected; the contribution is in quantifying its magnitude and benchmark-dependence. Strengths Worth Preserving -  The experimental scale and systematic confound control are genuinely impressive -  The cross-benchmark variance gradient (MMLU→ARC→GSM8K→MATH) is a clean, well-supported finding -  D-study budgets (380–950 items, 3–5× items-over-prompts ratio) fill a real practical gap -  The fine-tuning contrast (inverted hierarchy) explains divergent reproducibility conventions -  The conditional separability insight (aggregate-level separability vs. item-level interactions) is nuanced and useful 5. Scores Overall: 4/6 — Borderline Reject.  Substantial empirical work with genuine practical value, but fundamental G-theory design issue, insufficient positioning against related work, and presentation gaps place it below the acceptance threshold. Addressable with revision; no new experiments required.\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd4abd67ca4b22c4379e5071f4\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779306065864\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — best | dream_20260520T190053]  · Overall: borderline accept Reviewer R1: Methodology and Experimental Rigor Summary This paper applies Generalizability Theory (G-theory) to decompose variance in LLM evaluation across infrastructure (hardware, precision), methodology (prompt, seed, temperature, ordering), and measurement (item) facets. Across 6 models, 5 benchmarks, and 2M+ evaluation records, the authors find that item selection dominates variance (42--58%), direct infrastructure x methodology interactions are negligible (<0.5%), and current evaluation practices yield unacceptably low generalizability coefficients (G  < 0.40). D-study projections provide actionable reproducibility budgets showing item count increases are far more cost-effective than prompt or seed replication. The paper is ambitious in scope and the cross-domain transfer of G-theory to LLM evaluation is well-motivated, but several methodological concerns---particularly around the treatment of \\\"model\\\" in the G-theory framework, the interpretation of item variance, and incomplete uncertainty quantification---temper my enthusiasm. Strengths -  Timely and well-motivated problem.  The paper addresses a genuine gap: no prior work crosses infrastructure and methodology layers in a single G-theory framework. The positioning relative to Mesting (2026), Yuan et al. (2025), and Brittlebench (2026) is accurate and clearly articulated. -  Impressive experimental scale.  8 experiments, 2M+ records, 6 models, 5 benchmarks, and extension to fine-tuning. The breadth of coverage strengthens the generality claims substantially. All 8 planned experiments are present. -  Engine confound identification is a genuine methodological contribution.  The discovery that vLLM routes FP32 through a different compute path than BF16/FP16, inflating precision variance from 0.87% to 7.24% (interaction), is a valuable finding of independent interest. The before/after comparison is convincing. -  Actionable D-study budgets.  The reproducibility budget tables translate abstract variance component estimates into concrete design recommendations. The cross-benchmark budget table (Table 8 / Table 13-15 in the summary) showing task-specific item requirements is practically useful. -  Good confound control.  Uniform vLLM V0 + enforce_ eager across all precision modes, generation-based evaluation following Hua et al. (2025) to avoid log-likelihood artifacts, and stratified item sampling all reflect careful experimental design. -  Fine-tuning extension adds generality.  Showing that item dominance holds in fine-tuning (36.8--44.5%) with seed/LR replacing prompt/temperature as secondary factors is a non-trivial extension. -  Clear task-difficulty gradient.  The systematic pattern across 5 benchmarks (item_ id share decreasing, residual and temp x item increasing with difficulty) is a well-supported finding that provides theoretical insight. Weaknesses Major -  (W1) Model is pooled rather than treated as a facet---this fundamentally distorts the variance decomposition.  The paper pools 4 models and decomposes variance across the pooled data, but \\\"model\\\" is not included as a facet in the G-study. In standard G-theory, the object of measurement (here, presumably each model's ability) should be the differentiation facet. By pooling across models without including model as a facet, model-level variance is absorbed into item_ id (since different models have different difficulty profiles on the same items) and into the residual. This means the 58.4% attributed to item_ id is confounded with model x item interaction---the very thing G-theory is designed to separate. The per-model analyses (Table 2) partially address this, but the headline numbers and the D-study projections are based on the pooled analysis. This is a fundamental design choice that needs explicit justification. If the goal is to assess reliability of a  single model's  evaluation, the per-model G-studies should be primary. If the goal is reliability of  cross-model comparisons , model must be a facet. The paper's framing suggests both goals but delivers neither cleanly. -  (W2) The 0.5% separability threshold is arbitrary and self-serving.  The paper defines separability as \\\"direct infrastructure x methodology interactions contribute less than 0.5% of total variance\\\" and then finds exactly 0.5%. This threshold is not derived from any principled criterion (e.g., effect size conventions, practical significance for model ranking, or comparison to measurement error). A threshold chosen post hoc to match the observed result raises concerns. The paper should either: (a) derive the threshold from practical consequences (e.g., what interaction magnitude would change a model ranking?), (b) report the result without a binary threshold and let readers judge, or (c) use a formal hypothesis test with appropriate power analysis. -  (W3) Bootstrap CIs are reported only for the MMLU item_id component in most tables.  The paper summary mentions \\\"Bootstrap CIs (1000 resamples)\\\" as a general methodology, but Table 1 in the paper shows CIs for all components only on MMLU. Cross-benchmark (Table 3/4), hardware (Table 5), 14B (Table 9), and fine-tuning (Table 10) tables report point estimates without CIs. For claims about variance component magnitudes being \\\"negligible\\\" or \\\"substantial,\\\" CIs are essential---a 0.5% point estimate with a CI of [ 0.0%, 3.0%] tells a very different story than [ 0.4%, 0.6% ]. This is especially critical for the separability claim where the threshold is tight. -  (W4) ANOVA-based estimation (Henderson Method I) is used in the code, but the paper claims REML.  The variance_ decomposition.py code implements classical ANOVA-based variance component estimation (Type-I SS with EMS equations), not REML. REML would use a mixed-effects model fitted via maximum likelihood with restricted estimation. These methods can give different results, especially when designs are slightly unbalanced or when negative variance components arise. The code truncates negative estimates to zero, which is the ANOVA convention; REML handles this differently (constrained optimization). The paper should either: (a) actually implement REML (e.g., using lme4/statsmodels), or (b) correctly describe the method as ANOVA-based Henderson Method I estimation. Claiming REML when using ANOVA-based methods is a methodological misrepresentation. Moderate -  (W5) Only 2 GPU types for the hardware facet, with partial crossing.  The hardware experiment (Exp 3) uses only 2 GPU types with partial crossing (only 2 of 4 models run on both). With n=2 levels, the hardware main effect has 1 degree of freedom---insufficient for stable variance component estimation. The claim that \\\"hardware-related variance totals 4.1%\\\" has very wide implicit uncertainty. The partial crossing also means the hardware x model interaction is confounded with the hardware main effect for the 2 models not run on both GPUs. This limitation is not adequately discussed. -  (W6) Item dominance may be a statistical artifact of the binary response variable.  With a binary correct/incorrect response, items with extreme p-values (very easy or very hard) contribute disproportionately to total variance. The paper's own Decision D002 acknowledges that text_ exact_ match produces a radically different variance structure (prompt x item at 37.5% vs item_ id at 58.4% for binary). Yet the paper presents only the binary metric results. If the core claim is \\\"item selection dominates variance,\\\" this claim is metric-dependent, and the paper should present both metrics or at minimum discuss the metric sensitivity. The dual-metric analysis planned in D002 appears to have been dropped from the paper. -  (W7) Temperature levels differ across experiments without justification.  Exp 1 uses {0.1, 0.5, 1.0}, the paper summary mentions {0.0, 0.3, 0.7}, the experiment plan mentions {0.1, 0.5, 1.0} for some and 2 temperatures for others. Exp 2 uses 2 temperatures while Exp 1 uses 3. These inconsistencies make cross-experiment comparisons unreliable and suggest the \\\"fully crossed\\\" characterization is only approximate. The design is not truly balanced across experiments. -  (W8) D-study projections assume independence of item samples.  The D-study formula G = sigma_ tau / (sigma_ tau + sigma_ delta) assumes that additional items are independently sampled from the same universe. But benchmark items are not a random sample from a well-defined universe---they are curated collections. Extrapolating from 200 stratified-sampled items to 600 or 1100 items assumes the variance structure holds for items not in the sample. For MATH (500 total items), the recommendation of 1100 items is infeasible and reveals the limitation of treating benchmark items as a random sample from an infinite universe. -  (W9) The paper omits higher-order interactions.  The code explicitly states \\\"Higher-order interactions (>=3-way) are absorbed into the residual.\\\" With 6 facets, there are 20 three-way interactions, 15 four-way, etc. The residual of 16.8% likely contains substantial structured variance. If precision x temperature x item is large (plausible given both two-way interactions are non-trivial), the attributed shares for the two-way components would be biased. The paper should at minimum discuss this limitation or fit selected three-way interactions. Minor -  (W10) The Kruskal-Wallis test (H=47.3, p<0.001) cited for cross-benchmark differences is underspecified.  What is the test comparing? Variance component estimates across benchmarks? With only 5 benchmarks and point estimates, the degrees of freedom and interpretation are unclear. -  (W11) No correction for multiple comparisons.  Multiple permutation tests and bootstrap CIs are computed without any family-wise error rate correction (e.g., Bonferroni, Holm). -  (W12) The \\\"10x more cost-effective\\\" headline claim conflates marginal and average returns.  The 10.2:1 ratio compares marginal G gains per unit cost, but the cost metric treats one additional item the same as one additional prompt. In practice, additional prompts require human design effort while additional items can be sampled automatically. The cost comparison should distinguish compute cost from human annotation cost. Questions for Authors 1.  Why is \\\"model\\\" not a facet in the G-study? If models are pooled, how much of the 58.4% item_ id variance is actually model x item interaction? Can you provide the per-model G-study results as the primary analysis? 2.  The code uses ANOVA-based Henderson Method I estimation, but the paper claims REML. Which method was actually used for the reported results? If ANOVA-based, have you verified that the balanced-design assumption holds exactly (i.e., every cell has exactly the same number of observations)? 3.  What happens to the variance decomposition when you use text_ exact_ match instead of binary correct? Decision D002 in your project files describes this as producing a radically different structure. Why was this analysis excluded from the paper? 4.  The separability threshold of 0.5% appears to match the observed result exactly. Was this threshold set before or after seeing the data? What would the conclusion be at a 1% threshold? At 0.1%? 5.  For the MATH D-study recommendation of 1100 items: MATH has only 500 items total. How should practitioners interpret a recommendation that exceeds the benchmark size? Does this invalidate the D-study framework for small benchmarks? 6.  Can you provide bootstrap CIs for the separability claim (total direct infra x method interaction)? The 0.5% point estimate needs uncertainty quantification to be interpretable. 7.  How sensitive are the variance component estimates to the exclusion of three-way interactions? Have you tested a model with, e.g., precision x temperature x item included? 8.  The paper mentions temperature {0.0, 0.3, 0.7} in the summary but {0.1, 0.5, 1.0} in the tex file. Which values were actually used, and does including T=0.0 (deterministic) vs T=0.1 (near-deterministic) materially change the temperature variance component? Score and Recommendation Score: 4 (Borderline Reject) Confidence: High Recommendation: Borderline Reject The paper tackles an important problem with impressive experimental scale and provides useful practical contributions (engine confound identification, D-study budgets). However, the methodological concerns are substantive: (1) the treatment of model as pooled rather than as a G-theory facet fundamentally confounds the headline variance decomposition; (2) the mismatch between claimed (REML) and implemented (ANOVA) estimation methods undermines methodological credibility; (3) incomplete uncertainty quantification (CIs missing from most tables, especially the separability claim); and (4) the single-metric presentation omits a known sensitivity that changes the core finding. These are not cosmetic issues---they affect the validity of the three central claims. If the authors can address W1 (model as facet), W4 (REML vs ANOVA), W3 (CIs throughout), and W6 (dual metric), the paper would be substantially strengthened and could merit acceptance. In its current form, the ambitious scope is undermined by methodological gaps that a psychometrics-savvy reviewer would flag immediately.\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd498d1bca4b3536a73c41fdc8\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779305825891\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — best | dream_20260520T190053]  · Overall: borderline Dream Review Report Paper:  Reproducibility Budgets for LLM Evaluation: Testing the Separability Assumption Between Infrastructure and Methodological Variance Sources via Generalizability Theory Review Mode:  Full (2 Reviewers + Roundtable)\\n Review Standard:  Top ML venue, ~ 25% acceptance rate, 6-point scale Reviewer Scores Paper Summary The paper conducts a fully-crossed Generalizability Theory (G-theory) study unifying infrastructure (hardware, precision) × methodology (prompt, seed, temperature, ordering) × measurement (test items) factors in LLM evaluation. Across 6 models (7–14B), 5 benchmarks, and 2M+ records, the authors report: (1) item selection dominates variance (42–58%), (2) infrastructure–methodology separability holds at aggregate (<0.5%) but is item-conditional (14.2%), and (3) current practices yield G  < 0.40 while D-study budgets show items are 10× more cost-effective than prompts for reliability. A fine-tuning extension with RoBERTa-large shows item dominance generalizes to training. Consolidated Strengths S1. Ambitious experimental scale and systematic design. \\n Seven experiments totaling 2M+ evaluation records, building from single-benchmark to cross-benchmark, cross-model, cross-hardware, and cross-paradigm coverage. All 8 planned experiments are reflected in the paper. This is a serious empirical effort. S2. Engine confound discovery is a genuine methodological contribution. \\n The finding that vLLM routes FP32 through a different compute path (non-V0 engine), inflating precision variance from 0.3% to 0.87% (main) and from 1.8% to 7.24% (interaction) with an 8.5pp accuracy gap, is independently valuable. It serves as a concrete cautionary tale for any study comparing precision modes and demonstrates how infrastructure configuration can systematically bias variance attribution. S3. Nuanced two-level separability result. \\n Rather than a simple binary answer, the separability test yields complementary findings: aggregate separability holds ( <0.5% direct interactions), licensing isolated-factor studies, while item-conditional interactions (14.2%) warn that such conclusions are contingent on item selection. This is more informative than either finding alone. S4. D-study budgets are actionable. \\n The budget tables (Table 7, Table 8) provide concrete, immediately usable guidance: 600 items + 3 prompts + 2 seeds → G ≥ 0.90 for MMLU. The 10:1 marginal effectiveness ratio (items vs. prompts) is a memorable, practical takeaway. Cross-benchmark budget differences (550–1100 items) provide task-specific guidance. S5. Cross-benchmark difficulty gradient. \\n The systematic relationship between task difficulty and variance structure (item_ id decreases 58.4% → 42.1%, residual increases 16.8% → 24.8%, temp×item increases 5.8% → 10.4% as accuracy drops) quantifies why reasoning benchmarks are less reproducible. This is a genuinely useful empirical finding. Consolidated Weaknesses W1. Incremental over Mesting et al. (2026) — the core methodological contribution is an extension, not a new framework.  [ Both reviewers, R2 primary ]\\n Mesting et al. (2026) already applied G-theory to LLM evaluation with item, prompt, judge, and temperature facets, finding judge dominance at 43.8%. This paper extends that framework by adding infrastructure facets (hardware, precision). However, these infrastructure facets turn out to contribute negligibly: hardware main effect 0.6%, precision main effect 0.3%. The extension is real but modest in substance — the paper's most important finding (item dominance) could plausibly have emerged from a Mesting-style design without the infrastructure layer. The \\\"first fully-crossed\\\" framing oversells what is fundamentally an incremental extension. W2. \\\"Fully crossed\\\" design is overstated.  [ R1 primary ]\\n The paper claims a fully-crossed design but the factorial structure is unbalanced: -  MMLU has the richest design (3 precisions, 3 temperatures, 4 orderings, 2 GPUs) -  Other benchmarks use reduced designs (2 precisions, 2 temperatures) -  Hardware crossing is only on MMLU (Exp. 3) -  14B extension uses a reduced facet set -  Fine-tuning uses a completely different model/task family\\n Claims about cross-benchmark separability and scale invariance rest on narrower evidence than the \\\"fully crossed\\\" framing implies. The paper should clearly delineate which claims are supported by full crossing and which by partial designs. W3. Pooled-model analysis likely inflates item_id variance.  [ R1 primary ]\\n The primary analysis pools 4 models, treating them as exchangeable observations. But model × item interactions (some items are harder for Mistral than Qwen3) get absorbed into the item_ id component, inflating its apparent dominance. The per-model analysis (Table 2) partially addresses this (item_ id range 54.7–62.0%), but should be the primary presentation. The pooled analysis overstates the universality of the 58.4% figure. W4. Item dominance is partially predictable from first principles.  [ R2 primary ]\\n Any assessment with a steep difficulty gradient (items ranging from trivial to expert) will show item difficulty as the dominant variance source. The paper's own Discussion explains exactly why this must be so. While quantifying the magnitude is useful, framing it as surprising (\\\"researchers are optimizing the wrong knobs\\\") oversells the finding. A more measured framing — \\\"item dominance is expected but its magnitude (>50%) and the relative inefficiency of other interventions have not been quantified\\\" — would be more appropriate. W5. Separability threshold (0.5%) is arbitrary and the result is borderline.  [ R1 primary, R2 concurs ]\\n The 0.5% threshold for \\\"separability\\\" is not justified from G-theory, psychometrics, or any principled argument. The observed value (0.5%) lands exactly on the threshold boundary, making the binary \\\"separability holds\\\" conclusion fragile. A bootstrap confidence interval on the total direct interaction variance would be more informative. The result should be presented as a continuous measure with uncertainty rather than a pass/fail test. W6. D-study projections lack uncertainty quantification.  [ R1 primary ]\\n The budget recommendations (e.g., \\\"600 items + 3 prompts + 2 seeds → G ≥ 0.90\\\") are point estimates derived from estimated variance components. No confidence intervals or sensitivity analysis is provided for the projected G values. Given that the input variance components have SEs of 0.1–2.1%, the projected G values could shift meaningfully. The paper should propagate estimation uncertainty through the D-study projections (e.g., via bootstrap). W7. Very sparse reference list (only 7 references).  [ R2 primary, R1 concurs ]\\n For a top ML venue, 7 references is far below expectations. Critical omissions include: -  Classical G-theory: Brennan (2001) \\\"Generalizability Theory,\\\" Shavelson & Webb (1991) — foundational references for G-theory methodology -  ML variance decomposition: Bouthillier et al. (2021) \\\"Accounting for Variance in Machine Learning Benchmarks\\\" — the closest ML-native predecessor, not cited -  IRT in NLP: Lalor et al. (2019), Rodriguez et al. (2021), Vania et al. (2021) — item-level analysis frameworks directly relevant to the item dominance finding -  Ordering effects: Lu et al. (2022) — relevant to the ordering facet -  ML reproducibility: Henderson et al. (2018), Pineau et al. (2021) — broader context\\n This is not a minor issue: the missing references include direct methodological predecessors and would substantially change the novelty positioning. W8. Fine-tuning generalization is weak.  [ Both reviewers ]\\n The claim that \\\"findings extend to fine-tuning settings\\\" is based solely on RoBERTa-large (355M, encoder-only) on 4 NLU classification tasks. This is a large architectural and paradigm gap from the 7–14B decoder models used in inference experiments. Fine-tuning a 7B+ decoder model with LoRA/QLoRA on a generation task would be far more convincing as a generalization argument. As presented, this is a separate (interesting) finding rather than evidence of generalization. Questions for Authors Q1.  How would the variance decomposition change if model were treated as a random facet rather than pooling? Specifically, would model × item interactions reduce the item_ id share substantially? Q2.  Can you provide a direct numerical comparison with Mesting et al. (2026) on overlapping facets (item, prompt, temperature)? This would clarify the incremental contribution. Q3.  Would item dominance survive adding judge/scorer as a facet? Mesting found judge at 43.8% — this could substantially alter the variance hierarchy. The paper uses fixed generation-based scoring, which removes this source but also limits comparability. Q4.  Can you provide bootstrap confidence intervals for the D-study G projections? The headline recommendation (600/3/2 → G = 0.90) would be more credible with uncertainty bounds. Q5.  What is the justification for the 0.5% separability threshold? Would results change with 1% or 0.25%? Q6.  The MATH entry in Table 8 shows 1,100 items with \\\"66× cost factor\\\" but 1100 × 3 prompts × 2 seeds = 6,600 evaluations, not 13,200. Is this a typo, or does MATH require more prompts/seeds? Q7.  How were the 6 prompt templates selected? Were they designed to maximize diversity, or sampled from existing evaluation suites? The prompt × item interaction (6.1%) depends critically on prompt diversity. Minor Issues M1.  Table 3 column headers are misaligned in the PDF — \\\"item_ id %\\\" appears to span the wrong column. M2.  The ThinkingMachines (2025) reference has placeholder arXiv ID \\\"2501.xxxxx\\\" — needs the real ID. M3.  The abstract says \\\"6 models\\\" but the paper primarily analyzes 4 models with 2 as extension. Should be clearer about primary vs. extension. M4.  The paper claims \\\"over 2 million evaluation records\\\" — the sum of stated record counts (1,036,800 + 3×230,400 + 691,200 + 2×172,800 + 1,728 + 230,400 + 172,800) ≈ 3.17M. The \\\"over 2 million\\\" is an undercount of the actual total. Clarify. M5.  \\\"LayerCast\\\" is not a standard term — should be cited or defined more precisely. M6.  The D-study discussion mentions G ≥ 0.80 as the psychometric minimum but doesn't cite the source for this threshold (Nunnally & Bernstein 1994 or similar). Experiment Coverage Assessment All 8 planned experiments from the design document are reflected in the paper: -  ✅ exp-001: Full-scale precision study (MMLU) -  ✅ exp-002: Multi-benchmark replication (GSM8K, ARC, HellaSwag) -  ✅ exp-003: Multi-hardware G-study -  ✅ exp-004: D-study projections -  ✅ exp-005: 14B model extension -  ✅ exp-006: Fine-tuning G-study -  ✅ exp-007: LayerCast precision study -  ✅ exp-008: MATH benchmark extension Coverage is complete. However, several figures described in the experiment plan (stacked-bar decompositions, heatmaps, scatter plots, D-study projection curves, iso-G contour plots) are absent from the paper. The paper is table-heavy with no figures, which significantly weakens communication of key results — particularly the D-study projection curves (planned Fig 8–10) and the variance decomposition comparisons (planned Fig 1, 4, 15) which would be far more effective visually than as tables. Recommendation Consensus Score: 3.5/6 (Borderline — between Weak Reject and Weak Accept) For acceptance, the paper would need: 1.  Reframe novelty claims to acknowledge extension-of-Mesting positioning honestly 2.  Add per-model analysis as primary, pooled as secondary 3.  Add uncertainty quantification to D-study projections 4.  Substantially expand the reference list (add ≥15 missing key references) 5.  Justify or remove the 0.5% separability threshold 6.  Add figures — at minimum D-study projection curves and variance decomposition stacked bars The paper's core strengths  — the engine confound discovery, the nuanced separability result, the cross-benchmark difficulty gradient, and the actionable D-study budgets — represent genuine value. But the incremental positioning over Mesting et al., inflated novelty claims, methodological concerns (pooled analysis, arbitrary threshold, no uncertainty propagation), and severely sparse references pull it below the acceptance threshold in its current form. If revised to address the top 4 weaknesses , this could become a solid Weak Accept (4/6). The empirical effort is substantial and the practical recommendations fill a real need. The revisions are achievable without new experiments.\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd4834c5138b29f314581070fc\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779305688229\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — best | dream_20260520T190053]  · Overall: Weak Reject (3/6) R2 Review: Novelty and Related Work Summary This paper applies Generalizability Theory (G-theory) to LLM evaluation, crossing infrastructure factors (hardware, precision) with methodology factors (prompt, seed, temperature, ordering) and item selection in a single factorial design. The main findings are that item selection dominates variance (42-58%), infrastructure and methodology are separable at the aggregate level but interact through item difficulty, and D-study projections show current practices are severely underpowered (G  < 0.40). The work directly extends Mesting et al. (2026), who applied G-theory to methodological facets only, by adding infrastructure facets and testing separability. While the experimental scale is impressive (2M+ records, 5 benchmarks, 6 models), the novelty is incremental over Mesting, the item dominance finding is largely predictable from psychometric first principles, and the related work has significant gaps. Strengths S1.  Well-motivated separability test with nuanced outcome.  The distinction between aggregate separability ( <0.5% direct interactions) and item-conditional non-separability (14.2% combined) is genuinely useful. This is the paper's strongest conceptual contribution — it provides a principled answer to whether isolated-factor studies are valid, with appropriate caveats. The two-level framing (aggregate license + item-conditional warning) is more informative than a binary separability verdict. S2.  Scale and breadth of the experimental design.  Crossing 7 facets across 6 models, 5 benchmarks, and 2M+ records is a substantial empirical effort. The cross-benchmark gradient (item dominance decreasing with task difficulty, from 58.4% on MMLU to 42.1% on MATH) is a non-obvious finding that adds genuine insight about why reasoning benchmarks produce less reproducible results. S3.  Engine confound discovery.  The identification that vLLM routes FP32 through a different compute path than BF16/FP16, inflating precision variance from 0.3% to 0.87% (and precision x item from 1.8% to 7.24%), is a concrete methodological contribution of independent value. This is actionable for anyone doing precision comparisons and illustrates how infrastructure confounds can systematically bias variance attribution. S4.  D-study budgets are actionable.  The 10:1 marginal effectiveness ratio (items vs. prompts) and specific budget recommendations (600 items + 3 prompts + 2 seeds for G >= 0.90) translate directly into evaluation design guidance. The cross-benchmark budget table (550-1100 items depending on task) adds practical value. S5.  Fine-tuning extension broadens scope.  Showing that item dominance persists in fine-tuning (37-45%) while the secondary variance hierarchy shifts (seed/LR replace prompt/temperature) demonstrates the framework's generality beyond inference evaluation. Weaknesses W1.  Incremental novelty over Mesting et al. (2026).  The paper's core methodological contribution — applying G-theory to LLM evaluation — is Mesting's. What this paper adds is (a) infrastructure facets and (b) the separability test. But infrastructure turns out to be nearly negligible: precision contributes 0.3% main effect and hardware 0.6%. The separability test yields a largely expected null result at the aggregate level (it would be surprising if GPU type x prompt template interacted strongly). The item-conditional nuance is more interesting but is a secondary finding. The paper risks appearing as \\\"Mesting + two more facets that turn out not to matter much.\\\" W2.  Item dominance is predictable from psychometric first principles.  In any assessment with heterogeneous item difficulty, item variance will dominate when other factors have small effects. MMLU items range from trivial recall to expert reasoning — of course this produces massive item variance. The paper's own Discussion section essentially explains why this must be the case (\\\"steep difficulty gradient within every benchmark\\\"). The 58% figure quantifies what psychometricians would predict qualitatively. The paper does not adequately engage with whether this finding is genuinely surprising vs. a confirmation of well-known measurement theory. The counter-argument in the paper framing doc (\\\"the magnitude was not previously quantified\\\") is weak — the magnitude is a function of the specific item difficulty distribution in these benchmarks, not a universal property of LLM evaluation. W3.  Significant related work gaps.  Several important bodies of work are missing: -  Classical G-theory beyond Cronbach 1972.  Brennan (2001, \\\"Generalizability Theory\\\") is the standard modern reference and is entirely absent. Shavelson & Webb (1991) is missing. The median paper draft cites Brennan but the best-case paper does not. This is a serious omission for a paper whose primary methodological framework is G-theory. -  Reproducibility in ML broadly.  Pineau et al. (2021, \\\"Improving Reproducibility in ML: A Report from the NeurIPS Reproducibility Program\\\") and the ML reproducibility checklist literature are not cited. Bouthillier et al. (2021, \\\"Accounting for Variance in Machine Learning Benchmarks\\\") directly decomposed hyperparameter vs. seed vs. dataset variance using ANOVA — this is the closest ML-native predecessor to the present work and is completely missing. -  IRT-based item analysis in NLP.  Item Response Theory is the dominant psychometric framework for item analysis, and there is growing work applying IRT to NLP benchmarks (e.g., Lalor et al. 2019; Rodriguez et al. 2021 on IRT for NLP evaluation; Vania et al. 2021). The paper's finding that item selection dominates would be enriched by connecting to IRT-based difficulty estimation. -  Prompt ordering sensitivity.  Lu et al. (2022, \\\"Fantastically Ordered Prompts and Where to Find Them\\\") is a seminal work on ordering effects in LLM evaluation. The paper includes ordering as a facet but does not cite this foundational work. -  Benchmark contamination and item difficulty.  The item dominance finding intersects with work on benchmark contamination (Jacovi et al. 2023; Deng et al. 2024) and adaptive/dynamic benchmarking, which are not discussed. -  Variance decomposition in deep learning.  Beyond Bouthillier, there is work by Henderson et al. (2018, \\\"Deep Reinforcement Learning that Matters\\\") on seed sensitivity and Dodge et al. (2020) on fine-tuning instability, both performing variance decomposition without G-theory. W4.  Positioning vs. Mesting is incomplete.  The paper claims to \\\"extend\\\" Mesting by adding infrastructure facets, but does not adequately address key differences: (a) Mesting included judge as a facet (43.8% variance), which this paper deliberately excludes — this makes the variance structures incomparable, and the paper's item dominance finding might not hold if judge were included; (b) Mesting studied API models with opaque infrastructure, while this paper studies open-weight models — the papers study fundamentally different evaluation settings; (c) the paper does not discuss whether its variance estimates are consistent with Mesting's for the overlapping facets (prompt, seed, temperature, item). A direct numerical comparison on shared facets would strengthen the positioning. W5.  D-study budgets are a straightforward computation, not a conceptual contribution.  Once variance components are estimated, D-study projections are a mechanical application of G-theory formulas (plug in different facet levels, compute G). Calling this a \\\"practical tool\\\" contribution overstates it — it is the standard output of any G-study. The novelty is in the variance component estimates, not in the D-study arithmetic. W6.  The \\\"first\\\" claims are overclaimed.  The paper claims \\\"first fully-crossed G-theory study spanning infrastructure x methodology x measurement.\\\" But Mesting (2026) already conducted a G-study of LLM evaluation with multiple crossed facets including items. The incremental \\\"first\\\" is adding hardware and precision facets to an existing G-theory framework. Similarly, \\\"first formal test of separability\\\" is a stretch — any multi-factor ANOVA implicitly tests interactions, which is the same as separability. The paper should frame its contribution as \\\"extending\\\" rather than claiming multiple \\\"firsts.\\\" W7.  Model as a fixed effect raises questions.  The paper pools across 4 models but treats model as fixed (not a random facet). This means the variance decomposition is conditional on this specific model set. If model were treated as a random facet (as in Mesting), model x item interactions might absorb a substantial portion of what is currently attributed to item main effect. The paper does not discuss this design choice or its implications. Questions for Authors Q1. How would the variance decomposition change if model were treated as a random facet rather than fixed? Specifically, what fraction of the current \\\"item_ id\\\" variance would be absorbed by model x item interactions? This is critical because the item dominance claim (58.4%) may be inflated by pooling across models with different difficulty profiles. Q2. Can you provide a direct numerical comparison with Mesting et al. (2026) on overlapping facets? Specifically, what are Mesting's estimates for item, prompt, temperature, and seed variance, and how do yours compare? If they differ substantially, what explains the discrepancy (different models, different evaluation protocol, different item samples)? Q3. If judge were added as a facet (as in Mesting, where it contributed 43.8%), would item dominance still hold? Your design decision to fix the judge is defensible but means your variance structure is not directly comparable to the most closely related prior work. Q4. The 0.5% threshold for separability appears arbitrary. What is the justification for this specific threshold? Would the conclusions change at 1%? At 2%? The multi-hardware G-study reports exactly 0.5% for direct interactions — right at the threshold — which warrants sensitivity analysis. Q5. The paper treats \\\"item selection\\\" as a single construct, but items vary in multiple dimensions (difficulty, domain, format, discrimination). Can you decompose item variance further — e.g., into difficulty, domain, and residual item components? This would make the \\\"prioritize item count\\\" recommendation more actionable (should practitioners sample more items within domains, or across domains?). Q6. Bouthillier et al. (2021) conducted ANOVA-based variance decomposition across datasets, hyperparameters, and seeds for ML benchmarks generally. How do your findings compare? Their work predates yours and covers similar ground using simpler methods. What does G-theory add beyond what ANOVA decomposition already provides? Minor Issues M1. The bibliography has only 7 entries for a paper of this scope. A related work section citing only 7 papers at a top venue will raise immediate red flags. Expect 30-50 references minimum. M2. The title is 22 words long and contains a colon, a subtitle, and a methodological term. Consider shortening — e.g., \\\"Reproducibility Budgets for LLM Evaluation via Generalizability Theory.\\\" M3. The abstract mentions \\\"over 2 million evaluation records\\\" but the experiments sum to approximately 2.7M records. Be precise. M4. The term \\\"empirical license\\\" for isolated-factor studies is loaded — it suggests this paper has authority to grant permission to other researchers. Consider \\\"empirical support for\\\" instead. M5. Table 1 reports residual at 16.8% — this is a large unexplained component. The paper should discuss what residual captures (higher-order interactions, measurement error, model-level stochasticity beyond seed). M6. The paper uses \\\"item dominance\\\" as a finding label, but in G-theory the term \\\"facet\\\" is standard. \\\"Item\\\" is the object of measurement, not a facet in the traditional sense. The paper should clarify the terminological mapping from psychometrics to ML evaluation more carefully. M7. The fine-tuning G-study uses RoBERTa-large, a 355M encoder model, which is architecturally very different from the 7-14B decoder models in the inference experiments. The generalizability of fine-tuning findings to modern LLM fine-tuning (e.g., LoRA on 7B+ models) is questionable. M8. Cronbach et al. (1972) citation is to the book \\\"The Dependability of Behavioral Measurements\\\" but the correct G-theory foundational reference is Cronbach, Gleser, Nanda & Rajaratnam (1972), which the paper does cite correctly in the bib — but should verify the title matches. Scores -  Novelty: 2.5/5 — The infrastructure extension over Mesting is modest (infrastructure contributes negligibly), the item dominance finding is predictable, and the D-study budgets are mechanical. The separability test and engine confound discovery provide genuine but limited novelty. -  Significance: 3/5 — The practical recommendations are useful and the scale is impressive, but the core message (\\\"use more items\\\") is not paradigm-shifting. The 18x cost factor for G >= 0.90 may actually discourage adoption. -  Related Work Completeness: 2/5 — Major gaps in classical G-theory references, ML reproducibility literature, IRT, and variance decomposition predecessors. Only 7 citations is far below venue expectations. -  Overall Score: 3/6 (Weak Reject) — A competent empirical study with impressive scale, but incremental novelty over Mesting et al. (2026), predictable main finding, significant related work gaps, and overclaimed \\\"first\\\" contributions. The separability test and engine confound are the strongest novel elements but are secondary to the paper's framing. With substantially expanded related work, more careful positioning (emphasizing extension rather than \\\"firsts\\\"), and deeper engagement with why item dominance is or is not surprising, this could reach borderline accept. -  Confidence: 4/5 — I am familiar with G-theory, the LLM evaluation reproducibility literature, and the ML benchmarking literature. I have read the cited papers. My uncertainty is primarily around whether the engine confound finding would be valued more highly by systems-oriented reviewers.\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd482bf9cacb4bec894662f6f2\", \"senderId\": \"cli_a974499e77fadbdd\", \"createTime\": \"1779305671259\", \"msgType\": \"post\", \"content\": \"🌙  [Dream Review Report — best | dream_20260520T190053]  · Overall: Weak Accept (4/6) R1 Review: Methods and Experiments Summary This paper applies Generalizability Theory to LLM evaluation in a fully-crossed design spanning infrastructure (hardware, precision) x methodology (prompt, seed, temperature, ordering) x measurement (item) factors across 6 models, 5 benchmarks, and >2M records. The core finding is that item selection dominates variance (42-58%), direct infrastructure x methodology interactions are negligible (<0.5%), and current evaluation practices yield unacceptably low generalizability (G <0.40). D-study projections provide actionable reproducibility budgets. The methodology is largely sound and the experimental coverage is impressive, but several issues with estimation, design balance, generalizability claims, and missing analyses prevent a higher score. Strengths S1.  Correct and well-motivated G-theory application.  The paper properly applies REML estimation for variance component extraction in a random-effects framework. The choice of G-theory over simpler ANOVA decomposition is well-justified: it enables simultaneous multi-facet decomposition and D-study projections, which are the paper's key practical contribution. The universe score / relative error decomposition for the G coefficient follows standard Brennan (2001) formulations. S2.  Engine confound identification is a genuine methodological contribution.  The discovery that vLLM routes FP32 through a different compute path than BF16/FP16 (inflating precision variance from 0.3% to 0.87% main, 1.8% to 7.24% interaction) is valuable to the community independent of the G-theory framing. The fix (V0 enforce_ eager for all precision modes) is principled and well-documented. This demonstrates the kind of careful confound control that is often missing in LLM evaluation studies. S3.  Comprehensive experimental coverage.  All 8 planned experiments are reflected in the paper, covering: multi-model (6 models), multi-benchmark (5 benchmarks), multi-hardware (2 GPU types), scale validation (14B), paradigm extension (fine-tuning), and precision mode analysis (LayerCast). The total record count (>2M) provides substantial statistical power. The cross-benchmark gradient (item_ id share decreasing with task difficulty) is a genuinely interesting finding. S4.  Actionable D-study budgets.  The reproducibility budget tables (Tables 7-8) translate abstract variance components into concrete practitioner guidance. The \\\"10x more effective to triple items than triple prompts\\\" headline is well-supported by the marginal effectiveness ratios and will be immediately useful to evaluation practitioners. S5.  Appropriate use of generation-based evaluation.  Following Hua et al. (2025) to avoid log-likelihood scoring artifacts is a sound design choice that strengthens the ecological validity of the findings. Weaknesses W1.  The \\\"fully crossed\\\" design has important structural gaps.  The paper claims a fully-crossed design but several elements are not fully crossed: -  Exp-1 (MMLU) uses 3 precisions x 6 prompts x 6 seeds x 3 temperatures x 4 orderings, but Exp-2 (GSM8K/ARC/HellaSwag) uses only 2 precisions x 2 temperatures. This means the cross-benchmark comparisons in Table 3 are not on equal footing -- MMLU has richer factorial coverage and more records (1,036,800 vs 230,400 per benchmark). -  Hardware is only crossed in Exp-3 (MMLU), not in the multi-benchmark experiments. The separability claim therefore rests on a single benchmark. -  The 14B extension (Exp-5) uses 2 precisions only, not the full factorial. Claiming \\\"scale invariance\\\" from a reduced design on one benchmark is an overstatement. -  These design imbalances mean the pooled analyses implicitly weight MMLU more heavily. The paper should be transparent about which claims rest on full versus partial factorial evidence. W2.  200 items is potentially insufficient for stable higher-order interaction estimates.  With 200 items per benchmark and up to 12 variance components (Table 1), some interaction terms (especially 3-way and higher) are estimated from thin margins. The SEs in Table 1 are reported but several CIs are wide relative to the point estimates (e.g., ordering x item: 1.4% with CI [ 0.8, 2.0]; seed: 0.1% with CI [ 0.0, 0.2 ]). The paper does not report whether REML convergence diagnostics were checked, whether negative variance estimates were encountered and how they were handled (boundary constraints or set to zero), or whether bootstrap CIs were used as a robustness check. For a G-theory study, these are standard reporting requirements (Brennan 2001, Chapter 8). W3.  The 0.5% separability threshold is arbitrary and not well-justified.  The paper defines separability as direct infra x method interactions <0.5% of total variance, and the observed value is exactly 0.5% (Table 5). This is a razor-thin pass. The threshold is not derived from any established criterion in G-theory or psychometrics. Furthermore, \\\"0.5% of total variance\\\" is a relative measure that depends on the magnitude of item_ id variance -- if items were held fixed (eliminating 56% of variance), the same absolute interaction magnitude would represent ~ 1.1% of the remaining variance. The paper should either: (a) justify the threshold from first principles or prior literature, (b) report the result on an absolute scale (raw variance component values), or (c) frame it as a continuous quantity rather than a binary pass/fail. W4.  \\\"4 models pooled\\\" analysis conflates model-level and condition-level variance.  Pooling 4 models into a single variance decomposition (Table 1) is problematic because model is not a random facet in the same sense as prompt or seed -- these are 4 specific models, not a random sample from a model population. The pooled analysis implicitly treats model differences as part of the residual or item_ id component. The per-model analyses (Table 2) partially address this, but the headline numbers (58.4% item_ id) come from the pooled analysis. If model were included as a facet, model x item interactions could absorb substantial variance currently attributed to item_ id. The paper should either: (a) include model as a facet and report model x item interactions, or (b) report per-model results as primary and pooled as secondary, with clear caveats. W5.  D-study projections do not propagate estimation uncertainty.  The D-study budget tables report point estimates of G for each allocation but do not provide confidence intervals on G itself. Since G is a function of estimated variance components, and those components have non-trivial SEs (Table 1), the projected G values inherit estimation uncertainty. A G=0.90 projection could easily be G=[ 0.85, 0.95 ] given the component SEs. Without propagated uncertainty, the specific budget recommendations (e.g., \\\"600 items + 3 prompts + 2 seeds\\\") appear more precise than warranted. Bootstrap or delta-method CIs on projected G values are standard in D-study practice. W6.  The fine-tuning extension (RoBERTa-large on 4 NLU tasks) is a weak generalizability probe.  RoBERTa-large is a 355M encoder model fine-tuned on classification tasks -- architecturally and procedurally very different from 7-14B decoder models evaluated via generation. Claiming that \\\"item dominance extends to fine-tuning\\\" based on this single architecture on classification tasks is a stretch. The fine-tuning facet structure is also quite different (seed, LR, data shuffle, GPU, precision vs. prompt, seed, temperature, ordering, precision, hardware), making direct comparison of variance shares across paradigms (Table 10) potentially misleading. This extension would be more convincing with at least one generative fine-tuning setting (e.g., SFT of a 7B model). W7.  Missing dual-metric analysis undermines a key design decision.  The project's decisions.yaml (D002) records a deliberate decision to adopt dual-metric analysis (binary correct + text exact match) as a core methodology, noting that text exact match produces fundamentally different variance structure (prompt x item dominant at 37.5%, G=0.975). This analysis is entirely absent from the paper. Its omission is concerning because: (a) it would substantially complicate the \\\"item dominance\\\" narrative (item_ id may not dominate under text exact match), and (b) it was identified as a methodological strength. If the dual-metric analysis was dropped, the paper should justify why; if it was never completed, the paper should acknowledge that variance structure is metric-conditional. W8.  Only 2 GPU types for the hardware facet.  The hardware facet has only 2 levels (RTX PRO 6000 + one other GPU). In G-theory, variance component estimates for facets with very few levels are unstable. With k=2 levels, the hardware main effect and hardware x item interaction have 1 degree of freedom each, providing minimal power to detect non-zero components. The 0.6% hardware main effect could easily be noise. The paper should acknowledge this limitation more prominently rather than drawing strong conclusions about hardware effects from 2 GPUs. Questions for Authors Q1. How were negative variance component estimates handled in REML? Were any components estimated as negative and subsequently constrained to zero? If so, which components and in which experiments? This is critical for interpreting the small components (seed: 0.1%, ordering: 0.3%). Q2. The paper reports 1,036,800 records for Exp-1 as 4 models x 3 precisions x 6 prompts x 6 seeds x 3 temperatures x 4 orderings x 200 items. Was model included as a facet in the REML estimation, or were records from 4 models simply concatenated? If concatenated, model-level variance is confounded with item_ id and residual. Please clarify the exact mixed model specification. Q3. The separability test uses data from Exp-3 (691,200 records on MMLU only). Were separability tests conducted on the other 4 benchmarks? If not, the separability claim is benchmark-conditional, which undermines its generality. Q4. Table 1 components sum to approximately 95.5% (58.4+16.8+6.1+5.8+2.9+1.8+1.4+0.9+0.7+0.3+0.3+0.1=95.5). What accounts for the remaining ~ 4.5%? Higher-order interactions? Confounded terms? This should be explained. Q5. The D002 decision explicitly adopted dual-metric (binary correct + text exact match) analysis as a core methodology, noting that text exact match yields G=0.975 with a completely different variance hierarchy. Why was this analysis excluded from the paper? Does item dominance hold under text exact match? Q6. For the fine-tuning G-study, was item treated as a random facet in the same way as for inference? In fine-tuning, all training items are used for training, and item_ id refers to test items. Is the item_ id variance in Table 10 comparable across the two paradigms? Q7. The paper uses vLLM 0.9.2 with V0 enforce_ eager. Were any experiments run with V1 or batch-invariant kernels to quantify how much the engine choice itself contributes to the variance decomposition? Given the engine confound discovery, the variance estimates are conditional on this specific engine configuration. Minor Issues M1.  Table 1 column headers : \\\"SE\\\" and \\\"95% CI\\\" are not defined in the table caption. Are SEs computed via REML information matrix, jackknife, or bootstrap? The method matters for interpretation. M2.  Inconsistent facet levels across experiments : The method section lists temperatures as \\\"2-3 levels (T in {0.1, 0.5, 1.0})\\\" but Exp-2 uses only 2 temperatures. The specific levels used in each experiment should be listed in a supplementary table. M3.  Table 8 (MATH budget) : 1,100 items x 3 prompts x 2 seeds = 6,600 evaluations, but the table reports 13,200. This implies either 4 prompts x 3 seeds or some other configuration not stated in the table header (\\\"3 prompts, 2 seeds\\\"). M4.  Missing effect sizes : Variance percentages are relative measures. Raw variance components (on the original score scale) should be reported at least in supplementary material to allow readers to assess practical significance. M5.  Bibliography incomplete : Several citations use placeholder information (e.g., \\\"arXiv:2501.xxxxx\\\" for ThinkingMachines 2025). Multiple cited papers lack venue, year, or full author information. M6.  No software/code availability statement.  For a methodology paper advocating specific evaluation practices, releasing the analysis pipeline and variance decomposition code would substantially increase impact and allow independent verification. M7.  The paper would benefit from a Figure 1  showing the facet structure diagram. The fully-crossed design is the paper's key methodological contribution, and a visual representation would aid comprehension. The current paper has no figures at all. M8.  Notation : The G-theory formulation in Eq. 1 uses generic alpha terms but does not specify which terms are estimated in each experiment. A mapping from the generic model to the specific facet structure would help readers unfamiliar with G-theory. Scores -  Soundness: 3/5 — Core G-theory application is correct, but the pooled-model analysis strategy, arbitrary separability threshold, missing dual-metric analysis, and lack of uncertainty propagation in D-study projections are non-trivial methodological concerns. -  Empirical Rigor: 4/5 — Impressive scale and coverage (2M+ records, 6 models, 5 benchmarks), engine confound identification is exemplary, but design imbalances across experiments and the thin hardware facet (k=2) weaken several claims. -  Overall Score: 4/6 (Weak Accept) — The paper addresses an important gap (unified infrastructure x methodology variance decomposition), provides actionable practical guidance (reproducibility budgets), and the engine confound finding alone justifies publication. However, the methodological concerns (W3-W5, W7) and design imbalances (W1) prevent confident acceptance. Addressing W4 (model as facet), W5 (uncertainty on G projections), and W7 (dual-metric analysis) in revision would elevate this to a clear accept. -  Confidence: 4/5 — Familiar with G-theory, REML estimation, and LLM evaluation methodology. Reviewed the full paper, experimental design, imagined results, and project context including design decisions.\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd4f0b3c0a0b20bc09f6f1b7f9\", \"senderId\": \"\", \"createTime\": \"1779305447925\", \"msgType\": \"system\", \"content\": \"[system]\", \"rootId\": \"\"}, {\"messageId\": \"om_x100b6fd4f0b164a4b1127b021fd2cae\", \"senderId\": \"\", \"createTime\": \"1779305447845\", \"msgType\": \"system\", \"content\": \"[system]\", \"rootId\": \"\"}], \"count\": 18, \"text\": \"[05-20 23:54] cli_a974499e77fadbdd: 🌙  [Dream Review Report — worst | dream_20260520T222113]  · Overall: weak reject Review Report: \\\"Variance Decomposition Is a Measurement, Not a Fact\\\" Dream ID:  20260520T222113 |  Review Mode:  Full (2 Reviewers + Roundtable) Reviewer Assignments -  R1  — Methodology & Experiments (Score: 4/6, Confidence: 4/5) -  R2  — Novelty & Related Work (Score: 3/6, Confidence: 4/5) 1. Paper Summary The paper applies Generalizability Theory to LLM evaluation variance across 5 benchmarks, 4–6 models, and multiple infrastructure × methodology factors (172,800–230,400 observations per experiment). It makes three claims: (1) item dominance estimates are sample-unstable (CV=33%), (2) model×item interaction (33%) is the largest overlooked component when model is treated as a crossed facet, and (3) D-study reproducibility budgets converge across benchmarks but carry ±190-item CIs rendering benchmark-specific recommendations meaningless. The framing: \\\"variance decomposition is a measurement, not a fact.\\\" 2. R1 Review: Methodology & Experiments Strengths -  Impressive experimental scale.  ~ 4M total records across 8 experiments, 5 benchmarks, 6 models. The factorial designs are well-constructed and the confound correction (V0 enforce_ eager) is a genuine contribution. -  Model-as-facet reanalysis is well-executed.  The item_ id drop from 37.8%→15.2% with model×item absorbing the difference is a clean, interpretable result that challenges standard practice. -  Separability analysis across hardware.  The infra×method jump from 1.5% (single-GPU) to 5.5% (multi-GPU) is well-demonstrated and practically important. -  D-study projections with uncertainty.  Reporting bootstrap CIs on reproducibility budgets is methodologically sound practice that prior work omits. Weaknesses -  Centerpiece claim rests on thin evidence.  The CV=33% finding (Exp 1b) uses only 3 item samples, 1 model (Llama-3.1-8B), 1 benchmark (MMLU). Three data points cannot reliably estimate a coefficient of variation. The CV itself has enormous uncertainty — it could plausibly be 15% or 50%. A claim that \\\"all prior single-decomposition studies over-commit\\\" requires far more resamples (30+ recommended) and generalization across models and benchmarks. -  Bootstrap validity concern.  Resampling 200 items with replacement creates ~ 127 unique items per bootstrap sample, producing duplicate observations that violate the independence assumptions of the G-theory model. The resulting CIs may be miscalibrated. The paper does not discuss this issue or compare with jackknife/subsampling alternatives. -  Cross-benchmark design asymmetry.  MMLU uses a 3×3 precision-temperature grid while other benchmarks use 2×2. Comparing variance percentages across different factorial structures without matched-design sensitivity analysis is methodologically questionable. -  G-coefficient interpretation.  The paper reports G=0.32 for 200 items as evidence of \\\"inherent low reliability,\\\" but standard MMLU evaluation uses all ~ 14K items. D-study projection to full benchmark size would likely yield G>0.90, substantially weakening the alarm about current practice. -  Zero figures.  A paper about variance decomposition with 18 tables and no figures is a critical presentation failure. Stacked bar charts, waterfall diagrams, and bootstrap density plots (all described in the design context) would dramatically improve comprehension. -  Thin secondary experiments.  Exp 5 (n=2 14B models, scale/architecture confounded) contributes near-zero evidential value. Exp 7 (LayerCast) is a null result that could be a footnote. Exp 6 (RoBERTa fine-tuning) uses encoder-only architecture, making the inference-training comparison apples-to-oranges for the LLM evaluation claim. Questions for Authors 1.  Why only 3 item resamples for the centerpiece claim? What is the bootstrap CI on the CV=0.33 estimate itself? 2.  How do you handle duplicate items in bootstrap resamples given G-theory's independence assumptions? 3.  What would G be for MMLU at its full ~ 14K item size under your D-study projections? 4.  The MMLU experiments use a richer factorial design than other benchmarks — have you verified that the cross-benchmark comparisons aren't confounded by design differences? R1 Score: 4/6 (Weak Accept) | Confidence: 4/5 3. R2 Review: Novelty & Related Work Strengths -  The resampling instability result is novel for ML evaluation.  Even if the concept is known in psychometrics, nobody has empirically demonstrated rank inversions across item samples for LLM evaluation variance decomposition. The qualitative finding (residual > item_ id in Sample 7) is striking. -  The bimodality→item_id correlation  (r=0.95) is an interesting mechanistic hypothesis that could guide benchmark design, even if underpowered (n=5 benchmarks). -  Engine confound correction  (V0 enforce_ eager reducing precision main effect from ~ 7% to 1.6%) is a valuable practical contribution for the community. -  Clear three-contribution structure  in the introduction makes claims easy to evaluate. Weaknesses -  The central conceptual claim is not novel.  \\\"Variance decomposition estimates have sampling variability\\\" is established in psychometric measurement theory (Brennan 2001, Chapter 8; Cardinet et al. 2010). The paper presents this as a discovery (\\\"we set out to build budgets and discovered the budget is unreliable\\\") without acknowledging that measurement theorists have known this for decades. For a measurement-literate audience, the surprise factor is low. -  Missing engagement with psychometric precedent.  The paper cites Shavelson & Webb (1991) and Brennan (2001) for G-theory basics but ignores their extensive discussion of variance component estimation error, sampling variability of G-coefficients, and the known sensitivity to universe definition (fixed vs. random facets). The critique of Mesting (2026) for treating model as fixed is particularly problematic — model-as-fixed is a legitimate design choice when generalizing only to those specific models, not an \\\"error.\\\" -  Three claims are one finding stated three ways.  All three contributions reduce to \\\"variance component estimates are uncertain\\\": (1) they vary across item samples, (2) they vary across model specifications, (3) the D-study projections derived from them are also uncertain. This is a single observation about estimation uncertainty, not three independent contributions. -  Purely diagnostic — no constructive contribution.  The three recommendations (report resampling stability, treat model as crossed, add CIs to budgets) are standard statistical advice. The paper does not provide a corrected estimation procedure, a practical resampling protocol, a software tool, or a concrete recommended minimum number of resamples. Practitioners reading this paper learn that their current approach is wrong but not what to do instead. -  The narrative pivot feels post-hoc.  The experiment design context reveals the paper originally aimed to demonstrate a \\\"cross-benchmark variance gradient\\\" (knowledge→reasoning). When this failed (spread=9pp, wrong direction), the paper reframed around instability. The narrative \\\"we set out to build budgets and discovered they're unreliable\\\" is technically accurate but obscures that the current framing was not the original research question. -  Bimodality correlation is underpowered.  r=0.95 from n=5 benchmarks has a 95% CI of approximately [ 0.63, 0.99 ] — wide enough to be consistent with moderate or near-perfect correlation. Moreover, bimodality mechanistically drives item-level variance almost by definition (bimodal difficulty → high between-item variance), making this partially tautological. -  Overclaiming.  \\\"Every prior study that reports a single variance decomposition... has presented one draw from a high-variance distribution as a finding\\\" is a sweeping claim supported by 3 resamples on 1 model × 1 benchmark. The paper does not test whether other studies' decompositions would show similar instability under their specific designs. -  Paper bloat.  18 tables across 13 pages with zero figures. Experiments 5 (14B extension), 6 (fine-tuning), and 7 (LayerCast) collectively contribute ~ 2 pages of marginal findings. The paper would be stronger at 10 pages with 4 core experiments and actual figures. Missing Related Work -  Cardinet, Johnson, & Pini (2010): \\\"Applying Generalizability Theory Using EduG\\\" — extensive treatment of variance component sampling variability -  Webb, Shavelson, & Haertel (2006): On reliability of G-study variance components -  Marcoulides (1996): On estimating variance components in G-theory -  The IRT literature on item sampling (e.g., Lord & Novick, 1968; van der Linden & Hambleton, 1997) covers similar ground on the instability of item parameter estimates Questions for Authors 1.  How do you respond to the argument that variance component estimation uncertainty is already well-characterized in Brennan (2001, Ch. 8) and Cardinet et al. (2010)? What specifically is new beyond applying known concepts to a new domain? 2.  The critique of model-as-fixed analysis assumes that prior work intended to generalize across models. If Mesting (2026) deliberately fixed model to study judge-specific behavior, how is this an error rather than a design choice? 3.  Can you provide a concrete, actionable resampling protocol? How many resamples, what sample sizes, what estimator? 4.  The r=0.95 bimodality correlation has n=5. Have you considered that this is partially tautological (bimodal item difficulty → high item variance, by construction)? 5.  Would you characterize your contribution as \\\"discovering that measurement error exists\\\" or as \\\"quantifying its magnitude in a specific domain\\\"? If the latter, how robust is the quantification with only 3 resamples? R2 Score: 3/6 (Weak Reject) | Confidence: 4/5 4. Roundtable Discussion Step 2: Cross-Sharing R1 responds to R2's novelty concern:  R1 acknowledges that the conceptual point is known in psychometrics but argues the empirical demonstration in the LLM evaluation context — particularly the rank inversions and the magnitude of model×item interaction — provides actionable new information to the ML community. However, R1 concedes that 3 resamples severely undermines the quantitative claim (CV=33% specifically). R2 responds to R1's methodology points:  R2 agrees that the bootstrap validity concern (duplicate items violating independence) is serious and not addressed. R2 also agrees that the G-coefficient interpretation at 200 items vs. full benchmark size is misleading. Step 3: Convergence Points of agreement (both reviewers): 1.  The zero-figures presentation is unacceptable for a variance decomposition paper. This alone would warrant revision. 2.  The centerpiece claim (CV=33%) rests on only 3 data points from 1 model and 1 benchmark — far too thin for the sweeping conclusion that \\\"all prior single-decomposition studies\\\" are unreliable. 3.  Experiments 5 (14B), 6 (fine-tuning with RoBERTa), and 7 (LayerCast) are bloat that should be cut or moved to appendix. 4.  The model-as-facet reanalysis (Exp 4) is the strongest individual result — the 37.8%→15.2% shift with model×item=33% is clean and important. 5.  The paper is purely diagnostic with no constructive solution beyond standard statistical advice. 6.  The bootstrap methodology needs more careful treatment of independence assumptions. Points of disagreement: -  R1 gives more credit for experimental scale and practical value to the ML community; R2 weights novelty relative to psychometric precedent more heavily. -  R1 sees the paper as publishable with revisions; R2 sees fundamental framing issues that require a major reconceptualization. Step 4: Score Convergence R1 initial: 4 (Weak Accept). R2 initial: 3 (Weak Reject). After discussion, R1 moves to  3–4 , acknowledging that the thin evidence base for the centerpiece claim (3 resamples) is more damaging than initially assessed. R2 holds at  3 , noting that even with more resamples, the conceptual novelty concern remains. Consensus score: 3 (Weak Reject) 5. Consolidated Assessment Overall Score: 3/6 (Weak Reject) Meta-Review Summary This paper attempts an ambitious meta-methodological critique of variance decomposition in LLM evaluation, arguing that decomposition estimates are themselves unreliable measurements. The experimental scale is impressive (~ 4M observations across 8 experiments), and individual results — particularly the model-as-facet reanalysis showing model×item interaction at 33% — are genuinely informative for the ML evaluation community. However, the paper suffers from several compounding weaknesses that collectively prevent acceptance: 1.  The centerpiece claim is underpowered.  CV=33% from 3 item resamples on 1 model × 1 benchmark cannot support the conclusion that all prior single-decomposition studies are unreliable. The CV estimate itself has enormous uncertainty and the generalization across models/benchmarks is untested. 2.  Conceptual novelty is limited.  The central insight — that variance component estimates have sampling variability — is well-established in the psychometric literature the paper builds on. The paper would be stronger if it acknowledged this precedent and focused on quantifying the problem's magnitude in the LLM evaluation domain, rather than framing it as a discovery. 3.  No constructive contribution.  The recommendations (\\\"report CIs,\\\" \\\"treat model as crossed,\\\" \\\"add error bars to budgets\\\") are standard statistical practice. The paper diagnoses a problem but offers no tool, protocol, or corrected estimator. 4.  Presentation is inadequate.  18 tables and zero figures in a variance decomposition paper. Several experiments (5, 6, 7) contribute marginal evidence and inflate the paper without strengthening core claims. 5.  Methodological gaps.  Bootstrap validity under item duplication, G-coefficient interpretation at subsampled vs. full benchmark size, and cross-benchmark design asymmetry are unaddressed. Actionable Revision Guidance To reach acceptance at a top venue, the authors should: -  Increase resamples to 30+ and extend across multiple models/benchmarks  to make the CV estimate credible -  Acknowledge psychometric precedent  (Brennan 2001 Ch. 8, Cardinet et al. 2010) and reframe as \\\"quantifying a known problem in a new, practically important domain\\\" -  Cut Experiments 5, 6, 7  and use the space for figures and deeper analysis of core results -  Add figures : stacked bars for variance decomposition comparison, waterfall for model-fixed→crossed shift, bootstrap density plots, D-study projection curves with CI bands -  Provide a constructive contribution : a concrete resampling protocol, minimum resample recommendations, or a software package -  Address bootstrap methodology : discuss independence violations from item duplication, compare with jackknife/subsampling, report calibration checks -  Reframe the three claims honestly : they are one finding (estimation uncertainty) demonstrated through three lenses, not three independent contributions Scores Summary\\n[05-20 23:52] cli_a974499e77fadbdd: 🌙  [Dream Review Report — best | dream_20260520T222113]  · Overall: weak accept (4/6) Reviewer R1: Methodology Soundness and Experimental Rigor 1. Summary This paper applies Generalizability Theory (G-theory) to decompose variance sources in LLM evaluation across five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), six models (4 at 7--9B, 2 at 14B), and approximately 4 million evaluation records. The design crosses infrastructure facets (numerical precision, GPU hardware) with methodology facets (prompt template, random seed, temperature, option ordering) and a measurement facet (item selection). Three claims are advanced: (1) item dominance is benchmark-conditional, following a monotonic 35pp gradient from knowledge retrieval (56%) to complex reasoning (21%); (2) direct infrastructure x methodology interactions are negligible ( <0.3%), confirming separability; (3) D-study reproducibility budgets reverse across task types (MMLU is item-limited, GSM8K is seed-limited), rendering universal evaluation recipes illusory. Eight experiments are presented, including a model-as-facet reanalysis, item resampling stability test, multi-hardware separability test, 14B scale extension, RoBERTa fine-tuning study, LayerCast precision mitigation, and MATH benchmark extension. 2. Methodology Assessment 2.1 G-Theory Application The application of G-theory is broadly correct and represents a natural fit for the research question. The crossed random-effects design, with item as the measurement facet and prompt/seed/temperature/ordering/precision as crossed facets, is the canonical G-theory setup for studying measurement dependability. The paper correctly distinguishes G-studies (variance decomposition) from D-studies (projection under alternative designs), which is the primary advantage of G-theory over standard ANOVA. However, there are several methodological concerns: (a) Object of measurement is underspecified.  In classical G-theory, the \\\"object of measurement\\\" (the entity whose score you want to generalize) must be clearly defined. In educational testing, this is typically the person. Here, the paper appears to treat benchmark accuracy as the object, but accuracy is an aggregate over items -- not a single observation. The paper decomposes item-level binary responses (correct/incorrect), which means the effective object of measurement is the  item-level response . The G coefficient then measures how well item-level responses generalize across facet conditions. This is a valid but nonstandard application. The paper should explicitly state what universe score is being estimated and what generalization is being made. The current framing conflates \\\"reliability of a benchmark score\\\" with \\\"stability of item-level responses across conditions,\\\" and these are different quantities. (b) Model-as-fixed vs. model-as-facet transition is handled well but incompletely.  The paper correctly identifies that pooling across models inflates item_ id (from 56% to 49.2% on MMLU when model is added as a facet). The model x item interaction (10.2%) is properly extracted. However, the paper does not discuss whether model should be treated as random or fixed from a G-theory perspective. With only 4 models drawn from a specific population (7-9B instruction-tuned open-weight models), the \\\"random\\\" assumption implies these 4 are a random sample from some universe of models -- a dubious claim given the deliberate selection. If model is fixed, model x item is not an error component but a systematic interaction, and the G coefficient computation changes. The paper should discuss this inferential scope issue. (c) Henderson Method I vs. III naming inconsistency.  The paper claims \\\"Henderson's Method III (expected mean squares)\\\" in Section 3.1, but the balanced fully-crossed design used here would typically employ Henderson Method I (which uses Type-I sums of squares and expected mean squares for balanced designs). Method III is Searle's approach for unbalanced designs. For the balanced design in exp-001, Method I is both simpler and more appropriate. This is either a naming error or an implementation concern -- the paper should clarify which method was actually used and verify consistency with the code. (d) Binary response variable creates floor/ceiling artifacts.  All primary analyses use binary correct/incorrect as the response. For items near 0% or 100% accuracy across conditions, variance is mechanically compressed (a Bernoulli variable with p near 0 or 1 has low variance). This means item_ id partially reflects the  range  of item difficulties rather than genuine measurement-relevant variance. The logprob analysis in Appendix B (item_ id drops to 42.8%) partially addresses this, but it is relegated to a 4-line appendix rather than being integrated into the main analysis. A continuous response variable would provide a more principled decomposition, and the paper should discuss the implications of using binary outcomes for variance component estimation. 2.2 Crossed/Nested Design Appropriateness The fully crossed design for MMLU (exp-001) is the gold standard for G-theory and is correctly specified. All facet levels are combined with all other facet levels, enabling clean estimation of all main effects and two-way interactions. The reduced designs for non-MMLU benchmarks (2 precisions x 2 temperatures vs. 3 x 3 for MMLU) are a pragmatic budget-driven decision but create a methodological asymmetry that is inadequately discussed. Variance percentages are  relative to total variance , and the total variance changes when you remove facet levels. Removing the FP32 precision level (which shows the highest deviation post-confound-fix) and the third temperature level changes the denominator of all percentage calculations. The cross-benchmark gradient (Table 4) compares percentages from designs with different factorial structures, which is a validity concern. The paper should either: (a) report a sensitivity analysis re-running MMLU with the reduced 2x2 design to confirm the gradient holds under matched designs, or (b) explicitly discuss why the design asymmetry does not invalidate the comparison. 2.3 Bootstrap Procedures The bootstrap procedure (1,000 item-level resamples) is appropriate in principle for constructing CIs on variance components, as parametric CIs for variance components in mixed models are notoriously unreliable. However: (a) Resampling items with replacement in a balanced design creates duplicates.  With 200 items and replacement, each bootstrap draw contains approximately 127 unique items (by the coupon collector / birthday problem). Duplicate items have identical response vectors across all conditions, violating the independence assumption in the ANOVA decomposition. This likely  deflates  the variability of item_ id estimates (making CIs too narrow), because the resampled datasets have artificially correlated item effects. A cluster bootstrap that resamples item-condition blocks without re-indexing duplicates, or a delete-d jackknife, would be more appropriate. The tight CI widths (4-6pp) should be interpreted with this caveat. (b) Nested bootstrap for D-study projections is not described.  The D-study projections in Table 11 presumably require computing variance components for each bootstrap sample and then projecting G under hypothetical designs. This is a two-stage procedure (bootstrap variance components -> project G), and the uncertainty in G projections depends on the joint distribution of all variance components, not just item_ id. The paper reports CIs on item_ id but not on D-study projections. The claim that \\\"420 items suffice for G >= 0.90 on MMLU\\\" has no associated uncertainty -- but given the bootstrap CIs on item_ id (46.1-52.3%), the projected item count for G >= 0.90 could range substantially. This uncertainty should be reported. 3. Experimental Rigor 3.1 Exp 1b: Item Resampling Stability The resampling stability test uses 1 model (Llama-3.1-8B) x 1 benchmark (MMLU) x 3 independent 200-item samples x 54 conditions per sample = 32,400 records. The CV of 4.1% on item_ id across samples is reassuring but has limited generalizability: -  Only 1 model tested.  The paper claims item resampling stability as a general property, but models with different accuracy distributions (e.g., Mistral-7B at 64.1% vs. Gemma-2 at 69.1%) might show different resampling sensitivity. A model near the population mean difficulty could show lower CV than one at the extremes. -  Only 3 samples.  A CV computed from 3 data points has essentially no statistical power. The standard error of a CV from n=3 is enormous. The paper would be better served by reporting the bootstrap distribution of variance components (which they have from exp-004, 1000 resamples) as the stability analysis, rather than the 3-sample CV. -  Only MMLU.  The critical question is whether resampling stability holds for GSM8K and MATH, where item_ id is much lower (21-25%) and closer to competing components. A CV of 4.1% on a 55% estimate is comfortable (55 +/- 2.3pp). But a CV of 4.1% on a 21% estimate would be 21 +/- 0.9pp -- still rank-1, but now within striking distance of temp x item at 20.8%. The resampling stability argument is weakest precisely where it matters most (reasoning benchmarks), and it is not tested there. Recommendation:  Replace the 3-sample CV with the bootstrap CI analysis from exp-004, and extend item resampling stability to at least one reasoning benchmark (GSM8K or MATH). 3.2 200-Item Sample Size Using 200 stratified items per benchmark is a reasonable choice that balances statistical power against computational cost. The stratification (by MMLU subject, presumably by difficulty for other benchmarks) ensures representative coverage. However: -  For MMLU (14K total items), 200 items is 1.4% of the pool -- adequate for stable percentage-based decompositions. -  For GSM8K (1,319 items in the test set), 200 items is 15.2% -- a much larger fraction, which reduces the effective resampling space. -  For MATH (5,000 items in the test set), 200 items is 4% -- again adequate. -  For ARC-Challenge (1,172 items), 200 items is 17.1%. The paper does not discuss how the item pool size interacts with the variance decomposition. When sampling 15-17% of the pool (GSM8K, ARC), the resampling stability results from MMLU (1.4% sampling fraction) may not transfer. This should be acknowledged. 3.3 Hardware Experiment (Exp 3): Confounds The multi-hardware study uses 2 GPU types. This is a minimal design for estimating hardware effects. Specific concerns: -  n=2 GPU types provides 1 degree of freedom for the hardware main effect.  This is barely identifiable in a variance decomposition. The hardware main effect (0.4%) and hardware x item (1.6%) estimates are based on between-GPU differences that could reflect any systematic difference between the two specific GPUs (driver version, cooling, memory controller characteristics, vLLM kernel selection), not hardware architecture per se. -  The paper does not specify the second GPU type.  The review context mentions \\\"RTX PRO 6000 + second GPU\\\" but the paper says only \\\"2 GPU types.\\\" For a claim about hardware separability to be meaningful, readers need to know whether these are architecturally similar (e.g., two Ampere-class GPUs) or substantially different (e.g., Ampere vs. Hopper). Two GPUs from the same architecture family would underestimate hardware variance. -  No confound control for driver/CUDA version differences between GPUs.  If the two GPUs run different CUDA toolkit versions or vLLM builds, observed differences reflect the software stack, not the hardware. Despite these limitations, the separability conclusion (<0.3% direct infra x method) is robust: even if hardware variance is underestimated due to limited GPU diversity, the  interaction  with methodology would need to be orders of magnitude larger to matter. The null result is defensible. 3.4 Fine-Tuning Experiment (Exp 6): RoBERTa Using RoBERTa-large for the fine-tuning study is a significant architectural mismatch. The inference experiments use 7-14B decoder-only autoregressive models on generation tasks; the fine-tuning experiment uses a 355M encoder-only model on classification tasks. The facets are also different (learning rate and data shuffle replace prompt template and temperature). This means: -  The cross-paradigm comparison (Table 13) compares variance percentages from incomparable designs. Item_ id being rank-1 in both does not constitute evidence of cross-paradigm generalization -- it could reflect the fact that any assessment with varying item difficulties will show item dominance, which is a tautological property of the design rather than an empirical finding. -  The claim that \\\"infrastructure effects are negligible in fine-tuning too\\\" is trivially expected for RoBERTa-large, which has no autoregressive error accumulation and was trained in FP32/FP16. -  The 1,728 fine-tuning runs (432 per task x 4 tasks) is a reasonable scale, but the number of  items  per evaluation is not specified. If each run evaluates the full dev/test set, the item-level observation count is much larger than 1,728. The experiment adds limited value to the core narrative.  Fine-tuning a decoder LLM (e.g., Llama-3.1-8B with LoRA on GSM8K, crossing seed x learning rate x data shuffle x items) would directly test cross-paradigm generalization. The current RoBERTa experiment tests a different claim entirely: that G-theory can decompose fine-tuning variance in encoder-only classification, which is unsurprising given that the same framework has been used in educational testing (which also involves classification-like assessments). 3.5 14B Scale Extension (Exp 5) With n=2 models (Qwen3-14B, DeepSeek-R1-Distill-14B), this experiment has minimal statistical power for any claim about scale effects. The two models differ in both scale and architecture: DeepSeek-R1-Distill-14B is a reasoning-distilled model with fundamentally different training objectives than Qwen3-14B. Scale and training methodology are fully confounded. The finding that both 14B models fall within the 8B range for item_ id is reassuring but does not demonstrate scale invariance -- it demonstrates that these two specific 14B models have similar variance profiles to the four 8B models. The elevated temp x item (8.8%) and seed x item (5.2%) for DeepSeek-R1-Distill-14B is attributed to \\\"reasoning distillation introducing implicit chain-of-thought tendencies\\\" (Section 8.1) -- this is a plausible but untestable hypothesis from n=1. The experiment contributes at best weak corroborating evidence. Two more 14B models (ideally from different training paradigms) would make the scale claim credible. 3.6 LayerCast (Exp 7) This is a null result experiment: LayerCast adds 0.03% precision variance, which is negligible. The experiment is methodologically clean but its contribution is marginal -- it confirms that precision is not a major concern (already established by exp-001 post-confound-fix) and evaluates a specific mitigation technique. For the paper's core claims, it is dispensable. Its inclusion creates a breadth-over-depth tradeoff that weakens the overall narrative. 4. Statistical Concerns 4.1 CV = 4.1% from 3 Samples The original review context described CV = 33% from 3 samples -- the paper now reports CV = 4.1%, which is a dramatic improvement, presumably reflecting better stratification and larger item counts in the revised design. However, a CV computed from n=3 is a point estimate with essentially no precision. The 95% CI on a CV from 3 observations is extremely wide (roughly 0.7x to 5x the point estimate under normal assumptions). The paper should not present CV = 4.1% as a precise number but rather as \\\"CV  < 15%\\\" or similar bounded claim. 4.2 Bootstrap with 1,000 Resamples 1,000 bootstrap resamples is adequate for percentile-based 95% CIs (Monte Carlo error approximately 0.5pp for the tail quantiles). The concern is not the number of resamples but the resampling unit: resampling items with replacement in a balanced design creates duplicate observations that violate independence assumptions in the ANOVA decomposition used within each bootstrap iteration. This is a known problem in bootstrap variance component estimation. The bias direction is toward underestimating CI width. 4.3 D-Study Projection Uncertainty D-study projections are deterministic functions of variance components: given estimated components, the projected G under any hypothetical design is a closed-form calculation. The uncertainty comes entirely from the variance component estimates. The paper reports CIs on item_ id (Table 8) but not on D-study projections. This is a significant omission. The practical recommendation \\\"use 420 items for G >= 0.90 on MMLU\\\" has no associated uncertainty band. If item_ id is at the upper end of its CI (52.3%), more items are needed; if at the lower end (46.1%), fewer suffice. The authors should propagate bootstrap uncertainty through the D-study projection to report a CI on the required item count. 4.4 D-Study Projection for GSM8K: Arithmetic Anomaly Table 10 shows that reducing items from 200 to 150 while keeping prompts=3 and seeds=10  increases  G from 0.68 to 0.90. In the G formula, reducing n_ items should  decrease  G (because item-related error terms are divided by n_ items). The only way G can increase with fewer items is if the optimization simultaneously changes other facet counts or if the table presents results from a joint optimization that is not monotonic in each facet individually. This anomaly is not explained and raises questions about the D-study optimization procedure. If the procedure involves multi-facet grid search, it should be documented; if it is an error, it should be corrected. 5. Coverage vs. Depth The paper runs 8 experiments across 20 tables. Several experiments feel thin: -  Exp 5 (14B):  n=2 models, confounded scale/architecture, 1 paragraph of analysis. Contributes weak corroboration. -  Exp 7 (LayerCast):  Null result for a specific mitigation technique. One table, 1 paragraph. Could be a footnote. -  Exp 6 (Fine-tuning):  Architecturally disjoint from the main study. Two tables, 2 paragraphs. The cross-paradigm claim it supports is unsustainable with encoder-only models. Recommendation:  Move Exp 5, 6, and 7 to an appendix. Use the freed space for: (a) figures -- the paper has zero figures, which is a critical presentation weakness for a variance decomposition study; (b) deeper analysis of the core gradient (Exp 1+2+8), including per-item analysis showing which items drive the benchmark-conditional variance shift; (c) D-study sensitivity analysis with propagated bootstrap uncertainty. Fewer, deeper experiments would produce a stronger paper. The current breadth creates an impression of thoroughness but at the cost of inadequate depth on several secondary experiments. 6. Strengths -  Cross-benchmark variance gradient is a genuine contribution.  The monotonic shift from item-dominated (56%) to interaction-dominated (21%) across five benchmarks, with non-overlapping bootstrap CIs, is novel, well-supported, and explanatory. It resolves the apparent contradiction between prior single-benchmark studies. -  Experimental scale is impressive.  Over 1M records for the MMLU full-factorial alone; approximately 3-4M total. This is among the largest factorial designs in the LLM evaluation literature. -  Engine confound discovery is independently valuable.  The identification and correction of the vLLM FP32/BF16 engine routing difference (V1 CUDA graph vs. V0 eager) is a methodological contribution that benefits any researcher using vLLM for precision-sensitive comparisons. -  D-study facet effectiveness inversion is the most actionable finding.  Items:seeds ratio shifting from 14.2:1 (MMLU) to 0.8:1 (GSM8K) has direct practical implications. This is the quantitative crystallization of \\\"no universal recipe.\\\" -  Model-as-facet reanalysis properly handles model heterogeneity.  Extracting model x item (10.2% on MMLU) while preserving item_ id as rank-1 and the gradient is a clean analytical move that addresses a legitimate concern from prior reviews. -  Separability confirmation is useful.  While a null result, confirming  <0.3% direct infrastructure x methodology interaction across all benchmarks provides empirical license for isolated-factor study designs. -  REML vs. Henderson sensitivity analysis  with  <1.4pp divergence and identical component rankings adds robustness. -  Item resampling stability  (despite the n=3 limitation) provides evidence that the variance structure is not an artifact of specific item selection. 7. Weaknesses Major -  (W1) D-study optimization procedure is undocumented.  The joint-optimal allocations in Table 11 (e.g., GSM8K: 150 items, 3 prompts, 10 seeds) appear to come from a multi-facet grid search, but the paper describes only single-facet D-study sweeps. The GSM8K anomaly (150 items yielding G=0.90 while 200 items with the same prompts/seeds yields G=0.68) is unexplained and arithmetically suspicious. Practitioners will use these specific numbers; they must be derived from a transparent procedure. -  (W2) Object of measurement and G coefficient interpretation.  The paper conflates the G coefficient (which measures generalizability over included facets relative to the universe of admissible observations) with overall measurement reliability. G = 0.22 for \\\"current practice\\\" on MMLU does not mean MMLU is unreliable in a practical sense -- it means that item-level binary responses are not stable across prompt/seed/temperature conditions. Since practitioners use  aggregate accuracy  (averaging over 200+ items and potentially multiple conditions), the effective reliability of the aggregate score is much higher. The paper's alarming framing (\\\"below the minimum threshold accepted in any measurement discipline\\\") risks misleading practitioners by applying item-level G to benchmark-level decisions. -  (W3) Bootstrap resampling with replacement in balanced designs.  Duplicate items in bootstrap samples violate the independence assumption of the within-bootstrap ANOVA, likely producing CIs that are too narrow. This affects the statistical significance claims for the gradient (non-overlapping CIs across benchmarks). The paper should report results from a cluster bootstrap or jackknife as sensitivity analysis. -  (W4) Cross-benchmark design asymmetry.  Comparing variance percentages across benchmarks when MMLU uses 3 precisions x 3 temperatures and others use 2 x 2 is methodologically questionable. The total variance denominator differs, and removing facet levels redistributes percentage shares. No sensitivity analysis is provided. -  (W5) Zero figures.  For a paper about variance decomposition across benchmarks, the absence of any visualization is a critical presentation failure. Stacked-bar charts, D-study projection curves, and bootstrap CI forest plots are standard idioms in this literature and would dramatically improve communication of the key findings. Moderate -  (W6) Fine-tuning experiment (Exp 6) is architecturally mismatched.  RoBERTa-large on classification tasks does not test cross-paradigm generalization to decoder-only LLM fine-tuning. The different facet structure (LR/shuffle vs. prompt/temperature) makes the comparison non-parallel. -  (W7) 14B scale extension (Exp 5) has n=2 with confounded scale/architecture.  Cannot separate scale effects from training methodology effects (reasoning distillation). -  (W8) Item resampling stability tested on only 1 model x 1 benchmark x 3 samples.  Not tested on reasoning benchmarks where the stability claim matters most. -  (W9) Hardware experiment uses only 2 unspecified GPU types.  The second GPU is never identified, and n=2 provides minimal diversity for hardware variance claims. -  (W10) Missing comparison with IRT-based benchmarking.  tinyBenchmarks recommends approximately 100 items for MMLU; the D-study recommends 420. This 4x discrepancy is never discussed. Since both address \\\"how many items suffice?\\\", the paper should explain why the answers differ and what each framework optimizes. 8. Questions for Authors 1.  D-study arithmetic:  In Table 10 (GSM8K), how does reducing items from 200 to 150 (with identical prompts=3, seeds=10) increase G from 0.68 to 0.90? This appears to violate the monotonicity of G in n_ items. Please describe the exact optimization procedure and verify these numbers. 2.  Object of measurement:  What is the universe score being estimated? Is it the expected accuracy of a model on the full item population, or the expected item-level response across all facet conditions? These yield different G coefficients, and the practical implications differ substantially. If the former, how do you handle the aggregation from items to benchmark score in the G formula? 3.  Bootstrap validity:  Have you conducted any calibration study (e.g., comparing bootstrap CIs to parametric REML-based CIs or to a delete-d jackknife) to verify that your bootstrap procedure produces correct coverage? Given the duplicate-item concern, what is the effective number of unique items per bootstrap sample, and have you assessed whether this deflation affects CI width? 4.  Design asymmetry:  If you re-run the MMLU analysis using only 2 precisions (BF16/FP16) and 2 temperatures (matching the non-MMLU design), does item_ id remain at approximately 56%, or does it shift? How large is the shift, and does the gradient survive with matched designs across all benchmarks? 5.  G interpretation for practitioners:  Your D-study says MMLU needs 420 items for G >= 0.90. But the standard MMLU evaluation uses the full 14K items with 1 prompt and 1 seed. What is the G coefficient for the full 14K-item, 1-prompt, 1-seed evaluation? If it is already above 0.90 (which it likely is, given that item-related error shrinks with 70x more items), the practical alarm about \\\"current practice being inadequate\\\" is overstated. 9. Score Score: 4/6 (Weak Accept) Justification:  The paper presents a large-scale, technically competent G-theory analysis with a genuinely novel primary finding (the cross-benchmark variance gradient) that has both explanatory and practical value. The engine confound discovery is independently valuable. The D-study facet effectiveness inversion is the most actionable result. However, several methodological concerns prevent a higher score: (a) the D-study optimization procedure contains an unexplained arithmetic anomaly and is not documented; (b) the G coefficient interpretation risks misleading practitioners by conflating item-level generalizability with benchmark-level reliability; (c) the bootstrap procedure has a known bias from duplicate items in balanced designs; (d) the cross-benchmark gradient is derived from designs with different factorial structures; (e) secondary experiments (Exp 5, 6, 7) are thin and architecturally mismatched. The core contribution -- the gradient + D-study reversal -- merits publication, but the paper needs honest scoping of what its G coefficients actually measure, documented D-study optimization, design-matched gradient validation, and figures. 10. Confidence Confidence: 4/5 I have working knowledge of G-theory (Brennan 2001, Shavelson & Webb 1991), variance component estimation methods (Henderson, REML), bootstrap procedures for mixed models, and the LLM evaluation reproducibility literature. My main uncertainty is whether the D-study anomaly in Table 10 reflects a multi-facet optimization procedure that I am not recognizing, and whether the binary-response decomposition introduces biases beyond what I have identified. I am confident in the assessment of the experimental design, the bootstrap validity concern, and the G coefficient interpretation issue.\\n[05-20 23:51] cli_a974499e77fadbdd: 🌙  [Dream Review Report — worst | dream_20260520T222113]  · Overall: 3 — Weak Reject Review Report — Reviewer R2 (Novelty, Significance, Positioning, Writing) Paper:  \\\"Variance Decomposition Is a Measurement, Not a Fact: On the Instability of Reproducibility Budgets for LLM Evaluation\\\" Tier:  worst 1. Novelty Assessment 1a. \\\"Variance decomposition is a measurement\\\" framing This framing is  not novel in psychometrics or the broader measurement sciences . The instability of variance component estimates under resampling is a well-known phenomenon in G-theory. Brennan (2001, Ch. 8) explicitly discusses sampling variability of variance components and recommends bootstrap or jackknife standard errors. Shavelson & Webb (1991) note that component estimates depend on facet sample size and the specific levels sampled. The educational measurement literature has used resampling stability checks for decades (e.g., Cardinet, Johnson, & Pini, 2010). The paper presents this as a discovery (\\\"we set out to build budgets and discovered the budget is unreliable\\\"), but anyone trained in G-theory would expect variance component estimates to have sampling distributions. The CV=33% finding is noteworthy in the LLM context, but the epistemological claim is standard measurement theory repackaged as a revelation. Verdict:  The framing is novel  for the ML audience  but risks appearing naive to measurement-literate reviewers. The contribution is empirical (documenting the magnitude of instability in LLM evaluation), not conceptual. 1b. Model-as-facet vs. model-as-fixed This is  standard G-theory practice , not a novel insight. The distinction between random and fixed facets is one of the first topics covered in any G-theory course. Whether to treat a facet as random or fixed depends on whether one wants to generalize beyond the specific levels observed. Mesting (2026) treating model as fixed is a defensible design choice (she studies a specific set of models), not an error. The paper's claim that prior work \\\"inflates\\\" item variance by treating model as fixed conflates a design decision with a methodological flaw. The 22pp shift is informative but expected: adding any large facet as random will redistribute variance from existing components. Verdict:  The finding quantifies a known effect in a new domain. Useful, but cannot be positioned as a methodological contribution. 1c. Item resampling instability This is the paper's strongest novelty claim. To my knowledge,  no prior ML evaluation study has explicitly tested the resampling stability of variance components . Bouthillier et al. (2021) and Mesting (2026) report point estimates without stability analysis. The demonstration that CV=33% with rank inversions across item samples is a genuinely useful empirical contribution. However, the magnitude of the CV depends heavily on design specifics (200 items from a 14,000-item pool with heterogeneous subject difficulty is expected to produce high variability). With 3 resamples, the CV estimate itself is poorly estimated (the standard error of a CV from n=3 is enormous). The paper needs 10+ resamples to make the CV=33% claim credible. Verdict:  Novel for ML evaluation. Underpowered (only 3 resamples to estimate a CV). The contribution is real but the specific numbers are unreliable. 1d. Bimodality-item_ id correlation (r=0.95) This is  potentially interesting but mechanistically trivial  and computed from only 5 data points. An r=0.95 from n=5 has a 95% CI of approximately [ 0.63, 0.99 ] under Fisher's z, so it is not as precise as it appears. More importantly, the relationship is tautological at its core: benchmarks with more variable item difficulties (bimodal = some very easy, some very hard) will necessarily produce more item-level variance. This is a mathematical near-identity, not an empirical finding. Verdict:  The correlation is real but trivially expected from the definition of item variance. Not a meaningful contribution. 2. Positioning Against Related Work 2a. Critique of Mesting (2026) and Brittlebench (2026) The critique is  partially fair but overstated . The paper claims (lines 43-50) that \\\"every prior study that reports a single variance decomposition without resampling stability analysis has, in effect, presented one draw from a high-variance distribution as a finding.\\\" This is true in principle but uncharitable. Mesting's study uses a large item set and reports REML standard errors (which capture estimation uncertainty within a fixed design). Brittlebench uses a different framework entirely (not G-theory). The paper implies these studies are fundamentally flawed rather than acknowledging that they answer different questions with different assumptions. The claim that \\\"if Mesting had used different items, her 43.8% judge-dominance estimate might have been 30% or 55%\\\" (line 245) is speculative. Mesting's study uses different benchmarks with different item pool sizes; the CV from MMLU does not transfer directly. 2b. Missing related work Several important references are absent: -  Cardinet, Johnson, & Pini (2010) : \\\"Applying Generalizability Theory using EduG\\\" — directly addresses variance component stability and CIs in G-theory -  Webb, Shavelson, & Haertel (2006) : Reliability coefficients and G-theory, including sampling variability of components -  Marcoulides (1999) : On the sampling variability of G-theory estimates -  Multiverse analysis literature  (Steegen et al., 2016): The \\\"analyst degrees of freedom\\\" argument has been made more rigorously in the multiverse framework -  Differential item functioning (DIF) literature : The model×item interaction is essentially DIF — items that function differently across subpopulations (here, models). This connection to the psychometric DIF literature is completely unmade. -  Bell (2010)  and other G-theory sampling papers in educational measurement The paper cites Brennan and Shavelson/Webb as canonical references but does not engage with the substantial G-theory literature on exactly the problem it claims to discover (component sampling variability). 2c. Distinction from Bouthillier et al. (2021) Adequately distinguished. The paper correctly notes that Bouthillier uses ANOVA without D-study projections. The distinction is clear. 3. Significance and Impact 3a. Would these findings change evaluation practice? Partially.  The resampling instability finding (Claim 1) should prompt researchers to report bootstrap CIs on variance components — this is a useful methodological recommendation. The model-as-facet finding (Claim 2) is relevant but its practical implication is unclear: most evaluation studies compare specific models, making model-as-fixed appropriate by design. The D-study CI finding (Claim 3) is a legitimate concern but the practical response (\\\"report uncertainty on budgets\\\") is straightforward. 3b. Is \\\"budgets need error bars\\\" actionable? Yes, but it is a modest recommendation.  The paper essentially says: report confidence intervals on your variance component estimates and D-study projections. This is standard statistical practice that has been advocated in psychometrics for decades. The novelty is in showing that the ML community has not been doing it, which is valuable but incremental. 3c. Solutions vs. diagnosis The paper is almost entirely diagnostic.  It identifies problems (instability, model specification sensitivity, CI width) but provides no solutions. It does not propose better estimation methods, more stable designs, or alternative frameworks. The three recommendations in the conclusion (report CIs, use model-as-facet, report uncertainty on budgets) are methodological hygiene points, not solutions to the underlying instability. 4. Writing Quality 4a. Narrative pivot The pivot from \\\"we set out to build budgets\\\" to \\\"the budget itself is unreliable\\\" is  well-executed rhetorically  but raises credibility concerns. Was this genuinely a surprise discovery, or was the \\\"failed hypothesis\\\" narrative constructed post-hoc to make negative results publishable? The paper framing document reveals this was indeed a pivot after the cross-benchmark gradient hypothesis failed. The pivot is honest, but the resulting narrative feels contrived — the paper is essentially a collection of negative/null results (no gradient, unstable components, wide CIs) reframed as meta-methodological insights. 4b. Paper length and bloat The paper is too long for its content density.  8 experiments across what would be 13+ pages is excessive. Specific concerns: -  Experiment 5 (14B extension) : Adds very little. With n=2 models and scale/architecture confounded, the finding that item dominance is \\\"lower for 14B\\\" is uninterpretable. This should be cut or relegated to a 2-line appendix mention. -  Experiment 7 (LayerCast) : Confirms precision is not a first-order concern — a finding already established in Experiment 1 after confound correction. Adds  <2% variance. Should be cut. -  Experiment 6 (fine-tuning) : Uses RoBERTa-large, a fundamentally different setting from LLM inference evaluation. The finding that learning rate dominates (instead of item) in fine-tuning is unsurprising and disconnected from the main narrative. The low correlation between inference and fine-tuning variance structures (r=0.18) is the only noteworthy point, and it could be a 3-sentence appendix finding. The paper would be stronger at 8-9 pages with Experiments 1, 1b, 2, 3, and 4 only. 4c. Table density 18 tables with no figures  is a severe presentation problem. The paper violates its own field's conventions (distilled writing patterns call for stacked-bar decomposition figures as the \\\"signature visual\\\"). The absence of any figure makes the paper visually impenetrable and prevents readers from grasping patterns at a glance. At minimum, the paper needs: (1) a stacked-bar variance decomposition across benchmarks, (2) a D-study projection curve, and (3) a resampling stability visualization. 5. Framing Concerns 5a. Is \\\"measurement error exists in variance decomposition\\\" surprising enough? No, not for a top venue.  This is a well-known concern in psychometrics. The contribution is showing its magnitude in LLM evaluation, which is useful but incremental. The paper would need to either (a) show that the instability is catastrophically worse than expected from theory, or (b) propose a solution that substantially improves practice. It does neither. 5b. Does the paper overclaim? Yes, in several places: -  \\\"Every prior study that reports a single variance decomposition...has presented one draw from a high-variance distribution as a finding\\\" — this over-generalizes from MMLU to all measurement settings -  \\\"Model×item interaction (33%) is the single largest overlooked component\\\" — whether it is \\\"overlooked\\\" depends on the research question; treating model as fixed is a legitimate design choice when comparing specific models -  \\\"Rendering benchmark-specific budget recommendations statistically meaningless\\\" — the CIs are wide but the point estimates are still informative; \\\"meaningless\\\" is too strong -  The title \\\"Variance Decomposition Is a Measurement, Not a Fact\\\" implies prior work treated decompositions as facts — most measurement researchers know they are estimates 6. Strengths and Weaknesses Strengths -  S1.  The resampling instability analysis (Exp 1b) is a genuinely novel contribution to ML evaluation methodology, even if the concept is known in psychometrics -  S2.  Large scale: 4 models, 5 benchmarks, multiple facets crossed — the most comprehensive G-theory study of LLM evaluation to date -  S3.  The engine confound discovery and correction (V0 enforce_ eager) is a valuable methodological contribution that benefits the community -  S4.  The model-as-facet reanalysis, while methodologically standard, provides useful quantification of model×item interaction magnitude in LLM evaluation -  S5.  The bimodality mechanism linking difficulty distribution shape to item dominance is intuitive and potentially useful for benchmark designers -  S6.  The REML vs. Henderson comparison adds a useful sensitivity dimension -  S7.  The pivot narrative is intellectually honest — admitting the gradient hypothesis failed Weaknesses -  W1.  The central framing claim (\\\"variance decomposition is a measurement, not a fact\\\") is well-established in psychometrics; presenting it as a discovery undermines credibility with measurement-literate reviewers -  W2.  Only 3 item resamples to estimate CV — the CV=33% figure is itself highly uncertain; need 10+ resamples for credible estimation -  W3.  No figures at all — 18 tables with zero visualizations makes the paper nearly unreadable -  W4.  Experiments 5, 6, and 7 contribute little and bloat the paper; the fine-tuning study (RoBERTa) is too far from the LLM inference setting -  W5.  The paper is purely diagnostic — no solutions, no improved methods, no practical tools beyond \\\"report CIs\\\" (standard advice) -  W6.  The critique of prior work is uncharitable: treating model as fixed is a design choice, not an error; Mesting reports REML SEs -  W7.  The non-gradient result (Exp 2, 8) is presented as meaningful, but 9pp spread across 5 benchmarks under model-as-fixed is expected given resampling instability — this is a null result, not a finding -  W8.  The bimodality correlation (r=0.95 from n=5) is both statistically underpowered and mechanistically tautological -  W9.  Missing engagement with the substantial psychometric literature on variance component sampling variability (Cardinet et al., Marcoulides, Webb et al.) -  W10.  The paper's three claims are essentially three ways of saying \\\"variance estimates are uncertain\\\" — this is one finding, not three 7. Questions for Authors 1.  On resampling stability : With only 3 item resamples, your CV=33% estimate has enormous uncertainty. What is the bootstrap standard error of the CV itself? Have you considered running 30+ resamples to produce a credible estimate? Would the CV decrease with larger item samples (e.g., 500 items from the 14,000-item MMLU pool)? 2.  On model-as-facet : You argue that treating model as fixed \\\"inflates\\\" item variance. But if a practitioner wants to evaluate a specific model (the common use case), treating model as fixed is correct by design — the goal is not to generalize to unseen models. Under what practical scenario is model-as-random the appropriate specification? How do you respond to the argument that model×item interaction is simply model-specific item difficulty, which is exactly what practitioners care about? 3.  On the non-gradient : Your original hypothesis was a cross-benchmark gradient from knowledge to reasoning. This failed (spread=9pp, non-monotonic). You then pivoted to \\\"the budget itself is unreliable.\\\" If the gradient had been confirmed, would you still have discovered the instability? Does the pivot undermine the claim that instability is the \\\"centerpiece\\\" finding, or was it only noticed because the primary hypothesis failed? 4.  On separability : You report that separability fails on GSM8K (4.5% infra×method) and with hardware (5.5%). But 4-5% is arguably still small in absolute terms. What threshold makes separability \\\"fail\\\"? Is there a principled way to set this threshold, or is the \\\"failure\\\" framing a judgment call? 5.  On engagement with psychometrics : Your central claim — that variance components are estimates with sampling distributions — is standard in the G-theory literature (Brennan 2001 Ch.8, Cardinet et al. 2010). Why does the paper not engage with this prior work? How does the observed CV=33% compare to typical component instability in educational measurement applications of G-theory? 8. Score Score: 3 (Weak Reject) Justification:  The paper addresses a relevant question (stability of variance decomposition in LLM evaluation) and provides useful empirical data at scale. However, the central conceptual contribution — that variance components are estimates with error — is well-established in psychometrics and cannot be claimed as novel. The paper is purely diagnostic with no solutions beyond standard statistical hygiene recommendations. The resampling analysis (the strongest contribution) is underpowered at n=3 samples. The presentation is severely hampered by 18 tables and zero figures. Experiments 5-7 add bulk without proportional insight. The framing overreaches: treating model-as-fixed as an \\\"error\\\" rather than a design choice, claiming prior work treats decompositions as \\\"facts,\\\" and declaring benchmark-specific budgets \\\"meaningless.\\\" For a top venue with ~ 25% acceptance, the paper needs either a substantially novel conceptual contribution or a practical solution, and it provides neither. The empirical findings (resampling CV, model×item magnitude) are useful contributions that would strengthen a paper with a more modest framing, but the current framing invites expert pushback. 9. Confidence Confidence: 4/5 I have substantial familiarity with both G-theory (through educational measurement applications) and LLM evaluation methodology. I have read the primary references (Brennan 2001, Shavelson & Webb 1991, Bouthillier et al. 2021) and am familiar with the variance component sampling variability literature. I am less certain about the specific numerical claims (I cannot verify the 4M observations or the exact variance decomposition numbers), but the methodological assessment is on firm ground.\\n[05-20 23:46] cli_a974499e77fadbdd: 🌙  [Dream Review Report — median | dream_20260520T222113]  · Overall: Weak Accept (4/6) Dream Review Report —  dream_20260520T222113  (median tier) Paper Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics Review Panel -  R1 : Methods & Experiments -  R2 : Novelty & Related Work 1. Independent Reviews R1: Methods & Experiments — Score 4/6 (Weak Accept), Confidence 4/5 Summary : The paper conducts a large-scale G-theory analysis crossing infrastructure with methodology facets across 5 benchmarks and 6 models (~ 3M+ observations). The experimental design is ambitious and the numerical results are internally consistent. However, several technical methodology issues undermine confidence. Strengths : 1.  Internal numerical consistency across all 15 tables is excellent — variance components sum correctly, cross-references between tables are coherent, and the model-as-facet correction systematically reduces item_ id by ~ 4pp across all benchmarks. 2.  The cross-benchmark gradient finding (item_ id: 48% MMLU → 28% MATH) is well-supported with bootstrap CIs showing non-overlapping intervals at endpoints (permutation p=0.003). 3.  The engine confound correction (V0 enforce_ eager eliminating the 0.22pp BF16 eager artifact) is a genuine standalone contribution that prevents other researchers from attributing engine-routing variance to precision effects. 4.  Experimental scale is impressive: 9 experiments, 5 benchmarks, 6 models, 2 GPU architectures, 3 scoring metrics. 5.  Item resampling stability analysis (Table 3) honestly quantifies the sampling uncertainty in item_ id estimates (CV=0.19) and correctly reports ranges rather than point estimates. Weaknesses : 1.  D-study optimization procedure is undocumented : Table 9 reports joint-optimal facet allocations (e.g., MMLU: 420 items, 3 prompts, 4 seeds for G≥0.90) but the paper does not describe how joint optimization across multiple facets was performed. Standard D-study sweeps one facet at a time while holding others fixed. If grid search was used, the search space and stopping criteria should be stated. This is critical because practitioners will use these numbers directly. 2.  G coefficient interpretation conflates with overall reliability : The paper presents G=0.37 (binary) as indicating \\\"substantial unreliability\\\" of MMLU. But G-theory's G coefficient measures generalizability over the  facets included in the design , not overall measurement quality. Since the universe of generalization includes only the specific facets crossed, the low G primarily reflects high item-sampling error, not that MMLU is unreliable in practice (where items are fixed). The paper should distinguish G as a design property from reliability as a benchmark property. 3.  Observation count claim : The abstract says \\\"over 3 million\\\" observations. Summing across experiments: MMLU ~ 1.04M + multi-benchmark ~ 1.15M (3×384K) + hardware ~ 1.15M + 14B unclear + fine-tuning ~ 1,728 runs (not observations) + MATH + LayerCast. The total depends on overlap assumptions (exp-004 reanalyzes existing data). The claim should be precisely itemized. 4.  MATH variance decomposition : Table 6 shows item_ id=28% for MATH (model-as-facet), but temp:item (14%) + seed:item (11%) = 25%, nearly matching item_ id. The paper does not adequately discuss that for MATH, item dominance is barely maintained — on a per-model basis, temperature×item may exceed item_ id for some models, weakening the \\\"item_ id always ranks #1\\\" claim. 5.  Missing details for replication : (a) Which 6 prompt templates were used? (b) What stratification procedure for 200 items across 57 MMLU subjects? (c) How were \\\"200 MATH items\\\" selected given MATH's difficulty distribution? (d) What temperature values (three temperatures stated but values not given)? These omissions make exact replication impossible. Questions for Authors : 1.  For the D-study projections, was the optimization over (items, prompts, seeds) done via exhaustive grid search or analytical formula? What were the grid bounds? 2.  Table 6 shows MATH prec:item and precision main as \\\"—\\\" (missing). Is this because the MATH experiment used only BF16/FP16 with insufficient precision levels for stable estimation? 3.  The bootstrap procedure resamples items × conditions. Are conditions resampled with replacement within the factorial structure, or is the bootstrap at the cell level? 4.  How does the G coefficient change if you remove the 3-way and higher interaction terms from the error variance? The 9% \\\"other 2-way/3-way\\\" in Table 1 is non-trivial. R2: Novelty & Related Work — Score 4/6 (Weak Accept), Confidence 4/5 Summary : The paper applies G-theory to multi-benchmark LLM evaluation, discovering a benchmark-conditional variance gradient and producing D-study reproducibility budgets. The cross-benchmark gradient is the genuine novel contribution; the infrastructure×methodology crossing — framed as the key methodological advance — yields near-null results. Strengths : 1.  The cross-benchmark variance gradient (item_ id: 48% → 28% from knowledge to proof reasoning) is genuinely novel. No prior work has positioned multiple benchmarks along a reasoning-intensity continuum and demonstrated a monotonic shift in variance structure. The unifying explanation — that prior single-benchmark studies reached contradictory conclusions because they studied benchmarks at different gradient positions — is insightful. 2.  The D-study budget differentiation is non-obvious and actionable: MMLU is item-limited while GSM8K is seed-limited, directly challenging the assumption that evaluation protocols can be standardized. 3.  Honest positioning of contributions. The paper correctly frames separability as confirmatory, acknowledges that item dominance is psychometrically expected, and scopes infrastructure to numerical precision. This intellectual honesty is appreciated. 4.  The G  < 0.37 finding for standard MMLU evaluation practice is an important indictment of current evaluation norms, framed in measurement-theory language that connects NLP to established psychometric standards. 5.  The experimental scale (3M+ records, 9 experiments) substantially exceeds both Mesting (2026, single benchmark) and all prior isolated-factor studies. Weaknesses : 1.  Infrastructure crossing yields near-null results, hollowing the novelty narrative : The introduction frames \\\"crossing infrastructure with methodology in a unified G-theory framework\\\" as a key gap filled. But infra×method < 0.5% on knowledge benchmarks means this crossing contributes essentially nothing to understanding. The three genuine findings (gradient, D-study reversal, G  < 0.37 indictment) would all emerge from a methodology-only design replicated across 5 benchmarks. The GSM8K exception (3%) partially rescues this, but the paper oversells the infrastructure crossing relative to its contribution. 2.  Missing critical related work :   -  No comparison with IRT-based item selection (tinyBenchmarks recommends ~ 100 items for MMLU vs. this paper's 420 for G≥0.90 — the 4× discrepancy is never discussed)   -  ThinkingMachines (2025) on batch-invariance failure in GEMM/attention kernels is directly relevant to the seed×item interaction mechanism   -  No engagement with Kunievsky & Evans (2025) alternative variance decomposition framework   -  15 references is thin for a venue submission of this scope 3.  \\\"First multi-benchmark G-theory analysis\\\" claim is narrow : Bouthillier et al. (2021) performed ANOVA-based variance decomposition across multiple ML benchmarks. The difference is \\\"G-theory (not ANOVA) applied to LLM evaluation (not ML generally) across multiple benchmarks.\\\" This is a narrow novelty window. 4.  Three-tier benchmark clustering is post-hoc : The ordering (knowledge > commonsense > reasoning) was presumably determined after observing results. An independent measure of \\\"reasoning intensity\\\" (e.g., average CoT length, multi-step count) would make the continuum principled rather than constructed. A 6th benchmark might not fall on the line. 5.  Zero figures is a critical presentation failure : 15 tables and no figures in a variance decomposition paper. Stacked-bar decomposition charts are the expected field idiom. The cross-benchmark gradient demands visualization. D-study projection curves would communicate the budget reversal far more effectively than tables. At a top venue, this is a significant competitive disadvantage. 6.  Fine-tuning G-study (Section 4.10) is architecturally disjoint : RoBERTa-large encoder fine-tuning uses different facets (LR, data shuffle) from the decoder inference study (prompt, temperature). The finding that \\\"infrastructure is negligible in fine-tuning too\\\" is unsurprising. The cross-paradigm generalization claimed is weak. 7.  IRT comparison is a missed opportunity : D-study budgets claim to be \\\"an alternative to IRT subsampling\\\" but never compare against actual IRT recommendations. If tinyBenchmarks and D-study agree, G-theory is confirmatory; if they disagree, the paper must explain why. Questions for Authors : 1.  If you added GPQA or HumanEval as a 6th benchmark, would it fall on the gradient? What would it mean for the claim if it did not? 2.  What mechanism drives the gradient for HellaSwag specifically? It does not involve explicit chain-of-thought. 3.  For MMLU, Polo et al. recommend ~ 100 items via IRT. Your D-study recommends 420. Can you explain the 4× discrepancy? 4.  If a practitioner uses LLM-as-judge evaluation, do D-study budgets still apply, or are they overwhelmed by judge variance (Mesting found judge identity at 43.8%)? 5.  What does the infrastructure crossing add beyond a confirmatory null, given that the three main findings would emerge from methodology-only replication? 2. Roundtable Cross-Sharing Areas of Agreement -  Score : Both reviewers converge on 4/6 (Weak Accept) — paper is at the acceptance threshold -  Core contribution : Both agree the cross-benchmark variance gradient is the paper's genuine and most important novel finding -  Experimental scale : Both praise the comprehensiveness (3M+ obs, 9 experiments, 5 benchmarks) -  Internal consistency : Both note that numerical results are coherent across tables -  Practical value : Both appreciate the D-study budgets as actionable for practitioners -  Item resampling : Both view the CV=0.19 finding as an honest and valuable contribution Areas of Complementary Concern -  R1 technical, R2 positioning : R1 identifies specific methodological gaps (D-study optimization procedure, G interpretation, missing experimental details), while R2 identifies framing gaps (infrastructure crossing as hollow, missing related work, post-hoc clustering) -  Both flag : Insufficient detail for replication (R1: prompts, temperatures, stratification; R2: comparison with IRT baselines) Disagreement Resolved -  R1 and R2 initially emphasized different aspects but neither raised objections to the other's concerns during sharing. R2's concern about \\\"infrastructure crossing as expensive null\\\" and R1's concern about \\\"D-study optimization undocumented\\\" are complementary weaknesses that jointly characterize the paper's limitations. 3. Consolidated Assessment Overall Score: 4/6 (Weak Accept) Confidence: 4/5 Decision Rationale The paper makes a genuine empirical contribution: the cross-benchmark variance gradient showing that item dominance shifts from 48% (knowledge) to 28% (proof reasoning) is novel, well-supported by bootstrap CIs, and provides a unifying explanation for seemingly contradictory findings in prior single-benchmark studies. The D-study reproducibility budgets are practically useful and the benchmark-specific budget differentiation (MMLU item-limited vs. GSM8K seed-limited) is non-obvious. The experimental scale is impressive. However, several issues keep the paper at the acceptance threshold rather than above it: 1.  Novelty concentration : The infrastructure×methodology crossing — framed as the key methodological advance over Mesting (2026) — yields  <0.5% on knowledge benchmarks. The main findings would emerge from methodology-only multi-benchmark replication. The GSM8K 3% exception partially rescues this but is insufficient to carry the infrastructure framing as a primary contribution. 2.  Presentation : Zero figures in a 15-table variance decomposition paper is a critical gap. The gradient and D-study curves practically demand visualization. 3.  Technical documentation gaps : D-study joint-optimization procedure undocumented, experimental details (prompt templates, temperature values, stratification) insufficient for replication, and the observation count claim needs precise itemization. 4.  Positioning gaps : Missing comparison with IRT-based recommendations (tinyBenchmarks 100 items vs. D-study 420 items), thin bibliography (15 refs), post-hoc gradient ordering without external validation. 5.  G coefficient interpretation : The paper somewhat conflates measurement generalizability (a design property) with benchmark reliability (a practical property), risking misinterpretation by practitioners. Actionable Revision Priorities (Ranked) 1.  Add 3-4 figures : (a) Stacked-bar variance decomposition across 5 benchmarks — the signature figure; (b) D-study projection curves (G vs. item count) with CI bands; (c) Forest plot of bootstrap CIs on item_ id across benchmarks; (d) Model-as-facet comparison (before/after stacked bars for MMLU) 2.  Document D-study optimization : State the joint-optimization procedure (grid search vs. analytical), the search bounds, and validate that recommendations are internally consistent 3.  Add IRT comparison : Compare D-study budgets with tinyBenchmarks recommendations and explain discrepancies — this strengthens the contribution 4.  Expand bibliography : Add ThinkingMachines (2025), Kunievsky & Evans (2025), and 3-5 additional relevant references to reach 20+ 5.  Provide experimental details : List all 6 prompt templates, the 3 temperature values, the item stratification procedure, and a precise observation count breakdown 6.  Reframe infrastructure crossing : Position as confirmatory evidence for separability rather than as a primary methodological contribution. Emphasize the GSM8K exception as the genuine finding from infrastructure crossing. 7.  Validate gradient externally : Add an independent measure of reasoning intensity for each benchmark (CoT length, multi-step count) to make the three-tier clustering principled rather than post-hoc 8.  Clarify G interpretation : Distinguish G as a generalizability coefficient over included facets from overall benchmark reliability, noting that practitioners using fixed items face different reliability profiles Experiment Coverage Assessment The paper covers all 9 planned experiments (exp-001 through exp-008 plus exp-001b). Coverage is breadth-oriented: 15 tables in 10 pages means each experiment gets 1-2 paragraphs. The fine-tuning study (exp-006) and LayerCast (exp-007) feel rushed — each could be appendix material to free space for figures and deeper analysis of the core experiments (exp-001, 002, 004). The MATH extension (exp-008) is well-integrated into the cross-benchmark narrative. Strengths Summary -  Cross-benchmark variance gradient: novel, statistically rigorous, explanatory -  D-study budget differentiation: practically actionable, non-obvious -  Experimental scale: ~ 3M observations, 9 experiments, 5 benchmarks, 6 models -  Item resampling stability: honest quantification of estimation uncertainty -  Engine confound correction: standalone methodological contribution -  Internal numerical consistency across all tables Weaknesses Summary -  Infrastructure crossing yields near-null, hollowing the claimed methodological advance -  Zero figures in a heavily quantitative variance decomposition paper -  D-study optimization procedure and experimental details undocumented -  Post-hoc gradient clustering without external validation -  Missing IRT comparison and thin bibliography -  G coefficient interpretation risks practitioner misunderstanding -  Fine-tuning and LayerCast sections are disjoint/rushed\\n[05-20 23:44] cli_a974499e77fadbdd: 🌙  [Dream Review Report — best | dream_20260520T222113]  · Overall: weak accept R1 Review: Methods & Experiments Summary This paper applies Generalizability Theory to LLM evaluation across five benchmarks, six models, and 4M+ records, crossing infrastructure (precision, hardware) with methodology (prompt, seed, temperature, ordering) and measurement (item) facets. The revised version addresses most structural issues from Dream #1: model is now treated as a crossed facet, bootstrap CIs are provided, the bibliography is expanded to 22 references, and the cross-benchmark variance gradient is correctly positioned as the primary contribution. The experimental design is ambitious and largely sound, with internal numerical consistency verified across tables. The paper demonstrates that variance structure shifts systematically from item-dominated (MMLU 56%) to interaction-dominated (MATH 21%), and that D-study optimal allocations reverse across task types. Strengths 1.  Internal numerical consistency is excellent.  Variance components in Table 1 sum to 100.0%. Model-as-facet Table 6 rows all sum to 100.0% (e.g., MMLU: 49.2+10.2+5.9+3.0+6.2+2.8+12.0+10.7=100.0). The interaction gradient in Table 5 is arithmetically consistent with Table 4 (e.g., MMLU sum(int item)=18.4 matches t i+s i+p i+prec i+ord i = 5.9+3.0+6.2+1.8+1.5=18.4). D-study projections in Tables 9-10 are internally consistent with the G_ full and G_ cur values in Table 7. 2.  The engine confound discovery and correction is a genuine methodological contribution.  Identifying that vLLM routes FP32 through V1 CUDA graph vs V0 eager for BF16/FP16, inflating precision* item from 1.8% to 7.2% and creating an 8.5pp accuracy gap, is valuable to any researcher using vLLM. The correction (standardizing all precisions to V0 enforce_ eager) is principled, and the before/after comparison (Table 1 MVP column) is convincing. The freed ~ 5.4% variance redistributing into residual is consistent with confound removal. 3.  Model-as-facet reanalysis (Table 6) addresses the most critical methodological gap from Dream #1.  Item_ id drops by ~ 6-7pp across all benchmarks (MMLU: 56.0->49.2, GSM8K: 25.0->22.6), with model* item absorbing ~ 10% on MMLU. Critically, item_ id remains rank-1 on all benchmarks and the gradient is preserved (49.2->38.4->30.8->22.6). This properly attributes model heterogeneity rather than inflating item estimates. 4.  Item resampling stability (Table 3) is a well-designed robustness check.  Three independent stratified 200-item MMLU samples with CV=4.1% on item_ id and consistent rank ordering across samples. The 30pp margin between item_ id (lowest sample: 52.8%) and the second-largest component eliminates single-sample artifact concerns. 5.  The factorial design for MMLU (exp-001) is densely crossed and large-scale.  4 models x 3 precisions x 6 prompts x 6 seeds x 3 temperatures x 4 orderings x 200 items = 1,036,800 records. This is among the largest factorial designs in the LLM evaluation variance literature. The per-model consistency (Table 2: item_ id 51.6-60.2% across four models) rules out single-model artifacts. 6.  The D-study facet effectiveness inversion (Table 11) is the paper's most practically useful finding.  The items:seeds effectiveness ratio shifting from 14.2:1 (MMLU) to 0.8:1 (GSM8K) has direct implications for evaluation protocol design and explains why prior studies on different benchmarks reached contradictory conclusions. 7.  Bootstrap CIs on item_id (Table 8) with non-overlapping intervals across adjacent benchmarks provide statistical support for the gradient.  The MMLU-ARC gap (CI upper 52.3 vs CI lower 35.6) and ARC-HellaSwag gap (CI upper 41.2 vs CI lower 28.2) show the gradient is not an artifact of sampling variability. Weaknesses Major 1.  Henderson Method I vs Method III discrepancy in the text.  The code ( variance_decomposition.py ) implements Henderson Method I (Type-I SS for balanced designs, solving EMS equations), but Section 3.1 (line 118) claims \\\"Henderson's Method III (expected mean squares)\\\" is used. Henderson's Method I and Method III are distinct estimation procedures -- Method I uses fitting-constants for balanced designs while Method III uses Searle's approach for unbalanced designs. For the balanced crossed design here, Method I is appropriate and the code is correct, but the paper misnames it. Table 1 caption says \\\"SE and 95% CI from Henderson's Method III\\\" -- this is incorrect given the code. Additionally, the paper later references \\\"REML vs Henderson\\\" sensitivity (Section 7.3, line 533) with  <=1.4pp differences and calls this \\\"Henderson Method I\\\" -- contradicting the earlier \\\"Method III\\\" claim. This inconsistency should be resolved. 2.  The D-study projection for GSM8K contains an arithmetically suspicious result.  In Table 10 (D-study GSM8K), the row \\\"150 items, 3 prompts, 10 seeds\\\" achieves G=0.90, while \\\"200 items, 3 prompts, 10 seeds\\\" achieves G=0.93. Yet in Table 7, the \\\"optimal\\\" allocation for GSM8K is listed as 150 items with 10 seeds. The issue: reducing items from 200 to 150 while achieving higher G only makes sense if item_ id variance is already small enough that removing 50 items has negligible impact on item-related error. But the G formula divides item-related variance components by n_ items -- so  fewer  items should yield  lower  G, not the same or higher. This suggests the \\\"150 items\\\" recommendation in Tables 7 and 9 may be from a different optimization (e.g., multi-facet joint optimization with different prompt/seed allocations) rather than a simple projection, but the paper does not explain the optimization procedure. The D-study code ( d_study.py ) sweeps one facet at a time while holding others fixed, which cannot produce the joint-optimization results in Table 9. Either the optimization procedure is undocumented, or the 150-item figure is derived from a different analysis than what the code implements. 3.  The \\\"counter-intuitive G pattern\\\" explanation (Section 5.1, line 283-284) has a logical gap.  The paper claims MMLU has lower G (0.36) than GSM8K (0.55) because \\\"high item_ id means item sampling is the measurement reliability bottleneck.\\\" But G is defined as sigma_ tau / (sigma_ tau + sigma_ delta), where sigma_ tau is universe-score variance (fixed-facet components only: precision, temperature, and their interaction). Looking at the code, sigma_ tau for MMLU would be dominated by precision (0.3%) and temperature (1.4%) main effects -- tiny values. For GSM8K, these would also be small. The G coefficient as implemented measures the ratio of fixed-facet variance to total variance -- so higher G for GSM8K means fixed facets explain proportionally more of the reduced-error variance on GSM8K. This is not the same as \\\"item sampling being the bottleneck.\\\" The paper's narrative explanation conflates the G coefficient with measurement reliability in a way that obscures what G actually measures in this design. Specifically: in a design where the object of measurement is benchmark accuracy and the facets are prompt/seed/ordering/item, the \\\"universe score\\\" is determined by which facets are treated as fixed vs random. The paper's partition (precision and temperature as fixed) means G measures how stable results are across prompt/seed/ordering/item variations  given  a fixed precision and temperature -- not overall measurement reliability. 4.  The paper claims \\\"4 million evaluation records\\\" (abstract, line 32) but the itemized totals fall short.  MMLU: 1,036,800. ARC+HellaSwag+GSM8K: 3 x 460,800 = 1,382,400. MATH: 460,800. Hardware: 691,200. 14B: 345,600. Fine-tuning: 1,728 runs (but unclear record count per run). Item resampling: 32,400. Even summing all inference experiments without double-counting (since hardware/14B experiments likely overlap with MMLU data), the total is closer to ~ 3.9M if MATH and hardware are fully independent, or ~ 3M if there is overlap. The \\\"over 4 million\\\" claim needs verification that these are truly independent records, not overlapping subsets counted multiple times. Moderate 5.  Reduced designs for non-MMLU benchmarks are insufficiently justified.  ARC/HellaSwag/GSM8K/MATH use 2 precisions x 2 temperatures (vs 3x3 for MMLU), but the paper does not explain why. If the reduction is due to GPU budget constraints, this should be stated explicitly. More importantly, the cross-benchmark gradient (Table 4) compares variance percentages from designs with different factorial structure (MMLU: 3 precisions, 3 temperatures vs others: 2 precisions, 2 temperatures). Variance percentages are relative to total variance, which changes with the design. Removing a precision level and a temperature level changes the total variance denominator and redistributes percentage shares. The paper should discuss whether the gradient would hold if all benchmarks used the identical design. 6.  Bootstrap resampling items with replacement while preserving balanced design (bootstrap_ci.py, lines 117-120) creates artificial correlation.  When a bootstrap sample draws the same item twice, the code assigns unique IDs (\\\"boot_ 0\\\", \\\"boot_ 1\\\") and treats them as independent items. But these duplicate items have identical responses across all conditions, violating the independence assumption underlying the ANOVA decomposition. This inflates the stability of item_ id estimates. A cluster bootstrap (resampling items and their complete observation vectors without re-indexing) would be more appropriate, though it would produce an unbalanced design requiring REML rather than Henderson Method I. 7.  The fine-tuning G-study (Section 8.2) uses a qualitatively different experimental paradigm.  RoBERTa-large is an encoder-only model fine-tuned on classification tasks; the inference experiments use decoder-only autoregressive models on generation/MC tasks. The variance hierarchy comparison (Table 13) across paradigms is informative but the claim that \\\"item dominance generalizes beyond inference to training\\\" overstates what this comparison can support. The facets themselves are different (learning rate and data shuffle replace prompt template and temperature), making direct comparison of variance percentages across paradigms questionable. 8.  The paper reports G_cur (current practice) in Table 7 but the definition of \\\"current practice\\\" is not consistent.  Table 7 defines G_ cur values (MMLU 0.22, GSM8K 0.14), and Table 9 shows MMLU with \\\"200 items, 1 prompt, 1 seed\\\" = G=0.22. But \\\"current practice\\\" typically includes a fixed temperature (usually 0) and a single precision -- if these are treated as fixed facets in the D-study, they should not contribute to error variance. The paper should clarify exactly what design parameters constitute \\\"current practice\\\" and whether the G_ cur values assume temperature=0 or marginalize over temperature levels. Questions for Authors 1.  Is the estimation method Henderson Method I (as implemented in the code) or Henderson Method III (as stated in the text)? If Method I, please correct the text. If Method III, please reconcile with the code. 2.  How is the joint D-study optimization (Table 9) computed? The provided D-study code sweeps one facet at a time. The joint recommendations (e.g., GSM8K: 150 items + 3 prompts + 10 seeds) appear to come from a different procedure. Please describe the optimization algorithm. 3.  For the counter-intuitive G pattern: what exactly is sigma_ tau in your D-study? If precision and temperature are treated as fixed, sigma_ tau is their variance plus their mutual interaction -- all tiny values. Doesn't this mean G is measuring something quite narrow (stability across precision/temperature choices) rather than overall measurement reliability? 4.  Can you provide the total observation count broken down by experiment, confirming non-overlap, to support the \\\"4 million\\\" claim? 5.  The abstract says \\\"item selection is the largest single variance source on all benchmarks\\\" with 56% to 21%. But on MATH (Appendix A), Llama-3.1-8B shows temperature item (21.8%) exceeding item_id (20.6%), and Mistral-7B shows temperature item (22.8%) exceeding item_ id (17.8%). How do you reconcile the \\\"all benchmarks\\\" claim when two of four models on MATH show item_ id is  not  the largest source? 6.  What is the effective sample size of the bootstrap after accounting for duplicate items? With 200 items and replacement sampling, each bootstrap draw will have ~ 127 unique items on average (by the birthday problem). Does this deflation affect CI coverage? Minor Issues 1.  The abstract states the item dominance gradient as \\\"56% on knowledge-retrieval tasks (MMLU) down to 21% on complex reasoning (MATH), a 35 percentage-point gradient.\\\" But Table 1 reports 56.0% for the pooled analysis, while Table 6 (model-as-facet, which is the more principled analysis) reports 49.2% for MMLU. The abstract should use the model-as-facet figures. 2.  Table 1 caption refers to \\\"SE\\\" but no standard error column is visible -- the columns are % Var, SE, CI Low, CI Up, MVP. Confirm that the SE column values are present and correctly computed. 3.  The paper uses \\\"infra x method\\\" as a single aggregate value (0.4% in Table 1) but does not list which specific interactions are included. From the 6-facet design (precision is the only infrastructure facet without hardware), the infrastructure x methodology interactions would be: precision x prompt, precision x seed, precision x temperature, precision x ordering. With hardware added (Table 6), this expands. Please enumerate. 4.  Line 118 says \\\"Henderson's Method III\\\" but line 533 says \\\"REML vs Henderson\\\" with no method number specified. Pick one consistent name. 5.  Table 12 (14B vs 8B) shows DeepSeek-R1-Distill-14B with temp item=8.8% and seed item=5.2%, both above the 8B range. The text attributes this to \\\"reasoning distillation introducing implicit chain-of-thought tendencies.\\\" This is speculative -- DeepSeek-R1-Distill-14B is architecturally different (distilled from a reasoning model), and the elevated interaction terms could also reflect the distillation training distribution rather than implicit CoT. The causal claim should be weakened. 6.  No figures. The cross-benchmark gradient and D-study projection curves would be substantially more impactful as visualizations than as tables. This is a presentation weakness, not a methodological one, but at a competitive venue it matters. 7.  The paper does not report effect sizes or practical significance thresholds beyond the 0.3% separability value. For which variance components is the estimate \\\"practically significant\\\"? A threshold framework (e.g., components >1% are \\\"practically relevant\\\") would aid interpretation. 8.  Reference [ 7 ] (Hua et al. 2025) is cited but never discussed in the Related Work section -- it appears only in the design decisions. Either discuss it or remove it. Score: 4/6 Confidence: 4/5\\n[05-20 23:39] cli_a974499e77fadbdd: 🌙  [Dream Review Report — best | dream_20260520T222113]  · Overall: weak accept Dream Review Report — Consolidated Roundtable Paper:  Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics Dream ID:  20260520T222113\\n Review Mode:  Full (2 Reviewers, 4-Step Roundtable) Roundtable Process -  R1 focus:  Methodology, experimental design, statistical rigor -  R2 focus:  Novelty, related work positioning, significance/impact -  Step 1 (Independent):  Both reviewers scored  4/6 (Weak Accept) , high confidence. -  Steps 2–3 (Cross-sharing & Convergence):  See §7 below. -  Step 4 (Synthesis):  This report. 1. Paper Summary The paper applies Generalizability Theory (G-theory) to LLM evaluation in a multi-benchmark setting. Three facet classes are crossed: measurement (item_ id, 200 stratified-sampled items per benchmark), methodology (prompt template ×6, random seed ×6, temperature ×2–3, option ordering ×4), and infrastructure (numerical precision FP32/BF16/FP16/LayerCast, GPU hardware ×2). Six models (4×7–9B, 2×14B) are evaluated on five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), totaling 4M+ evaluation records. A fine-tuning G-study with RoBERTa-large on four NLU tasks adds cross-paradigm evidence. Three claims: 1.  Cross-benchmark variance gradient:  item_ id dominance is benchmark-conditional — 56% on MMLU down to 21% on MATH, a 35pp monotonic gradient. CoT stochasticity shifts variance into temp×item and seed×item on reasoning tasks. 2.  Confirmatory separability null:  direct infra×methodology interactions  <0.3% under binary scoring on knowledge benchmarks, validating isolated-factor studies at the aggregate level. Both factor types interact substantially with items. 3.  D-study protocol reversal:  optimal evaluation protocol reverses across task types — MMLU is item-limited (420 items for G≥0.90), GSM8K is seed-limited (10 seeds). Current practice G <0.25 everywhere. 2. Novelty Assessment (R2-led, R1-endorsed) Claim 1 (Cross-benchmark variance gradient):  Moderate-to-high novelty. The paper's strongest contribution. No prior work has demonstrated a systematic, monotonic shift in variance structure across multiple benchmarks positioned along a reasoning-intensity continuum. The 35pp gradient (MMLU→MATH) with the CoT stochasticity mechanism unifies apparently contradictory conclusions from prior single-benchmark studies (Sclar on prompt sensitivity, Pezeshkpour on ordering, Yuan on precision). The \\\"unifying explanation\\\" framing is well-executed. However, item_ id dominance per se is expected from measurement theory (Brennan 2001); the contribution is the quantification and the gradient, not the dominance finding itself. Claim 2 (Confirmatory separability):  Low novelty, moderate utility. A confirmatory null. The infrastructure crossing — the paper's methodological advance over Mesting (2026) — yields near-nothing ( <0.3% direct interactions). The nuanced decomposition into direct vs. item-conditional interactions (aggregate separability + item-level coupling) adds value but is not a primary novelty claim. R1 further notes that the separability claim is benchmark-conditional: GSM8K and MATH show 2.5–3.0% infra×method, weakening the generality. Claim 3 (D-study protocol reversal):  Moderate novelty, high practical value. The facet effectiveness ratio inversion (MMLU items:seeds = 14.2:1, GSM8K = 0.8:1) is non-obvious and actionable. The D-study projection grids are the most practically useful output. The G <0.25 finding is an important indictment of current practice. Collective Assessment The three claims are stronger together than individually. The gradient explains the protocol reversal; the separability null validates independent factor study. The paper is best understood as a large-scale empirical study applying a well-established framework (G-theory) to a new domain (multi-benchmark LLM evaluation) and discovering a systematic empirical regularity (the gradient). This is a meaningful contribution, not a methodological breakthrough. Incrementality over Mesting (2026) Clear advance in three dimensions: (a) five benchmarks vs. one, (b) infrastructure crossing, (c) model as crossed facet. The infrastructure crossing yields near-null results, so (b) is confirmatory. The multi-benchmark gradient and model-as-facet analysis are genuine advances. R2 notes that the complementarity with Mesting (who found judge identity dominant at 43.8%) should be discussed more explicitly — this paper fixes the judge and reveals the structure underneath. 3. Methodology Assessment (R1-led, R2-endorsed) 3.1 G-Theory Application Largely correct.  Model-as-facet (Section 7) properly separates model×item interaction (~ 10%) from item variance, addressing a key prior concern. Henderson Method III with REML sensitivity check is appropriate for the nearly-balanced crossed designs. Max divergence of ~ 1.4pp with preserved rankings is reassuring. 3.2 Critical Methodological Concerns (a) Binary data in G-theory (R1, Major).  Standard Henderson III / REML assume continuous, approximately normal responses. Binary 0/1 data violates this. Item variance is mechanically linked to item difficulty via the Bernoulli variance function p(1-p), partially inflating item_ id dominance. The logprob analysis (Appendix B, item_ id = 42.8%) on continuous data is methodologically cleaner and partially mitigates this, but the primary analysis is on binary data. The paper must discuss this limitation. A generalized G-theory approach (Brennan 2001, Ch. 12) or link-function-based decomposition would be more appropriate. (b) Temperature and ordering as random facets (R1, Major).  With 2–3 temperature levels (specific design points, not random draws) and 4 systematic orderings (cyclic rotations of 24 possible permutations), the exchangeability assumption required for random effects is questionable. Misspecification inflates variance estimates for these facets and their interactions. The paper should either justify the random-effects assumption, treat these as fixed, or present both as sensitivity analysis. (c) Asymmetric designs across benchmarks (R1, Moderate).  MMLU uses 3 precisions × 3 temperatures; other benchmarks use 2×2. FP32 is absent from non-MMLU experiments. The cross-benchmark precision gradient (MMLU 3.0% → MATH 0.5%) is confounded with different precision levels tested. A BF16/FP16-only MMLU reanalysis for cross-benchmark comparison is needed. (d) Separability claim overstated (R1, Moderate).  Abstract says \\\" <0.3% under binary scoring\\\" but GSM8K reaches 3.0% and MATH 2.5%. A finding that holds on 3/5 benchmarks is benchmark-conditional, not general. The abstract and conclusions should lead with the conditionality. 3.3 Experimental Design -  MMLU G-study (1,036,800 records):  Strong. V0 enforce_ eager control is excellent experimental hygiene. -  Cross-benchmark (1,382,400 records):  Adequate but reduced design; asymmetry concern above. -  Multi-hardware (691,200 records):  Adequate; 2 GPU types is the minimum, findings are directional. -  Item resampling stability (32,400 records):  Well-designed; CV=4.1% on item_ id is reassuring. -  14B extension (345,600 records):  Useful but underpowered (2 models, 1 df for model effects). -  Fine-tuning (1,728 runs):  Adequate for its scope but architecturally distant from the decoder inference setting. Best framed as preliminary evidence. 3.4 Reproducibility Gaps R1 flags: vLLM version should include commit hash (not just version number); model weight HuggingFace revision hashes needed; exact CUDA/cuDNN/driver versions should be reported; prompt template text should appear in an appendix; item sampling seeds should be released. 4. Related Work Assessment (R2-led) The bibliography has improved dramatically from earlier drafts (7→22 references). Four Related Work paragraphs are well-organized. Positioning against prior work is largely fair and accurate. Missing References (R2) 1.  GeneralizIT (Nalisnick et al., 2024)  — G-theory software for ML. Relevant to tooling discussion. 2.  Kunievsky et al. (2025)  — prompt sensitivity decomposition into intent/articulation/model uncertainty. Relevant to interpreting prompt×item. 3.  Brittlebench (2026)  — prompt brittleness benchmark, ~ 50% prompt variance. Directly relevant. 4.  Bui et al. (2025)  — seed sensitivity in RoBERTa/Llama fine-tuning. Relevant to Section 8.2. 5.  ThinkingMachines (2025)  — batch invariance failure (80/1000 unique completions at T=0). Explains why seed×item is non-zero even at T=0; relevant to the vLLM batch nondeterminism concern. Minor Positioning Issues -  The claim that prior ANOVA studies \\\"lack D-study machinery\\\" is technically true but slightly misleading — bootstrap approaches can achieve similar projections; G-theory's advantage is closed-form projection. -  Vania et al. (2021) is in the bibliography but not discussed in Related Work text. 5. Presentation Assessment (Joint) Strengths -  Clean three-claim structure, well-supported throughout. -  \\\"Unifying explanation\\\" framing for the gradient is effective. -  Balanced Discussion with thorough Limitations paragraph. -  Engine confound discovery presented with appropriate before/after validation. -  Honest framing of infrastructure crossing as confirmatory. Weaknesses -  Zero figures (R2, Major).  This is a serious deficiency for a variance decomposition paper. Stacked-bar charts are an expected field idiom (Mesting 2026). The cross-benchmark gradient, D-study projections, and facet effectiveness inversion all cry out for visualization. With 19 tables and 0 figures, the paper is dense and visually monotonous. This is a competitive disadvantage at a top venue. Easily fixable. -  Title promises \\\"Evaluation Metrics\\\" but delivers only binary scoring (R2, Moderate).  Logprob analysis is a one-paragraph appendix. Either deliver the metric-conditional analysis or adjust the title. -  Fine-tuning section feels bolted on (R2, Moderate).  RoBERTa-large fine-tuning on SST-2/MNLI/RTE/COPA is architecturally distant from 7–14B decoder inference. Cross-paradigm generalization is weak. Should be explicitly qualified as preliminary. -  No cost analysis for recommended budgets (R2, Minor).  The D-study recommends specific allocations but does not estimate GPU-hour costs. Without cost, the budgets remain theoretical. 6. Scope Assessment (Joint) Adequate for claimed scope -  5 benchmarks spanning knowledge-to-reasoning: sufficient for the gradient claim. Non-overlapping bootstrap CIs provide statistical support. -  4×7–9B models showing consistent per-model patterns: gradient is not a single-model artifact. -  14B extension within the 8B range: scale invariance holds at this increment. Limitations that should constrain claims -  No 70B+ models.  Larger models may compress item_ id through higher accuracy and reduce CoT stochasticity through stronger reasoning. Generality claims should be scoped to 7–14B. -  No proprietary API models.  GPT-4/Claude/Gemini have opaque infrastructure. Separability null may not hold when infrastructure is uncontrolled. Mesting studied API models; this paper studies open-weight models. Complementarity should be discussed. -  No non-English benchmarks.  Tokenization effects on item difficulty could alter cross-lingual variance structure. -  No generation-based benchmarks.  All are multiple-choice or short-answer. Open-ended generation may have fundamentally different variance structures. -  200-item samples.  Resampling stability tested only for MMLU. Other benchmarks lack resampling validation. 7. Roundtable: Convergence and Divergence Full Convergence (Both Reviewers) 1.  Score: 4/6 (Weak Accept).  At the acceptance threshold, contingent on addressable revisions. 2.  Cross-benchmark gradient is the paper's strongest, most novel contribution.  Well-supported by data, non-overlapping CIs, per-model consistency. 3.  Separability null is confirmatory, not novel.  Honest framing is appreciated. 4.  D-study budgets are the most practically useful output.  Immediately actionable. 5.  Infrastructure crossing yields near-null results.  The claimed advance over Mesting produces confirmatory rather than discovery findings. 6.  Fine-tuning extension is architecturally distant.  Should be qualified as preliminary. 7.  Zero figures is a serious presentation weakness.  Easily fixable; would materially improve the paper. 8.  Scope limited to 7–14B open-weight models.  Claims should be scoped accordingly. 9.  Engine confound discovery is a standalone methodological contribution.  Valuable to the community. Partial Convergence 10.  Separability conditionality (R1 raised, R2 endorsed after cross-sharing).  The abstract's \\\" <0.3%\\\" is accurate for knowledge benchmarks but not for GSM8K/MATH. Both reviewers agree the abstract should qualify this. 11.  Missing references (R2 raised, R1 endorsed).  Five missing references (GeneralizIT, Kunievsky, Brittlebench, Bui, ThinkingMachines) are relevant and should be added. R1-Only Concerns (Not Contested by R2) 12.  Binary data in G-theory  — a critical methodological point that R2 did not independently flag but endorses as important. The paper's primary analysis uses binary data under methods assuming continuous responses. Must be discussed. 13.  Temperature/ordering as random facets  — 2–3 temperature levels and 4 systematic orderings are dubious as random draws. R2 did not raise this but acknowledges the statistical logic. 14.  Asymmetric designs across benchmarks  — FP32 absent from non-MMLU experiments confounds cross-benchmark precision comparisons. R2-Only Concerns (Not Contested by R1) 15.  Title/metrics mismatch  — \\\"Evaluation Metrics\\\" in title but only binary scoring in main text. R1 did not flag this but agrees the title should match content. 16.  Comparison with IRT approaches  — the D-study budgets should be compared with tinyBenchmarks (Polo et al.) recommendations. What does G-theory add over IRT-based subsampling? 17.  Cost analysis for budgets  — GPU-hour estimates would make recommendations concrete. 8. Consolidated Strengths 1.  Cross-benchmark variance gradient is a genuine, well-supported empirical contribution  that unifies contradictory prior findings. The monotonic 35pp gradient with mechanistic CoT explanation and non-overlapping bootstrap CIs is the paper's signature finding. 2.  Massive experimental scale  (4M+ records, 5 benchmarks, 6 models, fully crossed factorial designs). Few empirical papers in this area match the breadth. 3.  D-study reproducibility budgets are immediately actionable.  Specific item/prompt/seed allocations for G≥0.90, benchmark-specific, with projection grids. 4.  Engine confound discovery and correction  (vLLM V0 vs. V1 routing) is a standalone methodological contribution. 5.  Model-as-facet analysis  cleanly separates model×item interaction (~ 10%) and preserves the gradient after extraction. 6.  Honest framing throughout.  Separability as confirmatory, item dominance as psychometrically expected, gradient as directional with quantified uncertainty. 7.  Comprehensive robustness checks.  Item resampling stability, REML vs. Henderson III, bootstrap CIs, per-model breakdowns, 14B scale validation. 8.  Counter-intuitive G pattern  (knowledge benchmarks yield lower G than reasoning benchmarks) is well-explained and insightful. 9.  Current-practice G<0.25  is an important and alarming finding for the field. 9. Consolidated Weaknesses Major 1.  Binary data in standard G-theory  without discussion of the methodological limitation. Item_ id dominance is partially artifactual from the Bernoulli variance function. Must be addressed in revision. 2.  Zero figures in a variance decomposition paper.  19 tables and 0 figures. Stacked-bar charts, D-study curves, and gradient visualizations are expected idioms. Serious competitive disadvantage at a top venue. 3.  Temperature (2–3 levels) and ordering (4 systematic rotations) as random facets  is statistically dubious. Sensitivity analysis with these as fixed effects is needed. Moderate 4.  Asymmetric designs across benchmarks  confound cross-benchmark precision comparisons (FP32 absent from non-MMLU experiments). 5.  Separability claim overstated in abstract  — holds on knowledge benchmarks but GSM8K (3.0%) and MATH (2.5%) exceed the stated threshold. Should be qualified. 6.  Title promises \\\"Evaluation Metrics\\\" but delivers only binary scoring  in main text. Logprob analysis relegated to one-paragraph appendix. 7.  Infrastructure crossing is the claimed advance over Mesting but yields near-null results.  The main findings would emerge from a Mesting-style design with fixed infrastructure. 8.  No models above 14B.  Generality cannot be claimed beyond this scale range. 9.  Missing references:  GeneralizIT, Kunievsky et al. (2025), Brittlebench (2026), Bui et al. (2025), ThinkingMachines (2025). 10.  Fine-tuning extension (RoBERTa-large, encoder-only)  is architecturally distant from decoder inference. Feels appended rather than integrated. Minor 11.  No cost analysis for recommended D-study budgets. 12.  Residual component (6–18%) is underanalyzed; higher-order interactions mentioned but not tabulated. 13.  14B extension is underpowered (2 models, 1 df for model effects). 14.  Item resampling stability tested only for MMLU, not for other benchmarks. 15.  Prompt template text not provided; reproducibility details (vLLM commit hash, model weight hashes, CUDA versions) insufficient. 10. Consolidated Questions for Authors 1.  Binary data:  How do you address the assumption violation of applying Henderson III / REML to binary (0/1) responses? Have you considered generalized G-theory or a probit/logit link-function decomposition? Does item_ id dominance survive under a method appropriate for binary data? 2.  Temperature as random facet:  What justifies treating 2–3 temperature levels (specific design points: 0, 0.5, 1.0) as a random rather than fixed facet? Have you compared results with temperature as fixed? 3.  Cross-benchmark precision confound:  Have you re-analyzed MMLU restricted to BF16/FP16 only (excluding FP32) for the cross-benchmark comparison? Does the precision gradient survive with matched precision levels? 4.  Gradient under logprob scoring:  Does the full 5-benchmark gradient (MMLU > ARC > HellaSwag > GSM8K > MATH) hold under logprob-based scoring? If not, is the gradient partially an artifact of binary scoring thresholds? 5.  Comparison with IRT:  How do the D-study budgets compare to Polo et al.'s tinyBenchmarks recommendations for MMLU? What does G-theory add over IRT-based efficient subsampling? 6.  Separability scope:  How confident are you that the separability null extends to more diverse hardware (A100 vs. H100 vs. B200) where architectural differences are more substantial? 7.  Judge variance complementarity:  Your entire variance structure sits \\\"underneath\\\" Mesting's judge variance (43.8%). How should practitioners interpret your budgets for LLM-as-judge evaluation? Would the gradient hold if judge were included as a facet? 8.  Negative variance estimates:  How are negative Henderson III estimates handled (set to zero, left negative, redistributed)? This affects the separability claim where infra×method components are near zero. 9.  D-study optimization procedure:  How were the \\\"optimal\\\" prompt and seed counts determined? Formal cost minimization, or chosen by inspection? 10.  Rank instability analysis:  Have you computed what fraction of published leaderboard rankings would change under re-evaluation with different seeds/prompts? This would make G <0.25 more concrete than an abstract coefficient. 11. Recommended Revisions (Priority-Ordered) Must-fix for acceptance 1.  Add 3–5 figures: (a) cross-benchmark stacked-bar gradient, (b) D-study G vs. total evaluations curves, (c) facet effectiveness ratio visualization, (d) bootstrap CI forest plot. 2.  Add a paragraph discussing binary data limitations in G-theory estimation and note that logprob scoring provides the methodologically cleaner decomposition. 3.  Present sensitivity analysis with temperature as fixed facet. 4.  Qualify separability claim in abstract: \\\" <0.3% on knowledge benchmarks; rises to 2–3% on reasoning benchmarks.\\\" Should-fix 5.  Re-analyze MMLU at BF16/FP16 only for the cross-benchmark comparison table. 6.  Add the 5 missing references (GeneralizIT, Kunievsky, Brittlebench, Bui, ThinkingMachines). 7.  Align title with content: either deliver metric-conditional analysis or remove \\\"Evaluation Metrics\\\" from title. 8.  Add prompt template text in an appendix; provide vLLM commit hash, model weight hashes. Nice-to-have 9.  Extend logprob analysis to all 5 benchmarks to test whether the gradient holds under continuous scoring. 10.  Add cost estimates (GPU-hours) for recommended D-study budgets. 11.  Expand higher-order interaction analysis in appendix. 12. Overall Assessment Score: 4/6 (Weak Accept) Confidence: High Meta-Review Justification Both reviewers independently scored this paper 4/6 (Weak Accept) with high confidence, and the roundtable did not identify grounds to change this. The cross-benchmark variance gradient is a genuine novel finding: no prior work has demonstrated the systematic shift from item-dominated (knowledge tasks) to interaction-dominated (reasoning tasks) variance structure, and the 35pp gradient with non-overlapping bootstrap CIs is well-supported. The D-study reproducibility budgets fill a real practical gap, and the G <0.25 indictment of current practice is alarming and important. The paper is held back by addressable issues: (a) zero figures is a serious presentation weakness at a top venue; (b) binary data in standard G-theory requires explicit discussion; (c) temperature/ordering as random facets needs sensitivity analysis; and (d) the separability claim needs scoping. None of these are fatal. If the must-fix revisions are made — especially adding figures and the binary data discussion — the paper would likely move to 5/6 (Accept). The infrastructure crossing, positioned as the key methodological advance over Mesting, yields near-null results. This is intellectually honest (confirmatory null) but means the paper's primary novelty rests on the cross-benchmark gradient and D-study budgets rather than on the infrastructure-methodology crossing. Both reviewers agree this is sufficient for a top venue, given the scale of the empirical contribution and the practical utility of the findings. Bottom line:  A well-executed, large-scale empirical study with a genuine novel finding (the gradient), actionable outputs (D-study budgets), and an important policy implication (G <0.25). At the acceptance threshold; fixable revisions would push it to a clear accept.\\n[05-20 23:36] cli_a974499e77fadbdd: 🌙  [Dream Review Report — median | dream_20260520T222113]  · Overall: weak accept dream_ id: dream_ 20260520T222113\\n tier: median\\n overall_ score: weak accept\\n timestamp: 2026-05-20T23:45:00+00:00 Dream Review Report — R1 (Methodology & Experimental Rigor) Paper:  Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics Tier:  Median Review mode:  R1 focus — Methodology, Experimental Design, Statistical Rigor 1. Paper Summary The paper applies Generalizability Theory (G-theory) to LLM evaluation, conducting multi-benchmark crossed-facet variance decompositions across five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), six models (4x7-9B + 2x14B), two GPU architectures, and multiple levels of precision, prompt template, seed, temperature, and answer ordering. Over 3 million evaluation records are analyzed. Three claims are made: (1) a benchmark-conditional variance gradient where item dominance ranges from 48% (MMLU) to 28% (MATH) under model-as-facet analysis; (2) infrastructure x methodology separability at the aggregate level ( <0.5% on knowledge benchmarks, rising to 3% on math-generation benchmarks); (3) metric-conditional, benchmark-specific reproducibility budgets via D-study projections. Extensions cover 14B models, RoBERTa fine-tuning, LayerCast precision mitigation, and three scoring metrics. 2. Methodological Soundness 2.1 G-Theory Framework Application Largely correct, with one significant improvement over Dream #1.  The revised paper treats model as a crossed random facet (Section 4.4 / Table 5), which was the most critical methodological concern in the prior review. This properly separates model×item interaction (16-22%) from pure item variance and residual. The 4pp systematic reduction across all benchmarks is plausible and consistent with psychometric expectation when objects of measurement have heterogeneous difficulty profiles. Henderson Method III vs. REML.  The paper uses Henderson Method III (expected mean squares) as primary estimation with REML as sensitivity check. This is defensible: Henderson III is unbiased for balanced designs, and the design is nearly balanced (fully crossed within each experiment). The reported max divergence of 2.1pp with preserved rank ordering is reassuring. However: -  Concern:  Henderson Method III can produce negative variance component estimates for near-zero components. The MATH table (Table 22 in the imagined experiments) shows a negative \\\"other\\\" entry (-1.5%), which is characteristic of this issue. The paper should explicitly state how negative estimates are handled (set to zero? redistributed? left as-is?). This matters for the separability claim where infra×method components are near zero — a negative estimate truncated to zero looks different from a genuinely zero estimate. -  Concern:  The G-theory formula presented in Equation 2 is simplified. The actual D-study formula for a multi-facet crossed design with 5+ facets involves many more terms. The paper should either present the full formula used or cite a specific implementation (e.g., GeneralizIT package). The simplified formula risks misleading readers about how D-study projections were actually computed. 2.2 Crossed Random-Effects Assumptions Items as random facet:  Justified. The 200 items per benchmark are sampled (stratified) from larger pools (MMLU: 14,042; ARC: 2,590; GSM8K: 1,319; HellaSwag: 10,042; MATH: 5,000). The random-facet assumption requires that observed items are exchangeable draws from a universe of admissible observations. Stratified sampling strengthens this by ensuring subject/topic coverage. Model as random facet:  Partially justified. Four 7-9B models from different families (Qwen, Llama, Gemma, Mistral) are treated as exchangeable draws from the universe of \\\"7-9B instruction-tuned LLMs.\\\" This is defensible but arguable — the model universe is not well-defined, and four models provide limited degrees of freedom for estimating model-related variance components. The 14B extension (2 models) is even more constrained. The paper should acknowledge that model-as-facet with k=4 yields imprecise estimates of model variance components and that the model universe is narrowly defined (open-weight, instruction-tuned, 7-9B). Prompt as random facet:  The 6 prompt templates are described but their generation process matters for the random-effects assumption. If they were systematically designed to vary specific dimensions (e.g., formality, instruction explicitness), they may not represent random draws from a prompt universe. The paper should clarify whether prompt templates were generated to be representative (supporting random effects) or to maximize diversity (which biases variance estimates upward). Seed as random facet:  Clearly justified — seeds are arbitrary integers drawn from a large space. Temperature as random facet:  Problematic. With only 2-3 levels (e.g., 0, 0.5, 1.0), treating temperature as a random facet is statistically dubious — these are specific points chosen to span the parameter range, not random draws from a temperature distribution. Temperature is better modeled as fixed. If treated as random, the variance estimates carry extreme uncertainty with 2-3 df. The paper should address this. Ordering as random facet:  Four orderings (ABCD, BCDA, CDAB, DABC) — these are systematic rotations, not random draws. The random-effects assumption is defensible only if one argues these represent exchangeable draws from the universe of possible orderings, which is reasonable for 4-option MC but should be noted. 2.3 Variance Estimation for Binary Data Critical methodological question.  Binary correct (0/1) data violates the normality assumption underlying standard G-theory variance component estimation. Henderson Method III and REML both assume continuous, approximately normal response variables. For binary data: -  Variance components are bounded by the Bernoulli variance p(1-p), creating ceiling effects for items near p=0 or p=1. -  Item-level variance is mechanically linked to item difficulty — easy and hard items contribute less variance by construction, inflating the apparent dominance of \\\"mid-difficulty\\\" items. -  The paper's finding that item_ id is the largest variance source is partially an artifact of using binary scoring on items with heterogeneous difficulty. This is the well-known \\\"item difficulty confound\\\" in classical test theory. The text-exact-match metric (also binary) and logprob metric (continuous) provide useful sensitivity checks. The logprob result (item_ id = 55%) is methodologically cleaner because the response variable is continuous, avoiding the binary data issue. The paper should discuss the binary data limitation explicitly and note that logprob scoring provides the most methodologically sound variance decomposition. 3. Experimental Design 3.1 Factorial Design Adequacy MMLU (Exp 1): Strong.  4 models × 3 precisions × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 items = 1,036,800 observations. This is the richest design and supports all claimed decompositions. The V0 enforce_ eager control eliminates the engine confound — this is excellent experimental hygiene. Cross-benchmark (Exp 3): Adequate but reduced.  2 precisions × 2 temperatures (vs. 3×3 on MMLU). The reduction is justified by compute constraints but creates an asymmetry: FP32 is absent from cross-benchmark experiments, meaning the precision facet is restricted to BF16/FP16 (which differ minimally). The claimed cross-benchmark gradient in precision effects (MMLU 3.0% vs. GSM8K 1.0%) is confounded with the different precision levels tested. This should be explicitly acknowledged. Multi-hardware (Exp 4): Adequate.  2 GPU types is the minimum for estimating hardware effects. With 1 df for hardware main effect, the estimate is necessarily imprecise. The paper correctly frames hardware findings as directional rather than definitive. Item resampling (Exp 2): Well-designed.  Three independent stratified draws with different seeds. The CV=0.19 (paper) or CV=0.19 (imagined experiments) on item_ id is an important honesty result. However, three draws provide only a rough estimate of resampling variability — 10+ draws would be more convincing, though the compute cost may be prohibitive. Fine-tuning (Exp 7): Adequate for its scope.  432 runs per task × 4 tasks = 1,728 total. The fully crossed design (seed × LR × shuffle × GPU × precision) is clean. The RoBERTa-large choice is acknowledged as a limitation (encoder-only, classification). This experiment is best framed as a conceptual extension rather than a direct generalization. 3.2 Missing Controls and Confounds 1.  Batch size / sequence length confound.  vLLM batches requests dynamically. If different benchmark items produce different output lengths (especially GSM8K/MATH with CoT), batch composition may vary, introducing an unmodeled variance source that gets absorbed into residual or item interactions. The paper uses \\\"default vLLM settings\\\" which is realistic but means batch-level nondeterminism is present. 2.  Prompt template × benchmark interaction.  The same 6 prompt templates are used across benchmarks, but their appropriateness may vary by task. A prompt template that works well for MMLU factual recall may be poorly suited for GSM8K math reasoning. This could inflate prompt×item interactions on some benchmarks for reasons unrelated to the \\\"prompt sensitivity\\\" construct. 3.  Item difficulty distribution differs across benchmarks.  MMLU items span a wide difficulty range; GSM8K items at 8B model scale cluster near 0.4-0.6 accuracy; MATH items are heavily bimodal (trivial or impossible for 8B models). These distributional differences mechanically affect how much variance is attributable to items vs. interactions. The paper's \\\"cognitive complexity\\\" explanation for the cross-benchmark gradient is plausible but not the only explanation — difficulty distribution differences could account for part of the pattern. 4.  Stratified sampling details.  The paper mentions stratified sampling across 57 MMLU subjects, but the stratification scheme for other benchmarks (GSM8K difficulty levels? MATH topics?) is not described. If non-MMLU benchmarks lack stratification, their item samples may be less representative. 5.  Answer extraction method.  For generation-based scoring, the method of extracting answers from generated text is a potential confound. Different regex/parsing strategies could produce different binary scores for the same generation. This is not discussed. 3.3 Item Sampling Strategy The 200-item stratified sample from MMLU's 14,042 items (1.4%) is a reasonable balance between compute cost and representativeness. The resampling stability test (CV=0.19) properly quantifies the sampling uncertainty. For other benchmarks: -  GSM8K: 200/1,319 = 15.2% — much denser sampling, less sampling uncertainty expected. -  ARC-Challenge: 200/2,590 = 7.7% — moderate. -  HellaSwag: 200/10,042 = 2.0% — similar to MMLU. -  MATH: 200/5,000 = 4.0% — moderate. The paper should note that cross-benchmark comparisons of item_ id variance share are confounded with sampling fraction — benchmarks with denser item sampling (GSM8K) mechanically have lower item-sampling uncertainty, which could affect the D-study projections. 4. Statistical Rigor 4.1 Bootstrap Confidence Intervals Construction:  1,000 item×condition resamples. This is a standard nonparametric bootstrap for G-theory (cf. Brennan, 2001, Ch. 10). The resampling unit matters: resampling items treats items as the primary sampling unit, which is appropriate given that item selection is the largest variance source. Concerns: -  The bootstrap resamples items but holds conditions (prompt, seed, temp, precision, ordering) fixed. This captures item-sampling uncertainty but not condition-sampling uncertainty. A more thorough approach would resample both items and conditions (double bootstrap), though this is computationally expensive and rarely done in G-theory applications. The paper should acknowledge this limitation. -  The reported CI widths (~ 0.14 for item_ id) are wide enough that the practical implications change substantially across the CI range. For example, MMLU item_ id [ 0.41, 0.55] maps to different D-study recommendations at each endpoint. The paper handles this well by reporting D-study CIs ([ 350, 510 ] for G≥0.90 on MMLU). 4.2 D-Study Projections Validity:  D-study projections assume that variance components estimated from the G-study generalize to the projected design. This is the standard G-theory assumption and is reasonable when the projected design changes only the number of levels (e.g., more items, more seeds) rather than the nature of the facets. The projections in Table 8 change item counts while holding prompt/seed counts at \\\"optimal\\\" levels — this is valid. Concern — optimal prompt/seed counts.  The D-study recommends \\\"3 prompts / 4 seeds\\\" for MMLU and \\\"4 prompts / 6 seeds\\\" for GSM8K. How are these \\\"optimal\\\" counts determined? If they are chosen to minimize total compute for a target G, the optimization procedure should be described. If they are chosen post-hoc to make the item counts look reasonable, this is problematic. Concern — extrapolation to 420+ items.  The G-study uses 200 items. Projecting to 420 items assumes linear scaling of the error reduction, which holds under the random-sampling model. However, if the additional 220 items are drawn from the same pool, they may not be independent of the original 200 (especially for smaller pools like GSM8K with only 1,319 total items). The finite-population correction should be applied when the projected sample is a large fraction of the universe. 4.3 REML Sensitivity Check Sufficient for its purpose.  The 2.1pp maximum divergence with preserved rankings is adequate evidence that the choice between Henderson III and REML does not affect qualitative conclusions. However, REML is generally preferred for unbalanced designs. Since the within-experiment designs are balanced (fully crossed), Henderson III is appropriate. The sensitivity check confirms this. 4.4 Permutation Test for Gradient The p=0.003 for the gradient direction (MMLU > HellaSwag on item_ id) is properly reported. The paper correctly notes that the CIs overlap partially at the margins ([ 0.38, 0.41 ]), supporting directional but not magnitude claims. This is honest and appropriate. 5. Reproducibility Concerns 1.  vLLM version dependency.  The paper uses vLLM 0.9.2 with V0 enforce_ eager. vLLM's behavior changes across versions (the V0/V1 engine confound demonstrates this). The results may not replicate on vLLM 0.8.x or 1.0.x. The paper should pin the exact vLLM commit hash, not just the version number. 2.  Model weight provenance.  The paper lists model names but not specific weight versions (e.g., HuggingFace revision hashes). Model weights on HuggingFace can be updated without changing the model card name. For reproducibility, exact weight hashes are needed. 3.  CUDA version and driver.  CUDA nondeterminism is a core topic of the paper. The exact CUDA version, cuDNN version, and driver version should be reported. The paper mentions \\\"CUDA 12.8\\\" support for vLLM 0.9.2 but does not pin the exact software stack. 4.  Item sample seeds.  The stratified sampling seeds for the 200-item samples should be released. The resampling stability test uses seeds 0, 7, 99 — are these the only seeds tested? If the main experiments use a single seed (e.g., seed 0), the results are conditional on that particular draw. 5.  Prompt template text.  The 6 prompt templates are critical to reproducibility but their exact text is not provided in the paper. They should appear in an appendix. 6. Strengths -  Comprehensive factorial design.  The MMLU experiment (1,036,800 observations, 5,184 conditions) is one of the largest crossed factorial designs in LLM evaluation research. The systematic approach — full crossing on MMLU, reduced crossing on other benchmarks, explicit confound controls — reflects careful experimental planning. -  Engine confound discovery and fix.  Identifying that default vLLM routes FP32 through a different engine (V1 CUDA graph) than BF16/FP16 (V0 eager) is a standalone methodological contribution. The enforce_ eager fix is simple, actionable, and immediately useful to the community. -  Model-as-facet analysis.  This revision correctly treats model as a crossed random facet, addressing the most fundamental concern from Dream #1. The systematic 4pp reduction across all benchmarks and the extraction of 16-22% model×item interaction is a clean result. -  Multi-benchmark coverage.  Five benchmarks spanning knowledge retrieval (MMLU, ARC), commonsense reasoning (HellaSwag), arithmetic reasoning (GSM8K), and proof reasoning (MATH) provides genuine coverage of the LLM evaluation landscape. The three-tier clustering is more nuanced than a simple monotonic gradient. -  Metric-conditional analysis.  The binary/text-match/logprob comparison (Table 9) is a first-order finding: G ranges from 0.32 to 0.97 depending on the scoring metric. This alone justifies the paper — practitioners cannot discuss \\\"reliability\\\" without specifying the metric. -  Honest uncertainty quantification.  Bootstrap CIs on variance components, D-study CIs on item counts, resampling stability tests, and REML sensitivity checks collectively demonstrate statistical maturity. The paper acknowledges that the gradient is directional rather than precisely quantified. -  Three-tier narrative is stronger than two-cluster.  Including MATH extends the gradient from {MMLU, ARC} vs. {GSM8K, HellaSwag} to a three-tier structure with 20pp spread, providing more evidence for the benchmark-conditional story. -  Separability as confirmatory null.  Reframing infrastructure×methodology separability as a confirmatory result (validating prior isolated-factor studies) rather than a breakthrough is intellectually honest and strengthens the paper's credibility. -  Fine-tuning contrast.  The inverted variance hierarchy (LR/seed dominate in fine-tuning vs. items dominate in inference) adds conceptual depth and explains why different evaluation modes have different reproducibility conventions. 7. Weaknesses Major -  Binary data in G-theory.  Applying standard G-theory variance component estimation (Henderson III / REML) to binary (0/1) data is methodologically questionable. The response variable violates normality and homoscedasticity assumptions. Item variance is mechanically linked to item difficulty via the Bernoulli variance function. This affects the headline item_ id estimates and all downstream D-study projections. The logprob analysis partially mitigates this, but the paper's primary analysis is on binary data. A generalized G-theory approach (Brennan, 2001, Ch. 12) or a link-function-based decomposition would be more appropriate. At minimum, the paper must discuss this limitation and note that item dominance under binary scoring is partially artifactual. -  Temperature and ordering as random facets.  With 2-3 temperature levels and 4 systematic ordering rotations, treating these as random facets is questionable. Random-effects estimation requires the observed levels to be exchangeable draws from a larger universe. Temperature levels (0, 0.5, 1.0) are specific design points, not random draws from a temperature distribution. The 4 orderings are systematic rotations, not random permutations of 4 !=24 possibilities. Misspecifying fixed effects as random inflates the estimated variance components for these facets and their interactions. The paper should either (a) justify the random-effects assumption for these facets, (b) treat them as fixed and re-estimate, or (c) present both analyses as a sensitivity check. -  Asymmetric designs across benchmarks weaken cross-benchmark claims.  MMLU uses 3 precisions × 3 temperatures; other benchmarks use 2 × 2. FP32 is absent from non-MMLU experiments. This means precision-related variance on MMLU includes the FP32 degradation effect that is absent from other benchmarks. The claimed gradient in precision effects (MMLU 3.0% → MATH 0.5%) is confounded with the different precision levels tested. The paper should either (a) re-analyze MMLU restricted to BF16/FP16 for the cross-benchmark comparison, or (b) explicitly state the confound. -  Separability claim is benchmark-conditional but presented as a general finding.  The abstract and contributions list separability as \\\" <0.5% binary\\\" but the body reveals GSM8K reaches 3.0% and MATH reaches 2.5%. A finding that holds on 3/5 benchmarks but fails on 2/5 is not a general separability result — it is a benchmark-conditional one. The abstract and conclusions should lead with the conditionality. Moderate -  D-study \\\"optimal\\\" prompt/seed counts are not derived.  The paper presents specific prompt and seed counts (3/4 for MMLU, 4/6 for GSM8K) as \\\"optimal\\\" without showing the optimization procedure. Are these the minimum counts that don't substantially change the D-study item projection? Are they from a cost-minimization formula? The derivation matters because practitioners will use these numbers directly. -  Residual component is large and underanalyzed.  Residual ranges from 6% to 18% across benchmarks and analyses. Under model-as-facet analysis, the residual on MMLU drops from 14% to 8%, which is progress, but 8% is still substantial. What is in this residual? Higher-order interactions (3-way and above) are mentioned in passing (\\\"3-5% total\\\") but not tabulated. The paper claims higher-order interactions are small, but 3-5% is comparable to many named 2-way interactions (e.g., seed×item at 2.0%). An appendix breaking down the residual would strengthen the paper. -  HellaSwag clustering with GSM8K is not well-explained.  HellaSwag is a commonsense reasoning / sentence completion task, not a math reasoning task. Its item_ id (31%) places it in the same tier as GSM8K (36%), but its infra×method (0.3%) is similar to knowledge benchmarks. The paper groups them in a \\\"mid\\\" tier based on item_ id alone, but the infra×method pattern suggests HellaSwag behaves differently from GSM8K. The three-tier narrative is cleaner than the data fully support. -  14B extension is underpowered.  With only 2 models, model-as-facet analysis has essentially 1 df for model effects. The reported model×item = 25% (vs. 21% at 8B) could reflect the specific model pair chosen (dense vs. reasoning-distilled) rather than a scale effect. The paper should note that the 8B→14B comparison confounds scale with architecture diversity. -  No correction for multiple comparisons.  Many variance components are tested across many benchmarks and metrics. While the bootstrap CIs provide individual component uncertainty, no family-wise error correction is applied. The GSM8K infra×method CI [ 0.012, 0.048 ] excludes zero, but is this still significant after correcting for testing the same hypothesis on 5 benchmarks? Minor -  \\\"Over 3 million\\\" vs. \\\"over 4 million.\\\"  The abstract says \\\"over 3 million\\\"; the best-tier paper says \\\"over 4 million.\\\" The actual count should be computed and reported exactly. -  MATH \\\"other\\\" = -1.5%.  Negative variance component estimates should be flagged and the handling policy stated (see Section 2.1 above). -  LayerCast section (8.3) adds little.  The finding that LayerCast provides marginal benefit over BF16 is expected given that precision effects are already small. This could be condensed to 1-2 sentences or moved to an appendix. -  Table 5 (model-as-facet) shows \\\"---\\\" for MATH precision entries.  If precision was not tested on MATH (only BF16/FP16), this should be noted explicitly rather than with a dash. 8. Questions for Authors 1.  How are negative variance component estimates handled?  Henderson Method III can produce negative estimates for near-zero components. Are these set to zero, left negative, or redistributed? This affects the separability claim. 2.  What justifies treating temperature (2-3 levels) as a random rather than fixed facet?  With 3 specific design points, the random-effects assumption is questionable. Have you compared results with temperature as fixed? 3.  For the cross-benchmark comparison, have you re-analyzed MMLU restricted to BF16/FP16 only (excluding FP32)?  This would make the precision facet comparable across benchmarks and test whether the precision gradient survives. 4.  How were the \\\"optimal\\\" prompt and seed counts in the D-study determined?  Is there a formal optimization procedure, or were these chosen by inspection? 5.  The bootstrap resamples items but not conditions. Have you considered a double bootstrap (resampling both items and conditions)?  This would capture total uncertainty rather than just item-sampling uncertainty. 6.  How do you address the binary data issue in G-theory estimation?  Standard methods assume continuous responses. Have you considered generalized G-theory or a probit/logit link function approach? 7.  The paper claims \\\"current practice G<0.25 everywhere\\\" — what specific \\\"current practice\\\" configuration yields this?  Is this 1 prompt × 1 seed × 200 items × 1 temperature × 1 precision? The baseline should be precisely defined. 8.  For GSM8K and MATH, how were answers extracted from generated text?  The extraction method is a potential confound for binary scoring. 9.  Were the 6 prompt templates the same across all 5 benchmarks?  If so, were they designed for MC format specifically, and how appropriate are they for GSM8K/MATH generation tasks? 10.  The fine-tuning experiment uses item-level accuracy across test set items as the response variable, or run-level aggregate accuracy?  If aggregate, G-theory is applied to a single number per run (N=432), which is a very different statistical regime than item-level analysis (N=432×test_ items). 9. Minor Issues -  The G-theory formula in Eq. 2 uses subscript notation that conflates \\\"conditions\\\" into a single $c$ — for a 5-facet design, the full formula should be shown or a reference to the exact formula used should be provided. -  Table 6 (cross-benchmark) reports 384,000 obs for GSM8K/ARC/HellaSwag but the experimental design (4 models × 2 prec × 6 prompts × 6 seeds × 2 temps × 4 orderings × 200 items) yields 4×2×6×6×2×4×200 = 230,400. The 384,000 figure is inconsistent — please verify. -  The paper switches between \\\"Henderson Method I\\\" (Section 4.6) and \\\"Henderson Method III\\\" (summary). These are different methods — please clarify which was used. -  Several tables show components that do not sum to 100% without explanation. A footnote about rounding and/or the treatment of negative estimates would help. -  The Related Work paragraph on training instability cites Dodge et al. (2020) but the bibliography entry has no venue information beyond \\\"arXiv preprint.\\\" -  The Lu et al. (2022) citation appears to be incorrect — the cited paper is about emergent abilities, not option ordering. Verify this reference. -  The Mesting (2026) bibliography entry says \\\"ACL\\\" but the literature map says \\\"arXiv.\\\" Verify the venue. 10. Score and Confidence Overall Score: 4/6 (Weak Accept) Confidence: High Justification The paper has substantially improved since Dream #1 by: (a) treating model as a crossed facet, (b) adding bootstrap CIs, (c) expanding to 5 benchmarks with a coherent three-tier narrative, (d) reframing infrastructure separability as confirmatory, (e) expanding the bibliography to 18 references (still below the 25+ target but much improved), and (f) acknowledging item dominance as psychometrically expected while emphasizing the benchmark-conditional gradient as the novel contribution. The cross-benchmark variance gradient — the central claim — is well-supported by data across five benchmarks, with honest uncertainty quantification (permutation p=0.003, directional not magnitude claims). The D-study reproducibility budgets fill a genuine practical gap. The metric-conditional finding (G=0.37 vs. G=0.97) is striking and immediately useful. The paper falls short of a clear accept (5/6) due to: (a) binary data in standard G-theory without discussion of the methodological limitation, (b) temperature/ordering as random facets with 2-4 levels is dubious, (c) asymmetric designs across benchmarks confound the cross-benchmark comparison of precision effects, and (d) the separability claim is overstated in the abstract given that 2/5 benchmarks show >2% infra×method interaction. These issues are addressable in revision: -  Add a paragraph discussing binary data limitations and cite generalized G-theory -  Present a sensitivity analysis with temperature as fixed -  Re-analyze MMLU at BF16/FP16 only for the cross-benchmark precision comparison -  Qualify the separability claim in the abstract with \\\"on knowledge benchmarks\\\" If these revisions are made, the paper would be a solid accept (5/6). The experimental scale, honest framing, and actionable D-study budgets make this a useful contribution to the evaluation methodology literature. Comparison to Dream #1 Score (4/6 Borderline Reject → 4/6 Weak Accept) Same numerical score but upgraded from \\\"borderline reject\\\" to \\\"weak accept\\\" in assessment. The Dream #1 review identified 7 actionable revisions; this version addresses 5 of them (model-as-facet, CIs, bibliography expansion, figures described, reframed contributions). The remaining 2 (separability threshold derivation, item dominance tautology acknowledgment) are partially addressed. The net effect is that the paper moves from \\\"below acceptance threshold\\\" to \\\"at the acceptance threshold, contingent on minor revisions.\\\" The methodological concerns raised in this review (binary data, temperature-as-random, asymmetric designs) are new issues not flagged in Dream #1 but are moderate rather than fatal.\\n[05-20 23:35] cli_a974499e77fadbdd: 🌙  [Dream Review Report — best | dream_20260520T222113]  · Overall: weak accept dream_ id: dream_ 20260520T222113\\n tier: best\\n reviewer: R2\\n focus: Novelty, Related Work Positioning, Significance/Impact\\n timestamp: 2026-05-20 Reviewer R2: Novelty, Related Work, and Significance 1. Summary This paper applies Generalizability Theory (G-theory) to LLM evaluation in a multi-benchmark setting, crossing infrastructure facets (numerical precision, GPU hardware) with methodology facets (prompt template, random seed, temperature, option ordering) and a measurement facet (item selection) across five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), six models (7--14B), and 4M+ evaluation records. Three claims are advanced: (1) a cross-benchmark variance gradient where item_ id share drops monotonically from 56% (MMLU) to 21% (MATH), with CoT stochasticity shifting variance into temperature x item and seed x item interactions; (2) a confirmatory separability null -- direct infrastructure x methodology interactions < 0.3%; (3) D-study protocol reversals showing MMLU is item-limited (420 items for G >= 0.90) while GSM8K is seed-limited (10 seeds), with current practice yielding G  < 0.25 everywhere. Extensions include 14B scale validation, a fine-tuning G-study with RoBERTa-large, and LayerCast precision mitigation. 2. Novelty Assessment Claim 1 (Cross-benchmark variance gradient): Moderate-to-high novelty. This is the paper's strongest novel contribution. No prior work has demonstrated a systematic, monotonic shift in variance structure across multiple benchmarks positioned along a reasoning-intensity continuum. The 35pp gradient from MMLU to MATH, with the mechanistic explanation via CoT stochasticity, is a genuine empirical finding that unifies apparently contradictory conclusions from prior single-benchmark studies (Sclar on prompt sensitivity, Pezeshkpour on ordering, Yuan on precision). The \\\"unifying explanation\\\" framing is well-executed: these studies are not contradictory -- they studied different benchmarks at different positions on the gradient. However, the finding that item_ id dominates is expected from measurement theory (Brennan, 2001, Ch. 3). Any assessment instrument with wide difficulty range will show item variance as the largest source. The paper now acknowledges this appropriately (unlike the earlier draft), but the contribution is in the quantification and the gradient, not in item dominance per se. Claim 2 (Confirmatory separability): Low novelty, moderate utility. This is a confirmatory null result. Infrastructure x methodology interactions are  < 0.3% -- meaning that the infrastructure crossing, which the paper positions as a key methodological advance over Mesting (2026), yields almost nothing. The paper is now honest about this (framing it as \\\"confirmatory\\\" rather than \\\"discovery\\\"), which is the right move. The nuanced decomposition into direct vs. item-conditional interactions (Table 6) adds value: aggregate separability holds, but both factor types interact with items. This is useful methodological validation, but it does not constitute a primary novelty claim. The practical implication is clear: researchers running isolated-factor studies (e.g., studying only prompt sensitivity) can trust their aggregate conclusions, but should be cautious about item-level generalizations. This is valuable guidance even if not surprising. Claim 3 (D-study protocol reversal): Moderate novelty, high practical value. The finding that MMLU needs 420 items while GSM8K needs 10 seeds -- and that the facet effectiveness ratio inverts from 14.2:1 (MMLU) to 0.8:1 (GSM8K) -- is actionable and non-obvious. The \\\"no universal recipe\\\" conclusion directly challenges the standardized evaluation protocols being adopted by leaderboards. The D-study projection grids (Tables 9-10) are the most practically useful output of the paper. The current-practice G  < 0.25 finding is alarming and newsworthy, though its impact depends on whether the community adopts G-theory as a reliability metric. The comparison to educational measurement's G >= 0.80 threshold is effective rhetoric. Collective novelty: The three claims together are stronger than any individual claim. The cross-benchmark gradient (Claim 1) explains the protocol reversal (Claim 3), and the separability null (Claim 2) validates the independent study of each factor type. The narrative coherence is good. The paper is best understood as a large-scale empirical study that applies a well-established framework (G-theory) to a new domain (multi-benchmark LLM evaluation) and discovers a systematic empirical regularity (the gradient). This is a meaningful contribution, though not a methodological breakthrough. Incrementality over Mesting (2026). The paper clearly advances over Mesting in three dimensions: (a) five benchmarks vs. one, (b) infrastructure crossing, (c) model as crossed facet. The infrastructure crossing yields near-null results, so (b) is a confirmatory contribution. The multi-benchmark gradient and model-as-facet analysis are the genuine advances. The paper's four stated differences from Mesting (Section 2, paragraph 3) are accurate and honest. One important difference the paper does not sufficiently emphasize: Mesting found judge identity as the dominant variance source (43.8%), while this paper fixes the judge and finds item_ id dominant. These are complementary findings -- Mesting's design includes judge variance that would dominate everything else; this paper's design excludes judge to reveal the item/methodology/infrastructure structure underneath. This complementarity should be discussed more explicitly. 3. Related Work Completeness The bibliography has improved dramatically from the earlier 7-reference draft to 22 references. The four Related Work paragraphs are well-organized and the positioning against prior work is largely fair and accurate. Adequately covered: -  Variance sources in LLM evaluation (Sclar, Pezeshkpour, Lu, Yuan, Biderman) -- good coverage -  ANOVA-based decomposition (Bouthillier, Henderson, Dodge, Sellam, Dehghani) -- well-positioned -  G-theory in NLP (Mesting, Brennan, Shavelson) -- properly cited with explicit differentiation -  IRT in NLP (Lalor, Rodriguez, Polo, Perlitz) -- good, with IRT/G-theory complementarity noted Missing or under-discussed references: 1.  Nalisnick et al. (2024), GeneralizIT  -- a G-theory software package for ML. Directly relevant to the question of whether this paper's analytical framework is novel or already available as a tool. Should be cited in the G-theory paragraph. 2.  Kunievsky et al. (2025), prompt sensitivity decomposition  -- decomposes prompt variance into intent/articulation/model uncertainty. Relevant to interpreting the prompt x item interaction component. The paper's related_ work_ notes mention it but the paper does not cite it. 3.  Brittlebench (2026)  -- prompt brittleness benchmark, ~ 50% prompt variance. In the project's own literature map but absent from the paper. Directly relevant to the prompt facet findings. 4.  Bui et al. (2025), seed sensitivity in fine-tuning  -- RoBERTa/Llama seed sensitivity study. Directly relevant to Section 8.2 (fine-tuning G-study). In the literature map but not cited. 5.  ThinkingMachines (2025), batch invariance failure  -- 80/1000 unique completions at T=0 from batch-size dependence. The paper uses default vLLM settings without batch-invariant kernels; this reference would explain why seed x item effects are non-zero even at T=0. Not cited. 6.  Vania et al. (2021)  -- IRT item properties in NLP. Listed in the bibliography but not discussed in the Related Work text. Should be integrated into the IRT paragraph. 7.  Mizrahi et al. (2024)  -- cited in the introduction but not in Related Work. Multi-prompt evaluation advocacy. Should appear in the variance sources paragraph. Positioning fairness: The paper's positioning against prior work is generally fair. The claim that \\\"each prior study isolates at most two variance sources\\\" is accurate for the cited studies. The differentiation from Mesting is honest and specific. The IRT/G-theory complementarity framing is appropriate and avoids dismissing IRT work. One concern: the paper states that prior ANOVA-based studies \\\"lack the D-study machinery for projecting reliability under alternative designs.\\\" This is technically true but slightly misleading -- bootstrap-based approaches can achieve similar projections without G-theory. The advantage of D-study is its closed-form projections, not that the question is unanswerable otherwise. 4. Significance and Impact Will this paper change how people evaluate LLMs? Partially. The D-study budgets are immediately actionable for benchmark designers and evaluation framework maintainers (e.g., lm-evaluation-harness, HELM). The \\\"G  < 0.25 everywhere\\\" finding is a compelling indictment of current practice. However, adoption depends on: 1.  Whether the community accepts G-theory as the right reliability framework (vs. IRT, bootstrap, or simple confidence intervals) 2.  Whether the computational cost of multi-seed, multi-prompt evaluation is acceptable 3.  Whether leaderboard operators are incentivized to change practices The paper would benefit from a concrete comparison: \\\"Running MMLU with the recommended budget (420 items, 3 prompts, 2 seeds = 2,520 evaluations) costs X GPU-hours per model, compared to Y GPU-hours for current practice.\\\" Without cost estimates, the budgets are theoretical. Are the D-study budgets practically useful? Yes, with caveats. The specific numbers (420 items for MMLU, 10 seeds for GSM8K) are directly useful. The facet effectiveness ratios (Table 12) provide a decision framework. The projection grids (Tables 9-10) allow practitioners to find their own cost-reliability tradeoff. The main limitation is that the budgets are derived from 7-14B open-weight models. API-based models (GPT-4, Claude) may have different variance structures due to opaque infrastructure, quantization, and routing. The paper acknowledges this but does not quantify the risk. Is \\\"no universal recipe\\\" surprising or obvious? Moderately surprising in its specificity. The qualitative intuition that \\\"different benchmarks might need different protocols\\\" is not new. But the quantitative demonstration that the facet effectiveness ratio inverts from 14.2:1 to 0.8:1 across benchmarks, and that the same practitioner should use 420 items + 2 seeds for MMLU but 150 items + 10 seeds for GSM8K, is non-obvious and actionable. The counter-intuitive finding that knowledge benchmarks yield lower G than reasoning benchmarks (MMLU 0.36 vs. GSM8K 0.55 under full factorial) is genuinely surprising and well-explained. 5. Framing and Narrative Strengths: -  The three-claim structure is clean and well-supported. -  The \\\"unifying explanation\\\" framing for the gradient is effective. -  The Discussion section is balanced, with a thorough Limitations paragraph. -  The engine confound discovery is presented with appropriate before/after validation. -  The paper correctly frames infrastructure crossing as confirmatory rather than primary novelty. Weaknesses: -  Zero figures.  This is a serious deficiency for a variance decomposition paper. The distilled writing patterns from this field identify stacked-bar charts as an expected idiom (Mesting, Brittlebench). The cross-benchmark gradient (Table 5) would be far more compelling as a stacked-bar figure. The D-study projections (Tables 9-10) cry out for line plots of G vs. facet allocation. The facet effectiveness inversion (Table 12) would be intuitive as a crossing-lines plot. With 14 tables and 0 figures, the paper is dense and visually monotonous. This is a competitive disadvantage at a top venue. -  The paper title promises \\\"Evaluation Metrics\\\" but delivers only binary scoring.  The abstract and main text focus entirely on binary correct scoring. Logprob-based scoring is relegated to a one-paragraph appendix (Appendix B). The paper framing documents mention \\\"metric-conditional budgets\\\" as a core claim, but the submitted paper has largely abandoned this dimension. Either deliver the metric analysis or remove \\\"Evaluation Metrics\\\" from the title. -  The fine-tuning section (8.2) feels bolted on.  RoBERTa-large fine-tuning on SST-2/MNLI/RTE/COPA is architecturally distant from the 7-14B decoder inference setting. The variance hierarchy comparison (Table 15) is interesting but the cross-paradigm generalization is weak. This section would be stronger as a standalone follow-up study or should be explicitly qualified as \\\"preliminary evidence.\\\" 6. Scope Concerns Is 5 benchmarks x 6 models x 7-14B sufficient? For the cross-benchmark gradient: yes, 5 benchmarks spanning knowledge-to-reasoning is adequate. The monotonic gradient with non-overlapping bootstrap CIs (Table 8) provides statistical support. Adding more benchmarks (e.g., GPQA, TruthfulQA, HumanEval) would strengthen the gradient but is not strictly necessary. For model generality: the 4 x 7-9B models show consistent patterns (per-model tables confirm the gradient within each model), and the 14B extension (Section 8.1) falls within the 8B range. However: 1.  No 70B+ models.  Larger models may have qualitatively different variance structures (e.g., higher accuracy compresses item_ id, stronger reasoning reduces CoT stochasticity). The paper cannot claim generality beyond the 7-14B scale. 2.  No proprietary API models.  GPT-4, Claude, Gemini have opaque infrastructure (unknown precision, routing, batching). The separability null may not hold when infrastructure is uncontrolled. Mesting (2026) studied API models; this paper studies open-weight models. The complementarity is noted but not deeply explored. 3.  No non-English benchmarks.  All five benchmarks are English-only. Cross-lingual variance structure could differ systematically (e.g., tokenization effects on item difficulty). 4.  No generation-based benchmarks.  All benchmarks are multiple-choice or short-answer. Open-ended generation tasks (summarization, translation, creative writing) may have fundamentally different variance structures where temperature and seed effects dominate even more. 5.  Only 200 items per benchmark.  MMLU has ~ 14K items, GSM8K has ~ 8K. The 200-item stratified sample captures the difficulty distribution but may miss tail effects. The resampling stability test (Section 4.3) partially addresses this but only for MMLU. 7. Strengths (bulleted) -  Cross-benchmark variance gradient is a genuine, well-supported empirical contribution  that unifies contradictory findings from prior single-benchmark studies. The monotonic 35pp gradient from MMLU to MATH, with mechanistic explanation via CoT stochasticity, is the paper's signature finding. -  Massive experimental scale : 4M+ evaluation records, 5 benchmarks, 6 models, crossed factorial designs. Few empirical papers in this area match the breadth. -  D-study reproducibility budgets are immediately actionable : specific item/prompt/seed allocations for G >= 0.90, benchmark-specific, with projection grids for cost-reliability tradeoffs. -  Engine confound discovery and correction  (vLLM V0 vs. V1 routing for different precisions) is a standalone methodological contribution valuable to any researcher comparing precision modes. -  Honest framing of the separability null : infrastructure crossing framed as confirmatory rather than primary novelty, with nuanced decomposition into aggregate vs. item-conditional interactions. -  Comprehensive robustness checks : item resampling stability, REML vs. Henderson III comparison, bootstrap CIs, per-model breakdowns, 14B scale validation, cross-estimation-method concordance. -  Bibliography substantially improved  over earlier drafts: 22 references covering variance sources, ANOVA decomposition, G-theory, and IRT literature. -  Counter-intuitive G pattern  (knowledge benchmarks yield lower G than reasoning benchmarks) is well-explained and adds insight beyond the headline gradient finding. 8. Weaknesses (bulleted) -  Zero figures in a variance decomposition paper  is a serious presentation deficiency. Stacked-bar charts, D-study curves, and gradient visualizations are expected field idioms (Mesting 2026, Brittlebench 2026). 14 tables + 0 figures makes the paper dense and hard to scan. -  Infrastructure crossing is the claimed methodological advance over Mesting but yields near-null results  ( < 0.3% direct interactions). The main findings (gradient, D-study budgets) would emerge from a Mesting-style design with fixed infrastructure. The paper is honest about this but it weakens the novelty argument. -  Title promises \\\"Evaluation Metrics\\\" but the paper delivers only binary scoring  in the main text. Logprob analysis is a one-paragraph appendix. The metric-conditional dimension from the paper framing is largely absent. -  No models above 14B.  Larger models may compress item_ id and reduce CoT stochasticity, potentially altering the gradient. Generality claims should be scoped to 7-14B. -  Fine-tuning extension (RoBERTa-large, encoder-only, classification)  is architecturally distant from the decoder inference setting. Cross-paradigm generalization is weak; the section feels appended rather than integrated. -  Missing references : GeneralizIT (2024), Kunievsky et al. (2025), Brittlebench (2026), Bui et al. (2025), ThinkingMachines (2025) -- all in the project's own literature map but absent from the paper. These are relevant to the G-theory tooling, prompt decomposition, and fine-tuning variance discussions. -  No cost analysis for recommended budgets.  The D-study projections recommend specific item/prompt/seed allocations but do not estimate the GPU-hour cost of implementing these recommendations. Without cost, the budgets are theoretical. -  200-item samples from much larger benchmarks.  Resampling stability is tested only for MMLU. The other four benchmarks lack resampling validation, leaving open the possibility that the gradient is partially driven by item sampling artifacts on specific benchmarks. 9. Questions for Authors 1.  The cross-benchmark gradient is your strongest finding. Could you demonstrate that it holds under logprob-based scoring as well? The one-paragraph Appendix B suggests item_ id drops to 42.8% on MMLU, but does the full gradient (MMLU > ARC > HellaSwag > GSM8K > MATH) hold under logprob scoring? If not, is the gradient an artifact of binary scoring thresholds? 2.  Your D-study recommends 420 items + 3 prompts + 2 seeds for MMLU (2,520 total evaluations). How does this compare to Polo et al.'s tinyBenchmarks recommendation for MMLU? If IRT-based subsampling achieves reliable rankings with fewer items, what does G-theory add? 3.  DeepSeek-R1-Distill-14B shows elevated temperature x item (8.8%) and seed x item (5.2%) on MMLU -- above the 8B range (Table 13). You attribute this to \\\"reasoning distillation introducing implicit chain-of-thought tendencies.\\\" Can you verify this mechanistically? Does DeepSeek-R1-Distill-14B produce longer or more variable outputs on MMLU items compared to the other models? 4.  The separability null holds for 2 GPU types (Section 6). How confident are you that this extends to, say, A100 vs. H100 vs. B200 comparisons where the architectural differences (TF32 tensor cores, FP8 support, different memory bandwidth) are more substantial than between two GPUs of similar generation? 5.  You fix the judge model, unlike Mesting who includes judge as a facet. Since Mesting found judge identity as the dominant source (43.8%), your entire variance structure sits \\\"underneath\\\" the judge variance. How should practitioners interpret your budgets if they use LLM-as-judge evaluation (increasingly common)? Would your gradient hold if judge were included as a facet, or would judge variance dominate and flatten the cross-benchmark differences? 6.  The fine-tuning G-study finds item_ id at rank-1 across all tasks (35.8-43.8%). But Bui et al. (2025) report extreme seed variance (RTES variance = 18.22) for RoBERTa on RTE. How do your RTE fine-tuning results compare to Bui et al.? Are the magnitudes consistent? 7.  Current-practice G  < 0.25 is your most alarming finding. Have you computed what fraction of published leaderboard rankings would change if evaluations were repeated with different seeds/prompts? A \\\"rank instability\\\" analysis (e.g., what percentage of model-pair orderings flip under re-evaluation) would make the inadequacy finding more concrete than an abstract G coefficient. 8.  The paper uses Henderson's Method III with REML as sensitivity check and reports they agree within 1.4pp. Have you considered Bayesian variance component estimation (e.g., via Stan or brms)? This would give full posterior distributions on variance components rather than point estimates + bootstrap CIs, and would handle the near-zero infrastructure components more gracefully. 10. Minor Issues -  Table 5 header says \\\"4 models pooled\\\" but the design description mentions \\\"4 models x 2 precisions x ...\\\" -- clarify whether model is pooled or crossed in this analysis. -  Table 7 (5-benchmark gradient) shows G_ full for GSM8K (0.55) higher than MATH (0.50), breaking the monotonic pattern. The text does not explain this reversal; add a brief note. -  The abstract says \\\"over 4 million evaluation records\\\" but summing the reported record counts (1,036,800 + 1,382,400 + 460,800 + 691,200 + 345,600 + 172,800 + fine-tuning) exceeds 4M. Provide an exact total or say \\\"approximately.\\\" -  Section 3.2 says \\\"2-3 levels\\\" for temperature but does not specify which benchmarks use 2 vs. 3 levels. Clarify. -  Table 1 (MMLU variance): the \\\"infra x method\\\" row aggregates multiple interaction terms. Break this out or provide the individual terms in an appendix. -  The paper references \\\"Section 7\\\" (comprehensive analysis) as Section \\\\ref{sec:comprehensive} but the numbering in the LaTeX may not match if figures are added later. Verify cross-references. -  Appendix C on higher-order interactions is interesting (temp x seed x item = 1.8%) but could be expanded. Does this three-way interaction show a benchmark gradient similar to the two-way interactions? 11. Score Score: 4/6 (Weak Accept) This is a well-executed, large-scale empirical study that applies G-theory to multi-benchmark LLM evaluation and discovers a genuine empirical regularity (the cross-benchmark variance gradient). The D-study budgets are practically useful, the experimental scale is impressive, and the paper has improved substantially from earlier drafts -- the bibliography is now adequate, the framing is honest about confirmatory vs. novel contributions, and the robustness checks are thorough. The cross-benchmark gradient as a unifying explanation for contradictory prior findings is the paper's strongest contribution and clears the novelty bar for a top venue. The paper is held back by: (a) zero figures, which is a serious presentation weakness for a variance decomposition paper; (b) the infrastructure crossing being the claimed advance over Mesting yet yielding near-null results; (c) missing metric-conditional analysis despite the title; and (d) scope limitations (7-14B only, no API models, encoder-only fine-tuning). The first issue (figures) is easily fixable and would likely move the paper to a solid accept. The others are structural but not disqualifying. The balance tips toward accept because the cross-benchmark gradient is genuinely novel, the D-study budgets fill a real practical gap, and the \\\"G  < 0.25 everywhere\\\" finding is an important wake-up call for the field. The paper would benefit from another revision addressing the figure deficit and the metric-conditional analysis, but the core contribution is sound. 12. Confidence Confidence: High I am familiar with G-theory (Brennan 2001, Shavelson & Webb 1991), the LLM evaluation reproducibility literature (Sclar, Pezeshkpour, Yuan, Biderman, Mesting), and the IRT/benchmark efficiency literature (Polo, Rodriguez, Perlitz). I have reviewed the full paper text, the related work notes, and the paper framing documents. My main uncertainty is whether models above 14B would substantially alter the gradient pattern -- this is an empirical question the paper cannot answer with its current design.\\n[05-20 19:51] cli_a974499e77fadbdd: 🌙  [Dream Review Report — worst | dream_20260520T190053]  · Overall: weak reject Dream Review Report — Full Roundtable Paper : \\\"No Universal Reproducibility Recipe: Variance Attribution in LLM Evaluation Is Benchmark-Conditional and Model-Conditional\\\" Review mode : full |  Reviewers : R1 (Methods+Experiments), R2 (Novelty+Related Work) Step 1: Independent Reviews Reviewer 1 — Methods & Experiments Summary : The paper applies G-theory to decompose LLM evaluation variance across 4 models, 5 benchmarks, and 172,800+ inference conditions plus a fine-tuning G-study. The experimental scale is ambitious and the float32 confound discovery is a genuine contribution. However, critical methodological gaps—residual dominance, missing uncertainty quantification, and a blocked hardware experiment—undermine the strength of the claims. Strengths : 1.  Large-scale factorial design : 4 models × 5 benchmarks with multiple crossed facets represents the most comprehensive G-theory study in LLM evaluation to date. The 172,800 MMLU records provide genuine statistical power. 2.  Float32 confound discovery : The identification of vLLM V1/V0 backend routing as a confound that inflated item variance from 24% to 58% is a standalone methodological contribution. The fix (enforce_ eager=True on V0) is immediately actionable. 3.  Honest reporting of failures : The paper transparently reports the blocked hardware experiment (exp-003), partial 14B results, and the confound discovery that invalidated the original hypothesis. This intellectual honesty is commendable. 4.  Fine-tuning G-study is genuinely novel : No prior work has applied G-theory to decompose fine-tuning variance. The finding that learning rate dominates (17.8%) with a 10% lr×seed interaction, and inference-training decorrelation (r=0.15), are new and useful. 5.  D-study projections are practically useful : Showing that optimal allocations diverge qualitatively across benchmarks (MMLU: more items; GSM8K: more seeds) is actionable advice. Weaknesses : 1.  Residual dominance is the paper's Achilles heel  (Tables 1, 3, 5). Residual is the largest component on ALL benchmarks (20–40%). Combined with the opaque \\\"all other\\\" category (26.5% in Table 1), over 54% of MMLU variance is unexplained or aggregated. For a paper whose contribution is variance  attribution , having the majority of variance  unattributed  is a serious problem. The paper does not adequately discuss what these missing sources might be, nor does it attempt higher-order interaction estimation to decompose the residual. 2.  No confidence intervals or uncertainty quantification . Variance component estimates are reported as point estimates without bootstrap CIs, jackknife intervals, or any measure of estimation uncertainty. G-theory provides standard methods for this (Brennan 2001, Ch. 8). Without CIs, we cannot assess whether the differences between benchmarks or models are statistically meaningful or within estimation noise. For example, is item_ id=24% on MMLU vs 22% on ARC a real difference or sampling variability? 3.  Single GPU architecture severely limits \\\"infrastructure\\\" claims . Experiment 3 (multi-hardware) was blocked. The paper's title and framing reference \\\"infrastructure\\\" factors, but only numerical precision on one GPU type was tested. The finding that \\\"direct infrastructure×methodology interaction  < 0.5%\\\" (Table 4) applies only to precision, not hardware broadly. This should be reflected in the title/abstract. 4.  Model is not treated as a G-theory facet . The per-model decompositions (Table 1) show item_ id ranging from 13.8% (Mistral) to 30.2% (Gemma), suggesting strong model×item interaction. But model is analyzed as a stratification variable, not a facet in the G-study design. A model-as-facet reanalysis of the existing MMLU data (no new experiments needed) would properly attribute this variance and likely reduce the residual. 5.  Fine-tuning G-study uses RoBERTa-large  — an encoder-only model from 2019 — on classification tasks. The relevance to modern LLM fine-tuning (decoder-only models, generation tasks, RLHF/DPO) is questionable. The paper acknowledges this in Limitations but the mismatch weakens the \\\"fine-tuning contribution\\\" claim substantially. 6.  200 items per benchmark : While adequate for point estimation, the paper does not report sensitivity analyses (e.g., split-half reliability of the variance decomposition, or bootstrap resampling of items) to establish stability. Different 200-item samples from the same benchmark could yield different decompositions, especially for benchmarks with heterogeneous item pools. 7.  REML vs actual estimation method : The paper states \\\"Variance components are estimated via Restricted Maximum Likelihood (REML)\\\" (Section 3.1) but does not describe the actual implementation. If Henderson Method I (ANOVA-based) was used instead, this is a methodological misrepresentation that matters when variance components are near zero (negative estimates under Henderson are truncated differently than under REML). Questions for Authors : 1.  Can you provide bootstrap CIs (e.g., 1000 resamples of items) for the variance components in Tables 1 and 3? This would address whether cross-benchmark differences are real. 2.  What happens if model is included as a random facet in the MMLU G-study rather than stratified out? How much of \\\"all other\\\" and \\\"residual\\\" is actually model×item interaction? 3.  What specific variance estimation method was implemented? REML, Henderson I, or Henderson III? 4.  Have you examined three-way interactions (e.g., model×prompt×item) that might explain the large residual? Score : 3/6 (Weak Reject)\\n Confidence : 4/5 Reviewer 2 — Novelty & Related Work Summary : The paper extends Mesting [ 2026 ]'s single-benchmark G-theory study to multiple benchmarks and adds a fine-tuning G-study. The central contribution is a negative result (no universal variance structure), which is valid but incrementally novel. The related work section is severely underdeveloped with only 7 references, missing critical prior work on ML reproducibility, IRT-based item analysis, and benchmark efficiency. Strengths : 1.  Cross-benchmark variance gradient is a genuine empirical contribution . Showing that variance structure systematically shifts from item-conditional (MMLU) to seed/temperature-conditional (GSM8K/MATH) as benchmarks move from knowledge retrieval to chain-of-thought reasoning is new and interpretable. 2.  D-study allocation divergence has immediate practical value . The finding that MMLU needs 500 items × 2 prompts × 1 seed while GSM8K needs 250 items × 4 prompts × 4 seeds (Table 7) is directly actionable for benchmark designers. 3.  The confound discovery is a standalone contribution  regardless of the paper's other claims. Documenting that vLLM V0/V1 routing inflates variance estimates warns the community about similar artifacts. 4.  Inference–training decorrelation (r=0.15)  is a novel finding that challenges the assumption that inference-time reproducibility insights transfer to training-time settings. Weaknesses : 1.  Incremental novelty over Mesting [2026] . The paper's claimed advance over Mesting is (a) adding precision as an infrastructure facet and (b) crossing benchmarks. But precision turns out to be a near-null factor ( <1.5% main effect post-fix), so the infrastructure extension yields almost nothing. The paper's strongest findings (benchmark-conditional variance, D-study divergence) would largely emerge from a Mesting-style design without infrastructure crossing. 2.  Severely inadequate bibliography . 7 references for a top-venue submission is far below standards. Critical omissions include:   -  Bouthillier et al. (2021, JMLR) : \\\"Accounting for Variance in Machine Learning Benchmarks\\\" — directly relevant, uses variance decomposition in ML evaluation.   -  Dodge et al. (2020, EMNLP) : Fine-tuning instability — essential context for the fine-tuning G-study.   -  Sellam et al. (2022) : MultiBERTs — multi-seed BERT training, directly relevant to seed variance.   -  Dehghani et al. (2021) : \\\"The Benchmark Lottery\\\" — benchmark selection effects.   -  Polo et al. (2024) : tinyBenchmarks — item subsampling for efficient evaluation, directly relevant to item variance.   -  Rodriguez et al. (2021) : IRT-based evaluation for NLP — alternative item-level analysis framework.   -  Shavelson & Webb (1991) : Foundational G-theory reference beyond Brennan (2001).   -  Henderson et al. (2018) : Deep RL reproducibility — established the multi-factor variance decomposition paradigm in ML.   -  Biderman et al. (2024) : Lessons from evaluation reproducibility.   -  Any ordering effects literature (the paper includes ordering as a facet but cites no prior work on option ordering effects). 3.  \\\"Diagnostic tool\\\" contribution is unsubstantiated . The paper claims G-theory as a \\\"practical diagnostic tool\\\" but releases no software, no analysis pipeline, no reusable framework. The \\\"tool\\\" is just applying G-theory, which Mesting [ 2026 ] already demonstrated. GeneralizIT and similar R packages already exist. Without a released tool, this contribution claim is empty. 4.  The negative result framing needs more work . \\\"No universal recipe\\\" is the central claim, but many practitioners already assume this. The paper confirms a suspicion with data but doesn't offer constructive solutions beyond \\\"diagnose your pipeline\\\" — which requires the very G-theory study the paper just demonstrated is expensive (172,800 conditions for one benchmark). Is the recommendation scalable? 5.  Zero figures is unusual and harmful . For a paper about variance decomposition across benchmarks, visual comparisons (stacked bars, heatmaps, radar charts) would dramatically improve readability. The reliance on 11 tables makes the paper harder to parse and less compelling than it could be. 6.  \\\"Fully crossed\\\" is overstated . Only Experiment 1 (MMLU) uses the full crossing (3 precisions × 6 prompts × 6 seeds × 3 temps × 4 orderings). Experiments 2 and the MATH extension use a reduced crossing (2 precisions × 2 temps). This is fine practically but should not be described as a \\\"fully-crossed design spanning 5 benchmarks\\\" in the abstract. 7.  Item dominance on knowledge benchmarks is partially expected from measurement theory . Items in MMLU span from trivially easy to near-impossible across 57 subjects. A large item variance component is expected given this difficulty range. The paper would benefit from contextualizing this against IRT-based item analysis. Questions for Authors : 1.  How does this work relate to Bouthillier et al. (2021), which also decomposed variance in ML benchmarks? 2.  Is the recommendation to run a full G-study per benchmark practical? What is the computational cost, and is there a lightweight diagnostic alternative? 3.  Why were no figures included? The knowledge-reasoning gradient would be far more compelling as a visualization. 4.  Can you release the analysis code alongside the data to substantiate the \\\"diagnostic tool\\\" claim? Score : 3/6 (Weak Reject)\\n Confidence : 4/5 Step 2: Cross-Sharing R1 → R2 : The methodological concerns (54% unexplained variance, no CIs, model not as facet) mean the \\\"no universal recipe\\\" finding may partly reflect an underspecified decomposition model rather than a genuine property of evaluation variance. If the residual were decomposed further (e.g., via three-way interactions or model-as-facet), the cross-benchmark differences might narrow or change qualitatively. R2 → R1 : The thin related work compounds the experimental concerns. Without positioning against Bouthillier et al., tinyBenchmarks, or IRT-based approaches, it's unclear whether G-theory adds diagnostic power beyond existing methods. The fine-tuning contribution is further weakened because Dodge et al. (2020) already documented seed sensitivity in fine-tuning — the G-theory framing is new but the phenomenon is not. Step 3: Convergence Points of agreement : -  The paper addresses an important problem (evaluation reproducibility diagnosis) -  The float32 confound discovery is a genuine, standalone contribution -  The cross-benchmark variance gradient is an interesting empirical finding -  Residual dominance (largest component everywhere) is the most serious methodological concern -  Missing statistical uncertainty quantification (no CIs) is a critical gap -  Single GPU limits infrastructure claims; the title/abstract overclaim relative to what was tested -  Related work is severely underdeveloped (7 references) -  Zero figures hurts presentation significantly -  Fine-tuning G-study is novel in framing but limited by RoBERTa on classification tasks -  The \\\"diagnostic tool\\\" contribution is claimed but not delivered (no released software) Points of mild disagreement : -  R1 is slightly more positive about the experimental scale and sees the multi-benchmark extension as substantive; R2 views it as more incremental over Mesting -  R2 emphasizes the bibliography gap more; R1 emphasizes the statistical rigor gap more Converged assessment : Both reviewers agree the paper falls below the acceptance threshold for a top ML venue in its current form, despite addressing a real problem with interesting findings. The gap between claims and delivered evidence is too large. Step 4: Consolidated Assessment Overall Score: 3/6 — Weak Reject Headline Assessment An ambitious and honest study that surfaces interesting empirical patterns (benchmark-conditional variance, float32 confound, inference-training decorrelation), but falls short of top-venue standards due to (1) the majority of variance remaining unattributed, (2) no uncertainty quantification on variance estimates, (3) severely thin related work, and (4) overclaiming relative to what was tested (single GPU ≠ \\\"infrastructure\\\"). What Would Change Our Minds (Revision Guidance) Essential (any two would likely move to borderline) : 1.  Bootstrap CIs on all variance components  (Tables 1, 3, 5, 9). This is feasible with existing data and would establish whether cross-benchmark differences are statistically meaningful. 2.  Model-as-facet reanalysis  of MMLU data to properly attribute model×item interaction and reduce the opaque residual/all-other categories. No new experiments needed. 3.  Expand bibliography to ≥25 references , including Bouthillier et al. (2021), Dodge et al. (2020), Sellam et al. (2022), Polo et al. (2024), Rodriguez et al. (2021), Shavelson & Webb (1991), Henderson et al. (2018), and ordering effects literature. Position contributions clearly against each. 4.  Add 3-4 figures : at minimum a stacked bar comparison across benchmarks, and a D-study projection curve. The paper is currently 11 tables and 0 figures. Important (would strengthen but not alone sufficient) :\\n 5. Downscope \\\"infrastructure\\\" claims to \\\"numerical precision\\\" throughout, including title consideration.\\n 6. Release analysis code (not just data) to substantiate the \\\"diagnostic tool\\\" contribution.\\n 7. Discuss what the large residual might contain and whether higher-order interactions or additional facets (e.g., batch size, system prompt) could reduce it.\\n 8. Clarify the exact variance estimation method (REML vs Henderson) and justify the choice. Desirable (for camera-ready) :\\n 9. Fine-tuning extension to at least one decoder-only model on a generation task.\\n 10. Sensitivity analysis: split-half reliability of variance decompositions across different 200-item samples. Contribution Ranking 1.  Float32 confound discovery  — strongest, standalone, immediately actionable ★★★★ 2.  Cross-benchmark variance gradient  — interesting empirical finding, needs CIs ★★★ 3.  D-study allocation divergence  — practically useful, well-presented ★★★ 4.  Inference-training decorrelation  — novel but limited by RoBERTa scope ★★☆ 5.  G-theory as diagnostic tool  — claimed but not delivered (no software) ★★ 6.  \\\"No universal recipe\\\" as central thesis  — valid but not constructive enough ★★ Experiment Coverage Assessment The paper covers 7 of 8 planned experiments (exp-003 blocked, acknowledged). Coverage is thorough. The main gap is not missing experiments but missing  analyses  on existing data (CIs, model-as-facet, higher-order interactions). Venue Fit The paper fits an evaluation/benchmarking track (e.g., NeurIPS Datasets & Benchmarks, COLM, or an EMNLP evaluation workshop). For a main-track top venue, the negative-result framing needs a stronger constructive component (released tool, lightweight diagnostic protocol, or a concrete evaluation standard proposal).\\n[05-20 19:49] cli_a974499e77fadbdd: 🌙  [Dream Review Report — worst | dream_20260520T190053]  · Overall: borderline reject Reviewer R1: Methods and Experiments 1. Summary This paper applies Generalizability Theory (G-theory) to decompose variance in LLM evaluation across infrastructure (numerical precision), methodology (prompt, seed, temperature, ordering), and measurement (item selection) facets. Across 4 models, 5 benchmarks, and 172,800+ records per full-crossing experiment, the authors report that variance attribution is benchmark-conditional and model-conditional: on MMLU item_ id=24% is the largest attributable source after confound correction, while on GSM8K and MATH seed x item and temperature x item interactions dominate. A float32 engine confound in vLLM is identified and corrected. D-study projections show that optimal measurement allocations diverge qualitatively across benchmarks, undermining any universal reproducibility recipe. A fine-tuning extension (RoBERTa-large, 1,728 runs) reveals an inverted variance hierarchy where learning rate (17.8%) and lr x seed interaction (10%) dominate. 2. Strengths 1.  Scale and systematic design.  The fully-crossed factorial on MMLU (4 models x 3 precisions x 6 prompts x 6 seeds x 3 temperatures x 4 orderings x 200 items = 172,800 records) with consistent confound control (V0 enforce_ eager across all precision modes) is a genuinely impressive experimental effort. The extension across 5 benchmarks and 6 models (4x8B + 2x14B) provides breadth rarely seen in evaluation methodology papers. 2.  Float32 engine confound discovery is a standalone contribution.  The identification that vLLM routes float32 to V1 backend versus V0 for BF16/FP16, inflating item variance from 24% to 58% (pre-fix MVP value), is a valuable methodological finding. The before/after comparison (Table 1 vs. MVP) is convincing and has immediate practical implications for any study using vLLM with mixed precision conditions. This finding alone justifies a methods paper. 3.  Honest reframing around negative results.  The title and framing acknowledge that the original hypothesis (item dominance as universal) did not survive cross-benchmark replication. Reporting that item dominance fails on 0/4 benchmarks outside MMLU (Table 4 in cross-benchmark replication) and that variance structure is benchmark-conditional is scientifically responsible. 4.  Benchmark-conditional variance gradient is well-supported.  The systematic pattern across 5 benchmarks -- item_ id declining (MMLU 24% -> GSM8K 12% -> MATH 10%), residual increasing (28% -> 35% -> 40%), temperature x item increasing (5.5% -> 18% -> 15%) -- is a clean empirical finding with a plausible mechanistic account (CoT length amplifies sampling noise, r=0.65). 5.  D-study allocation divergence is practically valuable.  The demonstration that optimal allocation strategies differ qualitatively across benchmarks (MMLU: 500 items x 2 prompts x 1 seed; GSM8K: 250 items x 4 prompts x 4 seeds for a fixed budget of 1000 conditions) is immediately actionable and fills a gap no prior work addresses. 6.  Fine-tuning extension adds genuine novelty.  The first G-theory decomposition of fine-tuning variance with a fully-crossed design (6 seeds x 3 LR x 4 shuffles x 3 GPUs x 2 precisions) reveals learning rate dominance (17.8%) and the lr x seed interaction (10%). The inference-training variance correlation of r=0.15 is a useful negative finding showing that inference-based reproducibility budgets cannot guide training-time decisions. 7.  Generation-based evaluation protocol.  Following Hua et al. (EMNLP 2025) to avoid log-likelihood scoring artifacts that inflate apparent prompt sensitivity reflects careful experimental design awareness. 3. Weaknesses Major (W1) Over 54% of total variance is unexplained or aggregated in the MMLU analysis.  Table 1 shows residual=27.9% and \\\"all other\\\"=26.5%, meaning 54.4% of total variance is either unmodeled or lumped into an opaque category. The \\\"all other\\\" row is not defined -- it presumably aggregates minor two-way interactions and possibly some bookkeeping artifact, but the paper does not specify which components it contains or their individual magnitudes. For a paper whose entire contribution rests on variance attribution, having the majority of variance unattributed is a fundamental problem. The reader cannot assess whether item_ id's 24% is genuinely the \\\"largest attributable source\\\" without knowing what is inside \\\"all other.\\\" If \\\"all other\\\" contains, say, a single three-way interaction at 15%, the variance hierarchy could look quite different. (W2) Model is pooled rather than treated as a G-theory facet.  The paper pools 4 models and decomposes variance across the pooled data, but \\\"model\\\" is not included as a facet in the G-study. In G-theory, model should either be the object of measurement (differentiation facet) or a crossed facet. By pooling, model-level variance and model x item interaction are absorbed into item_ id and residual respectively. The per-model analyses (Table 1 showing Mistral-7B with item=13.8% vs. Gemma-2 with item=30.2%) demonstrate that model x item interaction is substantial, yet this is never estimated as a separate variance component. The Mistral anomaly (residual=38.2%) likely reflects model x higher-order interactions being dumped into residual. This design choice fundamentally undermines the headline variance decomposition. A proper model-as-facet analysis would separate model x item interaction and almost certainly reduce item_ id's attributed share further while revealing how much of the \\\"residual\\\" is actually structured model x condition interaction. (W3) ANOVA-based estimation is used but the paper's methodological framing implies REML.  The code ( variance_decomposition.py ) implements classical ANOVA-based Henderson Method I estimation: it computes Type-I sums of squares, derives mean squares, and solves Expected Mean Square equations for variance components. Negative estimates are truncated to zero. This is not REML. REML uses restricted maximum likelihood via iterative optimization (e.g., Fisher scoring, EM) and handles boundary constraints differently (constrained optimization rather than truncation). The distilled research skill cites Mesting (2026) as using \\\"REML + D-study\\\" and positions this work as methodologically comparable. If the paper claims or implies REML while implementing ANOVA-based estimation, this is a misrepresentation that a psychometrics-aware reviewer would catch immediately. The two methods can yield different results, especially with unbalanced cells or when negative variance components arise (the truncation-to-zero approach inflates other components' relative shares). (W4) Bootstrap CIs are structurally incomplete across experiments.  The code computes bootstrap CIs for all components on MMLU (exp-001), but the paper summary provides CIs only selectively. For the cross-benchmark experiments (exp-002), the 14B extension (exp-005), and the fine-tuning study (exp-006), no confidence intervals are reported. This is especially problematic for: (a) the separability claim, where \\\"direct infra x method < 0.5%\\\" needs a CI to be interpretable -- is the CI [ 0.0%, 3.0%] or [ 0.3%, 0.7%]?; (b) the cross-benchmark gradient, where overlapping CIs on item_ id shares across benchmarks would weaken the \\\"qualitatively different\\\" claim; (c) the fine-tuning lr dominance claim (17.8%), where the CI width determines whether lr is statistically distinguishable from item_ id (13.8%). Without CIs on all reported variance components, the paper is presenting point estimates as if they were precise measurements. (W5) Experiment 3 (multi-hardware) is blocked, fatally weakening the separability claim.  The paper claims to test \\\"infrastructure vs. methodology separability\\\" but the only infrastructure facet actually crossed is numerical precision. Without a second GPU type, the paper cannot distinguish hardware-specific from hardware-universal variance. The separability claim must be scoped to \\\"precision vs. methodology\\\" rather than \\\"infrastructure vs. methodology.\\\" This is not merely a limitation -- it undermines the paper's positioning relative to its stated contribution of being the \\\"first fully-crossed G-theory study spanning infrastructure x methodology.\\\" With only precision as the infrastructure proxy, the study is methodologically closer to Mesting (2026) than advertised, differing primarily in adding precision as a facet rather than adding \\\"infrastructure\\\" broadly. Moderate (W6) Experiment 5 (14B) has no hardware crossing and only 2 models, making scale claims unreliable.  With n=2 (Qwen3-14B and DeepSeek-R1-Distill-14B), the 14B extension cannot separate model scale from architecture effects. DeepSeek-R1-Distill-14B is a reasoning-distilled model with fundamentally different generation characteristics (item=10%, residual=42%), making it an inappropriate comparison partner for studying \\\"scale effects.\\\" The paper acknowledges this but still draws conclusions about scale invariance/variance that are confounded with architecture. (W7) Temperature and precision levels differ across experiments without justification.  Exp-001 uses 3 precisions x 3 temperatures x 4 orderings on MMLU. Exp-002 uses 2 precisions x 2 temperatures on GSM8K/ARC/HellaSwag. This means the cross-benchmark comparison in Tables 3-4 is confounded with design differences: the reduced crossing on non-MMLU benchmarks means fewer levels of temperature and precision, which mechanically reduces their estimated variance shares. A fair cross-benchmark comparison requires identical factorial designs. The paper does not discuss how design asymmetry affects the comparability of variance component estimates. (W8) All three-way and higher interactions are absorbed into the residual.  With 6 facets, there are 20 three-way interactions, 15 four-way, 6 five-way, and 1 six-way -- 42 higher-order terms total, all dumped into \\\"residual.\\\" The residual ranges from 20-40% across experiments. Some of this is likely structured: for instance, precision x temperature x item is plausible given that both precision x item (3.5%) and temperature x item (5.5%) are non-trivial on MMLU. If even one three-way interaction accounts for 5-8% of total variance, the relative ranking of two-way components would shift. The paper neither estimates selected three-way interactions nor discusses this confound in the residual. (W9) D-study projections assume items are sampled from an infinite universe.  The G-theory D-study formula G = sigma_ tau / (sigma_ tau + sigma_ delta/n) assumes random sampling from an infinite item universe. Benchmark items are curated, finite collections. For MATH (G=0.30, recommending 2200 items for G>=0.90 when only 5000 items exist in the full benchmark), the extrapolation is questionable. For GSM8K (recommending 1400 items), similar concerns apply. The paper acknowledges infeasibility but does not discuss the statistical invalidity of extrapolating finite-population variance components to hypothetical infinite-population D-study projections. (W10) Fine-tuning experiment uses RoBERTa-large (355M, encoder-only) rather than a decoder-only model.  The architectural mismatch between the inference experiments (7-14B decoder-only autoregressive models) and the fine-tuning experiment (encoder-only classification model) weakens cross-paradigm generalization claims. Fine-tuning a decoder model (e.g., Llama-3.1-8B with LoRA on a generation task) would make the inference-vs-fine-tuning variance hierarchy comparison far more credible. As designed, the fine-tuning experiment measures a fundamentally different computational process (classification head fine-tuning vs. autoregressive generation), making the r=0.15 correlation between inference and training variance structures potentially an artifact of architectural mismatch rather than a deep insight about variance structure differences. Minor (W11) The Kruskal-Wallis test (H=47.3, p<0.001) is underspecified.  What is being compared? Per-item variance contributions across benchmarks? With k=5 benchmarks and point estimates derived from different experimental designs (different numbers of levels), the test's assumptions (independent samples from the same distribution family) may not hold. The degrees of freedom and sample sizes per group are not reported. (W12) No multiple comparison correction.  Multiple bootstrap CIs and permutation tests are computed without family-wise error rate correction (Bonferroni, Holm, or FDR). With 11+ variance components per experiment and 7+ experiments, the number of implicit hypothesis tests is substantial. (W13) The \\\"all other\\\" category in Table 1 (26.5%) is not decomposed.  This catch-all category is almost as large as residual (27.9%) and larger than item_ id (24.0%). Presenting an aggregated \\\"all other\\\" without itemizing its constituents is unusual for a variance decomposition paper and prevents readers from understanding the full variance structure. 4. Questions for Authors 1.  Why is \\\"model\\\" not included as a facet in the G-study? The per-model results (Table 1) show item_ id ranges from 13.8% (Mistral) to 30.2% (Gemma-2) -- this 16.4pp range suggests substantial model x item interaction. If model were a facet, how much of the current item_ id and residual estimates would be reclassified as model x item interaction? 2.  What exactly is in the \\\"all other\\\" category (26.5% in Table 1)? Please enumerate all components and their individual estimates. Is this a sum of small two-way interactions, or does it include terms that individually exceed 5%? 3.  The code ( variance_decomposition.py ) uses ANOVA-based Henderson Method I estimation with truncation of negative variance components to zero. Does the paper describe this correctly, or does it claim REML? If ANOVA-based, have you verified exact balance (every cell has the same number of observations) across all experiments? 4.  Why do the factorial designs differ between MMLU (3 precisions, 3 temperatures) and the other benchmarks (2 precisions, 2 temperatures)? How does this design asymmetry affect the comparability of cross-benchmark variance component estimates? 5.  Can you provide bootstrap CIs for the total direct infrastructure x methodology interaction on each benchmark? The 0.5% point estimate for separability requires uncertainty quantification. 6.  The D-study recommends 2200 items for MATH to reach G>=0.90, but MATH has only 5000 items total. At what point does the finite-population assumption break the D-study framework? Have you considered finite-population corrections? 7.  Have you tested any three-way interactions (e.g., precision x temperature x item, prompt x seed x item)? Given residual accounts for 28-40% across experiments, some of this may be structured and recoverable. 8.  For the fine-tuning experiment, why was RoBERTa-large chosen instead of fine-tuning one of the same decoder-only models used in the inference experiments (e.g., Llama-3.1-8B with LoRA)? How confident are you that the r=0.15 inference-training correlation reflects a genuine structural difference rather than an architectural mismatch artifact? 9.  The inference-training variance correlation (r=0.15) is computed between what exactly? Variance component shares? G coefficients? Per-item accuracy variance? The operationalization is unclear. 10.  Mistral-7B shows a qualitatively different variance profile (item=13.8%, residual=38.2%) compared to the other three 8B models. Is this anomaly investigated? Could it indicate that the G-theory facet structure is model-inappropriate for certain architectures? 5. Missing Experiments or Analyses 1.  Model as a crossed facet.  Re-analyze the MMLU data with model as a 7th facet (or as the object of measurement). This requires no new data collection and would resolve the most fundamental methodological concern. 2.  Three-way interaction estimation.  Fit at least the theoretically motivated three-way interactions (precision x temperature x item, prompt x seed x item, prompt x temperature x item) to determine how much of the residual is structured. This also requires no new data. 3.  Dual-metric analysis.  Decision D002 describes radically different variance structures for binary correct (item_ id=58.4%) vs. text exact match (prompt x item=37.5%). This analysis appears to have been planned but dropped. Including it would demonstrate metric sensitivity, which strengthens the \\\"no universal recipe\\\" argument. 4.  Sensitivity analysis for the separability threshold.  Rather than a binary pass/fail at 0.5%, report the full bootstrap distribution of total direct infrastructure x methodology interaction and let readers judge. 5.  ANOVA vs. REML comparison.  Run the same data through a proper REML implementation (e.g., lme4 in R, or statsmodels MixedLM in Python) and compare results. This validates or invalidates the ANOVA-based approach and is a single-afternoon analysis task. 6.  Finite-population correction for D-study.  For benchmarks with small item pools (MATH: 5000, ARC: ~ 2590), apply finite-population corrections to the D-study projections and report adjusted G coefficients. 7.  Decoder-only fine-tuning comparison.  Even a small-scale LoRA fine-tuning experiment with Llama-3.1-8B on one task would dramatically strengthen the inference-vs-fine-tuning comparison. 6. Score Score: 3/6 (Weak Reject) The paper presents substantial experimental effort and several genuine contributions (engine confound discovery, benchmark-conditional variance gradient, D-study allocation divergence). However, the methodological execution has fundamental gaps: (1) over 54% of variance is unexplained or aggregated into opaque categories; (2) model is pooled rather than treated as a facet, confounding the core variance decomposition; (3) the estimation method may be misrepresented; (4) the blocked hardware experiment undermines the central \\\"infrastructure vs. methodology\\\" framing; (5) cross-benchmark comparisons use non-identical factorial designs. These are not cosmetic issues -- they affect the validity of all three central claims. The contributions that survive scrutiny (confound fix, benchmark gradient, fine-tuning decomposition) are individually interesting but do not cohere into a unified paper at the current level of methodological rigor. Most concerns are addressable without new experiments (model-as-facet reanalysis, three-way interactions, dual-metric analysis, proper CIs), but the revision scope is substantial. 7. Confidence Confidence: 4/5 (High) I have expertise in experimental design, variance decomposition methods, and G-theory applications. I verified claims against the actual analysis code ( variance_decomposition.py ,  d_study.py ) and cross-referenced the experimental plan against reported results. My main uncertainty is whether the paper text (which I reviewed via summary rather than the full manuscript) accurately represents the estimation method -- the ANOVA-vs-REML concern is based on the code, which is definitive, but the paper's textual claims may differ from what I infer.\\n[05-20 19:49] cli_a974499e77fadbdd: 🌙  [Dream Review Report — best | dream_20260520T190053]  · Overall: weak reject dream_ id: dream_ 20260520T190053\\n tier: best\\n reviewer: R2\\n focus: Novelty and Related Work\\n timestamp: 2026-05-20T20:15:00+00:00 Reviewer R2: Novelty and Related Work 1. Summary This paper applies Generalizability Theory (G-theory) to LLM evaluation, crossing infrastructure facets (hardware, numerical precision) with methodology facets (prompt, seed, temperature, ordering) and item selection as the measurement facet. Across 6 models, 5 benchmarks, and 2M+ evaluation records, it finds that item selection dominates variance (42--58%), infrastructure--methodology interactions are negligible (<0.5%), and current evaluation practices yield G  < 0.40. D-study projections provide reproducibility budgets, and a fine-tuning extension shows an inverted variance hierarchy. A vLLM engine confound (FP32 using a different backend) is identified and corrected. 2. Strengths 1.  The cross-benchmark variance gradient is a genuine empirical contribution.  Showing that item dominance systematically weakens from 58.4% (MMLU) to 42.1% (MATH) as task difficulty and reasoning demands increase, with temperature x item and seed x item interactions correspondingly increasing, is a well-supported quantitative finding. This gradient was intuited but never measured across this many benchmarks in a unified framework. It explains why prior single-benchmark studies reached apparently contradictory conclusions. 2.  The two-level separability decomposition is more nuanced than a binary answer.  Distinguishing aggregate-level separability ( <0.5% direct interaction) from item-conditional interactions (14.2% combined) is a mature analytical move. The \\\"empirical license with caveats\\\" framing -- isolated-factor studies are valid on average but their conclusions are item-conditional -- is the right level of nuance and provides a useful guideline for future work. 3.  D-study reproducibility budgets fill a genuine practical gap.  Translating variance components into concrete recommendations (600 items, 3 prompts, 2 seeds for G >= 0.90 on MMLU; different budgets for other benchmarks) is immediately actionable. The cross-benchmark budget table showing that HellaSwag needs 550 items while MATH needs 1,100 is the kind of task-specific guidance the field lacks. 4.  The engine confound discovery is a standalone methodological contribution.  Identifying that vLLM routes FP32 through a different execution backend (V1 vs V0), inflating precision variance from 0.3% to 7.24% and creating an 8.5pp accuracy gap, is genuinely valuable to any researcher comparing precision modes. The before/after validation is convincing. 5.  The fine-tuning extension adds structural insight.  Demonstrating that the variance hierarchy inverts in fine-tuning (learning rate and seed dominate over items, explaining the \\\"5 seeds, report mean +/- std\\\" convention) is a non-trivial contribution that connects inference and training reproducibility. 6.  Experimental scale is impressive.  7 experiments, 2M+ records, 6 models (7B--14B), 5 benchmarks spanning MC knowledge to multi-step reasoning, plus a fine-tuning scenario. Few empirical papers in this area match the breadth. 3. Weaknesses Major (W1) Incremental novelty over Mesting (2026).  The paper's stated methodological advance over Mesting is the addition of infrastructure facets (hardware, precision) to the G-theory design. But these infrastructure facets contribute negligibly: hardware main effect 1.2% (in Exp 3), precision 0.3%, direct infrastructure x methodology interactions  <0.5%. The paper's strongest findings -- item dominance, the benchmark-dependent variance gradient, D-study budgets, the task-difficulty modulation -- would emerge from a Mesting-style design with fixed infrastructure. The infrastructure extension is effectively a confirmatory null result: infrastructure does not interact with methodology. This is useful information, but it is a confirmation, not a discovery. The paper frames the infrastructure crossing as the primary novelty (\\\"first fully-crossed G-theory study spanning infrastructure and methodology\\\"), yet the results demonstrate that crossing infrastructure was unnecessary for arriving at the main conclusions. The actual novelty lies elsewhere (cross-benchmark gradient, D-study budgets, engine confound), and the paper needs to honestly acknowledge that. (W2) Severely inadequate bibliography.  Seven references is far below the standard for a top-venue submission on evaluation methodology. Critical omissions include: -  Bouthillier et al. (2021, JMLR), \\\"Accounting for Variance in Machine Learning Benchmarks.\\\"  This is the closest ML-native predecessor: it decomposes benchmark variance via ANOVA across hyperparameters, data splits, initialization seeds, and implementation choices. Not citing it inflates the paper's apparent novelty -- the idea of factorial variance decomposition for ML evaluation is not new, and Bouthillier et al. established the template. The paper's claim of being the \\\"first\\\" to decompose variance across multiple factors needs qualification. -  IRT-based item analysis in NLP.  Lalor et al. (2019, NAACL), Rodriguez et al. (2021, ACL), and Vania et al. (2021) have studied item-level properties in NLP benchmarks using Item Response Theory. The paper claims item selection is an overlooked variance source, but IRT researchers have been analyzing item difficulty, discrimination, and selection effects for years. The item dominance finding should be contextualized against this existing body of work. -  Benchmark subsampling literature.  Polo et al. (2024, \\\"tinyBenchmarks\\\"), HELM-Lite, and Perlitz et al. (2023, \\\"Efficient Benchmarking of LLMs\\\") address the same practical question -- how many items suffice for reliable evaluation? -- from a different methodological angle (IRT-based subsampling vs. G-theory D-study). The D-study recommendations should be directly compared against these approaches. -  Henderson et al. (2018), \\\"Deep Reinforcement Learning that Matters.\\\"  A pioneering study on variance sources in ML evaluation (hyperparameters, implementations, environments, seeds). Foundational for the \\\"variance in evaluation\\\" literature that this paper belongs to. -  Shavelson & Webb (1991), \\\"Generalizability Theory: A Primer.\\\"  A canonical G-theory reference. The paper cites only Cronbach et al. (1972) for G-theory foundations, but the Shavelson & Webb primer and the full Brennan (2001) textbook are standard citations in any G-theory paper. The Brennan textbook appears in the task summary but not in the \\\"best\\\" paper's bibliography. -  Lu et al. (2022) and Pezeshkpour & Hruschka (2024) on option ordering effects.  Directly relevant to the ordering facet. The paper includes ordering as a facet but does not cite any prior work on ordering sensitivity. -  Dodge et al. (2020, \\\"Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping.\\\"  Directly relevant to the fine-tuning G-study (Exp 6), which examines seed and data shuffle variance. With only 7 references, the paper creates a misleading impression of operating in a vacuum. Expanding to 25+ references with proper contextualization is essential. (W3) Item dominance is partially expected from measurement theory -- the framing oversells it.  Any assessment instrument with a wide difficulty range will show item variance as the dominant source. This is a well-established property in psychometrics (Brennan, 2001, Chapter 3; Shavelson & Webb, 1991). MMLU spans trivial factual recall to expert-level reasoning; GSM8K spans single-step arithmetic to multi-step word problems. The paper's hook -- \\\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs\\\" -- oversells a finding that is, from a measurement theory perspective, expected. The contribution is in (a) quantifying the magnitude and (b) showing its benchmark-dependence, but the paper should acknowledge: \\\"Item dominance is expected from measurement theory when item difficulty varies widely; our contribution is in quantifying its magnitude (42--58%), demonstrating its systematic variation with task reasoning demands, and deriving D-study implications specific to LLM evaluation.\\\" (W4) The \\\"diagnostic tool\\\" contribution is not substantiated.  Contribution 1 claims G-theory as a \\\"practical diagnostic tool for evaluation pipeline designers\\\" and mentions releasing 172,800+ records. But no software tool, library, or interactive diagnostic is provided. The \\\"tool\\\" is simply running G-theory analysis on evaluation data, which Mesting (2026) and GeneralizIT (2024) already provide. The paper contributes data and analysis, not a tool. Either substantiate the tool claim (e.g., release a pipeline that takes raw evaluation logs and produces variance decompositions + D-study recommendations) or reframe the contribution as \\\"empirical analysis\\\" rather than \\\"diagnostic tool.\\\" Moderate (W5) The fine-tuning extension uses RoBERTa-large (355M, encoder-only, classification), which is architecturally distant from the 7--14B decoder-only autoregressive models in the inference experiments.  The claim that \\\"these findings extend to fine-tuning settings\\\" implies generalization across paradigms, but fine-tuning RoBERTa on SST-2 is a fundamentally different operation than fine-tuning Llama-8B with LoRA on a generation task. The variance hierarchy inversion (LR and seed dominating) may be specific to small encoder-only models on classification tasks with high baseline accuracy. Fine-tuning a decoder model would make the cross-paradigm claim far more credible. At minimum, the paper should explicitly qualify: \\\"Our fine-tuning analysis is limited to encoder-only models on classification tasks and may not generalize to decoder-only fine-tuning.\\\" (W6) The \\\"fully crossed\\\" claim is overstated.  Only MMLU Exp 1 has the richest factorial design (4 models x 3 precisions x 6 prompts x 6 seeds x 3 temperatures x 4 orderings x 200 items). Other benchmarks use reduced designs (Exp 2: 2 precisions, 2 temperatures). The hardware experiment (Exp 3) uses only 2 GPU types with partial crossing (2/4 models on both). The paper's title and abstract claim a \\\"fully-crossed\\\" study, but only one of seven experiments is fully crossed. The other experiments are partially crossed replications with reduced designs, which is fine methodologically but should be honestly described. (W7) Zero figures is a serious presentation weakness for a paper about variance decomposition.  The distilled writing patterns from the field identify stacked-bar variance decomposition charts and D-study projection curves as expected idioms in this literature (Mesting 2026, Brittlebench 2026 both use them). With 11 tables and 0 figures, the paper buries its most visually compelling findings -- the cross-benchmark variance gradient, the D-study cost-effectiveness curves, the before/after engine confound comparison -- in dense tabular format. A stacked-bar chart showing variance components across 5 benchmarks would communicate the benchmark-dependency finding far more effectively than Tables 3--4. D-study projection curves showing G vs. item count for different benchmarks would make the budget recommendations intuitive. This is not cosmetic: at a competitive venue, reviewers have limited time, and visual communication of the key findings would substantially strengthen the paper's impact. (W8) The paper does not adequately address the relationship between its findings and the paper summary title claim.  The paper summary states the central finding is that \\\"variance attribution patterns are benchmark-conditional and model-conditional -- no universal reproducibility recipe exists.\\\" This negative result framing is potentially powerful, but the paper itself leans more toward positive claims (\\\"item selection dominates,\\\" \\\"separability holds,\\\" \\\"here are budgets\\\"). The tension between these two framings is unresolved. If the central message is \\\"no universal recipe,\\\" the paper should lead with how different benchmarks and models require different remediation strategies. If the central message is \\\"item selection dominates,\\\" the paper should explain why this holds despite the benchmark gradient. The current framing tries to claim both simultaneously, which weakens both. Minor (W9)  The inference-fine-tuning correlation of r=0.15 (mentioned in the task summary) is never discussed in the paper text. If this is an actual finding, it reinforces the \\\"no universal recipe\\\" message and deserves discussion. If it was not computed, it should be. (W10)  The paper uses \\\"first\\\" language extensively (\\\"first fully-crossed G-theory study,\\\" \\\"first empirical evidence,\\\" \\\"first formal test of separability\\\"). Priority claims require thorough literature review to sustain, and with only 7 references, these claims are vulnerable. 4. Missing Related Work The following lines of work should be discussed: 5. Questions for Authors 1.  How do your D-study item budget recommendations compare to IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite)? These methods also answer \\\"how many items suffice?\\\" -- what does G-theory add beyond what IRT already provides? 2.  The infrastructure extension is the claimed methodological advance over Mesting (2026), but infrastructure contributes  <1% of variance. If you ran the same study with fixed infrastructure (single GPU, single precision), which of your three contributions would change? Please be specific. 3.  You claim G-theory as a \\\"diagnostic tool\\\" (Contribution 1), but no software or pipeline is released. What exactly is the tool? Is it the G-theory framework itself (which Mesting already applied), the data release, or something else? 4.  Item dominance (42--58%) is expected from psychometric theory when item difficulty varies widely. How do you respond to the concern that this finding is partially tautological? What would it mean for item dominance  not  to hold -- would that indicate a problem with the assessment, the analysis, or the theory? 5.  The fine-tuning experiment uses RoBERTa-large on classification tasks. Would you expect the same inverted variance hierarchy if fine-tuning a 7B decoder model on a generation task (e.g., Llama-8B with LoRA on GSM8K)? What is your basis for generalizing across architectures? 6.  Your literature map includes 10 papers (Bui 2025, \\\"Same Prompt Different Outcomes\\\" 2026, GeneralizIT 2024, etc.), but the paper cites only 7. Why were the other 3 dropped? More critically, why are there no citations to the IRT item analysis literature, the benchmark subsampling literature, or the ML variance decomposition literature (Bouthillier et al., Henderson et al.)? 7.  The paper has zero figures. The distilled writing patterns from your own field analysis identify stacked-bar charts and D-study curves as expected idioms. Was this a deliberate choice? What would a Figure 1 (variance decomposition across benchmarks) add to the narrative? 6. Score Score: 3/6 (Weak Reject) The paper presents a large-scale empirical study with genuine practical value (D-study budgets, engine confound fix, cross-benchmark gradient). However, the novelty claim rests on infrastructure crossing that yields near-null results ( <0.5% variance), the bibliography is severely inadequate (7 references, missing entire lines of relevant work), the item dominance finding is partially expected from measurement theory but oversold, and the \\\"diagnostic tool\\\" contribution is unsubstantiated. The actual novelty -- cross-benchmark variance gradient, task-specific budgets, confound identification -- is real but needs honest reframing and thorough contextualization against related work that currently goes unacknowledged. 7. Confidence Confidence: 4/5 I am familiar with the G-theory literature, the LLM evaluation reproducibility literature, and the IRT/benchmark subsampling work. My main uncertainty is whether the full Bouthillier et al. (2021) framework is sufficiently different in scope that the \\\"first\\\" claims could be partially defended, and whether there are very recent (2026) papers in this space that I have not seen.\\n[05-20 19:43] cli_a974499e77fadbdd: 🌙  [Dream Review Report — median | dream_20260520T190053]  · Overall: borderline reject Dream Review Report Paper:  Benchmark-Dependent Variance Structure in LLM Evaluation: A Generalizability Theory Analysis of Infrastructure and Methodological Reproducibility Review mode:  full |  Reviewers:  R1 (Methods + Experiments), R2 (Novelty + Related Work) 1. Paper Summary This paper applies Generalizability Theory (G-theory) to LLM evaluation, crossing infrastructure facets (hardware type, numerical precision) with methodology facets (prompt template, random seed, sampling temperature, option ordering) and item selection as the measurement facet. Across 6 models (4×8B, 2×14B), 5 benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), and over 1 million evaluation records, the paper reports three findings: (1) item selection is the single largest variance source on MC benchmarks (30–46%) but its dominance is benchmark-dependent, weakening on reasoning tasks; (2) infrastructure and methodology are approximately separable at the aggregate level (direct interaction  <1%); (3) D-study projections yield task-specific reproducibility budgets (380–950 items for G≥0.90). A fine-tuning extension with RoBERTa-large shows the variance hierarchy inverts (LR and seed dominate). Eight experiments are presented across 13 pages with 15 tables and zero figures. 2. Roundtable: Independent Assessments R1 — Methods and Experiments (Score: 4/6, Borderline Reject) Strengths: -  Massive fully-crossed factorial design on MMLU (1,036,800 records) with systematic confound control (enforce_ eager fix reducing the FP32 accuracy gap from 8.5pp to  <1pp) -  Cross-benchmark extension (Exp 2–3) revealing the variance gradient from item-dominated (HellaSwag 45%) to residual/interaction-dominated (MATH 30% residual) is methodologically sound -  D-study projections with bootstrap CIs ([ 420, 680 ] for MMLU) provide genuine uncertainty quantification on a policy-relevant number -  Fine-tuning extension adds conceptual value by demonstrating the inverted variance hierarchy -  Statistical toolkit is appropriate: REML, bootstrap, Kruskal-Wallis, permutation tests Major weaknesses: 1.  Model pooled rather than treated as a crossed random facet.  In G-theory, model (the object of measurement) should be treated as a facet. By pooling, model×item interactions get absorbed into the item_ id component, inflating the headline 43% figure. The Gemma-2 sensitivity analysis (removing it raises pooled item_ id to 46%) hints at this, but a proper model-as-facet analysis would separate model×item interaction and likely reduce item_ id's share. This is a fundamental design choice that weakens the central claim. 2.  Bootstrap CIs reported only for item_id in Table 1 ([38%, 48%]).  All other variance components in all tables lack uncertainty intervals. For a paper whose core claim rests on the relative magnitude of variance components, this is a serious gap — particularly for the separability claim (is 0.3% direct Infra×Method significantly different from 0?). 3.  Arbitrary separability threshold.  The 1% threshold for \\\"approximate separability\\\" is not derived from G-theory or psychometric literature. The observed value (0.3–0.5%) lands comfortably below this threshold, but no sensitivity analysis examines what changes at 0.25% or 2%. A bootstrap CI on total direct interaction would be more informative than a pass/fail test. 4.  D-study extrapolation beyond item universe.  MATH has 500 total items; the D-study recommends 950 items for G≥0.90. The paper notes this makes reliable evaluation \\\"effectively unattainable,\\\" which is fair, but the D-study formula assumes sampling from an infinite item universe. When the recommendation exceeds the actual item pool, the projection's validity breaks down — this limitation is acknowledged but under-discussed. Moderate weaknesses: -  Only 2 GPU types with partial crossing (2/4 models fully crossed on hardware); 1 df for hardware main effect makes the separability test directional at best -  Temperature levels differ across experiments (3 levels in Exp 1, 2 in Exp 2) without clear justification -  All 3-way and higher interactions absorbed into residual (14.2–21% depending on experiment) without discussion of which higher-order terms might be substantively meaningful -  Binary accuracy metric on MC tasks inflates item variance (items near 0 or 1 contribute little variation); log-likelihood or calibration-based metrics could yield different decompositions -  Fine-tuning experiment uses only 2 precisions and 3 GPUs but claims to test separability generalization — this is a weaker test than the inference experiments R2 — Novelty and Related Work (Score: 3/6, Weak Reject) Strengths: -  The benchmark-dependent variance gradient (item_ id declining from 45% on HellaSwag to 22% on MATH, with temperature×item and seed×item rising correspondingly) is a genuine quantitative contribution — it quantifies an intuition the field has had but never measured systematically -  The two-level separability decomposition (aggregate  <1% vs. item-conditional 14–18%) is more informative than a binary answer and the \\\"empirical license with caveats\\\" framing is mature -  D-study budgets with cross-benchmark variation (380 items for HellaSwag vs. 950 for MATH) are immediately actionable for practitioners -  The engine confound discovery (enforce_ eager fix) is a standalone methodological contribution -  The fine-tuning contrast (LR+seed dominate, explaining the \\\"5 seeds\\\" convention) adds structural insight Major weaknesses: 1.  Incremental novelty over Mesting (2026).  The core methodological contribution is extending Mesting's G-theory framework by adding infrastructure facets. But these infrastructure facets contribute negligibly (hardware 1.2%, precision 0.8%, direct Infra×Method 0.3–0.5%). The paper's most impactful findings — item dominance, benchmark-dependent variance gradient, D-study budgets — would emerge from a Mesting-style design with fixed infrastructure. The \\\"first fully-crossed\\\" claim is technically true but the marginal value of crossing infrastructure with methodology is a confirmatory null result, not a breakthrough. The paper needs to reframe: the infrastructure extension is valuable as a confirmatory finding; the actual novelty is in the cross-benchmark gradient, D-study budgets, and confound fix. 2.  Severely deficient bibliography.  Only 9 references for a 13-page top-venue submission. Critical omissions include:   -  Bouthillier et al. (2021, JMLR), \\\"Accounting for Variance in Machine Learning Benchmarks\\\"  — the closest ML-native predecessor, decomposing variance via ANOVA across hyperparameters, data splits, and seeds. Not citing it inflates the paper's apparent novelty.   -  IRT-based item analysis in NLP:  Lalor et al. (2019, NAACL), Rodriguez et al. (2021, ACL), Vania et al. (2021) — directly relevant to the item dominance finding. The paper claims item selection is under-studied, but IRT has been analyzing item-level properties for years.   -  Benchmark subsampling literature:  Polo et al. (2024, \\\"tinyBenchmarks\\\"), HELM-Lite, Perlitz et al. (2023) address the same practical question (how many items suffice?) from different angles. The D-study budgets should be contextualized against these.   -  Henderson et al. (2018), \\\"Deep Reinforcement Learning that Matters\\\"  — pioneering work on variance in ML evaluation.   -  Shavelson & Webb (1991)  and full Brennan (2001) textbook — canonical G-theory references that a G-theory paper must cite.   -  Lu et al. (2022)  — ordering effects in MC evaluation, relevant to the ordering facet. 3.  Item dominance is partially tautological.  Any assessment instrument with a wide difficulty range will show item variance as the dominant source — this is a well-known property in psychometrics (Brennan, 2001, Ch. 3). The paper's framing (\\\"researchers are optimizing the wrong knobs\\\") oversells a finding that is expected from measurement theory. The contribution is in quantifying the magnitude and its benchmark-dependence, but the paper should acknowledge: \\\"Item dominance is expected from measurement theory; what we contribute is its precise magnitude, systematic variation with task reasoning demands, and D-study implications.\\\" Moderate weaknesses: -  Fine-tuning extension uses RoBERTa-large (355M, encoder-only, classification) — architecturally distant from the 7–14B decoder-only models in inference experiments. Fine-tuning a decoder model (e.g., Llama-8B with LoRA on a generation task) would make cross-paradigm generalization claims far more credible. -  The \\\"fully crossed\\\" claim is overstated: only MMLU Exp 1 has the richest factorial design. Other benchmarks use reduced designs (2 precisions, 2 temperatures). Hardware crossing is partial (2/4 models). Cross-benchmark separability claims rest on narrower evidence than the framing suggests. -  No figures at all — highly unusual for a top venue paper. D-study projection curves, stacked-bar variance decompositions, and the benchmark gradient would dramatically improve communication. The paper's 15 tables contain rich data that is hard to absorb in tabular form. 3. Roundtable: Cross-Sharing and Convergence Areas of Agreement (both reviewers) 1.  Model-as-facet treatment is the most fundamental methodological concern.  R1 identified it as a G-theory design flaw; R2 flagged it as inflating the headline item_ id number. Both agree that a proper model-as-facet analysis would likely reduce item_ id below 43% and reveal model×item interaction as a substantial component. This directly affects Claim 1. 2.  The separability threshold is arbitrary and the test under-powered.  Both reviewers independently flagged the 1% threshold as unjustified and the hardware crossing as insufficient (2 GPU types, partial). The separability claim is directional evidence, not proof. 3.  D-study budgets are the most actionable contribution.  Both reviewers rate the concrete, benchmark-specific reproducibility budgets as filling a genuine practical gap. The bootstrap CIs on MMLU items ([ 420, 680 ]) demonstrate honest uncertainty quantification (though CIs are needed for other benchmarks too). 4.  The cross-benchmark variance gradient is a genuine empirical contribution.  Both agree the systematic relationship between task reasoning demands and variance structure (item dominance weakening, temperature/seed interactions strengthening) is informative and well-supported by data across 5 benchmarks. 5.  The bibliography is far below top-venue standards.  R2 provided detailed missing references; R1 implicitly relied on broader knowledge that confirms these gaps. Areas of Divergence -  Severity of novelty concern:  R2 weights the incremental novelty over Mesting more heavily (infrastructure extension is a near-null result) → 3/6. R1 is more willing to credit the experimental scale and scope → 4/6. -  Statistical vs. conceptual critique:  R1 focuses on the technical execution (CI coverage, REML specification, residual interpretation). R2 focuses on positioning and framing (overselling item dominance, missing related work, tautological aspects). -  Fine-tuning extension value:  R1 accepts it as an interesting conceptual addition. R2 considers the architectural mismatch (RoBERTa vs. decoder-only) a moderate weakness that undermines cross-paradigm claims. Convergence After cross-sharing, both reviewers converge on: the paper presents a substantial empirical effort with real practical value, but the current version has (a) a fundamental G-theory design issue (model treatment), (b) severely inadequate related work, (c) framing that oversells the infrastructure contribution and item dominance finding, and (d) missing uncertainty quantification across most results. These issues are addressable without new experiments but require significant revision. 4. Consolidated Assessment Overall Score: 4/6 (Borderline Reject) Confidence: High Recommendation: Borderline Reject Verdict Summary The paper tackles an important problem — understanding and quantifying variance sources in LLM evaluation — with impressive experimental scale (1M+ records, 8 experiments, 5 benchmarks, 6 models). The cross-benchmark variance gradient and task-specific D-study budgets are genuine contributions that would be useful to the community. The engine confound discovery (enforce_ eager fix) is a practical contribution in its own right. However, the paper falls short of the acceptance threshold for three main reasons: 1.  Methodological concern:  Model is pooled rather than treated as a G-theory facet, inflating the central item_ id claim. For a paper whose entire framework is G-theory, this is a fundamental design choice that needs addressing. 2.  Novelty and positioning:  The infrastructure extension — the claimed methodological advance over Mesting (2026) — yields near-null results ( <1% variance). The paper's actual novelty (cross-benchmark gradient, D-study budgets, confound fix) does not depend on the infrastructure extension and needs honest reframing. The bibliography (9 references) is far below top-venue standards with critical omissions (Bouthillier et al., IRT literature, benchmark subsampling work). 3.  Presentation:  15 tables, 0 figures. Key uncertainty quantification (CIs) is reported for only one component in one table. The separability threshold is arbitrary. These are fixable but collectively reduce confidence in the claims. Actionable Revisions (no new experiments needed) 1.  Re-analyze with model as a crossed facet  — report model×item interaction separately; adjust item_ id shares and D-study projections accordingly. 2.  Add CIs to all variance component tables  — especially for the direct Infra×Method interaction term. 3.  Expand bibliography to ≥25 references  — must include Bouthillier et al. (2021), IRT item analysis papers, tinyBenchmarks/HELM-Lite, Henderson et al. (2018), Shavelson & Webb (1991). 4.  Add 3–4 figures  — D-study curves, stacked-bar variance decomposition across benchmarks, benchmark gradient visualization. 5.  Reframe contributions honestly  — infrastructure separability as confirmatory null; item dominance as expected from measurement theory but newly quantified; cross-benchmark gradient as the primary novel finding. 6.  Derive or justify the separability threshold  — or replace with bootstrap CI on total direct interaction. 7.  Acknowledge item dominance tautology  — wide difficulty range → large item variance is psychometrically expected; the contribution is in quantifying its magnitude and benchmark-dependence. Strengths Worth Preserving -  The experimental scale and systematic confound control are genuinely impressive -  The cross-benchmark variance gradient (MMLU→ARC→GSM8K→MATH) is a clean, well-supported finding -  D-study budgets (380–950 items, 3–5× items-over-prompts ratio) fill a real practical gap -  The fine-tuning contrast (inverted hierarchy) explains divergent reproducibility conventions -  The conditional separability insight (aggregate-level separability vs. item-level interactions) is nuanced and useful 5. Scores Overall: 4/6 — Borderline Reject.  Substantial empirical work with genuine practical value, but fundamental G-theory design issue, insufficient positioning against related work, and presentation gaps place it below the acceptance threshold. Addressable with revision; no new experiments required.\\n[05-20 19:41] cli_a974499e77fadbdd: 🌙  [Dream Review Report — best | dream_20260520T190053]  · Overall: borderline accept Reviewer R1: Methodology and Experimental Rigor Summary This paper applies Generalizability Theory (G-theory) to decompose variance in LLM evaluation across infrastructure (hardware, precision), methodology (prompt, seed, temperature, ordering), and measurement (item) facets. Across 6 models, 5 benchmarks, and 2M+ evaluation records, the authors find that item selection dominates variance (42--58%), direct infrastructure x methodology interactions are negligible (<0.5%), and current evaluation practices yield unacceptably low generalizability coefficients (G  < 0.40). D-study projections provide actionable reproducibility budgets showing item count increases are far more cost-effective than prompt or seed replication. The paper is ambitious in scope and the cross-domain transfer of G-theory to LLM evaluation is well-motivated, but several methodological concerns---particularly around the treatment of \\\"model\\\" in the G-theory framework, the interpretation of item variance, and incomplete uncertainty quantification---temper my enthusiasm. Strengths -  Timely and well-motivated problem.  The paper addresses a genuine gap: no prior work crosses infrastructure and methodology layers in a single G-theory framework. The positioning relative to Mesting (2026), Yuan et al. (2025), and Brittlebench (2026) is accurate and clearly articulated. -  Impressive experimental scale.  8 experiments, 2M+ records, 6 models, 5 benchmarks, and extension to fine-tuning. The breadth of coverage strengthens the generality claims substantially. All 8 planned experiments are present. -  Engine confound identification is a genuine methodological contribution.  The discovery that vLLM routes FP32 through a different compute path than BF16/FP16, inflating precision variance from 0.87% to 7.24% (interaction), is a valuable finding of independent interest. The before/after comparison is convincing. -  Actionable D-study budgets.  The reproducibility budget tables translate abstract variance component estimates into concrete design recommendations. The cross-benchmark budget table (Table 8 / Table 13-15 in the summary) showing task-specific item requirements is practically useful. -  Good confound control.  Uniform vLLM V0 + enforce_ eager across all precision modes, generation-based evaluation following Hua et al. (2025) to avoid log-likelihood artifacts, and stratified item sampling all reflect careful experimental design. -  Fine-tuning extension adds generality.  Showing that item dominance holds in fine-tuning (36.8--44.5%) with seed/LR replacing prompt/temperature as secondary factors is a non-trivial extension. -  Clear task-difficulty gradient.  The systematic pattern across 5 benchmarks (item_ id share decreasing, residual and temp x item increasing with difficulty) is a well-supported finding that provides theoretical insight. Weaknesses Major -  (W1) Model is pooled rather than treated as a facet---this fundamentally distorts the variance decomposition.  The paper pools 4 models and decomposes variance across the pooled data, but \\\"model\\\" is not included as a facet in the G-study. In standard G-theory, the object of measurement (here, presumably each model's ability) should be the differentiation facet. By pooling across models without including model as a facet, model-level variance is absorbed into item_ id (since different models have different difficulty profiles on the same items) and into the residual. This means the 58.4% attributed to item_ id is confounded with model x item interaction---the very thing G-theory is designed to separate. The per-model analyses (Table 2) partially address this, but the headline numbers and the D-study projections are based on the pooled analysis. This is a fundamental design choice that needs explicit justification. If the goal is to assess reliability of a  single model's  evaluation, the per-model G-studies should be primary. If the goal is reliability of  cross-model comparisons , model must be a facet. The paper's framing suggests both goals but delivers neither cleanly. -  (W2) The 0.5% separability threshold is arbitrary and self-serving.  The paper defines separability as \\\"direct infrastructure x methodology interactions contribute less than 0.5% of total variance\\\" and then finds exactly 0.5%. This threshold is not derived from any principled criterion (e.g., effect size conventions, practical significance for model ranking, or comparison to measurement error). A threshold chosen post hoc to match the observed result raises concerns. The paper should either: (a) derive the threshold from practical consequences (e.g., what interaction magnitude would change a model ranking?), (b) report the result without a binary threshold and let readers judge, or (c) use a formal hypothesis test with appropriate power analysis. -  (W3) Bootstrap CIs are reported only for the MMLU item_id component in most tables.  The paper summary mentions \\\"Bootstrap CIs (1000 resamples)\\\" as a general methodology, but Table 1 in the paper shows CIs for all components only on MMLU. Cross-benchmark (Table 3/4), hardware (Table 5), 14B (Table 9), and fine-tuning (Table 10) tables report point estimates without CIs. For claims about variance component magnitudes being \\\"negligible\\\" or \\\"substantial,\\\" CIs are essential---a 0.5% point estimate with a CI of [ 0.0%, 3.0%] tells a very different story than [ 0.4%, 0.6% ]. This is especially critical for the separability claim where the threshold is tight. -  (W4) ANOVA-based estimation (Henderson Method I) is used in the code, but the paper claims REML.  The variance_ decomposition.py code implements classical ANOVA-based variance component estimation (Type-I SS with EMS equations), not REML. REML would use a mixed-effects model fitted via maximum likelihood with restricted estimation. These methods can give different results, especially when designs are slightly unbalanced or when negative variance components arise. The code truncates negative estimates to zero, which is the ANOVA convention; REML handles this differently (constrained optimization). The paper should either: (a) actually implement REML (e.g., using lme4/statsmodels), or (b) correctly describe the method as ANOVA-based Henderson Method I estimation. Claiming REML when using ANOVA-based methods is a methodological misrepresentation. Moderate -  (W5) Only 2 GPU types for the hardware facet, with partial crossing.  The hardware experiment (Exp 3) uses only 2 GPU types with partial crossing (only 2 of 4 models run on both). With n=2 levels, the hardware main effect has 1 degree of freedom---insufficient for stable variance component estimation. The claim that \\\"hardware-related variance totals 4.1%\\\" has very wide implicit uncertainty. The partial crossing also means the hardware x model interaction is confounded with the hardware main effect for the 2 models not run on both GPUs. This limitation is not adequately discussed. -  (W6) Item dominance may be a statistical artifact of the binary response variable.  With a binary correct/incorrect response, items with extreme p-values (very easy or very hard) contribute disproportionately to total variance. The paper's own Decision D002 acknowledges that text_ exact_ match produces a radically different variance structure (prompt x item at 37.5% vs item_ id at 58.4% for binary). Yet the paper presents only the binary metric results. If the core claim is \\\"item selection dominates variance,\\\" this claim is metric-dependent, and the paper should present both metrics or at minimum discuss the metric sensitivity. The dual-metric analysis planned in D002 appears to have been dropped from the paper. -  (W7) Temperature levels differ across experiments without justification.  Exp 1 uses {0.1, 0.5, 1.0}, the paper summary mentions {0.0, 0.3, 0.7}, the experiment plan mentions {0.1, 0.5, 1.0} for some and 2 temperatures for others. Exp 2 uses 2 temperatures while Exp 1 uses 3. These inconsistencies make cross-experiment comparisons unreliable and suggest the \\\"fully crossed\\\" characterization is only approximate. The design is not truly balanced across experiments. -  (W8) D-study projections assume independence of item samples.  The D-study formula G = sigma_ tau / (sigma_ tau + sigma_ delta) assumes that additional items are independently sampled from the same universe. But benchmark items are not a random sample from a well-defined universe---they are curated collections. Extrapolating from 200 stratified-sampled items to 600 or 1100 items assumes the variance structure holds for items not in the sample. For MATH (500 total items), the recommendation of 1100 items is infeasible and reveals the limitation of treating benchmark items as a random sample from an infinite universe. -  (W9) The paper omits higher-order interactions.  The code explicitly states \\\"Higher-order interactions (>=3-way) are absorbed into the residual.\\\" With 6 facets, there are 20 three-way interactions, 15 four-way, etc. The residual of 16.8% likely contains substantial structured variance. If precision x temperature x item is large (plausible given both two-way interactions are non-trivial), the attributed shares for the two-way components would be biased. The paper should at minimum discuss this limitation or fit selected three-way interactions. Minor -  (W10) The Kruskal-Wallis test (H=47.3, p<0.001) cited for cross-benchmark differences is underspecified.  What is the test comparing? Variance component estimates across benchmarks? With only 5 benchmarks and point estimates, the degrees of freedom and interpretation are unclear. -  (W11) No correction for multiple comparisons.  Multiple permutation tests and bootstrap CIs are computed without any family-wise error rate correction (e.g., Bonferroni, Holm). -  (W12) The \\\"10x more cost-effective\\\" headline claim conflates marginal and average returns.  The 10.2:1 ratio compares marginal G gains per unit cost, but the cost metric treats one additional item the same as one additional prompt. In practice, additional prompts require human design effort while additional items can be sampled automatically. The cost comparison should distinguish compute cost from human annotation cost. Questions for Authors 1.  Why is \\\"model\\\" not a facet in the G-study? If models are pooled, how much of the 58.4% item_ id variance is actually model x item interaction? Can you provide the per-model G-study results as the primary analysis? 2.  The code uses ANOVA-based Henderson Method I estimation, but the paper claims REML. Which method was actually used for the reported results? If ANOVA-based, have you verified that the balanced-design assumption holds exactly (i.e., every cell has exactly the same number of observations)? 3.  What happens to the variance decomposition when you use text_ exact_ match instead of binary correct? Decision D002 in your project files describes this as producing a radically different structure. Why was this analysis excluded from the paper? 4.  The separability threshold of 0.5% appears to match the observed result exactly. Was this threshold set before or after seeing the data? What would the conclusion be at a 1% threshold? At 0.1%? 5.  For the MATH D-study recommendation of 1100 items: MATH has only 500 items total. How should practitioners interpret a recommendation that exceeds the benchmark size? Does this invalidate the D-study framework for small benchmarks? 6.  Can you provide bootstrap CIs for the separability claim (total direct infra x method interaction)? The 0.5% point estimate needs uncertainty quantification to be interpretable. 7.  How sensitive are the variance component estimates to the exclusion of three-way interactions? Have you tested a model with, e.g., precision x temperature x item included? 8.  The paper mentions temperature {0.0, 0.3, 0.7} in the summary but {0.1, 0.5, 1.0} in the tex file. Which values were actually used, and does including T=0.0 (deterministic) vs T=0.1 (near-deterministic) materially change the temperature variance component? Score and Recommendation Score: 4 (Borderline Reject) Confidence: High Recommendation: Borderline Reject The paper tackles an important problem with impressive experimental scale and provides useful practical contributions (engine confound identification, D-study budgets). However, the methodological concerns are substantive: (1) the treatment of model as pooled rather than as a G-theory facet fundamentally confounds the headline variance decomposition; (2) the mismatch between claimed (REML) and implemented (ANOVA) estimation methods undermines methodological credibility; (3) incomplete uncertainty quantification (CIs missing from most tables, especially the separability claim); and (4) the single-metric presentation omits a known sensitivity that changes the core finding. These are not cosmetic issues---they affect the validity of the three central claims. If the authors can address W1 (model as facet), W4 (REML vs ANOVA), W3 (CIs throughout), and W6 (dual metric), the paper would be substantially strengthened and could merit acceptance. In its current form, the ambitious scope is undermined by methodological gaps that a psychometrics-savvy reviewer would flag immediately.\\n[05-20 19:37] cli_a974499e77fadbdd: 🌙  [Dream Review Report — best | dream_20260520T190053]  · Overall: borderline Dream Review Report Paper:  Reproducibility Budgets for LLM Evaluation: Testing the Separability Assumption Between Infrastructure and Methodological Variance Sources via Generalizability Theory Review Mode:  Full (2 Reviewers + Roundtable)\\n Review Standard:  Top ML venue, ~ 25% acceptance rate, 6-point scale Reviewer Scores Paper Summary The paper conducts a fully-crossed Generalizability Theory (G-theory) study unifying infrastructure (hardware, precision) × methodology (prompt, seed, temperature, ordering) × measurement (test items) factors in LLM evaluation. Across 6 models (7–14B), 5 benchmarks, and 2M+ records, the authors report: (1) item selection dominates variance (42–58%), (2) infrastructure–methodology separability holds at aggregate (<0.5%) but is item-conditional (14.2%), and (3) current practices yield G  < 0.40 while D-study budgets show items are 10× more cost-effective than prompts for reliability. A fine-tuning extension with RoBERTa-large shows item dominance generalizes to training. Consolidated Strengths S1. Ambitious experimental scale and systematic design. \\n Seven experiments totaling 2M+ evaluation records, building from single-benchmark to cross-benchmark, cross-model, cross-hardware, and cross-paradigm coverage. All 8 planned experiments are reflected in the paper. This is a serious empirical effort. S2. Engine confound discovery is a genuine methodological contribution. \\n The finding that vLLM routes FP32 through a different compute path (non-V0 engine), inflating precision variance from 0.3% to 0.87% (main) and from 1.8% to 7.24% (interaction) with an 8.5pp accuracy gap, is independently valuable. It serves as a concrete cautionary tale for any study comparing precision modes and demonstrates how infrastructure configuration can systematically bias variance attribution. S3. Nuanced two-level separability result. \\n Rather than a simple binary answer, the separability test yields complementary findings: aggregate separability holds ( <0.5% direct interactions), licensing isolated-factor studies, while item-conditional interactions (14.2%) warn that such conclusions are contingent on item selection. This is more informative than either finding alone. S4. D-study budgets are actionable. \\n The budget tables (Table 7, Table 8) provide concrete, immediately usable guidance: 600 items + 3 prompts + 2 seeds → G ≥ 0.90 for MMLU. The 10:1 marginal effectiveness ratio (items vs. prompts) is a memorable, practical takeaway. Cross-benchmark budget differences (550–1100 items) provide task-specific guidance. S5. Cross-benchmark difficulty gradient. \\n The systematic relationship between task difficulty and variance structure (item_ id decreases 58.4% → 42.1%, residual increases 16.8% → 24.8%, temp×item increases 5.8% → 10.4% as accuracy drops) quantifies why reasoning benchmarks are less reproducible. This is a genuinely useful empirical finding. Consolidated Weaknesses W1. Incremental over Mesting et al. (2026) — the core methodological contribution is an extension, not a new framework.  [ Both reviewers, R2 primary ]\\n Mesting et al. (2026) already applied G-theory to LLM evaluation with item, prompt, judge, and temperature facets, finding judge dominance at 43.8%. This paper extends that framework by adding infrastructure facets (hardware, precision). However, these infrastructure facets turn out to contribute negligibly: hardware main effect 0.6%, precision main effect 0.3%. The extension is real but modest in substance — the paper's most important finding (item dominance) could plausibly have emerged from a Mesting-style design without the infrastructure layer. The \\\"first fully-crossed\\\" framing oversells what is fundamentally an incremental extension. W2. \\\"Fully crossed\\\" design is overstated.  [ R1 primary ]\\n The paper claims a fully-crossed design but the factorial structure is unbalanced: -  MMLU has the richest design (3 precisions, 3 temperatures, 4 orderings, 2 GPUs) -  Other benchmarks use reduced designs (2 precisions, 2 temperatures) -  Hardware crossing is only on MMLU (Exp. 3) -  14B extension uses a reduced facet set -  Fine-tuning uses a completely different model/task family\\n Claims about cross-benchmark separability and scale invariance rest on narrower evidence than the \\\"fully crossed\\\" framing implies. The paper should clearly delineate which claims are supported by full crossing and which by partial designs. W3. Pooled-model analysis likely inflates item_id variance.  [ R1 primary ]\\n The primary analysis pools 4 models, treating them as exchangeable observations. But model × item interactions (some items are harder for Mistral than Qwen3) get absorbed into the item_ id component, inflating its apparent dominance. The per-model analysis (Table 2) partially addresses this (item_ id range 54.7–62.0%), but should be the primary presentation. The pooled analysis overstates the universality of the 58.4% figure. W4. Item dominance is partially predictable from first principles.  [ R2 primary ]\\n Any assessment with a steep difficulty gradient (items ranging from trivial to expert) will show item difficulty as the dominant variance source. The paper's own Discussion explains exactly why this must be so. While quantifying the magnitude is useful, framing it as surprising (\\\"researchers are optimizing the wrong knobs\\\") oversells the finding. A more measured framing — \\\"item dominance is expected but its magnitude (>50%) and the relative inefficiency of other interventions have not been quantified\\\" — would be more appropriate. W5. Separability threshold (0.5%) is arbitrary and the result is borderline.  [ R1 primary, R2 concurs ]\\n The 0.5% threshold for \\\"separability\\\" is not justified from G-theory, psychometrics, or any principled argument. The observed value (0.5%) lands exactly on the threshold boundary, making the binary \\\"separability holds\\\" conclusion fragile. A bootstrap confidence interval on the total direct interaction variance would be more informative. The result should be presented as a continuous measure with uncertainty rather than a pass/fail test. W6. D-study projections lack uncertainty quantification.  [ R1 primary ]\\n The budget recommendations (e.g., \\\"600 items + 3 prompts + 2 seeds → G ≥ 0.90\\\") are point estimates derived from estimated variance components. No confidence intervals or sensitivity analysis is provided for the projected G values. Given that the input variance components have SEs of 0.1–2.1%, the projected G values could shift meaningfully. The paper should propagate estimation uncertainty through the D-study projections (e.g., via bootstrap). W7. Very sparse reference list (only 7 references).  [ R2 primary, R1 concurs ]\\n For a top ML venue, 7 references is far below expectations. Critical omissions include: -  Classical G-theory: Brennan (2001) \\\"Generalizability Theory,\\\" Shavelson & Webb (1991) — foundational references for G-theory methodology -  ML variance decomposition: Bouthillier et al. (2021) \\\"Accounting for Variance in Machine Learning Benchmarks\\\" — the closest ML-native predecessor, not cited -  IRT in NLP: Lalor et al. (2019), Rodriguez et al. (2021), Vania et al. (2021) — item-level analysis frameworks directly relevant to the item dominance finding -  Ordering effects: Lu et al. (2022) — relevant to the ordering facet -  ML reproducibility: Henderson et al. (2018), Pineau et al. (2021) — broader context\\n This is not a minor issue: the missing references include direct methodological predecessors and would substantially change the novelty positioning. W8. Fine-tuning generalization is weak.  [ Both reviewers ]\\n The claim that \\\"findings extend to fine-tuning settings\\\" is based solely on RoBERTa-large (355M, encoder-only) on 4 NLU classification tasks. This is a large architectural and paradigm gap from the 7–14B decoder models used in inference experiments. Fine-tuning a 7B+ decoder model with LoRA/QLoRA on a generation task would be far more convincing as a generalization argument. As presented, this is a separate (interesting) finding rather than evidence of generalization. Questions for Authors Q1.  How would the variance decomposition change if model were treated as a random facet rather than pooling? Specifically, would model × item interactions reduce the item_ id share substantially? Q2.  Can you provide a direct numerical comparison with Mesting et al. (2026) on overlapping facets (item, prompt, temperature)? This would clarify the incremental contribution. Q3.  Would item dominance survive adding judge/scorer as a facet? Mesting found judge at 43.8% — this could substantially alter the variance hierarchy. The paper uses fixed generation-based scoring, which removes this source but also limits comparability. Q4.  Can you provide bootstrap confidence intervals for the D-study G projections? The headline recommendation (600/3/2 → G = 0.90) would be more credible with uncertainty bounds. Q5.  What is the justification for the 0.5% separability threshold? Would results change with 1% or 0.25%? Q6.  The MATH entry in Table 8 shows 1,100 items with \\\"66× cost factor\\\" but 1100 × 3 prompts × 2 seeds = 6,600 evaluations, not 13,200. Is this a typo, or does MATH require more prompts/seeds? Q7.  How were the 6 prompt templates selected? Were they designed to maximize diversity, or sampled from existing evaluation suites? The prompt × item interaction (6.1%) depends critically on prompt diversity. Minor Issues M1.  Table 3 column headers are misaligned in the PDF — \\\"item_ id %\\\" appears to span the wrong column. M2.  The ThinkingMachines (2025) reference has placeholder arXiv ID \\\"2501.xxxxx\\\" — needs the real ID. M3.  The abstract says \\\"6 models\\\" but the paper primarily analyzes 4 models with 2 as extension. Should be clearer about primary vs. extension. M4.  The paper claims \\\"over 2 million evaluation records\\\" — the sum of stated record counts (1,036,800 + 3×230,400 + 691,200 + 2×172,800 + 1,728 + 230,400 + 172,800) ≈ 3.17M. The \\\"over 2 million\\\" is an undercount of the actual total. Clarify. M5.  \\\"LayerCast\\\" is not a standard term — should be cited or defined more precisely. M6.  The D-study discussion mentions G ≥ 0.80 as the psychometric minimum but doesn't cite the source for this threshold (Nunnally & Bernstein 1994 or similar). Experiment Coverage Assessment All 8 planned experiments from the design document are reflected in the paper: -  ✅ exp-001: Full-scale precision study (MMLU) -  ✅ exp-002: Multi-benchmark replication (GSM8K, ARC, HellaSwag) -  ✅ exp-003: Multi-hardware G-study -  ✅ exp-004: D-study projections -  ✅ exp-005: 14B model extension -  ✅ exp-006: Fine-tuning G-study -  ✅ exp-007: LayerCast precision study -  ✅ exp-008: MATH benchmark extension Coverage is complete. However, several figures described in the experiment plan (stacked-bar decompositions, heatmaps, scatter plots, D-study projection curves, iso-G contour plots) are absent from the paper. The paper is table-heavy with no figures, which significantly weakens communication of key results — particularly the D-study projection curves (planned Fig 8–10) and the variance decomposition comparisons (planned Fig 1, 4, 15) which would be far more effective visually than as tables. Recommendation Consensus Score: 3.5/6 (Borderline — between Weak Reject and Weak Accept) For acceptance, the paper would need: 1.  Reframe novelty claims to acknowledge extension-of-Mesting positioning honestly 2.  Add per-model analysis as primary, pooled as secondary 3.  Add uncertainty quantification to D-study projections 4.  Substantially expand the reference list (add ≥15 missing key references) 5.  Justify or remove the 0.5% separability threshold 6.  Add figures — at minimum D-study projection curves and variance decomposition stacked bars The paper's core strengths  — the engine confound discovery, the nuanced separability result, the cross-benchmark difficulty gradient, and the actionable D-study budgets — represent genuine value. But the incremental positioning over Mesting et al., inflated novelty claims, methodological concerns (pooled analysis, arbitrary threshold, no uncertainty propagation), and severely sparse references pull it below the acceptance threshold in its current form. If revised to address the top 4 weaknesses , this could become a solid Weak Accept (4/6). The empirical effort is substantial and the practical recommendations fill a real need. The revisions are achievable without new experiments.\\n[05-20 19:34] cli_a974499e77fadbdd: 🌙  [Dream Review Report — best | dream_20260520T190053]  · Overall: Weak Reject (3/6) R2 Review: Novelty and Related Work Summary This paper applies Generalizability Theory (G-theory) to LLM evaluation, crossing infrastructure factors (hardware, precision) with methodology factors (prompt, seed, temperature, ordering) and item selection in a single factorial design. The main findings are that item selection dominates variance (42-58%), infrastructure and methodology are separable at the aggregate level but interact through item difficulty, and D-study projections show current practices are severely underpowered (G  < 0.40). The work directly extends Mesting et al. (2026), who applied G-theory to methodological facets only, by adding infrastructure facets and testing separability. While the experimental scale is impressive (2M+ records, 5 benchmarks, 6 models), the novelty is incremental over Mesting, the item dominance finding is largely predictable from psychometric first principles, and the related work has significant gaps. Strengths S1.  Well-motivated separability test with nuanced outcome.  The distinction between aggregate separability ( <0.5% direct interactions) and item-conditional non-separability (14.2% combined) is genuinely useful. This is the paper's strongest conceptual contribution — it provides a principled answer to whether isolated-factor studies are valid, with appropriate caveats. The two-level framing (aggregate license + item-conditional warning) is more informative than a binary separability verdict. S2.  Scale and breadth of the experimental design.  Crossing 7 facets across 6 models, 5 benchmarks, and 2M+ records is a substantial empirical effort. The cross-benchmark gradient (item dominance decreasing with task difficulty, from 58.4% on MMLU to 42.1% on MATH) is a non-obvious finding that adds genuine insight about why reasoning benchmarks produce less reproducible results. S3.  Engine confound discovery.  The identification that vLLM routes FP32 through a different compute path than BF16/FP16, inflating precision variance from 0.3% to 0.87% (and precision x item from 1.8% to 7.24%), is a concrete methodological contribution of independent value. This is actionable for anyone doing precision comparisons and illustrates how infrastructure confounds can systematically bias variance attribution. S4.  D-study budgets are actionable.  The 10:1 marginal effectiveness ratio (items vs. prompts) and specific budget recommendations (600 items + 3 prompts + 2 seeds for G >= 0.90) translate directly into evaluation design guidance. The cross-benchmark budget table (550-1100 items depending on task) adds practical value. S5.  Fine-tuning extension broadens scope.  Showing that item dominance persists in fine-tuning (37-45%) while the secondary variance hierarchy shifts (seed/LR replace prompt/temperature) demonstrates the framework's generality beyond inference evaluation. Weaknesses W1.  Incremental novelty over Mesting et al. (2026).  The paper's core methodological contribution — applying G-theory to LLM evaluation — is Mesting's. What this paper adds is (a) infrastructure facets and (b) the separability test. But infrastructure turns out to be nearly negligible: precision contributes 0.3% main effect and hardware 0.6%. The separability test yields a largely expected null result at the aggregate level (it would be surprising if GPU type x prompt template interacted strongly). The item-conditional nuance is more interesting but is a secondary finding. The paper risks appearing as \\\"Mesting + two more facets that turn out not to matter much.\\\" W2.  Item dominance is predictable from psychometric first principles.  In any assessment with heterogeneous item difficulty, item variance will dominate when other factors have small effects. MMLU items range from trivial recall to expert reasoning — of course this produces massive item variance. The paper's own Discussion section essentially explains why this must be the case (\\\"steep difficulty gradient within every benchmark\\\"). The 58% figure quantifies what psychometricians would predict qualitatively. The paper does not adequately engage with whether this finding is genuinely surprising vs. a confirmation of well-known measurement theory. The counter-argument in the paper framing doc (\\\"the magnitude was not previously quantified\\\") is weak — the magnitude is a function of the specific item difficulty distribution in these benchmarks, not a universal property of LLM evaluation. W3.  Significant related work gaps.  Several important bodies of work are missing: -  Classical G-theory beyond Cronbach 1972.  Brennan (2001, \\\"Generalizability Theory\\\") is the standard modern reference and is entirely absent. Shavelson & Webb (1991) is missing. The median paper draft cites Brennan but the best-case paper does not. This is a serious omission for a paper whose primary methodological framework is G-theory. -  Reproducibility in ML broadly.  Pineau et al. (2021, \\\"Improving Reproducibility in ML: A Report from the NeurIPS Reproducibility Program\\\") and the ML reproducibility checklist literature are not cited. Bouthillier et al. (2021, \\\"Accounting for Variance in Machine Learning Benchmarks\\\") directly decomposed hyperparameter vs. seed vs. dataset variance using ANOVA — this is the closest ML-native predecessor to the present work and is completely missing. -  IRT-based item analysis in NLP.  Item Response Theory is the dominant psychometric framework for item analysis, and there is growing work applying IRT to NLP benchmarks (e.g., Lalor et al. 2019; Rodriguez et al. 2021 on IRT for NLP evaluation; Vania et al. 2021). The paper's finding that item selection dominates would be enriched by connecting to IRT-based difficulty estimation. -  Prompt ordering sensitivity.  Lu et al. (2022, \\\"Fantastically Ordered Prompts and Where to Find Them\\\") is a seminal work on ordering effects in LLM evaluation. The paper includes ordering as a facet but does not cite this foundational work. -  Benchmark contamination and item difficulty.  The item dominance finding intersects with work on benchmark contamination (Jacovi et al. 2023; Deng et al. 2024) and adaptive/dynamic benchmarking, which are not discussed. -  Variance decomposition in deep learning.  Beyond Bouthillier, there is work by Henderson et al. (2018, \\\"Deep Reinforcement Learning that Matters\\\") on seed sensitivity and Dodge et al. (2020) on fine-tuning instability, both performing variance decomposition without G-theory. W4.  Positioning vs. Mesting is incomplete.  The paper claims to \\\"extend\\\" Mesting by adding infrastructure facets, but does not adequately address key differences: (a) Mesting included judge as a facet (43.8% variance), which this paper deliberately excludes — this makes the variance structures incomparable, and the paper's item dominance finding might not hold if judge were included; (b) Mesting studied API models with opaque infrastructure, while this paper studies open-weight models — the papers study fundamentally different evaluation settings; (c) the paper does not discuss whether its variance estimates are consistent with Mesting's for the overlapping facets (prompt, seed, temperature, item). A direct numerical comparison on shared facets would strengthen the positioning. W5.  D-study budgets are a straightforward computation, not a conceptual contribution.  Once variance components are estimated, D-study projections are a mechanical application of G-theory formulas (plug in different facet levels, compute G). Calling this a \\\"practical tool\\\" contribution overstates it — it is the standard output of any G-study. The novelty is in the variance component estimates, not in the D-study arithmetic. W6.  The \\\"first\\\" claims are overclaimed.  The paper claims \\\"first fully-crossed G-theory study spanning infrastructure x methodology x measurement.\\\" But Mesting (2026) already conducted a G-study of LLM evaluation with multiple crossed facets including items. The incremental \\\"first\\\" is adding hardware and precision facets to an existing G-theory framework. Similarly, \\\"first formal test of separability\\\" is a stretch — any multi-factor ANOVA implicitly tests interactions, which is the same as separability. The paper should frame its contribution as \\\"extending\\\" rather than claiming multiple \\\"firsts.\\\" W7.  Model as a fixed effect raises questions.  The paper pools across 4 models but treats model as fixed (not a random facet). This means the variance decomposition is conditional on this specific model set. If model were treated as a random facet (as in Mesting), model x item interactions might absorb a substantial portion of what is currently attributed to item main effect. The paper does not discuss this design choice or its implications. Questions for Authors Q1. How would the variance decomposition change if model were treated as a random facet rather than fixed? Specifically, what fraction of the current \\\"item_ id\\\" variance would be absorbed by model x item interactions? This is critical because the item dominance claim (58.4%) may be inflated by pooling across models with different difficulty profiles. Q2. Can you provide a direct numerical comparison with Mesting et al. (2026) on overlapping facets? Specifically, what are Mesting's estimates for item, prompt, temperature, and seed variance, and how do yours compare? If they differ substantially, what explains the discrepancy (different models, different evaluation protocol, different item samples)? Q3. If judge were added as a facet (as in Mesting, where it contributed 43.8%), would item dominance still hold? Your design decision to fix the judge is defensible but means your variance structure is not directly comparable to the most closely related prior work. Q4. The 0.5% threshold for separability appears arbitrary. What is the justification for this specific threshold? Would the conclusions change at 1%? At 2%? The multi-hardware G-study reports exactly 0.5% for direct interactions — right at the threshold — which warrants sensitivity analysis. Q5. The paper treats \\\"item selection\\\" as a single construct, but items vary in multiple dimensions (difficulty, domain, format, discrimination). Can you decompose item variance further — e.g., into difficulty, domain, and residual item components? This would make the \\\"prioritize item count\\\" recommendation more actionable (should practitioners sample more items within domains, or across domains?). Q6. Bouthillier et al. (2021) conducted ANOVA-based variance decomposition across datasets, hyperparameters, and seeds for ML benchmarks generally. How do your findings compare? Their work predates yours and covers similar ground using simpler methods. What does G-theory add beyond what ANOVA decomposition already provides? Minor Issues M1. The bibliography has only 7 entries for a paper of this scope. A related work section citing only 7 papers at a top venue will raise immediate red flags. Expect 30-50 references minimum. M2. The title is 22 words long and contains a colon, a subtitle, and a methodological term. Consider shortening — e.g., \\\"Reproducibility Budgets for LLM Evaluation via Generalizability Theory.\\\" M3. The abstract mentions \\\"over 2 million evaluation records\\\" but the experiments sum to approximately 2.7M records. Be precise. M4. The term \\\"empirical license\\\" for isolated-factor studies is loaded — it suggests this paper has authority to grant permission to other researchers. Consider \\\"empirical support for\\\" instead. M5. Table 1 reports residual at 16.8% — this is a large unexplained component. The paper should discuss what residual captures (higher-order interactions, measurement error, model-level stochasticity beyond seed). M6. The paper uses \\\"item dominance\\\" as a finding label, but in G-theory the term \\\"facet\\\" is standard. \\\"Item\\\" is the object of measurement, not a facet in the traditional sense. The paper should clarify the terminological mapping from psychometrics to ML evaluation more carefully. M7. The fine-tuning G-study uses RoBERTa-large, a 355M encoder model, which is architecturally very different from the 7-14B decoder models in the inference experiments. The generalizability of fine-tuning findings to modern LLM fine-tuning (e.g., LoRA on 7B+ models) is questionable. M8. Cronbach et al. (1972) citation is to the book \\\"The Dependability of Behavioral Measurements\\\" but the correct G-theory foundational reference is Cronbach, Gleser, Nanda & Rajaratnam (1972), which the paper does cite correctly in the bib — but should verify the title matches. Scores -  Novelty: 2.5/5 — The infrastructure extension over Mesting is modest (infrastructure contributes negligibly), the item dominance finding is predictable, and the D-study budgets are mechanical. The separability test and engine confound discovery provide genuine but limited novelty. -  Significance: 3/5 — The practical recommendations are useful and the scale is impressive, but the core message (\\\"use more items\\\") is not paradigm-shifting. The 18x cost factor for G >= 0.90 may actually discourage adoption. -  Related Work Completeness: 2/5 — Major gaps in classical G-theory references, ML reproducibility literature, IRT, and variance decomposition predecessors. Only 7 citations is far below venue expectations. -  Overall Score: 3/6 (Weak Reject) — A competent empirical study with impressive scale, but incremental novelty over Mesting et al. (2026), predictable main finding, significant related work gaps, and overclaimed \\\"first\\\" contributions. The separability test and engine confound are the strongest novel elements but are secondary to the paper's framing. With substantially expanded related work, more careful positioning (emphasizing extension rather than \\\"firsts\\\"), and deeper engagement with why item dominance is or is not surprising, this could reach borderline accept. -  Confidence: 4/5 — I am familiar with G-theory, the LLM evaluation reproducibility literature, and the ML benchmarking literature. I have read the cited papers. My uncertainty is primarily around whether the engine confound finding would be valued more highly by systems-oriented reviewers.\\n[05-20 19:34] cli_a974499e77fadbdd: 🌙  [Dream Review Report — best | dream_20260520T190053]  · Overall: Weak Accept (4/6) R1 Review: Methods and Experiments Summary This paper applies Generalizability Theory to LLM evaluation in a fully-crossed design spanning infrastructure (hardware, precision) x methodology (prompt, seed, temperature, ordering) x measurement (item) factors across 6 models, 5 benchmarks, and >2M records. The core finding is that item selection dominates variance (42-58%), direct infrastructure x methodology interactions are negligible (<0.5%), and current evaluation practices yield unacceptably low generalizability (G <0.40). D-study projections provide actionable reproducibility budgets. The methodology is largely sound and the experimental coverage is impressive, but several issues with estimation, design balance, generalizability claims, and missing analyses prevent a higher score. Strengths S1.  Correct and well-motivated G-theory application.  The paper properly applies REML estimation for variance component extraction in a random-effects framework. The choice of G-theory over simpler ANOVA decomposition is well-justified: it enables simultaneous multi-facet decomposition and D-study projections, which are the paper's key practical contribution. The universe score / relative error decomposition for the G coefficient follows standard Brennan (2001) formulations. S2.  Engine confound identification is a genuine methodological contribution.  The discovery that vLLM routes FP32 through a different compute path than BF16/FP16 (inflating precision variance from 0.3% to 0.87% main, 1.8% to 7.24% interaction) is valuable to the community independent of the G-theory framing. The fix (V0 enforce_ eager for all precision modes) is principled and well-documented. This demonstrates the kind of careful confound control that is often missing in LLM evaluation studies. S3.  Comprehensive experimental coverage.  All 8 planned experiments are reflected in the paper, covering: multi-model (6 models), multi-benchmark (5 benchmarks), multi-hardware (2 GPU types), scale validation (14B), paradigm extension (fine-tuning), and precision mode analysis (LayerCast). The total record count (>2M) provides substantial statistical power. The cross-benchmark gradient (item_ id share decreasing with task difficulty) is a genuinely interesting finding. S4.  Actionable D-study budgets.  The reproducibility budget tables (Tables 7-8) translate abstract variance components into concrete practitioner guidance. The \\\"10x more effective to triple items than triple prompts\\\" headline is well-supported by the marginal effectiveness ratios and will be immediately useful to evaluation practitioners. S5.  Appropriate use of generation-based evaluation.  Following Hua et al. (2025) to avoid log-likelihood scoring artifacts is a sound design choice that strengthens the ecological validity of the findings. Weaknesses W1.  The \\\"fully crossed\\\" design has important structural gaps.  The paper claims a fully-crossed design but several elements are not fully crossed: -  Exp-1 (MMLU) uses 3 precisions x 6 prompts x 6 seeds x 3 temperatures x 4 orderings, but Exp-2 (GSM8K/ARC/HellaSwag) uses only 2 precisions x 2 temperatures. This means the cross-benchmark comparisons in Table 3 are not on equal footing -- MMLU has richer factorial coverage and more records (1,036,800 vs 230,400 per benchmark). -  Hardware is only crossed in Exp-3 (MMLU), not in the multi-benchmark experiments. The separability claim therefore rests on a single benchmark. -  The 14B extension (Exp-5) uses 2 precisions only, not the full factorial. Claiming \\\"scale invariance\\\" from a reduced design on one benchmark is an overstatement. -  These design imbalances mean the pooled analyses implicitly weight MMLU more heavily. The paper should be transparent about which claims rest on full versus partial factorial evidence. W2.  200 items is potentially insufficient for stable higher-order interaction estimates.  With 200 items per benchmark and up to 12 variance components (Table 1), some interaction terms (especially 3-way and higher) are estimated from thin margins. The SEs in Table 1 are reported but several CIs are wide relative to the point estimates (e.g., ordering x item: 1.4% with CI [ 0.8, 2.0]; seed: 0.1% with CI [ 0.0, 0.2 ]). The paper does not report whether REML convergence diagnostics were checked, whether negative variance estimates were encountered and how they were handled (boundary constraints or set to zero), or whether bootstrap CIs were used as a robustness check. For a G-theory study, these are standard reporting requirements (Brennan 2001, Chapter 8). W3.  The 0.5% separability threshold is arbitrary and not well-justified.  The paper defines separability as direct infra x method interactions <0.5% of total variance, and the observed value is exactly 0.5% (Table 5). This is a razor-thin pass. The threshold is not derived from any established criterion in G-theory or psychometrics. Furthermore, \\\"0.5% of total variance\\\" is a relative measure that depends on the magnitude of item_ id variance -- if items were held fixed (eliminating 56% of variance), the same absolute interaction magnitude would represent ~ 1.1% of the remaining variance. The paper should either: (a) justify the threshold from first principles or prior literature, (b) report the result on an absolute scale (raw variance component values), or (c) frame it as a continuous quantity rather than a binary pass/fail. W4.  \\\"4 models pooled\\\" analysis conflates model-level and condition-level variance.  Pooling 4 models into a single variance decomposition (Table 1) is problematic because model is not a random facet in the same sense as prompt or seed -- these are 4 specific models, not a random sample from a model population. The pooled analysis implicitly treats model differences as part of the residual or item_ id component. The per-model analyses (Table 2) partially address this, but the headline numbers (58.4% item_ id) come from the pooled analysis. If model were included as a facet, model x item interactions could absorb substantial variance currently attributed to item_ id. The paper should either: (a) include model as a facet and report model x item interactions, or (b) report per-model results as primary and pooled as secondary, with clear caveats. W5.  D-study projections do not propagate estimation uncertainty.  The D-study budget tables report point estimates of G for each allocation but do not provide confidence intervals on G itself. Since G is a function of estimated variance components, and those components have non-trivial SEs (Table 1), the projected G values inherit estimation uncertainty. A G=0.90 projection could easily be G=[ 0.85, 0.95 ] given the component SEs. Without propagated uncertainty, the specific budget recommendations (e.g., \\\"600 items + 3 prompts + 2 seeds\\\") appear more precise than warranted. Bootstrap or delta-method CIs on projected G values are standard in D-study practice. W6.  The fine-tuning extension (RoBERTa-large on 4 NLU tasks) is a weak generalizability probe.  RoBERTa-large is a 355M encoder model fine-tuned on classification tasks -- architecturally and procedurally very different from 7-14B decoder models evaluated via generation. Claiming that \\\"item dominance extends to fine-tuning\\\" based on this single architecture on classification tasks is a stretch. The fine-tuning facet structure is also quite different (seed, LR, data shuffle, GPU, precision vs. prompt, seed, temperature, ordering, precision, hardware), making direct comparison of variance shares across paradigms (Table 10) potentially misleading. This extension would be more convincing with at least one generative fine-tuning setting (e.g., SFT of a 7B model). W7.  Missing dual-metric analysis undermines a key design decision.  The project's decisions.yaml (D002) records a deliberate decision to adopt dual-metric analysis (binary correct + text exact match) as a core methodology, noting that text exact match produces fundamentally different variance structure (prompt x item dominant at 37.5%, G=0.975). This analysis is entirely absent from the paper. Its omission is concerning because: (a) it would substantially complicate the \\\"item dominance\\\" narrative (item_ id may not dominate under text exact match), and (b) it was identified as a methodological strength. If the dual-metric analysis was dropped, the paper should justify why; if it was never completed, the paper should acknowledge that variance structure is metric-conditional. W8.  Only 2 GPU types for the hardware facet.  The hardware facet has only 2 levels (RTX PRO 6000 + one other GPU). In G-theory, variance component estimates for facets with very few levels are unstable. With k=2 levels, the hardware main effect and hardware x item interaction have 1 degree of freedom each, providing minimal power to detect non-zero components. The 0.6% hardware main effect could easily be noise. The paper should acknowledge this limitation more prominently rather than drawing strong conclusions about hardware effects from 2 GPUs. Questions for Authors Q1. How were negative variance component estimates handled in REML? Were any components estimated as negative and subsequently constrained to zero? If so, which components and in which experiments? This is critical for interpreting the small components (seed: 0.1%, ordering: 0.3%). Q2. The paper reports 1,036,800 records for Exp-1 as 4 models x 3 precisions x 6 prompts x 6 seeds x 3 temperatures x 4 orderings x 200 items. Was model included as a facet in the REML estimation, or were records from 4 models simply concatenated? If concatenated, model-level variance is confounded with item_ id and residual. Please clarify the exact mixed model specification. Q3. The separability test uses data from Exp-3 (691,200 records on MMLU only). Were separability tests conducted on the other 4 benchmarks? If not, the separability claim is benchmark-conditional, which undermines its generality. Q4. Table 1 components sum to approximately 95.5% (58.4+16.8+6.1+5.8+2.9+1.8+1.4+0.9+0.7+0.3+0.3+0.1=95.5). What accounts for the remaining ~ 4.5%? Higher-order interactions? Confounded terms? This should be explained. Q5. The D002 decision explicitly adopted dual-metric (binary correct + text exact match) analysis as a core methodology, noting that text exact match yields G=0.975 with a completely different variance hierarchy. Why was this analysis excluded from the paper? Does item dominance hold under text exact match? Q6. For the fine-tuning G-study, was item treated as a random facet in the same way as for inference? In fine-tuning, all training items are used for training, and item_ id refers to test items. Is the item_ id variance in Table 10 comparable across the two paradigms? Q7. The paper uses vLLM 0.9.2 with V0 enforce_ eager. Were any experiments run with V1 or batch-invariant kernels to quantify how much the engine choice itself contributes to the variance decomposition? Given the engine confound discovery, the variance estimates are conditional on this specific engine configuration. Minor Issues M1.  Table 1 column headers : \\\"SE\\\" and \\\"95% CI\\\" are not defined in the table caption. Are SEs computed via REML information matrix, jackknife, or bootstrap? The method matters for interpretation. M2.  Inconsistent facet levels across experiments : The method section lists temperatures as \\\"2-3 levels (T in {0.1, 0.5, 1.0})\\\" but Exp-2 uses only 2 temperatures. The specific levels used in each experiment should be listed in a supplementary table. M3.  Table 8 (MATH budget) : 1,100 items x 3 prompts x 2 seeds = 6,600 evaluations, but the table reports 13,200. This implies either 4 prompts x 3 seeds or some other configuration not stated in the table header (\\\"3 prompts, 2 seeds\\\"). M4.  Missing effect sizes : Variance percentages are relative measures. Raw variance components (on the original score scale) should be reported at least in supplementary material to allow readers to assess practical significance. M5.  Bibliography incomplete : Several citations use placeholder information (e.g., \\\"arXiv:2501.xxxxx\\\" for ThinkingMachines 2025). Multiple cited papers lack venue, year, or full author information. M6.  No software/code availability statement.  For a methodology paper advocating specific evaluation practices, releasing the analysis pipeline and variance decomposition code would substantially increase impact and allow independent verification. M7.  The paper would benefit from a Figure 1  showing the facet structure diagram. The fully-crossed design is the paper's key methodological contribution, and a visual representation would aid comprehension. The current paper has no figures at all. M8.  Notation : The G-theory formulation in Eq. 1 uses generic alpha terms but does not specify which terms are estimated in each experiment. A mapping from the generic model to the specific facet structure would help readers unfamiliar with G-theory. Scores -  Soundness: 3/5 — Core G-theory application is correct, but the pooled-model analysis strategy, arbitrary separability threshold, missing dual-metric analysis, and lack of uncertainty propagation in D-study projections are non-trivial methodological concerns. -  Empirical Rigor: 4/5 — Impressive scale and coverage (2M+ records, 6 models, 5 benchmarks), engine confound identification is exemplary, but design imbalances across experiments and the thin hardware facet (k=2) weaken several claims. -  Overall Score: 4/6 (Weak Accept) — The paper addresses an important gap (unified infrastructure x methodology variance decomposition), provides actionable practical guidance (reproducibility budgets), and the engine confound finding alone justifies publication. However, the methodological concerns (W3-W5, W7) and design imbalances (W1) prevent confident acceptance. Addressing W4 (model as facet), W5 (uncertainty on G projections), and W7 (dual-metric analysis) in revision would elevate this to a clear accept. -  Confidence: 4/5 — Familiar with G-theory, REML estimation, and LLM evaluation methodology. Reviewed the full paper, experimental design, imagined results, and project context including design decisions.\\n[05-20 19:30] : [system]\\n[05-20 19:30] : [system]\", \"mode\": \"chat\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "6b8ce20c-481a-46f6-98b3-4989722c48c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Runtime record

_source line 1296 · 2026-05-21T03:11:58.150Z_

```json
{
  "parentUuid": "2c95eceb-deb6-4a33-92b5-db2ed6459f91",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4f0d0fa9-37b5-4df5-9a99-618ca3836edb",
  "timestamp": "2026-05-21T03:11:58.150Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

---


### Runtime record

_source line 1297_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[飞书用户 孙震 (ou_12185aa391efc8ff13eea9c848f0ab5a)]: 分析一下c群的审稿情况，然后再发掘发掘有没有提升空间",
  "leafUuid": "4f0d0fa9-37b5-4df5-9a99-618ca3836edb",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


### Runtime record

_source line 1298_

```json
{
  "type": "ai-title",
  "aiTitle": "Bootstrap NLP variance G-theory MVP",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


### Assistant

_source line 1299 · 2026-05-21T03:12:01.472Z_

<details><summary>Logged reasoning block</summary>

```text
The chat history is too large to read directly. Let me use an Agent to analyze it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f0d0fa9-37b5-4df5-9a99-618ca3836edb",
  "isSidechain": false,
  "requestId": "req_011CbEywQEZHvdhNV75oLvqX",
  "type": "assistant",
  "uuid": "718426c0-513f-4b00-8999-780572a512bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2KHEbMm511xybGgbYDKcY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 837,
      "cache_read_input_tokens": 97947,
      "output_tokens": 485,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 837,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 485,
          "cache_read_input_tokens": 97947,
          "cache_creation_input_tokens": 837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 837
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 1300 · 2026-05-21T03:12:09.862Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GsE9safrXkDPMAhwEcQgWZ`</summary>

```json
{
  "description": "Analyze Group C review chat",
  "prompt": "I need you to analyze a Feishu chat history from a paper review group (Group C) for the project nlp_variance_gtheory. The file is at:\n\n/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-projects-nlp-variance-gtheory--claude-sessions-director-754d9c1f/10a54869-31d0-4dae-bcb8-806914c682ec/tool-results/mcp-agent-ml-research-feishu_read_chat_history-1779333118130.txt\n\nThis is JSON with schema: {result: string}. The result field contains the actual chat messages.\n\nPlease:\n1. First probe the structure with jq (type/length/keys)\n2. Extract and read the content using jq or python to parse the messages\n3. Identify all participants and their roles\n4. Summarize the review process chronologically: what stages have been completed, what's the current status\n5. List ALL specific issues/concerns raised by reviewers, organized by severity/category\n6. Note any actionable recommendations or unresolved items\n7. Assess the overall review quality and identify areas where the paper/review process could be improved\n\nBe thorough - read ALL messages. Quote key findings verbatim where important. Report back in Chinese (中文).\n\nThe paper is about applying Generalizability Theory to LLM evaluation variance decomposition across benchmarks, models, and evaluation metrics. Target venue: AAAI 2027.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "718426c0-513f-4b00-8999-780572a512bc",
  "isSidechain": false,
  "requestId": "req_011CbEywQEZHvdhNV75oLvqX",
  "type": "assistant",
  "uuid": "d072b7ba-9225-420a-9c35-f61788b208c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2KHEbMm511xybGgbYDKcY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 837,
      "cache_read_input_tokens": 97947,
      "output_tokens": 485,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 837,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 485,
          "cache_read_input_tokens": 97947,
          "cache_creation_input_tokens": 837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 837
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1301 · 2026-05-21T03:15:26.090Z_

<details><summary>↩ Tool result · `toolu_01GsE9safrXkDPMAhwEcQgWZ`</summary>

```text
Now I have all the data needed for a comprehensive analysis. Here is the full report:

---

## Group C 审稿群聊分析报告

### 一、参与者与结构

**群聊时间**：2026-05-20 19:30 ~ 23:54（约4.5小时）

**参与者**：
- `cli_a974499e77fadbdd`：唯一的 bot 发送者（16条消息），发布了两轮 Dream Review Report
- 2条系统消息（群创建/初始化）

**无人类审稿人参与** — 本群全部内容是 Dream 模拟审稿（AI 模拟审稿人生成的假想审稿报告），不是真实的 Group C 审稿流程。群里没有真实的 Review Director、Reviewer 1、Reviewer 2 的对话。

### 二、时间线与审稿流程

| 时间段 | Dream ID | 内容 |
|--------|----------|------|
| 19:30-19:51 | `dream_20260520T190053` | 第一轮 Dream（8份报告：best/median/worst 三档，R1+R2+Roundtable） |
| 23:35-23:54 | `dream_20260520T222113` | 第二轮 Dream（8份报告：同结构） |

### 三、评分汇总

**第一轮 Dream（dream_20260520T190053）**：

| 档位 | R1 (Methods) | R2 (Novelty) | Roundtable |
|------|-------------|-------------|------------|
| Best | Weak Accept (4/6) | Weak Reject (3/6) | Borderline (3.5/6) |
| Median | Borderline Reject (4/6) | Weak Reject (3/6) | Borderline Reject (4/6) |
| Worst | Borderline Reject (3/6) | Weak Reject (3/6) | Weak Reject (3/6) |

**第二轮 Dream（dream_20260520T222113）** — 明显改善：

| 档位 | R1 (Methods) | R2 (Novelty) | Roundtable |
|------|-------------|-------------|------------|
| Best | Weak Accept (4/6) | Weak Accept (4/6) | Weak Accept (4/6) |
| Median | Weak Accept (4/6) | Weak Accept (4/6) | Weak Accept (4/6) |
| Worst | Weak Accept (4/6) | Weak Reject (3/6) | Weak Reject (3/6) |

**趋势**：从第一轮到第二轮，论文从 borderline reject 区间上升到 weak accept 区间。R2（新颖性）始终是最苛刻的审稿人。

### 四、所有审稿问题分类汇总

#### A. 结构性/致命级问题（三档一致指出 — 最高优先级）

**A1. 零图表（18-19张表，0张图）**
- 所有审稿一致认为这是"serious presentation weakness"/"critical presentation failure"
- 原话（Dream2 Roundtable）："With 19 tables and 0 figures, the paper is dense and visually monotonous. This is a competitive disadvantage at a top venue."
- 所需图表：(1) 跨benchmark方差堆叠柱状图; (2) D-study投影曲线; (3) facet effectiveness ratio可视化; (4) bootstrap CI forest plot

**A2. 二值数据在 G-theory 中的方法论问题**
- 标准 Henderson III / REML 假设连续近正态响应变量；二值 0/1 数据违反此假设
- 原话（Dream2 R1）："Item variance is mechanically linked to item difficulty via the Bernoulli variance function p(1-p), partially inflating item_id dominance."
- 要求：至少讨论此局限，理想情况应用 generalized G-theory (Brennan 2001, Ch.12) 或 link-function 分解

**A3. Temperature 和 ordering 作为随机 facet 的合理性**
- Temperature 只有2-3个特定设计点(0, 0.5, 1.0)，不是从分布中随机抽取
- Ordering 是4个系统性轮换，不是随机排列
- 要求：提供 fixed vs. random 的敏感性分析

#### B. 重大方法论问题（Major）

**B1. 跨 benchmark 设计不对称**
- MMLU: 3 precisions x 3 temperatures; 其他 benchmark: 2 x 2
- FP32 在非 MMLU 实验中缺失
- 原话："Comparing variance percentages across different factorial structures without matched-design sensitivity analysis is methodologically questionable."
- 要求：至少用 BF16/FP16-only 重新分析 MMLU 以匹配设计

**B2. Separability 声明过度概括**
- 摘要说 "<0.3% under binary scoring"，但 GSM8K 达 3.0%，MATH 达 2.5%
- 3/5 benchmarks 成立，2/5 不成立 — 这是 benchmark-conditional 结论，不是一般性结论
- 要求：摘要和结论需加限定条件

**B3. D-study 优化过程未记录 + 算术异常**
- Table 10 (GSM8K): 减少 items 从 200→150 反而 G 从 0.68 升到 0.90 — 违反单调性
- "Optimal" prompt/seed 数量的确定方法未说明
- 原话："Practitioners will use these specific numbers; they must be derived from a transparent procedure."

**B4. G-coefficient 解释误导**
- G=0.22 for 200 items ≠ MMLU 本身不可靠（标准 MMLU 用全部~14K items）
- D-study 投影到 14K items 时 G 很可能 >0.90
- 原话："The paper's alarming framing risks misleading practitioners by applying item-level G to benchmark-level decisions."

**B5. Bootstrap 方法论缺陷**
- 有放回抽样 200 items 产生约 127 个唯一 items — 重复 items 违反独立性假设
- CI 可能偏窄
- 要求：考虑 cluster bootstrap 或 jackknife

#### C. 新颖性与定位问题（Moderate-Major）

**C1. 相对于 Mesting (2026) 的增量性新颖性**
- Infrastructure facets 贡献几乎可忽略（hardware 0.6%, precision 0.3%）
- 原话（Dream1 R2）："The paper risks appearing as 'Mesting + two more facets that turn out not to matter much.'"
- 建议：诚实 reframe — infrastructure crossing 是 confirmatory null；真正的新颖性是 cross-benchmark gradient 和 D-study budgets

**C2. Item dominance 部分可从心理测量学第一原理预测**
- 任何有异质 item difficulty 的评估都会显示 item variance 占主导
- 原话："The paper should acknowledge: 'Item dominance is expected from measurement theory; what we contribute is its precise magnitude, systematic variation with task reasoning demands, and D-study implications.'"

**C3. 标题承诺"Evaluation Metrics"但主文仅提供 binary scoring**
- Logprob 分析被放到一段话的附录
- 要求：要么交付 metric-conditional 分析，要么调整标题

#### D. 参考文献问题

**D1. 第一轮只有7篇引用 — "far below top-venue standards"**（第二轮改善到22篇但仍不够）

**关键缺失引用（跨两轮一致指出）**：
- Bouthillier et al. (2021, JMLR) — ML variance decomposition 的最近前辈
- GeneralizIT (Nalisnick et al., 2024) — G-theory 软件包
- Kunievsky et al. (2025) — prompt sensitivity decomposition
- Brittlebench (2026) — prompt brittleness benchmark
- Bui et al. (2025) — seed sensitivity in fine-tuning
- ThinkingMachines (2025) — batch invariance failure
- Cardinet, Johnson, & Pini (2010) — G-theory variance component stability
- Lu et al. (2022) — ordering effects
- Henderson et al. (2018) — deep RL reproducibility
- Polo et al. (2024) / tinyBenchmarks — benchmark subsampling

#### E. 实验范围限制

**E1. Fine-tuning 实验（RoBERTa-large）架构不匹配**
- 355M encoder-only 分类模型 vs. 7-14B decoder-only 生成模型
- 所有审稿一致：cross-paradigm generalization 声明不成立
- 建议：至少加一个 decoder-only fine-tuning (e.g., Llama-8B + LoRA)

**E2. 无 70B+ 模型**
- 更大模型可能压缩 item_id（更高精度）并减少 CoT 随机性

**E3. 只有2种 GPU 类型**
- hardware facet 只有 1 df，估计不稳定

**E4. 14B 扩展欠缺统计效力**
- 仅2个模型，scale 和 architecture 混淆

**E5. Item resampling stability 仅测试 MMLU**
- 未在 reasoning benchmarks 上测试（那里最需要稳定性验证）

#### F. 次要问题

- Table 数值不一致（部分表不加和到100%、记录数不匹配）
- Henderson Method I vs III 命名不一致
- 负方差分量处理方式未说明
- 无多重比较校正
- 缺乏可重复性细节（vLLM commit hash, model weight hashes, CUDA版本, prompt template全文）
- "LayerCast" 非标准术语未定义
- 无成本分析（推荐的 D-study budget 需要多少 GPU 小时）

### 五、两轮 Dream 之间的改善

第二轮相比第一轮明确改善的方面：
1. **Model-as-facet 分析** — 正确将 model 作为 crossed random facet，分离 model x item interaction (10-22%)
2. **参考文献** — 从7篇扩展到22篇
3. **Bootstrap CIs** — 添加了 item_id 的 bootstrap CI
4. **Framing 诚实度** — infrastructure crossing 被 reframe 为 confirmatory null
5. **REML vs Henderson 敏感性分析** — 两者差异 <1.4pp

仍未解决的问题：
- 零图表
- 二值数据方法论局限
- Temperature/ordering 作为 random facet
- 跨 benchmark 设计不对称
- D-study 优化过程不透明
- 标题与内容不匹配

### 六、可行动建议（按优先级排序）

**必须修复（阻碍 accept）**：
1. 添加 3-5 张图（堆叠柱状图、D-study 曲线、CI forest plot）
2. 讨论二值数据在 G-theory 中的局限性
3. Temperature 作为 fixed facet 的敏感性分析
4. 限定 separability 声明范围（"knowledge benchmarks 上 <0.3%"）
5. 记录 D-study 优化过程并修复算术异常

**应当修复**：
6. BF16/FP16-only MMLU 重新分析用于跨 benchmark 对比
7. 补充 5 篇缺失引用
8. 标题与内容对齐
9. 添加可重复性细节

**锦上添花**：
10. 扩展 logprob 分析到所有 5 个 benchmarks
11. 添加 D-study 推荐预算的 GPU 小时成本估算
12. 展开高阶交互分析

### 七、整体评估

**审稿质量**：Dream 模拟审稿质量极高 — 两位模拟审稿人（R1 方法论 / R2 新颖性）分工明确，在 G-theory 方法论、心理测量学文献、ML 评估实践方面展现了专家级知识。审稿覆盖面广泛，从方法论假设违反到实验设计不对称到参考文献缺失均有涉及。

**论文现状**：第二轮 Dream 的 best/median 档均达到 Weak Accept (4/6)，表明论文核心方向（cross-benchmark variance gradient + D-study reproducibility budgets）已站住脚。但 worst 档仍为 Weak Reject (3/6)，说明容错率有限 — 如果实际审稿人恰好是 psychometrics 专家或对增量新颖性苛刻，论文可能被拒。

**最关键的改善杠杆**：添加图表 + 讨论二值数据局限 + 限定 separability 声明范围。这三项改动不需要新实验，预计可将论文从 borderline 推至 solid weak accept (4-5/6)。

**风险点**：worst case 中 R2 的核心批评 — "variance decomposition is a measurement, not a fact" 的 framing 在心理测量学界是 well-known（不是发现） — 如果 AAAI 审稿人有 psychometrics 背景，这可能成为 reject 的主要理由。应对策略：reframe 为"在 LLM evaluation 这个新领域量化已知问题的规模"，而非声称发现了新概念。

agentId: a0fb11c61693717cd (use SendMessage with to: 'a0fb11c61693717cd' to continue this agent)
&lt;usage>total_tokens: 110944
tool_uses: 20
duration_ms: 196222&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d072b7ba-9225-420a-9c35-f61788b208c7",
  "isSidechain": false,
  "promptId": "8a5b1a73-827a-4f60-a50c-f013e2c40e39",
  "type": "user",
  "uuid": "6ae6a747-8344-44f8-b58e-73221a253366",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to analyze a Feishu chat history from a paper review group (Group C) for the project nlp_variance_gtheory. The file is at:\n\n/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-projects-nlp-variance-gtheory--claude-sessions-director-754d9c1f/10a54869-31d0-4dae-bcb8-806914c682ec/tool-results/mcp-agent-ml-research-feishu_read_chat_history-1779333118130.txt\n\nThis is JSON with schema: {result: string}. The result field contains the actual chat messages.\n\nPlease:\n1. First probe the structure with jq (type/length/keys)\n2. Extract and read the content using jq or python to parse the messages\n3. Identify all participants and their roles\n4. Summarize the review process chronologically: what stages have been completed, what's the current status\n5. List ALL specific issues/concerns raised by reviewers, organized by severity/category\n6. Note any actionable recommendations or unresolved items\n7. Assess the overall review quality and identify areas where the paper/review process could be improved\n\nBe thorough - read ALL messages. Quote key findings verbatim where important. Report back in Chinese (中文).\n\nThe paper is about applying Generalizability Theory to LLM evaluation variance decomposition across benchmarks, models, and evaluation metrics. Target venue: AAAI 2027.",
    "agentId": "a0fb11c61693717cd",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the data needed for a comprehensive analysis. Here is the full report:\n\n---\n\n## Group C 审稿群聊分析报告\n\n### 一、参与者与结构\n\n**群聊时间**：2026-05-20 19:30 ~ 23:54（约4.5小时）\n\n**参与者**：\n- `cli_a974499e77fadbdd`：唯一的 bot 发送者（16条消息），发布了两轮 Dream Review Report\n- 2条系统消息（群创建/初始化）\n\n**无人类审稿人参与** — 本群全部内容是 Dream 模拟审稿（AI 模拟审稿人生成的假想审稿报告），不是真实的 Group C 审稿流程。群里没有真实的 Review Director、Reviewer 1、Reviewer 2 的对话。\n\n### 二、时间线与审稿流程\n\n| 时间段 | Dream ID | 内容 |\n|--------|----------|------|\n| 19:30-19:51 | `dream_20260520T190053` | 第一轮 Dream（8份报告：best/median/worst 三档，R1+R2+Roundtable） |\n| 23:35-23:54 | `dream_20260520T222113` | 第二轮 Dream（8份报告：同结构） |\n\n### 三、评分汇总\n\n**第一轮 Dream（dream_20260520T190053）**：\n\n| 档位 | R1 (Methods) | R2 (Novelty) | Roundtable |\n|------|-------------|-------------|------------|\n| Best | Weak Accept (4/6) | Weak Reject (3/6) | Borderline (3.5/6) |\n| Median | Borderline Reject (4/6) | Weak Reject (3/6) | Borderline Reject (4/6) |\n| Worst | Borderline Reject (3/6) | Weak Reject (3/6) | Weak Reject (3/6) |\n\n**第二轮 Dream（dream_20260520T222113）** — 明显改善：\n\n| 档位 | R1 (Methods) | R2 (Novelty) | Roundtable |\n|------|-------------|-------------|------------|\n| Best | Weak Accept (4/6) | Weak Accept (4/6) | Weak Accept (4/6) |\n| Median | Weak Accept (4/6) | Weak Accept (4/6) | Weak Accept (4/6) |\n| Worst | Weak Accept (4/6) | Weak Reject (3/6) | Weak Reject (3/6) |\n\n**趋势**：从第一轮到第二轮，论文从 borderline reject 区间上升到 weak accept 区间。R2（新颖性）始终是最苛刻的审稿人。\n\n### 四、所有审稿问题分类汇总\n\n#### A. 结构性/致命级问题（三档一致指出 — 最高优先级）\n\n**A1. 零图表（18-19张表，0张图）**\n- 所有审稿一致认为这是\"serious presentation weakness\"/\"critical presentation failure\"\n- 原话（Dream2 Roundtable）：\"With 19 tables and 0 figures, the paper is dense and visually monotonous. This is a competitive disadvantage at a top venue.\"\n- 所需图表：(1) 跨benchmark方差堆叠柱状图; (2) D-study投影曲线; (3) facet effectiveness ratio可视化; (4) bootstrap CI forest plot\n\n**A2. 二值数据在 G-theory 中的方法论问题**\n- 标准 Henderson III / REML 假设连续近正态响应变量；二值 0/1 数据违反此假设\n- 原话（Dream2 R1）：\"Item variance is mechanically linked to item difficulty via the Bernoulli variance function p(1-p), partially inflating item_id dominance.\"\n- 要求：至少讨论此局限，理想情况应用 generalized G-theory (Brennan 2001, Ch.12) 或 link-function 分解\n\n**A3. Temperature 和 ordering 作为随机 facet 的合理性**\n- Temperature 只有2-3个特定设计点(0, 0.5, 1.0)，不是从分布中随机抽取\n- Ordering 是4个系统性轮换，不是随机排列\n- 要求：提供 fixed vs. random 的敏感性分析\n\n#### B. 重大方法论问题（Major）\n\n**B1. 跨 benchmark 设计不对称**\n- MMLU: 3 precisions x 3 temperatures; 其他 benchmark: 2 x 2\n- FP32 在非 MMLU 实验中缺失\n- 原话：\"Comparing variance percentages across different factorial structures without matched-design sensitivity analysis is methodologically questionable.\"\n- 要求：至少用 BF16/FP16-only 重新分析 MMLU 以匹配设计\n\n**B2. Separability 声明过度概括**\n- 摘要说 \"<0.3% under binary scoring\"，但 GSM8K 达 3.0%，MATH 达 2.5%\n- 3/5 benchmarks 成立，2/5 不成立 — 这是 benchmark-conditional 结论，不是一般性结论\n- 要求：摘要和结论需加限定条件\n\n**B3. D-study 优化过程未记录 + 算术异常**\n- Table 10 (GSM8K): 减少 items 从 200→150 反而 G 从 0.68 升到 0.90 — 违反单调性\n- \"Optimal\" prompt/seed 数量的确定方法未说明\n- 原话：\"Practitioners will use these specific numbers; they must be derived from a transparent procedure.\"\n\n**B4. G-coefficient 解释误导**\n- G=0.22 for 200 items ≠ MMLU 本身不可靠（标准 MMLU 用全部~14K items）\n- D-study 投影到 14K items 时 G 很可能 >0.90\n- 原话：\"The paper's alarming framing risks misleading practitioners by applying item-level G to benchmark-level decisions.\"\n\n**B5. Bootstrap 方法论缺陷**\n- 有放回抽样 200 items 产生约 127 个唯一 items — 重复 items 违反独立性假设\n- CI 可能偏窄\n- 要求：考虑 cluster bootstrap 或 jackknife\n\n#### C. 新颖性与定位问题（Moderate-Major）\n\n**C1. 相对于 Mesting (2026) 的增量性新颖性**\n- Infrastructure facets 贡献几乎可忽略（hardware 0.6%, precision 0.3%）\n- 原话（Dream1 R2）：\"The paper risks appearing as 'Mesting + two more facets that turn out not to matter much.'\"\n- 建议：诚实 reframe — infrastructure crossing 是 confirmatory null；真正的新颖性是 cross-benchmark gradient 和 D-study budgets\n\n**C2. Item dominance 部分可从心理测量学第一原理预测**\n- 任何有异质 item difficulty 的评估都会显示 item variance 占主导\n- 原话：\"The paper should acknowledge: 'Item dominance is expected from measurement theory; what we contribute is its precise magnitude, systematic variation with task reasoning demands, and D-study implications.'\"\n\n**C3. 标题承诺\"Evaluation Metrics\"但主文仅提供 binary scoring**\n- Logprob 分析被放到一段话的附录\n- 要求：要么交付 metric-conditional 分析，要么调整标题\n\n#### D. 参考文献问题\n\n**D1. 第一轮只有7篇引用 — \"far below top-venue standards\"**（第二轮改善到22篇但仍不够）\n\n**关键缺失引用（跨两轮一致指出）**：\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition 的最近前辈\n- GeneralizIT (Nalisnick et al., 2024) — G-theory 软件包\n- Kunievsky et al. (2025) — prompt sensitivity decomposition\n- Brittlebench (2026) — prompt brittleness benchmark\n- Bui et al. (2025) — seed sensitivity in fine-tuning\n- ThinkingMachines (2025) — batch invariance failure\n- Cardinet, Johnson, & Pini (2010) — G-theory variance component stability\n- Lu et al. (2022) — ordering effects\n- Henderson et al. (2018) — deep RL reproducibility\n- Polo et al. (2024) / tinyBenchmarks — benchmark subsampling\n\n#### E. 实验范围限制\n\n**E1. Fine-tuning 实验（RoBERTa-large）架构不匹配**\n- 355M encoder-only 分类模型 vs. 7-14B decoder-only 生成模型\n- 所有审稿一致：cross-paradigm generalization 声明不成立\n- 建议：至少加一个 decoder-only fine-tuning (e.g., Llama-8B + LoRA)\n\n**E2. 无 70B+ 模型**\n- 更大模型可能压缩 item_id（更高精度）并减少 CoT 随机性\n\n**E3. 只有2种 GPU 类型**\n- hardware facet 只有 1 df，估计不稳定\n\n**E4. 14B 扩展欠缺统计效力**\n- 仅2个模型，scale 和 architecture 混淆\n\n**E5. Item resampling stability 仅测试 MMLU**\n- 未在 reasoning benchmarks 上测试（那里最需要稳定性验证）\n\n#### F. 次要问题\n\n- Table 数值不一致（部分表不加和到100%、记录数不匹配）\n- Henderson Method I vs III 命名不一致\n- 负方差分量处理方式未说明\n- 无多重比较校正\n- 缺乏可重复性细节（vLLM commit hash, model weight hashes, CUDA版本, prompt template全文）\n- \"LayerCast\" 非标准术语未定义\n- 无成本分析（推荐的 D-study budget 需要多少 GPU 小时）\n\n### 五、两轮 Dream 之间的改善\n\n第二轮相比第一轮明确改善的方面：\n1. **Model-as-facet 分析** — 正确将 model 作为 crossed random facet，分离 model x item interaction (10-22%)\n2. **参考文献** — 从7篇扩展到22篇\n3. **Bootstrap CIs** — 添加了 item_id 的 bootstrap CI\n4. **Framing 诚实度** — infrastructure crossing 被 reframe 为 confirmatory null\n5. **REML vs Henderson 敏感性分析** — 两者差异 <1.4pp\n\n仍未解决的问题：\n- 零图表\n- 二值数据方法论局限\n- Temperature/ordering 作为 random facet\n- 跨 benchmark 设计不对称\n- D-study 优化过程不透明\n- 标题与内容不匹配\n\n### 六、可行动建议（按优先级排序）\n\n**必须修复（阻碍 accept）**：\n1. 添加 3-5 张图（堆叠柱状图、D-study 曲线、CI forest plot）\n2. 讨论二值数据在 G-theory 中的局限性\n3. Temperature 作为 fixed facet 的敏感性分析\n4. 限定 separability 声明范围（\"knowledge benchmarks 上 <0.3%\"）\n5. 记录 D-study 优化过程并修复算术异常\n\n**应当修复**：\n6. BF16/FP16-only MMLU 重新分析用于跨 benchmark 对比\n7. 补充 5 篇缺失引用\n8. 标题与内容对齐\n9. 添加可重复性细节\n\n**锦上添花**：\n10. 扩展 logprob 分析到所有 5 个 benchmarks\n11. 添加 D-study 推荐预算的 GPU 小时成本估算\n12. 展开高阶交互分析\n\n### 七、整体评估\n\n**审稿质量**：Dream 模拟审稿质量极高 — 两位模拟审稿人（R1 方法论 / R2 新颖性）分工明确，在 G-theory 方法论、心理测量学文献、ML 评估实践方面展现了专家级知识。审稿覆盖面广泛，从方法论假设违反到实验设计不对称到参考文献缺失均有涉及。\n\n**论文现状**：第二轮 Dream 的 best/median 档均达到 Weak Accept (4/6)，表明论文核心方向（cross-benchmark variance gradient + D-study reproducibility budgets）已站住脚。但 worst 档仍为 Weak Reject (3/6)，说明容错率有限 — 如果实际审稿人恰好是 psychometrics 专家或对增量新颖性苛刻，论文可能被拒。\n\n**最关键的改善杠杆**：添加图表 + 讨论二值数据局限 + 限定 separability 声明范围。这三项改动不需要新实验，预计可将论文从 borderline 推至 solid weak accept (4-5/6)。\n\n**风险点**：worst case 中 R2 的核心批评 — \"variance decomposition is a measurement, not a fact\" 的 framing 在心理测量学界是 well-known（不是发现） — 如果 AAAI 审稿人有 psychometrics 背景，这可能成为 reject 的主要理由。应对策略：reframe 为\"在 LLM evaluation 这个新领域量化已知问题的规模\"，而非声称发现了新概念。"
      }
    ],
    "totalDurationMs": 196222,
    "totalTokens": 110944,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 105555,
      "output_tokens": 3909,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1479
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3909,
          "cache_read_input_tokens": 105555,
          "cache_creation_input_tokens": 1479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1479,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 13,
      "searchCount": 0,
      "bashCount": 7,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "d072b7ba-9225-420a-9c35-f61788b208c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Assistant

_source line 1302 · 2026-05-21T03:15:35.085Z_

<details><summary>Logged reasoning block</summary>

```text
The agent did a thorough analysis. Let me summarize the key findings and identify improvement areas for the user. I need to reply in Chinese via director_reply_to_user.

Key findings:
1. Group C currently only has Dream simulation reviews (no real reviewers yet) - two rounds of Dream reviews
2. Dream #1: borderline reject → Dream #2: weak accept (improvement after framing revision)
3. Critical issues that persist across both rounds:
   - Zero figures (18-19 tables, 0 figures)
   - Binary data in G-theory (methodological limitation)
   - Temperature/ordering as random facets questionable
   - Cross-benchmark design asymmetry
   - D-study optimization undocumented
   - Separability claim over-generalized

Beyond what the Dream reviews flagged, there are additional improvement opportunities I should highlight in my comprehensive response to the user.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ae6a747-8344-44f8-b58e-73221a253366",
  "isSidechain": false,
  "requestId": "req_011CbEzCjLvqehEmNFkir4Sj",
  "type": "assistant",
  "uuid": "68636ec3-d4e8-4107-9d4f-05510ba568e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XBoukWtaYmyWKv998VH4Sn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4468,
      "cache_read_input_tokens": 98784,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 304,
          "cache_read_input_tokens": 98784,
          "cache_creation_input_tokens": 4468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4468
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 1303 · 2026-05-21T03:15:35.171Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MS99GWrokHu4k5Uunpt16j`</summary>

```json
{
  "query": "select:director_reply_to_user",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68636ec3-d4e8-4107-9d4f-05510ba568e4",
  "isSidechain": false,
  "requestId": "req_011CbEzCjLvqehEmNFkir4Sj",
  "type": "assistant",
  "uuid": "cce6d39c-128c-405a-a727-a14504beb95d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XBoukWtaYmyWKv998VH4Sn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4468,
      "cache_read_input_tokens": 98784,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 304,
          "cache_read_input_tokens": 98784,
          "cache_creation_input_tokens": 4468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4468
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1304 · 2026-05-21T03:15:35.175Z_

<details><summary>↩ Tool result · `toolu_01MS99GWrokHu4k5Uunpt16j`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cce6d39c-128c-405a-a727-a14504beb95d",
  "isSidechain": false,
  "promptId": "8a5b1a73-827a-4f60-a50c-f013e2c40e39",
  "type": "user",
  "uuid": "76813655-63aa-461a-92ef-1985f139cb02",
  "toolUseResult": {
    "matches": [],
    "query": "select:director_reply_to_user",
    "total_deferred_tools": 99
  },
  "sourceToolAssistantUUID": "cce6d39c-128c-405a-a727-a14504beb95d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Runtime record

_source line 1305_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[飞书用户 孙震 (ou_12185aa391efc8ff13eea9c848f0ab5a)]: 分析一下c群的审稿情况，然后再发掘发掘有没有提升空间",
  "leafUuid": "76813655-63aa-461a-92ef-1985f139cb02",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


### Runtime record

_source line 1306_

```json
{
  "type": "ai-title",
  "aiTitle": "Bootstrap NLP variance G-theory MVP",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


### Tool call

_source line 1307 · 2026-05-21T03:15:37.654Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Tje515LznAiaRcammdnr4V`</summary>

```json
{
  "query": "director reply user",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76813655-63aa-461a-92ef-1985f139cb02",
  "isSidechain": false,
  "requestId": "req_011CbEzDQA3KxuhkjcQjovN7",
  "type": "assistant",
  "uuid": "01495685-fb91-4971-a27a-4732ac747296",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eGjeUY5FpKTcCk9JUSzDF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 322,
      "cache_read_input_tokens": 103252,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 103252,
          "cache_creation_input_tokens": 322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 322
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1308 · 2026-05-21T03:15:37.661Z_

<details><summary>↩ Tool result · `toolu_01Tje515LznAiaRcammdnr4V`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_reply_to_user"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01495685-fb91-4971-a27a-4732ac747296",
  "isSidechain": false,
  "promptId": "8a5b1a73-827a-4f60-a50c-f013e2c40e39",
  "type": "user",
  "uuid": "2838f4df-bcf7-43b6-ae6d-3c1f8e595e7d",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__director_reply_to_user"
    ],
    "query": "director reply user",
    "total_deferred_tools": 99
  },
  "sourceToolAssistantUUID": "01495685-fb91-4971-a27a-4732ac747296",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Tool call

_source line 1309 · 2026-05-21T03:16:13.799Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_reply_to_user · `toolu_01KY844TD2GJw9szozKgvWhG`</summary>

```json
{
  "text": "## C群审稿分析 + 提升空间\n\n### 当前状态\n\nC群目前只有两轮 **Dream 模拟审稿**（AI 模拟审稿人），尚未进入真人/正式审稿流程。论文还在实验阶段，未提交审稿。\n\n**评分趋势**（framing 修订后明显改善）：\n\n| | Dream #1 | Dream #2 |\n|---|---|---|\n| Best | 3.5/6 (Borderline) | **4/6 (Weak Accept)** |\n| Median | 4/6 (Borderline Reject) | **4/6 (Weak Accept)** |\n| Worst | 3/6 (Weak Reject) | 3/6 (Weak Reject) |\n\n### 两轮 Dream 一致指出的核心问题（未解决）\n\n**必须修（阻碍 accept）：**\n\n1. **零图表** — 18-19 张表、0 张图。所有审稿一致认为\"critical presentation failure\"。需要 3-5 张：跨 benchmark 方差堆叠柱状图、D-study 投影曲线、bootstrap CI forest plot、model-as-facet 对比图\n\n2. **二值数据 + G-theory 方法论局限** — binary 0/1 违反 G-theory 连续正态假设，item variance 被 Bernoulli p(1-p) 机制性膨胀。需至少讨论局限，理想情况用 generalized G-theory\n\n3. **Temperature/ordering 作为 random facet 不合理** — 只有 2-3 个设计点，不是从分布中抽样。需提供 fixed vs random 敏感性分析\n\n4. **Separability 声明过度概括** — 摘要说\"<0.3%\"，但 GSM8K=3.0%、MATH=2.5%。需限定为\"knowledge benchmarks 上\"\n\n5. **D-study 优化过程未记录** — Table 10 有算术异常（减少 items 反而 G 上升），优化方法不透明\n\n**应当修：**\n\n6. 跨 benchmark 设计不对称（MMLU 3×3 vs 其他 2×2），需匹配设计敏感性分析\n7. G=0.22 的解释误导（200 items vs 实际 14K items），需区分 facet-level vs benchmark-level 可靠性\n8. Bootstrap 独立性问题（有放回抽样产生重复 items），需考虑 jackknife 对比\n9. 标题承诺\"Evaluation Metrics\"但 logprob 分析仅一段话\n\n### 提升空间（我的判断）\n\n**高杠杆（不需新实验，直接提分）：**\n\n1. **加图** — 这是投入产出比最高的一项。4 张图可以让论文从\"读起来像技术报告\"升级为\"conference paper\"。exp-001 数据很快全部就位，可以立即开始画\n2. **二值数据讨论 + 敏感性分析** — 在 Discussion 中用一段话承认局限，再用 text_exact_match（连续指标）做平行分析，证明结论 robust。我们已有 dual-metric 框架，这是现成的防守\n3. **fixed vs random 敏感性分析** — 纯分析任务，在 exp-004 中加一个 sub-analysis，代码改动很小\n\n**中杠杆（需要额外工作但值得）：**\n\n4. **IRT vs G-theory 直接对比** — tinyBenchmarks 推荐 ~100 items，我们 D-study 推荐 420。解释清楚 4× 差异（G-theory 考虑了 prompt/seed 维度而 IRT 忽略）会是一个独立贡献\n5. **扩展 logprob 分析** — 当前只在 MMLU 上做了。5 个 benchmark 都跑 logprob scoring 让标题名副其实\n6. **添加 D-study 的 GPU 成本估算** — 审稿人问\"推荐 420 items 的评估方案实际花多少钱\"，一张成本表直接回答\n\n**结论**：worst case 仍在 3/6，容错率有限。最大风险是审稿人有心理测量学背景时会认为核心概念不新颖。应对策略是 reframe 为\"在 LLM evaluation 新领域量化已知问题的规模\"。加图 + 二值数据讨论 + 限定 separability 这三项改动预计可把 worst case 从 3/6 推到 3.5-4/6。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2838f4df-bcf7-43b6-ae6d-3c1f8e595e7d",
  "isSidechain": false,
  "requestId": "req_011CbEzDayAtmqDMbJfD8pdn",
  "type": "assistant",
  "uuid": "acd9d228-32cc-4d23-96eb-5f6ed170d3c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01681BSJ2fizf1iS57N9tEfk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 384,
      "cache_read_input_tokens": 103574,
      "output_tokens": 1401,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 384,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1401,
          "cache_read_input_tokens": 103574,
          "cache_creation_input_tokens": 384,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 384
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1310 · 2026-05-21T03:16:14.544Z_

<details><summary>↩ Tool result · `toolu_01KY844TD2GJw9szozKgvWhG`</summary>

```text
{"result":"{\"success\": true}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acd9d228-32cc-4d23-96eb-5f6ed170d3c8",
  "isSidechain": false,
  "promptId": "8a5b1a73-827a-4f60-a50c-f013e2c40e39",
  "type": "user",
  "uuid": "6873df26-cd5a-452f-8f76-ffd3f3d69390",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true}"
    }
  },
  "sourceToolAssistantUUID": "acd9d228-32cc-4d23-96eb-5f6ed170d3c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Runtime record

_source line 1311_

```json
{
  "type": "ai-title",
  "aiTitle": "Bootstrap NLP variance G-theory MVP",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


### Runtime record

_source line 1312 · 2026-05-21T03:18:06.103Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:18:06.103Z",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "content": "[飞书用户 孙震 (ou_12185aa391efc8ff13eea9c848f0ab5a)]: 强力修复这些问题，并想尽办法尝试提升分数"
}
```

---


### Runtime record

_source line 1313 · 2026-05-21T03:18:06.104Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:18:06.104Z",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


## Round 167

## Round 167

2 recorded events


### User

_source line 1314 · 2026-05-21T03:18:06.094Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6873df26-cd5a-452f-8f76-ffd3f3d69390",
  "isSidechain": false,
  "promptId": "e7f4bce4-3601-4156-9c94-fdbb9b592014",
  "type": "user",
  "isMeta": true,
  "uuid": "15334b1a-fcdd-4254-b9a0-c90445d5fd8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Assistant

_source line 1315 · 2026-05-21T03:18:06.094Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15334b1a-fcdd-4254-b9a0-c90445d5fd8b",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "e8236993-aaeb-43fa-b799-bfe282195683",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "id": "ca2d00fb-eef2-41b3-a437-72ad6aefb424",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 168

## Round 168

32 recorded events


### User

_source line 1316 · 2026-05-21T03:18:06.249Z_

[飞书用户 孙震 (ou_12185aa391efc8ff13eea9c848f0ab5a)]: 强力修复这些问题，并想尽办法尝试提升分数

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8236993-aaeb-43fa-b799-bfe282195683",
  "isSidechain": false,
  "promptId": "e7f4bce4-3601-4156-9c94-fdbb9b592014",
  "type": "user",
  "uuid": "6b6830e5-2fe3-463e-b8a2-b72a329ca252",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Assistant

_source line 1317 · 2026-05-21T03:18:28.226Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to aggressively fix all the issues identified from the Dream reviews and find ways to boost the paper score. Let me think about what can be done right now vs. what needs to wait for experiment data.

Current state:
- exp-001 Llama: DONE (239,200 records)
- exp-001 Gemma bf16: DONE (86,400 records)
- exp-001 Gemma fp32: RUNNING (~21%, ~65 min to complete)
- Mistral: ready, waiting for GPU
- Qwen: downloaded, shards ready, waiting for GPU


- Analysis code: dry-run passed, -Infinity fix applied

I've got a clear split between what I can tackle immediately and what depends on the remaining experiments. For the immediate fixes, I can start working on the figures using the Llama data, dive into the binary data discussion with sensitivity analysis, run the fixed vs random comparisons, tighten up the separability claims, document the D-study optimization better, clarify the G-coefficient interpretation, compare bootstrap and jackknife approaches, expand the bibliography, realign the title, and establish a clearer IRT vs G-theory framework. The cross-model analysis will have to wait until the other experiments finish running.

My best move is to spin up multiple parallel tracks: get the Agent started on analysis and figure generation with what we have now, update the paper framing document to address all the conceptual issues, and plan out the additional sensitivity analyses. Since the user wants an aggressive fix, I should prioritize updating the framing document comprehensively while the Agent works through the analysis pipeline in parallel with the ongoing model runs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b6830e5-2fe3-463e-b8a2-b72a329ca252",
  "isSidechain": false,
  "requestId": "req_011CbEzQY5M9EW7mHHTM1ZNP",
  "type": "assistant",
  "uuid": "acdcd7eb-a19b-4b62-90f4-740ca64054de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113sTSXtLiz95LSenYqBEAy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 78,
      "cache_read_input_tokens": 105383,
      "output_tokens": 786,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 78,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 786,
          "cache_read_input_tokens": 105383,
          "cache_creation_input_tokens": 78,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 78
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 1318 · 2026-05-21T03:18:28.597Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_agent_queue_status · `toolu_01B7JwxFfPi6Q88EhvmTBibX`</summary>

```json
{
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acdcd7eb-a19b-4b62-90f4-740ca64054de",
  "isSidechain": false,
  "requestId": "req_011CbEzQY5M9EW7mHHTM1ZNP",
  "type": "assistant",
  "uuid": "202b5782-d05f-4a71-8c0e-9b84fcf06c79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113sTSXtLiz95LSenYqBEAy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 78,
      "cache_read_input_tokens": 105383,
      "output_tokens": 786,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 78,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 786,
          "cache_read_input_tokens": 105383,
          "cache_creation_input_tokens": 78,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 78
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1319 · 2026-05-21T03:18:28.633Z_

<details><summary>↩ Tool result · `toolu_01B7JwxFfPi6Q88EhvmTBibX`</summary>

```text
{"result":"{\"found\":true,\"processing\":false,\"depth\":0,\"current\":null,\"pending\":[],\"idle_seconds\":1312}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "202b5782-d05f-4a71-8c0e-9b84fcf06c79",
  "isSidechain": false,
  "promptId": "e7f4bce4-3601-4156-9c94-fdbb9b592014",
  "type": "user",
  "uuid": "0ab3ea6d-aaf6-4dba-b1a5-e36d66faabd0",
  "toolUseResult": "{\"result\":\"{\\\"found\\\":true,\\\"processing\\\":false,\\\"depth\\\":0,\\\"current\\\":null,\\\"pending\\\":[],\\\"idle_seconds\\\":1312}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"found\":true,\"processing\":false,\"depth\":0,\"current\":null,\"pending\":[],\"idle_seconds\":1312}"
    }
  },
  "sourceToolAssistantUUID": "202b5782-d05f-4a71-8c0e-9b84fcf06c79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Assistant

_source line 1320 · 2026-05-21T03:19:08.150Z_

<details><summary>Logged reasoning block</summary>

```text
Agent is idle for 22 minutes! I need to send immediate instructions. Let me plan the comprehensive fix strategy.

Current resources:
- 4 GPUs: running Gemma fp32 (should be done soon or already done given 22 min idle)
- Agent: idle
- CPU: available for analysis work

Let me send a comprehensive multi-worker instruction to the Agent, and simultaneously update paper_framing.md and experiment_plan.yaml to address the structural issues.

Let me structure the attack:

**Immediate parallel work (Agent, multiple Workers):**


I'll queue up seven concurrent analysis tasks: verify Gemma fp32 completion and trigger Mistral if ready, run full variance decomposition on the Llama dataset with 239K records, generate the four core figures from Llama results, implement sensitivity analysis for fixed versus random effects, set up dual-metric evaluation comparing binary and text_exact_match scoring, add jackknife resampling alongside bootstrap for confidence interval comparison, and establish the IRT comparison framework between tinyBenchmarks and D-study approaches.

**Director work:**
Update paper_framing.md to address structural gaps.
Update experiment_plan.yaml with the new analysis sub-tasks.

Now I'm thinking about what could meaningfully strengthen the paper. Implementing generalized G-theory with probit/logit link functions for binary data would be a solid methodological upgrade that directly counters the strongest criticism. Adding a 70B model would help with the scale concern but might be too resource-intensive given the timeline. Testing item resampling stability on reasoning tasks like GSM8K and MATH beyond just MMLU would address the knowledge-only limitation. A cost analysis table is straightforward to add and high-impact. Building a reproducibility package with code and data would round out the contribution.

I should also document the vLLM commit hash and model weight hashes to ensure full reproducibility, then send comprehensive instructions to the agent and update the framing documents accordingly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ab3ea6d-aaf6-4dba-b1a5-e36d66faabd0",
  "isSidechain": false,
  "requestId": "req_011CbEzSBsyMg1Qm3VJ8dP1S",
  "type": "assistant",
  "uuid": "cc2d0942-7944-439a-81da-0ead1bbc53b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qzp74Qn2SXfgTpx1NribAG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 105461,
      "output_tokens": 1771,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 834,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1771,
          "cache_read_input_tokens": 105461,
          "cache_creation_input_tokens": 834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 834
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 1321 · 2026-05-21T03:19:08.152Z_

Agent 空闲 22 分钟。全面反攻——同时推进多条线。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc2d0942-7944-439a-81da-0ead1bbc53b2",
  "isSidechain": false,
  "requestId": "req_011CbEzSBsyMg1Qm3VJ8dP1S",
  "type": "assistant",
  "uuid": "0d52bccb-6798-47ee-9cb8-9fa6b948db4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qzp74Qn2SXfgTpx1NribAG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 105461,
      "output_tokens": 1771,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 834,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1771,
          "cache_read_input_tokens": 105461,
          "cache_creation_input_tokens": 834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 834
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 1322 · 2026-05-21T03:19:28.558Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_main_agent · `toolu_01SqikadgjfzaQpSQ4iSQEx7`</summary>

```json
{
  "text": "[Director 指令] ⚡ 全面提分攻势 — 6 个 Worker 并行\n\n用户要求强力修复所有 Dream 审稿问题。以下任务全部并行派 Worker，不等 GPU 任务完成。\n\n---\n\n**Worker 1: GPU 状态 + 模型切换**\n- 检查 Gemma fp32 是否完成\n- 如果完成：合并 Gemma bf16+fp32 数据，注册 DONE，立即启动 Mistral 推理（4 GPU）\n- 如果未完成：报进度\n\n**Worker 2: Llama 单模型 G-study 全量分析**（CPU 任务）\n- 用 Llama 239,200 records 跑完整 G-theory 方差分解\n- 两个 metric 分别跑：binary correct + text exact match\n- 输出每个 variance component 百分比 + 排名\n- 特别关注：item_id 占比、precision main effect、temperature×item、residual\n- 与 MVP (50 items) 对比，验证 scaling 稳定性\n- 结果保存到 `artifacts/analysis/llama_single_model_gstudy.json`\n\n**Worker 3: Fixed vs Random 敏感性分析**（CPU 任务）\n- 实现代码：将 temperature 和 ordering 分别作为 fixed facet 重新分析\n- 对比 random vs fixed 的方差分解差异\n- 这直接回应 Dream reviewers 最强的方法论批评之一\n- 用 Llama 数据验证\n- 保存到 `artifacts/analysis/fixed_vs_random_sensitivity.json`\n\n**Worker 4: Bootstrap vs Jackknife 对比**（CPU 任务）\n- 在 bootstrap_ci.py 基础上实现 delete-1 jackknife CI\n- 用 Llama 数据对比 bootstrap (1000 resamples) vs jackknife 的 CI 宽度\n- bootstrap 有 item 重复导致独立性问题，jackknife 没有——如果 CI 宽度接近，证明 bootstrap 结果 robust\n- 保存到 `artifacts/analysis/bootstrap_vs_jackknife.json`\n\n**Worker 5: 二值数据局限性分析**（CPU 任务）\n- 计算 Llama 数据的 item difficulty 分布 p_i = mean(correct_i)\n- 计算 Bernoulli variance p_i(1-p_i) 与 observed item variance 的相关性\n- 如果高度相关（r > 0.9），说明 item_id 确实被 Bernoulli 机制膨胀\n- 用 text_exact_match 做平行分析，对比 binary vs continuous metric 的方差分解\n- 这是 Dream reviewers 的核心方法论批评——主动分析比被动承认强\n- 保存到 `artifacts/analysis/binary_data_limitation.json`\n\n**Worker 6: IRT vs G-theory 对比框架**（CPU 任务）\n- 用 Llama MMLU 数据做 IRT 2PL 模型拟合（用 `py-irt` 或手写 Rasch）\n- 基于 IRT item information 计算 \"IRT 推荐最少 items\"\n- 对比 D-study 推荐 vs IRT 推荐，解释差异来源（G-theory 考虑 prompt/seed/ordering 维度）\n- 这是论文的潜在独立贡献——\"first direct IRT vs G-theory comparison for LLM evaluation\"\n- 保存到 `artifacts/analysis/irt_vs_gtheory.json`\n\n---\n\n**优先级**：Worker 1 最紧急（GPU 不能空）。Worker 2-6 全部 CPU 任务，同时派出。\n\n**汇报格式**：每个 Worker 完成后汇报关键数值结果（不要只说\"完成了\"，要给数据）。",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d52bccb-6798-47ee-9cb8-9fa6b948db4d",
  "isSidechain": false,
  "requestId": "req_011CbEzSBsyMg1Qm3VJ8dP1S",
  "type": "assistant",
  "uuid": "44533a2f-a1d3-4501-adc7-c74149e69b49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qzp74Qn2SXfgTpx1NribAG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 105461,
      "output_tokens": 1771,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 834,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1771,
          "cache_read_input_tokens": 105461,
          "cache_creation_input_tokens": 834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 834
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1323 · 2026-05-21T03:19:32.471Z_

<details><summary>↩ Tool result · `toolu_01SqikadgjfzaQpSQ4iSQEx7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"message_id\": \"om_x100b6fd3d2f8d0bcb372a91ab2f9920\", \"queued\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44533a2f-a1d3-4501-adc7-c74149e69b49",
  "isSidechain": false,
  "promptId": "e7f4bce4-3601-4156-9c94-fdbb9b592014",
  "type": "user",
  "uuid": "53ac2e43-0228-4778-85c7-ba56c4b30d11",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"message_id\\\": \\\"om_x100b6fd3d2f8d0bcb372a91ab2f9920\\\", \\\"queued\\\": true}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"message_id\": \"om_x100b6fd3d2f8d0bcb372a91ab2f9920\", \"queued\": true}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "44533a2f-a1d3-4501-adc7-c74149e69b49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Assistant

_source line 1324 · 2026-05-21T03:19:37.190Z_

同时更新 paper_framing.md，把 Dream 审稿的结构性问题全部纳入。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53ac2e43-0228-4778-85c7-ba56c4b30d11",
  "isSidechain": false,
  "requestId": "req_011CbEzWtv9DFPbM8gFmY22i",
  "type": "assistant",
  "uuid": "67e40cbc-b681-4f04-82a3-2248af898197",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVr7pxPqMuUfKoAANBCPA1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 106295,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1843,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 106295,
          "cache_creation_input_tokens": 1843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1843
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 1325 · 2026-05-21T03:19:38.654Z_

<details open><summary>🔧 Tool call — Read · `toolu_017g3eh3y5QNaALnf7JVr1eX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67e40cbc-b681-4f04-82a3-2248af898197",
  "isSidechain": false,
  "requestId": "req_011CbEzWtv9DFPbM8gFmY22i",
  "type": "assistant",
  "uuid": "15efc705-f2a8-4065-99aa-eccf6c6dd08c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVr7pxPqMuUfKoAANBCPA1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 106295,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1843,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 106295,
          "cache_creation_input_tokens": 1843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1843
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1326 · 2026-05-21T03:19:38.666Z_

<details><summary>↩ Tool result · `toolu_017g3eh3y5QNaALnf7JVr1eX`</summary>

```text
1	# Paper Framing — nlp_variance_gtheory
2	
3	## Target Venue
4	- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)
5	- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)
6	- Extended: TACL (rolling)
7	
8	## Title
9	Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics
10	
11	## Core Claims (3 条，可证伪)
12	
13	**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation (MVP: 58.4% on MMLU single-model; expected to decrease with model-as-facet reanalysis). Its magnitude is hypothesized to be benchmark-dependent — weakening on reasoning tasks where temperature/seed interactions increase — but this gradient requires exp-002 confirmation. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating whether a systematic benchmark-dependent gradient exists, and (c) deriving D-study implications specific to LLM evaluation.
14	**Fallback narratives**: (A) If gradient confirmed → "benchmark-conditional variance structure"; (B) If gradient not significant → "item dominance is universal but magnitude varies"; (C) If model-as-facet reduces item_id below 30% → pivot to "model×item interaction is the dominant source" — narrative direction changes substantially.
15	
16	**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), "infrastructure" is currently limited to the precision facet.
17	
18	**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.
19	
20	## Contributions (3 条，明确区分)
21	
22	1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.
23	
24	2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.
25	
26	3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).
27	
28	## Story Spine
29	
30	**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.
31	
32	**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.
33	
34	**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.
35	
36	**Headline result template**: "In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (X-Y%, benchmark-dependent [placeholder: fill after exp-001/002]), while direct infrastructure×methodology interactions are negligible. Variance structure [is/is not] benchmark-conditional [pending exp-002]. D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional."
37	
38	## Hook (Counter-Intuitive Quantified Claim)
39	"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory."
40	
41	## Narrative Strategy
42	- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)
43	- **Tension**: "No universal recipe" — the field seeks standardization but variance structure varies qualitatively across task types
44	- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)
45	- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)
46	- **Figure plan** (4 figures minimum):
47	  1. Problem illustration: same model, different benchmark → different dominant variance source
48	  2. G-theory facet diagram showing crossed design
49	  3. Stacked-bar variance decomposition across benchmarks (signature figure)
50	  4. D-study projection curves: G vs item count for different benchmarks
51	- **Key framing shifts from Dream feedback**:
52	  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty
53	  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient
54	  - Cross-benchmark gradient is the **primary novel finding**
55	  - "Fully crossed" language qualified to MMLU exp-001 only; other benchmarks use reduced designs
56	
57	## Venue Fit Risks
58	- AAAI: Strong fit for "evaluation methodology" track. Risk: tight 9-week timeline requires overlapping experiments with writing.
59	- Reviewer concern 1: "Only open-weight models, not API models" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.
60	- Reviewer concern 2: "G-theory is borrowed methodology, not novel" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.
61	- Reviewer concern 3: "Item dominance is obvious from measurement theory" — Acknowledge explicitly. Contribution is quantification (X-Y%, pending exp-001/002), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.
62	
63	## Anticipated Reviewer Concerns & Planned Responses
64	1. **"Only N GPU types"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to "numerical precision" and frame hardware as future work.
65	2. **"float32 engine confound"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.
66	3. **"Only MMLU"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.
67	4. **"Small item sample"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.
68	5. **"No training-time analysis"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.
69	6. **"Missing scale validation"** → exp-005 (14B models)
70	7. **"G-theory may not be right framework"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.
71	8. **"Separability claim is metric-dependent"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.
72	9. **"FP32 degradation is already known (Yuan 2025)"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.
73	10. **"Incremental over Mesting (2026)"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.
74	11. **"Model not treated as G-theory facet"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.
75	12. **"No CIs on variance components"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.
76	13. **"Missing related work — IRT, tinyBenchmarks, Bouthillier"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.
77	14. **"Diagnostic tool claim unsubstantiated"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as "empirical analysis + data release."
78	15. **"Fine-tuning uses encoder-only RoBERTa"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.
79	
80	## Design Decisions
81	- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.
82	- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.
83	- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.
84	- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.
85	- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.
86	- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as "reduced crossing" rather than "fully crossed."
87	
88	## Required Bibliography (minimum 25 references)
89	Key references to include beyond current literature_map:
90	- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA
91	- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP
92	- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP
93	- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling
94	- Perlitz et al. (2023) — Efficient LLM benchmarking
95	- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition
96	- Shavelson & Webb (1991) — G-theory primer (canonical)
97	- Brennan (2001) — G-theory textbook (canonical)
98	- Lu et al. (2022) — Option ordering effects in MC evaluation
99	- Pezeshkpour & Hruschka (2024) — Option ordering effects
100	- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)
101	- Sellam et al. (2022) — MultiBERTs, multi-seed training
102	- Dehghani et al. (2021) — Benchmark Lottery
103	- Biderman et al. (2024) — Evaluation reproducibility lessons
104	- Vania et al. (2021) — IRT item properties in NLP
105	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15efc705-f2a8-4065-99aa-eccf6c6dd08c",
  "isSidechain": false,
  "promptId": "e7f4bce4-3601-4156-9c94-fdbb9b592014",
  "type": "user",
  "uuid": "3bd1e42c-1ea3-4717-91c5-41ca7f6a4a59",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/paper_framing.md",
      "content": "# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation (MVP: 58.4% on MMLU single-model; expected to decrease with model-as-facet reanalysis). Its magnitude is hypothesized to be benchmark-dependent — weakening on reasoning tasks where temperature/seed interactions increase — but this gradient requires exp-002 confirmation. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating whether a systematic benchmark-dependent gradient exists, and (c) deriving D-study implications specific to LLM evaluation.\n**Fallback narratives**: (A) If gradient confirmed → \"benchmark-conditional variance structure\"; (B) If gradient not significant → \"item dominance is universal but magnitude varies\"; (C) If model-as-facet reduces item_id below 30% → pivot to \"model×item interaction is the dominant source\" — narrative direction changes substantially.\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \"infrastructure\" is currently limited to the precision facet.\n\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.\n\n## Contributions (3 条，明确区分)\n\n1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.\n\n2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.\n\n3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\n\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\n\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\n\n**Headline result template**: \"In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (X-Y%, benchmark-dependent [placeholder: fill after exp-001/002]), while direct infrastructure×methodology interactions are negligible. Variance structure [is/is not] benchmark-conditional [pending exp-002]. D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\n- **Tension**: \"No universal recipe\" — the field seeks standardization but variance structure varies qualitatively across task types\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\n- **Figure plan** (4 figures minimum):\n  1. Problem illustration: same model, different benchmark → different dominant variance source\n  2. G-theory facet diagram showing crossed design\n  3. Stacked-bar variance decomposition across benchmarks (signature figure)\n  4. D-study projection curves: G vs item count for different benchmarks\n- **Key framing shifts from Dream feedback**:\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\n  - Cross-benchmark gradient is the **primary novel finding**\n  - \"Fully crossed\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious from measurement theory\" — Acknowledge explicitly. Contribution is quantification (X-Y%, pending exp-001/002), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \"numerical precision\" and frame hardware as future work.\n2. **\"float32 engine confound\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\n8. **\"Separability claim is metric-dependent\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\n9. **\"FP32 degradation is already known (Yuan 2025)\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\n10. **\"Incremental over Mesting (2026)\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\n11. **\"Model not treated as G-theory facet\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\n12. **\"No CIs on variance components\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\n13. **\"Missing related work — IRT, tinyBenchmarks, Bouthillier\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\n14. **\"Diagnostic tool claim unsubstantiated\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \"empirical analysis + data release.\"\n15. **\"Fine-tuning uses encoder-only RoBERTa\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"\n\n## Required Bibliography (minimum 25 references)\nKey references to include beyond current literature_map:\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\n- Perlitz et al. (2023) — Efficient LLM benchmarking\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\n- Shavelson & Webb (1991) — G-theory primer (canonical)\n- Brennan (2001) — G-theory textbook (canonical)\n- Lu et al. (2022) — Option ordering effects in MC evaluation\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\n- Dehghani et al. (2021) — Benchmark Lottery\n- Biderman et al. (2024) — Evaluation reproducibility lessons\n- Vania et al. (2021) — IRT item properties in NLP\n",
      "numLines": 105,
      "startLine": 1,
      "totalLines": 105
    }
  },
  "sourceToolAssistantUUID": "15efc705-f2a8-4065-99aa-eccf6c6dd08c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Runtime record

_source line 1327 · 2026-05-21T03:19:38.670Z_

```json
{
  "parentUuid": "3bd1e42c-1ea3-4717-91c5-41ca7f6a4a59",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8f24dbc4-f9b6-4f78-8d2d-d2ae19e92a79",
  "timestamp": "2026-05-21T03:19:38.670Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

---


### Runtime record

_source line 1328_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[飞书用户 孙震 (ou_12185aa391efc8ff13eea9c848f0ab5a)]: 强力修复这些问题，并想尽办法尝试提升分数",
  "leafUuid": "8f24dbc4-f9b6-4f78-8d2d-d2ae19e92a79",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


### Runtime record

_source line 1329_

```json
{
  "type": "ai-title",
  "aiTitle": "Bootstrap NLP variance G-theory MVP",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


### Tool call

_source line 1330 · 2026-05-21T03:19:42.626Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VCQ8uSkE3FW5j6wiXoUTJW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/paper_framing.md",
  "offset": 105
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f24dbc4-f9b6-4f78-8d2d-d2ae19e92a79",
  "isSidechain": false,
  "requestId": "req_011CbEzXMXYY2961ihhCEB3A",
  "type": "assistant",
  "uuid": "f13d4cbb-3247-41a9-ad8d-368306cea9f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oRmqTuLdr7TxZvkqstzcD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3913,
      "cache_read_input_tokens": 108138,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 108138,
          "cache_creation_input_tokens": 3913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3913
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1331 · 2026-05-21T03:19:42.631Z_

<details><summary>↩ Tool result · `toolu_01VCQ8uSkE3FW5j6wiXoUTJW`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (105). The file has 105 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f13d4cbb-3247-41a9-ad8d-368306cea9f2",
  "isSidechain": false,
  "promptId": "e7f4bce4-3601-4156-9c94-fdbb9b592014",
  "type": "user",
  "uuid": "7fc40fa7-112d-4a05-baae-53bc8cd26685",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/paper_framing.md",
      "content": "",
      "numLines": 1,
      "startLine": 105,
      "totalLines": 105
    }
  },
  "sourceToolAssistantUUID": "f13d4cbb-3247-41a9-ad8d-368306cea9f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Assistant

_source line 1332 · 2026-05-21T03:19:51.787Z_

<details><summary>Logged reasoning block</summary>

```text
OK, the paper_framing.md is 105 lines. I need to add sections addressing the Dream review issues. Let me add:

1. Binary data limitation discussion plan
2. Fixed vs random sensitivity analysis plan
3. Separability claim qualification
4. D-study optimization documentation requirement
5. G-coefficient interpretation clarification
6. Additional anticipated reviewer concerns from Dream #2

Let me also update the experiment_plan.yaml to add the new analysis tasks to exp-004.

Let me edit paper_framing.md to add these critical items.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fc40fa7-112d-4a05-baae-53bc8cd26685",
  "isSidechain": false,
  "requestId": "req_011CbEzXebTaKKD7vm6qoFiG",
  "type": "assistant",
  "uuid": "b639a692-1ff6-4a7d-8b34-cfffa239522d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NKFR2no6YGJYBqpLKKhyWD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 146,
      "cache_read_input_tokens": 112051,
      "output_tokens": 1971,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1971,
          "cache_read_input_tokens": 112051,
          "cache_creation_input_tokens": 146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 146
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 1333 · 2026-05-21T03:20:27.663Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01MeEAyPMh3vmk5yc54STtkL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/paper_framing.md",
  "old_string": "## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"",
  "new_string": "## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"\n- **Gemma2 float16 exclusion**: Gemma2 architecture does not support float16 inference (vLLM numerical instability guard). Cross-model analysis uses bf16+fp32 (balanced). fp16 data from Llama/Mistral/Qwen used in within-model analyses. bf16≈fp16 difference <0.1pp (D005).\n\n## Methodological Defenses (Dream #2 审稿问题逐条应对)\n\n### MD1. Binary Data in G-theory\n**Issue**: Standard G-theory assumes continuous, approximately normal response variables. Binary 0/1 data violates this; item variance is mechanically linked to item difficulty via Bernoulli p(1-p).\n**Defense strategy**: (a) Report correlation between Bernoulli variance p_i(1-p_i) and observed item variance — quantify how much item_id is \"mechanical\" vs informative; (b) Run parallel analysis on text_exact_match (continuous metric) to show variance structure is robust across metrics; (c) Discuss generalized G-theory (Brennan 2001 Ch.12) in Limitations; (d) Cite Lalor et al. (2019) who used IRT (also assumes latent continuous) on binary NLP data without this criticism being fatal.\n\n### MD2. Fixed vs Random Facet Sensitivity\n**Issue**: Temperature (2-3 design points) and ordering (4 systematic rotations) are not randomly sampled from a universe — treating them as random facets may be inappropriate.\n**Defense strategy**: Run sensitivity analysis with temperature and ordering as fixed facets. If variance decomposition changes <5%, report as robust. If substantial, discuss implications and present both analyses. This directly addresses Reviewer concern.\n\n### MD3. Separability Claim Scope\n**Issue**: Separability (<0.3%) holds for knowledge benchmarks but not reasoning tasks (GSM8K=3.0%, MATH=2.5%).\n**Defense**: Qualify all separability claims as \"under binary scoring on knowledge-retrieval benchmarks.\" Present benchmark-conditional separability as a finding (not a limitation): \"separability itself varies across task types.\"\n\n### MD4. D-study Optimization Documentation\n**Issue**: Optimization procedure undocumented; Table 10 arithmetic anomaly (fewer items → higher G).\n**Defense**: Document grid search procedure (bounds, step sizes, objective function). Verify and explain any non-monotonicity (likely due to joint optimization across facets where reallocating item budget to prompt/seed is more efficient).\n\n### MD5. G-coefficient Interpretation\n**Issue**: G=0.22 for 200 items ≠ \"MMLU is unreliable\" (standard MMLU uses ~14K items).\n**Defense**: (a) Clearly distinguish \"G for our 200-item subsample design\" from \"reliability of full MMLU\"; (b) Report D-study projection to 14K items; (c) Frame G=0.22 as \"cost of subsampling\" rather than \"MMLU is broken.\"\n\n### MD6. Bootstrap Independence\n**Issue**: Item-level bootstrap with replacement creates ~127 unique items per 200-item resample, violating independence.\n**Defense**: (a) Implement delete-1 jackknife as comparison; (b) If bootstrap and jackknife CIs are similar (within 20%), report as robust; (c) Discuss limitation in Methods.\n\n### MD7. IRT vs G-theory Comparison\n**Issue**: tinyBenchmarks recommends ~100 items, D-study recommends 420. 4× discrepancy unexplained.\n**Defense**: Direct comparison showing G-theory accounts for prompt/seed/ordering dimensions that IRT ignores. The 4× difference is the \"cost of multi-facet reliability\" — G-theory's budget is larger because it targets reliability across ALL facets, not just items. This comparison is a potential standalone contribution.\n\n### MD8. Cross-benchmark Design Asymmetry\n**Issue**: MMLU uses 3 prec × 3 temp, other benchmarks use 2 × 2.\n**Defense**: Re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7) and compare variance decomposition. If <5% change, report as robust to design reduction.\n\n### MD9. Title-Content Alignment\n**Issue**: Title promises \"Evaluation Metrics\" but logprob analysis is minimal.\n**Defense**: Expand logprob analysis across all benchmarks in exp-004, OR adjust title to \"...Across Benchmarks and Models.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b639a692-1ff6-4a7d-8b34-cfffa239522d",
  "isSidechain": false,
  "requestId": "req_011CbEzXebTaKKD7vm6qoFiG",
  "type": "assistant",
  "uuid": "741eefc7-7179-4f2f-b777-122a94528285",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NKFR2no6YGJYBqpLKKhyWD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 146,
      "cache_read_input_tokens": 112051,
      "output_tokens": 1971,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1971,
          "cache_read_input_tokens": 112051,
          "cache_creation_input_tokens": 146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 146
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1334 · 2026-05-21T03:20:27.693Z_

<details><summary>↩ Tool result · `toolu_01MeEAyPMh3vmk5yc54STtkL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "741eefc7-7179-4f2f-b777-122a94528285",
  "isSidechain": false,
  "promptId": "e7f4bce4-3601-4156-9c94-fdbb9b592014",
  "type": "user",
  "uuid": "3996f393-d184-4e05-86d8-6ca7b20392a3",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/paper_framing.md",
    "oldString": "## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"",
    "newString": "## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"\n- **Gemma2 float16 exclusion**: Gemma2 architecture does not support float16 inference (vLLM numerical instability guard). Cross-model analysis uses bf16+fp32 (balanced). fp16 data from Llama/Mistral/Qwen used in within-model analyses. bf16≈fp16 difference <0.1pp (D005).\n\n## Methodological Defenses (Dream #2 审稿问题逐条应对)\n\n### MD1. Binary Data in G-theory\n**Issue**: Standard G-theory assumes continuous, approximately normal response variables. Binary 0/1 data violates this; item variance is mechanically linked to item difficulty via Bernoulli p(1-p).\n**Defense strategy**: (a) Report correlation between Bernoulli variance p_i(1-p_i) and observed item variance — quantify how much item_id is \"mechanical\" vs informative; (b) Run parallel analysis on text_exact_match (continuous metric) to show variance structure is robust across metrics; (c) Discuss generalized G-theory (Brennan 2001 Ch.12) in Limitations; (d) Cite Lalor et al. (2019) who used IRT (also assumes latent continuous) on binary NLP data without this criticism being fatal.\n\n### MD2. Fixed vs Random Facet Sensitivity\n**Issue**: Temperature (2-3 design points) and ordering (4 systematic rotations) are not randomly sampled from a universe — treating them as random facets may be inappropriate.\n**Defense strategy**: Run sensitivity analysis with temperature and ordering as fixed facets. If variance decomposition changes <5%, report as robust. If substantial, discuss implications and present both analyses. This directly addresses Reviewer concern.\n\n### MD3. Separability Claim Scope\n**Issue**: Separability (<0.3%) holds for knowledge benchmarks but not reasoning tasks (GSM8K=3.0%, MATH=2.5%).\n**Defense**: Qualify all separability claims as \"under binary scoring on knowledge-retrieval benchmarks.\" Present benchmark-conditional separability as a finding (not a limitation): \"separability itself varies across task types.\"\n\n### MD4. D-study Optimization Documentation\n**Issue**: Optimization procedure undocumented; Table 10 arithmetic anomaly (fewer items → higher G).\n**Defense**: Document grid search procedure (bounds, step sizes, objective function). Verify and explain any non-monotonicity (likely due to joint optimization across facets where reallocating item budget to prompt/seed is more efficient).\n\n### MD5. G-coefficient Interpretation\n**Issue**: G=0.22 for 200 items ≠ \"MMLU is unreliable\" (standard MMLU uses ~14K items).\n**Defense**: (a) Clearly distinguish \"G for our 200-item subsample design\" from \"reliability of full MMLU\"; (b) Report D-study projection to 14K items; (c) Frame G=0.22 as \"cost of subsampling\" rather than \"MMLU is broken.\"\n\n### MD6. Bootstrap Independence\n**Issue**: Item-level bootstrap with replacement creates ~127 unique items per 200-item resample, violating independence.\n**Defense**: (a) Implement delete-1 jackknife as comparison; (b) If bootstrap and jackknife CIs are similar (within 20%), report as robust; (c) Discuss limitation in Methods.\n\n### MD7. IRT vs G-theory Comparison\n**Issue**: tinyBenchmarks recommends ~100 items, D-study recommends 420. 4× discrepancy unexplained.\n**Defense**: Direct comparison showing G-theory accounts for prompt/seed/ordering dimensions that IRT ignores. The 4× difference is the \"cost of multi-facet reliability\" — G-theory's budget is larger because it targets reliability across ALL facets, not just items. This comparison is a potential standalone contribution.\n\n### MD8. Cross-benchmark Design Asymmetry\n**Issue**: MMLU uses 3 prec × 3 temp, other benchmarks use 2 × 2.\n**Defense**: Re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7) and compare variance decomposition. If <5% change, report as robust to design reduction.\n\n### MD9. Title-Content Alignment\n**Issue**: Title promises \"Evaluation Metrics\" but logprob analysis is minimal.\n**Defense**: Expand logprob analysis across all benchmarks in exp-004, OR adjust title to \"...Across Benchmarks and Models.\"",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 84,
        "oldLines": 7,
        "newStart": 84,
        "newLines": 46,
        "lines": [
          " - **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.",
          " - **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.",
          " - **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"",
          "+- **Gemma2 float16 exclusion**: Gemma2 architecture does not support float16 inference (vLLM numerical instability guard). Cross-model analysis uses bf16+fp32 (balanced). fp16 data from Llama/Mistral/Qwen used in within-model analyses. bf16≈fp16 difference <0.1pp (D005).",
          " ",
          "+## Methodological Defenses (Dream #2 审稿问题逐条应对)",
          "+",
          "+### MD1. Binary Data in G-theory",
          "+**Issue**: Standard G-theory assumes continuous, approximately normal response variables. Binary 0/1 data violates this; item variance is mechanically linked to item difficulty via Bernoulli p(1-p).",
          "+**Defense strategy**: (a) Report correlation between Bernoulli variance p_i(1-p_i) and observed item variance — quantify how much item_id is \"mechanical\" vs informative; (b) Run parallel analysis on text_exact_match (continuous metric) to show variance structure is robust across metrics; (c) Discuss generalized G-theory (Brennan 2001 Ch.12) in Limitations; (d) Cite Lalor et al. (2019) who used IRT (also assumes latent continuous) on binary NLP data without this criticism being fatal.",
          "+",
          "+### MD2. Fixed vs Random Facet Sensitivity",
          "+**Issue**: Temperature (2-3 design points) and ordering (4 systematic rotations) are not randomly sampled from a universe — treating them as random facets may be inappropriate.",
          "+**Defense strategy**: Run sensitivity analysis with temperature and ordering as fixed facets. If variance decomposition changes <5%, report as robust. If substantial, discuss implications and present both analyses. This directly addresses Reviewer concern.",
          "+",
          "+### MD3. Separability Claim Scope",
          "+**Issue**: Separability (<0.3%) holds for knowledge benchmarks but not reasoning tasks (GSM8K=3.0%, MATH=2.5%).",
          "+**Defense**: Qualify all separability claims as \"under binary scoring on knowledge-retrieval benchmarks.\" Present benchmark-conditional separability as a finding (not a limitation): \"separability itself varies across task types.\"",
          "+",
          "+### MD4. D-study Optimization Documentation",
          "+**Issue**: Optimization procedure undocumented; Table 10 arithmetic anomaly (fewer items → higher G).",
          "+**Defense**: Document grid search procedure (bounds, step sizes, objective function). Verify and explain any non-monotonicity (likely due to joint optimization across facets where reallocating item budget to prompt/seed is more efficient).",
          "+",
          "+### MD5. G-coefficient Interpretation",
          "+**Issue**: G=0.22 for 200 items ≠ \"MMLU is unreliable\" (standard MMLU uses ~14K items).",
          "+**Defense**: (a) Clearly distinguish \"G for our 200-item subsample design\" from \"reliability of full MMLU\"; (b) Report D-study projection to 14K items; (c) Frame G=0.22 as \"cost of subsampling\" rather than \"MMLU is broken.\"",
          "+",
          "+### MD6. Bootstrap Independence",
          "+**Issue**: Item-level bootstrap with replacement creates ~127 unique items per 200-item resample, violating independence.",
          "+**Defense**: (a) Implement delete-1 jackknife as comparison; (b) If bootstrap and jackknife CIs are similar (within 20%), report as robust; (c) Discuss limitation in Methods.",
          "+",
          "+### MD7. IRT vs G-theory Comparison",
          "+**Issue**: tinyBenchmarks recommends ~100 items, D-study recommends 420. 4× discrepancy unexplained.",
          "+**Defense**: Direct comparison showing G-theory accounts for prompt/seed/ordering dimensions that IRT ignores. The 4× difference is the \"cost of multi-facet reliability\" — G-theory's budget is larger because it targets reliability across ALL facets, not just items. This comparison is a potential standalone contribution.",
          "+",
          "+### MD8. Cross-benchmark Design Asymmetry",
          "+**Issue**: MMLU uses 3 prec × 3 temp, other benchmarks use 2 × 2.",
          "+**Defense**: Re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7) and compare variance decomposition. If <5% change, report as robust to design reduction.",
          "+",
          "+### MD9. Title-Content Alignment",
          "+**Issue**: Title promises \"Evaluation Metrics\" but logprob analysis is minimal.",
          "+**Defense**: Expand logprob analysis across all benchmarks in exp-004, OR adjust title to \"...Across Benchmarks and Models.\"",
          "+",
          " ## Required Bibliography (minimum 25 references)",
          " Key references to include beyond current literature_map:",
          " - Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "741eefc7-7179-4f2f-b777-122a94528285",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Assistant

_source line 1335 · 2026-05-21T03:20:30.681Z_

现在更新 experiment_plan.yaml，把新增的分析任务加到 exp-004。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3996f393-d184-4e05-86d8-6ca7b20392a3",
  "isSidechain": false,
  "requestId": "req_011CbEzaxstBjYn8rQ6TKdyc",
  "type": "assistant",
  "uuid": "aa46fbc5-c679-42bc-be75-cf51267fa230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015w1GHVFEdXuXYiJ4pKNYUf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2041,
      "cache_read_input_tokens": 112197,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2041,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 112197,
          "cache_creation_input_tokens": 2041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2041
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 1336 · 2026-05-21T03:20:31.346Z_

<details open><summary>🔧 Tool call — Read · `toolu_01347i8TWoLioMY6JQJRY9Ru`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/experiment_plan.yaml",
  "offset": 55,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa46fbc5-c679-42bc-be75-cf51267fa230",
  "isSidechain": false,
  "requestId": "req_011CbEzaxstBjYn8rQ6TKdyc",
  "type": "assistant",
  "uuid": "2524956d-ccdf-4e04-8b1c-006b13e1ec95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015w1GHVFEdXuXYiJ4pKNYUf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2041,
      "cache_read_input_tokens": 112197,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2041,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 112197,
          "cache_creation_input_tokens": 2041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2041
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1337 · 2026-05-21T03:20:31.351Z_

<details><summary>↩ Tool result · `toolu_01347i8TWoLioMY6JQJRY9Ru`</summary>

```text
55	    deps: []  # independent, can run as soon as second GPU available
56	    status: blocked  # waiting for second GPU type
57	
58	  - id: exp-004
59	    claim: 3  # D-study reproducibility budget
60	    description: >
61	      Comprehensive analysis of combined exp-001/001b/002/003 data. Includes:
62	      (a) Model-as-facet G-theory reanalysis — treat model as crossed random facet to properly
63	      attribute model×item interaction and reduce inflated item_id/residual (Dream critical);
64	      (b) Bootstrap CIs (1000 resamples) on ALL variance components in ALL tables, especially
65	      direct infra×method interaction term (Dream critical);
66	      (c) D-study projections with CIs for optimal allocation across facets for G≥0.90/0.95/0.99,
67	      with benchmark-specific budgets and comparison to IRT-based subsampling (tinyBenchmarks);
68	      (d) REML vs Henderson Method I comparison as sensitivity analysis;
69	      (e) Logprob-based scoring as third response variable;
70	      (f) Ranking stability analysis — does precision×temperature interaction alter model rankings?
71	      (g) Higher-order interaction estimation to decompose the residual component;
72	      (h) G-theory vs IRT direct comparison — same MMLU data, D-study vs tinyBenchmarks IRT
73	      subsampling, compare recommended item counts and discuss why G-theory is more conservative
74	      (accounts for prompt/seed dimensions IRT ignores). First direct comparison in the literature;
75	      (i) Power analysis — verify statistical power to detect ≥X% interaction effects given
76	      5184×200 design scale, preempt "underpowered" reviewer concern;
77	      (j) Practitioner evaluation protocol guide (Discussion/Appendix).
78	    priority: P0
79	    gpu_budget_hours: 0  # pure analysis, no GPU
80	    hardware: none
81	    deps: [exp-001, exp-002, exp-003]
82	    status: planned
83	
84	  # === P1: Important for paper strength ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2524956d-ccdf-4e04-8b1c-006b13e1ec95",
  "isSidechain": false,
  "promptId": "e7f4bce4-3601-4156-9c94-fdbb9b592014",
  "type": "user",
  "uuid": "96e2490d-4158-4fce-87b6-542736c153cb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/experiment_plan.yaml",
      "content": "    deps: []  # independent, can run as soon as second GPU available\n    status: blocked  # waiting for second GPU type\n\n  - id: exp-004\n    claim: 3  # D-study reproducibility budget\n    description: >\n      Comprehensive analysis of combined exp-001/001b/002/003 data. Includes:\n      (a) Model-as-facet G-theory reanalysis — treat model as crossed random facet to properly\n      attribute model×item interaction and reduce inflated item_id/residual (Dream critical);\n      (b) Bootstrap CIs (1000 resamples) on ALL variance components in ALL tables, especially\n      direct infra×method interaction term (Dream critical);\n      (c) D-study projections with CIs for optimal allocation across facets for G≥0.90/0.95/0.99,\n      with benchmark-specific budgets and comparison to IRT-based subsampling (tinyBenchmarks);\n      (d) REML vs Henderson Method I comparison as sensitivity analysis;\n      (e) Logprob-based scoring as third response variable;\n      (f) Ranking stability analysis — does precision×temperature interaction alter model rankings?\n      (g) Higher-order interaction estimation to decompose the residual component;\n      (h) G-theory vs IRT direct comparison — same MMLU data, D-study vs tinyBenchmarks IRT\n      subsampling, compare recommended item counts and discuss why G-theory is more conservative\n      (accounts for prompt/seed dimensions IRT ignores). First direct comparison in the literature;\n      (i) Power analysis — verify statistical power to detect ≥X% interaction effects given\n      5184×200 design scale, preempt \"underpowered\" reviewer concern;\n      (j) Practitioner evaluation protocol guide (Discussion/Appendix).\n    priority: P0\n    gpu_budget_hours: 0  # pure analysis, no GPU\n    hardware: none\n    deps: [exp-001, exp-002, exp-003]\n    status: planned\n\n  # === P1: Important for paper strength ===",
      "numLines": 30,
      "startLine": 55,
      "totalLines": 154
    }
  },
  "sourceToolAssistantUUID": "2524956d-ccdf-4e04-8b1c-006b13e1ec95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Runtime record

_source line 1338_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[飞书用户 孙震 (ou_12185aa391efc8ff13eea9c848f0ab5a)]: 强力修复这些问题，并想尽办法尝试提升分数",
  "leafUuid": "96e2490d-4158-4fce-87b6-542736c153cb",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


### Runtime record

_source line 1339_

```json
{
  "type": "ai-title",
  "aiTitle": "Bootstrap NLP variance G-theory MVP",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


### Tool call

_source line 1340 · 2026-05-21T03:20:41.901Z_

<details open><summary>🔧 Tool call — Edit · `toolu_016FFJ4MwufaT6YkLSEubZvn`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/experiment_plan.yaml",
  "old_string": "      (j) Practitioner evaluation protocol guide (Discussion/Appendix).\n    priority: P0\n    gpu_budget_hours: 0  # pure analysis, no GPU\n    hardware: none\n    deps: [exp-001, exp-002, exp-003]\n    status: planned",
  "new_string": "      (j) Practitioner evaluation protocol guide (Discussion/Appendix);\n      (k) Fixed vs random sensitivity — rerun G-study with temperature/ordering as fixed facets,\n      compare variance decomposition (MD2 defense);\n      (l) Binary data limitation analysis — correlate Bernoulli p(1-p) with observed item variance,\n      parallel binary vs text_exact_match analysis (MD1 defense);\n      (m) Bootstrap vs jackknife CI comparison — delete-1 jackknife as independence-safe alternative,\n      compare CI widths (MD6 defense);\n      (n) Cross-benchmark design asymmetry sensitivity — re-analyze MMLU with matched 2×2 design\n      (bf16/fp16 × T=0.0/T=0.7), compare with full 3×3 (MD8 defense);\n      (o) G-coefficient at full benchmark size — D-study projection to 14K MMLU items (MD5 defense);\n      (p) Logprob-based scoring across all benchmarks — expand from MMLU-only to all 5 benchmarks,\n      support \"Evaluation Metrics\" in title (MD9 defense);\n      (q) GPU cost analysis — estimate compute cost for recommended D-study budgets.\n    priority: P0\n    gpu_budget_hours: 0  # pure analysis, no GPU\n    hardware: none\n    deps: [exp-001, exp-002, exp-003]\n    status: planned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96e2490d-4158-4fce-87b6-542736c153cb",
  "isSidechain": false,
  "requestId": "req_011CbEzbEkruycx8nVwcEEbX",
  "type": "assistant",
  "uuid": "16dfb8ac-070b-45fa-9771-ac32dcdb31a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEwR4c6D97jFAfYJvCjtXU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 711,
      "cache_read_input_tokens": 114238,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 711,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 557,
          "cache_read_input_tokens": 114238,
          "cache_creation_input_tokens": 711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 711
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-21T03:20:41.913Z_

<details><summary>↩ Tool result · `toolu_016FFJ4MwufaT6YkLSEubZvn`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16dfb8ac-070b-45fa-9771-ac32dcdb31a7",
  "isSidechain": false,
  "promptId": "e7f4bce4-3601-4156-9c94-fdbb9b592014",
  "type": "user",
  "uuid": "cf5f80df-e940-4c2f-a982-4759387911a8",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/experiment_plan.yaml",
    "oldString": "      (j) Practitioner evaluation protocol guide (Discussion/Appendix).\n    priority: P0\n    gpu_budget_hours: 0  # pure analysis, no GPU\n    hardware: none\n    deps: [exp-001, exp-002, exp-003]\n    status: planned",
    "newString": "      (j) Practitioner evaluation protocol guide (Discussion/Appendix);\n      (k) Fixed vs random sensitivity — rerun G-study with temperature/ordering as fixed facets,\n      compare variance decomposition (MD2 defense);\n      (l) Binary data limitation analysis — correlate Bernoulli p(1-p) with observed item variance,\n      parallel binary vs text_exact_match analysis (MD1 defense);\n      (m) Bootstrap vs jackknife CI comparison — delete-1 jackknife as independence-safe alternative,\n      compare CI widths (MD6 defense);\n      (n) Cross-benchmark design asymmetry sensitivity — re-analyze MMLU with matched 2×2 design\n      (bf16/fp16 × T=0.0/T=0.7), compare with full 3×3 (MD8 defense);\n      (o) G-coefficient at full benchmark size — D-study projection to 14K MMLU items (MD5 defense);\n      (p) Logprob-based scoring across all benchmarks — expand from MMLU-only to all 5 benchmarks,\n      support \"Evaluation Metrics\" in title (MD9 defense);\n      (q) GPU cost analysis — estimate compute cost for recommended D-study budgets.\n    priority: P0\n    gpu_budget_hours: 0  # pure analysis, no GPU\n    hardware: none\n    deps: [exp-001, exp-002, exp-003]\n    status: planned",
    "originalFile": "experiments:\n  # === P0: Must-run for paper submission ===\n\n  - id: exp-001\n    claim: 1  # Item dominance at scale\n    description: >\n      Full-scale precision study: 4 models (Qwen3-8B, Llama-3.1-8B-Instruct, Gemma-2-9B-IT, Mistral-7B-Instruct-v0.3)\n      × 3 precisions (FP32, BF16, FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings\n      × 200 MMLU items (stratified). All precisions use consistent vLLM engine (V0 enforce_eager)\n      to eliminate the float32 engine confound found in MVP. Validates item dominance finding at\n      scale and with multiple models.\n    priority: P0\n    gpu_budget_hours: 100\n    hardware: westd-32570 (RTX PRO 6000 96GB)\n    deps: []\n    status: planned\n\n  - id: exp-001b\n    claim: 1  # Item dominance stability across item samples\n    description: >\n      Item resampling stability test: 3 independent stratified samples of 200 MMLU items\n      (seeds 0, 7, 99) × 1 model (Llama-3.1-8B-Instruct) × 3 precisions × 3 prompts\n      × 3 seeds × 2 orderings = 54 conditions per sample. Tests whether the 58% item\n      dominance finding is stable across different item draws from MMLU, not an artifact\n      of the specific 200-item sample. Critical for defending the headline claim.\n    priority: P0\n    gpu_budget_hours: 15\n    hardware: westd-32570\n    deps: [exp-001]  # reuses exp-001 pipeline, runs after main study\n    status: planned\n\n  - id: exp-002\n    claim: 1  # Item dominance generalizes across benchmarks\n    description: >\n      Multi-benchmark replication: same 4 models × BF16/FP16 × 6 prompts × 6 seeds\n      × 2 temperatures × 4 orderings on GSM8K (200 items), ARC-Challenge (200 items),\n      HellaSwag (200 items). Tests whether item dominance and separability hold across\n      task types (math reasoning, science reasoning, commonsense).\n    priority: P0\n    gpu_budget_hours: 200\n    hardware: westd-32570\n    deps: [exp-001]  # need analysis pipeline validated first\n    status: planned\n\n  - id: exp-003\n    claim: 2  # Separability with hardware factor\n    description: >\n      Multi-hardware G-study: 4 models × 2+ GPU types × 2 precisions (BF16, FP16)\n      × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items.\n      Tests hardware × methodology interaction — the core separability question\n      that MVP couldn't address with only 1 GPU type.\n    priority: P0\n    gpu_budget_hours: 120\n    hardware: westd-32570 + TBD (second GPU type from Manager)\n    deps: []  # independent, can run as soon as second GPU available\n    status: blocked  # waiting for second GPU type\n\n  - id: exp-004\n    claim: 3  # D-study reproducibility budget\n    description: >\n      Comprehensive analysis of combined exp-001/001b/002/003 data. Includes:\n      (a) Model-as-facet G-theory reanalysis — treat model as crossed random facet to properly\n      attribute model×item interaction and reduce inflated item_id/residual (Dream critical);\n      (b) Bootstrap CIs (1000 resamples) on ALL variance components in ALL tables, especially\n      direct infra×method interaction term (Dream critical);\n      (c) D-study projections with CIs for optimal allocation across facets for G≥0.90/0.95/0.99,\n      with benchmark-specific budgets and comparison to IRT-based subsampling (tinyBenchmarks);\n      (d) REML vs Henderson Method I comparison as sensitivity analysis;\n      (e) Logprob-based scoring as third response variable;\n      (f) Ranking stability analysis — does precision×temperature interaction alter model rankings?\n      (g) Higher-order interaction estimation to decompose the residual component;\n      (h) G-theory vs IRT direct comparison — same MMLU data, D-study vs tinyBenchmarks IRT\n      subsampling, compare recommended item counts and discuss why G-theory is more conservative\n      (accounts for prompt/seed dimensions IRT ignores). First direct comparison in the literature;\n      (i) Power analysis — verify statistical power to detect ≥X% interaction effects given\n      5184×200 design scale, preempt \"underpowered\" reviewer concern;\n      (j) Practitioner evaluation protocol guide (Discussion/Appendix).\n    priority: P0\n    gpu_budget_hours: 0  # pure analysis, no GPU\n    hardware: none\n    deps: [exp-001, exp-002, exp-003]\n    status: planned\n\n  # === P1: Important for paper strength ===\n\n  - id: exp-005\n    claim: 2  # Scale validation\n    description: >\n      14B model extension: Qwen3-14B and DeepSeek-R1-Distill-14B on datacenter GPUs\n      at BF16/FP16. Tests whether variance attribution patterns change with model scale\n      and architecture (dense vs reasoning-distilled).\n    priority: P1\n    gpu_budget_hours: 100\n    hardware: TBD (needs ≥48GB VRAM per GPU)\n    deps: [exp-003]\n    status: planned\n\n  - id: exp-006\n    claim: 2  # Training-time variance\n    description: >\n      Fine-tuning G-study: RoBERTa-large on SST-2/MNLI/RTE/COPA.\n      Fully crossed: 6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions\n      = 432 runs/task × 4 tasks = 1,728 total fine-tuning runs.\n      Validates whether variance hierarchy differs between inference and fine-tuning.\n    priority: P1\n    gpu_budget_hours: 200\n    hardware: westd-32570 (RoBERTa-large fits easily on 96GB)\n    deps: []\n    status: planned\n\n  # === P2: Nice-to-have ===\n\n  - id: exp-007\n    claim: 2  # LayerCast mitigation\n    description: >\n      Test LayerCast (FP16 storage + FP32 compute) as additional precision condition\n      on MMLU. Quantifies variance reduction from this mitigation strategy.\n    priority: P2\n    gpu_budget_hours: 30\n    hardware: westd-32570\n    deps: [exp-001]\n    status: planned\n\n  - id: exp-008\n    claim: 1  # Reasoning benchmark extension\n    description: >\n      MATH benchmark (200 items) — tests whether item dominance pattern differs\n      for reasoning-heavy tasks where chain-of-thought introduces additional variance.\n    priority: P2\n    gpu_budget_hours: 50\n    hardware: westd-32570\n    deps: [exp-002]\n    status: planned\n\n# MVP experiment (completed)\nmvp:\n  - id: mvp-001\n    registry_id: null  # MVP was run directly, not through registry\n    description: >\n      MVP Phase A: 1 model (Llama-3.1-8B) × 1 hardware (RTX PRO 6000) × 3 precisions\n      × 3 prompts × 3 seeds × 2 temps × 2 orderings = 108 conditions × 50 MMLU items.\n    result: >\n      PASS. item_id=58.4%, precision×item=7.2%, temp×item=6.9%, prompt×item=5.7%.\n      Direct precision×methodology <0.02%. G=0.357. float32 engine confound identified.\n    status: completed\n\n# GPU budget summary\nbudget:\n  P0_total: 435  # exp-001(100) + exp-001b(15) + exp-002(200) + exp-003(120) + exp-004(0)\n  P1_total: 300  # exp-005(100) + exp-006(200)\n  P2_total: 80   # exp-007(30) + exp-008(50)\n  grand_total: 815\n  available: \"4× RTX PRO 6000 96GB (westd-32570) + TBD second GPU type\"\n",
    "structuredPatch": [
      {
        "oldStart": 74,
        "oldLines": 7,
        "newStart": 74,
        "newLines": 19,
        "lines": [
          "       (accounts for prompt/seed dimensions IRT ignores). First direct comparison in the literature;",
          "       (i) Power analysis — verify statistical power to detect ≥X% interaction effects given",
          "       5184×200 design scale, preempt \"underpowered\" reviewer concern;",
          "-      (j) Practitioner evaluation protocol guide (Discussion/Appendix).",
          "+      (j) Practitioner evaluation protocol guide (Discussion/Appendix);",
          "+      (k) Fixed vs random sensitivity — rerun G-study with temperature/ordering as fixed facets,",
          "+      compare variance decomposition (MD2 defense);",
          "+      (l) Binary data limitation analysis — correlate Bernoulli p(1-p) with observed item variance,",
          "+      parallel binary vs text_exact_match analysis (MD1 defense);",
          "+      (m) Bootstrap vs jackknife CI comparison — delete-1 jackknife as independence-safe alternative,",
          "+      compare CI widths (MD6 defense);",
          "+      (n) Cross-benchmark design asymmetry sensitivity — re-analyze MMLU with matched 2×2 design",
          "+      (bf16/fp16 × T=0.0/T=0.7), compare with full 3×3 (MD8 defense);",
          "+      (o) G-coefficient at full benchmark size — D-study projection to 14K MMLU items (MD5 defense);",
          "+      (p) Logprob-based scoring across all benchmarks — expand from MMLU-only to all 5 benchmarks,",
          "+      support \"Evaluation Metrics\" in title (MD9 defense);",
          "+      (q) GPU cost analysis — estimate compute cost for recommended D-study budgets.",
          "     priority: P0",
          "     gpu_budget_hours: 0  # pure analysis, no GPU",
          "     hardware: none"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "16dfb8ac-070b-45fa-9771-ac32dcdb31a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Assistant

_source line 1342 · 2026-05-21T03:20:50.233Z_

通知用户进展。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf5f80df-e940-4c2f-a982-4759387911a8",
  "isSidechain": false,
  "requestId": "req_011CbEzc1b85km4fAkWUn45e",
  "type": "assistant",
  "uuid": "24fedd38-3982-4e64-ad5c-a5246441ed09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168FxvT1uSsCn8QmroS3EeY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 114949,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 609,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 538,
          "cache_read_input_tokens": 114949,
          "cache_creation_input_tokens": 609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 609
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 1343 · 2026-05-21T03:21:03.320Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_reply_to_user · `toolu_01XpByko67NqQLDEw6iz41sk`</summary>

```json
{
  "text": "已全面启动修复：\n\n**立即执行（6 个 Worker 并行，不等 GPU）：**\n1. GPU 状态检查 + 下一个模型切换（Gemma fp32 → Mistral）\n2. Llama 单模型全量 G-study 分析（binary + text_exact_match 双 metric）\n3. Fixed vs Random 敏感性分析（温度/ordering 作为固定因子重跑）\n4. Bootstrap vs Jackknife CI 对比（解决独立性问题批评）\n5. 二值数据局限性分析（Bernoulli p(1-p) 相关性 + 双 metric 平行对比）\n6. IRT vs G-theory 直接对比框架（解释 100 vs 420 items 的 4× 差异）\n\n**paper_framing.md 已更新**：新增 9 条 Methodological Defenses（MD1-MD9），逐条对应 Dream 审稿的每个结构性问题，含具体防守策略。\n\n**experiment_plan.yaml 已扩展**：exp-004 新增 7 个子分析（k-q），覆盖所有 Dream reviewers 提出的方法论缺陷。\n\n**推理进度**：Llama ✅ (239K records) → Gemma bf16 ✅ (86K) → Gemma fp32 运行中 → Mistral/Qwen 待切换。2 个模型完成后立即开始 model-as-facet 分析（Claim 1 验证）。\n\n目标：通过主动分析（不是被动辩护）把每个批评点转化为论文的加分项。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24fedd38-3982-4e64-ad5c-a5246441ed09",
  "isSidechain": false,
  "requestId": "req_011CbEzc1b85km4fAkWUn45e",
  "type": "assistant",
  "uuid": "1e2d9768-52c9-4e5f-ad63-c541ca476927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168FxvT1uSsCn8QmroS3EeY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 114949,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 609,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 538,
          "cache_read_input_tokens": 114949,
          "cache_creation_input_tokens": 609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 609
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1344 · 2026-05-21T03:21:04.117Z_

<details><summary>↩ Tool result · `toolu_01XpByko67NqQLDEw6iz41sk`</summary>

```text
{"result":"{\"success\": true}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e2d9768-52c9-4e5f-ad63-c541ca476927",
  "isSidechain": false,
  "promptId": "e7f4bce4-3601-4156-9c94-fdbb9b592014",
  "type": "user",
  "uuid": "44d530ff-2125-4c35-a6a4-4e19a239a488",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true}"
    }
  },
  "sourceToolAssistantUUID": "1e2d9768-52c9-4e5f-ad63-c541ca476927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Runtime record

_source line 1345_

```json
{
  "type": "ai-title",
  "aiTitle": "Bootstrap NLP variance G-theory MVP",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


### Runtime record

_source line 1346 · 2026-05-21T03:22:52.683Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:22:52.683Z",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "content": "[飞书用户 孙震 (ou_12185aa391efc8ff13eea9c848f0ab5a)]: 需要我提供什么吗？"
}
```

---


### Runtime record

_source line 1347 · 2026-05-21T03:22:52.683Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:22:52.683Z",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


## Round 169

## Round 169

2 recorded events


### User

_source line 1348 · 2026-05-21T03:22:52.672Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44d530ff-2125-4c35-a6a4-4e19a239a488",
  "isSidechain": false,
  "promptId": "3b8d4cc7-74a9-47a9-8a1d-0343edadbcc4",
  "type": "user",
  "isMeta": true,
  "uuid": "35107680-e86e-43cf-8477-47fdb7bcac03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Assistant

_source line 1349 · 2026-05-21T03:22:52.672Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35107680-e86e-43cf-8477-47fdb7bcac03",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "15615981-2a4c-4fac-a2bd-332e2c5c1a53",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "id": "3a795b52-3c86-432c-a47a-54c99fe88af8",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 170

## Round 170

6 recorded events


### User

_source line 1350 · 2026-05-21T03:22:52.830Z_

[飞书用户 孙震 (ou_12185aa391efc8ff13eea9c848f0ab5a)]: 需要我提供什么吗？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15615981-2a4c-4fac-a2bd-332e2c5c1a53",
  "isSidechain": false,
  "promptId": "3b8d4cc7-74a9-47a9-8a1d-0343edadbcc4",
  "type": "user",
  "uuid": "5b1c65a2-7fc3-4e88-9c7d-f8ce1ffb9133",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Tool call

_source line 1351 · 2026-05-21T03:23:03.338Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_reply_to_user · `toolu_017bBEHVt3kTpXhYJB9SSKSY`</summary>

```json
{
  "text": "目前不需要你提供任何东西，实验和分析都在自动推进。\n\n唯一可能需要你帮忙的：**exp-003 的第二种 GPU**。已催 Manager 3 次，还没回复。如果你能直接开一台 AutoDL A100/H100 实例（2 卡，预估用 60h，¥210-360），可以加速 Claim 2（multi-hardware separability）。没有的话 Claim 2 scope 到 precision-only，论文仍然成立，只是贡献度降一档。\n\n不急——等 Manager 回复也行。其他一切正常运转。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b1c65a2-7fc3-4e88-9c7d-f8ce1ffb9133",
  "isSidechain": false,
  "requestId": "req_011CbEzmfMz356qvNnzP4Ejk",
  "type": "assistant",
  "uuid": "cf68475b-921e-4f74-8407-ad0fb9dea1e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDji4HWygvXYrHDecsoTmG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 66,
      "cache_read_input_tokens": 116118,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 66,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 248,
          "cache_read_input_tokens": 116118,
          "cache_creation_input_tokens": 66,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 66
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1352 · 2026-05-21T03:23:06.342Z_

<details><summary>↩ Tool result · `toolu_017bBEHVt3kTpXhYJB9SSKSY`</summary>

```text
{"result":"{\"success\": true}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf68475b-921e-4f74-8407-ad0fb9dea1e8",
  "isSidechain": false,
  "promptId": "3b8d4cc7-74a9-47a9-8a1d-0343edadbcc4",
  "type": "user",
  "uuid": "538b11ec-9234-4cca-a4e7-21d6e7cb89ee",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true}"
    }
  },
  "sourceToolAssistantUUID": "cf68475b-921e-4f74-8407-ad0fb9dea1e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Runtime record

_source line 1353_

```json
{
  "type": "ai-title",
  "aiTitle": "Bootstrap NLP variance G-theory MVP",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


### Runtime record

_source line 1354 · 2026-05-21T03:48:42.983Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:48:42.983Z",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "content": "[Reviewer 回复]:\n## 审查报告 — Llama single-model G-study (exp-001 首次分析)\n\n**结论**: WARNING — binary_correct 结果稳固，但 text_exact_match G=0.007 需要谨慎解读，可能导致 Claim 3 叙事方向变化\n\n### 独立核实\n\n直接读取了远程 `results/analysis/llama_single_model_gstudy.json`，确认所有数值与 worker 报告一致。239,200 records, 1,196 conditions, 200 items。\n\n### 发现\n\n**A. binary_correct — 强力支撑 Claims 1 & 2**\n\n- [severity: info] **item_id 主导地位稳固**：61.1% (MVP: 58.4%)，200 items × 6 facets 规模下确认。这是 Claim 1 在 MMLU-Llama 上的核心证据。\n\n- [severity: info] **Conditional separability 确认**：所有直接 infra×method 交互 < 0.1%（precision:temperature=0.05%, precision:prompt=0.01%, precision:seed=0.002%）。比 MVP 更加确定。Claim 2 binary scoring 下成立。\n\n- [severity: info] **Facet×item 交互浮现**：seed:item_id=4.7%, prompt:item_id=4.6%, precision:item_id=4.2%。MVP 中受 50 items 限制信号不足，200 items 后清晰。这支持 \"item-conditional effects\" 叙事——每个 facet 的效应取决于具体 item。\n\n**B. text_exact_match — 需要重要的分析补充**\n\n- [severity: warning] **G=0.007 是真实现象但需要分层解读**。temperature 占 79.7% 方差，驱动 G 崩溃。原因明确：T=0.7 下文本匹配近乎随机（grand_mean=0.331 说明仅 1/3 的 text responses 在同 condition 内一致）。MVP 的 G=0.975 是在 T=0.0+T=0.5 下计算的，温度范围扩展后 G 剧变。\n\n  **这不是 bug，但在论文中不能直接报 \"G dropped from 0.975 to 0.007\"，因为实验设计不同。** 建议增加分析：\n  1. **按温度分层计算 G** — 分别报 T=0.0 / T=0.3 / T=0.7 的 text_exact_match G coefficient。预期 T=0.0 下 G 接近 1.0（确定性输出），T=0.7 下接近 0（随机文本）。这能精确展示 \"metric×temperature 交互\" 的机制。\n  2. **binary vs text G 对比表**（按温度分层），作为 Claim 3 的核心 table。\n\n- [severity: warning] **precision:temperature = 4.15%（MVP: 1.3%）**。这个交互扩大了 3x，符合 Messina 浮点非结合性机制（higher temp → more fp operations → more precision divergence in text）。但 4.15% 意味着 Claim 2 \"separability\" 在 text metric 下进一步弱化。paper_framing.md 当前说 \"<0.5% under binary\"——需要同时明确报告 text metric 下 4.15% 且解释机制。\n\n**C. D-study**\n\n- [severity: info] **G>0.8 需要 ~510 items**（binary_correct，全 facets random）。这是 Claim 3 的关键数字。但注意：这假设所有 facets 都是 random 的。实践中研究者通常固定 temperature 和 precision，只变化 prompt/seed/item。建议补充 \"实践场景 D-study\"：固定 precision+temperature，只 prompt/seed/ordering/item 为 random facets，预计 item 需求会大幅降低。\n\n### 对论文叙事的影响评估\n\n1. **Claim 1 (item dominance)**: ✅ 强化。61.1% 在 Llama-only、200 items 下确认。待 model-as-facet 后可能下降（model:item_id 会吸收部分 item_id 方差）。\n2. **Claim 2 (separability)**: ✅ binary 下更加确定。⚠️ text 下 precision:temperature=4.15% 需要更细致的叙述。\n3. **Claim 3 (metric-conditional budgets)**: ⚠️ 需要重新设计呈现方式。不能简单报 \"binary G=0.61, text G=0.007\" 而不解释 temperature range 差异。建议以 temperature-stratified G coefficient table 为核心展示。"
}
```

---


### Runtime record

_source line 1355 · 2026-05-21T03:48:42.984Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:48:42.984Z",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


## Round 171

## Round 171

2 recorded events


### User

_source line 1356 · 2026-05-21T03:48:42.968Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "538b11ec-9234-4cca-a4e7-21d6e7cb89ee",
  "isSidechain": false,
  "promptId": "5468e520-2d98-41a4-a2e7-f0047192a341",
  "type": "user",
  "isMeta": true,
  "uuid": "9aeb358a-cfb4-4732-bbe2-44a6260272c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Assistant

_source line 1357 · 2026-05-21T03:48:42.972Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9aeb358a-cfb4-4732-bbe2-44a6260272c4",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "3b89279f-465e-4396-b1ab-69fe4b0c17b2",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "id": "cbe48ecb-eebe-469b-b3da-b1efc50b5b1e",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 172

## Round 172

13 recorded events


### User

_source line 1358 · 2026-05-21T03:48:43.130Z_

[Reviewer 回复]:
## 审查报告 — Llama single-model G-study (exp-001 首次分析)

**结论**: WARNING — binary_correct 结果稳固，但 text_exact_match G=0.007 需要谨慎解读，可能导致 Claim 3 叙事方向变化

### 独立核实

直接读取了远程 `results/analysis/llama_single_model_gstudy.json`，确认所有数值与 worker 报告一致。239,200 records, 1,196 conditions, 200 items。

### 发现

**A. binary_correct — 强力支撑 Claims 1 & 2**

- [severity: info] **item_id 主导地位稳固**：61.1% (MVP: 58.4%)，200 items × 6 facets 规模下确认。这是 Claim 1 在 MMLU-Llama 上的核心证据。

- [severity: info] **Conditional separability 确认**：所有直接 infra×method 交互 < 0.1%（precision:temperature=0.05%, precision:prompt=0.01%, precision:seed=0.002%）。比 MVP 更加确定。Claim 2 binary scoring 下成立。

- [severity: info] **Facet×item 交互浮现**：seed:item_id=4.7%, prompt:item_id=4.6%, precision:item_id=4.2%。MVP 中受 50 items 限制信号不足，200 items 后清晰。这支持 "item-conditional effects" 叙事——每个 facet 的效应取决于具体 item。

**B. text_exact_match — 需要重要的分析补充**

- [severity: warning] **G=0.007 是真实现象但需要分层解读**。temperature 占 79.7% 方差，驱动 G 崩溃。原因明确：T=0.7 下文本匹配近乎随机（grand_mean=0.331 说明仅 1/3 的 text responses 在同 condition 内一致）。MVP 的 G=0.975 是在 T=0.0+T=0.5 下计算的，温度范围扩展后 G 剧变。

  **这不是 bug，但在论文中不能直接报 "G dropped from 0.975 to 0.007"，因为实验设计不同。** 建议增加分析：
  1. **按温度分层计算 G** — 分别报 T=0.0 / T=0.3 / T=0.7 的 text_exact_match G coefficient。预期 T=0.0 下 G 接近 1.0（确定性输出），T=0.7 下接近 0（随机文本）。这能精确展示 "metric×temperature 交互" 的机制。
  2. **binary vs text G 对比表**（按温度分层），作为 Claim 3 的核心 table。

- [severity: warning] **precision:temperature = 4.15%（MVP: 1.3%）**。这个交互扩大了 3x，符合 Messina 浮点非结合性机制（higher temp → more fp operations → more precision divergence in text）。但 4.15% 意味着 Claim 2 "separability" 在 text metric 下进一步弱化。paper_framing.md 当前说 "<0.5% under binary"——需要同时明确报告 text metric 下 4.15% 且解释机制。

**C. D-study**

- [severity: info] **G>0.8 需要 ~510 items**（binary_correct，全 facets random）。这是 Claim 3 的关键数字。但注意：这假设所有 facets 都是 random 的。实践中研究者通常固定 temperature 和 precision，只变化 prompt/seed/item。建议补充 "实践场景 D-study"：固定 precision+temperature，只 prompt/seed/ordering/item 为 random facets，预计 item 需求会大幅降低。

### 对论文叙事的影响评估

1. **Claim 1 (item dominance)**: ✅ 强化。61.1% 在 Llama-only、200 items 下确认。待 model-as-facet 后可能下降（model:item_id 会吸收部分 item_id 方差）。
2. **Claim 2 (separability)**: ✅ binary 下更加确定。⚠️ text 下 precision:temperature=4.15% 需要更细致的叙述。
3. **Claim 3 (metric-conditional budgets)**: ⚠️ 需要重新设计呈现方式。不能简单报 "binary G=0.61, text G=0.007" 而不解释 temperature range 差异。建议以 temperature-stratified G coefficient table 为核心展示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b89279f-465e-4396-b1ab-69fe4b0c17b2",
  "isSidechain": false,
  "promptId": "5468e520-2d98-41a4-a2e7-f0047192a341",
  "type": "user",
  "uuid": "c1e96b4f-7144-458e-a6af-5df8112f8584",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Runtime record

_source line 1359 · 2026-05-21T03:48:43.129Z_

```json
{
  "parentUuid": "c1e96b4f-7144-458e-a6af-5df8112f8584",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "802dcfaf-8561-404e-8608-113c12234e97",
  "timestamp": "2026-05-21T03:48:43.129Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

---


### Assistant

_source line 1360 · 2026-05-21T03:48:55.263Z_

<details><summary>Logged reasoning block</summary>

```text
This is an important analysis result. Let me process the key findings:

**Binary correct results:**
- item_id = 61.1% (confirms Claim 1)
- All infra×method interactions < 0.1% (confirms Claim 2 under binary)
- facet×item interactions: seed:item=4.7%, prompt:item=4.6%, precision:item=4.2%
- G>0.8 needs ~510 items

**Text exact match results:**
- G = 0.007 (collapsed from MVP's 0.975)
- temperature = 79.7% of variance (because T=0.7 makes text matching nearly random)


- precision:temperature = 4.15% (up from 1.3% in MVP due to the expanded temperature range in this experiment)

The reviewer's suggestions are solid—I need to add temperature-stratified analysis for the text metric, create a comparison table showing how G differs across temperature levels, run a practical D-study with precision and temperature fixed, and clarify Claim 2 for text with that 4.15% interaction effect.

The 4.15% precision-temperature interaction is actually quite meaningful for the story we're telling. I should queue up these additional analyses with the Agent and note the adjustments needed for Claim 3's presentation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "802dcfaf-8561-404e-8608-113c12234e97",
  "isSidechain": false,
  "requestId": "req_011CbF2jwYFFTbTC1C9JbqTC",
  "type": "assistant",
  "uuid": "34aa307c-ccee-4efb-a221-bd14016c88eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019X7mfprcZK1q8YgDxpW7p5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1497,
      "cache_read_input_tokens": 116456,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1497,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 478,
          "cache_read_input_tokens": 116456,
          "cache_creation_input_tokens": 1497,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1497
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 1361 · 2026-05-21T03:48:55.349Z_

Reviewer 发现关键：text G=0.007 不是 bug 而是 temperature range 扩展导致。需要温度分层分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34aa307c-ccee-4efb-a221-bd14016c88eb",
  "isSidechain": false,
  "requestId": "req_011CbF2jwYFFTbTC1C9JbqTC",
  "type": "assistant",
  "uuid": "1ddfe00a-43cf-475a-84a2-f33ee74241aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019X7mfprcZK1q8YgDxpW7p5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1497,
      "cache_read_input_tokens": 116456,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1497,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 478,
          "cache_read_input_tokens": 116456,
          "cache_creation_input_tokens": 1497,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1497
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 1362 · 2026-05-21T03:48:55.731Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_agent_queue_status · `toolu_01NCMmhjeQ4N3hPuuPxuzFzE`</summary>

```json
{
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ddfe00a-43cf-475a-84a2-f33ee74241aa",
  "isSidechain": false,
  "requestId": "req_011CbF2jwYFFTbTC1C9JbqTC",
  "type": "assistant",
  "uuid": "caf3a5ad-1005-4a66-aa8c-9acff79ffeaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019X7mfprcZK1q8YgDxpW7p5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1497,
      "cache_read_input_tokens": 116456,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1497,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 478,
          "cache_read_input_tokens": 116456,
          "cache_creation_input_tokens": 1497,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1497
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1363 · 2026-05-21T03:48:55.765Z_

<details><summary>↩ Tool result · `toolu_01NCMmhjeQ4N3hPuuPxuzFzE`</summary>

```text
{"result":"{\"found\":true,\"processing\":true,\"depth\":1,\"current\":{\"source\":\"worker:done\",\"preview\":\"[WORKER DONE] Worker worker_exp_gpu_status_mistral_launch_20260521T032003 已完成（status=done）。用 `get_worker_status('worker_\"},\"pending\":[{\"source\":\"worker:done\",\"preview\":\"[WORKER DONE] Worker worker_analysis_llama_single_gstudy_20260521T034025 已完成（status=done）。用 `get_worker_status('worker_a\",\"queued_at\":1779335171.1659102}],\"idle_seconds\":562}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caf3a5ad-1005-4a66-aa8c-9acff79ffeaa",
  "isSidechain": false,
  "promptId": "5468e520-2d98-41a4-a2e7-f0047192a341",
  "type": "user",
  "uuid": "c7b45753-37ec-47b5-86b5-5a2ad9175bb1",
  "toolUseResult": "{\"result\":\"{\\\"found\\\":true,\\\"processing\\\":true,\\\"depth\\\":1,\\\"current\\\":{\\\"source\\\":\\\"worker:done\\\",\\\"preview\\\":\\\"[WORKER DONE] Worker worker_exp_gpu_status_mistral_launch_20260521T032003 已完成（status=done）。用 `get_worker_status('worker_\\\"},\\\"pending\\\":[{\\\"source\\\":\\\"worker:done\\\",\\\"preview\\\":\\\"[WORKER DONE] Worker worker_analysis_llama_single_gstudy_20260521T034025 已完成（status=done）。用 `get_worker_status('worker_a\\\",\\\"queued_at\\\":1779335171.1659102}],\\\"idle_seconds\\\":562}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"found\":true,\"processing\":true,\"depth\":1,\"current\":{\"source\":\"worker:done\",\"preview\":\"[WORKER DONE] Worker worker_exp_gpu_status_mistral_launch_20260521T032003 已完成（status=done）。用 `get_worker_status('worker_\"},\"pending\":[{\"source\":\"worker:done\",\"preview\":\"[WORKER DONE] Worker worker_analysis_llama_single_gstudy_20260521T034025 已完成（status=done）。用 `get_worker_status('worker_a\",\"queued_at\":1779335171.1659102}],\"idle_seconds\":562}"
    }
  },
  "sourceToolAssistantUUID": "caf3a5ad-1005-4a66-aa8c-9acff79ffeaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Assistant

_source line 1364 · 2026-05-21T03:49:08.722Z_

<details><summary>Logged reasoning block</summary>

```text
Agent is processing the GPU status / Mistral launch worker and has the Llama G-study analysis worker done notification pending. Queue depth=1. Let me wait for Agent to process both before sending new instructions about temperature-stratified analysis. Or I can queue the instruction since it's important and won't conflict.

Actually, let me queue it - the temperature-stratified analysis is a new requirement that the Agent won't know about from the worker done notification alone.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7b45753-37ec-47b5-86b5-5a2ad9175bb1",
  "isSidechain": false,
  "requestId": "req_011CbF2kskZzr9cMiKxJAZu6",
  "type": "assistant",
  "uuid": "1e7c565f-c4fc-4725-a7d2-4196d1c2d379",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kRCzC3XggsAku4Vpz9tdD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 664,
      "cache_read_input_tokens": 117953,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 117953,
          "cache_creation_input_tokens": 664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 664
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 1365 · 2026-05-21T03:49:09.831Z_

Agent 正在处理 GPU/Mistral 切换 + Llama G-study 回调。排一条指令补充温度分层分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e7c565f-c4fc-4725-a7d2-4196d1c2d379",
  "isSidechain": false,
  "requestId": "req_011CbF2kskZzr9cMiKxJAZu6",
  "type": "assistant",
  "uuid": "5e1398b0-5898-4e6a-8829-9c910468e764",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kRCzC3XggsAku4Vpz9tdD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 664,
      "cache_read_input_tokens": 117953,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 117953,
          "cache_creation_input_tokens": 664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 664
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-21T03:49:23.937Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_main_agent · `toolu_01BU16Wwmzp28jcRUY7mf8hQ`</summary>

```json
{
  "text": "[Director 指令] Llama G-study 结果优秀 — 追加温度分层分析\n\n**binary_correct 结果确认 Claims 1&2**：item_id=61.1% ✅，infra×method <0.1% ✅。\n\n**text_exact_match G=0.007 需要分层处理**。Reviewer 分析：temperature 占 79.7% 方差是因为 T=0.7 下 text matching 近乎随机。这不是 bug，但论文不能直接报 \"G dropped from 0.975 to 0.007\"。\n\n**追加分析（1 个 Worker，CPU 任务）**：\n1. **按温度分层的 G coefficient**：分别计算 T=0.0 / T=0.3 / T=0.7 三组数据的 binary_correct G 和 text_exact_match G。预期 text G 在 T=0.0 接近 1.0，T=0.7 接近 0。\n2. **实践场景 D-study**：固定 precision + temperature（不作为 random facet），只让 prompt/seed/ordering/item 为 random。重新计算 G 和 \"达到 G≥0.80 需要多少 items\"——这更接近实际研究者的使用场景。\n3. **precision:temperature=4.15%**：比 MVP 的 1.3% 扩大 3x，在 text metric 下 Claim 2 separability 需更细致叙述。计算 binary 下的 precision:temperature 交互作为对比。\n\n保存到 `artifacts/analysis/temperature_stratified_analysis.json`。",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e1398b0-5898-4e6a-8829-9c910468e764",
  "isSidechain": false,
  "requestId": "req_011CbF2kskZzr9cMiKxJAZu6",
  "type": "assistant",
  "uuid": "1bbcc063-abf7-4fd3-840b-dbdb116b4578",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kRCzC3XggsAku4Vpz9tdD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 664,
      "cache_read_input_tokens": 117953,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 117953,
          "cache_creation_input_tokens": 664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 664
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 1367 · 2026-05-21T03:49:27.617Z_

<details><summary>↩ Tool result · `toolu_01BU16Wwmzp28jcRUY7mf8hQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"message_id\": \"om_x100b6fdc42a7f0a8b4c1b060183e9f5\", \"queued\": true, \"agent_busy\": true, \"agent_queue_depth\": 1, \"note\": \"Agent 正在处理之前的指令，你的消息已排队。Agent 会按顺序处理，当前指令完成后才能看到这条新消息。如果这条消息与之前的指令矛盾，请注意 Agent 可能已经按之前的指令执行了。\", \"agent_processing\": \"[WORKER DONE] Worker worker_exp_gpu_status_mistral_launch_20260521T032003 已完成（status=done）。用 `get_worker_status('worker_exp_gpu_status_mistral_launch_20260521T032003')` 读取结果，然后处理。\\n\\n- worker_id: worker\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bbcc063-abf7-4fd3-840b-dbdb116b4578",
  "isSidechain": false,
  "promptId": "5468e520-2d98-41a4-a2e7-f0047192a341",
  "type": "user",
  "uuid": "887eac96-f203-4a10-8ecb-71c9c3b5595a",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"message_id\\\": \\\"om_x100b6fdc42a7f0a8b4c1b060183e9f5\\\", \\\"queued\\\": true, \\\"agent_busy\\\": true, \\\"agent_queue_depth\\\": 1, \\\"note\\\": \\\"Agent 正在处理之前的指令，你的消息已排队。Agent 会按顺序处理，当前指令完成后才能看到这条新消息。如果这条消息与之前的指令矛盾，请注意 Agent 可能已经按之前的指令执行了。\\\", \\\"agent_processing\\\": \\\"[WORKER DONE] Worker worker_exp_gpu_status_mistral_launch_20260521T032003 已完成（status=done）。用 `get_worker_status('worker_exp_gpu_status_mistral_launch_20260521T032003')` 读取结果，然后处理。\\\\n\\\\n- worker_id: worker\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"message_id\": \"om_x100b6fdc42a7f0a8b4c1b060183e9f5\", \"queued\": true, \"agent_busy\": true, \"agent_queue_depth\": 1, \"note\": \"Agent 正在处理之前的指令，你的消息已排队。Agent 会按顺序处理，当前指令完成后才能看到这条新消息。如果这条消息与之前的指令矛盾，请注意 Agent 可能已经按之前的指令执行了。\", \"agent_processing\": \"[WORKER DONE] Worker worker_exp_gpu_status_mistral_launch_20260521T032003 已完成（status=done）。用 `get_worker_status('worker_exp_gpu_status_mistral_launch_20260521T032003')` 读取结果，然后处理。\\n\\n- worker_id: worker\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "1bbcc063-abf7-4fd3-840b-dbdb116b4578",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---


### Runtime record

_source line 1368_

```json
{
  "type": "ai-title",
  "aiTitle": "Bootstrap NLP variance G-theory MVP",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


### Runtime record

_source line 1369 · 2026-05-21T04:03:29.681Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T04:03:29.681Z",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "content": "[Reviewer 回复]:\n## 审查报告 — Fixed vs Random sensitivity analysis\n\n**结论**: PASS — 方法论稳健性确认，增强论文防御力\n\n### 发现\n\n- [severity: info] **binary_correct G 对 fixed/random 假设不敏感 (0.611-0.664)**。这是关键的防御性证据。无论 reviewer 如何质疑 temperature/precision/ordering 应为 fixed 还是 random，item dominance (61.1%) 和 binary 评估的中等可靠性结论不变。Δ最大仅 0.053 (all_random → three_fixed)。\n\n- [severity: info] **text_exact_match 在所有假设下 G<0.07**。即使将 temperature 设为 fixed (G=0.045) 或三个 facet 都 fixed (G=0.061)，text_exact_match 仍然不可靠。这与 MVP 的 G=0.975 形成强烈对比，明确说明 text metric 的可靠性在 3-temperature 设计下崩溃，与 MVP 的 2-temperature 设计不可直接比较。\n\n- [severity: info] **可直接纳入论文 Discussion/Appendix**。这组数据完美回答 reviewer concern \"你们的 facet 分类选择是否影响结论？\"——答案是 \"binary 下不影响，text 下都不行\"。\n\n### 仍需补充的分析（重申上次建议）\n\n**Temperature-stratified G coefficient 仍未做**。当前分析展示了 fixed/random 敏感度，但未展示**按温度水平分层**的 G coefficient。这是不同的分析：\n- Fixed/random 分析：将 temperature 从 error term 移到 universe score\n- 分层分析：在 T=0.0 / T=0.3 / T=0.7 各自子集上独立计算 5-facet G-study\n\n分层分析的价值：能精确展示 text_exact_match 从 T=0.0 (预期 G≈1.0) 到 T=0.7 (预期 G≈0) 的退化曲线，解释为何实践中 T=0 下 text matching 有效但 T>0 无效。这比 fixed/random 分析更直观，更适合 Figures/Main text。"
}
```

---


### Runtime record

_source line 1370 · 2026-05-21T04:03:29.682Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T04:03:29.682Z",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec"
}
```

---


## Round 173

## Round 173

2 recorded events


### User

_source line 1371 · 2026-05-21T04:03:29.664Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "887eac96-f203-4a10-8ecb-71c9c3b5595a",
  "isSidechain": false,
  "promptId": "483495cc-9d6f-4922-9d5b-9a21396234c6",
  "type": "user",
  "isMeta": true,
  "uuid": "47f11c65-6f20-43d9-87a9-8115675afe8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "10a54869-31d0-4dae-bcb8-806914c682ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-greeting-unicorn"
}
```

</details>

---
